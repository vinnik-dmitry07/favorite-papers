I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper proposes a new policy gradient algorithm, SPO, which is group-free and uses global advantage normalization. The authors claim that their algorithm is motivated by the drawbacks of the existing GRPO algorithm. The authors show that SPO outperforms GRPO on several reasoning benchmarks.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

- The proposed algorithm is simple and easy to implement.
- The authors show that SPO outperforms GRPO on several reasoning benchmarks.

### Weaknesses

#### Some Related Works

[1] A Baseline for Any RL Algorithm, NeurIPS 2020.

#### comment

 - The baselines are not strong enough. The authors only compare their algorithm with GRPO. However, there are several works that improve GRPO, such as CISPO [1], which outperforms GRPO on most of the tasks in this paper. It is unclear if the performance gain comes from the proposed global advantage normalization or the group-free design.
- The experiments are not comprehensive enough. The authors only evaluate their algorithm on reasoning tasks. It is unclear if the proposed algorithm can generalize to other tasks, such as RLHF tasks. The lack of evaluation on diverse tasks makes it difficult to assess the robustness and general applicability of the proposed method.
- The authors claim that their algorithm is more robust to degenerate groups. However, there is no experiment to support this claim. It is unclear how the proposed algorithm handles situations where a large portion of the generated samples are degenerate, and how this compares to GRPO in such scenarios.

### Suggestions

The paper would benefit significantly from a more thorough experimental evaluation. Specifically, the authors should compare their algorithm against a wider range of baselines, including CISPO [1], which has demonstrated superior performance compared to GRPO on various tasks. This comparison is crucial to isolate the impact of the proposed global advantage normalization and the group-free design. Furthermore, the authors should evaluate their algorithm on a more diverse set of tasks, including those commonly used in RLHF, such as the summarization task from the AlpacaEval benchmark. This would provide a more comprehensive understanding of the algorithm's generalizability and robustness. The evaluation should also include an analysis of the performance of the algorithm under different levels of degenerate groups, to validate the claim that SPO is more robust to such scenarios.

To further strengthen the paper, the authors should provide a more detailed analysis of the performance differences between SPO and GRPO. Specifically, it would be beneficial to investigate the impact of the global advantage normalization on the learning dynamics. For example, the authors could analyze the variance of the gradients and the convergence rate of the two algorithms. This analysis could provide insights into why SPO outperforms GRPO and how the proposed normalization technique contributes to this improvement. Additionally, the authors should provide a more detailed explanation of the KL-adaptive tracker, including how it is initialized and how it adapts during training. This would help the reader better understand the inner workings of the algorithm.

Finally, the authors should provide a more detailed discussion of the limitations of their algorithm. For example, they should discuss the computational cost of SPO compared to GRPO, and whether the proposed algorithm is suitable for all types of reinforcement learning tasks. They should also discuss the potential challenges of applying SPO to more complex environments with high-dimensional state and action spaces. Addressing these limitations would provide a more balanced and comprehensive view of the proposed algorithm and its potential impact.

### Questions

- Could you provide more baselines and experiments to support your claim?
- Could you provide more analysis to show the performance gain comes from the proposed global advantage normalization?
- Could you provide more analysis to show that SPO is more robust to degenerate groups?

### Rating

3

### Confidence

4

**********

## Reviewer 2

### Summary

This paper proposes a new policy gradient algorithm, SPO, which is group-free and uses global advantage normalization. The authors claim that their algorithm is motivated by the drawbacks of the existing GRPO algorithm. The authors show that SPO outperforms GRPO on several reasoning benchmarks.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The proposed algorithm is simple and easy to implement.
2. The authors show that SPO outperforms GRPO on several reasoning benchmarks.

### Weaknesses

#### Some Related Works


#### comment

1. The baselines are not strong enough. The authors only compare their algorithm with GRPO. However, there are several works that improve GRPO, such as CISPO [1], which outperforms GRPO on most of the tasks in this paper. It is unclear if the performance gain comes from the proposed global advantage normalization or the group-free design.
2. The experiments are not comprehensive enough. The authors only evaluate their algorithm on reasoning tasks. It is unclear if the proposed algorithm can generalize to other tasks, such as RLHF tasks. The lack of evaluation on diverse tasks makes it difficult to assess the robustness and general applicability of the proposed method.
3. The authors claim that their algorithm is more robust to degenerate groups. However, there is no experiment to support this claim. It is unclear how the proposed algorithm handles situations where a large portion of the generated samples are degenerate, and how this compares to GRPO in such scenarios.

### Suggestions

