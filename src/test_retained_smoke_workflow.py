'''The retained full-corpus smoke is short, manual, isolated, and always removed.'''

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
from test_geometry_probe_workflow import evaluate


ROOT = Path(__file__).resolve().parents[1]


def workflow():
    return yaml.safe_load((ROOT / '.github/workflows/agent-api.yml').read_text())


def job():
    return workflow()['jobs']['retained_full_smoke']


def steps():
    return {step['id']: step for step in job()['steps'] if 'id' in step}


def test_retained_requires_explicit_manual_free_account_and_probe_flags():
    definition = workflow()
    inputs = definition['on']['workflow_dispatch']['inputs']
    assert 'push' not in definition['on']
    assert 'retained' in inputs['do_probe_phase']['options']
    assert inputs['do_probe_phase']['default'] == 'pilot'
    assert inputs['static_probe']['default'] is False
    assert inputs['free_plan_confirmed']['default'] is False
    values = {'inputs.do_probe_phase': 'retained'}
    selected = [name for name, value in definition['jobs'].items()
                if 'if' in value and evaluate(value['if'], **values)]
    assert selected == ['retained_full_smoke']
    for key, value in (
        ('github.event_name', 'push'), ('github.event_name', 'pull_request'),
        ('inputs.static_probe', False), ('inputs.probe_runtime', 'worker'),
        ('inputs.free_plan_confirmed', False), ('inputs.do_probe_phase', 'pilot'),
        ('inputs.do_probe_phase', 'full'), ('inputs.do_probe_phase', 'geometry'),
    ):
        assert not evaluate(job()['if'], **{**values, key: value})
    expression = definition['concurrency']['group'].split('${{', 1)[1].rsplit('}}', 1)[0]
    assert evaluate(expression, **values) == 'cloudflare'
    assert definition['concurrency']['cancel-in-progress'] is False


def test_retained_reuses_pinned_artifact_with_no_model_or_production_work():
    commands = '\n'.join(step.get('run', '') for step in job()['steps'])
    assert 'actions/runs/40448979121' in commands
    assert 'actions/artifacts/12715563729/zip' in commands
    assert 'python src/restore_full_search_artifact.py' in commands
    assert '--out full-probe-reports/replay' in commands
    assert 'load_fixture(\'full-probe-reports/replay\')' in commands
    assert 'python -m pip install -r requirements-agent.txt numpy==2.3.4' in commands
    for forbidden in ('requirements-real-probe', 'requirements-torch-probe',
                      'embed_real_search_probe.py', 'AutoTokenizer', 'AutoModel',
                      'evaluate_full_search_probe.py', 'run_real_search_probe.py',
                      'publish_agent_index.py', '--config wrangler.toml',
                      'full_run_confirmed', 'gh workflow run'):
        assert forbidden not in commands
    assert 20 <= job()['timeout-minutes'] <= 30
    assert job()['needs'] == 'offline'
    offline = '\n'.join(step.get('run', '') for step in workflow()['jobs']['offline']['steps'])
    assert 'src/test_retained_search_smoke.py' in offline
    assert 'src/test_retained_smoke_workflow.py' in offline
    assert 'src/run_retained_search_smoke.py --origin' not in offline


def test_lifecycle_authentication_and_report_cover_failure_and_cancel():
    selected = steps()
    order = ['controls', 'restore', 'preflight', 'deploy', 'capture', 'measure', 'cleanup']
    assert [list(selected).index(name) for name in order] == sorted(list(selected).index(name) for name in order)
    name = job()['env']['PROBE_NAME'].replace('${{ github.run_id }}', '123').replace(
        '${{ github.run_attempt }}', '1')
    assert validate_name(name) == name
    credentials = [step['env'] for step in selected.values()
                   if 'CLOUDFLARE_ACCOUNT_ID' in step.get('env', {})]
    assert len(credentials) == 5
    for credential in credentials[1:]:
        assert credential['CLOUDFLARE_ACCOUNT_ID'] == credentials[0]['CLOUDFLARE_ACCOUNT_ID']
        assert credential['CLOUDFLARE_API_TOKEN'] == credentials[0]['CLOUDFLARE_API_TOKEN']
    assert 'CLOUDFLARE_API_TOKEN' not in selected['measure'].get('env', {})
    auth = next(step for step in job()['steps'] if 'secrets.token_urlsafe' in step.get('run', ''))
    assert 'timedelta(minutes=15)' in auth['run'] and '::add-mask::' in auth['run']
    assert 'chmod(0o600)' in auth['run']
    deploy = selected['deploy']['run']
    assert '--config wrangler.full-real-probe.toml --name "$PROBE_NAME"' in deploy
    assert '--secrets-file "$RUNNER_TEMP/retained-probe-secrets.json"' in deploy
    assert '--var "PROBE_EXPIRES_AT:$PROBE_EXPIRES_AT"' in deploy
    assert '--authorize-query-submissions 2' in selected['measure']['run']
    assert selected['measure']['continue-on-error'] is True
    for outcome in ('success', 'failure', 'cancelled', 'skipped'):
        expression = selected['cleanup']['if'].replace('always()', 'True').replace(
            'steps.deploy.outcome', repr(outcome))
        assert bool(evaluate(expression)) is (outcome != 'skipped')
    upload = next(step for step in job()['steps']
                  if step.get('uses', '').startswith('actions/upload-artifact'))
    assert upload['if'] == 'always()'
    for expected in ('retained-smoke-reports/', 'restoration.json',
                     'probe-do-lifecycle.json', 'probe-do-cleanup.txt'):
        assert expected in upload['with']['path']
    assert 'secret' not in upload['with']['path'] and 'RUNNER_TEMP' not in upload['with']['path']
    remove = next(step for step in job()['steps'] if step.get('run', '').startswith('rm -f'))
    assert remove['if'] == 'always()'


