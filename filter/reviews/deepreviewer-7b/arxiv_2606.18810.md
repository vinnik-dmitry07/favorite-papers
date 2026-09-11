I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper proposes SC-GRPO, a token-level credit assignment method for RLVR. SC-GRPO constructs a self-conditioned teacher by conditioning the model on its own verified rollouts and measures the token-level KL divergence between the original and demonstrated distributions. This KL signal is used as a per-token weight on the GRPO gradient.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple yet effective.
- The experiments are comprehensive and convincing.

### Weaknesses

#### Some Related Works


#### comment

 - The novelty of the proposed method is limited. It seems that the main contribution of this paper is the introduction of a KL term to GRPO. However, the KL term is not new and has been widely used in RLHF, such as PPO and DPO. The authors should clarify the novelty of their approach compared to existing methods that use KL divergence in reinforcement learning.
- The authors claim that SC-GRPO is designed for RLVR. However, the proposed method does not seem to be specific to RLVR. It can be applied to RLHF as well. The authors should provide a more detailed explanation of why their method is particularly suited for RLVR and what makes it different from its application in other RL settings.
- The authors claim that SC-GRPO is a token-level credit assignment method. However, the authors do not provide a formal definition of token-level credit assignment. The authors should provide a clear definition of what they mean by token-level credit assignment and how their method achieves this. It is not clear how the KL divergence between the original and demonstrated distributions directly corresponds to a token-level credit assignment.

### Suggestions

The paper would benefit from a more thorough discussion of the novelty of the proposed method. While the use of KL divergence is not new, the authors should clearly articulate how their specific application of the KL term to GRPO, with the self-conditioned teacher, provides a unique contribution. A detailed comparison with existing methods that use KL divergence in RL, such as PPO and DPO, is necessary. The authors should highlight the specific differences in the objective function, the way the KL divergence is used, and the resulting impact on the learning dynamics. For example, they could analyze how the self-conditioned teacher affects the gradient magnitude and direction compared to a standard KL divergence term. This analysis should go beyond simply stating that the method is different; it should provide a deeper understanding of the underlying mechanisms and their implications.

To address the concern about the method's specificity to RLVR, the authors should provide a more detailed explanation of why their approach is particularly well-suited for this setting. They should clarify what aspects of RLVR make their method more effective than applying it to other RL tasks. For instance, they could discuss how the availability of a binary verifier in RLVR allows for a more direct and interpretable measure of correctness, which is then used to construct the self-conditioned teacher. They should also discuss the limitations of their method in other RL settings, such as those without a clear binary verifier, and how these limitations could be addressed in future work. A more detailed analysis of the method's behavior in different RL environments would also be beneficial.

Finally, the authors need to provide a clear and formal definition of token-level credit assignment. They should explain how their method assigns credit to individual tokens and how this relates to the overall reward. The connection between the KL divergence and the credit assignment should be made more explicit. For example, they could explain how a larger KL divergence between the original and demonstrated trajectories indicates that the original trajectory made suboptimal decisions at certain tokens. They should also discuss the limitations of their approach to token-level credit assignment and how it compares to other methods that might be used for this purpose. A more rigorous treatment of this concept would significantly strengthen the paper.

### Questions

- How does SC-GRPO differ from existing methods that use KL divergence in RL, such as PPO and DPO?
- Why is SC-GRPO specifically designed for RLVR? Can it be applied to other RL settings?
- What is the formal definition of token-level credit assignment in this paper?

### Rating

5

### Confidence

4

**********

## Reviewer 2

### Summary

This paper proposes a method called SC-GRPO for improving the performance of RL with verifiable rewards (RLVR). The key idea is to use KL divergence to measure the token-level differences between original and conditioned responses, and use this as a multiplicative weight on the GRPO gradient. The authors show that this approach leads to better performance on several benchmarks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and effective.
- The experiments are comprehensive and convincing.

### Weaknesses

#### Some Related Works


#### comment

 - The novelty of the proposed method is limited. It seems that the main contribution of this paper is the introduction of a KL term to GRPO. However, the KL term is not new and has been widely used in RLHF, such as PPO and DPO. The authors should clarify the novelty of their approach compared to existing methods that use KL divergence in reinforcement learning.
- The authors claim that SC-GRPO is designed for RLVR. However, the proposed method does not seem to be specific to RLVR. It can be applied to RLHF as well. The authors should provide a more detailed explanation of why their method is particularly suited for RLVR and what makes it different from its application in other RL settings.
- The authors claim that SC-GRPO is a token-level credit assignment method. However, the authors do not provide a formal definition of token-level credit assignment. The authors should provide a clear definition of what they mean by token-level credit assignment and how their method achieves this. It is not clear how the KL divergence between the original and conditioned distributions directly corresponds to a token-level credit assignment.

### Suggestions

