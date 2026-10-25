'''Contract oracles and bounded workload regressions for the real probe.'''

import base64
import hashlib
import json
import time

import pytest

import run_real_search_probe as probe


def fixture():
    text = '😀 preface critic baseline 64 and KL coefficient 0.04. End.'
    row = {
        'paper_id': 'arxiv:2402.03300',
        'chunk_index': 0,
        'start': 10,
        'end': 50,
        'content_hash': 'hash',
        'input_hash': 'input',
        'token_count': 8,
    }
    paper = {
        'paper_id': row['paper_id'],
        'text': text,
        'chunks': [
            {
                'index': 0,
                **{
                    key: row[key]
                    for key in (
                        'start',
                        'end',
                        'content_hash',
                        'input_hash',
                        'token_count',
                    )
                },
            }
        ],
    }
    return {
        'sha256': 'a' * 64,
        'manifest': {
            'release_id': 'b' * 64,
            'paper_ids': [row['paper_id']],
            'compatibility_indices': list(range(200)),
            'source_sha': 's',
        },
        'papers': {row['paper_id']: paper},
        'by_chunk': {(row['paper_id'], 0): row},
        'graph': {
            'nodes': {
                row['paper_id']: {
                    'id': row['paper_id'],
                    'title': 'Paper',
                    'url': 'https://arxiv.org/abs/2402.03300',
                }
            },
            'out': {row['paper_id']: []},
            'in': {row['paper_id']: []},
        },
    }


def hit(value):
    row = next(iter(value['by_chunk'].values()))
    paper = value['papers'][row['paper_id']]
    return {
        'paper_id': row['paper_id'],
        'chunk_index': row['chunk_index'],
        'start': row['start'],
        'end': row['end'],
        'score': 0.5,
        'corpus_version': value['manifest']['release_id'],
        'snippet': paper['text'][row['start'] : row['end']][:480],
        'url': value['graph']['nodes'][row['paper_id']]['url'],
        'content': '/v1/content?id=arxiv%3A2402.03300&offset=10&version='
        + 'b' * 64,
    }


def test_rest_oracle_uses_code_points_and_exact_content_link():
    value = fixture()
    body = {'corpus_version': 'b' * 64, 'hits': [hit(value)]}
    probe.validate_rest_search(body, value)
    body['hits'][0]['snippet'] = value['papers']['arxiv:2402.03300']['text'][
        9:49
    ]
    with pytest.raises(ValueError, match='Snippet'):
        probe.validate_rest_search(body, value)


@pytest.mark.parametrize(
    'link',
    [
        'https://elsewhere.example/v1/content',
        '//elsewhere.example/v1/content',
        '/v1/content?id=other&offset=10&version=' + 'b' * 64,
    ],
)
def test_untrusted_search_links_cannot_redirect_authenticated_requests(link):
    value = fixture()
    row = hit(value)
    row['content'] = link
    with pytest.raises(ValueError, match='link'):
        probe.validate_rest_search(
            {'corpus_version': 'b' * 64, 'hits': [row]}, value
        )


def test_content_oracle_rejects_utf16_offset():
    value = fixture()
    text = value['papers']['arxiv:2402.03300']['text']
    body = {
        'corpus_version': 'b' * 64,
        'paper_id': 'arxiv:2402.03300',
        'available': True,
        'offset': 1,
        'total_length': len(text),
        'next_offset': 6,
        'text': text[1:6],
    }
    probe.validate_content(body, value, 'arxiv:2402.03300', 1, 5)
    body['text'] = text[:5]
    with pytest.raises(ValueError, match='Content'):
        probe.validate_content(body, value, 'arxiv:2402.03300', 1, 5)


def document_id(paper='arxiv:2402.03300', version='b' * 64, start=0):
    raw = json.dumps(
        {'paper': paper, 'version': version, 'start': start}
    ).encode()
    return 'doc:' + base64.urlsafe_b64encode(raw).decode().rstrip('=')


def test_fetch_must_match_copied_search_id_and_canonical_text():
    value = fixture()
    text = value['papers']['arxiv:2402.03300']['text']
    key = document_id()
    body = {
        'id': key,
        'text': text,
        'url': 'https://arxiv.org/abs/2402.03300',
        'metadata': {
            'paper_id': 'arxiv:2402.03300',
            'corpus_version': 'b' * 64,
            'item_type': 'text_part',
            'start': 0,
            'end': len(text),
            'total_length': len(text),
        },
    }
    probe.validate_fetch(body, value, key)
    body['id'] = document_id(version='c' * 64)
    with pytest.raises(ValueError, match='MCP fetch'):
        probe.validate_fetch(body, value, key)


