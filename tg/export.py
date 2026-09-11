'''Sync the Telegram ML folder into tg/ml_folder.sqlite.

    python tg/export.py
    python tg/export.py --only gonzo_ML
    python tg/export.py --folder ML
    python tg/export.py --channels assets/channels.txt
    python tg/export.py --reindex
'''

from __future__ import annotations

import argparse
import asyncio
import signal
import sys
import time
from datetime import datetime, timezone
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
    DEFAULT_FOLDER,
    DEFAULT_SLUG,
    channel_label,
    channel_last_id,
    configure_stdio,
    db_size,
    format_size,
    index_message,
    make_client,
    message_row,
    open_db,
    reindex_all,
    set_channel_progress,
    upsert_channel,
)

BATCH = 200


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Export ML-folder Telegram channels into a local SQLite index',
    )
    parser.add_argument(
        '--slug',
        default=DEFAULT_SLUG,
        help='t.me/addlist/<slug> (default: the ML folder invite)',
    )
    parser.add_argument(
        '--folder',
        metavar='NAME',
        help=f'dialog-filter title fallback (e.g. {DEFAULT_FOLDER})',
    )
    parser.add_argument(
        '--channels',
        type=Path,
        metavar='FILE',
        help='file of t.me URLs or @usernames, one per line',
    )
    parser.add_argument(
        '--include-groups',
        action='store_true',
        help='also sync megagroups / chats, not only broadcast channels',
    )
    parser.add_argument(
        '--since',
        metavar='YYYY-MM-DD',
        help='skip messages older than this date',
    )
    parser.add_argument(
        '--only',
        help='comma-separated usernames to sync (e.g. gonzo_ML,data_secrets)',
    )
    parser.add_argument(
        '--refresh-tail',
        type=int,
        default=0,
        metavar='N',
        help='re-fetch the newest N messages per channel (picks up edits)',
    )
    parser.add_argument(
        '--reindex',
        action='store_true',
        help='rebuild paper_keys + FTS from stored messages (no network)',
    )
    return parser.parse_args()


def parse_since(raw: str | None) -> datetime | None:
    if not raw:
        return None
    return datetime.strptime(raw, '%Y-%m-%d').replace(tzinfo=timezone.utc)


def parse_only(raw: str | None) -> set[str]:
    if not raw:
        return set()
    return {
        part.strip().lstrip('@').lower()
        for part in raw.split(',')
        if part.strip()
    }


def parse_channel_file(path: Path) -> list[str]:
    handles: list[str] = []
    for line in path.read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        line = line.rstrip('/')
        if 't.me/' in line:
            line = line.split('t.me/', 1)[1]
        if line.startswith('s/'):
            line = line[2:]
        line = line.split('/', 1)[0].lstrip('@')
        if line:
            handles.append(line)
    return handles


def _is_broadcast(ent) -> bool:
    return bool(getattr(ent, 'broadcast', False))


def _is_group(ent) -> bool:
    return bool(
        getattr(ent, 'megagroup', False)
        or getattr(ent, 'gigagroup', False)
        or type(ent).__name__ == 'Chat'
    )


def _entity_key(ent) -> tuple[str, int]:
    return (type(ent).__name__, int(ent.id))


def _peer_key(peer) -> tuple[str, int] | None:
    if getattr(peer, 'channel_id', None):
        return ('Channel', int(peer.channel_id))
    if getattr(peer, 'chat_id', None):
        return ('Chat', int(peer.chat_id))
    if getattr(peer, 'user_id', None):
        return ('User', int(peer.user_id))
    return None


def _filter_title(filt) -> str:
    title = getattr(filt, 'title', None)
    if title is None:
        return ''
    if isinstance(title, str):
        return title
    return getattr(title, 'text', '') or ''


