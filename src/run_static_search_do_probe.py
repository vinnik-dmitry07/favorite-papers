'''Bounded, authenticated Durable Object probe with platform-only CPU evidence.

The pilot must establish separate gateway and object invocations before a
matrix is sent. Exit 0 means the requested observed-sample phase passed,
not production readiness; 1 means observed failure, 2 means unverified.
'''

from __future__ import annotations

import argparse
import concurrent.futures
import http.client
import json
import math
import os
import time
import urllib.parse
import uuid
from pathlib import Path

from run_static_search_probe import (
    EXPECTED_CASES, decode_body, exchange, percentiles, persist, validate,
)

MAX_REQUESTS = 1500
ROLES = ('gateway', 'durable_object')
KINDS = ('rest_search', 'mcp_search', 'mcp_fetch',
         'content', 'contents', 'find')


def finite_number(value):
    return (isinstance(value, (int, float)) and not isinstance(value, bool)
            and math.isfinite(value) and value >= 0)


def prepare(report, kind, mode, sequence, group='requests'):
    if time.time() * 1000 > report.get('load_deadline_ms', float('inf')):
        raise ValueError('Load time budget exhausted')
    if report.get('http_attempts', 0) >= MAX_REQUESTS:
        raise ValueError('External request budget exhausted')
    report['http_attempts'] = report.get('http_attempts', 0) + 1
    record = {
        'marker': str(uuid.uuid4()), 'case': f'{kind}.{mode}',
        'kind': kind, 'mode': mode, 'sequence': sequence,
        'state': 'in_flight', 'success': False, 'eligible': True,
        'isolate_cold_verified': False,
    }
    report.setdefault(group, []).append(record)
    persist(report)
    return record


def request_spec(report, record):
    info = report.get('info', {})
    kind, sequence = record['kind'], record['sequence']
    params = {'variant': 'wasm-json16'}
    if record['mode'] == 'application_cold':
        params['cold'] = 1
    query = info.get('sample_query', 'attention')
    if sequence >= 0 and sequence % 10 == 9:
        query = info.get('sample_query_max', query)
        record['max_query_used'] = True
    elif sequence >= 0 and sequence % 10 == 8:
        query = info.get('sample_query_adversarial', query)
        record['adversarial_query_used'] = True
    query += f' probe {sequence}'
    payload = None
    if kind == 'info':
        path = '/probe/info'
    elif kind in {'mcp_search', 'mcp_fetch'}:
        path = '/mcp'
        arguments = ({'query': query + ' mcp'} if kind == 'mcp_search'
                     else {'id': info['sample_fetch_id']})
        payload = {'jsonrpc': '2.0', 'id': sequence, 'method': 'tools/call',
                   'params': {'name': kind[4:], 'arguments': arguments}}
    elif kind == 'rest_search':
        path = '/v1/search'
        params.update(q=query, k=8)
    else:
        path = '/v1/' + kind
        params.update(id=info['longest_paper_id'],
                      version=info['corpus_version'])
        if kind == 'content':
            params['length'] = 32000
        elif kind == 'find':
            params['q'] = info.get('sample_find_query', 'the')
    return (report['origin'] + path + '?' + urllib.parse.urlencode(params),
            payload)


