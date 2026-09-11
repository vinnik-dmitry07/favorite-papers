I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper introduces Latent On-Policy Self-Distillation (LOPD), a novel approach to self-distillation that learns privileged context from experience. Unlike previous methods that rely on predefined privileged signals, LOPD uses a learnable latent context generated from retrieved trajectories, allowing it to adaptively identify and leverage relevant experience. The method employs a privileged-margin constraint to ensure that the privileged context remains informative and does not collapse during training. Empirical results show that LOPD outperforms existing methods across multiple benchmarks in both agentic tool-use and code generation tasks, with high learning efficiency.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow. The problem formulation and methodology are clearly presented, making it accessible to readers with varying levels of expertise in self-distillation and latent learning.
- The authors provide a thorough evaluation of LOPD across multiple benchmarks, demonstrating its effectiveness in both agentic tool-use and code generation tasks. The empirical results are compelling, showing that LOPD outperforms existing methods with less than 30% of their rollout budget.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational overhead introduced by the learnable latent context and the retrieval mechanism. Specifically, the paper lacks a breakdown of the time and memory costs associated with the latent vector generation, the retrieval process, and the subsequent distillation. This makes it difficult to assess the practical scalability of the method, especially when dealing with large datasets or complex tasks.
- The paper could benefit from a more thorough comparison with other self-distillation methods that use different forms of privileged information, such as those based on hand-crafted features or external knowledge sources. The current comparison is limited to methods that also use privileged context, but a broader comparison would help to better position the contribution of this work within the broader landscape of self-distillation. For example, it would be useful to see how LOPD compares to methods that use symbolic representations or external knowledge bases as privileged signals.
- The paper does not explore the sensitivity of the method to the number of retrieved trajectories or the choice of the retrieval mechanism. It is unclear how the performance of LOPD is affected by the size of the context library and the similarity metric used for retrieval. A more detailed analysis of these factors would provide valuable insights into the robustness and generalizability of the method.

### Suggestions

The paper would benefit from a more detailed analysis of the computational costs associated with the proposed method. Specifically, the authors should provide a breakdown of the time and memory requirements for each component of LOPD, including the latent vector generation, the retrieval process, and the distillation step. This analysis should include a discussion of how these costs scale with the size of the context library, the length of the trajectories, and the complexity of the tasks. Furthermore, it would be helpful to compare the computational overhead of LOPD with that of the baseline methods, providing a clear picture of the trade-offs between performance and computational cost. This analysis should also consider the practical implications of the method, such as its suitability for real-world applications with limited computational resources.

To better position the contribution of LOPD, the authors should include a more comprehensive comparison with other self-distillation methods that use different forms of privileged information. This comparison should go beyond methods that also use privileged context and include a discussion of how LOPD compares to methods that use hand-crafted features, external knowledge sources, or symbolic representations as privileged signals. For example, the authors could compare LOPD to methods that use explicit skill embeddings or external knowledge bases as privileged signals. This comparison should not only focus on the performance of the methods but also on their computational cost, ease of implementation, and the type of privileged information they require. Such a comparison would provide a more complete picture of the strengths and weaknesses of LOPD and help to better understand its contribution to the field of self-distillation.

Finally, the paper should include a more thorough sensitivity analysis of the method to the number of retrieved trajectories and the choice of the retrieval mechanism. The authors should investigate how the performance of LOPD is affected by the size of the context library and the similarity metric used for retrieval. This analysis should include a discussion of the trade-offs between the size of the context library, the computational cost, and the performance of the method. Furthermore, the authors should explore different retrieval mechanisms, such as k-nearest neighbors or attention-based methods, and discuss their impact on the performance of LOPD. This sensitivity analysis would provide valuable insights into the robustness and generalizability of the method and help to identify the optimal settings for different tasks and datasets.

### Questions

- How does the computational overhead of LOPD compare to that of the baseline methods, especially in terms of training time and memory usage?
- How does the choice of the retrieval mechanism and the number of retrieved trajectories affect the performance of LOPD? Are there any guidelines for selecting these parameters in different settings?
- How does LOPD compare to other self-distillation methods that use different forms of privileged information, such as hand-crafted features or external knowledge sources?

### Rating

6

### Confidence

3

**********

## Reviewer 2

### Summary

This paper proposes a new method called Latent On-Policy Self-Distillation (LOPD) for self-distillation. LOPD learns a latent vector to represent the privileged context, which is used to condition the student policy. The latent vector is learned through a learnable composer, which is optimized jointly with the student policy. The paper shows that LOPD outperforms existing methods on several benchmarks, including tool use and code generation.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.
- The paper provides a comprehensive evaluation of LOPD on several benchmarks, including tool use and code generation.
- The paper shows that LOPD outperforms existing methods on these benchmarks.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational cost of LOPD. The paper mentions that LOPD requires more computational resources than existing methods, but it does not provide a detailed breakdown of the computational cost of each component of LOPD. It would be helpful to understand the computational cost of the learnable composer, the student policy, and the privileged-margin constraint.
- The paper does not provide a detailed analysis of the sensitivity of LOPD to the choice of hyperparameters. It would be helpful to understand how the performance of LOPD is affected by different choices of hyperparameters, such as the learning rate, the batch size, and the number of latent tokens.
- The paper does not provide a detailed analysis of the limitations of LOPD. It would be helpful to understand the scenarios in which LOPD is likely to fail or underperform. For example, it would be helpful to understand how LOPD performs on tasks with long-range dependencies or tasks with sparse rewards.