def test_paper_membership_is_not_passage_evidence():
    value = fixture()
    row = hit(value)
    query = {
        'expected_paper_id': row['paper_id'],
        'required_passage_terms': ['critic', 'baseline'],
    }
    assert probe.passage_relevant(row, query, value)
    row['start'], row['end'] = 0, 5
    assert not probe.passage_relevant(row, query, value)


def test_evidence_requires_all_terms_and_one_complete_alternative():
    query = {
        'required_passage_terms': ['baseline'],
        'passage_evidence_any': [
            ['critic', 'group'],
            ['value function', 'average reward', 'multiple sampled outputs'],
        ],
    }
    assert probe.text_supports_evidence('critic GROUP baseline', query)
    assert probe.text_supports_evidence(
        'The baseline uses average reward of multiple sampled outputs '
        'instead of a value function.',
        query,
    )
    assert not probe.text_supports_evidence('critic group', query)
    assert not probe.text_supports_evidence('baseline value function', query)


def test_answer_evidence_outside_returned_window_cannot_pass():
    query = {'required_passage_terms': ['0.04', '64']}
    source = 'irrelevant returned window. Later: KL 0.04 and 64 outputs.'
    assert probe.text_supports_evidence(source, query)
    assert not probe.text_supports_evidence(source[:27], query)


@pytest.mark.parametrize(
    'answer_offset, context_passes', [(1000, True), (7000, False)]
)
def test_journey_distinguishes_passage_and_actual_read_evidence(
    answer_offset, context_passes, monkeypatch
):
    value = fixture()
    paper_id = 'arxiv:2402.03300'
    text = '😀 ' + 'x' * 10000
    text = (
        text[:answer_offset]
        + ' 64 outputs and KL 0.04. '
        + text[answer_offset:]
    )
    value['papers'][paper_id]['text'] = text
    value['manifest']['queries'] = [
        {
            'id': f'q{i}',
            'query': f'Natural question {i}',
            'expected_paper_id': paper_id,
            'required_passage_terms': ['0.04', '64'] if i < 2 else [],
        }
        for i in range(6)
    ]
    content_lengths = []

    class StubProbe(probe.Probe):
        def request(self, kind, path, params=None, **kwargs):
            if kind == 'rest_search':
                return {'corpus_version': 'b' * 64, 'hits': [hit(value)]}
            assert kind == 'content'
            content_lengths.append(params['length'])
            start, end = params['offset'], params['offset'] + params['length']
            return {
                'paper_id': paper_id,
                'corpus_version': 'b' * 64,
                'available': True,
                'offset': start,
                'total_length': len(text),
                'next_offset': end if end < len(text) else None,
                'text': text[start:end],
            }

        def call(self, tool, args, kind=None):
            key = document_id()
            source_url = value['graph']['nodes'][paper_id]['url']
            if tool == 'search':
                return {
                    'results': [
                        {'id': key, 'title': 'Paper', 'url': source_url}
                    ]
                }
            assert tool == 'fetch' and args == {'id': key}
            return {
                'id': key,
                'url': source_url,
                'text': text,
                'metadata': {
                    'paper_id': paper_id,
                    'corpus_version': 'b' * 64,
                    'item_type': 'text_part',
                    'start': 0,
                    'end': len(text),
                    'total_length': len(text),
                },
            }

    monkeypatch.setattr(probe, 'persist', lambda *_: None)
    report_value = {}
    StubProbe(report_value, value).journeys()
    assert content_lengths == [6000] * 6
    rest, mcp = report_value['journeys'][:2]
    assert rest['passage_relevant'] is False
    assert rest['answer_context_relevant'] is context_passes
    assert rest['context_start'] == 10 and rest['context_end'] == 6010
    assert mcp['answer_context_relevant'] is True
    assert mcp['document_id'] == document_id()


def compatibility(checked=200, status='passed', cosine=1.0):
    return {
        'checked': checked,
        'expected': 200,
        'threshold': 0.999,
        'status': status,
        'min_cosine': cosine if checked else None,
        'results': [
            {'index': index, 'cosine': cosine, 'remote_norm': 1.0}
            for index in range(checked)
        ],
    }


