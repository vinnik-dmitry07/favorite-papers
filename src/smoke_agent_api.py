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
            'mcp-protocol-version': '2025-06-18',
        },
        method='POST',
    )
    return _read(request)


def _rpc_result(text: str) -> dict:
    lines = [line[5:].strip() for line in text.splitlines() if line.startswith('data:')]
    envelope = json.loads(lines[-1] if lines else text)
    if envelope.get('error'):
        raise ValueError(f'MCP protocol error: {envelope["error"]}')
    return envelope['result']


def _tool(origin: str, name: str, arguments: dict) -> dict:
    status, text = _post(f'{origin}/mcp', {
        'jsonrpc': '2.0', 'id': 2, 'method': 'tools/call',
        'params': {'name': name, 'arguments': arguments},
    })
    result = _rpc_result(text)
    if status != 200 or result.get('isError'):
        raise ValueError(f'MCP tool failed: {name}: {result}')
    structured = result.get('structuredContent')
    if structured != json.loads(result['content'][0]['text']):
        raise ValueError(f'MCP content disagrees with structuredContent: {name}')
    return structured


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
    hits = json.loads(search_text).get('hits', [])
    checks['search'] = (status == 200 and bool(hits)
                        and all(hit['paper_id'] in nodes and hit['snippet'] for hit in hits))
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

    # Exercise the exact user journey that the original external-agent audit failed.
    key = 'arxiv:2402.03300'
    status, catalog_text = _get(f'{origin}/v1/catalog?q=DeepSeekMath')
    checks['title_lookup'] = status == 200 and key in {
        paper['id'] for paper in json.loads(catalog_text).get('papers', [])
    }
    seen = []
    cursor = None
    for _ in range(len(nodes) + 1):
        params = {'id': key, 'dir': 'in', 'limit': 24}
        if cursor:
            params['cursor'] = cursor
        status, page_text = _get(f'{origin}/v1/citations?' + urllib.parse.urlencode(params))
        if status != 200:
            break
        page = json.loads(page_text)
        seen.extend(item['id'] for item in page['neighbors'])
        cursor = page['next_cursor']
        if not cursor:
            break
    expected = {edge['source'] for edge in graph['in'][key]}
    checks['complete_incoming'] = (status == 200 and cursor is None
                                   and set(seen) == expected and len(seen) == len(expected))
    status, toc_text = _get(f'{origin}/v1/contents?id={key}')
    checks['contents'] = status == 200 and bool(json.loads(toc_text).get('sections'))
    status, found_text = _get(f'{origin}/v1/find?id={key}&q=64')
    found = json.loads(found_text)
    checks['find_in_paper'] = status == 200 and bool(found.get('matches'))
    if found.get('matches'):
        offset = found['matches'][0]['start']
        status, passage_text = _get(f'{origin}/v1/content?' + urllib.parse.urlencode({
            'id': key, 'offset': offset, 'length': 32000, 'version': found['corpus_version'],
        }))
        checks['read_at_match'] = status == 200 and json.loads(passage_text)['text'].startswith('64')
    status, listed_text = _post(f'{origin}/mcp', {
        'jsonrpc': '2.0', 'id': 2, 'method': 'tools/list',
    })
    listed = _rpc_result(listed_text).get('tools', [])
    names = {tool['name'] for tool in listed}
    checks['mcp_contract'] = (status == 200 and {'search', 'fetch', 'list_papers'} <= names
                              and all(tool.get('outputSchema') for tool in listed))
    results = _tool(origin, 'search', {'query': key})['results']
    document = _tool(origin, 'fetch', {'id': results[0]['id']}) if results else {}
    checks['mcp_search_fetch'] = (
        document.get('id') == results[0]['id'] if results else False
    ) and bool(document.get('text')) and document.get('metadata', {}).get('paper_id') == key
    return {'ok': all(checks.values()), 'origin': origin, 'checks': checks}


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args:
        raise SystemExit('usage: smoke_agent_api.py https://<name>.workers.dev')
    origin = args[0].rstrip('/')
    graph = DEFAULT_OUT / 'graph.json'
    if not graph.is_file():
        raise SystemExit('agent_build/graph.json is missing; build the release first')
    SMOKE_PATH.unlink(missing_ok=True)
    try:
        report = smoke(origin, graph)
    except (OSError, ValueError, KeyError, IndexError, TypeError) as exc:
        print(f'smoke failed: {exc}')
        return 1
    print(json.dumps(report['checks'], sort_keys=True))
    if not report['ok']:
        print('smoke failed')
        return 1
    SMOKE_PATH.parent.mkdir(parents=True, exist_ok=True)
    SMOKE_PATH.write_text(
        json.dumps(report, sort_keys=True) + '\n',
        encoding='utf-8',
    )
    print(f'smoke ok {origin}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
