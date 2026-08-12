import json
import re
from pathlib import Path

from extract_papers import message_text

PATTERN = re.compile(
    r'https?://(?:www\.)?(?:openreview\.net|nature\.com|science\.org|'
    r'jmlr\.org|distill\.pub|dl\.acm\.org|pnas\.org|cell\.com)/\S+'
)


def main() -> None:
    messages = json.loads(Path('result.json').read_text(encoding='utf-8'))['messages']
    seen = []
    for msg in messages:
        for url in PATTERN.findall(message_text(msg)):
            url = url.rstrip(').,\'"')
            if url not in seen:
                seen.append(url)
    print('\n'.join(seen))


if __name__ == '__main__':
    main()
