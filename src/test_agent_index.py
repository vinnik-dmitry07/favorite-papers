'''Offline checks for cleaning, chunk coverage, and release identity.'''

from __future__ import annotations

import json
from copy import deepcopy
import sys
from pathlib import Path

import pytest

SRC = Path(__file__).resolve().parent
sys.path.insert(0, str(SRC))

from build_agent_index import (  # noqa: E402
    BuildError,
    CapacityError,
    WordPieceTokenizer,
    assert_capacity,
    build_from_disk,
    build_release,
    build_signature,
    chunk_text,
    clean_markdown,
    embedding_signature,
    input_hash,
    load_embed,
    load_written_release,
    vector_id,
    write_release,
)
from build_fulltext_search import search_blob  # noqa: E402
from common import GRAPH, load_json  # noqa: E402

EMBED = load_embed()
TOKENIZER = WordPieceTokenizer(EMBED)


def _node(node_id, title='Title', kind='web', url='https://example.test'):
    return {
        'id': node_id,
        'title': title,
        'authors': ['Ada Lovelace'],
        'section': 'Test',
        'kind': kind,
        'url': url,
    }


def _count_chars(piece: str) -> int:
    return len(piece) + 2


def test_provider_signature_preserves_exact_main_cache_namespace():
    assert embedding_signature(EMBED) == (
        'df5126063ec2f6589a0b994d6b7ebaaed'
        '8767dd49adb742803ab02b8a666cefe'
    )
    changed = deepcopy(EMBED)
    changed['tokenizer']['do_lower_case'] = False
    signature = embedding_signature(EMBED)
    assert embedding_signature(changed) == signature
    assert build_signature(changed) != build_signature(EMBED)
    assert input_hash(changed, 'Keep CASE', signature) == input_hash(
        EMBED, 'Keep CASE', signature,
    )
    assert input_hash(EMBED, 'Keep CASE', signature) != input_hash(
        EMBED, 'keep case', signature,
    )


@pytest.mark.parametrize('key,value', [
    ('model', '@cf/other/model'), ('dimensions', 384),
    ('metric', 'euclidean'), ('pooling', 'mean'),
    ('query_template', 'new query: '), ('passage_template', 'new passage: '),
    ('max_input_tokens', 256),
])
def test_provider_configuration_still_invalidates_embedding_cache(key, value):
    changed = deepcopy(EMBED)
    changed[key] = value
    assert embedding_signature(changed) != embedding_signature(EMBED)


def test_banner_is_only_the_leading_issue_block():
    markdown = (
        '##### Report GitHub Issue\n\n'
        'Content selection saved. Describe the issue below:\n\n'
        '# Kept Title\n\n'
        'Body Stays.\n'
    )
    cleaned = clean_markdown(markdown)
    assert 'Report GitHub Issue' not in cleaned
    assert 'Describe the issue below' not in cleaned
    assert '# Kept Title' in cleaned
    assert 'Body Stays.' in cleaned


def test_pre_heading_note_is_kept_when_there_is_no_banner():
    markdown = 'Note before title\n\n# Title\n'
    assert clean_markdown(markdown).startswith('Note before title')


def test_references_drop_and_numbered_appendix_returns():
    markdown = (
        '# Title\n\nBody stays.\n\n'
        '## References\n\nONLYINREFS\n\n'
        '## 6 Appendix\n\n'
        'variance-covariance matrix of the distance estimate\n'
    )
    cleaned = clean_markdown(markdown)
    assert 'ONLYINREFS' not in cleaned
    assert 'variance-covariance matrix of the distance estimate' in cleaned
    assert 'Body stays.' in cleaned
    assert cleaned != cleaned.lower()


def test_real_appendix_sentence_survives():
    path = (
        Path(__file__).resolve().parents[1]
        / 'filter' / 'fulltext' / 'arxiv_2007.02789.md'
    )
    cleaned = clean_markdown(path.read_text(encoding='utf-8'))
    assert 'variance-covariance matrix of the distance estimate' in cleaned
    assert 'Diedrichsen J, Zareamoghaddam H' not in cleaned


def test_map_search_blob_still_lowercases():
    assert search_blob('Keep CASE\n') == 'keep case'


def test_tokenizer_matches_bert_hello_world():
    ids = TOKENIZER.token_ids('', 'Hello, world!')
    assert ids[0] == TOKENIZER.ids_by_token['[CLS]']
    assert ids[-1] == TOKENIZER.ids_by_token['[SEP]']
    assert ids[1:-1] == [
        TOKENIZER.ids_by_token['hello'],
        TOKENIZER.ids_by_token[','],
        TOKENIZER.ids_by_token['world'],
        TOKENIZER.ids_by_token['!'],
    ]
    assert TOKENIZER.token_ids('', 'Hello') == TOKENIZER.token_ids('', 'hello')


