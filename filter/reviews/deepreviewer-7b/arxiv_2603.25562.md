I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper addresses the issue of instability in on-policy distillation (OPD) for large language models (LLMs), where the student model's training signal can become unreliable, especially in long-horizon settings. The authors identify three failure modes: imbalanced token-level supervision, unreliable teacher guidance on student-generated prefixes, and mismatches due to tokenization differences. To tackle these challenges, they propose a method called "Teacher top-K local support matching," which compares teacher and student distributions over a teacher-selected support set at each prefix, rather than relying on a single sampled token. This approach aims to provide a more stable and effective training signal, particularly for tasks involving reasoning and agentic behavior. The authors demonstrate the effectiveness of their method through experiments on single-task math reasoning and multi-task agentic-plus-reasoning training, showing significant performance gains over standard sampled-token OPD.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper provides a thorough theoretical analysis of the bias-variance trade-off between token-level and sequence-level reverse-KL divergence, offering insights into the advantages of token-level OPD in long-horizon settings.
2. The proposed method, teacher top-K local support matching, is well-motivated and addresses specific failure modes of sampled-token OPD, such as imbalanced token-level supervision and unreliable teacher guidance.
3. The empirical results are compelling, showing substantial performance improvements over standard sampled-token OPD across various benchmarks, including math reasoning and agentic-plus-reasoning tasks.
4. The paper is well-written and clearly organized, with a logical flow from problem identification to solution proposal and experimental validation.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on sampled-token OPD, which is a common but not the only approach for on-policy distillation. Exploring how the proposed method could be extended or adapted to other distillation techniques would broaden its applicability.
2. While the paper provides a theoretical analysis of the bias-variance trade-off, it lacks a detailed discussion on the computational overhead of the proposed method, especially in comparison to sampled-token OPD. This is important for practical implementation, particularly in resource-constrained environments.
3. The method's reliance on a teacher model introduces potential biases, especially if the teacher model has its own limitations or biases. A more in-depth analysis of how these biases might propagate through the distillation process would be valuable.
4. The paper could benefit from a more comprehensive comparison with other state-of-the-art distillation methods, including both on-policy and off-policy approaches, to better contextualize the performance gains.
5. The experimental evaluation, while promising, is limited to a specific set of benchmarks. Expanding the evaluation to include a wider range of tasks and datasets would strengthen the generalizability of the findings.

### Suggestions

The paper's focus on sampled-token on-policy distillation (OPD) is a limitation, as it overlooks other relevant distillation techniques. While the authors' method shows promise for sampled-token OPD, its applicability to other approaches, such as full-vocabulary distillation or knowledge distillation based on intermediate layer activations, remains unclear. A more thorough investigation into how the proposed teacher top-K local support matching could be adapted to these alternative methods would significantly enhance the paper's impact. For instance, could the local support matching concept be applied to the intermediate representations of the teacher and student models, rather than just the token-level distributions? Exploring these connections would not only broaden the method's applicability but also provide a more comprehensive understanding of its underlying principles. Furthermore, a discussion of the potential trade-offs between different distillation methods, including computational cost and performance, would be beneficial for practitioners seeking to apply these techniques in various scenarios.

While the theoretical analysis of the bias-variance trade-off is valuable, the paper lacks a detailed discussion of the computational overhead associated with the proposed method. The introduction of top-K selection and local support matching likely increases the computational cost compared to standard sampled-token OPD. A thorough analysis of this overhead, including a breakdown of the time and memory requirements for each step of the algorithm, is crucial for assessing the practical feasibility of the method. This analysis should consider the impact of different values of K on both computational cost and performance, as well as the potential for optimization. Additionally, a comparison of the computational cost with other distillation methods, including both on-policy and off-policy approaches, would provide a more complete picture of the method's efficiency. This would allow practitioners to make informed decisions about the trade-offs between performance and computational resources.

The paper's reliance on a teacher model introduces the potential for propagating biases, especially if the teacher model itself is flawed. A more in-depth analysis of how these biases might manifest in the student model's behavior is needed. For example, if the teacher model exhibits biases in its reasoning or decision-making, how might these biases be transferred to the student model through the distillation process? The authors should explore methods for mitigating these biases, such as using multiple teacher models with diverse perspectives or incorporating regularization techniques that encourage the student model to learn unbiased representations. Furthermore, a more detailed analysis of the teacher's limitations and how they might affect the distillation process would be valuable. This would provide a more nuanced understanding of the method's limitations and potential risks, and help practitioners make informed decisions about its applicability in different contexts.

### Questions

1. How does the proposed method compare to other distillation techniques, such as full-vocabulary distillation or knowledge distillation based on intermediate layer activations? Are there specific scenarios where the proposed method would be more or less effective than these alternatives?
2. What is the computational overhead of the proposed method compared to standard sampled-token OPD? How does this overhead scale with the size of the models and the value of K?
3. How sensitive is the performance of the proposed method to the choice of the teacher model? What are the implications if the teacher model has its own biases or limitations?
4. How does the proposed method perform on tasks that require more complex reasoning or planning beyond math reasoning and agentic behavior? Are there specific types of tasks where the method might struggle?
5. Could the proposed method be extended to handle multi-modal tasks or tasks involving external knowledge sources? What challenges might arise in such extensions?

### Rating

5

### Confidence

3

**********

## Reviewer 2

### Summary

The paper addresses the issue of instability in on-policy distillation (OPD) for large language models (LLMs), where the training signal can become unreliable, especially in long-horizon settings. The authors identify three failure modes: imbalanced token-level supervision, unreliable teacher guidance on student-generated prefixes, and mismatches due to tokenization differences. To tackle these challenges, they propose a method called "Teacher top-K local support matching," which compares teacher and student distributions over a teacher-selected support set at each prefix, rather than relying on a single sampled token. This approach aims to provide a more stable and effective training signal, particularly for tasks involving reasoning and agentic behavior. The authors demonstrate the effectiveness of their method through experiments on single-task math reasoning and multi-task agentic-plus-reasoning training, showing significant performance gains over standard sampled-token OPD.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper provides a thorough theoretical analysis of the bias-variance trade-off between token-level and sequence-level reverse-KL divergence, offering insights into the advantages of token-level OPD in long-horizon settings.
2. The proposed method, teacher top-K local support matching, is well-motivated and addresses specific failure modes of sampled-token OPD, such as imbalanced token-level supervision and unreliable teacher guidance.
3. The empirical results are compelling, showing substantial performance improvements over standard sampled-token OPD across various benchmarks, including math reasoning and agentic-plus-reasoning tasks.
4. The paper is well-written and clearly organized, with a logical flow from problem identification to solution proposal and experimental validation.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on sampled-token OPD, which is a common but not the only approach for on-policy distillation. Exploring how the proposed method could be extended or adapted to other distillation techniques would broaden its applicability.
2. While the paper provides a theoretical analysis of the bias-variance trade-off, it lacks a detailed discussion on the computational overhead of the proposed method, especially in comparison to sampled-token OPD. This is important for practical implementation, particularly in resource-constrained environments.
3. The method's reliance on a teacher model introduces potential biases, especially if the teacher model has its own limitations or biases. A more in-depth analysis of how these biases might propagate through the distillation process would be valuable.
4. The paper could benefit from a more comprehensive comparison with other state-of-the-art distillation methods, including both on-policy and off-policy approaches, to better contextualize the performance gains.
5. The experimental evaluation, while promising, is limited to a specific set of benchmarks. Expanding the evaluation to include a wider range of tasks and datasets would strengthen the generalizability of the findings.

