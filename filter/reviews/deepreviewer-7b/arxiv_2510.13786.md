I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper presents a principled study on scaling RLHF for LLMs, introducing a sigmoidal curve to predict RLHF scaling, inspired by the scaling laws in pre-training. The authors fit this curve to the validation performance of RLHF across different compute budgets, revealing two key parameters: the asymptotic performance ceiling and the compute efficiency. Through extensive experiments, they identify three principles governing RLHF scaling: (1) different recipes yield different ceilings on performance, (2) RLHF performance plateaus after a certain point, and (3) scaling efficiency improves with larger batch sizes. Based on these insights, they propose a best-practice recipe, ScaleRL, and demonstrate its effectiveness by scaling up to 100,000 GPU hours, achieving state-of-the-art performance and predictability in scaling.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper introduces a novel sigmoidal scaling curve for RLHF, providing a predictive framework for scaling analysis.
- The study is comprehensive, covering a wide range of design choices and providing valuable insights into RLHF scaling.
- The proposed ScaleRL recipe is well-validated, achieving state-of-the-art performance and predictability in scaling.

### Weaknesses

#### Some Related Works


#### comment

 - The paper is primarily empirical, focusing on the empirical study of RLHF scaling without proposing new algorithmic or theoretical innovations. While the empirical findings are valuable, the lack of theoretical depth limits the paper's contribution to the broader machine learning community.
- The paper's scope is limited to RLHF, and it does not explore other RL training paradigms, such as PPO. This narrow focus restricts the generalizability of the findings and the applicability of the proposed scaling laws to other RL methods.
- The paper does not provide a detailed analysis of the impact of different reward structures on the scaling behavior of RLHF. Given that the reward model plays a crucial role in RLHF, understanding how different reward models affect scaling is essential for practical applications.
- The paper does not explore the impact of different reward model architectures on the scaling behavior of RLHF. Given that the reward model plays a crucial role in RLHF, understanding how different reward models affect scaling is essential for practical applications.

### Suggestions

The paper would benefit significantly from a more in-depth theoretical analysis of the proposed sigmoidal scaling curve. While the empirical validation is strong, a theoretical justification for why this specific functional form is appropriate for modeling RLHF scaling would greatly enhance the paper's contribution. This could involve exploring connections to existing theoretical frameworks in machine learning or developing a novel theoretical argument to support the use of the sigmoidal curve. Furthermore, the authors should investigate the limitations of the sigmoidal curve and discuss scenarios where it might not accurately capture the scaling behavior of RLHF. This would provide a more nuanced understanding of the applicability of the proposed framework.

To broaden the scope of the paper, the authors should investigate the scaling behavior of other RL algorithms beyond RLHF. This would involve conducting experiments with algorithms like PPO and comparing their scaling properties with those of RLHF. Such an analysis would help determine whether the observed principles of scaling are universal across different RL methods or specific to RLHF. Additionally, the authors should explore the impact of different reward structures on the scaling behavior of RLHF. This could involve experimenting with different reward models, including those with varying levels of complexity and training data. A detailed analysis of how these reward models affect the scaling curve would provide valuable insights for practitioners. The authors should also consider the impact of different reward model architectures, such as transformer-based models versus simpler MLPs, on the overall scaling behavior.

Finally, the paper should address the potential for reward hacking, especially in the context of long-context reasoning tasks. While the authors acknowledge this issue, they do not provide a detailed analysis of its impact on the scaling behavior of RLHF. This analysis should include experiments with different reward models and training strategies to determine the extent to which reward hacking affects the scaling curve. The authors should also discuss potential mitigation strategies for reward hacking, such as using more robust reward models or incorporating techniques like adversarial training. A thorough investigation of reward hacking is crucial for ensuring the reliability and robustness of RLHF scaling.

### Questions

- Could the authors provide a more detailed explanation of the sigmoidal curve and its theoretical underpinnings?
- How do the authors justify the choice of the sigmoidal curve over other potential functional forms?
- What are the potential implications of reward hacking on the scaling behavior of RLHF?
- How do the authors plan to extend their findings to other RL training paradigms beyond RLHF?

### Rating

5

### Confidence

3

**********

## Reviewer 2

### Summary

