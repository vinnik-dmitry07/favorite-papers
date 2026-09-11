'''Retrieve reference lists for every catalog entry.

arXiv entries are read from the arXiv HTML rendering (ar5iv as fallback);
blogs and other pages are read from their own HTML; DOI entries use Crossref
metadata and its reference list; OpenReview entries only yield metadata.

Outputs assets/refs.json (per-node outgoing references) and assets/page_meta.json
(titles / dates / authors discovered while fetching). Raw responses are cached
gzipped under cache/ so re-runs are offline and resumable.

Run:  python src/fetch_refs.py [--limit N] [--refresh] [--workers N] [--only ID]
'''

import html as html_lib
import json
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import (  # noqa: E402
    ARXIV_META, ARXIV_TEXT_RE, ARXIV_URL_RE, CACHE_DIR, CATALOG, DOI_RE,
    KNOWN_META, PAGE_META, REFS, ROOT, cache_path, clean_arxiv_id,
    clean_doi, dump_json, host_of, load_json, node_arxiv_ids, norm_title,
    read_gz, write_gz,
)

HEADERS = {
    'User-Agent': 'key-papers-citation-map/0.1 (local research map builder)',
    'Accept': 'text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8',
}
TIMEOUT = 45
HOST_DELAY = 0.5
MAX_SEARCH_CHARS = 400_000

BIBITEM_SPLIT = re.compile(r'<li[^>]*class="[^"]*ltx_bibitem[^"]*"[^>]*>', re.I)
REF_HEADING_RE = re.compile(
    r'<h[1-6][^>]*>\s*(?:<[^>]+>\s*)*'
    r'(?:references|bibliography|works cited|citations)\b',
    re.I,
)
SCRIPT_RE = re.compile(r'<(script|style|svg)\b.*?</\1>', re.S | re.I)
TAG_RE = re.compile(r'<[^>]+>')
HREF_RE = re.compile(r'href=["\']([^"\'<>]+)["\']', re.I)
META_RE = re.compile(r'<meta\b[^>]*>', re.I)
ATTR_RE = re.compile(r'([\w:.-]+)\s*=\s*["\']([^"\']*)["\']')
# Matches 2024-03-21, 2024-03-21T08:00Z, 2022/5 and a bare 2024.
DATE_IN_TEXT_RE = re.compile(
    r'\b((?:19|20)\d{2})(?:[-/](\d{1,2})(?:[-/](\d{1,2}))?)?'
)
LD_DATE_RE = re.compile(
    r'"date(?:Published|Created|Modified)"\s*:\s*"([^"]{4,40})"', re.I
)

DATE_META_KEYS = (
    'citation_publication_date', 'citation_date', 'article:published_time',
    'datepublished', 'date', 'dc.date', 'dc.date.issued', 'og:published_time',
    'article:modified_time', 'last-modified',
)
TITLE_META_KEYS = ('citation_title', 'og:title', 'dc.title', 'twitter:title')
AUTHOR_META_KEYS = ('citation_author', 'author', 'article:author', 'dc.creator')

_host_locks: dict[str, threading.Lock] = {}
_host_last: dict[str, float] = {}
_locks_guard = threading.Lock()
_print_lock = threading.Lock()


def throttle(url: str) -> None:
    '''Keep at least HOST_DELAY seconds between hits on the same host.'''
    host = host_of(url)
    with _locks_guard:
        lock = _host_locks.setdefault(host, threading.Lock())
    with lock:
        wait = HOST_DELAY - (time.monotonic() - _host_last.get(host, 0.0))
        if wait > 0:
            time.sleep(wait)
        _host_last[host] = time.monotonic()


def http_get(url: str, attempts: int = 2) -> requests.Response | None:
    for attempt in range(attempts):
        throttle(url)
        try:
            resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        except requests.RequestException:
            if attempt + 1 == attempts:
                return None
            time.sleep(1.5)
            continue
        if resp.status_code == 200:
            return resp
        if resp.status_code in (429, 500, 502, 503) and attempt + 1 < attempts:
            time.sleep(3)
            continue
        return None
    return None


def strip_tags(markup: str) -> str:
    text = SCRIPT_RE.sub(' ', markup)
    text = TAG_RE.sub(' ', text)
    return html_lib.unescape(text)


def bib_region(markup: str) -> tuple[str | None, int]:
    '''Return the bibliography markup and the number of LaTeXML bib items.'''
    parts = BIBITEM_SPLIT.split(markup)
    if len(parts) > 1:
        items = [chunk.split('</li>', 1)[0] for chunk in parts[1:]]
        return '\n'.join(items), len(items)
    match = None
    for match in REF_HEADING_RE.finditer(markup):
        pass
    if match:
        return markup[match.start():], 0
    return None, 0


