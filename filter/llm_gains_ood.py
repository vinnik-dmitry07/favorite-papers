'''Temporal OOD classifier and paper-specific gain overrides.

A rendered markdown cell requires ood_basis=temporal: the bench date is after
the full training-chain cutoff (student + teacher + train data). Inventory
eval_ood is not enough. Historical benches never auto-qualify.
'''

from __future__ import annotations

from dataclasses import dataclass
import re
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
TWO_GRPO = 'arxiv:2510.00977'
SELF_DISTILL = 'arxiv:2603.24472'
SHAO = 'arxiv:2506.10947'

OOD_BASES = ('temporal', 'rl_stage', 'id', 'unverified')
CKPT_SELECT = (
    'final',
    'last',
    'last@300; 10-step smoothed curve',
    'last@287; 10-step smoothed curve',
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

# Shao §3 + Paradox App C: non-Qwen checkpoints with no memorization shortcut
# on the benches both papers treat as historical / contaminated for Qwen.
LEAKAGE_FREE_MODELS = frozenset({
    'Llama-3.1-8B',
    'Llama-3.1-8B-Base',
    'Llama-3.1-8B-Instruct',
    'Llama-3.2-3B',
    'Llama-3.2-3B-Instruct',
    'OLMo-2-1124-7B',
    'OLMo-2-1124-7B-SFT',
})
LEAKAGE_FREE_BENCHES = frozenset({
    'MATH-500',
    'AMC 2023',
    'AIME 2024',
    'Minerva Math',
})
LEAKAGE_FREE_SOURCE = (
    'https://arxiv.org/html/2506.10947v2#S3',
    'https://arxiv.org/html/2601.11061v1#A3',
)


def leakage_free(model: str, bench: str) -> bool:
    return model in LEAKAGE_FREE_MODELS and bench in LEAKAGE_FREE_BENCHES


@dataclass(frozen=True)
class Cutoff:
    '''A dated bound. Empty source is unknown: the date cannot admit a row.'''

    day: date
    source: str
    basis: str  # release | content | contest


# LCB sitting date is the row's bench_span, not a contest URL.
LCB_SPAN_SOURCE = 'row:bench_span'

_AIME26 = Cutoff(
    date(2026, 2, 5),
    'https://maa.org/news/2025-26-aime-thresholds-are-now-available/',
    'contest',
)
BENCH_DATES = {
    'AIME 2025': Cutoff(
        date(2025, 2, 6),
        'https://maa.org/news/aime-thresholds-are-available/',
        'contest',
    ),
    'AIME26': _AIME26,
    'AIME 2026': _AIME26,
}

_LLAMA3 = Cutoff(
    date(2024, 4, 18),
    'https://ai.meta.com/blog/meta-llama-3/',
    'release',
)

# Known student data cutoffs (release = upper bound on training content).
# Bare Qwen3 is omitted: AIME25 stays unverified.
MODEL_CUTOFFS = (
    (
        'DeepSeek-R1-Distill',
        Cutoff(
            date(2025, 1, 20),
            'https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B',
            'release',
        ),
    ),
    (
        'Qwen3-4B-Instruct-2507',
        Cutoff(
            date(2025, 8, 6),
            'https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507',
            'release',
        ),
    ),
    (
        'Qwen3-4B-Base',
        Cutoff(
            date(2025, 4, 29),
            'https://qwenlm.github.io/blog/qwen3/',
            'release',
        ),
    ),
    (
        'Qwen2.5',
        Cutoff(
            date(2024, 9, 19),
            'https://qwenlm.github.io/blog/qwen2.5/',
            'release',
        ),
    ),
    (
        'Llama-3.2',
        Cutoff(
            date(2024, 9, 25),
            'https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/',
            'release',
        ),
    ),
    (
        'Llama-3.1',
        Cutoff(
            date(2024, 7, 23),
            'https://ai.meta.com/blog/meta-llama-3-1/',
            'release',
        ),
    ),
    ('Llama-3-', _LLAMA3),
    ('Llama-3 ', _LLAMA3),
    (
        'OLMo-3',
        Cutoff(
            date(2025, 11, 20),
            'https://allenai.org/blog/olmo3',
            'release',
        ),
    ),
    (
        'OLMo-2',
        Cutoff(
            date(2024, 11, 26),
            'https://allenai.org/blog/olmo2',
            'release',
        ),
    ),
    (
        'Phi-3.5',
        Cutoff(
            date(2024, 8, 20),
            'https://huggingface.co/microsoft/Phi-3.5-mini-instruct',
            'release',
        ),
    ),
)

HMMT_FEB_2025 = Cutoff(
    date(2025, 2, 15),
    'https://hmmt-archive.s3.amazonaws.com/tournaments/2025/feb/results/short.htm',
    'contest',
)
PAPER_HMMT_DATE = {
    CONSPO: HMMT_FEB_2025,
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

# Empty teacher is a hole, not “no teacher”. Online WeightGeo has none.
REQUIRE_TEACHER = frozenset({
    OPRD_PAPER,
    REVISIT_OPD,
})

WEIGHT_GEO_ONLINE = frozenset({
    'Online GRPO',
    'Online DAPO',
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

# Known train-data cutoffs (content = max dated component). Empty/unknown fail closed.
# DeepScaleR HF card (commits 2025-02-09/10, no later data) lists AIME 1984–2023,
# AMC < 2023, Omni-MATH (arXiv 2410.07985 v1 2024-10-10), and STILL-3
# (MATH + NuminaMathCoT + AIME 1983–2023; all HF commits 2025-01-26).
# The dataset *release* (2025-02-09) is after AIME 2025 I (2025-02-06); only
# the component bound admits AIME 2025.
_DAPO_MATH = Cutoff(
    date(2025, 3, 17),
    'https://huggingface.co/datasets/BytedTsinghua-SIA/DAPO-Math-17k/commit/851fd44a728da639d3a8b2c12be5d971f45b360e',
    'content',
)
DATASET_CUTOFFS = (
    ('dapo-math-17k', _DAPO_MATH),
    ('dapo-math-sub', _DAPO_MATH),
    ('dapo-math', _DAPO_MATH),
    (
        'deepscaler',
        Cutoff(
            date(2025, 1, 26),
            'https://huggingface.co/datasets/RUC-AIBOX/STILL-3-Preview-RL-Data',
            'content',
        ),
    ),
    (
        'smoltalk2',
        Cutoff(
            date(2025, 7, 10),
            'https://huggingface.co/datasets/HuggingFaceTB/smoltalk2/commit/cf3d7c37036a55161f2fa02f40a020a109ed757d',
            'content',
        ),
    ),
)

# Hendrycks MATH as a token, not *Math* compounds or the word "mathematical".
MATH_DATASET_CUTOFF = Cutoff(
    date(2021, 3, 5),
    'https://arxiv.org/abs/2103.03874v1',
    'content',
)
MATH_DATASET_RE = re.compile(
    r'(?:^|[\s(/,])math(?:$|[\s]*\(|[\s]+train\b)',
    re.I,
)

PAPER_TRAIN_DATA = {
    ONESHOT: 'DeepScaleR subset',
    SELF_DISTILL: 'DAPO-Math-17k',
    SHAO: 'DeepScaleR',
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

# 1.5B Table 1 DeepScaleR (avg@32). Tuple is (base, score, ref=GRPO).
CONSPO_T1_1P5 = {
    ('GRPO', 'AIME 2024'): (20.9, 28.6, 28.6),
    ('GRPO', 'AIME 2025'): (20.7, 22.9, 22.9),
    ('GRPO', 'AIME26'): (13.9, 20.4, 20.4),
    ('GRPO', 'HMMT 2025'): (9.7, 11.7, 11.7),
    ('GRPO', 'AMC 2023'): (52.8, 64.4, 64.4),
    ('DAPO', 'AIME 2024'): (20.9, 28.6, 28.6),
    ('DAPO', 'AIME 2025'): (20.7, 22.9, 22.9),
    ('DAPO', 'AIME26'): (13.9, 20.8, 20.4),
    ('DAPO', 'HMMT 2025'): (9.7, 13.5, 11.7),
    ('DAPO', 'AMC 2023'): (52.8, 66.2, 64.4),
    ('Dr.GRPO', 'AIME 2024'): (20.9, 27.4, 28.6),
    ('Dr.GRPO', 'AIME 2025'): (20.7, 22.0, 22.9),
    ('Dr.GRPO', 'AIME26'): (13.9, 19.5, 20.4),
    ('Dr.GRPO', 'HMMT 2025'): (9.7, 10.7, 11.7),
    ('Dr.GRPO', 'AMC 2023'): (52.8, 63.5, 64.4),
    ('DisCO', 'AIME 2024'): (20.9, 28.3, 28.6),
    ('DisCO', 'AIME 2025'): (20.7, 24.8, 22.9),
    ('DisCO', 'AIME26'): (13.9, 21.7, 20.4),
    ('DisCO', 'HMMT 2025'): (9.7, 14.4, 11.7),
    ('DisCO', 'AMC 2023'): (52.8, 66.5, 64.4),
    ('GMPO', 'AIME 2024'): (20.9, 31.5, 28.6),
    ('GMPO', 'AIME 2025'): (20.7, 24.6, 22.9),
    ('GMPO', 'AIME26'): (13.9, 23.8, 20.4),
    ('GMPO', 'HMMT 2025'): (9.7, 12.8, 11.7),
    ('GMPO', 'AMC 2023'): (52.8, 70.0, 64.4),
    ('CISPO', 'AIME 2024'): (20.9, 31.4, 28.6),
    ('CISPO', 'AIME 2025'): (20.7, 23.0, 22.9),
    ('CISPO', 'AIME26'): (13.9, 23.0, 20.4),
    ('CISPO', 'HMMT 2025'): (9.7, 13.3, 11.7),
    ('CISPO', 'AMC 2023'): (52.8, 65.2, 64.4),
    ('SAPO', 'AIME 2024'): (20.9, 30.6, 28.6),
    ('SAPO', 'AIME 2025'): (20.7, 25.3, 22.9),
    ('SAPO', 'AIME26'): (13.9, 23.3, 20.4),
    ('SAPO', 'HMMT 2025'): (9.7, 12.8, 11.7),
    ('SAPO', 'AMC 2023'): (52.8, 70.1, 64.4),
    ('ConSPO', 'AIME 2024'): (20.9, 34.7, 28.6),
    ('ConSPO', 'AIME 2025'): (20.7, 26.7, 22.9),
    ('ConSPO', 'AIME26'): (13.9, 23.9, 20.4),
    ('ConSPO', 'HMMT 2025'): (9.7, 14.9, 11.7),
    ('ConSPO', 'AMC 2023'): (52.8, 70.4, 64.4),
}

def _conspo_cells(model, source, train, benches, base, scores, ref):
    rows = []
    for code, vals in scores.items():
        for bench, score in zip(benches, vals):
            rows.append({
                'model': model,
                'code': code,
                'method': code,
                'bench': bench,
                'base': base[bench],
                'score': score,
                'ref': ref[bench],
                'source': source,
                'train_data': train,
            })
    return tuple(rows)


# Extra ConSPO cells omitted by the extract. Numbers from arxiv HTML tables.
_T2 = 'Table 2 / §5.2'
_T3 = 'Table 3 / §5.2'
_T4 = 'Table 4 / §5.2'
_T9 = 'Table 9 / Appendix D'
_DS = 'DeepScaleR-Preview-Dataset'
_DM = 'DAPO-Math-17k'

CONSPO_EXTRA = tuple(
    _conspo_cells(
        'DeepSeek-R1-Distill-Qwen-7B',
        _T2,
        _DS,
        ('AIME 2025', 'AIME26', 'HMMT 2025'),
        {'AIME 2025': 30.3, 'AIME26': 35.5, 'HMMT 2025': 17.5},
        {
            'GRPO': (35.9, 43.9, 20.7),
            'DAPO': (34.2, 37.9, 20.4),
            'Dr.GRPO': (35.3, 43.3, 21.7),
            'DisCO': (36.9, 45.1, 19.6),
            'ConSPO': (39.1, 46.8, 21.5),
        },
        {'AIME 2025': 35.9, 'AIME26': 43.9, 'HMMT 2025': 20.7},
    )
    + _conspo_cells(
        'DeepSeek-R1-Distill-Llama-8B',
        _T2,
        _DS,
        ('AIME 2025', 'AIME26', 'HMMT 2025'),
        {'AIME 2025': 21.3, 'AIME26': 20.6, 'HMMT 2025': 13.5},
        {
            'GRPO': (25.5, 34.2, 18.5),
            'DAPO': (24.0, 29.9, 17.9),
            'Dr.GRPO': (26.8, 32.4, 19.6),
            'DisCO': (28.8, 32.8, 19.7),
            'ConSPO': (29.6, 35.5, 22.6),
        },
        {'AIME 2025': 25.5, 'AIME26': 34.2, 'HMMT 2025': 18.5},
    )
    + _conspo_cells(
        'Qwen3-4B-Base',
        _T3,
        _DS,
        ('AIME26',),
        {'AIME26': 4.8},
        {
            'GRPO': (10.5,),
            'DAPO': (8.5,),
            'Dr.GRPO': (12.4,),
            'DisCO': (9.4,),
            'ConSPO': (12.8,),
        },
        {'AIME26': 10.5},
    )
    + _conspo_cells(
        'DeepSeek-R1-Distill-Qwen-1.5B',
        _T4,
        _DM,
        ('AIME26',),
        {'AIME26': 13.9},
        {
            'Dr.GRPO': (19.6,),
            'DisCO': (20.2,),
        },
        {'AIME26': 21.6},
    )
    + (
        {
            'model': 'DeepSeek-R1-Distill-Qwen-32B',
            'code': 'ConSPO',
            'method': 'ConSPO',
            'bench': 'AIME 2025',
            'gain_ref': 3.2,
            'source': _T9,
            'train_data': _DS,
        },
        {
            'model': 'DeepSeek-R1-Distill-Qwen-32B',
            'code': 'ConSPO',
            'method': 'ConSPO',
            'bench': 'AIME26',
            'gain_ref': 2.9,
            'source': _T9,
            'train_data': _DS,
        },
    )
)


def is_qwen3(model: str) -> bool:
    return (model or '').replace(' ', '').lower().startswith('qwen3')


def usable_day(rec: Cutoff | None) -> date | None:
    if rec is None or not rec.source:
        return None
    return rec.day


def model_cutoff_rec(model: str) -> Cutoff | None:
    text = model or ''
    for prefix, cutoff in MODEL_CUTOFFS:
        if text.startswith(prefix):
            return cutoff if cutoff.source else None
    return None


def model_cutoff(model: str) -> date | None:
    return usable_day(model_cutoff_rec(model))


def bench_date_rec(bench: str, key: str = '') -> Cutoff | None:
    if bench in {'HMMT 2025', 'HMMT'}:
        rec = PAPER_HMMT_DATE.get(key)
        return rec if rec and rec.source else None
    rec = BENCH_DATES.get(bench)
    return rec if rec and rec.source else None


def bench_date(bench: str, key: str = '') -> date | None:
    return usable_day(bench_date_rec(bench, key=key))


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


def dataset_cutoff_rec(train_data: str) -> Cutoff | None:
    text = (train_data or '').lower()
    if not text:
        return None
    recs = [
        cutoff for prefix, cutoff in DATASET_CUTOFFS
        if prefix.lower() in text and cutoff.source
    ]
    if MATH_DATASET_RE.search(train_data or '') and MATH_DATASET_CUTOFF.source:
        recs.append(MATH_DATASET_CUTOFF)
    if not recs:
        return None
    return max(recs, key=lambda rec: rec.day)


def dataset_cutoff(train_data: str) -> date | None:
    return usable_day(dataset_cutoff_rec(train_data))


def _parse_iso(text: str) -> date | None:
    if not text:
        return None
    return date.fromisoformat(text)


def cutoff_proof(
    model: str,
    teacher: str,
    train_data: str,
    bench: str,
    key: str,
    code: str = '',
    method: str = '',
    bench_span: str = '',
) -> dict:
    student = model_cutoff_rec(model)
    train = dataset_cutoff_rec(train_data)
    names = split_teachers(teacher)
    teacher_recs = [model_cutoff_rec(name) for name in names]
    teacher_rec = None
    if names and all(teacher_recs) and not has_unknown_teacher(
        key, code, method, teacher,
    ):
        teacher_rec = max(teacher_recs, key=lambda rec: rec.day)
    if bench in LCB_BENCHES:
        span = parse_bench_span(bench_span)
        bench_rec = (
            Cutoff(span, LCB_SPAN_SOURCE, 'contest') if span else None
        )
    else:
        bench_rec = bench_date_rec(bench, key=key)
    return {
        'model_cutoff': student.day.isoformat() if student else '',
        'train_cutoff': train.day.isoformat() if train else '',
        'teacher_cutoff': teacher_rec.day.isoformat() if teacher_rec else '',
        'benchmark_date': bench_rec.day.isoformat() if bench_rec else '',
        'cutoff_source': {
            'model': student.source if student else '',
            'train': train.source if train else '',
            'teacher': teacher_rec.source if teacher_rec else '',
            'bench': bench_rec.source if bench_rec else '',
        },
    }


def chain_from_proof(proof: dict, teacher: str, key: str) -> date | None:
    student = _parse_iso(proof.get('model_cutoff') or '')
    trained = _parse_iso(proof.get('train_cutoff') or '')
    if student is None or trained is None:
        return None
    dates = [student, trained]
    taught = _parse_iso(proof.get('teacher_cutoff') or '')
    names = split_teachers(teacher)
    if names or key in REQUIRE_TEACHER:
        if taught is None:
            return None
        dates.append(taught)
    return max(dates)


def temporal_proof(
    model: str,
    teacher: str,
    train_data: str,
    key: str,
    code: str,
    method: str,
) -> bool:
    proof = cutoff_proof(model, teacher, train_data, '', key, code, method)
    return chain_from_proof(proof, teacher, key) is not None


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
    proof: dict | None = None,
) -> str:
    if bench in HISTORICAL_BENCHES:
        if listed_id:
            return 'id'
        return 'rl_stage'
    proof = proof or cutoff_proof(
        model, teacher, train_data, bench, key, code, method,
        bench_span=bench_span,
    )
    contest = _parse_iso(proof.get('benchmark_date') or '')
    if contest is None:
        return 'unverified'
    if is_qwen3(model) and bench == 'AIME 2025':
        return 'unverified'
    if has_unknown_teacher(key, code, method, teacher):
        return 'unverified'
    cutoff = chain_from_proof(proof, teacher, key)
    if cutoff is None:
        return 'unverified'
    if contest > cutoff:
        return 'temporal'
    if bench in LCB_BENCHES:
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
    proof = cutoff_proof(model, teacher, train_data, '', key, code, method)
    return chain_from_proof(proof, teacher, key)


def default_ckpt_select(key: str, explicit: str = '') -> str:
    if explicit and explicit != 'unspecified':
        return explicit
    return PAPER_CKPT_SELECT.get(key, explicit or 'unspecified')


def is_weight_geo_online(code: str, method: str, source: str = '') -> bool:
    blob = f'{code} {method} {source}'.lower()
    if 'off-grpo' in blob or 'offline' in blob:
        return False
    if (code or '') in WEIGHT_GEO_ONLINE or (method or '') in WEIGHT_GEO_ONLINE:
        return True
    return 'online grpo' in blob or 'online dapo' in blob


def infer_train_data(row: dict) -> str:
    key = row.get('key') or ''
    if key == HICRA:
        return ''
    if row.get('train_data'):
        return row['train_data']
    source = (row.get('source') or '').lower()
    if key == TWO_GRPO:
        if 'dapo-math' in source:
            return 'DAPO-Math-sub'
        if 'math train' in source:
            return 'MATH'
    return PAPER_TRAIN_DATA.get(key, '')


def resolve_teacher(
    key: str,
    code: str,
    method: str,
    explicit: str = '',
    inventory: list[str] | None = None,
    source: str = '',
) -> str:
    if key == WEIGHT_GEO and is_weight_geo_online(code, method, source):
        return ''
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


def default_teacher(
    key: str,
    code: str,
    method: str,
    explicit: str = '',
    source: str = '',
) -> str:
    return resolve_teacher(
        key, code, method, explicit=explicit, source=source,
    )


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


# Appendix D Figures 12–13, last point of the thick 10-step-smoothed SVG
# curve (usually step 300). Tuple is (base, score, gain). Gain is the
# independently rounded last-minus-first from the curve; it can differ
# from score-base by 0.1. Do not use the curve max.
SHAO_PLOT_SOURCE = 'Appendix D, Figure 12/13'
SHAO_PLOT_CKPT = 'last@300; 10-step smoothed curve'
SHAO_PLOT_CKPT_287 = 'last@287; 10-step smoothed curve'
SHAO_PLOT_NOISE_PP = 2.0
SHAO_PLOT_METHODS = (
    ('gt', 'GRPO', 'GRPO (ground-truth reward)'),
    ('majority', 'GRPO-majority', 'GRPO (majority vote)'),
    ('incorrect', 'GRPO-incorrect', 'GRPO (incorrect reward)'),
    ('format', 'GRPO-format', 'GRPO (format reward)'),
    ('random', 'GRPO-random', 'GRPO (random reward)'),
)
SHAO_AIME25_PLOT = {
    'Qwen2.5-Math-7B': {
        'gt': (6.3, 13.7, 7.4),
        'majority': (5.4, 9.9, 4.5),
        'incorrect': (4.2, 6.9, 2.8),
        'format': (5.4, 5.0, -0.4),
        'random': (6.3, 8.7, 2.4),
    },
    'Qwen2.5-Math-1.5B': {
        'gt': (5.0, 6.5, 1.5),
        'majority': (2.9, 6.3, 3.4),
        'incorrect': (5.0, 5.7, 0.7),
        'format': (5.0, 4.3, -0.7),
        'random': (5.0, 4.2, -0.8),
    },
    'Qwen2.5-1.5B': {
        'gt': (0.4, 1.5, 1.1),
        'majority': (0.0, 1.9, 1.9),
        'incorrect': (0.0, 0.7, 0.7),
        'format': (0.4, 0.3, -0.1),
        'random': (0.4, 0.0, -0.4),
    },
    'Qwen2.5-7B': {
        'gt': (0.8, 7.7, 6.8),
        'majority': (0.4, 3.2, 2.8),
        'incorrect': (0.0, 3.9, 3.9),
        'format': (0.8, 2.8, 2.0),
        'random': (0.8, 5.2, 4.4),
    },
    'OLMo-2-1124-7B': {
        'gt': (0.0, 0.0, 0.0),
        'majority': (0.0, 0.0, 0.0),
        'incorrect': (0.4, 0.0, -0.4),
        'format': (0.0, 0.0, 0.0),
        'random': (0.0, 0.0, 0.0),
    },
    'OLMo-2-1124-7B-SFT': {
        'gt': (0.4, 0.2, -0.3),
        'majority': (0.0, 0.1, 0.1),
        'incorrect': (0.0, 0.2, 0.2),
        'format': (0.4, 0.4, 0.0),
        'random': (0.4, 0.2, -0.3),
    },
    'Llama-3.2-3B': {
        'gt': (0.2, 0.0, -0.2),
        'majority': (0.4, 0.0, -0.4),
        'incorrect': (0.8, 0.1, -0.7),
        'format': (0.4, 0.0, -0.4),
        'random': (0.4, 1.2, 0.8),
    },
    'Llama-3.1-8B': {
        'gt': (0.0, 0.2, 0.2),
        'majority': (0.0, 0.0, 0.0),
        'incorrect': (0.0, 0.0, 0.0),
        'format': (0.0, 0.0, 0.0),
        'random': (0.0, 0.6, 0.6),
    },
    'Llama-3.2-3B-Instruct': {
        'gt': (0.4, 0.6, 0.2),
        'majority': (0.0, 0.2, 0.2),
        'incorrect': (0.4, 0.1, -0.3),
        'format': (0.4, 0.2, -0.2),
        'random': (0.4, 0.3, -0.1),
    },
    'Llama-3.1-8B-Instruct': {
        'gt': (0.8, 0.2, -0.7),
        'majority': (0.8, 0.1, -0.7),
        'incorrect': (0.0, 0.0, 0.0),
        'format': (0.8, 0.7, -0.2),
        'random': (0.8, 0.3, -0.5),
    },
}
SHAO_PLOT_CKPT_OVERRIDE = {
    ('Llama-3.2-3B', 'random'): SHAO_PLOT_CKPT_287,
}


def apply_gain_overrides(rows: list[dict]) -> list[dict]:
    out = []
    have = set()
    have_scored = set()
    for row in rows:
        item = alias_conspo_code(unscale_row(dict(row)))
        if item.get('key') == CONSPO:
            item['train_data'] = item.get('train_data') or conspo_train_data(
                item.get('source') or '',
            )
            item['metric'] = item.get('metric') or 'avg@32'
            if item['bench'] in {'MATH-500', 'OlympiadBench'}:
                item['metric'] = item.get('metric') or 'pass@1'
        item['train_data'] = infer_train_data(item)
        if should_drop_row(item):
            continue
        out.append(item)
        pair = (
            item.get('key'),
            item.get('model'),
            item.get('code'),
            item.get('bench'),
            item.get('train_data') or '',
            item.get('source') or '',
        )
        have.add(pair)
        if item.get('score') is not None:
            have_scored.add(pair)
    out.extend(_conspo_table1_rows(have_scored))
    out.extend(_conspo_extra_rows(have_scored))
    out.extend(_weight_geo_dapo_rows(have))
    out.extend(_shao_aime25_plot_rows(have_scored))
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


def _conspo_table1_rows(have_scored: set[tuple]) -> list[dict]:
    added = []
    model = 'DeepSeek-R1-Distill-Qwen-1.5B'
    source = 'Table 1 / §5.2'
    train = 'DeepScaleR-Preview-Dataset'
    for (code, bench), (base, score, ref) in CONSPO_T1_1P5.items():
        pair = (CONSPO, model, code, bench, train, source)
        if pair in have_scored:
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


def _conspo_extra_rows(have_scored: set[tuple]) -> list[dict]:
    added = []
    for spec in CONSPO_EXTRA:
        source = spec['source']
        train = spec.get('train_data') or 'DeepScaleR-Preview-Dataset'
        pair = (
            CONSPO,
            spec['model'],
            spec['code'],
            spec['bench'],
            train,
            source,
        )
        if pair in have_scored:
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
            'train_data': spec.get('train_data') or 'DeepScaleR-Preview-Dataset',
            'teacher': '',
            'unit': 'pp',
            'bench_span': '',
            'ckpt_select': 'best-every-100',
            'ood_basis': '',
            'ood': False,
        })
    return added


def _shao_aime25_plot_rows(have_scored: set[tuple]) -> list[dict]:
    added = []
    source = SHAO_PLOT_SOURCE
    train = 'DeepScaleR'
    for model, cells in SHAO_AIME25_PLOT.items():
        gt_final = cells['gt'][1]
        for key, code, method in SHAO_PLOT_METHODS:
            pair = (SHAO, model, code, 'AIME 2025', train, source)
            if pair in have_scored:
                continue
            base, score, gain = cells[key]
            is_gt = key == 'gt'
            added.append({
                'key': SHAO,
                'code': code,
                'method': method,
                'model': model,
                'bench': 'AIME 2025',
                'metric': 'avg@8',
                'base': base,
                'ref': score if is_gt else gt_final,
                'ref_method': 'GRPO',
                'score': score,
                'gain': gain,
                'gain_ref': None if is_gt else round(score - gt_final, 1),
                'source': source,
                'source_precision': 'plot',
                'train_data': train,
                'teacher': '',
                'unit': 'pp',
                'bench_span': '',
                'ckpt_select': SHAO_PLOT_CKPT_OVERRIDE.get(
                    (model, key), SHAO_PLOT_CKPT,
                ),
                'ood_basis': '',
                'ood': False,
            })
    return added
