'''Canonical integrity, induced graph and bounds of the real subset builder.'''

import hashlib
import json

import pytest

from build_agent_index import (
    BuildError,
    build_release,
    canonical_json,
    clean_markdown,
    input_hash,
    load_embed,
    sha256_hex,
    vector_id,
)
from build_real_search_probe import (
    SEED_ID,
    SLOT,
    build_subset,
    integration_queries,
    main,
    spread_indices,
    write_subset,
)


def node(identifier):
    return {
        'id': identifier,
        'title': identifier,
        'authors': ['A. Author'],
        'section': 'Test',
        'kind': 'arxiv',
        'url': 'https://example.test/paper',
    }


def fixture():
    # Source indices intentionally differ from the sorted subset indices.
    graph = {
        'nodes': [node('z'), node(SEED_ID), node('a'), node('unrelated')],
        'edges': [[0, 1, 'id'], [1, 2, 'title'], [2, 3, 'url']],
    }
    texts = {
        SEED_ID: '# Seed\n\n' + (
            'GRPO foregoes the critic model, instead estimating the baseline '
            'from group scores. The KL coefficient is 0.04. '
            'For each question, '
            'we sample 64 64 outputs. 😀 café 中文. '
        ) * 13,
        'a': '# Neighbor\n\n' + 'Related explanation. ' * 60,
        'z': '# Other neighbor\n\n' + 'Other data. ' * 100,
        'unrelated': '# Remote\n\nOnly farther away.\n',
    }
    return graph, texts, load_embed()


def build_fixture():
    graph, texts, embed = fixture()
    return build_subset(graph, texts, embed, minimum=3, target=5, maximum=10)


def test_induced_edges_remap_and_selected_papers_remain_complete():
    graph, texts, embed = fixture()
    release, probe = build_subset(
        graph, texts, embed, minimum=3, target=5, maximum=10,
    )
    assert probe['paper_ids'] == ['a', SEED_ID]
    assert probe['edge_count'] == 1
    assert release['graph']['out'][SEED_ID] == [
        {'target': 'a', 'evidence': 'title'},
    ]
    assert release['graph']['in']['a'] == [
        {'source': SEED_ID, 'evidence': 'title'},
    ]
    assert 'z' not in release['graph']['nodes']
    for paper_id in probe['paper_ids']:
        assert release['papers'][paper_id]['text'] == clean_markdown(
            texts[paper_id])
    expected = build_release(
        [node('a'), node(SEED_ID)], [[1, 0, 'title']],
        {paper_id: texts[paper_id] for paper_id in probe['paper_ids']}, embed,
    )
    assert release == expected


def test_rows_preserve_code_point_offsets_and_canonical_hashes():
    release, probe = build_fixture()
    embed = load_embed()
    for row in probe['rows']:
        paper = release['papers'][row['paper_id']]
        chunk = paper['chunks'][row['chunk_index']]
        assert (row['start'], row['end']) == (chunk['start'], chunk['end'])
        piece = paper['text'][row['start']:row['end']]
        assert row['content_hash'] == sha256_hex(piece)
        assert row['input_hash'] == input_hash(
            embed, piece, probe['embedding_signature'])
        assert row['id'] == vector_id(
            SLOT, row['paper_id'], row['chunk_index'])
        assert row['token_count'] == chunk['token_count']
    text = release['papers'][SEED_ID]['text']
    assert '😀' in text
    assert len(text.encode('utf-16-le')) // 2 > len(text)


def test_source_order_does_not_change_subset_release_or_rows():
    graph, texts, embed = fixture()
    first, first_probe = build_subset(
        graph, texts, embed, minimum=3, target=5, maximum=10,
    )
    reversed_graph = {
        'nodes': graph['nodes'][::-1],
        'edges': [[3 - source, 3 - target, evidence]
                  for source, target, evidence in reversed(graph['edges'])],
    }
    second, second_probe = build_subset(
        reversed_graph, texts, embed, minimum=3, target=5, maximum=10,
    )
    assert first == second
    assert first_probe['rows'] == second_probe['rows']
    assert first_probe['paper_ids'] == second_probe['paper_ids']


def test_written_files_match_manifest_hashes_and_have_no_publication_marker(
    tmp_path,
):
    release, probe = build_fixture()
    saved = write_subset(release, probe, tmp_path)
    assert saved == json.loads((tmp_path / 'probe.json').read_text())
    assert saved['embeddings'] is None
    assert saved['publication_ready'] is False
    assert saved['semantic_quality_gate'] == 'not_tested'
    assert not (tmp_path / 'active.json').exists()
    assert not (tmp_path / 'slots').exists()
    for relative, expected in saved['files'].items():
        raw = (tmp_path / relative).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == expected
        assert raw == canonical_json(json.loads(raw)).encode()
    assert len(saved['files']) == len(saved['paper_ids']) + 1
    assert all(query['expected_paper_id'] == SEED_ID
               for query in saved['queries'])
    assert len(saved['queries']) == 6


