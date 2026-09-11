I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper proposes a new method called Sample-Routed Policy Optimization (SRPO) for post-training large language models (LLMs) using verifiable rewards. SRPO combines the advantages of two existing methods: Group Relative Policy Optimization (GRPO) and Self-Distillation Policy Optimization (SDPO). GRPO provides reward-aligned reinforcement by normalizing outcomes across a group of rollouts, while SDPO uses self-distillation to provide dense, logit-level guidance for corrections. SRPO routes correct samples to GRPO for reward alignment and failed samples to SDPO for logit-level correction, incorporating an entropy-aware dynamic weighting mechanism to suppress unreliable corrections. The authors demonstrate that SRPO achieves better early training efficiency and long-horizon stability compared to GRPO and SDPO, with improvements in peak performance and reduced per-step compute costs. The method is evaluated across five benchmarks and two model scales, showing consistent outperformance and moderate response lengths.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper is well-organized and clearly written, making it easy to follow and understand. The authors provide a detailed explanation of the proposed method, including the motivation, methodology, and experimental setup.
2. The authors conduct extensive experiments across five benchmarks and two model scales, demonstrating the effectiveness of SRPO. The results show that SRPO consistently outperforms GRPO and SDPO, achieving higher peak performance and reduced per-step compute costs.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational overhead of SRPO compared to GRPO and SDPO. While the authors mention lower per-step compute costs, they do not provide a breakdown of the computational resources required for each component of SRPO, such as the self-teacher computation and entropy-aware dynamic weighting. This makes it difficult to assess the practical efficiency of the method.
2. The paper does not explore the sensitivity of SRPO to different hyperparameters, such as the routing threshold and the weighting parameters. A thorough analysis of the hyperparameter space is crucial for understanding the robustness and generalizability of the method.
3. The paper does not provide a detailed comparison of SRPO with other state-of-the-art methods for post-training LLMs. While the authors compare SRPO with GRPO and SDPO, they do not discuss its performance relative to other relevant methods, such as reinforcement learning from human feedback (RLHF) or other self-improvement techniques. This limits the understanding of SRPO's relative advantages and disadvantages.
4. The paper does not provide a detailed analysis of the failure cases of SRPO. It would be beneficial to understand the types of errors that SRPO makes and how these errors compare to those made by GRPO and SDPO. This would provide insights into the strengths and weaknesses of the method.
5. The paper does not discuss the limitations of SRPO and potential directions for future research. For example, the authors could discuss the potential challenges of applying SRPO to more complex tasks or environments, or the limitations of the entropy-aware dynamic weighting mechanism.

### Suggestions

The paper would benefit from a more detailed analysis of the computational overhead of SRPO. Specifically, the authors should provide a breakdown of the computational costs associated with each component of the method, including the self-teacher computation and the entropy-aware dynamic weighting. This analysis should include a comparison of the computational costs of SRPO with those of GRPO and SDPO, and should consider the impact of different batch sizes and model sizes on the overall computational cost. Furthermore, the authors should provide a more detailed analysis of the memory requirements of SRPO, as this is an important factor in the practical application of the method. A clear understanding of the computational overhead is crucial for assessing the practical efficiency of SRPO and for comparing it with other post-training methods.

To improve the robustness and generalizability of the method, the authors should conduct a thorough sensitivity analysis of SRPO to different hyperparameters. This analysis should include a systematic exploration of the impact of the routing threshold, the weighting parameters, and other relevant hyperparameters on the performance of SRPO. The authors should also provide a detailed explanation of how these hyperparameters were selected and what impact they have on the overall performance of the method. This analysis should include a discussion of the trade-offs between different hyperparameter settings and should provide guidance on how to choose the optimal hyperparameter values for different tasks and environments. A more detailed sensitivity analysis would help to ensure that SRPO is robust and generalizable across a range of different settings.

Finally, the paper should include a more detailed comparison of SRPO with other state-of-the-art methods for post-training LLMs. This comparison should include a discussion of the strengths and weaknesses of SRPO relative to other methods, such as RLHF and other self-improvement techniques. The authors should also discuss the potential limitations of SRPO and should identify areas for future research. For example, the authors could discuss the potential challenges of applying SRPO to more complex tasks or environments, or the limitations of the entropy-aware dynamic weighting mechanism. A more comprehensive comparison with other methods would help to contextualize the contribution of SRPO and to identify potential areas for future research.

### Questions

1. How does the entropy-aware dynamic weighting mechanism in SRPO affect the stability and convergence of the training process? Are there any specific conditions under which this mechanism might fail or perform suboptimally?
2. How does SRPO perform on tasks that require more complex reasoning or planning? Are there any limitations or challenges in applying SRPO to such tasks?
3. How does the performance of SRPO scale with the size of the LLM and the number of samples? Are there any practical limitations or trade-offs in scaling SRPO to larger models or datasets?

### Rating

5

### Confidence

4

**********

## Reviewer 2

### Summary

