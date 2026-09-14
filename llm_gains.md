# Compact OOD gains

Per-paper numbers from `filter/fulltext/*.md`, stored in `filter/llm_gains.jsonl`. One jsonl row is one (paper × method × model × bench × train data × source table). Markdown keeps only **temporal OOD**: the bench date is after the full training-chain cutoff. Historical benches and version-only LCB slices stay in the jsonl as `rl_stage` / `id` / `unverified` and are not drawn. API and GPT-family models are omitted. Model inventory: [`llm_models.md`](llm_models.md).

## Summary

- Papers with at least one temporal OOD number: **8**
- Temporal gain cells vs starting checkpoint: **59**
- Temporal gain cells vs GRPO / nearest RLVR: **40**
- From-scratch papers (no starting checkpoint): **13**

## Gain over the starting checkpoint

Cell = method − the paper's starting checkpoint (pretrained, instruct, or distilled), percentage points, one decimal. `avg@k` is not `pass@k`. A trailing `†` means the paper picked a checkpoint using eval benches (ConSPO: every 100 steps; 1-shot RLVR: best mean on six benches including AIME25). Temporal OOD of the tasks still holds; the final score is not an independent hold-out. Blank if that paper does not report the starting checkpoint on that bench. Numbers stay inside one experiment (same table, train data, and metric).

### DeepSeek-R1-Distill-Qwen-1.5B

