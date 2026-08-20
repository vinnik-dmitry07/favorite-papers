import json
import re
from pathlib import Path

RESULT = Path('result.json')
PAPERS = Path('readme.md')
OUT = Path('readme.md')

CHAT_ID = 268338453  # Saved Messages peer from export

CHANNEL_HANDLES = {
    'gonzo-обзоры ml статей': 'gonzo_ML',
    'data secrets': 'data_secrets',
    'борис опять': 'boris_again',
    'denis sexy it 🤖': 'denissexy',
    'эйай ньюз': 'ai_newz',
    'нейроэкзистенциализм': 'neuroexistencialism',
    'агенты ии | agi_and_rl': 'AGI_and_RL',
    'axis of ordinary': 'axisofordinary',
    'сиолошная': 'seeallochnaya',
    'love. death. transformers.': 'lovedeathtransformers',
    'just links': 'j_links',
    'abstractdl': 'abstractDL',
    'knowledge accumulator': 'knowledge_accumulator',
    'техножрица 👩‍💻👩‍🏫mechanic'.replace('mechanic', '👩‍🔧'): 'tech_priestess',
    'dlstories': 'dl_stories',
    'dealer.ai': 'dealerAI',
    'ai для всех': 'nn_for_science',
    'partially unsupervised': 'partially_unsupervised',
}

# Fix tech_priestess key carefully
CHANNEL_HANDLES = {
    'gonzo-обзоры ml статей': 'gonzo_ML',
    'data secrets': 'data_secrets',
    'борис опять': 'boris_again',
    'denis sexy it 🤖': 'denissexy',
    'эйай ньюз': 'ai_newz',
    'нейроэкзистенциализм': 'neuroexistencialism',
    'агенты ии | agi_and_rl': 'AGI_and_RL',
    'axis of ordinary': 'axisofordinary',
    'сиолошная': 'seeallochnaya',
    'love. death. transformers.': 'lovedeathtransformers',
    'just links': 'j_links',
    'abstractdl': 'abstractDL',
    'knowledge accumulator': 'knowledge_accumulator',
    'dlstories': 'dl_stories',
    'dealer.ai': 'dealerAI',
    'ai для всех': 'nn_for_science',
    'partially unsupervised': 'partially_unsupervised',
    'machine learning research': 'MLResearch',
}

KNOWN_HANDLES = {
    'boris_again', 'knowledge_accumulator', 'seeallochnaya', 'gonzo_ml',
    'axisofordinary', 'tech_priestess', 'nn_for_science', 'lovedeathtransformers',
    'doomgrad', 'rybolos_channel', 'neuroexistencialism', 'derplearning',
    'data_secrets', 'dl_stories', 'aihouse', 'ai_newz', 'nejdanov',
    'buckwheat_thoughts', 'denissexy', 'abstractdl', 'mishin_learning',
    'partially_unsupervised', 'victor_osyka', 'techsparks', 'danokhlopkov',
    'sonya_aesthetics', 'dealerai', 'j_links', 'dendi_math_ai',
    'tagir_analyzes', 'dtulinov', 'repushko_channel', 'chillhousetech',
    'agi_and_rl', 'ai_deeplearning', 'inneuralnetwork', 'mlresearch',
    'stackmorelayers', 'mlunderground', 'ntr_neural', 'fminxyz',
    'emptyset_of_ideas', 'gradientdip',
}