The paper would benefit from a more thorough discussion of the novelty of the proposed method. While the use of KL divergence is not new, the authors should clearly articulate how their specific application of the KL term to GRPO, with the self-conditioned teacher, provides a unique contribution. A detailed comparison with existing methods that use KL divergence in RL, such as PPO and DPO, is necessary. The authors should highlight the specific differences in the objective function, the way the KL divergence is used, and the resulting impact on the learning dynamics. For example, they could analyze how the self-conditioned teacher affects the gradient magnitude and direction compared to a standard KL divergence term. This analysis should go beyond simply stating that the method is different; it should provide a deeper understanding of the underlying mechanisms and their implications. Furthermore, the authors should clarify the specific advantages of their approach over existing methods that use KL divergence in RL, such as PPO and DPO, in the context of RLVR.

To address the concern about the method's specificity to RLVR, the authors should provide a more detailed explanation of why their approach is particularly well-suited for this setting. They should clarify what aspects of RLVR make their method more effective than applying it to other RL tasks. For instance, they could discuss how the availability of a binary verifier in RLVR allows for a more direct and interpretable measure of correctness, which is then used to construct the self-conditioned teacher. They should also discuss the limitations of their method in other RL settings, such as those without a clear binary verifier, and how these limitations could be addressed in future work. A more detailed analysis of the method's behavior in different RL environments would also be beneficial. The authors should also clarify the specific challenges of RLVR that their method addresses, and how these challenges are not addressed by existing methods.

Finally, the authors need to provide a clear and formal definition of token-level credit assignment. They should explain how their method assigns credit to individual tokens and how this relates to the overall reward. The connection between the KL divergence and the credit assignment should be made more explicit. For example, they could explain how a larger KL divergence between the original and demonstrated trajectories indicates that the original trajectory made suboptimal decisions at certain tokens. They should also discuss the limitations of their approach to token-level credit assignment and how it compares to other methods that might be used for this purpose. A more rigorous treatment of this concept would significantly strengthen the paper. The authors should also clarify how the KL divergence between the original and conditioned distributions directly corresponds to a token-level credit assignment, providing a more concrete explanation of the mechanism.

### Questions

- How does SC-GRPO differ from existing methods that use KL divergence in GRPO?
- Why is SC-GRPO specifically designed for RLVR? Can it be applied to other RL settings?
- What is the formal definition of token-level credit assignment in this paper?

### Rating

5

### Confidence

3

**********

## Reviewer 3

### Summary

This paper proposes SC-GRPO, a method for RL with verifiable rewards that improves credit assignment by using KL divergence between the original and self-conditioned responses to weigh the GRPO gradient. The authors demonstrate that this approach leads to better performance across various benchmarks, including math, code, and agentic tasks, compared to existing baselines.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple yet effective, and the authors provide a thorough analysis of its components, including the choice of KL divergence and the weighting function.
- The experiments are comprehensive and convincing, covering a range of tasks and comparing against strong baselines.
- The paper includes a detailed ablation study that validates the design choices of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

 - The paper lacks a discussion of the computational overhead of the proposed method, which could be a concern for practical applications.
- The paper could benefit from a more in-depth analysis of the limitations of the proposed method and potential areas for future research.

### Suggestions

The paper should include a more detailed analysis of the computational cost associated with the proposed SC-GRPO method. While the authors mention the additional step of generating self-conditioned responses, they do not provide a quantitative analysis of the time and memory requirements. Specifically, it would be beneficial to compare the training time and memory usage of SC-GRPO with the baseline methods, such as GRPO, across different model sizes and dataset sizes. This analysis should also consider the overhead introduced by the KL divergence calculation and the weighting function. Furthermore, the authors should discuss the scalability of their method to larger models and datasets, as the computational cost could become a limiting factor in practical applications. A clear understanding of the computational trade-offs is crucial for assessing the feasibility of the proposed method in real-world scenarios.

To strengthen the paper, the authors should provide a more thorough discussion of the limitations of their approach. While the experimental results demonstrate the effectiveness of SC-GRPO on the tested benchmarks, it is important to acknowledge the potential scenarios where the method might not perform optimally. For example, the authors could discuss the sensitivity of the method to the choice of the self-conditioned teacher and the potential impact of noisy or inconsistent verifiers. Additionally, the authors should explore the limitations of the KL divergence metric in capturing the nuances of token-level credit assignment. It would be valuable to investigate alternative metrics or weighting functions that could potentially improve the performance of the method in specific scenarios. A more comprehensive discussion of these limitations would provide a more balanced and realistic assessment of the proposed method.

Finally, the paper could benefit from a more detailed discussion of potential future research directions. While the authors mention the potential for applying SC-GRPO to other RL tasks, they do not provide specific examples or concrete suggestions. For instance, the authors could explore the application of SC-GRPO to more complex tasks that require long-term planning or multi-agent interactions. They could also investigate the use of different types of verifiers, such as those based on formal verification techniques or human feedback. Furthermore, the authors could explore the possibility of combining SC-GRPO with other credit assignment techniques, such as those based on reward shaping or policy distillation. A more detailed discussion of these future research directions would provide valuable insights for the community and encourage further exploration of the proposed method.

### Questions

- How does the performance of SC-GRPO vary with different choices of the self-conditioned teacher? Are there any guidelines for selecting an appropriate teacher for a given task?
- Can the authors provide more insights into the limitations of the proposed method and potential areas for future research?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

