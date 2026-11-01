'''Failure and resume checks for the slot publisher. No Cloudflare calls.'''

from __future__ import annotations

from copy import deepcopy
import sys
from pathlib import Path

import pytest

SRC = Path(__file__).resolve().parent
sys.path.insert(0, str(SRC))

from build_agent_index import (  # noqa: E402
    WordPieceTokenizer,
    build_release,
    embedding_signature,
    load_embed,
    vector_id,
)
from publish_agent_index import (  # noqa: E402
    ACTIVE_KEY,
    CloudflareCloud,
    FatalError,
    GET_IDS_BATCH,
    MemoryCloud,
    ProbeError,
    PublishError,
    Publisher,
    run_probe,
    slot_confirmed_key,
)

EMBED = load_embed()


def _node(node_id: str) -> dict:
    return {
        'id': node_id,
        'title': node_id,
        'authors': ['Ada Lovelace'],
        'section': 'Test',
        'kind': 'arxiv',
        'url': 'https://example.test/' + node_id,
    }


def make_release(texts: dict[str, str]):
    nodes = [_node(node_id) for node_id in texts]
    return build_release(nodes, [], texts, EMBED, progress=False)


def start(hooks=None):
    cloud = MemoryCloud(EMBED)
    return Publisher(cloud, EMBED, hooks), cloud


def test_second_publish_of_the_active_release_does_not_embed():
    publisher, cloud = start()
    release = make_release({'arxiv:1': '# T\n\nHello corpus.\n'})
    publisher.publish(release, 'a')
    calls = cloud.embed_calls
    result = publisher.publish(release, 'a')
    assert result['status'] == 'noop'
    assert result['promoted'] is True
    assert cloud.embed_calls == calls


def test_unchanged_passage_keeps_its_vector_without_a_release_stamp():
    publisher, cloud = start()
    original = '# T\n\n' + ('alpha ' * 40)
    changed = '# T\n\n' + ('beta ' * 40)
    first = make_release({'p-a': original, 'p-b': original})
    publisher.publish(first, 'a', promote=False)
    calls = cloud.embed_calls
    upserts = cloud.upsert_calls
    second = make_release({'p-a': original, 'p-b': changed})
    publisher.publish(second, 'a', promote=False)
    assert cloud.embed_calls == calls + 1
    assert cloud.upsert_calls == upserts + 1
    confirmed = cloud.get_json(slot_confirmed_key('a'))
    kept = vector_id('a', 'p-a', 0)
    assert kept in confirmed['vectors']
    assert 'corpus_version' not in confirmed['vectors'][kept]
    assert 'corpus_version' not in cloud.vectors[kept]['metadata']
    assert confirmed['release_id'] == second['release_id']


@pytest.mark.parametrize('target_slot', ['a', 'b'])
def test_tokenizer_only_release_reuses_provider_vectors_and_cache(target_slot):
    previous_config = deepcopy(EMBED)
    # Before literal-special-token support these characters were ordinary
    # input text. Both releases send the exact same text to Workers AI.
    previous_config['tokenizer']['added_tokens'] = [
        row for row in previous_config['tokenizer']['added_tokens']
        if row['content'] not in {'[PAD]', '[MASK]'}
    ]
    texts = {'arxiv:1': '# Title\nUse the [MASK] model for this experiment.'}
    nodes = [_node(key) for key in texts]
    previous = build_release(nodes, [], texts, previous_config)
    current = build_release(nodes, [], texts, EMBED)
    assert previous['build_signature'] != current['build_signature']
    assert previous['embedding_signature'] == current['embedding_signature']
    assert previous['report']['tokens'] != current['report']['tokens']
    assert previous['passages'][0]['input_hash'] == (
        current['passages'][0]['input_hash']
    )
    cloud = MemoryCloud(previous_config)
    Publisher(cloud, previous_config).publish(previous, 'a', promote=False)
    calls, upserts = cloud.embed_calls, cloud.upsert_calls
    Publisher(cloud, EMBED).publish(current, target_slot, promote=False)
    assert cloud.embed_calls == calls
    if target_slot == 'a':
        assert cloud.upsert_calls == upserts
    else:
        assert cloud.upsert_calls > upserts
    assert cloud.get_json(slot_confirmed_key(target_slot))[
        'build_signature'
    ] == current['build_signature']


