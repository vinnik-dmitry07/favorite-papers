'''Shared paths, Telethon client, SQLite index, and message flattening.'''

from __future__ import annotations

import re
import sqlite3
import sys
from datetime import datetime, timezone
from os import environ
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / 'src'
if str(SRC) not in sys.path:
    sys.path.append(str(SRC))

from add_tg_links import (  # noqa: E402
    channel_translate_link,
    is_arxiv_id,
    normalize_keys,
    paper_keys_from_text,
)

CANONICAL_TG = ROOT / 'tg'
LEGACY_TG = ROOT / 'assets' / 'tg'
SCHEMA_VERSION = 2
URL_RE = re.compile(r'https?://[^\s\]\)>\'",]+', re.I)
ARXIV_BARE_RE = re.compile(r'(?<![\d.])(\d{4}\.\d{4,5})(?:v\d+)?(?![\d.])')
DEFAULT_SLUG = '5iWgAjztpOJiYTQy'
DEFAULT_FOLDER = 'ML'
ENV = ROOT / '.env'


def resolve_db_path() -> Path:
    for path in (
        CANONICAL_TG / 'ml_folder.sqlite',
        LEGACY_TG / 'ml_folder.sqlite',
    ):
        if path.exists():
            return path
    return CANONICAL_TG / 'ml_folder.sqlite'


def resolve_session_path() -> Path:
    '''Telethon session stem, independent of where the sqlite file lives.'''
    for stem in (CANONICAL_TG / 'ml_folder', LEGACY_TG / 'ml_folder'):
        if stem.with_suffix('.session').exists():
            return stem
    return CANONICAL_TG / 'ml_folder'


DB = resolve_db_path()
SESSION = resolve_session_path()
TG_DIR = DB.parent

SCHEMA = '''
CREATE TABLE IF NOT EXISTS meta (
    key TEXT PRIMARY KEY,
    value TEXT
);

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
    is_fwd INTEGER DEFAULT 0,
    key_count INTEGER DEFAULT 0,
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
CREATE INDEX IF NOT EXISTS paper_keys_msg ON paper_keys(channel_id, msg_id);

CREATE VIRTUAL TABLE IF NOT EXISTS fts USING fts5(
    text,
    tokenize='unicode61'
);
'''


def configure_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, 'reconfigure', None)
        if reconfigure is None:
            continue
        try:
            reconfigure(encoding='utf-8', errors='replace')
        except Exception:  # noqa: BLE001
            pass


def load_env(path: Path | None = None) -> dict[str, str]:
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
    '''Telethon client. FloodWait is raised so export can log the sleep.'''
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

    SESSION.parent.mkdir(parents=True, exist_ok=True)
    client = TelegramClient(str(SESSION), api_id, api_hash)
    client.flood_sleep_threshold = 0
    return client


def _table_columns(conn: sqlite3.Connection, table: str) -> set[str]:
    return {row[1] for row in conn.execute(f'PRAGMA table_info({table})')}


def _schema_version(conn: sqlite3.Connection) -> int:
    conn.execute(
        'CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT)'
    )
    row = conn.execute(
        "SELECT value FROM meta WHERE key = 'schema'",
    ).fetchone()
    return int(row[0]) if row else 0


def _fts_is_legacy(conn: sqlite3.Connection) -> bool:
    row = conn.execute(
        "SELECT sql FROM sqlite_master WHERE type = 'table' AND name = 'fts'",
    ).fetchone()
    if not row or not row[0]:
        return True
    return 'channel_id' in row[0]


def _ensure_message_columns(conn: sqlite3.Connection) -> None:
    cols = _table_columns(conn, 'messages')
    if 'is_fwd' not in cols:
        conn.execute(
            'ALTER TABLE messages ADD COLUMN is_fwd INTEGER DEFAULT 0',
        )
    if 'key_count' not in cols:
        conn.execute(
            'ALTER TABLE messages ADD COLUMN key_count INTEGER DEFAULT 0',
        )


def migrate_schema(conn: sqlite3.Connection) -> None:
    _ensure_message_columns(conn)
    conn.execute(
        'CREATE INDEX IF NOT EXISTS paper_keys_msg '
        'ON paper_keys(channel_id, msg_id)',
    )
    version = _schema_version(conn)
    legacy_fts = _fts_is_legacy(conn)
    if version >= SCHEMA_VERSION and not legacy_fts:
        return
    stored = conn.execute('SELECT COUNT(*) FROM messages').fetchone()[0]
    if legacy_fts:
        print('migrating telegram index (rebuild fts)...', flush=True)
        conn.execute('DROP TABLE IF EXISTS fts')
        conn.execute(
            "CREATE VIRTUAL TABLE fts USING fts5(text, tokenize='unicode61')",
        )
        conn.commit()
    if stored:
        print('migrating telegram index (paper keys + fts)...', flush=True)
        reindex_all(conn)
    conn.execute(
        "INSERT OR REPLACE INTO meta (key, value) VALUES ('schema', ?)",
        (str(SCHEMA_VERSION),),
    )
    conn.commit()


def open_db(path: Path | None = None) -> sqlite3.Connection:
    db_path = path or DB
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute('PRAGMA journal_mode=WAL')
    conn.execute('PRAGMA foreign_keys=ON')
    conn.executescript(SCHEMA)
    migrate_schema(conn)
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
        'is_fwd': 0,
    }
    if fwd is None:
        return info
    info['is_fwd'] = 1
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


