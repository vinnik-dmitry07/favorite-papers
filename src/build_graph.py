'''Match retrieved references against the catalog and emit assets/graph.json.

An edge `a -> b` means "a cites b"; only pairs where both ends are catalog
entries survive. Node `cites` is the in-corpus in-degree, which is what the
map uses as its vertical axis.

Run:  python src/build_graph.py [--report N]
'''

import re
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import (  # noqa: E402
    ARXIV_META, ASSETS, CATALOG, GRAPH, GRAPH_JS, KNOWN_META, LITMAPS,
    PAGE_META, REFS, ROOT, apply_date_overrides, classify, clean_arxiv_id,
    clean_doi, DOI_RE,
    dump_json, load_json, node_arxiv_ids, norm_title, url_slug,
)

# A cited work published long after the citing paper means the title matcher
# latched onto the wrong entry; genuine late citations come from revisions.
FUTURE_SLACK = timedelta(days=730)
SCHOLARLY_KINDS = ('doi', 'acl', 'openreview')
LABEL_YEAR_RE = re.compile(r'\b(19[89]\d|20[0-4]\d)\b')
STOP_WORDS = {
    'the', 'a', 'an', 'on', 'of', 'in', 'to', 'and', 'for', 'is', 'how',
    'why', 'when', 'what', 'from', 'with', 'into', 'your', 'this', 'that',
}
PAREN_RE = re.compile(r'\(([^)]+)\)')
# Parentheticals that name a venue, author, or lab — not a method.
SKIP_PAREN_RE = re.compile(
    r'\b(neurips|iclr|icml|acl|emnlp|nature|pnas|plos|workshop|best|'
    r'series|et al|meta$|^meta\b|google|deepmind|openai|anthropic|sakana|'
    r'nvidia|fair|airi|weco|lilian|weng|cameron|wolfe|schmidhuber|'
    r'chalmers|kokotajlo|aschenbrenner|kambhampati|shanahan|bishop|'
    r'alignment|forum|iscience|biorxiv|precursor|october|july|clune|'
    r'lecun|sutton|kean|fedorenko|kantamneni|tegmark|tufa|intellect|'
    r'oreilly|whittington|sergey|ivanov|epoch|airi|nagel|kelly|'
    r'problem collection|geometry processing|speech generation|'
    r'strong baseline|human-level|open language|superalignment|'
    r'thinking machines|alex zhang|prime intellect|reilly|'
    r'20\d{2})\b',
    re.I,
)


def arxiv_hint(meta: dict) -> str | None:
    '''arXiv id behind a page that turned out to be a paper landing page.'''
    resolved = meta.get('resolved')
    classified = classify(resolved) if resolved else None
    if classified and classified[0] == 'arxiv':
        return classified[1].split(':', 1)[1]
    return None


def merge_metadata(catalog: list[dict], page_meta: dict) -> None:
    '''Fill gaps in the catalog with whatever the fetch stage discovered.'''
    arxiv_known: dict[str, dict] = {}
    for name in ('papers_titles.json', 'added_titles.json'):
        arxiv_known.update(load_json(ASSETS / name, {}))
    arxiv_known.update(load_json(ARXIV_META, {}))
    overrides = load_json(KNOWN_META, {})

    for node in catalog:
        meta = page_meta.get(node['id'], {})
        hint = arxiv_hint(meta) if node['kind'] != 'arxiv' else None
        if hint:
            # Timestamps on such pages describe the discussion, not the paper.
            node['date'] = None
            node['date_source'] = None
            info = arxiv_known.get(hint)
            if info:
                node['fetched_title'] = info['title']
                node['authors'] = info.get('authors') or []
                node['date'] = info.get('published') or None
                node['date_source'] = 'arxiv-api'
            meta = {}
        if node['kind'] != 'arxiv':
            if meta.get('date') and not node['date']:
                node['date'] = meta['date']
                node['date_source'] = 'page-meta'
            if meta.get('authors') and not node['authors']:
                node['authors'] = meta['authors']
            # og:title on a marketing page is often just the site name, so only
            # trust fetched titles from scholarly sources.
            if meta.get('title') and node['kind'] in SCHOLARLY_KINDS:
                node['fetched_title'] = ' '.join(meta['title'].split())
        if not node['date'] and node['kind'] == 'acl':
            year = re.match(r'^(20\d{2})\.', node['id'].split(':', 1)[1])
            if year:
                node['date'] = f'{year.group(1)}-06-30'
                node['date_source'] = 'venue-year'
        if not node['date']:
            years = LABEL_YEAR_RE.findall(node['label'])
            if years:
                node['date'] = f'{max(years)}-06-30'
                node['date_source'] = 'label-year'
        apply_date_overrides(node, arxiv_known, overrides)


