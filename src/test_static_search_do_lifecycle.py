'''The DO experiment cannot orphan or delete another service's namespace.'''

import hashlib
import json
import tomllib

import pytest

import static_search_do_lifecycle as lifecycle


NAME = 'key-papers-static-do-probe-123-1'
ACCOUNT = 'a' * 32
SOURCE = 'b' * 40
ROW = {'id': 'namespace-1', 'script': NAME, 'class': 'StaticSearchProbe',
       'use_sqlite': True}


class FakeAPI:
    account = ACCOUNT

    def __init__(self, batches):
        self.batches = list(batches)
        self.calls = []

    def namespaces(self):
        self.calls.append('list')
        return self.batches.pop(0)

    def request(self, path, **kwargs):
        self.calls.append((path, kwargs))
        return {'success': True}


def report():
    return {'name': NAME, 'preflight': 'passed', 'namespace': dict(ROW),
            'source_sha': SOURCE,
            'account_fingerprint': hashlib.sha256(ACCOUNT.encode()).hexdigest()}


@pytest.fixture(autouse=True)
def no_sleep(monkeypatch):
    monkeypatch.setattr(lifecycle.time, 'sleep', lambda _: None)
    monkeypatch.setenv('GITHUB_SHA', SOURCE)
    monkeypatch.setenv('GITHUB_REPOSITORY', 'owner/repo')
    monkeypatch.setenv('CLOUDFLARE_ACCOUNT_ID', ACCOUNT)
    monkeypatch.setenv('CLOUDFLARE_API_TOKEN', 'test-token')


@pytest.mark.parametrize('name', ['key-papers-api', 'key-papers-static-do-probe',
                                  NAME + '/../key-papers-api'])
def test_rejects_production_or_ambiguous_names(name):
    with pytest.raises(ValueError, match='run-specific'):
        lifecycle.validate_name(name)


def test_preflight_blocks_previous_probe_but_ignores_other_services():
    api = FakeAPI([[dict(ROW, script='production')]])
    assert lifecycle.preflight(api, NAME)['preflight'] == 'passed'
    with pytest.raises(ValueError, match='cleanup is incomplete'):
        lifecycle.preflight(FakeAPI([[ROW]]), NAME)


def test_capture_retries_absence_but_not_unexpected_class():
    result = lifecycle.capture(FakeAPI([[], [ROW]]), NAME, report())
    assert result['namespace']['id'] == 'namespace-1'
    with pytest.raises(ValueError, match='exactly one'):
        lifecycle.capture(FakeAPI([[dict(ROW, **{'class': 'Other'})]]),
                          NAME, report())


def test_tombstone_has_no_class_binding_or_implementation(tmp_path):
    config = lifecycle.migration_files(tmp_path, NAME)
    data = tomllib.loads(config.read_text())
    assert data['name'] == NAME
    assert data['exports'] == {
        'StaticSearchProbe': {'type': 'durable-object', 'state': 'deleted'}}
    assert 'migrations' not in data and 'durable_objects' not in data
    assert 'StaticSearchProbe' not in (tmp_path / 'cleanup.mjs').read_text()


def test_namespace_is_deleted_and_verified_before_script(tmp_path, monkeypatch):
    api = FakeAPI([[ROW], [ROW], []])
    order = []
    monkeypatch.setattr(lifecycle, 'delete_class',
                        lambda *_: order.append('tombstone'))
    out = tmp_path / 'lifecycle.json'
    result = lifecycle.cleanup(api, NAME, report(), out, tmp_path / 'log')
    assert order == ['tombstone']
    assert api.calls[:3] == ['list'] * 3
    path, kwargs = api.calls[3]
    assert path == '/workers/scripts/' + NAME
    assert kwargs == {'method': 'DELETE', 'allow_absent': True}
    assert result['namespace_absent'] and result['cleanup'] == 'passed'
    assert json.loads(out.read_text())['phase'] == 'removed'


def test_partial_deployment_can_be_cleaned_before_capture(tmp_path, monkeypatch):
    data = report()
    data['namespace'] = None
    api = FakeAPI([[ROW], []])
    monkeypatch.setattr(lifecycle, 'delete_class', lambda *_: None)
    result = lifecycle.cleanup(api, NAME, data, tmp_path / 'report',
                               tmp_path / 'log')
    assert result['namespace']['id'] == ROW['id']
    assert result['cleanup'] == 'passed'


@pytest.mark.parametrize('rows', [
    [dict(ROW, script='production')],
    [dict(ROW, id='replacement')],
    [dict(ROW, use_sqlite=False)],
    [ROW, dict(ROW, id='another')],
])
def test_changed_ownership_or_unexpected_namespace_never_mutates(
        tmp_path, monkeypatch, rows):
    api = FakeAPI([rows])
    monkeypatch.setattr(lifecycle, 'delete_class',
                        lambda *_: pytest.fail('Unsafe migration'))
    with pytest.raises(ValueError):
        lifecycle.cleanup(api, NAME, report(), tmp_path / 'report',
                          tmp_path / 'log')
    assert api.calls == ['list']


def test_failed_migration_never_deletes_worker(tmp_path, monkeypatch):
    def fail(*_):
        raise ValueError('migration rejected')

    api = FakeAPI([[ROW]])
    monkeypatch.setattr(lifecycle, 'delete_class', fail)
    with pytest.raises(ValueError, match='migration rejected'):
        lifecycle.cleanup(api, NAME, report(), tmp_path / 'report',
                          tmp_path / 'log')
    assert api.calls == ['list']


def test_still_present_namespace_never_deletes_worker(tmp_path, monkeypatch):
    api = FakeAPI([[ROW]] * 7)
    monkeypatch.setattr(lifecycle, 'delete_class', lambda *_: None)
    with pytest.raises(ValueError, match='still exists'):
        lifecycle.cleanup(api, NAME, report(), tmp_path / 'report',
                          tmp_path / 'log')
    assert api.calls == ['list'] * 7


