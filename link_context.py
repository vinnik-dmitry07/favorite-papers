import json
import re
from pathlib import Path

from extract_papers import message_text

TARGETS = [
    'openreview.net', 'aclanthology.org', 'proceedings.neurips.cc',
    'paperswithcode.com/paper', 'huggingface.co/papers',
]


def main() -> None:
    messages = json.loads(Path('result.json').read_text(encoding='utf-8'))['messages']
    seen = set()
    for msg in messages:
        text = ' '.join(message_text(msg).split())
        if not any(t in text for t in TARGETS):
            continue
        for match in re.finditer(
                r'https?://\S*(?:openreview\.net|aclanthology\.org|'
                r'proceedings\.neurips\.cc|paperswithcode\.com/paper|'
                r'huggingface\.co/papers)\S*', text):
            url = match.group(0).rstrip(').,;\'"')
            if url in seen:
                continue
            seen.add(url)
            start = max(0, match.start() - 350)
            end = min(len(text), match.end() + 250)
            source = msg.get('forwarded_from') or '-'
            print(f'### {url}\n[{source} | {msg.get("date")}]\n'
                  f'...{text[start:end]}...\n')


if __name__ == '__main__':
    main()
