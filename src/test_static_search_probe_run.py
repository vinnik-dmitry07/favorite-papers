'''Regression checks for the probe's measurement and evidence boundaries.'''

import json

import pytest

from run_static_search_probe import (
    EXPECTED_CASES,
    PROBE_USER_AGENT,
    attach_telemetry,
    decode_body,
    exchange,
    main,
    percentiles,
    probe_info,
    run_samples,
    sample,
    summarize,
    validate,
)


def make_report(count=50):
    return {
        'origin': 'https://synthetic.example',
        'run_id': 'run-123',
        'info': {'corpus_version': 'v1'},
        'requests': [
            {'case': case, 'marker': f'{case}-{i}',
             'url': f'https://synthetic.example/{case}/{i}',
             'success': True, 'client_wall_ms': 0.1}
            for case in EXPECTED_CASES for i in range(count)
        ],
    }


def events_for(report, cpu=2):
    return [
        {'$metadata': {'id': str(i), 'url': 'REDACTED', 'type': 'cf-worker-event'},
         'source': {'probe_marker': row['marker'], 'probe_run': report['run_id']},
         '$workers': {'cpuTimeMs': cpu, 'wallTimeMs': 12, 'outcome': 'ok',
                      'requestId': str(i)}}
        for i, row in enumerate(report['requests'])
    ]


def test_exchange_identifies_client_in_get_and_post(monkeypatch):
    requests = []

    class FakeResponse:
        status = 200
        headers = {'content-type': 'application/json'}

        def __enter__(self):
            return self

        def __exit__(self, *_args):
            return False

        def read(self):
            return b'{}'

    def fake_urlopen(request, timeout):
        requests.append((request, timeout))
        return FakeResponse()

    monkeypatch.setattr('run_static_search_probe.urllib.request.urlopen',
                        fake_urlopen)
    for payload in (None, {'queryId': 'pilot'}):
        status, _, body = exchange('https://probe.example/probe/info',
                                   payload=payload)
        assert status == 200
        assert body == '{}'
    assert [req.get_method() for req, _ in requests] == ['GET', 'POST']
    assert all(req.get_header('User-agent') == PROBE_USER_AGENT
               for req, _ in requests)
    assert all(timeout == 20 for _, timeout in requests)


def test_cpu_comes_from_platform_and_runtime_never_passes():
    report = make_report()
    attach_telemetry(report, events_for(report))
    summarize(report)
    assert report['cpu_gate'] == 'passed'
    assert report['cases']['rest_search.warm']['cpu_ms']['p99'] == 2
    assert report['runtime_gate'] == 'unverified'
    assert report['memory_gate'] == 'unverified'
    assert report['isolate_cold_gate'] == 'unverified'


def test_missing_case_prevents_overall_pass():
    report = make_report()
    report['requests'] = [row for row in report['requests']
                          if row['case'] == 'rest_search.warm']
    attach_telemetry(report, events_for(report))
    summarize(report)
    assert report['cases']['rest_search.warm']['cpu_gate'] == 'passed'
    assert report['cpu_gate'] == 'unverified'
    assert len(report['missing_cases']) == 11


@pytest.mark.parametrize(
    'kind', ['missing', 'no_cpu', 'partial', 'few_samples'])
def test_absent_or_insufficient_telemetry_is_unverified(kind):
    report = make_report(10 if kind == 'few_samples' else 50)
    events = events_for(report)
    if kind == 'missing':
        events = []
    elif kind == 'partial':
        events = events[:-1]
    elif kind == 'no_cpu':
        for event in events:
            event['$workers'].pop('cpuTimeMs')
    attach_telemetry(report, events)
    summarize(report)
    assert report['cpu_gate'] == 'unverified'


@pytest.mark.parametrize('failure', ['http', 'outcome', 'threshold'])
def test_failures_and_strict_p99_are_not_successes(failure):
    report = make_report()
    events = events_for(report)
    if failure == 'http':
        report['requests'][0].update(success=False, status=429)
    elif failure == 'outcome':
        events[0]['$workers']['outcome'] = 'exceededCpu'
    else:
        events[-1]['$workers']['cpuTimeMs'] = 8
    attach_telemetry(report, events)
    summarize(report)
    assert report['cpu_gate'] == 'failed'
    assert percentiles(list(range(1, 51)))['p99'] == 50