def test_absent_namespace_skips_tombstone_for_idempotent_cleanup(
        tmp_path, monkeypatch):
    api = FakeAPI([[]])
    monkeypatch.setattr(lifecycle, 'delete_class',
                        lambda *_: pytest.fail('Unnecessary migration'))
    result = lifecycle.cleanup(api, NAME, report(), tmp_path / 'report',
                               tmp_path / 'log')
    assert result['cleanup'] == 'passed'


def test_namespace_api_paginates_and_handles_empty_account(monkeypatch):
    api = lifecycle.Cloudflare()
    responses = [{'result': [ROW], 'result_info': {'total_pages': 2}},
                 {'result': [dict(ROW, id='second')],
                  'result_info': {'total_pages': 2}}]
    paths = []

    def request(path):
        paths.append(path)
        return responses.pop(0)

    monkeypatch.setattr(api, 'request', request)
    assert len(api.namespaces()) == 2
    assert 'page=1&per_page=1000' in paths[0]
    assert 'page=2&per_page=1000' in paths[1]
    monkeypatch.setattr(api, 'request', lambda _: {
        'result': [], 'result_info': {'total_pages': 0, 'total_count': 0}})
    assert api.namespaces() == []


def test_missing_namespace_ownership_is_not_proof_of_absence(monkeypatch):
    api = lifecycle.Cloudflare()
    monkeypatch.setattr(api, 'request', lambda _: {'result': [{'id': 'n'}]})
    with pytest.raises(ValueError, match='Malformed namespace'):
        api.namespaces()


def pilot_files(tmp_path):
    run = {'id': 123, 'run_attempt': 1, 'head_sha': SOURCE,
           'repository': {'full_name': 'owner/repo'},
           'path': '.github/workflows/agent-api.yml',
           'event': 'workflow_dispatch', 'conclusion': 'success',
           'status': 'completed'}
    run_file = tmp_path / 'run.json'
    run_file.write_text(json.dumps(run))
    data = report()
    data.update(cleanup='passed', namespace_absent=True)
    artifact = tmp_path / 'artifact'
    artifact.mkdir()
    (artifact / 'probe-do-lifecycle.json').write_text(json.dumps(data))
    measurement = {'source_sha': SOURCE, 'script_name': NAME,
                   'phase': 'pilot', 'phase_complete': True,
                   'sample_gate': 'passed', 'preflight_gate': 'passed',
                   'runtime_gate': 'unverified'}
    (artifact / 'probe-do-report.json').write_text(json.dumps(measurement))
    return artifact, run_file


def test_pilot_requires_real_run_identity_but_not_unproven_memory(tmp_path):
    artifact, run = pilot_files(tmp_path)
    assert lifecycle.validate_pilot(artifact, run, '123', ACCOUNT)[
        'pilot_verified']


@pytest.mark.parametrize('file,key,value', [
    ('run.json', 'head_sha', 'c' * 40),
    ('run.json', 'path', '.github/workflows/other.yml'),
    ('run.json', 'conclusion', 'failure'),
    ('probe-do-report.json', 'phase', 'matrix'),
    ('probe-do-report.json', 'phase_complete', False),
    ('probe-do-report.json', 'preflight_gate', 'unverified'),
    ('probe-do-lifecycle.json', 'cleanup', 'failed'),
    ('probe-do-lifecycle.json', 'namespace_absent', False),
    ('probe-do-lifecycle.json', 'account_fingerprint', 'other'),
])
def test_matrix_rejects_unproven_or_unrelated_pilot(tmp_path, file, key, value):
    artifact, run = pilot_files(tmp_path)
    path = run if file == 'run.json' else artifact / file
    data = json.loads(path.read_text())
    data[key] = value
    path.write_text(json.dumps(data))
    with pytest.raises(ValueError):
        lifecycle.validate_pilot(artifact, run, '123', ACCOUNT)


@pytest.mark.parametrize('gate', ['failed', 'unverified', None])
def test_complete_samples_with_negative_gate_never_make_ci_green(gate):
    assert not lifecycle.phase_passed(
        {'phase_complete': True, 'sample_gate': gate},
        {'cleanup': 'passed', 'namespace_absent': True})


def test_ci_gate_requires_namespace_absence():
    assert not lifecycle.phase_passed(
        {'phase_complete': True, 'sample_gate': 'passed'},
        {'cleanup': 'passed'})
    assert lifecycle.phase_passed(
        {'phase_complete': True, 'sample_gate': 'passed'},
        {'cleanup': 'passed', 'namespace_absent': True})


def test_workflow_bounds_load_and_cleans_cancelled_deployments():
    import yaml

    path = lifecycle.ROOT / '.github/workflows/agent-api.yml'
    workflow = yaml.safe_load(path.read_text())
    job = workflow['jobs']['static_do_probe']
    assert workflow['permissions']['actions'] == 'read'
    assert job['timeout-minutes'] == 50
    steps = {item.get('id'): item for item in job['steps'] if item.get('id')}
    assert steps['measure']['timeout-minutes'] == 20
    assert steps['cleanup']['timeout-minutes'] == 8
    assert "steps.deploy.outcome == 'cancelled'" in steps['cleanup']['if']
    assert 'always()' in steps['cleanup']['if']
    assert '--max-load-seconds 900' in steps['measure']['run']
    final = job['steps'][-1]['run']
    assert 'phase_passed(report, lifecycle)' in final
    upload = next(item for item in job['steps']
                  if item.get('uses', '').startswith('actions/upload-artifact'))
    assert 'secrets' not in upload['with']['path']
