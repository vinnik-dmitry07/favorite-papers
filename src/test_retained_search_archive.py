'''Archival must preserve exact bytes and never silently replace a Release.'''

import json
import hashlib
from pathlib import Path

import pytest
import yaml

import retained_search_archive as archive


def test_archive_pins_match_the_authenticated_restorer():
    import restore_full_search_artifact as restore
    for key in ('RUN_ID', 'ARTIFACT_ID', 'SOURCE_COMMIT', 'ARTIFACT_SHA256'):
        assert getattr(archive, key) == getattr(restore, key)


def fixture(monkeypatch):
    content = b'authenticated retained corpus'
    monkeypatch.setattr(archive, 'SIZE', len(content))
    monkeypatch.setattr(archive, 'ARTIFACT_SHA256',
                        hashlib.sha256(content).hexdigest())
    return content


def test_release_download_verifies_bytes_and_never_depends_on_actions(
        tmp_path, monkeypatch):
    content = fixture(monkeypatch)
    calls = []

    def gh(*args, output=None, absent=False):
        calls.append(args)
        if args[-1].endswith('/releases/tags/' + archive.TAG):
            return {'assets': [{'id': 5, 'name': archive.ASSET,
                                'size': len(content)}]}
        assert args[-1].endswith('/releases/assets/5')
        output.write(content)

    monkeypatch.setattr(archive, 'gh', gh)
    path = tmp_path / 'corpus.zip'
    assert archive.download(path, release_only=True)['source'] == 'release'
    assert path.read_bytes() == content
    assert not any('actions/' in str(call) for call in calls)


def test_wrong_release_bytes_are_rejected_without_fallback(
        tmp_path, monkeypatch):
    content = fixture(monkeypatch)

    def gh(*args, output=None, absent=False):
        if output is not None:
            output.write(b'x' * len(content))
            return
        return {'assets': [{'id': 5, 'name': archive.ASSET,
                            'size': len(content)}]}

    monkeypatch.setattr(archive, 'gh', gh)
    with pytest.raises(ValueError, match='reviewed bytes'):
        archive.download(tmp_path / 'corpus.zip')


def test_missing_permanent_archive_stops_publication_before_artifact_fallback(
        tmp_path, monkeypatch):
    monkeypatch.setattr(archive, 'gh', lambda *a, **kw: None)
    with pytest.raises(ValueError, match='not been saved'):
        archive.download(tmp_path / 'corpus.zip', release_only=True)


def test_archival_workflow_can_write_release_but_cannot_deploy_or_embed():
    root = Path(__file__).resolve().parents[1]
    source_path = root / '.github/workflows/preserve-search-corpus.yml'
    source = source_path.read_text()
    workflow = yaml.safe_load(source)
    assert workflow['permissions'] == {'contents': 'write', 'actions': 'read'}
    assert workflow['jobs']['preserve']['timeout-minutes'] == 15
    assert 'src/retained_search_archive.py --preserve' in source
    for forbidden in ('CLOUDFLARE_', 'wrangler', 'AutoModel', 'embed_real_',
                      'pull_request_target', 'secrets.'):
        assert forbidden not in source


def test_archive_release_targets_main_without_workflow_write_permission(
        tmp_path, monkeypatch):
    main = 'e' * 40
    created = []

    def gh(*args, **kwargs):
        if args[-1].endswith('/git/ref/heads/main'):
            return {'object': {'type': 'commit', 'sha': main}}
        assert '/git/ref/tags/' in args[-1]
        return None

    downloads = []

    def download(path, release_only=False):
        downloads.append(release_only)
        return {'source': 'release' if release_only else 'actions'}

    monkeypatch.setattr(archive, 'gh', gh)
    monkeypatch.setattr(archive, 'download', download)
    monkeypatch.setattr(archive.subprocess, 'run',
                        lambda args, **kw: created.append(args))
    assert archive.preserve(tmp_path)['preserved'] is True
    assert downloads == [False, True]
    args = created[0]
    assert args[args.index('--target') + 1] == main
    assert archive.SOURCE_COMMIT not in args
    notes = (tmp_path / 'release-notes.txt').read_text()
    assert archive.SOURCE_COMMIT in notes
    assert archive.ARTIFACT_SHA256 in notes