def surname(name: str) -> str:
    parts = [p for p in re.split(r'[\s.]+', name.strip()) if p]
    return parts[-1] if parts else ''


def _clean_token(text: str) -> str:
    return ' '.join(text.replace('\u2014', '-').replace('\u2013', '-').split())


GENERIC_WORDS = {
    'survey', 'review', 'book', 'analysis', 'approach', 'tutorial',
    'position', 'proof', 'mapping', 'learning', 'sometimes', 'methods',
    'system', 'art', 'skip', 'people', 'incorrect', 'unreasonable',
    'toward', 'towards', 'beyond', 'revisiting', 'rethinking', 'why',
    'how', 'when', 'what', 'could', 'can', 'does', 'do', 'from',
    'understanding', 'addressing', 'evaluating', 'comparing',
    'estimating', 'detecting', 'reinforcement', 'evolutionary',
    'gradient', 'emergent', 'formal', 'modular', 'competitive',
    'lookahead', 'reinforcing', 'constitutional', 'palatable',
    'parametrically', 'activation', 'tracing', 'attribution', 'sparse',
    'consciousness', 'photonic', 'optical', 'intelligent', 'virtue',
    'tokens', 'attractor', 'relating', 'sleep', 'neural', 'social',
    'definition', 'externalization', 'competition', 'emergence',
    'evaluation', 'incorrect', 'extremely', 'harnesses', 'language',
    'a', 'an', 'the', 'tasks',
}

def _paren_candidates(text: str) -> list[str]:
    '''Method-like pieces pulled out of parentheses, last one preferred.'''
    found = []
    for raw in PAREN_RE.findall(text):
        for piece in re.split(r'\s*[/,]\s*', raw):
            piece = _clean_token(piece)
            if not 2 <= len(piece) <= 22 or piece[0].isdigit():
                continue
            if SKIP_PAREN_RE.search(piece):
                continue
            if piece.lower() in GENERIC_WORDS:
                continue
            words = piece.split()
            if len(words) > 3:
                continue
            if not re.search(r'[A-Z0-9]', piece):
                continue
            found.append(piece)
    return found


def _is_coined(token: str) -> bool:
    '''True for invented names, not ordinary English.'''
    if re.search(r'[0-9+\-/]', token):
        return True
    if re.search(r'[A-Z][a-z]+[A-Z]', token):
        return True
    if re.fullmatch(r'[A-Z]{3,10}', token):
        return True
    if re.fullmatch(r'[A-Z][a-z]+(?:[A-Z][a-zA-Z0-9]+)+', token):
        return True
    return False


def _looks_like_method(text: str) -> bool:
    '''True for short coined names: DAPO, DreamerV3, rStar-Math, SALE.'''
    text = _clean_token(text)
    if not 2 <= len(text) <= 24:
        return False
    words = [w for w in text.split() if w.lower() not in STOP_WORDS]
    if not words or len(words) > 2:
        return False
    token = ' '.join(words)
    if token.lower() in GENERIC_WORDS or SKIP_PAREN_RE.search(token):
        return False
    if not re.fullmatch(
        r'[A-Za-z][A-Za-z0-9.+/\-.]*'
        r'(?:\s+(?:[A-Z][A-Za-z0-9.+/\-.]*|[0-9]+))?',
        token,
    ):
        return False
    return True


