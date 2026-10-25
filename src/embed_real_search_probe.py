'''Encode the isolated canonical subset with pinned BGE FP32 CLS embeddings.

The normal CLI never creates synthetic vectors. Model weights are loaded only
from the pinned public revision, with safetensors and remote code disabled.
The output is an experiment artifact; local encoding does not establish
compatibility with Workers AI or authorize a production publication.
'''

from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import math
from pathlib import Path
import struct
import time

from build_agent_index import (
    BuildError, WordPieceTokenizer, build_signature, canonical_json,
    embedding_signature, input_hash, load_embed, model_input, sha256_hex,
    vector_id,
)

MODEL_ID = 'BAAI/bge-base-en-v1.5'
MODEL_REVISION = 'a5beb1e3e68b9ab74eb54cfd186867f64f240e1a'
DIMENSIONS = 768
IMPLEMENTATION = 'canonical-wordpiece-bge-cls-fp32-v1'
VECTOR_FILE = 'vectors.f32'


def atomic_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_bytes(data)
    temporary.replace(path)


def checked_path(root: Path, name: str) -> Path:
    if (not isinstance(name, str) or not name or '\\' in name
            or Path(name).is_absolute()
            or any(part in ('', '.', '..') for part in name.split('/'))):
        raise BuildError('Invalid artifact path')
    path = root / name
    if not path.resolve().is_relative_to(root.resolve()):
        raise BuildError('Artifact path escapes the subset directory')
    return path


def checked_asset(root: Path, manifest: dict, name: str) -> bytes:
    expected = manifest['files'].get(name)
    if not isinstance(expected, str) or len(expected) != 64:
        raise BuildError(f'Artifact hash missing: {name}')
    data = checked_path(root, name).read_bytes()
    if hashlib.sha256(data).hexdigest() != expected:
        raise BuildError(f'Artifact checksum mismatch: {name}')
    return data


def canonical_inputs(root: Path, config: dict) -> tuple[dict, list[str]]:
    '''Validate complete-paper coverage and return exact model input strings.'''
    manifest = json.loads((root / 'probe.json').read_text(encoding='utf-8'))
    if (manifest.get('schema_version') != 1
            or manifest.get('kind') != 'real-subset'
            or manifest.get('synthetic') is not False
            or manifest.get('slot') != 'real-probe'
            or manifest.get('dimensions') != DIMENSIONS
            or manifest.get('embedding_signature') != embedding_signature(config)
            or manifest.get('build_signature') != build_signature(config)):
        raise BuildError('Subset does not match the canonical embedding config')
    rows = manifest.get('rows')
    paper_ids = manifest.get('paper_ids')
    if (not isinstance(rows, list) or not 1 <= len(rows) <= 500
            or not all(isinstance(row, dict) for row in rows)
            or manifest.get('passage_count') != len(rows)
            or not isinstance(paper_ids, list)
            or not all(isinstance(value, str) for value in paper_ids)
            or paper_ids != sorted(set(paper_ids))
            or not isinstance(manifest.get('files'), dict)):
        raise BuildError('Invalid bounded subset manifest')
    for name in manifest['files']:
        checked_asset(root, manifest, name)
    release_id = manifest.get('release_id')
    if (not isinstance(release_id, str) or len(release_id) != 64
            or any(char not in '0123456789abcdef' for char in release_id)):
        raise BuildError('Invalid release identity')
    prefix = f'releases/{release_id}'
    graph = json.loads(checked_asset(root, manifest, prefix + '/graph.json'))
    if sorted(graph.get('nodes', {})) != paper_ids:
        raise BuildError('Graph and subset paper IDs differ')
    papers = {}
    expected_rows = []
    for paper_id in paper_ids:
        name = prefix + '/papers/' + sha256_hex(paper_id) + '.json'
        paper = json.loads(checked_asset(root, manifest, name))
        if (paper.get('paper_id') != paper_id
                or not isinstance(paper.get('text'), str)
                or not isinstance(paper.get('chunks'), list)):
            raise BuildError('Malformed canonical paper')
        if not all(isinstance(chunk, dict) for chunk in paper['chunks']):
            raise BuildError('Malformed canonical chunk')
        papers[paper_id] = paper
        for chunk in paper['chunks']:
            expected_rows.append((paper_id, chunk.get('index')))
    if [(row.get('paper_id'), row.get('chunk_index')) for row in rows] != expected_rows:
        raise BuildError('Rows must cover every canonical paper chunk in order')
    tokenizer = WordPieceTokenizer(config)
    inputs = []
    for row in rows:
        paper_id, index = row['paper_id'], row['chunk_index']
        if (not isinstance(index, int) or isinstance(index, bool)
                or not 0 <= index < len(papers[paper_id]['chunks'])):
            raise BuildError('Invalid canonical chunk index')
        paper = papers[paper_id]
        chunk = paper['chunks'][index]
        start, end = chunk.get('start'), chunk.get('end')
        if (not all(isinstance(value, int) and not isinstance(value, bool)
                    for value in (start, end))
                or not 0 <= start < end <= len(paper['text'])):
            raise BuildError('Invalid code-point chunk offsets')
        piece = paper['text'][start:end]
        if (row.get('id') != vector_id('real-probe', paper_id, index)
                or any(row.get(key) != chunk.get(key) for key in (
                    'start', 'end', 'token_count', 'content_hash', 'input_hash'))
                or sha256_hex(piece) != row['content_hash']
                or input_hash(config, piece, manifest['embedding_signature'])
                != row['input_hash']):
            raise BuildError('Canonical passage hash or mapping mismatch')
        tokens = tokenizer.token_ids(config['passage_template'], piece)
        if (len(tokens) != row['token_count']
                or len(tokens) > config['max_input_tokens']):
            raise BuildError('Canonical passage token count mismatch')
        inputs.append(model_input(config['passage_template'], piece))
    return manifest, inputs


