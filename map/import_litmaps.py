'''Build map/litmaps.json from the Litmaps CSV + the tagged paper list.

CSV supplies global citation / reference counts. The pasted list supplies tags
(the CSV Tags column is empty).

Run:  python map/import_litmaps.py [csv] [list.txt]
'''

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import MAP_DIR, dump_json, norm_title

LITMAPS = MAP_DIR / 'litmaps.json'
DEFAULT_CSV = Path(r'D:\Downloads\All Papers (5).csv')
DEFAULT_LIST = MAP_DIR / 'litmaps_list.txt'

HEAD = re.compile(r'^.+, (?:19|20)\d{2}$')
VENUE = re.compile(
    r'^(arxiv|proceedings|international conference|aaai |nature |'
    r'the naturalist|trans\.|plos |research square|cold spring|'
    r'aaai conference)',
    re.I,
)
COUNT = re.compile(r'^\d+(?:\.\d+)?k?$')
SKIP = {
    'references', 'citations', 'citation', 'tag', 'add to litmap', 'remove',
}

CANON_TAGS = [
    'Catastrophic forgetting',
    'Mathematical Reasoning in Neural Networks and Language Models',
    'Alignment & Coherence & Mechanistic Interpretability and Internal Representations',
    'Alignment & Coherence & Mechanistic Interpretability',
    'Scaling, Training Efficiency, and Optimization',
    'Reinforcement Learning Algorithms and Applications',
    'Optimizers and Gradient Descent',
    'Generalization and Model Robustness',
    'Architectural Innovations in Deep Learning',
    'Prompt Engineering and Task Adaptation',
    'Jepa',
    'Self-Improvement and Adaptation in AI Systems',
    'Recurrent Models',
    'Self-refining',
    'Stepping stone',
    'Self-distillation',
    'Continual Learning and Plasticity',
    'Feedback Mechanisms and Learning Paradigms',
    'Environment Generation',
    'AI in Scientific Discovery and Problem Solving',
    'Heuristic Approaches in Language Models',
    'Encoder-Decoder',
    'Recursive Models',
    'Evolutionary Approaches in AI',
]

TAG_SHORT = {
    'Catastrophic forgetting': 'Forgetting',
    'Mathematical Reasoning in Neural Networks and Language Models':
        'Math reasoning',
    'Alignment & Coherence & Mechanistic Interpretability and Internal Representations':
        'Interp',
    'Alignment & Coherence & Mechanistic Interpretability': 'Interp',
    'Scaling, Training Efficiency, and Optimization': 'Scaling',
    'Reinforcement Learning Algorithms and Applications': 'RL',
    'Optimizers and Gradient Descent': 'Optimizers',
    'Generalization and Model Robustness': 'Generalization',
    'Architectural Innovations in Deep Learning': 'Architecture',
    'Prompt Engineering and Task Adaptation': 'Prompts',
    'Jepa': 'JEPA',
    'Self-Improvement and Adaptation in AI Systems': 'Self-improve',
    'Recurrent Models': 'Recurrent',
    'Self-refining': 'Self-refine',
    'Stepping stone': 'Stepping stone',
    'Self-distillation': 'Self-distill',
    'Continual Learning and Plasticity': 'Continual',
    'Feedback Mechanisms and Learning Paradigms': 'Feedback',
    'Environment Generation': 'Environments',
    'AI in Scientific Discovery and Problem Solving': 'Discovery',
    'Heuristic Approaches in Language Models': 'Heuristics',
    'Encoder-Decoder': 'Enc-dec',
    'Recursive Models': 'Recursive',
    'Evolutionary Approaches in AI': 'Evolution',
}


def canon_tag(raw: str) -> str | None:
    text = ' '.join(raw.split()).strip()
    if not text or text.lower() in SKIP or COUNT.match(text):
        return None
    if text.startswith('<') or VENUE.match(text) or HEAD.match(text):
        return None
    for name in CANON_TAGS:
        if text == name or name.startswith(text) or text.startswith(name):
            return name
    if len(text) >= 8 and not text[0].isdigit():
        return text
    return None


