'''The full-size geometry diagnostic is bounded, isolated, and always removed.'''

import ast
import fnmatch
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tomllib

import pytest
import yaml

from static_search_do_lifecycle import validate_name


ROOT = Path(__file__).resolve().parents[1]


def workflow():
    return yaml.safe_load((ROOT / '.github/workflows/agent-api.yml').read_text())


def geometry_job():
    return workflow()['jobs']['full_geometry_probe']


def steps_by_id():
    return {step['id']: step for step in geometry_job()['steps'] if 'id' in step}


def evaluate(expression, **overrides):
    values = {
        'github.event_name': 'workflow_dispatch', 'github.ref': 'refs/heads/main',
        'inputs.static_probe': True, 'inputs.probe_runtime': 'durable-object',
        'inputs.do_probe_phase': 'geometry', 'inputs.free_plan_confirmed': True,
    }
    values.update(overrides)
    source = re.sub(r'\b(?:github|inputs)\.[a-z_]+\b',
                    lambda match: repr(values[match.group()]), expression)
    source = source.replace('&&', ' and ').replace('||', ' or ').strip()
    tree = ast.parse(source, mode='eval')
    allowed = (ast.Expression, ast.BoolOp, ast.And, ast.Or, ast.Compare,
               ast.Eq, ast.NotEq, ast.Constant)
    assert all(isinstance(node, allowed) for node in ast.walk(tree))
    return eval(compile(tree, '<geometry predicate>', 'eval'), {'__builtins__': {}})


def test_geometry_dispatch_is_explicit_and_exclusive():
    definition = workflow()
    inputs = definition['on']['workflow_dispatch']['inputs']
    assert 'geometry' in inputs['do_probe_phase']['options']
    assert inputs['do_probe_phase']['default'] == 'pilot'
    assert inputs['static_probe']['default'] is False
    assert inputs['free_plan_confirmed']['default'] is False
    assert geometry_job()['needs'] == 'offline'
    selected = [name for name, job in definition['jobs'].items()
                if 'if' in job and evaluate(job['if'])]
    assert selected == ['full_geometry_probe']
    for key, value in (
        ('github.event_name', 'pull_request'), ('inputs.static_probe', False),
        ('inputs.probe_runtime', 'worker'), ('inputs.free_plan_confirmed', False),
        ('inputs.do_probe_phase', 'full'), ('inputs.do_probe_phase', 'real'),
        ('inputs.do_probe_phase', 'pilot'), ('inputs.do_probe_phase', 'collect'),
    ):
        assert not evaluate(geometry_job()['if'], **{key: value})
    expression = definition['concurrency']['group'].split('${{', 1)[1].rsplit('}}', 1)[0]
    assert evaluate(expression) == 'cloudflare'
    assert definition['concurrency']['cancel-in-progress'] is False


def test_geometry_build_has_no_model_downloads_or_full_run_admission():
    job = geometry_job()
    commands = '\n'.join(step.get('run', '') for step in job['steps'])
    assert 'python -m pip install -r requirements-agent.txt numpy==2.3.4' in commands
    assert 'python src/build_full_search_probe.py --out agent_full_probe' in commands
    assert '--out agent_geometry_probe --geometry-fixture --seed 17' in commands
    assert 'npm ci' in commands and 'npm run build:probe' in commands
    for forbidden in ('requirements-real-probe', 'requirements-torch-probe',
                      'embed_real_search_probe.py', 'preflight_full_search_probe.py',
                      'run_full_probe_canary.py', 'AutoTokenizer', 'AutoModel',
                      'publish_agent_index.py', 'gh workflow run',
                      '--config wrangler.toml', 'full_run_confirmed'):
        assert forbidden not in commands
    assert job['timeout-minutes'] <= 20
    assert job['timeout-minutes'] >= sum(
        step.get('timeout-minutes', 0) for step in job['steps']) + 3
    offline_commands = '\n'.join(step.get('run', '')
                                 for step in workflow()['jobs']['offline']['steps'])
    assert 'src/test_geometry_probe_workflow.py' in offline_commands
    assert 'src/test_run_full_geometry_probe.py' in offline_commands
    assert 'python src/pack_full_search_probe.py' not in offline_commands