def _trailing_method(text: str) -> str | None:
    '''A coined phrase at the end: Double Q-learning, Dr. GRPO.'''
    words = [w for w in re.split(r'[\s:,/]+', text) if w]
    for count in (2, 1):
        if len(words) < count:
            continue
        chunk = ' '.join(words[-count:])
        if any(w.lower() in STOP_WORDS for w in chunk.split()):
            continue
        if not _looks_like_method(chunk):
            continue
        if not any(_is_coined(w) for w in chunk.split()):
            continue
        return chunk
    return None


def method_keyword(entry: str, title: str) -> str:
    '''One short name for the map: usually the method, else a compact title.'''
    entry = _clean_token(entry or '')
    title = _clean_token(title or '')
    if 'f(g(x))' in entry.lower():
        return 'f(g(x))'
    bare = _clean_token(PAREN_RE.sub(' ', entry)).rstrip(' -:')

    parens = _paren_candidates(entry) + _paren_candidates(title)
    if parens:
        return parens[-1]

    if ':' in entry:
        head, tail = [p.strip() for p in entry.split(':', 1)]
        head = _clean_token(PAREN_RE.sub(' ', head))
        tail = _clean_token(PAREN_RE.sub(' ', tail))
        if _looks_like_method(head):
            return ' '.join(w for w in head.split() if w.lower() not in STOP_WORDS)
        trail = _trailing_method(tail)
        if trail:
            return trail

    if '/' in bare:
        right = bare.rsplit('/', 1)[-1].strip()
        if _looks_like_method(right):
            return right

    if re.fullmatch(r'\d+(?:\.\d+)?', bare):
        if 'physics of language' in title.lower():
            return f'PoLM {bare}'
        return (title.split(':')[0] if title else bare)[:18]

    if _looks_like_method(bare):
        return bare
    if 2 <= len(bare) <= 18 and bare.lower() not in GENERIC_WORDS:
        return bare
    first = bare.split()[0] if bare else ''
    if _is_coined(first) and _looks_like_method(first):
        return first

    trail = _trailing_method(bare) or _trailing_method(title)
    if trail and trail.lower() not in GENERIC_WORDS:
        return trail

    source = title if len(bare) <= 3 and title else (bare or title)
    words = [w for w in re.split(r'[\s:,/?]+', source) if w]
    picked, total = [], 0
    for word in words:
        low = word.lower().strip('-.')
        if not picked and (low in STOP_WORDS or low in GENERIC_WORDS):
            continue
        if picked and (low in STOP_WORDS or total + len(word) > 22):
            break
        picked.append(word)
        total += len(word) + 1
        if len(picked) == 2:
            break
    return ' '.join(picked) or (bare or title)[:18]


def display_label(node: dict) -> str:
    year = node['date'][:4] if node['date'] else None
    if node['authors']:
        who = surname(node['authors'][0])
    else:
        words = [w for w in re.split(r'[\s:,/(-]+', node['label']) if w]
        picked, total = [], 0
        for word in words:
            if picked and (total + len(word) > 20):
                break
            if not picked and word.lower() in STOP_WORDS:
                continue
            picked.append(word)
            total += len(word) + 1
        who = ' '.join(picked) or node['label'][:20]
    return f'{who}, {year}' if year else who


def build_indices(
    catalog: list[dict],
    overrides: dict | None = None,
    page_meta: dict | None = None,
) -> dict[str, dict[str, str]]:
    '''Every identifier that can point at a catalog entry.'''
    index = {'arxiv': {}, 'doi': {}, 'openreview': {}, 'acl': {}, 'url': {}}
    overrides = overrides if overrides is not None else load_json(KNOWN_META, {})
    page_meta = page_meta if page_meta is not None else {}
    canonical_arxiv = {
        node['id'].split(':', 1)[1]
        for node in catalog if node['kind'] == 'arxiv'
    }
    for node in catalog:
        for url in node['urls']:
            classified = classify(url)
            if not classified:
                continue
            kind, node_key = classified
            value = node_key.split(':', 1)[1]
            bucket = index[kind] if kind in index else index['url']
            bucket.setdefault(value, node['id'])
            if kind not in index:
                index['url'].setdefault(url_slug(url), node['id'])
            embedded = DOI_RE.search(url)
            if embedded:
                index['doi'].setdefault(clean_doi(embedded.group(1)), node['id'])
        for aid in node_arxiv_ids(node, overrides, page_meta):
            if node['kind'] != 'arxiv' and aid in canonical_arxiv:
                continue
            index['arxiv'].setdefault(aid, node['id'])
    return index


