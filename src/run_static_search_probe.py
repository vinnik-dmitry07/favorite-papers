'''Measure the isolated synthetic probe; only Cloudflare logs measure CPU.

Exit 0: local functional success, or online CPU gate passed. Exit 1: failure.
Exit 2: online CPU gate is unverified. Runtime readiness is a separate gate.
'''

from __future__ import annotations

import argparse
import http.client
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


PROBE_USER_AGENT = (
    'favorite-papers-static-probe/1.0 '
    '(+https://github.com/vinnik-dmitry07/favorite-papers)'
)


EXPECTED_CASES = tuple(
    f'{kind}.{mode}' for mode in ('application_cold', 'warm')
    for kind in ('rest_search', 'mcp_search', 'mcp_fetch',
                 'content', 'contents', 'find')
)


def exchange(url, payload=None, headers=None, timeout=20):
    request_headers = {
        'accept': 'application/json, text/event-stream',
        'user-agent': PROBE_USER_AGENT,
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
    if kind.startswith('stage_'):
        if body.get('synthetic') is not True or body.get('stage') != kind[6:]:
            raise ValueError('Invalid diagnostic response')
        return
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


def persist(report):
    '''Atomic checkpoint, including run identity before the first request.'''
    output = report.get('output_path')
    if not output:
        return
    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)
    report['updated_ms'] = int(time.time() * 1000)
    report.setdefault(
        'finished_ms', report.get('started_ms', report['updated_ms']))
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    temporary.replace(path)


def all_requests(report):
    groups = ('requests', 'priming_requests', 'diagnostics',
              'preflight_requests')
    return [row for key in groups for row in report.get(key, [])]


def probe_info(report, wait_seconds):
    '''Check readiness without counting startup retries as measurements.'''
    deadline = time.monotonic() + wait_seconds
    attempts = report.setdefault('readiness_attempts', [])
    report['readiness_gate'] = 'unverified'
    persist(report)
    while True:
        row = {'started_ms': int(time.time() * 1000)}
        retryable = True
        try:
            status, headers, text = exchange(
                report['origin'] + '/probe/info',
                timeout=min(20, max(1, deadline - time.monotonic())))
            headers = {key.lower(): value for key, value in headers.items()}
            row.update(status=status, response_excerpt=text[:1000],
                       content_type=headers.get('content-type'),
                       cf_ray=headers.get('cf-ray'),
                       boot_id=headers.get('x-probe-boot-id'))
            retryable = status in {404, 408, 429} or status >= 500
            if status == 200:
                info = decode_body(text)
                if (info.get('synthetic') is not True
                        or headers.get('x-probe-synthetic') != 'true'):
                    raise ValueError('Target is not the isolated probe')
                if (not isinstance(info.get('variants'), list)
                        or not info['variants']
                        or not all(isinstance(v, str)
                                   for v in info['variants'])
                        or not isinstance(info.get('corpus_version'), str)
                        or not info['corpus_version']):
                    raise ValueError('Malformed probe discovery response')
                row.pop('response_excerpt')
                attempts.append(row)
                report['readiness_gate'] = 'passed'
                persist(report)
                return info
            row['error'] = f'Probe discovery HTTP {status}'
        except (http.client.HTTPException, OSError, ValueError) as exc:
            row['error'] = type(exc).__name__ + ': ' + str(exc)[:160]
        attempts.append(row)
        if not retryable:
            report['readiness_gate'] = 'failed'
        persist(report)
        print('Probe discovery: ' + json.dumps(row), flush=True)
        if not retryable or time.monotonic() >= deadline:
            return None
        time.sleep(min(2, max(0, deadline - time.monotonic())))


