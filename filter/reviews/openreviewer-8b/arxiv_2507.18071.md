# Review

## Summary
This paper introduces Group Sequence Policy Optimization (GSPO), a reinforcement learning algorithm designed to train large language models efficiently and stably. GSPO improves upon previous methods by using sequence likelihood-based importance ratios and sequence-level clipping and optimization. It outperforms the previous algorithm GRPO in training efficiency, stabilizes Mixture-of-Experts (MoE) model training, and simplifies RL infrastructure requirements. GSPO has significantly contributed to the development of the latest Qwen3 models and is expected to be a robust base for future large-scale RL training.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. GSPO introduces a sequence-level approach to importance sampling, which is a novel shift from token-level methods. This change addresses the instability issues in previous algorithms and improves training stability and efficiency.
2. The paper provides a detailed theoretical basis for the GSPO algorithm, explaining how it aligns with the principles of importance sampling and how it can be derived from a probabilistic perspective.
3. GSPO has been successfully applied to the training of the Qwen3 models, demonstrating its effectiveness at scale. This real-world application is a strong indicator of the algorithm's practical value.

## Weaknesses
1. The paper does not provide a detailed analysis of the computational overhead of GSPO compared to GRPO and other methods. Understanding the computational costs, especially in terms of time and resources, is crucial for assessing the feasibility of adopting GSPO in practical settings.
2. The paper focuses on the empirical performance of GSPO but does not include a sensitivity analysis of its hyperparameters. A sensitivity analysis could provide insights into how sensitive the algorithm is to different parameter settings and whether it requires careful tuning to perform well.
3. The paper does not discuss the potential for overfitting with GSPO, especially since it addresses the training of large language models. Overfitting can be a significant concern in such settings, and strategies to mitigate it would be valuable.

## Questions
1. How does GSPO perform in terms of computational efficiency compared to GRPO and other state-of-the-art methods? Are there any benchmarks or metrics that can be shared to illustrate these differences?
2. Can you provide a sensitivity analysis of the hyperparameters used in GSPO? How sensitive is the algorithm to these parameters, and are there any guidelines for tuning them effectively?
3. What measures have been taken to mitigate the risk of overfitting with GSPO, especially when training on the large-scale datasets typical in language model training? Are there any strategies that have been implemented to ensure the model's generalization capabilities?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4