'''Hash-bound, resumable fail-fast gates for the intended full offline encode.

This CLI never loads model weights or calls a provider. UNKNOWN is STOP. Local
geometry checks are engineering filters and do not establish Cloudflare limits.
'''
from __future__ import annotations

import argparse
from collections import Counter
from contextlib import contextmanager
from contextvars import ContextVar
from datetime import datetime, timezone
import hashlib
import importlib.metadata
import json
import math
import multiprocessing
import os
from pathlib import Path
import platform
import subprocess
import tempfile
import sys
import time
import xml.etree.ElementTree as ET

from build_agent_index import (
    BuildError, WordPieceTokenizer, canonical_json, load_embed, model_input,
    read_texts, clean_markdown, sha256_hex, _assert_coverage,
)
from common import ROOT
from embed_real_search_probe import (
    BgeEncoder, atomic_bytes, canonical_inputs, checked_asset,
    encoder_identity,
)

SCHEMA = 1
SCOPE = 'GO_FOR_FULL_OFFLINE_ENCODE'
TTL_SECONDS = 24 * 60 * 60
GATE_CHECKS = {
    'tokenizer-parity': {'all_passages', 'all_queries', 'hf_token_ids',
                         'runtime_token_ids', 'no_truncation', 'no_model_load'},
    'numeric-contracts': {'real_vectors', 'quantized_oracle', 'js_wasm',
                          'tie_boundaries', 'rest_wrapper', 'mcp_wrapper',
                          'catalog_routes', 'row_mapping'},
    'geometry-memory': {'canonical_full_coverage', 'synthetic_provenance',
                        'production_rejects_fixture',
                        'observed_peak_below_local_threshold',
                        'repeated_churn_retained_growth_bounded',
                        'singleton_initialization', 'bounded_admission',
                        'bounded_queue', 'structural_allocation_bound'},
    'local-canary': {'tokenizer_parity', 'finite_unit_768', 'batch_invariance',
                     'input_identity', 'within_budget'},
    'provider-compatibility': {'targeted_coverage', 'finite_unit_768',
                               'min_cosine', 'batch_invariance', 'input_identity',
                               'free_allowance_operator_asserted',
                               'within_budget'},
}
BUDGET_SECONDS = {'tokenizer-parity': 600, 'numeric-contracts': 180,
                  'geometry-memory': 600, 'local-canary': 300,
                  'provider-compatibility': 300}
DEPENDENCIES = {
    'tokenizer-parity': [], 'numeric-contracts': ['tokenizer-parity'],
    'geometry-memory': ['tokenizer-parity'],
    'local-canary': ['tokenizer-parity', 'numeric-contracts', 'geometry-memory'],
    'provider-compatibility': ['local-canary'],
}
_CANARY_INPUT_CACHE = ContextVar('canary_input_cache', default=None)


def require(condition, message):
    if not condition:
        raise BuildError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def digest(value):
    return sha(canonical_json(value).encode())


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def write_json(path, value):
    atomic_bytes(Path(path), (canonical_json(value) + '\n').encode())


def verify_frozen_queries(corpus, queries, pin):
    '''Require the reviewed ordered query payload and its source inventory.'''
    manifest = read_json(Path(corpus) / 'probe.json')
    document = read_json(queries)
    expected = read_json(pin)
    rows = document.get('queries')
    require(isinstance(rows, list) and all(isinstance(row, dict)
                                         for row in rows),
            'Frozen query payload is invalid')
    actual = {
        'schema_version': 1,
        'kind': 'reviewed-full-query-pin',
        'query_count': len(rows),
        'cohorts': dict(Counter(row.get('cohort') for row in rows)),
        'ordered_queries_sha256': digest(rows),
        'source_graph_sha256': manifest.get('source_graph_sha256'),
        'source_texts_sha256': manifest.get('source_texts_sha256'),
    }
    require(expected == actual,
            'Frozen queries or source inventory differ from reviewed pin')
    return {'status': 'PASS', **actual}


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def code_hashes():
    paths = set()
    for directory, patterns in [('src', ['*.py']), ('worker/src', ['*.ts']),
                                ('worker/probe-kernel', ['*.ts', '*.mjs', '*.wat', '*.wasm']),
                                ('.github/workflows', ['*.yml', '*.yaml'])]:
        for pattern in patterns:
            paths.update((ROOT / directory).glob(pattern))
    for relative in ['worker/embed.json', 'worker/tokenizer/vocab.txt',
                     'worker/tokenizer/tokenizer_config.json', 'worker/package-lock.json',
                     'requirements-real-probe.txt',
                     'requirements-torch-probe.txt',
                     'requirements-probe-quality.txt']:
        paths.add(ROOT / relative)
    paths.update((ROOT / 'worker/fixtures').glob('*.json'))
    return {str(path.relative_to(ROOT)): sha(path.read_bytes())
            for path in sorted(paths) if path.is_file()}


