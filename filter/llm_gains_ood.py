'''Temporal OOD classifier and paper-specific gain overrides.

A rendered markdown cell requires ood_basis=temporal: the bench date is after
the full training-chain cutoff (student + teacher + train data). Inventory
eval_ood is not enough. Historical benches never auto-qualify.
'''

from __future__ import annotations

from datetime import date

CONSPO = 'arxiv:2605.12969'
WEIGHT_GEO = 'arxiv:2606.23740'
ESPO = 'arxiv:2512.00499'
DFT = 'arxiv:2508.05629'
MIDTRAIN = 'arxiv:2601.21343'
HICRA = 'arxiv:2509.03646'
ONESHOT = 'arxiv:2504.20571'
OPRD_PAPER = 'arxiv:2606.06021'
REVISIT_OPD = 'arxiv:2603.25562'

OOD_BASES = ('temporal', 'rl_stage', 'id', 'unverified')
CKPT_SELECT = (
    'final',
    'last',
    'best-every-100',
    'validation-avg',
    'mixed-avg-and-per-bench',
    'per-bench-best',
    'unspecified',
)
EVAL_CKPT = frozenset({
    'best-every-100',
    'validation-avg',
    'mixed-avg-and-per-bench',
    'per-bench-best',
})

HISTORICAL_BENCHES = frozenset({
    'AIME 2024',
    'AMC 2023',
    'AMC',
    'MATH-500',
    'GSM8K',
    'Minerva Math',
    'OlympiadBench',
    'Olympiad',
    'GPQA',
    'GPQA Diamond',
    'MMLU-Pro',
})

LCB_BENCHES = frozenset({
    'LiveCodeBench',
    'LiveCodeBench v5',
    'LiveCodeBench v6',
})

# Contest / problem-window start. HMMT needs an explicit month on the row.
BENCH_DATES = {
    'AIME 2025': date(2025, 2, 1),
    'AIME26': date(2026, 2, 1),
    'AIME 2026': date(2026, 2, 1),
}

# Official LiveCodeBench v6 release starts May 2023; version is not a cutoff.
LCB_DEFAULT_SPAN_START = date(2023, 5, 1)

# Known student data cutoffs. Qwen3 has none: AIME25 is not temporal.
MODEL_CUTOFFS = (
    ('DeepSeek-R1-Distill', date(2025, 1, 20)),
    ('Qwen2.5', date(2024, 9, 19)),
    ('Llama-3.2', date(2024, 9, 25)),
    ('Llama-3.1', date(2024, 7, 23)),
    ('Llama-3-', date(2024, 4, 18)),
    ('Llama-3 ', date(2024, 4, 18)),
    ('OLMo-3', date(2025, 11, 20)),
    ('OLMo-2', date(2024, 11, 1)),
    ('Phi-3.5', date(2024, 8, 20)),
)

PAPER_HMMT_MONTH = {
    CONSPO: date(2025, 2, 1),
}

PAPER_CKPT_SELECT = {
    CONSPO: 'best-every-100',
    ONESHOT: 'validation-avg',
}

PAPER_MODEL_ALIASES = {
    (ESPO, 'Qwen3'): 'Qwen3-14B-Base',
    (DFT, 'Qwen2.5-Math'): 'Qwen2.5-Math-7B',
    (HICRA, 'Llama-3.1-Instruct'): 'Llama-3.1-8B-Instruct',
}

CONSPO_CODE_ALIASES = {
    'ConSPO-DAPO': 'ConSPO',
    'DAPO-DAPO': 'DAPO',
    'GRPO-DAPO': 'GRPO',
}

# Empty teacher is a hole, not “no teacher”.
REQUIRE_TEACHER = frozenset({
    OPRD_PAPER,
    REVISIT_OPD,
    WEIGHT_GEO,
})

# Teacher with unknown cutoff: student date is not enough.
UNKNOWN_TEACHER = {
    WEIGHT_GEO: frozenset({
        'SFT',
        'DPO',
        'Off-GRPO',
        'Offline GRPO',
    }),
}

