'''Publish a built release into R2 and Vectorize.

The active pointer changes only after the inactive slot is visible. Local
calls may probe and dry-run. Production promotion is the CI writer.
'''

from __future__ import annotations

import json
import math
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import quote

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_agent_index import (  # noqa: E402
    DEFAULT_OUT,
    SLOTS,
    WordPieceTokenizer,
    assert_capacity,
    canonical_json,
    embedding_signature,
    load_embed,
    load_written_release,
    model_input,
    sha256_hex,
    vector_id,
)

ACTIVE_KEY = 'active.json'
PROBE_SLOT = 'probe'
UNCONFIRMED = {'sending', 'unknown', 'accepted'}
GET_IDS_BATCH = 100
DELETE_IDS_BATCH = 1000
MUTATION_WAIT_SECONDS = 120


def serving_object(key: str) -> bool:
    return (
        key == ACTIVE_KEY
        or key.startswith('slots/a')
        or key.startswith('slots/b')
    )


class PublishError(Exception):
    def __init__(self, code: str, message: str):
        super().__init__(message)
        self.code = code


class RetryableError(PublishError):
    def __init__(self, message: str, retry_after: float = 0):
        super().__init__('retryable', message)
        self.retry_after = retry_after


class FatalError(PublishError):
    def __init__(self, message: str, status: int | None = None):
        super().__init__('fatal', message)
        self.status = status


class QuotaError(PublishError):
    def __init__(self, message: str):
        super().__init__('paused_quota', message)


class UnknownWrite(PublishError):
    def __init__(self, mutation_id: str):
        super().__init__('unknown_write', mutation_id)
        self.mutation_id = mutation_id


class ProbeError(PublishError):
    def __init__(self, message: str):
        super().__init__('probe_failed', message)


def slot_status_key(slot: str) -> str:
    return f'slots/{slot}/status.json'


def slot_confirmed_key(slot: str) -> str:
    return f'slots/{slot}/confirmed.json'


def journal_key(slot: str) -> str:
    return f'slots/{slot}/journal.json'


def cache_object_key(digest: str) -> str:
    return f'cache/emb/{digest}.json'


def fake_embed(text: str, dimensions: int) -> list[float]:
    '''Bag-of-words vector so probe distractors are separable offline.'''
    vector = [0.0] * dimensions
    for token in text.lower().split():
        digest = sha256_hex(token)
        bucket = int(digest[:8], 16) % dimensions
        sign = 1.0 if int(digest[8:10], 16) % 2 == 0 else -1.0
        vector[bucket] += sign
    norm = math.sqrt(sum(value * value for value in vector)) or 1.0
    return [value / norm for value in vector]


def _cosine(left: list[float], right: list[float]) -> float:
    return sum(a * b for a, b in zip(left, right))


