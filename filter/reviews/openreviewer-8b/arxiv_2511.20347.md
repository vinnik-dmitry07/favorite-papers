# Review

## Summary
This paper introduces a new algorithm, Soft Adaptive Policy Optimization (SAPO), which addresses the issue of training instability in reinforcement learning for large language models. SAPO replaces the hard clipping used in previous methods with a smooth, temperature-controlled gating function that adaptively attenuates off-policy updates while preserving relevant learning signals. This approach aims to improve the stability and efficiency of policy optimization, particularly in scenarios with high variance in token-level importance ratios. The authors demonstrate that SAPO outperforms existing methods, such as GSPO and GRPO, in terms of training stability and performance on mathematical reasoning tasks.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The introduction of a smooth, temperature-controlled gating mechanism is a novel approach to handling off-policy updates in reinforcement learning for LLMs.
2. The paper provides a thorough theoretical analysis of SAPO, including its connections and differences with existing methods like GSPO and GRPO.
3. The authors conduct both controlled experiments and large-scale evaluations on Qwen3-VL models, demonstrating the effectiveness of SAPO across diverse tasks and model sizes.

## Weaknesses
1. The paper does not provide a detailed analysis of the computational overhead introduced by the soft gating mechanism compared to hard clipping methods.
2. The paper could benefit from a more extensive discussion on the generalizability of SAPO to other types of LLM tasks beyond mathematical reasoning.
3. The paper could provide more insight into how sensitive SAPO is to the choice of hyperparameters, particularly the temperatures for positive and negative tokens.

## Questions
1. How does the computational cost of SAPO compare to GSPO and GRPO, particularly in large-scale settings?
2. Can the authors provide more insights into the generalizability of SAPO to other types of LLM tasks, such as natural language inference or summarization?
3. How does SAPO handle extremely long sequences, and what are the potential limitations in such scenarios?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4