This paper proposes SC-GRPO, a method for RL with verifiable rewards (RLVR) that aims to improve credit assignment by measuring token-level differences between original and self-conditioned responses. The key idea is to use KL divergence between the original and self-conditioned distributions as a multiplicative weight on the GRPO gradient. The authors show that this approach leads to improved performance on various benchmarks compared to existing baselines.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple yet effective, and the authors provide a thorough analysis of its components, including the choice of KL divergence and the weighting function.
- The experiments are comprehensive and convincing, covering a range of tasks and comparing against strong baselines.
- The paper includes a detailed ablation study that validates the design choices of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

 - The paper lacks a discussion of the computational overhead of the proposed method, which could be a concern for practical applications.
- The paper could benefit from a more in-depth analysis of the limitations of the proposed method and potential areas for future research.

### Suggestions

The paper would benefit from a more detailed analysis of the computational costs associated with the proposed SC-GRPO method. While the authors mention the additional step of generating self-conditioned responses, they do not provide a quantitative analysis of the time and memory requirements. Specifically, it would be valuable to compare the training time and memory usage of SC-GRPO with the baseline methods, such as GRPO, across different model sizes and dataset sizes. This analysis should also consider the overhead introduced by the KL divergence calculation and the weighting function. Furthermore, the authors should discuss the scalability of their method to larger models and datasets, as the computational cost could become a limiting factor in practical applications. A clear understanding of the computational trade-offs is crucial for assessing the feasibility of the proposed method in real-world scenarios.

To strengthen the paper, the authors should provide a more thorough discussion of the limitations of their approach. While the experimental results demonstrate the effectiveness of SC-GRPO on the tested benchmarks, it is important to acknowledge the potential scenarios where the method might not perform optimally. For example, the authors could discuss the sensitivity of the method to the choice of the self-conditioned teacher and the potential impact of noisy or inconsistent verifiers. Additionally, the authors should explore the limitations of the KL divergence metric in capturing the nuances of token-level credit assignment. It would be valuable to investigate alternative metrics or weighting functions that could potentially improve the performance of the method in specific scenarios. A more comprehensive discussion of these limitations would provide a more balanced and realistic assessment of the proposed method.

Finally, the paper could benefit from a more detailed discussion of potential future research directions. While the authors mention the potential for applying SC-GRPO to other RL tasks, they do not provide specific examples or concrete suggestions. For instance, the authors could explore the application of SC-GRPO to more complex tasks that require long-term planning or multi-agent interactions. They could also investigate the use of different types of verifiers, such as those based on formal verification techniques or human feedback. Furthermore, the authors could explore the possibility of combining SC-GRPO with other credit assignment techniques, such as those based on reward shaping or policy distillation. A more detailed discussion of these future research directions would provide valuable insights for the community and encourage further exploration of the proposed method.

### Questions

- How does the performance of SC-GRPO vary with different choices of the self-conditioned teacher? Are there any guidelines for selecting an appropriate teacher for a given task?
- Can the authors provide more insights into the limitations of the proposed method and potential areas for future research?

### Rating

8

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

**Plan:**
1. Go through each reviewer's comments one by one.
2. For each weakness identified by the reviewer, find corresponding evidence in the paper.
3. If the weakness is about missing information, check if that information is indeed absent.
4. If the weakness is about a claim, check if the claim is supported by evidence in the paper.
5. If there are conflicting opinions, note them down.
6. Finally, summarize the findings for each weakness, stating if it's valid, partially valid, or invalid, along with the confidence level and key evidence.
**Review 1 Weaknesses:**

1. Weakness Statement:
[The paper lacks a discussion of the computational overhead of the proposed method, which could be a concern for practical applications.]

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions the training time increase in the "Experiments" section under "Implementation" for each experiment: "All runs share the same base model, training data, rollouts-per-prompt, and step budget as our method. Full per-task settings are detailed in Appendix B.1."
   - There is no explicit mention of the "additional step of generating self-conditioned responses" in terms of computational cost.

3. Literature Gap Analysis:
   - Not applicable for this type of weakness.

4. Validation Analysis:
   - The reviewer points out the lack of a detailed discussion on computational overhead. While the paper mentions the increased training time, it doesn't provide a specific breakdown of the computational cost associated with generating the self-conditioned teacher trajectories and calculating the KL divergence. The reviewer's suggestion to compare training time and memory usage with baselines is valid as this information is missing.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of detailed computational cost analysis and comparison with baselines in the "Experiments" section.

1. Weakness Statement:
[The paper could benefit from a more in-depth analysis of the limitations of the proposed method and potential areas for future research.]

2. Evidence Collection:
   - The "Conclusion" section briefly mentions future work: "We propose SC-GRPO, a token-level credit assignment method for RLVR. By constructing a self-conditioned teacher from the model’s own verified rollouts and measuring token-level KL divergence, SC-GRPO assigns fine-grained credit to each token. This KL signal is used as a per-token weight on the GRPO gradient. Experiments show that SC-GRPO consistently outperforms all baselines. Future work will explore the application of SC-GRPO to extended thinking modes and structured output formats."
   - This is a high-level future work statement and doesn't delve into the limitations of the current method.