@pytest.mark.parametrize('changed', ['text', 'model'])
def test_provider_migration_does_not_reuse_changed_inputs(changed):
    texts = {'arxiv:1': '# Title\nOriginal input to the embedding model.'}
    nodes = [_node(key) for key in texts]
    cloud = MemoryCloud(EMBED)
    previous = build_release(nodes, [], texts, EMBED)
    Publisher(cloud, EMBED).publish(previous, 'a', promote=False)
    calls = cloud.embed_calls
    config = deepcopy(EMBED)
    if changed == 'text':
        texts['arxiv:1'] += '\nChanged source sentence.'
    else:
        config['model'] += '-next-revision'
        assert embedding_signature(config) != embedding_signature(EMBED)
    current = build_release(nodes, [], texts, config)
    Publisher(cloud, config).publish(current, 'a', promote=False)
    assert cloud.embed_calls > calls


def test_shorten_and_delete_remove_only_stale_slot_ids():
    publisher, cloud = start()
    long_text = '# T\n\n' + ('word ' * 400)
    first = make_release({'p': long_text, 'q': '# T\n\nkeep me\n'})
    assert first['manifest']['passage_count'] > 2
    publisher.publish(first, 'a', promote=False)
    old_p = [
        vector_id('a', 'p', index)
        for index in range(len(first['papers']['p']['chunks']))
    ]
    assert len(old_p) > 1
    second = make_release({'p': '# T\n\nshort\n', 'q': '# T\n\nkeep me\n'})
    publisher.publish(second, 'a', promote=False)
    assert old_p[0] in cloud.vectors or vector_id('a', 'p', 0) in cloud.vectors
    for stale in old_p[1:]:
        assert stale not in cloud.vectors
    third = make_release({'q': '# T\n\nkeep me\n'})
    publisher.publish(third, 'a', promote=False)
    assert vector_id('a', 'p', 0) not in cloud.vectors
    assert vector_id('a', 'q', 0) in cloud.vectors


def test_crash_before_cache_embeds_again_and_after_cache_does_not():
    release = make_release({'arxiv:1': '# T\n\nHello corpus.\n'})

    def crash():
        raise RuntimeError('stopped')

    publisher, cloud = start({'after_embed_received': crash})
    with pytest.raises(RuntimeError):
        publisher.publish(release, 'a')
    calls = cloud.embed_calls
    Publisher(cloud, EMBED).publish(release, 'a')
    assert cloud.embed_calls > calls

    publisher, cloud = start({'after_cache': crash})
    with pytest.raises(RuntimeError):
        publisher.publish(release, 'a')
    calls = cloud.embed_calls
    Publisher(cloud, EMBED).publish(release, 'a')
    assert cloud.embed_calls == calls
    assert cloud.get_json(ACTIVE_KEY)['release_id'] == release['release_id']


def test_unknown_upsert_replays_same_ids():
    publisher, cloud = start()
    release = make_release({'arxiv:1': '# T\n\nHello corpus.\n'})
    cloud.unknown_upserts = 1
    waiting = publisher.publish(release, 'a')
    assert waiting['status'] == 'waiting'
    assert waiting['promoted'] is False
    assert cloud.get_json(ACTIVE_KEY) is None
    upserts = cloud.upsert_calls
    done = publisher.publish(release, 'a')
    assert done['promoted'] is True
    assert cloud.upsert_calls > upserts


def test_queued_mutation_does_not_promote_until_visible():
    publisher, cloud = start()
    release = make_release({'arxiv:1': '# T\n\nHello corpus.\n'})
    cloud.hold = True
    waiting = publisher.publish(release, 'a')
    assert waiting['status'] == 'waiting'
    assert cloud.get_json(ACTIVE_KEY) is None
    calls = cloud.embed_calls
    cloud.hold = False
    cloud.complete_all()
    done = publisher.publish(release, 'a')
    assert done['promoted'] is True
    assert cloud.embed_calls == calls


def test_quota_pauses_and_leaves_the_active_release():
    publisher, cloud = start()
    cloud.quota = True
    release = make_release({'arxiv:1': '# T\n\nHello corpus.\n'})
    paused = publisher.publish(release, 'a')
    assert paused['status'] == 'paused_quota'
    assert cloud.get_json(ACTIVE_KEY) is None
    cloud.quota = False
    assert publisher.publish(release, 'a')['promoted'] is True


def test_new_run_deletes_orphan_ids_from_an_old_journal():
    publisher, cloud = start()
    release = make_release({'arxiv:1': '# T\n\nHello corpus.\n'})
    cloud.put_json('slots/a/journal.json', {
        'run_id': 'old-run',
        'release_id': 'different-release',
        'embedding_signature': release['embedding_signature'],
        'build_signature': release['build_signature'],
        'slot': 'a',
        'base_active_release': None,
        'status': 'waiting',
        'batches': [{
            'vector_ids': ['orphan-id'],
            'status': 'unknown',
            'mutation_id': 'old',
        }],
        'deletes': [],
    })
    cloud.vectors['orphan-id'] = {
        'id': 'orphan-id',
        'namespace': 'a',
        'values': [0.0] * EMBED['dimensions'],
        'metadata': {},
    }
    publisher.publish(release, 'a')
    assert 'orphan-id' not in cloud.vectors
    assert cloud.get_json('slots/a/journals/old-run.json')['release_id'] == (
        'different-release'
    )