PAPER_TEACHERS = {
    WEIGHT_GEO: 'DeepSeek-V4-Flash',
    OPRD_PAPER: 'JustRL-Deepseek-1.5B',
    REVISIT_OPD: 'OpenThinker3-7B',
}

PAPER_TEACHERS_BY_CODE = {
    (REVISIT_OPD, 'top-K OPD-MT'): (
        'OpenThinker3-7B; GiGPO-Qwen2.5-7B-Instruct-ALFWorld'
    ),
}

TEACHER_NAME = PAPER_TEACHERS

# Known train-data cutoffs. Unknown datasets must not fail closed
# (ConSPO DeepScaleR would drop). Fill dates only when verified.
DATASET_CUTOFFS = ()

# (key, model, code, bench) -> temporal. Overrides the classifier.
TEMPORAL_ADMITS = {
    (WEIGHT_GEO, 'Qwen3-4B-Instruct-2507', 'GRPO', 'AIME26'),
    (WEIGHT_GEO, 'Qwen3-4B-Instruct-2507', 'DAPO', 'AIME26'),
    (CONSPO, 'Qwen3-4B-Base', 'ConSPO', 'AIME26'),
    (CONSPO, 'Qwen3-4B-Base', 'GRPO', 'AIME26'),
    (CONSPO, 'Qwen3-4B-Base', 'DAPO', 'AIME26'),
}

# Fold raw Online names before TEMPORAL_ADMITS lookup.
ADMIT_CODE_ALIASES = {
    'Online GRPO': 'GRPO',
    'Online DAPO': 'DAPO',
}

# Already-scaled pp victims from the first coerce pass. Divide if > 1.5.
# Each inner tuple is an AND of tokens; outer tuples are OR alternatives.
UNSCALE_MODELS = {
    (HICRA, 'AIME 2025'): (('llama-3.1', 'instruct'),),
    (DFT, 'AIME 2024'): (
        ('llama-3.2-3b',),
        ('llama-3.1-8b-base',),
        ('deepseekmath-7b',),
    ),
}

DROP_ROWS = {
    (CONSPO, 'Llama-3.2-3B-Instruct', 'AIME 2025'),
    (CONSPO, 'Llama-3.2-3B-Instruct', 'AIME26'),
}

# 1.5B Table 1 DeepScaleR (avg@32). base from the shared starting checkpoint.
CONSPO_T1_1P5 = {
    ('GRPO', 'AIME 2024'): (20.9, 28.6, 28.6),
    ('GRPO', 'AIME 2025'): (20.7, 22.9, 22.9),
    ('GRPO', 'AIME26'): (13.9, 20.4, 20.4),
    ('GRPO', 'AMC 2023'): (52.8, 64.4, 64.4),
    ('DAPO', 'AIME 2024'): (20.9, 28.6, 28.6),
    ('DAPO', 'AIME 2025'): (20.7, 22.9, 22.9),
    ('DAPO', 'AIME26'): (13.9, 20.8, 20.4),
    ('DAPO', 'AMC 2023'): (52.8, 66.2, 64.4),
    ('ConSPO', 'AIME 2024'): (20.9, 34.7, 28.6),
    ('ConSPO', 'AIME 2025'): (20.7, 26.7, 22.9),
    ('ConSPO', 'AIME26'): (13.9, 23.9, 20.4),
    ('ConSPO', 'AMC 2023'): (52.8, 70.4, 64.4),
}

