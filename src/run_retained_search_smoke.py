'''Run exactly two fresh HTTP search -> returned-paper read smoke journeys.

This is a bounded plumbing check of retained genuine corpus embeddings and live
query embeddings. It is not an autonomous-agent evaluation or held-out quality
test. No corpus encoding, model loading, provider retries, or gold targets.
'''

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid

from restore_full_search_artifact import ARTIFACT_ID, ARTIFACT_SHA256, RUN_ID
from run_real_search_probe import (
    require, validate_budget, validate_compatibility, validate_content,
    validate_rest_search,
)
from run_static_search_probe import PROBE_USER_AGENT

PACKED_SHA = '6b9c87883f525a128eb9a48aead5914d9524ba2f7433ff3b14c62b3c0d970b47'
CANONICAL_SHA = 'ad36309a7b1823dd64eab28658602408afc69054aa2159b4d63074cfbe04d8fd'
FROZEN_SHA = '049e5e887505ec9c19e030559034ff5f999388c7722af0b42cfa836570d8d556'
QUERIES = (
    'How can an inference system reduce the memory occupied by a long '
    'conversation\'s key value cache while preserving useful earlier context?',
    'Which methods let a language model spend extra computation checking and '
    'revising a difficult reasoning answer before returning it?',
)
QUERY_SUBMISSIONS = 2
MAX_HTTP_ATTEMPTS = 32
MAX_LOAD_SECONDS = 600


def checked_json(path, expected):
    raw = Path(path).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == expected,
            'Retained evidence hash differs: ' + str(path))
    return json.loads(raw)


def validate_fresh_queries(frozen):
    def normalize(text):
        return ' '.join(text.casefold().split())

    items = frozen.get('queries')
    require(isinstance(items, list) and len(items) == 2064,
            'Expected the authenticated 2064 frozen queries')
    existing = {normalize(item['query']) for item in items}
    fresh = {normalize(text) for text in QUERIES}
    require(len(fresh) == QUERY_SUBMISSIONS and not fresh & existing,
            'Smoke queries must be distinct and absent from frozen diagnostics')


def load_fixture(root):
    root = Path(root)
    restoration = json.loads((root / 'restoration.json').read_text())
    for key, expected in {
        'run_id': RUN_ID, 'artifact_id': ARTIFACT_ID,
        'artifact_sha256': ARTIFACT_SHA256,
        'canonical_manifest_sha256': CANONICAL_SHA,
        'packed_manifest_sha256': PACKED_SHA,
        'query_manifest_sha256': FROZEN_SHA,
        'passages': 40575, 'queries': 2064,
        'restored_assets_match_historical_run': True,
        'admission_certificate_issued': False,
        'provider_calls': 0, 'model_loaded': False, 'production_ready': False,
    }.items():
        require(restoration.get(key) == expected,
                'Restoration identity differs: ' + key)
    packed = checked_json(root / 'runtime/probe.json', PACKED_SHA)
    canonical = checked_json(root / 'corpus/probe.json', CANONICAL_SHA)
    frozen = checked_json(root / 'corpus/quality-combined-frozen.json', FROZEN_SHA)
    validate_fresh_queries(frozen)
    require(packed.get('kind') == 'full-corpus-int8'
            and packed.get('synthetic') is False
            and packed.get('passage_count') == 40575
            and packed.get('source_manifest_sha256') == CANONICAL_SHA,
            'Expected the pinned genuine full-corpus protocol')
    release = canonical['release_id']
    graph_path = f'releases/{release}/graph.json'
    graph = checked_json(root / 'corpus' / graph_path,
                         canonical['files'][graph_path])
    return {
        'root': root, 'restoration': restoration,
        'manifest': {**canonical,
                     'compatibility_indices': packed['compatibility']['indices']},
        'graph': graph, 'papers': {},
        'by_chunk': {(row['paper_id'], row['chunk_index']): row
                     for row in canonical['rows']},
    }


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def exchange_once(url, payload, headers, timeout):
    '''One HTTP attempt, with no redirect or network retry carrying credentials.'''
    request = urllib.request.Request(
        url, data=None if payload is None else json.dumps(payload).encode(),
        headers={'accept': 'application/json', 'content-type': 'application/json',
                 'user-agent': PROBE_USER_AGENT,
                 **headers},
    )
    try:
        response = urllib.request.build_opener(NoRedirect()).open(
            request, timeout=timeout)
    except urllib.error.HTTPError as error:
        response = error
    with response:
        return response.status, dict(response.headers), response.read().decode()


def persist(report, output):
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_suffix(output.suffix + '.tmp')
    temporary.write_text(json.dumps(report, indent=2) + '\n')
    temporary.replace(output)


