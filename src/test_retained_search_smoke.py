'''The two-query HTTP smoke fails closed and never retries provider work.'''

import hashlib
from io import BytesIO
import json
import urllib.parse

import pytest

import run_retained_search_smoke as smoke


def fixture(tmp_path):
    paper_id, release = 'arxiv:2402.03300', 'b' * 64
    text = 'Canonical text of the returned paper, with useful context.'
    paper = {'paper_id': paper_id, 'text': text}
    relative = f'releases/{release}/papers/{hashlib.sha256(paper_id.encode()).hexdigest()}.json'
    path = tmp_path / 'corpus' / relative
    path.parent.mkdir(parents=True)
    path.write_text(json.dumps(paper))
    row = {'paper_id': paper_id, 'chunk_index': 0, 'start': 0, 'end': len(text)}
    return {
        'root': tmp_path, 'manifest': {
            'release_id': release, 'compatibility_indices': list(range(200)),
            'files': {relative: hashlib.sha256(path.read_bytes()).hexdigest()},
        },
        'papers': {}, 'by_chunk': {(paper_id, 0): row},
        'graph': {'nodes': {paper_id: {'url': 'https://example.org/paper'}}},
    }


class Server:
    def __init__(self, value, failure=None):
        self.fixture, self.failure = value, failure
        self.checked = self.queries = self.calls = 0
        self.paths = []

    def budget(self):
        return {
            'compatibility_texts': self.checked, 'query_texts': self.queries,
            'total_texts': self.checked + self.queries,
            'input_tokens': 10 * (self.checked + self.queries),
            'ai_calls': self.calls,
            'limits': {'total_texts': 300, 'query_texts': 24, 'input_tokens': 153600},
        }

    def compatibility(self):
        return {
            'status': 'passed' if self.checked == 200 else ('running' if self.checked else 'not_started'),
            'checked': self.checked, 'expected': 200, 'threshold': .999,
            'min_cosine': 1 if self.checked else None,
            'results': [{'index': n, 'cosine': 1, 'remote_norm': 1}
                        for n in range(self.checked)],
            'budget': self.budget(), 'manifest_sha256': smoke.PACKED_SHA,
            'release_id': self.fixture['manifest']['release_id'],
        }

    def __call__(self, url, payload, headers, timeout):
        parsed = urllib.parse.urlsplit(url)
        self.paths.append(parsed.path)
        assert timeout <= 60
        assert headers['x-probe-token'] == 'secret'
        release = self.fixture['manifest']['release_id']
        paper_id = next(iter(self.fixture['graph']['nodes']))
        if parsed.path == '/probe/info':
            body = {
                'probe_type': 'real-full-corpus', 'runtime': 'durable-object',
                'scope': 'full', 'synthetic': False,
                'manifest_sha256': smoke.PACKED_SHA,
                'source_manifest_sha256': smoke.CANONICAL_SHA,
                'passage_count': 40575, 'release_id': release,
                'compatibility_indices': list(range(200)),
                'compatibility': self.compatibility(), 'budget': self.budget(),
            }
        elif parsed.path == '/probe/compatibility':
            assert payload == {}
            self.checked = min(200, self.checked + 16)
            self.calls += 1
            if self.failure == 'ambiguous_compatibility':
                raise TimeoutError('provider may have received this batch')
            body = self.compatibility()
            if self.failure == 'failed_cosine':
                body['status'] = 'failed'
        elif parsed.path == '/health':
            body = {'search_enabled': True, 'scope': 'full', 'compatibility_gate': 'passed'}
        elif parsed.path == '/v1/search':
            self.queries += 1
            self.calls += 1
            assert urllib.parse.parse_qs(parsed.query)['q'] == [smoke.QUERIES[self.queries - 1]]
            if self.failure == 'ambiguous_query':
                raise TimeoutError('provider may have received the query')
            relative = next(iter(self.fixture['manifest']['files']))
            paper = json.loads((self.fixture['root'] / 'corpus' / relative).read_text())
            body = {'corpus_version': release, 'hits': [{
                'paper_id': paper_id, 'chunk_index': 0, 'start': 0, 'end': len(paper['text']),
                'corpus_version': release, 'score': .3, 'snippet': paper['text'],
                'url': 'https://example.org/paper',
                'content': '/v1/content?' + urllib.parse.urlencode(
                    {'id': paper_id, 'offset': 0, 'version': release}),
            }]}
            if self.failure == 'off_origin_read':
                body['hits'][0]['content'] = 'https://malicious.example/v1/content'
            if self.failure == 'empty_hits':
                body['hits'] = []
        elif parsed.path == '/v1/content':
            text = self.fixture['papers'][paper_id]['text']
            body = {
                'paper_id': paper_id, 'corpus_version': release, 'available': True,
                'offset': 0, 'total_length': len(text), 'next_offset': None, 'text': text,
            }
            if self.failure == 'read_consumes_provider':
                self.queries += 1
                self.calls += 1
        else:
            pytest.fail('Unexpected endpoint: ' + parsed.path)
        identity = {
            'x-probe-runtime': 'durable-object', 'x-probe-kind': 'real-full-corpus',
            'x-probe-synthetic': 'false', 'x-probe-manifest-sha256': smoke.PACKED_SHA,
            'x-probe-object-id': 'same-object', 'x-probe-boot-id': 'boot',
            'x-probe-marker': headers['x-probe-marker'],
        }
        if self.failure == 'wrong_identity':
            identity['x-probe-kind'] = 'geometry-fixture'
        return 200, identity, json.dumps(body)