def test_grace_rollback_and_blocked_reuse():
    publisher, cloud = start()
    first = make_release({'arxiv:1': '# T\n\nFirst release.\n'})
    second = make_release({'arxiv:1': '# T\n\nSecond release.\n'})
    publisher.publish(first, 'a')
    publisher.publish(second, 'b')
    with pytest.raises(PublishError) as caught:
        publisher.publish(first, 'a')
    assert caught.value.code == 'grace'
    rolled = publisher.rollback()
    assert rolled['slot'] == 'a'
    assert rolled['release_id'] == first['release_id']
    cloud.now = EMBED['limits']['grace_seconds']
    publisher.publish(second, 'b')
    cloud.now = EMBED['limits']['grace_seconds'] * 2
    seen = {}

    def during_staging():
        with pytest.raises(PublishError) as blocked:
            publisher.rollback()
        seen['code'] = blocked.value.code

    staged = Publisher(cloud, EMBED, {'after_staging': during_staging})
    third = make_release({'arxiv:1': '# T\n\nThird release.\n'})
    staged.publish(third, 'a')
    assert seen['code'] == 'rollback_unavailable'
    assert cloud.get_json(f'releases/{first["release_id"]}/graph.json')


def test_newer_active_release_blocks_promotion():
    publisher, cloud = start()
    first = make_release({'arxiv:1': '# T\n\nFirst release.\n'})
    second = make_release({'arxiv:1': '# T\n\nSecond release.\n'})
    publisher.publish(first, 'a')
    publisher.publish(second, 'b')
    cloud.now = 120

    def replace_active():
        cloud.put_json(ACTIVE_KEY, {
            'release_id': 'newer-release',
            'slot': 'b',
            'embedding_signature': second['embedding_signature'],
            'build_signature': second['build_signature'],
        })

    third = make_release({'arxiv:1': '# T\n\nThird release.\n'})
    result = Publisher(cloud, EMBED, {'after_ready': replace_active}).publish(
        third, 'a',
    )
    assert result['status'] == 'stale_base'
    assert result['promoted'] is False
    assert cloud.get_json(ACTIVE_KEY)['release_id'] == 'newer-release'


def test_reader_mismatch_does_not_promote():
    publisher, cloud = start()
    cloud.reader_schema = 99
    release = make_release({'arxiv:1': '# T\n\nHello corpus.\n'})
    result = publisher.publish(release, 'a')
    assert result['status'] == 'reader_incompatible'
    assert cloud.get_json(ACTIVE_KEY) is None


def test_retryable_embed_succeeds_inside_the_attempt_budget():
    publisher, cloud = start()
    cloud.retry_embeds = 1
    release = make_release({'arxiv:1': '# T\n\nHello corpus.\n'})
    assert publisher.publish(release, 'a')['promoted'] is True
    assert cloud.embed_calls == 2


def test_probe_is_confined_to_its_namespace():
    publisher, cloud = start()
    release = make_release({'arxiv:1': '# T\n\nHello corpus.\n'})
    publisher.publish(release, 'a')
    report = run_probe(cloud, EMBED, WordPieceTokenizer(EMBED))
    assert report['ok'] is True
    assert cloud.get_json(ACTIVE_KEY)['release_id'] == release['release_id']
    assert vector_id('a', 'arxiv:1', 0) in cloud.vectors
    assert vector_id('probe', 'x' * 132, 0) not in cloud.vectors
    cloud.hold = True
    with pytest.raises(ProbeError, match='not visible'):
        run_probe(cloud, EMBED, WordPieceTokenizer(EMBED))


def test_slot_ids_differ_for_the_same_passage():
    assert vector_id('a', 'arxiv:1', 0) != vector_id('b', 'arxiv:1', 0)
    assert len(vector_id('a', 'x' * 132, 3)) == 64


def test_inactive_slot_follows_the_pointer():
    from publish_agent_index import inactive_slot
    _, cloud = start()
    assert inactive_slot(cloud) == 'a'
    cloud.put_json(ACTIVE_KEY, {'slot': 'a', 'release_id': 'r'})
    assert inactive_slot(cloud) == 'b'
    cloud.put_json(ACTIVE_KEY, {'slot': 'b', 'release_id': 'r'})
    assert inactive_slot(cloud) == 'a'


