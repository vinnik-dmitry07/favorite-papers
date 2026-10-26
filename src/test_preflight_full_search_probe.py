'''Fail-closed admission tests; no model construction, network or long compute.'''
from copy import deepcopy
from datetime import datetime, timezone
import json
from pathlib import Path
from types import SimpleNamespace

import pytest

from build_agent_index import BuildError, canonical_json, load_embed
from build_full_search_probe import build_full_corpus, write_full_corpus
import preflight_full_search_probe as gate


@pytest.fixture
def run(tmp_path, monkeypatch):
    binding = {'corpus': str(tmp_path / 'corpus'), 'queries': str(tmp_path / 'queries.json'),
               'counts': {'passages': 45, 'cards': 10, 'texts': 9, 'queries': 2064},
               'code_sha256': {}, 'encoder_identity': {'test': 'identity'}}
    monkeypatch.setattr(gate, 'current_binding', lambda *args, **kwargs: deepcopy(binding))
    gate.snapshot(binding['corpus'], binding['queries'], tmp_path)
    return tmp_path, binding


def test_missing_or_unknown_mandatory_gate_is_stop(run):
    root, _ = run
    result = gate.aggregate(root)
    assert result['status'] == 'STOP'
    assert set(result['failures']) == set(gate.GATE_CHECKS)
    assert result['production_ready'] is False
    assert result['platform_cpu_gate'] == 'UNKNOWN'
    with pytest.raises(BuildError, match='PASS'):
        gate.verify_certificate(root / 'certificate.json', corpus=root / 'corpus', queries=root / 'queries.json')


def test_new_attempt_revokes_prior_pass_and_dependents(run):
    root, _ = run
    old = {'status': 'PASS', 'untrusted': 'old'}
    for name in gate.GATE_CHECKS:
        gate.write_json(gate.evidence_path(root, name), old)
    gate.begin_gate(root, 'tokenizer-parity')
    assert all(gate.read_json(gate.evidence_path(root, name))['status'] == 'UNKNOWN'
               for name in gate.GATE_CHECKS)
    assert len(list((root / 'history').glob('*.json'))) == len(gate.GATE_CHECKS)


def test_code_or_query_change_invalidates_snapshot(run, monkeypatch):
    root, binding = run
    changed = {**binding, 'query_manifest_sha256': 'changed'}
    monkeypatch.setattr(gate, 'current_binding', lambda *args, **kwargs: changed)
    with pytest.raises(BuildError, match='Stale'):
        gate.load_run(root)
    with pytest.raises(BuildError, match='Stale'):
        gate.aggregate(root)


def test_certificate_checksum_and_missing_gates_cannot_be_bypassed(run):
    root, _ = run
    result = gate.aggregate(root)
    result['status'] = 'PASS'
    gate.write_json(root / 'certificate.json', result)
    with pytest.raises(BuildError, match='checksum'):
        gate.verify_certificate(root / 'certificate.json', corpus=root / 'corpus', queries=root / 'queries.json')
    result.pop('certificate_sha256')
    result['certificate_sha256'] = gate.digest(result)
    gate.write_json(root / 'certificate.json', result)
    with pytest.raises(BuildError, match='mandatory'):
        gate.verify_certificate(root / 'certificate.json', corpus=root / 'corpus', queries=root / 'queries.json')


def test_all_true_booleans_are_not_numeric_or_memory_evidence(run):
    root, _ = run
    document = gate.load_run(root)
    note = root / 'claim.json'
    gate.write_json(note, {'status': 'PASS'})
    for name in ('numeric-contracts', 'geometry-memory'):
        evidence = {'gate': name, 'artifacts': [{'path': str(note)}]}
        with pytest.raises(BuildError):
            gate.validate_raw_evidence(evidence, document)


def test_raw_memory_report_requires_current_implementation_and_baseline(run):
    root, binding = run
    report = {'schema_version': 2, 'gate': 'geometry-memory', 'status': 'PASS',
              'checks': {key: True for key in gate.GATE_CHECKS['geometry-memory']},
              'passages': 45, 'papers': 10, 'synthetic': True,
              'source_rows_sha256': 'rows', 'source_manifest_sha256': 'source'}
    binding.update(rows_sha256='rows', preembedding_manifest_sha256='source')
    snapshot = {'binding': binding}
    path = root / 'raw-memory.json'
    gate.write_json(path, report)
    with pytest.raises(BuildError, match='implementation'):
        gate.validate_raw_evidence({'gate': 'geometry-memory', 'artifacts': [{'path': str(path)}]}, snapshot)
    report['passages'] = 44
    gate.write_json(path, report)
    with pytest.raises(BuildError, match='coverage'):
        gate.validate_raw_evidence({'gate': 'geometry-memory', 'artifacts': [{'path': str(path)}]}, snapshot)


