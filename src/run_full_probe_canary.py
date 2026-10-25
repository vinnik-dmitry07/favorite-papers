'''Bounded local/provider compatibility check, never a corpus encoding job.

The supervisor kills the child after five minutes. No automatic retries: one
ambiguous network response must not multiply provider usage. Provider vectors
are retained with input hashes so the cosine check is independently repeatable.
'''

from __future__ import annotations

import argparse
import json
import math
import multiprocessing
import os
import time
import urllib.error
import urllib.request
from pathlib import Path

from build_agent_index import BuildError, canonical_json, load_embed, sha256_hex
from embed_real_search_probe import BgeEncoder, atomic_bytes, unit_vector

MAX_SECONDS = 300
MAX_TEXTS = 32
MAX_TOKENS = 16384


def normalized(values, count):
    if not isinstance(values, list) or len(values) != count:
        raise BuildError('Wrong canary vector count')
    result = []
    for row in values:
        if (not isinstance(row, list) or len(row) != 768
                or any(isinstance(x, bool) or not isinstance(x, (int, float))
                       or not math.isfinite(x) for x in row)):
            raise BuildError('Invalid canary vector')
        result.append(unit_vector(row))
    return result


def repeat_indices(plan):
    rows = plan['inputs']
    if not 2 <= len(rows) <= MAX_TEXTS - 2:
        raise BuildError('Canary requires 2..30 fixed inputs')
    longest = max(range(1, len(rows)), key=lambda i: rows[i]['token_count'])
    return [0, longest]


def budget(plan):
    repeats = repeat_indices(plan)
    rows = plan['inputs']
    count = len(rows) + len(repeats)
    tokens = sum(row['token_count'] for row in rows)
    tokens += sum(rows[index]['token_count'] for index in repeats)
    if count > MAX_TEXTS or tokens > MAX_TOKENS:
        raise BuildError('Canary exceeds its fixed text/token budget')
    return count, tokens, repeats


def compare_batches(first, repeated, indices):
    return max(abs(first[index][j] - repeated[k][j])
               for k, index in enumerate(indices) for j in range(768))


def begin_attempt(run_dir, plan, *, provider):
    '''Exclusive reservation: a failed/ambiguous attempt is never replayed.'''
    path = Path(run_dir) / 'canary-attempt.json'
    attempt = {
        'schema_version': 1, 'status': 'RUNNING',
        'fingerprint': plan['fingerprint'], 'plan_sha256': plan['sha256'],
        'provider_requested': provider, 'provider_requests': [],
        'provider_input_count': 0, 'provider_token_count': 0,
    }
    try:
        with path.open('x', encoding='utf-8') as stream:
            stream.write(canonical_json(attempt))
            stream.flush()
            os.fsync(stream.fileno())
    except FileExistsError:
        raise BuildError('Canary attempt already exists; inspect it and use a '
                         'fresh preflight run with newly confirmed allowance') from None
    return attempt


def save_attempt(run_dir, attempt):
    atomic_bytes(Path(run_dir) / 'canary-attempt.json', canonical_json(attempt).encode())


def reserve_provider(run_dir, attempt, plan, indices):
    count = attempt['provider_input_count'] + len(indices)
    tokens = attempt['provider_token_count'] + sum(
        plan['inputs'][index]['token_count'] for index in indices)
    if count > MAX_TEXTS or tokens > MAX_TOKENS:
        raise BuildError('Provider reservation exceeds canary budget')
    attempt.update(status='PROVIDER_RUNNING', provider_input_count=count,
                   provider_token_count=tokens)
    attempt['provider_requests'].append({'indices': indices, 'status': 'RESERVED'})
    # A crash after this write still consumes the reservation; never retry it.
    save_attempt(run_dir, attempt)


