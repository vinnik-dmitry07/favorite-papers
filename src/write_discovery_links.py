'''Write the workers.dev origin into the map and readme after a live smoke.

A missing or failed smoke leaves both files alone. The origin has to be an
https host under workers.dev. This script does not invent one.
'''

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_agent_index import SMOKE_PATH  # noqa: E402
from common import README, ROOT  # noqa: E402

HTML = ROOT / 'src' / 'index.html'
MAP_URL = '(https://vinnik-dmitry07.github.io/favorite-papers/)'


def valid_origin(origin: str) -> bool:
    parsed = urlparse(origin)
    host = parsed.hostname or ''
    return (
        parsed.scheme == 'https'
        and host.endswith('.workers.dev')
        and parsed.username is None
        and parsed.path in ('', '/')
        and parsed.query == ''
        and parsed.fragment == ''
    )


def worker_origin(log: str, worker_name: str) -> str:
    '''The workers.dev URL wrangler printed for this worker, or ''.'''
    prefix = 'https://' + worker_name + '.'
    for item in re.findall(r'https://[A-Za-z0-9.-]+\.workers\.dev', log):
        if item.startswith(prefix) and valid_origin(item):
            return item
    return ''


def update_html(text: str, origin: str) -> str:
    link = f'<a id="agent-api" href="{origin}">agent API</a>'
    marker = '<a id="agent-api" href="'
    if marker in text:
        start = text.index(marker)
        end = text.index('</a>', start) + len('</a>')
        return text[:start] + link + text[end:]
    needle = '</h1>'
    if needle not in text:
        raise ValueError('map header has no h1')
    return text.replace(needle, f'{needle}\n  {link}', 1)


def update_readme(text: str, origin: str) -> str:
    sentence = f' Agent API: [{origin}]({origin}).'
    pattern = re.compile(r' Agent API: \[[^\]]+\]\(https://[^)]+\)\.')
    if pattern.search(text):
        return pattern.sub(sentence, text, count=1)
    if MAP_URL not in text:
        raise ValueError('readme intro has no live map link')
    return text.replace(MAP_URL, MAP_URL + sentence, 1)


def _flag(args: list[str], name: str, default: Path) -> Path:
    if name not in args:
        return default
    return Path(args[args.index(name) + 1])


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    smoke_path = _flag(args, '--smoke', SMOKE_PATH)
    html_path = _flag(args, '--html', HTML)
    readme_path = _flag(args, '--readme', README)
    if not smoke_path.is_file():
        print('discovery links unchanged: no successful smoke')
        return 0
    smoke = json.loads(smoke_path.read_text(encoding='utf-8'))
    origin = smoke.get('origin') or ''
    if smoke.get('ok') is not True or not valid_origin(origin):
        print('discovery links unchanged: smoke did not verify a workers.dev origin')
        return 0
    html_path.write_text(
        update_html(html_path.read_text(encoding='utf-8'), origin),
        encoding='utf-8',
    )
    readme_path.write_text(
        update_readme(readme_path.read_text(encoding='utf-8'), origin),
        encoding='utf-8',
    )
    print(f'discovery links updated for {origin}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