@pytest.mark.parametrize('failure', ['threshold', 'outcome', 'outcome_no_cpu'])
def test_observed_failure_fails_before_sufficient_samples(failure):
    report = make_report(2)
    events = events_for(report)[:1]
    if failure == 'threshold':
        events[0]['$workers']['cpuTimeMs'] = 8
    else:
        events[0]['$workers']['outcome'] = 'exceededCpu'
        if failure == 'outcome_no_cpu':
            events[0]['$workers'].pop('cpuTimeMs')
    attach_telemetry(report, events)
    summarize(report)
    assert report['cpu_gate'] == 'failed'


def test_telemetry_matches_markers_and_keeps_only_platform_cpu():
    report = make_report(1)
    events = events_for(report)
    events.append({'$metadata': {'url': report['requests'][0]['url']},
                   '$workers': {'outcome': 'ok'},
                   'source': {'cpuTimeMs': 0}})
    events.append({'$metadata': {'url': 'https://another.example/'},
                   '$workers': {'cpuTimeMs': 99}})
    attach_telemetry(report, events)
    assert report['requests'][0]['telemetry']['cpu_ms'] == 2


def test_mcp_sse_checks_structured_content():
    body = {'results': [{'id': 'paper', 'url': 'https://paper.example'}]}
    result = {'structuredContent': body,
              'content': [{'type': 'text', 'text': json.dumps(body)}]}
    assert decode_body('data: ' + json.dumps({'result': result}), True) == body
    result['content'][0]['text'] = '{}'
    with pytest.raises(ValueError, match='mismatch'):
        decode_body(json.dumps({'result': result}), True)
    with pytest.raises(ValueError, match='protocol'):
        decode_body(json.dumps({'error': {'code': -1}}), True)


@pytest.mark.parametrize('body', [[], {'result': []}, {
    'result': {'structuredContent': {}, 'content': [None]},
}])
def test_malformed_mcp_containers_are_rejected(body):
    with pytest.raises(ValueError):
        decode_body(json.dumps(body), True)


def test_nonobject_hit_is_reported_as_failure(monkeypatch):
    report = make_report(0)
    monkeypatch.setattr('run_static_search_probe.exchange', lambda *_: (
        200, {'x-probe-synthetic': 'true', 'x-probe-boot-id': 'boot',
              'x-probe-cache': 'warm'},
        json.dumps({'corpus_version': 'v1', 'hits': [None]})))
    assert sample(report, 'rest_search', 'warm', 0, '/v1/search') is None
    assert report['requests'][0]['success'] is False


def test_requested_application_cold_is_not_isolate_cold(monkeypatch):
    report = make_report(0)
    body = {'hits': [{'paper_id': 'paper', 'snippet': 'text'}],
            'corpus_version': 'v1'}
    monkeypatch.setattr('run_static_search_probe.exchange', lambda *_: (
        200, {'X-Probe-Synthetic': 'true', 'X-Probe-Boot-Id': 'boot-1',
              'X-Probe-Cache': 'cold', 'x-probe-marker': _[2]['x-probe-marker']}, json.dumps(body)))
    sample(report, 'rest_search', 'application_cold', 0, '/v1/search',
           {'q': 'café attention'})
    row = report['requests'][0]
    assert row['success']
    assert row['cache_condition'] == 'application_cold'
    assert row['observed_cache'] == 'cold'
    assert row['isolate_cold_verified'] is False
    assert 'cold=1' in row['url']
    assert row['query_codepoints'] == len('café attention')


def test_max_query_runs_every_tenth_measured_search(monkeypatch):
    report = make_report(0)
    max_query = ' '.join(['a'] * 500)
    report['info'].update(sample_query='short', sample_query_max=max_query,
                          longest_paper_id='paper')
    queries = []

    def capture(_report, kind, mode, sequence, _path, params=None, tool=None):
        if kind == 'rest_search':
            queries.append((mode, kind, sequence, params['q']))
        elif kind == 'mcp_search':
            queries.append((mode, kind, sequence,
                            tool['params']['arguments']['query']))

    monkeypatch.setattr('run_static_search_probe.sample', capture)
    run_samples(report, 10)
    maximum = [item for item in queries if item[-1].startswith(max_query)]
    assert len(maximum) == 4
    assert all(item[2] == 9 for item in maximum)
    assert all(len(item[-1]) < 2000 for item in maximum)
    assert all(item[-1].startswith('short') for item in queries
               if item[2] != 9)


