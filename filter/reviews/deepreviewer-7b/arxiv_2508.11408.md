I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper proposes a novel method named Chord, which aims to unify Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) for Large Language Models (LLMs). The authors identify a "shift-readapt-overfit" progression when utilizing off-policy data in SFT, where the model initially disrupts established patterns, then learns new patterns, and finally overfits, leading to performance degradation. Chord addresses this by reframing SFT as a dynamic weighted auxiliary objective within the RL process, introducing two key components: a global coefficient μ and a token-wise weighting function ϕ. The global coefficient μ balances the influence of SFT and RL, while ϕ selectively absorbs expert knowledge by down-weighting highly probable or improbable tokens. Experiments demonstrate that Chord achieves stable and efficient learning, outperforming traditional SFT-then-RL approaches across various tasks.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper introduces a novel dual-control mechanism that effectively integrates SFT and RL, providing a new perspective on how to combine these two post-training paradigms.
2. Chord is evaluated across a diverse set of tasks, including mathematical reasoning and tool-use, demonstrating its versatility and robustness.
3. The paper is well-structured, with clear explanations of the methodology and experimental setup, making it easy to follow and understand.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational overhead introduced by the dual-control mechanism. It would be beneficial to understand the trade-offs between performance gains and computational costs, especially in resource-constrained environments. Specifically, the paper lacks a breakdown of the computational cost associated with the token-wise weighting function, which could be a significant overhead, especially for longer sequences. A comparison of training time and memory usage with baseline methods is also missing.
2. The choice of the token-wise weighting function ϕ(⋅) seems somewhat arbitrary. While the authors provide empirical evidence for its effectiveness, a more theoretical justification or comparison with other weighting functions would strengthen the paper. The paper does not explore alternative weighting functions or provide a sensitivity analysis of the parameters within ϕ(⋅). It is unclear how the performance is affected by different parameter settings of the weighting function.
3. The paper does not thoroughly investigate the limitations of Chord, such as scenarios where it might fail or underperform. For example, it would be useful to explore the performance of Chord when the off-policy data is significantly different from the on-policy data or when the quality of the off-policy data is poor. The paper should also discuss the potential for bias in the off-policy data to affect the performance of Chord.
4. The paper could benefit from a more in-depth discussion of the hyperparameter tuning process for μ and ϕ(⋅). The paper lacks details on how these hyperparameters were selected and whether the performance is sensitive to these choices. A more detailed analysis of the hyperparameter sensitivity would be beneficial.

### Suggestions

The paper should include a more detailed analysis of the computational overhead introduced by the Chord method. This should include a breakdown of the time and memory costs associated with the token-wise weighting function, as well as a comparison of training time and memory usage with baseline methods. It would be beneficial to provide a table or graph that shows the training time and memory usage for Chord and the baseline methods, broken down by different stages of training. This analysis should also consider the impact of sequence length on the computational cost, as the token-wise weighting function could become more computationally expensive for longer sequences. Furthermore, the paper should explore techniques to reduce the computational overhead of the token-wise weighting function, such as using a more efficient implementation or approximating the weighting function.

The paper should provide a more thorough justification for the choice of the token-wise weighting function ϕ(⋅). This should include a theoretical analysis of why this particular function is effective and a comparison with other weighting functions. The paper should also explore alternative weighting functions and provide a sensitivity analysis of the parameters within ϕ(⋅). This analysis should include a discussion of how the performance is affected by different parameter settings of the weighting function. For example, the paper could explore the impact of using different activation functions or different ways of combining the global and local weighting factors. The paper should also provide a more detailed explanation of the intuition behind the design of the weighting function and how it relates to the learning dynamics of the model.

The paper should include a more thorough investigation of the limitations of Chord. This should include an analysis of the performance of Chord when the off-policy data is significantly different from the on-policy data or when the quality of the off-policy data is poor. The paper should also discuss the potential for bias in the off-policy data to affect the performance of Chord. For example, the paper could explore the performance of Chord when the off-policy data is generated by a model that is significantly different from the policy model. The paper should also discuss the potential for the Chord method to fail in certain scenarios and provide guidance on when it is appropriate to use this method. This analysis should also consider the impact of the quality of the off-policy data on the performance of Chord and provide recommendations on how to select high-quality off-policy data.

### Questions

1. How sensitive is Chord to the choice of hyperparameters, such as μ and the parameters within ϕ(⋅)? Could you provide a sensitivity analysis or guidelines for selecting these parameters in different scenarios?
2. How does Chord perform when the off-policy data is significantly different from the on-policy data, or when the quality of the off-policy data is poor?
3. Could you provide more details on the computational overhead introduced by the Chord method, especially the token-wise weighting function? How does the training time and memory usage of Chord compare to the baseline methods?

### Rating

6

### Confidence

3

**********

## Reviewer 2

### Summary

