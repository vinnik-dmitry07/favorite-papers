import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path
from xml.etree import ElementTree

DUMP = Path('arxiv_dump.txt')
OUT = Path('papers_titles.json')
API = 'http://export.arxiv.org/api/query'
NS = {'a': 'http://www.w3.org/2005/Atom'}


def read_ids() -> list[str]:
    ids = []
    for line in DUMP.read_text(encoding='utf-8').splitlines():
        if '|' in line:
            ids.append(line.split('|', 1)[0].strip())
    return ids


def fetch(batch: list[str]) -> dict[str, dict]:
    query = urllib.parse.urlencode(
        {'id_list': ','.join(batch), 'max_results': len(batch)}
    )
    with urllib.request.urlopen(f'{API}?{query}', timeout=60) as resp:
        root = ElementTree.fromstring(resp.read())
    out = {}
    for entry in root.findall('a:entry', NS):
        url = entry.findtext('a:id', default='', namespaces=NS)
        match = re.search(r'abs/(.+?)(?:v\d+)?$', url)
        if not match:
            continue
        out[match.group(1)] = {
            'title': ' '.join(
                entry.findtext('a:title', default='', namespaces=NS).split()
            ),
            'published': entry.findtext('a:published', default='', namespaces=NS)[:10],
            'authors': [
                a.findtext('a:name', default='', namespaces=NS)
                for a in entry.findall('a:author', NS)
            ][:4],
        }
    return out


def main() -> None:
    ids = read_ids()
    result = {}
    size = 40
    for start in range(0, len(ids), size):
        batch = ids[start:start + size]
        try:
            result.update(fetch(batch))
        except Exception as exc:  # noqa: BLE001
            print(f'batch {start} failed: {exc}')
        print(f'progress: {min(start + size, len(ids))}/{len(ids)} '
              f'resolved={len(result)}', flush=True)
        time.sleep(3)
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    missing = [i for i in ids if i not in result]
    print(f'done. resolved {len(result)}/{len(ids)}; missing: {missing}')


if __name__ == '__main__':
    main()
