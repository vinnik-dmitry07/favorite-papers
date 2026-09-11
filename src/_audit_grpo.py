from collections import defaultdict
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent.parent
SRC = Path(r'D:\Downloads\Telegram Desktop\ChatExport_2026-08-19\result.json')
README = ROOT / 'readme.md'
OUT = ROOT / '_grpo_audit.txt'

data = json.loads(SRC.read_text(encoding='utf-8'))
readme = README.read_text(encoding='utf-8')

ARXIV = re.compile(
    r'(?:arxiv\.org/(?:abs|pdf|html)/|huggingface\.co/papers/|'
    r'alphaxiv\.org/(?:abs|pdf|html)/|ar5iv\.(?:labs\.)?arxiv\.org/(?:html|abs)/)'
    r'(\d{4}\.\d{4,5}|[a-z\-]+/\d{7})(?:v\d+)?',
    re.I,
)
ARXIV_INLINE = re.compile(r'arxiv[:\s]\s*(\d{4}\.\d{4,5})', re.I)
BARE_ID = re.compile(r'(?<![\d./v])(\d{2}(?:0[1-9]|1[0-2])\.\d{4,5})(?![\d.])')
OPENREVIEW = re.compile(r'openreview\.net/(?:forum\?id=|pdf\?id=)([A-Za-z0-9_\-]+)', re.I)
HF_PAPERS = re.compile(r'huggingface\.co/papers/(\d{4}\.\d{4,5})', re.I)

GRPO_HINT = re.compile(
    r'(?i)\b('
    r'grpo|gspo|dapo|dr\.?\s*grpo|gigpo|gppo|skpo|espo|sapo|'
    r'group[\s\-]?relative|group[\s\-]?sequence|'
    r'policy optimization|rlvr|rlhf|r1[\s\-]?zero|'
    r'deepseekmath|oat[\s\-]?zero|'
    r'critique[\s\-]?grpo|sr[\s\-]?grpo|sc[\s\-]?grpo|'
    r'ppo\b|dpo\b'
    r')\b'
)

README_IDS = set(re.findall(r'arxiv\.org/abs/(\d{4}\.\d{4,5}|[a-z\-]+/\d{7})', readme))
README_OR = set(re.findall(r'openreview\.net/(?:forum|pdf)\?id=([A-Za-z0-9_\-]+)', readme))


def walk_strings(obj):
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from walk_strings(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from walk_strings(v)


def message_blob(msg: dict) -> str:
    chunks = []
    for field in ('text', 'text_entities', 'caption', 'caption_entities'):
        if field in msg:
            chunks.extend(walk_strings(msg[field]))
    for field in (
        'file', 'file_name', 'media_type', 'mime_type',
        'forwarded_from', 'via_bot', 'author',
    ):
        val = msg.get(field)
        if isinstance(val, str):
            chunks.append(val)
    for key in ('photo', 'document', 'video', 'audio'):
        if key in msg:
            chunks.extend(walk_strings(msg[key]))
    return '\n'.join(chunks)


def normalize_id(arxiv_id: str) -> str:
    return re.sub(r'v\d+$', '', arxiv_id)


messages = data['messages']
by_id = defaultdict(list)
or_by_id = defaultdict(list)
grpo_msgs = []
all_ids_in_grpo_msgs = set()
all_or_in_grpo_msgs = set()

for msg in messages:
    blob = message_blob(msg)
    if not blob.strip():
        continue
    ids = {normalize_id(x) for x in ARXIV.findall(blob)}
    ids |= {normalize_id(x) for x in ARXIV_INLINE.findall(blob)}
    ids |= {normalize_id(x) for x in HF_PAPERS.findall(blob)}
    if re.search(r'(?i)(arxiv|paper|статья|препринт|abs/|huggingface\.co/papers)', blob):
        ids |= set(BARE_ID.findall(blob))
    ors = set(OPENREVIEW.findall(blob))
    for arxiv_id in ids:
        by_id[arxiv_id].append(msg.get('id'))
    for forum in ors:
        or_by_id[forum].append(msg.get('id'))
    if GRPO_HINT.search(blob):
        snippet = ' '.join(blob.split())[:400]
        grpo_msgs.append({
            'id': msg.get('id'),
            'date': msg.get('date'),
            'from': msg.get('forwarded_from') or msg.get('from'),
            'ids': sorted(ids),
            'openreview': sorted(ors),
            'snippet': snippet,
        })
        all_ids_in_grpo_msgs |= ids
        all_or_in_grpo_msgs |= ors

# Also treat as GRPO-related any paper whose title/readme line mentions GRPO,
# plus any paper appearing in a GRPO message.
readme_grpo_ids = set()
for line in readme.splitlines():
    if GRPO_HINT.search(line):
        readme_grpo_ids |= set(re.findall(r'arxiv\.org/abs/(\d{4}\.\d{4,5})', line))

missing_ids = sorted(all_ids_in_grpo_msgs - README_IDS)
present_ids = sorted(all_ids_in_grpo_msgs & README_IDS)
missing_or = sorted(all_or_in_grpo_msgs - README_OR)
all_missing = sorted(set(by_id) - README_IDS)

lines = []
lines.append(f'export name: {data.get("name")}')
lines.append(f'messages: {len(messages)}')
lines.append(f'unique arxiv in export: {len(by_id)}')
lines.append(f'unique arxiv in readme: {len(README_IDS)}')
lines.append(f'grpo-hint messages: {len(grpo_msgs)}')
lines.append(f'arxiv in grpo-hint messages: {len(all_ids_in_grpo_msgs)}')
lines.append(f'already in readme: {len(present_ids)}')
lines.append(f'MISSING from readme (grpo-hint msgs): {len(missing_ids)}')
lines.append(f'MISSING openreview from readme (grpo-hint msgs): {len(missing_or)}')
lines.append(f'ALL export ids missing from readme: {len(all_missing)}')
lines.append('')
lines.append('=== MISSING GRPO-CONTEXT ARXIV ===')
for arxiv_id in missing_ids:
    lines.append(f'{arxiv_id}  msgs={by_id[arxiv_id]}')
lines.append('')
lines.append('=== MISSING GRPO-CONTEXT OPENREVIEW ===')
for forum in missing_or:
    lines.append(f'{forum}  msgs={or_by_id[forum]}')
lines.append('')
lines.append('=== GRPO-HINT MESSAGES ===')
for item in grpo_msgs:
    lines.append(
        f"--- msg {item['id']} {item['date']} from={item['from']} "
        f"ids={item['ids']} or={item['openreview']}"
    )
    lines.append(item['snippet'])
    lines.append('')
lines.append('=== ALL EXPORT IDS NOT IN README ===')
for arxiv_id in all_missing:
    lines.append(f'{arxiv_id}  msgs={by_id[arxiv_id]}')

OUT.write_text('\n'.join(lines), encoding='utf-8')
print(f'wrote {OUT} ({OUT.stat().st_size} bytes)')
print(f'grpo-hint messages: {len(grpo_msgs)}')
print(f'missing grpo-context arxiv: {missing_ids}')
print(f'missing grpo-context openreview: {missing_or}')
print(f'all missing count: {len(all_missing)}')
