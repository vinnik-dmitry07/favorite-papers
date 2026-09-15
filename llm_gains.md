# Compact OOD gains

Per-paper numbers from `filter/fulltext/*.md`, stored in `filter/llm_gains.jsonl`. One jsonl row is one (paper × method × model × bench × train data × source table). Markdown keeps only **temporal OOD**: the bench date is after the full training-chain cutoff, plus one leakage-free historical block (Llama / OLMo, see below). Other historical benches and version-only LCB slices stay in the jsonl as `rl_stage` / `id` / `unverified` and are not drawn. API and GPT-family models are omitted. Model inventory: [`llm_models.md`](llm_models.md).

## Summary

- Papers with at least one temporal OOD number: **6**
- Temporal gain cells vs starting checkpoint: **94**
- Temporal gain cells vs GRPO / nearest RLVR: **66**
- Leakage-free historical cells vs starting checkpoint: **60**
- Leakage-free historical cells vs GRPO / nearest RLVR: **28**
- From-scratch papers (no starting checkpoint): **13**

## Notes

- [Spurious Rewards](https://arxiv.org/html/2506.10947v2#A4) (`2506.10947`): AIME 2025 avg@8 from Appendix D Figures 12–13. Last point of the thick 10-step-smoothed SVG curve (usually step 300; Llama-3.2-3B random ends at 287), not the curve max — that overstates (Qwen2.5-Math-7B Incorrect last +2.8 vs peak +6.0). Non-ground-truth last-point gains on Qwen2.5-Math-7B are **−0.4…+4.5 pp**. A trailing `‡` marks |Δ| < 2 pp (AIME has 30 problems). Train data DeepScaleR: the STILL-3 component is dated 2025-01-26, which is before AIME 2025 I (2025-02-06). The dataset card itself appeared on 2025-02-09.
- [Paradox](https://arxiv.org/html/2601.11061v1#S4.SS1) (`2601.11061`, already in `readme.md`): MATH-500 and MinervaMath are contaminated; LiveMathBench is the leakage-free control. It does not replace these AIME 2025 cells. Qwen2.5 rows still share `2506.10947` with the MATH-500 / AIME 2024 jsonl rows (those stay `id` / `rl_stage`).

## Leakage-free (both papers)

Intersection of [Spurious Rewards](https://arxiv.org/abs/2506.10947) and [Paradox](https://arxiv.org/abs/2601.11061): the model already has the answers (Qwen2.5-Math / Qwen3) vs it does not (Llama / OLMo).

- Models with no memorization shortcut: **Llama-3.1-8B** and **OLMo-2-1124-7B**. Paradox: partial prompts do not complete to the answer; spurious RLVR raises perplexity without unlocking stored solutions. Shao: spurious rewards stay flat; gains need ground-truth. Shao only (same family pattern): Llama-3.1-8B-Instruct, Llama-3.2-3B, Llama-3.2-3B-Instruct, OLMo-2-1124-7B-SFT.
- Bench both treat as fresh: **AIME 2025**. Shao: written after the cutoff of every model they train. Paradox: the memorization gate fires on 0/30 AIME-2025 items (same as 0/100 on LiveMathBench).
- Paradox-only clean bench: LiveMathBench (not in these tables). Leaked on Qwen2.5-Math-7B and Qwen3-8B: MATH-500 and MinervaMath.
- Drawn below: Shao's six non-Qwen checkpoints (Llama-3.1-8B / -Instruct / -Base, Llama-3.2-3B / -Instruct, OLMo-2-1124-7B / -SFT) × MATH-500, AMC 2023, AIME 2024, Minerva Math ([Shao §3](https://arxiv.org/html/2506.10947v2#S3), [Paradox App C](https://arxiv.org/html/2601.11061v1#A3)). Every jsonl row with `leakage_free: true` on those benches, from every paper (basis stays `id` / `rl_stage`). Shao Figure 3 MATH-500 curves are not extracted.

## Leakage-free: gain over the starting checkpoint

Cell = method − the paper's starting checkpoint (pretrained, instruct, or distilled), percentage points, one decimal. `avg@k` is not `pass@k`. A trailing `†` means the paper picked a checkpoint using eval benches. Blank if that paper does not report the starting checkpoint on that bench. Numbers stay inside one experiment (same table, train data, and metric).

### Llama-3.1-8B-Instruct

| method | id | metric | AIME24 | AMC23 | MATH500 | Minerva |
|---|---|---|---|---|---|---|
| [GRPO](https://arxiv.org/abs/2509.03646) | 2509.03646 | avg@32 | +4.7 |  |  |  |
| [GRPO](https://arxiv.org/abs/2509.03646) | 2509.03646 | avg@4 |  | +7.9 |  |  |
| [GRPO](https://arxiv.org/abs/2509.03646) | 2509.03646 | pass@1 |  |  | +2.8 | +6.3 |
| [HICRA](https://arxiv.org/abs/2509.03646) | 2509.03646 | avg@32 | +4.1 |  |  |  |
| [HICRA](https://arxiv.org/abs/2509.03646) | 2509.03646 | avg@4 |  | +10.0 |  |  |
| [HICRA](https://arxiv.org/abs/2509.03646) | 2509.03646 | pass@1 |  |  | +4.6 | +4.9 |
| [TTRL](https://arxiv.org/abs/2504.16084) | 2504.16084 | pass@1 | +5.4 | +9.0 | +15.1 |  |
| [RFT](https://arxiv.org/abs/2503.02875) | 2503.02875 | acc | +3.4 |  |  |  |
| [SFT](https://arxiv.org/abs/2503.02875) | 2503.02875 | acc | +0.0 |  |  |  |
| [UPFT](https://arxiv.org/abs/2503.02875) | 2503.02875 | acc | +3.4 |  |  |  |
| [V-STaR](https://arxiv.org/abs/2503.02875) | 2503.02875 | acc | +3.4 |  |  |  |
| [EM-FT](https://arxiv.org/abs/2505.15134) | 2505.15134 | pass@1 | +2.3 | +3.6 | +1.6 | -3.6 |
| [EM-RL](https://arxiv.org/abs/2505.15134) | 2505.15134 | pass@1 | +4.6 | +0.0 | +0.4 | -3.3 |
| [EM-RL-sequence](https://arxiv.org/abs/2505.15134) | 2505.15134 | pass@1 | +6.8 | +0.0 | +1.0 | -4.0 |
| [RLOO](https://arxiv.org/abs/2505.15134) | 2505.15134 | pass@1 | +2.3 | +7.2 | +11.4 | +4.4 |

### Llama-3.2-3B-Instruct

| method | id | metric | MATH500 | AIME24 | AMC23 | Minerva |
|---|---|---|---|---|---|---|
| [ConSPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | pass@1 | +31.0† |  |  |  |
| [DAPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | pass@1 | +26.4† |  |  |  |
| [GRPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | pass@1 | +26.4† |  |  |  |
| [Critique-GRPO](https://arxiv.org/abs/2506.03106) | 2506.03106 | pass@1 |  | +6.7 | +7.5 | +8.4 |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@8 |  | -0.4† | +0.0† |  |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | pass@1 | +5.0† |  |  | +0.7† |
| [GRPO](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@8 |  | +2.9† | +2.5† |  |
| [GRPO](https://arxiv.org/abs/2504.20571) | 2504.20571 | pass@1 | +2.4† |  |  | +3.7† |

### Llama-3.2-3B

| method | id | metric | AIME24 | AMC23 | Minerva |
|---|---|---|---|---|---|
| [DFT](https://arxiv.org/abs/2508.05629) | 2508.05629 | avg@16 | +0.4 | +2.4 | +1.5 |
| [SFT](https://arxiv.org/abs/2508.05629) | 2508.05629 | avg@16 | -0.4 | +1.6 | +1.0 |
| [Dr.GRPO](https://arxiv.org/abs/2503.20783) | 2503.20783 | pass@1 | +3.3 | +4.8 | +4.7 |

### Other checkpoints

| method | id | metric | Llama-3.1-8B-Base · AIME24 | Llama-3.1-8B-Base · AMC23 | Llama-3.1-8B-Base · Minerva |
|---|---|---|---|---|---|
| [DFT](https://arxiv.org/abs/2508.05629) | 2508.05629 | avg@16 | +0.2 | +11.0 | +7.3 |
| [SFT](https://arxiv.org/abs/2508.05629) | 2508.05629 | avg@16 | -0.2 | +4.2 | +4.8 |

## Leakage-free: gain over GRPO

Cell = method − the paper's vanilla GRPO, or the nearest vanilla RLVR baseline when GRPO is absent (`vs` column). A trailing `*` means the reference is not vanilla GRPO. The reference method itself is omitted. Equal scores of different methods show `+0.0`. Blank if no RLVR baseline is reported on that bench. Same experiment only.

### Llama-3.2-3B-Instruct

| method | id | metric | vs | AIME24 | MATH500 | AMC23 | Minerva |
|---|---|---|---|---|---|---|---|
| [ConSPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | pass@1 | GRPO |  | +4.6† |  |  |
| [DAPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | pass@1 | GRPO |  | +0.0† |  |  |
| [E2H-C](https://arxiv.org/abs/2506.06632) | 2506.06632 | pass@1 | GRPO | +6.7 |  |  |  |
| [E2H-G](https://arxiv.org/abs/2506.06632) | 2506.06632 | pass@1 | GRPO | +3.3 |  |  |  |
| [Self-Evolve](https://arxiv.org/abs/2506.06632) | 2506.06632 | pass@1 | GRPO | +3.3 |  |  |  |
| [Critique-GRPO](https://arxiv.org/abs/2506.03106) | 2506.03106 | pass@1 | GRPO | +6.7 |  | +7.5 | +6.2 |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@8 | GRPO | -3.3† |  | -2.5† |  |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | pass@1 | GRPO |  | +2.6† |  | -3.0† |

### Llama-3.1-8B-Instruct

| method | id | metric | vs | AIME24 | AMC23 | MATH500 | Minerva |
|---|---|---|---|---|---|---|---|
| [HICRA](https://arxiv.org/abs/2509.03646) | 2509.03646 | avg@32 | GRPO | -0.6 |  |  |  |
| [HICRA](https://arxiv.org/abs/2509.03646) | 2509.03646 | avg@4 | GRPO |  | +2.1 |  |  |
| [HICRA](https://arxiv.org/abs/2509.03646) | 2509.03646 | pass@1 | GRPO |  |  | +1.8 | -1.4 |
| [EM-FT](https://arxiv.org/abs/2505.15134) | 2505.15134 | pass@1 | RLOO | +0.0* | -3.6* | -9.8* | -8.0* |
| [EM-RL](https://arxiv.org/abs/2505.15134) | 2505.15134 | pass@1 | RLOO | +2.3* | -7.2* | -11.0* | -7.7* |
| [EM-RL-sequence](https://arxiv.org/abs/2505.15134) | 2505.15134 | pass@1 | RLOO | +4.5* | -7.2* | -10.4* | -8.4* |

## Gain over the starting checkpoint

Cell = method − the paper's starting checkpoint (pretrained, instruct, or distilled), percentage points, one decimal. `avg@k` is not `pass@k`. A trailing `†` means the paper picked a checkpoint using eval benches (ConSPO: every 100 steps; 1-shot RLVR: best mean on six benches including AIME25). Temporal OOD of the tasks still holds; the final score is not an independent hold-out. A trailing `‡` marks |Δ| < 2 pp on last-point SVG curves (AIME n=30). GRPO-format / incorrect / majority / random, 2-GRPO+RS, and R1-GRPO are omitted. Blank if that paper does not report the starting checkpoint on that bench. Numbers stay inside one experiment (same table, train data, and metric).

### DeepSeek-R1-Distill-Qwen-1.5B

| method | id | metric | AIME26 | AIME25 | HMMT25 |
|---|---|---|---|---|---|
| [CISPO · DeepScaleR](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +9.1† | +2.3† | +3.6† |
| [ConSPO · DeepScaleR](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +10.0† | +6.0† | +5.2† |
| [ConSPO · DAPO-Math](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +10.9† |  |  |
| [DAPO · DeepScaleR](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +6.9† | +2.2† | +3.8† |
| [DAPO · DAPO-Math](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +5.7† |  |  |
| [DisCO · DeepScaleR](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +7.8† | +4.1† | +4.7† |
| [DisCO · DAPO-Math](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +6.3† |  |  |
| [Dr.GRPO · DeepScaleR](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +5.6† | +1.3† | +1.0† |
| [Dr.GRPO · DAPO-Math](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +5.7† |  |  |
| [GMPO · DeepScaleR](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +9.9† | +3.9† | +3.1† |
| [GRPO · DeepScaleR](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +6.5† | +2.2† | +2.0† |
| [GRPO · DAPO-Math](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +7.7† |  |  |
| [SAPO · DeepScaleR](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +9.4† | +4.6† | +3.1† |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@64 |  | +0.2† |  |
| [GRPO](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@64 |  | +3.9† |  |

### DeepSeek-R1-Distill-Qwen-7B

| method | id | metric | AIME25 | AIME26 | HMMT25 |
|---|---|---|---|---|---|
| [ConSPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +8.8† | +11.3† | +4.0† |
| [DAPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +3.9† | +2.4† | +2.9† |
| [DisCO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +6.6† | +9.6† | +2.1† |
| [Dr.GRPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +5.0† | +7.8† | +4.2† |
| [GRPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +5.6† | +8.4† | +3.2† |
| [Critique-GRPO](https://arxiv.org/abs/2602.09000) | 2602.09000 | pass@1 | +1.0 |  |  |
| [GRPO](https://arxiv.org/abs/2602.09000) | 2602.09000 | pass@1 | +0.3 |  |  |
| [Self-Verification](https://arxiv.org/abs/2602.09000) | 2602.09000 | pass@1 | +0.9 |  |  |
| [iGRPO](https://arxiv.org/abs/2602.09000) | 2602.09000 | pass@1 | +1.6 |  |  |

### DeepSeek-R1-Distill-Llama-8B

| method | id | metric | AIME25 | AIME26 | HMMT25 |
|---|---|---|---|---|---|
| [ConSPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +8.3† | +14.9† | +9.1† |
| [DAPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +2.7† | +9.3† | +4.4† |
| [DisCO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +7.5† | +12.2† | +6.2† |
| [Dr.GRPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +5.5† | +11.8† | +6.1† |
| [GRPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +4.2† | +13.6† | +5.0† |

### Qwen2.5-Math-7B

| method | id | metric | AIME25 |
|---|---|---|---|
| [2-GRPO](https://arxiv.org/abs/2510.00977) | 2510.00977 | Mean@32 | +7.8 |
| [GRPO](https://arxiv.org/abs/2510.00977) | 2510.00977 | Mean@32 | +8.2 |
| [GRPO](https://arxiv.org/abs/2506.10947) | 2506.10947 | avg@8 | +7.4 |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@8 | +4.1† |
| [GRPO](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@8 | +7.9† |

### Qwen3-4B-Base

| method | id | metric | AIME26 |
|---|---|---|---|
| [ConSPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +8.0† |
| [DAPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +3.7† |
| [DisCO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +4.6† |
| [Dr.GRPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +7.6† |
| [GRPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +5.7† |

### Llama-3.2-3B-Instruct

| method | id | metric | AIME25 |
|---|---|---|---|
| [GRPO](https://arxiv.org/abs/2506.10947) | 2506.10947 | avg@8 | +0.2‡ |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@8 | -0.5† |
| [GRPO](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@8 | -0.9† |

### Qwen2.5-1.5B

| method | id | metric | AIME25 |
|---|---|---|---|
| [GRPO](https://arxiv.org/abs/2506.10947) | 2506.10947 | avg@8 | +1.1‡ |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@8 | -1.3† |
| [GRPO](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@8 | -0.9† |

### Qwen2.5-Math-1.5B

| method | id | metric | AIME25 |
|---|---|---|---|
| [GRPO](https://arxiv.org/abs/2506.10947) | 2506.10947 | avg@8 | +1.5‡ |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@8 | +2.5† |
| [GRPO](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@8 | +3.7† |

### Other checkpoints

| method | id | metric | Qwen2.5-Math-1.5B-Instruct · AIME25 | Qwen3-4B-Instruct-2507 · AIME26 |
|---|---|---|---|---|
| [DAPO](https://arxiv.org/abs/2606.23740) | 2606.23740 | pass@1 |  | +0.0 |
| [GRPO](https://arxiv.org/abs/2606.23740) | 2606.23740 | pass@1 |  | +3.3 |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@8 | +5.4† |  |
| [GRPO](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@8 | +5.4† |  |

## Gain over GRPO

Cell = method − the paper's vanilla GRPO, or the nearest vanilla RLVR baseline when GRPO is absent (`vs` column). A trailing `*` means the reference is not vanilla GRPO (Dr. GRPO, DAPO, PPO, RLOO, REINFORCE++). `†` means a checkpoint chosen on eval benches (ConSPO every 100 steps; 1-shot RLVR best mean on six benches including AIME25). `‡` marks |Δ| < 2 pp on last-point SVG curves (AIME n=30). GRPO-format / incorrect / majority / random, 2-GRPO+RS, and R1-GRPO are omitted. The reference method itself is omitted. Equal scores of different methods show `+0.0`. Blank if no RLVR baseline is reported on that bench. Same experiment only.

### DeepSeek-R1-Distill-Qwen-1.5B

| method | id | metric | vs | AIME26 | AIME25 | HMMT25 |
|---|---|---|---|---|---|---|
| [CISPO · DeepScaleR](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | GRPO | +2.6† | +0.1† | +1.6† |
| [ConSPO · DeepScaleR](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | GRPO | +3.5† | +3.8† | +3.2† |
| [ConSPO · DAPO-Math](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | GRPO | +3.2† |  |  |
| [DAPO · DeepScaleR](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | GRPO | +0.4† | +0.0† | +1.8† |
| [DAPO · DAPO-Math](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | GRPO | -2.0† |  |  |
| [DisCO · DeepScaleR](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | GRPO | +1.3† | +1.9† | +2.7† |
| [DisCO · DAPO-Math](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | GRPO | -1.4† |  |  |
| [Dr.GRPO · DeepScaleR](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | GRPO | -0.9† | -0.9† | -1.0† |
| [Dr.GRPO · DAPO-Math](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | GRPO | -2.0† |  |  |
| [GMPO · DeepScaleR](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | GRPO | +3.4† | +1.7† | +1.1† |
| [SAPO · DeepScaleR](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | GRPO | +2.9† | +2.4† | +1.1† |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@64 | GRPO |  | -3.7† |  |

### DeepSeek-R1-Distill-Qwen-7B

| method | id | metric | vs | AIME25 | AIME26 | HMMT25 |
|---|---|---|---|---|---|---|
| [ConSPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | GRPO | +3.2† | +2.9† | +0.8† |
| [DAPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | GRPO | -1.7† | -6.0† | -0.3† |
| [DisCO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | GRPO | +1.0† | +1.2† | -1.1† |
| [Dr.GRPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | GRPO | -0.6† | -0.6† | +1.0† |
| [Critique-GRPO](https://arxiv.org/abs/2602.09000) | 2602.09000 | pass@1 | GRPO | +0.7 |  |  |
| [Self-Verification](https://arxiv.org/abs/2602.09000) | 2602.09000 | pass@1 | GRPO | +0.6 |  |  |
| [iGRPO](https://arxiv.org/abs/2602.09000) | 2602.09000 | pass@1 | GRPO | +1.3 |  |  |

### DeepSeek-R1-Distill-Llama-8B

| method | id | metric | vs | AIME25 | AIME26 | HMMT25 |
|---|---|---|---|---|---|---|
| [ConSPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | GRPO | +4.1† | +1.3† | +4.1† |
| [DAPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | GRPO | -1.5† | -4.3† | -0.6† |
| [DisCO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | GRPO | +3.3† | -1.4† | +1.2† |
| [Dr.GRPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | GRPO | +1.3† | -1.8† | +1.1† |

### Qwen3-4B-Base

| method | id | metric | vs | AIME26 |
|---|---|---|---|---|
| [ConSPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | GRPO | +2.3† |
| [DAPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | GRPO | -2.0† |
| [DisCO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | GRPO | -1.1† |
| [Dr.GRPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | GRPO | +1.9† |

### Other checkpoints

| method | id | metric | vs | Qwen2.5-Math-7B · AIME25 | DeepSeek-R1-Distill-Qwen-32B · AIME25 | DeepSeek-R1-Distill-Qwen-32B · AIME26 | Llama-3.2-3B-Instruct · AIME25 | Qwen2.5-1.5B · AIME25 | Qwen2.5-Math-1.5B · AIME25 | Qwen2.5-Math-1.5B-Instruct · AIME25 | Qwen3-4B-Instruct-2507 · AIME26 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [DAPO](https://arxiv.org/abs/2606.23740) | 2606.23740 | pass@1 | GRPO |  |  |  |  |  |  |  | -3.3 |
| [ConSPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | GRPO |  | +3.2† | +2.9† |  |  |  |  |  |
| [2-GRPO](https://arxiv.org/abs/2510.00977) | 2510.00977 | Mean@32 | GRPO | -0.4 |  |  |  |  |  |  |  |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@8 | GRPO | -3.8† |  |  |  |  |  |  |  |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@8 | GRPO |  |  |  | +0.4† |  |  |  |  |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@8 | GRPO |  |  |  |  | -0.4† |  |  |  |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@8 | GRPO |  |  |  |  |  | -1.2† |  |  |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@8 | GRPO |  |  |  |  |  |  | +0.0† |  |

## Not applicable

Trained open models with an OOD list, but only from-scratch pretraining (`pretrain` / `next-token` / `autoregressive` / `MLM` / `causal LM`). Continued / mid-training pretrain is not from-scratch. There is no starting checkpoint to subtract.

| id | paper | methods |
|---|---|---|
| 2607.02303 | [HOLA: A Hippocampus for Linear Attention](https://arxiv.org/abs/2607.02303) | pretrain (same-backbone GDN anchor), pretrain |
| 2405.12250 | [Your Transformer is Secretly Linear (ACL 2024, A](https://arxiv.org/abs/2405.12250) | pretrain + cosine-similarity regularization |
| 2312.04927 | [Zoology: Measuring and Improving Recall in Effic](https://arxiv.org/abs/2312.04927) | pretrain |
| 2302.10866 | [Hyena Hierarchy](https://arxiv.org/abs/2302.10866) | autoregressive LM |
| 2512.16902 | [In-Context Algebra](https://arxiv.org/abs/2512.16902) | next-token prediction (nanoGPT + RoPE) |
| 2503.21676 | [How do language models learn facts? (DeepMind)](https://arxiv.org/abs/2503.21676) | next-token pre-training; fine-tuning on new individuals |
| 2407.20311 | [2.1](https://arxiv.org/abs/2407.20311) | autoregressive pretrain from scratch |
| 2309.14316 | [3.1](https://arxiv.org/abs/2309.14316) | MLM mixed training; BIO pretrain + QA finetune, mixed training; BIO pretrain + Q |
| 2309.14402 | [3.2](https://arxiv.org/abs/2309.14402) | mixed training; BIO pretrain + LoRA QA finetune, BIO pretrain + LoRA QA finetune |
| 2405.20541 | [Perplexed by Perplexity: Data Pruning With Small](https://arxiv.org/abs/2405.20541) | next-token prediction on perplexity-pruned data |
| 2405.18392 | [Scaling Laws and Compute-Optimal Training Beyond](https://arxiv.org/abs/2405.18392) | pretrain (AdamW; cosine vs constant+cooldown) |
| 2307.06440 | [No Train No Gain: Revisiting Efficient Training ](https://arxiv.org/abs/2307.06440) | MLM pre-training (AdamW vs layer stacking, layer dropping, selective backprop, R |
| 2507.18074 | [AlphaGo Moment for Model Architecture Discovery](https://arxiv.org/abs/2507.18074) | next-token LM (AdamW / FLAME) |
