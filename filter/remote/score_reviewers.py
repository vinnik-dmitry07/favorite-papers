'''Full-paper reviewers: CycleReviewer, DeepReviewer, OpenReviewer, SEA-E.

    python score_reviewers.py --model openreviewer-8b
    python score_reviewers.py --model sea-e --only-keys arxiv:2503.14858
'''

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from data_paths import (  # noqa: E402
    append_jsonl,
    fulltext_for,
    fulltext_index,
    load_joined,
    reviews_dir,
    safe_key,
    scored_keys,
    scores_path,
)
from vllm_boot import make_llm  # noqa: E402

MODELS = {
    'cyclereviewer-8b': {
        'repo': 'WestlakeNLP/CycleReviewer-ML-Llama-3.1-8B',
        'kind': 'cycle',
        'size': '8B',
        'max_len': 40960,
        'max_tokens': 7000,
        'temperature': 0.4,
        'top_p': 0.95,
        'quant': None,
    },
    'cyclereviewer-70b': {
        'repo': 'WestlakeNLP/CycleReviewer-Llama-3.1-70B',
        'kind': 'cycle',
        'size': '70B',
        'max_len': 40960,
        'max_tokens': 7000,
        'temperature': 0.4,
        'top_p': 0.95,
        'quant': 'fp8',
    },
    'deepreviewer-7b': {
        'repo': 'WestlakeNLP/DeepReviewer-7B',
        'kind': 'deep',
        'size': '7B',
        'max_len': 49152,
        'max_tokens': 32768,
        'temperature': 0.4,
        'top_p': 0.95,
        'quant': None,
        'mode': 'Standard Mode',
    },
    'deepreviewer-7b-fast': {
        'repo': 'WestlakeNLP/DeepReviewer-7B',
        'kind': 'deep',
        'size': '7B',
        'max_len': 49152,
        'max_tokens': 16384,
        'temperature': 0.4,
        'top_p': 0.95,
        'quant': None,
        'mode': 'Fast Mode',
    },
    'deepreviewer-14b': {
        'repo': 'WestlakeNLP/DeepReviewer-14B',
        'kind': 'deep',
        'size': '14B',
        'max_len': 49152,
        'max_tokens': 16384,
        'temperature': 0.4,
        'top_p': 0.95,
        'quant': None,
        'mode': 'Fast Mode',
    },
    'openreviewer-8b': {
        'repo': 'maxidl/Llama-OpenReviewer-8B',
        'kind': 'openreviewer',
        'size': '8B',
        'max_len': 32768,
        'max_tokens': 4096,
        'temperature': 0.3,
        'top_p': None,
        'quant': None,
    },
    'sea-e': {
        'repo': 'ECNU-SEA/SEA-E',
        'kind': 'sea',
        'size': '7B',
        'max_len': 32768,
        'max_tokens': 8192,
        'temperature': 0.3,
        'top_p': None,
        'quant': None,
    },
}

AVG_RE = re.compile(
    r'avg(?:erage)?\s*(?:rating|score)\s*[:\-]?\s*(\d{1,2}(?:\.\d+)?)',
    re.I,
)
DECISION_RE = re.compile(
    r'(?:paper\s+)?decision\b[^\n]{0,80}?\b(accept|reject)\b',
    re.I,
)
DECISION_LINE_RE = re.compile(
    r'(?m)^\s*[-*]?\s*decision\s*[:\-]\s*(accept|reject)\b',
    re.I,
)
DECISION_HEAD_RE = re.compile(
    r'(?:^|\n)#{1,3}\s*(?:paper\s+)?decision\b[^\n]*\n+\s*[:\-*]*\s*(accept|reject)\b',
    re.I,
)
DECISION_NL_RE = re.compile(
    r'(?:\*\*)?(?:paper\s+)?decision(?:\*\*)?\s*[:\-]?\*{0,2}\s*(?:\n\s*)+(accept|reject)\b',
    re.I,
)
WEAK_RE = re.compile(
    r'(?:\*\*)?weakness(?:es)?(?:\*\*)?\s*:?\s*(.*?)(?:\n\s*\n|\*\*questions|\*\*rating|\*\*paper|#{1,3}\s+questions)',
    re.I | re.S,
)
THINK_RE = re.compile(r'<think>.*?</think>', re.I | re.S)
BOXED_START_RE = re.compile(r'\\?boxed_review\{', re.I)


