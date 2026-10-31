'''Encoder integrity checks; fake vectors here are not semantic evidence.'''

import hashlib
import json
import math
import os
from pathlib import Path
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


def test_cache_records_producing_settings_without_relabelling_reused_rows(
    subset,
):
    root, config, _, _ = subset
    cache = root / 'cache'
    first = FakeEncoder()
    first.threads = 4
    report = encode.encode_probe(
        root, first, config, cache_dir=cache, batch_size=2,
        length_bucketing=True, progress=False,
    )
    namespace = cache / report['encoder_signature']
    before = {path.name: path.read_bytes()
              for path in namespace.glob('*.f32.json')}
    profiles = [json.loads(raw)['execution'] for raw in before.values()]
    assert profiles
    assert all(profile['threads'] == 4 and profile['batch_size'] == 2
               and profile['length_bucketing'] is True
               and 1 <= profile['actual_batch_size'] <= 2
               and profile['padded_tokens'] > 0 for profile in profiles)
    second = FakeEncoder()
    second.threads = 8
    reused = encode.encode_probe(
        root, second, config, cache_dir=cache, batch_size=8, progress=False,
    )
    assert not second.calls
    assert reused['execution_settings_requested']['threads'] == 8
    assert reused['cache_reuse_contract'] == (
        'semantic-identity-not-bitwise-equivalence'
    )
    assert {path.name: path.read_bytes()
            for path in namespace.glob('*.f32.json')} == before


def test_legacy_cache_execution_provenance_stays_unknown(tmp_path):
    signature, key = 'a' * 64, 'b' * 64
    path = tmp_path / signature / (key + '.f32')
    expected = {'encoder_signature': signature, 'input_hash': key}
    encode.write_cached_vector(
        path, [1.0] + [0.0] * 767, expected=expected,
    )
    sidecar = path.with_suffix('.f32.json')
    metadata = json.loads(sidecar.read_text())
    metadata.pop('execution')
    sidecar.write_text(json.dumps(metadata))
    before = sidecar.read_bytes()
    assert encode.recover_cached_vector(
        path, expected=expected, cache_root=tmp_path,
    ) is not None
    assert sidecar.read_bytes() == before
    assert 'execution' not in json.loads(sidecar.read_text())


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


def test_swapped_cache_vector_is_recomputed_after_validation(subset):
    root, config, _, _ = subset
    encoder = FakeEncoder()
    encode.encode_probe(root, encoder, config, cache_dir=root / 'cache', progress=False)
    signature = encode.sha256_hex(canonical_json(encoder.identity))
    entry = next((root / 'cache' / signature).glob('*.f32'))
    entry.write_bytes(encode.vector_bytes([1.0] + [0.0] * 767))
    other = FakeEncoder()
    report = encode.encode_probe(
        root, other, config, cache_dir=root / 'cache', progress=False,
    )
    assert other.calls
    assert report['encoded'] >= 1
    assert report['recovered_cache_entries'] == [
        {'input_hash': entry.stem, 'reason': 'BuildError'},
    ]
    assert encode.cached_vector(entry)[:2] == pytest.approx([0.6, 0.8])
    resumed = FakeEncoder()
    encode.encode_probe(
        root, resumed, config, cache_dir=root / 'cache', progress=False,
    )
    assert not resumed.calls


def test_full_run_does_not_repair_cache_before_admission(subset):
    root, config, _, _ = subset
    encoder = FakeEncoder()
    encode.encode_probe(
        root, encoder, config, cache_dir=root / 'cache', progress=False,
    )
    entry = next((root / 'cache').glob('*/*.f32'))
    entry.write_bytes(b'corrupted')
    stopped = FakeEncoder()
    with pytest.raises(BuildError, match='full-run-confirmed'):
        encode.encode_probe(
            root, stopped, config, cache_dir=root / 'cache',
            full_corpus=True, progress=False,
        )
    assert not stopped.calls
    assert entry.read_bytes() == b'corrupted'


