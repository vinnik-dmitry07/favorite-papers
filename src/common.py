'''Shared helpers for the citation-map pipeline.

Node ids are stable strings derived from a URL:
    arxiv:2503.20783 / openreview:s0JVsx3bx1 / doi:10.1038/... /
    acl:2022.acl-long.360 / url:lilianweng.github.io/posts/...
'''

import gzip
import json
import re
import unicodedata
from pathlib import Path
from urllib.parse import urlsplit

SRC_DIR = Path(__file__).resolve().parent
ROOT = SRC_DIR.parent
ASSETS = ROOT / 'assets'
CACHE_DIR = ROOT / 'cache'
MAP_DIR = ASSETS

README = ROOT / 'readme.md'
CATALOG = ASSETS / 'catalog.json'
REFS = ASSETS / 'refs.json'
PAGE_META = ASSETS / 'page_meta.json'
GRAPH = ASSETS / 'graph.json'
GRAPH_JS = ASSETS / 'graph_data.js'
ARXIV_META = ASSETS / 'arxiv_meta.json'
KNOWN_META = ASSETS / 'known_meta.json'
LITMAPS = ASSETS / 'litmaps.json'

ARXIV_URL_RE = re.compile(
    r'arxiv\.org/(?:abs|pdf|html|format)/'
    r'(\d{4}\.\d{4,5}|[a-z\-]+(?:\.[A-Z]{2})?/\d{7})',
    re.I,
)
# Mirrors that put the arXiv id straight in the path.
ARXIV_MIRROR_RE = re.compile(
    r'(?:huggingface\.co/papers|ar5iv\.org/abs|alphaxiv\.org/(?:abs|overview))/'
    r'(\d{4}\.\d{4,5})',
    re.I,
)
ARXIV_TEXT_RE = re.compile(
    r'ar[xX]iv[:\s]{1,3}(\d{4}\.\d{4,5})',
    re.I,
)
DOI_RE = re.compile(r'\b(10\.\d{4,9}/[^\s"<>)\]},;]+)')
OPENREVIEW_RE = re.compile(r'openreview\.net/(?:forum|pdf)\?id=([\w\-]+)', re.I)
ACL_RE = re.compile(r'aclanthology\.org/([\w\-.]+?)/?(?:$|[?#])', re.I)

# Domains that never describe a paper: telegram mirrors, the Litmaps app itself.
SKIP_HOSTS = (
    't-me.translate.goog', 't.me', 'telegram.me', 'app.litmaps.com',
    'litmaps.com',
)

_WORD_RE = re.compile(r'[a-z0-9]+')


def clean_arxiv_id(raw: str) -> str:
    '''Strip a version suffix and normalise case.'''
    return re.sub(r'v\d+$', '', raw.strip(), flags=re.I).lower()


def clean_doi(raw: str) -> str:
    doi = raw.strip().rstrip('.,;:')
    doi = re.sub(r'^https?://(?:dx\.)?doi\.org/', '', doi, flags=re.I)
    return doi.lower()


def host_of(url: str) -> str:
    host = urlsplit(url).netloc.lower()
    return host[4:] if host.startswith('www.') else host


def is_skippable(url: str) -> bool:
    return host_of(url) in SKIP_HOSTS


def url_slug(url: str) -> str:
    '''Canonical `host/path` slug, used for non-identifier URLs.'''
    parts = urlsplit(url)
    host = host_of(url)
    path = re.sub(r'/+$', '', parts.path)
    path = re.sub(r'/(index|index\.html?)$', '', path, flags=re.I)
    slug = f'{host}{path}'
    if parts.query:
        slug = f'{slug}?{parts.query}'
    return slug.lower()


