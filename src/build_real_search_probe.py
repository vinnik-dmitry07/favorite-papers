'''Build a complete-paper canonical subset for an isolated real-search probe.

The generated assets are not a production release. No model is downloaded and
no embeddings or publication markers are fabricated by this builder.
'''

from __future__ import annotations

import argparse
from collections import deque
import hashlib
import json
from pathlib import Path

from build_agent_index import (
    BuildError,
    build_release,
    canonical_json,
    git_sha,
    load_embed,
    read_texts,
    sha256_hex,
    validate_edges,
    vector_id,
)
from common import GRAPH, ROOT

SEED_ID = 'arxiv:2402.03300'
SLOT = 'real-probe'
DEFAULT_OUT = ROOT / 'agent_real_probe'
ORACLE_REVISION = 2
ORACLE_NOTE = {
    'post_observation': True,
    'reason': (
        'After the local v1 run, source review confirmed that chunk 56 '
        'answers the baseline question using the value-function synonym. '
        'Revision 2 corrects that lexical false negative for diagnosis; '
        'it is not a held-out or preregistered retrieval pass. The GRPO '
        'settings oracle and all query strings are unchanged.'
    ),
}


def integration_queries(seed_id: str, paper: dict) -> list[dict]:
    '''Fixed integration prompts, not a held-out retrieval benchmark.'''
    prompts = [
        ('group-baseline',
         'How can policy optimization estimate a reward baseline from groups '
         'of generated answers without training a separate critic?'),
        ('relative-advantage',
         'How are advantages calculated using relative rewards of several '
         'outputs sampled for the same question?'),
        ('kl-placement',
         'Why would a reinforcement learning algorithm add KL divergence '
         'directly to the loss instead of adding a KL penalty to rewards?'),
        ('grpo-settings',
         'What KL coefficient and number of sampled outputs per question '
         'were used in the GRPO training experiment?'),
        ('web-math-data',
         'How was mathematical pretraining data selected from Common Crawl '
         'to improve language model reasoning?'),
        ('online-training',
         'What factors make online reinforcement learning more effective '
         'than offline training for mathematical reasoning?'),
    ]
    queries = [{'id': name, 'query': query, 'expected_paper_id': seed_id}
               for name, query in prompts]
    criteria = {
        'group-baseline': ['baseline'],
        'grpo-settings': ['0.04', '64'],
    }
    for query in queries:
        terms = criteria.get(query['id'])
        if not terms:
            continue
        query['required_passage_terms'] = terms
        if query['id'] == 'group-baseline':
            query['passage_evidence_any'] = [
                ['critic', 'group'],
                ['value function', 'average reward',
                 'multiple sampled outputs'],
            ]
        alternatives = query.get('passage_evidence_any', [[]])
        query['gold_chunk_indices'] = [
            chunk['index'] for chunk in paper['chunks']
            if all(term.casefold() in paper['text'][
                chunk['start']:chunk['end']].casefold() for term in terms)
            and any(all(term.casefold() in paper['text'][
                chunk['start']:chunk['end']].casefold() for term in group)
                for group in alternatives)
        ]
        if not query['gold_chunk_indices']:
            raise BuildError('Fixed passage oracle is absent from seed text')
        if query['id'] == 'grpo-settings':
            quote = 'The KL coefficient is 0.04.'
            if quote not in paper['text']:
                raise BuildError('Fixed answer quote is absent from seed text')
            query['expected_quote'] = quote
    return queries


