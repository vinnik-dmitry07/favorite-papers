# Review

## Summary
This paper critically examines the R1-Zero-like training method and identifies two key components that influence its performance: base models and reinforcement learning algorithms. The authors conduct a series of experiments to analyze how the characteristics of base models, such as Qwen2.5 and DeepSeek-V3, affect the model's reasoning capabilities. They also identify an optimization bias in the GRPO algorithm that leads to inefficient token use and propose a modified version, Dr. GRPO, to address this issue. Finally, the authors present a minimalist recipe for R1-Zero-like training that achieves state-of-the-art performance on the AIME 2024 benchmark using a 7B parameter model.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper provides a critical perspective on the R1-Zero-like training method, which is a novel approach that directly applies reinforcement learning to large language models without the need for supervised fine-tuning. This perspective helps in understanding the underlying mechanisms and limitations of this method.
2. The authors conduct a thorough analysis of the base models used in R1-Zero-like training, such as Qwen2.5 and DeepSeek-V3. This analysis reveals how the pretraining characteristics of these models, including their reasoning capabilities and emergent behaviors, affect the performance of the reinforcement learning process.
3. The paper identifies an optimization bias in the GRPO algorithm that leads to inefficient token use during training. The authors propose a modified version of GRPO called Dr. GRPO that addresses this issue and improves token efficiency while maintaining reasoning performance.

## Weaknesses
1. The paper does not provide a detailed comparison of the proposed Dr. GRPO algorithm with other existing reinforcement learning algorithms for large language models. It would be beneficial to include such a comparison to understand the advantages and limitations of Dr. GRPO in relation to other approaches.
2. The paper focuses on achieving state-of-the-art performance on the AIME 2024 benchmark using a 7B parameter model. It would be interesting to see how the proposed approach scales with larger models and whether it can achieve similar results on other benchmarks beyond math reasoning.

## Questions
1. How does the proposed Dr. GRPO algorithm compare to other existing reinforcement learning algorithms for large language models in terms of token efficiency and reasoning performance?
2. Can the proposed approach be scaled up to larger models, such as 70B or 175B parameters, and still achieve similar results on the AIME 2024 benchmark or other reasoning benchmarks?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4