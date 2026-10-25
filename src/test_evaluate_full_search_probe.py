'''Independent ranking, evidence-window and frozen-input regressions.'''

import numpy as np
import pytest

import evaluate_full_search_probe as quality
from build_agent_index import BuildError


def test_top_k_includes_ties_then_orders_by_vector_id():
    scores = np.array([[0.4, 0.8, 0.8, 0.8, 0.1]])
    ids = ['e', 'c', 'a', 'b', 'd']
    assert quality.rank_scores(scores, ids, 2).tolist() == [[2, 3]]


def test_production_candidate_depth_precedes_paper_deduplication():
    rows = [{'paper_id': 'same'} for _ in range(41)]
    rows += [{'paper_id': 'second'}, {'paper_id': 'third'}]
    ranking = list(range(len(rows)))
    assert quality.retained(ranking, rows, 40, 8) == [0]
    assert quality.retained(ranking, rows, 25, 5) == [0]
    assert quality.retained(ranking, rows, 43, 8) == [0, 41, 42]


def question():
    return {
        'id': 'q',
        'query': 'What setting was used?',
        'expected_paper_id': 'p',
        'gold_chunk_indices': [1],
        'answer_span_policy': 'all',
        'answer_spans': [{'start': 6050, 'end': 6060, 'quote': 'gold quote'}],
    }


def test_passage_and_answer_windows_are_different_and_bounded():
    rows = [{'paper_id': 'p', 'chunk_index': 0, 'start': 100, 'end': 800}]
    papers = {'p': {'text': 'x' * 20000}}
    item = question()
    result = quality.outcomes(
        [0], item, rows, papers, candidates=40, limit=8, protocol='rest'
    )
    assert result['paper'] is True
    assert result['source_chunk'] is result['answer_passage'] is False
    assert result['answer_window'] is True
    item['answer_spans'][0].update(start=6100, end=6110)
    assert (
        quality.outcomes(
            [0], item, rows, papers, candidates=40, limit=8, protocol='rest'
        )['answer_window']
        is False
    )
    assert (
        quality.outcomes(
            [0], item, rows, papers, candidates=25, limit=5, protocol='mcp'
        )['answer_window']
        is True
    )


def test_answer_spans_all_required_and_unicode_offsets_exact():
    item = question()
    text = '😀 gold quote and second'
    item['answer_spans'] = [
        {'start': 2, 'end': 12, 'quote': 'gold quote'},
        {'start': 17, 'end': 23, 'quote': 'second'},
    ]
    item['gold_chunk_indices'] = [0]
    papers = {'p': {'text': text, 'chunks': [{'start': 0, 'end': len(text)}]}}
    quality.validate_question(item, papers)
    item['answer_spans'][0]['start'] = 3
    with pytest.raises(BuildError, match='canonical source'):
        quality.validate_question(item, papers)


def test_frozen_file_cannot_be_replaced_with_new_labels(tmp_path):
    path = tmp_path / 'frozen.json'
    quality.write_json(path, {'id': 1}, immutable=True)
    quality.write_json(path, {'id': 1}, immutable=True)
    with pytest.raises(BuildError, match='overwrite frozen'):
        quality.write_json(path, {'id': 2}, immutable=True)


def synthetic_sources():
    papers, rows, nodes = {}, [], {}
    for paper_num in range(3):
        paper_id = f'paper-{paper_num}'
        sentences = [
            f'This experiment number {index} for material {paper_num} evaluates '
            'the proposed method with several independent measurements and '
            'reports stable evidence across the carefully selected conditions.'
            for index in range(10)
        ]
        text, chunks = '', []
        for index, sentence in enumerate(sentences):
            start = len(text)
            text += sentence + '\n'
            chunk = {'start': start, 'end': len(text), 'index': index}
            chunks.append(chunk)
            rows.append({**chunk, 'paper_id': paper_id, 'chunk_index': index})
        papers[paper_id] = {
            'paper_id': paper_id,
            'text': text,
            'chunks': chunks,
        }
        nodes[paper_id] = {'title': 'Unrelated title'}
    return papers, rows, {'nodes': nodes}


