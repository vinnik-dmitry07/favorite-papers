'''Look up t.me posts for a paper URL, arXiv id, DOI, or title.

    python tg/find.py https://arxiv.org/abs/2503.14858
    python tg/find.py 2503.14858 --badge
    python tg/find.py "1000 Layer Networks" --md
'''

from __future__ import annotations

import argparse
import re
import sqlite3
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

from tg.common import (  # noqa: E402
    DB,
    badge_for,
    configure_stdio,
    keys_from_query,
    open_db,
    public_post_url,
)

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
DIGEST_HEAD = re.compile(
    r'(?is)^\s*(links for|some links|#\s*дайджест|#\s*digest|дайджест\b)',
)
DIGEST_NEAR = re.compile(r'(?i)подборка')
POST_REF_RE = re.compile(
    r'(?:t-me\.translate\.goog/s|t\.me)/([A-Za-z0-9_]+)/(\d+)',
)
TITLE_COVERAGE_MIN = 1.0
TITLE_AND_MIN_WORDS = 4
TITLE_SPAN_MAX = 120
DIGEST_KEY_COUNT = 6
YEAR_RE = re.compile(r'^\d{4}$')
MONTH_YEAR_RE = re.compile(r'^[A-Za-z]+\s+20\d{2}$')
WEAK_ALIAS = {
    'google research', 'deepmind', 'meta', 'openai', 'anthropic',
    'nature', 'science', 'pnas', 'neurips', 'icml', 'iclr', 'acl',
    'workshop', 'lilian weng', 'schmidhuber', 'lecun', 'biorxiv',
    'alignment forum', 'thinking machines', 'google', 'facebook',
    'nvidia', 'microsoft', 'sometimes', 'position', 'nature 2024',
    'for sale', 'rift',
}

HIT_SELECT = '''
SELECT m.channel_id, m.id, m.date, m.text, m.views,
       m.fwd_username, m.fwd_post_id, m.fwd_channel_id, m.fwd_name,
       COALESCE(m.is_fwd, 0) AS is_fwd,
       COALESCE(m.key_count, 0) AS key_count,
       c.username, c.title
'''

KEY_SQL = HIT_SELECT + '''
FROM messages m
JOIN channels c ON c.id = m.channel_id
WHERE (m.channel_id, m.id) IN (
    SELECT channel_id, msg_id FROM paper_keys
    WHERE key IN ({placeholders})
)
ORDER BY COALESCE(m.is_fwd, 0) ASC,
         CASE WHEN COALESCE(m.key_count, 0) = 0 THEN 99
              ELSE m.key_count END ASC,
         COALESCE(m.views, 0) DESC,
         m.date DESC
LIMIT ?
'''

FTS_SQL = HIT_SELECT + '''
       , bm25(fts) AS fts_rank
FROM fts
JOIN messages m ON m.rowid = fts.rowid
JOIN channels c ON c.id = m.channel_id
WHERE fts MATCH ?
ORDER BY COALESCE(m.is_fwd, 0) ASC,
         bm25(fts) ASC,
         CASE WHEN COALESCE(m.key_count, 0) = 0 THEN 99
              ELSE m.key_count END ASC,
         COALESCE(m.views, 0) DESC,
         m.date DESC
LIMIT ?
'''


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


def significant_words(query: str) -> list[str]:
    words = []
    seen: set[str] = set()
    for word in WORD_RE.findall(query):
        low = word.lower()
        if low in STOP or low in seen:
            continue
        seen.add(low)
        words.append(low)
    return words


def fts_and(query: str) -> str:
    return ' AND '.join(significant_words(query))


def _word_in_text(word: str, text: str) -> bool:
    return bool(
        re.search(
            r'(?<![A-Za-z0-9])' + re.escape(word) + r'(?![A-Za-z0-9])',
            text,
            flags=re.I,
        )
    )