This paper proposes a novel method called Chord to unify SFT and RL. The authors first analyze the training dynamics of SFT, and find that the model initially disrupts established response patterns, then learns new patterns, and finally overfits. To address this, they introduce a dual-control mechanism, which consists of a global coefficient μ and a token-wise weighting function ϕ(⋅). The global coefficient μ controls the overall influence of expert data, and the token-wise weighting function ϕ(⋅) selectively absorbs expert knowledge by down-weighting highly probable or improbable tokens. Experiments demonstrate that Chord achieves stable and efficient learning, outperforming traditional SFT-then-RL approaches across various tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a thorough analysis of the training dynamics of SFT, and identify the "shift-readapt-overfit" progression, which is a novel and insightful finding.
3. The proposed Chord method is simple yet effective, and the dual-control mechanism is well-motivated and theoretically sound.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational overhead introduced by the dual-control mechanism. It would be beneficial to understand the trade-offs between performance gains and computational costs, especially in resource-constrained environments. Specifically, the paper lacks a breakdown of the computational cost associated with the token-wise weighting function, which could be a significant overhead, especially for longer sequences. A comparison of training time and memory usage with baseline methods is also missing.
2. The choice of the token-wise weighting function ϕ(⋅) seems somewhat arbitrary. While the authors provide empirical evidence for its effectiveness, a more theoretical justification or comparison with other weighting functions would strengthen the paper. The paper does not explore alternative weighting functions or provide a sensitivity analysis of the parameters within ϕ(⋅). It is unclear how the performance is affected by different parameter settings of the weighting function.
3. The paper does not thoroughly investigate the limitations of Chord, such as scenarios where it might fail or underperform. For example, it would be useful to explore the performance of Chord when the off-policy data is significantly different from the on-policy data or when the quality of the off-policy data is poor. The paper should also discuss the potential for bias in the off-policy data to affect the performance of Chord.
4. The paper could benefit from a more in-depth discussion of the hyperparameter tuning process for μ and ϕ(⋅). The paper lacks details on how these hyperparameters were selected and whether the performance is sensitive to these choices. A more detailed analysis of the hyperparameter sensitivity would be beneficial.

### Suggestions

The paper would benefit from a more rigorous analysis of the computational cost associated with the proposed Chord method. Specifically, a detailed breakdown of the time and memory requirements for the token-wise weighting function should be provided, including how these costs scale with sequence length. This analysis should be compared against the computational costs of the baseline methods, such as standard SFT and RL, to provide a clear understanding of the trade-offs involved. Furthermore, the authors should explore potential optimizations to reduce the computational overhead of the token-wise weighting function, such as using more efficient data structures or approximation techniques. This would make the method more practical for resource-constrained environments and larger models.

To strengthen the justification for the chosen token-wise weighting function, the authors should provide a more in-depth theoretical analysis of its properties. This analysis should explain why the specific form of the weighting function is effective in balancing exploration and exploitation. Additionally, the paper should include a comparison with alternative weighting functions, such as those based on entropy or variance of token probabilities. A sensitivity analysis of the parameters within the weighting function is also necessary to understand how the performance is affected by different parameter settings. This analysis should include a discussion of the optimal parameter values and their impact on the overall performance of the method. The authors should also explore the potential for adaptive parameter tuning to improve the robustness of the method.

Finally, the paper should include a more thorough investigation of the limitations of the Chord method. This should include an analysis of the performance of Chord when the off-policy data is significantly different from the on-policy data, or when the quality of the off-policy data is poor. The authors should also discuss the potential for bias in the off-policy data to affect the performance of Chord. Furthermore, a more detailed discussion of the hyperparameter tuning process for μ and ϕ(⋅) is needed. The paper should include details on how these hyperparameters were selected, and whether the performance is sensitive to these choices. A more detailed analysis of the hyperparameter sensitivity would be beneficial to ensure the robustness of the method.

### Questions

1. How does Chord perform when the off-policy data is significantly different from the on-policy data, or when the quality of the off-policy data is poor?
2. Could you provide more details on the hyperparameter tuning process for μ and ϕ(⋅)? How sensitive is the performance to these hyperparameters?
3. How does the computational overhead of Chord compare to the baseline methods?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper proposes a novel framework, Chord, that unifies SFT and RL by introducing a dual-control mechanism. The framework consists of two key components: a global coefficient μ and a token-wise weighting function ϕ(⋅). The global coefficient μ controls the overall influence of expert data, and the token-wise weighting function ϕ(⋅) selectively absorbs expert knowledge by down-weighting highly probable or improbable tokens. Experiments demonstrate that Chord achieves stable and efficient learning, outperforming traditional SFT-then-RL approaches across various tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a thorough analysis of the training dynamics of SFT, and identify the "shift-readapt-overfit" progression, which is a novel and insightful finding.
3. The proposed Chord method is simple yet effective, and the dual-control mechanism is well-motivated and theoretically sound.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational overhead introduced by the dual-control mechanism. It would be beneficial to understand the trade-offs between performance gains and computational costs, especially in resource-constrained environments. Specifically, the paper lacks a breakdown of the computational cost associated with the token-wise weighting function, which could be a significant overhead, especially for longer sequences. A comparison of training time and memory usage with baseline methods is also missing.
2. The choice of the token-wise weighting function ϕ(⋅) seems somewhat arbitrary. While the authors provide empirical evidence for its effectiveness, a more theoretical justification or comparison with other weighting functions would strengthen the paper. The paper does not explore alternative weighting functions or provide a sensitivity analysis of the parameters within ϕ(⋅). It is unclear how the performance is affected by different parameter settings of the weighting function.
3. The paper does not thoroughly investigate the limitations of Chord, such as scenarios where it might fail or underperform. For example, it would be useful to explore the performance of Chord when the off-policy data is significantly different from the on-policy data or when the quality of the off-policy data is poor. The paper should also discuss the potential for bias in the off-policy data to affect the performance of Chord.
4. The paper could benefit from a more in-depth discussion of the hyperparameter tuning process for μ and ϕ(⋅). The paper lacks details on how these hyperparameters were selected and whether the performance is sensitive to these choices. A more detailed analysis of the hyperparameter sensitivity would be beneficial.

### Suggestions

The paper would benefit from a more rigorous analysis of the computational cost associated with the proposed Chord method. Specifically, a detailed breakdown of the time and memory requirements for the token-wise weighting function should be provided, including how these costs scale with sequence length. This analysis should be compared against the computational costs of the baseline methods, such as standard SFT and RL, to provide a clear understanding of the trade-offs involved. Furthermore, the authors should explore potential optimizations to reduce the computational overhead of the token-wise weighting function, such as using more efficient data structures or approximation techniques. This would make the method more practical for resource-constrained environments and larger models. Without this analysis, it is difficult to assess the practical applicability of the proposed method.