def sample(report, kind, mode, sequence, path, params=None, tool=None):
    variant = report.get('active_variant')
    case = f'{kind}.{mode}'
    if variant:
        case = variant + '.' + case
    query = {**(params or {}), 'probe_run': report['run_id'],
             'probe_case': case, 'probe_seq': sequence}
    if variant:
        query['variant'] = variant
    if mode == 'application_cold':
        query['cold'] = 1
    url = report['origin'] + path + '?' + urllib.parse.urlencode(query)
    marker = str(uuid.uuid4())
    record = {'case': case, 'variant': variant, 'url': url,
              'marker': marker, 'success': False, 'eligible': True,
              'cache_condition': mode, 'isolate_cold_verified': False,
              'state': 'in_flight'}
    target = ('preflight_requests' if report.get('preflight_running') else
              'diagnostics' if kind.startswith('stage_') else
              'priming_requests' if sequence < 0 else 'requests')
    report.setdefault(target, []).append(record)
    persist(report)
    if kind in {'rest_search', 'mcp_search'}:
        text_query = ((params or {}).get('q', '') if kind == 'rest_search'
                      else tool['params']['arguments']['query'])
        record['query_codepoints'] = len(text_query)
        record['max_query_used'] = sequence >= 0 and (sequence + 1) % 10 == 0
        record['adversarial_query_used'] = sequence >= 0 and sequence % 10 == 8
    started = time.perf_counter()
    body = None
    try:
        status, headers, text = exchange(url, tool, {'x-probe-marker': marker})
        headers = {key.lower(): value for key, value in headers.items()}
        record.update(status=status, boot_id=headers.get('x-probe-boot-id'),
                      observed_cache=headers.get('x-probe-cache'),
                      first_request=(
                          headers.get('x-probe-first-request') == 'true'))
        if status != 200:
            raise ValueError(f'HTTP {status}')
        if headers.get('x-probe-synthetic') != 'true' or not record['boot_id']:
            raise ValueError('Missing synthetic probe identity headers')
        if headers.get('x-probe-marker') != marker:
            raise ValueError('Request marker was not echoed')
        if variant and headers.get('x-probe-variant') != variant:
            raise ValueError('Unexpected probe variant')
        body = decode_body(text, tool is not None)
        validate(body, kind, report['info']['corpus_version'])
        if (kind == 'mcp_fetch'
                and body['id'] != tool['params']['arguments']['id']):
            raise ValueError('MCP fetch returned a different item')
        expected = 'cold' if mode == 'application_cold' else 'warm'
        if sequence >= 0 and record['observed_cache'] != expected:
            if mode == 'warm' and record['observed_cache'] == 'cold':
                record.update(eligible=False,
                              excluded_reason='cache_reset_or_isolate_change')
            else:
                raise ValueError('Application cache precondition not met')
        record['success'] = True
    except (http.client.HTTPException, OSError) as exc:
        record.update(eligible=False, excluded_reason='transport_error',
                      error=f'{type(exc).__name__}: {exc}'[:200])
    except (ValueError, KeyError, TypeError, IndexError) as exc:
        record['error'] = f'{type(exc).__name__}: {exc}'[:200]
    report['finished_ms'] = int(time.time() * 1000)
    record.update(client_wall_ms=(time.perf_counter() - started) * 1000,
                  state='complete')
    persist(report)
    return body if record['success'] else None


def run_samples(report, samples):
    info = report['info']
    base_query = info.get('sample_query', 'attention')
    for mode in ('application_cold', 'warm'):
        fetch_id = info.get('sample_fetch_id')
        find_query = info.get('sample_find_query', 'synthetic')
        for sequence in range(-1 if mode == 'warm' else 0, samples):
            query_base = base_query
            if sequence >= 0 and (sequence + 1) % 10 == 0:
                query_base = info.get('sample_query_max', base_query)
            elif sequence >= 0 and sequence % 10 == 8:
                query_base = info.get('sample_query_adversarial', base_query)
            query = f'{query_base} probe {sequence}'
            sample(report, 'rest_search', mode, sequence, '/v1/search',
                   {'q': query, 'k': 8})
            result = sample(
                report, 'mcp_search', mode, sequence, '/mcp', tool={
                'jsonrpc': '2.0', 'id': sequence, 'method': 'tools/call',
                'params': {'name': 'search',
                           'arguments': {'query': query + ' mcp'}},
            })
            if result and fetch_id is None:
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
        if report.get('diagnostic_stages'):
            for stage in ('noop', 'tokenize', 'scan'):
                for sequence in range(min(samples, 10)):
                    sample(report, 'stage_' + stage, mode, sequence,
                           '/probe/stage', {'stage': stage,
                                            'q': info.get(
                                                'sample_query_adversarial',
                                                base_query)})


