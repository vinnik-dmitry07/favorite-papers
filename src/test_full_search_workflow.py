'''Full-corpus dispatch cannot bypass cheap gates or deploy a production API.'''

import ast
import os
from pathlib import Path
import re
import subprocess

import pytest
import yaml


ROOT = Path(__file__).resolve().parents[1]


def workflow():
    return yaml.safe_load((ROOT / '.github/workflows/agent-api.yml').read_text())


def full_job():
    return workflow()['jobs']['full_offline_probe']


def steps_by_id():
    return {step['id']: step for step in full_job()['steps'] if 'id' in step}


def test_full_mode_defaults_to_no_long_run_or_provider_allowance():
    definition = workflow()
    trigger = definition.get('on', definition.get(True))
    inputs = trigger['workflow_dispatch']['inputs']
    assert 'full' in inputs['do_probe_phase']['options']
    assert inputs['full_run_confirmed']['type'] == 'boolean'
    assert inputs['full_run_confirmed']['default'] is False
    assert inputs['provider_available_neurons']['default'] == '0'
    assert inputs['full_numeric_run_id']['default'] == '40238828496'
    assert definition['permissions'] == {'contents': 'read', 'actions': 'read'}


def test_full_dispatch_is_isolated_from_every_deployment_job():
    jobs = workflow()['jobs']
    condition = full_job()['if']
    assert "github.event_name == 'workflow_dispatch'" in condition
    assert "inputs.do_probe_phase == 'full'" in condition
    for name in ('publish', 'static_probe', 'static_do_probe', 'static_real_probe'):
        assert "inputs.do_probe_phase != 'full'" in jobs[name]['if']
    commands = '\n'.join(step.get('run', '') for step in full_job()['steps'])
    for forbidden in ('wrangler deploy', 'publish_agent_index.py',
                      'gh workflow run', 'write_discovery_links.py',
                      'static_search_do_lifecycle.py'):
        assert forbidden not in commands
    assert full_job()['needs'] == 'offline'


def test_cheap_gate_order_precedes_any_canary_or_long_encode():
    steps = full_job()['steps']
    ids = [step['id'] for step in steps if 'id' in step]
    ordered = ['controls', 'cheap_tests', 'numeric_source', 'canonical',
               'frozen_queries', 'snapshot', 'tokenizer_gate', 'numeric_gate',
               'geometry_pack', 'geometry_memory', 'geometry_gate',
               'canary_controls', 'canary', 'admission', 'full_encode',
               'query_encode', 'full_pack', 'full_quality']
    assert [ids.index(name) for name in ordered] == sorted(ids.index(name) for name in ordered)
    by_id = steps_by_id()
    assert 'preflight_full_search_probe.py numeric' in by_id['numeric_gate']['run']
    assert '--real-source full-probe-reports/numeric-source/agent_real_probe' in by_id['numeric_gate']['run']
    assert '--geometry-fixture' in by_id['geometry_pack']['run']
    assert '--data-label geometry-fixture' in by_id['geometry_memory']['run']
    assert '--canonical agent_full_probe/probe.json' in by_id['geometry_memory']['run']
    assert 'record-geometry' in by_id['geometry_gate']['run']
    assert by_id['geometry_gate']['if'] == "always() && steps.geometry_pack.outcome == 'success'"
    before_canary = '\n'.join(step.get('run', '') for step in steps[:next(
        i for i, step in enumerate(steps) if step.get('id') == 'canary')])
    assert 'AutoTokenizer.from_pretrained' in before_canary
    assert 'AutoModel' not in before_canary
    assert 'embed_real_search_probe.py' not in before_canary
    assert 'run_full_probe_canary.py' not in before_canary


def test_long_entrypoints_require_explicit_confirmation_and_certificate():
    steps = steps_by_id()
    assert full_job()['timeout-minutes'] == 350
    assert steps['full_encode']['timeout-minutes'] == 240
    assert steps['query_encode']['timeout-minutes'] == 45
    assert sum(step.get('timeout-minutes', 0) for step in full_job()['steps']) <= 345
    for name in ('full_encode', 'query_encode', 'full_pack', 'full_quality'):
        step = steps[name]
        assert 'success()' in step['if']
        assert 'inputs.full_run_confirmed' in step['if']
        assert ".outcome == 'success'" in step['if']
        assert not step.get('continue-on-error', False)
    for name in ('full_encode', 'query_encode', 'full_quality'):
        assert '--full-run-confirmed' in steps[name]['run']
        assert 'full-probe-reports/preflight/certificate.json' in steps[name]['run']
    assert '--local-files-only' in steps['full_encode']['run']
    assert '--allow-model-download' not in steps['query_encode']['run']
    assert "report.get('extractive_fidelity_gate') != 'passed'" in steps['full_quality']['run']
    assert steps['admission']['if'] == "always() && steps.snapshot.outcome == 'success'"
    assert not steps['admission'].get('continue-on-error', False)


