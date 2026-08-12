import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path
from xml.etree import ElementTree

IDS = [
    '2201.09746', '1905.10985', '2505.22954', '2509.03646', '2508.16204',
    '2112.04035', '2505.13763', '2502.00873', '2405.15071',
]
NS = {'a': 'http://www.w3.org/2005/Atom'}
UA = {'User-Agent': 'key-papers/1.0'}


def get(url: str) -> bytes:
    last = None
    for attempt in range(5):
        try:
            with urllib.request.urlopen(url, timeout=60) as resp:
                return resp.read()
        except Exception as exc:  # noqa: BLE001
            last = exc
            print(f'  retry {attempt + 1}/5 after {exc}', flush=True)
            time.sleep(10 * (attempt + 1))
    raise last


def main() -> None:
    query = urllib.parse.urlencode({'id_list': ','.join(IDS), 'max_results': len(IDS)})
    root = ElementTree.fromstring(get(f'http://export.arxiv.org/api/query?{query}'))
    out = {}
    for entry in root.findall('a:entry', NS):
        arxiv_id = re.search(
            r'abs/(.+?)(?:v\d+)?$', entry.findtext('a:id', '', NS)).group(1)
        out[arxiv_id] = {
            'title': ' '.join(entry.findtext('a:title', '', NS).split()),
            'published': entry.findtext('a:published', '', NS)[:10],
            'authors': [a.findtext('a:name', '', NS)
                        for a in entry.findall('a:author', NS)][:3],
        }
    known = set(json.loads(Path('papers_titles.json').read_text(encoding='utf-8')))
    for arxiv_id in IDS:
        info = out.get(arxiv_id)
        flag = 'already listed' if arxiv_id in known else 'NEW'
        if info:
            print(f'{arxiv_id} [{flag}] {info["published"]} — {info["title"]} '
                  f'({", ".join(info["authors"])})')
        else:
            print(f'{arxiv_id} [{flag}] <not resolved>')
    Path('added_titles.json').write_text(
        json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')


if __name__ == '__main__':
    main()
