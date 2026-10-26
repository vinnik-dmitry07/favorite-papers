'''Recovery must read original logs without relabelling or replaying a workload.'''

import hashlib
import json
from pathlib import Path

import pytest
import yaml

import prepare_static_search_do_collection as collection


REPOSITORY = 'owner/papers'
SOURCE = 'a' * 40
COLLECTOR = 'b' * 40
ACCOUNT = '1' * 32
SCRIPT = 'key-papers-static-do-probe-123-2'


@pytest.fixture
def evidence(tmp_path):
    source = tmp_path / 'source'
    source.mkdir()
    run_file = tmp_path / 'run.json'
    run = {
        'id': 123, 'run_attempt': 2, 'head_sha': SOURCE,
        'repository': {'full_name': REPOSITORY},
        'head_repository': {'full_name': REPOSITORY},
        'path': '.github/workflows/agent-api.yml',
        'event': 'workflow_dispatch', 'status': 'completed',
        'conclusion': 'failure',
    }
    report = {
        'probe_type': 'durable-object', 'phase': 'pilot',
        'source_sha': SOURCE, 'script_name': SCRIPT,
        'started_ms': 1000, 'finished_ms': 2000, 'http_attempts': 2,
        'sample_gate': 'unverified', 'pilot': [
            {'marker': name, 'kind': name, 'case': name + '.application_cold',
             'mode': 'application_cold', 'eligible': True, 'success': True,
             'state': 'complete', 'client_wall_ms': 10,
             'cold_kind': 'application-cache-reset'}
            for name in ('rest_search', 'mcp_search')
        ],
    }
    lifecycle = {
        'name': SCRIPT, 'source_sha': SOURCE, 'phase': 'removed',
        'account_fingerprint': hashlib.sha256(ACCOUNT.encode()).hexdigest(),
        'cleanup': 'passed', 'namespace_absent': True,
        'namespace': {'script': SCRIPT, 'class': 'StaticSearchProbe',
                      'use_sqlite': True},
    }
    for path, value in ((run_file, run),
                        (source / 'probe-do-report.json', report),
                        (source / 'probe-do-lifecycle.json', lifecycle)):
        path.write_text(json.dumps(value) + '\n')
    return source, run_file, tmp_path / 'output'


def prepare(evidence):
    source, run_file, output = evidence
    return collection.prepare(source, run_file, '123', REPOSITORY,
                              ACCOUNT, COLLECTOR, output)


def change(path, key, value):
    document = json.loads(path.read_text())
    document[key] = value
    path.write_text(json.dumps(document))


def test_failed_source_run_can_be_collected_without_changing_source(evidence):
    provenance = prepare(evidence)
    source, run_file, output = evidence
    assert provenance['source_sha'] == SOURCE
    assert provenance['collector_sha'] == COLLECTOR
    assert provenance['artifact_name'] == 'durable-object-probe-123-2'
    assert provenance['new_workload_requests'] == 0
    assert (output / 'original-probe-do-report.json').read_bytes() == (
        source / 'probe-do-report.json').read_bytes()
    assert provenance['source_run_metadata_sha256'] == collection.digest(run_file)
    report, passed = collection.verify_result(output)
    assert not passed
    assert report['source_sha'] == SOURCE
    assert report['sample_gate'] == 'unverified'


@pytest.mark.parametrize('key,value', [
    ('id', 124), ('run_attempt', 0), ('run_attempt', True),
    ('head_sha', 'bad'), ('status', 'in_progress'),
    ('repository', {'full_name': 'other/repo'}),
    ('head_repository', {'full_name': 'other/repo'}),
    ('path', '.github/workflows/other.yml'), ('event', 'pull_request'),
])
def test_unrelated_or_incomplete_source_run_rejected(evidence, key, value):
    change(evidence[1], key, value)
    with pytest.raises(ValueError, match='completed Agent API'):
        prepare(evidence)