The paper would benefit significantly from a more thorough experimental evaluation. Specifically, the authors should compare their algorithm against a wider range of baselines, including CISPO [1], which has demonstrated superior performance compared to GRPO on various tasks. This comparison is crucial to isolate the impact of the proposed global advantage normalization and the group-free design. Furthermore, the authors should evaluate their algorithm on a more diverse set of tasks, including those commonly used in RLHF, such as the summarization task from the AlpacaEval benchmark. This would provide a more comprehensive understanding of the algorithm's generalizability and robustness. The evaluation should also include an analysis of the performance of the algorithm under different levels of degenerate groups, to validate the claim that SPO is more robust to such scenarios. 

To further strengthen the paper, the authors should provide a more detailed analysis of the performance differences between SPO and GRPO. Specifically, it would be beneficial to investigate the impact of the global advantage normalization on the learning dynamics. For example, the authors could analyze the variance of the gradients and the convergence rate of the two algorithms. This analysis could provide insights into why SPO outperforms GRPO and how the proposed normalization technique contributes to this improvement. Additionally, the authors should provide a more detailed explanation of the KL-adaptive tracker, including how it is initialized and how it adapts during training. This would help the reader better understand the inner workings of the algorithm. 

Finally, the authors should provide a more detailed discussion of the limitations of their algorithm. For example, they should discuss the computational cost of SPO compared to GRPO, and whether the proposed algorithm is suitable for all types of reinforcement learning tasks. They should also discuss the potential challenges of applying SPO to more complex environments with high-dimensional state and action spaces. Addressing these limitations would provide a more balanced and comprehensive view of the proposed algorithm and its potential impact.

### Questions

See weakness.

### Rating

3

### Confidence

4

**********

## Reviewer 3

### Summary

This paper proposes a new policy gradient method, SPO, which is group-free and uses global advantage normalization. The authors claim that their algorithm is motivated by the drawbacks of the existing GRPO algorithm. The authors show that SPO outperforms GRPO on several reasoning benchmarks.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

The proposed algorithm is simple and easy to implement. The authors show that SPO outperforms GRPO on several reasoning benchmarks.

### Weaknesses

#### Some Related Works


#### comment

The baselines are not strong enough. The authors only compare their algorithm with GRPO. However, there are several works that improve GRPO, such as CISPO [1], which outperforms GRPO on most of the tasks in this paper. It is unclear if the performance gain comes from the proposed global advantage normalization or the group-free design.

The experiments are not comprehensive enough. The authors only evaluate their algorithm on reasoning tasks. It is unclear if the proposed algorithm can generalize to other tasks, such as RLHF tasks.

The authors claim that their algorithm is more robust to degenerate groups. However, there is no experiment to support this claim. It is unclear how the proposed algorithm handles situations where a large portion of the generated samples are degenerate, and how this compares to GRPO in such scenarios.

### Suggestions

The paper would benefit significantly from a more thorough experimental evaluation. Specifically, the authors should compare their algorithm against a wider range of baselines, including CISPO [1], which has demonstrated superior performance compared to GRPO on various tasks. This comparison is crucial to isolate the impact of the proposed global advantage normalization and the group-free design. Furthermore, the authors should evaluate their algorithm on a more diverse set of tasks, including those commonly used in RLHF, such as the summarization task from the AlpacaEval benchmark. This would provide a more comprehensive understanding of the algorithm's generalizability and robustness. The evaluation should also include an analysis of the performance of the algorithm under different levels of degenerate groups, to validate the claim that SPO is more robust to such scenarios.

To further strengthen the paper, the authors should provide a more detailed analysis of the performance differences between SPO and GRPO. Specifically, it would be beneficial to investigate the impact of the global advantage normalization on the learning dynamics. For example, the authors could analyze the variance of the gradients and the convergence rate of the two algorithms. This analysis could provide insights into why SPO outperforms GRPO and how the proposed normalization technique contributes to this improvement. Additionally, the authors should provide a more detailed explanation of the KL-adaptive tracker, including how it is initialized and how it adapts during training. This would help the reader better understand the inner workings of the algorithm.

Finally, the authors should provide a more detailed discussion of the limitations of their algorithm. For example, they should discuss the computational cost of SPO compared to GRPO, and whether the proposed algorithm is suitable for all types of reinforcement learning tasks. They should also discuss the potential challenges of applying SPO to more complex environments with high-dimensional state and action spaces. Addressing these limitations would provide a more balanced and comprehensive view of the proposed algorithm and its potential impact.

### Questions

See weakness.

### Rating

5

### Confidence

3

**********

## Reviewer 4

### Summary

