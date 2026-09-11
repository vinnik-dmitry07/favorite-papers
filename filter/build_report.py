'''Merge model scores into scores.csv and write report.md.

    python filter/build_report.py
'''

from __future__ import annotations

import csv
import math
import re
import sys
from collections import defaultdict
from pathlib import Path
from statistics import mean

FILTER_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(FILTER_DIR))

from aggregate import (  # noqa: E402
    AGG_FIELDS,
    aggregate,
    load_and_salvage,
    report_lines,
    tables_by_file,
)
from paths import (  # noqa: E402
    FILTER_DIR as ROOT,
    REPORT_MD,
    REVIEWS_DIR,
    SCORE_FILES,
    SCORES_CSV,
    is_score_row,
    last_valid_by_key,
    load_joined,
    read_jsonl,
    report_anchor,
    safe_key,
    year_of,
)

CSV_FIELDS = [
    'key', 'section', 'title', 'published', 'tg_channels', 'tg_first_post',
    'naipv2', 'naipv1', 'scijudge_bt', 'dgcbert_p',
    'cr8b_rating', 'cr8b_decision',
    'cr70b_rating', 'cr70b_decision',
    'dr7b_rating', 'dr7b_decision',
    'dr7bf_rating', 'dr7bf_decision',
    'dr7bf_soundness', 'dr7bf_presentation', 'dr7bf_contribution',
    'dr14b_rating', 'dr14b_decision',
    'or8b_rating', 'or8b_decision', 'or8b_soundness', 'or8b_presentation', 'or8b_contribution',
    'seae_rating', 'seae_decision',
    'mean_rating10', 'accept_votes', 'n_models', 'rank_avg', 'rank_in_year',
    'final_score', 'final_conf', 'final_pct', 'impact_z', 'verdict', 'q_hat',
    'salvage',
]

MEAN_RATING10 = [
    ('cr8b_rating', 'cr8b_decision'),
    ('dr7bf_rating', 'dr7bf_decision'),
    ('dr14b_rating', 'dr14b_decision'),
    ('or8b_rating', 'or8b_decision'),
    ('seae_rating', 'seae_decision'),
]
VOTE_RATING10 = [
    ('cr8b_rating', 'cr8b_decision'),
    ('dr7b_rating', 'dr7b_decision'),
    ('dr7bf_rating', 'dr7bf_decision'),
    ('dr14b_rating', 'dr14b_decision'),
    ('or8b_rating', 'or8b_decision'),
    ('seae_rating', 'seae_decision'),
]

NUMERIC = [
    'naipv2', 'naipv1', 'scijudge_bt', 'dgcbert_p',
    'cr8b_rating', 'cr70b_rating', 'dr7b_rating', 'dr7bf_rating', 'dr14b_rating',
    'or8b_rating', 'seae_rating',
]


def by_key(name: str) -> dict[str, dict]:
    return {
        row['key']: row
        for row in last_valid_by_key(read_jsonl(ROOT / SCORE_FILES[name]))
        if is_score_row(row)
    }


def as_float(value) -> float | None:
    if value is None or value == '':
        return None
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if math.isnan(number):
        return None
    return number


def decision_of(rating, decision) -> str | None:
    if isinstance(decision, str) and decision.strip():
        text = decision.strip().lower()
        if re.search(r'\breject\b', text):
            return 'Reject'
        if re.search(r'\baccept\b', text):
            return 'Accept'
    number = as_float(rating)
    if number is None:
        return None
    return 'Accept' if number >= 6 else 'Reject'


def percentile_ranks(values: list[tuple[str, float]], reverse: bool = True) -> dict[str, float]:
    raw = ranks(values, reverse=reverse)
    n = len(values)
    if n <= 1:
        return {key: 50.0 for key in raw}
    return {key: 100.0 * (n - rank) / (n - 1) for key, rank in raw.items()}


def ranks(values: list[tuple[str, float]], reverse: bool = True) -> dict[str, float]:
    ordered = sorted(values, key=lambda item: item[1], reverse=reverse)
    result: dict[str, float] = {}
    index = 0
    while index < len(ordered):
        end = index
        while end + 1 < len(ordered) and ordered[end + 1][1] == ordered[index][1]:
            end += 1
        rank = (index + end + 2) / 2
        for pos in range(index, end + 1):
            result[ordered[pos][0]] = rank
        index = end + 1
    return result


