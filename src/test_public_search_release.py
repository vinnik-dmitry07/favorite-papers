'''A failed candidate must not mutate a later release or refund usage.'''

import hashlib
import io
import json
import os
import shutil
import subprocess
import sys
from types import SimpleNamespace

import pytest

import public_search_release as release


def test_release_identity_matches_the_publication_validator():
    import smoke_public_search_api as smoke
    assert release.PACKED_SHA == smoke.PACKED_SHA
    assert release.WORKER_NAME == smoke.WORKER_NAME


PREVIOUS = release.LEGACY_VERSION
CURRENT = 'bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb'
ORIGIN = 'https://key-papers-search.example.workers.dev'


class FakeCloudflare:
    account = 'a' * 32

    def __init__(self, identity='new-publication', current=CURRENT):
        self.current = current
        self.identity = identity
        self.writes = []

    def request(self, path):
        if path.endswith('/deployments'):
            return {'result': {'deployments': [{'versions': [
                {'version_id': self.current, 'percentage': 100}]}]}}
        if '/versions/' in path:
            return {'result': {'resources': {'bindings': [
                {'name': 'PUBLIC_MANIFEST_SHA', 'type': 'plain_text',
                 'text': release.PACKED_SHA},
                {'name': 'PUBLICATION_ID', 'type': 'plain_text',
                 'text': self.identity},
            ]}}}
        raise AssertionError(path)

    def write_deployment(self, version):
        self.writes.append(version)
        self.current = version


def checkpoint():
    return {
        'kind': 'public-search-release-recovery',
        'worker': release.WORKER_NAME, 'origin': ORIGIN,
        'publication_id': 'new-publication', 'previous_version': PREVIOUS,
        'previous_publication_id': 'old-publication',
        'previous_health': {'search_enabled': True},
        'account_fingerprint': hashlib.sha256(b'a' * 32).hexdigest(),
        'storage_rewind': False, 'global_reservations_preserved': True,
    }


def old_health(origin):
    assert origin == ORIGIN
    return {'publication_id': 'old-publication', 'search_enabled': True,
            'manifest_sha256': release.PACKED_SHA}


def health_transport(monkeypatch, status, text):
    import run_retained_search_smoke as smoke
    calls = []

    def open_response(request, timeout):
        calls.append(request)
        assert request.full_url == ORIGIN + '/health'
        assert request.get_method() == 'GET' and request.data is None
        assert request.get_header('User-agent') == smoke.PROBE_USER_AGENT
        assert request.get_header('Authorization') is None
        assert request.get_header('X-publication-token') is None
        assert timeout == 30
        body = io.BytesIO(text.encode())
        headers = {'content-type': 'application/json'}
        if status != 200:
            raise release.urllib.error.HTTPError(
                request.full_url, status, 'rejected', headers, body)
        body.status = status
        body.headers = headers
        return body

    def build(*handlers):
        assert len(handlers) == 1
        assert isinstance(handlers[0], smoke.NoRedirect)
        return SimpleNamespace(open=open_response)

    monkeypatch.setattr(smoke.urllib.request, 'build_opener', build)
    monkeypatch.setattr(smoke.urllib.request, 'urlopen', lambda *a, **kw:
                        pytest.fail('Health must use the shared smoke client'))
    return calls


def test_health_uses_project_identity_without_admin_credentials(monkeypatch):
    expected = old_health(ORIGIN)
    calls = health_transport(monkeypatch, 200, json.dumps(expected))
    assert release.health(ORIGIN) == expected
    assert len(calls) == 1


@pytest.mark.parametrize('status', [302, 403, 503])
def test_health_rejects_http_errors_without_retry_or_redirect(
        monkeypatch, status):
    calls = health_transport(monkeypatch, status,
                             json.dumps(old_health(ORIGIN)))
    with pytest.raises(ValueError, match=f'HTTP {status}'):
        release.health(ORIGIN)
    assert len(calls) == 1


@pytest.mark.parametrize('text', ['not-json', '[]'])
def test_health_requires_a_json_object(monkeypatch, text):
    calls = health_transport(monkeypatch, 200, text)
    with pytest.raises(ValueError):
        release.health(ORIGIN)
    assert len(calls) == 1


def test_exact_previous_version_and_activation_are_recovered():
    api = FakeCloudflare()
    report = release.recover(api, checkpoint(), 'new-publication', old_health)
    assert report['recovery'] == 'verified'
    assert report['storage_rewind'] is False
    assert report['global_reservations_preserved'] is True
    assert api.writes == [PREVIOUS]