PAPER_PATTERNS = [
    # arxiv abs/pdf/html (incl. www.arxiv.org)
    (re.compile(r'(?:www\.)?arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})', re.I), 'arxiv'),
    (re.compile(r'arxiv\.org/ftp/arxiv/papers/\d{4}/(\d{4}\.\d{4,5})', re.I), 'arxiv'),
    (re.compile(r'huggingface\.co/papers/(\d{4}\.\d{4,5})', re.I), 'arxiv'),
    # openreview
    (re.compile(r'openreview\.net/(?:forum|pdf)\?id=([A-Za-z0-9_\-]+)', re.I), 'openreview'),
    # acl
    (re.compile(r'aclanthology\.org/([0-9]{4}\.[a-z0-9.\-]+)/?', re.I), 'acl'),
    # doi with or without resolver
    (re.compile(r'(?:doi\.org/)?(10\.\d{4,9}/[^\s\)\]\'",]+)', re.I), 'doi'),
    # nature etc by path
    (re.compile(r'nature\.com/articles/(s?[0-9a-z\-]+)', re.I), 'nature'),
    (re.compile(r'science\.org/doi/(10\.1126/[^\s\)\]\'",]+)', re.I), 'science'),
    # transformer-circuits
    (re.compile(r'transformer-circuits\.pub/([0-9]{4}/[^\s\)\]\'",#]+)', re.I), 'tc'),
    # anthropic/openai/meta research pages
    (re.compile(r'openai\.com/(?:research|index)/([^\s\)\]\'",/#]+)', re.I), 'openai'),
    (re.compile(r'anthropic\.com/(?:research|news)/([^\s\)\]\'",/#]+)', re.I), 'anthropic'),
    (re.compile(r'ai\.meta\.com/research/publications/([^\s\)\]\'",/#]+)', re.I), 'meta'),
    (re.compile(r'(?:www\.)?sakana\.ai/([^\s\)\]\'",/#]+)', re.I), 'sakana'),
    (re.compile(r'pub\.sakana\.ai/([^\s\)\]\'",/#]+)', re.I), 'sakana_pub'),
    (re.compile(r'abehrouz\.github\.io/files/([^\s\)\]\'",/#]+)', re.I), 'nested'),
    (re.compile(r'research\.google/blog/([^\s\)\]\'",/#]+)', re.I), 'google'),
    (re.compile(r'cell\.com/[^\s]*/fulltext/(S[0-9\-]+\([^)]+\)[0-9]+)', re.I), 'cell'),
    (re.compile(r'paperswithcode\.com/paper/([^\s\)\]\'",/#]+)', re.I), 'pwc'),
    (re.compile(r'direct\.mit\.edu/[^\s]*/([0-9]+)/([0-9]+)/([0-9]+)/', re.I), 'mit'),
    (re.compile(r'biorxiv\.org/content/(10\.1101/[0-9.]+)', re.I), 'doi'),
    (re.compile(r'selfrag\.github\.io', re.I), 'site:selfrag'),
    (re.compile(r'diamond-wm\.github\.io', re.I), 'site:diamond'),
    (re.compile(r'google-research\.github\.io/seanet/audiopalm', re.I), 'site:audiopalm'),
    (re.compile(r'ai\.facebook\.com/blog/voicebox', re.I), 'site:voicebox'),
    (re.compile(r'research\.nvidia\.com/labs/par/Perfusion', re.I), 'site:perfusion'),
    (re.compile(r'minedojo\.org', re.I), 'site:minedojo'),
    (re.compile(r'schema-harness\.github\.io', re.I), 'site:schema'),
    (re.compile(r'herasight-project\.webflow\.io', re.I), 'site:cogpgt'),
    (re.compile(r'situational-awareness\.ai', re.I), 'site:sa'),
    (re.compile(r'neuroevolutionbook\.com', re.I), 'site:nebook'),
    (re.compile(r'rlhfbook\.com', re.I), 'site:rlhfbook'),
]

TME_POST = re.compile(r'https?://t\.me/([A-Za-z0-9_]+)/(\d+)')
TG_BADGE = re.compile(
    r'\s*\[(?:⌲ )?tg\]\((?:https?://|tg://)[^)]+\)'
)
MD_URL = re.compile(r'https?://[^\s\)\]>]+')

# Google Translate wrapper for public Telegram posts -> English
TRANSLATE_QS = '_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=wapp'


def channel_translate_link(handle: str, post_id: str) -> str:
    return (
        f'https://t-me.translate.goog/s/{handle}/{post_id}?{TRANSLATE_QS}'
    )


def message_text(msg: dict) -> str:
    text = msg.get('text')
    if isinstance(text, str):
        return text
    parts = []
    for part in text or []:
        if isinstance(part, str):
            parts.append(part)
        else:
            parts.append(part.get('href') or part.get('text', ''))
    return ''.join(parts)