def test_cold_request_requires_cold_header(monkeypatch):
    report = make_report(0)
    body = {'hits': [{'paper_id': 'paper', 'snippet': 'text'}],
            'corpus_version': 'v1'}
    monkeypatch.setattr('run_static_search_probe.exchange', lambda *_: (
        200, {'x-probe-synthetic': 'true', 'x-probe-boot-id': 'boot',
              'x-probe-cache': 'warm', 'x-probe-marker': _[2]['x-probe-marker']}, json.dumps(body)))
    assert sample(report, 'rest_search', 'application_cold',
                  0, '/v1/search') is None
    assert 'precondition' in report['requests'][0]['error']


@pytest.mark.parametrize('kind', ['rest_search', 'mcp_fetch'])
def test_version_is_required(kind):
    with pytest.raises(ValueError, match='version'):
        validate({}, kind, 'v1')
    with pytest.raises(ValueError, match='version'):
        validate({'metadata': {'corpus_version': 'v2'}}, kind, 'v1')


@pytest.mark.parametrize('local,expected', [(False, 2), (True, 0)])
def test_exit_code_distinguishes_unverified_online_gate(
        monkeypatch, tmp_path, local, expected):
    report_path = tmp_path / 'report.json'
    report_path.write_text(json.dumps(make_report(2)), encoding='utf-8')
    monkeypatch.setattr('run_static_search_probe.collect', lambda *_: None)
    argv = ['--collect-only', str(report_path), '--output', str(report_path)]
    assert main(argv + (['--local'] if local else [])) == expected


@pytest.mark.parametrize(
    'status,body', [(429, '{}'), (503, '{}'), (200, '{}')])
def test_request_failure_is_recorded(monkeypatch, status, body):
    report = make_report(0)
    monkeypatch.setattr('run_static_search_probe.exchange', lambda *_: (
        status, {'x-probe-synthetic': 'true', 'x-probe-boot-id': 'boot'},
        body))
    assert sample(report, 'rest_search', 'warm', 0, '/v1/search') is None
    assert report['requests'][0]['success'] is False
    summarize(report)
    assert report['cpu_gate'] == 'failed'


def test_redacted_urls_join_across_pages_and_ignore_custom_cpu():
    report = make_report(1)
    row = report['requests'][0]
    invocation = {'$metadata': {'type': 'cf-worker-event', 'url': 'REDACTED'},
                  '$workers': {'requestId': 'platform-id', 'cpuTimeMs': 9,
                               'outcome': 'ok'}}
    log = {'$metadata': {'type': 'cf-worker-log'},
           '$workers': {'requestId': 'platform-id', 'cpuTimeMs': 0},
           'source': json.dumps({'probe_marker': row['marker'],
                                 'probe_run': report['run_id'], 'cpu_ms': 0})}
    attach_telemetry(report, [invocation])
    assert 'telemetry' not in row
    attach_telemetry(report, [log])
    assert row['telemetry']['cpu_ms'] == 9
    summarize(report)
    assert report['cpu_gate'] == 'failed'


def test_ambiguous_request_identity_cannot_pass():
    report = make_report()
    events = events_for(report)
    attach_telemetry(report, events)
    conflicting = json.loads(json.dumps(events[0]))
    conflicting['$workers']['requestId'] = 'another-request'
    attach_telemetry(report, [conflicting])
    summarize(report)
    assert report['cpu_gate'] != 'passed'


def test_isolate_rotation_is_excluded_but_retained(monkeypatch):
    report = make_report(0)
    body = {'hits': [{'paper_id': 'paper', 'snippet': 'text'}],
            'corpus_version': 'v1'}
    monkeypatch.setattr('run_static_search_probe.exchange', lambda *args: (
        200, {'x-probe-synthetic': 'true', 'x-probe-boot-id': 'new-boot',
              'x-probe-cache': 'cold', 'x-probe-marker': args[2]['x-probe-marker'],
              'x-probe-first-request': 'true'}, json.dumps(body)))
    sample(report, 'rest_search', 'warm', 0, '/v1/search')
    row = report['requests'][0]
    assert row['success'] and not row['eligible'] and row['first_request']
    summarize(report)
    assert report['cpu_gate'] == 'unverified'
    assert report['cases']['rest_search.warm']['excluded'] == 1


