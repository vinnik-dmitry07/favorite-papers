'''Publish small, linked HTML/JSON documents for agents without JavaScript.

Run after staging the map: python src/build_agent_pages.py --out site
Only derived files under site/agents and site/llms.txt are written.
'''

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import shutil
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

from build_agent_index import clean_markdown, strip_banner, validate_edges
from common import FULLTEXT_DIR, GRAPH, ROOT, safe_key

SITE_URL = 'https://vinnik-dmitry07.github.io/favorite-papers'
PAGE_SIZE = 24
TEXT_SIZE = 16000
STYLE = ('body{max-width:72rem;margin:2rem auto;padding:0 1rem;'
         'font:18px/1.6 system-ui;color:#222}a{color:#174ea6}'
         'pre{white-space:pre-wrap;overflow-wrap:anywhere;'
         'font:16px/1.6 ui-monospace,monospace}'
         'li{margin:.6rem 0}nav{margin:1rem 0}code{overflow-wrap:anywhere}')


def slug(paper_id: str) -> str:
    return hashlib.sha256(paper_id.encode('utf-8')).hexdigest()


def escape(value: object) -> str:
    return html.escape(str(value), quote=True)


def link(url: str, label: object) -> str:
    return f'<a href="{escape(url)}">{escape(label)}</a>'


def source_link(url: str | None) -> str:
    if url and urlparse(url).scheme in ('https', 'http'):
        return link(url, 'Original source')
    return 'Original source unavailable'


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, separators=(',', ':'))
                    + '\n', encoding='utf-8')


def write_page(path: Path, title: str, body: str, site_url: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    home = link(site_url + '/agents/', 'Catalog / agent guide')
    page = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{escape(title)}</title><style>{STYLE}</style></head>'
            f'<body><nav>{home}</nav><main><h1>{escape(title)}</h1>{body}'
            '</main></body></html>')
    path.write_text(page, encoding='utf-8')


