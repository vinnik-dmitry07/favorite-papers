'''Hierarchical factor aggregation of reviewer scores into [-1, 1].

    python filter/aggregate.py
    python filter/aggregate.py --no-year-adjust
    python filter/aggregate.py --section-adjust
'''

from __future__ import annotations

import argparse
import importlib.util
import math
import re
import sys
from collections import defaultdict
from pathlib import Path
from statistics import mean

import numpy as np
from scipy.cluster.hierarchy import fcluster, linkage
from scipy.optimize import minimize
from scipy.stats import norm

FILTER_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(FILTER_DIR))

from paths import (  # noqa: E402
    FILTER_DIR as ROOT,
    REVIEWS_DIR,
    SCORE_FILES,
    is_score_row,
    last_valid_by_key,
    load_joined,
    read_jsonl,
    safe_key,
    year_of,
)

_PARSE_SPEC = importlib.util.spec_from_file_location(
    'parse_review', FILTER_DIR / 'remote' / 'parse_review.py',
)
_PARSE_MOD = importlib.util.module_from_spec(_PARSE_SPEC)
assert _PARSE_SPEC.loader is not None
_PARSE_SPEC.loader.exec_module(_PARSE_MOD)
parse_review = _PARSE_MOD.parse_review

FAMILIES = {
    'deep': ('dr7b', 'dr7bf', 'dr14b'),
    'citation': ('naipv1', 'scijudge'),
}
IMPACT_FAMILIES = frozenset({'citation'})
QUALITY_ORDER = ('naipv2', 'deep', 'cr8b', 'or8b', 'seae', 'dgcbert')
SUBSCORE_WEIGHTS = {
    'rating': 0.45,
    'contribution': 0.25,
    'soundness': 0.20,
    'presentation': 0.10,
}
DECISION_NUDGE = 0.15
PARTIAL_MULT = 0.5
YEAR_SHRINK_K = 10.0
CAL_VOTE_RANGE = (0.1, 0.9)
CLUSTER_CUTS = (0.65, 0.75)
WEIGHT_OVERRIDE: dict[str, float] = {}
DROP_BELOW = -0.2
WATCH_ABS = 0.2
MIN_CONF = 0.5
HIGH_IMPACT = 0.5
AGG_FIELDS = (
    'final_score', 'final_conf', 'final_pct', 'impact_z', 'verdict', 'q_hat',
)

MODELS = {
    'naipv2': {
        'file': 'naipv2', 'family': 'naipv2', 'kind': 'abstract',
        'value': 'score', 'year_adjust': True, 'label': 'NAIPv2',
    },
    'naipv1': {
        'file': 'naipv1', 'family': 'citation', 'kind': 'abstract',
        'value': 'score', 'year_adjust': True, 'label': 'NAIP-v1',
    },
    'scijudge': {
        'file': 'scijudge', 'family': 'citation', 'kind': 'abstract',
        'value': 'bt_score', 'year_adjust': False, 'label': 'SciJudge',
    },
    'dgcbert': {
        'file': 'dgcbert', 'family': 'dgcbert', 'kind': 'abstract',
        'value': 'p_accept', 'year_adjust': True, 'label': 'DGC-BERT',
        'has_decision': True,
    },
    'cr8b': {
        'file': 'cyclereviewer-8b', 'family': 'cr8b', 'kind': 'reviewer',
        'parse_kind': 'cycle', 'year_adjust': True, 'label': 'CR-8B',
    },
    'dr7b': {
        'file': 'deepreviewer-7b', 'family': 'deep', 'kind': 'reviewer',
        'parse_kind': 'deep', 'year_adjust': True, 'label': 'DR-7B Std',
    },
    'dr7bf': {
        'file': 'deepreviewer-7b-fast', 'family': 'deep', 'kind': 'reviewer',
        'parse_kind': 'deep', 'year_adjust': True, 'label': 'DR-7B Fast',
    },
    'dr14b': {
        'file': 'deepreviewer-14b', 'family': 'deep', 'kind': 'reviewer',
        'parse_kind': 'deep', 'year_adjust': True, 'label': 'DR-14B Fast',
    },
    'or8b': {
        'file': 'openreviewer-8b', 'family': 'or8b', 'kind': 'reviewer',
        'parse_kind': 'openreviewer', 'year_adjust': True, 'label': 'OR-8B',
    },
    'seae': {
        'file': 'sea-e', 'family': 'seae', 'kind': 'reviewer',
        'parse_kind': 'sea', 'year_adjust': True, 'label': 'SEA-E',
    },
}

FAMILY_LABELS = {
    'naipv2': 'NAIPv2',
    'deep': 'DeepReviewer',
    'cr8b': 'CR-8B',
    'or8b': 'OR-8B',
    'seae': 'SEA-E',
    'dgcbert': 'DGC-BERT',
    'citation': 'citation (impact)',
}


def progress(step: int, total: int, msg: str) -> None:
    print(f'[{step}/{total}] {msg}', flush=True)


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


def year_int(row: dict) -> int | None:
    text = year_of(row)
    if text.isdigit():
        return int(text)
    return None


def year_bucket(year: int | None) -> str:
    if year is None:
        return 'unknown'
    if year <= 2020:
        return '<=2020'
    if year <= 2022:
        return '2021-22'
    return str(year)