def spread_indices(count: int, limit: int = 200) -> list[int]:
    if count < 1 or limit < 1:
        raise BuildError('Compatibility selection needs positive bounds')
    size = min(count, limit)
    if size == 1:
        return [0]
    return [index * (count - 1) // (size - 1) for index in range(size)]


def _candidate_order(
    nodes: list[dict], edges: list, seed_id: str,
) -> list[str]:
    resolved = validate_edges(nodes, edges)
    ids = {node['id'] for node in nodes}
    if seed_id not in ids:
        raise BuildError(f'Required seed paper is missing: {seed_id}')
    adjacent = {node_id: set() for node_id in ids}
    for edge in resolved:
        adjacent[edge['source']].add(edge['target'])
        adjacent[edge['target']].add(edge['source'])
    distances = {seed_id: 0}
    queue = deque([seed_id])
    while queue:
        current = queue.popleft()
        for neighbor in sorted(adjacent[current]):
            if neighbor not in distances:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
    return sorted(ids, key=lambda node_id: (
        distances.get(node_id, len(ids) + 1), node_id,
    ))


def subset_graph(nodes: list[dict], edges: list, selected: set[str]):
    '''Retain induced edges and remap their original numeric endpoints.'''
    validate_edges(nodes, edges)
    chosen = sorted((node for node in nodes if node['id'] in selected),
                    key=lambda node: node['id'])
    indices = {node['id']: index for index, node in enumerate(chosen)}
    retained = [
        [indices[nodes[source]['id']], indices[nodes[target]['id']], evidence]
        for source, target, evidence in edges
        if nodes[source]['id'] in selected and nodes[target]['id'] in selected
    ]
    retained.sort(key=lambda edge: (edge[0], edge[1], edge[2]))
    return chosen, retained


def build_subset(
    graph: dict,
    texts: dict[str, str | None],
    embed: dict,
    *,
    seed_id: str = SEED_ID,
    minimum: int = 200,
    target: int = 300,
    maximum: int = 500,
    source_sha: str | None = None,
    source_graph_sha256: str | None = None,
    progress: bool = False,
) -> tuple[dict, dict]:
    '''Select whole papers by graph distance, then use the canonical builder.

    Small custom bounds support local contract fixtures. The CLI always uses
    the real experiment's 200..500-passage bounds.
    '''
    if (any(isinstance(value, bool) or not isinstance(value, int)
            for value in (minimum, target, maximum))
            or not 1 <= minimum <= target <= maximum <= 500):
        raise BuildError('Expected 1 <= minimum <= target <= maximum <= 500')
    if not isinstance(graph, dict):
        raise BuildError('Source graph must be an object')
    nodes, edges = graph.get('nodes'), graph.get('edges')
    if not isinstance(nodes, list) or not isinstance(edges, list):
        raise BuildError('Source graph must contain nodes and edges arrays')
    order = _candidate_order(nodes, edges, seed_id)
    by_id = {node['id']: node for node in nodes}
    selected = set()
    total = 0
    considered = 0
    for node_id in order:
        considered += 1
        markdown = texts.get(node_id)
        if not isinstance(markdown, str):
            if node_id == seed_id:
                raise BuildError('Required seed paper has no Markdown text')
            continue
        one = build_release([by_id[node_id]], [], {node_id: markdown}, embed)
        count = len(one['passages'])
        if not count:
            if node_id == seed_id:
                raise BuildError('Required seed paper has no canonical text')
            continue
        if total + count > maximum:
            if node_id == seed_id:
                raise BuildError('Required seed paper alone exceeds the cap')
            continue
        selected.add(node_id)
        total += count
        if progress:
            print(f'Selected {node_id}: {count} passages ({total} total)',
                  flush=True)
        if total >= target:
            break
    if seed_id not in selected or total < minimum:
        raise BuildError('Complete papers cannot meet the requested bounds')
    chosen, retained = subset_graph(nodes, edges, selected)
    release = build_release(
        chosen, retained, {node_id: texts[node_id] for node_id in selected},
        embed, git_sha_value=source_sha,
    )
    if len(release['passages']) != total:
        raise BuildError('Canonical passage count changed during selection')
    probe = {
        'schema_version': 1,
        'kind': 'real-subset',
        'synthetic': False,
        'dimensions': embed['dimensions'],
        'slot': SLOT,
        'release_id': release['release_id'],
        'embedding_signature': release['embedding_signature'],
        'build_signature': release['build_signature'],
        'reader_schema': embed['reader_schema'],
        'passage_count': total,
        'node_count': len(chosen),
        'edge_count': len(retained),
        'token_count': sum(row['token_count'] for row in release['passages']),
        'paper_ids': sorted(selected),
        'sample_paper_id': seed_id,
        'source_sha': source_sha,
        'source_graph_sha256': (source_graph_sha256
                                or sha256_hex(canonical_json(graph))),
        'selection': {
            'method': 'whole-papers-by-undirected-distance-then-id',
            'minimum_passages': minimum,
            'target_passages': target,
            'maximum_passages': maximum,
            'considered_papers': considered,
        },
        'rows': [{**row, 'id': vector_id(SLOT, row['paper_id'],
                                       row['chunk_index'])}
                 for row in release['passages']],
        'files': {},
        'embeddings': None,
        'compatibility_indices': spread_indices(total),
        'queries': integration_queries(seed_id, release['papers'][seed_id]),
        'oracle_revision': ORACLE_REVISION,
        'oracle_note': dict(ORACLE_NOTE),
        'scope': 'isolated-integration-subset-not-full-corpus',
        'semantic_quality_gate': 'not_tested',
        'publication_ready': False,
    }
    return release, probe


def write_subset(release: dict, probe: dict, output: Path) -> dict:
    '''Write canonical bytes first, then atomically switch the manifest.'''
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    release_id = release['release_id']
    documents = {f'releases/{release_id}/graph.json': release['graph']}
    documents.update({
        f'releases/{release_id}/papers/{sha256_hex(paper_id)}.json': paper
        for paper_id, paper in release['papers'].items()
    })
    files = {}
    for relative, document in sorted(documents.items()):
        encoded = canonical_json(document).encode('utf-8')
        path = output / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(encoded)
        files[relative] = hashlib.sha256(encoded).hexdigest()
    probe = {**probe, 'files': files, 'embeddings': None}
    temporary = output / 'probe.json.tmp'
    temporary.write_text(canonical_json(probe), encoding='utf-8')
    temporary.replace(output / 'probe.json')
    return probe


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=DEFAULT_OUT)
    parser.add_argument('--graph', type=Path, default=GRAPH)
    parser.add_argument('--target', type=int, default=300)
    args = parser.parse_args(argv)
    if not 200 <= args.target <= 500:
        parser.error('target must be between 200 and 500 passages')
    try:
        data = args.graph.read_bytes()
        graph = json.loads(data)
        release, probe = build_subset(
            graph, read_texts(graph['nodes']), load_embed(),
            target=args.target,
            source_sha=git_sha(),
            source_graph_sha256=hashlib.sha256(data).hexdigest(),
            progress=True,
        )
        saved = write_subset(release, probe, args.out)
    except (OSError, ValueError, KeyError, TypeError, BuildError) as exc:
        parser.exit(1, str(exc) + '\n')
    print(json.dumps({
        'output': str(args.out), 'release_id': saved['release_id'],
        'papers': saved['paper_ids'], 'passages': saved['passage_count'],
        'edges': saved['edge_count'], 'embeddings': 'not_generated',
    }), flush=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
