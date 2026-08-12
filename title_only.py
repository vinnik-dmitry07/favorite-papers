import json
import re
from pathlib import Path

from extract_papers import ARXIV_RE, message_text

ML_SOURCES = {
    'gonzo-обзоры ML статей', 'Data Secrets', 'Борис опять', 'Denis Sexy IT 🤖',
    'эйай ньюз', 'Нейроэкзистенциализм', 'Агенты ИИ | AGI_and_RL',
    'Axis of Ordinary', 'Сиолошная', 'Love. Death. Transformers.', 'Just links',
    'AbstractDL', 'Knowledge Accumulator', 'Техножрица 👩‍💻👩‍🏫👩‍🔧', 'DLStories',
    'Dealer.AI', 'AI для Всех', 'Machine Learning Research', 'Hacker News',
}

PAPER_HINT = re.compile(
    r'(?i)(стать[яию]|paper|препринт|preprint|работа|публикаци|arxiv|'
    r'neurips|icml|iclr|acl |emnlp|cvpr)'
)
LINK = re.compile(r'https?://\S+')


def main() -> None:
    messages = json.loads(Path('result.json').read_text(encoding='utf-8'))['messages']
    shown = 0
    for msg in messages:
        text = ' '.join(message_text(msg).split())
        if len(text) < 120:
            continue
        source = msg.get('forwarded_from')
        if source not in ML_SOURCES:
            continue
        if ARXIV_RE.search(text):
            continue
        if not PAPER_HINT.search(text):
            continue
        shown += 1
        print(f'### [{source} | {msg.get("date")}]\n{text[:700]}\n')
    print(f'total candidates: {shown}')


if __name__ == '__main__':
    main()