def test_incomplete_read_keeps_run_and_request_on_disk(monkeypatch, tmp_path):
    from http.client import IncompleteRead
    report = make_report(0)
    report['output_path'] = str(tmp_path / 'partial.json')

    def interrupted(*_args):
        checkpoint = json.loads(Path(report['output_path']).read_text())
        assert checkpoint['run_id'] == report['run_id']
        assert checkpoint['requests'][0]['state'] == 'in_flight'
        raise IncompleteRead(b'partial')

    from pathlib import Path
    monkeypatch.setattr('run_static_search_probe.exchange', interrupted)
    sample(report, 'rest_search', 'warm', 0, '/v1/search')
    saved = json.loads(Path(report['output_path']).read_text())
    assert saved['requests'][0]['excluded_reason'] == 'transport_error'
    assert saved['requests'][0]['state'] == 'complete'


def test_transient_telemetry_failure_is_retried(monkeypatch):
    from run_static_search_probe import collect
    report = make_report(1)
    report.update(started_ms=1000, finished_ms=2000)
    monkeypatch.setenv('CLOUDFLARE_ACCOUNT_ID', 'test-account')
    monkeypatch.setenv('CLOUDFLARE_API_TOKEN', 'test-token')
    calls = []

    def response(_url, payload, *_args, **_kwargs):
        calls.append(payload)
        if len(calls) == 1:
            return 429, {}, '{}'
        return 200, {}, json.dumps(
            {'result': {'events': {'events': events_for(report)}}})

    monkeypatch.setattr('run_static_search_probe.exchange', response)
    monkeypatch.setattr('run_static_search_probe.time.sleep', lambda *_: None)
    collect(report, 10)
    assert len(calls) == 2
    assert 'needle' not in calls[0]['parameters']
    assert all('telemetry' in row for row in report['requests'])


def test_empty_telemetry_query_preserves_diagnostic_evidence(monkeypatch):
    from run_static_search_probe import collect

    report = make_report(0)
    report.update(started_ms=1000, finished_ms=2000)
    report['preflight_requests'] = [{
        'case': 'stage_noop.application_cold', 'marker': 'pilot',
        'success': True,
    }]
    monkeypatch.setenv('CLOUDFLARE_ACCOUNT_ID', 'test-account')
    monkeypatch.setenv('CLOUDFLARE_API_TOKEN', 'test-token')
    monkeypatch.setattr('run_static_search_probe.exchange',
                        lambda *_args, **_kwargs: (
                            200, {}, json.dumps({'result': {
                                'events': {'count': 0, 'events': []},
                            }})))
    collect(report, 0)
    assert report['telemetry_error'] == 'Missing logs; retry --collect-only'
    diagnostics = report['telemetry_diagnostics']
    assert diagnostics['queries'] == 1
    assert diagnostics['events_across_queries'] == 0
    assert diagnostics['last_page_events'] == 0
    assert diagnostics['last_reported_count'] == 0
    assert diagnostics['linked_markers'] == 0
    assert diagnostics['linked_invocations'] == 0


def test_telemetry_diagnostics_distinguish_events_from_joins(monkeypatch):
    from run_static_search_probe import collect

    report = make_report(0)
    report.update(started_ms=1000, finished_ms=2000)
    report['preflight_requests'] = [{
        'case': 'stage_noop.application_cold', 'marker': 'pilot',
        'success': True,
    }]
    events = [{
        '$metadata': {'type': 'cf-worker-event',
                      'requestId': 'metadata-id'},
        '$workers': {'requestId': 'worker-id',
                     'cpuTimeMs': 1, 'outcome': 'ok'},
    }]
    monkeypatch.setenv('CLOUDFLARE_ACCOUNT_ID', 'test-account')
    monkeypatch.setenv('CLOUDFLARE_API_TOKEN', 'test-token')
    monkeypatch.setattr('run_static_search_probe.exchange',
                        lambda *_args, **_kwargs: (
                            200, {}, json.dumps({'result': {
                                'events': {'count': 1, 'events': events},
                            }})))
    collect(report, 0)
    diagnostics = report['telemetry_diagnostics']
    assert diagnostics['invocation_events'] == 1
    assert diagnostics['worker_request_ids'] == 1
    assert diagnostics['metadata_request_ids'] == 1
    assert diagnostics['linked_markers'] == 0
    assert diagnostics['linked_invocations'] == 1
    assert 'telemetry' not in report['preflight_requests'][0]