To strengthen the justification for the chosen token-wise weighting function, the authors should provide a more in-depth theoretical analysis of its properties. This analysis should explain why the specific form of the weighting function is effective in balancing exploration and exploitation. Additionally, the paper should include a comparison with alternative weighting functions, such as those based on entropy or variance of token probabilities. A sensitivity analysis of the parameters within the weighting function is also necessary to understand how the performance is affected by different parameter settings. This analysis should include a discussion of the optimal parameter values and their impact on the overall performance of the method. The authors should also explore the potential for adaptive parameter tuning to improve the robustness of the method. Without a more thorough justification and analysis, the choice of the weighting function appears somewhat arbitrary.

Finally, the paper should include a more thorough investigation of the limitations of the Chord method. This should include an analysis of the performance of Chord when the off-policy data is significantly different from the on-policy data, or when the quality of the off-policy data is poor. The authors should also discuss the potential for bias in the off-policy data to affect the performance of Chord. Furthermore, a more detailed discussion of the hyperparameter tuning process for μ and ϕ(⋅) is needed. The paper should include details on how these hyperparameters were selected, and whether the performance is sensitive to these choices. A more detailed analysis of the hyperparameter sensitivity would be beneficial to ensure the robustness of the method. Without this analysis, it is difficult to assess the generalizability of the proposed method.

### Questions

Please refer to the weakness.

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

This paper presents a new method for combining SFT and RL for LLMs. The authors observe that SFT-then-RL can suffer from a "shift-readapt-overfit" pattern, where the model initially disrupts established patterns, then learns new patterns, and finally overfits. The authors propose a new method that combines SFT and RL via a weighted combination of the RL and SFT losses, with the weights being determined by a global coefficient and a token-wise weighting function. Experiments show that this method outperforms SFT-then-RL and other baselines on a variety of tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple yet effective, and the authors provide a thorough analysis of the training dynamics of SFT, which is insightful.
- The experiments are comprehensive and demonstrate the effectiveness of the proposed method across a variety of tasks.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational overhead introduced by the dual-control mechanism. It would be beneficial to understand the trade-offs between performance gains and computational costs, especially in resource-constrained environments. Specifically, the paper lacks a breakdown of the computational cost associated with the token-wise weighting function, which could be a significant overhead, especially for longer sequences. A comparison of training time and memory usage with baseline methods is also missing.
- The choice of the token-wise weighting function ϕ(⋅) seems somewhat arbitrary. While the authors provide empirical evidence for its effectiveness, a more theoretical justification or comparison with other weighting functions would strengthen the paper. The paper does not explore alternative weighting functions or provide a sensitivity analysis of the parameters within ϕ(⋅). It is unclear how the performance is affected by different parameter settings of the weighting function.
- The paper does not thoroughly investigate the limitations of Chord, such as scenarios where it might fail or underperform. For example, it would be useful to explore the performance of Chord when the off-policy data is significantly different from the on-policy data or when the quality of the off-policy data is poor. The paper should also discuss the potential for bias in the off-policy data to affect the performance of Chord.
- The paper could benefit from a more in-depth discussion of the hyperparameter tuning process for μ and ϕ(⋅). The paper lacks details on how these hyperparameters were selected and whether the performance is sensitive to these choices. A more detailed analysis of the hyperparameter sensitivity would be beneficial.

### Suggestions

The paper would benefit from a more rigorous analysis of the computational cost associated with the proposed Chord method. Specifically, a detailed breakdown of the time and memory requirements for the token-wise weighting function should be provided, including how these costs scale with sequence length. This analysis should be compared against the computational costs of the baseline methods, such as standard SFT and RL, to provide a clear understanding of the trade-offs involved. Furthermore, the authors should explore potential optimizations to reduce the computational overhead of the token-wise weighting function, such as using more efficient data structures or approximation techniques. This would make the method more practical for resource-constrained environments and larger models. Without this analysis, it is difficult to assess the practical applicability of the proposed method.

To strengthen the justification for the chosen token-wise weighting function, the authors should provide a more in-depth theoretical analysis of its properties. This analysis should explain why the specific form of the weighting function is effective in balancing exploration and exploitation. Additionally, the paper should include a comparison with alternative weighting functions, such as those based on entropy or variance of token probabilities. A sensitivity analysis of the parameters within the weighting function is also necessary to understand how the performance is affected by different parameter settings. This analysis should include a discussion of the optimal parameter values and their impact on the overall performance of the method. The authors should also explore the potential for adaptive parameter tuning to improve the robustness of the method. Without a more thorough justification and analysis, the choice of the weighting function appears somewhat arbitrary.

Finally, the paper should include a more thorough investigation of the limitations of the Chord method. This should include an analysis of the performance of Chord when the off-policy data is significantly different from the on-policy data, or when the quality of the off-policy data is poor. The authors should also discuss the potential for bias in the off-policy data to affect the performance of Chord. Furthermore, a more detailed discussion of the hyperparameter tuning process for μ and ϕ(⋅) is needed. The paper should include details on how these hyperparameters were selected, and whether the performance is sensitive to these choices. A more detailed analysis of the hyperparameter sensitivity would be beneficial to ensure the robustness of the method. Without this analysis, it is difficult to assess the generalizability of the proposed method.

### Questions

- How does the computational overhead of the token-wise weighting function compare to the baseline methods?
- How sensitive is the performance of Chord to the choice of hyperparameters, such as μ and the parameters within ϕ(⋅)?
- How does Chord perform when the off-policy data is significantly different from the on-policy data, or when the quality of the off-policy data is poor?