### Suggestions

The paper's focus on sampled-token on-policy distillation (OPD) is a significant limitation. While the proposed method, teacher top-K local support matching, shows promise, its applicability to other distillation techniques remains unclear. For instance, the method could be explored in the context of full-vocabulary distillation, where the entire probability distribution is compared rather than individual tokens. This would require a re-evaluation of the local support matching concept, potentially involving the selection of top-K teacher distributions and comparing them to the student's full distribution. Furthermore, the method could be adapted to knowledge distillation based on intermediate layer activations, where the proposed approach could be applied to the distributions of hidden states or attention weights. Exploring these extensions would significantly broaden the impact of the work and provide a more comprehensive understanding of the proposed method's capabilities and limitations.

While the theoretical analysis of the bias-variance trade-off is valuable, the paper lacks a detailed discussion of the computational overhead associated with the proposed method. The introduction of top-K selection and local support matching likely increases the computational cost compared to standard sampled-token OPD. A thorough analysis of this overhead, including a breakdown of the time and memory requirements for each step of the algorithm, is crucial for assessing the practical feasibility of the method. This analysis should consider the impact of different values of K on both computational cost and performance, as well as the potential for optimization. Furthermore, a comparison of the computational cost with other distillation methods, including both on-policy and off-policy approaches, would provide a more complete picture of the method's efficiency. This would allow practitioners to make informed decisions about the trade-offs between performance and computational resources.

The reliance on a teacher model introduces the potential for propagating biases, especially if the teacher model itself is flawed. A more in-depth analysis of how these biases might manifest in the student model's behavior is needed. For example, if the teacher model exhibits biases in its reasoning or decision-making, how might these biases be transferred to the student model through the distillation process? The authors should explore methods for mitigating these biases, such as using multiple teacher models with diverse perspectives or incorporating regularization techniques that encourage the student model to learn unbiased representations. Furthermore, a more detailed analysis of the teacher's limitations and how they might affect the distillation process would be valuable. This would provide a more nuanced understanding of the method's limitations and potential risks, and help practitioners make informed decisions about its applicability in different contexts.

### Questions

1. How does the proposed method compare to other distillation techniques, such as full-vocabulary distillation or knowledge distillation based on intermediate layer activations? Are there specific scenarios where the proposed method would be more or less effective than these alternatives?
2. What is the computational overhead of the proposed method compared to standard sampled-token OPD? How does this overhead scale with the size of the models and the value of K?
3. How sensitive is the performance of the proposed method to the choice of the teacher model? What are the implications if the teacher model has its own biases or limitations?
4. How does the proposed method perform on tasks that require more complex reasoning or planning beyond math reasoning and agentic behavior? Are there specific types of tasks where the method might struggle?
5. Could the proposed method be extended to handle multi-modal tasks or tasks involving external knowledge sources? What challenges might arise in such extensions?

### Rating

5

### Confidence

4

**********

## Reviewer 3

### Summary

The paper revisits on-policy distillation (OPD) for large language post-training. The authors identify three failure modes of sampled-token OPD: imbalanced token-level supervision, unreliable teacher guidance on student-generated prefixes, and tokenizer or special-token mismatch. To address these issues, they propose teacher top-K local support matching, which compares teacher and student distributions over a teacher-selected support set at each prefix, rather than relying on a single sampled token. This approach aims to provide a more stable and effective training signal, particularly for tasks involving reasoning and agentic behavior. The authors demonstrate the effectiveness of their method through experiments on single-task math reasoning and multi-task agentic-plus-reasoning training, showing significant performance gains over standard sampled-token OPD.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper provides a thorough theoretical analysis of the bias-variance trade-off between token-level and sequence-level reverse-KL divergence, offering insights into the advantages of token-level OPD in long-horizon settings.
2. The proposed method, teacher top-K local support matching, is well-motivated and addresses specific failure modes of sampled-token OPD, such as imbalanced token-level supervision and unreliable teacher guidance.
3. The empirical results are compelling, showing substantial performance improvements over standard sampled-token OPD across various benchmarks, including math reasoning and agentic-plus-reasoning tasks.
4. The paper is well-written and clearly organized, with a logical flow from problem identification to solution proposal and experimental validation.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on sampled-token OPD, which is a common but not the only approach for on-policy distillation. Exploring how the proposed method could be extended or adapted to other distillation techniques would broaden its applicability.
2. While the paper provides a theoretical analysis of the bias-variance trade-off, it lacks a detailed discussion on the computational overhead of the proposed method, especially in comparison to sampled-token OPD. This is important for practical implementation, particularly in resource-constrained environments.
3. The method's reliance on a teacher model introduces potential biases, especially if the teacher model has its own limitations or biases. A more in-depth analysis of how these biases might propagate through the distillation process would be valuable.
4. The paper could benefit from a more comprehensive comparison with other state-of-the-art distillation methods, including both on-policy and off-policy approaches, to better contextualize the performance gains.
5. The experimental evaluation, while promising, is limited to a specific set of benchmarks. Expanding the evaluation to include a wider range of tasks and datasets would strengthen the generalizability of the findings.

### Suggestions

The paper's focus on sampled-token on-policy distillation (OPD) is a significant limitation. While the proposed method shows promise, its applicability to other distillation techniques, such as full-vocabulary distillation or knowledge distillation based on intermediate layer activations, remains unclear. For instance, could the local support matching concept be adapted to compare distributions of hidden states or attention weights, rather than just token probabilities? Exploring these extensions would greatly broaden the impact of the work. Furthermore, the paper should discuss the potential challenges and modifications needed to apply the method to different distillation paradigms. This would provide a more comprehensive understanding of the method's versatility and limitations.

The paper lacks a detailed analysis of the computational overhead introduced by the proposed method. While the theoretical analysis of the bias-variance trade-off is valuable, it does not address the practical implications of the method's computational cost. The introduction of top-K selection and local support matching likely increases the computational burden compared to standard sampled-token OPD. A thorough analysis of this overhead, including a breakdown of the time and memory requirements for each step of the algorithm, is crucial for assessing the method's feasibility in resource-constrained environments. The authors should provide a comparison of the computational cost with other distillation methods, including both on-policy and off-policy approaches, to better contextualize the method's efficiency. This analysis should also consider the impact of different values of K on both computational cost and performance.

Finally, the paper's reliance on a teacher model introduces potential biases that need to be addressed more thoroughly. The authors should investigate how biases in the teacher model might propagate through the distillation process and affect the student model's behavior. For example, if the teacher model exhibits biases in its reasoning or decision-making, how might these biases be transferred to the student model through the distillation process? The authors should explore methods for mitigating these biases, such as using multiple teacher models with diverse perspectives or incorporating regularization techniques that encourage the student model to learn unbiased representations. Furthermore, a more detailed analysis of the teacher's limitations and how they might affect the distillation process is needed to provide a more nuanced understanding of the method's limitations and potential risks.