def environment():
    versions = {}
    for name in ('torch', 'transformers', 'tokenizers', 'numpy'):
        try:
            versions[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            versions[name] = None
    return {'python': platform.python_version(), 'packages': versions,
            'node': subprocess.check_output(['node', '--version'], text=True).strip()}


def frozen_inputs(corpus, queries, config):
    # Import lazily: tokenizer-only entry still does not import/load AutoModel.
    from evaluate_full_search_probe import corpus_inputs, validate_question
    manifest, papers, _, identity = corpus_inputs(corpus)
    document = read_json(queries)
    require(document.get('kind') == 'frozen-full-corpus-quality-diagnostics'
            and document.get('corpus_identity') == identity
            and document.get('release_id') == manifest['release_id']
            and document.get('embedding_signature') == manifest['embedding_signature'],
            'Frozen questions do not match current canonical corpus')
    questions = document.get('queries')
    require(isinstance(questions, list) and questions, 'Frozen questions missing')
    require(len({row['id'] for row in questions}) == len(questions), 'Duplicate query IDs')
    counts = Counter(row.get('cohort') for row in questions)
    require(counts['extractive_fidelity'] == 2000 and counts['natural_development'] >= 64,
            'Need frozen extractive2000 and at least64 natural development questions')
    for item in questions:
        validate_question(item, papers)
    return document, [model_input(config['query_template'], row['query'])
                      for row in questions]


@contextmanager
def canary_validation_cache():
    '''Reuse canary tokenization, checking every asset on each use.'''
    token = _CANARY_INPUT_CACHE.set({})
    try:
        yield
    finally:
        _CANARY_INPUT_CACHE.reset(token)


def _canonical_inputs(corpus, config):
    cache = _CANARY_INPUT_CACHE.get()
    corpus = Path(corpus).resolve()
    if cache is None:
        return canonical_inputs(corpus, config, full_corpus=True)

    def fingerprint():
        raw = (corpus / 'probe.json').read_bytes()
        manifest = json.loads(raw)
        require(isinstance(manifest.get('files'), dict),
                'Invalid canary asset manifest')
        # Hash bytes, not mtimes: same-size edits and restored timestamps must
        # not let cached token IDs certify different inputs. checked_asset also
        # enforces path containment and each manifest checksum.
        for name in manifest['files']:
            checked_asset(corpus, manifest, name)
        return digest({'manifest_sha256': sha(raw), 'config': config})

    before = fingerprint()
    cached = cache.get(corpus)
    if cached is not None:
        require(cached[0] == before, 'Canary corpus/config changed during run')
        return cached[1]
    result = canonical_inputs(corpus, config, full_corpus=True)
    require(before == fingerprint(), 'Canary corpus changed during validation')
    cache[corpus] = (before, result)
    return result


def current_binding(corpus, queries, config=None):
    config = config or load_embed()
    corpus, queries = Path(corpus).resolve(), Path(queries).resolve()
    manifest, _ = _canonical_inputs(corpus, config)
    document, _ = frozen_inputs(corpus, queries, config)
    stable = {key: value for key, value in manifest.items() if key != 'embeddings'}
    stable['files'] = {key: value for key, value in stable['files'].items()
                       if key != 'vectors.f32'}
    preembedding = {**stable, 'embeddings': None}
    # Binding raw source files prevents a stale canonical artifact from hiding
    # a changed source, while completed vector attachments do not break resume.
    source = Path(manifest['source_path'])
    source = source if source.is_absolute() else ROOT / source
    raw = source.read_bytes()
    require(sha(raw) == manifest['source_graph_sha256'], 'Source graph changed')
    source_texts = read_texts(json.loads(raw)['nodes'])
    text_hashes = {pid: sha(text.encode()) if text is not None else None
                   for pid, text in source_texts.items()}
    require(text_hashes == manifest['source_text_hashes'], 'Source texts changed')
    source_ids = sorted(node['id'] for node in json.loads(raw)['nodes'])
    require(source_ids == manifest['paper_ids'], 'Canonical catalog omits or adds source cards')
    expected_texts = {pid: clean_markdown(text) for pid, text in source_texts.items()
                      if text is not None and clean_markdown(text).strip()}
    require(sorted(expected_texts) == manifest['text_paper_ids'], 'Canonical text inventory differs from source')
    graph = read_json(corpus / f'releases/{manifest["release_id"]}/graph.json')
    for pid in source_ids:
        card = graph['nodes'][pid]
        if pid not in expected_texts:
            reason = 'no_markdown' if source_texts[pid] is None else 'empty_cleaned'
            require(card['text']['available'] is False and card['text']['reason'] == reason,
                    'Unavailable card reason differs from source')
            continue
        paper = read_json(corpus / f'releases/{manifest["release_id"]}/papers/{sha256_hex(pid)}.json')
        require(paper['text'] == expected_texts[pid], 'Canonical body differs from complete cleaned source')
        _assert_coverage(len(paper['text']),
                         [(row['start'], row['end'], row['token_count']) for row in paper['chunks']],
                         config['max_code_points'], config['overlap_code_points'])
    head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT,
                                   text=True).strip()
    return {
        'corpus': str(corpus), 'queries': str(queries), 'head': head,
        'canonical_manifest_sha256': digest(stable),
        'preembedding_manifest_sha256': digest(preembedding),
        'release_id': manifest['release_id'],
        'rows_sha256': digest(manifest['rows']),
        'source_graph_sha256': sha(raw), 'source_texts_sha256': digest(text_hashes),
        'query_manifest_sha256': sha(queries.read_bytes()),
        'query_corpus_identity': document['corpus_identity'],
        'counts': {'passages': len(manifest['rows']), 'cards': len(manifest['paper_ids']),
                   'texts': len(manifest['text_paper_ids']), 'queries': len(document['queries'])},
        'code_sha256': code_hashes(), 'environment': environment(),
        'encoder_identity': encoder_identity(config),
        'gate_policy_sha256': digest({'checks': {k: sorted(v) for k, v in GATE_CHECKS.items()},
                                     'budgets': BUDGET_SECONDS, 'dependencies': DEPENDENCIES}),
    }


def snapshot(corpus, queries, output):
    output = Path(output)
    binding = current_binding(corpus, queries)
    value = {'schema_version': SCHEMA, 'kind': 'full-search-preflight-snapshot',
             'created_at': utc_now(), 'binding': binding, 'fingerprint': digest(binding),
             'scope': SCOPE, 'platform_cpu_gate': 'UNKNOWN',
             'platform_memory_gate': 'UNKNOWN', 'quality_gate': 'UNKNOWN'}
    path = output / 'snapshot.json'
    if path.exists():
        require(read_json(path)['fingerprint'] == value['fingerprint'],
                'Existing run binds different inputs; use a fresh directory')
        return read_json(path)
    write_json(path, value)
    return value


def load_run(run_dir, *, refresh=True):
    run_dir = Path(run_dir)
    document = read_json(run_dir / 'snapshot.json')
    require(document.get('schema_version') == SCHEMA
            and document.get('kind') == 'full-search-preflight-snapshot'
            and document.get('scope') == SCOPE
            and document.get('fingerprint') == digest(document.get('binding')),
            'Invalid preflight snapshot')
    if refresh:
        bound = document['binding']
        require(current_binding(bound['corpus'], bound['queries']) == bound,
                'Stale preflight: source, queries, environment or code changed')
    return document


def evidence_path(run_dir, gate):
    require(gate in GATE_CHECKS, 'Unknown preflight gate')
    return Path(run_dir) / ('gate-' + gate + '.json')


