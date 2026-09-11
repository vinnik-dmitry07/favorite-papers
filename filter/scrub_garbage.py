'''Mark challenge/missing fulltext as no_fulltext; flag short texts partial.

    python filter/scrub_garbage.py
'''

from __future__ import annotations

import sys
from pathlib import Path

FILTER_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(FILTER_DIR))

from paths import (  # noqa: E402
    FILTER_DIR as ROOT,
    FULLTEXT_DIR,
    FULLTEXT_INDEX,
    SCORE_FILES,
    is_score_row,
    read_jsonl,
    safe_key,
    write_jsonl,
)

FULLTEXT_MODELS = (
    'cyclereviewer-8b',
    'cyclereviewer-70b',
    'deepreviewer-7b',
    'deepreviewer-7b-fast',
    'deepreviewer-14b',
    'openreviewer-8b',
    'sea-e',
)
# Keys to force to no_fulltext even if the index looks fine.
HARD_MISSING: set[str] = set()


def missing_keys() -> set[str]:
    keys = set(HARD_MISSING)
    for row in read_jsonl(FULLTEXT_INDEX):
        if row.get('source') == 'missing' or row.get('n_tokens') == 0:
            keys.add(row['key'])
    for path in FULLTEXT_DIR.glob('*.md'):
        if path.stat().st_size < 200:
            keys.add(path.stem.replace('_', ':', 1))
    return keys


def short_keys(exclude: set[str]) -> set[str]:
    keys = set()
    for row in read_jsonl(FULLTEXT_INDEX):
        if row['key'] in exclude:
            continue
        if row.get('incomplete') or (row.get('n_tokens') or 0) < 1500:
            keys.add(row['key'])
    for path in FULLTEXT_DIR.glob('*.md'):
        key = path.stem.replace('_', ':', 1)
        if key in exclude:
            continue
        if path.stat().st_size < 6000:
            keys.add(key)
    return keys


def scrub_model(name: str, missing: set[str], short: set[str]) -> tuple[int, int]:
    path = ROOT / SCORE_FILES[name]
    rows = read_jsonl(path)
    if not rows:
        return 0, 0
    n_missing = 0
    n_partial = 0
    out = []
    for row in rows:
        key = row.get('key')
        if key in missing:
            out.append({'key': key, 'error': 'no_fulltext'})
            n_missing += 1
            continue
        if key in short and is_score_row(row):
            row = dict(row)
            row['partial'] = True
            n_partial += 1
        out.append(row)
    write_jsonl(path, out)
    print(f'{name}: no_fulltext={n_missing} partial={n_partial}', flush=True)
    return n_missing, n_partial


def main() -> None:
    missing = missing_keys()
    short = short_keys(missing)
    print(f'scrub: missing={len(missing)} short={len(short)}', flush=True)
    for key in sorted(missing):
        print(f'  missing {key}', flush=True)
    for name in FULLTEXT_MODELS:
        scrub_model(name, missing, short)


if __name__ == '__main__':
    main()
