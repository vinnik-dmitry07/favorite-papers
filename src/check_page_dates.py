'''Open every non-arXiv-API catalog page and read a first-public date.

Always live-fetches (cache is only a fallback). Prints progress per article.

Run:  python src/check_page_dates.py [--apply]
'''

from __future__ import annotations

import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import urlsplit

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import (  # noqa: E402
    ASSETS, CATALOG, GRAPH, KNOWN_META, cache_path, clean_doi, dump_json,
    host_of, load_json, read_gz, write_gz,
)
from fetch_refs import (  # noqa: E402
    DATE_IN_TEXT_RE, HEADERS, TIMEOUT, http_get, openreview_meta,
    parse_date_text, parse_meta, strip_tags, throttle,
)

MONTHS = {
    'january': '01', 'jan': '01', 'february': '02', 'feb': '02',
    'march': '03', 'mar': '03', 'april': '04', 'apr': '04',
    'may': '05', 'june': '06', 'jun': '06', 'july': '07', 'jul': '07',
    'august': '08', 'aug': '08', 'september': '09', 'sep': '09',
    'sept': '09', 'october': '10', 'oct': '10', 'november': '11',
    'nov': '11', 'december': '12', 'dec': '12',
}
MONTH_ALT = '|'.join(sorted(MONTHS, key=len, reverse=True))
PUBLISHED_RE = re.compile(
    r'(?:published|posted|submitted|first published|date published|'
    r'released|appeared|updated)\s*(?:on|at|:)?\s+'
    r'(?:'
    r'(\d{1,2})\s+(' + MONTH_ALT + r')[a-z]*\.?,?\s+(20\d{2}|19\d{2})'
    r'|'
    r'(' + MONTH_ALT + r')[a-z]*\.?\s+(\d{1,2})(?:st|nd|rd|th)?,?\s+'
    r'(20\d{2}|19\d{2})'
    r')',
    re.I,
)
ISO_VISIBLE_RE = re.compile(
    r'(?:published|posted|submitted|date)\s*(?:on|at|:)?\s+'
    r'((?:19|20)\d{2})[-/](\d{1,2})[-/](\d{1,2})',
    re.I,
)
CROSSREF = 'https://api.crossref.org/works/'
OR_API = 'https://api2.openreview.net/notes?forum='
PUBLISHED_META = (
    'citation_publication_date', 'citation_date', 'article:published_time',
    'datepublished', 'dc.date.issued', 'og:published_time', 'dc.date', 'date',
)
SKIP_META = ('article:modified_time', 'last-modified')


def from_words(day: str, month: str, year: str) -> str | None:
    key = month.lower()
    mm = MONTHS.get(key) or MONTHS.get(key[:3])
    if not mm:
        return None
    d = int(day)
    if not 1 <= d <= 31:
        return None
    return f'{year}-{mm}-{d:02d}'


def dates_from_html(markup: str) -> list[tuple[str, str]]:
    found: list[tuple[str, str]] = []
    meta = parse_meta(markup)
    raw_keys = []
    for tag in re.findall(r'<meta\b[^>]*>', markup, re.I):
        attrs = {
            k.lower(): v
            for k, v in re.findall(r'([\w:.-]+)\s*=\s*["\']([^"\']*)["\']', tag)
        }
        key = attrs.get('name') or attrs.get('property') or attrs.get('itemprop')
        content = attrs.get('content')
        if key and content:
            raw_keys.append((key.lower(), content))
    for key, content in raw_keys:
        if key in SKIP_META:
            continue
        if key not in PUBLISHED_META:
            continue
        iso = parse_date_text(content)
        if iso:
            found.append((iso, f'meta:{key}'))
    if meta.get('date') and not found:
        found.append((meta['date'], 'html-meta'))
    time_tag = re.search(
        r'<time[^>]*datetime=["\']([^"\']+)', markup, re.I,
    )
    if time_tag:
        iso = parse_date_text(time_tag.group(1))
        if iso:
            found.append((iso, 'html-time'))
    text = strip_tags(markup[:250_000])
    for match in PUBLISHED_RE.finditer(text):
        if match.group(1):
            iso = from_words(match.group(1), match.group(2), match.group(3))
        else:
            iso = from_words(match.group(5), match.group(4), match.group(6))
        if iso:
            found.append((iso, 'html-text'))
    for match in ISO_VISIBLE_RE.finditer(text):
        iso = parse_date_text('-'.join(match.groups()))
        if iso:
            found.append((iso, 'html-text'))
    return found