@pytest.mark.parametrize(
    'change',
    [
        {'checked': 199},
        {'min_cosine': 0.998},
        {'expected': 199},
        {'threshold': 0.9},
        {'results': []},
    ],
)
def test_incomplete_or_inconsistent_compatibility_cannot_pass(change):
    body = compatibility()
    body.update(change)
    with pytest.raises(ValueError):
        probe.validate_compatibility(body, fixture())


def test_compatibility_validates_all_cosines_and_row_identity():
    body = compatibility()
    assert probe.validate_compatibility(body, fixture()) == 'passed'
    body['results'][3]['cosine'] = 0.98
    body['min_cosine'] = 0.98
    with pytest.raises(ValueError, match='incompatible'):
        probe.validate_compatibility(body, fixture())
    body = compatibility()
    body['results'][3]['index'] = 2
    with pytest.raises(ValueError, match='different canonical'):
        probe.validate_compatibility(body, fixture())


def budget(compat=200, queries=12):
    return {
        'compatibility_texts': compat,
        'query_texts': queries,
        'total_texts': compat + queries,
        'input_tokens': 1000,
        'ai_calls': 13 + queries,
        'limits': {
            'total_texts': 300,
            'query_texts': 24,
            'input_tokens': 153600,
        },
    }


def test_budget_bounds_and_monotonicity():
    probe.validate_budget(budget())
    with pytest.raises(ValueError, match='budget'):
        probe.validate_budget(budget(queries=25))
    with pytest.raises(ValueError, match='backwards'):
        probe.validate_budget(budget(queries=11), budget())


def report(tmp_path=None):
    value = {
        'http_attempts': 0,
        '_deadline': time.monotonic() + 60,
        'requests': [],
        'origin': 'https://probe.workers.dev',
        'run_id': 'run',
        'started_ms': 1,
        'finished_ms': 1,
    }
    if tmp_path:
        value['output_path'] = str(tmp_path / 'report.json')
    return value


def headers(row, value):
    return {
        'x-probe-runtime': 'durable-object',
        'x-probe-kind': 'real-subset',
        'x-probe-synthetic': 'false',
        'x-probe-marker': row['marker'],
        'x-probe-manifest-sha256': value['sha256'],
        'x-probe-object-id': 'object',
        'x-probe-boot-id': 'boot',
    }


def test_request_budget_is_checked_before_network(monkeypatch):
    value = report()
    value['http_attempts'] = 60
    monkeypatch.setattr(
        probe, 'exchange', lambda *_a, **_k: pytest.fail('network called')
    )
    with pytest.raises(ValueError, match='budget'):
        probe.Probe(value, fixture()).request('info', '/probe/info')


def test_transport_failure_preserves_intent_and_does_not_leak_token(
    tmp_path, monkeypatch
):
    value = report(tmp_path)
    monkeypatch.setenv('PROBE_TOKEN', 'never-serialize-this')

    def timeout(*_args, **_kwargs):
        saved = json.loads((tmp_path / 'report.json').read_text())
        assert saved['requests'][0]['state'] == 'in_flight'
        assert saved['http_attempts'] == 1
        raise TimeoutError('network deadline')

    monkeypatch.setattr(probe, 'exchange', timeout)
    with pytest.raises(ValueError, match='TimeoutError'):
        probe.Probe(value, fixture()).request('info', '/probe/info')
    saved = (tmp_path / 'report.json').read_text()
    assert 'never-serialize-this' not in saved
    assert json.loads(saved)['requests'][0]['state'] == 'complete'


def test_expected_error_response_still_requires_probe_identity(monkeypatch):
    value = report()
    local = fixture()

    def respond(*_args, **_kwargs):
        return (
            409,
            headers(value['requests'][-1], local),
            json.dumps({'error': {'code': 'version_conflict'}}),
        )

    monkeypatch.setattr(probe, 'exchange', respond)
    body = probe.Probe(value, local).request(
        'stale', '/v1/content', expected_status=409
    )
    assert body['error']['code'] == 'version_conflict'
    assert value['requests'][0]['success']


