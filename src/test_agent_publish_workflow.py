'''Production publishing is explicit and independent of probe workloads.'''

import ast
import fnmatch
from pathlib import Path
import re

import pytest
import yaml


ROOT = Path(__file__).resolve().parents[1]


def workflow():
    path = ROOT / '.github/workflows/agent-publish.yml'
    return yaml.safe_load(path.read_text())


def evaluate(expression, *, event='workflow_dispatch', ref='refs/heads/main',
             confirmed=False):
    values = {
        'github.event_name': event, 'github.ref': ref,
        'inputs.production_publish_confirmed': confirmed,
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


@pytest.mark.parametrize('context,allowed', [
    ({'event': 'push'}, False),
    ({'event': 'push', 'confirmed': True}, False),
    ({'event': 'pull_request', 'confirmed': True}, False),
    ({}, False), ({'confirmed': True}, True),
    ({'confirmed': True, 'ref': 'refs/heads/feature'}, False),
])
def test_publish_requires_explicit_manual_main(context, allowed):
    condition = workflow()['jobs']['publish']['if']
    assert bool(evaluate(condition, **context)) is allowed


def test_production_workflow_has_no_experiment_inputs_or_jobs():
    definition = workflow()
    trigger = definition.get('on', definition.get(True))
    inputs = trigger['workflow_dispatch']['inputs']
    assert set(inputs) == {'production_publish_confirmed'}
    assert inputs['production_publish_confirmed']['default'] is False
    assert set(definition['jobs']) == {'offline', 'publish'}
    assert definition['jobs']['publish']['needs'] == 'offline'
    commands = '\n'.join(step.get('run', '')
                         for step in definition['jobs']['offline']['steps'])
    for forbidden in ('build:probe', 'build_static_search_probe',
                      'build_real_search_probe', 'wrangler.do-probe',
                      'test_full_search', 'test_static_search', 'npm test'):
        assert forbidden not in commands
    assert 'tsconfig.production.json' in commands
    assert 'src/api.test.ts' in commands


@pytest.mark.parametrize('path', [
    'src/build_fulltext_search.py', 'src/write_discovery_links.py',
    'requirements-agent.txt', '.github/workflows/agent-publish.yml',
])
def test_build_dependencies_trigger_offline_main_checks(path):
    definition = workflow()
    trigger = definition.get('on', definition.get(True))
    for event in ('push', 'pull_request'):
        assert any(fnmatch.fnmatchcase(path, item)
                   for item in trigger[event]['paths'])
    assert not evaluate(definition['jobs']['publish']['if'], event='push')


def test_production_install_and_test_steps_never_receive_cloudflare_secrets():
    for job in workflow()['jobs'].values():
        assert not any('CLOUDFLARE' in name for name in job.get('env', {}))
        for step in job['steps']:
            script = step.get('run', '')
            if any(command in script for command in (
                    'npm ci', 'pip install', 'pytest', 'vitest', 'tsc')):
                assert not any('secrets.' in str(value)
                               for value in step.get('env', {}).values())


def test_manual_production_uses_shared_cloudflare_lock():
    concurrency = workflow()['concurrency']
    assert concurrency['cancel-in-progress'] is False
    assert concurrency['queue'] == 'max'
    expression = concurrency['group'].split('${{', 1)[1].rsplit('}}', 1)[0]
    assert evaluate(expression) == 'cloudflare'
    assert evaluate(expression, event='push') == 'validate-production'
