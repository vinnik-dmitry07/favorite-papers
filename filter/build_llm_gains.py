'''Merge per-paper OOD gain extracts into llm_gains.jsonl and llm_gains.md.

    python filter/build_llm_gains.py
        renormalize existing jsonl and re-render markdown
    python filter/build_llm_gains.py --from-jsonl
        same
    python filter/build_llm_gains.py --extract-dir PATH
        merge extracts; refuse a missing/empty dir and refuse shrinking jsonl
'''

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

FILTER_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(FILTER_DIR))

import build_llm_models as blm  # noqa: E402
import llm_gains_ood as ood  # noqa: E402
from paths import (  # noqa: E402
    FILTER_DIR as ROOT,
    FULLTEXT_INDEX,
    PAPERS_JSONL,
    print_progress,
    read_jsonl,
    safe_key,
    write_jsonl,
)

REPO = ROOT.parent
JSONL_PATH = ROOT / 'llm_gains.jsonl'
MD_PATH = REPO / 'llm_gains.md'
MODELS_JSONL = ROOT / 'llm_models.jsonl'

SKIP_EXTRACT_NAMES = frozenset({
    'candidates.json',
    'not_applicable.json',
    'batches.json',
    'manifest.json',
    'INSTRUCTIONS.md',
})

MAX_ROWS = 45
MIN_CHECKPOINT_ROWS = 3
MAX_OTHER_COLS = 12
MAX_BATCH_TOKENS = 120_000
MAX_BATCH_PAPERS = 6

ROW_FIELDS = (
    'key',
    'code',
    'method',
    'model',
    'bench',
    'metric',
    'base',
    'ref',
    'ref_method',
    'score',
    'gain',
    'gain_ref',
    'source',
    'ood',
    'ood_basis',
    'ckpt_select',
    'train_data',
    'teacher',
    'unit',
    'bench_span',
)

FROM_SCRATCH_RE = re.compile(
    r'\b(pretrain|next-token|autoregressive|mlm|causal\s+lm)\b',
    re.I,
)
CONTINUED_PRETRAIN_RE = re.compile(
    r'\b(continual|continued|mid-?train)\b',
    re.I,
)
METHOD_CELL_LIMIT = 40
VANILLA_GRPO_RE = re.compile(r'^(online\s+)?grpo$', re.I)
BASE_CODES = frozenset({
    'base',
    'untrained',
    'untuned',
    'checkpoint',
    'pretrained',
    'starting',
})

CODE_ALIASES = {
    '1-shot RLVR (GRPO)': '1-shot RLVR',
    'DAPO (top-20% high-entropy tokens)': 'DAPO-top20%',
    'TTRL (GRPO)': 'TTRL',
    'E2H (GRPO + LoRA)': 'E2H',
    'LADDER (GRPO) + TTRL': 'LADDER+TTRL',
    'EM-FT / EM-RL': 'EM',
    'PPO / GRPO / Reinforce++ / RLOO / ReMax / DAPO (VeRL)': 'RL-suite',
    'RFT then DAPO': 'RFT+DAPO',
    'SFT + ScaleRL': 'SFT+ScaleRL',
    'SFT + OPD': 'SFT+OPD',
    'GRPO (random reward)': 'GRPO-random',
    'GRPO (incorrect reward)': 'GRPO-incorrect',
    'GRPO (ground-truth reward)': 'GRPO',
    'GRPO (format reward)': 'GRPO-format',
    'continual pretrain + Dr. GRPO': 'CPT+DrGRPO',
    'teacher top-K local support matching': 'top-K OPD',
    'RLVE (DAPO)': 'RLVE',
    'DrGRPO (RL mid-training)': 'DrGRPO-mid',
    'thinking SFT + DrGRPO (RL mid-training)': 'SFT(think) 10k + RLMT 5k + RLPT',
    'SFT+DrGRPO': 'SFT(think) 10k + RLMT 5k + RLPT',
    'online DPO / RF-NLL (Self-Improving Pretraining)': 'online-DPO',
    'SPADE (GRPO)': 'SPADE',
    'OPRD-Vanilla': 'OPRD',
    'OPRD-Bridge': 'OPRD-Bridge',
    'rStar-Math (4-round MCTS self-evolution + SFT)': 'rStar-Math',
    'SFT on Qwen2.5-Math-7B round-4 trajectories': 'rStar-SFT',
    'CoT (full) SFT': 'CoT-SFT',
    'PrefixLM + knowledge distillation': 'PrefixLM',
    'LoRA + TransformerFAM': 'TransformerFAM',
    'RPT (GRPO)': 'RPT',
    'Dr. Zero (HRPO proposer + GRPO solver)': 'Dr.Zero',
    'SSR (CWM-RL)': 'SSR',
    'baseline RL (CWM agentic SWE-RL)': 'CWM-RL',
    'PSV (RFT / expert iteration + difficulty-aware ICL proposer)': 'PSV',
    'iterative RFT': 'iter-RFT',
    'OPUT + SPD (DMax-Coder)': 'DMax-Coder',
    'OPUT + SPD (DMax-Math)': 'DMax-Math',
    'FLAN instruction tuning': 'FLAN',
    'Offline GRPO': 'Off-GRPO',
    'Online GRPO': 'GRPO',
    'Intuitor-Code': 'Intuitor-Code',
    '2-GRPO': '2-GRPO',
    'Critique-GRPO': 'Critique-GRPO',
    'GRPO-VPS': 'GRPO-VPS',
}

BENCH_SHORT = {
    'AIME 2024': 'AIME24',
    'AIME 2025': 'AIME25',
    'AIME26': 'AIME26',
    'AIME 2026': 'AIME26',
    'AMC 2023': 'AMC23',
    'AMC': 'AMC',
    'MATH-500': 'MATH500',
    'Minerva Math': 'Minerva',
    'OlympiadBench': 'Olymp',
    'Olympiad': 'Olymp',
    'GSM8K': 'GSM8K',
    'GPQA Diamond': 'GPQA-D',
    'GPQA': 'GPQA',
    'MMLU-Pro': 'MMLU-Pro',
    'LiveCodeBench': 'LCB',
    'LiveCodeBench v5': 'LCBv5',
    'LiveCodeBench v6': 'LCBv6',
    'HMMT 2025': 'HMMT25',
    'HMMT': 'HMMT',
}

BENCH_ORDER = (
    'AIME 2024',
    'AIME 2025',
    'AIME26',
    'AMC 2023',
    'MATH-500',
    'Minerva Math',
    'OlympiadBench',
    'HMMT 2025',
    'GSM8K',
    'GPQA Diamond',
    'MMLU-Pro',
    'LiveCodeBench',
    'LiveCodeBench v6',
)

