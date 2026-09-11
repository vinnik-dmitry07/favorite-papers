'''Parse readme.md into scoreable papers and attach Telegram posts.

    python filter/collect_readme.py
'''

from __future__ import annotations

import sys
from pathlib import Path

FILTER_DIR = Path(__file__).resolve().parent
ROOT = FILTER_DIR.parent
SRC = ROOT / 'src'
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(SRC))
sys.path.insert(0, str(FILTER_DIR))

from parse_readme import build_catalog  # noqa: E402
from tg.common import DB, open_db  # noqa: E402
from tg.find import fetch_hits_by_keys  # noqa: E402

from paths import (  # noqa: E402
    PAPERS_JSONL,
    README,
    SCOREABLE_KINDS,
    print_progress,
    tg_lookup_keys,
    write_jsonl,
)


def fetch_tg_posts(conn, node_id: str) -> list[dict]:
    keys = tg_lookup_keys(node_id)
    if not keys or not DB.exists():
        return []
    hits = fetch_hits_by_keys(conn, set(keys), limit=20)
    return [
        {
            'channel': hit['username'] or hit['title'] or str(hit['channel_id']),
            'msg_id': hit['id'],
            'date': hit['date'],
            'url': hit['url'],
            'public': hit['public'],
        }
        for hit in hits
    ]


def readme_line_index() -> dict[str, int]:
    '''Map a paper URL fragment to the 1-based readme line that first mentions it.'''
    index: dict[str, int] = {}
    for number, line in enumerate(
        README.read_text(encoding='utf-8').splitlines(), start=1,
    ):
        if 'http' not in line and '10.' not in line:
            continue
        for url in line.split(']('):
            if url not in index and ('http' in url or url.startswith('10.')):
                index[url.split(')')[0]] = number
    return index


def line_no_for(urls: list[str], index: dict[str, int]) -> int | None:
    for url in urls:
        if url in index:
            return index[url]
        for key, number in index.items():
            if url in key or key in url:
                return number
    return None


def main() -> None:
    nodes = build_catalog()
    line_index = readme_line_index()
    conn = open_db() if DB.exists() else None
    if conn is None:
        print('tg/ml_folder.sqlite missing; tg_posts will be empty', flush=True)

    rows = []
    skipped = 0
    total = len(nodes)
    for index, node in enumerate(nodes.values(), start=1):
        if node['kind'] not in SCOREABLE_KINDS:
            skipped += 1
            print_progress(index, total, f'skip={skipped} keep={len(rows)}')
            continue
        row = {
            'key': node['id'],
            'kind': node['kind'],
            'section': node['section'],
            'line_title': node.get('label') or node.get('title'),
            'urls': node['urls'],
            'readme_line_no': line_no_for(node['urls'], line_index),
            'order': node.get('order'),
            'tg_posts': fetch_tg_posts(conn, node['id']) if conn else [],
        }
        rows.append(row)
        print_progress(index, total, f'skip={skipped} keep={len(rows)}')

    if conn is not None:
        conn.close()

    write_jsonl(PAPERS_JSONL, rows)
    with_tg = sum(1 if row['tg_posts'] else 0 for row in rows)
    print(
        f'wrote {PAPERS_JSONL}: {len(rows)} papers, '
        f'{skipped} web/repo skipped, {with_tg} with tg posts',
        flush=True,
    )


if __name__ == '__main__':
    main()