def test_discovery_retries_only_unidentified_provider_failure(monkeypatch):
    value = report()
    local = fixture()
    calls = []

    def info(self):
        calls.append(1)
        row = {'success': False, 'status': 404}
        self.report['requests'].append(row)
        if len(calls) == 1:
            raise ValueError('propagation')
        return {'ok': True}

    monkeypatch.setattr(probe.Probe, 'info', info)
    monkeypatch.setattr(probe.time, 'sleep', lambda *_: None)
    assert probe.Probe(value, local).discover() == {'ok': True}
    assert value['requests'][0]['startup_retry'] is True
    calls.clear()
    value = report()

    def identified(self):
        self.report['requests'].append(
            {'success': False, 'status': 503, 'object_id': 'object'}
        )
        raise ValueError('identified failure')

    monkeypatch.setattr(probe.Probe, 'info', identified)
    with pytest.raises(ValueError, match='identified'):
        probe.Probe(value, local).discover()
    assert len(value['requests']) == 1


def passed_integration_report():
    return {
        'requests': [
            {
                'marker': 'one',
                'kind': 'rest_search',
                'mode': 'integration',
                'success': True,
                'client_wall_ms': 20,
            }
        ],
        'journeys': [
            {
                'query_id': f'q{i // 2}',
                'protocol': 'rest' if i % 2 == 0 else 'mcp',
                'relevant': True,
                'passage_relevant': True if i % 2 == 0 else None,
                'answer_context_relevant': True,
                'passage_evidence_required': i < 4,
            }
            for i in range(12)
        ],
        'phase_complete': True,
        'compatibility_gate': 'passed',
        'graph_contracts_passed': True,
        'error_contracts_passed': True,
        'unicode_contract_passed': True,
        'budget': budget(),
    }


def test_integration_completion_does_not_invent_cpu_or_full_quality():
    value = passed_integration_report()
    probe.summarize(value)
    assert value['integration_gate'] == 'passed'
    assert value['cpu_gate'] == value['sample_gate'] == 'unverified'
    assert value['full_corpus_quality_gate'] == 'unverified'
    assert value['external_agent_evaluation'] == 'not_run'


def test_observed_cpu_failure_fails_even_with_other_missing_records():
    value = passed_integration_report()
    value['requests'][0]['telemetry'] = {
        'gateway': {'cpu_ms': 8, 'outcome': 'ok'}
    }
    probe.summarize(value)
    assert value['integration_gate'] == 'passed'
    assert value['cpu_gate'] == value['sample_gate'] == 'failed'


def test_paper_only_smoke_cannot_pass():
    value = passed_integration_report()
    for row in value['journeys']:
        row['passage_evidence_required'] = False
    probe.summarize(value)
    assert value['relevance_smoke_gate'] == 'unverified'
    assert value['integration_gate'] == 'unverified'


def test_passage_oracle_failure_is_not_hidden_by_other_queries():
    value = passed_integration_report()
    value['journeys'][0]['relevant'] = False
    value['journeys'][0]['passage_relevant'] = False
    probe.summarize(value)
    assert value['relevance_smoke_gate'] == 'failed'
    assert value['passage_retrieval_gate'] == 'failed'
    assert value['answer_context_gate'] == 'passed'
    assert value['integration_gate'] == 'passed'


def test_missing_answer_evidence_fails_even_if_passage_diagnostic_passes():
    value = passed_integration_report()
    value['journeys'][1]['answer_context_relevant'] = False
    probe.summarize(value)
    assert value['passage_retrieval_gate'] == 'passed'
    assert value['answer_context_gate'] == 'failed'
    assert value['integration_gate'] == 'failed'


def test_answer_context_requires_two_distinct_queries_in_both_protocols():
    value = passed_integration_report()
    value['journeys'][3]['passage_evidence_required'] = False
    probe.summarize(value)
    assert value['passage_retrieval_gate'] == 'passed'
    assert value['answer_context_gate'] == 'unverified'
    assert value['integration_gate'] == 'unverified'


