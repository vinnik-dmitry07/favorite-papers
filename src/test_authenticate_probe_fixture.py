'''Pinned fixture trust must survive squash and Python optimization flags.'''

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import zipfile

import pytest

import authenticate_probe_fixture as fixture


def metadata():
    run = {
        'id': fixture.RUN_ID, 'status': 'completed', 'conclusion': 'success',
        'name': 'Agent API', 'event': 'workflow_dispatch',
        'path': '.github/workflows/agent-api.yml',
        'repository': {'full_name': 'owner/papers'},
        'head_repository': {'full_name': 'owner/papers'},
        'head_sha': fixture.SOURCE_SHA, 'run_attempt': 1,
    }
    artifact = {
        'id': fixture.ARTIFACT_ID, 'expired': False,
        'name': f'real-search-probe-{fixture.RUN_ID}-1',
        'workflow_run': {'id': fixture.RUN_ID},
    }
    return run, artifact


def test_fixture_pin_does_not_depend_on_current_head_or_ancestry(monkeypatch):
    monkeypatch.setenv('GITHUB_SHA', 'a' * 40)
    fixture.validate_metadata(*metadata(), 'owner/papers')


@pytest.mark.parametrize('part,key,value', [
    (0, 'head_sha', 'a' * 40), (0, 'status', 'in_progress'),
    (0, 'conclusion', 'failure'), (0, 'event', 'pull_request'),
    (0, 'path', '.github/workflows/other.yml'),
    (0, 'head_repository', {'full_name': 'fork/papers'}),
    (0, 'repository', {'full_name': 'fork/papers'}),
    (0, 'run_attempt', True), (1, 'expired', True),
    (1, 'id', 1), (1, 'workflow_run', {'id': 1}),
])
def test_substituted_or_expired_metadata_is_rejected(part, key, value):
    pair = metadata()
    pair[part][key] = value
    with pytest.raises(ValueError):
        fixture.validate_metadata(*pair, 'owner/papers')


def test_optimized_python_cannot_disable_metadata_validation(tmp_path):
    run, artifact = metadata()
    run['head_sha'] = 'a' * 40
    run_path, artifact_path = tmp_path / 'run.json', tmp_path / 'artifact.json'
    run_path.write_text(json.dumps(run))
    artifact_path.write_text(json.dumps(artifact))
    result = subprocess.run([
        sys.executable, '-O', str(Path(fixture.__file__)),
        '--run', str(run_path), '--artifact', str(artifact_path),
        '--repository', 'owner/papers',
    ], capture_output=True, text=True)
    assert result.returncode != 0
    assert 'does not match the reviewed pin' in result.stderr


def archive(tmp_path, monkeypatch, extra=None):
    path = tmp_path / 'fixture.zip'
    with zipfile.ZipFile(path, 'w') as target:
        target.writestr('agent_real_probe/probe.json', json.dumps({
            'source_sha': fixture.SOURCE_SHA,
        }))
        target.writestr('agent_real_probe/vectors.f32', b'vectors')
        if extra:
            target.writestr(extra, b'bad')
    monkeypatch.setattr(fixture, 'ARCHIVE_SHA256', hashlib.sha256(
        path.read_bytes()).hexdigest())
    return path


def test_exact_digest_archive_is_extracted(tmp_path, monkeypatch):
    path = archive(tmp_path, monkeypatch)
    fixture.extract_fixture(path, tmp_path / 'output')
    assert (tmp_path / 'output/agent_real_probe/vectors.f32').read_bytes()


@pytest.mark.parametrize('name', ['../escape', '/absolute', 'a\\b', 'C:file'])
def test_unsafe_archive_never_extracts(tmp_path, monkeypatch, name):
    path = archive(tmp_path, monkeypatch, name)
    with pytest.raises(ValueError, match='Unsafe'):
        fixture.extract_fixture(path, tmp_path / 'output')
    assert not (tmp_path / 'output').exists()


def test_different_archive_cannot_be_used(tmp_path, monkeypatch):
    path = archive(tmp_path, monkeypatch)
    path.write_bytes(path.read_bytes() + b'changed')
    with pytest.raises(ValueError, match='checksum'):
        fixture.extract_fixture(path, tmp_path / 'output')
    assert not (tmp_path / 'output').exists()
