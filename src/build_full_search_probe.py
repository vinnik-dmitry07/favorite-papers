'''Build a canonical full-corpus artifact for isolated local evaluation.

This builder reuses the production cleaner, chunker and model-input hashes.
It does not download models, encode vectors, call Cloudflare or publish a
release. Metadata remains separate from the future binary vector stream.
'''

from __future__ import annotations

import argparse
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
    vector_id,
)
from common import GRAPH, ROOT

DEFAULT_OUT = ROOT / 'agent_full_probe'
SLOT = 'full-probe'
SCOPE = 'isolated-full-corpus-evaluation-not-production'


def build_full_corpus(
    graph: dict,
    texts: dict[str, str | None],
    embed: dict,
    *,
    source_path: str = 'assets/graph.json',
    source_sha: str | None = None,
    source_graph_sha256: str | None = None,
    progress: bool = False,
) -> tuple[dict, dict]:
    '''Include every catalog card and every available canonical passage.'''
    if not isinstance(graph, dict):
        raise BuildError('Source graph must be an object')
    if embed.get('dimensions') != 768:
        raise BuildError('The full-corpus probe requires 768 dimensions')
    release = build_release(
        graph.get('nodes'), graph.get('edges'), texts, embed,
        git_sha_value=source_sha, progress=progress,
    )
    if not release['passages']:
        raise BuildError('Full corpus contains no canonical passages')
    paper_ids = sorted(release['graph']['nodes'])
    text_paper_ids = sorted(release['papers'])
    unavailable = []
    for paper_id in paper_ids:
        card = release['graph']['nodes'][paper_id]
        if paper_id not in release['papers']:
            if (card['text']['available'] is not False
                    or card['text']['reason'] not in (
                        'no_markdown', 'empty_cleaned')):
                raise BuildError('Unavailable paper lacks an explicit reason')
            unavailable.append({
                'paper_id': paper_id, 'reason': card['text']['reason'],
            })
    rows = [
        {**row, 'id': vector_id(SLOT, row['paper_id'], row['chunk_index'])}
        for row in release['passages']
    ]
    if len({row['id'] for row in rows}) != len(rows):
        raise BuildError('Full-corpus vector ID collision')
    text_hashes = {
        paper_id: (sha256_hex(texts[paper_id])
                   if texts.get(paper_id) is not None else None)
        for paper_id in paper_ids
    }
    public_embed = {key: value for key, value in embed.items()
                    if not key.startswith('_')}
    probe = {
        'schema_version': 1,
        'kind': 'full-corpus',
        'synthetic': False,
        'dimensions': embed['dimensions'],
        'slot': SLOT,
        'scope': SCOPE,
        'release_id': release['release_id'],
        'embedding_signature': release['embedding_signature'],
        'build_signature': release['build_signature'],
        'reader_schema': embed['reader_schema'],
        'source_path': source_path,
        'source_sha': source_sha,
        'source_graph_sha256': (source_graph_sha256
                                or sha256_hex(canonical_json(graph))),
        'source_embed_sha256': sha256_hex(canonical_json(public_embed)),
        'source_text_hashes': text_hashes,
        'source_texts_sha256': sha256_hex(canonical_json(text_hashes)),
        'canonical_manifest_sha256': sha256_hex(
            canonical_json(release['manifest'])),
        'node_count': len(paper_ids),
        'edge_count': release['manifest']['edge_count'],
        'papers_with_text': len(text_paper_ids),
        'papers_without_text': len(unavailable),
        'passage_count': len(rows),
        'token_count': sum(row['token_count'] for row in rows),
        'code_points': sum(len(paper['text'])
                           for paper in release['papers'].values()),
        'paper_ids': paper_ids,
        'text_paper_ids': text_paper_ids,
        'unavailable_text': unavailable,
        'row_order': 'paper_id-lexicographic-then-chunk_index',
        'rows_sha256': sha256_hex(canonical_json(rows)),
        'rows': rows,
        'vector_layout': {
            'dtype': 'float32', 'byte_order': 'little',
            'order': 'row-major', 'dimensions': embed['dimensions'],
            'row_bytes': embed['dimensions'] * 4,
            'expected_bytes': len(rows) * embed['dimensions'] * 4,
        },
        'files': {},
        'embeddings': None,
        'semantic_quality_gate': 'unverified',
        'workers_ai_compatibility': 'unverified',
        'publication_ready': False,
    }
    return release, probe


def write_full_corpus(release: dict, probe: dict, output: Path) -> dict:
    '''Write each canonical paper independently, then switch the manifest.'''
    output = Path(output)
    manifest_path = output / 'probe.json'
    if manifest_path.exists():
        previous = json.loads(manifest_path.read_text(encoding='utf-8'))
        if previous.get('kind') != 'full-corpus':
            raise BuildError('Refusing to replace a different probe kind')
    output.mkdir(parents=True, exist_ok=True)
    prefix = f'releases/{release["release_id"]}'
    files = {}

    def write_document(relative: str, document: dict) -> None:
        encoded = canonical_json(document).encode('utf-8')
        path = output / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary = path.with_suffix(path.suffix + '.tmp')
        temporary.write_bytes(encoded)
        temporary.replace(path)
        files[relative] = hashlib.sha256(encoded).hexdigest()

    write_document(prefix + '/graph.json', release['graph'])
    write_document(prefix + '/manifest.json', release['manifest'])
    for paper_id in sorted(release['papers']):
        write_document(
            prefix + '/papers/' + sha256_hex(paper_id) + '.json',
            release['papers'][paper_id],
        )
    saved = {**probe, 'files': files, 'embeddings': None}
    temporary = output / 'probe.json.tmp'
    temporary.write_text(canonical_json(saved), encoding='utf-8')
    temporary.replace(manifest_path)
    return saved


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=DEFAULT_OUT)
    parser.add_argument('--graph', type=Path, default=GRAPH)
    args = parser.parse_args(argv)
    if args.out.resolve() == (ROOT / 'agent_real_probe').resolve():
        parser.error('Use a separate output from the real-subset probe')
    try:
        raw = args.graph.read_bytes()
        graph = json.loads(raw)
        path = args.graph.resolve()
        source_path = str(path.relative_to(ROOT)) if path.is_relative_to(
            ROOT) else str(path)
        release, probe = build_full_corpus(
            graph, read_texts(graph['nodes']), load_embed(),
            source_path=source_path, source_sha=git_sha(),
            source_graph_sha256=hashlib.sha256(raw).hexdigest(),
            progress=True,
        )
        saved = write_full_corpus(release, probe, args.out)
    except (OSError, ValueError, KeyError, TypeError, BuildError) as exc:
        parser.exit(1, str(exc) + '\n')
    print(json.dumps({
        'output': str(args.out), 'release_id': saved['release_id'],
        'catalog_papers': saved['node_count'],
        'papers_with_text': saved['papers_with_text'],
        'papers_without_text': saved['papers_without_text'],
        'passages': saved['passage_count'], 'edges': saved['edge_count'],
        'token_count': saved['token_count'],
        'vectors_expected_bytes': saved['vector_layout']['expected_bytes'],
        'embeddings': 'not_generated',
    }), flush=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
