---
name: SKPO + audit leakage-free Llama/OLMo cells
overview: The markdown extracts (`filter/fulltext/*.md`) dropped the table bodies for several papers, so `filter/llm_gains.jsonl` lacks the Llama/OLMo × {MATH-500, AMC 2023, AIME 2024, Minerva Math} cells that `is_leakage_free_row` would admit. Inject those cells (SKPO Table 1 plus eight audited papers) through a new override in `filter/llm_gains_ood.py` modelled on `_conspo_extra_rows`, numbers copied from the cached arXiv HTML tables, then regenerate `filter/llm_gains.jsonl` / `llm_gains.md`. The temporal gate (`classify_ood_basis`) is untouched; the new rows enter the leakage-free block only.
todos:
  - id: ood-constants-helper
    content: Add paper-key constants, `_table_cells()` spec builder and `HISTORICAL_EXTRA` tuple to `filter/llm_gains_ood.py`
    status: pending
  - id: ood-skpo-cells
    content: Fill `HISTORICAL_EXTRA` with SKPO Table 1 Llama-3.2-3B-Instruct cells (AIME 2024 avg@32, AMC 2023 avg@3; MATH-500 avg@3 per open question)
    status: pending
  - id: ood-audit-cells
    content: Fill `HISTORICAL_EXTRA` with SCRL, TTRL, Critique-GRPO, DFT, Dr. GRPO, UPFT, Intuitor cells (numbers in this plan)
    status: pending
  - id: ood-conspo-table5
    content: Extend `_conspo_cells()` with a per-bench `metrics` kwarg and append ConSPO Table 5 Llama-3.2-3B-Instruct AIME 2024 / AMC 2023 / MATH-500 cells to `CONSPO_EXTRA`
    status: pending
  - id: ood-register
    content: Add `_historical_extra_rows(have_scored)` and register it in `apply_gain_overrides` after `_conspo_extra_rows`
    status: pending
  - id: md-note
    content: Add one provenance bullet to the `## Leakage-free (both papers)` notes in `render_md`
    status: pending
  - id: tests
    content: Add unit tests (scope guard, idempotency, SKPO cell values, render check) to `filter/test_build_llm_gains.py`
    status: pending
  - id: regenerate
    content: Run `python filter/build_llm_gains.py --from-jsonl` twice, confirm byte-identical, read the new md rows back
    status: pending
---

## Goal

