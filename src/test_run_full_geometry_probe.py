'''Offline workload, identity, error and evidence-boundary regressions.'''

from argparse import Namespace
from collections import Counter
import hashlib
import json
import time
import urllib.parse

import pytest

import run_full_geometry_probe as probe


ORIGIN = 'https://key-papers-static-do-probe-123-1.example.workers.dev'
TOKEN = 'never-write-this-authentication-token'


@pytest.fixture
def fixture(tmp_path):
    nodes = {f'paper-{index:02}': {
        'id': f'paper-{index:02}',
        'text': {'available': True, 'code_points': 40000 + index},
    } for index in range(48)}
    graph = json.dumps({'nodes': nodes}).encode()
    (tmp_path / 'graph.json').write_bytes(graph)
    manifest = {
        'kind': 'full-corpus-int8-geometry-fixture', 'synthetic': True,
        'publication_ready': False, 'dimensions': 768,
        'release_id': 'a' * 64, 'passage_count': 40575,
        'graph_path': 'graph.json', 'paper_ids': sorted(nodes),
        'text_paper_ids': sorted(nodes),
        'files': {'graph.json': {
            'sha256': hashlib.sha256(graph).hexdigest(),
        }},
    }
    (tmp_path / 'probe.json').write_text(json.dumps(manifest))
    return tmp_path


def args_for(path):
    return Namespace(base_url=ORIGIN, script_name=None, token_env='PROBE_TOKEN',
                     assets=path, max_load_seconds=30, wait_seconds=0,
                     out=path / 'report.json')


def report_for(path):
    return {'run_id': 'test-run', 'started_ms': int(time.time() * 1000),
            'output_path': str(path / 'report.json'), 'requests': [],
            'http_attempts': 0, 'workload_complete': False}


class FakeRemote:
    def __init__(self, fixture):
        self.identity, self.nodes, _ = probe.read_fixture(fixture)
        self.prepared = 0
        self.queries = set()
        self.calls = []

    def __call__(self, url, payload, headers, timeout):
        self.calls.append((url, payload))
        assert headers['x-probe-token'] == TOKEN
        assert 0 < timeout <= 30
        parsed = urllib.parse.urlsplit(url)
        if payload:
            name = payload['params']['name']
            kind = {'read_content': 'content', 'find_in_paper': 'find',
                    'search_passages': 'search'}[name]
            args = payload['params']['arguments']
        else:
            kind = parsed.path.rsplit('/', 1)[1]
            args = {key: values[0] for key, values
                    in urllib.parse.parse_qs(parsed.query).items()}
        response_headers = {
            'x-probe-marker': headers['x-probe-marker'],
            'x-probe-runtime-role': 'durable_object',
            'x-probe-synthetic': 'true',
            'x-probe-manifest-sha256': self.identity['manifest_sha256'],
            'x-probe-boot-id': 'boot-1', 'x-probe-object-id': 'object-1',
            'x-probe-first-request': 'true' if len(self.calls) == 1 else 'false',
        }
        if kind == 'catalog' and len(self.calls) > 12:
            return 503, response_headers, json.dumps({
                'error': {'code': 'probe_overloaded'}})
        body = {'corpus_version': self.identity['release_id']}
        if kind in ('status', 'prepare'):
            if kind == 'prepare':
                self.prepared = 16
            body.update(self.identity, kind='full-geometry-probe',
                        synthetic=True, prepared_queries=self.prepared,
                        embedded_queries=len(self.queries))
        elif kind == 'catalog':
            body.update(total=len(self.nodes), papers=[{'id': key}
                        for key in list(self.nodes)[:24]])
        elif kind in ('content', 'contents', 'find'):
            length = self.nodes[args['id']]['text']['code_points']
            body.update(paper_id=args['id'], available=True,
                        total_length=length)
            if kind == 'content':
                offset = int(args['offset'])
                size = min(probe.CONTENT_MAX, length - offset)
                body.update(text='\U0001f680' * size, offset=offset,
                            next_offset=offset + size
                            if offset + size < length else None)
            elif kind == 'contents':
                body['sections'] = [{'offset': 0}]
            else:
                body['matches'] = [{'start': 0, 'end': 3}]
        else:
            assert self.prepared == 16
            self.queries.add(args['q'])
            body['hits'] = [{'paper_id': 'paper-00', 'score': 0.9,
                             'start': 0, 'end': 5,
                             'corpus_version': self.identity['release_id']}]
        if payload:
            body = {'jsonrpc': '2.0', 'id': payload['id'], 'result': {
                'structuredContent': body,
                'content': [{'type': 'text', 'text': json.dumps(body)}],
            }}
        return 200, response_headers, json.dumps(body)


