'''Reproduce the external subset review and evaluate the actual probe kernels.

Requires the extracted repro-bench-pq.tar.gz and a current agent_build
manifest.
No models, API credentials, network requests or Cloudflare deployment are used.
'''

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import subprocess
from pathlib import Path

import faiss
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = 200


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def retained(ranking, paper_of, limit):
    seen = set()
    result = []
    for row in ranking:
        paper = paper_of[row]
        if paper not in seen:
            seen.add(paper)
            result.append(row)
            if len(result) == limit:
                break
    return result


def cluster_upper(loss, groups):
    '''Same query-weighted paper-cluster bootstrap as the external script.'''
    unique, inverse = np.unique(groups, return_inverse=True)
    counts = np.bincount(inverse)
    totals = np.bincount(inverse, weights=loss)
    draws = np.random.default_rng(7).choice(
        len(unique), size=(4000, len(unique)), replace=True,
    )
    statistics = totals[draws].sum(axis=1) / counts[draws].sum(axis=1)
    return float(np.quantile(statistics, 0.95))


def evaluate(ranking, reference, targets, paper_of):
    groups = paper_of[targets]
    reference_retained = [retained(row, paper_of, 8) for row in reference]
    selected = [retained(row, paper_of, 8) for row in ranking]
    ref_hit = np.array([
        target in paper_of[rows]
        for target, rows in zip(groups, reference_retained)
    ])
    hit = np.array([
        target in paper_of[rows] for target, rows in zip(groups, selected)
    ])
    loss = ref_hit.astype(float) - hit.astype(float)
    overlap = np.array([
        len(set(exact[:8]) & set(candidate[:8])) / 8
        for exact, candidate in zip(reference, ranking)
    ])
    gold_selected = np.array([
        target in rows for target, rows in zip(targets, selected)
    ])
    ref_gold = np.array([
        target in rows for target, rows in zip(targets, reference_retained)
    ])
    return {
        'gold_passage_recall@50': round(float(np.mean([
            target in row[:50] for target, row in zip(targets, ranking)
        ])), 4),
        'exact_top8_covered_in_top50': round(float(np.mean([
            len(set(exact[:8]) & set(candidate[:50])) / 8
            for exact, candidate in zip(reference, ranking)
        ])), 4),
        'recall@8_vs_exact_mean': round(float(overlap.mean()), 4),
        'share_queries_recall@8_below_0.5': round(
            float((overlap < 0.5).mean()), 4,
        ),
        'paper_hit@8': round(float(hit.mean()), 4),
        'paper_hit@8_loss_pp': round(100 * float(loss.mean()), 2),
        'lost_b': int((ref_hit & ~hit).sum()),
        'gained_c': int((~ref_hit & hit).sum()),
        'loss_upper95_cluster_pp': round(
            100 * cluster_upper(loss, groups), 2,
        ),
        'zero_discordance': bool(np.all(loss == 0)),
        'target_chunk_retained@8': round(float(gold_selected.mean()), 4),
        'target_chunk_retained@8_loss_pp': round(
            100 * float((ref_gold.astype(float)
                         - gold_selected.astype(float)).mean()), 2,
        ),
        'semantic_only_paper_hit@5': round(float(np.mean([
            target in paper_of[rows[:5]]
            for target, rows in zip(groups, selected)
        ])), 4),
        'candidate_count': int(ranking.shape[1]),
    }


def rerank(queries, candidates, vectors):
    return np.stack([
        rows[np.argsort(-(vectors[rows] @ query), kind='stable')]
        for query, rows in zip(queries, candidates)
    ])