def last_by_key(name: str) -> dict[str, dict]:
    return {
        row['key']: row
        for row in last_valid_by_key(read_jsonl(ROOT / SCORE_FILES[name]))
    }


def load_tables() -> dict[str, dict[str, dict]]:
    tables = {}
    for model, spec in MODELS.items():
        tables[model] = last_by_key(spec['file'])
    return tables


def tables_by_file(model_tables: dict[str, dict[str, dict]]) -> dict[str, dict[str, dict]]:
    return {spec['file']: model_tables[model] for model, spec in MODELS.items()}


def load_and_salvage() -> tuple[dict[str, dict[str, dict]], dict[str, int]]:
    tables = load_tables()
    salvage = salvage_unparsed(tables)
    enrich_cycle_reviews(tables)
    return tables, salvage


def usable_row(row: dict | None) -> bool:
    if not row:
        return False
    if row.get('salvage'):
        return True
    if row.get('error'):
        return False
    return is_score_row(row)


CYCLE_OVERLAY = (
    'rating', 'decision', 'soundness', 'presentation', 'contribution',
    'weaknesses', 'n_valid', 'expected_n',
)
SUB_FIELDS = ('soundness', 'presentation', 'contribution')


def has_sub_scores(parsed: dict) -> bool:
    return any(parsed.get(field) is not None for field in SUB_FIELDS)


def recover_unparsed_row(row: dict, parsed: dict) -> tuple[dict, str] | None:
    '''Promote a full rating to a normal row; S/P/C-only stays salvage.'''
    if parsed.get('rating') is not None:
        copy = dict(row)
        for field in CYCLE_OVERLAY:
            if field in parsed:
                copy[field] = parsed[field]
        copy.pop('error', None)
        copy.pop('salvage', None)
        return copy, 'full'
    if not has_sub_scores(parsed):
        return None
    copy = dict(row)
    for field in SUB_FIELDS:
        if parsed.get(field) is not None:
            copy[field] = parsed[field]
    copy['salvage'] = True
    copy.pop('error', None)
    return copy, 'salvage'


def apply_cycle_overlay(row: dict, parsed: dict) -> dict:
    '''Authoritative Cycle parse: None clears stale jsonl fields.'''
    copy = dict(row)
    for field in CYCLE_OVERLAY:
        copy[field] = parsed.get(field)
    copy.pop('error', None)
    if parsed.get('rating') is not None:
        copy.pop('salvage', None)
    return copy


def salvage_unparsed(tables: dict[str, dict[str, dict]]) -> dict[str, int]:
    counts = {}
    for model, spec in MODELS.items():
        if spec['kind'] != 'reviewer':
            continue
        n_salvage = 0
        review_dir = REVIEWS_DIR / spec['file']
        for key, row in tables[model].items():
            if row.get('salvage'):
                continue
            error = str(row.get('error') or '')
            if not error.startswith('unparsed'):
                continue
            path = review_dir / f'{safe_key(key)}.md'
            if not path.exists():
                continue
            raw = path.read_text(encoding='utf-8', errors='replace')
            parsed = parse_review(raw, kind=spec.get('parse_kind') or '')
            recovered = recover_unparsed_row(row, parsed)
            if recovered is None:
                continue
            copy, kind = recovered
            tables[model][key] = copy
            if kind == 'salvage':
                n_salvage += 1
        counts[model] = n_salvage
    return counts


def enrich_cycle_reviews(tables: dict[str, dict[str, dict]]) -> int:
    '''Re-parse CycleReviewer markdown in memory. Does not rewrite jsonl.'''
    n_done = 0
    for model, spec in MODELS.items():
        if spec.get('parse_kind') != 'cycle':
            continue
        review_dir = REVIEWS_DIR / spec['file']
        items = list(tables[model].items())
        total = len(items)
        for index, (key, row) in enumerate(items, 1):
            if index == 1 or index == total or index % 50 == 0:
                print(
                    f'  enrich {spec["file"]}: {index}/{total}',
                    flush=True,
                )
            path = review_dir / f'{safe_key(key)}.md'
            if not path.exists():
                continue
            raw = path.read_text(encoding='utf-8', errors='replace')
            parsed = parse_review(raw, kind='cycle')
            if parsed.get('rating') is None and not has_sub_scores(parsed):
                continue
            tables[model][key] = apply_cycle_overlay(row, parsed)
            n_done += 1
    print(f'  enrich cycle reviews: {n_done} rows', flush=True)
    return n_done


def rank_normal(values: dict[str, float]) -> dict[str, float]:
    if not values:
        return {}
    items = sorted(values.items(), key=lambda item: (item[1], item[0]))
    n = len(items)
    ranks: dict[str, float] = {}
    index = 0
    while index < n:
        end = index
        while end + 1 < n and items[end + 1][1] == items[index][1]:
            end += 1
        avg = (index + end + 2) / 2
        for pos in range(index, end + 1):
            ranks[items[pos][0]] = avg
        index = end + 1
    return {key: float(norm.ppf(rank / (n + 1))) for key, rank in ranks.items()}


def group_adjust(
    zs: dict[str, float],
    group_of: dict[str, str],
    shrink_k: float = YEAR_SHRINK_K,
) -> dict[str, float]:
    buckets: dict[str, list[float]] = defaultdict(list)
    for key, value in zs.items():
        buckets[group_of.get(key, 'unknown')].append(value)
    offset = {}
    for name, nums in buckets.items():
        raw = mean(nums)
        offset[name] = (len(nums) / (len(nums) + shrink_k)) * raw
    return {key: value - offset[group_of.get(key, 'unknown')] for key, value in zs.items()}


