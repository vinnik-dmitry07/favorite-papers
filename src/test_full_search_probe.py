'''Full-corpus canonical fidelity, missing text and row mapping checks.'''

import hashlib
import json

import pytest

from build_agent_index import (
    BuildError,
    WordPieceTokenizer,
    build_release,
    canonical_json,
    clean_markdown,
    input_hash,
    load_embed,
    model_input,
    sha256_hex,
    vector_id,
)
from build_full_search_probe import (
    SCOPE,
    SLOT,
    build_full_corpus,
    main,
    write_full_corpus,
)
from common import ROOT


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
    graph = {
        'nodes': [node('z'), node('missing'), node('a'), node('empty')],
        'edges': [[0, 1, 'id'], [2, 0, 'title'], [1, 3, 'url']],
    }
    texts = {
        'a': '# Unicode\n\n' + '😀 café 中文𝒜. Canonical evidence. ' * 40,
        'z': '# Second paper\n\nThe final available document.\n',
        'empty': '## References\nRemoved citation.\n',
    }
    return graph, texts, load_embed()


def build_fixture(**kwargs):
    return build_full_corpus(*fixture(), **kwargs)


def test_full_release_is_exactly_canonical_including_unavailable_cards():
    graph, texts, embed = fixture()
    release, probe = build_full_corpus(
        graph, texts, embed, source_sha='source-commit',
    )
    expected = build_release(
        graph['nodes'], graph['edges'], texts, embed,
        git_sha_value='source-commit',
    )
    assert release == expected
    assert probe['paper_ids'] == ['a', 'empty', 'missing', 'z']
    assert probe['text_paper_ids'] == ['a', 'z']
    assert probe['unavailable_text'] == [
        {'paper_id': 'empty', 'reason': 'empty_cleaned'},
        {'paper_id': 'missing', 'reason': 'no_markdown'},
    ]
    assert probe['node_count'] == 4
    assert probe['papers_with_text'] == probe['papers_without_text'] == 2
    assert probe['edge_count'] == 3
    assert release['graph']['out']['missing'] == [
        {'target': 'empty', 'evidence': 'url'},
    ]
    assert 'empty' not in release['papers']
    assert 'missing' not in release['papers']


def test_rows_match_canonical_unicode_offsets_hashes_and_model_token_ids():
    graph, texts, embed = fixture()
    embed['passage_template'] = 'passage: '
    release, probe = build_full_corpus(graph, texts, embed)
    tokenizer = WordPieceTokenizer(embed)
    expected_pairs = []
    for paper_id in probe['text_paper_ids']:
        paper = release['papers'][paper_id]
        assert paper['text'] == clean_markdown(texts[paper_id])
        expected_pairs.extend((paper_id, chunk['index'])
                              for chunk in paper['chunks'])
    assert [(row['paper_id'], row['chunk_index'])
            for row in probe['rows']] == expected_pairs
    for row in probe['rows']:
        paper = release['papers'][row['paper_id']]
        chunk = paper['chunks'][row['chunk_index']]
        for key in ('start', 'end', 'token_count', 'content_hash',
                    'input_hash'):
            assert row[key] == chunk[key]
        piece = paper['text'][row['start']:row['end']]
        assert sha256_hex(piece) == row['content_hash']
        assert input_hash(embed, piece, probe['embedding_signature']) == (
            row['input_hash'])
        ids = tokenizer.token_ids(embed['passage_template'], piece)
        assert ids == tokenizer.token_ids(
            '', model_input(embed['passage_template'], piece))
        assert len(ids) == row['token_count'] <= embed['max_input_tokens']
        assert row['id'] == vector_id(
            SLOT, row['paper_id'], row['chunk_index'])
    text = release['papers']['a']['text']
    assert len(text.encode('utf-16-le')) // 2 > len(text)
    assert probe['rows_sha256'] == sha256_hex(canonical_json(probe['rows']))


def test_order_changes_do_not_change_release_or_vector_row_mapping():
    graph, texts, embed = fixture()
    first, first_probe = build_full_corpus(graph, texts, embed)
    reordered = {
        'nodes': graph['nodes'][::-1],
        'edges': [[3 - source, 3 - target, evidence]
                  for source, target, evidence in reversed(graph['edges'])],
    }
    second, second_probe = build_full_corpus(reordered, texts, embed)
    assert first == second
    assert first_probe['rows'] == second_probe['rows']
    assert first_probe['rows_sha256'] == second_probe['rows_sha256']
    assert first_probe['paper_ids'] == second_probe['paper_ids']
    assert first_probe['source_graph_sha256'] != (
        second_probe['source_graph_sha256'])


