'''The bounded compatibility canary cannot turn malformed output into PASS.'''

import json
import os
from io import BytesIO
from types import SimpleNamespace

import pytest

from build_agent_index import BuildError
import preflight_full_search_probe as preflight
import run_full_probe_canary as canary
from run_full_probe_canary import (
    begin_attempt, budget, compare_batches, normalized, provider_vectors,
    reserve_provider,
)


def plan(count=16, tokens=512):
    return {'inputs': [{'input': str(i), 'token_count': tokens}
                       for i in range(count)]}


def test_budget_counts_batch_repeats_and_rejects_overrun():
    count, tokens, repeats = budget(plan())
    assert (count, tokens, repeats) == (18, 9216, [0, 1])
    with pytest.raises(BuildError):
        budget(plan(31))
    with pytest.raises(BuildError):
        budget(plan(30, 513))


@pytest.mark.parametrize('row', [[], [0.0] * 768, [float('nan')] * 768,
                                  [True] * 768, [float('inf')] * 768])
def test_bad_vectors_are_not_compatibility_evidence(row):
    with pytest.raises(BuildError):
        normalized([row], 1)


def test_batch_comparison_is_not_self_comparison():
    left = normalized([[1.0] + [0.0] * 767, [0.0, 1.0] + [0.0] * 766], 2)
    assert compare_batches(left, list(reversed(left)), [0, 1]) == 1


def test_provider_uses_same_model_pooling_and_keeps_secrets_out_of_result():
    calls = []

    def open_request(request, timeout):
        calls.append((request, timeout))
        return BytesIO(json.dumps({'success': True, 'result': {
            'data': [[2.0] + [0.0] * 767]}}).encode())

    result = provider_vectors(['[MASK]'], {
        'model': '@cf/baai/bge-base-en-v1.5', 'pooling': 'cls',
    }, account='abc123', token='private-test-token', opener=open_request)
    assert result == [[1.0] + [0.0] * 767]
    assert len(calls) == 1
    request, timeout = calls[0]
    assert json.loads(request.data) == {'text': ['[MASK]'], 'pooling': 'cls'}
    assert timeout == 45
    assert request.full_url.endswith('/ai/run/@cf/baai/bge-base-en-v1.5')


def test_provider_rejects_error_envelope_without_retry():
    calls = []

    def open_request(request, timeout):
        calls.append(request)
        return BytesIO(b'{"success":false,"errors":[{"message":"error"}]}')

    with pytest.raises(BuildError, match='did not report success'):
        provider_vectors(['x'], {'model': 'model', 'pooling': 'cls'},
                         account='abc', token='token', opener=open_request)
    assert len(calls) == 1


def test_attempt_reserves_budget_durably_before_request_and_cannot_replay(tmp_path):
    inputs = {**plan(), 'fingerprint': 'bound', 'sha256': 'plan'}
    attempt = begin_attempt(tmp_path, inputs, provider=True)
    reserve_provider(tmp_path, attempt, inputs, list(range(16)))
    saved = json.loads((tmp_path / 'canary-attempt.json').read_text())
    assert saved['status'] == 'PROVIDER_RUNNING'
    assert saved['provider_input_count'] == 16
    assert saved['provider_requests'][0]['status'] == 'RESERVED'
    with pytest.raises(BuildError, match='already exists'):
        begin_attempt(tmp_path, inputs, provider=True)
    reserve_provider(tmp_path, attempt, inputs, list(range(16)))
    with pytest.raises(BuildError, match='budget'):
        reserve_provider(tmp_path, attempt, inputs, [0])


def test_late_preflight_stops_before_encoder_or_provider(
    tmp_path, monkeypatch,
):
    clock = [0.0]
    monkeypatch.setattr(canary, 'time', SimpleNamespace(
        monotonic=lambda: clock[0],
    ))

    def late_preflight(_run_dir):
        clock[0] = 301.0

    def unexpected(*args, **kwargs):
        pytest.fail('Expired preflight must not start another operation')

    monkeypatch.setattr(
        preflight, 'check_canary_prerequisites', late_preflight,
    )
    monkeypatch.setattr(preflight, 'canary_plan', unexpected)
    monkeypatch.setattr(canary, 'BgeEncoder', unexpected)
    monkeypatch.setattr(canary, 'provider_vectors', unexpected)
    with pytest.raises(BuildError, match='completion of prerequisites'):
        canary.execute(tmp_path, provider=True, available_neurons=100,
                       started=0.0, deadline=300.0)
    assert not (tmp_path / 'canary-attempt.json').exists()