def begin_gate(run_dir, gate):
    '''Revoke an old PASS before a retry, including every dependent gate.'''
    run = load_run(run_dir)
    affected = {gate}
    while True:
        expanded = affected | {name for name, deps in DEPENDENCIES.items()
                               if affected.intersection(deps)}
        if expanded == affected:
            break
        affected = expanded
    for name in affected:
        path = evidence_path(run_dir, name)
        if path.exists():
            previous = path.read_bytes()
            atomic_bytes(Path(run_dir) / 'history' / (name + '-' + sha(previous) + '.json'), previous)
        write_json(path, {'schema_version': SCHEMA, 'kind': 'full-search-preflight-evidence',
                          'gate': name, 'status': 'UNKNOWN', 'created_at': utc_now(),
                          'fingerprint': run['fingerprint'], 'reason': 'New attempt: ' + gate})
    return run


def raw_documents(document):
    return {Path(item['path']).name: read_json(item['path'])
            for item in document['artifacts'] if item['path'].endswith('.json')}


def build_memory_bundle(output):
    '''Rebuild from the bound checkout; an old executable is not new evidence.'''
    subprocess.run([
        str(ROOT / 'worker/node_modules/.bin/esbuild'),
        str(ROOT / 'worker/probe-kernel/full-memory.ts'), '--bundle',
        '--platform=node', '--format=esm', '--outfile=' + str(output),
    ], cwd=ROOT, check=True, capture_output=True, timeout=60)
    return sha(Path(output).read_bytes())


def verify_memory_bundle(value, artifacts):
    executed = value.get('executed_bundle_sha256')
    retained = [entry for entry in artifacts
                if entry['path'].endswith('.mjs') and entry.get('sha256') == executed]
    require(len(retained) == 1, 'Memory executed bundle is not retained')
    with tempfile.TemporaryDirectory(prefix='full-memory-verify-') as directory:
        checksum = build_memory_bundle(Path(directory) / 'reviewed.mjs')
    require(checksum == executed, 'Memory executed bundle differs from reviewed source')


def validate_raw_evidence(document, run):
    '''Check retained consistency, not trusted execution attestation.'''
    gate, raw = document['gate'], raw_documents(document)
    bound = run['binding']
    if gate == 'tokenizer-parity':
        result = raw.get('tokenizer-result.json', {})
        require(result.get('status') == 'PASS' and result.get('model_loaded') is False
                and result.get('passages') == bound['counts']['passages']
                and result.get('queries') == bound['counts']['queries']
                and result.get('fixture_count', 0) >= 49
                and result.get('overlimit_rejected') is True,
                'Tokenizer raw coverage/no-model evidence missing')
        runtime = result.get('runtime', {})
        require(runtime.get('checked') == result.get('count')
                and runtime.get('mismatch_count') == 0
                and runtime.get('input_sha256') == result.get('records_sha256'),
                'Tokenizer raw runtime report mismatch')
        files = {Path(item['path']).name: item['sha256'] for item in document['artifacts']}
        require(files.get('tokenizer-inputs.jsonl') == result.get('records_sha256')
                and result.get('runtime_harness_sha256') in files.values(),
                'Tokenizer raw inputs/bundle not retained')
        records = next(item['path'] for item in document['artifacts']
                       if Path(item['path']).name == 'tokenizer-inputs.jsonl')
        validate_tokenizer_records(records, result)
    elif gate == 'numeric-contracts':
        result = raw.get('numeric-result.json', {})
        require(result.get('kind') == 'full-search-numeric-evidence'
                and result.get('fingerprint') == run['fingerprint']
                and result.get('pytest_exit_code') == result.get('vitest_exit_code') == 0,
                'Numeric process reports missing or failed')
        files = {Path(item['path']).name: item['path'] for item in document['artifacts']}
        root = ET.parse(files['numeric-pytest.xml']).getroot()
        cases = root.findall('.//testcase')
        require(len(cases) >= 30 and not root.findall('.//failure')
                and not root.findall('.//error') and not root.findall('.//skipped'),
                'Numeric Python tests incomplete/failed/skipped')
        names = ' '.join(case.get('name', '') for case in cases)
        require('test_fixture_is_honest_reproducible_and_preserves_mapping' in names
                and 'test_quantizer_independent_round_to_even_and_normalization' in names,
                'Required pack tests were not executed')
        vitest = raw.get('numeric-vitest.json', {})
        require(vitest.get('success') is True and vitest.get('numFailedTests') == 0
                and vitest.get('numPendingTests') == 0 and vitest.get('numPassedTests', 0) >= 15,
                'Numeric Worker tests incomplete/failed/skipped')
        names = ' '.join(case.get('fullName', '') for suite in vitest.get('testResults', [])
                         for case in suite.get('assertionResults', []))
        for required in ['independent quantized cosine', 'top25/top40',
                         'top40 before deduplication', 'MCP top25 before deduplication',
                         'eight REST and five MCP', 'exact catalog-only match']:
            require(required in names, 'Required Worker contract test missing: ' + required)
        real = raw.get('numeric-real-vectors.json', {})
        require(real.get('kind') == 'full-search-real-numeric' and real.get('status') == 'PASS'
                and real.get('synthetic') is False and real.get('count') == 390
                and real.get('query_count') == 32 and real.get('candidate_limits') == [25, 40, 50]
                and 0 <= real.get('max_score_difference', float('inf')) <= 1e-12
                and all(real.get('checks', {}).get(key) is True
                        for key in ('quantized_oracle', 'js_wasm', 'row_mapping')),
                'Genuine390 vector numerical evidence missing or failed')
        require(real.get('source_sha256') and all(bound['code_sha256'].get(key) == value
                for key, value in real['source_sha256'].items()), 'Stale real numerical implementation')
    elif gate == 'geometry-memory':
        matches = [value for value in raw.values() if value.get('gate') == 'geometry-memory'
                   and value.get('schema_version') == 2]
        require(len(matches) == 1, 'Expected one raw memory harness report')
        value = matches[0]
        require(value.get('status') == 'PASS'
                and all(value.get('checks', {}).get(key) is True for key in GATE_CHECKS[gate])
                and value.get('passages') == bound['counts']['passages']
                and value.get('papers') == bound['counts']['cards']
                and value.get('source_rows_sha256') == bound['rows_sha256']
                and value.get('source_manifest_sha256') == bound['preembedding_manifest_sha256']
                and value.get('synthetic') is True,
                'Memory raw provenance/coverage/checks mismatch')
        sources = value.get('source_sha256', {})
        require({'worker/probe-kernel/full-memory.ts', 'worker/src/full-corpus-store.ts',
                 'worker/src/full-search-index.ts', 'worker/probe-kernel/scan.wasm'} <= sources.keys()
                and all(bound['code_sha256'].get(key) == checksum for key, checksum in sources.items()),
                'Memory raw implementation is stale or unbound')
        verify_memory_bundle(value, document['artifacts'])
        require(value.get('manifest_sha256') == sha(Path(value['packed_manifest_path']).read_bytes()),
                'Memory packed manifest changed')
        require(value['summary']['peaks']['heap_plus_external'] < 96 * 1024**2
                and value['retained_growth']['bytes'] <= 8 * 1024**2
                and value['method']['local_threshold_bytes'] <= 96 * 1024**2
                and value['elapsed_ms'] <= 600000,
                'Memory raw thresholds exceeded')
        account = value.get('structural_allocation_account', {})
        require(account.get('unknowns') and account['one_source_shard_bytes'] <= 4096 * 768
                and account['request_admission']['max_active'] <= 4
                and account['request_admission']['max_queued'] <= 8
                and value.get('cloudflare_memory_gate') == 'unverified',
                'Memory structural bounds/platform scope missing')
    else:
        local = raw.get('canary-local-vectors.json', {})
        plan = canary_plan(Path(document['run_dir']))
        require(local.get('plan_sha256') == plan['sha256']
                and local.get('inputs') == plan['inputs']
                and local.get('encoder') == bound['encoder_identity'],
                'Canary raw input/model identity differs')
        indices = local.get('repeat_indices', [])
        require(len(indices) == 2 and len(set(indices)) == 2
                and all(type(index) is int and 0 <= index < len(plan['inputs']) for index in indices),
                'Canary raw repetition missing')
        def vectors(values, count):
            require(isinstance(values, list) and len(values) == count, 'Canary raw vector count mismatch')
            for vector in values:
                require(isinstance(vector, list) and len(vector) == 768
                        and all(type(x) in (int, float) and math.isfinite(x) for x in vector)
                        and abs(math.sqrt(math.fsum(x*x for x in vector)) - 1) <= 1e-4,
                        'Canary raw vectors must be finite unit768')
            return values
        first = vectors(local.get('vectors'), len(plan['inputs']))
        repeats = vectors(local.get('repeated_vectors'), 2)
        require(max(abs(first[index][j] - repeats[k][j]) for k, index in enumerate(indices)
                    for j in range(768)) <= 1e-5, 'Local raw batch invariance failed')
        require(document['measurements']['input_count'] == len(first) + len(repeats)
                and document['measurements']['total_input_tokens'] ==
                sum(row['token_count'] for row in plan['inputs']) +
                sum(plan['inputs'][i]['token_count'] for i in indices), 'Canary actual usage differs')
        ledger = read_json(Path(document['run_dir']) / 'canary-attempt.json')
        require(ledger.get('status') in ('LOCAL_ONLY', 'PASSED')
                and ledger.get('fingerprint') == run['fingerprint']
                and ledger.get('plan_sha256') == plan['sha256'], 'Canary attempt is incomplete/stale/stopped')
        if gate == 'provider-compatibility':
            require(ledger.get('status') == 'PASSED' and ledger.get('provider_requested') is True
                    and ledger.get('provider_requests') == [
                        {'indices': list(range(len(plan['inputs']))), 'status': 'COMPLETE'},
                        {'indices': indices, 'status': 'COMPLETE'}]
                    and ledger.get('provider_input_count') == document['measurements']['input_count']
                    and ledger.get('provider_token_count') == document['measurements']['total_input_tokens'],
                    'Provider attempt has not passed exact reserved usage')
            remote = raw.get('canary-provider-vectors.json', {})
            require(remote.get('plan_sha256') == plan['sha256']
                    and remote.get('model') == plan['model']
                    and remote.get('repeat_indices') == indices, 'Provider raw identity differs')
            other = vectors(remote.get('vectors'), len(first))
            again = vectors(remote.get('repeated_vectors'), 2)
            cosine = min(math.fsum(a*b for a, b in zip(left, right)) for left, right in zip(first, other))
            require(cosine >= .999 and abs(cosine - document['measurements']['min_cosine']) <= 1e-12
                    and max(abs(other[index][j] - again[k][j]) for k, index in enumerate(indices)
                            for j in range(768)) <= 1e-5, 'Provider raw cosine/batch evidence failed')