@pytest.mark.parametrize('kind', [
    'length', 'checksum', 'zero_norm', 'nan', 'invalid_json', 'wrong_type',
    'invalid_unicode', 'metadata_too_large', 'missing_sidecar', 'missing_data',
])
def test_corrupt_managed_entries_become_misses(tmp_path, kind):
    signature, key = 'a' * 64, 'b' * 64
    path = tmp_path / signature / (key + '.f32')
    expected = {'encoder_signature': signature, 'input_hash': key}
    encode.write_cached_vector(
        path, [1.0] + [0.0] * 767, expected=expected,
    )
    sidecar = path.with_suffix('.f32.json')
    if kind == 'length':
        path.write_bytes(b'incomplete')
    elif kind == 'checksum':
        path.write_bytes(encode.vector_bytes([0.0, 1.0] + [0.0] * 766))
    elif kind in {'zero_norm', 'nan'}:
        values = [0.0] * 768
        if kind == 'nan':
            values[0] = float('nan')
        raw = struct.pack('<768f', *values)
        path.write_bytes(raw)
        metadata = json.loads(sidecar.read_text())
        metadata['vector_sha256'] = hashlib.sha256(raw).hexdigest()
        sidecar.write_text(json.dumps(metadata))
    elif kind == 'invalid_json':
        sidecar.write_text('{broken')
    elif kind == 'wrong_type':
        sidecar.write_text('[]')
    elif kind == 'invalid_unicode':
        sidecar.write_bytes(b'\xff')
    elif kind == 'metadata_too_large':
        sidecar.write_bytes(b' ' * 8193)
    elif kind == 'missing_sidecar':
        sidecar.unlink()
    else:
        path.unlink()
    temporary = path.with_suffix('.f32.tmp')
    temporary.write_bytes(b'incomplete')
    logs = []
    assert encode.recover_cached_vector(
        path, expected=expected, cache_root=tmp_path, recovery_log=logs,
    ) is None
    assert len(logs) == 1 and logs[0]['input_hash'] == key
    assert not path.exists() and not sidecar.exists()
    assert not temporary.exists()


@pytest.mark.parametrize(
    'kind', ['namespace', 'entry', 'sidecar', 'temporary'],
)
def test_cache_recovery_refuses_symlinks_without_deleting_anything(
    tmp_path, kind,
):
    root = tmp_path / 'cache'
    signature, key = 'a' * 64, 'b' * 64
    path = root / signature / (key + '.f32')
    expected = {'encoder_signature': signature, 'input_hash': key}
    protected = tmp_path / 'protected'
    protected.mkdir()
    target = protected / 'keep'
    target.write_text('preserve')
    if kind == 'namespace':
        root.mkdir()
        path.parent.symlink_to(protected, target_is_directory=True)
    else:
        path.parent.mkdir(parents=True)
        path.write_bytes(b'corrupted')
        link = {
            'entry': path,
            'sidecar': path.with_suffix('.f32.json'),
            'temporary': path.with_suffix('.f32.tmp'),
        }[kind]
        link.unlink(missing_ok=True)
        link.symlink_to(target)
    with pytest.raises(BuildError, match='managed|unsafe'):
        encode.recover_cached_vector(
            path, expected=expected, cache_root=root,
        )
    assert target.read_text() == 'preserve'
    if kind not in {'namespace', 'entry'}:
        assert path.read_bytes() == b'corrupted'


def test_cache_recovery_does_not_swallow_permission_errors(
    tmp_path, monkeypatch,
):
    signature, key = 'a' * 64, 'b' * 64
    path = tmp_path / signature / (key + '.f32')
    expected = {'encoder_signature': signature, 'input_hash': key}
    encode.write_cached_vector(
        path, [1.0] + [0.0] * 767, expected=expected,
    )

    def denied(*_args, **_kwargs):
        raise PermissionError('Cannot access cache')

    monkeypatch.setattr(encode, 'cached_vector', denied)
    with pytest.raises(PermissionError):
        encode.recover_cached_vector(
            path, expected=expected, cache_root=tmp_path,
        )
    assert path.exists() and path.with_suffix('.f32.json').exists()


