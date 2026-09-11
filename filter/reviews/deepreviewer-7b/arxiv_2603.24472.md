I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper investigates the phenomenon of self-distillation in LLMs, particularly in the context of mathematical reasoning. The authors observe that while self-distillation often improves performance on in-domain tasks by encouraging concise and confident responses, it can lead to performance degradation on out-of-distribution (OOD) tasks, especially in mathematical reasoning where concise responses are beneficial. The authors hypothesize that this degradation is linked to the suppression of epistemic verbalization, which is the model's tendency to express uncertainty during reasoning. They conduct extensive experiments with various models and settings, analyzing the relationship between conditioning context richness, task coverage, and generalization ability.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper provides a detailed analysis of the relationship between self-distillation, epistemic verbalization, and OOD generalization in LLMs, particularly in the context of mathematical reasoning.
2. The authors conduct extensive experiments with multiple models and settings, providing strong empirical evidence for their claims.
3. The paper is well-written and easy to follow, with clear explanations of the methodology and results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on the negative effects of self-distillation on OOD generalization, but it does not explore potential strategies to mitigate these issues or leverage the benefits of self-distillation in certain scenarios.
2. While the paper provides a detailed analysis of the relationship between self-distillation, epistemic verbalization, and OOD generalization, it does not offer a comprehensive theoretical framework to explain these phenomena.
3. The experiments are primarily conducted on mathematical reasoning tasks, which may limit the generalizability of the findings to other types of reasoning tasks or domains.

### Suggestions

The paper would benefit from a more thorough exploration of potential mitigation strategies for the observed negative impacts of self-distillation on OOD generalization. While the authors acknowledge the performance degradation, they do not delve into specific techniques that could potentially alleviate this issue. For instance, the paper could investigate methods such as regularization techniques that encourage the model to maintain a balance between concise and diverse responses, or explore adaptive self-distillation strategies that dynamically adjust the distillation process based on the model's uncertainty or the task at hand. Furthermore, the authors could consider incorporating techniques like adversarial training to enhance the model's robustness to the specific types of errors that arise from self-distillation. A more detailed analysis of these potential solutions would significantly strengthen the paper's contribution.

To enhance the theoretical underpinnings of the paper, the authors should consider developing a more formal framework that explains the observed relationship between epistemic verbalization, self-distillation, and OOD generalization. While the paper provides an empirical analysis, it lacks a deeper theoretical understanding of why self-distillation leads to the suppression of epistemic verbalization and how this affects OOD performance. This could involve exploring concepts from information theory or Bayesian inference to model the model's uncertainty and reasoning process. For example, the authors could investigate how the self-distillation process alters the model's posterior distribution over possible solutions, leading to a reduction in epistemic uncertainty and a subsequent decrease in performance on OOD tasks. A more rigorous theoretical framework would provide a more solid foundation for the paper's findings and facilitate future research in this area.

Finally, the paper's focus on mathematical reasoning limits the generalizability of the findings. While mathematical reasoning is a complex task, it is not representative of all types of reasoning that LLMs are capable of. The authors should consider expanding their experiments to include other types of reasoning tasks, such as commonsense reasoning, logical reasoning, or natural language inference. This would provide a more comprehensive understanding of the impact of self-distillation on different types of reasoning and help determine whether the observed phenomena are specific to mathematical reasoning or are more generalizable. Furthermore, the authors could explore the performance of self-distillation on tasks from different domains, such as code generation or scientific text summarization, to assess the broader applicability of their findings.

### Questions

1. How does the choice of the base model affect the observed phenomena? Are the findings consistent across different model architectures and sizes?
2. Can the authors provide more insights into the relationship between task coverage and the suppression of epistemic verbalization?
3. How does the performance of self-distillation vary across different types of mathematical reasoning tasks? Are there specific task characteristics that are more susceptible to the negative effects of self-distillation?

### Rating

5

### Confidence

3

**********

## Reviewer 2

### Summary

This paper investigates the impact of self-distillation on LLMs' reasoning abilities, particularly in mathematical tasks. The authors find that while self-distillation can improve performance on in-domain tasks by encouraging concise responses, it can degrade performance on out-of-domain tasks, especially in math reasoning, where concise and confident reasoning is beneficial. The authors hypothesize that this degradation is linked to the suppression of epistemic verbalization, where models explicitly express uncertainty during reasoning. They conduct experiments with various models and settings, analyzing the relationship between conditioning context richness, task coverage, and generalization ability.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper provides a novel perspective on self-distillation, highlighting the importance of epistemic verbalization for robust reasoning and OOD generalization.
- The experiments are well-designed and cover a range of models and settings, providing strong empirical evidence for the claims.
- The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

 - The paper's focus on math reasoning tasks limits the generalizability of the findings. While math reasoning is a complex task, it is not representative of all types of reasoning that LLMs are capable of. The authors should consider expanding their experiments to include other types of reasoning tasks, such as commonsense reasoning, logical reasoning, or natural language inference.
- The paper does not explore the potential benefits of self-distillation in scenarios where concise and confident reasoning is beneficial, such as in code generation or scientific text summarization. It would be valuable to investigate whether self-distillation can improve performance on these tasks, especially in cases where the model is already capable of generating concise and confident responses.
- The paper does not provide a clear definition of what constitutes a "concise" response. The authors should provide a more precise definition of conciseness and explore how different metrics of conciseness affect the results.
- The paper does not explore the potential of using different types of distillation objectives, such as those that explicitly encourage epistemic verbalization. It would be valuable to investigate whether different distillation objectives can mitigate the negative effects of self-distillation on OOD performance.

### Suggestions