def is_paper_alias(name: str) -> bool:
    name = ' '.join((name or '').split()).strip(' -—:')
    if len(name) < 4 or len(name) > 40:
        return False
    if YEAR_RE.fullmatch(name) or MONTH_YEAR_RE.fullmatch(name):
        return False
    if name.casefold() in WEAK_ALIAS:
        return False
    if re.search(r'[\d+\-]', name) or (
        '.' in name and not name.replace('.', '').isdigit()
    ):
        return True
    letters = re.sub(r'[^A-Za-z]', '', name)
    if re.search(r'[A-Z]{2,}', name) and len(letters) >= 5:
        return True
    if re.search(r'[a-z][A-Z]', name):
        return True
    if re.match(r'Dr\.\s+\S', name):
        return True
    return False


def is_specific_query(query: str) -> bool:
    if keys_from_query(query):
        return True
    if is_paper_alias(query):
        return True
    return len(significant_words(query)) >= 2


def title_coverage(query: str, text: str) -> float:
    words = significant_words(query)
    if not words:
        return 0.0
    hay = text or ''
    found = sum(1 for word in words if _word_in_text(word, hay))
    return found / len(words)


def title_span(query: str, text: str) -> int | None:
    '''Smallest character window covering one hit of every query word.'''
    words = significant_words(query)
    if not words:
        return None
    events: list[tuple[int, int]] = []
    for index, word in enumerate(words):
        pattern = (
            r'(?<![A-Za-z0-9])' + re.escape(word) + r'(?![A-Za-z0-9])'
        )
        found = False
        for match in re.finditer(pattern, text or '', flags=re.I):
            events.append((match.start(), index))
            found = True
        if not found:
            return None
    events.sort()
    count = [0] * len(words)
    have = 0
    left = 0
    best: int | None = None
    for right, (pos, word_i) in enumerate(events):
        if count[word_i] == 0:
            have += 1
        count[word_i] += 1
        while have == len(words) and left <= right:
            span = events[right][0] - events[left][0]
            if best is None or span < best:
                best = span
            left_word = events[left][1]
            count[left_word] -= 1
            if count[left_word] == 0:
                have -= 1
            left += 1
    return best


def is_digest(hit: dict) -> bool:
    if (hit.get('key_count') or 0) >= DIGEST_KEY_COUNT:
        return True
    text = hit.get('text') or ''
    if DIGEST_HEAD.match(text):
        return True
    return bool(DIGEST_NEAR.search(text[:200]))


def post_ref(url: str | None) -> str | None:
    if not url:
        return None
    match = POST_REF_RE.search(url)
    if not match:
        return None
    return f'{match.group(1)}/{match.group(2)}'


def annotate_hit(hit: dict, mode: str, query: str = '') -> dict:
    out = dict(hit)
    out['match_mode'] = mode
    out['is_digest'] = is_digest(out)
    if mode.startswith('title') and query:
        out['title_coverage'] = title_coverage(query, out.get('text') or '')
    return out


def _row_to_hit(row: sqlite3.Row) -> dict:
    username = row['username']
    url, public = public_post_url(username, row['channel_id'], row['id'])
    is_fwd = bool(row['is_fwd'])
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
        'is_forward': is_fwd,
        'fwd_name': row['fwd_name'],
        'fwd_username': row['fwd_username'],
        'fwd_post_id': row['fwd_post_id'],
        'original_url': orig,
        'original_public': orig_public,
        'key_count': row['key_count'],
        'views': row['views'],
    }


def fetch_hits_by_keys(
    conn: sqlite3.Connection,
    keys: set[str],
    limit: int = 10,
) -> list[dict]:
    if not keys:
        return []
    sql = KEY_SQL.format(placeholders=','.join('?' * len(keys)))
    rows = conn.execute(sql, (*keys, limit)).fetchall()
    return [_row_to_hit(row) for row in rows]


def _fetch_fts(
    conn: sqlite3.Connection,
    match: str,
    limit: int,
) -> list[dict]:
    if not match:
        return []
    try:
        rows = conn.execute(FTS_SQL, (match, limit)).fetchall()
    except sqlite3.OperationalError as exc:
        print(f'FTS query failed: {exc}', file=sys.stderr, flush=True)
        if 'syntax' in str(exc).lower():
            return []
        raise
    return [_row_to_hit(row) for row in rows]