def test_incomplete_cache_data_without_sidecar_is_recomputed(tmp_path):
    path = tmp_path / 'incomplete.f32'
    path.write_bytes(encode.vector_bytes([1.0] + [0.0] * 767))
    assert encode.cached_vector(path, expected={'encoder_signature': 'new'}) is None


@pytest.fixture
def numerical_sources(tmp_path):
    for name in encode.NUMERICAL_SYMBOLS:
        source = Path(encode.__file__).with_name(name)
        (tmp_path / name).write_bytes(source.read_bytes())
    return tmp_path


def test_cache_identity_ignores_comments_docs_and_unrelated_code(
    numerical_sources,
):
    before = encode.numerical_source_hashes(numerical_sources)
    path = numerical_sources / 'embed_real_search_probe.py'
    source = path.read_text()
    source = source.replace(
        'Use the first token only, never mean pooling over the sequence.',
        'Clarified documentation without numerical changes.',
    )
    source = source.replace(
        '''parser.add_argument('--threads', type=int, default=4)''',
        '''parser.add_argument('--threads', type=int, default=8)''',
    )
    path.write_text('# A harmless comment\n' + source)
    build = numerical_sources / 'build_agent_index.py'
    build.write_text(build.read_text() + '\nUNRELATED_REPORT_VERSION = 999\n')
    assert encode.numerical_source_hashes(numerical_sources) == before


@pytest.mark.parametrize('name,before,after', [
    ('build_agent_index.py', '''startswith('P')''', '''startswith('Z')'''),
    ('build_agent_index.py', 'end -= 1', 'end -= 2'),
    ('embed_real_search_probe.py', 'unit_vector(sequence[0])',
     'unit_vector(sequence[-1])'),
    ('embed_real_search_probe.py', 'attn_implementation=\'eager\'',
     'attn_implementation=\'sdpa\''),
])
def test_cache_identity_changes_with_numerical_code(
    numerical_sources, name, before, after,
):
    original = encode.numerical_source_hashes(numerical_sources)
    path = numerical_sources / name
    source = path.read_text()
    assert before in source
    path.write_text(source.replace(before, after))
    assert encode.numerical_source_hashes(numerical_sources) != original


def test_missing_numerical_symbol_fails_closed(numerical_sources):
    path = numerical_sources / 'build_agent_index.py'
    path.write_text(path.read_text().replace(
        'def _clean_table()', 'def _renamed_clean_table()',
    ))
    with pytest.raises(BuildError, match='source symbol'):
        encode.numerical_source_hashes(numerical_sources)


def test_encoder_identity_binds_config_model_and_dependency_versions(
    monkeypatch,
):
    versions = {'torch': 'test-1', 'transformers': 'test-1',
                'tokenizers': 'test-1'}
    monkeypatch.setattr(
        encode.importlib.metadata, 'version', versions.__getitem__,
    )
    config = load_embed()
    original = encode.encoder_identity(config)
    assert original['cache_schema'] == 2
    assert 'source_sha256' not in original['tokenizer_semantics']
    assert original['numerical_source_sha256']
    changed = json.loads(json.dumps(config))
    changed['tokenizer']['algorithm_version'] += 1
    assert encode.encoder_identity(changed) != original
    versions['torch'] = 'test-2'
    assert encode.encoder_identity(config) != original
    versions['torch'] = 'test-1'
    monkeypatch.setattr(encode, 'MODEL_REVISION', 'different-pinned-revision')
    assert encode.encoder_identity(config) != original


def cache_entry(cache, namespace, key, *, size=8, timestamp=1):
    directory = cache / namespace
    directory.mkdir(parents=True, exist_ok=True)
    vector = directory / (key + '.f32')
    vector.write_bytes(b'v' * size)
    sidecar = vector.with_suffix('.f32.json')
    sidecar.write_bytes(b'{}')
    for path in (vector, sidecar, directory):
        os.utime(path, (timestamp, timestamp))
    return vector


