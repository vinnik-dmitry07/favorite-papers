'''Public publication is explicit, bounded, authenticated and reversible.'''

import ast
import base64
from datetime import date
import json
from pathlib import Path
import re
import subprocess
import urllib.parse

import pytest
import yaml

import smoke_public_search_api as publication
from test_geometry_probe_workflow import evaluate


ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://key-papers-search.example.workers.dev'
KEY = 'arxiv:2402.03300'
RELEASE = 'test-release'
TOKEN = 'private-publication-token'


def workflow():
    path = ROOT / '.github/workflows/agent-api.yml'
    return yaml.safe_load(path.read_text())


def job():
    return workflow()['jobs']['publish_retained_api']


def compatibility(checked=0):
    return {
        'status': 'passed' if checked == 200 else 'not_started',
        'checked': checked, 'expected': 200, 'threshold': .999,
        'min_cosine': 1.0 if checked else None,
        'results': [{'index': n, 'cosine': 1.0, 'remote_norm': 1.0}
                    for n in range(checked)],
    }


def budget():
    return {
        'day': date.today().isoformat(), 'query_texts': 0,
        'query_tokens_reserved': 0, 'compatibility_texts': 0,
        'compatibility_tokens_reserved': 0, 'ai_calls': 0,
        'limits': publication.PUBLIC_LIMITS.copy(),
    }


def fixture():
    text = '64 ' + 'A scientific paper about reasoning and memory. ' * 200
    row = {'paper_id': KEY, 'chunk_index': 0, 'start': 0, 'end': 60}
    return {
        'manifest': {'release_id': RELEASE,
                     'compatibility_indices': list(range(200))},
        'papers': {KEY: {'text': text}}, 'by_chunk': {(KEY, 0): row},
        'graph': {'nodes': {KEY: {'url': 'https://arxiv.org/abs/2402.03300'}},
                  'in': {KEY: [{'source': 'catalog-citing-paper'}]}},
    }