BENCH_EXTRAS = {
    'aime26': 'AIME26',
    'aime 26': 'AIME26',
    'aime2026': 'AIME26',
    'aime 2026': 'AIME26',
    'hmmt 2025': 'HMMT 2025',
    'hmmt25': 'HMMT 2025',
    'olympiad': 'OlympiadBench',
    'amc': 'AMC 2023',
}

REF_PRIORITY = (
    ('GRPO', re.compile(r'^(online\s+)?grpo$', re.I)),
    ('Dr. GRPO', re.compile(r'^dr\.?\s*grpo$', re.I)),
    ('DAPO', re.compile(r'^dapo$', re.I)),
    ('PPO', re.compile(r'^ppo$', re.I)),
    ('RLOO', re.compile(r'^rloo$', re.I)),
    ('REINFORCE++', re.compile(r'^reinforce(\+\+|plusplus)$', re.I)),
)

MODEL_FIXES = (
    (re.compile(r'^Llama(\d)', re.I), r'Llama-\1'),
    (re.compile(r'DeepSeek-R1-Distill-Qwen(?=\d)'), 'DeepSeek-R1-Distill-Qwen-'),
    (re.compile(r'^Llama3\.2-3B-Instruct$', re.I), 'Llama-3.2-3B-Instruct'),
    (re.compile(r'^Llama3\.1-8B-Instruct$', re.I), 'Llama-3.1-8B-Instruct'),
)

MODEL_CANON = {
    'qwen 2.5 instruct': 'Qwen2.5-Instruct',
    'qwen2.5 instruct': 'Qwen2.5-Instruct',
    'llama 3.2 3b instruct': 'Llama-3.2-3B-Instruct',
    'llama 3.2 3b': 'Llama-3.2-3B',
    'llama 3.2': 'Llama-3.2-3B',
    'qwen2.5 math 7b base': 'Qwen2.5-Math-7B',
    'qwen3 14b base': 'Qwen3-14B-Base',
    'qwen3 32b base': 'Qwen3-32B-Base',
    'deepseek r1 distill 1.5b': 'DeepSeek-R1-Distill-Qwen-1.5B',
    'llama 3.1 instruct': 'Llama-3.1-Instruct',
    'llama 3.1 8b': 'Llama-3.1-8B',
    'olmo3 7b': 'OLMo-3-7B',
    'qwen3 4b instruct': 'Qwen3-4B-Instruct',
    'llama 2 chat': 'Llama-2-chat',
    'llama 2 1.4 billion parameter model': 'Llama-2-1.4B',
    'qwen2.5 7b deepseek r1 distilled': 'DeepSeek-R1-Distill-Qwen-7B',
    'qwen3 base': 'Qwen3-Base',
    'qwen3 4b base': 'Qwen3-4B-Base',
}

CORE_BENCHES = frozenset({
    'AIME 2024',
    'AIME 2025',
    'AIME26',
    'AMC 2023',
    'AMC',
    'MATH-500',
    'Minerva Math',
    'OlympiadBench',
    'Olympiad',
    'HMMT 2025',
    'HMMT',
    'GSM8K',
    'GPQA Diamond',
    'GPQA',
    'MMLU-Pro',
    'LiveCodeBench',
    'LiveCodeBench v5',
    'LiveCodeBench v6',
})


def load_json(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))


def fold_model(name: str | None, key: str = '') -> str:
    text = blm.norm_model(name) or ''
    for pattern, repl in MODEL_FIXES:
        text = pattern.sub(repl, text)
    text = MODEL_CANON.get(blm.alias_key(text), text)
    return ood.alias_paper_model(key, text)


def model_core(name: str) -> str:
    text = blm.alias_key(name)
    text = re.sub(r'\b\d+(?:\.\d+)?[bm]\b', '', text)
    return re.sub(r'\s+', ' ', text).strip()


def is_omitted_gain(row: dict) -> bool:
    return blm.is_omitted_row({
        'model': row.get('model') or '',
        'family': '',
        'generation': '',
        'variant': '',
        'start_point': '',
    })


def is_vanilla_grpo_name(text: str) -> bool:
    return bool(VANILLA_GRPO_RE.match((text or '').strip()))


def is_qualified_grpo_name(text: str) -> bool:
    blob = (text or '').strip()
    if not re.search(r'grpo', blob, re.I):
        return False
    if is_vanilla_grpo_name(blob):
        return False
    return bool(re.search(
        r'random|incorrect|format|spurious|r1|2-|sr-|sc-|critique|vps|'
        r'off-?|offline|dapo|i-?grpo',
        blob,
        re.I,
    ))


def resolve_gain_bench(text: str) -> str:
    resolved = blm.resolve_bench(text)
    spaced = blm.alias_key(resolved)
    compact = spaced.replace(' ', '')
    if spaced in BENCH_EXTRAS:
        return BENCH_EXTRAS[spaced]
    if compact in BENCH_EXTRAS:
        return BENCH_EXTRAS[compact]
    return resolved


def bench_short(name: str) -> str:
    return BENCH_SHORT.get(name, name.replace(' ', ''))


def method_to_code(method: str, explicit: str = '') -> str:
    explicit = blm.norm_space(explicit)
    text = blm.norm_space(method)
    if explicit and is_vanilla_grpo_name(explicit) and is_qualified_grpo_name(text):
        explicit = ''
    chosen = explicit or text
    if not chosen:
        return ''
    if chosen in CODE_ALIASES:
        return CODE_ALIASES[chosen]
    folded = blm.alias_key(chosen)
    for raw, code in CODE_ALIASES.items():
        if blm.alias_key(raw) == folded:
            return code
    if explicit:
        return explicit
    if len(text) <= METHOD_CELL_LIMIT:
        return text
    prefix = re.split(r'\s*\(|\s+/', text, maxsplit=1)[0].strip()
    if prefix and len(prefix) <= METHOD_CELL_LIMIT:
        return prefix
    return text[:METHOD_CELL_LIMIT]


def is_from_scratch_method(method: str) -> bool:
    blob = method or ''
    if CONTINUED_PRETRAIN_RE.search(blob):
        return False
    return bool(FROM_SCRATCH_RE.search(blob))


def is_base_code(code: str, method: str = '') -> bool:
    blob = f'{code} {method}'.strip().lower()
    return blob in BASE_CODES or (code or '').strip().lower() in BASE_CODES