# Extra temporal ConSPO cells where the extract omitted Table 1/2/3/9 AIME.
# gain / gain_ref only when the paper does not give a starting score.
CONSPO_EXTRA = (
    {
        'model': 'DeepSeek-R1-Distill-Qwen-7B',
        'code': 'ConSPO',
        'method': 'ConSPO',
        'bench': 'AIME 2025',
        'gain': 8.8,
        'gain_ref': 3.2,
        'source': 'Table 2 / §5.2',
    },
    {
        'model': 'DeepSeek-R1-Distill-Qwen-7B',
        'code': 'ConSPO',
        'method': 'ConSPO',
        'bench': 'AIME26',
        'gain': 11.3,
        'gain_ref': 2.9,
        'source': 'Table 2 / §5.2',
    },
    {
        'model': 'DeepSeek-R1-Distill-Llama-8B',
        'code': 'ConSPO',
        'method': 'ConSPO',
        'bench': 'AIME 2025',
        'gain': 8.3,
        'gain_ref': 4.1,
        'source': 'Table 2 / §5.2',
    },
    {
        'model': 'DeepSeek-R1-Distill-Llama-8B',
        'code': 'ConSPO',
        'method': 'ConSPO',
        'bench': 'AIME26',
        'gain': 14.9,
        'gain_ref': 1.3,
        'source': 'Table 2 / §5.2',
    },
    {
        'model': 'Qwen3-4B-Base',
        'code': 'ConSPO',
        'method': 'ConSPO',
        'bench': 'AIME26',
        'gain': 8.0,
        'gain_ref': 2.3,
        'source': 'Table 3 / §5.2',
    },
    {
        'model': 'DeepSeek-R1-Distill-Qwen-32B',
        'code': 'ConSPO',
        'method': 'ConSPO',
        'bench': 'AIME 2025',
        'gain_ref': 3.2,
        'source': 'Table 9 / Appendix D',
    },
    {
        'model': 'DeepSeek-R1-Distill-Qwen-32B',
        'code': 'ConSPO',
        'method': 'ConSPO',
        'bench': 'AIME26',
        'gain_ref': 2.9,
        'source': 'Table 9 / Appendix D',
    },
)


def is_qwen3(model: str) -> bool:
    return (model or '').replace(' ', '').lower().startswith('qwen3')


def model_cutoff(model: str) -> date | None:
    text = model or ''
    for prefix, cutoff in MODEL_CUTOFFS:
        if text.startswith(prefix):
            return cutoff
    return None


def bench_date(bench: str, hmmt_month: date | None = None) -> date | None:
    if bench in {'HMMT 2025', 'HMMT'}:
        return hmmt_month
    return BENCH_DATES.get(bench)


def parse_bench_span(text: str) -> date | None:
    raw = (text or '').strip()
    if not raw:
        return None
    try:
        parts = [int(bit) for bit in raw.split('-')[:3]]
    except ValueError:
        return None
    if len(parts) < 2:
        return None
    year, month = parts[0], parts[1]
    day = parts[2] if len(parts) > 2 else 1
    return date(year, month, day)


def split_teachers(teacher: str) -> list[str]:
    return [part.strip() for part in (teacher or '').split(';') if part.strip()]


def has_unknown_teacher(key: str, code: str, method: str, teacher: str) -> bool:
    names = split_teachers(teacher)
    if key in REQUIRE_TEACHER and not names:
        return True
    for name in names:
        if not model_cutoff(name):
            return True
    blocked = UNKNOWN_TEACHER.get(key) or set()
    return (code or '') in blocked or (method or '') in blocked


def dataset_cutoff(train_data: str) -> date | None:
    text = (train_data or '').lower()
    if not text:
        return None
    for prefix, cutoff in DATASET_CUTOFFS:
        if prefix.lower() in text:
            return cutoff
    return None


def admit_names(code: str, method: str) -> tuple[str, ...]:
    names = []
    for name in (code, method, code or method):
        if not name or name in names:
            continue
        names.append(name)
        aliased = ADMIT_CODE_ALIASES.get(name)
        if aliased and aliased not in names:
            names.append(aliased)
    return tuple(names)


def classify_ood_basis(
    key: str,
    model: str,
    bench: str,
    code: str = '',
    method: str = '',
    train_data: str = '',
    teacher: str = '',
    bench_span: str = '',
    listed_id: bool = False,
    listed_ood: bool = False,
    hmmt_month: date | None = None,
) -> str:
    for name in admit_names(code, method):
        if (key, model, name, bench) in TEMPORAL_ADMITS:
            return 'temporal'
    if bench in HISTORICAL_BENCHES:
        if listed_id:
            return 'id'
        return 'rl_stage'
    if bench in LCB_BENCHES:
        span = parse_bench_span(bench_span)
        if span is None:
            return 'unverified'
        cutoff = chain_cutoff(model, teacher, train_data, key, code, method)
        if cutoff is None:
            return 'unverified'
        if span > cutoff:
            return 'temporal'
        return 'rl_stage'
    contest = bench_date(bench, hmmt_month=hmmt_month)
    if contest is None:
        return 'unverified'
    if is_qwen3(model) and bench == 'AIME 2025':
        return 'unverified'
    if has_unknown_teacher(key, code, method, teacher):
        return 'unverified'
    cutoff = chain_cutoff(model, teacher, train_data, key, code, method)
    if cutoff is None:
        return 'unverified'
    if contest > cutoff:
        return 'temporal'
    if listed_id:
        return 'id'
    if listed_ood:
        return 'rl_stage'
    return 'unverified'