def inferred_is_fwd(row: dict[str, Any]) -> int:
    if row.get('is_fwd'):
        return 1
    if row.get('fwd_post_id') or row.get('fwd_channel_id') or row.get('fwd_name'):
        return 1
    return 0


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
        'key_count': 0,
    }
    row.update(_forward_info(msg))
    return row


def keys_from_query(query: str) -> set[str]:
    keys = normalize_keys(paper_keys_from_text(query))
    for match in ARXIV_BARE_RE.finditer(query):
        value = match.group(1)
        if is_arxiv_id(value):
            keys.add(f'arxiv:{value}')
    return normalize_keys(keys)


def keys_from_row(row: dict[str, Any]) -> set[str]:
    blob = f'{row.get("text") or ""}\n{row.get("urls") or ""}'
    return normalize_keys(paper_keys_from_text(blob))


def _message_rowid(
    conn: sqlite3.Connection,
    channel_id: int,
    msg_id: int,
) -> int | None:
    row = conn.execute(
        'SELECT rowid FROM messages WHERE channel_id = ? AND id = ?',
        (channel_id, msg_id),
    ).fetchone()
    return int(row[0]) if row else None


def refresh_index(
    conn: sqlite3.Connection,
    row: dict[str, Any],
    *,
    replace: bool = True,
) -> None:
    '''Rebuild paper_keys + FTS for one already-stored message.'''
    channel_id = row['channel_id']
    msg_id = row['id']
    rowid = _message_rowid(conn, channel_id, msg_id)
    if rowid is None:
        return
    keys = keys_from_row(row)
    is_fwd = inferred_is_fwd(row)
    if replace:
        conn.execute(
            'DELETE FROM paper_keys WHERE channel_id = ? AND msg_id = ?',
            (channel_id, msg_id),
        )
        conn.execute('DELETE FROM fts WHERE rowid = ?', (rowid,))
    for key in keys:
        conn.execute(
            'INSERT OR IGNORE INTO paper_keys (key, channel_id, msg_id) '
            'VALUES (?, ?, ?)',
            (key, channel_id, msg_id),
        )
    conn.execute(
        'UPDATE messages SET is_fwd = ?, key_count = ? WHERE rowid = ?',
        (is_fwd, len(keys), rowid),
    )
    if row.get('text'):
        conn.execute(
            'INSERT INTO fts (rowid, text) VALUES (?, ?)',
            (rowid, row['text']),
        )


def index_message(conn: sqlite3.Connection, row: dict[str, Any]) -> int:
    '''Insert or replace one message and refresh paper_keys + FTS. Returns 1.'''
    row = dict(row)
    row['is_fwd'] = inferred_is_fwd(row)
    row.setdefault('key_count', 0)
    conn.execute(
        '''
        INSERT INTO messages (
            channel_id, id, date, text, urls,
            fwd_channel_id, fwd_username, fwd_post_id, fwd_name,
            is_fwd, key_count, grouped_id, views
        ) VALUES (
            :channel_id, :id, :date, :text, :urls,
            :fwd_channel_id, :fwd_username, :fwd_post_id, :fwd_name,
            :is_fwd, :key_count, :grouped_id, :views
        )
        ON CONFLICT(channel_id, id) DO UPDATE SET
            date = excluded.date,
            text = excluded.text,
            urls = excluded.urls,
            fwd_channel_id = excluded.fwd_channel_id,
            fwd_username = COALESCE(
                excluded.fwd_username, messages.fwd_username
            ),
            fwd_post_id = excluded.fwd_post_id,
            fwd_name = COALESCE(excluded.fwd_name, messages.fwd_name),
            is_fwd = excluded.is_fwd,
            grouped_id = excluded.grouped_id,
            views = excluded.views
        ''',
        row,
    )
    refresh_index(conn, row, replace=True)
    return 1


def reindex_all(conn: sqlite3.Connection) -> tuple[int, int]:
    '''Rebuild paper_keys and FTS from stored messages. Returns (msgs, keys).'''
    total = conn.execute('SELECT COUNT(*) FROM messages').fetchone()[0]
    conn.execute('DELETE FROM paper_keys')
    conn.execute('DELETE FROM fts')
    conn.commit()
    cursor = conn.execute(
        'SELECT channel_id, id, date, text, urls, '
        'fwd_channel_id, fwd_username, fwd_post_id, fwd_name, '
        'is_fwd, key_count, grouped_id, views FROM messages',
    )
    done = 0
    while True:
        batch = cursor.fetchmany(500)
        if not batch:
            break
        for raw in batch:
            refresh_index(conn, dict(raw), replace=False)
            done += 1
        conn.commit()
        if total:
            pct = 100 * done / total
            print(f'\rreindex {done}/{total} ({pct:.0f}%)', end='', flush=True)
    keys = conn.execute('SELECT COUNT(*) FROM paper_keys').fetchone()[0]
    if total:
        print(flush=True)
    return done, keys


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
        INSERT INTO channels (
            id, username, title, kind, last_id, total, synced_at
        )
        VALUES (?, ?, ?, ?, COALESCE(?, 0), ?, ?)
        ON CONFLICT(id) DO UPDATE SET
            username = COALESCE(excluded.username, channels.username),
            title = COALESCE(excluded.title, channels.title),
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
    if username:
        return f'https://t.me/{username}/{msg_id}', True
    return f'https://t.me/c/{channel_id}/{msg_id}', False


def badge_for(username: str | None, msg_id: int) -> str | None:
    if not username:
        return None
    return f'[⌲ tg]({channel_translate_link(username, str(msg_id))})'


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


def channel_label(
    username: str | None,
    title: str | None,
    channel_id: int,
) -> str:
    return username or title or str(channel_id)
