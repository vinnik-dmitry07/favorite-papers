# Review

## Summary
This paper proposes a novel perspective on Group Relative Policy Optimization (GRPO), a prominent reinforcement learning algorithm for post-training large language models (LLMs). The authors argue that the effectiveness of GRPO stems from its implicit contrastive objective, rather than its ability to estimate accurate value baselines. They propose 2-GRPO, a variant of GRPO that uses only two rollouts per prompt to construct contrastive signals, and demonstrate its effectiveness and efficiency compared to the original GRPO. The paper provides theoretical analysis and empirical results to support their claims.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper provides a new perspective on GRPO by framing it as a contrastive learning method, which leads to the development of 2-GRPO, a more efficient variant.
2. The paper provides both theoretical analysis and empirical results to support its claims, demonstrating the effectiveness and efficiency of 2-GRPO compared to GRPO.
3. The authors conduct experiments on various reasoning tasks, including math, code, and vision, showing the broad applicability of their method.

## Weaknesses
1. The paper does not provide a detailed analysis of the computational overhead of 2-GRPO compared to GRPO, beyond training time. Other metrics such as FLOPs, memory usage, and GPU hours could provide a more comprehensive picture.
2. The paper does not compare 2-GRPO to other state-of-the-art methods for post-training LLMs, such as PPO or REINFORCE.
3. The paper does not provide a detailed analysis of the sensitivity of 2-GRPO to hyperparameters, such as the learning rate or the number of resampling attempts.

## Questions
1. Can you provide more details on the computational overhead of 2-GRPO compared to GRPO, including metrics such as FLOPs, memory usage, and GPU hours?
2. How does 2-GRPO compare to other state-of-the-art methods for post-training LLMs, such as PPO or REINFORCE?
3. Can you provide a more detailed analysis of the sensitivity of 2-GRPO to hyperparameters, such as the learning rate or the number of resampling attempts?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4