def chain_cutoff(
    model: str,
    teacher: str,
    train_data: str,
    key: str,
    code: str,
    method: str,
) -> date | None:
    if has_unknown_teacher(key, code, method, teacher):
        return None
    dates = []
    student = model_cutoff(model)
    if student:
        dates.append(student)
    for name in split_teachers(teacher):
        taught = model_cutoff(name)
        if taught:
            dates.append(taught)
        elif name:
            return None
    trained = dataset_cutoff(train_data)
    if trained:
        dates.append(trained)
    if not dates:
        return None
    return max(dates)


def default_ckpt_select(key: str, explicit: str = '') -> str:
    if explicit and explicit != 'unspecified':
        return explicit
    return PAPER_CKPT_SELECT.get(key, explicit or 'unspecified')


def resolve_teacher(
    key: str,
    code: str,
    method: str,
    explicit: str = '',
    inventory: list[str] | None = None,
) -> str:
    if explicit:
        return explicit
    named = PAPER_TEACHERS_BY_CODE.get((key, code or ''))
    if named:
        return named
    named = PAPER_TEACHERS_BY_CODE.get((key, method or ''))
    if named:
        return named
    if key in PAPER_TEACHERS:
        return PAPER_TEACHERS[key]
    names = []
    for item in inventory or []:
        if item and item not in names:
            names.append(item)
    if names:
        return '; '.join(names)
    blocked = UNKNOWN_TEACHER.get(key)
    if blocked and ((code in blocked) or (method in blocked)):
        return PAPER_TEACHERS.get(key, '')
    return ''


def default_teacher(key: str, code: str, method: str, explicit: str = '') -> str:
    return resolve_teacher(key, code, method, explicit=explicit)


def short_train_tag(text: str) -> str:
    blob = (text or '').lower()
    if 'dapo-math' in blob or 'dapo math' in blob:
        return 'DAPO-Math'
    if 'deepscaler' in blob:
        return 'DeepScaleR'
    compact = (text or '').split('(')[0].strip()
    return compact[:18] if compact else ''


def should_unscale(row: dict) -> bool:
    specs = UNSCALE_MODELS.get((row.get('key'), row.get('bench')))
    if not specs:
        return False
    model = (row.get('model') or '').lower()
    return any(all(token in model for token in tokens) for tokens in specs)


def unscale_row(row: dict) -> dict:
    item = dict(row)
    if not should_unscale(item):
        return item
    nums = [
        item[field]
        for field in ('base', 'ref', 'score')
        if item.get(field) is not None
    ]
    if not nums or max(abs(value) for value in nums) <= 1.5:
        return item
    for field in ('base', 'ref', 'score', 'gain', 'gain_ref'):
        value = item.get(field)
        if value is not None and abs(value) > 1.5:
            item[field] = value / 100.0
    item['unit'] = 'pp'
    return item


def alias_conspo_code(row: dict) -> dict:
    item = dict(row)
    if item.get('key') != CONSPO:
        return item
    chosen = item.get('code') or item.get('method') or ''
    aliased = CONSPO_CODE_ALIASES.get(chosen)
    if aliased:
        item['code'] = aliased
        item['method'] = aliased
    return item


def alias_paper_model(key: str, model: str) -> str:
    return PAPER_MODEL_ALIASES.get((key, model), model)


def should_drop_row(row: dict) -> bool:
    return (
        row.get('key'),
        row.get('model'),
        row.get('bench'),
    ) in DROP_ROWS


