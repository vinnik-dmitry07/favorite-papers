'''Verify the no-JavaScript research path, not just generated file counts.'''

import json
from html.parser import HTMLParser
from urllib.parse import unquote, urljoin, urlparse

from build_agent_index import clean_markdown
from build_agent_pages import SITE_URL, TEXT_SIZE, build_pages, slug, verified_origin


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.text = []
        self.in_pre = False

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.links.append(dict(attrs).get('href', ''))
        if tag == 'pre':
            self.in_pre = True

    def handle_endtag(self, tag):
        if tag == 'pre':
            self.in_pre = False

    def handle_data(self, data):
        if self.in_pre:
            self.text.append(data)


def fixture():
    ids = ['doi:10.example/a/b', 'url:missing'] + [f'arxiv:{i}' for i in range(67)]
    nodes = [{'id': key, 'title': f'Paper <{i}> & 😀', 'authors': ['Ada'],
              'kind': 'arxiv', 'section': 'Tests', 'url': 'https://example.org/'}
             for i, key in enumerate(ids)]
    return {'nodes': nodes, 'edges': [[i, 0, 'id'] for i in range(2, len(ids))]}


def test_static_walk_covers_every_neighbor_and_text_code_point(tmp_path):
    graph = fixture()
    key = graph['nodes'][0]['id']
    raw = ('# Method 😀\n\n' + ('Formula $x < y$ & [64]\n\n' * 1600)
           + '\n## References\nBibliography entry\n\n## Appendix A\nTail 😀')
    report = build_pages(graph, {key: raw}, tmp_path)
    assert report['papers'] == 69
    assert report['with_text'] == 1
    paper = tmp_path / 'agents' / 'papers' / slug(key)
    card = json.loads((paper / 'paper.json').read_text())
    assert len(card['incoming']) == 67
    assert all(edge['target'] == key for edge in card['incoming'])
    visited = []
    for number in range(1, 4):
        parser = Links()
        parser.feed((paper / f'in-{number}.html').read_text())
        visited.extend(url for url in parser.links if '/papers/' in url)
    assert len(visited) == len(set(visited)) == 67
    collected = ''
    for number, part in enumerate(card['text_parts'], 1):
        parser = Links()
        parser.feed((paper / f'part-{number}.html').read_text())
        text = ''.join(parser.text)
        assert len(text) <= TEXT_SIZE
        assert text == clean_markdown(raw)[part['start']:part['end']]
        collected += text
    assert collected == clean_markdown(raw)
    assert 'Bibliography entry' not in collected
    assert (paper / 'source.md').read_text() == raw
    assert collected.endswith('Tail 😀')
    assert '<script' not in (paper / 'index.html').read_text()
    missing = tmp_path / 'agents' / 'papers' / slug('url:missing')
    assert not json.loads((missing / 'paper.json').read_text())['text_available']

    # An agent can follow every published local link using plain HTML.
    for page in (tmp_path / 'agents').rglob('*.html'):
        parser = Links()
        parser.feed(page.read_text())
        current = SITE_URL + '/' + page.relative_to(tmp_path).as_posix()
        for href in parser.links:
            target = urljoin(current, href)
            if target.startswith(SITE_URL + '/'):
                path = unquote(urlparse(target).path.removeprefix('/favorite-papers/'))
                local = tmp_path / path
                assert local.exists(), (page, href)
                if local.is_dir():
                    assert (local / 'index.html').is_file()


def test_rebuild_removes_stale_papers_but_preserves_map(tmp_path):
    (tmp_path / 'index.html').write_text('map')
    graph = fixture()
    build_pages(graph, {}, tmp_path)
    graph['nodes'] = graph['nodes'][:1]
    graph['edges'] = []
    build_pages(graph, {}, tmp_path)
    assert (tmp_path / 'index.html').read_text() == 'map'
    assert not (tmp_path / 'agents' / 'papers' / slug('url:missing')).exists()
    assert 'No verified API' in (tmp_path / 'agents' / 'index.html').read_text()


def test_discovery_requires_success_and_live_health(tmp_path, monkeypatch):
    import io
    import urllib.request

    path = tmp_path / 'smoke.json'
    origin = 'https://key-papers-api.example.workers.dev'
    assert verified_origin(path) == ''
    path.write_text(json.dumps({'ok': False, 'origin': origin}))
    assert verified_origin(path) == ''
    path.write_text(json.dumps({'ok': True, 'origin': origin}))
    monkeypatch.setattr(urllib.request, 'urlopen',
                        lambda *a, **kw: io.BytesIO(b'{"status":"ready"}'))
    assert verified_origin(path) == origin
    monkeypatch.setattr(urllib.request, 'urlopen',
                        lambda *a, **kw: io.BytesIO(b'{"status":"unavailable"}'))
    assert verified_origin(path) == ''


def test_smoke_accepts_json_or_sse_and_rejects_broken_tool_contract(monkeypatch):
    import pytest
    import smoke_agent_api as smoke

    result = {'structuredContent': {'results': []},
              'content': [{'type': 'text', 'text': '{"results":[]}'}]}
    envelope = json.dumps({'jsonrpc': '2.0', 'id': 2, 'result': result})
    for body in [envelope, 'event: message\ndata: ' + envelope + '\n\n']:
        monkeypatch.setattr(smoke, '_post', lambda *args: (200, body))
        assert smoke._tool('https://example.test', 'search', {}) == {'results': []}
    result['structuredContent'] = {'results': ['inconsistent']}
    monkeypatch.setattr(smoke, '_post', lambda *args: (
        200, json.dumps({'result': result}),
    ))
    with pytest.raises(ValueError, match='disagrees'):
        smoke._tool('https://example.test', 'search', {})
