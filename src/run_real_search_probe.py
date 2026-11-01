'''Run a bounded real-subset REST/MCP integration probe.

The workload uses canonical source text as its response oracle. Compatibility,
contracts, answer context and latency are separate from passage retrieval,
platform CPU coverage, memory, full-corpus quality and production readiness.
'''

from __future__ import annotations

import argparse
import base64
import hashlib
import http.client
import json
import math
import os
import re
import time
import urllib.parse
import uuid
from pathlib import Path

from run_static_search_do_probe import collect, finite_number, records
from run_static_search_probe import decode_body, exchange, percentiles, persist

MAX_REQUESTS = 60
LOAD_SECONDS = 600
COMPATIBILITY_BATCHES = 14
MODEL_REVISION = 'a5beb1e3e68b9ab74eb54cfd186867f64f240e1a'
GROUPS = (
    'compatibility_gate',
    'contracts_gate',
    'answer_context_gate',
    'latency_gate',
    'budget_gate',
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def integer(value):
    return isinstance(value, int) and not isinstance(value, bool)


def evidence_required(query):
    return bool(
        query.get('required_passage_terms')
        or query.get('passage_evidence_any')
    )


def text_supports_evidence(text, query):
    '''Match the declared source terms only within the supplied text window.'''
    text = text.casefold()
    required = query.get('required_passage_terms', [])
    alternatives = query.get('passage_evidence_any', [])
    return all(term.casefold() in text for term in required) and (
        not alternatives
        or any(
            all(term.casefold() in text for term in group)
            for group in alternatives
        )
    )


def load_fixture(path, expected_hash):
    '''Load the exact manifest and independently verify its response oracles.'''
    path = Path(path)
    raw = path.read_bytes()
    require(
        re.fullmatch(r'[a-f0-9]{64}', expected_hash),
        'Expected manifest SHA-256 is required',
    )
    require(sha256(raw) == expected_hash, 'Local manifest hash mismatch')
    manifest = json.loads(raw)
    require(
        isinstance(manifest, dict)
        and manifest.get('kind') == 'real-subset'
        and manifest.get('synthetic') is False
        and manifest.get('schema_version') == 1,
        'Expected a versioned real-subset manifest',
    )
    rows = manifest.get('rows')
    require(
        isinstance(rows, list)
        and 200 <= len(rows) <= 500
        and manifest.get('passage_count') == len(rows)
        and manifest.get('dimensions') == 768,
        'Expected 200–500 canonical 768-dimensional passages',
    )
    embedding = manifest.get('embeddings')
    require(
        isinstance(embedding, dict)
        and embedding.get('model_revision') == MODEL_REVISION
        and embedding.get('pooling') == 'cls'
        and embedding.get('normalization') == 'l2'
        and embedding.get('dtype') == 'float32'
        and embedding.get('byte_order') == 'little',
        'Pinned local FP32 embeddings are required',
    )
    files = manifest.get('files')
    require(isinstance(files, dict) and files, 'Missing asset checksums')
    require(
        embedding.get('path') in files
        and files[embedding['path']] == embedding.get('sha256'),
        'Vector artifact checksum is missing or inconsistent',
    )
    loaded = {}
    for name, expected in files.items():
        require(
            isinstance(name, str)
            and name
            and not Path(name).is_absolute()
            and '..' not in Path(name).parts
            and '\\' not in name,
            'Unsafe asset path',
        )
        asset = path.parent / name
        require(
            asset.resolve().is_relative_to(path.parent.resolve()),
            'Asset escaped the fixture directory',
        )
        data = asset.read_bytes()
        require(sha256(data) == expected, f'Asset hash mismatch: {name}')
        if name.endswith('.json'):
            loaded[name] = json.loads(data)
    release = manifest['release_id']
    graph = loaded.get(f'releases/{release}/graph.json')
    require(isinstance(graph, dict), 'Missing canonical graph')
    papers = {}
    for paper_id in manifest['paper_ids']:
        name = sha256(paper_id.encode())
        paper = loaded.get(f'releases/{release}/papers/{name}.json')
        require(
            isinstance(paper, dict) and paper.get('paper_id') == paper_id,
            'Missing canonical paper',
        )
        papers[paper_id] = paper
    require(
        set(papers) == set(graph.get('nodes', {})), 'Subset graph mismatch'
    )
    require(
        any(
            ord(char) > 0xFFFF
            for paper in papers.values()
            for char in paper['text']
        ),
        'Subset lacks a non-BMP offset oracle',
    )
    require(
        (path.parent / embedding['path']).stat().st_size
        == len(rows) * 768 * 4,
        'Vector byte count mismatch',
    )
    by_chunk = {}
    for row in rows:
        paper = papers[row['paper_id']]
        chunk = next(
            (
                value
                for value in paper['chunks']
                if value['index'] == row['chunk_index']
            ),
            None,
        )
        require(chunk is not None, 'Missing canonical chunk')
        require(
            all(
                chunk[key] == row[key]
                for key in (
                    'start',
                    'end',
                    'token_count',
                    'content_hash',
                    'input_hash',
                )
            ),
            'Canonical row differs from its paper chunk',
        )
        text = paper['text'][row['start'] : row['end']]
        require(
            sha256(text.encode()) == row['content_hash'],
            'Canonical chunk hash mismatch',
        )
        identity = (row['paper_id'], row['chunk_index'])
        require(identity not in by_chunk, 'Duplicate canonical chunk')
        by_chunk[identity] = row
    queries = manifest.get('queries')
    require(
        isinstance(queries, list) and len(queries) == 6,
        'The probe requires six fixed queries',
    )
    require(
        len({item['query'] for item in queries}) == 6
        and len({item['id'] for item in queries}) == 6,
        'Probe queries and their IDs must be distinct',
    )
    for query in queries:
        require(
            isinstance(query.get('id'), str)
            and isinstance(query.get('query'), str)
            and 1 <= len(query['query']) <= 2000
            and query.get('expected_paper_id') in papers,
            'Invalid fixed query',
        )
        require(
            all(
                query['query'].casefold() != node['title'].casefold()
                for node in graph['nodes'].values()
            ),
            'Semantic query must not be an exact paper title',
        )
    require(
        sum(evidence_required(item) for item in queries) >= 2,
        'At least two source-backed passage-evidence checks are required',
    )
    for query in queries:
        terms = query.get('required_passage_terms', [])
        alternatives = query.get('passage_evidence_any', [])
        require(
            isinstance(terms, list)
            and all(isinstance(term, str) and term for term in terms),
            'Invalid source-backed passage terms',
        )
        require(
            isinstance(alternatives, list)
            and all(
                isinstance(group, list)
                and group
                and all(isinstance(term, str) and term for term in group)
                for group in alternatives
            ),
            'Invalid passage-evidence alternatives',
        )
        if evidence_required(query):
            require(
                any(
                    text_supports_evidence(
                        papers[query['expected_paper_id']]['text'][
                            row['start'] : row['end']
                        ],
                        query,
                    )
                    for row in rows
                    if row['paper_id'] == query['expected_paper_id']
                ),
                'Passage oracle has no supporting canonical chunk',
            )
    indices = manifest.get('compatibility_indices')
    require(
        isinstance(indices, list)
        and len(indices) == 200
        and len(set(indices)) == len(indices)
        and all(
            integer(index) and 0 <= index < len(rows) for index in indices
        ),
        'Expected 200 compatibility rows',
    )
    return {
        'manifest': manifest,
        'sha256': expected_hash,
        'papers': papers,
        'graph': graph,
        'by_chunk': by_chunk,
    }


def fetch_identity(document_id):
    require(
        isinstance(document_id, str)
        and document_id.startswith('doc:')
        and len(document_id) <= 4096,
        'Invalid MCP document ID',
    )
    encoded = document_id[4:]
    try:
        decoded = base64.urlsafe_b64decode(encoded + '=' * (-len(encoded) % 4))
        value = json.loads(decoded)
    except (ValueError, UnicodeError) as exc:
        raise ValueError('Invalid MCP document identity') from exc
    require(
        isinstance(value, dict)
        and isinstance(value.get('paper'), str)
        and isinstance(value.get('version'), str)
        and (
            value.get('start') is None
            or integer(value.get('start'))
            and value['start'] >= 0
        ),
        'Invalid MCP document identity',
    )
    return value


def validate_rest_search(body, fixture):
    manifest = fixture['manifest']
    require(
        body.get('corpus_version') == manifest['release_id'],
        'Search version mismatch',
    )
    hits = body.get('hits')
    require(
        isinstance(hits, list) and 0 < len(hits) <= 8,
        'Search must return bounded nonempty hits',
    )
    seen = set()
    for hit in hits:
        key = (hit.get('paper_id'), hit.get('chunk_index'))
        row = fixture['by_chunk'].get(key)
        require(
            row is not None and hit['paper_id'] not in seen,
            'Unknown or duplicate search hit',
        )
        seen.add(hit['paper_id'])
        require(
            all(hit.get(key) == row[key] for key in ('start', 'end'))
            and hit.get('corpus_version') == manifest['release_id']
            and isinstance(hit.get('score'), (int, float))
            and math.isfinite(hit['score']),
            'Invalid passage identity',
        )
        paper = fixture['papers'][hit['paper_id']]
        require(
            hit.get('snippet')
            == paper['text'][row['start'] : row['end']][:480],
            'Snippet does not match canonical code-point range',
        )
        node = fixture['graph']['nodes'][hit['paper_id']]
        require(
            hit.get('url') == node.get('url'), 'Source citation URL mismatch'
        )
        content = urllib.parse.urlsplit(hit.get('content', ''))
        require(
            not content.scheme
            and not content.netloc
            and content.path == '/v1/content'
            and not content.fragment,
            'Search content link is not an allowed relative API link',
        )
        params = urllib.parse.parse_qs(content.query, strict_parsing=True)
        require(
            params
            == {
                'id': [hit['paper_id']],
                'offset': [str(row['start'])],
                'version': [manifest['release_id']],
            },
            'Search content link disagrees with its hit',
        )
    return hits


def validate_content(body, fixture, paper_id, offset, length):
    paper = fixture['papers'][paper_id]
    end = min(len(paper['text']), offset + length)
    require(
        body.get('corpus_version') == fixture['manifest']['release_id']
        and body.get('paper_id') == paper_id
        and body.get('available') is True
        and body.get('offset') == offset
        and body.get('total_length') == len(paper['text'])
        and body.get('next_offset')
        == (end if end < len(paper['text']) else None)
        and body.get('text') == paper['text'][offset:end],
        'Content does not match canonical code-point range',
    )


def validate_mcp_search(body, fixture):
    results = body.get('results')
    require(
        isinstance(results, list) and 0 < len(results) <= 8,
        'MCP search returned invalid results',
    )
    seen = set()
    for result in results:
        identity = fetch_identity(result.get('id'))
        require(result['id'] not in seen, 'Duplicate MCP result')
        seen.add(result['id'])
        require(
            identity['paper'] in fixture['papers']
            and identity['version'] == fixture['manifest']['release_id'],
            'MCP result identity is outside the subset',
        )
        start = identity['start']
        if start is not None:
            text = fixture['papers'][identity['paper']]['text']
            require(
                start % 16000 == 0 and start < len(text),
                'MCP text part is outside the canonical paper',
            )
        require(
            isinstance(result.get('title'), str)
            and isinstance(result.get('url'), str),
            'Invalid MCP citation',
        )
    return results


def validate_fetch(body, fixture, document_id):
    identity = fetch_identity(document_id)
    require(identity['start'] is not None, 'Text-part fetch expected')
    paper_id, start = identity['paper'], identity['start']
    text = fixture['papers'][paper_id]['text']
    end = min(len(text), start + 16000)
    metadata = body.get('metadata', {})
    require(
        body.get('id') == document_id
        and body.get('text') == text[start:end]
        and metadata.get('paper_id') == paper_id
        and metadata.get('corpus_version') == fixture['manifest']['release_id']
        and metadata.get('item_type') == 'text_part'
        and metadata.get('start') == start
        and metadata.get('end') == end
        and metadata.get('total_length') == len(text),
        'MCP fetch differs from the exact search result or canonical text',
    )
    source_url = fixture['graph']['nodes'][paper_id].get('url')
    if source_url:
        require(body.get('url') == source_url, 'MCP citation URL mismatch')


def passage_relevant(hit, query, fixture):
    if hit.get('paper_id') != query['expected_paper_id']:
        return False
    text = fixture['papers'][hit['paper_id']]['text'][
        hit['start'] : hit['end']
    ]
    return text_supports_evidence(text, query)


def validate_budget(value, previous=None):
    require(isinstance(value, dict), 'Missing AI budget evidence')
    names = (
        'compatibility_texts',
        'query_texts',
        'total_texts',
        'input_tokens',
        'ai_calls',
    )
    require(
        all(integer(value.get(key)) and value[key] >= 0 for key in names),
        'Invalid AI budget counters',
    )
    require(
        value['total_texts']
        == value['compatibility_texts'] + value['query_texts']
        and value['total_texts'] <= 300
        and value['query_texts'] <= 24
        and value['input_tokens'] <= 153600,
        'AI input budget exceeded or inconsistent',
    )
    require(
        value.get('limits')
        == {
            'total_texts': 300,
            'query_texts': 24,
            'input_tokens': 153600,
        },
        'Unexpected server-side AI budget limits',
    )
    if previous:
        require(
            all(value[key] >= previous[key] for key in names),
            'AI budget counters went backwards',
        )


def validate_compatibility(body, fixture, previous_checked=0):
    expected_indices = fixture['manifest']['compatibility_indices']
    require(
        body.get('status') in ('not_started', 'running', 'passed', 'failed')
        and body.get('expected') == len(expected_indices)
        and body.get('threshold') == 0.999
        and integer(body.get('checked'))
        and previous_checked <= body['checked'] <= len(expected_indices),
        'Invalid or regressed compatibility progress',
    )
    results = body.get('results', [])
    require(
        isinstance(results, list) and len(results) == body['checked'],
        'Compatibility result count mismatch',
    )
    require(
        [item.get('index') for item in results]
        == expected_indices[: body['checked']],
        'Compatibility checked different canonical rows',
    )
    require(
        all(
            finite_number(item.get('remote_norm')) and item['remote_norm'] > 0
            for item in results
        ),
        'Invalid remote embedding norm',
    )
    cosines = [item.get('cosine') for item in results]
    require(
        all(finite_number(value) and value <= 1.000001 for value in cosines),
        'Invalid cosine measurement',
    )
    minimum = min(cosines) if cosines else None
    require(
        body.get('min_cosine') == minimum,
        'Compatibility minimum does not match individual results',
    )
    if body['status'] == 'passed':
        require(
            body['checked'] == len(expected_indices)
            and minimum is not None
            and minimum >= 0.999,
            'Compatibility cannot pass with missing or incompatible vectors',
        )
    return body['status']


class Probe:
    def __init__(self, report, fixture):
        self.report = report
        self.fixture = fixture

    def request(
        self,
        kind,
        path,
        *,
        params=None,
        payload=None,
        expected_status=200,
        mcp=False,
        timeout=20,
    ):
        report = self.report
        require(
            report['http_attempts'] < MAX_REQUESTS,
            'Service request budget exhausted',
        )
        require(
            time.monotonic() < report['_deadline'], 'Load deadline exhausted'
        )
        require(
            path.startswith('/')
            and not path.startswith('//')
            and not urllib.parse.urlsplit(path).scheme,
            'Only local API routes may be requested',
        )
        report['http_attempts'] += 1
        row = {
            'marker': str(uuid.uuid4()),
            'kind': kind,
            'case': kind,
            'mode': 'integration',
            'sequence': report['http_attempts'],
            'state': 'in_flight',
            'success': False,
            'eligible': True,
            'started_ms': int(time.time() * 1000),
        }
        report['requests'].append(row)
        persist(report)
        started = time.perf_counter()
        try:
            query = '?' + urllib.parse.urlencode(params) if params else ''
            status, headers, text = exchange(
                report['origin'] + path + query,
                payload,
                {
                    'x-probe-token': os.environ.get('PROBE_TOKEN', ''),
                    'x-probe-marker': row['marker'],
                    'x-probe-run-id': report['run_id'],
                },
                timeout=min(
                    timeout, max(0.01, report['_deadline'] - time.monotonic())
                ),
            )
            headers = {key.lower(): value for key, value in headers.items()}
            row.update(
                status=status,
                object_id=headers.get('x-probe-object-id'),
                boot_id=headers.get('x-probe-boot-id'),
            )
            require(
                headers.get('x-probe-runtime') == 'durable-object'
                and headers.get('x-probe-kind') == 'real-subset'
                and headers.get('x-probe-synthetic') == 'false'
                and headers.get('x-probe-marker') == row['marker']
                and headers.get('x-probe-manifest-sha256')
                == self.fixture['sha256']
                and row['object_id']
                and row['boot_id'],
                'Response probe identity mismatch',
            )
            if report.get('object_id'):
                require(
                    row['object_id'] == report['object_id'],
                    'Request routed to another object',
                )
            else:
                report['object_id'] = row['object_id']
            require(
                status == expected_status,
                f'Expected HTTP {expected_status}, received {status}',
            )
            body = decode_body(text, mcp=mcp)
            row['response'] = body
            row['success'] = True
            return body
        except (
            OSError,
            http.client.HTTPException,
            ValueError,
            KeyError,
            TypeError,
            IndexError,
        ) as exc:
            row['error'] = f'{type(exc).__name__}: {exc}'[:300]
            raise ValueError(row['error']) from exc
        finally:
            row.update(
                state='complete',
                finished_ms=int(time.time() * 1000),
                client_wall_ms=(time.perf_counter() - started) * 1000,
            )
            report['finished_ms'] = row['finished_ms']
            persist(report)

    def call(self, tool, arguments, kind=None):
        return self.request(
            kind or 'mcp_' + tool,
            '/mcp',
            mcp=True,
            payload={
                'jsonrpc': '2.0',
                'id': self.report['http_attempts'] + 1,
                'method': 'tools/call',
                'params': {'name': tool, 'arguments': arguments},
            },
        )

    def budget(self, value):
        validate_budget(value, self.report.get('budget'))
        self.report['budget'] = value
        persist(self.report)

    def info(self):
        body = self.request('info', '/probe/info')
        manifest = self.fixture['manifest']
        require(
            body.get('probe_type') == 'real-subset'
            and body.get('synthetic') is False
            and body.get('runtime') == 'durable-object'
            and body.get('scope') == 'subset'
            and body.get('manifest_sha256') == self.fixture['sha256']
            and body.get('release_id') == manifest['release_id']
            and body.get('source_sha') == manifest['source_sha']
            and body.get('passage_count') == manifest['passage_count']
            and body.get('paper_ids') == manifest['paper_ids']
            and body.get('queries') == manifest['queries']
            and body.get('compatibility_indices')
            == manifest['compatibility_indices'],
            'Discovery does not describe the pinned real subset',
        )
        self.budget(body.get('budget'))
        self.report['info'] = body
        return body

    def discover(self):
        for attempt in range(6):
            try:
                return self.info()
            except ValueError:
                row = self.report['requests'][-1]
                if (
                    attempt == 5
                    or row.get('object_id')
                    or row.get('boot_id')
                    or row.get('status')
                    not in (None, 404, 408, 429, 500, 502, 503, 504)
                ):
                    raise
                row['startup_retry'] = True
                persist(self.report)
                time.sleep(
                    min(1, max(0, self.report['_deadline'] - time.monotonic()))
                )

    def compatibility(self):
        checked = 0
        for _ in range(COMPATIBILITY_BATCHES):
            body = self.request(
                'compatibility', '/probe/compatibility', payload={}, timeout=60
            )
            status = validate_compatibility(body, self.fixture, checked)
            self.budget(body.get('budget'))
            self.report['compatibility'] = body
            persist(self.report)
            if status == 'failed':
                self.report['compatibility_gate'] = 'failed'
                raise ValueError(
                    'Local BGE and Workers AI compatibility failed'
                )
            if status == 'passed':
                self.report['compatibility_gate'] = 'passed'
                return
            require(
                body['checked'] > checked, 'Compatibility made no progress'
            )
            checked = body['checked']
        raise ValueError('Compatibility batch budget exhausted')

    def journeys(self):
        fixture, report = self.fixture, self.report
        report['journeys'] = []
        for query in fixture['manifest']['queries']:
            q = query['query']
            body = self.request(
                'rest_search', '/v1/search', params={'q': q, 'k': 8}
            )
            hits = validate_rest_search(body, fixture)
            relevant = any(
                passage_relevant(hit, query, fixture) for hit in hits
            )
            chosen = next(
                (
                    hit
                    for hit in hits
                    if hit['paper_id'] == query['expected_paper_id']
                ),
                hits[0],
            )
            # Follow the production default reading window from the returned
            # passage. Keep its answer evidence separate from the passage score.
            length = 6000
            content = self.request(
                'content',
                '/v1/content',
                params={
                    'id': chosen['paper_id'],
                    'offset': chosen['start'],
                    'version': fixture['manifest']['release_id'],
                    'length': length,
                },
            )
            validate_content(
                content, fixture, chosen['paper_id'], chosen['start'], length
            )
            context_relevant = chosen['paper_id'] == query[
                'expected_paper_id'
            ] and text_supports_evidence(content['text'], query)
            report['journeys'].append(
                {
                    'query_id': query['id'],
                    'protocol': 'rest',
                    'query': q,
                    'relevant': relevant,
                    'passage_relevant': relevant,
                    'answer_context_relevant': context_relevant,
                    'passage_evidence_required': evidence_required(query),
                    'required_passage_terms': query.get(
                        'required_passage_terms', []
                    ),
                    'passage_evidence_any': query.get(
                        'passage_evidence_any', []
                    ),
                    'paper_id': chosen['paper_id'],
                    'chunk_index': chosen['chunk_index'],
                    'start': chosen['start'],
                    'end': chosen['end'],
                    'context_start': content['offset'],
                    'context_end': content['offset'] + len(content['text']),
                    'context_length': len(content['text']),
                    'citation_url': chosen['url'],
                    'quote': content['text'][:160],
                    'contract_passed': True,
                }
            )
            result = self.call('search', {'query': q})
            results = validate_mcp_search(result, fixture)
            text_results = [
                item
                for item in results
                if fetch_identity(item['id'])['start'] is not None
            ]
            require(
                text_results, 'MCP search returned no fetchable paper text'
            )
            item = next(
                (
                    item
                    for item in text_results
                    if fetch_identity(item['id'])['paper']
                    == query['expected_paper_id']
                ),
                text_results[0],
            )
            fetched = self.call('fetch', {'id': item['id']})
            validate_fetch(fetched, fixture, item['id'])
            # MCP returns 16k document parts. These can support an answer, but
            # cannot substitute for an exact retrieved-passage diagnostic.
            paper_match = (
                fetch_identity(item['id'])['paper']
                == query['expected_paper_id']
            )
            report['journeys'].append(
                {
                    'query_id': query['id'],
                    'protocol': 'mcp',
                    'query': q,
                    'relevant': paper_match,
                    'answer_context_relevant': paper_match
                    and text_supports_evidence(fetched['text'], query),
                    'passage_evidence_required': evidence_required(query),
                    'required_passage_terms': query.get(
                        'required_passage_terms', []
                    ),
                    'passage_evidence_any': query.get(
                        'passage_evidence_any', []
                    ),
                    'document_id': item['id'],
                    'paper_id': fetched['metadata']['paper_id'],
                    'context_start': fetched['metadata']['start'],
                    'context_end': fetched['metadata']['end'],
                    'context_length': len(fetched['text']),
                    'citation_url': fetched['url'],
                    'quote': fetched['text'][:160],
                    'contract_passed': True,
                }
            )
            persist(report)

    def additional_contracts(self):
        fixture, report = self.fixture, self.report
        manifest, graph = fixture['manifest'], fixture['graph']
        seed, version = manifest['sample_paper_id'], manifest['release_id']
        expected = {edge['target'] for edge in graph['out'][seed]}
        expected |= {edge['source'] for edge in graph['in'][seed]}
        require(expected, 'Selected seed must have a graph connection')
        body = self.request(
            'citations',
            '/v1/citations',
            params={
                'id': seed,
                'dir': 'both',
                'limit': 24,
            },
        )
        require(
            body.get('corpus_version') == version
            and body.get('paper_id') == seed
            and body.get('total') == len(expected)
            and {node['id'] for node in body.get('neighbors', [])} == expected
            and body.get('next_cursor') is None,
            'Citation neighbors do not match the canonical subset graph',
        )
        body = self.request(
            'traverse',
            '/v1/traverse',
            params={
                'id': seed,
                'dir': 'both',
                'hops': 1,
                'max_nodes': 24,
            },
        )
        require(
            body.get('corpus_version') == version
            and body.get('seed') == seed
            and {node['id'] for node in body.get('nodes', [])}
            == expected | {seed},
            'Traversal does not match the canonical subset graph',
        )
        for edge in body.get('edges', []):
            require(
                {'target': edge['target'], 'evidence': edge['evidence']}
                in graph['out'][edge['source']],
                'Invented traversal edge',
            )
        report['graph_contracts_passed'] = True
        stale = 'f' * 64 if version != 'f' * 64 else 'e' * 64
        body = self.request(
            'stale_version',
            '/v1/content',
            expected_status=409,
            params={'id': seed, 'version': stale},
        )
        require(
            body.get('error', {}).get('code') == 'version_conflict',
            'Stale version was not rejected',
        )
        body = self.request(
            'query_bound',
            '/v1/search',
            expected_status=400,
            params={'q': 'x' * 2001},
        )
        require(
            body.get('error', {}).get('code') == 'query_too_long',
            'Oversized query was not rejected',
        )
        report['error_contracts_passed'] = True
        for paper_id, paper in fixture['papers'].items():
            index = next(
                (
                    i
                    for i, char in enumerate(paper['text'])
                    if ord(char) > 0xFFFF
                ),
                None,
            )
            if index is None:
                continue
            offset = max(0, index - 3)
            body = self.request(
                'unicode_content',
                '/v1/content',
                params={
                    'id': paper_id,
                    'offset': offset,
                    'length': 12,
                    'version': version,
                },
            )
            validate_content(body, fixture, paper_id, offset, 12)
            report['unicode_contract_passed'] = True
            break
        require(
            report.get('unicode_contract_passed'),
            'Subset lacks a non-BMP offset test',
        )


def summarize(report):
    rows = records(report)
    report['contracts_gate'] = (
        'failed'
        if report.get('failure')
        and report.get('failure_stage')
        in ('discovery', 'journeys', 'contracts')
        else (
            'passed'
            if report.get('phase_complete')
            and len(report.get('journeys', [])) == 12
            and all(row.get('success') for row in rows)
            and report.get('graph_contracts_passed')
            and report.get('error_contracts_passed')
            and report.get('unicode_contract_passed')
            else 'unverified'
        )
    )
    journeys = report.get('journeys', [])
    passage_checks = [
        row
        for row in journeys
        if row.get('protocol') == 'rest'
        and row.get('passage_evidence_required')
    ]
    rest_journeys = [row for row in journeys if row.get('protocol') == 'rest']
    passage_query_ids = {row.get('query_id') for row in passage_checks}
    report['passage_retrieval_gate'] = (
        'failed'
        if any(row.get('passage_relevant') is False for row in rest_journeys)
        else (
            'passed'
            if len(rest_journeys) == 6
            and all(
                row.get('passage_relevant') is True for row in rest_journeys
            )
            and len(passage_query_ids - {None}) >= 2
            else 'unverified'
        )
    )
    # Preserve the earlier diagnostic name without allowing paper membership
    # or a wider read to turn failed passage retrieval into a quality pass.
    report['relevance_smoke_gate'] = report['passage_retrieval_gate']
    context_coverage = {}
    for row in journeys:
        if row.get('passage_evidence_required') and row.get('query_id'):
            context_coverage.setdefault(row['query_id'], set()).add(
                row.get('protocol')
            )
    report['answer_context_gate'] = (
        'failed'
        if any(row.get('answer_context_relevant') is False for row in journeys)
        else (
            'passed'
            if len(journeys) == 12
            and all(
                row.get('answer_context_relevant') is True for row in journeys
            )
            and sum(
                protocols == {'rest', 'mcp'}
                for protocols in context_coverage.values()
            )
            >= 2
            else 'unverified'
        )
    )
    by_kind = {}
    latency_failed = False
    for row in rows:
        value = row.get('client_wall_ms')
        if finite_number(value):
            by_kind.setdefault(row['kind'], []).append(value)
            limit = 60000 if row['kind'] == 'compatibility' else 20000
            latency_failed |= value > limit
    report['latency_ms'] = {
        kind: percentiles(values) for kind, values in by_kind.items()
    }
    report['latency_gate'] = (
        'failed'
        if latency_failed
        else 'passed' if report.get('phase_complete') else 'unverified'
    )
    budget = report.get('budget')
    try:
        validate_budget(budget)
        report['budget_gate'] = (
            'failed'
            if report.get('budget_validation_failed')
            else 'passed' if report.get('phase_complete') else 'unverified'
        )
    except ValueError:
        report['budget_gate'] = (
            'failed' if budget is not None else 'unverified'
        )
    role_gates = []
    for role, limit in (('gateway', 8), ('durable_object', 30000)):
        values = [row.get('telemetry', {}).get(role, {}) for row in rows]
        failed = any(
            finite_number(item.get('cpu_ms'))
            and item['cpu_ms'] >= limit
            or item.get('outcome') not in (None, '', 'ok')
            for item in values
        )
        complete = bool(rows) and all(
            not row.get('telemetry_conflict')
            and finite_number(item.get('cpu_ms'))
            and item.get('outcome') == 'ok'
            for row, item in zip(rows, values)
        )
        gate = 'failed' if failed else 'passed' if complete else 'unverified'
        report[role + '_cpu_gate'] = gate
        role_gates.append(gate)
    report['cpu_gate'] = (
        'failed'
        if 'failed' in role_gates
        else 'passed' if set(role_gates) == {'passed'} else 'unverified'
    )
    gates = [report.get(name, 'unverified') for name in GROUPS]
    report['integration_gate'] = (
        'failed'
        if 'failed' in gates
        else 'passed' if set(gates) == {'passed'} else 'unverified'
    )
    report['sample_gate'] = (
        'failed'
        if 'failed' in (report['integration_gate'], report['cpu_gate'])
        else (
            'passed'
            if report['integration_gate'] == report['cpu_gate'] == 'passed'
            else 'unverified'
        )
    )
    report.update(
        runtime_gate='unverified',
        memory_gate='unverified',
        full_corpus_quality_gate='unverified',
        external_agent_evaluation='not_run',
    )


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--origin', required=True)
    parser.add_argument('--manifest', type=Path, required=True)
    parser.add_argument('--expected-manifest-sha', required=True)
    parser.add_argument('--script-name', required=True)
    parser.add_argument(
        '--output', type=Path, default=Path('probe-real-report.json')
    )
    parser.add_argument('--wait-seconds', type=int, default=120)
    parser.add_argument('--local', action='store_true')
    args = parser.parse_args(argv)
    parsed = urllib.parse.urlsplit(args.origin)
    local = args.local and parsed.hostname in ('localhost', '127.0.0.1', '::1')
    if (
        (parsed.scheme != 'https' and not (local and parsed.scheme == 'http'))
        or not parsed.netloc
        or any(
            (parsed.username, parsed.password, parsed.query, parsed.fragment)
        )
        or parsed.path not in ('', '/')
        or not 0 <= args.wait_seconds <= 300
    ):
        parser.error(
            'Use a clean HTTPS origin (or local loopback) and wait 0..300'
        )
    if not os.environ.get('PROBE_TOKEN'):
        parser.error('PROBE_TOKEN is required')
    fixture = load_fixture(args.manifest, args.expected_manifest_sha)
    started = int(time.time() * 1000)
    report = {
        'probe_type': 'real-subset',
        'synthetic': False,
        'scope': 'subset',
        'phase': 'real-integration',
        'origin': args.origin.rstrip('/'),
        'source_sha': os.environ.get('GITHUB_SHA', ''),
        'manifest_source_sha': fixture['manifest']['source_sha'],
        'manifest_sha256': fixture['sha256'],
        'release_id': fixture['manifest']['release_id'],
        'oracle_revision': fixture['manifest'].get('oracle_revision', 1),
        'oracle_note': fixture['manifest'].get('oracle_note'),
        'integration_criterion': (
            'Development answer-context criterion, introduced after observing '
            'local retrieval. Passage retrieval remains a separate diagnostic.'
        ),
        'run_id': str(uuid.uuid4()),
        'script_name': args.script_name,
        'started_ms': started,
        'finished_ms': started,
        'output_path': str(args.output.resolve()),
        'http_attempts': 0,
        'requests': [],
        'phase_complete': False,
        '_deadline': time.monotonic() + LOAD_SECONDS,
        'compatibility_gate': 'unverified',
        'limitations': [
            'Small development subset, not a held-out full-corpus benchmark.',
            'Paper retrieval alone is trivial in this small catalog; '
            'source-backed passage and answer-window checks are separate.',
            'HTTP/MCP contract journey, not an external LLM agent evaluation.',
            'Missing platform CPU remains unverified; wall time is never CPU.',
            'Old synthetic matrix gates are unchanged.',
        ],
    }
    persist(report)
    probe = Probe(report, fixture)
    stage = 'discovery'
    try:
        probe.discover()
        body = probe.request(
            'compatibility_search_guard',
            '/v1/search',
            params={'q': fixture['manifest']['queries'][0]['query']},
            expected_status=503,
        )
        require(
            body.get('error', {}).get('code')
            == 'embedding_compatibility_unverified',
            'Semantic search was not blocked before compatibility',
        )
        report['compatibility_guard_passed'] = True
        stage = 'compatibility'
        probe.compatibility()
        stage = 'journeys'
        probe.journeys()
        stage = 'contracts'
        probe.additional_contracts()
        probe.info()
        stage = 'budget'
        require(
            report['budget']['compatibility_texts'] == 200
            and report['budget']['query_texts'] == 12,
            'Expected 200 compatibility texts and twelve uncached '
            'query embeddings',
        )
        report['phase_complete'] = True
    except (
        ValueError,
        OSError,
        http.client.HTTPException,
        KeyError,
        TypeError,
        IndexError,
    ) as exc:
        report['failure'] = f'{type(exc).__name__}: {exc}'[:500]
        report['failure_stage'] = stage
        if stage == 'compatibility':
            report['compatibility_gate'] = 'failed'
        if stage == 'budget':
            report['budget_validation_failed'] = True
    finally:
        report.pop('_deadline', None)
        summarize(report)
        persist(report)
    if not args.local:
        collect(report, args.wait_seconds)
        summarize(report)
        persist(report)
    print(
        json.dumps(
            {
                name: report[name]
                for name in (
                    *GROUPS,
                    'passage_retrieval_gate',
                    'integration_gate',
                    'cpu_gate',
                    'sample_gate',
                )
            }
        )
    )
    if (
        report['integration_gate'] == 'failed'
        or report['cpu_gate'] == 'failed'
    ):
        return 1
    return 0 if report['integration_gate'] == 'passed' else 2


if __name__ == '__main__':
    raise SystemExit(main())
