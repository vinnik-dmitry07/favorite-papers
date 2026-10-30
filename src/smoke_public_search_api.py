'''Publish-check the retained public API without encoding the corpus again.

Compatibility is authenticated. REST/MCP checks carry no publication credential.
Failures disable semantic search, preserving the public catalog and paper text.
This is a bounded scripted integration check, not an autonomous quality test.
'''

from __future__ import annotations

import argparse
from datetime import date
import hashlib
import json
import os
from pathlib import Path
import re
import time
import urllib.parse

from run_real_search_probe import (
    fetch_identity, require, validate_compatibility, validate_content,
    validate_fetch, validate_mcp_search, validate_rest_search,
)
from run_retained_search_smoke import (
    PACKED_SHA, checked_json, exchange_once, load_fixture, persist,
)
from static_search_do_lifecycle import Cloudflare

WORKER_NAME = 'key-papers-search'
MAX_HTTP_ATTEMPTS = 80
MAX_SECONDS = 600
PUBLIC_LIMITS = {
    'query_texts': 1000, 'query_tokens_reserved': 512000,
    'compatibility_texts': 200, 'compatibility_tokens_reserved': 102400,
    'ai_timeout_ms': 20000,
}
REST_QUERIES = (
    'How can an inference system reduce the memory occupied by a long '
    'conversation\'s key value cache while preserving useful earlier context?',
    'Training-free key value cache compression or eviction for long '
    'multi-turn conversations preserving important earlier tokens',
)
MCP_QUERY = (
    'Which inference-time methods use feedback to revise a reasoning answer '
    'before returning it?'
)


def verify_worker_ownership(api):
    '''Read only; never replace an existing Worker without our bindings.'''
    body = api.request('/workers/scripts/' + WORKER_NAME + '/settings',
                       allow_absent=True)
    if body is None:
        return {'worker_name': WORKER_NAME, 'existing': False,
                'ownership': 'name_available'}
    result = body.get('result')
    require(isinstance(result, dict)
            and isinstance(result.get('bindings'), list),
            'Existing Worker settings do not identify the public API')
    bindings = result['bindings']
    require(all(isinstance(item, dict) and isinstance(item.get('name'), str)
                for item in bindings), 'Malformed existing Worker bindings')
    by_name = {item['name']: item for item in bindings}
    require(len(by_name) == len(bindings), 'Ambiguous existing Worker bindings')
    binding = by_name.get('PUBLIC_SEARCH', {})
    manifest = by_name.get('PUBLIC_MANIFEST_SHA', {})
    require(binding.get('type') == 'durable_object_namespace'
            and binding.get('class_name') == 'PublicSearch'
            and binding.get('script_name', WORKER_NAME) == WORKER_NAME
            and manifest.get('type') == 'plain_text'
            and manifest.get('text') == PACKED_SHA,
            'Existing Worker is not this retained public API')
    return {'worker_name': WORKER_NAME, 'existing': True,
            'ownership': 'verified_public_search_bindings',
            'manifest_sha256': PACKED_SHA}


def public_origin(value):
    parsed = urllib.parse.urlsplit(value)
    require(
        parsed.scheme == 'https' and parsed.hostname
        and parsed.hostname.startswith(WORKER_NAME + '.')
        and parsed.hostname.endswith('.workers.dev')
        and not parsed.username and not parsed.password and not parsed.port
        and parsed.path in ('', '/')
        and not parsed.query and not parsed.fragment,
        'Expected the dedicated key-papers-search workers.dev origin',
    )
    return value.rstrip('/')


def rpc_result(text):
    lines = [line[5:].strip() for line in text.splitlines()
             if line.startswith('data:')]
    body = json.loads(lines[-1] if lines else text)
    require(not body.get('error') and isinstance(body.get('result'), dict),
            'MCP returned a protocol error or invalid result')
    return body['result']


def deployment_pending(row):
    try:
        body = json.loads(row.get('response_text', ''))
    except (ValueError, TypeError):
        return False
    return (
        row.get('path') == '/admin/state' and row.get('method') == 'GET'
        and row.get('status') == 404 and isinstance(body, dict)
        and body.get('cloudflare_error') is True
        and body.get('status') == 404 and body.get('error_code') == 1042
        and body.get('error_name') == 'workers_dev_script_not_found'
    )