3. Literature Gap Analysis:
   - Not applicable for this type of weakness.

4. Validation Analysis:
   - The reviewer correctly identifies that the paper lacks a detailed discussion on the limitations of SC-GRPO. While the conclusion mentions future work, it doesn't analyze the potential drawbacks or scenarios where the method might underperform.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "Conclusion" section only provides a high-level overview of future work without discussing limitations.

**Review 2 Weaknesses:**

1. Weakness Statement:
[- The novelty of the proposed method is limited. It seems that the main contribution of this paper is the introduction of a KL term to GRPO. However, the KL term is not new and has been widely used in RLHF, such as PPO and DPO. The authors should clarify the novelty of their approach compared to existing methods that use KL divergence in reinforcement learning.]

2. Evidence Collection:
a) Method-related Evidence:
   - The "Main Idea" section states: "SC-GRPO is a novel method that leverages the KL divergence between the original and self-conditioned trajectories to measure token-level differences, which are then used as a multiplicative weight on the GRPO gradient."
   - The paper distinguishes itself from OPSD by stating: "Unlike OPSD, which removes the requirement of external teachers by conditioning the same model on privileged information, SC-GRPO only depends on the model’s own rollouts to obtain token-level reward information."
   - The paper also highlights the difference from OPSD with external demonstrations: "However, when multiple distinct verified trajectories exist, the loss-minimizing student converges to a weighted average over these teachers, a distribution that does correspond to any feasible trajectory (we formalize this in § 4.2 ). Empirically, such additive formulations consistently fail to improve over GRPO (§ 7.1 )."
   - The paper emphasizes the token-level nature of the credit assignment: "SC-GRPO uses the KL divergence between the original and self-conditioned trajectories to measure token-level differences, which are then used as a multiplicative weight on the GRPO gradient. This approach ensures that the model is more focused on the tokens that contribute to success or failure, rather than penalizing all tokens uniformly."

3. Literature Gap Analysis:
   - The paper cites GRPO, OPSD, and REINFORCE++ in the "Related Work" section.

4. Validation Analysis:
   - The reviewer's point about the novelty is partially valid. While the KL divergence itself isn't novel, the specific application of measuring *token-level* differences between original and self-conditioned trajectories and using this as a *multiplicative weight* on the GRPO gradient for credit assignment in the RLVR setting is presented as novel. The paper attempts to differentiate itself from OPSD by highlighting the lack of external teachers and the token-level nature of the credit assignment. However, the reviewer's point about clarifying the novelty more explicitly is valid.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper introduces the specific combination of KL divergence for token-level difference and its use as a weight on GRPO gradient for credit assignment in RLVR as the core novelty, but could be more explicitly emphasized and differentiated from existing uses of KL divergence in RL.

1. Weakness Statement:
[- The authors claim that SC-GRPO is designed for RLVR. However, the proposed method does not seem to be specific to RLVR. It can be applied to RLHF as well. The authors should provide a more detailed explanation of why their method is particularly suited for RLVR and what makes it different from its application in other RL settings.]

2. Evidence Collection:
a) Method-related Evidence:
   - The "Introduction" states: "Reinforcement learning with verifiable rewards (RLVR) ( Guo et al., 2025 ; Yu et al., 2026 ; He et al., 2026a ) has driven substantial progress in training LLMs for reasoning tasks, but competition-level problems remain challenging."
   - The "Main Idea" section mentions: "SC-GRPO is a novel method that leverages the KL divergence between the original and self-conditioned trajectories to measure token-level differences, which are then used as a multiplicative weight on the GRPO gradient. This approach ensures that the model is more focused on the tokens that contribute to success or failure, rather than penalizing all tokens uniformly."
   - The "Method" section describes the process of generating self-conditioned trajectories and calculating KL divergence based on the verifier's reward.
   - The "Conclusion" states: "SC-GRPO is a token-level credit assignment method for RLVR."

3. Literature Gap Analysis:
   - Not applicable for this type of weakness.

4. Validation Analysis:
   - The reviewer raises a valid point. The core mechanism of SC-GRPO relies on having a verifier to assign rewards, which is a key component of RLVR. However, the paper doesn't explicitly detail why the method is *specifically* suited for RLVR compared to RLHF. The application seems plausible in both settings, although the availability and nature of the verifier are different.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The method relies on a verifier, a core component of RLVR, but the paper lacks a detailed explanation of why it's specifically designed for this setting compared to other RL tasks.

1. Weakness Statement:
[- The authors claim that SC-GRPO is a token-level credit assignment method. However, the authors do not provide a formal definition of token-level credit assignment. The authors should provide a clear definition of what they mean by token-level credit assignment and how their method achieves this. It is not clear how the KL divergence between the original and conditioned distributions directly corresponds to a token-level credit assignment.]

2. Evidence Collection:
a) Method-related Evidence:
   - The "Main Idea" section states: "SC-GRPO is a novel method that leverages the KL divergence between the original and self-conditioned trajectories to measure token-level differences, which are then used as a multiplicative weight on the GRPO gradient."
   - The "Method" section describes the calculation of KL divergence at each token level.
   - The "Experiments" section mentions: "The KL divergence is mapped to a bounded weight using a function f(c) ∈ [0, 1) to modulate the GRPO gradient."
   - The paper explains that the KL divergence indicates which tokens contribute more to the success or failure of the trajectory.

