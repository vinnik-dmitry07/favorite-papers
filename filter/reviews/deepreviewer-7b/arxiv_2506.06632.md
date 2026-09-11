I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper proposes a curriculum reinforcement learning method to enhance the reasoning capabilities of language models. The proposed method, E2H Reasoner (E2H-Reasoner), schedules tasks from easy to hard, allowing LLMs to build core reasoning abilities and generalize to more complex problems. Theoretical analysis and finite-sample complexity bounds are provided, demonstrating that E2H-Reasoner requires fewer samples than direct learning approaches. Empirical results show that E2H-Reasoner outperforms existing methods on five reasoning tasks, including Blocksworld, Countdown, and AQuA, with significant improvements in accuracy and generalization.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper introduces a novel curriculum reinforcement learning approach (E2H-Reasoner) that effectively schedules tasks from easy to hard, enabling LLMs to build core reasoning abilities and generalize to more complex problems.
2. Theoretical analysis and finite-sample complexity bounds are provided, demonstrating that E2H-Reasoner requires fewer samples than direct learning approaches.
3. Empirical results show that E2H-Reasoner outperforms existing methods on five reasoning tasks, including Blocksworld, Countdown, and AQuA, with significant improvements in accuracy and generalization.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's theoretical analysis relies on assumptions that may not hold in practical scenarios, such as the bounded distribution shift and the assumption of a well-defined curriculum. Specifically, the assumption of a bounded distribution shift between consecutive tasks is a strong one, as it requires a careful selection of intermediate tasks to ensure that the agent can smoothly transition between them. The paper does not provide a clear methodology for how to achieve this in practice, and it is unclear how sensitive the method is to violations of this assumption. Furthermore, the assumption of a well-defined curriculum, where the difficulty of tasks is clearly ordered, may not always be the case in real-world scenarios, and the paper does not discuss how the method would perform with a less structured curriculum.
2. The empirical evaluation is limited to a small set of reasoning tasks, and it is unclear how well the proposed method would generalize to other types of tasks or domains. The tasks used in the evaluation, such as Blocksworld and Countdown, are relatively simple and may not fully capture the complexities of real-world reasoning problems. The paper does not provide a detailed analysis of the types of reasoning skills that are learned by the proposed method, nor does it discuss how the method could be adapted to learn more complex reasoning skills. Additionally, the paper does not provide a clear comparison of the computational cost of the proposed method with existing approaches, making it difficult to assess its practical applicability.
3. The paper does not provide a detailed discussion of the limitations of the proposed method, such as its sensitivity to hyperparameter settings or its robustness to noisy or incomplete data. The paper also does not discuss the potential ethical implications of using the proposed method, such as the risk of overfitting to specific types of problems or the potential for bias in the learned reasoning skills. A more thorough discussion of these limitations would help to provide a more balanced and realistic assessment of the proposed method.

### Suggestions

The paper would benefit from a more detailed discussion of the assumptions underlying the theoretical analysis and how these assumptions might affect the practical performance of the proposed method. Specifically, the authors should provide a more rigorous analysis of the sensitivity of the method to violations of the bounded distribution shift assumption, and they should discuss how the method could be adapted to handle more complex or less structured curricula. This could involve exploring alternative methods for selecting intermediate tasks or developing techniques for automatically generating a suitable curriculum. Furthermore, the authors should provide a more detailed analysis of the types of reasoning skills that are learned by the proposed method, and they should discuss how the method could be adapted to learn more complex reasoning skills. This could involve exploring different reward functions or using more sophisticated task decomposition techniques. A more thorough discussion of these limitations would help to provide a more balanced and realistic assessment of the proposed method.

To address the limitations of the empirical evaluation, the authors should consider evaluating the proposed method on a wider range of reasoning tasks, including more complex and realistic problems. This could involve using benchmark datasets from areas such as natural language understanding, common-sense reasoning, or mathematical problem-solving. The authors should also provide a more detailed analysis of the types of reasoning skills that are learned by the proposed method, and they should discuss how the method could be adapted to learn more complex reasoning skills. This could involve exploring different reward functions or using more sophisticated task decomposition techniques. Additionally, the authors should provide a more detailed comparison of the computational cost of the proposed method with existing approaches, making it easier to assess its practical applicability. This could involve reporting the training time and memory requirements of the proposed method, as well as comparing its performance to other methods in terms of both accuracy and computational efficiency.

Finally, the paper should include a more detailed discussion of the limitations of the proposed method, such as its sensitivity to hyperparameter settings or its robustness to noisy or incomplete data. The authors should also discuss the potential ethical implications of using the proposed method, such as the risk of overfitting to specific types of problems or the potential for bias in the learned reasoning skills. This could involve exploring techniques for mitigating these limitations, such as using regularization or data augmentation. A more thorough discussion of these limitations would help to provide a more balanced and realistic assessment of the proposed method and would make the paper more useful to the broader research community.

### Questions

1. How does the proposed method handle tasks with unclear or overlapping difficulty levels? Could you provide more details on how the method determines task difficulty in such cases?
2. Could you elaborate on the sensitivity of the method to hyperparameter settings? Are there specific hyperparameters that are particularly critical for performance?
3. How does the proposed method compare to other curriculum learning approaches in terms of computational cost and scalability?

### Rating

5

### Confidence

3

**********

## Reviewer 2

### Summary

This paper proposes a curriculum reinforcement learning method for LLMs, which gradually increases the difficulty of tasks. The authors provide theoretical guarantees for the method and conduct experiments on five reasoning tasks, demonstrating that it outperforms existing methods.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide theoretical guarantees for the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The motivation for the method is unclear. The authors mention that the proposed method is inspired by curriculum learning and reinforcement learning, but the connection between these two areas is not well-established. Specifically, the paper does not clearly articulate why a reinforcement learning framework is necessary for curriculum learning in the context of LLMs, especially given that the tasks are pre-defined and the learning process is primarily focused on improving performance on these tasks. The paper needs to better justify the choice of a reinforcement learning approach over simpler curriculum learning strategies that do not involve reward functions.
2. The proposed method is not novel. The method is a combination of curriculum learning and reinforcement learning, which is not a new idea. The paper does not sufficiently highlight the unique aspects of their approach compared to existing methods that combine these two areas. The specific implementation details and the theoretical analysis are not presented in a way that clearly distinguishes the proposed method from existing approaches. The paper needs to provide a more detailed comparison to existing methods and clearly articulate the novel contributions of their approach.

