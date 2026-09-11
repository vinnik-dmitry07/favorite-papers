'''Reparse saved DeepReviewer reviews after the boxed_review fix.

    python filter/reparse_reviews.py
'''

from __future__ import annotations

import sys
from pathlib import Path

FILTER_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(FILTER_DIR))
sys.path.insert(0, str(FILTER_DIR / 'remote'))

from paths import (  # noqa: E402
    FILTER_DIR as ROOT,
    REVIEWS_DIR,
    SCORE_FILES,
    is_score_row,
    read_jsonl,
    safe_key,
    write_jsonl,
)
from parse_review import parse_review  # noqa: E402
from score_reviewers import score_row  # noqa: E402

DEEP_MODELS = (
    'deepreviewer-7b',
    'deepreviewer-7b-fast',
    'deepreviewer-14b',
)


def reparse_model(name: str) -> tuple[int, int, int]:
    scores_path = ROOT / SCORE_FILES[name]
    review_dir = REVIEWS_DIR / name
    old_rows = read_jsonl(scores_path)
    if not old_rows:
        print(f'{name}: no scores', flush=True)
        return 0, 0, 0
    # Resumed runs can append a key twice; the last row is the freshest.
    last_by_key: dict[str, dict] = {}
    for old in old_rows:
        last_by_key[old.get('key') or id(old)] = old
    n_dups = len(old_rows) - len(last_by_key)
    old_rows = list(last_by_key.values())
    new_rows = []
    recovered = 0
    still_bad = 0
    kept = 0
    for old in old_rows:
        key = old.get('key')
        path = review_dir / f'{safe_key(key)}.md' if key else None
        if not key or path is None or not path.exists():
            new_rows.append(old)
            kept += 1
            continue
        raw = path.read_text(encoding='utf-8', errors='replace')
        parsed = parse_review(raw, kind='deep')
        if parsed['rating'] is None and parsed['decision'] is None:
            new_rows.append({
                'key': key,
                'error': old.get('error') or 'unparsed:ok',
                'raw_tail': raw[-300:],
            })
            still_bad += 1
            continue
        row = score_row(key, parsed, partial=bool(old.get('partial')))
        new_rows.append(row)
        if not is_score_row(old):
            recovered += 1
        else:
            kept += 1
    write_jsonl(scores_path, new_rows)
    print(
        f'{name}: {len(new_rows)} rows, recovered={recovered} '
        f'still_unparsed={still_bad} kept={kept} dropped_dups={n_dups}',
        flush=True,
    )
    return len(new_rows), recovered, still_bad


def main() -> None:
    total_rec = 0
    for name in DEEP_MODELS:
        _n, recovered, _bad = reparse_model(name)
        total_rec += recovered
    print(f'reparse_reviews: recovered {total_rec} rows', flush=True)


if __name__ == '__main__':
    main()