def _brace_body(text: str, open_idx: int) -> str | None:
    depth = 0
    i = open_idx
    while i < len(text):
        ch = text[i]
        if ch == '\\' and i + 1 < len(text):
            i += 2
            continue
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0:
                return text[open_idx + 1:i]
        i += 1
    return None


def extract_boxed_review(text: str) -> str | None:
    starts = list(BOXED_START_RE.finditer(text or ''))
    if not starts:
        return None
    for match in reversed(starts):
        body = _brace_body(text, match.end() - 1)
        if body:
            return body
    return None
HEADING_RATING_RE = re.compile(
    r'(?:^|\n)#{1,3}\s*rating\b[^\n]*\n+\s*[:\-*]*\s*(\d{1,2}(?:\.\d+)?)',
    re.I,
)
META_HEAD_RE = re.compile(r'^#{1,3}\s*meta\s+review\b', re.I | re.M)

# Official SEA instruction_e (github.com/ecnu-sea/SEA inference/template.json).
SEA_INSTRUCTION = '''You are a highly experienced, conscientious, and fair academic reviewer, please help me review this paper. The review should be organized into nine sections: 
1. Summary: A summary of the paper in 100-150 words.
2. Strengths/Weaknesses/Questions: The Strengths/Weaknesses/Questions of paper, which should be listed in bullet points, with each point supported by specific examples from the article where possible.
3. Soundness/Contribution/Presentation: Rate the paper's Soundness/Contribution/Presentation, and match this score to the corresponding description from the list below and provide the result. The possible scores and their descriptions are: 
 1 poor
 2 fair
 3 good
 4 excellent
4. Rating: Give this paper an appropriate rating, match this rating to the corresponding description from the list below and provide the result. The possible Ratings and their descriptions are: 
 1 strong reject
 2 reject, significant issues present
 3 reject, not good enough
 4 possibly reject, but has redeeming facets
 5 marginally below the acceptance threshold
 6 marginally above the acceptance threshold
 7 accept, but needs minor improvements 
 8 accept, good paper
 9 strong accept, excellent work
 10 strong accept, should be highlighted at the conference 
5. Paper Decision: It must include the Decision itself(Accept or Reject) and the reasons for this decision, based on the criteria of originality, methodological soundness, significance of results, and clarity and logic of presentation.

Here is the template for a review format, you must follow this format to output your review result:
**Summary:**
Summary content

**Strengths:**
- Strength 1
- Strength 2
- ...

**Weaknesses:**
- Weakness 1
- Weakness 2
- ...

**Questions:**
- Question 1
- Question 2
- ...

**Soundness:**
Soundness result

**Presentation:**
Presentation result

**Contribution:**
Contribution result

**Rating:**
Rating result

**Paper Decision:**
- Decision: Accept/Reject
- Reasons: reasons content


Please ensure your feedback is objective and constructive. The paper is as follows:'''

OR_FIELDS = '''## Summary
Briefly summarize the paper and its contributions.

## Soundness
4: excellent
3: good
2: fair
1: poor

## Presentation
4: excellent
3: good
2: fair
1: poor

## Contribution
4: excellent
3: good
2: fair
1: poor

## Strengths
## Weaknesses
## Questions
## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns

## Rating
Please provide an overall score on its own line, for example:
8
'''

OR_SYSTEM = '''You are an expert reviewer for AI conferences. You follow best practices and review papers according to the reviewer guidelines.
Your write reviews in markdown format. Your reviews contain the following sections:

# Review

{fields}

Put the numeric Rating on its own line immediately after the ## Rating heading.
Your response must only contain the review in markdown format with sections as defined above.
'''.format(fields=OR_FIELDS)