def standardize(
    values: dict[str, float],
    refs: dict[str, float] | None = None,
) -> dict[str, float]:
    source = refs if refs is not None and len(refs) >= 8 else values
    if len(source) < 2:
        return {key: 0.0 for key in values}
    nums = list(source.values())
    mu = mean(nums)
    var = sum((x - mu) ** 2 for x in nums) / (len(nums) - 1)
    if var <= 1e-12:
        return {key: 0.0 for key in values}
    scale = math.sqrt(var)
    return {key: (value - mu) / scale for key, value in values.items()}


def midranks(values: list[float]) -> list[float]:
    items = list(enumerate(values))
    items.sort(key=lambda item: (item[1], item[0]))
    ranks = [0.0] * len(values)
    index = 0
    n = len(items)
    while index < n:
        end = index
        while end + 1 < n and items[end + 1][1] == items[index][1]:
            end += 1
        avg = (index + end + 2) / 2
        for pos in range(index, end + 1):
            ranks[items[pos][0]] = avg
        index = end + 1
    return ranks


def spearman(xs: list[float], ys: list[float]) -> float | None:
    n = len(xs)
    if n < 3:
        return None
    return _pearson(midranks(xs), midranks(ys))


def _pearson(xs: list[float], ys: list[float]) -> float | None:
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


def paired_rho(
    left: dict[str, float],
    right: dict[str, float],
) -> tuple[int, float | None]:
    keys = [key for key in left if key in right]
    if len(keys) < 3:
        return len(keys), None
    return len(keys), spearman([left[k] for k in keys], [right[k] for k in keys])


def explicit_decision_pm(row: dict, spec: dict) -> float | None:
    if spec.get('has_decision'):
        value = as_float(row.get('p_accept'))
        if value is None:
            return None
        return 1.0 if value >= 0.5 else -1.0
    text = str(row.get('decision') or '')
    if re.search(r'\breject\b', text, re.I):
        return -1.0
    if re.search(r'\baccept\b', text, re.I):
        return 1.0
    return None


def decision_pm(row: dict, spec: dict) -> float | None:
    explicit = explicit_decision_pm(row, spec)
    if explicit is not None:
        return explicit
    rating = as_float(row.get('rating'))
    if rating is None:
        return None
    return 1.0 if rating >= 6 else -1.0


def field_zscores(
    tables: dict[str, dict[str, dict]],
    papers: dict[str, dict],
    year_adjust: bool,
    section_adjust: bool,
) -> dict[str, dict[str, dict[str, float]]]:
    year_of_key = {key: year_bucket(year_int(row)) for key, row in papers.items()}
    calendar_year = {key: year_of(row) or 'unknown' for key, row in papers.items()}
    section_of_key = {key: row.get('section') or 'unknown' for key, row in papers.items()}
    out: dict[str, dict[str, dict[str, float]]] = {}
    for model, spec in MODELS.items():
        fields = ['rating', 'contribution', 'soundness', 'presentation']
        if spec['kind'] == 'abstract':
            fields = [spec['value']]
        z_fields: dict[str, dict[str, float]] = {}
        for field in fields:
            raw = {}
            for key, row in tables[model].items():
                if key not in papers or not usable_row(row):
                    continue
                if row.get('salvage') and field == 'rating':
                    continue
                value = as_float(row.get(field))
                if value is not None:
                    raw[key] = value
            if spec.get('year_adjust', True):
                zs = rank_normal(raw)
                if year_adjust:
                    zs = group_adjust(zs, year_of_key)
            else:
                by_year: dict[str, dict[str, float]] = defaultdict(dict)
                for key, value in raw.items():
                    by_year[calendar_year.get(key, 'unknown')][key] = value
                zs = {}
                for group in by_year.values():
                    zs.update(rank_normal(group))
            if section_adjust:
                zs = group_adjust(zs, section_of_key)
            z_fields[field] = zs
        out[model] = z_fields
    return out


def model_composites(
    tables: dict[str, dict[str, dict]],
    z_fields: dict[str, dict[str, dict[str, float]]],
    papers: dict[str, dict],
) -> tuple[dict[str, dict[str, float]], dict[str, dict[str, float]]]:
    composites: dict[str, dict[str, float]] = {}
    weights: dict[str, dict[str, float]] = {}
    for model, spec in MODELS.items():
        raw: dict[str, float] = {}
        wts: dict[str, float] = {}
        for key in papers:
            row = tables[model].get(key)
            if not usable_row(row):
                continue
            salvage = bool(row.get('salvage'))
            if spec['kind'] == 'abstract':
                value = z_fields[model].get(spec['value'], {}).get(key)
                if value is None:
                    continue
                raw[key] = value
            else:
                num = 0.0
                used_w = 0.0
                for field, weight in SUBSCORE_WEIGHTS.items():
                    if salvage and field == 'rating':
                        continue
                    z = z_fields[model].get(field, {}).get(key)
                    if z is None:
                        continue
                    num += weight * z
                    used_w += weight
                if used_w:
                    total = num / used_w
                    used = True
                else:
                    total = 0.0
                    used = False
                if not salvage:
                    explicit = explicit_decision_pm(row, spec)
                    rating = as_float(row.get('rating'))
                    if explicit is not None and rating is not None:
                        implied = 1.0 if rating >= 6 else -1.0
                        if explicit != implied:
                            total += DECISION_NUDGE * explicit
                    elif explicit is not None:
                        total += DECISION_NUDGE * explicit
                        used = True
                if not used:
                    continue
                raw[key] = total
            weight = PARTIAL_MULT if (row.get('partial') or salvage) else 1.0
            n_valid = as_float(row.get('n_valid'))
            expected_n = as_float(row.get('expected_n'))
            if n_valid is not None and expected_n and expected_n > 0:
                weight *= min(1.0, n_valid / expected_n)
            wts[key] = weight
        composites[model] = standardize(raw)
        weights[model] = wts
    return composites, weights


