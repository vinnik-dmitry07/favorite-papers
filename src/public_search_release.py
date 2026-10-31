'''Check publication controls and recover only our interrupted release.

Code rollback does not rewind Durable Object storage. Runtime activation and
pause records are publication-specific; global ledgers are never restored.
'''

import argparse
import getpass
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tomllib
import urllib.error
import urllib.request

from static_search_do_lifecycle import Cloudflare, checkpoint


LEGACY_VERSION = 'bde6f5d0-1c1c-4d99-807f-0a8f640cd01e'
WORKER_NAME = 'key-papers-search'
PACKED_SHA = (
    '6b9c87883f525a128eb9a48aead5914d9524ba2f7433ff3b14c62b3c0d970b47'
)
SCRIPT = '/workers/scripts/' + WORKER_NAME


def persist(report, path):
    checkpoint(path, report)


def public_origin(origin, preview=False):
    # Setup/control checks need only Python's standard library and gh.
    from smoke_public_search_api import public_origin as checked_origin
    return checked_origin(origin, preview)


def require(value, message):
    if not value:
        raise ValueError(message)


def github(path):
    result = subprocess.run(['gh', 'api', path], capture_output=True,
                            text=True, check=True, timeout=30)
    return json.loads(result.stdout)


def validate_environment(environment, branches):
    policy = environment.get('deployment_branch_policy') or {}
    require(environment.get('name') == 'public-search'
            and policy.get('custom_branch_policies') is True
            and policy.get('protected_branches') is False,
            'public-search must use an explicit main-only branch policy')
    rules = branches.get('branch_policies')
    require(isinstance(rules, list) and len(rules) == 1
            and rules[0].get('name') == 'main'
            and rules[0].get('type', 'branch') == 'branch',
            'Only the main branch, without tag rules, may publish')
    reviewers = [r for r in environment.get('protection_rules', [])
                 if r.get('type') == 'required_reviewers']
    require(len(reviewers) == 1 and reviewers[0].get('reviewers'),
            'public-search needs a required publication reviewer')
    return {'environment': 'public-search', 'main_only': True,
            'required_reviewers': True,
            'prevent_self_review': reviewers[0].get('prevent_self_review'),
            'admin_bypass': environment.get('can_admins_bypass')}


def controls():
    repository = os.environ.get('GITHUB_REPOSITORY')
    require(repository == 'vinnik-dmitry07/favorite-papers',
            'Unexpected publication repository')
    root = f'repos/{repository}/environments/public-search'
    report = validate_environment(
        github(root), github(root + '/deployment-branch-policies'))
    token = os.environ.get('CLOUDFLARE_API_TOKEN', '')
    reviewed = os.environ.get('TOKEN_SCOPE_SHA256', '')
    require(token and re.fullmatch(r'[a-f0-9]{64}', reviewed)
            and hashlib.sha256(token.encode()).hexdigest() == reviewed,
            'Review the dedicated token scope and set the matching '
            'PUBLIC_SEARCH_TOKEN_SCOPE_SHA256 environment variable')
    report['token_scope'] = 'operator-reviewed-matching-credential'
    report['token_scope_machine_verified'] = False
    # The token need not gain token-administration rights merely to read its
    # own policy. Scope review is explicit; capability checks are separate.
    return report


