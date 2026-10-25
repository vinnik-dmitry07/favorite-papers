'''Evidence-boundary and workload regressions for the DO probe.'''

import json

import pytest

import run_static_search_do_probe as probe


def report():
    value = {
        'run_id': 'run-1', 'phase': 'pilot', 'origin': 'https://probe.example',
        'script_name': 'key-papers-static-probe-1-1',
        'info': {'corpus_version': 'v1', 'longest_paper_id': 'paper',
                 'sample_fetch_id': 'document'},
        'pilot': [{'marker': 'marker-1',
                   'case': 'rest_search.application_cold',
                   'kind': 'rest_search', 'mode': 'application_cold',
                   'sequence': 0, 'success': True, 'eligible': True,
                   'state': 'complete', 'object_id': 'object-1',
                   'cold_kind': 'application-cache-reset',
                   'client_wall_ms': 10}],
    }
    value['pilot'].append({**value['pilot'][0], 'marker': 'marker-2',
                           'kind': 'mcp_search',
                           'case': 'mcp_search.application_cold'})
    return value


def events(role, request_id='request-1', cpu=2, outcome='ok'):
    workers = {'cpuTimeMs': cpu, 'wallTimeMs': 15, 'outcome': outcome}
    if role == 'durable_object':
        workers['durableObjectId'] = 'object-1'
    first = [
        {'$metadata': {'type': 'cf-worker', 'requestId': request_id},
         '$workers': {key: value for key, value in workers.items()
                      if key == 'durableObjectId'},
         'source': {'probe_marker': 'marker-1', 'run_id': 'run-1',
                    'runtime_role': role, 'object_id': 'object-1',
                    'cpuTimeMs': 0}},
        {'$metadata': {'type': 'cf-worker-event', 'requestId': request_id,
                       'id': role + '-event'}, '$workers': workers},
    ]
    second = json.loads(json.dumps(first).replace('marker-1', 'marker-2')
                        .replace(request_id, request_id + '-2'))
    return first + second


def test_shared_request_id_distinguishes_gateway_and_object():
    value = report()
    probe.attach_telemetry(value, events('durable_object', cpu=60)[::-1])
    probe.attach_telemetry(value, events('gateway'))
    probe.summarize(value)
    assert value['sample_gate'] == 'passed'
    assert value['runtime_gate'] == 'unverified'
    evidence = value['pilot'][0]['telemetry']
    assert evidence['gateway']['cpu_ms'] == 2
    assert evidence['durable_object']['cpu_ms'] == 60


def test_custom_role_and_cpu_cannot_establish_object_scope():
    value = report()
    data = events('durable_object')
    for event in data:
        event['$workers'].pop('durableObjectId', None)
    probe.attach_telemetry(value, data + events('gateway', 'gateway-request'))
    probe.summarize(value)
    assert value['gateway_cpu_gate'] == 'passed'
    assert value['do_cpu_gate'] == 'unverified'
    assert value['sample_gate'] == 'unverified'


def test_unrelated_aggregate_cpu_not_used():
    value = report()
    probe.attach_telemetry(value, [{
        'sum': {'cpuTime': 0}, 'source': {'cpuTimeMs': 0},
        '$metadata': {'type': 'aggregate', 'requestId': 'request-1'},
    }])
    probe.summarize(value)
    assert value['do_cpu_gate'] == 'unverified'


@pytest.mark.parametrize('role,cpu', [
    ('gateway', 8), ('durable_object', 30000),
])
def test_observed_cpu_failure_does_not_need_complete_telemetry(role, cpu):
    value = report()
    probe.attach_telemetry(value, events(role, cpu=cpu))
    probe.summarize(value)
    assert value['sample_gate'] == 'failed'


def test_platform_failure_without_cpu_fails():
    value = report()
    probe.attach_telemetry(value, events('durable_object', cpu=None,
                                        outcome='exceededMemory'))
    probe.summarize(value)
    assert value['do_cpu_gate'] == 'failed'


def test_conflicting_ids_and_duplicate_cpu_fail_closed():
    value = report()
    probe.attach_telemetry(value, events('gateway') + events('durable_object'))
    probe.attach_telemetry(value, events('gateway', cpu=3))
    assert not probe.evidence_complete(value['pilot'][0])
    assert value['pilot'][0]['telemetry_conflict'] is True
    value = report()
    data = events('gateway')
    data[0]['$workers']['requestId'] = 'other'
    probe.attach_telemetry(value, data + events('durable_object'))
    assert not probe.evidence_complete(value['pilot'][0])