async def await_flood(coro_factory):
    '''Retry a Telethon call after FloodWait, logging the sleep.'''
    from telethon.errors import FloodWaitError

    while True:
        try:
            return await coro_factory()
        except FloodWaitError as exc:
            print(
                f'\nflood wait {exc.seconds}s, sleeping...',
                flush=True,
            )
            await asyncio.sleep(exc.seconds + 1)


async def _entity_from_peer(client, peer):
    try:
        return await await_flood(lambda: client.get_entity(peer))
    except Exception as exc:  # noqa: BLE001
        print(f'  skip peer {peer}: {exc}', flush=True)
        return None


async def chats_from_invite(client, result) -> list:
    by_key = {_entity_key(c): c for c in (getattr(result, 'chats', None) or [])}
    peers = []
    for attr in ('peers', 'already_peers', 'missing_peers'):
        peers.extend(getattr(result, attr, None) or [])
    out = []
    seen: set[tuple[str, int]] = set()
    for peer in peers:
        key = _peer_key(peer)
        ent = by_key.get(key) if key is not None else None
        if ent is None:
            ent = await _entity_from_peer(client, peer)
        if ent is None:
            continue
        ekey = _entity_key(ent)
        if ekey in seen:
            continue
        seen.add(ekey)
        out.append(ent)
    if out:
        return out
    return [c for c in by_key.values() if _is_broadcast(c) or _is_group(c)]


async def resolve_from_slug(client, slug: str) -> list:
    from telethon.tl.functions.chatlists import CheckChatlistInviteRequest

    result = await await_flood(
        lambda: client(CheckChatlistInviteRequest(slug=slug)),
    )
    return await chats_from_invite(client, result)


async def resolve_from_folder(client, name: str) -> list:
    from telethon.tl.functions.messages import GetDialogFiltersRequest

    filters = await client(GetDialogFiltersRequest())
    if hasattr(filters, 'filters'):
        filters = filters.filters
    wanted = name.casefold()
    match = None
    for filt in filters:
        if _filter_title(filt).casefold() == wanted:
            match = filt
            break
    if match is None:
        titles = [
            _filter_title(filt) or type(filt).__name__
            for filt in filters
        ]
        raise SystemExit(
            f'no dialog filter named {name!r}; '
            f'available: {", ".join(titles) or "(none)"}'
        )
    peers = []
    for attr in ('include_peers', 'peers', 'pinned_peers'):
        peers.extend(getattr(match, attr, None) or [])
    out = []
    seen: set[tuple[str, int]] = set()
    for peer in peers:
        ent = await _entity_from_peer(client, peer)
        if ent is None:
            continue
        ekey = _entity_key(ent)
        if ekey in seen:
            continue
        seen.add(ekey)
        out.append(ent)
    return out


async def resolve_from_file(client, path: Path) -> list:
    out = []
    for handle in parse_channel_file(path):
        try:
            ent = await client.get_entity(handle)
        except Exception as exc:  # noqa: BLE001
            print(f'  skip {handle}: {exc}', flush=True)
            continue
        out.append(ent)
    return out


def keep_chat(ent, include_groups: bool) -> bool:
    if _is_broadcast(ent):
        return True
    if include_groups and _is_group(ent):
        return True
    return False


def matches_only(ent, wanted: set[str]) -> bool:
    if not wanted:
        return True
    username = (getattr(ent, 'username', None) or '').lower()
    title = (getattr(ent, 'title', None) or '').lower()
    return username in wanted or title in wanted


