'''Compare cached / scored paper text with the latest arXiv or bioRxiv version.

    python filter/check_versions.py --only-keys k1,k2
    python filter/check_versions.py
    python filter/check_versions.py --force
    python filter/check_versions.py --refresh

arXiv latest comes from https://arxiv.org/abs/<id> (never the export API —
100-id batches get 429). bioRxiv latest comes from api.biorxiv.org.
Used version: fulltext_index.version, then cache watermark, then md watermark.
'''

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

FILTER_DIR = Path(__file__).resolve().parent
ROOT = FILTER_DIR.parent
sys.path.insert(0, str(FILTER_DIR))
sys.path.insert(0, str(ROOT / 'src'))

from extract_fulltext import EXTRA_PDF_URLS, detect_arxiv_version  # noqa: E402
from paths import (  # noqa: E402
    FULLTEXT_DIR,
    FULLTEXT_INDEX,
    PAPERS_JSONL,
    VERSIONS_JSONL,
    cache_path,
    read_gz,
    read_jsonl,
    safe_key,
    write_jsonl,
)

HEADERS = {
    'User-Agent': 'key-papers-filter/0.1 (local research scoring)',
    'Accept': 'text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8',
}
ARXIV_DELAY = 1.2
BIORXIV_DELAY = 1.0
ABS_VER_RE = re.compile(
    r'(?:this version,\s*v(\d+)|arXiv:\d{4}\.\d{4,5}v(\d+)|'
    r'/pdf/\d{4}\.\d{4,5}v(\d+))',
    re.I,
)
ABS_REVISED_RE = re.compile(r'last revised ([^(]+)\(this version', re.I)
ABS_SUBMITTED_RE = re.compile(r'\[Submitted on ([^\]]+)\]', re.I)
WATERMARK_RE = re.compile(r'arXiv:(\d{4}\.\d{4,5})v(\d+)')
ARXIV_PDF_RE = re.compile(r'arxiv\.org/pdf/(\d{4}\.\d{4,5})', re.I)
POSTED_RE = re.compile(
    r'this(?:this)? version posted\s+([A-Za-z]+ \d{1,2}, \d{4})', re.I
)
RESCORE_MODELS = (
    'openreviewer-8b sea-e cyclereviewer-8b '
    'deepreviewer-7b-fast deepreviewer-14b deepreviewer-7b'
)
PUBLISHER_OK = {
    'arxiv:2303.07103': 'Boston Review published version',
    'arxiv:2210.08340': 'Neuron journal version',
    'arxiv:2304.01433': 'conference / local PDF',
    'arxiv:2112.03978': 'Nature Reviews Neuroscience',
}


def extra_arxiv_mirrors() -> dict[str, str]:
    out: dict[str, str] = {}
    for key, urls in EXTRA_PDF_URLS.items():
        for url in urls:
            match = ARXIV_PDF_RE.search(url)
            if match:
                out[key] = match.group(1)
                break
    return out


def http_text(url: str, timeout: int = 40, attempts: int = 6) -> str | None:
    delay = 8
    for attempt in range(attempts):
        try:
            request = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(request, timeout=timeout) as resp:
                return resp.read().decode('utf-8', 'replace')
        except urllib.error.HTTPError as exc:
            print(f'  HTTP {exc.code} {url} try {attempt + 1}/{attempts}', flush=True)
            if exc.code == 404:
                return None
            time.sleep(delay)
            delay = min(delay * 2, 90)
        except Exception as exc:  # noqa: BLE001
            print(f'  fail {url} try {attempt + 1}/{attempts}: {exc}', flush=True)
            time.sleep(delay)
            delay = min(delay * 2, 90)
    return None


def parse_abs(html: str) -> dict:
    versions = [int(g) for m in ABS_VER_RE.finditer(html) for g in m.groups() if g]
    latest = max(versions) if versions else None
    revised = ABS_REVISED_RE.search(html)
    submitted = ABS_SUBMITTED_RE.search(html)
    raw_date = ''
    if revised:
        raw_date = re.sub(r'<[^>]+>', '', revised.group(1)).strip()
    elif submitted:
        raw_date = re.sub(r'<[^>]+>', '', submitted.group(1)).strip()
    title = ''
    title_m = re.search(
        r'<meta[^>]+name="citation_title"[^>]+content="([^"]+)"', html, re.I
    )
    if title_m:
        title = ' '.join(title_m.group(1).split())
    return {'latest': latest, 'latest_date': raw_date, 'title': title}