def setup_environment(reviewer, credentials=False, scope_reviewed=False):
    '''Run locally with the repository owner's gh login, never from CI.'''
    require(reviewer and re.fullmatch(r'[a-zA-Z0-9-]{1,39}', reviewer),
            'Specify the exact GitHub login of the publication reviewer')
    require(not credentials or scope_reviewed,
            'Review the token scope before --set-credentials')
    repository = 'vinnik-dmitry07/favorite-papers'
    root = f'repos/{repository}/environments/public-search'
    user = github('users/' + reviewer)
    require(user.get('login', '').lower() == reviewer.lower()
            and isinstance(user.get('id'), int), 'Reviewer identity differs')

    def write(path, payload, method='PUT'):
        result = subprocess.run(
            ['gh', 'api', '-X', method, path, '--input', '-'],
            input=json.dumps(payload), capture_output=True,
            text=True, timeout=30, check=True,
        )
        return json.loads(result.stdout) if result.stdout.strip() else None

    write(root, {'wait_timer': 0, 'prevent_self_review': False,
                 'can_admins_bypass': False,
                 'reviewers': [{'type': 'User', 'id': user['id']}],
                 'deployment_branch_policy': {
                     'protected_branches': False,
                     'custom_branch_policies': True}})
    policies = github(root + '/deployment-branch-policies')['branch_policies']
    main = [p for p in policies if p.get('name') == 'main'
            and p.get('type', 'branch') == 'branch']
    for policy in policies:
        if policy not in main:
            write(root + '/deployment-branch-policies/' + str(policy['id']),
                  {}, 'DELETE')
    if not main:
        write(root + '/deployment-branch-policies',
              {'name': 'main', 'type': 'branch'}, 'POST')
    report = validate_environment(
        github(root), github(root + '/deployment-branch-policies'))
    if credentials:
        account = getpass.getpass('Cloudflare account ID: ').strip()
        token = getpass.getpass('Dedicated token (existing Worker Editor): ')
        require(re.fullmatch(r'[a-fA-F0-9]{32}', account)
                and len(token) >= 20, 'Malformed Cloudflare credentials')
        for name, value in (
                ('PUBLIC_SEARCH_CLOUDFLARE_ACCOUNT_ID', account),
                ('PUBLIC_SEARCH_CLOUDFLARE_API_TOKEN', token)):
            subprocess.run([
                'gh', 'secret', 'set', name, '--env', 'public-search',
                '--repo', repository,
            ], input=value, text=True, check=True, timeout=30)
        fingerprint = hashlib.sha256(token.encode()).hexdigest()
        subprocess.run([
            'gh', 'variable', 'set', 'PUBLIC_SEARCH_TOKEN_SCOPE_SHA256',
            '--env', 'public-search', '--repo', repository,
            '--body', fingerprint,
        ], check=True, timeout=30)
        report['token_scope'] = 'operator-reviewed-matching-credential'
        report['token_scope_machine_verified'] = False
    return report


class ReleaseApi(Cloudflare):
    def write_deployment(self, version):
        # Secret values are versioned and differ per publication. The exact
        # recorded prior version is the only allowed forced rollback target.
        path = SCRIPT + '/deployments?force=true'
        payload = {'strategy': 'percentage',
                   'versions': [{'version_id': version, 'percentage': 100}],
                   'annotations': {'workers/message':
                                   'Recover failed retained API publication'}}
        request = urllib.request.Request(
            f'https://api.cloudflare.com/client/v4/accounts/{self.account}'
            + path, data=json.dumps(payload).encode(), method='POST',
            headers={'authorization': 'Bearer ' + self.token,
                     'content-type': 'application/json'})
        # Do not retry an ambiguous mutation. The caller records uncertainty.
        with urllib.request.urlopen(request, timeout=30) as response:
            body = json.load(response)
        require(body.get('success') is True, 'Rollback API did not confirm')


def current_version(api):
    body = api.request(SCRIPT + '/deployments')['result']
    deployments = body.get('deployments') if isinstance(body, dict) else body
    require(isinstance(deployments, list) and deployments,
            'The current deployment could not be identified')
    versions = deployments[0].get('versions', [])
    require(len(versions) == 1 and versions[0].get('percentage') == 100,
            'Refuse to replace or roll back a split deployment')
    version = versions[0].get('version_id')
    require(isinstance(version, str)
            and re.fullmatch(r'[a-f0-9-]{36}', version),
            'Invalid prior version identity')
    return version


def version_publication(api, version):
    body = api.request(SCRIPT + '/versions/' + version)['result']
    bindings = body.get('resources', {}).get('bindings', [])
    values = {b.get('name'): b.get('text') for b in bindings
              if b.get('type') == 'plain_text'}
    require(values.get('PUBLIC_MANIFEST_SHA') == PACKED_SHA,
            'The deployed version has another corpus')
    publication = values.get('PUBLICATION_ID')
    require(isinstance(publication, str) and publication != 'UNPUBLISHED',
            'The deployed version has no publication identity')
    return publication


