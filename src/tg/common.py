'''Shared paths, Telethon client, SQLite index, and message flattening.'''

from __future__ import annotations

import re
import sqlite3
import sys
from datetime import datetime, timezone
from os import environ
from pathlib import Path
from typing import Any

SRC = Path(__file__).resolve().parent.parent
ROOT = SRC.parent
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from add_tg_links import (  # noqa: E402
    TME_POST,
    channel_translate_link,
    normalize_keys,
    paper_keys_from_text,
)


def _tg_dir() -> Path:
    assets_tg = ROOT / 'assets' / 'tg'
    legacy = ROOT / 'tg'
    if (assets_tg / 'ml_folder.sqlite').exists():
        return assets_tg
    if (legacy / 'ml_folder.sqlite').exists():
        return legacy
    return assets_tg


TG_DIR = _tg_dir()
DB = TG_DIR / 'ml_folder.sqlite'
SESSION = TG_DIR / 'ml_folder'
ENV = ROOT / '.env'
DEFAULT_SLUG = '5iWgAjztpOJiYTQy'
DEFAULT_FOLDER = 'ML'

URL_RE = re.compile(r'https?://[^\s\]\)>\'",]+', re.I)
ARXIV_BARE_RE = re.compile(
    r'(?<![\d.])(\d{4}\.\d{4,5})(?:v\d+)?(?![\d.])',
)
SCHEMA = '''
CREATE TABLE IF NOT EXISTS channels (
    id INTEGER PRIMARY KEY,
    username TEXT,
    title TEXT,
    kind TEXT,
    last_id INTEGER DEFAULT 0,
    total INTEGER,
    synced_at TEXT
);

CREATE TABLE IF NOT EXISTS messages (
    channel_id INTEGER NOT NULL,
    id INTEGER NOT NULL,
    date TEXT,
    text TEXT,
    urls TEXT,
    fwd_channel_id INTEGER,
    fwd_username TEXT,
    fwd_post_id INTEGER,
    fwd_name TEXT,
    grouped_id INTEGER,
    views INTEGER,
    PRIMARY KEY (channel_id, id)
);

CREATE TABLE IF NOT EXISTS paper_keys (
    key TEXT NOT NULL,
    channel_id INTEGER NOT NULL,
    msg_id INTEGER NOT NULL,
    PRIMARY KEY (key, channel_id, msg_id)
);
CREATE INDEX IF NOT EXISTS paper_keys_key ON paper_keys(key);

CREATE VIRTUAL TABLE IF NOT EXISTS fts USING fts5(
    channel_id UNINDEXED,
    msg_id UNINDEXED,
    text
);
'''


def load_env(path: Path | None = None) -> dict[str, str]:
    '''Parse a tiny KEY=value .env file. Existing process env wins.'''
    env_path = path or ENV
    out: dict[str, str] = {}
    if env_path.exists():
        for raw in env_path.read_text(encoding='utf-8').splitlines():
            line = raw.strip()
            if not line or line.startswith('#') or '=' not in line:
                continue
            key, _, value = line.partition('=')
            out[key.strip()] = value.strip().strip('\'').strip('"')
    return out


def env_get(name: str, default: str = '') -> str:
    return environ.get(name) or load_env().get(name) or default


def make_client():
    '''Telethon client; session lives next to the SQLite index.'''
    try:
        from telethon import TelegramClient
    except ImportError as exc:
        raise SystemExit('Install telethon: pip install telethon') from exc

    api_id_raw = env_get('TG_API_ID')
    api_hash = env_get('TG_API_HASH')
    if not api_id_raw or not api_hash:
        raise SystemExit(
            'Set TG_API_ID and TG_API_HASH in .env '
            '(create an app at https://my.telegram.org).'
        )
    try:
        api_id = int(api_id_raw)
    except ValueError as exc:
        raise SystemExit('TG_API_ID must be an integer') from exc

    TG_DIR.mkdir(parents=True, exist_ok=True)
    client = TelegramClient(str(SESSION), api_id, api_hash)
    # Sleep through FloodWait instead of raising.
    client.flood_sleep_threshold = 24 * 60 * 60
    return client


def open_db(path: Path | None = None) -> sqlite3.Connection:
    db_path = path or DB
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute('PRAGMA journal_mode=WAL')
    conn.execute('PRAGMA foreign_keys=ON')
    conn.executescript(SCHEMA)
    return conn


