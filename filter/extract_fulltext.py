'''Turn cached HTML (and fallbacks) into markdown full text.

    python filter/extract_fulltext.py
    python filter/extract_fulltext.py --only-keys openreview:XyGJJ4FPoX
'''

from __future__ import annotations

import argparse
import html as html_lib
import io
import json
import re
import sys
import urllib.request
import zipfile
from pathlib import Path

FILTER_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(FILTER_DIR))
sys.path.insert(0, str(FILTER_DIR.parent / 'src'))

from paths import (  # noqa: E402
    FULLTEXT_DIR,
    FULLTEXT_INDEX,
    FULLTEXT_ZIP,
    PAPERS_JSONL,
    cache_path,
    print_progress,
    read_gz,
    read_jsonl,
    safe_key,
    write_jsonl,
)

SCRIPT_RE = re.compile(r'<(script|style|svg|nav)\b.*?</\1>', re.S | re.I)
HEADING_RE = re.compile(
    r'<h([1-6])\b[^>]*>(.*?)</h\1>',
    re.S | re.I,
)
P_RE = re.compile(r'<p\b[^>]*>(.*?)</p>', re.S | re.I)
DIV_RE = re.compile(
    r'<div\b[^>]*class="[^"]*ltx_para[^"]*"[^>]*>(.*?)</div>',
    re.S | re.I,
)
LI_RE = re.compile(r'<li\b[^>]*>(.*?)</li>', re.S | re.I)
TAG_RE = re.compile(r'<[^>]+>')
HEADERS = {
    'User-Agent': 'key-papers-filter/0.1 (local research scoring)',
    'Accept': 'application/pdf, text/html, application/json;q=0.9,*/*;q=0.8',
}
BROWSER_UA = (
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/128.0 Safari/537.36'
)
CHALLENGE_RE = re.compile(
    r'verifying your browser|just a moment\b|enable javascript and cookies|'
    r'verify you are human|checking your browser|cf-browser-verification',
    re.I,
)
OPENREVIEW_APIS = (
    'https://api2.openreview.net/notes?id={fid}',
    'https://api2.openreview.net/notes?forum={fid}',
)

REF_HEAD = re.compile(
    r'^#{1,6}\s+(references|bibliography|works cited)\b',
    re.I,
)
APP_HEAD = re.compile(
    r'^#{1,6}\s+(appendix|supplementary|supplement)\b',
    re.I,
)


def strip_tags(markup: str) -> str:
    text = SCRIPT_RE.sub(' ', markup)
    text = TAG_RE.sub(' ', text)
    return ' '.join(html_lib.unescape(text).split())


def html_to_markdown(markup: str) -> str:
    markup = SCRIPT_RE.sub(' ', markup)
    parts: list[str] = []
    cursor = 0
    tokens = []
    for match in HEADING_RE.finditer(markup):
        tokens.append((match.start(), match.end(), 'h', match))
    for match in P_RE.finditer(markup):
        tokens.append((match.start(), match.end(), 'p', match))
    for match in DIV_RE.finditer(markup):
        tokens.append((match.start(), match.end(), 'p', match))
    for match in LI_RE.finditer(markup):
        tokens.append((match.start(), match.end(), 'p', match))
    tokens.sort(key=lambda item: item[0])
    for start, end, kind, match in tokens:
        if start < cursor:
            continue
        if kind == 'h':
            level = int(match.group(1))
            title = strip_tags(match.group(2))
            if title:
                parts.append(f'{"#" * level} {title}')
        else:
            text = strip_tags(match.group(1))
            if text:
                parts.append(text)
        cursor = end
    if not parts:
        text = strip_tags(markup)
        if text:
            parts.append(text[:200_000])
    return '\n\n'.join(parts)