@pytest.mark.parametrize('file,key,value', [
    ('probe-do-report.json', 'source_sha', COLLECTOR),
    ('probe-do-report.json', 'script_name', 'production'),
    ('probe-do-report.json', 'phase', 'collect'),
    ('probe-do-report.json', 'probe_type', 'worker'),
    ('probe-do-lifecycle.json', 'name', 'production'),
    ('probe-do-lifecycle.json', 'source_sha', COLLECTOR),
    ('probe-do-lifecycle.json', 'account_fingerprint', 'other-account'),
    ('probe-do-lifecycle.json', 'cleanup', 'failed'),
    ('probe-do-lifecycle.json', 'namespace_absent', False),
    ('probe-do-lifecycle.json', 'phase', 'captured'),
    ('probe-do-lifecycle.json', 'namespace', {'script': 'production'}),
])
def test_mismatched_or_uncleaned_probe_rejected(evidence, file, key, value):
    change(evidence[0] / file, key, value)
    with pytest.raises(ValueError, match='must agree'):
        prepare(evidence)


@pytest.mark.parametrize('key,value', [
    ('started_ms', False), ('finished_ms', 0),
    ('finished_ms', 90000000), ('finished_ms', '2000'),
])
def test_collection_timeframe_is_bounded(evidence, key, value):
    change(evidence[0] / 'probe-do-report.json', key, value)
    with pytest.raises(ValueError, match='timeframe'):
        prepare(evidence)


@pytest.mark.parametrize('run_id', ['0', '1; echo unsafe', '-2', '1\n2'])
def test_source_id_cannot_inject_output_or_shell(evidence, run_id):
    with pytest.raises(ValueError, match='numeric'):
        collection.identify(collection.read_json(evidence[1]), run_id,
                            REPOSITORY)


def test_recovered_cpu_can_pass_but_runtime_remains_unverified(evidence):
    prepare(evidence)
    output = evidence[2]
    path = output / 'probe-do-report.json'
    report = json.loads(path.read_text())
    for row in report['pilot']:
        row['telemetry'] = {
            'gateway': {'cpu_ms': 1, 'outcome': 'ok'},
            'durable_object': {'cpu_ms': 109, 'outcome': 'ok'},
        }
    path.write_text(json.dumps(report))
    report, passed = collection.verify_result(output)
    assert passed
    assert report['runtime_gate'] == 'unverified'
    assert report['source_sha'] == SOURCE


def test_saved_pass_string_is_not_evidence(evidence):
    prepare(evidence)
    output = evidence[2]
    change(output / 'probe-do-report.json', 'sample_gate', 'passed')
    report, passed = collection.verify_result(output)
    assert not passed
    assert report['sample_gate'] == 'unverified'


@pytest.mark.parametrize('key,value', [
    ('http_attempts', 3), ('source_sha', COLLECTOR),
    ('phase', 'matrix'), ('pilot', []), ('started_ms', 500),
])
def test_replayed_or_changed_workload_is_rejected(evidence, key, value):
    prepare(evidence)
    change(evidence[2] / 'probe-do-report.json', key, value)
    with pytest.raises(ValueError, match='workload or source identity'):
        collection.verify_result(evidence[2])


@pytest.mark.parametrize('name', [
    'original-probe-do-report.json', 'probe-do-lifecycle.json', 'source-run.json',
])
def test_original_evidence_must_remain_byte_identical(evidence, name):
    prepare(evidence)
    path = evidence[2] / name
    path.write_bytes(path.read_bytes() + b' ')
    with pytest.raises(ValueError, match='Original evidence changed'):
        collection.verify_result(evidence[2])


def test_collection_job_cannot_deploy_or_send_new_workload():
    path = Path(__file__).resolve().parents[1] / '.github/workflows/agent-api.yml'
    workflow = yaml.safe_load(path.read_text())
    job = workflow['jobs']['static_do_collect']
    steps = job['steps']
    commands = '\n'.join(step.get('run', '') for step in steps)
    assert 'wrangler' not in commands
    assert 'npm' not in commands
    assert 'static_search_do_lifecycle.py' not in commands
    assert 'PROBE_TOKEN' not in json.dumps(job)
    assert '--collect-only' in commands
    assert '--wait-seconds 300' in commands
    assert '--name "$SOURCE_ARTIFACT_NAME"' in commands
    assert '--pattern' not in commands
    assert 'prepare_static_search_do_collection.py verify' in commands
    assert job['timeout-minutes'] == 12
    collect = next(step for step in steps if step.get('id') == 'collect')
    assert collect['timeout-minutes'] == 6
    assert 'publish' not in workflow['jobs']
    for name in ('static_do_probe', 'static_probe'):
        assert "inputs.do_probe_phase != 'collect'" in workflow['jobs'][name]['if']
    assert "inputs.do_probe_phase == 'collect'" in job['if']
    assert workflow['permissions']['actions'] == 'read'
