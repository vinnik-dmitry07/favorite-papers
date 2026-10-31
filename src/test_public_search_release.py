'''A failed candidate must not mutate a later release or refund usage.'''

import hashlib
import json
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


def test_exact_previous_version_and_activation_are_recovered():
    api = FakeCloudflare()
    report = release.recover(api, checkpoint(), 'new-publication', old_health)
    assert report['recovery'] == 'verified'
    assert report['storage_rewind'] is False
    assert report['global_reservations_preserved'] is True
    assert api.writes == [PREVIOUS]


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


def test_unreviewed_or_rotated_credential_stops_publication(monkeypatch):
    monkeypatch.setenv('GITHUB_REPOSITORY',
                       'vinnik-dmitry07/favorite-papers')
    monkeypatch.setenv('CLOUDFLARE_API_TOKEN', 'dedicated-token')
    monkeypatch.setattr(release, 'github', lambda path: branches()
                        if path.endswith('deployment-branch-policies')
                        else environment())
    with pytest.raises(ValueError, match='dedicated token scope'):
        release.controls()
    monkeypatch.setenv('TOKEN_SCOPE_SHA256', hashlib.sha256(
        b'dedicated-token').hexdigest())
    report = release.controls()
    assert report['token_scope_machine_verified'] is False
    monkeypatch.setenv('CLOUDFLARE_API_TOKEN', 'rotated-token')
    with pytest.raises(ValueError, match='dedicated token scope'):
        release.controls()


def test_preview_receipt_cannot_redirect_credentials_to_a_foreign_origin(
        tmp_path):
    path = tmp_path / 'preview.json'
    name = 'release-123-1'
    origin = f'https://{name}-key-papers-search.example.workers.dev'
    path.write_text(json.dumps({'preview': {'name': name, 'urls': [origin]}}))
    assert release.preview_origin(path, name) == origin
    for url in [ORIGIN, 'https://attacker.example', origin + '/path']:
        path.write_text(json.dumps({'preview': {'name': name, 'urls': [url]}}))
        with pytest.raises(ValueError):
            release.preview_origin(path, name)


def test_owner_setup_removes_wildcard_rules_and_keeps_secrets_out_of_argv(
        monkeypatch):
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
    report = release.setup_environment('vinnik-dmitry07', True, True)
    assert report['main_only'] is True
    assert report['token_scope_machine_verified'] is False
    assert any('DELETE' in args and args[-3].endswith('/2')
               for args, _ in calls)
    assert all(token not in str(args) for args, _ in calls)
    secrets = [(args, kw) for args, kw in calls if 'secret' in args]
    assert len(secrets) == 2
    assert secrets[1][1]['input'] == token
    assert token not in json.dumps(report)


def test_credential_setup_requires_explicit_scope_review_before_any_mutation(
        monkeypatch):
    monkeypatch.setattr(release, 'github', lambda _: pytest.fail(
        'No API access before the scope-review requirement'))
    with pytest.raises(ValueError, match='Review the token scope'):
        release.setup_environment('vinnik-dmitry07', True, False)


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
