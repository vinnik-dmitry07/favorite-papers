'''Parse reviewer markdown into rating / decision / S/P/C. No GPU imports.'''

from __future__ import annotations

import re

AVG_RE = re.compile(
    r'avg(?:erage)?\s*(?:rating|score)\s*[:\-]?\s*(\d{1,2}(?:\.\d+)?)',
    re.I,
)
DECISION_RE = re.compile(
    r'(?:paper\s+)?decision\b[^\n]{0,80}?\b(accept|reject)\b',
    re.I,
)
DECISION_LINE_RE = re.compile(
    r'(?m)^\s*[-*]?\s*decision\s*[:\-]\s*(accept|reject)\b',
    re.I,
)
DECISION_HEAD_RE = re.compile(
    r'(?:^|\n)#{1,3}\s*(?:paper\s+)?decision\b[^\n]*\n+\s*[:\-*]*\s*(accept|reject)\b',
    re.I,
)
DECISION_NL_RE = re.compile(
    r'(?:\*\*)?(?:paper\s+)?decision(?:\*\*)?\s*[:\-]?\*{0,2}\s*(?:\n\s*)+(accept|reject)\b',
    re.I,
)
WEAK_RE = re.compile(
    r'(?:\*\*)?weakness(?:es)?(?:\*\*)?\s*:?\s*(.*?)(?:\n\s*\n|\*\*questions|\*\*rating|\*\*paper|#{1,3}\s+questions)',
    re.I | re.S,
)
THINK_RE = re.compile(r'<think>.*?</think>', re.I | re.S)
BOXED_START_RE = re.compile(r'\\?boxed_review\{', re.I)
HEADING_RATING_RE = re.compile(
    r'(?:^|\n)#{1,3}\s*rating\b[^\n]*\n+\s*[:\-*]*\s*(\d{1,2}(?:\.\d+)?)',
    re.I,
)
META_HEAD_RE = re.compile(r'^#{1,3}\s*meta\s+review\b', re.I | re.M)
RUBRIC_AFTER = re.compile(r'\s*:\s*(excellent|good|fair|poor)\b', re.I)


def _brace_body(text: str, open_idx: int) -> str | None:
    depth = 0
    i = open_idx
    while i < len(text):
        ch = text[i]
        if ch == '\\' and i + 1 < len(text):
            i += 2
            continue
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0:
                return text[open_idx + 1:i]
        i += 1
    return None


def extract_boxed_review(text: str) -> str | None:
    starts = list(BOXED_START_RE.finditer(text or ''))
    if not starts:
        return None
    for match in reversed(starts):
        body = _brace_body(text, match.end() - 1)
        if body:
            return body
    return None


def first_score(
    text: str,
    label: str,
    *,
    last: bool = True,
    lo: float | None = None,
    hi: float | None = None,
) -> float | None:
    heading = re.compile(
        rf'(?:^|\n)#{{1,3}}\s*{label}\b[^\n]*\n+\s*[:\-*]*\s*(\d{{1,2}}(?:\.\d+)?)',
        re.I,
    )
    inline = re.compile(
        rf'(?:\*\*)?{label}(?:\*\*)?\s*[:\-]?\*{{0,2}}\s*(?:\n\s*)?(\d{{1,2}}(?:\.\d+)?)',
        re.I,
    )
    body = text or ''
    hits = []
    for match in list(heading.finditer(body)) + list(inline.finditer(body)):
        value = float(match.group(1))
        if lo is not None and value < lo:
            continue
        if hi is not None and value > hi:
            continue
        if RUBRIC_AFTER.match(body[match.end():match.end() + 24]):
            continue
        hits.append((match.start(), value))
    if not hits:
        return None
    hits.sort()
    return hits[-1][1] if last else hits[0][1]


def parse_decision(body: str) -> str | None:
    for rex in (DECISION_HEAD_RE, DECISION_NL_RE, DECISION_LINE_RE, DECISION_RE):
        hits = list(rex.finditer(body))
        if hits:
            return hits[-1].group(1).capitalize()
    return None


def _fields_from(body: str, kind: str = '') -> dict:
    rating = None
    if kind == 'cycle':
        cut = META_HEAD_RE.search(body)
        head = body[:cut.start()] if cut else body
        ratings = []
        for match in HEADING_RATING_RE.finditer(head):
            value = float(match.group(1))
            if 1 <= value <= 10:
                ratings.append(value)
        if ratings:
            rating = sum(ratings) / len(ratings)
    if rating is None:
        avgs = list(AVG_RE.finditer(body))
        if avgs:
            rating = float(avgs[-1].group(1))
        else:
            rating = first_score(body, r'(?:overall\s+)?rating', last=True, lo=1, hi=10)
    if rating is not None:
        rating = min(10.0, max(1.0, rating))
    decision = parse_decision(body)
    if decision is None and rating is not None:
        decision = 'Accept' if rating >= 6 else 'Reject'
    weak = WEAK_RE.search(body)
    return {
        'rating': rating,
        'decision': decision,
        'soundness': first_score(body, 'soundness', last=True, lo=1, hi=4),
        'presentation': first_score(body, 'presentation', last=True, lo=1, hi=4),
        'contribution': first_score(body, 'contribution', last=True, lo=1, hi=4),
        'weaknesses': ' '.join((weak.group(1) if weak else '').split())[:400],
    }


def parse_review(text: str, kind: str = '') -> dict:
    body = text or ''
    if kind == 'deep':
        body = THINK_RE.sub('', body)
        boxed = extract_boxed_review(body)
        if boxed:
            boxed_fields = _fields_from(boxed)
            if boxed_fields['rating'] is not None or boxed_fields['decision'] is not None:
                return boxed_fields
    return _fields_from(body, kind=kind)
