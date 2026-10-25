'''Encoder integrity checks; fake vectors here are not semantic evidence.'''

import hashlib
import json
import math
import struct

import pytest

from build_agent_index import BuildError, canonical_json, load_embed, vector_id
from build_real_search_probe import build_subset, write_subset
import embed_real_search_probe as encode


@pytest.fixture
def subset(tmp_path):
    config = load_embed()
    paper_id = 'arxiv:2402.03300'
    graph = {'nodes': [{
        'id': paper_id, 'title': 'Fixture', 'authors': ['Author'],
        'section': 'Tests', 'kind': 'arxiv', 'url': 'https://example.test',
    }], 'edges': []}
    text = ('# Fixture\n\nCritic baseline. The KL coefficient is 0.04. '
            'Group size 64.\n\n' + 'Group 😀 baseline café 中文. ' * 60)
    release, probe = build_subset(
        graph, {paper_id: text}, config, seed_id=paper_id,
        minimum=1, target=1, maximum=10,
    )
    write_subset(release, probe, tmp_path)
    return tmp_path, config, release, probe


class FakeEncoder:
    '''Deterministic test double, never loaded by the encoder CLI.'''

    def __init__(self, identity='test-double-v1'):
        self.identity = {'implementation': identity}
        self.calls = []

    def __call__(self, texts):
        self.calls.append(texts)
        return [encode.unit_vector([3.0, 4.0] + [0.0] * 766)
                for _ in texts]


def mutate_manifest(root, mutation):
    path = root / 'probe.json'
    doc = json.loads(path.read_text())
    mutation(doc)
    path.write_text(canonical_json(doc))


def test_canonical_inputs_preserve_unicode_and_full_coverage(subset):
    root, config, release, _ = subset
    manifest, texts = encode.canonical_inputs(root, config)
    assert len(texts) == manifest['passage_count']
    assert any('😀' in text and 'café' in text for text in texts)
    for row, text in zip(manifest['rows'], texts):
        original = release['papers'][row['paper_id']]['text']
        assert text == original[row['start']:row['end']]


@pytest.mark.parametrize('mutation', [
    lambda m: m['rows'].pop(),
    lambda m: m['rows'].reverse(),
    lambda m: m['rows'][0].update(start=1),
    lambda m: m['rows'][0].update(content_hash='0' * 64),
    lambda m: m['rows'][0].update(input_hash='0' * 64),
    lambda m: m['rows'][0].update(token_count=513),
    lambda m: m['rows'][0].update(id='0' * 64),
    lambda m: m.update(embedding_signature='0' * 64),
    lambda m: m.update(synthetic=True),
])
def test_invalid_canonical_inputs_are_rejected(subset, mutation):
    root, config, _, _ = subset
    mutate_manifest(root, mutation)
    with pytest.raises(BuildError):
        encode.canonical_inputs(root, config)


def test_corrupted_asset_fails_before_encoding(subset):
    root, config, _, probe = subset
    graph_path = root / f'releases/{probe["release_id"]}/graph.json'
    graph_path.write_text('{}')
    encoder = FakeEncoder()
    with pytest.raises(BuildError, match='checksum'):
        encode.encode_probe(root, encoder, config, cache_dir=root / 'cache')
    assert not encoder.calls
    assert not (root / 'vectors.f32').exists()


@pytest.mark.parametrize('path', ['../secret', '/tmp/secret', 'a/../b', 'a\\b'])
def test_paths_cannot_escape_subset(tmp_path, path):
    with pytest.raises(BuildError, match='path'):
        encode.checked_path(tmp_path, path)


def test_cls_pooling_ignores_other_tokens_and_uses_fp32():
    first = [3.0, 4.0] + [0.0] * 766
    other = [100.0] * 768
    vector = encode.cls_vectors([[first, other]])[0]
    assert vector[:2] == list(struct.unpack('<2f', struct.pack('<2f', 0.6, 0.8)))
    assert vector[2:] == [0.0] * 766
    assert abs(math.sqrt(sum(x * x for x in vector)) - 1) < 1e-7


@pytest.mark.parametrize('values', [
    [0.0] * 768,
    [float('nan')] + [0.0] * 767,
    [float('inf')] + [0.0] * 767,
    [True] + [0.0] * 767,
    [1.0] * 767,
])
def test_invalid_model_vectors_fail(values):
    with pytest.raises(BuildError):
        encode.unit_vector(values)


