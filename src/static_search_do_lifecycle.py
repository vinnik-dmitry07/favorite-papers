'''Create evidence and remove only an isolated Durable Object probe namespace.

Namespace lifecycle follows the supported declarative exports flow. The namespace
is deleted and its absence is verified before the Worker script is removed.
'''

import argparse
import hashlib
import http.client
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import time
import urllib.error
import urllib.request


PREFIX = 'key-papers-static-do-probe-'
CLASS_NAME = 'StaticSearchProbe'
ROOT = Path(__file__).resolve().parents[1]


def validate_name(name):
    if not re.fullmatch(PREFIX + r'[1-9][0-9]*-[1-9][0-9]*', name):
        raise ValueError('Only a run-specific Durable Object probe is allowed')
    return name


class Cloudflare:
    def __init__(self):
        self.account = os.environ.get('CLOUDFLARE_ACCOUNT_ID', '')
        self.token = os.environ.get('CLOUDFLARE_API_TOKEN', '')
        if not re.fullmatch(r'[a-fA-F0-9]{32}', self.account) or not self.token:
            raise ValueError('Cloudflare credentials are missing or malformed')

    def request(self, path, method='GET', allow_absent=False):
        request = urllib.request.Request(
            f'https://api.cloudflare.com/client/v4/accounts/{self.account}'
            + path, method=method,
            headers={'authorization': f'Bearer {self.token}'})
        for attempt in range(3):
            try:
                try:
                    response = urllib.request.urlopen(request, timeout=20)
                except urllib.error.HTTPError as exc:
                    response = exc
                with response:
                    status = response.status
                    raw = response.read().decode()
                try:
                    body = json.loads(raw) if raw.strip() else {}
                except ValueError:
                    body = {}
                errors = body.get('errors') if isinstance(body, dict) else None
                # Cloudflare may serialize an empty errors collection as null.
                # Other non-list values are malformed, even if they are falsy.
                valid_errors = errors is None or isinstance(errors, list)
                error_items = errors if isinstance(errors, list) else []
                codes = [item['code'] for item in error_items
                         if isinstance(item, dict)
                         and isinstance(item.get('code'), int)
                         and not isinstance(item['code'], bool)]
                if (200 <= status < 300 and isinstance(body, dict)
                        and valid_errors and not error_items
                        and (body.get('success') is True
                             or (method == 'DELETE' and not raw))):
                    return body
                if (allow_absent and status == 404 and valid_errors and codes
                        and len(codes) == len(error_items)
                        and set(codes) <= {10007, 10090}):
                    return None
                message = f'Cloudflare HTTP {status}; error codes: {codes}'
                if not valid_errors:
                    message += '; malformed errors field'
                if status != 429 and status < 500:
                    raise ValueError(message)
            except (OSError, http.client.HTTPException) as exc:
                message = 'Cloudflare network error: ' + type(exc).__name__
            if attempt < 2:
                time.sleep(attempt + 1)
        raise ValueError(message)

    def namespaces(self):
        rows = []
        for page in range(1, 21):
            body = self.request('/workers/durable_objects/namespaces'
                                f'?page={page}&per_page=1000')
            batch = body.get('result')
            if not isinstance(batch, list):
                raise ValueError('Namespace list is missing its result array')
            for row in batch:
                if (not isinstance(row, dict) or not row.get('id')
                        or not isinstance(row.get('script'), str)
                        or not row.get('class')):
                    raise ValueError('Malformed namespace record')
            rows.extend(batch)
            info = body.get('result_info') or {}
            if not isinstance(info, dict):
                raise ValueError('Invalid namespace pagination metadata')
            total_pages = info.get('total_pages')
            if total_pages is not None:
                if (total_pages == 0 and page == 1 and not batch
                        and info.get('total_count', 0) == 0):
                    return rows
                if not isinstance(total_pages, int) or total_pages < page:
                    raise ValueError('Invalid namespace pagination')
                if page == total_pages:
                    return rows
            elif len(batch) < 1000:
                return rows
        raise ValueError('Namespace pagination exceeded the bounded scan')


def checkpoint(path, report):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + '.tmp')
    temp.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    temp.replace(path)