def fetch_arxiv_latest(aid: str) -> dict:
    html = http_text(f'https://arxiv.org/abs/{aid}')
    if html is None:
        return {}
    return parse_abs(html)


def fetch_biorxiv(doi: str) -> list[dict]:
    raw = http_text(f'https://api.biorxiv.org/details/biorxiv/{doi}')
    if not raw:
        return []
    try:
        return json.loads(raw).get('collection') or []
    except json.JSONDecodeError:
        return []


def cache_watermark(key: str, aid: str) -> int | None:
    path = cache_path(key, '.html.gz')
    if not path.exists():
        return None
    raw = read_gz(path)
    _head, _, body = raw.partition('\n')
    return detect_arxiv_version(body, aid)


def md_watermark(key: str, aid: str | None = None) -> tuple[int | None, str]:
    path = FULLTEXT_DIR / f'{safe_key(key)}.md'
    if not path.exists():
        return None, ''
    text = path.read_text(encoding='utf-8')[:12000]
    if aid:
        ver = detect_arxiv_version(text, aid)
        if ver is not None:
            return ver, aid
    found = WATERMARK_RE.search(text)
    if found:
        return int(found.group(2)), found.group(1)
    return None, ''


def md_posted_date(key: str) -> str | None:
    path = FULLTEXT_DIR / f'{safe_key(key)}.md'
    if not path.exists():
        return None
    match = POSTED_RE.search(path.read_text(encoding='utf-8')[:20000])
    if not match:
        return None
    try:
        return datetime.strptime(match.group(1), '%B %d, %Y').strftime('%Y-%m-%d')
    except ValueError:
        return None


def used_arxiv_version(key: str, aid: str, index_row: dict | None) -> int | None:
    if index_row and index_row.get('version') is not None:
        try:
            return int(index_row['version'])
        except (TypeError, ValueError):
            pass
    cached = cache_watermark(key, aid)
    if cached is not None:
        return cached
    ver, _ = md_watermark(key, aid)
    return ver


def is_fresh(row: dict | None, max_age_days: int, force: bool) -> bool:
    if force or not row:
        return False
    checked = row.get('checked') or ''
    try:
        dt = datetime.strptime(checked[:10], '%Y-%m-%d')
    except ValueError:
        return False
    return (datetime.now() - dt).days < max_age_days


def classify_arxiv(used: int | None, latest: int | None, key: str) -> str:
    if key in PUBLISHER_OK:
        return 'ok-publisher'
    if latest is None:
        return 'no-fetch'
    if used is None:
        return 'unknown'
    if used < latest:
        return 'stale'
    return 'ok'


def check_arxiv(paper: dict, index_row: dict | None) -> dict:
    key = paper['key']
    aid = key.split(':', 1)[1]
    used = used_arxiv_version(key, aid, index_row)
    info = fetch_arxiv_latest(aid)
    time.sleep(ARXIV_DELAY)
    latest = info.get('latest')
    return {
        'key': key,
        'aid': aid,
        'source': (index_row or {}).get('source', 'missing'),
        'used': used,
        'latest': latest,
        'latest_date': info.get('latest_date') or '',
        'status': classify_arxiv(used, latest, key),
        'checked': datetime.now().strftime('%Y-%m-%d'),
        'title': (paper.get('line_title') or info.get('title') or '')[:80],
        'reason': PUBLISHER_OK.get(key, ''),
    }