def test_canonical_coverage_is_checked_against_raw_sources(tmp_path, monkeypatch):
    config = load_embed()
    graph = {'nodes': [{'id': 'paper-a', 'title': 'A', 'authors': [],
                        'kind': 'url', 'section': 'Tests', 'url': 'https://example.test'}], 'edges': []}
    text = '# Full evidence\n\n' + 'Retain every source character. ' * 50
    source = tmp_path / 'graph.json'
    source.write_text(canonical_json(graph))
    release, manifest = build_full_corpus(graph, {'paper-a': text}, config,
        source_path=str(source), source_graph_sha256=gate.sha(source.read_bytes()))
    corpus = tmp_path / 'corpus'
    write_full_corpus(release, manifest, corpus)
    queries = tmp_path / 'queries.json'
    queries.write_text('{}')
    monkeypatch.setattr(gate, 'frozen_inputs', lambda *args: ({'corpus_identity': 'test', 'queries': []}, []))
    monkeypatch.setattr(gate, 'read_texts', lambda nodes: {'paper-a': text})
    monkeypatch.setattr(gate, 'environment', lambda: {})
    monkeypatch.setattr(gate, 'encoder_identity', lambda config: {})
    bound = gate.current_binding(corpus, queries, config)
    assert bound['counts']['cards'] == 1
    # Atomic vector attachment and manifest formatting must not revoke source
    # identity between passage encoding and the later frozen-query encoding.
    attached = gate.read_json(corpus / 'probe.json')
    vector = corpus / 'vectors.f32'
    vector.write_bytes(b'completed-fixture-vector-attachment')
    attached['files']['vectors.f32'] = gate.sha(vector.read_bytes())
    attached['embeddings'] = {'path': 'vectors.f32', 'fixture': True}
    (corpus / 'probe.json').write_text(json.dumps(attached, indent=2) + '\n')
    assert gate.current_binding(corpus, queries, config) == bound
    # Make a self-consistent smaller canonical corpus with unchanged declared
    # source hashes. Canonical internal hashes alone would accept it.
    shortened, small = build_full_corpus(graph, {'paper-a': text[:500]}, config,
        source_path=str(source), source_graph_sha256=gate.sha(source.read_bytes()))
    small['source_text_hashes'] = manifest['source_text_hashes']
    write_full_corpus(shortened, small, corpus)
    with pytest.raises(BuildError, match='complete cleaned source'):
        gate.current_binding(corpus, queries, config)


def test_geometry_failure_is_retained_for_aggregate(run):
    root, _ = run
    raw = root / 'memory-failed.json'
    gate.write_json(raw, {'status': 'FAIL', 'checks': {'observed_peak_below_local_threshold': False},
                          'elapsed_ms': 10})
    with pytest.raises(BuildError, match='FAIL evidence retained'):
        gate.record_geometry(root, raw)
    assert gate.read_json(gate.evidence_path(root, 'geometry-memory'))['status'] == 'FAIL'
    assert gate.aggregate(root)['status'] == 'STOP'


def test_old_memory_executable_cannot_claim_new_checkout_hashes(tmp_path, monkeypatch):
    old = tmp_path / 'old.mjs'
    old.write_text('old executable')
    old_hash = gate.sha(old.read_bytes())
    report = {'executed_bundle_sha256': old_hash}
    artifacts = [{'path': str(old), 'sha256': old_hash}]
    monkeypatch.setattr(gate, 'build_memory_bundle', lambda output: 'current-checkout-hash')
    with pytest.raises(BuildError, match='differs from reviewed'):
        gate.verify_memory_bundle(report, artifacts)
    with pytest.raises(BuildError, match='not retained'):
        gate.verify_memory_bundle(report, [])
    monkeypatch.setattr(gate, 'build_memory_bundle', lambda output: old_hash)
    gate.verify_memory_bundle(report, artifacts)