This paper introduces Single-stream Policy Optimization (SPO), a new policy gradient method for reinforcement learning (RL) in large language models (LLMs). The authors argue that existing group-based methods, such as GRPO, suffer from inefficiencies like wasted computational resources and synchronization bottlenecks. SPO addresses these issues by employing a KL-adaptive value tracker and global advantage normalization, which provide a stable, low-variance learning signal and eliminate the need for group-based baselines. The authors demonstrate that SPO outperforms GRPO on challenging reasoning benchmarks, such as AIME and HMMT 2025, with more robust and consistent performance. The paper also highlights the scalability and efficiency of SPO, showing that it can achieve a 4.35× training throughput speedup in agentic training scenarios.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a thorough background and motivation for their work, clearly articulating the limitations of existing methods and the need for a more efficient and scalable approach.
3. The experimental results are comprehensive and demonstrate the effectiveness of SPO on challenging reasoning benchmarks.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed discussion of the limitations of SPO, such as its potential sensitivity to hyperparameter settings or its applicability to different types of tasks. Specifically, the paper does not explore how the KL-divergence threshold, which controls the exploration of the value tracker, impacts performance across various tasks. It is unclear if a single threshold is optimal for all scenarios, or if task-specific tuning is necessary. Furthermore, the paper does not address the potential for the value tracker to become overly conservative, hindering exploration in complex environments.
2. The paper could benefit from a more comprehensive comparison with other state-of-the-art RL algorithms, beyond just GRPO. While the authors demonstrate improvements over GRPO, it is not clear how SPO compares to other single-policy optimization methods or to methods that use different forms of advantage estimation. A more thorough comparison would help to contextualize the contribution of SPO and highlight its unique advantages and disadvantages.

### Suggestions

The authors should provide a more in-depth analysis of the KL-divergence threshold's impact on SPO's performance. This should include experiments with varying threshold values across different tasks, such as AIME, BGE, and HMMT, to determine the optimal setting for each. The paper should also discuss the potential trade-offs between exploration and exploitation when tuning this parameter. For example, a higher threshold might lead to faster convergence but could also limit the exploration of potentially high-reward solutions. It would be beneficial to include a sensitivity analysis that shows how the performance of SPO changes with different threshold values, and provide guidelines for selecting appropriate values for different types of tasks. This analysis should also consider the computational cost associated with different threshold values, as a very high threshold might lead to slower training times.

Furthermore, the paper should include a more comprehensive comparison with other state-of-the-art single-policy optimization methods. This comparison should not be limited to GRPO, but should also include methods that use different forms of advantage estimation, such as those based on temporal difference learning or actor-critic frameworks. The authors should also compare SPO with methods that do not rely on group-based baselines, to highlight the specific advantages of their approach. This comparison should include a detailed analysis of the computational cost, convergence speed, and final performance of each method. The paper should also discuss the potential limitations of SPO, such as its applicability to different types of tasks or its sensitivity to hyperparameter settings. This would help to provide a more balanced and comprehensive view of the contribution of SPO.

Finally, the authors should provide more details on the implementation of SPO, including the specific choices of hyperparameters and the optimization algorithm used. This would allow other researchers to reproduce the results and build upon the work. The paper should also include a discussion of the potential limitations of SPO, such as its applicability to different types of tasks or its sensitivity to hyperparameter settings. This would help to provide a more balanced and comprehensive view of the contribution of SPO. The authors should also discuss the potential for the value tracker to become overly conservative, hindering exploration in complex environments. This should include experiments with different value trackers and a discussion of the trade-offs between exploration and exploitation.

### Questions

1. How does SPO perform on tasks that require more complex reasoning or planning?
2. What are the limitations of SPO, and how can they be addressed in future work?

### Rating

5

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in a given paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

**Plan:**
1. Read each reviewer's weakness.
2. Search the paper for evidence related to the weakness.
3. Categorize the evidence and link it to the specific weakness.
4. Formulate a conclusion about the validity of the weakness based on the evidence.
**Review 1 Weaknesses:**

1. Weakness Statement:
"The baselines are not strong enough. The authors only compare their algorithm with GRPO. However, there are several works that improve GRPO, such as CISPO [1], which outperforms GRPO on most of the tasks in this paper. It is unclear if the performance gain comes from the proposed global advantage normalization or the group-free design."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper explicitly states the baselines used in the experiments: "We compare SPO with GRPO, a baseline method that uses a leave-one-out approach for estimating the group baseline." (Section 5.2)
b) Experiment-related Evidence:
   - The "Empirical Comparison with GRPO" experiment (Section 5.2) only includes GRPO as a baseline.
   - The results section (Table 1) only presents comparisons between Qwen3-8B and SPO, and Qwen3-8B and GRPO.

3. Literature Gap Analysis:
   - The paper does not cite or compare against CISPO or other methods that directly improve upon GRPO.