def test_tokenizer_unicode_and_long_word():
    cafe = TOKENIZER.token_ids('', 'café')
    assert cafe[0] == 101 and cafe[-1] == 102
    assert len(TOKENIZER.token_ids('', '中文')) > 2
    assert len(TOKENIZER.token_ids('', 'hi 😀 there')) > 2
    long_ids = TOKENIZER.token_ids('', 'a' * 120)
    assert long_ids == [101, TOKENIZER.ids_by_token['[UNK]'], 102]


def test_chunk_coverage_overlap_and_token_cap():
    text = 'word ' * 500
    ranges = chunk_text(
        text,
        lambda piece: len(TOKENIZER.token_ids('', piece)),
        max_code_points=800,
        overlap=120,
        max_tokens=512,
    )
    assert ranges[0][0] == 0
    assert ranges[-1][1] == len(text)
    for start, end, _count in ranges:
        assert end - start <= 800
        assert len(TOKENIZER.token_ids('', text[start:end])) <= 512
    for (start0, end0, _count0), (start1, end1, _count1) in zip(ranges, ranges[1:]):
        assert start1 > start0
        assert start1 <= end0
        assert end0 - start1 <= 120
    cursor = 0
    for start, end, _count in ranges:
        assert start <= cursor
        cursor = max(cursor, end)
    assert cursor == len(text)


def test_long_paragraph_and_code_point_offsets():
    text = 'x' * 2000
    ranges = chunk_text(
        text,
        _count_chars,
        max_code_points=800,
        overlap=120,
        max_tokens=10_000,
    )
    assert len(ranges) > 1
    assert ranges[-1][1] == 2000
    emoji = 'a😀b'
    assert len(emoji) == 3
    one = chunk_text(
        emoji, _count_chars, max_code_points=800, overlap=120, max_tokens=100,
    )
    assert [(start, end) for start, end, _count in one] == [(0, 3)]


def test_edges_follow_indexes_when_node_order_changes():
    nodes = [
        _node('b', title='B'),
        _node('a', title='A'),
    ]
    release = build_release(
        nodes, [[0, 1, 'id']], {'b': None, 'a': None}, EMBED, progress=False,
    )
    assert release['graph']['out']['b'] == [
        {'target': 'a', 'evidence': 'id'},
    ]
    assert release['graph']['in']['a'][0]['source'] == 'b'


def test_snapshot_edge_zero():
    graph = load_json(GRAPH, {})
    source, target, evidence = graph['edges'][0]
    assert graph['nodes'][source]['id'] == 'arxiv:2608.17163'
    assert graph['nodes'][target]['id'] == 'arxiv:1801.01290'
    assert evidence in {'id', 'title', 'url'}


def test_missing_and_empty_text_are_explicit():
    nodes = [
        _node('web:missing'),
        _node('web:empty'),
    ]
    release = build_release(
        nodes,
        [],
        {'web:missing': None, 'web:empty': '## References\n\nonly refs\n'},
        EMBED,
        progress=False,
    )
    assert release['graph']['nodes']['web:missing']['text'] == {
        'available': False,
        'reason': 'no_markdown',
        'code_points': 0,
        'chunks': 0,
    }
    empty = release['graph']['nodes']['web:empty']['text']
    assert empty['available'] is False
    assert empty['reason'] == 'empty_cleaned'


def test_safe_key_collision_aborts():
    shared = 'url:' + ('a' * 116)
    nodes = [_node(shared), _node(shared + 'tail')]
    with pytest.raises(BuildError, match='safe_key collision'):
        build_release(nodes, [], {shared: None, shared + 'tail': None}, EMBED)


def test_bad_evidence_and_edge_bounds_abort():
    nodes = [_node('a')]
    with pytest.raises(BuildError, match='evidence'):
        build_release(nodes, [[0, 0, 'guess']], {'a': None}, EMBED)
    with pytest.raises(BuildError, match='out of range'):
        build_release(nodes, [[0, 3, 'id']], {'a': None}, EMBED)


def test_release_id_ignores_git_sha_and_is_stable():
    nodes = [_node('arxiv:1')]
    texts = {'arxiv:1': '# Title\n\nHello corpus.\n'}
    first = build_release(
        nodes, [], texts, EMBED, git_sha_value='abc', progress=False,
    )
    second = build_release(
        nodes, [], texts, EMBED, git_sha_value='def', progress=False,
    )
    assert first['release_id'] == second['release_id']
    assert first['manifest']['git_sha'] == 'abc'
    assert second['manifest']['git_sha'] == 'def'
    piece = first['papers']['arxiv:1']['text']
    assert 'Hello corpus.' in piece
    assert piece != piece.lower()


def test_vector_id_is_64_hex_and_depends_on_slot():
    left = vector_id('a', 'x' * 132, 0)
    right = vector_id('b', 'x' * 132, 0)
    assert len(left) == 64
    assert left != right
    assert left.isascii()