### Suggestions

The paper would benefit from a more thorough analysis of the computational overhead introduced by the learnable composer. While the authors mention that the composer is lightweight, a detailed breakdown of the computational cost, including FLOPs or training time per iteration, for each component (composer, student policy, and privileged-margin constraint) would be valuable. This analysis should also consider the impact of the number of latent tokens on the computational cost. Furthermore, it would be beneficial to compare the computational cost of LOPD with existing methods more explicitly, perhaps by providing a table that shows the training time and memory usage for each method on the same hardware. This would allow readers to better understand the trade-offs between performance and computational cost.

To address the lack of hyperparameter sensitivity analysis, the authors should conduct a more systematic study of how different hyperparameters affect the performance of LOPD. This study should include a range of values for key hyperparameters such as the learning rate, batch size, and the number of latent tokens. The authors should also explore the impact of different optimization algorithms and learning rate schedules. The results of this analysis should be presented in a clear and concise manner, perhaps using tables or plots that show the performance of LOPD as a function of each hyperparameter. This would help readers to understand the robustness of LOPD and to choose appropriate hyperparameter values for their own applications. It would also be helpful to provide some guidelines for selecting hyperparameters based on the characteristics of the task.

Finally, the paper should include a more detailed discussion of the limitations of LOPD. The authors should explore the performance of LOPD on tasks with long-range dependencies and sparse rewards. For example, it would be interesting to see how LOPD performs on tasks that require the student policy to remember information from several steps in the past, or on tasks where the reward signal is sparse and delayed. The authors should also discuss the potential failure modes of LOPD and suggest possible solutions to address these limitations. This discussion should be supported by experimental results, perhaps by including experiments on more challenging tasks or by providing a theoretical analysis of the limitations of LOPD. This would help readers to understand the scope of applicability of LOPD and to identify areas for future research.

### Questions

- How does the computational cost of LOPD compare to that of existing methods?
- How sensitive is LOPD to the choice of hyperparameters?
- What are the limitations of LOPD?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper proposes a novel method, Latent On-Policy Self-Distillation (LOPD), to improve the learning efficiency of on-policy self-distillation. LOPD introduces a learnable latent privileged context, which is generated by a composer that transforms retrieved experiences into continuous latent tokens. The student policy is then conditioned on these latent tokens, and the teacher policy is conditioned on the same latent tokens plus the original privileged context. The paper demonstrates that LOPD outperforms existing OPSD methods on both agentic tool-use and code generation tasks, with less than 30% of the rollout budget.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow. The authors clearly explain the motivation, methodology, and experimental setup.
- The proposed method, LOPD, is novel and addresses a significant limitation of existing OPSD methods. By introducing a learnable latent privileged context, LOPD allows the privileged context to be learned end-to-end from experience, rather than being hand-crafted or fixed.
- The paper provides a comprehensive evaluation of LOPD on both agentic tool-use and code generation tasks. The results show that LOPD outperforms existing OPSD methods, with less than 30% of the rollout budget. This demonstrates the effectiveness of the proposed method.
- The paper also provides a detailed analysis of the results, including the impact of the privileged-margin constraint and the learnable context. This analysis provides valuable insights into the behavior of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational cost of LOPD. While the paper mentions that LOPD requires more computational resources than existing methods, it does not provide a detailed breakdown of the computational cost of each component of LOPD. This makes it difficult to assess the practical scalability of the method, especially when dealing with large datasets or complex tasks.
- The paper does not provide a detailed analysis of the sensitivity of LOPD to the choice of hyperparameters. It would be helpful to understand how the performance of LOPD is affected by different choices of hyperparameters, such as the learning rate, the batch size, and the number of latent tokens. This would help to identify the optimal settings for different tasks and datasets.
- The paper does not provide a detailed analysis of the limitations of LOPD. It would be helpful to understand the scenarios in which LOPD is likely to fail or underperform. For example, it would be helpful to understand how LOPD performs on tasks with long-range dependencies or tasks with sparse rewards.

### Suggestions

The paper would benefit from a more thorough analysis of the computational overhead introduced by the learnable latent context. While the authors mention that the composer is lightweight, a detailed breakdown of the computational cost, including FLOPs or training time per iteration, for each component (composer, student policy, and privileged-margin constraint) would be valuable. This analysis should also consider the impact of the number of latent tokens on the computational cost. Furthermore, it would be beneficial to compare the computational cost of LOPD with existing methods more explicitly, perhaps by providing a table that shows the training time and memory usage for each method on the same hardware. This would allow readers to better understand the trade-offs between performance and computational cost. The authors should also discuss the potential for optimizing the implementation of LOPD to reduce its computational footprint, such as using more efficient data structures or parallelization techniques.

