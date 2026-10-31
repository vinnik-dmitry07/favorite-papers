'''Run the bounded full synthetic geometry workload against an isolated DO.

No embeddings, deployment, or provider calls are made. The 324 REST/MCP
requests match full-memory.ts; three authenticated controls verify identity
and prepare reference vectors. Exit 1 means failure, 2 missing requested CPU
evidence, and 0 completed observed checks, never production readiness.
'''

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import http.client
import json
import math
import multiprocessing
import os
from pathlib import Path
import re
import time
import urllib.parse
import uuid

from run_static_search_do_probe import collect, finite_number
from run_static_search_probe import decode_body, percentiles, persist

MAX_REQUESTS = 350
MAX_RESPONSE_BYTES = 1024 * 1024
CONTENT_MAX = 32000
WORKLOAD_REQUESTS = 324
SCRIPT_PATTERN = r'key-papers-static-do-probe-\d+-\d+'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate_url(value, script_name=None):
    '''Only the existing temporary probe namespace; never follow redirects.'''
    url = urllib.parse.urlsplit(value)
    require(url.scheme == 'https' and not any((url.username, url.password,
            url.query, url.fragment)) and url.path in ('', '/')
            and url.port is None, 'Expected a clean HTTPS probe origin')
    require(re.fullmatch(SCRIPT_PATTERN + r'\.[a-z0-9-]+\.workers\.dev',
                         url.hostname or ''), 'Unexpected probe hostname')
    name = url.hostname.split('.')[0]
    require(script_name is None or script_name == name,
            'Script name does not match probe origin')
    return value.rstrip('/'), name


def read_fixture(assets):
    root = Path(assets).resolve()
    raw = (root / 'probe.json').read_bytes()
    manifest = json.loads(raw)
    require(manifest.get('kind') == 'full-corpus-int8-geometry-fixture'
            and manifest.get('synthetic') is True
            and manifest.get('publication_ready') is False
            and manifest.get('dimensions') == 768,
            'Expected the isolated packed synthetic geometry fixture')
    require(type(manifest.get('passage_count')) is int
            and 1 <= manifest['passage_count'] <= 60000
            and re.fullmatch(r'[a-f0-9]{64}', manifest['release_id']),
            'Invalid fixture geometry or release identity')
    relative = manifest['graph_path']
    require(isinstance(relative, str) and '\\' not in relative
            and not relative.startswith('/') and all(
                part not in ('', '.', '..') for part in relative.split('/')),
            'Unsafe graph asset path')
    path = (root / relative).resolve()
    require(path.is_relative_to(root), 'Graph escaped the asset directory')
    graph_bytes = path.read_bytes()
    require(hashlib.sha256(graph_bytes).hexdigest()
            == manifest['files'][relative]['sha256'], 'Graph checksum mismatch')
    nodes = json.loads(graph_bytes)['nodes']
    require(sorted(nodes) == manifest['paper_ids'], 'Catalog identity mismatch')
    papers = [node for node in nodes.values() if node['text']['available']]
    require(sorted(node['id'] for node in papers) == manifest['text_paper_ids']
            and len(papers) >= 48, 'Expected at least 48 verified text papers')
    papers.sort(key=lambda node: (-node['text']['code_points'], node['id']))
    identity = {
        'manifest_sha256': hashlib.sha256(raw).hexdigest(),
        'release_id': manifest['release_id'],
        'passages': manifest['passage_count'], 'papers': len(nodes),
        'text_papers': len(papers),
    }
    return identity, nodes, papers