def parse_date_text(value: str) -> str | None:
    '''Pull an ISO date out of a metadata value, padding missing parts.'''
    match = DATE_IN_TEXT_RE.search(value)
    if not match:
        return None
    year, month, day = match.groups()
    month = int(month or 1)
    day = int(day or 1)
    if not 1 <= month <= 12 or not 1 <= day <= 31:
        return None
    return f'{year}-{month:02d}-{day:02d}'


def parse_meta(markup: str) -> dict:
    found: dict[str, list[str]] = {}
    for tag in META_RE.findall(markup):
        attrs = {k.lower(): v for k, v in ATTR_RE.findall(tag)}
        key = attrs.get('name') or attrs.get('property') or attrs.get('itemprop')
        content = attrs.get('content')
        if key and content:
            found.setdefault(key.lower(), []).append(html_lib.unescape(content))

    meta: dict = {}
    for key in TITLE_META_KEYS:
        if found.get(key):
            meta['title'] = ' '.join(found[key][0].split())
            break
    for key in DATE_META_KEYS:
        for value in found.get(key, []):
            meta['date'] = parse_date_text(value)
            if meta['date']:
                break
        if meta.get('date'):
            break
    for key in AUTHOR_META_KEYS:
        if found.get(key):
            meta['authors'] = [' '.join(a.split()) for a in found[key][:4]]
            break

    if not meta.get('date'):
        time_tag = re.search(r'<time[^>]*datetime=["\']([^"\']+)', markup, re.I)
        if time_tag:
            meta['date'] = parse_date_text(time_tag.group(1))
    if not meta.get('date'):
        ld_tag = LD_DATE_RE.search(markup)
        if ld_tag:
            meta['date'] = parse_date_text(ld_tag.group(1))
    return meta


class TitleMatcher:
    '''Finds catalog titles quoted verbatim inside a block of text.'''

    MIN_CHARS = 22

    def __init__(self, catalog: list[dict]):
        lookup: dict[str, str] = {}
        overrides = load_json(KNOWN_META, {})
        arxiv_known = load_json(ARXIV_META, {})
        page_meta = load_json(PAGE_META, {})
        for node in catalog:
            extras = []
            for aid in node_arxiv_ids(node, overrides, page_meta):
                info = arxiv_known.get(aid) or {}
                if info.get('title'):
                    extras.append(info['title'])
            page_title = (page_meta.get(node['id']) or {}).get('title')
            if page_title and node.get('kind') in (
                'doi', 'acl', 'openreview', 'arxiv',
            ):
                extras.append(page_title)
            for raw in (
                node.get('title'), node.get('label'),
                node.get('fetched_title'), *extras,
            ):
                key = norm_title(raw)
                if not key or key in lookup:
                    continue
                if len(key) >= self.MIN_CHARS or self._distinctive(key):
                    lookup[key] = node['id']
        self.lookup = lookup
        keys = sorted(lookup, key=len, reverse=True)
        self.pattern = re.compile(
            r'(?<![a-z0-9])(?:%s)(?![a-z0-9])'
            % '|'.join(re.escape(k) for k in keys)
        )

    @staticmethod
    def _distinctive(key: str) -> bool:
        '''Short titles are only safe as a single, reasonably long token.'''
        return ' ' not in key and len(key) >= 6

    def match(self, text: str) -> list[str]:
        found = {self.lookup[m.group(0)] for m in self.pattern.finditer(text)}
        return sorted(found)


def extract_from_html(markup: str, hosts: set[str], matcher: TitleMatcher) -> dict:
    bib_markup, item_count = bib_region(markup)
    search_markup = bib_markup or markup
    text = ' '.join(strip_tags(search_markup).split())[:MAX_SEARCH_CHARS]

    arxiv_ids = {clean_arxiv_id(i) for i in ARXIV_URL_RE.findall(search_markup)}
    arxiv_ids |= {clean_arxiv_id(i) for i in ARXIV_TEXT_RE.findall(text)}

    dois = {clean_doi(d) for d in DOI_RE.findall(text)}
    urls = []
    for href in HREF_RE.findall(search_markup):
        if href.startswith('http') and host_of(href) in hosts:
            urls.append(href)
        match = DOI_RE.search(href)
        if match and 'doi.org' in href:
            dois.add(clean_doi(match.group(1)))

    return {
        'arxiv': sorted(arxiv_ids),
        'doi': sorted(dois),
        'urls': sorted(set(urls))[:400],
        'titles': matcher.match(norm_title(text)),
        'bib_items': item_count,
        'has_bibliography': bool(bib_markup),
        'search_chars': len(text),
    }