### Suggestions

The paper should provide a more detailed explanation of why a reinforcement learning framework is necessary for curriculum learning in the context of LLMs. The authors should clarify the specific advantages of using reinforcement learning over simpler curriculum learning strategies, especially given that the tasks are pre-defined. For example, they could discuss how the reinforcement learning framework allows for more adaptive task selection or how it can handle situations where the optimal curriculum is not known a priori. The paper should also provide a more detailed comparison to existing methods that combine curriculum learning and reinforcement learning. The authors should clearly articulate the novel contributions of their approach and provide a more detailed analysis of the differences between their method and existing approaches. This could include a discussion of the specific implementation details and the theoretical analysis that distinguishes their method from existing approaches. The paper should also provide a more detailed explanation of the task decomposition strategies used for tasks without human-annotated difficulty levels. The authors should explain how they estimate difficulty using the zero-shot error rate of the base model and how they use this information to define the curriculum. The paper should also provide a more detailed analysis of the experimental results, including a discussion of the limitations of the proposed method and potential directions for future research. This could include a discussion of the computational cost of the proposed method and how it scales with the number of tasks and the complexity of the tasks.

### Questions

1. How is the proposed method different from curriculum learning and reinforcement learning?
2. How does the proposed method handle tasks without human-annotated difficulty levels?
3. How does the proposed method compare to other curriculum learning approaches?

### Rating

5

### Confidence

3

**********

## Reviewer 3

### Summary

This paper introduces a curriculum reinforcement learning approach, E2H Reasoner, to enhance the reasoning capabilities of language models. The method schedules tasks from easy to hard, enabling the model to learn core reasoning abilities and generalize to more complex problems. Theoretical analysis and finite-sample complexity bounds are provided, demonstrating that E2H Reasoner requires fewer total samples than direct learning on the final task. Empirical results show that E2H Reasoner outperforms existing methods on five reasoning tasks, including Blocksworld, Countdown, and AQuA, with significant improvements in accuracy and generalization.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide theoretical guarantees for the proposed method, which is a strong point.
3. The proposed method achieves better performance on five reasoning tasks.

### Weaknesses

#### Some Related Works


#### comment

1. The motivation for the method is unclear. The authors mention that the proposed method is inspired by curriculum learning and reinforcement learning, but the connection between these two areas is not well-established. Specifically, the paper does not clearly articulate why a reinforcement learning framework is necessary for curriculum learning in the context of LLMs, especially given that the tasks are pre-defined and the learning process is primarily focused on improving performance on these tasks. The paper needs to better justify the choice of a reinforcement learning approach over simpler curriculum learning strategies that do not involve reward functions.
2. The proposed method is not novel. The method is a combination of curriculum learning and reinforcement learning, which is not a new idea. The paper does not sufficiently highlight the unique aspects of their approach compared to existing methods that combine these two areas. The specific implementation details and the theoretical analysis are not presented in a way that clearly distinguishes the proposed method from existing approaches. The paper needs to provide a more detailed comparison to existing methods and clearly articulate the novel contributions of their approach.

### Suggestions

The paper should provide a more detailed explanation of why a reinforcement learning framework is necessary for curriculum learning in the context of LLMs. The authors should clarify the specific advantages of using reinforcement learning over simpler curriculum learning strategies, especially given that the tasks are pre-defined. For example, they could discuss how the reinforcement learning framework allows for more adaptive task selection or how it can handle situations where the optimal curriculum is not known a priori. The paper should also provide a more detailed comparison to existing methods that combine curriculum learning and reinforcement learning. The authors should clearly articulate the novel contributions of their approach and provide a more detailed analysis of the differences between their method and existing approaches. This could include a discussion of the specific implementation details and the theoretical analysis that distinguishes their method from existing approaches. The paper should also provide a more detailed explanation of the task decomposition strategies used for tasks without human-annotated difficulty levels. The authors should explain how they estimate difficulty using the zero-shot error rate of the base model and how they use this information to define the curriculum. The paper should also provide a more detailed analysis of the experimental results, including a discussion of the limitations of the proposed method and potential directions for future research. This could include a discussion of the computational cost of the proposed method and how it scales with the number of tasks and the complexity of the tasks.

### Questions

1. Can you provide more details about the task decomposition strategies used for tasks without human-annotated difficulty levels?
2. How does the proposed method compare to other curriculum learning approaches?

### Rating

5

### Confidence

3

**********

## Reviewer 4

### Summary

This paper proposes a curriculum reinforcement learning method to improve the reasoning ability of LLMs. The authors propose a method to decompose tasks into different difficulty levels and use a probabilistic scheduler to sample tasks from different difficulty levels. The authors provide theoretical analysis and empirical results to show the effectiveness of their method.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide theoretical analysis and empirical results to show the effectiveness of their method.
3. The authors propose a method to decompose tasks into different difficulty levels and use a probabilistic scheduler to sample tasks from different difficulty levels.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a clear definition of reasoning ability, which makes it difficult to evaluate the effectiveness of the proposed method. The authors should provide a more precise definition of reasoning ability and justify why their method is effective in improving this ability.
2. The authors do not provide a clear explanation of how the difficulty levels are determined. The authors should provide more details on how the difficulty levels are determined and justify why the chosen difficulty levels are appropriate for the tasks.
3. The authors do not provide a clear explanation of how the probabilistic scheduler is designed. The authors should provide more details on how the probabilistic scheduler is designed and justify why the chosen design is effective in improving the reasoning ability of LLMs.
4. The authors do not provide a clear explanation of how the proposed method is different from existing curriculum learning methods. The authors should provide a more detailed comparison of their method with existing curriculum learning methods and justify why their method is more effective in improving the reasoning ability of LLMs.

### Suggestions

The paper would benefit significantly from a more rigorous definition of 'reasoning ability' within the context of LLMs. Currently, the term is used somewhat loosely, making it difficult to assess the true impact of the proposed method. The authors should consider defining reasoning ability in terms of specific cognitive processes, such as multi-step inference, logical deduction, or problem-solving under uncertainty. This definition should then be used to evaluate the effectiveness of the proposed method. For example, they could measure the model's ability to solve problems that require a specific number of reasoning steps, or its performance on tasks that involve logical deduction. Furthermore, the authors should provide a more detailed analysis of how their method improves these specific aspects of reasoning, rather than simply showing overall performance gains. This would allow for a more nuanced understanding of the method's strengths and weaknesses.