def validate_evidence(document, snapshot_doc):
    gate = document.get('gate')
    require(gate in GATE_CHECKS and document.get('schema_version') == SCHEMA
            and document.get('kind') == 'full-search-preflight-evidence', 'Invalid gate report')
    require(document.get('fingerprint') == snapshot_doc['fingerprint'], 'Stale gate fingerprint')
    require(document.get('status') == 'PASS', f'{gate}: missing, failed or UNKNOWN')
    checks = document.get('checks', {})
    require(GATE_CHECKS[gate] <= checks.keys()
            and all(checks[key] is True for key in GATE_CHECKS[gate]),
            f'{gate}: mandatory checks are not all true')
    elapsed = document.get('elapsed_seconds')
    require(type(elapsed) in (float, int) and 0 <= elapsed <= BUDGET_SECONDS[gate],
            f'{gate}: elapsed budget exceeded or missing')
    age = datetime.now(timezone.utc).timestamp() - datetime.fromisoformat(document['created_at']).timestamp()
    require(0 <= age <= TTL_SECONDS, f'{gate}: expired or future evidence')
    artifacts = document.get('artifacts')
    require(isinstance(artifacts, list) and artifacts, f'{gate}: no raw evidence artifact')
    for entry in artifacts:
        require(sha(Path(entry['path']).read_bytes()) == entry['sha256'], f'{gate}: raw evidence changed')
    metrics = document.get('measurements', {})
    if gate in ('local-canary', 'provider-compatibility'):
        require(type(metrics.get('input_count')) is int and 1 <= metrics['input_count'] <= 32
                and type(metrics.get('total_input_tokens')) is int
                and 0 < metrics['total_input_tokens'] <= 16384,
                f'{gate}: canary input budget invalid')
        difference = metrics.get('batch_max_abs_difference')
        require(type(difference) in (float, int) and 0 <= difference <= 1e-5,
                f'{gate}: batch invariance exceeds declared tolerance')
        require(metrics.get('plan_sha256') == document.get('canary_plan_sha256'),
                f'{gate}: canary plan differs')
        if gate == 'provider-compatibility':
            cosine = metrics.get('min_cosine')
            require(type(cosine) in (int, float) and .999 <= cosine <= 1.000001,
                    'Provider cosine below .999')
            allowance = metrics.get('available_neurons_operator_asserted')
            estimate = math.ceil(
                metrics['total_input_tokens'] * load_embed()['pricing'][
                    'neurons_per_million_tokens'] / 1_000_000)
            require(type(allowance) is int and allowance >= estimate
                    and metrics.get('free_allowance_evidence')
                    == 'operator-assertion-not-provider-verified',
                    'Provider allowance lacks sufficient operator assertion')
    validate_raw_evidence(document, snapshot_doc)
    return document