def check_biorxiv(paper: dict, index_row: dict | None) -> dict:
    key = paper['key']
    doi = key.split(':', 1)[1]
    coll = fetch_biorxiv(doi)
    time.sleep(BIORXIV_DELAY)
    versions = [int(c.get('version') or 0) for c in coll]
    latest = max(versions) if versions else None
    dates = {c.get('date'): int(c.get('version') or 0) for c in coll}
    used = None
    if index_row and index_row.get('version') is not None:
        try:
            used = int(index_row['version'])
        except (TypeError, ValueError):
            used = None
    if used is None:
        posted = md_posted_date(key)
        used = dates.get(posted) if posted else None
    if latest is None:
        status = 'no-fetch'
    elif used is None:
        status = 'unknown'
    elif used < latest:
        status = 'stale'
    else:
        status = 'ok'
    latest_date = ''
    if coll:
        latest_date = max((c.get('date') or '') for c in coll)
    return {
        'key': key,
        'aid': doi,
        'source': (index_row or {}).get('source', 'missing'),
        'used': used,
        'latest': latest,
        'latest_date': latest_date,
        'status': status,
        'checked': datetime.now().strftime('%Y-%m-%d'),
        'title': (paper.get('line_title') or '')[:80],
        'reason': '',
    }


def check_mirror(paper: dict, index_row: dict | None, aid: str) -> dict:
    key = paper['key']
    used = used_arxiv_version(key, aid, index_row)
    if used is None:
        used, found = md_watermark(key, aid)
        if found:
            aid = found
    info = fetch_arxiv_latest(aid)
    time.sleep(ARXIV_DELAY)
    return {
        'key': key,
        'aid': aid,
        'source': (index_row or {}).get('source', 'missing'),
        'used': used,
        'latest': info.get('latest'),
        'latest_date': info.get('latest_date') or '',
        'status': 'mirror',
        'checked': datetime.now().strftime('%Y-%m-%d'),
        'title': (paper.get('line_title') or info.get('title') or '')[:80],
        'reason': f'arxiv:{aid}',
    }


def versioned_kind(paper: dict, mirrors: dict[str, str]) -> str | None:
    key = paper['key']
    kind, value = key.split(':', 1)
    if kind == 'arxiv':
        return 'arxiv'
    if kind == 'doi' and value.startswith('10.1101/'):
        return 'biorxiv'
    if key in mirrors:
        return 'mirror'
    _ver, aid = md_watermark(key)
    if aid:
        mirrors[key] = aid
        return 'mirror'
    return None


def run_cmd(args: list[str]) -> None:
    print(' '.join(args), flush=True)
    proc = subprocess.run(args, cwd=str(ROOT))
    if proc.returncode:
        raise SystemExit(proc.returncode)


def refresh_keys(keys: list[str]) -> None:
    python = sys.executable
    for key in keys:
        html = cache_path(key, '.html.gz')
        if html.exists():
            html.unlink()
            print(f'  deleted {html.name}', flush=True)
        run_cmd([python, 'src/fetch_refs.py', '--refresh', '--only', key])
    joined = ','.join(keys)
    run_cmd([python, 'filter/extract_fulltext.py', '--only-keys', joined])
    run_cmd([python, 'filter/fetch_meta.py', '--only-keys', joined])


def print_report(rows: list[dict]) -> dict[str, list[dict]]:
    buckets: dict[str, list[dict]] = {}
    for row in rows:
        buckets.setdefault(row['status'], []).append(row)
    for status in ('stale', 'unknown', 'no-fetch', 'ok-publisher', 'mirror', 'ok'):
        group = buckets.get(status) or []
        print(f'\n== {status.upper()}: {len(group)}', flush=True)
        if status in ('ok',) and len(group) > 12:
            continue
        for rec in group:
            used = rec.get('used')
            latest = rec.get('latest')
            extra = rec.get('reason') or rec.get('latest_date') or ''
            print(
                f'  {rec["key"]:36s} used={used} latest={latest} '
                f'src={rec.get("source")} {extra} | {rec.get("title", "")}',
                flush=True,
            )
    counts = {status: len(items) for status, items in buckets.items()}
    print(
        f'\nmacro: {counts}  total={len(rows)}  wrote {VERSIONS_JSONL}',
        flush=True,
    )
    return buckets


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--only-keys', default='')
    parser.add_argument('--force', action='store_true')
    parser.add_argument('--refresh', action='store_true')
    parser.add_argument('--max-age', type=int, default=7)
    return parser.parse_args()


def check_paper(
    paper: dict,
    index_row: dict | None,
    kind: str,
    mirrors: dict[str, str],
) -> dict:
    if kind == 'arxiv':
        return check_arxiv(paper, index_row)
    if kind == 'biorxiv':
        return check_biorxiv(paper, index_row)
    return check_mirror(paper, index_row, mirrors[paper['key']])


