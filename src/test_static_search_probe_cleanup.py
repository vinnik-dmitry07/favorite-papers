'''Cleanup touches only one probe and does not expand token permissions.'''

from io import BytesIO
import urllib.error

import pytest

from cleanup_static_search_probe import delete_probe


NAME = 'key-papers-static-probe-39350277748-2'


class Response(BytesIO):
    def __init__(self, status, body):
        super().__init__(body)
        self.status = status


@pytest.fixture(autouse=True)
def credentials(monkeypatch):
    monkeypatch.setenv('CLOUDFLARE_ACCOUNT_ID', 'a' * 32)
    monkeypatch.setenv('CLOUDFLARE_API_TOKEN', 'test-token')


@pytest.mark.parametrize('status,body,expected', [
    (204, b'', 'deleted'),
    (200, b'{"success": true, "errors": []}', 'deleted'),
    (404, b'{"errors": [{"code": 10007}]}', 'already absent'),
    (404, b'{"errors": [{"code": 10090}]}', 'already absent'),
])
def test_only_script_endpoint_is_used(monkeypatch, status, body, expected):
    calls = []

    def exchange(request, **_kwargs):
        calls.append(request)
        return Response(status, body)

    monkeypatch.setattr('cleanup_static_search_probe.urllib.request.urlopen',
                        exchange)
    assert delete_probe(NAME) == expected
    assert len(calls) == 1
    assert calls[0].full_url.endswith('/workers/scripts/' + NAME)
    assert calls[0].get_method() == 'DELETE'
    assert '?' not in calls[0].full_url


@pytest.mark.parametrize('name', [
    'key-papers-api', 'key-papers-static-probe',
    'key-papers-static-probe-1-1/../key-papers-api',
])
def test_production_or_ambiguous_names_never_reach_api(monkeypatch, name):
    def unexpected(*_, **__):
        pytest.fail('Unsafe name reached the API')

    monkeypatch.setattr('cleanup_static_search_probe.urllib.request.urlopen',
                        unexpected)
    with pytest.raises(ValueError, match='run-specific'):
        delete_probe(name)


def test_authentication_error_is_not_treated_as_absence(monkeypatch):
    def denied(request, **_kwargs):
        raise urllib.error.HTTPError(
            request.full_url, 403, 'Forbidden', {},
            BytesIO(b'{"errors": [{"code": 10000}]}'))

    monkeypatch.setattr('cleanup_static_search_probe.urllib.request.urlopen',
                        denied)
    with pytest.raises(ValueError, match='HTTP 403') as error:
        delete_probe(NAME)
    assert 'test-token' not in str(error.value)
    assert 'a' * 32 not in str(error.value)


def test_transient_failure_retries_only_same_probe(monkeypatch):
    calls = []

    def exchange(request, **_kwargs):
        calls.append(request.full_url)
        return Response(503, b'upstream unavailable') if len(calls) == 1 else (
            Response(204, b''))

    monkeypatch.setattr('cleanup_static_search_probe.urllib.request.urlopen',
                        exchange)
    monkeypatch.setattr('cleanup_static_search_probe.time.sleep',
                        lambda _: None)
    assert delete_probe(NAME) == 'deleted'
    assert len(calls) == 2 and len(set(calls)) == 1


@pytest.mark.parametrize('status,body', [
    (404, b'not found'),
    (200, b'{"success": false}'),
])
def test_unrecognized_response_is_not_success(monkeypatch, status, body):
    monkeypatch.setattr('cleanup_static_search_probe.urllib.request.urlopen',
                        lambda *_, **__: Response(status, body))
    with pytest.raises(ValueError):
        delete_probe(NAME)
