---
name: Fulltext regex search
overview: Расширить `#search` на карте так, чтобы запрос находил статьи по извлечённому телу (`filter/fulltext/*.md`) через glob (`abducti*`) и явный `/re/flags`, не раздувая стартовый `graph_data.js` и не ломая литеральный поиск (`grpo`, `f(g(x))`) на GitHub Pages.
todos:
  - id: corpus-builder
    content: "src/build_fulltext_search.py: id→lowercase body+appendix (без References), node.fulltext, gitignored assets/fulltext_search.js; вызов из build_graph.py"
    status: completed
  - id: query-syntax
    content: Литерал без * ? и без /…/ (как сейчас indexOf); * / ? → glob; /re/flags → JS RegExp; invalid → литерал, без throw
    status: completed
  - id: map-search
    content: "map.js: haystack OR FULLTEXT_SEARCH[id]; URL корпуса от script[src=graph_data.js]; lazy script; debounce 150ms; footer loading"
    status: completed
  - id: pages-deploy
    content: "pages.yml: python3 src/build_fulltext_search.py, test -s, cp в site/assets/; map.js не ходит в filter/"
    status: completed
  - id: verify
    content: "verify_map.py assert: grpo; abducti* → openreview:klU4737opt bright; ( без pageerror; hyperdreambooth → url:hyperdreambooth.github.io; placeholder в index.html"
    status: completed
isProject: false
---

# Fulltext regex search

## Goal

Поле `#search` на карте (`src/index.html`, `src/map.js`) должно подсвечивать узлы, у которых запрос есть в извлечённом тексте статьи, а не только в title/author/section/tag. Пример пользователя: `abducti*` → abduction / abductive. Явный regex — через `/pattern/flags`. Метаданные ищутся как сейчас. Карта остаётся статическим GitHub Pages.

## Assumptions