def family_members() -> dict[str, list[str]]:
    grouped: dict[str, list[str]] = defaultdict(list)
    for model, spec in MODELS.items():
        grouped[spec['family']].append(model)
    return dict(grouped)


def mean_map(dicts: list[dict[str, float]]) -> dict[str, float]:
    bag: dict[str, list[float]] = defaultdict(list)
    for mapping in dicts:
        for key, value in mapping.items():
            bag[key].append(value)
    return {key: mean(vals) for key, vals in bag.items()}


def lofo_against_families(
    target: dict[str, float],
    family_zs: dict[str, dict[str, float]],
    skip: str,
) -> float | None:
    others = [zs for name, zs in family_zs.items() if name != skip and zs]
    if not others:
        return None
    consensus = mean_map(others)
    _n, rho = paired_rho(target, consensus)
    return rho


def family_composites(
    model_z: dict[str, dict[str, float]],
    model_w: dict[str, dict[str, float]],
) -> tuple[dict[str, dict[str, float]], dict[str, dict[str, float]]]:
    members = family_members()
    quality_temp = {
        family: standardize(mean_map([model_z[m] for m in models if model_z[m]]))
        for family, models in members.items()
        if family not in IMPACT_FAMILIES
    }
    lofo: dict[str, float | None] = {}
    for model, spec in MODELS.items():
        family = spec['family']
        if family in IMPACT_FAMILIES:
            siblings = [
                model_z[other]
                for other in members[family]
                if other != model and model_z.get(other)
            ]
            if siblings:
                _n, rho = paired_rho(model_z[model], mean_map(siblings))
                lofo[model] = rho
            else:
                lofo[model] = 0.01
        else:
            lofo[model] = lofo_against_families(
                model_z[model], quality_temp, family,
            )
    family_z: dict[str, dict[str, float]] = {}
    family_cov: dict[str, dict[str, float]] = {}
    for family, models in members.items():
        rel = {}
        for model in models:
            rho = lofo[model]
            rel[model] = 0.01 if rho is None else max(float(rho), 0.01)
        expected = sum(rel.values())
        bag: dict[str, list[tuple[float, float]]] = defaultdict(list)
        for model in models:
            for key, value in model_z[model].items():
                weight = rel[model] * model_w[model].get(key, 1.0)
                bag[key].append((value, weight))
        raw = {}
        cov = {}
        for key, pairs in bag.items():
            num = sum(value * weight for value, weight in pairs)
            available = sum(weight for _value, weight in pairs)
            if available <= 0:
                continue
            raw[key] = num / available
            cov[key] = min(1.0, available / expected) if expected else 1.0
        covered = [set(model_z[model]) for model in models if model_z.get(model)]
        full_keys = set.intersection(*covered) if covered else set()
        refs = {key: raw[key] for key in full_keys if key in raw}
        family_z[family] = standardize(raw, refs)
        family_cov[family] = cov
    return family_z, {'model_lofo': lofo, 'family_cov': family_cov}


def corr_matrix(series: dict[str, dict[str, float]], names: list[str]) -> np.ndarray:
    n = len(names)
    mat = np.eye(n)
    for i, a in enumerate(names):
        for j, b in enumerate(names):
            if j <= i:
                continue
            _overlap, rho = paired_rho(series[a], series[b])
            mat[i, j] = mat[j, i] = 0.0 if rho is None else float(rho)
    return mat


def paf_loadings(corr: np.ndarray) -> np.ndarray:
    n = corr.shape[0]
    if n == 0:
        return np.array([])
    h2 = np.array([
        max((abs(corr[i, j]) for j in range(n) if j != i), default=0.0)
        for i in range(n)
    ])
    loadings = np.zeros(n)
    for _ in range(80):
        starred = corr.copy()
        np.fill_diagonal(starred, h2)
        evals, evecs = np.linalg.eigh(starred)
        idx = int(np.argmax(evals))
        ev = max(float(evals[idx]), 0.0)
        vec = evecs[:, idx]
        if vec.sum() < 0:
            vec = -vec
        loadings = vec * math.sqrt(ev)
        new_h2 = np.clip(loadings ** 2, 0.0, 0.99)
        if np.max(np.abs(new_h2 - h2)) < 1e-7:
            break
        h2 = new_h2
    if float(np.max(np.abs(loadings))) < 1e-9:
        print('[warn] PAF collapsed to zero loadings; using equal weights', flush=True)
        loadings = np.full(n, 0.4)
    return loadings


def pc1_loadings(corr: np.ndarray) -> np.ndarray:
    if corr.size == 0:
        return np.array([])
    evals, evecs = np.linalg.eigh(corr)
    idx = int(np.argmax(evals))
    vec = evecs[:, idx]
    if vec.sum() < 0:
        vec = -vec
    return vec * math.sqrt(max(float(evals[idx]), 0.0))


