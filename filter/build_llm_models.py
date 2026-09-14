'''Merge per-paper LLM extracts into llm_models.jsonl and llm_models.md.

    python filter/build_llm_models.py
        renormalize existing jsonl and re-render markdown
    python filter/build_llm_models.py --from-jsonl
        same
    python filter/build_llm_models.py --extract-dir PATH
        merge extracts; refuse a missing/empty dir and refuse shrinking jsonl
'''

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

FILTER_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(FILTER_DIR))

from paths import (  # noqa: E402
    FILTER_DIR as ROOT,
    PAPERS_JSONL,
    classify,
    print_progress,
    read_jsonl,
    safe_key,
    write_jsonl,
)

REPO = ROOT.parent
JSONL_PATH = ROOT / 'llm_models.jsonl'
META_PATH = ROOT / 'llm_inventory_meta.json'
MD_PATH = REPO / 'llm_models.md'

SKIP_EXTRACT_NAMES = frozenset({
    'candidates.json',
    'excluded.json',
    'no_fulltext.json',
    'manifest.json',
})

START_POINTS = (
    'base',
    'instruct',
    'reasoning-distilled',
    'rl-tuned',
    'api',
    'unknown',
)
ROLES = (
    'trained',
    'baseline',
    'teacher',
    'judge/reward',
    'introduced',
    'analyzed',
)

FAMILY_ALIASES = {
    'llama': 'Llama',
    'llamma': 'Llama',
    'llma': 'Llama',
    'qwen': 'Qwen',
    'deepseek': 'DeepSeek',
    'gemma': 'Gemma',
    't5gemma': 'T5Gemma',
    'diffusiongemma': 'DiffusionGemma',
    'olmo': 'OLMo',
    'phi': 'Phi',
    'mistral': 'Mistral',
    'mixtral': 'Mixtral',
    'smollm': 'SmolLM',
    'nemotron': 'Nemotron',
    'glm': 'GLM',
    'kimi': 'Kimi',
    'minimax': 'MiniMax',
    'llada': 'LLaDA',
    'gpt': 'GPT',
    'claude': 'Claude',
    'gemini': 'Gemini',
    'pythia': 'Pythia',
    'palm': 'PaLM',
    'chinchilla': 'Chinchilla',
    'gopher': 'Gopher',
    'codex': 'Codex',
    'instructgpt': 'InstructGPT',
    'vicuna': 'Vicuna',
    'zephyr': 'Zephyr',
    'yi': 'Yi',
    'internlm': 'InternLM',
    'starcoder': 'StarCoder',
    'codellama': 'CodeLlama',
    'grok': 'Grok',
    'qwq': 'QwQ',
    'gptoss': 'GPT-OSS',
    'mimo': 'MiMo',
    'minigpt': 'MiniGPT',
    'minigpt4': 'MiniGPT-4',
    'tulu': 'Tulu',
    'o1': 'o1',
    'o3': 'o3',
    'o4': 'o4',
}

FAMILY_PREFIX_RE = re.compile(
    r'(GPT-OSS|DeepSeek|Qwen|Llama|Gemma|T5Gemma|DiffusionGemma|OLMo|'
    r'Phi|Mistral|Mixtral|SmolLM|Nemotron|GLM|Kimi|MiniMax|'
    r'LLaDA|GPT|Claude|Gemini|Pythia|Tulu|PaLM|Yi|InternLM|'
    r'StarCoder|CodeLlama|Grok|QwQ|Mamba|MiMo)',
    re.I,
)
GEN_FAMILY_RE = re.compile(
    r'(?:Qwen|Llama|Gemma|OLMo|Phi|GLM|LLaDA|GPT|Tulu|Yi)'
    r'[- ]?(\d+(?:\.\d+)?)(?!\s*[BM]\b)',
    re.I,
)
SIZE_RE = re.compile(r'(\d+(?:\.\d+)?)\s*([BM])(?![a-zA-Z])', re.I)
SIZE_TOKEN_RE = re.compile(
    r'^\d+(?:\.\d+)?[BM]$'
    r'|^\d+(?:\.\d+)?B-A\d+(?:\.\d+)?B$'
    r'|^\d+(?:\.\d+)?B \(\d+(?:\.\d+)?B act\)$',
    re.I,
)