This paper proposes a new method called Sample-Routed Policy Optimization (SRPO) for post-training large language models (LLMs). SRPO combines the advantages of two existing methods: Group Relative Policy Optimization (GRPO) and Self-Distillation Policy Optimization (SDPO). GRPO provides reward-aligned reinforcement by normalizing outcomes across a group of rollouts, while SDPO uses self-distillation to provide dense, logit-level guidance for corrections. SRPO routes correct samples to GRPO for reward alignment and failed samples with teacher information to SDPO for logit-level correction, incorporating an entropy-aware dynamic weighting mechanism to suppress unreliable corrections. The authors demonstrate that SRPO achieves better early training efficiency and long-horizon stability compared to GRPO and SDPO, with improvements in peak performance and reduced per-step compute costs. The method is evaluated across five benchmarks and two model scales, showing consistent outperformance and moderate response lengths.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow. The authors clearly explain the motivation behind SRPO and the details of the method. The figures and tables are well-designed and effectively illustrate the key concepts and results.
2. The proposed method, SRPO, is novel and addresses a critical issue in RL from verifiable rewards. The combination of GRPO and SDPO, along with the entropy-aware dynamic weighting mechanism, is a creative and effective approach to improving the stability and efficiency of post-training.
3. The experimental results are comprehensive and convincing. The authors evaluate SRPO across five benchmarks and two model scales, demonstrating its effectiveness and robustness. The results show that SRPO consistently outperforms GRPO and SDPO, achieving higher peak performance and reduced per-step compute costs. The ablation study further validates the importance of the different components of SRPO.

### Weaknesses

#### Some Related Works


#### comment

1. While the paper provides a good overview of the related work, it could benefit from a more detailed comparison of SRPO with other state-of-the-art methods for post-training LLMs. Specifically, the paper should discuss how SRPO compares to other methods that also aim to improve the stability and efficiency of post-training, such as those based on reinforcement learning from human feedback (RLHF) or other self-improvement techniques. A more thorough comparison would help to contextualize the contribution of SRPO and highlight its unique advantages and limitations.
2. The paper could provide more insights into the practical implications of SRPO. For example, it would be helpful to discuss how SRPO can be applied to different types of LLMs and tasks, and what are the potential challenges and limitations in real-world applications. The authors should also discuss the computational resources required to train and deploy SRPO, and how these resources compare to those required by other methods. A more detailed discussion of the practical implications of SRPO would help to increase its impact and relevance.
3. The paper could benefit from a more detailed analysis of the performance of SRPO on different types of tasks and benchmarks. While the results show that SRPO consistently outperforms GRPO and SDPO, it would be helpful to understand why this is the case and what are the specific characteristics of the tasks and benchmarks that make SRPO more effective. For example, the authors could analyze the performance of SRPO on tasks that require different types of reasoning or planning, and discuss how the combination of GRPO and SDPO contributes to its success. A more detailed analysis of the performance of SRPO on different tasks would help to provide a more comprehensive understanding of its strengths and weaknesses.

### Suggestions

To strengthen the paper, the authors should include a more comprehensive comparison with existing methods for post-training LLMs, particularly those that address similar challenges in stability and efficiency. This comparison should not only focus on performance metrics but also delve into the underlying mechanisms and assumptions of each method. For instance, a detailed analysis of how SRPO's sample routing and entropy-aware weighting compare to the exploration-exploitation trade-offs in RLHF or the curriculum learning strategies in other self-improvement techniques would be beneficial. This would help to clarify the unique contributions of SRPO and its potential advantages over existing approaches. Furthermore, the authors should discuss the computational overhead of SRPO compared to other methods, including the cost of calculating the self-teacher distribution and the dynamic weighting mechanism. This analysis should consider both training and inference costs, providing a more complete picture of the practical implications of using SRPO.

In addition to the performance comparisons, the authors should provide a more in-depth discussion of the practical implications of SRPO. This should include a detailed analysis of how SRPO can be applied to different types of LLMs and tasks, as well as the potential challenges and limitations that may arise in real-world applications. For example, the authors could discuss how SRPO performs on tasks that require different types of reasoning or planning, and how the combination of GRPO and SDPO contributes to its success in these different contexts. They should also discuss the sensitivity of SRPO to different hyperparameters and provide guidelines for selecting appropriate values. Furthermore, the authors should discuss the computational resources required to train and deploy SRPO, including the memory and processing power needed for both training and inference. This analysis should also consider the scalability of SRPO to larger models and datasets, providing a more complete picture of its practical feasibility.

Finally, the authors should provide a more detailed analysis of the performance of SRPO on different types of tasks and benchmarks. This analysis should go beyond simply reporting overall performance metrics and delve into the specific characteristics of the tasks and benchmarks that make SRPO more effective. For example, the authors could analyze the performance of SRPO on tasks that require different types of reasoning or planning, and discuss how the combination of GRPO and SDPO contributes to its success in these different contexts. They should also analyze the performance of SRPO on tasks with varying levels of complexity and difficulty, and discuss how the method adapts to these different challenges. This analysis should also include a discussion of the failure cases of SRPO and the potential reasons for these failures. By providing a more detailed analysis of the performance of SRPO on different tasks, the authors can provide a more comprehensive understanding of its strengths and weaknesses and help to guide future research in this area.

### Questions