def crossref_date(doi: str) -> tuple[str, str] | None:
    url = CROSSREF + clean_doi(doi)
    print(f'    opening {url}', flush=True)
    try:
        throttle(url)
        resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
    except requests.RequestException:
        return None
    if resp.status_code != 200:
        print(f'    crossref HTTP {resp.status_code}', flush=True)
        return None
    msg = resp.json().get('message') or {}
    candidates = []
    for key in ('posted', 'published-online', 'published-print', 'published',
                'issued'):
        parts = ((msg.get(key) or {}).get('date-parts') or [[]])[0]
        if len(parts) >= 1:
            year = parts[0]
            month = parts[1] if len(parts) > 1 else 1
            day = parts[2] if len(parts) > 2 else 1
            candidates.append((f'{year:04d}-{month:02d}-{day:02d}', key))
    if not candidates:
        return None
    iso, key = min(candidates, key=lambda item: item[0])
    return iso, f'crossref:{key}'


def openreview_date(forum: str) -> tuple[str, str] | None:
    url = OR_API + forum
    print(f'    opening {url}', flush=True)
    resp = http_get(url)
    if resp is None:
        return None
    try:
        payload = resp.json()
    except ValueError:
        return None
    meta = openreview_meta(payload)
    if meta.get('date'):
        return meta['date'], 'openreview-api'
    return None


def github_date(url: str) -> tuple[str, str] | None:
    parts = urlsplit(url).path.strip('/').split('/')
    if len(parts) < 2:
        return None
    api = f'https://api.github.com/repos/{parts[0]}/{parts[1]}'
    print(f'    opening {api}', flush=True)
    resp = http_get(api)
    if resp is None:
        return None
    try:
        created = resp.json().get('created_at')
    except ValueError:
        return None
    iso = parse_date_text(created or '')
    if iso:
        return iso, 'github-api'
    return None


def live_html(url: str, node_id: str) -> str | None:
    if not url or not url.startswith('http'):
        return None
    print(f'    opening {url[:90]}', flush=True)
    resp = http_get(url)
    if resp is None or not resp.text:
        cached = cache_path(node_id, '.html.gz')
        if cached.exists():
            raw = read_gz(cached)
            _, _, body = raw.partition('\n')
            print('    live fetch failed, using cache', flush=True)
            return body or raw
        return None
    write_gz(cache_path(node_id, '.html.gz'), f'{url}\n{resp.text}')
    return resp.text


def page_urls(node: dict) -> list[str]:
    urls = []
    for url in node.get('urls') or []:
        if url and url not in urls:
            urls.append(url)
    kind = node.get('kind')
    nid = node['id']
    if kind == 'doi':
        doi = nid.split(':', 1)[1]
        urls.append('https://doi.org/' + clean_doi(doi))
    if kind == 'openreview':
        forum = nid.split(':', 1)[1]
        urls.append(f'https://openreview.net/forum?id={forum}')
    if kind == 'acl':
        acl = nid.split(':', 1)[1]
        urls.append(f'https://aclanthology.org/{acl}/')
    primary = node.get('url')
    if primary and primary not in urls:
        urls.append(primary)
    return urls