BENCH_ALIASES = {
    'math500': 'MATH-500',
    'math 500': 'MATH-500',
    'math-500': 'MATH-500',
    'gsm-8k': 'GSM8K',
    'gsm8k': 'GSM8K',
    'aime24': 'AIME 2024',
    'aime 24': 'AIME 2024',
    'aime2024': 'AIME 2024',
    "aime'24": 'AIME 2024',
    'aime 2024': 'AIME 2024',
    'aime25': 'AIME 2025',
    'aime 25': 'AIME 2025',
    'aime2025': 'AIME 2025',
    "aime'25": 'AIME 2025',
    'aime 2025': 'AIME 2025',
    'amc23': 'AMC 2023',
    'amc 23': 'AMC 2023',
    'amc2023': 'AMC 2023',
    'amc 2023': 'AMC 2023',
    'minerva': 'Minerva Math',
    'minervamath': 'Minerva Math',
    'minerva-math': 'Minerva Math',
    'minerva math': 'Minerva Math',
    'gpqa diamond': 'GPQA Diamond',
    'gpqa-diamond': 'GPQA Diamond',
    'gpqadiamond': 'GPQA Diamond',
    'livecodebench': 'LiveCodeBench',
    'livecodebench v5': 'LiveCodeBench v5',
    'livecodebench v6': 'LiveCodeBench v6',
    'livecodebenchv5': 'LiveCodeBench v5',
    'livecodebenchv6': 'LiveCodeBench v6',
    'codeforces': 'Codeforces',
    'swe-bench verified': 'SWE-bench Verified',
    'swe bench verified': 'SWE-bench Verified',
    'swe-bench': 'SWE-bench',
    'swe bench': 'SWE-bench',
    'humaneval': 'HumanEval',
    'mmlu-pro': 'MMLU-Pro',
    'mmlu pro': 'MMLU-Pro',
    'mmlupro': 'MMLU-Pro',
    'hellaswag': 'HellaSwag',
    'winogrande': 'WinoGrande',
    'ifeval': 'IFEval',
    'olympiadbench': 'OlympiadBench',
    'olympiad bench': 'OlympiadBench',
    'livemathbench': 'LiveMathBench',
}

BENCH_DOMAIN = {
    'MATH-500': 'math',
    'MATH': 'math',
    'GSM8K': 'math',
    'AIME 2024': 'math',
    'AIME 2025': 'math',
    'AMC 2023': 'math',
    'AMC': 'math',
    'Minerva Math': 'math',
    'OlympiadBench': 'math',
    'LiveMathBench': 'math',
    'Omni-MATH': 'math',
    'HMMT': 'math',
    'BeyondAIME': 'math',
    'AOPS': 'math',
    'HumanEval': 'code',
    'MBPP': 'code',
    'LiveCodeBench': 'code',
    'Codeforces': 'code',
    'BigCodeBench': 'code',
    'CRUXEval': 'code',
    'SWE-bench': 'code',
    'GPQA': 'science QA',
    'GPQA Diamond': 'science QA',
    'ScienceQA': 'science QA',
    'SciQ': 'science QA',
    'TheoremQA': 'science QA',
    'MedQA': 'science QA',
    'ChemBench': 'science QA',
    'MMLU': 'general',
    'MMLU-Pro': 'general',
    'BBH': 'general',
    'IFEval': 'general',
    'TruthfulQA': 'general',
    'AlpacaEval': 'general',
    'Arena-Hard': 'general',
    'MT-Bench': 'general',
    'ZebraLogic': 'general',
    'SimpleQA': 'general',
    'BBEH': 'general',
    'LongBench': 'general',
    'RULER': 'general',
    'BrowseComp': 'agentic',
    'WebArena': 'agentic',
}

ROW_FIELDS = (
    'key',
    'title',
    'section',
    'model',
    'family',
    'generation',
    'variant',
    'sizes',
    'start_point',
    'role',
    'method',
    'train_data',
    'eval_id',
    'eval_ood',
    'ood_basis',
    'notes',
)
META_KEEP = ('key', 'safe_key', 'title', 'section', 'rel_path', 'n_tokens', 'urls')


def load_json(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))


def unique(items) -> list[str]:
    return list(dict.fromkeys(items))


def norm_space(text: str) -> str:
    return re.sub(r'\s+', ' ', (text or '').strip())


def alias_key(text: str) -> str:
    folded = unicodedata.normalize('NFKD', text)
    folded = folded.encode('ascii', 'ignore').decode('ascii')
    folded = folded.lower().replace('–', '-').replace('—', '-')
    folded = folded.replace("'", '').replace('’', '')
    folded = re.sub(r'[-_/]+', ' ', folded)
    return re.sub(r'\s+', ' ', folded).strip()


def fold_family_key(text: str) -> str:
    folded = unicodedata.normalize('NFKD', text)
    folded = folded.encode('ascii', 'ignore').decode('ascii')
    return re.sub(r'[^a-z0-9]', '', folded.lower())