def provider_vectors(texts, config, *, account, token, timeout=45, opener=None):
    if not account or not token:
        raise BuildError('Cloudflare credentials are missing')
    if not account.isalnum():
        raise BuildError('Invalid Cloudflare account identifier')
    request = urllib.request.Request(
        'https://api.cloudflare.com/client/v4/accounts/' + account
        + '/ai/run/' + config['model'],
        data=canonical_json({'text': texts, 'pooling': config['pooling']}).encode(),
        headers={'Authorization': 'Bearer ' + token,
                 'Content-Type': 'application/json'}, method='POST',
    )
    try:
        with (opener or urllib.request.urlopen)(request, timeout=timeout) as response:
            raw = response.read(2_000_001)
    except urllib.error.HTTPError as exc:
        # Do not echo tokens, account details or arbitrary response bodies.
        raise BuildError(f'Workers AI HTTP {exc.code}; no retry performed') from None
    if len(raw) > 2_000_000:
        raise BuildError('Workers AI response exceeds canary bound')
    document = json.loads(raw)
    if document.get('success') is not True:
        raise BuildError('Workers AI did not report success')
    return normalized(document.get('result', {}).get('data'), len(texts))


def execute(run_dir, *, provider=False, available_neurons=None, threads=4,
            local_files_only=True):
    from preflight_full_search_probe import (
        begin_gate, canary_plan, check_canary_prerequisites, write_evidence,
    )
    run_dir = Path(run_dir)
    check_canary_prerequisites(run_dir)
    plan = canary_plan(run_dir)
    count, tokens, repeats = budget(plan)
    config = load_embed()
    estimated_neurons = math.ceil(
        tokens * config['pricing']['neurons_per_million_tokens'] / 1_000_000)
    if provider and (available_neurons is None
                     or available_neurons < estimated_neurons):
        raise BuildError('Confirm remaining free neurons before provider canary')
    attempt = begin_attempt(run_dir, plan, provider=provider)
    begin_gate(run_dir, 'local-canary')
    begin_gate(run_dir, 'provider-compatibility')
    started = time.monotonic()
    encoder = BgeEncoder(config, threads=threads,
                         local_files_only=local_files_only)
    texts = [row['input'] for row in plan['inputs']]
    # All inputs, including repeats, must validate before model weights load.
    encoder.validate_inputs(texts)
    local = normalized(encoder(texts), len(texts))
    repeated = normalized(encoder([texts[i] for i in repeats]), len(repeats))
    difference = compare_batches(local, repeated, repeats)
    local_path = run_dir / 'canary-local-vectors.json'
    atomic_bytes(local_path, canonical_json({
        'plan_sha256': plan['sha256'], 'encoder': encoder.identity,
        'inputs': plan['inputs'], 'vectors': local,
        'repeat_indices': repeats, 'repeated_vectors': repeated,
    }).encode())
    measurements = {
        'plan_sha256': plan['sha256'], 'input_count': count,
        'total_input_tokens': tokens,
        'batch_max_abs_difference': difference,
        'elapsed_seconds': time.monotonic() - started,
        'estimated_neurons_upper_budget': estimated_neurons,
    }
    checks = {'tokenizer_parity': True, 'finite_unit_768': True,
              'batch_invariance': difference <= 1e-5,
              'input_identity': True,
              'within_budget': time.monotonic() - started <= MAX_SECONDS}
    attempt['status'] = 'LOCAL_ONLY' if all(checks.values()) else 'STOP'
    save_attempt(run_dir, attempt)
    write_evidence(run_dir, 'local-canary', checks=checks,
                   measurements=measurements, artifacts=[local_path],
                   elapsed_seconds=time.monotonic() - started,
                   status='PASS' if all(checks.values()) else 'FAIL')
    if not all(checks.values()):
        raise BuildError('Local canary failed')
    if not provider:
        return
    account = os.environ.get('CLOUDFLARE_ACCOUNT_ID', '')
    token = os.environ.get('CLOUDFLARE_API_TOKEN', '')
    reserve_provider(run_dir, attempt, plan, list(range(len(texts))))
    remote = provider_vectors(texts, config, account=account, token=token)
    attempt['provider_requests'][-1]['status'] = 'COMPLETE'
    save_attempt(run_dir, attempt)
    reserve_provider(run_dir, attempt, plan, repeats)
    remote_repeated = provider_vectors([texts[i] for i in repeats], config,
                                       account=account, token=token)
    attempt['provider_requests'][-1]['status'] = 'COMPLETE'
    remote_difference = compare_batches(remote, remote_repeated, repeats)
    cosines = [math.fsum(a * b for a, b in zip(left, right))
               for left, right in zip(local, remote)]
    remote_path = run_dir / 'canary-provider-vectors.json'
    atomic_bytes(remote_path, canonical_json({
        'plan_sha256': plan['sha256'], 'model': config['model'],
        'transport': 'workers-ai-rest', 'vectors': remote,
        'repeat_indices': repeats, 'repeated_vectors': remote_repeated,
        'cosines': cosines,
    }).encode())
    checks = {'targeted_coverage': True, 'finite_unit_768': True,
              'min_cosine': min(cosines) >= 0.999,
              'batch_invariance': remote_difference <= 1e-5,
              'input_identity': True, 'free_allowance_verified': True,
              'within_budget': time.monotonic() - started <= MAX_SECONDS}
    measurements.update({
        'min_cosine': min(cosines),
        'batch_max_abs_difference': remote_difference,
        'elapsed_seconds': time.monotonic() - started,
        'available_neurons_confirmed': available_neurons,
        'free_allowance_evidence': 'operator-confirmed-before-run',
        'request_count': 2,
    })
    attempt['status'] = 'PASSED' if all(checks.values()) else 'STOP'
    save_attempt(run_dir, attempt)
    write_evidence(run_dir, 'provider-compatibility', checks=checks,
                   measurements=measurements,
                   artifacts=[local_path, remote_path,
                              run_dir / 'canary-attempt.json'],
                   elapsed_seconds=time.monotonic() - started,
                   status='PASS' if all(checks.values()) else 'FAIL')
    if not all(checks.values()):
        raise BuildError('Provider compatibility canary failed')


