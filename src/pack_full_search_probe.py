'''Pack a verified full FP32 corpus into bounded, isolated int8 runtime assets.

The original FP32 corpus is retained for evaluation. This output is neither a
production publication nor evidence that quantization meets a quality gate.
'''

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import struct

import numpy as np

from build_agent_index import (
    BuildError, canonical_json, embedding_signature, build_signature,
    load_embed, sha256_hex, vector_id,
)

ROW_BYTES = 128
SHARD_ROWS = 4096
MAX_ASSET_BYTES = 24 * 1024 * 1024
FIXTURE_GENERATOR = 'modular-normalized-fp32-v1'


def file_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()


def require(condition, message):
    if not condition:
        raise BuildError(message)


def safe_path(root: Path, relative: str) -> Path:
    require(isinstance(relative, str) and relative and '\\' not in relative
            and not relative.startswith('/')
            and all(part not in ('', '.', '..')
                    for part in relative.split('/')), 'Unsafe asset path')
    path = root / relative
    require(path.resolve().is_relative_to(root.resolve()), 'Escaping asset path')
    return path


def geometry_vectors(indices, dimensions: int, seed: int):
    """Deterministic test vectors only; bounded to the requested row batch."""
    rows = np.asarray(indices, dtype=np.int64).reshape(-1, 1)
    columns = np.arange(dimensions, dtype=np.int64).reshape(1, -1)
    values = ((rows * 37 + columns * 19 + seed) % 255 - 127).astype(np.float64)
    values /= np.linalg.norm(values, axis=1, keepdims=True)
    return values.astype('<f4')


def quantize_rows(values):
    """Shared real/fixture transform: row-maxabs int8 plus exact inverse norms."""
    values = np.asarray(values, dtype=np.float64)
    require(values.ndim == 2 and values.shape[1] == 768
            and np.isfinite(values).all()
            and np.max(np.abs(np.linalg.norm(values, axis=1) - 1)) <= 1e-4,
            'FP32 vectors must be finite and L2 normalized')
    integers = np.rint(values * (127 / np.max(np.abs(values), axis=1, keepdims=True))).astype(np.int8)
    norms = 1 / np.linalg.norm(integers.astype(np.float64), axis=1)
    return integers, norms.astype('<f8')


