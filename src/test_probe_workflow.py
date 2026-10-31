'''Probe dispatch is isolated and its credentials are scoped to API steps.'''

import ast
from pathlib import Path
import re

import pytest
import yaml


ROOT = Path(__file__).resolve().parents[1]


def workflow():
    path = ROOT / '.github/workflows/agent-api.yml'
    return yaml.safe_load(path.read_text())


def evaluate(expression, *, event='workflow_dispatch', ref='refs/heads/main',
             confirmed=False, probe=False, phase='pilot', runtime='worker'):
    '''Evaluate the boolean/string subset used by the actual job predicates.'''
    values = {
        'github.event_name': event, 'github.ref': ref,
        'inputs.production_publish_confirmed': confirmed,
        'inputs.static_probe': probe, 'inputs.do_probe_phase': phase,
        'inputs.probe_runtime': runtime,
    }
    source = re.sub(r'\b(?:github|inputs)\.[a-z_]+\b',
                    lambda match: repr(values[match.group()]), expression)
    source = source.replace('&&', ' and ').replace('||', ' or ')
    source = re.sub(r'!(?!=)', ' not ', source).strip()
    tree = ast.parse(source, mode='eval')
    allowed = (ast.Expression, ast.BoolOp, ast.And, ast.Or, ast.UnaryOp,
               ast.Not, ast.Compare, ast.Eq, ast.NotEq, ast.Constant)
    assert all(isinstance(node, allowed) for node in ast.walk(tree))
    return eval(compile(tree, '<workflow predicate>', 'eval'),
                {'__builtins__': {}})


@pytest.mark.parametrize('outcome,expected', [
    ('success', True), ('failure', True),
    ('cancelled', True), ('skipped', False),
])
def test_worker_probe_cleanup_covers_interrupted_deploy(outcome, expected):
    steps = workflow()['jobs']['static_probe']['steps']
    cleanup = next(step for step in steps
                   if 'cleanup_static_search_probe.py' in step.get('run', '')
                   and '--preflight' not in step['run'])
    expression = cleanup['if'].replace('always()', 'True').replace(
        'steps.deploy.outcome', repr(outcome))
    assert bool(evaluate(expression)) is expected


def test_worker_probe_secrets_are_injected_before_first_deploy():
    steps = workflow()['jobs']['static_probe']['steps']
    setup = next(
        i for i, step in enumerate(steps)
        if step.get('name') == 'Create expiring Worker probe credentials'
    )
    deploy = next(i for i, step in enumerate(steps)
                  if step.get('id') == 'deploy')
    assert setup < deploy
    assert '::add-mask::' in steps[setup]['run']
    assert 'chmod(0o600)' in steps[setup]['run']
    secret_arg = '--secrets-file "$RUNNER_TEMP/worker-probe-secrets.json"'
    assert secret_arg in steps[deploy]['run']
    assert '--var "PROBE_EXPIRES_AT:$PROBE_EXPIRES_AT"' in steps[deploy]['run']
    remove = next(step for step in steps if step.get('name')
                  == 'Remove the temporary Worker probe secret file')
    assert remove['if'] == 'always()'
    uploads = [step for step in steps
               if step.get('uses', '').startswith('actions/upload-artifact@')]
    assert all('secrets.json' not in step['with']['path'] for step in uploads)


def test_probe_is_separate_and_uses_the_shared_cloudflare_lock():
    definition = workflow()
    trigger = definition.get('on', definition.get(True))
    assert 'push' not in trigger
    assert 'publish' not in definition['jobs']
    inputs = trigger['workflow_dispatch']['inputs']
    assert 'production_publish_confirmed' not in inputs
    assert inputs['probe_credentials']['default'] == 'probe_environment'
    concurrency = definition['concurrency']
    assert concurrency['cancel-in-progress'] is False
    assert concurrency['queue'] == 'max'
    expression = concurrency['group'].split('${{', 1)[1].rsplit('}}', 1)[0]
    for phase in ('pilot', 'matrix', 'real', 'full'):
        assert evaluate(expression, probe=True, phase=phase) == 'cloudflare'
    assert evaluate(expression, phase='collect', probe=True) == 'collect'


def test_probe_dependencies_never_receive_cloudflare_secrets():
    for job in workflow()['jobs'].values():
        assert not any('CLOUDFLARE' in name for name in job.get('env', {}))
        for step in job['steps']:
            script = step.get('run', '')
            assert not re.search(
                r'CLOUDFLARE[^\n]*>>[^\n]*GITHUB_ENV', script)
            if any(command in script for command in (
                    'npm ci', 'pip install', 'pytest', 'vitest',
                    'embed_real_search_probe.py --out', 'AutoTokenizer')):
                assert not any('secrets.' in str(value)
                               for value in step.get('env', {}).values())


@pytest.mark.parametrize('choice,repository,probe,expected', [
    ('repository', 'repo-secret', 'probe-secret', 'repo-secret'),
    ('repository', '', 'probe-secret', ''),
    ('probe_environment', 'repo-secret', 'probe-secret', 'probe-secret'),
    ('probe_environment', 'repo-secret', '', ''),
    ('invalid', 'repo-secret', 'probe-secret', ''),
])
def test_selected_secrets_never_fallback(choice, repository, probe, expected):
    for job_name, job in workflow()['jobs'].items():
        for step in job['steps']:
            for name, expression in step.get('env', {}).items():
                if name not in {
                        'CLOUDFLARE_ACCOUNT_ID', 'CLOUDFLARE_API_TOKEN'}:
                    continue
                if job_name == 'publish_retained_api':
                    assert expression == (
                        '${{ secrets.PUBLIC_SEARCH_' + name + ' }}')
                    continue
                values = {
                    'inputs.probe_credentials': choice,
                    'secrets.' + name: repository,
                    'secrets.PROBE_' + name: probe,
                }
                source = expression.removeprefix('${{').removesuffix('}}')
                source = re.sub(
                    r'\b(?:inputs|secrets)\.[A-Za-z_]+\b',
                    lambda match: repr(values[match.group()]), source,
                ).replace('&&', ' and ').replace('||', ' or ').strip()
                assert eval(source, {'__builtins__': {}}) == expected


def test_cpu_packages_use_one_index_per_install():
    assert '--extra-index-url' not in (
        ROOT / 'requirements-real-probe.txt').read_text()
    for job in workflow()['jobs'].values():
        for step in job['steps']:
            script = step.get('run', '')
            if ('pip install' in script
                    and 'requirements-real-probe.txt' in script):
                torch = ('--index-url https://download.pytorch.org/whl/cpu '
                         '-r requirements-torch-probe.txt')
                other = ('--index-url https://pypi.org/simple '
                         '-r requirements-real-probe.txt')
                assert torch in script and other in script


def test_full_phase_requires_the_same_explicit_probe_flags():
    condition = workflow()['jobs']['full_offline_probe']['if']
    assert evaluate(condition, phase='full', probe=True,
                    runtime='durable-object')
    assert not evaluate(condition, phase='full', probe=False,
                        runtime='durable-object')
    assert not evaluate(condition, phase='full', probe=True, runtime='worker')
