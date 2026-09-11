import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
d = json.loads((ROOT / 'result.json').read_text(encoding='utf-8'))
ms = [m for m in d['messages'] if m.get('type') == 'message']


def txt(msg: dict) -> str:
    text = msg.get('text')
    if isinstance(text, str):
        return text
    parts = []
    for part in text or []:
        if isinstance(part, str):
            parts.append(part)
        else:
            parts.append(part.get('href') or part.get('text', ''))
    return ''.join(parts)


kinds = Counter()
for msg in ms:
    fid = msg.get('forwarded_from_id')
    if fid:
        match = re.match(r'[A-Za-z_]+', fid)
        kinds[match.group(0) if match else fid] += 1
print('forwarded_from_id kinds:', kinds)

paper_re = re.compile(
    r'arxiv\.org|openreview\.net|transformer-circuits|doi\.org|aclanthology',
    re.I,
)
tme_re = re.compile(r'https?://t\.me/([A-Za-z0-9_]+)/(\d+)')
with_tme = without = 0
examples = []
for msg in ms:
    text = txt(msg)
    if not paper_re.search(text):
        continue
    hits = tme_re.findall(text)
    if hits:
        with_tme += 1
        if len(examples) < 8:
            examples.append((msg['id'], msg.get('forwarded_from'), hits[:3]))
    else:
        without += 1
print(f'paper msgs with t.me/post: {with_tme}, without: {without}')
for example in examples:
    print(example)

print('--- channel forwards with papers ---')
n = 0
for msg in ms:
    fid = msg.get('forwarded_from_id', '')
    if not str(fid).startswith('channel'):
        continue
    text = txt(msg)
    if not paper_re.search(text):
        continue
    print(msg.get('forwarded_from'), fid, msg.get('saved_from'), msg['id'])
    print(text[:180].replace('\n', ' '))
    print('---')
    n += 1
    if n >= 5:
        break

print('unique forwarded_from channel names:')
names = Counter()
for msg in ms:
    fid = msg.get('forwarded_from_id', '')
    if str(fid).startswith('channel'):
        names[msg.get('forwarded_from')] += 1
print(names.most_common(30))