def norm_family(name: str) -> str:
    raw = norm_space(name)
    if not raw:
        return ''
    return FAMILY_ALIASES.get(fold_family_key(raw), raw)


def norm_generation(value: str) -> str:
    text = norm_space(value)
    if re.fullmatch(r'v\d+(\.\d+)?', text, re.I):
        text = 'V' + text[1:]
    if text.lower().startswith('qwen'):
        text = re.sub(r'^Qwen-?', '', text, flags=re.I)
    aliases = {
        'r1-distill': 'R1',
        'r1-distill-qwen': 'R1',
        '2-1124': '2',
    }
    return aliases.get(text.lower(), text)


def norm_model(name: str | None) -> str | None:
    if name is None:
        return None
    text = norm_space(name)
    if not text or text.lower() in {'null', 'none', 'n/a'}:
        return None
    text = text.replace('LLaMA', 'Llama')
    text = re.sub(r'Qwen-(\d)', r'Qwen\1', text)
    text = text.replace('MATH500', 'MATH-500')
    return text


def norm_str_list(items) -> list[str]:
    if not items:
        return []
    if isinstance(items, str):
        items = [items]
    out = []
    seen = set()
    for item in items:
        text = norm_space(str(item))
        if text and text not in seen:
            seen.add(text)
            out.append(text)
    return out


def resolve_bench(text: str) -> str:
    spaced = alias_key(text)
    compact = spaced.replace(' ', '')
    if spaced in BENCH_ALIASES:
        return BENCH_ALIASES[spaced]
    if compact in BENCH_ALIASES:
        return BENCH_ALIASES[compact]
    if re.fullmatch(r"aime['’]?24", text, re.I):
        return 'AIME 2024'
    if re.fullmatch(r"aime['’]?25", text, re.I):
        return 'AIME 2025'
    if re.fullmatch(r'aime2024', text, re.I):
        return 'AIME 2024'
    if re.fullmatch(r'aime2025', text, re.I):
        return 'AIME 2025'
    return text


def norm_bench_list(items) -> list[str]:
    return unique(resolve_bench(item) for item in norm_str_list(items))


def norm_start(value: str) -> str:
    text = (value or 'unknown').strip().lower()
    aliases = {
        'chat': 'instruct',
        'it': 'instruct',
        'instruct-tuned': 'instruct',
        'r1-distill': 'reasoning-distilled',
        'distilled': 'reasoning-distilled',
        'rl': 'rl-tuned',
        'closed': 'api',
        'proprietary': 'api',
    }
    text = aliases.get(text, text)
    return text if text in START_POINTS else 'unknown'


def norm_role(value: str) -> str:
    text = (value or 'analyzed').strip().lower()
    aliases = {
        'train': 'trained',
        'finetuned': 'trained',
        'fine-tuned': 'trained',
        'eval': 'baseline',
        'compared': 'baseline',
        'comparison': 'baseline',
        'reward': 'judge/reward',
        'judge': 'judge/reward',
        'verifier': 'judge/reward',
        'tech report': 'introduced',
        'released': 'introduced',
        'interpret': 'analyzed',
        'analysis': 'analyzed',
    }
    text = aliases.get(text, text)
    return text if text in ROLES else 'analyzed'


def is_plausible_size(token: str) -> bool:
    return bool(SIZE_TOKEN_RE.fullmatch(norm_space(token)))


def is_version_as_size(token: str, model: str | None, start_point: str) -> bool:
    match = re.fullmatch(r'(\d+(?:\.\d+)?)M', norm_space(token), re.I)
    if not match:
        return False
    if start_point == 'api':
        return True
    number = match.group(1)
    return bool(re.search(
        rf'(?<![\d.]){re.escape(number)}\s*(mini|max|medium|nano)\b',
        model or '',
        re.I,
    ))


def infer_sizes(model: str | None, start_point: str) -> list[str]:
    if not model:
        return []
    if start_point == 'api' and not re.search(r'\d+(?:\.\d+)?\s*B\b', model, re.I):
        return []
    found = [f'{number}{unit.upper()}' for number, unit in SIZE_RE.findall(model)]
    return unique(found)


def canon_size(token: str) -> str:
    text = norm_space(token)
    simple = re.fullmatch(r'(\d+(?:\.\d+)?)\s*([BM])', text, re.I)
    if simple:
        return f'{simple.group(1)}{simple.group(2).upper()}'
    return text


def clean_sizes(raw_sizes, model: str | None, start_point: str) -> list[str]:
    kept = unique([
        canon_size(item) for item in norm_str_list(raw_sizes)
        if is_plausible_size(item) and not is_version_as_size(item, model, start_point)
    ])
    if kept:
        return kept
    return infer_sizes(model, start_point)


