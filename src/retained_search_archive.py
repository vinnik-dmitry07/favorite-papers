'''Preserve or download the pinned search corpus without model inference.'''

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile

REPOSITORY = 'vinnik-dmitry07/favorite-papers'
RUN_ID = 40448979121
ARTIFACT_ID = 12715563729
SOURCE_COMMIT = 'fa3f4ec3724949a98b2b510949cf8efe405baf8a'
ARTIFACT_SHA256 = (
    '8f3fd29b369ae41f1474e052e0eef931a23ca7437c99640adbc6bc13d519c65c'
)
TAG = 'retained-search-corpus-2026-10-26'
ASSET = 'retained-full-search-40575.zip'
SIZE = 149682694


def file_hash(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def gh(*args, output=None, absent=False):
    result = subprocess.run(
        ['gh', *args], stdout=output or subprocess.PIPE,
        stderr=subprocess.PIPE, timeout=240, check=False,
    )
    if absent and result.returncode and b'HTTP 404' in result.stderr:
        return None
    if result.returncode:
        raise ValueError('GitHub operation failed: ' + args[0])
    return json.loads(result.stdout) if output is None else True


def checked(path):
    if Path(path).stat().st_size != SIZE or file_hash(path) != ARTIFACT_SHA256:
        raise ValueError('Retained archive differs from the reviewed bytes')


def download(path, *, release_only=False):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    release = gh('api', f'repos/{REPOSITORY}/releases/tags/{TAG}', absent=True)
    if release is not None:
        assets = [a for a in release.get('assets', [])
                  if a.get('name') == ASSET]
        if len(assets) != 1 or assets[0].get('size') != SIZE:
            raise ValueError('Retained Release asset is missing or changed')
        with path.open('wb') as stream:
            gh('api', '-H', 'Accept: application/octet-stream',
               f'repos/{REPOSITORY}/releases/assets/{assets[0]["id"]}',
               output=stream)
        source = 'release'
    else:
        if release_only:
            raise ValueError('The permanent corpus Release has not been saved')
        artifact = gh('api', f'repos/{REPOSITORY}/actions/artifacts/'
                      f'{ARTIFACT_ID}')
        if (artifact.get('expired') is not False
                or artifact.get('workflow_run', {}).get('id') != RUN_ID
                or artifact.get('workflow_run', {}).get('head_sha')
                != SOURCE_COMMIT):
            raise ValueError('Original artifact metadata differs or expired')
        with path.open('wb') as stream:
            gh('api', f'repos/{REPOSITORY}/actions/artifacts/'
               f'{ARTIFACT_ID}/zip', output=stream)
        source = 'actions'
    checked(path)
    return {'source': source, 'sha256': ARTIFACT_SHA256, 'bytes': SIZE,
            'provider_calls': 0}


def preserve(directory):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / ASSET
    report = download(path)
    if report['source'] == 'actions':
        notes = directory / 'release-notes.txt'
        notes.write_text(
            'Pinned corpus and saved FP32 query/corpus vectors.\n'
            f'Original run: {RUN_ID}; source: {SOURCE_COMMIT}.\n'
            f'Archive SHA-256: {ARTIFACT_SHA256}.\n'
            'This preserves existing bytes, without inference or a new '
            'production-readiness certificate.\n', encoding='utf-8')
        # Never replace an existing release, tag or same-named asset.
        existing_tag = gh('api', f'repos/{REPOSITORY}/git/ref/tags/{TAG}',
                          absent=True)
        target = (existing_tag or {}).get('object', {}).get('sha')
        if existing_tag is not None and target != SOURCE_COMMIT:
            raise ValueError('The archive tag points at another source commit')
        subprocess.run([
            'gh', 'release', 'create', TAG, str(path), '--repo', REPOSITORY,
            '--target', SOURCE_COMMIT, '--title', 'Retained search corpus',
            '--notes-file', str(notes), '--latest=false',
        ], check=True, timeout=240)
    with tempfile.TemporaryDirectory() as temporary:
        receipt = download(Path(temporary) / ASSET, release_only=True)
    return {**receipt, 'preserved': True, 'tag': TAG, 'asset': ASSET,
            'url': f'https://github.com/{REPOSITORY}/releases/tag/{TAG}'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--preserve', action='store_true')
    parser.add_argument('--archive', type=Path)
    parser.add_argument('--report', type=Path, required=True)
    args = parser.parse_args()
    if args.preserve:
        with tempfile.TemporaryDirectory() as temporary:
            report = preserve(temporary)
    elif args.archive:
        report = download(args.archive, release_only=True)
    else:
        parser.error('--preserve or --archive is required')
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report))


if __name__ == '__main__':
    main()