def load_inputs(evidence, manifest_path):
    out = evidence / 'pq' / 'out'
    manifest = read_json(manifest_path)
    subset = read_json(out / 'subset.json')
    vectors = np.load(out / 'corpus_vecs.npy', allow_pickle=False)
    assert vectors.dtype == np.float32 and vectors.shape == (12135, 768)
    assert np.isfinite(vectors).all()
    assert np.max(np.abs(np.linalg.norm(vectors, axis=1) - 1)) < 1e-4
    rows = [manifest['passages'][index] for index in subset['indices']]
    assert len(rows) == len(vectors) == subset['n_chunks']
    paper_of = np.array([row['paper_id'] for row in rows])
    assert len(np.unique(paper_of)) == subset['n_papers'] == 103
    papers = {
        paper['paper_id']: paper
        for path in (manifest_path.parent / 'papers').glob('*.json')
        for paper in [read_json(path)]
    }
    sentence = read_json(out / 'sentence_queries_extra.json')['queries']
    natural = read_json(out / 'natural_queries.json')['queries']
    for query in sentence:
        row = rows[query['target_pos']]
        assert (row['paper_id'], row['chunk_index']) == (
            query['paper_id'], query['chunk_index'],
        )
        text = papers[row['paper_id']]['text'][row['start']:row['end']]
        assert query['query'] in text
    datasets = {}
    for name, suffix in (
        ('sentence_2000', 'sentence_extra'), ('natural_53', 'natural'),
    ):
        queries = np.load(out / f'q_{suffix}.npy', allow_pickle=False)
        targets = np.load(out / f't_{suffix}.npy', allow_pickle=False)
        assert queries.dtype == np.float32 and queries.shape[1] == 768
        assert np.isfinite(queries).all() and len(queries) == len(targets)
        assert np.max(np.abs(np.linalg.norm(queries, axis=1) - 1)) < 1e-4
        assert np.issubdtype(targets.dtype, np.integer)
        assert ((targets >= 0) & (targets < len(vectors))).all()
        if name == 'sentence_2000':
            assert len(queries) == 2000
            assert targets.tolist() == [q['target_pos'] for q in sentence]
        else:
            assert len(queries) == 53
            assert targets.tolist() == [q['target_pos'] for q in natural]
        datasets[name] = (queries, targets)
    return vectors, paper_of, datasets, manifest