# Official CycleReviewer system prompt (ai_researcher.cycle_reviewer).
CYCLE_SYSTEM = '''You are an expert academic reviewer tasked with providing a thorough and balanced evaluation of research papers. For each paper submitted, conduct a comprehensive review addressing the following aspects:

            1. Summary: Briefly outline main points and objectives.
            2. Soundness: Assess methodology and logical consistency.
            3. Presentation: Evaluate clarity, organization, and visual aids.
            4. Contribution: Analyze significance and novelty in the field.
            5. Strengths: Identify the paper's strongest aspects.
            6. Weaknesses: Point out areas for improvement.
            7. Questions: Pose questions for the authors.
            8. Rating: Score 1-10, justify your rating.
            9. Meta Review: Provide overall assessment and recommendation (Accept/Reject).

            Maintain objectivity and provide specific examples from the paper to support your evaluation.

            You need to fill out **4** review opinions.'''

DEEP_SIMREVIEWER = (
    'When you simulate different reviewers, write the sections in this order: '
    'Summary, Soundness, Presentation, Contribution, Strengths, Weaknesses, '
    'Suggestions, Questions, Rating and Confidence.'
)

_FALLBACK_WARNED = False


def deep_system(mode: str, reviewer_num: int = 4) -> str:
    if mode == 'Best Mode':
        prompt = (
            'You are an expert academic reviewer tasked with providing a thorough '
            'and balanced evaluation of research papers. Your thinking mode is '
            'Best Mode. In this mode, you should aim to provide the most reliable '
            'review results by conducting a thorough analysis of the paper. I allow '
            'you to use search tools to obtain background knowledge about the paper '
            '- please provide three different questions. I will help you with the '
            'search. After you complete your thinking, you should review by '
            f'simulating {reviewer_num} different reviewers, and use self-verification '
            'to double-check any paper deficiencies identified. Finally, provide '
            'complete review results.'
        )
        return prompt + DEEP_SIMREVIEWER
    if mode == 'Standard Mode':
        prompt = (
            'You are an expert academic reviewer tasked with providing a thorough '
            'and balanced evaluation of research papers. Your thinking mode is '
            'Standard Mode. In this mode, you should review by simulating '
            f'{reviewer_num} different reviewers, and use self-verification to '
            'double-check any paper deficiencies identified. Finally, provide '
            'complete review results.'
        )
        return prompt + DEEP_SIMREVIEWER
    if mode == 'Fast Mode':
        return (
            'You are an expert academic reviewer tasked with providing a thorough '
            'and balanced evaluation of research papers. Your thinking mode is '
            'Fast Mode. In this mode, you should quickly provide the review results.'
        )
    return (
        'You are an expert academic reviewer tasked with providing a thorough '
        'and balanced evaluation of research papers.'
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', required=True, choices=sorted(MODELS))
    parser.add_argument('--only-keys', default='')
    parser.add_argument('--tp', type=int, default=1)
    parser.add_argument('--max-paper-chars', type=int, default=60_000)
    parser.add_argument('--backend', choices=['vllm', 'ai_researcher'], default='vllm')
    parser.add_argument('--batch-size', type=int, default=0)
    parser.add_argument('--deep-mode', default='')
    parser.add_argument('--seed', type=int, default=0)
    parser.add_argument('--max-tokens', type=int, default=0)
    parser.add_argument('--out-suffix', default='')
    return parser.parse_args()


def output_name(name: str, suffix: str = '') -> str:
    suffix = (suffix or '').strip().lstrip('.')
    return f'{name}.{suffix}' if suffix else name


def deep_mode_of(spec: dict, args) -> str:
    return args.deep_mode or spec.get('mode') or 'Standard Mode'


RUBRIC_AFTER = re.compile(r'\s*:\s*(excellent|good|fair|poor)\b', re.I)


def first_score(
    text: str,
    label: str,
    *,
    last: bool = True,
    lo: float | None = None,
    hi: float | None = None,
) -> float | None:
    heading = re.compile(
        rf'(?:^|\n)#{{1,3}}\s*{label}\b[^\n]*\n+\s*[:\-*]*\s*(\d{{1,2}}(?:\.\d+)?)',
        re.I,
    )
    inline = re.compile(
        rf'(?:\*\*)?{label}(?:\*\*)?\s*[:\-]?\*{{0,2}}\s*(?:\n\s*)?(\d{{1,2}}(?:\.\d+)?)',
        re.I,
    )
    body = text or ''
    hits = []
    for match in list(heading.finditer(body)) + list(inline.finditer(body)):
        value = float(match.group(1))
        if lo is not None and value < lo:
            continue
        if hi is not None and value > hi:
            continue
        if RUBRIC_AFTER.match(body[match.end():match.end() + 24]):
            continue
        hits.append((match.start(), value))
    if not hits:
        return None
    hits.sort()
    return hits[-1][1] if last else hits[0][1]


def parse_decision(body: str) -> str | None:
    for rex in (DECISION_HEAD_RE, DECISION_NL_RE, DECISION_LINE_RE, DECISION_RE):
        hits = list(rex.finditer(body))
        if hits:
            return hits[-1].group(1).capitalize()
    return None


def _fields_from(body: str, kind: str = '') -> dict:
    rating = None
    if kind == 'cycle':
        cut = META_HEAD_RE.search(body)
        head = body[:cut.start()] if cut else body
        ratings = []
        for match in HEADING_RATING_RE.finditer(head):
            value = float(match.group(1))
            if 1 <= value <= 10:
                ratings.append(value)
        if ratings:
            rating = sum(ratings) / len(ratings)
    if rating is None:
        avgs = list(AVG_RE.finditer(body))
        if avgs:
            rating = float(avgs[-1].group(1))
        else:
            rating = first_score(body, r'(?:overall\s+)?rating', last=True, lo=1, hi=10)
    if rating is not None:
        rating = min(10.0, max(1.0, rating))
    decision = parse_decision(body)
    if decision is None and rating is not None:
        decision = 'Accept' if rating >= 6 else 'Reject'
    weak = WEAK_RE.search(body)
    return {
        'rating': rating,
        'decision': decision,
        'soundness': first_score(body, 'soundness', last=True, lo=1, hi=4),
        'presentation': first_score(body, 'presentation', last=True, lo=1, hi=4),
        'contribution': first_score(body, 'contribution', last=True, lo=1, hi=4),
        'weaknesses': ' '.join((weak.group(1) if weak else '').split())[:400],
    }


def parse_review(text: str, kind: str = '') -> dict:
    body = text or ''
    if kind == 'deep':
        body = THINK_RE.sub('', body)
        boxed = extract_boxed_review(body)
        if boxed:
            boxed_fields = _fields_from(boxed)
            if boxed_fields['rating'] is not None or boxed_fields['decision'] is not None:
                return boxed_fields
    return _fields_from(body, kind=kind)


def messages_for(kind: str, paper_text: str, mode: str = 'Standard Mode') -> list[dict]:
    if kind == 'openreviewer':
        return [
            {'role': 'system', 'content': OR_SYSTEM},
            {'role': 'user', 'content': f'Review the following paper:\n\n{paper_text}'},
        ]
    if kind == 'sea':
        return [
            {'role': 'system', 'content': SEA_INSTRUCTION},
            {'role': 'user', 'content': paper_text},
        ]
    if kind == 'deep':
        return [
            {'role': 'system', 'content': deep_system(mode)},
            {'role': 'user', 'content': paper_text},
        ]
    return [
        {'role': 'system', 'content': CYCLE_SYSTEM},
        {'role': 'user', 'content': paper_text},
    ]


def render_text(tokenizer, kind: str, paper: str, mode: str) -> str:
    global _FALLBACK_WARNED
    messages = messages_for(kind, paper, mode)
    try:
        return tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True,
        )
    except Exception as exc:  # noqa: BLE001
        if not _FALLBACK_WARNED:
            print(f'warning: chat template failed ({exc}); using raw join', flush=True)
            _FALLBACK_WARNED = True
        return '\n\n'.join(item['content'] for item in messages)