def exchange(url, payload, headers, timeout):
    '''Bound response bytes and refuse redirects, including same-host ones.'''
    parsed = urllib.parse.urlsplit(url)
    connection = http.client.HTTPSConnection(parsed.hostname, timeout=timeout)
    body = None if payload is None else json.dumps(payload).encode()
    try:
        connection.request('GET' if body is None else 'POST',
                           urllib.parse.urlunsplit(('', '', parsed.path,
                                                   parsed.query, '')),
                           body=body, headers={
                               'accept': 'application/json, text/event-stream',
                               'content-type': 'application/json',
                               'mcp-protocol-version': '2025-06-18',
                               **headers,
                           })
        response = connection.getresponse()
        raw = response.read(MAX_RESPONSE_BYTES + 1)
        require(len(raw) <= MAX_RESPONSE_BYTES, 'Response exceeds byte budget')
        return response.status, dict(response.getheaders()), raw.decode('utf-8')
    finally:
        connection.close()


def validate_body(body, spec, identity, nodes):
    kind, args = spec['kind'], spec['args']
    if kind in ('status', 'prepare'):
        require(body.get('kind') == 'full-geometry-probe'
                and body.get('synthetic') is True
                and all(body.get(key) == value
                        for key, value in identity.items()),
                'Remote synthetic fixture identity mismatch')
        if kind == 'prepare':
            require(body.get('prepared_queries') == 16,
                    'Expected 16 prepared reference queries')
        return
    require(body.get('corpus_version') == identity['release_id'],
            'Unexpected corpus version')
    if kind == 'catalog':
        require(body.get('total') == identity['papers']
                and isinstance(body.get('papers'), list)
                and len(body['papers']) == 24
                and all(item.get('id') in nodes for item in body['papers']),
                'Invalid catalog response')
    elif kind in ('content', 'contents', 'find'):
        length = nodes[args['id']]['text']['code_points']
        require(body.get('paper_id') == args['id']
                and body.get('available') is True, 'Paper identity mismatch')
        if kind == 'content':
            offset = args.get('offset', 0)
            size = min(CONTENT_MAX, length - offset)
            require(body.get('total_length') == length
                    and body.get('offset') == offset
                    and isinstance(body.get('text'), str)
                    and len(body['text']) == size
                    and body.get('next_offset') == (
                        offset + size if offset + size < length else None),
                    'Invalid content length, offset or continuation')
        elif kind == 'contents':
            require(body.get('total_length') == length
                    and isinstance(body.get('sections'), list)
                    and all(0 <= section['offset'] < length
                            for section in body['sections']),
                    'Invalid contents offsets')
        else:
            require(isinstance(body.get('matches'), list)
                    and all(0 <= item['start'] < item['end'] <= length
                            for item in body['matches']),
                    'Invalid find offsets')
    elif kind == 'search':
        hits = body.get('hits')
        require(isinstance(hits, list) and 1 <= len(hits) <= 8,
                'Invalid search hit count')
        require(len({hit['paper_id'] for hit in hits}) == len(hits),
                'Duplicate search papers')
        for hit in hits:
            node = nodes.get(hit.get('paper_id'))
            score = hit.get('score')
            require(node and node['text']['available']
                    and isinstance(score, (int, float))
                    and not isinstance(score, bool) and math.isfinite(score)
                    and 0 <= hit['start'] < hit['end']
                    <= node['text']['code_points']
                    and hit.get('corpus_version') == identity['release_id'],
                    'Invalid search hit geometry or identity')


def request_spec(kind, args=None, mcp=False):
    return {'kind': kind, 'args': args or {}, 'mcp': mcp}