To address the lack of hyperparameter sensitivity analysis, the authors should conduct a more systematic study of how different hyperparameters affect the performance of LOPD. This study should include a range of values for key hyperparameters such as the learning rate, batch size, and the number of latent tokens. The authors should also explore the impact of different optimization algorithms and learning rate schedules. The results of this analysis should be presented in a clear and concise manner, perhaps using tables or plots that show the performance of LOPD as a function of each hyperparameter. This would help readers to understand the robustness of LOPD and to choose appropriate hyperparameter values for their own applications. It would also be helpful to provide some guidelines for selecting hyperparameters based on the characteristics of the task. For example, the authors could discuss how the optimal learning rate might vary depending on the complexity of the task or the size of the dataset.

Finally, the paper should include a more detailed discussion of the limitations of LOPD. The authors should explore the performance of LOPD on tasks with long-range dependencies and sparse rewards. For example, it would be interesting to see how LOPD performs on tasks that require the student policy to remember information from several steps in the past, or on tasks where the reward signal is sparse and delayed. The authors should also discuss the potential failure modes of LOPD and suggest possible solutions to address these limitations. This discussion should be supported by experimental results, perhaps by including experiments on more challenging tasks or by providing a theoretical analysis of the limitations of LOPD. This would help readers to understand the scope of applicability of LOPD and to identify areas for future research.

### Questions

- How does the computational cost of LOPD compare to that of existing methods?
- How sensitive is LOPD to the choice of hyperparameters?
- What are the limitations of LOPD?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

This paper proposes a new method for on-policy self-distillation called Latent On-Policy Self-Distillation (LOPD). The key idea is to learn a latent vector representing the privileged context from experience, which is then used to condition the student policy. The method uses a learnable composer to transform retrieved experiences into a continuous latent vector, which is then optimized jointly with the student policy. The paper shows that LOPD outperforms existing methods on several benchmarks in both agentic tool-use and code generation tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The idea of learning a latent privileged context from experience is novel and interesting.
- The method is well-motivated and the paper is clearly written.
- The empirical results are promising and show that LOPD outperforms existing methods on several benchmarks.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational cost of LOPD. The paper mentions that LOPD requires more computational resources than existing methods, but it does not provide a detailed breakdown of the computational cost of each component of LOPD. It would be helpful to understand the computational cost of the learnable composer, the student policy, and the privileged-margin constraint.
- The paper does not provide a detailed analysis of the sensitivity of LOPD to the choice of hyperparameters. It would be helpful to understand how the performance of LOPD is affected by different choices of hyperparameters, such as the learning rate, the batch size, and the number of latent tokens.
- The paper does not provide a detailed analysis of the limitations of LOPD. It would be helpful to understand the scenarios in which LOPD is likely to fail or underperform. For example, it would be helpful to understand how LOPD performs on tasks with long-range dependencies or tasks with sparse rewards.

### Suggestions

The paper would benefit from a more thorough analysis of the computational overhead introduced by the learnable latent context. While the authors mention that the composer is lightweight, a detailed breakdown of the computational cost, including FLOPs or training time per iteration, for each component (composer, student policy, and privileged-margin constraint) would be valuable. This analysis should also consider the impact of the number of latent tokens on the computational cost. Furthermore, it would be beneficial to compare the computational cost of LOPD with existing methods more explicitly, perhaps by providing a table that shows the training time and memory usage for each method on the same hardware. This would allow readers to better understand the trade-offs between performance and computational cost. The authors should also discuss the potential for optimizing the implementation of LOPD to reduce its computational footprint, such as using more efficient data structures or parallelization techniques.

To address the lack of hyperparameter sensitivity analysis, the authors should conduct a more systematic study of how different hyperparameters affect the performance of LOPD. This study should include a range of values for key hyperparameters such as the learning rate, batch size, and the number of latent tokens. The authors should also explore the impact of different optimization algorithms and learning rate schedules. The results of this analysis should be presented in a clear and concise manner, perhaps using tables or plots that show the performance of LOPD as a function of each hyperparameter. This would help readers to understand the robustness of LOPD and to choose appropriate hyperparameter values for their own applications. It would also be helpful to provide some guidelines for selecting hyperparameters based on the characteristics of the task. For example, the authors could discuss how the optimal learning rate might vary depending on the complexity of the task or the size of the dataset.

Finally, the paper should include a more detailed discussion of the limitations of LOPD. The authors should explore the performance of LOPD on tasks with long-range dependencies and sparse rewards. For example, it would be interesting to see how LOPD performs on tasks that require the student policy to remember information from several steps in the past, or on tasks where the reward signal is sparse and delayed. The authors should also discuss the potential failure modes of LOPD and suggest possible solutions to address these limitations. This discussion should be supported by experimental results, perhaps by including experiments on more challenging tasks or by providing a theoretical analysis of the limitations of LOPD. This would help readers to understand the scope of applicability of LOPD and to identify areas for future research.