class FakeApi:
    def __init__(self, *, corrupt_read=False, startup=None, already_passed=False):
        self.fixture = fixture()
        self.active = False
        self.checked = 200 if already_passed else 0
        self.budget = budget()
        self.calls = []
        self.corrupt_read = corrupt_read
        self.startup = startup

    def state(self):
        return {
            'kind': 'public-static-search', 'manifest_sha256': publication.PACKED_SHA,
            'publication_id': 'publication-1', 'passage_count': 40575,
            'release_id': RELEASE, 'active': self.active,
            'compatibility': compatibility(self.checked),
            'budget': self.budget.copy(),
        }

    def __call__(self, url, payload, headers, timeout):
        parsed = urllib.parse.urlsplit(url)
        path = parsed.path
        self.calls.append((path, payload, headers.copy()))
        if path == '/admin/state' and self.startup:
            status, body = self.startup
            self.startup = None
            return status, {}, json.dumps(body)
        if path.startswith('/admin/') and headers.get('x-publication-token') != TOKEN:
            return 403, {}, json.dumps({'error': {'code': 'unauthorized'}})
        if path == '/admin/state':
            body = self.state()
        elif path == '/admin/deactivate':
            self.active = False
            body = self.state()
        elif path == '/admin/activate':
            assert self.checked == 200
            self.active = True
            body = self.state()
        elif path == '/admin/compatibility':
            self.checked = min(200, self.checked + 16)
            self.budget.update(compatibility_texts=self.checked,
                               compatibility_tokens_reserved=self.checked * 512)
            self.budget['ai_calls'] += 1
            body = compatibility(self.checked)
            if self.checked < 200:
                body['status'] = 'running'
        elif path == '/health':
            body = {**self.state(), 'status': 'ready', 'search_enabled': self.active}
        elif path in ('/', '/llms.txt'):
            return 200, {}, 'Use /v1/search and /mcp for paper research.'
        elif path == '/openapi.json':
            body = {'openapi': '3.1.0', 'servers': [{'url': ORIGIN}]}
        elif path == '/v1/catalog':
            body = {'papers': [{'id': KEY}]}
        elif path == '/v1/citations':
            body = {'neighbors': [{'id': 'catalog-citing-paper'}],
                    'next_cursor': None}
        elif path == '/v1/contents':
            body = {'sections': [{'title': 'Introduction', 'offset': 0}]}
        elif path == '/v1/find':
            body = {'matches': [{'start': 0}], 'corpus_version': RELEASE}
        elif path == '/v1/content':
            query = urllib.parse.parse_qs(parsed.query)
            offset = int(query.get('offset', ['0'])[0])
            length = int(query.get('length', ['6000'])[0])
            text = self.fixture['papers'][KEY]['text']
            end = min(len(text), offset + length)
            body = {'paper_id': KEY, 'corpus_version': RELEASE, 'available': True,
                    'offset': offset, 'total_length': len(text),
                    'next_offset': end if end < len(text) else None,
                    'text': 'wrong text' if self.corrupt_read else text[offset:end]}
        elif path == '/v1/search':
            assert self.active
            self.query_charge()
            body = {'corpus_version': RELEASE, 'hits': [{
                'paper_id': KEY, 'chunk_index': 0, 'start': 0, 'end': 60,
                'score': .9, 'corpus_version': RELEASE,
                'snippet': self.fixture['papers'][KEY]['text'][:60],
                'url': self.fixture['graph']['nodes'][KEY]['url'],
                'content': '/v1/content?' + urllib.parse.urlencode({
                    'id': KEY, 'offset': 0, 'version': RELEASE}),
            }]}
        elif path == '/mcp':
            body = self.mcp(payload)
        else:
            raise AssertionError(path)
        return 200, {}, json.dumps(body)

    def query_charge(self):
        self.budget['query_texts'] += 1
        self.budget['query_tokens_reserved'] += 512
        self.budget['ai_calls'] += 1

    def mcp(self, payload):
        identity = {'paper': KEY, 'version': RELEASE, 'start': 0}
        encoded = base64.urlsafe_b64encode(json.dumps(identity).encode()).decode()
        document_id = 'doc:' + encoded.rstrip('=')
        if payload['method'] == 'initialize':
            result = {'serverInfo': {'name': 'key-papers'}}
        elif payload['method'] == 'tools/list':
            result = {'tools': [{'name': name, 'outputSchema': {'type': 'object'}}
                                for name in ('search', 'fetch', 'list_papers')]}
        else:
            name = payload['params']['name']
            if name == 'search':
                assert self.active
                self.query_charge()
                content = {'results': [{'id': document_id, 'title': 'Paper',
                                       'url': 'https://arxiv.org/abs/2402.03300'}]}
            else:
                assert name == 'fetch'
                text = self.fixture['papers'][KEY]['text']
                content = {
                    'id': document_id, 'text': text[:16000],
                    'url': 'https://arxiv.org/abs/2402.03300',
                    'metadata': {'paper_id': KEY, 'corpus_version': RELEASE,
                                 'item_type': 'text_part', 'start': 0,
                                 'end': min(len(text), 16000),
                                 'total_length': len(text)},
                }
            result = {'structuredContent': content,
                      'content': [{'type': 'text', 'text': json.dumps(content)}]}
        return {'jsonrpc': '2.0', 'id': payload['id'], 'result': result}


def execute(tmp_path, monkeypatch, api):
    monkeypatch.setattr(publication, 'load_fixture', lambda _: api.fixture)
    return publication.run(ORIGIN, TOKEN, 'publication-1', tmp_path,
                           tmp_path / 'report.json', exchange=api)


def test_complete_publication_checks_rest_mcp_and_canonical_reads(
        tmp_path, monkeypatch):
    api = FakeApi()
    report = execute(tmp_path, monkeypatch, api)
    assert report['ok'] is True and report['semantic_active'] is True
    assert report['last_state']['budget']['query_texts'] == 3
    assert report['compatibility']['checked'] == 200
    assert report['incoming_citations'] == 1
    assert len(report['requests']) < publication.MAX_HTTP_ATTEMPTS
    assert all(report['checks'].values())
    for path, _, headers in api.calls:
        if not path.startswith('/admin/'):
            assert 'x-publication-token' not in headers
    assert TOKEN not in (tmp_path / 'report.json').read_text()


def test_failed_read_disables_semantic_without_deletion(
        tmp_path, monkeypatch):
    api = FakeApi(corrupt_read=True)
    report = execute(tmp_path, monkeypatch, api)
    assert report['ok'] is False and api.active is False
    assert report['failure_deactivation'] == 'verified'
    assert api.calls[-1][0] == '/admin/deactivate'
    assert all('delete' not in path for path, _, _ in api.calls)


