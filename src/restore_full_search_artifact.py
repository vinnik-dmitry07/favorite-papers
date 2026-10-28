'''Restore one authenticated historical search artifact for read-only analysis.

This command reconstructs assets and reuses retained vectors. It never loads an
embedding model, calls a provider, or issues an inference/deployment certificate.
'''

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import zipfile

from build_agent_index import BuildError, load_embed, read_texts
from build_full_search_probe import build_full_corpus, write_full_corpus
from common import ROOT
from pack_full_search_probe import pack

RUN_ID = 40448979121
ARTIFACT_ID = 12715563729
SOURCE_COMMIT = 'fa3f4ec3724949a98b2b510949cf8efe405baf8a'
ARTIFACT_SHA256 = (
    '8f3fd29b369ae41f1474e052e0eef931a23ca7437c99640adbc6bc13d519c65c'
)
SOURCE_PATHS = (
    'src/common.py', 'src/build_agent_index.py',
    'src/build_fulltext_search.py', 'src/build_full_search_probe.py',
    'src/pack_full_search_probe.py', 'src/embed_real_search_probe.py',
    'src/evaluate_full_search_probe.py', 'worker/embed.json',
    'worker/tokenizer/vocab.txt', 'worker/src/full-search-index.ts',
    'worker/src/static-search-int8.ts', 'worker/probe-kernel/scan.wat',
    'worker/probe-kernel/scan.wasm', 'worker/probe-kernel/build.mjs',
    'worker/package-lock.json',
)


def file_hash(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def require(condition, message):
    if not condition:
        raise BuildError(message)


def restore(archive, output):
    archive, output = Path(archive), Path(output)
    require(file_hash(archive) == ARTIFACT_SHA256,
            'Archive differs from the authenticated GitHub artifact')
    require(not output.exists() or not any(output.iterdir()),
            'Restoration output must be empty')
    with zipfile.ZipFile(archive) as source:
        require(len(source.namelist()) == len(set(source.namelist())),
                'Duplicate archive members')

        def read(name):
            info = source.getinfo(name)
            require(info.file_size <= 150_000_000, 'Oversized archive member')
            return source.read(name)

        snapshot = json.loads(read('full-probe-reports/preflight/snapshot.json'))
        require(snapshot['binding']['head'] == SOURCE_COMMIT,
                'Historical source commit differs')
        hashes = snapshot['binding']['code_sha256']
        for relative in SOURCE_PATHS:
            require(file_hash(ROOT / relative) == hashes.get(relative),
                    'Historical implementation changed: ' + relative)

        manifest_bytes = read('agent_full_probe/probe.json')
        original = json.loads(manifest_bytes)
        graph_bytes = (ROOT / 'assets/graph.json').read_bytes()
        require(hashlib.sha256(graph_bytes).hexdigest()
                == original['source_graph_sha256'], 'Source graph changed')
        graph = json.loads(graph_bytes)
        print('Rebuilding canonical assets without inference...', flush=True)
        release, manifest = build_full_corpus(
            graph, read_texts(graph['nodes']), load_embed(),
            source_path=original['source_path'], source_sha=SOURCE_COMMIT,
            source_graph_sha256=original['source_graph_sha256'],
        )
        corpus = output / 'corpus'
        rebuilt = write_full_corpus(release, manifest, corpus)
        before_encoding = {**original, 'embeddings': None,
                           'files': {key: value for key, value
                                     in original['files'].items()
                                     if key != 'vectors.f32'}}
        require(rebuilt == before_encoding,
                'Rebuilt canonical metadata or asset hashes differ')

        def copy(name, target):
            target.parent.mkdir(parents=True, exist_ok=True)
            require(source.getinfo(name).file_size <= 150_000_000,
                    'Oversized retained file')
            with source.open(name) as reader, target.open('wb') as writer:
                shutil.copyfileobj(reader, writer, 1024 * 1024)

        copy('agent_full_probe/vectors.f32', corpus / 'vectors.f32')
        require(file_hash(corpus / 'vectors.f32')
                == original['embeddings']['sha256'], 'Corpus vector hash differs')
        (corpus / 'probe.json').write_bytes(manifest_bytes)
        copy('agent_full_probe/quality-combined-frozen.json',
             corpus / 'quality-combined-frozen.json')
        for name in ('query-vectors.f32', 'query-vectors.f32.json'):
            copy('full-probe-reports/' + name, output / name)
        query_metadata = json.loads((output / 'query-vectors.f32.json').read_bytes())
        require(file_hash(output / 'query-vectors.f32')
                == query_metadata['vectors_sha256'], 'Query vector hash differs')
        query_hash = file_hash(corpus / 'quality-combined-frozen.json')
        require(query_hash == query_metadata['query_manifest_sha256']
                and query_metadata['encoder_signature']
                == original['embeddings']['encoder_signature'],
                'Query or encoder identity differs')
        require(original['passage_count'] == 40575
                and query_metadata['count'] == 2064, 'Unexpected replay dimensions')

        print('Repacking retained vectors and comparing historical bytes...',
              flush=True)
        pack(corpus, output / 'runtime')
        packed_bytes = (output / 'runtime/probe.json').read_bytes()
        require(packed_bytes == read('agent_full_runtime/probe.json'),
                'Repacked manifest or asset hashes differ from historical run')
        report = {
            'schema_version': 1,
            'kind': 'historical-full-search-artifact-restoration',
            'run_id': RUN_ID, 'artifact_id': ARTIFACT_ID,
            'artifact_sha256': ARTIFACT_SHA256, 'source_commit': SOURCE_COMMIT,
            'source_sha256': {key: hashes[key] for key in SOURCE_PATHS},
            'canonical_manifest_sha256': hashlib.sha256(manifest_bytes).hexdigest(),
            'packed_manifest_sha256': hashlib.sha256(packed_bytes).hexdigest(),
            'query_vectors_sha256': query_metadata['vectors_sha256'],
            'query_manifest_sha256': query_hash,
            'corpus_vectors_sha256': original['embeddings']['sha256'],
            'passages': original['passage_count'], 'queries': query_metadata['count'],
            'restored_assets_match_historical_run': True,
            'admission_certificate_issued': False, 'provider_calls': 0,
            'model_loaded': False, 'production_ready': False,
        }
        (output / 'restoration.json').write_text(json.dumps(report, indent=2) + '\n')
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    report = restore(args.archive, args.out)
    print(json.dumps(report))


if __name__ == '__main__':
    main()
