'''Build the lazy fulltext corpus for the citation-map search box.

Reads filter/fulltext/<safe_key>.md, drops the bibliography, keeps body and
appendix, and writes assets/fulltext_search.js as window.FULLTEXT_SEARCH.

Run:  python src/build_fulltext_search.py
'''

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import FULLTEXT_DIR, FULLTEXT_SEARCH_JS, GRAPH, load_json, safe_key

REF_HEAD = re.compile(
    r'^#{1,6}\s+(references|bibliography|works cited)\b',
    re.I,
)
APP_HEAD = re.compile(
    r'^#{1,6}\s+(?:\d+\.?\s+)?'
    r'(appendix|supplementary|supplemental|supplement)\b',
    re.I,
)

ABDUCT_KEYS = ('openreview:klU4737opt', 'arxiv:2608.19197')
WS_RE = re.compile(r'\s+')


def search_blob(markdown: str) -> str:
    keep = []
    skip = False
    for line in markdown.splitlines():
        stripped = line.strip()
        if REF_HEAD.match(stripped):
            skip = True
            continue
        if APP_HEAD.match(stripped):
            skip = False
        if not skip:
            keep.append(line)
    return WS_RE.sub(' ', ' '.join(keep).lower()).strip()


def print_progress(done: int, total: int, extra: str = '') -> None:
    pct = 100 * done / total if total else 100
    suffix = f'  {extra}' if extra else ''
    print(f'\rprogress: {done}/{total} ({pct:.0f}%){suffix}', end='', flush=True)
    if done >= total:
        print(flush=True)


def build_corpus(ids: list[str]) -> dict[str, str]:
    corpus: dict[str, str] = {}
    total = len(ids)
    for index, node_id in enumerate(ids, start=1):
        path = FULLTEXT_DIR / f'{safe_key(node_id)}.md'
        extra = ''
        if path.exists():
            extra = node_id
            blob = search_blob(path.read_text(encoding='utf-8'))
            if blob:
                corpus[node_id] = blob
        print_progress(index, total, extra)
    return corpus


def write_js(path: Path, corpus: dict[str, str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + '.tmp')
    payload = json.dumps(corpus, ensure_ascii=False)
    payload = payload.replace('\u2028', '\\u2028').replace('\u2029', '\\u2029')
    tmp.write_text(
        'window.FULLTEXT_SEARCH = ' + payload + ';\n',
        encoding='utf-8',
    )
    tmp.replace(path)


def check_corpus(corpus: dict[str, str]) -> None:
    for key in ABDUCT_KEYS:
        blob = corpus.get(key, '')
        if 'abduct' not in blob:
            raise SystemExit(f'fulltext self-check failed: {key} missing abduct')
    numbered = corpus.get('arxiv:2007.02789', '')
    if 'variance-covariance matrix of the distance estimate' not in numbered:
        raise SystemExit(
            'fulltext self-check failed: arxiv:2007.02789 dropped numbered appendix'
        )


def build_and_write(ids: list[str]) -> dict[str, str]:
    corpus = build_corpus(ids)
    write_js(FULLTEXT_SEARCH_JS, corpus)
    print(f'fulltext search  {len(corpus)} with text / {len(ids)} nodes')
    print(f'wrote {FULLTEXT_SEARCH_JS}')
    return corpus


def main() -> None:
    graph = load_json(GRAPH, {})
    ids = [node['id'] for node in graph.get('nodes') or [] if node.get('id')]
    if not ids:
        raise SystemExit(f'no nodes in {GRAPH}')
    corpus = build_and_write(ids)
    if '--self-check' in sys.argv[1:]:
        check_corpus(corpus)


if __name__ == '__main__':
    main()
