'''Validate and preserve an existing DO probe before read-only log collection.'''

import argparse
import hashlib
import json
import os
from pathlib import Path
import re

from static_search_do_lifecycle import PREFIX, checkpoint, phase_passed


def read_json(path):
    value = json.loads(Path(path).read_text(encoding='utf-8'))
    if not isinstance(value, dict):
        raise ValueError('Expected an evidence object')
    return value


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def identify(run, run_id, repository):
    if not re.fullmatch(r'[1-9][0-9]*', run_id):
        raise ValueError('A numeric source run ID is required')
    attempt = run.get('run_attempt')
    if (not repository or str(run.get('id')) != run_id
            or run.get('repository', {}).get('full_name') != repository
            or run.get('head_repository', {}).get('full_name') != repository
            or run.get('path') != '.github/workflows/agent-api.yml'
            or run.get('event') != 'workflow_dispatch'
            or run.get('status') != 'completed'
            or not isinstance(attempt, int) or isinstance(attempt, bool)
            or attempt < 1
            or not re.fullmatch(r'[a-f0-9]{40}', run.get('head_sha', ''))):
        raise ValueError('Source must be a completed Agent API dispatch in this repository')
    return {
        'source_run_id': int(run_id), 'source_run_attempt': attempt,
        'source_sha': run['head_sha'],
        'artifact_name': f'durable-object-probe-{run_id}-{attempt}',
        'script_name': f'{PREFIX}{run_id}-{attempt}',
    }


def workload_digest(report):
    '''Exclude only fields that the telemetry collector is allowed to update.'''
    value = {key: report.get(key) for key in (
        'probe_type', 'phase', 'source_sha', 'origin', 'run_id', 'script_name',
        'started_ms', 'finished_ms', 'http_attempts', 'matrix_finished',
        'info', 'object_id',
    )}
    for group in ('requests', 'discovery', 'pilot', 'priming', 'concurrency'):
        value[group] = [
            {key: item for key, item in row.items()
             if key not in ('telemetry', 'telemetry_conflict')}
            for row in report.get(group, [])
        ]
    encoded = json.dumps(value, sort_keys=True, separators=(',', ':')).encode()
    return hashlib.sha256(encoded).hexdigest()


def prepare(directory, run_file, run_id, repository, account, collector_sha,
            output_dir):
    identity = identify(read_json(run_file), run_id, repository)
    directory, output_dir = Path(directory), Path(output_dir)
    report_path = directory / 'probe-do-report.json'
    lifecycle_path = directory / 'probe-do-lifecycle.json'
    report, lifecycle = read_json(report_path), read_json(lifecycle_path)
    if (not re.fullmatch(r'[a-fA-F0-9]{32}', account)
            or not re.fullmatch(r'[a-f0-9]{40}', collector_sha)):
        raise ValueError('Account and collector SHA are required')
    fingerprint = hashlib.sha256(account.encode()).hexdigest()
    namespace = lifecycle.get('namespace') or {}
    if (report.get('probe_type') != 'durable-object'
            or report.get('phase') not in ('pilot', 'matrix')
            or report.get('source_sha') != identity['source_sha']
            or report.get('script_name') != identity['script_name']
            or lifecycle.get('name') != identity['script_name']
            or lifecycle.get('source_sha') != identity['source_sha']
            or lifecycle.get('account_fingerprint') != fingerprint
            or lifecycle.get('cleanup') != 'passed'
            or lifecycle.get('namespace_absent') is not True
            or lifecycle.get('phase') != 'removed'
            or namespace.get('script') != identity['script_name']
            or namespace.get('class') != 'StaticSearchProbe'
            or namespace.get('use_sqlite') is not True):
        raise ValueError('Source report, account and verified cleanup must agree')
    started, finished = report.get('started_ms'), report.get('finished_ms')
    if (not all(isinstance(value, int) and not isinstance(value, bool)
                for value in (started, finished))
            or not 0 < started <= finished <= started + 86400000):
        raise ValueError('Source telemetry timeframe is invalid or unbounded')
    provenance = {
        **identity, 'repository': repository,
        'collector_sha': collector_sha,
        'source_report_sha256': digest(report_path),
        'source_lifecycle_sha256': digest(lifecycle_path),
        'source_run_metadata_sha256': digest(run_file),
        'workload_sha256': workload_digest(report),
        'new_workload_requests': 0,
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    # Keep byte-exact originals; a later successful collection cannot rewrite
    # what the original Actions run observed or its original conclusion.
    for source, name in (
        (report_path, 'original-probe-do-report.json'),
        (lifecycle_path, 'probe-do-lifecycle.json'),
        (Path(run_file), 'source-run.json'),
    ):
        (output_dir / name).write_bytes(source.read_bytes())
    report['collection_provenance'] = provenance
    checkpoint(output_dir / 'probe-do-report.json', report)
    checkpoint(output_dir / 'collection-provenance.json', provenance)
    return provenance


def verify_result(directory):
    directory = Path(directory)
    provenance = read_json(directory / 'collection-provenance.json')
    report = read_json(directory / 'probe-do-report.json')
    lifecycle = read_json(directory / 'probe-do-lifecycle.json')
    for filename, key in (
        ('original-probe-do-report.json', 'source_report_sha256'),
        ('probe-do-lifecycle.json', 'source_lifecycle_sha256'),
        ('source-run.json', 'source_run_metadata_sha256'),
    ):
        if digest(directory / filename) != provenance[key]:
            raise ValueError('Original evidence changed during collection')
    if (report.get('collection_provenance') != provenance
            or report.get('source_sha') != provenance['source_sha']
            or workload_digest(report) != provenance['workload_sha256']):
        raise ValueError('Collection changed workload or source identity')
    # Compute the gates again from request-level evidence, never trust saved
    # gate strings supplied by an artifact.
    from run_static_search_do_probe import summarize
    summarize(report)
    checkpoint(directory / 'probe-do-report.json', report)
    return report, phase_passed(report, lifecycle)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('identify', 'prepare', 'verify'))
    parser.add_argument('--run-id', default='')
    parser.add_argument('--run-json', type=Path, default=Path('source-do-run.json'))
    parser.add_argument('--source-dir', type=Path, default=Path('source-do-artifact'))
    parser.add_argument('--output-dir', type=Path, default=Path('do-collection'))
    args = parser.parse_args(argv)
    try:
        if args.action == 'identify':
            identity = identify(read_json(args.run_json), args.run_id,
                                os.environ.get('GITHUB_REPOSITORY', ''))
            with open(os.environ['GITHUB_OUTPUT'], 'a') as output:
                output.write('artifact_name=' + identity['artifact_name'] + '\n')
                output.write('script_name=' + identity['script_name'] + '\n')
        elif args.action == 'prepare':
            prepare(args.source_dir, args.run_json, args.run_id,
                    os.environ.get('GITHUB_REPOSITORY', ''),
                    os.environ.get('CLOUDFLARE_ACCOUNT_ID', ''),
                    os.environ.get('GITHUB_SHA', ''), args.output_dir)
        else:
            report, passed = verify_result(args.output_dir)
            for key in ('functional_gate', 'gateway_cpu_gate', 'do_cpu_gate',
                        'latency_gate', 'sample_gate', 'runtime_gate'):
                print(key + ':', report.get(key, 'unverified'))
            return 0 if passed else 1
    except (ValueError, OSError, KeyError, TypeError) as exc:
        parser.exit(1, str(exc) + '\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
