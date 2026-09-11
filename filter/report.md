# Paper quality scores

319 readme papers (web/repo skipped). 319 have at least one Accept/Reject vote.

Ratings of well-known older papers (Llama 3, DeepSeekMath, DAPO, …) can be inflated: those works appear in Llama-3.1 / Qwen3 / Phi-4 pretraining. Rank **within year** when comparing.

## Model coverage

| model | n scored |
|---|---:|
| NAIPv2 | 319 |
| NAIP-v1 | 319 |
| SciJudge BT | 319 |
| DGC-BERT p(accept) | 319 |
| CycleReviewer-8B | 319 |
| CycleReviewer-70B | 0 |
| DeepReviewer-7B Standard | 310 |
| DeepReviewer-7B Fast | 307 |
| DeepReviewer-14B Fast | 317 |
| OpenReviewer-8B | 319 |
| SEA-E | 319 |

## DeepReviewer-7B Fast vs Standard

Intersection n=301. Spearman `0.374`. Accept/Reject macro-F1 `0.604` (n=301). Standard is a partial run; Fast is the column used in mean_rating10 / rank_avg.

## Self-agreement (seed 0 vs seed 1)

| model | n | Spearman | macro-F1 |
|---|---:|---:|---:|
| CR-8B | 51 | 0.512 | 0.648 |
| DR-14B Fast | 51 | 0.742 | 0.753 |


## Aggregation

Hierarchical factor score on quality families (citation/impact held out). `final_score` is in [-1, 1]. 0 is where reviewer Accept/Reject votes split 50/50 among families whose accept rate is in (0.1, 0.9) (now `['cr8b', 'deep', 'dgcbert', 'naipv2', 'or8b']`). `accepts/models` on badges are raw reviewer votes, not this score. VERDICT: DROP if score < -0.2 and conf >= 0.5 and impact_z < 0.5; WATCH if missing impact, conf < 0.5, or |score| <= 0.2; else KEEP.

Calibration `sigmoid(1.577 q + 0.081)`; share of papers with final_score > 0: `0.618`. VERDICT KEEP/WATCH/DROP = `{'WATCH': 131, 'KEEP': 121, 'DROP': 67}`.

Family accept rates used for `CAL_VOTE_RANGE`: CR-8B 0.232, DeepReviewer 0.556, DGC-BERT 0.520, NAIPv2 0.502, OR-8B 0.809, SEA-E 0.934. In target: `['cr8b', 'deep', 'dgcbert', 'naipv2', 'or8b']`.

| family | λ | w | PC1 |
|---|---:|---:|---:|
| NAIPv2 | 0.579 | 0.505 | 0.693 |
| DeepReviewer | 0.753 | 1.313 | 0.779 |
| CR-8B | 0.361 | 0.150 | 0.504 |
| OR-8B | 0.315 | 0.110 | 0.447 |
| SEA-E | 0.484 | 0.306 | 0.627 |
| DGC-BERT | 0.330 | 0.122 | 0.455 |

| model | LOFO rho vs other families | salvage |
|---|---:|---:|
| NAIPv2 | 0.436 | 0 |
| NAIP-v1 | 0.459 | 0 |
| SciJudge | 0.459 | 0 |
| DGC-BERT | 0.244 | 0 |
| CR-8B | 0.272 | 0 |
| DR-7B Std | 0.400 | 0 |
| DR-7B Fast | 0.405 | 6 |
| DR-14B Fast | 0.445 | 0 |
| OR-8B | 0.195 | 0 |
| SEA-E | 0.348 | 0 |

Family clusters at rho>=0.35: deep+naipv2, cr8b, or8b, seae, dgcbert. At rho>=0.25: deep+naipv2+seae, cr8b, or8b, dgcbert. Model clusters at rho>=0.35: dr14b+naipv2, naipv1+scijudge, dgcbert, cr8b, dr7b+dr7bf, or8b, seae. At rho>=0.25: dr14b+dr7b+dr7bf+naipv2, naipv1+scijudge, dgcbert, cr8b, or8b+seae.

| model | field | n | rho vs other families |
|---|---|---:|---:|
| CR-8B | rating | 319 | 0.261 |
| CR-8B | contribution | 319 | 0.272 |
| CR-8B | soundness | 319 | 0.234 |
| CR-8B | presentation | 319 | 0.141 |
| DR-7B Std | rating | 310 | 0.382 |
| DR-7B Std | contribution | 310 | 0.387 |
| DR-7B Std | soundness | 310 | 0.313 |
| DR-7B Std | presentation | 310 | 0.329 |
| DR-7B Fast | rating | 307 | 0.359 |
| DR-7B Fast | contribution | 312 | 0.355 |
| DR-7B Fast | soundness | 312 | 0.297 |
| DR-7B Fast | presentation | 312 | 0.338 |
| DR-14B Fast | rating | 317 | 0.386 |
| DR-14B Fast | contribution | 317 | 0.472 |
| DR-14B Fast | soundness | 317 | 0.461 |
| DR-14B Fast | presentation | 317 | 0.344 |
| OR-8B | rating | 319 | 0.187 |
| OR-8B | contribution | 319 | 0.224 |
| OR-8B | soundness | 319 | 0.081 |
| OR-8B | presentation | 319 | 0.152 |
| SEA-E | rating | 319 | 0.343 |
| SEA-E | contribution | 319 | 0.238 |
| SEA-E | soundness | 319 | 0.158 |
| SEA-E | presentation | 319 | 0.092 |

| model | subset | n | mean consensus z |
|---|---|---:|---:|
| CR-8B | parsed | 319 | -0.001 |
| CR-8B | unparsed | 0 |  |
| DR-7B Std | parsed | 310 | 0.025 |
| DR-7B Std | unparsed | 9 | -0.877 |
| DR-7B Fast | parsed | 307 | 0.014 |
| DR-7B Fast | unparsed | 12 | -0.364 |
| DR-14B Fast | parsed | 317 | 0.009 |
| DR-14B Fast | unparsed | 2 | -1.524 |
| OR-8B | parsed | 319 | -0.001 |
| OR-8B | unparsed | 0 |  |
| SEA-E | parsed | 319 | -0.001 |
| SEA-E | unparsed | 0 |  |

Remaining unparsed reviews after retry are shifted down (DR-7B Std n=9, consensus z=-0.877; DR-7B Fast n=12, consensus z=-0.364; DR-14B Fast n=2, consensus z=-1.524). No reject-imputation; those papers already get signal from other families.


## Agreement (Spearman)

| model A | model B | n | Spearman |
|---|---|---:|---:|
| NAIPv2 | NAIP-v1 | 319 | 0.249 |
| NAIPv2 | SciJudge | 319 | 0.426 |
| NAIPv2 | DGC-BERT | 319 | 0.329 |
| NAIPv2 | CR-8B | 319 | 0.168 |
| NAIPv2 | CR-70B | 0 |  |
| NAIPv2 | DR-7B Std | 310 | 0.402 |
| NAIPv2 | DR-7B Fast | 307 | 0.316 |
| NAIPv2 | DR-14B Fast | 317 | 0.485 |
| NAIPv2 | OR-8B | 319 | 0.220 |
| NAIPv2 | SEA-E | 319 | 0.333 |
| NAIP-v1 | SciJudge | 319 | 0.487 |
| NAIP-v1 | DGC-BERT | 319 | 0.125 |
| NAIP-v1 | CR-8B | 319 | 0.215 |
| NAIP-v1 | CR-70B | 0 |  |
| NAIP-v1 | DR-7B Std | 310 | 0.129 |
| NAIP-v1 | DR-7B Fast | 307 | 0.153 |
| NAIP-v1 | DR-14B Fast | 317 | 0.105 |
| NAIP-v1 | OR-8B | 319 | 0.118 |
| NAIP-v1 | SEA-E | 319 | 0.114 |
| SciJudge | DGC-BERT | 319 | 0.406 |
| SciJudge | CR-8B | 319 | 0.333 |
| SciJudge | CR-70B | 0 |  |
| SciJudge | DR-7B Std | 310 | 0.248 |
| SciJudge | DR-7B Fast | 307 | 0.219 |
| SciJudge | DR-14B Fast | 317 | 0.341 |
| SciJudge | OR-8B | 319 | 0.256 |
| SciJudge | SEA-E | 319 | 0.332 |
| DGC-BERT | CR-8B | 319 | 0.101 |
| DGC-BERT | CR-70B | 0 |  |
| DGC-BERT | DR-7B Std | 310 | 0.216 |
| DGC-BERT | DR-7B Fast | 307 | 0.191 |
| DGC-BERT | DR-14B Fast | 317 | 0.198 |
| DGC-BERT | OR-8B | 319 | -0.053 |
| DGC-BERT | SEA-E | 319 | 0.137 |
| CR-8B | CR-70B | 0 |  |
| CR-8B | DR-7B Std | 310 | 0.233 |
| CR-8B | DR-7B Fast | 307 | 0.168 |
| CR-8B | DR-14B Fast | 317 | 0.219 |
| CR-8B | OR-8B | 319 | 0.122 |
| CR-8B | SEA-E | 319 | 0.171 |
| CR-70B | DR-7B Std | 0 |  |
| CR-70B | DR-7B Fast | 0 |  |
| CR-70B | DR-14B Fast | 0 |  |
| CR-70B | OR-8B | 0 |  |
| CR-70B | SEA-E | 0 |  |
| DR-7B Std | DR-7B Fast | 301 | 0.374 |
| DR-7B Std | DR-14B Fast | 310 | 0.377 |
| DR-7B Std | OR-8B | 310 | 0.230 |
| DR-7B Std | SEA-E | 310 | 0.292 |
| DR-7B Fast | DR-14B Fast | 306 | 0.314 |
| DR-7B Fast | OR-8B | 307 | 0.231 |
| DR-7B Fast | SEA-E | 307 | 0.287 |
| DR-14B Fast | OR-8B | 317 | 0.265 |
| DR-14B Fast | SEA-E | 317 | 0.243 |
| OR-8B | SEA-E | 319 | 0.232 |

## Agreement (macro-F1 Accept/Reject)

| model A | model B | n | macro-F1 |
|---|---|---:|---:|
| DGC-BERT | CR-8B | 319 | 0.452 |
| DGC-BERT | CR-70B | 0 |  |
| DGC-BERT | DR-7B Std | 310 | 0.561 |
| DGC-BERT | DR-7B Fast | 307 | 0.573 |
| DGC-BERT | DR-14B Fast | 317 | 0.573 |
| DGC-BERT | OR-8B | 319 | 0.452 |
| DGC-BERT | SEA-E | 319 | 0.431 |
| CR-8B | CR-70B | 0 |  |
| CR-8B | DR-7B Std | 310 | 0.532 |
| CR-8B | DR-7B Fast | 307 | 0.479 |
| CR-8B | DR-14B Fast | 317 | 0.438 |
| CR-8B | OR-8B | 319 | 0.347 |
| CR-8B | SEA-E | 319 | 0.271 |
| CR-70B | DR-7B Std | 0 |  |
| CR-70B | DR-7B Fast | 0 |  |
| CR-70B | DR-14B Fast | 0 |  |
| CR-70B | OR-8B | 0 |  |
| CR-70B | SEA-E | 0 |  |
| DR-7B Std | DR-7B Fast | 301 | 0.604 |
| DR-7B Std | DR-14B Fast | 310 | 0.589 |
| DR-7B Std | OR-8B | 310 | 0.527 |
| DR-7B Std | SEA-E | 310 | 0.407 |
| DR-7B Fast | DR-14B Fast | 306 | 0.645 |
| DR-7B Fast | OR-8B | 307 | 0.553 |
| DR-7B Fast | SEA-E | 307 | 0.499 |
| DR-14B Fast | OR-8B | 317 | 0.571 |
| DR-14B Fast | SEA-E | 317 | 0.540 |
| OR-8B | SEA-E | 319 | 0.636 |

## Ranking by readme section

### Reinforcement learning

| rank | title | year | final | accept | key |
|---:|---|---|---:|---:|---|
| 1 | [First return, then explore](#arxiv-2004.12919) | 2020 | +0.68 | 6/7 | `arxiv:2004.12919` |
| 2 | [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](#arxiv-1801.01290) | 2018 | +0.52 | 6/7 | `arxiv:1801.01290` |
| 3 | [Deep Neuroevolution: Genetic Algorithms Are a Competitive Alternative for Training Deep Neural Networks for Reinforcement Learning](#arxiv-1712.06567) | 2017 | +0.45 | 4/7 | `arxiv:1712.06567` |
| 4 | [A Distributional Perspective on Reinforcement Learning](#arxiv-1707.06887) | 2017 | +0.38 | 6/7 | `arxiv:1707.06887` |
| 5 | [The Primacy Bias in Deep Reinforcement Learning](#arxiv-2205.07802) | 2022 | +0.35 | 6/7 | `arxiv:2205.07802` |
| 6 | [Bigger, Better, Faster: Human-level Atari with human-level efficiency](#arxiv-2305.19452) | 2023 | +0.28 | 3/7 | `arxiv:2305.19452` |
| 7 | [Mastering Diverse Domains through World Models](#arxiv-2301.04104) | 2023 | +0.19 | 5/7 | `arxiv:2301.04104` |
| 8 | [Sample-Efficient RL by Breaking the Replay Ratio Barrier (ICLR 2023, precursor of BBF)](#openreview-OpC-9aBBVJe) | unknown | +0.18 | 6/7 | `openreview:OpC-9aBBVJe` |
| 9 | [Beyond The Rainbow: High Performance Deep Reinforcement Learning on a Desktop PC](#arxiv-2411.03820) | 2024 | +0.17 | 2/7 | `arxiv:2411.03820` |
| 10 | [CDE: Curiosity-Driven Exploration for Efficient Reinforcement Learning in Large Language Models](#arxiv-2509.09675) | 2025 | +0.14 | 6/7 | `arxiv:2509.09675` |
| 11 | [Metalearning Continual Learning Algorithms](#arxiv-2312.00276) | 2023 | +0.11 | 5/7 | `arxiv:2312.00276` |
| 12 | [Dueling Network Architectures for Deep Reinforcement Learning](#arxiv-1511.06581) | 2015 | +0.11 | 6/7 | `arxiv:1511.06581` |
| 13 | [Q-Learning With World Models](#arxiv-2608.17163) | 2026 | +0.11 | 6/7 | `arxiv:2608.17163` |
| 14 | [Deep Reinforcement Learning with Double Q-learning](#arxiv-1509.06461) | 2015 | +0.10 | 5/7 | `arxiv:1509.06461` |
| 15 | [For SALE: State-Action Representation Learning for Deep Reinforcement Learning](#arxiv-2306.02451) | 2023 | +0.05 | 5/7 | `arxiv:2306.02451` |
| 16 | [1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities](#arxiv-2503.14858) | 2025 | -0.02 | 5/7 | `arxiv:2503.14858` |
| 17 | [Prioritized Experience Replay](#arxiv-1511.05952) | 2015 | -0.04 | 4/7 | `arxiv:1511.05952` |
| 18 | [In-Context Reinforcement Learning for Variable Action Spaces](#arxiv-2312.13327) | 2023 | -0.06 | 4/7 | `arxiv:2312.13327` |
| 19 | [Rainbow: Combining Improvements in Deep Reinforcement Learning](#arxiv-1710.02298) | 2017 | -0.14 | 3/7 | `arxiv:1710.02298` |
| 20 | [Towards General-Purpose Model-Free Reinforcement Learning](#arxiv-2501.16142) | 2025 | -0.16 | 5/7 | `arxiv:2501.16142` |
| 21 | [Revisiting Rainbow: Promoting more Insightful and Inclusive Deep Reinforcement Learning Research](#arxiv-2011.14826) | 2020 | -0.41 | 1/7 | `arxiv:2011.14826` |
| 22 | [Addressing Function Approximation Error in Actor-Critic Methods](#arxiv-1802.09477) | 2018 | -0.50 | 1/4 | `arxiv:1802.09477` |
| 23 | [Offline Reinforcement Learning: Tutorial, Review, and Perspectives on Open Problems](#arxiv-2005.01643) | 2020 | -0.59 | 0/7 | `arxiv:2005.01643` |
| 24 | [A Minimalist Approach to Offline Reinforcement Learning](#arxiv-2106.06860) | 2021 | -0.61 | 3/7 | `arxiv:2106.06860` |
| 25 | [Meta-Reinforcement Learning with Zero-Shot RL](#openreview-XyGJJ4FPoX) | unknown | -0.61 | 0/7 | `openreview:XyGJJ4FPoX` |
| 26 | [Benchmarking Batch Deep Reinforcement Learning Algorithms](#arxiv-1910.01708) | 2019 | -0.67 | 2/7 | `arxiv:1910.01708` |

### Post-training

| rank | title | year | final | accept | key |
|---:|---|---|---:|---:|---|
| 1 | [Rethinking RL for LLM Reasoning: It's Sparse Policy Selection, Not Capability Learning](#arxiv-2605.06241) | 2026 | +0.56 | 5/7 | `arxiv:2605.06241` |
| 2 | [OPRD: On-Policy Representation Distillation](#arxiv-2606.06021) | 2026 | +0.55 | 5/7 | `arxiv:2606.06021` |
| 3 | [GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning](#arxiv-2507.19457) | 2025 | +0.54 | 6/7 | `arxiv:2507.19457` |
| 4 | [On the Generalization of SFT: A Reinforcement Learning Perspective with Reward Rectification](#arxiv-2508.05629) | 2025 | +0.53 | 6/7 | `arxiv:2508.05629` |
| 5 | [Critique-GRPO: Advancing LLM Reasoning with Natural Language and Numerical Feedback](#arxiv-2506.03106) | 2025 | +0.52 | 7/7 | `arxiv:2506.03106` |
| 6 | [The Art of Scaling Reinforcement Learning Compute for LLMs](#arxiv-2510.13786) | 2025 | +0.48 | 6/7 | `arxiv:2510.13786` |
| 7 | [Spurious Rewards Paradox: Mechanistically Understanding How RLVR Activates Memorization Shortcuts in LLMs](#arxiv-2601.11061) | 2026 | +0.47 | 6/7 | `arxiv:2601.11061` |
| 8 | [Revisiting Reinforcement Learning with Verifiable Rewards from a Contrastive Perspective](#arxiv-2605.12969) | 2026 | +0.42 | 6/7 | `arxiv:2605.12969` |
| 9 | [Rethinking On-Policy Distillation of Large Language Models: Phenomenology, Mechanism, and Recipe](#arxiv-2604.13016) | 2026 | +0.42 | 6/7 | `arxiv:2604.13016` |
| 10 | [Understanding R1-Zero-Like Training: A Critical Perspective](#arxiv-2503.20783) | 2025 | +0.42 | 5/7 | `arxiv:2503.20783` |
| 11 | [RLVE: Scaling Up Reinforcement Learning for Language Models with Adaptive Verifiable Environments](#arxiv-2511.07317) | 2025 | +0.41 | 5/7 | `arxiv:2511.07317` |
| 12 | [MiniMax-M1: Scaling Test-Time Compute Efficiently with Lightning Attention](#arxiv-2506.13585) | 2025 | +0.40 | 4/7 | `arxiv:2506.13585` |
| 13 | [TTRL: Test-Time Reinforcement Learning](#arxiv-2504.16084) | 2025 | +0.40 | 5/7 | `arxiv:2504.16084` |
| 14 | [Group-in-Group Policy Optimization for LLM Agent Training](#arxiv-2505.10978) | 2025 | +0.39 | 7/7 | `arxiv:2505.10978` |
| 15 | [Skip-Connected Policy Optimization for Implicit Advantage](#arxiv-2604.08690) | 2026 | +0.36 | 6/7 | `arxiv:2604.08690` |
| 16 | [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](#arxiv-2402.03300) | 2024 | +0.33 | 5/7 | `arxiv:2402.03300` |
| 17 | [Reinforcement Learning via Self-Distillation](#arxiv-2601.20802) | 2026 | +0.32 | 6/7 | `arxiv:2601.20802` |
| 18 | [Learning to Discover at Test Time](#arxiv-2601.16175) | 2026 | +0.31 | 6/7 | `arxiv:2601.16175` |
| 19 | [SR-GRPO: Stable Rank as an Intrinsic Geometric Reward for Large Language Model Alignment](#arxiv-2512.02807) | 2025 | +0.29 | 6/7 | `arxiv:2512.02807` |
| 20 | [Self-Distillation Bridges Distribution Gap in Language Model Fine-Tuning](#arxiv-2402.13669) | 2024 | +0.28 | 5/7 | `arxiv:2402.13669` |
| 21 | [Beyond the 80/20 Rule: High-Entropy Minority Tokens Drive Effective Reinforcement Learning for LLM Reasoning](#arxiv-2506.01939) | 2025 | +0.26 | 4/7 | `arxiv:2506.01939` |
| 22 | [Reasoning with Sampling: Your Base Model is Smarter Than You Think](#arxiv-2510.14901) | 2025 | +0.25 | 6/7 | `arxiv:2510.14901` |
| 23 | [ESPO: Entropy Importance Sampling Policy Optimization](#arxiv-2512.00499) | 2025 | +0.25 | 6/7 | `arxiv:2512.00499` |
| 24 | [From Reasoning Chains to Verifiable Subproblems: Curriculum Reinforcement Learning Enables Credit Assignment for LLM Reasoning](#arxiv-2605.22074) | 2026 | +0.23 | 6/7 | `arxiv:2605.22074` |
| 25 | [Latent On-Policy Self-Distillation](#arxiv-2608.13040) | 2026 | +0.19 | 6/7 | `arxiv:2608.13040` |
| 26 | [Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models](#arxiv-2601.18734) | 2026 | +0.17 | 5/7 | `arxiv:2601.18734` |
| 27 | [Gradient Regularization Mitigates Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards](#arxiv-2602.18037) | 2026 | +0.16 | 4/7 | `arxiv:2602.18037` |
| 28 | [Soft Adaptive Policy Optimization](#arxiv-2511.20347) | 2025 | +0.14 | 5/7 | `arxiv:2511.20347` |
| 29 | [Self-Refine: Iterative Refinement with Self-Feedback](#arxiv-2303.17651) | 2023 | +0.11 | 6/7 | `arxiv:2303.17651` |
| 30 | [To Retain or to Adapt? Generalizing Continual Learning](#arxiv-2607.05609) | 2026 | +0.09 | 5/7 | `arxiv:2607.05609` |
| 31 | [Curriculum Reinforcement Learning from Easy to Hard Tasks Improves LLM Reasoning](#arxiv-2506.06632) | 2025 | +0.08 | 5/7 | `arxiv:2506.06632` |
| 32 | [Group Sequence Policy Optimization](#arxiv-2507.18071) | 2025 | +0.05 | 5/7 | `arxiv:2507.18071` |
| 33 | [Towards Execution-Grounded Automated AI Research](#arxiv-2601.14525) | 2026 | +0.04 | 5/7 | `arxiv:2601.14525` |
| 34 | [Unifying Group-Relative and Self-Distillation Policy Optimization via Sample Routing](#arxiv-2604.02288) | 2026 | +0.01 | 5/7 | `arxiv:2604.02288` |
| 35 | [Learning from Own Solutions: Self-Conditioned Credit Assignment for Reinforcement Learning with Verifiable Rewards](#arxiv-2606.18810) | 2026 | +0.01 | 4/7 | `arxiv:2606.18810` |
| 36 | [When Does Continual Learning Require Learning](#arxiv-2607.07847) | 2026 | +0.00 | 4/7 | `arxiv:2607.07847` |
| 37 | [Learning to Reason without External Rewards](#arxiv-2505.19590) | 2025 | -0.00 | 3/7 | `arxiv:2505.19590` |
| 38 | [GRPO-VPS: Enhancing Group Relative Policy Optimization with Verifiable Process Supervision for Effective Reasoning](#arxiv-2604.20659) | 2026 | -0.02 | 5/7 | `arxiv:2604.20659` |
| 39 | [Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?](#arxiv-2504.13837) | 2025 | -0.02 | 4/7 | `arxiv:2504.13837` |
| 40 | [LADDER: Self-Improving LLMs Through Recursive Problem Decomposition](#arxiv-2503.00735) | 2025 | -0.04 | 4/7 | `arxiv:2503.00735` |
| 41 | [From $f(x)$ and $g(x)$ to $f(g(x))$: LLMs Learn New Skills in RL by Composing Old Ones](#arxiv-2509.25123) | 2025 | -0.07 | 5/7 | `arxiv:2509.25123` |
| 42 | [Single-stream Policy Optimization](#arxiv-2509.13232) | 2025 | -0.07 | 5/7 | `arxiv:2509.13232` |
| 43 | [iGRPO: Self-Feedback-Driven LLM Reasoning](#arxiv-2602.09000) | 2026 | -0.08 | 4/7 | `arxiv:2602.09000` |
| 44 | [Emergent Hierarchical Reasoning in LLMs through Reinforcement Learning](#arxiv-2509.03646) | 2025 | -0.09 | 3/7 | `arxiv:2509.03646` |
| 45 | [Revisiting On-Policy Distillation: Empirical Failure Modes and Simple Fixes](#arxiv-2603.25562) | 2026 | -0.09 | 5/7 | `arxiv:2603.25562` |
| 46 | [Self-Distillation Enables Continual Learning](#arxiv-2601.19897) | 2026 | -0.09 | 6/7 | `arxiv:2601.19897` |
| 47 | [It Takes Two: Your GRPO Is Secretly DPO](#arxiv-2510.00977) | 2025 | -0.10 | 5/7 | `arxiv:2510.00977` |
| 48 | [The First Few Tokens Are All You Need: An Efficient and Effective Unsupervised Prefix Fine-Tuning Method for Reasoning Models](#arxiv-2503.02875) | 2025 | -0.16 | 3/7 | `arxiv:2503.02875` |
| 49 | [RIFT: A RubrIc Failure Mode Taxonomy and Automated Diagnostics](#arxiv-2604.01375) | 2026 | -0.16 | 3/7 | `arxiv:2604.01375` |
| 50 | [Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs?](#arxiv-2603.24472) | 2026 | -0.24 | 3/7 | `arxiv:2603.24472` |
| 51 | [Klear-Reasoner: Advancing Reasoning Capability via Gradient-Preserving Clipping Policy Optimization](#arxiv-2508.07629) | 2025 | -0.28 | 3/6 | `arxiv:2508.07629` |
| 52 | [Weight-Space Geometry of Offline Reasoning Training](#arxiv-2606.23740) | 2026 | -0.32 | 2/7 | `arxiv:2606.23740` |
| 53 | [DAPO: An Open-Source LLM Reinforcement Learning System at Scale](#arxiv-2503.14476) | 2025 | -0.40 | 3/7 | `arxiv:2503.14476` |
| 54 | [BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](#arxiv-2608.09888) | 2026 | -0.43 | 2/7 | `arxiv:2608.09888` |
| 55 | [Evolutionary Strategies lead to Catastrophic Forgetting in LLMs](#arxiv-2601.20861) | 2026 | -0.67 | 3/7 | `arxiv:2601.20861` |

### LLMs: architectures, context, training

| rank | title | year | final | accept | key |
|---:|---|---|---:|---:|---|
| 1 | [Cache-to-Cache: Direct Semantic Communication Between Large Language Models](#arxiv-2510.03215) | 2025 | +0.58 | 5/7 | `arxiv:2510.03215` |
| 2 | [Large Language Diffusion Models](#arxiv-2502.09992) | 2025 | +0.58 | 6/7 | `arxiv:2502.09992` |
| 3 | [Hyena Hierarchy: Towards Larger Convolutional Language Models](#arxiv-2302.10866) | 2023 | +0.53 | 6/7 | `arxiv:2302.10866` |
| 4 | [Language Is Not All You Need: Aligning Perception with Language Models](#arxiv-2302.14045) | 2023 | +0.35 | 6/7 | `arxiv:2302.14045` |
| 5 | [Neural Networks and the Chomsky Hierarchy](#arxiv-2207.02098) | 2022 | +0.34 | 7/7 | `arxiv:2207.02098` |
| 6 | [Enabling Agents to Communicate Entirely in Latent Space](#arxiv-2511.09149) | 2025 | +0.33 | 4/7 | `arxiv:2511.09149` |
| 7 | [Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference](#arxiv-2412.13663) | 2024 | +0.32 | 5/7 | `arxiv:2412.13663` |
| 8 | [2 OLMo 2 Furious](#arxiv-2501.00656) | 2024 | +0.30 | 5/7 | `arxiv:2501.00656` |
| 9 | [Memorizing Transformers](#arxiv-2203.08913) | 2022 | +0.28 | 5/7 | `arxiv:2203.08913` |
| 10 | [A Hippocampus for Linear Attention: An Exact Memory for What the Recurrent State Forgets](#arxiv-2607.02303) | 2026 | +0.27 | 6/7 | `arxiv:2607.02303` |
| 11 | [DiffusionGemma Technical Report](#arxiv-2608.00146) | 2026 | +0.27 | 3/7 | `arxiv:2608.00146` |
| 12 | [XBridge: Entity-Grounded Latent Bridge for Heterogeneous LLM Communication](#arxiv-2608.11676) | 2026 | +0.27 | 5/7 | `arxiv:2608.11676` |
| 13 | [DMax: Aggressive Parallel Decoding for dLLMs](#arxiv-2604.08302) | 2026 | +0.26 | 4/7 | `arxiv:2604.08302` |
| 14 | [Scaling MLPs: A Tale of Inductive Bias](#arxiv-2306.13575) | 2023 | +0.26 | 3/7 | `arxiv:2306.13575` |
| 15 | [Skip a Layer or Loop It? Learning Program-of-Layers in LLMs](#arxiv-2606.06574) | 2026 | +0.26 | 6/7 | `arxiv:2606.06574` |
| 16 | [Florence-2: Advancing a Unified Representation for a Variety of Vision Tasks](#arxiv-2311.06242) | 2023 | +0.25 | 4/7 | `arxiv:2311.06242` |
| 17 | [Olmo 3](#arxiv-2512.13961) | 2025 | +0.23 | 3/7 | `arxiv:2512.13961` |
| 18 | [Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation](#arxiv-2507.10524) | 2025 | +0.23 | 7/7 | `arxiv:2507.10524` |
| 19 | [Unlimiformer: Long-Range Transformers with Unlimited Length Input](#arxiv-2305.01625) | 2023 | +0.22 | 5/7 | `arxiv:2305.01625` |
| 20 | [Recursive Language Models](#arxiv-2512.24601) | 2025 | +0.19 | 4/7 | `arxiv:2512.24601` |
| 21 | [Cross-Model KV Cache Transfer in LLM Families: A Closed-Form Linear Mapping for Prefill Reuse](#arxiv-2608.03893) | 2026 | +0.19 | 5/7 | `arxiv:2608.03893` |
| 22 | [LLaDA2.0: Scaling Up Diffusion Language Models to 100B](#arxiv-2512.15745) | 2025 | +0.18 | 4/7 | `arxiv:2512.15745` |
| 23 | [Communicating Activations Between Language Model Agents](#arxiv-2501.14082) | 2025 | +0.10 | 6/7 | `arxiv:2501.14082` |
| 24 | [Searching for Activation Functions](#arxiv-1710.05941) | 2017 | +0.10 | 4/7 | `arxiv:1710.05941` |
| 25 | [Encoder-Decoder or Decoder-Only? Revisiting Encoder-Decoder Large Language Model](#arxiv-2510.26622) | 2025 | +0.07 | 6/7 | `arxiv:2510.26622` |
| 26 | [Beyond Scattered Acceptance: Fast and Coherent Inference for DLMs via Longest Stable Prefixes](#arxiv-2603.05454) | 2026 | +0.07 | 5/7 | `arxiv:2603.05454` |
| 27 | [The Llama 3 Herd of Models](#arxiv-2407.21783) | 2024 | +0.05 | 3/7 | `arxiv:2407.21783` |
| 28 | [Encoder-Decoder Gemma: Improving the Quality-Efficiency Trade-Off via Adaptation](#arxiv-2504.06225) | 2025 | -0.02 | 5/7 | `arxiv:2504.06225` |
| 29 | [LLaDA2.1: Speeding Up Text Diffusion via Token Editing](#arxiv-2602.08676) | 2026 | -0.04 | 5/7 | `arxiv:2602.08676` |
| 30 | [Leave No Context Behind: Efficient Infinite Context Transformers with Infini-attention](#arxiv-2404.07143) | 2024 | -0.12 | 3/7 | `arxiv:2404.07143` |
| 31 | [TransformerFAM: Feedback attention is working memory](#arxiv-2404.09173) | 2024 | -0.15 | 3/7 | `arxiv:2404.09173` |
| 32 | [Latent Cache Flow: Model-to-Model Communication Without Text](#arxiv-2605.22863) | 2026 | -0.20 | 4/7 | `arxiv:2605.22863` |
| 33 | [Energy Transformer](#arxiv-2302.07253) | 2023 | -0.37 | 4/7 | `arxiv:2302.07253` |
| 34 | [T5Gemma 2: Seeing, Reading, and Understanding Longer](#arxiv-2512.14856) | 2025 | -0.39 | 2/7 | `arxiv:2512.14856` |
| 35 | [xLSTM: Extended Long Short-Term Memory](#arxiv-2405.04517) | 2024 | -0.44 | 2/7 | `arxiv:2405.04517` |
| 36 | [Your Transformer is Secretly Linear](#arxiv-2405.12250) | 2024 | -0.52 | 3/7 | `arxiv:2405.12250` |
| 37 | [GLU Variants Improve Transformer](#arxiv-2002.05202) | 2020 | -0.70 | 1/7 | `arxiv:2002.05202` |

### Reasoning and the "physics" of language models

| rank | title | year | final | accept | key |
|---:|---|---|---:|---:|---|
| 1 | [Progress measures for grokking via mechanistic interpretability](#arxiv-2301.05217) | 2023 | +0.72 | 7/7 | `arxiv:2301.05217` |
| 2 | [Arithmetic Without Algorithms: Language Models Solve Math With a Bag of Heuristics](#arxiv-2410.21272) | 2024 | +0.68 | 6/7 | `arxiv:2410.21272` |
| 3 | [Reinforcing General Reasoning without Verifiers](#arxiv-2505.21493) | 2025 | +0.59 | 6/7 | `arxiv:2505.21493` |
| 4 | [Physics of Language Models: Part 1, Learning Hierarchical Language Structures](#arxiv-2305.13673) | 2023 | +0.54 | 6/7 | `arxiv:2305.13673` |
| 5 | [Grokked Transformers are Implicit Reasoners: A Mechanistic Journey to the Edge of Generalization](#arxiv-2405.15071) | 2024 | +0.51 | 6/7 | `arxiv:2405.15071` |
| 6 | [Are Emergent Abilities of Large Language Models a Mirage?](#arxiv-2304.15004) | 2023 | +0.49 | 5/7 | `arxiv:2304.15004` |
| 7 | [rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking](#arxiv-2501.04519) | 2025 | +0.48 | 6/7 | `arxiv:2501.04519` |
| 8 | [Grokking Group Multiplication with Cosets](#openreview-hcQfTsVnBo) | unknown | +0.47 | 5/7 | `openreview:hcQfTsVnBo` |
| 9 | [Spurious Rewards: Rethinking Training Signals in RLVR](#arxiv-2506.10947) | 2025 | +0.45 | 7/7 | `arxiv:2506.10947` |
| 10 | [Language Models Use Trigonometry to Do Addition](#arxiv-2502.00873) | 2025 | +0.44 | 6/7 | `arxiv:2502.00873` |
| 11 | [Pre-trained Large Language Models Use Fourier Features to Compute Addition](#arxiv-2406.03445) | 2024 | +0.43 | 6/7 | `arxiv:2406.03445` |
| 12 | [Physics of Language Models: Part 3.3, Knowledge Capacity Scaling Laws](#arxiv-2404.05405) | 2024 | +0.43 | 5/7 | `arxiv:2404.05405` |
| 13 | [In-Context Algebra](#arxiv-2512.16902) | 2025 | +0.41 | 7/7 | `arxiv:2512.16902` |
| 14 | [How do language models learn facts? Dynamics, curricula and hallucinations](#arxiv-2503.21676) | 2025 | +0.37 | 6/7 | `arxiv:2503.21676` |
| 15 | [Physics of Language Models: Part 2.1, Grade-School Math and the Hidden Reasoning Process](#arxiv-2407.20311) | 2024 | +0.36 | 5/7 | `arxiv:2407.20311` |
| 16 | [Bridging the Gap Between Latent and Explicit Reasoning with Looped Transformers](#arxiv-2606.31779) | 2026 | +0.36 | 5/7 | `arxiv:2606.31779` |
| 17 | [Reliable Chain-of-Thought via Prefix Consistency](#arxiv-2605.07654) | 2026 | +0.31 | 6/7 | `arxiv:2605.07654` |
| 18 | [SIM-CoT: Supervised Implicit Chain-of-Thought](#arxiv-2509.20317) | 2025 | +0.30 | 6/7 | `arxiv:2509.20317` |
| 19 | [Self-Consistency Improves Chain of Thought Reasoning in Language Models](#arxiv-2203.11171) | 2022 | +0.29 | 7/7 | `arxiv:2203.11171` |
| 20 | [The Unreasonable Effectiveness of Entropy Minimization in LLM Reasoning](#arxiv-2505.15134) | 2025 | +0.29 | 6/7 | `arxiv:2505.15134` |
| 21 | [Physics of Language Models: Part 3.2, Knowledge Manipulation](#arxiv-2309.14402) | 2023 | +0.27 | 3/6 | `arxiv:2309.14402` |
| 22 | [Reinforcement Learning for Reasoning in Large Language Models with One Training Example](#arxiv-2504.20571) | 2025 | +0.26 | 4/7 | `arxiv:2504.20571` |
| 23 | [Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach](#arxiv-2502.05171) | 2025 | +0.25 | 5/7 | `arxiv:2502.05171` |
| 24 | [The Reversal Curse: LLMs trained on "A is B" fail to learn "B is A"](#arxiv-2309.12288) | 2023 | +0.24 | 4/7 | `arxiv:2309.12288` |
| 25 | [Physics of Language Models: Part 3.1, Knowledge Storage and Extraction](#arxiv-2309.14316) | 2023 | +0.24 | 4/7 | `arxiv:2309.14316` |
| 26 | [Evaluating the World Model Implicit in a Generative Model](#arxiv-2406.03689) | 2024 | +0.20 | 4/7 | `arxiv:2406.03689` |
| 27 | [Training Large Language Models to Reason in a Continuous Latent Space](#arxiv-2412.06769) | 2024 | +0.15 | 5/7 | `arxiv:2412.06769` |
| 28 | [Emergent Analogical Reasoning in Large Language Models](#arxiv-2212.09196) | 2022 | +0.13 | 5/7 | `arxiv:2212.09196` |
| 29 | [A Formal Comparison Between Chain of Thought and Latent Thought](#arxiv-2509.25239) | 2025 | +0.13 | 5/7 | `arxiv:2509.25239` |
| 30 | [How Do Large Language Models Acquire Factual Knowledge During Pretraining?](#arxiv-2406.11813) | 2024 | +0.11 | 5/7 | `arxiv:2406.11813` |
| 31 | [Modular Arithmetic: Language Models Solve Math Digit by Digit](#arxiv-2508.02513) | 2025 | +0.09 | 6/7 | `arxiv:2508.02513` |
| 32 | [Transcendence: Generative Models Can Outperform The Experts That Train Them](#arxiv-2406.11741) | 2024 | +0.06 | 4/7 | `arxiv:2406.11741` |
| 33 | [Why Can't Transformers Learn Multiplication? Reverse-Engineering Reveals Long-Range Dependency Pitfalls](#arxiv-2510.00184) | 2025 | +0.05 | 6/7 | `arxiv:2510.00184` |
| 34 | [Dissociating language and thought in large language models](#arxiv-2301.06627) | 2023 | +0.05 | 3/7 | `arxiv:2301.06627` |
| 35 | [LiveMathematicianBench: A Live Benchmark for Mathematician-Level Reasoning with Proof Sketches](#arxiv-2604.01754) | 2026 | +0.03 | 4/7 | `arxiv:2604.01754` |
| 36 | [Multimodal Chain-of-Thought Reasoning in Language Models](#arxiv-2302.00923) | 2023 | +0.03 | 5/7 | `arxiv:2302.00923` |
| 37 | [The Truth is in There: Improving Reasoning in Language Models with Layer-Selective Rank Reduction](#arxiv-2312.13558) | 2023 | +0.02 | 4/7 | `arxiv:2312.13558` |
| 38 | [Emergent Capabilities Arise Randomly from Learning Sparse Attention Patterns](#arxiv-2606.25010) | 2026 | +0.02 | 4/7 | `arxiv:2606.25010` |
| 39 | [Language Models Compare Quantities Using Number-specific and Unit-specific Heuristics](#arxiv-2606.03982) | 2026 | -0.01 | 4/7 | `arxiv:2606.03982` |
| 40 | [Evidence from formal logical reasoning reveals that the language of thought is not natural language](#doi-10.1073-pnas.2520095123) | 2026 | -0.11 | 5/7 | `doi:10.1073/pnas.2520095123` |
| 41 | [From Explicit CoT to Implicit CoT: Learning to Internalize CoT Step by Step](#arxiv-2405.14838) | 2024 | -0.14 | 4/7 | `arxiv:2405.14838` |
| 42 | [Language Models Are Capable of Metacognitive Monitoring and Control of Their Internal Activations](#arxiv-2505.13763) | 2025 | -0.15 | 4/7 | `arxiv:2505.13763` |
| 43 | [A Mechanistic Analysis of Looped Reasoning Language Models](#arxiv-2604.11791) | 2026 | -0.21 | 3/7 | `arxiv:2604.11791` |
| 44 | [Can Large Reasoning Models Self-Train?](#arxiv-2505.21444) | 2025 | -0.23 | 2/7 | `arxiv:2505.21444` |
| 45 | [The Lookahead Limitation: Why Multi-Operand Addition is Hard for LLMs](#arxiv-2502.19981) | 2025 | -0.23 | 3/7 | `arxiv:2502.19981` |
| 46 | [LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks](#arxiv-2402.01817) | 2024 | -0.31 | 2/7 | `arxiv:2402.01817` |
| 47 | [Knowledge Mechanisms in Large Language Models: A Survey and Perspective](#arxiv-2407.15017) | 2024 | -0.32 | 3/7 | `arxiv:2407.15017` |
| 48 | [Language is primarily a tool for communication rather than thought](#doi-10.1038-s41586-024-07522-w) | 2024 | -0.33 | 4/5 | `doi:10.1038/s41586-024-07522-w` |
| 49 | [Competitive Programming with Large Reasoning Models](#arxiv-2502.06807) | 2025 | -0.33 | 4/7 | `arxiv:2502.06807` |
| 50 | [Position: LLMs can't jump](#openreview-klU4737opt) | unknown | -0.37 | 2/7 | `openreview:klU4737opt` |
| 51 | [Large Language Models Still Can't Plan / PlanBench (Kambhampati)](#openreview-wUU-7XTL5XO) | unknown | -0.39 | 2/7 | `openreview:wUU-7XTL5XO` |
| 52 | [Why mathematics is set to be revolutionized by AI](#doi-10.1038-d41586-024-01413-w) | 2024 | -0.45 | 3/5 | `doi:10.1038/d41586-024-01413-w` |
| 53 | [AI-rithmetic](#arxiv-2602.10416) | 2026 | -0.53 | 2/7 | `arxiv:2602.10416` |
| 54 | [Scaling of Search and Learning: A Roadmap to Reproduce o1 from Reinforcement Learning Perspective](#arxiv-2412.14135) | 2024 | -0.80 | 0/7 | `arxiv:2412.14135` |

### Data, training, optimization

| rank | title | year | final | accept | key |
|---:|---|---|---:|---:|---|
| 1 | [Sharpness-Aware Minimization for Efficiently Improving Generalization](#arxiv-2010.01412) | 2020 | +0.65 | 5/7 | `arxiv:2010.01412` |
| 2 | [Large Batch Optimization for Deep Learning: Training BERT in 76 minutes](#arxiv-1904.00962) | 2019 | +0.56 | 4/7 | `arxiv:1904.00962` |
| 3 | [Tasks, stability, architecture, and compute: Training more effective learned optimizers, and using them to train themselves](#arxiv-2009.11243) | 2020 | +0.55 | 5/7 | `arxiv:2009.11243` |
| 4 | [Symbolic Discovery of Optimization Algorithms](#arxiv-2302.06675) | 2023 | +0.50 | 5/7 | `arxiv:2302.06675` |
| 5 | [Scaling Laws for Neural Language Models](#arxiv-2001.08361) | 2020 | +0.43 | 4/7 | `arxiv:2001.08361` |
| 6 | [The Loss Does Not See the Basis, but Adam Does](#arxiv-2608.05136) | 2026 | +0.41 | 6/7 | `arxiv:2608.05136` |
| 7 | [Loss of plasticity in deep continual learning](#doi-10.1038-s41586-024-07711-7) | 2024 | +0.40 | 5/7 | `doi:10.1038/s41586-024-07711-7` |
| 8 | [The Road Less Scheduled](#arxiv-2405.15682) | 2024 | +0.39 | 5/7 | `arxiv:2405.15682` |
| 9 | [Explorative Modeling: Unlocking a Third Pretraining Axis and End-to-End Generation](#arxiv-2607.27372) | 2026 | +0.37 | 7/7 | `arxiv:2607.27372` |
| 10 | [The AdEMAMix Optimizer: Better, Faster, Older](#arxiv-2409.03137) | 2024 | +0.35 | 4/7 | `arxiv:2409.03137` |
| 11 | [How much do language models memorize?](#arxiv-2505.24832) | 2025 | +0.31 | 6/7 | `arxiv:2505.24832` |
| 12 | [How Neural Networks Extrapolate: From Feedforward to Graph Neural Networks](#arxiv-2009.11848) | 2020 | +0.28 | 5/7 | `arxiv:2009.11848` |
| 13 | [Scaling Laws and Compute-Optimal Training Beyond Fixed Training Durations](#arxiv-2405.18392) | 2024 | +0.27 | 5/7 | `arxiv:2405.18392` |
| 14 | [Scaling Laws for Reward Model Overoptimization](#arxiv-2210.10760) | 2022 | +0.24 | 5/7 | `arxiv:2210.10760` |
| 15 | [On-Policy RL Meets Off-Policy Experts: Harmonizing Supervised Fine-Tuning and Reinforcement Learning via Dynamic Weighting](#arxiv-2508.11408) | 2025 | +0.22 | 5/7 | `arxiv:2508.11408` |
| 16 | [Perplexed by Perplexity: Perplexity-Based Data Pruning With Small Reference Models](#arxiv-2405.20541) | 2024 | +0.19 | 4/7 | `arxiv:2405.20541` |
| 17 | [Grokfast: Accelerated Grokking by Amplifying Slow Gradients](#arxiv-2405.20233) | 2024 | +0.18 | 3/7 | `arxiv:2405.20233` |
| 18 | [Learning Vision from Models Rivals Learning Vision from Data](#arxiv-2312.17742) | 2023 | +0.17 | 3/7 | `arxiv:2312.17742` |
| 19 | [The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks](#arxiv-1803.03635) | 2018 | +0.14 | 3/7 | `arxiv:1803.03635` |
| 20 | [NorMuon: Making Muon more efficient and scalable](#arxiv-2510.05491) | 2025 | +0.10 | 6/7 | `arxiv:2510.05491` |
| 21 | [Emergent properties with repeated examples](#arxiv-2410.07041) | 2024 | +0.07 | 5/7 | `arxiv:2410.07041` |
| 22 | [Sophia: A Scalable Stochastic Second-order Optimizer for Language Model Pre-training](#arxiv-2305.14342) | 2023 | +0.04 | 4/7 | `arxiv:2305.14342` |
| 23 | [Overcoming catastrophic forgetting in neural networks](#doi-10.1073-pnas.1611835114) | 2017 | +0.00 | 4/7 | `doi:10.1073/pnas.1611835114` |
| 24 | [No Train No Gain: Revisiting Efficient Training Algorithms For Transformer-based Language Models](#arxiv-2307.06440) | 2023 | -0.01 | 3/7 | `arxiv:2307.06440` |
| 25 | [On the Information Bottleneck Theory of Deep Learning (Saxe et al.)](#openreview-ry_WPG-A-) | unknown | -0.03 | 5/7 | `openreview:ry_WPG-A-` |
| 26 | [Super-Convergence: Very Fast Training of Neural Networks Using Large Learning Rates](#arxiv-1708.07120) | 2017 | -0.07 | 3/7 | `arxiv:1708.07120` |
| 27 | [gzip Predicts Data-dependent Scaling Laws](#arxiv-2405.16684) | 2024 | -0.09 | 3/7 | `arxiv:2405.16684` |
| 28 | [Cramming: Training a Language Model on a Single GPU in One Day](#arxiv-2212.14034) | 2022 | -0.16 | 3/7 | `arxiv:2212.14034` |
| 29 | [MetaOptimize: A Framework for Optimizing Step Sizes and Other Meta-parameters](#arxiv-2402.02342) | 2024 | -0.30 | 3/7 | `arxiv:2402.02342` |
| 30 | [Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved)](#arxiv-2507.12856) | 2025 | -0.32 | 3/7 | `arxiv:2507.12856` |
| 31 | [Learning in High Dimension Always Amounts to Extrapolation](#arxiv-2110.09485) | 2021 | -0.39 | 1/7 | `arxiv:2110.09485` |
| 32 | [Continual Learning and Catastrophic Forgetting](#arxiv-2403.05175) | 2024 | -0.39 | 2/7 | `arxiv:2403.05175` |
| 33 | [Self-Improving Pretraining: using post-trained models to pretrain better models](#arxiv-2601.21343) | 2026 | -0.40 | 3/7 | `arxiv:2601.21343` |
| 34 | [Reinforcement Pre-Training](#arxiv-2506.08007) | 2025 | -0.51 | 3/7 | `arxiv:2506.08007` |
| 35 | [Cyclical Learning Rates for Training Neural Networks](#arxiv-1506.01186) | 2015 | -0.52 | 1/7 | `arxiv:1506.01186` |
| 36 | [Continual Backprop: Stochastic Gradient Descent with Persistent Randomness](#arxiv-2108.06325) | 2021 | -0.62 | 0/7 | `arxiv:2108.06325` |
| 37 | [Measuring Catastrophic Forgetting in Neural Networks](#arxiv-1708.02072) | 2017 | -0.63 | 2/7 | `arxiv:1708.02072` |
| 38 | [Nested Learning: The Illusion of Deep Learning Architectures](#arxiv-2512.24695) | 2025 | -0.75 | 0/6 | `arxiv:2512.24695` |
| 39 | [Step-size Optimization for Continual Learning](#arxiv-2401.17401) | 2024 | -0.78 | 1/7 | `arxiv:2401.17401` |
| 40 | [Catastrophic Forgetting in Deep Learning: A Comprehensive Taxonomy](#arxiv-2312.10549) | 2023 | -0.78 | 0/7 | `arxiv:2312.10549` |

### Self-supervised learning and vision

| rank | title | year | final | accept | key |
|---:|---|---|---:|---:|---|
| 1 | [When Does LeJEPA Learn a World Model?](#arxiv-2605.26379) | 2026 | +0.71 | 6/7 | `arxiv:2605.26379` |
| 2 | [Emerging Properties in Self-Supervised Vision Transformers](#arxiv-2104.14294) | 2021 | +0.54 | 5/7 | `arxiv:2104.14294` |
| 3 | [ImageReward: Learning and Evaluating Human Preferences for Text-to-Image Generation](#arxiv-2304.05977) | 2023 | +0.53 | 5/7 | `arxiv:2304.05977` |
| 4 | [Unsupervised Learning of Visual Features by Contrasting Cluster Assignments](#arxiv-2006.09882) | 2020 | +0.48 | 4/7 | `arxiv:2006.09882` |
| 5 | [VISReg: Variance-Invariance-Sketching Regularization for JEPA training](#arxiv-2606.02572) | 2026 | +0.42 | 6/7 | `arxiv:2606.02572` |
| 6 | [LeJEPA: Provable and Scalable Self-Supervised Learning Without the Heuristics](#arxiv-2511.08544) | 2025 | +0.40 | 6/7 | `arxiv:2511.08544` |
| 7 | [Image as a Foreign Language: BEiT Pretraining for All Vision and Vision-Language Tasks](#arxiv-2208.10442) | 2022 | +0.27 | 5/7 | `arxiv:2208.10442` |
| 8 | [DINOv2: Learning Robust Visual Features without Supervision](#arxiv-2304.07193) | 2023 | +0.25 | 4/7 | `arxiv:2304.07193` |
| 9 | [Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture](#arxiv-2301.08243) | 2023 | +0.23 | 4/7 | `arxiv:2301.08243` |
| 10 | [Emu: Enhancing Image Generation Models Using Photogenic Needles in a Haystack](#arxiv-2309.15807) | 2023 | +0.21 | 4/7 | `arxiv:2309.15807` |
| 11 | [Latent Consistency Models: Synthesizing High-Resolution Images with Few-Step Inference](#arxiv-2310.04378) | 2023 | +0.21 | 3/7 | `arxiv:2310.04378` |
| 12 | [iBOT: Image BERT Pre-Training with Online Tokenizer](#arxiv-2111.07832) | 2021 | +0.16 | 4/7 | `arxiv:2111.07832` |
| 13 | [The GAN is dead; long live the GAN! A Modern GAN Baseline](#arxiv-2501.05441) | 2025 | +0.06 | 5/7 | `arxiv:2501.05441` |
| 14 | [Towards Universal Fake Image Detectors that Generalize Across Generative Models](#arxiv-2302.10174) | 2023 | +0.06 | 4/7 | `arxiv:2302.10174` |
| 15 | [ELT: Elastic Looped Transformers for Visual Generation](#arxiv-2604.09168) | 2026 | +0.05 | 4/7 | `arxiv:2604.09168` |
| 16 | [VICReg: Variance-Invariance-Covariance Regularization for Self-Supervised Learning](#arxiv-2105.04906) | 2021 | -0.11 | 3/7 | `arxiv:2105.04906` |
| 17 | [Tune-A-Video: One-Shot Tuning of Image Diffusion Models for Text-to-Video Generation](#arxiv-2212.11565) | 2022 | -0.32 | 3/7 | `arxiv:2212.11565` |
| 18 | [To Compress or Not to Compress- Self-Supervised Learning and Information Theory: A Review](#arxiv-2304.09355) | 2023 | -0.47 | 1/7 | `arxiv:2304.09355` |
| 19 | [A Cookbook of Self-Supervised Learning](#arxiv-2304.12210) | 2023 | -0.69 | 1/7 | `arxiv:2304.12210` |
| 20 | [A Path Towards Autonomous Machine Intelligence (LeCun, 2022)](#openreview-BZ5a1r-kVsf) | unknown | -0.73 | 2/7 | `openreview:BZ5a1r-kVsf` |

### Retrieval, embeddings, benchmarks

| rank | title | year | final | accept | key |
|---:|---|---|---:|---:|---|
| 1 | [Matryoshka Representation Learning](#arxiv-2205.13147) | 2022 | +0.68 | 6/7 | `arxiv:2205.13147` |
| 2 | [One Embedder, Any Task: Instruction-Finetuned Text Embeddings](#arxiv-2212.09741) | 2022 | +0.60 | 6/7 | `arxiv:2212.09741` |
| 3 | [Beyond the Imitation Game: Quantifying and extrapolating the capabilities of language models](#arxiv-2206.04615) | 2022 | +0.46 | 3/6 | `arxiv:2206.04615` |
| 4 | [Rainbow Teaming: Open-Ended Generation of Diverse Adversarial Prompts](#arxiv-2402.16822) | 2024 | +0.45 | 6/7 | `arxiv:2402.16822` |
| 5 | [MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering](#arxiv-2410.07095) | 2024 | +0.39 | 4/7 | `arxiv:2410.07095` |
| 6 | [Large Dual Encoders Are Generalizable Retrievers](#arxiv-2112.07899) | 2021 | +0.36 | 4/7 | `arxiv:2112.07899` |
| 7 | [Demonstrate-Search-Predict: Composing retrieval and language models for knowledge-intensive NLP](#arxiv-2212.14024) | 2022 | +0.35 | 6/7 | `arxiv:2212.14024` |
| 8 | [CEO-Bench: Can Agents Play the Long Game?](#arxiv-2606.18543) | 2026 | +0.18 | 5/7 | `arxiv:2606.18543` |
| 9 | [Super-NaturalInstructions: Generalization via Declarative Instructions on 1600+ NLP Tasks](#acl-2022.emnlp-main.340) | unknown | +0.10 | 4/7 | `acl:2022.emnlp-main.340` |
| 10 | [Did Aristotle Use a Laptop? A Question Answering Benchmark with Implicit Reasoning Strategies](#arxiv-2101.02235) | 2021 | +0.06 | 5/7 | `arxiv:2101.02235` |
| 11 | [Can Generalist Foundation Models Outcompete Special-Purpose Tuning? Case Study in Medicine](#arxiv-2311.16452) | 2023 | +0.03 | 5/7 | `arxiv:2311.16452` |
| 12 | [Artifacts or Abduction: How Do LLMs Answer Multiple-Choice Questions Without the Question?](#arxiv-2402.12483) | 2024 | -0.07 | 4/7 | `arxiv:2402.12483` |
| 13 | [Learning to Compress Prompts with Gist Tokens](#arxiv-2304.08467) | 2023 | -0.12 | 4/7 | `arxiv:2304.08467` |
| 14 | [PRIMERA: Pyramid-based Masked Sentence Pre-training for Multi-document Summarization](#acl-2022.acl-long.360) | unknown | -0.13 | 3/7 | `acl:2022.acl-long.360` |
| 15 | [Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution](#arxiv-2309.16797) | 2023 | -0.25 | 4/7 | `arxiv:2309.16797` |
| 16 | [A System for Answering Simple Questions in Multiple Languages](#acl-2023.acl-demo.51) | unknown | -0.37 | 2/7 | `acl:2023.acl-demo.51` |
| 17 | [People cannot distinguish GPT-4 from a human in a Turing test](#arxiv-2405.08007) | 2024 | -0.40 | 1/7 | `arxiv:2405.08007` |

### Agents, open-endedness, AGI

| rank | title | year | final | accept | key |
|---:|---|---|---:|---:|---|
| 1 | [Robust agents learn causal world models (ICLR 2024 best paper)](#openreview-pOoKI3ouv1) | unknown | +0.72 | 6/7 | `openreview:pOoKI3ouv1` |
| 2 | [MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory](#arxiv-2601.03192) | 2026 | +0.54 | 6/7 | `arxiv:2601.03192` |
| 3 | [SPADE: Self-Play in Adaptive Synthetic Executable Environments](#arxiv-2608.19197) | 2026 | +0.45 | 6/7 | `arxiv:2608.19197` |
| 4 | [MemEvolve: Meta-Evolution of Agent Memory Systems](#arxiv-2512.18746) | 2025 | +0.45 | 5/7 | `arxiv:2512.18746` |
| 5 | [Learning Formal Mathematics From Intrinsic Motivation](#arxiv-2407.00695) | 2024 | +0.44 | 3/7 | `arxiv:2407.00695` |
| 6 | [Self-Improvements in Modern Agentic Systems: A Survey](#arxiv-2607.13104) | 2026 | +0.29 | 6/7 | `arxiv:2607.13104` |
| 7 | [Learning to Continually Learn via Meta-learning Agentic Memory Designs](#arxiv-2602.07755) | 2026 | +0.14 | 6/7 | `arxiv:2602.07755` |
| 8 | [Propose, Solve, Verify: Self-Play Through Formal Verification](#arxiv-2512.18160) | 2025 | +0.11 | 5/7 | `arxiv:2512.18160` |
| 9 | [Automated Design of Agentic Systems](#arxiv-2408.08435) | 2024 | +0.09 | 4/7 | `arxiv:2408.08435` |
| 10 | [Dr. Zero: Self-Evolving Search Agents without Training Data](#arxiv-2601.07055) | 2026 | +0.06 | 5/7 | `arxiv:2601.07055` |
| 11 | [Competition and Attraction Improve Model Fusion](#arxiv-2508.16204) | 2025 | +0.04 | 4/7 | `arxiv:2508.16204` |
| 12 | [Hyperagents](#arxiv-2603.19461) | 2026 | +0.04 | 6/7 | `arxiv:2603.19461` |
| 13 | [Harnessing Agentic Evolution](#arxiv-2605.13821) | 2026 | +0.04 | 5/7 | `arxiv:2605.13821` |
| 14 | [Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents](#arxiv-2505.22954) | 2025 | +0.03 | 4/7 | `arxiv:2505.22954` |
| 15 | [Meta Context Engineering via Agentic Skill Evolution](#arxiv-2601.21557) | 2026 | +0.00 | 5/7 | `arxiv:2601.21557` |
| 16 | [A Definition of Open-Ended Learning Problems for Goal-Conditioned Agents](#arxiv-2311.00344) | 2023 | -0.12 | 3/7 | `arxiv:2311.00344` |
| 17 | [Ouroboros: A Self-Developing Frontier Coding Agent with Reviewed Core Evolution](#arxiv-2608.08311) | 2026 | -0.16 | 3/7 | `arxiv:2608.08311` |
| 18 | [AlphaGo Moment for Model Architecture Discovery](#arxiv-2507.18074) | 2025 | -0.32 | 3/7 | `arxiv:2507.18074` |
| 19 | [Toward Training Superintelligent Software Agents through Self-Play SWE-RL](#arxiv-2512.18552) | 2025 | -0.33 | 3/7 | `arxiv:2512.18552` |
| 20 | [Open-Endedness is Essential for Artificial Superhuman Intelligence](#arxiv-2406.04268) | 2024 | -0.36 | 2/7 | `arxiv:2406.04268` |
| 21 | [Vending-Bench: A Benchmark for Long-Term Coherence of Autonomous Agents](#arxiv-2502.15840) | 2025 | -0.37 | 3/7 | `arxiv:2502.15840` |
| 22 | [Levels of AGI for Operationalizing Progress on the Path to AGI](#arxiv-2311.02462) | 2023 | -0.42 | 2/7 | `arxiv:2311.02462` |
| 23 | [AI-GAs: AI-generating algorithms, an alternate paradigm for producing general artificial intelligence](#arxiv-1905.10985) | 2019 | -0.45 | 1/7 | `arxiv:1905.10985` |
| 24 | [What Does It Take to Be a Good AI Research Agent? Studying the Role of Ideation Diversity](#arxiv-2511.15593) | 2025 | -0.59 | 2/7 | `arxiv:2511.15593` |
| 25 | [A social path to human-like artificial intelligence](#doi-10.1038-s42256-023-00754-x) | 2023 | -0.64 | 1/7 | `doi:10.1038/s42256-023-00754-x` |
| 26 | [AI Finds A Way](#arxiv-2608.23875) | 2026 | -0.68 | 2/7 | `arxiv:2608.23875` |
| 27 | [Self-Programming AI: Code-Learning Agents for Autonomous Refactoring and Architectural Evolution](#doi-10.21203-rs.3.rs-6688473-v1) | 2025 | -0.81 | 2/7 | `doi:10.21203/rs.3.rs-6688473/v1` |

### Harness

| rank | title | year | final | accept | key |
|---:|---|---|---:|---:|---|
| 1 | [Structured Scaling of AI Discovery Across Diverse Scientific Domains](#arxiv-2604.19341) | 2026 | +0.70 | 6/7 | `arxiv:2604.19341` |
| 2 | [Meta-Harness: End-to-End Optimization of Model Harnesses](#arxiv-2603.28052) | 2026 | +0.38 | 6/7 | `arxiv:2603.28052` |
| 3 | [Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System Deployment on Open-Ended Task Streams](#arxiv-2606.01770) | 2026 | +0.26 | 5/7 | `arxiv:2606.01770` |
| 4 | [Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses](#arxiv-2604.25850) | 2026 | +0.09 | 3/7 | `arxiv:2604.25850` |
| 5 | [HarnessDev: Can LLMs Create and Evolve Their Own Agent Harness?](#arxiv-2609.01437) | 2026 | -0.07 | 4/7 | `arxiv:2609.01437` |
| 6 | [Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering](#arxiv-2604.08224) | 2026 | -0.27 | 3/7 | `arxiv:2604.08224` |

### AI safety and consciousness

| rank | title | year | final | accept | key |
|---:|---|---|---:|---:|---|
| 1 | [Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming](#arxiv-2501.18837) | 2025 | +0.13 | 6/7 | `arxiv:2501.18837` |
| 2 | [Sparse Autoencoders Find Highly Interpretable Features in Language Models](#arxiv-2309.08600) | 2023 | +0.11 | 4/7 | `arxiv:2309.08600` |
| 3 | [When Activation Oracles Learn Not to Read: Concept-Specific Blind Spots in Fine-Tuned Oracles](#arxiv-2607.23379) | 2026 | +0.06 | 4/7 | `arxiv:2607.23379` |
| 4 | [Optimal Policies Tend to Seek Power](#arxiv-1912.01683) | 2019 | -0.01 | 3/7 | `arxiv:1912.01683` |
| 5 | [Consciousness in Artificial Intelligence: Insights from the Science of Consciousness](#arxiv-2308.08708) | 2023 | -0.02 | 4/7 | `arxiv:2308.08708` |
| 6 | [Is Power-Seeking AI an Existential Risk?](#arxiv-2206.13353) | 2022 | -0.07 | 3/7 | `arxiv:2206.13353` |
| 7 | [Parametrically Retargetable Decision-Makers Tend To Seek Power](#arxiv-2206.13477) | 2022 | -0.16 | 3/7 | `arxiv:2206.13477` |
| 8 | [Could a Large Language Model be Conscious?](#arxiv-2303.07103) | 2023 | -0.27 | 3/7 | `arxiv:2303.07103` |
| 9 | [Is Evaluation Awareness Just Format Sensitivity? Limitations of Probe-Based Evidence under Controlled Prompt Structure](#arxiv-2603.19426) | 2026 | -0.34 | 5/7 | `arxiv:2603.19426` |
| 10 | [Power-seeking can be probable and predictive for trained agents](#arxiv-2304.06528) | 2023 | -0.39 | 3/7 | `arxiv:2304.06528` |
| 11 | [Detecting Strategic Deception Using Linear Probes](#arxiv-2502.03407) | 2025 | -0.49 | 3/7 | `arxiv:2502.03407` |
| 12 | [Palatable Conceptions of Disembodied Being](#arxiv-2503.16348) | 2025 | -0.82 | 2/7 | `arxiv:2503.16348` |

### NeuroAI

| rank | title | year | final | accept | key |
|---:|---|---|---:|---:|---|
| 1 | [From Tokens to Thoughts: How LLMs and Humans Trade Compression for Meaning](#arxiv-2505.17117) | 2025 | +0.50 | 7/7 | `arxiv:2505.17117` |
| 2 | [Neural spiking for causal inference and learning](#doi-10.1371-journal.pcbi.1011005) | 2023 | +0.22 | 4/6 | `doi:10.1371/journal.pcbi.1011005` |
| 3 | [Attractor and integrator networks in the brain](#arxiv-2112.03978) | 2021 | +0.15 | 5/7 | `arxiv:2112.03978` |
| 4 | [Sleep prevents catastrophic forgetting in spiking neural networks by forming a joint synaptic weight representation](#doi-10.1371-journal.pcbi.1010628) | 2022 | +0.09 | 4/7 | `doi:10.1371/journal.pcbi.1010628` |
| 5 | [MetaWorm: An Integrative Data-Driven Model Simulating <i>C. elegans</i> Brain, Body and Environment Interactions](#doi-10.1101-2024.02.22.581686) | 2024 | +0.05 | 4/7 | `doi:10.1101/2024.02.22.581686` |
| 6 | [Emergence of belief-like representations through reinforcement learning](#doi-10.1101-2023.04.04.535512) | 2023 | +0.01 | 2/7 | `doi:10.1101/2023.04.04.535512` |
| 7 | [Relating transformers to models and neural representations of the hippocampal formation](#arxiv-2112.04035) | 2021 | -0.04 | 3/7 | `arxiv:2112.04035` |
| 8 | [Toward Next-Generation Artificial Intelligence: Catalyzing the NeuroAI Revolution](#arxiv-2210.08340) | 2022 | -0.16 | 3/7 | `arxiv:2210.08340` |
| 9 | [This is how the Neocortex Learns](#arxiv-2606.08720) | 2026 | -0.27 | 3/7 | `arxiv:2606.08720` |
| 10 | [Correspondence between neuroevolution and gradient descent](#doi-10.1038-s41467-021-26568-2) | 2021 | -0.43 | 3/7 | `doi:10.1038/s41467-021-26568-2` |

### Representation alignment

| rank | title | year | final | accept | key |
|---:|---|---|---:|---:|---|
| 1 | [Comparing representational geometries using whitened unbiased-distance-matrix similarity](#arxiv-2007.02789) | 2020 | +0.78 | 5/7 | `arxiv:2007.02789` |
| 2 | [Estimating Neural Representation Alignment from Sparsely Sampled Inputs and Features](#arxiv-2502.15104) | 2025 | +0.57 | 6/7 | `arxiv:2502.15104` |
| 3 | [Revisiting the Platonic Representation Hypothesis: An Aristotelian View](#arxiv-2602.14486) | 2026 | +0.39 | 5/7 | `arxiv:2602.14486` |
| 4 | [Proof of a perfect platonic representation hypothesis](#arxiv-2507.01098) | 2025 | -0.16 | 3/7 | `arxiv:2507.01098` |
| 5 | [The Platonic Representation Hypothesis](#arxiv-2405.07987) | 2024 | -0.21 | 3/6 | `arxiv:2405.07987` |
| 6 | [Correcting Biased Centered Kernel Alignment Measures in Biological and Artificial Neural Networks](#arxiv-2405.01012) | 2024 | -0.60 | 1/7 | `arxiv:2405.01012` |

### Finance

| rank | title | year | final | accept | key |
|---:|---|---|---:|---:|---|
| 1 | [INVESTORBENCH: A Benchmark for Financial Decision-Making Tasks with LLM-based Agent](#acl-2025.acl-long.126) | unknown | -0.23 | 2/7 | `acl:2025.acl-long.126` |
| 2 | [A Deep Reinforcement Learning Framework for the Financial Portfolio Management Problem](#arxiv-1706.10059) | 2017 | -0.78 | 0/7 | `arxiv:1706.10059` |
| 3 | [Applications of deep learning in stock market prediction: recent progress](#arxiv-2003.01859) | 2020 | -0.82 | 1/7 | `arxiv:2003.01859` |
| 4 | [Financial Trading as a Game: A Deep Reinforcement Learning Approach](#arxiv-1807.02787) | 2018 | -0.84 | 1/7 | `arxiv:1807.02787` |

### Books

| rank | title | year | final | accept | key |
|---:|---|---|---:|---:|---|
| 1 | [Deep Learning Interviews: Hundreds of fully solved job interview questions from a wide range of key topics in AI](#arxiv-2201.00650) | 2021 | -0.64 | 0/5 | `arxiv:2201.00650` |
| 2 | [Reinforcement Learning Textbook](#arxiv-2201.09746) | 2022 | -0.65 | 1/7 | `arxiv:2201.09746` |

### Other

| rank | title | year | final | accept | key |
|---:|---|---|---:|---:|---|
| 1 | [TPU v4: An Optically Reconfigurable Supercomputer for Machine Learning with Hardware Support for Embeddings](#arxiv-2304.01433) | 2023 | +0.11 | 3/6 | `arxiv:2304.01433` |
| 2 | [Inverse-designed low-index-contrast structures on a silicon photonics platform for vector–matrix multiplication](#doi-10.1038-s41566-024-01394-2) | 2024 | -0.24 | 2/6 | `doi:10.1038/s41566-024-01394-2` |
| 3 | [Fully parallel optical matrix-matrix multiplication](#arxiv-2309.10232) | 2023 | -0.86 | 0/7 | `arxiv:2309.10232` |

## DROP

`final_score` < -0.2 with conf >= 0.5 and impact_z below +0.5. Not a raw accept-vote count.

| title | section | year | final | conf | impact | accept |
|---|---|---|---:|---:|---:|---:|
| [Fully parallel optical matrix-matrix multiplication](#arxiv-2309.10232) | Other | 2023 | -0.86 | 0.71 | -2.00 | 0/7 |
| [Financial Trading as a Game: A Deep Reinforcement Learning Approach](#arxiv-1807.02787) | Finance | 2018 | -0.84 | 0.71 | -1.91 | 1/7 |
| [Palatable Conceptions of Disembodied Being](#arxiv-2503.16348) | AI safety and consciousness | 2025 | -0.82 | 0.71 | -2.26 | 2/7 |
| [Applications of deep learning in stock market prediction: recent progress](#arxiv-2003.01859) | Finance | 2020 | -0.82 | 0.71 | +0.30 | 1/7 |
| [Self-Programming AI: Code-Learning Agents for Autonomous Refactoring and Architectural Evolution](#doi-10.21203-rs.3.rs-6688473-v1) | Agents, open-endedness, AGI | 2025 | -0.81 | 0.71 | -0.34 | 2/7 |
| [Scaling of Search and Learning: A Roadmap to Reproduce o1 from Reinforcement Learning Perspective](#arxiv-2412.14135) | Reasoning and the "physics" of language models | 2024 | -0.80 | 0.71 | -1.50 | 0/7 |
| [Catastrophic Forgetting in Deep Learning: A Comprehensive Taxonomy](#arxiv-2312.10549) | Data, training, optimization | 2023 | -0.78 | 0.71 | -0.18 | 0/7 |
| [A Deep Reinforcement Learning Framework for the Financial Portfolio Management Problem](#arxiv-1706.10059) | Finance | 2017 | -0.78 | 0.71 | -2.19 | 0/7 |
| [Step-size Optimization for Continual Learning](#arxiv-2401.17401) | Data, training, optimization | 2024 | -0.78 | 0.70 | -2.36 | 1/7 |
| [Nested Learning: The Illusion of Deep Learning Architectures](#arxiv-2512.24695) | Data, training, optimization | 2025 | -0.75 | 0.68 | -2.20 | 0/6 |
| [A Path Towards Autonomous Machine Intelligence (LeCun, 2022)](#openreview-BZ5a1r-kVsf) | Self-supervised learning and vision | unknown | -0.73 | 0.70 | +0.06 | 2/7 |
| [GLU Variants Improve Transformer](#arxiv-2002.05202) | LLMs: architectures, context, training | 2020 | -0.70 | 0.71 | -1.07 | 1/7 |
| [A Cookbook of Self-Supervised Learning](#arxiv-2304.12210) | Self-supervised learning and vision | 2023 | -0.69 | 0.71 | +0.16 | 1/7 |
| [AI Finds A Way](#arxiv-2608.23875) | Agents, open-endedness, AGI | 2026 | -0.68 | 0.71 | -0.56 | 2/7 |
| [Evolutionary Strategies lead to Catastrophic Forgetting in LLMs](#arxiv-2601.20861) | Post-training | 2026 | -0.67 | 0.71 | -1.29 | 3/7 |
| [Benchmarking Batch Deep Reinforcement Learning Algorithms](#arxiv-1910.01708) | Reinforcement learning | 2019 | -0.67 | 0.71 | -1.16 | 2/7 |
| [Reinforcement Learning Textbook](#arxiv-2201.09746) | Books | 2022 | -0.65 | 0.61 | -0.58 | 1/7 |
| [Deep Learning Interviews: Hundreds of fully solved job interview questions from a wide range of key topics in AI](#arxiv-2201.00650) | Books | 2021 | -0.64 | 0.53 | -1.38 | 0/5 |
| [A social path to human-like artificial intelligence](#doi-10.1038-s42256-023-00754-x) | Agents, open-endedness, AGI | 2023 | -0.64 | 0.71 | -1.89 | 1/7 |
| [Measuring Catastrophic Forgetting in Neural Networks](#arxiv-1708.02072) | Data, training, optimization | 2017 | -0.63 | 0.71 | -0.42 | 2/7 |
| [Continual Backprop: Stochastic Gradient Descent with Persistent Randomness](#arxiv-2108.06325) | Data, training, optimization | 2021 | -0.62 | 0.71 | -1.86 | 0/7 |
| [Meta-Reinforcement Learning with Zero-Shot RL](#openreview-XyGJJ4FPoX) | Reinforcement learning | unknown | -0.61 | 0.71 | -0.87 | 0/7 |
| [A Minimalist Approach to Offline Reinforcement Learning](#arxiv-2106.06860) | Reinforcement learning | 2021 | -0.61 | 0.71 | -0.68 | 3/7 |
| [Correcting Biased Centered Kernel Alignment Measures in Biological and Artificial Neural Networks](#arxiv-2405.01012) | Representation alignment | 2024 | -0.60 | 0.71 | -1.36 | 1/7 |
| [What Does It Take to Be a Good AI Research Agent? Studying the Role of Ideation Diversity](#arxiv-2511.15593) | Agents, open-endedness, AGI | 2025 | -0.59 | 0.71 | -1.50 | 2/7 |
| [AI-rithmetic](#arxiv-2602.10416) | Reasoning and the "physics" of language models | 2026 | -0.53 | 0.71 | -0.02 | 2/7 |
| [Cyclical Learning Rates for Training Neural Networks](#arxiv-1506.01186) | Data, training, optimization | 2015 | -0.52 | 0.71 | -0.25 | 1/7 |
| [Your Transformer is Secretly Linear](#arxiv-2405.12250) | LLMs: architectures, context, training | 2024 | -0.52 | 0.71 | +0.12 | 3/7 |
| [Reinforcement Pre-Training](#arxiv-2506.08007) | Data, training, optimization | 2025 | -0.51 | 0.71 | -1.23 | 3/7 |
| [Addressing Function Approximation Error in Actor-Critic Methods](#arxiv-1802.09477) | Reinforcement learning | 2018 | -0.50 | 0.54 | -1.13 | 1/4 |
| [Detecting Strategic Deception Using Linear Probes](#arxiv-2502.03407) | AI safety and consciousness | 2025 | -0.49 | 0.71 | +0.23 | 3/7 |
| [To Compress or Not to Compress- Self-Supervised Learning and Information Theory: A Review](#arxiv-2304.09355) | Self-supervised learning and vision | 2023 | -0.47 | 0.70 | -0.21 | 1/7 |
| [Why mathematics is set to be revolutionized by AI](#doi-10.1038-d41586-024-01413-w) | Reasoning and the "physics" of language models | 2024 | -0.45 | 0.53 | -1.25 | 3/5 |
| [AI-GAs: AI-generating algorithms, an alternate paradigm for producing general artificial intelligence](#arxiv-1905.10985) | Agents, open-endedness, AGI | 2019 | -0.45 | 0.71 | -0.45 | 1/7 |
| [BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](#arxiv-2608.09888) | Post-training | 2026 | -0.43 | 0.71 | -0.42 | 2/7 |
| [Correspondence between neuroevolution and gradient descent](#doi-10.1038-s41467-021-26568-2) | NeuroAI | 2021 | -0.43 | 0.71 | -1.15 | 3/7 |
| [Levels of AGI for Operationalizing Progress on the Path to AGI](#arxiv-2311.02462) | Agents, open-endedness, AGI | 2023 | -0.42 | 0.71 | -0.25 | 2/7 |
| [Revisiting Rainbow: Promoting more Insightful and Inclusive Deep Reinforcement Learning Research](#arxiv-2011.14826) | Reinforcement learning | 2020 | -0.41 | 0.71 | -1.41 | 1/7 |
| [Self-Improving Pretraining: using post-trained models to pretrain better models](#arxiv-2601.21343) | Data, training, optimization | 2026 | -0.40 | 0.71 | -0.35 | 3/7 |
| [DAPO: An Open-Source LLM Reinforcement Learning System at Scale](#arxiv-2503.14476) | Post-training | 2025 | -0.40 | 0.71 | +0.37 | 3/7 |
| [Continual Learning and Catastrophic Forgetting](#arxiv-2403.05175) | Data, training, optimization | 2024 | -0.39 | 0.71 | -1.07 | 2/7 |
| [Learning in High Dimension Always Amounts to Extrapolation](#arxiv-2110.09485) | Data, training, optimization | 2021 | -0.39 | 0.71 | -0.44 | 1/7 |
| [Large Language Models Still Can't Plan / PlanBench (Kambhampati)](#openreview-wUU-7XTL5XO) | Reasoning and the "physics" of language models | unknown | -0.39 | 0.71 | +0.29 | 2/7 |
| [Power-seeking can be probable and predictive for trained agents](#arxiv-2304.06528) | AI safety and consciousness | 2023 | -0.39 | 0.71 | +0.30 | 3/7 |
| [T5Gemma 2: Seeing, Reading, and Understanding Longer](#arxiv-2512.14856) | LLMs: architectures, context, training | 2025 | -0.39 | 0.71 | -0.26 | 2/7 |
| [Position: LLMs can't jump](#openreview-klU4737opt) | Reasoning and the "physics" of language models | unknown | -0.37 | 0.71 | -1.34 | 2/7 |
| [Vending-Bench: A Benchmark for Long-Term Coherence of Autonomous Agents](#arxiv-2502.15840) | Agents, open-endedness, AGI | 2025 | -0.37 | 0.71 | -0.32 | 3/7 |
| [Energy Transformer](#arxiv-2302.07253) | LLMs: architectures, context, training | 2023 | -0.37 | 0.71 | -0.72 | 4/7 |
| [A System for Answering Simple Questions in Multiple Languages](#acl-2023.acl-demo.51) | Retrieval, embeddings, benchmarks | unknown | -0.37 | 0.70 | -0.96 | 2/7 |
| [Open-Endedness is Essential for Artificial Superhuman Intelligence](#arxiv-2406.04268) | Agents, open-endedness, AGI | 2024 | -0.36 | 0.71 | +0.33 | 2/7 |
| [Is Evaluation Awareness Just Format Sensitivity? Limitations of Probe-Based Evidence under Controlled Prompt Structure](#arxiv-2603.19426) | AI safety and consciousness | 2026 | -0.34 | 0.71 | -1.53 | 5/7 |
| [Toward Training Superintelligent Software Agents through Self-Play SWE-RL](#arxiv-2512.18552) | Agents, open-endedness, AGI | 2025 | -0.33 | 0.71 | -0.56 | 3/7 |
| [Language is primarily a tool for communication rather than thought](#doi-10.1038-s41586-024-07522-w) | Reasoning and the "physics" of language models | 2024 | -0.33 | 0.62 | -2.64 | 4/5 |
| [Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved)](#arxiv-2507.12856) | Data, training, optimization | 2025 | -0.32 | 0.71 | -2.11 | 3/7 |
| [Weight-Space Geometry of Offline Reasoning Training](#arxiv-2606.23740) | Post-training | 2026 | -0.32 | 0.71 | -0.97 | 2/7 |
| [LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks](#arxiv-2402.01817) | Reasoning and the "physics" of language models | 2024 | -0.31 | 0.71 | -0.17 | 2/7 |
| [MetaOptimize: A Framework for Optimizing Step Sizes and Other Meta-parameters](#arxiv-2402.02342) | Data, training, optimization | 2024 | -0.30 | 0.71 | -1.71 | 3/7 |
| [Klear-Reasoner: Advancing Reasoning Capability via Gradient-Preserving Clipping Policy Optimization](#arxiv-2508.07629) | Post-training | 2025 | -0.28 | 0.68 | -0.90 | 3/6 |
| [This is how the Neocortex Learns](#arxiv-2606.08720) | NeuroAI | 2026 | -0.27 | 0.70 | -1.69 | 3/7 |
| [Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution](#arxiv-2309.16797) | Retrieval, embeddings, benchmarks | 2023 | -0.25 | 0.71 | +0.36 | 4/7 |
| [Inverse-designed low-index-contrast structures on a silicon photonics platform for vector–matrix multiplication](#doi-10.1038-s41566-024-01394-2) | Other | 2024 | -0.24 | 0.68 | -1.51 | 2/6 |
| [Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs?](#arxiv-2603.24472) | Post-training | 2026 | -0.24 | 0.71 | +0.19 | 3/7 |
| [INVESTORBENCH: A Benchmark for Financial Decision-Making Tasks with LLM-based Agent](#acl-2025.acl-long.126) | Finance | unknown | -0.23 | 0.70 | -0.08 | 2/7 |
| [Can Large Reasoning Models Self-Train?](#arxiv-2505.21444) | Reasoning and the "physics" of language models | 2025 | -0.23 | 0.71 | -0.82 | 2/7 |
| [A Mechanistic Analysis of Looped Reasoning Language Models](#arxiv-2604.11791) | Reasoning and the "physics" of language models | 2026 | -0.21 | 0.71 | -1.38 | 3/7 |
| [The Platonic Representation Hypothesis](#arxiv-2405.07987) | Representation alignment | 2024 | -0.21 | 0.68 | +0.00 | 3/6 |
| [Latent Cache Flow: Model-to-Model Communication Without Text](#arxiv-2605.22863) | LLMs: architectures, context, training | 2026 | -0.20 | 0.71 | -0.72 | 4/7 |

## WATCH

Missing impact_z, conf < 0.5, |final_score| <= 0.2, or low score with high predicted impact. Showing 40 of 131.

| title | section | year | final | conf | impact | accept |
|---|---|---|---:|---:|---:|---:|
| [Offline Reinforcement Learning: Tutorial, Review, and Perspectives on Open Problems](#arxiv-2005.01643) | Reinforcement learning | 2020 | -0.59 | 0.71 | +0.54 | 0/7 |
| [xLSTM: Extended Long Short-Term Memory](#arxiv-2405.04517) | LLMs: architectures, context, training | 2024 | -0.44 | 0.71 | +0.60 | 2/7 |
| [People cannot distinguish GPT-4 from a human in a Turing test](#arxiv-2405.08007) | Retrieval, embeddings, benchmarks | 2024 | -0.40 | 0.71 | +2.09 | 1/7 |
| [Competitive Programming with Large Reasoning Models](#arxiv-2502.06807) | Reasoning and the "physics" of language models | 2025 | -0.33 | 0.71 | +0.55 | 4/7 |
| [Tune-A-Video: One-Shot Tuning of Image Diffusion Models for Text-to-Video Generation](#arxiv-2212.11565) | Self-supervised learning and vision | 2022 | -0.32 | 0.71 | +0.84 | 3/7 |
| [AlphaGo Moment for Model Architecture Discovery](#arxiv-2507.18074) | Agents, open-endedness, AGI | 2025 | -0.32 | 0.71 | +1.12 | 3/7 |
| [Knowledge Mechanisms in Large Language Models: A Survey and Perspective](#arxiv-2407.15017) | Reasoning and the "physics" of language models | 2024 | -0.32 | 0.71 | +0.68 | 3/7 |
| [Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering](#arxiv-2604.08224) | Harness | 2026 | -0.27 | 0.71 | +1.26 | 3/7 |
| [Could a Large Language Model be Conscious?](#arxiv-2303.07103) | AI safety and consciousness | 2023 | -0.27 | 0.70 | +0.74 | 3/7 |
| [The Lookahead Limitation: Why Multi-Operand Addition is Hard for LLMs](#arxiv-2502.19981) | Reasoning and the "physics" of language models | 2025 | -0.23 | 0.71 | +0.63 | 3/7 |
| [Towards General-Purpose Model-Free Reinforcement Learning](#arxiv-2501.16142) | Reinforcement learning | 2025 | -0.16 | 0.71 | -1.10 | 5/7 |
| [Ouroboros: A Self-Developing Frontier Coding Agent with Reviewed Core Evolution](#arxiv-2608.08311) | Agents, open-endedness, AGI | 2026 | -0.16 | 0.71 | -0.75 | 3/7 |
| [RIFT: A RubrIc Failure Mode Taxonomy and Automated Diagnostics](#arxiv-2604.01375) | Post-training | 2026 | -0.16 | 0.71 | -0.30 | 3/7 |
| [Parametrically Retargetable Decision-Makers Tend To Seek Power](#arxiv-2206.13477) | AI safety and consciousness | 2022 | -0.16 | 0.71 | +0.99 | 3/7 |
| [Cramming: Training a Language Model on a Single GPU in One Day](#arxiv-2212.14034) | Data, training, optimization | 2022 | -0.16 | 0.71 | -0.92 | 3/7 |
| [Proof of a perfect platonic representation hypothesis](#arxiv-2507.01098) | Representation alignment | 2025 | -0.16 | 0.71 | -2.72 | 3/7 |
| [The First Few Tokens Are All You Need: An Efficient and Effective Unsupervised Prefix Fine-Tuning Method for Reasoning Models](#arxiv-2503.02875) | Post-training | 2025 | -0.16 | 0.71 | +0.94 | 3/7 |
| [Toward Next-Generation Artificial Intelligence: Catalyzing the NeuroAI Revolution](#arxiv-2210.08340) | NeuroAI | 2022 | -0.16 | 0.70 | -1.25 | 3/7 |
| [TransformerFAM: Feedback attention is working memory](#arxiv-2404.09173) | LLMs: architectures, context, training | 2024 | -0.15 | 0.71 | +0.30 | 3/7 |
| [Language Models Are Capable of Metacognitive Monitoring and Control of Their Internal Activations](#arxiv-2505.13763) | Reasoning and the "physics" of language models | 2025 | -0.15 | 0.71 | +0.06 | 4/7 |
| [Rainbow: Combining Improvements in Deep Reinforcement Learning](#arxiv-1710.02298) | Reinforcement learning | 2017 | -0.14 | 0.71 | +1.07 | 3/7 |
| [From Explicit CoT to Implicit CoT: Learning to Internalize CoT Step by Step](#arxiv-2405.14838) | Reasoning and the "physics" of language models | 2024 | -0.14 | 0.71 | +0.04 | 4/7 |
| [PRIMERA: Pyramid-based Masked Sentence Pre-training for Multi-document Summarization](#acl-2022.acl-long.360) | Retrieval, embeddings, benchmarks | unknown | -0.13 | 0.70 | +0.69 | 3/7 |
| [A Definition of Open-Ended Learning Problems for Goal-Conditioned Agents](#arxiv-2311.00344) | Agents, open-endedness, AGI | 2023 | -0.12 | 0.71 | -1.56 | 3/7 |
| [Leave No Context Behind: Efficient Infinite Context Transformers with Infini-attention](#arxiv-2404.07143) | LLMs: architectures, context, training | 2024 | -0.12 | 0.71 | +0.62 | 3/7 |
| [Learning to Compress Prompts with Gist Tokens](#arxiv-2304.08467) | Retrieval, embeddings, benchmarks | 2023 | -0.12 | 0.71 | +0.16 | 4/7 |
| [VICReg: Variance-Invariance-Covariance Regularization for Self-Supervised Learning](#arxiv-2105.04906) | Self-supervised learning and vision | 2021 | -0.11 | 0.71 | +0.07 | 3/7 |
| [Evidence from formal logical reasoning reveals that the language of thought is not natural language](#doi-10.1073-pnas.2520095123) | Reasoning and the "physics" of language models | 2026 | -0.11 | 0.70 | -1.14 | 5/7 |
| [It Takes Two: Your GRPO Is Secretly DPO](#arxiv-2510.00977) | Post-training | 2025 | -0.10 | 0.71 | -1.18 | 5/7 |
| [Self-Distillation Enables Continual Learning](#arxiv-2601.19897) | Post-training | 2026 | -0.09 | 0.71 | +0.62 | 6/7 |
| [gzip Predicts Data-dependent Scaling Laws](#arxiv-2405.16684) | Data, training, optimization | 2024 | -0.09 | 0.71 | -0.80 | 3/7 |
| [Revisiting On-Policy Distillation: Empirical Failure Modes and Simple Fixes](#arxiv-2603.25562) | Post-training | 2026 | -0.09 | 0.71 | +0.39 | 5/7 |
| [Emergent Hierarchical Reasoning in LLMs through Reinforcement Learning](#arxiv-2509.03646) | Post-training | 2025 | -0.09 | 0.71 | +0.33 | 3/7 |
| [iGRPO: Self-Feedback-Driven LLM Reasoning](#arxiv-2602.09000) | Post-training | 2026 | -0.08 | 0.71 | +0.61 | 4/7 |
| [Super-Convergence: Very Fast Training of Neural Networks Using Large Learning Rates](#arxiv-1708.07120) | Data, training, optimization | 2017 | -0.07 | 0.71 | -0.34 | 3/7 |
| [HarnessDev: Can LLMs Create and Evolve Their Own Agent Harness?](#arxiv-2609.01437) | Harness | 2026 | -0.07 | 0.71 | -0.15 | 4/7 |
| [Is Power-Seeking AI an Existential Risk?](#arxiv-2206.13353) | AI safety and consciousness | 2022 | -0.07 | 0.71 | +1.32 | 3/7 |
| [Single-stream Policy Optimization](#arxiv-2509.13232) | Post-training | 2025 | -0.07 | 0.71 | +0.37 | 5/7 |
| [From $f(x)$ and $g(x)$ to $f(g(x))$: LLMs Learn New Skills in RL by Composing Old Ones](#arxiv-2509.25123) | Post-training | 2025 | -0.07 | 0.71 | -0.13 | 5/7 |
| [Artifacts or Abduction: How Do LLMs Answer Multiple-Choice Questions Without the Question?](#arxiv-2402.12483) | Retrieval, embeddings, benchmarks | 2024 | -0.07 | 0.71 | +0.87 | 4/7 |

## Per paper

<a id="arxiv-2608.17163"></a>
### Q-Learning With World Models

`arxiv:2608.17163` · Reinforcement learning · 2026-08-17

- final **+0.11** (conf 0.71, pct 53) · impact -1.00 · WATCH
- mean rating (1–10): **6.0** · accept votes **6/7** · percentile rank_avg 54.2 (100=best) · rank in year 43.0 (1=best)
- NAIPv2 `-0.711` · NAIP-v1 `0.593` · SciJudge `-4.647` · DGC-BERT `0.760`
- CycleReviewer 8B `5.8` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/2.5) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [boris_again/4075](https://t.me/boris_again/4075), [AGI_and_RL/1351](https://t.me/AGI_and_RL/1351)
- Weaknesses: cyclereviewer-8b: Weaknesses  The main weakness of the paper is that the authors do not provide a theoretical analysis of their method. While the authors do provide some experimental results, the results are limited to a few tasks and do not provide a comprehensive evaluation of the method. In particular, the authors do not provide a comparison with other model-based RL methods or other methods that use world model deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2509.09675"></a>
### CDE: Curiosity-Driven Exploration for Efficient Reinforcement Learning in Large Language Models

`arxiv:2509.09675` · Reinforcement learning · 2025-09-11

- final **+0.14** (conf 0.71, pct 56) · impact -1.15 · WATCH
- mean rating (1–10): **6.0** · accept votes **6/7** · percentile rank_avg 51.4 (100=best) · rank in year 51.0 (1=best)
- NAIPv2 `-0.663` · NAIP-v1 `0.401` · SciJudge `-2.386` · DGC-BERT `0.946`
- CycleReviewer 8B `5.8` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `5.8` Accept (S/P/C 2.6/2.6/2.4) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/7659](https://t.me/axisofordinary/7659)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The novelty of the paper is limited. The idea of using perplexity as a curiosity signal is not new. There are many papers that use perplexity as a curiosity signal for exploration. For example, (1) uses perplexity as a curiosity signal for exploration in RL. The idea of using the variance of value estimates as a curiosity signal is also not new. There are many papers that use the va cyclereviewer-8b.seed1: Weaknesses  1. The experiments are not convincing. The au

<a id="arxiv-2503.14858"></a>
### 1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities

`arxiv:2503.14858` · Reinforcement learning · 2025-03-19

- final **-0.02** (conf 0.71, pct 36) · impact -0.15 · WATCH
- mean rating (1–10): **5.5** · accept votes **5/7** · percentile rank_avg 45.9 (100=best) · rank in year 64.0 (1=best)
- NAIPv2 `0.184` · NAIP-v1 `0.590` · SciJudge `-0.760` · DGC-BERT `0.755`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.5` Reject · 7B Fast `5.7` Accept (S/P/C 2.67/3.0/2.67) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/7998](https://t.me/axisofordinary/7998)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The contribution of this paper is limited. The authors only show that increasing the depth of the model can improve the performance of self-supervised RL. However, the authors do not provide any theoretical analysis or explanation for the improvement. 2. The authors only show the results of contrastive RL. It is unclear whether the improvement also applies to other self-supervised R deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2501.16142"></a>
### Towards General-Purpose Model-Free Reinforcement Learning

`arxiv:2501.16142` · Reinforcement learning · 2025-01-27

- final **-0.16** (conf 0.71, pct 24) · impact -1.10 · WATCH
- mean rating (1–10): **5.7** · accept votes **5/7** · percentile rank_avg 41.1 (100=best) · rank in year 68.0 (1=best)
- NAIPv2 `-1.769` · NAIP-v1 `0.462` · SciJudge `-3.849` · DGC-BERT `0.865`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `4.8` Reject (S/P/C 2.25/2.5/2.5) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/6926](https://t.me/axisofordinary/6926), [AGI_and_RL/988](https://t.me/AGI_and_RL/988)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The novelty is limited. The idea of learning a representation that captures a linear relationship between state-action pairs and value is not new, and has been explored in previous works such as TD7 and many other representation learning methods. The main difference is that the proposed method learns the representation using a model-based approach, but the model is not used for plan deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2411.03820"></a>
### Beyond The Rainbow: High Performance Deep Reinforcement Learning on a Desktop PC

`arxiv:2411.03820` · Reinforcement learning · 2024-11-06

- final **+0.17** (conf 0.71, pct 58) · impact -0.70 · WATCH
- mean rating (1–10): **5.8** · accept votes **2/7** · percentile rank_avg 41.8 (100=best) · rank in year 28.0 (1=best)
- NAIPv2 `0.004` · NAIP-v1 `0.487` · SciJudge `-3.803` · DGC-BERT `0.091`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `5.8` Reject (S/P/C 3.0/3.25/2.75) · 14B Fast `5.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `7.0` Accept
- Telegram: [j_links/7764](https://t.me/j_links/7764)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper does not provide a detailed analysis of the computational resources required to train the agent. It would be helpful to provide a more detailed breakdown of the computational resources required, such as the number of GPUs, CPU cores, and memory required to train the agent. 2. The paper does not provide a detailed analysis of the hyperparameters used to train the agent. It  deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2312.13327"></a>
### In-Context Reinforcement Learning for Variable Action Spaces

`arxiv:2312.13327` · Reinforcement learning · 2023-12-20

- final **-0.06** (conf 0.71, pct 34) · impact -1.36 · WATCH
- mean rating (1–10): **5.7** · accept votes **4/7** · percentile rank_avg 37.1 (100=best) · rank in year 40.0 (1=best)
- NAIPv2 `0.215` · NAIP-v1 `0.453` · SciJudge `-5.308` · DGC-BERT `0.658`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `4.0` Reject · 7B Fast `6.0` Accept (S/P/C 2.5/3.0/2.75) · 14B Fast `5.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [knowledge_accumulator/204](https://t.me/knowledge_accumulator/204), [ai_newz/3059](https://t.me/ai_newz/3059), [boris_again/2678](https://t.me/boris_again/2678), [data_secrets/4591](https://t.me/data_secrets/4591)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The novelty of the proposed method is limited. The main idea of using random embeddings for actions is not new and has been used in previous work (1). The contrastive loss is also not new. - The experiments are not sufficient. The paper only evaluates the proposed method on simple environments such as Bernoulli bandit and Darkroom. More complex environments are needed to show the eff deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2312.00276"></a>
### Metalearning Continual Learning Algorithms

`arxiv:2312.00276` · Reinforcement learning · 2023-12-01

- final **+0.11** (conf 0.71, pct 54) · impact -0.79 · WATCH
- mean rating (1–10): **5.6** · accept votes **5/7** · percentile rank_avg 40.4 (100=best) · rank in year 33.0 (1=best)
- NAIPv2 `-2.000` · NAIP-v1 `0.537` · SciJudge `-2.953` · DGC-BERT `0.504`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `8.0` Accept · 7B Fast `5.7` Reject (S/P/C 2.67/2.67/2.67) · 14B Fast `5.8` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [knowledge_accumulator/145](https://t.me/knowledge_accumulator/145)
- Weaknesses: cyclereviewer-8b: Weaknesses  The proposed method is not novel. The authors claim that their method is novel because it is the first to meta-learn a learning algorithm for continual learning. However, there are many prior works that have done the same thing. For example, see (1, 2, 3).  (1) Learning to Learn for Continual Learning  (2) Meta-Continual Learning: A Continual Learning Framework Using Meta-Learning  (3) cyclereviewer-8b.seed1: Weaknesses  - The method seems to be a straightforward ap

<a id="arxiv-2306.02451"></a>
### For SALE: State-Action Representation Learning for Deep Reinforcement Learning

`arxiv:2306.02451` · Reinforcement learning · 2023-06-04

- final **+0.05** (conf 0.71, pct 46) · impact -1.30 · WATCH
- mean rating (1–10): **5.6** · accept votes **5/7** · percentile rank_avg 45.0 (100=best) · rank in year 29.0 (1=best)
- NAIPv2 `-2.250` · NAIP-v1 `0.436` · SciJudge `-3.172` · DGC-BERT `0.900`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `8.0` Accept · 7B Fast `6.2` Accept (S/P/C 2.75/2.5/2.5) · 14B Fast `4.7` Reject
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [AGI_and_RL/988](https://t.me/AGI_and_RL/988)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The proposed method is an extension of OFENet, and the main difference is the clipping of the target value function. However, the authors do not provide a theoretical justification for the clipping operation, and it is unclear why this is necessary. - The authors do not provide a clear explanation of how the state-action representation is used in the RL algorithm. It is unclear how t deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2305.19452"></a>
### Bigger, Better, Faster: Human-level Atari with human-level efficiency

`arxiv:2305.19452` · Reinforcement learning · 2023-05-30

- final **+0.28** (conf 0.71, pct 72) · impact -0.29 · KEEP
- mean rating (1–10): **5.8** · accept votes **3/7** · percentile rank_avg 51.6 (100=best) · rank in year 20.0 (1=best)
- NAIPv2 `1.444` · NAIP-v1 `0.643` · SciJudge `-2.788` · DGC-BERT `0.799`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `6.0` Reject (S/P/C 3.0/3.25/2.5) · 14B Fast `6.2` Accept
- OpenReviewer `5.0` Reject (S/P/C 2.0/3.0/2.0) · SEA-E `7.0` Accept
- Telegram: [knowledge_accumulator/194](https://t.me/knowledge_accumulator/194), [axisofordinary/5007](https://t.me/axisofordinary/5007)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper does not provide any new algorithmic contributions. The proposed method is a combination of existing techniques, including SR-SPR, Impala-CNN, and other design choices. - The paper does not provide any theoretical analysis of the proposed method. - The paper does not provide any experimental results on other benchmarks, such as the Atari 500K benchmark or the Atari 1M bench deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2301.04104"></a>
### Mastering Diverse Domains through World Models

`arxiv:2301.04104` · Reinforcement learning · 2023-01-10

- final **+0.19** (conf 0.71, pct 61) · impact +1.64 · WATCH
- mean rating (1–10): **6.1** · accept votes **5/7** · percentile rank_avg 58.7 (100=best) · rank in year 9.0 (1=best)
- NAIPv2 `-1.748` · NAIP-v1 `0.739` · SciJudge `3.516` · DGC-BERT `0.596`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.2` Reject · 7B Fast `7.0` Accept (S/P/C 3.0/3.0/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/4175](https://t.me/gonzo_ML/4175), [knowledge_accumulator/155](https://t.me/knowledge_accumulator/155), [gonzo_ML/1791](https://t.me/gonzo_ML/1791), [ai_newz/1700](https://t.me/ai_newz/1700), [j_links/6396](https://t.me/j_links/6396), [AGI_and_RL/988](https://t.me/AGI_and_RL/988)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper lacks a detailed comparison with previous work, particularly in terms of the specific hyperparameters used and the computational resources required. 2. The paper does not provide a clear explanation of the intuition behind the proposed algorithm and how it addresses the challenges of reinforcement learning. 3. The paper does not provide a detailed analysis of the computati cyclereviewer-8b.seed1: Weaknesses  The paper presents a new algorithm for reinfo

<a id="openreview-XyGJJ4FPoX"></a>
### Meta-Reinforcement Learning with Zero-Shot RL

`openreview:XyGJJ4FPoX` · Reinforcement learning · unknown

- final **-0.61** (conf 0.71, pct 7) · impact -0.87 · DROP
- mean rating (1–10): **4.7** · accept votes **0/7** · percentile rank_avg 17.5 (100=best) · rank in year 12.0 (1=best)
- NAIPv2 `-3.945` · NAIP-v1 `0.472` · SciJudge `-3.924` · DGC-BERT `0.183`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `5.7` Reject (S/P/C 2.67/2.33/2.33) · 14B Fast `4.2` Reject
- OpenReviewer `5.0` Reject (S/P/C 2.0/3.0/2.0) · SEA-E `4.0` Reject
- Telegram: [j_links/8463](https://t.me/j_links/8463)
- Weaknesses: cyclereviewer-8b: Weaknesses  The proposed method is a combination of existing methods and the novelty is limited. The experiments are not convincing enough. The proposed method does not show significant improvement over existing methods.  ### Questions  1. The proposed method is a combination of existing methods. What is the main contribution of this paper? 2. The experiments are not convincing enough. The propose deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="openreview-OpC-9aBBVJe"></a>
### Sample-Efficient RL by Breaking the Replay Ratio Barrier (ICLR 2023, precursor of BBF)

`openreview:OpC-9aBBVJe` · Reinforcement learning · unknown

- final **+0.18** (conf 0.71, pct 60) · impact +0.67 · WATCH
- mean rating (1–10): **6.0** · accept votes **6/7** · percentile rank_avg 49.7 (100=best) · rank in year 3.0 (1=best)
- NAIPv2 `-1.396` · NAIP-v1 `0.698` · SciJudge `1.251` · DGC-BERT `0.016`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.8` Accept · 7B Fast `5.8` Accept (S/P/C 2.75/2.75/2.25) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/4.0/3.0) · SEA-E `6.0` Accept
- Telegram: [knowledge_accumulator/194](https://t.me/knowledge_accumulator/194)
- Weaknesses: cyclereviewer-8b: Weaknesses  The main weakness of the paper is the novelty of the approach. The idea of resetting the parameters periodically has been proposed in previous works (e.g., Nikishin et al., 2022). The authors do not provide a theoretical analysis of the proposed approach. The results are only evaluated on two benchmarks and the baselines are not up-to-date. For example, the authors only compare with RE deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2205.07802"></a>
### The Primacy Bias in Deep Reinforcement Learning

`arxiv:2205.07802` · Reinforcement learning · 2022-05-16

- final **+0.35** (conf 0.71, pct 78) · impact -1.50 · KEEP
- mean rating (1–10): **6.1** · accept votes **6/7** · percentile rank_avg 47.9 (100=best) · rank in year 13.0 (1=best)
- NAIPv2 `-1.850` · NAIP-v1 `0.358` · SciJudge `-3.554` · DGC-BERT `0.855`
- CycleReviewer 8B `4.8` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.5` Accept (S/P/C 3.0/3.5/2.75) · 14B Fast `6.2` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [knowledge_accumulator/188](https://t.me/knowledge_accumulator/188), [j_links/5862](https://t.me/j_links/5862)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The proposed method is not novel. The idea of resetting part of the network has been explored in the supervised learning literature (e.g., (1, 2, 3)). The authors should discuss the difference between their method and the existing work. - The authors only consider discrete and continuous control tasks. The authors should also consider more complex tasks, such as robotics manipulation deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2106.06860"></a>
### A Minimalist Approach to Offline Reinforcement Learning

`arxiv:2106.06860` · Reinforcement learning · 2021-06-12

- final **-0.61** (conf 0.71, pct 7) · impact -0.68 · DROP
- mean rating (1–10): **5.0** · accept votes **3/7** · percentile rank_avg 26.5 (100=best) · rank in year 10.0 (1=best)
- NAIPv2 `-3.971` · NAIP-v1 `0.426` · SciJudge `1.049` · DGC-BERT `0.685`
- CycleReviewer 8B `3.8` Reject · 70B `` 
- DeepReviewer 7B Std `3.5` Reject · 7B Fast `4.2` Reject (S/P/C 2.25/2.25/2.0) · 14B Fast `5.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [AGI_and_RL/988](https://t.me/AGI_and_RL/988)
- Weaknesses: cyclereviewer-8b: Weaknesses  The main weakness of the paper is that the proposed method is not novel. The idea of adding a behavior cloning term to the policy update is not new and has been explored in several previous works (see the related work section). The only novelty of this paper is the specific formulation of the behavior cloning loss, which is not very well motivated. The authors do not provide any theore deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2011.14826"></a>
### Revisiting Rainbow: Promoting more Insightful and Inclusive Deep Reinforcement Learning Research

`arxiv:2011.14826` · Reinforcement learning · 2020-11-20

- final **-0.41** (conf 0.71, pct 12) · impact -1.41 · DROP
- mean rating (1–10): **4.4** · accept votes **1/7** · percentile rank_avg 17.8 (100=best) · rank in year 10.0 (1=best)
- NAIPv2 `-3.248` · NAIP-v1 `0.415` · SciJudge `-3.891` · DGC-BERT `0.397`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `5.2` Reject (S/P/C 2.25/2.75/2.25) · 14B Fast `4.8` Reject
- OpenReviewer `3.0` Reject (S/P/C 3.0/2.0/2.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper lacks novelty in terms of the experiments performed. The authors have not introduced any new algorithms or techniques, but rather have performed experiments on existing ones. The paper would benefit from more in-depth analysis and insights from the experiments.  ### Questions  1. What are the limitations of the paper? How can they be addressed in future work? 2. What are the  cyclereviewer-8b.seed1: Weaknesses  1. The contribution of this paper is limited.

<a id="arxiv-2005.01643"></a>
### Offline Reinforcement Learning: Tutorial, Review, and Perspectives on Open Problems

`arxiv:2005.01643` · Reinforcement learning · 2020-05-04

- final **-0.59** (conf 0.71, pct 8) · impact +0.54 · WATCH
- mean rating (1–10): **4.2** · accept votes **0/7** · percentile rank_avg 23.5 (100=best) · rank in year 8.0 (1=best)
- NAIPv2 `-4.117` · NAIP-v1 `0.684` · SciJudge `2.038` · DGC-BERT `0.060`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.0` Reject · 7B Fast `5.7` Reject (S/P/C 3.0/3.0/2.0) · 14B Fast `4.3` Reject
- OpenReviewer `5.0` Reject (S/P/C 3.0/2.0/2.0) · SEA-E `3.0` Reject
- Telegram: [gonzo_ML/722](https://t.me/gonzo_ML/722), [j_links/3476](https://t.me/j_links/3476)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper is a tutorial paper and does not present any new results or contributions to the field of offline reinforcement learning. The paper does not provide any new insights or perspectives on the field, and it does not discuss any of the recent advances or developments in the field. The paper also does not provide any empirical evaluations or comparisons of the different algorithms  deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2004.12919"></a>
### First return, then explore

`arxiv:2004.12919` · Reinforcement learning · 2020-04-27

- final **+0.68** (conf 0.71, pct 98) · impact +1.54 · KEEP
- mean rating (1–10): **6.2** · accept votes **6/7** · percentile rank_avg 67.1 (100=best) · rank in year 2.0 (1=best)
- NAIPv2 `-0.674` · NAIP-v1 `0.851` · SciJudge `2.038` · DGC-BERT `0.740`
- CycleReviewer 8B `2.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `7.3` Accept (S/P/C 3.67/3.33/3.33) · 14B Fast `6.2` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [j_links/3440](https://t.me/j_links/3440)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper's novelty is limited, as the idea of exploring promising states and returning to them is not a new concept in the field of reinforcement learning. The paper does not provide a clear justification for why this approach is necessary or how it differs from existing methods. 2. The paper lacks a thorough comparison with existing exploration algorithms, making it difficult to a deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-1910.01708"></a>
### Benchmarking Batch Deep Reinforcement Learning Algorithms

`arxiv:1910.01708` · Reinforcement learning · 2019-10-03

- final **-0.67** (conf 0.71, pct 5) · impact -1.16 · DROP
- mean rating (1–10): **4.2** · accept votes **2/7** · percentile rank_avg 19.1 (100=best) · rank in year 4.0 (1=best)
- NAIPv2 `-2.742` · NAIP-v1 `0.356` · SciJudge `-0.785` · DGC-BERT `0.787`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `3.0` Reject · 7B Fast `3.5` Reject (S/P/C 2.25/2.25/2.0) · 14B Fast `3.5` Reject
- OpenReviewer `5.0` Reject (S/P/C 2.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [AGI_and_RL/988](https://t.me/AGI_and_RL/988)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper only considers a single partially-trained behavioral policy for data generation, which may not be representative of real-world scenarios where data is generated by multiple policies. It would be interesting to see how the algorithms perform with data generated by multiple policies. 2. The paper only considers a single batch size of 10 million transitions, which may not be  deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-1802.09477"></a>
### Addressing Function Approximation Error in Actor-Critic Methods

`arxiv:1802.09477` · Reinforcement learning · 2018-02-26

- final **-0.50** (conf 0.54, pct 9) · impact -1.13 · DROP
- mean rating (1–10): **4.3** · accept votes **1/4** · percentile rank_avg 26.8 (100=best) · rank in year 3.0 (1=best)
- NAIPv2 `-3.898` · NAIP-v1 `0.363` · SciJudge `-0.461` · DGC-BERT `0.888`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std ``  · 7B Fast ``  (S/P/C None/None/None) · 14B Fast `` 
- OpenReviewer `3.0` Reject (S/P/C 2.0/2.0/2.0) · SEA-E `5.0` Reject
- Telegram: [AGI_and_RL/988](https://t.me/AGI_and_RL/988)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The proposed method is not novel enough. The idea of learning a contrastive model to detect adversarial examples has been explored in previous works (1, 2, 3). The authors should compare their method with these works and discuss the differences and advantages of their method. - The evaluation is not comprehensive enough. The authors only evaluate their method on a limited number of d deepreviewer-7b: weaknesses, pushing for rigor and detail.     * **Reviewer 4 (St

<a id="arxiv-1801.01290"></a>
### Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor

`arxiv:1801.01290` · Reinforcement learning · 2018-01-04

- final **+0.52** (conf 0.71, pct 92) · impact +1.38 · KEEP
- mean rating (1–10): **6.4** · accept votes **6/7** · percentile rank_avg 68.2 (100=best) · rank in year 1.0 (1=best)
- NAIPv2 `-3.234` · NAIP-v1 `0.771` · SciJudge `1.989` · DGC-BERT `0.915`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.2` Accept · 7B Fast `7.5` Accept (S/P/C 3.25/3.25/3.25) · 14B Fast `5.7` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `8.0` Accept
- Telegram: [gonzo_ML/4277](https://t.me/gonzo_ML/4277)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The proposed algorithm is similar to the soft Q-learning algorithm proposed by Haarnoja et al. (2017). The main difference is that the proposed algorithm uses a separate critic network to estimate the state value function, while the soft Q-learning algorithm does not. The authors should compare the proposed algorithm with the soft Q-learning algorithm more clearly. - The proposed alg deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-1712.06567"></a>
### Deep Neuroevolution: Genetic Algorithms Are a Competitive Alternative for Training Deep Neural Networks for Reinforcement Learning

`arxiv:1712.06567` · Reinforcement learning · 2017-12-18

- final **+0.45** (conf 0.71, pct 87) · impact +0.40 · KEEP
- mean rating (1–10): **6.3** · accept votes **4/7** · percentile rank_avg 60.1 (100=best) · rank in year 1.0 (1=best)
- NAIPv2 `-0.830` · NAIP-v1 `0.779` · SciJudge `-2.734` · DGC-BERT `0.451`
- CycleReviewer 8B `6.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.8` Reject · 7B Fast `5.8` Accept (S/P/C 2.75/3.0/2.75) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper only compares the GA with other deep RL methods, but does not provide a comparison with other evolutionary algorithms. - The paper only considers a limited set of tasks, and it is unclear how the GA would perform on other tasks. - The paper does not provide a detailed analysis of the computational resources required to train the GA.  ### Questions  - How does the GA compare deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-1710.02298"></a>
### Rainbow: Combining Improvements in Deep Reinforcement Learning

`arxiv:1710.02298` · Reinforcement learning · 2017-10-06

- final **-0.14** (conf 0.71, pct 27) · impact +1.07 · WATCH
- mean rating (1–10): **5.7** · accept votes **3/7** · percentile rank_avg 51.0 (100=best) · rank in year 3.0 (1=best)
- NAIPv2 `-3.051` · NAIP-v1 `0.667` · SciJudge `2.473` · DGC-BERT `0.881`
- CycleReviewer 8B `5.8` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `5.5` Reject (S/P/C 2.75/3.0/2.25) · 14B Fast `5.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [knowledge_accumulator/194](https://t.me/knowledge_accumulator/194), [j_links/520](https://t.me/j_links/520)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper does not provide a clear motivation for combining all these extensions. It would be helpful to provide a more detailed explanation of why these extensions are complementary and how they work together to improve performance. - The paper does not provide a detailed analysis of the hyperparameters used in the experiments. It would be helpful to provide a more detailed discussi cyclereviewer-8b.seed1: Weaknesses  The paper is a combination of existing method

<a id="arxiv-1707.06887"></a>
### A Distributional Perspective on Reinforcement Learning

`arxiv:1707.06887` · Reinforcement learning · 2017-07-21

- final **+0.38** (conf 0.71, pct 81) · impact +0.88 · KEEP
- mean rating (1–10): **6.0** · accept votes **6/7** · percentile rank_avg 55.7 (100=best) · rank in year 2.0 (1=best)
- NAIPv2 `-2.482` · NAIP-v1 `0.682` · SciJudge `2.160` · DGC-BERT `0.891`
- CycleReviewer 8B `5.8` Reject · 70B `` 
- DeepReviewer 7B Std `4.5` Accept · 7B Fast `5.8` Accept (S/P/C 2.5/2.75/2.5) · 14B Fast `6.7` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [knowledge_accumulator/194](https://t.me/knowledge_accumulator/194), [j_links/332](https://t.me/j_links/332)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The theoretical results are not very surprising. The distributional Bellman operator is a contraction in Wasserstein distance, which has been shown in previous work. The authors only show that the distributional Bellman operator is a contraction in Wasserstein distance, but do not show that the proposed algorithm converges to the optimal solution.   2. The proposed algorithm is a si deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-1511.06581"></a>
### Dueling Network Architectures for Deep Reinforcement Learning

`arxiv:1511.06581` · Reinforcement learning · 2015-11-20

- final **+0.11** (conf 0.71, pct 53) · impact +0.29 · WATCH
- mean rating (1–10): **5.9** · accept votes **6/7** · percentile rank_avg 53.1 (100=best) · rank in year 1.0 (1=best)
- NAIPv2 `-4.504` · NAIP-v1 `0.628` · SciJudge `-0.007` · DGC-BERT `0.840`
- CycleReviewer 8B `4.8` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.7` Accept (S/P/C 3.0/3.0/2.33) · 14B Fast `5.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [knowledge_accumulator/194](https://t.me/knowledge_accumulator/194)
- Weaknesses: cyclereviewer-8b: Weaknesses  The main weakness of the paper is the lack of novelty. The proposed architecture is a simple modification of the standard Q-network architecture, and the idea of separating the value and advantage functions has been explored in previous work. The paper also lacks a thorough theoretical analysis of the proposed architecture. The empirical evaluation is limited to a single benchmark (Ata deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-1511.05952"></a>
### Prioritized Experience Replay

`arxiv:1511.05952` · Reinforcement learning · 2015-11-18

- final **-0.04** (conf 0.71, pct 35) · impact +1.06 · WATCH
- mean rating (1–10): **5.5** · accept votes **4/7** · percentile rank_avg 50.0 (100=best) · rank in year 2.0 (1=best)
- NAIPv2 `-1.875` · NAIP-v1 `0.706` · SciJudge `2.060` · DGC-BERT `0.910`
- CycleReviewer 8B `4.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.8` Reject · 7B Fast `4.8` Reject (S/P/C 2.5/3.0/2.25) · 14B Fast `5.0` Accept
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/4.0) · SEA-E `6.0` Accept
- Telegram: [knowledge_accumulator/194](https://t.me/knowledge_accumulator/194), [AGI_and_RL/189](https://t.me/AGI_and_RL/189)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The proposed algorithm is not novel.  - The experimental results are not convincing.  - The proposed algorithm is not well-motivated.   The proposed algorithm is not novel. The idea of prioritizing transitions based on TD error is not new. The authors should cite prior work (1) that also proposes prioritized experience replay for deep Q-learning.   The experimental results are not co deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-1509.06461"></a>
### Deep Reinforcement Learning with Double Q-learning

`arxiv:1509.06461` · Reinforcement learning · 2015-09-22

- final **+0.10** (conf 0.71, pct 51) · impact +0.42 · WATCH
- mean rating (1–10): **5.5** · accept votes **5/7** · percentile rank_avg 49.0 (100=best) · rank in year 3.0 (1=best)
- NAIPv2 `-2.979` · NAIP-v1 `0.721` · SciJudge `-0.671` · DGC-BERT `0.890`
- CycleReviewer 8B `5.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.0` Reject (S/P/C 2.75/3.0/2.75) · 14B Fast `4.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [knowledge_accumulator/194](https://t.me/knowledge_accumulator/194)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper lacks a comprehensive discussion of the limitations and potential drawbacks of the proposed approach. The authors should provide a more detailed analysis of the computational complexity and scalability of the proposed algorithm, as well as its potential limitations in terms of generalizability and applicability to different types of problems.  ### Questions  The paper present deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2608.13040"></a>
### Latent On-Policy Self-Distillation

`arxiv:2608.13040` · Post-training · 2026-08-13

- final **+0.19** (conf 0.71, pct 61) · impact -0.50 · WATCH
- mean rating (1–10): **6.1** · accept votes **6/7** · percentile rank_avg 56.4 (100=best) · rank in year 37.0 (1=best)
- NAIPv2 `-0.950` · NAIP-v1 `0.536` · SciJudge `-2.097` · DGC-BERT `0.842`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `7.0` Accept (S/P/C 3.0/3.0/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/4.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper is not well written and it is hard to follow. The notations are not well defined and the description of the method is not clear. The evaluation is not sufficient. The authors should provide more details about the baselines, the hyper-parameters, and the training and evaluation settings.  ### Questions  1. What is the difference between the proposed method and the existing OPS deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2608.09888"></a>
### BDH-CQ: In-Context Learning with Recurrent Latent Reasoning

`arxiv:2608.09888` · Post-training · 2026-08-10

- final **-0.43** (conf 0.71, pct 11) · impact -0.42 · DROP
- mean rating (1–10): **5.4** · accept votes **2/7** · percentile rank_avg 39.0 (100=best) · rank in year 65.0 (1=best)
- NAIPv2 `-0.529` · NAIP-v1 `0.629` · SciJudge `-3.334` · DGC-BERT `0.411`
- CycleReviewer 8B `5.2` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `4.2` Reject (S/P/C 2.5/2.75/2.5) · 14B Fast `5.7` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/8994](https://t.me/axisofordinary/8994)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper lacks a detailed description of the model architecture and its training procedure. The authors only provide a high-level overview of the model and its components, without providing specific details on how it is trained or how the recurrent memory is updated. This makes it difficult to understand the specific design choices and how they contribute to the model's performance deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2607.07847"></a>
### When Does Continual Learning Require Learning

`arxiv:2607.07847` · Post-training · 2026-07-08

- final **+0.00** (conf 0.71, pct 38) · impact +0.55 · WATCH
- mean rating (1–10): **5.9** · accept votes **4/7** · percentile rank_avg 50.4 (100=best) · rank in year 53.0 (1=best)
- NAIPv2 `-0.608` · NAIP-v1 `0.653` · SciJudge `1.443` · DGC-BERT `0.382`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.8` Reject · 7B Fast `6.0` Accept (S/P/C 3.0/3.25/3.0) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/5812](https://t.me/gonzo_ML/5812)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper only evaluates eight methods across four families, which may not be representative of all possible approaches to continual learning in LLMs. - The paper only uses a single model, Qwen3-8B, for all evaluations, which may not generalize to other models or model sizes. - The paper only considers a limited set of realistic environmental changes, such as domain shifts, agentic s deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2607.05609"></a>
### To Retain or to Adapt? Generalizing Continual Learning

`arxiv:2607.05609` · Post-training · 2026-07-06

- final **+0.09** (conf 0.71, pct 49) · impact -0.68 · WATCH
- mean rating (1–10): **6.1** · accept votes **5/7** · percentile rank_avg 59.8 (100=best) · rank in year 30.0 (1=best)
- NAIPv2 `0.292` · NAIP-v1 `0.529` · SciJudge `-2.818` · DGC-BERT `0.825`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `7.0` Accept · 7B Fast `6.0` Reject (S/P/C 2.75/3.0/2.5) · 14B Fast `6.5` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/5817](https://t.me/gonzo_ML/5817)
- Weaknesses: cyclereviewer-8b: Weaknesses  The authors do not provide an experimental evaluation of the proposed algorithm, Window. It would be interesting to see how the Window algorithm compares to other continual learning algorithms in terms of Transfer Efficiency.  ### Questions  How does the Window algorithm compare to other continual learning algorithms in terms of Transfer Efficiency?  ### Flag For Ethics Review  No ethi cyclereviewer-8b.seed1: Weaknesses  1. The authors claim that the paper challenge

<a id="arxiv-2606.23740"></a>
### Weight-Space Geometry of Offline Reasoning Training

`arxiv:2606.23740` · Post-training · 2026-06-21

- final **-0.32** (conf 0.71, pct 18) · impact -0.97 · DROP
- mean rating (1–10): **5.5** · accept votes **2/7** · percentile rank_avg 36.5 (100=best) · rank in year 67.0 (1=best)
- NAIPv2 `0.401` · NAIP-v1 `0.346` · SciJudge `0.405` · DGC-BERT `0.074`
- CycleReviewer 8B `4.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.2` Reject · 7B Fast `4.8` Reject (S/P/C 2.5/2.5/2.5) · 14B Fast `6.5` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [lovedeathtransformers/10841](https://t.me/lovedeathtransformers/10841), [lovedeathtransformers/10825](https://t.me/lovedeathtransformers/10825)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper only considers a single domain and checkpoint, which may limit the generalizability of the findings.  2. The analysis is limited to attention-only LoRA, which may not be representative of the full range of LoRA configurations.  3. The paper does not consider other contrastive methods such as IPO, KTO, SimPO, which may provide additional insights into the weight-space geome deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2606.18810"></a>
### Learning from Own Solutions: Self-Conditioned Credit Assignment for Reinforcement Learning with Verifiable Rewards

`arxiv:2606.18810` · Post-training · 2026-06-17

- final **+0.01** (conf 0.71, pct 39) · impact -0.97 · WATCH
- mean rating (1–10): **6.3** · accept votes **4/7** · percentile rank_avg 49.5 (100=best) · rank in year 55.0 (1=best)
- NAIPv2 `-1.278` · NAIP-v1 `0.505` · SciJudge `-3.719` · DGC-BERT `0.160`
- CycleReviewer 8B `5.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Reject · 7B Fast `6.5` Accept (S/P/C 3.0/3.25/2.5) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  - The novelty of the paper is limited. The idea of using KL divergence as a multiplicative weight on gradients is not new and has been explored in other contexts. The novelty of the paper lies in the application of this idea to RLVR and the observation that conditioning the model on its own verified trajectories induces a measurable per-token KL divergence between the original and cond deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2606.06021"></a>
### OPRD: On-Policy Representation Distillation

`arxiv:2606.06021` · Post-training · 2026-06-04

- final **+0.55** (conf 0.71, pct 95) · impact +0.72 · KEEP
- mean rating (1–10): **6.3** · accept votes **5/7** · percentile rank_avg 76.1 (100=best) · rank in year 2.0 (1=best)
- NAIPv2 `3.092` · NAIP-v1 `0.698` · SciJudge `0.898` · DGC-BERT `0.915`
- CycleReviewer 8B `5.8` Reject · 70B `` 
- DeepReviewer 7B Std `6.8` Accept · 7B Fast `6.0` Reject (S/P/C 3.0/3.0/3.0) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper proposes a new approach to on-policy distillation, which is to distill the model in the hidden-state space. However, the paper does not provide a thorough analysis of the proposed method. For example, it is not clear how the proposed method compares to other distillation methods, such as knowledge distillation and distillation with reinforcement learning. It would be helpful  deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2605.22074"></a>
### From Reasoning Chains to Verifiable Subproblems: Curriculum Reinforcement Learning Enables Credit Assignment for LLM Reasoning

`arxiv:2605.22074` · Post-training · 2026-05-21

- final **+0.23** (conf 0.71, pct 64) · impact +0.63 · KEEP
- mean rating (1–10): **6.3** · accept votes **6/7** · percentile rank_avg 69.8 (100=best) · rank in year 9.0 (1=best)
- NAIPv2 `-0.527` · NAIP-v1 `0.638` · SciJudge `1.754` · DGC-BERT `0.907`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.2` Accept · 7B Fast `7.0` Accept (S/P/C 3.0/3.25/3.25) · 14B Fast `5.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  I am not an expert in this area, but I am not sure if the method is novel enough. It seems that the method is a combination of existing ideas, such as curriculum learning and subproblem decomposition. The paper does not provide a clear comparison with other methods, and it is not clear how the proposed method compares to other methods in terms of novelty and effectiveness.  ### Questio deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2605.12969"></a>
### Revisiting Reinforcement Learning with Verifiable Rewards from a Contrastive Perspective

`arxiv:2605.12969` · Post-training · 2026-05-13

- final **+0.42** (conf 0.71, pct 85) · impact -0.86 · KEEP
- mean rating (1–10): **6.5** · accept votes **6/7** · percentile rank_avg 64.9 (100=best) · rank in year 21.0 (1=best)
- NAIPv2 `0.069` · NAIP-v1 `0.457` · SciJudge `-2.193` · DGC-BERT `0.943`
- CycleReviewer 8B `5.8` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `7.0` Accept (S/P/C 3.0/2.75/3.0) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The novelty of this paper is limited. The proposed method is based on a contrastive view of RLVR optimization, which is a common approach in the field of RL. The proposed method also uses a group-wise InfoNCE-style objective, which is a widely used contrastive loss function.   2. The proposed method is only evaluated on math reasoning tasks. It is unclear how the proposed method per deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2605.06241"></a>
### Rethinking RL for LLM Reasoning: It's Sparse Policy Selection, Not Capability Learning

`arxiv:2605.06241` · Post-training · 2026-05-07

- final **+0.56** (conf 0.71, pct 95) · impact +1.40 · KEEP
- mean rating (1–10): **7.2** · accept votes **5/7** · percentile rank_avg 80.6 (100=best) · rank in year 1.0 (1=best)
- NAIPv2 `0.688` · NAIP-v1 `0.633` · SciJudge `3.496` · DGC-BERT `0.163`
- CycleReviewer 8B `5.8` Reject · 70B `` 
- DeepReviewer 7B Std `7.0` Accept · 7B Fast `7.5` Accept (S/P/C 3.25/3.25/3.0) · 14B Fast `7.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/4.0/3.0) · SEA-E `7.0` Accept
- Telegram: [j_links/8484](https://t.me/j_links/8484)
- Weaknesses: cyclereviewer-8b: Weaknesses  The proposed method is a simple baseline and has been proposed before in (1). The authors should compare the proposed method with more advanced RL-free methods.   (1) Zelikman, Michael, et al. "Self-training large language models for reasoning." International Conference on Learning Representations. 2022.  ### Questions  See above  ### Flag For Ethics Review  No ethics review needed.  # deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2604.20659"></a>
### GRPO-VPS: Enhancing Group Relative Policy Optimization with Verifiable Process Supervision for Effective Reasoning

`arxiv:2604.20659` · Post-training · 2026-04-22

- final **-0.02** (conf 0.71, pct 36) · impact -0.77 · WATCH
- mean rating (1–10): **6.0** · accept votes **5/7** · percentile rank_avg 48.2 (100=best) · rank in year 56.0 (1=best)
- NAIPv2 `-1.234` · NAIP-v1 `0.453` · SciJudge `-1.101` · DGC-BERT `0.697`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.2` Accept · 7B Fast `5.8` Reject (S/P/C 2.75/2.75/2.5) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  - The proposed method is an extension of GRPO, and the novelty is limited. - The proposed method relies on the model's confidence in the correct answer, which may not be reliable in all cases. For example, if the model is uncertain about the correct answer, it may not provide a reliable confidence score. - The proposed method is only evaluated on math and general reasoning benchmarks,  deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2604.13016"></a>
### Rethinking On-Policy Distillation of Large Language Models: Phenomenology, Mechanism, and Recipe

`arxiv:2604.13016` · Post-training · 2026-04-14

- final **+0.42** (conf 0.71, pct 85) · impact -0.09 · KEEP
- mean rating (1–10): **6.3** · accept votes **6/7** · percentile rank_avg 66.0 (100=best) · rank in year 15.0 (1=best)
- NAIPv2 `0.490` · NAIP-v1 `0.563` · SciJudge `0.207` · DGC-BERT `0.852`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `7.0` Accept · 7B Fast `7.5` Accept (S/P/C 3.0/3.0/2.75) · 14B Fast `6.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper focuses on mathematical benchmarks, which may not be representative of other domains such as code and open-ended settings. It would be interesting to see if the same conditions and token-level mechanisms govern OPD in these other domains.  2. The paper does not isolate the impact of pre-training on OPD. It would be helpful to understand how differences in pre-training corp deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2604.08690"></a>
### Skip-Connected Policy Optimization for Implicit Advantage

`arxiv:2604.08690` · Post-training · 2026-04-09

- final **+0.36** (conf 0.71, pct 79) · impact -1.49 · KEEP
- mean rating (1–10): **6.5** · accept votes **6/7** · percentile rank_avg 61.7 (100=best) · rank in year 26.0 (1=best)
- NAIPv2 `-0.349` · NAIP-v1 `0.353` · SciJudge `-3.046` · DGC-BERT `0.886`
- CycleReviewer 8B `5.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `7.5` Accept (S/P/C 3.0/3.0/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  - The proposed method is very similar to the existing method, DAPO (Yu et al., 2025b). The main difference is that DAPO uses a self-critic, while the proposed method uses a separate upstream and downstream phase. I think the authors should discuss more about the difference between the proposed method and DAPO.  - The proposed method is not very efficient. It requires generating two sep deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2604.02288"></a>
### Unifying Group-Relative and Self-Distillation Policy Optimization via Sample Routing

`arxiv:2604.02288` · Post-training · 2026-04-02

- final **+0.01** (conf 0.71, pct 40) · impact +0.63 · WATCH
- mean rating (1–10): **5.9** · accept votes **5/7** · percentile rank_avg 59.7 (100=best) · rank in year 31.0 (1=best)
- NAIPv2 `0.539` · NAIP-v1 `0.620` · SciJudge `2.061` · DGC-BERT `0.848`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.8` Reject · 7B Fast `6.0` Accept (S/P/C 2.5/3.0/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper only compares SRPO with GRPO and SDPO. It would be interesting to see how SRPO compares to other methods for post-hoc training of LLMs, such as RLHF. - The paper only evaluates SRPO on five benchmarks and two model scales. It would be interesting to see how SRPO performs on a wider range of benchmarks and model scales. - The paper does not provide any analysis of the limita deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2604.01375"></a>
### RIFT: A RubrIc Failure Mode Taxonomy and Automated Diagnostics

`arxiv:2604.01375` · Post-training · 2026-04-01

- final **-0.16** (conf 0.71, pct 25) · impact -0.30 · WATCH
- mean rating (1–10): **5.8** · accept votes **3/7** · percentile rank_avg 46.2 (100=best) · rank in year 57.0 (1=best)
- NAIPv2 `-1.389` · NAIP-v1 `0.541` · SciJudge `-0.397` · DGC-BERT `0.309`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.2` Reject (S/P/C 2.75/3.0/3.0) · 14B Fast `5.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper focuses on the evaluation of rubrics, but does not discuss how to construct good rubrics. This is an important limitation, as the quality of the rubric is critical to the effectiveness of the evaluation. The paper should discuss how to construct good rubrics and how to evaluate their quality.  2. The paper does not provide a clear definition of the failure modes in the tax deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2603.25562"></a>
### Revisiting On-Policy Distillation: Empirical Failure Modes and Simple Fixes

`arxiv:2603.25562` · Post-training · 2026-03-26

- final **-0.09** (conf 0.71, pct 31) · impact +0.39 · WATCH
- mean rating (1–10): **5.8** · accept votes **5/7** · percentile rank_avg 53.9 (100=best) · rank in year 44.0 (1=best)
- NAIPv2 `-0.349` · NAIP-v1 `0.660` · SciJudge `0.503` · DGC-BERT `0.870`
- CycleReviewer 8B `4.2` Reject · 70B `` 
- DeepReviewer 7B Std `5.2` Reject · 7B Fast `5.8` Accept (S/P/C 2.5/3.0/2.5) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  - The proposed method is not novel. The idea of using top-K local support matching has been studied in the RL community for a long time. See, for example, (1,2). It is unclear why the authors did not cite these papers. - The empirical results are not convincing. The proposed method is only evaluated on two small datasets, which are not sufficient to demonstrate its effectiveness. The a deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2603.24472"></a>
### Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs?

`arxiv:2603.24472` · Post-training · 2026-03-25

- final **-0.24** (conf 0.71, pct 22) · impact +0.19 · DROP
- mean rating (1–10): **5.7** · accept votes **3/7** · percentile rank_avg 43.3 (100=best) · rank in year 61.0 (1=best)
- NAIPv2 `-0.968` · NAIP-v1 `0.561` · SciJudge `1.424` · DGC-BERT `0.251`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `5.8` Reject (S/P/C 2.75/2.75/2.75) · 14B Fast `5.8` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  - The authors only consider the math reasoning tasks, which is a very narrow scope. It is not clear whether the findings can be generalized to other reasoning tasks, such as commonsense reasoning, natural language inference, and so on. - The authors only consider the self-distillation methods, which is not a comprehensive study. It is not clear whether the findings can be generalized t deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2602.18037"></a>
### Gradient Regularization Mitigates Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards

`arxiv:2602.18037` · Post-training · 2026-02-20

- final **+0.16** (conf 0.71, pct 58) · impact -0.38 · WATCH
- mean rating (1–10): **6.0** · accept votes **4/7** · percentile rank_avg 56.4 (100=best) · rank in year 38.0 (1=best)
- NAIPv2 `-1.482` · NAIP-v1 `0.387` · SciJudge `1.787` · DGC-BERT `0.828`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `8.0` Accept · 7B Fast `6.5` Reject (S/P/C 2.75/2.75/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [j_links/8317](https://t.me/j_links/8317)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper lacks a comprehensive evaluation of the proposed method, with only a few experiments conducted on small-scale datasets. 2. The paper does not provide a detailed analysis of the computational cost of the proposed method. 3. The paper does not discuss the limitations of the proposed method and potential future research directions.  ## Questions  1. How does the proposed meth deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2602.09000"></a>
### iGRPO: Self-Feedback-Driven LLM Reasoning

`arxiv:2602.09000` · Post-training · 2026-02-09

- final **-0.08** (conf 0.71, pct 31) · impact +0.61 · WATCH
- mean rating (1–10): **5.6** · accept votes **4/7** · percentile rank_avg 52.6 (100=best) · rank in year 48.0 (1=best)
- NAIPv2 `-1.219` · NAIP-v1 `0.502` · SciJudge `3.180` · DGC-BERT `0.912`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `5.5` Reject (S/P/C 2.5/2.75/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/8164](https://t.me/axisofordinary/8164)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The proposed method is a simple extension of GRPO, and the authors do not provide a clear motivation for why the proposed method should work better than GRPO.  - The authors do not provide a clear analysis of why the proposed method outperforms other self-improvement baselines.  - The authors do not provide a clear analysis of the computational cost of the proposed method compared to deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2601.20861"></a>
### Evolutionary Strategies lead to Catastrophic Forgetting in LLMs

`arxiv:2601.20861` · Post-training · 2026-01-28

- final **-0.67** (conf 0.71, pct 4) · impact -1.29 · DROP
- mean rating (1–10): **5.1** · accept votes **3/7** · percentile rank_avg 24.1 (100=best) · rank in year 71.0 (1=best)
- NAIPv2 `-2.814` · NAIP-v1 `0.345` · SciJudge `-2.096` · DGC-BERT `0.038`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `5.7` Accept (S/P/C 2.67/2.67/2.67) · 14B Fast `4.0` Reject
- OpenReviewer `5.0` Reject (S/P/C 2.0/3.0/2.0) · SEA-E `5.0` Accept
- Telegram: [gonzo_ML/4709](https://t.me/gonzo_ML/4709)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper only evaluates ES on a limited set of tasks and models, which may not be representative of the broader LLM landscape. - The paper only considers a single type of ES implementation, which may not be representative of all ES variants. - The paper does not provide any insights into how to mitigate catastrophic forgetting in ES.  ### Questions  - How do the results generalize t deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2601.20802"></a>
### Reinforcement Learning via Self-Distillation

`arxiv:2601.20802` · Post-training · 2026-01-28

- final **+0.32** (conf 0.71, pct 76) · impact +1.08 · KEEP
- mean rating (1–10): **6.2** · accept votes **6/7** · percentile rank_avg 68.4 (100=best) · rank in year 10.0 (1=best)
- NAIPv2 `-0.924` · NAIP-v1 `0.584` · SciJudge `3.395` · DGC-BERT `0.912`
- CycleReviewer 8B `5.2` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.5` Accept (S/P/C 3.0/3.0/2.75) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/4681](https://t.me/gonzo_ML/4681)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper does not provide a clear motivation for the proposed method. The paper states that the key limitation is not RL per se, but the information bottleneck imposed by scalar outcome rewards. However, it is not clear why this is the case or how the proposed method addresses this limitation. 2. The paper does not provide a clear explanation of the proposed method. The paper state deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2601.19897"></a>
### Self-Distillation Enables Continual Learning

`arxiv:2601.19897` · Post-training · 2026-01-27

- final **-0.09** (conf 0.71, pct 30) · impact +0.62 · WATCH
- mean rating (1–10): **6.0** · accept votes **6/7** · percentile rank_avg 59.5 (100=best) · rank in year 32.0 (1=best)
- NAIPv2 `-1.568` · NAIP-v1 `0.601` · SciJudge `2.262` · DGC-BERT `0.924`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.8` Reject · 7B Fast `6.2` Accept (S/P/C 2.75/3.0/2.75) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/8164](https://t.me/axisofordinary/8164), [gonzo_ML/4687](https://t.me/gonzo_ML/4687)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper lacks a theoretical analysis of the proposed method. It would be helpful to have a theoretical analysis of the method's performance and its limitations. 2. The paper only evaluates the proposed method on a limited number of tasks. It would be helpful to evaluate the method on a larger number of tasks to demonstrate its generalizability. 3. The paper does not provide a deta deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2601.18734"></a>
### Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models

`arxiv:2601.18734` · Post-training · 2026-01-26

- final **+0.17** (conf 0.71, pct 58) · impact +0.51 · WATCH
- mean rating (1–10): **6.3** · accept votes **5/7** · percentile rank_avg 66.4 (100=best) · rank in year 13.0 (1=best)
- NAIPv2 `1.841` · NAIP-v1 `0.656` · SciJudge `0.972` · DGC-BERT `0.813`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.2` Reject · 7B Fast `6.7` Accept (S/P/C 3.0/3.0/2.67) · 14B Fast `6.0` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  The main weakness of the paper is that it lacks novelty. The idea of using a teacher-student framework for knowledge distillation is not new, and the use of ground-truth solutions as privileged information is also not novel. Additionally, the experimental results are not particularly surprising, and the authors do not provide any new insights into the problem of knowledge distillation. deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2601.16175"></a>
### Learning to Discover at Test Time

`arxiv:2601.16175` · Post-training · 2026-01-22

- final **+0.31** (conf 0.71, pct 75) · impact +1.25 · KEEP
- mean rating (1–10): **6.5** · accept votes **6/7** · percentile rank_avg 65.9 (100=best) · rank in year 16.0 (1=best)
- NAIPv2 `-0.401` · NAIP-v1 `0.564` · SciJudge `3.644` · DGC-BERT `0.030`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.2` Accept · 7B Fast `5.8` Accept (S/P/C 2.75/2.5/2.5) · 14B Fast `8.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [j_links/8337](https://t.me/j_links/8337), [gonzo_ML/4643](https://t.me/gonzo_ML/4643)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper only evaluates the method on a limited set of problems and does not provide a comprehensive evaluation of its performance. The paper also does not provide a detailed analysis of the method's performance on different types of problems.  ### Questions  The paper mentions that the method can only be applied to problems with continuous rewards. Can the method be extended to probl deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2601.14525"></a>
### Towards Execution-Grounded Automated AI Research

`arxiv:2601.14525` · Post-training · 2026-01-20

- final **+0.04** (conf 0.71, pct 43) · impact +0.16 · WATCH
- mean rating (1–10): **6.2** · accept votes **5/7** · percentile rank_avg 53.8 (100=best) · rank in year 45.0 (1=best)
- NAIPv2 `-0.429` · NAIP-v1 `0.485` · SciJudge `2.164` · DGC-BERT `0.572`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/3.0) · 14B Fast `6.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/4.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/4660](https://t.me/gonzo_ML/4660)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The novelty of this paper is limited. The proposed executor is a simple combination of existing ideas. The authors use the Tinker API to generate code from LLMs, and the scheduler and worker are also standard components. The authors also use evolutionary search and reinforcement learning to learn from execution feedback, which are both existing methods. 2. The idea of using LLMs to  deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2601.11061"></a>
### Spurious Rewards Paradox: Mechanistically Understanding How RLVR Activates Memorization Shortcuts in LLMs

`arxiv:2601.11061` · Post-training · 2026-01-16

- final **+0.47** (conf 0.71, pct 89) · impact +1.01 · KEEP
- mean rating (1–10): **6.3** · accept votes **6/7** · percentile rank_avg 73.1 (100=best) · rank in year 5.0 (1=best)
- NAIPv2 `2.123` · NAIP-v1 `0.655` · SciJudge `2.783` · DGC-BERT `0.666`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `7.0` Accept · 7B Fast `7.0` Accept (S/P/C 3.0/3.25/3.25) · 14B Fast `6.5` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [j_links/8281](https://t.me/j_links/8281), [buckwheat_thoughts/308](https://t.me/buckwheat_thoughts/308), [gonzo_ML/4704](https://t.me/gonzo_ML/4704)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper only studies the Qwen2.5 model, which is a specific model architecture. It is unclear whether the findings can be generalized to other model architectures. - The paper only studies the spurious rewards paradox in RLVR, which is a specific phenomenon. It is unclear whether the findings can be generalized to other phenomena in RLVR. - The paper does not provide a comprehensiv deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2512.02807"></a>
### SR-GRPO: Stable Rank as an Intrinsic Geometric Reward for Large Language Model Alignment

`arxiv:2512.02807` · Post-training · 2025-12-02

- final **+0.29** (conf 0.71, pct 73) · impact +0.19 · KEEP
- mean rating (1–10): **6.0** · accept votes **6/7** · percentile rank_avg 61.6 (100=best) · rank in year 28.0 (1=best)
- NAIPv2 `-0.412` · NAIP-v1 `0.616` · SciJudge `0.117` · DGC-BERT `0.904`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.5` Accept (S/P/C 2.75/2.75/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [tech_priestess/2494](https://t.me/tech_priestess/2494)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper does not provide any theoretical motivation for the proposed reward signal. It is not clear why stable rank is a good proxy for human preference. - The paper does not provide any analysis of the robustness of the proposed reward signal to different LLM architectures and training settings. - The paper does not provide any analysis of the computational cost of computing the p deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2512.00499"></a>
### ESPO: Entropy Importance Sampling Policy Optimization

`arxiv:2512.00499` · Post-training · 2025-11-29

- final **+0.25** (conf 0.71, pct 67) · impact -0.90 · KEEP
- mean rating (1–10): **6.2** · accept votes **6/7** · percentile rank_avg 53.7 (100=best) · rank in year 46.0 (1=best)
- NAIPv2 `-0.965` · NAIP-v1 `0.544` · SciJudge `-4.422` · DGC-BERT `0.884`
- CycleReviewer 8B `5.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `7.5` Accept (S/P/C 3.0/3.25/3.25) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  The novelty of the proposed method seems limited. The idea of using entropy to group tokens has been explored in prior works such as (1), and the proposed entropy adaptive clipping is similar to dynamic clipping in DCPO (2). The proposed method is also very similar to SPO (3), which also decomposes sequences into groups based on entropy. The main difference is that the proposed method  deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2511.20347"></a>
### Soft Adaptive Policy Optimization

`arxiv:2511.20347` · Post-training · 2025-11-25

- final **+0.14** (conf 0.71, pct 57) · impact -0.29 · WATCH
- mean rating (1–10): **6.3** · accept votes **5/7** · percentile rank_avg 60.7 (100=best) · rank in year 32.0 (1=best)
- NAIPv2 `-0.818` · NAIP-v1 `0.581` · SciJudge `-1.591` · DGC-BERT `0.819`
- CycleReviewer 8B `5.8` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.0` Reject (S/P/C 2.5/3.0/2.5) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  The main weakness of the paper is the lack of novelty. The proposed algorithm is based on existing techniques, such as group-based policy optimization and soft clipping, and does not introduce any new ideas or techniques. The experimental results are also not very convincing, as the proposed algorithm only shows a small improvement over the existing algorithms.  ### Questions  1. What  deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2511.07317"></a>
### RLVE: Scaling Up Reinforcement Learning for Language Models with Adaptive Verifiable Environments

`arxiv:2511.07317` · Post-training · 2025-11-10

- final **+0.41** (conf 0.71, pct 83) · impact -0.23 · KEEP
- mean rating (1–10): **6.5** · accept votes **5/7** · percentile rank_avg 61.2 (100=best) · rank in year 31.0 (1=best)
- NAIPv2 `-0.931` · NAIP-v1 `0.519` · SciJudge `-0.278` · DGC-BERT `0.547`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.2` Reject · 7B Fast `6.8` Accept (S/P/C 3.25/3.25/3.0) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper does not provide a clear comparison with other RL training frameworks. The authors should compare RLVE with other RL training frameworks, such as RLVR and ProRL, and show how RLVE improves upon them. - The paper does not provide a clear analysis of the performance of RLVE on different types of reasoning benchmarks. The authors should analyze the performance of RLVE on diffe deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2510.14901"></a>
### Reasoning with Sampling: Your Base Model is Smarter Than You Think

`arxiv:2510.14901` · Post-training · 2025-10-16

- final **+0.25** (conf 0.71, pct 67) · impact +0.05 · KEEP
- mean rating (1–10): **6.5** · accept votes **6/7** · percentile rank_avg 63.2 (100=best) · rank in year 20.0 (1=best)
- NAIPv2 `-1.463` · NAIP-v1 `0.513` · SciJudge `1.057` · DGC-BERT `0.885`
- CycleReviewer 8B `5.8` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `7.0` Accept (S/P/C 3.0/3.25/3.0) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper claims that the proposed method is training-free, but it requires additional inference-time computation. The paper should discuss the trade-off between training time and inference time. 2. The paper only compares the proposed method with GRPO, which is a specific RL-based method. It would be better to compare it with other RL-based methods as well. 3. The paper only evalua deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2510.13786"></a>
### The Art of Scaling Reinforcement Learning Compute for LLMs

`arxiv:2510.13786` · Post-training · 2025-10-15

- final **+0.48** (conf 0.71, pct 90) · impact +0.90 · KEEP
- mean rating (1–10): **6.3** · accept votes **6/7** · percentile rank_avg 74.3 (100=best) · rank in year 5.0 (1=best)
- NAIPv2 `0.044` · NAIP-v1 `0.693` · SciJudge `1.318` · DGC-BERT `0.852`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `8.0` Accept · 7B Fast `6.8` Accept (S/P/C 3.25/3.25/3.25) · 14B Fast `6.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [lovedeathtransformers/9883](https://t.me/lovedeathtransformers/9883), [axisofordinary/7787](https://t.me/axisofordinary/7787)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The authors only study the scaling law of RL for LLMs, but do not discuss the scaling law of RL for other tasks, such as robotics and game playing. 2. The authors do not provide a theoretical analysis of the scaling law of RL for LLMs. 3. The authors do not discuss the limitations of the proposed method.  ### Questions  1. Can you provide a theoretical analysis of the scaling law of deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2510.00977"></a>
### It Takes Two: Your GRPO Is Secretly DPO

`arxiv:2510.00977` · Post-training · 2025-10-01

- final **-0.10** (conf 0.71, pct 30) · impact -1.18 · WATCH
- mean rating (1–10): **5.7** · accept votes **5/7** · percentile rank_avg 44.3 (100=best) · rank in year 65.0 (1=best)
- NAIPv2 `-0.455` · NAIP-v1 `0.411` · SciJudge `-2.651` · DGC-BERT `0.614`
- CycleReviewer 8B `5.2` Reject · 70B `` 
- DeepReviewer 7B Std `6.2` Accept · 7B Fast `4.8` Reject (S/P/C 2.5/2.75/2.25) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [dealerAI/1498](https://t.me/dealerAI/1498)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The authors only provide a theoretical analysis of 2-GRPO and empirical results on a single dataset. The authors should provide more empirical results on other datasets to validate the effectiveness of 2-GRPO. 2. The authors should provide more details about the implementation of 2-GRPO and the hyperparameters used in the experiments. 3. The authors should provide more discussion on deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2509.25123"></a>
### From $f(x)$ and $g(x)$ to $f(g(x))$: LLMs Learn New Skills in RL by Composing Old Ones

`arxiv:2509.25123` · Post-training · 2025-09-29

- final **-0.07** (conf 0.71, pct 33) · impact -0.13 · WATCH
- mean rating (1–10): **5.8** · accept votes **5/7** · percentile rank_avg 50.7 (100=best) · rank in year 53.0 (1=best)
- NAIPv2 `-0.188` · NAIP-v1 `0.603` · SciJudge `-0.882` · DGC-BERT `0.417`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `4.2` Reject (S/P/C 2.25/2.25/2.25) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/7729](https://t.me/axisofordinary/7729)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper's focus on synthetic tasks may limit its generalizability to real-world applications. - The paper does not provide a clear answer to the question of how to incentivize skill acquisition in RL. - The paper does not provide a clear answer to the question of whether the skills learned by LLMs during RL are transferable to other tasks.  ### Questions  - How do the authors think deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2509.13232"></a>
### Single-stream Policy Optimization

`arxiv:2509.13232` · Post-training · 2025-09-16

- final **-0.07** (conf 0.71, pct 33) · impact +0.37 · WATCH
- mean rating (1–10): **6.0** · accept votes **5/7** · percentile rank_avg 54.2 (100=best) · rank in year 44.0 (1=best)
- NAIPv2 `-0.961` · NAIP-v1 `0.567` · SciJudge `1.330` · DGC-BERT `0.947`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.0` Reject · 7B Fast `7.0` Accept (S/P/C 3.0/3.25/2.75) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper lacks a theoretical analysis of the proposed method. 2. The experiments are not comprehensive. The authors only compare with GRPO, but there are other baselines such as A*-PO (1), RLOO (2), and Lite PPO (3). 3. The paper does not discuss the limitations of the proposed method. 4. The paper does not provide any insights into why SPO outperforms GRPO.  (1) Brantley, J., Chen deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2509.03646"></a>
### Emergent Hierarchical Reasoning in LLMs through Reinforcement Learning

`arxiv:2509.03646` · Post-training · 2025-09-03

- final **-0.09** (conf 0.71, pct 31) · impact +0.33 · WATCH
- mean rating (1–10): **5.9** · accept votes **3/7** · percentile rank_avg 57.6 (100=best) · rank in year 41.0 (1=best)
- NAIPv2 `-0.492` · NAIP-v1 `0.669` · SciJudge `-0.405` · DGC-BERT `0.871`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.2` Reject · 7B Fast `5.5` Reject (S/P/C 2.75/2.75/2.5) · 14B Fast `6.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [axisofordinary/7653](https://t.me/axisofordinary/7653), [tech_priestess/2386](https://t.me/tech_priestess/2386)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper assumes that the reasoning process can be decomposed into high-level planning and low-level execution. This assumption is not always valid. For example, in the case of mathematical problem-solving, the high-level plan and low-level execution are often intertwined. The authors should provide more evidence to support their assumption.  2. The authors use a heuristic to ident deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2508.07629"></a>
### Klear-Reasoner: Advancing Reasoning Capability via Gradient-Preserving Clipping Policy Optimization

`arxiv:2508.07629` · Post-training · 2025-08-11

- final **-0.28** (conf 0.68, pct 20) · impact -0.90 · DROP
- mean rating (1–10): **5.8** · accept votes **3/6** · percentile rank_avg 37.6 (100=best) · rank in year 69.0 (1=best)
- NAIPv2 `-1.587` · NAIP-v1 `0.330` · SciJudge `0.493` · DGC-BERT `0.049`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std ``  · 7B Fast `5.2` Reject (S/P/C 2.75/3.0/2.5) · 14B Fast `6.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper focuses on a specific problem of clipping in RL, which may limit its generalizability to other areas of research. - The paper does not provide a detailed comparison with other state-of-the-art models, making it difficult to evaluate the effectiveness of the proposed method. - The paper does not discuss potential limitations or drawbacks of the proposed method.  ### Question deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2508.05629"></a>
### On the Generalization of SFT: A Reinforcement Learning Perspective with Reward Rectification

`arxiv:2508.05629` · Post-training · 2025-08-07

- final **+0.53** (conf 0.71, pct 93) · impact -0.50 · KEEP
- mean rating (1–10): **6.4** · accept votes **6/7** · percentile rank_avg 67.8 (100=best) · rank in year 12.0 (1=best)
- NAIPv2 `1.032` · NAIP-v1 `0.536` · SciJudge `-2.207` · DGC-BERT `0.950`
- CycleReviewer 8B `5.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.4` Accept · 7B Fast `7.0` Accept (S/P/C 3.25/3.25/3.25) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [buckwheat_thoughts/297](https://t.me/buckwheat_thoughts/297), [abstractDL/345](https://t.me/abstractDL/345)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The theoretical analysis in Section 3.2 is not very convincing. The authors claim that SFT can be viewed as a form of policy gradient with a sparse reward function, which is inversely proportional to the model's probability of expert actions. However, this is not a new observation. The authors should provide a more rigorous proof of this claim. - The proposed method is only evaluated deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2507.19457"></a>
### GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning

`arxiv:2507.19457` · Post-training · 2025-07-25

- final **+0.54** (conf 0.71, pct 94) · impact -0.09 · KEEP
- mean rating (1–10): **6.3** · accept votes **6/7** · percentile rank_avg 66.8 (100=best) · rank in year 14.0 (1=best)
- NAIPv2 `2.922` · NAIP-v1 `0.504` · SciJudge `0.575` · DGC-BERT `0.518`
- CycleReviewer 8B `5.2` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.5` Accept (S/P/C 2.75/3.0/2.5) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [axisofordinary/7502](https://t.me/axisofordinary/7502), [gonzo_ML/3879](https://t.me/gonzo_ML/3879)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The proposed method is not novel. The idea of using a genetic algorithm to search for better prompts has been explored in previous work, such as EvoPrompt (1). The authors should provide a more detailed comparison with existing methods. - The evaluation of the proposed method is not comprehensive. The authors only evaluate the method on a few benchmarks and do not compare it with a w deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2507.18071"></a>
### Group Sequence Policy Optimization

`arxiv:2507.18071` · Post-training · 2025-07-24

- final **+0.05** (conf 0.71, pct 44) · impact -0.33 · WATCH
- mean rating (1–10): **5.5** · accept votes **5/7** · percentile rank_avg 47.9 (100=best) · rank in year 59.0 (1=best)
- NAIPv2 `-1.184` · NAIP-v1 `0.424` · SciJudge `1.292` · DGC-BERT `0.875`
- CycleReviewer 8B `4.2` Reject · 70B `` 
- DeepReviewer 7B Std `7.0` Accept · 7B Fast `4.8` Reject (S/P/C 2.5/2.75/2.25) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [dealerAI/1474](https://t.me/dealerAI/1474), [data_secrets/7470](https://t.me/data_secrets/7470)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper lacks a detailed theoretical analysis of the proposed algorithm, GSPO. While the authors provide some intuition behind the algorithm, a more rigorous theoretical analysis would strengthen the paper. 2. The paper only compares GSPO with GRPO, and it would be beneficial to include comparisons with other state-of-the-art methods for training large language models using RL. 3. deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2506.13585"></a>
### MiniMax-M1: Scaling Test-Time Compute Efficiently with Lightning Attention

`arxiv:2506.13585` · Post-training · 2025-06-16

- final **+0.40** (conf 0.71, pct 83) · impact -0.28 · KEEP
- mean rating (1–10): **6.0** · accept votes **4/7** · percentile rank_avg 52.3 (100=best) · rank in year 49.0 (1=best)
- NAIPv2 `1.191` · NAIP-v1 `0.258` · SciJudge `3.205` · DGC-BERT `0.306`
- CycleReviewer 8B `4.8` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `5.5` Reject (S/P/C 3.25/3.25/3.0) · 14B Fast `8.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  - The authors claim that MiniMax-M1 is the world's first open-weight, large-scale hybrid-attention reasoning model, but there are many other open-source LLMs that use hybrid attention, such as Hunyuan-T1 (https://arxiv.org/abs/2305.14360). The authors should compare MiniMax-M1 with these models and discuss the differences. - The authors claim that MiniMax-M1 is the world's first open-w deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2506.06632"></a>
### Curriculum Reinforcement Learning from Easy to Hard Tasks Improves LLM Reasoning

`arxiv:2506.06632` · Post-training · 2025-06-07

- final **+0.08** (conf 0.71, pct 49) · impact -0.69 · WATCH
- mean rating (1–10): **5.9** · accept votes **5/7** · percentile rank_avg 50.2 (100=best) · rank in year 54.0 (1=best)
- NAIPv2 `1.160` · NAIP-v1 `0.422` · SciJudge `0.002` · DGC-BERT `0.832`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `5.2` Reject · 7B Fast `6.5` Accept (S/P/C 3.0/3.0/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The proposed method is not novel. There are many previous works on curriculum learning for LLMs, such as (1,2,3). The authors should compare the proposed method with these works. 2. The theoretical analysis is not rigorous. The authors assume that the curriculum is well-designed, but it is not clear how to design a good curriculum. The authors should provide more details on how to d deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2506.03106"></a>
### Critique-GRPO: Advancing LLM Reasoning with Natural Language and Numerical Feedback

`arxiv:2506.03106` · Post-training · 2025-06-03

- final **+0.52** (conf 0.71, pct 92) · impact +0.84 · KEEP
- mean rating (1–10): **6.5** · accept votes **7/7** · percentile rank_avg 77.7 (100=best) · rank in year 2.0 (1=best)
- NAIPv2 `1.530` · NAIP-v1 `0.635` · SciJudge `1.974` · DGC-BERT `0.909`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/2.75) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  The main weakness of the paper is the limited novelty. The paper builds on existing work on RL methods for improving the reasoning capabilities of LLMs and combines numerical and natural language feedback. The method is not significantly different from existing methods, and the results are not surprising. The paper also lacks a thorough comparison with existing methods. The authors com deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2506.01939"></a>
### Beyond the 80/20 Rule: High-Entropy Minority Tokens Drive Effective Reinforcement Learning for LLM Reasoning

`arxiv:2506.01939` · Post-training · 2025-06-02

- final **+0.26** (conf 0.71, pct 69) · impact +0.63 · KEEP
- mean rating (1–10): **6.2** · accept votes **4/7** · percentile rank_avg 60.0 (100=best) · rank in year 35.0 (1=best)
- NAIPv2 `-1.289` · NAIP-v1 `0.601` · SciJudge `1.841` · DGC-BERT `0.275`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `5.8` Reject (S/P/C 2.75/2.75/2.75) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [axisofordinary/7296](https://t.me/axisofordinary/7296), [tech_priestess/2386](https://t.me/tech_priestess/2386)
- Weaknesses: cyclereviewer-8b: Weaknesses  The main weakness of the paper is that the results are not very surprising and do not seem to have a significant impact on the field. The paper is essentially showing that high-entropy tokens are important for reasoning, which is already known. The paper also shows that training on high-entropy tokens can achieve comparable performance to training on all tokens, but this is not surpris cyclereviewer-8b.seed1: Weaknesses  I have several concerns about the paper: 1. T

<a id="arxiv-2505.19590"></a>
### Learning to Reason without External Rewards

`arxiv:2505.19590` · Post-training · 2025-05-26

- final **-0.00** (conf 0.71, pct 38) · impact +0.36 · WATCH
- mean rating (1–10): **5.3** · accept votes **3/7** · percentile rank_avg 51.7 (100=best) · rank in year 50.0 (1=best)
- NAIPv2 `1.556` · NAIP-v1 `0.594` · SciJudge `1.122` · DGC-BERT `0.822`
- CycleReviewer 8B `4.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.2` Reject · 7B Fast `4.8` Reject (S/P/C 2.5/2.75/2.25) · 14B Fast `6.0` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `7.0` Accept
- Telegram: [axisofordinary/8273](https://t.me/axisofordinary/8273), [gonzo_ML/3767](https://t.me/gonzo_ML/3767), [axisofordinary/7262](https://t.me/axisofordinary/7262)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper lacks novelty. The proposed method is simple and straightforward. The method is similar to the previous work (1) which uses the self-certainty as the reward signal for RLHF.  2. The paper lacks theoretical analysis. The paper does not provide any theoretical analysis of the proposed method. 3. The paper lacks ablation study. The paper does not provide any ablation study to deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2505.10978"></a>
### Group-in-Group Policy Optimization for LLM Agent Training

`arxiv:2505.10978` · Post-training · 2025-05-16

- final **+0.39** (conf 0.71, pct 81) · impact +0.84 · KEEP
- mean rating (1–10): **6.3** · accept votes **7/7** · percentile rank_avg 75.1 (100=best) · rank in year 4.0 (1=best)
- NAIPv2 `0.338` · NAIP-v1 `0.675` · SciJudge `1.363` · DGC-BERT `0.888`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `7.0` Accept · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/2.67) · 14B Fast `6.7` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper does not provide a theoretical analysis of the proposed method, which could help understand its properties and limitations. - The paper does not discuss the limitations of the proposed method, such as potential issues with scalability or generalizability to other tasks. - The paper does not provide a detailed comparison with prior methods, such as a discussion of the trade- deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2504.16084"></a>
### TTRL: Test-Time Reinforcement Learning

`arxiv:2504.16084` · Post-training · 2025-04-22

- final **+0.40** (conf 0.71, pct 82) · impact -0.11 · KEEP
- mean rating (1–10): **6.1** · accept votes **5/7** · percentile rank_avg 62.0 (100=best) · rank in year 25.0 (1=best)
- NAIPv2 `1.952` · NAIP-v1 `0.403` · SciJudge `2.112` · DGC-BERT `0.948`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/3.0) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [gonzo_ML/4151](https://t.me/gonzo_ML/4151)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The novelty of this paper is limited. The proposed method is similar to self-play training, which has been widely used in the field of reinforcement learning. The main difference is that the proposed method uses a single model instead of multiple models in self-play training.   2. The paper lacks a theoretical analysis of the proposed method. It is unclear how the method works and w deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2504.13837"></a>
### Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?

`arxiv:2504.13837` · Post-training · 2025-04-18

- final **-0.02** (conf 0.71, pct 36) · impact +0.41 · WATCH
- mean rating (1–10): **5.8** · accept votes **4/7** · percentile rank_avg 50.0 (100=best) · rank in year 56.0 (1=best)
- NAIPv2 `-1.139` · NAIP-v1 `0.544` · SciJudge `1.785` · DGC-BERT `0.742`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `6.5` Accept (S/P/C 3.0/3.0/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `5.0` Reject (S/P/C 2.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/4286](https://t.me/gonzo_ML/4286), [data_secrets/8212](https://t.me/data_secrets/8212), [abstractDL/332](https://t.me/abstractDL/332), [AGI_and_RL/1058](https://t.me/AGI_and_RL/1058), [boris_again/3157](https://t.me/boris_again/3157), [lovedeathtransformers/9272](https://t.me/lovedeathtransformers/9272)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper does not provide a clear explanation for the observed phenomenon. 2. The paper does not provide a clear recommendation for future research directions.  ### Questions  1. What are the possible reasons for the observed phenomenon? 2. What are the potential implications of the findings for future research?  ### Flag For Ethics Review  No ethics review needed.  ### Rating  5:  deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2503.20783"></a>
### Understanding R1-Zero-Like Training: A Critical Perspective

`arxiv:2503.20783` · Post-training · 2025-03-26

- final **+0.42** (conf 0.71, pct 84) · impact +0.16 · KEEP
- mean rating (1–10): **6.2** · accept votes **5/7** · percentile rank_avg 61.6 (100=best) · rank in year 26.0 (1=best)
- NAIPv2 `1.818` · NAIP-v1 `0.442` · SciJudge `2.446` · DGC-BERT `0.447`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.5` Accept (S/P/C 3.0/3.0/2.75) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper lacks novelty. The authors have identified two issues in the R1-zero-like training, but the proposed solution is simply removing the normalization terms in the GRPO algorithm, which is a straightforward fix.  2. The paper lacks experiments. The authors have only conducted experiments on a small number of models and datasets, and the results are not convincing.  ### Questio deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2503.14476"></a>
### DAPO: An Open-Source LLM Reinforcement Learning System at Scale

`arxiv:2503.14476` · Post-training · 2025-03-18

- final **-0.40** (conf 0.71, pct 13) · impact +0.37 · DROP
- mean rating (1–10): **6.0** · accept votes **3/7** · percentile rank_avg 46.5 (100=best) · rank in year 63.0 (1=best)
- NAIPv2 `-1.369` · NAIP-v1 `0.501` · SciJudge `2.191` · DGC-BERT `0.160`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `4.0` Reject · 7B Fast `5.0` Reject (S/P/C 2.5/2.5/2.5) · 14B Fast `6.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [axisofordinary/7039](https://t.me/axisofordinary/7039), [AGI_and_RL/1061](https://t.me/AGI_and_RL/1061)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper does not include any ablation studies to show the impact of each modification to the GRPO algorithm. This makes it difficult to determine which modifications are most important for the improved performance.  ### Questions  The paper does not include any comparison to other RLHF algorithms, such as PPO or PPO-Clip. It would be helpful to see how the proposed algorithm compares deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2503.02875"></a>
### The First Few Tokens Are All You Need: An Efficient and Effective Unsupervised Prefix Fine-Tuning Method for Reasoning Models

`arxiv:2503.02875` · Post-training · 2025-03-04

- final **-0.16** (conf 0.71, pct 26) · impact +0.94 · WATCH
- mean rating (1–10): **6.2** · accept votes **3/7** · percentile rank_avg 59.0 (100=best) · rank in year 39.0 (1=best)
- NAIPv2 `-1.960` · NAIP-v1 `0.596` · SciJudge `3.143` · DGC-BERT `0.817`
- CycleReviewer 8B `5.5` Reject · 70B `` 
- DeepReviewer 7B Std `5.8` Reject · 7B Fast `5.8` Reject (S/P/C 2.75/2.75/2.75) · 14B Fast `6.5` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [data_secrets/6419](https://t.me/data_secrets/6419), [axisofordinary/7009](https://t.me/axisofordinary/7009)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The authors claim that the proposed method is "unsupervised" in the sense that it does not require labeled data or rejection sampling. However, the method still requires a dataset of questions and answers, which is not entirely unsupervised. In addition, the authors use a subset of the dataset for full reasoning trace generation, which is still supervised. I would suggest the authors cyclereviewer-8b.seed1: Weaknesses  - The paper does not provide a theoretical an

<a id="arxiv-2503.00735"></a>
### LADDER: Self-Improving LLMs Through Recursive Problem Decomposition

`arxiv:2503.00735` · Post-training · 2025-03-02

- final **-0.04** (conf 0.71, pct 34) · impact +1.35 · WATCH
- mean rating (1–10): **6.0** · accept votes **4/7** · percentile rank_avg 59.8 (100=best) · rank in year 36.0 (1=best)
- NAIPv2 `-0.900` · NAIP-v1 `0.600` · SciJudge `3.585` · DGC-BERT `0.731`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.0` Reject · 7B Fast `6.0` Reject (S/P/C 3.0/3.0/3.0) · 14B Fast `6.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/7020](https://t.me/axisofordinary/7020), [AGI_and_RL/986](https://t.me/AGI_and_RL/986)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper focuses on mathematical integration tasks, which may not be representative of all types of complex tasks that LLMs need to solve. It would be helpful to see if the approach works on other types of tasks as well. - The paper does not provide a detailed analysis of the computational cost of the approach. It would be helpful to understand the trade-off between the potential im deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2402.13669"></a>
### Self-Distillation Bridges Distribution Gap in Language Model Fine-Tuning

`arxiv:2402.13669` · Post-training · 2024-02-21

- final **+0.28** (conf 0.71, pct 71) · impact +0.36 · KEEP
- mean rating (1–10): **6.4** · accept votes **5/7** · percentile rank_avg 62.3 (100=best) · rank in year 4.0 (1=best)
- NAIPv2 `0.723` · NAIP-v1 `0.570` · SciJudge `1.364` · DGC-BERT `0.909`
- CycleReviewer 8B `5.5` Reject · 70B `` 
- DeepReviewer 7B Std `4.2` Reject · 7B Fast `6.0` Accept (S/P/C 2.67/3.0/2.67) · 14B Fast `6.7` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper does not provide a thorough analysis of the limitations of the proposed method. For example, the paper does not discuss the computational cost of generating the distilled dataset, or the potential trade-off between performance and computational cost. 2. The paper does not provide a comparison with other methods for mitigating catastrophic forgetting in LLM fine-tuning. For deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2402.03300"></a>
### DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models

`arxiv:2402.03300` · Post-training · 2024-02-05

- final **+0.33** (conf 0.71, pct 76) · impact +0.57 · KEEP
- mean rating (1–10): **6.2** · accept votes **5/7** · percentile rank_avg 57.1 (100=best) · rank in year 13.0 (1=best)
- NAIPv2 `-1.261` · NAIP-v1 `0.440` · SciJudge `3.477` · DGC-BERT `0.859`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `5.5` Reject (S/P/C 3.0/3.0/3.0) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/4555](https://t.me/gonzo_ML/4555), [gonzo_ML/4303](https://t.me/gonzo_ML/4303), [gonzo_ML/3319](https://t.me/gonzo_ML/3319), [gonzo_ML/3313](https://t.me/gonzo_ML/3313), [buckwheat_thoughts/104](https://t.me/buckwheat_thoughts/104), [buckwheat_thoughts/105](https://t.me/buckwheat_thoughts/105), [AGI_and_RL/948](https://t.me/AGI_and_RL/948), [gonzo_ML/3239](https://t.me/gonzo_ML/3239)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper does not provide a detailed analysis of the data selection pipeline used to construct the DeepSeekMath Corpus. It would be helpful to have a more detailed description of the data selection process, including how the data was filtered and how the quality of the data was assessed.  2. The paper does not provide a detailed analysis of the performance of the model on different cyclereviewer-8b.seed1: Weaknesses  1. The paper is not well-organized, some part

<a id="arxiv-2303.17651"></a>
### Self-Refine: Iterative Refinement with Self-Feedback

`arxiv:2303.17651` · Post-training · 2023-03-30

- final **+0.11** (conf 0.71, pct 53) · impact +1.88 · WATCH
- mean rating (1–10): **6.2** · accept votes **6/7** · percentile rank_avg 60.7 (100=best) · rank in year 8.0 (1=best)
- NAIPv2 `-2.209` · NAIP-v1 `0.704` · SciJudge `4.059` · DGC-BERT `0.851`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `5.8` Accept (S/P/C 3.0/3.0/2.5) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [gonzo_ML/1467](https://t.me/gonzo_ML/1467)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper evaluates Self-Refine on a limited number of tasks, and it is not clear how well the approach would perform on other tasks or domains. The paper also does not provide a detailed comparison with other approaches that use feedback and refinement to improve LLM outputs.  The paper does not provide a detailed analysis of the computational cost of Self-Refine, including the time a deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2608.11676"></a>
### XBridge: Entity-Grounded Latent Bridge for Heterogeneous LLM Communication

`arxiv:2608.11676` · LLMs: architectures, context, training · 2026-08-12

- final **+0.27** (conf 0.71, pct 69) · impact -0.49 · KEEP
- mean rating (1–10): **6.2** · accept votes **5/7** · percentile rank_avg 56.6 (100=best) · rank in year 35.0 (1=best)
- NAIPv2 `-0.440` · NAIP-v1 `0.609` · SciJudge `-3.182` · DGC-BERT `0.209`
- CycleReviewer 8B `6.0` Reject · 70B `` 
- DeepReviewer 7B Std `7.0` Accept · 7B Fast `5.7` Accept (S/P/C 3.0/3.0/2.33) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The proposed method is only evaluated on a limited set of benchmarks, and it is unclear how the method will perform on other tasks. 2. The method requires training a separate bridge for each sender-receiver pair, which may be computationally expensive. 3. The method assumes that the sender and receiver have the same vocabulary, which may not always be the case in real-world applicat deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2608.03893"></a>
### Cross-Model KV Cache Transfer in LLM Families: A Closed-Form Linear Mapping for Prefill Reuse

`arxiv:2608.03893` · LLMs: architectures, context, training · 2026-08-04

- final **+0.19** (conf 0.71, pct 61) · impact -0.77 · WATCH
- mean rating (1–10): **5.8** · accept votes **5/7** · percentile rank_avg 50.6 (100=best) · rank in year 52.0 (1=best)
- NAIPv2 `-0.026` · NAIP-v1 `0.437` · SciJudge `-0.487` · DGC-BERT `0.067`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.5` Accept (S/P/C 3.0/3.0/2.5) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [lovedeathtransformers/10993](https://t.me/lovedeathtransformers/10993)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The proposed method is evaluated on 6 matched-KV pairs across 3 model families. The authors claim that the linear structure in cross-model KV cache transfer is a general phenomenon, but the evaluation is not sufficient to support this claim.  - The proposed method is evaluated on 5 accuracy benchmarks. However, the authors did not evaluate the proposed method on more challenging benc deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2608.00146"></a>
### DiffusionGemma Technical Report

`arxiv:2608.00146` · LLMs: architectures, context, training · 2026-07-31

- final **+0.27** (conf 0.71, pct 70) · impact +1.43 · KEEP
- mean rating (1–10): **6.7** · accept votes **3/7** · percentile rank_avg 66.3 (100=best) · rank in year 14.0 (1=best)
- NAIPv2 `-0.480` · NAIP-v1 `0.688` · SciJudge `3.269` · DGC-BERT `0.309`
- CycleReviewer 8B `6.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `5.6` Reject (S/P/C 3.0/3.0/3.0) · 14B Fast `8.0` Accept
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/4.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/5942](https://t.me/gonzo_ML/5942)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper does not provide a detailed comparison with existing methods, making it difficult to assess the novelty and effectiveness of the proposed method. 2. The paper does not provide a detailed analysis of the computational cost of the proposed method, making it difficult to assess its efficiency. 3. The paper does not provide a detailed discussion of the limitations of the propo deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2607.02303"></a>
### A Hippocampus for Linear Attention: An Exact Memory for What the Recurrent State Forgets

`arxiv:2607.02303` · LLMs: architectures, context, training · 2026-07-02

- final **+0.27** (conf 0.71, pct 70) · impact +0.30 · KEEP
- mean rating (1–10): **6.2** · accept votes **6/7** · percentile rank_avg 61.6 (100=best) · rank in year 27.0 (1=best)
- NAIPv2 `0.288` · NAIP-v1 `0.584` · SciJudge `1.483` · DGC-BERT `0.693`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.8` Accept · 7B Fast `5.8` Accept (S/P/C 2.75/2.75/2.75) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [gonzo_ML/5675](https://t.me/gonzo_ML/5675)
- Weaknesses: cyclereviewer-8b: Weaknesses  The main weakness of the paper is that the proposed method is not novel. The idea of using a cache to improve the performance of linear attention models has been proposed in previous works such as LTE and NHA. The novelty of this paper is mainly in the way the cache is filled with the most important key-value pairs.  ### Questions  1. How does the proposed method compare to LTE and NHA cyclereviewer-8b.seed1: Weaknesses  - The paper does not provide a detailed compa

<a id="arxiv-2606.06574"></a>
### Skip a Layer or Loop It? Learning Program-of-Layers in LLMs

`arxiv:2606.06574` · LLMs: architectures, context, training · 2026-06-04

- final **+0.26** (conf 0.71, pct 68) · impact +0.33 · KEEP
- mean rating (1–10): **6.0** · accept votes **6/7** · percentile rank_avg 64.4 (100=best) · rank in year 23.0 (1=best)
- NAIPv2 `-0.587` · NAIP-v1 `0.680` · SciJudge `-0.313` · DGC-BERT `0.957`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.0` Accept (S/P/C 3.25/3.25/3.0) · 14B Fast `6.2` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [gonzo_ML/5950](https://t.me/gonzo_ML/5950)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The authors claim that their method can reduce the inference latency. However, the authors only report the number of layers executed, but not the actual inference latency. I think it is more important to report the actual inference latency, as the number of layers executed may not be a good indicator of the actual inference latency.  2. The authors only evaluate the proposed method  cyclereviewer-8b.seed1: Weaknesses  1. The motivation is not clear. The authors c

<a id="arxiv-2605.22863"></a>
### Latent Cache Flow: Model-to-Model Communication Without Text

`arxiv:2605.22863` · LLMs: architectures, context, training · 2026-05-19

- final **-0.20** (conf 0.71, pct 24) · impact -0.72 · DROP
- mean rating (1–10): **5.7** · accept votes **4/7** · percentile rank_avg 37.6 (100=best) · rank in year 66.0 (1=best)
- NAIPv2 `-1.681` · NAIP-v1 `0.490` · SciJudge `-2.298` · DGC-BERT `0.281`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/3.0) · 14B Fast `5.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The novelty of this paper is limited. The idea of compressing the key-value cache into a lower-dimensional latent space is not new. In fact, the authors mentioned that "KV states can be compressed within a model" in the paper. The novelty of this paper lies in the application of this idea to LLM communication. 2. The experiments are not convincing. The authors only conduct experimen cyclereviewer-8b.seed1: Weaknesses  1. The paper is not well written. The present

<a id="arxiv-2604.08302"></a>
### DMax: Aggressive Parallel Decoding for dLLMs

`arxiv:2604.08302` · LLMs: architectures, context, training · 2026-04-09

- final **+0.26** (conf 0.71, pct 69) · impact -0.52 · KEEP
- mean rating (1–10): **6.2** · accept votes **4/7** · percentile rank_avg 56.1 (100=best) · rank in year 40.0 (1=best)
- NAIPv2 `2.402` · NAIP-v1 `0.470` · SciJudge `-0.034` · DGC-BERT `0.709`
- CycleReviewer 8B `5.8` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `7.5` Accept (S/P/C 3.25/3.25/3.25) · 14B Fast `6.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/5420](https://t.me/gonzo_ML/5420)
- Weaknesses: cyclereviewer-8b: Weaknesses  The proposed method is not novel enough. The idea of using mask embedding and token embedding to represent the intermediate state in parallel decoding has been explored in previous works such as SM (1) and EvoToken (2). The main difference is that the proposed method uses the mask embedding as a prior to represent the uncertainty of the model. However, this idea is not new and has been deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2603.05454"></a>
### Beyond Scattered Acceptance: Fast and Coherent Inference for DLMs via Longest Stable Prefixes

`arxiv:2603.05454` · LLMs: architectures, context, training · 2026-03-05

- final **+0.07** (conf 0.71, pct 48) · impact +0.35 · WATCH
- mean rating (1–10): **6.0** · accept votes **5/7** · percentile rank_avg 59.3 (100=best) · rank in year 33.0 (1=best)
- NAIPv2 `-0.349` · NAIP-v1 `0.573` · SciJudge `1.690` · DGC-BERT `0.820`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.2` Accept · 7B Fast `5.8` Reject (S/P/C 2.75/2.75/2.75) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [derplearning/4956](https://t.me/derplearning/4956)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The proposed method is only evaluated on two DLMs, and it is unclear how the proposed method would perform on other DLMs. - The proposed method is only evaluated on a limited set of benchmarks, and it is unclear how the proposed method would perform on other benchmarks. - The proposed method is only evaluated on the inference speed, and it is unclear how the proposed method would per deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2602.08676"></a>
### LLaDA2.1: Speeding Up Text Diffusion via Token Editing

`arxiv:2602.08676` · LLMs: architectures, context, training · 2026-02-09

- final **-0.04** (conf 0.71, pct 35) · impact +0.76 · WATCH
- mean rating (1–10): **5.5** · accept votes **5/7** · percentile rank_avg 54.5 (100=best) · rank in year 42.0 (1=best)
- NAIPv2 `0.517` · NAIP-v1 `0.613` · SciJudge `2.557` · DGC-BERT `0.633`
- CycleReviewer 8B `4.0` Reject · 70B `` 
- DeepReviewer 7B Std `7.0` Accept · 7B Fast `5.5` Reject (S/P/C 2.75/2.25/2.5) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/8164](https://t.me/axisofordinary/8164)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The proposed decoding algorithm is not new. There have been many previous works that use a mixture of mask-to-token and token-to-token decoding to improve the decoding efficiency. For example, (1) also uses a mixture of mask-to-token and token-to-token decoding to improve the decoding efficiency. The main difference between the proposed method and (1) is that the proposed method use cyclereviewer-8b.seed1: Weaknesses  The paper is not well-written and the experim

<a id="arxiv-2512.24601"></a>
### Recursive Language Models

`arxiv:2512.24601` · LLMs: architectures, context, training · 2025-12-31

- final **+0.19** (conf 0.71, pct 62) · impact +0.02 · WATCH
- mean rating (1–10): **6.0** · accept votes **4/7** · percentile rank_avg 60.7 (100=best) · rank in year 33.0 (1=best)
- NAIPv2 `1.517` · NAIP-v1 `0.511` · SciJudge `1.017` · DGC-BERT `0.906`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.2` Reject · 7B Fast `5.2` Reject (S/P/C 2.5/2.75/2.25) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [axisofordinary/8235](https://t.me/axisofordinary/8235), [data_secrets/8718](https://t.me/data_secrets/8718), [AIHOUSE/1370](https://t.me/AIHOUSE/1370), [gonzo_ML/4562](https://t.me/gonzo_ML/4562)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper lacks a detailed discussion of the limitations of RLMs. While the authors mention some limitations in the appendix, a more thorough discussion in the main paper would provide a more balanced view of the approach.  2. The paper does not provide a clear comparison with other methods for handling long prompts. While the authors mention some related work in the introduction, a deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2512.14856"></a>
### T5Gemma 2: Seeing, Reading, and Understanding Longer

`arxiv:2512.14856` · LLMs: architectures, context, training · 2025-12-16

- final **-0.39** (conf 0.71, pct 15) · impact -0.26 · DROP
- mean rating (1–10): **5.4** · accept votes **2/7** · percentile rank_avg 33.5 (100=best) · rank in year 74.0 (1=best)
- NAIPv2 `-1.177` · NAIP-v1 `0.465` · SciJudge `0.722` · DGC-BERT `0.348`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/2.75) · 14B Fast `5.5` Reject
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [boris_again/3650](https://t.me/boris_again/3650), [gonzo_ML/4421](https://t.me/gonzo_ML/4421)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper does not provide a detailed comparison with other existing models in the field, making it difficult to assess its novelty and significance. - The paper does not provide a detailed discussion of the limitations of the proposed methods and potential future research directions. - The paper does not provide a detailed discussion of the ethical considerations related to the use  deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2512.13961"></a>
### Olmo 3

`arxiv:2512.13961` · LLMs: architectures, context, training · 2025-12-15

- final **+0.23** (conf 0.71, pct 65) · impact +0.38 · KEEP
- mean rating (1–10): **6.3** · accept votes **3/7** · percentile rank_avg 62.2 (100=best) · rank in year 24.0 (1=best)
- NAIPv2 `-0.192` · NAIP-v1 `0.468` · SciJudge `2.817` · DGC-BERT `0.135`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.7` Reject · 7B Fast `6.2` Reject (S/P/C 3.0/3.0/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 4.0/3.0/4.0) · SEA-E `8.0` Accept
- Telegram: [abstractDL/356](https://t.me/abstractDL/356), [j_links/8236](https://t.me/j_links/8236)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper lacks a clear and concise summary of the main contributions and findings. The introduction is lengthy and does not provide a clear overview of the paper's main contributions. The paper also lacks a clear and concise conclusion that summarizes the main findings and contributions.  The paper does not provide a clear and detailed explanation of the methodology used to train the  cyclereviewer-8b.seed1: Weaknesses  The paper lacks a clear and well-defined rese

<a id="arxiv-2512.15745"></a>
### LLaDA2.0: Scaling Up Diffusion Language Models to 100B

`arxiv:2512.15745` · LLMs: architectures, context, training · 2025-12-10

- final **+0.18** (conf 0.71, pct 59) · impact +0.79 · WATCH
- mean rating (1–10): **6.4** · accept votes **4/7** · percentile rank_avg 62.9 (100=best) · rank in year 21.0 (1=best)
- NAIPv2 `0.392` · NAIP-v1 `0.606` · SciJudge `2.352` · DGC-BERT `0.073`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `5.5` Accept (S/P/C 2.75/2.75/2.75) · 14B Fast `6.5` Reject
- OpenReviewer `8.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [gonzo_ML/5420](https://t.me/gonzo_ML/5420)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper lacks a clear motivation for the proposed approach. The authors do not provide a clear explanation of why they chose to use a discrete diffusion model instead of an autoregressive model. - The paper does not provide a detailed analysis of the computational cost of the proposed approach. The authors do not provide a clear comparison of the computational cost of their approac deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2511.09149"></a>
### Enabling Agents to Communicate Entirely in Latent Space

`arxiv:2511.09149` · LLMs: architectures, context, training · 2025-11-12

- final **+0.33** (conf 0.71, pct 76) · impact +0.04 · KEEP
- mean rating (1–10): **6.6** · accept votes **4/7** · percentile rank_avg 65.5 (100=best) · rank in year 18.0 (1=best)
- NAIPv2 `0.965` · NAIP-v1 `0.694` · SciJudge `-2.694` · DGC-BERT `0.637`
- CycleReviewer 8B `5.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.2` Reject · 7B Fast `6.0` Reject (S/P/C 3.0/3.0/2.67) · 14B Fast `7.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  - The proposed method is limited to a two-agent setting. It is unclear how it would scale to more complex multi-agent systems. - The method assumes access to internal model representations, which may not be available in all scenarios. - The method is not interpretable and may be difficult to debug or monitor.  ### Questions  - How does the method scale to more complex multi-agent syste cyclereviewer-8b.seed1: Weaknesses  The paper lacks a clear motivation for the pr

<a id="arxiv-2510.26622"></a>
### Encoder-Decoder or Decoder-Only? Revisiting Encoder-Decoder Large Language Model

`arxiv:2510.26622` · LLMs: architectures, context, training · 2025-10-30

- final **+0.07** (conf 0.71, pct 48) · impact -0.14 · WATCH
- mean rating (1–10): **5.9** · accept votes **6/7** · percentile rank_avg 52.9 (100=best) · rank in year 48.0 (1=best)
- NAIPv2 `-0.363` · NAIP-v1 `0.578` · SciJudge `-0.524` · DGC-BERT `0.763`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `5.7` Reject (S/P/C 2.67/2.33/2.67) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/4220](https://t.me/gonzo_ML/4220), [gonzo_ML/4217](https://t.me/gonzo_ML/4217)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The authors only compare the performance of the encoder-decoder and decoder-only models on a single pretraining dataset (RedPajama V1). It would be interesting to see how the models perform on other pretraining datasets, such as the Common Crawl dataset used by LLaMA.  2. The authors only compare the performance of the encoder-decoder and decoder-only models on a single finetuning d deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2510.03215"></a>
### Cache-to-Cache: Direct Semantic Communication Between Large Language Models

`arxiv:2510.03215` · LLMs: architectures, context, training · 2025-10-03

- final **+0.58** (conf 0.71, pct 97) · impact -0.02 · KEEP
- mean rating (1–10): **6.5** · accept votes **5/7** · percentile rank_avg 67.3 (100=best) · rank in year 13.0 (1=best)
- NAIPv2 `2.059` · NAIP-v1 `0.631` · SciJudge `-0.916` · DGC-BERT `0.227`
- CycleReviewer 8B `5.2` Reject · 70B `` 
- DeepReviewer 7B Std `7.0` Accept · 7B Fast `6.5` Accept (S/P/C 2.75/3.0/2.75) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [axisofordinary/7864](https://t.me/axisofordinary/7864), [data_secrets/8179](https://t.me/data_secrets/8179), [boris_again/4044](https://t.me/boris_again/4044)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper lacks a clear motivation for why KV cache is a better communication medium than text. The paper mentions that KV cache is a richer representation than text, but it does not provide any evidence to support this claim. In fact, KV cache is a lower-dimensional representation of the input, whereas text is a higher-dimensional representation. The paper also mentions that KV cach deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2507.10524"></a>
### Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation

`arxiv:2507.10524` · LLMs: architectures, context, training · 2025-07-14

- final **+0.23** (conf 0.71, pct 64) · impact +1.24 · KEEP
- mean rating (1–10): **6.0** · accept votes **7/7** · percentile rank_avg 65.7 (100=best) · rank in year 17.0 (1=best)
- NAIPv2 `0.704` · NAIP-v1 `0.743` · SciJudge `1.590` · DGC-BERT `0.916`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `5.2` Accept (S/P/C 2.75/3.0/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/3835](https://t.me/gonzo_ML/3835), [data_secrets/7384](https://t.me/data_secrets/7384)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper does not provide a detailed analysis of the computational cost of the proposed method. - The paper does not provide a detailed analysis of the memory requirements of the proposed method. - The paper does not provide a detailed analysis of the performance of the proposed method on different types of tasks.  ### Questions  - How does the proposed method compare to other metho deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2504.06225"></a>
### Encoder-Decoder Gemma: Improving the Quality-Efficiency Trade-Off via Adaptation

`arxiv:2504.06225` · LLMs: architectures, context, training · 2025-04-08

- final **-0.02** (conf 0.71, pct 37) · impact +0.12 · WATCH
- mean rating (1–10): **5.2** · accept votes **5/7** · percentile rank_avg 50.1 (100=best) · rank in year 55.0 (1=best)
- NAIPv2 `-0.588` · NAIP-v1 `0.592` · SciJudge `0.225` · DGC-BERT `0.919`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `5.0` Reject (S/P/C 2.67/3.0/2.67) · 14B Fast `6.8` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `5.0` Accept
- Telegram: [gonzo_ML/4217](https://t.me/gonzo_ML/4217), [gonzo_ML/4218](https://t.me/gonzo_ML/4218)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper lacks novelty. The idea of adapting a pretrained decoder-only LLM to an encoder-decoder LLM is not new. In fact, the authors mentioned the related work in Section 2, but they did not compare their work with the existing methods. For example, the authors did not compare their method with the method proposed in Wang et al. (2022). Wang et al. (2022) also explored the adaptati deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2502.09992"></a>
### Large Language Diffusion Models

`arxiv:2502.09992` · LLMs: architectures, context, training · 2025-02-14

- final **+0.58** (conf 0.71, pct 96) · impact +1.97 · KEEP
- mean rating (1–10): **6.7** · accept votes **6/7** · percentile rank_avg 80.6 (100=best) · rank in year 1.0 (1=best)
- NAIPv2 `0.659` · NAIP-v1 `0.700` · SciJudge `3.608` · DGC-BERT `0.892`
- CycleReviewer 8B `4.8` Reject · 70B `` 
- DeepReviewer 7B Std `8.0` Accept · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/3.0) · 14B Fast `7.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [data_secrets/6190](https://t.me/data_secrets/6190)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper lacks novelty. The proposed method is very similar to MaskGIT. The only difference is the training data and the model size. The authors should compare their method with MaskGIT more comprehensively. 2. The paper lacks experimental results. The authors only provide results on a few datasets. It is hard to evaluate the performance of the proposed method. 3. The paper lacks t deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2501.14082"></a>
### Communicating Activations Between Language Model Agents

`arxiv:2501.14082` · LLMs: architectures, context, training · 2025-01-23

- final **+0.10** (conf 0.71, pct 52) · impact -0.40 · WATCH
- mean rating (1–10): **6.2** · accept votes **6/7** · percentile rank_avg 49.8 (100=best) · rank in year 57.0 (1=best)
- NAIPv2 `-2.201` · NAIP-v1 `0.405` · SciJudge `1.197` · DGC-BERT `0.102`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.2` Accept · 7B Fast `5.8` Accept (S/P/C 2.75/3.0/2.5) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/2.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper lacks an ablation study on the hyperparameters. For example, the choice of layer $j$ and $k$ seems to be crucial. However, the authors only provide a single choice for these hyperparameters.  - The paper lacks a discussion of the limitations of the proposed method. For example, the paper does not discuss the limitations of the proposed method in terms of scalability and gen deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2501.00656"></a>
### 2 OLMo 2 Furious

`arxiv:2501.00656` · LLMs: architectures, context, training · 2024-12-31

- final **+0.30** (conf 0.71, pct 74) · impact +1.86 · KEEP
- mean rating (1–10): **6.0** · accept votes **5/7** · percentile rank_avg 58.2 (100=best) · rank in year 12.0 (1=best)
- NAIPv2 `-0.377` · NAIP-v1 `0.689` · SciJudge `3.646` · DGC-BERT `0.052`
- CycleReviewer 8B `3.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.0` Accept (S/P/C 2.75/2.75/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper does not provide a clear explanation of the model architecture, training data, and training recipe. The evaluation results are not compared to other models, making it difficult to assess the model's performance.  ## Questions  1. What is the motivation behind using a larger tokenizer vocabulary for OLMo 2? 2. How does the larger tokenizer vocabulary impact the model's perform deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2412.13663"></a>
### Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference

`arxiv:2412.13663` · LLMs: architectures, context, training · 2024-12-18

- final **+0.32** (conf 0.71, pct 75) · impact +0.22 · KEEP
- mean rating (1–10): **6.0** · accept votes **5/7** · percentile rank_avg 53.8 (100=best) · rank in year 18.0 (1=best)
- NAIPv2 `-1.003` · NAIP-v1 `0.656` · SciJudge `-1.417` · DGC-BERT `0.731`
- CycleReviewer 8B `5.2` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/3.0) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [dealerAI/1023](https://t.me/dealerAI/1023), [gonzo_ML/3090](https://t.me/gonzo_ML/3090), [gonzo_ML/3091](https://t.me/gonzo_ML/3091)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper does not provide a detailed analysis of the performance of ModernBERT on specific tasks, such as long-context retrieval and code retrieval.  - The paper does not provide a detailed analysis of the computational resources required to train and deploy ModernBERT.  - The paper does not provide a detailed analysis of the limitations of ModernBERT, such as its performance on low deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2407.21783"></a>
### The Llama 3 Herd of Models

`arxiv:2407.21783` · LLMs: architectures, context, training · 2024-07-31

- final **+0.05** (conf 0.71, pct 44) · impact +2.34 · WATCH
- mean rating (1–10): **6.0** · accept votes **3/7** · percentile rank_avg 58.3 (100=best) · rank in year 11.0 (1=best)
- NAIPv2 `-2.232` · NAIP-v1 `0.744` · SciJudge `4.050` · DGC-BERT `0.445`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Reject · 7B Fast `6.8` Accept (S/P/C 3.0/3.0/2.75) · 14B Fast `4.0` Reject
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/4.0) · SEA-E `6.0` Accept
- Telegram: [rybolos_channel/1386](https://t.me/rybolos_channel/1386), [MLResearch/1040](https://t.me/MLResearch/1040), [ai_newz/3669](https://t.me/ai_newz/3669), [gonzo_ML/3239](https://t.me/gonzo_ML/3239), [knowledge_accumulator/221](https://t.me/knowledge_accumulator/221), [j_links/7774](https://t.me/j_links/7774), [lovedeathtransformers/8609](https://t.me/lovedeathtransformers/8609)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper does not provide a detailed description of the data used for pre-training and post-training, making it difficult to assess the quality and diversity of the data. The paper also does not provide a clear explanation of the methodology used for evaluating the performance of Llama 3, making it difficult to assess the validity of the results. The paper does not provide a detailed  deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2405.12250"></a>
### Your Transformer is Secretly Linear

`arxiv:2405.12250` · LLMs: architectures, context, training · 2024-05-19

- final **-0.52** (conf 0.71, pct 9) · impact +0.12 · DROP
- mean rating (1–10): **4.9** · accept votes **3/7** · percentile rank_avg 35.7 (100=best) · rank in year 37.0 (1=best)
- NAIPv2 `-2.941` · NAIP-v1 `0.483` · SciJudge `1.824` · DGC-BERT `0.769`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `4.0` Reject (S/P/C 2.25/2.25/2.25) · 14B Fast `3.5` Reject
- OpenReviewer `5.0` Reject (S/P/C 3.0/2.0/3.0) · SEA-E `6.0` Accept
- Telegram: [seeallochnaya/1531](https://t.me/seeallochnaya/1531), [abstractDL/281](https://t.me/abstractDL/281), [dendi_math_ai/24](https://t.me/dendi_math_ai/24), [lovedeathtransformers/7691](https://t.me/lovedeathtransformers/7691)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper focuses on the linearity of transformer decoders, which is a relatively narrow topic. The paper could benefit from a more thorough discussion of related work on sparsity and pruning in transformers. The paper also could benefit from a more in-depth analysis of the limitations of the proposed method.  ### Questions  1. What are the limitations of the proposed method? How does  deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2405.04517"></a>
### xLSTM: Extended Long Short-Term Memory

`arxiv:2405.04517` · LLMs: architectures, context, training · 2024-05-07

- final **-0.44** (conf 0.71, pct 11) · impact +0.60 · WATCH
- mean rating (1–10): **4.5** · accept votes **2/7** · percentile rank_avg 35.4 (100=best) · rank in year 38.0 (1=best)
- NAIPv2 `-1.738` · NAIP-v1 `0.465` · SciJudge `3.424` · DGC-BERT `0.254`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `3.5` Reject (S/P/C 2.0/2.0/1.75) · 14B Fast `6.2` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `4.0` Reject
- Telegram: [gonzo_ML/2624](https://t.me/gonzo_ML/2624), [gonzo_ML/2626](https://t.me/gonzo_ML/2626), [axisofordinary/6294](https://t.me/axisofordinary/6294), [data_secrets/4008](https://t.me/data_secrets/4008), [lovedeathtransformers/8203](https://t.me/lovedeathtransformers/8203)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper presents a new LSTM architecture that is designed to address the limitations of the original LSTM model. The authors introduce two new components: a scalar memory and a matrix memory, and a new update rule based on covariance. The authors also introduce a new gating mechanism that is designed to improve the performance of the model. The authors evaluate the proposed model on  cyclereviewer-8b.seed1: Weaknesses  The paper does not provide a clear motivation

<a id="arxiv-2404.09173"></a>
### TransformerFAM: Feedback attention is working memory

`arxiv:2404.09173` · LLMs: architectures, context, training · 2024-04-14

- final **-0.15** (conf 0.71, pct 27) · impact +0.30 · WATCH
- mean rating (1–10): **5.5** · accept votes **3/7** · percentile rank_avg 47.3 (100=best) · rank in year 24.0 (1=best)
- NAIPv2 `-2.414` · NAIP-v1 `0.595` · SciJudge `0.830` · DGC-BERT `0.948`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.8` Reject · 7B Fast `6.0` Reject (S/P/C 2.75/3.0/2.5) · 14B Fast `4.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/2585](https://t.me/gonzo_ML/2585), [gonzo_ML/2586](https://t.me/gonzo_ML/2586), [axisofordinary/6257](https://t.me/axisofordinary/6257)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The experiments are not convincing. The authors only evaluate the proposed method on a few datasets, and the results are not significantly better than the baselines. The authors should conduct more experiments to demonstrate the effectiveness of the proposed method.  2. The authors should provide more details about the implementation of the proposed method. For example, how to initi deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2404.07143"></a>
### Leave No Context Behind: Efficient Infinite Context Transformers with Infini-attention

`arxiv:2404.07143` · LLMs: architectures, context, training · 2024-04-10

- final **-0.12** (conf 0.71, pct 29) · impact +0.62 · WATCH
- mean rating (1–10): **5.5** · accept votes **3/7** · percentile rank_avg 44.1 (100=best) · rank in year 26.0 (1=best)
- NAIPv2 `-2.006` · NAIP-v1 `0.497` · SciJudge `3.254` · DGC-BERT `0.878`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Reject · 7B Fast `5.8` Accept (S/P/C 2.5/2.5/2.75) · 14B Fast `5.5` Reject
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [lovedeathtransformers/7589](https://t.me/lovedeathtransformers/7589), [gonzo_ML/2585](https://t.me/gonzo_ML/2585), [gonzo_ML/2586](https://t.me/gonzo_ML/2586), [chillhousetech/690](https://t.me/chillhousetech/690), [axisofordinary/6247](https://t.me/axisofordinary/6247)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The proposed method is not as effective as the baseline methods on the long-context language modeling tasks. - The proposed method is not evaluated on the long-context tasks with 8B LLMs.  ### Questions  - The proposed method is not as effective as the baseline methods on the long-context language modeling tasks. For example, the proposed method achieves a perplexity of 2.29 on PG19, deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2311.06242"></a>
### Florence-2: Advancing a Unified Representation for a Variety of Vision Tasks

`arxiv:2311.06242` · LLMs: architectures, context, training · 2023-11-10

- final **+0.25** (conf 0.71, pct 67) · impact +0.09 · KEEP
- mean rating (1–10): **6.1** · accept votes **4/7** · percentile rank_avg 53.8 (100=best) · rank in year 16.0 (1=best)
- NAIPv2 `-1.918` · NAIP-v1 `0.479` · SciJudge `2.835` · DGC-BERT `0.049`
- CycleReviewer 8B `6.0` Reject · 70B `` 
- DeepReviewer 7B Std `8.0` Accept · 7B Fast `6.5` Accept (S/P/C 3.0/3.0/2.75) · 14B Fast `6.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [boris_again/3018](https://t.me/boris_again/3018), [lovedeathtransformers/7855](https://t.me/lovedeathtransformers/7855), [axisofordinary/5811](https://t.me/axisofordinary/5811), [AI_DeepLearning/1076](https://t.me/AI_DeepLearning/1076), [lovedeathtransformers/9741](https://t.me/lovedeathtransformers/9741), [gonzo_ML/3270](https://t.me/gonzo_ML/3270)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper does not provide a detailed analysis of the model's performance on specific tasks, such as object detection and image captioning. It would be helpful to include more quantitative results and analysis to demonstrate the model's performance on these tasks.  The paper does not provide a detailed analysis of the model's performance on tasks that require more complex reasoning, su deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2306.13575"></a>
### Scaling MLPs: A Tale of Inductive Bias

`arxiv:2306.13575` · LLMs: architectures, context, training · 2023-06-23

- final **+0.26** (conf 0.71, pct 68) · impact -0.05 · KEEP
- mean rating (1–10): **5.6** · accept votes **3/7** · percentile rank_avg 46.6 (100=best) · rank in year 28.0 (1=best)
- NAIPv2 `-1.609` · NAIP-v1 `0.617` · SciJudge `-0.042` · DGC-BERT `0.307`
- CycleReviewer 8B `4.0` Reject · 70B `` 
- DeepReviewer 7B Std `8.0` Accept · 7B Fast `6.0` Reject (S/P/C 2.67/3.0/2.33) · 14B Fast `6.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/1674](https://t.me/gonzo_ML/1674)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The novelty of this paper is limited. The authors mainly study the performance of MLPs on vision tasks and show that they can achieve strong performance with sufficient scale. This is not surprising and has been shown in previous works such as (1).  2. The authors do not provide any theoretical analysis for the performance of MLPs.  3. The authors do not compare the performance of M deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2305.01625"></a>
### Unlimiformer: Long-Range Transformers with Unlimited Length Input

`arxiv:2305.01625` · LLMs: architectures, context, training · 2023-05-02

- final **+0.22** (conf 0.71, pct 63) · impact -0.29 · KEEP
- mean rating (1–10): **5.8** · accept votes **5/7** · percentile rank_avg 50.4 (100=best) · rank in year 24.0 (1=best)
- NAIPv2 `0.546` · NAIP-v1 `0.543` · SciJudge `0.005` · DGC-BERT `0.843`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `5.8` Accept (S/P/C 2.75/2.5/2.5) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/1584](https://t.me/gonzo_ML/1584), [axisofordinary/4895](https://t.me/axisofordinary/4895), [gonzo_ML/1507](https://t.me/gonzo_ML/1507)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The method is only evaluated on summarization tasks. It is unclear how the method will perform on other tasks such as translation. - The method requires a kNN search over the encoder output, which can be slow. This may limit the applicability of the method to long inputs. - The method requires a large amount of memory to store the kNN index, which can be a limitation for very long in deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2302.14045"></a>
### Language Is Not All You Need: Aligning Perception with Language Models

`arxiv:2302.14045` · LLMs: architectures, context, training · 2023-02-27

- final **+0.35** (conf 0.71, pct 77) · impact +1.02 · KEEP
- mean rating (1–10): **6.2** · accept votes **6/7** · percentile rank_avg 67.3 (100=best) · rank in year 4.0 (1=best)
- NAIPv2 `-1.012` · NAIP-v1 `0.670` · SciJudge `3.013` · DGC-BERT `0.908`
- CycleReviewer 8B `6.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/2.67) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [gonzo_ML/2009](https://t.me/gonzo_ML/2009), [scitator_ai/79](https://t.me/scitator_ai/79), [gonzo_ML/1364](https://t.me/gonzo_ML/1364), [axisofordinary/4500](https://t.me/axisofordinary/4500), [gonzo_ML/1339](https://t.me/gonzo_ML/1339), [derplearning/2399](https://t.me/derplearning/2399), [j_links/6507](https://t.me/j_links/6507), [derplearning/2372](https://t.me/derplearning/2372)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper does not provide a detailed analysis of the limitations of the proposed approach. 2. The paper does not provide a comparison with other state-of-the-art models on the same tasks. 3. The paper does not provide a discussion of the potential applications of the proposed approach.  ### Questions  1. Can you provide a detailed analysis of the limitations of the proposed approac deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2302.10866"></a>
### Hyena Hierarchy: Towards Larger Convolutional Language Models

`arxiv:2302.10866` · LLMs: architectures, context, training · 2023-02-21

- final **+0.53** (conf 0.71, pct 93) · impact +1.24 · KEEP
- mean rating (1–10): **6.2** · accept votes **6/7** · percentile rank_avg 69.8 (100=best) · rank in year 2.0 (1=best)
- NAIPv2 `-0.003` · NAIP-v1 `0.679` · SciJudge `3.511` · DGC-BERT `0.908`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.5` Accept (S/P/C 3.0/3.25/2.5) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [ntr_neural/218](https://t.me/ntr_neural/218), [gonzo_ML/1754](https://t.me/gonzo_ML/1754), [axisofordinary/4834](https://t.me/axisofordinary/4834)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper does not provide a thorough comparison with other attention-free models, such as RWKV and AFT. It would be helpful to include a comparison with these models in the main text. - The paper does not provide a thorough analysis of the computational complexity of Hyena. It would be helpful to include a more detailed analysis of the computational complexity in the main text. - Th deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2302.07253"></a>
### Energy Transformer

`arxiv:2302.07253` · LLMs: architectures, context, training · 2023-02-14

- final **-0.37** (conf 0.71, pct 16) · impact -0.72 · DROP
- mean rating (1–10): **5.6** · accept votes **4/7** · percentile rank_avg 34.5 (100=best) · rank in year 41.0 (1=best)
- NAIPv2 `-2.529` · NAIP-v1 `0.485` · SciJudge `-0.631` · DGC-BERT `0.732`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.2` Reject · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/2.5) · 14B Fast `6.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `5.0` Accept
- Telegram: [axisofordinary/4425](https://t.me/axisofordinary/4425)
- Weaknesses: cyclereviewer-8b: Weaknesses  The main weakness of this paper is that the proposed model is not well motivated. The authors claim that the proposed model is based on a sequence of attention layers that are designed to minimize a specifically engineered energy function. However, it is not clear why this is a good idea. The authors do not provide any theoretical justification for the proposed model, and the experimen deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2207.02098"></a>
### Neural Networks and the Chomsky Hierarchy

`arxiv:2207.02098` · LLMs: architectures, context, training · 2022-07-05

- final **+0.34** (conf 0.71, pct 77) · impact -1.18 · KEEP
- mean rating (1–10): **6.4** · accept votes **7/7** · percentile rank_avg 51.4 (100=best) · rank in year 10.0 (1=best)
- NAIPv2 `-1.336` · NAIP-v1 `0.379` · SciJudge `-1.255` · DGC-BERT `0.580`
- CycleReviewer 8B `5.8` Accept · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `5.8` Accept (S/P/C 2.75/3.0/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/4.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/1049](https://t.me/gonzo_ML/1049)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper does not provide any theoretical analysis of the generalization of neural networks, and the authors only provide empirical results.  ### Questions  1. Why do the authors only consider the Chomsky hierarchy, but not other computational models? For example, the Blum-Shub machine (BSM) is a more general model than the Turing machine, and it has been shown that RNNs are equivalen deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2203.08913"></a>
### Memorizing Transformers

`arxiv:2203.08913` · LLMs: architectures, context, training · 2022-03-16

- final **+0.28** (conf 0.71, pct 72) · impact +0.36 · KEEP
- mean rating (1–10): **6.3** · accept votes **5/7** · percentile rank_avg 60.2 (100=best) · rank in year 4.0 (1=best)
- NAIPv2 `-1.776` · NAIP-v1 `0.668` · SciJudge `1.050` · DGC-BERT `0.663`
- CycleReviewer 8B `6.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `6.2` Accept (S/P/C 3.25/3.25/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [gonzo_ML/1507](https://t.me/gonzo_ML/1507), [abstractDL/198](https://t.me/abstractDL/198), [axisofordinary/4642](https://t.me/axisofordinary/4642), [j_links/6549](https://t.me/j_links/6549), [dlinnlp/1565](https://t.me/dlinnlp/1565), [lovedeathtransformers/5700](https://t.me/lovedeathtransformers/5700)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper does not provide a thorough analysis of the proposed method. For example, the authors do not provide an ablation study on the effect of the memory size, the number of heads, or the number of layers. The authors also do not provide a comparison with other long-range attention methods. - The paper does not provide a detailed explanation of the experimental setup. For example, deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2002.05202"></a>
### GLU Variants Improve Transformer

`arxiv:2002.05202` · LLMs: architectures, context, training · 2020-02-12

- final **-0.70** (conf 0.71, pct 3) · impact -1.07 · DROP
- mean rating (1–10): **3.5** · accept votes **1/7** · percentile rank_avg 16.8 (100=best) · rank in year 11.0 (1=best)
- NAIPv2 `-2.363` · NAIP-v1 `0.392` · SciJudge `-0.798` · DGC-BERT `0.806`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `3.0` Reject · 7B Fast `2.3` Reject (S/P/C 1.67/1.67/1.67) · 14B Fast `4.0` Reject
- OpenReviewer `3.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `5.0` Reject
- Telegram: [gonzo_ML/4099](https://t.me/gonzo_ML/4099), [gonzo_ML/4071](https://t.me/gonzo_ML/4071), [gonzo_ML/3592](https://t.me/gonzo_ML/3592), [dealerAI/1023](https://t.me/dealerAI/1023), [gonzo_ML/2500](https://t.me/gonzo_ML/2500), [seeallochnaya/1165](https://t.me/seeallochnaya/1165)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The main concern is the novelty of the proposed method. The GLU unit has been proposed in 2016, and it has been widely used in many NLP tasks. The proposed method is simply replacing the FFN with GLU and its variants. The novelty of the proposed method is limited.  2. The evaluation is limited to T5, and the results on other tasks are missing. It is unclear whether the proposed meth deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-1710.05941"></a>
### Searching for Activation Functions

`arxiv:1710.05941` · LLMs: architectures, context, training · 2017-10-16

- final **+0.10** (conf 0.71, pct 51) · impact +0.93 · WATCH
- mean rating (1–10): **5.7** · accept votes **4/7** · percentile rank_avg 46.7 (100=best) · rank in year 4.0 (1=best)
- NAIPv2 `-1.962` · NAIP-v1 `0.734` · SciJudge `1.835` · DGC-BERT `0.614`
- CycleReviewer 8B `5.8` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `6.0` Accept (S/P/C 3.0/3.25/2.75) · 14B Fast `5.8` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/2.0/2.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/364](https://t.me/gonzo_ML/364), [j_links/542](https://t.me/j_links/542)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The novelty of the paper is limited. The search space is very similar to the one proposed in Bello et al. (2017). The search method is also similar to the one used in Zoph & Le (2016).  - The experiments are not convincing. The authors only compare their method with a few baselines. The proposed activation function is only evaluated on a few datasets. The authors also do not compare  deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="doi-10.1073-pnas.2520095123"></a>
### Evidence from formal logical reasoning reveals that the language of thought is not natural language

`doi:10.1073/pnas.2520095123` · Reasoning and the "physics" of language models · 2026-07-06

- final **-0.11** (conf 0.70, pct 30) · impact -1.14 · WATCH · partial fulltext
- mean rating (1–10): **5.7** · accept votes **5/7** · percentile rank_avg 41.4 (100=best) · rank in year 62.0 (1=best)
- NAIPv2 `-1.912` · NAIP-v1 `0.588` · SciJudge `-7.299` · DGC-BERT `0.105`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `5.5` Accept (S/P/C 2.75/2.75/2.75) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper does not provide a clear hypothesis or research question. The abstract suggests that the paper aims to investigate the relationship between logical reasoning and language, but the specific research question or hypothesis is not stated. This makes it difficult to understand the purpose of the study and evaluate the results in the context of the research question.  2. The pa deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2606.31779"></a>
### Bridging the Gap Between Latent and Explicit Reasoning with Looped Transformers

`arxiv:2606.31779` · Reasoning and the "physics" of language models · 2026-06-30

- final **+0.36** (conf 0.71, pct 79) · impact +1.03 · KEEP
- mean rating (1–10): **6.0** · accept votes **5/7** · percentile rank_avg 65.0 (100=best) · rank in year 20.0 (1=best)
- NAIPv2 `2.404` · NAIP-v1 `0.771` · SciJudge `0.833` · DGC-BERT `0.735`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.5` Accept (S/P/C 3.0/3.0/2.5) · 14B Fast `6.2` Reject
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/5761](https://t.me/gonzo_ML/5761)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The proposed method is only evaluated on math reasoning tasks. It would be interesting to see how it performs on other tasks, such as language translation or question answering. 2. The proposed method is only compared to one previous method. It would be interesting to see how it compares to other methods.  ### Questions  1. How does the proposed method compare to other methods on ot deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2606.25010"></a>
### Emergent Capabilities Arise Randomly from Learning Sparse Attention Patterns

`arxiv:2606.25010` · Reasoning and the "physics" of language models · 2026-06-23

- final **+0.02** (conf 0.71, pct 40) · impact -0.94 · WATCH
- mean rating (1–10): **6.0** · accept votes **4/7** · percentile rank_avg 53.6 (100=best) · rank in year 46.0 (1=best)
- NAIPv2 `-0.768` · NAIP-v1 `0.409` · SciJudge `-0.623` · DGC-BERT `0.879`
- CycleReviewer 8B `5.2` Reject · 70B `` 
- DeepReviewer 7B Std `6.2` Reject · 7B Fast `7.0` Accept (S/P/C 2.75/3.0/3.0) · 14B Fast `6.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/5867](https://t.me/gonzo_ML/5867)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper does not seem to have any significant contributions. The authors show that the emergence of capabilities is driven by the learning of task-relevant attention patterns. This is not a new finding. The authors also show that the difficulty of learning attention patterns depends on context length and pattern sparsity. This is also not a new finding. The authors also show that sca cyclereviewer-8b.seed1: Weaknesses  1. The experiments are not very convincing. T

<a id="arxiv-2606.03982"></a>
### Language Models Compare Quantities Using Number-specific and Unit-specific Heuristics

`arxiv:2606.03982` · Reasoning and the "physics" of language models · 2026-06-02

- final **-0.01** (conf 0.71, pct 37) · impact -1.39 · WATCH
- mean rating (1–10): **6.0** · accept votes **4/7** · percentile rank_avg 45.3 (100=best) · rank in year 59.0 (1=best)
- NAIPv2 `-0.947` · NAIP-v1 `0.431` · SciJudge `-3.789` · DGC-BERT `0.120`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/2.5) · 14B Fast `6.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper lacks novelty. The authors have conducted a thorough analysis of language models' behavior in comparing quantities with measurement units. However, the results are not surprising, and the conclusions drawn from the analysis are not particularly novel or groundbreaking. The paper could benefit from a more in-depth exploration of the implications of these findings or a more  deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2605.07654"></a>
### Reliable Chain-of-Thought via Prefix Consistency

`arxiv:2605.07654` · Reasoning and the "physics" of language models · 2026-05-08

- final **+0.31** (conf 0.71, pct 75) · impact +0.98 · KEEP
- mean rating (1–10): **6.2** · accept votes **6/7** · percentile rank_avg 65.7 (100=best) · rank in year 17.0 (1=best)
- NAIPv2 `0.827` · NAIP-v1 `0.720` · SciJudge `1.572` · DGC-BERT `0.774`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.8` Accept · 7B Fast `7.0` Accept (S/P/C 3.25/3.25/3.0) · 14B Fast `6.8` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper lacks sufficient analysis of the proposed method. For example, the paper does not provide any theoretical analysis of the proposed method. The authors only show that the reproduction rate is higher for correct answers than for incorrect answers. However, it is not clear why this is the case or how it leads to the proposed method. It would be helpful to provide a more detai cyclereviewer-8b.seed1: Weaknesses  1. The paper does not discuss the limitations

<a id="arxiv-2604.11791"></a>
### A Mechanistic Analysis of Looped Reasoning Language Models

`arxiv:2604.11791` · Reasoning and the "physics" of language models · 2026-04-13

- final **-0.21** (conf 0.71, pct 23) · impact -1.38 · DROP
- mean rating (1–10): **6.2** · accept votes **3/7** · percentile rank_avg 46.0 (100=best) · rank in year 58.0 (1=best)
- NAIPv2 `-0.953` · NAIP-v1 `0.346` · SciJudge `-2.487` · DGC-BERT `0.489`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `5.8` Reject (S/P/C 2.75/2.75/2.5) · 14B Fast `6.5` Reject
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/5206](https://t.me/gonzo_ML/5206)
- Weaknesses: cyclereviewer-8b: Weaknesses  The main weakness of the paper is that it is unclear what the contribution of the paper is. The paper studies the behavior of looped LLMs, but it is not clear what this behavior tells us about how to design better looped LLMs. The authors do not provide any practical guidance on how to design better looped LLMs based on their results.  ### Questions  I would like to see more discussion deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2604.01754"></a>
### LiveMathematicianBench: A Live Benchmark for Mathematician-Level Reasoning with Proof Sketches

`arxiv:2604.01754` · Reasoning and the "physics" of language models · 2026-04-02

- final **+0.03** (conf 0.71, pct 41) · impact +1.84 · WATCH
- mean rating (1–10): **6.8** · accept votes **4/7** · percentile rank_avg 70.5 (100=best) · rank in year 8.0 (1=best)
- NAIPv2 `-0.744` · NAIP-v1 `0.756` · SciJudge `3.322` · DGC-BERT `0.424`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.0` Reject (S/P/C 3.0/2.5/2.5) · 14B Fast `5.8` Reject
- OpenReviewer `8.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `8.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: weaknesses of each model.  ### Weaknesses  1. The paper does not provide a detailed description of the dataset used to train the models being evaluated. This makes it difficult to understand the potential biases and limitations of the models and how they may impact the results. 2. The paper does not provide a detailed analysis of the potential sources of error in the benchmark. This makes it diffi deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2602.10416"></a>
### AI-rithmetic

`arxiv:2602.10416` · Reasoning and the "physics" of language models · 2026-02-11

- final **-0.53** (conf 0.71, pct 8) · impact -0.02 · DROP
- mean rating (1–10): **5.5** · accept votes **2/7** · percentile rank_avg 34.8 (100=best) · rank in year 69.0 (1=best)
- NAIPv2 `-1.744` · NAIP-v1 `0.367` · SciJudge `3.162` · DGC-BERT `0.162`
- CycleReviewer 8B `5.8` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `5.2` Accept (S/P/C 2.75/3.0/2.5) · 14B Fast `5.8` Reject
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper does not provide a clear explanation of why the error rate is periodic with respect to the length of the numbers being added. - The paper does not provide a clear explanation of why the error rate is higher for numbers whose length is not a multiple of 3. - The paper does not provide a clear explanation of why the error rate is higher for numbers whose length is not a multi cyclereviewer-8b.seed1: Weaknesses  - The paper only considers the task of adding

<a id="openreview-klU4737opt"></a>
### Position: LLMs can't jump

`openreview:klU4737opt` · Reasoning and the "physics" of language models · unknown

- final **-0.37** (conf 0.71, pct 15) · impact -1.34 · DROP
- mean rating (1–10): **5.5** · accept votes **2/7** · percentile rank_avg 27.8 (100=best) · rank in year 9.0 (1=best)
- NAIPv2 `-3.801` · NAIP-v1 `0.327` · SciJudge `-1.420` · DGC-BERT `0.040`
- CycleReviewer 8B `6.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.2` Reject · 7B Fast `5.0` Reject (S/P/C 2.5/2.25/2.5) · 14B Fast `4.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper does not provide a clear definition of what is meant by "abductive leap" or how it differs from inductive and deductive reasoning. - The paper does not provide a clear explanation of how physically consistent, multimodal world models could enable AI systems to make abductive leaps. - The paper does not provide a clear evaluation of the proposed solution or a plan for how it deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2512.16902"></a>
### In-Context Algebra

`arxiv:2512.16902` · Reasoning and the "physics" of language models · 2025-12-18

- final **+0.41** (conf 0.71, pct 84) · impact -0.78 · KEEP
- mean rating (1–10): **6.8** · accept votes **7/7** · percentile rank_avg 67.9 (100=best) · rank in year 11.0 (1=best)
- NAIPv2 `-0.869` · NAIP-v1 `0.504` · SciJudge `-2.895` · DGC-BERT `0.931`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.8` Accept · 7B Fast `6.2` Accept (S/P/C 3.0/2.75/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/4.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper does not provide a comprehensive review of the existing literature on in-context learning and its applications. The authors should provide a more detailed discussion of the current state of the field and how their work contributes to it.  - The paper does not provide a clear explanation of the limitations of the proposed approach. The authors should discuss the potential li deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2510.00184"></a>
### Why Can't Transformers Learn Multiplication? Reverse-Engineering Reveals Long-Range Dependency Pitfalls

`arxiv:2510.00184` · Reasoning and the "physics" of language models · 2025-09-30

- final **+0.05** (conf 0.71, pct 45) · impact +0.43 · WATCH
- mean rating (1–10): **6.3** · accept votes **6/7** · percentile rank_avg 59.7 (100=best) · rank in year 37.0 (1=best)
- NAIPv2 `-1.400` · NAIP-v1 `0.696` · SciJudge `-0.497` · DGC-BERT `0.774`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `6.8` Accept (S/P/C 3.0/3.0/2.5) · 14B Fast `6.7` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/7757](https://t.me/axisofordinary/7757)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper only studies a simple 2-layer model. It would be interesting to see how the findings generalize to larger models. - The paper only considers a single task. It would be interesting to see how the findings generalize to other tasks that require long-range dependencies.  ### Questions  - How do the findings generalize to larger models? - How do the findings generalize to other deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2509.25239"></a>
### A Formal Comparison Between Chain of Thought and Latent Thought

`arxiv:2509.25239` · Reasoning and the "physics" of language models · 2025-09-25

- final **+0.13** (conf 0.71, pct 55) · impact -1.01 · WATCH
- mean rating (1–10): **6.0** · accept votes **5/7** · percentile rank_avg 48.9 (100=best) · rank in year 58.0 (1=best)
- NAIPv2 `-2.500` · NAIP-v1 `0.488` · SciJudge `-3.979` · DGC-BERT `0.853`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.0` Reject (S/P/C 3.0/3.0/3.0) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper focuses on theoretical analysis and lacks empirical validation of the theoretical results. The experimental results are limited to a few simple tasks and do not demonstrate the practical applicability of the theoretical findings. 2. The paper does not discuss the limitations of the theoretical analysis, such as the assumptions made and the potential biases introduced. 3. T deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2509.20317"></a>
### SIM-CoT: Supervised Implicit Chain-of-Thought

`arxiv:2509.20317` · Reasoning and the "physics" of language models · 2025-09-24

- final **+0.30** (conf 0.71, pct 74) · impact +0.71 · KEEP
- mean rating (1–10): **6.5** · accept votes **6/7** · percentile rank_avg 70.8 (100=best) · rank in year 8.0 (1=best)
- NAIPv2 `1.872` · NAIP-v1 `0.683` · SciJudge `0.980` · DGC-BERT `0.939`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `3.8` Reject · 7B Fast `6.3` Accept (S/P/C 3.0/3.0/2.67) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [abstractDL/348](https://t.me/abstractDL/348), [boris_again/3470](https://t.me/boris_again/3470)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper only evaluates the method on a single dataset, GSM8k-Aug, which is a relatively small dataset. It would be good to see the performance of SIM-CoT on other datasets, such as GSM-Hard, MultiArith, and SVAMP. 2. The paper does not provide a detailed analysis of the computational cost of SIM-CoT. While it is mentioned that the auxiliary decoder is removed at inference, it is n deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2508.02513"></a>
### Modular Arithmetic: Language Models Solve Math Digit by Digit

`arxiv:2508.02513` · Reasoning and the "physics" of language models · 2025-08-04

- final **+0.09** (conf 0.71, pct 50) · impact +0.27 · WATCH
- mean rating (1–10): **6.2** · accept votes **6/7** · percentile rank_avg 61.6 (100=best) · rank in year 27.0 (1=best)
- NAIPv2 `-0.951` · NAIP-v1 `0.661` · SciJudge `-0.412` · DGC-BERT `0.733`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.2` Accept · 7B Fast `5.8` Reject (S/P/C 2.75/2.5/2.5) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The authors only consider addition and subtraction in their experiments. It would be interesting to see if the proposed approach can be extended to more complex arithmetic operations such as multiplication and division. 2. The authors only consider MLP layers in their analysis. It would be interesting to see if the proposed approach can be extended to other components such as attent deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2506.10947"></a>
### Spurious Rewards: Rethinking Training Signals in RLVR

`arxiv:2506.10947` · Reasoning and the "physics" of language models · 2025-06-12

- final **+0.45** (conf 0.70, pct 87) · impact -1.06 · KEEP · salvage dr7bf
- mean rating (1–10): **7.1** · accept votes **7/7** · percentile rank_avg 70.1 (100=best) · rank in year 9.0 (1=best)
- NAIPv2 `-0.237` · NAIP-v1 `0.326` · SciJudge `0.084` · DGC-BERT `0.888`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.2` Accept · 7B Fast ``  (S/P/C 3.0/3.0/3.0) · 14B Fast `7.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [buckwheat_thoughts/306](https://t.me/buckwheat_thoughts/306), [gonzo_ML/4702](https://t.me/gonzo_ML/4702)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper does not provide a clear explanation for why spurious rewards can lead to improvements in performance. The authors hypothesize that it is due to the clipping bias in GRPO, but this is not clearly explained. It would be helpful if the authors could provide a more detailed explanation of this phenomenon. - The paper only considers a single type of spurious reward, which is ra deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2505.21493"></a>
### Reinforcing General Reasoning without Verifiers

`arxiv:2505.21493` · Reasoning and the "physics" of language models · 2025-05-27

- final **+0.59** (conf 0.71, pct 97) · impact +0.52 · KEEP
- mean rating (1–10): **6.6** · accept votes **6/7** · percentile rank_avg 73.2 (100=best) · rank in year 6.0 (1=best)
- NAIPv2 `0.858` · NAIP-v1 `0.455` · SciJudge `3.250` · DGC-BERT `0.812`
- CycleReviewer 8B `5.2` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `7.0` Accept (S/P/C 3.25/3.0/3.0) · 14B Fast `6.8` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `8.0` Accept
- Telegram: [buckwheat_thoughts/306](https://t.me/buckwheat_thoughts/306), [gonzo_ML/4702](https://t.me/gonzo_ML/4702)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The proposed method relies on the assumption that there is a single correct answer for each question. However, this assumption may not hold for many general reasoning tasks, such as open-ended questions or questions with multiple correct answers. The paper does not discuss this limitation. - The proposed method is not novel. The idea of using the probability of the correct answer as  deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2505.21444"></a>
### Can Large Reasoning Models Self-Train?

`arxiv:2505.21444` · Reasoning and the "physics" of language models · 2025-05-27

- final **-0.23** (conf 0.71, pct 23) · impact -0.82 · DROP
- mean rating (1–10): **6.0** · accept votes **2/7** · percentile rank_avg 42.5 (100=best) · rank in year 66.0 (1=best)
- NAIPv2 `-1.297` · NAIP-v1 `0.361` · SciJudge `0.133` · DGC-BERT `0.480`
- CycleReviewer 8B `5.5` Reject · 70B `` 
- DeepReviewer 7B Std `5.2` Reject · 7B Fast `5.5` Reject (S/P/C 2.75/3.0/2.5) · 14B Fast `5.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [buckwheat_thoughts/306](https://t.me/buckwheat_thoughts/306), [gonzo_ML/4702](https://t.me/gonzo_ML/4702)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper is a bit incremental, as it is a simple extension of the previous work. The authors should discuss more about the difference between the previous work and the current work.  2. The authors should discuss more about the limitations of the paper.  3. The authors should discuss more about the potential future work.  ### Questions  1. The authors should discuss more about the  deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2505.15134"></a>
### The Unreasonable Effectiveness of Entropy Minimization in LLM Reasoning

`arxiv:2505.15134` · Reasoning and the "physics" of language models · 2025-05-21

- final **+0.29** (conf 0.71, pct 73) · impact +2.22 · KEEP
- mean rating (1–10): **6.3** · accept votes **6/7** · percentile rank_avg 68.2 (100=best) · rank in year 10.0 (1=best)
- NAIPv2 `-0.945` · NAIP-v1 `0.718` · SciJudge `3.711` · DGC-BERT `0.750`
- CycleReviewer 8B `4.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.2` Accept · 7B Fast `6.5` Accept (S/P/C 3.25/3.25/2.75) · 14B Fast `7.0` Accept
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/3.0) · SEA-E `6.0` Accept
- Telegram: [buckwheat_thoughts/306](https://t.me/buckwheat_thoughts/306), [gonzo_ML/4702](https://t.me/gonzo_ML/4702)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper lacks novelty. The proposed methods are simple and have been explored in previous works. The main difference is that this paper applies these methods to LLMs. 2. The paper lacks ablation studies. The authors only show the results of the proposed methods without showing the results of the individual components. 3. The paper lacks comparison with other methods. The authors o cyclereviewer-8b.seed1: Weaknesses  - The paper lacks a theoretical analysis of w

<a id="arxiv-2505.13763"></a>
### Language Models Are Capable of Metacognitive Monitoring and Control of Their Internal Activations

`arxiv:2505.13763` · Reasoning and the "physics" of language models · 2025-05-19

- final **-0.15** (conf 0.71, pct 27) · impact +0.06 · WATCH
- mean rating (1–10): **6.5** · accept votes **4/7** · percentile rank_avg 50.7 (100=best) · rank in year 52.0 (1=best)
- NAIPv2 `-1.741` · NAIP-v1 `0.559` · SciJudge `0.290` · DGC-BERT `0.055`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `4.8` Reject · 7B Fast `6.2` Reject (S/P/C 2.5/3.0/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/4.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/7240](https://t.me/axisofordinary/7240)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper lacks a discussion of the limitations of the proposed neurofeedback paradigm. For example, how do the authors ensure that the LLMs are not just memorizing the relationship between the input and the label, rather than actually understanding the underlying concept? How do the authors ensure that the LLMs are not just exploiting the correlation between the input and the label deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2504.20571"></a>
### Reinforcement Learning for Reasoning in Large Language Models with One Training Example

`arxiv:2504.20571` · Reasoning and the "physics" of language models · 2025-04-29

- final **+0.26** (conf 0.71, pct 69) · impact +0.93 · KEEP
- mean rating (1–10): **5.9** · accept votes **4/7** · percentile rank_avg 58.3 (100=best) · rank in year 40.0 (1=best)
- NAIPv2 `1.729` · NAIP-v1 `0.521` · SciJudge `3.507` · DGC-BERT `0.725`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [buckwheat_thoughts/306](https://t.me/buckwheat_thoughts/306), [axisofordinary/7262](https://t.me/axisofordinary/7262), [data_secrets/6880](https://t.me/data_secrets/6880), [tech_priestess/2091](https://t.me/tech_priestess/2091), [axisofordinary/7159](https://t.me/axisofordinary/7159), [gonzo_ML/4702](https://t.me/gonzo_ML/4702), [boris_again/3219](https://t.me/boris_again/3219)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper only investigates the effectiveness of RLVR with a single training example on a base model Qwen2.5-Math-1.5B. It would be interesting to see if the results hold for other base models and RL algorithms.  2. The paper only investigates the effectiveness of RLVR with a single training example on a base model Qwen2.5-Math-1.5B. It would be interesting to see if the results hol deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2503.21676"></a>
### How do language models learn facts? Dynamics, curricula and hallucinations

`arxiv:2503.21676` · Reasoning and the "physics" of language models · 2025-03-27

- final **+0.37** (conf 0.71, pct 80) · impact -0.04 · KEEP
- mean rating (1–10): **6.5** · accept votes **6/7** · percentile rank_avg 62.5 (100=best) · rank in year 23.0 (1=best)
- NAIPv2 `-0.619` · NAIP-v1 `0.448` · SciJudge `1.715` · DGC-BERT `0.792`
- CycleReviewer 8B `4.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `7.0` Accept (S/P/C 3.0/3.25/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/4.0) · SEA-E `7.0` Accept
- Telegram: [data_secrets/6564](https://t.me/data_secrets/6564)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The authors claim that their findings are generalizable to LLMs, but the experiments are conducted on small models (44M parameters). The authors should conduct experiments on larger models to support their claims. 2. The authors claim that their findings are generalizable to real-world data, but the experiments are conducted on synthetic data. The authors should conduct experiments  deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2502.19981"></a>
### The Lookahead Limitation: Why Multi-Operand Addition is Hard for LLMs

`arxiv:2502.19981` · Reasoning and the "physics" of language models · 2025-02-27

- final **-0.23** (conf 0.71, pct 22) · impact +0.63 · WATCH
- mean rating (1–10): **5.8** · accept votes **3/7** · percentile rank_avg 53.0 (100=best) · rank in year 47.0 (1=best)
- NAIPv2 `-2.475` · NAIP-v1 `0.728` · SciJudge `-0.304` · DGC-BERT `0.449`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `8.0` Accept · 7B Fast `6.0` Reject (S/P/C 2.5/2.75/2.5) · 14B Fast `4.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  The proposed hypothesis is somewhat trivial. The authors show that LLMs use a one-digit lookahead heuristic to solve addition, which is not surprising. This paper does not provide any new insights into the limitations of LLMs.  ### Questions  - Can the authors provide more insights into the limitations of LLMs? For example, what are the implications of this limitation for other tasks t deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2502.05171"></a>
### Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach

`arxiv:2502.05171` · Reasoning and the "physics" of language models · 2025-02-07

- final **+0.25** (conf 0.71, pct 66) · impact -0.31 · KEEP
- mean rating (1–10): **6.3** · accept votes **5/7** · percentile rank_avg 61.3 (100=best) · rank in year 30.0 (1=best)
- NAIPv2 `-1.399` · NAIP-v1 `0.460` · SciJudge `0.514` · DGC-BERT `0.918`
- CycleReviewer 8B `6.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.0` Reject (S/P/C 3.25/2.75/2.5) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [seeallochnaya/3895](https://t.me/seeallochnaya/3895), [gonzo_ML/5334](https://t.me/gonzo_ML/5334), [axisofordinary/7296](https://t.me/axisofordinary/7296), [buckwheat_thoughts/110](https://t.me/buckwheat_thoughts/110), [axisofordinary/6971](https://t.me/axisofordinary/6971)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper does not include a comparison with existing methods for scaling language models.  ### Questions  How does the proposed approach compare to existing methods for scaling language models?  ### Flag For Ethics Review  No ethics review needed.  ### Rating  6: marginally above the acceptance threshold  ### Confidence  4: You are confident in your assessment, but not absolutely cert deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2502.06807"></a>
### Competitive Programming with Large Reasoning Models

`arxiv:2502.06807` · Reasoning and the "physics" of language models · 2025-02-03

- final **-0.33** (conf 0.71, pct 17) · impact +0.55 · WATCH
- mean rating (1–10): **5.8** · accept votes **4/7** · percentile rank_avg 47.3 (100=best) · rank in year 62.0 (1=best)
- NAIPv2 `-0.521` · NAIP-v1 `0.472` · SciJudge `3.213` · DGC-BERT `0.503`
- CycleReviewer 8B `2.5` Reject · 70B `` 
- DeepReviewer 7B Std `3.2` Reject · 7B Fast `6.5` Reject (S/P/C 3.25/2.75/2.5) · 14B Fast `5.8` Accept
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/6978](https://t.me/axisofordinary/6978), [data_secrets/6133](https://t.me/data_secrets/6133), [seeallochnaya/2304](https://t.me/seeallochnaya/2304), [j_links/7875](https://t.me/j_links/7875)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper is not a research paper, but rather a report of the performance of OpenAI's o1, o1-ioi and o3 models on competitive programming tasks. The paper lacks a clear research question, methodology, and results section.  2. The paper does not provide any technical details on the models, including the architecture, training data, and training procedure.   3. The paper does not comp deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2502.00873"></a>
### Language Models Use Trigonometry to Do Addition

`arxiv:2502.00873` · Reasoning and the "physics" of language models · 2025-02-02

- final **+0.44** (conf 0.71, pct 86) · impact +0.95 · KEEP
- mean rating (1–10): **6.2** · accept votes **6/7** · percentile rank_avg 63.9 (100=best) · rank in year 19.0 (1=best)
- NAIPv2 `-0.740` · NAIP-v1 `0.506` · SciJudge `3.569` · DGC-BERT `0.164`
- CycleReviewer 8B `5.2` Accept · 70B `` 
- DeepReviewer 7B Std `8.0` Accept · 7B Fast `7.0` Accept (S/P/C 3.25/3.25/3.25) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper is not very novel. The authors show that numbers are represented as a helix in LLMs and that LLMs compute addition by manipulating this helix using the "Clock" algorithm. However, this has already been shown by previous works (e.g., Levy & Geva, 2024; Zhu et al., 2025).  ### Questions  1. How is the proposed method different from previous works (e.g., Levy & Geva, 2024; Zhu e deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2501.04519"></a>
### rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking

`arxiv:2501.04519` · Reasoning and the "physics" of language models · 2025-01-08

- final **+0.48** (conf 0.71, pct 90) · impact +1.39 · KEEP
- mean rating (1–10): **6.5** · accept votes **6/7** · percentile rank_avg 71.3 (100=best) · rank in year 7.0 (1=best)
- NAIPv2 `2.328` · NAIP-v1 `0.656` · SciJudge `3.417` · DGC-BERT `0.417`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.8` Accept · 7B Fast `7.0` Accept (S/P/C 3.0/3.25/3.25) · 14B Fast `6.2` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [axisofordinary/6880](https://t.me/axisofordinary/6880), [dealerAI/1054](https://t.me/dealerAI/1054), [data_secrets/5881](https://t.me/data_secrets/5881)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The proposed method requires a large amount of compute resources to train the models.  - The proposed method is not generalizable to other tasks.   I am willing to increase my score if the authors can address the above two concerns.  ### Questions  - The proposed method requires a large amount of compute resources to train the models. It is unclear how much compute resources are requ deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2412.14135"></a>
### Scaling of Search and Learning: A Roadmap to Reproduce o1 from Reinforcement Learning Perspective

`arxiv:2412.14135` · Reasoning and the "physics" of language models · 2024-12-18

- final **-0.80** (conf 0.71, pct 2) · impact -1.50 · DROP
- mean rating (1–10): **3.8** · accept votes **0/7** · percentile rank_avg 7.4 (100=best) · rank in year 47.0 (1=best)
- NAIPv2 `-3.502` · NAIP-v1 `0.258` · SciJudge `-3.088` · DGC-BERT `0.003`
- CycleReviewer 8B `1.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.2` Reject · 7B Fast `4.8` Reject (S/P/C 2.25/2.75/2.25) · 14B Fast `3.0` Reject
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `5.0` Reject
- Telegram: [AGI_and_RL/881](https://t.me/AGI_and_RL/881)
- Weaknesses: cyclereviewer-8b: Weaknesses  This paper is a survey paper about the four key components of the o1 model: policy initialization, reward design, search, and learning. The authors first introduce the background of reinforcement learning and its connection to LLM. Then, the authors introduce the four key components of the o1 model. The authors first introduce the policy initialization of the o1 model, which includes p deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2412.06769"></a>
### Training Large Language Models to Reason in a Continuous Latent Space

`arxiv:2412.06769` · Reasoning and the "physics" of language models · 2024-12-09

- final **+0.15** (conf 0.71, pct 57) · impact +0.19 · WATCH
- mean rating (1–10): **6.1** · accept votes **5/7** · percentile rank_avg 54.2 (100=best) · rank in year 16.0 (1=best)
- NAIPv2 `-1.824` · NAIP-v1 `0.554` · SciJudge `1.218` · DGC-BERT `0.750`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.2` Reject (S/P/C 2.5/3.0/2.75) · 14B Fast `6.2` Reject
- OpenReviewer `6.0` Accept (S/P/C 2.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/4622](https://t.me/gonzo_ML/4622), [gonzo_ML/4210](https://t.me/gonzo_ML/4210), [seeallochnaya/2541](https://t.me/seeallochnaya/2541), [gonzo_ML/3567](https://t.me/gonzo_ML/3567), [gonzo_ML/3569](https://t.me/gonzo_ML/3569), [buckwheat_thoughts/110](https://t.me/buckwheat_thoughts/110), [abstractDL/311](https://t.me/abstractDL/311), [axisofordinary/6838](https://t.me/axisofordinary/6838)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper does not provide a thorough analysis of the limitations of the proposed method. For example, it is unclear how Coconut would perform on tasks that require more complex reasoning, such as multi-hop reasoning or reasoning over long chains of reasoning. 2. The paper does not provide a detailed discussion of the computational efficiency of Coconut compared to CoT. While the pa deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2410.21272"></a>
### Arithmetic Without Algorithms: Language Models Solve Math With a Bag of Heuristics

`arxiv:2410.21272` · Reasoning and the "physics" of language models · 2024-10-28

- final **+0.68** (conf 0.71, pct 98) · impact +0.50 · KEEP
- mean rating (1–10): **6.6** · accept votes **6/7** · percentile rank_avg 66.2 (100=best) · rank in year 2.0 (1=best)
- NAIPv2 `-0.077` · NAIP-v1 `0.618` · SciJudge `1.307` · DGC-BERT `0.291`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.0` Accept (S/P/C 3.0/3.25/3.0) · 14B Fast `8.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [j_links/7782](https://t.me/j_links/7782)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper does not discuss how the heuristics are learned during training. The paper only shows that the heuristics are present in the final model, but it does not show how they are learned. It would be interesting to see how the heuristics are learned during training and how they change over time.  ### Questions  How are the heuristics learned during training? How do they change over  cyclereviewer-8b.seed1: Weaknesses  - The paper does not provide a detailed expla

<a id="arxiv-2305.13673"></a>
### Physics of Language Models: Part 1, Learning Hierarchical Language Structures

`arxiv:2305.13673` · Reasoning and the "physics" of language models · 2023-05-23

- final **+0.54** (conf 0.71, pct 93) · impact -0.21 · KEEP
- mean rating (1–10): **6.1** · accept votes **6/7** · percentile rank_avg 64.3 (100=best) · rank in year 6.0 (1=best)
- NAIPv2 `-0.169` · NAIP-v1 `0.496` · SciJudge `1.199` · DGC-BERT `0.867`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `8.0` Accept · 7B Fast `6.7` Accept (S/P/C 3.0/3.0/2.67) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [lovedeathtransformers/8152](https://t.me/lovedeathtransformers/8152)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper focuses on CFGs, which are a limited class of grammars. It would be interesting to see how the proposed approach generalizes to other types of grammars, such as context-sensitive grammars.  The paper does not provide a comprehensive evaluation of the proposed approach. It would be interesting to see how the approach performs on a wider range of tasks and datasets.  The paper  deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2407.20311"></a>
### Physics of Language Models: Part 2.1, Grade-School Math and the Hidden Reasoning Process

`arxiv:2407.20311` · Reasoning and the "physics" of language models · 2024-07-29

- final **+0.36** (conf 0.71, pct 79) · impact +0.30 · KEEP
- mean rating (1–10): **6.4** · accept votes **5/7** · percentile rank_avg 58.5 (100=best) · rank in year 9.0 (1=best)
- NAIPv2 `-2.086` · NAIP-v1 `0.498` · SciJudge `2.144` · DGC-BERT `0.745`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.8` Reject · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/2.5) · 14B Fast `7.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/3.0) · SEA-E `6.0` Accept
- Telegram: [lovedeathtransformers/8152](https://t.me/lovedeathtransformers/8152)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper focuses on a very specific domain (grade-school math) and it is unclear how the findings can be generalized to other domains. - The authors only consider a single model architecture (GPT-2) and it is unclear how the findings can be generalized to other model architectures. - The probing task is not well motivated and the authors do not compare their probing task to other ex deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2309.14316"></a>
### Physics of Language Models: Part 3.1, Knowledge Storage and Extraction

`arxiv:2309.14316` · Reasoning and the "physics" of language models · 2023-09-25

- final **+0.24** (conf 0.71, pct 65) · impact -0.85 · KEEP
- mean rating (1–10): **6.1** · accept votes **4/7** · percentile rank_avg 44.0 (100=best) · rank in year 31.0 (1=best)
- NAIPv2 `-1.495` · NAIP-v1 `0.444` · SciJudge `-0.565` · DGC-BERT `0.152`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `5.2` Reject · 7B Fast `6.5` Accept (S/P/C 3.0/3.0/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [rybolos_channel/1195](https://t.me/rybolos_channel/1195), [lovedeathtransformers/8152](https://t.me/lovedeathtransformers/8152)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper lacks novelty. The authors' proposed approach to understanding how LLMs store and extract knowledge from pretraining data has been explored in previous studies. The paper does not provide any new insights or contributions to the field.  ### Questions  N/A  ### Flag For Ethics Review  No ethics review needed.  ### Rating  3: reject, not good enough  ### Confidence  4: You are  deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2309.14402"></a>
### Physics of Language Models: Part 3.2, Knowledge Manipulation

`arxiv:2309.14402` · Reasoning and the "physics" of language models · 2023-09-25

- final **+0.27** (conf 0.68, pct 71) · impact -0.39 · KEEP
- mean rating (1–10): **7.0** · accept votes **3/6** · percentile rank_avg 58.4 (100=best) · rank in year 10.0 (1=best)
- NAIPv2 `-1.719` · NAIP-v1 `0.454` · SciJudge `1.264` · DGC-BERT `0.177`
- CycleReviewer 8B `6.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast ``  (S/P/C None/None/None) · 14B Fast `7.0` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [lovedeathtransformers/8152](https://t.me/lovedeathtransformers/8152)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper only focuses on a specific type of knowledge manipulation tasks, i.e., the tasks that can be solved by simple logical reasoning. It would be interesting to see if the findings hold for more complex knowledge manipulation tasks. 2. The paper only considers a limited number of language models, i.e., GPT-2 and LLaMA. It would be interesting to see if the findings hold for oth deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2404.05405"></a>
### Physics of Language Models: Part 3.3, Knowledge Capacity Scaling Laws

`arxiv:2404.05405` · Reasoning and the "physics" of language models · 2024-04-08

- final **+0.43** (conf 0.71, pct 86) · impact +1.02 · KEEP
- mean rating (1–10): **6.6** · accept votes **5/7** · percentile rank_avg 63.1 (100=best) · rank in year 3.0 (1=best)
- NAIPv2 `-0.638` · NAIP-v1 `0.514` · SciJudge `3.621` · DGC-BERT `0.237`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `5.7` Accept (S/P/C 2.67/2.67/2.67) · 14B Fast `7.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/4.0) · SEA-E `7.0` Accept
- Telegram: [lovedeathtransformers/7555](https://t.me/lovedeathtransformers/7555), [seeallochnaya/1268](https://t.me/seeallochnaya/1268), [lovedeathtransformers/8152](https://t.me/lovedeathtransformers/8152)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper focuses on a synthetic dataset and doesn't study the knowledge storage capacity of real-world language models. The results are not generalizable to real-world models. The paper also doesn't discuss the limitations of the proposed method.  ### Questions  - What are the limitations of the proposed method? How can it be improved? - Can the proposed method be applied to real-worl deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2407.15017"></a>
### Knowledge Mechanisms in Large Language Models: A Survey and Perspective

`arxiv:2407.15017` · Reasoning and the "physics" of language models · 2024-07-22

- final **-0.32** (conf 0.71, pct 19) · impact +0.68 · WATCH
- mean rating (1–10): **5.8** · accept votes **3/7** · percentile rank_avg 39.2 (100=best) · rank in year 34.0 (1=best)
- NAIPv2 `-2.588` · NAIP-v1 `0.644` · SciJudge `1.432` · DGC-BERT `0.021`
- CycleReviewer 8B `5.8` Reject · 70B `` 
- DeepReviewer 7B Std `4.2` Reject · 7B Fast `5.8` Reject (S/P/C 2.5/2.75/2.5) · 14B Fast `5.8` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [AGI_and_RL/844](https://t.me/AGI_and_RL/844)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper does not provide any new insights or contributions to the field of LLMs.  ### Questions  What are the potential applications of knowledge editing and representation editing in LLMs?  ### Flag For Ethics Review  No ethics review needed.  ### Rating  5: marginally below the acceptance threshold  ### Confidence  2: You are willing to defend your assessment, but it is quite likel deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="doi-10.1038-s41586-024-07522-w"></a>
### Language is primarily a tool for communication rather than thought

`doi:10.1038/s41586-024-07522-w` · Reasoning and the "physics" of language models · 2024-06-19

- final **-0.33** (conf 0.62, pct 18) · impact -2.64 · DROP
- mean rating (1–10): **5.9** · accept votes **4/5** · percentile rank_avg 27.5 (100=best) · rank in year 41.0 (1=best)
- NAIPv2 `-5.289` · NAIP-v1 `0.204` · SciJudge `-8.846` · DGC-BERT `0.060`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std ``  · 7B Fast ``  (S/P/C None/None/None) · 14B Fast `5.8` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/2797](https://t.me/gonzo_ML/2797)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper does not provide a detailed analysis of the relationship between language and thought, and it does not fully explore the implications of the authors' argument for our understanding of human cognition and culture.  ### Questions  1. What are the implications of the authors' argument for our understanding of the relationship between language and thought? 2. How does language in deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2406.11813"></a>
### How Do Large Language Models Acquire Factual Knowledge During Pretraining?

`arxiv:2406.11813` · Reasoning and the "physics" of language models · 2024-06-17

- final **+0.11** (conf 0.71, pct 53) · impact -0.16 · WATCH
- mean rating (1–10): **6.0** · accept votes **5/7** · percentile rank_avg 46.7 (100=best) · rank in year 25.0 (1=best)
- NAIPv2 `-1.204` · NAIP-v1 `0.502` · SciJudge `0.072` · DGC-BERT `0.244`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.2` Reject · 7B Fast `6.2` Accept (S/P/C 2.75/3.25/2.75) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/6439](https://t.me/axisofordinary/6439)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper has some limitations. The authors only study the acquisition of factual knowledge in LLMs, and do not study other types of knowledge, such as common sense or world knowledge. The authors also only study the acquisition of knowledge in LLMs during pretraining, and do not study the acquisition of knowledge during fine-tuning or inference. The authors also only study the acquisi deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2406.11741"></a>
### Transcendence: Generative Models Can Outperform The Experts That Train Them

`arxiv:2406.11741` · Reasoning and the "physics" of language models · 2024-06-17

- final **+0.06** (conf 0.71, pct 47) · impact +0.67 · WATCH
- mean rating (1–10): **6.0** · accept votes **4/7** · percentile rank_avg 54.1 (100=best) · rank in year 17.0 (1=best)
- NAIPv2 `-1.136` · NAIP-v1 `0.593` · SciJudge `2.147` · DGC-BERT `0.654`
- CycleReviewer 8B `5.8` Reject · 70B `` 
- DeepReviewer 7B Std `5.8` Reject · 7B Fast `5.8` Accept (S/P/C 2.75/2.75/2.5) · 14B Fast `5.2` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `7.0` Accept
- Telegram: [axisofordinary/6439](https://t.me/axisofordinary/6439), [seeallochnaya/1559](https://t.me/seeallochnaya/1559)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper lacks a clear motivation for studying the phenomenon of "transcendence". While the paper provides a theoretical analysis of the conditions under which transcendence can occur, it is not clear why this phenomenon is important or interesting. The paper also lacks a clear discussion of the limitations of the theoretical results, and how they relate to the empirical results. Addi cyclereviewer-8b.seed1: Weaknesses  - The paper only studies the phenomenon of tr

<a id="arxiv-2406.03689"></a>
### Evaluating the World Model Implicit in a Generative Model

`arxiv:2406.03689` · Reasoning and the "physics" of language models · 2024-06-06

- final **+0.20** (conf 0.71, pct 62) · impact -0.48 · WATCH
- mean rating (1–10): **6.5** · accept votes **4/7** · percentile rank_avg 55.1 (100=best) · rank in year 14.0 (1=best)
- NAIPv2 `-1.565` · NAIP-v1 `0.471` · SciJudge `-1.244` · DGC-BERT `0.861`
- CycleReviewer 8B `5.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Reject · 7B Fast `5.2` Reject (S/P/C 2.5/2.75/2.5) · 14B Fast `6.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/3.0) · SEA-E `7.0` Accept
- Telegram: [boris_again/2625](https://t.me/boris_again/2625), [axisofordinary/6441](https://t.me/axisofordinary/6441), [j_links/7562](https://t.me/j_links/7562)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper focuses on deterministic finite automata. However, in practice, the world is not deterministic. It would be interesting to see how the proposed metrics can be extended to handle stochasticity. 2. The paper only considers next-token prediction as the generative model. It would be interesting to see how the proposed metrics can be extended to other generative models, such as deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2406.03445"></a>
### Pre-trained Large Language Models Use Fourier Features to Compute Addition

`arxiv:2406.03445` · Reasoning and the "physics" of language models · 2024-06-05

- final **+0.43** (conf 0.71, pct 86) · impact +0.88 · KEEP
- mean rating (1–10): **5.8** · accept votes **6/7** · percentile rank_avg 62.2 (100=best) · rank in year 5.0 (1=best)
- NAIPv2 `-1.313` · NAIP-v1 `0.676` · SciJudge `1.613` · DGC-BERT `0.871`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `7.0` Accept · 7B Fast `7.5` Accept (S/P/C 3.0/3.25/3.25) · 14B Fast `5.8` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper's contribution is not very significant. The authors only analyzed a single task (addition) and a single model (GPT-2-XL) and did not generalize to other models or tasks. 2. The paper's findings are somewhat limited to the specific model and task analyzed. It would be more impactful if the authors could generalize their findings to other models and tasks. 3. The paper does  deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2405.15071"></a>
### Grokked Transformers are Implicit Reasoners: A Mechanistic Journey to the Edge of Generalization

`arxiv:2405.15071` · Reasoning and the "physics" of language models · 2024-05-23

- final **+0.51** (conf 0.71, pct 92) · impact +1.04 · KEEP
- mean rating (1–10): **6.0** · accept votes **6/7** · percentile rank_avg 62.0 (100=best) · rank in year 6.0 (1=best)
- NAIPv2 `-0.824` · NAIP-v1 `0.652` · SciJudge `3.092` · DGC-BERT `0.698`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `7.0` Accept · 7B Fast `7.3` Accept (S/P/C 3.0/3.33/3.0) · 14B Fast `5.8` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [chillhousetech/773](https://t.me/chillhousetech/773), [lovedeathtransformers/7720](https://t.me/lovedeathtransformers/7720), [seeallochnaya/1473](https://t.me/seeallochnaya/1473), [axisofordinary/6349](https://t.me/axisofordinary/6349)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper is limited in its scope and does not fully explore the implications of its findings. The paper only studies two tasks, composition and comparison, and does not consider other types of reasoning, such as logical reasoning. The paper also does not consider other types of models, such as recurrent neural networks or graph neural networks, and only studies transformers. The paper deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2405.14838"></a>
### From Explicit CoT to Implicit CoT: Learning to Internalize CoT Step by Step

`arxiv:2405.14838` · Reasoning and the "physics" of language models · 2024-05-23

- final **-0.14** (conf 0.71, pct 28) · impact +0.04 · WATCH
- mean rating (1–10): **5.6** · accept votes **4/7** · percentile rank_avg 42.4 (100=best) · rank in year 27.0 (1=best)
- NAIPv2 `-2.850` · NAIP-v1 `0.458` · SciJudge `1.895` · DGC-BERT `0.909`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `6.5` Accept (S/P/C 2.75/3.25/2.75) · 14B Fast `5.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/3583](https://t.me/gonzo_ML/3583), [gonzo_ML/3568](https://t.me/gonzo_ML/3568), [axisofordinary/6807](https://t.me/axisofordinary/6807), [axisofordinary/6481](https://t.me/axisofordinary/6481), [axisofordinary/6364](https://t.me/axisofordinary/6364)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper lacks novelty. The proposed method is similar to knowledge distillation, which transfers the knowledge from a teacher model to a student model. The difference is that the proposed method removes the intermediate steps and finetunes the model. However, the finetuning process is similar to knowledge distillation. 2. The proposed method is not evaluated on a wide range of tas deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="doi-10.1038-d41586-024-01413-w"></a>
### Why mathematics is set to be revolutionized by AI

`doi:10.1038/d41586-024-01413-w` · Reasoning and the "physics" of language models · 2024-05-14

- final **-0.45** (conf 0.53, pct 10) · impact -1.25 · DROP · partial fulltext
- mean rating (1–10): **5.2** · accept votes **3/5** · percentile rank_avg 21.9 (100=best) · rank in year 43.0 (1=best)
- NAIPv2 `-4.922` · NAIP-v1 `0.454` · SciJudge `-5.475` · DGC-BERT `0.036`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std ``  · 7B Fast ``  (S/P/C None/None/None) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/6315](https://t.me/axisofordinary/6315)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper is not well written. The idea of generating mathematical conjectures using machine learning is interesting, but the paper does not provide enough detail on how the method works and how it is implemented. The paper also does not provide enough evidence that the generated conjectures are actually true or useful.  ### Questions  I have the following questions regarding the paper deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2402.01817"></a>
### LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks

`arxiv:2402.01817` · Reasoning and the "physics" of language models · 2024-02-02

- final **-0.31** (conf 0.71, pct 19) · impact -0.17 · DROP
- mean rating (1–10): **6.0** · accept votes **2/7** · percentile rank_avg 34.5 (100=best) · rank in year 39.0 (1=best)
- NAIPv2 `-2.639` · NAIP-v1 `0.513` · SciJudge `-0.267` · DGC-BERT `0.004`
- CycleReviewer 8B `3.5` Reject · 70B `` 
- DeepReviewer 7B Std `4.2` Reject · 7B Fast `5.5` Reject (S/P/C 2.75/2.5/2.5) · 14B Fast `5.8` Reject
- OpenReviewer `8.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [data_secrets/5225](https://t.me/data_secrets/5225), [tech_priestess/1697](https://t.me/tech_priestess/1697)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper does not provide sufficient evidence to support its claims about the limitations of LLMs in planning and reasoning tasks. The paper relies on previous studies to support its claims, but does not provide any new empirical evidence. The paper also does not provide a clear description of the LLM-Modulo framework, and how it differs from existing approaches.  ### Questions  The p deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2312.13558"></a>
### The Truth is in There: Improving Reasoning in Language Models with Layer-Selective Rank Reduction

`arxiv:2312.13558` · Reasoning and the "physics" of language models · 2023-12-21

- final **+0.02** (conf 0.71, pct 41) · impact -0.87 · WATCH
- mean rating (1–10): **5.8** · accept votes **4/7** · percentile rank_avg 42.9 (100=best) · rank in year 32.0 (1=best)
- NAIPv2 `-1.128` · NAIP-v1 `0.379` · SciJudge `0.676` · DGC-BERT `0.923`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `4.8` Reject · 7B Fast `5.5` Reject (S/P/C 2.5/2.75/2.25) · 14B Fast `6.2` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [tech_priestess/1311](https://t.me/tech_priestess/1311), [data_secrets/3301](https://t.me/data_secrets/3301), [axisofordinary/5886](https://t.me/axisofordinary/5886), [j_links/7306](https://t.me/j_links/7306)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper lacks a clear explanation of the underlying mechanism of LASER and how it improves the performance of LLMs. While the paper provides some insights into the relationship between the model's training data and the samples that benefit from LASER, it does not provide a comprehensive explanation of how LASER works. 2. The paper does not provide a thorough evaluation of the robu deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="openreview-hcQfTsVnBo"></a>
### Grokking Group Multiplication with Cosets

`openreview:hcQfTsVnBo` · Reasoning and the "physics" of language models · unknown

- final **+0.47** (conf 0.71, pct 89) · impact -1.56 · KEEP
- mean rating (1–10): **6.5** · accept votes **5/7** · percentile rank_avg 50.2 (100=best) · rank in year 2.0 (1=best)
- NAIPv2 `-3.244` · NAIP-v1 `0.371` · SciJudge `-6.980` · DGC-BERT `0.035`
- CycleReviewer 8B `6.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.8` Accept · 7B Fast `7.0` Accept (S/P/C 3.25/3.0/3.0) · 14B Fast `6.8` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [axisofordinary/6435](https://t.me/axisofordinary/6435)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper is more of a case study and I am not sure if it is ready for ICLR. The paper should be expanded to include more details about the experiments, the experimental setup, the data, the models, etc.  ### Questions  What is the experimental setup? What is the data? What are the models? What are the results? How do the results compare to other models?  ### Flag For Ethics Review  No deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2309.12288"></a>
### The Reversal Curse: LLMs trained on "A is B" fail to learn "B is A"

`arxiv:2309.12288` · Reasoning and the "physics" of language models · 2023-09-21

- final **+0.24** (conf 0.71, pct 65) · impact +0.70 · KEEP
- mean rating (1–10): **5.7** · accept votes **4/7** · percentile rank_avg 55.3 (100=best) · rank in year 14.0 (1=best)
- NAIPv2 `1.487` · NAIP-v1 `0.676` · SciJudge `1.757` · DGC-BERT `0.254`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.2` Reject · 7B Fast `6.3` Accept (S/P/C 2.67/2.67/2.67) · 14B Fast `5.8` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/4618](https://t.me/gonzo_ML/4618), [abstractDL/245](https://t.me/abstractDL/245), [boris_again/1973](https://t.me/boris_again/1973)
- Weaknesses: cyclereviewer-8b: Weaknesses  The main weakness of this paper is that the experiments are not convincing. The authors only use a small dataset of 30 facts about celebrities. The authors also only perform finetuning on this dataset. It is unclear whether the Reversal Curse still exists in pretraining. The authors also only use GPT-3 and Llama-1 models. It is unclear whether the Reversal Curse exists in other models. deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2304.15004"></a>
### Are Emergent Abilities of Large Language Models a Mirage?

`arxiv:2304.15004` · Reasoning and the "physics" of language models · 2023-04-28

- final **+0.49** (conf 0.71, pct 91) · impact +0.46 · KEEP
- mean rating (1–10): **6.2** · accept votes **5/7** · percentile rank_avg 63.4 (100=best) · rank in year 7.0 (1=best)
- NAIPv2 `0.762` · NAIP-v1 `0.551` · SciJudge `2.948` · DGC-BERT `0.254`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.2` Accept (S/P/C 2.75/3.0/3.0) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [Victor_Osyka/511](https://t.me/Victor_Osyka/511), [rybolos_channel/995](https://t.me/rybolos_channel/995), [chillhousetech/524](https://t.me/chillhousetech/524), [lovedeathtransformers/6780](https://t.me/lovedeathtransformers/6780), [abstractDL/215](https://t.me/abstractDL/215), [emptyset_of_ideas/429](https://t.me/emptyset_of_ideas/429)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper focuses primarily on LLMs, but the authors do not provide a clear explanation of why emergent abilities are not a fundamental property of other types of models, such as computer vision models. - The paper does not provide a clear explanation of how the choice of metric affects the performance of models on different tasks. - The paper does not provide a clear explanation of  deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2302.00923"></a>
### Multimodal Chain-of-Thought Reasoning in Language Models

`arxiv:2302.00923` · Reasoning and the "physics" of language models · 2023-02-02

- final **+0.03** (conf 0.71, pct 41) · impact +0.72 · WATCH
- mean rating (1–10): **6.2** · accept votes **5/7** · percentile rank_avg 57.1 (100=best) · rank in year 11.0 (1=best)
- NAIPv2 `-0.418` · NAIP-v1 `0.730` · SciJudge `0.912` · DGC-BERT `0.793`
- CycleReviewer 8B `5.8` Accept · 70B `` 
- DeepReviewer 7B Std `5.2` Reject · 7B Fast `5.7` Accept (S/P/C 2.67/3.0/2.67) · 14B Fast `5.8` Reject
- OpenReviewer `8.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/4464](https://t.me/axisofordinary/4464), [axisofordinary/4323](https://t.me/axisofordinary/4323), [j_links/6440](https://t.me/j_links/6440)
- Weaknesses: cyclereviewer-8b: Weaknesses  The method is not novel. The idea of using two stages for CoT reasoning has been proposed in previous works, such as (1). The method of using a single-head attention network to correlate text tokens with image patches has also been proposed in previous works, such as (2). The method of using a gated fusion mechanism to fuse language and vision representations has also been proposed in  deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2301.06627"></a>
### Dissociating language and thought in large language models

`arxiv:2301.06627` · Reasoning and the "physics" of language models · 2023-01-16

- final **+0.05** (conf 0.71, pct 45) · impact -0.39 · WATCH
- mean rating (1–10): **6.2** · accept votes **3/7** · percentile rank_avg 48.1 (100=best) · rank in year 27.0 (1=best)
- NAIPv2 `-2.279` · NAIP-v1 `0.436` · SciJudge `1.583` · DGC-BERT `0.311`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.2` Reject · 7B Fast `6.5` Reject (S/P/C 2.75/2.75/2.75) · 14B Fast `6.8` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [axisofordinary/4244](https://t.me/axisofordinary/4244)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper lacks a clear and concise abstract that summarizes the main contributions and findings of the paper. 2. The paper lacks a clear and concise introduction that provides background information and sets the stage for the rest of the paper. 3. The paper lacks a clear and concise conclusion that summarizes the main findings and contributions of the paper. 4. The paper lacks a cl cyclereviewer-8b.seed1: Weaknesses  - The paper's evaluation of LLMs on functiona

<a id="arxiv-2301.05217"></a>
### Progress measures for grokking via mechanistic interpretability

`arxiv:2301.05217` · Reasoning and the "physics" of language models · 2023-01-12

- final **+0.72** (conf 0.71, pct 100) · impact -0.01 · KEEP
- mean rating (1–10): **6.6** · accept votes **7/7** · percentile rank_avg 67.4 (100=best) · rank in year 3.0 (1=best)
- NAIPv2 `-0.686` · NAIP-v1 `0.491` · SciJudge `1.824` · DGC-BERT `0.559`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `8.0` Accept · 7B Fast `8.0` Accept (S/P/C 3.5/3.5/3.5) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [j_links/6406](https://t.me/j_links/6406)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper focuses on a very specific task and model architecture, which limits the generalizability of the findings. It is not clear how the results would extend to other tasks or model architectures. - The paper does not provide a clear explanation for why the model uses the Fourier multiplication algorithm to solve the modular addition task. It would be helpful to have a more in-de deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2212.09196"></a>
### Emergent Analogical Reasoning in Large Language Models

`arxiv:2212.09196` · Reasoning and the "physics" of language models · 2022-12-19

- final **+0.13** (conf 0.71, pct 55) · impact +0.96 · WATCH
- mean rating (1–10): **6.3** · accept votes **5/7** · percentile rank_avg 56.2 (100=best) · rank in year 7.0 (1=best)
- NAIPv2 `-1.596` · NAIP-v1 `0.756` · SciJudge `2.115` · DGC-BERT `0.046`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `5.2` Reject (S/P/C 2.5/3.0/2.25) · 14B Fast `6.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/4.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/4214](https://t.me/axisofordinary/4214), [axisofordinary/4140](https://t.me/axisofordinary/4140), [dtulinov/501](https://t.me/dtulinov/501)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper would benefit from a more detailed discussion of the limitations of the study. For example, the authors note that GPT-3 was not able to use analogies to solve a transfer problem involving construction and use of simple tools. However, it is not clear why this is the case, or whether it is a limitation of GPT-3 or simply a limitation of the particular task. Additionally, the a deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="openreview-wUU-7XTL5XO"></a>
### Large Language Models Still Can't Plan / PlanBench (Kambhampati)

`openreview:wUU-7XTL5XO` · Reasoning and the "physics" of language models · unknown

- final **-0.39** (conf 0.71, pct 14) · impact +0.29 · DROP
- mean rating (1–10): **5.4** · accept votes **2/7** · percentile rank_avg 33.8 (100=best) · rank in year 8.0 (1=best)
- NAIPv2 `-1.282` · NAIP-v1 `0.555` · SciJudge `1.544` · DGC-BERT `0.014`
- CycleReviewer 8B `5.2` Reject · 70B `` 
- DeepReviewer 7B Std `3.0` Reject · 7B Fast `4.2` Reject (S/P/C 2.5/2.25/2.25) · 14B Fast `5.7` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [data_secrets/5225](https://t.me/data_secrets/5225)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper only evaluates the benchmark on GPT-3, Instruct-GPT3 and BLOOM, and does not evaluate other popular LLMs such as Llama-2, Vicuna, etc. - The paper only evaluates the benchmark on simple planning tasks, and does not evaluate the benchmark on more complex planning tasks. - The paper does not provide any analysis of why the LLMs perform poorly on the benchmark. - The paper doe deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2203.11171"></a>
### Self-Consistency Improves Chain of Thought Reasoning in Language Models

`arxiv:2203.11171` · Reasoning and the "physics" of language models · 2022-03-21

- final **+0.29** (conf 0.71, pct 73) · impact +1.58 · KEEP
- mean rating (1–10): **5.7** · accept votes **7/7** · percentile rank_avg 60.0 (100=best) · rank in year 5.0 (1=best)
- NAIPv2 `-2.383` · NAIP-v1 `0.759` · SciJudge `3.638` · DGC-BERT `0.917`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.0` Accept (S/P/C 3.0/3.25/2.75) · 14B Fast `4.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/7585](https://t.me/axisofordinary/7585), [seeallochnaya/1765](https://t.me/seeallochnaya/1765), [gonzo_ML/1885](https://t.me/gonzo_ML/1885), [rybolos_channel/700](https://t.me/rybolos_channel/700), [axisofordinary/3588](https://t.me/axisofordinary/3588), [axisofordinary/2249](https://t.me/axisofordinary/2249)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper could benefit from a more thorough discussion of the limitations of the proposed method. For example, the authors mention that self-consistency incurs more computation cost, but it would be helpful to provide more details on how much more expensive it is compared to other methods. Additionally, the authors mention that self-consistency can sometimes generate incorrect or nons deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2608.05136"></a>
### The Loss Does Not See the Basis, but Adam Does

`arxiv:2608.05136` · Data, training, optimization · 2026-08-05

- final **+0.41** (conf 0.71, pct 84) · impact -0.62 · KEEP
- mean rating (1–10): **6.4** · accept votes **6/7** · percentile rank_avg 61.8 (100=best) · rank in year 25.0 (1=best)
- NAIPv2 `1.129` · NAIP-v1 `0.627` · SciJudge `-3.796` · DGC-BERT `0.208`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.5` Accept (S/P/C 2.75/3.0/2.75) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/5956](https://t.me/gonzo_ML/5956)
- Weaknesses: cyclereviewer-8b: Weaknesses  The main weakness of the paper is that the authors do not provide a clear explanation of why the low-rank bias is present in some non-adaptive methods such as Shampoo and Muon. The authors only provide a partial explanation of why the low-rank bias is present in these methods.  ### Questions  1. Why is the low-rank bias not present in Adam and other adaptive methods? Is it because thes deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2607.27372"></a>
### Explorative Modeling: Unlocking a Third Pretraining Axis and End-to-End Generation

`arxiv:2607.27372` · Data, training, optimization · 2026-07-29

- final **+0.37** (conf 0.71, pct 80) · impact +1.41 · KEEP
- mean rating (1–10): **6.2** · accept votes **7/7** · percentile rank_avg 71.1 (100=best) · rank in year 7.0 (1=best)
- NAIPv2 `0.640` · NAIP-v1 `0.771` · SciJudge `2.110` · DGC-BERT `0.888`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/2.67) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/5858](https://t.me/gonzo_ML/5858)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper does not provide a detailed explanation of the mathematical formulation of the XM approach. While the authors provide an intuitive explanation of the approach, a more formal mathematical description would be helpful for readers who want to understand the underlying principles of the method. - The paper does not provide a detailed comparison of XM with other existing generat deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2601.21343"></a>
### Self-Improving Pretraining: using post-trained models to pretrain better models

`arxiv:2601.21343` · Data, training, optimization · 2026-01-29

- final **-0.40** (conf 0.71, pct 13) · impact -0.35 · DROP
- mean rating (1–10): **5.8** · accept votes **3/7** · percentile rank_avg 39.1 (100=best) · rank in year 64.0 (1=best)
- NAIPv2 `-2.145` · NAIP-v1 `0.484` · SciJudge `0.425` · DGC-BERT `0.335`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.2` Reject · 7B Fast `5.5` Reject (S/P/C 2.5/2.5/2.5) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/8485](https://t.me/axisofordinary/8485), [gonzo_ML/4691](https://t.me/gonzo_ML/4691)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper lacks a clear comparison with existing methods. The authors should provide a more comprehensive comparison with other approaches to improve the training of LLMs, such as chain-of-thought and reasoning-based pretraining.  2. The paper does not provide a detailed analysis of the limitations of the proposed approach. The authors should discuss the potential limitations of the cyclereviewer-8b.seed1: Weaknesses  1. The paper lacks a detailed discussion of t

<a id="arxiv-2512.24695"></a>
### Nested Learning: The Illusion of Deep Learning Architectures

`arxiv:2512.24695` · Data, training, optimization · 2025-12-31

- final **-0.75** (conf 0.68, pct 3) · impact -2.20 · DROP
- mean rating (1–10): **4.0** · accept votes **0/6** · percentile rank_avg 11.7 (100=best) · rank in year 80.0 (1=best)
- NAIPv2 `-2.021` · NAIP-v1 `0.319` · SciJudge `-7.195` · DGC-BERT `0.206`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std ``  · 7B Fast `5.0` Reject (S/P/C 2.5/2.5/2.5) · 14B Fast `4.2` Reject
- OpenReviewer `5.0` Reject (S/P/C 2.0/2.0/2.0) · SEA-E `3.0` Reject
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper's presentation is not clear enough, and the motivation for the Nested Learning paradigm is not well explained. The authors should provide more clarity on how the Nested Learning paradigm addresses the limitations of current machine learning models and why it is a necessary step forward. Additionally, the paper's organization and structure should be improved to make it easier  cyclereviewer-8b.seed1: Weaknesses  The paper is very hard to follow and understa

<a id="arxiv-2510.05491"></a>
### NorMuon: Making Muon more efficient and scalable

`arxiv:2510.05491` · Data, training, optimization · 2025-10-07

- final **+0.10** (conf 0.71, pct 52) · impact -0.55 · WATCH
- mean rating (1–10): **5.9** · accept votes **6/7** · percentile rank_avg 47.6 (100=best) · rank in year 60.0 (1=best)
- NAIPv2 `-1.236` · NAIP-v1 `0.512` · SciJudge `-1.707` · DGC-BERT `0.663`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.2` Accept · 7B Fast `7.0` Accept (S/P/C 3.25/3.25/3.0) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper lacks novelty. The proposed method is a combination of Muon and Adam, which has been done in previous works (1, 2). The authors should compare NorMuon with these works and explain the differences and advantages of their method.  2. The paper does not provide a theoretical analysis of the proposed method. The authors should provide a theoretical analysis of the convergence  cyclereviewer-8b.seed1: Weaknesses  The paper's novelty is limited, as it builds 

<a id="arxiv-2508.11408"></a>
### On-Policy RL Meets Off-Policy Experts: Harmonizing Supervised Fine-Tuning and Reinforcement Learning via Dynamic Weighting

`arxiv:2508.11408` · Data, training, optimization · 2025-08-15

- final **+0.22** (conf 0.71, pct 63) · impact -0.19 · KEEP
- mean rating (1–10): **6.1** · accept votes **5/7** · percentile rank_avg 53.8 (100=best) · rank in year 45.0 (1=best)
- NAIPv2 `1.382` · NAIP-v1 `0.602` · SciJudge `-1.390` · DGC-BERT `0.046`
- CycleReviewer 8B `5.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/2.5) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [abstractDL/345](https://t.me/abstractDL/345)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper lacks a detailed discussion on the potential limitations of the proposed approach. For example, how does the proposed method perform when dealing with large-scale datasets or complex tasks? Are there any potential trade-offs between the performance improvement and computational efficiency?  2. The paper does not provide a clear comparison with existing methods in the liter deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2507.12856"></a>
### Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved)

`arxiv:2507.12856` · Data, training, optimization · 2025-07-17

- final **-0.32** (conf 0.71, pct 18) · impact -2.11 · DROP
- mean rating (1–10): **5.8** · accept votes **3/7** · percentile rank_avg 35.6 (100=best) · rank in year 71.0 (1=best)
- NAIPv2 `-3.164` · NAIP-v1 `0.229` · SciJudge `-4.049` · DGC-BERT `0.201`
- CycleReviewer 8B `5.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `5.8` Reject (S/P/C 2.5/2.75/2.25) · 14B Fast `6.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [abstractDL/345](https://t.me/abstractDL/345)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The novelty of the paper is limited. The connection between SFT and RL is not new. The proposed method is a simple modification of SFT. 2. The experiments are not comprehensive. The authors only evaluate the proposed method on two tasks, one for large language models and one for continuous control tasks. More experiments on different tasks are needed to demonstrate the effectiveness deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2506.08007"></a>
### Reinforcement Pre-Training

`arxiv:2506.08007` · Data, training, optimization · 2025-06-09

- final **-0.51** (conf 0.71, pct 9) · impact -1.23 · DROP
- mean rating (1–10): **5.5** · accept votes **3/7** · percentile rank_avg 31.9 (100=best) · rank in year 75.0 (1=best)
- NAIPv2 `-2.857` · NAIP-v1 `0.424` · SciJudge `-3.298` · DGC-BERT `0.913`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `3.0` Reject · 7B Fast `6.0` Reject (S/P/C 2.67/2.67/2.67) · 14B Fast `5.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [dealerAI/1339](https://t.me/dealerAI/1339), [data_secrets/7130](https://t.me/data_secrets/7130), [axisofordinary/7337](https://t.me/axisofordinary/7337), [AGI_and_RL/1136](https://t.me/AGI_and_RL/1136)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The authors claim that RPT offers a scalable and general-purpose approach to RL pre-training, but the authors only conduct experiments on a small-scale model (14B) and a specific dataset (mathematical documents). The authors should conduct experiments on large-scale models (e.g., 70B, 130B) and general-domain text. 2. The authors claim that RPT minimizes reward hacking through rule- deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2505.24832"></a>
### How much do language models memorize?

`arxiv:2505.24832` · Data, training, optimization · 2025-05-30

- final **+0.31** (conf 0.71, pct 75) · impact +0.51 · KEEP
- mean rating (1–10): **6.0** · accept votes **6/7** · percentile rank_avg 61.4 (100=best) · rank in year 29.0 (1=best)
- NAIPv2 `-0.806` · NAIP-v1 `0.508` · SciJudge `2.637` · DGC-BERT `0.785`
- CycleReviewer 8B `5.2` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.5` Accept (S/P/C 3.25/3.25/3.25) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/5721](https://t.me/gonzo_ML/5721), [data_secrets/7050](https://t.me/data_secrets/7050), [axisofordinary/7283](https://t.me/axisofordinary/7283), [abstractDL/338](https://t.me/abstractDL/338)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper's main contribution is the proposed definition of memorization based on Kolmogorov complexity. However, this definition is not very practical, as it is difficult to estimate Kolmogorov complexity in practice. The paper also does not provide a clear comparison with existing definitions of memorization, such as those based on perplexity or likelihood.  The paper's experiments a cyclereviewer-8b.seed1: Weaknesses  The paper lacks a clear motivation for the pr

<a id="arxiv-2410.07041"></a>
### Emergent properties with repeated examples

`arxiv:2410.07041` · Data, training, optimization · 2024-10-09

- final **+0.07** (conf 0.71, pct 48) · impact -2.05 · WATCH
- mean rating (1–10): **6.1** · accept votes **5/7** · percentile rank_avg 41.4 (100=best) · rank in year 29.0 (1=best)
- NAIPv2 `-2.184` · NAIP-v1 `0.120` · SciJudge `-3.312` · DGC-BERT `0.719`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `6.5` Accept (S/P/C 2.75/3.25/2.75) · 14B Fast `6.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [abstractDL/300](https://t.me/abstractDL/300), [axisofordinary/6696](https://t.me/axisofordinary/6696)
- Weaknesses: cyclereviewer-8b: Weaknesses  The main weakness of the paper is that the results are only shown on synthetic datasets. While the authors argue that these datasets are well suited for studying the effect of repeated examples, it would be nice to see some results on real-world datasets. Additionally, the authors only study the effect of repeated examples in the context of transformers, it would be nice to see if the  deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2409.03137"></a>
### The AdEMAMix Optimizer: Better, Faster, Older

`arxiv:2409.03137` · Data, training, optimization · 2024-09-05

- final **+0.35** (conf 0.71, pct 77) · impact -0.26 · KEEP
- mean rating (1–10): **6.1** · accept votes **4/7** · percentile rank_avg 51.4 (100=best) · rank in year 19.0 (1=best)
- NAIPv2 `-0.882` · NAIP-v1 `0.472` · SciJudge `0.180` · DGC-BERT `0.901`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `7.5` Accept (S/P/C 3.25/3.25/3.25) · 14B Fast `6.5` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/6587](https://t.me/axisofordinary/6587)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper does not provide a theoretical analysis of the proposed optimizer. - The paper does not provide a detailed analysis of the hyperparameters, including how they affect the performance and how to choose them in practice. - The paper does not compare AdEMAMix with other optimizers, such as SGD and AdamW with different hyperparameters.  ### Questions  - Can the authors provide a deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2405.20541"></a>
### Perplexed by Perplexity: Perplexity-Based Data Pruning With Small Reference Models

`arxiv:2405.20541` · Data, training, optimization · 2024-05-30

- final **+0.19** (conf 0.71, pct 60) · impact -0.60 · WATCH
- mean rating (1–10): **5.2** · accept votes **4/7** · percentile rank_avg 40.0 (100=best) · rank in year 32.0 (1=best)
- NAIPv2 `-1.069` · NAIP-v1 `0.432` · SciJudge `-0.741` · DGC-BERT `0.758`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.2` Reject · 7B Fast `6.0` Accept (S/P/C 3.25/3.0/2.75) · 14B Fast `7.0` Accept
- OpenReviewer `2.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [data_secrets/4407](https://t.me/data_secrets/4407), [axisofordinary/6387](https://t.me/axisofordinary/6387)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper's main contribution is an empirical investigation of perplexity-based data pruning for LLMs. While the results are promising, the paper lacks a theoretical foundation or a clear explanation of the underlying mechanisms driving the observed effects. The authors acknowledge this limitation and suggest that future work should investigate the predictive theory for how pruning par cyclereviewer-8b.seed1: Weaknesses  - The novelty of the paper is limited. The me

<a id="arxiv-2405.20233"></a>
### Grokfast: Accelerated Grokking by Amplifying Slow Gradients

`arxiv:2405.20233` · Data, training, optimization · 2024-05-30

- final **+0.18** (conf 0.71, pct 60) · impact -0.73 · WATCH
- mean rating (1–10): **6.0** · accept votes **3/7** · percentile rank_avg 50.1 (100=best) · rank in year 23.0 (1=best)
- NAIPv2 `1.244` · NAIP-v1 `0.455` · SciJudge `-2.139` · DGC-BERT `0.789`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `6.0` Reject (S/P/C 2.75/3.0/2.5) · 14B Fast `5.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [axisofordinary/6444](https://t.me/axisofordinary/6444), [axisofordinary/6417](https://t.me/axisofordinary/6417)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper lacks a theoretical analysis of the proposed method. It would be helpful to have a theoretical explanation of why the method works and under what conditions it is effective. - The paper only considers a limited set of tasks and datasets. It would be helpful to see if the method works on a wider range of tasks and datasets.  ### Questions  - Can the method be applied to othe deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2405.18392"></a>
### Scaling Laws and Compute-Optimal Training Beyond Fixed Training Durations

`arxiv:2405.18392` · Data, training, optimization · 2024-05-28

- final **+0.27** (conf 0.71, pct 70) · impact +0.07 · KEEP
- mean rating (1–10): **5.9** · accept votes **5/7** · percentile rank_avg 50.8 (100=best) · rank in year 21.0 (1=best)
- NAIPv2 `1.571` · NAIP-v1 `0.550` · SciJudge `0.251` · DGC-BERT `0.653`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.8` Reject · 7B Fast `5.8` Accept (S/P/C 2.75/3.0/2.5) · 14B Fast `6.8` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [fminxyz/26](https://t.me/fminxyz/26)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper does not provide a thorough theoretical analysis of the proposed approach. It would be helpful to understand the underlying reasons for the effectiveness of the constant learning rate schedule with a cooldown period. 2. The paper does not provide a detailed comparison with other learning rate schedules, such as the inverse square root schedule, which is commonly used for t deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2405.16684"></a>
### gzip Predicts Data-dependent Scaling Laws

`arxiv:2405.16684` · Data, training, optimization · 2024-05-26

- final **-0.09** (conf 0.71, pct 31) · impact -0.80 · WATCH
- mean rating (1–10): **5.2** · accept votes **3/7** · percentile rank_avg 40.2 (100=best) · rank in year 30.0 (1=best)
- NAIPv2 `-0.097` · NAIP-v1 `0.392` · SciJudge `-0.759` · DGC-BERT `0.855`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.8` Reject · 7B Fast `4.8` Reject (S/P/C 2.25/2.5/2.5) · 14B Fast `4.2` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/6364](https://t.me/axisofordinary/6364)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper only considers a synthetic dataset generated by PCFG, which is not very realistic. - The paper does not provide any theoretical analysis or justification for the proposed data-dependent scaling law. - The paper does not evaluate the proposed scaling law on real-world datasets or real-world applications.  ### Questions  - What is the motivation for using gzip-compressibility deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2405.15682"></a>
### The Road Less Scheduled

`arxiv:2405.15682` · Data, training, optimization · 2024-05-24

- final **+0.39** (conf 0.71, pct 82) · impact +0.32 · KEEP
- mean rating (1–10): **5.8** · accept votes **5/7** · percentile rank_avg 59.9 (100=best) · rank in year 7.0 (1=best)
- NAIPv2 `-0.572` · NAIP-v1 `0.472` · SciJudge `2.952` · DGC-BERT `0.912`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `8.0` Accept · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/2.67) · 14B Fast `5.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper only considers convex problems and does not provide any theoretical results for non-convex problems. - The method requires the stopping time T to be known or set in advance, which may not always be possible in practice. - The method requires the use of a new hyperparameter $\beta$ which may require additional tuning. - The method does not provide any convergence guarantees  cyclereviewer-8b.seed1: Weaknesses  1. The method seems to be a combination of mo

<a id="arxiv-2403.05175"></a>
### Continual Learning and Catastrophic Forgetting

`arxiv:2403.05175` · Data, training, optimization · 2024-03-08

- final **-0.39** (conf 0.71, pct 14) · impact -1.07 · DROP
- mean rating (1–10): **5.6** · accept votes **2/7** · percentile rank_avg 24.1 (100=best) · rank in year 42.0 (1=best)
- NAIPv2 `-3.904` · NAIP-v1 `0.467` · SciJudge `-4.969` · DGC-BERT `0.018`
- CycleReviewer 8B `5.2` Reject · 70B `` 
- DeepReviewer 7B Std `3.0` Reject · 7B Fast `5.0` Reject (S/P/C None/None/None) · 14B Fast `5.8` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/4.0/2.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  - The chapter does not provide a lot of new insights. The authors do not present any new results or new approaches. The chapter is mostly a summary of the existing literature.  - The chapter does not provide a clear conclusion or future directions for the field of continual learning.  ## Questions  - Why is the field of continual learning so important? What are the main challenges in t deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2402.02342"></a>
### MetaOptimize: A Framework for Optimizing Step Sizes and Other Meta-parameters

`arxiv:2402.02342` · Data, training, optimization · 2024-02-04

- final **-0.30** (conf 0.71, pct 20) · impact -1.71 · DROP
- mean rating (1–10): **5.4** · accept votes **3/7** · percentile rank_avg 32.5 (100=best) · rank in year 40.0 (1=best)
- NAIPv2 `-1.805` · NAIP-v1 `0.266` · SciJudge `-4.786` · DGC-BERT `0.945`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.8` Reject · 7B Fast `4.2` Reject (S/P/C 2.5/2.25/2.25) · 14B Fast `5.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/2.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper does not provide a comprehensive comparison with existing methods for optimizing meta-parameters. - The paper does not provide a detailed analysis of the computational complexity of the proposed framework. - The paper does not provide a detailed analysis of the performance of the proposed framework on a wide range of machine learning tasks.  ### Questions  - Can the framewo deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2401.17401"></a>
### Step-size Optimization for Continual Learning

`arxiv:2401.17401` · Data, training, optimization · 2024-01-30

- final **-0.78** (conf 0.70, pct 3) · impact -2.36 · DROP · salvage dr7bf
- mean rating (1–10): **3.4** · accept votes **1/7** · percentile rank_avg 12.8 (100=best) · rank in year 46.0 (1=best)
- NAIPv2 `-3.381` · NAIP-v1 `0.206` · SciJudge `-7.192` · DGC-BERT `0.502`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast ``  (S/P/C 2.67/2.33/2.0) · 14B Fast `3.0` Reject
- OpenReviewer `3.0` Reject (S/P/C 2.0/2.0/2.0) · SEA-E `3.0` Reject
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper does not provide any new results or insights that are not already available in the literature. The authors do not provide any new experiments or analysis that demonstrate the effectiveness of their approach.  ### Questions  The authors should provide more details about the experimental setup and the results. For example, what are the hyperparameters used for each method? What deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2312.17742"></a>
### Learning Vision from Models Rivals Learning Vision from Data

`arxiv:2312.17742` · Data, training, optimization · 2023-12-28

- final **+0.17** (conf 0.71, pct 59) · impact +0.15 · WATCH
- mean rating (1–10): **5.8** · accept votes **3/7** · percentile rank_avg 51.0 (100=best) · rank in year 21.0 (1=best)
- NAIPv2 `-1.154` · NAIP-v1 `0.652` · SciJudge `0.142` · DGC-BERT `0.916`
- CycleReviewer 8B `4.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.0` Reject · 7B Fast `6.0` Reject (S/P/C 3.0/3.0/2.5) · 14B Fast `7.0` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [axisofordinary/5918](https://t.me/axisofordinary/5918)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The authors claim that "learning from models, without training on any real data, can yield representations that match the top-performing representations learnt from real data." However, the results in Table 8 show that the proposed method performs worse than methods that use real data, such as DINO v2. The authors should clarify this point in the paper. - The authors claim that "the  deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2312.10549"></a>
### Catastrophic Forgetting in Deep Learning: A Comprehensive Taxonomy

`arxiv:2312.10549` · Data, training, optimization · 2023-12-16

- final **-0.78** (conf 0.71, pct 2) · impact -0.18 · DROP
- mean rating (1–10): **3.3** · accept votes **0/7** · percentile rank_avg 16.0 (100=best) · rank in year 47.0 (1=best)
- NAIPv2 `-3.830` · NAIP-v1 `0.671` · SciJudge `-2.951` · DGC-BERT `0.045`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `4.5` Reject (S/P/C 2.75/2.75/2.0) · 14B Fast `3.0` Reject
- OpenReviewer `3.0` Reject (S/P/C 2.0/2.0/2.0) · SEA-E `3.0` Reject
- Telegram: —
- Weaknesses: cyclereviewer-8b: weaknesses of each category and provide a discussion of the current state of the field.  ## Soundness  2 fair  ## Presentation  2 fair  ## Contribution  2 fair  ## Strengths  The paper provides a comprehensive review of the literature on catastrophic forgetting in deep learning, including a taxonomy of methods for mitigating catastrophic forgetting. The authors discuss the problem of catastrophic  cyclereviewer-8b.seed1: weaknesses of each category and provide a taxonomy to hel

<a id="arxiv-2307.06440"></a>
### No Train No Gain: Revisiting Efficient Training Algorithms For Transformer-based Language Models

`arxiv:2307.06440` · Data, training, optimization · 2023-07-12

- final **-0.01** (conf 0.71, pct 37) · impact -0.70 · WATCH
- mean rating (1–10): **4.8** · accept votes **3/7** · percentile rank_avg 37.6 (100=best) · rank in year 37.0 (1=best)
- NAIPv2 `0.661` · NAIP-v1 `0.517` · SciJudge `-2.688` · DGC-BERT `0.796`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.2` Reject · 7B Fast `5.2` Reject (S/P/C 2.5/3.0/2.5) · 14B Fast `6.8` Accept
- OpenReviewer `3.0` Reject (S/P/C 2.0/2.0/1.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper does not provide any significant contribution. The authors evaluate a number of methods that aim to speed up training of transformer-based language models and find that they do not improve over the baseline models. The paper does not propose any new methods for speeding up training of transformer-based language models.  ### Questions  N/A  ### Flag For Ethics Review  No ethic deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="doi-10.1038-s41586-024-07711-7"></a>
### Loss of plasticity in deep continual learning

`doi:10.1038/s41586-024-07711-7` · Data, training, optimization · 2024-08-21

- final **+0.40** (conf 0.71, pct 83) · impact -0.79 · KEEP
- mean rating (1–10): **6.2** · accept votes **5/7** · percentile rank_avg 50.7 (100=best) · rank in year 22.0 (1=best)
- NAIPv2 `-2.879` · NAIP-v1 `0.428` · SciJudge `-1.420` · DGC-BERT `0.407`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.8` Accept · 7B Fast `7.0` Accept (S/P/C 3.0/3.25/3.25) · 14B Fast `6.8` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `8.0` Accept
- Telegram: [knowledge_accumulator/323](https://t.me/knowledge_accumulator/323), [AGI_and_RL/847](https://t.me/AGI_and_RL/847)
- Weaknesses: cyclereviewer-8b: Weaknesses  The main weakness of the paper is the lack of theoretical analysis. The authors do not provide any theoretical analysis of the proposed algorithm or the loss of plasticity phenomenon. While the experiments are extensive, they do not provide any insights into why the proposed algorithm works or why the loss of plasticity occurs. The authors should provide some theoretical analysis to su deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2305.14342"></a>
### Sophia: A Scalable Stochastic Second-order Optimizer for Language Model Pre-training

`arxiv:2305.14342` · Data, training, optimization · 2023-05-23

- final **+0.04** (conf 0.71, pct 42) · impact +0.72 · WATCH
- mean rating (1–10): **5.8** · accept votes **4/7** · percentile rank_avg 53.9 (100=best) · rank in year 15.0 (1=best)
- NAIPv2 `-1.202` · NAIP-v1 `0.658` · SciJudge `2.084` · DGC-BERT `0.770`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `6.2` Reject (S/P/C 2.75/2.75/2.5) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [data_secrets/1518](https://t.me/data_secrets/1518), [ai_newz/1954](https://t.me/ai_newz/1954)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The theoretical analysis is not sufficient. The theoretical results are only for convex functions, which is not the case for LLMs. - The proposed method is not compared with other second-order methods.  ### Questions  - The proposed method is not compared with other second-order methods. - The theoretical analysis is not sufficient. The theoretical results are only for convex functio deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2302.06675"></a>
### Symbolic Discovery of Optimization Algorithms

`arxiv:2302.06675` · Data, training, optimization · 2023-02-13

- final **+0.50** (conf 0.71, pct 91) · impact +1.70 · KEEP
- mean rating (1–10): **6.5** · accept votes **5/7** · percentile rank_avg 73.8 (100=best) · rank in year 1.0 (1=best)
- NAIPv2 `-0.872` · NAIP-v1 `0.779` · SciJudge `3.506` · DGC-BERT `0.449`
- CycleReviewer 8B `6.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `7.0` Accept (S/P/C 3.0/3.0/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [knowledge_accumulator/139](https://t.me/knowledge_accumulator/139), [gonzo_ML/1674](https://t.me/gonzo_ML/1674), [axisofordinary/4403](https://t.me/axisofordinary/4403), [lovedeathtransformers/5426](https://t.me/lovedeathtransformers/5426), [tech_priestess/1159](https://t.me/tech_priestess/1159), [derplearning/2341](https://t.me/derplearning/2341), [j_links/6478](https://t.me/j_links/6478)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper does not provide a detailed analysis of the discovered Lion algorithm, such as its convergence properties and theoretical guarantees. - The paper does not compare the proposed method with other existing approaches to discovering optimization algorithms, such as reinforcement learning-based methods. - The paper does not discuss the limitations of the proposed method and the  deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2212.14034"></a>
### Cramming: Training a Language Model on a Single GPU in One Day

`arxiv:2212.14034` · Data, training, optimization · 2022-12-28

- final **-0.16** (conf 0.71, pct 25) · impact -0.92 · WATCH
- mean rating (1–10): **5.8** · accept votes **3/7** · percentile rank_avg 37.7 (100=best) · rank in year 16.0 (1=best)
- NAIPv2 `-1.931` · NAIP-v1 `0.429` · SciJudge `-0.124` · DGC-BERT `0.737`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `5.5` Reject (S/P/C 2.75/3.0/2.5) · 14B Fast `5.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `7.0` Accept
- Telegram: [gonzo_ML/1217](https://t.me/gonzo_ML/1217), [scitator_ai/58](https://t.me/scitator_ai/58), [gonzo_ML/1179](https://t.me/gonzo_ML/1179), [axisofordinary/4093](https://t.me/axisofordinary/4093), [j_links/6380](https://t.me/j_links/6380)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The novelty of this paper is limited. The authors mainly investigate the effects of various modifications to the training pipeline and find that most of the improvements are related to the scaling laws. This is not a surprising result and has been known in the literature.   2. The experiments are not convincing. The authors only conduct experiments on a single task, GLUE, and the re deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2210.10760"></a>
### Scaling Laws for Reward Model Overoptimization

`arxiv:2210.10760` · Data, training, optimization · 2022-10-19

- final **+0.24** (conf 0.71, pct 66) · impact -0.39 · KEEP
- mean rating (1–10): **6.1** · accept votes **5/7** · percentile rank_avg 51.9 (100=best) · rank in year 9.0 (1=best)
- NAIPv2 `-0.943` · NAIP-v1 `0.466` · SciJudge `1.368` · DGC-BERT `0.793`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `6.7` Accept (S/P/C 2.67/2.67/2.67) · 14B Fast `5.8` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [dealerAI/8](https://t.me/dealerAI/8), [lovedeathtransformers/5297](https://t.me/lovedeathtransformers/5297), [lovedeathtransformers/5427](https://t.me/lovedeathtransformers/5427)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper does not provide a clear motivation for why the synthetic setup is a good proxy for real-world RLHF. The authors acknowledge this limitation in the paper, but do not provide any evidence that the synthetic setup is a good approximation of real-world RLHF. 2. The paper does not provide a clear explanation of how the results can be used to improve RLHF. The authors find that deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2110.09485"></a>
### Learning in High Dimension Always Amounts to Extrapolation

`arxiv:2110.09485` · Data, training, optimization · 2021-10-18

- final **-0.39** (conf 0.71, pct 14) · impact -0.44 · DROP
- mean rating (1–10): **3.9** · accept votes **1/7** · percentile rank_avg 27.1 (100=best) · rank in year 9.0 (1=best)
- NAIPv2 `-0.846` · NAIP-v1 `0.525` · SciJudge `0.209` · DGC-BERT `0.218`
- CycleReviewer 8B `1.0` Reject · 70B `` 
- DeepReviewer 7B Std `3.0` Reject · 7B Fast `5.5` Reject (S/P/C 3.0/2.75/2.5) · 14B Fast `6.0` Reject
- OpenReviewer `1.0` Reject (S/P/C 2.0/2.0/1.0) · SEA-E `6.0` Accept
- Telegram: [j_links/5300](https://t.me/j_links/5300)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper is not well written and the contribution is not clear. The authors do not provide any new theoretical results. They just collect some known results from convex geometry and use them to support their claim. The experiments are not well designed and the results are not clear. The authors do not provide any conclusion or recommendation.  ### Questions  - The authors claim that i deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2108.06325"></a>
### Continual Backprop: Stochastic Gradient Descent with Persistent Randomness

`arxiv:2108.06325` · Data, training, optimization · 2021-08-13

- final **-0.62** (conf 0.71, pct 6) · impact -1.86 · DROP
- mean rating (1–10): **3.7** · accept votes **0/7** · percentile rank_avg 15.5 (100=best) · rank in year 11.0 (1=best)
- NAIPv2 `-2.754` · NAIP-v1 `0.266` · SciJudge `-4.440` · DGC-BERT `0.349`
- CycleReviewer 8B `4.2` Reject · 70B `` 
- DeepReviewer 7B Std `5.8` Reject · 7B Fast `5.2` Reject (S/P/C 2.75/2.25/2.5) · 14B Fast `3.0` Reject
- OpenReviewer `3.0` Reject (S/P/C 3.0/2.0/2.0) · SEA-E `3.0` Reject
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper is poorly written and the results are not convincing. The paper does not cite a large body of work on continual learning. The paper does not compare with other continual learning methods. The paper does not discuss the limitations of the proposed method.  ### Questions  1. What is the main contribution of the paper? The paper claims that it shows that backprop degrades over t deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2010.01412"></a>
### Sharpness-Aware Minimization for Efficiently Improving Generalization

`arxiv:2010.01412` · Data, training, optimization · 2020-10-03

- final **+0.65** (conf 0.71, pct 97) · impact +1.68 · KEEP
- mean rating (1–10): **6.0** · accept votes **5/7** · percentile rank_avg 68.0 (100=best) · rank in year 1.0 (1=best)
- NAIPv2 `1.366` · NAIP-v1 `0.811` · SciJudge `2.862` · DGC-BERT `0.925`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `7.0` Accept (S/P/C 3.25/3.25/3.0) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/2001](https://t.me/gonzo_ML/2001), [j_links/4264](https://t.me/j_links/4264), [tech_priestess/1047](https://t.me/tech_priestess/1047), [lovedeathtransformers/6486](https://t.me/lovedeathtransformers/6486)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The proposed method is not well motivated. The theorem in Section 2 does not provide a clear justification for why minimizing loss sharpness improves generalization. The connection between loss sharpness and generalization is not well established. - The proposed method is not novel. The idea of penalizing sharpness has been explored in previous work, such as (1,2,3). The proposed met deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2009.11848"></a>
### How Neural Networks Extrapolate: From Feedforward to Graph Neural Networks

`arxiv:2009.11848` · Data, training, optimization · 2020-09-24

- final **+0.28** (conf 0.71, pct 72) · impact -0.43 · KEEP
- mean rating (1–10): **6.1** · accept votes **5/7** · percentile rank_avg 51.3 (100=best) · rank in year 7.0 (1=best)
- NAIPv2 `-0.141` · NAIP-v1 `0.540` · SciJudge `-0.798` · DGC-BERT `0.418`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `5.7` Accept (S/P/C 2.67/2.67/2.33) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [j_links/4183](https://t.me/j_links/4183)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper studies the extrapolation ability of neural networks, but the results are only for ReLU MLPs in the NTK regime. The results are not generalizable to other types of neural networks.  2. The paper only considers the setting of two-layer networks. The results may not be generalizable to deeper networks.  3. The paper only considers the setting of GD with squared loss. The res deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2009.11243"></a>
### Tasks, stability, architecture, and compute: Training more effective learned optimizers, and using them to train themselves

`arxiv:2009.11243` · Data, training, optimization · 2020-09-23

- final **+0.55** (conf 0.71, pct 95) · impact +0.10 · KEEP
- mean rating (1–10): **6.7** · accept votes **5/7** · percentile rank_avg 59.4 (100=best) · rank in year 5.0 (1=best)
- NAIPv2 `-1.413` · NAIP-v1 `0.625` · SciJudge `0.558` · DGC-BERT `0.619`
- CycleReviewer 8B `5.8` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `8.0` Accept (S/P/C 3.67/3.67/3.67) · 14B Fast `5.8` Reject
- OpenReviewer `8.0` Accept (S/P/C 3.0/4.0/4.0) · SEA-E `6.0` Accept
- Telegram: [knowledge_accumulator/110](https://t.me/knowledge_accumulator/110), [gonzo_ML/372](https://t.me/gonzo_ML/372), [j_links/4121](https://t.me/j_links/4121)
- Weaknesses: cyclereviewer-8b: Weaknesses  The main weakness of the paper is that it does not provide a clear explanation of why the proposed optimizer works better than previous learned optimizers. The authors do not provide any analysis of the learned optimizer's behavior, such as the types of inductive biases it learns or how it adapts to different tasks. This makes it difficult to understand the underlying mechanisms that l deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2001.08361"></a>
### Scaling Laws for Neural Language Models

`arxiv:2001.08361` · Data, training, optimization · 2020-01-23

- final **+0.43** (conf 0.71, pct 86) · impact +1.83 · KEEP
- mean rating (1–10): **5.6** · accept votes **4/7** · percentile rank_avg 66.1 (100=best) · rank in year 3.0 (1=best)
- NAIPv2 `0.012` · NAIP-v1 `0.787` · SciJudge `3.527` · DGC-BERT `0.896`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.0` Reject · 7B Fast `6.0` Reject (S/P/C 2.67/3.33/2.33) · 14B Fast `4.0` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [gonzo_ML/4730](https://t.me/gonzo_ML/4730), [data_secrets/5534](https://t.me/data_secrets/5534), [gonzo_ML/1856](https://t.me/gonzo_ML/1856), [AGI_and_RL/612](https://t.me/AGI_and_RL/612), [gonzo_ML/1216](https://t.me/gonzo_ML/1216), [rybolos_channel/316](https://t.me/rybolos_channel/316), [dlinnlp/736](https://t.me/dlinnlp/736), [lovedeathtransformers/5878](https://t.me/lovedeathtransformers/5878)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper does not provide any theoretical analysis of the scaling laws.  ## Questions  1. What are the theoretical implications of the scaling laws? 2. How do the scaling laws depend on the choice of loss function?  ## Flag For Ethics Review  No ethics review needed.  ## Rating  6: marginally above the acceptance threshold  ## Confidence  4: You are confident in your assessment, but n deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-1904.00962"></a>
### Large Batch Optimization for Deep Learning: Training BERT in 76 minutes

`arxiv:1904.00962` · Data, training, optimization · 2019-04-01

- final **+0.56** (conf 0.71, pct 96) · impact +0.46 · KEEP
- mean rating (1–10): **5.8** · accept votes **4/7** · percentile rank_avg 61.7 (100=best) · rank in year 1.0 (1=best)
- NAIPv2 `0.668` · NAIP-v1 `0.668` · SciJudge `1.367` · DGC-BERT `0.913`
- CycleReviewer 8B `5.2` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `7.0` Accept (S/P/C 3.25/3.0/2.75) · 14B Fast `6.0` Reject
- OpenReviewer `5.0` Reject (S/P/C 2.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [j_links/2316](https://t.me/j_links/2316)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper is not well-organized. The authors present the convergence analysis of Lamb and Lars in Section 3, but do not provide any experimental results in this section. Instead, the experimental results are presented in Section 4. This makes it difficult to understand the significance of the convergence analysis.  2. The paper lacks a clear motivation for the proposed algorithm. Th cyclereviewer-8b.seed1: Weaknesses  1. The paper only provides a limited number o

<a id="arxiv-1803.03635"></a>
### The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks

`arxiv:1803.03635` · Data, training, optimization · 2018-03-09

- final **+0.14** (conf 0.71, pct 56) · impact +0.66 · WATCH
- mean rating (1–10): **5.7** · accept votes **3/7** · percentile rank_avg 46.1 (100=best) · rank in year 2.0 (1=best)
- NAIPv2 `-1.059` · NAIP-v1 `0.703` · SciJudge `1.989` · DGC-BERT `0.135`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `5.0` Reject (S/P/C 2.5/2.5/2.5) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/4350](https://t.me/gonzo_ML/4350), [partially_unsupervised/228](https://t.me/partially_unsupervised/228), [gonzo_ML/884](https://t.me/gonzo_ML/884), [dlinnlp/956](https://t.me/dlinnlp/956), [gonzo_ML/196](https://t.me/gonzo_ML/196), [gonzo_ML/21](https://t.me/gonzo_ML/21)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper only considers small datasets (MNIST and CIFAR-10), and the proposed method is not efficient to apply to large-scale datasets. It would be better to consider larger datasets and more efficient methods for finding winning tickets. 2. The paper only considers sparse pruning, and it would be better to consider other pruning methods such as structured pruning. 3. The paper onl deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="openreview-ry_WPG-A-"></a>
### On the Information Bottleneck Theory of Deep Learning (Saxe et al.)

`openreview:ry_WPG-A-` · Data, training, optimization · unknown

- final **-0.03** (conf 0.71, pct 35) · impact +0.03 · WATCH
- mean rating (1–10): **5.8** · accept votes **5/7** · percentile rank_avg 40.6 (100=best) · rank in year 5.0 (1=best)
- NAIPv2 `-1.558` · NAIP-v1 `0.431` · SciJudge `2.281` · DGC-BERT `0.465`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `3.0` Reject · 7B Fast `5.5` Accept (S/P/C 2.25/2.5/2.5) · 14B Fast `5.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [j_links/582](https://t.me/j_links/582)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper claims that the information bottleneck theory of deep learning is not supported by the experimental results. However, the experiments are limited to small networks and simple datasets. The authors do not provide a comprehensive analysis of the theory and its limitations. The authors also do not provide a clear explanation of the reasons why the compression phase is not observ cyclereviewer-8b.seed1: Weaknesses  The paper could benefit from a more detailed 

<a id="arxiv-1708.07120"></a>
### Super-Convergence: Very Fast Training of Neural Networks Using Large Learning Rates

`arxiv:1708.07120` · Data, training, optimization · 2017-08-23

- final **-0.07** (conf 0.71, pct 32) · impact -0.34 · WATCH
- mean rating (1–10): **4.7** · accept votes **3/7** · percentile rank_avg 38.0 (100=best) · rank in year 6.0 (1=best)
- NAIPv2 `-0.206` · NAIP-v1 `0.528` · SciJudge `0.748` · DGC-BERT `0.854`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.2` Reject · 7B Fast `5.8` Reject (S/P/C 2.5/2.5/2.5) · 14B Fast `6.7` Accept
- OpenReviewer `3.0` Reject (S/P/C 2.0/1.0/2.0) · SEA-E `5.0` Accept
- Telegram: [j_links/420](https://t.me/j_links/420)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper lacks a thorough theoretical analysis of the proposed method. The authors provide some insights into the effect of large learning rates and the balance of regularization, but a more rigorous theoretical framework would strengthen the paper. The experimental results are promising, but more comprehensive experiments and comparisons with other state-of-the-art methods would be b deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-1708.02072"></a>
### Measuring Catastrophic Forgetting in Neural Networks

`arxiv:1708.02072` · Data, training, optimization · 2017-08-07

- final **-0.63** (conf 0.71, pct 6) · impact -0.42 · DROP
- mean rating (1–10): **4.0** · accept votes **2/7** · percentile rank_avg 22.9 (100=best) · rank in year 7.0 (1=best)
- NAIPv2 `-2.916` · NAIP-v1 `0.558` · SciJudge `-0.195` · DGC-BERT `0.521`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.2` Reject · 7B Fast `4.8` Reject (S/P/C 2.25/2.75/2.25) · 14B Fast `3.5` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `3.0` Reject
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper does not provide any new insights or contributions to the field. - The paper only provides a review of existing methods and does not propose any new methods to mitigate catastrophic forgetting. - The paper does not provide any experimental results on new datasets or benchmarks.  ### Questions  Please see the weaknesses.  ### Flag For Ethics Review  No ethics review needed.  deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="doi-10.1073-pnas.1611835114"></a>
### Overcoming catastrophic forgetting in neural networks

`doi:10.1073/pnas.1611835114` · Data, training, optimization · 2017-03-14

- final **+0.00** (conf 0.71, pct 39) · impact -0.12 · WATCH
- mean rating (1–10): **5.8** · accept votes **4/7** · percentile rank_avg 39.4 (100=best) · rank in year 5.0 (1=best)
- NAIPv2 `-4.164` · NAIP-v1 `0.542` · SciJudge `1.496` · DGC-BERT `0.360`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `6.0` Accept (S/P/C 3.0/2.75/2.75) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  The main weakness of the paper is that the method is not evaluated on a wide range of tasks and datasets. The authors only evaluate their method on MNIST and Atari, which are relatively simple tasks. It would be good to see how the method performs on more complex tasks, such as image classification on CIFAR-10 or CIFAR-100, or language modeling on text datasets. Additionally, the autho deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-1506.01186"></a>
### Cyclical Learning Rates for Training Neural Networks

`arxiv:1506.01186` · Data, training, optimization · 2015-06-03

- final **-0.52** (conf 0.71, pct 8) · impact -0.25 · DROP
- mean rating (1–10): **4.4** · accept votes **1/7** · percentile rank_avg 20.3 (100=best) · rank in year 4.0 (1=best)
- NAIPv2 `-3.008` · NAIP-v1 `0.664` · SciJudge `-1.382` · DGC-BERT `0.304`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `2.5` Reject · 7B Fast `5.2` Reject (S/P/C 2.5/2.75/2.25) · 14B Fast `4.8` Reject
- OpenReviewer `3.0` Reject (S/P/C 2.0/1.0/1.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The authors only provide experimental results on a limited number of datasets and architectures. It would be better if the authors can provide more experimental results on other datasets and architectures. 2. The authors only provide results on classification tasks. It would be better if the authors can provide results on other tasks such as regression and generative tasks. 3. The a deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2606.02572"></a>
### VISReg: Variance-Invariance-Sketching Regularization for JEPA training

`arxiv:2606.02572` · Self-supervised learning and vision · 2026-06-01

- final **+0.42** (conf 0.71, pct 85) · impact -0.29 · KEEP
- mean rating (1–10): **6.5** · accept votes **6/7** · percentile rank_avg 62.3 (100=best) · rank in year 24.0 (1=best)
- NAIPv2 `1.062` · NAIP-v1 `0.622` · SciJudge `-2.665` · DGC-BERT `0.537`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `8.0` Accept (S/P/C 3.25/3.25/3.25) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [gonzo_ML/5832](https://t.me/gonzo_ML/5832)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper does not provide a theoretical analysis of the proposed method. While the authors provide an analysis of the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, it would be helpful to have a more rigorous theoretical analysis of the proposed method. - The paper does not compare with some recent SOTA methods, such as LpJEPA (1) and KerJEPA (2). - The pa deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2605.26379"></a>
### When Does LeJEPA Learn a World Model?

`arxiv:2605.26379` · Self-supervised learning and vision · 2026-05-25

- final **+0.71** (conf 0.71, pct 99) · impact -0.65 · KEEP
- mean rating (1–10): **6.7** · accept votes **6/7** · percentile rank_avg 68.4 (100=best) · rank in year 11.0 (1=best)
- NAIPv2 `0.844` · NAIP-v1 `0.475` · SciJudge `-1.511` · DGC-BERT `0.929`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.2` Accept · 7B Fast `6.5` Accept (S/P/C 3.0/3.0/3.0) · 14B Fast `8.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `8.0` Accept
- Telegram: [gonzo_ML/5489](https://t.me/gonzo_ML/5489)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper focuses on a specific type of self-supervised learning, LeJEPA, and does not consider other types of self-supervised learning. - The paper assumes that the latent variables are Gaussian, which may not be realistic in many cases. - The paper does not provide a clear explanation of how the theoretical results can be applied in practice.  ### Questions  - What are the limitati deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2604.09168"></a>
### ELT: Elastic Looped Transformers for Visual Generation

`arxiv:2604.09168` · Self-supervised learning and vision · 2026-04-10

- final **+0.05** (conf 0.71, pct 45) · impact -0.01 · WATCH
- mean rating (1–10): **6.0** · accept votes **4/7** · percentile rank_avg 53.0 (100=best) · rank in year 47.0 (1=best)
- NAIPv2 `-1.056` · NAIP-v1 `0.587` · SciJudge `0.397` · DGC-BERT `0.404`
- CycleReviewer 8B `4.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.8` Reject · 7B Fast `6.7` Accept (S/P/C 3.0/3.0/2.67) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [gonzo_ML/5303](https://t.me/gonzo_ML/5303)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The novelty of this paper is limited. The idea of using a recurrent transformer architecture for visual generation is not new. The proposed method is a combination of existing techniques, such as looping and distillation. 2. The experiments are not convincing. The authors only compare their method with MaskGIT and MAGVIT, which are not the state-of-the-art methods in visual generati cyclereviewer-8b.seed1: Weaknesses  1. The paper does not provide a thorough comp

<a id="arxiv-2511.08544"></a>
### LeJEPA: Provable and Scalable Self-Supervised Learning Without the Heuristics

`arxiv:2511.08544` · Self-supervised learning and vision · 2025-11-11

- final **+0.40** (conf 0.71, pct 82) · impact +0.72 · KEEP
- mean rating (1–10): **6.0** · accept votes **6/7** · percentile rank_avg 62.7 (100=best) · rank in year 22.0 (1=best)
- NAIPv2 `1.300` · NAIP-v1 `0.690` · SciJudge `0.745` · DGC-BERT `0.684`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `5.8` Accept (S/P/C 3.0/2.75/2.75) · 14B Fast `7.0` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [data_secrets/8254](https://t.me/data_secrets/8254), [axisofordinary/7894](https://t.me/axisofordinary/7894), [gonzo_ML/4212](https://t.me/gonzo_ML/4212)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The proposed method is not novel, as it combines two existing methods: JEPA and SIGReg. The authors should provide a more detailed discussion on how their method is different from existing methods. - The theoretical analysis is not convincing. The authors should provide more rigorous proofs and analysis to support their claims. - The experimental results are not convincing. The autho deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2501.05441"></a>
### The GAN is dead; long live the GAN! A Modern GAN Baseline

`arxiv:2501.05441` · Self-supervised learning and vision · 2025-01-09

- final **+0.06** (conf 0.71, pct 47) · impact +1.32 · WATCH
- mean rating (1–10): **5.8** · accept votes **5/7** · percentile rank_avg 59.6 (100=best) · rank in year 38.0 (1=best)
- NAIPv2 `0.142` · NAIP-v1 `0.849` · SciJudge `0.109` · DGC-BERT `0.967`
- CycleReviewer 8B `5.2` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `5.2` Reject (S/P/C 3.0/3.0/2.25) · 14B Fast `6.2` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [data_secrets/5891](https://t.me/data_secrets/5891)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The novelty of the paper is limited. The proposed method is a combination of existing methods, and the only novelty is the choice of hyperparameters. 2. The paper does not provide a thorough analysis of the proposed method. For example, the authors do not provide an ablation study of the R1 and R2 regularization terms. 3. The paper does not provide a comparison with other GAN baseli deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2310.04378"></a>
### Latent Consistency Models: Synthesizing High-Resolution Images with Few-Step Inference

`arxiv:2310.04378` · Self-supervised learning and vision · 2023-10-06

- final **+0.21** (conf 0.71, pct 62) · impact +1.73 · KEEP
- mean rating (1–10): **5.7** · accept votes **3/7** · percentile rank_avg 56.8 (100=best) · rank in year 13.0 (1=best)
- NAIPv2 `0.217` · NAIP-v1 `0.715` · SciJudge `3.772` · DGC-BERT `0.846`
- CycleReviewer 8B `5.8` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `5.2` Reject (S/P/C 2.75/2.75/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [lovedeathtransformers/6578](https://t.me/lovedeathtransformers/6578)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The proposed method is a direct extension of the consistency model to latent space. The novelty is limited. - The proposed method is not compared with the latest diffusion models, such as (1-3).  - The proposed method is not compared with the latest consistency models, such as (4, 5). - The proposed method is only evaluated on LAION-5B-Aesthetics dataset. It is not clear how the prop deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2309.15807"></a>
### Emu: Enhancing Image Generation Models Using Photogenic Needles in a Haystack

`arxiv:2309.15807` · Self-supervised learning and vision · 2023-09-27

- final **+0.21** (conf 0.71, pct 63) · impact -0.20 · KEEP
- mean rating (1–10): **6.2** · accept votes **4/7** · percentile rank_avg 53.7 (100=best) · rank in year 17.0 (1=best)
- NAIPv2 `-0.754` · NAIP-v1 `0.502` · SciJudge `1.108` · DGC-BERT `0.109`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `6.5` Reject (S/P/C 3.0/3.0/2.5) · 14B Fast `6.7` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [seeallochnaya/663](https://t.me/seeallochnaya/663), [lovedeathtransformers/9356](https://t.me/lovedeathtransformers/9356)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper has several weaknesses:  1. The paper does not provide a thorough analysis of the limitations of the proposed approach. For example, the paper does not discuss how the approach would perform on a wider range of tasks or datasets.  2. The paper does not provide a thorough analysis of the potential risks and challenges associated with the proposed approach. For example, the pap cyclereviewer-8b.seed1: Weaknesses  The paper lacks novelty. The idea of fine-tun

<a id="arxiv-2304.12210"></a>
### A Cookbook of Self-Supervised Learning

`arxiv:2304.12210` · Self-supervised learning and vision · 2023-04-24

- final **-0.69** (conf 0.71, pct 4) · impact +0.16 · DROP
- mean rating (1–10): **4.9** · accept votes **1/7** · percentile rank_avg 27.9 (100=best) · rank in year 44.0 (1=best)
- NAIPv2 `-2.777` · NAIP-v1 `0.688` · SciJudge `-0.587` · DGC-BERT `0.047`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.0` Reject · 7B Fast `5.5` Reject (S/P/C 3.0/3.0/2.25) · 14B Fast `3.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `5.0` Reject
- Telegram: [data_secrets/4262](https://t.me/data_secrets/4262), [data_secrets/1335](https://t.me/data_secrets/1335), [ai_newz/1874](https://t.me/ai_newz/1874), [dealerAI/129](https://t.me/dealerAI/129)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper is a survey paper that discusses the recent advances in self-supervised learning (SSL). The paper does not provide any new contributions or insights into the field of SSL. The paper is well-written and provides a comprehensive overview of the recent advances in SSL. However, the paper does not provide any new insights or contributions to the field of SSL. The paper is well-or deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2304.09355"></a>
### To Compress or Not to Compress- Self-Supervised Learning and Information Theory: A Review

`arxiv:2304.09355` · Self-supervised learning and vision · 2023-04-19

- final **-0.47** (conf 0.70, pct 10) · impact -0.21 · DROP · salvage dr7bf
- mean rating (1–10): **4.5** · accept votes **1/7** · percentile rank_avg 24.3 (100=best) · rank in year 45.0 (1=best)
- NAIPv2 `-2.838` · NAIP-v1 `0.636` · SciJudge `-1.772` · DGC-BERT `0.108`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast ``  (S/P/C 2.25/2.5/2.5) · 14B Fast `4.0` Reject
- OpenReviewer `5.0` Reject (S/P/C 3.0/2.0/2.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper lacks a clear research question and does not provide any new insights or contributions to the field. The paper is a review of existing work and does not provide any new results or experiments. The paper is not well-organized and is difficult to follow. The authors do not provide any clear conclusions or recommendations for future research.  ## Questions  See above.  ## Flag F cyclereviewer-8b.seed1: Weaknesses  The paper is not a research paper but a revie

<a id="arxiv-2304.07193"></a>
### DINOv2: Learning Robust Visual Features without Supervision

`arxiv:2304.07193` · Self-supervised learning and vision · 2023-04-14

- final **+0.25** (conf 0.71, pct 66) · impact +1.66 · KEEP
- mean rating (1–10): **5.7** · accept votes **4/7** · percentile rank_avg 53.7 (100=best) · rank in year 18.0 (1=best)
- NAIPv2 `-2.252` · NAIP-v1 `0.729` · SciJudge `3.537` · DGC-BERT `0.380`
- CycleReviewer 8B `5.2` Reject · 70B `` 
- DeepReviewer 7B Std `7.0` Accept · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/2.5) · 14B Fast `6.0` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [AI_DeepLearning/1031](https://t.me/AI_DeepLearning/1031), [ai_newz/1871](https://t.me/ai_newz/1871), [j_links/6646](https://t.me/j_links/6646)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper proposes a new dataset and training recipe, but the novelty is limited. The authors do not provide a detailed analysis of the proposed dataset and training recipe, and it is not clear how they differ from previous approaches.  The paper also does not provide a detailed analysis of the performance of the proposed features on different tasks and datasets. The authors only provi deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2304.05977"></a>
### ImageReward: Learning and Evaluating Human Preferences for Text-to-Image Generation

`arxiv:2304.05977` · Self-supervised learning and vision · 2023-04-12

- final **+0.53** (conf 0.71, pct 92) · impact +1.87 · KEEP
- mean rating (1–10): **6.0** · accept votes **5/7** · percentile rank_avg 65.0 (100=best) · rank in year 5.0 (1=best)
- NAIPv2 `1.893` · NAIP-v1 `0.827` · SciJudge `3.247` · DGC-BERT `0.405`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.0` Accept (S/P/C 2.75/3.0/2.75) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [axisofordinary/4834](https://t.me/axisofordinary/4834)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The authors only compared their method with a few existing methods, and it would be better if they could compare with more existing methods in the field.  - The authors only tested their method on a small set of prompts, and it would be better if they could test their method on a larger set of prompts.  - The authors only tested their method on a single diffusion model, and it would  deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2302.10174"></a>
### Towards Universal Fake Image Detectors that Generalize Across Generative Models

`arxiv:2302.10174` · Self-supervised learning and vision · 2023-02-20

- final **+0.06** (conf 0.71, pct 47) · impact +1.17 · WATCH
- mean rating (1–10): **6.4** · accept votes **4/7** · percentile rank_avg 56.9 (100=best) · rank in year 12.0 (1=best)
- NAIPv2 `-1.620` · NAIP-v1 `0.738` · SciJudge `2.115` · DGC-BERT `0.277`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `6.0` Accept (S/P/C 2.67/3.0/2.67) · 14B Fast `6.0` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper lacks novelty. The authors use the pre-trained CLIP model to extract features and then use the nearest neighbor and linear probing methods to perform the classification task. These methods are commonly used in the field of image classification and have been widely studied. The authors do not provide sufficient theoretical analysis and experimental results to support the ef deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2301.08243"></a>
### Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture

`arxiv:2301.08243` · Self-supervised learning and vision · 2023-01-19

- final **+0.23** (conf 0.71, pct 64) · impact +0.19 · KEEP
- mean rating (1–10): **6.0** · accept votes **4/7** · percentile rank_avg 50.9 (100=best) · rank in year 22.0 (1=best)
- NAIPv2 `-1.402` · NAIP-v1 `0.562` · SciJudge `1.736` · DGC-BERT `0.423`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Reject · 7B Fast `7.5` Accept (S/P/C 3.0/3.25/3.0) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/3501](https://t.me/gonzo_ML/3501), [j_links/6821](https://t.me/j_links/6821)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper lacks a strong theoretical foundation for the proposed method. While the authors provide some intuition for why the method works, there is no formal analysis or proof of its correctness or optimality. This makes it difficult to understand the underlying principles of the method and its limitations. - The paper does not provide a clear comparison to existing methods. While t cyclereviewer-8b.seed1: Weaknesses  1. The proposed method is not very novel. The

<a id="arxiv-2212.11565"></a>
### Tune-A-Video: One-Shot Tuning of Image Diffusion Models for Text-to-Video Generation

`arxiv:2212.11565` · Self-supervised learning and vision · 2022-12-22

- final **-0.32** (conf 0.71, pct 19) · impact +0.84 · WATCH
- mean rating (1–10): **5.0** · accept votes **3/7** · percentile rank_avg 41.3 (100=best) · rank in year 15.0 (1=best)
- NAIPv2 `-2.020` · NAIP-v1 `0.669` · SciJudge `2.791` · DGC-BERT `0.743`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `4.0` Reject (S/P/C 2.5/2.75/2.0) · 14B Fast `5.8` Reject
- OpenReviewer `5.0` Reject (S/P/C 2.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [monkeyinlaw/1044](https://t.me/monkeyinlaw/1044), [derplearning/2267](https://t.me/derplearning/2267), [AI_DeepLearning/831](https://t.me/AI_DeepLearning/831)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The proposed method is based on the existing T2I model, and the proposed method is not very novel. 2. The proposed method is not very effective. For example, the video generation results in Fig. 7 are not good enough. 3. The proposed method is not very efficient. For example, the training time is 10 minutes for a single video.  ### Questions  1. The proposed method is based on the e deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2208.10442"></a>
### Image as a Foreign Language: BEiT Pretraining for All Vision and Vision-Language Tasks

`arxiv:2208.10442` · Self-supervised learning and vision · 2022-08-22

- final **+0.27** (conf 0.71, pct 71) · impact +2.15 · KEEP
- mean rating (1–10): **5.5** · accept votes **5/7** · percentile rank_avg 54.1 (100=best) · rank in year 8.0 (1=best)
- NAIPv2 `-0.626` · NAIP-v1 `0.862` · SciJudge `3.207` · DGC-BERT `0.574`
- CycleReviewer 8B `4.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/3.0) · 14B Fast `6.5` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/3146](https://t.me/axisofordinary/3146), [boris_again/1163](https://t.me/boris_again/1163), [j_links/6062](https://t.me/j_links/6062), [abstractDL/157](https://t.me/abstractDL/157), [cats_shredinger/25](https://t.me/cats_shredinger/25)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The novelty of the paper is limited. The proposed method is a straightforward combination of existing methods, i.e., BEiT and Multiway Transformer.  2. The paper does not provide any analysis of the model's performance on low-resource languages, which is an important aspect of a multimodal foundation model. 3. The paper does not provide any analysis of the model's performance on out deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="openreview-BZ5a1r-kVsf"></a>
### A Path Towards Autonomous Machine Intelligence (LeCun, 2022)

`openreview:BZ5a1r-kVsf` · Self-supervised learning and vision · unknown

- final **-0.73** (conf 0.70, pct 3) · impact +0.06 · DROP · salvage dr7bf
- mean rating (1–10): **4.4** · accept votes **2/7** · percentile rank_avg 23.0 (100=best) · rank in year 11.0 (1=best)
- NAIPv2 `-4.348` · NAIP-v1 `0.523` · SciJudge `1.412` · DGC-BERT `0.006`
- CycleReviewer 8B `1.0` Reject · 70B `` 
- DeepReviewer 7B Std `3.0` Reject · 7B Fast ``  (S/P/C 2.75/2.5/2.5) · 14B Fast `3.5` Reject
- OpenReviewer `8.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `5.0` Accept
- Telegram: [gonzo_ML/3501](https://t.me/gonzo_ML/3501), [gonzo_ML/3150](https://t.me/gonzo_ML/3150), [chillhousetech/680](https://t.me/chillhousetech/680), [knowledge_accumulator/46](https://t.me/knowledge_accumulator/46), [dtulinov/508](https://t.me/dtulinov/508), [rybolos_channel/249](https://t.me/rybolos_channel/249), [scitator_ai/25](https://t.me/scitator_ai/25), [rybolos_channel/239](https://t.me/rybolos_channel/239)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper lacks concrete implementation details and experimental results to support the proposed architecture and training paradigms. The paper does not provide any code or pseudocode for the proposed architecture, and the experimental results are limited to a few examples and do not provide any quantitative evaluation of the performance of the proposed methods. The paper also does not deepreviewer-14b: Weaknesses:  The most significant weakness of this paper is its

<a id="arxiv-2111.07832"></a>
### iBOT: Image BERT Pre-Training with Online Tokenizer

`arxiv:2111.07832` · Self-supervised learning and vision · 2021-11-15

- final **+0.16** (conf 0.71, pct 58) · impact +1.50 · WATCH
- mean rating (1–10): **6.2** · accept votes **4/7** · percentile rank_avg 58.7 (100=best) · rank in year 3.0 (1=best)
- NAIPv2 `-1.606` · NAIP-v1 `0.771` · SciJudge `3.295` · DGC-BERT `0.353`
- CycleReviewer 8B `5.5` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `7.0` Accept (S/P/C 3.0/3.0/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/5626](https://t.me/gonzo_ML/5626), [j_links/5504](https://t.me/j_links/5504)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The novelty of the proposed method is limited. The idea of using self-distillation for pre-training has been explored in previous works, such as DINO. 2. The paper lacks a clear motivation for the proposed method. The authors do not provide a clear explanation of why masked image modeling with a self-distillation objective is a good approach for pre-training vision transformers. 3.  deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2105.04906"></a>
### VICReg: Variance-Invariance-Covariance Regularization for Self-Supervised Learning

`arxiv:2105.04906` · Self-supervised learning and vision · 2021-05-11

- final **-0.11** (conf 0.71, pct 29) · impact +0.07 · WATCH
- mean rating (1–10): **5.2** · accept votes **3/7** · percentile rank_avg 40.4 (100=best) · rank in year 6.0 (1=best)
- NAIPv2 `-2.426` · NAIP-v1 `0.488` · SciJudge `3.088` · DGC-BERT `0.930`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `4.0` Reject · 7B Fast `5.8` Reject (S/P/C 2.75/3.0/2.5) · 14B Fast `6.5` Accept
- OpenReviewer `3.0` Reject (S/P/C 2.0/2.0/2.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/590](https://t.me/gonzo_ML/590)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The novelty of the proposed method is limited. The proposed method is based on the principle of preserving the information content of the embeddings. The method is similar to the Barlow Twins method, which also decorrelates the variables of each embedding and prevents an informational collapse in which the variables would vary together or be highly correlated. - The experiments are n deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2104.14294"></a>
### Emerging Properties in Self-Supervised Vision Transformers

`arxiv:2104.14294` · Self-supervised learning and vision · 2021-04-29

- final **+0.54** (conf 0.71, pct 94) · impact +2.04 · KEEP
- mean rating (1–10): **6.5** · accept votes **5/7** · percentile rank_avg 72.6 (100=best) · rank in year 1.0 (1=best)
- NAIPv2 `-1.077` · NAIP-v1 `0.827` · SciJudge `3.530` · DGC-BERT `0.159`
- CycleReviewer 8B `5.8` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.7` Accept (S/P/C 3.0/3.0/2.33) · 14B Fast `7.3` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [gonzo_ML/5626](https://t.me/gonzo_ML/5626), [gonzo_ML/688](https://t.me/gonzo_ML/688), [j_links/4810](https://t.me/j_links/4810), [tech_priestess/247](https://t.me/tech_priestess/247)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The novelty of the proposed method is limited. The authors mention that their method is similar to BYOL and MoCov2, and the main difference is the use of a momentum encoder and multi-crop training. However, these components have been used in previous works, and the authors do not provide any new insights or analysis on how they contribute to the performance of the method.  2. The ex deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2006.09882"></a>
### Unsupervised Learning of Visual Features by Contrasting Cluster Assignments

`arxiv:2006.09882` · Self-supervised learning and vision · 2020-06-17

- final **+0.48** (conf 0.71, pct 90) · impact +1.06 · KEEP
- mean rating (1–10): **6.3** · accept votes **4/7** · percentile rank_avg 61.4 (100=best) · rank in year 4.0 (1=best)
- NAIPv2 `-1.362` · NAIP-v1 `0.729` · SciJudge `2.331` · DGC-BERT `0.839`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.0` Reject · 7B Fast `7.5` Accept (S/P/C 3.25/3.25/3.25) · 14B Fast `7.0` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [gonzo_ML/688](https://t.me/gonzo_ML/688)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The proposed method is not novel, as it is a variant of DeepCluster. The main difference is that the proposed method learns the cluster assignments online, while DeepCluster learns them offline. However, the online learning approach requires a more complex optimization process and is not as efficient as the offline learning approach. - The paper does not provide a thorough analysis o deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2606.18543"></a>
### CEO-Bench: Can Agents Play the Long Game?

`arxiv:2606.18543` · Retrieval, embeddings, benchmarks · 2026-06-16

- final **+0.18** (conf 0.71, pct 59) · impact +1.20 · WATCH
- mean rating (1–10): **6.4** · accept votes **5/7** · percentile rank_avg 65.6 (100=best) · rank in year 19.0 (1=best)
- NAIPv2 `-0.407` · NAIP-v1 `0.710` · SciJudge `2.263` · DGC-BERT `0.191`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.8` Reject · 7B Fast `6.5` Accept (S/P/C 3.0/3.0/2.75) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [boris_again/3974](https://t.me/boris_again/3974), [dealerAI/1857](https://t.me/dealerAI/1857)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper does not provide a detailed description of the models used in the evaluation, including their architecture, training data, and hyperparameters. This makes it difficult to understand the specific capabilities and limitations of each model and how they relate to the task. - The paper does not provide a detailed analysis of the results, including the performance of each model  deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2410.07095"></a>
### MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering

`arxiv:2410.07095` · Retrieval, embeddings, benchmarks · 2024-10-09

- final **+0.39** (conf 0.71, pct 81) · impact +0.90 · KEEP
- mean rating (1–10): **6.0** · accept votes **4/7** · percentile rank_avg 58.3 (100=best) · rank in year 10.0 (1=best)
- NAIPv2 `0.277` · NAIP-v1 `0.631` · SciJudge `2.609` · DGC-BERT `0.394`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.0` Accept (S/P/C 2.5/3.0/2.75) · 14B Fast `6.2` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `7.0` Accept
- Telegram: [gonzo_ML/4261](https://t.me/gonzo_ML/4261), [lovedeathtransformers/8445](https://t.me/lovedeathtransformers/8445), [rybolos_channel/1270](https://t.me/rybolos_channel/1270), [data_secrets/5120](https://t.me/data_secrets/5120), [seeallochnaya/1866](https://t.me/seeallochnaya/1866)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper does not provide a clear definition of machine learning engineering and how it is distinct from other areas of AI research. It would be helpful to provide a more detailed explanation of the scope and focus of the benchmark.  2. The paper does not provide a clear explanation of how the 75 Kaggle competitions were selected and why they are representative of contemporary ML e deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2405.08007"></a>
### People cannot distinguish GPT-4 from a human in a Turing test

`arxiv:2405.08007` · Retrieval, embeddings, benchmarks · 2024-05-09

- final **-0.40** (conf 0.71, pct 13) · impact +2.09 · WATCH
- mean rating (1–10): **4.6** · accept votes **1/7** · percentile rank_avg 37.9 (100=best) · rank in year 35.0 (1=best)
- NAIPv2 `-2.674` · NAIP-v1 `0.806` · SciJudge `3.261` · DGC-BERT `0.083`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `3.8` Reject · 7B Fast `4.7` Reject (S/P/C 2.67/3.0/2.33) · 14B Fast `7.5` Accept
- OpenReviewer `3.0` Reject (S/P/C 3.0/3.0/1.0) · SEA-E `3.0` Reject
- Telegram: [axisofordinary/6315](https://t.me/axisofordinary/6315), [gonzo_ML/2655](https://t.me/gonzo_ML/2655), [tech_priestess/1735](https://t.me/tech_priestess/1735)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper is not written in a way that is easy to understand. The authors seem to be writing for a very specific audience, and the paper is not well-suited for a broader audience.  ### Questions  What is the significance of the results? Why is it important to know that GPT-4 was judged to be human 54% of the time?  ### Flag For Ethics Review  No ethics review needed.  ### Rating  5: ma deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2402.16822"></a>
### Rainbow Teaming: Open-Ended Generation of Diverse Adversarial Prompts

`arxiv:2402.16822` · Retrieval, embeddings, benchmarks · 2024-02-26

- final **+0.45** (conf 0.71, pct 88) · impact +1.23 · KEEP
- mean rating (1–10): **6.6** · accept votes **6/7** · percentile rank_avg 71.5 (100=best) · rank in year 1.0 (1=best)
- NAIPv2 `-1.450` · NAIP-v1 `0.661` · SciJudge `3.145` · DGC-BERT `0.923`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.2` Accept · 7B Fast `6.7` Accept (S/P/C 2.67/3.33/2.67) · 14B Fast `7.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/4.0/3.0) · SEA-E `6.0` Accept
- Telegram: [rybolos_channel/1495](https://t.me/rybolos_channel/1495)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper lacks a clear definition of what constitutes an adversarial prompt and how it is evaluated. The authors use a variety of terms such as "harmful", "incorrect", "toxic", and "unsafe" to describe the outputs of LLMs when prompted with adversarial prompts, but it is not clear how these terms are defined or measured. Additionally, the authors do not provide a clear explanation o deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2402.12483"></a>
### Artifacts or Abduction: How Do LLMs Answer Multiple-Choice Questions Without the Question?

`arxiv:2402.12483` · Retrieval, embeddings, benchmarks · 2024-02-19

- final **-0.07** (conf 0.71, pct 33) · impact +0.87 · WATCH
- mean rating (1–10): **6.0** · accept votes **4/7** · percentile rank_avg 51.2 (100=best) · rank in year 20.0 (1=best)
- NAIPv2 `-1.801` · NAIP-v1 `0.656` · SciJudge `1.980` · DGC-BERT `0.747`
- CycleReviewer 8B `5.5` Reject · 70B `` 
- DeepReviewer 7B Std `4.2` Reject · 7B Fast `6.3` Accept (S/P/C 2.67/3.0/2.67) · 14B Fast `6.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [tech_priestess/1699](https://t.me/tech_priestess/1699), [axisofordinary/6146](https://t.me/axisofordinary/6146), [seeallochnaya/1697](https://t.me/seeallochnaya/1697)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper does not provide a clear conclusion or recommendation for how to improve MCQA benchmarks. The authors state that the LLMs' performance on choices-only prompts is not solely due to memorization, but do not provide a clear explanation of what is causing the performance. The authors also state that abductive question inference is a contributing factor, but do not provide a cle cyclereviewer-8b.seed1: Weaknesses  - The paper does not provide a clear conclusi

<a id="arxiv-2311.16452"></a>
### Can Generalist Foundation Models Outcompete Special-Purpose Tuning? Case Study in Medicine

`arxiv:2311.16452` · Retrieval, embeddings, benchmarks · 2023-11-28

- final **+0.03** (conf 0.71, pct 42) · impact +0.55 · WATCH
- mean rating (1–10): **5.9** · accept votes **5/7** · percentile rank_avg 50.6 (100=best) · rank in year 23.0 (1=best)
- NAIPv2 `-2.244` · NAIP-v1 `0.628` · SciJudge `1.979` · DGC-BERT `0.706`
- CycleReviewer 8B `5.5` Accept · 70B `` 
- DeepReviewer 7B Std `5.2` Reject · 7B Fast `5.3` Reject (S/P/C 2.67/3.0/2.33) · 14B Fast `6.8` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/5812](https://t.me/axisofordinary/5812), [seeallochnaya/928](https://t.me/seeallochnaya/928)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper lacks a comprehensive evaluation of the proposed method, particularly in real-world scenarios. - The paper does not provide a detailed comparison with existing methods, making it difficult to assess the novelty and effectiveness of the proposed approach. - The paper does not discuss potential risks and limitations of the proposed method, such as bias and hallucinations.  ## deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2309.16797"></a>
### Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution

`arxiv:2309.16797` · Retrieval, embeddings, benchmarks · 2023-09-28

- final **-0.25** (conf 0.71, pct 21) · impact +0.36 · DROP
- mean rating (1–10): **4.9** · accept votes **4/7** · percentile rank_avg 40.3 (100=best) · rank in year 34.0 (1=best)
- NAIPv2 `-4.238` · NAIP-v1 `0.704` · SciJudge `-0.132` · DGC-BERT `0.860`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/3.0) · 14B Fast `6.7` Accept
- OpenReviewer `3.0` Reject (S/P/C 2.0/2.0/2.0) · SEA-E `6.0` Accept
- Telegram: [rybolos_channel/1495](https://t.me/rybolos_channel/1495), [axisofordinary/5574](https://t.me/axisofordinary/5574), [j_links/7082](https://t.me/j_links/7082)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The proposed method is not well-motivated. The authors claim that the proposed method is self-referential, but it is not clear what self-referential means. The authors also claim that the proposed method is an interesting future where larger and more capable LLMs could further amplify the gains of our approach. However, it is not clear how the proposed method can be scaled to larger deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="acl-2023.acl-demo.51"></a>
### A System for Answering Simple Questions in Multiple Languages

`acl:2023.acl-demo.51` · Retrieval, embeddings, benchmarks · unknown

- final **-0.37** (conf 0.70, pct 16) · impact -0.96 · DROP · partial fulltext
- mean rating (1–10): **5.2** · accept votes **2/7** · percentile rank_avg 24.9 (100=best) · rank in year 10.0 (1=best)
- NAIPv2 `-3.318` · NAIP-v1 `0.375` · SciJudge `-1.117` · DGC-BERT `0.054`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `4.0` Reject · 7B Fast `5.0` Reject (S/P/C 2.75/3.0/2.5) · 14B Fast `3.7` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [boris_again/2173](https://t.me/boris_again/2173), [abstractDL/233](https://t.me/abstractDL/233)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The method is limited to simple questions and cannot handle multi-hop questions. - The method is limited to one-hop questions and cannot handle complex questions that require reasoning. - The method is limited to questions that can be answered by a single triple in the knowledge graph and cannot handle questions that require multiple triples to answer. - The method is limited to ques deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2304.08467"></a>
### Learning to Compress Prompts with Gist Tokens

`arxiv:2304.08467` · Retrieval, embeddings, benchmarks · 2023-04-17

- final **-0.12** (conf 0.71, pct 29) · impact +0.16 · WATCH
- mean rating (1–10): **5.3** · accept votes **4/7** · percentile rank_avg 44.0 (100=best) · rank in year 30.0 (1=best)
- NAIPv2 `-1.269` · NAIP-v1 `0.576` · SciJudge `1.554` · DGC-BERT `0.801`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `4.8` Reject (S/P/C 2.5/2.75/2.5) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `5.0` Reject
- Telegram: [axisofordinary/4834](https://t.me/axisofordinary/4834)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper lacks a clear motivation for the proposed method. The authors mention that the goal is to compress prompts into a smaller set of tokens, but it is not clear why this is necessary or what the benefits of doing so are. - The evaluation is limited to a single dataset and a single LM architecture. It would be helpful to see how the method performs on other datasets and architec deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2212.14024"></a>
### Demonstrate-Search-Predict: Composing retrieval and language models for knowledge-intensive NLP

`arxiv:2212.14024` · Retrieval, embeddings, benchmarks · 2022-12-28

- final **+0.35** (conf 0.71, pct 78) · impact +0.57 · KEEP
- mean rating (1–10): **6.1** · accept votes **6/7** · percentile rank_avg 58.9 (100=best) · rank in year 6.0 (1=best)
- NAIPv2 `0.195` · NAIP-v1 `0.791` · SciJudge `-1.896` · DGC-BERT `0.669`
- CycleReviewer 8B `5.8` Accept · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `5.7` Reject (S/P/C 2.67/2.67/2.67) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [seeallochnaya/368](https://t.me/seeallochnaya/368), [seeallochnaya/55](https://t.me/seeallochnaya/55), [seeallochnaya/20](https://t.me/seeallochnaya/20)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper lacks a clear motivation for the DSP framework. The authors should provide a more detailed explanation of the limitations of existing retrieval-augmented in-context learning approaches and how DSP addresses these limitations.  The paper does not provide a clear comparison with existing retrieval-augmented in-context learning approaches. The authors should compare DSP with oth deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2212.09741"></a>
### One Embedder, Any Task: Instruction-Finetuned Text Embeddings

`arxiv:2212.09741` · Retrieval, embeddings, benchmarks · 2022-12-19

- final **+0.60** (conf 0.71, pct 97) · impact +1.00 · KEEP
- mean rating (1–10): **6.1** · accept votes **6/7** · percentile rank_avg 70.3 (100=best) · rank in year 1.0 (1=best)
- NAIPv2 `0.333` · NAIP-v1 `0.723` · SciJudge `2.727` · DGC-BERT `0.877`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.5` Accept (S/P/C 3.0/3.25/3.0) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [buckwheat_thoughts/15](https://t.me/buckwheat_thoughts/15), [dealerAI/8](https://t.me/dealerAI/8), [lovedeathtransformers/5427](https://t.me/lovedeathtransformers/5427)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The novelty of the paper is limited. The paper only proposes a new dataset and a new method based on the existing GTR model. The proposed method is not novel, as it is a simple extension of the existing GTR model. 2. The paper does not provide a thorough analysis of the proposed method. For example, the paper does not compare the proposed method with other state-of-the-art methods o deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2206.04615"></a>
### Beyond the Imitation Game: Quantifying and extrapolating the capabilities of language models

`arxiv:2206.04615` · Retrieval, embeddings, benchmarks · 2022-06-09

- final **+0.46** (conf 0.68, pct 89) · impact +2.04 · KEEP
- mean rating (1–10): **6.4** · accept votes **3/6** · percentile rank_avg 67.0 (100=best) · rank in year 2.0 (1=best)
- NAIPv2 `-0.651` · NAIP-v1 `0.794` · SciJudge `3.713` · DGC-BERT `0.391`
- CycleReviewer 8B `6.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.2` Reject · 7B Fast ``  (S/P/C None/None/None) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [rybolos_channel/705](https://t.me/rybolos_channel/705), [rybolos_channel/641](https://t.me/rybolos_channel/641), [rybolos_channel/157](https://t.me/rybolos_channel/157), [j_links/5901](https://t.me/j_links/5901), [j_links/6786](https://t.me/j_links/6786), [tech_priestess/536](https://t.me/tech_priestess/536)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper does not provide a clear definition of what is meant by "beyond the imitation game". It would be helpful to have a more explicit definition of what the benchmark is intended to measure and what it is trying to achieve. - The paper does not provide a clear explanation of how the tasks were selected for the benchmark. It would be helpful to have a more detailed description of deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2205.13147"></a>
### Matryoshka Representation Learning

`arxiv:2205.13147` · Retrieval, embeddings, benchmarks · 2022-05-26

- final **+0.68** (conf 0.71, pct 98) · impact -0.01 · KEEP
- mean rating (1–10): **6.1** · accept votes **6/7** · percentile rank_avg 65.6 (100=best) · rank in year 3.0 (1=best)
- NAIPv2 `2.609` · NAIP-v1 `0.626` · SciJudge `0.610` · DGC-BERT `0.871`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `7.0` Accept (S/P/C 3.25/3.0/3.0) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/3368](https://t.me/gonzo_ML/3368), [doomgrad/757](https://t.me/doomgrad/757), [buckwheat_thoughts/8](https://t.me/buckwheat_thoughts/8), [gonzo_ML/2311](https://t.me/gonzo_ML/2311), [rybolos_channel/1037](https://t.me/rybolos_channel/1037), [gonzo_ML/2037](https://t.me/gonzo_ML/2037), [gonzo_ML/3369](https://t.me/gonzo_ML/3369)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper lacks a clear motivation for the proposed method. The authors should provide more details on why learning a single representation that can be used for multiple downstream tasks is important and how it can benefit the community. - The paper lacks a clear explanation of the proposed method. The authors should provide more details on how the proposed method works and how it ca cyclereviewer-8b.seed1: Weaknesses  - The paper does not provide a clear motivati

<a id="acl-2022.emnlp-main.340"></a>
### Super-NaturalInstructions: Generalization via Declarative Instructions on 1600+ NLP Tasks

`acl:2022.emnlp-main.340` · Retrieval, embeddings, benchmarks · unknown

- final **+0.10** (conf 0.68, pct 51) · impact +0.99 · WATCH · partial fulltext · salvage dr7bf
- mean rating (1–10): **6.0** · accept votes **4/7** · percentile rank_avg 49.4 (100=best) · rank in year 4.0 (1=best)
- NAIPv2 `-2.061` · NAIP-v1 `0.551` · SciJudge `3.130` · DGC-BERT `0.241`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast ``  (S/P/C 2.75/2.75/2.75) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/1585](https://t.me/gonzo_ML/1585)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper does not provide a detailed analysis of the limitations of the benchmark and the model. - The paper does not provide a detailed analysis of the potential biases in the benchmark and the model. - The paper does not provide a detailed analysis of the potential ethical implications of using the benchmark and the model. - The paper does not provide a detailed analysis of the po deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2112.07899"></a>
### Large Dual Encoders Are Generalizable Retrievers

`arxiv:2112.07899` · Retrieval, embeddings, benchmarks · 2021-12-15

- final **+0.36** (conf 0.71, pct 78) · impact +0.23 · KEEP
- mean rating (1–10): **6.3** · accept votes **4/7** · percentile rank_avg 59.0 (100=best) · rank in year 2.0 (1=best)
- NAIPv2 `-0.023` · NAIP-v1 `0.572` · SciJudge `2.128` · DGC-BERT `0.059`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.2` Accept · 7B Fast `6.2` Reject (S/P/C 2.75/3.0/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [dealerAI/8](https://t.me/dealerAI/8), [lovedeathtransformers/5427](https://t.me/lovedeathtransformers/5427)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper does not provide a clear explanation of why scaling up the model size improves the generalization of dual encoders. The authors should provide more analysis and discussion on this aspect. - The paper does not provide a comparison with other models that use different interaction layers, such as multi-vector encoding models and ColBERT. The authors should provide more discuss deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="acl-2022.acl-long.360"></a>
### PRIMERA: Pyramid-based Masked Sentence Pre-training for Multi-document Summarization

`acl:2022.acl-long.360` · Retrieval, embeddings, benchmarks · unknown

- final **-0.13** (conf 0.70, pct 28) · impact +0.69 · WATCH · partial fulltext
- mean rating (1–10): **5.7** · accept votes **3/7** · percentile rank_avg 38.5 (100=best) · rank in year 7.0 (1=best)
- NAIPv2 `-2.773` · NAIP-v1 `0.625` · SciJudge `1.730` · DGC-BERT `0.079`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `3.8` Reject · 7B Fast `5.7` Reject (S/P/C 2.67/3.0/2.67) · 14B Fast `6.0` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/1507](https://t.me/gonzo_ML/1507)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper does not discuss the limitations of the proposed method. It would be helpful to discuss the potential limitations and future work. - The paper does not provide any qualitative analysis of the results. It would be helpful to provide some examples of the generated summaries and compare them with the ground truth summaries. - The paper does not discuss the computational cost o deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2101.02235"></a>
### Did Aristotle Use a Laptop? A Question Answering Benchmark with Implicit Reasoning Strategies

`arxiv:2101.02235` · Retrieval, embeddings, benchmarks · 2021-01-06

- final **+0.06** (conf 0.71, pct 47) · impact +0.15 · WATCH
- mean rating (1–10): **6.0** · accept votes **5/7** · percentile rank_avg 51.1 (100=best) · rank in year 4.0 (1=best)
- NAIPv2 `-2.572` · NAIP-v1 `0.593` · SciJudge `1.722` · DGC-BERT `0.469`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `4.8` Reject (S/P/C 2.5/2.5/2.25) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [gonzo_ML/1585](https://t.me/gonzo_ML/1585)
- Weaknesses: cyclereviewer-8b: Weaknesses  The authors should provide more details about the baselines and their performance. In particular, it would be helpful to know how the baselines are trained and evaluated, and what types of reasoning they are able to perform.  ### Questions  1. What are the main differences between the proposed dataset and existing multi-hop reasoning datasets? 2. How does the proposed dataset compare t deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2608.23875"></a>
### AI Finds A Way

`arxiv:2608.23875` · Agents, open-endedness, AGI · 2026-08-24

- final **-0.68** (conf 0.71, pct 4) · impact -0.56 · DROP
- mean rating (1–10): **4.7** · accept votes **2/7** · percentile rank_avg 24.6 (100=best) · rank in year 70.0 (1=best)
- NAIPv2 `-2.221` · NAIP-v1 `0.558` · SciJudge `-2.715` · DGC-BERT `0.067`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `4.7` Reject (S/P/C 2.0/2.33/2.0) · 14B Fast `3.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/5974](https://t.me/gonzo_ML/5974), [j_links/8501](https://t.me/j_links/8501)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper lacks a clear and concise summary of the main contributions and findings. - The paper does not provide a clear and well-defined research question or hypothesis. - The paper does not provide a clear and well-defined methodology for collecting and analyzing the anecdotes. - The paper does not provide a clear and well-defined evaluation or validation of the findings. - The pap deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2608.19197"></a>
### SPADE: Self-Play in Adaptive Synthetic Executable Environments

`arxiv:2608.19197` · Agents, open-endedness, AGI · 2026-08-19

- final **+0.45** (conf 0.71, pct 88) · impact +0.25 · KEEP
- mean rating (1–10): **7.0** · accept votes **6/7** · percentile rank_avg 72.9 (100=best) · rank in year 6.0 (1=best)
- NAIPv2 `0.183` · NAIP-v1 `0.656` · SciJudge `0.132` · DGC-BERT `0.078`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `7.0` Accept (S/P/C 3.0/3.0/3.0) · 14B Fast `7.0` Accept
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/4.0) · SEA-E `7.0` Accept
- Telegram: [axisofordinary/9061](https://t.me/axisofordinary/9061)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper lacks a clear comparison with existing methods in the field, making it difficult to assess the novelty and significance of the proposed approach.  2. The paper does not provide a detailed explanation of the limitations of the proposed approach, which is important for understanding the potential applications and limitations of the method.  3. The paper does not provide a cl deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2608.08311"></a>
### Ouroboros: A Self-Developing Frontier Coding Agent with Reviewed Core Evolution

`arxiv:2608.08311` · Agents, open-endedness, AGI · 2026-08-08

- final **-0.16** (conf 0.71, pct 25) · impact -0.75 · WATCH
- mean rating (1–10): **6.2** · accept votes **3/7** · percentile rank_avg 40.4 (100=best) · rank in year 63.0 (1=best)
- NAIPv2 `-1.249` · NAIP-v1 `0.368` · SciJudge `0.816` · DGC-BERT `0.012`
- CycleReviewer 8B `4.0` Reject · 70B `` 
- DeepReviewer 7B Std `3.0` Reject · 7B Fast `7.5` Accept (S/P/C 3.5/3.25/3.75) · 14B Fast `5.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `8.0` Accept
- Telegram: [lovedeathtransformers/10949](https://t.me/lovedeathtransformers/10949), [abstractDL/439](https://t.me/abstractDL/439)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper lacks clarity in explaining the methodology and evaluation of the agent. The paper does not provide enough details on how the agent's performance is evaluated, and how the benchmarks are used to assess the agent's capabilities. The paper also does not provide enough information on the agent's limitations and potential biases. Additionally, the paper does not discuss the poten deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2607.13104"></a>
### Self-Improvements in Modern Agentic Systems: A Survey

`arxiv:2607.13104` · Agents, open-endedness, AGI · 2026-07-14

- final **+0.29** (conf 0.71, pct 74) · impact +0.91 · KEEP
- mean rating (1–10): **6.3** · accept votes **6/7** · percentile rank_avg 65.7 (100=best) · rank in year 18.0 (1=best)
- NAIPv2 `0.084` · NAIP-v1 `0.655` · SciJudge `2.386` · DGC-BERT `0.010`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `7.0` Accept · 7B Fast `7.0` Accept (S/P/C 3.25/3.0/2.75) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `5.0` Accept
- Telegram: [gonzo_ML/5772](https://t.me/gonzo_ML/5772)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper is a survey, and it does not present any new research results. The authors do not provide any new insights or perspectives on the field of self-improving agents. The paper is also quite long and dense, which may make it difficult for readers to follow.  ## Questions  The paper does not provide any new insights or perspectives on the field of self-improving agents. The authors deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2605.13821"></a>
### Harnessing Agentic Evolution

`arxiv:2605.13821` · Agents, open-endedness, AGI · 2026-05-13

- final **+0.04** (conf 0.71, pct 42) · impact +0.28 · WATCH
- mean rating (1–10): **6.3** · accept votes **5/7** · percentile rank_avg 61.2 (100=best) · rank in year 28.0 (1=best)
- NAIPv2 `-0.344` · NAIP-v1 `0.618` · SciJudge `0.831` · DGC-BERT `0.625`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `7.0` Accept (S/P/C 3.0/3.25/3.0) · 14B Fast `6.5` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper does not provide a detailed discussion of the limitations of the proposed approach. - The paper does not provide a discussion of the potential risks and challenges associated with the proposed approach. - The paper does not provide a discussion of the potential applications of the proposed approach. - The paper does not provide a discussion of the potential future work.  ## deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2603.19461"></a>
### Hyperagents

`arxiv:2603.19461` · Agents, open-endedness, AGI · 2026-03-19

- final **+0.04** (conf 0.71, pct 43) · impact +1.00 · WATCH
- mean rating (1–10): **6.2** · accept votes **6/7** · percentile rank_avg 64.5 (100=best) · rank in year 22.0 (1=best)
- NAIPv2 `-0.993` · NAIP-v1 `0.700` · SciJudge `1.850` · DGC-BERT `0.445`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.5` Accept (S/P/C 2.75/2.75/2.5) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/5042](https://t.me/gonzo_ML/5042), [rybolos_channel/1775](https://t.me/rybolos_channel/1775), [axisofordinary/8281](https://t.me/axisofordinary/8281), [gonzo_ML/5032](https://t.me/gonzo_ML/5032), [boris_again/3821](https://t.me/boris_again/3821)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper lacks a theoretical analysis of the proposed method. - The paper lacks a comparison with other self-improvement algorithms. - The paper lacks a discussion of the limitations of the proposed method.  ### Questions  1. How does the proposed method compare to other self-improvement algorithms? 2. What are the limitations of the proposed method? 3. Can the proposed method be ap deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2602.07755"></a>
### Learning to Continually Learn via Meta-learning Agentic Memory Designs

`arxiv:2602.07755` · Agents, open-endedness, AGI · 2026-02-08

- final **+0.14** (conf 0.71, pct 56) · impact +0.13 · WATCH
- mean rating (1–10): **6.3** · accept votes **6/7** · percentile rank_avg 56.5 (100=best) · rank in year 36.0 (1=best)
- NAIPv2 `-0.724` · NAIP-v1 `0.525` · SciJudge `1.570` · DGC-BERT `0.013`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.5` Accept (S/P/C 2.75/3.0/2.75) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/8164](https://t.me/axisofordinary/8164)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper lacks a clear definition of the search space for memory designs. The authors mention that the search space is defined as code, but it is unclear what specific aspects of memory design are being explored. - The paper does not provide a thorough analysis of the limitations of the proposed method. For example, it is not clear how ALMA would perform in more complex or dynamic e deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2601.21557"></a>
### Meta Context Engineering via Agentic Skill Evolution

`arxiv:2601.21557` · Agents, open-endedness, AGI · 2026-01-29

- final **+0.00** (conf 0.71, pct 39) · impact +0.04 · WATCH
- mean rating (1–10): **5.5** · accept votes **5/7** · percentile rank_avg 52.5 (100=best) · rank in year 49.0 (1=best)
- NAIPv2 `-0.715` · NAIP-v1 `0.563` · SciJudge `0.796` · DGC-BERT `0.512`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `7.0` Accept · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/3.0) · 14B Fast `5.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper is not well-organized. The authors should consider reorganizing the paper to make it more coherent and easier to follow. 2. The paper lacks sufficient technical details. The authors should provide more technical details about the proposed method and the experimental setup. 3. The paper lacks sufficient experimental results. The authors should provide more experimental resu deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2601.07055"></a>
### Dr. Zero: Self-Evolving Search Agents without Training Data

`arxiv:2601.07055` · Agents, open-endedness, AGI · 2026-01-11

- final **+0.06** (conf 0.71, pct 46) · impact +0.57 · WATCH
- mean rating (1–10): **6.0** · accept votes **5/7** · percentile rank_avg 56.3 (100=best) · rank in year 39.0 (1=best)
- NAIPv2 `-0.861` · NAIP-v1 `0.525` · SciJudge `2.974` · DGC-BERT `0.679`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `5.8` Reject · 7B Fast `6.5` Accept (S/P/C 2.75/3.0/2.75) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/9061](https://t.me/axisofordinary/9061), [axisofordinary/8089](https://t.me/axisofordinary/8089)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper lacks a detailed description of the methodology, making it difficult to understand the specific techniques used in the framework. 2. The paper does not provide a clear explanation of the advantages of the proposed framework over existing methods. 3. The paper does not discuss the potential limitations of the proposed framework. 4. The paper does not provide a clear explana deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2601.03192"></a>
### MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory

`arxiv:2601.03192` · Agents, open-endedness, AGI · 2026-01-06

- final **+0.54** (conf 0.71, pct 94) · impact +1.38 · KEEP
- mean rating (1–10): **6.4** · accept votes **6/7** · percentile rank_avg 75.5 (100=best) · rank in year 3.0 (1=best)
- NAIPv2 `1.841` · NAIP-v1 `0.729` · SciJudge `2.600` · DGC-BERT `0.796`
- CycleReviewer 8B `5.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `7.5` Accept (S/P/C 3.25/3.25/3.25) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/9061](https://t.me/axisofordinary/9061), [axisofordinary/8089](https://t.me/axisofordinary/8089)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The novelty is limited. The idea of optimizing the retrieval policy via RL is not new, and the method is quite similar to the existing methods (e.g., (1)). The novelty of this work is mainly the application of the idea to LLM agents. - The evaluation is not sufficient. The method is evaluated on only a few benchmarks, and the results are not convincing enough to support the claim of  deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2512.18746"></a>
### MemEvolve: Meta-Evolution of Agent Memory Systems

`arxiv:2512.18746` · Agents, open-endedness, AGI · 2025-12-21

- final **+0.45** (conf 0.71, pct 88) · impact +0.04 · KEEP
- mean rating (1–10): **6.2** · accept votes **5/7** · percentile rank_avg 60.0 (100=best) · rank in year 34.0 (1=best)
- NAIPv2 `-0.453` · NAIP-v1 `0.626` · SciJudge `-0.581` · DGC-BERT `0.161`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `7.0` Accept · 7B Fast `7.0` Accept (S/P/C 3.0/3.25/3.25) · 14B Fast `6.2` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper focuses on a specific aspect of LLM-based agents, namely the memory architecture, and does not explore other important aspects such as the LLM itself or the environment interactions. This narrow focus may limit the generalizability of the proposed framework. - The paper does not provide a thorough analysis of the limitations of the proposed framework. For example, it is not deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2512.18552"></a>
### Toward Training Superintelligent Software Agents through Self-Play SWE-RL

`arxiv:2512.18552` · Agents, open-endedness, AGI · 2025-12-21

- final **-0.33** (conf 0.71, pct 17) · impact -0.56 · DROP
- mean rating (1–10): **5.7** · accept votes **3/7** · percentile rank_avg 36.7 (100=best) · rank in year 70.0 (1=best)
- NAIPv2 `-1.922` · NAIP-v1 `0.484` · SciJudge `-0.837` · DGC-BERT `0.233`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `4.8` Reject (S/P/C 2.25/2.75/2.25) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/9061](https://t.me/axisofordinary/9061), [data_secrets/8572](https://t.me/data_secrets/8572), [axisofordinary/8028](https://t.me/axisofordinary/8028)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper lacks a clear explanation of the motivation for the proposed method. What are the benefits of self-play SWE-RL (SSR) compared to existing methods? - The paper does not provide a detailed explanation of the experimental setup, including the data used, the evaluation metrics, and the baselines used for comparison. More details are needed to understand the experimental design  cyclereviewer-8b.seed1: Weaknesses  1. The paper does not provide a clear explana

<a id="arxiv-2512.18160"></a>
### Propose, Solve, Verify: Self-Play Through Formal Verification

`arxiv:2512.18160` · Agents, open-endedness, AGI · 2025-12-20

- final **+0.11** (conf 0.71, pct 52) · impact -0.48 · WATCH
- mean rating (1–10): **6.1** · accept votes **5/7** · percentile rank_avg 54.3 (100=best) · rank in year 43.0 (1=best)
- NAIPv2 `-1.147` · NAIP-v1 `0.551` · SciJudge `-2.296` · DGC-BERT `0.943`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `6.5` Accept (S/P/C 2.75/3.25/2.5) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/9061](https://t.me/axisofordinary/9061), [axisofordinary/8073](https://t.me/axisofordinary/8073)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper lacks a clear explanation of how the proposer model is trained. The authors mention that the proposer is updated using the data pool, but do not provide details on the training process. - The paper does not provide a clear explanation of how the difficulty-aware proposer works. The authors mention that the proposer generates problems in the form of formal specifications, bu deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2511.15593"></a>
### What Does It Take to Be a Good AI Research Agent? Studying the Role of Ideation Diversity

`arxiv:2511.15593` · Agents, open-endedness, AGI · 2025-11-19

- final **-0.59** (conf 0.71, pct 8) · impact -1.50 · DROP
- mean rating (1–10): **5.3** · accept votes **2/7** · percentile rank_avg 25.5 (100=best) · rank in year 77.0 (1=best)
- NAIPv2 `-2.432` · NAIP-v1 `0.436` · SciJudge `-5.377` · DGC-BERT `0.401`
- CycleReviewer 8B `6.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.5` Reject · 7B Fast `5.8` Accept (S/P/C 2.75/3.0/2.75) · 14B Fast `4.8` Reject
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `5.0` Accept
- Telegram: [rybolos_channel/1703](https://t.me/rybolos_channel/1703), [gonzo_ML/4261](https://t.me/gonzo_ML/4261), [rybolos_channel/1670](https://t.me/rybolos_channel/1670)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper only considers a single benchmark (MLE-bench) and a single type of agent (AI research agents). It would be interesting to see if the findings generalize to other benchmarks and types of agents. - The paper does not provide a clear definition of ideation diversity and how it is measured. It would be helpful to provide a more formal definition and description of the methodolo deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2508.16204"></a>
### Competition and Attraction Improve Model Fusion

`arxiv:2508.16204` · Agents, open-endedness, AGI · 2025-08-22

- final **+0.04** (conf 0.71, pct 43) · impact -1.07 · WATCH
- mean rating (1–10): **5.8** · accept votes **4/7** · percentile rank_avg 47.4 (100=best) · rank in year 61.0 (1=best)
- NAIPv2 `0.670` · NAIP-v1 `0.460` · SciJudge `-3.828` · DGC-BERT `0.853`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.8` Reject · 7B Fast `6.2` Reject (S/P/C 2.75/2.75/2.5) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/7621](https://t.me/axisofordinary/7621), [data_secrets/7685](https://t.me/data_secrets/7685)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The novelty of the proposed method is limited. The idea of model merging using evolutionary algorithms has been explored in previous works (1,2). The proposed method is an extension of these works with some modifications. 2. The experiments are not comprehensive. The proposed method is evaluated on three tasks, but the results are not compared to the state-of-the-art methods on thes deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2507.18074"></a>
### AlphaGo Moment for Model Architecture Discovery

`arxiv:2507.18074` · Agents, open-endedness, AGI · 2025-07-24

- final **-0.32** (conf 0.71, pct 19) · impact +1.12 · WATCH
- mean rating (1–10): **5.2** · accept votes **3/7** · percentile rank_avg 41.7 (100=best) · rank in year 67.0 (1=best)
- NAIPv2 `-0.628` · NAIP-v1 `0.658` · SciJudge `2.782` · DGC-BERT `0.119`
- CycleReviewer 8B `5.2` Accept · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `5.0` Reject (S/P/C 2.75/2.75/2.5) · 14B Fast `5.5` Reject
- OpenReviewer `5.0` Reject (S/P/C 2.0/3.0/2.0) · SEA-E `5.0` Accept
- Telegram: [rybolos_channel/1549](https://t.me/rybolos_channel/1549), [gonzo_ML/3874](https://t.me/gonzo_ML/3874), [data_secrets/7461](https://t.me/data_secrets/7461)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper proposes a framework for neural architecture search using large language models, but it does not provide a detailed evaluation of the framework's performance compared to other neural architecture search methods. The paper also does not provide a detailed analysis of the strengths and weaknesses of the framework, and it does not discuss potential limitations and future work.   deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2505.22954"></a>
### Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents

`arxiv:2505.22954` · Agents, open-endedness, AGI · 2025-05-29

- final **+0.03** (conf 0.71, pct 42) · impact +1.10 · WATCH
- mean rating (1–10): **6.0** · accept votes **4/7** · percentile rank_avg 55.9 (100=best) · rank in year 42.0 (1=best)
- NAIPv2 `-0.615` · NAIP-v1 `0.709` · SciJudge `1.646` · DGC-BERT `0.376`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.2` Reject · 7B Fast `5.8` Accept (S/P/C 2.5/2.75/2.25) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [data_secrets/7688](https://t.me/data_secrets/7688), [lovedeathtransformers/9379](https://t.me/lovedeathtransformers/9379), [data_secrets/7012](https://t.me/data_secrets/7012), [axisofordinary/7267](https://t.me/axisofordinary/7267), [gonzo_ML/3678](https://t.me/gonzo_ML/3678), [gonzo_ML/3681](https://t.me/gonzo_ML/3681)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper proposes a novel approach to self-improving AI systems that uses a combination of evolutionary algorithms and empirical validation to improve its performance on coding benchmarks. However, the paper does not provide a detailed analysis of the limitations of this approach. For example, it is not clear how the DGM would perform on more complex coding tasks or on tasks that requ deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="doi-10.21203-rs.3.rs-6688473-v1"></a>
### Self-Programming AI: Code-Learning Agents for Autonomous Refactoring and Architectural Evolution

`doi:10.21203/rs.3.rs-6688473/v1` · Agents, open-endedness, AGI · 2025-05-20

- final **-0.81** (conf 0.71, pct 1) · impact -0.34 · DROP
- mean rating (1–10): **4.5** · accept votes **2/7** · percentile rank_avg 19.3 (100=best) · rank in year 78.0 (1=best)
- NAIPv2 `-2.812` · NAIP-v1 `0.604` · SciJudge `-2.483` · DGC-BERT `0.009`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `4.0` Reject · 7B Fast `4.0` Reject (S/P/C 2.25/2.75/1.75) · 14B Fast `3.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `5.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper lacks a comprehensive literature review. The authors should include more relevant works in the related work section to provide a more thorough background and context for their proposed method. 2. The evaluation is limited to five simple tasks. The authors should consider adding more complex tasks to demonstrate the effectiveness of their method. 3. The paper lacks a discus deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2502.15840"></a>
### Vending-Bench: A Benchmark for Long-Term Coherence of Autonomous Agents

`arxiv:2502.15840` · Agents, open-endedness, AGI · 2025-02-20

- final **-0.37** (conf 0.71, pct 15) · impact -0.32 · DROP
- mean rating (1–10): **4.5** · accept votes **3/7** · percentile rank_avg 30.9 (100=best) · rank in year 76.0 (1=best)
- NAIPv2 `-1.640` · NAIP-v1 `0.395` · SciJudge `1.397` · DGC-BERT `0.032`
- CycleReviewer 8B `1.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `6.3` Accept (S/P/C 2.67/3.0/2.67) · 14B Fast `4.0` Reject
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [lovedeathtransformers/9266](https://t.me/lovedeathtransformers/9266), [AGI_and_RL/1055](https://t.me/AGI_and_RL/1055)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper lacks a clear and well-defined research question. The authors do not provide a clear motivation for the benchmark or explain why it is important to test the long-term performance of LLMs. Additionally, the paper does not provide a clear definition of what is meant by "long-term coherence" and how it is measured.  The paper lacks a clear and well-defined methodology. The autho deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2408.08435"></a>
### Automated Design of Agentic Systems

`arxiv:2408.08435` · Agents, open-endedness, AGI · 2024-08-15

- final **+0.09** (conf 0.71, pct 49) · impact +1.11 · WATCH
- mean rating (1–10): **6.2** · accept votes **4/7** · percentile rank_avg 54.6 (100=best) · rank in year 15.0 (1=best)
- NAIPv2 `-2.412` · NAIP-v1 `0.655` · SciJudge `3.114` · DGC-BERT `0.327`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `5.5` Reject (S/P/C 2.5/3.0/2.5) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [knowledge_accumulator/231](https://t.me/knowledge_accumulator/231)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper does not provide a detailed analysis of the limitations of the proposed approach. - The paper does not discuss the potential risks and challenges of automating the design of agentic systems. - The paper does not provide a detailed comparison with other approaches to automating the design of agentic systems.  ### Questions  - What are the limitations of the proposed approach cyclereviewer-8b.seed1: Weaknesses  - The authors do not provide any analysis of 

<a id="arxiv-2407.00695"></a>
### Learning Formal Mathematics From Intrinsic Motivation

`arxiv:2407.00695` · Agents, open-endedness, AGI · 2024-06-30

- final **+0.44** (conf 0.71, pct 87) · impact -0.19 · KEEP
- mean rating (1–10): **6.4** · accept votes **3/7** · percentile rank_avg 59.0 (100=best) · rank in year 8.0 (1=best)
- NAIPv2 `-0.889` · NAIP-v1 `0.455` · SciJudge `1.298` · DGC-BERT `0.242`
- CycleReviewer 8B `6.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Reject · 7B Fast `5.7` Reject (S/P/C 2.67/2.67/2.67) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/2.0/3.0) · SEA-E `7.0` Accept
- Telegram: [axisofordinary/6466](https://t.me/axisofordinary/6466), [j_links/7590](https://t.me/j_links/7590)
- Weaknesses: cyclereviewer-8b: Weaknesses  The authors claim that their method can generate conjectures and prove them without any prior knowledge. However, the method relies on the type-directed synthesis algorithm to generate conjectures, which requires prior knowledge of the mathematical domain. The authors should clarify this point.  The authors claim that their method can generate conjectures and prove them without any hum deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2406.04268"></a>
### Open-Endedness is Essential for Artificial Superhuman Intelligence

`arxiv:2406.04268` · Agents, open-endedness, AGI · 2024-06-06

- final **-0.36** (conf 0.71, pct 16) · impact +0.33 · DROP
- mean rating (1–10): **5.5** · accept votes **2/7** · percentile rank_avg 36.7 (100=best) · rank in year 36.0 (1=best)
- NAIPv2 `-2.396` · NAIP-v1 `0.614` · SciJudge `0.634` · DGC-BERT `0.008`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.2` Reject · 7B Fast `4.8` Reject (S/P/C 2.75/2.25/2.25) · 14B Fast `4.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/4.0/3.0) · SEA-E `7.0` Accept
- Telegram: [rybolos_channel/1195](https://t.me/rybolos_channel/1195), [gonzo_ML/2746](https://t.me/gonzo_ML/2746), [gonzo_ML/2743](https://t.me/gonzo_ML/2743), [axisofordinary/6414](https://t.me/axisofordinary/6414)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper does not provide any new experimental results or empirical evidence to support its claims.  The paper does not provide a clear roadmap or plan for how to achieve open-endedness in AI systems.  The paper does not discuss the potential challenges and limitations of achieving open-endedness in AI systems.  ### Questions  How do you plan to achieve open-endedness in AI systems?   cyclereviewer-8b.seed1: Weaknesses  1. The paper does not provide a clear roadmap

<a id="openreview-pOoKI3ouv1"></a>
### Robust agents learn causal world models (ICLR 2024 best paper)

`openreview:pOoKI3ouv1` · Agents, open-endedness, AGI · unknown

- final **+0.72** (conf 0.71, pct 99) · impact +0.96 · KEEP
- mean rating (1–10): **7.1** · accept votes **6/7** · percentile rank_avg 74.9 (100=best) · rank in year 1.0 (1=best)
- NAIPv2 `-0.457` · NAIP-v1 `0.615` · SciJudge `2.534` · DGC-BERT `0.221`
- CycleReviewer 8B `8.0` Accept · 70B `` 
- DeepReviewer 7B Std `8.0` Accept · 7B Fast `7.0` Accept (S/P/C 3.0/3.0/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/4.0/3.0) · SEA-E `8.0` Accept
- Telegram: [j_links/7476](https://t.me/j_links/7476)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper could benefit from more examples and illustrations to help readers understand the concepts and results - The paper could also benefit from a more detailed discussion of the limitations of the results  ### Questions  - How do the results of this paper relate to existing work on causal reasoning and generalization? - How do the results of this paper relate to other approaches deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="doi-10.1038-s42256-023-00754-x"></a>
### A social path to human-like artificial intelligence

`doi:10.1038/s42256-023-00754-x` · Agents, open-endedness, AGI · 2023-11-17

- final **-0.64** (conf 0.71, pct 6) · impact -1.89 · DROP
- mean rating (1–10): **4.5** · accept votes **1/7** · percentile rank_avg 17.8 (100=best) · rank in year 46.0 (1=best)
- NAIPv2 `-4.184` · NAIP-v1 `0.438` · SciJudge `-10.641` · DGC-BERT `0.050`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.8` Reject · 7B Fast `5.0` Reject (S/P/C 2.0/3.0/2.0) · 14B Fast `5.2` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/2.0/3.0) · SEA-E `3.0` Reject
- Telegram: [dtulinov/647](https://t.me/dtulinov/647)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper is more of a perspective than a research paper, and it is not clear what the main contribution is. - The authors do not provide any concrete examples of how social interactions can be used to improve AI systems. - The paper does not provide a clear roadmap for how to integrate social interactions into AI systems.  ### Questions  - What are the concrete examples of how socia deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2311.02462"></a>
### Levels of AGI for Operationalizing Progress on the Path to AGI

`arxiv:2311.02462` · Agents, open-endedness, AGI · 2023-11-04

- final **-0.42** (conf 0.71, pct 12) · impact -0.25 · DROP
- mean rating (1–10): **5.5** · accept votes **2/7** · percentile rank_avg 31.6 (100=best) · rank in year 42.0 (1=best)
- NAIPv2 `-2.020` · NAIP-v1 `0.513` · SciJudge `0.813` · DGC-BERT `0.009`
- CycleReviewer 8B `5.8` Reject · 70B `` 
- DeepReviewer 7B Std `4.2` Reject · 7B Fast `4.8` Reject (S/P/C 2.75/2.75/2.25) · 14B Fast `4.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [knowledge_accumulator/241](https://t.me/knowledge_accumulator/241), [gonzo_ML/2744](https://t.me/gonzo_ML/2744), [axisofordinary/5714](https://t.me/axisofordinary/5714), [seeallochnaya/802](https://t.me/seeallochnaya/802)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper lacks empirical evaluation of the proposed framework. The authors do not provide any empirical results to support the claims made in the paper. The paper is more of a conceptual paper that proposes a framework for classifying AGI models and their precursors. The framework is based on six principles that a useful ontology for AGI should satisfy. The authors also discuss the ch deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2311.00344"></a>
### A Definition of Open-Ended Learning Problems for Goal-Conditioned Agents

`arxiv:2311.00344` · Agents, open-endedness, AGI · 2023-11-01

- final **-0.12** (conf 0.71, pct 28) · impact -1.56 · WATCH
- mean rating (1–10): **5.5** · accept votes **3/7** · percentile rank_avg 30.0 (100=best) · rank in year 43.0 (1=best)
- NAIPv2 `-1.090` · NAIP-v1 `0.426` · SciJudge `-6.302` · DGC-BERT `0.007`
- CycleReviewer 8B `4.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.2` Reject · 7B Fast `6.5` Accept (S/P/C 3.0/3.0/3.0) · 14B Fast `4.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/2743](https://t.me/gonzo_ML/2743)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper lacks a clear methodology for evaluating open-ended learning agents and comparing their performance. The authors acknowledge this limitation and suggest that future work should focus on characterizing a goal discovery process and introducing performance measures for various capabilities. However, this leaves the paper without a clear evaluation or experimental validation of t deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-1905.10985"></a>
### AI-GAs: AI-generating algorithms, an alternate paradigm for producing general artificial intelligence

`arxiv:1905.10985` · Agents, open-endedness, AGI · 2019-05-27

- final **-0.45** (conf 0.71, pct 11) · impact -0.45 · DROP
- mean rating (1–10): **4.3** · accept votes **1/7** · percentile rank_avg 24.5 (100=best) · rank in year 3.0 (1=best)
- NAIPv2 `-2.426` · NAIP-v1 `0.621` · SciJudge `-3.201` · DGC-BERT `0.007`
- CycleReviewer 8B `1.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `6.5` Reject (S/P/C 2.75/2.75/2.75) · 14B Fast `3.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `5.0` Reject
- Telegram: [knowledge_accumulator/94](https://t.me/knowledge_accumulator/94), [gonzo_ML/450](https://t.me/gonzo_ML/450), [gonzo_ML/3680](https://t.me/gonzo_ML/3680)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper is more of an opinion piece rather than a research paper. It does not provide a clear research question, methodology, or evaluation criteria. The paper does not provide any concrete examples or experiments to support the proposed ideas. The paper is also not well-organized and lacks a clear structure. The writing is not clear and concise, and the paper contains many typos and deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2609.01437"></a>
### HarnessDev: Can LLMs Create and Evolve Their Own Agent Harness?

`arxiv:2609.01437` · Harness · 2026-09-01

- final **-0.07** (conf 0.71, pct 32) · impact -0.15 · WATCH
- mean rating (1–10): **6.6** · accept votes **4/7** · percentile rank_avg 51.2 (100=best) · rank in year 50.0 (1=best)
- NAIPv2 `-1.231` · NAIP-v1 `0.617` · SciJudge `-1.947` · DGC-BERT `0.023`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `4.2` Reject · 7B Fast `6.0` Accept (S/P/C 2.5/2.75/2.75) · 14B Fast `7.0` Accept
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/4.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper lacks novelty. The idea of evaluating the ability of LLMs to develop their own agent harness is not new, and there have been several previous works on this topic. For example, the Meta-Agent Challenge (Lu et al., 2023) directly evaluates the development ability of LLMs. The paper does not clearly explain why the proposed benchmark is better than these previous works.  2. T cyclereviewer-8b.seed1: Weaknesses  - The paper only reports results for six crea

<a id="arxiv-2606.01770"></a>
### Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System Deployment on Open-Ended Task Streams

`arxiv:2606.01770` · Harness · 2026-06-01

- final **+0.26** (conf 0.71, pct 68) · impact -0.48 · KEEP
- mean rating (1–10): **6.3** · accept votes **5/7** · percentile rank_avg 54.6 (100=best) · rank in year 41.0 (1=best)
- NAIPv2 `0.798` · NAIP-v1 `0.486` · SciJudge `-0.345` · DGC-BERT `0.032`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `7.0` Accept (S/P/C 3.25/3.25/3.25) · 14B Fast `6.7` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper is mostly focused on the technical details of the proposed framework, but it would be helpful to provide more context on how this work can be applied in real-world scenarios. For example, how can this framework be used in a real-world deployment setting? What are the practical challenges that need to be addressed?  ### Questions  1. The authors mention that the proposed frame deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2604.25850"></a>
### Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses

`arxiv:2604.25850` · Harness · 2026-04-28

- final **+0.09** (conf 0.71, pct 50) · impact -0.18 · WATCH
- mean rating (1–10): **5.9** · accept votes **3/7** · percentile rank_avg 57.0 (100=best) · rank in year 34.0 (1=best)
- NAIPv2 `1.099` · NAIP-v1 `0.507` · SciJudge `0.536` · DGC-BERT `0.459`
- CycleReviewer 8B `5.2` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `4.8` Reject (S/P/C 2.75/2.5/2.5) · 14B Fast `6.5` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper lacks a clear motivation for the proposed approach. The authors should explain why the three components of AHE are necessary, and how they address the challenges of harness engineering. - The paper lacks a clear explanation of the experimental setup. The authors should provide more details on the specific models and datasets used in the experiments, as well as the specific  deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2604.19341"></a>
### Structured Scaling of AI Discovery Across Diverse Scientific Domains

`arxiv:2604.19341` · Harness · 2026-04-21

- final **+0.70** (conf 0.71, pct 99) · impact +1.53 · KEEP
- mean rating (1–10): **6.6** · accept votes **6/7** · percentile rank_avg 74.3 (100=best) · rank in year 4.0 (1=best)
- NAIPv2 `-0.211` · NAIP-v1 `0.596` · SciJudge `3.677` · DGC-BERT `0.518`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `10.0` Accept · 7B Fast `8.0` Accept (S/P/C 3.5/3.5/3.5) · 14B Fast `7.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  I have the following concerns:  1. The paper does not clearly explain how the proposal constructor $\Phi$ is implemented. The authors mention that it is a graph-based variant of the PUCT rule, but they do not provide any details. It would be helpful to include a more detailed description of how $\Phi$ is implemented.  2. The paper does not provide any analysis of the computational effi cyclereviewer-8b.seed1: Weaknesses  1. The novelty of the paper is limited. The p

<a id="arxiv-2604.08224"></a>
### Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering

`arxiv:2604.08224` · Harness · 2026-04-09

- final **-0.27** (conf 0.71, pct 20) · impact +1.26 · WATCH
- mean rating (1–10): **5.8** · accept votes **3/7** · percentile rank_avg 49.8 (100=best) · rank in year 54.0 (1=best)
- NAIPv2 `-0.827` · NAIP-v1 `0.681` · SciJudge `3.109` · DGC-BERT `0.030`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `5.2` Reject (S/P/C 3.0/3.0/2.25) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [gonzo_ML/5479](https://t.me/gonzo_ML/5479)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper does not provide a clear and concise summary of the main contributions of the paper. The abstract and introduction are quite long and do not clearly state the main contributions of the paper.  The paper does not provide a clear and concise summary of the related work. The related work section is quite long and does not clearly summarize the main contributions of other papers  deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2603.28052"></a>
### Meta-Harness: End-to-End Optimization of Model Harnesses

`arxiv:2603.28052` · Harness · 2026-03-30

- final **+0.38** (conf 0.71, pct 80) · impact -0.26 · KEEP
- mean rating (1–10): **6.0** · accept votes **6/7** · percentile rank_avg 60.4 (100=best) · rank in year 29.0 (1=best)
- NAIPv2 `0.213` · NAIP-v1 `0.458` · SciJudge `1.148` · DGC-BERT `0.909`
- CycleReviewer 8B `4.8` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.0` Accept (S/P/C 3.0/3.0/3.0) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [lovedeathtransformers/10644](https://t.me/lovedeathtransformers/10644), [gonzo_ML/5093](https://t.me/gonzo_ML/5093)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The proposed method is limited to the LLM-based coding agent. It is not clear whether the proposed method can be generalized to other types of agents. - The proposed method requires a large amount of memory to store the source code, scores, and execution traces of all prior candidates. It is not clear whether the proposed method can be applied to resource-constrained environments. -  deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2607.23379"></a>
### When Activation Oracles Learn Not to Read: Concept-Specific Blind Spots in Fine-Tuned Oracles

`arxiv:2607.23379` · AI safety and consciousness · 2026-07-25

- final **+0.06** (conf 0.71, pct 46) · impact -0.95 · WATCH
- mean rating (1–10): **6.5** · accept votes **4/7** · percentile rank_avg 50.8 (100=best) · rank in year 51.0 (1=best)
- NAIPv2 `-0.958` · NAIP-v1 `0.502` · SciJudge `-3.611` · DGC-BERT `0.398`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `7.0` Accept (S/P/C 3.0/3.0/3.0) · 14B Fast `7.0` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/4.0/3.0) · SEA-E `6.0` Accept
- Telegram: [tech_priestess/2709](https://t.me/tech_priestess/2709)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper only studies a single model architecture (Qwen3-8B) and a single training setup (Taboo Word Guessing). It would be good to see if the findings generalize to other model architectures and training setups. - The paper only studies a single hidden concept (e.g., "leaf") per subject model. It would be good to see if the findings generalize to multiple hidden concepts per subjec deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2603.19426"></a>
### Is Evaluation Awareness Just Format Sensitivity? Limitations of Probe-Based Evidence under Controlled Prompt Structure

`arxiv:2603.19426` · AI safety and consciousness · 2026-03-19

- final **-0.34** (conf 0.71, pct 17) · impact -1.53 · DROP
- mean rating (1–10): **6.0** · accept votes **5/7** · percentile rank_avg 43.7 (100=best) · rank in year 60.0 (1=best)
- NAIPv2 `-1.178` · NAIP-v1 `0.428` · SciJudge `-3.866` · DGC-BERT `0.848`
- CycleReviewer 8B `6.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `6.2` Accept (S/P/C 2.5/3.0/2.5) · 14B Fast `5.8` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [lovedeathtransformers/10549](https://t.me/lovedeathtransformers/10549)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper does not provide a clear definition of evaluation awareness, making it difficult to understand the specific phenomenon being studied. - The paper does not provide a clear explanation of why probes are sensitive to format rather than context, and how this sensitivity affects the reliability of probe-based analysis. - The paper does not provide a clear discussion of the impli deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2503.16348"></a>
### Palatable Conceptions of Disembodied Being

`arxiv:2503.16348` · AI safety and consciousness · 2025-03-20

- final **-0.82** (conf 0.71, pct 1) · impact -2.26 · DROP
- mean rating (1–10): **4.4** · accept votes **2/7** · percentile rank_avg 12.1 (100=best) · rank in year 79.0 (1=best)
- NAIPv2 `-4.512` · NAIP-v1 `0.242` · SciJudge `-5.599` · DGC-BERT `0.013`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `3.5` Reject · 7B Fast `4.5` Reject (S/P/C 2.75/2.25/2.25) · 14B Fast `2.5` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/7048](https://t.me/axisofordinary/7048), [gonzo_ML/3491](https://t.me/gonzo_ML/3491)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper's main weakness is its lack of originality and contribution. The authors draw heavily on existing philosophical theories and concepts, such as Wittgenstein's later philosophy and Buddhist thought, without providing a new or original perspective. The paper also lacks empirical evidence or experimental results to support its claims. The authors rely on philosophical argumentati cyclereviewer-8b.seed1: Weaknesses  The paper does not provide a clear or well-de

<a id="arxiv-2502.03407"></a>
### Detecting Strategic Deception Using Linear Probes

`arxiv:2502.03407` · AI safety and consciousness · 2025-02-05

- final **-0.49** (conf 0.71, pct 10) · impact +0.23 · DROP
- mean rating (1–10): **5.3** · accept votes **3/7** · percentile rank_avg 35.5 (100=best) · rank in year 72.0 (1=best)
- NAIPv2 `-2.174` · NAIP-v1 `0.558` · SciJudge `1.094` · DGC-BERT `0.056`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast `4.2` Reject (S/P/C 2.25/2.75/2.0) · 14B Fast `5.8` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper lacks novelty. The authors use existing datasets and methods for training and evaluating their probes. The only novelty seems to be the use of a new model (LLaMA-3.3-70B-Instruct) and the evaluation on additional datasets. However, this is not enough to justify the novelty of the paper. - The authors do not provide a thorough analysis of the limitations of their method. Whi deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2501.18837"></a>
### Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming

`arxiv:2501.18837` · AI safety and consciousness · 2025-01-31

- final **+0.13** (conf 0.71, pct 55) · impact +1.11 · WATCH
- mean rating (1–10): **6.4** · accept votes **6/7** · percentile rank_avg 66.6 (100=best) · rank in year 15.0 (1=best)
- NAIPv2 `-1.560` · NAIP-v1 `0.645` · SciJudge `2.925` · DGC-BERT `0.877`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `5.7` Reject (S/P/C 2.67/2.67/2.67) · 14B Fast `6.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/4.0) · SEA-E `6.0` Accept
- Telegram: [data_secrets/6078](https://t.me/data_secrets/6078)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper does not provide a detailed discussion of the limitations of Constitutional Classifiers. While the paper mentions that the approach is not foolproof and that vulnerabilities may still exist, it does not provide a detailed analysis of the potential limitations and weaknesses of the approach.  The paper does not provide a detailed discussion of the potential risks and challenge deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2309.08600"></a>
### Sparse Autoencoders Find Highly Interpretable Features in Language Models

`arxiv:2309.08600` · AI safety and consciousness · 2023-09-15

- final **+0.11** (conf 0.71, pct 54) · impact -0.03 · WATCH
- mean rating (1–10): **6.2** · accept votes **4/7** · percentile rank_avg 48.7 (100=best) · rank in year 26.0 (1=best)
- NAIPv2 `-1.755` · NAIP-v1 `0.449` · SciJudge `2.857` · DGC-BERT `0.063`
- CycleReviewer 8B `5.2` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `7.0` Accept (S/P/C 3.25/3.25/3.25) · 14B Fast `6.7` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper does not provide a clear evaluation of the performance of the learned features compared to other methods. For example, it would be helpful to see a comparison of the interpretability scores of the learned features with those of other methods such as PCA or ICA. It would also be helpful to see a comparison of the performance of the learned features on the indirect object id deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2308.08708"></a>
### Consciousness in Artificial Intelligence: Insights from the Science of Consciousness

`arxiv:2308.08708` · AI safety and consciousness · 2023-08-17

- final **-0.02** (conf 0.71, pct 36) · impact -0.32 · WATCH
- mean rating (1–10): **6.0** · accept votes **4/7** · percentile rank_avg 37.5 (100=best) · rank in year 39.0 (1=best)
- NAIPv2 `-2.592` · NAIP-v1 `0.605` · SciJudge `-0.852` · DGC-BERT `0.033`
- CycleReviewer 8B `3.5` Reject · 70B `` 
- DeepReviewer 7B Std `3.5` Reject · 7B Fast `6.0` Accept (S/P/C 3.0/2.5/2.75) · 14B Fast `6.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/4.0) · SEA-E `6.0` Accept
- Telegram: [rybolos_channel/873](https://t.me/rybolos_channel/873), [ai_newz/2126](https://t.me/ai_newz/2126), [axisofordinary/5356](https://t.me/axisofordinary/5356), [dtulinov/626](https://t.me/dtulinov/626)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper is a report on the current state of the art in the field of artificial consciousness, and it does not provide any new or original contributions. The paper is a summary of existing knowledge in the field, and it does not provide any new insights or perspectives. The paper also does not provide any new or original ideas for future research in the field.  The paper also does not deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2304.06528"></a>
### Power-seeking can be probable and predictive for trained agents

`arxiv:2304.06528` · AI safety and consciousness · 2023-04-13

- final **-0.39** (conf 0.71, pct 14) · impact +0.30 · DROP
- mean rating (1–10): **5.0** · accept votes **3/7** · percentile rank_avg 40.0 (100=best) · rank in year 35.0 (1=best)
- NAIPv2 `-0.491` · NAIP-v1 `0.650` · SciJudge `0.946` · DGC-BERT `0.750`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `2.5` Reject · 7B Fast `4.2` Reject (S/P/C 2.5/2.75/2.25) · 14B Fast `6.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/4895](https://t.me/axisofordinary/4895), [gonzo_ML/1475](https://t.me/gonzo_ML/1475)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper makes several strong assumptions that limit the applicability of the results. For example, it assumes that the agent learns a goal during the training process, and that the learned goal is randomly chosen from the training-compatible goal set. It also assumes that the state and action spaces are finite, and that the rewards are nonnegative. These assumptions may not hold in a cyclereviewer-8b.seed1: Weaknesses  The main weakness of the paper is the lack of

<a id="arxiv-2303.07103"></a>
### Could a Large Language Model be Conscious?

`arxiv:2303.07103` · AI safety and consciousness · 2023-03-04

- final **-0.27** (conf 0.70, pct 21) · impact +0.74 · WATCH · salvage dr7bf
- mean rating (1–10): **5.9** · accept votes **3/7** · percentile rank_avg 49.0 (100=best) · rank in year 25.0 (1=best)
- NAIPv2 `-2.414` · NAIP-v1 `0.783` · SciJudge `-0.326` · DGC-BERT `0.037`
- CycleReviewer 8B `6.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.0` Accept · 7B Fast ``  (S/P/C 2.5/2.5/2.5) · 14B Fast `3.5` Reject
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/3.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/1479](https://t.me/gonzo_ML/1479), [dtulinov/554](https://t.me/dtulinov/554)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper is more of a philosophical discussion than a scientific paper, and does not provide any empirical evidence to support the author's claims. - The author does not provide a clear definition of consciousness, which makes it difficult to evaluate the claims made in the paper. - The author does not provide a clear roadmap for how to overcome the challenges identified, making it  cyclereviewer-8b.seed1: Weaknesses  The paper is more of a philosophical discussi

<a id="arxiv-2206.13477"></a>
### Parametrically Retargetable Decision-Makers Tend To Seek Power

`arxiv:2206.13477` · AI safety and consciousness · 2022-06-27

- final **-0.16** (conf 0.71, pct 25) · impact +0.99 · WATCH
- mean rating (1–10): **5.2** · accept votes **3/7** · percentile rank_avg 48.9 (100=best) · rank in year 12.0 (1=best)
- NAIPv2 `-0.744` · NAIP-v1 `0.739` · SciJudge `2.456` · DGC-BERT `0.269`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.8` Reject · 7B Fast `5.8` Accept (S/P/C 2.5/2.25/2.25) · 14B Fast `4.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [gonzo_ML/1475](https://t.me/gonzo_ML/1475)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper has several weaknesses that need to be addressed:  1. The paper is poorly written and difficult to follow. The authors use a lot of technical jargon and do not provide enough background information for readers who are not familiar with the topic. The paper also lacks a clear structure and organization, making it hard to understand the main arguments and results.  2. The paper deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2206.13353"></a>
### Is Power-Seeking AI an Existential Risk?

`arxiv:2206.13353` · AI safety and consciousness · 2022-06-16

- final **-0.07** (conf 0.71, pct 32) · impact +1.32 · WATCH
- mean rating (1–10): **5.8** · accept votes **3/7** · percentile rank_avg 50.2 (100=best) · rank in year 11.0 (1=best)
- NAIPv2 `-0.861` · NAIP-v1 `0.852` · SciJudge `0.882` · DGC-BERT `0.020`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `6.2` Accept · 7B Fast `6.8` Reject (S/P/C 2.75/2.75/2.75) · 14B Fast `4.8` Reject
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/3.0) · SEA-E `5.0` Accept
- Telegram: [gonzo_ML/1475](https://t.me/gonzo_ML/1475)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper does not provide a detailed analysis of the six premises and does not provide a clear argument for why they are true. The author assigns subjective probabilities to each premise, but does not provide a clear justification for these probabilities. The paper also does not provide a clear discussion of the potential solutions to the problem of power-seeking AI.  ## Questions  Wh deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-1912.01683"></a>
### Optimal Policies Tend to Seek Power

`arxiv:1912.01683` · AI safety and consciousness · 2019-12-03

- final **-0.01** (conf 0.71, pct 38) · impact -0.25 · WATCH
- mean rating (1–10): **5.7** · accept votes **3/7** · percentile rank_avg 44.0 (100=best) · rank in year 2.0 (1=best)
- NAIPv2 `-0.605` · NAIP-v1 `0.415` · SciJudge `2.619` · DGC-BERT `0.705`
- CycleReviewer 8B `3.5` Reject · 70B `` 
- DeepReviewer 7B Std `4.8` Reject · 7B Fast `5.2` Reject (S/P/C 2.5/2.75/2.5) · 14B Fast `5.5` Reject
- OpenReviewer `8.0` Accept (S/P/C 4.0/3.0/4.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/1475](https://t.me/gonzo_ML/1475)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper only considers optimal policies in MDPs and does not discuss the implications for learned policies in real-world environments. The authors also do not provide any empirical results or experiments to support their claims.  ## Questions  1. How do the results in this paper apply to learned policies in real-world environments? 2. Can you provide empirical results or experiments  deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2606.08720"></a>
### This is how the Neocortex Learns

`arxiv:2606.08720` · NeuroAI · 2026-06-07

- final **-0.27** (conf 0.70, pct 21) · impact -1.69 · DROP · partial fulltext
- mean rating (1–10): **6.0** · accept votes **3/7** · percentile rank_avg 35.7 (100=best) · rank in year 68.0 (1=best)
- NAIPv2 `-1.618` · NAIP-v1 `0.485` · SciJudge `-7.319` · DGC-BERT `0.213`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `1.0` Reject · 7B Fast `8.0` Accept (S/P/C 3.67/3.67/3.67) · 14B Fast `3.8` Reject
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/4.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/5565](https://t.me/gonzo_ML/5565)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper is not a research paper, but rather a review paper. It does not present any new results or findings. The authors do not provide any new insights or perspectives on the topic. The paper is more like a summary of the current state of the art in the field.  ## Questions  N/A  ## Flag For Ethics Review  No ethics review needed.  ## Rating  3: reject, not good enough  ## Confidenc deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2505.17117"></a>
### From Tokens to Thoughts: How LLMs and Humans Trade Compression for Meaning

`arxiv:2505.17117` · NeuroAI · 2025-05-21

- final **+0.50** (conf 0.71, pct 91) · impact +1.45 · KEEP
- mean rating (1–10): **6.6** · accept votes **7/7** · percentile rank_avg 77.6 (100=best) · rank in year 3.0 (1=best)
- NAIPv2 `-0.097` · NAIP-v1 `0.768` · SciJudge `1.890` · DGC-BERT `0.626`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `8.0` Accept · 7B Fast `7.5` Accept (S/P/C 3.0/3.25/3.25) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper could benefit from a more detailed discussion of the limitations of the Information Bottleneck framework and how it may not fully capture the complexity of human cognition. 2. The paper could benefit from a more detailed discussion of the implications of the findings for the development of LLMs and their applications. 3. The paper could benefit from a more detailed discuss deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="doi-10.1101-2024.02.22.581686"></a>
### MetaWorm: An Integrative Data-Driven Model Simulating <i>C. elegans</i> Brain, Body and Environment Interactions

`doi:10.1101/2024.02.22.581686` · NeuroAI · 2024-02-26

- final **+0.05** (conf 0.70, pct 44) · impact -0.72 · WATCH · partial fulltext
- mean rating (1–10): **5.7** · accept votes **4/7** · percentile rank_avg 40.2 (100=best) · rank in year 31.0 (1=best)
- NAIPv2 `-2.701` · NAIP-v1 `0.501` · SciJudge `-4.023` · DGC-BERT `0.096`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `6.5` Accept · 7B Fast `6.0` Reject (S/P/C 2.75/2.5/2.5) · 14B Fast `7.3` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/6364](https://t.me/axisofordinary/6364)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper is not well written and lacks clarity. The figures are not self-explanatory and the text is not clear. The authors should provide more details about the methods used to build the model and the results obtained. The authors should also provide more details about the limitations of the model and the future directions for improvement.   The authors should also provide more detai deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="doi-10.1101-2023.04.04.535512"></a>
### Emergence of belief-like representations through reinforcement learning

`doi:10.1101/2023.04.04.535512` · NeuroAI · 2023-04-07

- final **+0.01** (conf 0.70, pct 40) · impact -1.87 · WATCH · partial fulltext
- mean rating (1–10): **6.0** · accept votes **2/7** · percentile rank_avg 37.6 (100=best) · rank in year 38.0 (1=best)
- NAIPv2 `-2.010` · NAIP-v1 `0.301` · SciJudge `-3.189` · DGC-BERT `0.470`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `3.5` Reject · 7B Fast `6.3` Reject (S/P/C 2.67/2.67/2.67) · 14B Fast `6.8` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `7.0` Accept
- Telegram: [axisofordinary/4834](https://t.me/axisofordinary/4834)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper is more of a computational neuroscience study, but it does not provide any neuroscience data. The authors should provide experimental data to support their hypothesis.  2. The authors should compare their model with other models that can learn belief states, such as the one in (1).  3. The authors should also compare their model with other RNN models, such as the ones in ( deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="doi-10.1371-journal.pcbi.1011005"></a>
### Neural spiking for causal inference and learning

`doi:10.1371/journal.pcbi.1011005` · NeuroAI · 2023-04-04

- final **+0.22** (conf 0.68, pct 64) · impact -1.99 · KEEP
- mean rating (1–10): **5.8** · accept votes **4/6** · percentile rank_avg 38.5 (100=best) · rank in year 36.0 (1=best)
- NAIPv2 `-1.458` · NAIP-v1 `0.341` · SciJudge `-6.510` · DGC-BERT `0.122`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std ``  · 7B Fast `6.5` Accept (S/P/C 3.0/3.0/3.0) · 14B Fast `6.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [axisofordinary/4763](https://t.me/axisofordinary/4763)
- Weaknesses: cyclereviewer-8b: Weaknesses  The main weakness of the paper is that the results are not convincing. The authors use a very simple model to test their idea, and the results are not convincing. For example, in Fig 3A, the authors show that the spiking discontinuity estimator is unbiased when p is small, but this is not surprising. In fact, if p is too small, the estimator will be very noisy. In Fig 3B, the authors s cyclereviewer-8b.seed1: Weaknesses  The paper is not well written and the authors

<a id="doi-10.1371-journal.pcbi.1010628"></a>
### Sleep prevents catastrophic forgetting in spiking neural networks by forming a joint synaptic weight representation

`doi:10.1371/journal.pcbi.1010628` · NeuroAI · 2022-11-18

- final **+0.09** (conf 0.71, pct 50) · impact -1.93 · WATCH
- mean rating (1–10): **6.7** · accept votes **4/7** · percentile rank_avg 42.5 (100=best) · rank in year 14.0 (1=best)
- NAIPv2 `-3.535` · NAIP-v1 `0.377` · SciJudge `-8.504` · DGC-BERT `0.018`
- CycleReviewer 8B `5.2` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `6.7` Accept (S/P/C 3.0/3.0/2.67) · 14B Fast `7.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper lacks novelty and the results are not surprising. The idea of using sleep to prevent catastrophic forgetting has been explored in previous works, and the authors do not provide any new insights or contributions to this area. The experimental setup is also too simple and does not reflect the complexity of real-world scenarios. The authors do not provide any discussion on the l deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2210.08340"></a>
### Toward Next-Generation Artificial Intelligence: Catalyzing the NeuroAI Revolution

`arxiv:2210.08340` · NeuroAI · 2022-10-15

- final **-0.16** (conf 0.70, pct 26) · impact -1.25 · WATCH · partial fulltext
- mean rating (1–10): **5.2** · accept votes **3/7** · percentile rank_avg 23.4 (100=best) · rank in year 17.0 (1=best)
- NAIPv2 `-3.387` · NAIP-v1 `0.479` · SciJudge `-5.469` · DGC-BERT `0.087`
- CycleReviewer 8B `2.5` Reject · 70B `` 
- DeepReviewer 7B Std `3.0` Reject · 7B Fast `7.0` Accept (S/P/C 3.0/3.25/3.0) · 14B Fast `5.8` Accept
- OpenReviewer `5.0` Reject (S/P/C 2.0/2.0/2.0) · SEA-E `6.0` Accept
- Telegram: [dtulinov/471](https://t.me/dtulinov/471)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper is more of a call for action than a scientific paper. It does not present any new scientific results or findings. It is more of a position paper or an opinion piece. It is not clear what specific scientific questions the authors are trying to address or what specific challenges they are trying to solve. The paper does not provide any concrete examples or case studies to suppo cyclereviewer-8b.seed1: Weaknesses  The paper lacks a clear research question or 

<a id="arxiv-2112.04035"></a>
### Relating transformers to models and neural representations of the hippocampal formation

`arxiv:2112.04035` · NeuroAI · 2021-12-07

- final **-0.04** (conf 0.71, pct 34) · impact -1.09 · WATCH
- mean rating (1–10): **6.1** · accept votes **3/7** · percentile rank_avg 38.3 (100=best) · rank in year 7.0 (1=best)
- NAIPv2 `-1.878` · NAIP-v1 `0.421` · SciJudge `-1.165` · DGC-BERT `0.043`
- CycleReviewer 8B `4.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.5` Reject · 7B Fast `6.0` Reject (S/P/C 2.75/2.25/2.5) · 14B Fast `6.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/7740](https://t.me/axisofordinary/7740), [boris_again/1275](https://t.me/boris_again/1275)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper is not well written and the ideas are not well presented. The authors should improve the presentation of their work.   2. The authors should provide more details about the experimental setup.   3. The authors should provide more details about the results.   4. The authors should provide more details about the limitations of their work.  ## Questions  1. What is the signifi cyclereviewer-8b.seed1: Weaknesses  The paper is written in a way that makes it d

<a id="arxiv-2112.03978"></a>
### Attractor and integrator networks in the brain

`arxiv:2112.03978` · NeuroAI · 2021-12-07

- final **+0.15** (conf 0.71, pct 57) · impact -0.00 · WATCH
- mean rating (1–10): **6.2** · accept votes **5/7** · percentile rank_avg 46.1 (100=best) · rank in year 5.0 (1=best)
- NAIPv2 `-2.477` · NAIP-v1 `0.616` · SciJudge `0.539` · DGC-BERT `0.040`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `6.8` Accept (S/P/C 3.5/3.5/2.5) · 14B Fast `6.0` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [dtulinov/468](https://t.me/dtulinov/468)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper is a review and does not present any new experimental or theoretical results. While it provides a comprehensive overview of the role of attractor dynamics in the brain, it does not provide any new insights or perspectives on the topic.  ## Questions  No questions.  ## Flag For Ethics Review  No ethics review needed.  ## Rating  6: marginally above the acceptance threshold  ## deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="doi-10.1038-s41467-021-26568-2"></a>
### Correspondence between neuroevolution and gradient descent

`doi:10.1038/s41467-021-26568-2` · NeuroAI · 2021-11-02

- final **-0.43** (conf 0.71, pct 12) · impact -1.15 · DROP
- mean rating (1–10): **6.0** · accept votes **3/7** · percentile rank_avg 34.7 (100=best) · rank in year 8.0 (1=best)
- NAIPv2 `-2.781` · NAIP-v1 `0.435` · SciJudge `-2.452` · DGC-BERT `0.114`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `4.5` Reject (S/P/C 2.0/2.75/2.0) · 14B Fast `5.8` Reject
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/3.0) · SEA-E `6.0` Accept
- Telegram: [axisofordinary/6807](https://t.me/axisofordinary/6807)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper is missing some important references. For example, there is a line of work studying the connection between gradient descent and evolutionary algorithms, such as (1,2,3). The authors should discuss the relationship between their work and these previous works.  (1) Li, Ji, et al. "A second-order gradient method for composition optimization. " Advances in Neural Information Proc deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2602.14486"></a>
### Revisiting the Platonic Representation Hypothesis: An Aristotelian View

`arxiv:2602.14486` · Representation alignment · 2026-02-16

- final **+0.39** (conf 0.71, pct 81) · impact -1.12 · KEEP
- mean rating (1–10): **7.1** · accept votes **5/7** · percentile rank_avg 66.7 (100=best) · rank in year 12.0 (1=best)
- NAIPv2 `-0.554` · NAIP-v1 `0.528` · SciJudge `-4.152` · DGC-BERT `0.477`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `6.2` Reject · 7B Fast `6.5` Accept (S/P/C 3.0/3.0/2.5) · 14B Fast `8.0` Accept
- OpenReviewer `8.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [gonzo_ML/5622](https://t.me/gonzo_ML/5622)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper could benefit from a more thorough discussion of the limitations of the proposed Aristotelian Representation Hypothesis. While the authors acknowledge that representational similarity has no ground-truth scale, they do not provide a clear explanation of how this limitation affects the validity of their findings.  2. The paper could benefit from a more detailed discussion o deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2507.01098"></a>
### Proof of a perfect platonic representation hypothesis

`arxiv:2507.01098` · Representation alignment · 2025-07-01

- final **-0.16** (conf 0.71, pct 26) · impact -2.72 · WATCH
- mean rating (1–10): **5.8** · accept votes **3/7** · percentile rank_avg 33.6 (100=best) · rank in year 73.0 (1=best)
- NAIPv2 `-2.256` · NAIP-v1 `0.222` · SciJudge `-8.591` · DGC-BERT `0.015`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `7.0` Accept · 7B Fast `6.2` Reject (S/P/C 2.5/2.5/2.75) · 14B Fast `6.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `6.0` Accept
- Telegram: [lovedeathtransformers/10956](https://t.me/lovedeathtransformers/10956)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper's contribution is limited, as it is a note that elaborates on the proof of the PRH for the EDLN model. 2. The paper does not provide any new experimental results or insights that are not already discussed in the original paper by Ziyin et al. (2025). 3. The paper does not discuss the limitations of the EDLN model and how they may affect the validity of the PRH.  ## Questio cyclereviewer-8b.seed1: Weaknesses  The paper is a note that elaborates on the pr

<a id="arxiv-2502.15104"></a>
### Estimating Neural Representation Alignment from Sparsely Sampled Inputs and Features

`arxiv:2502.15104` · Representation alignment · 2025-02-20

- final **+0.57** (conf 0.71, pct 96) · impact -0.93 · KEEP
- mean rating (1–10): **6.5** · accept votes **6/7** · percentile rank_avg 66.2 (100=best) · rank in year 16.0 (1=best)
- NAIPv2 `-0.112` · NAIP-v1 `0.555` · SciJudge `-5.210` · DGC-BERT `0.833`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `8.0` Accept · 7B Fast `7.0` Accept (S/P/C 3.25/3.0/3.25) · 14B Fast `7.5` Accept
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper only considers the case where the neural representations are centered. In practice, it is often the case that the neural representations are not centered, and it is not clear how the proposed estimator would perform in this case. - The paper does not provide any theoretical results on the convergence rate of the proposed estimator. - The paper does not provide any empirical deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2405.07987"></a>
### The Platonic Representation Hypothesis

`arxiv:2405.07987` · Representation alignment · 2024-05-13

- final **-0.21** (conf 0.68, pct 24) · impact +0.00 · DROP
- mean rating (1–10): **6.0** · accept votes **3/6** · percentile rank_avg 39.9 (100=best) · rank in year 33.0 (1=best)
- NAIPv2 `-2.098` · NAIP-v1 `0.557` · SciJudge `-0.180` · DGC-BERT `0.039`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std ``  · 7B Fast `5.7` Reject (S/P/C 2.67/2.33/2.67) · 14B Fast `6.5` Accept
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/3.0) · SEA-E `5.0` Accept
- Telegram: [boris_again/3487](https://t.me/boris_again/3487), [axisofordinary/7502](https://t.me/axisofordinary/7502), [boris_again/3151](https://t.me/boris_again/3151), [axisofordinary/6337](https://t.me/axisofordinary/6337), [lovedeathtransformers/10318](https://t.me/lovedeathtransformers/10318), [dealerAI/806](https://t.me/dealerAI/806), [boris_again/2579](https://t.me/boris_again/2579)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper's main weakness is its lack of concrete evidence to support the hypothesis of a shared statistical model of reality. While the authors provide several examples of representation convergence, these examples are largely anecdotal and do not provide a rigorous empirical basis for their hypothesis. Additionally, the paper does not provide a clear definition of what constitutes a  cyclereviewer-8b.seed1: Weaknesses  The paper lacks a clear research question and

<a id="arxiv-2405.01012"></a>
### Correcting Biased Centered Kernel Alignment Measures in Biological and Artificial Neural Networks

`arxiv:2405.01012` · Representation alignment · 2024-05-02

- final **-0.60** (conf 0.71, pct 7) · impact -1.36 · DROP
- mean rating (1–10): **4.6** · accept votes **1/7** · percentile rank_avg 18.0 (100=best) · rank in year 45.0 (1=best)
- NAIPv2 `-1.223` · NAIP-v1 `0.264` · SciJudge `-1.800` · DGC-BERT `0.024`
- CycleReviewer 8B `4.5` Reject · 70B `` 
- DeepReviewer 7B Std `4.2` Reject · 7B Fast `3.5` Reject (S/P/C 2.0/2.5/2.0) · 14B Fast `4.0` Reject
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper is written in a way that is hard to follow. For example, the abstract and introduction are not clear about the main contributions of the paper. The abstract states that the paper highlights issues with the use of CKA as an alignment metric, but it does not clearly state what these issues are. The introduction mentions that the paper shows that CKA can be sensitive to the r deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2007.02789"></a>
### Comparing representational geometries using whitened unbiased-distance-matrix similarity

`arxiv:2007.02789` · Representation alignment · 2020-07-06

- final **+0.78** (conf 0.71, pct 100) · impact -1.97 · KEEP
- mean rating (1–10): **6.8** · accept votes **5/7** · percentile rank_avg 58.0 (100=best) · rank in year 6.0 (1=best)
- NAIPv2 `-0.351` · NAIP-v1 `0.339` · SciJudge `-4.614` · DGC-BERT `0.388`
- CycleReviewer 8B `5.5` Reject · 70B `` 
- DeepReviewer 7B Std `7.5` Accept · 7B Fast `6.5` Accept (S/P/C 3.0/3.0/3.25) · 14B Fast `8.0` Accept
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/4.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper is not well written and is difficult to follow. The authors should consider revising the paper to make it more accessible to a broader audience.  - The paper only considers the Euclidean and Mahalanobis distances, and it is not clear how the method would generalize to other dissimilarity measures.  - The paper does not provide a thorough evaluation of the method, and it is  deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="acl-2025.acl-long.126"></a>
### INVESTORBENCH: A Benchmark for Financial Decision-Making Tasks with LLM-based Agent

`acl:2025.acl-long.126` · Finance · unknown

- final **-0.23** (conf 0.70, pct 23) · impact -0.08 · DROP · partial fulltext
- mean rating (1–10): **5.6** · accept votes **2/7** · percentile rank_avg 40.6 (100=best) · rank in year 6.0 (1=best)
- NAIPv2 `-2.904` · NAIP-v1 `0.557` · SciJudge `-0.440` · DGC-BERT `0.468`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std `5.0` Reject · 7B Fast `6.0` Reject (S/P/C 2.5/2.75/2.5) · 14B Fast `4.0` Reject
- OpenReviewer `6.0` Accept (S/P/C 3.0/3.0/3.0) · SEA-E `7.0` Accept
- Telegram: [rybolos_channel/1561](https://t.me/rybolos_channel/1561)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper lacks a clear evaluation of the proposed benchmark. The authors only provide a brief description of the benchmark and its components, but do not provide a comprehensive evaluation of its effectiveness or limitations.  2. The paper does not provide a clear comparison of the proposed benchmark with existing benchmarks for evaluating LLMs for financial decision-making tasks.  cyclereviewer-8b.seed1: Weaknesses  The paper lacks a clear motivation for the pr

<a id="arxiv-2003.01859"></a>
### Applications of deep learning in stock market prediction: recent progress

`arxiv:2003.01859` · Finance · 2020-02-29

- final **-0.82** (conf 0.71, pct 1) · impact +0.30 · DROP
- mean rating (1–10): **4.3** · accept votes **1/7** · percentile rank_avg 20.6 (100=best) · rank in year 9.0 (1=best)
- NAIPv2 `-6.262` · NAIP-v1 `0.747` · SciJudge `-3.255` · DGC-BERT `0.028`
- CycleReviewer 8B `4.6` Reject · 70B `` 
- DeepReviewer 7B Std `1.0` Reject · 7B Fast `3.0` Reject (S/P/C 2.0/2.0/1.67) · 14B Fast `3.0` Reject
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper is a survey of the literature on deep learning for stock market prediction, and does not provide any new insights or contributions to the field. The paper is also quite long, and could be condensed to make it more concise.  ## Questions  The paper is a survey of the literature on deep learning for stock market prediction, and does not provide any new insights or contributions deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-1807.02787"></a>
### Financial Trading as a Game: A Deep Reinforcement Learning Approach

`arxiv:1807.02787` · Finance · 2018-07-08

- final **-0.84** (conf 0.71, pct 0) · impact -1.91 · DROP
- mean rating (1–10): **3.2** · accept votes **1/7** · percentile rank_avg 7.5 (100=best) · rank in year 4.0 (1=best)
- NAIPv2 `-4.266` · NAIP-v1 `0.237` · SciJudge `-3.517` · DGC-BERT `0.592`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `2.0` Reject · 7B Fast `4.0` Reject (S/P/C 2.25/2.25/2.25) · 14B Fast `3.0` Reject
- OpenReviewer `3.0` Reject (S/P/C 2.0/2.0/2.0) · SEA-E `3.0` Reject
- Telegram: —
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper is poorly written and the results are not convincing. The authors do not provide enough details about the data they used and the evaluation metrics they used to evaluate their method. The authors also do not compare their method with other state-of-the-art methods for trading in the foreign exchange market.  ### Questions  The authors should provide more details about the dat deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-1706.10059"></a>
### A Deep Reinforcement Learning Framework for the Financial Portfolio Management Problem

`arxiv:1706.10059` · Finance · 2017-06-30

- final **-0.78** (conf 0.71, pct 2) · impact -2.19 · DROP
- mean rating (1–10): **3.8** · accept votes **0/7** · percentile rank_avg 3.1 (100=best) · rank in year 8.0 (1=best)
- NAIPv2 `-5.109` · NAIP-v1 `0.235` · SciJudge `-5.784` · DGC-BERT `0.003`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `1.0` Reject · 7B Fast `4.0` Reject (S/P/C 2.25/2.5/2.5) · 14B Fast `4.0` Reject
- OpenReviewer `3.0` Reject (S/P/C 2.0/2.0/2.0) · SEA-E `5.0` Reject
- Telegram: [j_links/374](https://t.me/j_links/374)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper lacks novelty. The proposed framework is a combination of existing techniques and the novelty is limited. The paper also lacks theoretical analysis and the experiments are not convincing.  ## Questions  1. The proposed framework is a combination of existing techniques, such as ensemble of identical independent evaluators, portfolio-vector memory, online stochastic batch learn deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2201.09746"></a>
### Reinforcement Learning Textbook

`arxiv:2201.09746` · Books · 2022-01-19

- final **-0.65** (conf 0.61, pct 5) · impact -0.58 · DROP · partial fulltext
- mean rating (1–10): **4.5** · accept votes **1/7** · percentile rank_avg 21.1 (100=best) · rank in year 18.0 (1=best)
- NAIPv2 `-4.305` · NAIP-v1 `0.616` · SciJudge `-3.755` · DGC-BERT `0.034`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `3.0` Reject · 7B Fast `5.0` Reject (S/P/C 3.0/3.0/2.0) · 14B Fast `3.8` Reject
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `3.0` Reject
- Telegram: [AGI_and_RL/1168](https://t.me/AGI_and_RL/1168), [AGI_and_RL/891](https://t.me/AGI_and_RL/891), [AGI_and_RL/734](https://t.me/AGI_and_RL/734), [AGI_and_RL/278](https://t.me/AGI_and_RL/278), [MLResearch/870](https://t.me/MLResearch/870)
- Weaknesses: cyclereviewer-8b: Weaknesses  The paper is a survey paper, and it does not have any technical contribution.  ### Questions  N/A  ### Flag For Ethics Review  No ethics review needed.  ### Rating  6: marginally above the acceptance threshold  ### Confidence  4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2201.00650"></a>
### Deep Learning Interviews: Hundreds of fully solved job interview questions from a wide range of key topics in AI

`arxiv:2201.00650` · Books · 2021-12-30

- final **-0.64** (conf 0.53, pct 5) · impact -1.38 · DROP · partial fulltext
- mean rating (1–10): **4.0** · accept votes **0/5** · percentile rank_avg 13.1 (100=best) · rank in year 12.0 (1=best)
- NAIPv2 `-3.359` · NAIP-v1 `0.475` · SciJudge `-7.502` · DGC-BERT `0.011`
- CycleReviewer 8B `5.0` Reject · 70B `` 
- DeepReviewer 7B Std ``  · 7B Fast `1.0` Reject (S/P/C 1.0/1.0/1.0) · 14B Fast `` 
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `5.0` Reject
- Telegram: [AIHOUSE/260](https://t.me/AIHOUSE/260), [AIHOUSE/19](https://t.me/AIHOUSE/19), [MLResearch/860](https://t.me/MLResearch/860), [tech_priestess/611](https://t.me/tech_priestess/611)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The paper does not provide any insights into the performance of AI models on these questions. - The paper does not provide any insights into the limitations of the dataset or the framework.  ### Questions  - How does the performance of AI models on these questions compare to human performance? - What are the limitations of the dataset or the framework? - How can the dataset or framew deepreviewer-7b: Weaknesses:** What are the limitations or areas for improvement?

<a id="doi-10.1038-s41566-024-01394-2"></a>
### Inverse-designed low-index-contrast structures on a silicon photonics platform for vector–matrix multiplication

`doi:10.1038/s41566-024-01394-2` · Other · 2024-02-16

- final **-0.24** (conf 0.68, pct 22) · impact -1.51 · DROP
- mean rating (1–10): **5.5** · accept votes **2/6** · percentile rank_avg 21.2 (100=best) · rank in year 44.0 (1=best)
- NAIPv2 `-3.393` · NAIP-v1 `0.338` · SciJudge `-4.369` · DGC-BERT `0.020`
- CycleReviewer 8B `4.8` Reject · 70B `` 
- DeepReviewer 7B Std ``  · 7B Fast `5.2` Reject (S/P/C 3.0/3.0/2.25) · 14B Fast `6.5` Accept
- OpenReviewer `5.0` Reject (S/P/C 3.0/3.0/2.0) · SEA-E `6.0` Accept
- Telegram: [gonzo_ML/2688](https://t.me/gonzo_ML/2688)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper is a review paper, which is not suitable for ICLR.   2. The paper does not provide any new results or insights. It is a comprehensive review of existing work.  3. The paper does not discuss the challenges and limitations of photonic matrix multiplication and photonic acceleration. It only provides a general discussion of the advantages of photonic matrix multiplication.  # deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2309.10232"></a>
### Fully parallel optical matrix-matrix multiplication

`arxiv:2309.10232` · Other · 2023-09-19

- final **-0.86** (conf 0.71, pct 0) · impact -2.00 · DROP
- mean rating (1–10): **3.2** · accept votes **0/7** · percentile rank_avg 5.3 (100=best) · rank in year 48.0 (1=best)
- NAIPv2 `-4.305` · NAIP-v1 `0.365` · SciJudge `-7.444` · DGC-BERT `0.022`
- CycleReviewer 8B `3.0` Reject · 70B `` 
- DeepReviewer 7B Std `3.5` Reject · 7B Fast `2.5` Reject (S/P/C 1.5/1.5/1.5) · 14B Fast `4.8` Reject
- OpenReviewer `3.0` Reject (S/P/C 2.0/2.0/2.0) · SEA-E `3.0` Reject
- Telegram: [gonzo_ML/2688](https://t.me/gonzo_ML/2688)
- Weaknesses: cyclereviewer-8b: Weaknesses  - The authors do not provide any experimental results to support their claims. The paper only provides a theoretical analysis of the proposed method and its potential applications in optical neural networks.  - The authors do not compare their proposed method with existing methods in the field of optical computing.  - The authors do not discuss the potential limitations and challenges  deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

<a id="arxiv-2304.01433"></a>
### TPU v4: An Optically Reconfigurable Supercomputer for Machine Learning with Hardware Support for Embeddings

`arxiv:2304.01433` · Other · 2023-04-04

- final **+0.11** (conf 0.65, pct 54) · impact +0.35 · WATCH · partial fulltext
- mean rating (1–10): **6.8** · accept votes **3/6** · percentile rank_avg 53.0 (100=best) · rank in year 19.0 (1=best)
- NAIPv2 `-1.127` · NAIP-v1 `0.679` · SciJudge `0.359` · DGC-BERT `0.010`
- CycleReviewer 8B `6.0` Accept · 70B `` 
- DeepReviewer 7B Std `3.0` Reject · 7B Fast ``  (S/P/C None/None/None) · 14B Fast `5.2` Reject
- OpenReviewer `8.0` Accept (S/P/C 4.0/4.0/3.0) · SEA-E `8.0` Accept
- Telegram: [gonzo_ML/2688](https://t.me/gonzo_ML/2688), [axisofordinary/4738](https://t.me/axisofordinary/4738), [j_links/6618](https://t.me/j_links/6618)
- Weaknesses: cyclereviewer-8b: Weaknesses  1. The paper is not well-organized. The authors should focus on the main contributions and highlight the main contributions in the introduction. 2. The paper does not provide enough details about the TPU v4 architecture. The authors should provide more details about the TPU v4 architecture, including the number of cores, the clock speed, the memory bandwidth, and the power consumption. deepreviewer-14b: Weaknesses, Suggestions, and Questions. Finally, I will output 