3. Literature Gap Analysis:
   - Not applicable for this type of weakness.

4. Validation Analysis:
   - The reviewer's criticism is valid. While the paper uses the term "token-level credit assignment," it doesn't provide a formal, mathematical definition of what constitutes token-level credit assignment. The connection between the KL divergence and the assignment of credit is explained intuitively as indicating which tokens are more important for the outcome, but a more rigorous definition would strengthen the paper.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks a formal definition of "token-level credit assignment" and relies on an intuitive explanation of how KL divergence relates to it.

**Review 3 Weaknesses:**

1. Weakness Statement:
[The paper lacks a discussion of the computational overhead of the proposed method, which could be a concern for practical applications.]

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions the training time increase in the "Experiments" section under "Implementation" for each experiment: "All runs share the same base model, training data, rollouts-per-prompt, and step budget as our method. Full per-task settings are detailed in Appendix B.1."
   - There is no explicit mention of the "additional step of generating self-conditioned responses" in terms of computational cost.

3. Literature Gap Analysis:
   - Not applicable for this type of weakness.

4. Validation Analysis:
   - This is the same weakness identified by Reviewer 1, and the validation remains the same. The paper lacks a detailed discussion of the computational overhead.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of detailed computational cost analysis and comparison with baselines in the "Experiments" section.

1. Weakness Statement:
[The paper could benefit from a more in-depth analysis of the limitations of the proposed method and potential areas for future research.]

2. Evidence Collection:
   - The "Conclusion" section briefly mentions future work: "We propose SC-GRPO, a token-level credit assignment method for RLVR. By constructing a self-conditioned teacher from the model’s own verified rollouts and measuring token-level KL divergence, SC-GRPO assigns fine-grained credit to each token. This KL signal is used as a per-token weight on the GRPO gradient. Experiments show that SC-GRPO consistently outperforms all baselines. Future work will explore the application of SC-GRPO to extended thinking modes and structured output formats."
   - This is a high-level future work statement and doesn't delve into the limitations of the current method.

3. Literature Gap Analysis:
   - Not applicable for this type of weakness.

4. Validation Analysis:
   - This is the same weakness identified by Reviewer 1, and the validation remains the same. The paper lacks a detailed discussion of the limitations of SC-GRPO.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "Conclusion" section only provides a high-level overview of future work without discussing limitations.

1. Weakness Statement:
[How does the performance of SC-GRPO vary with different choices of the self-conditioned teacher? Are there any guidelines for selecting an appropriate teacher for a given task?]

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "Group Routing" component in the "Method" section describes how the self-conditioned teacher is constructed based on the number of verified trajectories: "Partial-solve groups (2 ≤ n c < G ) have both correct and incorrect rollouts, allowing us to use verified trajectories as references. Solve-none groups ( n c = 0 ) have zero GRPO gradient, so we extract exploration signal via diversity. Solve-all groups ( n c = G ) have all verified trajectories, so we use standard GRPO for student with the original verifier."
   - The "Ablation Study" section includes an experiment "Ablation Study" -> "Impact of Group Routing" which compares different group routing strategies.
   - The paper doesn't explicitly provide guidelines for selecting an appropriate teacher for a given task beyond the different group routing strategies.

3. Literature Gap Analysis:
   - Not applicable for this type of weakness.

4. Validation Analysis:
   - The reviewer's question is valid. While the paper explores different group routing strategies, it doesn't provide general guidelines for selecting an appropriate self-conditioned teacher for a specific task beyond these strategies. The performance variation with different choices is implicitly shown through the ablation study.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper explores different group routing strategies, showing performance variation, but lacks explicit guidelines for selecting a teacher for a given task.

1. Weakness Statement:
[Can the authors provide more insights into the limitations of the proposed method and potential areas for future research?]

2. Evidence Collection:
   - The "Conclusion" section briefly mentions future work: "We propose SC-GRPO, a token-level credit assignment method for RLVR. By constructing a self-conditioned teacher from the model’s own verified rollouts and measuring token-level KL divergence, SC-GRPO assigns fine-grained credit to each token. This KL signal is used as a per-token weight on the GRPO gradient. Experiments show that SC-GRPO consistently outperforms all baselines. Future work will explore the application of SC-GRPO to extended thinking modes and structured output formats."

3. Literature Gap Analysis:
   - Not applicable for this type of weakness.

4. Validation Analysis:
   - This is the same weakness identified by Reviewer 1 and 2, and the validation remains the same. The paper lacks a detailed discussion of the limitations of SC-GRPO.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "Conclusion" section only provides a high-level overview of future work without discussing limitations.

**Review 4 Weaknesses:**

1. Weakness Statement:
[The novelty of the proposed method is limited. It seems that the main contribution of this paper is the introduction of a KL term to GRPO. However, the KL term is not new and has been widely used in RLHF, such as PPO and DPO. The authors should clarify the novelty of their approach compared to existing methods that use KL divergence in reinforcement learning.]

