# Review

## Summary
This paper introduces Skip-Connected Policy Optimization (SKPO), a novel approach to improve Group Relative Policy Optimization (GRPO) for reinforcement learning in large language models. GRPO uses outcome-based rewards, but fine-grained dense rewards are theoretically more beneficial. The authors identify that Monte Carlo estimation of these fine-grained rewards at early reasoning stages leads to high variance and sign inconsistencies, undermining performance. SKPO addresses this by splitting reasoning into upstream and downstream phases: upstream generates initial segments with dense rewards from downstream sampling, while downstream maintains group-relative optimization with a skip connection that concatenates the upstream segment with the original problem. This allows the model to benefit from upstream reasoning while retaining flexibility to bypass flawed reasoning. Experiments show SKPO achieves 3.91% and 6.17% performance gains over strong baselines on Qwen2.5-Math-7B and Llama-3.2-3B models, respectively, across math benchmarks and out-of-domain tasks. Analysis reveals an implicit advantage: SKPO produces higher quality intermediate-step outputs even when matched for final correctness.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The introduction of the Skip-Connected Policy Optimization (SKPO) framework is a novel approach that creatively addresses the challenges of fine-grained reward estimation in reinforcement learning for large language models.
2. The paper provides a thorough analysis of the limitations of existing methods and clearly explains how SKPO overcomes these limitations through its upstream-downstream phase decomposition and skip connection mechanism.
3. The experimental results demonstrate significant performance improvements on multiple benchmarks, validating the effectiveness of the proposed method.

## Weaknesses
1. The paper lacks a detailed analysis of the computational efficiency and scalability of SKPO. It would be beneficial to compare the training time and resource requirements of SKPO with other methods, especially for larger models or datasets.
2. The paper could benefit from a more detailed error analysis to understand the types of errors made by the model and how SKPO specifically addresses them.
3. The paper could provide more insights into the selection of hyperparameters and their impact on performance, as well as the robustness of the method to different hyperparameter settings.

## Questions
1. How does the computational cost of SKPO compare to other state-of-the-art methods, particularly in terms of training time and resource requirements?
2. Can you provide more details on the types of errors that the model makes and how SKPO specifically helps in overcoming them?
3. How sensitive is SKPO to the choice of hyperparameters, and are there any guidelines for selecting optimal hyperparameters?
4. How does SKPO perform on tasks beyond mathematical reasoning, such as logical reasoning or commonsense reasoning?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4