def extract_from_crossref(payload: dict, matcher: TitleMatcher) -> tuple[dict, dict]:
    message = payload.get('message', {})
    titles = message.get('title') or []
    parts = (message.get('issued', {}).get('date-parts') or [[]])[0]
    date = None
    if parts:
        padded = list(parts) + [1, 1]
        date = f'{padded[0]:04d}-{padded[1]:02d}-{padded[2]:02d}'
    authors = [
        ' '.join(filter(None, (a.get('given'), a.get('family'))))
        for a in (message.get('author') or [])[:4]
    ]
    meta = {
        'title': ' '.join(titles[0].split()) if titles else None,
        'date': date,
        'authors': [a for a in authors if a],
    }

    dois, arxiv_ids, blobs = set(), set(), []
    for ref in message.get('reference') or []:
        if ref.get('DOI'):
            dois.add(clean_doi(ref['DOI']))
        for field in ('article-title', 'volume-title', 'unstructured'):
            if ref.get(field):
                blobs.append(ref[field])
        raw = ' '.join(str(v) for v in ref.values())
        arxiv_ids |= {clean_arxiv_id(i) for i in ARXIV_TEXT_RE.findall(raw)}
        arxiv_ids |= {clean_arxiv_id(i) for i in ARXIV_URL_RE.findall(raw)}

    refs = {
        'arxiv': sorted(arxiv_ids),
        'doi': sorted(dois),
        'urls': [],
        'titles': matcher.match(norm_title(' ; '.join(blobs))),
        'bib_items': len(message.get('reference') or []),
        'has_bibliography': bool(message.get('reference')),
        'search_chars': sum(len(b) for b in blobs),
    }
    return refs, meta


def openreview_meta(payload: dict) -> dict:
    notes = payload.get('notes') or []
    if not notes:
        return {}
    note = notes[0]
    content = note.get('content') or {}

    def value(key):
        item = content.get(key)
        if isinstance(item, dict):
            return item.get('value')
        return item

    stamp = note.get('pdate') or note.get('cdate') or note.get('tcdate')
    date = None
    if stamp:
        date = time.strftime('%Y-%m-%d', time.gmtime(stamp / 1000))
    authors = value('authors') or []
    return {
        'title': ' '.join((value('title') or '').split()) or None,
        'date': date,
        'authors': authors[:4] if isinstance(authors, list) else [],
    }


def fetch_urls_for(node: dict) -> list[str]:
    '''Candidate documents to read for a node, best source first.'''
    node_id, kind = node['id'], node['kind']
    primary = node['urls'][0]
    if kind == 'arxiv':
        arxiv_id = node_id.split(':', 1)[1]
        return [
            f'https://arxiv.org/html/{arxiv_id}',
            f'https://ar5iv.labs.arxiv.org/html/{arxiv_id}',
        ]
    if kind == 'openreview':
        forum = node_id.split(':', 1)[1]
        return [
            f'https://api2.openreview.net/notes?forum={forum}',
            f'https://api.openreview.net/notes?forum={forum}',
        ]
    if kind == 'doi':
        doi = node_id.split(':', 1)[1]
        return [f'https://api.crossref.org/works/{doi}']
    return [primary] + [
        u for u in node['urls'][1:]
        if u.lower().endswith(('.html', '.htm', '/'))
    ][:1]


def load_cached(node: dict) -> tuple[str, str, str] | None:
    '''Return `(payload, source_url, cache_kind)` from disk if present.'''
    for suffix in ('.html.gz', '.json.gz'):
        path = cache_path(node['id'], suffix)
        if not path.exists():
            continue
        raw = read_gz(path)
        head, _, body = raw.partition('\n')
        return body, head.strip(), 'json' if suffix.startswith('.json') else 'html'
    return None


def store_cache(node: dict, url: str, body: str, cache_kind: str) -> None:
    suffix = '.json.gz' if cache_kind == 'json' else '.html.gz'
    write_gz(cache_path(node['id'], suffix), f'{url}\n{body}')