def test_cross_object_result_and_cross_run_marker_rejected():
    value = report()
    value['pilot'][0]['object_id'] = 'different'
    probe.attach_telemetry(value, events('durable_object'))
    assert value['pilot'][0]['telemetry_conflict'] is True
    value = report()
    data = events('durable_object')
    data[0]['source']['run_id'] = 'other'
    probe.attach_telemetry(value, data)
    assert not value['pilot'][0]['telemetry']


def test_pilot_pass_is_not_matrix_pass():
    value = report()
    value['phase'] = 'matrix'
    probe.attach_telemetry(value, events('gateway') + events('durable_object'))
    probe.summarize(value)
    assert value['preflight_gate'] == 'passed'
    assert value['sample_gate'] == 'unverified'


def test_request_budget_is_hard_bound():
    value = report()
    value['http_attempts'] = 1500
    with pytest.raises(ValueError, match='budget'):
        probe.prepare(value, 'rest_search', 'warm', 0)
    assert value['http_attempts'] == 1500


def test_time_budget_is_hard_bound():
    value = report()
    value['load_deadline_ms'] = 0
    with pytest.raises(ValueError, match='time budget'):
        probe.prepare(value, 'rest_search', 'warm', 0)


def test_full_matrix_scope_and_concurrency(monkeypatch):
    value = report()
    active = 0
    peak = 0

    def fake_send(_report, row):
        nonlocal active, peak
        # Scheduling need not overlap; executor must never exceed four.
        active += 1
        peak = max(active, peak)
        active -= 1
        return {**row, 'success': True, 'client_wall_ms': 2,
                'state': 'complete'}

    monkeypatch.setattr(probe, 'send', fake_send)
    probe.run_matrix(value, 50)
    assert len(value['requests']) == 600
    assert len(value['priming']) == 6
    assert len(value['concurrency']) == 24
    assert peak <= 4
    assert value['http_attempts'] == 630
    assert value['matrix_finished'] is True


def test_failed_request_stops_load(monkeypatch):
    value = report()
    monkeypatch.setattr(probe, 'send', lambda _, row: {
        **row, 'state': 'complete', 'success': False,
    })
    probe.run_matrix(value, 50)
    assert len(value['requests']) == 1
    assert 'matrix_finished' not in value


def test_startup_retry_does_not_poison_workload_gate():
    value = report()
    value['discovery'] = [{'startup_retry': True, 'state': 'complete',
                           'success': False}]
    probe.attach_telemetry(value, events('gateway') + events('durable_object'))
    probe.summarize(value)
    assert value['functional_gate'] == 'passed'


def test_secret_only_in_request_headers(monkeypatch):
    value = report()
    row = value['pilot'][0]
    monkeypatch.setenv('PROBE_TOKEN', 'secret-token')
    seen = []

    def fake_exchange(url, payload, headers, timeout):
        seen.append((url, headers))
        return 200, {
            'x-probe-runtime': 'durable-object', 'x-probe-synthetic': 'true',
            'x-probe-marker': row['marker'], 'x-probe-boot-id': 'boot',
            'x-probe-cache-id': 'cache', 'x-probe-object-id': 'object-1',
            'x-probe-cold-kind': 'application-cache-reset',
            'x-probe-variant': 'wasm-json16',
        }, json.dumps({'corpus_version': 'v1', 'hits': [
            {'paper_id': 'paper', 'snippet': 'text'},
        ]})

    monkeypatch.setattr(probe, 'exchange', fake_exchange)
    result = probe.send(value, row)
    assert result['success'] is True
    assert seen[0][1]['x-probe-token'] == 'secret-token'
    assert 'secret-token' not in seen[0][0]
    assert 'secret-token' not in json.dumps(result)


def test_unverified_pilot_never_sends_matrix(tmp_path, monkeypatch):
    monkeypatch.setenv('PROBE_TOKEN', 'secret-token')
    output = tmp_path / 'report.json'

    def fake_send(_report, row):
        result = {**row, 'state': 'complete', 'success': True,
                  'eligible': True, 'client_wall_ms': 1, 'object_id': 'object'}
        if row['kind'] == 'info':
            result['info'] = {'corpus_version': 'v1', 'sample_fetch_id': 'doc'}
        return result

    monkeypatch.setattr(probe, 'send', fake_send)
    monkeypatch.setattr(probe, 'collect', lambda *_: None)
    monkeypatch.setattr(probe, 'run_matrix',
                        lambda *_: pytest.fail('matrix sent'))
    assert probe.main(['https://probe.example', '--script-name', 'test',
                       '--phase', 'matrix', '--output', str(output)]) == 2
    saved = json.loads(output.read_text())
    assert saved['preflight_gate'] == 'unverified'
    assert not saved['requests']
    assert 'secret-token' not in output.read_text()


