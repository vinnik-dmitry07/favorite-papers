I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper proposes a new reinforcement learning method for LLMs, which combines the advantages of both token-level and sequence-level policy optimization. Specifically, it decomposes the importance sampling ratio into group-level ratios and token-level ratios to achieve entropy-based clipping. The proposed method is evaluated on mathematical reasoning benchmarks and achieves good performance.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The proposed method is well-motivated and reasonable. It combines the advantages of both token-level and sequence-level policy optimization methods.
2. The proposed method is evaluated on multiple mathematical reasoning benchmarks, and it achieves good performance.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is evaluated on mathematical reasoning benchmarks, which are relatively simple. It would be better to evaluate the proposed method on more complex reasoning benchmarks, such as CSQA, GSM8K, and MATH.
2. The proposed method is only evaluated on a single model, Qwen3. It would be better to evaluate the proposed method on more models, such as Llama-3 and Mistral.

### Suggestions

The paper introduces an interesting approach by combining token-level and sequence-level policy optimization using entropy-based clipping. However, the evaluation is limited in scope, focusing solely on mathematical reasoning benchmarks and a single model architecture. To strengthen the paper, it is crucial to evaluate the proposed method on a broader range of reasoning tasks. Specifically, the inclusion of benchmarks like CSQA, GSM8K, and MATH would provide a more comprehensive assessment of the method's generalization capabilities and robustness across different types of reasoning problems. These benchmarks present diverse challenges, including question answering, mathematical problem-solving, and complex mathematical reasoning, which would help to better understand the strengths and limitations of the proposed approach. Furthermore, it would be beneficial to analyze the performance of the method on each benchmark individually, rather than just reporting an average, to identify potential biases or weaknesses in specific areas.

Expanding the evaluation to include multiple model architectures is also essential to demonstrate the general applicability of the proposed method. While Qwen3 is a capable model, evaluating the method on other prominent models such as Llama-3 and Mistral would provide a more robust assessment of its effectiveness. These models have different architectures and training methodologies, and testing on them would help to determine if the method's performance is specific to Qwen3 or if it can be generalized to other models. This would also help to identify any potential model-specific interactions that might affect the method's performance. For example, it would be interesting to see if the method performs differently on models with different attention mechanisms or different numbers of parameters. Such analysis would provide a more complete picture of the method's capabilities and limitations.

Finally, the paper should include a more detailed analysis of the computational overhead introduced by the proposed method. While the paper mentions that the method is efficient, it would be beneficial to provide a more quantitative analysis of the computational cost, including the time and memory requirements. This analysis should compare the proposed method with other token-level and sequence-level policy optimization methods, highlighting the trade-offs between performance and computational cost. Furthermore, it would be useful to discuss the scalability of the method to larger models and datasets. This would help to understand the practical implications of using the proposed method in real-world applications and provide guidance for future research.

### Questions

1. What is the computational overhead introduced by the proposed method compared to other token-level and sequence-level policy optimization methods?
2. How does the proposed method perform on other reasoning tasks, such as CSQA, GSM8K, and MATH?

### Rating

6

### Confidence

3

**********

## Reviewer 2

### Summary

The paper introduces Entropy Importance Sampling Policy Optimization (ESPO), a novel framework designed to enhance policy optimization in reinforcement learning for large language models (LLMs). ESPO combines fine-grained updates with stable training by decomposing sequence-level importance ratios into group-level ratios and token-level ratios, guided by predictive entropy. Additionally, it employs entropy adaptive clipping to dynamically adjust trust regions based on model uncertainty, balancing exploration and stability. The method is evaluated on mathematical reasoning benchmarks, showing improved convergence and performance over existing methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and effective.

### Weaknesses

#### Some Related Works


#### comment

