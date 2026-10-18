'''Build the agent corpus from assets/graph.json and filter/fulltext.

This module does not talk to Cloudflare. It checks the graph, cleans markdown
without lowercasing, and writes code-point chunks that fit the embedding
token budget. Release ids depend on the artifacts and embed.json, not on the
clock or the git SHA.

Run:  python src/build_agent_index.py
'''

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_fulltext_search import APP_HEAD, REF_HEAD, print_progress
from common import FULLTEXT_DIR, GRAPH, ROOT, load_json, safe_key

WORKER = ROOT / 'worker'
EMBED_PATH = WORKER / 'embed.json'
DEFAULT_OUT = ROOT / 'agent_build'
SMOKE_PATH = DEFAULT_OUT / 'smoke.json'
EVIDENCE = {'id', 'title', 'url'}
REQUIRED_NODE_FIELDS = ('id', 'title', 'authors', 'section', 'kind', 'url')
SLOTS = ('a', 'b')

BANNER_START = re.compile(r'report github issue', re.I)
BANNER_END = re.compile(r'describe the issue below', re.I)


class BuildError(Exception):
    '''The catalog or embed.json cannot produce a corpus.'''


class CapacityError(BuildError):
    '''The account cannot store both slots. The corpus is left intact.'''


def canonical_json(value) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(',', ':'), ensure_ascii=False,
    )


