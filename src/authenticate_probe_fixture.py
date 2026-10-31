'''Authenticate the pinned historical fixture without requiring Git ancestry.

The archive digest and exact historical run bind this regression fixture even
when the experiment branch is squash-merged. This does not certify current
provider compatibility. Expired GitHub artifacts must be replaced by a reviewed
pin; the downloader never accepts a substitute automatically.
'''

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import stat
import zipfile


RUN_ID = 40238828496
ARTIFACT_ID = 12616396041
SOURCE_SHA = '4723db4635bd6d2865211e1527f014460e1405da'
ARCHIVE_SHA256 = (
    'ae50de4d8de1ebc0d44c9b73d1d3e677a4523bbb9caf10a8db78acad8030a8c0'
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate_metadata(run, artifact, repository):
    '''Check run and artifact identities before downloading any archive.'''
    require(bool(repository), 'Repository identity is missing')
    require(
        run.get('id') == RUN_ID and run.get('status') == 'completed'
        and run.get('conclusion') == 'success'
        and run.get('name') == 'Agent API'
        and run.get('event') == 'workflow_dispatch'
        and run.get('path') == '.github/workflows/agent-api.yml'
        and run.get('repository', {}).get('full_name') == repository
        and run.get('head_repository', {}).get('full_name') == repository
        and run.get('head_sha') == SOURCE_SHA,
        'Historical numerical run identity does not match the reviewed pin',
    )
    attempt = run.get('run_attempt')
    require(type(attempt) is int and attempt > 0, 'Invalid run attempt')
    require(
        artifact.get('id') == ARTIFACT_ID
        and artifact.get('expired') is False
        and artifact.get('name') == f'real-search-probe-{RUN_ID}-{attempt}'
        and artifact.get('workflow_run', {}).get('id') == RUN_ID,
        'Historical numerical artifact is expired or differs from the pin',
    )


def extract_fixture(archive, target):
    '''Validate the exact archive and safe members before extracting it.'''
    archive, target = Path(archive), Path(target)
    require(hashlib.sha256(archive.read_bytes()).hexdigest() == ARCHIVE_SHA256,
            'Numerical fixture archive checksum mismatch')
    require(not target.exists(), 'Numerical fixture target must be absent')
    with zipfile.ZipFile(archive) as source:
        entries = source.infolist()
        require(len(entries) < 1000
                and sum(item.file_size for item in entries) < 64 * 1024 * 1024,
                'Numerical fixture archive exceeds its extraction bound')
        seen = set()
        for item in entries:
            path = PurePosixPath(item.filename)
            require(not path.is_absolute() and '..' not in path.parts
                    and '\\' not in item.filename
                    and ':' not in item.filename and path.parts
                    and item.filename not in seen,
                    'Unsafe or duplicate archive path')
            require(stat.S_IFMT(item.external_attr >> 16) != stat.S_IFLNK,
                    'Archive symlink rejected')
            seen.add(item.filename)
        source.extractall(target)
    manifest = json.loads((target / 'agent_real_probe/probe.json').read_text())
    require(manifest.get('source_sha') == SOURCE_SHA,
            'Fixture source commit differs from the authenticated run')
    require((target / 'agent_real_probe/vectors.f32').is_file(),
            'Numerical fixture vectors are missing')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run', type=Path, required=True)
    parser.add_argument('--artifact', type=Path, required=True)
    parser.add_argument('--repository', default=os.environ.get(
        'GITHUB_REPOSITORY', ''))
    parser.add_argument('--archive', type=Path)
    parser.add_argument('--target', type=Path)
    args = parser.parse_args(argv)
    if bool(args.archive) != bool(args.target):
        parser.error('--archive and --target must be supplied together')
    validate_metadata(json.loads(args.run.read_text()),
                      json.loads(args.artifact.read_text()), args.repository)
    if args.archive:
        extract_fixture(args.archive, args.target)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