class MemoryCloud:
    '''In-memory R2 and Vectorize. Tests drive faults and visibility.'''

    def __init__(self, embed: dict):
        self.embed_config = embed
        self.objects: dict[str, object] = {}
        self.vectors: dict[str, dict] = {}
        self.pending: dict[str, list] = {}
        self.mutations: dict[str, str] = {}
        self.hold = False
        self.embed_calls = 0
        self.upsert_calls = 0
        self.delete_calls = 0
        self.poolings: list[str] = []
        self.reader_schema = embed['reader_schema']
        self.dimension_budget = 10 ** 12
        self.permissions_ok = True
        self.index_dimensions = embed['dimensions']
        self.index_metric = embed['metric']
        self.now = 0.0
        self.unknown_upserts = 0
        self.retry_embeds = 0
        self.quota = False
        self.fail_deletes = 0
        self._mutation_serial = 0

    def clock(self) -> float:
        return self.now

    def sleep(self, seconds: float) -> None:
        self.now += seconds

    def put_json(self, key: str, payload) -> None:
        self.objects[key] = json.loads(canonical_json(payload))

    def get_json(self, key: str):
        value = self.objects.get(key)
        if value is None:
            return None
        return json.loads(canonical_json(value))

    def check_permissions(self) -> None:
        if not self.permissions_ok:
            raise FatalError('cloudflare token cannot read Vectorize or R2')
        if self.index_dimensions != self.embed_config['dimensions']:
            raise FatalError('index dimensions do not match embed.json')
        if self.index_metric != self.embed_config['metric']:
            raise FatalError('index metric does not match embed.json')

    def embed(self, texts: list[str], pooling: str) -> list[list[float]]:
        self.embed_calls += 1
        self.poolings.append(pooling)
        if pooling != self.embed_config['pooling']:
            raise FatalError('pooling does not match embed.json')
        if self.quota:
            raise QuotaError('workers ai neuron quota')
        if self.retry_embeds:
            self.retry_embeds -= 1
            raise RetryableError('429', retry_after=0)
        dimensions = self.embed_config['dimensions']
        return [fake_embed(text, dimensions) for text in texts]

    def upsert(self, vectors: list[dict]) -> str:
        self.upsert_calls += 1
        self._mutation_serial += 1
        mutation_id = f'up-{self._mutation_serial}'
        self.pending[mutation_id] = vectors
        self.mutations[mutation_id] = 'queued'
        if self.unknown_upserts:
            self.unknown_upserts -= 1
            if not self.hold:
                self._apply(mutation_id)
            raise UnknownWrite(mutation_id)
        if not self.hold:
            self._apply(mutation_id)
        return mutation_id

    def delete_ids(self, ids: list[str]) -> str:
        self.delete_calls += 1
        if self.fail_deletes:
            self.fail_deletes -= 1
            raise RuntimeError('stopped')
        self._mutation_serial += 1
        mutation_id = f'del-{self._mutation_serial}'
        self.pending[mutation_id] = [{'id': item, 'delete': True} for item in ids]
        self.mutations[mutation_id] = 'queued'
        if not self.hold:
            self._apply(mutation_id)
        return mutation_id

    def mutation_status(self, mutation_id: str) -> str:
        return self.mutations.get(mutation_id, 'unknown')

    def complete_all(self) -> None:
        if self.hold:
            return
        for mutation_id, status in list(self.mutations.items()):
            if status == 'queued':
                self._apply(mutation_id)

    def _apply(self, mutation_id: str) -> None:
        for item in self.pending.get(mutation_id, []):
            if item.get('delete'):
                self.vectors.pop(item['id'], None)
            else:
                self.vectors[item['id']] = item
        self.mutations[mutation_id] = 'complete'

    def get_vectors(self, ids: list[str]) -> dict[str, dict]:
        return {
            item_id: self.vectors[item_id]
            for item_id in ids
            if item_id in self.vectors
        }

    def query(self, namespace: str, vector: list[float], top_k: int) -> list[dict]:
        scored = []
        for item in self.vectors.values():
            if item.get('namespace') != namespace:
                continue
            scored.append({
                'id': item['id'],
                'score': _cosine(vector, item['values']),
                'metadata': item.get('metadata') or {},
            })
        scored.sort(key=lambda row: (-row['score'], row['id']))
        return scored[:top_k]


def _call_with_retry(cloud, fn):
    last = None
    for _attempt in range(5):
        try:
            return fn()
        except RetryableError as exc:
            last = exc
            delay = exc.retry_after or min(2 ** _attempt, 30)
            cloud.sleep(delay)
    raise last