def unit_vector(values, dimensions: int = DIMENSIONS) -> list[float]:
    if (len(values) != dimensions
            or any(isinstance(value, bool)
                   or not isinstance(value, (int, float))
                   or not math.isfinite(value) for value in values)):
        raise BuildError('Embedding must contain finite numeric dimensions')
    norm = math.sqrt(math.fsum(value * value for value in values))
    if not math.isfinite(norm) or norm <= 0:
        raise BuildError('Embedding has a zero or invalid norm')
    normalized = [value / norm for value in values]
    # Round explicitly to the bytes the Worker will read, not Python doubles.
    raw = struct.pack(f'<{dimensions}f', *normalized)
    return list(struct.unpack(f'<{dimensions}f', raw))


def cls_vectors(hidden_states) -> list[list[float]]:
    '''Use the first token only, never mean pooling over the sequence.'''
    if any(not sequence for sequence in hidden_states):
        raise BuildError('The model returned an empty token sequence')
    return [unit_vector(sequence[0]) for sequence in hidden_states]


def vector_bytes(vector) -> bytes:
    if (len(vector) != DIMENSIONS
            or any(isinstance(value, bool)
                   or not isinstance(value, (int, float))
                   or not math.isfinite(value) for value in vector)):
        raise BuildError('Invalid vector dimensions or values')
    norm = math.sqrt(math.fsum(value * value for value in vector))
    if abs(norm - 1) > 1e-4:
        raise BuildError('Embedding is not L2 normalized')
    return struct.pack(f'<{DIMENSIONS}f', *vector)


def cached_vector(path: Path) -> list[float] | None:
    if not path.exists():
        return None
    raw = path.read_bytes()
    if len(raw) != DIMENSIONS * 4:
        raise BuildError(f'Invalid embedding cache length: {path.name}')
    vector = list(struct.unpack(f'<{DIMENSIONS}f', raw))
    vector_bytes(vector)
    return vector