def render_ids(tokenizer, kind: str, paper: str, mode: str) -> list[int]:
    text = render_text(tokenizer, kind, paper, mode)
    try:
        ids = tokenizer.encode(text, add_special_tokens=False)
    except TypeError:
        ids = tokenizer.encode(text)
    if hasattr(ids, 'tolist'):
        ids = ids.tolist()
    if ids and isinstance(ids[0], list):
        ids = ids[0]
    if not ids or not isinstance(ids[0], int):
        raise TypeError(f'tokenizer.encode returned {type(ids[0]).__name__ if ids else "empty"}')
    return list(ids)


def paper_budget(
    tokenizer, kind: str, max_model_len: int, max_new: int, mode: str,
) -> int:
    used = len(render_ids(tokenizer, kind, '', mode))
    return max(256, max_model_len - max_new - used - 64)


def clip_paper(tokenizer, text: str, budget: int) -> str:
    ids = tokenizer.encode(text)
    if len(ids) <= budget:
        return text
    return tokenizer.decode(ids[:budget])


def paper_text(key: str, max_chars: int, index: dict[str, dict]) -> tuple[str, bool]:
    info = index.get(key) or {}
    if info.get('source') == 'missing' or info.get('n_tokens') == 0:
        return '', False
    return fulltext_for(key, max_chars), bool(info.get('incomplete'))


