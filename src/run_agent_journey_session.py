'''Keep the local API and its interactive client in one network namespace.

Run with ``python -u -i``; evaluators use only ``get`` or ``rpc`` in the REPL.
The launched Node adapter enforces the measurement's call and response limits.
'''

import argparse
import atexit
import http.client
import json
from pathlib import Path
import subprocess
import urllib.parse


def arguments():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--session', required=True)
    parser.add_argument('--sessions', required=True, type=Path)
    parser.add_argument('--bundle', required=True, type=Path)
    parser.add_argument('--out', required=True, type=Path)
    parser.add_argument('--manifest-sha', required=True)
    parser.add_argument('--port', type=int, default=8765)
    parser.add_argument('--retained-reading', action='store_true',
                        help='Replay live search bodies, then local reading only')
    return parser.parse_args()


OPTIONS = arguments()
ROOT = Path(__file__).resolve().parents[1]
SERVER = subprocess.Popen(
    [
        'node', str(OPTIONS.bundle.resolve()),
        '--assets', str(ROOT / 'full-probe-reports/replay/runtime'),
        '--manifest-sha', OPTIONS.manifest_sha,
        '--query-vectors',
        str(ROOT / 'full-probe-reports/replay/query-vectors.f32'),
        '--query-metadata',
        str(ROOT / 'full-probe-reports/replay/query-vectors.f32.json'),
        '--sessions', str(OPTIONS.sessions.resolve()),
        '--out', str(OPTIONS.out.resolve()),
        '--port', str(OPTIONS.port),
        *(['--retained-reading'] if OPTIONS.retained_reading else []),
    ],
    cwd=ROOT / 'worker', stdout=subprocess.PIPE, text=True,
)


def close():
    '''Close the evaluation server; called when the interactive client exits.'''
    if SERVER.poll() is None:
        SERVER.terminate()
        try:
            SERVER.wait(timeout=5)
        except subprocess.TimeoutExpired:
            SERVER.kill()
            SERVER.wait(timeout=5)


atexit.register(close)
READY = SERVER.stdout.readline()
if not READY:
    raise RuntimeError('Journey adapter exited before readiness')
print(READY, end='')


def request(method, path, parameters=None, body=None):
    '''Deliver an unchanged API body and budget counters to the agent.'''
    if not path.startswith('/') or '?' in path or '#' in path:
        raise ValueError('Use an endpoint path and a separate parameter dict')
    target = '/session/' + OPTIONS.session + path
    if parameters:
        target += '?' + urllib.parse.urlencode(parameters)
    connection = http.client.HTTPConnection(
        '127.0.0.1', OPTIONS.port, timeout=30,
    )
    headers = {'Content-Type': 'application/json'} if body else {}
    try:
        connection.request(method, target, body=body, headers=headers)
        response = connection.getresponse()
        payload = response.read().decode('utf-8')
        print(json.dumps({
            'http_status': response.status,
            'calls': response.getheader('x-journey-attempted-calls'),
            'delivered_code_points': response.getheader(
                'x-journey-delivered-code-points',
            ),
            'delivered_bytes': response.getheader('x-journey-delivered-bytes'),
        }))
        print(payload)
    finally:
        connection.close()


def get(path, parameters=None):
    request('GET', path, parameters)


def rpc(name, arguments, request_id=1):
    request('POST', '/mcp', body=json.dumps({
        'jsonrpc': '2.0', 'id': request_id, 'method': 'tools/call',
        'params': {'name': name, 'arguments': arguments},
    }))


print('Ready. Use get(path, parameters) or rpc(name, arguments).')
