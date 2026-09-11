'''Turn readme.md into assets/catalog.json - one node per list entry.

A bullet may hold several entries separated by ' * ' (middle dot); a segment
starts a new entry when it carries its own `Label - [url]` prefix, otherwise
its links become aliases of the previous entry.

Run:  python src/parse_readme.py [--offline]
'''

import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path
from xml.etree import ElementTree

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import (  # noqa: E402
    ARXIV_META, ASSETS, CATALOG, KNOWN_META, PAGE_META, README, ROOT,
    apply_date_overrides, arxiv_date, classify, dump_json, is_skippable,
    load_json, node_arxiv_ids,
)

TITLE_SOURCES = ('papers_titles.json', 'added_titles.json')
ARXIV_API = 'http://export.arxiv.org/api/query'
NS = {'a': 'http://www.w3.org/2005/Atom'}

# One level of parentheses is allowed (Cell/Elsevier article ids).
LINK_RE = re.compile(
    r'\[(?P<text>[^\]]*)\]\((?P<url>https?://(?:[^()\s]+|\([^()\s]*\))+)\)'
)
TG_BADGE_RE = re.compile(r'\[⌲[^\]]*\]\([^)]*\)')
BARE_URL_RE = re.compile(r'(?<![(\[])\bhttps?://[^\s<>"\')\]]+')
LABEL_RE = re.compile(r'^\s*(?P<label>[^\[].*?)\s+—\s+(?=\[|https?://)')
SEGMENT_SPLIT = ' · '
URL_DATE_RES = (
    re.compile(r'/(20\d{2})[-/](\d{2})[-/](\d{2})'),
    re.compile(r'/(20\d{2})[-/](\d{2})(?:/|$)'),
    re.compile(r'/(20\d{2})(?:/|$)'),
)
MONTHS = {
    'january': '01', 'jan': '01', 'february': '02', 'feb': '02',
    'march': '03', 'mar': '03', 'april': '04', 'apr': '04',
    'may': '05', 'june': '06', 'jun': '06', 'july': '07', 'jul': '07',
    'august': '08', 'aug': '08', 'september': '09', 'sep': '09',
    'october': '10', 'oct': '10', 'november': '11', 'nov': '11',
    'december': '12', 'dec': '12',
}
LABEL_MONTH_RE = re.compile(
    r'\b(' + '|'.join(MONTHS) + r')\s+(20\d{2})\b',
    re.I,
)


def iter_bullets(text: str):
    '''Yield `(section, bullet_text)`, joining wrapped continuation lines.'''
    section = 'Uncategorised'
    buffer: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith('## '):
            if buffer:
                yield section, ' '.join(buffer)
                buffer = []
            section = stripped[3:].strip()
            continue
        if stripped.startswith('- '):
            if buffer:
                yield section, ' '.join(buffer)
            buffer = [stripped[2:].strip()]
            continue
        if not buffer:
            continue
        if not stripped or stripped.startswith(('#', '---', '```')):
            yield section, ' '.join(buffer)
            buffer = []
            continue
        buffer.append(stripped)
    if buffer:
        yield section, ' '.join(buffer)


def segment_urls(segment: str) -> list[str]:
    urls = [m.group('url') for m in LINK_RE.finditer(segment)]
    urls += BARE_URL_RE.findall(LINK_RE.sub(' ', segment))
    seen, out = set(), []
    for url in urls:
        url = url.rstrip('.,;:')
        if url in seen or is_skippable(url):
            continue
        seen.add(url)
        out.append(url)
    return out


def segment_label(segment: str) -> str | None:
    match = LABEL_RE.match(segment)
    if not match:
        return None
    label = LINK_RE.sub(lambda m: m.group('text'), match.group('label'))
    return ' '.join(label.split()).strip(' -—:')


def starts_entry(label: str | None) -> bool:
    '''Only treat a segment label as a new entry if it looks like a name.'''
    if not label or len(label) < 2:
        return False
    return any(ch.isdigit() or ch.isupper() for ch in label)


def date_from_label(label: str) -> str | None:
    '''Month + year in the readme label, e.g. (October 2025).'''
    match = LABEL_MONTH_RE.search(label or '')
    if not match:
        return None
    return f'{match.group(2)}-{MONTHS[match.group(1).lower()]}-01'


def date_from_url(url: str) -> str | None:
    for index, pattern in enumerate(URL_DATE_RES):
        match = pattern.search(url)
        if not match:
            continue
        year = match.group(1)
        month = match.group(2) if index < 2 else '01'
        day = match.group(3) if index == 0 else '01'
        if not 1 <= int(month) <= 12 or not 1 <= int(day) <= 31:
            continue
        return f'{year}-{month}-{day}'
    return None


