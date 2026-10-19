'''Check probe geometry and real-text offsets, not search quality.'''

import hashlib
import json
import math
import struct

import pytest

from build_agent_index import clean_markdown
from build_agent_pages import slug
from build_static_search_probe import (
    CENTROIDS,
    DIMENSIONS,
    SUBQUANTIZERS,
    TEXT_PART_SIZE,
    build_probe,
)


def fixture():
    key = 'doi:10.example/unicode'
    nodes = [
        {'id': key, 'title': 'Paper 😀', 'url': 'https://example.org/paper'},
        {'id': 'url:no-text', 'title': 'Metadata', 'url': None},
    ]
    raw = ('# Method 😀\n\n' + 'αβγ 😀 $x$\n' * 3500
           + '\n## References\nBibliography entry\n'
           + '\n## Appendix A\nPreserved tail 😀')
    return {'nodes': nodes, 'edges': []}, {key: raw}, key


def test_deterministic_geometry_and_report_accounting(tmp_path):
    graph, texts, _ = fixture()
    first, second = tmp_path / 'first', tmp_path / 'second'
    manifest = build_probe(graph, texts, first, count=130, seed=42)
    assert build_probe(graph, texts, second, count=130, seed=42) == manifest
    files = sorted(path for path in first.rglob('*') if path.is_file())
    for path in files:
        other = second / path.relative_to(first)
        assert path.read_bytes() == other.read_bytes()
    assert manifest['asset_count'] == len(files)
    total_bytes = sum(path.stat().st_size for path in files)
    assert manifest['total_bytes'] == total_bytes
    assert manifest['codes']['bytes'] == 130 * SUBQUANTIZERS
    assert manifest['codebooks']['bytes'] == DIMENSIONS * CENTROIDS * 4
    for name in ('codes', 'codebooks'):
        data = (first / manifest[name]['path'].lstrip('/')).read_bytes()
        assert hashlib.sha256(data).hexdigest() == manifest[name]['sha256']
    codebooks = (first / 'probe/codebooks.bin').read_bytes()
    values = struct.unpack(f'<{DIMENSIONS * CENTROIDS}f', codebooks)
    assert all(math.isfinite(value) and abs(value) < 1 for value in values)
    report = json.loads((first / 'probe/measurements.json').read_text())
    assert report['synthetic'] is True
    assert report['semantic_quality_measured'] is False
    assert report['cloudflare_cpu_measured'] is False
    assert report['total_bytes'] == manifest['total_bytes']
    changed = build_probe(graph, texts, second, count=130, seed=43)
    assert changed['corpus_version'] != manifest['corpus_version']
    assert changed['codes']['sha256'] != manifest['codes']['sha256']


def test_parts_and_records_use_cleaned_unicode_code_points(tmp_path):
    graph, texts, key = fixture()
    manifest = build_probe(graph, texts, tmp_path, count=130)
    cleaned = clean_markdown(texts[key])
    paper = tmp_path / 'probe/papers' / slug(key)
    info = json.loads((paper / 'paperinfo.json').read_text())
    assert info['available'] is True
    assert info['total_length'] == len(cleaned)
    reconstructed = ''
    for part in range(1, info['part_count'] + 1):
        value = json.loads((paper / f'parts/{part}.json').read_text())
        assert value['offset'] == len(reconstructed)
        assert len(value['text']) <= TEXT_PART_SIZE
        reconstructed += value['text']
        last_part = part == info['part_count']
        expected_next = None if last_part else len(reconstructed)
        assert value['next_offset'] == expected_next
    assert reconstructed == cleaned
    assert 'Bibliography entry' not in reconstructed
    assert reconstructed.endswith('Preserved tail 😀')
    assert all(cleaned[heading['offset']:].startswith('#')
               for heading in info['sections'])
    records = []
    for shard in range(manifest['records']['shards']):
        records.extend(json.loads(
            (tmp_path / f'probe/records/{shard}.json').read_text(),
        ))
    assert [row['index'] for row in records] == list(range(130))
    for row in records:
        assert row['snippet'] == cleaned[row['start']:row['end']]
        assert row['part'] == row['start'] // TEXT_PART_SIZE + 1
        assert row['corpus_version'] == manifest['corpus_version']
        assert row['synthetic'] is True
    missing = tmp_path / 'probe/papers' / slug('url:no-text')
    card = json.loads((missing / 'paperinfo.json').read_text())
    assert card['available'] is False
    assert card['part_count'] == 0


def test_rebuild_preserves_unrelated_files_and_rejects_invalid_size(tmp_path):
    graph, texts, _ = fixture()
    (tmp_path / 'unrelated.txt').write_text('preserve')
    build_probe(graph, texts, tmp_path, count=130)
    build_probe(graph, texts, tmp_path, count=1)
    assert not (tmp_path / 'probe/records/1.json').exists()
    assert (tmp_path / 'unrelated.txt').read_text() == 'preserve'
    with pytest.raises(ValueError, match='positive'):
        build_probe(graph, texts, tmp_path, count=0)
    with pytest.raises(ValueError, match='25 MiB'):
        build_probe(graph, texts, tmp_path, count=1_000_000)
    with pytest.raises(ValueError, match='paper with text'):
        build_probe(graph, {}, tmp_path, count=1)
    for seed in (-1, 2 ** 53):
        with pytest.raises(ValueError, match='JavaScript-safe integer'):
            build_probe(graph, texts, tmp_path, count=1, seed=seed)


def test_small_shards_and_quantized_assets_share_row_identity(tmp_path):
    graph, texts, _ = fixture()
    manifest = build_probe(graph, texts, tmp_path, count=33)
    base = tmp_path / 'probe'
    rows = json.loads((base / 'records/0.json').read_text())
    small = [row for shard in range(manifest['records_small']['shards'])
             for row in json.loads((base / f'records16/{shard}.json').read_text())]
    assert small == rows
    vectors = b''.join((tmp_path / ref['path'].lstrip('/')).read_bytes()
                       for ref in manifest['int8'])
    norms = (base / 'int8-norms.bin').read_bytes()
    bits = (base / 'binary.bin').read_bytes()
    assert len(vectors) == 33 * DIMENSIONS
    assert len(norms) == 33 * 8
    assert len(bits) == 33 * DIMENSIONS // 8
    for row in range(33):
        values = struct.unpack_from(f'{DIMENSIONS}b', vectors,
                                    row * DIMENSIONS)
        inverse_norm = struct.unpack_from('<d', norms, row * 8)[0]
        assert math.sqrt(sum(v * v for v in values)) * \
            inverse_norm == pytest.approx(1)
        for dimension, value in enumerate(values):
            index = row * DIMENSIONS + dimension
            assert bool(bits[index // 8] & (1 << (index % 8))) == (value >= 0)