class Publisher:
    def __init__(self, cloud, embed: dict, hooks: dict | None = None):
        self.cloud = cloud
        self.embed = embed
        self.hooks = hooks or {}
        self.grace = float(embed['limits']['grace_seconds'])
        self.batch_size = 32

    def _hook(self, name: str) -> None:
        hook = self.hooks.get(name)
        if hook:
            hook()

    def publish(
        self,
        release: dict,
        slot: str,
        *,
        promote: bool = True,
        source_sha: str | None = None,
    ) -> dict:
        if slot not in SLOTS:
            raise PublishError('bad_slot', 'serving slots are a and b')
        if (
            self._active_slot() == slot
            and self._active_release() == release['release_id']
        ):
            return self._result('noop', release, slot, promoted=True)
        self._reject_active_target(slot)
        self._reject_grace(slot)
        journal = self._open_journal(release, slot, source_sha)
        if (
            journal.get('status') == 'promoted'
            and self._active_release() == release['release_id']
            and self._active_slot() == slot
        ):
            return self._result('noop', release, slot, promoted=True)
        self._mark_staging(slot)
        self._upload_release(release)
        try:
            self._sync_vectors(release, slot, journal)
        except QuotaError as exc:
            journal['status'] = 'paused_quota'
            self._save_journal(slot, journal)
            return self._result('paused_quota', release, slot, promoted=False, detail=str(exc))
        if journal['status'] != 'ready':
            return self._result(journal['status'], release, slot, promoted=False)
        if not promote:
            return self._result('staged', release, slot, promoted=False)
        if not self._reader_ok(release):
            return self._result('reader_incompatible', release, slot, promoted=False)
        if not self._base_still_current(journal):
            return self._result('stale_base', release, slot, promoted=False)
        self._hook('before_pointer')
        self._activate(release, slot)
        journal['status'] = 'promoted'
        self._save_journal(slot, journal)
        self._hook('after_pointer')
        return self._result('promoted', release, slot, promoted=True)

    def rollback(self) -> dict:
        active = self.cloud.get_json(ACTIVE_KEY)
        if not active:
            raise PublishError('no_active', 'there is no active release')
        previous = 'b' if active['slot'] == 'a' else 'a'
        status = self.cloud.get_json(slot_status_key(previous)) or {}
        if status.get('state') != 'ready' or status.get('rollback_blocked'):
            raise PublishError(
                'rollback_unavailable',
                'the previous slot must be republished from its stored release',
            )
        self._leave_slot(active['slot'])
        pointer = {
            'release_id': status['release_id'],
            'slot': previous,
            'activated_at': self.cloud.clock(),
            'reader_schema': self.embed['reader_schema'],
            'embedding_signature': status['embedding_signature'],
            'build_signature': status['build_signature'],
            'verified_passage_count': status['verified_passage_count'],
            'global_index_count': active.get('global_index_count'),
            'publication_check': {
                'ok': True,
                'checked_at': self.cloud.clock(),
                'by': 'rollback',
            },
        }
        self.cloud.put_json(ACTIVE_KEY, pointer)
        return pointer

    def _result(self, status, release, slot, *, promoted, detail=None) -> dict:
        return {
            'status': status,
            'release_id': release['release_id'],
            'slot': slot,
            'promoted': promoted,
            'embed_calls': self.cloud.embed_calls,
            'detail': detail,
        }

    def _reject_active_target(self, slot: str) -> None:
        if self._active_slot() == slot:
            raise PublishError('active_target', f'slot {slot} is active')

    def _reject_grace(self, slot: str) -> None:
        status = self.cloud.get_json(slot_status_key(slot)) or {}
        deactivated = status.get('deactivated_at')
        if deactivated is None:
            return
        if self.cloud.clock() - deactivated < self.grace:
            raise PublishError('grace', f'slot {slot} is inside the grace window')

    def _open_journal(self, release: dict, slot: str, source_sha: str | None) -> dict:
        current = self.cloud.get_json(journal_key(slot))
        same = (
            current
            and current.get('release_id') == release['release_id']
            and current.get('embedding_signature') == release['embedding_signature']
            and current.get('build_signature') == release['build_signature']
        )
        if same:
            return current
        if current:
            self._archive_journal(slot, current)
        journal = {
            'run_id': sha256_hex(canonical_json([
                slot, release['release_id'], source_sha,
            ]))[:16],
            'release_id': release['release_id'],
            'embedding_signature': release['embedding_signature'],
            'build_signature': release['build_signature'],
            'slot': slot,
            'source_sha': source_sha,
            'base_active_release': self._active_release(),
            'status': 'staging',
            'batches': [],
            'deletes': [],
        }
        self._save_journal(slot, journal)
        return journal

    def _archive_journal(self, slot: str, journal: dict) -> None:
        dirty = []
        for batch in journal.get('batches', []):
            if batch.get('status') in UNCONFIRMED:
                dirty.extend(batch.get('vector_ids') or [])
        for batch in journal.get('deletes', []):
            if batch.get('status') in UNCONFIRMED:
                dirty.extend(batch.get('vector_ids') or [])
        status = self.cloud.get_json(slot_status_key(slot)) or {}
        status['dirty_ids'] = sorted(set(status.get('dirty_ids') or []) | set(dirty))
        self.cloud.put_json(slot_status_key(slot), status)
        run_id = journal.get('run_id') or 'archived'
        self.cloud.put_json(f'slots/{slot}/journals/{run_id}.json', journal)

    def _mark_staging(self, slot: str) -> None:
        '''Drop rollback for this slot before any vector mutation.'''
        status = self.cloud.get_json(slot_status_key(slot)) or {}
        status['state'] = 'staging'
        status['rollback_blocked'] = True
        status['rollback_release_id'] = None
        self.cloud.put_json(slot_status_key(slot), status)
        self._hook('after_staging')

    def _upload_release(self, release: dict) -> None:
        release_id = release['release_id']
        self.cloud.put_json(f'releases/{release_id}/graph.json', release['graph'])
        self.cloud.put_json(
            f'releases/{release_id}/manifest.json', release['manifest'],
        )
        for paper_id, paper in release['papers'].items():
            name = sha256_hex(paper_id)
            self.cloud.put_json(
                f'releases/{release_id}/papers/{name}.json', paper,
            )

    def _sync_vectors(self, release: dict, slot: str, journal: dict) -> None:
        if journal.get('status') != 'paused_quota':
            journal['status'] = 'staging'
        desired = self._desired(release, slot)
        desired_ids = {item['id'] for item in desired}
        confirmed = self._confirmed_map(slot)
        dirty = set((self.cloud.get_json(slot_status_key(slot)) or {}).get('dirty_ids') or [])
        for batch in journal.get('batches', []):
            if batch.get('status') in UNCONFIRMED:
                dirty.update(batch.get('vector_ids') or [])
        known = set(confirmed) | dirty
        stale = sorted(known - desired_ids)
        pending = []
        for item in desired:
            previous = confirmed.get(item['id'])
            if (
                previous
                and previous.get('content_hash') == item['metadata']['content_hash']
                and previous.get('input_hash') == item['metadata']['input_hash']
                and item['id'] not in dirty
            ):
                continue
            pending.append(item)
        self._upsert_pending(pending, journal, slot)
        if journal.get('status') == 'waiting':
            self._save_journal(slot, journal)
            return
        self._delete_ids(stale, journal, slot)
        if journal.get('status') == 'waiting':
            self._save_journal(slot, journal)
            return
        if not self._visible(journal, desired_ids, stale):
            journal['status'] = 'waiting'
            self._save_journal(slot, journal)
            return
        vectors = {}
        for item in desired:
            meta = dict(item['metadata'])
            vectors[item['id']] = meta
        confirmed_doc = {
            'release_id': release['release_id'],
            'embedding_signature': release['embedding_signature'],
            'build_signature': release['build_signature'],
            'passage_count': len(desired),
            'vectors': vectors,
        }
        self.cloud.put_json(slot_confirmed_key(slot), confirmed_doc)
        status = self.cloud.get_json(slot_status_key(slot)) or {}
        status.update({
            'state': 'ready',
            'release_id': release['release_id'],
            'embedding_signature': release['embedding_signature'],
            'build_signature': release['build_signature'],
            'verified_passage_count': len(desired),
            'dirty_ids': [],
            'rollback_blocked': True,
        })
        self.cloud.put_json(slot_status_key(slot), status)
        journal['status'] = 'ready'
        for batch in journal['batches']:
            if batch['status'] in UNCONFIRMED:
                batch['status'] = 'confirmed'
        for batch in journal['deletes']:
            if batch['status'] in UNCONFIRMED:
                batch['status'] = 'confirmed'
        self._save_journal(slot, journal)
        self._hook('after_ready')

    def _desired(self, release: dict, slot: str) -> list[dict]:
        papers = release['papers']
        rows = []
        for passage in release['passages']:
            paper = papers[passage['paper_id']]
            piece = paper['text'][passage['start']:passage['end']]
            rows.append({
                'id': vector_id(slot, passage['paper_id'], passage['chunk_index']),
                'namespace': slot,
                'input': model_input(self.embed['passage_template'], piece),
                'input_hash': passage['input_hash'],
                'metadata': {
                    'paper_id': passage['paper_id'],
                    'chunk_index': passage['chunk_index'],
                    'content_hash': passage['content_hash'],
                    'input_hash': passage['input_hash'],
                },
            })
        return rows

    def _confirmed_map(self, slot: str) -> dict:
        doc = self.cloud.get_json(slot_confirmed_key(slot)) or {}
        vectors = doc.get('vectors') or {}
        signature = doc.get('embedding_signature')
        if signature is None or signature == embedding_signature(self.embed):
            return vectors
        return {item_id: {'_stale': True} for item_id in vectors}

    def _upsert_pending(self, pending: list[dict], journal: dict, slot: str) -> None:
        sent = set()
        replay = []
        for batch in journal['batches']:
            if batch['status'] in {'confirmed', 'accepted'}:
                sent.update(batch['vector_ids'])
            elif batch['status'] in {'sending', 'unknown'}:
                replay.extend(batch['vector_ids'])
        by_id = {item['id']: item for item in pending}
        replay_items = [by_id[item_id] for item_id in replay if item_id in by_id]
        fresh = [
            item for item in pending
            if item['id'] not in sent and item['id'] not in replay
        ]
        if self._embed_and_send(replay_items, journal, slot, replay=True):
            return
        if self._embed_and_send(fresh, journal, slot, replay=False):
            return

    def _embed_and_send(self, items, journal, slot, *, replay: bool) -> bool:
        for offset in range(0, len(items), self.batch_size):
            batch_items = items[offset:offset + self.batch_size]
            values = self._values_for(batch_items)
            vectors = []
            vector_ids = [item['id'] for item in batch_items]
            for item, value in zip(batch_items, values):
                vectors.append({
                    'id': item['id'],
                    'values': value,
                    'namespace': slot,
                    'metadata': item['metadata'],
                })
            existing = None
            if replay:
                for batch in journal['batches']:
                    if batch.get('vector_ids') == vector_ids:
                        existing = batch
                        break
            batch = existing or {
                'vector_ids': vector_ids,
                'status': 'sending',
                'mutation_id': None,
            }
            if existing is None:
                journal['batches'].append(batch)
            else:
                batch['status'] = 'sending'
            self._save_journal(slot, journal)
            if self._accept_mutation(
                batch, journal, slot,
                lambda vectors=vectors: self.cloud.upsert(vectors),
            ):
                return True
            self._hook('after_upsert_journal')
        return False

    def _values_for(self, items: list[dict]) -> list[list[float]]:
        values = [None] * len(items)
        missing = []
        for index, item in enumerate(items):
            cached = self.cloud.get_json(cache_object_key(item['input_hash']))
            if cached and cached.get('pooling') == self.embed['pooling']:
                values[index] = cached['values']
            else:
                missing.append(index)
        if not missing:
            return values
        texts = [items[index]['input'] for index in missing]
        embedded = _call_with_retry(
            self.cloud,
            lambda: self.cloud.embed(texts, self.embed['pooling']),
        )
        self._hook('after_embed_received')
        for index, vector in zip(missing, embedded):
            self.cloud.put_json(cache_object_key(items[index]['input_hash']), {
                'pooling': self.embed['pooling'],
                'values': vector,
                'model': self.embed['model'],
            })
            values[index] = vector
        self._hook('after_cache')
        return values

    def _delete_ids(self, ids: list[str], journal: dict, slot: str) -> None:
        requested = set(ids)
        done = set()
        replay = []
        for batch in journal['deletes']:
            batch_ids = list(batch.get('vector_ids') or [])
            if batch['status'] in {'confirmed', 'accepted'}:
                done.update(batch_ids)
                continue
            if batch['status'] not in {'sending', 'unknown'}:
                continue
            still = [item for item in batch_ids if item in requested]
            batch['vector_ids'] = still
            if still:
                replay.append(batch)
            else:
                batch['status'] = 'confirmed'
        if self._finish_deletes(replay, journal, slot):
            return
        covered = {item for batch in replay for item in batch['vector_ids']}
        fresh = [item for item in ids if item not in done and item not in covered]
        for offset in range(0, len(fresh), DELETE_IDS_BATCH):
            batch = {
                'vector_ids': fresh[offset:offset + DELETE_IDS_BATCH],
                'status': 'sending',
                'mutation_id': None,
            }
            journal['deletes'].append(batch)
            if self._finish_deletes([batch], journal, slot):
                return

    def _finish_deletes(self, batches, journal: dict, slot: str) -> bool:
        for batch in batches:
            batch['status'] = 'sending'
            self._save_journal(slot, journal)
            chunk = list(batch['vector_ids'])
            if self._accept_mutation(
                batch, journal, slot,
                lambda ids=chunk: self.cloud.delete_ids(ids),
            ):
                return True
        return False

    def _accept_mutation(self, batch: dict, journal: dict, slot: str, call) -> bool:
        '''True when the write is unconfirmed and the journal is waiting.'''
        try:
            mutation_id = _call_with_retry(self.cloud, call)
        except UnknownWrite as exc:
            batch['status'] = 'unknown'
            batch['mutation_id'] = exc.mutation_id
            journal['status'] = 'waiting'
            self._save_journal(slot, journal)
            return True
        batch['status'] = 'accepted'
        batch['mutation_id'] = mutation_id
        self._save_journal(slot, journal)
        return False

    def _visible(self, journal, desired_ids, stale_ids) -> bool:
        pending = [
            batch for batch in journal['batches'] + journal['deletes']
            if batch['status'] != 'confirmed'
        ]
        if any(not batch.get('mutation_id') for batch in pending):
            return False
        if pending:
            latest = pending[-1]['mutation_id']
            if self.cloud.mutation_status(latest) != 'complete':
                return False
        present = self.cloud.get_vectors(sorted(desired_ids))
        if set(present) != set(desired_ids):
            return False
        if stale_ids and self.cloud.get_vectors(stale_ids):
            return False
        return True

    def _reader_ok(self, release: dict) -> bool:
        return self.cloud.reader_schema == release['manifest']['reader_schema']

    def _base_still_current(self, journal: dict) -> bool:
        current = self._active_release()
        base = journal.get('base_active_release')
        return current in (base, journal['release_id'])

    def _activate(self, release: dict, slot: str) -> None:
        active = self.cloud.get_json(ACTIVE_KEY)
        if active and active.get('slot') != slot:
            self._leave_slot(active['slot'])
        self.cloud.put_json(ACTIVE_KEY, {
            'release_id': release['release_id'],
            'slot': slot,
            'activated_at': self.cloud.clock(),
            'reader_schema': release['manifest']['reader_schema'],
            'embedding_signature': release['embedding_signature'],
            'build_signature': release['build_signature'],
            'verified_passage_count': release['manifest']['passage_count'],
            'global_index_count': None,
            'publication_check': {
                'ok': True,
                'checked_at': self.cloud.clock(),
                'by': 'publish',
            },
        })

    def _leave_slot(self, slot: str) -> None:
        status = self.cloud.get_json(slot_status_key(slot)) or {}
        if status.get('state') == 'ready':
            status['deactivated_at'] = self.cloud.clock()
            status['rollback_blocked'] = False
            self.cloud.put_json(slot_status_key(slot), status)

    def _active_slot(self) -> str | None:
        active = self.cloud.get_json(ACTIVE_KEY)
        if not active:
            return None
        return active.get('slot')

    def _active_release(self) -> str | None:
        active = self.cloud.get_json(ACTIVE_KEY)
        if not active:
            return None
        return active.get('release_id')

    def _save_journal(self, slot: str, journal: dict) -> None:
        self.cloud.put_json(journal_key(slot), journal)