def pearson(xs: list[float], ys: list[float]) -> float | None:
    n = len(xs)
    if n < 3:
        return None
    mx, my = sum(xs) / n, sum(ys) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    dx = math.sqrt(sum((x - mx) ** 2 for x in xs))
    dy = math.sqrt(sum((y - my) ** 2 for y in ys))
    if dx == 0 or dy == 0:
        return None
    return num / (dx * dy)


def spearman(xs: list[float], ys: list[float]) -> float | None:
    rx = ranks([(str(i), x) for i, x in enumerate(xs)])
    ry = ranks([(str(i), y) for i, y in enumerate(ys)])
    return pearson([rx[str(i)] for i in range(len(xs))], [ry[str(i)] for i in range(len(ys))])


def macro_f1(truth: list[str], pred: list[str]) -> float | None:
    labels = ('Accept', 'Reject')
    if len(truth) < 2:
        return None
    scores = []
    for label in labels:
        tp = sum(1 for t, p in zip(truth, pred) if t == label and p == label)
        fp = sum(1 for t, p in zip(truth, pred) if t != label and p == label)
        fn = sum(1 for t, p in zip(truth, pred) if t == label and p != label)
        prec = tp / (tp + fp) if tp + fp else 0.0
        rec = tp / (tp + fn) if tp + fn else 0.0
        scores.append(2 * prec * rec / (prec + rec) if prec + rec else 0.0)
    return sum(scores) / len(scores)


def symmetric_macro_f1(left: list[str], right: list[str]) -> float | None:
    a = macro_f1(left, right)
    b = macro_f1(right, left)
    if a is None or b is None:
        return None
    return (a + b) / 2


def fmt(value, digits: int = 3) -> str:
    if value is None:
        return ''
    if isinstance(value, float):
        return f'{value:.{digits}f}'
    return str(value)


def signed(value, digits: int = 2) -> str:
    if value is None:
        return ''
    return f'{float(value):+.{digits}f}'


def weaknesses_for(key: str, fallback: str = '') -> str:
    safe = safe_key(key)
    chunks = []
    if REVIEWS_DIR.exists():
        for path in sorted(REVIEWS_DIR.glob(f'*/{safe}.md')):
            text = path.read_text(encoding='utf-8', errors='replace')
            lower = text.lower()
            mark = lower.find('weakness')
            if mark == -1:
                continue
            snippet = text[mark:mark + 400].replace('\n', ' ')
            chunks.append(f'{path.parent.name}: {snippet}')
            if len(chunks) >= 2:
                break
    if chunks:
        return ' '.join(chunks)[:500]
    return fallback


