'''Measure the isolated synthetic probe; only Cloudflare logs measure CPU.

Exit 0: local functional success, or online CPU gate passed. Exit 1: failure.
Exit 2: online CPU gate is unverified. Runtime readiness is a separate gate.
'''

from __future__ import annotations

import argparse
import json
import math
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from collections import Counter
from pathlib import Path


EXPECTED_CASES = tuple(
    f'{kind}.{mode}' for mode in ('application_cold', 'warm')
    for kind in ('rest_search', 'mcp_search', 'mcp_fetch',
                 'content', 'contents', 'find')
)


def exchange(url, payload=None, headers=None, timeout=20):
    request_headers = {
        'accept': 'application/json, text/event-stream',
        'content-type': 'application/json',
        'mcp-protocol-version': '2025-06-18',
        **(headers or {}),
    }
    request = urllib.request.Request(
        url, data=None if payload is None else json.dumps(payload).encode(),
        headers=request_headers,
    )
    try:
        response = urllib.request.urlopen(request, timeout=timeout)
    except urllib.error.HTTPError as exc:
        response = exc
    with response:
        body = response.read().decode()
        return response.status, dict(response.headers), body


def decode_body(text, mcp=False):
    lines = [line[5:].strip() for line in text.splitlines()
             if line.startswith('data:')]
    body = json.loads(lines[-1] if lines else text)
    if not isinstance(body, dict):
        raise ValueError('Expected an object response')
    if mcp:
        if body.get('error') or not isinstance(body.get('result'), dict):
            raise ValueError('MCP protocol error or missing result')
        body = body['result']
        if body.get('isError'):
            raise ValueError('MCP tool error')
        structured = body.get('structuredContent')
        content = body.get('content')
        if (not isinstance(content, list) or not content
                or not isinstance(content[0], dict)):
            raise ValueError('Malformed MCP text content')
        if structured != json.loads(content[0]['text']):
            raise ValueError('MCP structured content mismatch')
        body = structured
    if not isinstance(body, dict):
        raise ValueError('Expected an object response')
    return body


def validate(body, kind, version):
    metadata = body.get('metadata')
    if kind == 'mcp_fetch' and not isinstance(metadata, dict):
        raise ValueError('Missing MCP document version metadata')
    actual_version = (metadata.get('corpus_version')
                      if kind == 'mcp_fetch' else body.get('corpus_version'))
    if kind != 'mcp_search' and actual_version != version:
        raise ValueError('Unexpected corpus version')
    if kind == 'rest_search':
        hits = body.get('hits')
        valid = isinstance(hits, list) and bool(hits) and all(
            isinstance(hit, dict) and hit.get('paper_id')
            and isinstance(hit.get('snippet'), str) and hit['snippet']
            for hit in hits)
    elif kind == 'mcp_search':
        results = body.get('results')
        valid = isinstance(results, list) and bool(results) and all(
            isinstance(item, dict) and isinstance(item.get('id'), str)
            and item['id'] and item.get('url') for item in results)
    elif kind == 'mcp_fetch':
        valid = bool(body.get('id') and body.get('text'))
    elif kind == 'content':
        valid = (body.get('available') is True and bool(body.get('text'))
                 and len(body['text']) == min(32000, body['total_length']))
    else:
        valid = body.get('available') is True and bool(
            body.get('sections' if kind == 'contents' else 'matches'))
    if not valid:
        raise ValueError(f'Invalid or empty {kind} response')


def percentiles(values):
    ordered = sorted(values)
    return {
        f'p{q}': ordered[math.ceil(len(ordered) * q / 100) - 1]
        if ordered else None for q in (50, 95, 99)
    }


def sample(report, kind, mode, sequence, path, params=None, tool=None):
    query = {**(params or {}), 'probe_run': report['run_id'],
             'probe_case': f'{kind}.{mode}', 'probe_seq': sequence}
    if mode == 'application_cold':
        query['cold'] = 1
    url = report['origin'] + path + '?' + urllib.parse.urlencode(query)
    record = {'case': query['probe_case'], 'url': url, 'success': False,
              'cache_condition': mode, 'isolate_cold_verified': False}
    if kind in {'rest_search', 'mcp_search'}:
        text_query = ((params or {}).get('q', '') if kind == 'rest_search'
                      else tool['params']['arguments']['query'])
        record['query_codepoints'] = len(text_query)
        record['max_query_used'] = bool(
            report['info'].get('sample_query_max')
            and sequence >= 0 and (sequence + 1) % 10 == 0)
    started = time.perf_counter()
    body = None
    try:
        status, headers, text = exchange(url, tool)
        headers = {key.lower(): value for key, value in headers.items()}
        record.update(status=status, boot_id=headers.get('x-probe-boot-id'),
                      observed_cache=headers.get('x-probe-cache'))
        if status != 200:
            raise ValueError(f'HTTP {status}')
        if headers.get('x-probe-synthetic') != 'true' or not record['boot_id']:
            raise ValueError('Missing synthetic probe identity headers')
        expected = 'cold' if mode == 'application_cold' else 'warm'
        if sequence >= 0 and record['observed_cache'] != expected:
            raise ValueError('Application cache precondition not met')
        body = decode_body(text, tool is not None)
        validate(body, kind, report['info']['corpus_version'])
        if (kind == 'mcp_fetch'
                and body['id'] != tool['params']['arguments']['id']):
            raise ValueError('MCP fetch returned a different item')
        record['success'] = True
    except (OSError, ValueError, KeyError, TypeError, IndexError) as exc:
        record['error'] = f'{type(exc).__name__}: {exc}'[:200]
    record['client_wall_ms'] = (time.perf_counter() - started) * 1000
    target = 'priming_requests' if sequence < 0 else 'requests'
    report.setdefault(target, []).append(record)
    return body if record['success'] else None