def test_source_and_canonical_manifest_provenance_are_distinct():
    graph, texts, embed = fixture()
    raw = json.dumps(graph, indent=4).encode()
    digest = hashlib.sha256(raw).hexdigest()
    release, probe = build_full_corpus(
        graph, texts, embed, source_path='custom/graph.json',
        source_sha='commit-a', source_graph_sha256=digest,
    )
    assert probe['source_path'] == 'custom/graph.json'
    assert probe['source_sha'] == 'commit-a'
    assert probe['source_graph_sha256'] == digest
    assert probe['source_text_hashes']['a'] == sha256_hex(texts['a'])
    assert probe['source_text_hashes']['missing'] is None
    assert probe['source_text_hashes']['empty'] == sha256_hex(texts['empty'])
    assert probe['source_texts_sha256'] == sha256_hex(
        canonical_json(probe['source_text_hashes']))
    assert probe['canonical_manifest_sha256'] == sha256_hex(
        canonical_json(release['manifest']))
    alternate, alternate_probe = build_full_corpus(
        graph, texts, embed, source_sha='commit-b',
    )
    assert alternate['release_id'] == release['release_id']
    assert alternate_probe['canonical_manifest_sha256'] != (
        probe['canonical_manifest_sha256'])
    embed['_vocab_path'] = 'irrelevant-local-path'
    # Local paths are not part of the reproducible source config checksum.
    public_embed = {key: value for key, value in embed.items()
                    if not key.startswith('_')}
    assert probe['source_embed_sha256'] == sha256_hex(
        canonical_json(public_embed))


def test_full_scope_is_explicit_and_no_quality_or_publication_is_claimed():
    _release, probe = build_fixture()
    assert probe['kind'] == 'full-corpus'
    assert probe['scope'] == SCOPE
    assert probe['slot'] == 'full-probe'
    assert probe['synthetic'] is False
    assert probe['publication_ready'] is False
    assert probe['semantic_quality_gate'] == 'unverified'
    assert probe['workers_ai_compatibility'] == 'unverified'
    assert probe['embeddings'] is None
    assert 'queries' not in probe
    assert probe['vector_layout'] == {
        'dtype': 'float32', 'byte_order': 'little', 'order': 'row-major',
        'dimensions': 768, 'row_bytes': 3072,
        'expected_bytes': probe['passage_count'] * 3072,
    }


def test_full_corpus_is_not_silently_capped_at_subset_size():
    graph = {'nodes': [node('many')], 'edges': []}
    embed = load_embed()
    embed['max_code_points'] = 32
    embed['overlap_code_points'] = 4
    release, probe = build_full_corpus(
        graph, {'many': 'A complete long source text. ' * 600}, embed,
    )
    assert probe['passage_count'] > 500
    assert probe['passage_count'] == len(release['papers']['many']['chunks'])
    assert probe['rows'][-1]['end'] == len(release['papers']['many']['text'])


def test_written_assets_are_canonical_and_absence_is_not_fabricated(tmp_path):
    release, probe = build_fixture()
    saved = write_full_corpus(release, probe, tmp_path)
    assert json.loads((tmp_path / 'probe.json').read_text()) == saved
    assert len(saved['files']) == len(saved['text_paper_ids']) + 2
    prefix = f'releases/{saved["release_id"]}'
    assert saved['files'][prefix + '/manifest.json'] == (
        saved['canonical_manifest_sha256'])
    for relative, digest in saved['files'].items():
        raw = (tmp_path / relative).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == digest
        assert raw == canonical_json(json.loads(raw)).encode()
    for paper_id in ('empty', 'missing'):
        assert not (tmp_path / prefix / 'papers'
                    / (sha256_hex(paper_id) + '.json')).exists()
    for forbidden in ('active.json', 'confirmed.json', 'vectors.f32',
                      'slots', 'smoke.json'):
        assert not (tmp_path / forbidden).exists()
    first_bytes = (tmp_path / 'probe.json').read_bytes()
    write_full_corpus(release, probe, tmp_path)
    assert (tmp_path / 'probe.json').read_bytes() == first_bytes


def test_writer_cannot_overwrite_existing_subset_manifest(tmp_path):
    release, probe = build_fixture()
    original = '{"kind":"real-subset","embeddings":{"ready":true}}'
    (tmp_path / 'probe.json').write_text(original)
    with pytest.raises(BuildError, match='different probe kind'):
        write_full_corpus(release, probe, tmp_path)
    assert (tmp_path / 'probe.json').read_text() == original
    assert sorted(path.name for path in tmp_path.iterdir()) == ['probe.json']


@pytest.mark.parametrize('graph', [
    None,
    {'nodes': [], 'edges': []},
    {'nodes': [node('only')], 'edges': []},
    {'nodes': [node('dup'), node('dup')], 'edges': []},
    {'nodes': [node('only')], 'edges': [[0, 9, 'id']]},
])
def test_empty_or_malformed_corpus_fails_closed(graph):
    with pytest.raises(BuildError):
        build_full_corpus(graph, {}, load_embed())


def test_wrong_embedding_dimension_fails():
    graph, texts, embed = fixture()
    embed['dimensions'] = 384
    with pytest.raises(BuildError, match='768 dimensions'):
        build_full_corpus(graph, texts, embed)


def test_cli_cannot_overwrite_real_subset():
    with pytest.raises(SystemExit) as error:
        main(['--out', str(ROOT / 'agent_real_probe')])
    assert error.value.code == 2