def test_full_genuine_config_and_no_production_push_trigger():
    config = tomllib.loads((ROOT / 'worker/wrangler.full-real-probe.toml').read_text())
    assert config['main'] == 'src/full-real-search-do-probe-entry.ts'
    assert config['assets']['directory'] == '../full-probe-reports/replay/runtime'
    assert config['assets']['run_worker_first'] is True
    assert config['vars']['PROBE_CORPUS_MODE'] == 'full'
    assert config['vars']['PROBE_MANIFEST_SHA'] == '6b9c87883f525a128eb9a48aead5914d9524ba2f7433ff3b14c62b3c0d970b47'
    assert config['ai'] == {'binding': 'AI'}
    assert not {'r2_buckets', 'vectorize', 'route', 'routes'} & config.keys()
    publish = yaml.safe_load((ROOT / '.github/workflows/agent-publish.yml').read_text())
    for path in ('worker/wrangler.full-real-probe.toml',
                 'worker/src/full-real-search-do-probe-entry.ts',
                 'worker/src/real-search-do-probe.ts',
                 'src/run_retained_search_smoke.py', '.github/workflows/agent-api.yml'):
        included = False
        for pattern in publish['on']['push']['paths']:
            excluded = pattern.startswith('!')
            if fnmatch.fnmatchcase(path, pattern[1:] if excluded else pattern):
                included = not excluded
        assert not included, path


def test_embedded_shell_and_python_parse_without_credentials():
    for step in job()['steps']:
        script = step.get('run', '')
        if script:
            subprocess.run(['bash', '-n'], input=script, text=True, check=True)
            for code in re.findall(r'<<\'PYTHON\'\n(.*?)\nPYTHON', script, re.S):
                ast.parse(code)


@pytest.mark.parametrize('confirmed,choice,account,token,passes', [
    ('true', 'repository', 'account', 'token', True),
    ('true', 'probe_environment', 'account', 'token', True),
    ('false', 'repository', 'account', 'token', False),
    ('true', 'invalid', 'account', 'token', False),
    ('true', 'repository', '', 'token', False),
    ('true', 'probe_environment', 'account', '', False),
])
def test_selected_credentials_and_free_account_fail_closed(confirmed, choice, account, token, passes):
    result = subprocess.run(
        ['bash', '-e', '-c', steps()['controls']['run']],
        env={**os.environ, 'FREE_PLAN_CONFIRMED': confirmed,
             'PROBE_CREDENTIALS': choice, 'CLOUDFLARE_ACCOUNT_ID': account,
             'CLOUDFLARE_API_TOKEN': token}, capture_output=True, text=True)
    assert (result.returncode == 0) is passes


@pytest.mark.parametrize('field,value,passes', [
    ('smoke_gate', 'passed', True), ('smoke_gate', 'failed', False),
    ('workload_complete', False, False), ('query_texts', 3, False),
    ('cleanup', 'failed', False), ('namespace_absent', False, False),
])
def test_final_status_requires_exact_smoke_and_verified_cleanup(tmp_path, field, value, passes):
    report = {'smoke_gate': 'passed', 'workload_complete': True, 'budget': {'query_texts': 2}}
    lifecycle = {'cleanup': 'passed', 'namespace_absent': True}
    if field == 'query_texts':
        report['budget'][field] = value
    else:
        (lifecycle if field in lifecycle else report)[field] = value
    reports = tmp_path / 'retained-smoke-reports'
    reports.mkdir()
    (reports / 'run.json').write_text(json.dumps(report))
    (tmp_path / 'probe-do-lifecycle.json').write_text(json.dumps(lifecycle))
    script = job()['steps'][-1]['run']
    code = script.split('<<\'PYTHON\'\n', 1)[1].rsplit('\nPYTHON', 1)[0]
    result = subprocess.run([sys.executable, '-c', code], cwd=tmp_path,
                            capture_output=True, text=True)
    assert (result.returncode == 0) is passes, result.stdout + result.stderr
    assert 'not an autonomous-agent evaluation or a held-out quality test' in result.stdout
