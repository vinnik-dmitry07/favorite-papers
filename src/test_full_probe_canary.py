'''The bounded compatibility canary cannot turn malformed output into PASS.'''

import json
from io import BytesIO

import pytest

from build_agent_index import BuildError
from run_full_probe_canary import (
    begin_attempt, budget, compare_batches, normalized, provider_vectors,
    reserve_provider,
)


def plan(count=16, tokens=512):
    return {'inputs': [{'input': str(i), 'token_count': tokens}
                       for i in range(count)]}


def test_budget_counts_batch_repeats_and_rejects_overrun():
    count, tokens, repeats = budget(plan())
    assert (count, tokens, repeats) == (18, 9216, [0, 1])
    with pytest.raises(BuildError):
        budget(plan(31))
    with pytest.raises(BuildError):
        budget(plan(30, 513))


@pytest.mark.parametrize('row', [[], [0.0] * 768, [float('nan')] * 768,
                                  [True] * 768, [float('inf')] * 768])
def test_bad_vectors_are_not_compatibility_evidence(row):
    with pytest.raises(BuildError):
        normalized([row], 1)


def test_batch_comparison_is_not_self_comparison():
    left = normalized([[1.0] + [0.0] * 767, [0.0, 1.0] + [0.0] * 766], 2)
    assert compare_batches(left, list(reversed(left)), [0, 1]) == 1


def test_provider_uses_same_model_pooling_and_keeps_secrets_out_of_result():
    calls = []

    def open_request(request, timeout):
        calls.append((request, timeout))
        return BytesIO(json.dumps({'success': True, 'result': {
            'data': [[2.0] + [0.0] * 767]}}).encode())

    result = provider_vectors(['[MASK]'], {
        'model': '@cf/baai/bge-base-en-v1.5', 'pooling': 'cls',
    }, account='abc123', token='private-test-token', opener=open_request)
    assert result == [[1.0] + [0.0] * 767]
    assert len(calls) == 1
    request, timeout = calls[0]
    assert json.loads(request.data) == {'text': ['[MASK]'], 'pooling': 'cls'}
    assert timeout == 45
    assert request.full_url.endswith('/ai/run/@cf/baai/bge-base-en-v1.5')


def test_provider_rejects_error_envelope_without_retry():
    calls = []

    def open_request(request, timeout):
        calls.append(request)
        return BytesIO(b'{"success":false,"errors":[{"message":"error"}]}')

    with pytest.raises(BuildError, match='did not report success'):
        provider_vectors(['x'], {'model': 'model', 'pooling': 'cls'},
                         account='abc', token='token', opener=open_request)
    assert len(calls) == 1


def test_attempt_reserves_budget_durably_before_request_and_cannot_replay(tmp_path):
    inputs = {**plan(), 'fingerprint': 'bound', 'sha256': 'plan'}
    attempt = begin_attempt(tmp_path, inputs, provider=True)
    reserve_provider(tmp_path, attempt, inputs, list(range(16)))
    saved = json.loads((tmp_path / 'canary-attempt.json').read_text())
    assert saved['status'] == 'PROVIDER_RUNNING'
    assert saved['provider_input_count'] == 16
    assert saved['provider_requests'][0]['status'] == 'RESERVED'
    with pytest.raises(BuildError, match='already exists'):
        begin_attempt(tmp_path, inputs, provider=True)
    reserve_provider(tmp_path, attempt, inputs, list(range(16)))
    with pytest.raises(BuildError, match='budget'):
        reserve_provider(tmp_path, attempt, inputs, [0])