def score_row(key: str, parsed: dict, *, partial: bool = False, extra: dict | None = None) -> dict:
    row = {'key': key, **parsed}
    if extra:
        row.update(extra)
    if partial:
        row['partial'] = True
    return row


def write_review(review_dir: Path, key: str, text: str) -> None:
    (review_dir / f'{safe_key(key)}.md').write_text(text, encoding='utf-8')


def vllm_prompts(token_ids: list[list[int]]):
    try:
        from vllm import TokensPrompt
        return [TokensPrompt(prompt_token_ids=ids) for ids in token_ids]
    except Exception:  # noqa: BLE001
        return [{'prompt_token_ids': ids} for ids in token_ids]


def run_ai_researcher(name: str, spec: dict, rows: list[dict], args, index: dict) -> None:
    from tqdm import tqdm
    if spec['kind'] == 'cycle':
        from ai_researcher import CycleReviewer
        reviewer = CycleReviewer(model_size=spec['size'])
    else:
        from ai_researcher import DeepReviewer
        reviewer = DeepReviewer(model_size=spec['size'])
    out = scores_path(name)
    review_dir = reviews_dir(name)
    mode = deep_mode_of(spec, args)
    for row in tqdm(rows, desc=name):
        text, partial = paper_text(row['key'], args.max_paper_chars, index)
        if not text:
            append_jsonl(out, {'key': row['key'], 'error': 'no_fulltext'})
            continue
        try:
            if spec['kind'] == 'deep':
                result = reviewer.evaluate(text, mode=mode)
            else:
                result = reviewer.evaluate(text)
            first = result[0] if isinstance(result, list) else result
        except Exception as exc:  # noqa: BLE001
            append_jsonl(out, {'key': row['key'], 'error': str(exc)})
            continue
        rating = first.get('avg_rating') or first.get('rating')
        decision = first.get('paper_decision') or first.get('decision')
        raw = str(first.get('raw_text') or first)[:8000]
        write_review(review_dir, row['key'], raw)
        parsed = parse_review(raw, kind=spec['kind'])
        parsed['rating'] = parsed['rating'] if parsed['rating'] is not None else rating
        parsed['decision'] = parsed['decision'] or decision
        append_jsonl(out, score_row(row['key'], parsed, partial=partial))