Every checkpoint in `ood.LEAKAGE_FREE_MODELS` that a readme paper trains and evaluates on a bench in `ood.LEAKAGE_FREE_BENCHES` gets a jsonl row that renders in the two `Leakage-free:` tables of `llm_gains.md`. Today the markdown extracts lost those table bodies, so SKPO (`arxiv:2604.08690`) has only LiveCodeBench + MMLU-Pro rows and eight other papers have partial Llama/OLMo coverage. Fix by injecting the cells from the cached arXiv HTML (`cache/arxiv_<id>.html.gz`, the same source ConSPO's `CONSPO_EXTRA` used), not by hand-editing `filter/llm_gains.jsonl`. Do not touch `classify_ood_basis`, `LEAKAGE_FREE_*`, `HISTORICAL_BENCHES`, or any temporal cutoff table.

## Assumptions

Verified in code (the implementer may rely on these):

- Admission path (`filter/build_llm_gains.py`): `render_md` → `table_gain_rows(rows, admit=is_leakage_free_row)`; `is_leakage_free_row` = `row['leakage_free']` and `ood_basis in {'id', 'rl_stage'}`. `attach_ood` sets `leakage_free = ood.leakage_free(model, bench)` (exact-string membership in `LEAKAGE_FREE_MODELS` × `LEAKAGE_FREE_BENCHES`) and `ood_basis = classify_row(...)` → `ood.classify_ood_basis`, whose first branch returns `'id'` / `'rl_stage'` for every bench in `HISTORICAL_BENCHES` (all four target benches are in it) regardless of dates. So any row with a leak-free model name and one of the four benches is admitted; no inventory slot or cutoff needed. `table_gain_rows` also requires `bench in CORE_BENCHES` (all four are), `not is_base_code(code)` (`BASE_CODES` = base/untrained/untuned/checkpoint/pretrained/starting), `not is_omitted_method` (`OMITTED_GAIN_CODES` includes `R1-GRPO`, so Critique-GRPO's R1-GRPO reference rows never render — expected; add them anyway as the `ref` carrier for sibling consistency).
- Override path: `renormalize_rows` = `normalize_gain_row` → `ood.apply_gain_overrides` → `normalize_gain_row` again → `attach_train_data` → `attach_teacher` → `coerce_pp_rows` → `attach_ood` → `fill_baselines` → `dedupe_rows` → `ROW_FIELDS` projection → `sort_rows`. `apply_gain_overrides` builds `have_scored` = `{(key, model, code, bench, train_data or '', source or '')}` over the incoming rows with a score, then `out.extend(...)` for each injector. Injected dicts must have the `_weight_geo_dapo_rows` shape (`key, code, method, model, bench, metric, base, ref, ref_method, score, gain=None, gain_ref=None, source, train_data, teacher='', unit='pp', bench_span='', ckpt_select='unspecified', ood_basis='', ood=False`).
- Both `build_llm_gains.py` entry points (`--from-jsonl` and `--extract-dir`) go through `renormalize_rows`, so the override is applied on every rebuild; on the second run the rows already exist in the jsonl and are skipped via `have_scored`. `dedupe_rows` key = `(key, code, model, bench, metric, train_data, source)`.
- `coerce_pp_rows` multiplies by 100 when every present `base/ref/score` is ≤ 1.0 and ≥ 0 — write Intuitor's fractions already converted to pp (43.6 not 0.436). None of the other new cells is all-≤1.0 (DFT MATH-500 bases 1.63 / 1.86 are > 1.0, unlike DFT AIME 2024 which needed `UNSCALE_MODELS`).
- `fill_baselines` only fills `base` / `ref` when they are `None`; every new cell carries its own `base`, `score` and (when a vanilla RLVR reference exists in the same table) `ref`, so nothing gets recomputed.
- `resolve_gain_bench`: `'AMC'` → `'AMC 2023'`, `'AIME24'` → `'AIME 2024'`, `'Minerva'` → `'Minerva Math'`, `'MATH500'` → `'MATH-500'`, but `'MATH'` → `'MATH'` (no canonicalisation). Write canonical bench names in the specs.
- `blm.norm_model`: `'LLaMA-3.2-3B-Instruct'` and `'Llama3.2-3B-Instruct'` → `'Llama-3.2-3B-Instruct'`; `'Llama-3.1-8B-Base'`, `'Llama-3.2-3B'`, `'OLMo-2-1124-7B-SFT'` pass through. Existing DFT rows use `'Llama-3.1-8B-Base'` for the paper's `LLaMA-3.1-8B`; reuse it.
- Sibling-row conventions to mirror (read from `filter/llm_gains.jsonl`): SKPO codes `GRPO, GSPO, SPO, SAPO, PRIME, DAPO, CISPO, SKPO`, `method == code`, `ref_method='GRPO'`, `source='Table 1 / §4.1'`, `train_data='dapo-math-17k'`; ConSPO Llama rows `source='Table 5 / §5.2'`, `train_data='DeepScaleR-Preview-Dataset'`, `ckpt_select='best-every-100'`; SCRL `ref_method='GRPO'`, `train_data='hard_1024'`; TTRL `code='TTRL'`, `method='TTRL (GRPO)'`, `metric='pass@1'`, `ref=None`, `ref_method=''`, `train_data=''` (inventory lists four train sets, so `attach_train_data` leaves it empty); Critique-GRPO `source='Table 5 / §5.5'`, `train_data='4k subset of a reorganized 46k subset of OpenR1-Math-220k'`, `ref_method='GRPO'`, R1-GRPO row carries `ref == score == base-of-ref`; DFT `metric='avg@16'`, `source='Table 1'`, `train_data='NuminaMath-CoT (100,000 random instances)'`, `ref=None`; Dr. GRPO `code='Dr.GRPO'`, `method='Dr. GRPO'`, `ref_method='Dr. GRPO'`, `ref == score`, `source='Table 4'`, `train_data='MATH training dataset'`; UPFT `metric='acc'`, `source='Table 2 (PRM)'` / `'Table 3 (PRM-12K)'`, `train_data=''`, `ref=None`; Intuitor `metric='pass@1'`, `source='Table 5'` / `'Table 6'`, `train_data='MATH training split (7,500 problems)'`, `ref_method='GRPO'`.
- Papers audited and found to have **no** table numbers for a leak-free checkpoint (skip, do not scrape plots): 80/20 `2506.01939` (Llama-3.1-8B only in Figure 11), SRT `2505.21444` (Llama-3.1-8B-Instruct MATH-500 only in Figure 33), Shao `2506.10947` (Figure 3, documented skip), HICRA Llama-3.1-8B-Base inventory row (no table). E2H `2506.06632` and 1-shot RLVR `2504.20571` Llama rows already render.
- SKPO Table 1 has **no Minerva Math column for Llama-3.2-3B-Instruct** (Llama block columns: AIME24, AIME25, AMC, MATH, Olympiad, MMLU, LiveCode; Minerva appears only in the Qwen2.5-Math-7B block). The task premise "Minerva" for SKPO Llama cannot be satisfied. SKPO's Critique-GRPO row is `N/A` for Llama — skip.
- SKPO metric per column (paper §4.1 / Table 1 caption): AIME24 `avg@32`; AMC, MATH, Olympiad, MMLU-Pro, LiveCodeBench `avg@3`. Existing SKPO rows already use `avg@3`.
- SKPO HTML column header is `MATH`, not `MATH-500`; the inventory row (`llm_models.jsonl`) recorded `"MATH"` verbatim. Treating it as MATH-500 is an inference (see Open questions).
- SCRL Table 1 numbers are pass@1 from the F.2 unbiased estimator over n = 64 rollouts; label them `pass@1` (Table 7 header `P@1`), not `accuracy` as the Appendix-D OOD rows do. SCRL F.2 says checkpoints are chosen by "best average validation score" without naming the set; leave `ckpt_select='unspecified'` (no `†`) rather than assert eval-bench selection.
- Qwen cells (SKPO Qwen2.5-Math-7B, SCRL Qwen3, ConSPO Qwen/DeepSeek, …) are out of scope: `leakage_free()` is False for them by construction and the task says not to add them.

## Changes

### filter/llm_gains_ood.py

- Constants (next to `CONSPO`, `DFT`, …): `SKPO = 'arxiv:2604.08690'`, `SCRL = 'arxiv:2605.22074'`, `TTRL = 'arxiv:2504.16084'`, `UPFT = 'arxiv:2503.02875'`, `DR_GRPO = 'arxiv:2503.20783'`, `CRITIQUE_GRPO = 'arxiv:2506.03106'`, `INTUITOR = 'arxiv:2505.19590'` (`DFT` already exists).
- `_conspo_cells(model, source, train, benches, base, scores, ref, metrics=None)`: add the optional kwarg; when given, set `'metric': metrics.get(bench)` on each spec (else omit the key). In `_conspo_extra_rows` use `'metric': spec.get('metric') or 'avg@32'` instead of the literal.
- Append to `CONSPO_EXTRA` (new `_T5 = 'Table 5 / §5.2'`; HTML `cache/arxiv_2605.12969.html.gz` v4, Table 5 "Generalization on Llama-3.2-3B-Instruct", columns AIME24 | MATH | AMC | O-Bench; metric per ConSPO §5.1 / App. C.1: avg@32 on AIME and AMC, pass@1 elsewhere — matches the existing MATH-500 `pass@1` rows):
  `_conspo_cells('Llama-3.2-3B-Instruct', _T5, _DS, ('AIME 2024', 'MATH-500', 'AMC 2023'), base={'AIME 2024': 3.3, 'MATH-500': 26.4, 'AMC 2023': 12.5}, scores={'GRPO': (12.0, 52.8, 25.9), 'DAPO': (10.5, 52.8, 25.0), 'Dr.GRPO': (11.1, 54.0, 26.5), 'DisCO': (11.4, 56.6, 27.5), 'ConSPO': (12.3, 57.4, 26.7)}, ref={'AIME 2024': 12.0, 'MATH-500': 52.8, 'AMC 2023': 25.9}, metrics={'MATH-500': 'pass@1'})`.
  The existing GRPO/DAPO/ConSPO MATH-500 rows are skipped by `have_scored` (same key/model/code/bench/train/source); Dr.GRPO and DisCO MATH-500 plus all ten AIME 2024 / AMC 2023 cells are new (12 rows). `DROP_ROWS` only drops ConSPO Llama AIME 2025 / AIME26 — unaffected.
- New spec builder, after `CONSPO_EXTRA`:

  ```python
  def _table_cells(key, model, source, train, metric, benches, base,
                   scores, ref=None, ref_method='GRPO', methods=None):
      '''One spec per (code × bench). metric: str or {bench: str}.
      ref: {bench: value} or None (no RLVR reference in that table).
      methods: {code: method} for codes whose method text differs.'''
  ```

  Returns a tuple of dicts `{key, model, code, method, bench, metric, base, score, ref, ref_method, source, train_data}` with `ref=None, ref_method=''` when `ref` is None, and `method = (methods or {}).get(code, code)`.
- `HISTORICAL_EXTRA = (...)` built from `_table_cells` calls, one per paper/table. Numbers (all from the cached HTML, version noted):
  - **SKPO** `cache/arxiv_2604.08690.html.gz` v1, Table 1 (`S4.T1`), Llama-3.2-3B-Instruct, `source='Table 1 / §4.1'`, `train='dapo-math-17k'`.
    - `AIME 2024`, metric `avg@32`: base 3.4; GRPO 4.7; GSPO 6.9; SPO 5.8; SAPO 7.9; PRIME 5.4; DAPO 13.8; CISPO 10.8; SKPO 14.7. ref 4.7.
    - `AMC 2023`, metric `avg@3`: base 20.1; GRPO 24.8; GSPO 30.4; SPO 26.1; SAPO 38.1; PRIME 29.7; DAPO 36.5; CISPO 25.3; SKPO 37.9. ref 24.8.
    - `MATH-500`, metric `avg@3` (only if Open question 1 resolves "include"): base 36.3; GRPO 39.6; GSPO 42.1; SPO 39.2; SAPO 42.0; PRIME 34.7; DAPO 41.1; CISPO 35.8; SKPO 44.8. ref 39.6.
    - 16 rows (24 with MATH-500). Write one `_table_cells` call per bench because the metric differs.
  - **SCRL** `cache/arxiv_2605.22074.html.gz` v1, Table 1 (`S5.T1`, columns Olym.B | Minerva | MATH | AIME'24 | AIME'25 | AMC | IMO-B) Llama3.2-3B-Instruct block, `model='Llama-3.2-3B-Instruct'`, `source='Table 1 / §5.2'`, `train='hard_1024'`, metric `pass@1`, benches `('Minerva Math', 'MATH-500', 'AIME 2024', 'AMC 2023')`:
    base (Initial) (13.7, 44.0, 6.4, 20.6); SFT (11.0, 44.1, 2.5, 18.1); GRPO (14.9, 44.5, 10.3, 20.9); DAPO (15.1, 45.9, 9.8, 22.2); QuestA (14.8, 45.9, 8.5, 21.4); NuRL (14.9, 45.2, 10.2, 21.7); SCRL (15.2, 45.2, 10.3, 21.4); ref = GRPO. 24 rows. (Table also has Olym.B, AIME'25, IMO-B — not leak-free benches, skip.)
  - **TTRL** `cache/arxiv_2504.16084.html.gz` v3, Table 2 (`S3.T2`) "Performance of TTRL on various models", LLaMA-3.2-3B-Instruct, `model='Llama-3.2-3B-Instruct'`, `code='TTRL'`, `methods={'TTRL': 'TTRL (GRPO)'}`, `source='Table 2'`, `train=''`, metric `pass@1`, `ref=None`: benches `('AIME 2024', 'AMC 2023', 'MATH-500')` base (6.0, 19.4, 43.9); TTRL (13.3, 31.3, 61.6). 3 rows. TTRL paper has no AIME 2025, so `AIME` = AIME 2024.
  - **Critique-GRPO** `cache/arxiv_2506.03106.html.gz` v7, Table 5 (`S5.T5`), Llama-3.2-3B-Instruct, `source='Table 5 / §5.5'`, `train='4k subset of a reorganized 46k subset of OpenR1-Math-220k'`, metric `pass@1`, bench `MATH-500` only (AIME24/AMC23/Minerva already in jsonl): base 46.6; R1-GRPO 53.6; Critique-GRPO 58.8; ref 53.6 (`ref_method='GRPO'`). 2 rows.
  - **DFT** `cache/arxiv_2508.05629.html.gz` v3, Table 1 (`S4.T1`), metric `avg@16`, `source='Table 1'`, `train='NuminaMath-CoT (100,000 random instances)'`, bench `MATH-500`, `ref=None`: `Llama-3.2-3B` base 1.63; SFT 8.65; DFT 12.79. `Llama-3.1-8B-Base` base 1.86; SFT 16.85; DFT 27.44. 4 rows.
  - **Dr. GRPO** `cache/arxiv_2503.20783.html.gz` v2, Table 4 (`A2.T4`), `Llama-3.2-3B`, bench `MATH-500`, metric `pass@1`, `source='Table 4'`, `train='MATH training dataset'`, `code='Dr.GRPO'`, `methods={'Dr.GRPO': 'Dr. GRPO'}`: base 6.4; score 10.0; ref 10.0 with `ref_method='Dr. GRPO'` (self-reference, mirrors the existing AIME/AMC/Minerva rows; omitted from the GRPO table by `is_self_ref`). 1 row. FineMath / NuminaQA variants are not in `LEAKAGE_FREE_MODELS` — skip.
  - **UPFT** `cache/arxiv_2503.02875.html.gz` v1, `Llama-3.1-8B-Instruct`, bench `MATH-500`, metric `acc`, `train=''`, `ref=None`: Table 2 (`S4.T2`) `source='Table 2 (PRM)'` base 51.0; SFT 48.4; UPFT 52.0. Table 3 (`S4.T3`) `source='Table 3 (PRM-12K)'` base 51.0; RFT 52.0; V-STaR 52.6. 4 rows (mirror the existing AIME 2024 code set per table; skip "Lable Filter").
  - **Intuitor** `cache/arxiv_2505.19590.html.gz` v5, bench `MATH-500` (paper column `MATH`; inventory `eval_id` = MATH-500), metric `pass@1`, `train='MATH training split (7,500 problems)'`, values ×100 written directly: Table 5 (`A2.T5`) `model='Llama-3.2-3B-Instruct'`, `source='Table 5'`: base 43.6; GRPO 49.4; Intuitor 47.6; ref 49.4. Table 6 (`A2.T6`) `model='OLMo-2-1124-7B-SFT'`, `source='Table 6'`: base 30.2; GRPO 37.4; Intuitor 37.2; ref 37.4. 4 rows (skip GRPO-PV; existing rows do not carry it).
  - Total: 58 rows in `HISTORICAL_EXTRA` (+8 if SKPO MATH-500) + 12 via `CONSPO_EXTRA` = 70 (78).
- `_historical_extra_rows(have_scored: set[tuple]) -> list[dict]`: `seen = {(k, m, c, b, s) for (k, m, c, b, _t, s) in have_scored}` (drop `train_data` from the identity so an inventory-filled `train_data` on a later run cannot re-inject); for each spec not in `seen` append a `_weight_geo_dapo_rows`-shaped dict with `metric=spec['metric']`, `ckpt_select='unspecified'`, `gain=None`, `gain_ref=None`. Register in `apply_gain_overrides`: `out.extend(_historical_extra_rows(have_scored))` right after `_conspo_extra_rows`.
- Comment block above `HISTORICAL_EXTRA`: "Leak-free Llama / OLMo cells whose table bodies are missing from `fulltext/*.md`. Copied from the cached arXiv HTML tables (id + table anchor per call). Plot-only papers (80/20 Fig. 11, SRT Fig. 33, Shao Fig. 3) are deliberately absent."

### filter/build_llm_gains.py

- `render_md`, `## Leakage-free (both papers)` bullet list: add one bullet after "Drawn below…": "Cells whose table bodies were lost in `filter/fulltext/*.md` are backfilled from the cached arXiv HTML tables (SKPO Table 1, ConSPO Table 5, SCRL Table 1, TTRL Table 2, Critique-GRPO Table 5, DFT Table 1, Dr. GRPO Table 4, UPFT Tables 2–3, Intuitor Tables 5–6); see `HISTORICAL_EXTRA` / `CONSPO_EXTRA` in `filter/llm_gains_ood.py`." No logic change; `table_gain_rows` / `is_leakage_free_row` / `classify_row` untouched.

### filter/test_build_llm_gains.py

- `class HistoricalExtraTest(unittest.TestCase)`:
  - `test_specs_stay_inside_leakage_free_block`: every spec in `ood.HISTORICAL_EXTRA` has `ood.leakage_free(model, bench)` True, non-empty `metric`, `source`, `score is not None`, `base is not None`; no spec has a Qwen model. Also assert the ConSPO Llama Table-5 specs in `ood.CONSPO_EXTRA` have `metric == 'pass@1'` for MATH-500 and default (missing) for AIME 2024 / AMC 2023.
  - `test_injects_once_and_is_idempotent`: `rows = ood.apply_gain_overrides([])`; `hist = [r for r in rows if r['key'] in {ood.SKPO, ood.SCRL, ood.TTRL, ood.CRITIQUE_GRPO, ood.DFT, ood.DR_GRPO, ood.UPFT, ood.INTUITOR}]`; `len(hist) == len(ood.HISTORICAL_EXTRA)`; `again = ood.apply_gain_overrides(rows)`; `len(again) == len(rows)`. Then `once = blg.renormalize_rows(rows, [])`, `twice = blg.renormalize_rows(once, [])`, `len(twice) == len(once)`.
  - `test_skpo_llama_cells`: from `blg.renormalize_rows(ood.apply_gain_overrides([]), [])` pick key `ood.SKPO`, model `'Llama-3.2-3B-Instruct'`, code `'SKPO'`, bench `'AIME 2024'`: `metric == 'avg@32'`, `base == 3.4`, `ref == 4.7`, `score == 14.7`, `ref_method == 'GRPO'`, `leakage_free is True`, `ood_basis in {'id', 'rl_stage'}`, `blg.is_leakage_free_row(row)`; AMC 2023 row: `metric == 'avg@3'`, `base == 20.1`, `score == 37.9`. Assert no SKPO row has `model` starting with `'Qwen'` and `leakage_free` True.
  - `test_leakage_free_tables_render_new_cells`: `md = blg.render_md(blg.renormalize_rows(read_jsonl(blg.JSONL_PATH), [], []), [], [])`; take the slice after `'## Leakage-free: gain over the starting checkpoint'` and assert it contains `'[SKPO](https://arxiv.org/abs/2604.08690) | 2604.08690 | avg@32 |'` and `'+11.3'` on that line, `'[SCRL](https://arxiv.org/abs/2605.22074)'`, `'[TTRL](https://arxiv.org/abs/2504.16084) | 2504.16084 | pass@1 | +17.7'` (MATH500 first column of the Llama-3.2-3B-Instruct table — verify column order after the rebuild and adjust), and `'OLMo-2-1124-7B-SFT · MATH500'` in an "Other checkpoints" header. Keep the assertions to method link + metric + one delta so column reordering does not make the test brittle.
- Existing `test_temporal_rows_carry_proof` (`temporal >= 50`) and `test_notes_range_does_not_change_counts` are unaffected: new rows are `id` / `rl_stage`, never `temporal`.

### filter/llm_gains.jsonl, llm_gains.md (regenerated, not edited)

- Expected diffs after `--from-jsonl`: jsonl grows by 70 (78) rows; `refuse_output_shrink` is not triggered. `llm_gains.md`:
  - Leakage-free base table, Llama-3.2-3B-Instruct: SKPO rows `avg@32 AIME24 +11.3`, `avg@3 AMC23 +17.8` (`MATH500 +8.5` if included); DAPO `+10.4` / `+16.4`; SAPO `+4.5` / `+18.0`; ConSPO `avg@32 AIME24 +9.0† AMC23 +14.2†`, Dr.GRPO(2605.12969) `MATH500 +27.6†`, DisCO `+30.2†`; SCRL `pass@1 MATH500 +1.2 AIME24 +3.9 AMC23 +0.8 Minerva +1.5`; TTRL `+17.7 / +7.3 / +11.9`; Critique-GRPO gains `MATH500 +12.2`; Intuitor `MATH500 +4.0`, GRPO(2505.19590) `+5.8`.
  - Llama-3.2-3B: DFT `MATH500 +11.2`, SFT `+7.0`, Dr.GRPO(2503.20783) `+3.6`. Llama-3.1-8B-Instruct: UPFT `MATH500 +1.0`, SFT `-2.6`, RFT `+1.0`, V-STaR `+1.6`. Other checkpoints: Llama-3.1-8B-Base DFT `+25.6`, SFT `+15.0`; OLMo-2-1124-7B-SFT Intuitor `+7.0`, GRPO `+7.2`.
  - Leakage-free GRPO table: SKPO `AIME24 +10.0 AMC23 +13.1` (`MATH500 +5.2`); SCRL `+0.7 / +0.0 / +0.5 / +0.3`; Critique-GRPO `MATH500 +5.2`; Intuitor `-1.8` (Llama), `-0.2` (OLMo); ConSPO `AIME24 +0.3 AMC23 +0.8`, Dr.GRPO(2605.12969) `MATH500 +1.2`, DisCO `+3.8`. TTRL / UPFT / DFT / Dr.GRPO(2503.20783) stay out of this table (no reference or self-reference).
  - Summary counts (`n_leak_base`, `n_leak_ref`) rise; temporal counts unchanged.

## Verification

```powershell
$env:PYTHONIOENCODING='utf-8'
python -m pytest filter/test_build_llm_gains.py -q
python filter/build_llm_gains.py --from-jsonl
Copy-Item filter/llm_gains.jsonl $env:TEMP/llm_gains.1.jsonl; Copy-Item llm_gains.md $env:TEMP/llm_gains.1.md
python filter/build_llm_gains.py --from-jsonl
fc.exe /b filter\llm_gains.jsonl $env:TEMP\llm_gains.1.jsonl
fc.exe /b llm_gains.md $env:TEMP\llm_gains.1.md
python -m pytest filter/ -q          # same as .github/workflows/llm_gains.yml
git diff --stat -- filter/llm_gains.jsonl llm_gains.md
```

Manual checks (Read tool, not grep in the same batch as the rebuild):

- Read the `### Llama-3.2-3B-Instruct` tables in both `## Leakage-free:` sections of `llm_gains.md`; confirm the SKPO, SCRL, TTRL, ConSPO avg@32 lines and the Critique-GRPO / Intuitor MATH500 cells match the expected deltas above; confirm no Qwen row appears there.
- Grep `filter/llm_gains.jsonl` for `"key": "arxiv:2604.08690"` and confirm 16 (24) new Llama rows with `"leakage_free": true`, `"ood_basis": "id"`, and none for Qwen2.5-Math-7B with `leakage_free: true`.
- Build output: `ood attach: ... temporal=<unchanged>`; `score rows lacking base` / `lacking ref` lists must not gain SKPO/SCRL/ConSPO-Llama entries (TTRL/UPFT/DFT `ref` holes are pre-existing by design).
- `python -m flake8 filter/llm_gains_ood.py filter/build_llm_gains.py filter/test_build_llm_gains.py` (PEP8, single quotes, line length as in the file).
- Do not commit. Delete any `%TEMP%` scratch copies afterwards.

## Open questions

1. SKPO Table 1 column `MATH` is not labelled MATH-500 anywhere in the paper (inventory `eval_id` keeps `"MATH"`, `resolve_gain_bench('MATH')` stays `'MATH'`). Include the 8 Llama cells as `MATH-500` (task premise; every other 2025–26 RLVR paper in the repo that says "MATH" reports the 500-problem subset), or leave MATH out (16 SKPO rows instead of 24)? Default if unanswered: include, and say so in the `HISTORICAL_EXTRA` comment.
