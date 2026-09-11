'''Print parse stats for a scores jsonl (bench 8 keys).'''
from __future__ import annotations

import json
import sys
from pathlib import Path

KEYS = [
    'arxiv:2608.17163',
    'arxiv:2509.09675',
    'arxiv:2503.14858',
    'arxiv:2501.16142',
    'arxiv:2411.03820',
    'arxiv:2312.13327',
    'arxiv:2312.00276',
    'arxiv:2306.02451',
]


def main() -> None:
    path = Path(sys.argv[1])
    wanted = set(KEYS)
    rows = []
    if path.exists():
        for line in path.read_text(encoding='utf-8').splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            if row.get('key') in wanted:
                rows.append(row)
    ratings = [row.get('rating') for row in rows if row.get('rating') is not None]
    decisions = [row.get('decision') for row in rows if row.get('decision')]
    errors = [row for row in rows if row.get('error')]
    print(f'file={path} n={len(rows)} rating={len(ratings)} decision={len(decisions)} error={len(errors)}')
    if ratings:
        print(f'rating min={min(ratings)} max={max(ratings)} mean={sum(ratings)/len(ratings):.2f}')
    if decisions:
        acc = sum(1 for d in decisions if str(d).lower().startswith('acc'))
        print(f'decision Accept={acc} Reject={len(decisions)-acc}')
    for row in rows:
        key = row.get('key')
        if row.get('error'):
            print(f'  {key} ERROR {row.get("error")}')
        else:
            print(
                f'  {key} rating={row.get("rating")} '
                f'decision={row.get("decision")} finish={row.get("finish")}'
            )


if __name__ == '__main__':
    main()