def test_failed_baseline_does_not_reject_a_passing_variant():
    report = make_report()
    original = report['requests']
    report['requests'] = [dict(row, case=v + '.' + row['case'],
                               marker=v + row['marker'])
                          for v in ['baseline', 'candidate'] for row in original]
    report['variants'] = ['baseline', 'candidate']
    report['expected_cases'] = [v + '.' + c for v in report['variants']
                                for c in EXPECTED_CASES]
    events = events_for(report)
    events[0]['$workers']['cpuTimeMs'] = 10
    attach_telemetry(report, events)
    summarize(report)
    assert report['variant_gates'] == {
        'baseline': 'failed', 'candidate': 'passed'}
    assert report['cpu_gate'] == 'passed'
    bound = report['cases']['candidate.rest_search.warm']['zero_exceedance_upper_95']
    assert bound == pytest.approx(0.058155079)


def test_mid_request_checkpoint_can_be_recovered(tmp_path, monkeypatch):
    report = make_report(0)
    report['requests'] = [{'case': 'rest_search.warm', 'marker': 'inflight',
                           'success': False, 'state': 'in_flight'}]
    path = tmp_path / 'interrupted.json'
    path.write_text(json.dumps(report))
    monkeypatch.setattr('run_static_search_probe.collect', lambda *_: None)
    assert main(['--collect-only', str(path), '--output', str(path),
                 '--local']) == 2
    saved = json.loads(path.read_text())
    assert saved['functional_gate'] == 'unverified'
    assert saved['cases']['rest_search.warm']['excluded'] == 1


def test_discovery_retries_before_measurements_and_keeps_evidence(
        tmp_path, monkeypatch):
    report = make_report(0)
    report['output_path'] = str(tmp_path / 'report.json')
    responses = iter([
        (503, {'CF-Ray': 'ray-1'}, '{"error": "asset unavailable"}'),
        (200, {'X-Probe-Synthetic': 'true'}, json.dumps({
            'synthetic': True, 'variants': ['js4-json16'],
            'corpus_version': 'v1'})),
    ])
    monkeypatch.setattr('run_static_search_probe.exchange',
                        lambda *_, **__: next(responses))
    monkeypatch.setattr('run_static_search_probe.time.sleep', lambda _: None)
    assert probe_info(report, 10)['corpus_version'] == 'v1'
    saved = json.loads((tmp_path / 'report.json').read_text())
    assert saved['readiness_gate'] == 'passed'
    assert saved['requests'] == []
    assert saved['readiness_attempts'][0]['status'] == 503
    assert saved['readiness_attempts'][0]['cf_ray'] == 'ray-1'
    assert 'asset unavailable' in saved['readiness_attempts'][0][
        'response_excerpt']


@pytest.mark.parametrize('status,body,expected', [
    (503, '{"error": "asset unavailable"}', 2),
    (403, 'error code: 1010', 1),
    (200, '{"synthetic": false}', 1),
    (200, '<html>wrong application</html>', 1),
])
def test_discovery_failure_is_saved_and_never_starts_matrix(
        tmp_path, monkeypatch, status, body, expected):
    path = tmp_path / 'failed-start.json'
    calls = []

    def exchange(url, **_kwargs):
        calls.append(url)
        return status, {}, body

    monkeypatch.setattr('run_static_search_probe.exchange', exchange)
    assert main(['https://synthetic.example', '--output', str(path),
                 '--ready-wait-seconds', '0']) == expected
    report = json.loads(path.read_text())
    assert report['run_id']
    assert report['cpu_gate'] == 'unverified'
    assert report['functional_gate'] != 'passed'
    assert report['requests'] == []
    assert report['readiness_attempts'][0]['response_excerpt'] == body
    assert calls == ['https://synthetic.example/probe/info']


def test_discovery_transport_error_keeps_checkpoint(tmp_path, monkeypatch):
    from http.client import IncompleteRead

    path = tmp_path / 'interrupted-start.json'

    def interrupted(*_, **__):
        assert path.exists()
        raise IncompleteRead(b'partial')

    monkeypatch.setattr('run_static_search_probe.exchange', interrupted)
    assert main(['https://synthetic.example', '--output', str(path),
                 '--ready-wait-seconds', '0']) == 2
    report = json.loads(path.read_text())
    assert 'IncompleteRead' in report['readiness_attempts'][0]['error']
    assert report['cpu_gate'] == 'unverified'


def test_collect_only_cannot_turn_failed_discovery_into_success(
        tmp_path, monkeypatch):
    report = make_report(0)
    report['readiness_gate'] = 'failed'
    path = tmp_path / 'failed-start.json'
    path.write_text(json.dumps(report))
    monkeypatch.setattr('run_static_search_probe.collect', lambda *_: None)
    assert main(['--collect-only', str(path), '--output', str(path)]) == 1
    assert json.loads(path.read_text())['cpu_gate'] == 'unverified'
