'''Pairwise SciJudge-30B scores, then Bradley-Terry within each year.

    python score_scijudge.py
    python score_scijudge.py --model OpenMOSS-Team/SciJudge-4B-2605
'''

from __future__ import annotations

import argparse
import random
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from data_paths import (  # noqa: E402
    append_jsonl,
    data_dir,
    fill_template,
    load_joined,
    read_jsonl,
    scores_path,
    write_jsonl,
    year_of,
)
from vllm_boot import make_llm  # noqa: E402

ANSWER_RE = re.compile(r'<answer>\s*([AB])\s*</answer>', re.I)
LINE_AB_RE = re.compile(r'(?m)^\s*([AB])\s*$')
TODAY = datetime.now(timezone.utc).strftime('%Y-%m-%d')
PROMPT = (
    'Today is {today}. Based on the titles, abstracts, and publication dates '
    'of the following two papers A and B, determine which paper has a higher '
    'citation count.\n'
    'Show your reasoning process in <reason> </reason> tags. And return the '
    'final answer in <answer> </answer> tags. The final answer should contain '
    'only \'A\' or \'B\'.\n\n'
    'Paper A:\nTitle: {title_a}\nAbstract: {abstract_a}\nDate: {date_a}\n\n'
    'Paper B:\nTitle: {title_b}\nAbstract: {abstract_b}\nDate: {date_b}'
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', default='OpenMOSS-Team/SciJudge-30B-2605')
    parser.add_argument('--k', type=int, default=8)
    parser.add_argument('--seed', type=int, default=0)
    parser.add_argument('--max-tokens', type=int, default=1024)
    parser.add_argument('--tp', type=int, default=1)
    return parser.parse_args()


def pair_id(shown_a: str, shown_b: str) -> str:
    return f'{shown_a}|{shown_b}|ab'


def build_pairs(rows: list[dict], k: int, seed: int) -> list[tuple[dict, dict]]:
    by_year: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        if not (row.get('title') or row.get('abstract')):
            continue
        by_year[year_of(row)].append(row)
    rng = random.Random(seed)
    pairs = []
    seen: set[tuple[str, str]] = set()
    for group in by_year.values():
        if len(group) < 2:
            continue
        lookup = {item['key']: item for item in group}
        for row in group:
            others = [item for item in group if item['key'] != row['key']]
            rivals = rng.sample(others, k=min(k, len(others)))
            for rival in rivals:
                unordered = tuple(sorted((row['key'], rival['key'])))
                if unordered in seen:
                    continue
                seen.add(unordered)
                left, right = lookup[unordered[0]], lookup[unordered[1]]
                pairs.append((left, right))
                pairs.append((right, left))
    return pairs


def parse_winner(text: str) -> str | None:
    match = ANSWER_RE.search(text or '')
    if match:
        return match.group(1).upper()
    if '<answer>' in (text or '').lower():
        return None
    lines = [line.strip() for line in (text or '').splitlines() if line.strip()]
    if lines and LINE_AB_RE.fullmatch(lines[-1]):
        return lines[-1].strip().upper()
    return None


def bradley_terry(keys: list[str], wins: list[tuple[str, str]], ridge: float = 0.1):
    '''MM update: π_i ← (W_i + λ) / (Σ_j n_ij/(π_i+π_j) + λ), then s = log π.'''
    import numpy as np
    if not keys:
        return {}
    index = {key: i for i, key in enumerate(keys)}
    n = len(keys)
    strength = np.zeros(n)
    for _ in range(80):
        pi = np.exp(strength)
        wins_i = np.zeros(n)
        inv = np.zeros(n)
        for winner, loser in wins:
            if winner not in index or loser not in index:
                continue
            i, j = index[winner], index[loser]
            total = float(pi[i] + pi[j] + 1e-12)
            wins_i[i] += 1
            inv[i] += 1.0 / total
            inv[j] += 1.0 / total
        nxt = np.log(np.maximum(wins_i + ridge, 1e-12)) - np.log(np.maximum(inv + ridge, 1e-12))
        nxt -= nxt.mean()
        if float(np.max(np.abs(nxt - strength))) < 1e-5:
            strength = nxt
            break
        strength = nxt
    return {key: float(strength[index[key]]) for key in keys}


def main() -> None:
    args = parse_args()
    rows = load_joined()
    pairs = build_pairs(rows, args.k, args.seed)
    pair_file = data_dir() / 'scores_scijudge_pairs.jsonl'
    done = {
        row['pair_id'] for row in read_jsonl(pair_file)
        if row.get('pair_id') and row.get('winner') in ('A', 'B')
    }
    pending = []
    for left, right in pairs:
        pid = pair_id(left['key'], right['key'])
        if pid not in done:
            pending.append((left, right, pid))
    print(f'scijudge: {len(done)} pairs cached, {len(pending)} to run', flush=True)

    if pending:
        from tqdm import tqdm
        from vllm import SamplingParams

        llm = make_llm(
            model=args.model,
            dtype='bfloat16',
            tensor_parallel_size=args.tp,
            trust_remote_code=True,
            max_model_len=8192,
        )
        tokenizer = llm.get_tokenizer()
        try:
            params = SamplingParams(
                temperature=0.7,
                top_p=0.8,
                top_k=20,
                max_tokens=args.max_tokens,
                seed=args.seed,
            )
        except TypeError:
            params = SamplingParams(
                temperature=0.7,
                top_p=0.8,
                top_k=20,
                max_tokens=args.max_tokens,
            )
        batch = 8
        for start in tqdm(range(0, len(pending), batch), desc='scijudge'):
            chunk = pending[start:start + batch]
            prompts = []
            for a, b, _pid in chunk:
                user = fill_template(
                    PROMPT,
                    today=TODAY,
                    title_a=a.get('title') or '',
                    abstract_a=a.get('abstract') or '',
                    date_a=a.get('published') or '',
                    title_b=b.get('title') or '',
                    abstract_b=b.get('abstract') or '',
                    date_b=b.get('published') or '',
                )
                messages = [
                    {
                        'role': 'system',
                        'content': (
                            'You are a helpful assistant. You first think about '
                            'the reasoning process in your mind and then provide '
                            'the user with the answer.'
                        ),
                    },
                    {'role': 'user', 'content': user},
                ]
                prompts.append(
                    tokenizer.apply_chat_template(
                        messages, tokenize=False, add_generation_prompt=True,
                    )
                )
            outputs = llm.generate(prompts, params)
            for item, output in zip(chunk, outputs):
                a, b, pid = item
                text = output.outputs[0].text
                append_jsonl(pair_file, {
                    'pair_id': pid,
                    'a': a['key'],
                    'b': b['key'],
                    'winner': parse_winner(text),
                    'raw': text[-500:],
                })

    results = read_jsonl(pair_file)
    row_map = {row['key']: row for row in rows}
    by_year: dict[str, list[str]] = defaultdict(list)
    for row in rows:
        by_year[year_of(row)].append(row['key'])
    wins_by_year: dict[str, list[tuple[str, str]]] = defaultdict(list)
    played: dict[str, list[int]] = defaultdict(lambda: [0, 0])
    for item in results:
        if item.get('winner') not in ('A', 'B'):
            continue
        winner_key = item['a'] if item['winner'] == 'A' else item['b']
        loser_key = item['b'] if item['winner'] == 'A' else item['a']
        year = year_of(row_map.get(item.get('a'), {}))
        wins_by_year[year].append((winner_key, loser_key))
        played[winner_key][0] += 1
        played[winner_key][1] += 1
        played[loser_key][1] += 1

    out_rows = []
    for year, keys in by_year.items():
        eligible = [key for key in keys if played[key][1] > 0]
        scores = bradley_terry(eligible, wins_by_year.get(year, []))
        for key in keys:
            wins, n = played[key]
            if not n:
                continue
            out_rows.append({
                'key': key,
                'bt_score': scores.get(key),
                'win_rate': wins / n,
                'n_valid': n,
                'year': year,
            })
    write_jsonl(scores_path('scijudge'), out_rows)
    print(f'scijudge: wrote {scores_path("scijudge")} ({len(out_rows)} rows)', flush=True)


if __name__ == '__main__':
    main()