def send(report, record, spec, token, nodes, deadline):
    started = time.monotonic()
    result = dict(record)
    try:
        remaining = deadline - started
        require(remaining > 0, 'Workload time budget exhausted')
        kind = spec['kind']
        if spec['mcp']:
            names = {'content': 'read_content', 'find': 'find_in_paper',
                     'search': 'search_passages'}
            path = '/mcp'
            payload = {'jsonrpc': '2.0', 'id': record['sequence'],
                       'method': 'tools/call', 'params': {
                           'name': names[kind], 'arguments': spec['args']}}
        else:
            path = ('/_probe/' if kind in ('status', 'prepare')
                    else '/v1/') + kind
            path += '?' + urllib.parse.urlencode(spec['args'])
            payload = None
        status, headers, wire = exchange(report['origin'] + path, payload, {
            'x-probe-token': token, 'x-probe-marker': record['marker'],
            'x-probe-run-id': report['run_id'],
        }, min(30, remaining))
        headers = {key.lower(): value for key, value in headers.items()}
        result.update(status=status, boot_id=headers.get('x-probe-boot-id'),
                      object_id=headers.get('x-probe-object-id'),
                      first_request=headers.get('x-probe-first-request'))
        require(headers.get('x-probe-marker') == record['marker']
                and headers.get('x-probe-runtime-role') == 'durable_object'
                and headers.get('x-probe-synthetic') == 'true'
                and headers.get('x-probe-manifest-sha256')
                == report['identity']['manifest_sha256']
                and result['boot_id'] and result['object_id']
                and result['first_request'] in ('true', 'false'),
                'Missing or incorrect isolated probe response identity')
        if status == 503 and record['allow_overload']:
            body = decode_body(wire)
            require(body.get('error', {}).get('code') == 'probe_overloaded',
                    'Unexpected 503 response')
            result['controlled_overload'] = True
        else:
            require(status == 200, f'Unexpected HTTP status {status}')
            body = decode_body(wire, spec['mcp'])
            validate_body(body, spec, report['identity'], nodes)
            if kind in ('status', 'prepare'):
                result['control'] = body
        result['success'] = True
    except Exception as exc:
        # Neither an exception containing a URL nor an echoed body may leak
        # the authentication token. Validation messages are our own constants.
        result['error'] = (str(exc)[:160] if isinstance(exc, ValueError)
                           and not isinstance(exc, json.JSONDecodeError)
                           else type(exc).__name__)
        result['error'] = result['error'].replace(token, '[redacted]')
    result.update(state='complete',
                  client_wall_ms=(time.monotonic() - started) * 1000)
    return result


def run_batch(report, phase, specs, token, nodes, deadline,
              concurrency=1, allow_overload=False):
    require(time.monotonic() < deadline, 'Workload time budget exhausted')
    require(report['http_attempts'] + len(specs) <= MAX_REQUESTS,
            'External request budget exhausted')
    if not any(row['phase'] == phase for row in report['requests']):
        print('Full geometry probe: ' + phase, flush=True)
    rows = []
    for spec in specs:
        record = {
            'marker': str(uuid.uuid4()), 'phase': phase,
            'case': phase + '.' + ('mcp_' if spec['mcp'] else 'rest_')
            + spec['kind'], 'kind': spec['kind'],
            'sequence': report['http_attempts'], 'state': 'in_flight',
            'success': False, 'allow_overload': allow_overload,
        }
        report['http_attempts'] += 1
        report['requests'].append(record)
        rows.append(record)
    persist(report)
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as pool:
        pending = {pool.submit(send, report, row, spec, token, nodes,
                               deadline): row for row, spec in zip(rows, specs)}
        for future in concurrent.futures.as_completed(pending):
            pending[future].update(future.result())
            report['finished_ms'] = int(time.time() * 1000)
            persist(report)
    require(all(row['success'] for row in rows),
            'Workload request failed; no retry was sent')
    require(any(not row.get('controlled_overload') for row in rows),
            'Every burst request was rejected')
    require(len({row['object_id'] for row in report['requests']}) == 1,
            'Requests routed to different Durable Objects')
    return rows