This paper presents a systematic study of scaling laws for RLHF, aiming to predict RLHF scaling in LLMs. The authors introduce a sigmoidal curve to model the relationship between expected reward and compute, and derive three key principles based on their empirical findings: (1) RLHF performance ceilings are not universal, (2) RLHF plateaus after a certain compute budget, and (3) scaling efficiency improves with larger batch sizes. They propose ScaleRL, an RL recipe combining various design choices, and demonstrate its effectiveness by scaling up to 100,000 GPU hours, achieving state-of-the-art performance and predictability. The study provides valuable insights into the scaling behavior of RLHF and offers a practical recipe for scaling up RL training.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper provides a systematic study of scaling laws for RLHF, addressing a critical gap in understanding how RL training scales with compute. The introduction of a sigmoidal curve to model the relationship between expected reward and compute is a novel approach that allows for more precise predictions of scaling behavior.
2. The authors conduct extensive experiments across various design choices, providing a comprehensive analysis of their impact on scaling performance. The derivation of three key principles offers valuable insights into the behavior of RLHF under different compute budgets.
3. The proposed ScaleRL recipe, combining various design choices, demonstrates strong empirical performance and predictability. The authors provide detailed ablation studies to justify the selection of each component in ScaleRL, showcasing the effectiveness of their approach.
4. The paper is well-written and clearly presents the methodology, experimental setup, and results. The figures and tables are informative and effectively communicate the key findings. The authors also provide a thorough discussion of the limitations and potential future directions.

### Weaknesses

#### Some Related Works


#### comment

1. While the paper provides a comprehensive study of scaling laws for RLHF, the analysis is primarily focused on a specific set of design choices and model architectures. It would be beneficial to explore the generalizability of the findings to other RL algorithms and model architectures, especially those with different inductive biases. For instance, the study could investigate how the observed principles apply to algorithms like PPO or TRPO, which have different optimization landscapes and convergence properties than the methods explored. Furthermore, the study should consider models with different architectures, such as those with varying depths or widths, to assess the robustness of the scaling laws.
2. The paper focuses on scaling up to 100,000 GPU hours, which is a significant computational effort. However, it would be valuable to explore the performance of ScaleRL at even larger scales to assess its long-term effectiveness and identify potential bottlenecks. The current study does not provide sufficient evidence to conclude that the observed scaling trends will continue to hold as the compute budget increases further. It is important to investigate the potential for diminishing returns or even negative scaling effects at extremely large scales.
3. While the paper provides a detailed analysis of the scaling behavior of RLHF, it would be helpful to include a more in-depth discussion of the limitations of the proposed scaling laws and potential failure modes. For example, the sigmoidal curve might not accurately capture the scaling behavior in all scenarios, especially when the compute budget is significantly different from those explored in the study. It is important to acknowledge the potential for the scaling laws to break down under certain conditions and to discuss the factors that might contribute to such breakdowns. The paper should also explore the sensitivity of the scaling laws to different hyperparameters and training configurations.

### Suggestions

To enhance the generalizability of the findings, the authors should conduct experiments with a wider range of RL algorithms and model architectures. Specifically, they could explore how the observed principles apply to algorithms like Proximal Policy Optimization (PPO) and Trust Region Policy Optimization (TRPO), which have different optimization landscapes and convergence properties than the methods explored in the paper. This would involve not only replicating the experiments with these algorithms but also carefully analyzing the differences in their scaling behavior. Furthermore, the authors should investigate models with varying depths and widths to assess the robustness of the scaling laws. This could involve training models with different numbers of layers and hidden units and analyzing how these architectural choices affect the scaling performance. Such experiments would provide a more comprehensive understanding of the factors that influence the scaling behavior of RLHF and would help to identify the key architectural features that contribute to optimal scaling.

To address the limitations of the current study's scale, the authors should conduct experiments at even larger scales to assess the long-term effectiveness of ScaleRL. This could involve training models with significantly larger compute budgets and analyzing the scaling trends over time. The authors should also investigate the potential for diminishing returns or even negative scaling effects at extremely large scales. This could involve analyzing the performance of ScaleRL at different stages of training and identifying any points where the scaling performance plateaus or even decreases. Furthermore, the authors should explore the potential for using different scaling strategies at different stages of training to optimize the overall performance. This could involve using different batch sizes or learning rates at different stages of training to adapt to the changing scaling behavior.