def paper_keys_from_text(text: str) -> set[str]:
    keys = set()
    for pattern, kind in PAPER_PATTERNS:
        for match in pattern.findall(text):
            if isinstance(match, tuple):
                value = '/'.join(match)
            else:
                value = match
            value = value.rstrip(').,;\'"')
            if kind == 'arxiv':
                yy = int(value[:2])
                mm = int(value[2:4])
                if mm < 1 or mm > 12 or yy < 7 or yy > 30:
                    continue
                keys.add(f'arxiv:{value}')
            elif kind == 'openreview':
                keys.add(f'or:{value}')
            elif kind == 'acl':
                keys.add(f'acl:{value.rstrip("/")}')
            elif kind == 'doi':
                keys.add(f'doi:{value.rstrip("/")}')
            elif kind == 'nature':
                keys.add(f'nature:{value}')
                # also common as doi 10.1038/<id>
                keys.add(f'doi:10.1038/{value}')
            elif kind == 'science':
                keys.add(f'doi:{value}')
            elif kind == 'tc':
                keys.add(f'tc:{value.rstrip("/")}')
            elif kind == 'openai':
                keys.add(f'openai:{value}')
            elif kind == 'anthropic':
                keys.add(f'anthropic:{value}')
            elif kind == 'meta':
                keys.add(f'meta:{value}')
            elif kind == 'sakana':
                keys.add(f'sakana:{value}')
            elif kind == 'sakana_pub':
                keys.add(f'sakana_pub:{value}')
            elif kind == 'nested':
                keys.add(f'nested:{value}')
            elif kind == 'google':
                keys.add(f'google:{value}')
            elif kind == 'cell':
                keys.add(f'cell:{value}')
            elif kind == 'pwc':
                keys.add(f'pwc:{value}')
            elif kind == 'mit':
                keys.add(f'mit:{value}')
            elif kind.startswith('site:'):
                keys.add(kind)
    return keys


def normalize_keys(keys: set[str]) -> set[str]:
    '''Add alias keys for brittle identifiers (biorxiv versions, etc.).'''
    out = set(keys)
    for key in list(keys):
        if key.startswith('doi:10.1101/'):
            base = re.sub(r'v\d+(?:\.full)?$', '', key)
            out.add(base)
        if key.startswith('doi:10.1038/'):
            # nature article ids sometimes listed bare
            out.add('nature:' + key.split('/', 2)[-1])
    return out


def lookup_link(keys: set[str], index: dict[str, str]) -> str | None:
    for key in normalize_keys(keys):
        if key in index:
            return index[key]
        # try truncated biorxiv
        if key.startswith('doi:10.1101/'):
            base = re.sub(r'v\d+(?:\.full)?$', '', key)
            if base in index:
                return index[base]
    return None


def keys_from_url(url: str) -> set[str]:
    return paper_keys_from_text(url)


def prefer_original_post(text: str, forwarded_from: str | None) -> str | None:
    hits = TME_POST.findall(text)
    if not hits:
        return None
    preferred_handle = None
    if forwarded_from:
        preferred_handle = CHANNEL_HANDLES.get(forwarded_from.lower())
    scored = []
    for handle, post_id in hits:
        score = 0
        if preferred_handle and handle.lower() == preferred_handle.lower():
            score += 10
        if handle.lower() in KNOWN_HANDLES:
            score += 5
        scored.append((score, handle, post_id))
    scored.sort(reverse=True)
    best_score, handle, post_id = scored[0]
    if best_score <= 0:
        return None
    return channel_translate_link(handle, post_id)


def saved_link(msg_id: int) -> str | None:
    # No shareable web URL for Saved Messages; skip badge when only this exists.
    return None


def build_index(messages: list[dict]) -> dict[str, str]:
    '''Map paper key -> best telegram link (public channel post only).'''
    best: dict[str, tuple[int, str, int]] = {}
    for msg in messages:
        text = message_text(msg)
        keys = normalize_keys(paper_keys_from_text(text))
        if not keys:
            continue
        original = prefer_original_post(text, msg.get('forwarded_from'))
        if not original:
            continue
        link = original
        rank = 2
        msg_num = msg['id']
        for key in keys:
            prev = best.get(key)
            if prev is None:
                best[key] = (rank, link, msg_num)
                continue
            prev_rank, prev_link, prev_num = prev
            if rank > prev_rank or (rank == prev_rank and msg_num > prev_num):
                best[key] = (rank, link, msg_num)
    return {k: v[1] for k, v in best.items()}


def badge(url: str) -> str:
    return f'[⌲ tg]({url})'


