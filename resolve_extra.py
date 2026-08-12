import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path
from xml.etree import ElementTree

UA = {'User-Agent': 'key-papers/1.0 (research notes compiler)'}

NEW_ARXIV = ['2405.12250', '2501.04519', '2501.05441', '2201.00650']

OPENREVIEW = [
    'BZ5a1r-kVsf', 'pOoKI3ouv1', 'hcQfTsVnBo', 'OpC-9aBBVJe', 'wUU-7XTL5XO',
    'ry_WPG-A-', 's0JVsx3bx1', 'bA6BgSbaUi', 'NhU661EZ9C', 'XyGJJ4FPoX',
]

ACL = [
    '2022.acl-long.360', '2022.emnlp-main.340', '2023.acl-demo.51',
    '2025.acl-long.126',
]

DOIS = [
    '10.1038/s44222-022-00001-9', '10.1038/s42256-023-00754-x',
    '10.1038/d41586-024-01413-w', '10.1038/s41566-024-01394-2',
    '10.1038/s41377-022-00717-8', '10.1038/s41586-024-07522-w',
    '10.1038/s41586-024-07711-7', '10.1038/s41582-021-00464-1',
    '10.1038/s41583-022-00642-0', '10.1038/s41467-021-26568-2',
    '10.1126/science.adn9083', '10.1371/journal.pcbi.1011005',
    '10.1111/tops.12278', '10.1137/030601879',
]

BIORXIV = [
    '10.1101/2023.04.04.535512', '10.1101/2023.03.27.534424',
    '10.1101/2024.05.24.595748', '10.1101/2024.02.22.581686',
]


def get(url: str, timeout: int = 40) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def arxiv_titles(ids: list[str]) -> dict[str, str]:
    ns = {'a': 'http://www.w3.org/2005/Atom'}
    query = urllib.parse.urlencode({'id_list': ','.join(ids), 'max_results': len(ids)})
    root = ElementTree.fromstring(get(f'http://export.arxiv.org/api/query?{query}'))
    out = {}
    for entry in root.findall('a:entry', ns):
        url = entry.findtext('a:id', default='', namespaces=ns)
        match = re.search(r'abs/(.+?)(?:v\d+)?$', url)
        title = ' '.join(entry.findtext('a:title', default='', namespaces=ns).split())
        if match:
            out[match.group(1)] = title
    return out


def openreview_titles(ids: list[str]) -> dict[str, str]:
    out = {}
    for forum_id in ids:
        title = ''
        for api in ('https://api2.openreview.net/notes?forum=',
                    'https://api.openreview.net/notes?forum='):
            try:
                data = json.loads(get(f'{api}{urllib.parse.quote(forum_id)}'))
            except Exception:  # noqa: BLE001
                continue
            for note in data.get('notes', []):
                raw = note.get('content', {}).get('title')
                if isinstance(raw, dict):
                    raw = raw.get('value')
                if raw:
                    title = raw
                    break
            if title:
                break
        out[forum_id] = title or '<not resolved>'
        print(f'  openreview {forum_id}: {out[forum_id][:80]}', flush=True)
        time.sleep(1)
    return out


def acl_titles(ids: list[str]) -> dict[str, str]:
    out = {}
    for paper_id in ids:
        try:
            html = get(f'https://aclanthology.org/{paper_id}/').decode(
                'utf-8', 'ignore')
            match = re.search(r'<title>(.*?)</title>', html, re.S)
            out[paper_id] = ' '.join(match.group(1).split()) if match else '?'
        except Exception as exc:  # noqa: BLE001
            out[paper_id] = f'<error: {exc}>'
        print(f'  acl {paper_id}: {out[paper_id][:90]}', flush=True)
        time.sleep(1)
    return out


def crossref_titles(dois: list[str]) -> dict[str, str]:
    out = {}
    for doi in dois:
        try:
            data = json.loads(get(f'https://api.crossref.org/works/{doi}'))
            msg = data['message']
            title = ' '.join(msg.get('title', ['?'])[0].split())
            year = msg.get('issued', {}).get('date-parts', [['?']])[0][0]
            out[doi] = f'{title} ({year}, {msg.get("container-title", ["?"])[0]})'
        except Exception as exc:  # noqa: BLE001
            out[doi] = f'<error: {exc}>'
        print(f'  doi {doi}: {out[doi][:100]}', flush=True)
        time.sleep(1)
    return out


def biorxiv_titles(dois: list[str]) -> dict[str, str]:
    out = {}
    for doi in dois:
        try:
            data = json.loads(get(f'https://api.biorxiv.org/details/biorxiv/{doi}'))
            coll = data.get('collection', [])
            out[doi] = coll[-1]['title'] if coll else '?'
        except Exception as exc:  # noqa: BLE001
            out[doi] = f'<error: {exc}>'
        print(f'  biorxiv {doi}: {out[doi][:90]}', flush=True)
        time.sleep(1)
    return out


def main() -> None:
    result = {}
    print('arxiv...', flush=True)
    result['arxiv'] = arxiv_titles(NEW_ARXIV)
    for k, v in result['arxiv'].items():
        print(f'  {k}: {v}')
    print('openreview...', flush=True)
    result['openreview'] = openreview_titles(OPENREVIEW)
    print('acl...', flush=True)
    result['acl'] = acl_titles(ACL)
    print('crossref...', flush=True)
    result['doi'] = crossref_titles(DOIS)
    print('biorxiv...', flush=True)
    result['biorxiv'] = biorxiv_titles(BIORXIV)
    Path('extra_titles.json').write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print('saved extra_titles.json')


if __name__ == '__main__':
    main()