class Smoke:
    def __init__(self, origin, token, fixture, report, output, exchange):
        self.origin, self.token, self.fixture = origin, token, fixture
        self.report, self.output, self.exchange = report, output, exchange
        self.deadline = time.monotonic() + MAX_LOAD_SECONDS

    def request(self, kind, path, payload=None):
        require(len(self.report['requests']) < MAX_HTTP_ATTEMPTS,
                'HTTP request budget exhausted')
        require(time.monotonic() < self.deadline, 'Smoke deadline exhausted')
        parsed = urllib.parse.urlsplit(path)
        require(path.startswith('/') and not path.startswith('//')
                and not parsed.scheme and not parsed.netloc and not parsed.fragment,
                'Only same-origin API paths are allowed')
        row = {'kind': kind, 'path': path, 'method': 'GET' if payload is None else 'POST',
               'marker': str(uuid.uuid4()), 'state': 'in_flight', 'success': False}
        self.report['requests'].append(row)
        persist(self.report, self.output)
        started = time.monotonic()
        try:
            status, headers, text = self.exchange(
                self.origin + path, payload,
                {'x-probe-token': self.token, 'x-probe-marker': row['marker'],
                 'x-probe-run-id': self.report['run_id']},
                min(60, max(.01, self.deadline - time.monotonic())),
            )
            headers = {key.lower(): value for key, value in headers.items()}
            row.update(status=status, response_text=text,
                       object_id=headers.get('x-probe-object-id'))
            require(status == 200, f'Unexpected HTTP status: {status}')
            require(headers.get('x-probe-runtime') == 'durable-object'
                    and headers.get('x-probe-kind') == 'real-full-corpus'
                    and headers.get('x-probe-synthetic') == 'false'
                    and headers.get('x-probe-manifest-sha256') == PACKED_SHA
                    and headers.get('x-probe-marker') == row['marker']
                    and row['object_id'] and headers.get('x-probe-boot-id'),
                    'Response probe identity mismatch')
            require(self.report.get('object_id', row['object_id']) == row['object_id'],
                    'Request routed to another Durable Object')
            self.report['object_id'] = row['object_id']
            body = json.loads(text)
            require(isinstance(body, dict), 'Expected a JSON object response')
            row.update(response=body, success=True)
            return body
        except Exception as error:
            row['error'] = f'{type(error).__name__}: {error}'
            raise
        finally:
            row.update(state='completed', elapsed_ms=(time.monotonic() - started) * 1000)
            persist(self.report, self.output)

    def ledger(self, label):
        info = self.request(label, '/probe/info')
        require(info.get('probe_type') == 'real-full-corpus'
                and info.get('scope') == 'full' and info.get('synthetic') is False
                and info.get('runtime') == 'durable-object'
                and info.get('manifest_sha256') == PACKED_SHA
                and info.get('source_manifest_sha256') == CANONICAL_SHA
                and info.get('passage_count') == 40575
                and info.get('release_id') == self.fixture['manifest']['release_id']
                and info.get('compatibility_indices')
                == self.fixture['manifest']['compatibility_indices'],
                'Remote full-corpus identity differs')
        validate_budget(info.get('budget'), self.report.get('budget'))
        self.report['budget'] = info['budget']
        self.report['ledgers'].append({'label': label, 'budget': info['budget'],
                                       'compatibility': info['compatibility']})
        persist(self.report, self.output)
        return info

    def run(self):
        initial = self.ledger('ledger_initial')
        require(all(initial['budget'][key] == 0 for key in (
            'compatibility_texts', 'query_texts', 'total_texts', 'input_tokens', 'ai_calls'))
            and initial['compatibility']['status'] == 'not_started',
            'Smoke requires a fresh zero-call ledger')
        checked = 0
        for batch in range(13):
            body = self.request('compatibility', '/probe/compatibility', {})
            status = validate_compatibility(body, self.fixture, checked)
            require(body.get('manifest_sha256') == PACKED_SHA
                    and body.get('release_id') == self.fixture['manifest']['release_id'],
                    'Compatibility identity differs')
            validate_budget(body.get('budget'), self.report['budget'])
            checked = min(200, checked + 16)
            budget = body['budget']
            require(body['checked'] == checked and budget['compatibility_texts'] == checked
                    and budget['query_texts'] == 0 and budget['total_texts'] == checked
                    and budget['ai_calls'] == batch + 1
                    and 0 < budget['input_tokens'] <= checked * 512
                    and status == ('passed' if checked == 200 else 'running'),
                    'Compatibility batch failed or consumed an unexpected budget')
            self.report.update(budget=budget, compatibility=body)
            persist(self.report, self.output)
        self.report['compatibility_gate'] = 'passed'
        health = self.request('health', '/health')
        require(health.get('search_enabled') is True and health.get('scope') == 'full'
                and health.get('compatibility_gate') == 'passed',
                'Search is unavailable after compatibility')
        for number, query in enumerate(QUERIES, start=1):
            before = self.ledger(f'ledger_before_query_{number}')['budget']
            require(before['query_texts'] == number - 1
                    and before['total_texts'] == 200 + number - 1
                    and before['ai_calls'] == 13 + number - 1,
                    'Unexpected provider activity before query')
            journey = {'query': query, 'ordinal': number, 'state': 'submitted'}
            self.report['journeys'].append(journey)
            persist(self.report, self.output)
            search = self.request('new_query', '/v1/search?' + urllib.parse.urlencode(
                {'q': query, 'k': 3}))
            for hit in search.get('hits', []):
                paper_id = hit['paper_id']
                name = hashlib.sha256(paper_id.encode()).hexdigest()
                release_id = self.fixture['manifest']['release_id']
                path = f'releases/{release_id}/papers/{name}.json'
                self.fixture['papers'][paper_id] = checked_json(
                    self.fixture['root'] / 'corpus' / path,
                    self.fixture['manifest']['files'][path])
            hits = validate_rest_search(search, self.fixture)
            top = hits[0]
            journey.update(hits=hits, selected_paper_id=top['paper_id'],
                           selection='first returned hit; no gold target')
            persist(self.report, self.output)
            content = self.request('read_returned_paper', top['content'])
            validate_content(content, self.fixture, top['paper_id'], top['start'], 6000)
            require(bool(content['text']), 'Returned paper read was empty')
            journey.update(read_body=content, state='read_completed')
            after = self.ledger(f'ledger_after_query_{number}')['budget']
            require(after['compatibility_texts'] == 200 and after['query_texts'] == number
                    and after['total_texts'] == 200 + number and after['ai_calls'] == 13 + number
                    and 0 < after['input_tokens'] - before['input_tokens'] <= 512,
                    'Expected exactly one live query embedding and no embedding for the read')
            journey['ledger_before'], journey['ledger_after'] = before, after
            persist(self.report, self.output)
        self.report.update(smoke_gate='passed', workload_complete=True)