def classify(url: str) -> tuple[str, str] | None:
    '''Map a URL to `(kind, node_id)`, or None if it is not a paper link.'''
    if not url or is_skippable(url):
        return None

    match = ARXIV_URL_RE.search(url) or ARXIV_MIRROR_RE.search(url)
    if match:
        return 'arxiv', f'arxiv:{clean_arxiv_id(match.group(1))}'

    match = OPENREVIEW_RE.search(url)
    if match:
        return 'openreview', f'openreview:{match.group(1)}'

    match = ACL_RE.search(url)
    if match:
        return 'acl', f'acl:{match.group(1)}'

    host = host_of(url)
    if host in ('doi.org', 'dx.doi.org'):
        match = DOI_RE.search(url)
        if match:
            return 'doi', f'doi:{clean_doi(match.group(1))}'

    kind = 'repo' if host in ('github.com', 'huggingface.co') else 'web'
    return kind, f'url:{url_slug(url)}'


def node_arxiv_ids(
    node: dict,
    overrides: dict | None = None,
    page_meta: dict | None = None,
) -> list[str]:
    '''arXiv ids on a node: own id, extra URLs, redirect, or known_meta.'''
    ids: list[str] = []
    if node.get('kind') == 'arxiv':
        ids.append(node['id'].split(':', 1)[1])
    for url in node.get('urls') or []:
        classified = classify(url)
        if not classified or classified[0] != 'arxiv':
            continue
        aid = classified[1].split(':', 1)[1]
        if aid not in ids:
            ids.append(aid)
    resolved = ((page_meta or {}).get(node['id']) or {}).get('resolved')
    classified = classify(resolved) if resolved else None
    if classified and classified[0] == 'arxiv':
        aid = classified[1].split(':', 1)[1]
        if aid not in ids:
            ids.append(aid)
    alias = ((overrides or {}).get(node['id']) or {}).get('arxiv')
    if alias and alias not in ids:
        ids.append(alias)
    return ids


_COARSE_DATES = ('url', 'label', 'label-year', 'arxiv-id')


def apply_date_overrides(
    node: dict, arxiv_known: dict, overrides: dict
) -> None:
    '''Fill from arXiv aliases, then apply curated first-public dates.

    known_meta dates always win: they are first-public of this catalog
    entry (blog, OpenReview, site) and may predate a later arXiv upload.
    '''
    override = overrides.get(node['id']) or {}
    coarse = not node.get('date') or node.get('date_source') in _COARSE_DATES
    for aid in node_arxiv_ids(node, overrides):
        info = arxiv_known.get(aid) or {}
        if info.get('title') and node.get('kind') != 'arxiv':
            node['fetched_title'] = info['title']
        if info.get('authors') and not node.get('authors'):
            node['authors'] = info['authors']
        if coarse and info.get('published') and not override.get('date'):
            node['date'] = info['published']
            node['date_source'] = 'arxiv-api'
            coarse = False
    if override.get('date'):
        node['date'] = override['date']
        node['date_source'] = override.get('date_source') or 'known'
    if override.get('authors'):
        node['authors'] = list(override['authors'])


def arxiv_date(arxiv_id: str) -> str | None:
    '''Approximate publication date encoded in a modern arXiv id (YYMM).'''
    match = re.match(r'^(\d{2})(\d{2})\.\d{4,5}$', arxiv_id)
    if not match:
        return None
    year, month = int(match.group(1)), int(match.group(2))
    if not 1 <= month <= 12:
        return None
    century = 1900 if year >= 91 else 2000
    return f'{century + year:04d}-{month:02d}-01'


def norm_title(text: str) -> str:
    '''Lowercase alphanumeric words joined by single spaces.'''
    text = unicodedata.normalize('NFKD', text or '')
    text = ''.join(ch for ch in text if not unicodedata.combining(ch))
    return ' '.join(_WORD_RE.findall(text.lower()))


def cache_path(node_id: str, suffix: str) -> Path:
    safe = re.sub(r'[^A-Za-z0-9._-]+', '_', node_id)[:120]
    return CACHE_DIR / f'{safe}{suffix}'


def read_gz(path: Path) -> str:
    with gzip.open(path, 'rt', encoding='utf-8', errors='replace') as handle:
        return handle.read()


def write_gz(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, 'wt', encoding='utf-8') as handle:
        handle.write(text)


def load_json(path: Path, default):
    if not Path(path).exists():
        return default
    return json.loads(Path(path).read_text(encoding='utf-8'))


def dump_json(path: Path, data) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8'
    )
