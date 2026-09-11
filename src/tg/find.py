'''Look up t.me posts for a paper URL, arXiv id, DOI, or title.

    python src/tg/find.py https://arxiv.org/abs/2503.14858
    python src/tg/find.py 2503.14858 --badge
    python src/tg/find.py "1000 Layer Networks" --md
'''

from __future__ import annotations

import argparse
import re
import sqlite3
import sys
from pathlib import Path

from common import (
    DB,
    badge_for,
    keys_from_query,
    open_db,
    public_post_url,
)


def configure_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, 'reconfigure', None)
        if reconfigure is None:
            continue
        try:
            reconfigure(encoding='utf-8', errors='replace')
        except Exception:  # noqa: BLE001
            pass


FTS_SPECIAL = re.compile(r'''["'*:()^+\-{}[\]@~]''')
WORD_RE = re.compile(r'[A-Za-z0-9]{3,}')
STOP = {
    'the', 'and', 'for', 'with', 'from', 'that', 'this', 'are', 'was',
    'were', 'via', 'into', 'your', 'how', 'why', 'what', 'when', 'who',
    'not', 'can', 'its', 'our', 'their', 'than', 'then', 'but', 'all',
    'any', 'out', 'new', 'old', 'using', 'use', 'used', 'paper',
    'arxiv', 'abs', 'pdf', 'html', 'https', 'http', 'www', 'com',
    'org', 'net',
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Find t.me posts that mention a paper',
    )
    parser.add_argument(
        'queries',
        nargs='+',
        help='paper URL, arXiv id, DOI, or title words',
    )
    parser.add_argument('--limit', type=int, default=10)
    parser.add_argument(
        '--badge',
        action='store_true',
        help='print [⌲ tg](...) translate.goog badges for public posts',
    )
    parser.add_argument(
        '--md',
        action='store_true',
        help='print a tg_link_choices.md-style block',
    )
    parser.add_argument(
        '--db',
        type=Path,
        default=None,
        help='sqlite path (default: tg/ml_folder.sqlite)',
    )
    return parser.parse_args()


def fts_phrase(query: str) -> str:
    cleaned = ' '.join(FTS_SPECIAL.sub(' ', query).split())
    if not cleaned:
        return ''
    return f'"{cleaned}"'


def fts_and(query: str) -> str:
    words = []
    seen: set[str] = set()
    for word in WORD_RE.findall(query):
        low = word.lower()
        if low in STOP or low in seen:
            continue
        seen.add(low)
        words.append(word)
    return ' AND '.join(words)


def _row_to_hit(row: sqlite3.Row) -> dict:
    username = row['username']
    url, public = public_post_url(username, row['channel_id'], row['id'])
    orig = None
    orig_public = False
    if row['fwd_post_id']:
        orig, orig_public = public_post_url(
            row['fwd_username'],
            row['fwd_channel_id'] or 0,
            row['fwd_post_id'],
        )
        if not row['fwd_username'] and not row['fwd_channel_id']:
            orig = None
    return {
        'channel_id': row['channel_id'],
        'id': row['id'],
        'date': (row['date'] or '')[:10],
        'text': row['text'] or '',
        'username': username,
        'title': row['title'] or username or str(row['channel_id']),
        'url': url,
        'public': public,
        'is_forward': row['fwd_post_id'] is not None,
        'fwd_name': row['fwd_name'],
        'original_url': orig,
        'original_public': orig_public,
    }


HIT_SQL = '''
SELECT m.channel_id, m.id, m.date, m.text,
       m.fwd_username, m.fwd_post_id, m.fwd_channel_id, m.fwd_name,
       c.username, c.title
FROM {from_sql}
WHERE {where_sql}
ORDER BY (m.fwd_post_id IS NULL) DESC, m.date DESC
LIMIT ?
'''


def _fetch_keys(conn: sqlite3.Connection, keys: set[str], limit: int) -> list[dict]:
    if not keys:
        return []
    placeholders = ','.join('?' * len(keys))
    sql = HIT_SQL.format(
        from_sql=(
            'paper_keys k '
            'JOIN messages m ON m.channel_id = k.channel_id AND m.id = k.msg_id '
            'JOIN channels c ON c.id = m.channel_id'
        ),
        where_sql=f'k.key IN ({placeholders})',
    )
    rows = conn.execute(sql, (*keys, limit)).fetchall()
    return _dedupe_hits(_row_to_hit(r) for r in rows)