def test_rollback_applies_the_recorded_version_to_active_objects_immediately(
        monkeypatch):
    monkeypatch.setenv('CLOUDFLARE_ACCOUNT_ID', 'a' * 32)
    monkeypatch.setenv('CLOUDFLARE_API_TOKEN', 'test-release-api-token')
    calls = []

    def open_response(request, timeout):
        calls.append(request)
        assert request.full_url.endswith(
            '/workers/scripts/key-papers-search/deployments?force=true')
        assert request.get_method() == 'POST' and timeout == 30
        body = json.loads(request.data)
        assert body['strategy'] == 'percentage'
        assert body['versions'] == [
            {'version_id': PREVIOUS, 'percentage': 100}]
        assert body['code_update_strategy'] == {'mode': 'immediate'}
        return io.BytesIO(b'{"success": true}')

    monkeypatch.setattr(release.urllib.request, 'urlopen', open_response)
    release.ReleaseApi().write_deployment(PREVIOUS)
    assert len(calls) == 1


def test_already_recovered_or_failed_before_deploy_requires_no_mutation():
    api = FakeCloudflare(current=PREVIOUS)
    assert release.recover(
        api, checkpoint(), 'new-publication', old_health,
    )['recovery'] == 'verified'
    assert not api.writes


def test_later_release_is_never_rolled_back():
    api = FakeCloudflare(identity='another-publication')
    with pytest.raises(ValueError, match='later publication'):
        release.recover(api, checkpoint(), 'new-publication', old_health)
    assert not api.writes


def test_failed_health_verification_never_claims_restoration():
    api = FakeCloudflare()
    with pytest.raises(ValueError, match='activation state'):
        release.recover(api, checkpoint(), 'new-publication',
                        lambda _: {**old_health(ORIGIN),
                                   'search_enabled': False})
    assert api.writes == [PREVIOUS]


@pytest.mark.parametrize('field,value', [
    ('worker', 'key-papers-api'), ('publication_id', 'other'),
    ('account_fingerprint', 'other'),
])
def test_checkpoint_cannot_target_another_account_or_service(field, value):
    api = FakeCloudflare()
    with pytest.raises(ValueError, match='another release or account'):
        release.recover(api, {**checkpoint(), field: value},
                        'new-publication', old_health)
    assert not api.writes


def environment():
    return {'name': 'public-search', 'deployment_branch_policy': {
        'protected_branches': False, 'custom_branch_policies': True,
    }, 'protection_rules': [{'type': 'required_reviewers',
                            'reviewers': [{'type': 'User',
                                           'reviewer': {'id': 24797359}}]}]}


def branches(name='main', kind='branch'):
    return {'branch_policies': [{'name': name, 'type': kind}]}


def test_actual_environment_requires_review_and_only_main():
    assert release.validate_environment(environment(), branches())['main_only']
    for name, kind in [('feat/*', 'branch'), ('main', 'tag'), ('*', 'branch')]:
        with pytest.raises(ValueError, match='Only the main'):
            release.validate_environment(environment(), branches(name, kind))
    with pytest.raises(ValueError, match='reviewer'):
        release.validate_environment({**environment(), 'protection_rules': []},
                                     branches())
    with pytest.raises(ValueError, match='Only the main'):
        release.validate_environment(environment(), {'branch_policies': [
            *branches()['branch_policies'], {'name': '*', 'type': 'tag'}]})


def test_missing_fingerprint_or_rotated_credential_stops_publication(
        monkeypatch):
    monkeypatch.setenv('GITHUB_REPOSITORY',
                       'vinnik-dmitry07/favorite-papers')
    monkeypatch.setenv('CLOUDFLARE_API_TOKEN', 'dedicated-token')
    monkeypatch.setattr(release, 'github', lambda path: branches()
                        if path.endswith('deployment-branch-policies')
                        else environment())
    with pytest.raises(ValueError, match='configured credential'):
        release.controls()
    monkeypatch.setenv('TOKEN_SCOPE_SHA256', hashlib.sha256(
        b'dedicated-token').hexdigest())
    report = release.controls()
    assert report['token_scope_machine_verified'] is False
    assert report['token_scope'] == 'unverified'
    assert report['credential_identity'] == 'fingerprint-matched'
    monkeypatch.setenv('CLOUDFLARE_API_TOKEN', 'rotated-token')
    with pytest.raises(ValueError, match='configured credential'):
        release.controls()