Finally, the authors should provide a more in-depth discussion of the limitations of the proposed scaling laws and potential failure modes. This should include a detailed analysis of the potential for the sigmoidal curve to break down under certain conditions and a discussion of the factors that might contribute to such breakdowns. The authors should also explore the sensitivity of the scaling laws to different hyperparameters and training configurations. This could involve conducting experiments with different hyperparameter settings and analyzing how these settings affect the scaling performance. Furthermore, the authors should discuss the potential for the scaling laws to be violated under specific conditions, such as when the compute budget is significantly different from those explored in the study. This would provide a more complete and nuanced understanding of the scaling behavior of RLHF and would help to identify the limitations of the proposed scaling laws.

### Questions

1. How do the authors plan to extend their findings to other RL algorithms and model architectures? Are there specific challenges or considerations they anticipate in such an extension?
2. What are the potential limitations of the proposed scaling laws at even larger scales, and how might the performance of ScaleRL be affected?
3. How sensitive are the proposed scaling laws to different hyperparameters and training configurations? Are there specific conditions under which the scaling laws might break down?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper presents a systematic study of scaling laws for RLHF, aiming to predict RLHF scaling in LLMs. The authors introduce a sigmoidal curve to model the relationship between expected reward and compute, and derive three key principles based on their empirical findings: (1) RLHF performance ceilings are not universal, (2) RLHF plateaus after a certain compute budget, and (3) scaling efficiency improves with larger batch sizes. They propose ScaleRL, an RL recipe combining various design choices, and demonstrate its effectiveness by scaling up to 100,000 GPU hours, achieving state-of-the-art performance and predictability. The study provides valuable insights into the scaling behavior of RLHF and offers a practical recipe for scaling up RL training.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a sigmoidal curve to model the relationship between expected reward and compute, which is a novel approach to understanding scaling in RLHF. This curve allows for more precise predictions of scaling behavior and provides a valuable tool for researchers and practitioners.

2. The authors conduct extensive experiments across various design choices, providing a comprehensive analysis of their impact on scaling performance. The derivation of three key principles offers valuable insights into the behavior of RLHF under different compute budgets.

3. The proposed ScaleRL recipe, combining various design choices, demonstrates strong empirical performance and predictability. The authors provide detailed ablation studies to justify the selection of each component in ScaleRL, showcasing the effectiveness of their approach.

4. The paper is well-written and clearly presents the methodology, experimental setup, and results. The figures and tables are informative and effectively communicate the key findings. The authors also provide a thorough discussion of the limitations and potential future directions.

### Weaknesses

#### Some Related Works


#### comment

1. The paper is primarily empirical, focusing on the empirical study of RLHF scaling without proposing new algorithmic or theoretical innovations. While the empirical findings are valuable, the lack of theoretical depth limits the paper's contribution to the broader machine learning community.

2. The paper's scope is limited to RLHF, and it does not explore other RL training paradigms, such as PPO. This narrow focus restricts the generalizability of the findings and the applicability of the proposed scaling laws to other RL methods.

3. The paper does not provide a detailed analysis of the impact of different reward structures on the scaling behavior of RLHF. Given that the reward model plays a crucial role in RLHF, understanding how different reward models affect scaling is essential for practical applications.

4. The paper does not explore the impact of different reward model architectures on the scaling behavior of RLHF. Given that the reward model plays a crucial role in RLHF, understanding how different reward models affect scaling is essential for practical applications.

### Suggestions

The paper would benefit from a more thorough investigation into the theoretical underpinnings of the observed scaling laws. While the empirical results are compelling, a theoretical framework could provide a deeper understanding of why these laws hold and how they might generalize to other settings. For example, exploring connections to existing theoretical work on generalization in RL or analyzing the optimization landscape of the RLHF objective could provide valuable insights. Furthermore, the paper could benefit from a more detailed analysis of the limitations of the proposed sigmoidal curve. While it provides a good fit to the empirical data, it is important to acknowledge that it may not capture all aspects of the scaling behavior. A discussion of the potential biases or assumptions inherent in the curve and how these might affect the conclusions would be beneficial. It would also be useful to explore alternative functional forms and compare their performance to the sigmoidal curve.