async def resolve_chats(client, args: argparse.Namespace) -> list:
    if args.channels:
        chats = await resolve_from_file(client, args.channels)
        source = f'file {args.channels}'
    else:
        chats = []
        source = f'slug {args.slug}'
        try:
            chats = await resolve_from_slug(client, args.slug)
        except Exception as exc:  # noqa: BLE001
            print(f'slug {args.slug} failed: {exc}', flush=True)
            if not args.folder:
                raise SystemExit(
                    'could not resolve the addlist slug; '
                    f'pass --folder {DEFAULT_FOLDER} or --channels FILE'
                ) from exc
        if args.folder:
            extra = await resolve_from_folder(client, args.folder)
            seen = {_entity_key(c) for c in chats}
            for ent in extra:
                key = _entity_key(ent)
                if key not in seen:
                    chats.append(ent)
                    seen.add(key)
            source = f'{source} + folder {args.folder}'
    wanted = parse_only(args.only)
    picked = [
        c for c in chats
        if keep_chat(c, args.include_groups) and matches_only(c, wanted)
    ]
    print(
        f'resolved {len(picked)} chats from {source} '
        f'(of {len(chats)} peers, groups='
        f'{"on" if args.include_groups else "off"})',
        flush=True,
    )
    return picked


async def channel_total(client, ent) -> int:
    try:
        result = await await_flood(lambda: client.get_messages(ent, limit=0))
        return int(result.total or 0)
    except Exception:  # noqa: BLE001
        return 0


def _progress_line(
    index: int,
    n: int,
    label: str,
    have: int,
    total: int,
    new_count: int,
) -> str:
    pct = 100 * have / total if total else 100
    return (
        f'[{index:02d}/{n:02d}] {label}  {have}/{total} '
        f'({pct:.0f}%)  new={new_count}'
    )


def _print_progress(line: str) -> None:
    print('\r' + line.ljust(88), end='', flush=True)


async def enrich_forward(client, row: dict, cache: dict) -> None:
    cid = row.get('fwd_channel_id')
    if not cid or row.get('fwd_username'):
        return
    if cid not in cache:
        try:
            ent = await await_flood(lambda: client.get_entity(cid))
            cache[cid] = getattr(ent, 'username', None)
        except Exception:  # noqa: BLE001
            cache[cid] = None
    row['fwd_username'] = cache[cid]


async def iter_messages_resumable(client, ent, min_id: int, offset_date=None):
    from telethon.errors import FloodWaitError

    kwargs: dict = {'min_id': min_id, 'reverse': True}
    if offset_date is not None:
        kwargs['offset_date'] = offset_date
    while True:
        try:
            async for msg in client.iter_messages(ent, **kwargs):
                yield msg
                kwargs['min_id'] = max(int(kwargs['min_id']), int(msg.id))
            return
        except FloodWaitError as exc:
            print(
                f'\nflood wait {exc.seconds}s, sleeping...',
                flush=True,
            )
            await asyncio.sleep(exc.seconds + 1)


def install_stop_flag() -> dict:
    stop = {'flag': False}

    def handler(_signum, _frame) -> None:
        if stop['flag']:
            signal.signal(signal.SIGINT, signal.default_int_handler)
            raise KeyboardInterrupt
        stop['flag'] = True
        print('\ninterrupt requested, saving...', flush=True)

    try:
        signal.signal(signal.SIGINT, handler)
    except Exception:  # noqa: BLE001
        pass
    return stop


async def refresh_recent(
    client,
    conn,
    ent,
    channel_id: int,
    limit: int,
    cache: dict,
) -> int:
    from telethon.errors import FloodWaitError

    if limit <= 0:
        return 0
    count = 0
    while True:
        try:
            async for msg in client.iter_messages(ent, limit=limit):
                row = message_row(msg, channel_id)
                if row is None:
                    continue
                await enrich_forward(client, row, cache)
                index_message(conn, row)
                count += 1
            return count
        except FloodWaitError as exc:
            print(
                f'\nflood wait {exc.seconds}s, sleeping...',
                flush=True,
            )
            await asyncio.sleep(exc.seconds + 1)


