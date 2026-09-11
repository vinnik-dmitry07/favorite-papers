---
name: Weaknesses sentence clip
overview: "Убрать посимвольные обрывы в блоке Weaknesses report.md: парсер отдаёт полный первый абзац, отчёт режет только на границе предложения, по одной строке на модель (CR-8B, затем DR-14B Fast с fallback)."
todos:
  - id: parse-cap
    content: "parse_review: WEAK_MAX_CHARS=2000 вместо [:400] в обеих ветках"
    status: completed
  - id: clip
    content: "build_report: clip_sentence с обрывом по границе предложения и очисткой '** -'"
    status: completed
  - id: weak-for
    content: "weaknesses_for: WEAK_MODELS порядок, до двух (label, text), без [:500]"
    status: completed
  - id: render
    content: "write_report: вложенные sub-bullets по модели, fallback '—'"
    status: completed
  - id: tests
    content: Тесты clip_sentence в test_aggregate.py
    status: completed
  - id: rebuild
    content: Пересобрать report.md и проверить QWM и отсутствие обрывов
    status: completed
isProject: false
---

# Weaknesses без обрывов на полуслове

## Почему режется сейчас

- [filter/remote/parse_review.py](filter/remote/parse_review.py) строки 138 и 163: `weaknesses = ...[:400]` — посимвольно, в обеих ветках (`_cycle_fields`, `_fields_from`).
- [filter/build_report.py](filter/build_report.py) `weaknesses_for`: склеивает две модели в одну строку и снова `[:500]`. CR-8B забирает ~400, DR-7B получает ~60 символов.
- `WEAK_RE` для SEA-E оставляет в тексте хвост заголовка `** - …`.
- Реальные длины первого абзаца (QWM): CR-8B 497, OR-8B 334, SEA-E 877, DR-14B 4483, DR-7B 3232.

## Изменения

### 1. `filter/remote/parse_review.py` — не резать по символу

- Константа `WEAK_MAX_CHARS = 2000`; в обеих ветках `[:400]` → `[:WEAK_MAX_CHARS]`. Первый абзац сохраняется целиком (лимит только защита jsonl от 4k-хвостов DeepReviewer).
- Файл общий с GPU-скорером (`score_reviewers.py` пишет `parsed` в jsonl) — существующие jsonl не меняются, новые прогоны получат более длинное поле. Безвредно.

### 2. `filter/build_report.py` — обрыв только на границе предложения

- `WEAK_MODELS = ('cyclereviewer-8b', 'deepreviewer-14b', 'deepreviewer-7b-fast', 'openreviewer-8b', 'sea-e')` — порядок предпочтения; DR-7B Std (partial run) не используется.
- Новая `clip_sentence(text, limit=400) -> str`:
  - нормализовать пробелы, снять ведущие `*`, `:`, `-`, пробелы (SEA-E `** - `);
  - если `len <= limit` — вернуть как есть;
  - иначе найти последний `. `, `? `, `! ` до `limit`; если он дальше ~120 символов — резать там; иначе по последнему пробелу; добавить `…`.
- `weaknesses_for(key, fallback) -> list[tuple[str, str]]`: идти по `WEAK_MODELS`, `parse_review` по `MODELS[...]['parse_kind']`, фильтр `usable_weak_text`, затем `clip_sentence`; вернуть до **двух** пар `(MODELS[...]['label'], text)`. Убрать `' '.join(chunks)[:500]`. Fallback `_weak` тоже через `clip_sentence`.
- Рендер в `write_report`: вместо одной строки

  ```markdown
  - Weaknesses:
    - CR-8B: The main weakness … future work.
    - DR-14B Fast: Despite the strengths … action selection.…
  ```

  Если ни одной модели — `- Weaknesses: —`. Каждый текст через `md_cell`.

### 3. Тесты в [filter/test_aggregate.py](filter/test_aggregate.py)

- `clip_sentence`: длинный текст обрывается на `.`/`?`/`!` и заканчивается `…`; текст короче лимита не меняется; `** - The paper…` теряет префикс; никогда не заканчивается на середине слова.
- Существующий `WeaknessesSnippetTest` остаётся.

### 4. Проверка

- `python filter/test_aggregate.py -v`.
- `python filter/build_report.py`; в `report.md` посмотреть QWM (`arxiv:2608.17163`), грепнуть, что нет строк Weaknesses, оканчивающихся на букву без `.`/`…`.
- Оценить рост `report.md` (≤ 326 × 2 × 400 символов сверх текущего).

Коммит и пуш — только по команде.