def main() -> None:
    args = parse_args()
    papers = read_jsonl(PAPERS_JSONL)
    if not papers:
        raise SystemExit('run filter/collect_readme.py first')
    wanted = {part.strip() for part in args.only_keys.split(',') if part.strip()}
    index = {row['key']: row for row in read_jsonl(FULLTEXT_INDEX)}
    previous = {row['key']: row for row in read_jsonl(VERSIONS_JSONL)}
    mirrors = extra_arxiv_mirrors()
    by_key = dict(previous)
    todo: list[tuple[dict, str]] = []
    skipped = 0
    reused = 0
    for paper in papers:
        key = paper['key']
        if wanted and key not in wanted:
            continue
        kind = versioned_kind(paper, mirrors)
        if kind is None:
            skipped += 1
            if wanted:
                print(f'skip {key} (not versioned)', flush=True)
            continue
        if is_fresh(previous.get(key), args.max_age, args.force):
            by_key[key] = previous[key]
            reused += 1
            continue
        todo.append((paper, kind))

    print(
        f'{len(todo)} to fetch, {reused} cached, {skipped} not versioned',
        flush=True,
    )
    for done, (paper, kind) in enumerate(todo, start=1):
        rec = check_paper(paper, index.get(paper['key']), kind, mirrors)
        by_key[paper['key']] = rec
        print(
            f'progress: {done}/{len(todo)} ({100 * done / max(len(todo), 1):.0f}%) '
            f'{rec["key"]} used={rec["used"]} latest={rec["latest"]} '
            f'status={rec["status"]}',
            flush=True,
        )
        if done % 20 == 0:
            write_versions(papers, by_key)

    write_versions(papers, by_key)

    if args.refresh:
        stale = [
            rec['key'] for rec in checked_rows(papers, by_key, wanted)
            if rec.get('status') == 'stale'
        ]
        if not stale:
            print('no stale keys to refresh', flush=True)
        else:
            print(f'refreshing {len(stale)} stale: {", ".join(stale)}', flush=True)
            refresh_keys(stale)
            index = {row['key']: row for row in read_jsonl(FULLTEXT_INDEX)}
            papers_by_key = {p['key']: p for p in papers}
            for i, key in enumerate(stale, start=1):
                paper = papers_by_key[key]
                kind = versioned_kind(paper, mirrors) or 'arxiv'
                rec = check_paper(paper, index.get(key), kind, mirrors)
                by_key[key] = rec
                print(
                    f'recheck: {i}/{len(stale)} {key} used={rec["used"]} '
                    f'latest={rec["latest"]} status={rec["status"]}',
                    flush=True,
                )
            write_versions(papers, by_key)
            print_rescore_hint(stale)

    rows = checked_rows(papers, by_key, wanted)
    buckets = print_report(rows)
    if buckets.get('stale'):
        raise SystemExit(1)


def checked_rows(
    papers: list[dict], by_key: dict[str, dict], wanted: set[str]
) -> list[dict]:
    rows = []
    for paper in papers:
        if wanted and paper['key'] not in wanted:
            continue
        rec = by_key.get(paper['key'])
        if rec and rec.get('status'):
            rows.append(rec)
    return rows


def write_versions(papers: list[dict], by_key: dict[str, dict]) -> None:
    order = [paper['key'] for paper in papers]
    seen = set(order)
    rows = [by_key[key] for key in order if key in by_key]
    rows.extend(by_key[key] for key in by_key if key not in seen)
    write_jsonl(VERSIONS_JSONL, rows)


def print_rescore_hint(keys: list[str]) -> None:
    joined = ','.join(keys)
    print(
        f'\nRescore on the GPU box (ask first; SciJudge shifts existing scores):\n'
        f"  KEYS='{joined}' MODELS='{RESCORE_MODELS}' "
        f'./_rescore_eight.sh\n'
        f'Abstract scorers (NAIP / SciJudge / DGC-BERT) only if meta.jsonl '
        f'abstract changed. Then filter/build_report.py and add_score_badges.py.',
        flush=True,
    )


if __name__ == '__main__':
    main()
