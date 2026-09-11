---
name: Verify tg link candidates
overview: "Проверка `tg_link_choices.md` показала три класса проблем (ложные FTS-совпадения, блоки только из дайджестов, пропущенные посты без arXiv-ссылки). План: усилить поиск по названию реальными заголовками, ввести оценку уверенности и пометку дайджестов, перегенерировать файл и вручную проверить выборку."
todos:
  - id: find-confidence
    content: "tg/find.py: is_digest, title_coverage filter for fts-and, search_many, detailed modes, tags in format_md"
    status: completed
  - id: titles
    content: "tg/find_missing.py: apply_known_metadata + fetch_arxiv_meta for missing titles, multi-query lookup (urls, real title, label sans parens, short name)"
    status: completed
  - id: sections
    content: "tg/find_missing.py: sections Dedicated / Only digests / Title matches / No posts; already-badge marks; collapse identical sibling blocks"
    status: completed
  - id: regen-verify
    content: Regenerate tg_link_choices.md, compare counts, manually spot-check ~15 posts, report doubtful ones
    status: completed
isProject: false
---

# Перепроверка кандидатов в tg_link_choices.md

## Что нашлось при проверке (read-only)

- 166 блоков с кандидатами: 147 по ключу (arXiv/DOI/URL), 19 по словам названия; 80 «No posts found». 401 ссылка, из них 91 — дайджесты Axis of Ordinary («Links for …»).
- **29 блоков состоят только из дайджестов** — для пользователя это фактически «поста нет», но они выглядят как найденные.
- **~9 из 19 FTS-блоков — ложные**: `fts-and` из двух общих слов («In-Context Algebra», «Cyclical Learning Rates», «Characterizing emergent phenomena», «Self-Programming AI», «ADAM … AdamCB», «Continual Learning and Catastrophic Forgetting», «Formal logical reasoning…», «The most cited neural nets…», «Language model harnesses…»). Пометка `_matched by title words_` не различает phrase и AND.
- **Пропуски**: `lookup()` в [tg/find_missing.py](tg/find_missing.py) останавливается на первом ключевом хите (даже если это дайджест) и никогда не ищет по названию. Посты без arXiv-ссылки теряются: Dr. GRPO → `lovedeathtransformers/9184`, `buckwheat_thoughts/165`, `AGI_and_RL/1004`; MiniMax-M1 → `data_secrets/7170`; Reasoning with Sampling → `axisofordinary/7804` — все в БД, все в «No posts found».
- Поиск по названию использует readme-label с приписками («(Schedule-Free)», «Dr. GRPO», «(Meta)») → `AND` всех слов проваливается. В `build_catalog()` title = label; реальные заголовки есть в `assets/arxiv_meta.json` (160 id) и подтягиваются только через `apply_known_metadata()`; для 129 из 235 узлов (в основном arXiv 2026) заголовка нет — их достаёт `fetch_arxiv_meta()` в [src/parse_readme.py](src/parse_readme.py).
- Косметика: Physics of LM даёт 4 блока с одинаковыми кандидатами, причём `dl_stories/848` уже стоит бейджем у части 1.
- БД свежая (max date 2026-09-10), поэтому 80 пропусков — не проблема экспорта.

## Изменения

### 1. `tg/find.py` — уверенность и дайджесты
- `is_digest(hit)`: `key_count >= 6` или текст начинается с `Links for` / `Some links` / `#дайджест` / содержит «подборка» в начале.
- Для FTS-хитов считать покрытие токенов названия (`title_coverage`: доля значимых слов названия, найденных в тексте); `fts-and` принимать только при покрытии ≥ 0.7, иначе отбрасывать.
- `search()` возвращает режим детальнее: `keys` / `title-phrase` / `title-words`; новая `search_many(conn, queries, limit)` — объединяет ключевые и title-хиты, дедуп по `(channel_id, id)`, сортировка: dedicated key → title-phrase → title-words → digest.
- `format_md`: тег `[digest]` у дайджестов, тег `[title match]` у FTS-хитов, отдельная строка уверенности блока.

### 2. `tg/find_missing.py` — реальные заголовки и объединённый поиск
- После `build_catalog()` вызывать `apply_known_metadata(nodes)` (offline, кэш `assets/arxiv_meta.json`); для id без заголовка — `fetch_arxiv_meta()` батчами и дописать в кэш (как делает `parse_readme.main()`).
- Запросы на узел: все `urls` (ключи) + реальный `title` (phrase) + label без скобок (phrase) + короткое имя из скобок/до двоеточия, если ≥ 4 символов (`Dr. GRPO`, `Schedule-Free`, `MR.Q`) как phrase.
- Всегда запускать и ключевой, и title-поиск, объединять через `search_many`.
- Пометка `[already badge for …]`, если `handle/id` уже используется в readme (собрать из `TG_BADGE_RE` по всему readme).
- Секции файла: «Dedicated posts» (есть хотя бы один не-дайджест), «Only digests found», «Title matches only — verify», «No posts found». Соседние узлы одной строки readme с идентичным набором кандидатов (Physics of LM) схлопывать в один блок с перечислением частей.

### 3. Перегенерация и ручная проверка
- `python tg/find_missing.py` → новый `tg_link_choices.md`; сверить цифры до/после (ожидание: «No posts found» сократится, ложные FTS исчезнут, 29 дайджестовых блоков уйдут в свою секцию).
- Прочитать текст ~15 постов выборочно (5 dedicated, 5 title-match, 5 digest) через sqlite и подтвердить релевантность; убрать/скорректировать эвристики, если найдутся промахи.
- Кратко отчитаться: сколько статей получили dedicated-кандидата, сколько — только дайджест, сколько без постов; список сомнительных для решения пользователя.

Бейджи в readme не проставляются — ждём выбор (`paper: handle/id` / `skip` / `both:`).