def test_encoder_writes_le_fp32_and_reuses_matching_cache(subset):
    root, config, _, _ = subset
    cache = root / 'cache'
    encoder = FakeEncoder()
    first = encode.encode_probe(root, encoder, config,
                                cache_dir=cache, batch_size=2, progress=False)
    data = (root / 'vectors.f32').read_bytes()
    manifest = json.loads((root / 'probe.json').read_text())
    assert len(data) == first['passage_count'] * 768 * 4
    assert struct.unpack('<2f', data[:8]) == pytest.approx((0.6, 0.8))
    assert manifest['files']['vectors.f32'] == hashlib.sha256(data).hexdigest()
    assert manifest['embeddings']['workers_ai_compatibility'] == 'unverified'
    assert manifest['publication_ready'] is False
    same = FakeEncoder()
    second = encode.encode_probe(root, same, config,
                                 cache_dir=cache, progress=False)
    assert not same.calls
    assert second['cached'] == first['passage_count']
    assert second['vectors_sha256'] == first['vectors_sha256']
    changed = FakeEncoder('test-double-v2')
    third = encode.encode_probe(root, changed, config,
                                cache_dir=cache, progress=False)
    assert changed.calls
    assert third['encoded'] == first['passage_count']
    assert third['encoder_signature'] != first['encoder_signature']


@pytest.mark.parametrize('bad', [b'x', struct.pack('<768f', *([0.0] * 768)),
                                 struct.pack('<768f', float('nan'),
                                             *([0.0] * 767))])
def test_invalid_cache_never_silently_substitutes_vectors(tmp_path, bad):
    path = tmp_path / 'entry.f32'
    path.write_bytes(bad)
    with pytest.raises(BuildError):
        encode.cached_vector(path)


def test_full_corpus_requires_explicit_scope_and_preserves_canonical_order(subset, monkeypatch):
    root, config, _, _ = subset

    def full_manifest(manifest):
        manifest.update(
            kind='full-corpus', slot='full-probe',
            scope='isolated-full-corpus-evaluation-not-production',
            text_paper_ids=manifest['paper_ids'],
        )
        for row in manifest['rows']:
            row['id'] = vector_id('full-probe', row['paper_id'],
                                  row['chunk_index'])

    mutate_manifest(root, full_manifest)
    with pytest.raises(BuildError):
        encode.canonical_inputs(root, config)
    original, inputs = encode.canonical_inputs(root, config, full_corpus=True)
    stopped = FakeEncoder()
    with pytest.raises(BuildError, match='full-run-confirmed'):
        encode.encode_probe(root, stopped, config, cache_dir=root / 'cache', full_corpus=True)
    assert not stopped.calls
    import preflight_full_search_probe as preflight
    checked = []
    monkeypatch.setattr(preflight, 'verify_certificate', lambda *a, **kw: checked.append(kw))
    report = encode.encode_probe(
        root, FakeEncoder(), config, cache_dir=root / 'cache',
        full_corpus=True, length_bucketing=True, progress=False,
        full_run_confirmed=True, preflight_certificate=root / 'certificate.json',
        frozen_queries=root / 'frozen.json',
    )
    assert checked[0]['corpus'] == root
    after = json.loads((root / 'probe.json').read_text())
    assert report['full_corpus'] is True
    assert report['passage_count'] == len(inputs)
    assert after['rows'] == original['rows']
    mutate_manifest(root, lambda m: m.update(publication_ready=True))
    with pytest.raises(BuildError, match='scope'):
        encode.canonical_inputs(root, config, full_corpus=True)


def test_interrupted_encoding_resumes_validated_cache_without_partial_publish(
    subset,
):
    root, config, _, _ = subset
    original_manifest = (root / 'probe.json').read_bytes()

    class InterruptedEncoder(FakeEncoder):
        def __call__(self, texts):
            if self.calls:
                raise RuntimeError('Interrupted during the next batch')
            return super().__call__(texts)

    with pytest.raises(RuntimeError, match='Interrupted'):
        encode.encode_probe(root, InterruptedEncoder(), config,
                            cache_dir=root / 'cache', batch_size=1,
                            progress=False)
    assert (root / 'probe.json').read_bytes() == original_manifest
    assert not (root / 'vectors.f32').exists()
    resumed = FakeEncoder()
    report = encode.encode_probe(root, resumed, config,
                                 cache_dir=root / 'cache', batch_size=1,
                                 progress=False)
    assert report['cached'] >= 1
    assert report['encoded'] + report['cached'] == report['passage_count']
    assert len((root / 'vectors.f32').read_bytes()) == (
        report['passage_count'] * 768 * 4)


def test_query_vectors_use_config_template_and_stay_unverified(subset):
    root, config, _, _ = subset
    encoder = FakeEncoder()
    encode.encode_probe(root, encoder, config, cache_dir=root / 'cache',
                        progress=False)
    query_encoder = FakeEncoder()
    output = root / 'test-query-vectors.json'
    data = encode.encode_queries(root, query_encoder, config, output)
    assert data['kind'] == 'local-real-query-vectors'
    assert data['workers_ai_compatibility'] == 'unverified'
    assert data['queries'][0]['vector'] == pytest.approx(
        [0.6, 0.8] + [0.0] * 766)
    assert query_encoder.calls[0][0] == data['queries'][0]['query']
    assert 'test-query-vectors.json' not in json.loads(
        (root / 'probe.json').read_text())['files']


