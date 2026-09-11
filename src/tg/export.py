'''Sync the Telegram ML folder into assets/tg/ml_folder.sqlite.

    python src/tg/export.py
    python src/tg/export.py --only gonzo_ML
    python src/tg/export.py --folder ML
    python src/tg/export.py --channels assets/channels.txt
    python src/tg/export.py --reindex
'''

from __future__ import annotations

import argparse
import asyncio
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from common import (
    DEFAULT_FOLDER,
    DEFAULT_SLUG,
    channel_label,
    channel_last_id,
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


def configure_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, 'reconfigure', None)
        if reconfigure is None:
            continue
        try:
            reconfigure(encoding='utf-8', errors='replace')
        except Exception:  # noqa: BLE001
            pass


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
    return {part.strip().lstrip('@').lower() for part in raw.split(',') if part.strip()}


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


def _filter_title(filt) -> str:
    title = getattr(filt, 'title', None)
    if title is None:
        return ''
    if isinstance(title, str):
        return title
    return getattr(title, 'text', '') or ''


def _peer_id(peer) -> int | None:
    for attr in ('channel_id', 'chat_id', 'user_id'):
        value = getattr(peer, attr, None)
        if value is not None:
            return int(value)
    return None


async def _entity_from_peer(client, peer):
    try:
        return await client.get_entity(peer)
    except Exception as exc:  # noqa: BLE001
        print(f'  skip peer {peer}: {exc}', flush=True)
        return None


async def chats_from_invite(client, result) -> list:
    by_id = {int(c.id): c for c in (getattr(result, 'chats', None) or [])}
    peers = []
    for attr in ('peers', 'already_peers', 'missing_peers'):
        peers.extend(getattr(result, attr, None) or [])
    out = []
    seen: set[int] = set()
    for peer in peers:
        cid = _peer_id(peer)
        ent = by_id.get(cid) if cid is not None else None
        if ent is None:
            ent = await _entity_from_peer(client, peer)
        if ent is None:
            continue
        eid = int(ent.id)
        if eid in seen:
            continue
        seen.add(eid)
        out.append(ent)
    if out:
        return out
    return [c for c in by_id.values() if _is_broadcast(c) or _is_group(c)]


async def resolve_from_slug(client, slug: str) -> list:
    from telethon.tl.functions.chatlists import CheckChatlistInviteRequest

    result = await client(CheckChatlistInviteRequest(slug=slug))
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
    seen: set[int] = set()
    for peer in peers:
        ent = await _entity_from_peer(client, peer)
        if ent is None:
            continue
        eid = int(ent.id)
        if eid in seen:
            continue
        seen.add(eid)
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
            seen = {int(c.id) for c in chats}
            for ent in extra:
                if int(ent.id) not in seen:
                    chats.append(ent)
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
        return int((await client.get_messages(ent, limit=0)).total or 0)
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


async def sync_channel(
    client,
    conn,
    ent,
    index: int,
    n: int,
    since: datetime | None,
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
    if total and last_id and already >= total:
        print(
            f'[{index:02d}/{n:02d}] {label}  no new posts ({total})',
            flush=True,
        )
        return 0

    kwargs: dict = {'min_id': last_id, 'reverse': True}
    if since is not None and last_id == 0:
        kwargs['offset_date'] = since

    new_count = 0
    batch = 0
    max_id = last_id
    t0 = time.monotonic()
    try:
        async for msg in client.iter_messages(ent, **kwargs):
            msg_date = getattr(msg, 'date', None)
            if since is not None and msg_date is not None:
                aware = msg_date
                if aware.tzinfo is None:
                    aware = aware.replace(tzinfo=timezone.utc)
                if aware < since:
                    continue
            row = message_row(msg, channel_id)
            if row is None:
                if msg.id > max_id:
                    max_id = msg.id
                continue
            index_message(conn, row)
            new_count += 1
            batch += 1
            if msg.id > max_id:
                max_id = msg.id
            if batch >= BATCH:
                set_channel_progress(conn, channel_id, max_id, total)
                conn.commit()
                batch = 0
                have = already + new_count
                print(
                    '\r' + _progress_line(
                        index, n, label, have, total or have, new_count,
                    ),
                    end='',
                    flush=True,
                )
    except KeyboardInterrupt:
        set_channel_progress(conn, channel_id, max_id, total)
        conn.commit()
        print('\ninterrupted, progress saved', flush=True)
        raise

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
            '\r' + _progress_line(
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
    new_total = 0
    n_chats = 0
    async with client:
        chats = await resolve_chats(client, args)
        n_chats = len(chats)
        if not chats:
            raise SystemExit('no channels to sync')
        for i, ent in enumerate(chats, start=1):
            try:
                new_total += await sync_channel(
                    client, conn, ent, i, n_chats, since,
                )
            except KeyboardInterrupt:
                break
            except Exception as exc:  # noqa: BLE001
                label = channel_label(
                    getattr(ent, 'username', None),
                    getattr(ent, 'title', None),
                    int(ent.id),
                )
                print(f'[{i:02d}/{n_chats:02d}] {label}  ERROR: {exc}', flush=True)
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