def resolve(refs: dict, index: dict, known: set[str]) -> dict[str, str]:
    '''Map each matched target to how it was matched: id, url or title.'''
    targets: dict[str, str] = {}

    def record(node_id: str | None, evidence: str) -> None:
        if node_id and node_id not in targets:
            targets[node_id] = evidence

    for raw in refs.get('arxiv', []):
        record(index['arxiv'].get(clean_arxiv_id(raw)), 'id')
    for raw in refs.get('doi', []):
        record(index['doi'].get(clean_doi(raw)), 'id')
    for url in refs.get('urls', []):
        classified = classify(url)
        if not classified:
            continue
        kind, node_key = classified
        value = node_key.split(':', 1)[1]
        record(index.get(kind, {}).get(value) or index['url'].get(url_slug(url)),
               'url')
    for node_id in refs.get('titles', []):
        if node_id in known:
            record(node_id, 'title')
    return targets


def parse_date(value: str | None) -> date | None:
    if not value:
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


def _title_tokens(text: str) -> set[str]:
    return {w for w in norm_title(text).split() if len(w) > 2}


def litmaps_score(node: dict, paper: dict) -> float:
    query = norm_title(paper.get('title') or '')
    titles = [
        norm_title(node.get('title') or ''),
        norm_title(node.get('entry') or ''),
    ]
    if not query:
        return 0.0
    for candidate in titles:
        if not candidate:
            continue
        if query == candidate:
            return 10.0
        shorter, longer = (
            (query, candidate) if len(query) <= len(candidate)
            else (candidate, query)
        )
        if shorter in longer and len(shorter) >= 0.6 * len(longer):
            return 8.0
    qt = _title_tokens(query)
    extras = titles + [norm_title(node.get('keyword') or '')]
    ct = set().union(*(_title_tokens(t) for t in extras if t))
    if not qt or not ct:
        return 0.0
    return len(qt & ct) / len(qt | ct)


def attach_litmaps(nodes_out: list[dict]) -> None:
    '''Copy Litmaps citations, references, and tags onto matched nodes.'''
    papers = load_json(LITMAPS, {}).get('papers') or []
    for node in nodes_out:
        node['tags'] = []
        node['topic'] = None
        node['lit_cites'] = None
        node['lit_refs'] = None
    used: set[int] = set()
    matched = 0
    for paper in papers:
        ranked = []
        for i, node in enumerate(nodes_out):
            if i in used:
                continue
            score = litmaps_score(node, paper)
            if score >= 0.55:
                ranked.append((score, i))
        if not ranked:
            continue
        ranked.sort(reverse=True)
        node = nodes_out[ranked[0][1]]
        used.add(ranked[0][1])
        node['tags'] = list(paper.get('tags') or [])
        node['topic'] = node['tags'][0] if node['tags'] else None
        node['lit_cites'] = paper.get('lit_cites')
        node['lit_refs'] = paper.get('lit_refs')
        matched += 1
    print(f'litmaps overlay     {matched}/{len(papers)} papers matched')