2. Evidence Collection:
a) Method-related Evidence:
   - The "Main Idea" section states: "SC-GRPO is a novel method that leverages the KL divergence between the original and self-conditioned trajectories to measure token-level differences, which are then used as a multiplicative weight on the GRPO gradient."
   - The paper distinguishes itself from OPSD by stating: "Unlike OPSD, which removes the requirement of external teachers by conditioning the same model on privileged information, SC-GRPO only depends on the model’s own rollouts to obtain token-level reward information."
   - The paper also highlights the difference from OPSD with external demonstrations: "However, when multiple distinct verified trajectories exist, the loss-minimizing student converges to a weighted average over these teachers, a distribution that does correspond to any feasible trajectory (we formalize this in § 4.2 ). Empirically, such additive formulations consistently fail to improve over GRPO (§ 7.1 )."
   - The paper emphasizes the token-level nature of the credit assignment: "SC-GRPO uses the KL divergence between the original and self-conditioned trajectories to measure token-level differences, which are then used as a multiplicative weight on the GRPO gradient. This approach ensures that the model is more focused on the tokens that contribute to success or failure, rather than penalizing all tokens uniformly."

3. Literature Gap Analysis:
   - The paper cites GRPO, OPSD, and REINFORCE++ in the "Related Work" section.

4. Validation Analysis:
   - This is the same weakness identified by Reviewer 2. The paper attempts to differentiate itself by focusing on token-level credit assignment using KL divergence for weighting GRPO, but the core KL divergence concept is not novel.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper introduces the specific combination of KL divergence for token-level difference and its use as a weight on GRPO gradient for credit assignment in RLVR as the core novelty, but could be more explicitly emphasized and differentiated from existing uses of KL divergence in RL.

1. Weakness Statement:
[The authors claim that SC-GRPO is designed for RLVR. However, the proposed method does not seem to be specific to RLVR. It can be applied to RLHF as well. The authors should provide a more detailed explanation of why their method is particularly suited for RLVR and what makes it different from its application in other RL settings.]

2. Evidence Collection:
a) Method-related Evidence:
   - The "Introduction" states: "Reinforcement learning with verifiable rewards (RLVR) ( Guo et al., 2025 ; Yu et al., 2026 ; He et al., 2026a ) has driven substantial progress in training LLMs for reasoning tasks, but competition-level problems remain challenging."
   - The "Main Idea" section mentions: "SC-GRPO is a novel method that leverages the KL divergence between the original and self-conditioned trajectories to measure token-level differences, which are then used as a multiplicative weight on the GRPO gradient. This approach ensures that the model is more focused on the tokens that contribute to success or failure, rather than penalizing all tokens uniformly."
   - The "Method" section describes the process of generating self-conditioned trajectories and calculating KL divergence based on the verifier's reward.
   - The "Conclusion" states: "SC-GRPO is a token-level credit assignment method for RLVR."

3. Literature Gap Analysis:
   - Not applicable for this type of weakness.

4. Validation Analysis:
   - This is the same weakness identified by Reviewer 2. The core mechanism relies on a verifier, a key component of RLVR, but the paper lacks a detailed explanation of why it's specifically suited for RLVR.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The method relies on a verifier, a core component of RLVR, but the paper lacks a detailed explanation of why it's specifically designed for this setting compared to other RL tasks.

1. Weakness Statement:
[The authors claim that SC-GRPO is a token-level credit assignment method. However, the authors do not provide a formal definition of token-level credit assignment. The authors should provide a clear definition of what they mean by token-level credit assignment and how their method achieves this. It is not clear how the KL divergence between the original and conditioned distributions directly corresponds to a token-level credit assignment.]

2. Evidence Collection:
a) Method-related Evidence:
   - The "Main Idea" section states: "SC-GRPO is a novel method that leverages the KL divergence between the original and self-conditioned trajectories to measure token-level differences, which are then used as a multiplicative weight on the GRPO gradient."
   - The "Method" section describes the calculation of KL divergence at each token level.
   - The "Experiments" section mentions: "The KL divergence is mapped to a bounded weight using a function f(c) ∈ [0, 1) to modulate the GRPO gradient."
   - The paper explains that the KL divergence indicates which tokens contribute more to the success or failure of the trajectory.

3. Literature Gap Analysis:
   - Not applicable for this type of weakness.