def send(report, record):
    '''Return data; the main thread owns checkpoints and report writes.'''
    result = dict(record)
    started = time.perf_counter()
    try:
        url, payload = request_spec(report, result)
        status, headers, text = exchange(url, payload, {
            'x-probe-token': os.environ.get('PROBE_TOKEN', ''),
            'x-probe-marker': record['marker'],
            'x-probe-run-id': report['run_id'],
        }, timeout=20)
        headers = {key.lower(): value for key, value in headers.items()}
        result.update(status=status, boot_id=headers.get('x-probe-boot-id'),
                      cache_id=headers.get('x-probe-cache-id'),
                      object_id=headers.get('x-probe-object-id'),
                      cold_kind=headers.get('x-probe-cold-kind'),
                      observed_cache=headers.get('x-probe-cache'))
        if status != 200:
            result['response_excerpt'] = text[:300]
            raise ValueError(f'HTTP {status}')
        if (headers.get('x-probe-runtime') != 'durable-object'
                or headers.get('x-probe-synthetic') != 'true'
                or headers.get('x-probe-marker') != record['marker']
                or not result['object_id'] or not result['boot_id']
                or not result['cache_id']):
            raise ValueError('Missing or incorrect DO probe identity')
        expected_object = report.get('object_id')
        if expected_object and result['object_id'] != expected_object:
            raise ValueError('Probe unexpectedly routed to another object')
        if headers.get('x-probe-variant') != 'wasm-json16':
            raise ValueError('Unexpected variant')
        body = decode_body(text, record['kind'].startswith('mcp_'))
        if record['kind'] == 'info':
            if (body.get('synthetic') is not True
                    or body.get('count') != 40575
                    or body.get('variants') != ['wasm-json16']
                    or not body.get('corpus_version')
                    or not body.get('sample_fetch_id')):
                raise ValueError('Expected full 40,575-row synthetic fixture')
            result['info'] = body
        else:
            validate(body, record['kind'], report['info']['corpus_version'])
            if (record['kind'] == 'mcp_fetch'
                    and body['id'] != report['info']['sample_fetch_id']):
                raise ValueError('MCP fetch returned a different item')
        allowed = {'object-constructor', 'application-cache-reset', 'warm'}
        if result['cold_kind'] not in allowed:
            raise ValueError('Unknown cache/cold condition')
        if record['mode'] == 'warm' and result['cold_kind'] != 'warm':
            result.update(eligible=False,
                          excluded_reason='object_or_cache_reinitialized')
        if (record['mode'] == 'application_cold'
                and result['cold_kind'] not in {
                    'object-constructor', 'application-cache-reset'}):
            raise ValueError('Application cache was not reset')
        result['success'] = True
    except (http.client.HTTPException, OSError, ValueError,
            KeyError, TypeError, IndexError) as exc:
        result['error'] = f'{type(exc).__name__}: {exc}'[:200]
    result.update(state='complete',
                  client_wall_ms=(time.perf_counter() - started) * 1000)
    return result


def perform(report, kind, mode, sequence, group='requests'):
    record = prepare(report, kind, mode, sequence, group)
    record.update(send(report, record))
    report['finished_ms'] = int(time.time() * 1000)
    persist(report)
    return record


def records(report):
    return [row for name in ('requests', 'discovery', 'pilot', 'priming',
                             'concurrency') for row in report.get(name, [])
            if not row.get('startup_retry')]


