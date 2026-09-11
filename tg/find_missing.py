'''Find readme papers that lack a Telegram badge and look them up.

    python tg/find_missing.py
'''

from __future__ import annotations

import re
import sys
from pathlib import Path

_TG = Path(__file__).resolve().parent
_ROOT = _TG.parent
_SRC = _ROOT / 'src'
sys.path[:] = [
    p for p in sys.path if Path(p).resolve() != _TG.resolve()
]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from common import ARXIV_META, README, dump_json, load_json  # noqa: E402
from parse_readme import (  # noqa: E402
    SEGMENT_SPLIT,
    apply_known_metadata,
    build_catalog,
    fetch_arxiv_meta,
    iter_bullets,
    segment_label,
)
from tg.common import DB, configure_stdio, open_db  # noqa: E402
from tg.find import (  # noqa: E402
    format_md,
    is_paper_alias,
    post_ref,
    search_many,
    significant_words,
)

OUT = _ROOT / 'tg_link_choices.md'
SKIP_LABELS = {'litmaps'}
PAREN_RE = re.compile(r'\(([^)]+)\)')
COLON_RE = re.compile(r'^(.{4,}?):\s+(.+)$')
BADGE_HREF = re.compile(r'\[(?:⌲ )?tg\]\((https?://[^)]+)\)', re.I)

SECTION_ORDER = (
    ('dedicated', 'Dedicated posts'),
    ('digest', 'Only digests found'),
    ('title', 'Title matches only — verify'),
    ('empty', 'No posts found'),
)