def run_samples(report, samples):
    info = report['info']
    base_query = info.get('sample_query', 'attention')
    for mode in ('application_cold', 'warm'):
        fetch_id = None
        find_query = info.get('sample_find_query', 'synthetic')
        for sequence in range(-1 if mode == 'warm' else 0, samples):
            query_base = (info.get('sample_query_max', base_query)
                          if sequence >= 0 and (sequence + 1) % 10 == 0
                          else base_query)
            query = f'{query_base} probe {sequence}'
            sample(report, 'rest_search', mode, sequence, '/v1/search',
                   {'q': query, 'k': 8})
            search_call = {
                'jsonrpc': '2.0', 'id': sequence, 'method': 'tools/call',
                'params': {'name': 'search',
                           'arguments': {'query': query + ' mcp'}},
            }
            result = sample(report, 'mcp_search', mode, sequence, '/mcp',
                            tool=search_call)
            if result and (mode == 'application_cold' or fetch_id is None):
                fetch_id = result['results'][0]['id']
            sample(report, 'mcp_fetch', mode, sequence, '/mcp', tool={
                'jsonrpc': '2.0', 'id': sequence, 'method': 'tools/call',
                'params': {'name': 'fetch',
                           'arguments': {'id': fetch_id or ''}},
            })
            params = {'id': info['longest_paper_id'],
                      'version': info['corpus_version']}
            content = sample(report, 'content', mode, sequence, '/v1/content',
                             {**params, 'length': 32000})
            if content:
                words = re.findall(r'[A-Za-z]{4,}', content['text'])
                find_query = words[0] if words else find_query
            sample(report, 'contents', mode, sequence, '/v1/contents', params)
            sample(report, 'find', mode, sequence, '/v1/find',
                   {**params, 'q': find_query})


def attach_telemetry(report, events):
    by_url = {record['url']: record for record in report['requests']}
    for event in events:
        if not isinstance(event, dict):
            continue
        workers = event.get('$workers', {})
        metadata = event.get('$metadata', {})
        if not isinstance(workers, dict) or not isinstance(metadata, dict):
            continue
        invocation = workers.get('event')
        request = (invocation.get('request')
                   if isinstance(invocation, dict) else {})
        url = request.get('url') if isinstance(request, dict) else None
        record = (by_url.get(url)
                  or by_url.get(metadata.get('url')))
        cpu = workers.get('cpuTimeMs')
        valid_cpu = (isinstance(cpu, (int, float))
                     and not isinstance(cpu, bool)
                     and math.isfinite(cpu) and cpu >= 0)
        outcome = workers.get('outcome')
        failed = isinstance(outcome, str) and outcome not in {'ok', ''}
        if record is not None and (valid_cpu or failed):
            record['telemetry'] = {
                'cpu_ms': cpu if valid_cpu else None,
                'wall_ms': workers.get('wallTimeMs'), 'outcome': outcome,
                'request_id': workers.get('requestId'),
                'event_id': metadata.get('id'),
            }


def collect(report, wait_seconds):
    account = os.environ.get('CLOUDFLARE_ACCOUNT_ID')
    token = os.environ.get('CLOUDFLARE_API_TOKEN')
    if not account or not token:
        report['telemetry_error'] = 'Cloudflare credentials are missing'
        return
    account = urllib.parse.quote(account, safe='')
    endpoint = ('https://api.cloudflare.com/client/v4/accounts/'
                f'{account}/workers/'
                'observability/telemetry/query')
    deadline = time.monotonic() + wait_seconds
    while True:
        payload = {
            'queryId': report['run_id'], 'view': 'events', 'dry': True,
            'timeframe': {'from': report['started_ms'] - 1000,
                          'to': report['finished_ms'] + 1000},
            'limit': 2000,
            'parameters': {'needle': {'value': report['run_id']}},
        }
        try:
            for _ in range(20):
                status, _, text = exchange(
                    endpoint, payload, {'authorization': f'Bearer {token}'},
                    timeout=min(20, max(1, deadline - time.monotonic())))
                if status != 200:
                    raise ValueError(f'Telemetry API HTTP {status}')
                body = json.loads(text)
                if body.get('errors'):
                    raise ValueError('Telemetry API rejected the query')
                events = body['result'].get('events', {}).get('events', [])
                attach_telemetry(report, events)
                if len(events) < 2000:
                    break
                cursor = events[-1]['$metadata']['id']
                if cursor == payload.get('offset'):
                    raise ValueError('Telemetry pagination did not advance')
                if time.monotonic() >= deadline:
                    raise ValueError('Pagination timeout; use --collect-only')
                payload.update(offset=cursor, offsetDirection='next')
            report.pop('telemetry_error', None)
        except (OSError, ValueError, KeyError, TypeError) as exc:
            report['telemetry_error'] = (
                type(exc).__name__ + ': ' + str(exc)[:120])
            return
        if all('telemetry' in row for row in report['requests']):
            return
        if time.monotonic() >= deadline:
            report['telemetry_error'] = 'Missing logs; retry --collect-only'
            return
        time.sleep(min(3, max(0, deadline - time.monotonic())))