The authors should consider expanding their experimental scope to include a wider variety of reasoning tasks beyond mathematical problem-solving. This would involve evaluating the impact of self-distillation on tasks such as logical inference, commonsense reasoning, and natural language understanding. For example, in logical inference, the model could be trained to deduce the correct conclusion from a set of premises, and the authors could examine whether self-distillation leads to a degradation in performance on out-of-domain inference tasks. Similarly, in commonsense reasoning, the model could be tasked with answering questions that require understanding of everyday knowledge, and the authors could investigate whether self-distillation affects the model's ability to generalize to unseen scenarios. These additional experiments would provide a more comprehensive understanding of the generalizability of the findings and the potential limitations of self-distillation in different reasoning contexts. Furthermore, it would be beneficial to explore the performance of self-distillation on tasks where the model is already capable of generating concise and confident responses, such as code generation or scientific text summarization. This would help to determine whether self-distillation can be used to improve performance in these scenarios, and if so, under what conditions.

To address the lack of a precise definition of conciseness, the authors should explore different metrics for measuring the length and complexity of generated responses. This could involve using metrics such as the number of tokens, the number of distinct words, or the perplexity of the generated text. The authors could then investigate how these different metrics correlate with the observed performance degradation on out-of-domain tasks. This would provide a more nuanced understanding of the relationship between conciseness and reasoning performance. Additionally, the authors should explore the impact of different training strategies on the model's ability to generate concise and confident responses. For example, they could investigate whether techniques such as reinforcement learning or adversarial training can be used to encourage the model to produce more concise responses without sacrificing performance. This would help to determine whether self-distillation is the most effective approach for improving conciseness, or if other methods are more suitable.

Finally, the authors should explore the potential of using different types of distillation objectives that explicitly encourage epistemic verbalization. This could involve using objectives that penalize the model for being overly confident or for failing to express uncertainty when appropriate. For example, the authors could investigate the use of objectives that encourage the model to explicitly state when it is unsure about its answer, or to provide evidence for its reasoning steps. This would help to determine whether different distillation objectives can mitigate the negative effects of self-distillation on OOD performance. Furthermore, the authors should investigate the impact of different teacher-student architectures on the effectiveness of self-distillation. For example, they could explore the use of different types of teachers, such as those that are trained on a more diverse dataset, or those that are trained using different objectives. This would help to determine whether the effectiveness of self-distillation is dependent on the specific architecture of the teacher and student models.

### Questions

- How does the choice of the base model affect the observed phenomena? Are the findings consistent across different model architectures and sizes?
- Can the authors provide more insights into the relationship between task coverage and the suppression of epistemic verbalization?
- How does the performance of self-distillation vary across different types of mathematical reasoning tasks? Are there specific task characteristics that are more susceptible to the negative effects of self-distillation?

### Rating

5

### Confidence

3

**********

## Reviewer 3

### Summary

This paper investigates the behavior of self-distillation in LLMs, specifically examining how it affects reasoning performance, particularly in mathematical tasks. The authors find that self-distillation can improve in-domain performance by encouraging concise and confident responses, but it can also degrade out-of-distribution (OOD) performance, especially in math reasoning, where concise responses are beneficial. The authors hypothesize that this degradation is linked to the suppression of epistemic verbalization, where models explicitly express uncertainty during reasoning. They conduct experiments with various models and settings, analyzing the relationship between conditioning context richness, task coverage, and generalization ability.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper provides a novel perspective on self-distillation by highlighting the importance of epistemic verbalization for robust reasoning and OOD generalization.
- The experiments are well-designed and cover a range of models and settings, providing strong empirical evidence for the claims.
- The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

 - The paper's focus on math reasoning tasks limits the generalizability of the findings. While math reasoning is a complex task, it is not representative of all types of reasoning that LLMs are capable of. The authors should consider expanding their experiments to include other types of reasoning tasks, such as commonsense reasoning, logical reasoning, or natural language inference.
- The paper does not explore the potential benefits of self-distillation in scenarios where concise and confident reasoning is beneficial, such as in code generation or scientific text summarization. It would be valuable to investigate whether self-distillation can improve performance on these tasks, especially in cases where the model is already capable of generating concise and confident responses.
- The paper does not provide a clear definition of what constitutes a "concise" response. The authors should provide a more precise definition of conciseness and explore how different metrics of conciseness affect the results.
- The paper does not explore the potential of using different types of distillation objectives, such as those that explicitly encourage epistemic verbalization. It would be valuable to investigate whether different distillation objectives can mitigate the negative effects of self-distillation on OOD performance.

### Suggestions

The authors should consider expanding their experimental scope to include a wider variety of reasoning tasks beyond mathematical problem-solving. This would involve evaluating the impact of self-distillation on tasks such as logical inference, commonsense reasoning, and natural language understanding. For example, in logical inference, the model could be trained to deduce the correct conclusion from a set of premises, and the authors could examine whether self-distillation leads to a degradation in performance on out-of-domain inference tasks. Similarly, in commonsense reasoning, the model could be tasked with answering questions that require understanding of everyday knowledge, and the authors could investigate whether self-distillation affects the model's ability to generalize to unseen scenarios. These additional experiments would provide a more comprehensive understanding of the generalizability of the findings and the potential limitations of self-distillation in different reasoning contexts. Furthermore, it would be beneficial to explore the performance of self-distillation on tasks where the model is already capable of generating concise and confident responses, such as code generation or scientific text summarization. This would help to determine whether self-distillation can be used to improve performance in these scenarios, and if so, under what conditions.

To address the lack of a precise definition of conciseness, the authors should explore different metrics for measuring the length and complexity of generated responses. This could involve using metrics such as the number of tokens, the number of distinct words, or the perplexity of the generated text. The authors could then investigate how these different metrics correlate with the observed performance degradation on out-of-domain tasks. This would provide a more nuanced understanding of the relationship between conciseness and reasoning performance. Additionally, the authors should explore the impact of different training strategies on the model's ability to generate concise and confident responses. For example, they could investigate whether techniques such as reinforcement learning or adversarial training can be used to encourage the model to produce more concise responses without sacrificing performance. This would help to determine whether self-distillation is the most effective approach for improving conciseness, or if other methods are more suitable.