def infer_family_fields(row: dict) -> dict:
    model = row.get('model')
    family = norm_family(row.get('family') or '')
    generation = norm_generation(row.get('generation') or '')
    variant = norm_space(row.get('variant') or '')
    start = (row.get('start_point') or '').lower()
    low = (model or '').lower()

    if model and re.search(r'gpt-?oss', model, re.I):
        family = 'GPT-OSS'
        if generation.lower() == 'oss':
            generation = ''
    elif family == 'GPT' and generation.lower() == 'oss':
        family = 'GPT-OSS'
        generation = ''
    elif model and not family:
        match = FAMILY_PREFIX_RE.match(model)
        if match:
            family = norm_family(match.group(1))

    if model and re.search(r'gpt-?4o\b', model, re.I):
        generation = '4o'
    if generation == '2' and model and re.search(r'\b2\.0\b', model):
        generation = '2.0'
    if family == 'LLaDA' and model and re.search(r'2\.0', model):
        generation = '2.0'

    inferred_gen = ''
    if model:
        match = GEN_FAMILY_RE.search(model)
        if match:
            inferred_gen = norm_generation(match.group(1))
        elif re.search(r'\bR1\b', model, re.I):
            inferred_gen = 'R1'
        elif re.search(r'\bV3\b', model, re.I):
            inferred_gen = 'V3'
        elif re.search(r'\bM1\b', model, re.I):
            inferred_gen = 'M1'
    if not generation:
        generation = inferred_gen
    elif generation and model:
        size_nums = [m.group(1) for m in re.finditer(
            r'(\d+(?:\.\d+)?)[BM]\b', model, re.I,
        )]
        versioned = bool(GEN_FAMILY_RE.search(model) and inferred_gen == generation)
        if generation in size_nums and not versioned:
            generation = inferred_gen

    if model and re.search(r'distill', model, re.I):
        if 'qwen' in low:
            variant = 'Distill-Qwen'
        elif 'llama' in low:
            variant = 'Distill-Llama'
    elif start == 'reasoning-distilled' and variant.lower() in {'', 'qwen', 'distill'}:
        if 'qwen' in low:
            variant = 'Distill-Qwen'
        elif 'llama' in low:
            variant = 'Distill-Llama'
    elif not variant:
        bits = []
        for label in (
            'Math', 'Coder', 'Code', 'Instruct', 'Chat', 'Base',
            'VL', 'Vision', 'MoE', 'Zero', 'Reasoner',
        ):
            if re.search(rf'\b{label}\b', model or '', re.I):
                bits.append(label)
        variant = '-'.join(bits)

    if start == 'base' and variant.lower() in {'', 'base'}:
        variant = 'Base'
    elif start == 'instruct' and variant.lower() in {'', 'instruct', 'chat', 'it'}:
        variant = 'Instruct'
    return {
        'family': family,
        'generation': generation,
        'variant': variant,
    }


def normalize_row(raw: dict, paper: dict) -> dict:
    model = norm_model(raw.get('model'))
    start_point = norm_start(raw.get('start_point') or 'unknown')
    inferred = infer_family_fields({
        **raw,
        'model': model,
        'start_point': start_point,
    })
    eval_id = norm_bench_list(raw.get('eval_id'))
    eval_ood = norm_bench_list(raw.get('eval_ood'))
    ood_basis = (raw.get('ood_basis') or '').strip().lower()
    if ood_basis not in {'paper', 'inferred', ''}:
        ood_basis = 'inferred' if eval_ood else ''
    if not eval_ood:
        ood_basis = ''
    row = {
        'key': paper['key'],
        'title': paper.get('line_title') or raw.get('title') or '',
        'section': paper.get('section') or raw.get('section') or '',
        'model': model,
        'family': inferred['family'],
        'generation': inferred['generation'],
        'variant': inferred['variant'],
        'sizes': clean_sizes(raw.get('sizes'), model, start_point),
        'start_point': start_point,
        'role': norm_role(raw.get('role') or 'analyzed'),
        'method': norm_space(raw.get('method') or ''),
        'train_data': norm_str_list(raw.get('train_data')),
        'eval_id': eval_id,
        'eval_ood': eval_ood,
        'ood_basis': ood_basis,
        'notes': norm_space(raw.get('notes') or ''),
    }
    if model is None:
        row['role'] = ''
        row['start_point'] = ''
        row['family'] = ''
        row['generation'] = ''
        row['variant'] = ''
        row['sizes'] = []
    return {field: row[field] for field in ROW_FIELDS}


