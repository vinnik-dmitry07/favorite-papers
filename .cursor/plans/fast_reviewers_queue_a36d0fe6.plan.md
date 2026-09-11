---
name: Fast reviewers queue
overview: Добить текущую очередь Fast-ревьюеров, починить парсер boxed_review, перевыкачать 8 мусорных OpenReview (PDF/API) и пересчитать только их, затем отчёт и destroy.
todos:
  - id: fast-model-key
    content: "score_reviewers.py: deepreviewer-7b-fast, mode в spec, max_tokens 16384 для Fast, batch 16, убрать bnb fallback"
    status: completed
  - id: queue-order
    content: "run_all.sh: очередь cr8b → 7b-fast → 14b → 7b Standard; убрать 70B"
    status: completed
  - id: report-columns
    content: "paths.py/build_report.py: dr7bf колонки, RATING10 на dr7bf, Spearman Fast vs Standard"
    status: completed
  - id: restart-queue
    content: Kill 7B Standard, rsync, nohup run_all.sh cyclereviewer-8b
    status: completed
  - id: monitor
    content: wait_step по шагам, unparsed, pull scores, кредит; стоп 7B Standard при кредите < $5
    status: completed
  - id: fix-boxed-parser
    content: "score_reviewers.py: brace-count boxed_review + fallback на весь текст; перепарсить reviews/* локально"
    status: completed
  - id: refetch-openreview
    content: "extract_fulltext: детектор challenge-страниц + PDF OpenReview; перевыкачать 8 ключей, иначе no_fulltext"
    status: completed
  - id: rescore-eight
    content: Если PDF ок — rsync md, выкинуть 8 ключей из jsonl/reviews, --only-keys на CR-8B / 7B-fast / 14B / SEA / OR-8B
    status: completed
  - id: scrub-garbage
    content: Обнулить SEA/OR оценки у непрокачанных challenge-страниц; 14 коротких пометить partial
    status: pending
  - id: collect-destroy
    content: rsync-back scores/reviews/logs; vastai destroy instance 50549154 -y
    status: completed
  - id: report-badges
    content: build_report.py + add_score_badges.py
    status: completed
  - id: commit
    content: Commit scripts, scores.csv, report.md, readme.md, .gitignore only
    status: completed
isProject: false
---

# Добить очередь + починить мусорный fulltext и парсер

Код очереди уже на инстансе. Не трогать GPU, пока идут 7B Fast / 14B Fast / остаток 7B Standard.

## Состояние на проверке (09:27 UTC)

- Очередь жива: `run_all.sh` → `deepreviewer-7b-fast`, 192/319, GPU 100 %, кредит **$10.75**.
- CR-8B готов: 319 строк, 302 good, mean 4.93. Все 8 `unparsed:stop` у CR-8B — это challenge-страницы OpenReview, не петли модели.
- 7B Fast: ~75 % парса; часть `unparsed` — баг `}` внутри `\boxed_review{...}`, часть — петли до 16384, часть — те же 8 заглушек.
- 8 файлов по 178 байт: Cloudflare «verifying your browser» (`openreview:BZ5a1r-kVsf`, `OpC-9aBBVJe`, `XyGJJ4FPoX`, `hcQfTsVnBo`, `klU4737opt`, `pOoKI3ouv1`, `ry_WPG-A-`, `wUU-7XTL5XO`). SEA-E и OpenReviewer-8B уже выставили им шумные 3–6.
- 14 файлов < 6000 символов (ACL-стабы, 5 arXiv ~1 KB, `arxiv:2303.07103` = 101 байт).
- `extract_fulltext.py` не качает PDF и не имеет OpenReview-фолбэка; HTML OpenReview попал в challenge.

## Пока крутится GPU

Продолжать [monitor](filter/remote/wait_step.sh): после 7B Fast и 14B — pull jsonl, доля unparsed, кредит. 7B Standard стартовать только если кредит ≥ $5, иначе остановить очередь.

Параллельно локально (без GPU): правки парсера и экстрактора ниже, чтобы к концу очереди они были готовы.

## 1. Парсер `\boxed_review` — [filter/remote/score_reviewers.py](filter/remote/score_reviewers.py)