def _dedupe(items: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for item in items:
        item = item.rstrip(').,;\'"')
        if not item or item in seen:
            continue
        seen.add(item)
        out.append(item)
    return out


def _entity_urls(msg: Any) -> list[str]:
    urls: list[str] = []
    for ent in getattr(msg, 'entities', None) or []:
        url = getattr(ent, 'url', None)
        if url:
            urls.append(url)
    return urls


def _webpage_bits(msg: Any) -> tuple[list[str], list[str]]:
    '''Return (urls, extra text) from a link preview, if any.'''
    media = getattr(msg, 'media', None)
    webpage = getattr(media, 'webpage', None)
    if webpage is None:
        return [], []
    urls: list[str] = []
    extra: list[str] = []
    url = getattr(webpage, 'url', None)
    if url:
        urls.append(url)
    for attr in ('title', 'description', 'display_url'):
        value = getattr(webpage, attr, None)
        if value:
            extra.append(str(value))
    return urls, extra


def _forward_info(msg: Any) -> dict[str, Any]:
    fwd = getattr(msg, 'fwd_from', None)
    info = {
        'fwd_channel_id': None,
        'fwd_username': None,
        'fwd_post_id': None,
        'fwd_name': None,
    }
    if fwd is None:
        return info
    from_id = getattr(fwd, 'from_id', None)
    if from_id is not None:
        info['fwd_channel_id'] = getattr(from_id, 'channel_id', None)
    info['fwd_post_id'] = getattr(fwd, 'channel_post', None)
    info['fwd_name'] = getattr(fwd, 'from_name', None)
    try:
        helper = getattr(msg, 'forward', None)
        chat = getattr(helper, 'chat', None) if helper is not None else None
    except Exception:  # noqa: BLE001
        chat = None
    if chat is not None:
        info['fwd_username'] = getattr(chat, 'username', None)
        if not info['fwd_name']:
            info['fwd_name'] = getattr(chat, 'title', None)
    return info


def message_row(msg: Any, channel_id: int) -> dict[str, Any] | None:
    '''Flatten a Telethon message into a DB row dict, or None if empty.'''
    if getattr(msg, 'action', None) is not None:
        return None
    body = getattr(msg, 'message', None) or ''
    hidden = _entity_urls(msg)
    preview_urls, preview_text = _webpage_bits(msg)
    body_urls = URL_RE.findall(body)
    urls = _dedupe([*hidden, *preview_urls, *body_urls])
    parts = [body, *hidden, *preview_urls, *preview_text]
    text = '\n'.join(part for part in parts if part).strip()
    if not text and not urls:
        return None
    date = getattr(msg, 'date', None)
    if isinstance(date, datetime):
        date_s = date.isoformat()
    else:
        date_s = str(date) if date else None
    row = {
        'channel_id': channel_id,
        'id': int(msg.id),
        'date': date_s,
        'text': text,
        'urls': '\n'.join(urls),
        'grouped_id': getattr(msg, 'grouped_id', None),
        'views': getattr(msg, 'views', None),
    }
    row.update(_forward_info(msg))
    return row


def keys_from_query(query: str) -> set[str]:
    '''Paper keys from a URL, bare arXiv id, DOI, or free text.'''
    keys = normalize_keys(paper_keys_from_text(query))
    for match in ARXIV_BARE_RE.finditer(query):
        value = match.group(1)
        yy = int(value[:2])
        mm = int(value[2:4])
        if 1 <= mm <= 12 and 7 <= yy <= 30:
            keys.add(f'arxiv:{value}')
    return normalize_keys(keys)


def keys_from_row(row: dict[str, Any]) -> set[str]:
    blob = f'{row.get("text") or ""}\n{row.get("urls") or ""}'
    return normalize_keys(paper_keys_from_text(blob))


def refresh_index(conn: sqlite3.Connection, row: dict[str, Any]) -> None:
    '''Rebuild paper_keys + FTS for one already-stored message.'''
    conn.execute(
        'DELETE FROM paper_keys WHERE channel_id = ? AND msg_id = ?',
        (row['channel_id'], row['id']),
    )
    for key in keys_from_row(row):
        conn.execute(
            'INSERT OR IGNORE INTO paper_keys (key, channel_id, msg_id) '
            'VALUES (?, ?, ?)',
            (key, row['channel_id'], row['id']),
        )
    conn.execute(
        'DELETE FROM fts WHERE channel_id = ? AND msg_id = ?',
        (row['channel_id'], row['id']),
    )
    if row.get('text'):
        conn.execute(
            'INSERT INTO fts (channel_id, msg_id, text) VALUES (?, ?, ?)',
            (row['channel_id'], row['id'], row['text']),
        )


def index_message(conn: sqlite3.Connection, row: dict[str, Any]) -> int:
    '''Insert or replace one message and refresh paper_keys + FTS. Returns 1.'''
    conn.execute(
        '''
        INSERT OR REPLACE INTO messages (
            channel_id, id, date, text, urls,
            fwd_channel_id, fwd_username, fwd_post_id, fwd_name,
            grouped_id, views
        ) VALUES (
            :channel_id, :id, :date, :text, :urls,
            :fwd_channel_id, :fwd_username, :fwd_post_id, :fwd_name,
            :grouped_id, :views
        )
        ''',
        row,
    )
    refresh_index(conn, row)
    return 1


def reindex_all(conn: sqlite3.Connection) -> tuple[int, int]:
    '''Rebuild paper_keys and FTS from stored messages. Returns (msgs, keys).'''
    rows = conn.execute(
        'SELECT channel_id, id, date, text, urls, '
        'fwd_channel_id, fwd_username, fwd_post_id, fwd_name, '
        'grouped_id, views FROM messages'
    ).fetchall()
    total = len(rows)
    conn.execute('DELETE FROM paper_keys')
    conn.execute('DELETE FROM fts')
    for done, raw in enumerate(rows, start=1):
        refresh_index(conn, dict(raw))
        if done % 500 == 0 or done == total:
            pct = 100 * done / total if total else 100
            print(f'\rreindex {done}/{total} ({pct:.0f}%)', end='', flush=True)
    conn.commit()
    keys = conn.execute('SELECT COUNT(*) FROM paper_keys').fetchone()[0]
    if total:
        print(flush=True)
    return total, keys


def upsert_channel(
    conn: sqlite3.Connection,
    channel_id: int,
    username: str | None,
    title: str | None,
    kind: str,
    last_id: int | None = None,
    total: int | None = None,
    synced: bool = False,
) -> None:
    conn.execute(
        '''
        INSERT INTO channels (id, username, title, kind, last_id, total, synced_at)
        VALUES (?, ?, ?, ?, COALESCE(?, 0), ?, ?)
        ON CONFLICT(id) DO UPDATE SET
            username = excluded.username,
            title = excluded.title,
            kind = excluded.kind,
            last_id = COALESCE(excluded.last_id, channels.last_id),
            total = COALESCE(excluded.total, channels.total),
            synced_at = COALESCE(excluded.synced_at, channels.synced_at)
        ''',
        (
            channel_id,
            username,
            title,
            kind,
            last_id,
            total,
            datetime.now(timezone.utc).isoformat(timespec='seconds')
            if synced else None,
        ),
    )


def channel_last_id(conn: sqlite3.Connection, channel_id: int) -> int:
    row = conn.execute(
        'SELECT last_id FROM channels WHERE id = ?',
        (channel_id,),
    ).fetchone()
    return int(row['last_id'] or 0) if row else 0


def set_channel_progress(
    conn: sqlite3.Connection,
    channel_id: int,
    last_id: int,
    total: int | None = None,
) -> None:
    conn.execute(
        '''
        UPDATE channels
        SET last_id = ?,
            total = COALESCE(?, total),
            synced_at = ?
        WHERE id = ?
        ''',
        (
            last_id,
            total,
            datetime.now(timezone.utc).isoformat(timespec='seconds'),
            channel_id,
        ),
    )


def public_post_url(
    username: str | None,
    channel_id: int,
    msg_id: int,
) -> tuple[str, bool]:
    '''Return (url, is_public).'''
    if username:
        return f'https://t.me/{username}/{msg_id}', True
    return f'https://t.me/c/{channel_id}/{msg_id}', False


def badge_for(username: str | None, msg_id: int) -> str | None:
    if not username:
        return None
    return (
        f'[⌲ tg]({channel_translate_link(username, str(msg_id))})'
    )


def db_size(path: Path | None = None) -> int:
    db_path = path or DB
    if not db_path.exists():
        return 0
    return db_path.stat().st_size


def format_size(n: int) -> str:
    if n < 1024:
        return f'{n} B'
    if n < 1024 ** 2:
        return f'{n / 1024:.1f} KB'
    return f'{n / (1024 ** 2):.1f} MB'


def channel_label(username: str | None, title: str | None, channel_id: int) -> str:
    return username or title or str(channel_id)


# Re-export for callers that only import common.
__all__ = [
    'ARXIV_BARE_RE',
    'DB',
    'DEFAULT_FOLDER',
    'DEFAULT_SLUG',
    'ENV',
    'ROOT',
    'SESSION',
    'TME_POST',
    'TG_DIR',
    'badge_for',
    'channel_label',
    'channel_last_id',
    'channel_translate_link',
    'db_size',
    'env_get',
    'format_size',
    'index_message',
    'refresh_index',
    'keys_from_query',
    'keys_from_row',
    'load_env',
    'make_client',
    'message_row',
    'normalize_keys',
    'open_db',
    'paper_keys_from_text',
    'public_post_url',
    'reindex_all',
    'set_channel_progress',
    'upsert_channel',
]
