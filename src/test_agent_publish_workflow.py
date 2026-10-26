'''Production publication is an explicit manual action, never a merge effect.'''

import ast
import fnmatch
from pathlib import Path
import re

import pytest
import yaml


ROOT = Path(__file__).resolve().parents[1]


def workflow():
    return yaml.safe_load((ROOT / '.github/workflows/agent-api.yml').read_text())


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
    return eval(compile(tree, '<workflow predicate>', 'eval'), {'__builtins__': {}})


@pytest.mark.parametrize('context,allowed', [
    ({'event': 'push'}, False),
    ({'event': 'push', 'confirmed': True}, False),
    ({'event': 'pull_request', 'confirmed': True}, False),
    ({}, False),
    ({'confirmed': True}, True),
    ({'confirmed': True, 'ref': 'refs/heads/feat/static-search-probe'}, False),
    ({'confirmed': True, 'probe': True}, False),
    ({'confirmed': True, 'phase': 'matrix'}, False),
    ({'confirmed': True, 'phase': 'real'}, False),
    ({'confirmed': True, 'phase': 'collect'}, False),
    ({'confirmed': True, 'phase': 'full'}, False),
])
def test_actual_publish_condition_requires_unambiguous_manual_main(context, allowed):
    assert bool(evaluate(workflow()['jobs']['publish']['if'], **context)) is allowed


def test_production_opt_in_defaults_off_and_probe_jobs_reject_it():
    definition = workflow()
    trigger = definition.get('on', definition.get(True))
    setting = trigger['workflow_dispatch']['inputs']['production_publish_confirmed']
    assert setting['type'] == 'boolean' and setting['default'] is False
    for name, phase, runtime in (
        ('static_probe', 'pilot', 'worker'),
        ('static_do_probe', 'pilot', 'durable-object'),
        ('static_real_probe', 'real', 'durable-object'),
        ('static_do_collect', 'collect', 'durable-object'),
        ('full_offline_probe', 'full', 'durable-object'),
    ):
        condition = definition['jobs'][name]['if']
        assert evaluate(condition, probe=True, phase=phase, runtime=runtime)
        assert not evaluate(condition, confirmed=True, probe=True,
                            phase=phase, runtime=runtime)


@pytest.mark.parametrize('path', [
    'src/build_fulltext_search.py',
    'src/write_discovery_links.py',
    'requirements-agent.txt',
    '.github/workflows/agent-api.yml',
])
def test_build_dependencies_trigger_offline_main_checks(path):
    definition = workflow()
    trigger = definition.get('on', definition.get(True))
    for event in ('push', 'pull_request'):
        patterns = trigger[event]['paths']
        assert any(fnmatch.fnmatchcase(path, item)
                   for item in patterns if not item.startswith('!'))
    assert 'if' not in definition['jobs']['offline']
    assert not evaluate(definition['jobs']['publish']['if'], event='push')


@pytest.mark.parametrize('outcome,expected', [
    ('success', True), ('failure', True),
    ('cancelled', True), ('skipped', False),
])
def test_worker_probe_cleanup_covers_interrupted_deploy(outcome, expected):
    steps = workflow()['jobs']['static_probe']['steps']
    cleanup = next(step for step in steps if step.get('run', '').startswith(
        'python src/cleanup_static_search_probe.py'))
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


def test_shared_cloudflare_account_work_is_serialized_without_cancellation():
    definition = workflow()['concurrency']
    assert definition['cancel-in-progress'] is False
    assert definition['queue'] == 'max'
    expression = definition['group'].split('${{', 1)[1].rsplit('}}', 1)[0]
    for phase in ('pilot', 'matrix', 'real', 'full'):
        assert evaluate(expression, probe=True, phase=phase) == 'cloudflare'
    assert evaluate(expression, confirmed=True) == 'cloudflare'
    assert evaluate(expression, phase='collect', probe=True) == 'collect'
    assert evaluate(expression, event='push') == 'validate-main'
    assert evaluate(expression, event='pull_request',
                    ref='refs/pull/2/merge') == 'refs/pull/2/merge'
