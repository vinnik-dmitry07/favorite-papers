'''Live checks against a deployed worker. Writes smoke.json only on success.'''

from __future__ import annotations

import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_agent_index import DEFAULT_OUT, SMOKE_PATH  # noqa: E402


def _read(request: urllib.request.Request) -> tuple[int, str]:
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return response.status, response.read().decode('utf-8')
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode('utf-8')


def _get(url: str) -> tuple[int, str]:
    return _read(urllib.request.Request(url, headers={'accept': 'application/json'}))


def _post(url: str, payload: dict) -> tuple[int, str]:
    data = json.dumps(payload).encode('utf-8')
    request = urllib.request.Request(
        url,
        data=data,
        headers={
            'content-type': 'application/json',
            'accept': 'application/json, text/event-stream',
        },
        method='POST',
    )
    return _read(request)


def smoke(origin: str, graph_path: Path) -> dict:
    graph = json.loads(graph_path.read_text(encoding='utf-8'))
    nodes = graph['nodes']
    doi = next(node_id for node_id in nodes if node_id.startswith('doi:') and '/' in node_id)
    missing_text = next(
        node_id for node_id, node in nodes.items() if not node['text']['available']
    )
    checks = {}
    status, health_text = _get(f'{origin}/health')
    health = json.loads(health_text)
    checks['health'] = status == 200 and health.get('status') == 'ready'
    status, spec_text = _get(f'{origin}/openapi.json')
    spec = json.loads(spec_text)
    checks['openapi'] = (
        status == 200
        and spec.get('openapi') == '3.1.0'
        and spec.get('security') == []
        and spec.get('servers', [{}])[0].get('url') == origin
    )
    status, paper_text = _get(f'{origin}/v1/paper?id={urllib.parse.quote(doi, safe="")}')
    checks['doi'] = status == 200 and json.loads(paper_text).get('id') == doi
    status, web_text = _get(
        f'{origin}/v1/paper?id={urllib.parse.quote(missing_text, safe="")}',
    )
    web = json.loads(web_text)
    checks['missing_text'] = status == 200 and web.get('text', {}).get('available') is False
    status, unknown_text = _get(f'{origin}/v1/paper?id=arxiv:does-not-exist')
    checks['unknown'] = status == 404 and 'unknown_id' in unknown_text
    status, cite_text = _get(f'{origin}/v1/citations?id={urllib.parse.quote(doi, safe="")}')
    checks['citations'] = status == 200
    status, walk_text = _get(f'{origin}/v1/traverse?id={urllib.parse.quote(doi, safe="")}')
    checks['traverse'] = status == 200
    version = json.loads(cite_text).get('corpus_version')
    content_url = (
        f'{origin}/v1/content?id={urllib.parse.quote(doi, safe="")}'
        f'&version={urllib.parse.quote(version or "", safe="")}'
    )
    status, content_text = _get(content_url)
    checks['content'] = status == 200 and 'Describe the issue below' not in content_text
    status, search_text = _get(f'{origin}/v1/search?q=attention&k=1')
    checks['search'] = status == 200 and 'hits' in search_text
    status, mcp_text = _post(f'{origin}/mcp', {
        'jsonrpc': '2.0',
        'id': 1,
        'method': 'initialize',
        'params': {
            'protocolVersion': '2025-06-18',
            'capabilities': {},
            'clientInfo': {'name': 'smoke', 'version': '0'},
        },
    })
    checks['mcp'] = status == 200 and 'key-papers' in mcp_text
    return {'ok': all(checks.values()), 'origin': origin, 'checks': checks}


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args:
        raise SystemExit('usage: smoke_agent_api.py https://<name>.workers.dev')
    origin = args[0].rstrip('/')
    graph = DEFAULT_OUT / 'graph.json'
    if not graph.is_file():
        raise SystemExit('agent_build/graph.json is missing; build the release first')
    report = smoke(origin, graph)
    print(json.dumps(report['checks'], sort_keys=True))
    if not report['ok']:
        print('smoke failed')
        return 1
    SMOKE_PATH.parent.mkdir(parents=True, exist_ok=True)
    SMOKE_PATH.write_text(
        json.dumps({'ok': True, 'origin': origin}, sort_keys=True) + '\n',
        encoding='utf-8',
    )
    print(f'smoke ok {origin}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