1. How does SRPO handle the exploration-exploitation trade-off in post-training? Does the combination of GRPO and SDPO encourage sufficient exploration of the policy space, or does it primarily rely on exploitation of the current policy?
2. How sensitive is SRPO to the choice of hyperparameters, such as the weighting parameters and the entropy threshold? Are there any guidelines for selecting appropriate values for these hyperparameters in different settings?
3. How does SRPO perform on tasks that require more complex reasoning or planning? Are there any limitations or challenges in applying SRPO to such tasks?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper proposes a new method called Sample-Routed Policy Optimization (SRPO) for post-training large language models (LLMs). SRPO combines the advantages of two existing methods: Group Relative Policy Optimization (GRPO) and Self-Distillation Policy Optimization (SDPO). GRPO provides reward-aligned reinforcement by normalizing outcomes across a group of rollouts, while SDPO uses self-distillation to provide dense logit-level guidance for corrections. SRPO routes correct samples to GRPO's reward-aligned reinforcement and failed samples to SDPO's targeted logit-level correction. SRPO further incorporates an entropy-aware dynamic weighting mechanism to suppress high-entropy, unreliable distillation targets while emphasizing confident ones. The authors demonstrate that SRPO achieves both the rapid early improvement of SDPO and the long-horizon stability of GRPO. It consistently surpasses the peak performance of both baselines, raising the five-benchmark average on Qwen3-8B by 3.4% over GRPO and 6.3% over SDPO, while simultaneously yielding moderate response lengths and lowering per-step compute cost by up to 17.2%.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow. The authors clearly explain the motivation behind SRPO and the details of the method. The figures and tables are well-designed and effectively illustrate the key concepts and results.
2. The proposed method, SRPO, is novel and addresses a critical issue in RL from verifiable rewards. The combination of GRPO and SDPO, along with the entropy-aware dynamic weighting mechanism, is a creative and effective approach to improving the stability and efficiency of post-training.
3. The experimental results are comprehensive and convincing. The authors evaluate SRPO across five benchmarks and two model scales, demonstrating its effectiveness and robustness. The results show that SRPO consistently outperforms GRPO and SDPO, achieving higher peak performance and reduced per-step compute costs. The ablation study further validates the importance of the different components of SRPO.

### Weaknesses

#### Some Related Works


#### comment

1. While the paper provides a good overview of the related work, it could benefit from a more detailed comparison of SRPO with other state-of-the-art methods for post-training LLMs. Specifically, the paper should discuss how SRPO compares to other methods that also aim to improve the stability and efficiency of post-training, such as those based on reinforcement learning from human feedback (RLHF) or other self-improvement techniques. A more thorough comparison would help to contextualize the contribution of SRPO and highlight its unique advantages and limitations.
2. The paper could provide more insights into the practical implications of SRPO. For example, it would be helpful to discuss how SRPO can be applied to different types of LLMs and tasks, and what are the potential challenges and limitations in real-world applications. The authors should also discuss the computational resources required to train and deploy SRPO, and how these resources compare to those required by other methods. A more detailed discussion of the practical implications of SRPO would help to increase its impact and relevance.
3. The paper could benefit from a more detailed analysis of the performance of SRPO on different types of tasks and benchmarks. While the results show that SRPO consistently outperforms GRPO and SDPO, it would be helpful to understand why this is the case and what are the specific characteristics of the tasks and benchmarks that make SRPO more effective. For example, the authors could analyze the performance of SRPO on tasks that require different types of reasoning or planning, and discuss how the combination of GRPO and SDPO contributes to its success in these different contexts. A more detailed analysis of the performance of SRPO on different tasks would help to provide a more comprehensive understanding of its strengths and weaknesses.

### Suggestions

The paper would be significantly strengthened by a more thorough comparison with existing methods in the field of post-training for large language models. Specifically, the authors should discuss how SRPO relates to and differs from techniques that employ reinforcement learning from human feedback (RLHF), which is a dominant approach in this area. A detailed comparison should not only focus on performance metrics but also on the underlying mechanisms and assumptions of each method. For instance, how does SRPO's sample-based approach compare to the more common policy gradient methods used in RLHF? Furthermore, the authors should explore how SRPO's self-distillation mechanism compares to other self-improvement techniques, such as those based on adversarial training or iterative refinement. This would help to contextualize the novelty and contribution of SRPO within the broader landscape of post-training methods. A more comprehensive comparison would also help to identify potential areas for future research and development.

In addition to the theoretical comparison, the paper should provide a more detailed analysis of the practical implications of SRPO. The authors should discuss how the method can be applied to different types of LLMs, including both open-source and proprietary models, and what challenges might arise in real-world applications. For example, how does the performance of SRPO vary across different model sizes and architectures? What are the computational costs associated with training and deploying SRPO, and how do these costs compare to other post-training methods? Furthermore, the authors should discuss the sensitivity of SRPO to hyperparameter settings and provide guidelines for selecting appropriate values. A more detailed analysis of the practical implications of SRPO would help to increase its impact and relevance to the broader research community. This would also help practitioners understand the trade-offs involved in using SRPO and how to optimize its performance for their specific use cases.