def run(tmp_path, monkeypatch, failure=None, authorization=2):
    value = fixture(tmp_path)
    monkeypatch.setattr(smoke, 'load_fixture', lambda root: value)
    server = Server(value, failure)
    output = tmp_path / 'run.json'
    report = smoke.run('https://probe.example', 'secret', tmp_path, output,
                       authorization, exchange=server)
    assert report == json.loads(output.read_text())
    assert 'secret' not in output.read_text()
    return report, server


def test_exact_two_new_queries_read_first_returned_paper_and_record_ledger(tmp_path, monkeypatch):
    report, server = run(tmp_path, monkeypatch)
    assert report['smoke_gate'] == 'passed', report.get('error')
    assert report['workload_complete'] is True
    assert server.paths.count('/probe/compatibility') == 13
    assert server.paths.count('/v1/search') == server.paths.count('/v1/content') == 2
    assert report['budget']['total_texts'] == 202
    assert report['budget']['ai_calls'] == 15
    assert report['budget']['query_texts'] == 2
    assert len(report['requests']) < smoke.MAX_HTTP_ATTEMPTS
    for journey in report['journeys']:
        assert journey['selected_paper_id'] == journey['hits'][0]['paper_id']
        assert journey['read_body']['text']
        assert journey['ledger_after']['query_texts'] - journey['ledger_before']['query_texts'] == 1
    assert all(row['status'] == 200 and row['elapsed_ms'] >= 0 for row in report['requests'])
    assert report['autonomous_agent_evaluation'] is False
    assert report['heldout_quality'] == report['production_readiness'] == 'unverified'


@pytest.mark.parametrize('failure,searches,reads,batches', [
    ('ambiguous_compatibility', 0, 0, 1), ('failed_cosine', 0, 0, 1),
    ('ambiguous_query', 1, 0, 13), ('empty_hits', 1, 0, 13),
    ('off_origin_read', 1, 0, 13), ('read_consumes_provider', 1, 1, 13),
    ('wrong_identity', 0, 0, 0),
])
def test_first_failure_stops_all_provider_work_but_recovers_read_only_ledger(
        tmp_path, monkeypatch, failure, searches, reads, batches):
    report, server = run(tmp_path, monkeypatch, failure)
    assert report['smoke_gate'] == 'failed'
    assert report['workload_complete'] is False
    assert report['error']
    assert server.paths.count('/v1/search') == searches
    assert server.paths.count('/v1/content') == reads
    assert server.paths.count('/probe/compatibility') == batches
    assert server.paths[-1] == '/probe/info'
    assert report['requests'][-1]['kind'] == 'ledger_after_failure_read_only'
    if failure.startswith('ambiguous'):
        failed = next(row for row in report['requests'] if 'error' in row)
        assert failed['state'] == 'completed' and failed['elapsed_ms'] >= 0
        assert 'TimeoutError' in failed['error']


@pytest.mark.parametrize('authorization', [0, 1, 3, 24])
def test_no_http_without_exact_explicit_two_query_authorization(tmp_path, monkeypatch, authorization):
    report, server = run(tmp_path, monkeypatch, authorization=authorization)
    assert report['smoke_gate'] == 'failed'
    assert server.paths == []


def test_queries_are_checked_against_every_frozen_query():
    frozen = {'queries': [{'query': f'Frozen diagnostic {i}'} for i in range(2064)]}
    smoke.validate_fresh_queries(frozen)
    frozen['queries'][1024]['query'] = '  ' + smoke.QUERIES[1].upper() + '  '
    with pytest.raises(ValueError, match='absent from frozen'):
        smoke.validate_fresh_queries(frozen)


def test_restore_identity_is_authenticated_before_network(tmp_path):
    (tmp_path / 'restoration.json').write_text('{}')
    with pytest.raises(ValueError, match='Restoration identity'):
        smoke.load_fixture(tmp_path)


def test_redirects_cannot_forward_the_probe_token():
    request = urllib.parse.urlsplit('https://probe.example')
    assert smoke.NoRedirect().redirect_request(request, None, 302, '', {},
                                               'https://elsewhere.example') is None


@pytest.mark.parametrize('payload', [None, {}])
def test_exchange_sends_application_identity_and_preserves_auth(
        monkeypatch, payload):
    captured = []

    class Response(BytesIO):
        status = 200
        headers = {'content-type': 'application/json'}

    class Opener:
        def open(self, request, timeout):
            captured.append((request, timeout))
            return Response(b'{}')

    def build_opener(*handlers):
        assert len(handlers) == 1
        assert isinstance(handlers[0], smoke.NoRedirect)
        return Opener()

    monkeypatch.setattr(smoke.urllib.request, 'build_opener', build_opener)
    assert smoke.exchange_once(
        'https://probe.example/probe/info', payload,
        {'x-probe-token': 'test-probe-secret'}, 12,
    ) == (200, {'content-type': 'application/json'}, '{}')
    assert len(captured) == 1
    request, timeout = captured[0]
    assert timeout == 12
    assert request.get_header('User-agent') == (
        'favorite-papers-static-probe/1.0 '
        '(+https://github.com/vinnik-dmitry07/favorite-papers)'
    )
    assert request.get_header('X-probe-token') == 'test-probe-secret'
    assert request.get_method() == ('GET' if payload is None else 'POST')