def main() -> None:
    args = sys.argv[1:]
    report = 0
    if '--report' in args:
        report = int(args[args.index('--report') + 1])

    catalog = load_json(CATALOG, [])
    refs_all = load_json(REFS, {})
    page_meta = load_json(PAGE_META, {})
    if not catalog:
        raise SystemExit('assets/catalog.json missing - run src/parse_readme.py')

    merge_metadata(catalog, page_meta)
    index = build_indices(catalog, load_json(KNOWN_META, {}), page_meta)
    known = {node['id'] for node in catalog}
    dates = {node['id']: parse_date(node['date']) for node in catalog}

    edges: list[tuple[str, str, str]] = []
    dropped_future = []
    raw_ref_total = 0
    with_docs = 0

    for node in catalog:
        refs = refs_all.get(node['id'], {})
        if refs.get('status') in ('cached', 'fetched'):
            with_docs += 1
        raw_ref_total += (len(refs.get('arxiv', [])) + len(refs.get('doi', []))
                          + len(refs.get('titles', [])))
        src_date = dates.get(node['id'])
        for target, evidence in sorted(resolve(refs, index, known).items()):
            if target == node['id']:
                continue
            dst_date = dates.get(target)
            if src_date and dst_date and dst_date - src_date > FUTURE_SLACK:
                dropped_future.append((node['id'], target,
                                       str(src_date), str(dst_date)))
                continue
            edges.append((node['id'], target, evidence))

    in_degree = {node['id']: 0 for node in catalog}
    out_degree = {node['id']: 0 for node in catalog}
    for src, dst, _ in edges:
        in_degree[dst] += 1
        out_degree[src] += 1

    order = {node['id']: i for i, node in enumerate(catalog)}
    nodes_out = []
    for node in catalog:
        refs = refs_all.get(node['id'], {})
        nodes_out.append({
            'id': node['id'],
            'label': display_label(node),
            'keyword': method_keyword(
                node['label'], node.get('fetched_title') or node['title']
            ),
            'title': node.get('fetched_title') or node['title'],
            'entry': node['label'],
            'authors': node['authors'],
            'date': node['date'],
            'date_source': node['date_source'],
            'section': node['section'],
            'kind': node['kind'],
            'url': node['urls'][0],
            'cites': in_degree[node['id']],
            'refs': out_degree[node['id']],
            'doc': refs.get('status') in ('cached', 'fetched'),
            'bib_items': refs.get('bib_items', 0),
        })
        if node.get('telegram'):
            nodes_out[-1]['telegram'] = True
    attach_litmaps(nodes_out)

    graph = {
        'generated': date.today().isoformat(),
        'source': 'readme.md + references parsed from arXiv/ar5iv HTML, '
                  'page HTML and Crossref',
        'nodes': nodes_out,
        'edges': [[order[s], order[d], e] for s, d, e in edges],
    }
    dump_json(GRAPH, graph)
    GRAPH_JS.write_text(
        'window.GRAPH_DATA = '
        + Path(GRAPH).read_text(encoding='utf-8')
        + ';\n',
        encoding='utf-8',
    )

    dated = sum(1 for n in nodes_out if n['date'])
    connected = sum(1 for n in nodes_out if n['cites'] or n['refs'])
    by_evidence: dict[str, int] = {}
    for _, _, evidence in edges:
        by_evidence[evidence] = by_evidence.get(evidence, 0) + 1
    print(f'nodes           {len(nodes_out)}')
    print(f'  with a document read   {with_docs}')
    print(f'  with a date            {dated}')
    print(f'  touching >=1 edge      {connected}')
    print(f'raw refs extracted       {raw_ref_total}')
    print(f'edges kept               {len(edges)}  ('
          + ', '.join(f'{k}={v}' for k, v in sorted(by_evidence.items())) + ')')
    print(f'edges dropped (target >2y newer) {len(dropped_future)}')
    print(f'\nwrote {GRAPH.relative_to(ROOT)} and {GRAPH_JS.relative_to(ROOT)}')

    top = sorted(nodes_out, key=lambda n: -n['cites'])[:12]
    print('\nmost cited inside the corpus:')
    for node in top:
        print(f'  {node["cites"]:3d}  {node["label"]:26s} {node["title"][:58]}')

    if report:
        titles = {node['id']: node['label'] for node in nodes_out}
        print('\nsample dropped edges:')
        for src, dst, sd, dd in dropped_future[:report]:
            print(f'  {src} ({sd}) -> {dst} ({dd})')
        print('\nsample title-only matches (least certain evidence):')
        shown = 0
        for src, dst, evidence in edges:
            if evidence != 'title':
                continue
            print(f'  {titles[src]:24s} -> {titles[dst]:24s} '
                  f'{next(n["title"] for n in nodes_out if n["id"] == dst)[:46]}')
            shown += 1
            if shown >= report:
                break
        print('\nnodes with no edges at all:')
        for node in nodes_out:
            if not node['cites'] and not node['refs']:
                print(f'  {node["kind"]:10s} doc={int(node["doc"])} '
                      f'{node["id"][:56]}')


if __name__ == '__main__':
    main()