def test_capacity_refuses_unknown_or_small_budget_without_trimming():
    nodes = [_node('arxiv:1')]
    release = build_release(
        nodes, [], {'arxiv:1': '# T\n\n' + ('word ' * 40)}, EMBED,
    )
    report = release['report']
    assert report['passages'] >= 1
    assert report['dimensions_with_probe'] == (
        report['passages'] * 768 * 2 + 8 * 768
    )
    with pytest.raises(CapacityError, match='unknown'):
        assert_capacity(report, None)
    with pytest.raises(CapacityError, match='Refusing to shrink'):
        assert_capacity(report, 1)
    assert_capacity(report, report['dimensions_with_probe'])


def test_real_corpus_exceeds_free_vectorize_and_covers_text():
    release = build_from_disk(EMBED, progress=True, git_sha_value='test')
    report = release['report']
    print(
        f"\nreal passages={report['passages']} tokens={report['tokens']} "
        f"dims={report['dimensions_with_probe']} "
        f"usd={report['embedding_usd_upper_bound']:.2f}"
    )
    assert report['fits_documented_free_tier'] is False
    assert report['dimensions_with_probe'] > report['documented_free_dimensions']
    assert report['papers_without_text'] == report['reasons']['no_markdown']
    paper = release['papers']['arxiv:2007.02789']
    assert 'variance-covariance matrix of the distance estimate' in paper['text']
    banner = release['papers'].get('arxiv:2503.14858')
    if banner:
        assert 'Describe the issue below' not in banner['text']
        assert banner['text'] != banner['text'].lower()
    for passage in release['passages']:
        assert passage['token_count'] <= 512
        paper_text = release['papers'][passage['paper_id']]['text']
        piece = paper_text[passage['start']:passage['end']]
        assert 0 <= passage['start'] < passage['end'] <= len(paper_text)
        assert len(piece) <= 800


def test_fixture_file_matches_tokenizer():
    path = (
        Path(__file__).resolve().parents[1]
        / 'worker' / 'fixtures' / 'token_ids.json'
    )
    if not path.is_file():
        pytest.skip('token fixture is written by --emit-token-fixtures')
    rows = json.loads(path.read_text(encoding='utf-8'))
    for row in rows:
        assert TOKENIZER.token_ids(row['template'], row['text']) == row['ids']


def test_written_release_round_trips(tmp_path):
    release = build_release(
        [_node('arxiv:1')], [], {'arxiv:1': '# T\n\nHello.\n'}, EMBED,
    )
    write_release(release, tmp_path)
    loaded = load_written_release(tmp_path)
    assert loaded['release_id'] == release['release_id']
    assert loaded['papers']['arxiv:1']['text'] == release['papers']['arxiv:1']['text']
    assert loaded['report']['fits_documented_free_tier'] is True


def test_discovery_refuses_to_invent_an_origin(tmp_path):
    from write_discovery_links import (
        main, update_html, update_readme, valid_origin, worker_origin,
    )
    assert valid_origin('https://key-papers-api.example.workers.dev')
    assert not valid_origin('https://evil.example')
    assert not valid_origin('http://key-papers-api.example.workers.dev')
    log = (
        'Deployed https://other.workers.dev and '
        'https://key-papers-api.account.workers.dev\n'
        'also https://key-papers-api.a.b.workers.dev/ignored'
    )
    assert worker_origin(log, 'key-papers-api') == (
        'https://key-papers-api.account.workers.dev'
    )
    assert worker_origin('https://evil.example', 'key-papers-api') == ''
    html = '<h1>Map</h1>\n'
    readme = 'See (https://vinnik-dmitry07.github.io/favorite-papers/) locally.\n'
    origin = 'https://key-papers-api.example.workers.dev'
    assert 'id="agent-api"' in update_html(html, origin)
    assert origin in update_readme(readme, origin)
    html_path = tmp_path / 'index.html'
    readme_path = tmp_path / 'readme.md'
    html_path.write_text(html, encoding='utf-8')
    readme_path.write_text(readme, encoding='utf-8')
    smoke = tmp_path / 'smoke.json'
    smoke.write_text(
        '{"ok": false, "origin": "https://evil.example"}\n', encoding='utf-8',
    )
    flags = [
        '--smoke', str(smoke),
        '--html', str(html_path),
        '--readme', str(readme_path),
    ]
    assert main(flags) == 0
    assert html_path.read_text(encoding='utf-8') == html
    assert 'agent-api' not in readme_path.read_text(encoding='utf-8')
    smoke.write_text(json.dumps({'ok': True, 'origin': origin}), encoding='utf-8')
    assert main(flags) == 0
    written = readme_path.read_text(encoding='utf-8')
    assert written.count('Agent API:') == 1
    assert origin in written
    assert origin in html_path.read_text(encoding='utf-8')
    assert update_readme(written, origin).count('Agent API:') == 1