def merge_row(paper: dict, tables: dict[str, dict[str, dict]]) -> dict:
    naipv2 = tables['naipv2'].get(paper['key'], {})
    naipv1 = tables['naipv1'].get(paper['key'], {})
    sci = tables['scijudge'].get(paper['key'], {})
    dgc = tables['dgcbert'].get(paper['key'], {})
    cr8 = tables['cyclereviewer-8b'].get(paper['key'], {})
    cr70 = tables['cyclereviewer-70b'].get(paper['key'], {})
    dr7 = tables['deepreviewer-7b'].get(paper['key'], {})
    dr7f = tables['deepreviewer-7b-fast'].get(paper['key'], {})
    dr14 = tables['deepreviewer-14b'].get(paper['key'], {})
    ore = tables['openreviewer-8b'].get(paper['key'], {})
    sea = tables['sea-e'].get(paper['key'], {})
    posts = paper.get('tg_posts') or []
    channels = sorted({post.get('channel') for post in posts if post.get('channel')})
    first = min((post.get('date') or '9999' for post in posts), default='')
    if first == '9999':
        first = ''
    row = {
        'key': paper['key'],
        'section': paper.get('section') or '',
        'title': paper.get('title') or paper.get('line_title') or '',
        'published': paper.get('published') or '',
        'tg_channels': ';'.join(channels),
        'tg_first_post': first,
        'naipv2': as_float(naipv2.get('score')),
        'naipv1': as_float(naipv1.get('score')),
        'scijudge_bt': as_float(sci.get('bt_score')),
        'dgcbert_p': as_float(dgc.get('p_accept')),
        'cr8b_rating': as_float(cr8.get('rating')),
        'cr8b_decision': decision_of(cr8.get('rating'), cr8.get('decision')),
        'cr70b_rating': as_float(cr70.get('rating')),
        'cr70b_decision': decision_of(cr70.get('rating'), cr70.get('decision')),
        'dr7b_rating': as_float(dr7.get('rating')),
        'dr7b_decision': decision_of(dr7.get('rating'), dr7.get('decision')),
        'dr7bf_rating': as_float(dr7f.get('rating')),
        'dr7bf_decision': decision_of(dr7f.get('rating'), dr7f.get('decision')),
        'dr7bf_soundness': dr7f.get('soundness'),
        'dr7bf_presentation': dr7f.get('presentation'),
        'dr7bf_contribution': dr7f.get('contribution'),
        'dr14b_rating': as_float(dr14.get('rating')),
        'dr14b_decision': decision_of(dr14.get('rating'), dr14.get('decision')),
        'or8b_rating': as_float(ore.get('rating')),
        'or8b_decision': decision_of(ore.get('rating'), ore.get('decision')),
        'or8b_soundness': ore.get('soundness'),
        'or8b_presentation': ore.get('presentation'),
        'or8b_contribution': ore.get('contribution'),
        'seae_rating': as_float(sea.get('rating')),
        'seae_decision': decision_of(sea.get('rating'), sea.get('decision')),
        'partial': any(
            bool(src.get('partial'))
            for src in (cr8, cr70, dr7, dr7f, dr14, ore, sea)
        ),
        'salvage': ';'.join(
            name for src, name in (
                (cr8, 'cr8b'), (dr7, 'dr7b'), (dr7f, 'dr7bf'),
                (dr14, 'dr14b'), (ore, 'or8b'), (sea, 'seae'),
            ) if src.get('salvage')
        ),
        '_weak': cr8.get('weaknesses') or ore.get('weaknesses') or sea.get('weaknesses') or '',
    }
    ratings = [row[field] for field, _ in MEAN_RATING10 if row[field] is not None]
    row['mean_rating10'] = mean(ratings) if ratings else None
    votes = []
    for field, dec_field in VOTE_RATING10:
        src = {
            'cr8b_rating': cr8, 'dr7b_rating': dr7, 'dr7bf_rating': dr7f,
            'dr14b_rating': dr14, 'or8b_rating': ore, 'seae_rating': sea,
        }.get(field) or {}
        if src.get('salvage'):
            continue
        votes.append(decision_of(row[field], row[dec_field] if dec_field else None))
    if row['dgcbert_p'] is not None:
        votes.append('Accept' if row['dgcbert_p'] >= 0.5 else 'Reject')
    known = [vote for vote in votes if vote]
    row['accept_votes'] = sum(1 for vote in known if vote == 'Accept')
    row['n_models'] = len(known)
    return row


def add_ranks(rows: list[dict]) -> None:
    rank_sets: list[dict[str, float]] = []
    for field in NUMERIC:
        if field == 'scijudge_bt':
            by_year: dict[str, list[tuple[str, float]]] = defaultdict(list)
            for row in rows:
                value = row.get(field)
                if value is not None:
                    by_year[year_of(row)].append((row['key'], value))
            merged: dict[str, float] = {}
            for group in by_year.values():
                merged.update(percentile_ranks(group))
            if merged:
                rank_sets.append(merged)
            continue
        pairs = [(row['key'], row[field]) for row in rows if row.get(field) is not None]
        if pairs:
            rank_sets.append(percentile_ranks(pairs))
    for row in rows:
        present = [table[row['key']] for table in rank_sets if row['key'] in table]
        row['rank_avg'] = mean(present) if present else None
    by_year = defaultdict(list)
    for row in rows:
        if row['rank_avg'] is not None:
            by_year[year_of(row)].append((row['key'], row['rank_avg']))
    year_rank: dict[str, float] = {}
    for group in by_year.values():
        year_rank.update(ranks(group))
    for row in rows:
        row['rank_in_year'] = year_rank.get(row['key'])