def preview_record():
    name = 'release-123-1'
    origin = f'https://{name}-key-papers-search.example.workers.dev'
    return {'type': 'preview', 'version': 1,
            'worker_name': release.WORKER_NAME,
            'preview_name': name, 'preview_slug': name,
            'preview_urls': [origin], 'deployment_id': 'test-deployment'}


def test_preview_receipt_cannot_redirect_credentials_to_a_foreign_origin(
        tmp_path):
    path = tmp_path / 'preview.ndjson'
    name = 'release-123-1'
    row = preview_record()
    origin = row['preview_urls'][0]
    path.write_text(json.dumps(row) + '\n')
    assert release.preview_origin(path, name) == origin
    for url in [ORIGIN, 'https://attacker.example', origin + '/path']:
        path.write_text(json.dumps({**row, 'preview_urls': [url]}) + '\n')
        with pytest.raises(ValueError):
            release.preview_origin(path, name)


@pytest.mark.parametrize('changes', [
    {'version': 2}, {'worker_name': 'key-papers-api'},
    {'preview_name': 'release-456-1'}, {'preview_urls': 'not-a-list'},
])
def test_preview_receipt_requires_the_expected_schema_worker_and_run(
        tmp_path, changes):
    path = tmp_path / 'preview.ndjson'
    path.write_text(json.dumps({**preview_record(), **changes}) + '\n')
    with pytest.raises(ValueError):
        release.preview_origin(path, 'release-123-1')


@pytest.mark.parametrize('mode', [
    'empty', 'session-only', 'duplicate', 'failed', 'non-object', 'truncated',
])
def test_preview_receipt_rejects_missing_ambiguous_or_failed_output(
        tmp_path, mode):
    row = preview_record()
    session = {'type': 'wrangler-session', 'version': 1}
    records = {
        'empty': [], 'session-only': [session], 'duplicate': [row, row],
        'failed': [row, {'type': 'command-failed'}],
        'non-object': [[]], 'truncated': [row],
    }[mode]
    text = '\n'.join(json.dumps(value) for value in records)
    if mode == 'truncated':
        text += '\n{'
    path = tmp_path / 'preview.ndjson'
    path.write_text(text)
    with pytest.raises(ValueError):
        release.preview_origin(path, 'release-123-1')


@pytest.mark.parametrize('mode', [
    'success', 'nonzero', 'missing', 'malformed', 'wrong-worker',
])
def test_actual_preview_workflow_consumes_machine_output_not_stdout(
        tmp_path, mode):
    from test_public_search_publication import ROOT, job
    step = next(value for value in job()['steps']
                if value.get('id') == 'preview_deploy')
    checkout = tmp_path / 'checkout'
    shutil.copytree(ROOT / 'src', checkout / 'src',
                    ignore=shutil.ignore_patterns('__pycache__'))
    worker = checkout / 'worker'
    worker.mkdir()
    reports = checkout / 'public-api-reports'
    reports.mkdir()
    runner = tmp_path / 'runner'
    runner.mkdir()
    output = runner / 'github-output'
    output.touch()
    commands = tmp_path / 'bin'
    commands.mkdir()
    fake_npx = commands / 'npx'
    fake_npx.write_text('#!' + sys.executable + '\n' + '''
import os
from pathlib import Path
import sys

print('Building list of assets...')
print('Starting asset upload...')
print('{"deployment": {"secret": "must-stay-private"}}')
path = os.environ.get('WRANGLER_OUTPUT_FILE_PATH')
if path:
    with Path(path).open('a') as output:
        output.write(os.environ['FAKE_WRANGLER_OUTPUT'])
sys.exit(int(os.environ['FAKE_WRANGLER_EXIT']))
''')
    fake_npx.chmod(0o755)
    row = preview_record()
    if mode == 'wrong-worker':
        row['worker_name'] = 'key-papers-api'
    records = [{'type': 'wrangler-session', 'version': 1}]
    if mode != 'missing':
        records.append(row)
    text = '\n'.join(json.dumps(value) for value in records) + '\n'
    if mode == 'malformed':
        text += '{'
    # Wrangler appends records: a previous attempt must not be reused.
    (runner / 'public-search-preview.ndjson').write_text(json.dumps(row))
    env = {**os.environ,
           'PATH': str(commands) + os.pathsep + os.environ['PATH'],
           'RUNNER_TEMP': str(runner), 'GITHUB_OUTPUT': str(output),
           'PREVIEW_NAME': 'release-123-1',
           'PUBLIC_WORKER_NAME': release.WORKER_NAME,
           'PUBLICATION_ID': 'test-publication',
           'PREVIEW_EXPIRES_AT': '2026-11-01T21:00:00Z',
           'FAKE_WRANGLER_OUTPUT': text,
           'FAKE_WRANGLER_EXIT': '23' if mode == 'nonzero' else '0'}
    result = subprocess.run(
        ['bash', '-c', step['run']], cwd=worker, env=env,
        capture_output=True, text=True, timeout=30,
    )
    report = reports / 'preview.json'
    if mode != 'success':
        assert result.returncode != 0
        if mode == 'nonzero':
            assert result.returncode == 23
        assert output.read_text() == ''
        assert not report.exists()
        return
    assert result.returncode == 0, result.stderr
    assert output.read_text() == 'origin=' + row['preview_urls'][0] + '\n'
    assert json.loads(report.read_text()) == {
        'name': row['preview_name'], 'slug': row['preview_slug'],
        'urls': row['preview_urls'], 'origin': row['preview_urls'][0],
    }
    assert 'must-stay-private' not in report.read_text() + result.stdout