def _fetch_fts(conn: sqlite3.Connection, match: str, limit: int) -> list[dict]:
    if not match:
        return []
    sql = HIT_SQL.format(
        from_sql=(
            'fts '
            'JOIN messages m ON m.channel_id = fts.channel_id AND m.id = fts.msg_id '
            'JOIN channels c ON c.id = m.channel_id'
        ),
        where_sql='fts MATCH ?',
    )
    try:
        rows = conn.execute(sql, (match, limit)).fetchall()
    except sqlite3.OperationalError:
        return []
    return _dedupe_hits(_row_to_hit(r) for r in rows)


def _dedupe_hits(hits) -> list[dict]:
    seen: set[tuple[int, int]] = set()
    out: list[dict] = []
    for hit in hits:
        key = (hit['channel_id'], hit['id'])
        if key in seen:
            continue
        seen.add(key)
        out.append(hit)
    return out


def search(
    conn: sqlite3.Connection,
    query: str,
    limit: int = 10,
) -> tuple[list[dict], str]:
    '''Return (hits, mode) where mode is keys / fts-phrase / fts-and / none.'''
    keys = keys_from_query(query)
    if keys:
        hits = _fetch_keys(conn, keys, limit)
        if hits:
            return hits, 'keys'
    phrase = fts_phrase(query)
    hits = _fetch_fts(conn, phrase, limit)
    if hits:
        return hits, 'fts-phrase'
    and_q = fts_and(query)
    if and_q and and_q != phrase.strip('"'):
        hits = _fetch_fts(conn, and_q, limit)
        if hits:
            return hits, 'fts-and'
    return [], 'none'


def _snippet(text: str, width: int = 160) -> str:
    flat = ' '.join(text.split())
    if len(flat) <= width:
        return flat
    return flat[: width - 1].rstrip() + '…'


def format_hit(hit: dict, badge: bool = False) -> str:
    extra = ''
    if not hit['public']:
        extra = '  [private, no public badge]'
    line = (
        f'{hit["url"]}  {hit["date"]}  {hit["title"]}  '
        f'«{_snippet(hit["text"])}»{extra}'
    )
    parts = [line]
    if hit['original_url']:
        src = hit['fwd_name'] or 'forward'
        priv = '' if hit['original_public'] else '  [private]'
        parts.append(f'  original ({src}): {hit["original_url"]}{priv}')
    if badge:
        mark = badge_for(hit['username'], hit['id'])
        if mark:
            parts.append(f'  {mark}')
        elif hit['original_public'] and hit['original_url']:
            # badge the public original of a private/forwarded copy
            handle = hit['original_url'].rstrip('/').split('/')[-2]
            post_id = hit['original_url'].rstrip('/').split('/')[-1]
            mark = badge_for(handle, int(post_id))
            if mark:
                parts.append(f'  {mark}')
    return '\n'.join(parts)


def format_md(title: str, hits: list[dict]) -> str:
    lines = [f'## {title}', '']
    if not hits:
        lines.append('_no public posts found_')
        lines.append('')
        return '\n'.join(lines)
    seen: set[str] = set()
    for hit in hits:
        url = hit['url'] if hit['public'] else None
        if url and url not in seen:
            seen.add(url)
            lines.append(url)
        orig = hit['original_url'] if hit['original_public'] else None
        if orig and orig not in seen:
            seen.add(orig)
            lines.append(orig)
    if len(lines) == 2:
        lines.append('_no public posts found_')
    lines.append('')
    return '\n'.join(lines)


def main() -> None:
    configure_stdio()
    args = parse_args()
    db_path = args.db or DB
    if not db_path.exists():
        raise SystemExit(
            f'{db_path} is missing. Run: python src/tg/export.py'
        )
    conn = open_db(db_path)
    any_hits = False
    for query in args.queries:
        hits, mode = search(conn, query, args.limit)
        if args.md:
            print(format_md(query, hits), end='')
            any_hits = any_hits or bool(hits)
            continue
        print(f'# {query}  [{mode}, {len(hits)} hit(s)]')
        if not hits:
            print('  no posts found')
            print()
            continue
        any_hits = True
        for hit in hits:
            print(format_hit(hit, badge=args.badge))
        print()
    conn.close()
    if not any_hits:
        sys.exit(1)


if __name__ == '__main__':
    main()