def parse_list(text: str) -> list[dict]:
    lines = [ln.strip() for ln in text.splitlines()]
    heads = [i for i, ln in enumerate(lines) if HEAD.match(ln)]
    papers, seen = [], set()
    for n, start in enumerate(heads):
        end = heads[n + 1] if n + 1 < len(heads) else len(lines)
        block = lines[start:end]
        author, year = block[0].rsplit(', ', 1)
        title_parts, tags = [], []
        after_cites = False
        for ln in block[1:]:
            if not ln or ln.lower() in SKIP:
                if ln.lower() in ('citations', 'citation', 'tag'):
                    after_cites = True
                continue
            if COUNT.match(ln) or ln.lower() == 'references':
                continue
            if VENUE.match(ln):
                continue
            if after_cites:
                tag = canon_tag(ln)
                if tag:
                    tags.append(tag)
                continue
            title_parts.append(ln)
        title = ' '.join(title_parts)
        key = (norm_title(title), year)
        if key in seen:
            for paper in papers:
                if (paper['norm'], paper['year']) == key:
                    for tag in tags:
                        if tag not in paper['tags']:
                            paper['tags'].append(tag)
            continue
        seen.add(key)
        papers.append({
            'title': title,
            'norm': norm_title(title),
            'author': author,
            'year': year,
            'tags': tags,
            'lit_cites': None,
            'lit_refs': None,
        })
    return papers


def parse_csv(path: Path) -> list[dict]:
    with path.open(encoding='utf-8-sig', newline='') as handle:
        return list(csv.DictReader(handle))


def tokens(text: str) -> set[str]:
    return {w for w in text.split() if len(w) > 2}


def title_score(query: str, candidate: str) -> float:
    q, c = norm_title(query), norm_title(candidate)
    if not q or not c:
        return 0.0
    if q == c or q in c or c in q:
        return 8.0
    qt, ct = tokens(q), tokens(c)
    if not qt or not ct:
        return 0.0
    return len(qt & ct) / len(qt | ct)


def attach_csv(papers: list[dict], rows: list[dict]) -> None:
    used = set()
    for paper in papers:
        ranked = []
        for i, row in enumerate(rows):
            if i in used:
                continue
            s = title_score(paper['title'], row.get('Title') or '')
            if s >= 0.55:
                ranked.append((s, i))
        ranked.sort(reverse=True)
        if not ranked:
            continue
        used.add(ranked[0][1])
        row = rows[ranked[0][1]]
        try:
            paper['lit_cites'] = int(row.get('Cited By') or 0)
        except ValueError:
            paper['lit_cites'] = 0
        try:
            paper['lit_refs'] = int(row.get('References') or 0)
        except ValueError:
            paper['lit_refs'] = 0


def shorten(tags: list[str]) -> list[str]:
    out, seen = [], set()
    for tag in tags:
        short = TAG_SHORT.get(tag, tag)
        if short not in seen:
            seen.add(short)
            out.append(short)
    return out


def main() -> None:
    csv_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_CSV
    list_path = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_LIST
    papers = parse_list(list_path.read_text(encoding='utf-8'))
    attach_csv(papers, parse_csv(csv_path))
    payload = []
    tagged = 0
    for paper in papers:
        tags = shorten(paper['tags'])
        tagged += bool(tags)
        payload.append({
            'title': paper['title'],
            'author': paper['author'],
            'year': paper['year'],
            'lit_cites': paper['lit_cites'],
            'lit_refs': paper['lit_refs'],
            'tags': tags,
        })
    dump_json(LITMAPS, {'papers': payload})
    print(f'wrote {LITMAPS.name}: {len(payload)} papers, {tagged} tagged')
    from collections import Counter
    counts = Counter(tag for p in payload for tag in p['tags'])
    for tag, n in counts.most_common():
        print(f'  {n:3d}  {tag}')


if __name__ == '__main__':
    main()