### Rating

6

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in a given paper. I need to go through each reviewer's comments and check if their criticisms are valid based on the content of the paper.

For each weakness, I will:
1. **State the weakness** as quoted from the review.
2. **Collect evidence** from the paper to support or refute the weakness. This will involve looking at the method description, experimental setup, results, and related work.
3. **Analyze literature gaps** by checking if the paper misses relevant citations or baseline comparisons.
4. **Provide a validation analysis** summarizing the evidence and its impact.
5. **Conclude** whether the weakness is valid, partially valid, or invalid, and state my confidence level.

Let's start with Reviewer 1.
**Review 1 Weaknesses Validation:**

1. Weakness Statement:
[The paper does not provide a detailed analysis of the computational overhead introduced by the dual-control mechanism. It would be beneficial to understand the trade-offs between performance gains and computational costs, especially in resource-constrained environments. Specifically, the paper lacks a breakdown of the computational cost associated with the token-wise weighting function, which could be a significant overhead, especially for longer sequences. A comparison of training time and memory usage with baseline methods is also missing.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper describes the token-wise weighting function as $\phi(y_t^*) = p_t^*(1 - p_t)$ (Method, Details, Token-wise Weighting Function).
   - The paper mentions the use of the GPT-4 scoring function for the token-wise weighting function (Experiments, Setup, Metrics).
   - There is no explicit mention of the computational cost of calculating these probabilities or the GPT-4 scoring function.

b) Experiment-related Evidence:
   - The paper reports performance metrics (accuracy, reward, entropy, KL divergence) but does not include training time, memory usage, or computational cost comparisons with baselines.

3. Literature Gap Analysis:
   - The paper does not cite works that specifically analyze the computational cost of token-wise operations or the use of LLMs for scoring in RL contexts.

4. Validation Analysis:
   - The reviewer correctly points out the absence of a detailed computational overhead analysis. The paper focuses on the effectiveness of the method in terms of performance metrics but does not delve into the computational resources required. The token-wise weighting function, involving probability calculations and potentially LLM calls (GPT-4), could indeed be computationally expensive, especially for longer sequences. The lack of training time and memory comparisons makes it difficult to assess the practical applicability of Chord in resource-constrained settings.

5. Conclusion:
   - Validity status: **Valid**
   - Confidence level: **High**
   - Key supporting evidence: The paper lacks any discussion or experimental results related to training time, memory usage, or computational cost analysis.

1. Weakness Statement:
[The choice of the token-wise weighting function ϕ(⋅) seems somewhat arbitrary. While the authors provide empirical evidence for its effectiveness, a more theoretical justification or comparison with other weighting functions would strengthen the paper. The paper does not explore alternative weighting functions or provide a sensitivity analysis of the parameters within ϕ(⋅). It is unclear how the performance is affected by different parameter settings of the weighting function.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper introduces the token-wise weighting function as $\phi(y_t^*) = p_t^*(1 - p_t)$ (Method, Details, Token-wise Weighting Function).
   - The paper mentions that the SFT objective function is designed to prevent disruption and reinforcement of established patterns (Method, Details, Token-wise Weighting Function).
   - The paper does not provide a theoretical justification for the specific form of $\phi(y_t^*)$.

b) Experiment-related Evidence:
   - The paper includes an ablation study comparing Chord-$\mu$ and Chord-$\phi$ (Experiments, Results, Analysis, Dynamic $\mu$ Versus Fixed $\mu$).
   - The paper does not include experiments comparing Chord-$\phi$ with other weighting functions.
   - The paper does not present a sensitivity analysis of the parameters within $\phi(y_t^*)$.

3. Literature Gap Analysis:
   - The paper does not cite works that explore different weighting functions for combining SFT and RL losses in similar contexts.

4. Validation Analysis:
   - The reviewer's criticism is valid. While the paper provides empirical evidence for the effectiveness of the chosen weighting function, it lacks a theoretical justification for its specific form. The absence of comparisons with alternative weighting functions and a sensitivity analysis weakens the argument for the optimality or even the superiority of the chosen function.

5. Conclusion:
   - Validity status: **Valid**
   - Confidence level: **High**
   - Key supporting evidence: The paper lacks theoretical justification, comparisons with other weighting functions, and sensitivity analysis for the chosen token-wise weighting function.

1. Weakness Statement:
[The paper does not thoroughly investigate the limitations of Chord, such as scenarios where it might fail or underperform. For example, it would be useful to explore the performance of Chord when the off-policy data is significantly different from the on-policy data or when the quality of the off-policy data is poor. The paper should also discuss the potential for bias in the off-policy data to affect the performance of Chord.]

2. Evidence Collection:
a) Experiment-related Evidence:
   - The paper includes experiments with different expert sources (Mathematical Reasoning, Tool-use) and different quality of expert data (strong vs. weaker models) (Experiments, Setup, Datasets, Baselines).
   - The paper shows that Chord-$\phi$ performs well even with weaker expert models (Experiments, Results, Analysis, Varying Expert Data Source).
   - The paper does not explicitly discuss scenarios where Chord might fail or underperform, such as with significantly different off-policy data.

3. Literature Gap Analysis:
   - The paper does not cite works that specifically analyze the limitations of combining SFT and RL with varying quality or relevance of off-policy data.

4. Validation Analysis:
   - The reviewer's point is partially valid. The paper does explore the impact of different expert data sources and qualities, showing robustness in some cases. However, it doesn't delve into scenarios where the off-policy data is *significantly* different from the on-policy data, nor does it explicitly discuss potential biases in the off-policy data and their impact.