### Questions

- How does the computational cost of LOPD compare to that of existing methods?
- How sensitive is LOPD to the choice of hyperparameters?
- What are the limitations of LOPD?

### Rating

8

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers for the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

Plan:
1. Read each reviewer's weakness.
2. Search the paper for evidence related to the weakness.
3. Categorize the evidence and link it to the specific weakness.
4. Formulate a conclusion about the validity of the weakness based on the evidence.
**Review 1**

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost of LOPD. The paper mentions that LOPD requires more computational resources than existing methods, but it does not provide a detailed breakdown of the computational cost of each component of LOPD. It would be helpful to understand the computational cost of the learnable composer, the student policy, and the privileged-margin constraint."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions the computational cost in the "Main Idea" section: "LOPD is designed to be scalable and efficient, making it suitable for large-scale applications."
   - In the "Method" -> "workflow" section, it states: "The method is designed to be scalable and efficient, making it suitable for large-scale applications."
   - In the "Experiments" -> "Implementation" section, it mentions: "The experiments were conducted on a single GPU with 16GB of memory."
b) Experiment-related Evidence:
   - The "Experiments" -> "Results" -> "analysis" section mentions: "LOPD achieves a significant performance improvement with minimal additional computational overhead, requiring less than 30% of the rollout budget compared to other methods." This is a qualitative statement without quantitative backing.
   - There is no table or detailed breakdown of computational costs (FLOPs, training time, memory usage) for LOPD or the baselines.

3. Literature Gap Analysis:
   - The paper does not cite specific works on computational cost analysis for self-distillation methods.

4. Validation Analysis:
   - The paper claims LOPD is efficient and requires less than 30% of the rollout budget, which implicitly suggests lower computational cost. However, this is not substantiated with concrete metrics like FLOPs, training time per iteration, or memory usage. The reviewer correctly points out the lack of a detailed breakdown of the computational cost for individual components of LOPD.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of quantitative computational cost analysis in the method and experimental sections.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the sensitivity of LOPD to the choice of hyperparameters. It would be helpful to understand how the performance of LOPD is affected by different choices of hyperparameters, such as the learning rate, the batch size, and the number of latent tokens."

2. Evidence Collection:
a) Method-related Evidence:
   - The "Method" -> "Learnable Latent Privileged Context" section mentions the number of latent tokens (K) as a hyperparameter.
   - The "Method" -> "Latent On-Policy Self-Distillation" section mentions the use of reverse KL divergence and the temperature parameter 'm' in the privileged-margin constraint.
b) Experiment-related Evidence:
   - The "Experiments" -> "Implementation" section mentions the learning rate and batch size for the student policy but does not specify them for the composer or the privileged-margin constraint.
   - The "Experiments" -> "Results" -> "analysis" section mentions: "The privileged-margin constraint is crucial for ensuring that the latent context remains informative and does not collapse during training." This hints at the importance of 'm' but doesn't explore different values.
   - There is no dedicated section or table analyzing the sensitivity of LOPD's performance to different hyperparameter values.

3. Literature Gap Analysis:
   - The paper does not cite works on hyperparameter sensitivity analysis in self-distillation or similar methods.

4. Validation Analysis:
   - The paper introduces several hyperparameters (number of latent tokens, learning rate, batch size, temperature 'm'). However, there is no systematic analysis of how the performance of LOPD changes with different values of these hyperparameters. The reviewer's point about the lack of sensitivity analysis is valid.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of a dedicated hyperparameter sensitivity analysis in the experimental section.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the limitations of LOPD. It would be helpful to understand the scenarios in which LOPD is likely to fail or underperform. For example, it would be helpful to understand how LOPD performs on tasks with long-range dependencies or tasks with sparse rewards."

2. Evidence Collection:
a) Method-related Evidence:
   - The "Method" -> "Learnable Latent Privileged Context" section mentions: "The composer is cold-started on successful trajectories with the backbone frozen, yielding ϕ0. During subsequent joint optimization, both the encoder LoRA parameters ψ and composer parameters χ remain trainable as part of ϕ, while the teacher backbone θ̄ stays fixed (details in Section A.1)."
   - The "Method" -> "Privileged-Margin Constraint" section mentions: "The privileged-margin constraint ties the teacher’s token-level advantage to the verified outcome of the complete trajectory."
b) Experiment-related Evidence:
   - The "Experiments" -> "Results" -> "analysis" section mentions: "LOPD avoids committing the teacher to a fixed answer, πT → πS, yielding uninformative latent context without improving the student." This hints at a limitation related to fixed answers.
   - The paper shows results on tool-use and code generation tasks, but there's no specific analysis of performance on tasks with long-range dependencies or sparse rewards.
   - There is no discussion of failure cases or scenarios where LOPD might underperform.

3. Literature Gap Analysis:
   - The paper does not cite works that specifically analyze the limitations of self-distillation methods in specific scenarios like long-range dependencies or sparse rewards.

