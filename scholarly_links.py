import json
import re
from pathlib import Path
from urllib.parse import urlparse

from extract_papers import message_text

SCHOLARLY = {
    'papers.ssrn.com', 'direct.mit.edu', 'www.researchgate.net',
    'www.semanticscholar.org', 'link.springer.com', 'onlinelibrary.wiley.com',
    'www.mdpi.com', 'www.cambridge.org', 'royalsocietypublishing.org',
    'journals.plos.org', 'psyarxiv.com', 'osf.io', 'pubmed.ncbi.nlm.nih.gov',
    'www.ncbi.nlm.nih.gov', 'www.thelancet.com', 'spie.org', 'www.computer.org',
    'transformer-circuits.pub', 'alignment.anthropic.com', 'nips.cc', 'iclr.cc',
    'philpapers.org', 'hal.archives-ouvertes.fr', 'www.groundai.com',
    'physics.allen-zhu.com', 'people.idsia.ch', 'research.nvidia.com',
    'www.ml.cmu.edu', 'rail.eecs.berkeley.edu', 'bair.berkeley.edu',
    'sci-hub.se', 'sci-hub.ru', 'www.cochranelibrary.com', 'gwern.net',
    'epochai.org', 'thegradient.pub', 'compcogneuro.org', 'www.lesswrong.com',
    'abehrouz.github.io', 'www.science.org', 'www.cell.com', 'www.sciencedirect.com',
    'www.biorxiv.org', 'doi.org', 'openai.com', 'www.anthropic.com', 'ai.meta.com',
    'ai.facebook.com', 'research.google', 'ai.googleblog.com', 'blog.google',
    'deepmind.google', 'www.deepmind.com', 'cdn.openai.com', 'sakana.ai',
    'normalcomputing.ai', 'minedojo.org', 'selfrag.github.io',
    'diamond-wm.github.io', 'latent-consistency-models.github.io',
    'hyperdreambooth.github.io', 'wang-kevin3290.github.io',
    'explorative-modeling.github.io', 'powerpaint.github.io',
    'emu-video.metademolab.com', 'dinov2.metademolab.com',
    'google-research.github.io', 'uber.github.io', 'johnchenresearch.github.io',
    'haotianye.com', 'silviasapora.github.io', 'haiyuwu.github.io',
    'schema-harness.github.io', 'neuroevolutionbook.com', 'rl-book.com',
    'rlhfbook.com', 'situational-awareness.ai', 'ai-2027.com',
    'herasight-project.webflow.io', 'www.educatingsilicon.com',
    'transluce.org', 'ceobench.com', 'thinkingmachines.ai',
}
URL_RE = re.compile(r'https?://[^\s<>"\')\]]+')


def main() -> None:
    messages = json.loads(Path('result.json').read_text(encoding='utf-8'))['messages']
    seen = set()
    for msg in messages:
        text = ' '.join(message_text(msg).split())
        for match in URL_RE.finditer(text):
            url = match.group(0).rstrip('.,;:!?»\'"')
            if urlparse(url).netloc.lower() not in SCHOLARLY or url in seen:
                continue
            seen.add(url)
            start = max(0, match.start() - 260)
            end = min(len(text), match.end() + 160)
            source = msg.get('forwarded_from') or '-'
            print(f'### {url}\n[{source} | {msg.get("date")}] ...'
                  f'{text[start:end]}...\n')
    print(f'total: {len(seen)}')


if __name__ == '__main__':
    main()