def reliability_weight(lam: float) -> float:
    # intentional reliability weighting; NOT Gaussian one-factor posterior
    clipped = min(max(abs(lam), 0.05), 0.95)
    return (clipped ** 2) / (1.0 - clipped ** 2)


def reliability_q(zs: list[float], lams: list[float]) -> float:
    '''q = Σ w z / (1 + Σ w) with w = λ² / (1 − λ²).'''
    num = 0.0
    w_present = 0.0
    for z, lam in zip(zs, lams):
        w = reliability_weight(lam)
        sign = 1.0 if lam >= 0 else -1.0
        num += w * sign * z
        w_present += w
    return num / (1.0 + w_present)


def family_weights(
    lambdas: dict[str, float],
) -> tuple[dict[str, float], dict[str, float]]:
    weights = {}
    signs = {}
    for name, lam in lambdas.items():
        if name in WEIGHT_OVERRIDE:
            raw = WEIGHT_OVERRIDE[name]
            weights[name] = abs(raw)
            signs[name] = 1.0 if raw >= 0 else -1.0
            continue
        weights[name] = reliability_weight(lam)
        signs[name] = 1.0 if lam >= 0 else -1.0
    return weights, signs


def posterior(
    family_z: dict[str, dict[str, float]],
    family_cov: dict[str, dict[str, float]],
    weights: dict[str, float],
    signs: dict[str, float],
    keys: list[str],
    families: list[str],
) -> tuple[dict[str, float], dict[str, float]]:
    q_hat, conf = {}, {}
    w_full = sum(weights.get(family, 0.0) for family in families)
    for key in keys:
        num = 0.0
        w_present = 0.0
        w_used = 0.0
        for family in families:
            z = family_z.get(family, {}).get(key)
            if z is None:
                continue
            sign = signs.get(family, 1.0)
            w = weights[family]
            num += w * sign * z
            w_present += w
            coverage = family_cov.get(family, {}).get(key, 1.0)
            w_used += w * coverage
        if w_present <= 0:
            q_hat[key] = 0.0
            conf[key] = 0.0
        else:
            q_hat[key] = num / (1.0 + w_present)
            conf[key] = min(1.0, w_used / w_full) if w_full else 0.0
    return q_hat, conf


def vote_pm(row: dict | None, spec: dict) -> float | None:
    if not usable_row(row) or row.get('salvage'):
        return None
    if spec['kind'] == 'abstract' and not spec.get('has_decision'):
        return None
    return decision_pm(row, spec)


def family_paper_vote(
    tables: dict[str, dict[str, dict]],
    models: list[str],
    key: str,
) -> float | None:
    votes = []
    for model in models:
        pm = vote_pm(tables[model].get(key), MODELS[model])
        if pm is not None:
            votes.append(1.0 if pm > 0 else 0.0)
    return mean(votes) if votes else None


def family_vote_rates(
    tables: dict[str, dict[str, dict]],
    keys: list[str],
) -> dict[str, float | None]:
    members = family_members()
    rates = {}
    for family, models in members.items():
        if family in IMPACT_FAMILIES:
            continue
        votes = [
            vote for key in keys
            if (vote := family_paper_vote(tables, models, key)) is not None
        ]
        rates[family] = mean(votes) if votes else None
    return rates


def accept_share(
    tables: dict[str, dict[str, dict]],
    keys: list[str],
    allowed: set[str],
) -> dict[str, float | None]:
    members = family_members()
    shares = {}
    for key in keys:
        num = 0.0
        den = 0.0
        for family, models in members.items():
            if family in IMPACT_FAMILIES or family not in allowed:
                continue
            vote = family_paper_vote(tables, models, key)
            if vote is None:
                continue
            num += vote
            den += 1.0
        shares[key] = (num / den) if den else None
    return shares


def sigmoid(x: float) -> float:
    if x >= 40:
        return 1.0
    if x <= -40:
        return 0.0
    return 1.0 / (1.0 + math.exp(-x))


def calibrate(
    q_hat: dict[str, float],
    conf: dict[str, float],
    shares: dict[str, float | None],
) -> tuple[float, float]:
    keys = [key for key, share in shares.items() if share is not None]
    if len(keys) < 8:
        return 1.0, 0.0

    def loss(params) -> float:
        a, b = params
        total = 0.0
        wsum = 0.0
        for key in keys:
            pred = min(max(sigmoid(a * q_hat[key] + b), 1e-6), 1 - 1e-6)
            target = shares[key]
            weight = max(conf.get(key, 0.0), 0.05)
            total += weight * (
                -target * math.log(pred) - (1 - target) * math.log(1 - pred)
            )
            wsum += weight
        return total / wsum if wsum else 0.0

    result = minimize(
        loss,
        x0=np.array([1.2, 0.0]),
        method='L-BFGS-B',
        bounds=((1e-3, 20.0), (-5.0, 5.0)),
    )
    if not result.success:
        print(f'[warn] calibration did not converge: {result.message}', flush=True)
    a, b = (float(x) for x in result.x)
    if not (math.isfinite(a) and math.isfinite(b)):
        print('[warn] calibration produced non-finite parameters; using a=1 b=0', flush=True)
        return 1.0, 0.0
    return a, b