### Questions

1. How does the proposed method compare to other distillation techniques, such as full-vocabulary distillation or knowledge distillation based on intermediate layer activations? Are there specific scenarios where the proposed method would be more or less effective than these alternatives?
2. What is the computational overhead of the proposed method compared to standard sampled-token OPD? How does this overhead scale with the size of the models and the value of K?
3. How sensitive is the performance of the proposed method to the choice of the teacher model? What are the implications if the teacher model has its own biases or limitations?
4. How does the proposed method perform on tasks that require more complex reasoning or planning beyond math reasoning and agentic behavior? Are there specific types of tasks where the method might struggle?
5. Could the proposed method be extended to handle multi-modal tasks or tasks involving external knowledge sources? What challenges might arise in such extensions?

### Rating

5

### Confidence

4

**********

## Reviewer 4

### Summary

The paper revisits on-policy distillation (OPD) for LLM post-training and identifies three failure modes of sampled-token OPD: imbalanced token-level supervision, unreliable teacher guidance on student-generated prefixes, and tokenizer or special-token mismatch. To address these issues, the authors propose teacher top-K local support matching, which compares teacher and student distributions over a teacher-selected support set at each prefix, rather than relying on a single sampled token. The proposed method yields a +19.8% performance gain over standard sampled-token OPD.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow. The authors clearly identify the limitations of the existing sampled-token OPD method and propose a simple yet effective solution to address these issues.
- The proposed method is supported by theoretical analysis and extensive experimental results. The authors provide a detailed discussion of the bias-variance trade-off between token-level and sequence-level reverse-KL divergence, which provides a solid theoretical foundation for the proposed method.
- The experimental results demonstrate the effectiveness of the proposed method across various benchmarks, including math reasoning and agentic-plus-reasoning tasks. The authors also provide ablation studies to analyze the impact of different components of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method introduces additional hyperparameters, such as the support size K and the number of rollout samples, which may require careful tuning for different tasks and datasets. The paper does not provide sufficient guidance on how to select these hyperparameters, and it is unclear how sensitive the performance is to different choices. Specifically, the paper lacks a systematic exploration of the hyperparameter space, making it difficult to assess the robustness of the method. For instance, it is not clear if the optimal K value is consistent across different datasets or if it needs to be tuned for each new task. Furthermore, the interaction between K and the number of rollout samples is not well understood, and the paper does not provide any analysis on how these parameters affect the training dynamics and final performance.
- The paper primarily focuses on sampled-token OPD, which is a common but not the only approach for on-policy distillation. The authors do not discuss how the proposed method could be extended or adapted to other distillation techniques. This limits the scope of the paper and makes it difficult to assess the generalizability of the proposed method. It is unclear if the local support matching concept can be applied to other distillation methods, such as full-vocabulary distillation or knowledge distillation based on intermediate layer activations. The paper should at least discuss the potential challenges and limitations of extending the proposed method to other distillation paradigms.

### Suggestions

The paper would benefit significantly from a more thorough investigation into the hyperparameter sensitivity of the proposed method. Specifically, the authors should conduct a systematic study to determine the optimal values of K and the number of rollout samples for different tasks and datasets. This could involve performing a grid search or using more sophisticated hyperparameter optimization techniques. The results of this study should be presented in the paper, along with guidelines for selecting appropriate hyperparameter values. Furthermore, the authors should analyze the interaction between K and the number of rollout samples, and provide insights into how these parameters affect the training dynamics and final performance. For example, it would be useful to show how the performance varies as K increases while keeping the number of rollout samples constant, and vice versa. This analysis would help to establish a more robust and reliable method.

To broaden the scope of the paper, the authors should discuss the potential for extending the proposed method to other distillation techniques. This could involve exploring how the local support matching concept can be adapted to other distillation methods, such as full-vocabulary distillation or knowledge distillation based on intermediate layer activations. The authors should also discuss the potential challenges and limitations of extending the proposed method to other distillation paradigms. For example, it would be useful to discuss how the proposed method could be adapted to handle the different types of distributions involved in full-vocabulary distillation, or how it could be integrated with intermediate layer knowledge distillation. This discussion would help to establish the broader applicability of the proposed method and provide a roadmap for future research.

Finally, the paper should include a more detailed analysis of the computational cost of the proposed method. The authors should provide a breakdown of the computational overhead associated with the proposed method, and compare it to the computational cost of standard sampled-token OPD. This analysis should include the cost of computing the local support matching, as well as the cost of the rollout sampling. This information would be valuable for practitioners who are considering using the proposed method in real-world applications. The authors should also discuss potential strategies for reducing the computational cost of the proposed method, such as using more efficient algorithms for computing the local support matching or reducing the number of rollout samples.

### Questions

- How sensitive is the performance of the proposed method to the choice of the teacher model? What are the implications if the teacher model has its own biases or limitations?
- How does the proposed method perform on tasks that require more complex reasoning or planning beyond math reasoning and agentic behavior? Are there specific types of tasks where the method might struggle?
- Could the proposed method be extended to handle multi-modal tasks or tasks involving external knowledge sources? What challenges might arise in such extensions?

### Rating

6

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers for the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support or refute their claims.