@pytest.mark.parametrize('allowance', [None, False, True, -1, 0, float('nan')])
def test_operator_allowance_must_be_sufficient_integer_before_model_setup(
        tmp_path, monkeypatch, allowance):
    inputs = {**plan(), 'fingerprint': 'bound', 'sha256': 'plan'}
    monkeypatch.setattr(
        preflight, 'check_canary_prerequisites', lambda _: None,
    )
    monkeypatch.setattr(preflight, 'canary_plan', lambda _: inputs)

    def forbidden(*_args, **_kwargs):
        pytest.fail('Insufficient allowance must stop before encoder setup')

    monkeypatch.setattr(canary, 'BgeEncoder', forbidden)
    with pytest.raises(BuildError, match='Confirm remaining free neurons'):
        canary.execute(tmp_path, provider=True, available_neurons=allowance)
    assert not (tmp_path / 'canary-attempt.json').exists()


def test_local_measurements_include_preflight_and_label_validation_scope(
    tmp_path, monkeypatch,
):
    clock = [0.0]
    revoked, reports = [], []
    monkeypatch.setattr(canary, 'time', SimpleNamespace(
        monotonic=lambda: clock[0],
    ))
    inputs = {**plan(), 'fingerprint': 'bound', 'sha256': 'plan'}

    def prerequisites(_run_dir):
        clock[0] += 20

    def input_plan(_run_dir):
        clock[0] += 5
        return inputs

    def revoke(_run_dir, gate):
        revoked.append(gate)
        clock[0] += 10

    class Encoder:
        identity = {'test': 'fake'}

        def __init__(self, *args, **kwargs):
            pass

        def validate_inputs(self, texts):
            clock[0] += 1

        def __call__(self, texts):
            clock[0] += 2
            return [[1.0] + [0.0] * 767 for _ in texts]

    def evidence(_run_dir, gate, **kwargs):
        reports.append((
            gate, kwargs['measurements'], kwargs['elapsed_seconds'],
        ))
        clock[0] += 5

    monkeypatch.setattr(preflight, 'check_canary_prerequisites', prerequisites)
    monkeypatch.setattr(preflight, 'canary_plan', input_plan)
    monkeypatch.setattr(preflight, 'begin_gate', revoke)
    monkeypatch.setattr(preflight, 'write_evidence', evidence)
    monkeypatch.setattr(canary, 'BgeEncoder', Encoder)
    canary.execute(tmp_path, started=0, deadline=300)
    assert revoked == ['local-canary']
    assert len(reports) == 1
    gate, measurements, elapsed = reports[0]
    assert gate == 'local-canary'
    assert measurements['elapsed_seconds'] == elapsed == 40
    assert 'excludes the following evidence validation' in measurements[
        'elapsed_scope']
    assert [phase['phase'] for phase in measurements['phase_timings']][:3] == [
        'prerequisites', 'input-plan', 'revoke-evidence',
    ]
    timing = json.loads((tmp_path / 'canary-timings.json').read_text())
    assert timing['elapsed_seconds'] == 45
    assert timing['phase_timings'][-1]['phase'] == 'local-evidence-validation'


def test_expired_window_cannot_reserve_or_call_provider(tmp_path, monkeypatch):
    monkeypatch.setattr(canary, 'time', SimpleNamespace(monotonic=lambda: 301))
    calls = []
    monkeypatch.setattr(canary, 'reserve_provider',
                        lambda *args: calls.append('reservation'))
    monkeypatch.setattr(canary, 'provider_vectors',
                        lambda *args, **kwargs: calls.append('provider'))
    with pytest.raises(BuildError, match='before provider reservation'):
        canary.request_provider(tmp_path, {}, {}, [], {}, account='account',
                                token='token', deadline=300)
    assert calls == []


def test_provider_socket_timeout_uses_remaining_after_reservation(
    tmp_path, monkeypatch,
):
    clock = [280.0]
    monkeypatch.setattr(canary, 'time', SimpleNamespace(
        monotonic=lambda: clock[0],
    ))
    inputs = {**plan(), 'fingerprint': 'bound', 'sha256': 'plan'}
    attempt = begin_attempt(tmp_path, inputs, provider=True)
    original = canary.reserve_provider

    def reservation(*args):
        original(*args)
        clock[0] += 2

    timeouts = []

    def provider(texts, _config, **kwargs):
        timeouts.append(kwargs['timeout'])
        return [[1.0] + [0.0] * 767 for _ in texts]

    monkeypatch.setattr(canary, 'reserve_provider', reservation)
    monkeypatch.setattr(canary, 'provider_vectors', provider)
    canary.request_provider(tmp_path, attempt, inputs, [0], {},
                            account='account', token='token', deadline=300)
    assert timeouts == [18.0]
    saved = json.loads((tmp_path / 'canary-attempt.json').read_text())
    assert saved['provider_requests'] == [
        {'indices': [0], 'status': 'COMPLETE'},
    ]


