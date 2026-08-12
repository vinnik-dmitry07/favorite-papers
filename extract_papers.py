import json
import re
from pathlib import Path

SRC = Path('result.json')
OUT = Path('arxiv_dump.txt')

ARXIV_RE = re.compile(
    r'arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5}|[a-z\-]+/\d{7})', re.I
)


def message_text(msg: dict) -> str:
    text = msg.get('text')
    if isinstance(text, str):
        return text
    parts = []
    for part in text or []:
        if isinstance(part, str):
            parts.append(part)
        elif part.get('type') in ('link', 'text_link') and part.get('href'):
            parts.append(part['href'])
        else:
            parts.append(part.get('text', ''))
    return ''.join(parts)


def main() -> None:
    messages = json.loads(SRC.read_text(encoding='utf-8'))['messages']
    found = {}
    for msg in messages:
        text = message_text(msg)
        for arxiv_id in ARXIV_RE.findall(text):
            arxiv_id = re.sub(r'v\d+$', '', arxiv_id)
            found.setdefault(arxiv_id, (msg.get('date', ''), text.strip()))

    lines = [f'total unique arxiv ids: {len(found)}', '']
    for arxiv_id, (date, text) in sorted(found.items()):
        snippet = ' '.join(text.split())[:250]
        lines.append(f'{arxiv_id} | {date} | {snippet}')
    OUT.write_text('\n'.join(lines), encoding='utf-8')
    print(OUT.read_text(encoding='utf-8'))


if __name__ == '__main__':
    main()
