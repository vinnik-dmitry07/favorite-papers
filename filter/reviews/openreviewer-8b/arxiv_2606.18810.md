# Review

## Summary
This paper introduces SC-GRPO, a novel approach to reinforcement learning with verifiable rewards (RLVR) that addresses the limitations of existing credit assignment methods for training large language models (LLMs) on reasoning tasks. SC-GRPO leverages the model's own verified trajectories to create a self-conditioned teacher, allowing for more effective token-level credit assignment without relying on external resources. The method demonstrates significant improvements over existing approaches, including GRPO and DAPO, across multiple benchmarks in math, code, and agentic tasks, showcasing its robustness and effectiveness in enhancing LLM performance.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The introduction of SC-GRPO, which uses the model's own verified trajectories for self-conditioning, is a novel approach that addresses the limitations of existing credit assignment methods in RLVR.
2. The paper provides a theoretical analysis of why traditional self-distillation fails in RLVR, adding depth to the understanding of the challenges in the domain.
3. The method is extensively tested across five benchmarks, showing consistent improvements over strong baselines like GRPO and DAPO, which demonstrates its effectiveness in various reasoning tasks.

## Weaknesses
1. The experiments are limited to models up to 8B parameters and response lengths of 12,288 tokens, raising questions about the scalability of SC-GRPO to larger models and longer responses.
2. The paper does not explore the applicability of SC-GRPO to extended thinking modes or structured output formats, which could be beneficial for certain complex reasoning tasks.

## Questions
1. How does SC-GRPO handle scenarios where multiple verified trajectories exist, and how does it ensure proper credit assignment in such cases?
2. Can the authors provide more insights into the choice of using the 75th percentile for the normalization threshold and its impact on the model's performance?
3. How does SC-GRPO compare to other credit assignment methods in terms of computational efficiency, especially in large-scale settings?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4