def attach_telemetry(report, events):
    '''Require a platform object ID to distinguish object CPU from gateway CPU.

    A custom role/CPU field alone cannot establish platform invocation scope.
    Missing or unfamiliar DO event layouts stay unverified. Events may arrive
    out of order or on different pages; conflicting identities are permanent.
    '''
    rows = {row['marker']: row for row in records(report)}
    links = report.setdefault('telemetry_links', {})
    invocations = report.setdefault('telemetry_invocations', {})
    conflicts = set(report.setdefault('telemetry_conflicts', []))
    for event in events:
        if not isinstance(event, dict):
            continue
        workers = event.get('$workers', {})
        metadata = event.get('$metadata', {})
        if not isinstance(workers, dict) or not isinstance(metadata, dict):
            continue
        left, right = metadata.get('requestId'), workers.get('requestId')
        if left and right and left != right:
            conflicts.update(str(item) for item in (left, right))
            continue
        request_id = left or right
        if not isinstance(request_id, str) or not request_id:
            continue
        diagnostic = {
            'type': metadata.get('type'), 'request_id': request_id,
            'object_id': workers.get('durableObjectId'),
            'cpu_ms': workers.get('cpuTimeMs'),
            'outcome': workers.get('outcome'),
            'worker_fields': sorted(workers),
        }
        examples = report.setdefault('telemetry_shape_examples', [])
        if len(examples) < 20 and diagnostic not in examples:
            examples.append(diagnostic)
        object_id = workers.get('durableObjectId')
        if object_id is not None and not isinstance(object_id, str):
            continue
        role = 'durable_object' if object_id else 'gateway'
        key = json.dumps([request_id, object_id or ''])
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
        if isinstance(source, dict):
            marker = source.get('probe_marker')
            if (marker in rows and source.get('run_id') == report['run_id']
                    and source.get('runtime_role') == role
                    and (role == 'gateway'
                         or source.get('object_id') == object_id)):
                link_key = marker + ':' + role
                previous = links.get(link_key)
                if previous and previous != key:
                    conflicts.add(link_key)
                links[link_key] = key
        if metadata.get('type') != 'cf-worker-event':
            continue
        cpu = workers.get('cpuTimeMs')
        value = {'request_id': request_id, 'object_id': object_id,
                 'runtime_role': role, 'event_id': metadata.get('id'),
                 'cpu_ms': cpu if finite_number(cpu) else None,
                 'wall_ms': workers.get('wallTimeMs'),
                 'outcome': workers.get('outcome')}
        prior = invocations.get(key)
        if prior and any(prior[field] != value[field]
                         for field in ('cpu_ms', 'outcome')):
            conflicts.add(key)
        invocations[key] = value
    reverse = {}
    for link_key, key in links.items():
        reverse.setdefault(key, []).append(link_key)
    for keys in reverse.values():
        if len(keys) > 1:
            conflicts.update(keys)
    for marker, row in rows.items():
        row['telemetry'] = {}
        for role in ROLES:
            link_key = marker + ':' + role
            key = links.get(link_key)
            invocation = invocations.get(key)
            if not invocation:
                continue
            if ({link_key, key, invocation['request_id']} & conflicts):
                row['telemetry_conflict'] = True
                continue
            if (role == 'durable_object'
                    and invocation['object_id'] != row.get('object_id')):
                row['telemetry_conflict'] = True
                continue
            row['telemetry'][role] = invocation
    report['telemetry_conflicts'] = sorted(conflicts)


def evidence_complete(row):
    return not row.get('telemetry_conflict') and all(
        finite_number(row.get('telemetry', {}).get(role, {}).get('cpu_ms'))
        and row['telemetry'][role].get('outcome') == 'ok' for role in ROLES)


def collect(report, wait_seconds):
    account = os.environ.get('CLOUDFLARE_ACCOUNT_ID')
    token = os.environ.get('CLOUDFLARE_API_TOKEN')
    if not account or not token:
        report['telemetry_error'] = 'Cloudflare credentials are missing'
        persist(report)
        return
    endpoint = ('https://api.cloudflare.com/client/v4/accounts/'
                + urllib.parse.quote(account, safe='')
                + '/workers/observability/telemetry/query')
    deadline = time.monotonic() + wait_seconds
    while True:
        payload = {
            'queryId': report['run_id'], 'view': 'events', 'dry': True,
            'timeframe': {'from': report['started_ms'] - 1000,
                          'to': report['finished_ms'] + 1000}, 'limit': 2000,
            'parameters': {'filters': [{
                'key': '$workers.scriptName', 'operation': 'eq',
                'type': 'string', 'value': report['script_name'],
            }]},
        }
        retryable = True
        try:
            for page in range(20):
                status, _, text = exchange(
                    endpoint, payload, {'authorization': f'Bearer {token}'},
                    timeout=min(20, max(1, deadline - time.monotonic())))
                if status != 200:
                    retryable = status == 429 or status >= 500
                    raise ValueError(f'Telemetry API HTTP {status}')
                body = json.loads(text)
                if body.get('errors'):
                    retryable = False
                    raise ValueError('Telemetry query rejected')
                bucket = body['result']['events']
                events = bucket['events']
                if not isinstance(events, list):
                    retryable = False
                    raise ValueError('Invalid events array')
                counts = report.setdefault('telemetry_diagnostics', {})
                counts['queries'] = counts.get('queries', 0) + 1
                counts['events_across_queries'] = counts.get(
                    'events_across_queries', 0) + len(events)
                counts['object_events_across_queries'] = counts.get(
                    'object_events_across_queries', 0) + sum(
                        isinstance(event, dict)
                        and isinstance(event.get('$workers'), dict)
                        and bool(event['$workers'].get('durableObjectId'))
                        for event in events)
                attach_telemetry(report, events)
                persist(report)
                if len(events) < 2000:
                    break
                cursor = events[-1]['$metadata']['id']
                if cursor == payload.get('offset') or page == 19:
                    raise ValueError('Telemetry pagination bound reached')
                if time.monotonic() >= deadline:
                    raise ValueError('Telemetry pagination timed out')
                payload.update(offset=cursor, offsetDirection='next')
            report.pop('telemetry_error', None)
        except (http.client.HTTPException, OSError, ValueError,
                KeyError, TypeError, IndexError) as exc:
            report['telemetry_error'] = f'{type(exc).__name__}: {exc}'[:200]
            persist(report)
            if not retryable or time.monotonic() >= deadline:
                return
        if all(evidence_complete(row) for row in records(report)):
            return
        if time.monotonic() >= deadline:
            report.setdefault('telemetry_error',
                              'Separate gateway/object evidence missing')
            persist(report)
            return
        time.sleep(min(3, max(0, deadline - time.monotonic())))