- Живая карта: [favorite-papers](https://vinnik-dmitry07.github.io/favorite-papers/). CI (`.github/workflows/pages.yml`) публикует только `index.html`, `map.js`, `graph_data.js`, D3. `filter/fulltext/*.md` закоммичены (~326 файлов, ~28 MB) и есть в checkout, но **на Pages их нет**. Локальный `fetch('../filter/fulltext/…')` обманет: на проде 404.
- `filter/*.jsonl` и `*.json.gz` в `.gitignore`. Корпус не класть в gzip-JSON.
- Совпадение: **haystack OR body**. Нет ключа в корпусе → только метаданные (R5). Нет корпуса на проде → degrade в сегодняшний поиск, без ложных «все не найдены».
- `node.doc` в `build_graph.py` — «refs HTML скачан», не «есть extract». Новый флаг `node.fulltext`. ~57 узлов без md (в основном `url:` / `web`).
- `src/` не импортирует `filter/`. `safe_key` уже совпадает с `cache_path` в `src/common.py` (`[^A-Za-z0-9._-]+`, 120 символов). Билдер копирует `REF_HEAD` / `APP_HEAD` / `split_sections` из `filter/extract_fulltext.py` (не тащить весь extract и не рефакторить GPU `data_paths.py`).
- Не вшивать сырой markdown в `graph_data.js` (~418 KB → десятки MB на каждый заход).

## Chosen approach

Отдельный CI-собираемый `assets/fulltext_search.js` (`window.FULLTEXT_SEARCH = {id: text}`), gitignored, lazy-load с карты. References выкидываются, appendix остаётся.

Отклонено:

- Сырой `new RegExp(box)` на каждый ввод: `abducti*` случайно срабатывает (`i*`), но `.` матчит все узлы, а `f(g(x))` (keyword `arxiv:2509.25123`) — не литерал.
- `fulltext_search.json.gz` + parallel `texts[i]`: `.gitignore` режет `*.json.gz`; массив без id ломается при смене порядка узлов.
- Обрезка на первом `References|Appendix`: у `arxiv:2608.19197` единственный `abducti*` в Appendix H **после** `## References`.
- Вшивать тела в `GRAPH_DATA` или ходить в `filter/` с Pages.

## Changes

### `src/build_fulltext_search.py` (новый)

- Читает ids из `assets/graph.json` (или каталога).
- `filter/fulltext/<safe_key>.md` → `split_sections` → lowercase, схлопнуть whitespace, **body + appendix**, без references (иначе ловят citation-only хиты).
- Пишет `assets/fulltext_search.js`: `window.FULLTEXT_SEARCH = {…}`. Ключи = node id, пустых значений нет (нет md → нет ключа).
- Stdlib, pathlib, `'`, PEP8, прогресс по ~326 файлам. Печать `with_text` / `missing`.
- Self-check на сборке: блобы `openreview:klU4737opt` и `arxiv:2608.19197` содержат `abduct`.
- `build_graph.py` после `apply_topics` вызывает сборку и ставит `node['fulltext']`.

### `src/map.js`

- Компилятор запроса (исходная строка, **не** `toLowerCase()` всей pattern):
  1. нет `*` / `?` и нет обёртки `/…/` → литерал, сегодняшний `indexOf` по уже-lowercased haystack и корпусу (`grpo`, `f(g(x))`);
  2. есть `*` или `?` → glob (`*` → `.*`, `?` → `.`, остальное экранировать), `RegExp` с `i`;
  3. `/pattern/flags` → `new RegExp` в `try/catch`; ошибка → литерал, без `pageerror`; сбросить `lastIndex` если есть флаг `g`.
- `applyFilters`: `haystack || FULLTEXT_SEARCH[d.id]`. Корпус не загружен / нет ключа → только haystack.
- Первый непустой term: inject `<script src=corpusUrl()>`. `corpusUrl` из `script[src$="graph_data.js"]` (локально `../assets/`, на Pages `assets/` после sed в `index.html`). Generation token против позднего onload. onerror → metadata-only.
- Debounce `#search` ~150 ms. Footer: `loading full text…` пока грузится.
- Не хардкодить `../assets/` и не ходить в `filter/`.

### `src/index.html`

- Placeholder: `title, author, tag, body; abducti* or /re/`. Ширину `#search` чуть увеличить (210px режет паттерн). Без лишнего `<script>` на корпус.

### `.gitignore`

- `assets/fulltext_search.js` (генерируется локально и в CI).

### `.github/workflows/pages.yml`

- После checkout: `python3 src/build_fulltext_search.py`, `test -s assets/fulltext_search.js`, `cp` в `site/assets/` рядом с `graph_data.js`. Job падает, если файла нет. `ubuntu-latest` уже имеет python3 — отдельный setup-python не обязателен.

### `src/verify_map.py`

Сервер уже отдаёт корень репо. Если JS нет — прогнать билдер. Assert, не только print:

- `grpo` димит часть узлов (регрессия метаданных);
- после появления `window.FULLTEXT_SEARCH`: `abducti*` оставляет **ярким** `openreview:klU4737opt` (title «Position: LLMs can't jump», в haystack нет `abduct*`) и **не** все узлы;
- `(` не даёт `pageerror`;
- `hyperdreambooth` оставляет ярким `url:hyperdreambooth.github.io` (нет md).

### `AGENTS.md`

Строка в шаге 4 / таблице: `build_graph.py` также пишет gitignored `assets/fulltext_search.js`; Pages пересобирает его.

### Не делать в этом проходе

- Web Worker (если `verify_map` / ручной замер покажет фриз на parse или `/re/` — отдельный шаг).
- Inverted index (мешает произвольному `/re/`).
- Инлайн тел в `GRAPH_DATA`.
- Менять Escape/Reset и `topics.py` haystack.
- Рефакторить `filter/extract_fulltext.py` / `filter/remote/data_paths.py`.
- Коммитить `filter/*.jsonl`.

## Acceptance

| ID | Как закрыто |
|---|---|
| R1 | `#search` OR с `FULLTEXT_SEARCH[id]` из md |
| R2 | glob `abducti*` + `/re/flags` |
| R3 | без `*?` и без `/…/` → `indexOf` |
| R4 | CI пишет JS в `site/assets/`; runtime не трогает `filter/` |
| R5 | нет ключа → только haystack |

## Verification

```text
python src/build_graph.py
python src/verify_map.py
```

Опционально: `python src/build_fulltext_search.py` и проверить два abduct self-check. После merge в main: на Pages тот же `abducti*`.

## Triggers to revisit

- `verify_map` таймаутится на загрузке/`abducti*`, или вкладка фризится на `/re/` → worker или отмена скана, синтаксис не менять.
- `openreview:klU4737opt` остаётся dim при живом `FULLTEXT_SEARCH` → сломан mapping id / `safe_key` / обрезка секций.
- `f(g(x))` димит `arxiv:2509.25123` → компилятор снова отдаёт сырой regex.
- Задеплоенный `fulltext_search.js` 404 → сломан generate/`test -s`/`cp`.
- Новые heading-варианты библиографии, которые `REF_HEAD` не режет → ложные citation-хиты; расширить regex, не откатывать appendix.

## Council note

Три независимых кандидата (разные модели), отдельный аудит, один раунд ремонта. Ремонт сменил синтаксис (литерал / glob / `/re/`), оставил appendix, заменил gzip-массив на id-keyed JS и зафиксировал body-only assert. Реализацию не начинать в этом ходе.