def papers_safe_map(papers: list[dict]) -> dict[str, str]:
    return {safe_key(paper['key']): paper['key'] for paper in papers if paper.get('key')}


def resolve_extract_key(
    path: Path,
    rows: list,
    papers_by_safe: dict[str, str],
    papers_by_key: dict[str, dict],
) -> str | None:
    for row in rows:
        if isinstance(row, dict) and row.get('key'):
            return row['key']
    stem = path.stem
    if stem in papers_by_key:
        return stem
    return papers_by_safe.get(stem)


def extract_json_paths(extract_dir: Path) -> list[Path]:
    return sorted(
        path for path in extract_dir.glob('*.json')
        if path.name not in SKIP_EXTRACT_NAMES
    )


def load_extracts(
    extract_dir: Path,
    papers: list[dict] | None = None,
) -> dict[str, list[dict]]:
    papers = papers or []
    papers_by_key = {paper['key']: paper for paper in papers}
    papers_by_safe = papers_safe_map(papers)
    by_key: dict[str, list[dict]] = {}
    paths = extract_json_paths(extract_dir)
    for i, path in enumerate(paths, start=1):
        data = load_json(path)
        if isinstance(data, dict):
            rows = data.get('rows') or data.get('models') or [data]
        else:
            rows = data
        if not isinstance(rows, list):
            rows = [rows]
        key = resolve_extract_key(path, rows, papers_by_safe, papers_by_key)
        if key is None:
            print(f'skip unmapped extract {path.name}', flush=True)
            print_progress(i, len(paths), path.name)
            continue
        by_key.setdefault(key, [])
        by_key[key].extend(row for row in rows if isinstance(row, dict))
        print_progress(i, len(paths), path.name)
    return by_key


def paper_url(key: str, extra_urls: list[str] | None = None) -> str:
    urls = [url for url in (extra_urls or []) if url]
    if urls:
        return urls[0]
    if not key:
        return ''
    if key.startswith('arxiv:'):
        return f'https://arxiv.org/abs/{key.split(":", 1)[1]}'
    if key.startswith('doi:'):
        return f'https://doi.org/{key.split(":", 1)[1]}'
    if key.startswith('openreview:'):
        return f'https://openreview.net/forum?id={key.split(":", 1)[1]}'
    if key.startswith('acl:'):
        return f'https://aclanthology.org/{key.split(":", 1)[1]}'
    return ''


def md_escape(text: str) -> str:
    return (text or '').replace('|', '\\|').replace('\n', ' ')


def md_link(title: str, url: str, limit: int | None = None) -> str:
    shown = title or ''
    if limit is not None and len(shown) > limit:
        shown = shown[:limit]
    shown = md_escape(shown)
    if url:
        return f'[{shown}]({url})'
    return shown


def join_cells(items: list[str], limit: int = 8) -> str:
    if not items:
        return ''
    shown = items[:limit]
    extra = len(items) - limit
    text = ', '.join(shown)
    if extra > 0:
        text += f' +{extra}'
    return md_escape(text)


def domain_of(name: str) -> str:
    if name in BENCH_DOMAIN:
        return BENCH_DOMAIN[name]
    low = name.lower()
    if any(key in low for key in (
        'math', 'aime', 'amc', 'gsm', 'olympiad', 'minerva', 'hmmt',
    )):
        return 'math'
    if any(key in low for key in (
        'code', 'humaneval', 'mbpp', 'swe', 'crux', 'leetcode',
    )):
        return 'code'
    if any(key in low for key in (
        'gpqa', 'science', 'chem', 'med', 'physics', 'theorem',
    )):
        return 'science QA'
    if any(key in low for key in ('web', 'browse', 'agent', 'swe-gym', 'osworld')):
        return 'agentic'
    return 'general'


def model_line_key(row: dict) -> tuple:
    return (
        row.get('family') or '',
        row.get('generation') or '',
        row.get('variant') or '',
        row.get('start_point') or '',
    )


def slim_meta_record(rec: dict, papers_by_title: dict[str, dict] | None = None) -> dict:
    urls = [url for url in (rec.get('urls') or []) if url]
    key = rec.get('key') or ''
    title = rec.get('title') or ''
    if not key and urls:
        classified = classify(urls[0])
        if classified:
            key = classified[1]
    if not key and papers_by_title:
        hit = papers_by_title.get(norm_space(title))
        if hit:
            key = hit.get('key') or key
            if not urls:
                urls = [url for url in (hit.get('urls') or []) if url]
    out = {}
    values = {
        'key': key,
        'safe_key': rec.get('safe_key') or '',
        'title': title,
        'section': rec.get('section') or '',
        'rel_path': rec.get('rel_path') or '',
        'n_tokens': rec.get('n_tokens'),
        'urls': urls,
    }
    for field in META_KEEP:
        value = values.get(field)
        if value in (None, '', []):
            continue
        out[field] = value
    return out