def validate_tokenizer_records(path, result):
    '''Reject malformed retained IDs; reports require a trusted runner.'''
    config = load_embed()
    tokenizer = WordPieceTokenizer(config)
    vocab_size = len(tokenizer.ids_by_token)
    require(all(type(result.get(key)) is int and result[key] >= 0
                for key in ('passages', 'queries', 'fixture_count')),
            'Tokenizer retained coverage counts are malformed')
    expected_count = (result['passages'] + result['queries']
                      + result['fixture_count'])
    require(type(result.get('count')) is int
            and result['count'] == expected_count,
            'Tokenizer retained record count differs from coverage')
    count = 0
    tokens = 0
    with Path(path).open(encoding='utf-8') as stream:
        for line in stream:
            row = json.loads(line)
            require(isinstance(row, dict) and row.get('id') == str(count)
                    and row.get('template') == ''
                    and isinstance(row.get('text'), str),
                    'Tokenizer retained input record is malformed')
            ids = row.get('ids')
            require(isinstance(ids, list)
                    and 2 <= len(ids) <= config['max_input_tokens']
                    and all(type(value) is int and 0 <= value < vocab_size
                            for value in ids)
                    and ids[0] == tokenizer.ids_by_token[tokenizer.cls]
                    and ids[-1] == tokenizer.ids_by_token[tokenizer.sep],
                    'Tokenizer retained IDs are malformed')
            count += 1
            tokens += len(ids)
            require(count <= expected_count,
                    'Tokenizer retained records exceed coverage')
    require(count == expected_count
            and type(result.get('token_count')) is int
            and result['token_count'] == tokens,
            'Tokenizer retained record/token totals differ')


def write_evidence(run_dir, gate, *, checks, measurements, artifacts,
                   elapsed_seconds, status='PASS'):
    run = load_run(run_dir)
    require(status in ('PASS', 'FAIL', 'UNKNOWN'), 'Invalid gate status')
    document = {'schema_version': SCHEMA, 'kind': 'full-search-preflight-evidence',
                'gate': gate, 'status': status, 'created_at': utc_now(),
                'fingerprint': run['fingerprint'], 'checks': checks,
                'run_dir': str(Path(run_dir).resolve()),
                'measurements': measurements, 'elapsed_seconds': elapsed_seconds,
                'budget_seconds': BUDGET_SECONDS[gate],
                'artifacts': [{'path': str(Path(path).resolve()),
                               'sha256': sha(Path(path).read_bytes())} for path in artifacts]}
    if gate in ('local-canary', 'provider-compatibility'):
        document['canary_plan_sha256'] = canary_plan(run_dir)['sha256']
    if status == 'PASS':
        for dependency in DEPENDENCIES[gate]:
            validate_evidence(read_json(evidence_path(run_dir, dependency)), run)
        validate_evidence(document, run)
    path = evidence_path(run_dir, gate)
    # Preserve previous attempts for audit; resumable work never upgrades them.
    if path.exists():
        previous = path.read_bytes()
        atomic_bytes(Path(run_dir) / 'history' / (gate + '-' + sha(previous) + '.json'), previous)
    write_json(path, document)
    return path


def check_canary_prerequisites(run_dir):
    run = load_run(run_dir)
    for gate in ('tokenizer-parity', 'numeric-contracts', 'geometry-memory'):
        validate_evidence(read_json(evidence_path(run_dir, gate)), run)
    return run


def canary_plan(run_dir):
    run = load_run(run_dir, refresh=False)
    config = load_embed()
    manifest, passages = _canonical_inputs(
        Path(run['binding']['corpus']), config,
    )
    tokenizer = WordPieceTokenizer(config)
    inputs = []

    def add(identifier, role, text, categories):
        value = model_input(config[role + '_template'], text)
        ids = tokenizer.token_ids('', value)
        require(len(ids) <= config['max_input_tokens'], 'Canary would truncate')
        inputs.append({'id': identifier, 'role': role, 'input': value,
                       'input_hash': sha(value.encode()), 'token_ids_sha256': digest(ids),
                       'token_count': len(ids), 'categories': categories})

    for token in ('[PAD]', '[UNK]', '[CLS]', '[SEP]', '[MASK]'):
        for role in ('passage', 'query'):
            add(role + '-' + token[1:-1].lower(), role,
                'Interpret ' + token + ' in the transformer sequence.', ['special-token', token])
    failing = [(i, row) for i, row in enumerate(manifest['rows'])
               if row['paper_id'] == 'arxiv:2211.10869' and '[MASK]' in passages[i]
               and 'performance worsens for single-task' in passages[i]]
    require(failing, 'Actual formerly failing MASK passage is absent')
    index, _ = failing[0]
    # Passage strings already contain the configured template.
    passage = passages[index][len(config['passage_template']):]
    add('actual-mask-passage', 'passage', passage, ['actual-failing-paper', '[MASK]'])
    add('actual-mask-query', 'query', 'What is the purpose of [MASK] in this method?', ['[MASK]', 'query'])
    add('unicode-passage', 'passage', 'Café naïve 中文 ΟΣ e\u0301 😀 A\u0000B.', ['unicode'])
    add('unicode-query', 'query', 'How does café 中文 ΟΣ e\u0301 😀 tokenization work?', ['unicode'])
    near = max(range(len(passages)), key=lambda i: manifest['rows'][i]['token_count'])
    add('longest-passage', 'passage', passages[near][len(config['passage_template']):], ['near-limit'])
    # Construct a max-length permitted query using the actual query template.
    text = 'a'
    while (len(tokenizer.token_ids(config['query_template'], text + ' a')) <= config['max_input_tokens']
           and len(text + ' a') <= config['limits']['query_code_points_max']):
        text += ' a'
    add('near-limit-query', 'query', text, ['near-limit'])
    require(len(inputs) == 16 and sum(row['token_count'] for row in inputs) <= 16384,
            'Invalid canary plan budget')
    plan = {'schema_version': SCHEMA, 'fingerprint': run['fingerprint'],
            'model': config['model'], 'local_model_id': config['tokenizer']['id'],
            'local_model_revision': config['tokenizer']['revision'],
            'query_template': config['query_template'], 'passage_template': config['passage_template'],
            'inputs': inputs, 'max_actual_texts': 32, 'max_actual_input_tokens': 16384,
            'max_seconds_per_provider': 300, 'min_cosine': .999,
            'batch_max_abs_difference': 1e-5}
    plan['sha256'] = digest(plan)
    return plan