To address the limited scope of the study, the authors should consider expanding their analysis to include other RL training paradigms, such as PPO. This would help to determine whether the observed scaling laws are specific to RLHF or are more general principles of RL training. Such an analysis would also help to identify any differences in the scaling behavior of different RL algorithms and provide guidance on how to choose the most appropriate algorithm for a given task. Furthermore, the paper should include a more detailed analysis of the impact of different reward structures on the scaling behavior of RLHF. This could involve experimenting with different reward models, including those with varying levels of complexity and training data. A thorough analysis of how different reward models affect the scaling curve would provide valuable insights for practitioners. Similarly, the paper should explore the impact of different reward model architectures on the scaling behavior of RLHF. This could involve experimenting with different types of reward models, such as transformer-based models or simpler MLPs, and analyzing how these architectures affect the scaling curve. Such an analysis would provide a more complete understanding of the role of the reward model in RLHF scaling.

Finally, the paper should provide more guidance on how to choose the appropriate scaling recipe for a given task. While the authors propose ScaleRL, they do not provide clear guidelines on how to adapt this recipe to different scenarios. For example, how should practitioners choose the optimal batch size or compute budget for a given task? The paper could also benefit from a more detailed discussion of the practical implications of the observed scaling laws. For example, how do these laws affect the cost and time required to train large language models? A more thorough discussion of these practical considerations would make the paper more useful to practitioners.

### Questions

1. How do the authors plan to extend their findings to other RL training paradigms beyond RLHF, such as PPO or TRPO? Are there specific challenges or considerations they anticipate in such an extension?

2. What are the potential limitations of the proposed scaling laws at even larger scales, and how might the performance of ScaleRL be affected?

3. How sensitive are the proposed scaling laws to different hyperparameters and training configurations? Are there specific conditions under which the scaling laws might break down?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

This paper presents a comprehensive study on scaling laws for RLHF, introducing a sigmoidal curve to model the relationship between expected reward and compute. The authors derive three key principles governing RLHF scaling and propose ScaleRL, an RL recipe combining various design choices, achieving state-of-the-art performance and predictability.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper provides a novel perspective on RLHF scaling by introducing a sigmoidal curve to model the relationship between expected reward and compute.
2. The authors conduct extensive experiments across various design choices, offering valuable insights into RLHF scaling.
3. The proposed ScaleRL recipe is well-validated, achieving state-of-the-art performance and predictability in scaling.
4. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on RLHF, and it would be beneficial to explore the generalizability of the findings to other RL training paradigms, such as PPO or TRPO.
2. The paper does not provide a detailed analysis of the impact of different reward structures on the scaling behavior of RLHF.
3. The paper does not explore the impact of different reward model architectures on the scaling behavior of RLHF.

### Suggestions

The paper's focus on RLHF is a significant limitation, as the scaling laws observed in this specific context may not directly translate to other reinforcement learning algorithms. To strengthen the paper, it would be crucial to investigate how the proposed scaling laws and the ScaleRL recipe perform with other popular RL algorithms like Proximal Policy Optimization (PPO) or Trust Region Policy Optimization (TRPO). This would involve conducting experiments with these algorithms under similar conditions as those used for RLHF, including varying compute budgets and analyzing the resulting scaling curves. Such an analysis would help determine the generalizability of the findings and identify any algorithm-specific factors that might influence scaling behavior. Furthermore, it would be valuable to explore whether the sigmoidal curve can accurately model the scaling behavior of these other algorithms, or if alternative functional forms are needed. This would provide a more comprehensive understanding of the scaling properties of RL algorithms in general.

Another area that requires further investigation is the impact of different reward structures on the scaling behavior of RLHF. The paper currently lacks a detailed analysis of how the choice of reward model, including its complexity and training data, affects the scaling curve. It would be beneficial to conduct experiments with different reward models, such as those with varying levels of complexity or trained on different datasets, and analyze how these variations impact the scaling performance. This analysis should include a comparison of the scaling curves obtained with different reward models, as well as an investigation into the underlying reasons for any observed differences. For example, it would be interesting to examine whether more complex reward models lead to different scaling behaviors compared to simpler ones, and whether the training data used for the reward model has any impact on the scaling curve. This would provide a more nuanced understanding of the role of the reward model in RLHF scaling.