5. Conclusion:
   - Validity status: **Partially Valid**
   - Confidence level: **Medium**
   - Key supporting evidence: The paper explores some limitations related to expert data quality but lacks analysis of significantly different data and explicit discussion of bias.

1. Weakness Statement:
[The paper could benefit from a more in-depth discussion of the hyperparameter tuning process for μ and ϕ(⋅). The paper lacks details on how these hyperparameters were selected and whether the performance is sensitive to these choices. A more detailed analysis of the hyperparameter sensitivity would be beneficial.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper introduces $\mu$ as a hyperparameter controlling the overall influence of expert data (Method, Details, The Shift-Readapt-Overfit Progression).
   - The paper introduces $\phi(y_t^*) = p_t^*(1 - p_t)$ as the token-wise weighting function (Method, Details, Token-wise Weighting Function).
   - The paper mentions that $\mu$ is dynamically adjusted in the experiments (Method, Details, The Shift-Readapt-Overfit Progression).

b) Experiment-related Evidence:
   - The paper mentions using a decay schedule for $\mu$ (Experiments, Setup, Hyperparameters).
   - The paper does not explicitly detail the range of values explored for $\mu$ or $\phi(y_t^*)$ during hyperparameter tuning.
   - The paper does not include a sensitivity analysis of $\mu$ and $\phi(y_t^*)$.

3. Literature Gap Analysis:
   - The paper does not cite works that specifically detail hyperparameter tuning strategies for similar methods combining SFT and RL.

4. Validation Analysis:
   - The reviewer's criticism is valid. The paper lacks a detailed discussion of the hyperparameter tuning process for $\mu$ and $\phi(y_t^*)$. It doesn't specify the search space, the optimization method used, or the sensitivity of the results to these hyperparameters.

5. Conclusion:
   - Validity status: **Valid**
   - Confidence level: **High**
   - Key supporting evidence: The paper lacks details on the hyperparameter tuning process, the range of values explored, and a sensitivity analysis.

**Review 2 Weaknesses Validation:**

1. Weakness Statement:
[The paper does not provide a detailed analysis of the computational overhead introduced by the dual-control mechanism. It would be beneficial to understand the trade-offs between performance gains and computational costs, especially in resource-constrained environments. Specifically, the paper lacks a breakdown of the computational cost associated with the token-wise weighting function, which could be a significant overhead, especially for longer sequences. A comparison of training time and memory usage with baseline methods is also missing.]

2. Evidence Collection:
   - This is the same weakness as Reviewer 1, Weakness 1. Please refer to the validation for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1, Weakness 1.

4. Validation Analysis:
   - Same as Reviewer 1, Weakness 1.

5. Conclusion:
   - Validity status: **Valid**
   - Confidence level: **High**
   - Key supporting evidence: Same as Reviewer 1, Weakness 1.

1. Weakness Statement:
[The choice of the token-wise weighting function ϕ(⋅) seems somewhat arbitrary. While the authors provide empirical evidence for its effectiveness, a more theoretical justification or comparison with other weighting functions would strengthen the paper. The paper does not explore alternative weighting functions or provide a sensitivity analysis of the parameters within ϕ(⋅). It is unclear how the performance is affected by different parameter settings of the weighting function.]

2. Evidence Collection:
   - This is the same weakness as Reviewer 1, Weakness 2. Please refer to the validation for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1, Weakness 2.

4. Validation Analysis:
   - Same as Reviewer 1, Weakness 2.

5. Conclusion:
   - Validity status: **Valid**
   - Confidence level: **High**
   - Key supporting evidence: Same as Reviewer 1, Weakness 2.

1. Weakness Statement:
[The paper does not thoroughly investigate the limitations of Chord, such as scenarios where it might fail or underperform. For example, it would be useful to explore the performance of Chord when the off-policy data is significantly different from the on-policy data or when the quality of the off-policy data is poor. The paper should also discuss the potential for bias in the off-policy data to affect the performance of Chord.]

2. Evidence Collection:
   - This is the same weakness as Reviewer 1, Weakness 3. Please refer to the validation for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1, Weakness 3.

4. Validation Analysis:
   - Same as Reviewer 1, Weakness 3.

5. Conclusion:
   - Validity status: **Partially Valid**
   - Confidence level: **Medium**
   - Key supporting evidence: Same as Reviewer 1, Weakness 3.

1. Weakness Statement:
[The paper could benefit from a more in-depth discussion of the hyperparameter tuning process for μ and ϕ(⋅). The paper lacks details on how these hyperparameters were selected and whether the performance is sensitive to these choices. A more detailed analysis of the hyperparameter sensitivity would be beneficial.]

2. Evidence Collection:
   - This is the same weakness as Reviewer 1, Weakness 4. Please refer to the validation for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1, Weakness 4.

4. Validation Analysis:
   - Same as Reviewer 1, Weakness 4.

5. Conclusion:
   - Validity status: **Valid**
   - Confidence level: **High**
   - Key supporting evidence: Same as Reviewer 1, Weakness 4.

**Review 3 Weaknesses Validation:**

1. Weakness Statement:
[The paper does not provide a detailed analysis of the computational overhead introduced by the dual-control mechanism. It would be beneficial to understand the trade-offs between performance gains and computational costs, especially in resource-constrained environments. Specifically, the paper lacks a breakdown of the computational cost associated with the token-wise weighting function, which could be a significant overhead, especially for longer sequences. A comparison of training time and memory usage with baseline methods is also missing.]

2. Evidence Collection:
   - This is the same weakness as Reviewer 1, Weakness 1 and Reviewer 2, Weakness 1. Please refer to the validation for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1, Weakness 1.