class BgeEncoder:
    '''CPU-only, FP32 encoder using canonical IDs and pinned model weights.'''

    def __init__(self, config: dict, *, threads: int = 4,
                 local_files_only: bool = False):
        if (config['tokenizer']['id'] != MODEL_ID
                or config['tokenizer']['revision'] != MODEL_REVISION
                or config['pooling'] != 'cls'
                or config['dimensions'] != DIMENSIONS):
            raise BuildError('This encoder only supports the pinned BGE config')
        self.config = config
        self.tokenizer = WordPieceTokenizer(config)
        self.threads = threads
        self.local_files_only = local_files_only
        self.model = None
        self.hf_tokenizer = None
        self.tokenizer_matches = 0
        self.identity = {
            'implementation': IMPLEMENTATION,
            'model_id': MODEL_ID, 'model_revision': MODEL_REVISION,
            'pooling': 'cls', 'normalization': 'l2', 'dtype': 'float32',
            'byte_order': 'little', 'dimensions': DIMENSIONS,
            'device': 'cpu', 'attention_implementation': 'eager',
            'embedding_signature': embedding_signature(config),
            'versions': {name: importlib.metadata.version(name)
                         for name in ('torch', 'transformers')},
        }

    def _load(self):
        if self.model is not None:
            return
        import torch
        from transformers import AutoModel, AutoTokenizer

        torch.set_num_threads(self.threads)
        self.hf_tokenizer = AutoTokenizer.from_pretrained(
            MODEL_ID, revision=MODEL_REVISION, use_fast=False,
            trust_remote_code=False, local_files_only=self.local_files_only,
        )
        self.model = AutoModel.from_pretrained(
            MODEL_ID, revision=MODEL_REVISION, use_safetensors=True,
            trust_remote_code=False, torch_dtype=torch.float32,
            attn_implementation='eager',
            local_files_only=self.local_files_only,
        ).to('cpu').float().eval()
        if (self.model.config.hidden_size != DIMENSIONS
                or self.model.config.max_position_embeddings < 512
                or self.model.config._commit_hash != MODEL_REVISION):
            raise BuildError('Downloaded model identity or shape mismatch')

    def __call__(self, inputs: list[str]) -> list[list[float]]:
        self._load()
        import torch

        ids = [self.tokenizer.token_ids('', text) for text in inputs]
        if any(len(row) > self.config['max_input_tokens'] for row in ids):
            raise BuildError('Refusing to truncate a canonical model input')
        expected = self.hf_tokenizer(
            inputs, add_special_tokens=True, truncation=False,
        )['input_ids']
        if ids != expected:
            raise BuildError('Canonical and pinned Hugging Face token IDs differ')
        self.tokenizer_matches += len(inputs)
        width = max(map(len, ids))
        pad = self.hf_tokenizer.pad_token_id
        input_ids = torch.tensor([
            row + [pad] * (width - len(row)) for row in ids
        ], dtype=torch.long)
        attention_mask = torch.tensor([
            [1] * len(row) + [0] * (width - len(row)) for row in ids
        ], dtype=torch.long)
        with torch.inference_mode():
            result = self.model(
                input_ids=input_ids, attention_mask=attention_mask,
                token_type_ids=torch.zeros_like(input_ids),
            )
            # Convert only CLS to Python; never materialize all hidden tokens.
            first_tokens = result.last_hidden_state[:, :1, :].float().tolist()
        return cls_vectors(first_tokens)


def encode_probe(root: Path, encoder, config: dict, *, cache_dir: Path,
                 batch_size: int = 8, progress: bool = True) -> dict:
    if not 1 <= batch_size <= 32:
        raise BuildError('Use batch size 1..32')
    manifest, inputs = canonical_inputs(root, config)
    identity = encoder.identity
    signature = sha256_hex(canonical_json(identity))
    vectors = [None] * len(inputs)
    missing = []
    started = time.monotonic()
    for index, row in enumerate(manifest['rows']):
        path = cache_dir / signature / (row['input_hash'] + '.f32')
        vectors[index] = cached_vector(path)
        if vectors[index] is None:
            missing.append(index)
    for offset in range(0, len(missing), batch_size):
        indices = missing[offset:offset + batch_size]
        batch = encoder([inputs[index] for index in indices])
        if len(batch) != len(indices):
            raise BuildError('Encoder returned the wrong batch size')
        for index, vector in zip(indices, batch):
            raw = vector_bytes(vector)
            vectors[index] = list(struct.unpack(f'<{DIMENSIONS}f', raw))
            path = cache_dir / signature / (
                manifest['rows'][index]['input_hash'] + '.f32')
            atomic_bytes(path, raw)
        if progress:
            completed = min(offset + len(indices), len(missing))
            print(f'Encoded {completed}/{len(missing)} new passages; '
                  f'{len(inputs) - len(missing)} cached', flush=True)
    raw = b''.join(vector_bytes(vector) for vector in vectors)
    digest = hashlib.sha256(raw).hexdigest()
    atomic_bytes(root / VECTOR_FILE, raw)
    manifest['files'][VECTOR_FILE] = digest
    manifest['embeddings'] = {
        **identity, 'encoder_signature': signature,
        'path': VECTOR_FILE, 'sha256': digest, 'count': len(vectors),
        'workers_ai_compatibility': 'unverified',
    }
    atomic_bytes(root / 'probe.json',
                 (canonical_json(manifest) + '\n').encode('utf-8'))
    report = {
        'release_id': manifest['release_id'], 'passage_count': len(inputs),
        'encoded': len(missing), 'cached': len(inputs) - len(missing),
        'elapsed_seconds': time.monotonic() - started,
        'vectors_sha256': digest, 'encoder_signature': signature,
        'model_inputs_checked_against_hf_tokenizer': getattr(
            encoder, 'tokenizer_matches', None),
        'max_norm_error': max(abs(math.sqrt(math.fsum(
            value * value for value in vector)) - 1) for vector in vectors),
        'encoder': identity,
        'workers_ai_compatibility': 'unverified',
    }
    if progress:
        print(json.dumps(report, sort_keys=True), flush=True)
    return report