Finally, the paper would benefit from a more in-depth analysis of the performance of SRPO across different types of tasks and benchmarks. While the results show that SRPO consistently outperforms GRPO and SDPO, it would be valuable to understand why this is the case and what specific characteristics of the tasks and benchmarks make SRPO more effective. For example, the authors could analyze the performance of SRPO on tasks that require different types of reasoning, such as logical inference, common-sense reasoning, or creative writing. How does SRPO perform on tasks that require planning or problem-solving? A more detailed analysis of the performance of SRPO on different tasks would provide a more comprehensive understanding of its strengths and weaknesses and help to identify areas where further improvement is needed. This would also help to guide future research efforts in this area and contribute to the development of more robust and versatile post-training methods.

### Questions

1. How does SRPO handle the exploration-exploitation trade-off in post-training? Does the combination of GRPO and SDPO encourage sufficient exploration of the policy space, or does it primarily rely on exploitation of the current policy?
2. How sensitive is SRPO to the choice of hyperparameters, such as the weighting parameters and the entropy threshold? Are there any guidelines for selecting appropriate values for these hyperparameters in different settings?
3. How does SRPO perform on tasks that require more complex reasoning or planning? Are there any limitations or challenges in applying SRPO to such tasks?

### Rating

6

### Confidence

4

**********

## Reviewer 4

### Summary

This paper introduces Sample-Routed Policy Optimization (SRPO), a method that combines Group Relative Policy Optimization (GRPO) and Self-Distillation Policy Optimization (SDPO) to improve the efficiency and stability of post-training large language models (LLMs) using verifiable rewards. SRPO routes correct samples to GRPO for reward-aligned reinforcement and failed samples to SDPO for logit-level correction, incorporating an entropy-aware dynamic weighting mechanism to enhance stability and performance. The method is evaluated across five benchmarks and two model scales, demonstrating consistent outperformance over baselines with improved peak performance and reduced per-step compute costs.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and addresses a critical issue in RL from verifiable rewards.
3. The experimental results are comprehensive and convincing, demonstrating the effectiveness of SRPO.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational overhead of SRPO compared to GRPO and SDPO. While the authors mention lower per-step compute costs, they do not provide a breakdown of the computational resources required for each component of SRPO, such as the self-teacher computation and entropy-aware dynamic weighting. This makes it difficult to assess the practical efficiency of the method.
2. The paper does not explore the sensitivity of SRPO to different hyperparameters, such as the weighting parameters and the entropy threshold. A thorough analysis of how these hyperparameters affect the performance of SRPO is missing, which could limit the understanding of the method's robustness and generalizability.

### Suggestions

To address the lack of detailed computational analysis, the authors should provide a more granular breakdown of the computational costs associated with each component of SRPO. This should include the time and memory requirements for calculating the self-teacher distribution, performing entropy-aware dynamic weighting, and updating the policy parameters. A comparison of these costs with those of GRPO and SDPO would be beneficial. Furthermore, the authors should investigate the scaling behavior of SRPO with respect to model size and dataset size. This would help to understand the practical applicability of the method in different scenarios. For example, how does the computational cost of SRPO compare to GRPO and SDPO when applied to larger models or datasets? This analysis should include both training and inference costs.

To improve the understanding of SRPO's sensitivity to hyperparameters, the authors should conduct a thorough ablation study. This study should systematically vary the weighting parameters and the entropy threshold and evaluate their impact on the performance of SRPO. The authors should also investigate the interaction between these hyperparameters and provide guidelines for selecting appropriate values for different tasks and datasets. For example, how does the optimal weighting parameter vary across different benchmarks? What is the effect of the entropy threshold on the stability and convergence of the training process? This analysis should include a discussion of the trade-offs between different hyperparameter settings and provide insights into the robustness of the method.

Finally, the authors should provide a more detailed analysis of the failure cases of SRPO. This analysis should include examples of scenarios where SRPO does not perform well and discuss the reasons for these failures. This would help to identify the limitations of the method and guide future research. For example, are there specific types of tasks or datasets where SRPO struggles? What are the potential causes of these failures? A more detailed analysis of the failure cases would provide a more complete understanding of the method's strengths and weaknesses.

### Questions

1. How does SRPO handle the exploration-exploitation trade-off in post-training? Does the combination of GRPO and SDPO encourage sufficient exploration of the policy space, or does it primarily rely on exploitation of the current policy?
2. How sensitive is SRPO to the choice of hyperparameters, such as the weighting parameters and the entropy threshold? Are there any guidelines for selecting appropriate values for these hyperparameters in different settings?
3. How does SRPO perform on tasks that require more complex reasoning or planning? Are there any limitations or challenges in applying SRPO to such tasks?

### Rating

6

### Confidence

2

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in a given paper. I need to go through each reviewer's comments and check if the criticism is valid based on the content of the paper.

For each weakness, I will:
1. **State the weakness** as quoted from the reviewer.
2. **Collect evidence** from the paper to support or refute the weakness. This will involve looking at the method description, experimental setup, results, and related work.
3. **Analyze literature gaps** by checking if the paper misses relevant citations or comparisons.
4. **Provide a validation analysis** summarizing the evidence and its impact.
5. **Conclude** whether the weakness is valid, partially valid, or invalid, and provide a confidence level and key supporting evidence.
**Review 1 Weaknesses:**