4. Validation Analysis:
   - The reviewer correctly points out that the experimental section only compares SPO against GRPO. The paper's motivation section mentions the limitations of GRPO, but the experimental validation doesn't directly address whether the performance gains are due to the global advantage normalization or the group-free design by comparing against more recent or stronger baselines like CISPO.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The experimental setup explicitly lists GRPO as the only baseline, and the results section only includes comparisons with GRPO.

1. Weakness Statement:
"The experiments are not comprehensive enough. The authors only evaluate their algorithm on reasoning tasks. It is unclear if the proposed algorithm can generalize to other tasks, such as RLHF tasks. The lack of evaluation on diverse tasks makes it difficult to assess the robustness and general applicability of the proposed method."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "Empirical Comparison with GRPO" experiment (Section 5.2) uses Tool-Integrated Reasoning (TIR) scenarios and benchmarks AIME 24, AIME 25, BeyondAIME, BRUMO 25, and HMMT 25.
   - The "Advantages over GRPO" experiment (Section 5.3) uses the same benchmarks.
   - The "Agentic Training Demonstrations" experiment (Section 5.4) uses agentic training scenarios with specific time constraints.

3. Literature Gap Analysis:
   - The paper does not include experiments on standard RLHF benchmarks or other types of tasks beyond reasoning.

4. Validation Analysis:
   - The reviewer is correct. The experiments are focused on reasoning tasks. There is no evaluation on tasks like RLHF, which would provide a different perspective on the algorithm's generalizability.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The experimental sections explicitly list the reasoning benchmarks used, with no mention of RLHF or other task types.

1. Weakness Statement:
"The authors claim that their algorithm is more robust to degenerate groups. However, there is no experiment to support this claim. It is unclear how the proposed algorithm handles situations where a large portion of the generated samples are degenerate, and how this compares to GRPO in such scenarios."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions the issue of degenerate groups in the introduction and motivation: "When all responses in a group share the same outcome (e.g., all correct or all incorrect), the relative advantage collapses to zero, yielding no learning signal." (Introduction)
   - The proposed method aims to address this by using a KL-adaptive tracker and global advantage normalization.
b) Experiment-related Evidence:
   - The "Empirical Comparison with GRPO" experiment (Section 5.2) includes an "ineffective gradient ratios" analysis (Figure 3a), which shows the fraction of ineffective samples in SPO is much lower than GRPO.
   - The paper states: "This indicates that SPO is more effective at avoiding situations where all responses in a group have the same outcome, leading to a more robust and consistent learning signal." (Section 5.2)

3. Literature Gap Analysis:
   - While the paper shows a lower fraction of ineffective samples, it doesn't explicitly compare the performance of SPO and GRPO under scenarios where a *large portion* of generated samples are degenerate.

4. Validation Analysis:
   - The reviewer's point is partially valid. The paper *does* provide evidence (Figure 3a) that SPO is less prone to having ineffective gradients compared to GRPO. However, it doesn't directly test the performance of SPO and GRPO when a *large portion* of generated samples are degenerate. The analysis focuses on the overall fraction of ineffective samples, not a specific scenario with a majority of degenerate samples.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: Figure 3a shows a lower fraction of ineffective samples for SPO, but there's no specific experiment testing performance under a high proportion of degenerate samples.

**Review 2 Weaknesses:**

1. Weakness Statement:
"The paper lacks a detailed discussion of the limitations of SPO, such as its potential sensitivity to hyperparameter settings or its applicability to different types of tasks. Specifically, the paper does not explore how the KL-divergence threshold, which controls the exploration of the value tracker, impacts performance across various tasks. It is unclear if a single threshold is optimal for all scenarios, or if task-specific tuning is necessary. Furthermore, the paper does not address the potential for the value tracker to become overly conservative, hindering exploration in complex environments."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper introduces the KL-adaptive tracker and mentions the discount factor $\rho(x)$ (Section 4.1).
   - The paper mentions the initial effective sample size $N_0$ and the initial learning rate $\eta_{\mathcal{X}}$ (Section 4.1).
b) Experiment-related Evidence:
   - The paper mentions the initialization of the value tracker parameters: "To initialize, we collect n 0 samples to compute an initial value estimate v ^ 0 ​ ." (Section 4.1)
   - The paper does not include experiments varying the KL-divergence threshold or the initial sample size $N_0$.

3. Literature Gap Analysis:
   - The paper does not discuss the sensitivity of SPO to hyperparameters like the KL-divergence threshold or the initial sample size.

4. Validation Analysis:
   - The reviewer is correct. The paper lacks a detailed discussion and experimentation on the sensitivity of SPO to its hyperparameters, particularly the KL-divergence threshold and the initial sample size. The paper also doesn't explicitly address the potential for the value tracker to become overly conservative.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The method section introduces hyperparameters like $\rho(x)$, $N_0$, and $\eta_{\mathcal{X}}$, but the experimental section lacks a systematic evaluation of their impact.