def test_geometry_configuration_has_no_ai_or_persistent_search_service():
    config = tomllib.loads((ROOT / 'worker/wrangler.geometry-probe.toml').read_text())
    assert config['main'] == 'src/full-geometry-do-probe-entry.ts'
    assert config['assets']['directory'] == '../agent_geometry_probe'
    assert config['assets']['run_worker_first'] is True
    assert config['durable_objects']['bindings'] == [
        {'name': 'SEARCH_PROBE', 'class_name': 'StaticSearchProbe'}]
    assert config['exports']['StaticSearchProbe'] == {
        'type': 'durable-object', 'storage': 'sqlite'}
    assert not {'ai', 'r2_buckets', 'vectorize', 'routes', 'route'} & config.keys()


def test_geometry_changes_cannot_trigger_production_push():
    publish = yaml.safe_load((ROOT / '.github/workflows/agent-publish.yml').read_text())
    patterns = publish['on']['push']['paths']
    assert 'push' not in workflow()['on']
    for path in ('worker/src/full-geometry-do-probe.ts',
                 'worker/src/full-geometry-do-probe-entry.ts',
                 'worker/src/full-geometry-do-probe.test.ts',
                 'worker/wrangler.geometry-probe.toml',
                 'src/run_full_geometry_probe.py',
                 'src/test_run_full_geometry_probe.py',
                 'src/test_geometry_probe_workflow.py',
                 '.github/workflows/agent-api.yml'):
        included = False
        for pattern in patterns:
            excluded = pattern.startswith('!')
            if fnmatch.fnmatchcase(path, pattern[1:] if excluded else pattern):
                included = not excluded
        assert not included, path


@pytest.mark.parametrize('confirmed,choice,account,token,passes', [
    ('true', 'repository', 'account', 'token', True),
    ('true', 'probe_environment', 'account', 'token', True),
    ('false', 'repository', 'account', 'token', False),
    ('true', 'invalid', 'account', 'token', False),
    ('true', 'repository', '', 'token', False),
    ('true', 'probe_environment', 'account', '', False),
])
def test_geometry_controls_fail_closed(confirmed, choice, account, token, passes):
    result = subprocess.run(
        ['bash', '-e', '-c', steps_by_id()['controls']['run']],
        env={**os.environ, 'FREE_PLAN_CONFIRMED': confirmed,
             'PROBE_CREDENTIALS': choice, 'CLOUDFLARE_ACCOUNT_ID': account,
             'CLOUDFLARE_API_TOKEN': token}, capture_output=True, text=True)
    assert (result.returncode == 0) is passes, result.stderr


def test_lifecycle_and_authentication_precede_bounded_geometry_requests():
    steps = geometry_job()['steps']
    ids = [step['id'] for step in steps if 'id' in step]
    ordered = ['controls', 'geometry_fixture', 'preflight', 'deploy',
               'capture', 'measure', 'cleanup']
    assert [ids.index(name) for name in ordered] == sorted(ids.index(name) for name in ordered)
    name = geometry_job()['env']['PROBE_NAME'].replace(
        '${{ github.run_id }}', '123').replace('${{ github.run_attempt }}', '1')
    assert validate_name(name) == name
    auth = next(step for step in steps if 'secrets.token_urlsafe' in step.get('run', ''))
    assert steps.index(auth) < steps.index(steps_by_id()['deploy'])
    assert "Path('agent_geometry_probe/probe.json')" in auth['run']
    assert 'hashlib.sha256(manifest.read_bytes()).hexdigest()' in auth['run']
    assert 'timedelta(minutes=15)' in auth['run']
    assert '::add-mask::' in auth['run'] and 'chmod(0o600)' in auth['run']
    deploy = steps_by_id()['deploy']['run']
    assert '--config wrangler.geometry-probe.toml --name "$PROBE_NAME"' in deploy
    assert '--secrets-file "$RUNNER_TEMP/geometry-probe-secrets.json"' in deploy
    assert '--var "PROBE_EXPIRES_AT:$PROBE_EXPIRES_AT"' in deploy
    assert '--var "PROBE_MANIFEST_SHA:$PROBE_MANIFEST_SHA"' in deploy
    measure = steps_by_id()['measure']['run']
    assert '--base-url "$PROBE_ORIGIN" --token-env PROBE_TOKEN' in measure
    assert '--max-load-seconds 300 --wait-seconds 90' in measure
    assert '--out full-geometry-reports/run.json' in measure