1. Weakness Statement:
[The paper lacks a detailed analysis of the computational overhead of SRPO compared to GRPO and SDPO. While the authors mention lower per-step compute costs, they do not provide a breakdown of the computational resources required for each component of SRPO, such as the self-teacher computation and entropy-aware dynamic weighting. This makes it difficult to assess the practical efficiency of the method.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions "lower per-step compute cost" in the abstract and introduction.
   - In the "Training Objective" section, the paper states: "The combined objective is given by:  `L_final = ∑_{i,t} z_{i,gt}^GRPO + ∑_{i,t} z_{i,dt}^DW`" where `z_{i,dt}^DW` involves the entropy-aware dynamic weighting.
   - The "Entropy-Aware Dynamic Weighting" component description details the calculation of `w_i,t`.
   - The paper does not provide a detailed breakdown of the computational cost for each component (GRPO, SDPO, dynamic weighting).

b) Experiment-related Evidence:
   - The "Training Objective" section mentions "average seconds per training step of Qwen3-8B, averaged over the five benchmarks."
   - Table 1 shows the "Per-Step Compute Cost" for GRPO, SDPO, and SRPO.

3. Literature Gap Analysis:
   - The paper cites relevant works on GRPO and SDPO but doesn't explicitly compare the computational complexity of SRPO with these baselines in detail.

4. Validation Analysis:
   - Primary evidence suggests the authors acknowledge lower per-step compute costs but don't provide a granular breakdown of the computational overhead of SRPO's components.
   - The paper does provide the overall per-step compute cost in Table 1, which partially addresses the concern.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper mentions lower per-step compute costs but lacks a detailed breakdown of SRPO's component costs. Table 1 provides the overall cost but not the individual contributions.

1. Weakness Statement:
[The paper does not explore the sensitivity of SRPO to different hyperparameters, such as the weighting parameters and the entropy threshold. A thorough analysis of how these hyperparameters affect the performance of SRPO is missing, which could limit the understanding of the method's robustness and generalizability.]

2. Evidence Collection:
a) Method-related Evidence:
   - The "Dynamic-Weighting Temperature β" is mentioned as a hyperparameter in the "Entropy-Aware Dynamic Weighting" component description.
   - The "Training Objective" section describes the weighting mechanism `w_i,t` which depends on `β`.
   - The "Ablation Study" section includes experiments on "Advantage-Mixed Policy" and "Dynamic Weighting," but these do not directly address the sensitivity to the specific hyperparameter `β`.

b) Experiment-related Evidence:
   - The "Ablation Study" section provides results for "Ablation Study on Advantage-Mixed Policy" and "Ablation Study on Dynamic Weighting."
   - The paper does not explicitly present an ablation study on the "Dynamic-Weighting Temperature β."

3. Literature Gap Analysis:
   - The paper doesn't cite specific literature on hyperparameter sensitivity analysis for similar methods.

4. Validation Analysis:
   - The paper mentions a hyperparameter `β` but doesn't provide a systematic analysis of its impact on performance.
   - The ablation study touches upon related concepts but doesn't isolate the effect of `β`.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper mentions the hyperparameter `β` but lacks a dedicated ablation study on its sensitivity.

**Review 2 Weaknesses:**

1. Weakness Statement:
[While the paper provides a good overview of the related work, it could benefit from a more detailed comparison of SRPO with other state-of-the-art methods for post-training LLMs. Specifically, the paper should discuss how SRPO compares to other methods that also aim to improve the stability and efficiency of post-training, such as those based on reinforcement learning from human feedback (RLHF) or other self-improvement techniques. A more thorough comparison would help to contextualize the contribution of SRPO and highlight its unique advantages and limitations.]

2. Evidence Collection:
a) Method-related Evidence:
   - The "Related Work" section discusses RLVR and SDPO.
   - The introduction mentions RLHF as a standard paradigm for post-training.

b) Experiment-related Evidence:
   - The baselines used are GRPO and SDPO.

3. Literature Gap Analysis:
   - The paper does not include a detailed comparison with RLHF or other self-improvement techniques.

4. Validation Analysis:
   - The paper focuses on comparing SRPO with GRPO and SDPO, which are relevant baselines for the specific problem of RL from verifiable rewards.
   - It acknowledges RLHF as a broader paradigm but doesn't delve into a detailed comparison with SRPO.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks a detailed comparison with RLHF and other self-improvement techniques.

1. Weakness Statement:
[The paper could provide more insights into the practical implications of SRPO. For example, it would be helpful to discuss how SRPO can be applied to different types of LLMs and tasks, and what are the potential challenges and limitations in real-world applications. The authors should also discuss the computational resources required to train and deploy SRPO, and how these resources compare to those required by other methods. A more detailed discussion of the practical implications of SRPO would help to increase its impact and relevance.]

2. Evidence Collection:
a) Method-related Evidence:
   - The method is described generally and should be applicable to various LLMs.

b) Experiment-related Evidence:
   - Experiments are conducted on Qwen3-4 models.
   - The paper mentions the computational cost in Table 1.

3. Literature Gap Analysis:
   - The paper doesn't discuss specific challenges in real-world applications beyond the benchmark settings.

4. Validation Analysis:
   - While the paper shows results on specific models, it lacks a broader discussion of applicability to different LLMs and tasks.
   - The computational cost is mentioned but not extensively discussed in terms of practical implications for training and deployment.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper lacks a detailed discussion on the practical implications of SRPO for various LLMs and tasks, beyond the specific models and benchmarks used.