def split_sections(markdown: str) -> tuple[str, str, str]:
    lines = markdown.splitlines()
    body, refs, appendix = [], [], []
    bucket = body
    for line in lines:
        if REF_HEAD.match(line.strip()):
            bucket = refs
        elif APP_HEAD.match(line.strip()):
            bucket = appendix
        bucket.append(line)
    return '\n'.join(body).strip(), '\n'.join(refs).strip(), '\n'.join(appendix).strip()


def load_cached_html(key: str) -> str | None:
    for suffix in ('.html.gz',):
        path = cache_path(key, suffix)
        if not path.exists():
            continue
        raw = read_gz(path)
        if '\n' in raw[:400]:
            _head, _, body = raw.partition('\n')
            return body
        return raw
    return None


def is_garbage_text(text: str) -> bool:
    stripped = ' '.join((text or '').split())
    if len(stripped) < 400:
        return True
    return bool(CHALLENGE_RE.search(stripped[:3000]))


def download_bytes(url: str, timeout: int = 60, browser: bool = False) -> bytes | None:
    # bioRxiv / Research Square sit behind Cloudflare and reject bot UAs.
    headers = {**HEADERS, 'User-Agent': BROWSER_UA} if browser else HEADERS
    request = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as resp:
            return resp.read()
    except Exception as exc:  # noqa: BLE001
        print(f'  download fail {url}: {exc}', flush=True)
        return None


def download_html(url: str) -> str | None:
    raw = download_bytes(url, timeout=45)
    if raw is None:
        return None
    return raw.decode('utf-8', 'replace')


def pdf_to_text(data: bytes) -> str:
    from pypdf import PdfReader

    reader = PdfReader(io.BytesIO(data))
    parts = []
    for page in reader.pages:
        parts.append(page.extract_text() or '')
    return '\n\n'.join(part.strip() for part in parts if part and part.strip())


def openreview_pdf_urls(forum_id: str) -> list[str]:
    urls = [f'https://openreview.net/pdf?id={forum_id}']
    for template in OPENREVIEW_APIS:
        raw = download_bytes(template.format(fid=forum_id), timeout=30)
        if raw is None:
            continue
        try:
            payload = json.loads(raw.decode('utf-8', 'replace'))
        except json.JSONDecodeError:
            continue
        for note in payload.get('notes') or []:
            content = note.get('content') or {}
            pdf = content.get('pdf') or {}
            value = pdf.get('value') if isinstance(pdf, dict) else pdf
            if isinstance(value, str) and value:
                if value.startswith('/'):
                    urls.append('https://openreview.net' + value)
                elif value.startswith('http'):
                    urls.append(value)
    seen, out = set(), []
    for url in urls:
        if url not in seen:
            seen.add(url)
            out.append(url)
    return out


# OpenReview itself is Cloudflare-blocked from this machine; use mirrors first.
EXTRA_PDF_URLS = {
    'openreview:BZ5a1r-kVsf': [
        'https://www.alphaxiv.org/abs/2603.a-path-towards-autonomous-machine-intelligence.pdf',
    ],
    'openreview:klU4737opt': [
        'https://www.tomzahavy.com/files/llms-cant-jump.pdf',
    ],
    'openreview:pOoKI3ouv1': ['https://arxiv.org/pdf/2402.10877'],
    'openreview:wUU-7XTL5XO': ['https://arxiv.org/pdf/2206.10498'],
    'openreview:hcQfTsVnBo': ['https://arxiv.org/pdf/2312.06581'],
    'openreview:ry_WPG-A-': ['https://arxiv.org/pdf/1703.09146'],
    'doi:10.1073/pnas.1611835114': ['https://arxiv.org/pdf/1612.00796'],
    'doi:10.1038/s41586-023-06924-6': [
        'https://www.nature.com/articles/s41586-023-06924-6.pdf',
    ],
}


LOCAL_PDF_ALIASES = {
    'openreview:XyGJJ4FPoX': '22_Meta_Reinforcement_Learning.pdf',
    'openreview:OpC-9aBBVJe': '3149_sample_efficient_reinforcement.pdf',
}