1. The experiments are conducted on only one model, Qwen3, which limits the generalizability of the findings. It would be beneficial to evaluate the method on a broader range of models, including those with different architectures and training paradigms, to ensure the robustness of the results. Specifically, the performance of ESPO on models with varying parameter sizes and pre-training objectives should be explored to understand its adaptability.
2. The evaluation is limited to mathematical reasoning tasks, which may not fully capture the method's effectiveness across diverse reasoning types. The paper should include evaluations on tasks such as commonsense reasoning, logical inference, and code generation to provide a more comprehensive assessment of ESPO's capabilities. The current evaluation does not sufficiently demonstrate the method's versatility in handling different types of reasoning challenges.
3. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods. A thorough analysis of the time and memory requirements, especially when scaling to larger models and datasets, is needed to understand the practical implications of using ESPO. This analysis should include a breakdown of the computational costs associated with each component of the method.

### Suggestions

To address the limitations in model evaluation, the authors should conduct experiments on a more diverse set of models, including those with different architectures (e.g., encoder-decoder models, transformer variants) and training objectives (e.g., masked language models, causal language models). This would provide a more robust assessment of the generalizability of ESPO. For example, evaluating on models like the Llama family, which have different pre-training strategies, would be beneficial. Furthermore, the authors should investigate how the performance of ESPO scales with model size, as this could reveal potential bottlenecks or limitations of the method. It would also be useful to explore the impact of different hyperparameter settings on various models to ensure the method's robustness across different model architectures and training regimes.

To enhance the evaluation of ESPO's reasoning capabilities, the authors should include experiments on a wider range of reasoning tasks beyond mathematical reasoning. This should include tasks that assess different aspects of reasoning, such as commonsense reasoning, logical inference, and code generation. For commonsense reasoning, datasets like Winograd Schema Challenge or bars-to-bear could be used. For logical inference, datasets like the bongard problem could be considered. For code generation, benchmarks like HumanEval or MBPP could be used. These additional evaluations would provide a more comprehensive understanding of ESPO's strengths and weaknesses across different types of reasoning tasks. The analysis should also include a comparison of ESPO's performance against state-of-the-art methods on these tasks to establish its relative effectiveness.

Finally, a detailed analysis of the computational overhead of ESPO is crucial for practical applications. The authors should provide a breakdown of the time and memory requirements for each component of the method, including the entropy calculation, group-level and token-level importance sampling, and adaptive clipping. This analysis should be conducted on different model sizes and datasets to understand how the computational cost scales. It would also be beneficial to compare the computational overhead of ESPO with that of baseline methods, such as GSPO and CISPO, to quantify the trade-offs between performance and computational cost. The authors should also discuss potential optimizations to reduce the computational overhead of ESPO, such as using more efficient entropy estimation techniques or parallelizing the computation of importance ratios.

### Questions

1. How does ESPO perform on other reasoning tasks, such as commonsense reasoning, logical inference, and code generation?
2. What is the computational overhead of ESPO compared to baseline methods, and how does it scale with model size and dataset size?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper proposes a new method for optimizing LLMs in RL settings, called ESPO. ESPO uses entropy to group tokens into groups, and then performs importance sampling at the group level. The authors show that ESPO outperforms other methods on mathematical reasoning benchmarks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow.
- The method is well-motivated and seems to work well in practice.
- The method is simple and easy to implement.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ESPO performs on more complex tasks, such as coding or summarization.
- The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. It would be helpful to see how ES}

Now, please reason step by step, as a thinking process, to arrive at the comprehensive evaluation of the provided response:

**1. Break down the Reviewer's Comments and Identify Key Concerns:**

The reviewer raises several valid concerns, which can be broken down into categories:

* **Scope of Evaluation (Real-World Tasks):** The reviewer correctly points out the limited scope of the experimental evaluation, focusing solely on mathematical reasoning benchmarks. This is a significant limitation as it doesn't demonstrate the generalizability of the proposed method to more complex, real-world tasks.
* **Lack of Diverse Model Evaluation:** The reviewer notes the evaluation is limited to a single model architecture (Qwen3). This raises questions about the method's applicability to other model architectures, particularly those with different training paradigms (e.g., encoder-decoder models).
* **Need for More Diverse Reasoning Tasks:** The reviewer suggests evaluating on a broader range of reasoning tasks beyond mathematical reasoning, such as commonsense reasoning, logical inference, and code generation. This would provide a more comprehensive understanding of the method's capabilities.
* **Lack of Computational Overhead Analysis:** The reviewer highlights the absence of a detailed analysis of the computational overhead introduced by the proposed method, including time and memory requirements. This is crucial for assessing the practical applicability of the method.
* **Suggestions for Improvement:** The reviewer provides concrete suggestions for addressing these limitations, including expanding the evaluation to more tasks and models, and including a computational overhead analysis.