def resume_tokenizer_checkpoint(checkpoint, records, fingerprint, total):
    '''Recover the verified committed prefix after an interrupted append.'''
    records_digest = hashlib.sha256()
    if not checkpoint.exists():
        return 0, 0, records_digest
    saved = read_json(checkpoint)
    require(isinstance(saved, dict), 'Corrupt tokenizer checkpoint')
    require(saved.get('fingerprint') == fingerprint,
            'Stale tokenizer checkpoint')
    completed = saved.get('checked')
    token_count = saved.get('token_count')
    require(type(completed) is int and 0 <= completed <= total
            and type(token_count) is int and token_count >= 0
            and records.is_file(), 'Corrupt tokenizer checkpoint')
    with records.open('r+b') as stream:
        # Older checkpoints omit records_bytes, so recover the boundary from
        # their committed row count. Never trust or parse an uncommitted tail.
        for _ in range(completed):
            row = stream.readline()
            require(row.endswith(b'\n'), 'Corrupt tokenizer checkpoint')
            records_digest.update(row)
        committed_bytes = stream.tell()
        saved_bytes = saved.get('records_bytes', committed_bytes)
        require(type(saved_bytes) is int and saved_bytes == committed_bytes
                and records_digest.hexdigest() == saved.get('records_sha256'),
                'Corrupt tokenizer checkpoint')
        stream.seek(0, os.SEEK_END)
        if stream.tell() != committed_bytes:
            stream.truncate(committed_bytes)
            stream.flush()
            os.fsync(stream.fileno())
    return completed, token_count, records_digest


def tokenize(run_dir, *, runtime_harness=None, vocab=None):
    started = time.monotonic()
    run = begin_gate(run_dir, 'tokenizer-parity')
    config = load_embed()
    corpus, queries = Path(run['binding']['corpus']), Path(run['binding']['queries'])
    manifest, passages = canonical_inputs(corpus, config, full_corpus=True)
    document, questions = frozen_inputs(corpus, queries, config)
    fixtures = read_json(ROOT / 'worker/fixtures/tokenizer_added_tokens.json')['cases']
    fixture_inputs = [model_input(row['template'], row['text']) for row in fixtures]
    fixture_inputs += [' '.join(['a'] * count) for count in (509, 510)]
    values = passages + questions + fixture_inputs
    labels = ([{'row': i, 'paper_id': row['paper_id'], 'chunk_index': row['chunk_index']}
               for i, row in enumerate(manifest['rows'])]
              + [{'query_id': row['id']} for row in document['queries']]
              + [{'fixture': i} for i in range(len(fixture_inputs))])
    checkpoint = Path(run_dir) / 'tokenizer-checkpoint.json'
    records = Path(run_dir) / 'tokenizer-inputs.jsonl'
    completed, token_count, records_digest = resume_tokenizer_checkpoint(
        checkpoint, records, run['fingerprint'], len(values))
    encoder = BgeEncoder(config, local_files_only=True)
    raw_report = Path(run_dir) / 'tokenizer-result.json'
    try:
        try:
            encoder._validated_ids([' '.join(['a'] * 511)])
        except BuildError as exc:
            require('truncate' in str(exc), 'Expected overlimit rejection')
        else:
            raise BuildError('Overlimit input was not rejected')
        with records.open('ab' if completed else 'wb') as stream:
            for first in range(completed, len(values), 128):
                require(time.monotonic() - started <= BUDGET_SECONDS['tokenizer-parity'], 'Tokenizer timeout')
                batch = values[first:first + 128]
                ids = encoder._validated_ids(batch, labels=labels[first:first + 128])
                for at, (text, tokens) in enumerate(zip(batch, ids), first):
                    encoded = (canonical_json({'id': str(at), 'template': '', 'text': text, 'ids': tokens}) + '\n').encode()
                    stream.write(encoded)
                    records_digest.update(encoded)
                    token_count += len(tokens)
                stream.flush()
                os.fsync(stream.fileno())
                completed = first + len(batch)
                write_json(checkpoint, {
                    'fingerprint': run['fingerprint'], 'checked': completed,
                    'records_sha256': records_digest.hexdigest(),
                    'records_bytes': stream.tell(), 'token_count': token_count,
                })
                print(canonical_json({'tokenizer_checked': completed, 'total': len(values)}), flush=True)
        remaining = BUDGET_SECONDS['tokenizer-parity'] - (time.monotonic() - started)
        require(remaining > 0, 'Tokenizer timeout before runtime parity')
        # Build from fingerprinted source; an arbitrary prebuilt bundle cannot
        # stand in for the production Worker tokenizer.
        runtime_harness = Path(runtime_harness or Path(run_dir) / 'tokenizer-parity.mjs').resolve()
        subprocess.run([str(ROOT / 'worker/node_modules/.bin/esbuild'),
                        str(ROOT / 'worker/probe-kernel/tokenizer-parity.ts'),
                        '--bundle', '--platform=node', '--format=esm',
                        '--outfile=' + str(runtime_harness)], check=True,
                       capture_output=True, text=True, timeout=min(30, remaining))
        remaining = BUDGET_SECONDS['tokenizer-parity'] - (time.monotonic() - started)
        require(remaining > 0, 'Tokenizer timeout before runtime parity')
        result = subprocess.run(['node', str(runtime_harness), str(records),
                                 str(vocab or config['_vocab_path'])],
                                capture_output=True, text=True, timeout=remaining)
        require(result.returncode == 0, 'Runtime tokenizer mismatch: ' + result.stdout[-4000:] + result.stderr[-1000:])
        runtime = json.loads(result.stdout)
        require(runtime.get('checked') == len(values) and runtime.get('mismatch_count') == 0
                and runtime.get('input_sha256') == records_digest.hexdigest(),
                'Incomplete runtime tokenizer parity')
        require(encoder.model is None, 'Tokenizer gate unexpectedly loaded weights')
        raw = {'status': 'PASS', 'count': len(values), 'passages': len(passages),
               'queries': len(questions), 'token_count': token_count,
               'fixture_count': len(fixture_inputs), 'overlimit_rejected': True,
               'records_sha256': sha(records.read_bytes()), 'runtime': runtime,
               'runtime_harness_sha256': sha(Path(runtime_harness).read_bytes()),
               'model_loaded': False, 'resumed_rows': completed - encoder.tokenizer_matches}
        write_json(raw_report, raw)
        return write_evidence(run_dir, 'tokenizer-parity',
                              checks={key: True for key in GATE_CHECKS['tokenizer-parity']},
                              measurements=raw, artifacts=[raw_report, records, runtime_harness],
                              elapsed_seconds=time.monotonic() - started)
    except (BuildError, OSError, ValueError, subprocess.SubprocessError) as exc:
        write_json(raw_report, {'status': 'FAIL', 'checked': completed, 'error': str(exc),
                                'model_loaded': encoder.model is not None})
        write_evidence(run_dir, 'tokenizer-parity', checks={}, measurements={},
                       artifacts=[raw_report], elapsed_seconds=time.monotonic() - started, status='FAIL')
        raise