def attach_telemetry(report, events):
    """Join a custom marker to its *platform* requestId, never to a URL.

    Pages can arrive in either order. Retain only matching invocation IDs and
    bounded invocation evidence; custom CPU fields are deliberately ignored.
    """
    records = {row.get('marker'): row for row in all_requests(report)
               if row.get('marker')}
    links = report.setdefault('telemetry_links', {})
    invocations = report.setdefault('telemetry_invocations', {})
    for event in events:
        if not isinstance(event, dict):
            continue
        workers, metadata = event.get(
            '$workers', {}), event.get(
            '$metadata', {})
        if not isinstance(workers, dict) or not isinstance(metadata, dict):
            continue
        request_id = workers.get('requestId')
        if not isinstance(request_id, str) or not request_id:
            continue
        source = event.get('source', {})
        if isinstance(source, str):
            try:
                source = json.loads(source)
            except ValueError:
                source = {}
        if isinstance(source, dict) and isinstance(source.get('message'), str):
            try:
                source = json.loads(source['message'])
            except ValueError:
                pass
        marker = source.get('probe_marker') if isinstance(
            source, dict) else None
        if marker in records and source.get('probe_run') == report['run_id']:
            previous = links.get(marker)
            if previous and previous != request_id:
                records[marker]['telemetry_conflict'] = True
                records[marker].pop('telemetry', None)
            else:
                links[marker] = request_id
        cpu = workers.get('cpuTimeMs')
        valid_cpu = (isinstance(cpu, (int, float))
                     and not isinstance(cpu, bool)
                     and math.isfinite(cpu) and cpu >= 0)
        outcome = workers.get('outcome')
        # Only platform invocation events can contribute CPU/outcome evidence.
        if metadata.get('type') != 'cf-worker-event':
            continue
        if valid_cpu or (isinstance(outcome, str)
                         and outcome not in {'ok', ''}):
            value = {'cpu_ms': cpu if valid_cpu else None,
                     'wall_ms': workers.get('wallTimeMs'), 'outcome': outcome,
                     'request_id': request_id, 'event_id': metadata.get('id')}
            prior = invocations.get(request_id)
            if prior and (prior['cpu_ms'] != value['cpu_ms']
                          or prior['outcome'] != value['outcome']):
                value['conflict'] = True
            invocations[request_id] = value
    by_request_id = {}
    for marker, request_id in links.items():
        by_request_id.setdefault(request_id, []).append(marker)
    for markers in by_request_id.values():
        if len(markers) > 1:
            for marker in markers:
                if marker in records:
                    records[marker]['telemetry_conflict'] = True
                    records[marker].pop('telemetry', None)
    for marker, row in records.items():
        invocation = invocations.get(links.get(marker))
        if invocation and not row.get('telemetry_conflict'):
            row['telemetry'] = invocation


def collect(report, wait_seconds):
    account = os.environ.get('CLOUDFLARE_ACCOUNT_ID')
    token = os.environ.get('CLOUDFLARE_API_TOKEN')
    if not account or not token:
        report['telemetry_error'] = 'Cloudflare credentials are missing'
        return
    account = urllib.parse.quote(account, safe='')
    endpoint = ('https://api.cloudflare.com/client/v4/accounts/'
                f'{account}/workers/observability/telemetry/query')
    deadline = time.monotonic() + wait_seconds
    while True:
        # Query the isolated script and time range, NOT a run-id needle: the
        # invocation event need not contain the custom marker or run id.
        payload = {
            'queryId': report['run_id'], 'view': 'events', 'dry': True,
            'timeframe': {'from': report['started_ms'] - 1000,
                          'to': report['finished_ms'] + 1000},
            'limit': 2000,
            'parameters': {'filters': [{
                'key': '$workers.scriptName', 'operation': 'eq',
                'type': 'string', 'value': report.get(
                    'script_name', 'key-papers-static-probe'),
            }]},
        }
        retryable = True
        try:
            for _ in range(50):
                status, _, text = exchange(
                    endpoint, payload, {'authorization': f'Bearer {token}'},
                    timeout=min(20, max(1, deadline - time.monotonic())))
                if status != 200:
                    retryable = status == 429 or status >= 500
                    raise ValueError(f'Telemetry API HTTP {status}')
                body = json.loads(text)
                if body.get('errors'):
                    retryable = False
                    raise ValueError('Telemetry API rejected the query')
                events = body['result'].get('events', {}).get('events', [])
                attach_telemetry(report, events)
                persist(report)
                if len(events) < 2000:
                    break
                cursor = events[-1]['$metadata']['id']
                if cursor == payload.get('offset'):
                    raise ValueError('Telemetry pagination did not advance')
                if time.monotonic() >= deadline:
                    raise ValueError('Pagination timeout; use --collect-only')
                payload.update(offset=cursor, offsetDirection='next')
            report.pop('telemetry_error', None)
        except (http.client.HTTPException, OSError, ValueError,
                KeyError, TypeError) as exc:
            report['telemetry_error'] = type(
                exc).__name__ + ': ' + str(exc)[:120]
            persist(report)
            if not retryable or time.monotonic() >= deadline:
                return
        if all('telemetry' in row for row in all_requests(report)):
            return
        if time.monotonic() >= deadline:
            report.setdefault(
                'telemetry_error',
                'Missing logs; retry --collect-only')
            return
        time.sleep(min(3, max(0, deadline - time.monotonic())))