def test_collector_retries_transient_and_records_shape(monkeypatch):
    value = report()
    value.update(started_ms=1, finished_ms=2)
    monkeypatch.setenv('CLOUDFLARE_ACCOUNT_ID', 'account')
    monkeypatch.setenv('CLOUDFLARE_API_TOKEN', 'token')
    replies = [(429, {}, '{}'), (200, {}, json.dumps({
        'result': {'events': {'events': events('gateway')
                             + events('durable_object')}}}))]
    monkeypatch.setattr(probe, 'exchange',
                        lambda *_args, **_kwargs: replies.pop(0))
    monkeypatch.setattr(probe.time, 'sleep', lambda *_: None)
    probe.collect(value, 10)
    assert probe.evidence_complete(value['pilot'][0])
    assert 'telemetry_error' not in value
    assert value['telemetry_shape_examples']


def test_per_operation_latency_not_diluted_by_fast_operations():
    value = report()
    value['requests'] = [
        {'marker': f'row-{index}',
         'kind': 'rest_search' if index < 50 else 'find',
         'case': 'rest_search.warm' if index < 50 else 'find.warm',
         'mode': 'warm', 'success': True, 'eligible': True,
         'state': 'complete',
         'client_wall_ms': 3000 if index < 3 else 1}
        for index in range(600)
    ]
    probe.summarize(value)
    assert value['warm_latency_cases']['rest_search.warm']['p95'] == 3000
    assert value['latency_gate'] == 'failed'


def test_concurrency_latency_has_separate_case():
    value = report()
    value['concurrency'] = [{
        'marker': 'parallel', 'kind': 'rest_search',
        'case': 'rest_search.warm',
        'mode': 'warm', 'success': True, 'eligible': True, 'state': 'complete',
        'client_wall_ms': 3000,
    }]
    probe.summarize(value)
    assert 'concurrency4.rest_search.warm' in value['warm_latency_cases']
    assert value['latency_gate'] == 'failed'


def test_rest_only_pilot_not_complete():
    value = report()
    value['pilot'] = value['pilot'][:1]
    probe.attach_telemetry(value, events('gateway') + events('durable_object'))
    probe.summarize(value)
    assert value['preflight_gate'] == 'unverified'


def test_identified_do_failure_is_not_startup_propagation(tmp_path, monkeypatch):
    monkeypatch.setenv('PROBE_TOKEN', 'secret-token')
    calls = []

    def failed(_report, row):
        calls.append(row['kind'])
        return {**row, 'success': False, 'state': 'complete', 'status': 503,
                'object_id': 'object', 'boot_id': 'boot', 'client_wall_ms': 10}

    monkeypatch.setattr(probe, 'send', failed)
    output = tmp_path / 'failure.json'
    assert probe.main(['https://probe.example', '--script-name', 'test',
                       '--output', str(output)]) == 1
    value = json.loads(output.read_text())
    assert calls == ['info']
    assert not value['discovery'][0].get('startup_retry')
    assert value['functional_gate'] == 'failed'


def test_provider_startup_retry_then_pilot_can_pass(tmp_path, monkeypatch):
    monkeypatch.setenv('PROBE_TOKEN', 'secret-token')
    calls = []

    def send_after_propagation(_report, row):
        calls.append(row['kind'])
        if len(calls) == 1:
            return {**row, 'success': False, 'state': 'complete',
                    'status': 503, 'client_wall_ms': 2}
        result = {**row, 'success': True, 'state': 'complete',
                  'object_id': 'object', 'boot_id': 'boot',
                  'client_wall_ms': 10}
        if row['kind'] == 'info':
            result['info'] = {'corpus_version': 'v1'}
        return result

    def platform_evidence(value, _wait):
        for row in probe.records(value):
            row['telemetry'] = {
                role: {'cpu_ms': 2, 'outcome': 'ok'} for role in probe.ROLES}

    monkeypatch.setattr(probe, 'send', send_after_propagation)
    monkeypatch.setattr(probe, 'collect', platform_evidence)
    monkeypatch.setattr(probe.time, 'sleep', lambda *_: None)
    output = tmp_path / 'pass.json'
    assert probe.main(['https://probe.example', '--script-name', 'test',
                       '--output', str(output)]) == 0
    value = json.loads(output.read_text())
    assert calls == ['info', 'info', 'rest_search', 'mcp_search']
    assert value['discovery'][0]['startup_retry'] is True
    assert value['sample_gate'] == 'passed'
