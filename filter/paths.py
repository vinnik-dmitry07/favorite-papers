'''Shared paths and helpers for the readme paper-scoring pipeline.'''

from __future__ import annotations

import importlib.util
import json
import re
from pathlib import Path

FILTER_DIR = Path(__file__).resolve().parent
ROOT = FILTER_DIR.parent
SRC = ROOT / 'src'

_spec = importlib.util.spec_from_file_location('map_common', SRC / 'common.py')
map_common = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(map_common)

CACHE_DIR = map_common.CACHE_DIR
CATALOG = map_common.CATALOG
README = map_common.README
cache_path = map_common.cache_path
classify = map_common.classify
load_json = map_common.load_json
read_gz = map_common.read_gz

PAPERS_JSONL = FILTER_DIR / 'papers.jsonl'
META_JSONL = FILTER_DIR / 'meta.jsonl'
FULLTEXT_DIR = FILTER_DIR / 'fulltext'
FULLTEXT_INDEX = FILTER_DIR / 'fulltext_index.jsonl'
FULLTEXT_ZIP = FILTER_DIR / 'fulltext.zip'
SCORES_CSV = FILTER_DIR / 'scores.csv'
REPORT_MD = FILTER_DIR / 'report.md'
REVIEWS_DIR = FILTER_DIR / 'reviews'
LOGS_DIR = FILTER_DIR / 'logs'
REMOTE_DIR = FILTER_DIR / 'remote'

SCOREABLE_KINDS = frozenset({'arxiv', 'openreview', 'acl', 'doi'})
SAFE_KEY_RE = re.compile(r'[^A-Za-z0-9._-]+')
SUCCESS_FIELDS = ('score', 'bt_score', 'p_accept', 'rating', 'decision')


def safe_key(key: str) -> str:
    return SAFE_KEY_RE.sub('_', key)[:120]


def year_of(row: dict) -> str:
    published = row.get('published') or ''
    if len(published) >= 4 and published[:4].isdigit():
        return published[:4]
    key = row.get('key') or ''
    if key.startswith('arxiv:'):
        aid = key.split(':', 1)[1]
        match = re.match(r'^(\d{2})(\d{2})\.\d{4,5}', aid)
        if match:
            year = int(match.group(1))
            century = 1900 if year >= 91 else 2000
            return f'{century + year:04d}'
    return 'unknown'


def is_score_row(row: dict) -> bool:
    if not row.get('key') or row.get('error'):
        return False
    if row.get('bt_score') is not None:
        return bool(row.get('n_valid'))
    if row.get('p_accept') is not None:
        return True
    if row.get('score') is not None:
        return True
    return row.get('rating') is not None or bool(row.get('decision'))


def last_valid_by_key(rows: list[dict], key_field: str = 'key') -> list[dict]:
    '''Same logical key: scan in order, ignore malformed, keep latest valid.'''
    latest: dict[str, dict] = {}
    valid: dict[str, dict] = {}
    for row in rows:
        key = row.get(key_field)
        if not key:
            continue
        latest[key] = row
        if is_score_row(row):
            valid[key] = row
    out = dict(latest)
    out.update(valid)
    return list(out.values())


SCORE_FILES = {
    'naipv2': 'scores_naipv2.jsonl',
    'naipv1': 'scores_naipv1.jsonl',
    'scijudge': 'scores_scijudge.jsonl',
    'dgcbert': 'scores_dgcbert.jsonl',
    'cyclereviewer-8b': 'scores_cyclereviewer-8b.jsonl',
    'cyclereviewer-70b': 'scores_cyclereviewer-70b.jsonl',
    'deepreviewer-7b': 'scores_deepreviewer-7b.jsonl',
    'deepreviewer-7b-fast': 'scores_deepreviewer-7b-fast.jsonl',
    'deepreviewer-14b': 'scores_deepreviewer-14b.jsonl',
    'openreviewer-8b': 'scores_openreviewer-8b.jsonl',
    'sea-e': 'scores_sea-e.jsonl',
}


def report_anchor(key: str) -> str:
    return SAFE_KEY_RE.sub('-', key.replace(':', '-'))[:80]


def load_joined() -> list[dict]:
    papers = read_jsonl(PAPERS_JSONL)
    meta = {row['key']: row for row in read_jsonl(META_JSONL)}
    rows = []
    for paper in papers:
        item = dict(paper)
        item.update(meta.get(paper['key'], {}))
        if not item.get('title'):
            item['title'] = paper.get('line_title') or ''
        rows.append(item)
    return rows

TG_KEY_ALIASES = {
    'openreview': ('openreview', 'or'),
}


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + '.tmp')
    with tmp.open('w', encoding='utf-8') as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + '\n')
    tmp.replace(path)


def append_jsonl(path: Path, row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a', encoding='utf-8') as handle:
        handle.write(json.dumps(row, ensure_ascii=False) + '\n')
        handle.flush()


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if line:
            rows.append(json.loads(line))
    return rows


def scored_keys(path: Path, key_field: str = 'key') -> set[str]:
    return {
        row[key_field] for row in read_jsonl(path)
        if row.get(key_field) and is_score_row(row)
    }


def tg_lookup_keys(node_id: str) -> list[str]:
    '''Keys stored in the Telegram index for this catalog id.'''
    import sys

    if str(SRC) not in sys.path:
        sys.path.insert(0, str(SRC))
    from add_tg_links import normalize_keys

    kind, value = node_id.split(':', 1)
    aliases = TG_KEY_ALIASES.get(kind, (kind,))
    raw = {f'{alias}:{value}' for alias in aliases}
    return list(normalize_keys(raw))


def print_progress(done: int, total: int, extra: str = '') -> None:
    pct = 100 * done / total if total else 100
    suffix = f'  {extra}' if extra else ''
    print(f'\rprogress: {done}/{total} ({pct:.0f}%){suffix}', end='', flush=True)
    if done >= total:
        print(flush=True)
