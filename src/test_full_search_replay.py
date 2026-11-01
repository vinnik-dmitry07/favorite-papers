'''Historical replay rejects changed evidence before doing metric work.'''

from copy import deepcopy

import pytest

from build_agent_index import BuildError
import restore_full_search_artifact as restore
import summarize_full_search_replay as replay


@pytest.fixture
def rankings():
    source_names = [
        'worker/src/full-search-index.ts', 'worker/src/static-search-int8.ts',
        'worker/probe-kernel/scan.wat', 'worker/probe-kernel/scan.wasm',
    ]
    sources = dict.fromkeys(source_names, 'original')
    binding = {'code_sha256': sources,
               'historical_packed_manifest_sha256': 'packed'}
    manifest = {'rows': [{} for _ in range(100)], 'rows_sha256': 'rows'}
    metadata = {'count': 64, 'vectors_sha256': 'queries'}
    runtime = {
        'engine': 'full-int8-runtime',
        'kind': 'historical-artifact-offline-rankings',
        'artifact_sha256': replay.ARTIFACT_SHA256, 'run_id': replay.RUN_ID,
        'query_count': 64, 'passage_count': 100,
        'query_vectors_sha256': 'queries',
        'query_manifest_sha256': 'frozen', 'source_rows_sha256': 'rows',
        'packed_manifest_sha256': 'packed',
        'implementation': {'source_sha256': dict(sources)},
        'wasm_sha256': 'original',
        'js_wasm_checked_queries': list(range(64)),
        'js_wasm_max_score_difference': 0,
        'rankings': [list(range(50)) for _ in range(64)],
    }
    return runtime, manifest, metadata, binding


def test_complete_historical_rankings_are_accepted_without_mutation(rankings):
    runtime, manifest, metadata, binding = rankings
    before = deepcopy(rankings)
    actual = replay.validated_rankings(
        runtime, manifest, metadata, 'frozen', binding
    )
    assert actual.shape == (64, 50)
    assert actual[0].tolist() == list(range(50))
    assert rankings == before


@pytest.mark.parametrize('change', [
    'fractional', 'boolean', 'duplicate', 'missing', 'out-of-range',
    'archive', 'packed', 'crosscheck', 'source',
])
def test_changed_rankings_or_provenance_are_rejected(rankings, change):
    runtime, manifest, metadata, binding = rankings
    if change == 'fractional':
        runtime['rankings'][0][0] = 0.5
    elif change == 'boolean':
        runtime['rankings'][0][0] = False
    elif change == 'duplicate':
        runtime['rankings'][0][0] = 1
    elif change == 'missing':
        runtime['rankings'].pop()
    elif change == 'out-of-range':
        runtime['rankings'][0][0] = 100
    elif change == 'archive':
        runtime['artifact_sha256'] = 'different'
    elif change == 'packed':
        runtime['packed_manifest_sha256'] = 'different'
    elif change == 'crosscheck':
        runtime['js_wasm_checked_queries'].pop()
    else:
        runtime['implementation']['source_sha256'][
            'worker/src/full-search-index.ts'
        ] = 'different'
    with pytest.raises(BuildError):
        replay.validated_rankings(
            runtime, manifest, metadata, 'frozen', binding
        )


def test_wrong_archive_stops_before_reading_assets_or_rebuilding(
        tmp_path, monkeypatch):
    archive = tmp_path / 'changed.zip'
    archive.write_bytes(b'not the authenticated retained artifact')
    output = tmp_path / 'replay'
    monkeypatch.setattr(restore, 'ROOT', tmp_path / 'no-source-assets')

    def forbidden(*args, **kwargs):
        pytest.fail('Restoration work began before archive authentication')

    for name in ('read_texts', 'build_full_corpus', 'write_full_corpus', 'pack'):
        monkeypatch.setattr(restore, name, forbidden)
    with pytest.raises(BuildError, match='authenticated GitHub artifact'):
        restore.restore(archive, output)
    assert not output.exists()