def matching(rows, name):
    return [row for row in rows if row.get('script') == name]


def owned_namespace(rows, name):
    matches = matching(rows, name)
    if len(matches) != 1 or matches[0].get('class') != CLASS_NAME:
        raise ValueError('Expected exactly one owned StaticSearchProbe namespace')
    row = matches[0]
    if row.get('use_sqlite') is not True:
        raise ValueError('The probe namespace must use SQLite on Workers Free')
    return {key: row[key] for key in ('id', 'script', 'class', 'use_sqlite')}


def preflight(api, name):
    validate_name(name)
    leftovers = [row for row in api.namespaces()
                 if str(row.get('script', '')).startswith(PREFIX)]
    if leftovers:
        scripts = sorted({str(row.get('script')) for row in leftovers})
        raise ValueError('Previous DO probe cleanup is incomplete: '
                         + ', '.join(scripts))
    return {'name': name, 'phase': 'preflight', 'preflight': 'passed',
            'namespace': None, 'cleanup': 'not_started',
            'source_sha': os.environ.get('GITHUB_SHA', ''),
            'account_fingerprint': hashlib.sha256(
                api.account.encode()).hexdigest()}


def capture(api, name, report):
    validate_name(name)
    if report.get('name') != name or report.get('preflight') != 'passed':
        raise ValueError('A matching successful preflight checkpoint is required')
    for attempt in range(4):
        rows = api.namespaces()
        if matching(rows, name) or attempt == 3:
            report['namespace'] = owned_namespace(rows, name)
            break
        time.sleep(2)
    report['phase'] = 'captured'
    return report


def migration_files(directory, name):
    validate_name(name)
    directory = Path(directory)
    entry = directory / 'cleanup.mjs'
    entry.write_text('export default { fetch() { return new Response('
                     '"Probe removed", { status: 410 }); } };\n',
                     encoding='utf-8')
    config = directory / 'wrangler.cleanup.toml'
    config.write_text(
        f'name = "{name}"\nmain = "cleanup.mjs"\n'
        'compatibility_date = "2026-10-15"\nworkers_dev = false\n'
        f'[exports.{CLASS_NAME}]\ntype = "durable-object"\n'
        'state = "deleted"\n', encoding='utf-8')
    return config


def delete_class(name, log_path):
    binary = ROOT / 'worker/node_modules/.bin/wrangler'
    if not binary.exists():
        raise ValueError('Pinned Wrangler is required to remove the DO class')
    with tempfile.TemporaryDirectory(prefix='do-probe-cleanup-') as directory:
        config = migration_files(directory, name)
        with Path(log_path).open('w', encoding='utf-8') as log:
            result = subprocess.run(
                [str(binary), 'deploy', '--config', str(config), '--name', name],
                cwd=ROOT / 'worker', stdout=log, stderr=subprocess.STDOUT,
                timeout=180, check=False)
        if result.returncode:
            raise ValueError('DO class deletion migration failed; see cleanup log')


def cleanup(api, name, report, path, log_path):
    validate_name(name)
    if report.get('name') != name or report.get('preflight') != 'passed':
        raise ValueError('Cleanup requires this run\'s preflight checkpoint')
    rows = api.namespaces()
    owned = matching(rows, name)
    captured = report.get('namespace')
    if captured:
        # A saved ID must never silently follow a renamed/transferred namespace.
        collisions = [row for row in rows if row['id'] == captured.get('id')
                      and row.get('script') != name]
        if collisions:
            raise ValueError('Captured namespace ownership has changed')
    if owned:
        current = owned_namespace(rows, name)
        if captured and current['id'] != captured.get('id'):
            raise ValueError('Namespace ID changed after capture')
        report['namespace'] = current
        report['cleanup'] = 'deleting_class'
        checkpoint(path, report)
        delete_class(name, log_path)
        for attempt in range(6):
            remaining = api.namespaces()
            if not any(row['id'] == current['id'] or row.get('script') == name
                       for row in remaining):
                break
            if attempt == 5:
                raise ValueError('Namespace still exists after deletion migration')
            time.sleep(2)
    report['namespace_absent'] = True
    report['cleanup'] = 'deleting_worker'
    checkpoint(path, report)
    # No force flag: any undeleted class must block deletion at the provider.
    api.request('/workers/scripts/' + name, method='DELETE', allow_absent=True)
    report['cleanup'] = 'passed'
    report['phase'] = 'removed'
    checkpoint(path, report)
    return report