def run_probe(cloud, embed: dict, tokenizer: WordPieceTokenizer) -> dict:
    '''Isolated namespace. Does not mutate serving slots or the active pointer.'''
    before = _serving_snapshot(cloud)
    cloud.check_permissions()
    if cloud.index_dimensions != embed['dimensions'] or cloud.index_metric != 'cosine':
        raise ProbeError('index is not cosine with the configured dimensions')
    short = 'synthetic probe passage for metadata'
    long_text = _text_with_token_count(tokenizer, embed, embed['max_input_tokens'])
    tails = [
        'alpha beta gamma UNIQUE_TAIL_ONE end',
        'alpha beta gamma UNIQUE_TAIL_TWO end',
        'alpha beta gamma UNIQUE_TAIL_THREE end',
    ]
    rows = [
        ('short', short),
        ('long', long_text),
        ('tail-1', tails[0]),
        ('tail-2', tails[1]),
        ('tail-3', tails[2]),
        ('notion-id', 'synthetic passage, not the notion page'),
    ]
    vectors = []
    embedded = cloud.embed([text for _name, text in rows], embed['pooling'])
    if cloud.poolings[-1] != 'cls':
        raise ProbeError('probe embed did not use cls pooling')
    for (name, text), values in zip(rows, embedded):
        if len(values) != embed['dimensions']:
            raise ProbeError(f'{name} vector dimension {len(values)}')
        if not all(math.isfinite(value) for value in values):
            raise ProbeError(f'{name} vector is not finite')
        if not any(value != 0 for value in values):
            raise ProbeError(f'{name} vector is zero')
        paper_id = 'x' * 132 if name == 'notion-id' else f'probe:{name}'
        vectors.append({
            'id': vector_id(PROBE_SLOT, paper_id, 0),
            'values': values,
            'namespace': PROBE_SLOT,
            'metadata': {
                'paper_id': paper_id,
                'chunk_index': 0,
                'content_hash': sha256_hex(text),
                'input_hash': sha256_hex(text),
            },
        })
    ids = [item['id'] for item in vectors]
    try:
        mutation_id = cloud.upsert(vectors)
        if cloud.mutation_status(mutation_id) != 'complete':
            cloud.complete_all()
        if cloud.mutation_status(mutation_id) != 'complete':
            raise ProbeError('probe upsert was not visible')
        notion_id = vector_id(PROBE_SLOT, 'x' * 132, 0)
        loaded = cloud.get_vectors([notion_id]).get(notion_id)
        if not loaded or loaded['metadata'].get('paper_id') != 'x' * 132:
            raise ProbeError('132-byte metadata did not round-trip')
        query_vector = cloud.embed(['UNIQUE_TAIL_TWO'], embed['pooling'])[0]
        hits = cloud.query(PROBE_SLOT, query_vector, 3)
        if not hits or hits[0]['id'] != vector_id(PROBE_SLOT, 'probe:tail-2', 0):
            raise ProbeError('tail query did not rank the matching distractor first')
        probe_ids = set(ids)
        for slot in SLOTS:
            serving = cloud.query(slot, query_vector, 24)
            if any(hit['id'] in probe_ids for hit in serving):
                raise ProbeError('probe id appeared in a serving namespace')
        for row in cloud.get_vectors(ids).values():
            if row.get('namespace') != PROBE_SLOT:
                raise ProbeError('probe vector was stored in a serving namespace')
    finally:
        _drop_probe(cloud, ids)
    after = _serving_snapshot(cloud)
    if before != after:
        raise ProbeError('probe mutated a serving slot or the active pointer')
    return {'ok': True, 'vectors': len(vectors)}