Finally, the paper should explore the impact of different reward model architectures on the scaling behavior of RLHF. The current study does not delve into the architectural choices of the reward model, such as the type of neural network used (e.g., MLP, CNN, Transformer) or the specific layers and activation functions employed. It would be valuable to conduct experiments with different reward model architectures and analyze how these architectural choices affect the scaling curve. This analysis should include a comparison of the scaling curves obtained with different reward model architectures, as well as an investigation into the underlying reasons for any observed differences. For example, it would be interesting to examine whether certain architectures are more prone to reward hacking or other scaling issues, and whether there are any architectural properties that can be leveraged to improve the scaling behavior of RLHF. This would provide a more complete understanding of the role of the reward model architecture in RLHF scaling.

### Questions

1. How do the authors plan to extend their findings to other RL training paradigms beyond RLHF, such as PPO or TRPO?
2. What are the potential limitations of the proposed scaling laws at even larger scales, and how might the performance of ScaleRL be affected?
3. How sensitive are the proposed scaling laws to different hyperparameters and training configurations? Are there specific conditions under which the scaling laws might break down?

### Rating

8

### Confidence

2

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

Plan:
1. Go through each reviewer's comments one by one.
2. For each comment identified as a weakness, find supporting evidence from the paper.
3. Categorize the weakness and provide specific quotes or references.
4. If a weakness is not supported by the paper, explain why.
**Review 1**

1. Weakness Statement:
"The paper is primarily empirical, focusing on the empirical study of RLHF scaling without proposing new algorithmic or theoretical innovations. While the empirical findings are valuable, the lack of theoretical depth limits the paper's contribution to the broader machine learning community."

2. Evidence Collection:
a) Method-related Evidence (if applicable):
   - The paper introduces a "sigmoidal curve" to model scaling behavior (Section 2, Equation 1). This is a mathematical formulation, but the paper doesn't delve into the theoretical underpinnings of why this specific form is chosen or how it relates to underlying RLHF mechanisms.
   - The derivation of principles (Section 3) is based on empirical observations from ablation studies, not on formal theoretical proofs or derivations from RL principles.

b) Experiment-related Evidence (if applicable):
   - The experiments focus on empirical validation of the scaling curve and principles (Section 3, Section 4). There are no theoretical analyses of the RLHF process itself.

3. Literature Gap Analysis:
   - The paper cites works on scaling laws in pre-training and generalization (Section 2), but it doesn't connect its sigmoidal curve to existing theoretical frameworks in RL or generalization.

4. Validation Analysis:
   - Primary evidence summary: The paper focuses on empirical validation of a scaling law using a sigmoidal curve and derived principles. It doesn't provide a theoretical justification for the curve or the principles.
   - Supporting quotes:
     - "We fit sigmoidal curves to RL training and ablate results to quantify the asymptotic performance ( A ) on an 8B model parameters scale, where 0 ≤ A ≤ 1 0\leq A \leq 1 0 ≤ A ≤ 1 represents the asymptotic reward ( R C R_{C} RC) on an iid validation set and training compute ( C C C )." (Section 2) - This shows the empirical fitting of the curve.
     - "Based on these insights, ScaleRL achieves predictable scaling by integrating existing methods, rather than inventing novel methods." (Section 7) - This highlights the focus on integration rather than innovation.
   - Impact assessment: The lack of theoretical depth limits the generalizability and deeper understanding of the proposed scaling law.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper's focus on empirical fitting of a sigmoidal curve and derivation of principles based on ablation studies, without theoretical justification.

1. Weakness Statement:
"The paper's scope is limited to RLHF, and it does not explore other RL training paradigms, such as PPO. This narrow focus restricts the generalizability of the findings and the applicability of the proposed scaling laws to other RL methods."

2. Evidence Collection:
a) Method-related Evidence (if applicable):
   - The paper explicitly focuses on RLHF in the introduction and throughout the methodology (Section 2, Section 3, Section 4).