Finally, the authors should explore the potential of using different types of distillation objectives that explicitly encourage epistemic verbalization. This could involve using objectives that penalize the model for being overly confident or for failing to express uncertainty when appropriate. For example, the authors could investigate the use of objectives that encourage the model to explicitly state when it is unsure about its answer, or to provide evidence for its reasoning steps. This would help to determine whether different distillation objectives can mitigate the negative effects of self-distillation on OOD performance. Furthermore, the authors should investigate the impact of different teacher-student architectures on the effectiveness of self-distillation. For example, they could explore the use of different types of teachers, such as those that are trained on a more diverse dataset, or those that are trained using different objectives. This would help to determine whether the effectiveness of self-distillation is dependent on the specific architecture of the teacher and student models.

### Questions

- How does the choice of the base model affect the observed phenomena? Are the findings consistent across different model architectures and sizes?
- Can the authors provide more insights into the relationship between task coverage and the suppression of epistemic verbalization?
- How does the performance of self-distillation vary across different types of mathematical reasoning tasks? Are there specific task characteristics that are more susceptible to the negative effects of self-distillation?

### Rating

6

### Confidence

4

**********

## Reviewer 4

### Summary

This paper investigates the impact of self-distillation on the reasoning capabilities of large language models (LLMs), specifically focusing on mathematical tasks. The authors observe that while self-distillation enhances in-domain performance by producing more concise and confident responses, it can degrade out-of-domain (OOD) performance, particularly in mathematical reasoning tasks. This degradation is attributed to the suppression of epistemic verbalization, where models tend to express uncertainty during reasoning. The authors conduct extensive experiments with various models, including Qwen3-8B, DeepSeek-R1-Distill-Qwen-7B, and Olmo-3-7B-Instruct, to validate their findings. They analyze the relationship between conditioning context richness, task coverage, and generalization ability, demonstrating that self-distillation can be detrimental to OOD performance when task coverage is limited. The paper provides valuable insights into the trade-offs between in-domain and OOD performance in self-distillation and highlights the importance of considering epistemic verbalization in the design of reasoning tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper addresses a critical and timely issue in the field of LLMs: the impact of self-distillation on reasoning capabilities, particularly in mathematical tasks. This is an important area of research as self-distillation is increasingly used to improve model performance and efficiency.

2. The authors provide a comprehensive analysis of the effects of self-distillation on both in-domain and OOD performance, offering a nuanced understanding of the trade-offs involved. The experiments are well-designed and cover a range of models and settings, strengthening the validity of the findings.

3. The paper introduces the concept of epistemic verbalization and its role in reasoning performance, which is a valuable contribution to the field. By highlighting the importance of expressing uncertainty during reasoning, the authors provide new insights into how LLMs can be improved for more robust and reliable performance.

4. The paper is well-written and easy to follow, with clear explanations of the methodology and results. The use of figures and tables effectively communicates the key findings and supports the overall argument.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on mathematical reasoning tasks, which may limit the generalizability of the findings to other types of reasoning tasks or domains. While the authors acknowledge this limitation, further exploration of the impact of self-distillation on other reasoning tasks, such as commonsense reasoning or logical inference, would strengthen the paper's conclusions.

2. The paper does not delve deeply into the underlying mechanisms that cause the observed performance degradation in OOD tasks. While the authors attribute the degradation to the suppression of epistemic verbalization, a more detailed analysis of the specific factors contributing to this phenomenon would be beneficial. For example, investigating the impact of different training objectives or architectural choices on the model's ability to express uncertainty could provide valuable insights.

3. The paper could benefit from a more thorough discussion of the practical implications of the findings. While the authors highlight the trade-offs between in-domain and OOD performance, they do not provide concrete recommendations for how to mitigate the negative effects of self-distillation in real-world applications. For instance, the paper could explore strategies for adapting self-distillation to specific tasks or domains to achieve better OOD performance.

### Suggestions

The authors should consider expanding their experimental scope to include a wider variety of reasoning tasks beyond mathematical problem-solving. This would involve evaluating the impact of self-distillation on tasks such as logical inference, commonsense reasoning, and natural language understanding. For example, in logical inference, the model could be trained to deduce the correct conclusion from a set of premises, and the authors could examine whether self-distillation leads to a degradation in performance on out-of-domain inference tasks. Similarly, in commonsense reasoning, the model could be tasked with answering questions that require understanding of everyday knowledge, and the authors could investigate whether self-distillation affects the model's ability to generalize to unseen scenarios. These additional experiments would provide a more comprehensive understanding of the generalizability of the findings and the potential limitations of self-distillation in different reasoning contexts. Furthermore, it would be beneficial to explore the performance of self-distillation on tasks where the model is already capable of generating concise and confident responses, such as code generation or scientific text summarization. This would help to determine whether self-distillation can be used to improve performance in these scenarios, and if so, under what conditions.

To address the lack of a deep dive into the underlying mechanisms causing the observed performance degradation in OOD tasks, the authors should investigate the impact of different training objectives or architectural choices on the model's ability to express uncertainty. For example, they could explore how different loss functions, such as those that explicitly encourage the model to express uncertainty, affect the model's performance on OOD tasks. Additionally, they could analyze the internal representations of the model to understand how self-distillation alters the model's ability to capture uncertainty. This could involve techniques such as probing the model's hidden states or analyzing the attention patterns. Furthermore, the authors could investigate the impact of different architectural choices, such as the number of layers or the size of the attention heads, on the model's ability to express uncertainty. A more detailed analysis of these factors would provide valuable insights into the mechanisms underlying the observed performance degradation and could lead to strategies for mitigating this issue.