To address the lack of clarity regarding difficulty levels, the authors should provide a more detailed explanation of the criteria used to determine these levels. Simply stating that difficulty is based on human-annotated difficulty scores or zero-shot error rates is insufficient. The authors should specify the exact algorithm or heuristic used to translate these scores into difficulty levels. For example, if human-annotated scores are used, they should describe how these scores are normalized or discretized to create distinct difficulty levels. Similarly, if zero-shot error rates are used, they should explain how these rates are used to define the boundaries between difficulty levels. Furthermore, the authors should justify why these specific criteria are appropriate for the tasks being considered. A more detailed explanation of the difficulty level determination process would enhance the reproducibility and credibility of the results. The authors should also consider exploring alternative methods for difficulty level determination, such as using model confidence scores or task completion rates, and compare their performance with the current approach.

Finally, the authors need to provide a more detailed explanation of the probabilistic scheduler and its design choices. The current description is too high-level, and it is unclear how the scheduler is designed to effectively sample tasks from different difficulty levels. The authors should provide a mathematical formulation of the scheduler, including the specific parameters and their impact on the sampling distribution. They should also justify why the chosen scheduler is effective in improving the reasoning ability of LLMs. For example, they could explain how the scheduler encourages the model to start with easier tasks and gradually progress to more difficult ones. Furthermore, the authors should compare their scheduler with other existing curriculum learning methods, highlighting the advantages and disadvantages of their approach. This would provide a more comprehensive understanding of the proposed method's contribution to the field.

### Questions

1. How is the difficulty level determined in your method?
2. How is the probabilistic scheduler designed in your method?
3. How is your method different from existing curriculum learning methods?

### Rating

6

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers for the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

Plan:
1. Go through each reviewer's comments one by one.
2. For each comment, identify the type of weakness (theoretical, methodological, experimental, practical).
3. Find specific evidence in the paper (quotes, formulas, missing citations, etc.) to support the reviewer's claim.
4. If the reviewer points out a missing element, check if it's indeed missing.
5. If there are conflicting opinions, note them.
6. Finally, conclude whether the weakness is valid, partially valid, or invalid based on the evidence.
**Review 1**

1. Weakness Statement:
"The paper does not provide a clear definition of reasoning ability, which makes it difficult to evaluate the effectiveness of the proposed method. The authors should provide a more precise definition of reasoning ability and justify why their method is effective in improving this ability."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper introduces the concept of "reasoning" in the Introduction: "Recent RL post-trained models like DeepSeek R1 (Guo et al., 2025) and OpenAI o1 (Jaech et al., 2024) shows that reinforcement learning (RL) based post-training enhances reasoning."
   - The paper defines reasoning as "the ability to extract principles from simpler tasks and apply them to harder ones."
   - The paper also states: "Therefore, we adopt a view focusing on generalization, defining reasoning as the ability to extract principles from simpler tasks and apply them to harder ones."
   - The paper further elaborates on the limitations of current RL-based post-training methods in learning reasoning on inherently difficult tasks and contrasts it with supervised fine-tuning's success in solving harder tasks.

3. Literature Gap Analysis:
   - The paper cites works that use the term "reasoning" in the context of LLMs.

4. Validation Analysis:
   - Primary evidence summary: The paper provides a definition of reasoning, albeit brief, and contrasts it with the limitations of RL-based methods.
   - Supporting quotes: "Therefore, we adopt a view focusing on generalization, defining reasoning as the ability to extract principles from simpler tasks and apply them to harder ones."
   - Impact assessment: While the definition is present, the reviewer's point about it being "precise" and "justified" is subjective. The paper doesn't delve into a formal, mathematical definition of reasoning ability.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper provides a definition, but it's not a formal, mathematically rigorous definition.

1. Weakness Statement:
"The authors do not provide a clear explanation of how the difficulty levels are determined. The authors should provide more details on how the difficulty levels are determined and justify why the chosen difficulty levels are appropriate for the tasks."

2. Evidence Collection:
a) Method-related Evidence:
   - Section 3.3 "Task decomposition for RL post-training" discusses how difficulty is determined.
   - For datasets with human-annotated difficulty scores (Blocksworld, MATH), the paper states: "For tasks like Blocksworld, MATH, and Countdown, we use human-aligned difficulty signals such as plan length, labeled difficulty, or operand count (see Table 9 ). For others like AQuA and GSM8K, where such annotations are unavailable, we automatically estimate difficulty based on model error rates under CoT prompting and group examples accordingly (see Figs. 4.2 and 6 )."
   - The paper provides examples of difficulty metrics used: "For tasks like Blocksworld, MATH, and Countdown, we use human-aligned difficulty signals such as plan length, labeled difficulty, or operand count (see Table 9 ). For others like AQuA and GSM8K, where such annotations are unavailable, we automatically estimate difficulty based on model error rates under CoT prompting and group examples accordingly (see Figs. 4.2 and 6 )."
   - The paper mentions the use of CoT prompting for estimating difficulty on AQuA and GSM8K.

3. Literature Gap Analysis:
   - The paper cites works that use CoT prompting.

4. Validation Analysis:
   - Primary evidence summary: The paper explicitly describes how difficulty levels are determined, differentiating between human-annotated scores and automatically estimated scores based on CoT error rates.
   - Supporting quotes: "For tasks like Blocksworld, MATH, and Countdown, we use human-aligned difficulty signals such as plan length, labeled difficulty, or operand count (see Table 9 ). For others like AQuA and GSM8K, where such annotations are unavailable, we automatically estimate difficulty based on model error rates under CoT prompting and group examples accordingly (see Figs. 4.2 and 6 )."
   - Impact assessment: The reviewer's claim is incorrect as the paper does provide an explanation of how difficulty levels are determined.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: Section 3.3 and the surrounding text clearly explain the methodology for determining difficulty levels.

1. Weakness Statement:
"The authors do not provide a clear explanation of how the probabilistic scheduler is designed. The authors should provide more details on how the probabilistic scheduler is designed and justify why the chosen design is effective in improving the reasoning ability of LLMs."