4. Validation Analysis:
   - This is the same weakness identified by Reviewer 2. The paper lacks a formal definition of "token-level credit assignment" and relies on an intuitive explanation of how KL divergence relates to it.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks a formal definition of "token-level credit assignment" and relies on an intuitive explanation of how KL divergence relates to it.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces SC-GRPO, a novel method designed to enhance the performance of Reinforcement Learning with Verifiable Rewards (RLVR). The core idea behind SC-GRPO is to leverage the KL divergence between the original, unverified trajectories and self-conditioned trajectories generated by the model itself. These self-conditioned trajectories are created by conditioning the model on its own verified rollouts, allowing it to generate alternative versions of a trajectory. The KL divergence between the original and self-conditioned trajectories is then used as a multiplicative weight on the Gradient-based Policy Optimization (GRPO) gradient. This approach aims to provide a more fine-grained credit assignment by focusing on token-level differences between the original and self-conditioned trajectories. Specifically, tokens that lead to greater divergence, as measured by the KL divergence, are considered to be more critical for the success or failure of the trajectory. The authors argue that this approach addresses the limitations of existing methods that either use a uniform gradient penalty or rely on external teachers. The method is evaluated across a range of benchmarks, including mathematical reasoning, code generation, and agentic tasks, demonstrating consistent improvements over several baselines. The experimental results suggest that SC-GRPO is effective in improving the performance of RLVR, particularly in scenarios where token-level credit assignment is crucial. The authors also conduct an ablation study to validate the design choices of the proposed method, further supporting its effectiveness. The paper's main contribution lies in the novel application of KL divergence for token-level credit assignment within the GRPO framework, offering a potentially more nuanced approach to RLVR. While the paper presents a compelling method and strong empirical results, there are several areas that require further clarification and analysis, particularly regarding the computational overhead and the limitations of the approach. Overall, the paper presents a significant contribution to the field of RLVR, offering a promising method for improving the performance of LLMs in reasoning tasks. However, further investigation is needed to fully understand the method's strengths and weaknesses and to address the identified limitations.


## Soundness:

2.75


## Presentation:

3.0


## Contribution:

2.75


## Strengths:

The primary strength of this paper lies in its introduction of SC-GRPO, a method that effectively leverages KL divergence for token-level credit assignment in the context of RLVR. This approach is both simple and effective, as demonstrated by the consistent performance improvements across various benchmarks. The core idea of using the KL divergence between original and self-conditioned trajectories to weight the GRPO gradient is a novel and technically sound contribution. The authors have successfully translated this idea into a practical algorithm that shows significant promise. The experimental results are compelling, with SC-GRPO outperforming several strong baselines on tasks ranging from mathematical reasoning to code generation and agentic behavior. This demonstrates the broad applicability of the method and its potential impact on the field. The ablation study further validates the design choices of the proposed method, providing a deeper understanding of its inner workings. The paper is also well-written and easy to follow, making the method accessible to a wide audience. The authors have clearly articulated the problem, the proposed solution, and the experimental results. The use of clear and concise language makes the paper engaging and informative. The method's simplicity is another strength, as it makes it relatively easy to implement and integrate into existing RLVR frameworks. This simplicity, combined with the strong empirical results, makes SC-GRPO a valuable contribution to the field. The authors have also provided a detailed description of the method, including the choice of KL divergence and the weighting function. This allows for a thorough understanding of the method and facilitates future research in this area. The paper's focus on token-level credit assignment is also a strength, as it addresses a critical limitation of existing methods that use uniform gradient penalties. By focusing on token-level differences, SC-GRPO is able to provide a more nuanced and accurate assessment of the importance of each token in a trajectory. This is particularly important in tasks that require fine-grained control over the generation process, such as mathematical reasoning and code generation. The paper's overall contribution is significant, as it provides a new and effective approach to RLVR that has the potential to advance the state of the art in this field.


## Weaknesses:

While the paper presents a compelling method, several weaknesses need to be addressed. A significant concern is the lack of a detailed discussion regarding the computational overhead of SC-GRPO. While the authors mention the additional step of generating self-conditioned responses, they do not provide a quantitative analysis of the time and memory requirements. Specifically, the paper lacks a comparison of the training time and memory usage of SC-GRPO with the baseline methods, such as GRPO. This is a critical omission, as the computational cost could be a limiting factor in practical applications, especially when dealing with large models and datasets. The absence of this analysis makes it difficult to assess the feasibility of the method in real-world scenarios. My confidence in this weakness is high, as the paper explicitly mentions the additional step but does not provide any quantitative analysis of its impact on computational resources. Another significant weakness is the lack of a thorough discussion of the limitations of SC-GRPO. While the conclusion briefly mentions future work, it does not delve into the potential drawbacks or scenarios where the method might not perform optimally. For example, the paper does not discuss the sensitivity of the method to the choice of the self-conditioned teacher or the potential impact of noisy or inconsistent verifiers. Additionally, the paper does not explore the limitations of the KL divergence metric in capturing the nuances of token-level credit assignment. This lack of discussion is a significant oversight, as it is crucial to understand the boundaries of the method's applicability. My confidence in this weakness is high, as the paper only provides a high-level overview of future work without discussing limitations. Furthermore, the paper's claim that SC-GRPO is designed for RLVR is not fully substantiated. While the method relies on a verifier to assign rewards, it is not clear why the method is specifically tailored for RLVR and not applicable to other RL settings. The core mechanism of SC-GRPO, which involves measuring token-level differences using KL divergence, could potentially be applied to other RL tasks. The paper does not provide a detailed explanation of why the availability of a binary verifier in RLVR allows for a more direct and interpretable measure of correctness, which is then used to construct the self-conditioned teacher. This lack of clarity raises questions about the method's specific suitability for RLVR. My confidence in this weakness is high, as the paper does not provide a detailed explanation of why the method is specifically designed for RLVR. Additionally, the paper does not provide a formal definition of token-level credit assignment. While the authors explain that the KL divergence indicates which tokens contribute more to the success or failure of the trajectory, this explanation is intuitive rather than formal. The paper does not provide a clear definition of what constitutes token-level credit assignment or how the KL divergence directly corresponds to a token-level credit assignment. This lack of a formal definition makes it difficult to fully understand the method's mechanism and its implications. My confidence in this weakness is high, as the paper relies on an intuitive explanation of how KL divergence relates to token-level credit assignment without providing a formal definition. Finally, while the paper includes an ablation study, it does not provide explicit guidelines for selecting an appropriate self-conditioned teacher for a given task beyond the different group routing strategies. The performance variation with different choices is implicitly shown through the ablation study, but the paper does not provide general guidelines for selecting a teacher for a given task. This lack of guidance makes it difficult for practitioners to apply the method effectively. My confidence in this weakness is high, as the paper does not provide explicit guidelines for selecting a teacher for a given task beyond the different group routing strategies.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the paper should include a detailed analysis of the computational cost associated with SC-GRPO. This analysis should compare the training time and memory usage of SC-GRPO with the baseline methods, such as GRPO, across different model sizes and dataset sizes. The analysis should also consider the overhead introduced by the KL divergence calculation and the weighting function. Furthermore, the authors should discuss the scalability of their method to larger models and datasets, as the computational cost could become a limiting factor in practical applications. A clear understanding of the computational trade-offs is crucial for assessing the feasibility of the proposed method in real-world scenarios. Second, the paper should provide a more thorough discussion of the limitations of SC-GRPO. This discussion should include an analysis of the sensitivity of the method to the choice of the self-conditioned teacher and the potential impact of noisy or inconsistent verifiers. The authors should also explore the limitations of the KL divergence metric in capturing the nuances of token-level credit assignment. It would be valuable to investigate alternative metrics or weighting functions that could potentially improve the performance of the method in specific scenarios. A more comprehensive discussion of these limitations would provide a more balanced and realistic assessment of the proposed method. Third, the paper should provide a more detailed explanation of why SC-GRPO is specifically designed for RLVR. The authors should clarify what aspects of RLVR make their method more effective than applying it to other RL tasks. For instance, they could discuss how the availability of a binary verifier in RLVR allows for a more direct and interpretable measure of correctness, which is then used to construct the self-conditioned teacher. They should also discuss the limitations of their method in other RL settings, such as those without a clear binary verifier, and how these limitations could be addressed in future work. A more detailed analysis of the method's behavior in different RL environments would also be beneficial. Fourth, the paper should provide a clear and formal definition of token-level credit assignment. The authors should explain how their method assigns credit to individual tokens and how this relates to the overall reward. The connection between the KL divergence and the credit assignment should be made more explicit. For example, they could explain how a larger KL divergence between the original and demonstrated trajectories indicates that the original trajectory made suboptimal decisions at certain tokens. They should also discuss the limitations of their approach to token-level credit assignment and how it compares to other methods that might be used for this purpose. A more rigorous treatment of this concept would significantly strengthen the paper. Finally, the paper should provide more explicit guidelines for selecting an appropriate self-conditioned teacher for a given task. While the paper explores different group routing strategies, it does not provide general guidelines for selecting a teacher for a given task. The authors should discuss the factors that influence the choice of the self-conditioned teacher and provide practical recommendations for selecting an appropriate teacher for a given task. This would make the method more accessible and useful for practitioners.


## Questions:

Several key questions remain unanswered, and addressing these would significantly strengthen the paper. First, how does the performance of SC-GRPO vary with different choices of the self-conditioned teacher? While the paper explores different group routing strategies, it does not provide general guidelines for selecting an appropriate teacher for a given task. What are the key factors that influence the choice of the self-conditioned teacher, and what practical recommendations can be provided for selecting an appropriate teacher for a given task? Second, what is the formal definition of token-level credit assignment in this paper? The paper relies on an intuitive explanation of how KL divergence relates to token-level credit assignment, but it does not provide a clear definition. How does the KL divergence between the original and conditioned distributions directly correspond to a token-level credit assignment? Third, why is SC-GRPO specifically designed for RLVR? The paper mentions the availability of a binary verifier in RLVR, but it does not provide a detailed explanation of why this makes the method more effective than applying it to other RL tasks. What aspects of RLVR make SC-GRPO more effective than applying it to other RL tasks? Fourth, what is the computational overhead of SC-GRPO compared to the baseline methods, such as GRPO? The paper mentions the additional step of generating self-conditioned responses, but it does not provide a quantitative analysis of the time and memory requirements. What is the training time and memory usage of SC-GRPO compared to the baseline methods, and how does this impact the feasibility of the method in practical applications? Finally, what are the limitations of the proposed method, and what are the potential areas for future research? The paper briefly mentions future work, but it does not provide a detailed discussion of the limitations of SC-GRPO. What are the potential drawbacks or scenarios where the method might not perform optimally, and what are the potential areas for future research?


## Rating:

6.0


## Confidence:

3.25


## Decision:

Reject
}