def phase_passed(measurement, cleanup_report):
    return (measurement.get('phase_complete') is True
            and measurement.get('sample_gate') == 'passed'
            and cleanup_report.get('cleanup') == 'passed'
            and cleanup_report.get('namespace_absent') is True)


def validate_pilot(directory, run_file, run_id, account):
    if not re.fullmatch(r'[1-9][0-9]*', run_id):
        raise ValueError('A numeric previous pilot run ID is required')
    source = os.environ.get('GITHUB_SHA', '')
    repository = os.environ.get('GITHUB_REPOSITORY', '')
    if not re.fullmatch(r'[a-f0-9]{40}', source) or not repository:
        raise ValueError('Pilot verification requires GitHub run identity')
    run = json.loads(Path(run_file).read_text(encoding='utf-8'))
    if (str(run.get('id')) != run_id or run.get('head_sha') != source
            or run.get('repository', {}).get('full_name') != repository
            or run.get('path') != '.github/workflows/agent-api.yml'
            or run.get('event') != 'workflow_dispatch'
            or run.get('conclusion') != 'success'
            or run.get('status') != 'completed'):
        raise ValueError('Pilot must be a successful Agent API run at this SHA')
    matches = []
    for path in Path(directory).rglob('probe-do-lifecycle.json'):
        report_path = path.with_name('probe-do-report.json')
        if not report_path.exists():
            continue
        lifecycle = json.loads(path.read_text(encoding='utf-8'))
        report = json.loads(report_path.read_text(encoding='utf-8'))
        expected_name = PREFIX + run_id + '-' + str(run.get('run_attempt'))
        if (lifecycle.get('name') == expected_name
                and lifecycle.get('source_sha') == source
                and lifecycle.get('account_fingerprint') == hashlib.sha256(
                    account.encode()).hexdigest()
                and lifecycle.get('cleanup') == 'passed'
                and lifecycle.get('namespace_absent') is True
                and report.get('source_sha') == source
                and report.get('script_name') == expected_name
                and report.get('phase') == 'pilot'
                and report.get('phase_complete') is True
                and report.get('preflight_gate') == 'passed'
                and report.get('sample_gate') == 'passed'):
            matches.append(path)
    if len(matches) != 1:
        raise ValueError('Exactly one completed pilot with verified cleanup is required')
    return {'pilot_run_id': run_id, 'pilot_source_sha': source,
            'pilot_verified': True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['preflight', 'capture', 'cleanup', 'validate-pilot'])
    parser.add_argument('name')
    parser.add_argument('--report', default='probe-do-lifecycle.json')
    parser.add_argument('--cleanup-log', default='probe-do-cleanup.txt')
    parser.add_argument('--pilot-dir', default='previous-do-pilot')
    parser.add_argument('--pilot-run-json', default='previous-do-pilot-run.json')
    parser.add_argument('--pilot-run-id', default='')
    args = parser.parse_args()
    report = {'name': args.name, 'phase': args.action}
    try:
        validate_name(args.name)
        api = Cloudflare()
        if args.action == 'validate-pilot':
            validate_pilot(args.pilot_dir, args.pilot_run_json,
                           args.pilot_run_id, api.account)
            print('Previous pilot telemetry and namespace cleanup verified')
            return
        if args.action == 'preflight':
            report = preflight(api, args.name)
        else:
            report = json.loads(Path(args.report).read_text(encoding='utf-8'))
            if args.action == 'capture':
                report = capture(api, args.name, report)
            else:
                report = cleanup(api, args.name, report, args.report,
                                 args.cleanup_log)
        checkpoint(args.report, report)
    except (ValueError, OSError, subprocess.TimeoutExpired) as exc:
        report['error'] = str(exc)
        report[args.action] = 'failed'
        checkpoint(args.report, report)
        parser.exit(1, str(exc) + '\n')
    print(f'{args.name}: {args.action} passed')


if __name__ == '__main__':
    main()
