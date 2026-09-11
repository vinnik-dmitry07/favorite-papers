---
name: Official prompts rerun reviewers
overview: SEA-E дал 100% брак (нужен system+user по шаблону чекпоинта), а DeepReviewer/CycleReviewer запущены с неофициальными промптами и в 10 раз меньшим лимитом генерации. Перевести все четыре ревьюера на официальные промпты/лимиты из ai_researcher и SEA/template.json, перезапустить очередь с шага sea-e, дальше — сбор, destroy, отчёт, бейджи, коммит.
todos:
  - id: official-prompts
    content: "score_reviewers.py: official system+user prompts for sea/deep/cycle, official limits and sampling, token-id prompts, per-kind parsers"
    status: completed
  - id: run-all-mode
    content: "run_all.sh: --deep-mode Fast Mode for deepreviewer-14b"
    status: completed
  - id: restart-queue
    content: Kill run_all + DR-7B, move bad SEA outputs aside, rsync, nohup run_all.sh sea-e
    status: completed
  - id: monitor
    content: Check first-chunk unparsed rate per step, credit, periodic score pull
    status: in_progress
  - id: collect-destroy
    content: rsync-back scores/reviews/logs; vastai destroy instance 50549154 -y
    status: pending
  - id: report-badges
    content: build_report.py + add_score_badges.py
    status: pending
  - id: commit
    content: Commit scripts, scores.csv, report.md, readme.md, .gitignore only
    status: pending
isProject: false
---

# Официальные промпты и перезапуск очереди ревьюеров

## Факты (read-only проверка, 06:48 UTC)

- OpenReviewer-8B: **готов и валиден** — 316/319, рейтинги 1–8 (медиана 6), 2 `unparsed:length`, 1 `no_fulltext`, S/P/C у всех. Оставить как есть.
- SciJudge: 319 строк, `n_valid` 5–45, BT в норме. Скачано локально.
- **SEA-E: 100% брак.** 121/193 `unparsed`, остальные — ложные «6/Accept». Сырые ответы — продолжение статьи (`## References`, `## Appendix A`): модель не видела `[/INST]`. Причина: шаблон чекпоинта `ECNU-SEA/SEA-E` **требует** `system` (инструкция) + `user` (статья); моё слияние в один `user` ломает Jinja → fallback без `[INST]`. Официальная инструкция — `instruction_e` из `SEA/inference/template.json`, статья без `## References`, `max_new_tokens=8192`.
- **DeepReviewer** (стартует сейчас со старым кодом): официально `system` = «You are an expert academic reviewer… Your thinking mode is Standard Mode… simulating 4 different reviewers…» + `user` = статья; `max_model_len=70000`, `max_tokens=45000`, `temp=0.4`, `top_p=0.95`. Выход: `<think>…</think>`, затем `\boxed_simreviewers{…}` и `\boxed_review{ ## Rating: N … }`, решение `## Decision:\nAccept`. 7B — DeepSeek-R1-Distill-Qwen-7B, 14B — Phi-4. Наши `max_tokens=4096` / `max_len=16384` дадут `unparsed:length` почти на всём.
- **CycleReviewer**: официально `system` = промпт «…You need to fill out **4** review opinions», `user` = статья; `max_model_len=50000`, `max_tokens=7000`, `temp=0.4`. Выход: 4 ревью через `**********`, секции `## Rating\n\nN`, затем `## Meta Review`, `## Paper Decision\n\nAccept`. Официальный парсер усредняет рейтинги ревьюеров.
- Prefetch Westlake идёт: 7B, 14B, CR-8B скачаны; 70B — 20/140 GB (готов к ~07:20). HF-кэш выровнен симлинками `hub/`.
- Кредит ~$14.5. Оценка новой очереди: SEA 15 мин, DR-7B ~1 ч, DR-14B (Fast Mode) ~40 мин, CR-8B ~30 мин, CR-70B ~3.5–4 ч → ~6.5 ч ≈ $8.

## Правки [`filter/remote/score_reviewers.py`](filter/remote/score_reviewers.py)

1. **Промпты по официальным источникам** (`messages_for`):
   - `sea`: `[system=INSTRUCTION_E, user=paper]` (текст из `template.json`, без примеров-чисел).
   - `deep`: `[system=DEEP_SYSTEM(mode), user=paper]`, `DEEP_SYSTEM` дословно из `ai_researcher/deep_reviewer.py._generate_system_prompt` + `simreviewer_prompt`; `--deep-mode` (`Standard Mode` для 7B, `Fast Mode` для 14B — иначе 14B не влезает в бюджет).
   - `cycle`: `[system=CYCLE_SYSTEM, user=paper]` дословно из `cycle_reviewer.py`.
   - `openreviewer`: без изменений.
2. **Лимиты в `MODELS`**: deep `max_len=49152`, `max_tokens=32768`; cycle `max_len=40960`, `max_tokens=7000`; sea `max_len=32768`, `max_tokens=8192`. `paper_budget` уже считает бюджет статьи от этих чисел.
3. **Sampling**: `temp=0.4, top_p=0.95` для deep/cycle; sea `temp=0.3`. Через `spec`.
4. **Без двойного BOS**: рендерить `apply_chat_template(tokenize=True)` и отдавать vLLM `{'prompt_token_ids': ids}` вместо строки (шаблоны SEA/Llama сами вставляют BOS).
5. **Парсер по виду**:
   - `deep`: срезать `<think>…</think>`; если есть `\boxed_review{…}` — парсить только его; `## Rating:` на той же или следующей строке.
   - `cycle`: рейтинг = среднее всех `## Rating` до `## Meta Review`; решение из `## Paper Decision`.
   - `sea`: текущие regex подходят (`**Rating:**\n6 …`, `- Decision: Accept`).
   - Если `render_prompt` упал в fallback — печатать предупреждение один раз, а не молча.

## [`filter/remote/run_all.sh`](filter/remote/run_all.sh)

- `deepreviewer-14b … --deep-mode "Fast Mode"`; остальное без изменений (`start_step` уже есть).

## Перезапуск на инстансе

1. `pkill -f run_all.sh; pkill -f score_reviewers.py` (DR-7B только стартовал, потерь нет).
2. `mv scores_sea-e.jsonl scores_sea-e.bad.jsonl; mv reviews/sea-e reviews/sea-e.bad`; удалить `scores_deepreviewer-7b.jsonl`, если успел появиться.
3. rsync `remote/`; `nohup bash run_all.sh sea-e > logs/run_all2.log &`.
4. Через ~10 мин после старта каждого нового шага — проверить `unparsed` в первом чанке; при >20% — стоп, правка regex, `run_all.sh <step>`.

## Далее (без изменений)

- Мониторинг + периодический rsync-back `scores_*.jsonl`; кредит.
- По завершении: rsync `scores_*.jsonl`, `reviews/`, `logs/`; `vastai destroy instance 50549154 -y`.
- `build_report.py` → `scores.csv`/`report.md`; `add_score_badges.py`; коммит только скриптов (без `wait_*.sh`, `status.sh`, `link_cache.sh`), `scores.csv`, `report.md`, `readme.md`, `.gitignore`.