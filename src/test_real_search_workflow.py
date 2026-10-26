'''The real integration job cannot deploy production or skip owned cleanup.'''

import ast
import fnmatch
import json
from pathlib import Path
import subprocess
import sys

import pytest
import yaml


ROOT = Path(__file__).resolve().parents[1]


def workflow():
    return yaml.safe_load((ROOT / '.github/workflows/agent-api.yml').read_text())


def matches_path(path, patterns):
    matched = False
    for pattern in patterns:
        excluded = pattern.startswith('!')
        if fnmatch.fnmatchcase(path, pattern[1:] if excluded else pattern):
            matched = not excluded
    return matched


def test_real_dispatch_does_not_run_another_deployment():
    jobs = workflow()['jobs']
    assert 'publish' not in jobs
    for name in ('static_probe', 'static_do_probe'):
        assert "inputs.do_probe_phase != 'real'" in jobs[name]['if']
    condition = jobs['static_real_probe']['if']
    for required in ('workflow_dispatch', 'inputs.static_probe',
                     "inputs.probe_runtime == 'durable-object'",
                     "inputs.do_probe_phase == 'real'"):
        assert required in condition


def test_isolated_source_changes_cannot_trigger_production_push():
    path = ROOT / '.github/workflows/agent-publish.yml'
    definition = yaml.safe_load(path.read_text())
    trigger = definition.get('on', definition.get(True))
    patterns = trigger['push']['paths']
    for name in ('worker/src/real-search-do-probe.ts',
                 'worker/src/static-corpus-store.ts',
                 'worker/src/real-search-integration.test.ts',
                 'worker/wrangler.real-probe.toml',
                 'src/embed_real_search_probe.py'):
        assert not matches_path(name, patterns), name
    assert matches_path('worker/src/service.ts', patterns)


def test_real_job_proves_local_vectors_before_deploy_and_cleans_after_failures():
    job = workflow()['jobs']['static_real_probe']
    steps = job['steps']
    commands = '\n'.join(step.get('run', '') for step in steps)
    assert 'publish_agent_index.py' not in commands
    assert 'write_discovery_links.py ' not in commands
    assert '--config wrangler.real-probe.toml --name "$PROBE_NAME"' in commands
    deploy = next(i for i, step in enumerate(steps) if step.get('id') == 'deploy')
    assert any('embed_real_search_probe.py' in step.get('run', '')
               for step in steps[:deploy])
    assert any('real-search-integration.test.ts' in step.get('run', '')
               for step in steps[:deploy])
    cleanup = next(step for step in steps if step.get('id') == 'cleanup')
    assert 'always()' in cleanup['if']
    assert "steps.deploy.outcome == 'cancelled'" in cleanup['if']
    assert 'static_search_do_lifecycle.py cleanup "$PROBE_NAME"' in cleanup['run']
    bounded = sum(step.get('timeout-minutes', 0) for step in steps)
    assert job['timeout-minutes'] >= bounded + 5
    upload = next(step for step in steps if step.get('uses', '').startswith('actions/upload-artifact'))
    assert upload['if'] == 'always()'
    assert 'secrets.json' not in upload['with']['path']
    assert 'probe-do-lifecycle.json' in upload['with']['path']
    final = steps[-1]['run']
    assert "report.get('integration_gate') == 'passed'" in final
    assert "('gateway_cpu_gate', 'durable_object_cpu_gate', 'cpu_gate')" in final
    assert "lifecycle.get('namespace_absent') is True" in final


def test_workflow_scripts_parse_before_secrets_are_available():
    for step in workflow()['jobs']['static_real_probe']['steps']:
        script = step.get('run')
        if not script:
            continue
        subprocess.run(['bash', '-n'], input=script, text=True, check=True)
        if "<<'PYTHON'" in script:
            python = script.split("<<'PYTHON'\n", 1)[1].rsplit('\nPYTHON', 1)[0]
            ast.parse(python)


@pytest.mark.parametrize('field,value,expected', [
    ('gateway_cpu_gate', 'failed', 1),
    ('durable_object_cpu_gate', 'failed', 1),
    ('cpu_gate', 'failed', 1),
    ('durable_object_cpu_gate', None, 1),
    ('cpu_gate', 'unverified', 0),
])
def test_cpu_failure_or_unknown_field_cannot_be_hidden_by_continue_on_error(
    tmp_path, field, value, expected,
):
    report = {'integration_gate': 'passed', 'gateway_cpu_gate': 'passed',
              'durable_object_cpu_gate': 'passed', 'cpu_gate': 'passed'}
    report[field] = value
    (tmp_path / 'probe-real-report.json').write_text(json.dumps(report))
    (tmp_path / 'probe-do-lifecycle.json').write_text(json.dumps({
        'cleanup': 'passed', 'namespace_absent': True,
    }))
    script = workflow()['jobs']['static_real_probe']['steps'][-1]['run']
    python = script.split("<<'PYTHON'\n", 1)[1].rsplit('\nPYTHON', 1)[0]
    result = subprocess.run([sys.executable, '-c', python], cwd=tmp_path,
                            capture_output=True, text=True)
    assert result.returncode == expected, result.stdout + result.stderr
