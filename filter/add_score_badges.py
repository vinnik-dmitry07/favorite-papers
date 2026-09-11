'''Insert compact score badges into readme.md after each paper's links.

    python filter/add_score_badges.py
'''

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

FILTER_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(FILTER_DIR))

from paths import README, SCORES_CSV, load_joined, report_anchor  # noqa: E402

SCORE_BADGE = re.compile(r'\s*\[⚖ [^\]]*\]\(filter/report\.md#[^)]+\)')
MD_HREF_RE = re.compile(r'\[[^\]]*\]\(([^)]+)\)')
ARXIV_ID_RE = re.compile(r'(?<![\d.])(\d{4}\.\d{4,5})(?![\d])')
LEGEND_RE = re.compile(r'^Score badges:.*$', re.M)
LEGEND = (
    'Score badges: [⚖ final · accepts/models · WATCH|DROP](filter/report.md) — aggregated quality '
    'in [-1, +1]. 0 is where reviewer Accept/Reject votes split 50/50. '
    'accepts/models are raw reviewer votes, not the aggregated score. '
    'WATCH/DROP is appended when the verdict is not KEEP. '
    'Older landmark papers can be inflated (pretrain leakage).'
)


def badge_text(
    final_score,
    accepts: int,
    n_models: int,
    key: str,
    verdict: str | None = None,
) -> str | None:
    if final_score in (None, '') and not n_models:
        return None
    if final_score in (None, ''):
        label = f'⚖ — · {accepts}/{n_models}'
    else:
        label = f'⚖ {float(final_score):+.2f} · {accepts}/{n_models}'
    if verdict in ('WATCH', 'DROP'):
        label += f' · {verdict}'
    return f'[{label}](filter/report.md#{report_anchor(key)})'


def load_scores() -> dict[str, dict]:
    if not SCORES_CSV.exists():
        return {}
    with SCORES_CSV.open(encoding='utf-8', newline='') as handle:
        return {row['key']: row for row in csv.DictReader(handle)}


def as_int(value) -> int:
    try:
        return int(float(value))
    except (TypeError, ValueError):
        return 0


def line_targets(line: str) -> set[str]:
    found = set(MD_HREF_RE.findall(line))
    found.update(ARXIV_ID_RE.findall(line))
    return found


def paper_markers(paper: dict) -> list[str]:
    marks = [url for url in (paper.get('urls') or []) if url]
    key = paper.get('key') or ''
    if ':' in key:
        marks.append(key.split(':', 1)[1])
    return [mark for mark in marks if mark]


def papers_on_line(line: str, papers: list[dict]) -> list[dict]:
    targets = line_targets(line)
    hits = []
    seen: set[str] = set()
    for paper in papers:
        if paper['key'] in seen:
            continue
        for mark in paper_markers(paper):
            if mark in targets or f']({mark})' in line:
                seen.add(paper['key'])
                hits.append(paper)
                break
    return hits


def strip_badges(line: str) -> str:
    return SCORE_BADGE.sub('', line).rstrip()


def inject_legend(text: str) -> str:
    lines = [line for line in text.splitlines() if not LEGEND_RE.match(line.strip())]
    if lines and lines[0].startswith('# '):
        first_non_blank = 1
        while first_non_blank < len(lines) and lines[first_non_blank].strip() == '':
            first_non_blank += 1
        lines[1:first_non_blank] = ['', LEGEND, '']
        return '\n'.join(lines) + ('\n' if text.endswith('\n') else '')
    return LEGEND + '\n\n' + text


def badge_for(paper: dict, scores: dict[str, dict]) -> str | None:
    row = scores.get(paper['key'])
    if not row:
        return None
    return badge_text(
        row.get('final_score'),
        as_int(row.get('accept_votes')),
        as_int(row.get('n_models')),
        paper['key'],
        row.get('verdict'),
    )


def main() -> None:
    scores = load_scores()
    papers = load_joined()
    original = README.read_text(encoding='utf-8')
    updated = []
    changed = 0
    for line in original.splitlines():
        if LEGEND_RE.match(line.strip()):
            continue
        clean = strip_badges(line)
        hits = papers_on_line(clean, papers)
        badges = [badge for paper in hits if (badge := badge_for(paper, scores))]
        next_line = f'{clean} {" ".join(badges)}'.rstrip() if badges else clean
        if next_line != line:
            changed += 1
        updated.append(next_line)
    text = '\n'.join(updated)
    if original.endswith('\n'):
        text += '\n'
    text = inject_legend(text)
    tmp = README.with_name(README.name + '.tmp')
    tmp.write_text(text, encoding='utf-8')
    tmp.replace(README)
    print(f'add_score_badges: updated {changed} lines in {README}', flush=True)


if __name__ == '__main__':
    main()