def test_cache_retention_keeps_active_and_one_recent_namespace(tmp_path):
    active = 'a' * 64
    oldest = cache_entry(tmp_path, 'b' * 64, '1' * 64, timestamp=1)
    recent = cache_entry(tmp_path, 'c' * 64, '2' * 64, timestamp=2)
    current = cache_entry(tmp_path, active, '3' * 64, timestamp=0)
    unrelated = tmp_path / 'not-an-encoder-namespace'
    unrelated.mkdir()
    (unrelated / 'keep.txt').write_text('Do not delete unrelated content')
    result = encode.prune_cache_namespaces(tmp_path, active)
    assert result['removed'] == ['b' * 64]
    assert not oldest.parent.exists()
    assert recent.exists() and current.exists()
    assert (unrelated / 'keep.txt').exists()
    assert result['retained_bytes'] == 20


def test_cache_retention_reserves_active_namespace_before_first_encode(
    tmp_path,
):
    active = 'a' * 64
    oldest = cache_entry(tmp_path, 'b' * 64, '1' * 64, timestamp=1)
    recent = cache_entry(tmp_path, 'c' * 64, '2' * 64, timestamp=2)
    encode.prune_cache_namespaces(tmp_path, active)
    assert (tmp_path / active).is_dir()
    assert not oldest.exists() and recent.exists()


def test_cache_byte_budget_removes_whole_old_entries_including_temps(tmp_path):
    active = 'a' * 64
    obsolete = cache_entry(tmp_path, 'b' * 64, '1' * 64, timestamp=99)
    oldest = cache_entry(tmp_path, active, '2' * 64, timestamp=1)
    newest = cache_entry(tmp_path, active, '3' * 64, timestamp=2)
    temporary = obsolete.with_suffix('.f32.tmp')
    temporary.write_bytes(b'partial write')
    result = encode.prune_cache_namespaces(tmp_path, active, max_bytes=10)
    assert result['evicted_entries'] == 2
    assert result['retained_bytes'] == 10
    assert not obsolete.exists() and not temporary.exists()
    assert not obsolete.with_suffix('.f32.json').exists()
    assert not oldest.exists() and newest.exists()


@pytest.mark.parametrize('kind', ['namespace', 'entry', 'marker'])
def test_cache_prune_rejects_symlinks_before_any_deletion(tmp_path, kind):
    cache = tmp_path / 'cache'
    active = 'a' * 64
    oldest = cache_entry(cache, 'b' * 64, '1' * 64)
    current = cache / active
    external = tmp_path / 'external'
    external.mkdir()
    protected = external / 'protected'
    protected.write_text('preserve')
    if kind == 'namespace':
        current.symlink_to(external, target_is_directory=True)
    else:
        current.mkdir()
        name = '2' * 64 + '.f32' if kind == 'entry' else '.last-used'
        (current / name).symlink_to(protected)
    with pytest.raises(BuildError, match='directory|files|symlink'):
        encode.prune_cache_namespaces(cache, active, keep=1)
    assert oldest.exists() and protected.read_text() == 'preserve'


def test_cache_prune_rejects_unexpected_managed_content(tmp_path):
    active = 'a' * 64
    current = cache_entry(tmp_path, active, '1' * 64)
    extra = current.parent / 'unknown-data.json'
    extra.write_text('{}')
    with pytest.raises(BuildError, match='Unexpected file'):
        encode.prune_cache_namespaces(tmp_path, active, max_bytes=1)
    assert current.exists() and extra.exists()


def test_cache_prune_cli_never_constructs_encoder_or_loads_model(
    tmp_path, monkeypatch,
):
    monkeypatch.setattr(
        encode, 'encoder_identity', lambda config: {'cache': 2},
    )
    monkeypatch.setattr(encode, 'BgeEncoder',
                        lambda *args, **kwargs: pytest.fail('No encoder load'))
    assert encode.main([
        '--prune-cache-dir', str(tmp_path / 'passages'),
        '--prune-cache-dir', str(tmp_path / 'queries'),
    ]) == 0
    signature = encode.sha256_hex(canonical_json({'cache': 2}))
    assert (tmp_path / 'passages' / signature).is_dir()
    assert (tmp_path / 'queries' / signature).is_dir()