def validate_daily_budget(budget):
    require(isinstance(budget, dict) and budget.get('limits') == PUBLIC_LIMITS,
            'Public AI budget limits differ from the reviewed caps')
    date.fromisoformat(budget['day'])
    for name in ('query_texts', 'query_tokens_reserved',
                 'compatibility_texts', 'compatibility_tokens_reserved',
                 'ai_calls'):
        value = budget.get(name)
        require(isinstance(value, int) and not isinstance(value, bool)
                and value >= 0, 'Invalid daily budget counter: ' + name)
        if name in PUBLIC_LIMITS:
            require(value <= PUBLIC_LIMITS[name],
                    'Daily budget exceeds its cap: ' + name)
    require(budget['query_tokens_reserved'] == budget['query_texts'] * 512
            and budget['compatibility_tokens_reserved']
            == budget['compatibility_texts'] * 512,
            'Conservative token reservations are inconsistent')
    require(budget['query_texts'] <= budget['ai_calls']
            <= budget['query_texts'] + budget['compatibility_texts'],
            'AI call count is inconsistent with reserved inputs')


class PublicSmoke:
    def __init__(self, origin, token, publication, fixture, output, report,
                 exchange=exchange_once):
        self.origin = public_origin(origin)
        require(bool(token), 'PUBLICATION_TOKEN is required')
        require(re.fullmatch(r'[A-Za-z0-9_.:-]{1,160}', publication),
                'Invalid publication identity')
        self.token, self.publication = token, publication
        self.fixture, self.output, self.report = fixture, output, report
        self.exchange = exchange
        self.deadline = time.monotonic() + MAX_SECONDS
        self.identity_verified = False

    def request(self, kind, path, payload=None, *, admin=False,
                expected=200, raw=False, rollback=False):
        limit = MAX_HTTP_ATTEMPTS if rollback else MAX_HTTP_ATTEMPTS - 1
        require(len(self.report['requests']) < limit, 'HTTP budget exhausted')
        require(rollback or time.monotonic() < self.deadline,
                'Publication smoke deadline exhausted')
        parsed = urllib.parse.urlsplit(path)
        require(path.startswith('/') and not path.startswith('//')
                and not parsed.scheme and not parsed.netloc
                and not parsed.fragment, 'Only same-origin paths are allowed')
        require(not admin or parsed.path.startswith('/admin/'),
                'Publication token may only be sent to admin routes')
        headers = {'accept': 'application/json, text/plain, text/event-stream',
                   'mcp-protocol-version': '2025-06-18'}
        if admin:
            headers['x-publication-token'] = self.token
        row = {'kind': kind, 'path': path, 'method': 'GET' if payload is None
               else 'POST', 'authenticated_admin': admin, 'state': 'in_flight'}
        self.report['requests'].append(row)
        persist(self.report, self.output)
        started = time.monotonic()
        try:
            timeout = 20 if rollback else min(
                60, max(.01, self.deadline - time.monotonic()))
            status, _, text = self.exchange(
                self.origin + path, payload, headers, timeout)
            row.update(status=status, response_text=text)
            require(status == expected, f'Unexpected HTTP status: {status}')
            body = text if raw else json.loads(text)
            row['success'] = True
            return body
        except Exception as error:
            row.update(success=False, error=f'{type(error).__name__}: {error}')
            raise
        finally:
            row.update(state='completed',
                       elapsed_ms=(time.monotonic() - started) * 1000)
            persist(self.report, self.output)

    def state(self, *, initial=False):
        for attempt in range(3 if initial else 1):
            try:
                body = self.request('publication_state', '/admin/state',
                                    admin=True)
                break
            except ValueError:
                row = self.report['requests'][-1]
                if not initial or attempt == 2 or not deployment_pending(row):
                    raise
                self.report['requests'][-1]['startup_retry'] = True
                time.sleep(1)
        require(body.get('kind') == 'public-static-search'
                and body.get('manifest_sha256') == PACKED_SHA
                and body.get('publication_id') == self.publication
                and body.get('passage_count') == 40575,
                'Public API identity differs from the reviewed publication')
        if self.fixture:
            require(body.get('release_id')
                    == self.fixture['manifest']['release_id'],
                    'Public API release differs from retained assets')
        validate_daily_budget(body.get('budget'))
        self.identity_verified = True
        self.report['last_state'] = body
        persist(self.report, self.output)
        return body

    def deactivate(self, *, rollback=False):
        body = self.request('deactivate', '/admin/deactivate', {},
                            admin=True, rollback=rollback)
        require(body.get('active') is False, 'Deactivation unverified')
        self.report['semantic_active'] = False
        return body

    def paper(self, paper_id):
        if paper_id not in self.fixture['papers']:
            node = self.fixture['graph']['nodes'].get(paper_id)
            require(isinstance(node, dict), 'Paper is outside the catalog')
            if node.get('text', {}).get('available') is False:
                # Metadata-only MCP hits have no source text asset to load.
                self.fixture['papers'][paper_id] = {'text': ''}
                return
            name = hashlib.sha256(paper_id.encode()).hexdigest()
            release = self.fixture['manifest']['release_id']
            path = f'releases/{release}/papers/{name}.json'
            self.fixture['papers'][paper_id] = checked_json(
                self.fixture['root'] / 'corpus' / path,
                self.fixture['manifest']['files'][path])

    def tool(self, name, arguments):
        result = rpc_result(self.request('mcp_' + name, '/mcp', {
            'jsonrpc': '2.0', 'id': 1, 'method': 'tools/call',
            'params': {'name': name, 'arguments': arguments},
        }, raw=True))
        require(not result.get('isError'), 'MCP tool returned an error')
        body = result.get('structuredContent')
        require(isinstance(body, dict)
                and body == json.loads(result['content'][0]['text']),
                'MCP structured and text results disagree')
        return body

    def run(self):
        state = self.state(initial=True)
        self.deactivate()
        compatibility = state['compatibility']
        status = validate_compatibility(compatibility, self.fixture)
        require(status != 'failed',
                'Compatibility failed earlier; review before explicit reset')
        for _ in range(13):
            if status == 'passed':
                break
            previous = compatibility['checked']
            compatibility = self.request(
                'compatibility', '/admin/compatibility', {}, admin=True)
            status = validate_compatibility(
                compatibility, self.fixture, previous)
            require(status != 'failed' and compatibility['checked'] > previous,
                    'Compatibility failed or did not advance')
        require(status == 'passed', 'All 200 compatibility checks must pass')
        self.report['compatibility'] = compatibility
        self.report['compatibility_gate'] = 'passed'
        active = self.request('activate', '/admin/activate', {}, admin=True)
        require(active.get('active') is True, 'Publication did not activate')
        self.report['semantic_active'] = True

        health = self.request('public_health', '/health')
        require(health.get('status') == 'ready'
                and health.get('search_enabled') is True
                and health.get('manifest_sha256') == PACKED_SHA
                and health.get('publication_id') == self.publication
                and health.get('passage_count') == 40575,
                'Public health is not ready for this publication')
        manual = self.request('public_manual', '/', raw=True)
        llms = self.request('public_llms', '/llms.txt', raw=True)
        require('/v1/search' in manual and '/mcp' in manual
                and '/v1/search' in llms and '/mcp' in llms,
                'Agent entrypoints omit search or MCP instructions')
        spec = self.request('public_openapi', '/openapi.json')
        require(spec.get('openapi') == '3.1.0'
                and spec.get('servers', [{}])[0].get('url') == self.origin,
                'OpenAPI does not identify this origin')
        self.request('reject_unauthenticated_admin', '/admin/state',
                     expected=403)
        self.report['checks']['discovery_and_admin_auth'] = True

        key = 'arxiv:2402.03300'
        catalog = self.request('title_lookup', '/v1/catalog?q=DeepSeekMath')
        require(key in {p['id'] for p in catalog.get('papers', [])},
                'Catalog title lookup did not find DeepSeekMath')
        seen, cursor = [], None
        for _ in range(20):
            params = {'id': key, 'dir': 'in', 'limit': 24}
            if cursor:
                params['cursor'] = cursor
            page = self.request('incoming_citations', '/v1/citations?'
                                + urllib.parse.urlencode(params))
            seen.extend(item['id'] for item in page['neighbors'])
            cursor = page.get('next_cursor')
            if cursor is None:
                break
        expected = {e['source'] for e in self.fixture['graph']['in'][key]}
        require(cursor is None and len(seen) == len(expected)
                and set(seen) == expected, 'Citation traversal was incomplete')
        self.report['incoming_citations'] = len(seen)
        contents = self.request('contents', '/v1/contents?id=' + key)
        require(bool(contents.get('sections')), 'Paper section list is empty')
        found = self.request('literal_find', '/v1/find?id=' + key + '&q=64')
        require(bool(found.get('matches')), 'Literal lookup found no match')
        self.paper(key)
        offset = found['matches'][0]['start']
        body = self.request('read_at_match', '/v1/content?'
                            + urllib.parse.urlencode({
                                'id': key, 'offset': offset, 'length': 6000,
                                'version': found['corpus_version'],
                            }))
        validate_content(body, self.fixture, key, offset, 6000)
        self.report['checks']['catalog_graph_and_reading'] = True

        for query in REST_QUERIES:
            search = self.request(
                'semantic_query', '/v1/search?'
                + urllib.parse.urlencode({'q': query, 'k': 3}))
            for hit in search.get('hits', []):
                self.paper(hit['paper_id'])
            hit = validate_rest_search(search, self.fixture)[0]
            content = self.request('read_semantic_result', hit['content'])
            validate_content(content, self.fixture, hit['paper_id'],
                             hit['start'], 6000)
        self.report['checks']['rest_query_and_reformulation'] = True

        initialize = rpc_result(self.request('mcp_initialize', '/mcp', {
            'jsonrpc': '2.0', 'id': 1, 'method': 'initialize',
            'params': {'protocolVersion': '2025-06-18', 'capabilities': {},
                       'clientInfo': {'name': 'public-search-smoke',
                                      'version': '1'}},
        }, raw=True))
        require(initialize.get('serverInfo', {}).get('name') == 'key-papers',
                'MCP initialization did not identify the paper server')
        tools = rpc_result(self.request('mcp_tools', '/mcp', {
            'jsonrpc': '2.0', 'id': 2, 'method': 'tools/list',
        }, raw=True))['tools']
        names = {tool['name'] for tool in tools}
        require({'search', 'fetch', 'list_papers'} <= names
                and all(t.get('outputSchema') for t in tools),
                'Required MCP tools or schemas are missing')
        result = self.tool('search', {'query': MCP_QUERY})
        for item in result.get('results', []):
            self.paper(fetch_identity(item['id'])['paper'])
        results = validate_mcp_search(result, self.fixture)
        parts = (item for item in results
                 if fetch_identity(item['id'])['start'] is not None)
        chosen = next(parts, None)
        require(chosen is not None, 'MCP search returned no text part')
        document = self.tool('fetch', {'id': chosen['id']})
        validate_fetch(document, self.fixture, chosen['id'])
        self.report['checks']['mcp_search_fetch'] = True
        final = self.state()
        require(final.get('active') is True, 'Publication lost active state')
        self.report.update(ok=True, semantic_active=True)