def health(origin):
    request = urllib.request.Request(origin + '/health',
                                     headers={'accept': 'application/json'})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def prepare(api, publication):
    config = tomllib.loads((Path(__file__).resolve().parents[1]
                           / 'worker/wrangler.public-search.toml').read_text())
    require(config.get('exports') == {
        'PublicSearch': {'type': 'durable-object', 'storage': 'sqlite'}
    } and not config.get('migrations'),
        'Class lifecycle changes require a new recovery review')
    subdomain = api.request('/workers/subdomain')['result']['subdomain']
    origin = public_origin(f'https://{WORKER_NAME}.{subdomain}.workers.dev')
    previous = current_version(api)
    identity = version_publication(api, previous)
    before = health(origin)
    require(before.get('publication_id') == identity
            and before.get('manifest_sha256') == PACKED_SHA,
            'Previous live identity differs from account metadata')
    require(previous == LEGACY_VERSION
            or before.get('recovery_protocol') == 'publication-v1',
            'Previous runtime has no reviewed state-preservation contract')
    require(identity != publication, 'Publication ID was already deployed')
    return {'schema_version': 1, 'kind': 'public-search-release-recovery',
            'worker': WORKER_NAME, 'origin': origin,
            'publication_id': publication, 'previous_version': previous,
            'previous_publication_id': identity, 'previous_health': before,
            'account_fingerprint': hashlib.sha256(api.account.encode())
            .hexdigest(), 'recovery': 'not_needed',
            'storage_rewind': False, 'global_reservations_preserved': True}


def recover(api, report, publication, probe=health):
    require(report.get('kind') == 'public-search-release-recovery'
            and report.get('worker') == WORKER_NAME
            and report.get('publication_id') == publication
            and report.get('account_fingerprint')
            == hashlib.sha256(api.account.encode()).hexdigest(),
            'Recovery checkpoint belongs to another release or account')
    origin = public_origin(report['origin'])
    current = current_version(api)
    if current != report['previous_version']:
        require(version_publication(api, current) == publication,
                'A later publication owns the Worker; refuse rollback')
        api.write_deployment(report['previous_version'])
    require(current_version(api) == report['previous_version'],
            'Previous version was not restored')
    after = probe(origin)
    require(after.get('publication_id') == report['previous_publication_id']
            and after.get('manifest_sha256') == PACKED_SHA
            and after.get('search_enabled')
            == report['previous_health'].get('search_enabled'),
            'Code rollback did not restore the previous activation state')
    return {**report, 'recovery': 'verified', 'restored_health': after}


def preview_origin(path, name):
    require(re.fullmatch(r'release-[1-9][0-9]*-[1-9][0-9]*', name),
            'Only a run-specific release Preview is allowed')
    body = json.loads(Path(path).read_text())
    preview = body.get('preview', {})
    require(preview.get('name') == name or preview.get('slug') == name,
            'Preview name differs from this run')
    urls = preview.get('urls', [])
    origins = [public_origin(url, preview=True) for url in urls
               if isinstance(url, str) and url.startswith(
                   'https://' + name + '-' + WORKER_NAME + '.')]
    require(len(origins) == 1, 'One run-specific Preview URL is required')
    return origins[0]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=[
        'setup', 'controls', 'prepare', 'recover', 'preview-origin',
    ])
    parser.add_argument('--publication-id')
    parser.add_argument('--report', type=Path, required=True)
    parser.add_argument('--name')
    parser.add_argument('--reviewer')
    parser.add_argument('--set-credentials', action='store_true')
    parser.add_argument('--token-scope-reviewed', action='store_true')
    args = parser.parse_args()
    if args.mode == 'preview-origin':
        print(preview_origin(args.report, args.name))
        return
    if args.mode == 'setup':
        report = setup_environment(args.reviewer, args.set_credentials,
                                   args.token_scope_reviewed)
    elif args.mode == 'controls':
        report = controls()
    elif args.mode == 'prepare':
        report = prepare(ReleaseApi(), args.publication_id)
    else:
        report = json.loads(args.report.read_text())
        report['recovery'] = 'in_progress'
        persist(report, args.report)
        try:
            report = recover(ReleaseApi(), report, args.publication_id)
        except Exception as error:
            report.update(recovery='unverified', error=type(error).__name__
                          + ': ' + str(error))
            persist(report, args.report)
            raise
    persist(report, args.report)
    print(json.dumps(report))


if __name__ == '__main__':
    main()