def build_catalog() -> dict:
    nodes: dict[str, dict] = {}
    order = 0
    skipped = 0

    for section, bullet in iter_bullets(README.read_text(encoding='utf-8')):
        previous: str | None = None
        for index, segment in enumerate(bullet.split(SEGMENT_SPLIT)):
            has_tg = bool(TG_BADGE_RE.search(segment))
            clean = TG_BADGE_RE.sub(' ', segment)
            urls = segment_urls(clean)
            if not urls:
                skipped += 1
                continue
            label = segment_label(clean)
            if index and not starts_entry(label) and previous:
                nodes[previous]['urls'].extend(
                    u for u in urls if u not in nodes[previous]['urls']
                )
                if has_tg:
                    nodes[previous]['telegram'] = True
                continue

            classified = classify(urls[0])
            if not classified:
                skipped += 1
                continue
            kind, node_id = classified
            if node_id in nodes:
                node = nodes[node_id]
                node['urls'].extend(u for u in urls if u not in node['urls'])
                if has_tg:
                    node['telegram'] = True
                previous = node_id
                continue

            nodes[node_id] = {
                'id': node_id,
                'kind': kind,
                'label': label or urls[0],
                'title': label or urls[0],
                'section': section,
                'urls': urls,
                'order': order,
                'authors': [],
                'date': None,
                'date_source': None,
            }
            if has_tg:
                nodes[node_id]['telegram'] = True
            order += 1
            previous = node_id

    print(f'parsed {len(nodes)} entries ({skipped} link-less segments skipped)')
    return nodes


def apply_known_metadata(nodes: dict) -> list[str]:
    known: dict[str, dict] = {}
    for name in TITLE_SOURCES:
        known.update(load_json(ASSETS / name, {}))
    known.update(load_json(ARXIV_META, {}))
    overrides = load_json(KNOWN_META, {})

    missing = []
    for node_id, node in nodes.items():
        if node['kind'] == 'arxiv':
            arxiv_id = node_id.split(':', 1)[1]
            info = known.get(arxiv_id)
            if info:
                node['title'] = info.get('title') or node['title']
                node['authors'] = info.get('authors') or []
                node['date'] = info.get('published') or None
                node['date_source'] = 'arxiv-api'
            else:
                missing.append(arxiv_id)
            if not node['date']:
                node['date'] = arxiv_date(arxiv_id)
                node['date_source'] = 'arxiv-id'
        if not node['date']:
            for url in node['urls']:
                guess = date_from_url(url)
                if guess:
                    node['date'] = guess
                    node['date_source'] = 'url'
                    break
        label_date = date_from_label(node['label'])
        if label_date and (
            not node['date']
            or (node.get('date_source') == 'url'
                and node['date'].endswith('-01-01'))
        ):
            node['date'] = label_date
            node['date_source'] = 'label'
        apply_date_overrides(node, known, overrides)
        for aid in node_arxiv_ids(node, overrides):
            if aid not in known and aid not in missing:
                missing.append(aid)
    return missing


def hinted_arxiv_ids() -> list[str]:
    '''arXiv ids that redirects exposed during an earlier fetch run.'''
    ids = []
    for meta in load_json(PAGE_META, {}).values():
        resolved = meta.get('resolved')
        classified = classify(resolved) if resolved else None
        if classified and classified[0] == 'arxiv':
            ids.append(classified[1].split(':', 1)[1])
    return ids


def fetch_arxiv_meta(ids: list[str]) -> dict:
    '''Resolve unknown arXiv ids through the arXiv API, in batches.'''
    out: dict[str, dict] = {}
    size = 40
    for start in range(0, len(ids), size):
        batch = ids[start:start + size]
        query = urllib.parse.urlencode(
            {'id_list': ','.join(batch), 'max_results': len(batch)}
        )
        try:
            with urllib.request.urlopen(f'{ARXIV_API}?{query}', timeout=60) as resp:
                root = ElementTree.fromstring(resp.read())
        except Exception as exc:  # noqa: BLE001
            print(f'  batch {start} failed: {exc}', flush=True)
            continue
        for entry in root.findall('a:entry', NS):
            url = entry.findtext('a:id', default='', namespaces=NS)
            match = re.search(r'abs/(.+?)(?:v\d+)?$', url)
            if not match:
                continue
            out[match.group(1)] = {
                'title': ' '.join(
                    entry.findtext('a:title', default='', namespaces=NS).split()
                ),
                'published': entry.findtext(
                    'a:published', default='', namespaces=NS
                )[:10],
                'authors': [
                    a.findtext('a:name', default='', namespaces=NS)
                    for a in entry.findall('a:author', NS)
                ][:4],
            }
        print(f'  arxiv api: {min(start + size, len(ids))}/{len(ids)} '
              f'resolved={len(out)}', flush=True)
        time.sleep(3)
    return out


def main() -> None:
    offline = '--offline' in sys.argv
    nodes = build_catalog()
    missing = apply_known_metadata(nodes)

    known_ids = set(load_json(ARXIV_META, {}))
    for name in TITLE_SOURCES:
        known_ids |= set(load_json(ASSETS / name, {}))
    missing += [i for i in hinted_arxiv_ids()
                if i not in known_ids and i not in missing]

    if missing and not offline:
        print(f'{len(missing)} arXiv ids lack metadata, querying arXiv API')
        fetched = fetch_arxiv_meta(missing)
        if fetched:
            cache = load_json(ARXIV_META, {})
            cache.update(fetched)
            dump_json(ARXIV_META, cache)
            apply_known_metadata(nodes)
    elif missing:
        print(f'{len(missing)} arXiv ids lack metadata (offline mode)')

    by_kind: dict[str, int] = {}
    undated = 0
    for node in nodes.values():
        by_kind[node['kind']] = by_kind.get(node['kind'], 0) + 1
        undated += node['date'] is None
    dump_json(CATALOG, list(nodes.values()))
    print(f'wrote {CATALOG.relative_to(ROOT)}: {len(nodes)} nodes, '
          f'{undated} without a date')
    print('by kind: ' + ', '.join(f'{k}={v}' for k, v in sorted(by_kind.items())))


if __name__ == '__main__':
    main()