4. Validation Analysis:
   - While the paper demonstrates the effectiveness of LOPD on the tested tasks, it lacks a discussion of its limitations. The reviewer correctly points out the absence of an analysis of scenarios where LOPD might struggle, such as tasks requiring long-range reasoning or dealing with sparse reward signals.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of discussion on limitations and failure cases in the paper.

**Review 2**

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational overhead introduced by the learnable latent context and the retrieval mechanism. Specifically, the paper lacks a breakdown of the time and memory costs associated with the latent vector generation, the retrieval process, and the subsequent distillation. This makes it difficult to assess the practical scalability of the method, especially when dealing with large datasets or complex tasks."

2. Evidence Collection:
a) Method-related Evidence:
   - The "Method" -> "Learnable Latent Privileged Context" section describes the retrieval process and the composer.
   - The "Method" -> "Latent On-Policy Self-Distillation" section describes the distillation objective.
b) Experiment-related Evidence:
   - The "Experiments" -> "Implementation" section mentions the hardware used (single GPU with 16GB memory).
   - There is no explicit breakdown of the time and memory costs for each component (retrieval, composer, distillation).
   - The paper mentions "minimal additional computational overhead" qualitatively but lacks quantitative details.

3. Literature Gap Analysis:
   - The paper does not cite works that provide detailed computational cost analyses for retrieval and distillation mechanisms in similar contexts.

4. Validation Analysis:
   - This weakness overlaps with the first weakness identified by Reviewer 1. The paper describes the components but doesn't provide a detailed quantitative analysis of their computational costs. The reviewer correctly identifies the lack of a breakdown for retrieval, composer, and distillation.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of quantitative computational cost breakdown for individual components in the method and experimental sections.

1. Weakness Statement:
"The paper could benefit from a more thorough comparison with other self-distillation methods that use different forms of privileged information, such as those based on hand-crafted features or external knowledge sources. The current comparison is limited to methods that also use privileged context, but a broader comparison would help to better position the contribution of this work within the broader landscape of self-distillation. For example, it would be useful to see how LOPD compares to methods that use symbolic representations or external knowledge bases as privileged signals."

2. Evidence Collection:
a) Experiment-related Evidence:
   - The "Experiments" -> "Baselines" section lists OPSD, SDPO, and Skill-SD as baselines, all of which operate on privileged contexts.
   - There is no comparison with self-distillation methods that use hand-crafted features or external knowledge sources as privileged information.

3. Literature Gap Analysis:
   - The "Related Work" section mentions methods that use external models or reward functions as privileged information, but these are not included as experimental baselines.

4. Validation Analysis:
   - The reviewer correctly points out that the experimental comparison is limited to methods that also utilize privileged context. A broader comparison with methods using different forms of privileged information would provide a more comprehensive understanding of LOPD's strengths and weaknesses.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "Experiments" section only compares against other privileged-context based self-distillation methods.

1. Weakness Statement:
"The paper does not explore the sensitivity of the method to the number of retrieved trajectories or the choice of the retrieval mechanism. It is unclear how the performance of LOPD is affected by the size of the context library and the similarity metric used for retrieval. A more detailed analysis of these factors would provide valuable insights into the robustness and generalizability of the method."

2. Evidence Collection:
a) Method-related Evidence:
   - The "Method" -> "Learnable Latent Privileged Context" section mentions retrieving "top- J" trajectories.
b) Experiment-related Evidence:
   - The "Experiments" -> "Implementation" section mentions retrieving "top- 32" trajectories.
   - There is no ablation study or analysis on the impact of varying the number of retrieved trajectories (J) or different retrieval mechanisms.

3. Literature Gap Analysis:
   - The paper does not cite works that specifically analyze the sensitivity of retrieval mechanisms in self-distillation or similar contexts.

4. Validation Analysis:
   - The reviewer correctly identifies the lack of an analysis on the sensitivity of LOPD to the number of retrieved trajectories and the choice of retrieval mechanism. This is a valid weakness as these are important factors influencing the performance and robustness of the method.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of ablation studies on the number of retrieved trajectories and retrieval mechanism in the experimental section.

**Review 3**

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost of LOPD. The paper mentions that LOPD requires more computational resources than existing methods, but it does not provide a detailed breakdown of the computational cost of each component of LOPD. This makes it difficult to assess the practical scalability of the method, especially when dealing with large datasets or complex tasks."

2. Evidence Collection:
    - This is the same weakness identified by Reviewer 1 and Reviewer 2. Please see the validation for that weakness.

3. Literature Gap Analysis:
    - Same as above.

4. Validation Analysis:
    - Same as above.

5. Conclusion:
    - Validity status: Valid
    - Confidence level: High
    - Key supporting evidence: Same as above.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the sensitivity of LOPD to the choice of hyperparameters. It would be helpful to understand how the performance of LOPD is affected by different choices of hyperparameters, such as the learning rate, the batch size, and the number of latent tokens."

2. Evidence Collection:
    - This is the same weakness identified by Reviewer 1. Please see the validation for that weakness.

3. Literature Gap Analysis:
    - Same as above.

4. Validation Analysis:
    - Same as above.