def test_passed_compatibility_is_not_recomputed_after_restart(
        tmp_path, monkeypatch):
    api = FakeApi(already_passed=True)
    assert execute(tmp_path, monkeypatch, api)['ok'] is True
    assert not any(path == '/admin/compatibility' for path, _, _ in api.calls)


@pytest.mark.parametrize('status,error,retries', [
    (404, {'cloudflare_error': True, 'status': 404, 'error_code': 1042,
           'error_name': 'workers_dev_script_not_found'}, True),
    (404, {'error': 'missing'}, False),
    (403, {'error': 'forbidden'}, False),
    (503, {'error': 'unavailable'}, False),
])
def test_only_exact_initial_routing_error_is_retried(
        tmp_path, monkeypatch, status, error, retries):
    monkeypatch.setattr(publication.time, 'sleep', lambda _: None)
    api = FakeApi(startup=(status, error), already_passed=True)
    report = execute(tmp_path, monkeypatch, api)
    assert report['ok'] is retries
    if not retries:
        assert len(api.calls) == 1


def test_wrong_publication_identity_prevents_mutations(tmp_path, monkeypatch):
    api = FakeApi()
    original = api.state

    def wrong_state():
        return {**original(), 'publication_id': 'another-deployment'}

    api.state = wrong_state
    report = execute(tmp_path, monkeypatch, api)
    assert report['ok'] is False
    assert [path for path, _, _ in api.calls] == ['/admin/state']


@pytest.mark.parametrize('origin', [
    'https://key-papers-api.example.workers.dev', 'https://example.com',
    ORIGIN + '/path', ORIGIN + '?query=1',
    'https://secret@key-papers-search.example.workers.dev',
])
def test_origin_cannot_target_old_production_or_a_foreign_service(origin):
    with pytest.raises(ValueError):
        publication.public_origin(origin)


@pytest.mark.parametrize('existing', [False, True])
def test_ownership_checks_only_the_dedicated_name_without_mutation(existing):
    bindings = [
        {'name': 'PUBLIC_SEARCH', 'type': 'durable_object_namespace',
         'class_name': 'PublicSearch'},
        {'name': 'PUBLIC_MANIFEST_SHA', 'type': 'plain_text',
         'text': publication.PACKED_SHA},
    ]

    class Api:
        def request(self, path, **kwargs):
            assert path == '/workers/scripts/key-papers-search/settings'
            assert kwargs == {'allow_absent': True}
            return {'result': {'bindings': bindings}} if existing else None

    result = publication.verify_worker_ownership(Api())
    assert result['existing'] is existing


@pytest.mark.parametrize('bindings', [
    [], [{'name': 'PUBLIC_SEARCH', 'type': 'service'}],
    [{'name': 'PUBLIC_SEARCH', 'type': 'durable_object_namespace',
      'class_name': 'AnotherClass'}],
])
def test_unrecognized_existing_worker_is_never_overwritten(bindings):
    class Api:
        def request(self, *args, **kwargs):
            return {'result': {'bindings': bindings}}

    with pytest.raises(ValueError, match='not this retained public API'):
        publication.verify_worker_ownership(Api())


def test_ownership_permission_and_server_failures_are_not_absence():
    class Api:
        def request(self, *args, **kwargs):
            raise ValueError('Cloudflare HTTP 403')

    with pytest.raises(ValueError, match='403'):
        publication.verify_worker_ownership(Api())


def test_daily_budget_rejects_changed_caps_and_inconsistent_reservations():
    publication.validate_daily_budget(budget())
    for values in ({'query_texts': 1001}, {'query_texts': 1},
                   {'query_tokens_reserved': -1}, {'query_texts': True},
                   {'limits': {}}, {'day': 'not-a-date'}, {'ai_calls': 1000}):
        with pytest.raises((ValueError, TypeError)):
            publication.validate_daily_budget({**budget(), **values})


def test_metadata_only_card_does_not_require_a_text_file(tmp_path):
    data = fixture()
    data['graph']['nodes']['catalog-only'] = {'text': {'available': False}}
    smoke = publication.PublicSmoke(
        ORIGIN, TOKEN, 'publication-1', data, tmp_path / 'report.json',
        {'requests': []}, exchange=FakeApi())
    smoke.paper('catalog-only')
    assert data['papers']['catalog-only'] == {'text': ''}
    with pytest.raises(ValueError, match='outside the catalog'):
        smoke.paper('unknown-paper')