def summarize(report):
    all_rows = records(report)
    failures = [row for row in all_rows
                if row.get('state') == 'complete' and not row.get('success')]
    report['functional_gate'] = (
        'failed' if failures else 'passed' if all_rows and all(
            row.get('success') for row in all_rows) else 'unverified')
    role_gates = {}
    for role, limit in (('gateway', 8), ('durable_object', 30000)):
        evidence = [row.get('telemetry', {}).get(role, {}) for row in all_rows]
        observed_failure = any(
            finite_number(item.get('cpu_ms')) and item['cpu_ms'] >= limit
            or item.get('outcome') not in (None, '', 'ok')
            for item in evidence)
        complete = bool(all_rows) and all(
            not row.get('telemetry_conflict')
            and finite_number(item.get('cpu_ms'))
            and item.get('outcome') == 'ok'
            for row, item in zip(all_rows, evidence))
        role_gates[role] = ('failed' if observed_failure else
                            'passed' if complete else 'unverified')
    report['gateway_cpu_gate'] = role_gates['gateway']
    report['do_cpu_gate'] = role_gates['durable_object']
    cases = {}
    for case in sorted({row['case'] for row in report.get('requests', [])}):
        attempted = [row for row in report['requests'] if row['case'] == case]
        rows = [row for row in attempted if row.get('eligible')]
        summary = {'attempted': len(attempted), 'samples': len(rows),
                   'excluded': len(attempted) - len(rows),
                   'client_wall_ms': percentiles([
                       row['client_wall_ms'] for row in rows
                       if 'client_wall_ms' in row])}
        for role in ROLES:
            values = [row.get('telemetry', {}).get(role, {}).get('cpu_ms')
                      for row in rows]
            values = [value for value in values if finite_number(value)]
            summary[role] = {'cpu_ms': percentiles(values),
                             'cpu_max_ms': max(values, default=None),
                             'matched': len(values)}
        cases[case] = summary
    report['cases'] = cases
    # Gate each operation separately; fast content/find must not dilute search.
    warm_cases = {}
    concurrency_markers = {row['marker']
                           for row in report.get('concurrency', [])}
    for row in all_rows:
        if (row.get('eligible') and row['mode'] == 'warm'
                and 'client_wall_ms' in row):
            prefix = ('concurrency4.'
                      if row['marker'] in concurrency_markers else '')
            warm_cases.setdefault(prefix + row['case'], []).append(
                row['client_wall_ms'])
    report['warm_latency_cases'] = {case: percentiles(values)
                                    for case, values in warm_cases.items()}
    cold = [row['client_wall_ms'] for row in all_rows
            if row.get('cold_kind') in {'object-constructor',
                                       'application-cache-reset'}
            and 'client_wall_ms' in row]
    latency_failed = (any(row.get('client_wall_ms', 0) > 20000
                          for row in all_rows)
                      or any(percentiles(values)['p95'] > 2000
                             for values in warm_cases.values())
                      or any(value > 10000 for value in cold))
    functional = bool(all_rows) and report['functional_gate'] == 'passed'
    report['latency_gate'] = ('failed' if latency_failed else
                              'passed' if functional else 'unverified')
    report['preflight_gate'] = (
        'passed' if {row['kind'] for row in report.get('pilot', [])}
        == {'rest_search', 'mcp_search'} and all(
            row.get('success') and evidence_complete(row)
            for row in report['pilot']) else 'unverified')
    matrix_complete = (report.get('matrix_finished') is True
                       and all(cases.get(case, {}).get('samples', 0) >= 50
                               for case in EXPECTED_CASES)
                       and len(report.get('concurrency', [])) == 24
                       and all(row.get('eligible') for row in
                               report.get('concurrency', [])))
    phase_complete = (report['preflight_gate'] == 'passed'
                      if report.get('phase') == 'pilot' else matrix_complete)
    report['phase_complete'] = phase_complete
    gates = [report['functional_gate'], report['gateway_cpu_gate'],
             report['do_cpu_gate'], report['latency_gate']]
    report['sample_gate'] = ('failed' if 'failed' in gates else
                             'passed' if phase_complete and all(
                                 gate == 'passed' for gate in gates)
                             else 'unverified')
    report.update(runtime_gate='unverified', memory_gate='unverified',
                  isolate_cold_gate='unverified',
                  retrieval_quality='not_tested')
    report['limitations'] = [
        'Synthetic vectors do not test Workers AI or semantic usefulness.',
        'App cache reset and object construction do not prove a new isolate.',
        'Platform CPU must be scoped separately to gateway and object.',
        'Absent/aggregate data cannot establish request-level percentiles.',
        'Sample gates do not establish population p99 or production readiness.',
        'Memory, quality, account quotas and rollback need later evidence.',
    ]


