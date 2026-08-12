import collections
import json
import re
from pathlib import Path
from urllib.parse import urlparse

from extract_papers import message_text

SKIP_DOMAINS = {
    't.me', 'instagram.com', 'open.spotify.com', 'youtu.be', 'youtube.com',
    'www.youtube.com', 'm.youtube.com', 'facebook.com', 'www.facebook.com',
    'twitter.com', 'x.com', 'linkedin.com', 'www.linkedin.com', 'reddit.com',
    'www.reddit.com', 'amazon.com', 'www.amazon.com', 'goodreads.com',
    'www.goodreads.com', 'xvideos.com', 'maps.app.goo.gl', 'google.com',
    'www.google.com', 'stackoverflow.com', 'i.scdn.co', 'archive.is',
    'imgur.com', 'i.imgur.com', 'telegra.ph', 'vc.ru', 'habr.com',
    'news.ycombinator.com', 'readhacker.news', 'medium.com', 'teletype.in',
    'en.wikipedia.org', 'ru.wikipedia.org', 'uk.wikipedia.org',
    'towardsdatascience.com', 'docs.google.com', 'drive.google.com',
    'colab.research.google.com', 'huggingface.co', 'github.com',
    'universe.roboflow.com', 'pypi.org', 'arxiv.org',
}
SKIP_SUBSTR = ('fbcdn.net', 'cdninstagram', 'fbsbx.com', 'scontent', 'tinyurl',
               'bit.ly', 'goo.gl', 't.co/', 'telegram.org', 'tenor.com',
               'giphy.com', 'twimg.com', '.jpg', '.png', '.gif', '.mp4')

URL_RE = re.compile(r'https?://[^\s<>"\')\]]+')


def main() -> None:
    messages = json.loads(Path('result.json').read_text(encoding='utf-8'))['messages']
    by_domain: dict[str, list[str]] = collections.defaultdict(list)
    pdfs: list[str] = []
    for msg in messages:
        for url in URL_RE.findall(message_text(msg)):
            url = url.rstrip('.,;:!?»\'"')
            low = url.lower()
            if any(s in low for s in SKIP_SUBSTR):
                continue
            domain = urlparse(url).netloc.lower()
            if domain in SKIP_DOMAINS:
                continue
            if low.endswith('.pdf') and url not in pdfs:
                pdfs.append(url)
            if url not in by_domain[domain]:
                by_domain[domain].append(url)

    print(f'=== PDF links ({len(pdfs)}) ===')
    for url in pdfs:
        print(url)

    print(f'\n=== domains ({len(by_domain)}) ===')
    for domain, urls in sorted(by_domain.items(), key=lambda kv: -len(kv[1])):
        print(f'{len(urls):4d}  {domain}')


if __name__ == '__main__':
    main()