def local_pdf_text(key: str) -> str | None:
    candidates = [FULLTEXT_DIR / f'{safe_key(key)}.pdf']
    alias = LOCAL_PDF_ALIASES.get(key)
    if alias:
        candidates.append(FULLTEXT_DIR / alias)
    for path in candidates:
        if not path.exists():
            continue
        try:
            text = pdf_to_text(path.read_bytes())
        except Exception as exc:  # noqa: BLE001
            print(f'  local pdf fail {path.name}: {exc}', flush=True)
            continue
        if text and not is_garbage_text(text):
            print(f'  local pdf {path.name} chars={len(text)}', flush=True)
            return text
    return None


BIORXIV_RE = re.compile(r'biorxiv\.org/content/(10\.1101/[\d.]+?)(v\d+)?(?:\.full)?(?:\.pdf)?/?$')
RS_RE = re.compile(r'^10\.21203/rs\.3\.(rs-\d+)/(v\d+)$')


def pdf_fallback_urls(paper: dict) -> list[str]:
    '''Direct PDF links for abstract-only landing pages.'''
    kind, value = paper['key'].split(':', 1)
    urls = [u for u in paper.get('urls') or [] if u.lower().endswith('.pdf')]
    if kind == 'arxiv':
        urls.append(f'https://arxiv.org/pdf/{value}')
    elif kind == 'acl':
        urls.append(f'https://aclanthology.org/{value}.pdf')
    elif kind == 'doi':
        if value.startswith('10.1101/'):
            urls.append(f'https://www.biorxiv.org/content/{value}v1.full.pdf')
        match = RS_RE.match(value)
        if match:
            urls.append(
                f'https://www.researchsquare.com/article/{match.group(1)}/{match.group(2)}.pdf'
            )
    for url in paper.get('urls') or []:
        match = BIORXIV_RE.search(url)
        if match:
            urls.append(
                f'https://www.biorxiv.org/content/{match.group(1)}{match.group(2) or "v1"}.full.pdf'
            )
    seen, out = set(), []
    for url in urls:
        if url not in seen:
            seen.add(url)
            out.append(url)
    return out


def fetch_pdf(urls: list[str]) -> str | None:
    for url in urls:
        print(f'  pdf {url}', flush=True)
        data = download_bytes(url, timeout=90, browser=True)
        if not data or not data.startswith(b'%PDF'):
            print(f'  not a pdf ({0 if not data else len(data)} bytes)', flush=True)
            continue
        try:
            text = pdf_to_text(data)
        except Exception as exc:  # noqa: BLE001
            print(f'  pdf parse fail: {exc}', flush=True)
            continue
        if text and not is_garbage_text(text):
            return text
        print(f'  pdf text garbage or empty ({len(text or "")} chars)', flush=True)
    return None


def fallback_urls(paper: dict) -> list[str]:
    kind, value = paper['key'].split(':', 1)
    urls = []
    if kind == 'arxiv':
        urls.extend([
            f'https://arxiv.org/html/{value}',
            f'https://ar5iv.labs.arxiv.org/html/{value}',
        ])
    elif kind == 'acl':
        urls.append(f'https://aclanthology.org/{value}/')
    urls.extend(u for u in paper.get('urls') or [] if not u.lower().endswith('.pdf'))
    seen, out = set(), []
    for url in urls:
        if url not in seen:
            seen.add(url)
            out.append(url)
    return out


def missing_entry(key: str) -> dict:
    return {
        'key': key,
        'n_tokens': 0,
        'has_refs': False,
        'source': 'missing',
        'incomplete': True,
    }


