# Compact OOD gains

Per-paper numbers from `filter/fulltext/*.md`, stored in `filter/llm_gains.jsonl`. One jsonl row is one (paper × method × model × bench). Tables keep only **OOD** benches (from `filter/llm_models.jsonl`). API and GPT-family models are omitted. Model inventory and reliability notes: [`llm_models.md`](llm_models.md).

## Summary

- Papers with at least one OOD number: **40**
- OOD gain cells vs untrained: **783**
- OOD gain cells vs GRPO / nearest RLVR: **470**
- From-scratch papers (no untrained checkpoint): **14**

## Gain over the untrained checkpoint

Cell = method − untrained checkpoint, percentage points, one decimal. Blank if that paper does not report the starting checkpoint on that bench. Numbers stay inside one paper and one metric (`pass@1` / `avg@k`); deltas are never mixed across tables or papers.

### Qwen2.5-Math-7B

| code | id | AMC23 | Olymp | AIME24 | Minerva | MMLU-Pro | AIME25 | LCB | MATH500 | GSM8K | GPQA-D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [GRPO](https://arxiv.org/abs/2605.06241) | 2605.06241 | +27.2 |  | +9.6 |  |  |  |  |  |  |  |
| [GRPO](https://arxiv.org/abs/2605.06241) | 2605.06241 |  | +25.3 |  | +6.3 |  |  |  |  | +37.7 |  |
| [ReasonMaxxer](https://arxiv.org/abs/2605.06241) | 2605.06241 | +20.6 |  | +10.0 |  |  |  |  |  |  |  |
| [ReasonMaxxer](https://arxiv.org/abs/2605.06241) | 2605.06241 |  | +27.4 |  | +15.8 |  |  |  |  | +36.6 |  |
| [GRPO](https://arxiv.org/abs/2604.20659) | 2604.20659 | +38.7 | +18.0 | +19.2 |  |  |  |  |  |  |  |
| [GRPO-VPS](https://arxiv.org/abs/2604.20659) | 2604.20659 | +41.0 | +18.4 | +20.9 |  |  |  |  |  |  |  |
| [CISPO](https://arxiv.org/abs/2604.08690) | 2604.08690 |  |  |  |  | +9.2 |  | +3.6 |  |  |  |
| [Critique-GRPO](https://arxiv.org/abs/2604.08690) | 2604.08690 |  |  |  |  | +4.2 |  | +1.4 |  |  |  |
| [DAPO](https://arxiv.org/abs/2604.08690) | 2604.08690 |  |  |  |  | +8.5 |  | +3.2 |  |  |  |
| [GRPO](https://arxiv.org/abs/2604.08690) | 2604.08690 |  |  |  |  | +2.7 |  | +0.8 |  |  |  |
| [GSPO](https://arxiv.org/abs/2604.08690) | 2604.08690 |  |  |  |  | +6.6 |  | +2.4 |  |  |  |
| [PRIME](https://arxiv.org/abs/2604.08690) | 2604.08690 |  |  |  |  | +6.4 |  | +5.1 |  |  |  |
| [SAPO](https://arxiv.org/abs/2604.08690) | 2604.08690 |  |  |  |  | +10.1 |  | +2.7 |  |  |  |
| [SKPO](https://arxiv.org/abs/2604.08690) | 2604.08690 |  |  |  |  | +9.8 |  | +5.8 |  |  |  |
| [SPO](https://arxiv.org/abs/2604.08690) | 2604.08690 |  |  |  |  | +5.5 |  | +1.9 |  |  |  |
| [GRPO](https://arxiv.org/abs/2510.14901) | 2510.14901 |  |  |  |  |  |  |  |  |  | +0.1 |
| [2-GRPO](https://arxiv.org/abs/2510.00977) | 2510.00977 | +26.2 | +16.6 |  | +17.1 |  | +7.8 |  |  |  |  |
| [2-GRPO+RS](https://arxiv.org/abs/2510.00977) | 2510.00977 | +23.3 | +15.6 |  | +18.9 |  | +6.7 |  |  |  |  |
| [2-GRPO+RS-DAPO](https://arxiv.org/abs/2510.00977) | 2510.00977 | +30.5 | +18.6 |  | +18.0 |  | +11.7 |  |  |  |  |
| [2-GRPO-DAPO](https://arxiv.org/abs/2510.00977) | 2510.00977 | +26.5 | +20.0 |  | +16.0 |  | +9.6 |  |  |  |  |
| [GRPO](https://arxiv.org/abs/2510.00977) | 2510.00977 | +23.4 | +16.2 |  | +16.8 |  | +8.2 |  |  |  |  |
| [GRPO-DAPO](https://arxiv.org/abs/2510.00977) | 2510.00977 | +31.3 | +19.0 |  | +18.5 |  | +9.3 |  |  |  |  |
| [Critique-GRPO](https://arxiv.org/abs/2506.03106) | 2506.03106 |  |  |  |  | +4.1 |  |  |  |  | +13.6 |
| [Dr. GRPO](https://arxiv.org/abs/2503.20783) | 2503.20783 | +24.1 | +24.4 | +26.6 | +20.2 |  |  |  |  |  |  |
| [GRPO](https://arxiv.org/abs/2506.10947) | 2506.10947 |  |  | +15.3 |  |  |  |  |  |  |  |
| [GRPO](https://arxiv.org/abs/2506.10947) | 2506.10947 |  |  |  |  |  |  |  | +29.1 |  |  |
| [GRPO-format](https://arxiv.org/abs/2506.10947) | 2506.10947 | +13.8 |  | +10.3 |  |  |  |  |  |  |  |
| [GRPO-incorrect](https://arxiv.org/abs/2506.10947) | 2506.10947 | +24.1 |  | +10.2 |  |  |  |  |  |  |  |
| [GRPO-incorrect](https://arxiv.org/abs/2506.10947) | 2506.10947 |  |  |  |  |  |  |  | +24.1 |  |  |
| [GRPO-random](https://arxiv.org/abs/2506.10947) | 2506.10947 | +21.4 |  | +10.2 |  |  |  |  |  |  |  |
| [GRPO-random](https://arxiv.org/abs/2506.10947) | 2506.10947 |  |  |  |  |  |  |  | +21.4 |  |  |
| [EM-FT](https://arxiv.org/abs/2505.15134) | 2505.15134 | +20.5 | +15.4 | -1.2 | +18.4 |  |  |  |  |  |  |
| [EM-RL](https://arxiv.org/abs/2505.15134) | 2505.15134 | +26.5 | +16.9 | +3.3 | +16.2 |  |  |  |  |  |  |
| [EM-RL-sequence](https://arxiv.org/abs/2505.15134) | 2505.15134 | +21.7 | +16.6 | +5.5 | +16.2 |  |  |  |  |  |  |
| [GRPO](https://arxiv.org/abs/2505.15134) | 2505.15134 | +25.3 | +16.9 | +5.5 | +10.3 |  |  |  |  |  |  |
| [RLOO](https://arxiv.org/abs/2505.15134) | 2505.15134 | +26.5 | +15.2 | +7.7 | +16.5 |  |  |  |  |  |  |
| [SC-RL](https://arxiv.org/abs/2505.15134) | 2505.15134 | +20.5 | +17.7 | +0.0 | +11.4 |  |  |  |  |  |  |
| [SFT](https://arxiv.org/abs/2505.15134) | 2505.15134 | -1.1 | +3.4 | -5.6 | +2.9 |  |  |  |  |  |  |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | +25.0 |  | +11.7 |  |  | +4.1 |  |  |  |  |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 |  | +20.9 |  | +16.9 |  |  |  |  |  |  |
| [GRPO](https://arxiv.org/abs/2504.20571) | 2504.20571 | +27.2 |  | +13.7 |  |  | +7.9 |  |  |  |  |
| [GRPO](https://arxiv.org/abs/2504.20571) | 2504.20571 |  | +23.4 |  | +22.8 |  |  |  |  |  |  |
| [GRPO-format](https://arxiv.org/abs/2504.20571) | 2504.20571 | +19.1 |  | +12.1 |  |  | +0.0 |  |  |  |  |
| [GRPO-format](https://arxiv.org/abs/2504.20571) | 2504.20571 |  | +12.2 |  | +13.3 |  |  |  |  |  |  |

### Qwen3-8B

| code | id | AIME25 | AIME24 | GPQA-D | MMLU-Pro | HMMT25 | LCBv6 |
|---|---|---|---|---|---|---|---|
| [DAPO](https://arxiv.org/abs/2606.18810) | 2606.18810 | +19.2 | +18.3 |  |  |  |  |
| [GRPO](https://arxiv.org/abs/2606.18810) | 2606.18810 | +15.4 | +16.3 |  |  |  |  |
| [OPSD](https://arxiv.org/abs/2606.18810) | 2606.18810 | +3.3 | +8.3 |  |  |  |  |
| [REINFORCE++](https://arxiv.org/abs/2606.18810) | 2606.18810 | -2.5 | -7.1 |  |  |  |  |
| [SC-GRPO](https://arxiv.org/abs/2606.18810) | 2606.18810 | +23.3 | +26.3 |  |  |  |  |
| [GRPO](https://arxiv.org/abs/2601.20802) | 2601.20802 |  |  |  | -0.2 |  |  |
| [SDPO](https://arxiv.org/abs/2601.20802) | 2601.20802 |  |  |  | +0.4 |  |  |
| [SFT](https://arxiv.org/abs/2601.20802) | 2601.20802 |  |  |  | -0.6 |  |  |
| [GRPO](https://arxiv.org/abs/2601.18734) | 2601.18734 | +3.3 | +0.6 |  |  | +2.8 |  |
| [OPSD](https://arxiv.org/abs/2601.18734) | 2601.18734 | +5.2 | +2.0 |  |  | +1.9 |  |
| [SFT](https://arxiv.org/abs/2601.18734) | 2601.18734 | -1.4 | -3.5 |  |  | -1.0 |  |
| [GRPO](https://arxiv.org/abs/2509.13232) | 2509.13232 | +1.6 | +5.5 |  |  | +7.4 |  |
| [SPO](https://arxiv.org/abs/2509.13232) | 2509.13232 | +6.0 | +6.2 |  |  | +10.7 |  |
| [GEPA](https://arxiv.org/abs/2507.19457) | 2507.19457 | +4.7 |  |  |  |  |  |
| [GRPO](https://arxiv.org/abs/2507.19457) | 2507.19457 | +10.7 |  |  |  |  |  |
| [Critique-GRPO](https://arxiv.org/abs/2506.03106) | 2506.03106 |  |  | +12.1 | +2.2 |  |  |
| [Dr. GRPO](https://arxiv.org/abs/2506.03106) | 2506.03106 |  |  | +8.6 | +2.3 |  |  |
| [R1-GRPO](https://arxiv.org/abs/2506.03106) | 2506.03106 |  |  | +4.5 | +1.8 |  |  |
| [RAFT](https://arxiv.org/abs/2506.03106) | 2506.03106 |  |  | +2.0 | +0.8 |  |  |
| [SFT](https://arxiv.org/abs/2506.03106) | 2506.03106 |  |  | +2.5 | -1.4 |  |  |
| [GRPO](https://arxiv.org/abs/2608.19197) | 2608.19197 |  |  | +0.5 |  |  |  |
| [GRPO](https://arxiv.org/abs/2608.19197) | 2608.19197 |  |  |  |  |  | +0.5 |
| [RLVE](https://arxiv.org/abs/2608.19197) | 2608.19197 |  |  | +2.2 |  |  |  |
| [RLVE](https://arxiv.org/abs/2608.19197) | 2608.19197 |  |  |  |  |  | +1.1 |
| [SPADE](https://arxiv.org/abs/2608.19197) | 2608.19197 |  |  | +3.5 |  |  |  |
| [SPADE](https://arxiv.org/abs/2608.19197) | 2608.19197 |  |  |  |  |  | +3.1 |

### DeepSeek-R1-Distill-Qwen-1.5B

| code | id | Olymp | AIME24 | AIME25 | HMMT25 | AMC23 | Minerva | MATH500 | GSM8K | GPQA |
|---|---|---|---|---|---|---|---|---|---|---|
| [OPD-top1](https://arxiv.org/abs/2606.06021) | 2606.06021 |  | +9.4 | +11.6 |  |  |  |  |  |  |
| [OPD-top16](https://arxiv.org/abs/2606.06021) | 2606.06021 |  | +14.2 | +12.1 |  |  |  |  |  |  |
| [OPRD](https://arxiv.org/abs/2606.06021) | 2606.06021 |  | +16.9 | +12.7 |  |  |  |  |  |  |
| [ConSPO](https://arxiv.org/abs/2605.12969) | 2605.12969 |  |  |  | +5.2 |  |  |  |  |  |
| [ConSPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | +13.5 |  |  |  |  |  |  |  |  |
| [ConSPO-DAPO](https://arxiv.org/abs/2605.12969) | 2605.12969 |  |  |  | +4.5 |  |  |  |  |  |
| [ConSPO-DAPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | +14.4 |  |  |  |  |  |  |  |  |
| [DAPO](https://arxiv.org/abs/2605.12969) | 2605.12969 |  |  |  | +3.8 |  |  |  |  |  |
| [DAPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | +12.6 |  |  |  |  |  |  |  |  |
| [DAPO-DAPO](https://arxiv.org/abs/2605.12969) | 2605.12969 |  |  |  | +3.1 |  |  |  |  |  |
| [DAPO-DAPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | +11.9 |  |  |  |  |  |  |  |  |
| [GRPO](https://arxiv.org/abs/2605.12969) | 2605.12969 |  |  |  | +2.0 |  |  |  |  |  |
| [GRPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | +8.9 |  |  |  |  |  |  |  |  |
| [GRPO-DAPO](https://arxiv.org/abs/2605.12969) | 2605.12969 |  |  |  | +3.4 |  |  |  |  |  |
| [GRPO-DAPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | +7.0 |  |  |  |  |  |  |  |  |
| [GRPO](https://arxiv.org/abs/2605.06241) | 2605.06241 |  | -1.7 |  |  | -0.7 |  |  |  |  |
| [GRPO](https://arxiv.org/abs/2605.06241) | 2605.06241 | +4.3 |  |  |  |  | +2.6 |  | +1.8 |  |
| [ReasonMaxxer](https://arxiv.org/abs/2605.06241) | 2605.06241 |  | +2.5 |  |  | -3.5 |  |  |  |  |
| [ReasonMaxxer](https://arxiv.org/abs/2605.06241) | 2605.06241 | +14.8 |  |  |  |  | +7.7 |  | +5.0 |  |
| [SR-GRPO](https://arxiv.org/abs/2512.02807) | 2512.02807 | +14.9 |  | +6.7 |  | +0.0 |  | +3.4 |  | +4.5 |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 |  | +1.2 | +0.2 |  | +2.9 |  |  |  |  |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | +1.5 |  |  |  |  | +1.9 | +1.0 |  |  |
| [GRPO](https://arxiv.org/abs/2504.20571) | 2504.20571 |  | +2.9 | +3.9 |  | +6.9 |  |  |  |  |
| [GRPO](https://arxiv.org/abs/2504.20571) | 2504.20571 | +3.8 |  |  |  |  | +3.1 | +1.6 |  |  |

### Llama-3.2-3B-Instruct

| code | id | MMLU-Pro | LCB | MATH500 | Olymp | AIME24 | AIME25 | AMC23 | Minerva | GPQA-D | LCBv6 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [ConSPO](https://arxiv.org/abs/2605.12969) | 2605.12969 |  |  | +31.0 | +11.1 |  |  |  |  |  |  |
| [DAPO](https://arxiv.org/abs/2605.12969) | 2605.12969 |  |  | +26.4 | +9.1 |  |  |  |  |  |  |
| [GRPO](https://arxiv.org/abs/2605.12969) | 2605.12969 |  |  | +26.4 | +9.4 |  |  |  |  |  |  |
| [CISPO](https://arxiv.org/abs/2604.08690) | 2604.08690 | +0.4 | -0.3 |  |  |  |  |  |  |  |  |
| [DAPO](https://arxiv.org/abs/2604.08690) | 2604.08690 | +0.7 | +0.3 |  |  |  |  |  |  |  |  |
| [GRPO](https://arxiv.org/abs/2604.08690) | 2604.08690 | +0.7 | +0.7 |  |  |  |  |  |  |  |  |
| [GSPO](https://arxiv.org/abs/2604.08690) | 2604.08690 | +1.0 | +1.4 |  |  |  |  |  |  |  |  |
| [PRIME](https://arxiv.org/abs/2604.08690) | 2604.08690 | +0.6 | +0.8 |  |  |  |  |  |  |  |  |
| [SAPO](https://arxiv.org/abs/2604.08690) | 2604.08690 | +0.9 | +0.2 |  |  |  |  |  |  |  |  |
| [SKPO](https://arxiv.org/abs/2604.08690) | 2604.08690 | +0.6 | +1.7 |  |  |  |  |  |  |  |  |
| [SPO](https://arxiv.org/abs/2604.08690) | 2604.08690 | +0.3 | +0.5 |  |  |  |  |  |  |  |  |
| [Critique-GRPO](https://arxiv.org/abs/2506.03106) | 2506.03106 | +5.6 |  |  |  |  |  |  |  | +14.6 |  |
| [R1-GRPO](https://arxiv.org/abs/2506.03106) | 2506.03106 | +2.6 |  |  |  |  |  |  |  | +7.1 |  |
| [GRPO](https://arxiv.org/abs/2505.19590) | 2505.19590 |  |  |  |  |  |  |  |  |  | +0.0 |
| [Intuitor](https://arxiv.org/abs/2505.19590) | 2505.19590 |  |  |  |  |  |  |  |  |  | +0.0 |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 |  |  |  |  | -0.4 | -0.5 | +0.0 |  |  |  |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 |  |  | +5.0 | +3.8 |  |  |  | +0.7 |  |  |
| [GRPO](https://arxiv.org/abs/2504.20571) | 2504.20571 |  |  |  |  | +2.9 | -0.9 | +2.5 |  |  |  |
| [GRPO](https://arxiv.org/abs/2504.20571) | 2504.20571 |  |  | +2.4 | +3.2 |  |  |  | +3.7 |  |  |

### Qwen2.5-Math-1.5B

| code | id | AMC23 | AIME24 | Olymp | Minerva | AIME25 |
|---|---|---|---|---|---|---|
| [GRPO](https://arxiv.org/abs/2604.20659) | 2604.20659 | +30.6 | +12.5 | +11.0 |  |  |
| [GRPO-VPS](https://arxiv.org/abs/2604.20659) | 2604.20659 | +38.7 | +9.2 | +13.1 |  |  |
| [DFT](https://arxiv.org/abs/2508.05629) | 2508.05629 | +18.8 | +2.7 | +11.2 | +12.4 |  |
| [DFT-OpenR1](https://arxiv.org/abs/2508.05629) | 2508.05629 | +29.5 | +5.6 | +17.6 | +18.5 |  |
| [DFT-offline](https://arxiv.org/abs/2508.05629) | 2508.05629 | +29.1 | +3.8 | +15.0 | +16.6 |  |
| [GRPO](https://arxiv.org/abs/2508.05629) | 2508.05629 | +21.9 | +4.2 | +12.7 | +10.4 |  |
| [PPO](https://arxiv.org/abs/2508.05629) | 2508.05629 | +18.6 | +3.3 | +10.4 | +6.9 |  |
| [RFT](https://arxiv.org/abs/2508.05629) | 2508.05629 | +11.4 | +0.2 | +6.4 | +5.7 |  |
| [SFT](https://arxiv.org/abs/2508.05629) | 2508.05629 | -0.6 | -2.3 | -3.2 | +4.5 |  |
| [SFT-OpenR1](https://arxiv.org/abs/2508.05629) | 2508.05629 | +16.1 | +0.0 | +8.4 | +11.8 |  |
| [Dr. GRPO](https://arxiv.org/abs/2503.20783) | 2503.20783 | +20.5 | +0.0 | +14.8 | +13.2 |  |
| [GRPO-random](https://arxiv.org/abs/2506.10947) | 2506.10947 | +4.9 |  |  |  |  |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | +23.5 | +8.7 |  |  | +2.5 |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 |  |  | +11.3 | +21.7 |  |
| [GRPO](https://arxiv.org/abs/2504.20571) | 2504.20571 | +22.5 | +10.4 |  |  | +3.7 |
| [GRPO](https://arxiv.org/abs/2504.20571) | 2504.20571 |  |  | +11.4 | +24.3 |  |
| [GRPO-format](https://arxiv.org/abs/2504.20571) | 2504.20571 | +17.8 | +1.6 |  |  | +0.8 |
| [GRPO-format](https://arxiv.org/abs/2504.20571) | 2504.20571 |  |  | +7.7 | +9.5 |  |

### Qwen2.5-7B-Base

| code | id | GPQA-D | MMLU-Pro | AIME24 | AIME25 | AMC23 | MATH500 | Minerva | Olymp |
|---|---|---|---|---|---|---|---|---|---|
| [GRPO](https://arxiv.org/abs/2509.03646) | 2509.03646 |  |  | +12.8 | +9.7 |  |  |  |  |
| [GRPO](https://arxiv.org/abs/2509.03646) | 2509.03646 |  |  |  |  | -0.2 |  |  |  |
| [GRPO](https://arxiv.org/abs/2509.03646) | 2509.03646 |  |  |  |  |  | +22.0 | +5.9 | +16.0 |
| [HICRA](https://arxiv.org/abs/2509.03646) | 2509.03646 |  |  | +15.3 | +13.1 |  |  |  |  |
| [HICRA](https://arxiv.org/abs/2509.03646) | 2509.03646 |  |  |  |  | +8.2 |  |  |  |
| [HICRA](https://arxiv.org/abs/2509.03646) | 2509.03646 |  |  |  |  |  | +24.6 | +7.7 | +20.0 |
| [Critique-GRPO](https://arxiv.org/abs/2506.03106) | 2506.03106 | +9.1 | +9.0 |  |  |  |  |  |  |
| [Dr. GRPO](https://arxiv.org/abs/2506.03106) | 2506.03106 | +10.1 | +6.6 |  |  |  |  |  |  |
| [R1-GRPO](https://arxiv.org/abs/2506.03106) | 2506.03106 | +4.5 | +5.6 |  |  |  |  |  |  |
| [RAFT](https://arxiv.org/abs/2506.03106) | 2506.03106 | -5.1 | +0.9 |  |  |  |  |  |  |
| [SFT](https://arxiv.org/abs/2506.03106) | 2506.03106 | +1.5 | +5.2 |  |  |  |  |  |  |

### Qwen3-4B

| code | id | LCBv6 | LCBv5 | AIME24 | AIME25 | HMMT25 | AMC23 | Minerva | Olymp | GSM8K |
|---|---|---|---|---|---|---|---|---|---|---|
| [GRPO](https://arxiv.org/abs/2608.13040) | 2608.13040 | +3.1 | +2.5 |  |  |  |  |  |  |  |
| [LOPD](https://arxiv.org/abs/2608.13040) | 2608.13040 | +3.8 | +2.9 |  |  |  |  |  |  |  |
| [OPSD](https://arxiv.org/abs/2608.13040) | 2608.13040 | -6.1 | -5.0 |  |  |  |  |  |  |  |
| [SDFT](https://arxiv.org/abs/2608.13040) | 2608.13040 | +2.3 | +1.1 |  |  |  |  |  |  |  |
| [SDPO](https://arxiv.org/abs/2608.13040) | 2608.13040 | -6.9 | -6.8 |  |  |  |  |  |  |  |
| [Skill-SD](https://arxiv.org/abs/2608.13040) | 2608.13040 | +0.8 | +2.1 |  |  |  |  |  |  |  |
| [ReasonMaxxer](https://arxiv.org/abs/2605.06241) | 2605.06241 |  |  | +1.3 |  |  | +25.6 |  |  |  |
| [ReasonMaxxer](https://arxiv.org/abs/2605.06241) | 2605.06241 |  |  |  |  |  |  | +22.0 | +10.3 | +42.2 |
| [GRPO](https://arxiv.org/abs/2601.18734) | 2601.18734 |  |  | +0.7 | +1.7 | +2.2 |  |  |  |  |
| [OPSD](https://arxiv.org/abs/2601.18734) | 2601.18734 |  |  | +1.5 | +1.9 | +3.9 |  |  |  |  |
| [SFT](https://arxiv.org/abs/2601.18734) | 2601.18734 |  |  | -4.7 | -4.1 | +1.2 |  |  |  |  |

### Qwen3-4B-Instruct-2507

| code | id | AIME26 | GSM8K | GPQA-D | LCBv6 |
|---|---|---|---|---|---|
| [DAPO](https://arxiv.org/abs/2606.23740) | 2606.23740 | +0.0 | -0.7 |  |  |
| [DPO](https://arxiv.org/abs/2606.23740) | 2606.23740 | -3.4 | +0.2 |  |  |
| [GRPO](https://arxiv.org/abs/2606.23740) | 2606.23740 | +3.3 | -0.3 |  |  |
| [Off-GRPO](https://arxiv.org/abs/2606.23740) | 2606.23740 | -10.0 | -6.7 |  |  |
| [SFT](https://arxiv.org/abs/2606.23740) | 2606.23740 | -10.0 | -6.4 |  |  |
| [GRPO](https://arxiv.org/abs/2608.19197) | 2608.19197 |  |  | +0.3 |  |
| [GRPO](https://arxiv.org/abs/2608.19197) | 2608.19197 |  |  |  | +0.3 |
| [RLVE](https://arxiv.org/abs/2608.19197) | 2608.19197 |  |  | +1.4 |  |
| [RLVE](https://arxiv.org/abs/2608.19197) | 2608.19197 |  |  |  | +0.8 |
| [SPADE](https://arxiv.org/abs/2608.19197) | 2608.19197 |  |  | +2.2 |  |
| [SPADE](https://arxiv.org/abs/2608.19197) | 2608.19197 |  |  |  | +2.1 |

### Qwen2.5-1.5B

| code | id | AIME24 | AMC23 | Minerva | Olymp | AIME25 | MATH500 | GSM8K | MMLU-Pro | LCBv6 |
|---|---|---|---|---|---|---|---|---|---|---|
| [GRPO](https://arxiv.org/abs/2605.06241) | 2605.06241 | +3.4 | +6.2 |  |  |  |  |  |  |  |
| [GRPO](https://arxiv.org/abs/2605.06241) | 2605.06241 |  |  | +6.3 | +9.6 |  |  | +17.2 |  |  |
| [ReasonMaxxer](https://arxiv.org/abs/2605.06241) | 2605.06241 | +2.5 | +7.5 |  |  |  |  |  |  |  |
| [ReasonMaxxer](https://arxiv.org/abs/2605.06241) | 2605.06241 |  |  | +7.0 | +7.4 |  |  | +14.9 |  |  |
| [GRPO](https://arxiv.org/abs/2505.19590) | 2505.19590 |  |  |  |  |  |  |  | +0.0 | +0.1 |
| [Intuitor](https://arxiv.org/abs/2505.19590) | 2505.19590 |  |  |  |  |  |  |  | +0.0 | +0.1 |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | +0.4 | +11.3 |  |  | -1.3 |  |  |  |  |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 |  |  | +10.3 | +16.4 |  | +40.4 |  |  |  |
| [GRPO](https://arxiv.org/abs/2504.20571) | 2504.20571 | +4.6 | +27.2 |  |  | -0.9 |  |  |  |  |
| [GRPO](https://arxiv.org/abs/2504.20571) | 2504.20571 |  |  | +15.0 | +20.0 |  | +54.0 |  |  |  |

### Qwen2.5-7B-Instruct

| code | id | MMLU-Pro | AIME24 | AIME25 | Minerva | Olymp |
|---|---|---|---|---|---|---|
| [OPD](https://arxiv.org/abs/2603.25562) | 2603.25562 |  | -3.3 | +16.7 | +5.9 | +10.2 |
| [top-K OPD](https://arxiv.org/abs/2603.25562) | 2603.25562 |  | +10.0 | +26.7 | +7.7 | +11.0 |
| [top-K OPD-MT](https://arxiv.org/abs/2603.25562) | 2603.25562 |  | +20.0 | +16.7 | +6.2 | +11.1 |
| [Chord](https://arxiv.org/abs/2508.11408) | 2508.11408 | +31.5 |  |  |  |  |
| [Chord-μ](https://arxiv.org/abs/2508.11408) | 2508.11408 | +18.6 |  |  |  |  |
| [GRPO](https://arxiv.org/abs/2508.11408) | 2508.11408 | +21.1 |  |  |  |  |
| [SFT-best](https://arxiv.org/abs/2508.11408) | 2508.11408 | +13.7 |  |  |  |  |
| [SFT-best+RL](https://arxiv.org/abs/2508.11408) | 2508.11408 | +26.6 |  |  |  |  |
| [SFT-light](https://arxiv.org/abs/2508.11408) | 2508.11408 | +3.3 |  |  |  |  |
| [SFT-light+RL](https://arxiv.org/abs/2508.11408) | 2508.11408 | +19.9 |  |  |  |  |

### Qwen3-4B-Base

| code | id | MATH500 | Olymp | HMMT25 | AIME24 | AMC23 | Minerva | GSM8K | MMLU-Pro | GPQA |
|---|---|---|---|---|---|---|---|---|---|---|
| [ConSPO](https://arxiv.org/abs/2605.12969) | 2605.12969 |  |  | +7.1 |  |  |  |  |  |  |
| [ConSPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | +32.8 | +18.5 |  |  |  |  |  |  |  |
| [DAPO](https://arxiv.org/abs/2605.12969) | 2605.12969 |  |  | +1.3 |  |  |  |  |  |  |
| [DAPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | +32.6 | +16.0 |  |  |  |  |  |  |  |
| [GRPO](https://arxiv.org/abs/2605.12969) | 2605.12969 |  |  | +1.7 |  |  |  |  |  |  |
| [GRPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | +30.8 | +16.2 |  |  |  |  |  |  |  |
| [Dr. GRPO](https://arxiv.org/abs/2505.21493) | 2505.21493 |  |  |  | +10.4 |  |  |  |  |  |
| [Dr. GRPO](https://arxiv.org/abs/2505.21493) | 2505.21493 | +0.4 | +6.3 |  |  | +7.5 | -4.8 | -0.6 | +15.8 | +19.7 |
| [VeriFree](https://arxiv.org/abs/2505.21493) | 2505.21493 |  |  |  | +11.7 |  |  |  |  |  |
| [VeriFree](https://arxiv.org/abs/2505.21493) | 2505.21493 | +1.4 | +5.3 |  |  | +15.0 | -4.0 | +14.4 | +16.3 | +17.7 |

### Qwen3-8B-Base

| code | id | AMC23 | MATH500 | Olymp | GSM8K | GPQA-D | AIME24 | Minerva | MMLU-Pro | GPQA |
|---|---|---|---|---|---|---|---|---|---|---|
| [Dr. GRPO](https://arxiv.org/abs/2505.21493) | 2505.21493 |  |  |  |  |  | +11.3 |  |  |  |
| [Dr. GRPO](https://arxiv.org/abs/2505.21493) | 2505.21493 | -7.5 | -0.8 | +0.5 | +1.7 |  |  | +0.8 | +6.1 | +5.0 |
| [VeriFree](https://arxiv.org/abs/2505.21493) | 2505.21493 |  |  |  |  |  | +18.7 |  |  |  |
| [VeriFree](https://arxiv.org/abs/2505.21493) | 2505.21493 | +2.5 | +3.8 | +8.9 | -0.1 |  |  | -7.7 | +7.4 | +5.5 |
| [DrGRPO-mid](https://arxiv.org/abs/2601.21343) | 2601.21343 | +0.0 |  |  |  |  |  |  |  |  |
| [DrGRPO-mid](https://arxiv.org/abs/2601.21343) | 2601.21343 |  | -0.0 | +0.0 | -0.0 | +0.0 |  |  |  |  |
| [SFT-raw](https://arxiv.org/abs/2601.21343) | 2601.21343 | -0.2 |  |  |  |  |  |  |  |  |
| [SFT-raw](https://arxiv.org/abs/2601.21343) | 2601.21343 |  | -0.1 | -0.1 | -0.1 | -0.1 |  |  |  |  |
| [think-SFT](https://arxiv.org/abs/2601.21343) | 2601.21343 | -0.2 |  |  |  |  |  |  |  |  |
| [think-SFT](https://arxiv.org/abs/2601.21343) | 2601.21343 |  | -0.2 | -0.1 | -0.3 | -0.0 |  |  |  |  |

### DeepSeek-R1-Distill-Qwen-7B

| code | id | AIME24 | AMC23 | AIME25 | Minerva | GSM8K | GPQA-D | MATH500 |
|---|---|---|---|---|---|---|---|---|
| [GRPO](https://arxiv.org/abs/2603.24472) | 2603.24472 | +1.3 | +1.8 |  |  |  |  |  |
| [SFT](https://arxiv.org/abs/2603.24472) | 2603.24472 | -34.6 | -32.0 |  |  |  |  | -26.7 |
| [Critique-GRPO](https://arxiv.org/abs/2602.09000) | 2602.09000 | +1.2 | +2.8 | +1.0 | +2.0 | +0.2 |  |  |
| [GRPO](https://arxiv.org/abs/2602.09000) | 2602.09000 | +0.6 | +0.0 | +0.3 | +1.3 | +0.1 |  |  |
| [Self-Verification](https://arxiv.org/abs/2602.09000) | 2602.09000 | +1.4 | +2.5 | +0.9 | +1.9 | +0.2 |  |  |
| [iGRPO](https://arxiv.org/abs/2602.09000) | 2602.09000 | +1.9 | +5.0 | +1.6 | +2.4 | +0.4 |  |  |
| [RFT](https://arxiv.org/abs/2503.02875) | 2503.02875 | +0.0 |  |  |  |  | -2.0 |  |
| [SFT](https://arxiv.org/abs/2503.02875) | 2503.02875 | -3.3 |  |  |  |  | -1.0 |  |
| [UPFT](https://arxiv.org/abs/2503.02875) | 2503.02875 | +10.0 |  |  |  |  | +2.6 |  |

### Llama-3-8B

| code | id | AMC23 | Olymp | GSM8K | GPQA-D |
|---|---|---|---|---|---|
| [DrGRPO](https://arxiv.org/abs/2601.21343) | 2601.21343 | +0.0 |  |  |  |
| [DrGRPO](https://arxiv.org/abs/2601.21343) | 2601.21343 |  | +0.0 | +0.2 | +0.0 |
| [SFT+DrGRPO](https://arxiv.org/abs/2601.21343) | 2601.21343 | +0.2 |  |  |  |
| [SFT+DrGRPO](https://arxiv.org/abs/2601.21343) | 2601.21343 |  | +0.2 | +0.8 | +0.1 |
| [SFT-raw](https://arxiv.org/abs/2601.21343) | 2601.21343 | +0.1 |  |  |  |
| [SFT-raw](https://arxiv.org/abs/2601.21343) | 2601.21343 |  | +0.0 | +0.3 | +0.0 |
| [think-SFT](https://arxiv.org/abs/2601.21343) | 2601.21343 | +0.2 |  |  |  |
| [think-SFT](https://arxiv.org/abs/2601.21343) | 2601.21343 |  | +0.1 | +0.7 | +0.1 |

### Qwen3-30B-A3B-Instruct-2507

| code | id | GPQA-D | LCBv6 |
|---|---|---|---|
| [GRPO](https://arxiv.org/abs/2608.19197) | 2608.19197 | +0.5 |  |
| [GRPO](https://arxiv.org/abs/2608.19197) | 2608.19197 |  | +0.5 |
| [GRPO-GPT-5.5](https://arxiv.org/abs/2608.19197) | 2608.19197 | +3.8 |  |
| [GRPO-GPT-5.5](https://arxiv.org/abs/2608.19197) | 2608.19197 |  | -0.6 |
| [RLVE](https://arxiv.org/abs/2608.19197) | 2608.19197 | -0.6 |  |
| [RLVE](https://arxiv.org/abs/2608.19197) | 2608.19197 |  | -0.7 |
| [SPADE](https://arxiv.org/abs/2608.19197) | 2608.19197 | +5.4 |  |
| [SPADE](https://arxiv.org/abs/2608.19197) | 2608.19197 |  | +4.1 |

### DeepSeek-R1-Distill-Llama-8B

| code | id | MATH500 | Olymp | HMMT25 |
|---|---|---|---|---|
| [ConSPO](https://arxiv.org/abs/2605.12969) | 2605.12969 |  |  | +9.1 |
| [ConSPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | +8.8 | +18.6 |  |
| [DAPO](https://arxiv.org/abs/2605.12969) | 2605.12969 |  |  | +4.4 |
| [DAPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | +6.0 | +11.2 |  |
| [GRPO](https://arxiv.org/abs/2605.12969) | 2605.12969 |  |  | +5.0 |
| [GRPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | +7.0 | +13.6 |  |

### Llama-3.1-Instruct

| code | id | AIME24 | AIME25 | AMC23 | MATH500 | Minerva | Olymp |
|---|---|---|---|---|---|---|---|
| [GRPO](https://arxiv.org/abs/2509.03646) | 2509.03646 | +4.7 | -0.1 |  |  |  |  |
| [GRPO](https://arxiv.org/abs/2509.03646) | 2509.03646 |  |  | +7.9 |  |  |  |
| [GRPO](https://arxiv.org/abs/2509.03646) | 2509.03646 |  |  |  | +2.8 | +6.3 | +6.6 |
| [HICRA](https://arxiv.org/abs/2509.03646) | 2509.03646 | +4.1 | +0.2 |  |  |  |  |
| [HICRA](https://arxiv.org/abs/2509.03646) | 2509.03646 |  |  | +10.0 |  |  |  |
| [HICRA](https://arxiv.org/abs/2509.03646) | 2509.03646 |  |  |  | +4.6 | +4.9 | +7.5 |

### OLMo-3-7B

| code | id | LCBv6 | LCBv5 |
|---|---|---|---|
| [GRPO](https://arxiv.org/abs/2608.13040) | 2608.13040 | +1.5 | +2.1 |
| [LOPD](https://arxiv.org/abs/2608.13040) | 2608.13040 | +1.5 | +6.1 |
| [OPSD](https://arxiv.org/abs/2608.13040) | 2608.13040 | +0.8 | -3.2 |
| [SDFT](https://arxiv.org/abs/2608.13040) | 2608.13040 | +0.0 | +0.4 |
| [SDPO](https://arxiv.org/abs/2608.13040) | 2608.13040 | -0.8 | +2.5 |
| [Skill-SD](https://arxiv.org/abs/2608.13040) | 2608.13040 | +0.8 | +1.8 |

### Qwen3-4B-Instruct

| code | id | AIME24 | AIME25 | AMC23 | MATH500 | Minerva | Olymp |
|---|---|---|---|---|---|---|---|
| [GRPO](https://arxiv.org/abs/2509.03646) | 2509.03646 | +5.1 | +12.3 |  |  |  |  |
| [GRPO](https://arxiv.org/abs/2509.03646) | 2509.03646 |  |  | +1.8 |  |  |  |
| [GRPO](https://arxiv.org/abs/2509.03646) | 2509.03646 |  |  |  | +1.6 | +4.8 | +0.3 |
| [HICRA](https://arxiv.org/abs/2509.03646) | 2509.03646 | +9.7 | +17.4 |  |  |  |  |
| [HICRA](https://arxiv.org/abs/2509.03646) | 2509.03646 |  |  | +3.5 |  |  |  |
| [HICRA](https://arxiv.org/abs/2509.03646) | 2509.03646 |  |  |  | +2.6 | +5.5 | -0.4 |

### Qwen2.5-7B

| code | id | AIME24 | AMC23 | Minerva | Olymp | GSM8K | GPQA-D |
|---|---|---|---|---|---|---|---|
| [GRPO](https://arxiv.org/abs/2605.06241) | 2605.06241 | +4.2 | +7.5 |  |  |  |  |
| [GRPO](https://arxiv.org/abs/2605.06241) | 2605.06241 |  |  | +0.3 | +6.4 | +10.0 |  |
| [ReasonMaxxer](https://arxiv.org/abs/2605.06241) | 2605.06241 | +6.7 | +17.5 |  |  |  |  |
| [ReasonMaxxer](https://arxiv.org/abs/2605.06241) | 2605.06241 |  |  | +7.7 | +11.7 | +16.7 |  |
| [GRPO](https://arxiv.org/abs/2510.14901) | 2510.14901 |  |  |  |  |  | +0.1 |

### Qwen3-0.6B

| code | id | AIME24 | AMC23 | Minerva | Olymp | GSM8K | MMLU-Pro |
|---|---|---|---|---|---|---|---|
| [GRPO](https://arxiv.org/abs/2605.06241) | 2605.06241 | +0.8 | -1.6 |  |  |  |  |
| [GRPO](https://arxiv.org/abs/2605.06241) | 2605.06241 |  |  | +0.0 | +2.0 | +1.4 |  |
| [ReasonMaxxer](https://arxiv.org/abs/2605.06241) | 2605.06241 | +1.7 | +12.8 |  |  |  |  |
| [ReasonMaxxer](https://arxiv.org/abs/2605.06241) | 2605.06241 |  |  | +3.7 | +5.3 | +16.7 |  |
| [LCF](https://arxiv.org/abs/2605.22863) | 2605.22863 |  |  |  |  |  | +6.7 |

### Qwen3-1.7B

| code | id | AIME24 | AIME25 | HMMT25 | GPQA |
|---|---|---|---|---|---|
| [GRPO](https://arxiv.org/abs/2604.20659) | 2604.20659 |  |  |  | +18.4 |
| [GRPO-VPS](https://arxiv.org/abs/2604.20659) | 2604.20659 |  |  |  | +20.0 |
| [GRPO](https://arxiv.org/abs/2601.18734) | 2601.18734 | -0.4 | +1.6 | +0.6 |  |
| [OPSD](https://arxiv.org/abs/2601.18734) | 2601.18734 | +5.7 | +7.2 | +6.1 |  |
| [SFT](https://arxiv.org/abs/2601.18734) | 2601.18734 | -3.1 | -0.4 | -0.4 |  |

### Qwen3-1.7B-Base

| code | id | AIME24 | AIME25 | Minerva | Olymp | GSM8K |
|---|---|---|---|---|---|---|
| [OPD-top1](https://arxiv.org/abs/2606.06021) | 2606.06021 | +7.9 | +6.1 |  |  |  |
| [OPD-top16](https://arxiv.org/abs/2606.06021) | 2606.06021 | +6.1 | +3.8 |  |  |  |
| [OPRD-Bridge](https://arxiv.org/abs/2606.06021) | 2606.06021 | +4.4 | +3.6 |  |  |  |
| [Dr. GRPO](https://arxiv.org/abs/2505.21493) | 2505.21493 |  |  | +11.0 | +6.5 | +10.3 |
| [VeriFree](https://arxiv.org/abs/2505.21493) | 2505.21493 |  |  | +1.5 | +6.5 | +4.8 |

### Llama-3.1-8B-Instruct

| code | id | AIME24 | GPQA-D |
|---|---|---|---|
| [RFT](https://arxiv.org/abs/2503.02875) | 2503.02875 | +3.4 | +0.5 |
| [SFT](https://arxiv.org/abs/2503.02875) | 2503.02875 | +0.0 | +0.0 |
| [UPFT](https://arxiv.org/abs/2503.02875) | 2503.02875 | +3.4 | +0.5 |
| [V-STaR](https://arxiv.org/abs/2503.02875) | 2503.02875 | +3.4 | +0.0 |

### Mistral-7B

| code | id | AIME24 | AMC23 | Minerva | Olymp | GSM8K |
|---|---|---|---|---|---|---|
| [GRPO](https://arxiv.org/abs/2605.06241) | 2605.06241 | +0.4 | +0.0 |  |  |  |
| [GRPO](https://arxiv.org/abs/2605.06241) | 2605.06241 |  |  | -3.1 | +0.0 | +0.6 |
| [ReasonMaxxer](https://arxiv.org/abs/2605.06241) | 2605.06241 | +5.9 | +0.5 |  |  |  |
| [ReasonMaxxer](https://arxiv.org/abs/2605.06241) | 2605.06241 |  |  | +1.3 | +0.0 | +0.2 |

### Nemotron-H-8B-Base-8K

| code | id | AIME24 | AIME25 | AMC23 | Minerva | GSM8K |
|---|---|---|---|---|---|---|
| [Critique-GRPO](https://arxiv.org/abs/2602.09000) | 2602.09000 | +0.5 | +2.2 | +3.6 | +13.9 | +47.4 |
| [GRPO](https://arxiv.org/abs/2602.09000) | 2602.09000 | +0.4 | +1.6 | +1.9 | +12.0 | +40.9 |
| [Self-Verification](https://arxiv.org/abs/2602.09000) | 2602.09000 | +0.6 | +2.3 | +3.3 | +13.5 | +45.2 |
| [iGRPO](https://arxiv.org/abs/2602.09000) | 2602.09000 | +0.9 | +3.0 | +5.5 | +15.1 | +50.2 |

### Qwen2.5-32B

| code | id | AIME24 | AMC23 | Minerva | Olymp | GSM8K |
|---|---|---|---|---|---|---|
| [GRPO](https://arxiv.org/abs/2605.06241) | 2605.06241 | +5.0 | +6.3 |  |  |  |
| [GRPO](https://arxiv.org/abs/2605.06241) | 2605.06241 |  |  | +3.7 | +5.2 | +4.0 |
| [ReasonMaxxer](https://arxiv.org/abs/2605.06241) | 2605.06241 | +10.0 | +13.8 |  |  |  |
| [ReasonMaxxer](https://arxiv.org/abs/2605.06241) | 2605.06241 |  |  | +8.5 | +8.1 | +2.9 |

### Qwen2.5-Math-1.5B-Instruct

| code | id | AIME24 | AIME25 | AMC23 | MATH500 | Minerva | Olymp |
|---|---|---|---|---|---|---|---|
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | +1.3 | +5.4 | +0.3 |  |  |  |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 |  |  |  | +1.2 | +1.9 | -0.6 |
| [GRPO](https://arxiv.org/abs/2504.20571) | 2504.20571 | +2.5 | +5.4 | +2.2 |  |  |  |
| [GRPO](https://arxiv.org/abs/2504.20571) | 2504.20571 |  |  |  | +2.2 | +2.2 | +1.1 |

### Qwen2.5-Math-7B-Instruct

| code | id | AIME24 | GPQA-D |
|---|---|---|---|
| [RFT](https://arxiv.org/abs/2503.02875) | 2503.02875 | +3.3 | +0.0 |
| [SFT](https://arxiv.org/abs/2503.02875) | 2503.02875 | +0.0 | +0.0 |
| [UPFT](https://arxiv.org/abs/2503.02875) | 2503.02875 | +9.9 | +0.0 |
| [V-STaR](https://arxiv.org/abs/2503.02875) | 2503.02875 | +3.3 | +0.5 |

### Encoder-Decoder Gemma 2

| code | id | MATH500 | GSM8K | MMLU-Pro | GPQA |
|---|---|---|---|---|---|
| [PrefixLM](https://arxiv.org/abs/2504.06225) | 2504.06225 | +1.4 |  |  | +5.8 |
| [PrefixLM](https://arxiv.org/abs/2504.06225) | 2504.06225 |  | +4.3 |  |  |
| [PrefixLM](https://arxiv.org/abs/2504.06225) | 2504.06225 |  |  | +5.8 |  |

### Llama-3.2-3B

| code | id | AIME24 | AMC23 | Minerva | Olymp |
|---|---|---|---|---|---|
| [DFT](https://arxiv.org/abs/2508.05629) | 2508.05629 | +0.4 | +2.4 | +1.5 | +1.9 |
| [SFT](https://arxiv.org/abs/2508.05629) | 2508.05629 | -0.4 | +1.6 | +1.0 | +1.1 |
| [Dr. GRPO](https://arxiv.org/abs/2503.20783) | 2503.20783 | +3.3 | +4.8 | +4.7 | +0.9 |

### Qwen2.5-32B-Instruct

| code | id | AIME24 | GPQA-D |
|---|---|---|---|
| [SFT](https://arxiv.org/abs/2507.12856) | 2507.12856 | +30.0 | +11.6 |
| [iw-SFT](https://arxiv.org/abs/2507.12856) | 2507.12856 | +40.0 | +15.1 |
| [iw-SFT-step](https://arxiv.org/abs/2507.12856) | 2507.12856 | +36.6 | +11.6 |

### Qwen2.5-3B

| code | id | LCBv6 |
|---|---|---|
| [GRPO](https://arxiv.org/abs/2505.19590) | 2505.19590 | -0.0 |
| [Intuitor](https://arxiv.org/abs/2505.19590) | 2505.19590 | +0.1 |
| [Intuitor-Code](https://arxiv.org/abs/2505.19590) | 2505.19590 | +0.1 |

### Other checkpoints (1)

| code | id | DeepSeekMath-7B · AIME24 | DeepSeekMath-7B · AMC23 | DeepSeekMath-7B · Minerva | DeepSeekMath-7B · Olymp | Gemma-2-2B-it · AIME24 | Gemma-2-2B-it · AMC23 | Gemma-2-2B-it · Olymp | Llama-3 · GSM8K | Llama-3.1-8B-Base · AIME24 | Llama-3.1-8B-Base · AMC23 | Llama-3.1-8B-Base · Minerva | Llama-3.1-8B-Base · Olymp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [GRPO](https://arxiv.org/abs/2604.20659) | 2604.20659 |  |  |  |  | +0.0 | +3.7 | +3.1 |  |  |  |  |  |
| [GRPO-VPS](https://arxiv.org/abs/2604.20659) | 2604.20659 |  |  |  |  | +0.8 | +4.3 | +3.4 |  |  |  |  |  |
| [DFT](https://arxiv.org/abs/2508.05629) | 2508.05629 | +1.0 | +13.3 | +14.6 | +13.3 |  |  |  |  |  |  |  |  |
| [SFT](https://arxiv.org/abs/2508.05629) | 2508.05629 | +0.2 | +5.3 | +5.1 | +4.6 |  |  |  |  |  |  |  |  |
| [DFT](https://arxiv.org/abs/2508.05629) | 2508.05629 |  |  |  |  |  |  |  |  | +0.2 | +11.0 | +7.3 | +6.0 |
| [SFT](https://arxiv.org/abs/2508.05629) | 2508.05629 |  |  |  |  |  |  |  |  | -0.2 | +4.2 | +4.8 | +2.9 |
| [SDFT](https://arxiv.org/abs/2402.13669) | 2402.13669 |  |  |  |  |  |  |  | -2.1 |  |  |  |  |
| [SFT](https://arxiv.org/abs/2402.13669) | 2402.13669 |  |  |  |  |  |  |  | -3.8 |  |  |  |  |

### Other checkpoints (2)

| code | id | OLMo-2-1124-7B-SFT · LCBv6 | OpenMath-Nemotron-14B · AIME24 | OpenMath-Nemotron-14B · AIME25 | OpenMath-Nemotron-7B · AIME24 | OpenMath-Nemotron-7B · AIME25 | OpenMath-Nemotron-7B · AMC23 | OpenMath-Nemotron-7B · GSM8K | OpenMath-Nemotron-7B · Minerva | Qwen2.5-Math · AIME24 | Qwen2.5-Math · AMC23 | Qwen2.5-Math · Minerva | Qwen2.5-Math · Olymp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [GRPO](https://arxiv.org/abs/2602.09000) | 2602.09000 |  | +1.5 | +3.4 |  |  |  |  |  |  |  |  |  |
| [iGRPO](https://arxiv.org/abs/2602.09000) | 2602.09000 |  | +3.4 | +4.4 |  |  |  |  |  |  |  |  |  |
| [GRPO](https://arxiv.org/abs/2602.09000) | 2602.09000 |  |  |  | +0.3 | +0.1 | +0.0 | +0.1 | +0.5 |  |  |  |  |
| [iGRPO](https://arxiv.org/abs/2602.09000) | 2602.09000 |  |  |  | +1.5 | +1.3 | +2.5 | +0.2 | +1.5 |  |  |  |  |
| [DFT](https://arxiv.org/abs/2508.05629) | 2508.05629 |  |  |  |  |  |  |  |  | +1.9 | +17.0 | +15.8 | +16.7 |
| [SFT](https://arxiv.org/abs/2508.05629) | 2508.05629 |  |  |  |  |  |  |  |  | -4.2 | -1.9 | +2.3 | +1.8 |
| [GRPO](https://arxiv.org/abs/2505.19590) | 2505.19590 | +0.0 |  |  |  |  |  |  |  |  |  |  |  |
| [Intuitor](https://arxiv.org/abs/2505.19590) | 2505.19590 | +0.0 |  |  |  |  |  |  |  |  |  |  |  |

### Other checkpoints (3)

| code | id | Qwen3-14B-Base · GPQA | Qwen3-14B-Base · LCBv6 | Deepseek-R1-Distill-Qwen14B · MMLU-Pro | Llama-3.2-3B-FineMath · AIME24 | Llama-3.2-3B-FineMath · AMC23 | Llama-3.2-3B-FineMath · Minerva | Llama-3.2-3B-FineMath · Olymp | Llama-3.2-3B-NuminaQA · AIME24 | Llama-3.2-3B-NuminaQA · AMC23 | Llama-3.2-3B-NuminaQA · Minerva | Llama-3.2-3B-NuminaQA · Olymp | OpenReasoning-Nemotron-7B · AIME24 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [GRPO](https://arxiv.org/abs/2605.22074) | 2605.22074 | -2.0 | +4.3 |  |  |  |  |  |  |  |  |  |  |
| [SCRL](https://arxiv.org/abs/2605.22074) | 2605.22074 | +2.5 | +4.8 |  |  |  |  |  |  |  |  |  |  |
| [iGRPO](https://arxiv.org/abs/2602.09000) | 2602.09000 |  |  |  |  |  |  |  |  |  |  |  | +1.5 |
| [CPT+Dr. GRPO](https://arxiv.org/abs/2503.20783) | 2503.20783 |  |  |  |  |  |  |  | +6.7 | +18.1 | +14.3 | +14.6 |  |
| [Dr. GRPO](https://arxiv.org/abs/2503.20783) | 2503.20783 |  |  |  | +3.3 | +7.2 | +7.0 | +6.8 |  |  |  |  |  |
| [RPT](https://arxiv.org/abs/2506.08007) | 2506.08007 |  |  | +2.2 |  |  |  |  |  |  |  |  |  |

### Other checkpoints (4)

| code | id | OpenReasoning-Nemotron-7B · AIME25 | OpenReasoning-Nemotron-7B · GPQA | OpenReasoning-Nemotron-7B · MMLU-Pro | Phi-3.5-mini-instruct · GPQA-D | Qwen2.5-0.5B-Instruct · MMLU-Pro | Qwen2.5-1.5B-Instruct · AIME25 | Qwen2.5-1.5B-Instruct · AMC23 | Qwen2.5-1.5B-Instruct · GPQA | Qwen2.5-1.5B-Instruct · MATH500 | Qwen2.5-1.5B-Instruct · Olymp | Qwen3-14B · LCBv6 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [iGRPO](https://arxiv.org/abs/2602.09000) | 2602.09000 | +1.8 | +1.8 | +0.9 |  |  |  |  |  |  |  |  |
| [SR-GRPO](https://arxiv.org/abs/2512.02807) | 2512.02807 |  |  |  |  |  | +10.0 | +2.5 | +2.2 | +4.4 | +0.9 |  |
| [GRPO](https://arxiv.org/abs/2510.14901) | 2510.14901 |  |  |  | +0.1 |  |  |  |  |  |  |  |
| [Intuitor](https://arxiv.org/abs/2505.19590) | 2505.19590 |  |  |  |  |  |  |  |  |  |  | -0.0 |
| [LCF](https://arxiv.org/abs/2605.22863) | 2605.22863 |  |  |  |  | +6.7 |  |  |  |  |  |  |

## Gain over GRPO

Cell = method − the paper's vanilla GRPO, or the nearest vanilla RLVR baseline when GRPO is absent (`vs` column). A trailing `*` means the reference is not vanilla GRPO (Dr. GRPO, DAPO, PPO, RLOO, REINFORCE++). The reference method itself is omitted. Blank if no RLVR baseline is reported on that bench. Same-table, same-metric only.

### Qwen2.5-Math-7B

| code | id | vs | AMC23 | Minerva | Olymp | AIME24 | MMLU-Pro | LCB | AIME25 | MATH500 | GSM8K | GPQA-D |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [ReasonMaxxer](https://arxiv.org/abs/2605.06241) | 2605.06241 | GRPO | -6.6 |  |  | +0.4 |  |  |  |  |  |  |
| [ReasonMaxxer](https://arxiv.org/abs/2605.06241) | 2605.06241 | GRPO |  | +9.5 | +2.1 |  |  |  |  |  | -1.1 |  |
| [GRPO-VPS](https://arxiv.org/abs/2604.20659) | 2604.20659 | GRPO | +2.3 |  | +0.4 | +1.7 |  |  |  |  |  |  |
| [CISPO](https://arxiv.org/abs/2604.08690) | 2604.08690 | GRPO |  |  |  |  | +6.5 | +2.8 |  |  |  |  |
| [Critique-GRPO](https://arxiv.org/abs/2604.08690) | 2604.08690 | GRPO |  |  |  |  | +1.5 | +0.6 |  |  |  |  |
| [DAPO](https://arxiv.org/abs/2604.08690) | 2604.08690 | GRPO |  |  |  |  | +5.8 | +2.4 |  |  |  |  |
| [GSPO](https://arxiv.org/abs/2604.08690) | 2604.08690 | GRPO |  |  |  |  | +3.9 | +1.6 |  |  |  |  |
| [PRIME](https://arxiv.org/abs/2604.08690) | 2604.08690 | GRPO |  |  |  |  | +3.7 | +4.3 |  |  |  |  |
| [SAPO](https://arxiv.org/abs/2604.08690) | 2604.08690 | GRPO |  |  |  |  | +7.4 | +1.9 |  |  |  |  |
| [SKPO](https://arxiv.org/abs/2604.08690) | 2604.08690 | GRPO |  |  |  |  | +7.1 | +5.0 |  |  |  |  |
| [SPO](https://arxiv.org/abs/2604.08690) | 2604.08690 | GRPO |  |  |  |  | +2.8 | +1.1 |  |  |  |  |
| [2-GRPO](https://arxiv.org/abs/2510.00977) | 2510.00977 | GRPO | +2.8 | +0.3 | +0.4 |  |  |  | -0.4 |  |  |  |
| [2-GRPO+RS](https://arxiv.org/abs/2510.00977) | 2510.00977 | GRPO | -0.1 | +2.1 | -0.6 |  |  |  | -1.6 |  |  |  |
| [2-GRPO+RS-DAPO](https://arxiv.org/abs/2510.00977) | 2510.00977 | GRPO | -0.8 | -0.5 | -0.5 |  |  |  | +2.4 |  |  |  |
| [2-GRPO-DAPO](https://arxiv.org/abs/2510.00977) | 2510.00977 | GRPO | -4.8 | -2.5 | +1.0 |  |  |  | +0.3 |  |  |  |
| [Critique-GRPO](https://arxiv.org/abs/2506.03106) | 2506.03106 | GRPO |  |  |  |  | +9.3 |  |  |  |  | +17.2 |
| [GRPO-format](https://arxiv.org/abs/2506.10947) | 2506.10947 | GRPO |  |  |  | -5.0 |  |  |  |  |  |  |
| [GRPO-incorrect](https://arxiv.org/abs/2506.10947) | 2506.10947 | GRPO |  |  |  | -5.1 |  |  |  |  |  |  |
| [GRPO-incorrect](https://arxiv.org/abs/2506.10947) | 2506.10947 | GRPO |  |  |  |  |  |  |  | -5.0 |  |  |
| [GRPO-random](https://arxiv.org/abs/2506.10947) | 2506.10947 | GRPO |  |  |  | -5.1 |  |  |  |  |  |  |
| [GRPO-random](https://arxiv.org/abs/2506.10947) | 2506.10947 | GRPO |  |  |  |  |  |  |  | -7.7 |  |  |
| [EM-FT](https://arxiv.org/abs/2505.15134) | 2505.15134 | GRPO | -4.8 | +8.1 | -1.5 | -6.7 |  |  |  |  |  |  |
| [EM-RL](https://arxiv.org/abs/2505.15134) | 2505.15134 | GRPO | +1.2 | +5.9 |  | -2.2 |  |  |  |  |  |  |
| [EM-RL-sequence](https://arxiv.org/abs/2505.15134) | 2505.15134 | GRPO | -3.6 | +5.9 | -0.3 |  |  |  |  |  |  |  |
| [RLOO](https://arxiv.org/abs/2505.15134) | 2505.15134 | GRPO | +1.2 | +6.2 | -1.7 | +2.2 |  |  |  |  |  |  |
| [SC-RL](https://arxiv.org/abs/2505.15134) | 2505.15134 | GRPO | -4.8 | +1.1 | +0.8 | -5.5 |  |  |  |  |  |  |
| [SFT](https://arxiv.org/abs/2505.15134) | 2505.15134 | GRPO | -26.4 | -7.4 | -13.5 | -11.1 |  |  |  |  |  |  |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | GRPO | -2.2 |  |  | -2.0 |  |  | -3.8 |  |  |  |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | GRPO |  | -5.9 | -2.5 |  |  |  |  |  |  |  |
| [GRPO-format](https://arxiv.org/abs/2504.20571) | 2504.20571 | GRPO | -8.1 |  |  | -1.6 |  |  | -7.9 |  |  |  |
| [GRPO-format](https://arxiv.org/abs/2504.20571) | 2504.20571 | GRPO |  | -9.5 | -11.2 |  |  |  |  |  |  |  |

### Qwen3-8B

| code | id | vs | AIME25 | AIME24 | GPQA-D | MMLU-Pro | HMMT25 | LCBv6 |
|---|---|---|---|---|---|---|---|---|
| [DAPO](https://arxiv.org/abs/2606.18810) | 2606.18810 | GRPO | +3.8 | +2.1 |  |  |  |  |
| [OPSD](https://arxiv.org/abs/2606.18810) | 2606.18810 | GRPO | -12.1 | -7.9 |  |  |  |  |
| [REINFORCE++](https://arxiv.org/abs/2606.18810) | 2606.18810 | GRPO | -17.9 | -23.3 |  |  |  |  |
| [SC-GRPO](https://arxiv.org/abs/2606.18810) | 2606.18810 | GRPO | +7.9 | +10.0 |  |  |  |  |
| [SDPO](https://arxiv.org/abs/2601.20802) | 2601.20802 | GRPO |  |  |  | +0.6 |  |  |
| [SFT](https://arxiv.org/abs/2601.20802) | 2601.20802 | GRPO |  |  |  | -0.4 |  |  |
| [OPSD](https://arxiv.org/abs/2601.18734) | 2601.18734 | GRPO | +1.9 | +1.4 |  |  | -0.9 |  |
| [SFT](https://arxiv.org/abs/2601.18734) | 2601.18734 | GRPO | -4.7 | -4.1 |  |  | -3.8 |  |
| [SPO](https://arxiv.org/abs/2509.13232) | 2509.13232 | GRPO | +4.4 | +0.7 |  |  | +3.3 |  |
| [GEPA](https://arxiv.org/abs/2507.19457) | 2507.19457 | GRPO | -6.0 |  |  |  |  |  |
| [Critique-GRPO](https://arxiv.org/abs/2506.03106) | 2506.03106 | GRPO |  |  | +7.6 | +0.5 |  |  |
| [Dr. GRPO](https://arxiv.org/abs/2506.03106) | 2506.03106 | GRPO |  |  | +4.0 | +0.5 |  |  |
| [RAFT](https://arxiv.org/abs/2506.03106) | 2506.03106 | GRPO |  |  | -2.5 | -1.0 |  |  |
| [SFT](https://arxiv.org/abs/2506.03106) | 2506.03106 | GRPO |  |  | -2.0 | -3.2 |  |  |
| [RLVE](https://arxiv.org/abs/2608.19197) | 2608.19197 | GRPO |  |  | +1.7 |  |  |  |
| [RLVE](https://arxiv.org/abs/2608.19197) | 2608.19197 | GRPO |  |  |  |  |  | +0.6 |
| [SPADE](https://arxiv.org/abs/2608.19197) | 2608.19197 | GRPO |  |  | +3.0 |  |  |  |
| [SPADE](https://arxiv.org/abs/2608.19197) | 2608.19197 | GRPO |  |  |  |  |  | +2.6 |

### Llama-3.2-3B-Instruct

| code | id | vs | MMLU-Pro | LCB | Olymp | AIME24 | MATH500 | AIME25 | AMC23 | Minerva | GPQA-D | LCBv6 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [ConSPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | GRPO |  |  | +1.7 |  | +4.6 |  |  |  |  |  |
| [DAPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | GRPO |  |  | -0.3 |  |  |  |  |  |  |  |
| [CISPO](https://arxiv.org/abs/2604.08690) | 2604.08690 | GRPO | -0.3 | -1.0 |  |  |  |  |  |  |  |  |
| [DAPO](https://arxiv.org/abs/2604.08690) | 2604.08690 | GRPO |  | -0.4 |  |  |  |  |  |  |  |  |
| [GSPO](https://arxiv.org/abs/2604.08690) | 2604.08690 | GRPO | +0.3 | +0.7 |  |  |  |  |  |  |  |  |
| [PRIME](https://arxiv.org/abs/2604.08690) | 2604.08690 | GRPO | -0.1 | +0.1 |  |  |  |  |  |  |  |  |
| [SAPO](https://arxiv.org/abs/2604.08690) | 2604.08690 | GRPO | +0.2 | -0.5 |  |  |  |  |  |  |  |  |
| [SKPO](https://arxiv.org/abs/2604.08690) | 2604.08690 | GRPO | -0.1 | +1.0 |  |  |  |  |  |  |  |  |
| [SPO](https://arxiv.org/abs/2604.08690) | 2604.08690 | GRPO | -0.4 | -0.2 |  |  |  |  |  |  |  |  |
| [E2H-C](https://arxiv.org/abs/2506.06632) | 2506.06632 | GRPO |  |  | +2.3 | +6.7 |  |  |  |  |  |  |
| [E2H-G](https://arxiv.org/abs/2506.06632) | 2506.06632 | GRPO |  |  | +1.6 | +3.3 |  |  |  |  |  |  |
| [Self-Evolve](https://arxiv.org/abs/2506.06632) | 2506.06632 | GRPO |  |  | +1.6 | +3.3 |  |  |  |  |  |  |
| [Critique-GRPO](https://arxiv.org/abs/2506.03106) | 2506.03106 | GRPO | +3.1 |  |  |  |  |  |  |  | +7.6 |  |
| [Intuitor](https://arxiv.org/abs/2505.19590) | 2505.19590 | GRPO |  |  |  |  |  |  |  |  |  | +0.0 |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | GRPO |  |  |  | -3.3 |  | +0.4 | -2.5 |  |  |  |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | GRPO |  |  | +0.6 |  | +2.6 |  |  | -3.0 |  |  |

### DeepSeek-R1-Distill-Qwen-1.5B

| code | id | vs | Olymp | HMMT25 | AIME24 | AMC23 | Minerva | AIME25 | MATH500 | GSM8K |
|---|---|---|---|---|---|---|---|---|---|---|
| [ConSPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | GRPO |  | +3.2 |  |  |  |  |  |  |
| [ConSPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | GRPO | +4.6 |  |  |  |  |  |  |  |
| [ConSPO-DAPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | GRPO |  | +1.1 |  |  |  |  |  |  |
| [ConSPO-DAPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | GRPO | +7.4 |  |  |  |  |  |  |  |
| [DAPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | GRPO |  | +1.8 |  |  |  |  |  |  |
| [DAPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | GRPO | +3.7 |  |  |  |  |  |  |  |
| [DAPO-DAPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | GRPO |  | -0.3 |  |  |  |  |  |  |
| [DAPO-DAPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | GRPO | +4.9 |  |  |  |  |  |  |  |
| [ReasonMaxxer](https://arxiv.org/abs/2605.06241) | 2605.06241 | GRPO |  |  | +4.2 | -2.8 |  |  |  |  |
| [ReasonMaxxer](https://arxiv.org/abs/2605.06241) | 2605.06241 | GRPO | +10.5 |  |  |  | +5.1 |  |  | +3.2 |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | GRPO |  |  | -1.7 | -4.0 |  | -3.7 |  |  |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | GRPO | -2.3 |  |  |  | -1.2 |  | -0.6 |  |

### Qwen2.5-Math-1.5B

| code | id | vs | AIME24 | AMC23 | Olymp | Minerva | AIME25 |
|---|---|---|---|---|---|---|---|
| [GRPO-VPS](https://arxiv.org/abs/2604.20659) | 2604.20659 | GRPO | -3.3 | +8.1 | +2.1 |  |  |
| [DFT](https://arxiv.org/abs/2508.05629) | 2508.05629 | GRPO | -1.5 | -3.1 | -1.5 | +2.0 |  |
| [DFT-OpenR1](https://arxiv.org/abs/2508.05629) | 2508.05629 | GRPO | +1.4 | +7.7 | +4.9 | +8.1 |  |
| [DFT-offline](https://arxiv.org/abs/2508.05629) | 2508.05629 | GRPO | -0.4 | +7.2 | +2.3 | +6.2 |  |
| [PPO](https://arxiv.org/abs/2508.05629) | 2508.05629 | GRPO | -0.8 | -3.3 | -2.3 | -3.5 |  |
| [RFT](https://arxiv.org/abs/2508.05629) | 2508.05629 | GRPO | -4.0 | -10.5 | -6.3 | -4.7 |  |
| [SFT](https://arxiv.org/abs/2508.05629) | 2508.05629 | GRPO | -6.5 | -22.5 | -16.0 | -5.9 |  |
| [SFT-OpenR1](https://arxiv.org/abs/2508.05629) | 2508.05629 | GRPO | -4.2 | -5.8 | -4.4 | +1.4 |  |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | GRPO | -1.7 | +1.0 |  |  | -1.2 |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | GRPO |  |  | -0.1 | -2.6 |  |
| [GRPO-format](https://arxiv.org/abs/2504.20571) | 2504.20571 | GRPO | -8.8 | -4.7 |  |  | -2.9 |
| [GRPO-format](https://arxiv.org/abs/2504.20571) | 2504.20571 | GRPO |  |  | -3.7 | -14.8 |  |

### Qwen3-4B-Base

| code | id | vs | AIME24 | AIME25 | HMMT | MATH500 | Olymp | HMMT25 | AMC23 | Minerva | GSM8K | MMLU-Pro | GPQA |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [ConSPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | GRPO |  |  |  |  |  | +5.4 |  |  |  |  |  |
| [ConSPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | GRPO |  |  |  | +2.0 | +2.3 |  |  |  |  |  |  |
| [DAPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | GRPO |  |  |  |  |  | -0.4 |  |  |  |  |  |
| [DAPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | GRPO |  |  |  | +1.8 | -0.2 |  |  |  |  |  |  |
| [CISPO](https://arxiv.org/abs/2512.00499) | 2512.00499 | DAPO | +3.0* | -2.8* | +0.7* |  |  |  |  |  |  |  |  |
| [ESPO](https://arxiv.org/abs/2512.00499) | 2512.00499 | DAPO | +1.5* | -1.4* | +0.3* |  |  |  |  |  |  |  |  |
| [GMPO](https://arxiv.org/abs/2512.00499) | 2512.00499 | DAPO | -0.9* | -2.8* | -1.3* |  |  |  |  |  |  |  |  |
| [GSPO](https://arxiv.org/abs/2512.00499) | 2512.00499 | DAPO | -2.7* | -4.0* | -1.8* |  |  |  |  |  |  |  |  |
| [VeriFree](https://arxiv.org/abs/2505.21493) | 2505.21493 | Dr. GRPO | +1.3* |  |  |  |  |  |  |  |  |  |  |
| [VeriFree](https://arxiv.org/abs/2505.21493) | 2505.21493 | Dr. GRPO |  |  |  | +1.0* | -1.0* |  | +7.5* | +0.8* | +15.0* | +0.5* | -2.0* |

### Qwen3-4B-Instruct-2507

| code | id | vs | AIME26 | GSM8K | GPQA-D | LCBv6 |
|---|---|---|---|---|---|---|
| [DAPO](https://arxiv.org/abs/2606.23740) | 2606.23740 | GRPO | -3.3 | -0.4 |  |  |
| [DPO](https://arxiv.org/abs/2606.23740) | 2606.23740 | GRPO | -6.7 | +0.5 |  |  |
| [Off-GRPO](https://arxiv.org/abs/2606.23740) | 2606.23740 | GRPO | -13.3 | -6.4 |  |  |
| [SFT](https://arxiv.org/abs/2606.23740) | 2606.23740 | GRPO | -13.3 | -6.1 |  |  |
| [RLVE](https://arxiv.org/abs/2608.19197) | 2608.19197 | GRPO |  |  | +1.1 |  |
| [RLVE](https://arxiv.org/abs/2608.19197) | 2608.19197 | GRPO |  |  |  | +0.5 |
| [SPADE](https://arxiv.org/abs/2608.19197) | 2608.19197 | GRPO |  |  | +1.9 |  |
| [SPADE](https://arxiv.org/abs/2608.19197) | 2608.19197 | GRPO |  |  |  | +1.8 |

### Qwen2.5-7B-Base

| code | id | vs | GPQA-D | MMLU-Pro | AIME24 | AIME25 | AMC23 | MATH500 | Minerva | Olymp |
|---|---|---|---|---|---|---|---|---|---|---|
| [HICRA](https://arxiv.org/abs/2509.03646) | 2509.03646 | GRPO |  |  | +2.5 | +3.4 |  |  |  |  |
| [HICRA](https://arxiv.org/abs/2509.03646) | 2509.03646 | GRPO |  |  |  |  | +8.4 |  |  |  |
| [HICRA](https://arxiv.org/abs/2509.03646) | 2509.03646 | GRPO |  |  |  |  |  | +2.6 | +1.8 | +4.0 |
| [Critique-GRPO](https://arxiv.org/abs/2506.03106) | 2506.03106 | GRPO | +4.6 | +3.5 |  |  |  |  |  |  |
| [Dr. GRPO](https://arxiv.org/abs/2506.03106) | 2506.03106 | GRPO | +5.6 | +1.0 |  |  |  |  |  |  |
| [RAFT](https://arxiv.org/abs/2506.03106) | 2506.03106 | GRPO | -9.6 | -4.7 |  |  |  |  |  |  |
| [SFT](https://arxiv.org/abs/2506.03106) | 2506.03106 | GRPO | -3.0 | -0.3 |  |  |  |  |  |  |

### Qwen3-4B

| code | id | vs | LCBv6 | LCBv5 | AIME24 | AIME25 | HMMT25 |
|---|---|---|---|---|---|---|---|
| [LOPD](https://arxiv.org/abs/2608.13040) | 2608.13040 | GRPO | +0.8 | +0.4 |  |  |  |
| [OPSD](https://arxiv.org/abs/2608.13040) | 2608.13040 | GRPO | -9.2 | -7.5 |  |  |  |
| [SDFT](https://arxiv.org/abs/2608.13040) | 2608.13040 | GRPO | -0.8 | -1.4 |  |  |  |
| [SDPO](https://arxiv.org/abs/2608.13040) | 2608.13040 | GRPO | -9.9 | -9.3 |  |  |  |
| [Skill-SD](https://arxiv.org/abs/2608.13040) | 2608.13040 | GRPO | -2.3 | -0.4 |  |  |  |
| [OPSD](https://arxiv.org/abs/2601.18734) | 2601.18734 | GRPO |  |  | +0.8 | +0.2 | +1.7 |
| [SFT](https://arxiv.org/abs/2601.18734) | 2601.18734 | GRPO |  |  | -5.4 | -5.8 | -1.0 |

### Llama-3-8B

| code | id | vs | AMC23 | Olymp | GSM8K | GPQA-D |
|---|---|---|---|---|---|---|
| [SFT+DrGRPO](https://arxiv.org/abs/2601.21343) | 2601.21343 | Dr. GRPO | +0.2* |  |  |  |
| [SFT+DrGRPO](https://arxiv.org/abs/2601.21343) | 2601.21343 | Dr. GRPO |  | +0.1* | +0.6* | +0.1* |
| [SFT-raw](https://arxiv.org/abs/2601.21343) | 2601.21343 | Dr. GRPO | +0.0* |  |  |  |
| [SFT-raw](https://arxiv.org/abs/2601.21343) | 2601.21343 | Dr. GRPO |  | +0.0* | +0.1* | -0.0* |
| [think-SFT](https://arxiv.org/abs/2601.21343) | 2601.21343 | Dr. GRPO | +0.2* |  |  |  |
| [think-SFT](https://arxiv.org/abs/2601.21343) | 2601.21343 | Dr. GRPO |  | +0.1* | +0.5* | +0.1* |

### Qwen2.5-7B-Instruct

| code | id | vs | MMLU-Pro |
|---|---|---|---|
| [Chord](https://arxiv.org/abs/2508.11408) | 2508.11408 | GRPO | +10.4 |
| [Chord-μ](https://arxiv.org/abs/2508.11408) | 2508.11408 | GRPO | -2.5 |
| [SFT-best](https://arxiv.org/abs/2508.11408) | 2508.11408 | GRPO | -7.4 |
| [SFT-best+RL](https://arxiv.org/abs/2508.11408) | 2508.11408 | GRPO | +5.5 |
| [SFT-light](https://arxiv.org/abs/2508.11408) | 2508.11408 | GRPO | -17.8 |
| [SFT-light+RL](https://arxiv.org/abs/2508.11408) | 2508.11408 | GRPO | -1.2 |

### Qwen3-30B-A3B-Instruct-2507

| code | id | vs | GPQA-D | LCBv6 |
|---|---|---|---|---|
| [GRPO-GPT-5.5](https://arxiv.org/abs/2608.19197) | 2608.19197 | GRPO | +3.3 |  |
| [GRPO-GPT-5.5](https://arxiv.org/abs/2608.19197) | 2608.19197 | GRPO |  | -1.1 |
| [RLVE](https://arxiv.org/abs/2608.19197) | 2608.19197 | GRPO | -1.1 |  |
| [RLVE](https://arxiv.org/abs/2608.19197) | 2608.19197 | GRPO |  | -1.2 |
| [SPADE](https://arxiv.org/abs/2608.19197) | 2608.19197 | GRPO | +4.9 |  |
| [SPADE](https://arxiv.org/abs/2608.19197) | 2608.19197 | GRPO |  | +3.6 |

### OLMo-3-7B

| code | id | vs | LCBv5 | LCBv6 |
|---|---|---|---|---|
| [LOPD](https://arxiv.org/abs/2608.13040) | 2608.13040 | GRPO | +3.9 |  |
| [OPSD](https://arxiv.org/abs/2608.13040) | 2608.13040 | GRPO | -5.4 | -0.8 |
| [SDFT](https://arxiv.org/abs/2608.13040) | 2608.13040 | GRPO | -1.8 | -1.5 |
| [SDPO](https://arxiv.org/abs/2608.13040) | 2608.13040 | GRPO | +0.4 | -2.3 |
| [Skill-SD](https://arxiv.org/abs/2608.13040) | 2608.13040 | GRPO | -0.4 | -0.8 |

### Qwen2.5-1.5B

| code | id | vs | AIME24 | AMC23 | Minerva | Olymp | AIME25 | MATH500 | GSM8K | MMLU-Pro | LCBv6 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [ReasonMaxxer](https://arxiv.org/abs/2605.06241) | 2605.06241 | GRPO | -0.9 | +1.3 |  |  |  |  |  |  |  |
| [ReasonMaxxer](https://arxiv.org/abs/2605.06241) | 2605.06241 | GRPO |  |  | +0.7 | -2.2 |  |  | -2.3 |  |  |
| [Intuitor](https://arxiv.org/abs/2505.19590) | 2505.19590 | GRPO |  |  |  |  |  |  |  | -0.0 | +0.0 |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | GRPO | -4.2 | -15.9 |  |  | -0.4 |  |  |  |  |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | GRPO |  |  | -4.7 | -3.6 |  | -13.6 |  |  |  |

### Qwen3-1.7B-Base

| code | id | vs | AIME24 | AIME25 | HMMT | Minerva | GSM8K |
|---|---|---|---|---|---|---|---|
| [CISPO](https://arxiv.org/abs/2512.00499) | 2512.00499 | DAPO | +0.7* | -1.8* | +0.9* |  |  |
| [ESPO](https://arxiv.org/abs/2512.00499) | 2512.00499 | DAPO | +0.7* | +1.3* | +0.3* |  |  |
| [GMPO](https://arxiv.org/abs/2512.00499) | 2512.00499 | DAPO | -5.3* | -3.0* | -0.5* |  |  |
| [GSPO](https://arxiv.org/abs/2512.00499) | 2512.00499 | DAPO | -3.4* | -2.8* | -0.5* |  |  |
| [VeriFree](https://arxiv.org/abs/2505.21493) | 2505.21493 | Dr. GRPO |  |  |  | -9.5* | -5.5* |

### Qwen3-14B-Base

| code | id | vs | AIME24 | AIME25 | HMMT | LCBv6 | GPQA |
|---|---|---|---|---|---|---|---|
| [SCRL](https://arxiv.org/abs/2605.22074) | 2605.22074 | GRPO |  |  |  | +0.5 | +4.5 |
| [CISPO](https://arxiv.org/abs/2512.00499) | 2512.00499 | DAPO | +6.7* | +5.4* | +1.2* |  |  |
| [ESPO](https://arxiv.org/abs/2512.00499) | 2512.00499 | DAPO | +4.2* | +7.4* | +1.2* |  |  |
| [GMPO](https://arxiv.org/abs/2512.00499) | 2512.00499 | DAPO | -1.9* |  | -1.7* |  |  |
| [GSPO](https://arxiv.org/abs/2512.00499) | 2512.00499 | DAPO | -1.9* | +3.1* |  |  |  |

### DeepSeek-R1-Distill-Llama-8B

| code | id | vs | MATH500 | Olymp | HMMT25 |
|---|---|---|---|---|---|
| [ConSPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | GRPO |  |  | +4.1 |
| [ConSPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | GRPO | +1.8 | +5.0 |  |
| [DAPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | GRPO |  |  | -0.6 |
| [DAPO](https://arxiv.org/abs/2605.12969) | 2605.12969 | GRPO | -1.0 | -2.4 |  |

### DeepSeek-R1-Distill-Qwen-7B

| code | id | vs | AIME24 | AMC23 | AIME25 | Minerva | GSM8K |
|---|---|---|---|---|---|---|---|
| [SFT](https://arxiv.org/abs/2603.24472) | 2603.24472 | GRPO | -35.8 | -34.1 |  |  |  |
| [Critique-GRPO](https://arxiv.org/abs/2602.09000) | 2602.09000 | GRPO | +0.6 | +2.8 | +0.7 | +0.7 | +0.1 |
| [Self-Verification](https://arxiv.org/abs/2602.09000) | 2602.09000 | GRPO | +0.8 | +2.5 | +0.6 | +0.6 | +0.1 |
| [iGRPO](https://arxiv.org/abs/2602.09000) | 2602.09000 | GRPO | +1.3 | +5.0 | +1.3 | +1.1 | +0.3 |

### Qwen3

| code | id | vs | AIME24 | AIME25 | HMMT |
|---|---|---|---|---|---|
| [CISPO](https://arxiv.org/abs/2512.00499) | 2512.00499 | DAPO | +6.7* | +5.4* | +1.2* |
| [ESPO](https://arxiv.org/abs/2512.00499) | 2512.00499 | DAPO | +4.2* | +7.4* | +1.2* |
| [GMPO](https://arxiv.org/abs/2512.00499) | 2512.00499 | DAPO | -1.9* |  | -1.7* |
| [GSPO](https://arxiv.org/abs/2512.00499) | 2512.00499 | DAPO | -1.9* | +3.1* |  |

### Qwen3-30B-A3B

| code | id | vs | AIME24 | AIME25 | HMMT |
|---|---|---|---|---|---|
| [CISPO](https://arxiv.org/abs/2512.00499) | 2512.00499 | DAPO | +9.5* | +7.6* | +10.9* |
| [ESPO](https://arxiv.org/abs/2512.00499) | 2512.00499 | DAPO | +12.6* | +9.0* | +10.5* |
| [GMPO](https://arxiv.org/abs/2512.00499) | 2512.00499 | DAPO | -1.6* | -2.0* | +0.5* |
| [GSPO](https://arxiv.org/abs/2512.00499) | 2512.00499 | DAPO | +0.5* |  |  |

### Llama-3.1-Instruct

| code | id | vs | AIME24 | AIME25 | AMC23 | MATH500 | Minerva | Olymp |
|---|---|---|---|---|---|---|---|---|
| [HICRA](https://arxiv.org/abs/2509.03646) | 2509.03646 | GRPO | -0.6 | +0.3 |  |  |  |  |
| [HICRA](https://arxiv.org/abs/2509.03646) | 2509.03646 | GRPO |  |  | +2.1 |  |  |  |
| [HICRA](https://arxiv.org/abs/2509.03646) | 2509.03646 | GRPO |  |  |  | +1.8 | -1.4 | +0.9 |

### Nemotron-H-8B-Base-8K

| code | id | vs | AIME24 | AIME25 | AMC23 | Minerva | GSM8K |
|---|---|---|---|---|---|---|---|
| [Critique-GRPO](https://arxiv.org/abs/2602.09000) | 2602.09000 | GRPO | +0.1 | +0.6 | +1.7 | +1.9 | +6.5 |
| [Self-Verification](https://arxiv.org/abs/2602.09000) | 2602.09000 | GRPO | +0.2 | +0.7 | +1.4 | +1.5 | +4.3 |
| [iGRPO](https://arxiv.org/abs/2602.09000) | 2602.09000 | GRPO | +0.6 | +1.4 | +3.6 | +3.2 | +9.3 |

### Qwen2.5-32B

| code | id | vs | AIME24 | AMC23 | Minerva | Olymp | GSM8K |
|---|---|---|---|---|---|---|---|
| [ReasonMaxxer](https://arxiv.org/abs/2605.06241) | 2605.06241 | GRPO | +5.0 | +7.5 |  |  |  |
| [ReasonMaxxer](https://arxiv.org/abs/2605.06241) | 2605.06241 | GRPO |  |  | +4.8 | +2.9 | -1.1 |
| [DAPO](https://arxiv.org/abs/2503.14476) | 2503.14476 | GRPO | +20.0 |  |  |  |  |

### Qwen2.5-Instruct

| code | id | vs | Olymp | AIME24 |
|---|---|---|---|---|
| [E2H-C](https://arxiv.org/abs/2506.06632) | 2506.06632 | GRPO | +2.7 | +3.4 |
| [E2H-G](https://arxiv.org/abs/2506.06632) | 2506.06632 | GRPO | +1.4 | +3.4 |
| [Self-Evolve](https://arxiv.org/abs/2506.06632) | 2506.06632 | GRPO | +0.7 |  |

### Qwen3-1.7B

| code | id | vs | AIME24 | AIME25 | HMMT25 | MMLU-Pro | GPQA |
|---|---|---|---|---|---|---|---|
| [GRPO-VPS](https://arxiv.org/abs/2604.20659) | 2604.20659 | GRPO |  |  |  | +1.7 | +1.6 |
| [OPSD](https://arxiv.org/abs/2601.18734) | 2601.18734 | GRPO | +6.1 | +5.6 | +5.5 |  |  |
| [SFT](https://arxiv.org/abs/2601.18734) | 2601.18734 | GRPO | -2.7 | -2.0 | -1.0 |  |  |

### Qwen3-4B-Instruct

| code | id | vs | AIME24 | AIME25 | AMC23 | MATH500 | Minerva | Olymp |
|---|---|---|---|---|---|---|---|---|
| [HICRA](https://arxiv.org/abs/2509.03646) | 2509.03646 | GRPO | +4.6 | +5.1 |  |  |  |  |
| [HICRA](https://arxiv.org/abs/2509.03646) | 2509.03646 | GRPO |  |  | +1.7 |  |  |  |
| [HICRA](https://arxiv.org/abs/2509.03646) | 2509.03646 | GRPO |  |  |  | +1.0 | +0.7 | -0.7 |

### Other checkpoints (1)

| code | id | vs | Qwen2.5-3B · LCBv6 | Gemma-2-2B-it · AIME24 | Gemma-2-2B-it · AMC23 | Gemma-2-2B-it · Olymp | Mistral-7B · AIME24 | Mistral-7B · AMC23 | Mistral-7B · GSM8K | Mistral-7B · Minerva | OpenMath-Nemotron-14B · AIME24 | OpenMath-Nemotron-14B · AIME25 | OpenMath-Nemotron-7B · AIME24 | OpenMath-Nemotron-7B · AIME25 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [ReasonMaxxer](https://arxiv.org/abs/2605.06241) | 2605.06241 | GRPO |  |  |  |  | +5.5 | +0.5 |  |  |  |  |  |  |
| [ReasonMaxxer](https://arxiv.org/abs/2605.06241) | 2605.06241 | GRPO |  |  |  |  |  |  | -0.4 | +4.4 |  |  |  |  |
| [GRPO-VPS](https://arxiv.org/abs/2604.20659) | 2604.20659 | GRPO |  | +0.8 | +0.6 | +0.3 |  |  |  |  |  |  |  |  |
| [iGRPO](https://arxiv.org/abs/2602.09000) | 2602.09000 | GRPO |  |  |  |  |  |  |  |  | +1.9 | +1.0 |  |  |
| [iGRPO](https://arxiv.org/abs/2602.09000) | 2602.09000 | GRPO |  |  |  |  |  |  |  |  |  |  | +1.2 | +1.1 |
| [Intuitor](https://arxiv.org/abs/2505.19590) | 2505.19590 | GRPO | +0.1 |  |  |  |  |  |  |  |  |  |  |  |
| [Intuitor-Code](https://arxiv.org/abs/2505.19590) | 2505.19590 | GRPO | +0.1 |  |  |  |  |  |  |  |  |  |  |  |

### Other checkpoints (2)

| code | id | vs | OpenMath-Nemotron-7B · AMC23 | OpenMath-Nemotron-7B · GSM8K | OpenMath-Nemotron-7B · Minerva | Qwen2.5-7B · AIME24 | Qwen2.5-7B · AMC23 | Qwen2.5-7B · GSM8K | Qwen2.5-7B · Minerva | Qwen2.5-7B · Olymp | Qwen2.5-Math-1.5B-Instruct · AIME24 | Qwen2.5-Math-1.5B-Instruct · AMC23 | Qwen2.5-Math-1.5B-Instruct · MATH500 | Qwen2.5-Math-1.5B-Instruct · Minerva |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [ReasonMaxxer](https://arxiv.org/abs/2605.06241) | 2605.06241 | GRPO |  |  |  | +2.5 | +10.0 |  |  |  |  |  |  |  |
| [ReasonMaxxer](https://arxiv.org/abs/2605.06241) | 2605.06241 | GRPO |  |  |  |  |  | +6.7 | +7.4 | +5.3 |  |  |  |  |
| [iGRPO](https://arxiv.org/abs/2602.09000) | 2602.09000 | GRPO | +2.5 | +0.2 | +0.9 |  |  |  |  |  |  |  |  |  |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | GRPO |  |  |  |  |  |  |  |  | -1.2 | -1.9 |  |  |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | GRPO |  |  |  |  |  |  |  |  |  |  | -1.0 | -0.3 |

### Other checkpoints (3)

| code | id | vs | Qwen2.5-Math-1.5B-Instruct · Olymp | Qwen3-0.6B · AIME24 | Qwen3-0.6B · AMC23 | Qwen3-0.6B · GSM8K | Qwen3-0.6B · Minerva | Qwen3-0.6B · Olymp | Qwen3-8B-Base · AIME24 | Qwen3-8B-Base · AMC23 | Qwen3-8B-Base · GPQA | Qwen3-8B-Base · GSM8K | Qwen3-8B-Base · MATH500 | Qwen3-8B-Base · MMLU-Pro |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [ReasonMaxxer](https://arxiv.org/abs/2605.06241) | 2605.06241 | GRPO |  | +0.9 | +14.4 |  |  |  |  |  |  |  |  |  |
| [ReasonMaxxer](https://arxiv.org/abs/2605.06241) | 2605.06241 | GRPO |  |  |  | +15.3 | +3.7 | +3.3 |  |  |  |  |  |  |
| [VeriFree](https://arxiv.org/abs/2505.21493) | 2505.21493 | Dr. GRPO |  |  |  |  |  |  | +7.4* |  |  |  |  |  |
| [VeriFree](https://arxiv.org/abs/2505.21493) | 2505.21493 | Dr. GRPO |  |  |  |  |  |  |  | +10.0* | +0.5* | -1.8* | +4.6* | +1.3* |
| [1-shot RLVR](https://arxiv.org/abs/2504.20571) | 2504.20571 | GRPO | -1.7 |  |  |  |  |  |  |  |  |  |  |  |

### Other checkpoints (4)

| code | id | vs | Qwen3-8B-Base · Minerva | Qwen3-8B-Base · Olymp |
|---|---|---|---|---|
| [VeriFree](https://arxiv.org/abs/2505.21493) | 2505.21493 | Dr. GRPO | -8.5* | +8.4* |

## Not applicable

Trained open models with an OOD list, but only from-scratch pretraining (`pretrain` / `next-token` / `autoregressive` / `MLM` / `causal LM`). There is no untrained starting checkpoint to subtract.

| id | paper | methods |
|---|---|---|
| 2402.03300 | [DeepSeekMath: introducing Group Relative Policy ](https://arxiv.org/abs/2402.03300) | math continued pretrain |
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
