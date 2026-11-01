'''Describe saved full-corpus vectors without issuing an admission certificate.

This replay authenticates one historical artifact and uses the existing
metric functions. It does not encode inputs, call a provider, or authorize a
publication. The original preflight/quality entrypoints remain unchanged.
'''

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import platform
import time
import zipfile

import numpy as np

import evaluate_full_search_probe as metrics
from build_agent_index import canonical_json, load_embed
from embed_real_search_probe import atomic_bytes, checked_path

ARTIFACT_ID = 12715563729
ARTIFACT_SHA256 = (
    '8f3fd29b369ae41f1474e052e0eef931a23ca7437c99640adbc6bc13d519c65c'
)
RUN_ID = 40448979121
SOURCE_COMMIT = 'fa3f4ec3724949a98b2b510949cf8efe405baf8a'
ROOT = Path(__file__).resolve().parents[1]


def authenticated_inputs(archive, corpus, queries_path, query_vectors):
    '''Bind replay inputs to original ZIP bytes, not a copied certificate.'''
    metrics.require(
        metrics.digest(Path(archive).read_bytes()) == ARTIFACT_SHA256,
        'Historical archive checksum mismatch',
    )
    pairs = [
        (Path(corpus) / 'probe.json', 'agent_full_probe/probe.json'),
        (Path(queries_path), 'agent_full_probe/quality-combined-frozen.json'),
        (Path(query_vectors), 'full-probe-reports/query-vectors.f32'),
        (Path(str(query_vectors) + '.json'),
         'full-probe-reports/query-vectors.f32.json'),
    ]
    with zipfile.ZipFile(archive) as saved:
        for local, name in pairs:
            metrics.require(
                metrics.digest(local.read_bytes())
                == metrics.digest(saved.read(name)),
                'Replay input differs from historical artifact: ' + name,
            )
        manifest = metrics.json_file(Path(corpus) / 'probe.json')
        vectors = checked_path(Path(corpus), manifest['embeddings']['path'])
        metrics.require(
            metrics.digest(vectors.read_bytes())
            == metrics.digest(saved.read('agent_full_probe/vectors.f32')),
            'Corpus vectors differ from historical artifact',
        )
        snapshot = json.loads(saved.read(
            'full-probe-reports/preflight/snapshot.json'
        ))
        packed_hash = metrics.digest(
            saved.read('agent_full_runtime/probe.json')
        )
    binding = {**snapshot['binding'],
               'historical_packed_manifest_sha256': packed_hash}
    metrics.require(binding['head'] == SOURCE_COMMIT,
                    'Historical artifact source differs')
    sources = binding['code_sha256']
    for relative in ('src/evaluate_full_search_probe.py',
                     'src/build_agent_index.py',
                     'src/embed_real_search_probe.py'):
        metrics.require(
            metrics.digest((ROOT / relative).read_bytes())
            == sources[relative],
            'Historical metric/input implementation changed: ' + relative,
        )
    return binding


def validated_rankings(runtime, manifest, query_meta, query_hash, binding):
    '''Reject mismatched, fractional, duplicate or incomplete ranking rows.'''
    count, passages = query_meta['count'], len(manifest['rows'])
    metrics.require(
        runtime.get('engine') == 'full-int8-runtime'
        and runtime.get('kind') == 'historical-artifact-offline-rankings'
        and runtime.get('artifact_sha256') == ARTIFACT_SHA256
        and runtime.get('run_id') == RUN_ID
        and runtime.get('query_count') == count
        and runtime.get('passage_count') == passages
        and runtime.get('query_vectors_sha256') == query_meta['vectors_sha256']
        and runtime.get('query_manifest_sha256') == query_hash
        and runtime.get('source_rows_sha256') == manifest['rows_sha256']
        and runtime.get('packed_manifest_sha256')
        == binding['historical_packed_manifest_sha256'],
        'Historical runtime ranking provenance mismatch',
    )
    sources = runtime.get('implementation', {}).get('source_sha256', {})
    for relative in ('worker/src/full-search-index.ts',
                     'worker/src/static-search-int8.ts',
                     'worker/probe-kernel/scan.wat'):
        metrics.require(
            sources.get(relative) == binding['code_sha256'][relative],
            'Historical runtime implementation changed: ' + relative,
        )
    metrics.require(
        runtime.get('implementation', {}).get('wasm_sha256',
                                             runtime.get('wasm_sha256'))
        == binding['code_sha256']['worker/probe-kernel/scan.wasm'],
        'Historical WASM implementation changed',
    )
    expected_crosschecks = [
        index * (count - 1) // 63 for index in range(64)
    ]
    metrics.require(
        runtime.get('js_wasm_checked_queries') == expected_crosschecks
        and runtime.get('js_wasm_max_score_difference') == 0,
        'Historical JS/WASM crosschecks are incomplete or disagree',
    )
    rows = runtime.get('rankings')
    metrics.require(
        isinstance(rows, list) and len(rows) == count
        and all(isinstance(row, list) and len(row) == metrics.TOP_CANDIDATES
                and all(type(value) is int and 0 <= value < passages
                        for value in row)
                and len(set(row)) == metrics.TOP_CANDIDATES for row in rows),
        'Invalid actual runtime ranking geometry',
    )
    return np.asarray(rows, dtype=np.int64)