def encode_queries(root: Path, encoder, config: dict, output: Path) -> dict:
    '''Local-only query vectors for production-contract integration tests.'''
    manifest, _ = canonical_inputs(root, config)
    embeddings = manifest.get('embeddings')
    if not isinstance(embeddings, dict):
        raise BuildError('Encode passage vectors before integration queries')
    queries = manifest.get('queries')
    if not isinstance(queries, list) or not 1 <= len(queries) <= 32:
        raise BuildError('Expected 1..32 predefined integration queries')
    texts = []
    for row in queries:
        query = row.get('query')
        if not isinstance(query, str) or not 0 < len(query) <= 2000:
            raise BuildError('Invalid integration query')
        texts.append(model_input(config['query_template'], query))
    vectors = encoder(texts)
    if len(vectors) != len(queries):
        raise BuildError('Encoder returned the wrong query batch size')
    for vector in vectors:
        vector_bytes(vector)
    doc = {
        'kind': 'local-real-query-vectors',
        'release_id': manifest['release_id'],
        'embedding_signature': manifest['embedding_signature'],
        'encoder_signature': sha256_hex(canonical_json(encoder.identity)),
        'vectors_sha256': embeddings.get('sha256'),
        'workers_ai_compatibility': 'unverified',
        'queries': [{**row, 'vector': vector}
                    for row, vector in zip(queries, vectors)],
    }
    atomic_bytes(output, (canonical_json(doc) + '\n').encode('utf-8'))
    return doc


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=Path('agent_real_probe'))
    parser.add_argument('--cache-dir', type=Path,
                        default=Path('.cache/real-probe-embeddings'))
    parser.add_argument('--batch-size', type=int, default=8)
    parser.add_argument('--threads', type=int, default=4)
    parser.add_argument('--local-files-only', action='store_true')
    parser.add_argument('--query-vectors', type=Path)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args(argv)
    if not 1 <= args.batch_size <= 32 or not 1 <= args.threads <= 16:
        parser.error('Use batch size 1..32 and CPU threads 1..16')
    try:
        config = load_embed()
        encoder = BgeEncoder(config, threads=args.threads,
                             local_files_only=args.local_files_only)
        report = encode_probe(args.out, encoder, config,
                              cache_dir=args.cache_dir,
                              batch_size=args.batch_size)
        if args.query_vectors:
            checked_before = encoder.tokenizer_matches
            queries = encode_queries(args.out, encoder, config,
                                     args.query_vectors)
            report['local_queries_encoded'] = len(queries['queries'])
            report['query_inputs_checked_against_hf_tokenizer'] = (
                encoder.tokenizer_matches - checked_before)
        if args.report:
            atomic_bytes(args.report,
                         (canonical_json(report) + '\n').encode('utf-8'))
    except (BuildError, OSError, ValueError, KeyError, TypeError,
            importlib.metadata.PackageNotFoundError) as exc:
        parser.exit(1, str(exc) + '\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
