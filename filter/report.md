# Paper quality scores

326 readme papers (web/repo skipped). 326 have at least one Accept/Reject vote.

Ratings of well-known older papers (Llama 3, DeepSeekMath, DAPO, …) can be inflated: those works appear in Llama-3.1 / Qwen3 / Phi-4 pretraining. Rank **within year** when comparing.

## Model coverage

| model | n scored |
|---|---:|
| NAIPv2 | 326 |
| NAIP-v1 | 326 |
| SciJudge BT | 326 |
| DGC-BERT p(accept) | 326 |
| CycleReviewer-8B | 326 |
| CycleReviewer-70B | 0 |
| DeepReviewer-7B Standard | 317 |
| DeepReviewer-7B Fast | 314 |
| DeepReviewer-14B Fast | 324 |
| OpenReviewer-8B | 326 |
| SEA-E | 326 |

## DeepReviewer-7B Fast vs Standard

Intersection n=308. Spearman `0.373`. Accept/Reject macro-F1 `0.610` (n=308). Standard is a partial run: it counts in accepts/models, not in mean_rating10.

## Self-agreement (seed 0 vs seed 1)

| model | n | Spearman | macro-F1 |
|---|---:|---:|---:|
| CR-8B | 51 | 0.512 | 0.648 |
| DR-14B Fast | 51 | 0.742 | 0.753 |


## Aggregation

Hierarchical factor score on quality families (citation/impact held out). `final_score` is in [-1, 1]. 0 is where reviewer Accept/Reject votes split 50/50 among families whose accept rate is in (0.1, 0.9) (now `['cr8b', 'deep', 'dgcbert', 'or8b']`). `accepts/models` on badges are raw reviewer votes, not this score. VERDICT: DROP if score < -0.2 and conf >= 0.5 and impact_z < 0.5; WATCH if missing impact, conf < 0.5, |score| <= 0.2, or score < -0.2 with impact_z >= 0.5; else KEEP. `final_conf` is coverage `Σ w_used / Σ w_full` (no prior +1). A present family keeps mass 1.0 in q; missingness only lowers coverage.

Calibration `sigmoid(1.205 q + 0.122)`; share of papers with final_score > 0: `0.641`. VERDICT KEEP/WATCH/DROP = `{'WATCH': 156, 'KEEP': 115, 'DROP': 55}`.

Family accept rates used for `CAL_VOTE_RANGE`: CR-8B 0.233, DeepReviewer 0.556, DGC-BERT 0.515, OR-8B 0.810, SEA-E 0.936. In target: `['cr8b', 'deep', 'dgcbert', 'or8b']`.

| family | λ | w | PC1 |
|---|---:|---:|---:|
| NAIPv2 | 0.586 | 0.524 | 0.699 |
| DeepReviewer | 0.769 | 1.450 | 0.788 |
| CR-8B | 0.380 | 0.168 | 0.523 |
| OR-8B | 0.325 | 0.118 | 0.456 |
| SEA-E | 0.483 | 0.304 | 0.624 |
| DGC-BERT | 0.313 | 0.109 | 0.433 |

| model | LOFO | vs | salvage |
|---|---:|---|---:|
| NAIPv2 | 0.433 | other families | 0 |
| NAIP-v1 | 0.448 | sibling | 0 |
| SciJudge | 0.448 | sibling | 0 |
| DGC-BERT | 0.222 | other families | 0 |
| CR-8B | 0.294 | other families | 0 |
| DR-7B Std | 0.409 | other families | 0 |
| DR-7B Fast | 0.400 | other families | 6 |
| DR-14B Fast | 0.457 | other families | 0 |
| OR-8B | 0.209 | other families | 0 |
| SEA-E | 0.348 | other families | 0 |

Family clusters at rho>=0.35: deep+naipv2, cr8b, or8b, seae, dgcbert. At rho>=0.25: deep+naipv2+seae, cr8b, or8b, dgcbert. Model clusters at rho>=0.35: dr14b+dr7bf+naipv2, naipv1+scijudge, dgcbert, cr8b, dr7b, or8b, seae. At rho>=0.25: dr14b+dr7b+dr7bf+naipv2+seae, naipv1+scijudge, dgcbert, cr8b, or8b.

| model | field | n | rho vs other families |
|---|---|---:|---:|
| CR-8B | rating | 326 | 0.273 |
| CR-8B | contribution | 326 | 0.297 |
| CR-8B | soundness | 326 | 0.244 |
| CR-8B | presentation | 326 | 0.224 |
| DR-7B Std | rating | 317 | 0.385 |
| DR-7B Std | contribution | 317 | 0.385 |
| DR-7B Std | soundness | 317 | 0.322 |
| DR-7B Std | presentation | 317 | 0.325 |
| DR-7B Fast | rating | 314 | 0.355 |
| DR-7B Fast | contribution | 319 | 0.357 |
| DR-7B Fast | soundness | 319 | 0.293 |
| DR-7B Fast | presentation | 319 | 0.333 |
| DR-14B Fast | rating | 324 | 0.381 |
| DR-14B Fast | contribution | 324 | 0.473 |
| DR-14B Fast | soundness | 324 | 0.466 |
| DR-14B Fast | presentation | 324 | 0.343 |
| OR-8B | rating | 326 | 0.204 |
| OR-8B | contribution | 326 | 0.238 |
| OR-8B | soundness | 326 | 0.087 |
| OR-8B | presentation | 326 | 0.158 |
| SEA-E | rating | 326 | 0.345 |
| SEA-E | contribution | 326 | 0.250 |
| SEA-E | soundness | 326 | 0.175 |
| SEA-E | presentation | 326 | 0.113 |

| model | subset | n | mean consensus z |
|---|---|---:|---:|
| CR-8B | parsed | 326 | -0.003 |
| CR-8B | salvage | 0 |  |
| CR-8B | unparsed | 0 |  |
| DR-7B Std | parsed | 317 | 0.021 |
| DR-7B Std | salvage | 0 |  |
| DR-7B Std | unparsed | 9 | -0.864 |
| DR-7B Fast | parsed | 314 | 0.010 |
| DR-7B Fast | salvage | 6 | -0.571 |
| DR-7B Fast | unparsed | 6 | -0.149 |
| DR-14B Fast | parsed | 324 | 0.006 |
| DR-14B Fast | salvage | 0 |  |
| DR-14B Fast | unparsed | 2 | -1.465 |
| OR-8B | parsed | 326 | -0.003 |
| OR-8B | salvage | 0 |  |
| OR-8B | unparsed | 0 |  |
| SEA-E | parsed | 326 | -0.003 |
| SEA-E | salvage | 0 |  |
| SEA-E | unparsed | 0 |  |

Remaining unparsed reviews after retry are shifted down (DR-7B Std n=9, consensus z=-0.864; DR-7B Fast n=6, consensus z=-0.149; DR-14B Fast n=2, consensus z=-1.465). No reject-imputation; those papers already get signal from other families.


## Agreement (Spearman)

| model A | model B | n | Spearman |
|---|---|---:|---:|
| NAIPv2 | NAIP-v1 | 326 | 0.250 |
| NAIPv2 | SciJudge | 326 | 0.435 |
| NAIPv2 | DGC-BERT | 326 | 0.318 |
| NAIPv2 | CR-8B | 326 | 0.174 |
| NAIPv2 | CR-70B | 0 |  |
| NAIPv2 | DR-7B Std | 317 | 0.403 |
| NAIPv2 | DR-7B Fast | 314 | 0.318 |
| NAIPv2 | DR-14B Fast | 324 | 0.480 |
| NAIPv2 | OR-8B | 326 | 0.225 |
| NAIPv2 | SEA-E | 326 | 0.327 |
| NAIP-v1 | SciJudge | 326 | 0.486 |
| NAIP-v1 | DGC-BERT | 326 | 0.125 |
| NAIP-v1 | CR-8B | 326 | 0.218 |
| NAIP-v1 | CR-70B | 0 |  |
| NAIP-v1 | DR-7B Std | 317 | 0.126 |
| NAIP-v1 | DR-7B Fast | 314 | 0.149 |
| NAIP-v1 | DR-14B Fast | 324 | 0.102 |
| NAIP-v1 | OR-8B | 326 | 0.122 |
| NAIP-v1 | SEA-E | 326 | 0.110 |
| SciJudge | DGC-BERT | 326 | 0.403 |
| SciJudge | CR-8B | 326 | 0.331 |
| SciJudge | CR-70B | 0 |  |
| SciJudge | DR-7B Std | 317 | 0.277 |
| SciJudge | DR-7B Fast | 314 | 0.216 |
| SciJudge | DR-14B Fast | 324 | 0.327 |
| SciJudge | OR-8B | 326 | 0.240 |
| SciJudge | SEA-E | 326 | 0.284 |
| DGC-BERT | CR-8B | 326 | 0.102 |
| DGC-BERT | CR-70B | 0 |  |
| DGC-BERT | DR-7B Std | 317 | 0.208 |
| DGC-BERT | DR-7B Fast | 314 | 0.188 |
| DGC-BERT | DR-14B Fast | 324 | 0.190 |
| DGC-BERT | OR-8B | 326 | -0.051 |
| DGC-BERT | SEA-E | 326 | 0.124 |
| CR-8B | CR-70B | 0 |  |
| CR-8B | DR-7B Std | 317 | 0.240 |
| CR-8B | DR-7B Fast | 314 | 0.160 |
| CR-8B | DR-14B Fast | 324 | 0.226 |
| CR-8B | OR-8B | 326 | 0.133 |
| CR-8B | SEA-E | 326 | 0.153 |
| CR-70B | DR-7B Std | 0 |  |
| CR-70B | DR-7B Fast | 0 |  |
| CR-70B | DR-14B Fast | 0 |  |
| CR-70B | OR-8B | 0 |  |
| CR-70B | SEA-E | 0 |  |
| DR-7B Std | DR-7B Fast | 308 | 0.373 |
| DR-7B Std | DR-14B Fast | 317 | 0.388 |
| DR-7B Std | OR-8B | 317 | 0.239 |
| DR-7B Std | SEA-E | 317 | 0.280 |
| DR-7B Fast | DR-14B Fast | 313 | 0.313 |
| DR-7B Fast | OR-8B | 314 | 0.234 |
| DR-7B Fast | SEA-E | 314 | 0.282 |
| DR-14B Fast | OR-8B | 324 | 0.270 |
| DR-14B Fast | SEA-E | 324 | 0.223 |
| OR-8B | SEA-E | 326 | 0.220 |

## Agreement (macro-F1 Accept/Reject)

| model A | model B | n | macro-F1 |
|---|---|---:|---:|
| DGC-BERT | CR-8B | 326 | 0.456 |
| DGC-BERT | CR-70B | 0 |  |
| DGC-BERT | DR-7B Std | 317 | 0.552 |
| DGC-BERT | DR-7B Fast | 314 | 0.567 |
| DGC-BERT | DR-14B Fast | 324 | 0.571 |
| DGC-BERT | OR-8B | 326 | 0.451 |
| DGC-BERT | SEA-E | 326 | 0.426 |
| CR-8B | CR-70B | 0 |  |
| CR-8B | DR-7B Std | 317 | 0.529 |
| CR-8B | DR-7B Fast | 314 | 0.480 |
| CR-8B | DR-14B Fast | 324 | 0.444 |
| CR-8B | OR-8B | 326 | 0.348 |
| CR-8B | SEA-E | 326 | 0.271 |
| CR-70B | DR-7B Std | 0 |  |
| CR-70B | DR-7B Fast | 0 |  |
| CR-70B | DR-14B Fast | 0 |  |
| CR-70B | OR-8B | 0 |  |
| CR-70B | SEA-E | 0 |  |
| DR-7B Std | DR-7B Fast | 308 | 0.610 |
| DR-7B Std | DR-14B Fast | 317 | 0.591 |
| DR-7B Std | OR-8B | 317 | 0.529 |
| DR-7B Std | SEA-E | 317 | 0.406 |
| DR-7B Fast | DR-14B Fast | 313 | 0.651 |
| DR-7B Fast | OR-8B | 314 | 0.553 |
| DR-7B Fast | SEA-E | 314 | 0.495 |
| DR-14B Fast | OR-8B | 324 | 0.573 |
| DR-14B Fast | SEA-E | 324 | 0.536 |
| OR-8B | SEA-E | 326 | 0.634 |

## Ranking by readme section

### Reinforcement learning

| rank | title | year | final | accept | key |
|---:|---|---|---:|---:|---|
| 1 | [First return, then explore](#arxiv-2004.12919) | 2020 | +0.60 | 6/7 | `arxiv:2004.12919` |
| 2 | [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](#arxiv-1801.01290) | 2018 | +0.47 | 6/7 | `arxiv:1801.01290` |
| 3 | [Deep Neuroevolution: Genetic Algorithms Are a Competitive Alternative for Training Deep Neural Networks for Reinforcement Learning](#arxiv-1712.06567) | 2017 | +0.41 | 4/7 | `arxiv:1712.06567` |
| 4 | [A Distributional Perspective on Reinforcement Learning](#arxiv-1707.06887) | 2017 | +0.36 | 6/7 | `arxiv:1707.06887` |
| 5 | [The Primacy Bias in Deep Reinforcement Learning](#arxiv-2205.07802) | 2022 | +0.27 | 6/7 | `arxiv:2205.07802` |
| 6 | [Bigger, Better, Faster: Human-level Atari with human-level efficiency](#arxiv-2305.19452) | 2023 | +0.22 | 3/7 | `arxiv:2305.19452` |
| 7 | [Beyond The Rainbow: High Performance Deep Reinforcement Learning on a Desktop PC](#arxiv-2411.03820) | 2024 | +0.21 | 2/7 | `arxiv:2411.03820` |
| 8 | [Sample-Efficient RL by Breaking the Replay Ratio Barrier (ICLR 2023, precursor of BBF)](#openreview-OpC-9aBBVJe) | unknown | +0.16 | 6/7 | `openreview:OpC-9aBBVJe` |
| 9 | [Mastering Diverse Domains through World Models](#arxiv-2301.04104) | 2023 | +0.16 | 5/7 | `arxiv:2301.04104` |
| 10 | [Metalearning Continual Learning Algorithms](#arxiv-2312.00276) | 2023 | +0.12 | 5/7 | `arxiv:2312.00276` |
| 11 | [Dueling Network Architectures for Deep Reinforcement Learning](#arxiv-1511.06581) | 2015 | +0.11 | 6/7 | `arxiv:1511.06581` |
| 12 | [CDE: Curiosity-Driven Exploration for Efficient Reinforcement Learning in Large Language Models](#arxiv-2509.09675) | 2025 | +0.11 | 6/7 | `arxiv:2509.09675` |
| 13 | [Deep Reinforcement Learning with Double Q-learning](#arxiv-1509.06461) | 2015 | +0.10 | 5/7 | `arxiv:1509.06461` |
| 14 | [Q-Learning With World Models](#arxiv-2608.17163) | 2026 | +0.08 | 6/7 | `arxiv:2608.17163` |
| 15 | [For SALE: State-Action Representation Learning for Deep Reinforcement Learning](#arxiv-2306.02451) | 2023 | +0.04 | 5/7 | `arxiv:2306.02451` |
| 16 | [Prioritized Experience Replay](#arxiv-1511.05952) | 2015 | +0.01 | 4/7 | `arxiv:1511.05952` |
| 17 | [1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities](#arxiv-2503.14858) | 2025 | +0.01 | 5/7 | `arxiv:2503.14858` |
| 18 | [Rainbow: Combining Improvements in Deep Reinforcement Learning](#arxiv-1710.02298) | 2017 | -0.04 | 3/7 | `arxiv:1710.02298` |
| 19 | [In-Context Reinforcement Learning for Variable Action Spaces](#arxiv-2312.13327) | 2023 | -0.06 | 4/7 | `arxiv:2312.13327` |
| 20 | [Towards General-Purpose Model-Free Reinforcement Learning](#arxiv-2501.16142) | 2025 | -0.13 | 5/7 | `arxiv:2501.16142` |
| 21 | [Revisiting Rainbow: Promoting more Insightful and Inclusive Deep Reinforcement Learning Research](#arxiv-2011.14826) | 2020 | -0.26 | 1/7 | `arxiv:2011.14826` |
| 22 | [Addressing Function Approximation Error in Actor-Critic Methods](#arxiv-1802.09477) | 2018 | -0.37 | 1/4 | `arxiv:1802.09477` |
| 23 | [Offline Reinforcement Learning: Tutorial, Review, and Perspectives on Open Problems](#arxiv-2005.01643) | 2020 | -0.42 | 0/7 | `arxiv:2005.01643` |
| 24 | [Meta-Reinforcement Learning with Zero-Shot RL](#openreview-XyGJJ4FPoX) | unknown | -0.47 | 0/7 | `openreview:XyGJJ4FPoX` |
| 25 | [A Minimalist Approach to Offline Reinforcement Learning](#arxiv-2106.06860) | 2021 | -0.49 | 3/7 | `arxiv:2106.06860` |
| 26 | [Benchmarking Batch Deep Reinforcement Learning Algorithms](#arxiv-1910.01708) | 2019 | -0.56 | 2/7 | `arxiv:1910.01708` |

### Post-training

| rank | title | year | final | accept | key |
|---:|---|---|---:|---:|---|
| 1 | [Rethinking RL for LLM Reasoning: It's Sparse Policy Selection, Not Capability Learning](#arxiv-2605.06241) | 2026 | +0.49 | 5/7 | `arxiv:2605.06241` |
| 2 | [OPRD: On-Policy Representation Distillation](#arxiv-2606.06021) | 2026 | +0.46 | 5/7 | `arxiv:2606.06021` |
| 3 | [GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning](#arxiv-2507.19457) | 2025 | +0.45 | 6/7 | `arxiv:2507.19457` |
| 4 | [On the Generalization of SFT: A Reinforcement Learning Perspective with Reward Rectification](#arxiv-2508.05629) | 2025 | +0.43 | 6/7 | `arxiv:2508.05629` |
| 5 | [Critique-GRPO: Advancing LLM Reasoning with Natural Language and Numerical Feedback](#arxiv-2506.03106) | 2025 | +0.42 | 7/7 | `arxiv:2506.03106` |
| 6 | [The Art of Scaling Reinforcement Learning Compute for LLMs](#arxiv-2510.13786) | 2025 | +0.42 | 6/7 | `arxiv:2510.13786` |
| 7 | [Spurious Rewards Paradox: Mechanistically Understanding How RLVR Activates Memorization Shortcuts in LLMs](#arxiv-2601.11061) | 2026 | +0.39 | 6/7 | `arxiv:2601.11061` |
| 8 | [RLVE: Scaling Up Reinforcement Learning for Language Models with Adaptive Verifiable Environments](#arxiv-2511.07317) | 2025 | +0.37 | 5/7 | `arxiv:2511.07317` |
| 9 | [Rethinking On-Policy Distillation of Large Language Models: Phenomenology, Mechanism, and Recipe](#arxiv-2604.13016) | 2026 | +0.36 | 6/7 | `arxiv:2604.13016` |
| 10 | [Revisiting Reinforcement Learning with Verifiable Rewards from a Contrastive Perspective](#arxiv-2605.12969) | 2026 | +0.35 | 6/7 | `arxiv:2605.12969` |
| 11 | [MiniMax-M1: Scaling Test-Time Compute Efficiently with Lightning Attention](#arxiv-2506.13585) | 2025 | +0.35 | 4/7 | `arxiv:2506.13585` |
| 12 | [Understanding R1-Zero-Like Training: A Critical Perspective](#arxiv-2503.20783) | 2025 | +0.33 | 5/7 | `arxiv:2503.20783` |
| 13 | [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](#arxiv-2402.03300) | 2024 | +0.32 | 5/7 | `arxiv:2402.03300` |
| 14 | [TTRL: Test-Time Reinforcement Learning](#arxiv-2504.16084) | 2025 | +0.32 | 5/7 | `arxiv:2504.16084` |
| 15 | [Group-in-Group Policy Optimization for LLM Agent Training](#arxiv-2505.10978) | 2025 | +0.31 | 7/7 | `arxiv:2505.10978` |
| 16 | [Skip-Connected Policy Optimization for Implicit Advantage](#arxiv-2604.08690) | 2026 | +0.29 | 6/7 | `arxiv:2604.08690` |
| 17 | [Reinforcement Learning via Self-Distillation](#arxiv-2601.20802) | 2026 | +0.27 | 6/7 | `arxiv:2601.20802` |
| 18 | [Learning to Discover at Test Time](#arxiv-2601.16175) | 2026 | +0.27 | 6/7 | `arxiv:2601.16175` |
| 19 | [Beyond the 80/20 Rule: High-Entropy Minority Tokens Drive Effective Reinforcement Learning for LLM Reasoning](#arxiv-2506.01939) | 2025 | +0.27 | 4/7 | `arxiv:2506.01939` |
| 20 | [SR-GRPO: Stable Rank as an Intrinsic Geometric Reward for Large Language Model Alignment](#arxiv-2512.02807) | 2025 | +0.23 | 6/7 | `arxiv:2512.02807` |
| 21 | [Self-Distillation Bridges Distribution Gap in Language Model Fine-Tuning](#arxiv-2402.13669) | 2024 | +0.22 | 5/7 | `arxiv:2402.13669` |
| 22 | [Reasoning with Sampling: Your Base Model is Smarter Than You Think](#arxiv-2510.14901) | 2025 | +0.21 | 6/7 | `arxiv:2510.14901` |
| 23 | [From Reasoning Chains to Verifiable Subproblems: Curriculum Reinforcement Learning Enables Credit Assignment for LLM Reasoning](#arxiv-2605.22074) | 2026 | +0.20 | 6/7 | `arxiv:2605.22074` |
| 24 | [ESPO: Entropy Importance Sampling Policy Optimization](#arxiv-2512.00499) | 2025 | +0.19 | 6/7 | `arxiv:2512.00499` |
| 25 | [Gradient Regularization Mitigates Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards](#arxiv-2602.18037) | 2026 | +0.13 | 4/7 | `arxiv:2602.18037` |
| 26 | [Latent On-Policy Self-Distillation](#arxiv-2608.13040) | 2026 | +0.13 | 6/7 | `arxiv:2608.13040` |
| 27 | [Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models](#arxiv-2601.18734) | 2026 | +0.12 | 5/7 | `arxiv:2601.18734` |
| 28 | [Soft Adaptive Policy Optimization](#arxiv-2511.20347) | 2025 | +0.12 | 5/7 | `arxiv:2511.20347` |
| 29 | [Self-Refine: Iterative Refinement with Self-Feedback](#arxiv-2303.17651) | 2023 | +0.10 | 6/7 | `arxiv:2303.17651` |
| 30 | [To Retain or to Adapt? Generalizing Continual Learning](#arxiv-2607.05609) | 2026 | +0.07 | 5/7 | `arxiv:2607.05609` |
| 31 | [Compute as Teacher: Turning Inference Compute Into Reference-Free Supervision](#arxiv-2509.14234) | 2025 | +0.06 | 5/7 | `arxiv:2509.14234` |
| 32 | [Curriculum Reinforcement Learning from Easy to Hard Tasks Improves LLM Reasoning](#arxiv-2506.06632) | 2025 | +0.05 | 5/7 | `arxiv:2506.06632` |
| 33 | [Group Sequence Policy Optimization](#arxiv-2507.18071) | 2025 | +0.04 | 5/7 | `arxiv:2507.18071` |
| 34 | [Towards Execution-Grounded Automated AI Research](#arxiv-2601.14525) | 2026 | +0.04 | 5/7 | `arxiv:2601.14525` |
| 35 | [When Does Continual Learning Require Learning](#arxiv-2607.07847) | 2026 | +0.02 | 4/7 | `arxiv:2607.07847` |
| 36 | [Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?](#arxiv-2504.13837) | 2025 | +0.01 | 4/7 | `arxiv:2504.13837` |
| 37 | [Learning from Own Solutions: Self-Conditioned Credit Assignment for Reinforcement Learning with Verifiable Rewards](#arxiv-2606.18810) | 2026 | +0.01 | 4/7 | `arxiv:2606.18810` |
| 38 | [Learning to Reason without External Rewards](#arxiv-2505.19590) | 2025 | +0.00 | 3/7 | `arxiv:2505.19590` |
| 39 | [Unifying Group-Relative and Self-Distillation Policy Optimization via Sample Routing](#arxiv-2604.02288) | 2026 | -0.00 | 5/7 | `arxiv:2604.02288` |
| 40 | [GRPO-VPS: Enhancing Group Relative Policy Optimization with Verifiable Process Supervision for Effective Reasoning](#arxiv-2604.20659) | 2026 | -0.01 | 5/7 | `arxiv:2604.20659` |
| 41 | [LADDER: Self-Improving LLMs Through Recursive Problem Decomposition](#arxiv-2503.00735) | 2025 | -0.01 | 4/7 | `arxiv:2503.00735` |
| 42 | [Emergent Hierarchical Reasoning in LLMs through Reinforcement Learning](#arxiv-2509.03646) | 2025 | -0.05 | 3/7 | `arxiv:2509.03646` |
| 43 | [iGRPO: Self-Feedback-Driven LLM Reasoning](#arxiv-2602.09000) | 2026 | -0.05 | 4/7 | `arxiv:2602.09000` |
| 44 | [From $f(x)$ and $g(x)$ to $f(g(x))$: LLMs Learn New Skills in RL by Composing Old Ones](#arxiv-2509.25123) | 2025 | -0.06 | 5/7 | `arxiv:2509.25123` |
| 45 | [Revisiting On-Policy Distillation: Empirical Failure Modes and Simple Fixes](#arxiv-2603.25562) | 2026 | -0.07 | 5/7 | `arxiv:2603.25562` |
| 46 | [The First Few Tokens Are All You Need: An Efficient and Effective Unsupervised Prefix Fine-Tuning Method for Reasoning Models](#arxiv-2503.02875) | 2025 | -0.07 | 3/7 | `arxiv:2503.02875` |
| 47 | [Single-stream Policy Optimization](#arxiv-2509.13232) | 2025 | -0.07 | 5/7 | `arxiv:2509.13232` |
| 48 | [Self-Distillation Enables Continual Learning](#arxiv-2601.19897) | 2026 | -0.08 | 6/7 | `arxiv:2601.19897` |
| 49 | [RIFT: A RubrIc Failure Mode Taxonomy and Automated Diagnostics](#arxiv-2604.01375) | 2026 | -0.10 | 3/7 | `arxiv:2604.01375` |
| 50 | [It Takes Two: Your GRPO Is Secretly DPO](#arxiv-2510.00977) | 2025 | -0.10 | 5/7 | `arxiv:2510.00977` |
| 51 | [Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs?](#arxiv-2603.24472) | 2026 | -0.17 | 3/7 | `arxiv:2603.24472` |
| 52 | [Klear-Reasoner: Advancing Reasoning Capability via Gradient-Preserving Clipping Policy Optimization](#arxiv-2508.07629) | 2025 | -0.23 | 3/6 | `arxiv:2508.07629` |
| 53 | [Weight-Space Geometry of Offline Reasoning Training](#arxiv-2606.23740) | 2026 | -0.25 | 2/7 | `arxiv:2606.23740` |
| 54 | [DAPO: An Open-Source LLM Reinforcement Learning System at Scale](#arxiv-2503.14476) | 2025 | -0.32 | 3/7 | `arxiv:2503.14476` |
| 55 | [BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](#arxiv-2608.09888) | 2026 | -0.35 | 2/7 | `arxiv:2608.09888` |
| 56 | [Evolutionary Strategies lead to Catastrophic Forgetting in LLMs](#arxiv-2601.20861) | 2026 | -0.54 | 3/7 | `arxiv:2601.20861` |

### LLMs: architectures, context, training

| rank | title | year | final | accept | key |
|---:|---|---|---:|---:|---|
| 1 | [Zoology: Measuring and Improving Recall in Efficient Language Models](#arxiv-2312.04927) | 2023 | +0.60 | 5/7 | `arxiv:2312.04927` |
| 2 | [Cache-to-Cache: Direct Semantic Communication Between Large Language Models](#arxiv-2510.03215) | 2025 | +0.50 | 5/7 | `arxiv:2510.03215` |
| 3 | [Large Language Diffusion Models](#arxiv-2502.09992) | 2025 | +0.50 | 6/7 | `arxiv:2502.09992` |
| 4 | [Hyena Hierarchy: Towards Larger Convolutional Language Models](#arxiv-2302.10866) | 2023 | +0.42 | 6/7 | `arxiv:2302.10866` |
| 5 | [Neural Networks and the Chomsky Hierarchy](#arxiv-2207.02098) | 2022 | +0.31 | 7/7 | `arxiv:2207.02098` |
| 6 | [Enabling Agents to Communicate Entirely in Latent Space](#arxiv-2511.09149) | 2025 | +0.29 | 4/7 | `arxiv:2511.09149` |
| 7 | [DiffusionGemma Technical Report](#arxiv-2608.00146) | 2026 | +0.29 | 3/7 | `arxiv:2608.00146` |
| 8 | [Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference](#arxiv-2412.13663) | 2024 | +0.28 | 5/7 | `arxiv:2412.13663` |
| 9 | [Language Is Not All You Need: Aligning Perception with Language Models](#arxiv-2302.14045) | 2023 | +0.26 | 6/7 | `arxiv:2302.14045` |
| 10 | [Memorizing Transformers](#arxiv-2203.08913) | 2022 | +0.25 | 5/7 | `arxiv:2203.08913` |
| 11 | [XBridge: Entity-Grounded Latent Bridge for Heterogeneous LLM Communication](#arxiv-2608.11676) | 2026 | +0.25 | 5/7 | `arxiv:2608.11676` |
| 12 | [A Hippocampus for Linear Attention: An Exact Memory for What the Recurrent State Forgets](#arxiv-2607.02303) | 2026 | +0.24 | 6/7 | `arxiv:2607.02303` |
| 13 | [Scaling MLPs: A Tale of Inductive Bias](#arxiv-2306.13575) | 2023 | +0.24 | 3/7 | `arxiv:2306.13575` |
| 14 | [2 OLMo 2 Furious](#arxiv-2501.00656) | 2024 | +0.23 | 5/7 | `arxiv:2501.00656` |
| 15 | [Florence-2: Advancing a Unified Representation for a Variety of Vision Tasks](#arxiv-2311.06242) | 2023 | +0.23 | 4/7 | `arxiv:2311.06242` |
| 16 | [Olmo 3](#arxiv-2512.13961) | 2025 | +0.22 | 3/7 | `arxiv:2512.13961` |
| 17 | [DMax: Aggressive Parallel Decoding for dLLMs](#arxiv-2604.08302) | 2026 | +0.21 | 4/7 | `arxiv:2604.08302` |
| 18 | [Skip a Layer or Loop It? Learning Program-of-Layers in LLMs](#arxiv-2606.06574) | 2026 | +0.19 | 6/7 | `arxiv:2606.06574` |
| 19 | [Unlimiformer: Long-Range Transformers with Unlimited Length Input](#arxiv-2305.01625) | 2023 | +0.18 | 5/7 | `arxiv:2305.01625` |
| 20 | [Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation](#arxiv-2507.10524) | 2025 | +0.17 | 7/7 | `arxiv:2507.10524` |
| 21 | [LLaDA2.0: Scaling Up Diffusion Language Models to 100B](#arxiv-2512.15745) | 2025 | +0.15 | 4/7 | `arxiv:2512.15745` |
| 22 | [Recursive Language Models](#arxiv-2512.24601) | 2025 | +0.15 | 4/7 | `arxiv:2512.24601` |
| 23 | [Cross-Model KV Cache Transfer in LLM Families: A Closed-Form Linear Mapping for Prefill Reuse](#arxiv-2608.03893) | 2026 | +0.14 | 5/7 | `arxiv:2608.03893` |
| 24 | [Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention](#arxiv-2006.16236) | 2020 | +0.13 | 5/7 | `arxiv:2006.16236` |
| 25 | [Searching for Activation Functions](#arxiv-1710.05941) | 2017 | +0.13 | 4/7 | `arxiv:1710.05941` |
| 26 | [Communicating Activations Between Language Model Agents](#arxiv-2501.14082) | 2025 | +0.11 | 6/7 | `arxiv:2501.14082` |
| 27 | [The Llama 3 Herd of Models](#arxiv-2407.21783) | 2024 | +0.08 | 3/7 | `arxiv:2407.21783` |
| 28 | [Encoder-Decoder or Decoder-Only? Revisiting Encoder-Decoder Large Language Model](#arxiv-2510.26622) | 2025 | +0.06 | 6/7 | `arxiv:2510.26622` |
| 29 | [Beyond Scattered Acceptance: Fast and Coherent Inference for DLMs via Longest Stable Prefixes](#arxiv-2603.05454) | 2026 | +0.05 | 5/7 | `arxiv:2603.05454` |
| 30 | [Encoder-Decoder Gemma: Improving the Quality-Efficiency Trade-Off via Adaptation](#arxiv-2504.06225) | 2025 | -0.01 | 5/7 | `arxiv:2504.06225` |
| 31 | [LLaDA2.1: Speeding Up Text Diffusion via Token Editing](#arxiv-2602.08676) | 2026 | -0.04 | 5/7 | `arxiv:2602.08676` |
| 32 | [Leave No Context Behind: Efficient Infinite Context Transformers with Infini-attention](#arxiv-2404.07143) | 2024 | -0.06 | 3/7 | `arxiv:2404.07143` |
| 33 | [TransformerFAM: Feedback attention is working memory](#arxiv-2404.09173) | 2024 | -0.09 | 3/7 | `arxiv:2404.09173` |
| 34 | [Latent Cache Flow: Model-to-Model Communication Without Text](#arxiv-2605.22863) | 2026 | -0.16 | 4/7 | `arxiv:2605.22863` |
| 35 | [Energy Transformer](#arxiv-2302.07253) | 2023 | -0.30 | 4/7 | `arxiv:2302.07253` |
| 36 | [T5Gemma 2: Seeing, Reading, and Understanding Longer](#arxiv-2512.14856) | 2025 | -0.30 | 2/7 | `arxiv:2512.14856` |
| 37 | [xLSTM: Extended Long Short-Term Memory](#arxiv-2405.04517) | 2024 | -0.33 | 2/7 | `arxiv:2405.04517` |
| 38 | [Your Transformer is Secretly Linear](#arxiv-2405.12250) | 2024 | -0.41 | 3/7 | `arxiv:2405.12250` |
| 39 | [GLU Variants Improve Transformer](#arxiv-2002.05202) | 2020 | -0.58 | 1/7 | `arxiv:2002.05202` |

### Reasoning and the "physics" of language models

| rank | title | year | final | accept | key |
|---:|---|---|---:|---:|---|
| 1 | [Progress measures for grokking via mechanistic interpretability](#arxiv-2301.05217) | 2023 | +0.65 | 7/7 | `arxiv:2301.05217` |
| 2 | [Arithmetic Without Algorithms: Language Models Solve Math With a Bag of Heuristics](#arxiv-2410.21272) | 2024 | +0.60 | 6/7 | `arxiv:2410.21272` |
| 3 | [Reinforcing General Reasoning without Verifiers](#arxiv-2505.21493) | 2025 | +0.50 | 6/7 | `arxiv:2505.21493` |
| 4 | [Grokked Transformers are Implicit Reasoners: A Mechanistic Journey to the Edge of Generalization](#arxiv-2405.15071) | 2024 | +0.46 | 6/7 | `arxiv:2405.15071` |
| 5 | [Physics of Language Models: Part 1, Learning Hierarchical Language Structures](#arxiv-2305.13673) | 2023 | +0.45 | 6/7 | `arxiv:2305.13673` |
| 6 | [Grokking Group Multiplication with Cosets](#openreview-hcQfTsVnBo) | unknown | +0.43 | 5/7 | `openreview:hcQfTsVnBo` |
| 7 | [rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking](#arxiv-2501.04519) | 2025 | +0.39 | 6/7 | `arxiv:2501.04519` |
| 8 | [Spurious Rewards: Rethinking Training Signals in RLVR](#arxiv-2506.10947) | 2025 | +0.39 | 6/6 | `arxiv:2506.10947` |
| 9 | [Language Models Use Trigonometry to Do Addition](#arxiv-2502.00873) | 2025 | +0.39 | 6/7 | `arxiv:2502.00873` |
| 10 | [Pre-trained Large Language Models Use Fourier Features to Compute Addition](#arxiv-2406.03445) | 2024 | +0.37 | 6/7 | `arxiv:2406.03445` |
| 11 | [Are Emergent Abilities of Large Language Models a Mirage?](#arxiv-2304.15004) | 2023 | +0.37 | 5/7 | `arxiv:2304.15004` |
| 12 | [Physics of Language Models: Part 3.3, Knowledge Capacity Scaling Laws](#arxiv-2404.05405) | 2024 | +0.36 | 5/7 | `arxiv:2404.05405` |
| 13 | [In-Context Algebra](#arxiv-2512.16902) | 2025 | +0.34 | 7/7 | `arxiv:2512.16902` |
| 14 | [Physics of Language Models: Part 2.1, Grade-School Math and the Hidden Reasoning Process](#arxiv-2407.20311) | 2024 | +0.32 | 5/7 | `arxiv:2407.20311` |
| 15 | [How do language models learn facts? Dynamics, curricula and hallucinations](#arxiv-2503.21676) | 2025 | +0.30 | 6/7 | `arxiv:2503.21676` |
| 16 | [Bridging the Gap Between Latent and Explicit Reasoning with Looped Transformers](#arxiv-2606.31779) | 2026 | +0.29 | 5/7 | `arxiv:2606.31779` |
| 17 | [Physics of Language Models: Part 3.2, Knowledge Manipulation](#arxiv-2309.14402) | 2023 | +0.29 | 3/6 | `arxiv:2309.14402` |
| 18 | [Self-Consistency Improves Chain of Thought Reasoning in Language Models](#arxiv-2203.11171) | 2022 | +0.25 | 7/7 | `arxiv:2203.11171` |
| 19 | [Reliable Chain-of-Thought via Prefix Consistency](#arxiv-2605.07654) | 2026 | +0.24 | 6/7 | `arxiv:2605.07654` |
| 20 | [The Unreasonable Effectiveness of Entropy Minimization in LLM Reasoning](#arxiv-2505.15134) | 2025 | +0.23 | 6/7 | `arxiv:2505.15134` |
| 21 | [SIM-CoT: Supervised Implicit Chain-of-Thought](#arxiv-2509.20317) | 2025 | +0.23 | 6/7 | `arxiv:2509.20317` |
| 22 | [Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach](#arxiv-2502.05171) | 2025 | +0.22 | 5/7 | `arxiv:2502.05171` |
| 23 | [Reinforcement Learning for Reasoning in Large Language Models with One Training Example](#arxiv-2504.20571) | 2025 | +0.21 | 4/7 | `arxiv:2504.20571` |
| 24 | [Physics of Language Models: Part 3.1, Knowledge Storage and Extraction](#arxiv-2309.14316) | 2023 | +0.21 | 4/7 | `arxiv:2309.14316` |
| 25 | [Evaluating the World Model Implicit in a Generative Model](#arxiv-2406.03689) | 2024 | +0.19 | 4/7 | `arxiv:2406.03689` |
| 26 | [The Reversal Curse: LLMs trained on "A is B" fail to learn "B is A"](#arxiv-2309.12288) | 2023 | +0.17 | 4/7 | `arxiv:2309.12288` |
| 27 | [Training Large Language Models to Reason in a Continuous Latent Space](#arxiv-2412.06769) | 2024 | +0.14 | 5/7 | `arxiv:2412.06769` |
| 28 | [Emergent Analogical Reasoning in Large Language Models](#arxiv-2212.09196) | 2022 | +0.13 | 5/7 | `arxiv:2212.09196` |
| 29 | [A Formal Comparison Between Chain of Thought and Latent Thought](#arxiv-2509.25239) | 2025 | +0.12 | 5/7 | `arxiv:2509.25239` |
| 30 | [How Do Large Language Models Acquire Factual Knowledge During Pretraining?](#arxiv-2406.11813) | 2024 | +0.10 | 5/7 | `arxiv:2406.11813` |
| 31 | [Transcendence: Generative Models Can Outperform The Experts That Train Them](#arxiv-2406.11741) | 2024 | +0.10 | 4/7 | `arxiv:2406.11741` |
| 32 | [Modular Arithmetic: Language Models Solve Math Digit by Digit](#arxiv-2508.02513) | 2025 | +0.09 | 6/7 | `arxiv:2508.02513` |
| 33 | [Why Can't Transformers Learn Multiplication? Reverse-Engineering Reveals Long-Range Dependency Pitfalls](#arxiv-2510.00184) | 2025 | +0.06 | 6/7 | `arxiv:2510.00184` |
| 34 | [Dissociating language and thought in large language models](#arxiv-2301.06627) | 2023 | +0.05 | 3/7 | `arxiv:2301.06627` |
| 35 | [LiveMathematicianBench: A Live Benchmark for Mathematician-Level Reasoning with Proof Sketches](#arxiv-2604.01754) | 2026 | +0.04 | 4/7 | `arxiv:2604.01754` |
| 36 | [Multimodal Chain-of-Thought Reasoning in Language Models](#arxiv-2302.00923) | 2023 | +0.04 | 5/7 | `arxiv:2302.00923` |
| 37 | [Emergent Capabilities Arise Randomly from Learning Sparse Attention Patterns](#arxiv-2606.25010) | 2026 | +0.03 | 4/7 | `arxiv:2606.25010` |
| 38 | [The Truth is in There: Improving Reasoning in Language Models with Layer-Selective Rank Reduction](#arxiv-2312.13558) | 2023 | +0.02 | 4/7 | `arxiv:2312.13558` |
| 39 | [Language Models Compare Quantities Using Number-specific and Unit-specific Heuristics](#arxiv-2606.03982) | 2026 | -0.01 | 4/7 | `arxiv:2606.03982` |
| 40 | [Evidence from formal logical reasoning reveals that the language of thought is not natural language](#doi-10.1073-pnas.2520095123) | 2026 | -0.08 | 5/7 | `doi:10.1073/pnas.2520095123` |
| 41 | [From Explicit CoT to Implicit CoT: Learning to Internalize CoT Step by Step](#arxiv-2405.14838) | 2024 | -0.09 | 4/7 | `arxiv:2405.14838` |
| 42 | [Language Models Are Capable of Metacognitive Monitoring and Control of Their Internal Activations](#arxiv-2505.13763) | 2025 | -0.09 | 4/7 | `arxiv:2505.13763` |
| 43 | [Can Large Reasoning Models Self-Train?](#arxiv-2505.21444) | 2025 | -0.12 | 2/7 | `arxiv:2505.21444` |
| 44 | [The Lookahead Limitation: Why Multi-Operand Addition is Hard for LLMs](#arxiv-2502.19981) | 2025 | -0.16 | 3/7 | `arxiv:2502.19981` |
| 45 | [A Mechanistic Analysis of Looped Reasoning Language Models](#arxiv-2604.11791) | 2026 | -0.16 | 3/7 | `arxiv:2604.11791` |
| 46 | [Language is primarily a tool for communication rather than thought](#doi-10.1038-s41586-024-07522-w) | 2024 | -0.17 | 4/5 | `doi:10.1038/s41586-024-07522-w` |
| 47 | [LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks](#arxiv-2402.01817) | 2024 | -0.20 | 2/7 | `arxiv:2402.01817` |
| 48 | [Knowledge Mechanisms in Large Language Models: A Survey and Perspective](#arxiv-2407.15017) | 2024 | -0.21 | 3/7 | `arxiv:2407.15017` |
| 49 | [Position: LLMs can't jump](#openreview-klU4737opt) | unknown | -0.25 | 2/7 | `openreview:klU4737opt` |
| 50 | [Competitive Programming with Large Reasoning Models](#arxiv-2502.06807) | 2025 | -0.26 | 4/7 | `arxiv:2502.06807` |
| 51 | [Why mathematics is set to be revolutionized by AI](#doi-10.1038-d41586-024-01413-w) | 2024 | -0.27 | 3/5 | `doi:10.1038/d41586-024-01413-w` |
| 52 | [Large Language Models Still Can't Plan / PlanBench (Kambhampati)](#openreview-wUU-7XTL5XO) | unknown | -0.30 | 2/7 | `openreview:wUU-7XTL5XO` |
| 53 | [AI-rithmetic](#arxiv-2602.10416) | 2026 | -0.41 | 2/7 | `arxiv:2602.10416` |
| 54 | [Scaling of Search and Learning: A Roadmap to Reproduce o1 from Reinforcement Learning Perspective](#arxiv-2412.14135) | 2024 | -0.67 | 0/7 | `arxiv:2412.14135` |

### Data, training, optimization

| rank | title | year | final | accept | key |
|---:|---|---|---:|---:|---|
| 1 | [Sharpness-Aware Minimization for Efficiently Improving Generalization](#arxiv-2010.01412) | 2020 | +0.58 | 5/7 | `arxiv:2010.01412` |
| 2 | [Tasks, stability, architecture, and compute: Training more effective learned optimizers, and using them to train themselves](#arxiv-2009.11243) | 2020 | +0.51 | 5/7 | `arxiv:2009.11243` |
| 3 | [Large Batch Optimization for Deep Learning: Training BERT in 76 minutes](#arxiv-1904.00962) | 2019 | +0.48 | 4/7 | `arxiv:1904.00962` |
| 4 | [Symbolic Discovery of Optimization Algorithms](#arxiv-2302.06675) | 2023 | +0.42 | 5/7 | `arxiv:2302.06675` |
| 5 | [Scaling Laws for Neural Language Models](#arxiv-2001.08361) | 2020 | +0.39 | 4/7 | `arxiv:2001.08361` |
| 6 | [Loss of plasticity in deep continual learning](#doi-10.1038-s41586-024-07711-7) | 2024 | +0.36 | 5/7 | `doi:10.1038/s41586-024-07711-7` |
| 7 | [The Loss Does Not See the Basis, but Adam Does](#arxiv-2608.05136) | 2026 | +0.34 | 6/7 | `arxiv:2608.05136` |
| 8 | [The Road Less Scheduled](#arxiv-2405.15682) | 2024 | +0.34 | 5/7 | `arxiv:2405.15682` |
| 9 | [The AdEMAMix Optimizer: Better, Faster, Older](#arxiv-2409.03137) | 2024 | +0.32 | 4/7 | `arxiv:2409.03137` |
| 10 | [Explorative Modeling: Unlocking a Third Pretraining Axis and End-to-End Generation](#arxiv-2607.27372) | 2026 | +0.29 | 7/7 | `arxiv:2607.27372` |
| 11 | [How much do language models memorize?](#arxiv-2505.24832) | 2025 | +0.26 | 6/7 | `arxiv:2505.24832` |
| 12 | [How Neural Networks Extrapolate: From Feedforward to Graph Neural Networks](#arxiv-2009.11848) | 2020 | +0.24 | 5/7 | `arxiv:2009.11848` |
| 13 | [Scaling Laws and Compute-Optimal Training Beyond Fixed Training Durations](#arxiv-2405.18392) | 2024 | +0.24 | 5/7 | `arxiv:2405.18392` |
| 14 | [Scaling Laws for Reward Model Overoptimization](#arxiv-2210.10760) | 2022 | +0.22 | 5/7 | `arxiv:2210.10760` |
| 15 | [Grokfast: Accelerated Grokking by Amplifying Slow Gradients](#arxiv-2405.20233) | 2024 | +0.18 | 3/7 | `arxiv:2405.20233` |
| 16 | [Learning Vision from Models Rivals Learning Vision from Data](#arxiv-2312.17742) | 2023 | +0.17 | 3/7 | `arxiv:2312.17742` |
| 17 | [On-Policy RL Meets Off-Policy Experts: Harmonizing Supervised Fine-Tuning and Reinforcement Learning via Dynamic Weighting](#arxiv-2508.11408) | 2025 | +0.16 | 5/7 | `arxiv:2508.11408` |
| 18 | [The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks](#arxiv-1803.03635) | 2018 | +0.16 | 3/7 | `arxiv:1803.03635` |
| 19 | [Perplexed by Perplexity: Perplexity-Based Data Pruning With Small Reference Models](#arxiv-2405.20541) | 2024 | +0.16 | 4/7 | `arxiv:2405.20541` |
| 20 | [Emergent properties with repeated examples](#arxiv-2410.07041) | 2024 | +0.09 | 5/7 | `arxiv:2410.07041` |
| 21 | [NorMuon: Making Muon more efficient and scalable](#arxiv-2510.05491) | 2025 | +0.06 | 6/7 | `arxiv:2510.05491` |
| 22 | [Sophia: A Scalable Stochastic Second-order Optimizer for Language Model Pre-training](#arxiv-2305.14342) | 2023 | +0.04 | 4/7 | `arxiv:2305.14342` |
| 23 | [Overcoming catastrophic forgetting in neural networks](#doi-10.1073-pnas.1611835114) | 2017 | +0.03 | 4/7 | `doi:10.1073/pnas.1611835114` |
| 24 | [No Train No Gain: Revisiting Efficient Training Algorithms For Transformer-based Language Models](#arxiv-2307.06440) | 2023 | +0.00 | 3/7 | `arxiv:2307.06440` |
| 25 | [Super-Convergence: Very Fast Training of Neural Networks Using Large Learning Rates](#arxiv-1708.07120) | 2017 | -0.01 | 3/7 | `arxiv:1708.07120` |
| 26 | [On the Information Bottleneck Theory of Deep Learning (Saxe et al.)](#openreview-ry_WPG-A-) | unknown | -0.01 | 5/7 | `openreview:ry_WPG-A-` |
| 27 | [gzip Predicts Data-dependent Scaling Laws](#arxiv-2405.16684) | 2024 | -0.04 | 3/7 | `arxiv:2405.16684` |
| 28 | [Cramming: Training a Language Model on a Single GPU in One Day](#arxiv-2212.14034) | 2022 | -0.08 | 3/7 | `arxiv:2212.14034` |
| 29 | [MetaOptimize: A Framework for Optimizing Step Sizes and Other Meta-parameters](#arxiv-2402.02342) | 2024 | -0.21 | 3/7 | `arxiv:2402.02342` |
| 30 | [Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved)](#arxiv-2507.12856) | 2025 | -0.24 | 3/7 | `arxiv:2507.12856` |
| 31 | [Continual Learning and Catastrophic Forgetting](#arxiv-2403.05175) | 2024 | -0.27 | 2/7 | `arxiv:2403.05175` |
| 32 | [Learning in High Dimension Always Amounts to Extrapolation](#arxiv-2110.09485) | 2021 | -0.30 | 1/7 | `arxiv:2110.09485` |
| 33 | [Self-Improving Pretraining: using post-trained models to pretrain better models](#arxiv-2601.21343) | 2026 | -0.32 | 3/7 | `arxiv:2601.21343` |
| 34 | [Cyclical Learning Rates for Training Neural Networks](#arxiv-1506.01186) | 2015 | -0.40 | 1/7 | `arxiv:1506.01186` |
| 35 | [Reinforcement Pre-Training](#arxiv-2506.08007) | 2025 | -0.42 | 3/7 | `arxiv:2506.08007` |
| 36 | [Continual Backprop: Stochastic Gradient Descent with Persistent Randomness](#arxiv-2108.06325) | 2021 | -0.48 | 0/7 | `arxiv:2108.06325` |
| 37 | [Measuring Catastrophic Forgetting in Neural Networks](#arxiv-1708.02072) | 2017 | -0.49 | 2/7 | `arxiv:1708.02072` |
| 38 | [Nested Learning: The Illusion of Deep Learning Architectures](#arxiv-2512.24695) | 2025 | -0.65 | 0/6 | `arxiv:2512.24695` |
| 39 | [Catastrophic Forgetting in Deep Learning: A Comprehensive Taxonomy](#arxiv-2312.10549) | 2023 | -0.66 | 0/7 | `arxiv:2312.10549` |
| 40 | [Step-size Optimization for Continual Learning](#arxiv-2401.17401) | 2024 | -0.68 | 1/6 | `arxiv:2401.17401` |

### Self-supervised learning and vision

| rank | title | year | final | accept | key |
|---:|---|---|---:|---:|---|
| 1 | [When Does LeJEPA Learn a World Model?](#arxiv-2605.26379) | 2026 | +0.62 | 6/7 | `arxiv:2605.26379` |
| 2 | [Emerging Properties in Self-Supervised Vision Transformers](#arxiv-2104.14294) | 2021 | +0.48 | 5/7 | `arxiv:2104.14294` |
| 3 | [Unsupervised Learning of Visual Features by Contrasting Cluster Assignments](#arxiv-2006.09882) | 2020 | +0.43 | 4/7 | `arxiv:2006.09882` |
| 4 | [ImageReward: Learning and Evaluating Human Preferences for Text-to-Image Generation](#arxiv-2304.05977) | 2023 | +0.43 | 5/7 | `arxiv:2304.05977` |
| 5 | [VISReg: Variance-Invariance-Sketching Regularization for JEPA training](#arxiv-2606.02572) | 2026 | +0.34 | 6/7 | `arxiv:2606.02572` |
| 6 | [LeJEPA: Provable and Scalable Self-Supervised Learning Without the Heuristics](#arxiv-2511.08544) | 2025 | +0.33 | 6/7 | `arxiv:2511.08544` |
| 7 | [Image as a Foreign Language: BEiT Pretraining for All Vision and Vision-Language Tasks](#arxiv-2208.10442) | 2022 | +0.24 | 5/7 | `arxiv:2208.10442` |
| 8 | [DINOv2: Learning Robust Visual Features without Supervision](#arxiv-2304.07193) | 2023 | +0.20 | 4/7 | `arxiv:2304.07193` |
| 9 | [Latent Consistency Models: Synthesizing High-Resolution Images with Few-Step Inference](#arxiv-2310.04378) | 2023 | +0.19 | 3/7 | `arxiv:2310.04378` |
| 10 | [Emu: Enhancing Image Generation Models Using Photogenic Needles in a Haystack](#arxiv-2309.15807) | 2023 | +0.19 | 4/7 | `arxiv:2309.15807` |
| 11 | [Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture](#arxiv-2301.08243) | 2023 | +0.18 | 4/7 | `arxiv:2301.08243` |
| 12 | [iBOT: Image BERT Pre-Training with Online Tokenizer](#arxiv-2111.07832) | 2021 | +0.14 | 4/7 | `arxiv:2111.07832` |
| 13 | [ELT: Elastic Looped Transformers for Visual Generation](#arxiv-2604.09168) | 2026 | +0.05 | 4/7 | `arxiv:2604.09168` |
| 14 | [Towards Universal Fake Image Detectors that Generalize Across Generative Models](#arxiv-2302.10174) | 2023 | +0.04 | 4/7 | `arxiv:2302.10174` |
| 15 | [The GAN is dead; long live the GAN! A Modern GAN Baseline](#arxiv-2501.05441) | 2025 | +0.03 | 5/7 | `arxiv:2501.05441` |
| 16 | [VICReg: Variance-Invariance-Covariance Regularization for Self-Supervised Learning](#arxiv-2105.04906) | 2021 | -0.08 | 3/7 | `arxiv:2105.04906` |
| 17 | [Tune-A-Video: One-Shot Tuning of Image Diffusion Models for Text-to-Video Generation](#arxiv-2212.11565) | 2022 | -0.25 | 3/7 | `arxiv:2212.11565` |
| 18 | [To Compress or Not to Compress- Self-Supervised Learning and Information Theory: A Review](#arxiv-2304.09355) | 2023 | -0.41 | 1/6 | `arxiv:2304.09355` |
| 19 | [A Cookbook of Self-Supervised Learning](#arxiv-2304.12210) | 2023 | -0.57 | 1/7 | `arxiv:2304.12210` |
| 20 | [A Path Towards Autonomous Machine Intelligence (LeCun, 2022)](#openreview-BZ5a1r-kVsf) | unknown | -0.61 | 2/6 | `openreview:BZ5a1r-kVsf` |

### Retrieval, embeddings, benchmarks

| rank | title | year | final | accept | key |
|---:|---|---|---:|---:|---|
| 1 | [Matryoshka Representation Learning](#arxiv-2205.13147) | 2022 | +0.59 | 6/7 | `arxiv:2205.13147` |
| 2 | [One Embedder, Any Task: Instruction-Finetuned Text Embeddings](#arxiv-2212.09741) | 2022 | +0.53 | 6/7 | `arxiv:2212.09741` |
| 3 | [Beyond the Imitation Game: Quantifying and extrapolating the capabilities of language models](#arxiv-2206.04615) | 2022 | +0.50 | 3/6 | `arxiv:2206.04615` |
| 4 | [Rainbow Teaming: Open-Ended Generation of Diverse Adversarial Prompts](#arxiv-2402.16822) | 2024 | +0.38 | 6/7 | `arxiv:2402.16822` |
| 5 | [MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering](#arxiv-2410.07095) | 2024 | +0.31 | 4/7 | `arxiv:2410.07095` |
| 6 | [Large Dual Encoders Are Generalizable Retrievers](#arxiv-2112.07899) | 2021 | +0.30 | 4/7 | `arxiv:2112.07899` |
| 7 | [Demonstrate-Search-Predict: Composing retrieval and language models for knowledge-intensive NLP](#arxiv-2212.14024) | 2022 | +0.30 | 6/7 | `arxiv:2212.14024` |
| 8 | [CEO-Bench: Can Agents Play the Long Game?](#arxiv-2606.18543) | 2026 | +0.17 | 5/7 | `arxiv:2606.18543` |
| 9 | [Super-NaturalInstructions: Generalization via Declarative Instructions on 1600+ NLP Tasks](#acl-2022.emnlp-main.340) | unknown | +0.10 | 4/6 | `acl:2022.emnlp-main.340` |
| 10 | [Did Aristotle Use a Laptop? A Question Answering Benchmark with Implicit Reasoning Strategies](#arxiv-2101.02235) | 2021 | +0.07 | 5/7 | `arxiv:2101.02235` |
| 11 | [Can Generalist Foundation Models Outcompete Special-Purpose Tuning? Case Study in Medicine](#arxiv-2311.16452) | 2023 | +0.05 | 5/7 | `arxiv:2311.16452` |
| 12 | [Artifacts or Abduction: How Do LLMs Answer Multiple-Choice Questions Without the Question?](#arxiv-2402.12483) | 2024 | -0.04 | 4/7 | `arxiv:2402.12483` |
| 13 | [PRIMERA: Pyramid-based Masked Sentence Pre-training for Multi-document Summarization](#acl-2022.acl-long.360) | unknown | -0.08 | 3/7 | `acl:2022.acl-long.360` |
| 14 | [Learning to Compress Prompts with Gist Tokens](#arxiv-2304.08467) | 2023 | -0.08 | 4/7 | `arxiv:2304.08467` |
| 15 | [Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution](#arxiv-2309.16797) | 2023 | -0.20 | 4/7 | `arxiv:2309.16797` |
| 16 | [People cannot distinguish GPT-4 from a human in a Turing test](#arxiv-2405.08007) | 2024 | -0.28 | 1/7 | `arxiv:2405.08007` |
| 17 | [A System for Answering Simple Questions in Multiple Languages](#acl-2023.acl-demo.51) | unknown | -0.28 | 2/7 | `acl:2023.acl-demo.51` |

### Agents, open-endedness, AGI

| rank | title | year | final | accept | key |
|---:|---|---|---:|---:|---|
| 1 | [Robust agents learn causal world models (ICLR 2024 best paper)](#openreview-pOoKI3ouv1) | unknown | +0.64 | 6/7 | `openreview:pOoKI3ouv1` |
| 2 | [Mathematical discoveries from program search with large language models](#doi-10.1038-s41586-023-06924-6) | 2023 | +0.54 | 6/7 | `doi:10.1038/s41586-023-06924-6` |
| 3 | [MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory](#arxiv-2601.03192) | 2026 | +0.46 | 6/7 | `arxiv:2601.03192` |
| 4 | [Learning Formal Mathematics From Intrinsic Motivation](#arxiv-2407.00695) | 2024 | +0.43 | 3/7 | `arxiv:2407.00695` |
| 5 | [MemEvolve: Meta-Evolution of Agent Memory Systems](#arxiv-2512.18746) | 2025 | +0.40 | 5/7 | `arxiv:2512.18746` |
| 6 | [SPADE: Self-Play in Adaptive Synthetic Executable Environments](#arxiv-2608.19197) | 2026 | +0.39 | 6/7 | `arxiv:2608.19197` |
| 7 | [Language Agents as Optimizable Graphs](#arxiv-2402.16823) | 2024 | +0.29 | 3/7 | `arxiv:2402.16823` |
| 8 | [Self-Improvements in Modern Agentic Systems: A Survey](#arxiv-2607.13104) | 2026 | +0.27 | 6/7 | `arxiv:2607.13104` |
| 9 | [Automated Design of Agentic Systems](#arxiv-2408.08435) | 2024 | +0.13 | 4/7 | `arxiv:2408.08435` |
| 10 | [Learning to Continually Learn via Meta-learning Agentic Memory Designs](#arxiv-2602.07755) | 2026 | +0.11 | 6/7 | `arxiv:2602.07755` |
| 11 | [Propose, Solve, Verify: Self-Play Through Formal Verification](#arxiv-2512.18160) | 2025 | +0.11 | 5/7 | `arxiv:2512.18160` |
| 12 | [Competition and Attraction Improve Model Fusion](#arxiv-2508.16204) | 2025 | +0.05 | 4/7 | `arxiv:2508.16204` |
| 13 | [Harnessing Agentic Evolution](#arxiv-2605.13821) | 2026 | +0.05 | 5/7 | `arxiv:2605.13821` |
| 14 | [Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents](#arxiv-2505.22954) | 2025 | +0.05 | 4/7 | `arxiv:2505.22954` |
| 15 | [Dr. Zero: Self-Evolving Search Agents without Training Data](#arxiv-2601.07055) | 2026 | +0.05 | 5/7 | `arxiv:2601.07055` |
| 16 | [Meta Context Engineering via Agentic Skill Evolution](#arxiv-2601.21557) | 2026 | +0.03 | 5/7 | `arxiv:2601.21557` |
| 17 | [Hyperagents](#arxiv-2603.19461) | 2026 | +0.02 | 6/7 | `arxiv:2603.19461` |
| 18 | [Paired Open-Ended Trailblazer (POET): Endlessly Generating Increasingly Complex and Diverse Learning Environments and Their Solutions](#arxiv-1901.01753) | 2019 | -0.02 | 1/7 | `arxiv:1901.01753` |
| 19 | [Gödel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement](#arxiv-2410.04444) | 2024 | -0.05 | 3/7 | `arxiv:2410.04444` |
| 20 | [A Definition of Open-Ended Learning Problems for Goal-Conditioned Agents](#arxiv-2311.00344) | 2023 | -0.09 | 3/7 | `arxiv:2311.00344` |
| 21 | [Ouroboros: A Self-Developing Frontier Coding Agent with Reviewed Core Evolution](#arxiv-2608.08311) | 2026 | -0.12 | 3/7 | `arxiv:2608.08311` |
| 22 | [AlphaGo Moment for Model Architecture Discovery](#arxiv-2507.18074) | 2025 | -0.22 | 3/7 | `arxiv:2507.18074` |
| 23 | [Open-Endedness is Essential for Artificial Superhuman Intelligence](#arxiv-2406.04268) | 2024 | -0.25 | 2/7 | `arxiv:2406.04268` |
| 24 | [Toward Training Superintelligent Software Agents through Self-Play SWE-RL](#arxiv-2512.18552) | 2025 | -0.25 | 3/7 | `arxiv:2512.18552` |
| 25 | [AI-GAs: AI-generating algorithms, an alternate paradigm for producing general artificial intelligence](#arxiv-1905.10985) | 2019 | -0.28 | 1/7 | `arxiv:1905.10985` |
| 26 | [Vending-Bench: A Benchmark for Long-Term Coherence of Autonomous Agents](#arxiv-2502.15840) | 2025 | -0.30 | 3/7 | `arxiv:2502.15840` |
| 27 | [Levels of AGI for Operationalizing Progress on the Path to AGI](#arxiv-2311.02462) | 2023 | -0.31 | 2/7 | `arxiv:2311.02462` |
| 28 | [What Does It Take to Be a Good AI Research Agent? Studying the Role of Ideation Diversity](#arxiv-2511.15593) | 2025 | -0.45 | 2/7 | `arxiv:2511.15593` |
| 29 | [A social path to human-like artificial intelligence](#doi-10.1038-s42256-023-00754-x) | 2023 | -0.49 | 1/7 | `doi:10.1038/s42256-023-00754-x` |
| 30 | [AI Finds A Way](#arxiv-2608.23875) | 2026 | -0.57 | 2/7 | `arxiv:2608.23875` |
| 31 | [Self-Programming AI: Code-Learning Agents for Autonomous Refactoring and Architectural Evolution](#doi-10.21203-rs.3.rs-6688473-v1) | 2025 | -0.72 | 2/7 | `doi:10.21203/rs.3.rs-6688473/v1` |

### Harness

| rank | title | year | final | accept | key |
|---:|---|---|---:|---:|---|
| 1 | [Structured Scaling of AI Discovery Across Diverse Scientific Domains](#arxiv-2604.19341) | 2026 | +0.65 | 6/7 | `arxiv:2604.19341` |
| 2 | [Meta-Harness: End-to-End Optimization of Model Harnesses](#arxiv-2603.28052) | 2026 | +0.31 | 6/7 | `arxiv:2603.28052` |
| 3 | [Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System Deployment on Open-Ended Task Streams](#arxiv-2606.01770) | 2026 | +0.23 | 5/7 | `arxiv:2606.01770` |
| 4 | [Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses](#arxiv-2604.25850) | 2026 | +0.08 | 3/7 | `arxiv:2604.25850` |
| 5 | [HarnessDev: Can LLMs Create and Evolve Their Own Agent Harness?](#arxiv-2609.01437) | 2026 | -0.04 | 4/7 | `arxiv:2609.01437` |
| 6 | [Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering](#arxiv-2604.08224) | 2026 | -0.20 | 3/7 | `arxiv:2604.08224` |

### AI safety and consciousness

| rank | title | year | final | accept | key |
|---:|---|---|---:|---:|---|
| 1 | [Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming](#arxiv-2501.18837) | 2025 | +0.13 | 6/7 | `arxiv:2501.18837` |
| 2 | [Sparse Autoencoders Find Highly Interpretable Features in Language Models](#arxiv-2309.08600) | 2023 | +0.09 | 4/7 | `arxiv:2309.08600` |
| 3 | [When Activation Oracles Learn Not to Read: Concept-Specific Blind Spots in Fine-Tuned Oracles](#arxiv-2607.23379) | 2026 | +0.08 | 4/7 | `arxiv:2607.23379` |
| 4 | [Optimal Policies Tend to Seek Power](#arxiv-1912.01683) | 2019 | +0.07 | 3/7 | `arxiv:1912.01683` |
| 5 | [Is Power-Seeking AI an Existential Risk?](#arxiv-2206.13353) | 2022 | +0.01 | 3/7 | `arxiv:2206.13353` |
| 6 | [Consciousness in Artificial Intelligence: Insights from the Science of Consciousness](#arxiv-2308.08708) | 2023 | -0.03 | 4/7 | `arxiv:2308.08708` |
| 7 | [Parametrically Retargetable Decision-Makers Tend To Seek Power](#arxiv-2206.13477) | 2022 | -0.10 | 3/7 | `arxiv:2206.13477` |
| 8 | [Could a Large Language Model be Conscious?](#arxiv-2303.07103) | 2023 | -0.25 | 3/6 | `arxiv:2303.07103` |
| 9 | [Is Evaluation Awareness Just Format Sensitivity? Limitations of Probe-Based Evidence under Controlled Prompt Structure](#arxiv-2603.19426) | 2026 | -0.30 | 5/7 | `arxiv:2603.19426` |
| 10 | [Power-seeking can be probable and predictive for trained agents](#arxiv-2304.06528) | 2023 | -0.34 | 3/7 | `arxiv:2304.06528` |
| 11 | [Detecting Strategic Deception Using Linear Probes](#arxiv-2502.03407) | 2025 | -0.40 | 3/7 | `arxiv:2502.03407` |
| 12 | [Palatable Conceptions of Disembodied Being](#arxiv-2503.16348) | 2025 | -0.72 | 2/7 | `arxiv:2503.16348` |

### NeuroAI

| rank | title | year | final | accept | key |
|---:|---|---|---:|---:|---|
| 1 | [From Tokens to Thoughts: How LLMs and Humans Trade Compression for Meaning](#arxiv-2505.17117) | 2025 | +0.43 | 7/7 | `arxiv:2505.17117` |
| 2 | [Neural spiking for causal inference and learning](#doi-10.1371-journal.pcbi.1011005) | 2023 | +0.23 | 4/6 | `doi:10.1371/journal.pcbi.1011005` |
| 3 | [Attractor and integrator networks in the brain](#arxiv-2112.03978) | 2021 | +0.14 | 5/7 | `arxiv:2112.03978` |
| 4 | [Sleep prevents catastrophic forgetting in spiking neural networks by forming a joint synaptic weight representation](#doi-10.1371-journal.pcbi.1010628) | 2022 | +0.12 | 4/7 | `doi:10.1371/journal.pcbi.1010628` |
| 5 | [MetaWorm: An Integrative Data-Driven Model Simulating <i>C. elegans</i> Brain, Body and Environment Interactions](#doi-10.1101-2024.02.22.581686) | 2024 | +0.10 | 4/7 | `doi:10.1101/2024.02.22.581686` |
| 6 | [Emergence of belief-like representations through reinforcement learning](#doi-10.1101-2023.04.04.535512) | 2023 | +0.02 | 2/7 | `doi:10.1101/2023.04.04.535512` |
| 7 | [Relating transformers to models and neural representations of the hippocampal formation](#arxiv-2112.04035) | 2021 | +0.01 | 3/7 | `arxiv:2112.04035` |
| 8 | [Toward Next-Generation Artificial Intelligence: Catalyzing the NeuroAI Revolution](#arxiv-2210.08340) | 2022 | -0.06 | 3/7 | `arxiv:2210.08340` |
| 9 | [This is how the Neocortex Learns](#arxiv-2606.08720) | 2026 | -0.21 | 3/7 | `arxiv:2606.08720` |
| 10 | [Correspondence between neuroevolution and gradient descent](#doi-10.1038-s41467-021-26568-2) | 2021 | -0.32 | 3/7 | `doi:10.1038/s41467-021-26568-2` |

### Representation alignment

| rank | title | year | final | accept | key |
|---:|---|---|---:|---:|---|
| 1 | [Comparing representational geometries using whitened unbiased-distance-matrix similarity](#arxiv-2007.02789) | 2020 | +0.71 | 5/7 | `arxiv:2007.02789` |
| 2 | [Estimating Neural Representation Alignment from Sparsely Sampled Inputs and Features](#arxiv-2502.15104) | 2025 | +0.50 | 6/7 | `arxiv:2502.15104` |
| 3 | [Revisiting the Platonic Representation Hypothesis: An Aristotelian View](#arxiv-2602.14486) | 2026 | +0.34 | 5/7 | `arxiv:2602.14486` |
| 4 | [Proof of a perfect platonic representation hypothesis](#arxiv-2507.01098) | 2025 | -0.09 | 3/7 | `arxiv:2507.01098` |
| 5 | [The Platonic Representation Hypothesis](#arxiv-2405.07987) | 2024 | -0.11 | 3/6 | `arxiv:2405.07987` |
| 6 | [Correcting Biased Centered Kernel Alignment Measures in Biological and Artificial Neural Networks](#arxiv-2405.01012) | 2024 | -0.52 | 1/7 | `arxiv:2405.01012` |

### Finance

| rank | title | year | final | accept | key |
|---:|---|---|---:|---:|---|
| 1 | [INVESTORBENCH: A Benchmark for Financial Decision-Making Tasks with LLM-based Agent](#acl-2025.acl-long.126) | unknown | -0.18 | 2/7 | `acl:2025.acl-long.126` |
| 2 | [A Deep Reinforcement Learning Framework for the Financial Portfolio Management Problem](#arxiv-1706.10059) | 2017 | -0.65 | 0/7 | `arxiv:1706.10059` |
| 3 | [Applications of deep learning in stock market prediction: recent progress](#arxiv-2003.01859) | 2020 | -0.72 | 1/7 | `arxiv:2003.01859` |
| 4 | [Financial Trading as a Game: A Deep Reinforcement Learning Approach](#arxiv-1807.02787) | 2018 | -0.74 | 1/7 | `arxiv:1807.02787` |

### Books

| rank | title | year | final | accept | key |
|---:|---|---|---:|---:|---|
| 1 | [Reinforcement Learning Textbook](#arxiv-2201.09746) | 2022 | -0.59 | 1/7 | `arxiv:2201.09746` |
| 2 | [Deep Learning Interviews: Hundreds of fully solved job interview questions from a wide range of key topics in AI](#arxiv-2201.00650) | 2021 | -0.83 | 0/5 | `arxiv:2201.00650` |

### Other

| rank | title | year | final | accept | key |
|---:|---|---|---:|---:|---|
| 1 | [TPU v4: An Optically Reconfigurable Supercomputer for Machine Learning with Hardware Support for Embeddings](#arxiv-2304.01433) | 2023 | +0.02 | 3/6 | `arxiv:2304.01433` |
| 2 | [Inverse-designed low-index-contrast structures on a silicon photonics platform for vector–matrix multiplication](#doi-10.1038-s41566-024-01394-2) | 2024 | -0.13 | 2/6 | `doi:10.1038/s41566-024-01394-2` |
| 3 | [Fully parallel optical matrix-matrix multiplication](#arxiv-2309.10232) | 2023 | -0.77 | 0/7 | `arxiv:2309.10232` |

## DROP

`final_score` < -0.2 with conf >= 0.5 and impact_z below +0.5. Not a raw accept-vote count.

| title | section | year | final | conf | impact | accept |
|---|---|---|---:|---:|---:|---:|
| [Fully parallel optical matrix-matrix multiplication](#arxiv-2309.10232) | Other | 2023 | -0.77 | 1.00 | -1.90 | 0/7 |
| [Financial Trading as a Game: A Deep Reinforcement Learning Approach](#arxiv-1807.02787) | Finance | 2018 | -0.74 | 1.00 | -1.93 | 1/7 |
| [Palatable Conceptions of Disembodied Being](#arxiv-2503.16348) | AI safety and consciousness | 2025 | -0.72 | 1.00 | -2.39 | 2/7 |
| [Applications of deep learning in stock market prediction: recent progress](#arxiv-2003.01859) | Finance | 2020 | -0.72 | 1.00 | +0.27 | 1/7 |
| [Self-Programming AI: Code-Learning Agents for Autonomous Refactoring and Architectural Evolution](#doi-10.21203-rs.3.rs-6688473-v1) | Agents, open-endedness, AGI | 2025 | -0.72 | 1.00 | -0.31 | 2/7 |
| [Step-size Optimization for Continual Learning](#arxiv-2401.17401) | Data, training, optimization | 2024 | -0.68 | 0.91 | -2.26 | 1/6 |
| [Scaling of Search and Learning: A Roadmap to Reproduce o1 from Reinforcement Learning Perspective](#arxiv-2412.14135) | Reasoning and the "physics" of language models | 2024 | -0.67 | 1.00 | -1.58 | 0/7 |
| [Catastrophic Forgetting in Deep Learning: A Comprehensive Taxonomy](#arxiv-2312.10549) | Data, training, optimization | 2023 | -0.66 | 1.00 | -0.09 | 0/7 |
| [A Deep Reinforcement Learning Framework for the Financial Portfolio Management Problem](#arxiv-1706.10059) | Finance | 2017 | -0.65 | 1.00 | -2.21 | 0/7 |
| [Nested Learning: The Illusion of Deep Learning Architectures](#arxiv-2512.24695) | Data, training, optimization | 2025 | -0.65 | 0.82 | -2.10 | 0/6 |
| [A Path Towards Autonomous Machine Intelligence (LeCun, 2022)](#openreview-BZ5a1r-kVsf) | Self-supervised learning and vision | unknown | -0.61 | 0.91 | +0.06 | 2/6 |
| [Reinforcement Learning Textbook](#arxiv-2201.09746) | Books | 2022 | -0.59 | 0.62 | -0.58 | 1/7 |
| [GLU Variants Improve Transformer](#arxiv-2002.05202) | LLMs: architectures, context, training | 2020 | -0.58 | 1.00 | -1.06 | 1/7 |
| [A Cookbook of Self-Supervised Learning](#arxiv-2304.12210) | Self-supervised learning and vision | 2023 | -0.57 | 1.00 | +0.07 | 1/7 |
| [AI Finds A Way](#arxiv-2608.23875) | Agents, open-endedness, AGI | 2026 | -0.57 | 1.00 | -0.56 | 2/7 |
| [Benchmarking Batch Deep Reinforcement Learning Algorithms](#arxiv-1910.01708) | Reinforcement learning | 2019 | -0.56 | 1.00 | -1.45 | 2/7 |
| [Evolutionary Strategies lead to Catastrophic Forgetting in LLMs](#arxiv-2601.20861) | Post-training | 2026 | -0.54 | 1.00 | -1.33 | 3/7 |
| [Correcting Biased Centered Kernel Alignment Measures in Biological and Artificial Neural Networks](#arxiv-2405.01012) | Representation alignment | 2024 | -0.52 | 1.00 | -1.44 | 1/7 |
| [A Minimalist Approach to Offline Reinforcement Learning](#arxiv-2106.06860) | Reinforcement learning | 2021 | -0.49 | 1.00 | -0.69 | 3/7 |
| [Measuring Catastrophic Forgetting in Neural Networks](#arxiv-1708.02072) | Data, training, optimization | 2017 | -0.49 | 1.00 | -0.43 | 2/7 |
| [A social path to human-like artificial intelligence](#doi-10.1038-s42256-023-00754-x) | Agents, open-endedness, AGI | 2023 | -0.49 | 1.00 | -1.92 | 1/7 |
| [Continual Backprop: Stochastic Gradient Descent with Persistent Randomness](#arxiv-2108.06325) | Data, training, optimization | 2021 | -0.48 | 1.00 | -1.87 | 0/7 |
| [Meta-Reinforcement Learning with Zero-Shot RL](#openreview-XyGJJ4FPoX) | Reinforcement learning | unknown | -0.47 | 1.00 | -0.89 | 0/7 |
| [What Does It Take to Be a Good AI Research Agent? Studying the Role of Ideation Diversity](#arxiv-2511.15593) | Agents, open-endedness, AGI | 2025 | -0.45 | 1.00 | -1.51 | 2/7 |
| [Reinforcement Pre-Training](#arxiv-2506.08007) | Data, training, optimization | 2025 | -0.42 | 1.00 | -1.06 | 3/7 |
| [Your Transformer is Secretly Linear](#arxiv-2405.12250) | LLMs: architectures, context, training | 2024 | -0.41 | 1.00 | +0.06 | 3/7 |
| [AI-rithmetic](#arxiv-2602.10416) | Reasoning and the "physics" of language models | 2026 | -0.41 | 1.00 | -0.07 | 2/7 |
| [To Compress or Not to Compress- Self-Supervised Learning and Information Theory: A Review](#arxiv-2304.09355) | Self-supervised learning and vision | 2023 | -0.41 | 0.91 | -0.23 | 1/6 |
| [Cyclical Learning Rates for Training Neural Networks](#arxiv-1506.01186) | Data, training, optimization | 2015 | -0.40 | 1.00 | -0.25 | 1/7 |
| [Detecting Strategic Deception Using Linear Probes](#arxiv-2502.03407) | AI safety and consciousness | 2025 | -0.40 | 1.00 | +0.23 | 3/7 |
| [BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](#arxiv-2608.09888) | Post-training | 2026 | -0.35 | 1.00 | -0.46 | 2/7 |
| [Power-seeking can be probable and predictive for trained agents](#arxiv-2304.06528) | AI safety and consciousness | 2023 | -0.34 | 1.00 | +0.28 | 3/7 |
| [DAPO: An Open-Source LLM Reinforcement Learning System at Scale](#arxiv-2503.14476) | Post-training | 2025 | -0.32 | 1.00 | +0.32 | 3/7 |
| [Correspondence between neuroevolution and gradient descent](#doi-10.1038-s41467-021-26568-2) | NeuroAI | 2021 | -0.32 | 1.00 | -1.16 | 3/7 |
| [Self-Improving Pretraining: using post-trained models to pretrain better models](#arxiv-2601.21343) | Data, training, optimization | 2026 | -0.32 | 1.00 | -0.43 | 3/7 |
| [Levels of AGI for Operationalizing Progress on the Path to AGI](#arxiv-2311.02462) | Agents, open-endedness, AGI | 2023 | -0.31 | 1.00 | -0.29 | 2/7 |
| [Learning in High Dimension Always Amounts to Extrapolation](#arxiv-2110.09485) | Data, training, optimization | 2021 | -0.30 | 1.00 | -0.45 | 1/7 |
| [T5Gemma 2: Seeing, Reading, and Understanding Longer](#arxiv-2512.14856) | LLMs: architectures, context, training | 2025 | -0.30 | 1.00 | -0.14 | 2/7 |
| [Energy Transformer](#arxiv-2302.07253) | LLMs: architectures, context, training | 2023 | -0.30 | 1.00 | -0.76 | 4/7 |
| [Is Evaluation Awareness Just Format Sensitivity? Limitations of Probe-Based Evidence under Controlled Prompt Structure](#arxiv-2603.19426) | AI safety and consciousness | 2026 | -0.30 | 1.00 | -1.54 | 5/7 |
| [Vending-Bench: A Benchmark for Long-Term Coherence of Autonomous Agents](#arxiv-2502.15840) | Agents, open-endedness, AGI | 2025 | -0.30 | 1.00 | -0.26 | 3/7 |
| [Large Language Models Still Can't Plan / PlanBench (Kambhampati)](#openreview-wUU-7XTL5XO) | Reasoning and the "physics" of language models | unknown | -0.30 | 1.00 | +0.29 | 2/7 |
| [A System for Answering Simple Questions in Multiple Languages](#acl-2023.acl-demo.51) | Retrieval, embeddings, benchmarks | unknown | -0.28 | 0.91 | -0.97 | 2/7 |
| [AI-GAs: AI-generating algorithms, an alternate paradigm for producing general artificial intelligence](#arxiv-1905.10985) | Agents, open-endedness, AGI | 2019 | -0.28 | 1.00 | -0.34 | 1/7 |
| [Continual Learning and Catastrophic Forgetting](#arxiv-2403.05175) | Data, training, optimization | 2024 | -0.27 | 1.00 | -1.11 | 2/7 |
| [Revisiting Rainbow: Promoting more Insightful and Inclusive Deep Reinforcement Learning Research](#arxiv-2011.14826) | Reinforcement learning | 2020 | -0.26 | 1.00 | -1.46 | 1/7 |
| [Weight-Space Geometry of Offline Reasoning Training](#arxiv-2606.23740) | Post-training | 2026 | -0.25 | 1.00 | -0.91 | 2/7 |
| [Toward Training Superintelligent Software Agents through Self-Play SWE-RL](#arxiv-2512.18552) | Agents, open-endedness, AGI | 2025 | -0.25 | 1.00 | -0.56 | 3/7 |
| [Position: LLMs can't jump](#openreview-klU4737opt) | Reasoning and the "physics" of language models | unknown | -0.25 | 1.00 | -1.35 | 2/7 |
| [Open-Endedness is Essential for Artificial Superhuman Intelligence](#arxiv-2406.04268) | Agents, open-endedness, AGI | 2024 | -0.25 | 1.00 | +0.33 | 2/7 |
| [Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved)](#arxiv-2507.12856) | Data, training, optimization | 2025 | -0.24 | 1.00 | -1.96 | 3/7 |
| [Klear-Reasoner: Advancing Reasoning Capability via Gradient-Preserving Clipping Policy Optimization](#arxiv-2508.07629) | Post-training | 2025 | -0.23 | 0.82 | -0.88 | 3/6 |
| [MetaOptimize: A Framework for Optimizing Step Sizes and Other Meta-parameters](#arxiv-2402.02342) | Data, training, optimization | 2024 | -0.21 | 1.00 | -1.37 | 3/7 |
| [This is how the Neocortex Learns](#arxiv-2606.08720) | NeuroAI | 2026 | -0.21 | 0.91 | -1.71 | 3/7 |
| [LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks](#arxiv-2402.01817) | Reasoning and the "physics" of language models | 2024 | -0.20 | 1.00 | -0.08 | 2/7 |

## WATCH

Missing impact_z, conf < 0.5, |final_score| <= 0.2, or low score with high predicted impact. Showing 40 of 156.

| title | section | year | final | conf | impact | accept |
|---|---|---|---:|---:|---:|---:|
| [Deep Learning Interviews: Hundreds of fully solved job interview questions from a wide range of key topics in AI](#arxiv-2201.00650) | Books | 2021 | -0.83 | 0.43 | -1.39 | 0/5 |
| [Offline Reinforcement Learning: Tutorial, Review, and Perspectives on Open Problems](#arxiv-2005.01643) | Reinforcement learning | 2020 | -0.42 | 1.00 | +0.73 | 0/7 |
| [Addressing Function Approximation Error in Actor-Critic Methods](#arxiv-1802.09477) | Reinforcement learning | 2018 | -0.37 | 0.46 | -1.14 | 1/4 |
| [xLSTM: Extended Long Short-Term Memory](#arxiv-2405.04517) | LLMs: architectures, context, training | 2024 | -0.33 | 0.95 | +0.60 | 2/7 |
| [People cannot distinguish GPT-4 from a human in a Turing test](#arxiv-2405.08007) | Retrieval, embeddings, benchmarks | 2024 | -0.28 | 1.00 | +1.95 | 1/7 |
| [Why mathematics is set to be revolutionized by AI](#doi-10.1038-d41586-024-01413-w) | Reasoning and the "physics" of language models | 2024 | -0.27 | 0.44 | -1.40 | 3/5 |
| [Competitive Programming with Large Reasoning Models](#arxiv-2502.06807) | Reasoning and the "physics" of language models | 2025 | -0.26 | 1.00 | +0.65 | 4/7 |
| [Could a Large Language Model be Conscious?](#arxiv-2303.07103) | AI safety and consciousness | 2023 | -0.25 | 0.91 | +0.69 | 3/6 |
| [Tune-A-Video: One-Shot Tuning of Image Diffusion Models for Text-to-Video Generation](#arxiv-2212.11565) | Self-supervised learning and vision | 2022 | -0.25 | 1.00 | +0.85 | 3/7 |
| [AlphaGo Moment for Model Architecture Discovery](#arxiv-2507.18074) | Agents, open-endedness, AGI | 2025 | -0.22 | 1.00 | +1.17 | 3/7 |
| [Knowledge Mechanisms in Large Language Models: A Survey and Perspective](#arxiv-2407.15017) | Reasoning and the "physics" of language models | 2024 | -0.21 | 1.00 | +0.67 | 3/7 |
| [Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution](#arxiv-2309.16797) | Retrieval, embeddings, benchmarks | 2023 | -0.20 | 1.00 | +0.57 | 4/7 |
| [Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering](#arxiv-2604.08224) | Harness | 2026 | -0.20 | 1.00 | +1.32 | 3/7 |
| [INVESTORBENCH: A Benchmark for Financial Decision-Making Tasks with LLM-based Agent](#acl-2025.acl-long.126) | Finance | unknown | -0.18 | 0.91 | -0.08 | 2/7 |
| [Language is primarily a tool for communication rather than thought](#doi-10.1038-s41586-024-07522-w) | Reasoning and the "physics" of language models | 2024 | -0.17 | 0.65 | -2.67 | 4/5 |
| [Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs?](#arxiv-2603.24472) | Post-training | 2026 | -0.17 | 1.00 | +0.19 | 3/7 |
| [A Mechanistic Analysis of Looped Reasoning Language Models](#arxiv-2604.11791) | Reasoning and the "physics" of language models | 2026 | -0.16 | 1.00 | -1.42 | 3/7 |
| [The Lookahead Limitation: Why Multi-Operand Addition is Hard for LLMs](#arxiv-2502.19981) | Reasoning and the "physics" of language models | 2025 | -0.16 | 1.00 | +0.68 | 3/7 |
| [Latent Cache Flow: Model-to-Model Communication Without Text](#arxiv-2605.22863) | LLMs: architectures, context, training | 2026 | -0.16 | 1.00 | -0.76 | 4/7 |
| [Inverse-designed low-index-contrast structures on a silicon photonics platform for vector–matrix multiplication](#doi-10.1038-s41566-024-01394-2) | Other | 2024 | -0.13 | 0.82 | -1.61 | 2/6 |
| [Towards General-Purpose Model-Free Reinforcement Learning](#arxiv-2501.16142) | Reinforcement learning | 2025 | -0.13 | 1.00 | -1.07 | 5/7 |
| [Can Large Reasoning Models Self-Train?](#arxiv-2505.21444) | Reasoning and the "physics" of language models | 2025 | -0.12 | 1.00 | -0.88 | 2/7 |
| [Ouroboros: A Self-Developing Frontier Coding Agent with Reviewed Core Evolution](#arxiv-2608.08311) | Agents, open-endedness, AGI | 2026 | -0.12 | 1.00 | -0.71 | 3/7 |
| [The Platonic Representation Hypothesis](#arxiv-2405.07987) | Representation alignment | 2024 | -0.11 | 0.82 | -0.03 | 3/6 |
| [It Takes Two: Your GRPO Is Secretly DPO](#arxiv-2510.00977) | Post-training | 2025 | -0.10 | 1.00 | -1.37 | 5/7 |
| [Parametrically Retargetable Decision-Makers Tend To Seek Power](#arxiv-2206.13477) | AI safety and consciousness | 2022 | -0.10 | 1.00 | +1.00 | 3/7 |
| [RIFT: A RubrIc Failure Mode Taxonomy and Automated Diagnostics](#arxiv-2604.01375) | Post-training | 2026 | -0.10 | 1.00 | -0.29 | 3/7 |
| [A Definition of Open-Ended Learning Problems for Goal-Conditioned Agents](#arxiv-2311.00344) | Agents, open-endedness, AGI | 2023 | -0.09 | 1.00 | -1.59 | 3/7 |
| [Proof of a perfect platonic representation hypothesis](#arxiv-2507.01098) | Representation alignment | 2025 | -0.09 | 1.00 | -2.74 | 3/7 |
| [Language Models Are Capable of Metacognitive Monitoring and Control of Their Internal Activations](#arxiv-2505.13763) | Reasoning and the "physics" of language models | 2025 | -0.09 | 1.00 | +0.03 | 4/7 |
| [TransformerFAM: Feedback attention is working memory](#arxiv-2404.09173) | LLMs: architectures, context, training | 2024 | -0.09 | 1.00 | +0.33 | 3/7 |
| [From Explicit CoT to Implicit CoT: Learning to Internalize CoT Step by Step](#arxiv-2405.14838) | Reasoning and the "physics" of language models | 2024 | -0.09 | 1.00 | -0.02 | 4/7 |
| [Cramming: Training a Language Model on a Single GPU in One Day](#arxiv-2212.14034) | Data, training, optimization | 2022 | -0.08 | 1.00 | -0.93 | 3/7 |
| [Self-Distillation Enables Continual Learning](#arxiv-2601.19897) | Post-training | 2026 | -0.08 | 1.00 | +0.66 | 6/7 |
| [Learning to Compress Prompts with Gist Tokens](#arxiv-2304.08467) | Retrieval, embeddings, benchmarks | 2023 | -0.08 | 1.00 | +0.12 | 4/7 |
| [Evidence from formal logical reasoning reveals that the language of thought is not natural language](#doi-10.1073-pnas.2520095123) | Reasoning and the "physics" of language models | 2026 | -0.08 | 0.91 | -1.14 | 5/7 |
| [PRIMERA: Pyramid-based Masked Sentence Pre-training for Multi-document Summarization](#acl-2022.acl-long.360) | Retrieval, embeddings, benchmarks | unknown | -0.08 | 0.91 | +0.69 | 3/7 |
| [VICReg: Variance-Invariance-Covariance Regularization for Self-Supervised Learning](#arxiv-2105.04906) | Self-supervised learning and vision | 2021 | -0.08 | 1.00 | +0.24 | 3/7 |
| [Single-stream Policy Optimization](#arxiv-2509.13232) | Post-training | 2025 | -0.07 | 1.00 | +0.40 | 5/7 |
| [The First Few Tokens Are All You Need: An Efficient and Effective Unsupervised Prefix Fine-Tuning Method for Reasoning Models](#arxiv-2503.02875) | Post-training | 2025 | -0.07 | 1.00 | +0.85 | 3/7 |

## Per paper

<a id="arxiv-2608.17163"></a>
### Q-Learning With World Models

`arxiv:2608.17163` · Reinforcement learning · 2026-08-17

- final **+0.08** (conf 1.00, pct 49) · impact -1.00 · WATCH
- mean rating (1–10): **6.0** · accept votes **6/7** · percentile rank_avg 54.3 (100=best) · rank in year 43.0 (1=best)
- NAIPv2 `-0.711` · NAIP-v1 `0.593` · SciJudge `-4.566` · DGC-BERT `0.760`
- CycleReviewer 8B `5.8` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/2.5) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [AGI_and_RL/1351](https://t.me/AGI_and_RL/1351), [boris_again/4075](https://t.me/boris_again/4075)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2608.17163.md#weaknesses): The main weakness of the paper is that the authors do not provide a theoretical analysis of their method. While the authors do provide some experimental results, the results are limited to a few tasks and do not provide a comprehensive evaluation of the method. In particular, the authors do not provide a comparison with other model-based RL methods or other methods that use world models.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2608.17163.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further consideration. First, while the paper demonstrates that QWM improves performance, it does not provide a detailed explanation of *why* this improvement occurs.…

<a id="arxiv-2509.09675"></a>
### CDE: Curiosity-Driven Exploration for Efficient Reinforcement Learning in Large Language Models

`arxiv:2509.09675` · Reinforcement learning · 2025-09-11

- final **+0.11** (conf 1.00, pct 52) · impact -1.20 · WATCH
- mean rating (1–10): **6.0** · accept votes **6/7** · percentile rank_avg 51.2 (100=best) · rank in year 53.0 (1=best)
- NAIPv2 `-0.663` · NAIP-v1 `0.401` · SciJudge `-2.350` · DGC-BERT `0.946`
- CycleReviewer 8B `5.8` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `5.8` Accept (S/P/C 2.6/2.6/2.4) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/7659](https://t.me/axisofordinary/7659)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2509.09675.md#weaknesses): 1. The novelty of the paper is limited. The idea of using perplexity as a curiosity signal is not new. There are many papers that use perplexity as a curiosity signal for exploration. For example, (1) uses perplexity as a curiosity signal for exploration in RL. The idea of using the variance of value estimates as a curiosity signal is also not new.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2509.09675.md#weaknesses): While the paper presents a compelling approach, I have identified several weaknesses that warrant further consideration. First, the paper lacks a thorough discussion of the limitations of the proposed CDE method.…

<a id="arxiv-2503.14858"></a>
### 1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities

`arxiv:2503.14858` · Reinforcement learning · 2025-03-19

- final **+0.01** (conf 1.00, pct 37) · impact -0.02 · WATCH
- mean rating (1–10): **5.5** · accept votes **5/7** · percentile rank_avg 46.6 (100=best) · rank in year 64.0 (1=best)
- NAIPv2 `0.184` · NAIP-v1 `0.590` · SciJudge `-0.316` · DGC-BERT `0.755`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.5` Reject · 7B Fast `5.7` Accept (S/P/C 2.67/3.0/2.67) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/7998](https://t.me/axisofordinary/7998)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2503.14858.md#weaknesses): 1. The contribution of this paper is limited. The authors only show that increasing the depth of the model can improve the performance of self-supervised RL. However, the authors do not provide any theoretical analysis or explanation for the improvement. 2. The authors only show the results of contrastive RL. It is unclear whether the improvement also applies to other self-supervised RL methods.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2503.14858.md#weaknesses): While this paper presents compelling evidence for the benefits of depth scaling in contrastive RL, several limitations warrant careful consideration. First, the paper's primary focus on contrastive RL (CRL) limits the generalizability of its findings to other RL algorithms.…

<a id="arxiv-2501.16142"></a>
### Towards General-Purpose Model-Free Reinforcement Learning

`arxiv:2501.16142` · Reinforcement learning · 2025-01-27

- final **-0.13** (conf 1.00, pct 23) · impact -1.07 · WATCH
- mean rating (1–10): **5.7** · accept votes **5/7** · percentile rank_avg 41.1 (100=best) · rank in year 69.0 (1=best)
- NAIPv2 `-1.769` · NAIP-v1 `0.462` · SciJudge `-3.189` · DGC-BERT `0.865`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `4.8` Reject (S/P/C 2.25/2.5/2.5) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/6926](https://t.me/axisofordinary/6926), [AGI_and_RL/988](https://t.me/AGI_and_RL/988)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2501.16142.md#weaknesses): 1. The novelty is limited. The idea of learning a representation that captures a linear relationship between state-action pairs and value is not new, and has been explored in previous works such as TD7 and many other representation learning methods.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2501.16142.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further consideration. First, while the paper claims to be a general-purpose model-free algorithm, it lacks a detailed comparison with other general-purpose methods, particularly model-based approaches like DreamerV3 and TD-MPC2.…

<a id="arxiv-2411.03820"></a>
### Beyond The Rainbow: High Performance Deep Reinforcement Learning on a Desktop PC

`arxiv:2411.03820` · Reinforcement learning · 2024-11-06

- final **+0.21** (conf 1.00, pct 66) · impact -0.74 · KEEP
- mean rating (1–10): **5.8** · accept votes **2/7** · percentile rank_avg 41.7 (100=best) · rank in year 30.0 (1=best)
- NAIPv2 `0.004` · NAIP-v1 `0.487` · SciJudge `-3.795` · DGC-BERT `0.091`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `5.8` Reject (S/P/C 3.0/3.25/2.75) · 14B Fast `5.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `7.0` Accept
- Telegram: [j_links/7764](https://t.me/j_links/7764)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2411.03820.md#weaknesses): 1. The paper does not provide a detailed analysis of the computational resources required to train the agent. It would be helpful to provide a more detailed breakdown of the computational resources required, such as the number of GPUs, CPU cores, and memory required to train the agent. 2. The paper does not provide a detailed analysis of the hyperparameters used to train the agent.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2411.03820.md#weaknesses): While the paper presents a compelling case for the effectiveness and accessibility of BTR, several weaknesses warrant careful consideration. First, the paper's novelty is limited, as it primarily involves combining existing techniques rather than introducing fundamentally new methods.…

<a id="arxiv-2312.13327"></a>
### In-Context Reinforcement Learning for Variable Action Spaces

`arxiv:2312.13327` · Reinforcement learning · 2023-12-20

- final **-0.06** (conf 1.00, pct 30) · impact -1.38 · WATCH
- mean rating (1–10): **5.7** · accept votes **4/7** · percentile rank_avg 37.1 (100=best) · rank in year 41.0 (1=best)
- NAIPv2 `0.215` · NAIP-v1 `0.453` · SciJudge `-4.719` · DGC-BERT `0.658`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `4.0` Reject · 7B Fast `6.0` Accept (S/P/C 2.5/3.0/2.75) · 14B Fast `5.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [data_secrets/4591](https://t.me/data_secrets/4591), [boris_again/2678](https://t.me/boris_again/2678), [knowledge_accumulator/204](https://t.me/knowledge_accumulator/204), [ai_newz/3059](https://t.me/ai_newz/3059)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2312.13327.md#weaknesses): The novelty of the proposed method is limited. The main idea of using random embeddings for actions is not new and has been used in previous work (1). The contrastive loss is also not new. - The experiments are not sufficient. The paper only evaluates the proposed method on simple environments such as Bernoulli bandit and Darkroom.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2312.13327.md#weaknesses): Despite the strengths of the proposed method, I have identified several weaknesses that need to be addressed. First, the paper's experimental evaluation, while demonstrating the core idea, is limited in scope and lacks comparisons to relevant baselines. The experiments are primarily conducted on relatively simple bandit problems and a basic gridworld environment.…

<a id="arxiv-2312.00276"></a>
### Metalearning Continual Learning Algorithms

`arxiv:2312.00276` · Reinforcement learning · 2023-12-01

- final **+0.12** (conf 1.00, pct 54) · impact -0.93 · WATCH
- mean rating (1–10): **5.6** · accept votes **5/7** · percentile rank_avg 39.8 (100=best) · rank in year 36.0 (1=best)
- NAIPv2 `-2.000` · NAIP-v1 `0.537` · SciJudge `-4.290` · DGC-BERT `0.504`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `8.0` Accept · 7B Fast `5.7` Reject (S/P/C 2.67/2.67/2.67) · 14B Fast `5.8` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [knowledge_accumulator/145](https://t.me/knowledge_accumulator/145)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2312.00276.md#weaknesses): The proposed method is not novel. The authors claim that their method is novel because it is the first to meta-learn a learning algorithm for continual learning. However, there are many prior works that have done the same thing. For example, see (1, 2, 3).
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2312.00276.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, while the paper introduces the concept of self-referential weight matrices (SRWMs), the explanation of their inner workings is not sufficiently detailed for a reader unfamiliar with the concept.…

<a id="arxiv-2306.02451"></a>
### For SALE: State-Action Representation Learning for Deep Reinforcement Learning

`arxiv:2306.02451` · Reinforcement learning · 2023-06-04

- final **+0.04** (conf 1.00, pct 42) · impact -1.17 · WATCH
- mean rating (1–10): **5.6** · accept votes **5/7** · percentile rank_avg 45.5 (100=best) · rank in year 31.0 (1=best)
- NAIPv2 `-2.250` · NAIP-v1 `0.436` · SciJudge `-3.215` · DGC-BERT `0.900`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `8.0` Accept · 7B Fast `6.2` Accept (S/P/C 2.75/2.5/2.5) · 14B Fast `4.7` Reject
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [AGI_and_RL/988](https://t.me/AGI_and_RL/988)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2306.02451.md#weaknesses): The proposed method is an extension of OFENet, and the main difference is the clipping of the target value function. However, the authors do not provide a theoretical justification for the clipping operation, and it is unclear why this is necessary. - The authors do not provide a clear explanation of how the state-action representation is used in the RL algorithm.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2306.02451.md#weaknesses): One of the most significant weaknesses of this paper is the lack of clarity in the presentation of the SALE method. The paper introduces several components, such as normalized embeddings, fixed embeddings, and clipped values, but the motivation for these design choices is not well-explained.…

<a id="arxiv-2305.19452"></a>
### Bigger, Better, Faster: Human-level Atari with human-level efficiency

`arxiv:2305.19452` · Reinforcement learning · 2023-05-30

- final **+0.22** (conf 1.00, pct 68) · impact -0.45 · KEEP
- mean rating (1–10): **5.8** · accept votes **3/7** · percentile rank_avg 51.0 (100=best) · rank in year 22.0 (1=best)
- NAIPv2 `1.444` · NAIP-v1 `0.643` · SciJudge `-3.935` · DGC-BERT `0.799`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `6.0` Reject (S/P/C 3.0/3.25/2.5) · 14B Fast `6.2` Accept
- OpenReviewer `5.0` Reject (S/P/C 2.0/3.0/2.0) · SEA-E `7.0` Accept
- Telegram: [axisofordinary/5007](https://t.me/axisofordinary/5007), [knowledge_accumulator/194](https://t.me/knowledge_accumulator/194)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2305.19452.md#weaknesses): The paper does not provide any new algorithmic contributions. The proposed method is a combination of existing techniques, including SR-SPR, Impala-CNN, and other design choices. - The paper does not provide any theoretical analysis of the proposed method. - The paper does not provide any experimental results on other benchmarks, such as the Atari 500K benchmark or the Atari 1M benchmark.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2305.19452.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. First, the paper's novelty is limited, as it primarily combines and modifies existing techniques rather than introducing fundamentally new algorithmic components.…

<a id="arxiv-2301.04104"></a>
### Mastering Diverse Domains through World Models

`arxiv:2301.04104` · Reinforcement learning · 2023-01-10

- final **+0.16** (conf 1.00, pct 60) · impact +1.47 · WATCH
- mean rating (1–10): **6.1** · accept votes **5/7** · percentile rank_avg 58.1 (100=best) · rank in year 12.0 (1=best)
- NAIPv2 `-1.748` · NAIP-v1 `0.739` · SciJudge `3.613` · DGC-BERT `0.596`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.2` Reject · 7B Fast `7.0` Accept (S/P/C 3.0/3.0/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [knowledge_accumulator/155](https://t.me/knowledge_accumulator/155), [j_links/6396](https://t.me/j_links/6396), [ai_newz/1700](https://t.me/ai_newz/1700), [gonzo_ML/4175](https://t.me/gonzo_ML/4175), [gonzo_ML/1791](https://t.me/gonzo_ML/1791), [AGI_and_RL/988](https://t.me/AGI_and_RL/988)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2301.04104.md#weaknesses): 1. The paper lacks a detailed comparison with previous work, particularly in terms of the specific hyperparameters used and the computational resources required. 2. The paper does not provide a clear explanation of the intuition behind the proposed algorithm and how it addresses the challenges of reinforcement learning. 3.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2301.04104.md#weaknesses): While the paper presents a compelling case for DreamerV3, I have identified several weaknesses that warrant further discussion. Firstly, the paper's claim of novelty is somewhat diminished by the fact that many of the introduced techniques, such as symlog transformations, free bits, and return normalization, have been explored in prior work.…

<a id="openreview-XyGJJ4FPoX"></a>
### Meta-Reinforcement Learning with Zero-Shot RL

`openreview:XyGJJ4FPoX` · Reinforcement learning · unknown

- final **-0.47** (conf 1.00, pct 7) · impact -0.89 · DROP
- mean rating (1–10): **4.7** · accept votes **0/7** · percentile rank_avg 17.4 (100=best) · rank in year 12.0 (1=best)
- NAIPv2 `-3.945` · NAIP-v1 `0.472` · SciJudge `-4.250` · DGC-BERT `0.183`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `5.7` Reject (S/P/C 2.67/2.33/2.33) · 14B Fast `4.2` Reject
- OpenReviewer `5.0` Reject (S/P/C 2.0/3.0/2.0) · SEA-E `4.0` Reject
- Telegram: [j_links/8463](https://t.me/j_links/8463)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/openreview_XyGJJ4FPoX.md#weaknesses): The proposed method is a combination of existing methods and the novelty is limited. The experiments are not convincing enough. The proposed method does not show significant improvement over existing methods.
  - [DR-14B Fast](reviews/deepreviewer-14b/openreview_XyGJJ4FPoX.md#weaknesses): and fully realize the potential of this approach. The paper's exploration of the intersection between meta-learning and foundation models is timely and relevant, and the proposed method, despite its limitations, represents a significant step towards more versatile and adaptable reinforcement learning agents.…

<a id="openreview-OpC-9aBBVJe"></a>
### Sample-Efficient RL by Breaking the Replay Ratio Barrier (ICLR 2023, precursor of BBF)

`openreview:OpC-9aBBVJe` · Reinforcement learning · unknown

- final **+0.16** (conf 1.00, pct 60) · impact +0.68 · WATCH
- mean rating (1–10): **6.0** · accept votes **6/7** · percentile rank_avg 49.6 (100=best) · rank in year 3.0 (1=best)
- NAIPv2 `-1.396` · NAIP-v1 `0.698` · SciJudge `1.090` · DGC-BERT `0.016`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.8` Accept · 7B Fast `5.8` Accept (S/P/C 2.75/2.75/2.25) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/4.0/3.0) · SEA-E `6.0` Accept
- Telegram: [knowledge_accumulator/194](https://t.me/knowledge_accumulator/194)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/openreview_OpC-9aBBVJe.md#weaknesses): The main weakness of the paper is the novelty of the approach. The idea of resetting the parameters periodically has been proposed in previous works (e.g., Nikishin et al., 2022). The authors do not provide a theoretical analysis of the proposed approach. The results are only evaluated on two benchmarks and the baselines are not up-to-date.…
  - [DR-14B Fast](reviews/deepreviewer-14b/openreview_OpC-9aBBVJe.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, while the paper introduces parameter resetting as a key component of its method, it does not provide a detailed analysis of the impact of different reset frequencies on the learning process.…

<a id="arxiv-2205.07802"></a>
### The Primacy Bias in Deep Reinforcement Learning

`arxiv:2205.07802` · Reinforcement learning · 2022-05-16

- final **+0.27** (conf 1.00, pct 75) · impact -1.51 · KEEP
- mean rating (1–10): **6.1** · accept votes **6/7** · percentile rank_avg 47.9 (100=best) · rank in year 13.0 (1=best)
- NAIPv2 `-1.850` · NAIP-v1 `0.358` · SciJudge `-3.692` · DGC-BERT `0.855`
- CycleReviewer 8B `4.8` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.5` Accept (S/P/C 3.0/3.5/2.75) · 14B Fast `6.2` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [knowledge_accumulator/188](https://t.me/knowledge_accumulator/188), [j_links/5862](https://t.me/j_links/5862)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2205.07802.md#weaknesses): The proposed method is not novel. The idea of resetting part of the network has been explored in the supervised learning literature (e.g., (1, 2, 3)). The authors should discuss the difference between their method and the existing work. - The authors only consider discrete and continuous control tasks. The authors should also consider more complex tasks, such as robotics manipulation tasks.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2205.07802.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further consideration. First, while the paper introduces the concept of 'primacy bias' and provides empirical evidence of its existence, the definition remains somewhat informal and lacks a rigorous theoretical grounding.…

<a id="arxiv-2106.06860"></a>
### A Minimalist Approach to Offline Reinforcement Learning

`arxiv:2106.06860` · Reinforcement learning · 2021-06-12

- final **-0.49** (conf 1.00, pct 6) · impact -0.69 · DROP
- mean rating (1–10): **5.0** · accept votes **3/7** · percentile rank_avg 26.5 (100=best) · rank in year 10.0 (1=best)
- NAIPv2 `-3.971` · NAIP-v1 `0.426` · SciJudge `1.290` · DGC-BERT `0.685`
- CycleReviewer 8B `3.8` Reject · 70B `` 
- DeepReviewer 7B Std `3.5` Reject · 7B Fast `4.2` Reject (S/P/C 2.25/2.25/2.0) · 14B Fast `5.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [AGI_and_RL/988](https://t.me/AGI_and_RL/988)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2106.06860.md#weaknesses): The main weakness of the paper is that the proposed method is not novel. The idea of adding a behavior cloning term to the policy update is not new and has been explored in several previous works (see the related work section). The only novelty of this paper is the specific formulation of the behavior cloning loss, which is not very well motivated.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2106.06860.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. First, while the paper introduces a dynamic weighting scheme for the behavior cloning (BC) term, it lacks a detailed analysis of its impact.…

<a id="arxiv-2011.14826"></a>
### Revisiting Rainbow: Promoting more Insightful and Inclusive Deep Reinforcement Learning Research

`arxiv:2011.14826` · Reinforcement learning · 2020-11-20

- final **-0.26** (conf 1.00, pct 16) · impact -1.46 · DROP
- mean rating (1–10): **4.4** · accept votes **1/7** · percentile rank_avg 17.7 (100=best) · rank in year 11.0 (1=best)
- NAIPv2 `-3.248` · NAIP-v1 `0.415` · SciJudge `-4.230` · DGC-BERT `0.397`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `5.2` Reject (S/P/C 2.25/2.75/2.25) · 14B Fast `4.8` Reject
- OpenReviewer `3.0` Reject (S/P/C 3.0/2.0/2.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2011.14826.md#weaknesses): The paper lacks novelty in terms of the experiments performed. The authors have not introduced any new algorithms or techniques, but rather have performed experiments on existing ones. The paper would benefit from more in-depth analysis and insights from the experiments.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2011.14826.md#weaknesses): of these different parameterizations. Furthermore, the paper's finding that the MSE loss can outperform the Huber loss when used with the Adam optimizer is a significant result that challenges conventional wisdom in the field. This finding highlights the importance of re-evaluating empirical choices that have become "folk wisdom" in RL research.…

<a id="arxiv-2005.01643"></a>
### Offline Reinforcement Learning: Tutorial, Review, and Perspectives on Open Problems

`arxiv:2005.01643` · Reinforcement learning · 2020-05-04

- final **-0.42** (conf 1.00, pct 8) · impact +0.73 · WATCH
- mean rating (1–10): **4.2** · accept votes **0/7** · percentile rank_avg 24.8 (100=best) · rank in year 9.0 (1=best)
- NAIPv2 `-4.117` · NAIP-v1 `0.684` · SciJudge `1.994` · DGC-BERT `0.060`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.0` Reject · 7B Fast `5.7` Reject (S/P/C 3.0/3.0/2.0) · 14B Fast `4.3` Reject
- OpenReviewer `5.0` Reject (S/P/C 3.0/2.0/2.0) · SEA-E `3.0` Reject
- Telegram: [gonzo_ML/722](https://t.me/gonzo_ML/722), [j_links/3476](https://t.me/j_links/3476)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2005.01643.md#weaknesses): The paper is a tutorial paper and does not present any new results or contributions to the field of offline reinforcement learning. The paper does not provide any new insights or perspectives on the field, and it does not discuss any of the recent advances or developments in the field.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2005.01643.md#weaknesses): Despite its strengths, the paper has several limitations that could be addressed to enhance its value and impact. One significant weakness is the lack of specific technical contributions. While the paper provides a comprehensive overview of existing methods, it does not introduce any novel algorithms, theoretical insights, or empirical findings.…

<a id="arxiv-2004.12919"></a>
### First return, then explore

`arxiv:2004.12919` · Reinforcement learning · 2020-04-27

- final **+0.60** (conf 1.00, pct 98) · impact +1.34 · KEEP
- mean rating (1–10): **6.2** · accept votes **6/7** · percentile rank_avg 65.6 (100=best) · rank in year 3.0 (1=best)
- NAIPv2 `-0.674` · NAIP-v1 `0.851` · SciJudge `1.705` · DGC-BERT `0.740`
- CycleReviewer 8B `2.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `7.3` Accept (S/P/C 3.67/3.33/3.33) · 14B Fast `6.2` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [j_links/3440](https://t.me/j_links/3440)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2004.12919.md#weaknesses): 1. The paper's novelty is limited, as the idea of exploring promising states and returning to them is not a new concept in the field of reinforcement learning. The paper does not provide a clear justification for why this approach is necessary or how it differs from existing methods. 2.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2004.12919.md#weaknesses): While the Go-Explore algorithm demonstrates impressive empirical results, several limitations warrant careful consideration. One significant weakness is the algorithm's reliance on domain-specific knowledge to effectively partition the state space into cells.…

<a id="arxiv-1910.01708"></a>
### Benchmarking Batch Deep Reinforcement Learning Algorithms

`arxiv:1910.01708` · Reinforcement learning · 2019-10-03

- final **-0.56** (conf 1.00, pct 5) · impact -1.45 · DROP
- mean rating (1–10): **4.2** · accept votes **2/7** · percentile rank_avg 17.0 (100=best) · rank in year 5.0 (1=best)
- NAIPv2 `-2.742` · NAIP-v1 `0.356` · SciJudge `-2.343` · DGC-BERT `0.787`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `3.0` Reject · 7B Fast `3.5` Reject (S/P/C 2.25/2.25/2.0) · 14B Fast `3.5` Reject
- OpenReviewer `5.0` Reject (S/P/C 2.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [AGI_and_RL/988](https://t.me/AGI_and_RL/988)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_1910.01708.md#weaknesses): 1. The paper only considers a single partially-trained behavioral policy for data generation, which may not be representative of real-world scenarios where data is generated by multiple policies. It would be interesting to see how the algorithms perform with data generated by multiple policies. 2.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_1910.01708.md#weaknesses): Despite its strengths, this paper suffers from several significant weaknesses that undermine its overall impact. First and foremost, the paper's core contribution, the discrete adaptation of BCQ, is not particularly novel. As the authors themselves acknowledge, the method is primarily an adaptation of the existing BCQ algorithm to a discrete action setting.…

<a id="arxiv-1802.09477"></a>
### Addressing Function Approximation Error in Actor-Critic Methods

`arxiv:1802.09477` · Reinforcement learning · 2018-02-26

- final **-0.37** (conf 0.46, pct 10) · impact -1.14 · WATCH
- mean rating (1–10): **4.3** · accept votes **1/4** · percentile rank_avg 26.7 (100=best) · rank in year 3.0 (1=best)
- NAIPv2 `-3.898` · NAIP-v1 `0.363` · SciJudge `-0.461` · DGC-BERT `0.888`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std ``  · 7B Fast ``  (S/P/C None/None/None) · 14B Fast `` 
- OpenReviewer `3.0` Reject (S/P/C 2.0/2.0/2.0) · SEA-E `5.0` Reject
- Telegram: [AGI_and_RL/988](https://t.me/AGI_and_RL/988)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_1802.09477.md#weaknesses): The proposed method is not novel enough. The idea of learning a contrastive model to detect adversarial examples has been explored in previous works (1, 2, 3). The authors should compare their method with these works and discuss the differences and advantages of their method. - The evaluation is not comprehensive enough.…
  - [OR-8B](reviews/openreviewer-8b/arxiv_1802.09477.md#weaknesses): 1. The novelty of the proposed method is limited. The method is based on contrastive learning, which has been extensively studied in the context of domain adaptation. The authors should clarify the novelty of the proposed method and how it differs from existing methods. 2. The evaluation is not comprehensive. The method is only evaluated on one dataset (Office-Home) and one model (CLIP).…

<a id="arxiv-1801.01290"></a>
### Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor

`arxiv:1801.01290` · Reinforcement learning · 2018-01-04

- final **+0.47** (conf 1.00, pct 94) · impact +1.39 · KEEP
- mean rating (1–10): **6.4** · accept votes **6/7** · percentile rank_avg 68.2 (100=best) · rank in year 1.0 (1=best)
- NAIPv2 `-3.234` · NAIP-v1 `0.771` · SciJudge `1.989` · DGC-BERT `0.915`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.2` Accept · 7B Fast `7.5` Accept (S/P/C 3.25/3.25/3.25) · 14B Fast `5.7` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `8.0` Accept
- Telegram: [gonzo_ML/4277](https://t.me/gonzo_ML/4277)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_1801.01290.md#weaknesses): The proposed algorithm is similar to the soft Q-learning algorithm proposed by Haarnoja et al. (2017). The main difference is that the proposed algorithm uses a separate critic network to estimate the state value function, while the soft Q-learning algorithm does not. The authors should compare the proposed algorithm with the soft Q-learning algorithm more clearly.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_1801.01290.md#weaknesses): While the paper presents a compelling algorithm and strong empirical results, there are several weaknesses that warrant attention. Firstly, the paper lacks a detailed analysis of the computational cost associated with SAC.…

<a id="arxiv-1712.06567"></a>
### Deep Neuroevolution: Genetic Algorithms Are a Competitive Alternative for Training Deep Neural Networks for Reinforcement Learning

`arxiv:1712.06567` · Reinforcement learning · 2017-12-18

- final **+0.41** (conf 1.00, pct 89) · impact +0.41 · KEEP
- mean rating (1–10): **6.3** · accept votes **4/7** · percentile rank_avg 60.1 (100=best) · rank in year 1.0 (1=best)
- NAIPv2 `-0.830` · NAIP-v1 `0.779` · SciJudge `-2.734` · DGC-BERT `0.451`
- CycleReviewer 8B `6.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.8` Reject · 7B Fast `5.8` Accept (S/P/C 2.75/3.0/2.75) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_1712.06567.md#weaknesses): The paper only compares the GA with other deep RL methods, but does not provide a comparison with other evolutionary algorithms. - The paper only considers a limited set of tasks, and it is unclear how the GA would perform on other tasks. - The paper does not provide a detailed analysis of the computational resources required to train the GA.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_1712.06567.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further consideration. First, the paper lacks a thorough analysis of the Deep GA's performance on the Atari suite.…

<a id="arxiv-1710.02298"></a>
### Rainbow: Combining Improvements in Deep Reinforcement Learning

`arxiv:1710.02298` · Reinforcement learning · 2017-10-06

- final **-0.04** (conf 1.00, pct 33) · impact +1.08 · WATCH
- mean rating (1–10): **5.7** · accept votes **3/7** · percentile rank_avg 51.0 (100=best) · rank in year 3.0 (1=best)
- NAIPv2 `-3.051` · NAIP-v1 `0.667` · SciJudge `2.473` · DGC-BERT `0.881`
- CycleReviewer 8B `5.8` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `5.5` Reject (S/P/C 2.75/3.0/2.25) · 14B Fast `5.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [j_links/520](https://t.me/j_links/520), [knowledge_accumulator/194](https://t.me/knowledge_accumulator/194)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_1710.02298.md#weaknesses): The paper does not provide a clear motivation for combining all these extensions. It would be helpful to provide a more detailed explanation of why these extensions are complementary and how they work together to improve performance. - The paper does not provide a detailed analysis of the hyperparameters used in the experiments.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_1710.02298.md#weaknesses): While the paper presents a compelling case for the effectiveness of the Rainbow agent, several weaknesses warrant careful consideration. First, the paper's novelty is somewhat limited, as it primarily focuses on the integration of existing techniques rather than introducing fundamentally new algorithms or insights.…

<a id="arxiv-1707.06887"></a>
### A Distributional Perspective on Reinforcement Learning

`arxiv:1707.06887` · Reinforcement learning · 2017-07-21

- final **+0.36** (conf 1.00, pct 85) · impact +0.89 · KEEP
- mean rating (1–10): **6.0** · accept votes **6/7** · percentile rank_avg 55.7 (100=best) · rank in year 2.0 (1=best)
- NAIPv2 `-2.482` · NAIP-v1 `0.682` · SciJudge `2.160` · DGC-BERT `0.891`
- CycleReviewer 8B `5.8` Reject · 70B `` 
- DeepReviewer 7B Std `4.5` Accept · 7B Fast `5.8` Accept (S/P/C 2.5/2.75/2.5) · 14B Fast `6.7` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [j_links/332](https://t.me/j_links/332), [knowledge_accumulator/194](https://t.me/knowledge_accumulator/194)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_1707.06887.md#weaknesses): 1. The theoretical results are not very surprising. The distributional Bellman operator is a contraction in Wasserstein distance, which has been shown in previous work. The authors only show that the distributional Bellman operator is a contraction in Wasserstein distance, but do not show that the proposed algorithm converges to the optimal solution.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_1707.06887.md#weaknesses): While this paper presents a compelling distributional perspective on reinforcement learning, several weaknesses warrant careful consideration. Firstly, the paper's discussion of the relationship between the proposed distributional approach and risk-sensitive reinforcement learning is insufficient.…

<a id="arxiv-1511.06581"></a>
### Dueling Network Architectures for Deep Reinforcement Learning

`arxiv:1511.06581` · Reinforcement learning · 2015-11-20

- final **+0.11** (conf 1.00, pct 53) · impact +0.29 · WATCH
- mean rating (1–10): **5.9** · accept votes **6/7** · percentile rank_avg 53.2 (100=best) · rank in year 1.0 (1=best)
- NAIPv2 `-4.504` · NAIP-v1 `0.628` · SciJudge `-0.007` · DGC-BERT `0.840`
- CycleReviewer 8B `4.8` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.7` Accept (S/P/C 3.0/3.0/2.33) · 14B Fast `5.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [knowledge_accumulator/194](https://t.me/knowledge_accumulator/194)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_1511.06581.md#weaknesses): The main weakness of the paper is the lack of novelty. The proposed architecture is a simple modification of the standard Q-network architecture, and the idea of separating the value and advantage functions has been explored in previous work. The paper also lacks a thorough theoretical analysis of the proposed architecture.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_1511.06581.md#weaknesses): While the paper introduces a powerful architectural innovation, several limitations warrant careful consideration. One significant weakness is the paper's limited exploration of the dueling network's performance in continuous action spaces.…

<a id="arxiv-1511.05952"></a>
### Prioritized Experience Replay

`arxiv:1511.05952` · Reinforcement learning · 2015-11-18

- final **+0.01** (conf 1.00, pct 38) · impact +1.07 · WATCH
- mean rating (1–10): **5.5** · accept votes **4/7** · percentile rank_avg 49.9 (100=best) · rank in year 2.0 (1=best)
- NAIPv2 `-1.875` · NAIP-v1 `0.706` · SciJudge `2.060` · DGC-BERT `0.910`
- CycleReviewer 8B `4.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.8` Reject · 7B Fast `4.8` Reject (S/P/C 2.5/3.0/2.25) · 14B Fast `5.0` Accept
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/4.0) · SEA-E `6.0` Accept
- Telegram: [AGI_and_RL/189](https://t.me/AGI_and_RL/189), [knowledge_accumulator/194](https://t.me/knowledge_accumulator/194)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_1511.05952.md#weaknesses): The proposed algorithm is not novel. - The experimental results are not convincing. - The proposed algorithm is not well-motivated.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_1511.05952.md#weaknesses): While I find the paper to be a strong contribution, there are several weaknesses that I have identified through my analysis. First, while the paper introduces the concept of TD-error as a measure of surprise, it lacks a deeper theoretical analysis of why this particular measure is effective for prioritization.…

<a id="arxiv-1509.06461"></a>
### Deep Reinforcement Learning with Double Q-learning

`arxiv:1509.06461` · Reinforcement learning · 2015-09-22

- final **+0.10** (conf 1.00, pct 51) · impact +0.43 · WATCH
- mean rating (1–10): **5.5** · accept votes **5/7** · percentile rank_avg 49.0 (100=best) · rank in year 3.0 (1=best)
- NAIPv2 `-2.979` · NAIP-v1 `0.721` · SciJudge `-0.671` · DGC-BERT `0.890`
- CycleReviewer 8B `5.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.0` Reject (S/P/C 2.75/3.0/2.75) · 14B Fast `4.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [knowledge_accumulator/194](https://t.me/knowledge_accumulator/194)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_1509.06461.md#weaknesses): The paper lacks a comprehensive discussion of the limitations and potential drawbacks of the proposed approach. The authors should provide a more detailed analysis of the computational complexity and scalability of the proposed algorithm, as well as its potential limitations in terms of generalizability and applicability to different types of problems.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_1509.06461.md#weaknesses): While the paper presents a valuable contribution, I have identified several weaknesses that warrant further discussion. Firstly, the paper's comparison of Double DQN is primarily against the original DQN algorithm.…

<a id="arxiv-2608.13040"></a>
### Latent On-Policy Self-Distillation

`arxiv:2608.13040` · Post-training · 2026-08-13

- final **+0.13** (conf 1.00, pct 57) · impact -0.53 · WATCH
- mean rating (1–10): **6.1** · accept votes **6/7** · percentile rank_avg 56.3 (100=best) · rank in year 39.0 (1=best)
- NAIPv2 `-0.950` · NAIP-v1 `0.536` · SciJudge `-2.128` · DGC-BERT `0.842`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `7.0` Accept (S/P/C 3.0/3.0/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/4.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2608.13040.md#weaknesses): The paper is not well written and it is hard to follow. The notations are not well defined and the description of the method is not clear. The evaluation is not sufficient. The authors should provide more details about the baselines, the hyper-parameters, and the training and evaluation settings.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2608.13040.md#weaknesses): Despite the paper's strengths, several aspects of the proposed method and its evaluation could be improved. One of the primary concerns is the clarity of the method's description. The introduction of the learnable composer and the privileged-margin objective, while innovative, is not sufficiently detailed.…

<a id="arxiv-2608.09888"></a>
### BDH-CQ: In-Context Learning with Recurrent Latent Reasoning

`arxiv:2608.09888` · Post-training · 2026-08-10

- final **-0.35** (conf 1.00, pct 10) · impact -0.46 · DROP
- mean rating (1–10): **5.4** · accept votes **2/7** · percentile rank_avg 38.8 (100=best) · rank in year 64.0 (1=best)
- NAIPv2 `-0.529` · NAIP-v1 `0.629` · SciJudge `-3.654` · DGC-BERT `0.411`
- CycleReviewer 8B `5.2` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `4.2` Reject (S/P/C 2.5/2.75/2.5) · 14B Fast `5.7` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/8994](https://t.me/axisofordinary/8994)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2608.09888.md#weaknesses): 1. The paper lacks a detailed description of the model architecture and its training procedure. The authors only provide a high-level overview of the model and its components, without providing specific details on how it is trained or how the recurrent memory is updated. This makes it difficult to understand the specific design choices and how they contribute to the model's performance.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2608.09888.md#weaknesses): , providing a nuanced understanding of its capabilities. The paper also provides a clear and concise description of the BDH-CQ system, making it easy to understand the core ideas and contributions. The authors have clearly articulated the motivation behind their work and the significance of their findings.…

<a id="arxiv-2607.07847"></a>
### When Does Continual Learning Require Learning

`arxiv:2607.07847` · Post-training · 2026-07-08

- final **+0.02** (conf 1.00, pct 39) · impact +0.56 · WATCH
- mean rating (1–10): **5.9** · accept votes **4/7** · percentile rank_avg 50.5 (100=best) · rank in year 53.0 (1=best)
- NAIPv2 `-0.608` · NAIP-v1 `0.653` · SciJudge `1.397` · DGC-BERT `0.382`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.8` Reject · 7B Fast `6.0` Accept (S/P/C 3.0/3.25/3.0) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/5812](https://t.me/gonzo_ML/5812)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2607.07847.md#weaknesses): The paper only evaluates eight methods across four families, which may not be representative of all possible approaches to continual learning in LLMs. - The paper only uses a single model, Qwen3-8B, for all evaluations, which may not generalize to other models or model sizes.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2607.07847.md#weaknesses): of different approaches. Fourth, the paper's empirical findings are valuable. The study reveals important trade-offs between different methods, highlighting the fact that no single method is universally superior. This is a crucial insight for researchers and practitioners working in this field.…

<a id="arxiv-2607.05609"></a>
### To Retain or to Adapt? Generalizing Continual Learning

`arxiv:2607.05609` · Post-training · 2026-07-06

- final **+0.07** (conf 1.00, pct 48) · impact -0.69 · WATCH
- mean rating (1–10): **6.1** · accept votes **5/7** · percentile rank_avg 59.7 (100=best) · rank in year 30.0 (1=best)
- NAIPv2 `0.292` · NAIP-v1 `0.529` · SciJudge `-2.730` · DGC-BERT `0.825`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `7.0` Accept · 7B Fast `6.0` Reject (S/P/C 2.75/3.0/2.5) · 14B Fast `6.5` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/5817](https://t.me/gonzo_ML/5817)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2607.05609.md#weaknesses): The authors do not provide an experimental evaluation of the proposed algorithm, Window. It would be interesting to see how the Window algorithm compares to other continual learning algorithms in terms of Transfer Efficiency.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2607.05609.md#weaknesses): While I appreciate the contributions of this paper, I have identified several weaknesses that warrant careful consideration. First, the paper's theoretical analysis relies heavily on the assumption of quadratic loss functions, which significantly limits the applicability of the derived analytical expressions.…

<a id="arxiv-2606.23740"></a>
### Weight-Space Geometry of Offline Reasoning Training

`arxiv:2606.23740` · Post-training · 2026-06-21

- final **-0.25** (conf 1.00, pct 17) · impact -0.91 · DROP
- mean rating (1–10): **5.5** · accept votes **2/7** · percentile rank_avg 36.9 (100=best) · rank in year 67.0 (1=best)
- NAIPv2 `0.401` · NAIP-v1 `0.346` · SciJudge `0.709` · DGC-BERT `0.074`
- CycleReviewer 8B `4.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.2` Reject · 7B Fast `4.8` Reject (S/P/C 2.5/2.5/2.5) · 14B Fast `6.5` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [lovedeathtransformers/10841](https://t.me/lovedeathtransformers/10841), [lovedeathtransformers/10825](https://t.me/lovedeathtransformers/10825)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2606.23740.md#weaknesses): 1. The paper only considers a single domain and checkpoint, which may limit the generalizability of the findings. 2. The analysis is limited to attention-only LoRA, which may not be representative of the full range of LoRA configurations. 3.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2606.23740.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. First, the paper's scope is limited by its focus on a single model (Qwen3-4B), a single dataset domain (math problems), and a specific training technique (attention-only LoRA).…

<a id="arxiv-2606.18810"></a>
### Learning from Own Solutions: Self-Conditioned Credit Assignment for Reinforcement Learning with Verifiable Rewards

`arxiv:2606.18810` · Post-training · 2026-06-17

- final **+0.01** (conf 1.00, pct 38) · impact -0.98 · WATCH
- mean rating (1–10): **6.3** · accept votes **4/7** · percentile rank_avg 49.4 (100=best) · rank in year 55.0 (1=best)
- NAIPv2 `-1.278` · NAIP-v1 `0.505` · SciJudge `-3.665` · DGC-BERT `0.160`
- CycleReviewer 8B `5.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Reject · 7B Fast `6.5` Accept (S/P/C 3.0/3.25/2.5) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2606.18810.md#weaknesses): The novelty of the paper is limited. The idea of using KL divergence as a multiplicative weight on gradients is not new and has been explored in other contexts.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2606.18810.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, while the paper demonstrates that SC-GRPO outperforms the GRPO baseline, it does not provide a detailed analysis of the computational cost associated with the proposed method.…

<a id="arxiv-2606.06021"></a>
### OPRD: On-Policy Representation Distillation

`arxiv:2606.06021` · Post-training · 2026-06-04

- final **+0.46** (conf 1.00, pct 93) · impact +0.74 · KEEP
- mean rating (1–10): **6.3** · accept votes **5/7** · percentile rank_avg 76.1 (100=best) · rank in year 2.0 (1=best)
- NAIPv2 `3.092` · NAIP-v1 `0.698` · SciJudge `0.956` · DGC-BERT `0.915`
- CycleReviewer 8B `5.8` Reject · 70B `` 
- DeepReviewer 7B Std `6.8` Accept · 7B Fast `6.0` Reject (S/P/C 3.0/3.0/3.0) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2606.06021.md#weaknesses): The paper proposes a new approach to on-policy distillation, which is to distill the model in the hidden-state space. However, the paper does not provide a thorough analysis of the proposed method. For example, it is not clear how the proposed method compares to other distillation methods, such as knowledge distillation and distillation with reinforcement learning.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2606.06021.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, the paper's evaluation is limited to mathematical reasoning benchmarks (AIME 2024, AIME 2025, AIMO). While these are important benchmarks, they do not fully capture the generalizability of the proposed method.…

<a id="arxiv-2605.22074"></a>
### From Reasoning Chains to Verifiable Subproblems: Curriculum Reinforcement Learning Enables Credit Assignment for LLM Reasoning

`arxiv:2605.22074` · Post-training · 2026-05-21

- final **+0.20** (conf 1.00, pct 65) · impact +0.59 · KEEP
- mean rating (1–10): **6.3** · accept votes **6/7** · percentile rank_avg 69.6 (100=best) · rank in year 9.0 (1=best)
- NAIPv2 `-0.527` · NAIP-v1 `0.638` · SciJudge `1.542` · DGC-BERT `0.907`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.2` Accept · 7B Fast `7.0` Accept (S/P/C 3.0/3.25/3.25) · 14B Fast `5.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2605.22074.md#weaknesses): I am not an expert in this area, but I am not sure if the method is novel enough. It seems that the method is a combination of existing ideas, such as curriculum learning and subproblem decomposition. The paper does not provide a clear comparison with other methods, and it is not clear how the proposed method compares to other methods in terms of novelty and effectiveness.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2605.22074.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further consideration. First, the paper's reliance on a fixed number of subproblems, denoted as 'K', is a significant limitation.…

<a id="arxiv-2605.12969"></a>
### Revisiting Reinforcement Learning with Verifiable Rewards from a Contrastive Perspective

`arxiv:2605.12969` · Post-training · 2026-05-13

- final **+0.35** (conf 1.00, pct 84) · impact -0.79 · KEEP
- mean rating (1–10): **6.5** · accept votes **6/7** · percentile rank_avg 65.2 (100=best) · rank in year 20.0 (1=best)
- NAIPv2 `0.069` · NAIP-v1 `0.457` · SciJudge `-1.566` · DGC-BERT `0.943`
- CycleReviewer 8B `5.8` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `7.0` Accept (S/P/C 3.0/2.75/3.0) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2605.12969.md#weaknesses): 1. The novelty of this paper is limited. The proposed method is based on a contrastive view of RLVR optimization, which is a common approach in the field of RL. The proposed method also uses a group-wise InfoNCE-style objective, which is a widely used contrastive loss function.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2605.12969.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. First, while the paper demonstrates empirical improvements over GRPO, it lacks a theoretical analysis of the convergence properties of the proposed ConSPO algorithm.…

<a id="arxiv-2605.06241"></a>
### Rethinking RL for LLM Reasoning: It's Sparse Policy Selection, Not Capability Learning

`arxiv:2605.06241` · Post-training · 2026-05-07

- final **+0.49** (conf 1.00, pct 94) · impact +1.40 · KEEP
- mean rating (1–10): **7.2** · accept votes **5/7** · percentile rank_avg 80.6 (100=best) · rank in year 1.0 (1=best)
- NAIPv2 `0.688` · NAIP-v1 `0.633` · SciJudge `3.479` · DGC-BERT `0.163`
- CycleReviewer 8B `5.8` Reject · 70B `` 
- DeepReviewer 7B Std `7.0` Accept · 7B Fast `7.5` Accept (S/P/C 3.25/3.25/3.0) · 14B Fast `7.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/4.0/3.0) · SEA-E `7.0` Accept
- Telegram: [j_links/8484](https://t.me/j_links/8484)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2605.06241.md#weaknesses): The proposed method is a simple baseline and has been proposed before in (1). The authors should compare the proposed method with more advanced RL-free methods.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2605.06241.md#weaknesses): While I found the paper to be generally strong, there are several weaknesses that I believe warrant further discussion. First, the paper's analysis is primarily focused on mathematical reasoning tasks, and it remains unclear how well the findings generalize to other types of reasoning.…

<a id="arxiv-2604.20659"></a>
### GRPO-VPS: Enhancing Group Relative Policy Optimization with Verifiable Process Supervision for Effective Reasoning

`arxiv:2604.20659` · Post-training · 2026-04-22

- final **-0.01** (conf 1.00, pct 35) · impact -0.78 · WATCH
- mean rating (1–10): **6.0** · accept votes **5/7** · percentile rank_avg 48.1 (100=best) · rank in year 56.0 (1=best)
- NAIPv2 `-1.234` · NAIP-v1 `0.453` · SciJudge `-0.894` · DGC-BERT `0.697`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.2` Accept · 7B Fast `5.8` Reject (S/P/C 2.75/2.75/2.5) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2604.20659.md#weaknesses): The proposed method is an extension of GRPO, and the novelty is limited. - The proposed method relies on the model's confidence in the correct answer, which may not be reliable in all cases. For example, if the model is uncertain about the correct answer, it may not provide a reliable confidence score.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2604.20659.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, the method's reliance on ground truth answers for calculating the progress signal is a significant limitation.…

<a id="arxiv-2604.13016"></a>
### Rethinking On-Policy Distillation of Large Language Models: Phenomenology, Mechanism, and Recipe

`arxiv:2604.13016` · Post-training · 2026-04-14

- final **+0.36** (conf 1.00, pct 85) · impact -0.07 · KEEP
- mean rating (1–10): **6.3** · accept votes **6/7** · percentile rank_avg 66.1 (100=best) · rank in year 15.0 (1=best)
- NAIPv2 `0.490` · NAIP-v1 `0.563` · SciJudge `0.303` · DGC-BERT `0.852`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `7.0` Accept · 7B Fast `7.5` Accept (S/P/C 3.0/3.0/2.75) · 14B Fast `6.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2604.13016.md#weaknesses): 1. The paper focuses on mathematical benchmarks, which may not be representative of other domains such as code and open-ended settings. It would be interesting to see if the same conditions and token-level mechanisms govern OPD in these other domains.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2604.13016.md#weaknesses): While this paper offers valuable insights into on-policy distillation (OPD), several limitations warrant careful consideration. First, the paper's analysis of the 'thinking-pattern consistency' condition, while insightful, lacks a precise definition and quantitative measure.…

<a id="arxiv-2604.08690"></a>
### Skip-Connected Policy Optimization for Implicit Advantage

`arxiv:2604.08690` · Post-training · 2026-04-09

- final **+0.29** (conf 1.00, pct 77) · impact -1.77 · KEEP
- mean rating (1–10): **6.5** · accept votes **6/7** · percentile rank_avg 60.8 (100=best) · rank in year 28.0 (1=best)
- NAIPv2 `-0.349` · NAIP-v1 `0.353` · SciJudge `-3.717` · DGC-BERT `0.886`
- CycleReviewer 8B `5.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `7.5` Accept (S/P/C 3.0/3.0/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2604.08690.md#weaknesses): The proposed method is very similar to the existing method, DAPO (Yu et al., 2025b). The main difference is that DAPO uses a self-critic, while the proposed method uses a separate upstream and downstream phase. I think the authors should discuss more about the difference between the proposed method and DAPO. - The proposed method is not very efficient.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2604.08690.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, while the paper demonstrates improvements on both Qwen2.5-Math-7B and Llama-3.2-3B models, the gains on the Llama-3.2-3B model are less pronounced compared to the Qwen2.5-Math-7B model.…

<a id="arxiv-2604.02288"></a>
### Unifying Group-Relative and Self-Distillation Policy Optimization via Sample Routing

`arxiv:2604.02288` · Post-training · 2026-04-02

- final **-0.00** (conf 1.00, pct 36) · impact +0.63 · WATCH
- mean rating (1–10): **5.9** · accept votes **5/7** · percentile rank_avg 59.7 (100=best) · rank in year 31.0 (1=best)
- NAIPv2 `0.539` · NAIP-v1 `0.620` · SciJudge `2.070` · DGC-BERT `0.848`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.8` Reject · 7B Fast `6.0` Accept (S/P/C 2.5/3.0/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2604.02288.md#weaknesses): The paper only compares SRPO with GRPO and SDPO. It would be interesting to see how SRPO compares to other methods for post-hoc training of LLMs, such as RLHF. - The paper only evaluates SRPO on five benchmarks and two model scales. It would be interesting to see how SRPO performs on a wider range of benchmarks and model scales. - The paper does not provide any analysis of the limitations of SRPO.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2604.02288.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, while the paper demonstrates that SRPO achieves both early efficiency and long-term stability, the explanation of *how* the proposed modifications lead to these improvements could be more detailed.…

<a id="arxiv-2604.01375"></a>
### RIFT: A RubrIc Failure Mode Taxonomy and Automated Diagnostics

`arxiv:2604.01375` · Post-training · 2026-04-01

- final **-0.10** (conf 1.00, pct 25) · impact -0.29 · WATCH
- mean rating (1–10): **5.8** · accept votes **3/7** · percentile rank_avg 46.3 (100=best) · rank in year 57.0 (1=best)
- NAIPv2 `-1.389` · NAIP-v1 `0.541` · SciJudge `-0.344` · DGC-BERT `0.309`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.2` Reject (S/P/C 2.75/3.0/3.0) · 14B Fast `5.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2604.01375.md#weaknesses): 1. The paper focuses on the evaluation of rubrics, but does not discuss how to construct good rubrics. This is an important limitation, as the quality of the rubric is critical to the effectiveness of the evaluation. The paper should discuss how to construct good rubrics and how to evaluate their quality.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2604.01375.md#weaknesses): of each approach, highlighting the need for human-in-the-loop rubric creation pipelines. The paper is also well-written and clearly structured, making it accessible to a broad audience. The authors provide sufficient detail about their methodology, allowing for reproducibility and further research.…

<a id="arxiv-2603.25562"></a>
### Revisiting On-Policy Distillation: Empirical Failure Modes and Simple Fixes

`arxiv:2603.25562` · Post-training · 2026-03-26

- final **-0.07** (conf 1.00, pct 29) · impact +0.37 · WATCH
- mean rating (1–10): **5.8** · accept votes **5/7** · percentile rank_avg 53.8 (100=best) · rank in year 45.0 (1=best)
- NAIPv2 `-0.349` · NAIP-v1 `0.660` · SciJudge `0.539` · DGC-BERT `0.870`
- CycleReviewer 8B `4.2` Reject · 70B `` 
- DeepReviewer 7B Std `5.2` Reject · 7B Fast `5.8` Accept (S/P/C 2.5/3.0/2.5) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2603.25562.md#weaknesses): The proposed method is not novel. The idea of using top-K local support matching has been studied in the RL community for a long time. See, for example, (1,2). It is unclear why the authors did not cite these papers. - The empirical results are not convincing. The proposed method is only evaluated on two small datasets, which are not sufficient to demonstrate its effectiveness.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2603.25562.md#weaknesses): While this paper presents a strong contribution to the field, there are several limitations that warrant further discussion. One significant weakness lies in the limited exploration of the trade-offs between the proposed method and alternative approaches, particularly in the context of multi-task learning.…

<a id="arxiv-2603.24472"></a>
### Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs?

`arxiv:2603.24472` · Post-training · 2026-03-25

- final **-0.17** (conf 1.00, pct 22) · impact +0.19 · WATCH
- mean rating (1–10): **5.7** · accept votes **3/7** · percentile rank_avg 43.4 (100=best) · rank in year 61.0 (1=best)
- NAIPv2 `-0.968` · NAIP-v1 `0.561` · SciJudge `1.327` · DGC-BERT `0.251`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `5.8` Reject (S/P/C 2.75/2.75/2.75) · 14B Fast `5.8` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2603.24472.md#weaknesses): The authors only consider the math reasoning tasks, which is a very narrow scope. It is not clear whether the findings can be generalized to other reasoning tasks, such as commonsense reasoning, natural language inference, and so on. - The authors only consider the self-distillation methods, which is not a comprehensive study.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2603.24472.md#weaknesses): While I appreciate the strengths of this paper, I have identified several weaknesses that warrant further consideration. First, the paper's reliance on a predefined set of epistemic markers is a significant limitation. The authors define epistemic verbalization using a set of 10 specific tokens, such as "wait" and "perhaps," as stated in Section 3.…

<a id="arxiv-2602.18037"></a>
### Gradient Regularization Mitigates Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards

`arxiv:2602.18037` · Post-training · 2026-02-20

- final **+0.13** (conf 1.00, pct 57) · impact -0.39 · WATCH
- mean rating (1–10): **6.0** · accept votes **4/7** · percentile rank_avg 56.3 (100=best) · rank in year 38.0 (1=best)
- NAIPv2 `-1.482` · NAIP-v1 `0.387` · SciJudge `1.762` · DGC-BERT `0.828`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `8.0` Accept · 7B Fast `6.5` Reject (S/P/C 2.75/2.75/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [j_links/8317](https://t.me/j_links/8317)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2602.18037.md#weaknesses): 1. The paper lacks a comprehensive evaluation of the proposed method, with only a few experiments conducted on small-scale datasets. 2. The paper does not provide a detailed analysis of the computational cost of the proposed method. 3. The paper does not discuss the limitations of the proposed method and potential future research directions.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2602.18037.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further consideration. First, while the paper provides a theoretical connection between flatness and reward model inaccuracy, the practical application of this theory in the context of discrete action spaces, such as those used with large language models (LLMs), is not fully addressed.…

<a id="arxiv-2602.09000"></a>
### iGRPO: Self-Feedback-Driven LLM Reasoning

`arxiv:2602.09000` · Post-training · 2026-02-09

- final **-0.05** (conf 1.00, pct 31) · impact +0.61 · WATCH
- mean rating (1–10): **5.6** · accept votes **4/7** · percentile rank_avg 52.4 (100=best) · rank in year 49.0 (1=best)
- NAIPv2 `-1.219` · NAIP-v1 `0.502` · SciJudge `3.149` · DGC-BERT `0.912`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `5.5` Reject (S/P/C 2.5/2.75/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/8164](https://t.me/axisofordinary/8164)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2602.09000.md#weaknesses): The proposed method is a simple extension of GRPO, and the authors do not provide a clear motivation for why the proposed method should work better than GRPO. - The authors do not provide a clear analysis of why the proposed method outperforms other self-improvement baselines.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2602.09000.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, while the paper introduces iGRPO as an extension of GRPO, it lacks a comprehensive comparison with other state-of-the-art RL algorithms, such as PPO or reward-weighted regression (RWR).…

<a id="arxiv-2601.20861"></a>
### Evolutionary Strategies lead to Catastrophic Forgetting in LLMs

`arxiv:2601.20861` · Post-training · 2026-01-28

- final **-0.54** (conf 1.00, pct 5) · impact -1.33 · DROP
- mean rating (1–10): **5.1** · accept votes **3/7** · percentile rank_avg 23.8 (100=best) · rank in year 71.0 (1=best)
- NAIPv2 `-2.814` · NAIP-v1 `0.345` · SciJudge `-1.974` · DGC-BERT `0.038`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `5.7` Accept (S/P/C 2.67/2.67/2.67) · 14B Fast `4.0` Reject
- OpenReviewer `5.0` Reject (S/P/C 2.0/3.0/2.0) · SEA-E `5.0` Accept
- Telegram: [gonzo_ML/4709](https://t.me/gonzo_ML/4709)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2601.20861.md#weaknesses): The paper only evaluates ES on a limited set of tasks and models, which may not be representative of the broader LLM landscape. - The paper only considers a single type of ES implementation, which may not be representative of all ES variants. - The paper does not provide any insights into how to mitigate catastrophic forgetting in ES.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2601.20861.md#weaknesses): of ES: its propensity for catastrophic forgetting when applied to continual learning. While ES achieves comparable performance to GRPO on individual tasks, the study reveals that ES leads to substantial model degradation and forgetting of previously learned abilities when sequentially trained on new tasks.…

<a id="arxiv-2601.20802"></a>
### Reinforcement Learning via Self-Distillation

`arxiv:2601.20802` · Post-training · 2026-01-28

- final **+0.27** (conf 1.00, pct 75) · impact +1.09 · KEEP
- mean rating (1–10): **6.2** · accept votes **6/7** · percentile rank_avg 68.4 (100=best) · rank in year 10.0 (1=best)
- NAIPv2 `-0.924` · NAIP-v1 `0.584` · SciJudge `3.379` · DGC-BERT `0.912`
- CycleReviewer 8B `5.2` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.5` Accept (S/P/C 3.0/3.0/2.75) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/4681](https://t.me/gonzo_ML/4681)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2601.20802.md#weaknesses): 1. The paper does not provide a clear motivation for the proposed method. The paper states that the key limitation is not RL per se, but the information bottleneck imposed by scalar outcome rewards. However, it is not clear why this is the case or how the proposed method addresses this limitation. 2. The paper does not provide a clear explanation of the proposed method.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2601.20802.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further consideration. First, the paper's reliance on specific types of feedback, particularly error messages and LeetCode-style feedback, raises concerns about its generalizability.…

<a id="arxiv-2601.19897"></a>
### Self-Distillation Enables Continual Learning

`arxiv:2601.19897` · Post-training · 2026-01-27

- final **-0.08** (conf 1.00, pct 27) · impact +0.66 · WATCH
- mean rating (1–10): **6.0** · accept votes **6/7** · percentile rank_avg 59.6 (100=best) · rank in year 32.0 (1=best)
- NAIPv2 `-1.568` · NAIP-v1 `0.601` · SciJudge `2.275` · DGC-BERT `0.924`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.8` Reject · 7B Fast `6.2` Accept (S/P/C 2.75/3.0/2.75) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/4687](https://t.me/gonzo_ML/4687), [axisofordinary/8164](https://t.me/axisofordinary/8164)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2601.19897.md#weaknesses): 1. The paper lacks a theoretical analysis of the proposed method. It would be helpful to have a theoretical analysis of the method's performance and its limitations. 2. The paper only evaluates the proposed method on a limited number of tasks. It would be helpful to evaluate the method on a larger number of tasks to demonstrate its generalizability. 3.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2601.19897.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, while the paper introduces SDFT as a method for continual learning, it lacks a clear definition of what constitutes a 'task' within its framework. The paper uses the term 'task' extensively, but it does not explicitly define what constitutes a 'task' in the context of their method.…

<a id="arxiv-2601.18734"></a>
### Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models

`arxiv:2601.18734` · Post-training · 2026-01-26

- final **+0.12** (conf 1.00, pct 55) · impact +0.54 · WATCH
- mean rating (1–10): **6.3** · accept votes **5/7** · percentile rank_avg 66.6 (100=best) · rank in year 13.0 (1=best)
- NAIPv2 `1.841` · NAIP-v1 `0.656` · SciJudge `1.189` · DGC-BERT `0.813`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.2` Reject · 7B Fast `6.7` Accept (S/P/C 3.0/3.0/2.67) · 14B Fast `6.0` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2601.18734.md#weaknesses): The main weakness of the paper is that it lacks novelty. The idea of using a teacher-student framework for knowledge distillation is not new, and the use of ground-truth solutions as privileged information is also not novel. Additionally, the experimental results are not particularly surprising, and the authors do not provide any new insights into the problem of knowledge distillation.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2601.18734.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. First, the paper suffers from a lack of clarity in its method description, particularly regarding the teacher's role and the training process.…

<a id="arxiv-2601.16175"></a>
### Learning to Discover at Test Time

`arxiv:2601.16175` · Post-training · 2026-01-22

- final **+0.27** (conf 1.00, pct 74) · impact +1.26 · KEEP
- mean rating (1–10): **6.5** · accept votes **6/7** · percentile rank_avg 65.9 (100=best) · rank in year 16.0 (1=best)
- NAIPv2 `-0.401` · NAIP-v1 `0.564` · SciJudge `3.609` · DGC-BERT `0.030`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.2` Accept · 7B Fast `5.8` Accept (S/P/C 2.75/2.5/2.5) · 14B Fast `8.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [gonzo_ML/4643](https://t.me/gonzo_ML/4643), [j_links/8337](https://t.me/j_links/8337)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2601.16175.md#weaknesses): The paper only evaluates the method on a limited set of problems and does not provide a comprehensive evaluation of its performance. The paper also does not provide a detailed analysis of the method's performance on different types of problems.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2601.16175.md#weaknesses): While I find the paper to be a strong contribution, there are several verified limitations that I believe should be addressed. First, the paper lacks a detailed analysis of the computational efficiency of the discovered algorithms, particularly in the context of GPU kernel engineering.…

<a id="arxiv-2601.14525"></a>
### Towards Execution-Grounded Automated AI Research

`arxiv:2601.14525` · Post-training · 2026-01-20

- final **+0.04** (conf 1.00, pct 42) · impact +0.18 · WATCH
- mean rating (1–10): **6.2** · accept votes **5/7** · percentile rank_avg 54.0 (100=best) · rank in year 44.0 (1=best)
- NAIPv2 `-0.429` · NAIP-v1 `0.485` · SciJudge `2.270` · DGC-BERT `0.572`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/3.0) · 14B Fast `6.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/4.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/4660](https://t.me/gonzo_ML/4660)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2601.14525.md#weaknesses): 1. The novelty of this paper is limited. The proposed executor is a simple combination of existing ideas. The authors use the Tinker API to generate code from LLMs, and the scheduler and worker are also standard components. The authors also use evolutionary search and reinforcement learning to learn from execution feedback, which are both existing methods. 2.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2601.14525.md#weaknesses): While I appreciate the novelty of this work, I have identified several weaknesses that warrant careful consideration. First, the paper's reliance on a single, potentially flawed, implementation of the GRPO algorithm as a baseline is a significant concern.…

<a id="arxiv-2601.11061"></a>
### Spurious Rewards Paradox: Mechanistically Understanding How RLVR Activates Memorization Shortcuts in LLMs

`arxiv:2601.11061` · Post-training · 2026-01-16

- final **+0.39** (conf 1.00, pct 88) · impact +1.02 · KEEP
- mean rating (1–10): **6.3** · accept votes **6/7** · percentile rank_avg 73.1 (100=best) · rank in year 5.0 (1=best)
- NAIPv2 `2.123` · NAIP-v1 `0.655` · SciJudge `2.750` · DGC-BERT `0.666`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `7.0` Accept · 7B Fast `7.0` Accept (S/P/C 3.0/3.25/3.25) · 14B Fast `6.5` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [buckwheat_thoughts/308](https://t.me/buckwheat_thoughts/308), [j_links/8281](https://t.me/j_links/8281), [gonzo_ML/4704](https://t.me/gonzo_ML/4704)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2601.11061.md#weaknesses): The paper only studies the Qwen2.5 model, which is a specific model architecture. It is unclear whether the findings can be generalized to other model architectures. - The paper only studies the spurious rewards paradox in RLVR, which is a specific phenomenon. It is unclear whether the findings can be generalized to other phenomena in RLVR.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2601.11061.md#weaknesses): While this paper presents significant contributions to our understanding of memorization in RLVR-tuned models, several limitations warrant careful consideration. First, the paper's reliance on a specific model architecture, the Qwen2.5-Math-7B, raises concerns about the generalizability of the findings.…

<a id="arxiv-2512.02807"></a>
### SR-GRPO: Stable Rank as an Intrinsic Geometric Reward for Large Language Model Alignment

`arxiv:2512.02807` · Post-training · 2025-12-02

- final **+0.23** (conf 1.00, pct 70) · impact +0.14 · KEEP
- mean rating (1–10): **6.0** · accept votes **6/7** · percentile rank_avg 61.3 (100=best) · rank in year 28.0 (1=best)
- NAIPv2 `-0.412` · NAIP-v1 `0.616` · SciJudge `0.108` · DGC-BERT `0.904`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.5` Accept (S/P/C 2.75/2.75/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [tech_priestess/2494](https://t.me/tech_priestess/2494)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2512.02807.md#weaknesses): The paper does not provide any theoretical motivation for the proposed reward signal. It is not clear why stable rank is a good proxy for human preference. - The paper does not provide any analysis of the robustness of the proposed reward signal to different LLM architectures and training settings.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2512.02807.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further consideration. One significant limitation is the lack of a comprehensive theoretical analysis explaining why stable rank correlates with response quality.…

<a id="arxiv-2512.00499"></a>
### ESPO: Entropy Importance Sampling Policy Optimization

`arxiv:2512.00499` · Post-training · 2025-11-29

- final **+0.19** (conf 1.00, pct 63) · impact -0.92 · WATCH
- mean rating (1–10): **6.2** · accept votes **6/7** · percentile rank_avg 53.6 (100=best) · rank in year 45.0 (1=best)
- NAIPv2 `-0.965` · NAIP-v1 `0.544` · SciJudge `-4.950` · DGC-BERT `0.884`
- CycleReviewer 8B `5.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `7.5` Accept (S/P/C 3.0/3.25/3.25) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2512.00499.md#weaknesses): The novelty of the proposed method seems limited. The idea of using entropy to group tokens has been explored in prior works such as (1), and the proposed entropy adaptive clipping is similar to dynamic clipping in DCPO (2). The proposed method is also very similar to SPO (3), which also decomposes sequences into groups based on entropy.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2512.00499.md#weaknesses): While the paper presents a compelling approach, I have identified several weaknesses that warrant further consideration. First, the paper's experimental evaluation is primarily focused on mathematical reasoning tasks, specifically AIME 2024/2025, HMMT, and MATH500, all of which are administered in English. This narrow focus limits the generalizability of the findings.…

<a id="arxiv-2511.20347"></a>
### Soft Adaptive Policy Optimization

`arxiv:2511.20347` · Post-training · 2025-11-25

- final **+0.12** (conf 1.00, pct 54) · impact -0.32 · WATCH
- mean rating (1–10): **6.3** · accept votes **5/7** · percentile rank_avg 60.5 (100=best) · rank in year 33.0 (1=best)
- NAIPv2 `-0.818` · NAIP-v1 `0.581` · SciJudge `-1.889` · DGC-BERT `0.819`
- CycleReviewer 8B `5.8` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.0` Reject (S/P/C 2.5/3.0/2.5) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2511.20347.md#weaknesses): The main weakness of the paper is the lack of novelty. The proposed algorithm is based on existing techniques, such as group-based policy optimization and soft clipping, and does not introduce any new ideas or techniques. The experimental results are also not very convincing, as the proposed algorithm only shows a small improvement over the existing algorithms.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2511.20347.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further consideration. Firstly, the paper's experimental evaluation is primarily focused on mathematical reasoning benchmarks and the training of the Qwen3-VL model series.…

<a id="arxiv-2511.07317"></a>
### RLVE: Scaling Up Reinforcement Learning for Language Models with Adaptive Verifiable Environments

`arxiv:2511.07317` · Post-training · 2025-11-10

- final **+0.37** (conf 1.00, pct 86) · impact -0.24 · KEEP
- mean rating (1–10): **6.5** · accept votes **5/7** · percentile rank_avg 61.2 (100=best) · rank in year 30.0 (1=best)
- NAIPv2 `-0.931` · NAIP-v1 `0.519` · SciJudge `-0.150` · DGC-BERT `0.547`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.2` Reject · 7B Fast `6.8` Accept (S/P/C 3.25/3.25/3.0) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2511.07317.md#weaknesses): The paper does not provide a clear comparison with other RL training frameworks. The authors should compare RLVE with other RL training frameworks, such as RLVR and ProRL, and show how RLVE improves upon them. - The paper does not provide a clear analysis of the performance of RLVE on different types of reasoning benchmarks.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2511.07317.md#weaknesses): While I am impressed with the contributions of this paper, I have identified several weaknesses that warrant further discussion. First, the paper's reliance on a manually curated suite of verifiable environments raises concerns about scalability and generalizability. As the authors themselves acknowledge, the construction of RLVE-Gym required substantial human effort and expert knowledge.…

<a id="arxiv-2510.14901"></a>
### Reasoning with Sampling: Your Base Model is Smarter Than You Think

`arxiv:2510.14901` · Post-training · 2025-10-16

- final **+0.21** (conf 1.00, pct 66) · impact -0.02 · KEEP
- mean rating (1–10): **6.5** · accept votes **6/7** · percentile rank_avg 62.7 (100=best) · rank in year 21.0 (1=best)
- NAIPv2 `-1.463` · NAIP-v1 `0.513` · SciJudge `0.607` · DGC-BERT `0.885`
- CycleReviewer 8B `5.8` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `7.0` Accept (S/P/C 3.0/3.25/3.0) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2510.14901.md#weaknesses): 1. The paper claims that the proposed method is training-free, but it requires additional inference-time computation. The paper should discuss the trade-off between training time and inference time. 2. The paper only compares the proposed method with GRPO, which is a specific RL-based method. It would be better to compare it with other RL-based methods as well. 3.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2510.14901.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, while the paper demonstrates impressive performance on the chosen benchmarks, it lacks a thorough analysis of the computational cost associated with the proposed power sampling method.…

<a id="arxiv-2510.13786"></a>
### The Art of Scaling Reinforcement Learning Compute for LLMs

`arxiv:2510.13786` · Post-training · 2025-10-15

- final **+0.42** (conf 1.00, pct 89) · impact +0.98 · KEEP
- mean rating (1–10): **6.3** · accept votes **6/7** · percentile rank_avg 74.8 (100=best) · rank in year 4.0 (1=best)
- NAIPv2 `0.044` · NAIP-v1 `0.693` · SciJudge `1.574` · DGC-BERT `0.852`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `8.0` Accept · 7B Fast `6.8` Accept (S/P/C 3.25/3.25/3.25) · 14B Fast `6.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [lovedeathtransformers/9883](https://t.me/lovedeathtransformers/9883), [axisofordinary/7787](https://t.me/axisofordinary/7787)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2510.13786.md#weaknesses): 1. The authors only study the scaling law of RL for LLMs, but do not discuss the scaling law of RL for other tasks, such as robotics and game playing. 2. The authors do not provide a theoretical analysis of the scaling law of RL for LLMs. 3. The authors do not discuss the limitations of the proposed method.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2510.13786.md#weaknesses): While this paper makes significant contributions, several weaknesses warrant attention. First, the paper's focus on a single task, verifiable math, limits the generalizability of the findings. Although the authors include a multi-task experiment with math and code, the primary analysis and the ScaleRL recipe are centered around verifiable math.…

<a id="arxiv-2510.00977"></a>
### It Takes Two: Your GRPO Is Secretly DPO

`arxiv:2510.00977` · Post-training · 2025-10-01

- final **-0.10** (conf 1.00, pct 24) · impact -1.37 · WATCH
- mean rating (1–10): **5.7** · accept votes **5/7** · percentile rank_avg 43.7 (100=best) · rank in year 66.0 (1=best)
- NAIPv2 `-0.455` · NAIP-v1 `0.411` · SciJudge `-3.230` · DGC-BERT `0.614`
- CycleReviewer 8B `5.2` Reject · 70B `` 
- DeepReviewer 7B Std `6.2` Accept · 7B Fast `4.8` Reject (S/P/C 2.5/2.75/2.25) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [dealerAI/1498](https://t.me/dealerAI/1498)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2510.00977.md#weaknesses): 1. The authors only provide a theoretical analysis of 2-GRPO and empirical results on a single dataset. The authors should provide more empirical results on other datasets to validate the effectiveness of 2-GRPO. 2. The authors should provide more details about the implementation of 2-GRPO and the hyperparameters used in the experiments. 3.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2510.00977.md#weaknesses): While this paper presents valuable insights and a promising new approach, several weaknesses warrant careful consideration. First, the paper's experimental evaluation, while demonstrating the efficiency of 2-GRPO, lacks a comprehensive comparison with other reinforcement learning algorithms, particularly those used in similar settings.…

<a id="arxiv-2509.25123"></a>
### From $f(x)$ and $g(x)$ to $f(g(x))$: LLMs Learn New Skills in RL by Composing Old Ones

`arxiv:2509.25123` · Post-training · 2025-09-29

- final **-0.06** (conf 1.00, pct 30) · impact -0.11 · WATCH
- mean rating (1–10): **5.8** · accept votes **5/7** · percentile rank_avg 50.8 (100=best) · rank in year 54.0 (1=best)
- NAIPv2 `-0.188` · NAIP-v1 `0.603` · SciJudge `-0.986` · DGC-BERT `0.417`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `4.2` Reject (S/P/C 2.25/2.25/2.25) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/7729](https://t.me/axisofordinary/7729)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2509.25123.md#weaknesses): The paper's focus on synthetic tasks may limit its generalizability to real-world applications. - The paper does not provide a clear answer to the question of how to incentivize skill acquisition in RL. - The paper does not provide a clear answer to the question of whether the skills learned by LLMs during RL are transferable to other tasks.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2509.25123.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, the paper's definition of 'new skills' as the ability to perform compositional reasoning, while central to the argument, is not entirely novel. As the authors themselves acknowledge, the idea that compositional reasoning can be learned through appropriate training is not new.…

<a id="arxiv-2509.14234"></a>
### Compute as Teacher: Turning Inference Compute Into Reference-Free Supervision

`arxiv:2509.14234` · Post-training · 2025-09-17

- final **+0.06** (conf 1.00, pct 47) · impact +0.12 · WATCH
- mean rating (1–10): **6.0** · accept votes **5/7** · percentile rank_avg 51.2 (100=best) · rank in year 52.0 (1=best)
- NAIPv2 `-1.042` · NAIP-v1 `0.547` · SciJudge `0.707` · DGC-BERT `0.040`
- CycleReviewer 8B `4.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.2` Accept · 7B Fast `6.2` Accept (S/P/C 2.75/3.0/2.5) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [gonzo_ML/4151](https://t.me/gonzo_ML/4151), [axisofordinary/7681](https://t.me/axisofordinary/7681)
- Weaknesses:
  - [OR-8B](reviews/openreviewer-8b/arxiv_2509.14234.md#weaknesses): 1. The paper does not provide a detailed analysis of the computational overhead introduced by the CaT framework. While it claims to reduce inference-time compute requirements, it is important to quantify the additional compute needed for tasks such as rubric generation and synthesis. A more comprehensive analysis of the computational trade-offs would strengthen the paper. 2.…

<a id="arxiv-2509.13232"></a>
### Single-stream Policy Optimization

`arxiv:2509.13232` · Post-training · 2025-09-16

- final **-0.07** (conf 1.00, pct 29) · impact +0.40 · WATCH
- mean rating (1–10): **6.0** · accept votes **5/7** · percentile rank_avg 54.3 (100=best) · rank in year 43.0 (1=best)
- NAIPv2 `-0.961` · NAIP-v1 `0.567` · SciJudge `1.527` · DGC-BERT `0.947`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.0` Reject · 7B Fast `7.0` Accept (S/P/C 3.0/3.25/2.75) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2509.13232.md#weaknesses): 1. The paper lacks a theoretical analysis of the proposed method. 2. The experiments are not comprehensive. The authors only compare with GRPO, but there are other baselines such as A*-PO (1), RLOO (2), and Lite PPO (3). 3. The paper does not discuss the limitations of the proposed method. 4. The paper does not provide any insights into why SPO outperforms GRPO.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2509.13232.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, while the paper introduces a Bayesian tabular tracker, it lacks a detailed explanation of its implementation within a distributed training context.…

<a id="arxiv-2509.03646"></a>
### Emergent Hierarchical Reasoning in LLMs through Reinforcement Learning

`arxiv:2509.03646` · Post-training · 2025-09-03

- final **-0.05** (conf 1.00, pct 31) · impact +0.25 · WATCH
- mean rating (1–10): **5.9** · accept votes **3/7** · percentile rank_avg 57.1 (100=best) · rank in year 41.0 (1=best)
- NAIPv2 `-0.492` · NAIP-v1 `0.669` · SciJudge `-0.602` · DGC-BERT `0.871`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.2` Reject · 7B Fast `5.5` Reject (S/P/C 2.75/2.75/2.5) · 14B Fast `6.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [axisofordinary/7653](https://t.me/axisofordinary/7653), [tech_priestess/2386](https://t.me/tech_priestess/2386)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2509.03646.md#weaknesses): 1. The paper assumes that the reasoning process can be decomposed into high-level planning and low-level execution. This assumption is not always valid. For example, in the case of mathematical problem-solving, the high-level plan and low-level execution are often intertwined. The authors should provide more evidence to support their assumption.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2509.03646.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. First, the paper lacks a thorough analysis of the hyperparameter α, which controls the amplification intensity of planning token rewards in HICRA.…

<a id="arxiv-2508.07629"></a>
### Klear-Reasoner: Advancing Reasoning Capability via Gradient-Preserving Clipping Policy Optimization

`arxiv:2508.07629` · Post-training · 2025-08-11

- final **-0.23** (conf 0.82, pct 18) · impact -0.88 · DROP
- mean rating (1–10): **5.8** · accept votes **3/6** · percentile rank_avg 37.7 (100=best) · rank in year 70.0 (1=best)
- NAIPv2 `-1.587` · NAIP-v1 `0.330` · SciJudge `0.554` · DGC-BERT `0.049`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std ``  · 7B Fast `5.2` Reject (S/P/C 2.75/3.0/2.5) · 14B Fast `6.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2508.07629.md#weaknesses): The paper focuses on a specific problem of clipping in RL, which may limit its generalizability to other areas of research. - The paper does not provide a detailed comparison with other state-of-the-art models, making it difficult to evaluate the effectiveness of the proposed method. - The paper does not discuss potential limitations or drawbacks of the proposed method.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2508.07629.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, while the paper introduces GPPO as a novel approach to address limitations of standard PPO, the motivation for the specific design choices in GPPO could be more thoroughly explained.…

<a id="arxiv-2508.05629"></a>
### On the Generalization of SFT: A Reinforcement Learning Perspective with Reward Rectification

`arxiv:2508.05629` · Post-training · 2025-08-07

- final **+0.43** (conf 1.00, pct 91) · impact -0.51 · KEEP
- mean rating (1–10): **6.4** · accept votes **6/7** · percentile rank_avg 67.7 (100=best) · rank in year 12.0 (1=best)
- NAIPv2 `1.032` · NAIP-v1 `0.536` · SciJudge `-2.038` · DGC-BERT `0.950`
- CycleReviewer 8B `5.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.4` Accept · 7B Fast `7.0` Accept (S/P/C 3.25/3.25/3.25) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [buckwheat_thoughts/297](https://t.me/buckwheat_thoughts/297), [abstractDL/345](https://t.me/abstractDL/345)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2508.05629.md#weaknesses): The theoretical analysis in Section 3.2 is not very convincing. The authors claim that SFT can be viewed as a form of policy gradient with a sparse reward function, which is inversely proportional to the model's probability of expert actions. However, this is not a new observation. The authors should provide a more rigorous proof of this claim.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2508.05629.md#weaknesses): . Finally, the paper's focus on improving SFT, a widely used technique, is highly relevant and timely in the context of large language models. The proposed method has the potential to significantly impact the way these models are fine-tuned for various downstream tasks.

<a id="arxiv-2507.19457"></a>
### GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning

`arxiv:2507.19457` · Post-training · 2025-07-25

- final **+0.45** (conf 1.00, pct 92) · impact -0.09 · KEEP
- mean rating (1–10): **6.3** · accept votes **6/7** · percentile rank_avg 66.8 (100=best) · rank in year 14.0 (1=best)
- NAIPv2 `2.922` · NAIP-v1 `0.504` · SciJudge `0.591` · DGC-BERT `0.518`
- CycleReviewer 8B `5.2` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.5` Accept (S/P/C 2.75/3.0/2.5) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [gonzo_ML/3879](https://t.me/gonzo_ML/3879), [axisofordinary/7502](https://t.me/axisofordinary/7502)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2507.19457.md#weaknesses): The proposed method is not novel. The idea of using a genetic algorithm to search for better prompts has been explored in previous work, such as EvoPrompt (1). The authors should provide a more detailed comparison with existing methods. - The evaluation of the proposed method is not comprehensive.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2507.19457.md#weaknesses): While I find the paper to be generally strong, there are several weaknesses that I believe warrant further discussion. First, while the paper introduces GEPA as a method that leverages natural language reflection, it lacks a detailed comparison with other methods that also use LLMs for reflection and self-improvement.…

<a id="arxiv-2507.18071"></a>
### Group Sequence Policy Optimization

`arxiv:2507.18071` · Post-training · 2025-07-24

- final **+0.04** (conf 1.00, pct 43) · impact -0.31 · WATCH
- mean rating (1–10): **5.5** · accept votes **5/7** · percentile rank_avg 48.0 (100=best) · rank in year 60.0 (1=best)
- NAIPv2 `-1.184` · NAIP-v1 `0.424` · SciJudge `1.173` · DGC-BERT `0.875`
- CycleReviewer 8B `4.2` Reject · 70B `` 
- DeepReviewer 7B Std `7.0` Accept · 7B Fast `4.8` Reject (S/P/C 2.5/2.75/2.25) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [data_secrets/7470](https://t.me/data_secrets/7470), [dealerAI/1474](https://t.me/dealerAI/1474)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2507.18071.md#weaknesses): 1. The paper lacks a detailed theoretical analysis of the proposed algorithm, GSPO. While the authors provide some intuition behind the algorithm, a more rigorous theoretical analysis would strengthen the paper. 2. The paper only compares GSPO with GRPO, and it would be beneficial to include comparisons with other state-of-the-art methods for training large language models using RL. 3.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2507.18071.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further consideration. First, the paper lacks a thorough discussion of the limitations of GSPO. While the authors present GSPO as a robust and scalable algorithm, they do not explicitly address scenarios where it might struggle or fail.…

<a id="arxiv-2506.13585"></a>
### MiniMax-M1: Scaling Test-Time Compute Efficiently with Lightning Attention

`arxiv:2506.13585` · Post-training · 2025-06-16

- final **+0.35** (conf 1.00, pct 83) · impact -0.19 · KEEP
- mean rating (1–10): **6.0** · accept votes **4/7** · percentile rank_avg 52.5 (100=best) · rank in year 48.0 (1=best)
- NAIPv2 `1.191` · NAIP-v1 `0.258` · SciJudge `3.618` · DGC-BERT `0.306`
- CycleReviewer 8B `4.8` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `5.5` Reject (S/P/C 3.25/3.25/3.0) · 14B Fast `8.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2506.13585.md#weaknesses): The authors claim that MiniMax-M1 is the world's first open-weight, large-scale hybrid-attention reasoning model, but there are many other open-source LLMs that use hybrid attention, such as Hunyuan-T1 (https://arxiv.org/abs/2305.14360). The authors should compare MiniMax-M1 with these models and discuss the differences.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2506.13585.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. First, the paper's evaluation of the CISPO algorithm is not as comprehensive as it could be.…

<a id="arxiv-2506.06632"></a>
### Curriculum Reinforcement Learning from Easy to Hard Tasks Improves LLM Reasoning

`arxiv:2506.06632` · Post-training · 2025-06-07

- final **+0.05** (conf 1.00, pct 43) · impact -0.48 · WATCH
- mean rating (1–10): **5.9** · accept votes **5/7** · percentile rank_avg 51.7 (100=best) · rank in year 51.0 (1=best)
- NAIPv2 `1.160` · NAIP-v1 `0.422` · SciJudge `0.690` · DGC-BERT `0.832`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `5.2` Reject · 7B Fast `6.5` Accept (S/P/C 3.0/3.0/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2506.06632.md#weaknesses): 1. The proposed method is not novel. There are many previous works on curriculum learning for LLMs, such as (1,2,3). The authors should compare the proposed method with these works. 2. The theoretical analysis is not rigorous. The authors assume that the curriculum is well-designed, but it is not clear how to design a good curriculum.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2506.06632.md#weaknesses): Despite its strengths, the paper exhibits several weaknesses that warrant careful consideration. First, the experimental evaluation, while demonstrating the potential of the E2H Reasoner, is limited in scope. The authors primarily use the Qwen-1.5B-Instruct model for their main experiments, as explicitly stated in Section 4.1.…

<a id="arxiv-2506.03106"></a>
### Critique-GRPO: Advancing LLM Reasoning with Natural Language and Numerical Feedback

`arxiv:2506.03106` · Post-training · 2025-06-03

- final **+0.42** (conf 1.00, pct 90) · impact +0.94 · KEEP
- mean rating (1–10): **6.5** · accept votes **7/7** · percentile rank_avg 78.1 (100=best) · rank in year 2.0 (1=best)
- NAIPv2 `1.530` · NAIP-v1 `0.635` · SciJudge `2.324` · DGC-BERT `0.909`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/2.75) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2506.03106.md#weaknesses): The main weakness of the paper is the limited novelty. The paper builds on existing work on RL methods for improving the reasoning capabilities of LLMs and combines numerical and natural language feedback. The method is not significantly different from existing methods, and the results are not surprising. The paper also lacks a thorough comparison with existing methods.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2506.03106.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further consideration. First, while the paper introduces the concept of natural language critiques, it does not delve deeply enough into the nuances of different critique types and their impact on the learning process.…

<a id="arxiv-2506.01939"></a>
### Beyond the 80/20 Rule: High-Entropy Minority Tokens Drive Effective Reinforcement Learning for LLM Reasoning

`arxiv:2506.01939` · Post-training · 2025-06-02

- final **+0.27** (conf 1.00, pct 74) · impact +0.65 · KEEP
- mean rating (1–10): **6.2** · accept votes **4/7** · percentile rank_avg 60.0 (100=best) · rank in year 35.0 (1=best)
- NAIPv2 `-1.289` · NAIP-v1 `0.601` · SciJudge `1.946` · DGC-BERT `0.275`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `5.8` Reject (S/P/C 2.75/2.75/2.75) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [axisofordinary/7296](https://t.me/axisofordinary/7296), [tech_priestess/2386](https://t.me/tech_priestess/2386)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2506.01939.md#weaknesses): The main weakness of the paper is that the results are not very surprising and do not seem to have a significant impact on the field. The paper is essentially showing that high-entropy tokens are important for reasoning, which is already known.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2506.01939.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further consideration. First, the paper's reliance on a single RLVR algorithm, DAPO, limits the generalizability of its findings. While DAPO is a state-of-the-art method, the authors do not explore whether their observations about high-entropy tokens hold true for other RLVR algorithms, such as PPO or GRPO.…

<a id="arxiv-2505.19590"></a>
### Learning to Reason without External Rewards

`arxiv:2505.19590` · Post-training · 2025-05-26

- final **+0.00** (conf 1.00, pct 36) · impact +0.40 · WATCH
- mean rating (1–10): **5.3** · accept votes **3/7** · percentile rank_avg 51.9 (100=best) · rank in year 50.0 (1=best)
- NAIPv2 `1.556` · NAIP-v1 `0.594` · SciJudge `1.067` · DGC-BERT `0.822`
- CycleReviewer 8B `4.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.2` Reject · 7B Fast `4.8` Reject (S/P/C 2.5/2.75/2.25) · 14B Fast `6.0` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `7.0` Accept
- Telegram: [gonzo_ML/3767](https://t.me/gonzo_ML/3767), [axisofordinary/7262](https://t.me/axisofordinary/7262), [axisofordinary/8273](https://t.me/axisofordinary/8273)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2505.19590.md#weaknesses): 1. The paper lacks novelty. The proposed method is simple and straightforward. The method is similar to the previous work (1) which uses the self-certainty as the reward signal for RLHF. 2. The paper lacks theoretical analysis. The paper does not provide any theoretical analysis of the proposed method. 3. The paper lacks ablation study.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2505.19590.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, the paper's reliance on self-certainty as the sole reward signal raises concerns about the potential for bias and manipulation.…

<a id="arxiv-2505.10978"></a>
### Group-in-Group Policy Optimization for LLM Agent Training

`arxiv:2505.10978` · Post-training · 2025-05-16

- final **+0.31** (conf 1.00, pct 79) · impact +0.58 · KEEP
- mean rating (1–10): **6.3** · accept votes **7/7** · percentile rank_avg 73.4 (100=best) · rank in year 5.0 (1=best)
- NAIPv2 `0.338` · NAIP-v1 `0.675` · SciJudge `0.530` · DGC-BERT `0.888`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `7.0` Accept · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/2.67) · 14B Fast `6.7` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2505.10978.md#weaknesses): The paper does not provide a theoretical analysis of the proposed method, which could help understand its properties and limitations. - The paper does not discuss the limitations of the proposed method, such as potential issues with scalability or generalizability to other tasks.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2505.10978.md#weaknesses): Despite the paper's strengths, I have identified several weaknesses that warrant further discussion. Firstly, the paper's reliance on state matching for anchor group construction raises concerns about its applicability in highly complex environments.…

<a id="arxiv-2504.16084"></a>
### TTRL: Test-Time Reinforcement Learning

`arxiv:2504.16084` · Post-training · 2025-04-22

- final **+0.32** (conf 1.00, pct 80) · impact -0.03 · KEEP
- mean rating (1–10): **6.1** · accept votes **5/7** · percentile rank_avg 62.4 (100=best) · rank in year 23.0 (1=best)
- NAIPv2 `1.952` · NAIP-v1 `0.403` · SciJudge `2.544` · DGC-BERT `0.948`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/3.0) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [gonzo_ML/4151](https://t.me/gonzo_ML/4151)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2504.16084.md#weaknesses): 1. The novelty of this paper is limited. The proposed method is similar to self-play training, which has been widely used in the field of reinforcement learning. The main difference is that the proposed method uses a single model instead of multiple models in self-play training.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2504.16084.md#weaknesses): While the paper presents a compelling approach to test-time reinforcement learning, several limitations warrant careful consideration. First, the scope of the experimental evaluation, while broad in terms of tasks and models, is somewhat limited in terms of the types of reasoning explored.…

<a id="arxiv-2504.13837"></a>
### Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?

`arxiv:2504.13837` · Post-training · 2025-04-18

- final **+0.01** (conf 1.00, pct 38) · impact +0.42 · WATCH
- mean rating (1–10): **5.8** · accept votes **4/7** · percentile rank_avg 50.0 (100=best) · rank in year 56.0 (1=best)
- NAIPv2 `-1.139` · NAIP-v1 `0.544` · SciJudge `1.764` · DGC-BERT `0.742`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `6.5` Accept (S/P/C 3.0/3.0/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `5.0` Reject (S/P/C 2.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [abstractDL/332](https://t.me/abstractDL/332), [data_secrets/8212](https://t.me/data_secrets/8212), [gonzo_ML/4286](https://t.me/gonzo_ML/4286), [lovedeathtransformers/9272](https://t.me/lovedeathtransformers/9272), [boris_again/3157](https://t.me/boris_again/3157), [AGI_and_RL/1058](https://t.me/AGI_and_RL/1058)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2504.13837.md#weaknesses): 1. The paper does not provide a clear explanation for the observed phenomenon. 2. The paper does not provide a clear recommendation for future research directions.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2504.13837.md#weaknesses): While this paper presents a compelling analysis of RLVR, several limitations warrant careful consideration. One significant weakness lies in the paper's definition and use of the term "reasoning capacity boundary." While the authors define this boundary using the pass@k metric, the term is somewhat ambiguous and could be interpreted in different ways.…

<a id="arxiv-2503.20783"></a>
### Understanding R1-Zero-Like Training: A Critical Perspective

`arxiv:2503.20783` · Post-training · 2025-03-26

- final **+0.33** (conf 1.00, pct 82) · impact +0.02 · KEEP
- mean rating (1–10): **6.2** · accept votes **5/7** · percentile rank_avg 61.0 (100=best) · rank in year 31.0 (1=best)
- NAIPv2 `1.818` · NAIP-v1 `0.442` · SciJudge `2.137` · DGC-BERT `0.447`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.5` Accept (S/P/C 3.0/3.0/2.75) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2503.20783.md#weaknesses): 1. The paper lacks novelty. The authors have identified two issues in the R1-zero-like training, but the proposed solution is simply removing the normalization terms in the GRPO algorithm, which is a straightforward fix. 2. The paper lacks experiments. The authors have only conducted experiments on a small number of models and datasets, and the results are not convincing.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2503.20783.md#weaknesses): While this paper presents several valuable contributions, there are some limitations that warrant careful consideration. One significant weakness is the lack of a thorough investigation into the sensitivity of Dr. GRPO to different reward functions.…

<a id="arxiv-2503.14476"></a>
### DAPO: An Open-Source LLM Reinforcement Learning System at Scale

`arxiv:2503.14476` · Post-training · 2025-03-18

- final **-0.32** (conf 1.00, pct 11) · impact +0.32 · DROP
- mean rating (1–10): **6.0** · accept votes **3/7** · percentile rank_avg 46.2 (100=best) · rank in year 65.0 (1=best)
- NAIPv2 `-1.369` · NAIP-v1 `0.501` · SciJudge `2.162` · DGC-BERT `0.160`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `4.0` Reject · 7B Fast `5.0` Reject (S/P/C 2.5/2.5/2.5) · 14B Fast `6.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [axisofordinary/7039](https://t.me/axisofordinary/7039), [AGI_and_RL/1061](https://t.me/AGI_and_RL/1061)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2503.14476.md#weaknesses): The paper does not include any ablation studies to show the impact of each modification to the GRPO algorithm. This makes it difficult to determine which modifications are most important for the improved performance.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2503.14476.md#weaknesses): While I appreciate the contributions of this paper, I have identified several weaknesses that warrant further discussion. First, the paper lacks a detailed analysis of the computational resources required by the DAPO algorithm. While the authors mention using the verl framework, they do not provide specific information on GPU memory usage, training time per epoch, or total training time.…

<a id="arxiv-2503.02875"></a>
### The First Few Tokens Are All You Need: An Efficient and Effective Unsupervised Prefix Fine-Tuning Method for Reasoning Models

`arxiv:2503.02875` · Post-training · 2025-03-04

- final **-0.07** (conf 1.00, pct 29) · impact +0.85 · WATCH
- mean rating (1–10): **6.2** · accept votes **3/7** · percentile rank_avg 58.6 (100=best) · rank in year 38.0 (1=best)
- NAIPv2 `-1.960` · NAIP-v1 `0.596` · SciJudge `2.834` · DGC-BERT `0.817`
- CycleReviewer 8B `5.5` Reject · 70B `` 
- DeepReviewer 7B Std `5.8` Reject · 7B Fast `5.8` Reject (S/P/C 2.75/2.75/2.75) · 14B Fast `6.5` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [data_secrets/6419](https://t.me/data_secrets/6419), [axisofordinary/7009](https://t.me/axisofordinary/7009)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2503.02875.md#weaknesses): The authors claim that the proposed method is "unsupervised" in the sense that it does not require labeled data or rejection sampling. However, the method still requires a dataset of questions and answers, which is not entirely unsupervised. In addition, the authors use a subset of the dataset for full reasoning trace generation, which is still supervised.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2503.02875.md#weaknesses): section, there are several limitations that need to be addressed to fully validate the claims made in the paper.

<a id="arxiv-2503.00735"></a>
### LADDER: Self-Improving LLMs Through Recursive Problem Decomposition

`arxiv:2503.00735` · Post-training · 2025-03-02

- final **-0.01** (conf 1.00, pct 34) · impact +1.21 · WATCH
- mean rating (1–10): **6.0** · accept votes **4/7** · percentile rank_avg 59.7 (100=best) · rank in year 37.0 (1=best)
- NAIPv2 `-0.900` · NAIP-v1 `0.600` · SciJudge `3.799` · DGC-BERT `0.731`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.0` Reject · 7B Fast `6.0` Reject (S/P/C 3.0/3.0/3.0) · 14B Fast `6.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [AGI_and_RL/986](https://t.me/AGI_and_RL/986), [axisofordinary/7020](https://t.me/axisofordinary/7020)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2503.00735.md#weaknesses): The paper focuses on mathematical integration tasks, which may not be representative of all types of complex tasks that LLMs need to solve. It would be helpful to see if the approach works on other types of tasks as well. - The paper does not provide a detailed analysis of the computational cost of the approach.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2503.00735.md#weaknesses): While the LADDER framework presents a promising approach, several limitations warrant careful consideration. One significant concern is the limited scope of the experimental evaluation. The paper focuses exclusively on mathematical integration, a domain with well-defined rules and a clear verification mechanism.…

<a id="arxiv-2402.13669"></a>
### Self-Distillation Bridges Distribution Gap in Language Model Fine-Tuning

`arxiv:2402.13669` · Post-training · 2024-02-21

- final **+0.22** (conf 1.00, pct 67) · impact +0.32 · KEEP
- mean rating (1–10): **6.4** · accept votes **5/7** · percentile rank_avg 62.0 (100=best) · rank in year 6.0 (1=best)
- NAIPv2 `0.723` · NAIP-v1 `0.570` · SciJudge `1.287` · DGC-BERT `0.909`
- CycleReviewer 8B `5.5` Reject · 70B `` 
- DeepReviewer 7B Std `4.2` Reject · 7B Fast `6.0` Accept (S/P/C 2.67/3.0/2.67) · 14B Fast `6.7` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2402.13669.md#weaknesses): 1. The paper does not provide a thorough analysis of the limitations of the proposed method. For example, the paper does not discuss the computational cost of generating the distilled dataset, or the potential trade-off between performance and computational cost. 2. The paper does not provide a comparison with other methods for mitigating catastrophic forgetting in LLM fine-tuning.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2402.13669.md#weaknesses): section, the paper has some limitations in terms of experimental scope and theoretical depth that need to be addressed.

<a id="arxiv-2402.03300"></a>
### DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models

`arxiv:2402.03300` · Post-training · 2024-02-05

- final **+0.32** (conf 1.00, pct 81) · impact +0.57 · KEEP
- mean rating (1–10): **6.2** · accept votes **5/7** · percentile rank_avg 57.0 (100=best) · rank in year 14.0 (1=best)
- NAIPv2 `-1.261` · NAIP-v1 `0.440` · SciJudge `3.816` · DGC-BERT `0.859`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `5.5` Reject (S/P/C 3.0/3.0/3.0) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [AGI_and_RL/948](https://t.me/AGI_and_RL/948), [gonzo_ML/3239](https://t.me/gonzo_ML/3239), [buckwheat_thoughts/105](https://t.me/buckwheat_thoughts/105), [gonzo_ML/4555](https://t.me/gonzo_ML/4555), [data_secrets/3942](https://t.me/data_secrets/3942), [buckwheat_thoughts/104](https://t.me/buckwheat_thoughts/104), [gonzo_ML/4303](https://t.me/gonzo_ML/4303), [gonzo_ML/3319](https://t.me/gonzo_ML/3319)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2402.03300.md#weaknesses): 1. The paper does not provide a detailed analysis of the data selection pipeline used to construct the DeepSeekMath Corpus. It would be helpful to have a more detailed description of the data selection process, including how the data was filtered and how the quality of the data was assessed.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2402.03300.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant attention. First, the paper lacks a detailed analysis of the model's failure cases. While the authors present overall performance metrics, there is no discussion of the types of mathematical problems that DeepSeekMath struggles with.…

<a id="arxiv-2303.17651"></a>
### Self-Refine: Iterative Refinement with Self-Feedback

`arxiv:2303.17651` · Post-training · 2023-03-30

- final **+0.10** (conf 1.00, pct 52) · impact +1.71 · WATCH
- mean rating (1–10): **6.2** · accept votes **6/7** · percentile rank_avg 60.5 (100=best) · rank in year 10.0 (1=best)
- NAIPv2 `-2.209` · NAIP-v1 `0.704` · SciJudge `4.050` · DGC-BERT `0.851`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `5.8` Accept (S/P/C 3.0/3.0/2.5) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [gonzo_ML/1467](https://t.me/gonzo_ML/1467)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2303.17651.md#weaknesses): The paper evaluates Self-Refine on a limited number of tasks, and it is not clear how well the approach would perform on other tasks or domains. The paper also does not provide a detailed comparison with other approaches that use feedback and refinement to improve LLM outputs.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2303.17651.md#weaknesses): While the paper presents a compelling method, several weaknesses warrant careful consideration. First, the paper's evaluation lacks a crucial comparison with a baseline that uses a larger number of samples from the same model.…

<a id="arxiv-2608.11676"></a>
### XBridge: Entity-Grounded Latent Bridge for Heterogeneous LLM Communication

`arxiv:2608.11676` · LLMs: architectures, context, training · 2026-08-12

- final **+0.25** (conf 1.00, pct 72) · impact -0.45 · KEEP
- mean rating (1–10): **6.2** · accept votes **5/7** · percentile rank_avg 56.7 (100=best) · rank in year 34.0 (1=best)
- NAIPv2 `-0.440` · NAIP-v1 `0.609` · SciJudge `-3.188` · DGC-BERT `0.209`
- CycleReviewer 8B `6.0` Reject · 70B `` 
- DeepReviewer 7B Std `7.0` Accept · 7B Fast `5.7` Accept (S/P/C 3.0/3.0/2.33) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2608.11676.md#weaknesses): 1. The proposed method is only evaluated on a limited set of benchmarks, and it is unclear how the method will perform on other tasks. 2. The method requires training a separate bridge for each sender-receiver pair, which may be computationally expensive. 3. The method assumes that the sender and receiver have the same vocabulary, which may not always be the case in real-world applications.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2608.11676.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further consideration. First, while the paper introduces the concept of the 'entity grounding problem' and provides a clear explanation of the 'rare-token compression collapse,' the explanation of *why* this collapse occurs is somewhat superficial.…

<a id="arxiv-2608.03893"></a>
### Cross-Model KV Cache Transfer in LLM Families: A Closed-Form Linear Mapping for Prefill Reuse

`arxiv:2608.03893` · LLMs: architectures, context, training · 2026-08-04

- final **+0.14** (conf 1.00, pct 58) · impact -0.78 · WATCH
- mean rating (1–10): **5.8** · accept votes **5/7** · percentile rank_avg 50.5 (100=best) · rank in year 52.0 (1=best)
- NAIPv2 `-0.026` · NAIP-v1 `0.437` · SciJudge `-0.462` · DGC-BERT `0.067`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.5` Accept (S/P/C 3.0/3.0/2.5) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [lovedeathtransformers/10993](https://t.me/lovedeathtransformers/10993)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2608.03893.md#weaknesses): The proposed method is evaluated on 6 matched-KV pairs across 3 model families. The authors claim that the linear structure in cross-model KV cache transfer is a general phenomenon, but the evaluation is not sufficient to support this claim. - The proposed method is evaluated on 5 accuracy benchmarks.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2608.03893.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, the paper's primary focus on 'matched-KV' configurations, where source and target models share the same number of KV heads and dimensions, limits the generalizability of the proposed method.…

<a id="arxiv-2608.00146"></a>
### DiffusionGemma Technical Report

`arxiv:2608.00146` · LLMs: architectures, context, training · 2026-07-31

- final **+0.29** (conf 1.00, pct 76) · impact +1.45 · KEEP
- mean rating (1–10): **6.7** · accept votes **3/7** · percentile rank_avg 66.3 (100=best) · rank in year 14.0 (1=best)
- NAIPv2 `-0.480` · NAIP-v1 `0.688` · SciJudge `3.275` · DGC-BERT `0.309`
- CycleReviewer 8B `6.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `5.6` Reject (S/P/C 3.0/3.0/3.0) · 14B Fast `8.0` Accept
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/4.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/5942](https://t.me/gonzo_ML/5942)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2608.00146.md#weaknesses): 1. The paper does not provide a detailed comparison with existing methods, making it difficult to assess the novelty and effectiveness of the proposed method. 2. The paper does not provide a detailed analysis of the computational cost of the proposed method, making it difficult to assess its efficiency. 3.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2608.00146.md#weaknesses): While the paper presents a compelling approach to fast text generation, I have identified several weaknesses that warrant further discussion. Firstly, the paper's comparison of DiffusionGemma against the base Gemma 4 model, without including a comparison against a Gemma 4 model fine-tuned with the same data, is a significant limitation.…

<a id="arxiv-2607.02303"></a>
### A Hippocampus for Linear Attention: An Exact Memory for What the Recurrent State Forgets

`arxiv:2607.02303` · LLMs: architectures, context, training · 2026-07-02

- final **+0.24** (conf 1.00, pct 72) · impact +0.37 · KEEP
- mean rating (1–10): **6.2** · accept votes **6/7** · percentile rank_avg 62.1 (100=best) · rank in year 26.0 (1=best)
- NAIPv2 `0.288` · NAIP-v1 `0.584` · SciJudge `1.596` · DGC-BERT `0.693`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.8` Accept · 7B Fast `5.8` Accept (S/P/C 2.75/2.75/2.75) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [gonzo_ML/5675](https://t.me/gonzo_ML/5675)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2607.02303.md#weaknesses): The main weakness of the paper is that the proposed method is not novel. The idea of using a cache to improve the performance of linear attention models has been proposed in previous works such as LTE and NHA. The novelty of this paper is mainly in the way the cache is filled with the most important key-value pairs.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2607.02303.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further consideration. First, while the paper demonstrates strong empirical results, the theoretical underpinnings of the proposed method could be further explored.…

<a id="arxiv-2606.06574"></a>
### Skip a Layer or Loop It? Learning Program-of-Layers in LLMs

`arxiv:2606.06574` · LLMs: architectures, context, training · 2026-06-04

- final **+0.19** (conf 1.00, pct 64) · impact +0.30 · WATCH
- mean rating (1–10): **6.0** · accept votes **6/7** · percentile rank_avg 64.2 (100=best) · rank in year 23.0 (1=best)
- NAIPv2 `-0.587` · NAIP-v1 `0.680` · SciJudge `-0.373` · DGC-BERT `0.957`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.0` Accept (S/P/C 3.25/3.25/3.0) · 14B Fast `6.2` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [gonzo_ML/5950](https://t.me/gonzo_ML/5950)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2606.06574.md#weaknesses): 1. The authors claim that their method can reduce the inference latency. However, the authors only report the number of layers executed, but not the actual inference latency. I think it is more important to report the actual inference latency, as the number of layers executed may not be a good indicator of the actual inference latency. 2.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2606.06574.md#weaknesses): While I find the paper to be generally strong, there are several weaknesses that I believe warrant further discussion. First, the paper lacks a detailed analysis of the computational overhead introduced by the proposed method.…

<a id="arxiv-2605.22863"></a>
### Latent Cache Flow: Model-to-Model Communication Without Text

`arxiv:2605.22863` · LLMs: architectures, context, training · 2026-05-19

- final **-0.16** (conf 1.00, pct 22) · impact -0.76 · WATCH
- mean rating (1–10): **5.7** · accept votes **4/7** · percentile rank_avg 37.3 (100=best) · rank in year 66.0 (1=best)
- NAIPv2 `-1.681` · NAIP-v1 `0.490` · SciJudge `-2.391` · DGC-BERT `0.281`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/3.0) · 14B Fast `5.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2605.22863.md#weaknesses): 1. The novelty of this paper is limited. The idea of compressing the key-value cache into a lower-dimensional latent space is not new. In fact, the authors mentioned that "KV states can be compressed within a model" in the paper. The novelty of this paper lies in the application of this idea to LLM communication. 2. The experiments are not convincing.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2605.22863.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. First, the paper lacks a comprehensive discussion of related work, particularly concerning alternative methods for model-to-model communication.…

<a id="arxiv-2604.08302"></a>
### DMax: Aggressive Parallel Decoding for dLLMs

`arxiv:2604.08302` · LLMs: architectures, context, training · 2026-04-09

- final **+0.21** (conf 1.00, pct 66) · impact -0.54 · KEEP
- mean rating (1–10): **6.2** · accept votes **4/7** · percentile rank_avg 56.0 (100=best) · rank in year 40.0 (1=best)
- NAIPv2 `2.402` · NAIP-v1 `0.470` · SciJudge `-0.175` · DGC-BERT `0.709`
- CycleReviewer 8B `5.8` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `7.5` Accept (S/P/C 3.25/3.25/3.25) · 14B Fast `6.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/5420](https://t.me/gonzo_ML/5420)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2604.08302.md#weaknesses): The proposed method is not novel enough. The idea of using mask embedding and token embedding to represent the intermediate state in parallel decoding has been explored in previous works such as SM (1) and EvoToken (2). The main difference is that the proposed method uses the mask embedding as a prior to represent the uncertainty of the model.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2604.08302.md#weaknesses): While the paper presents a compelling approach to parallel decoding in diffusion language models, several limitations warrant careful consideration. First, the evaluation is primarily focused on LLaDA-2.0-mini as the base model. While the paper demonstrates significant improvements on this model, the generalizability of DMax to other diffusion language model architectures remains unclear.…

<a id="arxiv-2603.05454"></a>
### Beyond Scattered Acceptance: Fast and Coherent Inference for DLMs via Longest Stable Prefixes

`arxiv:2603.05454` · LLMs: architectures, context, training · 2026-03-05

- final **+0.05** (conf 1.00, pct 45) · impact +0.37 · WATCH
- mean rating (1–10): **6.0** · accept votes **5/7** · percentile rank_avg 59.4 (100=best) · rank in year 33.0 (1=best)
- NAIPv2 `-0.349` · NAIP-v1 `0.573` · SciJudge `1.675` · DGC-BERT `0.820`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.2` Accept · 7B Fast `5.8` Reject (S/P/C 2.75/2.75/2.75) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [derplearning/4956](https://t.me/derplearning/4956)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2603.05454.md#weaknesses): The proposed method is only evaluated on two DLMs, and it is unclear how the proposed method would perform on other DLMs. - The proposed method is only evaluated on a limited set of benchmarks, and it is unclear how the proposed method would perform on other benchmarks.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2603.05454.md#weaknesses): section, there are some limitations and areas that require further investigation.

<a id="arxiv-2602.08676"></a>
### LLaDA2.1: Speeding Up Text Diffusion via Token Editing

`arxiv:2602.08676` · LLMs: architectures, context, training · 2026-02-09

- final **-0.04** (conf 1.00, pct 32) · impact +0.80 · WATCH
- mean rating (1–10): **5.5** · accept votes **5/7** · percentile rank_avg 54.7 (100=best) · rank in year 41.0 (1=best)
- NAIPv2 `0.517` · NAIP-v1 `0.613` · SciJudge `2.580` · DGC-BERT `0.633`
- CycleReviewer 8B `4.0` Reject · 70B `` 
- DeepReviewer 7B Std `7.0` Accept · 7B Fast `5.5` Reject (S/P/C 2.75/2.25/2.5) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/8164](https://t.me/axisofordinary/8164)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2602.08676.md#weaknesses): 1. The proposed decoding algorithm is not new. There have been many previous works that use a mixture of mask-to-token and token-to-token decoding to improve the decoding efficiency. For example, (1) also uses a mixture of mask-to-token and token-to-token decoding to improve the decoding efficiency.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2602.08676.md#weaknesses): While the paper presents several compelling innovations, there are several weaknesses that warrant careful consideration. Firstly, the paper lacks a detailed analysis of the computational overhead associated with the proposed decoding strategies, particularly Multi-Block Editing (MBE).…

<a id="arxiv-2512.24601"></a>
### Recursive Language Models

`arxiv:2512.24601` · LLMs: architectures, context, training · 2025-12-31

- final **+0.15** (conf 1.00, pct 59) · impact +0.13 · WATCH
- mean rating (1–10): **6.0** · accept votes **4/7** · percentile rank_avg 61.3 (100=best) · rank in year 29.0 (1=best)
- NAIPv2 `1.517` · NAIP-v1 `0.511` · SciJudge `1.123` · DGC-BERT `0.906`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.2` Reject · 7B Fast `5.2` Reject (S/P/C 2.5/2.75/2.25) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [data_secrets/8718](https://t.me/data_secrets/8718), [gonzo_ML/4562](https://t.me/gonzo_ML/4562), [AIHOUSE/1370](https://t.me/AIHOUSE/1370), [axisofordinary/8235](https://t.me/axisofordinary/8235)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2512.24601.md#weaknesses): 1. The paper lacks a detailed discussion of the limitations of RLMs. While the authors mention some limitations in the appendix, a more thorough discussion in the main paper would provide a more balanced view of the approach.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2512.24601.md#weaknesses): While the paper presents a compelling approach, several weaknesses warrant careful consideration. First, the paper's evaluation, while diverse, does not fully explore the potential of RLMs in scenarios that require iterative refinement of information or learning from long-term interactions.…

<a id="arxiv-2512.14856"></a>
### T5Gemma 2: Seeing, Reading, and Understanding Longer

`arxiv:2512.14856` · LLMs: architectures, context, training · 2025-12-16

- final **-0.30** (conf 1.00, pct 13) · impact -0.14 · DROP
- mean rating (1–10): **5.4** · accept votes **2/7** · percentile rank_avg 34.2 (100=best) · rank in year 74.0 (1=best)
- NAIPv2 `-1.177` · NAIP-v1 `0.465` · SciJudge `1.066` · DGC-BERT `0.348`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/2.75) · 14B Fast `5.5` Reject
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/4421](https://t.me/gonzo_ML/4421), [mishin_learning/1867](https://t.me/mishin_learning/1867), [boris_again/3650](https://t.me/boris_again/3650)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2512.14856.md#weaknesses): The paper does not provide a detailed comparison with other existing models in the field, making it difficult to assess its novelty and significance. - The paper does not provide a detailed discussion of the limitations of the proposed methods and potential future research directions.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2512.14856.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. First, the paper's claim of presenting the first capable long-context encoder-decoder LLM is not fully supported by the evidence. While the authors state that T5Gemma 2 can handle contexts up to 128K, the pre-training is only done on sequences up to 16K.…

<a id="arxiv-2512.13961"></a>
### Olmo 3

`arxiv:2512.13961` · LLMs: architectures, context, training · 2025-12-15

- final **+0.22** (conf 1.00, pct 68) · impact +0.45 · KEEP
- mean rating (1–10): **6.3** · accept votes **3/7** · percentile rank_avg 62.5 (100=best) · rank in year 22.0 (1=best)
- NAIPv2 `-0.192` · NAIP-v1 `0.468` · SciJudge `3.346` · DGC-BERT `0.135`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.7` Reject · 7B Fast `6.2` Reject (S/P/C 3.0/3.0/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 4.0/3.0/4.0) · SEA-E `8.0` Accept
- Telegram: [abstractDL/356](https://t.me/abstractDL/356), [j_links/8236](https://t.me/j_links/8236)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2512.13961.md#weaknesses): The paper lacks a clear and concise summary of the main contributions and findings. The introduction is lengthy and does not provide a clear overview of the paper's main contributions. The paper also lacks a clear and concise conclusion that summarizes the main findings and contributions.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2512.13961.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant attention. First, the paper's organization and writing style present a significant challenge to the reader. The sheer volume of information, often presented with excessive detail, makes it difficult to grasp the core contributions and novel aspects of the work.…

<a id="arxiv-2512.15745"></a>
### LLaDA2.0: Scaling Up Diffusion Language Models to 100B

`arxiv:2512.15745` · LLMs: architectures, context, training · 2025-12-10

- final **+0.15** (conf 1.00, pct 59) · impact +0.77 · WATCH
- mean rating (1–10): **6.4** · accept votes **4/7** · percentile rank_avg 62.8 (100=best) · rank in year 20.0 (1=best)
- NAIPv2 `0.392` · NAIP-v1 `0.606` · SciJudge `2.193` · DGC-BERT `0.073`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `5.5` Accept (S/P/C 2.75/2.75/2.75) · 14B Fast `6.5` Reject
- OpenReviewer `8.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [gonzo_ML/5420](https://t.me/gonzo_ML/5420)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2512.15745.md#weaknesses): The paper lacks a clear motivation for the proposed approach. The authors do not provide a clear explanation of why they chose to use a discrete diffusion model instead of an autoregressive model. - The paper does not provide a detailed analysis of the computational cost of the proposed approach.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2512.15745.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant attention. First, the paper lacks a detailed analysis of the Warmup-Stable-Decay (WSD) strategy's impact on model performance. While the authors describe the three phases of WSD, they do not provide specific metrics or visualizations that demonstrate the model's behavior during each phase.…

<a id="arxiv-2511.09149"></a>
### Enabling Agents to Communicate Entirely in Latent Space

`arxiv:2511.09149` · LLMs: architectures, context, training · 2025-11-12

- final **+0.29** (conf 1.00, pct 78) · impact +0.07 · KEEP
- mean rating (1–10): **6.6** · accept votes **4/7** · percentile rank_avg 65.6 (100=best) · rank in year 18.0 (1=best)
- NAIPv2 `0.965` · NAIP-v1 `0.694` · SciJudge `-2.378` · DGC-BERT `0.637`
- CycleReviewer 8B `5.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.2` Reject · 7B Fast `6.0` Reject (S/P/C 3.0/3.0/2.67) · 14B Fast `7.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2511.09149.md#weaknesses): The proposed method is limited to a two-agent setting. It is unclear how it would scale to more complex multi-agent systems. - The method assumes access to internal model representations, which may not be available in all scenarios. - The method is not interpretable and may be difficult to debug or monitor.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2511.09149.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further consideration. First, the paper's evaluation of generalization capabilities is limited. While the authors evaluate Interlat on both ALFWorld and MATH, these benchmarks primarily assess performance on tasks within the same domain.…

<a id="arxiv-2510.26622"></a>
### Encoder-Decoder or Decoder-Only? Revisiting Encoder-Decoder Large Language Model

`arxiv:2510.26622` · LLMs: architectures, context, training · 2025-10-30

- final **+0.06** (conf 1.00, pct 46) · impact -0.23 · WATCH
- mean rating (1–10): **5.9** · accept votes **6/7** · percentile rank_avg 52.4 (100=best) · rank in year 49.0 (1=best)
- NAIPv2 `-0.363` · NAIP-v1 `0.578` · SciJudge `-1.158` · DGC-BERT `0.763`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `5.7` Reject (S/P/C 2.67/2.33/2.67) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/4220](https://t.me/gonzo_ML/4220), [gonzo_ML/4217](https://t.me/gonzo_ML/4217)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2510.26622.md#weaknesses): 1. The authors only compare the performance of the encoder-decoder and decoder-only models on a single pretraining dataset (RedPajama V1). It would be interesting to see how the models perform on other pretraining datasets, such as the Common Crawl dataset used by LLaMA.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2510.26622.md#weaknesses): While this paper presents valuable insights, several limitations warrant careful consideration. First, the paper's central claim that RedLLMs exhibit 'similar scaling exponents' to DecLLMs is not fully supported by the presented evidence.…

<a id="arxiv-2510.03215"></a>
### Cache-to-Cache: Direct Semantic Communication Between Large Language Models

`arxiv:2510.03215` · LLMs: architectures, context, training · 2025-10-03

- final **+0.50** (conf 1.00, pct 96) · impact -0.07 · KEEP
- mean rating (1–10): **6.5** · accept votes **5/7** · percentile rank_avg 67.0 (100=best) · rank in year 13.0 (1=best)
- NAIPv2 `2.059` · NAIP-v1 `0.631` · SciJudge `-1.763` · DGC-BERT `0.227`
- CycleReviewer 8B `5.2` Reject · 70B `` 
- DeepReviewer 7B Std `7.0` Accept · 7B Fast `6.5` Accept (S/P/C 2.75/3.0/2.75) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [data_secrets/8179](https://t.me/data_secrets/8179), [axisofordinary/7864](https://t.me/axisofordinary/7864), [boris_again/4044](https://t.me/boris_again/4044), [nn_for_science/2711](https://t.me/nn_for_science/2711)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2510.03215.md#weaknesses): The paper lacks a clear motivation for why KV cache is a better communication medium than text. The paper mentions that KV cache is a richer representation than text, but it does not provide any evidence to support this claim. In fact, KV cache is a lower-dimensional representation of the input, whereas text is a higher-dimensional representation.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2510.03215.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further consideration. First, while the paper demonstrates the effectiveness of C2C, it lacks a detailed analysis of the computational overhead associated with the cache fusion process itself.…

<a id="arxiv-2507.10524"></a>
### Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation

`arxiv:2507.10524` · LLMs: architectures, context, training · 2025-07-14

- final **+0.17** (conf 1.00, pct 62) · impact +1.26 · WATCH
- mean rating (1–10): **6.0** · accept votes **7/7** · percentile rank_avg 65.7 (100=best) · rank in year 17.0 (1=best)
- NAIPv2 `0.704` · NAIP-v1 `0.743` · SciJudge `1.579` · DGC-BERT `0.916`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `5.2` Accept (S/P/C 2.75/3.0/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [data_secrets/7384](https://t.me/data_secrets/7384), [gonzo_ML/3835](https://t.me/gonzo_ML/3835), [nn_for_science/2498](https://t.me/nn_for_science/2498)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2507.10524.md#weaknesses): The paper does not provide a detailed analysis of the computational cost of the proposed method. - The paper does not provide a detailed analysis of the memory requirements of the proposed method. - The paper does not provide a detailed analysis of the performance of the proposed method on different types of tasks.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2507.10524.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, while the paper introduces the concept of expert-choice and token-choice routing, the explanation of the router's implementation could be more detailed.…

<a id="arxiv-2504.06225"></a>
### Encoder-Decoder Gemma: Improving the Quality-Efficiency Trade-Off via Adaptation

`arxiv:2504.06225` · LLMs: architectures, context, training · 2025-04-08

- final **-0.01** (conf 1.00, pct 34) · impact +0.10 · WATCH
- mean rating (1–10): **5.2** · accept votes **5/7** · percentile rank_avg 50.0 (100=best) · rank in year 57.0 (1=best)
- NAIPv2 `-0.588` · NAIP-v1 `0.592` · SciJudge `0.393` · DGC-BERT `0.919`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `5.0` Reject (S/P/C 2.67/3.0/2.67) · 14B Fast `6.8` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `5.0` Accept
- Telegram: [gonzo_ML/4218](https://t.me/gonzo_ML/4218), [gonzo_ML/4217](https://t.me/gonzo_ML/4217)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2504.06225.md#weaknesses): The paper lacks novelty. The idea of adapting a pretrained decoder-only LLM to an encoder-decoder LLM is not new. In fact, the authors mentioned the related work in Section 2, but they did not compare their work with the existing methods. For example, the authors did not compare their method with the method proposed in Wang et al. (2022). Wang et al.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2504.06225.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. First, the paper's evaluation is limited in scope, primarily focusing on the Gemma-2 family of models.…

<a id="arxiv-2502.09992"></a>
### Large Language Diffusion Models

`arxiv:2502.09992` · LLMs: architectures, context, training · 2025-02-14

- final **+0.50** (conf 1.00, pct 95) · impact +2.17 · KEEP
- mean rating (1–10): **6.7** · accept votes **6/7** · percentile rank_avg 80.7 (100=best) · rank in year 1.0 (1=best)
- NAIPv2 `0.659` · NAIP-v1 `0.700` · SciJudge `4.051` · DGC-BERT `0.892`
- CycleReviewer 8B `4.8` Reject · 70B `` 
- DeepReviewer 7B Std `8.0` Accept · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/3.0) · 14B Fast `7.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [data_secrets/6190](https://t.me/data_secrets/6190)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2502.09992.md#weaknesses): 1. The paper lacks novelty. The proposed method is very similar to MaskGIT. The only difference is the training data and the model size. The authors should compare their method with MaskGIT more comprehensively. 2. The paper lacks experimental results. The authors only provide results on a few datasets. It is hard to evaluate the performance of the proposed method. 3.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2502.09992.md#weaknesses): While I appreciate the novelty of the approach, several weaknesses in the paper warrant careful consideration. First, the paper's comparison of LLaDA with autoregressive models is not always conducted under strictly controlled conditions.…

<a id="arxiv-2501.14082"></a>
### Communicating Activations Between Language Model Agents

`arxiv:2501.14082` · LLMs: architectures, context, training · 2025-01-23

- final **+0.11** (conf 1.00, pct 53) · impact -0.46 · WATCH
- mean rating (1–10): **6.2** · accept votes **6/7** · percentile rank_avg 49.3 (100=best) · rank in year 58.0 (1=best)
- NAIPv2 `-2.201` · NAIP-v1 `0.405` · SciJudge `0.894` · DGC-BERT `0.102`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.2` Accept · 7B Fast `5.8` Accept (S/P/C 2.75/3.0/2.5) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/2.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2501.14082.md#weaknesses): The paper lacks an ablation study on the hyperparameters. For example, the choice of layer $j$ and $k$ seems to be crucial. However, the authors only provide a single choice for these hyperparameters. - The paper lacks a discussion of the limitations of the proposed method. For example, the paper does not discuss the limitations of the proposed method in terms of scalability and generalizability.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2501.14082.md#weaknesses): While the paper presents a compelling approach to inter-agent communication, several limitations warrant careful consideration. First, the paper's focus on two-agent communication is a significant constraint. The method, as described, is inherently pairwise, requiring a model to communicate with each other agent individually.…

<a id="arxiv-2501.00656"></a>
### 2 OLMo 2 Furious

`arxiv:2501.00656` · LLMs: architectures, context, training · 2024-12-31

- final **+0.23** (conf 1.00, pct 70) · impact +1.76 · KEEP
- mean rating (1–10): **6.0** · accept votes **5/7** · percentile rank_avg 58.1 (100=best) · rank in year 13.0 (1=best)
- NAIPv2 `-0.377` · NAIP-v1 `0.689` · SciJudge `3.821` · DGC-BERT `0.052`
- CycleReviewer 8B `3.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.0` Accept (S/P/C 2.75/2.75/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2501.00656.md#weaknesses): The paper does not provide a clear explanation of the model architecture, training data, and training recipe. The evaluation results are not compared to other models, making it difficult to assess the model's performance.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2501.00656.md#weaknesses): While the paper presents several strengths, there are also some notable weaknesses that warrant attention. One significant limitation is the lack of a dedicated section explicitly outlining the limitations of the proposed approach.…

<a id="arxiv-2412.13663"></a>
### Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference

`arxiv:2412.13663` · LLMs: architectures, context, training · 2024-12-18

- final **+0.28** (conf 1.00, pct 75) · impact +0.20 · KEEP
- mean rating (1–10): **6.0** · accept votes **5/7** · percentile rank_avg 53.8 (100=best) · rank in year 18.0 (1=best)
- NAIPv2 `-1.003` · NAIP-v1 `0.656` · SciJudge `-1.574` · DGC-BERT `0.731`
- CycleReviewer 8B `5.2` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/3.0) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/3091](https://t.me/gonzo_ML/3091), [dealerAI/1023](https://t.me/dealerAI/1023), [gonzo_ML/3090](https://t.me/gonzo_ML/3090)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2412.13663.md#weaknesses): The paper does not provide a detailed analysis of the performance of ModernBERT on specific tasks, such as long-context retrieval and code retrieval. - The paper does not provide a detailed analysis of the computational resources required to train and deploy ModernBERT.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2412.13663.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further consideration. Firstly, while the paper introduces several architectural modifications, it lacks a detailed analysis of the individual impact of each component.…

<a id="arxiv-2407.21783"></a>
### The Llama 3 Herd of Models

`arxiv:2407.21783` · LLMs: architectures, context, training · 2024-07-31

- final **+0.08** (conf 1.00, pct 48) · impact +2.37 · WATCH
- mean rating (1–10): **6.0** · accept votes **3/7** · percentile rank_avg 58.3 (100=best) · rank in year 11.0 (1=best)
- NAIPv2 `-2.232` · NAIP-v1 `0.744` · SciJudge `4.102` · DGC-BERT `0.445`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Reject · 7B Fast `6.8` Accept (S/P/C 3.0/3.0/2.75) · 14B Fast `4.0` Reject
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/4.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/3239](https://t.me/gonzo_ML/3239), [knowledge_accumulator/221](https://t.me/knowledge_accumulator/221), [ai_newz/3669](https://t.me/ai_newz/3669), [rybolos_channel/1386](https://t.me/rybolos_channel/1386), [MLResearch/1040](https://t.me/MLResearch/1040), [lovedeathtransformers/8609](https://t.me/lovedeathtransformers/8609), [j_links/7774](https://t.me/j_links/7774)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2407.21783.md#weaknesses): The paper does not provide a detailed description of the data used for pre-training and post-training, making it difficult to assess the quality and diversity of the data. The paper also does not provide a clear explanation of the methodology used for evaluating the performance of Llama 3, making it difficult to assess the validity of the results.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2407.21783.md#weaknesses): While the paper provides a detailed account of the development of Llama 3, several weaknesses limit its overall impact and suitability for a top-tier AI conference like ICLR. One significant concern is the lack of novel scientific contributions. The paper primarily focuses on the engineering aspects of scaling up LLMs, rather than presenting new research insights or theoretical advancements.…

<a id="arxiv-2405.12250"></a>
### Your Transformer is Secretly Linear

`arxiv:2405.12250` · LLMs: architectures, context, training · 2024-05-19

- final **-0.41** (conf 1.00, pct 8) · impact +0.06 · DROP
- mean rating (1–10): **4.9** · accept votes **3/7** · percentile rank_avg 35.4 (100=best) · rank in year 39.0 (1=best)
- NAIPv2 `-2.941` · NAIP-v1 `0.483` · SciJudge `1.763` · DGC-BERT `0.769`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `4.0` Reject (S/P/C 2.25/2.25/2.25) · 14B Fast `3.5` Reject
- OpenReviewer `5.0` Reject (S/P/C 3.0/2.0/3.0) · SEA-E `6.0` Accept
- Telegram: [abstractDL/281](https://t.me/abstractDL/281), [seeallochnaya/1531](https://t.me/seeallochnaya/1531), [lovedeathtransformers/7691](https://t.me/lovedeathtransformers/7691), [dendi_math_ai/24](https://t.me/dendi_math_ai/24)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2405.12250.md#weaknesses): The paper focuses on the linearity of transformer decoders, which is a relatively narrow topic. The paper could benefit from a more thorough discussion of related work on sparsity and pruning in transformers. The paper also could benefit from a more in-depth analysis of the limitations of the proposed method.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2405.12250.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. First, the paper lacks a clear and detailed explanation of the 'depth-pruning algorithm' mentioned in Section 5.…

<a id="arxiv-2405.04517"></a>
### xLSTM: Extended Long Short-Term Memory

`arxiv:2405.04517` · LLMs: architectures, context, training · 2024-05-07

- final **-0.33** (conf 0.95, pct 11) · impact +0.60 · WATCH
- mean rating (1–10): **4.5** · accept votes **2/7** · percentile rank_avg 35.3 (100=best) · rank in year 40.0 (1=best)
- NAIPv2 `-1.738` · NAIP-v1 `0.465` · SciJudge `3.495` · DGC-BERT `0.254`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `3.5` Reject (S/P/C 2.0/2.0/1.75) · 14B Fast `6.2` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `4.0` Reject
- Telegram: [data_secrets/4008](https://t.me/data_secrets/4008), [gonzo_ML/2626](https://t.me/gonzo_ML/2626), [axisofordinary/6294](https://t.me/axisofordinary/6294), [gonzo_ML/2624](https://t.me/gonzo_ML/2624), [lovedeathtransformers/8203](https://t.me/lovedeathtransformers/8203)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2405.04517.md#weaknesses): The paper presents a new LSTM architecture that is designed to address the limitations of the original LSTM model. The authors introduce two new components: a scalar memory and a matrix memory, and a new update rule based on covariance. The authors also introduce a new gating mechanism that is designed to improve the performance of the model.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2405.04517.md#weaknesses): of traditional LSTMs. The authors' approach to enhancing the memory capacity of LSTMs, particularly through the matrix memory in mLSTM, is a notable contribution. The fact that they have managed to scale LSTMs to billions of parameters, a feat previously thought to be challenging, is a significant achievement. Furthermore, the reported empirical results are impressive.…

<a id="arxiv-2404.09173"></a>
### TransformerFAM: Feedback attention is working memory

`arxiv:2404.09173` · LLMs: architectures, context, training · 2024-04-14

- final **-0.09** (conf 1.00, pct 26) · impact +0.33 · WATCH
- mean rating (1–10): **5.5** · accept votes **3/7** · percentile rank_avg 47.5 (100=best) · rank in year 25.0 (1=best)
- NAIPv2 `-2.414` · NAIP-v1 `0.595` · SciJudge `0.672` · DGC-BERT `0.948`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.8` Reject · 7B Fast `6.0` Reject (S/P/C 2.75/3.0/2.5) · 14B Fast `4.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/2586](https://t.me/gonzo_ML/2586), [gonzo_ML/2585](https://t.me/gonzo_ML/2585), [axisofordinary/6257](https://t.me/axisofordinary/6257)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2404.09173.md#weaknesses): 1. The experiments are not convincing. The authors only evaluate the proposed method on a few datasets, and the results are not significantly better than the baselines. The authors should conduct more experiments to demonstrate the effectiveness of the proposed method.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2404.09173.md#weaknesses): section, there are some limitations in the evaluation and analysis that need to be addressed to fully validate the claims made in the paper.

<a id="arxiv-2404.07143"></a>
### Leave No Context Behind: Efficient Infinite Context Transformers with Infini-attention

`arxiv:2404.07143` · LLMs: architectures, context, training · 2024-04-10

- final **-0.06** (conf 1.00, pct 30) · impact +0.47 · WATCH
- mean rating (1–10): **5.5** · accept votes **3/7** · percentile rank_avg 43.4 (100=best) · rank in year 28.0 (1=best)
- NAIPv2 `-2.006` · NAIP-v1 `0.497` · SciJudge `3.327` · DGC-BERT `0.878`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Reject · 7B Fast `5.8` Accept (S/P/C 2.5/2.5/2.75) · 14B Fast `5.5` Reject
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [lovedeathtransformers/7589](https://t.me/lovedeathtransformers/7589), [chillhousetech/690](https://t.me/chillhousetech/690), [gonzo_ML/2586](https://t.me/gonzo_ML/2586), [gonzo_ML/2585](https://t.me/gonzo_ML/2585), [axisofordinary/6247](https://t.me/axisofordinary/6247)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2404.07143.md#weaknesses): The proposed method is not as effective as the baseline methods on the long-context language modeling tasks. - The proposed method is not evaluated on the long-context tasks with 8B LLMs.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2404.07143.md#weaknesses): While the paper presents a compelling approach to long-context modeling, I have identified several weaknesses that warrant further consideration. Firstly, the paper lacks a thorough analysis of the computational overhead introduced by the memory read and write operations.…

<a id="arxiv-2312.04927"></a>
### Zoology: Measuring and Improving Recall in Efficient Language Models

`arxiv:2312.04927` · LLMs: architectures, context, training · 2023-12-08

- final **+0.60** (conf 1.00, pct 98) · impact -0.01 · KEEP
- mean rating (1–10): **6.7** · accept votes **5/7** · percentile rank_avg 67.6 (100=best) · rank in year 3.0 (1=best)
- NAIPv2 `2.451` · NAIP-v1 `0.635` · SciJudge `-0.367` · DGC-BERT `0.071`
- CycleReviewer 8B `6.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.5` Accept (S/P/C 3.0/3.25/3.0) · 14B Fast `7.0` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/2719](https://t.me/gonzo_ML/2719), [ntr_neural/218](https://t.me/ntr_neural/218), [tech_priestess/1363](https://t.me/tech_priestess/1363)
- Weaknesses:
  - [OR-8B](reviews/openreviewer-8b/arxiv_2312.04927.md#weaknesses): The paper does not provide any empirical results on the hybrid convolution-attention model on real-world language modeling tasks, such as WikiText103 or other standard language modeling benchmarks. It would be helpful to see how well the model performs on these tasks and how it compares to other state-of-the-art models.

<a id="arxiv-2311.06242"></a>
### Florence-2: Advancing a Unified Representation for a Variety of Vision Tasks

`arxiv:2311.06242` · LLMs: architectures, context, training · 2023-11-10

- final **+0.23** (conf 1.00, pct 68) · impact +0.10 · KEEP
- mean rating (1–10): **6.1** · accept votes **4/7** · percentile rank_avg 53.8 (100=best) · rank in year 19.0 (1=best)
- NAIPv2 `-1.918` · NAIP-v1 `0.479` · SciJudge `3.031` · DGC-BERT `0.049`
- CycleReviewer 8B `6.0` Reject · 70B `` 
- DeepReviewer 7B Std `8.0` Accept · 7B Fast `6.5` Accept (S/P/C 3.0/3.0/2.75) · 14B Fast `6.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [boris_again/3018](https://t.me/boris_again/3018), [AI_DeepLearning/1076](https://t.me/AI_DeepLearning/1076), [lovedeathtransformers/7855](https://t.me/lovedeathtransformers/7855), [axisofordinary/5811](https://t.me/axisofordinary/5811), [gonzo_ML/3270](https://t.me/gonzo_ML/3270), [lovedeathtransformers/9741](https://t.me/lovedeathtransformers/9741)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2311.06242.md#weaknesses): The paper does not provide a detailed analysis of the model's performance on specific tasks, such as object detection and image captioning. It would be helpful to include more quantitative results and analysis to demonstrate the model's performance on these tasks.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2311.06242.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. Firstly, while the paper introduces Florence-2 as a unified model, it lacks a detailed comparison with existing unified models, particularly those employing transformer-based architectures for multi-task learning.…

<a id="arxiv-2306.13575"></a>
### Scaling MLPs: A Tale of Inductive Bias

`arxiv:2306.13575` · LLMs: architectures, context, training · 2023-06-23

- final **+0.24** (conf 1.00, pct 71) · impact -0.07 · KEEP
- mean rating (1–10): **5.6** · accept votes **3/7** · percentile rank_avg 46.4 (100=best) · rank in year 30.0 (1=best)
- NAIPv2 `-1.609` · NAIP-v1 `0.617` · SciJudge `-0.341` · DGC-BERT `0.307`
- CycleReviewer 8B `4.0` Reject · 70B `` 
- DeepReviewer 7B Std `8.0` Accept · 7B Fast `6.0` Reject (S/P/C 2.67/3.0/2.33) · 14B Fast `6.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/1674](https://t.me/gonzo_ML/1674)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2306.13575.md#weaknesses): 1. The novelty of this paper is limited. The authors mainly study the performance of MLPs on vision tasks and show that they can achieve strong performance with sufficient scale. This is not surprising and has been shown in previous works such as (1). 2. The authors do not provide any theoretical analysis for the performance of MLPs. 3.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2306.13575.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. First, the paper's central claim regarding the role of inductive bias, while interesting, lacks sufficient nuance. The authors state that lack of inductive bias can be compensated by scale, and that MLPs are a good proxy for modern architectures.…

<a id="arxiv-2305.01625"></a>
### Unlimiformer: Long-Range Transformers with Unlimited Length Input

`arxiv:2305.01625` · LLMs: architectures, context, training · 2023-05-02

- final **+0.18** (conf 1.00, pct 62) · impact -0.26 · WATCH
- mean rating (1–10): **5.8** · accept votes **5/7** · percentile rank_avg 50.6 (100=best) · rank in year 26.0 (1=best)
- NAIPv2 `0.546` · NAIP-v1 `0.543` · SciJudge `-0.087` · DGC-BERT `0.843`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `5.8` Accept (S/P/C 2.75/2.5/2.5) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/1584](https://t.me/gonzo_ML/1584), [gonzo_ML/1507](https://t.me/gonzo_ML/1507), [axisofordinary/4895](https://t.me/axisofordinary/4895)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2305.01625.md#weaknesses): The method is only evaluated on summarization tasks. It is unclear how the method will perform on other tasks such as translation. - The method requires a kNN search over the encoder output, which can be slow. This may limit the applicability of the method to long inputs. - The method requires a large amount of memory to store the kNN index, which can be a limitation for very long inputs.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2305.01625.md#weaknesses): While I find the proposed Unlimiformer approach to be promising, my analysis has identified several weaknesses that warrant further consideration. Firstly, the paper lacks a detailed analysis of the method's robustness to variations in input data quality.…

<a id="arxiv-2302.14045"></a>
### Language Is Not All You Need: Aligning Perception with Language Models

`arxiv:2302.14045` · LLMs: architectures, context, training · 2023-02-27

- final **+0.26** (conf 1.00, pct 73) · impact +1.00 · KEEP
- mean rating (1–10): **6.2** · accept votes **6/7** · percentile rank_avg 67.2 (100=best) · rank in year 5.0 (1=best)
- NAIPv2 `-1.012` · NAIP-v1 `0.670` · SciJudge `3.295` · DGC-BERT `0.908`
- CycleReviewer 8B `6.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/2.67) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [techsparks/3925](https://t.me/techsparks/3925), [gonzo_ML/1339](https://t.me/gonzo_ML/1339), [axisofordinary/4500](https://t.me/axisofordinary/4500), [gonzo_ML/1364](https://t.me/gonzo_ML/1364), [gonzo_ML/2009](https://t.me/gonzo_ML/2009), [scitator_ai/79](https://t.me/scitator_ai/79), [nn_for_science/1346](https://t.me/nn_for_science/1346), [derplearning/2372](https://t.me/derplearning/2372)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2302.14045.md#weaknesses): 1. The paper does not provide a detailed analysis of the limitations of the proposed approach. 2. The paper does not provide a comparison with other state-of-the-art models on the same tasks. 3. The paper does not provide a discussion of the potential applications of the proposed approach.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2302.14045.md#weaknesses): Despite the promising results, several weaknesses in the paper's methodology and experimental design need to be addressed. First, the paper lacks a clear and detailed description of the image embedding process.…

<a id="arxiv-2302.10866"></a>
### Hyena Hierarchy: Towards Larger Convolutional Language Models

`arxiv:2302.10866` · LLMs: architectures, context, training · 2023-02-21

- final **+0.42** (conf 0.95, pct 90) · impact +1.20 · KEEP
- mean rating (1–10): **6.2** · accept votes **6/7** · percentile rank_avg 69.7 (100=best) · rank in year 2.0 (1=best)
- NAIPv2 `-0.003` · NAIP-v1 `0.679` · SciJudge `3.640` · DGC-BERT `0.908`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.5` Accept (S/P/C 3.0/3.25/2.5) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [dl_stories/824](https://t.me/dl_stories/824), [ntr_neural/218](https://t.me/ntr_neural/218), [gonzo_ML/1754](https://t.me/gonzo_ML/1754), [axisofordinary/4834](https://t.me/axisofordinary/4834)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2302.10866.md#weaknesses): The paper does not provide a thorough comparison with other attention-free models, such as RWKV and AFT. It would be helpful to include a comparison with these models in the main text. - The paper does not provide a thorough analysis of the computational complexity of Hyena. It would be helpful to include a more detailed analysis of the computational complexity in the main text.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2302.10866.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further consideration. First, while the paper demonstrates the effectiveness of Hyena on language modeling and image classification tasks, it lacks a thorough evaluation on tasks that require processing extremely long sequences, such as genomic sequence analysis.…

<a id="arxiv-2302.07253"></a>
### Energy Transformer

`arxiv:2302.07253` · LLMs: architectures, context, training · 2023-02-14

- final **-0.30** (conf 1.00, pct 13) · impact -0.76 · DROP
- mean rating (1–10): **5.6** · accept votes **4/7** · percentile rank_avg 34.4 (100=best) · rank in year 43.0 (1=best)
- NAIPv2 `-2.529` · NAIP-v1 `0.485` · SciJudge `-0.904` · DGC-BERT `0.732`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.2` Reject · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/2.5) · 14B Fast `6.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `5.0` Accept
- Telegram: [axisofordinary/4425](https://t.me/axisofordinary/4425)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2302.07253.md#weaknesses): The main weakness of this paper is that the proposed model is not well motivated. The authors claim that the proposed model is based on a sequence of attention layers that are designed to minimize a specifically engineered energy function. However, it is not clear why this is a good idea.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2302.07253.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. One of the most significant concerns is the lack of a thorough comparison with standard transformer architectures, particularly the BERT-style models.…

<a id="arxiv-2207.02098"></a>
### Neural Networks and the Chomsky Hierarchy

`arxiv:2207.02098` · LLMs: architectures, context, training · 2022-07-05

- final **+0.31** (conf 1.00, pct 79) · impact -1.29 · KEEP
- mean rating (1–10): **6.4** · accept votes **7/7** · percentile rank_avg 50.7 (100=best) · rank in year 10.0 (1=best)
- NAIPv2 `-1.336` · NAIP-v1 `0.379` · SciJudge `-1.578` · DGC-BERT `0.580`
- CycleReviewer 8B `5.8` Accept · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `5.8` Accept (S/P/C 2.75/3.0/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/4.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/1049](https://t.me/gonzo_ML/1049)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2207.02098.md#weaknesses): The paper does not provide any theoretical analysis of the generalization of neural networks, and the authors only provide empirical results.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2207.02098.md#weaknesses): While this paper presents a compelling empirical study, several limitations warrant careful consideration. One significant weakness is the lack of a dedicated section explicitly outlining the paper's contributions and their implications. While the introduction and conclusion touch upon these aspects, a more focused discussion would greatly enhance the paper's impact and accessibility.…

<a id="arxiv-2203.08913"></a>
### Memorizing Transformers

`arxiv:2203.08913` · LLMs: architectures, context, training · 2022-03-16

- final **+0.25** (conf 1.00, pct 73) · impact +0.36 · KEEP
- mean rating (1–10): **6.3** · accept votes **5/7** · percentile rank_avg 60.3 (100=best) · rank in year 5.0 (1=best)
- NAIPv2 `-1.776` · NAIP-v1 `0.668` · SciJudge `1.048` · DGC-BERT `0.663`
- CycleReviewer 8B `6.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `6.2` Accept (S/P/C 3.25/3.25/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [abstractDL/198](https://t.me/abstractDL/198), [dl_stories/704](https://t.me/dl_stories/704), [j_links/6549](https://t.me/j_links/6549), [axisofordinary/4642](https://t.me/axisofordinary/4642), [gonzo_ML/1507](https://t.me/gonzo_ML/1507), [lovedeathtransformers/5700](https://t.me/lovedeathtransformers/5700), [dlinnlp/1565](https://t.me/dlinnlp/1565)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2203.08913.md#weaknesses): The paper does not provide a thorough analysis of the proposed method. For example, the authors do not provide an ablation study on the effect of the memory size, the number of heads, or the number of layers. The authors also do not provide a comparison with other long-range attention methods. - The paper does not provide a detailed explanation of the experimental setup.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2203.08913.md#weaknesses): While I find the proposed method to be promising, several limitations warrant further discussion. Firstly, the paper lacks a thorough analysis of the computational overhead introduced by the k-NN search. While the authors mention step time increases with memory size, a more detailed breakdown of the time spent on k-NN search versus other operations is missing.…

<a id="arxiv-2006.16236"></a>
### Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention

`arxiv:2006.16236` · LLMs: architectures, context, training · 2020-06-29

- final **+0.13** (conf 1.00, pct 57) · impact +0.51 · WATCH
- mean rating (1–10): **5.8** · accept votes **5/7** · percentile rank_avg 51.1 (100=best) · rank in year 7.0 (1=best)
- NAIPv2 `-1.190` · NAIP-v1 `0.669` · SciJudge `1.961` · DGC-BERT `0.564`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.2` Reject · 7B Fast `5.0` Reject (S/P/C 2.5/2.75/2.5) · 14B Fast `6.2` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/2718](https://t.me/gonzo_ML/2718), [dlinnlp/1312](https://t.me/dlinnlp/1312), [gonzo_ML/397](https://t.me/gonzo_ML/397), [gonzo_ML/1754](https://t.me/gonzo_ML/1754), [dlinnlp/1645](https://t.me/dlinnlp/1645)
- Weaknesses:
  - [OR-8B](reviews/openreviewer-8b/arxiv_2006.16236.md#weaknesses): 1. The idea of linear attention is not new. It has been explored in previous works such as (1, 2, 3). The authors should discuss these works in the paper. 2. The proposed method is not as good as the baselines on some tasks.…

<a id="arxiv-2002.05202"></a>
### GLU Variants Improve Transformer

`arxiv:2002.05202` · LLMs: architectures, context, training · 2020-02-12

- final **-0.58** (conf 1.00, pct 4) · impact -1.06 · DROP
- mean rating (1–10): **3.5** · accept votes **1/7** · percentile rank_avg 16.9 (100=best) · rank in year 12.0 (1=best)
- NAIPv2 `-2.363` · NAIP-v1 `0.392` · SciJudge `-1.128` · DGC-BERT `0.806`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `3.0` Reject · 7B Fast `2.3` Reject (S/P/C 1.67/1.67/1.67) · 14B Fast `4.0` Reject
- OpenReviewer `3.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `5.0` Reject
- Telegram: [gonzo_ML/4099](https://t.me/gonzo_ML/4099), [dealerAI/1023](https://t.me/dealerAI/1023), [mishin_learning/816](https://t.me/mishin_learning/816), [gonzo_ML/3592](https://t.me/gonzo_ML/3592), [gonzo_ML/2500](https://t.me/gonzo_ML/2500), [gonzo_ML/4071](https://t.me/gonzo_ML/4071), [seeallochnaya/1165](https://t.me/seeallochnaya/1165)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2002.05202.md#weaknesses): 1. The main concern is the novelty of the proposed method. The GLU unit has been proposed in 2016, and it has been widely used in many NLP tasks. The proposed method is simply replacing the FFN with GLU and its variants. The novelty of the proposed method is limited.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2002.05202.md#weaknesses): While this paper presents a valuable exploration of GLU variants in Transformers, several weaknesses limit the impact and generalizability of its findings. A primary concern is the lack of a strong theoretical justification for the observed performance improvements.…

<a id="arxiv-1710.05941"></a>
### Searching for Activation Functions

`arxiv:1710.05941` · LLMs: architectures, context, training · 2017-10-16

- final **+0.13** (conf 1.00, pct 56) · impact +0.94 · WATCH
- mean rating (1–10): **5.7** · accept votes **4/7** · percentile rank_avg 46.6 (100=best) · rank in year 4.0 (1=best)
- NAIPv2 `-1.962` · NAIP-v1 `0.734` · SciJudge `1.835` · DGC-BERT `0.614`
- CycleReviewer 8B `5.8` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `6.0` Accept (S/P/C 3.0/3.25/2.75) · 14B Fast `5.8` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/2.0/2.0) · SEA-E `6.0` Accept
- Telegram: [j_links/542](https://t.me/j_links/542), [gonzo_ML/364](https://t.me/gonzo_ML/364)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_1710.05941.md#weaknesses): The novelty of the paper is limited. The search space is very similar to the one proposed in Bello et al. (2017). The search method is also similar to the one used in Zoph & Le (2016). - The experiments are not convincing. The authors only compare their method with a few baselines. The proposed activation function is only evaluated on a few datasets.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_1710.05941.md#weaknesses): While the paper presents a compelling case for the Swish activation function, there are several weaknesses that warrant further discussion. One significant limitation is the lack of a comprehensive theoretical analysis of why Swish outperforms ReLU.…

<a id="doi-10.1073-pnas.2520095123"></a>
### Evidence from formal logical reasoning reveals that the language of thought is not natural language

`doi:10.1073/pnas.2520095123` · Reasoning and the "physics" of language models · 2026-07-06

- final **-0.08** (conf 0.91, pct 28) · impact -1.14 · WATCH · partial fulltext
- mean rating (1–10): **5.7** · accept votes **5/7** · percentile rank_avg 41.4 (100=best) · rank in year 62.0 (1=best)
- NAIPv2 `-1.912` · NAIP-v1 `0.588` · SciJudge `-7.362` · DGC-BERT `0.105`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `5.5` Accept (S/P/C 2.75/2.75/2.75) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/doi_10.1073_pnas.2520095123.md#weaknesses): 1. The paper does not provide a clear hypothesis or research question. The abstract suggests that the paper aims to investigate the relationship between logical reasoning and language, but the specific research question or hypothesis is not stated. This makes it difficult to understand the purpose of the study and evaluate the results in the context of the research question.
  - [DR-14B Fast](reviews/deepreviewer-14b/doi_10.1073_pnas.2520095123.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. The most significant limitation, in my view, is the small sample size of the aphasia group. The study relies on the performance of only two individuals with profound aphasia to draw conclusions about the dissociation between language and reasoning.…

<a id="arxiv-2606.31779"></a>
### Bridging the Gap Between Latent and Explicit Reasoning with Looped Transformers

`arxiv:2606.31779` · Reasoning and the "physics" of language models · 2026-06-30

- final **+0.29** (conf 1.00, pct 76) · impact +0.98 · KEEP
- mean rating (1–10): **6.0** · accept votes **5/7** · percentile rank_avg 64.6 (100=best) · rank in year 22.0 (1=best)
- NAIPv2 `2.404` · NAIP-v1 `0.771` · SciJudge `0.777` · DGC-BERT `0.735`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.5` Accept (S/P/C 3.0/3.0/2.5) · 14B Fast `6.2` Reject
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/5761](https://t.me/gonzo_ML/5761)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2606.31779.md#weaknesses): 1. The proposed method is only evaluated on math reasoning tasks. It would be interesting to see how it performs on other tasks, such as language translation or question answering. 2. The proposed method is only compared to one previous method. It would be interesting to see how it compares to other methods.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2606.31779.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, the method's reliance on gold-CoT for training is a significant limitation. As the authors themselves acknowledge, the training objective directly aligns the latent representations with the gold-CoT tokens.…

<a id="arxiv-2606.25010"></a>
### Emergent Capabilities Arise Randomly from Learning Sparse Attention Patterns

`arxiv:2606.25010` · Reasoning and the "physics" of language models · 2026-06-23

- final **+0.03** (conf 1.00, pct 40) · impact -0.95 · WATCH
- mean rating (1–10): **6.0** · accept votes **4/7** · percentile rank_avg 53.6 (100=best) · rank in year 46.0 (1=best)
- NAIPv2 `-0.768` · NAIP-v1 `0.409` · SciJudge `-0.594` · DGC-BERT `0.879`
- CycleReviewer 8B `5.2` Reject · 70B `` 
- DeepReviewer 7B Std `6.2` Reject · 7B Fast `7.0` Accept (S/P/C 2.75/3.0/3.0) · 14B Fast `6.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/5867](https://t.me/gonzo_ML/5867)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2606.25010.md#weaknesses): The paper does not seem to have any significant contributions. The authors show that the emergence of capabilities is driven by the learning of task-relevant attention patterns. This is not a new finding. The authors also show that the difficulty of learning attention patterns depends on context length and pattern sparsity. This is also not a new finding.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2606.25010.md#weaknesses): Despite its strengths, this paper has several weaknesses that warrant careful consideration. One significant limitation is the lack of a precise definition of 'emergent capabilities' within the context of this study. While the paper describes how emergence is measured operationally, it does not provide a formal definition of the term itself.…

<a id="arxiv-2606.03982"></a>
### Language Models Compare Quantities Using Number-specific and Unit-specific Heuristics

`arxiv:2606.03982` · Reasoning and the "physics" of language models · 2026-06-02

- final **-0.01** (conf 1.00, pct 35) · impact -1.40 · WATCH
- mean rating (1–10): **6.0** · accept votes **4/7** · percentile rank_avg 45.3 (100=best) · rank in year 59.0 (1=best)
- NAIPv2 `-0.947` · NAIP-v1 `0.431` · SciJudge `-3.712` · DGC-BERT `0.120`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/2.5) · 14B Fast `6.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2606.03982.md#weaknesses): 1. The paper lacks novelty. The authors have conducted a thorough analysis of language models' behavior in comparing quantities with measurement units. However, the results are not surprising, and the conclusions drawn from the analysis are not particularly novel or groundbreaking.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2606.03982.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further consideration. First, while the paper provides a detailed description of the Quantity Margin calculation in Section 2.1, including the formula and an example, the initial presentation of this concept could be improved.…

<a id="arxiv-2605.07654"></a>
### Reliable Chain-of-Thought via Prefix Consistency

`arxiv:2605.07654` · Reasoning and the "physics" of language models · 2026-05-08

- final **+0.24** (conf 1.00, pct 72) · impact +0.95 · KEEP
- mean rating (1–10): **6.2** · accept votes **6/7** · percentile rank_avg 65.5 (100=best) · rank in year 18.0 (1=best)
- NAIPv2 `0.827` · NAIP-v1 `0.720` · SciJudge `1.499` · DGC-BERT `0.774`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.8` Accept · 7B Fast `7.0` Accept (S/P/C 3.25/3.25/3.0) · 14B Fast `6.8` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2605.07654.md#weaknesses): 1. The paper lacks sufficient analysis of the proposed method. For example, the paper does not provide any theoretical analysis of the proposed method. The authors only show that the reproduction rate is higher for correct answers than for incorrect answers. However, it is not clear why this is the case or how it leads to the proposed method.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2605.07654.md#weaknesses): Despite the paper's strengths, several limitations and areas for improvement have been identified. First, the evaluation is limited to a few reasoning benchmarks, specifically FrontierScience-Olympiad, HMMT Feb 2026, AIME 2025, and Brumo 2025.…

<a id="arxiv-2604.11791"></a>
### A Mechanistic Analysis of Looped Reasoning Language Models

`arxiv:2604.11791` · Reasoning and the "physics" of language models · 2026-04-13

- final **-0.16** (conf 1.00, pct 22) · impact -1.42 · WATCH
- mean rating (1–10): **6.2** · accept votes **3/7** · percentile rank_avg 45.9 (100=best) · rank in year 58.0 (1=best)
- NAIPv2 `-0.953` · NAIP-v1 `0.346` · SciJudge `-2.454` · DGC-BERT `0.489`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `5.8` Reject (S/P/C 2.75/2.75/2.5) · 14B Fast `6.5` Reject
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/5206](https://t.me/gonzo_ML/5206)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2604.11791.md#weaknesses): The main weakness of the paper is that it is unclear what the contribution of the paper is. The paper studies the behavior of looped LLMs, but it is not clear what this behavior tells us about how to design better looped LLMs. The authors do not provide any practical guidance on how to design better looped LLMs based on their results.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2604.11791.md#weaknesses): Despite the strengths, I have identified several weaknesses that warrant attention. First, the paper lacks a comprehensive explanation for the observed behavior of looped Transformers. While the authors demonstrate that looped models exhibit cyclic behavior and mirroring of feedforward stages of inference, the underlying reasons for these phenomena are not fully explored.…

<a id="arxiv-2604.01754"></a>
### LiveMathematicianBench: A Live Benchmark for Mathematician-Level Reasoning with Proof Sketches

`arxiv:2604.01754` · Reasoning and the "physics" of language models · 2026-04-02

- final **+0.04** (conf 1.00, pct 42) · impact +1.86 · WATCH
- mean rating (1–10): **6.8** · accept votes **4/7** · percentile rank_avg 70.6 (100=best) · rank in year 8.0 (1=best)
- NAIPv2 `-0.744` · NAIP-v1 `0.756` · SciJudge `3.339` · DGC-BERT `0.424`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.0` Reject (S/P/C 3.0/2.5/2.5) · 14B Fast `5.8` Reject
- OpenReviewer `8.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `8.0` Accept
- Telegram: —
- Weaknesses:
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2604.01754.md#weaknesses): While I appreciate the contributions of this paper, I have identified several weaknesses that warrant attention. First, the paper's reliance on multiple language models throughout the benchmark construction pipeline raises concerns about potential biases and error propagation.…
  - [DR-7B Fast](reviews/deepreviewer-7b-fast/arxiv_2604.01754.md#weaknesses): Despite its strengths, I have identified several weaknesses in this paper that warrant careful consideration. First, while the authors claim novelty in their approach, the paper lacks a clear and detailed comparison to existing benchmarks, particularly those that also utilize arXiv-derived content.…

<a id="arxiv-2602.10416"></a>
### AI-rithmetic

`arxiv:2602.10416` · Reasoning and the "physics" of language models · 2026-02-11

- final **-0.41** (conf 1.00, pct 9) · impact -0.07 · DROP
- mean rating (1–10): **5.5** · accept votes **2/7** · percentile rank_avg 34.5 (100=best) · rank in year 69.0 (1=best)
- NAIPv2 `-1.744` · NAIP-v1 `0.367` · SciJudge `2.983` · DGC-BERT `0.162`
- CycleReviewer 8B `5.8` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `5.2` Accept (S/P/C 2.75/3.0/2.5) · 14B Fast `5.8` Reject
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2602.10416.md#weaknesses): The paper does not provide a clear explanation of why the error rate is periodic with respect to the length of the numbers being added. - The paper does not provide a clear explanation of why the error rate is higher for numbers whose length is not a multiple of 3. - The paper does not provide a clear explanation of why the error rate is higher for numbers whose length is not a multiple of 3.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2602.10416.md#weaknesses): While this paper presents valuable insights into the arithmetic limitations of LLMs, several weaknesses warrant careful consideration. A primary concern is the paper's lack of a detailed explanation of the error categorization process, particularly for misalignment errors.…

<a id="openreview-klU4737opt"></a>
### Position: LLMs can't jump

`openreview:klU4737opt` · Reasoning and the "physics" of language models · unknown

- final **-0.25** (conf 1.00, pct 18) · impact -1.35 · DROP
- mean rating (1–10): **5.5** · accept votes **2/7** · percentile rank_avg 27.7 (100=best) · rank in year 9.0 (1=best)
- NAIPv2 `-3.801` · NAIP-v1 `0.327` · SciJudge `-1.683` · DGC-BERT `0.040`
- CycleReviewer 8B `6.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.2` Reject · 7B Fast `5.0` Reject (S/P/C 2.5/2.25/2.5) · 14B Fast `4.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/openreview_klU4737opt.md#weaknesses): The paper does not provide a clear definition of what is meant by "abductive leap" or how it differs from inductive and deductive reasoning. - The paper does not provide a clear explanation of how physically consistent, multimodal world models could enable AI systems to make abductive leaps.…
  - [DR-14B Fast](reviews/deepreviewer-14b/openreview_klU4737opt.md#weaknesses): While the paper presents a compelling argument, several weaknesses undermine its overall impact. A primary concern is the lack of empirical evidence to support the claim that LLMs are fundamentally incapable of abductive reasoning.…

<a id="arxiv-2512.16902"></a>
### In-Context Algebra

`arxiv:2512.16902` · Reasoning and the "physics" of language models · 2025-12-18

- final **+0.34** (conf 1.00, pct 82) · impact -0.77 · KEEP
- mean rating (1–10): **6.8** · accept votes **7/7** · percentile rank_avg 68.0 (100=best) · rank in year 11.0 (1=best)
- NAIPv2 `-0.869` · NAIP-v1 `0.504` · SciJudge `-2.892` · DGC-BERT `0.931`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.8` Accept · 7B Fast `6.2` Accept (S/P/C 3.0/2.75/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/4.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2512.16902.md#weaknesses): The paper does not provide a comprehensive review of the existing literature on in-context learning and its applications. The authors should provide a more detailed discussion of the current state of the field and how their work contributes to it. - The paper does not provide a clear explanation of the limitations of the proposed approach.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2512.16902.md#weaknesses): While the paper presents compelling results, I have identified several weaknesses that warrant further consideration. First, the paper's presentation of the task description, particularly the token mapping process, is difficult to follow. The description of how variable tokens are mapped to elements of different groups across sequences, as described in Section 2, is dense and hard to parse.…

<a id="arxiv-2510.00184"></a>
### Why Can't Transformers Learn Multiplication? Reverse-Engineering Reveals Long-Range Dependency Pitfalls

`arxiv:2510.00184` · Reasoning and the "physics" of language models · 2025-09-30

- final **+0.06** (conf 1.00, pct 46) · impact +0.45 · WATCH
- mean rating (1–10): **6.3** · accept votes **6/7** · percentile rank_avg 59.8 (100=best) · rank in year 36.0 (1=best)
- NAIPv2 `-1.400` · NAIP-v1 `0.696` · SciJudge `-0.466` · DGC-BERT `0.774`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `6.8` Accept (S/P/C 3.0/3.0/2.5) · 14B Fast `6.7` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/7757](https://t.me/axisofordinary/7757)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2510.00184.md#weaknesses): The paper only studies a simple 2-layer model. It would be interesting to see how the findings generalize to larger models. - The paper only considers a single task. It would be interesting to see how the findings generalize to other tasks that require long-range dependencies.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2510.00184.md#weaknesses): While this paper offers valuable insights, several limitations warrant careful consideration. First, the paper's primary focus on a 4x4 multiplication task, while providing a controlled environment for analysis, raises concerns about the generalizability of the findings.…

<a id="arxiv-2509.25239"></a>
### A Formal Comparison Between Chain of Thought and Latent Thought

`arxiv:2509.25239` · Reasoning and the "physics" of language models · 2025-09-25

- final **+0.12** (conf 1.00, pct 55) · impact -1.08 · WATCH
- mean rating (1–10): **6.0** · accept votes **5/7** · percentile rank_avg 48.7 (100=best) · rank in year 59.0 (1=best)
- NAIPv2 `-2.500` · NAIP-v1 `0.488` · SciJudge `-3.698` · DGC-BERT `0.853`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.0` Reject (S/P/C 3.0/3.0/3.0) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2509.25239.md#weaknesses): 1. The paper focuses on theoretical analysis and lacks empirical validation of the theoretical results. The experimental results are limited to a few simple tasks and do not demonstrate the practical applicability of the theoretical findings. 2. The paper does not discuss the limitations of the theoretical analysis, such as the assumptions made and the potential biases introduced. 3.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2509.25239.md#weaknesses): of these approaches by analyzing their computational power through the lens of circuit complexity. They introduce a formal framework, defining CoT as a sequential computation model akin to Turing machines, while Latent Thought, encompassing methods like Coconut and Looped Transformers, is treated as a parallel computation model similar to Boolean circuits.…

<a id="arxiv-2509.20317"></a>
### SIM-CoT: Supervised Implicit Chain-of-Thought

`arxiv:2509.20317` · Reasoning and the "physics" of language models · 2025-09-24

- final **+0.23** (conf 1.00, pct 69) · impact +0.75 · KEEP
- mean rating (1–10): **6.5** · accept votes **6/7** · percentile rank_avg 71.0 (100=best) · rank in year 8.0 (1=best)
- NAIPv2 `1.872` · NAIP-v1 `0.683` · SciJudge `0.797` · DGC-BERT `0.939`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `3.8` Reject · 7B Fast `6.3` Accept (S/P/C 3.0/3.0/2.67) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [abstractDL/348](https://t.me/abstractDL/348), [boris_again/3470](https://t.me/boris_again/3470)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2509.20317.md#weaknesses): 1. The paper only evaluates the method on a single dataset, GSM8k-Aug, which is a relatively small dataset. It would be good to see the performance of SIM-CoT on other datasets, such as GSM-Hard, MultiArith, and SVAMP. 2. The paper does not provide a detailed analysis of the computational cost of SIM-CoT.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2509.20317.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, while the paper introduces step-level supervision as a solution to latent instability, it does not fully explore the impact of varying step lengths on the model's performance.…

<a id="arxiv-2508.02513"></a>
### Modular Arithmetic: Language Models Solve Math Digit by Digit

`arxiv:2508.02513` · Reasoning and the "physics" of language models · 2025-08-04

- final **+0.09** (conf 1.00, pct 50) · impact +0.29 · WATCH
- mean rating (1–10): **6.2** · accept votes **6/7** · percentile rank_avg 61.8 (100=best) · rank in year 25.0 (1=best)
- NAIPv2 `-0.951` · NAIP-v1 `0.661` · SciJudge `-0.407` · DGC-BERT `0.733`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.2` Accept · 7B Fast `5.8` Reject (S/P/C 2.75/2.5/2.5) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2508.02513.md#weaknesses): 1. The authors only consider addition and subtraction in their experiments. It would be interesting to see if the proposed approach can be extended to more complex arithmetic operations such as multiplication and division. 2. The authors only consider MLP layers in their analysis. It would be interesting to see if the proposed approach can be extended to other components such as attention heads.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2508.02513.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. First, the scope of the paper is limited to addition and subtraction, and the experiments are primarily conducted on three- digit numbers.…

<a id="arxiv-2506.10947"></a>
### Spurious Rewards: Rethinking Training Signals in RLVR

`arxiv:2506.10947` · Reasoning and the "physics" of language models · 2025-06-12

- final **+0.39** (conf 0.91, pct 87) · impact -0.96 · KEEP · salvage dr7bf
- mean rating (1–10): **7.1** · accept votes **6/6** · percentile rank_avg 70.8 (100=best) · rank in year 9.0 (1=best)
- NAIPv2 `-0.237` · NAIP-v1 `0.326` · SciJudge `0.486` · DGC-BERT `0.888`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.2` Accept · 7B Fast ``  (S/P/C 3.0/3.0/3.0) · 14B Fast `7.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [buckwheat_thoughts/306](https://t.me/buckwheat_thoughts/306), [gonzo_ML/4702](https://t.me/gonzo_ML/4702)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2506.10947.md#weaknesses): The paper does not provide a clear explanation for why spurious rewards can lead to improvements in performance. The authors hypothesize that it is due to the clipping bias in GRPO, but this is not clearly explained. It would be helpful if the authors could provide a more detailed explanation of this phenomenon. - The paper only considers a single type of spurious reward, which is random rewards.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2506.10947.md#weaknesses): While this paper presents compelling findings, several limitations warrant careful consideration. First, the paper's reliance on the GRPO algorithm, while justified by its popularity in RLVR research, limits the generalizability of the findings.…

<a id="arxiv-2505.21493"></a>
### Reinforcing General Reasoning without Verifiers

`arxiv:2505.21493` · Reasoning and the "physics" of language models · 2025-05-27

- final **+0.50** (conf 1.00, pct 96) · impact +0.42 · KEEP
- mean rating (1–10): **6.6** · accept votes **6/7** · percentile rank_avg 72.9 (100=best) · rank in year 6.0 (1=best)
- NAIPv2 `0.858` · NAIP-v1 `0.455` · SciJudge `3.357` · DGC-BERT `0.812`
- CycleReviewer 8B `5.2` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `7.0` Accept (S/P/C 3.25/3.0/3.0) · 14B Fast `6.8` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `8.0` Accept
- Telegram: [buckwheat_thoughts/306](https://t.me/buckwheat_thoughts/306), [gonzo_ML/4702](https://t.me/gonzo_ML/4702)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2505.21493.md#weaknesses): The proposed method relies on the assumption that there is a single correct answer for each question. However, this assumption may not hold for many general reasoning tasks, such as open-ended questions or questions with multiple correct answers. The paper does not discuss this limitation. - The proposed method is not novel.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2505.21493.md#weaknesses): While the paper presents a compelling approach, several weaknesses warrant careful consideration. First, the paper's scope is primarily focused on multiple-choice question answering, which limits the generalizability of its findings.…

<a id="arxiv-2505.21444"></a>
### Can Large Reasoning Models Self-Train?

`arxiv:2505.21444` · Reasoning and the "physics" of language models · 2025-05-27

- final **-0.12** (conf 1.00, pct 23) · impact -0.88 · WATCH
- mean rating (1–10): **6.0** · accept votes **2/7** · percentile rank_avg 42.0 (100=best) · rank in year 67.0 (1=best)
- NAIPv2 `-1.297` · NAIP-v1 `0.361` · SciJudge `0.324` · DGC-BERT `0.480`
- CycleReviewer 8B `5.5` Reject · 70B `` 
- DeepReviewer 7B Std `5.2` Reject · 7B Fast `5.5` Reject (S/P/C 2.75/3.0/2.5) · 14B Fast `5.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [buckwheat_thoughts/306](https://t.me/buckwheat_thoughts/306), [gonzo_ML/4702](https://t.me/gonzo_ML/4702)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2505.21444.md#weaknesses): 1. The paper is a bit incremental, as it is a simple extension of the previous work. The authors should discuss more about the difference between the previous work and the current work.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2505.21444.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. First, while the paper introduces SRT as a novel approach, the novelty is somewhat overstated.…

<a id="arxiv-2505.15134"></a>
### The Unreasonable Effectiveness of Entropy Minimization in LLM Reasoning

`arxiv:2505.15134` · Reasoning and the "physics" of language models · 2025-05-21

- final **+0.23** (conf 1.00, pct 69) · impact +2.06 · KEEP
- mean rating (1–10): **6.3** · accept votes **6/7** · percentile rank_avg 68.2 (100=best) · rank in year 10.0 (1=best)
- NAIPv2 `-0.945` · NAIP-v1 `0.718` · SciJudge `3.930` · DGC-BERT `0.750`
- CycleReviewer 8B `4.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.2` Accept · 7B Fast `6.5` Accept (S/P/C 3.25/3.25/2.75) · 14B Fast `7.0` Accept
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/3.0) · SEA-E `6.0` Accept
- Telegram: [buckwheat_thoughts/306](https://t.me/buckwheat_thoughts/306), [gonzo_ML/4702](https://t.me/gonzo_ML/4702)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2505.15134.md#weaknesses): 1. The paper lacks novelty. The proposed methods are simple and have been explored in previous works. The main difference is that this paper applies these methods to LLMs. 2. The paper lacks ablation studies. The authors only show the results of the proposed methods without showing the results of the individual components. 3. The paper lacks comparison with other methods.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2505.15134.md#weaknesses): While I find the paper to be generally strong, there are several weaknesses that I have identified through my analysis. First, the paper's reliance on the assumption that high model confidence correlates with correctness is a significant limitation.…

<a id="arxiv-2505.13763"></a>
### Language Models Are Capable of Metacognitive Monitoring and Control of Their Internal Activations

`arxiv:2505.13763` · Reasoning and the "physics" of language models · 2025-05-19

- final **-0.09** (conf 1.00, pct 26) · impact +0.03 · WATCH
- mean rating (1–10): **6.5** · accept votes **4/7** · percentile rank_avg 50.5 (100=best) · rank in year 55.0 (1=best)
- NAIPv2 `-1.741` · NAIP-v1 `0.559` · SciJudge `0.416` · DGC-BERT `0.055`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `4.8` Reject · 7B Fast `6.2` Reject (S/P/C 2.5/3.0/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/4.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/7240](https://t.me/axisofordinary/7240)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2505.13763.md#weaknesses): 1. The paper lacks a discussion of the limitations of the proposed neurofeedback paradigm. For example, how do the authors ensure that the LLMs are not just memorizing the relationship between the input and the label, rather than actually understanding the underlying concept?…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2505.13763.md#weaknesses): While I find the paper's approach innovative, several weaknesses need to be addressed. Firstly, the paper's claim of novelty, while partially valid, could be more nuanced. The authors state that their paradigm differs from prior methods by quantifying metacognition at the neural level, contrasting it with probing and standard ICL.…

<a id="arxiv-2504.20571"></a>
### Reinforcement Learning for Reasoning in Large Language Models with One Training Example

`arxiv:2504.20571` · Reasoning and the "physics" of language models · 2025-04-29

- final **+0.21** (conf 1.00, pct 66) · impact +0.77 · KEEP
- mean rating (1–10): **5.9** · accept votes **4/7** · percentile rank_avg 57.9 (100=best) · rank in year 40.0 (1=best)
- NAIPv2 `1.729` · NAIP-v1 `0.521` · SciJudge `3.472` · DGC-BERT `0.725`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [data_secrets/6880](https://t.me/data_secrets/6880), [axisofordinary/7262](https://t.me/axisofordinary/7262), [tech_priestess/2091](https://t.me/tech_priestess/2091), [buckwheat_thoughts/306](https://t.me/buckwheat_thoughts/306), [axisofordinary/7159](https://t.me/axisofordinary/7159), [boris_again/3219](https://t.me/boris_again/3219), [gonzo_ML/4702](https://t.me/gonzo_ML/4702)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2504.20571.md#weaknesses): 1. The paper only investigates the effectiveness of RLVR with a single training example on a base model Qwen2.5-Math-1.5B. It would be interesting to see if the results hold for other base models and RL algorithms.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2504.20571.md#weaknesses): While this paper presents a compelling and novel approach to RLVR, several weaknesses warrant careful consideration. First, the paper's claim that one-shot RLVR works across different base models is not fully supported by the experimental results. While the authors demonstrate improvements on Llama-3.2-3B-Instruct, the gains are substantially smaller compared to those observed on the Qwen models.…

<a id="arxiv-2503.21676"></a>
### How do language models learn facts? Dynamics, curricula and hallucinations

`arxiv:2503.21676` · Reasoning and the "physics" of language models · 2025-03-27

- final **+0.30** (conf 1.00, pct 78) · impact -0.15 · KEEP
- mean rating (1–10): **6.5** · accept votes **6/7** · percentile rank_avg 62.0 (100=best) · rank in year 24.0 (1=best)
- NAIPv2 `-0.619` · NAIP-v1 `0.448` · SciJudge `1.357` · DGC-BERT `0.792`
- CycleReviewer 8B `4.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `7.0` Accept (S/P/C 3.0/3.25/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/4.0) · SEA-E `7.0` Accept
- Telegram: [data_secrets/6564](https://t.me/data_secrets/6564)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2503.21676.md#weaknesses): 1. The authors claim that their findings are generalizable to LLMs, but the experiments are conducted on small models (44M parameters). The authors should conduct experiments on larger models to support their claims. 2. The authors claim that their findings are generalizable to real-world data, but the experiments are conducted on synthetic data.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2503.21676.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. First, the paper's reliance on a synthetic dataset, while providing control, raises concerns about the generalizability of the findings to real-world language models trained on diverse, natural data.…

<a id="arxiv-2502.19981"></a>
### The Lookahead Limitation: Why Multi-Operand Addition is Hard for LLMs

`arxiv:2502.19981` · Reasoning and the "physics" of language models · 2025-02-27

- final **-0.16** (conf 1.00, pct 22) · impact +0.68 · WATCH
- mean rating (1–10): **5.8** · accept votes **3/7** · percentile rank_avg 53.2 (100=best) · rank in year 47.0 (1=best)
- NAIPv2 `-2.475` · NAIP-v1 `0.728` · SciJudge `-0.141` · DGC-BERT `0.449`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `8.0` Accept · 7B Fast `6.0` Reject (S/P/C 2.5/2.75/2.5) · 14B Fast `4.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2502.19981.md#weaknesses): The proposed hypothesis is somewhat trivial. The authors show that LLMs use a one-digit lookahead heuristic to solve addition, which is not surprising. This paper does not provide any new insights into the limitations of LLMs.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2502.19981.md#weaknesses): Despite its strengths, I have identified several weaknesses that warrant attention. First, the paper's claim that LLMs rely on a one-digit lookahead heuristic, regardless of tokenization, is not fully supported by the experimental evidence.…

<a id="arxiv-2502.05171"></a>
### Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach

`arxiv:2502.05171` · Reasoning and the "physics" of language models · 2025-02-07

- final **+0.22** (conf 1.00, pct 67) · impact -0.37 · KEEP
- mean rating (1–10): **6.3** · accept votes **5/7** · percentile rank_avg 60.9 (100=best) · rank in year 32.0 (1=best)
- NAIPv2 `-1.399` · NAIP-v1 `0.460` · SciJudge `0.457` · DGC-BERT `0.918`
- CycleReviewer 8B `6.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.0` Reject (S/P/C 3.25/2.75/2.5) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [seeallochnaya/3895](https://t.me/seeallochnaya/3895), [axisofordinary/6971](https://t.me/axisofordinary/6971), [gonzo_ML/5334](https://t.me/gonzo_ML/5334), [buckwheat_thoughts/110](https://t.me/buckwheat_thoughts/110), [axisofordinary/7296](https://t.me/axisofordinary/7296)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2502.05171.md#weaknesses): The paper does not include a comparison with existing methods for scaling language models.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2502.05171.md#weaknesses): While I find the core idea of this paper compelling, my analysis has revealed several weaknesses that warrant careful consideration. Firstly, the paper's comparison to existing recurrent models is limited.…

<a id="arxiv-2502.06807"></a>
### Competitive Programming with Large Reasoning Models

`arxiv:2502.06807` · Reasoning and the "physics" of language models · 2025-02-03

- final **-0.26** (conf 1.00, pct 16) · impact +0.65 · WATCH
- mean rating (1–10): **5.8** · accept votes **4/7** · percentile rank_avg 47.6 (100=best) · rank in year 62.0 (1=best)
- NAIPv2 `-0.521` · NAIP-v1 `0.472` · SciJudge `3.654` · DGC-BERT `0.503`
- CycleReviewer 8B `2.5` Reject · 70B `` 
- DeepReviewer 7B Std `3.2` Reject · 7B Fast `6.5` Reject (S/P/C 3.25/2.75/2.5) · 14B Fast `5.8` Accept
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/3.0) · SEA-E `6.0` Accept
- Telegram: [seeallochnaya/2304](https://t.me/seeallochnaya/2304), [data_secrets/6133](https://t.me/data_secrets/6133), [j_links/7875](https://t.me/j_links/7875), [axisofordinary/6978](https://t.me/axisofordinary/6978)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2502.06807.md#weaknesses): 1. The paper is not a research paper, but rather a report of the performance of OpenAI's o1, o1-ioi and o3 models on competitive programming tasks. The paper lacks a clear research question, methodology, and results section.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2502.06807.md#weaknesses): While this paper presents valuable findings, several weaknesses warrant careful consideration. Firstly, the paper lacks a detailed explanation of the reinforcement learning training process, which significantly impacts the interpretability of the results.…

<a id="arxiv-2502.00873"></a>
### Language Models Use Trigonometry to Do Addition

`arxiv:2502.00873` · Reasoning and the "physics" of language models · 2025-02-02

- final **+0.39** (conf 1.00, pct 87) · impact +1.03 · KEEP
- mean rating (1–10): **6.2** · accept votes **6/7** · percentile rank_avg 64.0 (100=best) · rank in year 19.0 (1=best)
- NAIPv2 `-0.740` · NAIP-v1 `0.506` · SciJudge `3.856` · DGC-BERT `0.164`
- CycleReviewer 8B `5.2` Accept · 70B `` 
- DeepReviewer 7B Std `8.0` Accept · 7B Fast `7.0` Accept (S/P/C 3.25/3.25/3.25) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [nn_for_science/2360](https://t.me/nn_for_science/2360)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2502.00873.md#weaknesses): The paper is not very novel. The authors show that numbers are represented as a helix in LLMs and that LLMs compute addition by manipulating this helix using the "Clock" algorithm. However, this has already been shown by previous works (e.g., Levy & Geva, 2024; Zhu et al., 2025).
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2502.00873.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. First, the paper's claim that the helical representation is the *only* way LLMs perform addition is not fully supported by the evidence.…

<a id="arxiv-2501.04519"></a>
### rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking

`arxiv:2501.04519` · Reasoning and the "physics" of language models · 2025-01-08

- final **+0.39** (conf 1.00, pct 88) · impact +1.54 · KEEP
- mean rating (1–10): **6.5** · accept votes **6/7** · percentile rank_avg 71.6 (100=best) · rank in year 7.0 (1=best)
- NAIPv2 `2.328` · NAIP-v1 `0.656` · SciJudge `3.818` · DGC-BERT `0.417`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.8` Accept · 7B Fast `7.0` Accept (S/P/C 3.0/3.25/3.25) · 14B Fast `6.2` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [data_secrets/5881](https://t.me/data_secrets/5881), [dealerAI/1054](https://t.me/dealerAI/1054), [axisofordinary/6880](https://t.me/axisofordinary/6880)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2501.04519.md#weaknesses): The proposed method requires a large amount of compute resources to train the models. - The proposed method is not generalizable to other tasks.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2501.04519.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further consideration. First, the paper's reliance on Python code execution for verification significantly limits the generalizability of the method.…

<a id="arxiv-2412.14135"></a>
### Scaling of Search and Learning: A Roadmap to Reproduce o1 from Reinforcement Learning Perspective

`arxiv:2412.14135` · Reasoning and the "physics" of language models · 2024-12-18

- final **-0.67** (conf 1.00, pct 2) · impact -1.58 · DROP
- mean rating (1–10): **3.8** · accept votes **0/7** · percentile rank_avg 7.1 (100=best) · rank in year 49.0 (1=best)
- NAIPv2 `-3.502` · NAIP-v1 `0.258` · SciJudge `-3.597` · DGC-BERT `0.003`
- CycleReviewer 8B `1.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.2` Reject · 7B Fast `4.8` Reject (S/P/C 2.25/2.75/2.25) · 14B Fast `3.0` Reject
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `5.0` Reject
- Telegram: [AGI_and_RL/881](https://t.me/AGI_and_RL/881)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2412.14135.md#weaknesses): This paper is a survey paper about the four key components of the o1 model: policy initialization, reward design, search, and learning. The authors first introduce the background of reinforcement learning and its connection to LLM. Then, the authors introduce the four key components of the o1 model.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2412.14135.md#weaknesses): One of the most significant weaknesses of this paper is its lack of empirical validation. While the authors propose a roadmap for reproducing o1 using reinforcement learning, they do not present any experimental results to support their claims.…

<a id="arxiv-2412.06769"></a>
### Training Large Language Models to Reason in a Continuous Latent Space

`arxiv:2412.06769` · Reasoning and the "physics" of language models · 2024-12-09

- final **+0.14** (conf 1.00, pct 58) · impact +0.21 · WATCH
- mean rating (1–10): **6.1** · accept votes **5/7** · percentile rank_avg 54.3 (100=best) · rank in year 17.0 (1=best)
- NAIPv2 `-1.824` · NAIP-v1 `0.554` · SciJudge `1.110` · DGC-BERT `0.750`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.2` Reject (S/P/C 2.5/3.0/2.75) · 14B Fast `6.2` Reject
- OpenReviewer `6.0` Accept (S/P/C 2.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [seeallochnaya/2541](https://t.me/seeallochnaya/2541), [data_secrets/5672](https://t.me/data_secrets/5672), [gonzo_ML/3567](https://t.me/gonzo_ML/3567), [gonzo_ML/3569](https://t.me/gonzo_ML/3569), [abstractDL/311](https://t.me/abstractDL/311), [gonzo_ML/4210](https://t.me/gonzo_ML/4210), [gonzo_ML/4622](https://t.me/gonzo_ML/4622), [buckwheat_thoughts/110](https://t.me/buckwheat_thoughts/110)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2412.06769.md#weaknesses): 1. The paper does not provide a thorough analysis of the limitations of the proposed method. For example, it is unclear how Coconut would perform on tasks that require more complex reasoning, such as multi-hop reasoning or reasoning over long chains of reasoning. 2. The paper does not provide a detailed discussion of the computational efficiency of Coconut compared to CoT.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2412.06769.md#weaknesses): Despite the strengths of this paper, I have identified several significant weaknesses that need to be addressed. First, the paper's claim that language space may not be optimal for reasoning, while intriguing, is not well-supported by the provided evidence.…

<a id="arxiv-2410.21272"></a>
### Arithmetic Without Algorithms: Language Models Solve Math With a Bag of Heuristics

`arxiv:2410.21272` · Reasoning and the "physics" of language models · 2024-10-28

- final **+0.60** (conf 1.00, pct 98) · impact +0.53 · KEEP
- mean rating (1–10): **6.6** · accept votes **6/7** · percentile rank_avg 66.4 (100=best) · rank in year 2.0 (1=best)
- NAIPv2 `-0.077` · NAIP-v1 `0.618` · SciJudge `1.411` · DGC-BERT `0.291`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.0` Accept (S/P/C 3.0/3.25/3.0) · 14B Fast `8.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [j_links/7782](https://t.me/j_links/7782)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2410.21272.md#weaknesses): The paper does not discuss how the heuristics are learned during training. The paper only shows that the heuristics are present in the final model, but it does not show how they are learned. It would be interesting to see how the heuristics are learned during training and how they change over time.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2410.21272.md#weaknesses): While this paper presents a compelling analysis of LLMs' arithmetic reasoning, several limitations warrant careful consideration. First, the study's focus on basic arithmetic operations (+, -, ×, ÷) with single-token operands and results restricts the generalizability of the findings.…

<a id="arxiv-2305.13673"></a>
### Physics of Language Models: Part 1, Learning Hierarchical Language Structures

`arxiv:2305.13673` · Reasoning and the "physics" of language models · 2023-05-23

- final **+0.45** (conf 1.00, pct 92) · impact -0.23 · KEEP
- mean rating (1–10): **6.1** · accept votes **6/7** · percentile rank_avg 64.1 (100=best) · rank in year 7.0 (1=best)
- NAIPv2 `-0.169` · NAIP-v1 `0.496` · SciJudge `1.237` · DGC-BERT `0.867`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `8.0` Accept · 7B Fast `6.7` Accept (S/P/C 3.0/3.0/2.67) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [dl_stories/848](https://t.me/dl_stories/848), [lovedeathtransformers/8152](https://t.me/lovedeathtransformers/8152)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2305.13673.md#weaknesses): The paper focuses on CFGs, which are a limited class of grammars. It would be interesting to see how the proposed approach generalizes to other types of grammars, such as context-sensitive grammars.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2305.13673.md#weaknesses): While the paper presents compelling results, I have identified several weaknesses that warrant further discussion. First, the paper's reliance on a single GPT-2 small architecture is a significant limitation. As the authors themselves acknowledge, this limits the generalizability of their findings.…

<a id="arxiv-2407.20311"></a>
### Physics of Language Models: Part 2.1, Grade-School Math and the Hidden Reasoning Process

`arxiv:2407.20311` · Reasoning and the "physics" of language models · 2024-07-29

- final **+0.32** (conf 1.00, pct 81) · impact +0.23 · KEEP
- mean rating (1–10): **6.4** · accept votes **5/7** · percentile rank_avg 58.1 (100=best) · rank in year 12.0 (1=best)
- NAIPv2 `-2.086` · NAIP-v1 `0.498` · SciJudge `1.933` · DGC-BERT `0.745`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.8` Reject · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/2.5) · 14B Fast `7.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/3.0) · SEA-E `6.0` Accept
- Telegram: [dl_stories/848](https://t.me/dl_stories/848), [lovedeathtransformers/8152](https://t.me/lovedeathtransformers/8152)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2407.20311.md#weaknesses): The paper focuses on a very specific domain (grade-school math) and it is unclear how the findings can be generalized to other domains. - The authors only consider a single model architecture (GPT-2) and it is unclear how the findings can be generalized to other model architectures.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2407.20311.md#weaknesses): While I found the paper to be generally strong, there are several weaknesses that I believe warrant further discussion. First, the paper's analysis of the model's internal states relies heavily on the V-probing technique, and the interpretation of these probing results could be more subjective than presented.…

<a id="arxiv-2309.14316"></a>
### Physics of Language Models: Part 3.1, Knowledge Storage and Extraction

`arxiv:2309.14316` · Reasoning and the "physics" of language models · 2023-09-25

- final **+0.21** (conf 1.00, pct 65) · impact -0.85 · KEEP
- mean rating (1–10): **6.1** · accept votes **4/7** · percentile rank_avg 44.0 (100=best) · rank in year 32.0 (1=best)
- NAIPv2 `-1.495` · NAIP-v1 `0.444` · SciJudge `-0.407` · DGC-BERT `0.152`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `5.2` Reject · 7B Fast `6.5` Accept (S/P/C 3.0/3.0/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [dl_stories/848](https://t.me/dl_stories/848), [rybolos_channel/1195](https://t.me/rybolos_channel/1195), [lovedeathtransformers/8152](https://t.me/lovedeathtransformers/8152)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2309.14316.md#weaknesses): The paper lacks novelty. The authors' proposed approach to understanding how LLMs store and extract knowledge from pretraining data has been explored in previous studies. The paper does not provide any new insights or contributions to the field.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2309.14316.md#weaknesses): While I appreciate the strengths of this paper, I have identified several weaknesses that warrant careful consideration. First, the paper's experimental setup, while controlled, lacks sufficient justification for its design choices. The authors introduce two training paradigms: pretraining followed by instruction fine-tuning, and 'mixed training'.…

<a id="arxiv-2309.14402"></a>
### Physics of Language Models: Part 3.2, Knowledge Manipulation

`arxiv:2309.14402` · Reasoning and the "physics" of language models · 2023-09-25

- final **+0.29** (conf 0.83, pct 76) · impact -0.50 · KEEP
- mean rating (1–10): **7.0** · accept votes **3/6** · percentile rank_avg 57.6 (100=best) · rank in year 13.0 (1=best)
- NAIPv2 `-1.719` · NAIP-v1 `0.454` · SciJudge `1.058` · DGC-BERT `0.177`
- CycleReviewer 8B `6.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast ``  (S/P/C None/None/None) · 14B Fast `7.0` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [dl_stories/848](https://t.me/dl_stories/848), [lovedeathtransformers/8152](https://t.me/lovedeathtransformers/8152)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2309.14402.md#weaknesses): 1. The paper only focuses on a specific type of knowledge manipulation tasks, i.e., the tasks that can be solved by simple logical reasoning. It would be interesting to see if the findings hold for more complex knowledge manipulation tasks. 2. The paper only considers a limited number of language models, i.e., GPT-2 and LLaMA.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2309.14402.md#weaknesses): While the paper presents compelling evidence for the limitations of LLMs in knowledge manipulation, several weaknesses warrant consideration. First, the paper's exclusive use of synthetic biographical data, while providing a controlled environment, limits the generalizability of the findings to real-world scenarios.…

<a id="arxiv-2404.05405"></a>
### Physics of Language Models: Part 3.3, Knowledge Capacity Scaling Laws

`arxiv:2404.05405` · Reasoning and the "physics" of language models · 2024-04-08

- final **+0.36** (conf 1.00, pct 84) · impact +1.15 · KEEP
- mean rating (1–10): **6.6** · accept votes **5/7** · percentile rank_avg 63.3 (100=best) · rank in year 4.0 (1=best)
- NAIPv2 `-0.638` · NAIP-v1 `0.514` · SciJudge `4.026` · DGC-BERT `0.237`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `5.7` Accept (S/P/C 2.67/2.67/2.67) · 14B Fast `7.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/4.0) · SEA-E `7.0` Accept
- Telegram: [seeallochnaya/1268](https://t.me/seeallochnaya/1268), [lovedeathtransformers/7555](https://t.me/lovedeathtransformers/7555), [dl_stories/848](https://t.me/dl_stories/848), [lovedeathtransformers/8152](https://t.me/lovedeathtransformers/8152)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2404.05405.md#weaknesses): The paper focuses on a synthetic dataset and doesn't study the knowledge storage capacity of real-world language models. The results are not generalizable to real-world models. The paper also doesn't discuss the limitations of the proposed method.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2404.05405.md#weaknesses): While this paper presents a compelling framework and significant findings, several limitations warrant careful consideration. A primary concern is the paper's reliance on synthetic datasets for training and evaluation.…

<a id="arxiv-2407.15017"></a>
### Knowledge Mechanisms in Large Language Models: A Survey and Perspective

`arxiv:2407.15017` · Reasoning and the "physics" of language models · 2024-07-22

- final **-0.21** (conf 1.00, pct 20) · impact +0.67 · WATCH
- mean rating (1–10): **5.8** · accept votes **3/7** · percentile rank_avg 39.0 (100=best) · rank in year 36.0 (1=best)
- NAIPv2 `-2.588` · NAIP-v1 `0.644` · SciJudge `1.682` · DGC-BERT `0.021`
- CycleReviewer 8B `5.8` Reject · 70B `` 
- DeepReviewer 7B Std `4.2` Reject · 7B Fast `5.8` Reject (S/P/C 2.5/2.75/2.5) · 14B Fast `5.8` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [AGI_and_RL/844](https://t.me/AGI_and_RL/844)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2407.15017.md#weaknesses): The paper does not provide any new insights or contributions to the field of LLMs.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2407.15017.md#weaknesses): Despite the paper's strengths, several limitations are evident. First, the paper's contribution is primarily a survey and perspective, which inherently relies on existing research rather than presenting new empirical findings or formal frameworks. This is a valid concern, as the paper's value is largely in its synthesis and interpretation of current knowledge.…

<a id="doi-10.1038-s41586-024-07522-w"></a>
### Language is primarily a tool for communication rather than thought

`doi:10.1038/s41586-024-07522-w` · Reasoning and the "physics" of language models · 2024-06-19

- final **-0.17** (conf 0.65, pct 21) · impact -2.67 · WATCH
- mean rating (1–10): **5.9** · accept votes **4/5** · percentile rank_avg 27.4 (100=best) · rank in year 43.0 (1=best)
- NAIPv2 `-5.289` · NAIP-v1 `0.204` · SciJudge `-10.659` · DGC-BERT `0.060`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std ``  · 7B Fast ``  (S/P/C None/None/None) · 14B Fast `5.8` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/2797](https://t.me/gonzo_ML/2797)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/doi_10.1038_s41586-024-07522-w.md#weaknesses): The paper does not provide a detailed analysis of the relationship between language and thought, and it does not fully explore the implications of the authors' argument for our understanding of human cognition and culture.
  - [DR-14B Fast](reviews/deepreviewer-14b/doi_10.1038_s41586-024-07522-w.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. First, while the authors present evidence for a 'double dissociation' between language and thought, I find that the evidence for the dissociation of language and thought in humans is not as strong as they suggest.…

<a id="arxiv-2406.11813"></a>
### How Do Large Language Models Acquire Factual Knowledge During Pretraining?

`arxiv:2406.11813` · Reasoning and the "physics" of language models · 2024-06-17

- final **+0.10** (conf 1.00, pct 51) · impact -0.27 · WATCH
- mean rating (1–10): **6.0** · accept votes **5/7** · percentile rank_avg 46.0 (100=best) · rank in year 26.0 (1=best)
- NAIPv2 `-1.204` · NAIP-v1 `0.502` · SciJudge `-0.321` · DGC-BERT `0.244`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.2` Reject · 7B Fast `6.2` Accept (S/P/C 2.75/3.25/2.75) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/6439](https://t.me/axisofordinary/6439)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2406.11813.md#weaknesses): The paper has some limitations. The authors only study the acquisition of factual knowledge in LLMs, and do not study other types of knowledge, such as common sense or world knowledge. The authors also only study the acquisition of knowledge in LLMs during pretraining, and do not study the acquisition of knowledge during fine-tuning or inference.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2406.11813.md#weaknesses): Despite the paper's strengths, I have identified several weaknesses that warrant further discussion. One major concern is the lack of a detailed justification for the choice of OLMo as the primary model for the experiments.…

<a id="arxiv-2406.11741"></a>
### Transcendence: Generative Models Can Outperform The Experts That Train Them

`arxiv:2406.11741` · Reasoning and the "physics" of language models · 2024-06-17

- final **+0.10** (conf 1.00, pct 50) · impact +0.55 · WATCH
- mean rating (1–10): **6.0** · accept votes **4/7** · percentile rank_avg 53.4 (100=best) · rank in year 19.0 (1=best)
- NAIPv2 `-1.136` · NAIP-v1 `0.593` · SciJudge `1.814` · DGC-BERT `0.654`
- CycleReviewer 8B `5.8` Reject · 70B `` 
- DeepReviewer 7B Std `5.8` Reject · 7B Fast `5.8` Accept (S/P/C 2.75/2.75/2.5) · 14B Fast `5.2` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `7.0` Accept
- Telegram: [seeallochnaya/1559](https://t.me/seeallochnaya/1559), [axisofordinary/6439](https://t.me/axisofordinary/6439)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2406.11741.md#weaknesses): The paper lacks a clear motivation for studying the phenomenon of "transcendence". While the paper provides a theoretical analysis of the conditions under which transcendence can occur, it is not clear why this phenomenon is important or interesting. The paper also lacks a clear discussion of the limitations of the theoretical results, and how they relate to the empirical results.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2406.11741.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. First, the paper's scope is limited by its focus on a specific setting: autoregressive transformers trained via cross-entropy minimization, primarily in the context of chess.…

<a id="arxiv-2406.03689"></a>
### Evaluating the World Model Implicit in a Generative Model

`arxiv:2406.03689` · Reasoning and the "physics" of language models · 2024-06-06

- final **+0.19** (conf 1.00, pct 64) · impact -0.53 · WATCH
- mean rating (1–10): **6.5** · accept votes **4/7** · percentile rank_avg 54.8 (100=best) · rank in year 16.0 (1=best)
- NAIPv2 `-1.565` · NAIP-v1 `0.471` · SciJudge `-1.463` · DGC-BERT `0.861`
- CycleReviewer 8B `5.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Reject · 7B Fast `5.2` Reject (S/P/C 2.5/2.75/2.5) · 14B Fast `6.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/3.0) · SEA-E `7.0` Accept
- Telegram: [boris_again/2625](https://t.me/boris_again/2625), [j_links/7562](https://t.me/j_links/7562), [axisofordinary/6441](https://t.me/axisofordinary/6441)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2406.03689.md#weaknesses): 1. The paper focuses on deterministic finite automata. However, in practice, the world is not deterministic. It would be interesting to see how the proposed metrics can be extended to handle stochasticity. 2. The paper only considers next-token prediction as the generative model.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2406.03689.md#weaknesses): Despite the paper's significant contributions, several limitations and concerns are evident. First, the proposed evaluation metrics are heavily dependent on the explicit knowledge of the underlying DFA, which is a significant limitation. The metrics require access to the true states, transitions, and accepting states of the DFA to compute the Myhill-Nerode boundary and interior.…

<a id="arxiv-2406.03445"></a>
### Pre-trained Large Language Models Use Fourier Features to Compute Addition

`arxiv:2406.03445` · Reasoning and the "physics" of language models · 2024-06-05

- final **+0.37** (conf 0.97, pct 86) · impact +1.10 · KEEP
- mean rating (1–10): **5.8** · accept votes **6/7** · percentile rank_avg 63.4 (100=best) · rank in year 3.0 (1=best)
- NAIPv2 `-1.313` · NAIP-v1 `0.676` · SciJudge `2.536` · DGC-BERT `0.871`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `7.0` Accept · 7B Fast `7.5` Accept (S/P/C 3.0/3.25/3.25) · 14B Fast `5.8` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2406.03445.md#weaknesses): 1. The paper's contribution is not very significant. The authors only analyzed a single task (addition) and a single model (GPT-2-XL) and did not generalize to other models or tasks. 2. The paper's findings are somewhat limited to the specific model and task analyzed. It would be more impactful if the authors could generalize their findings to other models and tasks. 3.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2406.03445.md#weaknesses): While this paper presents a compelling analysis of Fourier features in LLMs performing addition, several weaknesses warrant careful consideration. One significant limitation is the lack of a detailed mechanistic explanation of how these Fourier features are formed during pre-training.…

<a id="arxiv-2405.15071"></a>
### Grokked Transformers are Implicit Reasoners: A Mechanistic Journey to the Edge of Generalization

`arxiv:2405.15071` · Reasoning and the "physics" of language models · 2024-05-23

- final **+0.46** (conf 1.00, pct 93) · impact +1.17 · KEEP
- mean rating (1–10): **6.0** · accept votes **6/7** · percentile rank_avg 62.5 (100=best) · rank in year 5.0 (1=best)
- NAIPv2 `-0.824` · NAIP-v1 `0.652` · SciJudge `3.381` · DGC-BERT `0.698`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `7.0` Accept · 7B Fast `7.3` Accept (S/P/C 3.0/3.33/3.0) · 14B Fast `5.8` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [seeallochnaya/1473](https://t.me/seeallochnaya/1473), [lovedeathtransformers/7720](https://t.me/lovedeathtransformers/7720), [chillhousetech/773](https://t.me/chillhousetech/773), [axisofordinary/6349](https://t.me/axisofordinary/6349)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2405.15071.md#weaknesses): The paper is limited in its scope and does not fully explore the implications of its findings. The paper only studies two tasks, composition and comparison, and does not consider other types of reasoning, such as logical reasoning. The paper also does not consider other types of models, such as recurrent neural networks or graph neural networks, and only studies transformers.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2405.15071.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further consideration. First, the paper's use of the term 'systematic generalization' to describe OOD generalization in compositional reasoning is not entirely consistent with its typical usage in the literature.…

<a id="arxiv-2405.14838"></a>
### From Explicit CoT to Implicit CoT: Learning to Internalize CoT Step by Step

`arxiv:2405.14838` · Reasoning and the "physics" of language models · 2024-05-23

- final **-0.09** (conf 1.00, pct 26) · impact -0.02 · WATCH
- mean rating (1–10): **5.6** · accept votes **4/7** · percentile rank_avg 42.0 (100=best) · rank in year 29.0 (1=best)
- NAIPv2 `-2.850` · NAIP-v1 `0.458` · SciJudge `1.787` · DGC-BERT `0.909`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `6.5` Accept (S/P/C 2.75/3.25/2.75) · 14B Fast `5.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/3583](https://t.me/gonzo_ML/3583), [gonzo_ML/3568](https://t.me/gonzo_ML/3568), [axisofordinary/6364](https://t.me/axisofordinary/6364), [axisofordinary/6807](https://t.me/axisofordinary/6807), [axisofordinary/6481](https://t.me/axisofordinary/6481)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2405.14838.md#weaknesses): 1. The paper lacks novelty. The proposed method is similar to knowledge distillation, which transfers the knowledge from a teacher model to a student model. The difference is that the proposed method removes the intermediate steps and finetunes the model. However, the finetuning process is similar to knowledge distillation. 2. The proposed method is not evaluated on a wide range of tasks.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2405.14838.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. First, while the paper demonstrates promising results on arithmetic and grade-school math problems, the scope of the evaluation is limited.…

<a id="doi-10.1038-d41586-024-01413-w"></a>
### Why mathematics is set to be revolutionized by AI

`doi:10.1038/d41586-024-01413-w` · Reasoning and the "physics" of language models · 2024-05-14

- final **-0.27** (conf 0.44, pct 15) · impact -1.40 · WATCH · partial fulltext
- mean rating (1–10): **5.2** · accept votes **3/5** · percentile rank_avg 21.5 (100=best) · rank in year 45.0 (1=best)
- NAIPv2 `-4.922` · NAIP-v1 `0.454` · SciJudge `-7.115` · DGC-BERT `0.036`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std ``  · 7B Fast ``  (S/P/C None/None/None) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/6315](https://t.me/axisofordinary/6315)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/doi_10.1038_d41586-024-01413-w.md#weaknesses): The paper is not well written. The idea of generating mathematical conjectures using machine learning is interesting, but the paper does not provide enough detail on how the method works and how it is implemented. The paper also does not provide enough evidence that the generated conjectures are actually true or useful.
  - [DR-14B Fast](reviews/deepreviewer-14b/doi_10.1038_d41586-024-01413-w.md#weaknesses): While the article presents a compelling vision of AI's role in mathematics, several weaknesses warrant attention. Firstly, the article lacks a detailed discussion of the specific AI techniques employed in the case studies it presents.…

<a id="arxiv-2402.01817"></a>
### LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks

`arxiv:2402.01817` · Reasoning and the "physics" of language models · 2024-02-02

- final **-0.20** (conf 1.00, pct 20) · impact -0.08 · DROP
- mean rating (1–10): **6.0** · accept votes **2/7** · percentile rank_avg 35.1 (100=best) · rank in year 41.0 (1=best)
- NAIPv2 `-2.639` · NAIP-v1 `0.513` · SciJudge `0.099` · DGC-BERT `0.004`
- CycleReviewer 8B `3.5` Reject · 70B `` 
- DeepReviewer 7B Std `4.2` Reject · 7B Fast `5.5` Reject (S/P/C 2.75/2.5/2.5) · 14B Fast `5.8` Reject
- OpenReviewer `8.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [data_secrets/5225](https://t.me/data_secrets/5225), [tech_priestess/1697](https://t.me/tech_priestess/1697)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2402.01817.md#weaknesses): The paper does not provide sufficient evidence to support its claims about the limitations of LLMs in planning and reasoning tasks. The paper relies on previous studies to support its claims, but does not provide any new empirical evidence. The paper also does not provide a clear description of the LLM-Modulo framework, and how it differs from existing approaches.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2402.01817.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further consideration. First, while the paper introduces the LLM-Modulo framework, the technical novelty of the approach is somewhat limited. The core idea of using LLMs as generators and symbolic methods for verification is not entirely new, as the authors themselves acknowledge.…

<a id="arxiv-2312.13558"></a>
### The Truth is in There: Improving Reasoning in Language Models with Layer-Selective Rank Reduction

`arxiv:2312.13558` · Reasoning and the "physics" of language models · 2023-12-21

- final **+0.02** (conf 1.00, pct 39) · impact -0.91 · WATCH
- mean rating (1–10): **5.8** · accept votes **4/7** · percentile rank_avg 42.6 (100=best) · rank in year 34.0 (1=best)
- NAIPv2 `-1.128` · NAIP-v1 `0.379` · SciJudge `0.058` · DGC-BERT `0.923`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `4.8` Reject · 7B Fast `5.5` Reject (S/P/C 2.5/2.75/2.25) · 14B Fast `6.2` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [data_secrets/3301](https://t.me/data_secrets/3301), [j_links/7306](https://t.me/j_links/7306), [axisofordinary/5886](https://t.me/axisofordinary/5886), [tech_priestess/1311](https://t.me/tech_priestess/1311)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2312.13558.md#weaknesses): 1. The paper lacks a clear explanation of the underlying mechanism of LASER and how it improves the performance of LLMs. While the paper provides some insights into the relationship between the model's training data and the samples that benefit from LASER, it does not provide a comprehensive explanation of how LASER works. 2.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2312.13558.md#weaknesses): While the paper presents a compelling approach to improving LLM performance, several weaknesses warrant careful consideration. First, the paper lacks a detailed analysis of the computational cost associated with the proposed LASER method.…

<a id="openreview-hcQfTsVnBo"></a>
### Grokking Group Multiplication with Cosets

`openreview:hcQfTsVnBo` · Reasoning and the "physics" of language models · unknown

- final **+0.43** (conf 1.00, pct 92) · impact -1.58 · KEEP
- mean rating (1–10): **6.5** · accept votes **5/7** · percentile rank_avg 50.1 (100=best) · rank in year 2.0 (1=best)
- NAIPv2 `-3.244` · NAIP-v1 `0.371` · SciJudge `-7.266` · DGC-BERT `0.035`
- CycleReviewer 8B `6.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.8` Accept · 7B Fast `7.0` Accept (S/P/C 3.25/3.0/3.0) · 14B Fast `6.8` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [axisofordinary/6435](https://t.me/axisofordinary/6435)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/openreview_hcQfTsVnBo.md#weaknesses): The paper is more of a case study and I am not sure if it is ready for ICLR. The paper should be expanded to include more details about the experiments, the experimental setup, the data, the models, etc.
  - [DR-14B Fast](reviews/deepreviewer-14b/openreview_hcQfTsVnBo.md#weaknesses): Despite its strengths, the paper has several notable weaknesses that I believe should be addressed. One of the primary concerns is the limited generalizability of the findings. The paper focuses on a highly constrained setting: a one-hidden-layer fully connected network trained on the specific task of group multiplication in S5 and S6.…

<a id="arxiv-2309.12288"></a>
### The Reversal Curse: LLMs trained on "A is B" fail to learn "B is A"

`arxiv:2309.12288` · Reasoning and the "physics" of language models · 2023-09-21

- final **+0.17** (conf 1.00, pct 61) · impact +0.70 · WATCH
- mean rating (1–10): **5.7** · accept votes **4/7** · percentile rank_avg 55.3 (100=best) · rank in year 16.0 (1=best)
- NAIPv2 `1.487` · NAIP-v1 `0.676` · SciJudge `1.893` · DGC-BERT `0.254`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.2` Reject · 7B Fast `6.3` Accept (S/P/C 2.67/2.67/2.67) · 14B Fast `5.8` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [abstractDL/245](https://t.me/abstractDL/245), [gonzo_ML/4618](https://t.me/gonzo_ML/4618), [boris_again/1973](https://t.me/boris_again/1973)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2309.12288.md#weaknesses): The main weakness of this paper is that the experiments are not convincing. The authors only use a small dataset of 30 facts about celebrities. The authors also only perform finetuning on this dataset. It is unclear whether the Reversal Curse still exists in pretraining. The authors also only use GPT-3 and Llama-1 models. It is unclear whether the Reversal Curse exists in other models.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2309.12288.md#weaknesses): in current LLM architectures and training methods, and suggest that further work is needed to address this limitation.

<a id="arxiv-2304.15004"></a>
### Are Emergent Abilities of Large Language Models a Mirage?

`arxiv:2304.15004` · Reasoning and the "physics" of language models · 2023-04-28

- final **+0.37** (conf 1.00, pct 85) · impact +0.34 · KEEP
- mean rating (1–10): **6.2** · accept votes **5/7** · percentile rank_avg 62.9 (100=best) · rank in year 8.0 (1=best)
- NAIPv2 `0.762` · NAIP-v1 `0.551` · SciJudge `2.855` · DGC-BERT `0.254`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.2` Accept (S/P/C 2.75/3.0/3.0) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [dl_stories/794](https://t.me/dl_stories/794), [abstractDL/215](https://t.me/abstractDL/215), [lovedeathtransformers/6780](https://t.me/lovedeathtransformers/6780), [chillhousetech/524](https://t.me/chillhousetech/524), [rybolos_channel/995](https://t.me/rybolos_channel/995), [Victor_Osyka/511](https://t.me/Victor_Osyka/511), [emptyset_of_ideas/429](https://t.me/emptyset_of_ideas/429)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2304.15004.md#weaknesses): The paper focuses primarily on LLMs, but the authors do not provide a clear explanation of why emergent abilities are not a fundamental property of other types of models, such as computer vision models. - The paper does not provide a clear explanation of how the choice of metric affects the performance of models on different tasks.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2304.15004.md#weaknesses): While I appreciate the paper's contributions, I have identified several weaknesses that warrant careful consideration. First, the paper's critique of 'emergence' is primarily focused on the discontinuity of performance scaling, neglecting other aspects of emergence, such as the unpredictability of *which* abilities will emerge.…

<a id="arxiv-2302.00923"></a>
### Multimodal Chain-of-Thought Reasoning in Language Models

`arxiv:2302.00923` · Reasoning and the "physics" of language models · 2023-02-02

- final **+0.04** (conf 1.00, pct 42) · impact +0.93 · WATCH
- mean rating (1–10): **6.2** · accept votes **5/7** · percentile rank_avg 58.3 (100=best) · rank in year 11.0 (1=best)
- NAIPv2 `-0.418` · NAIP-v1 `0.730` · SciJudge `1.666` · DGC-BERT `0.793`
- CycleReviewer 8B `5.8` Accept · 70B `` 
- DeepReviewer 7B Std `5.2` Reject · 7B Fast `5.7` Accept (S/P/C 2.67/3.0/2.67) · 14B Fast `5.8` Reject
- OpenReviewer `8.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [j_links/6440](https://t.me/j_links/6440), [axisofordinary/4464](https://t.me/axisofordinary/4464), [axisofordinary/4323](https://t.me/axisofordinary/4323)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2302.00923.md#weaknesses): The method is not novel. The idea of using two stages for CoT reasoning has been proposed in previous works, such as (1). The method of using a single-head attention network to correlate text tokens with image patches has also been proposed in previous works, such as (2).…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2302.00923.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further consideration. First, the paper's reliance on annotated rationales is a significant limitation. As the authors themselves acknowledge, the datasets used in this study, ScienceQA and A-OKVQA, provide ground-truth rationales, which are not always available in real-world scenarios.…

<a id="arxiv-2301.06627"></a>
### Dissociating language and thought in large language models

`arxiv:2301.06627` · Reasoning and the "physics" of language models · 2023-01-16

- final **+0.05** (conf 1.00, pct 44) · impact -0.44 · WATCH
- mean rating (1–10): **6.2** · accept votes **3/7** · percentile rank_avg 47.8 (100=best) · rank in year 29.0 (1=best)
- NAIPv2 `-2.279` · NAIP-v1 `0.436` · SciJudge `1.612` · DGC-BERT `0.311`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.2` Reject · 7B Fast `6.5` Reject (S/P/C 2.75/2.75/2.75) · 14B Fast `6.8` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [axisofordinary/4244](https://t.me/axisofordinary/4244)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2301.06627.md#weaknesses): 1. The paper lacks a clear and concise abstract that summarizes the main contributions and findings of the paper. 2. The paper lacks a clear and concise introduction that provides background information and sets the stage for the rest of the paper. 3. The paper lacks a clear and concise conclusion that summarizes the main findings and contributions of the paper. 4.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2301.06627.md#weaknesses): Despite its strengths, I have identified several weaknesses in this paper that warrant careful consideration. First, the paper's definition of formal linguistic competence, while generally clear, lacks sufficient nuance regarding the role of semantics.…

<a id="arxiv-2301.05217"></a>
### Progress measures for grokking via mechanistic interpretability

`arxiv:2301.05217` · Reasoning and the "physics" of language models · 2023-01-12

- final **+0.65** (conf 1.00, pct 99) · impact +0.01 · KEEP
- mean rating (1–10): **6.6** · accept votes **7/7** · percentile rank_avg 67.5 (100=best) · rank in year 4.0 (1=best)
- NAIPv2 `-0.686` · NAIP-v1 `0.491` · SciJudge `2.071` · DGC-BERT `0.559`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `8.0` Accept · 7B Fast `8.0` Accept (S/P/C 3.5/3.5/3.5) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [j_links/6406](https://t.me/j_links/6406)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2301.05217.md#weaknesses): The paper focuses on a very specific task and model architecture, which limits the generalizability of the findings. It is not clear how the results would extend to other tasks or model architectures. - The paper does not provide a clear explanation for why the model uses the Fourier multiplication algorithm to solve the modular addition task.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2301.05217.md#weaknesses): While this paper presents a compelling analysis of grokking in modular addition, several limitations warrant careful consideration. The most significant weakness is the narrow scope of the empirical investigation. The entire experimental analysis focuses on a single model architecture: a one-layer transformer without LayerNorm, trained on a single task, modular addition.…

<a id="arxiv-2212.09196"></a>
### Emergent Analogical Reasoning in Large Language Models

`arxiv:2212.09196` · Reasoning and the "physics" of language models · 2022-12-19

- final **+0.13** (conf 1.00, pct 56) · impact +0.98 · WATCH
- mean rating (1–10): **6.3** · accept votes **5/7** · percentile rank_avg 56.1 (100=best) · rank in year 7.0 (1=best)
- NAIPv2 `-1.596` · NAIP-v1 `0.756` · SciJudge `2.294` · DGC-BERT `0.046`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `5.2` Reject (S/P/C 2.5/3.0/2.25) · 14B Fast `6.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/4.0/3.0) · SEA-E `6.0` Accept
- Telegram: [dtulinov/501](https://t.me/dtulinov/501), [axisofordinary/4214](https://t.me/axisofordinary/4214), [axisofordinary/4140](https://t.me/axisofordinary/4140)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2212.09196.md#weaknesses): The paper would benefit from a more detailed discussion of the limitations of the study. For example, the authors note that GPT-3 was not able to use analogies to solve a transfer problem involving construction and use of simple tools. However, it is not clear why this is the case, or whether it is a limitation of GPT-3 or simply a limitation of the particular task.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2212.09196.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. First, the paper's experimental scope is limited to a single LLM, GPT-3. While the authors acknowledge the existence of other LLMs, such as PaLM and Claude, they do not provide any evidence of how these models perform on the same tasks.…

<a id="openreview-wUU-7XTL5XO"></a>
### Large Language Models Still Can't Plan / PlanBench (Kambhampati)

`openreview:wUU-7XTL5XO` · Reasoning and the "physics" of language models · unknown

- final **-0.30** (conf 1.00, pct 14) · impact +0.29 · DROP
- mean rating (1–10): **5.4** · accept votes **2/7** · percentile rank_avg 33.6 (100=best) · rank in year 8.0 (1=best)
- NAIPv2 `-1.282` · NAIP-v1 `0.555` · SciJudge `1.625` · DGC-BERT `0.014`
- CycleReviewer 8B `5.2` Reject · 70B `` 
- DeepReviewer 7B Std `3.0` Reject · 7B Fast `4.2` Reject (S/P/C 2.5/2.25/2.25) · 14B Fast `5.7` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [data_secrets/5225](https://t.me/data_secrets/5225)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/openreview_wUU-7XTL5XO.md#weaknesses): The paper only evaluates the benchmark on GPT-3, Instruct-GPT3 and BLOOM, and does not evaluate other popular LLMs such as Llama-2, Vicuna, etc. - The paper only evaluates the benchmark on simple planning tasks, and does not evaluate the benchmark on more complex planning tasks. - The paper does not provide any analysis of why the LLMs perform poorly on the benchmark.…
  - [DR-14B Fast](reviews/deepreviewer-14b/openreview_wUU-7XTL5XO.md#weaknesses): After a thorough examination of the paper, I have identified several key weaknesses that warrant discussion. Firstly, the paper's evaluation is limited by the choice of LLMs. The experiments were conducted using GPT-3, Instruct-GPT3, and BLOOM, all of which are now considered outdated.…

<a id="arxiv-2203.11171"></a>
### Self-Consistency Improves Chain of Thought Reasoning in Language Models

`arxiv:2203.11171` · Reasoning and the "physics" of language models · 2022-03-21

- final **+0.25** (conf 1.00, pct 73) · impact +1.83 · KEEP
- mean rating (1–10): **5.7** · accept votes **7/7** · percentile rank_avg 60.5 (100=best) · rank in year 4.0 (1=best)
- NAIPv2 `-2.383` · NAIP-v1 `0.759` · SciJudge `3.944` · DGC-BERT `0.917`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.0` Accept (S/P/C 3.0/3.25/2.75) · 14B Fast `4.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [seeallochnaya/1765](https://t.me/seeallochnaya/1765), [axisofordinary/7585](https://t.me/axisofordinary/7585), [gonzo_ML/1885](https://t.me/gonzo_ML/1885), [axisofordinary/3588](https://t.me/axisofordinary/3588), [axisofordinary/2249](https://t.me/axisofordinary/2249), [rybolos_channel/700](https://t.me/rybolos_channel/700)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2203.11171.md#weaknesses): The paper could benefit from a more thorough discussion of the limitations of the proposed method. For example, the authors mention that self-consistency incurs more computation cost, but it would be helpful to provide more details on how much more expensive it is compared to other methods.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2203.11171.md#weaknesses): While the paper presents a compelling method with strong empirical results, there are several limitations that warrant further discussion. First, the paper lacks a detailed analysis of the computational cost associated with self-consistency.…

<a id="arxiv-2608.05136"></a>
### The Loss Does Not See the Basis, but Adam Does

`arxiv:2608.05136` · Data, training, optimization · 2026-08-05

- final **+0.34** (conf 1.00, pct 83) · impact -0.43 · KEEP
- mean rating (1–10): **6.4** · accept votes **6/7** · percentile rank_avg 62.4 (100=best) · rank in year 25.0 (1=best)
- NAIPv2 `1.129` · NAIP-v1 `0.627` · SciJudge `-3.627` · DGC-BERT `0.208`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.5` Accept (S/P/C 2.75/3.0/2.75) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/5956](https://t.me/gonzo_ML/5956)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2608.05136.md#weaknesses): The main weakness of the paper is that the authors do not provide a clear explanation of why the low-rank bias is present in some non-adaptive methods such as Shampoo and Muon. The authors only provide a partial explanation of why the low-rank bias is present in these methods.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2608.05136.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, while the paper introduces the concept of gauge equivariance and its importance for preserving low-rank solutions, it does not provide a sufficiently intuitive explanation of this concept in the introduction.…

<a id="arxiv-2607.27372"></a>
### Explorative Modeling: Unlocking a Third Pretraining Axis and End-to-End Generation

`arxiv:2607.27372` · Data, training, optimization · 2026-07-29

- final **+0.29** (conf 1.00, pct 77) · impact +1.42 · KEEP
- mean rating (1–10): **6.2** · accept votes **7/7** · percentile rank_avg 71.1 (100=best) · rank in year 7.0 (1=best)
- NAIPv2 `0.640` · NAIP-v1 `0.771` · SciJudge `2.127` · DGC-BERT `0.888`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/2.67) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/5858](https://t.me/gonzo_ML/5858)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2607.27372.md#weaknesses): The paper does not provide a detailed explanation of the mathematical formulation of the XM approach. While the authors provide an intuitive explanation of the approach, a more formal mathematical description would be helpful for readers who want to understand the underlying principles of the method.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2607.27372.md#weaknesses): section, there are several limitations that need to be addressed in future work.

<a id="arxiv-2601.21343"></a>
### Self-Improving Pretraining: using post-trained models to pretrain better models

`arxiv:2601.21343` · Data, training, optimization · 2026-01-29

- final **-0.32** (conf 1.00, pct 12) · impact -0.43 · DROP
- mean rating (1–10): **5.8** · accept votes **3/7** · percentile rank_avg 38.5 (100=best) · rank in year 65.0 (1=best)
- NAIPv2 `-2.145` · NAIP-v1 `0.484` · SciJudge `0.240` · DGC-BERT `0.335`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.2` Reject · 7B Fast `5.5` Reject (S/P/C 2.5/2.5/2.5) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/4691](https://t.me/gonzo_ML/4691), [axisofordinary/8485](https://t.me/axisofordinary/8485)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2601.21343.md#weaknesses): 1. The paper lacks a clear comparison with existing methods. The authors should provide a more comprehensive comparison with other approaches to improve the training of LLMs, such as chain-of-thought and reasoning-based pretraining.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2601.21343.md#weaknesses): of each approach. Finally, the paper's focus on addressing the limitations of standard pretraining methods and proposing concrete solutions is a valuable contribution to the field. The authors clearly identify the shortcomings of current approaches and offer a well-thought-out alternative that has the potential to significantly advance the state-of-the-art in language model training.

<a id="arxiv-2512.24695"></a>
### Nested Learning: The Illusion of Deep Learning Architectures

`arxiv:2512.24695` · Data, training, optimization · 2025-12-31

- final **-0.65** (conf 0.82, pct 3) · impact -2.10 · DROP
- mean rating (1–10): **4.0** · accept votes **0/6** · percentile rank_avg 11.7 (100=best) · rank in year 81.0 (1=best)
- NAIPv2 `-2.021` · NAIP-v1 `0.319` · SciJudge `-7.151` · DGC-BERT `0.206`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std ``  · 7B Fast `5.0` Reject (S/P/C 2.5/2.5/2.5) · 14B Fast `4.2` Reject
- OpenReviewer `5.0` Reject (S/P/C 2.0/2.0/2.0) · SEA-E `3.0` Reject
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2512.24695.md#weaknesses): The paper's presentation is not clear enough, and the motivation for the Nested Learning paradigm is not well explained. The authors should provide more clarity on how the Nested Learning paradigm addresses the limitations of current machine learning models and why it is a necessary step forward.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2512.24695.md#weaknesses): section, the paper suffers from a lack of clarity and precision in its definitions and experimental setup, which limits the impact of its contributions.

<a id="arxiv-2510.05491"></a>
### NorMuon: Making Muon more efficient and scalable

`arxiv:2510.05491` · Data, training, optimization · 2025-10-07

- final **+0.06** (conf 1.00, pct 47) · impact -0.51 · WATCH
- mean rating (1–10): **5.9** · accept votes **6/7** · percentile rank_avg 47.9 (100=best) · rank in year 61.0 (1=best)
- NAIPv2 `-1.236` · NAIP-v1 `0.512` · SciJudge `-1.756` · DGC-BERT `0.663`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.2` Accept · 7B Fast `7.0` Accept (S/P/C 3.25/3.25/3.0) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2510.05491.md#weaknesses): 1. The paper lacks novelty. The proposed method is a combination of Muon and Adam, which has been done in previous works (1, 2). The authors should compare NorMuon with these works and explain the differences and advantages of their method.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2510.05491.md#weaknesses): section, there are several areas where the paper could be strengthened to provide a more complete picture of NorMuon's capabilities and limitations.

<a id="arxiv-2508.11408"></a>
### On-Policy RL Meets Off-Policy Experts: Harmonizing Supervised Fine-Tuning and Reinforcement Learning via Dynamic Weighting

`arxiv:2508.11408` · Data, training, optimization · 2025-08-15

- final **+0.16** (conf 1.00, pct 61) · impact -0.16 · WATCH
- mean rating (1–10): **6.1** · accept votes **5/7** · percentile rank_avg 53.9 (100=best) · rank in year 44.0 (1=best)
- NAIPv2 `1.382` · NAIP-v1 `0.602` · SciJudge `-1.549` · DGC-BERT `0.046`
- CycleReviewer 8B `5.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/2.5) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [abstractDL/345](https://t.me/abstractDL/345)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2508.11408.md#weaknesses): 1. The paper lacks a detailed discussion on the potential limitations of the proposed approach. For example, how does the proposed method perform when dealing with large-scale datasets or complex tasks? Are there any potential trade-offs between the performance improvement and computational efficiency?
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2508.11408.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further consideration. First, while the paper introduces a token-wise weighting function, ϕ, it lacks a thorough analysis of its impact on the model's learning process beyond the overall performance metrics.…

<a id="arxiv-2507.12856"></a>
### Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved)

`arxiv:2507.12856` · Data, training, optimization · 2025-07-17

- final **-0.24** (conf 1.00, pct 18) · impact -1.96 · DROP
- mean rating (1–10): **5.8** · accept votes **3/7** · percentile rank_avg 36.1 (100=best) · rank in year 72.0 (1=best)
- NAIPv2 `-3.164` · NAIP-v1 `0.229` · SciJudge `-3.125` · DGC-BERT `0.201`
- CycleReviewer 8B `5.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `5.8` Reject (S/P/C 2.5/2.75/2.25) · 14B Fast `6.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [abstractDL/345](https://t.me/abstractDL/345)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2507.12856.md#weaknesses): 1. The novelty of the paper is limited. The connection between SFT and RL is not new. The proposed method is a simple modification of SFT. 2. The experiments are not comprehensive. The authors only evaluate the proposed method on two tasks, one for large language models and one for continuous control tasks.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2507.12856.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. First, the paper's presentation of the connection between SFT and RL is not as clear as it could be.…

<a id="arxiv-2506.08007"></a>
### Reinforcement Pre-Training

`arxiv:2506.08007` · Data, training, optimization · 2025-06-09

- final **-0.42** (conf 1.00, pct 8) · impact -1.06 · DROP
- mean rating (1–10): **5.5** · accept votes **3/7** · percentile rank_avg 32.5 (100=best) · rank in year 76.0 (1=best)
- NAIPv2 `-2.857` · NAIP-v1 `0.424` · SciJudge `-2.290` · DGC-BERT `0.913`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `3.0` Reject · 7B Fast `6.0` Reject (S/P/C 2.67/2.67/2.67) · 14B Fast `5.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [data_secrets/7130](https://t.me/data_secrets/7130), [dealerAI/1339](https://t.me/dealerAI/1339), [AGI_and_RL/1136](https://t.me/AGI_and_RL/1136), [axisofordinary/7337](https://t.me/axisofordinary/7337)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2506.08007.md#weaknesses): 1. The authors claim that RPT offers a scalable and general-purpose approach to RL pre-training, but the authors only conduct experiments on a small-scale model (14B) and a specific dataset (mathematical documents). The authors should conduct experiments on large-scale models (e.g., 70B, 130B) and general-domain text. 2.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2506.08007.md#weaknesses): While I appreciate the novelty of the proposed approach, I have identified several weaknesses that need to be addressed. First, the experimental evaluation is limited in scope. The pre-training is exclusively performed on the OmniMATH dataset, which consists of mathematical problems and solutions. This narrow focus raises concerns about the generalizability of the method to other domains.…

<a id="arxiv-2505.24832"></a>
### How much do language models memorize?

`arxiv:2505.24832` · Data, training, optimization · 2025-05-30

- final **+0.26** (conf 1.00, pct 74) · impact +0.51 · KEEP
- mean rating (1–10): **6.0** · accept votes **6/7** · percentile rank_avg 61.4 (100=best) · rank in year 27.0 (1=best)
- NAIPv2 `-0.806` · NAIP-v1 `0.508` · SciJudge `2.631` · DGC-BERT `0.785`
- CycleReviewer 8B `5.2` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.5` Accept (S/P/C 3.25/3.25/3.25) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [data_secrets/7050](https://t.me/data_secrets/7050), [nn_for_science/2464](https://t.me/nn_for_science/2464), [gonzo_ML/5721](https://t.me/gonzo_ML/5721), [axisofordinary/7283](https://t.me/axisofordinary/7283), [abstractDL/338](https://t.me/abstractDL/338)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2505.24832.md#weaknesses): The paper's main contribution is the proposed definition of memorization based on Kolmogorov complexity. However, this definition is not very practical, as it is difficult to estimate Kolmogorov complexity in practice. The paper also does not provide a clear comparison with existing definitions of memorization, such as those based on perplexity or likelihood.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2505.24832.md#weaknesses): While this paper presents a valuable framework for understanding memorization in language models, I have identified several weaknesses that warrant further consideration. First, the paper's reliance on a single reference model, typically a larger model trained on a superset of the training data, raises concerns about the robustness of the memorization metric.…

<a id="arxiv-2410.07041"></a>
### Emergent properties with repeated examples

`arxiv:2410.07041` · Data, training, optimization · 2024-10-09

- final **+0.09** (conf 1.00, pct 50) · impact -2.25 · WATCH
- mean rating (1–10): **6.1** · accept votes **5/7** · percentile rank_avg 40.8 (100=best) · rank in year 31.0 (1=best)
- NAIPv2 `-2.184` · NAIP-v1 `0.120` · SciJudge `-4.219` · DGC-BERT `0.719`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `6.5` Accept (S/P/C 2.75/3.25/2.75) · 14B Fast `6.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [abstractDL/300](https://t.me/abstractDL/300), [axisofordinary/6696](https://t.me/axisofordinary/6696)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2410.07041.md#weaknesses): The main weakness of the paper is that the results are only shown on synthetic datasets. While the authors argue that these datasets are well suited for studying the effect of repeated examples, it would be nice to see some results on real-world datasets.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2410.07041.md#weaknesses): While I appreciate the strengths of this paper, I have identified several weaknesses that warrant careful consideration. Firstly, the paper's reliance on synthetic datasets, while allowing for controlled experiments, limits the generalizability of the findings to real-world scenarios.…

<a id="arxiv-2409.03137"></a>
### The AdEMAMix Optimizer: Better, Faster, Older

`arxiv:2409.03137` · Data, training, optimization · 2024-09-05

- final **+0.32** (conf 1.00, pct 80) · impact -0.30 · KEEP
- mean rating (1–10): **6.1** · accept votes **4/7** · percentile rank_avg 51.2 (100=best) · rank in year 21.0 (1=best)
- NAIPv2 `-0.882` · NAIP-v1 `0.472` · SciJudge `-0.025` · DGC-BERT `0.901`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `7.5` Accept (S/P/C 3.25/3.25/3.25) · 14B Fast `6.5` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/6587](https://t.me/axisofordinary/6587)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2409.03137.md#weaknesses): The paper does not provide a theoretical analysis of the proposed optimizer. - The paper does not provide a detailed analysis of the hyperparameters, including how they affect the performance and how to choose them in practice. - The paper does not compare AdEMAMix with other optimizers, such as SGD and AdamW with different hyperparameters.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2409.03137.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, while the authors provide an intuitive explanation for why AdEMAMix works, the paper lacks a rigorous theoretical analysis of the proposed method.…

<a id="arxiv-2405.20541"></a>
### Perplexed by Perplexity: Perplexity-Based Data Pruning With Small Reference Models

`arxiv:2405.20541` · Data, training, optimization · 2024-05-30

- final **+0.16** (conf 1.00, pct 59) · impact -0.68 · WATCH
- mean rating (1–10): **5.2** · accept votes **4/7** · percentile rank_avg 39.6 (100=best) · rank in year 34.0 (1=best)
- NAIPv2 `-1.069` · NAIP-v1 `0.432` · SciJudge `-0.605` · DGC-BERT `0.758`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.2` Reject · 7B Fast `6.0` Accept (S/P/C 3.25/3.0/2.75) · 14B Fast `7.0` Accept
- OpenReviewer `2.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [data_secrets/4407](https://t.me/data_secrets/4407), [axisofordinary/6387](https://t.me/axisofordinary/6387)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2405.20541.md#weaknesses): The paper's main contribution is an empirical investigation of perplexity-based data pruning for LLMs. While the results are promising, the paper lacks a theoretical foundation or a clear explanation of the underlying mechanisms driving the observed effects.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2405.20541.md#weaknesses): While this paper presents compelling results, several limitations warrant careful consideration. First, the paper's exploration of optimal pruning strategies is primarily empirical, lacking a theoretical framework to explain why certain perplexity ranges are more effective for different datasets.…

<a id="arxiv-2405.20233"></a>
### Grokfast: Accelerated Grokking by Amplifying Slow Gradients

`arxiv:2405.20233` · Data, training, optimization · 2024-05-30

- final **+0.18** (conf 1.00, pct 62) · impact -0.81 · WATCH
- mean rating (1–10): **6.0** · accept votes **3/7** · percentile rank_avg 49.8 (100=best) · rank in year 24.0 (1=best)
- NAIPv2 `1.244` · NAIP-v1 `0.455` · SciJudge `-2.424` · DGC-BERT `0.789`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `6.0` Reject (S/P/C 2.75/3.0/2.5) · 14B Fast `5.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [axisofordinary/6444](https://t.me/axisofordinary/6444), [axisofordinary/6417](https://t.me/axisofordinary/6417)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2405.20233.md#weaknesses): The paper lacks a theoretical analysis of the proposed method. It would be helpful to have a theoretical explanation of why the method works and under what conditions it is effective. - The paper only considers a limited set of tasks and datasets. It would be helpful to see if the method works on a wider range of tasks and datasets.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2405.20233.md#weaknesses): While this paper presents a compelling approach to accelerating grokking, several weaknesses warrant careful consideration. First, the paper lacks a detailed analysis of the computational overhead introduced by the Grokfast algorithm, particularly concerning the memory requirements of the moving average (MA) filter.…

<a id="arxiv-2405.18392"></a>
### Scaling Laws and Compute-Optimal Training Beyond Fixed Training Durations

`arxiv:2405.18392` · Data, training, optimization · 2024-05-28

- final **+0.24** (conf 1.00, pct 71) · impact +0.06 · KEEP
- mean rating (1–10): **5.9** · accept votes **5/7** · percentile rank_avg 50.8 (100=best) · rank in year 22.0 (1=best)
- NAIPv2 `1.571` · NAIP-v1 `0.550` · SciJudge `0.148` · DGC-BERT `0.653`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.8` Reject · 7B Fast `5.8` Accept (S/P/C 2.75/3.0/2.5) · 14B Fast `6.8` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [fminxyz/26](https://t.me/fminxyz/26)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2405.18392.md#weaknesses): 1. The paper does not provide a thorough theoretical analysis of the proposed approach. It would be helpful to understand the underlying reasons for the effectiveness of the constant learning rate schedule with a cooldown period. 2.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2405.18392.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, the paper's central claim that cosine schedules are a primary obstacle in scaling research, while valid, may be overstated.…

<a id="arxiv-2405.16684"></a>
### gzip Predicts Data-dependent Scaling Laws

`arxiv:2405.16684` · Data, training, optimization · 2024-05-26

- final **-0.04** (conf 1.00, pct 32) · impact -0.80 · WATCH
- mean rating (1–10): **5.2** · accept votes **3/7** · percentile rank_avg 40.2 (100=best) · rank in year 32.0 (1=best)
- NAIPv2 `-0.097` · NAIP-v1 `0.392` · SciJudge `-0.504` · DGC-BERT `0.855`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.8` Reject · 7B Fast `4.8` Reject (S/P/C 2.25/2.5/2.5) · 14B Fast `4.2` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/6364](https://t.me/axisofordinary/6364)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2405.16684.md#weaknesses): The paper only considers a synthetic dataset generated by PCFG, which is not very realistic. - The paper does not provide any theoretical analysis or justification for the proposed data-dependent scaling law. - The paper does not evaluate the proposed scaling law on real-world datasets or real-world applications.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2405.16684.md#weaknesses): While I appreciate the novel approach of this paper, I have identified several weaknesses that warrant careful consideration. First, the paper's reliance on synthetic data generated from PCFGs raises concerns about the generalizability of its findings to real-world language.…

<a id="arxiv-2405.15682"></a>
### The Road Less Scheduled

`arxiv:2405.15682` · Data, training, optimization · 2024-05-24

- final **+0.34** (conf 1.00, pct 83) · impact +0.33 · KEEP
- mean rating (1–10): **5.8** · accept votes **5/7** · percentile rank_avg 60.0 (100=best) · rank in year 7.0 (1=best)
- NAIPv2 `-0.572` · NAIP-v1 `0.472` · SciJudge `3.083` · DGC-BERT `0.912`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `8.0` Accept · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/2.67) · 14B Fast `5.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2405.15682.md#weaknesses): The paper only considers convex problems and does not provide any theoretical results for non-convex problems. - The method requires the stopping time T to be known or set in advance, which may not always be possible in practice. - The method requires the use of a new hyperparameter $\beta$ which may require additional tuning.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2405.15682.md#weaknesses): section, there are some important limitations that need to be addressed.

<a id="arxiv-2403.05175"></a>
### Continual Learning and Catastrophic Forgetting

`arxiv:2403.05175` · Data, training, optimization · 2024-03-08

- final **-0.27** (conf 1.00, pct 15) · impact -1.11 · DROP
- mean rating (1–10): **5.6** · accept votes **2/7** · percentile rank_avg 23.9 (100=best) · rank in year 44.0 (1=best)
- NAIPv2 `-3.904` · NAIP-v1 `0.467` · SciJudge `-4.599` · DGC-BERT `0.018`
- CycleReviewer 8B `5.2` Reject · 70B `` 
- DeepReviewer 7B Std `3.0` Reject · 7B Fast `5.0` Reject (S/P/C None/None/None) · 14B Fast `5.8` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/4.0/2.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2403.05175.md#weaknesses): The chapter does not provide a lot of new insights. The authors do not present any new results or new approaches. The chapter is mostly a summary of the existing literature. - The chapter does not provide a clear conclusion or future directions for the field of continual learning.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2403.05175.md#weaknesses): of individual methods, a thorough discussion of the trade-offs between different approaches, and an exploration of the connections to meta-learning and related fields. Additionally, the paper could benefit from a more in-depth analysis of the underlying reasons for catastrophic forgetting and a clearer articulation of its unique contributions to the field.

<a id="arxiv-2402.02342"></a>
### MetaOptimize: A Framework for Optimizing Step Sizes and Other Meta-parameters

`arxiv:2402.02342` · Data, training, optimization · 2024-02-04

- final **-0.21** (conf 1.00, pct 19) · impact -1.37 · DROP
- mean rating (1–10): **5.4** · accept votes **3/7** · percentile rank_avg 33.7 (100=best) · rank in year 42.0 (1=best)
- NAIPv2 `-1.805` · NAIP-v1 `0.266` · SciJudge `-2.145` · DGC-BERT `0.945`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.8` Reject · 7B Fast `4.2` Reject (S/P/C 2.5/2.25/2.25) · 14B Fast `5.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/2.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2402.02342.md#weaknesses): The paper does not provide a comprehensive comparison with existing methods for optimizing meta-parameters. - The paper does not provide a detailed analysis of the computational complexity of the proposed framework. - The paper does not provide a detailed analysis of the performance of the proposed framework on a wide range of machine learning tasks.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2402.02342.md#weaknesses): After a thorough examination of the paper, I've identified several key weaknesses that significantly impact its overall contribution. Firstly, the paper's introduction lacks a comprehensive overview of the existing literature on learning step sizes.…

<a id="arxiv-2401.17401"></a>
### Step-size Optimization for Continual Learning

`arxiv:2401.17401` · Data, training, optimization · 2024-01-30

- final **-0.68** (conf 0.91, pct 2) · impact -2.26 · DROP · salvage dr7bf
- mean rating (1–10): **3.4** · accept votes **1/6** · percentile rank_avg 13.0 (100=best) · rank in year 48.0 (1=best)
- NAIPv2 `-3.381` · NAIP-v1 `0.206` · SciJudge `-6.733` · DGC-BERT `0.502`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast ``  (S/P/C 2.67/2.33/2.0) · 14B Fast `3.0` Reject
- OpenReviewer `3.0` Reject (S/P/C 2.0/2.0/2.0) · SEA-E `3.0` Reject
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2401.17401.md#weaknesses): The paper does not provide any new results or insights that are not already available in the literature. The authors do not provide any new experiments or analysis that demonstrate the effectiveness of their approach.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2401.17401.md#weaknesses): While the paper presents a compelling argument, I have identified several weaknesses that significantly limit its impact. First, the paper's experimental validation is limited to simple, synthetic problems. While these problems effectively illustrate the core concepts, they do not reflect the complexities of real-world continual learning scenarios.…

<a id="arxiv-2312.17742"></a>
### Learning Vision from Models Rivals Learning Vision from Data

`arxiv:2312.17742` · Data, training, optimization · 2023-12-28

- final **+0.17** (conf 0.95, pct 61) · impact +0.13 · WATCH
- mean rating (1–10): **5.8** · accept votes **3/7** · percentile rank_avg 50.9 (100=best) · rank in year 23.0 (1=best)
- NAIPv2 `-1.154` · NAIP-v1 `0.652` · SciJudge `-0.232` · DGC-BERT `0.916`
- CycleReviewer 8B `4.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.0` Reject · 7B Fast `6.0` Reject (S/P/C 3.0/3.0/2.5) · 14B Fast `7.0` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [axisofordinary/5918](https://t.me/axisofordinary/5918)
- Weaknesses:
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2312.17742.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further consideration. First, while the paper demonstrates strong performance on image classification and semantic segmentation, it lacks a thorough evaluation on object detection tasks.…
  - [DR-7B Fast](reviews/deepreviewer-7b-fast/arxiv_2312.17742.md#weaknesses): of the proposed approach. The paper is well-written and easy to follow, and the authors have provided sufficient details about their methodology and experimental setup. The inclusion of a comparison with DINO v2 is also a strength, as it provides a direct comparison with a state-of-the-art method.…

<a id="arxiv-2312.10549"></a>
### Catastrophic Forgetting in Deep Learning: A Comprehensive Taxonomy

`arxiv:2312.10549` · Data, training, optimization · 2023-12-16

- final **-0.66** (conf 1.00, pct 2) · impact -0.09 · DROP
- mean rating (1–10): **3.3** · accept votes **0/7** · percentile rank_avg 16.4 (100=best) · rank in year 49.0 (1=best)
- NAIPv2 `-3.830` · NAIP-v1 `0.671` · SciJudge `-3.152` · DGC-BERT `0.045`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `4.5` Reject (S/P/C 2.75/2.75/2.0) · 14B Fast `3.0` Reject
- OpenReviewer `3.0` Reject (S/P/C 2.0/2.0/2.0) · SEA-E `3.0` Reject
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2312.10549.md#weaknesses): of each category and provide a discussion of the current state of the field.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2312.10549.md#weaknesses): of each approach. The paper aims to offer a structured overview of the field, identify research gaps, and provide insights into the most suitable application scenarios for each technique.…

<a id="arxiv-2307.06440"></a>
### No Train No Gain: Revisiting Efficient Training Algorithms For Transformer-based Language Models

`arxiv:2307.06440` · Data, training, optimization · 2023-07-12

- final **+0.00** (conf 1.00, pct 36) · impact -0.82 · WATCH
- mean rating (1–10): **4.8** · accept votes **3/7** · percentile rank_avg 37.0 (100=best) · rank in year 42.0 (1=best)
- NAIPv2 `0.661` · NAIP-v1 `0.517` · SciJudge `-3.309` · DGC-BERT `0.796`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.2` Reject · 7B Fast `5.2` Reject (S/P/C 2.5/3.0/2.5) · 14B Fast `6.8` Accept
- OpenReviewer `3.0` Reject (S/P/C 2.0/2.0/1.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2307.06440.md#weaknesses): The paper does not provide any significant contribution. The authors evaluate a number of methods that aim to speed up training of transformer-based language models and find that they do not improve over the baseline models. The paper does not propose any new methods for speeding up training of transformer-based language models.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2307.06440.md#weaknesses): While this paper makes several valuable contributions, I have identified some weaknesses that warrant further discussion. Firstly, the paper's experimental scope, while comprehensive in some respects, is limited in others. Specifically, the authors focus on BERT and T5 models, which, while widely used, do not represent the full spectrum of modern architectures.…

<a id="doi-10.1038-s41586-024-07711-7"></a>
### Loss of plasticity in deep continual learning

`doi:10.1038/s41586-024-07711-7` · Data, training, optimization · 2024-08-21

- final **+0.36** (conf 1.00, pct 84) · impact -0.82 · KEEP
- mean rating (1–10): **6.2** · accept votes **5/7** · percentile rank_avg 50.6 (100=best) · rank in year 23.0 (1=best)
- NAIPv2 `-2.879` · NAIP-v1 `0.428` · SciJudge `-1.859` · DGC-BERT `0.407`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.8` Accept · 7B Fast `7.0` Accept (S/P/C 3.0/3.25/3.25) · 14B Fast `6.8` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `8.0` Accept
- Telegram: [knowledge_accumulator/323](https://t.me/knowledge_accumulator/323), [AGI_and_RL/847](https://t.me/AGI_and_RL/847)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/doi_10.1038_s41586-024-07711-7.md#weaknesses): The main weakness of the paper is the lack of theoretical analysis. The authors do not provide any theoretical analysis of the proposed algorithm or the loss of plasticity phenomenon. While the experiments are extensive, they do not provide any insights into why the proposed algorithm works or why the loss of plasticity occurs.…
  - [DR-14B Fast](reviews/deepreviewer-14b/doi_10.1038_s41586-024-07711-7.md#weaknesses): While this paper makes a valuable contribution to the field of continual learning, several weaknesses warrant careful consideration. First, the paper's framing of plasticity loss as a novel problem is somewhat misleading.…

<a id="arxiv-2305.14342"></a>
### Sophia: A Scalable Stochastic Second-order Optimizer for Language Model Pre-training

`arxiv:2305.14342` · Data, training, optimization · 2023-05-23

- final **+0.04** (conf 1.00, pct 43) · impact +0.71 · WATCH
- mean rating (1–10): **5.8** · accept votes **4/7** · percentile rank_avg 53.8 (100=best) · rank in year 18.0 (1=best)
- NAIPv2 `-1.202` · NAIP-v1 `0.658` · SciJudge `2.112` · DGC-BERT `0.770`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `6.2` Reject (S/P/C 2.75/2.75/2.5) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [ai_newz/1954](https://t.me/ai_newz/1954), [nn_for_science/1533](https://t.me/nn_for_science/1533), [data_secrets/1518](https://t.me/data_secrets/1518)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2305.14342.md#weaknesses): The theoretical analysis is not sufficient. The theoretical results are only for convex functions, which is not the case for LLMs. - The proposed method is not compared with other second-order methods.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2305.14342.md#weaknesses): While the paper presents a promising new optimization algorithm, several weaknesses warrant careful consideration. A primary concern is the limited scope of the empirical evaluation. The paper focuses exclusively on language modeling tasks using GPT models, with sizes ranging from 125 million to 1.5 billion parameters.…

<a id="arxiv-2302.06675"></a>
### Symbolic Discovery of Optimization Algorithms

`arxiv:2302.06675` · Data, training, optimization · 2023-02-13

- final **+0.42** (conf 1.00, pct 89) · impact +1.97 · KEEP
- mean rating (1–10): **6.5** · accept votes **5/7** · percentile rank_avg 74.5 (100=best) · rank in year 1.0 (1=best)
- NAIPv2 `-0.872` · NAIP-v1 `0.779` · SciJudge `3.932` · DGC-BERT `0.449`
- CycleReviewer 8B `6.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `7.0` Accept (S/P/C 3.0/3.0/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [lovedeathtransformers/5426](https://t.me/lovedeathtransformers/5426), [knowledge_accumulator/139](https://t.me/knowledge_accumulator/139), [gonzo_ML/1674](https://t.me/gonzo_ML/1674), [axisofordinary/4403](https://t.me/axisofordinary/4403), [tech_priestess/1159](https://t.me/tech_priestess/1159), [derplearning/2341](https://t.me/derplearning/2341), [j_links/6478](https://t.me/j_links/6478)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2302.06675.md#weaknesses): The paper does not provide a detailed analysis of the discovered Lion algorithm, such as its convergence properties and theoretical guarantees. - The paper does not compare the proposed method with other existing approaches to discovering optimization algorithms, such as reinforcement learning-based methods.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2302.06675.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, while the paper introduces the concept of an infinite and sparse search space, it lacks a detailed analysis of the search space's structure and its impact on the optimization process.…

<a id="arxiv-2212.14034"></a>
### Cramming: Training a Language Model on a Single GPU in One Day

`arxiv:2212.14034` · Data, training, optimization · 2022-12-28

- final **-0.08** (conf 1.00, pct 27) · impact -0.93 · WATCH
- mean rating (1–10): **5.8** · accept votes **3/7** · percentile rank_avg 37.7 (100=best) · rank in year 16.0 (1=best)
- NAIPv2 `-1.931` · NAIP-v1 `0.429` · SciJudge `-0.085` · DGC-BERT `0.737`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `5.5` Reject (S/P/C 2.75/3.0/2.5) · 14B Fast `5.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `7.0` Accept
- Telegram: [gonzo_ML/1217](https://t.me/gonzo_ML/1217), [j_links/6380](https://t.me/j_links/6380), [axisofordinary/4093](https://t.me/axisofordinary/4093), [scitator_ai/58](https://t.me/scitator_ai/58), [gonzo_ML/1179](https://t.me/gonzo_ML/1179)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2212.14034.md#weaknesses): 1. The novelty of this paper is limited. The authors mainly investigate the effects of various modifications to the training pipeline and find that most of the improvements are related to the scaling laws. This is not a surprising result and has been known in the literature.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2212.14034.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. First, while the paper presents a comprehensive ablation study, it lacks a clear narrative thread connecting the various experiments.…

<a id="arxiv-2210.10760"></a>
### Scaling Laws for Reward Model Overoptimization

`arxiv:2210.10760` · Data, training, optimization · 2022-10-19

- final **+0.22** (conf 1.00, pct 67) · impact -0.40 · KEEP
- mean rating (1–10): **6.1** · accept votes **5/7** · percentile rank_avg 51.9 (100=best) · rank in year 9.0 (1=best)
- NAIPv2 `-0.943` · NAIP-v1 `0.466` · SciJudge `1.191` · DGC-BERT `0.793`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `6.7` Accept (S/P/C 2.67/2.67/2.67) · 14B Fast `5.8` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [lovedeathtransformers/5297](https://t.me/lovedeathtransformers/5297), [dealerAI/8](https://t.me/dealerAI/8), [lovedeathtransformers/5427](https://t.me/lovedeathtransformers/5427)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2210.10760.md#weaknesses): 1. The paper does not provide a clear motivation for why the synthetic setup is a good proxy for real-world RLHF. The authors acknowledge this limitation in the paper, but do not provide any evidence that the synthetic setup is a good approximation of real-world RLHF. 2. The paper does not provide a clear explanation of how the results can be used to improve RLHF.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2210.10760.md#weaknesses): Despite its strengths, this paper has several limitations that warrant careful consideration. One of the most significant weaknesses is the heavy reliance on a synthetic data setup, which, while ingenious, raises concerns about the generalizability of the findings to real-world scenarios.…

<a id="arxiv-2110.09485"></a>
### Learning in High Dimension Always Amounts to Extrapolation

`arxiv:2110.09485` · Data, training, optimization · 2021-10-18

- final **-0.30** (conf 1.00, pct 12) · impact -0.45 · DROP
- mean rating (1–10): **3.9** · accept votes **1/7** · percentile rank_avg 27.1 (100=best) · rank in year 9.0 (1=best)
- NAIPv2 `-0.846` · NAIP-v1 `0.525` · SciJudge `0.222` · DGC-BERT `0.218`
- CycleReviewer 8B `1.0` Reject · 70B `` 
- DeepReviewer 7B Std `3.0` Reject · 7B Fast `5.5` Reject (S/P/C 3.0/2.75/2.5) · 14B Fast `6.0` Reject
- OpenReviewer `1.0` Reject (S/P/C 2.0/2.0/1.0) · SEA-E `6.0` Accept
- Telegram: [j_links/5300](https://t.me/j_links/5300)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2110.09485.md#weaknesses): The paper is not well written and the contribution is not clear. The authors do not provide any new theoretical results. They just collect some known results from convex geometry and use them to support their claim. The experiments are not well designed and the results are not clear. The authors do not provide any conclusion or recommendation.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2110.09485.md#weaknesses): While I find the paper's core argument compelling, there are several weaknesses that I believe need to be addressed. First, the paper's reliance on the convex hull as the sole definition of interpolation is a significant limitation.…

<a id="arxiv-2108.06325"></a>
### Continual Backprop: Stochastic Gradient Descent with Persistent Randomness

`arxiv:2108.06325` · Data, training, optimization · 2021-08-13

- final **-0.48** (conf 1.00, pct 7) · impact -1.87 · DROP
- mean rating (1–10): **3.7** · accept votes **0/7** · percentile rank_avg 15.5 (100=best) · rank in year 11.0 (1=best)
- NAIPv2 `-2.754` · NAIP-v1 `0.266` · SciJudge `-4.632` · DGC-BERT `0.349`
- CycleReviewer 8B `4.2` Reject · 70B `` 
- DeepReviewer 7B Std `5.8` Reject · 7B Fast `5.2` Reject (S/P/C 2.75/2.25/2.5) · 14B Fast `3.0` Reject
- OpenReviewer `3.0` Reject (S/P/C 3.0/2.0/2.0) · SEA-E `3.0` Reject
- Telegram: [nn_for_science/381](https://t.me/nn_for_science/381)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2108.06325.md#weaknesses): The paper is poorly written and the results are not convincing. The paper does not cite a large body of work on continual learning. The paper does not compare with other continual learning methods. The paper does not discuss the limitations of the proposed method.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2108.06325.md#weaknesses): Despite the strengths of this paper, I have identified several significant weaknesses that warrant careful consideration. First, the paper's framing of the problem as one of 'non-stationarity' rather than 'continual learning' is problematic.…

<a id="arxiv-2010.01412"></a>
### Sharpness-Aware Minimization for Efficiently Improving Generalization

`arxiv:2010.01412` · Data, training, optimization · 2020-10-03

- final **+0.58** (conf 1.00, pct 97) · impact +1.73 · KEEP
- mean rating (1–10): **6.0** · accept votes **5/7** · percentile rank_avg 68.1 (100=best) · rank in year 1.0 (1=best)
- NAIPv2 `1.366` · NAIP-v1 `0.811` · SciJudge `3.001` · DGC-BERT `0.925`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `7.0` Accept (S/P/C 3.25/3.25/3.0) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [j_links/4264](https://t.me/j_links/4264), [gonzo_ML/2001](https://t.me/gonzo_ML/2001), [lovedeathtransformers/6486](https://t.me/lovedeathtransformers/6486), [tech_priestess/1047](https://t.me/tech_priestess/1047)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2010.01412.md#weaknesses): The proposed method is not well motivated. The theorem in Section 2 does not provide a clear justification for why minimizing loss sharpness improves generalization. The connection between loss sharpness and generalization is not well established. - The proposed method is not novel. The idea of penalizing sharpness has been explored in previous work, such as (1,2,3).…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2010.01412.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further consideration. First, while the authors demonstrate the effectiveness of SAM on several datasets and architectures, the experimental evaluation is not as comprehensive as it could be.…

<a id="arxiv-2009.11848"></a>
### How Neural Networks Extrapolate: From Feedforward to Graph Neural Networks

`arxiv:2009.11848` · Data, training, optimization · 2020-09-24

- final **+0.24** (conf 1.00, pct 71) · impact -0.55 · KEEP
- mean rating (1–10): **6.1** · accept votes **5/7** · percentile rank_avg 50.5 (100=best) · rank in year 8.0 (1=best)
- NAIPv2 `-0.141` · NAIP-v1 `0.540` · SciJudge `-1.128` · DGC-BERT `0.418`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `5.7` Accept (S/P/C 2.67/2.67/2.33) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [j_links/4183](https://t.me/j_links/4183)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2009.11848.md#weaknesses): 1. The paper studies the extrapolation ability of neural networks, but the results are only for ReLU MLPs in the NTK regime. The results are not generalizable to other types of neural networks.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2009.11848.md#weaknesses): Despite its strengths, the paper has several verified limitations that warrant discussion. One of the primary concerns is the strong assumptions made in the theoretical results, particularly in Theorem 2. The assumption that the training data contains an orthogonal basis, as stated in Lemma 1, is highly artificial and unlikely to hold in real-world scenarios.…

<a id="arxiv-2009.11243"></a>
### Tasks, stability, architecture, and compute: Training more effective learned optimizers, and using them to train themselves

`arxiv:2009.11243` · Data, training, optimization · 2020-09-23

- final **+0.51** (conf 1.00, pct 96) · impact +0.04 · KEEP
- mean rating (1–10): **6.7** · accept votes **5/7** · percentile rank_avg 58.9 (100=best) · rank in year 5.0 (1=best)
- NAIPv2 `-1.413` · NAIP-v1 `0.625` · SciJudge `0.236` · DGC-BERT `0.619`
- CycleReviewer 8B `5.8` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `8.0` Accept (S/P/C 3.67/3.67/3.67) · 14B Fast `5.8` Reject
- OpenReviewer `8.0` Accept (S/P/C 3.0/4.0/4.0) · SEA-E `6.0` Accept
- Telegram: [knowledge_accumulator/110](https://t.me/knowledge_accumulator/110), [j_links/4121](https://t.me/j_links/4121), [gonzo_ML/372](https://t.me/gonzo_ML/372)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2009.11243.md#weaknesses): The main weakness of the paper is that it does not provide a clear explanation of why the proposed optimizer works better than previous learned optimizers. The authors do not provide any analysis of the learned optimizer's behavior, such as the types of inductive biases it learns or how it adapts to different tasks.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2009.11243.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. First, the paper lacks a detailed analysis of the computational overhead associated with the proposed learned optimizer.…

<a id="arxiv-2001.08361"></a>
### Scaling Laws for Neural Language Models

`arxiv:2001.08361` · Data, training, optimization · 2020-01-23

- final **+0.39** (conf 1.00, pct 87) · impact +1.87 · KEEP
- mean rating (1–10): **5.6** · accept votes **4/7** · percentile rank_avg 66.1 (100=best) · rank in year 2.0 (1=best)
- NAIPv2 `0.012` · NAIP-v1 `0.787` · SciJudge `3.608` · DGC-BERT `0.896`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.0` Reject · 7B Fast `6.0` Reject (S/P/C 2.67/3.33/2.33) · 14B Fast `4.0` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [gonzo_ML/1856](https://t.me/gonzo_ML/1856), [dlinnlp/736](https://t.me/dlinnlp/736), [data_secrets/5534](https://t.me/data_secrets/5534), [gonzo_ML/1216](https://t.me/gonzo_ML/1216), [AGI_and_RL/612](https://t.me/AGI_and_RL/612), [rybolos_channel/316](https://t.me/rybolos_channel/316), [gonzo_ML/4730](https://t.me/gonzo_ML/4730), [lovedeathtransformers/5878](https://t.me/lovedeathtransformers/5878)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2001.08361.md#weaknesses): The paper does not provide any theoretical analysis of the scaling laws.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2001.08361.md#weaknesses): While this paper presents a compelling empirical study of scaling laws, several weaknesses warrant careful consideration. First, the paper's primary focus on cross-entropy loss, while a standard metric for language modeling, limits the generalizability of the findings.…

<a id="arxiv-1904.00962"></a>
### Large Batch Optimization for Deep Learning: Training BERT in 76 minutes

`arxiv:1904.00962` · Data, training, optimization · 2019-04-01

- final **+0.48** (conf 1.00, pct 94) · impact +0.58 · KEEP
- mean rating (1–10): **5.8** · accept votes **4/7** · percentile rank_avg 62.5 (100=best) · rank in year 1.0 (1=best)
- NAIPv2 `0.668` · NAIP-v1 `0.668` · SciJudge `1.685` · DGC-BERT `0.913`
- CycleReviewer 8B `5.2` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `7.0` Accept (S/P/C 3.25/3.0/2.75) · 14B Fast `6.0` Reject
- OpenReviewer `5.0` Reject (S/P/C 2.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [j_links/2316](https://t.me/j_links/2316)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_1904.00962.md#weaknesses): 1. The paper is not well-organized. The authors present the convergence analysis of Lamb and Lars in Section 3, but do not provide any experimental results in this section. Instead, the experimental results are presented in Section 4. This makes it difficult to understand the significance of the convergence analysis.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_1904.00962.md#weaknesses): While the paper presents a novel and promising optimization algorithm, several weaknesses warrant careful consideration. Firstly, the paper's claim of being the "first" to achieve certain results on BERT training is inaccurate. As pointed out by Reviewer 1, prior work has already demonstrated training BERT within a similar timeframe, albeit on different hardware.…

<a id="arxiv-1803.03635"></a>
### The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks

`arxiv:1803.03635` · Data, training, optimization · 2018-03-09

- final **+0.16** (conf 1.00, pct 60) · impact +0.67 · WATCH
- mean rating (1–10): **5.7** · accept votes **3/7** · percentile rank_avg 46.1 (100=best) · rank in year 2.0 (1=best)
- NAIPv2 `-1.059` · NAIP-v1 `0.703` · SciJudge `1.989` · DGC-BERT `0.135`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `5.0` Reject (S/P/C 2.5/2.5/2.5) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [nn_for_science/2452](https://t.me/nn_for_science/2452), [gonzo_ML/21](https://t.me/gonzo_ML/21), [partially_unsupervised/228](https://t.me/partially_unsupervised/228), [gonzo_ML/4350](https://t.me/gonzo_ML/4350), [gonzo_ML/196](https://t.me/gonzo_ML/196), [dlinnlp/956](https://t.me/dlinnlp/956), [gonzo_ML/884](https://t.me/gonzo_ML/884)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_1803.03635.md#weaknesses): 1. The paper only considers small datasets (MNIST and CIFAR-10), and the proposed method is not efficient to apply to large-scale datasets. It would be better to consider larger datasets and more efficient methods for finding winning tickets. 2. The paper only considers sparse pruning, and it would be better to consider other pruning methods such as structured pruning. 3.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_1803.03635.md#weaknesses): While the paper presents a compelling hypothesis and strong empirical evidence, several limitations warrant careful consideration. First, the paper's experimental scope is primarily limited to smaller datasets, specifically MNIST and CIFAR10.…

<a id="openreview-ry_WPG-A-"></a>
### On the Information Bottleneck Theory of Deep Learning (Saxe et al.)

`openreview:ry_WPG-A-` · Data, training, optimization · unknown

- final **-0.01** (conf 1.00, pct 34) · impact +0.02 · WATCH
- mean rating (1–10): **5.8** · accept votes **5/7** · percentile rank_avg 40.5 (100=best) · rank in year 6.0 (1=best)
- NAIPv2 `-1.558` · NAIP-v1 `0.431` · SciJudge `2.361` · DGC-BERT `0.465`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `3.0` Reject · 7B Fast `5.5` Accept (S/P/C 2.25/2.5/2.5) · 14B Fast `5.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [j_links/582](https://t.me/j_links/582), [neuroexistencialism/3399](https://t.me/neuroexistencialism/3399)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/openreview_ry_WPG-A-.md#weaknesses): The paper claims that the information bottleneck theory of deep learning is not supported by the experimental results. However, the experiments are limited to small networks and simple datasets. The authors do not provide a comprehensive analysis of the theory and its limitations.…
  - [DR-14B Fast](reviews/deepreviewer-14b/openreview_ry_WPG-A-.md#weaknesses): While this paper presents a compelling critique of the information bottleneck theory as applied to deep learning, there are several limitations that warrant careful consideration. Firstly, the paper's primary focus on the specific claims of Shwartz-Ziv and Tishby (2017) limits its scope in addressing the broader information bottleneck principle.…

<a id="arxiv-1708.07120"></a>
### Super-Convergence: Very Fast Training of Neural Networks Using Large Learning Rates

`arxiv:1708.07120` · Data, training, optimization · 2017-08-23

- final **-0.01** (conf 1.00, pct 35) · impact -0.35 · WATCH
- mean rating (1–10): **4.7** · accept votes **3/7** · percentile rank_avg 38.0 (100=best) · rank in year 6.0 (1=best)
- NAIPv2 `-0.206` · NAIP-v1 `0.528` · SciJudge `0.748` · DGC-BERT `0.854`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.2` Reject · 7B Fast `5.8` Reject (S/P/C 2.5/2.5/2.5) · 14B Fast `6.7` Accept
- OpenReviewer `3.0` Reject (S/P/C 2.0/1.0/2.0) · SEA-E `5.0` Accept
- Telegram: [j_links/420](https://t.me/j_links/420)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_1708.07120.md#weaknesses): The paper lacks a thorough theoretical analysis of the proposed method. The authors provide some insights into the effect of large learning rates and the balance of regularization, but a more rigorous theoretical framework would strengthen the paper. The experimental results are promising, but more comprehensive experiments and comparisons with other state-of-the-art methods would be beneficial.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_1708.07120.md#weaknesses): Despite the promising results, this paper has several weaknesses that warrant careful consideration. A significant limitation is the lack of a comprehensive comparison with other state-of-the-art training techniques.…

<a id="arxiv-1708.02072"></a>
### Measuring Catastrophic Forgetting in Neural Networks

`arxiv:1708.02072` · Data, training, optimization · 2017-08-07

- final **-0.49** (conf 1.00, pct 6) · impact -0.43 · DROP
- mean rating (1–10): **4.0** · accept votes **2/7** · percentile rank_avg 22.9 (100=best) · rank in year 7.0 (1=best)
- NAIPv2 `-2.916` · NAIP-v1 `0.558` · SciJudge `-0.195` · DGC-BERT `0.521`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.2` Reject · 7B Fast `4.8` Reject (S/P/C 2.25/2.75/2.25) · 14B Fast `3.5` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `3.0` Reject
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_1708.02072.md#weaknesses): The paper does not provide any new insights or contributions to the field. - The paper only provides a review of existing methods and does not propose any new methods to mitigate catastrophic forgetting. - The paper does not provide any experimental results on new datasets or benchmarks.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_1708.02072.md#weaknesses): of each mitigation strategy. Furthermore, the paper's clear and concise writing style makes it accessible to a broad audience. The authors provide sufficient detail about their methodology and experimental setup, which enhances the reproducibility of their work.…

<a id="doi-10.1073-pnas.1611835114"></a>
### Overcoming catastrophic forgetting in neural networks

`doi:10.1073/pnas.1611835114` · Data, training, optimization · 2017-03-14

- final **+0.03** (conf 1.00, pct 41) · impact -0.13 · WATCH
- mean rating (1–10): **5.8** · accept votes **4/7** · percentile rank_avg 39.3 (100=best) · rank in year 5.0 (1=best)
- NAIPv2 `-4.164` · NAIP-v1 `0.542` · SciJudge `1.496` · DGC-BERT `0.360`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `6.0` Accept (S/P/C 3.0/2.75/2.75) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/doi_10.1073_pnas.1611835114.md#weaknesses): The main weakness of the paper is that the method is not evaluated on a wide range of tasks and datasets. The authors only evaluate their method on MNIST and Atari, which are relatively simple tasks. It would be good to see how the method performs on more complex tasks, such as image classification on CIFAR-10 or CIFAR-100, or language modeling on text datasets.…
  - [DR-14B Fast](reviews/deepreviewer-14b/doi_10.1073_pnas.1611835114.md#weaknesses): While the paper presents a compelling approach to continual learning, several weaknesses warrant careful consideration. First, the paper lacks a thorough discussion of the limitations of the EWC method.…

<a id="arxiv-1506.01186"></a>
### Cyclical Learning Rates for Training Neural Networks

`arxiv:1506.01186` · Data, training, optimization · 2015-06-03

- final **-0.40** (conf 1.00, pct 9) · impact -0.25 · DROP
- mean rating (1–10): **4.4** · accept votes **1/7** · percentile rank_avg 20.3 (100=best) · rank in year 4.0 (1=best)
- NAIPv2 `-3.008` · NAIP-v1 `0.664` · SciJudge `-1.382` · DGC-BERT `0.304`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `2.5` Reject · 7B Fast `5.2` Reject (S/P/C 2.5/2.75/2.25) · 14B Fast `4.8` Reject
- OpenReviewer `3.0` Reject (S/P/C 2.0/1.0/1.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_1506.01186.md#weaknesses): 1. The authors only provide experimental results on a limited number of datasets and architectures. It would be better if the authors can provide more experimental results on other datasets and architectures. 2. The authors only provide results on classification tasks. It would be better if the authors can provide results on other tasks such as regression and generative tasks. 3.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_1506.01186.md#weaknesses): While the paper introduces a novel and promising approach to learning rate scheduling, several significant weaknesses limit its overall impact and generalizability. The most prominent concern is the lack of a rigorous theoretical analysis of why CLR works.…

<a id="arxiv-2606.02572"></a>
### VISReg: Variance-Invariance-Sketching Regularization for JEPA training

`arxiv:2606.02572` · Self-supervised learning and vision · 2026-06-01

- final **+0.34** (conf 1.00, pct 82) · impact -0.22 · KEEP
- mean rating (1–10): **6.5** · accept votes **6/7** · percentile rank_avg 62.6 (100=best) · rank in year 24.0 (1=best)
- NAIPv2 `1.062` · NAIP-v1 `0.622` · SciJudge `-2.289` · DGC-BERT `0.537`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `8.0` Accept (S/P/C 3.25/3.25/3.25) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [gonzo_ML/5832](https://t.me/gonzo_ML/5832)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2606.02572.md#weaknesses): The paper does not provide a theoretical analysis of the proposed method. While the authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, it would be helpful to have a more rigorous theoretical analysis of the proposed method. - The paper does not compare with some recent SOTA methods, such as LpJEPA (1) and KerJEPA (2).…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2606.02572.md#weaknesses): section. Overall, the paper presents a well-motivated and technically sound approach to self-supervised learning, with a focus on addressing the limitations of existing regularization techniques.

<a id="arxiv-2605.26379"></a>
### When Does LeJEPA Learn a World Model?

`arxiv:2605.26379` · Self-supervised learning and vision · 2026-05-25

- final **+0.62** (conf 1.00, pct 99) · impact -0.66 · KEEP
- mean rating (1–10): **6.7** · accept votes **6/7** · percentile rank_avg 68.3 (100=best) · rank in year 11.0 (1=best)
- NAIPv2 `0.844` · NAIP-v1 `0.475` · SciJudge `-1.515` · DGC-BERT `0.929`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.2` Accept · 7B Fast `6.5` Accept (S/P/C 3.0/3.0/3.0) · 14B Fast `8.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `8.0` Accept
- Telegram: [gonzo_ML/5489](https://t.me/gonzo_ML/5489)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2605.26379.md#weaknesses): The paper focuses on a specific type of self-supervised learning, LeJEPA, and does not consider other types of self-supervised learning. - The paper assumes that the latent variables are Gaussian, which may not be realistic in many cases. - The paper does not provide a clear explanation of how the theoretical results can be applied in practice.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2605.26379.md#weaknesses): While the paper presents a strong theoretical contribution, several limitations warrant careful consideration. First, the theoretical framework relies on several strong assumptions about the world, which may not hold in many real-world scenarios.…

<a id="arxiv-2604.09168"></a>
### ELT: Elastic Looped Transformers for Visual Generation

`arxiv:2604.09168` · Self-supervised learning and vision · 2026-04-10

- final **+0.05** (conf 1.00, pct 44) · impact +0.01 · WATCH
- mean rating (1–10): **6.0** · accept votes **4/7** · percentile rank_avg 53.2 (100=best) · rank in year 47.0 (1=best)
- NAIPv2 `-1.056` · NAIP-v1 `0.587` · SciJudge `0.389` · DGC-BERT `0.404`
- CycleReviewer 8B `4.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.8` Reject · 7B Fast `6.7` Accept (S/P/C 3.0/3.0/2.67) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [gonzo_ML/5303](https://t.me/gonzo_ML/5303)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2604.09168.md#weaknesses): 1. The novelty of this paper is limited. The idea of using a recurrent transformer architecture for visual generation is not new. The proposed method is a combination of existing techniques, such as looping and distillation. 2. The experiments are not convincing. The authors only compare their method with MaskGIT and MAGVIT, which are not the state-of-the-art methods in visual generation.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2604.09168.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. Firstly, while the paper introduces the concept of a 'composite block,' the explanation of how this block is implemented and how the parameters are shared across loops could be more detailed.…

<a id="arxiv-2511.08544"></a>
### LeJEPA: Provable and Scalable Self-Supervised Learning Without the Heuristics

`arxiv:2511.08544` · Self-supervised learning and vision · 2025-11-11

- final **+0.33** (conf 1.00, pct 81) · impact +0.57 · KEEP
- mean rating (1–10): **6.0** · accept votes **6/7** · percentile rank_avg 61.7 (100=best) · rank in year 26.0 (1=best)
- NAIPv2 `1.300` · NAIP-v1 `0.690` · SciJudge `0.329` · DGC-BERT `0.684`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `5.8` Accept (S/P/C 3.0/2.75/2.75) · 14B Fast `7.0` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [data_secrets/8254](https://t.me/data_secrets/8254), [gonzo_ML/4212](https://t.me/gonzo_ML/4212), [axisofordinary/7894](https://t.me/axisofordinary/7894)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2511.08544.md#weaknesses): The proposed method is not novel, as it combines two existing methods: JEPA and SIGReg. The authors should provide a more detailed discussion on how their method is different from existing methods. - The theoretical analysis is not convincing. The authors should provide more rigorous proofs and analysis to support their claims. - The experimental results are not convincing.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2511.08544.md#weaknesses): Despite the paper's strengths, there are several verified limitations that need to be addressed. One of the most significant concerns is the lack of a direct comparison with DINO on ImageNet using the standard linear probing evaluation protocol. The paper primarily uses full fine-tuning results on ImageNet, which is not the standard benchmark for evaluating self-supervised learning methods.…

<a id="arxiv-2501.05441"></a>
### The GAN is dead; long live the GAN! A Modern GAN Baseline

`arxiv:2501.05441` · Self-supervised learning and vision · 2025-01-09

- final **+0.03** (conf 1.00, pct 41) · impact +1.17 · WATCH
- mean rating (1–10): **5.8** · accept votes **5/7** · percentile rank_avg 58.5 (100=best) · rank in year 39.0 (1=best)
- NAIPv2 `0.142` · NAIP-v1 `0.849` · SciJudge `-0.512` · DGC-BERT `0.967`
- CycleReviewer 8B `5.2` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `5.2` Reject (S/P/C 3.0/3.0/2.25) · 14B Fast `6.2` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [data_secrets/5891](https://t.me/data_secrets/5891)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2501.05441.md#weaknesses): 1. The novelty of the paper is limited. The proposed method is a combination of existing methods, and the only novelty is the choice of hyperparameters. 2. The paper does not provide a thorough analysis of the proposed method. For example, the authors do not provide an ablation study of the R1 and R2 regularization terms. 3.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2501.05441.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, while the authors present a theoretical analysis of the convergence properties of their proposed loss function, the analysis is limited to local convergence.…

<a id="arxiv-2310.04378"></a>
### Latent Consistency Models: Synthesizing High-Resolution Images with Few-Step Inference

`arxiv:2310.04378` · Self-supervised learning and vision · 2023-10-06

- final **+0.19** (conf 1.00, pct 64) · impact +1.46 · WATCH
- mean rating (1–10): **5.7** · accept votes **3/7** · percentile rank_avg 56.2 (100=best) · rank in year 15.0 (1=best)
- NAIPv2 `0.217` · NAIP-v1 `0.715` · SciJudge `3.875` · DGC-BERT `0.846`
- CycleReviewer 8B `5.8` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `5.2` Reject (S/P/C 2.75/2.75/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [lovedeathtransformers/6578](https://t.me/lovedeathtransformers/6578)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2310.04378.md#weaknesses): The proposed method is a direct extension of the consistency model to latent space. The novelty is limited. - The proposed method is not compared with the latest diffusion models, such as (1-3). - The proposed method is not compared with the latest consistency models, such as (4, 5). - The proposed method is only evaluated on LAION-5B-Aesthetics dataset.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2310.04378.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, while the paper claims to introduce a novel method, the core idea of applying consistency models in the latent space is not entirely new, as similar approaches have been explored in the context of video generation.…

<a id="arxiv-2309.15807"></a>
### Emu: Enhancing Image Generation Models Using Photogenic Needles in a Haystack

`arxiv:2309.15807` · Self-supervised learning and vision · 2023-09-27

- final **+0.19** (conf 1.00, pct 63) · impact -0.21 · WATCH
- mean rating (1–10): **6.2** · accept votes **4/7** · percentile rank_avg 53.7 (100=best) · rank in year 20.0 (1=best)
- NAIPv2 `-0.754` · NAIP-v1 `0.502` · SciJudge `1.167` · DGC-BERT `0.109`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `6.5` Reject (S/P/C 3.0/3.0/2.5) · 14B Fast `6.7` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [seeallochnaya/663](https://t.me/seeallochnaya/663), [lovedeathtransformers/9356](https://t.me/lovedeathtransformers/9356)
- Weaknesses:
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2309.15807.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, while the paper introduces the concept of 'aesthetic alignment,' it does not provide a formal definition of this term.…
  - [DR-7B Fast](reviews/deepreviewer-7b-fast/arxiv_2309.15807.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. First, the paper lacks a thorough comparison with other existing methods for improving the aesthetic quality of generated images.…

<a id="arxiv-2304.12210"></a>
### A Cookbook of Self-Supervised Learning

`arxiv:2304.12210` · Self-supervised learning and vision · 2023-04-24

- final **-0.57** (conf 1.00, pct 4) · impact +0.07 · DROP
- mean rating (1–10): **4.9** · accept votes **1/7** · percentile rank_avg 27.3 (100=best) · rank in year 46.0 (1=best)
- NAIPv2 `-2.777` · NAIP-v1 `0.688` · SciJudge `-0.908` · DGC-BERT `0.047`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.0` Reject · 7B Fast `5.5` Reject (S/P/C 3.0/3.0/2.25) · 14B Fast `3.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `5.0` Reject
- Telegram: [ai_newz/1874](https://t.me/ai_newz/1874), [data_secrets/4262](https://t.me/data_secrets/4262), [dl_stories/723](https://t.me/dl_stories/723), [dealerAI/129](https://t.me/dealerAI/129), [nn_for_science/1451](https://t.me/nn_for_science/1451), [data_secrets/1335](https://t.me/data_secrets/1335)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2304.12210.md#weaknesses): The paper is a survey paper that discusses the recent advances in self-supervised learning (SSL). The paper does not provide any new contributions or insights into the field of SSL. The paper is well-written and provides a comprehensive overview of the recent advances in SSL. However, the paper does not provide any new insights or contributions to the field of SSL.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2304.12210.md#weaknesses): Despite its ambitious goals, the paper suffers from several significant weaknesses that undermine its effectiveness as a comprehensive guide to self-supervised learning (SSL). First, the presentation is often unclear and difficult to follow, which is a major issue for a paper intended to be a practical guide for newcomers.…

<a id="arxiv-2304.09355"></a>
### To Compress or Not to Compress- Self-Supervised Learning and Information Theory: A Review

`arxiv:2304.09355` · Self-supervised learning and vision · 2023-04-19

- final **-0.41** (conf 0.91, pct 9) · impact -0.23 · DROP · salvage dr7bf
- mean rating (1–10): **4.5** · accept votes **1/6** · percentile rank_avg 24.1 (100=best) · rank in year 47.0 (1=best)
- NAIPv2 `-2.838` · NAIP-v1 `0.636` · SciJudge `-2.287` · DGC-BERT `0.108`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast ``  (S/P/C 2.25/2.5/2.5) · 14B Fast `4.0` Reject
- OpenReviewer `5.0` Reject (S/P/C 3.0/2.0/2.0) · SEA-E `6.0` Accept
- Telegram: [nn_for_science/1455](https://t.me/nn_for_science/1455)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2304.09355.md#weaknesses): The paper lacks a clear research question and does not provide any new insights or contributions to the field. The paper is a review of existing work and does not provide any new results or experiments. The paper is not well-organized and is difficult to follow. The authors do not provide any clear conclusions or recommendations for future research.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2304.09355.md#weaknesses): Despite its strengths, the paper has several significant limitations that need to be addressed. One major concern is the lack of a detailed discussion on the practical challenges of applying information theory to self-supervised learning.…

<a id="arxiv-2304.07193"></a>
### DINOv2: Learning Robust Visual Features without Supervision

`arxiv:2304.07193` · Self-supervised learning and vision · 2023-04-14

- final **+0.20** (conf 1.00, pct 65) · impact +2.01 · WATCH
- mean rating (1–10): **5.7** · accept votes **4/7** · percentile rank_avg 54.1 (100=best) · rank in year 17.0 (1=best)
- NAIPv2 `-2.252` · NAIP-v1 `0.729` · SciJudge `4.260` · DGC-BERT `0.380`
- CycleReviewer 8B `5.2` Reject · 70B `` 
- DeepReviewer 7B Std `7.0` Accept · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/2.5) · 14B Fast `6.0` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [ai_newz/1871](https://t.me/ai_newz/1871), [AI_DeepLearning/1031](https://t.me/AI_DeepLearning/1031), [j_links/6646](https://t.me/j_links/6646), [nn_for_science/1435](https://t.me/nn_for_science/1435)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2304.07193.md#weaknesses): The paper proposes a new dataset and training recipe, but the novelty is limited. The authors do not provide a detailed analysis of the proposed dataset and training recipe, and it is not clear how they differ from previous approaches.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2304.07193.md#weaknesses): While this paper presents significant contributions, several weaknesses warrant careful consideration. First, the paper's technical novelty is limited, as it primarily combines existing techniques rather than introducing fundamentally new self-supervised learning methods.…

<a id="arxiv-2304.05977"></a>
### ImageReward: Learning and Evaluating Human Preferences for Text-to-Image Generation

`arxiv:2304.05977` · Self-supervised learning and vision · 2023-04-12

- final **+0.43** (conf 1.00, pct 91) · impact +1.85 · KEEP
- mean rating (1–10): **6.0** · accept votes **5/7** · percentile rank_avg 64.9 (100=best) · rank in year 6.0 (1=best)
- NAIPv2 `1.893` · NAIP-v1 `0.827` · SciJudge `3.476` · DGC-BERT `0.405`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.0` Accept (S/P/C 2.75/3.0/2.75) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [axisofordinary/4834](https://t.me/axisofordinary/4834)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2304.05977.md#weaknesses): The authors only compared their method with a few existing methods, and it would be better if they could compare with more existing methods in the field. - The authors only tested their method on a small set of prompts, and it would be better if they could test their method on a larger set of prompts.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2304.05977.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further consideration. Firstly, the evaluation of ImageReward, as presented in Section 4.1, is not as robust as it could be.…

<a id="arxiv-2302.10174"></a>
### Towards Universal Fake Image Detectors that Generalize Across Generative Models

`arxiv:2302.10174` · Self-supervised learning and vision · 2023-02-20

- final **+0.04** (conf 1.00, pct 41) · impact +1.05 · WATCH
- mean rating (1–10): **6.4** · accept votes **4/7** · percentile rank_avg 56.2 (100=best) · rank in year 14.0 (1=best)
- NAIPv2 `-1.620` · NAIP-v1 `0.738` · SciJudge `1.942` · DGC-BERT `0.277`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `6.0` Accept (S/P/C 2.67/3.0/2.67) · 14B Fast `6.0` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [dl_stories/730](https://t.me/dl_stories/730)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2302.10174.md#weaknesses): 1. The paper lacks novelty. The authors use the pre-trained CLIP model to extract features and then use the nearest neighbor and linear probing methods to perform the classification task. These methods are commonly used in the field of image classification and have been widely studied.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2302.10174.md#weaknesses): While this paper presents a compelling approach to fake image detection, there are several weaknesses that warrant careful consideration. First, the paper lacks a detailed analysis of the computational cost associated with the proposed method, particularly the nearest neighbor approach.…

<a id="arxiv-2301.08243"></a>
### Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture

`arxiv:2301.08243` · Self-supervised learning and vision · 2023-01-19

- final **+0.18** (conf 1.00, pct 63) · impact +0.18 · WATCH
- mean rating (1–10): **6.0** · accept votes **4/7** · percentile rank_avg 50.8 (100=best) · rank in year 25.0 (1=best)
- NAIPv2 `-1.402` · NAIP-v1 `0.562` · SciJudge `1.804` · DGC-BERT `0.423`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Reject · 7B Fast `7.5` Accept (S/P/C 3.0/3.25/3.0) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [nn_for_science/1511](https://t.me/nn_for_science/1511), [dl_stories/671](https://t.me/dl_stories/671), [gonzo_ML/3501](https://t.me/gonzo_ML/3501), [j_links/6821](https://t.me/j_links/6821)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2301.08243.md#weaknesses): The paper lacks a strong theoretical foundation for the proposed method. While the authors provide some intuition for why the method works, there is no formal analysis or proof of its correctness or optimality. This makes it difficult to understand the underlying principles of the method and its limitations. - The paper does not provide a clear comparison to existing methods.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2301.08243.md#weaknesses): While I find the paper to be generally strong, there are several weaknesses that I believe need to be addressed. First, while the paper claims that I-JEPA learns semantic representations that do not require extensive fine-tuning on downstream tasks, the empirical evidence for this claim is not as robust as it could be.…

<a id="arxiv-2212.11565"></a>
### Tune-A-Video: One-Shot Tuning of Image Diffusion Models for Text-to-Video Generation

`arxiv:2212.11565` · Self-supervised learning and vision · 2022-12-22

- final **-0.25** (conf 1.00, pct 17) · impact +0.85 · WATCH
- mean rating (1–10): **5.0** · accept votes **3/7** · percentile rank_avg 41.3 (100=best) · rank in year 15.0 (1=best)
- NAIPv2 `-2.020` · NAIP-v1 `0.669` · SciJudge `2.860` · DGC-BERT `0.743`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `4.0` Reject (S/P/C 2.5/2.75/2.0) · 14B Fast `5.8` Reject
- OpenReviewer `5.0` Reject (S/P/C 2.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [monkeyinlaw/1044](https://t.me/monkeyinlaw/1044), [AI_DeepLearning/831](https://t.me/AI_DeepLearning/831), [derplearning/2267](https://t.me/derplearning/2267)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2212.11565.md#weaknesses): 1. The proposed method is based on the existing T2I model, and the proposed method is not very novel. 2. The proposed method is not very effective. For example, the video generation results in Fig. 7 are not good enough. 3. The proposed method is not very efficient. For example, the training time is 10 minutes for a single video.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2212.11565.md#weaknesses): While the paper presents a compelling approach to text-to-video generation, I have identified several weaknesses that warrant further discussion. Firstly, the paper's reliance on DDIM inversion for structure guidance, while effective, lacks a thorough analysis of its limitations.…

<a id="arxiv-2208.10442"></a>
### Image as a Foreign Language: BEiT Pretraining for All Vision and Vision-Language Tasks

`arxiv:2208.10442` · Self-supervised learning and vision · 2022-08-22

- final **+0.24** (conf 1.00, pct 70) · impact +2.16 · KEEP
- mean rating (1–10): **5.5** · accept votes **5/7** · percentile rank_avg 54.2 (100=best) · rank in year 8.0 (1=best)
- NAIPv2 `-0.626` · NAIP-v1 `0.862` · SciJudge `3.291` · DGC-BERT `0.574`
- CycleReviewer 8B `4.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/3.0) · 14B Fast `6.5` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [j_links/6062](https://t.me/j_links/6062), [boris_again/1163](https://t.me/boris_again/1163), [abstractDL/157](https://t.me/abstractDL/157), [axisofordinary/3146](https://t.me/axisofordinary/3146), [cats_shredinger/25](https://t.me/cats_shredinger/25)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2208.10442.md#weaknesses): 1. The novelty of the paper is limited. The proposed method is a straightforward combination of existing methods, i.e., BEiT and Multiway Transformer. 2. The paper does not provide any analysis of the model's performance on low-resource languages, which is an important aspect of a multimodal foundation model. 3.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2208.10442.md#weaknesses): While the paper presents a compelling case for BEiT-3, several weaknesses warrant careful consideration. Firstly, the paper's claim of introducing a 'general-purpose multimodal foundation model' is somewhat overstated, as the experiments are limited to vision and language tasks.…

<a id="openreview-BZ5a1r-kVsf"></a>
### A Path Towards Autonomous Machine Intelligence (LeCun, 2022)

`openreview:BZ5a1r-kVsf` · Self-supervised learning and vision · unknown

- final **-0.61** (conf 0.91, pct 3) · impact +0.06 · DROP · salvage dr7bf
- mean rating (1–10): **4.4** · accept votes **2/6** · percentile rank_avg 22.9 (100=best) · rank in year 11.0 (1=best)
- NAIPv2 `-4.348` · NAIP-v1 `0.523` · SciJudge `1.364` · DGC-BERT `0.006`
- CycleReviewer 8B `1.0` Reject · 70B `` 
- DeepReviewer 7B Std `3.0` Reject · 7B Fast ``  (S/P/C 2.75/2.5/2.5) · 14B Fast `3.5` Reject
- OpenReviewer `8.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `5.0` Accept
- Telegram: [dtulinov/508](https://t.me/dtulinov/508), [dl_stories/497](https://t.me/dl_stories/497), [rybolos_channel/249](https://t.me/rybolos_channel/249), [gonzo_ML/3150](https://t.me/gonzo_ML/3150), [rybolos_channel/239](https://t.me/rybolos_channel/239), [emptyset_of_ideas/304](https://t.me/emptyset_of_ideas/304), [chillhousetech/680](https://t.me/chillhousetech/680), [knowledge_accumulator/46](https://t.me/knowledge_accumulator/46)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/openreview_BZ5a1r-kVsf.md#weaknesses): The paper lacks concrete implementation details and experimental results to support the proposed architecture and training paradigms. The paper does not provide any code or pseudocode for the proposed architecture, and the experimental results are limited to a few examples and do not provide any quantitative evaluation of the performance of the proposed methods.…
  - [DR-14B Fast](reviews/deepreviewer-14b/openreview_BZ5a1r-kVsf.md#weaknesses): The most significant weakness of this paper is its lack of empirical validation. As a position paper, it primarily outlines a proposed architecture and training paradigms without providing concrete experimental results to support its claims. This absence of empirical evidence makes it difficult to assess the practical viability of the proposed approach.…

<a id="arxiv-2111.07832"></a>
### iBOT: Image BERT Pre-Training with Online Tokenizer

`arxiv:2111.07832` · Self-supervised learning and vision · 2021-11-15

- final **+0.14** (conf 1.00, pct 58) · impact +1.33 · WATCH
- mean rating (1–10): **6.2** · accept votes **4/7** · percentile rank_avg 57.7 (100=best) · rank in year 3.0 (1=best)
- NAIPv2 `-1.606` · NAIP-v1 `0.771` · SciJudge `3.147` · DGC-BERT `0.353`
- CycleReviewer 8B `5.5` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `7.0` Accept (S/P/C 3.0/3.0/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [j_links/5504](https://t.me/j_links/5504), [gonzo_ML/5626](https://t.me/gonzo_ML/5626), [nn_for_science/1435](https://t.me/nn_for_science/1435)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2111.07832.md#weaknesses): 1. The novelty of the proposed method is limited. The idea of using self-distillation for pre-training has been explored in previous works, such as DINO. 2. The paper lacks a clear motivation for the proposed method. The authors do not provide a clear explanation of why masked image modeling with a self-distillation objective is a good approach for pre-training vision transformers. 3.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2111.07832.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. One significant limitation is the lack of a comprehensive analysis of the computational cost associated with iBOT's training process.…

<a id="arxiv-2105.04906"></a>
### VICReg: Variance-Invariance-Covariance Regularization for Self-Supervised Learning

`arxiv:2105.04906` · Self-supervised learning and vision · 2021-05-11

- final **-0.08** (conf 1.00, pct 28) · impact +0.24 · WATCH
- mean rating (1–10): **5.2** · accept votes **3/7** · percentile rank_avg 41.2 (100=best) · rank in year 6.0 (1=best)
- NAIPv2 `-2.426` · NAIP-v1 `0.488` · SciJudge `3.352` · DGC-BERT `0.930`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `4.0` Reject · 7B Fast `5.8` Reject (S/P/C 2.75/3.0/2.5) · 14B Fast `6.5` Accept
- OpenReviewer `3.0` Reject (S/P/C 2.0/2.0/2.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/590](https://t.me/gonzo_ML/590)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2105.04906.md#weaknesses): The novelty of the proposed method is limited. The proposed method is based on the principle of preserving the information content of the embeddings. The method is similar to the Barlow Twins method, which also decorrelates the variables of each embedding and prevents an informational collapse in which the variables would vary together or be highly correlated.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2105.04906.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further attention. First, while the paper introduces the variance preservation term as a novel contribution, the in-depth analysis of its behavior is lacking.…

<a id="arxiv-2104.14294"></a>
### Emerging Properties in Self-Supervised Vision Transformers

`arxiv:2104.14294` · Self-supervised learning and vision · 2021-04-29

- final **+0.48** (conf 1.00, pct 94) · impact +2.06 · KEEP
- mean rating (1–10): **6.5** · accept votes **5/7** · percentile rank_avg 72.6 (100=best) · rank in year 1.0 (1=best)
- NAIPv2 `-1.077` · NAIP-v1 `0.827` · SciJudge `3.543` · DGC-BERT `0.159`
- CycleReviewer 8B `5.8` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.7` Accept (S/P/C 3.0/3.0/2.33) · 14B Fast `7.3` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [dl_stories/722](https://t.me/dl_stories/722), [j_links/4810](https://t.me/j_links/4810), [dl_stories/667](https://t.me/dl_stories/667), [gonzo_ML/5626](https://t.me/gonzo_ML/5626), [gonzo_ML/688](https://t.me/gonzo_ML/688), [nn_for_science/1435](https://t.me/nn_for_science/1435), [tech_priestess/247](https://t.me/tech_priestess/247)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2104.14294.md#weaknesses): 1. The novelty of the proposed method is limited. The authors mention that their method is similar to BYOL and MoCov2, and the main difference is the use of a momentum encoder and multi-crop training. However, these components have been used in previous works, and the authors do not provide any new insights or analysis on how they contribute to the performance of the method.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2104.14294.md#weaknesses): While I find the paper to be generally strong, there are several weaknesses that I believe warrant further attention. First, the paper's focus on Vision Transformers (ViTs) leads to a lack of detailed analysis of how the DINO framework interacts with specific architectural components of ViTs.…

<a id="arxiv-2006.09882"></a>
### Unsupervised Learning of Visual Features by Contrasting Cluster Assignments

`arxiv:2006.09882` · Self-supervised learning and vision · 2020-06-17

- final **+0.43** (conf 1.00, pct 91) · impact +1.11 · KEEP
- mean rating (1–10): **6.3** · accept votes **4/7** · percentile rank_avg 61.5 (100=best) · rank in year 4.0 (1=best)
- NAIPv2 `-1.362` · NAIP-v1 `0.729` · SciJudge `2.525` · DGC-BERT `0.839`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.0` Reject · 7B Fast `7.5` Accept (S/P/C 3.25/3.25/3.25) · 14B Fast `7.0` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [gonzo_ML/688](https://t.me/gonzo_ML/688), [nn_for_science/1435](https://t.me/nn_for_science/1435)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2006.09882.md#weaknesses): The proposed method is not novel, as it is a variant of DeepCluster. The main difference is that the proposed method learns the cluster assignments online, while DeepCluster learns them offline. However, the online learning approach requires a more complex optimization process and is not as efficient as the offline learning approach.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2006.09882.md#weaknesses): While I find the paper to be strong overall, there are several weaknesses that I believe warrant further discussion. Firstly, while the paper introduces the multi-crop strategy as a key contribution, the analysis of its individual components could be more granular.…

<a id="arxiv-2606.18543"></a>
### CEO-Bench: Can Agents Play the Long Game?

`arxiv:2606.18543` · Retrieval, embeddings, benchmarks · 2026-06-16

- final **+0.17** (conf 1.00, pct 62) · impact +1.15 · WATCH
- mean rating (1–10): **6.4** · accept votes **5/7** · percentile rank_avg 65.4 (100=best) · rank in year 19.0 (1=best)
- NAIPv2 `-0.407` · NAIP-v1 `0.710` · SciJudge `2.262` · DGC-BERT `0.191`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.8` Reject · 7B Fast `6.5` Accept (S/P/C 3.0/3.0/2.75) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [dealerAI/1857](https://t.me/dealerAI/1857), [boris_again/3974](https://t.me/boris_again/3974)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2606.18543.md#weaknesses): The paper does not provide a detailed description of the models used in the evaluation, including their architecture, training data, and hyperparameters. This makes it difficult to understand the specific capabilities and limitations of each model and how they relate to the task.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2606.18543.md#weaknesses): of current language models in long-horizon planning. The ablation studies, which explore the impact of competitor strength and time horizon, are also a valuable addition, providing a more nuanced understanding of the benchmark's challenges.…

<a id="arxiv-2410.07095"></a>
### MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering

`arxiv:2410.07095` · Retrieval, embeddings, benchmarks · 2024-10-09

- final **+0.31** (conf 1.00, pct 80) · impact +0.92 · KEEP
- mean rating (1–10): **6.0** · accept votes **4/7** · percentile rank_avg 58.5 (100=best) · rank in year 9.0 (1=best)
- NAIPv2 `0.277` · NAIP-v1 `0.631` · SciJudge `2.588` · DGC-BERT `0.394`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.0` Accept (S/P/C 2.5/3.0/2.75) · 14B Fast `6.2` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `7.0` Accept
- Telegram: [seeallochnaya/1866](https://t.me/seeallochnaya/1866), [data_secrets/5120](https://t.me/data_secrets/5120), [lovedeathtransformers/8445](https://t.me/lovedeathtransformers/8445), [gonzo_ML/4261](https://t.me/gonzo_ML/4261), [rybolos_channel/1270](https://t.me/rybolos_channel/1270)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2410.07095.md#weaknesses): 1. The paper does not provide a clear definition of machine learning engineering and how it is distinct from other areas of AI research. It would be helpful to provide a more detailed explanation of the scope and focus of the benchmark.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2410.07095.md#weaknesses): Despite its strengths, the paper exhibits several weaknesses that warrant careful consideration. One significant limitation is the lack of a deep analysis of the agent's behavior and the factors influencing its performance.…

<a id="arxiv-2405.08007"></a>
### People cannot distinguish GPT-4 from a human in a Turing test

`arxiv:2405.08007` · Retrieval, embeddings, benchmarks · 2024-05-09

- final **-0.28** (conf 1.00, pct 15) · impact +1.95 · WATCH
- mean rating (1–10): **4.6** · accept votes **1/7** · percentile rank_avg 37.3 (100=best) · rank in year 37.0 (1=best)
- NAIPv2 `-2.674` · NAIP-v1 `0.806` · SciJudge `3.333` · DGC-BERT `0.083`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `3.8` Reject · 7B Fast `4.7` Reject (S/P/C 2.67/3.0/2.33) · 14B Fast `7.5` Accept
- OpenReviewer `3.0` Reject (S/P/C 3.0/3.0/1.0) · SEA-E `3.0` Reject
- Telegram: [denissexy/8700](https://t.me/denissexy/8700), [gonzo_ML/2655](https://t.me/gonzo_ML/2655), [axisofordinary/6315](https://t.me/axisofordinary/6315), [tech_priestess/1735](https://t.me/tech_priestess/1735)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2405.08007.md#weaknesses): The paper is not written in a way that is easy to understand. The authors seem to be writing for a very specific audience, and the paper is not well-suited for a broader audience.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2405.08007.md#weaknesses): While this paper presents a valuable contribution to the field, several weaknesses warrant careful consideration. First, the paper's core contribution, while empirically sound, may be considered somewhat incremental.…

<a id="arxiv-2402.16822"></a>
### Rainbow Teaming: Open-Ended Generation of Diverse Adversarial Prompts

`arxiv:2402.16822` · Retrieval, embeddings, benchmarks · 2024-02-26

- final **+0.38** (conf 1.00, pct 86) · impact +1.36 · KEEP
- mean rating (1–10): **6.6** · accept votes **6/7** · percentile rank_avg 71.9 (100=best) · rank in year 1.0 (1=best)
- NAIPv2 `-1.450` · NAIP-v1 `0.661` · SciJudge `3.444` · DGC-BERT `0.923`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.2` Accept · 7B Fast `6.7` Accept (S/P/C 2.67/3.33/2.67) · 14B Fast `7.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/4.0/3.0) · SEA-E `6.0` Accept
- Telegram: [rybolos_channel/1495](https://t.me/rybolos_channel/1495)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2402.16822.md#weaknesses): The paper lacks a clear definition of what constitutes an adversarial prompt and how it is evaluated. The authors use a variety of terms such as "harmful", "incorrect", "toxic", and "unsafe" to describe the outputs of LLMs when prompted with adversarial prompts, but it is not clear how these terms are defined or measured.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2402.16822.md#weaknesses): While I find the paper to be a valuable contribution, there are several weaknesses that I have identified through my analysis. First, the paper lacks a thorough comparison with existing adversarial prompt generation techniques. While the authors mention that their method is inspired by Samvelyan et al.…

<a id="arxiv-2402.12483"></a>
### Artifacts or Abduction: How Do LLMs Answer Multiple-Choice Questions Without the Question?

`arxiv:2402.12483` · Retrieval, embeddings, benchmarks · 2024-02-19

- final **-0.04** (conf 1.00, pct 33) · impact +0.90 · WATCH
- mean rating (1–10): **6.0** · accept votes **4/7** · percentile rank_avg 51.3 (100=best) · rank in year 20.0 (1=best)
- NAIPv2 `-1.801` · NAIP-v1 `0.656` · SciJudge `1.994` · DGC-BERT `0.747`
- CycleReviewer 8B `5.5` Reject · 70B `` 
- DeepReviewer 7B Std `4.2` Reject · 7B Fast `6.3` Accept (S/P/C 2.67/3.0/2.67) · 14B Fast `6.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [tech_priestess/1699](https://t.me/tech_priestess/1699), [axisofordinary/6146](https://t.me/axisofordinary/6146), [seeallochnaya/1697](https://t.me/seeallochnaya/1697)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2402.12483.md#weaknesses): The paper does not provide a clear conclusion or recommendation for how to improve MCQA benchmarks. The authors state that the LLMs' performance on choices-only prompts is not solely due to memorization, but do not provide a clear explanation of what is causing the performance.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2402.12483.md#weaknesses): While this paper presents a compelling investigation into LLM behavior on MCQA tasks, several weaknesses warrant careful consideration. First, the paper's reliance on a black-box approach, while practical given the computational constraints, limits the depth of analysis.…

<a id="arxiv-2311.16452"></a>
### Can Generalist Foundation Models Outcompete Special-Purpose Tuning? Case Study in Medicine

`arxiv:2311.16452` · Retrieval, embeddings, benchmarks · 2023-11-28

- final **+0.05** (conf 1.00, pct 46) · impact +0.62 · WATCH
- mean rating (1–10): **5.9** · accept votes **5/7** · percentile rank_avg 50.8 (100=best) · rank in year 24.0 (1=best)
- NAIPv2 `-2.244` · NAIP-v1 `0.628` · SciJudge `2.399` · DGC-BERT `0.706`
- CycleReviewer 8B `5.5` Accept · 70B `` 
- DeepReviewer 7B Std `5.2` Reject · 7B Fast `5.3` Reject (S/P/C 2.67/3.0/2.33) · 14B Fast `6.8` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/5812](https://t.me/axisofordinary/5812), [seeallochnaya/928](https://t.me/seeallochnaya/928)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2311.16452.md#weaknesses): The paper lacks a comprehensive evaluation of the proposed method, particularly in real-world scenarios. - The paper does not provide a detailed comparison with existing methods, making it difficult to assess the novelty and effectiveness of the proposed approach. - The paper does not discuss potential risks and limitations of the proposed method, such as bias and hallucinations.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2311.16452.md#weaknesses): While this paper presents compelling results, I have identified several weaknesses that warrant further consideration. Firstly, the paper lacks a detailed analysis of the computational resources required for Medprompt's preprocessing stage.…

<a id="arxiv-2309.16797"></a>
### Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution

`arxiv:2309.16797` · Retrieval, embeddings, benchmarks · 2023-09-28

- final **-0.20** (conf 1.00, pct 20) · impact +0.57 · WATCH
- mean rating (1–10): **4.9** · accept votes **4/7** · percentile rank_avg 41.6 (100=best) · rank in year 35.0 (1=best)
- NAIPv2 `-4.238` · NAIP-v1 `0.704` · SciJudge `0.737` · DGC-BERT `0.860`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/3.0) · 14B Fast `6.7` Accept
- OpenReviewer `3.0` Reject (S/P/C 2.0/2.0/2.0) · SEA-E `6.0` Accept
- Telegram: [j_links/7082](https://t.me/j_links/7082), [rybolos_channel/1495](https://t.me/rybolos_channel/1495), [axisofordinary/5574](https://t.me/axisofordinary/5574)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2309.16797.md#weaknesses): 1. The proposed method is not well-motivated. The authors claim that the proposed method is self-referential, but it is not clear what self-referential means. The authors also claim that the proposed method is an interesting future where larger and more capable LLMs could further amplify the gains of our approach. However, it is not clear how the proposed method can be scaled to larger models. 2.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2309.16797.md#weaknesses): While I find the paper's contributions to be significant, there are several weaknesses that I have identified through my analysis. First, the paper lacks a thorough analysis of the computational cost associated with Promptbreeder.…

<a id="acl-2023.acl-demo.51"></a>
### A System for Answering Simple Questions in Multiple Languages

`acl:2023.acl-demo.51` · Retrieval, embeddings, benchmarks · unknown

- final **-0.28** (conf 0.91, pct 14) · impact -0.97 · DROP · partial fulltext
- mean rating (1–10): **5.2** · accept votes **2/7** · percentile rank_avg 24.9 (100=best) · rank in year 10.0 (1=best)
- NAIPv2 `-3.318` · NAIP-v1 `0.375` · SciJudge `-1.113` · DGC-BERT `0.054`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `4.0` Reject · 7B Fast `5.0` Reject (S/P/C 2.75/3.0/2.5) · 14B Fast `3.7` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [abstractDL/233](https://t.me/abstractDL/233), [boris_again/2173](https://t.me/boris_again/2173)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/acl_2023.acl-demo.51.md#weaknesses): The method is limited to simple questions and cannot handle multi-hop questions. - The method is limited to one-hop questions and cannot handle complex questions that require reasoning. - The method is limited to questions that can be answered by a single triple in the knowledge graph and cannot handle questions that require multiple triples to answer.…
  - [DR-14B Fast](reviews/deepreviewer-14b/acl_2023.acl-demo.51.md#weaknesses): After a thorough review of the paper and the provided analyses, several key weaknesses emerge, which I have independently validated. Firstly, the paper's scope is notably narrow, focusing exclusively on simple, one-hop KGQA. As stated in the introduction, the authors explicitly focus on questions like “What is the capital of France?” and acknowledge the opinion that this task is nearly solved.…

<a id="arxiv-2304.08467"></a>
### Learning to Compress Prompts with Gist Tokens

`arxiv:2304.08467` · Retrieval, embeddings, benchmarks · 2023-04-17

- final **-0.08** (conf 1.00, pct 27) · impact +0.12 · WATCH
- mean rating (1–10): **5.3** · accept votes **4/7** · percentile rank_avg 43.7 (100=best) · rank in year 33.0 (1=best)
- NAIPv2 `-1.269` · NAIP-v1 `0.576` · SciJudge `1.529` · DGC-BERT `0.801`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `4.8` Reject (S/P/C 2.5/2.75/2.5) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `5.0` Reject
- Telegram: [axisofordinary/4834](https://t.me/axisofordinary/4834)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2304.08467.md#weaknesses): The paper lacks a clear motivation for the proposed method. The authors mention that the goal is to compress prompts into a smaller set of tokens, but it is not clear why this is necessary or what the benefits of doing so are. - The evaluation is limited to a single dataset and a single LM architecture. It would be helpful to see how the method performs on other datasets and architectures.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2304.08467.md#weaknesses): While I appreciate the simplicity and potential of the proposed gisting method, my analysis has revealed several weaknesses that warrant careful consideration. First, the paper's evaluation lacks a thorough analysis of the method's robustness to prompt variations.…

<a id="arxiv-2212.14024"></a>
### Demonstrate-Search-Predict: Composing retrieval and language models for knowledge-intensive NLP

`arxiv:2212.14024` · Retrieval, embeddings, benchmarks · 2022-12-28

- final **+0.30** (conf 1.00, pct 78) · impact +0.68 · KEEP
- mean rating (1–10): **6.1** · accept votes **6/7** · percentile rank_avg 59.5 (100=best) · rank in year 6.0 (1=best)
- NAIPv2 `0.195` · NAIP-v1 `0.791` · SciJudge `-1.113` · DGC-BERT `0.669`
- CycleReviewer 8B `5.8` Accept · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `5.7` Reject (S/P/C 2.67/2.67/2.67) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [seeallochnaya/368](https://t.me/seeallochnaya/368), [seeallochnaya/55](https://t.me/seeallochnaya/55), [seeallochnaya/20](https://t.me/seeallochnaya/20)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2212.14024.md#weaknesses): The paper lacks a clear motivation for the DSP framework. The authors should provide a more detailed explanation of the limitations of existing retrieval-augmented in-context learning approaches and how DSP addresses these limitations.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2212.14024.md#weaknesses): Despite the strengths of the proposed DSP framework, I have identified several weaknesses that warrant careful consideration. A primary concern is the limited scope of the experimental evaluation. The authors conduct experiments using only one language model, GPT-3.5, and one retrieval model, ColBERTv2.…

<a id="arxiv-2212.09741"></a>
### One Embedder, Any Task: Instruction-Finetuned Text Embeddings

`arxiv:2212.09741` · Retrieval, embeddings, benchmarks · 2022-12-19

- final **+0.53** (conf 1.00, pct 97) · impact +1.01 · KEEP
- mean rating (1–10): **6.1** · accept votes **6/7** · percentile rank_avg 70.3 (100=best) · rank in year 1.0 (1=best)
- NAIPv2 `0.333` · NAIP-v1 `0.723` · SciJudge `2.739` · DGC-BERT `0.877`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.5` Accept (S/P/C 3.0/3.25/3.0) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [buckwheat_thoughts/15](https://t.me/buckwheat_thoughts/15), [dealerAI/8](https://t.me/dealerAI/8), [lovedeathtransformers/5427](https://t.me/lovedeathtransformers/5427)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2212.09741.md#weaknesses): 1. The novelty of the paper is limited. The paper only proposes a new dataset and a new method based on the existing GTR model. The proposed method is not novel, as it is a simple extension of the existing GTR model. 2. The paper does not provide a thorough analysis of the proposed method.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2212.09741.md#weaknesses): While I find the paper to be generally strong, there are several weaknesses that I have identified through my analysis. First, the paper lacks a detailed analysis of the model's performance on individual tasks within the MEDI dataset.…

<a id="arxiv-2206.04615"></a>
### Beyond the Imitation Game: Quantifying and extrapolating the capabilities of language models

`arxiv:2206.04615` · Retrieval, embeddings, benchmarks · 2022-06-09

- final **+0.50** (conf 0.83, pct 95) · impact +1.82 · KEEP
- mean rating (1–10): **6.4** · accept votes **3/6** · percentile rank_avg 66.4 (100=best) · rank in year 2.0 (1=best)
- NAIPv2 `-0.651` · NAIP-v1 `0.794` · SciJudge `3.656` · DGC-BERT `0.391`
- CycleReviewer 8B `6.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.2` Reject · 7B Fast ``  (S/P/C None/None/None) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [mishin_learning/1023](https://t.me/mishin_learning/1023), [rybolos_channel/157](https://t.me/rybolos_channel/157), [j_links/5901](https://t.me/j_links/5901), [rybolos_channel/705](https://t.me/rybolos_channel/705), [rybolos_channel/641](https://t.me/rybolos_channel/641), [j_links/6786](https://t.me/j_links/6786), [tech_priestess/536](https://t.me/tech_priestess/536)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2206.04615.md#weaknesses): The paper does not provide a clear definition of what is meant by "beyond the imitation game". It would be helpful to have a more explicit definition of what the benchmark is intended to measure and what it is trying to achieve. - The paper does not provide a clear explanation of how the tasks were selected for the benchmark.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2206.04615.md#weaknesses): While I appreciate the contributions of this paper, I have identified several weaknesses that warrant discussion. Firstly, the paper's analysis of task characteristics, particularly the categorization of tasks as either 'knowledge-based' or 'composite,' lacks a rigorous, quantifiable approach.…

<a id="arxiv-2205.13147"></a>
### Matryoshka Representation Learning

`arxiv:2205.13147` · Retrieval, embeddings, benchmarks · 2022-05-26

- final **+0.59** (conf 1.00, pct 98) · impact +0.08 · KEEP
- mean rating (1–10): **6.1** · accept votes **6/7** · percentile rank_avg 66.2 (100=best) · rank in year 3.0 (1=best)
- NAIPv2 `2.609` · NAIP-v1 `0.626` · SciJudge `0.790` · DGC-BERT `0.871`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `7.0` Accept (S/P/C 3.25/3.0/3.0) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [rybolos_channel/1037](https://t.me/rybolos_channel/1037), [nn_for_science/1914](https://t.me/nn_for_science/1914), [doomgrad/757](https://t.me/doomgrad/757), [gonzo_ML/2311](https://t.me/gonzo_ML/2311), [gonzo_ML/3368](https://t.me/gonzo_ML/3368), [gonzo_ML/2037](https://t.me/gonzo_ML/2037), [buckwheat_thoughts/8](https://t.me/buckwheat_thoughts/8), [gonzo_ML/3369](https://t.me/gonzo_ML/3369)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2205.13147.md#weaknesses): The paper lacks a clear motivation for the proposed method. The authors should provide more details on why learning a single representation that can be used for multiple downstream tasks is important and how it can benefit the community. - The paper lacks a clear explanation of the proposed method.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2205.13147.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. One significant concern is the lack of a detailed analysis of the computational overhead introduced during the training phase due to the multi-objective optimization.…

<a id="acl-2022.emnlp-main.340"></a>
### Super-NaturalInstructions: Generalization via Declarative Instructions on 1600+ NLP Tasks

`acl:2022.emnlp-main.340` · Retrieval, embeddings, benchmarks · unknown

- final **+0.10** (conf 0.83, pct 51) · impact +1.00 · WATCH · partial fulltext · salvage dr7bf
- mean rating (1–10): **6.0** · accept votes **4/6** · percentile rank_avg 49.3 (100=best) · rank in year 4.0 (1=best)
- NAIPv2 `-2.061` · NAIP-v1 `0.551` · SciJudge `3.138` · DGC-BERT `0.241`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast ``  (S/P/C 2.75/2.75/2.75) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/1585](https://t.me/gonzo_ML/1585)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/acl_2022.emnlp-main.340.md#weaknesses): The paper does not provide a detailed analysis of the limitations of the benchmark and the model. - The paper does not provide a detailed analysis of the potential biases in the benchmark and the model. - The paper does not provide a detailed analysis of the potential ethical implications of using the benchmark and the model.…
  - [DR-14B Fast](reviews/deepreviewer-14b/acl_2022.emnlp-main.340.md#weaknesses): . The fact that Tk-INSTRUCT consistently outperforms other generalization-based methods across all task types is a strong indication of its effectiveness.

<a id="arxiv-2112.07899"></a>
### Large Dual Encoders Are Generalizable Retrievers

`arxiv:2112.07899` · Retrieval, embeddings, benchmarks · 2021-12-15

- final **+0.30** (conf 1.00, pct 78) · impact +0.23 · KEEP
- mean rating (1–10): **6.3** · accept votes **4/7** · percentile rank_avg 59.0 (100=best) · rank in year 2.0 (1=best)
- NAIPv2 `-0.023` · NAIP-v1 `0.572` · SciJudge `2.174` · DGC-BERT `0.059`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.2` Accept · 7B Fast `6.2` Reject (S/P/C 2.75/3.0/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [dealerAI/8](https://t.me/dealerAI/8), [lovedeathtransformers/5427](https://t.me/lovedeathtransformers/5427)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2112.07899.md#weaknesses): The paper does not provide a clear explanation of why scaling up the model size improves the generalization of dual encoders. The authors should provide more analysis and discussion on this aspect. - The paper does not provide a comparison with other models that use different interaction layers, such as multi-vector encoding models and ColBERT.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2112.07899.md#weaknesses): While this paper presents compelling results, several limitations warrant careful consideration. First, the paper lacks a direct comparison with other similarly scaled dense retrieval models. The authors primarily compare against smaller models like DPR and ANCE, as well as sparse methods like BM25 and DocT5Query.…

<a id="acl-2022.acl-long.360"></a>
### PRIMERA: Pyramid-based Masked Sentence Pre-training for Multi-document Summarization

`acl:2022.acl-long.360` · Retrieval, embeddings, benchmarks · unknown

- final **-0.08** (conf 0.91, pct 28) · impact +0.69 · WATCH · partial fulltext
- mean rating (1–10): **5.7** · accept votes **3/7** · percentile rank_avg 38.5 (100=best) · rank in year 7.0 (1=best)
- NAIPv2 `-2.773` · NAIP-v1 `0.625` · SciJudge `1.991` · DGC-BERT `0.079`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `3.8` Reject · 7B Fast `5.7` Reject (S/P/C 2.67/3.0/2.67) · 14B Fast `6.0` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/1507](https://t.me/gonzo_ML/1507)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/acl_2022.acl-long.360.md#weaknesses): The paper does not discuss the limitations of the proposed method. It would be helpful to discuss the potential limitations and future work. - The paper does not provide any qualitative analysis of the results. It would be helpful to provide some examples of the generated summaries and compare them with the ground truth summaries.…
  - [DR-14B Fast](reviews/deepreviewer-14b/acl_2022.acl-long.360.md#weaknesses): While the paper presents a compelling approach, I have identified several weaknesses that warrant further consideration. First, the paper lacks a detailed analysis of the computational costs associated with PRIMERA.…

<a id="arxiv-2101.02235"></a>
### Did Aristotle Use a Laptop? A Question Answering Benchmark with Implicit Reasoning Strategies

`arxiv:2101.02235` · Retrieval, embeddings, benchmarks · 2021-01-06

- final **+0.07** (conf 1.00, pct 48) · impact +0.16 · WATCH
- mean rating (1–10): **6.0** · accept votes **5/7** · percentile rank_avg 51.1 (100=best) · rank in year 4.0 (1=best)
- NAIPv2 `-2.572` · NAIP-v1 `0.593` · SciJudge `1.830` · DGC-BERT `0.469`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `4.8` Reject (S/P/C 2.5/2.5/2.25) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [gonzo_ML/1585](https://t.me/gonzo_ML/1585)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2101.02235.md#weaknesses): The authors should provide more details about the baselines and their performance. In particular, it would be helpful to know how the baselines are trained and evaluated, and what types of reasoning they are able to perform.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2101.02235.md#weaknesses): While the paper presents a valuable contribution, several weaknesses warrant careful consideration. First, the paper's definition of 'implicit' questions, while providing examples, lacks a formal definition and clear, objective criteria.…

<a id="arxiv-2608.23875"></a>
### AI Finds A Way

`arxiv:2608.23875` · Agents, open-endedness, AGI · 2026-08-24

- final **-0.57** (conf 1.00, pct 5) · impact -0.56 · DROP
- mean rating (1–10): **4.7** · accept votes **2/7** · percentile rank_avg 24.5 (100=best) · rank in year 70.0 (1=best)
- NAIPv2 `-2.221` · NAIP-v1 `0.558` · SciJudge `-2.610` · DGC-BERT `0.067`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `4.7` Reject (S/P/C 2.0/2.33/2.0) · 14B Fast `3.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [j_links/8501](https://t.me/j_links/8501), [gonzo_ML/5974](https://t.me/gonzo_ML/5974)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2608.23875.md#weaknesses): The paper lacks a clear and concise summary of the main contributions and findings. - The paper does not provide a clear and well-defined research question or hypothesis. - The paper does not provide a clear and well-defined methodology for collecting and analyzing the anecdotes. - The paper does not provide a clear and well-defined evaluation or validation of the findings.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2608.23875.md#weaknesses): Despite the paper's strengths, several limitations are evident. Firstly, the paper's reliance on anecdotal evidence without a systematic analysis of the conditions under which these behaviors emerge is a significant weakness.…

<a id="arxiv-2608.19197"></a>
### SPADE: Self-Play in Adaptive Synthetic Executable Environments

`arxiv:2608.19197` · Agents, open-endedness, AGI · 2026-08-19

- final **+0.39** (conf 1.00, pct 86) · impact +0.26 · KEEP
- mean rating (1–10): **7.0** · accept votes **6/7** · percentile rank_avg 72.9 (100=best) · rank in year 6.0 (1=best)
- NAIPv2 `0.183` · NAIP-v1 `0.656` · SciJudge `-0.099` · DGC-BERT `0.078`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `7.0` Accept (S/P/C 3.0/3.0/3.0) · 14B Fast `7.0` Accept
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/4.0) · SEA-E `7.0` Accept
- Telegram: [axisofordinary/9061](https://t.me/axisofordinary/9061)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2608.19197.md#weaknesses): 1. The paper lacks a clear comparison with existing methods in the field, making it difficult to assess the novelty and significance of the proposed approach.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2608.19197.md#weaknesses): While I am impressed with the overall contribution of this paper, my analysis has identified several weaknesses that warrant further discussion. First, the paper lacks a detailed analysis of the hint generation process. While the paper describes the *use* of hints, it does not delve into the *nature* of these hints, their complexity, or their impact on the learning process.…

<a id="arxiv-2608.08311"></a>
### Ouroboros: A Self-Developing Frontier Coding Agent with Reviewed Core Evolution

`arxiv:2608.08311` · Agents, open-endedness, AGI · 2026-08-08

- final **-0.12** (conf 1.00, pct 24) · impact -0.71 · WATCH
- mean rating (1–10): **6.2** · accept votes **3/7** · percentile rank_avg 40.6 (100=best) · rank in year 63.0 (1=best)
- NAIPv2 `-1.249` · NAIP-v1 `0.368` · SciJudge `0.814` · DGC-BERT `0.012`
- CycleReviewer 8B `4.0` Reject · 70B `` 
- DeepReviewer 7B Std `3.0` Reject · 7B Fast `7.5` Accept (S/P/C 3.5/3.25/3.75) · 14B Fast `5.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `8.0` Accept
- Telegram: [abstractDL/439](https://t.me/abstractDL/439), [lovedeathtransformers/10949](https://t.me/lovedeathtransformers/10949)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2608.08311.md#weaknesses): The paper lacks clarity in explaining the methodology and evaluation of the agent. The paper does not provide enough details on how the agent's performance is evaluated, and how the benchmarks are used to assess the agent's capabilities. The paper also does not provide enough information on the agent's limitations and potential biases.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2608.08311.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. The most significant issue, in my view, is the lack of detailed technical explanations, which makes it challenging to fully understand the Ouroboros framework and its implementation.…

<a id="arxiv-2607.13104"></a>
### Self-Improvements in Modern Agentic Systems: A Survey

`arxiv:2607.13104` · Agents, open-endedness, AGI · 2026-07-14

- final **+0.27** (conf 1.00, pct 74) · impact +0.92 · KEEP
- mean rating (1–10): **6.3** · accept votes **6/7** · percentile rank_avg 65.6 (100=best) · rank in year 17.0 (1=best)
- NAIPv2 `0.084` · NAIP-v1 `0.655` · SciJudge `2.367` · DGC-BERT `0.010`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `7.0` Accept · 7B Fast `7.0` Accept (S/P/C 3.25/3.0/2.75) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `5.0` Accept
- Telegram: [gonzo_ML/5772](https://t.me/gonzo_ML/5772)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2607.13104.md#weaknesses): The paper is a survey, and it does not present any new research results. The authors do not provide any new insights or perspectives on the field of self-improving agents. The paper is also quite long and dense, which may make it difficult for readers to follow.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2607.13104.md#weaknesses): While the paper is thorough and well-structured, it has several limitations that could be addressed to enhance its overall quality and impact. One significant weakness is the lack of a detailed discussion on the limitations and scalability of scaffold improvement.…

<a id="arxiv-2605.13821"></a>
### Harnessing Agentic Evolution

`arxiv:2605.13821` · Agents, open-endedness, AGI · 2026-05-13

- final **+0.05** (conf 1.00, pct 45) · impact +0.29 · WATCH
- mean rating (1–10): **6.3** · accept votes **5/7** · percentile rank_avg 61.3 (100=best) · rank in year 27.0 (1=best)
- NAIPv2 `-0.344` · NAIP-v1 `0.618` · SciJudge `0.792` · DGC-BERT `0.625`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `7.0` Accept (S/P/C 3.0/3.25/3.0) · 14B Fast `6.5` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2605.13821.md#weaknesses): The paper does not provide a detailed discussion of the limitations of the proposed approach. - The paper does not provide a discussion of the potential risks and challenges associated with the proposed approach. - The paper does not provide a discussion of the potential applications of the proposed approach. - The paper does not provide a discussion of the potential future work.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2605.13821.md#weaknesses): Despite the paper's strengths, several limitations and areas for improvement are evident. One of the primary concerns is the clarity and readability of the paper, particularly in the methodology section. The introduction of mathematical notations and the description of the meta-agent's role are dense and challenging to follow.…

<a id="arxiv-2603.19461"></a>
### Hyperagents

`arxiv:2603.19461` · Agents, open-endedness, AGI · 2026-03-19

- final **+0.02** (conf 1.00, pct 38) · impact +1.01 · WATCH
- mean rating (1–10): **6.2** · accept votes **6/7** · percentile rank_avg 64.6 (100=best) · rank in year 21.0 (1=best)
- NAIPv2 `-0.993` · NAIP-v1 `0.700` · SciJudge `1.803` · DGC-BERT `0.445`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.5` Accept (S/P/C 2.75/2.75/2.5) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [rybolos_channel/1775](https://t.me/rybolos_channel/1775), [gonzo_ML/5042](https://t.me/gonzo_ML/5042), [axisofordinary/8281](https://t.me/axisofordinary/8281), [boris_again/3821](https://t.me/boris_again/3821), [gonzo_ML/5032](https://t.me/gonzo_ML/5032)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2603.19461.md#weaknesses): The paper lacks a theoretical analysis of the proposed method. - The paper lacks a comparison with other self-improvement algorithms. - The paper lacks a discussion of the limitations of the proposed method.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2603.19461.md#weaknesses): Despite the paper's strengths, several weaknesses and areas for improvement are evident. One of the primary concerns is the clarity and precision of the terminology used.…

<a id="arxiv-2602.07755"></a>
### Learning to Continually Learn via Meta-learning Agentic Memory Designs

`arxiv:2602.07755` · Agents, open-endedness, AGI · 2026-02-08

- final **+0.11** (conf 1.00, pct 54) · impact +0.13 · WATCH
- mean rating (1–10): **6.3** · accept votes **6/7** · percentile rank_avg 56.5 (100=best) · rank in year 36.0 (1=best)
- NAIPv2 `-0.724` · NAIP-v1 `0.525` · SciJudge `1.527` · DGC-BERT `0.013`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.5` Accept (S/P/C 2.75/3.0/2.75) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/8164](https://t.me/axisofordinary/8164)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2602.07755.md#weaknesses): The paper lacks a clear definition of the search space for memory designs. The authors mention that the search space is defined as code, but it is unclear what specific aspects of memory design are being explored. - The paper does not provide a thorough analysis of the limitations of the proposed method. For example, it is not clear how ALMA would perform in more complex or dynamic environments.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2602.07755.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, while the paper claims to minimize human effort, the initial setup of the Meta Agent and the definition of the search space require significant human effort and expertise.…

<a id="arxiv-2601.21557"></a>
### Meta Context Engineering via Agentic Skill Evolution

`arxiv:2601.21557` · Agents, open-endedness, AGI · 2026-01-29

- final **+0.03** (conf 1.00, pct 40) · impact +0.07 · WATCH
- mean rating (1–10): **5.5** · accept votes **5/7** · percentile rank_avg 52.7 (100=best) · rank in year 48.0 (1=best)
- NAIPv2 `-0.715` · NAIP-v1 `0.563` · SciJudge `0.788` · DGC-BERT `0.512`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `7.0` Accept · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/3.0) · 14B Fast `5.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2601.21557.md#weaknesses): 1. The paper is not well-organized. The authors should consider reorganizing the paper to make it more coherent and easier to follow. 2. The paper lacks sufficient technical details. The authors should provide more technical details about the proposed method and the experimental setup. 3. The paper lacks sufficient experimental results.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2601.21557.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further consideration. First, while the paper introduces the concept of 'skills' and 'agentic crossover,' it lacks a detailed explanation of how these skills are represented and how the crossover mechanism operates.…

<a id="arxiv-2601.07055"></a>
### Dr. Zero: Self-Evolving Search Agents without Training Data

`arxiv:2601.07055` · Agents, open-endedness, AGI · 2026-01-11

- final **+0.05** (conf 1.00, pct 44) · impact +0.57 · WATCH
- mean rating (1–10): **6.0** · accept votes **5/7** · percentile rank_avg 56.4 (100=best) · rank in year 37.0 (1=best)
- NAIPv2 `-0.861` · NAIP-v1 `0.525` · SciJudge `2.962` · DGC-BERT `0.679`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `5.8` Reject · 7B Fast `6.5` Accept (S/P/C 2.75/3.0/2.75) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/8089](https://t.me/axisofordinary/8089), [axisofordinary/9061](https://t.me/axisofordinary/9061)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2601.07055.md#weaknesses): 1. The paper lacks a detailed description of the methodology, making it difficult to understand the specific techniques used in the framework. 2. The paper does not provide a clear explanation of the advantages of the proposed framework over existing methods. 3. The paper does not discuss the potential limitations of the proposed framework. 4.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2601.07055.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, the paper's novelty is somewhat limited. While the authors introduce HRPO as a key contribution, the underlying concept of using structural similarity to optimize training is not entirely new, as it builds upon the existing GRPO method.…

<a id="arxiv-2601.03192"></a>
### MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory

`arxiv:2601.03192` · Agents, open-endedness, AGI · 2026-01-06

- final **+0.46** (conf 1.00, pct 93) · impact +1.36 · KEEP
- mean rating (1–10): **6.4** · accept votes **6/7** · percentile rank_avg 75.3 (100=best) · rank in year 3.0 (1=best)
- NAIPv2 `1.841` · NAIP-v1 `0.729` · SciJudge `2.547` · DGC-BERT `0.796`
- CycleReviewer 8B `5.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `7.5` Accept (S/P/C 3.25/3.25/3.25) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/8089](https://t.me/axisofordinary/8089), [axisofordinary/9061](https://t.me/axisofordinary/9061)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2601.03192.md#weaknesses): The novelty is limited. The idea of optimizing the retrieval policy via RL is not new, and the method is quite similar to the existing methods (e.g., (1)). The novelty of this work is mainly the application of the idea to LLM agents. - The evaluation is not sufficient. The method is evaluated on only a few benchmarks, and the results are not convincing enough to support the claim of the method.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2601.03192.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further consideration. First, while the paper introduces a memory bank, it lacks a thorough discussion of the memory's capacity limitations and the mechanisms for memory management.…

<a id="arxiv-2512.18746"></a>
### MemEvolve: Meta-Evolution of Agent Memory Systems

`arxiv:2512.18746` · Agents, open-endedness, AGI · 2025-12-21

- final **+0.40** (conf 1.00, pct 88) · impact +0.06 · KEEP
- mean rating (1–10): **6.2** · accept votes **5/7** · percentile rank_avg 60.1 (100=best) · rank in year 34.0 (1=best)
- NAIPv2 `-0.453` · NAIP-v1 `0.626` · SciJudge `-0.532` · DGC-BERT `0.161`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `7.0` Accept · 7B Fast `7.0` Accept (S/P/C 3.0/3.25/3.25) · 14B Fast `6.2` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2512.18746.md#weaknesses): The paper focuses on a specific aspect of LLM-based agents, namely the memory architecture, and does not explore other important aspects such as the LLM itself or the environment interactions. This narrow focus may limit the generalizability of the proposed framework. - The paper does not provide a thorough analysis of the limitations of the proposed framework.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2512.18746.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further attention. First, the paper lacks a detailed explanation of the specific mechanisms used for the 'diagnosis' and 'design' phases within the meta-evolutionary process.…

<a id="arxiv-2512.18552"></a>
### Toward Training Superintelligent Software Agents through Self-Play SWE-RL

`arxiv:2512.18552` · Agents, open-endedness, AGI · 2025-12-21

- final **-0.25** (conf 1.00, pct 17) · impact -0.56 · DROP
- mean rating (1–10): **5.7** · accept votes **3/7** · percentile rank_avg 36.7 (100=best) · rank in year 71.0 (1=best)
- NAIPv2 `-1.922` · NAIP-v1 `0.484` · SciJudge `-0.916` · DGC-BERT `0.233`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `4.8` Reject (S/P/C 2.25/2.75/2.25) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [data_secrets/8572](https://t.me/data_secrets/8572), [axisofordinary/8028](https://t.me/axisofordinary/8028), [axisofordinary/9061](https://t.me/axisofordinary/9061)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2512.18552.md#weaknesses): The paper lacks a clear explanation of the motivation for the proposed method. What are the benefits of self-play SWE-RL (SSR) compared to existing methods? - The paper does not provide a detailed explanation of the experimental setup, including the data used, the evaluation metrics, and the baselines used for comparison.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2512.18552.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. First, the paper's claim of achieving 'superintelligence' appears to be an overstatement based on the presented evidence.…

<a id="arxiv-2512.18160"></a>
### Propose, Solve, Verify: Self-Play Through Formal Verification

`arxiv:2512.18160` · Agents, open-endedness, AGI · 2025-12-20

- final **+0.11** (conf 1.00, pct 53) · impact -0.64 · WATCH
- mean rating (1–10): **6.1** · accept votes **5/7** · percentile rank_avg 53.6 (100=best) · rank in year 46.0 (1=best)
- NAIPv2 `-1.147` · NAIP-v1 `0.551` · SciJudge `-2.947` · DGC-BERT `0.943`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `6.5` Accept (S/P/C 2.75/3.25/2.5) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/8073](https://t.me/axisofordinary/8073), [axisofordinary/9061](https://t.me/axisofordinary/9061)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2512.18160.md#weaknesses): The paper lacks a clear explanation of how the proposer model is trained. The authors mention that the proposer is updated using the data pool, but do not provide details on the training process. - The paper does not provide a clear explanation of how the difficulty-aware proposer works.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2512.18160.md#weaknesses): While I find the paper's contributions to be significant, there are several weaknesses that I have identified through my analysis. First, the paper's reliance on a sound but incomplete verifier introduces a potential bias in the training process. As the authors acknowledge, the Verus verifier may incorrectly reject correct solutions.…

<a id="arxiv-2511.15593"></a>
### What Does It Take to Be a Good AI Research Agent? Studying the Role of Ideation Diversity

`arxiv:2511.15593` · Agents, open-endedness, AGI · 2025-11-19

- final **-0.45** (conf 1.00, pct 7) · impact -1.51 · DROP
- mean rating (1–10): **5.3** · accept votes **2/7** · percentile rank_avg 25.4 (100=best) · rank in year 78.0 (1=best)
- NAIPv2 `-2.432` · NAIP-v1 `0.436` · SciJudge `-5.855` · DGC-BERT `0.401`
- CycleReviewer 8B `6.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.5` Reject · 7B Fast `5.8` Accept (S/P/C 2.75/3.0/2.75) · 14B Fast `4.8` Reject
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `5.0` Accept
- Telegram: [rybolos_channel/1670](https://t.me/rybolos_channel/1670), [gonzo_ML/4261](https://t.me/gonzo_ML/4261), [rybolos_channel/1703](https://t.me/rybolos_channel/1703)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2511.15593.md#weaknesses): The paper only considers a single benchmark (MLE-bench) and a single type of agent (AI research agents). It would be interesting to see if the findings generalize to other benchmarks and types of agents. - The paper does not provide a clear definition of ideation diversity and how it is measured.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2511.15593.md#weaknesses): While the paper presents a compelling case for the importance of ideation diversity, several weaknesses warrant attention. First, the paper's definition of ideation diversity is limited to the distribution of model architectures proposed during the initial planning phase.…

<a id="arxiv-2508.16204"></a>
### Competition and Attraction Improve Model Fusion

`arxiv:2508.16204` · Agents, open-endedness, AGI · 2025-08-22

- final **+0.05** (conf 1.00, pct 46) · impact -1.17 · WATCH
- mean rating (1–10): **5.8** · accept votes **4/7** · percentile rank_avg 47.1 (100=best) · rank in year 63.0 (1=best)
- NAIPv2 `0.670` · NAIP-v1 `0.460` · SciJudge `-3.412` · DGC-BERT `0.853`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.8` Reject · 7B Fast `6.2` Reject (S/P/C 2.75/2.75/2.5) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [data_secrets/7685](https://t.me/data_secrets/7685), [axisofordinary/7621](https://t.me/axisofordinary/7621)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2508.16204.md#weaknesses): 1. The novelty of the proposed method is limited. The idea of model merging using evolutionary algorithms has been explored in previous works (1,2). The proposed method is an extension of these works with some modifications. 2. The experiments are not comprehensive. The proposed method is evaluated on three tasks, but the results are not compared to the state-of-the-art methods on these tasks.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2508.16204.md#weaknesses): While I find the paper to be generally strong, there are several weaknesses that I believe warrant further attention. First, while the paper introduces the concept of dynamically adjusting merging boundaries, the explanation of the split-point parameter, $w_s$, could be more detailed.…

<a id="arxiv-2507.18074"></a>
### AlphaGo Moment for Model Architecture Discovery

`arxiv:2507.18074` · Agents, open-endedness, AGI · 2025-07-24

- final **-0.22** (conf 1.00, pct 19) · impact +1.17 · WATCH
- mean rating (1–10): **5.2** · accept votes **3/7** · percentile rank_avg 41.8 (100=best) · rank in year 68.0 (1=best)
- NAIPv2 `-0.628` · NAIP-v1 `0.658` · SciJudge `3.092` · DGC-BERT `0.119`
- CycleReviewer 8B `5.2` Accept · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `5.0` Reject (S/P/C 2.75/2.75/2.5) · 14B Fast `5.5` Reject
- OpenReviewer `5.0` Reject (S/P/C 2.0/3.0/2.0) · SEA-E `5.0` Accept
- Telegram: [data_secrets/7461](https://t.me/data_secrets/7461), [gonzo_ML/3874](https://t.me/gonzo_ML/3874), [rybolos_channel/1549](https://t.me/rybolos_channel/1549)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2507.18074.md#weaknesses): The paper proposes a framework for neural architecture search using large language models, but it does not provide a detailed evaluation of the framework's performance compared to other neural architecture search methods. The paper also does not provide a detailed analysis of the strengths and weaknesses of the framework, and it does not discuss potential limitations and future work.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2507.18074.md#weaknesses): Despite the ambitious vision and novel approach, several significant weaknesses undermine the paper's claims. First, the paper's claim of a 'fully autonomous' multi-agent system is misleading. While the paper describes distinct modules (Researcher, Engineer, Analyst), these are not separate LLMs but rather different 'agents' within a single LLM, orchestrated through prompt engineering.…

<a id="arxiv-2505.22954"></a>
### Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents

`arxiv:2505.22954` · Agents, open-endedness, AGI · 2025-05-29

- final **+0.05** (conf 1.00, pct 45) · impact +1.12 · WATCH
- mean rating (1–10): **6.0** · accept votes **4/7** · percentile rank_avg 55.9 (100=best) · rank in year 42.0 (1=best)
- NAIPv2 `-0.615` · NAIP-v1 `0.709` · SciJudge `1.749` · DGC-BERT `0.376`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.2` Reject · 7B Fast `5.8` Accept (S/P/C 2.5/2.75/2.25) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [data_secrets/7012](https://t.me/data_secrets/7012), [lovedeathtransformers/9379](https://t.me/lovedeathtransformers/9379), [axisofordinary/7267](https://t.me/axisofordinary/7267), [data_secrets/7688](https://t.me/data_secrets/7688), [gonzo_ML/3681](https://t.me/gonzo_ML/3681), [gonzo_ML/3678](https://t.me/gonzo_ML/3678)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2505.22954.md#weaknesses): The paper proposes a novel approach to self-improving AI systems that uses a combination of evolutionary algorithms and empirical validation to improve its performance on coding benchmarks. However, the paper does not provide a detailed analysis of the limitations of this approach.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2505.22954.md#weaknesses): , is also a strength in that it provides a practical and concrete way to evaluate the performance of the DGM. The use of coding benchmarks allows for a clear and objective assessment of the system's ability to improve itself.…

<a id="doi-10.21203-rs.3.rs-6688473-v1"></a>
### Self-Programming AI: Code-Learning Agents for Autonomous Refactoring and Architectural Evolution

`doi:10.21203/rs.3.rs-6688473/v1` · Agents, open-endedness, AGI · 2025-05-20

- final **-0.72** (conf 1.00, pct 2) · impact -0.31 · DROP
- mean rating (1–10): **4.5** · accept votes **2/7** · percentile rank_avg 19.3 (100=best) · rank in year 79.0 (1=best)
- NAIPv2 `-2.812` · NAIP-v1 `0.604` · SciJudge `-2.305` · DGC-BERT `0.009`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `4.0` Reject · 7B Fast `4.0` Reject (S/P/C 2.25/2.75/1.75) · 14B Fast `3.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `5.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/doi_10.21203_rs.3.rs-6688473_v1.md#weaknesses): 1. The paper lacks a comprehensive literature review. The authors should include more relevant works in the related work section to provide a more thorough background and context for their proposed method. 2. The evaluation is limited to five simple tasks. The authors should consider adding more complex tasks to demonstrate the effectiveness of their method. 3.…
  - [DR-14B Fast](reviews/deepreviewer-14b/doi_10.21203_rs.3.rs-6688473_v1.md#weaknesses): After a thorough examination of the paper, I have identified several significant weaknesses that warrant careful consideration. First, the paper lacks a direct baseline comparison to a one-shot code generation approach. While the authors do compare their iterative approach to a single attempt by the LLM, this is not the same as a dedicated one-shot generation.…

<a id="arxiv-2502.15840"></a>
### Vending-Bench: A Benchmark for Long-Term Coherence of Autonomous Agents

`arxiv:2502.15840` · Agents, open-endedness, AGI · 2025-02-20

- final **-0.30** (conf 1.00, pct 14) · impact -0.26 · DROP
- mean rating (1–10): **4.5** · accept votes **3/7** · percentile rank_avg 31.1 (100=best) · rank in year 77.0 (1=best)
- NAIPv2 `-1.640` · NAIP-v1 `0.395` · SciJudge `1.750` · DGC-BERT `0.032`
- CycleReviewer 8B `1.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.3` Accept (S/P/C 2.67/3.0/2.67) · 14B Fast `4.0` Reject
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [lovedeathtransformers/9266](https://t.me/lovedeathtransformers/9266), [AGI_and_RL/1055](https://t.me/AGI_and_RL/1055)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2502.15840.md#weaknesses): The paper lacks a clear and well-defined research question. The authors do not provide a clear motivation for the benchmark or explain why it is important to test the long-term performance of LLMs. Additionally, the paper does not provide a clear definition of what is meant by "long-term coherence" and how it is measured.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2502.15840.md#weaknesses): Despite its strengths, I have identified several weaknesses in this paper that warrant further discussion. First, while the paper introduces Vending-Bench as a novel benchmark, it lacks a thorough comparison with existing benchmarks for long-term reasoning or agent-based tasks.…

<a id="arxiv-2410.04444"></a>
### Gödel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement

`arxiv:2410.04444` · Agents, open-endedness, AGI · 2024-10-06

- final **-0.05** (conf 1.00, pct 31) · impact +0.03 · WATCH
- mean rating (1–10): **5.6** · accept votes **3/7** · percentile rank_avg 44.7 (100=best) · rank in year 27.0 (1=best)
- NAIPv2 `-1.400` · NAIP-v1 `0.561` · SciJudge `-0.284` · DGC-BERT `0.569`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `5.8` Reject (S/P/C 2.75/2.75/2.5) · 14B Fast `4.2` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [seeallochnaya/1935](https://t.me/seeallochnaya/1935), [gonzo_ML/2964](https://t.me/gonzo_ML/2964), [gonzo_ML/3677](https://t.me/gonzo_ML/3677), [gonzo_ML/2965](https://t.me/gonzo_ML/2965), [knowledge_accumulator/231](https://t.me/knowledge_accumulator/231)
- Weaknesses:
  - [OR-8B](reviews/openreviewer-8b/arxiv_2410.04444.md#weaknesses): 1. The paper does not provide a detailed comparison with other self-improvement methods, such as self-refine, self-debug, and self-correct. 2. The paper does not provide a detailed analysis of the computational resources required for implementing Gödel Agent and the potential scalability issues that may arise when deploying it in larger, real-world scenarios. 3.…

<a id="arxiv-2408.08435"></a>
### Automated Design of Agentic Systems

`arxiv:2408.08435` · Agents, open-endedness, AGI · 2024-08-15

- final **+0.13** (conf 1.00, pct 55) · impact +1.24 · WATCH
- mean rating (1–10): **6.2** · accept votes **4/7** · percentile rank_avg 55.0 (100=best) · rank in year 15.0 (1=best)
- NAIPv2 `-2.412` · NAIP-v1 `0.655` · SciJudge `3.410` · DGC-BERT `0.327`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `5.5` Reject (S/P/C 2.5/3.0/2.5) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [knowledge_accumulator/231](https://t.me/knowledge_accumulator/231)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2408.08435.md#weaknesses): The paper does not provide a detailed analysis of the limitations of the proposed approach. - The paper does not discuss the potential risks and challenges of automating the design of agentic systems. - The paper does not provide a detailed comparison with other approaches to automating the design of agentic systems.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2408.08435.md#weaknesses): While the paper presents a compelling vision for automating the design of agentic systems, several weaknesses warrant careful consideration. First, the paper's use of the term "agent" is broader than some readers might expect.…

<a id="arxiv-2407.00695"></a>
### Learning Formal Mathematics From Intrinsic Motivation

`arxiv:2407.00695` · Agents, open-endedness, AGI · 2024-06-30

- final **+0.43** (conf 1.00, pct 90) · impact -0.28 · KEEP
- mean rating (1–10): **6.4** · accept votes **3/7** · percentile rank_avg 58.5 (100=best) · rank in year 10.0 (1=best)
- NAIPv2 `-0.889` · NAIP-v1 `0.455` · SciJudge `0.660` · DGC-BERT `0.242`
- CycleReviewer 8B `6.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Reject · 7B Fast `5.7` Reject (S/P/C 2.67/2.67/2.67) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/2.0/3.0) · SEA-E `7.0` Accept
- Telegram: [j_links/7590](https://t.me/j_links/7590), [axisofordinary/6466](https://t.me/axisofordinary/6466)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2407.00695.md#weaknesses): The authors claim that their method can generate conjectures and prove them without any prior knowledge. However, the method relies on the type-directed synthesis algorithm to generate conjectures, which requires prior knowledge of the mathematical domain. The authors should clarify this point.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2407.00695.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. Firstly, the paper's approach to conjecture generation, while innovative, appears to be somewhat limited in its exploration of the hypothesis space.…

<a id="arxiv-2406.04268"></a>
### Open-Endedness is Essential for Artificial Superhuman Intelligence

`arxiv:2406.04268` · Agents, open-endedness, AGI · 2024-06-06

- final **-0.25** (conf 1.00, pct 18) · impact +0.33 · DROP
- mean rating (1–10): **5.5** · accept votes **2/7** · percentile rank_avg 36.6 (100=best) · rank in year 38.0 (1=best)
- NAIPv2 `-2.396` · NAIP-v1 `0.614` · SciJudge `0.401` · DGC-BERT `0.008`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.2` Reject · 7B Fast `4.8` Reject (S/P/C 2.75/2.25/2.25) · 14B Fast `4.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/4.0/3.0) · SEA-E `7.0` Accept
- Telegram: [gonzo_ML/2746](https://t.me/gonzo_ML/2746), [gonzo_ML/2743](https://t.me/gonzo_ML/2743), [axisofordinary/6414](https://t.me/axisofordinary/6414), [rybolos_channel/1195](https://t.me/rybolos_channel/1195)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2406.04268.md#weaknesses): The paper does not provide any new experimental results or empirical evidence to support its claims.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2406.04268.md#weaknesses): While I appreciate the paper's attempt to formalize open-endedness, I have identified several weaknesses that I believe significantly impact its overall contribution. First, the paper's definition of open-endedness, while mathematically precise, does not fully capture the essence of the concept as it is commonly understood.…

<a id="arxiv-2402.16823"></a>
### Language Agents as Optimizable Graphs

`arxiv:2402.16823` · Agents, open-endedness, AGI · 2024-02-26

- final **+0.29** (conf 1.00, pct 77) · impact +0.63 · KEEP
- mean rating (1–10): **6.1** · accept votes **3/7** · percentile rank_avg 59.5 (100=best) · rank in year 8.0 (1=best)
- NAIPv2 `0.780` · NAIP-v1 `0.586` · SciJudge `2.168` · DGC-BERT `0.378`
- CycleReviewer 8B `5.8` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.0` Reject (S/P/C 2.67/2.67/2.67) · 14B Fast `5.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [knowledge_accumulator/167](https://t.me/knowledge_accumulator/167), [j_links/7391](https://t.me/j_links/7391), [axisofordinary/6171](https://t.me/axisofordinary/6171), [rybolos_channel/1195](https://t.me/rybolos_channel/1195)
- Weaknesses:
  - [OR-8B](reviews/openreviewer-8b/arxiv_2402.16823.md#weaknesses): 1. The optimization process may be computationally expensive, especially for larger graphs. The paper does not provide a detailed analysis of the computational complexity or runtime of the proposed methods. 2. The evaluation is limited to relatively simple tasks.…

<a id="openreview-pOoKI3ouv1"></a>
### Robust agents learn causal world models (ICLR 2024 best paper)

`openreview:pOoKI3ouv1` · Agents, open-endedness, AGI · unknown

- final **+0.64** (conf 1.00, pct 99) · impact +0.97 · KEEP
- mean rating (1–10): **7.1** · accept votes **6/7** · percentile rank_avg 75.0 (100=best) · rank in year 1.0 (1=best)
- NAIPv2 `-0.457` · NAIP-v1 `0.615` · SciJudge `2.594` · DGC-BERT `0.221`
- CycleReviewer 8B `8.0` Accept · 70B `` 
- DeepReviewer 7B Std `8.0` Accept · 7B Fast `7.0` Accept (S/P/C 3.0/3.0/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/4.0/3.0) · SEA-E `8.0` Accept
- Telegram: [j_links/7476](https://t.me/j_links/7476)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/openreview_pOoKI3ouv1.md#weaknesses): The paper could benefit from more examples and illustrations to help readers understand the concepts and results - The paper could also benefit from a more detailed discussion of the limitations of the results…
  - [DR-14B Fast](reviews/deepreviewer-14b/openreview_pOoKI3ouv1.md#weaknesses): section, the assumptions and scope of the paper limit its direct applicability to real-world scenarios.

<a id="doi-10.1038-s42256-023-00754-x"></a>
### A social path to human-like artificial intelligence

`doi:10.1038/s42256-023-00754-x` · Agents, open-endedness, AGI · 2023-11-17

- final **-0.49** (conf 1.00, pct 6) · impact -1.92 · DROP
- mean rating (1–10): **4.5** · accept votes **1/7** · percentile rank_avg 17.8 (100=best) · rank in year 48.0 (1=best)
- NAIPv2 `-4.184` · NAIP-v1 `0.438` · SciJudge `-10.666` · DGC-BERT `0.050`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.8` Reject · 7B Fast `5.0` Reject (S/P/C 2.0/3.0/2.0) · 14B Fast `5.2` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/2.0/3.0) · SEA-E `3.0` Reject
- Telegram: [dtulinov/647](https://t.me/dtulinov/647)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/doi_10.1038_s42256-023-00754-x.md#weaknesses): The paper is more of a perspective than a research paper, and it is not clear what the main contribution is. - The authors do not provide any concrete examples of how social interactions can be used to improve AI systems. - The paper does not provide a clear roadmap for how to integrate social interactions into AI systems.
  - [DR-14B Fast](reviews/deepreviewer-14b/doi_10.1038_s42256-023-00754-x.md#weaknesses): While the paper presents a compelling argument, several weaknesses limit its overall impact. A primary concern, identified by multiple reviewers, is the lack of concrete examples and specific details to support the central thesis.…

<a id="arxiv-2311.02462"></a>
### Levels of AGI for Operationalizing Progress on the Path to AGI

`arxiv:2311.02462` · Agents, open-endedness, AGI · 2023-11-04

- final **-0.31** (conf 1.00, pct 12) · impact -0.29 · DROP
- mean rating (1–10): **5.5** · accept votes **2/7** · percentile rank_avg 31.2 (100=best) · rank in year 44.0 (1=best)
- NAIPv2 `-2.020` · NAIP-v1 `0.513` · SciJudge `0.306` · DGC-BERT `0.009`
- CycleReviewer 8B `5.8` Reject · 70B `` 
- DeepReviewer 7B Std `4.2` Reject · 7B Fast `4.8` Reject (S/P/C 2.75/2.75/2.25) · 14B Fast `4.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [seeallochnaya/802](https://t.me/seeallochnaya/802), [nn_for_science/1725](https://t.me/nn_for_science/1725), [axisofordinary/5714](https://t.me/axisofordinary/5714), [knowledge_accumulator/241](https://t.me/knowledge_accumulator/241), [gonzo_ML/2744](https://t.me/gonzo_ML/2744)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2311.02462.md#weaknesses): The paper lacks empirical evaluation of the proposed framework. The authors do not provide any empirical results to support the claims made in the paper. The paper is more of a conceptual paper that proposes a framework for classifying AGI models and their precursors. The framework is based on six principles that a useful ontology for AGI should satisfy.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2311.02462.md#weaknesses): , and then propose six principles for a clear and operationalizable definition of AGI. These principles emphasize focusing on capabilities rather than processes, considering both generality and performance, and prioritizing potential over deployment.…

<a id="arxiv-2311.00344"></a>
### A Definition of Open-Ended Learning Problems for Goal-Conditioned Agents

`arxiv:2311.00344` · Agents, open-endedness, AGI · 2023-11-01

- final **-0.09** (conf 1.00, pct 25) · impact -1.59 · WATCH
- mean rating (1–10): **5.5** · accept votes **3/7** · percentile rank_avg 29.9 (100=best) · rank in year 45.0 (1=best)
- NAIPv2 `-1.090` · NAIP-v1 `0.426` · SciJudge `-5.424` · DGC-BERT `0.007`
- CycleReviewer 8B `4.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.2` Reject · 7B Fast `6.5` Accept (S/P/C 3.0/3.0/3.0) · 14B Fast `4.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/2743](https://t.me/gonzo_ML/2743)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2311.00344.md#weaknesses): The paper lacks a clear methodology for evaluating open-ended learning agents and comparing their performance. The authors acknowledge this limitation and suggest that future work should focus on characterizing a goal discovery process and introducing performance measures for various capabilities.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2311.00344.md#weaknesses): While this paper makes a valuable contribution to the field, several weaknesses warrant careful consideration. Firstly, the paper's core definition of open-endedness, while novel in its formalization, lacks sufficient justification and comparison to existing definitions.…

<a id="doi-10.1038-s41586-023-06924-6"></a>
### Mathematical discoveries from program search with large language models

`doi:10.1038/s41586-023-06924-6` · Agents, open-endedness, AGI · 2023-12-14

- final **+0.54** (conf 1.00, pct 97) · impact +0.59 · KEEP
- mean rating (1–10): **6.4** · accept votes **6/7** · percentile rank_avg 61.1 (100=best) · rank in year 9.0 (1=best)
- NAIPv2 `-1.022` · NAIP-v1 `0.500` · SciJudge `3.893` · DGC-BERT `0.193`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `8.0` Accept · 7B Fast `5.7` Accept (S/P/C 3.0/3.0/2.33) · 14B Fast `8.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [seeallochnaya/936](https://t.me/seeallochnaya/936), [nn_for_science/1841](https://t.me/nn_for_science/1841), [j_links/7285](https://t.me/j_links/7285)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/doi_10.1038_s41586-023-06924-6.md#weaknesses): The method relies on a pretrained LLM, which may not be available to all researchers. - The method requires a skeleton program, which may not be available for all problems. - The method requires an efficient evaluator function, which may not be available for all problems. - The method is not applicable to problems that require a proof or a formal verification.
  - [DR-14B Fast](reviews/deepreviewer-14b/doi_10.1038_s41586-023-06924-6.md#weaknesses): While I am impressed with the results, I have identified several weaknesses that warrant further consideration. First, the paper lacks a thorough analysis of the computational cost associated with FunSearch.…

<a id="arxiv-1905.10985"></a>
### AI-GAs: AI-generating algorithms, an alternate paradigm for producing general artificial intelligence

`arxiv:1905.10985` · Agents, open-endedness, AGI · 2019-05-27

- final **-0.28** (conf 1.00, pct 14) · impact -0.34 · DROP
- mean rating (1–10): **4.3** · accept votes **1/7** · percentile rank_avg 25.7 (100=best) · rank in year 4.0 (1=best)
- NAIPv2 `-2.426` · NAIP-v1 `0.621` · SciJudge `-2.343` · DGC-BERT `0.007`
- CycleReviewer 8B `1.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `6.5` Reject (S/P/C 2.75/2.75/2.75) · 14B Fast `3.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `5.0` Reject
- Telegram: [gonzo_ML/450](https://t.me/gonzo_ML/450), [knowledge_accumulator/94](https://t.me/knowledge_accumulator/94), [gonzo_ML/3680](https://t.me/gonzo_ML/3680)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_1905.10985.md#weaknesses): The paper is more of an opinion piece rather than a research paper. It does not provide a clear research question, methodology, or evaluation criteria. The paper does not provide any concrete examples or experiments to support the proposed ideas. The paper is also not well-organized and lacks a clear structure.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_1905.10985.md#weaknesses): Despite its strengths, the paper suffers from several significant weaknesses that limit its overall impact. Firstly, the paper lacks a clear and detailed explanation of how the proposed AI-GA approach would address the core challenges of AI development.…

<a id="arxiv-1901.01753"></a>
### Paired Open-Ended Trailblazer (POET): Endlessly Generating Increasingly Complex and Diverse Learning Environments and Their Solutions

`arxiv:1901.01753` · Agents, open-endedness, AGI · 2019-01-07

- final **-0.02** (conf 1.00, pct 34) · impact -0.33 · WATCH
- mean rating (1–10): **5.3** · accept votes **1/7** · percentile rank_avg 31.6 (100=best) · rank in year 3.0 (1=best)
- NAIPv2 `-1.227` · NAIP-v1 `0.508` · SciJudge `0.300` · DGC-BERT `0.022`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.0` Reject · 7B Fast `5.8` Reject (S/P/C 2.75/2.5/2.5) · 14B Fast `5.8` Reject
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [knowledge_accumulator/98](https://t.me/knowledge_accumulator/98), [gonzo_ML/2744](https://t.me/gonzo_ML/2744)
- Weaknesses:
  - [OR-8B](reviews/openreviewer-8b/arxiv_1901.01753.md#weaknesses): My main concern is the scalability of the proposed method. It seems that the method is only tested in a simple 2-D bipedal-walking obstacle-course domain, which is not convincing enough to show the effectiveness of the proposed method. I would expect the authors to test the proposed method in more complex environments, such as 3-D environments. - The compared baselines are not strong enough.…

<a id="arxiv-2609.01437"></a>
### HarnessDev: Can LLMs Create and Evolve Their Own Agent Harness?

`arxiv:2609.01437` · Harness · 2026-09-01

- final **-0.04** (conf 1.00, pct 32) · impact -0.17 · WATCH
- mean rating (1–10): **6.6** · accept votes **4/7** · percentile rank_avg 51.0 (100=best) · rank in year 51.0 (1=best)
- NAIPv2 `-1.231` · NAIP-v1 `0.617` · SciJudge `-1.916` · DGC-BERT `0.023`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.2` Reject · 7B Fast `6.0` Accept (S/P/C 2.5/2.75/2.75) · 14B Fast `7.0` Accept
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/4.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2609.01437.md#weaknesses): 1. The paper lacks novelty. The idea of evaluating the ability of LLMs to develop their own agent harness is not new, and there have been several previous works on this topic. For example, the Meta-Agent Challenge (Lu et al., 2023) directly evaluates the development ability of LLMs. The paper does not clearly explain why the proposed benchmark is better than these previous works.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2609.01437.md#weaknesses): After a thorough examination of the paper, I have identified several key weaknesses that warrant careful consideration. Firstly, the paper acknowledges the strong coupling between the harness and the executor LLM, a phenomenon often referred to as 'executor-specificity'.…

<a id="arxiv-2606.01770"></a>
### Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System Deployment on Open-Ended Task Streams

`arxiv:2606.01770` · Harness · 2026-06-01

- final **+0.23** (conf 1.00, pct 70) · impact -0.47 · KEEP
- mean rating (1–10): **6.3** · accept votes **5/7** · percentile rank_avg 54.6 (100=best) · rank in year 42.0 (1=best)
- NAIPv2 `0.798` · NAIP-v1 `0.486` · SciJudge `-0.271` · DGC-BERT `0.032`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `7.0` Accept (S/P/C 3.25/3.25/3.25) · 14B Fast `6.7` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2606.01770.md#weaknesses): The paper is mostly focused on the technical details of the proposed framework, but it would be helpful to provide more context on how this work can be applied in real-world scenarios. For example, how can this framework be used in a real-world deployment setting? What are the practical challenges that need to be addressed?
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2606.01770.md#weaknesses): of the system in different contexts. The authors also provide a clear and well-structured presentation of their work, making it easy to follow the logic and understand the key contributions. The use of figures and tables is effective in conveying the experimental results and analyses.…

<a id="arxiv-2604.25850"></a>
### Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses

`arxiv:2604.25850` · Harness · 2026-04-28

- final **+0.08** (conf 1.00, pct 49) · impact -0.21 · WATCH
- mean rating (1–10): **5.9** · accept votes **3/7** · percentile rank_avg 56.7 (100=best) · rank in year 35.0 (1=best)
- NAIPv2 `1.099` · NAIP-v1 `0.507` · SciJudge `0.549` · DGC-BERT `0.459`
- CycleReviewer 8B `5.2` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `4.8` Reject (S/P/C 2.75/2.5/2.5) · 14B Fast `6.5` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2604.25850.md#weaknesses): The paper lacks a clear motivation for the proposed approach. The authors should explain why the three components of AHE are necessary, and how they address the challenges of harness engineering. - The paper lacks a clear explanation of the experimental setup.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2604.25850.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. One significant limitation is the lack of detailed information about the specific prompts used for each agent within the AHE framework.…

<a id="arxiv-2604.19341"></a>
### Structured Scaling of AI Discovery Across Diverse Scientific Domains

`arxiv:2604.19341` · Harness · 2026-04-21

- final **+0.65** (conf 1.00, pct 100) · impact +1.54 · KEEP
- mean rating (1–10): **6.6** · accept votes **6/7** · percentile rank_avg 74.3 (100=best) · rank in year 4.0 (1=best)
- NAIPv2 `-0.211` · NAIP-v1 `0.596` · SciJudge `3.658` · DGC-BERT `0.518`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `10.0` Accept · 7B Fast `8.0` Accept (S/P/C 3.5/3.5/3.5) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses:
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2604.19341.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further consideration. One significant limitation is the lack of a detailed analysis of the computational cost associated with SimpleTES.…
  - [DR-7B Fast](reviews/deepreviewer-7b-fast/arxiv_2604.19341.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, while the paper demonstrates the effectiveness of SimpleTES, it lacks a detailed analysis of the computational cost associated with the method.…

<a id="arxiv-2604.08224"></a>
### Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering

`arxiv:2604.08224` · Harness · 2026-04-09

- final **-0.20** (conf 1.00, pct 21) · impact +1.32 · WATCH
- mean rating (1–10): **5.8** · accept votes **3/7** · percentile rank_avg 49.9 (100=best) · rank in year 54.0 (1=best)
- NAIPv2 `-0.827` · NAIP-v1 `0.681` · SciJudge `3.088` · DGC-BERT `0.030`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `5.2` Reject (S/P/C 3.0/3.0/2.25) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [gonzo_ML/5479](https://t.me/gonzo_ML/5479)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2604.08224.md#weaknesses): The paper does not provide a clear and concise summary of the main contributions of the paper. The abstract and introduction are quite long and do not clearly state the main contributions of the paper.
  - [DR-7B Fast](reviews/deepreviewer-7b-fast/arxiv_2604.08224.md#weaknesses): Despite its strengths, I have identified several weaknesses in this paper that warrant careful consideration. First, while the paper provides a good overview of the field, it lacks a deep dive into the technical details of specific methods.…

<a id="arxiv-2603.28052"></a>
### Meta-Harness: End-to-End Optimization of Model Harnesses

`arxiv:2603.28052` · Harness · 2026-03-30

- final **+0.31** (conf 1.00, pct 79) · impact -0.29 · KEEP
- mean rating (1–10): **6.0** · accept votes **6/7** · percentile rank_avg 60.2 (100=best) · rank in year 29.0 (1=best)
- NAIPv2 `0.213` · NAIP-v1 `0.458` · SciJudge `1.126` · DGC-BERT `0.909`
- CycleReviewer 8B `4.8` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/3.0) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [lovedeathtransformers/10644](https://t.me/lovedeathtransformers/10644), [gonzo_ML/5093](https://t.me/gonzo_ML/5093)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2603.28052.md#weaknesses): The proposed method is limited to the LLM-based coding agent. It is not clear whether the proposed method can be generalized to other types of agents. - The proposed method requires a large amount of memory to store the source code, scores, and execution traces of all prior candidates. It is not clear whether the proposed method can be applied to resource-constrained environments.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2603.28052.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. A primary concern is the limited scope of the experiments regarding the coding agent used for harness optimization.…

<a id="arxiv-2607.23379"></a>
### When Activation Oracles Learn Not to Read: Concept-Specific Blind Spots in Fine-Tuned Oracles

`arxiv:2607.23379` · AI safety and consciousness · 2026-07-25

- final **+0.08** (conf 1.00, pct 49) · impact -0.88 · WATCH
- mean rating (1–10): **6.5** · accept votes **4/7** · percentile rank_avg 51.1 (100=best) · rank in year 50.0 (1=best)
- NAIPv2 `-0.958` · NAIP-v1 `0.502` · SciJudge `-3.607` · DGC-BERT `0.398`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `7.0` Accept (S/P/C 3.0/3.0/3.0) · 14B Fast `7.0` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/4.0/3.0) · SEA-E `6.0` Accept
- Telegram: [dl_stories/1036](https://t.me/dl_stories/1036), [tech_priestess/2709](https://t.me/tech_priestess/2709)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2607.23379.md#weaknesses): The paper only studies a single model architecture (Qwen3-8B) and a single training setup (Taboo Word Guessing). It would be good to see if the findings generalize to other model architectures and training setups. - The paper only studies a single hidden concept (e.g., "leaf") per subject model. It would be good to see if the findings generalize to multiple hidden concepts per subject model.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2607.23379.md#weaknesses): While I find the paper to be generally strong, there are several weaknesses that I believe warrant further discussion. First, the paper's central claim regarding the emergence of concept-specific blind spots in fine-tuned AOs, while intriguing, lacks a clear and convincing explanation.…

<a id="arxiv-2603.19426"></a>
### Is Evaluation Awareness Just Format Sensitivity? Limitations of Probe-Based Evidence under Controlled Prompt Structure

`arxiv:2603.19426` · AI safety and consciousness · 2026-03-19

- final **-0.30** (conf 1.00, pct 13) · impact -1.54 · DROP
- mean rating (1–10): **6.0** · accept votes **5/7** · percentile rank_avg 43.7 (100=best) · rank in year 60.0 (1=best)
- NAIPv2 `-1.178` · NAIP-v1 `0.428` · SciJudge `-3.797` · DGC-BERT `0.848`
- CycleReviewer 8B `6.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `6.2` Accept (S/P/C 2.5/3.0/2.5) · 14B Fast `5.8` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [lovedeathtransformers/10549](https://t.me/lovedeathtransformers/10549)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2603.19426.md#weaknesses): The paper does not provide a clear definition of evaluation awareness, making it difficult to understand the specific phenomenon being studied. - The paper does not provide a clear explanation of why probes are sensitive to format rather than context, and how this sensitivity affects the reliability of probe-based analysis.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2603.19426.md#weaknesses): While I appreciate the contributions of this paper, I have identified several weaknesses that warrant careful consideration. First, the paper's scope is somewhat limited by its reliance on a single LLM backbone, Llama-3.1-8B-Instruct.…

<a id="arxiv-2503.16348"></a>
### Palatable Conceptions of Disembodied Being

`arxiv:2503.16348` · AI safety and consciousness · 2025-03-20

- final **-0.72** (conf 1.00, pct 1) · impact -2.39 · DROP
- mean rating (1–10): **4.4** · accept votes **2/7** · percentile rank_avg 11.9 (100=best) · rank in year 80.0 (1=best)
- NAIPv2 `-4.512` · NAIP-v1 `0.242` · SciJudge `-8.886` · DGC-BERT `0.013`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `3.5` Reject · 7B Fast `4.5` Reject (S/P/C 2.75/2.25/2.25) · 14B Fast `2.5` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/7048](https://t.me/axisofordinary/7048), [gonzo_ML/3491](https://t.me/gonzo_ML/3491)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2503.16348.md#weaknesses): The paper's main weakness is its lack of originality and contribution. The authors draw heavily on existing philosophical theories and concepts, such as Wittgenstein's later philosophy and Buddhist thought, without providing a new or original perspective. The paper also lacks empirical evidence or experimental results to support its claims.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2503.16348.md#weaknesses): Despite its strengths, the paper suffers from several significant weaknesses that undermine its overall impact. A primary concern is the paper's lack of engagement with contemporary discussions in the philosophy of mind, particularly those related to embodied and extended cognition.…

<a id="arxiv-2502.03407"></a>
### Detecting Strategic Deception Using Linear Probes

`arxiv:2502.03407` · AI safety and consciousness · 2025-02-05

- final **-0.40** (conf 1.00, pct 10) · impact +0.23 · DROP
- mean rating (1–10): **5.3** · accept votes **3/7** · percentile rank_avg 35.4 (100=best) · rank in year 73.0 (1=best)
- NAIPv2 `-2.174` · NAIP-v1 `0.558` · SciJudge `1.016` · DGC-BERT `0.056`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `4.2` Reject (S/P/C 2.25/2.75/2.0) · 14B Fast `5.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2502.03407.md#weaknesses): The paper lacks novelty. The authors use existing datasets and methods for training and evaluating their probes. The only novelty seems to be the use of a new model (LLaMA-3.3-70B-Instruct) and the evaluation on additional datasets. However, this is not enough to justify the novelty of the paper. - The authors do not provide a thorough analysis of the limitations of their method.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2502.03407.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. First, the paper's reliance on GPT-4o for labeling the honesty of responses introduces a potential source of error and bias. As the authors acknowledge, this labeling process is not perfect, and there is a risk that the labels themselves are not entirely accurate.…

<a id="arxiv-2501.18837"></a>
### Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming

`arxiv:2501.18837` · AI safety and consciousness · 2025-01-31

- final **+0.13** (conf 1.00, pct 56) · impact +1.12 · WATCH
- mean rating (1–10): **6.4** · accept votes **6/7** · percentile rank_avg 66.6 (100=best) · rank in year 15.0 (1=best)
- NAIPv2 `-1.560` · NAIP-v1 `0.645` · SciJudge `3.193` · DGC-BERT `0.877`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `5.7` Reject (S/P/C 2.67/2.67/2.67) · 14B Fast `6.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/4.0) · SEA-E `6.0` Accept
- Telegram: [data_secrets/6078](https://t.me/data_secrets/6078)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2501.18837.md#weaknesses): The paper does not provide a detailed discussion of the limitations of Constitutional Classifiers. While the paper mentions that the approach is not foolproof and that vulnerabilities may still exist, it does not provide a detailed analysis of the potential limitations and weaknesses of the approach.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2501.18837.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, the paper lacks a detailed analysis of the computational costs associated with the proposed method.…

<a id="arxiv-2309.08600"></a>
### Sparse Autoencoders Find Highly Interpretable Features in Language Models

`arxiv:2309.08600` · AI safety and consciousness · 2023-09-15

- final **+0.09** (conf 1.00, pct 50) · impact -0.02 · WATCH
- mean rating (1–10): **6.2** · accept votes **4/7** · percentile rank_avg 48.6 (100=best) · rank in year 27.0 (1=best)
- NAIPv2 `-1.755` · NAIP-v1 `0.449` · SciJudge `3.106` · DGC-BERT `0.063`
- CycleReviewer 8B `5.2` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `7.0` Accept (S/P/C 3.25/3.25/3.25) · 14B Fast `6.7` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [nn_for_science/1656](https://t.me/nn_for_science/1656)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2309.08600.md#weaknesses): 1. The paper does not provide a clear evaluation of the performance of the learned features compared to other methods. For example, it would be helpful to see a comparison of the interpretability scores of the learned features with those of other methods such as PCA or ICA.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2309.08600.md#weaknesses): While I appreciate the contributions of this paper, my analysis has revealed several weaknesses that warrant careful consideration. Firstly, the paper's claim of novelty, while partially valid, is not as strong as it could be. The authors acknowledge prior work by Yun et al. (2021) and Sharkey et al. (2023) that also use sparse autoencoders for feature learning in language models.…

<a id="arxiv-2308.08708"></a>
### Consciousness in Artificial Intelligence: Insights from the Science of Consciousness

`arxiv:2308.08708` · AI safety and consciousness · 2023-08-17

- final **-0.03** (conf 1.00, pct 33) · impact -0.26 · WATCH
- mean rating (1–10): **6.0** · accept votes **4/7** · percentile rank_avg 37.8 (100=best) · rank in year 40.0 (1=best)
- NAIPv2 `-2.592` · NAIP-v1 `0.605` · SciJudge `-0.845` · DGC-BERT `0.033`
- CycleReviewer 8B `3.5` Reject · 70B `` 
- DeepReviewer 7B Std `3.5` Reject · 7B Fast `6.0` Accept (S/P/C 3.0/2.5/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/4.0) · SEA-E `6.0` Accept
- Telegram: [rybolos_channel/873](https://t.me/rybolos_channel/873), [ai_newz/2126](https://t.me/ai_newz/2126), [dtulinov/626](https://t.me/dtulinov/626), [axisofordinary/5356](https://t.me/axisofordinary/5356)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2308.08708.md#weaknesses): The paper is a report on the current state of the art in the field of artificial consciousness, and it does not provide any new or original contributions. The paper is a summary of existing knowledge in the field, and it does not provide any new insights or perspectives. The paper also does not provide any new or original ideas for future research in the field.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2308.08708.md#weaknesses): While this paper offers a valuable framework for assessing AI consciousness, I have identified several weaknesses that warrant careful consideration. First, the paper's reliance on 'indicator properties' derived from human-centric neuroscientific theories raises concerns about the potential for anthropomorphism.…

<a id="arxiv-2304.06528"></a>
### Power-seeking can be probable and predictive for trained agents

`arxiv:2304.06528` · AI safety and consciousness · 2023-04-13

- final **-0.34** (conf 1.00, pct 10) · impact +0.28 · DROP
- mean rating (1–10): **5.0** · accept votes **3/7** · percentile rank_avg 39.8 (100=best) · rank in year 37.0 (1=best)
- NAIPv2 `-0.491` · NAIP-v1 `0.650` · SciJudge `0.969` · DGC-BERT `0.750`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `2.5` Reject · 7B Fast `4.2` Reject (S/P/C 2.5/2.75/2.25) · 14B Fast `6.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/1475](https://t.me/gonzo_ML/1475), [axisofordinary/4895](https://t.me/axisofordinary/4895)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2304.06528.md#weaknesses): The paper makes several strong assumptions that limit the applicability of the results. For example, it assumes that the agent learns a goal during the training process, and that the learned goal is randomly chosen from the training-compatible goal set. It also assumes that the state and action spaces are finite, and that the rewards are nonnegative.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2304.06528.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. First, the paper's reliance on a high discount factor is a significant limitation. The authors explicitly state that their results depend on the discount factor being sufficiently high, and they even use the limit case of a discount factor approaching 1 in their proofs.…

<a id="arxiv-2303.07103"></a>
### Could a Large Language Model be Conscious?

`arxiv:2303.07103` · AI safety and consciousness · 2023-03-04

- final **-0.25** (conf 0.91, pct 16) · impact +0.69 · WATCH · salvage dr7bf
- mean rating (1–10): **5.9** · accept votes **3/6** · percentile rank_avg 48.5 (100=best) · rank in year 28.0 (1=best)
- NAIPv2 `-2.414` · NAIP-v1 `0.783` · SciJudge `-0.436` · DGC-BERT `0.037`
- CycleReviewer 8B `6.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast ``  (S/P/C 2.5/2.5/2.5) · 14B Fast `3.5` Reject
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/1479](https://t.me/gonzo_ML/1479), [dtulinov/554](https://t.me/dtulinov/554)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2303.07103.md#weaknesses): The paper is more of a philosophical discussion than a scientific paper, and does not provide any empirical evidence to support the author's claims. - The author does not provide a clear definition of consciousness, which makes it difficult to evaluate the claims made in the paper.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2303.07103.md#weaknesses): While the paper offers a valuable philosophical perspective, several weaknesses limit its overall impact and suitability for a venue like ICLR. Firstly, the paper's primary focus on the *can* question of LLM consciousness, while acknowledging the *ought* question, does not sufficiently address the ethical implications of creating conscious AI.…

<a id="arxiv-2206.13477"></a>
### Parametrically Retargetable Decision-Makers Tend To Seek Power

`arxiv:2206.13477` · AI safety and consciousness · 2022-06-27

- final **-0.10** (conf 1.00, pct 25) · impact +1.00 · WATCH
- mean rating (1–10): **5.2** · accept votes **3/7** · percentile rank_avg 49.0 (100=best) · rank in year 12.0 (1=best)
- NAIPv2 `-0.744` · NAIP-v1 `0.739` · SciJudge `2.402` · DGC-BERT `0.269`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.8` Reject · 7B Fast `5.8` Accept (S/P/C 2.5/2.25/2.25) · 14B Fast `4.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [gonzo_ML/1475](https://t.me/gonzo_ML/1475)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2206.13477.md#weaknesses): The paper has several weaknesses that need to be addressed:…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2206.13477.md#weaknesses): Despite its strengths, the paper faces several significant challenges that undermine its overall impact and clarity. One of the primary concerns is the lack of clear articulation of the paper's novel contributions, particularly in the context of reinforcement learning.…

<a id="arxiv-2206.13353"></a>
### Is Power-Seeking AI an Existential Risk?

`arxiv:2206.13353` · AI safety and consciousness · 2022-06-16

- final **+0.01** (conf 1.00, pct 37) · impact +1.25 · WATCH
- mean rating (1–10): **5.8** · accept votes **3/7** · percentile rank_avg 49.6 (100=best) · rank in year 11.0 (1=best)
- NAIPv2 `-0.861` · NAIP-v1 `0.852` · SciJudge `0.681` · DGC-BERT `0.020`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.2` Accept · 7B Fast `6.8` Reject (S/P/C 2.75/2.75/2.75) · 14B Fast `4.8` Reject
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/3.0) · SEA-E `5.0` Accept
- Telegram: [gonzo_ML/1475](https://t.me/gonzo_ML/1475)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2206.13353.md#weaknesses): The paper does not provide a detailed analysis of the six premises and does not provide a clear argument for why they are true. The author assigns subjective probabilities to each premise, but does not provide a clear justification for these probabilities. The paper also does not provide a clear discussion of the potential solutions to the problem of power-seeking AI.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2206.13353.md#weaknesses): Despite its strengths, the paper exhibits several weaknesses that warrant careful consideration. A primary concern, validated by multiple reviewers, is the paper's lack of technical depth and its failure to adequately engage with the practical challenges of AI development.…

<a id="arxiv-1912.01683"></a>
### Optimal Policies Tend to Seek Power

`arxiv:1912.01683` · AI safety and consciousness · 2019-12-03

- final **+0.07** (conf 1.00, pct 47) · impact -0.18 · WATCH
- mean rating (1–10): **5.7** · accept votes **3/7** · percentile rank_avg 44.0 (100=best) · rank in year 2.0 (1=best)
- NAIPv2 `-0.605` · NAIP-v1 `0.415` · SciJudge `2.700` · DGC-BERT `0.705`
- CycleReviewer 8B `3.5` Reject · 70B `` 
- DeepReviewer 7B Std `4.8` Reject · 7B Fast `5.2` Reject (S/P/C 2.5/2.75/2.5) · 14B Fast `5.5` Reject
- OpenReviewer `8.0` Accept (S/P/C 4.0/3.0/4.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/1475](https://t.me/gonzo_ML/1475)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_1912.01683.md#weaknesses): The paper only considers optimal policies in MDPs and does not discuss the implications for learned policies in real-world environments. The authors also do not provide any empirical results or experiments to support their claims.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_1912.01683.md#weaknesses): While this paper presents a valuable theoretical framework, several weaknesses limit its impact and practical relevance. A primary concern is the paper's heavy reliance on a simplified, didactic example—a small grid-world environment—to illustrate its core concepts and theorems. As I observed, the paper introduces the environment of Fig.…

<a id="arxiv-2606.08720"></a>
### This is how the Neocortex Learns

`arxiv:2606.08720` · NeuroAI · 2026-06-07

- final **-0.21** (conf 0.91, pct 19) · impact -1.71 · DROP · partial fulltext
- mean rating (1–10): **6.0** · accept votes **3/7** · percentile rank_avg 35.6 (100=best) · rank in year 68.0 (1=best)
- NAIPv2 `-1.618` · NAIP-v1 `0.485` · SciJudge `-7.365` · DGC-BERT `0.213`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `1.0` Reject · 7B Fast `8.0` Accept (S/P/C 3.67/3.67/3.67) · 14B Fast `3.8` Reject
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/4.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/5565](https://t.me/gonzo_ML/5565)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2606.08720.md#weaknesses): The paper is not a research paper, but rather a review paper. It does not present any new results or findings. The authors do not provide any new insights or perspectives on the topic. The paper is more like a summary of the current state of the art in the field.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2606.08720.md#weaknesses): Despite its strengths, the paper has several verified weaknesses that impact its overall robustness and generalizability. One of the most significant concerns is the paper's reliance on strong conclusions without sufficient empirical evidence. For example, the statement that 'only one current theory ...…

<a id="arxiv-2505.17117"></a>
### From Tokens to Thoughts: How LLMs and Humans Trade Compression for Meaning

`arxiv:2505.17117` · NeuroAI · 2025-05-21

- final **+0.43** (conf 1.00, pct 90) · impact +1.52 · KEEP
- mean rating (1–10): **6.6** · accept votes **7/7** · percentile rank_avg 77.9 (100=best) · rank in year 3.0 (1=best)
- NAIPv2 `-0.097` · NAIP-v1 `0.768` · SciJudge `2.164` · DGC-BERT `0.626`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `8.0` Accept · 7B Fast `7.5` Accept (S/P/C 3.0/3.25/3.25) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [neuroexistencialism/3399](https://t.me/neuroexistencialism/3399)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2505.17117.md#weaknesses): 1. The paper could benefit from a more detailed discussion of the limitations of the Information Bottleneck framework and how it may not fully capture the complexity of human cognition. 2. The paper could benefit from a more detailed discussion of the implications of the findings for the development of LLMs and their applications. 3.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2505.17117.md#weaknesses): While this paper presents a compelling analysis, several weaknesses warrant careful consideration. First, the paper's central claim regarding the trade-off between compression and meaning, while intuitively appealing, lacks sufficient empirical grounding.…

<a id="doi-10.1101-2024.02.22.581686"></a>
### MetaWorm: An Integrative Data-Driven Model Simulating <i>C. elegans</i> Brain, Body and Environment Interactions

`doi:10.1101/2024.02.22.581686` · NeuroAI · 2024-02-26

- final **+0.10** (conf 0.91, pct 52) · impact -0.75 · WATCH · partial fulltext
- mean rating (1–10): **5.7** · accept votes **4/7** · percentile rank_avg 40.1 (100=best) · rank in year 33.0 (1=best)
- NAIPv2 `-2.701` · NAIP-v1 `0.501` · SciJudge `-4.099` · DGC-BERT `0.096`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.0` Reject (S/P/C 2.75/2.5/2.5) · 14B Fast `7.3` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/6364](https://t.me/axisofordinary/6364)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/doi_10.1101_2024.02.22.581686.md#weaknesses): The paper is not well written and lacks clarity. The figures are not self-explanatory and the text is not clear. The authors should provide more details about the methods used to build the model and the results obtained. The authors should also provide more details about the limitations of the model and the future directions for improvement.
  - [DR-14B Fast](reviews/deepreviewer-14b/doi_10.1101_2024.02.22.581686.md#weaknesses): Despite the strengths of this work, I have identified several weaknesses that warrant attention. Firstly, the paper lacks a clear and detailed explanation of how the membrane potential of motor neurons is translated into muscle activation signals.…

<a id="doi-10.1101-2023.04.04.535512"></a>
### Emergence of belief-like representations through reinforcement learning

`doi:10.1101/2023.04.04.535512` · NeuroAI · 2023-04-07

- final **+0.02** (conf 0.91, pct 39) · impact -1.78 · WATCH · partial fulltext
- mean rating (1–10): **6.0** · accept votes **2/7** · percentile rank_avg 37.9 (100=best) · rank in year 39.0 (1=best)
- NAIPv2 `-2.010` · NAIP-v1 `0.301` · SciJudge `-3.736` · DGC-BERT `0.470`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `3.5` Reject · 7B Fast `6.3` Reject (S/P/C 2.67/2.67/2.67) · 14B Fast `6.8` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `7.0` Accept
- Telegram: [axisofordinary/4834](https://t.me/axisofordinary/4834)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/doi_10.1101_2023.04.04.535512.md#weaknesses): 1. The paper is more of a computational neuroscience study, but it does not provide any neuroscience data. The authors should provide experimental data to support their hypothesis.
  - [DR-14B Fast](reviews/deepreviewer-14b/doi_10.1101_2023.04.04.535512.md#weaknesses): While I found the paper to be generally strong, there are several weaknesses that I believe warrant careful consideration. First, the paper lacks a direct comparison of the RNN model with a standard RL agent that uses explicit belief states as input.…

<a id="doi-10.1371-journal.pcbi.1011005"></a>
### Neural spiking for causal inference and learning

`doi:10.1371/journal.pcbi.1011005` · NeuroAI · 2023-04-04

- final **+0.23** (conf 0.82, pct 69) · impact -2.14 · KEEP
- mean rating (1–10): **5.8** · accept votes **4/6** · percentile rank_avg 38.2 (100=best) · rank in year 38.0 (1=best)
- NAIPv2 `-1.458` · NAIP-v1 `0.341` · SciJudge `-8.494` · DGC-BERT `0.122`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std ``  · 7B Fast `6.5` Accept (S/P/C 3.0/3.0/3.0) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [axisofordinary/4763](https://t.me/axisofordinary/4763)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/doi_10.1371_journal.pcbi.1011005.md#weaknesses): The main weakness of the paper is that the results are not convincing. The authors use a very simple model to test their idea, and the results are not convincing. For example, in Fig 3A, the authors show that the spiking discontinuity estimator is unbiased when p is small, but this is not surprising. In fact, if p is too small, the estimator will be very noisy.…
  - [DR-14B Fast](reviews/deepreviewer-14b/doi_10.1371_journal.pcbi.1011005.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. One significant limitation is the lack of a detailed explanation of how the proposed learning rule can be implemented at the synaptic level.…

<a id="doi-10.1371-journal.pcbi.1010628"></a>
### Sleep prevents catastrophic forgetting in spiking neural networks by forming a joint synaptic weight representation

`doi:10.1371/journal.pcbi.1010628` · NeuroAI · 2022-11-18

- final **+0.12** (conf 1.00, pct 54) · impact -1.94 · WATCH
- mean rating (1–10): **6.7** · accept votes **4/7** · percentile rank_avg 42.4 (100=best) · rank in year 14.0 (1=best)
- NAIPv2 `-3.535` · NAIP-v1 `0.377` · SciJudge `-8.708` · DGC-BERT `0.018`
- CycleReviewer 8B `5.2` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `6.7` Accept (S/P/C 3.0/3.0/2.67) · 14B Fast `7.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/doi_10.1371_journal.pcbi.1010628.md#weaknesses): The paper lacks novelty and the results are not surprising. The idea of using sleep to prevent catastrophic forgetting has been explored in previous works, and the authors do not provide any new insights or contributions to this area. The experimental setup is also too simple and does not reflect the complexity of real-world scenarios.…
  - [DR-14B Fast](reviews/deepreviewer-14b/doi_10.1371_journal.pcbi.1010628.md#weaknesses): Despite the paper's strengths, several limitations and areas for improvement have been identified. One of the most significant concerns is the limited exploration of the sleep mechanism's parameters and its generalizability.…

<a id="arxiv-2210.08340"></a>
### Toward Next-Generation Artificial Intelligence: Catalyzing the NeuroAI Revolution

`arxiv:2210.08340` · NeuroAI · 2022-10-15

- final **-0.06** (conf 0.91, pct 30) · impact -1.27 · WATCH · partial fulltext
- mean rating (1–10): **5.2** · accept votes **3/7** · percentile rank_avg 23.3 (100=best) · rank in year 17.0 (1=best)
- NAIPv2 `-3.387` · NAIP-v1 `0.479` · SciJudge `-5.664` · DGC-BERT `0.087`
- CycleReviewer 8B `2.5` Reject · 70B `` 
- DeepReviewer 7B Std `3.0` Reject · 7B Fast `7.0` Accept (S/P/C 3.0/3.25/3.0) · 14B Fast `5.8` Accept
- OpenReviewer `5.0` Reject (S/P/C 2.0/2.0/2.0) · SEA-E `6.0` Accept
- Telegram: [nn_for_science/1135](https://t.me/nn_for_science/1135), [dtulinov/471](https://t.me/dtulinov/471)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2210.08340.md#weaknesses): The paper is more of a call for action than a scientific paper. It does not present any new scientific results or findings. It is more of a position paper or an opinion piece. It is not clear what specific scientific questions the authors are trying to address or what specific challenges they are trying to solve.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2210.08340.md#weaknesses): While I find the paper's overall vision compelling, several weaknesses need to be addressed. Firstly, the paper's proposal of the 'embodied Turing test' as a replacement for the traditional Turing test, while intriguing, lacks a clear justification for its necessity.…

<a id="arxiv-2112.04035"></a>
### Relating transformers to models and neural representations of the hippocampal formation

`arxiv:2112.04035` · NeuroAI · 2021-12-07

- final **+0.01** (conf 0.97, pct 37) · impact -1.10 · WATCH
- mean rating (1–10): **6.1** · accept votes **3/7** · percentile rank_avg 38.2 (100=best) · rank in year 7.0 (1=best)
- NAIPv2 `-1.878` · NAIP-v1 `0.421` · SciJudge `-1.192` · DGC-BERT `0.043`
- CycleReviewer 8B `4.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `6.0` Reject (S/P/C 2.75/2.25/2.5) · 14B Fast `6.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/3.0) · SEA-E `6.0` Accept
- Telegram: [dl_stories/589](https://t.me/dl_stories/589), [axisofordinary/7740](https://t.me/axisofordinary/7740), [nn_for_science/1099](https://t.me/nn_for_science/1099), [boris_again/1275](https://t.me/boris_again/1275)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2112.04035.md#weaknesses): 1. The paper is not well written and the ideas are not well presented. The authors should improve the presentation of their work.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2112.04035.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. One significant concern is the lack of a detailed comparison between the proposed transformer model and the original TEM model, particularly regarding the attractor dynamics.…

<a id="arxiv-2112.03978"></a>
### Attractor and integrator networks in the brain

`arxiv:2112.03978` · NeuroAI · 2021-12-07

- final **+0.14** (conf 1.00, pct 58) · impact +0.00 · WATCH
- mean rating (1–10): **6.2** · accept votes **5/7** · percentile rank_avg 46.1 (100=best) · rank in year 5.0 (1=best)
- NAIPv2 `-2.477` · NAIP-v1 `0.616` · SciJudge `0.607` · DGC-BERT `0.040`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `6.8` Accept (S/P/C 3.5/3.5/2.5) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [dtulinov/468](https://t.me/dtulinov/468)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2112.03978.md#weaknesses): The paper is a review and does not present any new experimental or theoretical results. While it provides a comprehensive overview of the role of attractor dynamics in the brain, it does not provide any new insights or perspectives on the topic.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2112.03978.md#weaknesses): Despite its strengths, the paper has several limitations that could be addressed to enhance its impact and clarity. One of the primary concerns is the lack of a detailed discussion of the limitations of attractor models. While the paper mentions the tradeoff between robustness and capacity, it does not delve into the specific conditions under which attractor networks fail or underperform.…

<a id="doi-10.1038-s41467-021-26568-2"></a>
### Correspondence between neuroevolution and gradient descent

`doi:10.1038/s41467-021-26568-2` · NeuroAI · 2021-11-02

- final **-0.32** (conf 1.00, pct 11) · impact -1.16 · DROP
- mean rating (1–10): **6.0** · accept votes **3/7** · percentile rank_avg 34.6 (100=best) · rank in year 8.0 (1=best)
- NAIPv2 `-2.781` · NAIP-v1 `0.435` · SciJudge `-2.651` · DGC-BERT `0.114`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `4.5` Reject (S/P/C 2.0/2.75/2.0) · 14B Fast `5.8` Reject
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/6807](https://t.me/axisofordinary/6807)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/doi_10.1038_s41467-021-26568-2.md#weaknesses): The paper is missing some important references. For example, there is a line of work studying the connection between gradient descent and evolutionary algorithms, such as (1,2,3). The authors should discuss the relationship between their work and these previous works.
  - [DR-14B Fast](reviews/deepreviewer-14b/doi_10.1038_s41467-021-26568-2.md#weaknesses): Despite its strengths, the paper exhibits several weaknesses that warrant careful consideration. A primary concern, validated by multiple reviewers, is the limited practical applicability of the specific neuroevolution algorithm analyzed.…

<a id="arxiv-2602.14486"></a>
### Revisiting the Platonic Representation Hypothesis: An Aristotelian View

`arxiv:2602.14486` · Representation alignment · 2026-02-16

- final **+0.34** (conf 1.00, pct 82) · impact -1.13 · KEEP
- mean rating (1–10): **7.1** · accept votes **5/7** · percentile rank_avg 66.7 (100=best) · rank in year 12.0 (1=best)
- NAIPv2 `-0.554` · NAIP-v1 `0.528` · SciJudge `-4.424` · DGC-BERT `0.477`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.2` Reject · 7B Fast `6.5` Accept (S/P/C 3.0/3.0/2.5) · 14B Fast `8.0` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [gonzo_ML/5622](https://t.me/gonzo_ML/5622)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2602.14486.md#weaknesses): 1. The paper could benefit from a more thorough discussion of the limitations of the proposed Aristotelian Representation Hypothesis. While the authors acknowledge that representational similarity has no ground-truth scale, they do not provide a clear explanation of how this limitation affects the validity of their findings.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2602.14486.md#weaknesses): Despite its strengths, the paper has several limitations that need to be addressed. One of the primary concerns is the theoretical gap in the justification for the width confounder correction when applied to neighborhood metrics.…

<a id="arxiv-2507.01098"></a>
### Proof of a perfect platonic representation hypothesis

`arxiv:2507.01098` · Representation alignment · 2025-07-01

- final **-0.09** (conf 1.00, pct 26) · impact -2.74 · WATCH
- mean rating (1–10): **5.8** · accept votes **3/7** · percentile rank_avg 33.5 (100=best) · rank in year 75.0 (1=best)
- NAIPv2 `-2.256` · NAIP-v1 `0.222` · SciJudge `-9.175` · DGC-BERT `0.015`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `7.0` Accept · 7B Fast `6.2` Reject (S/P/C 2.5/2.5/2.75) · 14B Fast `6.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [lovedeathtransformers/10956](https://t.me/lovedeathtransformers/10956)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2507.01098.md#weaknesses): 1. The paper's contribution is limited, as it is a note that elaborates on the proof of the PRH for the EDLN model. 2. The paper does not provide any new experimental results or insights that are not already discussed in the original paper by Ziyin et al. (2025). 3. The paper does not discuss the limitations of the EDLN model and how they may affect the validity of the PRH.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2507.01098.md#weaknesses): Despite its strengths, this paper exhibits several weaknesses that warrant careful consideration. A primary concern is the paper's reliance on a simplified model, the embedded deep linear network (EDLN). While the authors acknowledge that this model is a simplification of real-world neural networks, the extent to which the results generalize to nonlinear networks remains unclear.…

<a id="arxiv-2502.15104"></a>
### Estimating Neural Representation Alignment from Sparsely Sampled Inputs and Features

`arxiv:2502.15104` · Representation alignment · 2025-02-20

- final **+0.50** (conf 1.00, pct 95) · impact -0.94 · KEEP
- mean rating (1–10): **6.5** · accept votes **6/7** · percentile rank_avg 66.2 (100=best) · rank in year 16.0 (1=best)
- NAIPv2 `-0.112` · NAIP-v1 `0.555` · SciJudge `-5.736` · DGC-BERT `0.833`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `8.0` Accept · 7B Fast `7.0` Accept (S/P/C 3.25/3.0/3.25) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2502.15104.md#weaknesses): The paper only considers the case where the neural representations are centered. In practice, it is often the case that the neural representations are not centered, and it is not clear how the proposed estimator would perform in this case. - The paper does not provide any theoretical results on the convergence rate of the proposed estimator.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2502.15104.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant attention. First, while the paper introduces a novel estimator for CKA that corrects for biases due to finite sampling of neurons and stimuli, it lacks a thorough discussion of the assumptions underlying the estimator's validity.…

<a id="arxiv-2405.07987"></a>
### The Platonic Representation Hypothesis

`arxiv:2405.07987` · Representation alignment · 2024-05-13

- final **-0.11** (conf 0.82, pct 24) · impact -0.03 · WATCH
- mean rating (1–10): **6.0** · accept votes **3/6** · percentile rank_avg 39.6 (100=best) · rank in year 35.0 (1=best)
- NAIPv2 `-2.098` · NAIP-v1 `0.557` · SciJudge `-0.318` · DGC-BERT `0.039`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std ``  · 7B Fast `5.7` Reject (S/P/C 2.67/2.33/2.67) · 14B Fast `6.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/3.0) · SEA-E `5.0` Accept
- Telegram: [dl_stories/957](https://t.me/dl_stories/957), [boris_again/3487](https://t.me/boris_again/3487), [boris_again/3151](https://t.me/boris_again/3151), [axisofordinary/6337](https://t.me/axisofordinary/6337), [axisofordinary/7502](https://t.me/axisofordinary/7502), [dealerAI/806](https://t.me/dealerAI/806), [lovedeathtransformers/10318](https://t.me/lovedeathtransformers/10318), [boris_again/2579](https://t.me/boris_again/2579)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2405.07987.md#weaknesses): The paper's main weakness is its lack of concrete evidence to support the hypothesis of a shared statistical model of reality. While the authors provide several examples of representation convergence, these examples are largely anecdotal and do not provide a rigorous empirical basis for their hypothesis.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2405.07987.md#weaknesses): While I find the paper's central hypothesis compelling, my analysis has revealed several weaknesses that warrant careful consideration. Firstly, the paper's reliance on the assumption of bijective observation functions is a significant limitation.…

<a id="arxiv-2405.01012"></a>
### Correcting Biased Centered Kernel Alignment Measures in Biological and Artificial Neural Networks

`arxiv:2405.01012` · Representation alignment · 2024-05-02

- final **-0.52** (conf 1.00, pct 6) · impact -1.44 · DROP
- mean rating (1–10): **4.6** · accept votes **1/7** · percentile rank_avg 17.6 (100=best) · rank in year 47.0 (1=best)
- NAIPv2 `-1.223` · NAIP-v1 `0.264` · SciJudge `-2.373` · DGC-BERT `0.024`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `4.2` Reject · 7B Fast `3.5` Reject (S/P/C 2.0/2.5/2.0) · 14B Fast `4.0` Reject
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2405.01012.md#weaknesses): 1. The paper is written in a way that is hard to follow. For example, the abstract and introduction are not clear about the main contributions of the paper. The abstract states that the paper highlights issues with the use of CKA as an alignment metric, but it does not clearly state what these issues are.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2405.01012.md#weaknesses): While I appreciate the paper's contributions, I have identified several weaknesses that warrant careful consideration. First, the paper's primary limitation is its incremental nature. As the authors acknowledge, the core methods, including CKA, RSA, and the THINGS dataset, are not novel.…

<a id="arxiv-2007.02789"></a>
### Comparing representational geometries using whitened unbiased-distance-matrix similarity

`arxiv:2007.02789` · Representation alignment · 2020-07-06

- final **+0.71** (conf 1.00, pct 100) · impact -2.01 · KEEP
- mean rating (1–10): **6.8** · accept votes **5/7** · percentile rank_avg 57.9 (100=best) · rank in year 6.0 (1=best)
- NAIPv2 `-0.351` · NAIP-v1 `0.339` · SciJudge `-4.951` · DGC-BERT `0.388`
- CycleReviewer 8B `5.5` Reject · 70B `` 
- DeepReviewer 7B Std `7.5` Accept · 7B Fast `6.5` Accept (S/P/C 3.0/3.0/3.25) · 14B Fast `8.0` Accept
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/4.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2007.02789.md#weaknesses): The paper is not well written and is difficult to follow. The authors should consider revising the paper to make it more accessible to a broader audience.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2007.02789.md#weaknesses): While I found the paper to be generally strong, there are several weaknesses that I believe warrant further attention. First, while the paper provides a clear rationale for using unbiased distance estimates, the explanation of when and why to use them could be more explicit.…

<a id="acl-2025.acl-long.126"></a>
### INVESTORBENCH: A Benchmark for Financial Decision-Making Tasks with LLM-based Agent

`acl:2025.acl-long.126` · Finance · unknown

- final **-0.18** (conf 0.91, pct 21) · impact -0.08 · WATCH · partial fulltext
- mean rating (1–10): **5.6** · accept votes **2/7** · percentile rank_avg 40.5 (100=best) · rank in year 5.0 (1=best)
- NAIPv2 `-2.904` · NAIP-v1 `0.557` · SciJudge `0.149` · DGC-BERT `0.468`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `6.0` Reject (S/P/C 2.5/2.75/2.5) · 14B Fast `4.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [rybolos_channel/1561](https://t.me/rybolos_channel/1561)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/acl_2025.acl-long.126.md#weaknesses): 1. The paper lacks a clear evaluation of the proposed benchmark. The authors only provide a brief description of the benchmark and its components, but do not provide a comprehensive evaluation of its effectiveness or limitations. 2. The paper does not provide a clear comparison of the proposed benchmark with existing benchmarks for evaluating LLMs for financial decision-making tasks.…
  - [DR-14B Fast](reviews/deepreviewer-14b/acl_2025.acl-long.126.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. First, the paper lacks a detailed explanation of the memory architecture's implementation.…

<a id="arxiv-2003.01859"></a>
### Applications of deep learning in stock market prediction: recent progress

`arxiv:2003.01859` · Finance · 2020-02-29

- final **-0.72** (conf 1.00, pct 1) · impact +0.27 · DROP
- mean rating (1–10): **4.3** · accept votes **1/7** · percentile rank_avg 20.4 (100=best) · rank in year 10.0 (1=best)
- NAIPv2 `-6.262` · NAIP-v1 `0.747` · SciJudge `-3.593` · DGC-BERT `0.028`
- CycleReviewer 8B `4.6` Reject · 70B `` 
- DeepReviewer 7B Std `1.0` Reject · 7B Fast `3.0` Reject (S/P/C 2.0/2.0/1.67) · 14B Fast `3.0` Reject
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2003.01859.md#weaknesses): The paper is a survey of the literature on deep learning for stock market prediction, and does not provide any new insights or contributions to the field. The paper is also quite long, and could be condensed to make it more concise.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2003.01859.md#weaknesses): . The paper's attempt to provide a comprehensive overview of the field is commendable, but the lack of depth and critical analysis limits its overall impact.

<a id="arxiv-1807.02787"></a>
### Financial Trading as a Game: A Deep Reinforcement Learning Approach

`arxiv:1807.02787` · Finance · 2018-07-08

- final **-0.74** (conf 1.00, pct 1) · impact -1.93 · DROP
- mean rating (1–10): **3.2** · accept votes **1/7** · percentile rank_avg 7.5 (100=best) · rank in year 4.0 (1=best)
- NAIPv2 `-4.266` · NAIP-v1 `0.237` · SciJudge `-3.517` · DGC-BERT `0.592`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `2.0` Reject · 7B Fast `4.0` Reject (S/P/C 2.25/2.25/2.25) · 14B Fast `3.0` Reject
- OpenReviewer `3.0` Reject (S/P/C 2.0/2.0/2.0) · SEA-E `3.0` Reject
- Telegram: —
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_1807.02787.md#weaknesses): The paper is poorly written and the results are not convincing. The authors do not provide enough details about the data they used and the evaluation metrics they used to evaluate their method. The authors also do not compare their method with other state-of-the-art methods for trading in the foreign exchange market.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_1807.02787.md#weaknesses): While this paper presents a promising application of deep reinforcement learning to financial trading, several weaknesses limit its overall impact and generalizability. One of the primary concerns is the lack of a comprehensive related work section.…

<a id="arxiv-1706.10059"></a>
### A Deep Reinforcement Learning Framework for the Financial Portfolio Management Problem

`arxiv:1706.10059` · Finance · 2017-06-30

- final **-0.65** (conf 1.00, pct 3) · impact -2.21 · DROP
- mean rating (1–10): **3.8** · accept votes **0/7** · percentile rank_avg 3.0 (100=best) · rank in year 8.0 (1=best)
- NAIPv2 `-5.109` · NAIP-v1 `0.235` · SciJudge `-5.784` · DGC-BERT `0.003`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `1.0` Reject · 7B Fast `4.0` Reject (S/P/C 2.25/2.5/2.5) · 14B Fast `4.0` Reject
- OpenReviewer `3.0` Reject (S/P/C 2.0/2.0/2.0) · SEA-E `5.0` Reject
- Telegram: [j_links/374](https://t.me/j_links/374)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_1706.10059.md#weaknesses): The paper lacks novelty. The proposed framework is a combination of existing techniques and the novelty is limited. The paper also lacks theoretical analysis and the experiments are not convincing.
  - [DR-7B Fast](reviews/deepreviewer-7b-fast/arxiv_1706.10059.md#weaknesses): Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. Firstly, the paper lacks a comprehensive comparison with existing state-of-the-art reinforcement learning methods for portfolio management. While the authors mention some related works, they do not provide a detailed comparison of their method's performance against these alternatives.…

<a id="arxiv-2201.09746"></a>
### Reinforcement Learning Textbook

`arxiv:2201.09746` · Books · 2022-01-19

- final **-0.59** (conf 0.62, pct 4) · impact -0.58 · DROP · partial fulltext
- mean rating (1–10): **4.5** · accept votes **1/7** · percentile rank_avg 21.1 (100=best) · rank in year 18.0 (1=best)
- NAIPv2 `-4.305` · NAIP-v1 `0.616` · SciJudge `-4.059` · DGC-BERT `0.034`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `3.0` Reject · 7B Fast `5.0` Reject (S/P/C 3.0/3.0/2.0) · 14B Fast `3.8` Reject
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `3.0` Reject
- Telegram: [AGI_and_RL/1168](https://t.me/AGI_and_RL/1168), [AGI_and_RL/734](https://t.me/AGI_and_RL/734), [AGI_and_RL/278](https://t.me/AGI_and_RL/278), [AGI_and_RL/891](https://t.me/AGI_and_RL/891), [MLResearch/870](https://t.me/MLResearch/870)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2201.09746.md#weaknesses): The paper is a survey paper, and it does not have any technical contribution.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2201.09746.md#weaknesses): in clarity, organization, and writing quality hinder its overall impact and accessibility.

<a id="arxiv-2201.00650"></a>
### Deep Learning Interviews: Hundreds of fully solved job interview questions from a wide range of key topics in AI

`arxiv:2201.00650` · Books · 2021-12-30

- final **-0.83** (conf 0.43, pct 0) · impact -1.39 · WATCH · partial fulltext
- mean rating (1–10): **4.0** · accept votes **0/5** · percentile rank_avg 12.9 (100=best) · rank in year 12.0 (1=best)
- NAIPv2 `-3.359` · NAIP-v1 `0.475` · SciJudge `-7.691` · DGC-BERT `0.011`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std ``  · 7B Fast `1.0` Reject (S/P/C 1.0/1.0/1.0) · 14B Fast `` 
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `5.0` Reject
- Telegram: [AIHOUSE/260](https://t.me/AIHOUSE/260), [AIHOUSE/19](https://t.me/AIHOUSE/19), [MLResearch/860](https://t.me/MLResearch/860), [tech_priestess/611](https://t.me/tech_priestess/611)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2201.00650.md#weaknesses): The paper does not provide any insights into the performance of AI models on these questions. - The paper does not provide any insights into the limitations of the dataset or the framework.
  - [DR-7B Fast](reviews/deepreviewer-7b-fast/arxiv_2201.00650.md#weaknesses): . * **Strengths (if any):** Specific positive aspects of the paper. * **Weaknesses (if any):** Specific negative aspects of the paper. * **Suggestions for Improvement:** Concrete recommendations to enhance the paper. * **Conclusion:** A final assessment of the paper's value and impact.

<a id="doi-10.1038-s41566-024-01394-2"></a>
### Inverse-designed low-index-contrast structures on a silicon photonics platform for vector–matrix multiplication

`doi:10.1038/s41566-024-01394-2` · Other · 2024-02-16

- final **-0.13** (conf 0.82, pct 23) · impact -1.61 · WATCH
- mean rating (1–10): **5.5** · accept votes **2/6** · percentile rank_avg 20.8 (100=best) · rank in year 46.0 (1=best)
- NAIPv2 `-3.393` · NAIP-v1 `0.338` · SciJudge `-4.581` · DGC-BERT `0.020`
- CycleReviewer 8B `4.8` Reject · 70B `` 
- DeepReviewer 7B Std ``  · 7B Fast `5.2` Reject (S/P/C 3.0/3.0/2.25) · 14B Fast `6.5` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/2688](https://t.me/gonzo_ML/2688)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/doi_10.1038_s41566-024-01394-2.md#weaknesses): 1. The paper is a review paper, which is not suitable for ICLR.
  - [DR-14B Fast](reviews/deepreviewer-14b/doi_10.1038_s41566-024-01394-2.md#weaknesses): Despite the paper's strengths, several limitations and gaps in the review are evident. One significant issue is the lack of a detailed discussion on the practical challenges of implementing photonic matrix multiplication, particularly concerning thermal management, fabrication tolerances, and integration with electronic components.…

<a id="arxiv-2309.10232"></a>
### Fully parallel optical matrix-matrix multiplication

`arxiv:2309.10232` · Other · 2023-09-19

- final **-0.77** (conf 1.00, pct 0) · impact -1.90 · DROP
- mean rating (1–10): **3.2** · accept votes **0/7** · percentile rank_avg 5.5 (100=best) · rank in year 50.0 (1=best)
- NAIPv2 `-4.305` · NAIP-v1 `0.365` · SciJudge `-7.551` · DGC-BERT `0.022`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `3.5` Reject · 7B Fast `2.5` Reject (S/P/C 1.5/1.5/1.5) · 14B Fast `4.8` Reject
- OpenReviewer `3.0` Reject (S/P/C 2.0/2.0/2.0) · SEA-E `3.0` Reject
- Telegram: [gonzo_ML/2688](https://t.me/gonzo_ML/2688)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2309.10232.md#weaknesses): The authors do not provide any experimental results to support their claims. The paper only provides a theoretical analysis of the proposed method and its potential applications in optical neural networks.
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2309.10232.md#weaknesses): After a thorough examination of the paper, I have identified several weaknesses that warrant careful consideration. Firstly, the paper lacks a detailed discussion of the practical limitations of the proposed architecture. While the authors mention the use of spatial light modulators (SLMs), they do not delve into the specific constraints imposed by these devices.…

<a id="arxiv-2304.01433"></a>
### TPU v4: An Optically Reconfigurable Supercomputer for Machine Learning with Hardware Support for Embeddings

`arxiv:2304.01433` · Other · 2023-04-04

- final **+0.02** (conf 0.74, pct 40) · impact +0.27 · WATCH · partial fulltext
- mean rating (1–10): **6.8** · accept votes **3/6** · percentile rank_avg 52.3 (100=best) · rank in year 21.0 (1=best)
- NAIPv2 `-1.127` · NAIP-v1 `0.679` · SciJudge `-0.281` · DGC-BERT `0.010`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `3.0` Reject · 7B Fast ``  (S/P/C None/None/None) · 14B Fast `5.2` Reject
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/3.0) · SEA-E `8.0` Accept
- Telegram: [techsparks/3989](https://t.me/techsparks/3989), [j_links/6618](https://t.me/j_links/6618), [axisofordinary/4738](https://t.me/axisofordinary/4738), [gonzo_ML/2688](https://t.me/gonzo_ML/2688)
- Weaknesses:
  - [CR-8B](reviews/cyclereviewer-8b/arxiv_2304.01433.md#weaknesses): 1. The paper is not well-organized. The authors should focus on the main contributions and highlight the main contributions in the introduction. 2. The paper does not provide enough details about the TPU v4 architecture. The authors should provide more details about the TPU v4 architecture, including the number of cores, the clock speed, the memory bandwidth, and the power consumption. 3.…
  - [DR-14B Fast](reviews/deepreviewer-14b/arxiv_2304.01433.md#weaknesses): While the paper presents a compelling narrative of the TPU v4 system, several weaknesses warrant careful consideration. One significant limitation lies in the lack of detailed analysis regarding the optical circuit switch (OCS).…