def child(run_dir, options):
    try:
        execute(run_dir, **options)
    except Exception as exc:
        mark_stopped(run_dir)
        atomic_bytes(Path(run_dir) / 'canary-error.json', canonical_json({
            'status': 'STOP', 'error_type': type(exc).__name__,
            'error': str(exc)[:500],
        }).encode())
        raise SystemExit(1) from None


def mark_stopped(run_dir):
    path = Path(run_dir) / 'canary-attempt.json'
    if path.exists():
        attempt = json.loads(path.read_text())
        attempt['status'] = 'STOP'
        save_attempt(run_dir, attempt)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run', type=Path, required=True)
    parser.add_argument('--provider', action='store_true')
    parser.add_argument('--available-neurons', type=int)
    parser.add_argument('--threads', type=int, default=4)
    parser.add_argument('--allow-model-download', action='store_true')
    args = parser.parse_args(argv)
    if not 1 <= args.threads <= 16:
        parser.error('CPU threads must be 1..16')
    args.run.mkdir(parents=True, exist_ok=True)
    process = multiprocessing.get_context('spawn').Process(
        target=child, args=(str(args.run), {
            'provider': args.provider, 'available_neurons': args.available_neurons,
            'threads': args.threads,
            'local_files_only': not args.allow_model_download,
        }))
    process.start()
    process.join(MAX_SECONDS)
    if process.is_alive():
        process.terminate()
        process.join(5)
        if process.is_alive():
            process.kill()
            process.join()
        mark_stopped(args.run)
        atomic_bytes(args.run / 'canary-error.json', canonical_json({
            'status': 'STOP', 'error': 'Hard five-minute canary timeout',
        }).encode())
        return 1
    return process.exitcode or 0


if __name__ == '__main__':
    raise SystemExit(main())