1. Weakness Statement:
[The paper could benefit from a more detailed analysis of the performance of SRPO on different types of tasks and benchmarks. While the results show that SRPO consistently outperforms GRPO and SDPO, it would be helpful to understand why this is the case and what are the specific characteristics of the tasks and benchmarks that make SRPO more effective. For example, the authors could analyze the performance of SRPO on tasks that require different types of reasoning or planning, and discuss how the combination of GRPO and SDPO contributes to its success in these different contexts. A more detailed analysis of the performance of SRPO on different tasks would help to provide a more comprehensive understanding of its strengths and weaknesses.]

2. Evidence Collection:
a) Experiment-related Evidence:
   - The paper evaluates SRPO on five benchmarks: Chemistry, Physics, Biology, Materials, and Tool Use.
   - The "Main Results" section provides aggregate performance metrics.
   - Figure 3 shows learning curves on Qwen3-8B, which implicitly shows performance across different tasks.

3. Literature Gap Analysis:
   - The paper doesn't include a detailed analysis of performance on individual tasks within the benchmarks.

4. Validation Analysis:
   - The paper presents overall performance but lacks a granular analysis of SRPO's effectiveness on individual tasks within the benchmarks.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks a detailed analysis of SRPO's performance on individual tasks within the five benchmarks.

**Review 3 Weaknesses:**

1. Weakness Statement:
[The paper lacks a detailed analysis of the computational overhead of SRPO compared to GRPO and SDPO. While the authors mention lower per-step compute costs, they do not provide a breakdown of the computational resources required for each component of SRPO, such as the self-teacher computation and entropy-aware dynamic weighting. This makes it difficult to assess the practical efficiency of the method.]

2. Evidence Collection:
   - This is the same weakness as identified by Reviewer 1. Please see the validation for Reviewer 1's first weakness.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1.