def run_workload(report, token, nodes, papers, deadline):
    def batch(phase, specs, concurrency=1, overload=False):
        return run_batch(report, phase, specs, token, nodes, deadline,
                         concurrency, overload)

    def content(node, mcp=False, offset=0):
        return request_spec('content', {
            'id': node['id'], 'offset': offset, 'length': CONTENT_MAX}, mcp)

    def search(index):
        return request_spec('search', {'q': f'memory workload query {index}',
                                       'k': 8}, bool(index % 2))

    batch('cold-catalog-burst', [request_spec('catalog', {'limit': 24})
                                for _ in range(16)], 16, True)
    report['initial_status'] = batch(
        'identity', [request_spec('status')])[0]['control']
    largest = papers[0]
    for spec in [content(largest), content(largest, True, max(
            0, largest['text']['code_points'] - CONTENT_MAX)),
            request_spec('contents', {'id': largest['id']}),
            request_spec('find', {'id': largest['id'], 'q': 'the',
                                  'offset': 0}, True)]:
        batch('largest-paper-rest-mcp', [spec])
    for round_number in range(4):
        batch('paper-burst', [content(
            papers[(round_number * 20 + index + 1) % len(papers)],
            bool(index % 2)) for index in range(20)], 20, True)
    for paper in papers[:48]:
        batch('paper-cache-churn', [content(paper)])
    report['prepared_status'] = batch(
        'prepare', [request_spec('prepare')])[0]['control']
    for start in range(0, 160, 4):
        batch('search-cache-churn-' + str(start // 80 + 1),
              [search(index) for index in range(start, start + 4)], 4)
    for _ in range(4):
        batch('repeat-cached-queries', [search(index)
                                      for index in range(156, 160)], 4)
    report['final_status'] = batch(
        'final-status', [request_spec('status')])[0]['control']
    final = report['final_status']
    require(final.get('prepared_queries') == 16
            and final.get('embedded_queries') == 160,
            'Unexpected preparation or embedding count after cached repeats')
    require(sum(row['kind'] not in ('status', 'prepare')
                for row in report['requests']) == WORKLOAD_REQUESTS,
            'Incomplete 324-request workload')
    report['workload_complete'] = True
    persist(report)


def summarize(report):
    rows = report.get('requests', [])
    report['functional_gate'] = (
        'failed' if report.get('error') or any(
            row['state'] == 'complete' and not row['success'] for row in rows)
        else 'passed' if report.get('workload_complete') else 'unverified')
    report['phases'] = {}
    for phase in sorted({row['phase'] for row in rows}):
        sample = [row for row in rows if row['phase'] == phase]
        report['phases'][phase] = {
            'attempted': len(sample),
            'completed': sum(row.get('success', False) for row in sample),
            'controlled_overload': sum(row.get('controlled_overload', False)
                                       for row in sample),
            'client_wall_ms': percentiles([row['client_wall_ms']
                for row in sample if 'client_wall_ms' in row]),
        }
    report['cpu'] = {}
    for role, limit in (('gateway', 8), ('durable_object', 30000)):
        evidence = [row.get('telemetry', {}).get(role, {}) for row in rows]
        values = [item['cpu_ms'] for item in evidence
                  if finite_number(item.get('cpu_ms'))]
        failed = any(value >= limit for value in values) or any(
            item.get('outcome') not in (None, '', 'ok') for item in evidence)
        complete = bool(rows) and all(
            not row.get('telemetry_conflict')
            and finite_number(item.get('cpu_ms'))
            and item.get('outcome') == 'ok'
            for row, item in zip(rows, evidence))
        gate = 'failed' if failed else 'passed' if complete else 'unverified'
        report['gateway_cpu_gate' if role == 'gateway' else 'do_cpu_gate'] = gate
        report['cpu'][role] = {'gate': gate, 'matched': len(values),
                               'cpu_ms': percentiles(values),
                               'max_ms': max(values, default=None)}
    report.update(memory_gate='unverified', production_readiness='unverified',
                  semantic_quality_gate='not-measured',
                  workers_ai_compatibility='not-measured',
                  isolate_cold_gate='unverified')
    report['boot_ids'] = sorted({row['boot_id'] for row in rows
                                 if row.get('boot_id')})
    report['limitations'] = [
        'Synthetic reference vectors; no embedding provider or quality test.',
        'Client elapsed time is not CPU; only joined platform events supply CPU.',
        'Object boot IDs do not prove isolate cold starts or measure memory.',
        'Controlled overload is allowed only in designated bursts; no retries.',
        'Observed samples do not establish production readiness or population p99.',
    ]


def execute(args, report):
    deadline = time.monotonic() + args.max_load_seconds
    try:
        report['origin'], report['script_name'] = validate_url(
            args.base_url, args.script_name)
        token = os.environ.get(args.token_env, '')
        require(len(token) >= 32, 'Probe token environment variable is missing')
        identity, nodes, papers = read_fixture(args.assets)
        report['identity'] = identity
        persist(report)
        run_workload(report, token, nodes, papers, deadline)
    except Exception as exc:
        report['error'] = (str(exc)[:200] if type(exc) is ValueError
                           else type(exc).__name__)
        token = os.environ.get(args.token_env, '')
        if token:
            report['error'] = report['error'].replace(token, '[redacted]')
    finally:
        report['finished_ms'] = int(time.time() * 1000)
        report['workload_stopped_ms'] = report['finished_ms']
        summarize(report)
        persist(report)
    if args.wait_seconds and report.get('requests'):
        try:
            collect(report, args.wait_seconds)
        except Exception as exc:
            report['telemetry_error'] = type(exc).__name__
        summarize(report)
        persist(report)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--assets', type=Path, required=True)
    parser.add_argument('--base-url', required=True)
    parser.add_argument('--token-env', default='PROBE_TOKEN')
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--script-name')
    parser.add_argument('--wait-seconds', type=int, default=0)
    parser.add_argument('--max-load-seconds', type=int, default=300)
    args = parser.parse_args(argv)
    if not 0 <= args.wait_seconds <= 120 or not 1 <= args.max_load_seconds <= 300:
        parser.error('wait-seconds must be 0..120; max-load-seconds 1..300')
    report = {'schema_version': 1, 'probe_type': 'full-geometry-durable-object',
              'synthetic': True, 'run_id': str(uuid.uuid4()),
              'started_ms': int(time.time() * 1000), 'requests': [],
              'http_attempts': 0, 'workload_complete': False,
              'max_load_seconds': args.max_load_seconds,
              'max_http_attempts': MAX_REQUESTS,
              'output_path': str(args.out.resolve())}
    persist(report)
    process = multiprocessing.get_context('spawn').Process(
        target=execute, args=(args, report))
    process.start()
    # A supervisor also bounds stalled DNS, response headers, or slow-drip
    # bodies, which ordinary socket timeouts alone cannot bound end to end.
    deadline = time.monotonic() + args.max_load_seconds
    while process.is_alive():
        process.join(min(1, max(0, deadline - time.monotonic())))
        checkpoint = json.loads(args.out.read_text(encoding='utf-8'))
        if 'workload_stopped_ms' in checkpoint:
            break
        if time.monotonic() >= deadline:
            break
    if process.is_alive() and 'workload_stopped_ms' in checkpoint:
        process.join(args.wait_seconds + 1)
    if process.is_alive():
        process.terminate()
        process.join(1)
        if process.is_alive():
            process.kill()
            process.join()
        report = json.loads(args.out.read_text(encoding='utf-8'))
        report['error'] = 'Hard process time budget exhausted'
    else:
        report = json.loads(args.out.read_text(encoding='utf-8'))
        if process.exitcode:
            report['error'] = 'Runner process exited unexpectedly'
    summarize(report)
    persist(report)
    gates = [report['functional_gate'], report['gateway_cpu_gate'],
             report['do_cpu_gate']]
    print(json.dumps({key: report[key] for key in (
        'functional_gate', 'gateway_cpu_gate', 'do_cpu_gate',
        'memory_gate', 'workload_complete')}))
    if 'failed' in gates:
        return 1
    return 0 if gates[0] == 'passed' and (
        not args.wait_seconds or all(gate == 'passed' for gate in gates)) else 2


if __name__ == '__main__':
    raise SystemExit(main())
