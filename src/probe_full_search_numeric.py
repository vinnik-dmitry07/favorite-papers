'''Bounded genuine-vector numerical contract; no model loading or network calls.'''
from __future__ import annotations

import argparse
import json
import math
import os
from pathlib import Path
import subprocess
import time

import numpy as np

from build_agent_index import BuildError, canonical_json, load_embed, sha256_hex, vector_id
from pack_full_search_probe import file_hash, quantize_rows, require

ROOT = Path(__file__).resolve().parents[1]


def run(source: Path, output: Path, work: Path) -> dict:
    started = time.monotonic()
    source, output, work = source.resolve(), output.resolve(), work.resolve()
    require(not work.exists() or not any(work.iterdir()), 'Numeric work directory must be empty')
    manifest_path = source / 'probe.json'
    manifest = json.loads(manifest_path.read_bytes())
    enc = manifest.get('embeddings') or {}
    config = load_embed()
    require(manifest.get('kind') == 'real-subset' and manifest.get('synthetic') is False
            and manifest.get('publication_ready') is False, 'Expected genuine isolated subset')
    count = manifest['passage_count']
    require(isinstance(count, int) and not isinstance(count, bool) and 50 <= count <= 500
            and manifest['dimensions'] == 768, 'Expected bounded 50..500 real rows')
    require(enc.get('model_id') == config['tokenizer']['id']
            and enc.get('model_revision') == config['tokenizer']['revision']
            and enc.get('pooling') == 'cls' and enc.get('normalization') == 'l2'
            and enc.get('dtype') == 'float32' and enc.get('byte_order') == 'little'
            and enc.get('path') == 'vectors.f32' and enc.get('dimensions') == 768
            and enc.get('count') == count, 'Genuine encoder identity mismatch')
    vectors_path = source / 'vectors.f32'
    vector_hash = file_hash(vectors_path)
    require(vectors_path.stat().st_size == count * 768 * 4
            and vector_hash == enc['sha256'] == manifest['files']['vectors.f32'],
            'Genuine FP32 bytes mismatch')
    rows = manifest['rows']
    require(len(rows) == count and len({row['id'] for row in rows}) == count
            and all(row['id'] == vector_id(manifest['slot'], row['paper_id'], row['chunk_index'])
                    for row in rows), 'Genuine source mapping mismatch')
    vectors = np.fromfile(vectors_path, dtype='<f4').reshape(count, 768)
    order = sorted(range(count), key=lambda index: rows[index]['id'])
    integers, norms = quantize_rows(vectors[order])
    # Independent scalar check of the transformation, not just the scan kernel.
    for packed_index, source_index in enumerate(order):
        values = [float(value) for value in vectors[source_index]]
        scale = 127 / max(abs(value) for value in values)
        expected = [round(value * scale) for value in values]
        require(integers[packed_index].tolist() == expected, 'Scalar quantization mismatch')
        expected_norm = 1 / math.sqrt(sum(value * value for value in expected))
        require(abs(float(norms[packed_index]) - expected_norm) <= 1e-15,
                'Scalar quantized normalization mismatch')
    sample = [i * (count - 1) // 31 for i in range(32)]
    work.mkdir(parents=True, exist_ok=True)
    (work / 'vectors.i8').write_bytes(integers.tobytes())
    (work / 'norms.f64').write_bytes(norms.tobytes())
    (work / 'queries.f32').write_bytes(vectors[sample].tobytes())
    descriptor = {'passage_count': count, 'dimensions': 768,
        'index': {'kind': 'exact-int8', 'quantization': 'per-row-maxabs-rint-127',
                  'norms_path': 'norms.f64', 'shards': [{'path': 'vectors.i8', 'start': 0, 'count': count}]},
        'source_rows': rows, 'packed_ids': [rows[i]['id'] for i in order], 'source_indices': order,
        'query_count': len(sample), 'query_source_indices': sample,
        'files': {name: file_hash(work / name) for name in ('vectors.i8', 'norms.f64', 'queries.f32')}}
    (work / 'numeric.json').write_text(canonical_json(descriptor))
    bundle = work / 'numeric.mjs'
    env = dict(os.environ)
    subprocess.run([str(ROOT / 'worker/node_modules/.bin/esbuild'),
                    str(ROOT / 'worker/probe-kernel/real-numeric.ts'), '--bundle', '--platform=node',
                    '--format=esm', '--outfile=' + str(bundle)],
                   cwd=ROOT, env=env, check=True, timeout=60, capture_output=True)
    intermediate = work / 'runtime.json'
    subprocess.run(['node', str(bundle), str(work), str(ROOT / 'worker/probe-kernel/scan.wasm'),
                    str(intermediate)], cwd=ROOT, env=env, check=True, timeout=60, capture_output=True)
    result = json.loads(intermediate.read_bytes())
    require(result.get('status') == 'PASS' and result.get('count') == count
            and all(result.get('checks', {}).values()), 'Actual runtime numeric checks failed')
    result['checks']['python_quantizer_oracle'] = True
    sources = ['src/pack_full_search_probe.py', 'src/probe_full_search_numeric.py',
               'worker/src/full-search-index.ts', 'worker/src/static-search-int8.ts',
               'worker/probe-kernel/scan.wat', 'worker/probe-kernel/scan.wasm',
               'worker/probe-kernel/real-numeric.ts']
    result.update({'kind': 'full-search-real-numeric',
        'source_manifest_sha256': file_hash(manifest_path), 'source_vectors_sha256': vector_hash,
        'source_rows_sha256': sha256_hex(canonical_json(rows)), 'synthetic': False,
        'source_encoder_signature': enc['encoder_signature'],
        'query_source': 'fixed-spread genuine passage vectors; numerical contract only',
        'source_embedding_signature': manifest['embedding_signature'],
        'current_embedding_signature_claim': 'not-established-by-this-numerical-probe',
        'source_sha256': {path: file_hash(ROOT / path) for path in sources},
        'numeric_input_sha256': file_hash(work / 'numeric.json'),
        'semantic_quality_gate': 'not-measured', 'workers_ai_compatibility': 'not-measured',
        'elapsed_seconds': time.monotonic() - started})
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(canonical_json(result) + '\n')
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--work-dir', type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        result = run(args.source, args.out, args.work_dir)
    except (BuildError, OSError, ValueError, KeyError, subprocess.SubprocessError) as exc:
        parser.exit(1, str(exc) + '\n')
    print(canonical_json({'status': result['status'], 'count': result['count'], 'output': str(args.out)}))


if __name__ == '__main__':
    main()