def load_inventory_lists(
    extract_dir: Path | None,
    papers: list[dict],
) -> tuple[list[dict], list[dict]]:
    papers_by_title = {
        norm_space(paper.get('line_title') or ''): paper
        for paper in papers
        if paper.get('line_title')
    }
    excluded = []
    no_fulltext = []
    if META_PATH.exists():
        meta = load_json(META_PATH)
        excluded = meta.get('excluded') or []
        no_fulltext = meta.get('no_fulltext') or []
    if extract_dir is not None:
        excluded_path = extract_dir / 'excluded.json'
        no_ft_path = extract_dir / 'no_fulltext.json'
        if excluded_path.exists():
            excluded = load_json(excluded_path)
        if no_ft_path.exists():
            no_fulltext = load_json(no_ft_path)
    excluded = [slim_meta_record(rec, papers_by_title) for rec in excluded]
    no_fulltext = [slim_meta_record(rec, papers_by_title) for rec in no_fulltext]
    return excluded, no_fulltext


def write_meta(excluded: list[dict], no_fulltext: list[dict]) -> None:
    META_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp = META_PATH.with_suffix(META_PATH.suffix + '.tmp')
    tmp.write_text(
        json.dumps(
            {'excluded': excluded, 'no_fulltext': no_fulltext},
            ensure_ascii=False,
            indent=2,
        ) + '\n',
        encoding='utf-8',
    )
    tmp.replace(META_PATH)