def percentile_of(values: dict[str, float]) -> dict[str, float]:
    if not values:
        return {}
    items = sorted(values.items(), key=lambda item: (item[1], item[0]))
    n = len(items)
    out = {}
    index = 0
    while index < n:
        end = index
        while end + 1 < n and items[end + 1][1] == items[index][1]:
            end += 1
        avg = (index + end) / 2
        pct = 100.0 * avg / (n - 1) if n > 1 else 50.0
        for pos in range(index, end + 1):
            out[items[pos][0]] = pct
        index = end + 1
    return out


def verdict_of(score: float | None, conf: float, impact: float | None) -> str:
    if score is None or conf < MIN_CONF or impact is None:
        return 'WATCH'
    if abs(score) <= WATCH_ABS:
        return 'WATCH'
    if score < DROP_BELOW:
        if impact >= HIGH_IMPACT:
            return 'WATCH'
        return 'DROP'
    return 'KEEP'


def cluster_labels(corr: np.ndarray, names: list[str], cut: float) -> list[str]:
    if len(names) < 2:
        return names
    dist = np.clip(1.0 - corr, 0.0, 2.0)
    condensed = dist[np.triu_indices(len(names), k=1)]
    if np.allclose(condensed, 0):
        return ['+'.join(names)]
    z = linkage(condensed, method='average')
    labels = fcluster(z, t=cut, criterion='distance')
    groups: dict[int, list[str]] = defaultdict(list)
    for name, lab in zip(names, labels):
        groups[int(lab)].append(name)
    return ['+'.join(sorted(group)) for group in groups.values()]


def subscore_table(
    z_fields: dict[str, dict[str, dict[str, float]]],
    family_z: dict[str, dict[str, float]],
) -> list[tuple[str, str, int, float | None]]:
    rows = []
    quality = {name: zs for name, zs in family_z.items() if name not in IMPACT_FAMILIES}
    for model, spec in MODELS.items():
        if spec['kind'] != 'reviewer':
            continue
        for field in ('rating', 'contribution', 'soundness', 'presentation'):
            zs = z_fields[model].get(field, {})
            rho = lofo_against_families(zs, quality, spec['family'])
            n = len(zs)
            rows.append((spec['label'], field, n, rho))
    return rows


def unparsed_bias(
    tables: dict[str, dict[str, dict]],
    family_z: dict[str, dict[str, float]],
    papers: dict[str, dict],
) -> list[tuple[str, str, int, float | None]]:
    quality = {name: zs for name, zs in family_z.items() if name not in IMPACT_FAMILIES}
    consensus = mean_map(list(quality.values()))
    rows = []
    for model, spec in MODELS.items():
        if spec['kind'] != 'reviewer':
            continue
        parsed, unparsed, salvaged = [], [], []
        for key in papers:
            row = tables[model].get(key) or {}
            z = consensus.get(key)
            if z is None:
                continue
            error = str(row.get('error') or '')
            if row.get('salvage'):
                salvaged.append(z)
            elif error.startswith('unparsed'):
                unparsed.append(z)
            elif as_float(row.get('rating')) is not None:
                parsed.append(z)
        for kind, nums in (
            ('parsed', parsed),
            ('salvage', salvaged),
            ('unparsed', unparsed),
        ):
            rows.append((
                spec['label'],
                kind,
                len(nums),
                mean(nums) if nums else None,
            ))
    return rows


def fmt(value, digits: int = 3) -> str:
    if value is None:
        return ''
    if isinstance(value, float):
        return f'{value:.{digits}f}'
    return str(value)


def diagnostics_tables(
    lambdas: dict[str, float],
    weights: dict[str, float],
    model_lofo: dict[str, float | None],
    pc1: dict[str, float],
    corr: np.ndarray,
    names: list[str],
    salvage: dict[str, int],
    sub_rows,
    bias_rows,
    a: float,
    b: float,
    pos_share: float,
    verdicts: dict[str, int],
    model_corr: np.ndarray,
    model_names: list[str],
) -> dict:
    return {
        'lambdas': lambdas,
        'weights': weights,
        'model_lofo': model_lofo,
        'pc1': pc1,
        'corr': corr,
        'corr_names': names,
        'clusters_035': cluster_labels(corr, names, CLUSTER_CUTS[0]),
        'clusters_025': cluster_labels(corr, names, CLUSTER_CUTS[1]),
        'model_clusters_035': cluster_labels(model_corr, model_names, CLUSTER_CUTS[0]),
        'model_clusters_025': cluster_labels(model_corr, model_names, CLUSTER_CUTS[1]),
        'salvage': salvage,
        'subscores': sub_rows,
        'unparsed_bias': bias_rows,
        'calibrate_a': a,
        'calibrate_b': b,
        'pos_share': pos_share,
        'verdicts': verdicts,
    }


def unparsed_note(bias_rows) -> str:
    bits = []
    for label, kind, n, value in bias_rows:
        if kind != 'unparsed' or not n:
            continue
        bits.append(f'{label} n={n}, consensus z={fmt(value)}')
    if not bits:
        return ''
    return (
        'Remaining unparsed reviews after retry are shifted down '
        f'({"; ".join(bits)}). No reject-imputation; those papers already '
        'get signal from other families.'
    )