1. Weakness Statement:
"The paper could benefit from a more comprehensive comparison with other state-of-the-art RL algorithms, beyond just GRPO. While the authors demonstrate improvements over GRPO, it is not clear how SPO compares to other single-policy optimization methods or to methods that use different forms of advantage estimation. A more thorough comparison would help to contextualize the contribution of SPO and highlight its unique advantages and disadvantages."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "Empirical Comparison with GRPO" experiment (Section 5.2) only includes GRPO as a baseline.
   - The paper does not include comparisons with other single-policy optimization methods or methods using different forms of advantage estimation.

3. Literature Gap Analysis:
   - The paper's related work section mentions some other group-free methods (Bastian et al., 2023; RLOO, 2023; Liu et al., 2023), but these are not used as experimental baselines.

4. Validation Analysis:
   - The reviewer's point is valid. The experimental section is limited to a comparison with GRPO. A broader comparison with other relevant state-of-the-art RL algorithms would provide a more comprehensive understanding of SPO's strengths and weaknesses.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The experimental section only includes GRPO as a baseline, and the related work section mentions other relevant methods that are not included in the experiments.

**Review 3 Weaknesses:**

1. Weakness Statement:
"The baselines are not strong enough. The authors only compare their algorithm with GRPO. However, there are several works that improve GRPO, such as CISPO [1], which outperforms GRPO on most of the tasks in this paper. It is unclear if the performance gain comes from the proposed global advantage normalization or the group-free design."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "Empirical Comparison with GRPO" experiment (Section 5.2) only includes GRPO as a baseline.
   - The results section (Table 1) only presents comparisons between Qwen3-8B and SPO, and Qwen3-8B and GRPO.

3. Literature Gap Analysis:
   - The paper does not cite or compare against CISPO or other methods that directly improve upon GRPO.

4. Validation Analysis:
   - This is the same weakness identified by Reviewer 1, and the validation remains the same. The experimental section lacks a comparison with stronger baselines.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The experimental setup explicitly lists GRPO as the only baseline, and the results section only includes comparisons with GRPO.

1. Weakness Statement:
"The experiments are not comprehensive enough. The authors only evaluate their algorithm on reasoning tasks. It is unclear if the proposed algorithm can generalize to other tasks, such as RLHF tasks. The lack of evaluation on diverse tasks makes it difficult to assess the robustness and general applicability of the proposed method."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "Empirical Comparison with GRPO" experiment (Section 5.2) uses Tool-Integrated Reasoning (TIR) scenarios and benchmarks AIME 24, AIME 25, BeyondAIME, BRUMO 25, and HMMT 25.
   - The "Advantages over GRPO" experiment (Section 5.3) uses the same benchmarks.
   - The "Agentic Training Demonstrations" experiment (Section 5.4) uses agentic training scenarios with specific time constraints.

3. Literature Gap Analysis:
   - The paper does not include experiments on standard RLHF benchmarks or other types of tasks beyond reasoning.

4. Validation Analysis:
   - This is the same weakness identified by Reviewer 1, and the validation remains the same. The experiments are limited to reasoning tasks.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The experimental sections explicitly list the reasoning benchmarks used, with no mention of RLHF or other task types.

1. Weakness Statement:
"The authors claim that their algorithm is more robust to degenerate groups. However, there is no experiment to support this claim. It is unclear how the proposed algorithm handles situations where a large portion of the generated samples are degenerate, and how this compares to GRPO in such scenarios."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions the issue of degenerate groups in the introduction and motivation: "When all responses in a group share the same outcome (e.g., all correct or all incorrect), the relative advantage collapses to zero, yielding no learning signal." (Introduction)
   - The proposed method aims to address this by using a KL-adaptive tracker and global advantage normalization.
b) Experiment-related Evidence:
   - The "Empirical Comparison with GRPO" experiment (Section 5.2) includes an "ineffective gradient ratios" analysis (Figure 3a), which shows the fraction of ineffective samples in SPO is much lower than GRPO.
   - The paper states: "This indicates that SPO is more effective at avoiding situations where all responses in a group have the same outcome, leading to a more robust and consistent learning signal." (Section 5.2)

3. Literature Gap Analysis:
   - While the paper shows a lower fraction of ineffective samples, it doesn't explicitly compare the performance of SPO and GRPO under scenarios where a *large portion* of generated samples are degenerate.

4. Validation Analysis:
   - This is the same weakness identified by Reviewer 1, and the validation remains the same. The paper provides evidence of reduced ineffective samples but lacks a specific experiment on high degeneracy scenarios.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: Figure 3a shows a lower fraction of ineffective samples for SPO, but there's no specific experiment testing performance under a high proportion of degenerate samples.