def test_batch_and_query_bounds_fail(subset):
    root, config, _, _ = subset
    with pytest.raises(BuildError, match='batch'):
        encode.encode_probe(root, FakeEncoder(), config,
                            cache_dir=root / 'cache', batch_size=0)
    with pytest.raises(BuildError, match='before integration'):
        encode.encode_queries(root, FakeEncoder(), config, root / 'queries.json')


def test_bge_refuses_truncation_without_calling_the_model(monkeypatch):
    # Exercise the production BGE call boundary without optional dependencies.
    encoder = object.__new__(encode.BgeEncoder)
    encoder.config = {'max_input_tokens': 512}
    encoder.tokenizer = type('Tokens', (), {
        'token_ids': lambda *args: list(range(513)),
    })()
    encoder._load_tokenizer = lambda: None
    encoder._load_model = lambda: pytest.fail('Model must not load for overlimit input')
    monkeypatch.setitem(__import__('sys').modules, 'torch', object())
    with pytest.raises(BuildError, match='truncate'):
        encoder(['input'])


def test_bge_refuses_hf_tokenizer_mismatch_before_model(monkeypatch):
    encoder = object.__new__(encode.BgeEncoder)
    encoder.config = {'max_input_tokens': 512}
    encoder.tokenizer = type('Tokens', (), {
        'token_ids': lambda *args: [101, 102],
    })()
    encoder.hf_tokenizer = lambda *_args, **_kwargs: {
        'input_ids': [[101, 999, 102]],
    }
    encoder._load_tokenizer = lambda: None
    encoder._load_model = lambda: pytest.fail('Model must not load for mismatched input')
    monkeypatch.setitem(__import__('sys').modules, 'torch', object())
    with pytest.raises(BuildError, match='token IDs differ'):
        encoder(['input'])


def test_late_hf_mismatch_checks_all_rows_before_any_inference_including_cache(subset):
    root, config, _, _ = subset
    # First populate genuine-shaped fixture caches; all inputs must still pass
    # tokenizer preflight on the next call even though none needs inference.
    first = FakeEncoder()
    encode.encode_probe(root, first, config, cache_dir=root / 'cache', progress=False)
    _, inputs = encode.canonical_inputs(root, config)
    original = (root / 'vectors.f32').read_bytes()

    class ValidatingFake(FakeEncoder):
        def validate_inputs(self, texts, **kwargs):
            assert texts == inputs
            for at, text in enumerate(texts):
                if at == len(texts) - 1:
                    raise BuildError('Canonical and pinned Hugging Face token IDs differ at final row')

    stopped = ValidatingFake()
    with pytest.raises(BuildError, match='final row'):
        encode.encode_probe(root, stopped, config, cache_dir=root / 'cache', progress=False)
    assert not stopped.calls
    assert (root / 'vectors.f32').read_bytes() == original


def test_production_tokenizer_late_batch_failure_does_not_load_weights():
    encoder = object.__new__(encode.BgeEncoder)
    encoder.config = {'max_input_tokens': 512}
    encoder.tokenizer_matches = 0
    encoder.model = None
    encoder._load_tokenizer = lambda: None
    encoder._load_model = lambda: pytest.fail('No model loads in all-input validation')
    encoder.tokenizer = type('Tokenizer', (), {'token_ids': lambda *args: [101, 102]})()
    encoder.hf_tokenizer = lambda values, **kwargs: {
        'input_ids': [[101, 999, 102] if value == 'bad-last' else [101, 102] for value in values]}
    with pytest.raises(BuildError, match='token IDs differ'):
        encoder.validate_inputs(['good'] * 129 + ['bad-last'], batch_size=32)
    assert encoder.tokenizer_matches == 128
    assert encoder.model is None


def test_swapped_valid_cache_vector_is_rejected(subset):
    root, config, _, _ = subset
    encoder = FakeEncoder()
    encode.encode_probe(root, encoder, config, cache_dir=root / 'cache', progress=False)
    signature = encode.sha256_hex(canonical_json(encoder.identity))
    entry = next((root / 'cache' / signature).glob('*.f32'))
    entry.write_bytes(encode.vector_bytes([1.0] + [0.0] * 767))
    other = FakeEncoder()
    with pytest.raises(BuildError, match='checksum'):
        encode.encode_probe(root, other, config, cache_dir=root / 'cache', progress=False)
    assert not other.calls


def test_incomplete_cache_data_without_sidecar_is_recomputed(tmp_path):
    path = tmp_path / 'incomplete.f32'
    path.write_bytes(encode.vector_bytes([1.0] + [0.0] * 767))
    assert encode.cached_vector(path, expected={'encoder_signature': 'new'}) is None