b) Experiment-related Evidence (if applicable):
   - All experiments are conducted using RLHF methods (Section 3, Section 4).

3. Literature Gap Analysis:
   - The related work section (Section A.1) mentions PPO but doesn't discuss its scaling properties or how they might differ from RLHF.

4. Validation Analysis:
   - Primary evidence summary: The paper's entire scope is centered around RLHF, with no exploration of other RL algorithms like PPO.
   - Supporting quotes:
     - "Reinforcement learning (RL) has become central to training large language models (LLMs), yet the field lacks predictive scaling methodologies comparable to those established for pre-training." (Abstract) - This sets the scope.
     - "We fit sigmoidal curves to RL training and ablate results to quantify the asymptotic performance ( A ) on an 8B model parameters scale, where 0 ≤ A ≤ 1 0\leq A \leq 1 0 ≤ A ≤ 1 represents the asymptotic reward ( R C R_{C} RC) on an iid validation set and training compute ( C C C )." (Section 2) - This is specific to RL.
     - "Based on these insights, ScaleRL achieves predictable scaling by integrating existing methods, rather than inventing novel methods." (Section 7) - This reinforces the RL focus.
   - Impact assessment: The findings might not be directly applicable to other RL paradigms, limiting the broader impact of the work.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper's explicit focus on RLHF and the absence of any discussion or experiments involving other RL algorithms like PPO.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the impact of different reward structures on the scaling behavior of RLHF. Given that the reward model plays a crucial role in RLHF, understanding how different reward models affect scaling is essential for practical applications."

2. Evidence Collection:
a) Method-related Evidence (if applicable):
   - The paper mentions the reward model in the methodology (Section 2) and in the ScaleRL recipe (Section 4).

b) Experiment-related Evidence (if applicable):
   - The ablation study on the reward model (Section 3.2) compares different reward models (ASPO, GSPO, DAPO, CISPO) and their impact on performance.
   - The paper states, "The reward model is a critical component of RLHF, and its choice can significantly impact the final performance." (Section 3.2).

3. Literature Gap Analysis:
   - The related work section (Section A.1) mentions different reward models but doesn't delve into their specific effects on scaling.

4. Validation Analysis:
   - Primary evidence summary: The paper does analyze the impact of different reward models in the ablation study, acknowledging its importance.
   - Supporting quotes:
     - "The reward model is a critical component of RLHF, and its choice can significantly impact the final performance." (Section 3.2)
     - "We compare the asymmetric DAPO loss (Eq. 8 ) with two recently proposed alternatives: GSPO ( Zheng et al., 2025a ) and CISPO ( MiniMax , 2024 ; Yao et al., 2025 ) . GSPO applies importance sampling at the sequence level as opposed to GRPO’s token-level formulation. Specifically, GSPO alters the token-level IS ratio (Eq. 2 ) to sequence-level ratios: ρ i ​ ( θ ) = π t ​ r ​ ( y i , t ) π g ​ e ​ n ​ ( y i , t ) ; 0< mean ⁡ ( { ρ i ​ ( θ ) } j = 1 G ) < 1 , \begin{array}{r}{\rho_{i,t}(\theta):=\frac{\pi_{train}^{\theta}(y_{i,t})}{\pi_{gen}^{\theta}(y_{i,t})},\quad\mathrm{sg}\text{ is the stop-gradient function:}}\end{array} \end{array} \begin{array}{r}{\mathrm{clip}_{\mathrm{asym}}(\rho,\epsilon^{-},\epsilon^{+}) :=\mathrm{clip}(\rho,\,1-\epsilon^{-},\,1+\epsilon^{+})\ .} \end{array} \end{array} \begin{array}{r}{\mathrm{GSPO}_{i}(\theta):=\hskip-6.99997pt\underset{\begin{array}{c}x\sim D}{\mathrm{clip}}\begin{array}{\mathrm{asym}}\mathrm{IS}\end{array}\begin{array}{\mathrm{clip}}\mathrm{asym}\mathrm{IS}\end{array}\mathrm{RL}\mathrm{loss}\mathrm{(\mathrm{\emph{G}}uan et al., 2024 )}\end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{array} \end{endarray}

Now, I have successfully verified each review. Next, I will generate a detailed summary of this paper.