def aggregate(
    papers: list[dict] | None = None,
    *,
    tables: dict[str, dict[str, dict]] | None = None,
    salvage: dict[str, int] | None = None,
    year_adjust: bool = True,
    section_adjust: bool = False,
) -> tuple[dict[str, dict], dict]:
    paper_rows = papers or load_joined()
    paper_index = {row['key']: row for row in paper_rows}
    keys = [row['key'] for row in paper_rows]
    if tables is None:
        progress(1, 7, f'load {len(keys)} papers')
        tables = load_tables()
        progress(2, 7, 'salvage unparsed S/P/C + cycle reviews')
        salvage = salvage_unparsed(tables)
        enrich_cycle_reviews(tables)
    else:
        progress(1, 7, f'reuse {len(keys)} papers / tables')
        progress(2, 7, f'salvage counts {salvage or {}}')
        salvage = salvage or {}
    progress(3, 7, 'rank-normal z + year/section adjust')
    z_fields = field_zscores(tables, paper_index, year_adjust, section_adjust)
    progress(4, 7, 'model and family composites')
    model_z, model_w = model_composites(tables, z_fields, paper_index)
    family_z, extra = family_composites(model_z, model_w)
    quality_names = [name for name in QUALITY_ORDER if family_z.get(name)]
    model_names = [name for name, zs in model_z.items() if zs]
    model_corr = corr_matrix(model_z, model_names)
    progress(5, 7, f'PAF on {len(quality_names)} quality families')
    if not quality_names:
        print('[warn] no quality families; scores are None / WATCH', flush=True)
        empty = {key: 0.0 for key in keys}
        q_hat, conf = empty, empty
        lambdas, weights, pc1 = {}, {}, {}
        corr = np.eye(0)
        impact = family_z.get('citation', {})
        a, b = 1.0, 0.0
        rates = family_vote_rates(tables, keys)
        allowed: set[str] = set()
        progress(6, 7, 'skip calibrate (no quality families)')
    else:
        corr = corr_matrix(family_z, quality_names)
        paf = paf_loadings(corr)
        pca = pc1_loadings(corr)
        lambdas = {name: float(paf[i]) for i, name in enumerate(quality_names)}
        pc1 = {name: float(pca[i]) for i, name in enumerate(quality_names)}
        weights, signs = family_weights(lambdas)
        q_hat, conf = posterior(
            family_z, extra['family_cov'], weights, signs, keys, quality_names,
        )
        impact = family_z.get('citation', {})
        progress(6, 7, 'calibrate accept threshold')
        rates = family_vote_rates(tables, keys)
        allowed = {
            family for family, rate in rates.items()
            if rate is not None and CAL_VOTE_RANGE[0] < rate < CAL_VOTE_RANGE[1]
        }
        if not allowed:
            allowed = {family for family, rate in rates.items() if rate is not None}
            print('[warn] CAL_VOTE_RANGE excluded every family; using all', flush=True)
        shares = accept_share(tables, keys, allowed)
        a, b = calibrate(q_hat, conf, shares)
    pct = percentile_of(q_hat)
    rows = {}
    verdicts: dict[str, int] = defaultdict(int)
    for key in keys:
        impact_z = impact.get(key)
        if conf[key] <= 0:
            score = None
            verdict = 'WATCH'
        else:
            score = 2.0 * sigmoid(a * q_hat[key] + b) - 1.0
            verdict = verdict_of(score, conf[key], impact_z)
        verdicts[verdict] += 1
        rows[key] = {
            'final_score': score,
            'final_conf': conf[key],
            'final_pct': pct.get(key),
            'impact_z': impact_z,
            'verdict': verdict,
            'q_hat': q_hat[key],
        }
    scored = [row['final_score'] for row in rows.values() if row['final_score'] is not None]
    pos_share = sum(1 for value in scored if value > 0) / max(len(scored), 1)
    progress(7, 7, 'diagnostics')
    sub_rows = subscore_table(z_fields, family_z)
    bias_rows = unparsed_bias(tables, family_z, paper_index)
    diag = diagnostics_tables(
        lambdas, weights, extra['model_lofo'], pc1, corr, quality_names,
        salvage, sub_rows, bias_rows, a, b, pos_share, dict(verdicts),
        model_corr, model_names,
    )
    diag['family_z'] = family_z
    diag['model_z'] = model_z
    diag['cal_families'] = sorted(allowed)
    diag['family_accept'] = rates
    diag['unparsed_note'] = unparsed_note(bias_rows)
    return rows, diag


def print_report(diag: dict) -> None:
    print('', flush=True)
    print('family  lambda   w      PC1    LOFO(models)', flush=True)
    for name in diag['corr_names']:
        models = FAMILIES.get(name) or (name,)
        lofos = ', '.join(
            f'{MODELS[m]["label"]}={fmt(diag["model_lofo"].get(m))}'
            for m in models if m in MODELS
        )
        print(
            f'{FAMILY_LABELS.get(name, name):16} {fmt(diag["lambdas"].get(name), 3):>6} '
            f'{fmt(diag["weights"].get(name), 3):>6} {fmt(diag["pc1"].get(name), 3):>6}  {lofos}',
            flush=True,
        )
    print(f'family clusters rho>=0.35: {diag["clusters_035"]}', flush=True)
    print(f'family clusters rho>=0.25: {diag["clusters_025"]}', flush=True)
    print(f'model clusters rho>=0.35: {diag["model_clusters_035"]}', flush=True)
    print(f'model clusters rho>=0.25: {diag["model_clusters_025"]}', flush=True)
    print(f'cal families: {diag.get("cal_families")} accept={diag.get("family_accept")}', flush=True)
    print(f'salvage: {diag["salvage"]}', flush=True)
    print(
        f'calibrate a={fmt(diag["calibrate_a"])} b={fmt(diag["calibrate_b"])} '
        f'share>0={fmt(diag["pos_share"])}',
        flush=True,
    )
    print(f'verdicts: {diag["verdicts"]}', flush=True)
    note = diag.get('unparsed_note') or ''
    if note:
        print(note, flush=True)
    print('sub-score LOFO vs other families', flush=True)
    for label, field, n, rho in diag['subscores']:
        print(f'  {label:14} {field:13} n={n:3} rho={fmt(rho)}', flush=True)
    print('unparsed bias (mean consensus z)', flush=True)
    for label, kind, n, value in diag['unparsed_bias']:
        print(f'  {label:14} {kind:9} n={n:3} z={fmt(value)}', flush=True)