2. Evidence Collection:
a) Method-related Evidence:
   - Section 3.2 "Training schedulers for LLM reasoning ability" introduces the concept of the probabilistic scheduler.
   - The paper describes three types of schedulers: Balanced, Cosine, and Gaussian.
   - For Balanced scheduling: "To avoid forgetting, the simplest way is to mix all data with different difficulties together and sample randomly, which can be considered as a trivial case of curriculum learning. Alternatively, this can be interpreted as the default behavior of any policy optimization algorithm (Shao et al., 2024; Schulman et al., 2017) ."
   - For Cosine scheduling: "To alleviate both the reward sparsity and forgetting issues, we propose a non-parametric scheduling strategy, namely, cosine sampling. This strategy can be written as:  𝑆 𝑐𝑜𝑠𝑒 𝑡 = 𝛼 𝑡 ⋅ ( 𝐾 − 𝑡 𝐾 ) , and  𝑥 𝑡 = ( 𝑡 𝐾 ) 𝛽 ⋅ 𝑘 , where we ignore the normalization term, and the probabilities will be normalized for sampling. In this sampling scheduler, we only have two hyperparameters, i.e. σ and β ."
   - For Gaussian scheduling: "As shown in Figure 4 (a), in a one-dimensional space, we assume the data distributions of tasks follow Gaussian distributions with the same variance σ  𝑘 , and the means of the adjacent task’s Gaussian distributions are assumed to have the same distance 1  𝛼 , i.e. , μ 𝑘 = 𝑘 − 1  𝛼 . Then the sampling probability is defined as the likelihood of a given position x t  belonging to different task Gaussian distributions, similar to the expectation–maximization algorithm ( McLachlan and Krishnan, 2008 ) ."
   - The paper provides the mathematical formulations for each scheduler.

3. Literature Gap Analysis:
   - The paper cites relevant works for policy optimization and expectation-maximization algorithms.

4. Validation Analysis:
   - Primary evidence summary: The paper provides detailed explanations of the three proposed schedulers, including their mathematical formulations and justifications for their design choices. The paper explicitly states the goals of each scheduler (e.g., avoiding forgetting for balanced, alleviating sparsity and forgetting for cosine, and bridging the gap for Gaussian).
   - Supporting quotes: The entire Section 3.2 provides the explanation of the schedulers.
   - Impact assessment: The reviewer's claim is incorrect as the paper provides a clear explanation of the scheduler design.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: Section 3.2 provides detailed descriptions and justifications for the proposed schedulers.

1. Weakness Statement:
"The authors do not provide a clear explanation of how the proposed method is different from existing curriculum learning methods. The authors should provide a more detailed comparison of their method with existing curriculum learning methods and justify why their method is more effective in improving the reasoning ability of LLMs."

2. Evidence Collection:
a) Method-related Evidence:
   - The Introduction mentions: "However, these initial efforts primarily rely on simplified strategies, such as training on easy tasks before switching to hard ones after a fixed number of iterations. In contrast, we introduce E2H Reasoner (E2H), a CRL approach with a probabilistic scheduler that gradually shifts focus from easy to hard tasks, enabling even LLMs to develop core reasoning abilities and generalize to more complex problems."
   - The Introduction also states: "To address the sparse reward problem, curriculum learning has been applied to reinforcement learning (CRL) by structuring training from easier to harder tasks ( Bengio et al., 2009 ) ."
   - The Related Work section discusses "Curriculum Learning organizes tasks by increasing difficulty to promote smoother and more effective training ( Bengio et al., 2009 ) ."
   - The Introduction contrasts RL post-training with CRL: "However, these initial efforts primarily rely on simplified strategies, such as training on easy tasks before switching to hard ones after a fixed number of iterations. In contrast, we introduce E2H Reasoner (E2H), a CRL approach with a probabilistic scheduler that gradually shifts focus from easy to hard tasks, enabling even LLMs to develop core reasoning abilities and generalize to more complex problems."
   - The Introduction also highlights the limitations of RL post-training: "However, RL struggles on harder tasks on which pre-trained models have low zero shot performance ( Shao et al., 2024 ; Zeng et al., 2025 ) and since rewards are granted only for correct answers, resulting in sparse learning signals."

3. Literature Gap Analysis:
   - The paper cites Bengio et al. (2009) as a foundational work on curriculum learning.

4. Validation Analysis:
   - Primary evidence summary: The paper explicitly differentiates its method from traditional RL post-training by highlighting the use of a probabilistic scheduler in CRL to address the sparse reward problem and enable gradual learning from easier to harder tasks. The introduction contrasts the proposed method with the limitations of RL post-training.
   - Supporting quotes: "However, these initial efforts primarily rely on simplified strategies... In contrast, we introduce E2H Reasoner (E2H), a CRL approach with a probabilistic scheduler that gradually shifts focus from easy to hard tasks..." and "However, RL struggles on harder tasks... since rewards are granted only for correct answers, resulting in sparse learning signals."
   - Impact assessment: The reviewer's claim is incorrect as the paper does provide a distinction between its method and existing curriculum learning approaches.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: The Introduction and Related Work sections clearly articulate the differences between the proposed method and existing curriculum learning approaches.

**Review 2**

1. Weakness Statement:
"The motivation for the method is unclear. The authors mention that the proposed method is inspired by curriculum learning and reinforcement learning, but the connection between these two areas is not well-established. Specifically, the paper does not clearly articulate why a reinforcement learning framework is necessary for curriculum learning in the context of LLMs, especially given that the tasks are pre-defined and the learning process is primarily focused on improving performance on these tasks. The paper needs to better justify the choice of a reinforcement learning framework over simpler curriculum learning strategies that do not involve reward functions."

2. Evidence Collection:
a) Method-related Evidence:
   - The Introduction states: "However, these initial efforts primarily rely on simplified strategies, such as training on easy tasks before switching to hard ones after a fixed number of iterations. In contrast, we introduce E2H Reasoner (E2H), a CRL approach with a probabilistic scheduler that gradually shifts focus from easy to hard tasks, enabling even LLMs to develop core reasoning abilities and generalize to more complex problems. We show that LLMs can learn tasks they initially failed in (Fig. 1 ). Empirically, we observe that, although easy tasks are important initially, fading them out through appropriate scheduling is essential in preventing overfitting. Theoretically, we establish convergence guarantees for E2H Reasoner within an approximate policy iteration framework."
   - The Introduction also mentions: "We formulate the reasoning process of LLMs as a RL problem defined over a discounted Markov Decision Process (MDP) ℳ = ( 𝒮 , 𝒜 , P , r , γ ) \mathcal{M}=(\mathcal{S},\mathcal{A},P,r,\gamma) , where 𝒮 \mathcal{S} is the state space, 𝒜 \mathcal{A} is the action space, P : 𝒮 × 𝒜 → Δ ⁡ ( 𝒮 ) P : \mathcal{S} \times \mathcal{A} \to \Delta(\mathcal{S}) is the transition kernel, r : 𝒮 × 𝒜 → [ 0 , R max ] r : \mathcal{S} \times \mathcal{A} \to [ 0, R_{\max} ] is the reward function, and γ ∈ ( 0 , 1 ) \gamma \in ( 0 , 1 ) is the discount factor."
   - The paper explicitly frames the problem as a Reinforcement Learning problem, defining the state space, action space, transition kernel, reward function, and discount factor.
   - The paper contrasts its approach with RL post-training, which is a form of RL.

