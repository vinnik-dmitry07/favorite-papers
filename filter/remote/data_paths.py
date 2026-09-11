'''Resolve data directories on the laptop or a Vast.ai box.'''

from __future__ import annotations

import json
import re
from os import environ
from pathlib import Path

SAFE_KEY_RE = re.compile(r'[^A-Za-z0-9._-]+')
REF_CUT = re.compile(r'\n#{1,6}\s+references\b', re.I)


def data_dir() -> Path:
    raw = environ.get('FILTER_DATA')
    if raw:
        return Path(raw)
    here = Path(__file__).resolve().parent
    parent = here.parent
    if (parent / 'meta.jsonl').exists() or (parent / 'papers.jsonl').exists():
        return parent
    workspace = Path('/workspace/filter')
    if workspace.exists():
        return workspace
    return parent


def meta_path() -> Path:
    return data_dir() / 'meta.jsonl'


def papers_path() -> Path:
    return data_dir() / 'papers.jsonl'


def fulltext_dir() -> Path:
    return data_dir() / 'fulltext'


def scores_path(name: str) -> Path:
    return data_dir() / f'scores_{name}.jsonl'


def reviews_dir(name: str) -> Path:
    path = data_dir() / 'reviews' / name
    path.mkdir(parents=True, exist_ok=True)
    return path


def safe_key(key: str) -> str:
    return SAFE_KEY_RE.sub('_', key)[:120]


def year_of(row: dict) -> str:
    published = row.get('published') or ''
    if len(published) >= 4 and published[:4].isdigit():
        return published[:4]
    key = row.get('key') or ''
    if key.startswith('arxiv:'):
        aid = key.split(':', 1)[1]
        match = re.match(r'^(\d{2})(\d{2})\.\d{4,5}', aid)
        if match:
            year = int(match.group(1))
            century = 1900 if year >= 91 else 2000
            return f'{century + year:04d}'
    return 'unknown'


def fill_template(template: str, **kwargs) -> str:
    text = template
    for key, value in kwargs.items():
        text = text.replace('{' + key + '}', str(value))
    return text


def is_score_row(row: dict) -> bool:
    if not row.get('key') or row.get('error'):
        return False
    if row.get('bt_score') is not None:
        return bool(row.get('n_valid'))
    if row.get('p_accept') is not None:
        return True
    if row.get('score') is not None:
        return True
    return row.get('rating') is not None or bool(row.get('decision'))


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding='utf-8').splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def append_jsonl(path: Path, row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a', encoding='utf-8') as handle:
        handle.write(json.dumps(row, ensure_ascii=False) + '\n')
        handle.flush()


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + '.tmp')
    with tmp.open('w', encoding='utf-8') as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + '\n')
    tmp.replace(path)


def scored_keys(path: Path) -> set[str]:
    return {row['key'] for row in read_jsonl(path) if is_score_row(row)}


def load_joined() -> list[dict]:
    meta = {row['key']: row for row in read_jsonl(meta_path())}
    papers = read_jsonl(papers_path())
    rows = []
    for paper in papers:
        item = dict(paper)
        item.update(meta.get(paper['key'], {}))
        if not item.get('title'):
            item['title'] = paper.get('line_title') or ''
        rows.append(item)
    return rows


def fulltext_index() -> dict[str, dict]:
    return {row['key']: row for row in read_jsonl(data_dir() / 'fulltext_index.jsonl')}


def fulltext_path(key: str) -> Path:
    directory = fulltext_dir()
    primary = directory / f'{safe_key(key)}.md'
    if primary.exists():
        return primary
    legacy_name = key.replace(':', '_')
    if '/' in legacy_name or '\\' in legacy_name or '..' in Path(legacy_name).parts:
        return primary
    legacy = directory / f'{legacy_name}.md'
    return legacy if legacy.exists() else primary


def fulltext_for(key: str, max_chars: int = 80_000) -> str:
    path = fulltext_path(key)
    if not path.exists():
        return ''
    text = path.read_text(encoding='utf-8')
    match = REF_CUT.search(text)
    if match:
        text = text[:match.start()]
    return text[:max_chars]