def annotate_line(line: str, index: dict[str, str]) -> str:
    if 'http' not in line and not re.search(r'10\.\d{4,9}/', line):
        return line
    clean = TG_BADGE.sub('', line)

    def replacer(match: re.Match) -> str:
        url = match.group(0).rstrip(').,;\'"')
        trailing = match.group(0)[len(url):]
        link = lookup_link(keys_from_url(url), index)
        if not link:
            return match.group(0)
        return f'{url} {badge(link)}{trailing}'

    # replace http(s) urls
    updated = MD_URL.sub(replacer, clean)

    # bare dois like 10.1038/...
    bare_doi = re.compile(r'(?<![/\w])(10\.\d{4,9}/[^\s\)\]\'",]+)')

    def doi_replacer(match: re.Match) -> str:
        doi = match.group(1).rstrip(').,;\'"')
        end = match.end()
        if updated[end:].startswith(' [tg]') or updated[end:].startswith(' [⌲ tg]'):
            return match.group(0)
        link = lookup_link({f'doi:{doi}'}, index)
        if not link:
            return match.group(0)
        return f'{doi} {badge(link)}'

    updated = bare_doi.sub(doi_replacer, updated)

    # bare arxiv ids in parentheses lists e.g. (2006.07982, 2011.13388, ...)
    bare_arxiv = re.compile(r'(?<![\d./v])(\d{4}\.\d{4,5})(?![\d.])')

    def arxiv_replacer(match: re.Match) -> str:
        arxiv_id = match.group(1)
        yy = int(arxiv_id[:2])
        mm = int(arxiv_id[2:4])
        if mm < 1 or mm > 12 or yy < 7 or yy > 30:
            return arxiv_id
        link = lookup_link({f'arxiv:{arxiv_id}'}, index)
        if not link:
            return arxiv_id
        return f'{arxiv_id} {badge(link)}'

    # only apply bare-arxiv replacement on the niche line that lists ids without urls
    if 'arxiv.org' not in updated and re.search(r'\(\d{4}\.\d{4,5}', updated):
        updated = bare_arxiv.sub(arxiv_replacer, updated)

    return updated.rstrip()


def annotate_table_row(line: str, index: dict[str, str]) -> str:
    if not line.startswith('|') or line.count('|') < 3:
        return line
    parts = [p.strip() for p in line.strip().strip('|').split('|')]
    if len(parts) < 3:
        return line
    if parts[0].lower() in ('year', '---', 'год'):
        return line
    cell = TG_BADGE.sub('', parts[2]).strip()
    url_match = MD_URL.search(cell)
    if not url_match:
        return line
    url = url_match.group(0).rstrip(').,;\'"')
    link = lookup_link(keys_from_url(url), index)
    if not link:
        parts[2] = cell
    else:
        parts[2] = f'{url} {badge(link)}'
    return '| ' + ' | '.join(parts) + ' |'


def main() -> None:
    data = json.loads(RESULT.read_text(encoding='utf-8'))
    index = build_index(data['messages'])
    print(f'indexed paper keys: {len(index)}')
    print(f'indexed public channel paper keys: {len(index)}')

    lines = PAPERS.read_text(encoding='utf-8').splitlines()
    out = []
    linked = missing = 0
    for line in lines:
        has_ref = (
            'http' in line
            or re.search(r'10\.\d{4,9}/', line)
            or re.search(r'\(\d{4}\.\d{4,5}', line)
        )
        if not has_ref or 'Telegram links:' in line:
            out.append(line)
            continue
        if line.startswith('|'):
            new = annotate_table_row(line, index)
        else:
            new = annotate_line(line, index)
        if '[⌲ tg](' in new and '[⌲ tg](' not in line:
            linked += 1
        elif has_ref and 'Year' not in line and '| ---' not in line:
            # still no badge on a reference-bearing line
            if '[⌲ tg](' not in new and '[tg](' not in new and MD_URL.search(new):
                # only count if we recognize a paper key at all
                keys = set()
                for url in MD_URL.findall(new):
                    keys |= keys_from_url(url)
                for doi in re.findall(r'10\.\d{4,9}/[^\s\)\]\'",]+', new):
                    cleaned = doi.rstrip(').,;\'"')
                    keys.add(f'doi:{cleaned}')
                if any(lookup_link({k}, index) for k in keys):
                    missing += 1
                elif keys:
                    missing += 1
        out.append(new)

    # footnote about link types
    note = (
        '\n---\n\n'
        'Telegram links: ``[⌲ tg](...)`` is included only when a public channel '
        'post (``t.me/<channel>/<id>``) was found in the saved message. It opens '
        'that post through Google Translate to English '
        '(``https://t-me.translate.goog/s/<channel>/<id>?_x_tr_sl=auto&_x_tr_tl=en...``). '
        'Papers without such a public post link have no Telegram badge.\n'
    )
    text = '\n'.join(out)
    if 'Telegram links:' not in text:
        text = text.rstrip() + note
    else:
        text = re.sub(
            r'\n---\n\nTelegram links:.*\n?',
            note,
            text,
            flags=re.S,
        )

    OUT.write_text(text, encoding='utf-8')
    print(f'updated lines with new tg badge: {linked}')
    print(f'paper-ish lines still without badge: {missing}')


if __name__ == '__main__':
    main()
