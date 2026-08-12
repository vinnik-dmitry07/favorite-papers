import json
import re
import time
import urllib.request
from pathlib import Path

IDS = [
    'BZ5a1r-kVsf', 'pOoKI3ouv1', 'hcQfTsVnBo', 'OpC-9aBBVJe', 'wUU-7XTL5XO',
    'ry_WPG-A-', 's0JVsx3bx1', 'bA6BgSbaUi', 'NhU661EZ9C', 'XyGJJ4FPoX',
]
UA = {'User-Agent': 'Mozilla/5.0 (compatible; key-papers/1.0)'}


def get(url: str) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=40) as resp:
        return resp.read()


def title_from_api(base: str, forum_id: str) -> str:
    data = json.loads(get(f'{base}/notes?forum={forum_id}'))
    for note in data.get('notes', []):
        raw = note.get('content', {}).get('title')
        if isinstance(raw, dict):
            raw = raw.get('value')
        if raw:
            return raw
    return ''


def main() -> None:
    out = {}
    for forum_id in IDS:
        title = ''
        errors = []
        for base in ('https://api2.openreview.net', 'https://api.openreview.net'):
            try:
                title = title_from_api(base, forum_id)
            except Exception as exc:  # noqa: BLE001
                errors.append(f'{base}: {exc}')
            if title:
                break
        if not title:
            try:
                html = get(
                    f'https://openreview.net/forum?id={forum_id}'
                ).decode('utf-8', 'ignore')
                match = re.search(
                    r'<meta name="citation_title" content="(.*?)"', html)
                if not match:
                    match = re.search(r'<title>(.*?)</title>', html, re.S)
                title = ' '.join(match.group(1).split()) if match else ''
            except Exception as exc:  # noqa: BLE001
                errors.append(f'html: {exc}')
        out[forum_id] = title or f'<unresolved> {errors}'
        print(f'{forum_id}: {out[forum_id][:120]}', flush=True)
        time.sleep(1)
    Path('openreview_titles.json').write_text(
        json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')


if __name__ == '__main__':
    main()