def is_vanilla_grpo_ref(ref_method: str) -> bool:
    return bool(VANILLA_GRPO_RE.match((ref_method or '').strip()))


def parse_score(value) -> float | None:
    if value is None or value == '':
        return None
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    text = str(value).strip().replace('%', '').replace(',', '')
    if text.lower() in {'n/a', 'na', '-', '—', '–', 'none', 'null'}:
        return None
    try:
        return float(text)
    except ValueError:
        return None


def format_delta(score: float | None, baseline: float | None) -> str:
    if score is None or baseline is None:
        return ''
    return f'{round(score - baseline, 1):+.1f}'


def paper_id(key: str) -> str:
    if ':' in (key or ''):
        return key.split(':', 1)[1]
    return key or ''


def extract_json_paths(extract_dir: Path) -> list[Path]:
    return sorted(
        path for path in extract_dir.glob('*.json')
        if path.name not in SKIP_EXTRACT_NAMES
        and not path.name.startswith('batch_')
    )


def existing_row_count(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for line in path.read_text(encoding='utf-8').splitlines() if line.strip())


def existing_keys(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return {row.get('key') for row in read_jsonl(path) if row.get('key')}


def refuse_shrink(existing_n: int, new_n: int, force: bool) -> bool:
    return existing_n > 0 and new_n < existing_n and not force


def refuse_shrink_keys(old_keys: set[str], new_keys: set[str], force: bool) -> bool:
    return bool(old_keys) and len(new_keys) < len(old_keys) and not force


def refuse_output_shrink(
    path: Path,
    rows: list[dict],
    force: bool,
) -> bool:
    new_keys = {row.get('key') for row in rows if row.get('key')}
    if refuse_shrink(existing_row_count(path), len(rows), force):
        print(
            f'refusing to shrink {path}: {existing_row_count(path)} -> {len(rows)} '
            f'(pass --force to override)',
            flush=True,
        )
        return True
    old_keys = existing_keys(path)
    if refuse_shrink_keys(old_keys, new_keys, force):
        print(
            f'refusing to shrink keys in {path}: {len(old_keys)} -> {len(new_keys)} '
            f'(pass --force to override)',
            flush=True,
        )
        return True
    return False


def require_extract_dir(extract_dir: Path) -> list[Path] | None:
    if not extract_dir.is_dir():
        print(f'extract dir missing: {extract_dir}', flush=True)
        print('use --from-jsonl to re-render, or pass --extract-dir PATH', flush=True)
        return None
    paths = extract_json_paths(extract_dir)
    if not paths:
        print(f'extract dir empty: {extract_dir}', flush=True)
        return None
    return paths


def is_trained_ood_open(row: dict) -> bool:
    return (
        (row.get('role') or '') == 'trained'
        and bool(row.get('eval_ood'))
        and bool(row.get('model'))
        and not blm.is_omitted_row(row)
    )


def fulltext_rel(key: str, index_row: dict | None) -> str:
    if index_row and index_row.get('path'):
        path = Path(index_row['path'])
        if path.suffix == '.md':
            try:
                return path.as_posix() if 'fulltext' in path.as_posix() else f'filter/fulltext/{path.name}'
            except ValueError:
                return f'filter/fulltext/{safe_key(key)}.md'
    return f'filter/fulltext/{safe_key(key)}.md'


def iter_candidates(
    model_rows: list[dict],
    index_by_key: dict[str, dict] | None = None,
) -> tuple[list[dict], list[dict]]:
    index_by_key = index_by_key or {}
    by_key: dict[str, list[dict]] = defaultdict(list)
    for row in model_rows:
        if is_trained_ood_open(row):
            by_key[row['key']].append(row)
    candidates = []
    skipped = []
    for key, recs in by_key.items():
        methods = [row.get('method') or '' for row in recs]
        title = recs[0].get('title') or ''
        section = recs[0].get('section') or ''
        if methods and all(is_from_scratch_method(method) for method in methods):
            skipped.append({
                'key': key,
                'title': title,
                'section': section,
                'reason': 'from-scratch only; no untrained checkpoint',
                'methods': blm.unique(methods),
            })
            continue
        index_row = index_by_key.get(key) or {}
        candidates.append({
            'key': key,
            'title': title,
            'section': section,
            'safe_key': safe_key(key),
            'n_tokens': index_row.get('n_tokens') or 0,
            'rel_path': fulltext_rel(key, index_row),
            'expected': [
                {
                    'model': fold_model(row.get('model'), key),
                    'method': row.get('method') or '',
                    'eval_ood': list(row.get('eval_ood') or []),
                    'eval_id': list(row.get('eval_id') or []),
                }
                for row in recs
            ],
        })
    return candidates, skipped


def pack_batches(
    candidates: list[dict],
    max_tokens: int = MAX_BATCH_TOKENS,
    max_papers: int = MAX_BATCH_PAPERS,
) -> list[list[dict]]:
    ordered = sorted(
        candidates,
        key=lambda item: (-(item.get('n_tokens') or 0), item.get('key') or ''),
    )
    batches: list[list[dict]] = []
    current: list[dict] = []
    used = 0
    for item in ordered:
        tokens = item.get('n_tokens') or 0
        if current and (used + tokens > max_tokens or len(current) >= max_papers):
            batches.append(current)
            current = []
            used = 0
        current.append(item)
        used += tokens
    if current:
        batches.append(current)
    return batches


def load_index_by_key() -> dict[str, dict]:
    return {row['key']: row for row in read_jsonl(FULLTEXT_INDEX) if row.get('key')}


def normalize_gain_row(raw: dict) -> dict | None:
    key = blm.norm_space(raw.get('key') or '')
    model = fold_model(raw.get('model'), key)
    bench = resolve_gain_bench(raw.get('bench') or '')
    method = blm.norm_space(raw.get('method') or '')
    code = method_to_code(method, raw.get('code') or '')
    if not key or not model or not bench:
        return None
    base = parse_score(raw.get('base'))
    ref = parse_score(raw.get('ref'))
    score = parse_score(raw.get('score'))
    gain = parse_score(raw.get('gain'))
    gain_ref = parse_score(raw.get('gain_ref'))
    unit = blm.norm_space(raw.get('unit') or '').lower()
    if unit not in {'pp', 'frac', ''}:
        unit = ''
    ood_basis = blm.norm_space(raw.get('ood_basis') or '')
    if ood_basis not in ood.OOD_BASES:
        ood_basis = ''
    ood_raw = raw.get('ood')
    if isinstance(ood_raw, str):
        ood_val = ood_raw.strip().lower() in {'1', 'true', 'yes'}
    elif ood_raw is None:
        ood_val = ood_basis == 'temporal'
    else:
        ood_val = bool(ood_raw)
    if ood_val and not ood_basis:
        ood_basis = 'temporal'
    return {
        'key': key,
        'code': code,
        'method': method,
        'model': model,
        'bench': bench,
        'metric': blm.norm_space(raw.get('metric') or ''),
        'base': base,
        'ref': ref,
        'ref_method': blm.norm_space(raw.get('ref_method') or ''),
        'score': score,
        'gain': gain,
        'gain_ref': gain_ref,
        'source': blm.norm_space(raw.get('source') or ''),
        'ood': ood_val,
        'ood_basis': ood_basis,
        'ckpt_select': ood.default_ckpt_select(
            key, blm.norm_space(raw.get('ckpt_select') or ''),
        ),
        'train_data': blm.norm_space(raw.get('train_data') or ''),
        'teacher': ood.default_teacher(
            key, code, method, blm.norm_space(raw.get('teacher') or ''),
        ),
        'unit': unit,
        'bench_span': blm.norm_space(raw.get('bench_span') or ''),
    }


def extract_rows_from_payload(payload) -> list[dict]:
    if isinstance(payload, list):
        return [item for item in payload if isinstance(item, dict)]
    if isinstance(payload, dict):
        rows = payload.get('rows')
        if isinstance(rows, list):
            return [item for item in rows if isinstance(item, dict)]
        if payload.get('key') or payload.get('model'):
            return [payload]
    return []


def key_from_stem(stem: str, known_keys: set[str] | None = None) -> str:
    known_keys = known_keys or set()
    for key in known_keys:
        if safe_key(key) == stem:
            return key
    if stem.startswith('arxiv_'):
        return 'arxiv:' + stem[6:]
    if stem.startswith('acl_'):
        return 'acl:' + stem[4:]
    if stem.startswith('openreview_'):
        return 'openreview:' + stem[11:]
    if stem.startswith('doi_'):
        return 'doi:' + stem[4:].replace('_', '/')
    return ''


def load_extracts(
    extract_dir: Path,
    known_keys: set[str] | None = None,
) -> dict[str, list[dict]]:
    known_keys = set(known_keys or [])
    by_key: dict[str, list[dict]] = {}
    paths = extract_json_paths(extract_dir)
    for i, path in enumerate(paths, start=1):
        try:
            payload = load_json(path)
        except (OSError, json.JSONDecodeError) as exc:
            print(f'bad extract {path.name}: {exc}', flush=True)
            print_progress(i, len(paths), path.name)
            continue
        file_key = key_from_stem(path.stem, known_keys)
        if not file_key and isinstance(payload, dict):
            file_key = blm.norm_space(payload.get('key') or '')
        rows = extract_rows_from_payload(payload)
        if not rows:
            if file_key:
                by_key.setdefault(file_key, [])
            print_progress(i, len(paths), path.name)
            continue
        for raw in rows:
            item = dict(raw)
            key = blm.norm_space(item.get('key') or '') or file_key
            if not key:
                continue
            item['key'] = key
            by_key.setdefault(key, []).append(item)
        print_progress(i, len(paths), path.name)
    return by_key


def _bench_set(values) -> set[str]:
    return {resolve_gain_bench(item) for item in values or [] if item}


def build_ood_index(model_rows: list[dict]) -> dict[tuple[str, str], dict]:
    index: dict[tuple[str, str], dict] = {}
    for row in model_rows:
        if not row.get('model') or not row.get('key'):
            continue
        if blm.is_omitted_row(row):
            continue
        pair = (row['key'], fold_model(row['model'], row['key']))
        slot = index.setdefault(pair, {
            'ood': set(),
            'id': set(),
            'train': set(),
            'by_method': {},
        })
        ood = _bench_set(row.get('eval_ood'))
        ids = _bench_set(row.get('eval_id'))
        train = set(row.get('train_data') or [])
        slot['ood'].update(ood)
        slot['id'].update(ids)
        slot['train'].update(train)
        method = blm.norm_space(row.get('method') or '')
        if method:
            mslot = slot['by_method'].setdefault(
                method, {'ood': set(), 'id': set(), 'train': set()},
            )
            mslot['ood'].update(ood)
            mslot['id'].update(ids)
            mslot['train'].update(train)
    return index


def resolve_index_pair(
    index: dict[tuple[str, str], dict],
    key: str,
    model: str,
) -> tuple[str, str] | None:
    if (key, model) in index:
        return (key, model)
    folded = blm.alias_key(model)
    core = model_core(model)
    names = [name for pair_key, name in index if pair_key == key]
    exact = [name for name in names if blm.alias_key(name) == folded]
    if len(exact) == 1:
        return (key, exact[0])
    cores = [name for name in names if model_core(name) == core and core]
    if len(cores) == 1:
        return (key, cores[0])
    contains = [
        name for name in names
        if folded in blm.alias_key(name) or blm.alias_key(name) in folded
    ]
    if len(contains) == 1:
        return (key, contains[0])
    return None


def pick_method_slot(slot: dict, method: str) -> dict:
    by_method = slot.get('by_method') or {}
    if not method or not by_method:
        return slot
    if method in by_method:
        return by_method[method]
    folded = blm.alias_key(method)
    code = method_to_code(method)
    hits = []
    for name, mslot in by_method.items():
        if blm.alias_key(name) == folded:
            hits.append(mslot)
        elif code and method_to_code(name) == code:
            hits.append(mslot)
    if len(hits) == 1:
        return hits[0]
    return slot


def lookup_ood_slot(
    index: dict[tuple[str, str], dict],
    key: str,
    model: str,
    method: str = '',
) -> dict | None:
    pair = resolve_index_pair(index, key, model)
    if pair is None:
        return None
    return pick_method_slot(index[pair], method)


def attach_train_data(rows: list[dict], model_rows: list[dict]) -> list[dict]:
    index = build_ood_index(model_rows)
    out = []
    for row in rows:
        item = dict(row)
        if item.get('train_data'):
            out.append(item)
            continue
        slot = lookup_ood_slot(
            index, item['key'], item['model'], item.get('method') or '',
        )
        trains = sorted(slot.get('train') or set()) if slot else []
        if len(trains) == 1:
            item['train_data'] = trains[0]
        out.append(item)
    return out


def classify_row(row: dict, slot: dict | None) -> str:
    ids = (slot or {}).get('id') or set()
    oods = (slot or {}).get('ood') or set()
    bench = row['bench']
    return ood.classify_ood_basis(
        key=row['key'],
        model=row['model'],
        bench=bench,
        code=row.get('code') or '',
        method=row.get('method') or '',
        train_data=row.get('train_data') or '',
        teacher=row.get('teacher') or '',
        bench_span=row.get('bench_span') or '',
        listed_id=bench in ids,
        listed_ood=bench in oods,
        hmmt_month=ood.PAPER_HMMT_MONTH.get(row['key']),
    )


def attach_ood(rows: list[dict], model_rows: list[dict]) -> list[dict]:
    index = build_ood_index(model_rows)
    out = []
    unmatched = 0
    n_temporal = 0
    for row in rows:
        item = dict(row)
        slot = lookup_ood_slot(
            index, item['key'], item['model'], item.get('method') or '',
        )
        if slot is None:
            unmatched += 1
        item['ood_basis'] = classify_row(item, slot)
        item['ood'] = item['ood_basis'] == 'temporal'
        item['ckpt_select'] = ood.default_ckpt_select(
            item['key'], item.get('ckpt_select') or '',
        )
        if item['ood']:
            n_temporal += 1
        out.append(item)
    print(
        f'ood attach: rows={len(out)} unmatched_models={unmatched} '
        f'temporal={n_temporal}',
        flush=True,
    )
    return out


SCORE_FIELDS = ('base', 'ref', 'score', 'gain', 'gain_ref')


def row_numeric_fields(row: dict) -> list[float]:
    return [row[field] for field in SCORE_FIELDS if row.get(field) is not None]


def row_looks_fraction(row: dict) -> bool:
    nums = [
        row[field] for field in ('base', 'ref', 'score')
        if row.get(field) is not None
    ]
    if not nums:
        return False
    if max(abs(value) for value in nums) > 1.0:
        return False
    if min(value for value in nums) < 0:
        return False
    return True


def coerce_pp_rows(rows: list[dict]) -> list[dict]:
    out = []
    n_scaled = 0
    for row in rows:
        item = dict(row)
        nums = [
            item[field] for field in ('base', 'ref', 'score')
            if item.get(field) is not None
        ]
        mixed = bool(nums) and min(abs(v) for v in nums) <= 1.0 and max(abs(v) for v in nums) > 1.5
        if mixed:
            print(
                f'mixed-scale row {item["key"]} {item["model"]} {item["bench"]} '
                f'left as-is',
                flush=True,
            )
        elif item.get('unit') == 'frac' or row_looks_fraction(item):
            for field in SCORE_FIELDS:
                if item.get(field) is not None:
                    item[field] = item[field] * 100.0
            item['unit'] = 'pp'
            n_scaled += 1
        elif item.get('unit') != 'frac':
            item['unit'] = item.get('unit') or 'pp'
        out.append(item)
    if n_scaled:
        print(f'rescaled {n_scaled} fraction rows x100', flush=True)
    return out


def rescale_unit_papers(rows: list[dict]) -> list[dict]:
    return coerce_pp_rows(rows)


def ref_rank(code: str, method: str) -> tuple[int, str] | None:
    if is_qualified_grpo_name(code) or is_qualified_grpo_name(method):
        return None
    for i, (name, pattern) in enumerate(REF_PRIORITY):
        if pattern.match((code or '').strip()) or pattern.match((method or '').strip()):
            return i, name
    return None


def experiment_key(row: dict) -> tuple:
    return (
        row['key'],
        row['model'],
        row['bench'],
        row.get('metric') or '',
        row.get('train_data') or '',
        row.get('source') or '',
    )


def fill_baselines(rows: list[dict]) -> list[dict]:
    groups: dict[tuple, list[dict]] = defaultdict(list)
    for row in rows:
        groups[experiment_key(row)].append(row)
    out = []
    for group in groups.values():
        bases = []
        for row in group:
            if row.get('base') is not None:
                bases.append(row['base'])
            elif (
                is_base_code(row.get('code') or '', row.get('method') or '')
                and row.get('score') is not None
            ):
                bases.append(row['score'])
        unique_bases = {round(value, 6) for value in bases}
        if len(unique_bases) == 1:
            shared_base = bases[0]
        else:
            if len(unique_bases) > 1:
                sample = group[0]
                print(
                    f'conflicting bases {sample["key"]} {sample["model"]} '
                    f'{sample["bench"]} {sample.get("metric") or ""}: {sorted(unique_bases)}',
                    flush=True,
                )
            shared_base = None
        ranked = []
        for row in group:
            if is_base_code(row.get('code') or '', row.get('method') or ''):
                continue
            hit = ref_rank(row.get('code') or '', row.get('method') or '')
            if hit and row.get('score') is not None:
                ranked.append((hit[0], row.get('code') or '', hit[1], row['score']))
        ranked.sort()
        shared_ref = ranked[0][3] if ranked else None
        shared_ref_method = ranked[0][2] if ranked else ''
        for row in group:
            item = dict(row)
            if item.get('base') is None and shared_base is not None:
                item['base'] = shared_base
            if item.get('ref') is None and shared_ref is not None:
                item['ref'] = shared_ref
                if not item.get('ref_method'):
                    item['ref_method'] = shared_ref_method
            out.append(item)
    return out


def delta_over_base(row: dict) -> float | None:
    if row.get('score') is not None and row.get('base') is not None:
        return row['score'] - row['base']
    return row.get('gain')


def delta_over_ref(row: dict) -> float | None:
    if row.get('score') is not None and row.get('ref') is not None:
        return row['score'] - row['ref']
    return row.get('gain_ref')


def format_gain_cell(
    delta: float | None,
    starred: bool = False,
    dagger: bool = False,
) -> str:
    if delta is None:
        return ''
    text = f'{round(delta, 1):+.1f}'
    if dagger:
        text += '†'
    if starred:
        text += '*'
    return text


def fold_ref_name(text: str) -> str:
    return re.sub(r'[^a-z0-9]', '', (text or '').lower())


def is_self_ref(row: dict) -> bool:
    ref_method = (row.get('ref_method') or '').strip()
    if not ref_method:
        return False
    code = row.get('code') or ''
    method = row.get('method') or ''
    if is_vanilla_grpo_name(ref_method) and is_vanilla_grpo_name(code):
        return True
    if blm.alias_key(ref_method) in {blm.alias_key(code), blm.alias_key(method)}:
        return True
    folded = fold_ref_name(ref_method)
    return bool(folded) and folded in {fold_ref_name(code), fold_ref_name(method)}


def dedupe_rows(rows: list[dict]) -> list[dict]:
    best: dict[tuple, dict] = {}
    for row in rows:
        pair = (
            row['key'],
            row['code'],
            row['model'],
            row['bench'],
            row.get('metric') or '',
            row.get('train_data') or '',
            row.get('source') or '',
        )
        prev = best.get(pair)
        if prev is None:
            best[pair] = row
            continue
        prev_n = sum(prev.get(field) is not None for field in ('base', 'ref', 'score', 'gain'))
        new_n = sum(row.get(field) is not None for field in ('base', 'ref', 'score', 'gain'))
        if new_n >= prev_n:
            best[pair] = row
    return list(best.values())


def sort_benches(names: list[str], coverage: dict[str, int]) -> list[str]:
    rank = {name: i for i, name in enumerate(BENCH_ORDER)}
    return sorted(
        names,
        key=lambda name: (-coverage.get(name, 0), rank.get(name, 1000), name),
    )


def model_variant_bucket(model: str) -> str:
    lowered = model.lower()
    if 'instruct' in lowered:
        return 'Instruct'
    if re.search(r'\bbase\b', lowered) or lowered.endswith('-base'):
        return 'Base'
    if 'distill' in lowered:
        return 'Distill'
    if 'math' in lowered:
        return 'Math'
    return 'other'


def split_row_groups(groups: list[list[dict]], cap: int = MAX_ROWS) -> list[tuple[str, list[list[dict]]]]:
    if len(groups) <= cap:
        return [('', groups)]
    buckets: dict[str, list[list[dict]]] = defaultdict(list)
    for group in groups:
        model = group[0]['model']
        buckets[model_variant_bucket(model)].append(group)
    if len(buckets) > 1 and all(len(items) <= cap for items in buckets.values()):
        return [(f'{name}', items) for name, items in buckets.items() if items]
    out = []
    for i in range(0, len(groups), cap):
        suffix = chr(ord('a') + i // cap) if len(groups) > cap else ''
        out.append((suffix, groups[i:i + cap]))
    return out


def code_cell(row: dict) -> str:
    url = blm.paper_url(row['key'])
    return blm.md_link(
        row['code'] or row['method'] or row['key'],
        url,
        limit=METHOD_CELL_LIMIT,
    )


def metric_cell(group: list[dict]) -> str:
    return blm.md_escape(group[0].get('metric') or '')


def pivot_groups(rows: list[dict]) -> list[list[dict]]:
    grouped: dict[tuple, list[dict]] = defaultdict(list)
    for row in rows:
        grouped[(
            row['key'],
            row['code'],
            row['model'],
            row.get('metric') or '',
            row.get('train_data') or '',
            row.get('source') or '',
        )].append(row)
    return list(grouped.values())


def filled_benches(groups: list[list[dict]], cell_fn) -> list[str]:
    coverage: dict[str, int] = defaultdict(int)
    names = set()
    for group in groups:
        seen = set()
        for row in group:
            if row['bench'] not in CORE_BENCHES:
                continue
            if cell_fn(row):
                names.add(row['bench'])
                if row['bench'] not in seen:
                    coverage[row['bench']] += 1
                    seen.add(row['bench'])
    return sort_benches(list(names), coverage)


def render_checkpoint_table(
    title: str,
    groups: list[list[dict]],
    cell_fn,
    extra_headers: list[str] | None = None,
    extra_fn=None,
) -> tuple[list[str], int, int]:
    extra_headers = extra_headers or []
    benches = filled_benches(groups, cell_fn)
    if not benches or not groups:
        return [], 0, 0
    headers = ['method', 'id', 'metric'] + extra_headers + [
        bench_short(name) for name in benches
    ]
    lines = [
        f'### {title}',
        '',
        '| ' + ' | '.join(headers) + ' |',
        '|' + '|'.join('---' for _ in headers) + '|',
    ]
    for group in groups:
        row0 = group[0]
        by_bench = {row['bench']: row for row in group}
        cells = [code_cell(row0), paper_id(row0['key']), metric_cell(group)]
        if extra_fn:
            cells.append(extra_fn(group))
        for bench in benches:
            hit = by_bench.get(bench)
            cells.append(cell_fn(hit) if hit else '')
        lines.append('| ' + ' | '.join(cells) + ' |')
    lines.append('')
    return lines, len(groups), len(benches)


def render_other_table(
    title: str,
    groups: list[list[dict]],
    cell_fn,
    extra_headers: list[str] | None = None,
    extra_fn=None,
) -> tuple[list[str], int, int]:
    extra_headers = extra_headers or []
    columns = []
    coverage: dict[str, int] = defaultdict(int)
    for group in groups:
        for row in group:
            if row['bench'] not in CORE_BENCHES or not cell_fn(row):
                continue
            col = f'{row["model"]} · {bench_short(row["bench"])}'
            columns.append(col)
            coverage[col] += 1
    names = sorted(set(columns), key=lambda name: (-coverage[name], name))
    if not names or not groups:
        return [], 0, 0
    chunks = [names[i:i + MAX_OTHER_COLS] for i in range(0, len(names), MAX_OTHER_COLS)]
    lines = []
    n_rows = 0
    for i, chunk in enumerate(chunks):
        label = title if len(chunks) == 1 else f'{title} ({i + 1})'
        headers = ['method', 'id', 'metric'] + extra_headers + chunk
        lines.append(f'### {label}')
        lines.append('')
        lines.append('| ' + ' | '.join(headers) + ' |')
        lines.append('|' + '|'.join('---' for _ in headers) + '|')
        used_groups = []
        for group in groups:
            by_col = {}
            for row in group:
                if row['bench'] not in CORE_BENCHES:
                    continue
                col = f'{row["model"]} · {bench_short(row["bench"])}'
                if col in chunk and cell_fn(row):
                    by_col[col] = row
            if not by_col:
                continue
            used_groups.append(group)
            row0 = group[0]
            cells = [code_cell(row0), paper_id(row0['key']), metric_cell(group)]
            if extra_fn:
                cells.append(extra_fn(group))
            for col in chunk:
                hit = by_col.get(col)
                cells.append(cell_fn(hit) if hit else '')
            lines.append('| ' + ' | '.join(cells) + ' |')
        n_rows += len(used_groups)
        lines.append('')
    return lines, n_rows, len(names)


def order_groups(groups: list[list[dict]], papers: list[dict]) -> list[list[dict]]:
    rank = {paper['key']: i for i, paper in enumerate(papers)}
    return sorted(
        groups,
        key=lambda group: (
            rank.get(group[0]['key'], 10**6),
            group[0].get('code') or '',
            group[0].get('model') or '',
        ),
    )


def ref_cell(group: list[dict]) -> str:
    for row in group:
        if row.get('ref_method'):
            return blm.md_escape(row['ref_method'])
    return ''


def starred_ref(row: dict) -> bool:
    return bool(row.get('ref_method')) and not is_vanilla_grpo_ref(row['ref_method'])


def best_ckpt_mark(row: dict) -> bool:
    return (row.get('ckpt_select') or '') == 'best-every-100'


def base_cell(row: dict) -> str:
    return format_gain_cell(delta_over_base(row), dagger=best_ckpt_mark(row))


def grpo_cell(row: dict) -> str:
    return format_gain_cell(
        delta_over_ref(row),
        starred=starred_ref(row),
        dagger=best_ckpt_mark(row),
    )


def group_has_cell(group: list[dict], cell_fn) -> bool:
    return any(cell_fn(row) for row in group)


def print_table_stats(label: str, title: str, n_rows: int, n_cols: int) -> None:
    print(f'table {label} / {title}: rows={n_rows} cols={n_cols}', flush=True)


def is_temporal_row(row: dict) -> bool:
    if row.get('ood_basis'):
        return row['ood_basis'] == 'temporal'
    return bool(row.get('ood'))


def table_gain_rows(rows: list[dict], skip_self_ref: bool = False) -> list[dict]:
    usable = [
        row for row in rows
        if is_temporal_row(row)
        and not is_base_code(row.get('code') or '', row.get('method') or '')
        and row.get('bench') in CORE_BENCHES
        and not is_omitted_gain(row)
    ]
    if skip_self_ref:
        return [row for row in usable if not is_self_ref(row)]
    return usable


def render_section(
    heading: str,
    legend: str,
    rows: list[dict],
    papers: list[dict],
    cell_fn,
    extra_headers: list[str] | None = None,
    extra_fn=None,
    skip_self_ref: bool = False,
) -> list[str]:
    usable = table_gain_rows(rows, skip_self_ref=skip_self_ref)
    groups = [
        group for group in pivot_groups(usable)
        if group_has_cell(group, cell_fn)
    ]
    groups = order_groups(groups, papers)
    by_model: dict[str, list[list[dict]]] = defaultdict(list)
    for group in groups:
        by_model[group[0]['model']].append(group)
    own = {
        model: items for model, items in by_model.items()
        if len(items) >= MIN_CHECKPOINT_ROWS
    }
    other = [
        group for model, items in by_model.items()
        if len(items) < MIN_CHECKPOINT_ROWS
        for group in items
    ]
    out = [f'## {heading}', '', legend, '']
    for model in sorted(own, key=lambda name: (-len(own[name]), name)):
        for suffix, chunk in split_row_groups(own[model]):
            title = model if not suffix else f'{model} ({suffix})'
            lines, n_rows, n_cols = render_checkpoint_table(
                title, chunk, cell_fn, extra_headers, extra_fn,
            )
            out.extend(lines)
            print_table_stats(heading, title, n_rows, n_cols)
    if other:
        for suffix, chunk in split_row_groups(other):
            title = 'Other checkpoints' if not suffix else f'Other checkpoints ({suffix})'
            lines, n_rows, n_cols = render_other_table(
                title, chunk, cell_fn, extra_headers, extra_fn,
            )
            out.extend(lines)
            print_table_stats(heading, title, n_rows, n_cols)
    if len(out) == 4:
        out.append('_No numeric OOD cells._')
        out.append('')
    return out


def missing_baseline_report(rows: list[dict]) -> tuple[list[str], list[str]]:
    usable = [
        row for row in table_gain_rows(rows)
        if row.get('score') is not None or row.get('gain') is not None
    ]
    no_base = []
    no_ref = []
    for row in usable:
        label = f'{row["key"]} {row["code"]} {row["model"]} {row["bench"]}'
        if delta_over_base(row) is None:
            no_base.append(label)
        if delta_over_ref(row) is None and not is_self_ref(row):
            no_ref.append(label)
    return no_base, no_ref


def render_md(
    rows: list[dict],
    papers: list[dict],
    not_applicable: list[dict],
) -> str:
    base_rows = table_gain_rows(rows)
    ref_rows = table_gain_rows(rows, skip_self_ref=True)
    keys = {row['key'] for row in base_rows} | {row['key'] for row in ref_rows}
    n_cells_base = sum(1 for row in base_rows if delta_over_base(row) is not None)
    n_cells_ref = sum(1 for row in ref_rows if delta_over_ref(row) is not None)
    out = [
        '# Compact OOD gains',
        '',
        'Per-paper numbers from `filter/fulltext/*.md`, stored in '
        '`filter/llm_gains.jsonl`. One jsonl row is one '
        '(paper × method × model × bench × train data × source table). '
        'Markdown keeps only **temporal OOD**: the bench date is after the '
        'full training-chain cutoff. Historical benches and version-only LCB '
        'slices stay in the jsonl as `rl_stage` / `id` / `unverified` and are '
        'not drawn. API and GPT-family models are omitted. '
        'Model inventory: [`llm_models.md`](llm_models.md).',
        '',
        '## Summary',
        '',
        f'- Papers with at least one temporal OOD number: **{len(keys)}**',
        f'- Temporal gain cells vs starting checkpoint: **{n_cells_base}**',
        f'- Temporal gain cells vs GRPO / nearest RLVR: **{n_cells_ref}**',
        f'- From-scratch papers (no starting checkpoint): **{len(not_applicable)}**',
        '',
    ]
    out.extend(render_section(
        'Gain over the starting checkpoint',
        'Cell = method − the paper\'s starting checkpoint (pretrained, instruct, '
        'or distilled), percentage points, one decimal. '
        '`avg@k` is not `pass@k`. A trailing `†` means the paper picked the '
        'best checkpoint (ConSPO: eval every 100 steps). '
        'Blank if that paper does not report the starting checkpoint on that bench. '
        'Numbers stay inside one experiment (same table, train data, and metric).',
        rows,
        papers,
        base_cell,
    ))
    out.extend(render_section(
        'Gain over GRPO',
        'Cell = method − the paper\'s vanilla GRPO, or the nearest vanilla RLVR '
        'baseline when GRPO is absent (`vs` column). A trailing `*` means the '
        'reference is not vanilla GRPO (Dr. GRPO, DAPO, PPO, RLOO, REINFORCE++). '
        '`†` is a best-every-100 checkpoint. The reference method itself is '
        'omitted. Equal scores of different methods show `+0.0`. '
        'Blank if no RLVR baseline is reported on that bench. '
        'Same experiment only.',
        rows,
        papers,
        grpo_cell,
        extra_headers=['vs'],
        extra_fn=ref_cell,
        skip_self_ref=True,
    ))
    out.append('## Not applicable')
    out.append('')
    if not not_applicable:
        out.append('None.')
        out.append('')
        return '\n'.join(out)
    out.append(
        'Trained open models with an OOD list, but only from-scratch pretraining '
        '(`pretrain` / `next-token` / `autoregressive` / `MLM` / `causal LM`). '
        'Continued / mid-training pretrain is not from-scratch. '
        'There is no starting checkpoint to subtract.'
    )
    out.append('')
    out.append('| id | paper | methods |')
    out.append('|---|---|---|')
    rank = {paper['key']: i for i, paper in enumerate(papers)}
    for item in sorted(not_applicable, key=lambda rec: rank.get(rec['key'], 10**6)):
        url = blm.paper_url(item['key'])
        title = blm.md_link(item.get('title') or item['key'], url, limit=48)
        methods = blm.md_escape(', '.join(item.get('methods') or [])[:80])
        out.append(f'| {paper_id(item["key"])} | {title} | {methods} |')
    out.append('')
    return '\n'.join(out)


def renormalize_rows(rows: list[dict], model_rows: list[dict]) -> list[dict]:
    out = []
    for raw in rows:
        item = normalize_gain_row(raw)
        if item:
            out.append(item)
    out = ood.apply_gain_overrides(out)
    out = attach_train_data(out, model_rows)
    out = coerce_pp_rows(out)
    out = attach_ood(out, model_rows)
    out = fill_baselines(out)
    return dedupe_rows(out)


def write_outputs(
    rows: list[dict],
    papers: list[dict],
    not_applicable: list[dict],
) -> None:
    write_jsonl(JSONL_PATH, rows)
    print(f'wrote {len(rows)} rows -> {JSONL_PATH}', flush=True)
    markdown = render_md(rows, papers, not_applicable)
    tmp = MD_PATH.with_suffix(MD_PATH.suffix + '.tmp')
    tmp.write_text(markdown, encoding='utf-8')
    tmp.replace(MD_PATH)
    print(f'wrote {MD_PATH} ({len(markdown.splitlines())} lines)', flush=True)
    no_base, no_ref = missing_baseline_report(rows)
    print(f'score rows lacking base: {len(no_base)}', flush=True)
    for label in no_base[:40]:
        print(f'  base {label}', flush=True)
    if len(no_base) > 40:
        print(f'  ... {len(no_base) - 40} more', flush=True)
    print(f'score rows lacking ref: {len(no_ref)}', flush=True)
    for label in no_ref[:40]:
        print(f'  ref {label}', flush=True)
    if len(no_ref) > 40:
        print(f'  ... {len(no_ref) - 40} more', flush=True)


def sort_rows(rows: list[dict], papers: list[dict]) -> list[dict]:
    rank = {paper['key']: i for i, paper in enumerate(papers)}
    return sorted(
        rows,
        key=lambda row: (
            rank.get(row['key'], 10**6),
            row.get('model') or '',
            row.get('code') or '',
            row.get('bench') or '',
            row.get('metric') or '',
            row.get('train_data') or '',
            row.get('source') or '',
        ),
    )


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Merge OOD gain extracts or re-render llm_gains.md',
    )
    parser.add_argument(
        'extract_dir_pos',
        nargs='?',
        type=Path,
        help='extract directory (same as --extract-dir)',
    )
    parser.add_argument('--extract-dir', type=Path)
    parser.add_argument(
        '--from-jsonl',
        action='store_true',
        help='renormalize filter/llm_gains.jsonl and re-render markdown',
    )
    parser.add_argument(
        '--force',
        action='store_true',
        help='allow writing fewer jsonl rows than the current file',
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    extract_dir = args.extract_dir or args.extract_dir_pos
    papers = read_jsonl(PAPERS_JSONL)
    model_rows = read_jsonl(MODELS_JSONL)
    _, not_applicable = iter_candidates(model_rows, load_index_by_key())

    if extract_dir is None:
        if not JSONL_PATH.exists():
            print(
                f'missing {JSONL_PATH}; pass --extract-dir PATH to merge',
                flush=True,
            )
            return 1
        print(f'renormalizing {JSONL_PATH}', flush=True)
        rows = renormalize_rows(read_jsonl(JSONL_PATH), model_rows)
        if refuse_output_shrink(JSONL_PATH, rows, args.force):
            return 1
        rows = sort_rows(rows, papers)
        write_outputs(rows, papers, not_applicable)
        return 0

    paths = require_extract_dir(extract_dir)
    if paths is None:
        return 1

    print(f'loading extracts from {extract_dir}', flush=True)
    candidate_path = extract_dir / 'candidates.json'
    if not candidate_path.exists():
        print(f'warning: no {candidate_path.name}; coverage check skipped', flush=True)
    candidates = load_json(candidate_path) if candidate_path.exists() else []
    known = {paper['key'] for paper in papers if paper.get('key')}
    known.update(item['key'] for item in candidates if item.get('key'))
    raw_by_key = load_extracts(extract_dir, known)
    want_keys = [item['key'] for item in candidates] if candidates else sorted(raw_by_key)
    missing = [key for key in want_keys if key not in raw_by_key]
    empty = [key for key in want_keys if key in raw_by_key and not raw_by_key[key]]
    if missing or empty:
        if missing:
            print(f'missing extracts: {len(missing)}', flush=True)
            for key in missing:
                print(f'  {key}', flush=True)
        if empty:
            print(f'empty extracts: {len(empty)}', flush=True)
            for key in empty:
                print(f'  {key}', flush=True)
        print('refusing to overwrite outputs', flush=True)
        return 1

    rows = []
    n = len(want_keys)
    for i, key in enumerate(want_keys, start=1):
        for raw in raw_by_key.get(key, []):
            if not raw.get('key'):
                raw = dict(raw)
                raw['key'] = key
            item = normalize_gain_row(raw)
            if item:
                rows.append(item)
        print_progress(i, n, key)

    rows = ood.apply_gain_overrides(rows)
    rows = attach_train_data(rows, model_rows)
    rows = coerce_pp_rows(rows)
    rows = attach_ood(rows, model_rows)
    rows = fill_baselines(rows)
    rows = dedupe_rows(rows)
    if refuse_output_shrink(JSONL_PATH, rows, args.force):
        return 1
    rows = sort_rows(rows, papers)
    write_outputs(rows, papers, not_applicable)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