**Review 4 Weaknesses:**

1. Weakness Statement:
"The paper lacks a detailed discussion of the limitations of SPO, such as its potential sensitivity to hyperparameter settings or its applicability to different types of tasks. Specifically, the paper does not explore how the KL-divergence threshold, which controls the exploration of the value tracker, impacts performance across various tasks. It is unclear if a single threshold is optimal for all scenarios, or if task-specific tuning is necessary. Furthermore, the paper does not address the potential for the value tracker to become overly conservative, hindering exploration in complex environments."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper introduces the KL-adaptive tracker and mentions the discount factor $\rho(x)$ (Section 4.1).
   - The paper mentions the initial effective sample size $N_0$ and the initial learning rate $\eta_{\mathcal{X}}$ (Section 4.1).
b) Experiment-related Evidence:
   - The paper mentions the initialization of the value tracker parameters: "To initialize, we collect n 0 samples to compute an initial value estimate v ^ 0 ​ ." (Section 4.1)
   - The paper does not include experiments varying the KL-divergence threshold or the initial sample size $N_0$.

3. Literature Gap Analysis:
   - The paper does not discuss the sensitivity of SPO to hyperparameters like the KL-divergence threshold or the initial sample size.

4. Validation Analysis:
   - This is the same weakness identified by Reviewer 2, and the validation remains the same. The paper lacks a detailed discussion and experimentation on the sensitivity of SPO to its hyperparameters.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The method section introduces hyperparameters like $\rho(x)$, $N_0$, and $\eta_{\mathcal{X}}$, but the experimental section lacks a systematic evaluation of their impact.

1. Weakness Statement:
"The paper could benefit from a more comprehensive comparison with other state-of-the-art RL algorithms, beyond just GRPO. While the authors demonstrate improvements over GRPO, it is not clear how SPO compares to other single-policy optimization methods or to methods that use different forms of advantage estimation. A more thorough comparison would help to contextualize the contribution of SPO and highlight its unique advantages and disadvantages."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "Empirical Comparison with GRPO" experiment (Section 5.2) only includes GRPO as a baseline.
   - The paper does not include comparisons with other single-policy optimization methods or methods using different forms of advantage estimation.

3. Literature Gap Analysis:
   - The paper's related work section mentions some other group-free methods (Bastian et al., 2023; RLOO, 2023; Liu et al., 2023), but these are not used as experimental baselines.

4. Validation Analysis:
   - This is the same weakness identified by Reviewer 2, and the validation remains the same. The experimental section is limited to a comparison with GRPO.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The experimental section only includes GRPO as a baseline, and the related work section mentions other relevant methods that are not included in the experiments.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces Single-stream Policy Optimization (SPO), a novel policy gradient algorithm designed to address the inefficiencies inherent in group-based methods like Grouped Policy Optimization (GRPO). The authors correctly identify that GRPO's drawbacks stem from its reliance on degenerate groups, where all responses within a group share the same outcome, leading to a collapse of the relative advantage and a lack of learning signal. SPO, in contrast, operates on a single stream of policy gradients, eliminating the need for group-based baselines and synchronization bottlenecks. The core of SPO lies in its use of a KL-adaptive value tracker, which provides a stable, low-variance learning signal by dynamically adjusting its memory based on the KL divergence between the current policy and a historical estimate. This tracker is combined with global advantage normalization, which further reduces the variance of the policy gradients. The authors argue that these design choices lead to more efficient and robust learning. Empirically, SPO is evaluated on a range of reasoning benchmarks, including AIME, BGE, and HMMT, where it demonstrates superior performance compared to GRPO. The results, presented in tables and figures, highlight SPO's ability to achieve higher success rates and more consistent performance across various tasks. Furthermore, the paper includes an analysis of the algorithm's scalability and efficiency, showing that SPO achieves a significant throughput speedup in agentic training scenarios. The authors also analyze the fraction of ineffective samples, demonstrating that SPO is less prone to getting stuck in situations where all responses in a group have the same outcome. Overall, the paper presents a well-motivated and empirically supported alternative to group-based policy optimization methods, with a focus on improving efficiency and robustness. The authors clearly articulate the limitations of existing methods and provide a compelling case for the advantages of SPO. The paper is well-written and easy to follow, making it accessible to a broad audience. However, there are some limitations in the experimental evaluation that need to be addressed to fully validate the claims made by the authors.


## Soundness:

2.25


## Presentation:

3.0


## Contribution:

2.0


## Strengths:

I find several aspects of this paper to be particularly strong. First, the proposed algorithm, SPO, is remarkably simple and easy to implement, which is a significant advantage for practical applications. The core idea of using a single stream of policy gradients, rather than group-based baselines, is a novel approach that directly addresses the inefficiencies of methods like GRPO. The use of a KL-adaptive value tracker is another notable contribution, as it provides a stable and low-variance learning signal, which is crucial for effective policy optimization. The global advantage normalization further enhances the stability and consistency of the learning process. The authors have clearly articulated the limitations of existing methods and have provided a compelling case for the advantages of SPO. The experimental results are also a significant strength of the paper. The authors demonstrate that SPO outperforms GRPO on a range of challenging reasoning benchmarks, including AIME, BGE, and HMMT. The inclusion of a thorough analysis of the algorithm's scalability and efficiency, showing that SPO achieves a significant throughput speedup in agentic training scenarios, is another positive aspect. The authors also show that SPO is more robust to degenerate groups, as evidenced by the lower fraction of ineffective samples compared to GRPO. The paper is well-written and easy to follow, making it accessible to a broad audience. The authors provide a clear and concise explanation of the algorithm and its motivation, which is essential for understanding the contribution of the paper. The experimental results are presented in a clear and organized manner, making it easy to compare the performance of SPO and GRPO. The inclusion of an analysis of the algorithm's performance under different conditions, such as varying levels of degenerate groups, is also a positive aspect. Overall, the paper presents a well-motivated and empirically supported alternative to group-based policy optimization methods, with a focus on improving efficiency and robustness. The authors have clearly demonstrated the potential of SPO and its advantages over existing methods.


## Weaknesses:

Despite the strengths of this paper, I have identified several weaknesses that need to be addressed. The most significant limitation is the lack of a comprehensive experimental evaluation. The authors only compare SPO against GRPO, a baseline method that has been shown to be outperformed by other methods, such as CISPO. This is a critical oversight, as it is unclear whether the performance gains observed with SPO are due to the proposed global advantage normalization or the group-free design. Without comparisons to stronger baselines, it is difficult to assess the true contribution of SPO. For example, the paper states that "Grouped Policy Optimization (GRPO) is a method that uses a leave-one-out approach for estimating the group baseline, but it suffers from several limitations, such as wasted computational resources and synchronization bottlenecks. In contrast, Single-stream Policy Optimization (SPO) aims to address these issues by providing a stable, low-variance learning signal and eliminating the need for group-based baselines." However, the experimental section only includes GRPO as a baseline, and the results section only presents comparisons with GRPO. This is a major limitation, as it does not provide a clear picture of how SPO compares to other state-of-the-art methods. My confidence in this weakness is high, as the paper explicitly states the limitations of GRPO and motivates the work, but the experimental validation doesn't directly address whether the performance gains are due to the proposed global advantage normalization or the group-free design by comparing against more recent or stronger baselines like CISPO. 

Another significant weakness is the limited scope of the experimental evaluation. The authors only evaluate their algorithm on reasoning tasks, specifically on benchmarks like AIME, BGE, and HMMT. While these are challenging reasoning tasks, it is unclear if the proposed algorithm can generalize to other tasks, such as RLHF tasks. The lack of evaluation on diverse tasks makes it difficult to assess the robustness and general applicability of the proposed method. The paper states that "The experiments are conducted using the Qwen3-8B model, which is a state-of-the-art large language model. The training data consists of the English subset from the DAPO dataset." However, the paper does not include experiments on standard RLHF benchmarks or other types of tasks beyond reasoning. This is a critical limitation, as it is unclear if the proposed algorithm can generalize to other tasks. My confidence in this weakness is high, as the experimental sections explicitly list the reasoning benchmarks used, with no mention of RLHF or other task types. 

Furthermore, the paper claims that their algorithm is more robust to degenerate groups, but there is no experiment to support this claim. While the paper does include an analysis of the fraction of ineffective samples, which shows that SPO is less prone to getting stuck in situations where all responses in a group have the same outcome, there is no specific experiment testing the performance of SPO and GRPO when a *large portion* of generated samples are degenerate. The paper states that "When all responses in a group share the same outcome (e.g., all correct or all incorrect), the relative advantage collapses to zero, yielding no learning signal." (Introduction) and that "This indicates that SPO is more effective at avoiding situations where all responses in a group have the same outcome, leading to a more robust and consistent learning signal." (Section 5.2). However, there is no experiment that specifically tests the performance of SPO and GRPO when a large portion of generated samples are degenerate. This is a critical oversight, as it is unclear how the proposed algorithm handles situations where a large portion of generated samples are degenerate. My confidence in this weakness is medium, as the paper shows a lower fraction of ineffective samples for SPO, but there's no specific experiment testing performance under a high proportion of degenerate samples. 

