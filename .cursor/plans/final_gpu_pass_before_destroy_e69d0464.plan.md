---
name: Final GPU pass before destroy
overview: Use the remaining ~$4.1 on instance 50549154 for one chained GPU pass (retry unparsed keys with a new seed, second-seed noise-floor run, 7B Standard holes), pull the unsynced SciJudge pairs, freeze the environment, then rebuild report/badges and commit. No destroy.
todos:
  - id: cli-flags
    content: "score_reviewers.py: --seed, --max-tokens, --out-suffix; rsync remote/*.py to box"
    status: completed
  - id: final-pass
    content: Build _final_pass.sh (retry + noise-floor per model), nohup on box with progress log
    status: completed
  - id: side-tasks
    content: Pull scores_scijudge_pairs.jsonl; pip freeze -> requirements.lock; versions block in setup.sh
    status: completed
  - id: monitor-pull
    content: wait_step monitoring, credit checks; rsync back scores/reviews/logs incl. seed1
    status: completed
  - id: report
    content: build_report.py self-agreement section; reparse -> scrub -> report -> badges
    status: completed
  - id: commit
    content: Commit allowed files only; report credit; do NOT destroy
    status: completed
isProject: false
---

# Final GPU pass before destroy

Instance 50549154 is idle, credit **$4.14** (~3.3 h @ $1.25/h). Planned GPU time ~70 min (~$1.5). Do **not** destroy; leave the box running and report remaining credit at the end.

## 1. `score_reviewers.py`: three small CLI flags (committed)

In [filter/remote/score_reviewers.py](filter/remote/score_reviewers.py) `parse_args` / `run_vllm`:
- `--seed` (int, default 0) → `sample['seed']`. Retrying with seed 0 would reproduce the same failure (deterministic per-request seed), so every retry uses `--seed 1`.
- `--max-tokens` (int, default 0 = spec) → overrides `spec['max_tokens']` for CR-8B 7000→12000 and 7B Fast 16384→24576. `paper_budget` already derives from `max_tokens`, so budgets stay consistent (7B Fast: 49152 − 24576 leaves ~24k for the paper; `--max-paper-chars 48000` fits).
- `--out-suffix` (str, default '') → `scores_path(f'{name}.{suffix}')` and `reviews_dir(f'{name}.{suffix}')`, i.e. `scores_deepreviewer-14b.seed1.jsonl` + `reviews/deepreviewer-14b.seed1/`. Used only for the noise-floor run so the main files stay untouched.

Then rsync `filter/remote/*.py` to `/workspace/filter/remote/` (single-line rsync inside `bash -lc`, `--rsync-path=//usr/local/bin/rsync`).

## 2. Helper `_final_pass.sh` on the box (not committed)

Generalize the existing [filter/remote/_rescore_eight.sh](filter/remote/_rescore_eight.sh) pattern (drop rows for KEYS from jsonl + review md, then `--only-keys`) into one `nohup` chain grouped by model so each model loads once. `pkill -9 -f VLLM::EngineCore` before each model. Progress goes to `logs/final_pass.log`; each step prints `[step] name start/done`.

Per-model key lists come from the local jsonl (computed locally, pasted into the script as env vars):
- `cyclereviewer-8b`: retry 8 `unparsed:length` (`--seed 1 --max-tokens 12000`) + noise-floor 48 keys (`--seed 1 --out-suffix seed1`). ~8 min.
- `deepreviewer-14b`: retry 5 unparsed (`--seed 1 --max-paper-chars 48000`) + noise-floor 48 keys (`--seed 1 --out-suffix seed1 --max-paper-chars 48000`). ~12 min.
- `openreviewer-8b`: retry 3 (`--seed 1`). ~3 min.
- `deepreviewer-7b-fast`: retry 61 (`--seed 1 --max-tokens 24576 --max-paper-chars 48000`). ~20 min.
- `deepreviewer-7b` (Standard): 19 keys = `doi:10.1073/pnas.1611835114` (now has fulltext) + 18 unparsed (`--seed 1 --max-paper-chars 48000`). ~25 min.

Noise-floor subset: deterministic, stratified — take keys with a valid, non-partial 14B rating, sort by that rating, pick every 6th (~48 keys). Same 48 for CR-8B. No row dropping for this run (separate suffix files).

```mermaid
flowchart LR
  rsyncPy[rsync remote py] --> cr8b[CR-8B retry8 plus seed1x48]
  cr8b --> dr14b[14B retry5 plus seed1x48]
  dr14b --> or8b[OR-8B retry3]
  or8b --> dr7bf[7B Fast retry61]
  dr7bf --> dr7b[7B Std 19 holes]
  dr7b --> pull[rsync back scores reviews logs]
```

## 3. While the GPU runs (no GPU needed)

- rsync `/workspace/filter/scores_scijudge_pairs.jsonl` → `filter/` (gitignored by `filter/*.jsonl`; 2.7 MB, 4296 pairs).
- On the box: `pip freeze > /workspace/filter/remote/requirements.lock`; rsync back to `filter/remote/requirements.lock`.
- [filter/remote/setup.sh](filter/remote/setup.sh): add a comment block with the verified stack (vLLM 0.29.0, torch 2.13.0+cu130, driver 610.43.02, RTX PRO 6000 Blackwell sm_120, `VLLM_USE_FLASHINFER_SAMPLER=0`, `VLLM_ATTENTION_BACKEND=FLASH_ATTN`) and an opt-in branch: `if [[ -f "$ROOT/requirements.lock" && "${USE_LOCK:-0}" == 1 ]]; then pip install -r "$ROOT/requirements.lock"; else <current install>; fi`.

## 4. Monitor and pull back

Poll `logs/final_pass.log` with the existing `wait_step.sh` pattern (grep `[step] ... done`), checking credit via `vastai show user --raw` between models. When the chain finishes: rsync back `scores_*.jsonl` (including `*.seed1.jsonl`), `reviews/` (including `*.seed1/`), `logs/`.

## 5. Local rebuild

- [filter/reparse_reviews.py](filter/reparse_reviews.py) → [filter/scrub_garbage.py](filter/scrub_garbage.py) → [filter/build_report.py](filter/build_report.py) → [filter/add_score_badges.py](filter/add_score_badges.py), as before.
- [filter/build_report.py](filter/build_report.py): add an optional section `## Self-agreement (seed 0 vs seed 1)` — for each model with a `scores_<m>.seed1.jsonl` present, Spearman + symmetric macro-F1 over common keys (reuse `spearman`, `symmetric_macro_f1`, `paired_spearman`). Skip silently when the file is absent. Update the coverage / unparsed numbers in the report automatically.
- Expected result: 7B Fast coverage 258 → ~290, CR-8B 311 → ~316, 14B 314 → ~318, plus a self-agreement row that contextualises the 0.17–0.38 cross-model Spearman.

## 6. Commit

Allowed files only: `filter/*.py`, `filter/remote/score_reviewers.py`, `filter/remote/setup.sh`, `filter/remote/requirements.lock` (approved as item 4), `filter/scores.csv`, `filter/report.md`, `readme.md`. Not committed: `_final_pass.sh`, jsonl, reviews, logs, seed1 files. Use `git commit -F $env:TEMP\cmsg.txt`.

Finish by reporting coverage deltas, self-agreement numbers, and remaining credit. Destroy (`vastai destroy instance 50549154 -y`) only on an explicit go from you.