def run(origin, token, publication, restored, output, *, deactivate_only=False,
        exchange=exchange_once):
    report = {
        'schema_version': 1, 'kind': 'public-retained-static-api-publication',
        'ok': False, 'origin': origin, 'publication_id': publication,
        'manifest_sha256': PACKED_SHA, 'checks': {}, 'requests': [],
        'max_http_attempts': MAX_HTTP_ATTEMPTS,
        'max_seconds': MAX_SECONDS, 'rollback_timeout_seconds': 20,
        'corpus_reencoded': False, 'autonomous_agent_evaluation': False,
        'query_submissions_planned': 0 if deactivate_only else 3,
        'compatibility_gate': 'unverified', 'semantic_active': 'unverified',
        'provider_retry_policy': 'No provider retries or automatic resets',
    }
    persist(report, output)
    smoke = None
    started = time.monotonic()
    try:
        fixture = None if deactivate_only else load_fixture(restored)
        smoke = PublicSmoke(origin, token, publication, fixture, output,
                            report, exchange)
        if deactivate_only:
            smoke.state(initial=True)
            smoke.deactivate(rollback=True)
            report['ok'] = True
        else:
            smoke.run()
    except Exception as error:
        report['error'] = f'{type(error).__name__}: {error}'
        if smoke is not None and smoke.identity_verified:
            try:
                smoke.deactivate(rollback=True)
                report['failure_deactivation'] = 'verified'
            except Exception as rollback_error:
                report['failure_deactivation'] = 'unverified'
                report['deactivation_error'] = str(rollback_error)
    finally:
        report['elapsed_seconds'] = time.monotonic() - started
        persist(report, output)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--origin')
    parser.add_argument('--publication-id')
    parser.add_argument('--restored', type=Path)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--deactivate-only', action='store_true')
    parser.add_argument('--check-account-ownership', action='store_true')
    args = parser.parse_args()
    if args.check_account_ownership:
        if (args.deactivate_only or args.origin
                or args.publication_id or args.restored):
            parser.error('Ownership checking is a separate read-only mode')
        report = verify_worker_ownership(Cloudflare())
        persist(report, args.out)
        print(json.dumps(report))
        return
    if not args.origin or not args.publication_id:
        parser.error('--origin and --publication-id are required')
    if not args.deactivate_only and args.restored is None:
        parser.error('--restored is required for publication checks')
    report = run(
        args.origin, os.environ.get('PUBLICATION_TOKEN', ''),
        args.publication_id, args.restored, args.out,
        deactivate_only=args.deactivate_only,
    )
    print(json.dumps({key: report.get(key) for key in (
        'ok', 'origin', 'checks', 'semantic_active', 'error',
        'failure_deactivation')}))
    raise SystemExit(0 if report['ok'] else 1)


if __name__ == '__main__':
    main()