@pytest.mark.parametrize('outcome,cleanup_runs', [
    ('success', True), ('failure', True), ('cancelled', True), ('skipped', False),
])
def test_cleanup_survives_failed_and_cancelled_deployment(outcome, cleanup_runs):
    cleanup = steps_by_id()['cleanup']
    expression = cleanup['if'].replace('always()', 'True').replace(
        'steps.deploy.outcome', repr(outcome))
    assert bool(evaluate(expression)) is cleanup_runs
    assert 'static_search_do_lifecycle.py cleanup "$PROBE_NAME"' in cleanup['run']
    upload = next(step for step in geometry_job()['steps']
                  if step.get('uses', '').startswith('actions/upload-artifact'))
    assert upload['if'] == 'always()'
    for expected in ('full-geometry-reports/', 'agent_geometry_probe/probe.json',
                     'agent_full_probe/probe.json', 'probe-do-lifecycle.json',
                     'probe-do-cleanup.txt'):
        assert expected in upload['with']['path']
    assert 'secret' not in upload['with']['path']
    assert 'RUNNER_TEMP' not in upload['with']['path']
    remove = next(step for step in geometry_job()['steps']
                  if step.get('run', '').startswith('rm -f'))
    assert remove['if'] == 'always()'


@pytest.mark.parametrize('field,value,passes', [
    ('gateway_cpu_gate', 'unverified', True), ('do_cpu_gate', 'failed', False),
    ('do_cpu_gate', None, False), ('functional_gate', 'failed', False),
    ('workload_complete', False, False), ('namespace_absent', False, False),
    ('cleanup', 'failed', False),
])
def test_final_status_retains_runtime_failures_and_cleanup_proof(tmp_path, field, value, passes):
    report = {'functional_gate': 'passed', 'workload_complete': True,
              'gateway_cpu_gate': 'passed', 'do_cpu_gate': 'passed',
              'memory_gate': 'unverified', 'production_readiness': 'unverified'}
    lifecycle = {'cleanup': 'passed', 'namespace_absent': True}
    (lifecycle if field in lifecycle else report)[field] = value
    reports = tmp_path / 'full-geometry-reports'
    reports.mkdir()
    (reports / 'run.json').write_text(json.dumps(report))
    (tmp_path / 'probe-do-lifecycle.json').write_text(json.dumps(lifecycle))
    script = geometry_job()['steps'][-1]['run']
    python = script.split("<<'PYTHON'\n", 1)[1].rsplit('\nPYTHON', 1)[0]
    result = subprocess.run([sys.executable, '-c', python], cwd=tmp_path,
                            capture_output=True, text=True)
    assert (result.returncode == 0) is passes, result.stdout + result.stderr
    assert '96 MiB full-run admission gate' in result.stdout
    assert 'production_readiness: unverified' in result.stdout


def test_geometry_shell_and_embedded_python_parse_without_credentials():
    for step in geometry_job()['steps']:
        script = step.get('run', '')
        if script:
            subprocess.run(['bash', '-n'], input=script, text=True, check=True)
            for python in re.findall(r"<<'PYTHON'\n(.*?)\nPYTHON", script, re.S):
                ast.parse(python)