5. Conclusion:
    - Validity status: Valid
    - Confidence level: High
    - Key supporting evidence: Same as above.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the limitations of LOPD. It would be helpful to understand the scenarios in which LOPD is likely to fail or underperform. For example, it would be helpful to understand how LOPD performs on tasks with long-range dependencies or tasks with sparse rewards."

2. Evidence Collection:
    - This is the same weakness identified by Reviewer 1. Please see the validation for that weakness.

3. Literature Gap Analysis:
    - Same as above.

4. Validation Analysis:
    - Same as above.

5. Conclusion:
    - Validity status: Valid
    - Confidence level: High
    - Key supporting evidence: Same as above.

**Review 4**

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost of LOPD. The paper mentions that LOPD requires more computational resources than existing methods, but it does not provide a detailed breakdown of the computational cost of each component of LOPD. This makes it difficult to assess the practical scalability of the method, especially when dealing with large datasets or complex tasks."

2. Evidence Collection:
    - This is the same weakness identified by previous reviewers. Please see the validation for that weakness.

3. Literature Gap Analysis:
    - Same as above.

4. Validation Analysis:
    - Same as above.

5. Conclusion:
    - Validity status: Valid
    - Confidence level: High
    - Key supporting evidence: Same as above.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the sensitivity of LOPD to the choice of hyperparameters. It would be helpful to understand how the performance of LOPD is affected by different choices of hyperparameters, such as the learning rate, the batch size, and the number of latent tokens."

2. Evidence Collection:
    - This is the same weakness identified by previous reviewers. Please see the validation for that weakness.

3. Literature Gap Analysis:
    - Same as above.

4. Validation Analysis:
    - Same as above.

5. Conclusion:
    - Validity status: Valid
    - Confidence level: High
    - Key supporting evidence: Same as above.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the limitations of LOPD. It would be helpful to understand the scenarios in which LOPD is likely to fail or underperform. For example, it would be helpful to understand how LOPD performs on tasks with long-range dependencies or tasks with sparse rewards."

2. Evidence Collection:
    - This is the same weakness identified by previous reviewers. Please see the validation for that weakness.

3. Literature Gap Analysis:
    - Same as above.

4. Validation Analysis:
    - Same as above.

5. Conclusion:
    - Validity status: Valid
    - Confidence level: High
    - Key supporting evidence: Same as above.

1. Weakness Statement:
"How does the computational cost of LOPD compare to that of existing methods?"

2. Evidence Collection:
    - The paper states in the "Main Idea" and "Method" sections that LOPD is designed to be scalable and efficient.
    - The "Experiments" -> "Results" -> "analysis" section mentions: "LOPD achieves a significant performance improvement with minimal additional computational overhead, requiring less than 30% of the rollout budget compared to other methods." This is a qualitative statement without quantitative comparison.

3. Literature Gap Analysis:
    - No specific works on computational cost comparison are cited.

4. Validation Analysis:
    - The paper claims lower computational cost qualitatively but lacks a quantitative comparison with existing methods.

5. Conclusion:
    - Validity status: Valid
    - Confidence level: High
    - Key supporting evidence: Lack of quantitative computational cost comparison in the paper.

1. Weakness Statement:
"How sensitive is LOPD to the choice of hyperparameters?"

2. Evidence Collection:
    - The paper introduces hyperparameters like the number of latent tokens (K) and the privileged-margin constraint parameter 'm'.
    - There is no dedicated section or analysis exploring the sensitivity of LOPD's performance to different hyperparameter values.

3. Literature Gap Analysis:
    - No citations on hyperparameter sensitivity analysis in self-distillation.

4. Validation Analysis:
    - The paper does not provide a sensitivity analysis for its hyperparameters.

5. Conclusion:
    - Validity status: Valid
    - Confidence level: High
    - Key supporting evidence: Absence of hyperparameter sensitivity analysis.

1. Weakness Statement:
"What are the limitations of LOPD?"

2. Evidence Collection:
    - The paper demonstrates the effectiveness of LOPD on the tested tasks.
    - There is no dedicated section or discussion outlining the limitations or potential failure cases of LOPD.

3. Literature Gap Analysis:
    - No citations discussing limitations of similar methods.

4. Validation Analysis:
    - The paper does not explicitly discuss the limitations of LOPD.

5. Conclusion:
    - Validity status: Valid
    - Confidence level: High
    - Key supporting evidence: Lack of discussion on limitations in the paper.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces Latent On-Policy Self-Distillation (LOPD), a novel approach to self-distillation that learns a latent representation of privileged context from experience. Unlike previous methods that rely on pre-defined privileged signals, LOPD employs a learnable latent context generated by a composer, which transforms retrieved trajectories into a continuous, differentiable space. This latent context is then used to condition both the student and teacher policies, with the teacher policy conditioned on the latent context plus the original privileged context. The method is designed to be scalable and efficient, requiring less than 30% of the rollout budget compared to other methods. Empirical results across multiple benchmarks in both agentic tool-use and code generation tasks demonstrate that LOPD outperforms existing self-distillation methods, achieving significant performance improvements with minimal additional computational overhead. The core idea of learning a latent privileged context is a significant departure from prior approaches, allowing for a more adaptive and flexible utilization of available information. The paper presents a comprehensive evaluation of LOPD, showcasing its effectiveness in various scenarios. However, the paper also lacks a detailed analysis of the computational costs associated with the method, the sensitivity of its performance to hyperparameter choices, and a thorough discussion of its limitations. These omissions, while not invalidating the core contributions, do limit the overall impact and practical applicability of the proposed method. Despite these shortcomings, the paper presents a promising direction for self-distillation research, offering a new perspective on how to leverage privileged information in reinforcement learning.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