def summarize(report):
    cases = {}
    for case in sorted({row['case'] for row in report['requests']}):
        attempted = [row for row in report['requests'] if row['case'] == case]
        rows = [row for row in attempted if row.get('eligible', True)
                and row.get('state') != 'in_flight']
        telemetry = [row['telemetry'] for row in rows if 'telemetry' in row]
        outcomes = Counter(item['outcome'] for item in telemetry)
        values = [item['cpu_ms']
                  for item in telemetry if item['cpu_ms'] is not None]
        valid = all(row['success'] for row in rows)
        complete = len(values) == len(rows) and len(rows) >= 50
        observed_failure = (any(value >= 8 for value in values)
                            or any(value not in {'ok', None, ''}
                                   for value in outcomes))
        conflicts = any(row.get('telemetry_conflict') for row in rows) or any(
            item.get('conflict') for item in telemetry)
        passed = (valid and complete and outcomes.get('ok') == len(rows)
                  and not observed_failure and not conflicts)
        gate = 'failed' if not valid or observed_failure else 'unverified'
        cases[case] = {
            'attempted': len(attempted), 'samples': len(rows),
            'excluded': len(attempted) - len(rows),
            'successful': sum(row['success'] for row in rows),
            'client_wall_ms': percentiles(
                [row['client_wall_ms'] for row in rows]),
            'cpu_ms': percentiles(values),
            'cpu_max_ms': max(values, default=None),
            'matched_telemetry': len(values),
            'missing_telemetry': len(rows) - len(values),
            'outcomes': outcomes, 'cpu_gate': 'passed' if passed else gate,
            'zero_exceedance_upper_95': 1 - 0.05 ** (1 / len(values))
            if values and not observed_failure else None,
            'max_query_samples': sum(
                row.get('max_query_used', False) for row in rows),
            'adversarial_query_samples': sum(
                row.get('adversarial_query_used', False) for row in rows),
        }
    expected = report.get('expected_cases', EXPECTED_CASES)
    report['cases'] = cases
    report['missing_cases'] = sorted(set(expected) - cases.keys())
    variants = report.get('variants') or ['legacy']
    report['variant_gates'] = {}
    for variant in variants:
        required = [case for case in expected if variant ==
                    'legacy' or case.startswith(variant + '.')]
        gates = [cases.get(case, {}).get('cpu_gate', 'unverified')
                 for case in required]
        report['variant_gates'][variant] = (
            'passed' if gates and all(gate == 'passed' for gate in gates)
            else 'failed' if 'failed' in gates else 'unverified')
    gates = list(report['variant_gates'].values())
    any_pass = 'passed' in gates and not report['missing_cases']
    all_fail = gates and all(gate == 'failed' for gate in gates)
    report['cpu_gate'] = ('passed' if any_pass else
                          'failed' if all_fail else 'unverified')
    failed = [row for row in all_requests(report) if not row['success']]
    report['functional_gate'] = (
        'failed' if any(row.get('eligible', True)
                        and row.get('state') != 'in_flight' for row in failed)
        else 'unverified' if failed else 'passed')
    if report.get('readiness_gate', 'passed') != 'passed':
        report['functional_gate'] = report['readiness_gate']
        report['cpu_gate'] = 'unverified'
    report.update(runtime_gate='unverified', memory_gate='unverified',
                  isolate_cold_gate='unverified',
                  retrieval_quality='not_tested')
    report['limitations'] = [
        'A failed variant does not reject static search or authorize Paid.',
        'Synthetic embeddings; Workers AI inference is not exercised.',
        'Observed-sample CPU gate is not a population p99 guarantee; '
        'bounds assume independent representative requests.',
        'cold=1 resets application cache, not the Cloudflare V8 isolate.',
        'Client wall time is not CPU time; absent telemetry never means zero.',
        'Excluded requests are retained; '
        'their CPU/outcomes still require review.',
        'Memory and isolate cold starts require separate measurement.',
    ]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('origin', nargs='?')
    parser.add_argument('--output', type=Path,
                        default=Path('probe-report.json'))
    parser.add_argument('--samples', type=int, default=50)
    parser.add_argument('--local', action='store_true')
    parser.add_argument('--variants', default='js4-json16',
                        help='Comma-separated variants, or all')
    parser.add_argument('--script-name', default='key-papers-static-probe')
    parser.add_argument('--collect-only', type=Path)
    parser.add_argument('--wait-seconds', type=int, default=30)
    parser.add_argument('--ready-wait-seconds', type=int, default=60)
    args = parser.parse_args(argv)
    if (not 1 <= args.samples <= 500
            or not 0 <= args.wait_seconds <= 60
            or not 0 <= args.ready_wait_seconds <= 60):
        parser.error('samples must be 1..500; wait values must be 0..60')
    if args.collect_only:
        report = json.loads(args.collect_only.read_text(encoding='utf-8'))
        report['output_path'] = str(args.output.resolve())
    else:
        parsed = urllib.parse.urlsplit(args.origin or '')
        local = args.local and parsed.hostname in {
            'localhost', '127.0.0.1', '::1'}
        if parsed.scheme != 'https' and not (
                local and parsed.scheme == 'http'):
            parser.error('Use HTTPS, or --local with an HTTP loopback origin')
        if any((parsed.username, parsed.password,
                parsed.query, parsed.fragment)):
            parser.error('Origin contains credentials, query or fragment')
        origin = args.origin.rstrip('/')
        report = {'origin': origin, 'run_id': str(uuid.uuid4()),
                  'started_ms': int(time.time() * 1000), 'requests': [],
                  'output_path': str(args.output.resolve()),
                  'script_name': args.script_name}
        info = probe_info(report, args.ready_wait_seconds)
        if info is None:
            summarize(report)
            persist(report)
            print('Probe discovery did not pass; no matrix was sent. '
                  'See readiness_attempts in ' + str(args.output))
            return 1 if report['readiness_gate'] == 'failed' else 2
        variants = (info['variants'] if args.variants == 'all'
                    else args.variants.split(','))
        if not variants or len(set(variants)) != len(variants) or any(
                variant not in info['variants'] for variant in variants):
            parser.error('Unknown or duplicate variant')
        report.update(info=info, variants=variants,
                      expected_cases=[v + '.' + c for v in variants
                                      for c in EXPECTED_CASES],
                      diagnostic_stages=True)
        persist(report)
        if not args.local:
            report['preflight_running'] = True
            sample(report, 'stage_noop', 'application_cold',
                   0, '/probe/stage', {'stage': 'noop'})
            report.pop('preflight_running')
            collect(report, args.wait_seconds)
            pilot = report['preflight_requests'][0]
            evidence = pilot.get('telemetry', {})
            if not pilot['success'] or evidence.get(
                    'cpu_ms') is None or evidence.get('outcome') != 'ok':
                report['preflight_gate'] = 'unverified'
                summarize(report)
                persist(report)
                print('Telemetry pilot unverified; '
                      'no measurement matrix was sent.')
                return 2
            report['preflight_gate'] = 'passed'
        try:
            for variant in variants:
                print(
                    f'Measuring {variant}: {
                        args.samples} samples per case',
                    flush=True)
                report['active_variant'] = variant
                run_samples(report, args.samples)
        finally:
            summarize(report)
            persist(report)
    if not args.local:
        collect(report, args.wait_seconds)
    summarize(report)
    persist(report)
    print(json.dumps({key: report[key] for key in (
        'cpu_gate', 'runtime_gate', 'variant_gates')}))
    if report['cpu_gate'] == 'failed' or report['functional_gate'] == 'failed':
        return 1
    if report['functional_gate'] != 'passed':
        return 2
    return 0 if args.local or report['cpu_gate'] == 'passed' else 2


if __name__ == '__main__':
    raise SystemExit(main())