def _drop_probe(cloud, ids: list[str]) -> None:
    if not ids:
        return
    mutation_id = cloud.delete_ids(ids)
    if cloud.mutation_status(mutation_id) != 'complete':
        cloud.complete_all()
    if cloud.get_vectors(ids):
        raise ProbeError('probe vectors were not deleted')


def _serving_snapshot(cloud) -> str:
    keys = [key for key in cloud.objects if serving_object(key)]
    return canonical_json({key: cloud.objects[key] for key in sorted(keys)})


def _text_with_token_count(tokenizer, embed, target: int) -> str:
    lo = 1
    hi = 400
    best = 'word'
    while lo <= hi:
        mid = (lo + hi) // 2
        text = 'word ' * mid
        count = len(tokenizer.token_ids(embed['passage_template'], text))
        if count <= target:
            best = text
            lo = mid + 1
        else:
            hi = mid - 1
    count = len(tokenizer.token_ids(embed['passage_template'], best))
    if count > target:
        raise ProbeError('failed to build a max-token passage')
    return best


def live_preflight(cloud, report: dict) -> None:
    cloud.check_permissions()
    assert_capacity(report, cloud.dimension_budget)


class CloudflareCloud:
    '''REST client for R2, Vectorize, and Workers AI.

    Unit tests subclass it and replace ``_request`` so no socket is opened.
    '''

    def __init__(self, embed: dict, account_id: str, token: str, budget: int | None):
        self.embed = embed
        self.account_id = account_id
        self.token = token
        self.dimension_budget = budget
        self.index_dimensions = None
        self.index_metric = None
        self.poolings: list[str] = []
        self.reader_schema = embed['reader_schema']
        self.objects: dict[str, object] = {}

    def clock(self) -> float:
        return time.time()

    def sleep(self, seconds: float) -> None:
        time.sleep(seconds)

    def _request(self, method: str, url: str, payload=None, *, body=None, content_type=None):
        data = None
        headers = {'Authorization': f'Bearer {self.token}'}
        if payload is not None:
            data = canonical_json(payload).encode('utf-8')
            headers['Content-Type'] = 'application/json'
        elif body is not None:
            data = body
            headers['Content-Type'] = content_type or 'application/octet-stream'
        request = urllib.request.Request(url, data=data, headers=headers, method=method)
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                raw = response.read()
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode('utf-8', errors='replace')
            if exc.code == 429 or exc.code >= 500:
                retry_after = float(exc.headers.get('Retry-After') or 0)
                raise RetryableError(detail[:500], retry_after=retry_after)
            if exc.code in (401, 403):
                raise FatalError(detail[:500], status=exc.code)
            raise FatalError(f'{exc.code} {detail[:500]}', status=exc.code)
        if not raw:
            return {}
        parsed = json.loads(raw.decode('utf-8'))
        if isinstance(parsed, dict) and parsed.get('success') is False:
            raise FatalError(canonical_json(parsed.get('errors') or parsed)[:500])
        return parsed

    def _account(self, path: str) -> str:
        return f'https://api.cloudflare.com/client/v4/accounts/{self.account_id}{path}'

    def _vectorize(self, suffix: str = '') -> str:
        name = self.embed['vectorize']['index_name']
        return self._account(f'/vectorize/v2/indexes/{name}{suffix}')

    def check_permissions(self) -> None:
        token = self._request(
            'GET', 'https://api.cloudflare.com/client/v4/user/tokens/verify',
        )
        status = ((token.get('result') or {}).get('status'))
        if status != 'active':
            raise FatalError(f'token status {status}')
        index = self._request('GET', self._vectorize())
        config = (index.get('result') or {}).get('config') or {}
        self.index_dimensions = config.get('dimensions')
        self.index_metric = config.get('metric')
        if self.index_dimensions != self.embed['dimensions']:
            raise FatalError('index dimensions do not match embed.json')
        if self.index_metric != 'cosine':
            raise FatalError('index metric is not cosine')
        self._request(
            'GET',
            self._account(f'/r2/buckets/{self.embed["r2_bucket"]}'),
        )

    def embed(self, texts: list[str], pooling: str) -> list[list[float]]:
        self.poolings.append(pooling)
        model = self.embed['model']
        parsed = self._request(
            'POST',
            self._account(f'/ai/run/{model}'),
            {'text': texts, 'pooling': pooling},
        )
        data = (parsed.get('result') or {}).get('data')
        if not isinstance(data, list):
            raise FatalError('workers ai response has no data')
        return data

    def upsert(self, vectors: list[dict]) -> str:
        lines = [
            canonical_json({
                'id': item['id'],
                'values': item['values'],
                'namespace': item['namespace'],
                'metadata': item.get('metadata') or {},
            })
            for item in vectors
        ]
        parsed = self._request(
            'POST',
            self._vectorize('/upsert'),
            body=('\n'.join(lines) + ('\n' if lines else '')).encode('utf-8'),
            content_type='application/x-ndjson',
        )
        return self._accepted_mutation(parsed)

    def delete_ids(self, ids: list[str]) -> str:
        if len(ids) > DELETE_IDS_BATCH:
            raise FatalError('delete batch exceeds 1000 ids')
        parsed = self._request(
            'POST',
            self._vectorize('/delete_by_ids'),
            {'ids': ids},
        )
        return self._accepted_mutation(parsed)

    def _accepted_mutation(self, parsed: dict) -> str:
        mutation = (parsed.get('result') or {}).get('mutationId')
        if not mutation:
            raise UnknownWrite('missing-mutation')
        self._wait_processed(mutation)
        return mutation

    def mutation_status(self, mutation_id: str) -> str:
        if not mutation_id:
            return 'unknown'
        parsed = self._request('GET', self._vectorize('/info'))
        latest = (parsed.get('result') or {}).get('processedUpToMutation')
        if latest == mutation_id:
            return 'complete'
        return 'queued'

    def _wait_processed(self, mutation_id: str) -> None:
        deadline = time.time() + MUTATION_WAIT_SECONDS
        while self.mutation_status(mutation_id) != 'complete':
            if time.time() >= deadline:
                raise RetryableError('mutation was not processed', retry_after=2)
            self.sleep(2)

    def complete_all(self) -> None:
        return None

    def get_vectors(self, ids: list[str]) -> dict[str, dict]:
        found = {}
        for offset in range(0, len(ids), GET_IDS_BATCH):
            chunk = ids[offset:offset + GET_IDS_BATCH]
            parsed = self._request(
                'POST',
                self._vectorize('/get_by_ids'),
                {'ids': chunk},
            )
            rows = parsed.get('result')
            if not isinstance(rows, list):
                raise FatalError('get_by_ids result is not a list')
            for row in rows:
                if isinstance(row, dict) and row.get('id'):
                    found[row['id']] = row
        return found

    def query(self, namespace: str, vector: list[float], top_k: int) -> list[dict]:
        parsed = self._request(
            'POST',
            self._vectorize('/query'),
            {
                'vector': vector,
                'topK': top_k,
                'namespace': namespace,
                'returnMetadata': 'all',
            },
        )
        return (parsed.get('result') or {}).get('matches') or []

    def put_json(self, key: str, payload) -> None:
        quoted = quote(key, safe='/')
        self._request(
            'PUT',
            self._account(f'/r2/buckets/{self.embed["r2_bucket"]}/objects/{quoted}'),
            payload,
        )
        if serving_object(key):
            self.objects[key] = payload

    def get_json(self, key: str):
        quoted = quote(key, safe='/')
        try:
            parsed = self._request(
                'GET',
                self._account(
                    f'/r2/buckets/{self.embed["r2_bucket"]}/objects/{quoted}'
                ),
            )
        except FatalError as exc:
            if exc.status == 404:
                return None
            raise
        return parsed


