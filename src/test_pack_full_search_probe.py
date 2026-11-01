'''No-inference pack provenance, mapping and corruption regressions.'''
import hashlib
import json
import struct

import numpy as np
import pytest

from build_agent_index import BuildError, canonical_json, load_embed, sha256_hex
from build_full_search_probe import build_full_corpus, write_full_corpus
from pack_full_search_probe import geometry_vectors, pack, quantize_rows


@pytest.fixture
def source(tmp_path):
    ids = [f'paper-{index:02}' for index in range(10)]
    graph = {'nodes': [{'id': pid, 'title': pid, 'authors': [], 'kind': 'url', 'section': 'Tests',
                       'url': 'https://example.test/' + pid} for pid in ids], 'edges': []}
    texts = {pid: '# Evidence\n\n' + ('😀 Café [MASK] evidence within full paper. ' * 110)
             for pid in ids}
    release, manifest = build_full_corpus(graph, texts, load_embed())
    root = tmp_path / 'source'
    manifest = write_full_corpus(release, manifest, root)
    assert len(manifest['rows']) > 40
    return root, manifest, release


def test_fixture_is_honest_reproducible_and_preserves_mapping(source, tmp_path):
    root, original, release = source
    packed = pack(root, tmp_path / 'packed', geometry_fixture=True, seed=17)
    second = pack(root, tmp_path / 'again', geometry_fixture=True, seed=17)
    assert packed == second
    assert packed['synthetic'] is True
    assert packed['kind'] == 'full-corpus-int8-geometry-fixture'
    assert 'source_embeddings' not in packed
    assert packed['fixture_vectors']['generator'] == 'modular-normalized-fp32-v1'
    assert not (tmp_path / 'packed' / 'vectors.f32').exists()
    assert packed['paper_ids'] == original['paper_ids']
    count = original['passage_count']
    ordered = sorted(original['rows'], key=lambda row: row['id'])
    raw = (tmp_path / 'packed' / 'metadata.bin').read_bytes()
    for index, expected in enumerate(ordered):
        row = struct.unpack_from('<32s6I32s32s8x', raw, index * 128)
        assert row[0].hex() == expected['id']
        assert packed['paper_ids'][row[1]] == expected['paper_id']
        assert row[2:6] == tuple(expected[key] for key in ('chunk_index', 'start', 'end', 'token_count'))
        assert original['rows'][row[6]] == expected
        assert row[7].hex() == expected['content_hash']
        assert row[8].hex() == expected['input_hash']
    vectors = geometry_vectors(list(range(count)), 768, 17)
    assert hashlib.sha256(vectors.tobytes()).hexdigest() == packed['fixture_vectors']['sha256']
    order = sorted(range(count), key=lambda i: original['rows'][i]['id'])
    integers, norms = quantize_rows(vectors[order])
    actual = b''.join((tmp_path / 'packed' / shard['path']).read_bytes()
                      for shard in packed['index']['shards'])
    assert actual == integers.tobytes()
    assert (tmp_path / 'packed' / 'norms.f64').read_bytes() == norms.tobytes()
    references = np.fromfile(tmp_path / 'packed' / 'references.f32', dtype='<f4').reshape(-1, 768)
    np.testing.assert_array_equal(references, vectors[packed['compatibility']['source_indices']])
    for path in original['files']:
        if '/papers/' in path or path.endswith('/graph.json'):
            assert (root / path).read_bytes() == (tmp_path / 'packed' / path).read_bytes()


def test_real_pack_rejects_missing_encoder_and_fixture_as_source(source, tmp_path):
    root, _, _ = source
    with pytest.raises(BuildError, match='genuine FP32'):
        pack(root, tmp_path / 'real')
    pack(root, tmp_path / 'fixture', geometry_fixture=True)
    with pytest.raises(BuildError, match='Not a full-corpus'):
        pack(tmp_path / 'fixture', tmp_path / 'false-real')


@pytest.mark.parametrize('change', ['bytes', 'source-index', 'offset', 'missing'])
def test_rejects_corrupt_canonical_input(source, tmp_path, change):
    root, manifest, _ = source
    path = root / 'probe.json'
    if change == 'bytes':
        target = next(name for name in manifest['files'] if '/papers/' in name)
        (root / target).write_bytes((root / target).read_bytes() + b' ')
    elif change == 'missing':
        target = next(name for name in manifest['files'] if '/papers/' in name)
        (root / target).unlink()
    else:
        if change == 'offset': manifest['rows'][0]['end'] += 1
        else: manifest['rows'][0], manifest['rows'][1] = manifest['rows'][1], manifest['rows'][0]
        manifest['rows_sha256'] = sha256_hex(canonical_json(manifest['rows']))
        path.write_text(canonical_json(manifest))
    with pytest.raises((BuildError, OSError)):
        pack(root, tmp_path / 'bad', geometry_fixture=True)


def test_quantizer_rejects_nonfinite_zero_and_nonunit_rows():
    for values in [np.zeros((2, 768)), np.full((2, 768), np.nan), np.ones((2, 768))]:
        with pytest.raises(BuildError, match='finite and L2'):
            quantize_rows(values)


def test_quantizer_independent_round_to_even_and_normalization():
    values = np.zeros((1, 768), dtype=np.float64)
    values[0, :5] = [127, .5, 1.5, -.5, -1.5]
    values /= np.linalg.norm(values)
    integers, norms = quantize_rows(values)
    assert integers[0, :5].tolist() == [127, 0, 2, 0, -2]
    assert abs(norms[0] - 1 / (127 * 127 + 8) ** .5) < 1e-15


def test_rejects_unsafe_release_identity_before_derived_path_access(source, tmp_path):
    root, manifest, _ = source
    manifest['release_id'] = '../../outside'
    (root / 'probe.json').write_text(canonical_json(manifest))
    with pytest.raises(BuildError, match='release identity'):
        pack(root, tmp_path / 'output', geometry_fixture=True)
    assert not (tmp_path / 'output').exists()
