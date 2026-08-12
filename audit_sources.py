import collections
import json
import re
from pathlib import Path

from extract_papers import message_text

CHANNELS = Path('channels.txt').read_text(encoding='utf-8').split()


def main() -> None:
    messages = json.loads(Path('result.json').read_text(encoding='utf-8'))['messages']
    fwd = collections.Counter()
    for msg in messages:
        src = msg.get('forwarded_from')
        if src:
            fwd[src] += 1
    print(f'messages with forwarded_from: {sum(fwd.values())}, '
          f'unique sources: {len(fwd)}')
    for name, count in fwd.most_common(60):
        print(f'{count:5d}  {name}')

    print('\n--- t.me handles mentioned in text ---')
    handles = collections.Counter()
    for msg in messages:
        for h in re.findall(r't\.me/([A-Za-z0-9_]+)', message_text(msg)):
            handles[h.lower()] += 1
    wanted = {c.rsplit('/', 1)[-1].lower() for c in CHANNELS}
    for h, count in handles.most_common():
        mark = '*' if h in wanted else ' '
        print(f'{mark} {count:5d}  {h}')


if __name__ == '__main__':
    main()