def _tokenizer_child(run_dir, runtime_harness):
    try:
        tokenize(run_dir, runtime_harness=runtime_harness)
    except Exception as exc:
        print(str(exc), file=sys.stderr, flush=True)
        raise SystemExit(1) from None


def tokenize_supervised(run_dir, *, runtime_harness=None):
    # Revoke old evidence before the child exists, even if it stalls on import.
    run = begin_gate(run_dir, 'tokenizer-parity')
    process = multiprocessing.get_context('spawn').Process(
        target=_tokenizer_child, args=(str(run_dir), str(runtime_harness) if runtime_harness else None))
    process.start()
    process.join(BUDGET_SECONDS['tokenizer-parity'])
    if process.is_alive():
        process.terminate()
        process.join(5)
        if process.is_alive():
            process.kill()
            process.join(5)
        write_json(Path(run_dir) / 'tokenizer-timeout.json',
                   {'status': 'FAIL', 'fingerprint': run['fingerprint'],
                    'error': 'Hard600-second tokenizer-only timeout; checkpoint retained'})
        raise BuildError('Hard600-second tokenizer-only timeout; gate remains UNKNOWN')
    require(process.exitcode == 0, 'Tokenizer-only gate failed; inspect tokenizer-result.json')
    return evidence_path(run_dir, 'tokenizer-parity')


def numeric(run_dir, *, real_source):
    started = time.monotonic()
    run = begin_gate(run_dir, 'numeric-contracts')
    for gate in DEPENDENCIES['numeric-contracts']:
        validate_evidence(read_json(evidence_path(run_dir, gate)), run)
    run_dir = Path(run_dir).resolve()
    pytest_path, vitest_path = run_dir / 'numeric-pytest.xml', run_dir / 'numeric-vitest.json'
    real_path, raw_path = run_dir / 'numeric-real-vectors.json', run_dir / 'numeric-result.json'
    def execute(args, cwd=ROOT):
        remaining = BUDGET_SECONDS['numeric-contracts'] - (time.monotonic() - started)
        require(remaining > 0, 'Numeric gate timeout')
        result = subprocess.run(args, cwd=cwd, capture_output=True, text=True, timeout=remaining)
        require(result.returncode == 0, 'Numeric command failed: ' + result.stdout[-3000:] + result.stderr[-1000:])
        return result.returncode
    py_exit = execute([sys.executable, '-m', 'pytest', 'src/test_pack_full_search_probe.py',
                       'src/test_embed_real_search_probe.py', 'src/test_tokenizer_contract.py',
                       '-q', '--junitxml=' + str(pytest_path)])
    js_exit = execute([str(ROOT / 'worker/node_modules/.bin/vitest'), 'run',
                       'src/full-corpus-store.test.ts', 'src/full-search-index.test.ts',
                       'src/full-quality-contracts.test.ts', '--reporter=json',
                       '--outputFile=' + str(vitest_path)], cwd=ROOT / 'worker')
    execute([sys.executable, str(ROOT / 'src/probe_full_search_numeric.py'),
             '--source', str(Path(real_source).resolve()), '--out', str(real_path),
             '--work-dir', str(run_dir / ('numeric-work-' + str(time.time_ns())))])
    write_json(raw_path, {'kind': 'full-search-numeric-evidence', 'fingerprint': run['fingerprint'],
                          'pytest_exit_code': py_exit, 'vitest_exit_code': js_exit})
    return write_evidence(run_dir, 'numeric-contracts',
                          checks={key: True for key in GATE_CHECKS['numeric-contracts']},
                          measurements={'genuine_vectors': 390},
                          artifacts=[raw_path, pytest_path, vitest_path, real_path],
                          elapsed_seconds=time.monotonic() - started)


def record_geometry(run_dir, report):
    run = begin_gate(run_dir, 'geometry-memory')
    raw = read_json(report)
    if raw.get('status') != 'PASS':
        write_evidence(run_dir, 'geometry-memory', checks=raw.get('checks', {}),
                       measurements={'raw_status': raw.get('status')}, artifacts=[Path(report)],
                       elapsed_seconds=raw.get('elapsed_ms', 0) / 1000, status='FAIL')
        raise BuildError('Memory raw report is not PASS; FAIL evidence retained')
    require(raw.get('source_sha256') and all(run['binding']['code_sha256'].get(key) == value
            for key, value in raw['source_sha256'].items()), 'Memory report code hashes are stale or missing')
    bundle = Path(run_dir) / 'geometry-reviewed.mjs'
    require(build_memory_bundle(bundle) == raw.get('executed_bundle_sha256'),
            'Memory executed bundle differs from reviewed source')
    return write_evidence(run_dir, 'geometry-memory', checks=raw.get('checks', {}),
                          measurements={'peak_bytes': raw['summary']['peaks']['heap_plus_external']},
                          artifacts=[Path(report), Path(raw['packed_manifest_path']), bundle],
                          elapsed_seconds=raw['elapsed_ms'] / 1000)