def write_csv(rows: list[dict]) -> None:
    SCORES_CSV.parent.mkdir(parents=True, exist_ok=True)
    with SCORES_CSV.open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS, extrasaction='ignore')
        writer.writeheader()
        for row in rows:
            extra_prec = {'final_score', 'final_conf', 'q_hat'}
            out = {}
            for field in CSV_FIELDS:
                if field in extra_prec:
                    prec = 6
                elif 'rank' in field or field.endswith('_p') or field == 'final_pct':
                    prec = 4
                else:
                    prec = 3
                out[field] = fmt(row.get(field), prec)
            out['key'] = row['key']
            out['section'] = row['section']
            out['title'] = row['title']
            out['published'] = row['published']
            out['tg_channels'] = row['tg_channels']
            out['tg_first_post'] = row['tg_first_post']
            for field in (
                'cr8b_decision', 'cr70b_decision', 'dr7b_decision',
                'dr7bf_decision', 'dr14b_decision', 'or8b_decision',
                'seae_decision',
            ):
                out[field] = row.get(field) or ''
            out['accept_votes'] = row['accept_votes']
            out['n_models'] = row['n_models']
            out['verdict'] = row.get('verdict') or ''
            out['salvage'] = row.get('salvage') or ''
            for field in (
                'dr7bf_soundness', 'dr7bf_presentation', 'dr7bf_contribution',
            ):
                value = row.get(field)
                out[field] = '' if value is None else str(value)
            writer.writerow(out)


def coverage_table(rows: list[dict]) -> list[tuple[str, int]]:
    labels = [
        ('NAIPv2', 'naipv2'),
        ('NAIP-v1', 'naipv1'),
        ('SciJudge BT', 'scijudge_bt'),
        ('DGC-BERT p(accept)', 'dgcbert_p'),
        ('CycleReviewer-8B', 'cr8b_rating'),
        ('CycleReviewer-70B', 'cr70b_rating'),
        ('DeepReviewer-7B Standard', 'dr7b_rating'),
        ('DeepReviewer-7B Fast', 'dr7bf_rating'),
        ('DeepReviewer-14B Fast', 'dr14b_rating'),
        ('OpenReviewer-8B', 'or8b_rating'),
        ('SEA-E', 'seae_rating'),
    ]
    return [(name, sum(1 for row in rows if row.get(field) is not None)) for name, field in labels]


def accept_label(row: dict, kind: str) -> str | None:
    if kind == 'dgcbert':
        value = row.get('dgcbert_p')
        if value is None:
            return None
        return 'Accept' if value >= 0.5 else 'Reject'
    if kind == 'or8b':
        return decision_of(row.get('or8b_rating'), row.get('or8b_decision'))
    mapping = {
        'cr8b': ('cr8b_rating', 'cr8b_decision'),
        'cr70b': ('cr70b_rating', 'cr70b_decision'),
        'dr7b': ('dr7b_rating', 'dr7b_decision'),
        'dr7bf': ('dr7bf_rating', 'dr7bf_decision'),
        'dr14b': ('dr14b_rating', 'dr14b_decision'),
        'seae': ('seae_rating', 'seae_decision'),
    }
    rating_field, decision_field = mapping[kind]
    return decision_of(row.get(rating_field), row.get(decision_field))


