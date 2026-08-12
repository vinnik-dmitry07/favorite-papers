import collections
import json
import re
from pathlib import Path

from extract_papers import message_text

ML_SOURCES = {
    'gonzo-обзоры ML статей': 'gonzo_ML',
    'Data Secrets': 'data_secrets',
    'Борис опять': 'boris_again',
    'Denis Sexy IT 🤖': 'denissexy',
    'эйай ньюз': 'ai_newz',
    'Нейроэкзистенциализм': 'neuroexistencialism',
    'Агенты ИИ | AGI_and_RL': 'AGI_and_RL',
    'Axis of Ordinary': 'axisofordinary',
    'Сиолошная': 'seeallochnaya',
    'Love. Death. Transformers.': 'lovedeathtransformers',
    'Just links': 'j_links',
    'AbstractDL': 'abstractDL',
    'Knowledge Accumulator': 'knowledge_accumulator',
    'Техножрица 👩‍💻👩‍🏫👩‍🔧': 'tech_priestess',
    'DLStories': 'dl_stories',
    'Dealer.AI': 'dealerAI',
    'AI для Всех': 'nn_for_science',
    'Derp Learning': 'derplearning',
    'Сайнс за минуту': '?',
    'partially unsupervised': 'partially_unsupervised',
    'Techsparks': 'techsparks',
    'Не Джанов': 'nejdanov',
    'Мишин Лернинг 🇺🇦🇮🇱': 'mishin_learning',
    'Doom Grad': 'doomgrad',
    'Kali Novskaya': 'rybolos_channel',
}

# Everything that can encode a paper reference, beyond plain arxiv.org links.
PATTERNS = {
    'arxiv_inline': re.compile(r'arxiv[:\s]\s*(\d{4}\.\d{4,5})', re.I),
    'arxiv_listing': re.compile(r'arxiv\.org/(?!abs|pdf|html)\S+', re.I),
    'hf_papers': re.compile(r'huggingface\.co/papers/(\d{4}\.\d{4,5})', re.I),
    'alphaxiv': re.compile(r'alphaxiv\.org/\S+', re.I),
    'ar5iv': re.compile(r'ar5iv\.\S+/(\d{4}\.\d{4,5})', re.I),
    'openreview': re.compile(r'openreview\.net/\S+', re.I),
    'acl': re.compile(r'aclanthology\.org/\S+', re.I),
    'pmlr': re.compile(r'proceedings\.mlr\.press/\S+', re.I),
    'neurips': re.compile(r'(?:papers\.)?(?:proceedings\.)?neurips\.cc/\S+', re.I),
    'biorxiv': re.compile(r'(?:bio|med|psy)rxiv\.org/\S+', re.I),
    'doi': re.compile(r'(?:doi\.org|dx\.doi\.org)/\S+', re.I),
    'semanticscholar': re.compile(r'semanticscholar\.org/\S+', re.I),
    'paperswithcode': re.compile(r'paperswithcode\.com/paper/\S+', re.I),
    'journals': re.compile(
        r'(?:nature|science|cell|pnas|jmlr|distill|sciencedirect|springer|'
        r'academic\.oup|royalsocietypublishing|frontiersin|plos|elifesciences)'
        r'[\w.]*\.\w+/\S+', re.I),
    'labs': re.compile(
        r'(?:openai\.com/(?:research|index)|deepmind\.(?:com|google)/\S*'
        r'(?:research|publications|blog)|ai\.meta\.com/research|'
        r'anthropic\.com/(?:research|news)|research\.google/\S*pubs)/?\S*', re.I),
}

BARE_ID = re.compile(r'(?<![\d./v])(\d{2}(?:0[1-9]|1[0-2])\.\d{4,5})(?![\d.])')


def known_ids() -> set[str]:
    return set(json.loads(Path('papers_titles.json').read_text(encoding='utf-8')))


def source_of(msg: dict) -> str | None:
    src = msg.get('forwarded_from')
    if src in ML_SOURCES:
        return ML_SOURCES[src]
    return src


def main() -> None:
    messages = json.loads(Path('result.json').read_text(encoding='utf-8'))['messages']
    known = known_ids()
    new_ids: dict[str, str] = {}
    hits: dict[str, list[tuple[str, str]]] = collections.defaultdict(list)

    for msg in messages:
        text = message_text(msg)
        if not text:
            continue
        src = source_of(msg) or ''
        for name, pattern in PATTERNS.items():
            for match in pattern.findall(text):
                value = match if isinstance(match, str) else match[0]
                value = value.rstrip(').,;\'"»')
                if name in ('arxiv_inline', 'hf_papers', 'ar5iv'):
                    if value not in known:
                        new_ids.setdefault(value, src)
                    continue
                pair = (value, src)
                if pair not in hits[name]:
                    hits[name].append(pair)
        for value in BARE_ID.findall(text):
            if value not in known and value not in new_ids:
                # only trust bare ids in a paper-ish context
                if re.search(r'(?i)(статья|paper|arxiv|препринт|abs/)', text):
                    new_ids[value] = src

    print(f'== new arxiv ids not in current list: {len(new_ids)}')
    for arxiv_id, src in sorted(new_ids.items()):
        print(f'{arxiv_id}  [{src}]')

    for name, pairs in hits.items():
        print(f'\n== {name} ({len(pairs)})')
        for value, src in pairs:
            print(f'{value}  [{src}]')


if __name__ == '__main__':
    main()