Finally, the paper lacks a detailed discussion of the limitations of SPO, such as its potential sensitivity to hyperparameter settings or its applicability to different types of tasks. Specifically, the paper does not explore how the KL-divergence threshold, which controls the exploration of the value tracker, impacts performance across various tasks. It is unclear if a single threshold is optimal for all scenarios, or if task-specific tuning is necessary. Furthermore, the paper does not address the potential for the value tracker to become overly conservative, hindering exploration in complex environments. The paper introduces the KL-adaptive tracker and mentions the discount factor $\rho(x)$ (Section 4.1), and the initial effective sample size $N_0$ and the initial learning rate $\eta_{\mathcal{X}}$ (Section 4.1). However, the experimental section lacks a systematic evaluation of their impact. My confidence in this weakness is high, as the method section introduces hyperparameters like $\rho(x)$, $N_0$, and $\eta_{\mathcal{X}}$, but the experimental section lacks a systematic evaluation of their impact.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First and foremost, the authors should significantly expand the experimental evaluation to include a wider range of baselines, including CISPO and other state-of-the-art single-policy optimization methods. This comparison is crucial to isolate the impact of the proposed global advantage normalization and the group-free design. Furthermore, the authors should evaluate their algorithm on a more diverse set of tasks, including those commonly used in RLHF, such as the summarization task from the AlpacaEval benchmark. This would provide a more comprehensive understanding of the algorithm's generalizability and robustness. The evaluation should also include an analysis of the performance of the algorithm under different levels of degenerate groups, to validate the claim that SPO is more robust to such scenarios. This could involve experiments with varying threshold values for the KL-divergence, to determine the optimal setting for each task. The paper should also discuss the potential trade-offs between exploration and exploitation when tuning this parameter. For example, a higher threshold might lead to faster convergence but could also limit the exploration of potentially high-reward solutions. It would be beneficial to include a sensitivity analysis that shows how the performance of SPO changes with different threshold values, and provide guidelines for selecting appropriate values for different types of tasks. This analysis should also consider the computational cost associated with different threshold values, as a very high threshold might lead to slower training times. 

To further strengthen the paper, the authors should provide a more detailed analysis of the performance differences between SPO and GRPO. Specifically, it would be beneficial to investigate the impact of the global advantage normalization on the learning dynamics. For example, the authors could analyze the variance of the gradients and the convergence rate of the two algorithms. This analysis could provide insights into why SPO outperforms GRPO and how the proposed normalization technique contributes to this improvement. Additionally, the authors should provide a more detailed explanation of the KL-adaptive tracker, including how it is initialized and how it adapts during training. This would help the reader better understand the inner workings of the algorithm. 

Finally, the authors should provide a more detailed discussion of the limitations of their algorithm. For example, they should discuss the computational cost of SPO compared to GRPO, and whether the proposed algorithm is suitable for all types of reinforcement learning tasks. They should also discuss the potential challenges of applying SPO to more complex environments with high-dimensional state and action spaces. Addressing these limitations would provide a more balanced and comprehensive view of the proposed algorithm and its potential impact. The authors should also discuss the potential for the value tracker to become overly conservative, hindering exploration in complex environments. This should include experiments with different value tracker initialization and adaptation strategies. By addressing these limitations, the authors would provide a more balanced and comprehensive view of the proposed algorithm and its potential impact.


## Questions:

I have several questions that arise from my analysis of the paper. First, could you provide more baselines and experiments to support your claim? Specifically, how does SPO compare to other state-of-the-art single-policy optimization methods, such as CISPO, and how does it compare to methods that use different forms of advantage estimation? This is crucial to understand the unique advantages and disadvantages of SPO. Second, could you provide more analysis to show the performance gain comes from the proposed global advantage normalization? Specifically, how does the global advantage normalization contribute to the improved performance compared to GRPO? This analysis could provide insights into why SPO outperforms GRPO and how the proposed normalization technique contributes to this improvement. Third, could you provide more analysis to show that SPO is more robust to degenerate groups? Specifically, how does SPO perform when a large portion of the generated samples are degenerate, and how does this compare to GRPO? This is crucial to validate the claim that SPO is more robust to such scenarios. Fourth, how does SPO perform on tasks that require more complex reasoning or planning? The current evaluation is limited to reasoning benchmarks, and it is unclear if the proposed algorithm can generalize to other types of tasks. Fifth, what are the limitations of SPO, and how can these limitations be addressed in future work? This is crucial to provide a more balanced and comprehensive view of the proposed algorithm and its potential impact. Finally, how does the choice of the KL-divergence threshold impact the performance of SPO across different tasks, and what are the guidelines for selecting appropriate values for different types of tasks? This is crucial to understand the sensitivity of SPO to hyperparameter settings.


## Rating:

4.0


## Confidence:

3.5


## Decision:

Reject
}