def summarize(report):
    cases = {}
    for case in sorted({row['case'] for row in report['requests']}):
        rows = [row for row in report['requests'] if row['case'] == case]
        telemetry = [row['telemetry'] for row in rows if 'telemetry' in row]
        outcomes = Counter(item['outcome'] for item in telemetry)
        values = [item['cpu_ms'] for item in telemetry
                  if item['cpu_ms'] is not None]
        cpu = percentiles(values)
        valid = all(row['success'] for row in rows)
        complete = len(values) == len(rows) and len(rows) >= 50
        observed_failure = (any(value >= 8 for value in values)
                            or any(value not in {'ok', None, ''}
                                   for value in outcomes))
        passed = (valid and complete and outcomes.get('ok') == len(rows)
                  and not observed_failure)
        gate = ('failed' if not valid or observed_failure else 'unverified')
        cases[case] = {
            'samples': len(rows),
            'successful': sum(row['success'] for row in rows),
            'client_wall_ms': percentiles(
                [row['client_wall_ms'] for row in rows]),
            'cpu_ms': cpu, 'matched_telemetry': len(values),
            'missing_telemetry': len(rows) - len(values),
            'outcomes': outcomes, 'cpu_gate': 'passed' if passed else gate,
            'max_query_samples': sum(row.get('max_query_used', False)
                                     for row in rows),
        }
    report['cases'] = cases
    report['missing_cases'] = sorted(set(EXPECTED_CASES) - cases.keys())
    gates = [case['cpu_gate'] for case in cases.values()]
    if any(not row['success'] for row in report.get('priming_requests', [])):
        gates.append('failed')
    report['cpu_gate'] = (
        'passed' if set(cases) == set(EXPECTED_CASES)
        and all(gate == 'passed' for gate in gates)
        else 'failed' if 'failed' in gates else 'unverified')
    report.update(runtime_gate='unverified', memory_gate='unverified',
                  isolate_cold_gate='unverified',
                  retrieval_quality='not_tested')
    report['limitations'] = [
        'Synthetic embeddings; Workers AI inference is not exercised.',
        'cold=1 resets application cache, not the Cloudflare V8 isolate.',
        'Client wall time is not CPU time; absent telemetry never means zero.',
        'Memory and isolate cold starts require separate measurement.',
    ]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('origin', nargs='?')
    parser.add_argument('--output', type=Path,
                        default=Path('probe-report.json'))
    parser.add_argument('--samples', type=int, default=50)
    parser.add_argument('--local', action='store_true')
    parser.add_argument('--collect-only', type=Path)
    parser.add_argument('--wait-seconds', type=int, default=30)
    args = parser.parse_args(argv)
    if not 1 <= args.samples <= 200 or not 0 <= args.wait_seconds <= 60:
        parser.error('samples must be 1..200; wait-seconds must be 0..60')
    if args.collect_only:
        report = json.loads(args.collect_only.read_text(encoding='utf-8'))
    else:
        parsed = urllib.parse.urlsplit(args.origin or '')
        local = args.local and parsed.hostname in {
            'localhost', '127.0.0.1', '::1'}
        if (parsed.scheme != 'https'
                and not (local and parsed.scheme == 'http')):
            parser.error('Use HTTPS, or --local with an HTTP loopback origin')
        if any((parsed.username, parsed.password,
                parsed.query, parsed.fragment)):
            parser.error('Origin contains credentials, query or fragment')
        origin = args.origin.rstrip('/')
        status, _, text = exchange(origin + '/probe/info')
        info = decode_body(text)
        if status != 200 or info.get('synthetic') is not True:
            raise SystemExit('Target is not the isolated synthetic probe')
        report = {'origin': origin, 'run_id': uuid.uuid4().hex, 'info': info,
                  'started_ms': int(time.time() * 1000), 'requests': []}
        run_samples(report, args.samples)
        report['finished_ms'] = int(time.time() * 1000)
    if not args.local:
        collect(report, args.wait_seconds)
    summarize(report)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + '\n',
                           encoding='utf-8')
    print(json.dumps({key: report[key]
                      for key in ('cpu_gate', 'runtime_gate')}))
    if report['cpu_gate'] == 'failed':
        return 1
    return 0 if args.local or report['cpu_gate'] == 'passed' else 2


if __name__ == '__main__':
    raise SystemExit(main())