def write_fixture(tmp_path):
    value = fixture()
    paper_id = 'arxiv:2402.03300'
    text = value['papers'][paper_id]['text']
    content_hash = hashlib.sha256(text.encode()).hexdigest()
    chunks = [
        {
            'index': i,
            'start': 0,
            'end': len(text),
            'token_count': 8,
            'content_hash': content_hash,
            'input_hash': f'input-{i}',
        }
        for i in range(200)
    ]
    paper = {'paper_id': paper_id, 'text': text, 'chunks': chunks}
    graph = value['graph']
    release = 'b' * 64
    files = {}
    paper_key = hashlib.sha256(paper_id.encode()).hexdigest()
    for name, body in {
        f'releases/{release}/graph.json': graph,
        f'releases/{release}/papers/{paper_key}.json': paper,
    }.items():
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(body))
        files[name] = hashlib.sha256(path.read_bytes()).hexdigest()
    vectors = tmp_path / 'vectors.f32'
    vectors.write_bytes(bytes(200 * 768 * 4))
    files['vectors.f32'] = hashlib.sha256(vectors.read_bytes()).hexdigest()
    manifest = {
        'kind': 'real-subset',
        'synthetic': False,
        'schema_version': 1,
        'passage_count': 200,
        'dimensions': 768,
        'release_id': release,
        'paper_ids': [paper_id],
        'files': files,
        'embeddings': {
            'model_revision': probe.MODEL_REVISION,
            'pooling': 'cls',
            'normalization': 'l2',
            'dtype': 'float32',
            'byte_order': 'little',
            'path': 'vectors.f32',
            'sha256': files['vectors.f32'],
        },
        'compatibility_indices': list(range(200)),
        'rows': [
            {
                'paper_id': paper_id,
                'chunk_index': chunk['index'],
                **{k: v for k, v in chunk.items() if k != 'index'},
            }
            for chunk in chunks
        ],
        'queries': [
            {
                'id': f'q{i}',
                'query': f'Natural source question {i}',
                'expected_paper_id': paper_id,
                'required_passage_terms': (
                    ['critic', 'baseline'] if i < 2 else []
                ),
            }
            for i in range(6)
        ],
    }
    path = tmp_path / 'probe.json'
    path.write_text(json.dumps(manifest))
    return path


def test_fixture_checks_exact_manifest_and_source_assets(tmp_path):
    path = write_fixture(tmp_path)
    checksum = hashlib.sha256(path.read_bytes()).hexdigest()
    assert len(probe.load_fixture(path, checksum)['by_chunk']) == 200
    with pytest.raises(ValueError, match='manifest hash'):
        probe.load_fixture(path, '0' * 64)
    vector = tmp_path / 'vectors.f32'
    vector.write_bytes(b'broken')
    with pytest.raises(ValueError, match='Asset hash'):
        probe.load_fixture(path, checksum)


def test_fixture_rejects_an_unverifiable_passage_oracle(tmp_path):
    path = write_fixture(tmp_path)
    manifest = json.loads(path.read_text())
    manifest['queries'][0]['required_passage_terms'] = [
        'not in the canonical source'
    ]
    path.write_text(json.dumps(manifest))
    with pytest.raises(ValueError, match='no supporting canonical'):
        probe.load_fixture(path, hashlib.sha256(path.read_bytes()).hexdigest())


@pytest.mark.parametrize('alternatives', [['critic'], [[]], [[42]]])
def test_fixture_rejects_invalid_evidence_alternatives(tmp_path, alternatives):
    path = write_fixture(tmp_path)
    manifest = json.loads(path.read_text())
    manifest['queries'][0]['passage_evidence_any'] = alternatives
    path.write_text(json.dumps(manifest))
    with pytest.raises(ValueError, match='evidence alternatives'):
        probe.load_fixture(path, hashlib.sha256(path.read_bytes()).hexdigest())


def test_fixture_rejects_unsupported_evidence_alternative(tmp_path):
    path = write_fixture(tmp_path)
    manifest = json.loads(path.read_text())
    manifest['queries'][0]['passage_evidence_any'] = [['unknown concept']]
    path.write_text(json.dumps(manifest))
    with pytest.raises(ValueError, match='no supporting canonical'):
        probe.load_fixture(path, hashlib.sha256(path.read_bytes()).hexdigest())


def test_fixture_rejects_paths_outside_asset_directory(tmp_path):
    path = write_fixture(tmp_path)
    manifest = json.loads(path.read_text())
    manifest['files']['../outside.json'] = 'a' * 64
    path.write_text(json.dumps(manifest))
    with pytest.raises(ValueError, match='Unsafe asset'):
        probe.load_fixture(path, hashlib.sha256(path.read_bytes()).hexdigest())


def test_failed_compatibility_does_not_claim_contracts_were_tested():
    value = report()
    value.update(
        compatibility_gate='failed',
        failure='incompatible vectors',
        failure_stage='compatibility',
    )
    probe.summarize(value)
    assert value['compatibility_gate'] == 'failed'
    assert value['contracts_gate'] == 'unverified'
    assert value['integration_gate'] == 'failed'