def test_compatibility_sample_spans_all_rows_without_duplicates():
    indices = spread_indices(390)
    assert len(indices) == len(set(indices)) == 200
    assert indices[0] == 0 and indices[-1] == 389
    assert indices == sorted(indices)
    assert spread_indices(3) == [0, 1, 2]
    assert spread_indices(1) == [0]


@pytest.mark.parametrize('minimum,target,maximum', [
    (0, 5, 10), (5, 3, 10), (3, 11, 10), (1, 5, 501), (True, 5, 10),
])
def test_invalid_bounds_fail(minimum, target, maximum):
    graph, texts, embed = fixture()
    with pytest.raises(BuildError, match='Expected'):
        build_subset(graph, texts, embed, minimum=minimum, target=target,
                     maximum=maximum)


def test_missing_seed_or_seed_text_fails():
    graph, texts, embed = fixture()
    with pytest.raises(BuildError, match='seed paper is missing'):
        build_subset({'nodes': [node('other')], 'edges': []}, {}, embed)
    for missing in (None, '', '## References\nDropped citation.\n'):
        with pytest.raises(BuildError, match='seed paper has no'):
            build_subset(graph, {**texts, SEED_ID: missing}, embed,
                         minimum=3, target=5, maximum=10)


def test_cap_never_slices_seed_or_accepts_inadequate_corpus():
    graph, texts, embed = fixture()
    with pytest.raises(BuildError, match='seed paper alone exceeds'):
        build_subset(graph, texts, embed, minimum=1, target=1, maximum=1)
    with pytest.raises(BuildError, match='cannot meet'):
        build_subset(graph, texts, embed, minimum=200, target=300, maximum=500)


def test_invalid_source_edge_rejected_before_selection():
    graph, texts, embed = fixture()
    graph['edges'].append([999, 1, 'id'])
    with pytest.raises(BuildError, match='index out of range'):
        build_subset(graph, texts, embed, minimum=3, target=5, maximum=10)


def test_cli_cannot_relax_experiment_bounds(tmp_path):
    with pytest.raises(SystemExit) as error:
        main(['--out', str(tmp_path), '--target', '100'])
    assert error.value.code == 2
    assert not list(tmp_path.iterdir())


def test_current_passage_oracles_are_source_grounded():
    release, probe = build_fixture()
    paper = release['papers'][SEED_ID]
    criteria = [query for query in probe['queries']
                if query.get('required_passage_terms')]
    assert {query['id'] for query in criteria} == {
        'group-baseline', 'grpo-settings',
    }
    for query in criteria:
        assert query['gold_chunk_indices']
        for index in query['gold_chunk_indices']:
            chunk = paper['chunks'][index]
            text = paper['text'][chunk['start']:chunk['end']].casefold()
            assert all(term.casefold() in text
                       for term in query['required_passage_terms'])
            assert any(all(term.casefold() in text for term in group)
                       for group in query.get('passage_evidence_any', [[]]))
        if 'expected_quote' in query:
            assert query['expected_quote'] in paper['text']


def test_missing_fixed_oracle_is_not_silently_dropped():
    graph, texts, embed = fixture()
    texts[SEED_ID] = texts[SEED_ID].replace('0.04', 'different')
    with pytest.raises(BuildError, match='oracle is absent'):
        build_subset(graph, texts, embed, minimum=3, target=5, maximum=10)


def test_v2_oracle_accepts_source_synonym_but_still_requires_answer_evidence():
    pieces = [
        'No baseline evidence here.',
        'Use the critic and group scores as a baseline.',
        'No extra value function: average reward of multiple sampled '
        'outputs supplies the baseline.',
        'A value function provides a baseline.',
        'The KL coefficient is 0.04. Sample 64 outputs.',
    ]
    text = '\n'.join(pieces)
    start = 0
    chunks = []
    for index, piece in enumerate(pieces):
        chunks.append({'index': index, 'start': start,
                       'end': start + len(piece)})
        start += len(piece) + 1
    queries = integration_queries(SEED_ID, {'text': text, 'chunks': chunks})
    by_id = {query['id']: query for query in queries}
    assert by_id['group-baseline']['gold_chunk_indices'] == [1, 2]
    assert by_id['grpo-settings']['gold_chunk_indices'] == [4]
    assert by_id['grpo-settings']['required_passage_terms'] == ['0.04', '64']


def test_v2_revision_explicitly_discloses_post_observation_adjudication():
    _release, probe = build_fixture()
    assert probe['oracle_revision'] == 2
    assert probe['oracle_note']['post_observation'] is True
    assert 'not a held-out or preregistered retrieval pass' in (
        probe['oracle_note']['reason'])
    assert probe['semantic_quality_gate'] == 'not_tested'