def download(node: dict) -> tuple[str, str, str] | None:
    '''Try each candidate document, preferring one that carries a bibliography.'''
    fallback = None
    for url in fetch_urls_for(node):
        if url.lower().endswith('.pdf'):
            continue
        resp = http_get(url)
        if resp is None:
            continue
        body = resp.text
        content_type = resp.headers.get('content-type', '')
        if 'json' in content_type or url.startswith((
            'https://api.crossref.org', 'https://api2.openreview.net',
            'https://api.openreview.net',
        )):
            try:
                payload = json.loads(body)
            except ValueError:
                continue
            if url.startswith('https://api.crossref.org'):
                if not payload.get('message'):
                    continue
            elif not payload.get('notes'):
                continue
            return body, resp.url, 'json'
        if len(body) < 400:
            continue
        if node['kind'] == 'arxiv' and 'ltx_' not in body:
            continue
        if bib_region(body)[1]:
            return body, resp.url, 'html'
        fallback = fallback or (body, resp.url, 'html')
    return fallback


def process(node: dict, hosts: set[str], matcher: TitleMatcher,
            refresh: bool) -> tuple[dict, dict, str]:
    cached = None if refresh else load_cached(node)
    if cached is None:
        got = download(node)
        if got is None:
            return {'status': 'unavailable'}, {}, 'unavailable'
        body, source_url, cache_kind = got
        store_cache(node, source_url, body, cache_kind)
    else:
        body, source_url, cache_kind = cached

    meta: dict = {}
    if cache_kind == 'json':
        payload = json.loads(body)
        if 'message' in payload:
            refs, meta = extract_from_crossref(payload, matcher)
        else:
            refs = {
                'arxiv': [], 'doi': [], 'urls': [], 'titles': [],
                'bib_items': 0, 'has_bibliography': False, 'search_chars': 0,
            }
            meta = openreview_meta(payload)
    else:
        refs = extract_from_html(body, hosts, matcher)
        meta = parse_meta(body)
        # A redirect can reveal that a page is really a paper landing page.
        if source_url and source_url not in node['urls']:
            meta['resolved'] = source_url

    refs['status'] = 'cached' if cached is not None else 'fetched'
    refs['source'] = source_url
    return refs, {k: v for k, v in meta.items() if v}, refs['status']


def main() -> None:
    args = sys.argv[1:]
    refresh = '--refresh' in args
    limit = None
    workers = 4
    only = None
    for flag, cast in (('--limit', int), ('--workers', int), ('--only', str)):
        if flag in args:
            value = args[args.index(flag) + 1]
            if flag == '--limit':
                limit = cast(value)
            elif flag == '--workers':
                workers = cast(value)
            else:
                only = value

    catalog = load_json(CATALOG, [])
    if not catalog:
        raise SystemExit('assets/catalog.json missing - run src/parse_readme.py')
    nodes = [n for n in catalog if not only or n['id'] == only]
    if limit:
        nodes = nodes[:limit]

    hosts = {host_of(u) for node in catalog for u in node['urls']}
    matcher = TitleMatcher(catalog)
    print(f'{len(nodes)} nodes to read; title matcher holds '
          f'{len(matcher.lookup)} titles; {workers} workers')
    CACHE_DIR.mkdir(parents=True, exist_ok=True)

    full_rebuild = refresh and not (only or limit)
    refs_out = {} if full_rebuild else load_json(REFS, {})
    meta_out = {} if full_rebuild else load_json(PAGE_META, {})

    counters = {'fetched': 0, 'cached': 0, 'unavailable': 0}
    done = 0
    started = time.monotonic()

    def run(node):
        try:
            return node, process(node, hosts, matcher, refresh)
        except Exception as exc:  # noqa: BLE001
            return node, ({'status': 'error', 'error': str(exc)}, {}, 'unavailable')

    with ThreadPoolExecutor(max_workers=workers) as pool:
        for node, (refs, meta, status) in pool.map(run, nodes):
            done += 1
            counters[status] = counters.get(status, 0) + 1
            refs_out[node['id']] = refs
            if meta:
                meta_out[node['id']] = meta
            hits = (len(refs.get('arxiv', [])) + len(refs.get('doi', []))
                    + len(refs.get('titles', [])))
            with _print_lock:
                print(f'[{done:4d}/{len(nodes)}] {status:11s} '
                      f'bib={refs.get("bib_items", 0):3d} raw_refs={hits:4d} '
                      f'{node["id"][:52]}', flush=True)
            if done % 25 == 0:
                dump_json(REFS, refs_out)
                dump_json(PAGE_META, meta_out)

    dump_json(REFS, refs_out)
    dump_json(PAGE_META, meta_out)
    elapsed = time.monotonic() - started
    print(f'\ndone in {elapsed / 60:.1f} min - '
          + ', '.join(f'{k}={v}' for k, v in counters.items() if v))
    print(f'wrote {REFS.relative_to(ROOT)} and {PAGE_META.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