def render_md(
    rows: list[dict],
    papers: list[dict],
    excluded: list[dict],
    no_fulltext: list[dict],
) -> str:
    papers_by_key = {paper['key']: paper for paper in papers}
    rows_by_key: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        rows_by_key[row['key']].append(row)
    keys_with_rows = set(rows_by_key)
    n_papers = len(keys_with_rows)
    n_with_model = len({row['key'] for row in rows if row.get('model')})
    n_null = n_papers - n_with_model
    lines_set = {model_line_key(row) for row in rows if row.get('model')}
    ood_names = sorted({
        bench for row in rows for bench in row.get('eval_ood') or []
    })
    n_trained_no_size = sum(
        1 for row in rows
        if row.get('role') == 'trained' and row.get('model') and not row.get('sizes')
    )

    out = []
    out.append('# LLM inventory from key-papers')
    out.append('')
    out.append(
        'Per-paper extraction from `filter/fulltext/*.md`. '
        'One row in `filter/llm_models.jsonl` is one model line '
        '(family / generation / variant / start-point); size sweeps stay in `sizes`.'
    )
    out.append('')
    out.append('## Summary')
    out.append('')
    out.append(f'- Papers read: **{n_papers}**')
    out.append(f'- Papers with at least one LLM: **{n_with_model}**')
    out.append(f'- Papers read but no LLM experiment: **{n_null}**')
    out.append(f'- Distinct model lines: **{len(lines_set)}**')
    out.append(f'- Distinct OOD benchmarks: **{len(ood_names)}**')
    out.append(f'- Trained rows with no size: **{n_trained_no_size}**')
    out.append(
        f'- Fulltexts excluded (no LLM name, not Post-training/Reasoning): '
        f'**{len(excluded)}**'
    )
    out.append(f'- Readme entries without fulltext: **{len(no_fulltext)}**')
    out.append('')

    groups: dict[tuple, list[dict]] = defaultdict(list)
    for row in rows:
        if row.get('model'):
            groups[model_line_key(row)].append(row)

    def sort_group(item):
        key, items = item
        return (-len({row['key'] for row in items}), key[0].lower(), *key[1:])

    out.append('## Model index')
    out.append('')
    out.append(
        '| Family | Gen | Variant | Start | Sizes | Papers | '
        'Post-training data | OOD evals |'
    )
    out.append('|---|---|---|---|---|---|---|---|')
    for key, items in sorted(groups.items(), key=sort_group):
        family, generation, variant, start = key
        sizes = unique([
            size for row in items for size in row.get('sizes') or []
        ])
        paper_keys = unique([row['key'] for row in items])
        paper_links = []
        for paper_key in paper_keys[:12]:
            title = papers_by_key.get(paper_key, {}).get('line_title') or paper_key
            paper_links.append(md_link(title, paper_url(paper_key), limit=40))
        extra = len(paper_keys) - 12
        papers_cell = '<br>'.join(paper_links)
        if extra > 0:
            papers_cell += f'<br>+{extra}'
        train = unique([
            item for row in items for item in row.get('train_data') or []
        ])
        evals = unique([
            item for row in items for item in row.get('eval_ood') or []
        ])
        out.append(
            f'| {md_escape(family)} | {md_escape(generation)} | '
            f'{md_escape(variant)} | {md_escape(start)} | '
            f'{join_cells(sizes, 10)} | {len(paper_keys)}: {papers_cell} | '
            f'{join_cells(train, 6)} | {join_cells(evals, 8)} |'
        )
    out.append('')

    out.append('## Per-paper')
    out.append('')
    by_section: dict[str, list[str]] = defaultdict(list)
    for paper in papers:
        key = paper['key']
        if key not in keys_with_rows:
            continue
        paper_rows = rows_by_key[key]
        section = paper.get('section') or paper_rows[0].get('section') or ''
        title = paper.get('line_title') or key
        link = md_link(title, paper_url(key, paper.get('urls')))
        if all(row.get('model') is None for row in paper_rows):
            notes = paper_rows[0].get('notes') or 'no LLM experiment'
            by_section[section].append(
                f'| {link} | — | — | — | — | — | {md_escape(notes)} |'
            )
            continue
        models = []
        methods = []
        trains = []
        ids = []
        oods = []
        notes = []
        for row in paper_rows:
            if not row.get('model'):
                continue
            size_s = ','.join(row.get('sizes') or [])
            bit = row['model']
            extra_bits = []
            if size_s and size_s not in bit:
                extra_bits.append(size_s)
            if row.get('start_point'):
                extra_bits.append(row['start_point'])
            if row.get('role'):
                extra_bits.append(row['role'])
            if extra_bits:
                bit += f' ({", ".join(extra_bits)})'
            if bit not in models:
                models.append(bit)
            if row.get('method') and row['method'] not in methods:
                methods.append(row['method'])
            for item in row.get('train_data') or []:
                if item not in trains:
                    trains.append(item)
            for item in row.get('eval_id') or []:
                if item not in ids:
                    ids.append(item)
            for item in row.get('eval_ood') or []:
                if item not in oods:
                    oods.append(item)
            if row.get('notes') and row['notes'] not in notes:
                notes.append(row['notes'])
        id_set = set(ids)
        oods = [item for item in oods if item not in id_set]
        by_section[section].append(
            f'| {link} | {md_escape("; ".join(models))} | '
            f'{md_escape("; ".join(methods))} | {join_cells(trains, 6)} | '
            f'{join_cells(ids, 6)} | {join_cells(oods, 8)} | '
            f'{join_cells(notes, 3)} |'
        )

    seen_sections = []
    for paper in papers:
        section = paper.get('section') or ''
        if section in by_section and section not in seen_sections:
            seen_sections.append(section)

    for section in seen_sections:
        out.append(f'### {section}')
        out.append('')
        out.append(
            '| Paper | Models | Method | Post-training data | '
            'ID eval | OOD eval | Notes |'
        )
        out.append('|---|---|---|---|---|---|---|')
        out.extend(by_section[section])
        out.append('')

    ood_map: dict[str, list[str]] = defaultdict(list)
    for row in rows:
        for bench in row.get('eval_ood') or []:
            if row['key'] not in ood_map[bench]:
                ood_map[bench].append(row['key'])
    out.append('## OOD benchmark index')
    out.append('')
    out.append('| Benchmark | Domain | Papers |')
    out.append('|---|---|---|')
    for bench, keys in sorted(ood_map.items(), key=lambda kv: (-len(kv[1]), kv[0].lower())):
        links = [
            md_link(
                papers_by_key.get(paper_key, {}).get('line_title') or paper_key,
                paper_url(paper_key),
                limit=36,
            )
            for paper_key in keys[:15]
        ]
        extra = len(keys) - 15
        cell = '<br>'.join(links)
        if extra > 0:
            cell += f'<br>+{extra}'
        out.append(f'| {md_escape(bench)} | {domain_of(bench)} | {len(keys)}: {cell} |')
    out.append('')

    if excluded:
        out.append('## Excluded fulltexts (no LLM name)')
        out.append('')
        by_ex: dict[str, list[dict]] = defaultdict(list)
        for rec in excluded:
            by_ex[rec.get('section') or ''].append(rec)
        for section, items in by_ex.items():
            links = []
            for item in items:
                title = item.get('title') or item.get('key') or ''
                links.append(md_link(title, paper_url(item.get('key') or '')))
            out.append(
                f'- **{section or "unsectioned"}** ({len(items)}): ' +
                ', '.join(links)
            )
        out.append('')

    if no_fulltext:
        out.append('## Readme entries without fulltext')
        out.append('')
        for rec in no_fulltext:
            title = rec.get('title') or rec.get('key') or ''
            url = paper_url(rec.get('key') or '', rec.get('urls'))
            section = rec.get('section') or ''
            out.append(f'- {md_link(title, url)} — {section}')
        out.append('')

    return '\n'.join(out) + '\n'


