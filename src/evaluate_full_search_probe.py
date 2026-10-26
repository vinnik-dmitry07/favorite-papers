'''Freeze and evaluate offline full-corpus retrieval diagnostics.

Extracted sentences test quantization fidelity, not representative user quality.
Natural questions are frozen source-grounded development cases. Neither cohort
can establish a held-out release-quality or production-readiness pass.
'''

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import re
import time
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

from build_agent_index import (
    BuildError,
    WordPieceTokenizer,
    canonical_json,
    embedding_signature,
    load_embed,
    model_input,
    vector_id,
)
from embed_real_search_probe import (
    BgeEncoder,
    atomic_bytes,
    cache_context,
    checked_asset,
    checked_path,
    execution_profile,
    recover_cached_vector,
    vector_bytes,
    write_cached_vector,
)

SEED = 'full-fidelity-source-sentences-v1'
MAX_PER_PAPER = 8
QUERY_COUNT = 2000
TOP_CANDIDATES = 50


def digest(data):
    return hashlib.sha256(data).hexdigest()


def json_file(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def require(condition, message):
    if not condition:
        raise BuildError(message)


def write_json(path, value, *, immutable=False):
    data = (canonical_json(value) + '\n').encode()
    path = Path(path)
    if immutable and path.exists():
        require(
            path.read_bytes() == data, 'Refusing to overwrite frozen inputs'
        )
        return
    atomic_bytes(path, data)


def corpus_inputs(root):
    root = Path(root)
    manifest = json_file(root / 'probe.json')
    require(
        manifest.get('kind') == 'full-corpus'
        and manifest.get('synthetic') is False
        and manifest.get('publication_ready') is False,
        'Expected an isolated real full-corpus manifest',
    )
    rows = manifest['rows']
    require(
        len(rows) == manifest['passage_count'] and len(rows) >= 2000,
        'Full-corpus row count is inconsistent',
    )
    require(
        len({row['id'] for row in rows}) == len(rows),
        'Duplicate passage identity',
    )
    prefix = f'releases/{manifest["release_id"]}'
    graph = json.loads(checked_asset(root, manifest, prefix + '/graph.json'))
    papers = {}
    source_assets = {
        prefix + '/graph.json': manifest['files'][prefix + '/graph.json']
    }
    for paper_id in sorted({row['paper_id'] for row in rows}):
        name = prefix + '/papers/' + digest(paper_id.encode()) + '.json'
        paper = json.loads(checked_asset(root, manifest, name))
        require(paper['paper_id'] == paper_id, 'Canonical paper mismatch')
        papers[paper_id] = paper
        source_assets[name] = manifest['files'][name]
    for row in rows:
        paper = papers[row['paper_id']]
        chunk = paper['chunks'][row['chunk_index']]
        require(
            all(
                row[key] == chunk[key]
                for key in (
                    'start',
                    'end',
                    'content_hash',
                    'input_hash',
                    'token_count',
                )
            ),
            'Canonical row differs from its source chunk',
        )
        require(
            digest(paper['text'][row['start'] : row['end']].encode())
            == row['content_hash'],
            'Canonical passage hash mismatch',
        )
    # Vector attachments may be added after queries are frozen. This identity
    # binds the immutable corpus/text mapping independently of those attachments.
    identity = digest(
        canonical_json(
            {
                'release_id': manifest['release_id'],
                'embedding_signature': manifest['embedding_signature'],
                'rows': rows,
                'source_assets': source_assets,
            }
        ).encode()
    )
    return manifest, papers, graph, identity


def containing_chunk_indices(paper, spans):
    '''Return every canonical chunk containing all exact source spans.'''
    return [
        chunk['index']
        for chunk in paper['chunks']
        if all(
            chunk['start'] <= span['start'] < span['end'] <= chunk['end']
            for span in spans
        )
    ]


def sentence_candidates(paper, rows, title):
    '''Extract exact source spans; never paraphrase or infer answer labels.'''
    candidates = {}
    text = paper['text']
    for row in rows:
        piece = text[row['start'] : row['end']]
        for match in re.finditer(r'[^.!?\n]{80,900}[.!?](?=\s|$)', piece):
            raw = match.group()
            sentence = raw.strip()
            words = re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", sentence)
            if not 18 <= len(words) <= 100:
                continue
            if any(char in sentence for char in ('\\', '$', '|', '<', '>')):
                continue
            if sum(char.isalpha() for char in sentence) / len(sentence) < 0.65:
                continue
            if (
                title
                and len(title) > 20
                and title.casefold() in sentence.casefold()
            ):
                continue
            start = row['start'] + match.start() + len(raw) - len(raw.lstrip())
            end = start + len(sentence)
            normalized = ' '.join(words).casefold()
            key = digest(normalized.encode())
            item = {
                'id': 'sentence-' + key[:24],
                'query': sentence,
                'cohort': 'extractive_fidelity',
                'expected_paper_id': row['paper_id'],
                'source_chunk_index': row['chunk_index'],
                'gold_chunk_indices': [row['chunk_index']],
                'answer_span_policy': 'all',
                'answer_spans': [
                    {'start': start, 'end': end, 'quote': sentence}
                ],
                'normalized_sha256': key,
            }
            # Keep the original extraction chunk for deterministic selection.
            # Gold coverage is derived below from exact source coordinates,
            # including neighbors whose regex did not extract this sentence.
            candidates.setdefault((start, end, key), item)
    for item in candidates.values():
        item['gold_chunk_indices'] = containing_chunk_indices(
            paper, item['answer_spans']
        )
    return sorted(
        candidates.values(),
        key=lambda item: digest(
            (SEED + '\n' + paper['paper_id'] + '\n' + item['id']).encode()
        ),
    )


def select_sentences(papers, rows, graph, count=QUERY_COUNT):
    by_paper = defaultdict(list)
    for row in rows:
        by_paper[row['paper_id']].append(row)
    pools = {}
    for paper_id, paper in papers.items():
        pools[paper_id] = sentence_candidates(
            paper, by_paper[paper_id], graph['nodes'][paper_id]['title']
        )
    order = sorted(pools, key=lambda key: digest((SEED + key).encode()))
    selected, seen, spans, chunks = (
        [],
        set(),
        defaultdict(list),
        defaultdict(set),
    )
    for _ in range(MAX_PER_PAPER):
        for paper_id in order:
            while pools[paper_id]:
                item = pools[paper_id].pop(0)
                span = item['answer_spans'][0]
                if item['normalized_sha256'] in seen:
                    continue
                if item['source_chunk_index'] in chunks[paper_id]:
                    continue
                if any(
                    span['start'] < end and start < span['end']
                    for start, end in spans[paper_id]
                ):
                    continue
                selected.append(item)
                seen.add(item['normalized_sha256'])
                chunks[paper_id].add(item['source_chunk_index'])
                spans[paper_id].append((span['start'], span['end']))
                break
            if len(selected) == count:
                return selected
    raise BuildError(
        f'Only {len(selected)} eligible sentences; frozen filters '
        'must not be relaxed after candidate results'
    )


def validate_question(item, papers):
    require(
        isinstance(item.get('id'), str)
        and item['id']
        and isinstance(item.get('query'), str)
        and 0 < len(item['query']) <= 2000,
        'Invalid frozen question',
    )
    paper_id = item.get('expected_paper_id')
    require(paper_id in papers, 'Question targets an unavailable paper')
    require(
        item.get('answer_span_policy', 'all') == 'all',
        'Only all-required answer spans are supported',
    )
    spans = item.get('answer_spans')
    require(
        isinstance(spans, list) and spans, 'Question has no answer evidence'
    )
    text = papers[paper_id]['text']
    for span in spans:
        start, end = span.get('start'), span.get('end')
        require(
            type(start) is int
            and type(end) is int
            and 0 <= start < end <= len(text)
            and text[start:end] == span.get('quote'),
            'Question answer differs from the canonical source',
        )
    gold = item.get('gold_chunk_indices')
    require(isinstance(gold, list) and gold, 'Missing source chunk annotation')
    for index in gold:
        require(
            type(index) is int
            and 0 <= index < len(papers[paper_id]['chunks']),
            'Invalid source chunk annotation',
        )
        chunk = papers[paper_id]['chunks'][index]
        require(
            all(
                chunk['start'] <= span['start'] < span['end'] <= chunk['end']
                for span in spans
            ),
            'Gold chunk does not contain all evidence',
        )


def prepare(root, output, natural=None):
    manifest, papers, graph, identity = corpus_inputs(root)
    queries = select_sentences(papers, manifest['rows'], graph)
    natural_provenance = None
    if natural:
        raw = Path(natural).read_bytes()
        document = json.loads(raw)
        questions = document['questions']
        require(
            len(questions) >= 60,
            'Expected at least 60 frozen natural questions',
        )
        queries += [
            {**item, 'cohort': 'natural_development'} for item in questions
        ]
        natural_provenance = {
            'path': str(natural),
            'sha256': digest(raw),
            'metadata': {
                key: value
                for key, value in document.items()
                if key != 'questions'
            },
        }
    for item in queries:
        validate_question(item, papers)
    require(
        len({item['id'] for item in queries}) == len(queries),
        'Duplicate query ID',
    )
    require(
        len({item['query'].casefold() for item in queries}) == len(queries),
        'Duplicate query text',
    )
    document = {
        'schema_version': 1,
        'kind': 'frozen-full-corpus-quality-diagnostics',
        'corpus_identity': identity,
        'release_id': manifest['release_id'],
        'embedding_signature': manifest['embedding_signature'],
        'preparation_manifest_sha256': digest(
            (Path(root) / 'probe.json').read_bytes()
        ),
        'selection': {
            'seed': SEED,
            'count': QUERY_COUNT,
            'max_per_paper': MAX_PER_PAPER,
            'method': 'hash-ranked round-robin source sentences',
            'filters': '18..100 English words; 80..900 characters; '
            'no formula markup; exact normalized dedup; no overlapping '
            'source spans or duplicate target chunks within a paper',
        },
        'natural_provenance': natural_provenance,
        'limitations': [
            'Extractive queries literally quote indexed source text.',
            'Fixed development diagnostics, not representative held-out quality.',
            'Source chunk identity is not an exhaustive relevance judgment.',
            'Answer windows use fixed source spans, not generated-answer grading.',
        ],
        'queries': queries,
    }
    write_json(output, document, immutable=True)
    return document


def rebase(old_root, new_root, queries_path, output):
    '''Remap frozen evidence to new chunks without changing any question.'''
    old_manifest, old_papers, _, old_identity = corpus_inputs(old_root)
    manifest, papers, _, identity = corpus_inputs(new_root)
    document = json_file(queries_path)
    require(
        document.get('kind') == 'frozen-full-corpus-quality-diagnostics'
        and document.get('corpus_identity') == old_identity,
        'Frozen queries do not belong to the original corpus',
    )
    require(
        old_manifest['paper_ids'] == manifest['paper_ids']
        and set(old_papers) == set(papers)
        and all(
            old_papers[key]['text'] == papers[key]['text'] for key in papers
        ),
        'Rebasing requires identical full-corpus canonical text',
    )
    require(
        Path(queries_path).resolve() != Path(output).resolve(),
        'Rebasing must preserve the original frozen query file',
    )
    remapped = []
    for original in document['queries']:
        validate_question(original, old_papers)
        item = json.loads(json.dumps(original))
        paper_id = item['expected_paper_id']
        indices = containing_chunk_indices(
            papers[paper_id], item['answer_spans']
        )
        require(
            indices,
            'Rechunking lost complete answer-span coverage: ' + item['id'],
        )
        item['gold_chunk_indices'] = indices
        if 'gold_chunk_ids' in item:
            item['gold_chunk_ids'] = [
                vector_id(manifest['slot'], paper_id, i) for i in indices
            ]
        if 'gold_chunk_keys' in item:
            item['gold_chunk_keys'] = [f'{paper_id}#{i}' for i in indices]
        if 'source_chunk_index' in item:
            item['source_chunk_index'] = indices[0]
        validate_question(item, papers)
        remapped.append(item)
    rebased = {
        **document,
        'queries': remapped,
        'corpus_identity': identity,
        'release_id': manifest['release_id'],
        'embedding_signature': manifest['embedding_signature'],
        'preparation_manifest_sha256': digest(
            (Path(new_root) / 'probe.json').read_bytes()
        ),
        'rebase': {
            'prior_query_manifest_sha256': digest(
                Path(queries_path).read_bytes()
            ),
            'prior_corpus_identity': old_identity,
            'prior_release_id': old_manifest['release_id'],
            'method': 'Exact unchanged source spans remapped to every '
            'containing canonical chunk; no retrieval scores used.',
            'questions_and_evidence_unchanged': True,
            'full_corpus_text_unchanged': True,
        },
    }
    write_json(output, rebased, immutable=True)
    return rebased


def verify_run(
    corpus, queries_path, full_run_confirmed, preflight_certificate
):
    require(
        full_run_confirmed and preflight_certificate and corpus,
        'Query encoding/evaluation requires explicit full-run '
        'confirmation and a current preflight certificate',
    )
    from preflight_full_search_probe import verify_certificate

    verify_certificate(
        preflight_certificate,
        corpus=corpus,
        queries=queries_path,
        config=load_embed(),
    )


def encode(
    queries_path,
    output,
    cache_dir,
    *,
    threads=4,
    batch_size=8,
    local_files_only=True,
    encoder=None,
    full_run_confirmed=False,
    preflight_certificate=None,
    corpus=None,
):
    document = json_file(queries_path)
    config = load_embed()
    require(
        document.get('kind') == 'frozen-full-corpus-quality-diagnostics'
        and document.get('embedding_signature') == embedding_signature(config),
        'Frozen queries use a different embedding configuration',
    )
    # Injection is useful for unit tests, but never bypasses authorization.
    # Small structural tests explicitly mock the verifier instead.
    verify_run(corpus, queries_path, full_run_confirmed, preflight_certificate)
    if encoder is None:
        encoder = BgeEncoder(
            config, threads=threads, local_files_only=local_files_only
        )
    signature = digest(canonical_json(encoder.identity).encode())
    cache_dir = Path(cache_dir) / signature
    cache_dir.mkdir(parents=True, exist_ok=True)
    inputs = [
        model_input(config['query_template'], row['query'])
        for row in document['queries']
    ]
    # Check every input, including cached queries, before any model inference.
    # The production encoder provides this tokenizer-only method.
    if hasattr(encoder, 'validate_inputs'):
        encoder.validate_inputs(inputs)
    keys = [digest(text.encode()) for text in inputs]
    tokenizer = WordPieceTokenizer(config)
    contexts = [
        cache_context(signature, key, text, config, tokenizer)
        for key, text in zip(keys, inputs)
    ]
    recovered = []
    vectors = [
        recover_cached_vector(
            cache_dir / (key + '.f32'), expected=context,
            cache_root=cache_dir.parent, recovery_log=recovered,
        )
        for key, context in zip(keys, contexts)
    ]
    missing = [i for i, value in enumerate(vectors) if value is None]
    for first in range(0, len(missing), batch_size):
        indices = missing[first : first + batch_size]
        values = encoder([inputs[index] for index in indices])
        require(
            len(values) == len(indices), 'Wrong query embedding batch size'
        )
        for index, value in zip(indices, values):
            write_cached_vector(
                cache_dir / (keys[index] + '.f32'),
                value,
                expected=contexts[index],
                execution=execution_profile(
                    encoder, batch_size=batch_size,
                    actual_batch_size=len(indices), length_bucketing=False,
                ),
            )
            vectors[index] = value
        print(
            json.dumps(
                {
                    'encoded': min(first + batch_size, len(missing)),
                    'missing': len(missing),
                }
            ),
            flush=True,
        )
    raw = b''.join(vector_bytes(value) for value in vectors)
    atomic_bytes(Path(output), raw)
    metadata = {
        'schema_version': 1,
        'count': len(vectors),
        'dimensions': 768,
        'dtype': 'float32',
        'byte_order': 'little',
        'query_manifest_sha256': digest(Path(queries_path).read_bytes()),
        'vectors_sha256': digest(raw),
        'encoder': encoder.identity,
        'encoder_signature': signature,
        'query_template': config['query_template'],
        'cached': len(vectors) - len(missing),
        'encoded': len(missing),
        'recovered_cache_entries': len(recovered),
        'execution_settings_requested': execution_profile(
            encoder, batch_size=batch_size, length_bucketing=False,
        ),
        'cache_trust': 'local-integrity-not-execution-attestation',
        'cache_reuse_contract': 'semantic-identity-not-bitwise-equivalence',
    }
    write_json(str(output) + '.json', metadata)
    return metadata


def unit_matrix(path, count, dimensions=768):
    require(
        Path(path).stat().st_size == count * dimensions * 4,
        'Embedding byte count mismatch',
    )
    values = np.memmap(path, dtype='<f4', mode='r', shape=(count, dimensions))
    require(np.isfinite(values).all(), 'Non-finite embedding')
    norms = np.linalg.norm(values.astype(np.float64), axis=1)
    require(np.max(np.abs(norms - 1)) < 1e-4, 'Non-unit embedding')
    return values


def rank_scores(scores, ids, limit=TOP_CANDIDATES):
    '''Deterministic score descending / vector-ID ascending, including ties.'''
    ids = np.asarray(ids)
    result = []
    for values in scores:
        if len(values) <= limit:
            candidates = np.arange(len(values))
        else:
            cutoff = np.partition(values, -limit)[-limit]
            candidates = np.flatnonzero(values >= cutoff)
        order = np.lexsort((ids[candidates], -values[candidates]))
        result.append(candidates[order[:limit]])
    return np.asarray(result, dtype=np.int64)


def retained(ranking, rows, candidates, limit):
    seen, result = set(), []
    for index in ranking[:candidates]:
        row = rows[int(index)]
        if row['paper_id'] not in seen:
            seen.add(row['paper_id'])
            result.append(int(index))
            if len(result) == limit:
                break
    return result


def outcomes(ranking, question, rows, papers, *, candidates, limit, protocol):
    selected = retained(ranking, rows, candidates, limit)
    target = next(
        (
            rows[index]
            for index in selected
            if rows[index]['paper_id'] == question['expected_paper_id']
        ),
        None,
    )
    if target is None:
        return dict(
            paper=False,
            source_chunk=False,
            answer_passage=False,
            answer_window=False,
            selected_rows=selected,
        )
    spans = question['answer_spans']
    contains = lambda start, end: all(
        start <= span['start'] < span['end'] <= end for span in spans
    )
    start = (
        target['start']
        if protocol == 'rest'
        else target['start'] // 16000 * 16000
    )
    length = 6000 if protocol == 'rest' else 16000
    end = min(len(papers[target['paper_id']]['text']), start + length)
    return {
        'paper': True,
        'source_chunk': target['chunk_index']
        in question['gold_chunk_indices'],
        'answer_passage': contains(target['start'], target['end']),
        'answer_window': contains(start, end),
        'selected_rows': selected,
        'target_chunk': target['chunk_index'],
        'context_start': start,
        'context_end': end,
    }


def paired_summary(reference, candidate, groups):
    reference, candidate = np.asarray(reference, bool), np.asarray(
        candidate, bool
    )
    losses = reference.astype(float) - candidate.astype(float)
    unique, inverse = np.unique(groups, return_inverse=True)
    counts = np.bincount(inverse)
    totals = np.bincount(inverse, weights=losses)
    draws = np.random.default_rng(751).integers(
        0, len(unique), (4000, len(unique))
    )
    bootstrap = totals[draws].sum(axis=1) / counts[draws].sum(axis=1)
    return {
        'reference': float(reference.mean()),
        'candidate': float(candidate.mean()),
        'paired_loss_pp': 100 * float(losses.mean()),
        'lost': int(np.sum(reference & ~candidate)),
        'gained': int(np.sum(~reference & candidate)),
        'clusters': len(unique),
        'diagnostic_cluster_bootstrap_upper95_pp': 100
        * float(np.quantile(bootstrap, 0.95)),
        'zero_discordance': bool(np.all(losses == 0)),
        'uncertainty_scope': 'Descriptive paper-cluster bootstrap; small development '
        'cohort and zero discordance do not establish a <=5pp population bound.',
    }


def evaluate(
    root,
    queries_path,
    query_vectors,
    runtime_rankings,
    output,
    *,
    batch_size=32,
    full_run_confirmed=False,
    preflight_certificate=None,
):
    verify_run(root, queries_path, full_run_confirmed, preflight_certificate)
    started = time.monotonic()
    manifest, papers, _, identity = corpus_inputs(root)
    document, query_meta = json_file(queries_path), json_file(
        str(query_vectors) + '.json'
    )
    require(
        document['corpus_identity'] == identity, 'Frozen query corpus changed'
    )
    query_hash = digest(Path(queries_path).read_bytes())
    require(
        query_meta['query_manifest_sha256'] == query_hash,
        'Query vectors use different questions',
    )
    require(
        query_meta['vectors_sha256']
        == digest(Path(query_vectors).read_bytes()),
        'Query embedding checksum mismatch',
    )
    questions, rows = document['queries'], manifest['rows']
    for question in questions:
        validate_question(question, papers)
    vectors_info = manifest['embeddings']
    require(
        query_meta.get('encoder_signature')
        == vectors_info.get('encoder_signature')
        and query_meta.get('encoder_signature')
        and query_meta['encoder_signature']
        == digest(canonical_json(query_meta['encoder']).encode()),
        'Corpus and query encoder identities differ',
    )
    require(
        query_meta.get('query_template') == load_embed()['query_template'],
        'Query template differs from the production embedding config',
    )
    fp32_path = checked_path(Path(root), vectors_info['path'])
    require(
        digest(fp32_path.read_bytes()) == vectors_info['sha256'],
        'FP32 corpus checksum mismatch',
    )
    corpus = unit_matrix(fp32_path, len(rows)).astype(np.float64)
    queries = unit_matrix(query_vectors, len(questions)).astype(np.float64)
    queries /= np.linalg.norm(queries, axis=1, keepdims=True)
    runtime = json_file(runtime_rankings)
    require(
        runtime.get('query_vectors_sha256') == query_meta['vectors_sha256']
        and runtime.get('manifest_sha256')
        == digest((Path(root) / 'probe.json').read_bytes())
        and runtime.get('engine') == 'full-int8-runtime',
        'Actual runtime rankings have different provenance',
    )
    candidate = np.asarray(runtime['rankings'], dtype=np.int64)
    require(
        candidate.shape == (len(questions), TOP_CANDIDATES)
        and np.all((candidate >= 0) & (candidate < len(rows)))
        and all(len(set(row)) == TOP_CANDIDATES for row in candidate),
        'Invalid actual runtime ranking geometry',
    )
    ids = [row['id'] for row in rows]
    reference = []
    for first in range(0, len(queries), batch_size):
        reference.extend(
            rank_scores(queries[first : first + batch_size] @ corpus.T, ids)
        )
    reference = np.asarray(reference)
    details = []
    for index, (question, ref, cand) in enumerate(
        zip(questions, reference, candidate)
    ):
        entry = {
            'query_id': question['id'],
            'cohort': question['cohort'],
            'paper_id': question['expected_paper_id'],
            'overlap_at8': len(set(ref[:8]) & set(cand[:8])) / 8,
            'reference8_contained_candidate50': len(
                set(ref[:8]) & set(cand[:50])
            )
            / 8,
            'reference_top50': ref.tolist(),
            'candidate_top50': cand.tolist(),
            'source_chunk_at50': {
                name: any(
                    rows[int(pos)]['paper_id'] == question['expected_paper_id']
                    and rows[int(pos)]['chunk_index']
                    in question['gold_chunk_indices']
                    for pos in rank[:50]
                )
                for name, rank in [('fp32', ref), ('int8', cand)]
            },
        }
        for protocol, candidate_limit, k in [
            ('rest', 40, 8),
            ('mcp_semantic', 25, 5),
        ]:
            entry[protocol] = {
                name: outcomes(
                    rank,
                    question,
                    rows,
                    papers,
                    candidates=candidate_limit,
                    limit=k,
                    protocol='rest' if protocol == 'rest' else 'mcp',
                )
                for name, rank in [('fp32', ref), ('int8', cand)]
            }
        details.append(entry)
    cohorts = {}
    for cohort in sorted({item['cohort'] for item in details}):
        selected = [item for item in details if item['cohort'] == cohort]
        overlap = np.array([item['overlap_at8'] for item in selected])
        containment = np.array(
            [item['reference8_contained_candidate50'] for item in selected]
        )
        result = {
            'n': len(selected),
            'papers': len({item['paper_id'] for item in selected}),
            'overlap_at8': float(overlap.mean()),
            'share_overlap_below_half': float(np.mean(overlap < 0.5)),
            'reference8_contained_candidate50': float(containment.mean()),
        }
        result['source_chunk_at50'] = paired_summary(
            [item['source_chunk_at50']['fp32'] for item in selected],
            [item['source_chunk_at50']['int8'] for item in selected],
            [item['paper_id'] for item in selected],
        )
        for protocol in ('rest', 'mcp_semantic'):
            result[protocol] = {
                metric: paired_summary(
                    [item[protocol]['fp32'][metric] for item in selected],
                    [item[protocol]['int8'][metric] for item in selected],
                    [item['paper_id'] for item in selected],
                )
                for metric in (
                    'paper',
                    'source_chunk',
                    'answer_passage',
                    'answer_window',
                )
            }
        cohorts[cohort] = result
    detail_path = Path(output).with_suffix('.queries.jsonl')
    atomic_bytes(
        detail_path,
        ''.join(canonical_json(row) + '\n' for row in details).encode(),
    )
    fidelity = cohorts.get('extractive_fidelity', {})
    report = {
        'schema_version': 1,
        'kind': 'offline-full-corpus-quality-diagnostics',
        'corpus_identity': identity,
        'release_id': manifest['release_id'],
        'passage_count': len(rows),
        'paper_count': len(papers),
        'manifest_sha256': digest((Path(root) / 'probe.json').read_bytes()),
        'query_manifest_sha256': query_hash,
        'query_vectors_sha256': query_meta['vectors_sha256'],
        'corpus_vectors_sha256': vectors_info['sha256'],
        'runtime_rankings_sha256': digest(Path(runtime_rankings).read_bytes()),
        'details_path': str(detail_path),
        'details_sha256': digest(detail_path.read_bytes()),
        'versions': {
            'python': platform.python_version(),
            'numpy': np.__version__,
        },
        'evaluator_source_sha256': digest(Path(__file__).read_bytes()),
        'reference': 'Canonical FP32 corpus, normalized FP32 query inputs, float64 BLAS accumulation',
        'candidate': runtime.get('implementation'),
        'cohorts': cohorts,
        'extractive_fidelity_gate': (
            'passed'
            if fidelity.get('n', 0) >= QUERY_COUNT
            and fidelity.get('reference8_contained_candidate50', 0) >= 0.95
            else 'failed'
        ),
        'heldout_quality_gate': 'unverified',
        'answer_utility_gate': 'unverified',
        'production_readiness': 'unverified',
        'platform_cpu_gate': 'unverified',
        'limitations': document['limitations']
        + [
            'MCP semantic projection uses top25->5, excluding catalog routing/metadata.',
            'Runtime rankings use actual candidate code; local wall time is not platform CPU.',
            'No query, answer span, or threshold is revised after observing results.',
        ],
        'elapsed_seconds': time.monotonic() - started,
    }
    write_json(output, report)
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    prepare_cli = sub.add_parser('prepare')
    prepare_cli.add_argument('--corpus', type=Path, required=True)
    prepare_cli.add_argument('--natural', type=Path)
    prepare_cli.add_argument('--output', type=Path, required=True)
    rebase_cli = sub.add_parser('rebase')
    rebase_cli.add_argument('--old-corpus', type=Path, required=True)
    rebase_cli.add_argument('--corpus', type=Path, required=True)
    rebase_cli.add_argument('--queries', type=Path, required=True)
    rebase_cli.add_argument('--output', type=Path, required=True)
    encode_cli = sub.add_parser('encode')
    encode_cli.add_argument('--queries', type=Path, required=True)
    encode_cli.add_argument('--output', type=Path, required=True)
    encode_cli.add_argument('--cache-dir', type=Path, required=True)
    encode_cli.add_argument('--threads', type=int, default=4)
    encode_cli.add_argument('--batch-size', type=int, default=8)
    encode_cli.add_argument('--allow-model-download', action='store_true')
    encode_cli.add_argument('--full-run-confirmed', action='store_true')
    encode_cli.add_argument('--preflight-certificate', type=Path)
    encode_cli.add_argument('--corpus', type=Path)
    evaluate_cli = sub.add_parser('evaluate')
    evaluate_cli.add_argument('--corpus', type=Path, required=True)
    evaluate_cli.add_argument('--queries', type=Path, required=True)
    evaluate_cli.add_argument('--query-vectors', type=Path, required=True)
    evaluate_cli.add_argument('--runtime-rankings', type=Path, required=True)
    evaluate_cli.add_argument('--output', type=Path, required=True)
    evaluate_cli.add_argument('--batch-size', type=int, default=32)
    evaluate_cli.add_argument('--full-run-confirmed', action='store_true')
    evaluate_cli.add_argument('--preflight-certificate', type=Path)
    args = parser.parse_args(argv)
    if args.command == 'prepare':
        result = prepare(args.corpus, args.output, args.natural)
        print(
            json.dumps(
                {'queries': len(result['queries']), 'output': str(args.output)}
            )
        )
    elif args.command == 'rebase':
        result = rebase(
            args.old_corpus, args.corpus, args.queries, args.output
        )
        print(
            json.dumps(
                {
                    'queries': len(result['queries']),
                    'output': str(args.output),
                    'rebase': result['rebase'],
                }
            )
        )
    elif args.command == 'encode':
        require(
            1 <= args.threads <= 8 and 1 <= args.batch_size <= 32,
            'Use at most eight CPU threads and batches <=32',
        )
        result = encode(
            args.queries,
            args.output,
            args.cache_dir,
            threads=args.threads,
            batch_size=args.batch_size,
            local_files_only=not args.allow_model_download,
            full_run_confirmed=args.full_run_confirmed,
            preflight_certificate=args.preflight_certificate,
            corpus=args.corpus,
        )
        print(json.dumps(result))
    else:
        require(1 <= args.batch_size <= 128, 'Scoring batch must be 1..128')
        result = evaluate(
            args.corpus,
            args.queries,
            args.query_vectors,
            args.runtime_rankings,
            args.output,
            batch_size=args.batch_size,
            full_run_confirmed=args.full_run_confirmed,
            preflight_certificate=args.preflight_certificate,
        )
        print(
            json.dumps(
                {
                    'extractive_fidelity_gate': result[
                        'extractive_fidelity_gate'
                    ],
                    'heldout_quality_gate': result['heldout_quality_gate'],
                }
            )
        )
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