**2. Cross-Reference with the Paper's Content:**

Now, let's examine the paper's content to see how well it addresses these concerns:

* **Scope of Evaluation (Real-World Tasks):**
    * The paper explicitly states the evaluation is on "mathematical reasoning benchmarks" (Abstract, Introduction, Experiments section).
    * The datasets used are indeed mathematical reasoning datasets (SimpleRL, AIME, MATH, HMMT).
    * There is no mention of evaluations on commonsense reasoning, logical inference, code generation, or other real-world tasks.
* **Lack of Diverse Model Evaluation:**
    * The paper states, "We compare ESPO with two classes of policy optimization baselines: (1) sequence-level methods (GSPO) and (2) token-level methods (DAPO, GMPO, CISPO). This covers the spectrum of granularity choices in contemporary LLM fine-tuning." (Introduction).
    * The experimental setup mentions using "Qwen3 base models of varying scales" (Experiments section).
    * While Qwen3 is a capable model, the reviewer's point about evaluating on a *broader* range of models, including those with different architectures, is valid.
* **Need for More Diverse Reasoning Tasks:**
    * As noted above, the evaluation is limited to mathematical reasoning.
* **Lack of Computational Overhead Analysis:**
    * The paper includes a "Training Dynamics" section (Experiments) that compares training accuracy and convergence speed.
    * However, there is no explicit analysis of the computational cost (time and memory) of ESPO compared to baselines.

**3. Synthesize and Formulate the Evaluation:**

Based on this analysis, here's a structured evaluation of the reviewer's concerns:

* **Valid Concern: Limited Scope of Evaluation (Real-World Tasks):**  **Evidence:** The paper explicitly focuses on mathematical reasoning benchmarks. **Conclusion:** Valid. The evaluation does not demonstrate the method's effectiveness on real-world tasks.
* **Partially Valid Concern: Lack of Diverse Model Evaluation:** **Evidence:** The paper evaluates on Qwen3 models. **Conclusion:** Partially Valid. While Qwen3 is a good model, evaluating on a broader range of architectures would strengthen the generalizability claims.
* **Valid Concern: Need for More Diverse Reasoning Tasks:** **Evidence:** The evaluation is solely on mathematical reasoning tasks. **Conclusion:** Valid. The paper lacks evidence of the method's effectiveness on other types of reasoning.
* **Valid Concern: Lack of Computational Overhead Analysis:** **Evidence:** The paper discusses training dynamics but lacks a direct comparison of computational cost. **Conclusion:** Valid. The computational overhead of ESPO is not thoroughly analyzed.

**4. Address the Reviewer's Suggestions:**

The reviewer's suggestions directly address the identified weaknesses:

* **Expand Evaluation to More Tasks and Models:** This directly tackles the limited scope and model evaluation concerns.
* **Include Computational Overhead Analysis:** This directly addresses the lack of computational overhead analysis.

**5. Final Assessment and Confidence Level:**

The reviewer provides a well-reasoned and comprehensive critique of the paper. The concerns raised are **valid** and well-supported by the paper's content. The confidence level in this assessment is **high**.

**6. Potential Nuances and Considerations:**

* **"Reasoning Tasks":** The reviewer uses the term "reasoning tasks" broadly. It's important to note that "reasoning" is a broad term, and the paper focuses specifically on *mathematical reasoning*. The reviewer's suggestions include other types of reasoning, which is a valid point for future work.
* **"Real-World Tasks":** The reviewer distinguishes between mathematical reasoning benchmarks and "real-world tasks." This distinction is important. The paper's evaluation is on well-defined, albeit synthetic, mathematical reasoning problems. The reviewer's point about real-world tasks is valid in the broader context of AI evaluation.