def test_sentence_selection_is_deterministic_balanced_and_exact():
    papers, rows, graph = synthetic_sources()
    # Numeric-only differences intentionally normalize to duplicate text, so
    # use distinct alphabetic markers to make this fixture eligible.
    for number, (paper_id, paper) in enumerate(papers.items()):
        marker = ('alpha', 'bravo', 'gamma')[number]
        text = paper['text']
        for i, word in enumerate(
            (
                'one',
                'two',
                'three',
                'four',
                'five',
                'six',
                'seven',
                'eight',
                'nine',
                'ten',
            )
        ):
            text = text.replace(
                f'number {i} for material {number}',
                f'number {word} for material {marker}',
            )
        # Rebuild offsets after changing the text length.
        sentences = text.splitlines(keepends=True)
        paper['text'], paper['chunks'] = text, []
        offset = 0
        for index, sentence in enumerate(sentences):
            chunk = {
                'start': offset,
                'end': offset + len(sentence),
                'index': index,
            }
            paper['chunks'].append(chunk)
            offset += len(sentence)
    rows = [
        {**chunk, 'paper_id': paper_id, 'chunk_index': chunk['index']}
        for paper_id, paper in papers.items()
        for chunk in paper['chunks']
    ]
    selected = quality.select_sentences(papers, rows, graph, count=12)
    assert selected == quality.select_sentences(papers, rows, graph, count=12)
    assert len({row['normalized_sha256'] for row in selected}) == 12
    assert all(
        sum(row['expected_paper_id'] == key for row in selected) == 4
        for key in papers
    )
    for item in selected:
        quality.validate_question(item, papers)


def test_insufficient_sentence_pool_does_not_relax_filters():
    papers, rows, graph = synthetic_sources()
    with pytest.raises(BuildError, match='must not be relaxed'):
        quality.select_sentences(papers, rows, graph, count=2000)


def test_zero_discordance_is_labeled_descriptive_not_population_proof():
    result = quality.paired_summary(
        [True] * 4, [True] * 4, ['a', 'a', 'b', 'b']
    )
    assert result['zero_discordance'] is True
    assert result['diagnostic_cluster_bootstrap_upper95_pp'] == 0
    assert 'do not establish' in result['uncertainty_scope']
    assert result['clusters'] == 2


def evaluation_fixture(tmp_path, monkeypatch):
    # All vectors below are tiny artificial fixtures, not a full model run.
    monkeypatch.setattr(quality, 'verify_run', lambda *args: None)
    rows = [
        {
            'id': f'{i:064x}',
            'paper_id': f'p{i}',
            'chunk_index': 0,
            'start': 0,
            'end': 15,
        }
        for i in range(50)
    ]
    papers = {
        row['paper_id']: {
            'text': '😀 source answer',
            'chunks': [{'start': 0, 'end': 15}],
        }
        for row in rows
    }
    vectors = np.zeros((50, 768), dtype='<f4')
    for index in range(50):
        vectors[index, index] = 1
    (tmp_path / 'vectors.f32').write_bytes(vectors.tobytes())
    encoder = {'test': 'structural fixture only'}
    signature = quality.digest(quality.canonical_json(encoder).encode())
    manifest = {
        'rows': rows,
        'release_id': 'test',
        'embeddings': {
            'path': 'vectors.f32',
            'sha256': quality.digest(vectors.tobytes()),
            'encoder_signature': signature,
        },
    }
    quality.write_json(tmp_path / 'probe.json', manifest)
    questions = [
        {
            'id': f'q{i}',
            'cohort': 'extractive_fidelity',
            'query': f'Source question {i}',
            'expected_paper_id': f'p{i}',
            'gold_chunk_indices': [0],
            'answer_span_policy': 'all',
            'answer_spans': [
                {'start': 2, 'end': 15, 'quote': 'source answer'}
            ],
        }
        for i in range(2)
    ]
    query_path = tmp_path / 'queries.json'
    quality.write_json(
        query_path,
        {
            'queries': questions,
            'corpus_identity': 'identity',
            'limitations': ['Not held-out'],
        },
    )
    query_vectors = tmp_path / 'queries.f32'
    query_vectors.write_bytes(vectors[:2].tobytes())
    quality.write_json(
        str(query_vectors) + '.json',
        {
            'query_manifest_sha256': quality.digest(query_path.read_bytes()),
            'vectors_sha256': quality.digest(query_vectors.read_bytes()),
            'encoder_signature': signature,
            'encoder': encoder,
            'query_template': quality.load_embed()['query_template'],
        },
    )
    runtime_path = tmp_path / 'runtime.json'
    quality.write_json(
        runtime_path,
        {
            'query_vectors_sha256': quality.digest(query_vectors.read_bytes()),
            'manifest_sha256': quality.digest(
                (tmp_path / 'probe.json').read_bytes()
            ),
            'engine': 'full-int8-runtime',
            'rankings': quality.rank_scores(
                vectors[:2].astype(float) @ vectors.T,
                [row['id'] for row in rows],
            ).tolist(),
        },
    )
    monkeypatch.setattr(
        quality, 'corpus_inputs', lambda _: (manifest, papers, {}, 'identity')
    )
    return query_path, query_vectors, runtime_path