def conspo_train_data(source: str) -> str:
    blob = (source or '').lower()
    if 'table 4' in blob:
        return 'DAPO-Math-17k'
    return 'DeepScaleR-Preview-Dataset'


def apply_gain_overrides(rows: list[dict]) -> list[dict]:
    out = []
    have = set()
    for row in rows:
        item = alias_conspo_code(unscale_row(dict(row)))
        if item.get('key') == CONSPO:
            item['train_data'] = item.get('train_data') or conspo_train_data(
                item.get('source') or '',
            )
            item['metric'] = item.get('metric') or 'avg@32'
            if item['bench'] in {'MATH-500', 'OlympiadBench'}:
                item['metric'] = item.get('metric') or 'pass@1'
        if should_drop_row(item):
            continue
        out.append(item)
        have.add((
            item.get('key'),
            item.get('model'),
            item.get('code'),
            item.get('bench'),
            item.get('train_data') or '',
            item.get('source') or '',
        ))
    out.extend(_conspo_table1_rows(have))
    out.extend(_conspo_extra_rows(have))
    out.extend(_weight_geo_dapo_rows(have))
    return out


def _weight_geo_dapo_rows(have: set[tuple]) -> list[dict]:
    model = 'Qwen3-4B-Instruct-2507'
    source = 'Table 2 (Online DAPO)'
    train = (
        'DeepScaleR prompts (on-policy; Table 2 adapters, '
        'same protocol as Online GRPO)'
    )
    pair = (WEIGHT_GEO, model, 'DAPO', 'AIME26', train, source)
    alt = (WEIGHT_GEO, model, 'DAPO', 'AIME26')
    if pair in have or any(
        item[:4] == alt for item in have
    ):
        return []
    return [{
        'key': WEIGHT_GEO,
        'code': 'DAPO',
        'method': 'DAPO',
        'model': model,
        'bench': 'AIME26',
        'metric': 'pass@1',
        'base': 16.7,
        'ref': 20.0,
        'ref_method': 'GRPO',
        'score': 16.7,
        'gain': None,
        'gain_ref': None,
        'source': source,
        'train_data': train,
        'teacher': '',
        'unit': 'pp',
        'bench_span': '',
        'ckpt_select': 'unspecified',
        'ood_basis': '',
        'ood': False,
    }]


def _conspo_table1_rows(have: set[tuple]) -> list[dict]:
    added = []
    model = 'DeepSeek-R1-Distill-Qwen-1.5B'
    source = 'Table 1 / §5.2'
    train = 'DeepScaleR-Preview-Dataset'
    for (code, bench), (base, score, ref) in CONSPO_T1_1P5.items():
        pair = (CONSPO, model, code, bench, train, source)
        if pair in have:
            continue
        added.append({
            'key': CONSPO,
            'code': code,
            'method': code,
            'model': model,
            'bench': bench,
            'metric': 'avg@32',
            'base': base,
            'ref': ref,
            'ref_method': 'GRPO',
            'score': score,
            'gain': None,
            'gain_ref': None,
            'source': source,
            'train_data': train,
            'teacher': '',
            'unit': 'pp',
            'bench_span': '',
            'ckpt_select': 'best-every-100',
            'ood_basis': '',
            'ood': False,
        })
    return added


def _conspo_extra_rows(have: set[tuple]) -> list[dict]:
    added = []
    train = 'DeepScaleR-Preview-Dataset'
    for spec in CONSPO_EXTRA:
        source = spec['source']
        pair = (CONSPO, spec['model'], spec['code'], spec['bench'], train, source)
        if pair in have:
            continue
        added.append({
            'key': CONSPO,
            'code': spec['code'],
            'method': spec['method'],
            'model': spec['model'],
            'bench': spec['bench'],
            'metric': 'avg@32',
            'base': spec.get('base'),
            'ref': spec.get('ref'),
            'ref_method': 'GRPO',
            'score': spec.get('score'),
            'gain': spec.get('gain'),
            'gain_ref': spec.get('gain_ref'),
            'source': source,
            'train_data': train,
            'teacher': '',
            'unit': 'pp',
            'bench_span': '',
            'ckpt_select': 'best-every-100',
            'ood_basis': '',
            'ood': False,
        })
    return added