3. Literature Gap Analysis:
   - The paper cites works that use RL for training language models.

4. Validation Analysis:
   - Primary evidence summary: The paper clearly frames the problem as a Reinforcement Learning problem and explicitly states the motivation for using an RL framework, particularly in the context of addressing the sparse reward problem in RL post-training. The paper contrasts its approach with traditional RL post-training methods.
   - Supporting quotes: "We formulate the reasoning process of LLMs as a RL problem..." and the entire Introduction section outlining the motivation.
   - Impact assessment: The reviewer's claim is incorrect as the paper explicitly states the motivation for using an RL framework.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: The Introduction and the formulation of the problem as an MDP clearly establish the use of an RL framework as a core component.

1. Weakness Statement:
"The proposed method is not novel. The method is a combination of curriculum learning and reinforcement learning, which is not a new idea. The paper does not sufficiently highlight the unique aspects of their approach compared to existing methods that combine these two areas. The specific implementation details and the theoretical analysis are not presented in a way that clearly distinguishes the proposed method from existing approaches. The paper needs to provide a more detailed comparison to existing methods and clearly articulate the novel contributions of their approach."

2. Evidence Collection:
a) Method-related Evidence:
   - The Introduction states: "However, these initial efforts primarily rely on simplified strategies, such as training on easy tasks before switching to hard ones after a fixed number of iterations. In contrast, we introduce E2H Reasoner (E2H), a CRL approach with a probabilistic scheduler that gradually shifts focus from easy to hard tasks, enabling even LLMs to develop core reasoning abilities and generalize to more complex problems."
   - The Introduction also mentions: "We show that LLMs can learn tasks they initially failed in (Fig. 1 ). Empirically, we observe that, although easy tasks are important initially, fading them out through appropriate scheduling is essential in preventing overfitting."
   - The Introduction highlights the specific contributions: "To address the sparse reward problem, curriculum learning has been applied to reinforcement learning (CRL) by structuring training from easier to harder tasks ( Bengio et al., 2009 ) . We show that LLMs can learn tasks they initially failed in (Fig. 1 ). Empirically, we observe that, although easy tasks are important initially, fading them out through appropriate scheduling is essential in preventing overfitting. Theoretically, we establish convergence guarantees for E2H Reasoner within an approximate policy iteration framework. We derive finite-sample complexity bounds and show that, when tasks are appropriately decomposed and conditioned, learning through curriculum stages requires fewer total samples than direct learning, aligning with and supporting our empirical observations."
   - The Related Work section discusses existing CRL methods and their limitations.
   - The Experiments section compares E2H Reasoner to other methods, including those that combine curriculum learning and reinforcement learning.

3. Literature Gap Analysis:
   - The paper cites relevant works in curriculum learning and reinforcement learning.

4. Validation Analysis:
   - Primary evidence summary: The paper explicitly claims novelty by contrasting its approach with existing methods that combine curriculum learning and reinforcement learning. The Introduction and Related Work sections highlight the specific contributions and limitations of existing methods. The experimental section provides empirical comparisons.
   - Supporting quotes: "However, these initial efforts primarily rely on simplified strategies... In contrast, we introduce E2H Reasoner... a CRL approach with a probabilistic scheduler..." and the claims made in the Introduction and Related Work sections.
   - Impact assessment: The reviewer's claim is partially valid. While the core idea of combining curriculum learning and RL is not entirely novel, the specific implementation (E2H Reasoner with its probabilistic schedulers and theoretical analysis) and its empirical validation constitute a novel contribution. The paper could strengthen its articulation of these novel aspects.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper claims novelty in the specific implementation and theoretical analysis, but could more clearly articulate the unique aspects compared to existing combinations of curriculum learning and RL.

**Review 3**

1. Weakness Statement:
"The paper's theoretical analysis relies on assumptions that may not hold in practical scenarios, such as the bounded distribution shift and the assumption of a well-defined curriculum. Specifically, the assumption of a bounded distribution shift between consecutive tasks is a strong one, as it requires a careful selection of intermediate tasks to ensure that the agent can smoothly transition between them. The paper does not provide a clear methodology for how to achieve this in practice, and it is unclear how sensitive the method is to violations of this assumption. Furthermore, the assumption of a well-defined curriculum, where the difficulty of tasks is clearly ordered, may not always be the case in real-world scenarios, and the paper does not discuss how the method would perform with a less structured curriculum."

2. Evidence Collection:
a) Method-related Evidence:
   - Section 3.3 "Theoretical Analysis" states: "The action-value function of a policy π \pi at step k k , i.e. , ‖ Q k ∗ − Q π k + 1 ‖ ∞ ≤ δ k ."
   - The paper defines δ k as the per-task Bellman error.
   - The paper defines the bounded curriculum drift condition: "Assume that μ k ≤ δ k for all k ."
   - The paper acknowledges the importance of task decomposition: "For tasks like Blocksworld, MATH, and Countdown, we use human-aligned difficulty signals... For others like AQuA and GSM8K, where such annotations are unavailable, we automatically estimate difficulty based on model error rates under CoT prompting..."
   - The paper does not explicitly detail a methodology for achieving bounded distribution shift in practice beyond the probabilistic schedulers.

3. Literature Gap Analysis:
   - The paper cites Chen and Maguluri (2025) for the theoretical analysis.