def search(
    conn: sqlite3.Connection,
    query: str,
    limit: int = 10,
) -> tuple[list[dict], str]:
    keys = keys_from_query(query)
    if keys:
        hits = fetch_hits_by_keys(conn, keys, limit)
        if hits:
            return [annotate_hit(hit, 'keys') for hit in hits], 'keys'
    phrase = fts_phrase(query)
    if phrase and is_specific_query(query):
        hits = _fetch_fts(conn, phrase, limit)
        if hits:
            return (
                [annotate_hit(hit, 'title-phrase', query) for hit in hits],
                'title-phrase',
            )
    words = significant_words(query)
    and_q = ' AND '.join(words)
    if len(words) >= TITLE_AND_MIN_WORDS and and_q and and_q != phrase.strip('"'):
        raw = _fetch_fts(conn, and_q, max(limit * 3, 16))
        kept = []
        for hit in raw:
            annotated = annotate_hit(hit, 'title-words', query)
            if annotated.get('title_coverage', 0) < TITLE_COVERAGE_MIN:
                continue
            span = title_span(query, annotated.get('text') or '')
            if span is None or span > TITLE_SPAN_MAX:
                continue
            kept.append(annotated)
            if len(kept) >= limit:
                break
        if kept:
            return kept, 'title-words'
    return [], 'none'


def _hit_tier(hit: dict) -> int:
    digest = bool(hit.get('is_digest'))
    mode = hit.get('match_mode') or ''
    if mode == 'keys' and not digest:
        return 0
    if mode == 'title-phrase' and not digest:
        return 1
    if mode == 'title-words' and not digest:
        return 2
    if mode == 'keys':
        return 3
    return 4


def _hit_rank(hit: dict) -> tuple:
    key_count = hit.get('key_count') or 0
    date = hit.get('date') or ''
    return (
        _hit_tier(hit),
        1 if hit.get('is_forward') else 0,
        99 if key_count == 0 else key_count,
        -(hit.get('views') or 0),
        tuple(-ord(char) for char in date),
    )


def block_mode(hits: list[dict]) -> str:
    if not hits:
        return 'none'
    has_key = any(hit.get('match_mode') == 'keys' for hit in hits)
    has_key_ded = any(
        hit.get('match_mode') == 'keys' and not hit.get('is_digest')
        for hit in hits
    )
    if has_key_ded:
        return 'keys'
    if has_key:
        return 'keys-digest'
    if any(hit.get('match_mode') == 'title-phrase' for hit in hits):
        return 'title-phrase'
    if any(hit.get('match_mode') == 'title-words' for hit in hits):
        return 'title-words'
    return 'none'


def search_many(
    conn: sqlite3.Connection,
    queries: list[str],
    limit: int = 10,
) -> tuple[list[dict], str]:
    by_id: dict[tuple[int, int], dict] = {}
    for query in queries:
        query = (query or '').strip()
        if not query:
            continue
        hits, _mode = search(conn, query, limit=limit)
        for hit in hits:
            key = (hit['channel_id'], hit['id'])
            prev = by_id.get(key)
            if prev is None or _hit_rank(hit) < _hit_rank(prev):
                by_id[key] = hit
    merged = sorted(by_id.values(), key=_hit_rank)
    has_key_ded = any(
        hit.get('match_mode') == 'keys' and not hit.get('is_digest')
        for hit in merged
    )
    if has_key_ded:
        merged = [
            hit for hit in merged if hit.get('match_mode') == 'keys'
        ]
    else:
        dedicated = [hit for hit in merged if not hit.get('is_digest')]
        if dedicated:
            merged = [
                hit for hit in merged
                if not hit.get('is_digest')
                or hit.get('match_mode') == 'keys'
            ]
    merged = merged[:limit]
    return merged, block_mode(merged)


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
        mark = None
        if hit['public']:
            mark = badge_for(hit['username'], hit['id'])
        if (
            not mark
            and hit.get('original_public')
            and hit.get('fwd_username')
            and hit.get('fwd_post_id')
        ):
            mark = badge_for(hit['fwd_username'], int(hit['fwd_post_id']))
        if mark:
            parts.append(f'  {mark}')
    return '\n'.join(parts)


