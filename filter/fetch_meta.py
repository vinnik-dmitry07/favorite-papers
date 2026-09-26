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

FILTER_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(FILTER_DIR))
sys.path.insert(0, str(FILTER_DIR.parent / 'src'))

from fetch_refs import parse_meta  # noqa: E402
from paths import (  # noqa: E402
    META_JSONL,
    PAPERS_JSONL,
    print_progress,
    read_jsonl,
    write_jsonl,
)

OPENREVIEW_APIS = (
    'https://api2.openreview.net/notes?id={fid}',
    'https://api2.openreview.net/notes?forum={fid}',
    'https://api.openreview.net/notes?id={fid}',
    'https://api.openreview.net/notes?forum={fid}',
)
CROSSREF = 'https://api.crossref.org/works/{doi}'
ACL_URL = 'https://aclanthology.org/{aid}/'
HEADERS = {
    'User-Agent': 'key-papers-filter/0.1 (local research scoring)',
    'Accept': 'application/json, text/html, application/atom+xml;q=0.9,*/*;q=0.8',
}
ABSTRACT_META = (
    'citation_abstract', 'dc.description', 'og:description',
    'twitter:description',
)
TITLE_META = ('citation_title', 'og:title', 'dc.title')
META_RE = re.compile(r'<meta\b[^>]*>', re.I)
ATTR_RE = re.compile(r'([\w:.-]+)\s*=\s*["\']([^"\']*)["\']')
TAG_RE = re.compile(r'<[^>]+>')
RETRY_STATUSES = {429, 500, 502, 503, 504}


def http_get(
    url: str, timeout: int = 45, attempts: int = 4,
) -> tuple[int, bytes] | None:
    delay = 8
    for attempt in range(attempts):
        request = urllib.request.Request(url, headers=HEADERS)
        try:
            with urllib.request.urlopen(request, timeout=timeout) as resp:
                return resp.status, resp.read()
        except urllib.error.HTTPError as exc:
            print(f'  HTTP {exc.code} {url}', flush=True)
            result: tuple[int, bytes] | None = (
                exc.code, exc.read() if exc.fp else b''
            )
            retry = exc.code in RETRY_STATUSES
        except Exception as exc:  # noqa: BLE001
            print(f'  fail {url}: {exc}', flush=True)
            result = None
            retry = True
        if not retry or attempt + 1 == attempts:
            return result
        time.sleep(delay)
        delay = min(delay * 2, 60)
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


def citation_meta(raw: bytes, category: str) -> dict:
    markup = raw.decode('utf-8', 'replace')
    found = parse_meta_tags(markup)
    title = first_meta(found, TITLE_META) or ''
    abstract = first_meta(found, ABSTRACT_META) or ''
    if not title and not abstract:
        return {}
    return {
        'title': title,
        'abstract': abstract,
        'published': parse_meta(markup).get('date') or '',
        'category': category,
    }


def fetch_page_meta(url: str, category: str) -> dict:
    hit = http_get(url)
    if hit is None:
        return {}
    status, raw = hit
    if status >= 400:
        return {}
    return citation_meta(raw, category)


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
    status, raw = hit
    if status == 404:
        return fetch_doi_page(doi)
    if status >= 400:
        return {}
    try:
        message = json.loads(raw.decode('utf-8', 'replace')).get('message') or {}
    except json.JSONDecodeError:
        return fetch_doi_page(doi)
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
    if title or abstract:
        return {
            'title': title,
            'abstract': abstract,
            'published': published,
            'category': (message.get('type') or 'doi'),
        }
    return fetch_doi_page(doi)


def fetch_doi_page(doi: str) -> dict:
    '''Citation meta from the DOI landing page when Crossref has no record.'''
    return fetch_page_meta(
        f'https://doi.org/{urllib.parse.quote(doi)}', 'doi'
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--force', action='store_true', help='refetch every paper')
    parser.add_argument(
        '--only-keys',
        default='',
        help='comma-separated keys to refetch (implies force for those keys)',
    )
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
    wanted = {part.strip() for part in args.only_keys.split(',') if part.strip()}
    cached = {row['key']: row for row in read_jsonl(META_JSONL)}
    if wanted:
        pending = [paper for paper in papers if paper['key'] in wanted]
        if not pending:
            raise SystemExit(f'no papers match --only-keys {sorted(wanted)}')
    else:
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

    # export.arxiv.org/api/query 406s on multi-id queries and 429s under load.
    resolved = 0
    for index, arxiv_id in enumerate(arxiv_ids, start=1):
        meta = fetch_page_meta(f'https://arxiv.org/abs/{arxiv_id}', '')
        if useful_meta(meta):
            cached[f'arxiv:{arxiv_id}'] = {
                'key': f'arxiv:{arxiv_id}',
                **meta,
            }
            resolved += 1
        print(
            f'arxiv abs: {index}/{len(arxiv_ids)} resolved={resolved}',
            flush=True,
        )
        if index < len(arxiv_ids):
            time.sleep(1.2)

    for index, paper in enumerate(other, start=1):
        kind, value = paper['key'].split(':', 1)
        meta = {}
        if kind == 'openreview':
            meta = fetch_openreview(value)
        elif kind == 'doi':
            meta = fetch_crossref(value)
        elif kind == 'acl':
            meta = fetch_page_meta(ACL_URL.format(aid=value), 'acl')
        if useful_meta(meta):
            cached[paper['key']] = {'key': paper['key'], **meta}
        print_progress(index, len(other), paper['key'])
        if index < len(other):
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