4. Validation Analysis:
   - Primary evidence summary: The reviewer correctly points out the assumptions made in the theoretical analysis, particularly the bounded distribution shift and the well-defined curriculum. The paper acknowledges the importance of task decomposition but doesn't provide a detailed methodology for ensuring bounded distribution shift in practice. The sensitivity to violations of these assumptions is not discussed.
   - Supporting quotes: "The action-value function of a policy π \pi at step k k , i.e. , ‖ Q k ∗ − Q π k + 1 ‖ ∞ ≤ δ k ." and "Assume that μ k ≤ δ k for all k ."
   - Impact assessment: The reviewer's criticism is valid. The paper relies on assumptions that might not always hold, and the practical implications of these assumptions are not fully explored.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The stated assumptions in the theoretical analysis and the lack of a detailed methodology for achieving bounded distribution shift support the reviewer's claim.

1. Weakness Statement:
"The empirical evaluation is limited to a small set of reasoning tasks, and it is unclear how well the proposed method would generalize to other types of tasks or domains. The tasks used in the evaluation, such as Blocksworld and Countdown, are relatively simple and may not fully capture the complexities of real-world reasoning problems. The paper does not provide a detailed analysis of the types of reasoning skills that are learned by the proposed method, nor does it discuss how the method could be adapted to learn more complex reasoning skills. Additionally, the paper does not provide a clear comparison of the computational cost of the proposed method with existing approaches, making it difficult to assess its practical applicability."

2. Evidence Collection:
a) Experiment-related Evidence:
   - The Experiments section describes evaluations on Blocksworld, Countdown, MATH, and AQuA.
   - The paper mentions using Qwen 2.5/1.5B Instruct for experiments.
   - The paper reports the number of samples needed for convergence.
   - The paper does not provide a detailed analysis of the specific reasoning skills learned.
   - The paper does not explicitly compare the computational cost with existing approaches.

3. Literature Gap Analysis:
   - The paper compares against several baselines in the experiments.

4. Validation Analysis:
   - Primary evidence summary: The reviewer's points are valid. The empirical evaluation is limited to a specific set of reasoning tasks. The paper lacks a detailed analysis of the learned reasoning skills and a comparison of computational costs.
   - Supporting quotes: The "Experiments" section details the specific tasks used. The results section reports sample complexity but not computational cost.
   - Impact assessment: The limited scope of the empirical evaluation and the lack of computational cost analysis are valid weaknesses.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The limited number of tasks in the experiments and the absence of computational cost analysis support the reviewer's claim.

1. Weakness Statement:
"The paper does not provide a detailed discussion of the limitations of the proposed method, such as its sensitivity to hyperparameter settings or its robustness to noisy or incomplete data. The paper also does not discuss the potential ethical implications of using the proposed method, such as the risk of overfitting to specific types of problems or the potential for bias in the learned reasoning skills. A more thorough discussion of these limitations would help to provide a more balanced and realistic assessment of the proposed method."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions hyperparameters for the Cosine and Gaussian schedulers (β, σ, α).
   - The paper does not include a detailed discussion of hyperparameter sensitivity.
   - The paper does not explicitly discuss robustness to noisy or incomplete data.
   - The paper does not discuss potential ethical implications.

3. Literature Gap Analysis:
   - Not applicable.

4. Validation Analysis:
   - Primary evidence summary: The reviewer correctly points out the absence of a detailed discussion on the limitations of the proposed method, including hyperparameter sensitivity, robustness, and ethical implications.
   - Supporting quotes: The method section introduces hyperparameters without discussing their impact.
   - Impact assessment: The lack of a detailed discussion of limitations is a valid weakness.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The absence of a dedicated section or detailed discussion on limitations supports the reviewer's claim.

**Review 4**

1. Weakness Statement:
"The motivation for the method is unclear. The authors mention that the proposed method is inspired by curriculum learning and reinforcement learning, but the connection between these two areas is not well-established. Specifically, the paper does not clearly articulate why a reinforcement learning framework is necessary for curriculum learning in the context of LLMs, especially given that the tasks are pre-defined and the learning process is primarily focused on improving performance on these tasks. The paper needs to better justify the choice of a reinforcement learning framework over simpler curriculum learning strategies that do not involve reward functions."

2. Evidence Collection:
   - This is the same weakness as Reviewer 2's first point. Please see the analysis for Reviewer 2's first point.

3. Literature Gap Analysis:
   - Same as Reviewer 2's first point.

4. Validation Analysis:
   - Same as Reviewer 2's first point.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 2's first point.

1. Weakness Statement:
"The proposed method is not novel. The method is a combination of curriculum learning and reinforcement learning, which is not a new idea. The paper does not sufficiently highlight the unique aspects of their approach compared to existing methods that combine these two areas. The specific implementation details and the theoretical analysis are not presented in a way that clearly distinguishes the proposed method from existing approaches. The paper needs to provide a more detailed comparison to existing methods and clearly articulate the novel contributions of their approach."

2. Evidence Collection:
   - This is the same weakness as Reviewer 2's second point. Please see the analysis for Reviewer 2's second point.

3. Literature Gap Analysis:
   - Same as Reviewer 2's second point.

4. Validation Analysis:
   - Same as Reviewer 2's second point.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: Same as Reviewer 2's second point.

1. Weakness Statement:
"The paper should provide a more detailed explanation of why a reinforcement learning framework is necessary for curriculum learning in the context of LLMs. The authors should clarify the specific advantages of using reinforcement learning over simpler curriculum learning strategies, especially given that the tasks are pre-defined. For example, they could discuss how the reinforcement learning framework allows for more adaptive task selection or how it can handle situations where the optimal curriculum is not known a priori. The paper should also provide a more detailed comparison to existing methods that combine curriculum learning and reinforcement learning. The authors should clearly articulate the novel contributions of their approach and provide a more detailed analysis of the differences between their method and existing approaches. This could include a discussion of the specific implementation details and the theoretical analysis that distinguishes their method from existing approaches. The paper should also provide a more detailed explanation of the task decomposition strategies used for tasks without human-annotated difficulty levels. The authors should explain how they estimate difficulty using the zero-shot error rate of the base model and how this information is used to define the curriculum. The paper should also provide a more detailed analysis of the experimental results, including a discussion of the limitations of the proposed method and potential directions for future research. This could include a discussion of the computational cost of the proposed method and how it scales with the number of tasks and the complexity of the tasks."

2. Evidence Collection:
   - This is a combination of several points already addressed. Please refer to the validation for Reviewer 2's first and second points, and Reviewer 3's first point.

3. Literature Gap Analysis:
   - Same as Reviewer 2's second point.

4. Validation Analysis:
   - Same as Reviewer 2's first and second points, and Reviewer 3's first point.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: Same as Reviewer 2's first and second points, and Reviewer 3's first point.