4. Validation Analysis:
   - Same as Reviewer 1, Weakness 1.

5. Conclusion:
   - Validity status: **Valid**
   - Confidence level: **High**
   - Key supporting evidence: Same as Reviewer 1, Weakness 1.

1. Weakness Statement:
[The choice of the token-wise weighting function ϕ(⋅) seems somewhat arbitrary. While the authors provide empirical evidence for its effectiveness, a more theoretical justification or comparison with other weighting functions would strengthen the paper. The paper does not explore alternative weighting functions or provide a sensitivity analysis of the parameters within ϕ(⋅). It is unclear how the performance is affected by different parameter settings of the weighting function.]

2. Evidence Collection:
   - This is the same weakness as Reviewer 1, Weakness 2 and Reviewer 2, Weakness 2. Please refer to the validation for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1, Weakness 2.

4. Validation Analysis:
   - Same as Reviewer 1, Weakness 2.

5. Conclusion:
   - Validity status: **Valid**
   - Confidence level: **High**
   - Key supporting evidence: Same as Reviewer 1, Weakness 2.

1. Weakness Statement:
[The paper does not thoroughly investigate the limitations of Chord, such as scenarios where it might fail or underperform. For example, it would be useful to explore the performance of Chord when the off-policy data is significantly different from the on-policy data or when the quality of the off-policy data is poor. The paper should also discuss the potential for bias in the off-policy data to affect the performance of Chord.]

2. Evidence Collection:
   - This is the same weakness as Reviewer 1, Weakness 3 and Reviewer 2, Weakness 3. Please refer to the validation for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1, Weakness 3.

4. Validation Analysis:
   - Same as Reviewer 1, Weakness 3.

5. Conclusion:
   - Validity status: **Partially Valid**
   - Confidence level: **Medium**
   - Key supporting evidence: Same as Reviewer 1, Weakness 3.

1. Weakness Statement:
[The paper could benefit from a more in-depth discussion of the hyperparameter tuning process for μ and ϕ(⋅). The paper lacks details on how these hyperparameters were selected and whether the performance is sensitive to these choices. A more detailed analysis of the hyperparameter sensitivity would be beneficial.]

2. Evidence Collection:
   - This is the same weakness as Reviewer 1, Weakness 4 and Reviewer 2, Weakness 4. Please refer to the validation for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1, Weakness 4.

4. Validation Analysis:
   - Same as Reviewer 1, Weakness 4.

5. Conclusion:
   - Validity status: **Valid**
   - Confidence level: **High**
   - Key supporting evidence: Same as Reviewer 1, Weakness 4.

**Review 4 Weaknesses Validation:**

1. Weakness Statement:
[The paper does not provide a detailed analysis of the computational overhead introduced by the dual-control mechanism. It would be beneficial to understand the trade-offs between performance gains and computational costs, especially in resource-constrained environments. Specifically, the paper lacks a breakdown of the computational cost associated with the token-wise weighting function, which could be a significant overhead, especially for longer sequences. A comparison of training time and memory usage with baseline methods is also missing.]

2. Evidence Collection:
   - This is the same weakness as Reviewer 1, Weakness 1, Reviewer 2, Weakness 1, and Reviewer 3, Weakness 1. Please refer to the validation for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1, Weakness 1.

4. Validation Analysis:
   - Same as Reviewer 1, Weakness 1.

5. Conclusion:
   - Validity status: **Valid**
   - Confidence level: **High**
   - Key supporting evidence: Same as Reviewer 1, Weakness 1.

1. Weakness Statement:
[The choice of the token-wise weighting function ϕ(⋅) seems somewhat arbitrary. While the authors provide empirical evidence for its effectiveness, a more theoretical justification or comparison with other weighting functions would strengthen the paper. The paper does not explore alternative weighting functions or provide a sensitivity analysis of the parameters within ϕ(⋅). It is unclear how the performance is affected by different parameter settings of the weighting function.]

2. Evidence Collection:
   - This is the same weakness as Reviewer 1, Weakness 2, Reviewer 2, Weakness 2, and Reviewer 3, Weakness 2. Please refer to the validation for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1, Weakness 2.

4. Validation Analysis:
   - Same as Reviewer 1, Weakness 2.

5. Conclusion:
   - Validity status: **Valid**
   - Confidence level: **High**
   - Key supporting evidence: Same as Reviewer 1, Weakness 2.

1. Weakness Statement:
[The paper does not thoroughly investigate the limitations of Chord, such as scenarios where it might fail or underperform. For example, it would be useful to explore the performance of Chord when the off-policy data is significantly different from the on-policy data or when the quality of the off-policy data is poor. The paper should also discuss the potential for bias in the off-policy data to affect the performance of Chord.]

2. Evidence Collection:
   - This is the same weakness as Reviewer 1, Weakness 3, Reviewer 2, Weakness 3, and Reviewer 3, Weakness 3. Please refer to the validation for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1, Weakness 3.

4. Validation Analysis:
   - Same as Reviewer 1, Weakness 3.

5. Conclusion:
   - Validity status: **Partially Valid**
   - Confidence level: **Medium**
   - Key supporting evidence: Same as Reviewer 1, Weakness 3.

1. Weakness Statement:
[The paper could benefit from a more in-depth discussion of the hyperparameter tuning process for μ and ϕ(⋅). The paper lacks details on how these hyperparameters were selected and whether the performance is sensitive to these choices. A more detailed analysis of the hyperparameter sensitivity would be beneficial.]

2. Evidence Collection:
   - This is the same weakness as Reviewer 1, Weakness 4, Reviewer 2, Weakness 4, and Reviewer 3, Weakness 4. Please refer to the validation for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1, Weakness 4.