def test_evaluation_uses_actual_rankings_without_promoting_quality(
    tmp_path, monkeypatch
):
    paths = evaluation_fixture(tmp_path, monkeypatch)
    result = quality.evaluate(tmp_path, *paths, tmp_path / 'report.json')
    assert result['heldout_quality_gate'] == 'unverified'
    assert result['answer_utility_gate'] == 'unverified'
    assert (
        result['extractive_fidelity_gate'] == 'failed'
    )  # Only two fixture queries.
    metric = result['cohorts']['extractive_fidelity']['rest']['answer_window']
    assert metric['reference'] == metric['candidate'] == 1


def test_evaluation_rejects_rankings_from_another_query_set(
    tmp_path, monkeypatch
):
    paths = evaluation_fixture(tmp_path, monkeypatch)
    runtime = quality.json_file(paths[2])
    runtime['query_vectors_sha256'] = 'wrong'
    quality.write_json(paths[2], runtime)
    with pytest.raises(BuildError, match='different provenance'):
        quality.evaluate(tmp_path, *paths, tmp_path / 'report.json')


def test_rebase_preserves_questions_and_evidence_and_remaps_only_chunks(
    tmp_path, monkeypatch
):
    old_root, new_root = tmp_path / 'old', tmp_path / 'new'
    old_root.mkdir()
    new_root.mkdir()
    old = {'paper_ids': ['p'], 'release_id': 'old', 'slot': 'full-probe'}
    new = {**old, 'release_id': 'new', 'embedding_signature': 'new-signature'}
    quality.write_json(new_root / 'probe.json', new)
    text = '😀 exact answer retained'
    papers_old = {
        'p': {
            'text': text,
            'chunks': [{'index': 0, 'start': 0, 'end': len(text)}],
        }
    }
    papers_new = {
        'p': {
            'text': text,
            'chunks': [
                {'index': 0, 'start': 0, 'end': 3},
                {'index': 1, 'start': 2, 'end': len(text)},
            ],
        }
    }
    monkeypatch.setattr(
        quality,
        'corpus_inputs',
        lambda root: (
            (old, papers_old, {}, 'old-identity')
            if root == old_root
            else (new, papers_new, {}, 'new-identity')
        ),
    )
    question = {
        'id': 'frozen',
        'query': 'What is retained?',
        'expected_answer': 'The exact answer.',
        'expected_paper_id': 'p',
        'gold_chunk_indices': [0],
        'gold_chunk_ids': ['old-id'],
        'gold_chunk_keys': ['p#0'],
        'source_chunk_index': 0,
        'answer_span_policy': 'all',
        'answer_spans': [{'start': 2, 'end': 14, 'quote': 'exact answer'}],
    }
    frozen = {
        'kind': 'frozen-full-corpus-quality-diagnostics',
        'corpus_identity': 'old-identity',
        'queries': [question],
    }
    source, target = tmp_path / 'frozen.json', tmp_path / 'rebased.json'
    quality.write_json(source, frozen, immutable=True)
    before = source.read_bytes()
    result = quality.rebase(old_root, new_root, source, target)
    assert source.read_bytes() == before
    remapped = result['queries'][0]
    for key in ('query', 'expected_answer', 'answer_spans'):
        assert remapped[key] == question[key]
    assert remapped['gold_chunk_indices'] == [1]
    assert remapped['gold_chunk_keys'] == ['p#1']
    assert result['rebase']['questions_and_evidence_unchanged'] is True
    assert result['rebase']['prior_query_manifest_sha256'] == quality.digest(
        before
    )
    papers_new['p']['text'] += ' changed'
    with pytest.raises(BuildError, match='identical full-corpus'):
        quality.rebase(old_root, new_root, source, target)