def _hit_for_url(hits: list[dict], url: str) -> dict | None:
    for hit in hits:
        if hit.get('original_url') == url or hit.get('url') == url:
            return hit
    return None


def _md_context(hit: dict, url: str) -> str:
    if hit.get('original_url') == url:
        channel = (
            hit.get('fwd_username')
            or hit.get('fwd_name')
            or hit.get('title')
            or ''
        )
    else:
        channel = hit.get('title') or hit.get('username') or ''
    date = hit.get('date') or ''
    snippet = _snippet(hit.get('text') or '', width=80)
    bits = [part for part in (date, channel) if part]
    if snippet:
        bits.append(f'«{snippet}»')
    return ' · '.join(bits)


def _confidence_line(hits: list[dict], mode: str) -> str:
    if not hits:
        return ''
    dedicated = [hit for hit in hits if not hit.get('is_digest')]
    if any(hit.get('match_mode') == 'keys' for hit in dedicated):
        return '_confidence: dedicated key match_'
    if dedicated and (mode or '').startswith('title'):
        kind = 'phrase' if mode == 'title-phrase' else 'words'
        return f'_confidence: title {kind} — verify_'
    if all(hit.get('is_digest') for hit in hits):
        if any(hit.get('match_mode') == 'keys' for hit in hits):
            return '_confidence: key match in digest posts_'
        return '_confidence: title match in digest posts — verify_'
    return ''


def _md_tags(
    hit: dict | None,
    url: str,
    already: dict[str, str] | None,
) -> str:
    tags: list[str] = []
    if hit:
        if hit.get('is_digest'):
            tags.append('[digest]')
        if (hit.get('match_mode') or '').startswith('title'):
            tags.append('[title match]')
    ref = post_ref(url)
    if already and ref and ref.lower() in already:
        other = already[ref.lower()]
        tags.append(f'[already badge for {other}]' if other else '[already badge]')
    return (' ' + ' '.join(tags)) if tags else ''


def format_md(
    title: str,
    hits: list[dict],
    mode: str = '',
    *,
    heading: str = '##',
    already: dict[str, str] | None = None,
) -> str:
    lines = [f'{heading} {title}', '']
    confidence = _confidence_line(hits, mode)
    if confidence:
        lines.append(confidence)
        lines.append('')
    if not hits:
        lines.append('_no public posts found_')
        lines.append('')
        return '\n'.join(lines)
    seen: set[str] = set()
    ordered = []
    for hit in hits:
        if 'is_digest' not in hit:
            hit['is_digest'] = is_digest(hit)
        if hit.get('original_public') and hit.get('original_url'):
            ordered.append(hit['original_url'])
        if hit['public']:
            ordered.append(hit['url'])
    for url in ordered:
        if url in seen:
            continue
        seen.add(url)
        hit = _hit_for_url(hits, url)
        extra = _md_context(hit, url) if hit else ''
        tags = _md_tags(hit, url, already)
        if extra:
            lines.append(f'{url} — {extra}{tags}')
        else:
            lines.append(f'{url}{tags}')
    if not seen:
        lines.append('_no public posts found_')
    lines.append('')
    return '\n'.join(lines)


def main() -> None:
    configure_stdio()
    args = parse_args()
    db_path = args.db or DB
    if not db_path.exists():
        raise SystemExit(
            f'{db_path} is missing. Run: python tg/export.py'
        )
    conn = open_db(db_path)
    any_hits = False
    for query in args.queries:
        hits, mode = search(conn, query, args.limit)
        if args.md:
            print(format_md(query, hits, mode), end='')
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
