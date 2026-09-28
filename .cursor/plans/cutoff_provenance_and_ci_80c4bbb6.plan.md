---
name: Cutoff provenance and CI
overview: Make every temporal-OOD row carry its own machine-readable cutoff proof (dates + sources), replace the unsourced DeepScaleR / OLMo-2 / Qwen3-2507 constants with sourced ones, and add a GitHub Actions check that runs the tests and verifies `llm_gains.jsonl` / `llm_gains.md` regenerate byte-identically.
todos:
  - id: cutoff-records
    content: Cutoff(day, source, basis) records for MODEL/DATASET/BENCH/HMMT; DeepScaleR 2025-01-26, OLMo-2 2024-11-26, Qwen3-2507 2025-08-06, AIME25 02-06, AIME26 02-05, HMMT 02-15; empty source -> unverified
    status: completed
  - id: cutoff-proof
    content: ood.cutoff_proof() + rewrite chain_cutoff/temporal_proof/classify_ood_basis on it
    status: completed
  - id: row-fields
    content: ROW_FIELDS + normalize drop + attach_ood fills model/train/teacher_cutoff, benchmark_date, cutoff_source; Notes DeepScaleR sentence
    status: completed
  - id: readme-order
    content: paths.readme_paper_keys() from readme.md via src/common.classify; use in build_llm_gains/models main; verify order == papers.jsonl
    status: completed
  - id: lf-newlines
    content: newline='\n' in write_jsonl and markdown writers
    status: completed
  - id: ci-workflow
    content: ".github/workflows/llm_gains.yml: pytest + --from-jsonl regen + git diff --exit-code"
    status: completed
  - id: tests-rebuild
    content: Tests for sources/dates/proof fields/readme order/LF; rebuild twice, expect 139/6/137/109
    status: completed
isProject: false
---

# Cutoff provenance and CI for `llm_gains`

Numeric OOD cells stay as they are (139 temporal rows / 137 base / 109 ref). Every date constant becomes a sourced record; a constant without a source cannot admit a row. DeepSeekMath rows are not added; no `Cutoffs` section in the markdown.

## 1. Sourced cutoff records in [filter/llm_gains_ood.py](filter/llm_gains_ood.py)

Replace bare `date` values with a frozen record `Cutoff(day, source, basis)` (`basis` in `release` / `content` / `contest`). A `Cutoff` with an empty `source` is treated as unknown by `model_cutoff` / `dataset_cutoff` / `bench_date`, so `classify_ood_basis` falls through to `unverified`.

- `MODEL_CUTOFFS` (basis `release`, an upper bound on training content):
  - `Qwen3-4B-Instruct-2507` -> **2025-08-06** (was 08-05; HF `Qwen/Qwen3-4B-Instruct-2507`, Qwen3 collection "Updated Aug 6, 2025")
  - `OLMo-2` -> **2024-11-26** (was 11-01; `allenai.org/blog/olmo2`)
  - keep the rest, each with its release page URL (Qwen2.5 blog 2024-09-19, Llama 3.2 blog 2024-09-25, Llama 3.1 blog 2024-07-23, Llama 3 blog 2024-04-18, DeepSeek-R1 HF 2025-01-20, Qwen3 blog 2025-04-29, OLMo 3 blog 2025-11-20, Phi-3.5 HF 2024-08-20). Verify each URL while implementing; any that cannot be confirmed gets `source=''`.
- `DATASET_CUTOFFS` (basis `content`):
  - `deepscaler` -> **2025-01-26**, not 2024-10-01. Card (`huggingface.co/datasets/agentica-org/DeepScaleR-Preview-Dataset`, commits 2025-02-09/10, no later data commits) lists AIME 1984–2023, AMC < 2023, Omni-MATH (arXiv 2410.07985 v1 2024-10-10), STILL (`RUC-AIBOX/STILL-3-Preview-RL-Data`: MATH + NuminaMathCoT + AIME 1983–2023, all commits 2025-01-26). Max component publication date = 2025-01-26 < AIME 2025 I. Note in code: the dataset *release* (2025-02-09) is after AIME 2025 I (2025-02-06), so only the component bound admits AIME 2025.
  - `dapo-math*` 2025-03-17 (HF initial commit `851fd44`), `smoltalk2` (verify HF commit date), `MATH` 2021-03-05 (arXiv 2103.03874 v1).