def test_query_encode_requires_explicit_guard_before_model_load(
    tmp_path, monkeypatch
):
    frozen = tmp_path / 'frozen.json'
    quality.write_json(
        frozen,
        {
            'kind': 'frozen-full-corpus-quality-diagnostics',
            'embedding_signature': quality.embedding_signature(
                quality.load_embed()
            ),
            'queries': [{'query': 'Frozen query'}],
        },
    )
    monkeypatch.setattr(
        quality,
        'BgeEncoder',
        lambda *args, **kwargs: pytest.fail(
            'Model must not load before guard'
        ),
    )
    with pytest.raises(BuildError, match='explicit full-run confirmation'):
        quality.encode(frozen, tmp_path / 'q.f32', tmp_path / 'cache')


def test_full_evaluation_guard_runs_before_loading_vectors(tmp_path):
    with pytest.raises(BuildError, match='explicit full-run confirmation'):
        quality.evaluate(
            tmp_path,
            tmp_path / 'absent-queries',
            tmp_path / 'absent-vectors',
            tmp_path / 'absent-ranks',
            tmp_path / 'report.json',
        )


def test_all_query_inputs_are_preflighted_before_encoding_including_prefix(
    tmp_path, monkeypatch
):
    monkeypatch.setattr(quality, 'verify_run', lambda *args: None)
    config = {**quality.load_embed(), 'query_template': 'instruction: '}
    monkeypatch.setattr(quality, 'load_embed', lambda: config)
    frozen = tmp_path / 'frozen.json'
    quality.write_json(
        frozen,
        {
            'kind': 'frozen-full-corpus-quality-diagnostics',
            'embedding_signature': quality.embedding_signature(config),
            'queries': [{'query': 'First'}, {'query': 'Second'}],
        },
    )

    class Encoder:
        identity = {'test': 'no model'}

        def validate_inputs(self, inputs):
            assert inputs == ['instruction: First', 'instruction: Second']
            raise BuildError('Deliberate tokenizer mismatch')

        def __call__(self, inputs):
            pytest.fail('Inference must not run after preflight failure')

    with pytest.raises(BuildError, match='Deliberate tokenizer mismatch'):
        quality.encode(
            frozen, tmp_path / 'q.f32', tmp_path / 'cache', encoder=Encoder()
        )


def test_injected_encoder_cannot_bypass_full_run_guard(tmp_path):
    frozen = tmp_path / 'frozen.json'
    quality.write_json(
        frozen,
        {
            'kind': 'frozen-full-corpus-quality-diagnostics',
            'embedding_signature': quality.embedding_signature(
                quality.load_embed()
            ),
            'queries': [{'query': 'Frozen query'}],
        },
    )
    with pytest.raises(BuildError, match='explicit full-run confirmation'):
        quality.encode(
            frozen, tmp_path / 'q.f32', tmp_path / 'cache', encoder=object()
        )


def test_query_cache_binds_each_vector_to_input_and_rechecks_cached_inputs(
    tmp_path, monkeypatch
):
    monkeypatch.setattr(quality, 'verify_run', lambda *args: None)
    frozen = tmp_path / 'frozen.json'
    quality.write_json(
        frozen,
        {
            'kind': 'frozen-full-corpus-quality-diagnostics',
            'embedding_signature': quality.embedding_signature(
                quality.load_embed()
            ),
            'queries': [{'query': 'First query'}, {'query': 'Second query'}],
        },
    )

    class Encoder:
        identity = {'test': 'structural fixture, no model'}
        checked = 0
        calls = 0

        def validate_inputs(self, inputs):
            self.checked += len(inputs)

        def __call__(self, inputs):
            self.calls += 1
            return [
                [float(i == dimension) for dimension in range(768)]
                for i in range(len(inputs))
            ]

    encoder = Encoder()
    cache = tmp_path / 'cache'
    quality.encode(frozen, tmp_path / 'q.f32', cache, encoder=encoder)
    quality.encode(frozen, tmp_path / 'q.f32', cache, encoder=encoder)
    assert encoder.checked == 4
    assert encoder.calls == 1
    first, second = sorted(cache.rglob('*.f32'))
    first.write_bytes(second.read_bytes())
    with pytest.raises(BuildError, match='cache identity/checksum mismatch'):
        quality.encode(frozen, tmp_path / 'q.f32', cache, encoder=encoder)
    assert encoder.calls == 1