def kernel_rankings(vectors, queries, pq, work):
    work.mkdir(parents=True, exist_ok=True)
    count, dimensions = vectors.shape
    config = {
        'format': 'pq-ip-v1', 'dimensions': dimensions,
        'subquantizers': 96, 'centroids': 256, 'count': count,
    }
    (work / 'config.json').write_text(json.dumps(config), encoding='utf-8')
    pq.sa_encode(vectors).tofile(work / 'codes.bin')
    faiss.vector_to_array(pq.pq.centroids).astype('<f4').tofile(
        work / 'codebooks.bin',
    )
    # Match build_static_search_probe.py: symmetric per-row rounding and
    # cosine scoring, with raw signs taken after quantization.
    values = vectors.astype(np.float64)
    scale = 127 / np.max(np.abs(values), axis=1, keepdims=True)
    integers = np.rint(values * scale).astype(np.int8)
    integers.tofile(work / 'int8.bin')
    norms = 1 / np.linalg.norm(integers.astype(np.float64), axis=1)
    norms.astype('<f8').tofile(work / 'norms.bin')
    np.packbits(integers >= 0, axis=1, bitorder='little').tofile(
        work / 'bits.bin',
    )
    queries.astype('<f4').tofile(work / 'queries.bin')
    worker = ROOT / 'worker'
    subprocess.run(['npm', 'run', 'build:probe'], cwd=worker, check=True)
    executable = worker / 'node_modules' / '.bin' / 'esbuild'
    bundle = work / 'review-quality.mjs'
    subprocess.run([
        str(executable), str(worker / 'probe-kernel' / 'review-quality.ts'),
        '--bundle', '--platform=node', '--format=esm', f'--outfile={bundle}',
    ], check=True)
    subprocess.run([
        'node', str(bundle), str(work),
        str(worker / 'probe-kernel' / 'scan.wasm'),
    ], check=True)
    return read_json(work / 'kernel-rankings.json')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--evidence', type=Path, required=True)
    parser.add_argument('--manifest', type=Path,
                        default=ROOT / 'agent_build' / 'manifest.json')
    parser.add_argument('--work-dir', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    faiss.omp_set_num_threads(1)
    vectors, paper_of, datasets, manifest = load_inputs(
        args.evidence, args.manifest,
    )
    queries = np.concatenate([query for query, _ in datasets.values()])
    print('Validated 12,135 vectors and 2,000 target texts; training PQ96.',
          flush=True)
    flat = faiss.IndexFlatIP(vectors.shape[1])
    flat.add(vectors)
    reference = flat.search(queries, CANDIDATES)[1]
    sq8 = faiss.IndexScalarQuantizer(
        vectors.shape[1], faiss.ScalarQuantizer.QT_8bit,
        faiss.METRIC_INNER_PRODUCT,
    )
    sq8.train(vectors)
    sq8.add(vectors)
    decoded = sq8.sa_decode(sq8.sa_encode(vectors))
    pq = faiss.IndexPQ(vectors.shape[1], 96, 8, faiss.METRIC_INNER_PRODUCT)
    pq.train(vectors)
    pq.add(vectors)
    pq_rows = pq.search(queries, CANDIDATES)[1]
    ranks = {
        'exact_fp32': reference,
        'sq8_flat': sq8.search(queries, CANDIDATES)[1],
        'pq96': pq_rows,
        'pq96_top100_sq8': rerank(
            queries, pq.search(queries, 100)[1], decoded,
        ),
        'pq96_top200_sq8': rerank(queries, pq_rows, decoded),
    }
    mean = vectors.mean(axis=0, keepdims=True)
    bits = np.packbits(vectors - mean > 0, axis=1)
    query_bits = np.packbits(queries - mean > 0, axis=1)
    candidates = np.stack([
        np.argsort(np.unpackbits(bits ^ query, axis=1).sum(axis=1),
                   kind='stable')[:CANDIDATES]
        for query in query_bits
    ])
    ranks['binary_top200_sq8'] = rerank(queries, candidates, decoded)
    print('Reference variants complete; running actual JS/WASM kernels.',
          flush=True)
    kernels = kernel_rankings(
        vectors, queries, pq, args.work_dir.resolve(),
    )
    ranks.update({
        name: np.asarray(rows, dtype=np.int64)
        for name, rows in kernels.pop('rankings').items()
    })
    assert np.array_equal(ranks['probe_pq_js'], ranks['probe_pq_js4'])
    assert np.array_equal(ranks['probe_pq_js'], ranks['probe_pq_wasm'])
    report = {
        'schema_version': 1,
        'scope': 'External 103-paper subset; exploratory, not a release gate.',
        'versions': {
            'python': platform.python_version(), 'numpy': np.__version__,
            'faiss': faiss.__version__,
        },
        'corpus': {
            'release_id': manifest['release_id'],
            'manifest_sha256': sha256(args.manifest),
            'full_passages': len(manifest['passages']),
            'subset_passages': len(vectors), 'subset_papers': 103,
            'sentence_target_texts_checked': 2000,
        },
        'input_sha256': {
            str(path.relative_to(args.evidence)): sha256(path)
            for path in sorted((args.evidence / 'pq' / 'out').iterdir())
            if path.name in {
                'corpus_vecs.npy', 'subset.json', 'q_sentence_extra.npy',
                't_sentence_extra.npy', 'q_natural.npy', 't_natural.npy',
                'sentence_queries_extra.json', 'natural_queries.json',
                'pr2_criteria.json',
            }
        },
        'source_sha256': {
            str(path.relative_to(ROOT)): sha256(path)
            for path in [
                Path(__file__), ROOT / 'src/build_agent_index.py',
                ROOT / 'worker/probe-kernel/review-quality.ts',
                ROOT / 'worker/probe-kernel/scan.wat',
                ROOT / 'worker/src/static-search.ts',
                ROOT / 'worker/src/static-search-wasm.ts',
                ROOT / 'worker/src/static-search-int8.ts',
                ROOT / 'requirements-probe-quality.txt',
                ROOT / 'worker/package-lock.json',
            ]
        },
        'pq_js_js4_wasm_top200_identical': True,
        'local_kernel_timing': kernels,
        'datasets': {},
        'external_report_differences': [],
        'limitations': [
            'Embeddings were supplied, not regenerated or matched to '
            'Workers AI.',
            'Sentence queries quote indexed passages; natural questions were '
            'written while reading the target chunks. Neither is a final '
            'holdout.',
            'All quantizers are trained on the supplied subset.',
            'External SQ8 uses per-dimension min/max and inner products; the '
            'probe uses per-row symmetric int8 and cosine normalization.',
            'External binary codes subtract the corpus mean; the probe '
            'takes uncentered signs after int8 quantization.',
            'Target-chunk retention is a strict proxy, not a judgment of '
            'every relevant passage; overlapping alternatives can also '
            'answer a query.',
            'Semantic-only Hit@5 excludes MCP catalog routing and '
            'metadata hits.',
            'Zero discordance makes the ordinary bootstrap degenerate; its '
            'zero upper bound is not a population guarantee.',
            'Node kernel wall time is not full-request or Cloudflare '
            'CPU time.',
        ],
    }
    published = read_json(args.evidence / 'pq/out/pr2_criteria.json')
    start = 0
    for name, (query, targets) in datasets.items():
        end = start + len(query)
        result = {
            'n': len(query),
            'target_papers': len(np.unique(paper_of[targets])),
            'variants': {},
        }
        for variant, ranking in ranks.items():
            metrics = evaluate(
                ranking[start:end], reference[start:end], targets, paper_of,
            )
            result['variants'][variant] = metrics
            for key, expected in published[name].get(variant, {}).items():
                if metrics[key] != expected:
                    report['external_report_differences'].append({
                        'dataset': name, 'variant': variant, 'metric': key,
                        'published': expected, 'reproduced': metrics[key],
                    })
        report['datasets'][name] = result
        start = end
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(report, indent=2) + '\n', encoding='utf-8',
    )
    print(f'Wrote {args.output}', flush=True)


if __name__ == '__main__':
    main()