@pytest.mark.parametrize('change', ['reserved', 'wrong-fingerprint', 'wrong-count', 'running'])
def test_provider_raw_vectors_do_not_override_unfinished_or_stale_ledger(run, monkeypatch, change):
    root, binding = run
    snapshot = gate.load_run(root)
    plan = {'sha256': 'plan', 'model': '@cf/test',
            'inputs': [{'id': 'a', 'token_count': 2}, {'id': 'b', 'token_count': 3}]}
    monkeypatch.setattr(gate, 'canary_plan', lambda directory: plan)
    vector = [1.0] + [0.0] * 767
    local = {'plan_sha256': 'plan', 'inputs': plan['inputs'], 'encoder': binding['encoder_identity'],
             'vectors': [vector, vector], 'repeat_indices': [0, 1], 'repeated_vectors': [vector, vector]}
    remote = {'plan_sha256': 'plan', 'model': '@cf/test', 'vectors': [vector, vector],
              'repeat_indices': [0, 1], 'repeated_vectors': [vector, vector]}
    paths = [root / 'canary-local-vectors.json', root / 'canary-provider-vectors.json']
    gate.write_json(paths[0], local)
    gate.write_json(paths[1], remote)
    ledger = {'status': 'PASSED', 'fingerprint': snapshot['fingerprint'], 'plan_sha256': 'plan',
              'provider_requested': True, 'provider_requests': [
                  {'indices': [0, 1], 'status': 'COMPLETE'}, {'indices': [0, 1], 'status': 'COMPLETE'}],
              'provider_input_count': 4, 'provider_token_count': 10}
    document = {'gate': 'provider-compatibility', 'run_dir': str(root),
                'artifacts': [{'path': str(path)} for path in paths],
                'measurements': {'input_count': 4, 'total_input_tokens': 10, 'min_cosine': 1.0}}
    gate.write_json(root / 'canary-attempt.json', ledger)
    gate.validate_raw_evidence(document, snapshot)
    if change == 'reserved':
        ledger['provider_requests'][1]['status'] = 'RESERVED'
    elif change == 'wrong-fingerprint':
        ledger['fingerprint'] = 'stale'
    elif change == 'wrong-count':
        ledger['provider_input_count'] = 2
    else:
        ledger['status'] = 'PROVIDER_RUNNING'
    gate.write_json(root / 'canary-attempt.json', ledger)
    with pytest.raises(BuildError, match='attempt'):
        gate.validate_raw_evidence(document, snapshot)


def test_tokenizer_resumes_uncommitted_batch_after_interruption(
        tmp_path, monkeypatch):
    binding = {'corpus': str(tmp_path), 'queries': str(tmp_path / 'queries')}
    run = {'binding': binding, 'fingerprint': 'test-fingerprint'}
    passages = ['passage-' + str(index) for index in range(130)]
    manifest = {'rows': [
        {'paper_id': 'test-paper', 'chunk_index': index}
        for index in range(len(passages))
    ]}
    monkeypatch.setattr(gate, 'begin_gate', lambda *args: run)
    monkeypatch.setattr(gate, 'canonical_inputs',
                        lambda *args, **kwargs: (manifest, passages))
    monkeypatch.setattr(gate, 'frozen_inputs',
                        lambda *args: ({'queries': []}, []))
    monkeypatch.setattr(gate, 'write_evidence',
                        lambda *args, **kwargs: tmp_path / 'evidence.json')
    batches = []

    class Encoder:
        model = None

        def __init__(self, *args, **kwargs):
            self.tokenizer_matches = 0

        def _validated_ids(self, values, *, labels=None):
            if values == [' '.join(['a'] * 511)]:
                raise BuildError('Refusing to truncate')
            batches.append(list(values))
            self.tokenizer_matches += len(values)
            return [[101, 102] for _ in values]

    monkeypatch.setattr(gate, 'BgeEncoder', Encoder)
    checkpoint = tmp_path / 'tokenizer-checkpoint.json'
    records = tmp_path / 'tokenizer-inputs.jsonl'
    write_json = gate.write_json
    checkpoints = 0

    def interrupted_write(path, value):
        nonlocal checkpoints
        if path == checkpoint:
            checkpoints += 1
            if checkpoints == 2:
                raise KeyboardInterrupt('killed after records flush')
        write_json(path, value)

    monkeypatch.setattr(gate, 'write_json', interrupted_write)
    with pytest.raises(KeyboardInterrupt, match='after records flush'):
        gate.tokenize(tmp_path)
    saved = gate.read_json(checkpoint)
    assert saved['checked'] == 128
    assert gate.sha(records.read_bytes()) != saved['records_sha256']
    committed = b''.join(records.read_bytes().splitlines(keepends=True)[:128])
    assert gate.sha(committed) == saved['records_sha256']

    def runtime_command(command, **kwargs):
        if command[0] != 'node':
            output = next(value[10:] for value in command
                          if value.startswith('--outfile='))
            Path(output).write_text('mock runtime harness')
            return SimpleNamespace(returncode=0, stdout='', stderr='')
        raw = records.read_bytes()
        rows = [json.loads(line) for line in raw.splitlines()]
        assert [row['id'] for row in rows] == [
            str(index) for index in range(len(rows))
        ]
        result = {'checked': len(rows), 'mismatch_count': 0,
                  'input_sha256': gate.sha(raw)}
        return SimpleNamespace(returncode=0, stdout=json.dumps(result),
                               stderr='')

    monkeypatch.setattr(gate, 'write_json', write_json)
    monkeypatch.setattr(gate.subprocess, 'run', runtime_command)
    batches.clear()
    gate.tokenize(tmp_path)
    report = gate.read_json(tmp_path / 'tokenizer-result.json')
    assert report['status'] == 'PASS'
    assert report['resumed_rows'] == 128
    assert batches[0][0] == passages[128]
    assert records.read_bytes().startswith(committed)
    assert gate.read_json(checkpoint)['records_sha256'] == gate.sha(
        records.read_bytes())