@pytest.mark.parametrize('scope_reviewed', [False, True])
def test_owner_setup_removes_wildcard_rules_and_keeps_secrets_out_of_argv(
        monkeypatch, scope_reviewed):
    token = 'dedicated-private-token-value'
    calls = []
    reads = 0

    def github(path):
        nonlocal reads
        if path.startswith('users/'):
            return {'login': 'vinnik-dmitry07', 'id': 24797359}
        if path.endswith('deployment-branch-policies'):
            reads += 1
            rows = [{'name': 'main', 'type': 'branch', 'id': 1}]
            if reads == 1:
                rows.append({'name': '*', 'type': 'tag', 'id': 2})
            return {'branch_policies': rows}
        return environment()

    def run(args, **kwargs):
        calls.append((args, kwargs))
        return SimpleNamespace(stdout='{}')

    prompts = iter(['a' * 32, token])
    monkeypatch.setattr(release, 'github', github)
    monkeypatch.setattr(release.subprocess, 'run', run)
    monkeypatch.setattr(release.getpass, 'getpass', lambda _: next(prompts))
    report = release.setup_environment(
        'vinnik-dmitry07', True, scope_reviewed,
    )
    assert report['main_only'] is True
    assert report['token_scope_machine_verified'] is False
    assert report['token_scope'] == 'unverified'
    assert any('DELETE' in args and args[-3].endswith('/2')
               for args, _ in calls)
    assert all(token not in str(args) for args, _ in calls)
    secrets = [(args, kw) for args, kw in calls if 'secret' in args]
    assert len(secrets) == 2
    assert secrets[1][1]['input'] == token
    assert token not in json.dumps(report)


def test_release_workflow_checks_candidate_and_recovers_after_partial_deploy():
    from test_public_search_publication import job
    steps = job()['steps']
    ids = {step['id']: step for step in steps if step.get('id')}
    order = list(ids)
    assert (order.index('checkpoint') < order.index('preview_deploy')
            < order.index('preview_smoke') < order.index('preview_cleanup')
            < order.index('deploy') < order.index('smoke')
            < order.index('deactivate') < order.index('recover'))
    assert '--ignore-base-config' in ids['preview_deploy']['run']
    assert '--preview' in ids['preview_smoke']['run']
    cleanup = ids['preview_cleanup']
    assert '--worker-name "$PUBLIC_WORKER_NAME"' in cleanup['run']
    assert 'always()' in ids['recover']['if']
    assert 'steps.deploy.outputs.origin' not in ids['recover']['if']
    assert "steps.deploy.outcome == 'cancelled'" in ids['recover']['if']
    assert "steps.preview_deploy.outcome == 'cancelled'" in cleanup['if']
    identity = next(step for step in steps
                    if 'controls --report' in step.get('run', ''))
    assert identity['env']['TOKEN_SCOPE_SHA256'] == (
        '${{ vars.PUBLIC_SEARCH_TOKEN_SCOPE_SHA256 }}')
    assert 'CREDENTIALS_REVIEWED_SHA256' not in identity['env']