def aggregate(run_dir):
    run = load_run(run_dir)
    failures, gates = {}, {}
    for gate in GATE_CHECKS:
        path = evidence_path(run_dir, gate)
        try:
            document = validate_evidence(read_json(path), run)
            gates[gate] = {'path': str(path.resolve()), 'sha256': sha(path.read_bytes())}
            for dependency in DEPENDENCIES[gate]:
                require(dependency in gates, f'{gate}: prerequisite {dependency} missing')
            if gate in ('local-canary', 'provider-compatibility'):
                require(document['canary_plan_sha256'] == canary_plan(run_dir)['sha256'],
                        'Canary plan changed')
        except (BuildError, OSError, ValueError, KeyError, TypeError) as exc:
            failures[gate] = str(exc)
            gates.pop(gate, None)
    now = datetime.now(timezone.utc).timestamp()
    certificate = {'schema_version': SCHEMA, 'kind': 'full-search-preflight-certificate',
                   'status': 'STOP' if failures else 'PASS', 'scope': SCOPE,
                   'created_at': utc_now(), 'expires_at_epoch': now + TTL_SECONDS,
                   'fingerprint': run['fingerprint'],
                   'snapshot_path': str((Path(run_dir) / 'snapshot.json').resolve()),
                   'snapshot_sha256': sha((Path(run_dir) / 'snapshot.json').read_bytes()),
                   'gates': gates, 'failures': failures,
                   'platform_cpu_gate': 'UNKNOWN', 'platform_memory_gate': 'UNKNOWN',
                   'heldout_quality_gate': 'UNKNOWN', 'production_ready': False}
    certificate['certificate_sha256'] = digest(certificate)
    write_json(Path(run_dir) / 'certificate.json', certificate)
    return certificate


def verify_certificate(path, *, corpus, queries, config=None):
    certificate = read_json(path)
    expected = certificate.pop('certificate_sha256', None)
    require(expected == digest(certificate), 'Certificate checksum mismatch')
    require(certificate.get('schema_version') == SCHEMA
            and certificate.get('kind') == 'full-search-preflight-certificate'
            and certificate.get('status') == 'PASS' and certificate.get('scope') == SCOPE,
            'Full encoding requires a PASS intended-path certificate')
    require(datetime.now(timezone.utc).timestamp() < certificate['expires_at_epoch'], 'Certificate expired')
    snapshot_path = Path(certificate['snapshot_path'])
    require(sha(snapshot_path.read_bytes()) == certificate['snapshot_sha256'], 'Snapshot changed')
    run = load_run(snapshot_path.parent, refresh=False)
    require(str(Path(corpus).resolve()) == run['binding']['corpus']
            and str(Path(queries).resolve()) == run['binding']['queries'], 'Certificate input paths differ')
    require(current_binding(corpus, queries, config) == run['binding']
            and certificate['fingerprint'] == run['fingerprint'], 'Certificate is stale')
    require(set(certificate['gates']) == set(GATE_CHECKS), 'Certificate is missing mandatory gates')
    for gate, entry in certificate['gates'].items():
        require(sha(Path(entry['path']).read_bytes()) == entry['sha256'], 'Gate report changed')
        report = validate_evidence(read_json(entry['path']), run)
        require(report['gate'] == gate, 'Gate report substituted')
        if gate in ('local-canary', 'provider-compatibility'):
            require(report['canary_plan_sha256'] == canary_plan(snapshot_path.parent)['sha256'],
                    'Canary plan changed')
    return certificate


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    create = commands.add_parser('snapshot')
    create.add_argument('--corpus', type=Path, required=True)
    create.add_argument('--queries', type=Path, required=True)
    create.add_argument('--out', type=Path, required=True)
    frozen = commands.add_parser('verify-queries')
    frozen.add_argument('--corpus', type=Path, required=True)
    frozen.add_argument('--queries', type=Path, required=True)
    frozen.add_argument('--pin', type=Path, required=True)
    tokens = commands.add_parser('tokenize')
    tokens.add_argument('--run', type=Path, required=True)
    tokens.add_argument('--runtime-harness', type=Path,
                        help='Output path for a bundle built from current source')
    numbers = commands.add_parser('numeric')
    numbers.add_argument('--run', type=Path, required=True)
    numbers.add_argument('--real-source', type=Path, required=True)
    geometry = commands.add_parser('record-geometry')
    geometry.add_argument('--run', type=Path, required=True)
    geometry.add_argument('--report', type=Path, required=True)
    record = commands.add_parser('record')
    record.add_argument('--run', type=Path, required=True)
    record.add_argument('--report', type=Path, required=True)
    for name in ('aggregate', 'canary-plan'):
        command = commands.add_parser(name)
        command.add_argument('--run', type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == 'snapshot':
            result = snapshot(args.corpus, args.queries, args.out)
        elif args.command == 'verify-queries':
            result = verify_frozen_queries(args.corpus, args.queries, args.pin)
        elif args.command == 'tokenize':
            result = {'report': str(tokenize_supervised(args.run, runtime_harness=args.runtime_harness))}
        elif args.command == 'numeric':
            result = {'report': str(numeric(args.run, real_source=args.real_source))}
        elif args.command == 'record-geometry':
            result = {'report': str(record_geometry(args.run, args.report))}
        elif args.command == 'record':
            report = read_json(args.report)
            validate_evidence(report, load_run(args.run))
            for dependency in DEPENDENCIES[report['gate']]:
                validate_evidence(read_json(evidence_path(args.run, dependency)), load_run(args.run, refresh=False))
            write_json(evidence_path(args.run, report['gate']), report)
            result = {'recorded': report['gate']}
        elif args.command == 'aggregate':
            result = aggregate(args.run)
        else:
            result = canary_plan(args.run)
        print(canonical_json(result), flush=True)
        return 1 if result.get('status') == 'STOP' else 0
    except (BuildError, OSError, ValueError, KeyError, TypeError,
            importlib.metadata.PackageNotFoundError, subprocess.SubprocessError) as exc:
        parser.exit(1, str(exc) + '\n')


if __name__ == '__main__':
    raise SystemExit(main())