4. Validation Analysis:
   - Same as Reviewer 1, Weakness 4.

5. Conclusion:
   - Validity status: **Valid**
   - Confidence level: **High**
   - Key supporting evidence: Same as Reviewer 1, Weakness 4.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces Chord, a novel framework designed to unify Supervised Fine-Tuning (SFT) and Reinforcement Learning from Human Feedback (RLHF) for large language models (LLMs). The authors identify a 'shift-readapt-overfit' progression during SFT, where the model initially disrupts established patterns, then learns new ones, and finally overfits. To address this, Chord proposes a dual-control mechanism that dynamically adjusts the influence of SFT and RL objectives. This is achieved through a global coefficient, μ, which balances the overall impact of expert data, and a token-wise weighting function, ϕ(⋅), which selectively absorbs expert knowledge by down-weighting highly probable or improbable tokens. The core idea is to provide a more stable and efficient learning process by integrating SFT and RL in a unified framework. The authors evaluate Chord across a diverse set of tasks, including mathematical reasoning and tool-use, demonstrating its effectiveness compared to traditional SFT-then-RL approaches. The experimental results show that Chord achieves stable and efficient learning, outperforming baseline methods in various tasks. The paper also includes an ablation study comparing Chord with and without the token-wise weighting function, further validating its contribution. The authors analyze the training dynamics of SFT, identifying the 'shift-readapt-overfit' pattern, which is a key insight that motivates their approach. The paper's main contribution lies in the introduction of a dual-control mechanism that effectively integrates SFT and RL, providing a new perspective on how to combine these two post-training paradigms. The authors' analysis of the SFT training dynamics and their proposed solution are both novel and insightful, offering a promising direction for future research in this area. The empirical results demonstrate the effectiveness of the proposed method, showing that it can achieve better performance than traditional SFT-then-RL approaches across a variety of tasks. Overall, the paper presents a well-motivated and well-executed study that makes a significant contribution to the field of LLM post-training.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

2.75


## Strengths:

I found several aspects of this paper to be particularly strong. First, the paper introduces a novel dual-control mechanism that effectively integrates SFT and RL, providing a new perspective on how to combine these two post-training paradigms. This approach is both theoretically sound and empirically effective, as demonstrated by the experimental results. The idea of using a global coefficient, μ, to control the overall influence of expert data, and a token-wise weighting function, ϕ(⋅), to selectively absorb expert knowledge, is well-motivated and intuitively appealing. The authors' analysis of the training dynamics of SFT, identifying the 'shift-readapt-overfit' pattern, is a significant contribution in itself. This analysis provides valuable insights into the behavior of SFT models and motivates the proposed solution. The paper is also well-written and easy to follow, making it accessible to a broad audience. The authors provide a thorough explanation of the methodology and experimental setup, which allows for a clear understanding of their approach. The experimental results are comprehensive and demonstrate the effectiveness of Chord across a variety of tasks, including mathematical reasoning and tool-use. The ablation study comparing Chord with and without the token-wise weighting function further validates the contribution of this component. The paper's focus on unifying SFT and RL is a significant step towards developing more robust and efficient post-training methods for LLMs. The authors' approach of dynamically adjusting the influence of SFT and RL objectives is a promising direction for future research in this area. The paper's overall contribution lies in its novel approach to combining SFT and RL, its insightful analysis of SFT training dynamics, and its strong empirical results. The authors have successfully demonstrated the effectiveness of their proposed method, and the paper makes a valuable contribution to the field.


## Weaknesses:

Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. A primary concern is the lack of a detailed analysis of the computational overhead introduced by the proposed Chord method. While the paper demonstrates the effectiveness of the method in terms of performance metrics, it does not provide a thorough analysis of the computational costs associated with the token-wise weighting function, particularly in comparison to baseline methods. The token-wise weighting function, which involves calculating probabilities and potentially using LLMs for scoring, could be computationally expensive, especially for longer sequences. The absence of a breakdown of the time and memory requirements for this step makes it difficult to assess the practical applicability of Chord in resource-constrained environments. Furthermore, the paper does not include training time or memory usage comparisons with baseline methods, which is a critical omission. This lack of analysis makes it difficult to determine the trade-offs between performance gains and computational costs, especially in resource-constrained environments. My confidence in this weakness is high, as the paper lacks any discussion or experimental results related to training time, memory usage, or computational cost analysis. 

Another significant weakness is the somewhat arbitrary choice of the token-wise weighting function, ϕ(⋅). While the authors provide empirical evidence for its effectiveness, they do not offer a theoretical justification for its specific form. The paper introduces the function as ϕ(y_t*) = p_t*(1 - p_t), where p_t is the probability of the token at time t. While this form is motivated by the idea of down-weighting highly probable or improbable tokens, the authors do not provide a deeper theoretical analysis of why this particular function is effective in balancing exploration and exploitation. The absence of a theoretical justification for the specific form of the weighting function appears to be a significant limitation. Furthermore, the paper does not explore alternative weighting functions or provide a sensitivity analysis of the parameters within ϕ(⋅). It is unclear how the performance is affected by different parameter settings of the weighting function. The lack of comparison with alternative weighting functions and the absence of a sensitivity analysis weaken the argument for the optimality or even the superiority of the chosen function. My confidence in this weakness is also high, as the paper lacks any theoretical justification, comparisons with other weighting functions, and sensitivity analysis for the chosen token-wise weighting function. 

