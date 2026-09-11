'''Fetch title, abstract, and date for scoreable readme papers.

    python filter/fetch_meta.py
'''

from __future__ import annotations

import argparse
import html as html_lib
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from xml.etree import ElementTree

FILTER_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(FILTER_DIR))
sys.path.insert(0, str(FILTER_DIR.parent / 'src'))

from paths import (  # noqa: E402
    META_JSONL,
    PAPERS_JSONL,
    print_progress,
    read_jsonl,
    write_jsonl,
)

ARXIV_API = 'https://export.arxiv.org/api/query'
OPENREVIEW_APIS = (
    'https://api2.openreview.net/notes?id={fid}',
    'https://api2.openreview.net/notes?forum={fid}',
    'https://api.openreview.net/notes?id={fid}',
    'https://api.openreview.net/notes?forum={fid}',
)
CROSSREF = 'https://api.crossref.org/works/{doi}'
ACL_URL = 'https://aclanthology.org/{aid}/'
NS = {'a': 'http://www.w3.org/2005/Atom'}
HEADERS = {
    'User-Agent': 'key-papers-filter/0.1 (local research scoring)',
    'Accept': 'application/json, text/html, application/atom+xml;q=0.9,*/*;q=0.8',
}
ABSTRACT_META = (
    'citation_abstract', 'dc.description', 'og:description',
    'description', 'twitter:description',
)
TITLE_META = ('citation_title', 'og:title', 'dc.title')
DATE_META = ('citation_publication_date', 'citation_date', 'dc.date')
META_RE = re.compile(r'<meta\b[^>]*>', re.I)
ATTR_RE = re.compile(r'([\w:.-]+)\s*=\s*["\']([^"\']*)["\']')
TAG_RE = re.compile(r'<[^>]+>')


def http_get(url: str, timeout: int = 45) -> tuple[int, bytes] | None:
    request = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as resp:
            return resp.status, resp.read()
    except urllib.error.HTTPError as exc:
        print(f'  HTTP {exc.code} {url}', flush=True)
        return exc.code, exc.read() if exc.fp else b''
    except Exception as exc:  # noqa: BLE001
        print(f'  fail {url}: {exc}', flush=True)
        return None


def parse_meta_tags(markup: str) -> dict[str, list[str]]:
    found: dict[str, list[str]] = {}
    for tag in META_RE.findall(markup):
        attrs = {k.lower(): v for k, v in ATTR_RE.findall(tag)}
        key = attrs.get('name') or attrs.get('property') or attrs.get('itemprop')
        content = attrs.get('content')
        if key and content:
            found.setdefault(key.lower(), []).append(html_lib.unescape(content))
    return found


def first_meta(found: dict[str, list[str]], keys: tuple[str, ...]) -> str | None:
    for key in keys:
        values = found.get(key)
        if values:
            return ' '.join(values[0].split())
    return None


def strip_jats(text: str) -> str:
    text = html_lib.unescape(text or '')
    text = TAG_RE.sub(' ', text)
    return ' '.join(text.split())


def fetch_arxiv_batch(ids: list[str]) -> dict[str, dict]:
    query = urllib.parse.urlencode(
        {'id_list': ','.join(ids), 'max_results': len(ids)}
    )
    hit = http_get(f'{ARXIV_API}?{query}')
    if hit is None:
        return {}
    status, raw = hit
    if status >= 400:
        return {}
    root = ElementTree.fromstring(raw)
    out = {}
    for entry in root.findall('a:entry', NS):
        url = entry.findtext('a:id', default='', namespaces=NS)
        match = re.search(r'abs/(.+?)(?:v\d+)?$', url)
        if not match:
            continue
        category = ''
        prim = entry.find('a:primary_category', NS)
        if prim is not None:
            category = prim.attrib.get('term', '')
        out[match.group(1)] = {
            'title': ' '.join(
                (entry.findtext('a:title', default='', namespaces=NS) or '').split()
            ),
            'abstract': ' '.join(
                (entry.findtext('a:summary', default='', namespaces=NS) or '').split()
            ),
            'published': (entry.findtext('a:published', default='', namespaces=NS) or '')[:10],
            'category': category,
        }
    return out


def note_value(content: dict, key: str):
    item = content.get(key)
    if isinstance(item, dict):
        return item.get('value')
    return item


def pick_submission(notes: list, forum_id: str) -> dict | None:
    for note in notes:
        if note.get('id') == forum_id:
            return note
    for note in notes:
        if note.get('replyto') in (None, ''):
            content = note.get('content') or {}
            if note_value(content, 'title') or note_value(content, 'abstract'):
                return note
    for note in notes:
        content = note.get('content') or {}
        if note_value(content, 'title') and note_value(content, 'abstract'):
            return note
    return notes[0] if notes else None