Сейчас `BOXED_REVIEW_RE` обрывается на первой `}` (LaTeX `\{\pi_1\}` или преждевременный close).

- Заменить на извлечение с подсчётом скобок от последнего `boxed_review{`.
- Если в теле бокса нет rating/decision — парсить весь текст после снятия `<think>`.
- Добавить `filter/reparse_reviews.py`: для каждого `reviews/<model>/*.md` вызвать `parse_review`, перезаписать соответствующий `scores_*.jsonl` (сохранить `error` только если после фикса всё ещё пусто). Модели: `deepreviewer-7b`, `deepreviewer-7b-fast`, `deepreviewer-14b`. Cycle не использует boxed.

Это чинится без GPU после rsync-back `reviews/`.

## 2. Перевыкачка 8 OpenReview — [filter/extract_fulltext.py](filter/extract_fulltext.py)

- Детектор мусора: `verifying your browser` / `just a moment` / `enable javascript and cookies` / текст < 400 символов после strip → считать `missing`, не писать md как валидный.
- Для `kind==openreview` добавить PDF: `https://openreview.net/pdf?id={fid}` (и при необходимости URL из `api2.openreview.net/notes?id=`). Текст — `pypdf` (поставить локально и на инстансе, если нет). Если PDF недоступен — title+abstract из [filter/fetch_meta.py](filter/fetch_meta.py) / `meta.jsonl` как `incomplete` (лучше заглушки, но для полнотекстовых ревьюеров всё равно `no_fulltext`, если нет PDF).
- Прогнать только эти 8 ключей. Консоль-прогресс обязателен.

Если PDF дал нормальный текст (≥3000 токенов или хотя бы полный abstract+секции): rsync md + `fulltext_index.jsonl` на инстанс.

Если PDF не вышел: ключи остаются `source=missing` / `no_fulltext`.

## 3. Пересчёт только 8 ключей (если PDF ок)

На инстансе, **после** текущей очереди (или вместо 7B Standard, если кредит < $5):

- Удалить строки этих 8 ключей из `scores_{cr8b,dr7bf,dr14b,sea-e,openreviewer-8b}.jsonl` и их `reviews/<model>/`.
- По очереди `score_reviewers.py --only-keys <8>` для `cyclereviewer-8b`, `deepreviewer-7b-fast`, `deepreviewer-14b`, `sea-e`, `openreviewer-8b`. Оценка: 8×5 ≈ 15–25 мин.
- 7B Standard для этих 8 не обязателен (колонка информационная, неполная).

Если PDF не вышел — этот шаг пропускаем.

## 4. Зачистка мусора в скорах

- Для ключей, которые так и остались challenge/missing: во всех полнотекстовых jsonl заменить rating на `error: no_fulltext` (SEA-E и OR-8B тоже — их 3–6 по заглушке не должны входить в `mean_rating10`).
- 14 коротких (<6000 символов / `incomplete` в индексе): оставить оценку, выставить `partial=true` в jsonl; [filter/build_report.py](filter/build_report.py) показать `partial` в per-paper блоке. `arxiv:2303.07103` (101 байт) — как `no_fulltext`.
- `paper_text` в `score_reviewers.py` уже возвращает `''` при `source==missing` / `n_tokens==0`; после правки индекса повторный прогон сам напишет `no_fulltext`.

## 5. Финал

- rsync-back `scores_*.jsonl`, `reviews/`, `logs/` (jsonl/reviews/logs не коммитить).
- `vastai destroy instance 50549154 -y`.
- `python filter/build_report.py` (уже есть `dr7bf`, RATING10 на Fast, Spearman Fast vs Standard).
- `python filter/add_score_badges.py`.
- Коммит только `filter/*.py`, `filter/remote/{score_*.py,data_paths.py,vllm_boot.py,run_all.sh,setup.sh,prefetch.sh}`, `filter/scores.csv`, `filter/report.md`, `readme.md`, `.gitignore`. Не коммитить helper-скрипты и jsonl.

## Не трогать сейчас

Живой `deepreviewer-7b-fast` и `run_all.sh`. Не запускать второй инстанс.