Additionally, the paper does not thoroughly investigate the limitations of Chord, such as scenarios where it might fail or underperform. While the paper explores the impact of different expert data sources and qualities, it does not delve into scenarios where the off-policy data is *significantly* different from the on-policy data. The paper also does not explicitly discuss potential biases in the off-policy data and their impact on the performance of Chord. The paper should also explore the performance of Chord when the off-policy data is significantly different from the on-policy data, or when the quality of the off-policy data is poor. The authors should also discuss the potential for bias in the off-policy data to affect the performance of Chord. Furthermore, the paper does not provide a detailed discussion of the hyperparameter tuning process for μ and ϕ(⋅). It doesn't specify the search space, the optimization method used, or the sensitivity of the results to these hyperparameters. A more detailed analysis of the hyperparameter sensitivity would be beneficial to ensure the robustness of the method. My confidence in this weakness is medium, as the paper explores some limitations related to expert data quality but lacks analysis of significantly different data and explicit discussion of bias. The paper also lacks details on the hyperparameter tuning process, the range of values explored, and a sensitivity analysis.


Finally, while the paper presents a novel approach to combining SFT and RL, it lacks a detailed discussion of the hyperparameter tuning process for μ and ϕ(⋅). The paper mentions using a decay schedule for μ (Method, Details, The Shift-Readapt-Overfit Progression) but does not specify the range of values explored for μ or ϕ(⋅) during hyperparameter tuning. The paper also does not include a sensitivity analysis of μ and ϕ(⋅). It is unclear how the performance is affected by different parameter settings of the weighting function. This lack of detail makes it difficult to assess the robustness of the method and to reproduce the results. My confidence in this weakness is high, as the paper lacks details on the hyperparameter tuning process, the range of values explored, and a sensitivity analysis.


In summary, while the paper presents a novel and promising approach, the lack of analysis of computational overhead, the somewhat arbitrary choice of the token-wise weighting function, the limited investigation of limitations, and the lack of detail on hyperparameter tuning are significant weaknesses that need to be addressed.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the paper should include a more rigorous analysis of the computational cost associated with the proposed Chord method. This should include a detailed breakdown of the time and memory requirements for the token-wise weighting function, including how these costs scale with sequence length. This analysis should be compared against the computational costs of the baseline methods, such as standard SFT and RL, to provide a clear understanding of the trade-offs involved. Furthermore, the authors should explore potential optimizations to reduce the computational overhead of the token-wise weighting function, such as using more efficient data structures or approximation techniques. This would make the method more practical for resource-constrained environments and larger models. Without this analysis, it is difficult to assess the practical applicability of the proposed method. 

Second, the paper should provide a more in-depth theoretical analysis of the chosen token-wise weighting function, ϕ(⋅). This analysis should explain why the specific form of the weighting function is effective in balancing exploration and exploitation. Additionally, the paper should include a comparison with alternative weighting functions, such as those based on entropy or variance of token probabilities. A sensitivity analysis of the parameters within the weighting function is also necessary to understand how the performance is affected by different parameter settings. This analysis should include a discussion of the optimal parameter values and their impact on the overall performance of the method. The authors should also explore the potential for adaptive parameter tuning to improve the robustness of the method. Without a more thorough justification and analysis, the choice of the weighting function appears somewhat arbitrary. 

Third, the paper should include a more thorough investigation of the limitations of Chord. This should include an analysis of the performance of Chord when the off-policy data is significantly different from the on-policy data, or when the quality of the off-policy data is poor. The authors should also discuss the potential for bias in the off-policy data to affect the performance of Chord. Furthermore, a more detailed discussion of the hyperparameter tuning process for μ and ϕ(⋅) is needed. The paper should include details on how these hyperparameters were selected, and whether the performance is sensitive to these choices. A more detailed analysis of the hyperparameter sensitivity would be beneficial to ensure the robustness of the method. 

Finally, the paper should include a more detailed discussion of the hyperparameter tuning process for μ and ϕ(⋅). The paper should include details on how these hyperparameters were selected, and whether the performance is sensitive to these choices. A more detailed analysis of the hyperparameter sensitivity would be beneficial to ensure the robustness of the method. Without this analysis, it is difficult to assess the generalizability of the proposed method. 

In summary, the paper would benefit from a more rigorous analysis of the computational cost, a more thorough justification for the chosen token-wise weighting function, a more detailed investigation of the limitations, and a more detailed discussion of the hyperparameter tuning process. These improvements would significantly strengthen the paper and enhance its impact on the field.


## Questions:

I have several questions that arise from my analysis of this paper. First, how does the computational overhead of Chord compare to the baseline methods, specifically in terms of training time and memory usage? The paper does not provide a detailed analysis of these aspects, and it would be valuable to understand the trade-offs between performance gains and computational costs. Second, how sensitive is Chord to the choice of hyperparameters, such as μ and the parameters within the token-wise weighting function, ϕ(⋅)? The paper lacks details on the hyperparameter tuning process and a sensitivity analysis, and it would be important to understand how the performance is affected by different parameter settings. Third, how does Chord perform when the off-policy data is significantly different from the on-policy data, or when the quality of the off-policy data is poor? The paper explores some limitations related to expert data quality but lacks analysis of significantly different data and explicit discussion of bias. Fourth, could you provide more details on the hyperparameter tuning process for μ and ϕ(⋅)? How sensitive is the performance to these hyperparameters? A more detailed analysis of the hyperparameter sensitivity would be beneficial to ensure the robustness of the method. Fifth, how does Chord perform when the off-policy data is significantly different from the on-policy data, or when the quality of the off-policy data is poor? The paper should also discuss the potential for bias in the off-policy data to affect the performance of Chord. Finally, could you provide more details on the computational overhead introduced by the token-wise weighting function, especially the GPT-4 scoring used? How does the training time and memory usage of Chord compare to the baseline methods? These questions are crucial for understanding the practical applicability and robustness of the proposed method.


## Rating:

6.0


## Confidence:

3.0


## Decision:

Accept
}