def sha256_hex(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def load_embed(path: Path | None = None) -> dict:
    embed_path = path or EMBED_PATH
    embed = json.loads(embed_path.read_text(encoding='utf-8'))
    vocab = (embed_path.parent / embed['tokenizer']['vocab_file']).resolve()
    digest = hashlib.sha256(vocab.read_bytes()).hexdigest()
    expected = embed['tokenizer']['vocab_sha256']
    if digest != expected:
        raise BuildError(
            f'vocab checksum {digest} != {expected} ({vocab})'
        )
    embed['_vocab_path'] = str(vocab)
    return embed


def build_signature(embed: dict) -> str:
    tok = embed['tokenizer']
    payload = {
        'schema_version': embed['schema_version'],
        'clean_version': embed['clean_version'],
        'chunk_version': embed['chunk_version'],
        'max_code_points': embed['max_code_points'],
        'overlap_code_points': embed['overlap_code_points'],
        'max_input_tokens': embed['max_input_tokens'],
        'passage_template': embed['passage_template'],
        'tokenizer_id': tok['id'],
        'tokenizer_revision': tok['revision'],
        'vocab_sha256': tok['vocab_sha256'],
        'do_lower_case': tok['do_lower_case'],
        'strip_accents': tok['strip_accents'],
        'tokenize_chinese_chars': tok['tokenize_chinese_chars'],
        'max_input_chars_per_word': tok['max_input_chars_per_word'],
        'cls_token': tok['cls_token'],
        'sep_token': tok['sep_token'],
        'unk_token': tok['unk_token'],
    }
    return sha256_hex(canonical_json(payload))


def embedding_signature(embed: dict) -> str:
    tok = embed['tokenizer']
    payload = {
        'model': embed['model'],
        'dimensions': embed['dimensions'],
        'metric': embed['metric'],
        'pooling': embed['pooling'],
        'query_template': embed['query_template'],
        'passage_template': embed['passage_template'],
        'max_input_tokens': embed['max_input_tokens'],
        'tokenizer_revision': tok['revision'],
        'vocab_sha256': tok['vocab_sha256'],
    }
    return sha256_hex(canonical_json(payload))


def vector_id(slot: str, paper_id: str, chunk_index: int) -> str:
    return sha256_hex(canonical_json([slot, paper_id, chunk_index]))


def model_input(template: str, text: str) -> str:
    if template:
        return template + text
    return text


def input_hash(embed: dict, text: str, signature: str) -> str:
    return sha256_hex(canonical_json({
        'embedding_signature': signature,
        'input': model_input(embed['passage_template'], text),
    }))


def git_sha() -> str | None:
    try:
        return subprocess.check_output(
            ['git', 'rev-parse', 'HEAD'],
            cwd=ROOT,
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip() or None
    except (OSError, subprocess.CalledProcessError):
        return None


def strip_banner(markdown: str) -> str:
    '''Drop a leading ar5iv issue banner and nothing else.'''
    lines = markdown.splitlines(keepends=True)
    start = 0
    while start < len(lines) and not lines[start].strip():
        start += 1
    if start >= len(lines) or not BANNER_START.search(lines[start]):
        return markdown
    end = None
    for index in range(start, min(len(lines), start + 40)):
        if BANNER_END.search(lines[index]):
            end = index
            break
    if end is None:
        return markdown
    rest = end + 1
    while rest < len(lines) and not lines[rest].strip():
        rest += 1
    return ''.join(lines[rest:])


def drop_bibliography(markdown: str) -> str:
    '''Drop references. Resume at an appendix heading, including numbered ones.'''
    kept = []
    skip = False
    for line in markdown.splitlines(keepends=True):
        stripped = line.strip()
        if REF_HEAD.match(stripped):
            skip = True
            continue
        if APP_HEAD.match(stripped):
            skip = False
        if not skip:
            kept.append(line)
    return ''.join(kept)


def clean_markdown(markdown: str) -> str:
    return drop_bibliography(strip_banner(markdown))


def _is_punctuation(char: str) -> bool:
    cp = ord(char)
    if cp < 128:
        return (
            33 <= cp <= 47 or 58 <= cp <= 64 or 91 <= cp <= 96 or 123 <= cp <= 126
        )
    return unicodedata.category(char).startswith('P')


def _is_whitespace(char: str) -> bool:
    if char in ' \t\n\r':
        return True
    if ord(char) < 128:
        return False
    return unicodedata.category(char) == 'Zs'


def _is_control(char: str) -> bool:
    if char in '\t\n\r':
        return False
    cp = ord(char)
    if cp < 32 or cp == 127:
        return True
    if cp < 128:
        return False
    return unicodedata.category(char).startswith('C')


_CHINESE_RE = re.compile(
    '['
    '\u4e00-\u9fff'
    '\u3400-\u4dbf'
    '\U00020000-\U0002a6df'
    '\U0002a700-\U0002b73f'
    '\U0002b740-\U0002b81f'
    '\U0002b820-\U0002ceaf'
    '\uf900-\ufaff'
    '\U0002f800-\U0002fa1f'
    ']'
)
_CLEAN_TABLE: dict[int, str | None] | None = None


def _clean_table() -> dict[int, str | None]:
    '''Delete controls and turn the whitespace predicates into spaces.'''
    global _CLEAN_TABLE
    if _CLEAN_TABLE is not None:
        return _CLEAN_TABLE
    table: dict[int, str | None] = {}
    for cp in range(0x110000):
        char = chr(cp)
        if cp == 0 or cp == 0xFFFD or _is_control(char):
            table[cp] = None
        elif _is_whitespace(char):
            table[cp] = ' '
    _CLEAN_TABLE = table
    return table


class WordPieceTokenizer:
    '''BertTokenizer basic + wordpiece, shared with worker/src/tokenize.ts.'''

    def __init__(self, embed: dict):
        tok = embed['tokenizer']
        self.do_lower = bool(tok['do_lower_case'])
        self.strip_accents = bool(tok['strip_accents'])
        self.chinese = bool(tok['tokenize_chinese_chars'])
        self.max_chars = int(tok['max_input_chars_per_word'])
        self.unk = tok['unk_token']
        self.cls = tok['cls_token']
        self.sep = tok['sep_token']
        self.ids_by_token = {}
        raw = Path(embed['_vocab_path']).read_text(encoding='utf-8')
        for index, line in enumerate(raw.splitlines()):
            self.ids_by_token[line] = index
        for special in (self.unk, self.cls, self.sep):
            if special not in self.ids_by_token:
                raise BuildError(f'vocab missing {special}')

    def token_ids(self, template: str, text: str) -> list[int]:
        pieces = self._basic(model_input(template, text))
        ids = [self.ids_by_token[self.cls]]
        for piece in pieces:
            ids.extend(self._wordpiece(piece))
        ids.append(self.ids_by_token[self.sep])
        return ids

    def _basic(self, text: str) -> list[str]:
        flattened = text.translate(_clean_table())
        if self.chinese:
            flattened = _CHINESE_RE.sub(r' \g<0> ', flattened)
        output = []
        for token in flattened.split():
            if self.do_lower:
                token = token.lower()
            if self.strip_accents and not token.isascii():
                token = ''.join(
                    char for char in unicodedata.normalize('NFD', token)
                    if unicodedata.category(char) != 'Mn'
                )
            if token.isalnum():
                output.append(token)
            else:
                output.extend(self._split_punctuation(token))
        return output

    def _split_punctuation(self, token: str) -> list[str]:
        parts = []
        chars = []
        for char in token:
            if _is_punctuation(char):
                if chars:
                    parts.append(''.join(chars))
                    chars = []
                parts.append(char)
            else:
                chars.append(char)
        if chars:
            parts.append(''.join(chars))
        return parts

    def _wordpiece(self, token: str) -> list[int]:
        unk = self.ids_by_token[self.unk]
        if len(token) > self.max_chars:
            return [unk]
        whole = self.ids_by_token.get(token)
        if whole is not None:
            return [whole]
        start = 0
        ids = []
        length = len(token)
        while start < length:
            end = length
            found = None
            while start < end:
                piece = token[start:end]
                if start > 0:
                    piece = '##' + piece
                found = self.ids_by_token.get(piece)
                if found is not None:
                    break
                end -= 1
            if found is None:
                return [unk]
            ids.append(found)
            start = end
        return ids


def _snap(text: str, start: int, best: int) -> int:
    if best >= len(text):
        return len(text)
    window = text[start:best]
    half = max(1, len(window) // 2)
    for separator in ('\n\n', '\n', ' '):
        index = window.rfind(separator)
        if index >= half:
            return start + index
    return best


def chunk_text(
    text: str,
    count_tokens,
    *,
    max_code_points: int,
    overlap: int,
    max_tokens: int,
) -> list[tuple[int, int, int]]:
    '''Half-open code-point ranges plus the token count of each slice.'''
    length = len(text)
    if length == 0:
        return []
    if count_tokens('') > max_tokens:
        raise BuildError('passage template exceeds the token budget')
    chunks = []
    start = 0
    steps = 0
    while start < length:
        steps += 1
        if steps > length + 1:
            raise BuildError('chunker failed to advance')
        hard = min(length, start + max_code_points)
        hard_count = count_tokens(text[start:hard])
        if hard_count <= max_tokens:
            best = hard
            best_count = hard_count
        else:
            lo = start + 1
            hi = hard - 1
            best = start + 1
            best_count = count_tokens(text[start:best])
            while lo <= hi:
                mid = (lo + hi) // 2
                mid_count = count_tokens(text[start:mid])
                if mid_count <= max_tokens:
                    best = mid
                    best_count = mid_count
                    lo = mid + 1
                else:
                    hi = mid - 1
        if best_count > max_tokens:
            raise BuildError('a single code point exceeds the token budget')
        snapped = _snap(text, start, best)
        if snapped != best and snapped > start:
            snapped_count = count_tokens(text[start:snapped])
            if snapped_count <= max_tokens:
                best = snapped
                best_count = snapped_count
        chunks.append((start, best, best_count))
        if best >= length:
            break
        room = best - start
        use_overlap = min(overlap, max(0, room - 1))
        next_start = best - use_overlap
        if next_start <= start:
            next_start = start + 1
        start = next_start
    _assert_coverage(length, chunks, max_code_points, overlap)
    return chunks


def _assert_coverage(length, chunks, max_code_points, overlap) -> None:
    if not chunks or chunks[0][0] != 0:
        raise BuildError('chunk coverage does not start at 0')
    covered = 0
    previous_start = -1
    for start, end, _count in chunks:
        if start <= previous_start:
            raise BuildError('chunker step was not positive')
        if end <= start:
            raise BuildError('empty chunk')
        if end - start > max_code_points:
            raise BuildError('chunk exceeds the code-point cap')
        if start > covered:
            raise BuildError(f'chunk gap at {covered}')
        covered = max(covered, end)
        previous_start = start
    for (start0, end0, _count0), (start1, _end1, _count1) in zip(chunks, chunks[1:]):
        if end0 - start1 > overlap:
            raise BuildError('chunk overlap exceeds the cap')
        if start1 > end0:
            raise BuildError('chunk gap')
    if covered != length:
        raise BuildError('chunk coverage does not reach the end')


def _node_card(node: dict, text_info: dict) -> dict:
    authors = [author for author in node['authors'] if isinstance(author, str)]
    return {
        'id': node['id'],
        'title': node['title'],
        'authors': authors,
        'date': node.get('date'),
        'section': node.get('section'),
        'topic': node.get('topic'),
        'kind': node.get('kind'),
        'url': node.get('url'),
        'quality': node.get('quality'),
        'quality_conf': node.get('quality_conf'),
        'quality_verdict': node.get('quality_verdict'),
        'quality_accepts': node.get('quality_accepts'),
        'quality_models': node.get('quality_models'),
        'text': text_info,
    }


def validate_edges(nodes: list[dict], edges: list) -> list[dict]:
    if not isinstance(nodes, list) or not isinstance(edges, list):
        raise BuildError('graph nodes and edges must be lists')
    ids = []
    seen = set()
    for index, node in enumerate(nodes):
        if not isinstance(node, dict):
            raise BuildError(f'node {index} is not an object')
        for field in REQUIRED_NODE_FIELDS:
            if field not in node:
                raise BuildError(f'node {index} missing {field}')
        node_id = node['id']
        if not isinstance(node_id, str) or not node_id:
            raise BuildError(f'node {index} has an empty id')
        if not isinstance(node['title'], str):
            raise BuildError(f'{node_id} title is not a string')
        if not isinstance(node['authors'], list):
            raise BuildError(f'{node_id} authors is not a list')
        if node_id in seen:
            raise BuildError(f'duplicate catalog id {node_id}')
        seen.add(node_id)
        ids.append(node_id)
    keys = {}
    for node_id in ids:
        key = safe_key(node_id)
        other = keys.get(key)
        if other is not None:
            raise BuildError(f'safe_key collision {key}: {other} and {node_id}')
        keys[key] = node_id
    resolved = []
    total = len(nodes)
    for index, edge in enumerate(edges):
        if not isinstance(edge, (list, tuple)) or len(edge) != 3:
            raise BuildError(f'edge {index} must be [source, target, evidence]')
        source, target, evidence = edge
        if isinstance(source, bool) or isinstance(target, bool):
            raise BuildError(f'edge {index} index is not an integer')
        if not isinstance(source, int) or not isinstance(target, int):
            raise BuildError(f'edge {index} index is not an integer')
        if not (0 <= source < total and 0 <= target < total):
            raise BuildError(f'edge {index} index out of range')
        if evidence not in EVIDENCE:
            raise BuildError(f'edge {index} evidence {evidence!r}')
        resolved.append({
            'source': ids[source],
            'target': ids[target],
            'evidence': evidence,
        })
    resolved.sort(key=lambda item: (
        item['source'], item['target'], item['evidence'],
    ))
    return resolved


def _adjacency(ids: list[str], edges: list[dict]) -> tuple[dict, dict]:
    outgoing = {node_id: [] for node_id in ids}
    incoming = {node_id: [] for node_id in ids}
    for edge in edges:
        outgoing[edge['source']].append({
            'target': edge['target'],
            'evidence': edge['evidence'],
        })
        incoming[edge['target']].append({
            'source': edge['source'],
            'evidence': edge['evidence'],
        })
    for node_id in ids:
        outgoing[node_id].sort(key=lambda item: (
            item['target'], item['evidence'],
        ))
        incoming[node_id].sort(key=lambda item: (
            item['source'], item['evidence'],
        ))
    return outgoing, incoming


def build_release(
    nodes: list[dict],
    edges: list,
    texts: dict[str, str | None],
    embed: dict,
    *,
    git_sha_value: str | None = None,
    progress: bool = False,
) -> dict:
    resolved = validate_edges(nodes, edges)
    ids = [node['id'] for node in nodes]
    outgoing, incoming = _adjacency(ids, resolved)
    tokeniser = WordPieceTokenizer(embed)
    embed_sig = embedding_signature(embed)
    template = embed['passage_template']
    max_tokens = int(embed['max_input_tokens'])
    max_points = int(embed['max_code_points'])
    overlap = int(embed['overlap_code_points'])

    def count_tokens(piece: str) -> int:
        return len(tokeniser.token_ids(template, piece))

    papers = {}
    cards = {}
    reasons = {'no_markdown': 0, 'empty_cleaned': 0}
    code_points = 0
    token_count = 0
    total = len(nodes)
    for index, node in enumerate(nodes, start=1):
        node_id = node['id']
        markdown = texts.get(node_id)
        if progress:
            print_progress(index, total, node_id)
        if markdown is None:
            reasons['no_markdown'] += 1
            cards[node_id] = _node_card(node, {
                'available': False,
                'reason': 'no_markdown',
                'code_points': 0,
                'chunks': 0,
            })
            continue
        cleaned = clean_markdown(markdown)
        if not cleaned.strip():
            reasons['empty_cleaned'] += 1
            cards[node_id] = _node_card(node, {
                'available': False,
                'reason': 'empty_cleaned',
                'code_points': 0,
                'chunks': 0,
            })
            continue
        ranges = chunk_text(
            cleaned,
            count_tokens,
            max_code_points=max_points,
            overlap=overlap,
            max_tokens=max_tokens,
        )
        chunks = []
        for chunk_index, (start, end, tokens) in enumerate(ranges):
            piece = cleaned[start:end]
            if tokens > max_tokens:
                raise BuildError(f'{node_id} chunk {chunk_index} exceeds tokens')
            content = sha256_hex(piece)
            hashed = input_hash(embed, piece, embed_sig)
            chunks.append({
                'index': chunk_index,
                'start': start,
                'end': end,
                'token_count': tokens,
                'content_hash': content,
                'input_hash': hashed,
            })
            token_count += tokens
        code_points += len(cleaned)
        papers[node_id] = {
            'paper_id': node_id,
            'text': cleaned,
            'chunks': chunks,
        }
        cards[node_id] = _node_card(node, {
            'available': True,
            'reason': None,
            'code_points': len(cleaned),
            'chunks': len(chunks),
            'object': sha256_hex(node_id),
        })
    passages = []
    for node_id in sorted(papers):
        for chunk in papers[node_id]['chunks']:
            passages.append({
                'paper_id': node_id,
                'chunk_index': chunk['index'],
                'start': chunk['start'],
                'end': chunk['end'],
                'token_count': chunk['token_count'],
                'content_hash': chunk['content_hash'],
                'input_hash': chunk['input_hash'],
            })
    seen_ids = set()
    for slot in SLOTS:
        for passage in passages:
            digest = vector_id(
                slot, passage['paper_id'], passage['chunk_index'],
            )
            if digest in seen_ids:
                raise BuildError(f'vector id collision in slot {slot}')
            seen_ids.add(digest)
    graph = {
        'nodes': {node_id: cards[node_id] for node_id in sorted(cards)},
        'out': {node_id: outgoing[node_id] for node_id in sorted(outgoing)},
        'in': {node_id: incoming[node_id] for node_id in sorted(incoming)},
    }
    paper_blob = {node_id: papers[node_id] for node_id in sorted(papers)}
    build_sig = build_signature(embed)
    graph_json = canonical_json(graph)
    papers_json = canonical_json(paper_blob)
    release_id = sha256_hex(canonical_json({
        'graph': sha256_hex(graph_json),
        'papers': sha256_hex(papers_json),
        'build_signature': build_sig,
        'embedding_signature': embed_sig,
    }))
    manifest = {
        'release_id': release_id,
        'schema_version': embed['schema_version'],
        'reader_schema': embed['reader_schema'],
        'build_signature': build_sig,
        'embedding_signature': embed_sig,
        'git_sha': git_sha_value,
        'passage_count': len(passages),
        'node_count': len(nodes),
        'edge_count': len(resolved),
        'papers_with_text': len(papers),
        'passages': passages,
    }
    report_source = {
        'passage_count': len(passages),
        'token_count': token_count,
        'code_points': code_points,
        'papers_with_text': len(papers),
        'papers_without_text': len(nodes) - len(papers),
        'reasons': reasons,
        'r2_bytes': (
            len(graph_json.encode('utf-8'))
            + len(papers_json.encode('utf-8'))
            + len(canonical_json(manifest).encode('utf-8'))
        ),
    }
    return {
        'release_id': release_id,
        'graph': graph,
        'papers': paper_blob,
        'manifest': manifest,
        'passages': passages,
        'report': capacity_report(report_source, embed),
        'build_signature': build_sig,
        'embedding_signature': embed_sig,
    }


def capacity_report(source: dict, embed: dict) -> dict:
    passages = source['passage_count']
    tokens = source['token_count']
    dimensions = int(embed['dimensions'])
    probe = int(embed['vectorize']['probe_vectors'])
    free = int(embed['vectorize']['free_dimensions'])
    one = passages * dimensions
    two = passages * 2 * dimensions
    with_probe = two + probe * dimensions
    millions = tokens / 1_000_000
    neurons_per = float(embed['pricing']['neurons_per_million_tokens'])
    usd_per = float(embed['pricing']['usd_per_million_tokens'])
    return {
        'passages': passages,
        'tokens': tokens,
        'code_points': source['code_points'],
        'papers_with_text': source['papers_with_text'],
        'papers_without_text': source['papers_without_text'],
        'reasons': source['reasons'],
        'dimensions_one_slot': one,
        'dimensions_two_slots': two,
        'dimensions_with_probe': with_probe,
        'documented_free_dimensions': free,
        'fits_documented_free_tier': with_probe <= free,
        'embedding_tokens_upper_bound': tokens,
        'neurons_upper_bound': millions * neurons_per,
        'embedding_usd_upper_bound': millions * usd_per,
        'free_neurons_per_day': embed['pricing']['free_neurons_per_day'],
        'r2_bytes': source['r2_bytes'],
        'note': (
            'Neuron cost is separate from Vectorize storage. '
            'Spreading embeddings across days does not reduce stored '
            'dimensions. The corpus is not trimmed to fit a quota.'
        ),
    }


def assert_capacity(report: dict, dimension_budget: int | None) -> None:
    if dimension_budget is None:
        raise CapacityError(
            'dimension budget is unknown; set AGENT_DIMENSION_BUDGET '
            'after checking the Cloudflare plan'
        )
    need = report['dimensions_with_probe']
    if need > dimension_budget:
        raise CapacityError(
            f'need {need} dimensions, budget {dimension_budget}. '
            'Refusing to shrink the corpus.'
        )


def read_texts(nodes: list[dict]) -> dict[str, str | None]:
    texts = {}
    for node in nodes:
        path = FULLTEXT_DIR / f'{safe_key(node["id"])}.md'
        if path.is_file():
            texts[node['id']] = path.read_text(encoding='utf-8')
        else:
            texts[node['id']] = None
    return texts


def load_written_release(out_dir: Path) -> dict:
    '''Reload the files write_release produced. The publisher uploads this.'''
    graph = json.loads((out_dir / 'graph.json').read_text(encoding='utf-8'))
    manifest = json.loads((out_dir / 'manifest.json').read_text(encoding='utf-8'))
    papers = {}
    for path in sorted((out_dir / 'papers').glob('*.json')):
        paper = json.loads(path.read_text(encoding='utf-8'))
        papers[paper['paper_id']] = paper
    report = json.loads((out_dir / 'dry_run.json').read_text(encoding='utf-8'))
    return {
        'release_id': manifest['release_id'],
        'graph': graph,
        'papers': papers,
        'manifest': manifest,
        'passages': manifest['passages'],
        'report': report,
        'build_signature': manifest['build_signature'],
        'embedding_signature': manifest['embedding_signature'],
    }


def write_release(release: dict, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    papers_dir = out_dir / 'papers'
    papers_dir.mkdir(exist_ok=True)
    for stale in papers_dir.glob('*.json'):
        stale.unlink()
    (out_dir / 'graph.json').write_text(
        canonical_json(release['graph']), encoding='utf-8',
    )
    (out_dir / 'manifest.json').write_text(
        canonical_json(release['manifest']), encoding='utf-8',
    )
    (out_dir / 'dry_run.json').write_text(
        json.dumps(release['report'], indent=2, ensure_ascii=False) + '\n',
        encoding='utf-8',
    )
    for paper_id, paper in release['papers'].items():
        name = sha256_hex(paper_id) + '.json'
        (papers_dir / name).write_text(
            canonical_json(paper), encoding='utf-8',
        )


def build_from_disk(
    embed: dict | None = None,
    *,
    graph_path: Path | None = None,
    progress: bool = True,
    git_sha_value: str | None = None,
) -> dict:
    config = embed or load_embed()
    graph = load_json(graph_path or GRAPH, {})
    nodes = graph.get('nodes') or []
    edges = graph.get('edges') or []
    return build_release(
        nodes,
        edges,
        read_texts(nodes),
        config,
        git_sha_value=git_sha_value,
        progress=progress,
    )


def emit_token_fixtures(path: Path, embed: dict | None = None) -> None:
    config = embed or load_embed()
    tokeniser = WordPieceTokenizer(config)
    samples = [
        'Hello, world!',
        'café',
        '中文',
        'hi 😀 there',
        'f(x) = x^2',
        '',
        'a' * 120,
    ]
    rows = []
    for text in samples:
        rows.append({
            'text': text,
            'template': '',
            'ids': tokeniser.token_ids('', text),
        })
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(rows, ensure_ascii=False, indent=2) + '\n',
        encoding='utf-8',
    )
    print(f'wrote {path}')


def main() -> None:
    args = sys.argv[1:]
    config = load_embed()
    if '--emit-token-fixtures' in args:
        index = args.index('--emit-token-fixtures')
        destination = Path(args[index + 1])
        emit_token_fixtures(destination, config)
        return
    out = DEFAULT_OUT
    if '--out' in args:
        out = Path(args[args.index('--out') + 1])
    release = build_from_disk(config, git_sha_value=git_sha())
    write_release(release, out)
    report = release['report']
    print(f'release_id     {release["release_id"]}')
    print(f'passages       {report["passages"]}')
    print(f'tokens         {report["tokens"]}')
    print(f'with_text      {report["papers_with_text"]}')
    print(f'without_text   {report["papers_without_text"]}  {report["reasons"]}')
    print(f'dimensions     two slots+probe {report["dimensions_with_probe"]}')
    print(f'free_tier_fit  {report["fits_documented_free_tier"]}')
    print(
        f'embed_upper    {report["neurons_upper_bound"]:.0f} neurons, '
        f'${report["embedding_usd_upper_bound"]:.2f}'
    )
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