Finally, the authors should provide a more thorough discussion of the practical implications of their findings. This could include concrete recommendations for how to adapt self-distillation to specific tasks or domains to achieve better OOD performance. For instance, they could explore strategies for incorporating uncertainty awareness into the self-distillation process, such as by explicitly training the model to express uncertainty when it is not confident about its answer. They could also investigate the use of techniques such as ensemble methods or adversarial training to improve the model's robustness to OOD tasks. Furthermore, the authors could discuss the trade-offs between in-domain and OOD performance in real-world applications and provide guidance on how to balance these competing objectives. A more detailed discussion of these practical implications would enhance the paper's relevance and impact.

### Questions

1. How does the choice of the base model affect the observed phenomena? Are the findings consistent across different model architectures and sizes?

2. Can the authors provide more insights into the relationship between task coverage and the suppression of epistemic verbalization? How does the model's ability to generalize to unseen tasks influence its tendency to suppress uncertainty?

3. How does the performance of self-distillation vary across different types of mathematical reasoning tasks? Are there specific task characteristics that are more susceptible to the negative effects of self-distillation?

4. What strategies can be employed to mitigate the negative effects of self-distillation on OOD performance, particularly in mathematical reasoning tasks?

### Rating

6

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers for the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support or refute their claims.

**Plan:**
1. Go through each reviewer's comments one by one.
2. For each comment identified as a weakness, find the corresponding section in the paper.
3. Extract evidence (quotes, experimental details, missing citations) from the paper to validate the weakness.
4. If the weakness is about missing information, check if that information is indeed absent.
5. If there are conflicting opinions between reviewers, note them down.
6. Finally, summarize the validation for each weakness.
**Review 1 Weaknesses:**

1. Weakness Statement:
"The paper primarily focuses on mathematical reasoning tasks, which may limit the generalizability of the findings to other types of reasoning tasks or domains."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper explicitly states the focus on mathematical reasoning tasks in the "motivation" section: "Self-distillation, a technique that involves training a model to mimic the predictions of a more capable model, has shown promise in improving performance on in-domain tasks, particularly in mathematical reasoning."
   - The "experiments" section includes subsections like "Off-Policy Self-Distillation (SDPO) with Math Reasoning Tasks" and "On-Policy Self-Distillation with Math Reasoning Tasks," consistently using mathematical reasoning datasets.
   - The "Relationship Between Task Coverage and Generalization Ability" experiment uses the "DAPO-Math-17k dataset, which exposes the model to 14,000 distinct problems, spanning a broad, non-overlapping range of problem types, and evaluation is performed on unseen problem types."

3. Literature Gap Analysis:
   - The paper does not include experiments on other reasoning tasks like commonsense reasoning or logical inference.

4. Validation Analysis:
   - The paper's experimental design and focus are clearly centered around mathematical reasoning tasks. While the "Relationship Between Task Coverage and Generalization Ability" experiment uses a broader dataset, the core analysis and the introduction of epistemic tokens are tied to the mathematical reasoning context.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Explicit focus on mathematical reasoning in the motivation and experimental sections.

1. Weakness Statement:
"The paper does not delve deeply into the underlying mechanisms that cause the observed performance degradation in OOD tasks. While the authors attribute the degradation to the suppression of epistemic verbalization, a more detailed analysis of the specific factors contributing to this phenomenon would be beneficial. For example, investigating the impact of different training objectives or architectural choices on the model's ability to express uncertainty could provide valuable insights."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper introduces the concept of epistemic verbalization and its role in reasoning performance in the "main_idea" and "method" sections.
   - The paper explains the connection between richness of context and task coverage and epistemic verbalization in Section 3.
b) Experiment-related Evidence:
   - The experiments focus on comparing performance with and without explicit epistemic tokens, providing evidence for the impact of this mechanism.
   - The paper does not include experiments varying training objectives or architectural choices to directly investigate their impact on epistemic verbalization.

3. Literature Gap Analysis:
   - The paper cites works related to self-distillation and reasoning but does not deeply explore literature on the mechanisms of epistemic uncertainty in LLMs or the impact of different training objectives on this.

4. Validation Analysis:
   - While the paper identifies epistemic verbalization as a key factor, it doesn't deeply analyze other potential mechanisms or systematically explore the influence of different training objectives or architectures.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper's focus on epistemic verbalization as the primary explanation, without a detailed investigation of other contributing factors or variations in training.

1. Weakness Statement:
"The paper could benefit from a more thorough discussion of the practical implications of the findings. While the authors highlight the trade-offs between in-domain and OOD performance, they do not provide concrete recommendations for how to mitigate the negative effects of self-distillation on OOD performance, particularly in mathematical reasoning tasks."

2. Evidence Collection:
   - The "Conclusion" section summarizes the findings and suggests future work on developing more robust training strategies.
   - The paper does not include a dedicated section or detailed discussion on specific mitigation strategies for OOD performance degradation in self-distillation.

3. Literature Gap Analysis:
   - While the paper cites relevant work on self-distillation and reasoning, it lacks a discussion of specific techniques or strategies for addressing the identified trade-offs.

4. Validation Analysis:
   - The paper focuses on identifying the problem and analyzing its causes but lacks concrete, actionable recommendations for practitioners.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of a dedicated discussion on mitigation strategies in the paper.

**Review 2 Weaknesses:**

1. Weakness Statement:
"The paper's focus on math reasoning tasks limits the generalizability of the findings. While math reasoning is a complex task, it is not representative of all types of reasoning that LLMs are capable of. The authors should consider expanding their experiments to include other types of reasoning tasks, such as commonsense reasoning, logical reasoning, or natural language inference."

2. Evidence Collection:
b) Experiment-related Evidence:
   - As identified in Review 1, the experiments are primarily focused on mathematical reasoning tasks.

3. Literature Gap Analysis:
   - The paper does not include experiments on other reasoning tasks.

4. Validation Analysis:
   - This is a reiteration of the first weakness from Review 1 and is valid.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence:  The experimental design and focus on mathematical reasoning tasks.