Plan:
1. Go through each reviewer's comments one by one.
2. For each comment identified as a weakness, find the corresponding section in the paper.
3. Extract evidence (quotes, experimental setup, missing citations, etc.) from the paper to validate the weakness.
4. If the weakness is about missing information, check if that information is indeed absent.
5. If the weakness is about a claim, check if the claim is supported by evidence in the paper.
6. If there are conflicting opinions, address them in the synthesis.
```json
[
  {
    "Weakness Statement": "The paper primarily focuses on sampled-token OPD, which is a common but not the only approach for on-policy distillation. Exploring how the proposed method could be extended or adapted to other distillation techniques would broaden its applicability.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "The paper explicitly focuses on sampled-token OPD as the primary method it builds upon: \"In current LLM pipelines, this token-level objective is usually instantiated by sampled-token comparison: at each training step, the update is driven by the teacher–student log-probability difference on the sampled token ( Lu and Lab, 2025 ; Xiao et al., 2026 ) .\"",
        "The proposed method, teacher top-K local support matching, is described as a modification to this sampled-token approach: \"Our method is designed as a direct response to the failure modes above: it retains token-level OPD, but replaces one-token supervision with a distribution-level comparison over a teacher-selected support set at each prefix, while retaining token-level updates for stability.\""
      ],
      "b) Experiment-related Evidence": [
        "The experiments are designed to evaluate the proposed method in the context of sampled-token OPD: \"We evaluate local support matching in three settings: single-task math reasoning (Section 4.2 ), alternating multi-task training over math and agentic tasks (Section 4.3 ), and an additional single-task agentic-plus-reasoning training (Appendix G.1 ).\""
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper explicitly focuses on sampled-token OPD and proposes a modification to this specific approach. The experimental evaluation is also centered around this method.",
      "Supporting quotes": [
        "\"In current LLM pipelines, this token-level objective is usually instantiated by sampled-token comparison...\"",
        "\"Our method is designed as a direct response to the failure modes above... it retains token-level OPD...\""
      ],
      "Impact assessment": "The reviewer's point is valid as the paper's scope is limited to sampled-token OPD, and it doesn't explore the applicability of the proposed method to other distillation techniques."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper's introduction, problem formulation, and experimental sections all center around sampled-token OPD."
    }
  },
  {
    "Weakness Statement": "While the theoretical analysis of the bias-variance trade-off is valuable, it lacks a detailed discussion on the computational overhead of the proposed method, especially in comparison to sampled-token OPD. This is important for practical implementation, particularly in resource-constrained environments.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "The method involves selecting a top-K teacher local support set and renormalizing the distributions: \"Within this support, we renormalize both teacher and student distributions: π ^ θ ( v ∣ c i , t ) = π θ ( v ∣ c i , t ) ∑ u ∈ S c i , π θ ( u ∣ c i , t ) , q ^ θ ( v ∣ c i , t ) = q θ ( v ∣ c i , t ) ∑ u ∈ S c i , q θ ( u ∣ c i , t ) .\"",
        "The paper mentions the use of a support set but doesn't explicitly quantify the computational cost of this selection process: \"For each prompt x x , we sample a group of outputs { o i } i = 1 G using the student inference policy. Let c i , t = ( x , y i , < t ) c_{i,t}=(x,y_{i,<t}) be the prefix at position t of output o i o_{i} , and define the teacher support set S c i , t = TopK q ( c i , t ) , S(c_{i,t})=\text{TopK}_{q}(c_{i,t}), (6) which contains the K highest-probability tokens under the teacher at that prefix.\""
      ],
      "b) Experiment-related Evidence": [
        "The experimental setup mentions the hardware used but doesn't provide details on computational time or resource usage: \"For math reasoning, we report pass@1 on five benchmarks: Math500 ( Hendrycks et al., 2021 ) , AIME24 ( Zhang and Math-AI, 2024 ) , AIME25 ( Zhang and Math-AI, 2025 ) , Minerva ( Lewkowycz et al., 2022 ) , and OlympiadBench ( He et al., 2024 ) . For ALFWorld ( Shridhar et al., 2021 ) , we report success rate by default. In a small number of cases, we additionally report avg@32 on the math benchmarks. More details on experimental setups can be found in Appendix F .\""
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper describes the steps involved in the proposed method, including the selection of the top-K support set and renormalization. However, it lacks a quantitative analysis of the computational cost associated with these steps and a direct comparison to the computational cost of sampled-token OPD.",
      "Supporting quotes": [
        "\"For each prompt x x , we sample a group of outputs { o i } i = 1 G using the student inference policy. Let c i , t = ( x , y i , < t ) c_{i,t}=(x,y_{i,<t}) be the prefix at position t of output o i o_{i} , and define the teacher support set S c i , t = TopK q ( c i , t ) , S(c_{i,t})=\text{TopK}_{q}(c_{i,t}), (6) which contains the K highest-probability tokens under the teacher at that prefix.\"",
        "\"Within this support, we renormalize both teacher and student distributions: π ^ θ ( v ∣ c i , t ) = π θ ( v ∣ c i , t ) ∑ u ∈ S c i , π θ ( u ∣ c i , t ) , q ^ θ ( v ∣ c i , t ) = q θ ( v ∣ c i , t ) ∑ u ∈ S c i , q θ ( u ∣ c i , t ) .\""
      ],
      "Impact assessment": "The reviewer's point is valid as the paper doesn't provide a detailed analysis of the computational overhead, which is a crucial factor for practical implementation."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The method description outlines the steps involved, but there's no quantitative analysis of the computational cost or comparison to the baseline."
    }
  },
  {
    "Weakness Statement": "The method's reliance on a teacher model introduces potential biases, especially if the teacher model has its own limitations or biases. A more in-depth analysis of how these biases might manifest in the student model's behavior is needed.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "The method explicitly uses the teacher model's distribution for comparison: \"Our method is designed as a direct response to the failure modes above: it retains token-level OPD, but replaces one-token supervision with a distribution-level comparison over a teacher-selected support set at each prefix, while retaining token-level updates for stability.\"",
        "The paper acknowledges the use of a teacher model: \"We implement local support matching on top of the verl-agent framework ( Feng et al., 2025 ) , using Qwen2.5-Instruct models as students. We consider two main settings. The first is single-task math reasoning, where OpenThinker3-7B ( Guha et al., 2025 ) serves as the teacher and Training2Go-Math-17K ( Guha et al., 2025 ) , an SFT model built on Qwen2.5-7B-Instruct, as the teacher.\""
      ],
      "b) Experiment-related Evidence": [
        "The paper includes an ablation study on masking: \"We mask problematic special tokens to reduce false negatives caused by incompatible tokenization conventions.\"",
        "The paper also includes an ablation study on the support set size: \"We evaluate the effect of different support set sizes on the performance of the proposed method.\""
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The method relies on the teacher model's distribution, and the paper acknowledges the use of a teacher. However, the paper does not explicitly analyze how biases in the teacher might affect the student or propose methods to mitigate these biases.",
      "Supporting quotes": [
        "\"Our method is designed as a direct response to the failure modes above... it replaces one-token supervision with a distribution-level comparison over a teacher-selected support set...\"",
        "\"We consider two main settings. The first is single-task math reasoning, where OpenThinker3-7B ... serves as the teacher...\""
      ],
      "Impact assessment": "The reviewer's point is valid as the paper doesn't delve into the potential for teacher-induced biases in the student's behavior."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The method description clearly states the use of the teacher model, and there's no explicit discussion or analysis of teacher bias."
    }
  },
  {
    "Weakness Statement": "The paper could benefit from a more comprehensive comparison with other state-of-the-art distillation methods, including both on-policy and off-policy approaches, to better contextualize the performance gains.",
    "Evidence Collection": {
      "b) Experiment-related Evidence": [
        "The paper compares against \"sampled-token OPD\" as the baseline: \"Table 1 shows that local support matching improves over sampled-token OPD in single-task math reasoning.\"",
        "The paper also compares against a masked version of sampled-token OPD: \"Table 2 shows that the effect of local support matching differs across the two task families in alternating multi-task training. The unmasked version raises the average math score from 34.8 to 41.7 (+19.8%), while maintaining competitive ALFWorld performance. The masked version achieves the best ALFWorld score at 97.7, but gives up part of the math improvement.\""
      ]
    },
    "Literature Gap Analysis": [
      "The Related Work section mentions various post-training methods, including those using sequence-level reverse-KL and token-level reverse-KL, but the experimental section primarily focuses on comparing against a sampled-token baseline."
    ],
    "Validation Analysis": {
      "Primary evidence summary": "The paper primarily compares against a sampled-token OPD baseline. While the related work mentions other distillation methods, the experimental section lacks a direct comparison with them.",
      "Supporting quotes": [
        "\"Table 1 shows that local support matching improves over sampled-token OPD...\"",
        "\"Table 2 shows that the effect of local support matching differs across the two task families... compared to sampled-token OPD...\""
      ],
      "Impact assessment": "The reviewer's point is valid as the experimental evaluation could be strengthened by including comparisons with a broader range of state-of-the-art distillation methods."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The experimental results section only presents comparisons against the sampled-token OPD baseline."
    }
  },
  {
    "Weakness Statement": "The experimental evaluation, while promising, is limited to a specific set of benchmarks. Expanding the evaluation to include a wider range of tasks and datasets would strengthen the generalizability of the findings.",
    "Evidence Collection": {
      "b) Experiment-related Evidence": [
        "The paper evaluates on math reasoning benchmarks: \"Math500, AIME24, AIME25, Minerva, and OlympiadBench.\"",
        "The paper also evaluates on an agentic-plus-reasoning task: \"ALFWorld.\""
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper evaluates on a set of math reasoning and agentic-plus-reasoning benchmarks. While these are relevant, the reviewer suggests expanding to a wider range of tasks to better assess generalizability.",
      "Supporting quotes": [
        "\"For math reasoning, we report pass@1 on five benchmarks... For ALFWorld...\""
      ],
      "Impact assessment": "The reviewer's point is valid as evaluating on a broader range of tasks would provide stronger evidence for the generalizability of the proposed method."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The experimental section details the specific benchmarks used, and while relevant, a broader set could strengthen generalizability claims."
    }
  },
  {
    "Weakness Statement": "The paper primarily focuses on sampled-token OPD, which is a common but not the only approach for on-policy distillation. While the proposed method shows promise, its applicability to other distillation techniques, such as full-vocabulary distillation or knowledge distillation based on intermediate layer activations, remains unclear. For instance, could the local support matching concept be applied to the distributions of hidden states or attention weights? Exploring these extensions would greatly broaden the impact of the work and provide a more comprehensive understanding of the proposed method's capabilities and limitations.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "The paper explicitly focuses on sampled-token OPD: \"In current LLM pipelines, this token-level objective is usually instantiated by sampled-token comparison...\"",
        "The proposed method is described as a modification to this sampled-token approach: \"Our method is designed as a direct response to the failure modes above: it retains token-level OPD, but replaces one-token supervision with a distribution-level comparison over a teacher-selected support set at each prefix...\""
      ],
      "b) Experiment-related Evidence": [
        "The experiments are designed to evaluate the proposed method in the context of sampled-token OPD: \"We evaluate local support matching in three settings: single-task math reasoning... alternating multi-task training... and an additional single-task agentic-plus-reasoning training...\""
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper's focus is explicitly on sampled-token OPD, and the proposed method is designed as a modification to this specific approach. The reviewer correctly points out the lack of exploration into other distillation techniques.",
      "Supporting quotes": [
        "\"In current LLM pipelines, this token-level objective is usually instantiated by sampled-token comparison...\"",
        "\"Our method is designed as a direct response to the failure modes above... it retains token-level OPD...\""
      ],
      "Impact assessment": "The reviewer's point is valid as the paper's scope is limited to sampled-token OPD, and its applicability to other distillation methods is not explored."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper's introduction, problem formulation, and experimental sections all center around sampled-token OPD."
    }
  },
  {
    "Weakness Statement": "While the theoretical analysis of the bias-variance trade-off is valuable, the paper lacks a detailed discussion on the computational overhead of the proposed method. The introduction of top-K selection and local support matching likely increases the computational cost compared to standard sampled-token OPD. A thorough analysis of this overhead, including a breakdown of the time and memory requirements for each step of the algorithm, is crucial for assessing the practical feasibility of the method. This analysis should consider the impact of different values of K on both computational cost and performance, as well as the potential for optimization. Furthermore, a comparison of the computational cost with other distillation methods, including both on-policy and off-policy approaches, would provide a more complete picture of the method's efficiency. This would allow practitioners to make informed decisions about the trade-offs between performance and computational resources.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "The method involves selecting a top-K teacher local support set and renormalizing the distributions: \"Within this support, we renormalize both teacher and student distributions: π ^ θ ( v ∣ c i , t ) = π θ ( v ∣ c i , t ) ∑ u ∈ S c i , π θ ( u ∣ c i , t ) , q ^ θ ( v ∣ c i , t ) = q θ ( v ∣ c i , t ) ∑ u ∈ S c i , q θ ( u ∣ c i , t ) .\""
      ],
      "b) Experiment-related Evidence": [
        "The experimental setup mentions the hardware used but doesn't provide details on computational time or resource usage: \"For math reasoning, we report pass@1 on five benchmarks... For ALFWorld...\""
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper describes the steps involved in the proposed method, including the selection of the top-K support set and renormalization. However, it lacks a quantitative analysis of the computational cost associated with these steps and a direct comparison to the computational cost of sampled-token OPD.",
      "Supporting quotes": [
        "\"Within this support, we renormalize both teacher and student distributions: π ^ θ ( v ∣ c i , t ) = π θ ( v ∣ c i , t ) ∑ u ∈ S c i , π θ ( u ∣ c i , t ) , q ^ θ ( v ∣ c i , t ) = q θ ( v ∣ c i , t ) ∑ u ∈ S c i , q θ ( u ∣ c i , t ) .\""
      ],
      "Impact assessment": "The reviewer's point is valid as the paper doesn't provide a detailed analysis of the computational overhead, which is a crucial factor for practical implementation."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The method description outlines the steps involved, but there's no quantitative analysis of the computational cost or comparison to the baseline."
    }
  },
  {
    "Weakness Statement": "Finally, the paper's reliance on a teacher model introduces the potential for propagating biases, especially if the teacher model itself is flawed. A more in-depth analysis of how these biases might manifest in the student model's behavior is needed. For example, if the teacher model exhibits biases in its reasoning or decision-making, how might these biases be transferred to the student model through the distillation process? The authors should explore methods for mitigating these biases, such as using multiple teacher models with diverse perspectives or incorporating regularization techniques that encourage the student model to learn unbiased representations. Furthermore, a more detailed analysis of the teacher's limitations and how they might affect the distillation process would be valuable. This would provide a more nuanced understanding of the method's limitations and potential risks, and help practitioners make informed decisions about its applicability in different contexts.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "The method explicitly uses the teacher model's distribution for comparison: \"Our method is designed as a direct response to the failure modes above: it retains token-level OPD, but replaces one-token supervision with a distribution-level comparison over a teacher-selected support set at each prefix, while retaining token-level updates for stability.\"",
        "The paper acknowledges the use of a teacher model: \"We implement local support matching on top of the verl-agent framework ( Feng et al., 2025 ) , using Qwen2.5-Instruct models as students. We consider two main settings. The first is single-task math reasoning, where OpenThinker3-7B ( Guha et al., 2025 ) serves as the teacher and Training2Go-Math-17K ( Guha et al., 2025 ) , an SFT model built on Qwen2.5-7B-Instruct, as the teacher.\""
      ],
      "b) Experiment-related Evidence": [
        "The paper includes an ablation study on masking: \"We mask problematic special tokens to reduce false negatives caused by incompatible tokenization conventions.\"",
        "The paper also includes an ablation study on the support set size: \"We evaluate the effect of different support set sizes on the performance of the proposed method.\""
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The method relies on the teacher model's distribution, and the paper acknowledges the use of a teacher. However, the paper does not explicitly analyze how biases in the teacher might affect the student or propose methods to mitigate these biases.",
      "Supporting quotes": [
        "\"Our method is designed as a direct response to the failure modes above... it replaces one-token supervision with a distribution-level comparison over a teacher-selected support set...\"",
        "\"We consider two main settings. The first is single-task math reasoning, where OpenThinker3-7B ... serves as the teacher...\""
      ],
      "Impact assessment": "The reviewer's point is valid as the paper doesn't delve into the potential for teacher-induced biases in the student's behavior."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The method description clearly states the use of the teacher model, and there's no explicit discussion or analysis of teacher bias."
    }
  },
  {
    "Weakness Statement": "How does the proposed method compare to other distillation techniques, such as full-vocabulary distillation or knowledge distillation based on intermediate layer activations? Are there specific scenarios where the proposed method would be more or less effective than these alternatives?",
    "Evidence Collection": {
      "b) Experiment-related Evidence": [
        "The paper compares against \"sampled-token OPD\" as the baseline: \"Table 1 shows that local support matching improves over sampled-token OPD in single-task math reasoning.\"",
        "The paper also compares against a masked version of sampled-token OPD: \"Table 2 shows that the effect of local support matching differs across the two task families in alternating multi-task training. The unmasked version raises the average math score from 34.8 to 41.7 (+19.8%), while maintaining competitive ALFWorld performance. The masked version achieves the best ALFWorld score at 97.7, but gives up part of the math improvement.\""
      ]
    },
    "Literature Gap Analysis": [
      "The Related Work section mentions various post-training methods, including those using sequence-level reverse-KL and token-level reverse-KL, but the experimental section lacks a direct comparison with them."
    ],
    "Validation Analysis": {
      "Primary evidence summary": "The paper primarily compares against a sampled-token OPD baseline. While the related work mentions other distillation methods, the experimental section lacks a direct comparison with them.",
      "Supporting quotes": [
        "\"Table 1 shows that local support matching improves over sampled-token OPD...\"",
        "\"Table 2 shows that the effect of local support matching differs across the two task families... compared to sampled-token OPD...\""
      ],
      "Impact assessment": "The reviewer's point is valid as the experimental evaluation could be strengthened by including comparisons with a broader range of distillation techniques."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The experimental results section only presents comparisons against the sampled-token OPD baseline."
    }
  },
  {
    "Weakness Statement": "What is the computational overhead of the proposed method compared to standard sampled-token OPD? How does this overhead scale with the size of the models and the value of K?",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "The method involves selecting a top-K teacher local support set and renormalization: \"Within this support, we renormalize both teacher and student distributions: π ^ θ ( v ∣ c i , t ) = π θ ( v ∣ c i , t ) ∑ u ∈ S c i , π θ ( u ∣ c i , t ) , q ^ θ ( v ∣ c i , t ) = q θ ( v ∣ c i , t ) ∑ u ∈ S c i , q θ ( u ∣ c i , t ) .\""
      ],
      "b) Experiment-related Evidence": [
        "The experimental setup mentions the hardware used but doesn't provide details on computational time or resource usage: \"For math reasoning, we report pass@1 on five benchmarks... For ALFWorld...\""
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper describes the steps involved in the proposed method, including the selection of the top-K support set and renormalization. However, it lacks a quantitative analysis of the computational cost associated with these steps and a direct comparison to the computational cost of sampled-token OPD.",
      "Supporting quotes": [
        "\"Within this support, we renormalize both teacher and student distributions: π ^ θ ( v ∣ c i , t ) = π θ ( v ∣ c i , t ) ∑ u ∈ S c i , π θ ( u ∣ c i , t ) , q ^ θ ( v ∣ c i , t ) = q θ ( v ∣ c i , t ) ∑ u ∈ S c i , q θ ( u ∣ c i , t ) .\""
      ],
      "Impact assessment": "The reviewer's point is valid as the paper doesn't provide a detailed analysis of the computational overhead, which is a crucial factor for practical implementation."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The method description outlines the steps involved, but there's no quantitative analysis of the computational cost or comparison to the baseline."
    }
  },
  {
    "Weakness Statement": "How sensitive is the performance of the proposed method to the choice of the teacher model? What are the implications if the teacher model has its own biases or limitations?",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "The method explicitly uses the teacher model's distribution for comparison: \"Our method is designed as a direct response to the failure modes above: it retains token-level OPD, but replaces one-token supervision with a distribution-level comparison over a teacher-selected support set at each prefix, while retaining token-level updates for stability.\"",
        "The paper acknowledges the use of a teacher model: \"We implement local support matching on top of the verl-agent framework ( Feng et al., 2025 ) , using Qwen2.5-Instruct models as students. We consider two main settings. The first is single-task math reasoning, where OpenThinker3-7B ( Guha et al., 2025 ) serves as the teacher and Training2Go-Math-17K ( Guha et al., 2025 ) , an SFT model built on Qwen2.5-7B-Instruct, as the teacher.\""
      ],
      "b) Experiment-related Evidence": [
        "The paper includes an ablation study on masking: \"We mask problematic special tokens to reduce false negatives caused by incompatible tokenization conventions.\"",
        "The paper also includes an ablation study on the support set size: \"We evaluate the effect of different support set sizes on the performance of the proposed method.\""
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The method relies on the teacher model's distribution, and the paper acknowledges the use of a teacher. However, the paper does not explicitly analyze how biases in the teacher might affect the student or propose methods to mitigate these biases.",
      "Supporting quotes": [
        "\"Our method is designed as a direct response to the failure modes above... it replaces one-token supervision with a distribution-level comparison over a teacher-selected support set...\"",
        "\"We consider two main settings. The first is single-task math reasoning, where OpenThinker3-7B ... serves as the teacher...\""
      ],
      "Impact assessment": "The reviewer's point is valid as the paper doesn't delve into the potential for teacher-induced biases in the student's behavior."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The method description clearly states the use of the teacher model, and there's no explicit discussion or analysis of teacher bias."
    }
  },
  {
    "Weakness Statement": "How does the proposed method perform on tasks that require more complex reasoning or planning beyond math reasoning and agentic behavior? Are there specific types of tasks where the method might struggle?",
    "Evidence Collection": {
      "b) Experiment-related Evidence": [
        "The paper evaluates on math reasoning benchmarks: \"Math500, AIME24, AIME25, Minerva, and OlympiadBench.\"",
        "The paper also evaluates on an agentic-plus-reasoning task: \"ALFWorld.\""
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper evaluates on a set of math reasoning and agentic-plus-reasoning benchmarks. While these are relevant, the reviewer suggests expanding to a wider range of tasks to better assess generalizability and identify potential limitations.",
      "Supporting quotes": [
        "\"For math reasoning, we report pass@1 on five benchmarks... For ALFWorld...\""
      ],
      "Impact assessment": "The reviewer's point is valid as evaluating on a broader range of tasks would provide stronger evidence for the generalizability of the proposed method and potential limitations."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The experimental section details the specific benchmarks used, and while relevant, a broader set could strengthen generalizability claims."
    }
  },
  {
    "Weakness Statement": "Could the proposed method be extended to handle multi-modal tasks or tasks involving external knowledge sources? What challenges might arise in such extensions?",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "The method focuses on token-level distributions and teacher-student alignment: \"Our method is designed as a direct response to the failure modes above: it retains token-level OPD, but replaces one-token supervision with a distribution-level comparison over a teacher-selected support set at each prefix, while retaining token-level updates for stability.\"",
        "The method uses token probabilities for comparison: \"Within this support, we renormalize both teacher and student distributions: π ^ θ ( v ∣ c i , t ) = π θ ( v ∣ c i , t ) ∑ u ∈ S c i , π θ ( u ∣ c i , t ) , q ^ θ ( v ∣ c i , t ) = q θ ( v ∣ c i , t ) ∑ u ∈ S c i , q θ ( u ∣ c i , t ) .\""
      ],
      "b) Experiment-related Evidence": [
        "The experiments are conducted on text-based tasks: \"Math reasoning, agentic-plus-reasoning tasks.\""
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper's method is designed for text-based tasks and relies on token-level distributions. The paper doesn't discuss extensions to multi-modal tasks or tasks involving external knowledge.",
      "Supporting quotes": [
        "\"Our method is designed as a direct response to the failure modes above: it retains token-level OPD...\"",
        "\"Within this support, we renormalize both teacher and student distributions...\""
      ],
      "Impact assessment": "The reviewer's point is valid as the paper doesn't explore the applicability of the method to other types of tasks."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The method description and experimental setup are focused on text-based tasks."
    }
  },
  {
    "Weakness Statement": "How does the proposed method compare to other distillation techniques, such as full-vocabulary distillation or knowledge distillation based on intermediate layer activations? Are there specific scenarios where the proposed method would be more or less effective than these alternatives?",
    "Evidence Collection": {
      "b) Experiment-related Evidence": [
        "The paper compares against \"sampled-token OPD\" as the baseline: \"Table 1 shows that local support matching improves over sampled-token OPD in single-task math reasoning.\"",
        "The paper also compares against a masked version of sampled-token OPD: \"Table 2 shows that the effect of local support matching differs across the two task families in alternating multi-task training. The unmasked version raises the average math score from 34.8 to 41.7 (+19.8%), while maintaining competitive ALFWorld performance. The masked version achieves the best ALFWorld score at 97.7, but gives up part of the math improvement.\""
      ]
    },
    "Literature Gap Analysis": [
      "The Related Work section mentions various post-training methods, including those using sequence-level reverse-KL and token-level reverse-KL, but the experimental section lacks a direct comparison with them."
    ],
    "Validation Analysis": {
      "Primary evidence summary": "The paper primarily compares against a sampled-token OPD baseline. While the related work mentions other distillation methods, the experimental section lacks a direct comparison with them.",
      "Supporting quotes": [
        "\"Table 1 shows that local support matching improves over sampled-token OPD...\"",
        "\"Table 2 shows that the effect of local support matching differs across the two task families... compared to sampled-token OPD...\""
      ],
      "Impact assessment": "The reviewer's point is valid as the experimental evaluation could be strengthened by including comparisons with a broader range of distillation techniques."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The experimental results section only presents comparisons against the sampled-token OPD baseline."
    }
  },
  {
    "Weakness Statement": "What is the computational overhead of the proposed method compared to standard sampled-token OPD? How does this overhead scale with the size of the models and the value of K?",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "The method involves selecting a top-K teacher local support set and renormalization: \"Within this support, we renormalize both teacher and student distributions: π ^ θ ( v ∣ c i , t ) = π θ ( v ∣ c i , t ) ∑ u ∈ S c i , π θ ( u ∣ c i , t ) , q ^ θ ( v ∣ c i , t ) = q θ ( v ∣ c i , t ) ∑ u ∈ S c i , q θ ( u ∣ c i , t ) .\""
      ],
      "b) Experiment-related Evidence": [
        "The experimental setup mentions the hardware used but doesn't provide details on computational time or resource usage: \"For math reasoning, we report pass@1 on five benchmarks... For ALFWorld...\""
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper describes the steps involved in the proposed method, including the selection of the top-K support set and renormalization. However, it lacks a quantitative analysis of the computational cost associated with these steps and a direct comparison to the computational cost of sampled-token OPD.",
      "Supporting quotes": [
        "\"Within this support, we renormalize both teacher and student distributions: π ^ θ ( v ∣ c i , t ) = π θ ( v ∣ c i , t ) ∑ u ∈ S c i , π θ ( u ∣ c i , t ) , q ^ θ ( v ∣ c i , t ) = q θ ( v ∣ c i , t ) ∑ u ∈ S c i , q θ ( u ∣ c i , t ) .\""
      ],
      "Impact assessment": "The reviewer's point is valid as the paper}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces a novel approach to on-policy distillation (OPD) for large language models (LLMs), addressing limitations identified in sampled-token OPD. The authors pinpoint three key failure modes: imbalanced token-level supervision, unreliable teacher guidance on student-generated prefixes, and mismatches due to tokenization differences. To tackle these issues, they propose a method called 'teacher top-K local support matching,' which compares teacher and student distributions over a teacher-selected support set at each prefix, rather than relying on a single sampled token. This approach aims to provide a more stable and effective training signal, particularly for tasks involving reasoning and agentic behavior. The authors demonstrate the effectiveness of their method through experiments on single-task math reasoning and alternating multi-task training over math and agentic tasks. Their results show significant performance gains over standard sampled-token OPD, highlighting the potential of their approach for enhancing the training of LLMs. The core idea is to retain the token-level guidance of sampled-token OPD while replacing one-token supervision with a distribution-level comparison, which is achieved by selecting a top-K teacher local support set and renormalizing the distributions. This method is designed to address the identified failure modes, such as imbalanced token-level supervision and unreliable teacher guidance. The experimental results show that this approach leads to substantial performance improvements in math reasoning and agentic-plus-reasoning tasks, suggesting that the proposed method is a promising alternative to standard sampled-token OPD. The paper provides a clear and well-organized presentation of the problem, the proposed solution, and the experimental results, making it a valuable contribution to the field of LLM post-training. The theoretical analysis of the bias-variance trade-off between token-level and sequence-level reverse-KL divergence also provides a solid foundation for the proposed method. Overall, the paper presents a well-motivated and empirically supported approach to on-policy distillation, with clear potential for practical applications in training LLMs for complex tasks.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

2.0


## Strengths:

I found several aspects of this paper to be particularly strong. First, the authors provide a thorough theoretical analysis of the bias-variance trade-off between token-level and sequence-level reverse-KL divergence, offering insights into the advantages of token-level OPD in long-horizon settings. This theoretical foundation is crucial for understanding the motivation behind the proposed method. Second, the proposed method, teacher top-K local support matching, is well-motivated and addresses specific failure modes of sampled-token OPD, such as imbalanced token-level supervision and unreliable teacher guidance. The approach of comparing teacher and student distributions over a teacher-selected support set at each prefix is a novel and effective way to provide a more stable training signal. Third, the experimental results are compelling, demonstrating substantial performance improvements over standard sampled-token OPD across various benchmarks, including math reasoning and agentic-plus-reasoning tasks. The authors clearly show the effectiveness of their method in addressing the identified issues. The paper is also well-written and clearly organized, with a logical flow from problem identification to solution proposal and experimental validation. The authors effectively illustrate the limitations of the existing sampled-token OPD method and propose a simple yet effective solution to address these limitations. The empirical results are compelling, showing substantial performance improvements over standard sampled-token OPD. The paper is well-written and clearly organized, making it easy to follow the authors' line of reasoning. The authors also provide a detailed discussion of the bias-variance trade-off, which provides a solid foundation for the proposed method. The inclusion of ablation studies, such as masking problematic special tokens and evaluating the effect of different support set sizes, further strengthens the paper by providing a deeper understanding of the proposed method's behavior. Overall, the paper presents a well-motivated and empirically supported approach to on-policy distillation, with clear potential for practical applications in training LLMs for complex tasks.


## Weaknesses:

Despite the strengths of this paper, I have identified several weaknesses that warrant further consideration. First, the paper primarily focuses on sampled-token OPD, which is a common but not the only approach for on-policy distillation. While the proposed method shows promise, its applicability to other distillation techniques, such as full-vocabulary distillation or knowledge distillation based on intermediate layer activations, remains unclear. The method's reliance on a teacher model introduces potential biases, especially if the teacher model has its own limitations or biases. The paper does not delve into the potential for teacher-induced biases in the student's behavior, nor does it propose methods to mitigate these biases. For example, the paper does not explore how biases in the teacher model might manifest in the student model's behavior, such as if the teacher model exhibits biases in its reasoning or decision-making. This is a significant limitation, as the teacher model's biases could propagate to the student model, potentially leading to biased or inaccurate predictions. Furthermore, the paper lacks a detailed analysis of the computational overhead associated with the proposed method. While the theoretical analysis of the bias-variance trade-off is valuable, it does not address the practical implications of the method's computational cost. The introduction of top-K selection and local support matching likely increases the computational cost compared to standard sampled-token OPD. The paper does not provide a breakdown of the time and memory requirements for each step of the algorithm, nor does it compare the computational cost with other distillation methods. This makes it difficult to assess the practical feasibility of the method, particularly in resource-constrained environments. The experimental evaluation, while promising, is limited to a specific set of benchmarks. Expanding the evaluation to include a wider range of tasks and datasets would strengthen the generalizability of the findings. The current evaluation is limited to math reasoning and agentic-plus-reasoning tasks, and it is unclear how the method would perform on other types of tasks, such as those requiring more complex reasoning or planning beyond math reasoning and agentic behavior. The paper also lacks a comprehensive comparison with other state-of-the-art distillation methods, including both on-policy and off-policy approaches. While the related work section mentions various post-training techniques, the experimental section primarily focuses on a comparison against a sampled-token OPD baseline. This makes it difficult to contextualize the performance gains within the broader landscape of distillation techniques. Finally, the paper does not explore how the proposed method could be extended or adapted to other distillation techniques. This limits the scope of the paper and makes it difficult to assess the generalizability of the proposed method. The paper's focus on sampled-token OPD, while understandable, restricts its applicability and limits its potential impact. The lack of exploration into other distillation techniques is a significant limitation, as it prevents the method from being evaluated in a broader context. These weaknesses, while not invalidating the paper's contributions, highlight areas where further research and analysis are needed to fully realize the potential of the proposed method.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should explore how the proposed teacher top-K local support matching concept can be extended or adapted to other distillation techniques. This would involve investigating how the local support matching concept can be applied to the distributions of hidden states or attention weights, rather than just token probabilities. Exploring these extensions would greatly broaden the impact of the work and provide a more comprehensive understanding of the proposed method's capabilities and limitations. Second, the authors should conduct a more thorough investigation into the computational overhead of the proposed method. This should include a breakdown of the time and memory requirements for each step of the algorithm, as well as a comparison of the computational cost with other distillation methods, including both on-policy and off-policy approaches. This analysis should consider the impact of different values of K on both computational cost and performance. Third, the authors should expand the experimental evaluation to include a wider range of tasks and datasets. This would strengthen the generalizability of the findings and provide a more comprehensive assessment of the method's performance. The authors should also consider evaluating the method on tasks that require more complex reasoning or planning beyond math reasoning and agentic behavior. Fourth, the authors should include a more comprehensive comparison with other state-of-the-art distillation methods, including both on-policy and off-policy approaches. This would provide a better context for the performance gains and allow for a more nuanced understanding of the method's efficiency trade-offs. Fifth, the authors should conduct a more in-depth analysis of the potential for teacher-induced biases in the student model's behavior. This should include exploring methods for mitigating these biases, such as using multiple teacher models with diverse perspectives or incorporating regularization techniques that encourage the student model to learn unbiased representations. Furthermore, a more detailed analysis of the teacher's limitations and how they might affect the distillation process would be valuable. Finally, the authors should discuss the potential challenges and modifications needed to apply the proposed method to other distillation techniques, such as full-vocabulary distillation or knowledge distillation based on intermediate layer activations. This would provide a more comprehensive understanding of the method's versatility and limitations. By addressing these suggestions, the authors can significantly strengthen the paper and make it more impactful for the research community.


## Questions:

I have several questions that arise from my analysis of this paper. First, how does the proposed method compare to other distillation techniques, such as full-vocabulary distillation or knowledge distillation based on intermediate layer activations? Are there specific scenarios where the proposed method would be more or less effective than these alternatives? Second, what is the computational overhead of the proposed method compared to standard sampled-token OPD? How does this overhead scale with the size of the models and the value of K? Third, how sensitive is the performance of the proposed method to the choice of the teacher model? What are the implications if the teacher model has its own biases or limitations? Fourth, how does the proposed method perform on tasks that require more complex reasoning or planning beyond math reasoning and agentic behavior? Are there specific types of tasks where the method might struggle? Fifth, could the proposed method be extended to handle multi-modal tasks or tasks involving external knowledge sources? What challenges might arise in such extensions? Sixth, what are the specific scenarios where the proposed method would be more or less effective than other distillation techniques, such as full-vocabulary distillation or knowledge distillation based on intermediate layer activations? Finally, what are the potential challenges and modifications needed to apply the proposed method to other distillation techniques? These questions target key uncertainties in the paper and seek clarification on critical methodological choices and assumptions. Addressing these questions would provide a more comprehensive understanding of the proposed method's capabilities and limitations.


## Rating:

5.25


## Confidence:

3.5


## Decision:

Reject
}