- `BENCH_DATES` (basis `contest`, first sitting): `AIME 2025` **2025-02-06**, `AIME26`/`AIME 2026` **2026-02-05** (MAA news + AoPS wiki); `PAPER_HMMT_MONTH` -> `PAPER_HMMT_DATE` `2025-02-15` (hmmt-archive). LCB rows keep `bench_span` as the date with `source='row:bench_span'`.

Add `cutoff_proof(model, teacher, train_data, bench, key, code, method, bench_span, hmmt)` returning
`{model_cutoff, train_cutoff, teacher_cutoff, benchmark_date, cutoff_source}` (ISO strings, `''` when unknown; `cutoff_source` is a dict `{model, train, teacher, bench}` of URLs). `chain_cutoff` / `temporal_proof` / `classify_ood_basis` are rewritten on top of it so the row's stored proof and the classification cannot diverge.

## 2. Persist the proof in [filter/build_llm_gains.py](filter/build_llm_gains.py)

- `ROW_FIELDS` += `model_cutoff`, `train_cutoff`, `teacher_cutoff`, `benchmark_date`, `cutoff_source`.
- `normalize_gain_row` drops these (derived); `attach_ood` recomputes them from `ood.cutoff_proof` for every row (filled where known, empty otherwise — the empty field shows why a row is `unverified`).
- Notes bullet for Shao: replace "Qwen2.5 / Llama / OLMo cutoffs put AIME 2025 after the chain" with the DeepScaleR content-bound sentence (STILL-3 2025-01-26 vs AIME 2025 I 2025-02-06).

## 3. Reproducible outputs for CI

- `filter/papers.jsonl` and `fulltext_index.jsonl` are gitignored. Add `readme_paper_keys()` to [filter/paths.py](filter/paths.py): parse `readme.md` bullets in order, first URL -> `src/common.classify` (stdlib only). `build_llm_gains.main` and `build_llm_models.main` use it for paper rank; `papers.jsonl` stays only for `known` keys in `--extract-dir` mode. Verify locally once that the readme order equals the current `papers.jsonl` order (byte-identical rebuild).
- `iter_candidates(model_rows, {})` already yields the same `not_applicable` without the fulltext index.
- Force LF: `write_jsonl` and the markdown writers open with `newline='\n'` so Linux and Windows produce identical bytes (index is already LF; `core.autocrlf=true` keeps the Windows checkout clean).

## 4. GitHub Actions: `.github/workflows/llm_gains.yml`

On `push` / `pull_request` to `main`: checkout, `setup-python` 3.10 (matches local), `pip install pytest numpy scipy`, `python -m pytest filter/`, then `python filter/build_llm_gains.py --from-jsonl` and `python filter/build_llm_models.py --from-jsonl`, then `git diff --exit-code -- filter/llm_gains.jsonl llm_gains.md filter/llm_models.jsonl llm_models.md`. If the models regeneration is not a no-op locally, drop it from the diff step and say so.

## 5. Tests in [filter/test_build_llm_gains.py](filter/test_build_llm_gains.py)

- A `Cutoff` with `source=''` -> `unverified`, even with a valid date.
- `dataset_cutoff('DeepScaleR')` == 2025-01-26 and Qwen2.5-Math-7B × AIME 2025 stays temporal; the dataset release date (2025-02-09) would not.
- `Qwen3-4B-Instruct-2507` == 2025-08-06; `OLMo-2-1124-7B` == 2024-11-26; `AIME 2025` == 2025-02-06; HMMT 2025-02-15.
- For every temporal row after `renormalize_rows`: all five proof fields non-empty (teacher may be empty only when no teacher), `benchmark_date > max(cutoffs)`, every `cutoff_source` value non-empty.
- `readme_paper_keys()` order equals `papers.jsonl` order (skip when the file is absent).
- `write_jsonl` emits `\n` only.
- Byte-idempotence test unchanged; rebuild twice with `--from-jsonl` and expect 139 / 6 / 137 / 109.

## Not done on purpose

- DeepSeekMath `2402.03300` rows (user: skip).
- No `Cutoffs` section in `llm_gains.md` (user: jsonl only).
- Do not commit unless asked.