1. Weakness Statement:
"The paper does not explore the potential benefits of self-distillation in scenarios where concise and confident reasoning is beneficial, such as in code generation or scientific text summarization. It would be valuable to investigate whether self-distillation can improve performance on these tasks, especially in cases where the model is already capable of generating concise and confident responses."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The experiments are conducted on mathematical reasoning tasks.
   - The paper does not include experiments on code generation or scientific text summarization.

3. Literature Gap Analysis:
   - The paper does not discuss or experiment with self-distillation in the context of code generation or scientific text summarization.

4. Validation Analysis:
   - The paper's scope is limited to mathematical reasoning, and it does not explore the potential of self-distillation in other domains where concise and confident reasoning might be beneficial.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The experimental focus on mathematical reasoning and the absence of experiments in other domains.

1. Weakness Statement:
"The paper does not provide a clear definition of what constitutes a "concise" response. The authors should provide a more precise definition of conciseness and explore how different metrics of conciseness affect the results."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper defines a set of 10 epistemic markers and uses the count of these markers as a measure of epistemic verbalization.
   - The paper uses the length of the generated response as a proxy for conciseness in the "Off-Policy Self-Distillation (SDPO) with Math Reasoning Tasks" section.
b) Experiment-related Evidence:
   - The paper reports the average response length as a metric in the results tables.

3. Literature Gap Analysis:
   - While the paper uses length as a metric for conciseness, it doesn't provide a formal definition or explore other metrics.

4. Validation Analysis:
   - The paper uses length as a proxy for conciseness, but a more formal definition and exploration of different metrics are missing.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The use of length as a metric without a formal definition.

1. Weakness Statement:
"The paper does not explore the potential of using different types of distillation objectives, such as those that explicitly encourage epistemic verbalization. It would be valuable to investigate whether different distillation objectives can mitigate the negative effects of self-distillation on OOD performance."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper uses standard self-distillation objectives (GRPO and SDPO).
   - The paper does not explore distillation objectives that explicitly encourage epistemic verbalization.

3. Literature Gap Analysis:
   - The paper does not discuss or experiment with distillation objectives designed to promote epistemic verbalization.

4. Validation Analysis:
   - The paper focuses on standard self-distillation methods and does not explore alternative objectives that might address the identified issue.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The use of standard self-distillation objectives without exploring alternatives.

**Review 3 Weaknesses:**

1. Weakness Statement:
"The paper primarily focuses on the negative effects of self-distillation on OOD generalization, but it does not explore potential strategies to mitigate these issues or leverage the benefits of self-distillation in certain scenarios."

2. Evidence Collection:
   - The paper's focus is on identifying and explaining the negative impact of self-distillation on OOD performance.
   - The paper does not include a dedicated section or detailed discussion on strategies to mitigate these negative effects or to leverage the benefits of self-distillation in specific scenarios.

3. Literature Gap Analysis:
   - While the paper cites relevant work, it lacks a discussion of techniques for mitigating negative effects or leveraging self-distillation benefits.

4. Validation Analysis:
   - The paper's scope is limited to analyzing the negative consequences of self-distillation without exploring mitigation or positive uses.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper's focus on negative impacts without discussing mitigation or positive uses.

1. Weakness Statement:
"While the paper provides a detailed analysis of the relationship between self-distillation, epistemic verbalization, and OOD generalization, it does not offer a comprehensive theoretical framework to explain these phenomena."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper introduces the concept of epistemic verbalization and its connection to reasoning performance.
   - The paper provides empirical evidence linking epistemic verbalization to the observed performance differences.
   - The paper does not present a formal mathematical or theoretical framework to explain these phenomena.

3. Literature Gap Analysis:
   - The paper builds upon existing work on self-distillation and reasoning but does not develop a novel theoretical framework.

4. Validation Analysis:
   - The paper's explanation is primarily empirical and conceptual, lacking a comprehensive theoretical framework.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The absence of a formal theoretical framework in the paper.

1. Weakness Statement:
"The experiments are primarily conducted on mathematical reasoning tasks, which may limit the generalizability of the findings to other types of reasoning tasks or domains."

2. Evidence Collection:
b) Experiment-related Evidence:
   - As previously established, the experiments are primarily focused on mathematical reasoning tasks.

3. Literature Gap Analysis:
   - The paper does not include experiments on other reasoning tasks.

4. Validation Analysis:
   - This is a consistent limitation across multiple reviews.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The experimental focus on mathematical reasoning tasks.

1. Weakness Statement:
"The paper does not explore the potential benefits of self-distillation in scenarios where concise and confident reasoning is beneficial, such as in code generation or scientific text summarization."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The experiments are conducted on mathematical reasoning tasks.

3. Literature Gap Analysis:
   - The paper does not discuss or experiment with self-distillation in other domains.

4. Validation Analysis:
   - This is a consistent point of concern.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The experimental focus on mathematical reasoning and the absence of experiments in other domains.

1. Weakness Statement:
"The paper does not provide a clear definition of what constitutes a "concise" response. The authors should provide a more precise definition of conciseness and explore how different metrics of conciseness affect the results."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper uses length as a proxy for conciseness.

3. Literature Gap Analysis:
   - A formal definition of conciseness is missing.

4. Validation Analysis:
   - This is a consistent point of concern.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The use of length as a metric without a formal definition.

1. Weakness Statement:
"The paper does not explore the potential of using different types of distillation objectives, such as those that explicitly encourage epistemic verbalization. It would be valuable to investigate whether different distillation objectives can mitigate the negative effects of self-distillation on OOD performance."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper uses standard self-distillation objectives.

3. Literature Gap Analysis:
   - Alternative distillation objectives are not explored.

4. Validation Analysis:
   - This is a consistent point of concern.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The use of standard self-distillation objectives.

**Review 4 Weaknesses:**