1. Weakness Statement:
"The paper would benefit significantly from a more rigorous definition of 'reasoning ability' within the context of LLMs. Currently, the term is used somewhat loosely, making it difficult to assess the effectiveness of the proposed method. The authors should consider defining reasoning ability in terms of specific cognitive processes, such as multi-step inference, logical deduction, or problem-solving under uncertainty. This definition should then be used to evaluate the effectiveness of the proposed method. For example, they could measure the model's ability to solve problems that require a specific number of reasoning steps, or its performance on tasks that involve logical deduction. Furthermore, the authors should provide a more detailed analysis of how their method improves these specific aspects of reasoning, rather than simply showing overall performance gains. This would allow for a more nuanced understanding of the method's strengths and weaknesses."

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's first point. Please see the analysis for Reviewer 1's first point.

3. Literature Gap Analysis:
   - Same as Reviewer 1's first point.

4. Validation Analysis:
   - Same as Reviewer 1's first point.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: Same as Reviewer 1's first point.

1. Weakness Statement:
"To address the lack of clarity regarding difficulty levels, the authors should provide a more detailed explanation of the criteria used to determine these levels. Simply stating that difficulty is based on human-annotated difficulty scores or zero-shot error rates is insufficient. The authors should specify the exact algorithm or heuristic used to translate these scores into difficulty levels. For example, if human-annotated scores are used, they should describe how these scores are normalized or discretized to create distinct difficulty levels. Similarly, if zero-shot error rates are used, they should explain how these rates are used to define the boundaries between difficulty levels. Furthermore, the authors should justify why these specific criteria are appropriate for the tasks being considered. A more detailed explanation of the difficulty level determination process would enhance the reproducibility and credibility of the results. The authors should also consider exploring alternative methods for difficulty level determination, such as using model confidence scores or task completion rates, and compare their performance with the current approach."

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's second point. Please see the analysis for Reviewer 1's second point.

3. Literature Gap Analysis:
   - Same as Reviewer 1's second point.

4. Validation Analysis:
   - Same as Reviewer 1's second point.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1's second point.

1. Weakness Statement:
"Finally, the authors need to provide a more detailed explanation of the probabilistic scheduler and its design choices. The current description is too high-level, and it is unclear how the scheduler is designed to effectively sample tasks from different difficulty levels. The authors should provide a mathematical formulation of the scheduler, including the specific parameters and their impact on the sampling distribution. They should also justify why the chosen scheduler is effective in improving the reasoning ability of LLMs. For example, they could explain how the scheduler encourages the model to start with easier tasks and gradually progress to more difficult ones. Furthermore, the authors should compare their scheduler with other existing curriculum learning methods, highlighting the advantages and disadvantages of their approach. This would provide a more comprehensive understanding of the proposed method's contribution to the field."

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's third point. Please see the analysis for Reviewer 1's third point.

3. Literature Gap Analysis:
   - Same as Reviewer 1's third point.

4. Validation Analysis:
   - Same as Reviewer 1's third point.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1's third point.

1. Weakness Statement:
"1. How is the difficulty level determined in your method?"

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's second point. Please see the analysis for Reviewer 1's second point.

3. Literature Gap Analysis:
   - Same as Reviewer 1's second point.

4. Validation Analysis:
   - Same as Reviewer 1's second point.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1's second point.

1. Weakness Statement:
"2. How is the probabilistic scheduler designed in your method?"

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's third point. Please see the analysis for Reviewer 1's third point.

3. Literature Gap Analysis:
   - Same as Reviewer 1's third point.

4. Validation Analysis:
   - Same as Reviewer 1's third point.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1's third point.

1. Weakness Statement:
"3. How is your method different from existing curriculum learning methods?"

2. Evidence Collection:
   - This is the same weakness as Reviewer 2's second point. Please see the analysis for Reviewer 2's second point.

3. Literature Gap Analysis:
   - Same as Reviewer 2's second point.

4. Validation Analysis:
   - Same as Reviewer 2's second point.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: Same as Reviewer 2's second point.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces E2H Reasoner (E2H-Reasoner), a curriculum reinforcement learning (CRL) method designed to enhance the reasoning capabilities of large language models (LLMs). The core idea is to gradually increase the difficulty of tasks during training, allowing the model to learn core reasoning abilities and generalize to more complex problems. The authors propose a probabilistic scheduler that adaptively samples tasks from different difficulty levels, aiming to improve learning efficiency and sample complexity. The method is evaluated on five reasoning tasks, including Blocksworld, Countdown, MATH, AQuA, and GSM8K, demonstrating significant performance improvements over existing methods. The paper also provides a theoretical analysis, establishing finite-sample complexity bounds and showing that the proposed method requires fewer total samples than direct learning. The authors frame the reasoning process of LLMs as a reinforcement learning problem, defining the state space, action space, transition kernel, reward function, and discount factor. The task decomposition is achieved through human-aligned difficulty signals or automatically estimated difficulty based on model error rates under Chain-of-Thought (CoT) prompting. The paper contrasts its approach with traditional RL post-training methods, highlighting the limitations of these methods in learning reasoning abilities. The authors claim that their method is more effective in preventing overfitting and enabling the model to generalize to more complex problems by gradually shifting focus from easy to hard tasks. The paper's main contribution lies in the proposed CRL method, the probabilistic scheduler, and the theoretical analysis of sample complexity. The empirical results show that E2H-Reasoner outperforms existing methods on the chosen reasoning tasks, suggesting that the proposed approach is a promising direction for enhancing the reasoning capabilities of LLMs. However, the paper also has some limitations, such as the reliance on bounded distribution shift assumptions and the limited scope of the empirical evaluation. Despite these limitations, the paper presents a valuable contribution to the field of LLM reasoning and provides a solid foundation for future research.


## Soundness:

2.5


## Presentation:

2.75


## Contribution:

2.25


## Strengths:

I found several aspects of this paper to be commendable. The core idea of using a curriculum reinforcement learning approach to enhance the reasoning abilities of LLMs is both intuitive and well-motivated. The authors clearly articulate the limitations of existing RL post-training methods and propose a method that addresses these limitations by gradually increasing the difficulty of tasks. The introduction of a probabilistic scheduler that adaptively samples tasks from different difficulty levels is a significant contribution. This approach allows the model to learn core reasoning abilities and generalize to more complex problems more efficiently. The paper also provides a theoretical analysis of the proposed method, establishing finite-sample complexity bounds and demonstrating that the method requires fewer total samples than direct learning. This theoretical grounding adds credibility to the proposed approach. The empirical results presented in the paper are also compelling. The authors demonstrate that E2H-Reasoner outperforms existing methods on five reasoning tasks, including Blocksworld, Countdown, MATH, AQuA, and GSM8K. These results provide strong evidence for the effectiveness of the proposed method. The paper is also well-written and easy to follow, making it accessible to a broad audience. The authors clearly explain the methodology, the theoretical analysis, and the empirical results. The use of a reinforcement learning framework to model the reasoning process of LLMs is a novel approach that provides a solid foundation for future research in this area. The paper's focus on preventing overfitting by gradually shifting focus from easy to hard tasks is also a valuable contribution. Overall, I believe that this paper presents a significant advancement in the field of LLM reasoning and provides a valuable contribution to the research community.


## Weaknesses:

While I appreciate the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, the paper's theoretical analysis relies on the assumption of a bounded distribution shift between consecutive tasks. Specifically, the paper assumes that the distribution shift between tasks is bounded by a parameter δk, and that the difficulty of tasks is well-ordered. This assumption is not always realistic in real-world scenarios, and the paper does not provide a clear methodology for achieving this in practice. The paper does not discuss how the method would perform with a less structured curriculum or if the tasks are not well-ordered. Furthermore, the paper does not provide a detailed analysis of the sensitivity of the method to violations of this assumption. This is a significant limitation because it is unclear how the method would perform in more complex or less structured environments. My confidence in this weakness is high, as the paper explicitly states the bounded distribution shift assumption and does not provide any mitigation strategies or analysis of its sensitivity. Second, the empirical evaluation is limited to a small set of reasoning tasks. While the paper evaluates the method on five tasks, including Blocksworld, Countdown, MATH, AQuA, and GSM8K, these tasks may not fully capture the complexities of real-world reasoning problems. The paper does not provide a detailed analysis of the types of reasoning skills that are learned by the proposed method, nor does it discuss how the method could be adapted to learn more complex reasoning skills. The paper also does not provide a detailed comparison of the computational cost of the proposed method with existing approaches, making it difficult to assess its practical applicability. My confidence in this weakness is high, as the paper explicitly lists the five tasks used in the experiments and does not provide any analysis of the computational cost. Third, the paper does not provide a detailed discussion of the limitations of the proposed method, such as its sensitivity to hyperparameter settings or its robustness to noisy or incomplete data. The paper mentions hyperparameters for the Cosine and Gaussian schedulers (β, σ, α) but does not discuss how these parameters are chosen or how sensitive the method is to their values. The paper also does not discuss how the method would perform with noisy or incomplete data. This lack of discussion is a significant limitation because it is important to understand the practical implications of the proposed method. My confidence in this weakness is high, as the paper does not include a dedicated section or detailed discussion on limitations. Finally, while the paper claims novelty in its specific implementation and theoretical analysis, the core idea of combining curriculum learning and reinforcement learning is not entirely new. The paper does not sufficiently highlight the unique aspects of their approach compared to existing methods that combine these two areas. The specific implementation details and the theoretical analysis are not presented in a way that clearly distinguishes the proposed method from existing approaches. My confidence in this weakness is medium, as the paper does claim novelty in the specific implementation and theoretical analysis, but could more clearly articulate the unique aspects compared to existing combinations of curriculum learning and RL.


## Suggestions:

To address the identified weaknesses, I recommend several improvements. First, the paper should provide a more detailed discussion of the assumptions underlying the theoretical analysis and how these assumptions might affect the practical performance of the proposed method. Specifically, the authors should provide a more rigorous analysis of the sensitivity of the method to violations of the bounded distribution shift assumption. They should also discuss how the method could be adapted to handle more complex or less structured environments. This could involve exploring alternative methods for selecting intermediate tasks or developing techniques for automatically generating a suitable curriculum. Second, the paper should expand the empirical evaluation to include a wider range of reasoning tasks, including more complex and realistic problems. This could involve using benchmark datasets from areas such as natural language understanding, common-sense reasoning, or mathematical problem-solving. The authors should also provide a more detailed analysis of the types of reasoning skills that are learned by the proposed method and discuss how the method could be adapted to learn more complex reasoning skills. This could involve exploring different reward functions or using more sophisticated task decomposition techniques. Third, the paper should include a more detailed discussion of the limitations of the proposed method, such as its sensitivity to hyperparameter settings and its robustness to noisy or incomplete data. The authors should also discuss the computational cost of the proposed method and how it scales with the number of tasks and the complexity of the tasks. This could involve comparing the computational cost of the proposed method with existing approaches and providing guidelines for choosing appropriate hyperparameters for different tasks and datasets. Finally, the paper should provide a more detailed comparison to existing methods that combine curriculum learning and reinforcement learning. The authors should clearly articulate the novel contributions of their approach and provide a more detailed analysis of the differences between their method and existing approaches. This could include a discussion of the specific implementation details and the theoretical analysis that distinguishes their method from existing approaches. The paper should also provide a more detailed explanation of the task decomposition strategies used for tasks without human-annotated difficulty levels. The authors should explain how they estimate difficulty using the zero-shot error rate of the base model and how this information is used to define the curriculum. These improvements would significantly strengthen the paper and make it more useful to the broader research community.


## Questions:

I have several questions that I would like to see addressed. First, how does the proposed method handle tasks with unclear or overlapping difficulty levels? Could you provide more details on how the method determines task difficulty in such cases? Second, could you elaborate on the sensitivity of the method to hyperparameter settings? Are there specific hyperparameters that are particularly critical for performance, and how should they be tuned? Third, how does the proposed method compare to other curriculum learning approaches in terms of computational cost and scalability? What are the practical implications of the theoretical analysis for real-world applications? Fourth, how does the proposed method address tasks with incomplete or noisy data? What are the potential limitations of the method in such scenarios, and how could these limitations be mitigated? Fifth, how does the proposed method compare to other curriculum learning approaches in terms of computational cost and scalability? What are the practical implications of the theoretical analysis for real-world applications? Finally, how does the proposed method generalize to tasks that are significantly different from those used in the training set? Are there any limitations in terms of the diversity of tasks that the method can handle? These questions are important for understanding the limitations of the proposed method and for guiding future research in this area.


## Rating:

5.25


## Confidence:

3.0


## Decision:

Reject
}