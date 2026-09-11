# Review

## Summary
This paper proposes a new policy optimization method for LLMs called Single-stream Policy Optimization (SPO). The authors identify key limitations in existing group-based methods like GRPO, such as computational inefficiencies from degenerate groups and scalability issues from synchronization requirements. To address these issues, SPO returns to a single-stream approach, using a persistent KL-adaptive value tracker and global advantage normalization to provide stable learning signals. Experiments with the Qwen3-8B model show that SPO outperforms GRPO on complex math benchmarks, achieving higher accuracy and efficiency. Ablation studies confirm that SPO’s improvements come from its principled approach to baseline estimation and advantage normalization. The authors argue that SPO offers a simpler yet more effective alternative to complex, group-based methods, highlighting the potential for a return to foundational RL principles in LLM optimization.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. **Simplicity and Effectiveness**: SPO offers a simpler alternative to complex group-based methods, achieving better performance on challenging benchmarks with fewer computational overheads. The use of a KL-adaptive value tracker and global advantage normalization provides a more stable learning signal, which could make the method easier to implement and more broadly applicable.

2. **Efficiency and Scalability**: By eliminating the need for group synchronization, SPO significantly improves efficiency in training, particularly beneficial for distributed or long-horizon agentic tasks. The method’s design allows for higher throughput and better scalability, addressing key limitations of current approaches.

3. **Principled Approach**: SPO’s approach to baseline estimation and advantage normalization is well-motivated and grounded in reinforcement learning theory. The method provides a more principled way to handle variance reduction, which could inspire future research in policy optimization for LLMs.

4. **Strong Empirical Results**: The experiments on Qwen3-8B demonstrate that SPO consistently outperforms GRPO on multiple hard math benchmarks, achieving significant improvements in accuracy (e.g., +7.3% on BRUMO 25). The results show that SPO is not only simpler but also more effective, challenging the trend of adding complexity to RL algorithms.

## Weaknesses
1. **Limited Evaluation Scope**: The paper only evaluates SPO on a single model (Qwen3-8B) and a specific set of math benchmarks. While these results are promising, broader evaluations across different models and tasks would strengthen the evidence for SPO’s general applicability.

2. **Lack of Theoretical Analysis**: The paper focuses heavily on empirical results but lacks a theoretical analysis of why the KL-adaptive value tracker and global normalization provide such a significant performance boost. A deeper theoretical exploration could help understand the method’s effectiveness.

3. **Sensitivity to Hyperparameters**: The paper does not discuss the sensitivity of SPO to its hyperparameters, such as the discount factor for the value tracker. Understanding how sensitive the method is to these hyperparameters would be important for practitioners looking to adopt it.

## Questions
1. Have you considered evaluating SPO on other LLMs beyond Qwen3-8B, such as different sizes of LLaMA or other architectures? This would help assess the generalizability of the method across models and architectures.

2. Can you provide more insights into the choice of the KL-adaptive value tracker and its hyperparameters? How sensitive is SPO to the choice of the discount factor, and how did you determine the optimal values?

3. How does SPO perform on tasks beyond math benchmarks? Have you considered evaluating it on other types of reasoning tasks or language tasks to demonstrate its broader applicability?

4. Can you provide more details on the implementation of SPO, including the computational overhead compared to GRPO and the resource requirements for your experiments?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4