def agreement(rows: list[dict]) -> tuple[list[str], list[str]]:
    spear_lines = ['| model A | model B | n | Spearman |', '|---|---|---:|---:|']
    f1_lines = ['| model A | model B | n | macro-F1 |', '|---|---|---:|---:|']
    score_pairs = [
        ('naipv2', 'NAIPv2'),
        ('naipv1', 'NAIP-v1'),
        ('scijudge_bt', 'SciJudge'),
        ('dgcbert_p', 'DGC-BERT'),
        ('cr8b_rating', 'CR-8B'),
        ('cr70b_rating', 'CR-70B'),
        ('dr7b_rating', 'DR-7B Std'),
        ('dr7bf_rating', 'DR-7B Fast'),
        ('dr14b_rating', 'DR-14B Fast'),
        ('or8b_rating', 'OR-8B'),
        ('seae_rating', 'SEA-E'),
    ]
    decision_kinds = [
        ('dgcbert', 'DGC-BERT'),
        ('cr8b', 'CR-8B'),
        ('cr70b', 'CR-70B'),
        ('dr7b', 'DR-7B Std'),
        ('dr7bf', 'DR-7B Fast'),
        ('dr14b', 'DR-14B Fast'),
        ('or8b', 'OR-8B'),
        ('seae', 'SEA-E'),
    ]
    for i, (fa, la) in enumerate(score_pairs):
        for fb, lb in score_pairs[i + 1:]:
            n, rho = paired_spearman(rows, fa, fb)
            spear_lines.append(f'| {la} | {lb} | {n} | {fmt(rho)} |')
    for i, (ka, la) in enumerate(decision_kinds):
        for kb, lb in decision_kinds[i + 1:]:
            left, right = [], []
            for row in rows:
                a, b = accept_label(row, ka), accept_label(row, kb)
                if a and b:
                    left.append(a)
                    right.append(b)
            f1_lines.append(f'| {la} | {lb} | {len(left)} | {fmt(symmetric_macro_f1(left, right))} |')
    return spear_lines, f1_lines


def paired_spearman(rows: list[dict], fa: str, fb: str) -> tuple[int, float | None]:
    if fa != 'scijudge_bt' and fb != 'scijudge_bt':
        xs, ys = [], []
        for row in rows:
            if row.get(fa) is not None and row.get(fb) is not None:
                xs.append(row[fa])
                ys.append(row[fb])
        return len(xs), spearman(xs, ys)
    by_year: dict[str, tuple[list[float], list[float]]] = defaultdict(lambda: ([], []))
    n = 0
    for row in rows:
        if row.get(fa) is None or row.get(fb) is None:
            continue
        xs, ys = by_year[year_of(row)]
        xs.append(row[fa])
        ys.append(row[fb])
        n += 1
    scores = [value for xs, ys in by_year.values() if (value := spearman(xs, ys)) is not None]
    if not scores:
        return n, None
    return n, mean(scores)


def md_cell(text: str) -> str:
    return (text or '').replace('|', '/').replace('\n', ' ').replace('[', '(').replace(']', ')')


SELF_AGREE_MODELS = (
    ('cyclereviewer-8b', 'CR-8B'),
    ('deepreviewer-14b', 'DR-14B Fast'),
)


def self_agreement_section() -> list[str]:
    rows_out = [
        '## Self-agreement (seed 0 vs seed 1)',
        '',
        '| model | n | Spearman | macro-F1 |',
        '|---|---:|---:|---:|',
    ]
    found = False
    for name, label in SELF_AGREE_MODELS:
        path = ROOT / f'scores_{name}.seed1.jsonl'
        if not path.exists():
            continue
        found = True
        seed0 = {
            row['key']: row
            for row in last_valid_by_key(read_jsonl(ROOT / SCORE_FILES[name]))
            if is_score_row(row)
        }
        seed1 = {
            row['key']: row
            for row in last_valid_by_key(read_jsonl(path))
            if is_score_row(row)
        }
        xs, ys, left, right = [], [], [], []
        for key, row1 in seed1.items():
            row0 = seed0.get(key)
            if not row0:
                continue
            a = as_float(row0.get('rating'))
            b = as_float(row1.get('rating'))
            if a is not None and b is not None:
                xs.append(a)
                ys.append(b)
            d0 = decision_of(row0.get('rating'), row0.get('decision'))
            d1 = decision_of(row1.get('rating'), row1.get('decision'))
            if d0 and d1:
                left.append(d0)
                right.append(d1)
        rows_out.append(
            f'| {label} | {len(xs)} | {fmt(spearman(xs, ys))} | '
            f'{fmt(symmetric_macro_f1(left, right))} |'
        )
    if not found:
        return []
    rows_out.append('')
    return rows_out