def extract_paper(paper: dict) -> dict:
    key = paper['key']
    kind, value = key.split(':', 1)
    source = 'cache'
    markup = load_cached_html(key)
    if markup is not None and (len(markup) <= 2000 or is_garbage_text(markup)):
        markup = None
    if markup is None:
        source = 'download'
        for url in fallback_urls(paper):
            candidate = download_html(url)
            if candidate and len(candidate) > 2000 and not is_garbage_text(candidate):
                markup = candidate
                break
    markdown = ''
    if markup:
        markdown = html_to_markdown(markup)
        if is_garbage_text(markdown):
            markdown = ''
    # Abstract-only HTML (arXiv stubs, ACL landing pages) loses to a real PDF.
    if not markdown or estimate_tokens(markdown) < 3000:
        local = local_pdf_text(key)
        if local and len(local) > len(markdown):
            source = 'local-pdf'
            markdown = local
    if not markdown or estimate_tokens(markdown) < 3000:
        urls = list(EXTRA_PDF_URLS.get(key, ()))
        if kind == 'openreview':
            urls.extend(openreview_pdf_urls(value))
        else:
            urls.extend(pdf_fallback_urls(paper))
        remote = fetch_pdf(urls)
        if remote and len(remote) > len(markdown):
            source = 'pdf'
            markdown = remote
    path = FULLTEXT_DIR / f'{safe_key(key)}.md'
    if not markdown:
        if path.exists():
            path.unlink()
        return missing_entry(key)
    body, refs, appendix = split_sections(markdown)
    write_markdown(key, body, refs, appendix)
    tokens = estimate_tokens(path.read_text(encoding='utf-8'))
    return {
        'key': key,
        'n_tokens': tokens,
        'has_refs': bool(refs),
        'source': source,
        'incomplete': tokens < 3000,
        'path': path.name,
    }


def estimate_tokens(text: str) -> int:
    return max(1, len(text) // 4) if text else 0


def write_markdown(key: str, body: str, refs: str, appendix: str) -> Path:
    safe = safe_key(key)
    path = FULLTEXT_DIR / f'{safe}.md'
    FULLTEXT_DIR.mkdir(parents=True, exist_ok=True)
    chunks = [body]
    if refs:
        chunks.append(refs if refs.lstrip().startswith('#') else f'# References\n\n{refs}')
    if appendix:
        chunks.append(
            appendix if appendix.lstrip().startswith('#') else f'# Appendix\n\n{appendix}'
        )
    path.write_text('\n\n'.join(chunk for chunk in chunks if chunk).strip() + '\n', encoding='utf-8')
    return path


def zip_fulltext() -> None:
    with zipfile.ZipFile(FULLTEXT_ZIP, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(FULLTEXT_DIR.glob('*.md')):
            zf.write(path, arcname=path.name)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--only-keys', default='')
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    papers = read_jsonl(PAPERS_JSONL)
    if not papers:
        raise SystemExit('run filter/collect_readme.py first')
    wanted = {part.strip() for part in args.only_keys.split(',') if part.strip()}
    if wanted:
        papers = [paper for paper in papers if paper['key'] in wanted]
        if not papers:
            raise SystemExit(f'no papers match --only-keys {sorted(wanted)}')
    by_key = {row['key']: row for row in read_jsonl(FULLTEXT_INDEX)} if wanted else {}
    missing = 0
    short = 0
    total = len(papers)
    for done, paper in enumerate(papers, start=1):
        entry = extract_paper(paper)
        by_key[paper['key']] = entry
        if entry['source'] == 'missing':
            missing += 1
        elif entry.get('incomplete'):
            short += 1
        print(
            f'progress: {done}/{total} ({100 * done / total:.0f}%) '
            f'{paper["key"]} source={entry["source"]} tokens={entry["n_tokens"]}',
            flush=True,
        )
    if wanted:
        order = [row['key'] for row in read_jsonl(PAPERS_JSONL)]
        index = [by_key[key] for key in order if key in by_key]
    else:
        index = [by_key[paper['key']] for paper in papers]
    write_jsonl(FULLTEXT_INDEX, index)
    zip_fulltext()
    ok = total - missing
    print(
        f'wrote {FULLTEXT_DIR} ({ok} texts, {missing} missing, {short} <3k tokens) '
        f'and {FULLTEXT_ZIP}',
        flush=True,
    )


if __name__ == '__main__':
    main()
