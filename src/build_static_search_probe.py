'''Build deterministic synthetic PQ assets for a runtime feasibility probe.

Rankings have no semantic meaning. Paper metadata, snippets and text offsets
come from the real corpus, while the codes and codebooks are random fixtures.
No embedding model, network service or Cloudflare credentials are used.
'''

from __future__ import annotations

import argparse
import hashlib
import json
import math
import struct
import random
import shutil
import sys
from array import array
from pathlib import Path

from build_agent_index import canonical_json, clean_markdown
from build_agent_pages import headings, slug
from common import FULLTEXT_DIR, GRAPH, ROOT, safe_key

DIMENSIONS = 768
SUBQUANTIZERS = 96
CENTROIDS = 256
RECORD_SHARD_SIZE = 128
TEXT_PART_SIZE = 16000
CHUNK_SIZE = 800
CHUNK_STEP = 680
MAX_ASSETS = 20000
MAX_ASSET_BYTES = 25 * 1024 * 1024
DEFAULT_COUNT = 40575
DEFAULT_SEED = 20261019


def json_bytes(value: object) -> bytes:
    return (canonical_json(value) + '\n').encode('utf-8')


class AssetWriter:
    '''Enforce static-hosting limits on every published file.'''

    def __init__(self, output: Path):
        self.output = output
        self.sizes: dict[str, int] = {}

    def write(self, relative: str, data: bytes) -> dict:
        if len(data) > MAX_ASSET_BYTES:
            raise ValueError(f'Asset exceeds 25 MiB: {relative}')
        if relative not in self.sizes and len(self.sizes) >= MAX_ASSETS:
            raise ValueError('Probe exceeds the 20,000 static asset limit')
        path = self.output / 'probe' / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        self.sizes[relative] = len(data)
        return {
            'path': '/probe/' + relative,
            'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest(),
        }

    def json(self, relative: str, value: object) -> dict:
        return self.write(relative, json_bytes(value))


def synthetic_vectors(count: int, seed: int) -> tuple[bytes, bytes]:
    '''Emit row-major uint8 codes and little-endian float32 codebooks.'''
    rng = random.Random(seed)
    codes = bytes(rng.getrandbits(8) for _ in range(count * SUBQUANTIZERS))
    values = array('f', (
        rng.uniform(-1.0, 1.0) / DIMENSIONS ** 0.5
        for _ in range(DIMENSIONS * CENTROIDS)
    ))
    if values.itemsize != 4:
        raise RuntimeError('This platform has no 32-bit array floats')
    if sys.byteorder != 'little':
        values.byteswap()
    return codes, values.tobytes()