def run_vllm(name: str, spec: dict, rows: list[dict], args, index: dict) -> None:
    from tqdm import tqdm
    from vllm import SamplingParams

    max_len = spec['max_len']
    mode = deep_mode_of(spec, args)
    kwargs = {
        'model': spec['repo'],
        'dtype': 'bfloat16',
        'tensor_parallel_size': args.tp,
        'trust_remote_code': True,
        'max_model_len': max_len,
    }
    if spec.get('quant') == 'fp8':
        kwargs['quantization'] = 'fp8'
    llm = make_llm(**kwargs)
    tokenizer = llm.get_tokenizer()
    sample = {
        'temperature': spec.get('temperature', 0.3),
        'max_tokens': spec['max_tokens'],
        'seed': args.seed,
    }
    if spec.get('top_p') is not None:
        sample['top_p'] = spec['top_p']
    try:
        params = SamplingParams(**sample)
    except TypeError:
        sample.pop('seed', None)
        params = SamplingParams(**sample)
    out = scores_path(name)
    review_dir = reviews_dir(name)
    if args.batch_size > 0:
        batch_size = args.batch_size
    elif spec['kind'] == 'deep':
        batch_size = 16 if mode == 'Fast Mode' else 8
    elif spec.get('size') == '70B':
        batch_size = 4
    elif spec.get('size') == '14B':
        batch_size = 16
    else:
        batch_size = 32
    budget = paper_budget(tokenizer, spec['kind'], max_len, spec['max_tokens'], mode)
    print(
        f'{name}: vLLM batch_size={batch_size} paper_budget={budget} '
        f'max_len={max_len} max_tokens={spec["max_tokens"]} seed={args.seed} '
        f'mode={mode!r}',
        flush=True,
    )

    def prompt_for(row: dict) -> tuple[str, bool] | None:
        text, partial = paper_text(row['key'], args.max_paper_chars, index)
        if not text:
            append_jsonl(out, {'key': row['key'], 'error': 'no_fulltext'})
            return None
        text = clip_paper(tokenizer, text, budget)
        return render_text(tokenizer, spec['kind'], text, mode), partial

    def save_output(row: dict, raw: str, finish, partial: bool) -> None:
        write_review(review_dir, row['key'], raw)
        parsed = parse_review(raw, kind=spec['kind'])
        if parsed['rating'] is None and parsed['decision'] is None:
            append_jsonl(out, {
                'key': row['key'],
                'error': f'unparsed:{finish or "ok"}',
                'raw_tail': raw[-300:],
            })
            return
        append_jsonl(out, score_row(row['key'], parsed, partial=partial))

    for start in tqdm(range(0, len(rows), batch_size), desc=name):
        chunk = rows[start:start + batch_size]
        items = []
        for row in chunk:
            item = prompt_for(row)
            if item is not None:
                prompt, partial = item
                items.append((row, prompt, partial))
        if not items:
            continue
        try:
            outputs = llm.generate([prompt for _row, prompt, _partial in items], params)
        except Exception as exc:  # noqa: BLE001
            for row, _prompt, _partial in items:
                append_jsonl(out, {'key': row['key'], 'error': str(exc)})
            continue
        for (row, _prompt, partial), output in zip(items, outputs):
            raw = output.outputs[0].text
            finish = getattr(output.outputs[0], 'finish_reason', None)
            save_output(row, raw, finish, partial)


def main() -> None:
    args = parse_args()
    spec = dict(MODELS[args.model])
    if args.max_tokens > 0:
        spec['max_tokens'] = args.max_tokens
    name = output_name(args.model, args.out_suffix)
    wanted = {part.strip() for part in args.only_keys.split(',') if part.strip()}
    out = scores_path(name)
    done = scored_keys(out)
    index = fulltext_index()
    rows = []
    for row in load_joined():
        if wanted and row['key'] not in wanted:
            continue
        if row['key'] in done:
            continue
        rows.append(row)
    print(f'{name}: {len(done)} cached, {len(rows)} to score', flush=True)
    if not rows:
        return
    if args.backend == 'ai_researcher' and spec['kind'] in {'cycle', 'deep'}:
        run_ai_researcher(name, spec, rows, args, index)
    else:
        run_vllm(name, spec, rows, args, index)
    print(f'{name}: wrote {out}', flush=True)


if __name__ == '__main__':
    main()