def run_matrix(report, samples):
    for mode in ('application_cold', 'warm'):
        if mode == 'warm':
            for kind in KINDS:
                perform(report, kind, 'priming', -1, 'priming')
        for sequence in range(samples):
            for kind in KINDS:
                row = perform(report, kind, mode, sequence)
                if not row['success']:
                    report['load_stopped'] = 'Workload request failed'
                    return
        print(f'DO probe {mode}: {samples * len(KINDS)} requests complete',
              flush=True)
    # Only warm requests overlap; cold resets are deliberately serialized.
    for sequence in range(6):
        batch = [prepare(report, 'rest_search' if i % 2 == 0 else 'mcp_search',
                         'warm', 1000 + sequence * 4 + i, 'concurrency')
                 for i in range(4)]
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            pending = {pool.submit(send, report, row): row for row in batch}
            for future in concurrent.futures.as_completed(pending):
                pending[future].update(future.result())
                report['finished_ms'] = int(time.time() * 1000)
                persist(report)
    report['matrix_finished'] = True


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('origin', nargs='?')
    parser.add_argument('--script-name', required=True)
    parser.add_argument('--output', type=Path,
                        default=Path('do-probe-report.json'))
    parser.add_argument('--phase', choices=('pilot', 'matrix'),
                        default='pilot')
    parser.add_argument('--samples', type=int, default=50)
    parser.add_argument('--wait-seconds', type=int, default=180)
    parser.add_argument('--ready-wait-seconds', type=int, default=60)
    parser.add_argument('--collect-only', type=Path)
    parser.add_argument('--max-load-seconds', type=int, default=1200)
    parser.add_argument('--local', action='store_true')
    args = parser.parse_args(argv)
    if (not 1 <= args.samples <= 50 or not 0 <= args.wait_seconds <= 300
            or not 0 <= args.ready_wait_seconds <= 60
            or not 30 <= args.max_load_seconds <= 1800):
        parser.error(
            'samples 1..50, wait 0..300, readiness 0..60, load 30..1800')
    if args.collect_only:
        report = json.loads(args.collect_only.read_text(encoding='utf-8'))
        if report.get('probe_type') != 'durable-object':
            parser.error('Report is not a Durable Object probe')
        report['output_path'] = str(args.output.resolve())
    else:
        parsed = urllib.parse.urlsplit(args.origin or '')
        local = args.local and parsed.hostname in {
            'localhost', '127.0.0.1', '::1'}
        if (parsed.scheme != 'https'
                and not (local and parsed.scheme == 'http')
                or any((parsed.username, parsed.password, parsed.query,
                        parsed.fragment)) or parsed.path not in ('', '/')):
            parser.error(
                'Use a clean HTTPS origin, or --local with loopback HTTP')
        if not os.environ.get('PROBE_TOKEN'):
            parser.error('PROBE_TOKEN environment variable is required')
        report = {
            'probe_type': 'durable-object', 'origin': args.origin.rstrip('/'),
            'run_id': str(uuid.uuid4()), 'started_ms': int(time.time() * 1000),
            'script_name': args.script_name, 'phase': args.phase,
            'source_sha': os.environ.get('GITHUB_SHA', ''),
            'load_deadline_ms': (int(time.time() * 1000)
                                 + args.max_load_seconds * 1000),
            'output_path': str(args.output.resolve()), 'requests': [],
        }
        persist(report)
        deadline = time.monotonic() + args.ready_wait_seconds
        while True:
            try:
                row = perform(report, 'info', 'discovery', 0, 'discovery')
            except ValueError as exc:
                report['load_stopped'] = str(exc)[:200]
                summarize(report)
                persist(report)
                return 2
            if row['success']:
                report['info'] = row.pop('info')
                report['object_id'] = row['object_id']
                break
            transient = (None, 404, 408, 429, 500, 502, 503, 504)
            if (row.get('status') not in transient
                    or row.get('object_id') or row.get('boot_id')
                    or time.monotonic() >= deadline):
                summarize(report)
                persist(report)
                return 1
            # Retain propagation errors separately from workload failures.
            row['startup_retry'] = True
            time.sleep(min(2, max(0, deadline - time.monotonic())))
        try:
            perform(report, 'rest_search', 'application_cold', 0, 'pilot')
            perform(report, 'mcp_search', 'application_cold', 1, 'pilot')
        except ValueError as exc:
            report['load_stopped'] = str(exc)[:200]
            summarize(report)
            persist(report)
            return 2
        if not args.local:
            collect(report, args.wait_seconds)
        summarize(report)
        persist(report)
        pilot_success = all(row['success'] for row in report['pilot'])
        if not pilot_success or (not args.local and (
                report['preflight_gate'] != 'passed'
                or report['sample_gate'] == 'failed')):
            print('DO telemetry pilot did not pass; no matrix was sent.',
                  flush=True)
            return 1 if report['sample_gate'] == 'failed' else 2
        if args.phase == 'matrix':
            try:
                run_matrix(report, args.samples)
            except (ValueError, OSError) as exc:
                report['load_stopped'] = str(exc)[:200]
            finally:
                summarize(report)
                persist(report)
    if not args.local:
        collect(report, args.wait_seconds)
    summarize(report)
    persist(report)
    print(json.dumps({name: report[name] for name in (
        'sample_gate', 'gateway_cpu_gate', 'do_cpu_gate', 'runtime_gate')}))
    if report['sample_gate'] == 'failed':
        return 1
    if args.local:
        return 0 if report['functional_gate'] == 'passed' else 1
    return 0 if report['sample_gate'] == 'passed' else 2


if __name__ == '__main__':
    raise SystemExit(main())