1. Weakness Statement:
[The paper does not explore the sensitivity of SRPO to different hyperparameters, such as the weighting parameters and the entropy threshold. A thorough analysis of how these hyperparameters affect the performance of SRPO is missing, which could limit the understanding of the method's robustness and generalizability.]

2. Evidence Collection:
   - This is the same weakness as identified by Reviewer 1. Please see the validation for Reviewer 1's second weakness.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1.

**Review 4 Weaknesses:**

1. Weakness Statement:
[The paper lacks a detailed analysis of the computational overhead of SRPO compared to GRPO and SDPO. While the authors mention lower per-step compute costs, they do not provide a breakdown of the computational resources required for each component of SRPO, such as the self-teacher computation and entropy-aware dynamic weighting. This makes it difficult to assess the practical efficiency of the method.]

2. Evidence Collection:
   - This is the same weakness as identified by Reviewer 1 and 3. Please see the validation for Reviewer 1's first weakness.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1.

1. Weakness Statement:
[The paper does not explore the sensitivity of SRPO to different hyperparameters, such as the weighting parameters and the entropy threshold. A thorough analysis of how these hyperparameters affect the performance of SRPO is missing, which could limit the understanding of the method's robustness and generalizability.]

2. Evidence Collection:
   - This is the same weakness as identified by Reviewer 1 and 3. Please see the validation for Reviewer 1's second weakness.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1.

1. Weakness Statement:
[How does SRPO handle the exploration-exploitation trade-off in post-training? Does the combination of GRPO and SDPO encourage sufficient exploration of the policy space, or does it primarily rely on exploitation of the current policy?]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper describes GRPO as a reward-driven approach, which inherently encourages exploration through reward maximization.
   - SDPO uses logit-level guidance, which can be seen as a form of exploitation.
   - The dynamic weighting mechanism in SRPO aims to balance the influence of GRPO and SDPO based on the reliability of the self-teacher's guidance.

3. Literature Gap Analysis:
   - The paper doesn't explicitly discuss the exploration-exploitation trade-off in the context of SRPO.

4. Validation Analysis:
   - While GRPO's nature encourages exploration, the paper doesn't explicitly analyze how the combination with SDPO and the dynamic weighting affects this trade-off.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper describes the components but lacks a direct analysis of the exploration-exploitation trade-off.

1. Weakness Statement:
[How sensitive is SRPO to the choice of hyperparameters, such as the weighting parameters and the entropy threshold? Are there any guidelines for selecting appropriate values for these hyperparameters in different settings?]

2. Evidence Collection:
   - This is the same weakness as identified by Reviewer 1 and 3. Please see the validation for Reviewer 1's second weakness.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1.

1. Weakness Statement:
[How does SRPO perform on tasks that require more complex reasoning or planning? Are there any limitations or challenges in applying SRPO to such tasks?]

2. Evidence Collection:
a) Experiment-related Evidence:
   - The paper evaluates on five benchmarks, which include tasks requiring reasoning (Chemistry, Physics, Biology, Materials) and tool use (Tool Use).
   - The results show SRPO's performance on these tasks.

3. Literature Gap Analysis:
   - The paper doesn't explicitly discuss limitations related to complex reasoning or planning.

4. Validation Analysis:
   - The paper shows results on tasks requiring reasoning, but it doesn't delve into the specific challenges or limitations of SRPO in these scenarios.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper shows results on reasoning tasks but lacks a detailed discussion of limitations.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces Sample-Routed Policy Optimization (SRPO), a novel method for post-training large language models (LLMs) using verifiable rewards. The core idea behind SRPO is to combine the strengths of two existing approaches: Group Relative Policy Optimization (GRPO) and Self-Distillation Policy Optimization (SDPO). GRPO provides reward-aligned reinforcement by normalizing outcomes across a group of rollouts, ensuring that the policy is optimized based on relative rewards. SDPO, on the other hand, uses self-distillation to provide dense, logit-level guidance for corrections, which is particularly useful for fine-grained adjustments. SRPO's key innovation lies in its ability to route correct samples to GRPO for reward alignment and failed samples to SDPO for targeted logit-level correction. This selective routing is further enhanced by an entropy-aware dynamic weighting mechanism, which suppresses unreliable corrections while emphasizing confident ones. The authors demonstrate that SRPO achieves a rapid early improvement and long-horizon stability compared to GRPO and SDPO, with improvements in peak performance and reduced per-step compute costs. The method is evaluated across five benchmarks and two model scales, showing consistent outperformance and moderate response lengths. The experimental results suggest that SRPO effectively balances the exploration-exploitation trade-off, leveraging the strengths of both reward-driven reinforcement and self-distilled guidance. The paper's main contribution is the SRPO framework, which offers a practical and efficient approach to post-training LLMs, particularly in scenarios where verifiable rewards are available. The authors present a clear and well-structured methodology, supported by comprehensive experimental results, making a significant contribution to the field of reinforcement learning from verifiable rewards. The combination of GRPO and SDPO, along with the dynamic weighting mechanism, is a creative and effective approach to improving the stability and efficiency of post-training. The empirical findings are compelling, demonstrating the superiority of SRPO over its individual components and other baselines. Overall, this paper presents a valuable contribution to the field, offering a novel and effective method for post-training LLMs that is both theoretically sound and empirically validated.


## Soundness:

2.75


## Presentation:

2.75


## Contribution:

2.75


## Strengths:

The primary strength of this paper lies in its introduction of Sample-Routed Policy Optimization (SRPO), a novel and effective method for post-training large language models. The core idea of combining GRPO and SDPO through a sample-based routing mechanism is both innovative and well-motivated. By routing correct samples to GRPO for reward alignment and failed samples to SDPO for targeted correction, SRPO effectively addresses the limitations of each individual method. The addition of an entropy-aware dynamic weighting mechanism further enhances the stability and efficiency of the training process. This mechanism intelligently suppresses unreliable corrections and emphasizes confident ones, leading to more robust policy updates. The experimental results presented in the paper are comprehensive and convincing. The authors evaluate SRPO across five benchmarks and two model scales, consistently demonstrating its superiority over GRPO and SDPO. The results show that SRPO achieves higher peak performance and reduced per-step compute costs, highlighting its practical efficiency. The ablation study further validates the importance of the different components of SRPO, confirming the effectiveness of the sample routing and dynamic weighting mechanisms. The paper is also well-written and easy to follow, with a clear explanation of the methodology and experimental setup. The figures and tables are well-designed and effectively illustrate the key concepts and results. The authors clearly articulate the motivation behind SRPO and the details of the method, making it accessible to a broad audience. The combination of GRPO and SDPO, along with the dynamic weighting mechanism, is a creative and effective approach to improving the stability and efficiency of post-training. The empirical findings are compelling, demonstrating the superiority of SRPO over its individual components and other baselines. The paper's contribution is significant, offering a novel and effective method for post-training LLMs that is both theoretically sound and empirically validated. The authors have successfully addressed a critical issue in RL from verifiable rewards by combining the strengths of two existing methods in a novel and effective way.


## Weaknesses:

While the paper presents a compelling method, several weaknesses warrant attention. First, the paper lacks a detailed analysis of the computational overhead of SRPO compared to GRPO and SDPO. Although the authors mention lower per-step compute costs, they do not provide a breakdown of the computational resources required for each component of SRPO, such as the self-teacher computation and the entropy-aware dynamic weighting. This makes it difficult to assess the practical efficiency of the method. While Table 1 provides the overall per-step compute cost, it does not offer a granular breakdown of the computational overhead of each component. This lack of detail makes it challenging to understand the computational trade-offs involved in using SRPO. Second, the paper does not explore the sensitivity of SRPO to different hyperparameters, such as the weighting parameters and the entropy threshold. A thorough analysis of how these hyperparameters affect the performance of SRPO is missing, which could limit the understanding of the method's robustness and generalizability. The paper mentions a hyperparameter β for the dynamic weighting mechanism, but it does not include a dedicated ablation study on its sensitivity. This omission makes it difficult to determine the optimal values for these hyperparameters in different settings and raises concerns about the method's practical applicability. The absence of such an analysis limits the understanding of the method's robustness and generalizability. Third, the paper lacks a detailed comparison of SRPO with other state-of-the-art methods for post-training LLMs, particularly those that also aim to improve the stability and efficiency of post-training, such as those based on reinforcement learning from human feedback (RLHF) or other self-improvement techniques. While the paper compares SRPO with GRPO and SDPO, it does not delve into a detailed comparison with RLHF or other self-improvement techniques. This omission limits the understanding of SRPO's unique advantages and limitations within the broader landscape of post-training methods. A more comprehensive comparison would help to contextualize the contribution of SRPO and highlight its specific strengths and weaknesses. Finally, while the paper presents results on five benchmarks, it lacks a detailed analysis of the performance of SRPO on different types of tasks and benchmarks. The paper evaluates SRPO across five benchmarks, but it does not include a granular analysis of SRPO's effectiveness on individual tasks within the benchmarks. This makes it difficult to understand why SRPO performs better on some tasks than others and how the method adapts to different task characteristics. A more detailed analysis of the performance of SRPO on different tasks would provide a more comprehensive understanding of its strengths and weaknesses. These weaknesses, while not invalidating the core contributions of the paper, highlight areas where further investigation and analysis are needed to fully understand the potential and limitations of SRPO.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should provide a more detailed analysis of the computational overhead of SRPO. This should include a breakdown of the computational costs associated with each component of SRPO, such as the self-teacher computation and the entropy-aware dynamic weighting. This analysis should include a comparison of the computational costs of SRPO with those of GRPO and SDPO, and should consider the impact of different batch sizes and model sizes on the overall computational cost. Furthermore, the authors should provide a more detailed analysis of the memory requirements of SRPO, as this is an important factor in the practical application of the method. A clear understanding of the computational overhead is crucial for assessing the practical efficiency of SRPO and for comparing it with other post-training methods. Second, the authors should conduct a thorough sensitivity analysis of SRPO to different hyperparameters. This analysis should include a systematic exploration of the impact of the weighting parameters and the entropy threshold on the performance of SRPO. The authors should also provide guidelines for selecting appropriate values for these hyperparameters in different settings. This analysis should include a discussion of the trade-offs between different hyperparameter settings and should provide insights into the robustness of the method. For example, how does the optimal weighting parameter vary across different benchmarks? What is the effect of the entropy threshold on the stability and convergence of the training process? This analysis would help to ensure that SRPO is robust and generalizable across a range of different settings. Third, the authors should include a more detailed comparison of SRPO with other state-of-the-art methods for post-training LLMs, particularly those that also aim to improve the stability and efficiency of post-training, such as techniques based on reinforcement learning from human feedback (RLHF) or other self-improvement techniques. This comparison should not only focus on performance metrics but also delve into the underlying mechanisms and assumptions of each method. For instance, a detailed analysis of how SRPO's sample-based approach compares to the more common policy gradient methods used in RLHF would be beneficial. This would help to clarify the unique contributions of SRPO and its potential advantages over existing approaches. This would also help to contextualize the contribution of SRPO within the broader landscape of post-training methods. Finally, the authors should provide a more detailed analysis of the performance of SRPO on different types of tasks and benchmarks. This analysis should go beyond simply reporting overall performance metrics and delve into the specific characteristics of the tasks and benchmarks that make SRPO more effective. For example, the authors could analyze the performance of SRPO on tasks that require different types of reasoning or planning, and discuss how the combination of GRPO and SDPO contributes to its success in these different contexts. They should also analyze the performance of SRPO on tasks with varying levels of complexity and difficulty, and discuss how the method adapts to these different challenges. This analysis should also include a discussion of the failure cases of SRPO and the potential reasons for these failures. By providing a more detailed analysis of the performance of SRPO on different tasks, the authors can provide a more comprehensive understanding of its strengths and weaknesses and help to guide future research in this area. These suggestions, if implemented, would significantly strengthen the paper and provide a more complete understanding of the SRPO method.


## Questions:

Several questions arise from my analysis of the paper. First, how does SRPO handle the exploration-exploitation trade-off in post-training? Does the combination of GRPO and SDPO encourage sufficient exploration of the policy space, or does it primarily rely on exploitation of the current policy? While GRPO's nature encourages exploration, the paper doesn't explicitly analyze how the combination with SDPO and the dynamic weighting affects this trade-off. A more detailed discussion of this aspect would be beneficial. Second, how sensitive is SRPO to the choice of hyperparameters, such as the weighting parameters and the entropy threshold? Are there any guidelines for selecting appropriate values for these hyperparameters in different settings? The paper mentions a hyperparameter β for the dynamic weighting mechanism, but it lacks a dedicated ablation study on its sensitivity. A more thorough analysis of the impact of these hyperparameters on performance is needed. Third, how does SRPO perform on tasks that require more complex reasoning or planning? Are there any limitations or challenges in applying SRPO to such tasks? The paper evaluates SRPO on five benchmarks, which include tasks requiring reasoning, but it doesn't delve into the specific challenges or limitations of SRPO in these scenarios. A more detailed discussion of the performance of SRPO on complex reasoning tasks would be valuable. Finally, how does the performance of SRPO scale with the size of the LLM and the number of samples? Are there any practical limitations or trade-offs in scaling SRPO to larger models or datasets? The paper evaluates SRPO on two model scales, but it does not provide a detailed analysis of the scaling behavior of SRPO with respect to model size and dataset size. A more detailed analysis of the scalability of SRPO would be beneficial for understanding its practical applicability.


## Rating:

5.75


## Confidence:

3.25


## Decision:

Reject
}