def existing_row_count(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for line in path.read_text(encoding='utf-8').splitlines() if line.strip())


def refuse_shrink(existing_n: int, new_n: int, force: bool) -> bool:
    return existing_n > 0 and new_n < existing_n and not force


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


def write_outputs(
    rows: list[dict],
    papers: list[dict],
    excluded: list[dict],
    no_fulltext: list[dict],
) -> None:
    write_jsonl(JSONL_PATH, rows)
    print(f'wrote {len(rows)} rows -> {JSONL_PATH}', flush=True)
    write_meta(excluded, no_fulltext)
    print(f'wrote {META_PATH}', flush=True)
    markdown = render_md(rows, papers, excluded, no_fulltext)
    tmp = MD_PATH.with_suffix(MD_PATH.suffix + '.tmp')
    tmp.write_text(markdown, encoding='utf-8')
    tmp.replace(MD_PATH)
    print(f'wrote {MD_PATH} ({len(markdown.splitlines())} lines)', flush=True)


def renormalize_rows(rows: list[dict], papers: list[dict]) -> list[dict]:
    papers_by_key = {paper['key']: paper for paper in papers}
    out = []
    n = len(rows)
    for i, raw in enumerate(rows, start=1):
        paper = papers_by_key.get(raw.get('key')) or {
            'key': raw.get('key') or '',
            'line_title': raw.get('title') or '',
            'section': raw.get('section') or '',
        }
        out.append(normalize_row(raw, paper))
        if i == n or i % 200 == 0:
            print_progress(i, n, raw.get('key') or '')
    order = {paper['key']: i for i, paper in enumerate(papers)}
    out.sort(key=lambda row: (order.get(row['key'], 10**6), row.get('model') or ''))
    return out


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Merge LLM extracts or re-render llm_models.md',
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
        help='renormalize filter/llm_models.jsonl and re-render markdown',
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
    papers_by_key = {paper['key']: paper for paper in papers}

    if extract_dir is None:
        if not JSONL_PATH.exists():
            print(
                f'missing {JSONL_PATH}; pass --extract-dir PATH to merge',
                flush=True,
            )
            return 1
        print(f'renormalizing {JSONL_PATH}', flush=True)
        rows = renormalize_rows(read_jsonl(JSONL_PATH), papers)
        excluded, no_fulltext = load_inventory_lists(None, papers)
        write_outputs(rows, papers, excluded, no_fulltext)
        return 0

    paths = require_extract_dir(extract_dir)
    if paths is None:
        return 1

    print(f'loading extracts from {extract_dir}', flush=True)
    raw_by_key = load_extracts(extract_dir, papers)
    candidate_path = extract_dir / 'candidates.json'
    candidates = load_json(candidate_path) if candidate_path.exists() else []
    want_keys = [item['key'] for item in candidates] if candidates else sorted(raw_by_key)
    rows = []
    missing = []
    for i, key in enumerate(want_keys, start=1):
        paper = papers_by_key.get(key) or {
            'key': key,
            'line_title': key,
            'section': '',
        }
        extracted = raw_by_key.get(key)
        if not extracted:
            missing.append(key)
            print_progress(i, len(want_keys), f'missing {key}')
            continue
        for raw in extracted:
            rows.append(normalize_row(raw, paper))
        print_progress(i, len(want_keys), key)

    if missing:
        print(f'missing extracts: {len(missing)}', flush=True)
        for key in missing:
            print(f'  {key}', flush=True)
        print('refusing to overwrite outputs', flush=True)
        return 1

    existing_n = existing_row_count(JSONL_PATH)
    if refuse_shrink(existing_n, len(rows), args.force):
        print(
            f'refusing to shrink {JSONL_PATH}: {existing_n} -> {len(rows)} '
            f'(pass --force to override)',
            flush=True,
        )
        return 1

    order = {paper['key']: i for i, paper in enumerate(papers)}
    rows.sort(key=lambda row: (order.get(row['key'], 10**6), row.get('model') or ''))
    excluded, no_fulltext = load_inventory_lists(extract_dir, papers)
    write_outputs(rows, papers, excluded, no_fulltext)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