def summarize(archive, corpus_path, queries_path, query_vectors,
              runtime_rankings, output, *, batch_size=32):
    metrics.require(1 <= batch_size <= 64,
                    'Batch size must be between 1 and 64')
    started = time.monotonic()
    binding = authenticated_inputs(
        archive, corpus_path, queries_path, query_vectors
    )
    manifest, papers, _, identity = metrics.corpus_inputs(corpus_path)
    document = metrics.json_file(queries_path)
    query_meta = metrics.json_file(str(query_vectors) + '.json')
    questions, rows = document['queries'], manifest['rows']
    metrics.require(
        len(rows) == 40575 and len(questions) == 2064
        and Counter(row['cohort'] for row in questions)
        == {'extractive_fidelity': 2000, 'natural_development': 64}
        and len({row['id'] for row in questions}) == len(questions)
        and document['corpus_identity'] == identity,
        'Frozen historical cohort or corpus identity differs',
    )
    query_hash = metrics.digest(Path(queries_path).read_bytes())
    metrics.require(
        query_meta['query_manifest_sha256'] == query_hash
        and query_meta['vectors_sha256']
        == metrics.digest(Path(query_vectors).read_bytes()),
        'Query vector checksum or question identity mismatch',
    )
    for question in questions:
        metrics.validate_question(question, papers)
    vectors_info = manifest['embeddings']
    metrics.require(
        query_meta.get('encoder_signature')
        == vectors_info.get('encoder_signature')
        == metrics.digest(canonical_json(query_meta['encoder']).encode())
        and query_meta['query_template'] == load_embed()['query_template'],
        'Corpus/query encoder or query template differs',
    )
    corpus_vectors = checked_path(Path(corpus_path), vectors_info['path'])
    metrics.require(
        metrics.digest(corpus_vectors.read_bytes()) == vectors_info['sha256'],
        'Corpus vector checksum mismatch',
    )
    corpus = metrics.unit_matrix(corpus_vectors, len(rows)).astype(np.float64)
    queries = metrics.unit_matrix(query_vectors, len(questions)).astype(
        np.float64
    )
    queries /= np.linalg.norm(queries, axis=1, keepdims=True)
    runtime = metrics.json_file(runtime_rankings)
    manifest_hash = metrics.digest(
        (Path(corpus_path) / 'probe.json').read_bytes()
    )
    metrics.require(runtime.get('manifest_sha256') == manifest_hash,
                    'Runtime used a different corpus manifest')
    candidate = validated_rankings(runtime, manifest, query_meta, query_hash,
                                   binding)
    ids = [row['id'] for row in rows]
    reference = []
    for first in range(0, len(queries), batch_size):
        reference.extend(metrics.rank_scores(
            queries[first:first + batch_size] @ corpus.T, ids
        ))
        if first % (batch_size * 8) == 0:
            print('FP32 reference queries:', min(first + batch_size,
                                                 len(queries)), flush=True)
    details = []
    for question, ref, cand in zip(questions, reference, candidate):
        entry = {
            'query_id': question['id'], 'cohort': question['cohort'],
            'paper_id': question['expected_paper_id'],
            'overlap_at8': len(set(ref[:8]) & set(cand[:8])) / 8,
            'reference8_contained_candidate50':
                len(set(ref[:8]) & set(cand[:50])) / 8,
            'reference_top50': ref.tolist(), 'candidate_top50': cand.tolist(),
            'source_chunk_at50': {
                name: any(rows[int(pos)]['paper_id']
                          == question['expected_paper_id']
                          and rows[int(pos)]['chunk_index']
                          in question['gold_chunk_indices']
                          for pos in rank[:50])
                for name, rank in [('fp32', ref), ('int8', cand)]
            },
        }
        for protocol, limit_candidates, limit in [
                ('rest', 40, 8), ('mcp_semantic', 25, 5)]:
            entry[protocol] = {
                name: metrics.outcomes(
                    rank, question, rows, papers, candidates=limit_candidates,
                    limit=limit,
                    protocol='rest' if protocol == 'rest' else 'mcp'
                ) for name, rank in [('fp32', ref), ('int8', cand)]
            }
        details.append(entry)
    cohorts = {}
    for cohort in sorted({item['cohort'] for item in details}):
        selected = [item for item in details if item['cohort'] == cohort]
        groups = [item['paper_id'] for item in selected]
        overlap = np.array([item['overlap_at8'] for item in selected])
        result = {
            'n': len(selected), 'papers': len(set(groups)),
            'overlap_at8': float(overlap.mean()),
            'share_overlap_below_half': float(np.mean(overlap < 0.5)),
            'reference8_contained_candidate50': float(np.mean([
                item['reference8_contained_candidate50'] for item in selected
            ])),
            'source_chunk_at50': metrics.paired_summary(
                [item['source_chunk_at50']['fp32'] for item in selected],
                [item['source_chunk_at50']['int8'] for item in selected],
                groups
            ),
        }
        for protocol in ('rest', 'mcp_semantic'):
            result[protocol] = {
                metric: metrics.paired_summary(
                    [item[protocol]['fp32'][metric] for item in selected],
                    [item[protocol]['int8'][metric] for item in selected],
                    groups
                ) for metric in ('paper', 'source_chunk', 'answer_passage',
                                 'answer_window')
            }
        cohorts[cohort] = result
    detail_path = Path(output).with_suffix('.queries.jsonl')
    atomic_bytes(detail_path, ''.join(canonical_json(row) + '\n'
                                     for row in details).encode())
    fidelity = cohorts['extractive_fidelity']
    report = {
        'schema_version': 1,
        'kind': 'historical-artifact-offline-quality-replay',
        'run_id': RUN_ID, 'source_commit': SOURCE_COMMIT,
        'artifact_id': ARTIFACT_ID, 'artifact_sha256': ARTIFACT_SHA256,
        'corpus_identity': identity, 'release_id': manifest['release_id'],
        'passage_count': len(rows), 'paper_count': len(papers),
        'query_count': len(questions), 'manifest_sha256': manifest_hash,
        'query_manifest_sha256': query_hash,
        'query_vectors_sha256': query_meta['vectors_sha256'],
        'corpus_vectors_sha256': vectors_info['sha256'],
        'runtime_rankings_sha256': metrics.digest(
            Path(runtime_rankings).read_bytes()
        ),
        'details_path': str(detail_path),
        'details_sha256': metrics.digest(detail_path.read_bytes()),
        'versions': {'python': platform.python_version(),
                     'numpy': np.__version__},
        'metric_source_sha256': metrics.digest(
            Path(metrics.__file__).read_bytes()
        ),
        'replay_source_sha256': metrics.digest(Path(__file__).read_bytes()),
        'reference': 'Canonical FP32 corpus, normalized FP32 query inputs, '
                     'float64 BLAS accumulation',
        'candidate': runtime.get('implementation'), 'cohorts': cohorts,
        'extractive_fidelity_diagnostic': (
            'passed' if fidelity['reference8_contained_candidate50'] >= 0.95
            else 'failed'
        ),
        'admission_certificate': 'not-issued',
        'heldout_quality_gate': 'unverified',
        'answer_utility_gate': 'unverified',
        'production_readiness': 'unverified',
        'platform_cpu_gate': 'unverified',
        'platform_memory_gate': 'unverified', 'provider_calls': 0,
        'model_loaded': False,
        'limitations': document['limitations'] + [
            'Historical saved-vector diagnostic, not a fresh intended-path '
            'admission.',
            'The original expired or environment-bound certificate is not '
            'reissued.',
            'MCP semantic projection uses top25->5, excluding catalog '
            'routing/metadata.',
            'Actual runtime rankings are local; wall time is not '
            'Cloudflare CPU.',
            'No query, answer span, or threshold is revised after '
            'observing results.',
        ],
        'elapsed_seconds': time.monotonic() - started,
    }
    metrics.write_json(output, report)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('archive', 'corpus', 'queries', 'query-vectors',
                 'runtime-rankings', 'output'):
        parser.add_argument('--' + name, required=True, type=Path)
    parser.add_argument('--batch-size', type=int, default=32)
    args = parser.parse_args()
    report = summarize(args.archive, args.corpus, args.queries,
                       args.query_vectors, args.runtime_rankings, args.output,
                       batch_size=args.batch_size)
    print(canonical_json({'output': str(args.output),
                          'cohorts': report['cohorts'],
                          'extractive_fidelity_diagnostic':
                              report['extractive_fidelity_diagnostic']}))


if __name__ == '__main__':
    main()