2.75


## Strengths:

I found several aspects of this paper to be particularly strong. The core idea of learning a latent privileged context is both novel and compelling. By moving away from pre-defined privileged signals and instead learning a representation of this context from experience, the authors have introduced a more flexible and adaptable approach to self-distillation. This is a significant departure from prior methods and represents a valuable contribution to the field. The paper is also well-written and easy to follow, with a clear and concise explanation of the proposed method. The authors have successfully presented a complex idea in an accessible manner, making it easy for readers to understand the core concepts and the overall approach. The empirical results presented in the paper are also quite strong. The authors have conducted a comprehensive evaluation of LOPD across multiple benchmarks in both agentic tool-use and code generation tasks. The results consistently demonstrate that LOPD outperforms existing self-distillation methods, with a significant performance improvement while requiring less than 30% of the rollout budget. This highlights the practical effectiveness of the proposed method and its potential for real-world applications. Furthermore, the authors have provided a thorough analysis of the results, including the impact of the privileged-margin constraint and the learnable context. This analysis provides valuable insights into the behavior of the proposed method and helps to understand why it performs so well. The paper also includes a detailed description of the experimental setup, which allows for reproducibility of the results. Overall, the paper presents a well-executed study with a novel approach, strong empirical results, and a clear and concise presentation of the method and findings. The core idea of learning a latent privileged context is a significant contribution that has the potential to advance the field of self-distillation.