async def sync_channel(
    client,
    conn,
    ent,
    index: int,
    n: int,
    since: datetime | None,
    refresh_tail: int,
    stop: dict,
    cache: dict,
) -> int:
    channel_id = int(ent.id)
    username = getattr(ent, 'username', None)
    title = getattr(ent, 'title', None)
    kind = 'channel' if _is_broadcast(ent) else 'group'
    label = channel_label(username, title, channel_id)
    last_id = channel_last_id(conn, channel_id)
    total = await channel_total(client, ent)
    upsert_channel(
        conn, channel_id, username, title, kind,
        last_id=last_id, total=total,
    )
    conn.commit()

    already = conn.execute(
        'SELECT COUNT(*) AS n FROM messages WHERE channel_id = ?',
        (channel_id,),
    ).fetchone()['n']

    new_count = 0
    if refresh_tail:
        new_count += await refresh_recent(
            client, conn, ent, channel_id, refresh_tail, cache,
        )
        conn.commit()

    kwargs_date = since if since is not None and last_id == 0 else None
    batch = 0
    max_id = last_id
    t0 = time.monotonic()
    async for msg in iter_messages_resumable(
        client, ent, last_id, kwargs_date,
    ):
        if stop['flag']:
            break
        if msg.id > max_id:
            max_id = msg.id
        msg_date = getattr(msg, 'date', None)
        if since is not None and msg_date is not None:
            aware = msg_date
            if aware.tzinfo is None:
                aware = aware.replace(tzinfo=timezone.utc)
            if aware < since:
                continue
        row = message_row(msg, channel_id)
        if row is None:
            continue
        await enrich_forward(client, row, cache)
        index_message(conn, row)
        new_count += 1
        batch += 1
        if batch >= BATCH:
            set_channel_progress(conn, channel_id, max_id, total)
            conn.commit()
            batch = 0
            have = already + new_count
            _print_progress(
                _progress_line(
                    index, n, label, have, total or have, new_count,
                ),
            )

    if max_id > last_id or new_count:
        set_channel_progress(conn, channel_id, max_id, total)
        conn.commit()

    elapsed = time.monotonic() - t0
    have = already + new_count
    if new_count == 0:
        print(
            f'[{index:02d}/{n:02d}] {label}  no new posts '
            f'({total or have})',
            flush=True,
        )
    else:
        print(
            '\r'
            + _progress_line(
                index, n, label, have, total or have, new_count,
            )
            + f'  {elapsed:.1f}s',
            flush=True,
        )
    return new_count


async def run_export(args: argparse.Namespace) -> None:
    since = parse_since(args.since)
    client = make_client()
    conn = open_db()
    stop = install_stop_flag()
    cache: dict = {}
    new_total = 0
    n_chats = 0
    async with client:
        chats = await resolve_chats(client, args)
        n_chats = len(chats)
        if not chats:
            raise SystemExit('no channels to sync')
        for i, ent in enumerate(chats, start=1):
            if stop['flag']:
                print('stopped before remaining channels', flush=True)
                break
            try:
                new_total += await sync_channel(
                    client, conn, ent, i, n_chats, since,
                    args.refresh_tail, stop, cache,
                )
            except Exception as exc:  # noqa: BLE001
                label = channel_label(
                    getattr(ent, 'username', None),
                    getattr(ent, 'title', None),
                    int(ent.id),
                )
                print(
                    f'[{i:02d}/{n_chats:02d}] {label}  ERROR: {exc}',
                    flush=True,
                )
    keys = conn.execute('SELECT COUNT(*) FROM paper_keys').fetchone()[0]
    msgs = conn.execute('SELECT COUNT(*) FROM messages').fetchone()[0]
    print(
        f'synced {n_chats} channels, +{new_total} messages, '
        f'{msgs} stored, {keys} paper keys, db={format_size(db_size())}',
        flush=True,
    )
    conn.close()


def main() -> None:
    configure_stdio()
    args = parse_args()
    if args.reindex:
        conn = open_db()
        done, keys = reindex_all(conn)
        print(
            f'reindexed {done} messages, {keys} paper keys, '
            f'db={format_size(db_size())}',
            flush=True,
        )
        conn.close()
        return
    asyncio.run(run_export(args))


if __name__ == '__main__':
    main()