def _cli_cloud(embed: dict):
    account = os.environ.get('CLOUDFLARE_ACCOUNT_ID')
    token = os.environ.get('CLOUDFLARE_API_TOKEN')
    if not account or not token:
        raise SystemExit('CLOUDFLARE_ACCOUNT_ID and CLOUDFLARE_API_TOKEN are required')
    raw_budget = os.environ.get('AGENT_DIMENSION_BUDGET')
    budget = int(raw_budget) if raw_budget else None
    return CloudflareCloud(embed, account, token, budget)


def main() -> None:
    args = sys.argv[1:]
    if not args:
        raise SystemExit('usage: publish_agent_index.py probe|preflight|publish|rollback')
    command = args[0]
    embed = load_embed()
    if command == 'preflight':
        from build_agent_index import build_from_disk
        release = build_from_disk(embed, progress=True)
        report = release['report']
        print(canonical_json(report))
        if '--live' in args:
            live_preflight(_cli_cloud(embed), report)
            print('preflight ok')
        else:
            print('offline report only; pass --live to check the account')
        if not report['fits_documented_free_tier']:
            print('documented free Vectorize storage cannot hold both slots')
        return
    if command == 'probe':
        cloud = _cli_cloud(embed)
        tokenizer = WordPieceTokenizer(embed)
        result = run_probe(cloud, embed, tokenizer)
        print(canonical_json(result))
        return
    if command == 'publish':
        if os.environ.get('AGENT_PUBLISH_ROLE') != 'ci':
            raise SystemExit(
                'production publish runs from the CI writer '
                '(AGENT_PUBLISH_ROLE=ci)'
            )
        release = load_written_release(DEFAULT_OUT)
        cloud = _cli_cloud(embed)
        live_preflight(cloud, release['report'])
        slot = _flag_value(args, '--slot') or inactive_slot(cloud)
        promote = '--promote' in args
        if '--stage' not in args and not promote:
            raise SystemExit('publish requires --stage or --promote')
        result = Publisher(cloud, embed).publish(
            release, slot, promote=promote, source_sha=os.environ.get('GITHUB_SHA'),
        )
        print(canonical_json(result))
        ok = {'noop'}
        ok.add('promoted' if promote else 'staged')
        if result['status'] not in ok:
            raise SystemExit(2)
        return
    if command == 'rollback':
        if os.environ.get('AGENT_PUBLISH_ROLE') != 'ci':
            raise SystemExit(
                'production rollback runs from the CI writer '
                '(AGENT_PUBLISH_ROLE=ci)'
            )
        cloud = _cli_cloud(embed)
        try:
            pointer = Publisher(cloud, embed).rollback()
        except PublishError as exc:
            print(canonical_json({'status': exc.code, 'detail': str(exc)}))
            raise SystemExit(2)
        print(canonical_json(pointer))
        return
    raise SystemExit(f'unknown command {command}')


def inactive_slot(cloud) -> str:
    active = cloud.get_json(ACTIVE_KEY) or {}
    if active.get('slot') == 'a':
        return 'b'
    return 'a'


def _flag_value(args: list[str], flag: str) -> str | None:
    if flag not in args:
        return None
    index = args.index(flag)
    if index + 1 >= len(args):
        raise SystemExit(f'{flag} needs a value')
    return args[index + 1]


if __name__ == '__main__':
    main()