def build_probe(graph: dict, texts: dict[str, str | None], output: Path,
                count: int = DEFAULT_COUNT, seed: int = DEFAULT_SEED) -> dict:
    '''Publish only output/probe; all other output files are preserved.'''
    if count <= 0:
        raise ValueError('count must be positive')
    if count * SUBQUANTIZERS > MAX_ASSET_BYTES:
        raise ValueError('Requested codes exceed the 25 MiB asset limit')
    if not isinstance(seed, int) or not 0 <= seed <= 2 ** 53 - 1:
        raise ValueError('seed must be a nonnegative JavaScript-safe integer')
    nodes = sorted(graph['nodes'], key=lambda node: node['id'])
    if len({node['id'] for node in nodes}) != len(nodes):
        raise ValueError('Duplicate paper identifiers in the graph')
    cleaned = {node['id']: clean_markdown(texts.get(node['id']) or '')
               for node in nodes}
    if not any(text.strip() for text in cleaned.values()):
        raise ValueError('At least one paper with text is required')
    version = hashlib.sha256(json_bytes({
        'format': 'pq-ip-v1', 'graph': graph, 'seed': seed, 'count': count,
        'text_sha256': {key: hashlib.sha256(text.encode('utf-8')).hexdigest()
                        for key, text in cleaned.items()},
        'chunk_size': CHUNK_SIZE, 'chunk_step': CHUNK_STEP,
        'text_part_size': TEXT_PART_SIZE, 'probe_layout': 2,
    })).hexdigest()
    root = output / 'probe'
    if root.exists():
        shutil.rmtree(root)
    writer = AssetWriter(output)
    common = {'corpus_version': version, 'synthetic': True,
              'offset_unit': 'unicode_code_points'}
    papers, candidates = [], []
    for node in nodes:
        key = node['id']
        text = cleaned[key]
        available = bool(text.strip())
        prefix = f'papers/{slug(key)}'
        starts = range(0, len(text), TEXT_PART_SIZE) if available else []
        for part, start in enumerate(starts, 1):
            end = min(start + TEXT_PART_SIZE, len(text))
            writer.json(f'{prefix}/parts/{part}.json', common | {
                'paper_id': key, 'offset': start,
                'next_offset': end if end < len(text) else None,
                'total_length': len(text), 'text': text[start:end],
            })
        info = common | {
            'id': key, 'title': node['title'], 'url': node.get('url'),
            'section': node.get('section'), 'topic': node.get('topic'),
            'total_length': len(text), 'available': available,
            'sections': headings(text) if available else [],
            'part_count': len(starts),
        }
        writer.json(f'{prefix}/paperinfo.json', info)
        papers.append({k: v for k, v in info.items() if k != 'sections'} | {
            'path': f'/probe/{prefix}/paperinfo.json',
        })
        if available:
            chunks = range(0, len(text), CHUNK_STEP)
            for chunk_index, start in enumerate(chunks):
                end = min(start + CHUNK_SIZE, len(text))
                candidates.append(common | {
                    'paper_id': key, 'title': node['title'],
                    'url': node.get('url'), 'chunk_index': chunk_index,
                    'start': start, 'end': end, 'snippet': text[start:end],
                    'part': start // TEXT_PART_SIZE + 1,
                })
    for first in range(0, count, RECORD_SHARD_SIZE):
        rows = [candidates[i % len(candidates)] | {'index': i}
                for i in range(first, min(first + RECORD_SHARD_SIZE, count))]
        writer.json(f'records/{first // RECORD_SHARD_SIZE}.json', rows)
    for first in range(0, count, 16):
        rows = [candidates[i % len(candidates)] | {'index': i}
                for i in range(first, min(first + 16, count))]
        writer.json(f'records16/{first // 16}.json', rows)
    writer.json('papers.json', papers)
    codes, codebooks = synthetic_vectors(count, seed)
    # Quantize reconstructed *synthetic* PQ rows. This supports rerank/scan
    # CPU comparisons, not a quality claim about trained embeddings.
    books = struct.unpack(f'<{DIMENSIONS * CENTROIDS}f', codebooks)
    subvectors = [books[i:i + 8] for i in range(0, len(books), 8)]
    vector_files = []
    norms = bytearray()
    bits = bytearray()
    for first in range(0, count, 4096):
        packed = bytearray()
        for row in range(first, min(count, first + 4096)):
            vector = [value for sub in range(SUBQUANTIZERS)
                      for value in subvectors[
                          sub * CENTROIDS + codes[row * SUBQUANTIZERS + sub]]]
            scale = 127 / max(abs(value) for value in vector)
            integers = [round(value * scale) for value in vector]
            packed.extend(value & 255 for value in integers)
            norms.extend(struct.pack('<d', 1 / math.sqrt(
                sum(value * value for value in integers))))
            for pos in range(0, DIMENSIONS, 8):
                bits.append(sum((integers[pos + b] >= 0) << b
                                for b in range(8)))
        vector_files.append(writer.write(f'int8/{first // 4096}.bin', packed))
    int8_norms = writer.write('int8-norms.bin', norms)
    binary_bits = writer.write('binary.bin', bits)
    manifest = common | {
        'format': 'pq-ip-v1', 'dimensions': DIMENSIONS,
        'subquantizers': SUBQUANTIZERS, 'centroids': CENTROIDS,
        'count': count, 'seed': seed,
        'int8': vector_files, 'int8_norms': int8_norms, 'binary': binary_bits,
        'records_small': {'path': '/probe/records16/{shard}.json',
                          'shards': (count + 15) // 16},
        'codes': writer.write('codes.bin', codes),
        'codebooks': writer.write('codebooks.bin', codebooks),
        'papers': {'path': '/probe/papers.json', 'count': len(papers)},
        'nodes': len(nodes), 'record_shard_size': RECORD_SHARD_SIZE,
        'records': {'path': '/probe/records/{shard}.json',
                    'shards': (count + RECORD_SHARD_SIZE - 1)
                    // RECORD_SHARD_SIZE},
        'text_part_size': TEXT_PART_SIZE,
        'measurements': '/probe/measurements.json',
        'asset_count': 0, 'total_bytes': 0,
    }
    measurements = common | {
        'purpose': 'Runtime feasibility only; rankings are random.',
        'semantic_quality_measured': False,
        'cloudflare_cpu_measured': False,
        'count': count, 'source_chunks': len(candidates),
        'with_text': sum(paper['available'] for paper in papers),
        'codes_bytes': len(codes), 'codebooks_bytes': len(codebooks),
        'pq_bytes': len(codes) + len(codebooks),
        'max_asset_bytes': MAX_ASSET_BYTES, 'max_assets': MAX_ASSETS,
        'asset_count': 0, 'total_bytes': 0,
    }
    # Include both reports in their own totals; decimal lengths stabilize.
    for _ in range(8):
        writer.json('index.json', manifest)
        writer.json('measurements.json', measurements)
        totals = {'asset_count': len(writer.sizes),
                  'total_bytes': sum(writer.sizes.values())}
        if all(manifest[key] == value for key, value in totals.items()):
            return manifest
        manifest.update(totals)
        measurements.update(totals)
    raise RuntimeError('Asset accounting did not converge')


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'agent_probe')
    parser.add_argument('--count', type=int, default=DEFAULT_COUNT)
    parser.add_argument('--seed', type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    graph = json.loads(GRAPH.read_text(encoding='utf-8'))
    texts = {}
    for node in graph['nodes']:
        path = FULLTEXT_DIR / f'{safe_key(node["id"])}.md'
        texts[node['id']] = (
            path.read_text(encoding='utf-8') if path.exists() else None
        )
    print(f'Building {args.count:,} synthetic PQ records; no embeddings used.')
    result = build_probe(graph, texts, args.output, args.count, args.seed)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