def test_numeric_fixture_has_reviewed_archive_identity_and_ancestry():
    script = steps_by_id()['numeric_source']['run']
    for text in ('12616396041', '40238828496',
                 'ae50de4d8de1ebc0d44c9b73d1d3e677a4523bbb9caf10a8db78acad8030a8c0',
                 "run['conclusion'] == 'success'", "run['name'] == 'Agent API'",
                 "run['path'] == '.github/workflows/agent-api.yml'",
                 "'merge-base', '--is-ancestor'", "manifest['source_sha'] == run['head_sha']",
                 'Archive symlink rejected'):
        assert text in script
    checkout = next(step for step in full_job()['steps'] if step.get('uses', '').startswith('actions/checkout'))
    assert checkout['with']['fetch-depth'] == 0


def test_canary_is_bounded_and_secrets_are_not_persisted():
    canary = steps_by_id()['canary']
    assert canary['timeout-minutes'] == 6
    assert '--provider --available-neurons "$PROVIDER_AVAILABLE_NEURONS"' in canary['run']
    assert canary['run'].count('run_full_probe_canary.py') == 1
    assert '$GITHUB_ENV' not in canary['run']
    assert not canary.get('continue-on-error', False)
    uploads = [step for step in full_job()['steps'] if step.get('uses', '').startswith('actions/upload-artifact')]
    assert len(uploads) == 1 and uploads[0]['if'] == 'always()'
    assert 'full-probe-reports/' in uploads[0]['with']['path']
    assert 'secret' not in uploads[0]['with']['path']
    assert 'agent_full_probe/vectors.f32' in uploads[0]['with']['path']


def test_partial_caches_are_restored_only_after_admission_and_saved_after_failure():
    steps = full_job()['steps']
    restore = next(step for step in steps if step.get('uses') == 'actions/cache/restore@v4')
    save = next(step for step in steps if step.get('uses') == 'actions/cache/save@v4')
    assert 'inputs.full_run_confirmed' in restore['if']
    assert "steps.admission.outcome == 'success'" in restore['if']
    assert 'always()' in save['if']
    assert "steps.full_encode.outcome == 'failure'" in save['if']
    assert "steps.full_encode.outcome == 'cancelled'" in save['if']
    assert restore['with']['path'] == save['with']['path']
    assert '.cache/full-probe-embeddings' in restore['with']['path']
    assert '.cache/full-probe-queries' in restore['with']['path']
    assert 'a5beb1e3e68b9ab74eb54cfd186867f64f240e1a-tokenizer-v2' in restore['with']['key']
    assert '${{ github.run_id }}-${{ github.run_attempt }}' in restore['with']['key']
    assert '${{ github.ref_name }}-' in restore['with']['restore-keys']
    assert save['with']['key'] == '${{ steps.restore_full_cache.outputs.cache-primary-key }}'


def test_all_workflow_shell_and_embedded_python_parse_without_credentials():
    for step in full_job()['steps']:
        script = step.get('run')
        if script:
            subprocess.run(['bash', '-n'], input=script, text=True, check=True)
            for python in re.findall(r"<<'PYTHON'\n(.*?)\nPYTHON", script, re.S):
                ast.parse(python)


@pytest.mark.parametrize('confirmed,neurons,run_id,passes', [
    ('false', '0', '40238828496', True),
    ('true', '0', '40238828496', False),
    ('true', '64', '40238828496', True),
    ('false', '-1', '40238828496', False),
    ('false', '1;echo unsafe', '40238828496', False),
    ('false', '64', '123', False),
])
def test_controls_fail_closed_before_model_work(tmp_path, confirmed, neurons, run_id, passes):
    env = {**os.environ, 'FULL_RUN_CONFIRMED': confirmed,
           'PROVIDER_AVAILABLE_NEURONS': neurons, 'FULL_NUMERIC_RUN_ID': run_id}
    result = subprocess.run(['bash', '-e', '-o', 'pipefail', '-c', steps_by_id()['controls']['run']],
                            cwd=tmp_path, env=env, capture_output=True, text=True)
    assert (result.returncode == 0) is passes, result.stderr


@pytest.mark.parametrize('free,neurons,passes', [
    ('false', '100', False), ('true', '0', False), ('true', '64', True),
])
def test_missing_provider_allowance_stops_before_any_canary(tmp_path, free, neurons, passes):
    env = {**os.environ, 'FREE_PLAN_CONFIRMED': free, 'PROVIDER_AVAILABLE_NEURONS': neurons}
    result = subprocess.run(['bash', '-e', '-c', steps_by_id()['canary_controls']['run']],
                            cwd=tmp_path, env=env, capture_output=True, text=True)
    assert (result.returncode == 0) is passes, result.stderr