def test_exact_bounded_workload_and_no_readiness_claim(fixture, monkeypatch):
    remote = FakeRemote(fixture)
    monkeypatch.setattr(probe, 'exchange', remote)
    monkeypatch.setenv('PROBE_TOKEN', TOKEN)
    report = report_for(fixture)
    probe.execute(args_for(fixture), report)
    assert report['functional_gate'] == 'passed'
    assert report['workload_complete'] is True
    assert len(remote.calls) == report['http_attempts'] == 327
    phases = Counter(row['phase'] for row in report['requests'])
    assert phases == {
        'cold-catalog-burst': 16, 'identity': 1,
        'largest-paper-rest-mcp': 4, 'paper-burst': 80,
        'paper-cache-churn': 48, 'prepare': 1,
        'search-cache-churn-1': 80, 'search-cache-churn-2': 80,
        'repeat-cached-queries': 16, 'final-status': 1,
    }
    assert len(remote.queries) == 160
    assert report['phases']['cold-catalog-burst']['controlled_overload'] == 4
    assert report['memory_gate'] == 'unverified'
    assert report['production_readiness'] == 'unverified'
    assert report['gateway_cpu_gate'] == report['do_cpu_gate'] == 'unverified'
    assert TOKEN not in (fixture / 'report.json').read_text()


@pytest.mark.parametrize('url', [
    'https://production.example.workers.dev',
    ORIGIN + '/v1/search', ORIGIN + '?token=hidden',
    ORIGIN.replace('https://', 'http://'),
    ORIGIN.replace('https://', 'https://user:password@'),
    ORIGIN + ':443', ORIGIN + '.evil.example',
])
def test_non_probe_and_credential_urls_rejected(url):
    with pytest.raises(ValueError):
        probe.validate_url(url)


def test_valid_origin_matches_script_name():
    assert probe.validate_url(ORIGIN)[0] == ORIGIN
    with pytest.raises(ValueError, match='Script name'):
        probe.validate_url(ORIGIN, 'different-script')


@pytest.mark.parametrize('change', [
    {'synthetic': False}, {'kind': 'full-corpus-int8'},
    {'publication_ready': True}, {'graph_path': '../graph.json'},
])
def test_fixture_rejects_non_synthetic_or_escaping_path(fixture, change):
    path = fixture / 'probe.json'
    manifest = json.loads(path.read_text())
    manifest.update(change)
    path.write_text(json.dumps(manifest))
    with pytest.raises(ValueError):
        probe.read_fixture(fixture)


def test_graph_checksum_is_bound(fixture):
    with (fixture / 'graph.json').open('ab') as stream:
        stream.write(b' ')
    with pytest.raises(ValueError, match='checksum'):
        probe.read_fixture(fixture)


@pytest.mark.parametrize('failure', ['identity', '503', 'mcp', 'version'])
def test_invalid_response_stops_without_retries(fixture, monkeypatch, failure):
    remote = FakeRemote(fixture)

    def exchange(*args):
        status, headers, text = remote(*args)
        if failure == 'identity':
            headers['x-probe-manifest-sha256'] = 'wrong'
        elif failure == '503':
            status, text = 503, '{"error":{"code":"corpus_unavailable"}}'
        elif failure == 'mcp' and args[1]:
            envelope = json.loads(text)
            envelope['result']['isError'] = True
            text = json.dumps(envelope)
        elif failure == 'version' and '/v1/content' in args[0]:
            body = json.loads(text)
            body['corpus_version'] = 'wrong'
            text = json.dumps(body)
        return status, headers, text

    monkeypatch.setattr(probe, 'exchange', exchange)
    monkeypatch.setenv('PROBE_TOKEN', TOKEN)
    report = report_for(fixture)
    probe.execute(args_for(fixture), report)
    assert report['functional_gate'] == 'failed'
    assert report['workload_complete'] is False
    assert len(remote.calls) <= 19
    assert (fixture / 'report.json').exists()