def test_supervisor_rejects_successful_exit_after_whole_deadline(
    tmp_path, monkeypatch,
):
    clock = [10.0]
    joined = []
    options = []
    monkeypatch.setattr(canary, 'time', SimpleNamespace(
        monotonic=lambda: clock[0],
    ))

    class Process:
        exitcode = 0

        def __init__(self, *, target, args):
            options.append(args[1])

        def start(self):
            clock[0] = 15.0

        def join(self, seconds):
            joined.append(seconds)
            clock[0] = 311.0

        def is_alive(self):
            return False

    monkeypatch.setattr(canary, 'multiprocessing', SimpleNamespace(
        get_context=lambda _name: SimpleNamespace(Process=Process),
    ))
    (tmp_path / 'canary-attempt.json').write_text('{"status":"PASSED"}')
    assert canary.main(['--run', str(tmp_path)]) == 1
    assert joined == [295.0]
    assert options[0]['started'] == 10.0
    assert options[0]['deadline'] == 310.0
    completion = json.loads((tmp_path / 'canary-completion.json').read_text())
    assert completion['status'] == 'STOP'
    assert completion['elapsed_seconds'] == 301.0
    assert completion['within_budget'] is False
    assert json.loads((tmp_path / 'canary-attempt.json').read_text()) == {
        'status': 'STOP',
    }


def cached_corpus(tmp_path, monkeypatch):
    asset = tmp_path / 'paper.json'
    asset.write_bytes(b'original')
    manifest = {'files': {'paper.json': preflight.sha(asset.read_bytes())}}
    preflight.write_json(tmp_path / 'probe.json', manifest)
    calls = []

    def canonical(root, config, *, full_corpus):
        assert root == tmp_path and full_corpus
        calls.append(dict(config))
        return manifest, ['exact validated input']

    monkeypatch.setattr(preflight, 'canonical_inputs', canonical)
    return asset, manifest, calls


def test_canary_reuses_tokenization_only_within_one_scoped_attempt(
    tmp_path, monkeypatch,
):
    _asset, _manifest, calls = cached_corpus(tmp_path, monkeypatch)
    with preflight.canary_validation_cache():
        for _ in range(10):
            assert preflight._canonical_inputs(tmp_path, {})[1] == [
                'exact validated input',
            ]
    assert len(calls) == 1
    with preflight.canary_validation_cache():
        preflight._canonical_inputs(tmp_path, {})
    preflight._canonical_inputs(tmp_path, {})
    assert len(calls) == 3


def test_cached_canary_rechecks_asset_bytes_even_with_same_size_and_mtime(
    tmp_path, monkeypatch,
):
    asset, _manifest, calls = cached_corpus(tmp_path, monkeypatch)
    with preflight.canary_validation_cache():
        preflight._canonical_inputs(tmp_path, {})
        previous = asset.stat()
        asset.write_bytes(b'modified')
        os.utime(asset, ns=(previous.st_atime_ns, previous.st_mtime_ns))
        with pytest.raises(BuildError, match='Artifact checksum mismatch'):
            preflight._canonical_inputs(tmp_path, {})
    assert len(calls) == 1


@pytest.mark.parametrize('change', ['manifest', 'config'])
def test_cached_canary_rejects_changed_manifest_or_config(
    tmp_path, monkeypatch, change,
):
    _asset, manifest, calls = cached_corpus(tmp_path, monkeypatch)
    with preflight.canary_validation_cache():
        preflight._canonical_inputs(tmp_path, {})
        config = {}
        if change == 'manifest':
            preflight.write_json(tmp_path / 'probe.json', {
                **manifest, 'new_field': True,
            })
        else:
            config['query_template'] = 'changed'
        with pytest.raises(BuildError, match='corpus/config changed'):
            preflight._canonical_inputs(tmp_path, config)
    assert len(calls) == 1


def test_canary_cache_rejects_mutation_during_initial_validation(
    tmp_path, monkeypatch,
):
    asset, manifest, _calls = cached_corpus(tmp_path, monkeypatch)

    def mutation(*args, **kwargs):
        asset.write_bytes(b'modified')
        preflight.write_json(tmp_path / 'probe.json', {
            'files': {'paper.json': preflight.sha(asset.read_bytes())},
        })
        return manifest, ['stale input']

    monkeypatch.setattr(preflight, 'canonical_inputs', mutation)
    with preflight.canary_validation_cache():
        with pytest.raises(BuildError, match='changed during validation'):
            preflight._canonical_inputs(tmp_path, {})


def test_canary_cache_does_not_cache_source_code_or_environment_binding(
    tmp_path, monkeypatch,
):
    binding = {'corpus': str(tmp_path), 'queries': 'questions.json',
               'source': 'original', 'environment': 'original'}
    preflight.write_json(tmp_path / 'snapshot.json', {
        'schema_version': preflight.SCHEMA,
        'kind': 'full-search-preflight-snapshot', 'scope': preflight.SCOPE,
        'binding': binding, 'fingerprint': preflight.digest(binding),
    })
    checked = []

    def current(*args):
        checked.append(True)
        return dict(binding)

    monkeypatch.setattr(preflight, 'current_binding', current)
    with preflight.canary_validation_cache():
        preflight.load_run(tmp_path)
        binding['source'] = 'changed'
        with pytest.raises(BuildError, match='Stale preflight'):
            preflight.load_run(tmp_path)
    assert len(checked) == 2