def write_report(
    rows: list[dict],
    diag: dict | None = None,
    papers: list[dict] | None = None,
) -> None:
    n = len(rows)
    scored = sum(1 for row in rows if row['n_models'])
    cov = coverage_table(rows)
    spear_lines, f1_lines = agreement(rows)
    by_section: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        by_section[row['section']].append(row)
    lines = [
        '# Paper quality scores',
        '',
        f'{n} readme papers (web/repo skipped). {scored} have at least one Accept/Reject vote.',
        '',
        'Ratings of well-known older papers (Llama 3, DeepSeekMath, DAPO, …) can be inflated: those works appear in Llama-3.1 / Qwen3 / Phi-4 pretraining. Rank **within year** when comparing.',
        '',
        '## Model coverage',
        '',
        '| model | n scored |',
        '|---|---:|',
    ]
    for name, count in cov:
        lines.append(f'| {name} | {count} |')
    n_fast_std, rho_fast_std = paired_spearman(rows, 'dr7bf_rating', 'dr7b_rating')
    left, right = [], []
    for row in rows:
        a, b = accept_label(row, 'dr7bf'), accept_label(row, 'dr7b')
        if a and b:
            left.append(a)
            right.append(b)
    f1_fast_std = symmetric_macro_f1(left, right)
    lines += [
        '',
        '## DeepReviewer-7B Fast vs Standard',
        '',
        f'Intersection n={n_fast_std}. Spearman `{fmt(rho_fast_std)}`. '
        f'Accept/Reject macro-F1 `{fmt(f1_fast_std)}` (n={len(left)}). '
        'Standard is a partial run: it counts in accepts/models, not in mean_rating10.',
    ]
    self_lines = self_agreement_section()
    if self_lines:
        lines += ['', *self_lines]
    if diag:
        lines += [''] + report_lines(diag)
    lines += ['', '## Agreement (Spearman)', '', *spear_lines, '', '## Agreement (macro-F1 Accept/Reject)', '', *f1_lines]
    lines += ['', '## Ranking by readme section', '']
    for section, group in by_section.items():
        ordered = sorted(
            group,
            key=lambda row: (row.get('final_score') is None, -(row.get('final_score') or 0)),
        )
        lines += [
            f'### {section}', '',
            '| rank | title | year | final | accept | key |',
            '|---:|---|---|---:|---:|---|',
        ]
        for index, row in enumerate(ordered, start=1):
            year = year_of(row)
            href = report_anchor(row['key'])
            lines.append(
                f'| {index} | [{md_cell(row["title"])}](#{href}) | {year} | '
                f'{signed(row.get("final_score"))} | {row["accept_votes"]}/{row["n_models"]} | `{row["key"]}` |'
            )
        lines.append('')
    drop_rows = sorted(
        [row for row in rows if row.get('verdict') == 'DROP'],
        key=lambda row: (row.get('final_score') is None, row.get('final_score') or 0),
    )
    watch_rows = sorted(
        [row for row in rows if row.get('verdict') == 'WATCH'],
        key=lambda row: (row.get('final_score') is None, row.get('final_score') or 0),
    )
    lines += [
        '## DROP',
        '',
        '`final_score` < -0.2 with conf >= 0.5 and impact_z below +0.5. '
        'Not a raw accept-vote count.',
        '',
        '| title | section | year | final | conf | impact | accept |',
        '|---|---|---|---:|---:|---:|---:|',
    ]
    for row in drop_rows:
        href = report_anchor(row['key'])
        lines.append(
            f'| [{md_cell(row["title"])}](#{href}) | {md_cell(row["section"])} | {year_of(row)} | '
            f'{signed(row.get("final_score"))} | {fmt(row.get("final_conf"), 2)} | '
            f'{signed(row.get("impact_z"))} | {row["accept_votes"]}/{row["n_models"]} |'
        )
    shown_watch = watch_rows[:40]
    lines += [
        '',
        '## WATCH',
        '',
        'Missing impact_z, conf < 0.5, |final_score| <= 0.2, or low score with high predicted impact.'
        + (f' Showing {len(shown_watch)} of {len(watch_rows)}.' if len(watch_rows) > 40 else ''),
        '',
        '| title | section | year | final | conf | impact | accept |',
        '|---|---|---|---:|---:|---:|---:|',
    ]
    for row in shown_watch:
        href = report_anchor(row['key'])
        lines.append(
            f'| [{md_cell(row["title"])}](#{href}) | {md_cell(row["section"])} | {year_of(row)} | '
            f'{signed(row.get("final_score"))} | {fmt(row.get("final_conf"), 2)} | '
            f'{signed(row.get("impact_z"))} | {row["accept_votes"]}/{row["n_models"]} |'
        )
    lines += ['', '## Per paper', '']
    paper_index = {row['key']: row for row in (papers or load_joined())}
    for row in rows:
        paper = paper_index.get(row['key'], {})
        posts = paper.get('tg_posts') or []
        tg = ', '.join(
            f'[{post.get("channel")}/{post.get("msg_id")}]({post.get("url")})'
            for post in posts[:8] if post.get('url')
        ) or '—'
        weak = weaknesses_for(row['key'], row.get('_weak') or '')
        lines += [
            f'<a id="{report_anchor(row["key"])}"></a>',
            f'### {md_cell(row["title"])}',
            '',
            f'`{row["key"]}` · {md_cell(row["section"])} · {row.get("published") or year_of(row)}',
            '',
            f'- final **{signed(row.get("final_score")) or "n/a"}** (conf {fmt(row.get("final_conf"), 2)}, pct {fmt(row.get("final_pct"), 0)}) · impact {signed(row.get("impact_z")) or "n/a"} · {row.get("verdict") or "—"}'
            + (' · partial fulltext' if row.get('partial') else '')
            + (f' · salvage {row.get("salvage")}' if row.get('salvage') else ''),
            f'- mean rating (1–10): **{fmt(row["mean_rating10"], 1) or "n/a"}** · accept votes **{row["accept_votes"]}/{row["n_models"]}** · percentile rank_avg {fmt(row["rank_avg"], 1)} (100=best) · rank in year {fmt(row["rank_in_year"], 1)} (1=best)',
            f'- NAIPv2 `{fmt(row["naipv2"])}` · NAIP-v1 `{fmt(row["naipv1"])}` · SciJudge `{fmt(row["scijudge_bt"])}` · DGC-BERT `{fmt(row["dgcbert_p"])}`',
            f'- CycleReviewer 8B `{fmt(row["cr8b_rating"], 1)}` {row.get("cr8b_decision") or ""} · 70B `{fmt(row["cr70b_rating"], 1)}` {row.get("cr70b_decision") or ""}',
            f'- DeepReviewer 7B Std `{fmt(row["dr7b_rating"], 1)}` {row.get("dr7b_decision") or ""} · 7B Fast `{fmt(row["dr7bf_rating"], 1)}` {row.get("dr7bf_decision") or ""} (S/P/C {row.get("dr7bf_soundness")}/{row.get("dr7bf_presentation")}/{row.get("dr7bf_contribution")}) · 14B Fast `{fmt(row["dr14b_rating"], 1)}` {row.get("dr14b_decision") or ""}',
            f'- OpenReviewer `{fmt(row["or8b_rating"], 1)}` {row.get("or8b_decision") or ""} (S/P/C {row.get("or8b_soundness")}/{row.get("or8b_presentation")}/{row.get("or8b_contribution")}) · SEA-E `{fmt(row["seae_rating"], 1)}` {row.get("seae_decision") or ""}',
            f'- Telegram: {tg}',
            f'- Weaknesses: {md_cell(weak) or "—"}',
            '',
        ]
    REPORT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')


def main() -> None:
    papers = load_joined()
    model_tables, salvage = load_and_salvage()
    tables = {name: by_key(name) for name in SCORE_FILES}
    tables.update(tables_by_file(model_tables))
    rows = [merge_row(paper, tables) for paper in papers]
    add_ranks(rows)
    agg, diag = aggregate(papers, tables=model_tables, salvage=salvage)
    for row in rows:
        extra = agg.get(row['key']) or {}
        for field in AGG_FIELDS:
            row[field] = extra.get(field)
    write_csv(rows)
    write_report(rows, diag, papers)
    print(f'wrote {SCORES_CSV} ({len(rows)} rows) and {REPORT_MD}', flush=True)


if __name__ == '__main__':
    main()
