'''Regression checks for the probe's measurement and evidence boundaries.'''

import json

import pytest

from run_static_search_probe import (
    EXPECTED_CASES,
    attach_telemetry,
    decode_body,
    main,
    percentiles,
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
            {'case': case,
             'url': f'https://synthetic.example/{case}/{i}',
             'success': True, 'client_wall_ms': 0.1}
            for case in EXPECTED_CASES for i in range(count)
        ],
    }


def events_for(report, cpu=2):
    return [
        {'$metadata': {'id': str(i), 'url': row['url']},
         '$workers': {'cpuTimeMs': cpu, 'wallTimeMs': 12, 'outcome': 'ok',
                      'requestId': str(i)}}
        for i, row in enumerate(report['requests'])
    ]


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


def test_telemetry_matches_exact_request_url_and_keeps_platform_cpu():
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
              'X-Probe-Cache': 'cold'}, json.dumps(body)))
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
              'x-probe-cache': 'warm'}, json.dumps(body)))
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