1. Weakness Statement:
"The paper's focus on math reasoning tasks limits the generalizability of the findings. While math reasoning is a complex task, it is not representative of all types of reasoning that LLMs are capable of. The authors should consider expanding their experiments to include other types of reasoning tasks, such as commonsense reasoning, logical reasoning, or natural language inference."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The experiments are primarily focused on mathematical reasoning tasks.

3. Literature Gap Analysis:
   - The paper does not include experiments on other reasoning tasks.

4. Validation Analysis:
   - This is a consistent limitation across multiple reviews.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The experimental focus on mathematical reasoning tasks.

1. Weakness Statement:
"The paper does not explore the potential benefits of self-distillation in scenarios where concise and confident reasoning is beneficial, such as in code generation or scientific text summarization. It would be valuable to investigate whether self-distillation can be used to improve performance on these tasks, especially in cases where the model is already capable of generating concise and confident responses."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The experiments are conducted on mathematical reasoning tasks.

3. Literature Gap Analysis:
   - The paper does not discuss or experiment with self-distillation in other domains.

4. Validation Analysis:
   - This is a consistent point of concern.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The experimental focus on mathematical reasoning and the absence of experiments in other domains.

1. Weakness Statement:
"The paper does not provide a clear definition of what constitutes a "concise" response. The authors should provide a more precise definition of conciseness and explore how different metrics of conciseness affect the results."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper uses length as a proxy for conciseness.

3. Literature Gap Analysis:
   - A formal definition of conciseness is missing.

4. Validation Analysis:
   - This is a consistent point of concern.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The use of length as a metric without a formal definition.

1. Weakness Statement:
"The paper does not explore the potential of using different types of distillation objectives, such as those that explicitly encourage epistemic verbalization. It would be valuable to investigate whether different distillation objectives can mitigate the negative effects of self-distillation on OOD performance."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper uses standard self-distillation objectives.

3. Literature Gap Analysis:
   - Alternative distillation objectives are not explored.

4. Validation Analysis:
   - This is a consistent point of concern.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The use of standard self-distillation objectives.

1. Weakness Statement:
"How does the choice of the base model affect the observed phenomena? Are the findings consistent across different model architectures and sizes?"

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper includes experiments with multiple models (Qwen3, DeepSeek-R, Olmo).
   - The results are presented separately for each model, showing variations in the degree of OOD performance degradation.

3. Literature Gap Analysis:
   - The paper does show results for different models, allowing for some assessment of consistency.

4. Validation Analysis:
   - While the paper includes experiments with multiple models, a direct comparison of the *degree* of OOD performance degradation across models for the same task is not explicitly presented in a single table or figure. The results are presented separately for each model.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: Experiments with multiple models are present, but a direct comparison of the magnitude of OOD degradation across models is not explicitly provided.

1. Weakness Statement:
"Can the authors provide more insights into the relationship between task coverage and the suppression of epistemic verbalization?"

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper includes an experiment titled "Relationship Between Task Coverage and Generalization Ability" that directly investigates this relationship.
   - Figure 9 shows the performance of different models on AIME24 and MATH500 with varying training scores, indicating how task coverage affects OOD performance.

3. Literature Gap Analysis:
   - The paper presents experimental evidence for this relationship.

4. Validation Analysis:
   - The paper does provide insights into this relationship through the "Relationship Between Task Coverage and Generalization Ability" experiment.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: The existence of the "Relationship Between Task Coverage and Generalization Ability" experiment and Figure 9.

1. Weakness Statement:
"How does the performance of self-distillation vary across different types of mathematical reasoning tasks? Are there specific task characteristics that are more susceptible to the negative effects of self-distillation?"

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper uses the DAPO-Math-17k dataset, which exposes the model to 14,000 distinct problems, spanning a broad range of problem types.
   - The paper does not explicitly categorize or analyze the performance based on specific types of mathematical reasoning tasks within the DAPO-Math-17k dataset.

3. Literature Gap Analysis:
   - The paper does not provide a detailed analysis of performance variation across different sub-types of mathematical reasoning within the DAPO-Math-17k dataset.

4. Validation Analysis:
   - While the dataset covers a broad range, the paper does not provide a granular analysis of performance across specific sub-types of mathematical reasoning.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The use of a broad dataset, but the lack of explicit analysis across specific sub-types.

1. Weakness Statement:
"How does the performance of self-distillation vary across different types of mathematical reasoning tasks? Are there specific task characteristics that are more susceptible to the negative effects of self-distillation?"

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper uses the DAPO-Math-17k dataset, which exposes the model to 14,000 distinct problems, spanning a broad range of problem types.
   - The paper does not explicitly categorize or analyze the performance based on specific types of mathematical reasoning tasks within the DAPO-Math-17k dataset.

3. Literature Gap Analysis:
   - The paper does not provide a detailed analysis of performance variation across different sub-types of mathematical reasoning within the DAPO-Math-17k dataset.

4. Validation Analysis:
   - While the dataset covers a broad range, the paper does not provide a granular analysis of performance across specific sub-types of mathematical reasoning.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The use of a broad dataset, but the lack of explicit analysis across specific sub-types.

1. Weakness Statement:
"What strategies can be employed to mitigate the negative effects of self-distillation on OOD performance, particularly in mathematical reasoning tasks?"

2. Evidence Collection:
   - The paper focuses on identifying and explaining the negative consequences of self-distillation without exploring mitigation strategies.

3. Literature Gap Analysis:
   - The paper lacks a discussion of techniques for mitigating negative effects.