def pack(source: Path, output: Path, *, geometry_fixture: bool = False,
         seed: int = 17) -> dict:
    source, output = Path(source), Path(output)
    require(type(geometry_fixture) is bool, 'Fixture mode must be explicit boolean')
    require(source.resolve() != output.resolve(), 'Output must differ from source')
    require(not output.exists() or not any(output.iterdir()),
            'Output must be empty; use a fresh version directory')
    source_bytes = (source / 'probe.json').read_bytes()
    source_hash = hashlib.sha256(source_bytes).hexdigest()
    manifest = json.loads(source_bytes)
    embed = load_embed()
    require(manifest.get('kind') == 'full-corpus'
            and manifest.get('synthetic') is False
            and manifest.get('publication_ready') is False
            and manifest.get('slot') == 'full-probe', 'Not a full-corpus probe')
    require(manifest['embedding_signature'] == embedding_signature(embed)
            and manifest['build_signature'] == build_signature(embed),
            'Canonical signatures disagree with reader')
    require(isinstance(manifest.get('release_id'), str)
            and re.fullmatch(r'[0-9a-f]{64}', manifest['release_id']),
            'Invalid release identity')
    count, dimensions = manifest['passage_count'], manifest['dimensions']
    require(type(count) is int and 1 <= count <= 60000
            and type(dimensions) is int and dimensions == 768, 'Unsupported geometry')
    rows = manifest['rows']
    require(len(rows) == count and sha256_hex(canonical_json(rows))
            == manifest['rows_sha256'], 'Row count or checksum mismatch')
    require(isinstance(seed, int) and not isinstance(seed, bool)
            and 0 <= seed <= 2 ** 32 - 1, 'Invalid geometry seed')
    enc = manifest.get('embeddings') or {}
    if not geometry_fixture:
        require(enc.get('path') == 'vectors.f32'
                and enc.get('model_id') == embed['tokenizer']['id']
                and enc.get('model_revision') == embed['tokenizer']['revision']
                and enc.get('pooling') == 'cls'
                and enc.get('normalization') == 'l2'
                and enc.get('dtype') == 'float32'
                and enc.get('byte_order') == 'little'
                and enc.get('count') == count
                and enc.get('dimensions') == dimensions, 'Missing genuine FP32 encoder metadata')
        vector_path = source / 'vectors.f32'
        require(vector_path.stat().st_size == count * dimensions * 4
                and file_hash(vector_path) == enc.get('sha256')
                and manifest['files'].get('vectors.f32') == enc.get('sha256'),
                'FP32 file integrity mismatch')
    for relative, digest in manifest['files'].items():
        if relative != 'vectors.f32':
            require(file_hash(safe_path(source, relative)) == digest,
                    'Canonical asset checksum mismatch: ' + relative)
    prefix = 'releases/' + manifest['release_id']
    graph_path = prefix + '/graph.json'
    graph = json.loads((source / graph_path).read_bytes())
    paper_ids = manifest['paper_ids']
    require(paper_ids == sorted(set(paper_ids))
            and sorted(graph['nodes']) == paper_ids
            and sorted(graph['out']) == paper_ids
            and sorted(graph['in']) == paper_ids, 'Graph paper set mismatch')
    text_ids = manifest['text_paper_ids']
    require(text_ids == [pid for pid in paper_ids
                         if graph['nodes'][pid]['text']['available']],
            'Text availability mismatch')
    outgoing, incoming = [], []
    for pid in paper_ids:
        for edge in graph['out'][pid]:
            require(edge['target'] in graph['nodes'], 'Dangling graph edge')
            outgoing.append((pid, edge['target'], edge['evidence']))
        for edge in graph['in'][pid]:
            require(edge['source'] in graph['nodes'], 'Dangling graph edge')
            incoming.append((edge['source'], pid, edge['evidence']))
    require(sorted(outgoing) == sorted(incoming), 'Reverse graph mismatch')
    papers, expected_rows, paper_paths = {}, [], []
    for pid in text_ids:
        relative = prefix + '/papers/' + sha256_hex(pid) + '.json'
        paper_paths.append(relative)
        paper = json.loads((source / relative).read_bytes())
        require(paper['paper_id'] == pid and isinstance(paper['text'], str),
                'Invalid paper identity')
        card, text = graph['nodes'][pid]['text'], paper['text']
        require(card['code_points'] == len(text)
                and card['chunks'] == len(paper['chunks'])
                and card['object'] == sha256_hex(pid), 'Paper card mismatch')
        covered, previous = 0, -1
        for index, chunk in enumerate(paper['chunks']):
            start, end = chunk['start'], chunk['end']
            require(chunk['index'] == index and previous < start <= covered
                    and 0 <= start < end <= len(text)
                    and covered - start <= embed['overlap_code_points']
                    and end - start <= embed['max_code_points']
                    and 2 <= chunk['token_count'] <= embed['max_input_tokens'],
                    'Invalid canonical chunk range')
            passage = text[start:end]
            require(chunk['content_hash'] == sha256_hex(passage)
                    and chunk['input_hash'] == sha256_hex(canonical_json({
                        'embedding_signature': manifest['embedding_signature'],
                        'input': embed['passage_template'] + passage,
                    })), 'Canonical passage hash mismatch')
            expected_rows.append({
                'id': vector_id('full-probe', pid, index), 'paper_id': pid,
                'chunk_index': index, **{key: chunk[key] for key in (
                    'start', 'end', 'token_count', 'content_hash', 'input_hash')},
            })
            covered, previous = max(covered, end), start
        require(covered == len(text), 'Incomplete canonical paper')
        papers[pid] = paper
    require(rows == expected_rows, 'Rows disagree with canonical paper chunks')
    require(manifest['release_id'] == sha256_hex(canonical_json({
        'graph': manifest['files'][graph_path],
        'papers': sha256_hex(canonical_json(papers)),
        'build_signature': manifest['build_signature'],
        'embedding_signature': manifest['embedding_signature'],
    })), 'Canonical release identity mismatch')
    del papers

    output.mkdir(parents=True, exist_ok=True)
    files = {}

    def register(relative):
        path = output / relative
        require(path.stat().st_size <= MAX_ASSET_BYTES, 'Asset exceeds static limit')
        files[relative] = {'sha256': file_hash(path), 'bytes': path.stat().st_size}

    for relative in [graph_path, *paper_paths]:
        destination = output / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source / relative, destination)
        register(relative)

    order = sorted(range(count), key=lambda index: rows[index]['id'])
    require(len({row['id'] for row in rows}) == count, 'Duplicate vector IDs')
    ordinals = {pid: index for index, pid in enumerate(paper_ids)}
    with (output / 'metadata.bin').open('wb') as stream:
        for source_index in order:
            row = rows[source_index]
            stream.write(struct.pack('<32s6I32s32s8x', bytes.fromhex(row['id']),
                                     ordinals[row['paper_id']], row['chunk_index'],
                                     row['start'], row['end'], row['token_count'],
                                     source_index, bytes.fromhex(row['content_hash']),
                                     bytes.fromhex(row['input_hash'])))
    register('metadata.bin')
    vectors = None if geometry_fixture else np.memmap(
        vector_path, dtype='<f4', mode='r', shape=(count, dimensions))
    def vector_rows(indices):
        return geometry_vectors(indices, dimensions, seed) if geometry_fixture else vectors[indices]

    fixture_identity = None
    if geometry_fixture:
        checksum = hashlib.sha256()
        for first in range(0, count, SHARD_ROWS):
            checksum.update(vector_rows(list(range(first, min(first + SHARD_ROWS, count)))).tobytes())
        fixture_identity = {
            'generator': FIXTURE_GENERATOR, 'seed': seed,
            'count': count, 'dimensions': dimensions, 'dtype': 'float32',
            'byte_order': 'little', 'normalization': 'l2',
            'sha256': checksum.hexdigest(),
            'purpose': 'allocation-and-contract-testing-not-semantic-quality',
        }
    shards = []
    with (output / 'norms.f64').open('wb') as norm_file:
        for start in range(0, count, SHARD_ROWS):
            integers, norms = quantize_rows(vector_rows(order[start:start + SHARD_ROWS]))
            name = f'vectors-{start // SHARD_ROWS:04d}.i8'
            (output / name).write_bytes(integers.tobytes())
            norm_file.write(norms.astype('<f8').tobytes())
            register(name)
            shards.append({'path': name, 'start': start, 'count': len(integers)})
    register('norms.f64')
    # Reference FP32 rows preserve the envelope's explicit real/synthetic provenance.
    sample_sources = [i * (count - 1) // (min(count, 200) - 1)
                      for i in range(min(count, 200))] if count > 1 else [0]
    inverse_order = {original: packed for packed, original in enumerate(order)}
    (output / 'references.f32').write_bytes(
        np.asarray(vector_rows(sample_sources), dtype='<f4').tobytes())
    register('references.f32')
    packed = {
        'schema_version': 1, 'reader_schema': embed['reader_schema'],
        'kind': ('full-corpus-int8-geometry-fixture' if geometry_fixture else 'full-corpus-int8'),
        'synthetic': geometry_fixture, 'publication_ready': False,
        'scope': 'isolated-full-corpus-evaluation-not-production',
        'slot': 'full-probe', 'release_id': manifest['release_id'],
        'embedding_signature': manifest['embedding_signature'],
        'build_signature': manifest['build_signature'],
        'passage_count': count, 'dimensions': dimensions,
        'paper_ids': paper_ids, 'text_paper_ids': text_ids,
        'graph_path': graph_path, 'files': files,
        'source_manifest_sha256': source_hash,
        'source_rows_sha256': manifest['rows_sha256'],
        **({'fixture_vectors': fixture_identity} if geometry_fixture else {'source_embeddings': enc}),
        'metadata': {'path': 'metadata.bin', 'row_bytes': ROW_BYTES,
                     'order': 'vector-id-lexicographic'},
        'index': {'kind': 'exact-int8', 'quantization': 'per-row-maxabs-rint-127',
                  'norms_path': 'norms.f64', 'shards': shards},
        'compatibility': {'path': 'references.f32',
                          'indices': [inverse_order[i] for i in sample_sources],
                          'source_indices': sample_sources},
        'semantic_quality_gate': 'not-measured' if geometry_fixture else 'unverified',
        'workers_ai_compatibility': 'not-applicable-synthetic' if geometry_fixture else 'unverified',
    }
    (output / 'probe.json').write_text(canonical_json(packed), encoding='utf-8')
    return packed


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--geometry-fixture', action='store_true',
                        help='Synthetic allocation fixture; never an encoder or quality result')
    parser.add_argument('--seed', type=int, default=17)
    args = parser.parse_args(argv)
    try:
        result = pack(args.source, args.out, geometry_fixture=args.geometry_fixture, seed=args.seed)
    except (OSError, ValueError, KeyError, TypeError, BuildError) as exc:
        parser.exit(1, str(exc) + '\n')
    print(json.dumps({'output': str(args.out), 'passages': result['passage_count'],
                      'manifest_sha256': file_hash(args.out / 'probe.json'),
                      'asset_bytes': sum(item['bytes'] for item in result['files'].values()),
                      'synthetic': result['synthetic'], 'kind': result['kind']}))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