| method | id | metric | AIME25 | AIME26 | HMMT25 |
|---|---|---|---|---|---|
| [ConSPO · DAPO-Math](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +5.1† | +10.9† | +4.5† |
| [ConSPO · DeepScaleR](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +6.0† | +10.0† | +5.2† |
| [DAPO · DAPO-Math](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +1.7† | +5.7† | +3.1† |
| [DAPO · DeepScaleR](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +2.2† | +6.9† | +3.8† |
| [GRPO · DAPO-Math](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +2.0† | +7.7† | +3.4† |
| [GRPO · DeepScaleR](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +2.2† | +6.5† | +2.0† |
| [SR-GRPO](https://arxiv.org/abs/2512.02807) | 2512.02807 | pass@1 | +6.7 |  |  |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@64 | +0.2† |  |  |
| [GRPO](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@64 | +3.9† |  |  |

### Qwen2.5-Math-7B

| method | id | metric | AIME25 |
|---|---|---|---|
| [2-GRPO](https://arxiv.org/abs/2510.00977) | 2510.00977 | Mean@32 | +7.8 |
| [2-GRPO+RS](https://arxiv.org/abs/2510.00977) | 2510.00977 | Mean@32 | +6.7 |
| [2-GRPO+RS-DAPO](https://arxiv.org/abs/2510.00977) | 2510.00977 | Mean@32 | +11.7 |
| [2-GRPO-DAPO](https://arxiv.org/abs/2510.00977) | 2510.00977 | Mean@32 | +9.6 |
| [GRPO](https://arxiv.org/abs/2510.00977) | 2510.00977 | Mean@32 | +8.2 |
| [GRPO-DAPO](https://arxiv.org/abs/2510.00977) | 2510.00977 | Mean@32 | +9.3 |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@8 | +4.1† |
| [GRPO](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@8 | +7.9† |
| [GRPO-format](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@8 | +0.0† |

### DeepSeek-R1-Distill-Qwen-7B

| method | id | metric | AIME25 | AIME26 |
|---|---|---|---|---|
| [ConSPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +8.8† | +11.3† |
| [SFT](https://arxiv.org/abs/2603.24472) | 2603.24472 | pass@1 | -25.2 |  |
| [Critique-GRPO](https://arxiv.org/abs/2602.09000) | 2602.09000 | pass@1 | +1.0 |  |
| [GRPO](https://arxiv.org/abs/2602.09000) | 2602.09000 | pass@1 | +0.3 |  |
| [Self-Verification](https://arxiv.org/abs/2602.09000) | 2602.09000 | pass@1 | +0.9 |  |
| [iGRPO](https://arxiv.org/abs/2602.09000) | 2602.09000 | pass@1 | +1.6 |  |

### DeepSeek-R1-Distill-Llama-8B

| method | id | metric | HMMT25 | AIME25 | AIME26 |
|---|---|---|---|---|---|
| [ConSPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +9.1† | +8.3† | +14.9† |
| [DAPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +4.4† |  |  |
| [GRPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | +5.0† |  |  |

### Qwen2.5-Math-1.5B

| method | id | metric | AIME25 |
|---|---|---|---|
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@8 | +2.5† |
| [GRPO](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@8 | +3.7† |
| [GRPO-format](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@8 | +0.8† |

### Other checkpoints

| method | id | metric | Llama-3.1-8B-Instruct · AIME25 | Llama-3.2-3B-Instruct · AIME25 | Qwen2.5-1.5B · AIME25 | Qwen2.5-7B-Base · AIME25 | Qwen2.5-Math-1.5B-Instruct · AIME25 | Qwen3-4B-Instruct-2507 · AIME26 | Qwen2.5-1.5B-Instruct · AIME25 | Qwen3-4B-Base · AIME26 |
|---|---|---|---|---|---|---|---|---|---|---|
| [DAPO](https://arxiv.org/abs/2606.23740) | 2606.23740 | pass@1 |  |  |  |  |  | +0.0 |  |  |
| [GRPO](https://arxiv.org/abs/2606.23740) | 2606.23740 | pass@1 |  |  |  |  |  | +3.3 |  |  |
| [ConSPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 |  |  |  |  |  |  |  | +8.0† |
| [SR-GRPO](https://arxiv.org/abs/2512.02807) | 2512.02807 | pass@1 |  |  |  |  |  |  | +10.0 |  |
| [GRPO](https://arxiv.org/abs/2509.03646) | 2509.03646 | avg@32 | -0.1 |  |  |  |  |  |  |  |
| [HICRA](https://arxiv.org/abs/2509.03646) | 2509.03646 | avg@32 | +0.2 |  |  |  |  |  |  |  |
| [GRPO](https://arxiv.org/abs/2509.03646) | 2509.03646 | avg@32 |  |  |  | +9.7 |  |  |  |  |
| [HICRA](https://arxiv.org/abs/2509.03646) | 2509.03646 | avg@32 |  |  |  | +13.1 |  |  |  |  |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@8 |  | -0.5† |  |  |  |  |  |  |
| [GRPO](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@8 |  | -0.9† |  |  |  |  |  |  |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@8 |  |  | -1.3† |  |  |  |  |  |
| [GRPO](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@8 |  |  | -0.9† |  |  |  |  |  |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@8 |  |  |  |  | +5.4† |  |  |  |
| [GRPO](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@8 |  |  |  |  | +5.4† |  |  |  |

## Gain over GRPO

Cell = method − the paper's vanilla GRPO, or the nearest vanilla RLVR baseline when GRPO is absent (`vs` column). A trailing `*` means the reference is not vanilla GRPO (Dr. GRPO, DAPO, PPO, RLOO, REINFORCE++). `†` means a checkpoint chosen on eval benches (ConSPO every 100 steps; 1-shot RLVR best mean on six benches including AIME25). The reference method itself is omitted. Equal scores of different methods show `+0.0`. Blank if no RLVR baseline is reported on that bench. Same experiment only.

### Qwen2.5-Math-7B

| method | id | metric | vs | AIME25 |
|---|---|---|---|---|
| [2-GRPO](https://arxiv.org/abs/2510.00977) | 2510.00977 | Mean@32 | GRPO | -0.4 |
| [2-GRPO+RS](https://arxiv.org/abs/2510.00977) | 2510.00977 | Mean@32 | GRPO | -1.6 |
| [2-GRPO+RS-DAPO](https://arxiv.org/abs/2510.00977) | 2510.00977 | Mean@32 | GRPO | +2.4 |
| [2-GRPO-DAPO](https://arxiv.org/abs/2510.00977) | 2510.00977 | Mean@32 | GRPO | +0.3 |
| [GRPO-DAPO](https://arxiv.org/abs/2510.00977) | 2510.00977 | Mean@32 | GRPO | +0.0 |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@8 | GRPO | -3.8† |
| [GRPO-format](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@8 | GRPO | -7.9† |

### DeepSeek-R1-Distill-Qwen-1.5B

| method | id | metric | vs | AIME25 | AIME26 | HMMT25 |
|---|---|---|---|---|---|---|
| [ConSPO · DAPO-Math](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | GRPO | +3.1† | +3.2† | +1.1† |
| [ConSPO · DeepScaleR](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | GRPO | +3.8† | +3.5† | +3.2† |
| [DAPO · DAPO-Math](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | GRPO | -0.3† | -2.0† | -0.3† |
| [DAPO · DeepScaleR](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | GRPO | +0.0† | +0.4† | +1.8† |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@64 | GRPO | -3.7† |  |  |

### DeepSeek-R1-Distill-Qwen-7B

| method | id | metric | vs | AIME25 | AIME26 |
|---|---|---|---|---|---|
| [ConSPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | GRPO | +3.2† | +2.9† |
| [Critique-GRPO](https://arxiv.org/abs/2602.09000) | 2602.09000 | pass@1 | GRPO | +0.7 |  |
| [Self-Verification](https://arxiv.org/abs/2602.09000) | 2602.09000 | pass@1 | GRPO | +0.6 |  |
| [iGRPO](https://arxiv.org/abs/2602.09000) | 2602.09000 | pass@1 | GRPO | +1.3 |  |

### Other checkpoints (1)

| method | id | metric | vs | DeepSeek-R1-Distill-Llama-8B · HMMT25 | Qwen2.5-Math-1.5B · AIME25 | DeepSeek-R1-Distill-Llama-8B · AIME25 | DeepSeek-R1-Distill-Llama-8B · AIME26 | DeepSeek-R1-Distill-Qwen-32B · AIME25 | DeepSeek-R1-Distill-Qwen-32B · AIME26 | Llama-3.1-8B-Instruct · AIME25 | Llama-3.2-3B-Instruct · AIME25 | Qwen2.5-1.5B · AIME25 | Qwen2.5-7B-Base · AIME25 | Qwen2.5-Math-1.5B-Instruct · AIME25 | Qwen3-4B-Base · AIME26 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [ConSPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | GRPO | +4.1† |  | +4.1† | +1.3† |  |  |  |  |  |  |  |  |
| [DAPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | GRPO | -0.6† |  |  |  |  |  |  |  |  |  |  |  |
| [ConSPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | GRPO |  |  |  |  | +3.2† | +2.9† |  |  |  |  |  |  |
| [ConSPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | avg@32 | GRPO |  |  |  |  |  |  |  |  |  |  |  | +2.3† |
| [HICRA](https://arxiv.org/abs/2509.03646) | 2509.03646 | avg@32 | GRPO |  |  |  |  |  |  | +0.3 |  |  |  |  |  |
| [HICRA](https://arxiv.org/abs/2509.03646) | 2509.03646 | avg@32 | GRPO |  |  |  |  |  |  |  |  |  | +3.4 |  |  |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@8 | GRPO |  |  |  |  |  |  |  | +0.4† |  |  |  |  |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@8 | GRPO |  |  |  |  |  |  |  |  | -0.4† |  |  |  |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@8 | GRPO |  | -1.2† |  |  |  |  |  |  |  |  |  |  |
| [GRPO-format](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@8 | GRPO |  | -2.9† |  |  |  |  |  |  |  |  |  |  |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | avg@8 | GRPO |  |  |  |  |  |  |  |  |  |  | +0.0† |  |

### Other checkpoints (2)

| method | id | metric | vs | Qwen3-4B-Instruct-2507 · AIME26 |
|---|---|---|---|---|
| [DAPO](https://arxiv.org/abs/2606.23740) | 2606.23740 | pass@1 | GRPO | -3.3 |

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