4. Validation Analysis:
   - The paper does not provide specific strategies for mitigating the negative effects.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper's focus on analysis rather than mitigation strategies.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper presents a compelling investigation into the impact of self-distillation on the reasoning capabilities of large language models (LLMs), with a particular focus on mathematical tasks. The authors introduce the concept of 'epistemic verbalization,' which refers to the explicit expression of uncertainty during reasoning, and they hypothesize that self-distillation can inadvertently suppress this verbalization, leading to performance degradation on out-of-distribution (OOD) tasks. The core methodological approach involves comparing the performance of models trained using in-domain data with those trained using self-distillation, where the model is trained to mimic its own predictions on a more comprehensive dataset. This allows the authors to analyze the relationship between reasoning context richness, task coverage, and generalization ability. The experiments are primarily conducted using various models from the Qwen and DeepSeek families, along with the Olmo model, and are evaluated on a range of mathematical reasoning datasets. The main empirical findings demonstrate that while self-distillation enhances in-domain performance, it often leads to a decline in OOD performance, especially in mathematical reasoning. This decline is correlated with a reduction in epistemic verbalization, suggesting that the model becomes less confident in its reasoning steps when it is self-distilled. The authors further explore the impact of task coverage, showing that models trained on more diverse datasets exhibit better OOD performance. The paper's overall significance lies in its identification of a critical trade-off between in-domain and OOD performance in self-distilled models, and in its emphasis on the importance of epistemic verbalization for robust reasoning. By highlighting the potential for self-distillation to undermine a model's ability to express uncertainty, the paper calls for a more nuanced approach to self-distillation that considers the model's reasoning behavior, rather than solely focusing on performance metrics. This work contributes to a deeper understanding of the complexities of self-distillation and its implications for the reasoning capabilities of LLMs, offering valuable insights for researchers and practitioners in the field.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

2.5


## Strengths:

This paper makes several notable contributions to the field of large language model research. First, the authors provide a novel perspective on self-distillation by highlighting the importance of epistemic verbalization for robust reasoning. This is a significant departure from the traditional view of self-distillation as simply a method for improving in-domain performance. By introducing the concept of epistemic verbalization, the authors offer a new lens through which to understand the behavior of self-distilled models. Second, the paper presents a comprehensive empirical analysis of the effects of self-distillation on mathematical reasoning tasks. The experiments are well-designed and cover a range of models and settings, providing strong evidence for the authors' claims. The use of multiple models, including Qwen3-8B, DeepSeek-R1-Distill-Qwen-7B, and Olmo-3-7B-Instruct, enhances the generalizability of the findings. The authors also explore the relationship between task coverage and OOD performance, demonstrating that models trained on more diverse datasets exhibit better generalization ability. This is an important finding that has implications for the design of training datasets for LLMs. Third, the paper is well-written and easy to follow, with clear explanations of the methodology and results. The use of figures and tables effectively communicates the key findings and supports the overall argument. The authors also provide a thorough discussion of the implications of their findings, which is essential for guiding future research. Finally, the paper addresses a critical and timely issue in the field of LLMs: the impact of self-distillation on reasoning capabilities. As self-distillation becomes increasingly popular, it is essential to understand its potential limitations and to develop strategies for mitigating these limitations. This paper makes a valuable contribution to this area of research, offering insights that are relevant to both researchers and practitioners.


## Weaknesses:

