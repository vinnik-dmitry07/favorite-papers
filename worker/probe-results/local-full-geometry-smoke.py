import hashlib
import http.client
import json
import os
from pathlib import Path
import signal
import socket
import subprocess
import sys
import time
import urllib.parse
import uuid
from datetime import datetime, timedelta, timezone

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'src'))
import run_full_geometry_probe as runner

HOST = '127.0.0.1'
PORT = 8789
TOKEN = 'local-only-geometry-test-token-no-cloudflare-access'
OUT = Path('/tmp/full-geometry-local-report.json')
LOG = Path('/tmp/full-geometry-local-workerd.log')

def local_exchange(url, payload, headers, timeout):
    parsed = urllib.parse.urlsplit(url)
    if (parsed.scheme, parsed.hostname, parsed.port) != ('http', HOST, PORT):
        raise ValueError('Local harness blocks every nonlocal target')
    connection = http.client.HTTPConnection(HOST, PORT, timeout=timeout)
    body = None if payload is None else json.dumps(payload).encode()
    try:
        connection.request('GET' if body is None else 'POST',
                           urllib.parse.urlunsplit(('', '', parsed.path, parsed.query, '')),
                           body=body, headers={
                               'accept': 'application/json, text/event-stream',
                               'content-type': 'application/json',
                               'mcp-protocol-version': '2025-06-18', **headers,
                           })
        response = connection.getresponse()
        raw = response.read(runner.MAX_RESPONSE_BYTES + 1)
        runner.require(len(raw) <= runner.MAX_RESPONSE_BYTES, 'Response exceeds byte budget')
        return response.status, dict(response.getheaders()), raw.decode('utf-8')
    finally:
        connection.close()

runner.exchange = local_exchange
identity, nodes, papers = runner.read_fixture(ROOT / 'agent_geometry_probe')
report = {
    'schema_version': 1, 'probe_type': 'full-geometry-local-workerd-smoke',
    'synthetic': True, 'run_id': str(uuid.uuid4()),
    'origin': f'http://{HOST}:{PORT}', 'identity': identity,
    'started_ms': int(time.time() * 1000), 'requests': [],
    'http_attempts': 0, 'workload_complete': False,
    'max_load_seconds': 300, 'max_http_attempts': runner.MAX_REQUESTS,
    'output_path': str(OUT), 'local_simulation_only': True,
}
runner.persist(report)
env = {key: value for key, value in os.environ.items()
       if not key.startswith(('CLOUDFLARE_', 'CF_'))}
env['WRANGLER_SEND_METRICS'] = 'false'
env['NO_PROXY'] = '127.0.0.1,localhost'
args = [str(ROOT / 'worker/node_modules/.bin/wrangler'), 'dev', '--local',
        '--config', 'wrangler.geometry-probe.toml', '--ip', HOST,
        '--port', str(PORT), '--inspector-port', '9239',
        '--persist-to', '/tmp/full-geometry-local-state',
        '--var', 'PROBE_TOKEN:' + TOKEN,
        '--var', 'PROBE_MANIFEST_SHA:' + identity['manifest_sha256'],
        '--var', 'PROBE_EXPIRES_AT:' + (datetime.now(timezone.utc) + timedelta(minutes=10)).isoformat()]
with LOG.open('w') as log:
    process = subprocess.Popen(args, cwd=ROOT / 'worker', env=env, stdout=log,
                               stderr=subprocess.STDOUT, start_new_session=True)
    try:
        ready_deadline = time.monotonic() + 90
        while time.monotonic() < ready_deadline:
            if process.poll() is not None:
                raise RuntimeError('Wrangler exited before startup')
            try:
                with socket.create_connection((HOST, PORT), timeout=0.5):
                    break
            except OSError:
                time.sleep(0.25)
        else:
            raise RuntimeError('Wrangler startup timed out')
        print('Local workerd ready; running 324 workload requests plus 3 controls.', flush=True)
        runner.run_workload(report, TOKEN, nodes, papers, time.monotonic() + 300)
    except Exception as exc:
        report['error'] = type(exc).__name__ + ': ' + str(exc)
    finally:
        report['finished_ms'] = int(time.time() * 1000)
        runner.summarize(report)
        runner.persist(report)
        try:
            os.killpg(process.pid, signal.SIGTERM)
        except ProcessLookupError:
            pass
        try:
            process.wait(timeout=10)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGKILL)
            process.wait(timeout=5)
print(json.dumps({key: report.get(key) for key in (
    'functional_gate', 'workload_complete', 'http_attempts', 'error', 'identity',
    'gateway_cpu_gate', 'do_cpu_gate', 'memory_gate', 'boot_ids')}, indent=2))
print('phases=' + json.dumps(report['phases']))
print('report=' + str(OUT))
sys.exit(0 if report['functional_gate'] == 'passed' and report['workload_complete'] else 1)