def text_parts(text: str) -> list[tuple[int, int]]:
    '''Bound response size without dropping or duplicating any code points.'''
    ranges = []
    start = 0
    while start < len(text):
        end = min(len(text), start + TEXT_SIZE)
        if end < len(text):
            boundary = text.rfind('\n\n', start + TEXT_SIZE // 2, end)
            if boundary >= 0:
                end = boundary + 2
        ranges.append((start, end))
        start = end
    return ranges


def headings(text: str) -> list[dict]:
    return [{'title': match.group(2).strip(), 'offset': match.start(),
             'level': len(match.group(1))}
            for match in re.finditer(r'^(#{1,6})\s+(.+)$', text, re.M)]


def verified_origin(discovery: Path | None) -> str:
    '''Recheck the successful API artifact before advertising its endpoint.'''
    from write_discovery_links import valid_origin

    if not discovery or not discovery.is_file():
        return ''
    try:
        report = json.loads(discovery.read_text(encoding='utf-8'))
        origin = report.get('origin', '')
        if report.get('ok') is not True or not valid_origin(origin):
            return ''
        with urllib.request.urlopen(origin.rstrip('/') + '/health', timeout=15) as response:
            health = json.load(response)
        return origin.rstrip('/') if health.get('status') == 'ready' else ''
    except (OSError, ValueError, urllib.error.URLError):
        print('API discovery unavailable; publishing the static catalog without an API link')
        return ''


def build_pages(graph: dict, texts: dict[str, str | None], out: Path,
                site_url: str = SITE_URL, api_origin: str = '') -> dict:
    nodes = {node['id']: node for node in graph['nodes']}
    edges = validate_edges(graph['nodes'], graph['edges'])
    root = out / 'agents'
    if root.exists():
        shutil.rmtree(root)
    root.mkdir(parents=True)
    base = site_url.rstrip('/')
    outgoing = {key: [] for key in nodes}
    incoming = {key: [] for key in nodes}
    for edge in edges:
        outgoing[edge['source']].append(edge)
        incoming[edge['target']].append(edge)

    def paper_url(key: str) -> str:
        return f'{base}/agents/papers/{slug(key)}/'

    cards = []
    for key, node in nodes.items():
        text = clean_markdown(texts.get(key) or '')
        cards.append({field: node.get(field) for field in
                      ('id', 'title', 'date', 'section', 'quality')} | {
                          'url': paper_url(key), 'source_url': node.get('url'),
                          'text_available': bool(text.strip()),
                      })
    cards.sort(key=lambda item: (item['title'].casefold(), item['id']))
    grouped = {'All papers': cards}
    for card in cards:
        grouped.setdefault(card['section'] or 'Uncategorized', []).append(card)
    index_links = []
    for group_index, (section, group) in enumerate(grouped.items()):
        prefix = f'catalog-{group_index}'
        paths = [f'{prefix}-{i // PAGE_SIZE + 1}.html'
                 for i in range(0, max(1, len(group)), PAGE_SIZE)]
        index_links.append('<li>' + link(paths[0], f'{section} ({len(group)})')
                           + '</li>')
        for page_index, filename in enumerate(paths):
            page_cards = group[page_index * PAGE_SIZE:(page_index + 1) * PAGE_SIZE]
            nav = ' | '.join(link(path, f'Page {i + 1}')
                             for i, path in enumerate(paths))
            rows = []
            for card in page_cards:
                status = 'text available' if card['text_available'] else 'metadata only'
                rows.append('<li>' + link(card['url'], card['title'])
                            + f'<br><code>{escape(card["id"])}</code> · '
                            + escape(card['date'] or 'date unknown')
                            + f' · {status}</li>')
            json_name = filename.replace('.html', '.json')
            write_json(root / json_name, {
                'total': len(group), 'papers': page_cards,
                'next': base + '/agents/' + paths[page_index + 1]
                if page_index + 1 < len(paths) else None,
            })
            write_page(root / filename, f'{section} — page {page_index + 1}',
                       f'<nav>{nav}</nav><ul>{"".join(rows)}</ul>'
                       + link(json_name, 'This page as JSON'), base)

    for card in cards:
        key = card['id']
        node = nodes[key]
        directory = root / 'papers' / slug(key)
        directory.mkdir(parents=True)
        raw = texts.get(key)
        cleaned = clean_markdown(raw or '')
        ranges = text_parts(cleaned) if cleaned.strip() else []
        toc = headings(cleaned)
        parts = []
        for number, (start, end) in enumerate(ranges, 1):
            filename = f'part-{number}.html'
            parts.append({'start': start, 'end': end,
                          'url': paper_url(key) + filename})
            nav = [link('./', 'Paper and contents')]
            if number > 1:
                nav.append(link(f'part-{number - 1}.html', 'Previous part'))
            if number < len(ranges):
                nav.append(link(f'part-{number + 1}.html', 'Next part'))
            write_page(directory / filename,
                       f'{node["title"]} — part {number}/{len(ranges)}',
                       '<nav>' + ' | '.join(nav) + '</nav>'
                       + f'<p>Cleaned-text code points [{start}, {end}). '
                       + 'Bibliography omitted here; source.md includes it.</p>'
                       + f'<pre id="text">{escape(cleaned[start:end])}</pre>'
                       + '<nav>' + ' | '.join(nav) + '</nav>', base)
        for heading in toc:
            part = next(p for p in parts if p['start'] <= heading['offset'] < p['end'])
            heading['url'] = part['url'] + '#text'
        if raw:
            (directory / 'source.md').write_text(strip_banner(raw), encoding='utf-8')
        if ranges:
            (directory / 'text.md').write_text(cleaned, encoding='utf-8')
        neighbors = {}
        for direction, adjacency in [('out', outgoing[key]), ('in', incoming[key])]:
            label = 'Cites' if direction == 'out' else 'Cited by'
            items = []
            for edge in adjacency:
                other = edge['target'] if direction == 'out' else edge['source']
                items.append(edge | {'id': other, 'title': nodes[other]['title'],
                                     'url': paper_url(other)})
            neighbors[direction] = items
            pages = max(1, (len(items) + PAGE_SIZE - 1) // PAGE_SIZE)
            for page in range(1, pages + 1):
                current = items[(page - 1) * PAGE_SIZE:page * PAGE_SIZE]
                rows = ['<li>' + link(item['url'], item['title'])
                        + f'<br><code>{escape(item["id"])}</code> · evidence: '
                        + escape(item['evidence']) + '</li>' for item in current]
                nav = ' | '.join(link(f'{direction}-{p}.html', f'Page {p}')
                                 for p in range(1, pages + 1))
                write_page(directory / f'{direction}-{page}.html',
                           f'{label}: {node["title"]}',
                           f'<p>{len(items)} citation edges inside this catalog. '
                           'A title match is weaker evidence than an identifier match. '
                           'Zero entries does not mean no citations on the web.</p>'
                           + f'<nav>{nav}</nav><ul>{"".join(rows)}</ul>'
                           + link('./', 'Back to paper'), base)
        summary = card | {'authors': node.get('authors', []),
                          'outgoing': neighbors['out'], 'incoming': neighbors['in'],
                          'text_parts': parts, 'contents': toc,
                          'text_code_points': len(cleaned),
                          'source_markdown': paper_url(key) + 'source.md' if raw else None}
        write_json(directory / 'paper.json', summary)
        body = (f'<p><code>{escape(key)}</code></p><p>'
                + source_link(node.get('url')) + ' · '
                + link('paper.json', 'Paper JSON') + '</p><p>'
                + escape(node.get('section') or '') + ' · '
                + escape(node.get('date') or 'date unknown') + '</p><p>'
                + link('out-1.html', f'Cites ({len(outgoing[key])})') + ' · '
                + link('in-1.html', f'Cited by ({len(incoming[key])})') + '</p>')
        if parts:
            body += ('<p>' + link('text.md', 'Complete cleaned Markdown') + ' · '
                     + link('source.md', 'Source Markdown including bibliography')
                     + '</p><h2>Read in parts</h2><ol>'
                     + ''.join('<li>' + link(p['url'], f'Part {i + 1}') + '</li>'
                               for i, p in enumerate(parts)) + '</ol><h2>Contents</h2><ul>'
                     + ''.join('<li>' + link(h['url'], h['title']) + '</li>' for h in toc)
                     + '</ul>')
        else:
            body += '<p>Full text is unavailable in this snapshot. Follow the original source.</p>'
        write_page(directory / 'index.html', node['title'], body, base)

    api_html = ('<p>' + link(api_origin, 'Verified REST / MCP API') + ' · '
                + link(api_origin + '/openapi.json', 'OpenAPI') + '</p>'
                if api_origin else '<p>No verified API deployment is linked. '
                'Catalog navigation and text below work without the API.</p>')
    intro = ('<p>Read this catalog without JavaScript, login, or a repository clone. '
             'Open a catalog section, select a paper, then follow Cites, Cited by, '
             'or its text parts. Every page contains ordinary links.</p>'
             f'<p>{len(nodes)} records; {sum(c["text_available"] for c in cards)} with text; '
             f'{len(edges)} citation edges inside the catalog. '
             'Missing text and missing citation edges are not evidence of absence.</p>'
             '<p>For exact titles, browse the appropriate section or alphabetical catalog. '
             'Semantic search needs the API and is separate from this static catalog.</p>')
    example_id = 'arxiv:2402.03300'
    if example_id in nodes:
        intro += ('<p>Example: ' + link(paper_url(example_id), 'DeepSeekMath')
                  + ' → Cited by → open a citing paper → read its text parts.</p>')
    write_page(root / 'index.html', 'Paper catalog for agents',
               intro + api_html + '<ul>' + ''.join(index_links) + '</ul>', base)
    write_json(root / 'graph.json', {'nodes': cards, 'edges': edges})
    guide = ('# Favorite papers\n\n'
             f'- [Agent guide and catalog]({base}/agents/)\n'
             f'- [Alphabetical catalog, page 1]({base}/agents/catalog-0-1.html)\n\n'
             'Open a paper link to obtain its canonical id, source URL, text parts, '
             'and links to all incoming/outgoing catalog citations. '
             'Follow pagination links; do not infer completeness from the first page. '
             'Paper JSON and source Markdown are linked on each paper page. '
             'Edges mean source cites target. Title-matched edges are weaker evidence.\n')
    if api_origin:
        guide += (f'\n- [Verified API manual]({api_origin}/)\n'
                  f'- [OpenAPI]({api_origin}/openapi.json)\n'
                  f'- MCP endpoint: {api_origin}/mcp\n')
    (out / 'llms.txt').write_text(guide, encoding='utf-8')
    return {'papers': len(cards), 'with_text': sum(c['text_available'] for c in cards),
            'edges': len(edges), 'html_pages': len(list(root.rglob('*.html')))}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=ROOT / 'site')
    parser.add_argument('--api-origin', default='')
    parser.add_argument('--discovery', type=Path,
                        help='Successful API smoke artifact; its health is rechecked')
    args = parser.parse_args()
    if args.api_origin:
        from write_discovery_links import valid_origin
        if not valid_origin(args.api_origin):
            parser.error('--api-origin must be a verified https workers.dev origin')
    graph = json.loads(GRAPH.read_text(encoding='utf-8'))
    texts = {}
    for node in graph['nodes']:
        path = FULLTEXT_DIR / f'{safe_key(node["id"])}.md'
        texts[node['id']] = path.read_text(encoding='utf-8') if path.is_file() else None
    origin = args.api_origin or verified_origin(args.discovery)
    print(json.dumps(build_pages(graph, texts, args.out, api_origin=origin)))


if __name__ == '__main__':
    main()