Despite its strengths, this paper has several limitations that warrant careful consideration. First, the paper's primary focus on mathematical reasoning tasks limits the generalizability of its findings. While mathematical reasoning is a complex task, it is not representative of all types of reasoning that LLMs are capable of. The authors do not explore the impact of self-distillation on other types of reasoning tasks, such as commonsense reasoning, logical inference, or natural language understanding. This is a significant limitation, as it is possible that the observed degradation of OOD performance is specific to mathematical reasoning and may not generalize to other domains. The paper's experimental design and focus are clearly centered around mathematical reasoning tasks, as evidenced by the 'motivation' section, 'experiments' section, and 'Relationship Between Task Coverage and Generalization Ability' experiment. This narrow focus raises concerns about the broader applicability of the findings. Second, the paper does not delve deeply into the underlying mechanisms that cause the observed performance degradation in OOD tasks. While the authors attribute the degradation to the suppression of epistemic verbalization, they do not provide a detailed analysis of the specific factors contributing to this phenomenon. For example, the paper does not investigate the impact of different training objectives or architectural choices on the model's ability to express uncertainty. The paper introduces the concept of epistemic verbalization and its connection to reasoning performance, but it does not deeply analyze other potential mechanisms or systematically explore the influence of different training objectives or architectures. This lack of a deeper analysis limits the paper's ability to provide a comprehensive understanding of the problem. Third, the paper lacks a thorough discussion of the practical implications of its findings. While the authors highlight the trade-offs between in-domain and OOD performance, they do not provide concrete recommendations for how to mitigate the negative effects of self-distillation on OOD performance, particularly in mathematical reasoning tasks. The paper focuses on identifying the problem and analyzing its causes but lacks a detailed discussion on specific mitigation strategies. This absence of practical guidance reduces the paper's relevance for practitioners who are looking for solutions to the identified issues. Fourth, the paper does not provide a clear definition of what constitutes a 'concise' response. The authors use the length of the generated response as a proxy for conciseness, but they do not provide a formal definition or explore how different metrics of conciseness affect the results. This lack of a precise definition makes it difficult to interpret the results and to compare them with other studies. The paper uses length as a metric without a formal definition, which is a significant limitation. Fifth, the paper does not explore the potential of using different types of distillation objectives that explicitly encourage epistemic verbalization. The paper uses standard self-distillation objectives (GRPO and SDPO) but does not explore alternative objectives that might address the identified issue. This lack of exploration limits the paper's ability to identify potential solutions to the problem. Finally, the paper does not explore the potential benefits of self-distillation in scenarios where concise and confident reasoning is beneficial, such as in code generation or scientific text summarization. The experiments are conducted on mathematical reasoning tasks, and the paper does not include experiments on other domains where concise and confident reasoning might be beneficial. This narrow focus limits the paper's ability to demonstrate the broader applicability of self-distillation. These limitations, while not invalidating the paper's findings, highlight areas where further research is needed to fully understand the implications of self-distillation on LLMs.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should expand their experimental scope to include a wider variety of reasoning tasks beyond mathematical problem-solving. This would involve evaluating the impact of self-distillation on tasks such as logical inference, commonsense reasoning, and natural language understanding. For example, in logical inference, the model could be trained to deduce the correct conclusion from a set of premises, and the authors could examine whether self-distillation leads to a degradation in performance on out-of-domain inference tasks. Similarly, in commonsense reasoning, the model could be tasked with answering questions that require understanding of everyday knowledge, and the authors could investigate whether self-distillation affects the model's ability to generalize to unseen scenarios. These additional experiments would provide a more comprehensive understanding of the generalizability of the findings and the potential limitations of self-distillation in different reasoning contexts. Furthermore, it would be beneficial to explore the performance of self-distillation on tasks where the model is already capable of generating concise and confident responses, such as code generation or scientific text summarization. This would help to determine whether self-distillation can be used to improve performance in these scenarios, and if so, under what conditions. Second, to address the lack of a deep dive into the underlying mechanisms causing the observed performance degradation in OOD tasks, the authors should investigate the impact of different training objectives or architectural choices on the model's ability to express uncertainty. For example, they could explore how different loss functions, such as those that explicitly encourage the model to express uncertainty when it is not confident about its answer, affect the model's performance on OOD tasks. Additionally, they could analyze the internal representations of the model to understand how self-distillation alters the model's ability to capture uncertainty. This could involve techniques such as probing the model's hidden states or analyzing the attention patterns. Furthermore, the authors could investigate the impact of different architectural choices, such as the number of layers or the size of the attention heads, on the model's ability to express uncertainty. A more detailed analysis of these factors would provide valuable insights into the mechanisms underlying the observed performance degradation and could lead to strategies for mitigating this issue. Third, the authors should provide a more thorough discussion of the practical implications of their findings. This could include concrete recommendations for how to adapt self-distillation to specific tasks or domains to achieve better OOD performance. For instance, the authors could explore strategies such as regularization techniques that encourage the model to maintain a balance between concise and diverse responses, or adaptive self-distillation strategies that dynamically adjust the distillation process based on the model's uncertainty or the task at hand. Furthermore, the authors could discuss the trade-offs between in-domain and OOD performance in more detail, providing guidance on how to balance these competing objectives. A more detailed discussion of these practical implications would enhance the paper's relevance and impact. Fourth, the authors should provide a more precise definition of 'conciseness' and explore how different metrics of conciseness affect the results. This could involve using metrics such as the number of tokens, the number of distinct words, or the perplexity of the generated text. The authors could then investigate how these different metrics correlate with the observed performance degradation on out-of-domain tasks. This would provide a more nuanced understanding of the relationship between conciseness and reasoning performance. Additionally, the authors should explore the impact of different training strategies on the model's ability to generate concise and confident responses. For example, they could investigate whether techniques such as reinforcement learning or adversarial training can be used to encourage the model to produce more concise responses without sacrificing performance. This would help to determine whether different distillation objectives can mitigate the negative effects of self-distillation on OOD performance. Finally, the authors should explore the potential of using different types of distillation objectives that explicitly encourage epistemic verbalization. This could involve using objectives that penalize the model for being overly confident or for failing to express uncertainty when appropriate. For example, the authors could investigate the use of objectives that encourage the model to explicitly state when it is unsure about its answer, or to provide evidence for its reasoning steps. This would help to determine whether different distillation objectives can mitigate the negative effects of self-distillation on OOD performance. Furthermore, the authors should investigate the impact of different teacher-student architectures on the effectiveness of self-distillation. For example, they could explore the use of different types of teachers, such as those that are trained on a more diverse dataset, or those that are trained using different objectives. This would help to determine whether the effectiveness of self-distillation is dependent on the specific architecture of the teacher and student models.


## Questions:

Several key questions arise from my analysis of this paper. First, how does the choice of the base model affect the observed phenomena? Are the findings consistent across different model architectures and sizes? While the paper includes experiments with multiple models, a more direct comparison of the *degree* of OOD performance degradation across models for the same task is not explicitly presented in a single table or figure. The results are presented separately for each model, making it difficult to assess the consistency of the findings across different model architectures. Second, can the authors provide more insights into the relationship between task coverage and the suppression of epistemic verbalization? While the paper includes an experiment titled 'Relationship Between Task Coverage and Generalization Ability' that directly investigates this relationship, the analysis is not as granular as it could be. It would be beneficial to see a more detailed analysis of how different task coverages affect the model's ability to express uncertainty and its OOD performance. Third, how does the performance of self-distillation vary across different types of mathematical reasoning tasks? Are there specific task characteristics that are more susceptible to the negative effects of self-distillation? The paper uses the DAPO-Math-17k dataset, which exposes the model to a broad range of problem types, but it does not explicitly categorize or analyze the performance based on specific types of mathematical reasoning tasks within the dataset. It would be valuable to see a more granular analysis of performance across different sub-types of mathematical reasoning. Fourth, what strategies can be employed to mitigate the negative effects of self-distillation on OOD performance, particularly in mathematical reasoning tasks? The paper focuses on identifying and explaining the negative consequences of self-distillation without exploring mitigation strategies. It would be beneficial to see a more detailed discussion of potential strategies for addressing this issue, such as regularization techniques or adaptive self-distillation strategies. Finally, how does the choice of the base model affect the observed phenomena? Are the findings consistent across different model architectures and sizes? While the paper includes experiments with multiple models, a more direct comparison of the *degree* of OOD performance degradation across models for the same task is not explicitly presented in a single table or figure. The results are presented separately for each model, making it difficult to assess the consistency of the findings across different model architectures. These questions highlight areas where further research is needed to fully understand the implications of self-distillation on LLMs and to develop effective strategies for mitigating its negative effects.


## Rating:

5.5


## Confidence:

3.25


## Decision:

Reject
}