def test_overload_is_rejected_outside_bursts(fixture, monkeypatch):
    remote = FakeRemote(fixture)
    report = report_for(fixture)
    report.update(origin=ORIGIN, identity=remote.identity)

    def overload(*args):
        _, headers, _ = remote(*args)
        return 503, headers, '{"error":{"code":"probe_overloaded"}}'

    monkeypatch.setattr(probe, 'exchange', overload)
    with pytest.raises(ValueError, match='no retry'):
        probe.run_batch(report, 'ordinary', [probe.request_spec('catalog')],
                        TOKEN, remote.nodes, time.monotonic() + 5)
    assert len(remote.calls) == 1


def test_request_and_time_budgets_fail_before_network(fixture, monkeypatch):
    remote = FakeRemote(fixture)
    monkeypatch.setattr(probe, 'exchange', remote)
    report = report_for(fixture)
    report.update(origin=ORIGIN, identity=remote.identity,
                  http_attempts=probe.MAX_REQUESTS)
    with pytest.raises(ValueError, match='request budget'):
        probe.run_batch(report, 'test', [probe.request_spec('status')],
                        TOKEN, remote.nodes, time.monotonic() + 5)
    with pytest.raises(ValueError, match='time budget'):
        probe.run_batch(report, 'test', [probe.request_spec('status')],
                        TOKEN, remote.nodes, time.monotonic() - 1)
    assert not remote.calls


def test_wrong_final_embedding_count_fails(fixture, monkeypatch):
    remote = FakeRemote(fixture)

    def wrong_count(*args):
        status, headers, text = remote(*args)
        if len(remote.calls) == 327:
            body = json.loads(text)
            body['embedded_queries'] = 176
            text = json.dumps(body)
        return status, headers, text

    monkeypatch.setattr(probe, 'exchange', wrong_count)
    monkeypatch.setenv('PROBE_TOKEN', TOKEN)
    report = report_for(fixture)
    probe.execute(args_for(fixture), report)
    assert report['functional_gate'] == 'failed'
    assert report['workload_complete'] is False


def test_only_joined_platform_cpu_affects_cpu_gate(fixture):
    report = report_for(fixture)
    report['requests'] = [{
        'phase': 'test', 'state': 'complete', 'success': True,
        'client_wall_ms': 100000, 'cpuTimeMs': 0,
        'telemetry': {'gateway': {'cpu_ms': 8, 'outcome': 'ok'}},
    }]
    probe.summarize(report)
    assert report['gateway_cpu_gate'] == 'failed'
    assert report['do_cpu_gate'] == 'unverified'
    assert report['memory_gate'] == 'unverified'


def test_hard_supervisor_timeout_persists_failure(tmp_path, monkeypatch):
    class Process:
        alive = True
        exitcode = None

        def start(self):
            pass

        def join(self, timeout=None):
            pass

        def is_alive(self):
            return self.alive

        def terminate(self):
            self.alive = False
            self.exitcode = -15

    process = Process()
    monkeypatch.setattr(probe.multiprocessing, 'get_context', lambda _: (
        Namespace(Process=lambda **kwargs: process)))
    ticks = iter([0, 0, 2])
    monkeypatch.setattr(probe.time, 'monotonic', lambda: next(ticks))
    output = tmp_path / 'timeout.json'
    assert probe.main(['--assets', str(tmp_path), '--base-url', ORIGIN,
                       '--out', str(output), '--max-load-seconds', '1']) == 1
    report = json.loads(output.read_text())
    assert report['error'] == 'Hard process time budget exhausted'
    assert report['functional_gate'] == 'failed'
    assert report['workload_complete'] is False
    assert report['requests'] == []


def test_http_redirect_is_returned_without_following(monkeypatch):
    requests = []

    class Response:
        status = 302

        def read(self, size):
            assert size == probe.MAX_RESPONSE_BYTES + 1
            return b'redirected'

        def getheaders(self):
            return [('Location', 'https://other.example')]

    class Connection:
        def __init__(self, hostname, timeout):
            assert hostname.endswith('.workers.dev')

        def request(self, method, path, body, headers):
            requests.append((method, path))

        def getresponse(self):
            return Response()

        def close(self):
            pass

    monkeypatch.setattr(probe.http.client, 'HTTPSConnection', Connection)
    status, _, _ = probe.exchange(ORIGIN + '/_probe/status', None, {}, 1)
    assert status == 302
    assert requests == [('GET', '/_probe/status')]