def public_urls(hits: list[dict]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for hit in hits:
        for url in (
            hit['original_url'] if hit.get('original_public') else None,
            hit['url'] if hit.get('public') else None,
        ):
            if url and url not in seen:
                seen.add(url)
                out.append(url)
    return out


def is_numeric_label(label: str) -> bool:
    return bool(label) and label[0].isdigit()


def display_title(node: dict, catalog: list[dict]) -> str:
    label = node.get('label') or node.get('title') or node['id']
    if not is_numeric_label(label):
        return label
    order = node.get('order', 0)
    parent = ''
    for prev in catalog:
        if prev.get('order', 0) >= order:
            break
        prev_label = prev.get('label') or prev.get('title') or ''
        if prev_label and not is_numeric_label(prev_label):
            parent = prev_label
    if parent:
        return f'{parent} · {label}'
    return label


def join_titles(titles: list[str]) -> str:
    if len(titles) == 1:
        return titles[0]
    parts = [title.split(' · ', 1) for title in titles]
    if all(len(part) == 2 for part in parts):
        parents = {part[0] for part in parts}
        if len(parents) == 1:
            parent = parts[0][0]
            tails = ' · '.join(part[1] for part in parts)
            return f'{parent} · {tails}'
    return ' · '.join(titles)


def has_real_title(node: dict) -> bool:
    title = (node.get('title') or '').strip()
    if not title or title.startswith('http'):
        return False
    label = (node.get('label') or '').strip()
    if title.casefold() != label.casefold():
        return True
    return node.get('date_source') == 'arxiv-api'


def enrich_titles(nodes: dict) -> None:
    apply_known_metadata(nodes)
    want: list[str] = []
    seen: set[str] = set()
    for node in nodes.values():
        if node.get('telegram'):
            continue
        if (node.get('label') or '').casefold() in SKIP_LABELS:
            continue
        if node.get('kind') != 'arxiv' or has_real_title(node):
            continue
        arxiv_id = node['id'].split(':', 1)[1]
        if arxiv_id in seen:
            continue
        seen.add(arxiv_id)
        want.append(arxiv_id)
    if not want:
        print('titles: all missing papers already have metadata', flush=True)
        return
    print(
        f'{len(want)} arXiv ids lack titles, querying arXiv API',
        flush=True,
    )
    fetched = fetch_arxiv_meta(want)
    if not fetched:
        print('arxiv api returned no titles', flush=True)
        return
    cache = load_json(ARXIV_META, {})
    cache.update(fetched)
    dump_json(ARXIV_META, cache)
    apply_known_metadata(nodes)
    print(f'cached {len(fetched)} titles in {ARXIV_META.name}', flush=True)


def query_strings(node: dict) -> list[str]:
    queries: list[str] = []
    seen: set[str] = set()

    def add(value: str) -> None:
        value = ' '.join((value or '').split()).strip(' -—:')
        if not value or value.casefold() in SKIP_LABELS:
            return
        key = value.casefold()
        if key in seen:
            return
        seen.add(key)
        queries.append(value)

    for url in node.get('urls') or []:
        add(url)

    title = (node.get('title') or '').strip()
    label = (node.get('label') or '').strip()
    if (
        title
        and not title.startswith('http')
        and title.casefold() != label.casefold()
    ):
        add(title)

    if label and not is_numeric_label(label):
        add(label)
        bare = ' '.join(PAREN_RE.sub(' ', label).split()).strip(' -—:')
        if bare and not is_numeric_label(bare):
            add(bare)

    for match in PAREN_RE.finditer(label):
        name = ' '.join(match.group(1).split())
        if is_paper_alias(name):
            add(name)

    colon = COLON_RE.match(label)
    if colon:
        head = colon.group(1).strip()
        tail = colon.group(2).strip()
        if is_paper_alias(head) or len(significant_words(head)) >= 2:
            add(head)
        if is_paper_alias(tail):
            add(tail)

    return queries


def existing_badges() -> dict[str, str]:
    mapping: dict[str, str] = {}
    text = README.read_text(encoding='utf-8')
    for _section, bullet in iter_bullets(text):
        for segment in bullet.split(SEGMENT_SPLIT):
            label = segment_label(segment) or ''
            for match in BADGE_HREF.finditer(segment):
                ref = post_ref(match.group(1))
                if not ref:
                    continue
                key = ref.lower()
                if label and (
                    key not in mapping or len(label) > len(mapping[key])
                ):
                    mapping[key] = label
                elif key not in mapping:
                    mapping[key] = ''
    return mapping


def _already_other(
    hit: dict,
    already: dict[str, str],
    label: str,
) -> bool:
    for url in (hit.get('url'), hit.get('original_url')):
        ref = post_ref(url)
        if not ref:
            continue
        other = already.get(ref.lower(), '')
        if other and other.casefold() != (label or '').casefold():
            return True
    return False


def classify_bucket(
    hits: list[dict],
    already: dict[str, str],
    label: str,
) -> str:
    if not hits or not public_urls(hits):
        return 'empty'
    own_key = any(
        hit.get('match_mode') == 'keys'
        and not hit.get('is_digest')
        and not _already_other(hit, already, label)
        for hit in hits
    )
    if own_key:
        return 'dedicated'
    if any(not hit.get('is_digest') for hit in hits):
        return 'title'
    return 'digest'


def core_urls(hits: list[dict]) -> tuple[str, ...]:
    dedicated = [hit for hit in hits if not hit.get('is_digest')]
    return tuple(public_urls(dedicated or hits))


def _title_parent(title: str) -> str | None:
    if ' · ' in title:
        return title.split(' · ', 1)[0]
    return None


def _are_siblings(prev: dict, item: dict) -> bool:
    parent_a = _title_parent(prev['titles'][0])
    parent_b = _title_parent(item['title'])
    return bool(parent_a and parent_a == parent_b)


def collapse_groups(items: list[dict]) -> list[dict]:
    groups: list[dict] = []
    for item in items:
        urls = core_urls(item['hits'])
        if groups and urls:
            prev = groups[-1]
            if (
                item['node'].get('section') == prev['node'].get('section')
                and item['bucket'] == prev['bucket']
                and urls == core_urls(prev['hits'])
                and _are_siblings(prev, item)
            ):
                prev['titles'].append(item['title'])
                prev['last_order'] = item['node'].get('order', 0)
                continue
        groups.append({
            'node': item['node'],
            'titles': [item['title']],
            'hits': item['hits'],
            'mode': item['mode'],
            'bucket': item['bucket'],
            'last_order': item['node'].get('order', 0),
        })
    return groups


def main() -> None:
    configure_stdio()
    if not DB.exists():
        raise SystemExit(f'{DB} is missing. Run: python tg/export.py')
    catalog = build_catalog()
    enrich_titles(catalog)
    already = existing_badges()
    ordered = sorted(catalog.values(), key=lambda n: n.get('order', 0))
    missing = [
        node for node in ordered
        if not node.get('telegram')
        and (node.get('label') or '').casefold() not in SKIP_LABELS
    ]
    print(
        f'readme papers without tg badge: {len(missing)} / {len(catalog)}',
        flush=True,
    )

    conn = open_db()
    items: list[dict] = []
    counts = {'dedicated': 0, 'digest': 0, 'title': 0, 'empty': 0}
    total = len(missing)
    for index, node in enumerate(missing, start=1):
        hits, mode = search_many(conn, query_strings(node), limit=8)
        urls = public_urls(hits)
        if not urls:
            hits, mode = [], 'none'
        bucket = classify_bucket(
            hits,
            already,
            node.get('label') or '',
        )
        counts[bucket] += 1
        items.append({
            'node': node,
            'hits': hits,
            'mode': mode,
            'title': display_title(node, ordered),
            'bucket': bucket,
        })
        pct = 100 * index / total if total else 100
        print(
            f'\rlookup {index}/{total} ({pct:.0f}%)  '
            f'dedicated={counts["dedicated"]}  '
            f'digest={counts["digest"]}  '
            f'title={counts["title"]}  '
            f'none={counts["empty"]}',
            end='',
            flush=True,
        )
    print(flush=True)
    conn.close()

    groups = collapse_groups(items)
    lines = [
        '# Telegram posts still needing a pick',
        '',
        'Full public links. Reply with `paper: handle/id` (or `skip`) for each.',
        'Use `both:` plus two links when you want both badges.',
        '',
        '`[digest]` = link dump / weekly digest. '
        '`[title match]` = no paper id in the post, verify. '
        '`[already badge for …]` = this post is already used on another paper.',
        '',
    ]
    by_bucket: dict[str, list[dict]] = {
        key: [] for key, _ in SECTION_ORDER
    }
    for group in groups:
        by_bucket[group['bucket']].append(group)

    for key, heading in SECTION_ORDER:
        section = by_bucket[key]
        if not section:
            continue
        lines.append(f'## {heading}')
        lines.append('')
        if key == 'empty':
            for group in section:
                node = group['node']
                url = node['urls'][0] if node['urls'] else node['id']
                lines.append(f'- {group["titles"][0]} — {url}')
            lines.append('')
            continue
        for group in section:
            title = join_titles(group['titles'])
            lines.append(
                format_md(
                    title,
                    group['hits'],
                    group['mode'],
                    heading='###',
                    already=already,
                ).rstrip()
            )
            lines.append('')

    OUT.write_text('\n'.join(lines), encoding='utf-8')
    collapsed = len(items) - len(groups)
    print(
        f'wrote {OUT.name}: '
        f'{counts["dedicated"]} dedicated, '
        f'{counts["digest"]} digest-only, '
        f'{counts["title"]} title-only, '
        f'{counts["empty"]} still missing'
        + (f' ({collapsed} collapsed)' if collapsed else ''),
        flush=True,
    )


if __name__ == '__main__':
    main()