class RecordingCloud(CloudflareCloud):
    '''Captures Vectorize HTTP calls. Does not open a socket.'''

    def __init__(self):
        self.embed = EMBED
        self.account_id = 'acct'
        self.token = 'token'
        self.calls = []

    def _request(self, method, url, payload=None, *, body=None, content_type=None):
        self.calls.append({
            'method': method,
            'url': url,
            'payload': payload,
            'body': body,
            'content_type': content_type,
        })
        if url.endswith('/upsert') or url.endswith('/delete_by_ids'):
            return {'success': True, 'result': {'mutationId': 'mut-1'}}
        if url.endswith('/info'):
            return {
                'success': True,
                'result': {'processedUpToMutation': 'mut-1'},
            }
        if url.endswith('/get_by_ids'):
            return {
                'success': True,
                'result': [
                    {
                        'id': item,
                        'namespace': 'a',
                        'values': [0.1],
                        'metadata': {},
                    }
                    for item in payload['ids']
                ],
            }
        return {'success': True, 'result': {}}


def test_live_upsert_is_ndjson_and_get_by_ids_reads_a_list():
    cloud = RecordingCloud()
    cloud.upsert([{
        'id': 'one',
        'values': [0.25],
        'namespace': 'a',
        'metadata': {'paper_id': 'arxiv:1'},
    }])
    upsert = cloud.calls[0]
    assert upsert['content_type'] == 'application/x-ndjson'
    assert upsert['body'] == (
        b'{"id":"one","metadata":{"paper_id":"arxiv:1"},'
        b'"namespace":"a","values":[0.25]}\n'
    )
    ids = [f'id-{index}' for index in range(GET_IDS_BATCH + 1)]
    found = cloud.get_vectors(ids)
    pages = [call for call in cloud.calls if call['url'].endswith('/get_by_ids')]
    assert [len(call['payload']['ids']) for call in pages] == [GET_IDS_BATCH, 1]
    assert set(found) == set(ids)
    assert found['id-0']['namespace'] == 'a'


def test_get_by_ids_object_is_fatal():
    cloud = RecordingCloud()

    def object_result(method, url, payload=None, *, body=None, content_type=None):
        return {'success': True, 'result': {'vectors': [{'id': 'x'}]}}

    cloud._request = object_result
    with pytest.raises(FatalError, match='not a list'):
        cloud.get_vectors(['x'])


def test_delete_crash_replays_the_same_ids():
    publisher, cloud = start()
    long_text = '# T\n\n' + ('word ' * 400)
    first = make_release({'p': long_text})
    publisher.publish(first, 'a', promote=False)
    second = make_release({'p': '# T\n\nshort\n'})
    first_ids = {
        vector_id('a', 'p', index)
        for index in range(len(first['papers']['p']['chunks']))
    }
    second_ids = {
        vector_id('a', 'p', index)
        for index in range(len(second['papers']['p']['chunks']))
    }
    stale = sorted(first_ids - second_ids)
    assert stale
    cloud.fail_deletes = 1
    with pytest.raises(RuntimeError, match='stopped'):
        publisher.publish(second, 'a', promote=False)
    journal = cloud.get_json('slots/a/journal.json')
    assert journal['deletes'][-1]['status'] == 'sending'
    assert journal['deletes'][-1]['mutation_id'] is None
    assert journal['deletes'][-1]['vector_ids'] == stale
    calls = cloud.delete_calls
    publisher.publish(second, 'a', promote=False)
    assert cloud.delete_calls == calls + 1
    for item in stale:
        assert item not in cloud.vectors


def test_changed_embedding_signature_reembeds_and_deletes_orphans():
    publisher, cloud = start()
    release = make_release({'arxiv:1': '# T\n\nHello corpus.\n'})
    publisher.publish(release, 'a', promote=False)
    calls = cloud.embed_calls
    confirmed = cloud.get_json(slot_confirmed_key('a'))
    confirmed['embedding_signature'] = 'other-signature'
    confirmed['vectors']['orphan-vector'] = {
        'content_hash': 'x',
        'input_hash': 'y',
        'chunk_index': 0,
    }
    cloud.put_json(slot_confirmed_key('a'), confirmed)
    cloud.vectors['orphan-vector'] = {
        'id': 'orphan-vector',
        'namespace': 'a',
        'values': [0.0] * EMBED['dimensions'],
        'metadata': {},
    }
    for key in list(cloud.objects):
        if str(key).startswith('cache/emb/'):
            del cloud.objects[key]
    rewritten = dict(release)
    rewritten['release_id'] = release['release_id'] + 'b'
    again = publisher.publish(rewritten, 'a', promote=False)
    assert again['status'] == 'staged'
    assert cloud.embed_calls == calls + 1
    assert 'orphan-vector' not in cloud.vectors
    assert vector_id('a', 'arxiv:1', 0) in cloud.vectors