def fetch_openreview(forum_id: str) -> dict:
    for template in OPENREVIEW_APIS:
        hit = http_get(template.format(fid=forum_id))
        if hit is None:
            continue
        _status, raw = hit
        try:
            payload = json.loads(raw.decode('utf-8', 'replace'))
        except json.JSONDecodeError:
            continue
        notes = payload.get('notes') or []
        if not notes:
            continue
        note = pick_submission(notes, forum_id)
        if note is None:
            continue
        content = note.get('content') or {}
        stamp = note.get('pdate') or note.get('cdate') or note.get('tcdate')
        published = ''
        if stamp:
            published = time.strftime('%Y-%m-%d', time.gmtime(stamp / 1000))
        return {
            'title': ' '.join(str(note_value(content, 'title') or '').split()),
            'abstract': ' '.join(str(note_value(content, 'abstract') or '').split()),
            'published': published,
            'category': 'openreview',
        }
    return {}


def fetch_crossref(doi: str) -> dict:
    hit = http_get(CROSSREF.format(doi=urllib.parse.quote(doi)))
    if hit is None:
        return {}
    _status, raw = hit
    try:
        message = json.loads(raw.decode('utf-8', 'replace')).get('message') or {}
    except json.JSONDecodeError:
        return {}
    issued = ((message.get('issued') or {}).get('date-parts') or [[]])[0]
    published = ''
    if issued:
        year = issued[0]
        month = issued[1] if len(issued) > 1 else 1
        day = issued[2] if len(issued) > 2 else 1
        published = f'{year:04d}-{month:02d}-{day:02d}'
    titles = message.get('title') or []
    title = ' '.join(str(titles[0]).split()) if titles else ''
    abstract = strip_jats(message.get('abstract') or '')
    if not title and not abstract:
        return {}
    return {
        'title': title,
        'abstract': abstract,
        'published': published,
        'category': (message.get('type') or 'doi'),
    }


def fetch_acl(acl_id: str) -> dict:
    hit = http_get(ACL_URL.format(aid=acl_id))
    if hit is None:
        return {}
    _status, raw = hit
    found = parse_meta_tags(raw.decode('utf-8', 'replace'))
    title = first_meta(found, TITLE_META) or ''
    abstract = first_meta(found, ABSTRACT_META) or ''
    if not title and not abstract:
        return {}
    return {
        'title': title,
        'abstract': abstract,
        'published': (first_meta(found, DATE_META) or '')[:10],
        'category': 'acl',
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--force', action='store_true', help='refetch every paper')
    return parser.parse_args()


def meta_complete(row: dict | None) -> bool:
    if not row:
        return False
    if row.get('abstract'):
        return True
    return bool(row.get('title') and row.get('published'))


def useful_meta(meta: dict) -> bool:
    return bool(meta and (meta.get('title') or meta.get('abstract')))


def main() -> None:
    args = parse_args()
    papers = read_jsonl(PAPERS_JSONL)
    if not papers:
        raise SystemExit('run filter/collect_readme.py first')
    cached = {row['key']: row for row in read_jsonl(META_JSONL)}
    pending = [
        paper for paper in papers
        if args.force or not meta_complete(cached.get(paper['key']))
    ]
    print(f'{len(cached)} cached, {len(pending)} to fetch', flush=True)

    arxiv_ids = []
    other = []
    for paper in pending:
        kind, value = paper['key'].split(':', 1)
        if kind == 'arxiv':
            arxiv_ids.append(value)
        else:
            other.append(paper)

    size = 100
    for start in range(0, len(arxiv_ids), size):
        batch = arxiv_ids[start:start + size]
        try:
            fetched = fetch_arxiv_batch(batch)
        except Exception as exc:  # noqa: BLE001
            print(f'arxiv batch {start} failed: {exc}', flush=True)
            fetched = {}
        for arxiv_id, meta in fetched.items():
            if useful_meta(meta):
                cached[f'arxiv:{arxiv_id}'] = {
                    'key': f'arxiv:{arxiv_id}',
                    **meta,
                }
        print(
            f'arxiv api: {min(start + size, len(arxiv_ids))}/{len(arxiv_ids)} '
            f'resolved={len(fetched)}',
            flush=True,
        )
        time.sleep(3)

    for index, paper in enumerate(other, start=1):
        kind, value = paper['key'].split(':', 1)
        meta = {}
        if kind == 'openreview':
            meta = fetch_openreview(value)
        elif kind == 'doi':
            meta = fetch_crossref(value)
        elif kind == 'acl':
            meta = fetch_acl(value)
        if useful_meta(meta):
            cached[paper['key']] = {'key': paper['key'], **meta}
        print_progress(index, len(other), paper['key'])
        time.sleep(1)

    rows = []
    missing = []
    for paper in papers:
        row = cached.get(paper['key'])
        if not row or not (row.get('title') or row.get('abstract')):
            missing.append(paper['key'])
            rows.append({
                'key': paper['key'],
                'title': paper.get('line_title') or '',
                'abstract': '',
                'published': '',
                'category': paper['kind'],
            })
            continue
        if not meta_complete(row):
            missing.append(paper['key'])
        rows.append(row)
    write_jsonl(META_JSONL, rows)
    with_abs = sum(1 if row.get('abstract') else 0 for row in rows)
    print(
        f'wrote {META_JSONL}: {len(rows)} rows, {with_abs} with abstracts, '
        f'{len(missing)} incomplete',
        flush=True,
    )
    if missing:
        print('incomplete: ' + ', '.join(missing[:12]), flush=True)


if __name__ == '__main__':
    main()