@pytest.mark.parametrize('start,passes', [(None, True), (0, False)])
def test_mcp_mixed_metadata_and_semantic_results_verify_text_availability(
        tmp_path, monkeypatch, start, passes):
    api = FakeApi(already_passed=True)
    api.fixture['graph']['nodes']['catalog-only'] = {'text': {'available': False}}
    original = api.mcp

    def with_metadata(payload):
        result = original(payload)
        if payload.get('params', {}).get('name') == 'search':
            identity = {'paper': 'catalog-only', 'version': RELEASE, 'start': start}
            encoded = base64.urlsafe_b64encode(json.dumps(identity).encode()).decode()
            body = result['result']['structuredContent']
            body['results'].insert(0, {
                'id': 'doc:' + encoded.rstrip('='),
                'title': 'Catalog-only paper', 'url': 'https://example.com/paper',
            })
            result['result']['content'][0]['text'] = json.dumps(body)
        return result

    api.mcp = with_metadata
    report = execute(tmp_path, monkeypatch, api)
    assert report['ok'] is passes
    assert api.active is passes


def test_manual_publish_is_exclusive_and_shares_cloudflare_lock():
    definition = workflow()
    values = {'inputs.do_probe_phase': 'publish'}
    assert 'push' not in definition['on']
    inputs = definition['on']['workflow_dispatch']['inputs']
    assert inputs['static_probe']['default'] is False
    assert 'publish' in inputs['do_probe_phase']['options']
    selected = [name for name, value in definition['jobs'].items()
                if 'if' in value and evaluate(value['if'], **values)]
    assert selected == ['publish_retained_api']
    for key, value in [('github.event_name', 'pull_request'),
                       ('inputs.static_probe', False),
                       ('inputs.probe_runtime', 'worker'),
                       ('inputs.free_plan_confirmed', False),
                       ('inputs.do_probe_phase', 'retained')]:
        assert not evaluate(job()['if'], **{**values, key: value})
    group = definition['concurrency']['group']
    expression = group.split('${{', 1)[1].rsplit('}}', 1)[0]
    assert evaluate(expression, **values) == 'cloudflare'


def test_publication_reuses_artifact_without_encoding_or_probe_cleanup():
    commands = '\n'.join(step.get('run', '') for step in job()['steps'])
    for expected in ('actions/artifacts/12715563729/zip',
                     'python src/restore_full_search_artifact.py',
                     '--config wrangler.public-search.toml',
                     '--var "PUBLICATION_ID:$PUBLICATION_ID"',
                     'python src/smoke_public_search_api.py',
                     '--deactivate-only'):
        assert expected in commands
    for forbidden in ('publish_agent_index.py', 'embed_real_search_probe.py',
                      'AutoModel', 'requirements-torch-probe',
                      'static_search_do_lifecycle.py', 'wrangler delete',
                      '--config wrangler.toml', 'gh workflow run'):
        assert forbidden not in commands
    assert job()['env']['PUBLIC_WORKER_NAME'] == publication.WORKER_NAME
    assert job()['env']['PUBLICATION_ID'] == (
        '${{ github.run_id }}-${{ github.run_attempt }}-${{ github.sha }}')
    assert job()['needs'] == 'offline' and job()['timeout-minutes'] <= 30
    for step in job()['steps']:
        if 'npm --prefix' in step.get('run', ''):
            assert not any('secrets.' in str(v) for v in step.get('env', {}).values())
        if step.get('uses', '').startswith('actions/upload-artifact'):
            assert 'secret' not in step['with']['path']
            assert 'RUNNER_TEMP' not in step['with']['path']
            assert step['with']['name'] != 'agent-api-discovery'
    steps = {step['id']: step for step in job()['steps'] if 'id' in step}
    assert steps['smoke']['continue-on-error'] is True
    assert 'always()' in steps['deactivate']['if']
    assert 'steps.smoke.outcome != \'success\'' in steps['deactivate']['if']
    assert 'CLOUDFLARE_API_TOKEN' not in steps['smoke'].get('env', {})
    assert list(steps).index('ownership') < list(steps).index('deploy')
    assert '--check-account-ownership' in steps['ownership']['run']


def test_workflow_embedded_commands_parse_without_credentials():
    for step in job()['steps']:
        command = step.get('run', '')
        if command:
            subprocess.run(['bash', '-n'], input=command, text=True, check=True)
            pattern = r'''<<'PYTHON'\n(.*?)\nPYTHON'''
            for code in re.findall(pattern, command, re.S):
                ast.parse(code)