def run(origin, token, fixture_root, output, authorized_queries, *, exchange=exchange_once):
    report = {
        'schema_version': 1, 'kind': 'retained-full-corpus-http-search-read-smoke',
        'purpose': 'two new English HTTP queries -> returned-paper reads',
        'autonomous_agent_evaluation': False, 'heldout_quality': 'unverified',
        'production_readiness': 'unverified', 'platform_cpu': 'unverified',
        'platform_memory': 'unverified', 'smoke_gate': 'failed',
        'compatibility_gate': 'unverified', 'workload_complete': False,
        'run_id': str(uuid.uuid4()), 'artifact_id': ARTIFACT_ID,
        'artifact_run_id': RUN_ID, 'artifact_sha256': ARTIFACT_SHA256,
        'packed_manifest_sha256': PACKED_SHA, 'query_manifest_sha256': FROZEN_SHA,
        'authorized_query_submissions': authorized_queries,
        'provider_retry_policy': 'never retry; read-only ledger recovery only',
        'max_http_attempts': MAX_HTTP_ATTEMPTS, 'max_load_seconds': MAX_LOAD_SECONDS,
        'requests': [], 'ledgers': [], 'journeys': [],
    }
    persist(report, output)
    smoke = None
    started = time.monotonic()
    try:
        require(authorized_queries == QUERY_SUBMISSIONS,
                'Explicit authorization for exactly two query submissions is required')
        parsed = urllib.parse.urlsplit(origin)
        require(parsed.scheme == 'https' and parsed.hostname
                and not parsed.username and not parsed.password
                and parsed.path in ('', '/') and not parsed.query and not parsed.fragment,
                'Expected an HTTPS probe origin')
        require(bool(token), 'The existing expiring probe token is required')
        fixture = load_fixture(fixture_root)
        smoke = Smoke(origin.rstrip('/'), token, fixture, report, output, exchange)
        smoke.run()
    except Exception as error:
        report['error'] = f'{type(error).__name__}: {error}'
        persist(report, output)
        if smoke is not None:
            try:
                smoke.ledger('ledger_after_failure_read_only')
            except Exception as ledger_error:
                report['ledger_recovery_error'] = f'{type(ledger_error).__name__}: {ledger_error}'
    finally:
        report['elapsed_seconds'] = time.monotonic() - started
        persist(report, output)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--origin', required=True)
    parser.add_argument('--restored', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--authorize-query-submissions', type=int, required=True, choices=[2])
    args = parser.parse_args()
    report = run(args.origin, os.environ.get('PROBE_TOKEN', ''), args.restored,
                 args.out, args.authorize_query_submissions)
    print(json.dumps({key: report.get(key) for key in (
        'smoke_gate', 'workload_complete', 'budget', 'error')}))
    raise SystemExit(0 if report['smoke_gate'] == 'passed' else 1)


if __name__ == '__main__':
    main()