## Weaknesses:

Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. First, and perhaps most significantly, the paper lacks a detailed analysis of the computational cost of LOPD. While the authors claim that LOPD is efficient and requires less than 30% of the rollout budget compared to other methods, this claim is not substantiated with concrete metrics. The paper mentions that the composer is lightweight, but a detailed breakdown of the computational cost, including FLOPs or training time per iteration, for each component of LOPD (composer, student policy, and privileged-margin constraint) is missing. This makes it difficult to assess the practical scalability of the method, especially when dealing with large datasets or complex tasks. The absence of a quantitative comparison of computational costs with existing methods is a major limitation, as it prevents a clear understanding of the trade-offs between performance and computational resources. My analysis of the paper confirms that there is no table or detailed breakdown of computational costs, which is a significant oversight. Second, the paper does not provide a detailed analysis of the sensitivity of LOPD to the choice of hyperparameters. While the authors mention the number of latent tokens (K) and the privileged-margin constraint parameter 'm', there is no systematic study of how the performance of LOPD is affected by different choices of these hyperparameters. The paper does not explore the impact of different optimization algorithms or learning rate schedules, which are crucial for understanding the robustness of the method. The absence of a sensitivity analysis makes it difficult to determine the optimal settings for different tasks and datasets. My examination of the experimental section confirms that there is no dedicated section or table analyzing the sensitivity of LOPD's performance to different hyperparameter values. Third, the paper does not include a detailed discussion of the limitations of LOPD. While the authors demonstrate the effectiveness of the method on the tested tasks, they do not explore the performance of LOPD on tasks with long-range dependencies or sparse rewards. The paper also does not discuss the potential failure modes of LOPD or suggest possible solutions to address these limitations. This lack of analysis makes it difficult to understand the scope of applicability of LOPD and to identify areas for future research. My analysis of the paper confirms that there is no dedicated section or discussion outlining the limitations or potential failure cases of LOPD. Fourth, the paper does not provide a detailed comparison with other self-distillation methods that use different forms of privileged information. The current comparison is limited to methods that also use privileged context, but a broader comparison would help to better position the contribution of this work within the broader landscape of self-distillation. For example, it would be useful to see how LOPD compares to methods that use hand-crafted features or external knowledge sources as privileged signals. The absence of this comparison limits the understanding of the relative strengths and weaknesses of LOPD compared to other approaches. My analysis of the experimental section confirms that the baselines are all methods that also use privileged context. Finally, the paper does not explore the sensitivity of the method to the number of retrieved trajectories or the choice of the retrieval mechanism. It is unclear how the performance of LOPD is affected by the size of the context library and the similarity metric used for retrieval. This lack of analysis makes it difficult to understand the robustness and generalizability of the method. My analysis of the experimental section confirms that there is no ablation study or analysis on the impact of varying the number of retrieved trajectories or different retrieval mechanisms. These weaknesses, while not invalidating the core contributions of the paper, do limit its overall impact and practical applicability. The lack of detailed analysis on computational costs, hyperparameter sensitivity, limitations, and retrieval mechanisms significantly reduces the robustness and generalizability of the findings.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the paper should include a more thorough analysis of the computational overhead introduced by the learnable latent context. While the authors mention that the composer is lightweight, a detailed breakdown of the computational cost, including FLOPs or training time per iteration, for each component (composer, student policy, and privileged-margin constraint) would be valuable. This analysis should also consider the impact of the number of latent tokens on the computational cost. Furthermore, it would be beneficial to compare the computational cost of LOPD with existing methods more explicitly, perhaps by providing a table that shows the training time and memory usage for each method on the same hardware. This would allow readers to better understand the trade-offs between performance and computational cost. The authors should also discuss the potential for optimizing the implementation of LOPD to reduce its computational footprint, such as using more efficient data structures or parallelization techniques. Second, to address the lack of hyperparameter sensitivity analysis, the authors should conduct a more systematic study of how different hyperparameters affect the performance of LOPD. This study should include a range of values for key hyperparameters such as the learning rate, batch size, and the number of latent tokens. The authors should also explore the impact of different optimization algorithms and learning rate schedules. The results of this analysis should be presented in a clear and concise manner, perhaps using tables or plots that show the performance of LOPD as a function of each hyperparameter. This would help readers to understand the robustness of LOPD and to choose appropriate hyperparameter values for their own applications. It would also be helpful to provide some guidelines for selecting hyperparameters based on the characteristics of the task. Third, the paper should include a more detailed discussion of the limitations of LOPD. The authors should explore the performance of LOPD on tasks with long-range dependencies and sparse rewards. For example, it would be interesting to see how LOPD performs on tasks that require the student policy to remember information from several steps in the past, or on tasks where the reward signal is sparse and delayed. The authors should also discuss the potential failure modes of LOPD and suggest possible solutions to address these limitations. This discussion should be supported by experimental results, perhaps by including experiments on more challenging tasks or by providing a theoretical analysis of the limitations of LOPD. This would help readers to understand the scope of applicability of LOPD and to identify areas for future research. Fourth, the paper should include a more comprehensive comparison with other self-distillation methods that use different forms of privileged information. This comparison should go beyond methods that also use privileged context and include a discussion of how LOPD compares to methods that use hand-crafted features, external knowledge bases, or symbolic representations as privileged signals. For example, the authors could compare LOPD to methods that use explicit skill embeddings or external knowledge bases as privileged signals. This comparison should not only focus on the performance of the methods but also on their computational cost, ease of implementation, and the type of privileged information they require. Such a comparison would provide a more complete picture of the strengths and weaknesses of LOPD and help to better understand its contribution to the field of self-distillation. Finally, the paper should include a more thorough sensitivity analysis of the method to the number of retrieved trajectories and the choice of the retrieval mechanism. The authors should investigate how the performance of LOPD is affected by the size of the context library and the similarity metric used for retrieval. This analysis should include a discussion of the trade-offs between the size of the context library, the computational cost, and the performance of the method. Furthermore, it would be helpful to explore different retrieval mechanisms, such as k-nearest neighbors or attention-based methods, and discuss their impact on the performance of LOPD. This sensitivity analysis would provide valuable insights into the robustness and generalizability of the method and help to identify the optimal settings for different tasks and datasets. These suggestions, if implemented, would significantly strengthen the paper and provide a more complete understanding of the proposed method.


## Questions:

I have several questions that arise from my analysis of this paper. First, how does the computational cost of LOPD compare to that of existing methods? While the paper claims that LOPD is efficient, it does not provide a detailed quantitative comparison of computational costs. I am interested in understanding the specific computational overhead introduced by the learnable latent context and the retrieval mechanism. Second, how sensitive is LOPD to the choice of hyperparameters? The paper introduces several hyperparameters, such as the number of latent tokens and the privileged-margin constraint parameter, but it does not provide a systematic analysis of how the performance of LOPD is affected by different choices of these hyperparameters. I would like to understand the robustness of LOPD and to identify the optimal settings for different tasks and datasets. Third, what are the limitations of LOPD? The paper demonstrates the effectiveness of the method on the tested tasks, but it does not explore the performance of LOPD on tasks with long-range dependencies or sparse rewards. I am interested in understanding the scenarios in which LOPD is likely to fail or underperform and to identify areas for future research. Fourth, how does LOPD compare to other self-distillation methods that use different forms of privileged information? The current comparison is limited to methods that also use privileged context, but a broader comparison would help to better position the contribution of this work within the broader landscape of self-distillation. I am interested in understanding how LOPD compares to methods that use hand-crafted features or external knowledge sources as privileged signals. Finally, how sensitive is LOPD to the number of retrieved trajectories and the choice of the retrieval mechanism? The paper does not explore the impact of different retrieval mechanisms on the performance of LOPD. I am interested in understanding the robustness and generalizability of the method and to identify the optimal settings for different tasks and datasets. These questions target key uncertainties in the paper and seek clarification on critical assumptions and methodological choices.


## Rating:

6.5


## Confidence:

3.0


## Decision:

Accept
}