def pick_date(candidates: list[tuple[str, str]]) -> tuple[str, str] | None:
    if not candidates:
        return None
    rank = {
        'openreview-api': 50,
        'github-api': 45,
        'crossref:posted': 40,
        'crossref:published-online': 38,
        'crossref:published': 36,
        'crossref:published-print': 34,
        'crossref:issued': 32,
        'meta:citation_publication_date': 30,
        'meta:citation_date': 29,
        'meta:article:published_time': 28,
        'meta:datepublished': 27,
        'meta:og:published_time': 26,
        'html-time': 20,
        'html-text': 15,
        'html-meta': 10,
    }
    scored = []
    for iso, src in candidates:
        precision = 3 if iso[8:10] != '01' else (2 if iso[5:7] != '01' else 1)
        scored.append((rank.get(src, 12), precision, iso, src))
    scored.sort(reverse=True)
    return scored[0][2], scored[0][3]


def is_coarse(iso: str | None, source: str | None) -> bool:
    if not iso:
        return True
    if source in ('url', 'label', 'label-year', 'venue-year'):
        return True
    return iso.endswith('-01-01')


def main() -> None:
    apply = '--apply' in sys.argv
    graph = load_json(GRAPH, {})
    nodes = [n for n in graph.get('nodes', []) if n.get('date_source') != 'arxiv-api']
    catalog = {n['id']: n for n in load_json(CATALOG, [])}
    print(f'opening {len(nodes)} non-arXiv-API articles live\n', flush=True)
    overrides = load_json(KNOWN_META, {})
    report = []
    updates = 0
    started = time.monotonic()
    for i, node in enumerate(nodes, 1):
        cat = catalog.get(node['id'], {})
        node = {**cat, **node}
        print(
            f'[{i:3d}/{len(nodes)}] {node["id"][:70]}',
            flush=True,
        )
        print(
            f'    now {node.get("date")} ({node.get("date_source")})  '
            f'{node.get("label", "")[:55]}',
            flush=True,
        )
        candidates: list[tuple[str, str]] = []
        if node.get('kind') == 'doi':
            cr = crossref_date(node['id'].split(':', 1)[1])
            if cr:
                candidates.append(cr)
        elif node.get('kind') == 'openreview':
            od = openreview_date(node['id'].split(':', 1)[1])
            if od:
                candidates.append(od)
        elif host_of((node.get('urls') or [''])[0]) == 'github.com':
            gd = github_date(node['urls'][0])
            if gd:
                candidates.append(gd)
        for url in page_urls(node)[:2]:
            html = live_html(url, node['id'])
            if html:
                candidates.extend(dates_from_html(html))
        picked = pick_date(candidates)
        if picked:
            page_date, page_src = picked
            print(f'    page {page_date} ({page_src})', flush=True)
        else:
            page_date, page_src = None, None
            print('    page NONE', flush=True)
        current = node.get('date')
        source = node.get('date_source')
        action = 'keep'
        if page_date and page_date != current:
            if current and page_date > current and not is_coarse(current, source):
                action = 'keep-earlier'
                print(f'    keep earlier first-public {current}', flush=True)
            else:
                action = 'update'
                print(f'    UPDATE {current} -> {page_date}', flush=True)
                if apply:
                    rec = overrides.get(node['id']) or {}
                    rec['date'] = page_date
                    rec['date_source'] = 'page'
                    overrides[node['id']] = rec
                    updates += 1
        elif page_date:
            print('    ok', flush=True)
        report.append({
            'id': node['id'],
            'label': node.get('label'),
            'current': current,
            'source': source,
            'page': page_date,
            'page_src': page_src,
            'action': action,
        })
        print(flush=True)
    out = ASSETS / 'date_check.json'
    dump_json(out, report)
    if apply and updates:
        dump_json(KNOWN_META, overrides)
        print(f'wrote {updates} dates to {KNOWN_META.name}')
    elapsed = time.monotonic() - started
    changed = sum(1 for r in report if r['action'] == 'update')
    print(
        f'done in {elapsed:.0f}s  {len(nodes)} pages  '
        f'{changed} would-update  report {out.name}',
        flush=True,
    )


if __name__ == '__main__':
    main()