def report_lines(diag: dict) -> list[str]:
    lines = [
        '## Aggregation',
        '',
        'Hierarchical factor score on quality families (citation/impact held out). '
        '`final_score` is in [-1, 1]. 0 is where reviewer Accept/Reject votes '
        f'split 50/50 among families whose accept rate is in {CAL_VOTE_RANGE} '
        f'(now `{diag.get("cal_families")}`). `accepts/models` on badges are raw '
        'reviewer votes, not this score. '
        f'VERDICT: DROP if score < {DROP_BELOW} and conf >= {MIN_CONF} and '
        f'impact_z < {HIGH_IMPACT}; WATCH if missing impact, conf < {MIN_CONF}, '
        f'|score| <= {WATCH_ABS}, or score < {DROP_BELOW} with impact_z >= {HIGH_IMPACT}; '
        'else KEEP. `final_conf` is coverage `Σ w_used / Σ w_full` '
        '(no prior +1). A present family keeps mass 1.0 in q; missingness '
        'only lowers coverage.',
        '',
        f'Calibration `sigmoid({fmt(diag["calibrate_a"])} q + {fmt(diag["calibrate_b"])})`; '
        f'share of papers with final_score > 0: `{fmt(diag["pos_share"])}`. '
        f'VERDICT KEEP/WATCH/DROP = `{diag["verdicts"]}`.',
        '',
        'Family accept rates used for `CAL_VOTE_RANGE`: '
        + ', '.join(
            f'{FAMILY_LABELS.get(name, name)} {fmt(rate)}'
            for name, rate in sorted((diag.get('family_accept') or {}).items())
            if rate is not None
        )
        + f'. In target: `{diag.get("cal_families")}`.',
        '',
        '| family | λ | w | PC1 |',
        '|---|---:|---:|---:|',
    ]
    for name in diag['corr_names']:
        lines.append(
            f'| {FAMILY_LABELS.get(name, name)} | {fmt(diag["lambdas"].get(name))} | '
            f'{fmt(diag["weights"].get(name))} | {fmt(diag["pc1"].get(name))} |'
        )
    lines += [
        '',
        '| model | LOFO | vs | salvage |',
        '|---|---:|---|---:|',
    ]
    for model, spec in MODELS.items():
        vs = 'sibling' if spec['family'] in IMPACT_FAMILIES else 'other families'
        lines.append(
            f'| {spec["label"]} | {fmt(diag["model_lofo"].get(model))} | {vs} | '
            f'{diag["salvage"].get(model, 0)} |'
        )
    lines += [
        '',
        f'Family clusters at rho>=0.35: {", ".join(diag["clusters_035"]) or "-"}. '
        f'At rho>=0.25: {", ".join(diag["clusters_025"]) or "-"}. '
        f'Model clusters at rho>=0.35: {", ".join(diag["model_clusters_035"]) or "-"}. '
        f'At rho>=0.25: {", ".join(diag["model_clusters_025"]) or "-"}.',
        '',
        '| model | field | n | rho vs other families |',
        '|---|---|---:|---:|',
    ]
    for label, field, n, rho in diag['subscores']:
        lines.append(f'| {label} | {field} | {n} | {fmt(rho)} |')
    lines += [
        '',
        '| model | subset | n | mean consensus z |',
        '|---|---|---:|---:|',
    ]
    for label, kind, n, value in diag['unparsed_bias']:
        lines.append(f'| {label} | {kind} | {n} | {fmt(value)} |')
    note = diag.get('unparsed_note') or ''
    if note:
        lines += ['', note]
    lines.append('')
    return lines


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--no-year-adjust', action='store_true')
    parser.add_argument('--section-adjust', action='store_true')
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rows, diag = aggregate(
        year_adjust=not args.no_year_adjust,
        section_adjust=args.section_adjust,
    )
    print_report(diag)
    by_v = defaultdict(list)
    for key, row in rows.items():
        by_v[row['verdict']].append((row['final_score'], key))
    for verdict in ('DROP', 'WATCH', 'KEEP'):
        items = sorted(
            by_v[verdict],
            key=lambda item: (item[0] is None, item[0] if item[0] is not None else 0),
        )
        print(f'{verdict}: {len(items)}', flush=True)
        for score, key in items[:8]:
            shown = 'n/a' if score is None else f'{score:+.3f}'
            print(f'  {shown} {key}', flush=True)


if __name__ == '__main__':
    main()