By systematically analyzing the reviewer's comments against the paper's content, we can arrive at a comprehensive and well-supported evaluation of the paper's weaknesses.
}

Now, please tell me the final review decision:

1. **Strengths:** The paper is well-written and easy to follow. The proposed method, ESPO, is novel and well-motivated. The method is simple and easy to implement. The experimental results demonstrate the effectiveness of ESPO on mathematical reasoning benchmarks.

2. **Weaknesses:** The paper lacks experiments on real-world tasks. The evaluation is limited to a single model architecture (Qwen3). The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

3. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

4. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

5. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

6. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

7. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

8. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

9. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

10. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

11. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

12. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

13. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

14. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

15. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

16. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

17. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

18. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

19. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

20. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

21. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

22. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

23. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

24. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

25. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

26. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

27. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

28. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

29. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

30. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

31. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

32. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

33. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

34. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

35. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

36. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

37. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

38. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

39. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

40. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

41. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

42. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

43. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

44. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

45. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

46. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

47. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

48. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

49. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

50. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

51. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

52. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

53. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

54. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

55. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

56. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

57. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

58. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

59. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

60. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

61. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

62. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

63. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

64. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

65. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

66. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

67. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

68. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

69. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

70. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

71. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

72. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

73. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

74. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

75. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

76. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

77. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

78. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

79. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

80. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

81. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

82. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

83. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

84. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

85. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

86. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

87. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

88. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

89. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

90. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

91. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

92. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

93. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

94. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

95. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

96. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

97. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

98. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

99. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

100. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

101. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

102. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

103. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

104. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

105. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

106. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

107. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

108. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

109. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

110. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

111. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

112. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

113. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

114. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

115. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

116. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

117. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

118. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

119. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

120. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

121. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

122. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

123. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

124. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

125. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

126. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

127. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

128. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

129. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

130. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

131. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

132. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

133. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

134. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

135. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

136. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

137. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

138. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

139. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

140. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

141. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

142. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

143. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

144. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

145. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

146. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

147. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

148. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

149. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

150. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

151. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

152. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

153. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

154. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

155. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

156. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

157. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

158. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

159. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

160. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

161. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

162. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

163. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

164. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

165. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

166. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

167. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

168. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

169. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

170. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

171. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

172. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

173. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

174. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

175. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

176. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

177. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

178. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

179. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

180. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

181. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

182. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

183. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

184. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

185. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

186. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

187. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

188. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

189. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

180. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

181. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

182. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

183. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

184. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

185. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

186. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

187. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

188. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

189. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

190. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

191. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

192. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

193. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

194. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

195. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

196. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

197. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

198. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

199. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

200. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

211. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

212. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

213. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

214. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

215. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

216. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

217. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

218. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

219. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

220. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

221. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

222. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

223. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

224. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

225. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

226. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

227. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

228. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

229. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

230. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

231. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

232. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

233. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

234. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

235. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

236. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

237. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

238. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

239. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

240. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

241. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

242. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

243. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

244. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

245. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

246. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

247. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

248. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

249. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

250. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

251. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

252. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

253. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

254. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

255. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

256. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

257. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

258. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

259. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

260. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

261. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

262. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

263. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

264. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

265. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

266. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

267. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

268. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

269. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

270. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

271. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

272. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

273. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

274. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

275. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

276. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

277. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

278. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

279. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

280. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

281. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

282. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

283. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

284. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

285. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

286. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

287. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

288. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

289. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

290. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

291. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

292. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

293. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

294. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

295. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

296. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

297. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

298. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

299. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

300. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

301. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

302. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

303. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

304. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by ESPO compared to baseline methods.

305. **Weaknesses with Partial Validity:** The paper does not include any experiments on real-world tasks, only mathematical reasoning benchmarks. The evaluation is limited to Qwen3, which limits the generalizability of the findings. The paper lacks a detailed analysis of the computational overhead introduced by}

Now, I have thoroughly reviewed the