@pytest.mark.parametrize('legacy', [False, True])
@pytest.mark.parametrize('tail', [b'{"unfinished":', b'garbage\xff\n'])
def test_tokenizer_checkpoint_discards_only_uncommitted_tail(
        tmp_path, legacy, tail):
    checkpoint = tmp_path / 'checkpoint.json'
    records = tmp_path / 'records.jsonl'
    prefix = b'{"id":"0","ids":[101,102]}\n'
    saved = {'fingerprint': 'current', 'checked': 1, 'token_count': 2,
             'records_sha256': gate.sha(prefix)}
    if not legacy:
        saved['records_bytes'] = len(prefix)
    gate.write_json(checkpoint, saved)
    records.write_bytes(prefix + tail)
    checked, tokens, digest = gate.resume_tokenizer_checkpoint(
        checkpoint, records, 'current', 2)
    assert (checked, tokens) == (1, 2)
    assert digest.hexdigest() == gate.sha(prefix)
    assert records.read_bytes() == prefix
    assert gate.read_json(checkpoint) == saved
    # A second interruption/resume at the same boundary is harmless.
    assert gate.resume_tokenizer_checkpoint(
        checkpoint, records, 'current', 2)[:2] == (1, 2)


@pytest.mark.parametrize('damage', [
    'committed-content', 'truncated-prefix', 'missing-newline',
    'wrong-byte-boundary', 'stale-fingerprint',
])
def test_tokenizer_checkpoint_rejects_committed_damage_without_truncation(
        tmp_path, damage):
    checkpoint = tmp_path / 'checkpoint.json'
    records = tmp_path / 'records.jsonl'
    prefix = b'{"id":"0","ids":[101,102]}\n'
    saved = {'fingerprint': 'current', 'checked': 1, 'token_count': 2,
             'records_sha256': gate.sha(prefix), 'records_bytes': len(prefix)}
    raw = prefix + b'uncommitted tail'
    if damage == 'committed-content':
        raw = raw.replace(b'101', b'999')
    elif damage == 'truncated-prefix':
        raw = prefix[:5]
    elif damage == 'missing-newline':
        raw = prefix[:-1]
    elif damage == 'wrong-byte-boundary':
        saved['records_bytes'] += 1
    else:
        saved['fingerprint'] = 'old'
    gate.write_json(checkpoint, saved)
    records.write_bytes(raw)
    with pytest.raises(BuildError, match='tokenizer checkpoint'):
        gate.resume_tokenizer_checkpoint(checkpoint, records, 'current', 2)
    assert records.read_bytes() == raw
