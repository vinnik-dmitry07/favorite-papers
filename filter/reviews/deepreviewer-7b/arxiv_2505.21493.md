I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper proposes a new method for training LLMs using reinforcement learning with verifiable rewards, called VeriFree. The key idea is to move away from relying on an external verifier model and instead train the model to maximize the probability of generating the reference answer given the question and a reasoning trace. This is motivated by the limitations of current RL with verifiable rewards (RLVR) methods, which typically rely on an external verifier that can be costly to train and prone to reward hacking. The authors show that their proposed objective is equivalent to the RLVR objective under certain assumptions, but offers advantages in terms of reduced variance and computational cost. They also introduce a novel gradient estimator that leverages Rao-Blackwellization to further reduce variance. Empirically, VeriFree achieves strong performance on general reasoning benchmarks, outperforming existing RLVR methods and demonstrating its effectiveness in training LLMs for general reasoning tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper addresses an important problem in the field of LLM training, namely how to effectively train models for complex reasoning tasks without relying on expensive and potentially problematic external verifiers.
- The proposed method is well-motivated and theoretically grounded, with clear connections to the existing RLVR literature.
- The empirical results are compelling, demonstrating strong performance across multiple benchmarks and model sizes. The ablation studies provide valuable insights into the effectiveness of different components of the method.
- The paper is generally well-written and easy to follow, with clear explanations of the key concepts and technical details.

### Weaknesses

#### Some Related Works


#### comment

 - The paper primarily focuses on the single-answer setting, which may limit the applicability of the method to more complex reasoning tasks with multiple valid solutions. While the authors acknowledge this limitation, it would be valuable to see some discussion of potential extensions to handle such cases.
- The paper does not provide a detailed analysis of the computational cost of the proposed method, particularly in comparison to existing RLVR methods. A more thorough analysis of the computational trade-offs would be helpful for practitioners.
- The paper could benefit from a more in-depth discussion of the limitations of the proposed approach, particularly in scenarios where the reasoning trace may be noisy or incomplete. It would also be useful to explore the sensitivity of the method to different hyperparameter settings and provide guidance on how to choose appropriate values.
- The paper could benefit from a more detailed comparison with other related methods in the literature, particularly those that also aim to improve the efficiency and robustness of RL-based training. A more comprehensive analysis of the strengths and weaknesses of the proposed method in comparison to existing approaches would be valuable.

### Suggestions

The authors should consider expanding their discussion on handling multi-answer scenarios, perhaps by exploring methods such as sampling multiple reasoning traces and aggregating their probabilities, or by incorporating a mechanism to explicitly model the distribution of valid answers. This would significantly broaden the applicability of their method to a wider range of reasoning tasks. Furthermore, a more detailed analysis of the computational cost is needed, including a breakdown of the time and memory requirements for each step of the algorithm, and a comparison with existing RLVR methods. This analysis should also consider the impact of different model sizes and dataset sizes on the computational cost. It would also be beneficial to provide a more thorough discussion of the limitations of the proposed approach, particularly in scenarios where the reasoning trace may be noisy or incomplete. For example, the authors could investigate the robustness of their method to errors in the reasoning trace, and explore techniques to mitigate the impact of such errors. Additionally, a more detailed sensitivity analysis of the method to different hyperparameter settings is needed, along with practical guidance on how to choose appropriate values. This analysis should include a discussion of the trade-offs between different hyperparameter settings and their impact on the performance of the method.

To further strengthen the paper, the authors should provide a more comprehensive comparison with other related methods in the literature, particularly those that also aim to improve the efficiency and robustness of RL-based training. This comparison should not only focus on the performance of the methods but also on their computational cost, robustness to noisy data, and ease of implementation. A more detailed discussion of the similarities and differences between the proposed method and existing approaches would help to clarify the unique contributions of this work. For example, the authors could compare their method with other approaches that use variational inference or other techniques to reduce the variance of the gradient estimator. This would help to highlight the advantages and disadvantages of the proposed method compared to other state-of-the-art techniques.

Finally, the authors should consider exploring the potential for combining their method with other techniques, such as knowledge distillation or multi-task learning, to further improve the performance and robustness of the model. This could involve using the proposed method to train a base model, and then using knowledge distillation to transfer the knowledge to a smaller, more efficient model. Alternatively, the authors could explore the use of multi-task learning to train a model that can perform multiple reasoning tasks simultaneously. This would help to demonstrate the versatility and potential of the proposed method for a wider range of applications.

### Questions

- How does the performance of VeriFree scale with the size of the reasoning trace?
- How sensitive is VeriFree to the quality of the reasoning trace? What happens if the trace contains errors or is incomplete?
- How does the computational cost of VeriFree compare to existing RLVR methods, particularly in terms of training time and memory usage?
- Can the authors provide more details on the choice of hyperparameters and their impact on the performance of VeriFree?

### Rating

6

### Confidence

3

**********

## Reviewer 2

### Summary

This paper proposes a new method for training LLMs with RL on verifiable rewards. The main idea is to replace the verifier with the model itself. The authors propose a new objective function and a corresponding gradient estimator. Experiments show that the proposed method outperforms previous methods on several benchmarks.

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

 - The paper lacks a comparison with RL on rule-based rewards. The authors should compare their method with RL on rule-based rewards on benchmarks like GPQA and MMLU-Pro. This comparison would help to understand the trade-offs between the two approaches.
- The paper does not discuss the limitations of the proposed method. For example, the authors should discuss the potential for the model to generate incorrect reasoning traces and how this could affect the performance of the method.
- The paper does not provide a detailed analysis of the computational cost of the proposed method. The authors should provide a comparison of the training time and memory usage of their method with previous methods.

### Suggestions

The paper would benefit from a more thorough comparison with RL methods that utilize rule-based rewards. Specifically, the authors should evaluate their method on benchmarks like GPQA and MMLU-Pro, which are commonly used to assess reasoning capabilities. This comparison should not only focus on the final performance but also analyze the learning curves and the sample efficiency of each method. It would be valuable to understand how the proposed method compares to RL with rule-based rewards in terms of convergence speed and the ability to generalize to unseen examples. Furthermore, the authors should investigate the impact of different rule-based reward functions on the performance of RL methods, as this could provide insights into the robustness of their approach. This analysis should also include a discussion of the potential for reward hacking in RL with rule-based rewards, and how the proposed method addresses this issue.

In addition to the comparison with rule-based RL, the paper should also include a more detailed discussion of the limitations of the proposed method. One key limitation is the potential for the model to generate incorrect reasoning traces. The authors should investigate the frequency of such errors and their impact on the overall performance. It would be beneficial to analyze the types of errors that the model makes and to explore techniques to mitigate these errors. For example, the authors could consider using a verification mechanism to filter out incorrect reasoning traces or to correct them automatically. Furthermore, the authors should discuss the potential for the model to overfit to the training data and to generalize poorly to unseen examples. This discussion should include an analysis of the model's sensitivity to different training data sizes and compositions.

Finally, the paper should provide a more detailed analysis of the computational cost of the proposed method. The authors should compare the training time and memory usage of their method with previous methods, including both RL with verifiable rewards and RL with rule-based rewards. This comparison should be performed on different hardware configurations to provide a more comprehensive understanding of the computational requirements of the proposed method. The authors should also discuss the scalability of their method to larger models and datasets. It would be valuable to understand how the computational cost of the proposed method scales with the size of the model and the dataset. This analysis should include a discussion of the potential for parallelizing the training process to reduce the overall training time.

### Questions

- How does the proposed method compare with RL on rule-based rewards on benchmarks like GPQA and MMLU-Pro?
- What are the limitations of the proposed method?
- What is the computational cost of the proposed method?

### Rating

6

### Confidence

4

**********

## Reviewer 3

### Summary

This paper proposes a method to train LLMs on tasks where there is no clear verification signal, such as general reasoning tasks. The method is based on the idea that the LLM should learn to generate reasoning traces that lead to the correct answer. The authors propose a new objective function that does not require a separate verifier model and derive a gradient estimator that is equivalent to the one proposed in Tang et al. (2023) but with lower variance. The method is evaluated on a variety of reasoning benchmarks, including MMLU-Pro, SuperGPQA, and GPQA, and compared against a number of baselines. The results show that the proposed method outperforms the baselines and achieves state-of-the-art performance on these benchmarks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper addresses an important problem: how to train LLMs on tasks where there is no clear verification signal. This is a challenging problem that is relevant to many real-world applications of LLMs.
- The proposed method is theoretically sound and well-motivated. The authors provide a clear explanation of the method and its connection to existing work.
- The empirical results are strong and demonstrate the effectiveness of the proposed method. The method outperforms the baselines on a variety of benchmarks and achieves state-of-the-art performance.

### Weaknesses

#### Some Related Works


#### comment

 - The paper focuses on general reasoning tasks, but it is not clear how the method would perform on tasks that require more complex reasoning, such as multi-hop reasoning or logical inference. It would be useful to see some discussion of the limitations of the method and how it could be extended to handle more complex reasoning tasks.
- The method requires a large amount of training data, which may not be available for all tasks. It would be useful to see some discussion of how the method could be adapted to work with smaller datasets.
- The paper does not discuss the computational cost of the method. It would be useful to see some analysis of the computational requirements of the method and how it compares to other methods.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations of the proposed method, particularly regarding its applicability to more complex reasoning tasks. While the current benchmarks demonstrate strong performance, it is crucial to acknowledge that real-world reasoning often involves multi-hop inference, logical deduction, and scenarios requiring common-sense understanding. The authors should consider including experiments on datasets that specifically test these capabilities, such as those involving chain-of-thought reasoning or symbolic manipulation. Furthermore, a discussion on how the method might be adapted to handle such tasks would be valuable. For instance, could the reasoning traces be made more structured to facilitate multi-hop reasoning, or could the model be trained to generate intermediate logical steps? Addressing these points would significantly strengthen the paper's contribution and provide a more comprehensive understanding of the method's potential and limitations.

Another important aspect to consider is the data efficiency of the proposed method. The reliance on large datasets for training is a common challenge in many machine learning applications, and it is particularly relevant for complex reasoning tasks. The authors should explore techniques to reduce the data requirements of their approach. This could involve investigating data augmentation strategies, curriculum learning, or methods that leverage weak supervision signals. For example, could the model be pre-trained on a large corpus of text and then fine-tuned on the target reasoning tasks? Or could the model be trained to generate plausible reasoning traces even when the ground truth is not available? Exploring these avenues would make the method more practical and accessible to researchers with limited computational resources. Additionally, a detailed analysis of the computational cost, including training time and memory requirements, is essential for assessing the feasibility of the method in real-world scenarios. This analysis should compare the proposed method with existing approaches and discuss potential optimizations to reduce computational overhead.

Finally, the paper should provide more clarity on the practical implementation details of the proposed method. For example, how are the reasoning traces generated, and what are the specific parameters used for training? A more detailed description of the experimental setup, including the hardware used and the training procedure, would enhance the reproducibility of the results. Furthermore, it would be beneficial to include an ablation study to analyze the impact of different components of the method on its performance. For instance, how does the performance change when the variance reduction technique is removed? Such an analysis would provide valuable insights into the method's inner workings and help guide future research in this area. By addressing these points, the authors can make their work more accessible and impactful to the broader research community.

### Questions

- How does the method perform on tasks that require more complex reasoning, such as multi-hop reasoning or logical inference?
- How does the method scale to larger models and datasets?
- What is the computational cost of the method?

### Rating

6

### Confidence

4

**********

## Reviewer 4

### Summary

This paper introduces a new method called VeriFree for training large language models (LLMs) on general reasoning tasks, where traditional reinforcement learning with verifiable rewards (RLVR) is often impractical. VeriFree addresses the limitations of RLVR by eliminating the need for an external verifier model, which can be costly and prone to reward hacking. Instead, it leverages the LLM itself to maximize the probability of generating the correct answer given the reasoning trace and the question. This approach simplifies training and reduces computational overhead. The authors provide a theoretical analysis showing that VeriFree's gradient estimator has lower variance than existing methods, and they demonstrate its effectiveness through extensive experiments on multiple reasoning benchmarks, showing that it outperforms existing RLVR methods and achieves state-of-the-art performance.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces VeriFree, a novel method for training LLMs on general reasoning tasks without relying on an external verifier model. This is a significant contribution as it addresses the limitations of traditional RLVR methods, which are often impractical for general reasoning tasks due to the need for a robust verifier.
2. The authors provide a thorough theoretical analysis of VeriFree, demonstrating that it has a lower variance gradient estimator compared to existing methods. This theoretical grounding adds credibility to the proposed approach.
3. The empirical evaluation is comprehensive, covering multiple reasoning benchmarks and model sizes. The results show that VeriFree outperforms existing RLVR methods and achieves state-of-the-art performance, demonstrating its practical effectiveness.

### Weaknesses

#### Some Related Works


#### comment

1. While the paper demonstrates the effectiveness of VeriFree on several reasoning benchmarks, it would be beneficial to explore its performance on a wider range of tasks and datasets. This would provide a more comprehensive understanding of the method's generalizability and robustness.
2. The paper could benefit from a more detailed discussion of the computational cost associated with VeriFree. While the authors mention that it reduces the need for a verifier model, it would be helpful to quantify the computational savings and compare them with existing RLVR methods.
3. The paper could also explore the sensitivity of VeriFree to different hyperparameters and training configurations. A more thorough analysis of these factors would provide valuable insights into the practical applicability of the method.

### Suggestions

The authors should consider expanding their experimental evaluation to include a more diverse set of reasoning tasks. While the current benchmarks are valuable, they may not fully capture the complexities of real-world reasoning scenarios. For instance, incorporating tasks that require multi-hop reasoning, common-sense inference, or complex logical deductions would provide a more rigorous test of VeriFree's capabilities. Furthermore, evaluating the method on datasets with varying levels of noise or ambiguity would help to assess its robustness in less ideal conditions. This would involve not only testing on different datasets but also varying the complexity of the reasoning required by the tasks themselves. Such an analysis would provide a more complete picture of the method's strengths and limitations.

In addition to expanding the experimental evaluation, the authors should provide a more detailed analysis of the computational cost of VeriFree. While the paper mentions that the method reduces the need for a verifier model, it is crucial to quantify the actual computational savings. This should include a comparison of the training time, memory usage, and inference speed of VeriFree with existing RLVR methods. The analysis should also consider the impact of different model sizes and training configurations on the computational cost. For example, how does the training time scale with the number of parameters in the model? What is the memory footprint of the method during training and inference? Providing this information would allow practitioners to make informed decisions about the practical applicability of VeriFree. Furthermore, it would be beneficial to explore potential optimizations that could further reduce the computational cost of the method.

Finally, the authors should conduct a more thorough sensitivity analysis of VeriFree to different hyperparameters and training configurations. This should include a systematic exploration of the impact of various factors, such as the learning rate, batch size, and the number of training epochs. The analysis should also consider the effect of different training data sizes and compositions. For example, how does the performance of VeriFree change when trained on a smaller or larger dataset? How does the method perform when trained on a dataset with different types of reasoning tasks? Understanding the sensitivity of the method to these factors is crucial for its practical application. This analysis should also include a discussion of the optimal hyperparameter settings for different tasks and datasets.

### Questions

1. How does VeriFree perform on tasks that require multi-hop reasoning or common-sense inference?
2. What is the computational cost of VeriFree compared to existing RLVR methods, and how does it scale with model size and training data?
3. How sensitive is VeriFree to different hyperparameters and training configurations?

### Rating

8

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers for the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

**Plan:**
1. Go through each reviewer's identified weaknesses one by one.
2. For each weakness, identify if it's related to the method, experiments, or general aspects.
3. Find specific evidence from the paper (quotes, numbers, missing information) to support the reviewer's claim.
4. If the weakness is about missing comparisons or citations, identify the specific areas where the paper lacks.
5. Finally, conclude whether the weakness is valid, partially valid, or invalid based on the evidence.
**Review 1**

1. Weakness Statement:
"The paper primarily focuses on the single-answer setting, which may limit the applicability of the method to more complex reasoning tasks with multiple valid solutions. While the authors acknowledge this limitation, it would be valuable to see some discussion of potential extensions to handle such cases."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper states in the "main_idea" section: "VeriFree is designed to be versatile and can be applied to a wide range of tasks, including those with single correct answers and those with multiple valid answers." This suggests the method is intended for both scenarios.
   - The "method" section describes the objective function as maximizing the probability of the reference answer given the reasoning trace and question. This formulation inherently assumes a single reference answer.
b) Experiment-related Evidence:
   - The "experiments" section uses datasets like MMLU-Pro and SuperGPQA, which primarily have single correct answers.
   - The "ablation study" on "Effects of Equivalence Class" uses MATH-12k, which has multiple equivalent correct answers. This suggests the authors considered this.

3. Literature Gap Analysis:
   - The paper does not explicitly discuss the challenges of extending the method to tasks with multiple valid answers in detail.

4. Validation Analysis:
   - The reviewer is correct that the primary formulation of the objective function and the experimental setup focus on single correct answers. While the ablation study touches upon equivalence classes, a more thorough discussion of the limitations and potential extensions for multi-answer scenarios is missing.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The "main_idea" mentions both single and multiple answers, but the core method description and primary experiments focus on single answers.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost of the proposed method, particularly in comparison to existing RLVR methods. A more thorough analysis of the computational trade-offs would be helpful for practitioners."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "experiments" section mentions the hardware used: "All collected samples from each step are used for one optimization step. The training is conducted on a single node with 8 × H100 GPUs."
   - The "main_idea" mentions: "VeriFree is designed to be versatile and can be applied to a wide range of tasks, including those with single correct answers and those with multiple valid answers."
   - There is no explicit comparison of training time, memory usage, or computational cost with other methods.

3. Literature Gap Analysis:
   - The paper does not cite or compare against works that specifically analyze the computational cost of RLVR methods.

4. Validation Analysis:
   - The reviewer's point is valid. While the paper mentions the hardware used, it lacks a detailed analysis and comparison of the computational cost of VeriFree with existing RLVR methods.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "experiments" section lacks a computational cost analysis, and the paper does not compare against other methods in this regard.

1. Weakness Statement:
"The paper could benefit from a more in-depth discussion of the limitations of the proposed approach, particularly in scenarios where the reasoning trace may be noisy or incomplete. It would also be useful to explore the sensitivity of the method to different hyperparameter settings and provide guidance on how to choose appropriate values."

2. Evidence Collection:
a) Method-related Evidence:
   - The "main_idea" mentions: "VeriFree is designed to be versatile and can be applied to a wide range of tasks, including those with single correct answers and those with multiple valid answers." This implies awareness of potential limitations.
   - The "method" section describes the gradient estimator, but doesn't explicitly discuss its robustness to noisy or incomplete traces.
b) Experiment-related Evidence:
   - The "experiments" section includes an ablation study on the "Effect of RLOO" and "Effects of Token Split," which touches upon some aspects of robustness.
   - There is no explicit discussion on the sensitivity to hyperparameters or guidance on choosing appropriate values.

3. Literature Gap Analysis:
   - The paper does not cite works that specifically analyze the robustness of RL methods to noisy or incomplete traces.

4. Validation Analysis:
   - The reviewer's point is valid. The paper lacks a detailed discussion on the limitations related to noisy or incomplete reasoning traces and a thorough analysis of hyperparameter sensitivity.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks explicit discussion and experiments on the impact of noisy or incomplete traces and a detailed hyperparameter sensitivity analysis.

1. Weakness Statement:
"The paper could benefit from a more detailed comparison with other related methods in the literature, particularly those that also aim to improve the efficiency and robustness of RL-based training. A more comprehensive analysis of the strengths and weaknesses of the proposed method in comparison to existing approaches would help to clarify the unique contributions of this work."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "experiments" section includes comparisons with several baselines, including "Verifier" (RL with a model-based verifier), "Dr. GRPO," "Natural Reasoner," and "General-Reasoner-7B-SimpleRL-Zoo."
   - The "Related Works" section discusses DeepSeek-R1-Zero-like reinforcement learning and other methods using verifier models.
3. Literature Gap Analysis:
   - While the paper compares against several baselines, the comparison could be more detailed, especially regarding the efficiency and robustness aspects mentioned by the reviewer.

4. Validation Analysis:
   - The reviewer's point is partially valid. The paper does compare against several relevant baselines, but a more in-depth analysis of the strengths and weaknesses concerning efficiency and robustness would be beneficial.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper includes comparisons, but the depth of analysis regarding efficiency and robustness could be improved.

**Review 2**

1. Weakness Statement:
"The paper lacks a comparison with RL on rule-based rewards. The authors should compare their method with RL on rule-based rewards on benchmarks like GPQA and MMLU-Pro. This comparison would help to understand the trade-offs between the two approaches."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "experiments" section includes "Natural Reasoner" as a baseline, which is a form of RL with a rule-based reward ( verifier model).
   - The paper does not explicitly compare against RL with rule-based rewards using explicit reward functions, without a separate verifier model.

3. Literature Gap Analysis:
   - The paper does not cite or compare against works that specifically focus on RL with rule-based rewards without a separate verifier.

4. Validation Analysis:
   - The reviewer is partially correct. The paper compares against a verifier-based RL method ("Natural Reasoner"), but a direct comparison with RL using explicit rule-based rewards (without a separate verifier) is missing.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper includes a verifier-based RL baseline but lacks a direct comparison with RL using explicit rule-based rewards.

1. Weakness Statement:
"The paper does not discuss the limitations of the proposed method. For example, the authors should discuss the potential for the model to generate incorrect reasoning traces and how this could affect the performance of the method."

2. Evidence Collection:
a) Method-related Evidence:
   - The "main_idea" mentions: "VeriFree is designed to be versatile and can be applied to a wide range of tasks, including those with single correct answers and those with multiple valid answers." This suggests the method is intended for both scenarios.
   - The "method" section describes the objective function as maximizing the probability of the reference answer given the reasoning trace and question. This formulation inherently assumes a single reference answer.
b) Experiment-related Evidence:
   - The "experiments" section uses datasets like MMLU-Pro and SuperGPQA, which primarily have single correct answers.
   - The "ablation study" on "Effects of Equivalence Class" uses MATH-12k, which has multiple equivalent correct answers. This suggests the authors considered this.

3. Literature Gap Analysis:
   - The paper does not explicitly discuss the challenges of extending the method to tasks with multiple valid answers in detail.

4. Validation Analysis:
   - The reviewer is correct. The paper lacks a detailed discussion on the limitations related to the generation of incorrect reasoning traces and how this could affect the performance, especially in scenarios with multiple valid answers.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks explicit discussion and experiments on the impact of incorrect reasoning traces.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost of the proposed method. It would be useful to see some analysis of the computational requirements of the method and how it compares to previous methods."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "experiments" section mentions the hardware used: "All collected samples from each step are used for one optimization step. The training is conducted on a single node with 8 × H100 GPUs."
   - The "main_idea" mentions: "VeriFree is designed to be versatile and can be applied to a wide range of tasks, including those with single correct answers and those with multiple valid answers."
   - There is no explicit comparison of training time, memory usage, or computational cost with other methods.

3. Literature Gap Analysis:
   - The paper does not cite or compare against works that specifically analyze the computational cost of RLVR methods.

4. Validation Analysis:
   - The reviewer's point is valid. The paper lacks a detailed analysis and comparison of the computational cost of VeriFree with existing RLVR methods.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "experiments" section lacks a computational cost analysis, and the paper does not compare against other methods in this regard.

1. Weakness Statement:
"The paper does not discuss the limitations of the proposed method, particularly in scenarios where the reasoning trace may be noisy or incomplete. It would be beneficial to investigate the robustness of their method to errors in the reasoning trace, and explore techniques to mitigate the impact of such errors."

2. Evidence Collection:
a) Method-related Evidence:
   - The "main_idea" mentions: "VeriFree is designed to be versatile and can be applied to a wide range of tasks, including those with single correct answers and those with multiple valid answers." This suggests the method is intended for both scenarios.
   - The "method" section describes the objective function as maximizing the probability of the reference answer given the reasoning trace and question. This formulation inherently assumes a single reference answer.
b) Experiment-related Evidence:
   - The "experiments" section uses datasets like MMLU-Pro and SuperGPQA, which primarily have single correct answers.
   - The "ablation study" on "Effects of Equivalence Class" uses MATH-12k, which has multiple equivalent correct answers. This suggests the authors considered this.

3. Literature Gap Analysis:
   - The paper does not explicitly discuss the challenges of extending the method to tasks with multiple valid answers in detail.

4. Validation Analysis:
   - The reviewer is correct. The paper lacks a detailed discussion on the limitations related to the generation of incorrect reasoning traces and how this could affect the performance, especially in scenarios with multiple valid answers.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks explicit discussion and experiments on the impact of noisy or incomplete traces and a detailed hyperparameter sensitivity analysis.

1. Weakness Statement:
"Finally, the paper should provide a more detailed analysis of the computational cost of the proposed method. The authors should compare the training time and memory usage of their method with previous methods, including both RL with verifiable rewards and RL with rule-based rewards. This analysis should be performed on different hardware configurations to provide a more comprehensive understanding of the computational requirements of the proposed method. The authors should also discuss the scalability of their method to larger models and datasets. It would be valuable to understand how the computational cost of the proposed method scales with the size of the model and the dataset. This analysis should include a discussion of the potential for parallelizing the training process to reduce the overall training time."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "experiments" section mentions the hardware used: "All collected samples from each step are used for one optimization step. The training is conducted on a single node with 8 × H100 GPUs."
   - The "main_idea" mentions: "VeriFree is designed to be versatile and can be applied to a wide range of tasks, including those with single correct answers and those with multiple valid answers."
   - There is no explicit comparison of training time, memory usage, or computational cost with other methods.

3. Literature Gap Analysis:
   - The paper does not cite or compare against works that specifically analyze the computational cost of RLVR methods.

4. Validation Analysis:
   - The reviewer's point is valid. The paper lacks a detailed analysis and comparison of the computational cost of VeriFree with existing RLVR methods.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "experiments" section lacks a computational cost analysis, and the paper does not compare against other methods in this regard.

**Review 3**

1. Weakness Statement:
"The paper focuses on general reasoning tasks, but it is not clear how the method would perform on tasks that require more complex reasoning, such as multi-hop reasoning or logical inference. It would be useful to see some discussion of the limitations of the method and how it could be extended to handle more complex reasoning tasks."

2. Evidence Collection:
a) Method-related Evidence:
   - The "main_idea" mentions: "VeriFree is designed to be versatile and can be applied to a wide range of tasks, including those with single correct answers and those with multiple valid answers." This suggests the method is intended for both scenarios.
   - The "method" section describes the objective function as maximizing the probability of the reference answer given the reasoning trace and question. This formulation inherently assumes a single reference answer.
b) Experiment-related Evidence:
   - The "experiments" section uses datasets like MMLU-Pro and SuperGPQA, which primarily have single correct answers.
   - The "ablation study" on "Effects of Equivalence Class" uses MATH-12k, which has multiple equivalent correct answers. This suggests the authors considered this.

3. Literature Gap Analysis:
   - The paper does not explicitly discuss the challenges of extending the method to tasks with multiple valid answers in detail.

4. Validation Analysis:
   - The reviewer is correct. The paper lacks a detailed discussion on the limitations related to the generation of incorrect reasoning traces and how this could affect the performance, especially in scenarios with multi-hop or logical inference.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks explicit discussion and experiments on the impact of noisy or incomplete traces and a detailed hyperparameter sensitivity analysis.

1. Weakness Statement:
"The method requires a large amount of training data, which may not be available for all tasks. It would be useful to see some discussion of how the method could be adapted to work with smaller datasets."

2. Evidence Collection:
a) Method-related Evidence:
   - The "method" section describes the objective function and gradient estimator, which are general and do not inherently require a large amount of data.
b) Experiment-related Evidence:
   - The "experiments" section uses datasets like MMLU-Pro and SuperGPQA, which are reasonably large.
   - There is no explicit discussion on the method's performance with smaller datasets.

3. Literature Gap Analysis:
   - The paper does not cite works that specifically address training with limited data in the context of RL or RLVR.

4. Validation Analysis:
   - The reviewer's point is valid. While the method itself doesn't inherently require large datasets, the paper lacks a discussion on its performance and potential adaptations for smaller datasets.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks a discussion on the method's performance with smaller datasets.

1. Weakness Statement:
"The paper does not discuss the computational cost of the method. It would be useful to see some analysis of the computational requirements of the method and how it compares to existing approaches."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "experiments" section mentions the hardware used: "All collected samples from each step are used for one optimization step. The training is conducted on a single node with 8 × H100 GPUs."
   - The "main_idea" mentions: "VeriFree is designed to be versatile and can be applied to a wide range of tasks, including those with single correct answers and those with multiple valid answers."
   - There is no explicit comparison of training time, memory usage, or computational cost with other methods.

3. Literature Gap Analysis:
   - The paper does not cite or compare against works that specifically analyze the computational cost of RLVR methods.

4. Validation Analysis:
   - The reviewer's point is valid. The paper lacks a detailed analysis and comparison of the computational cost of VeriFree with existing RLVR methods.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "experiments" section lacks a computational cost analysis, and the paper does not compare against other methods in this regard.

**Review 4**

1. Weakness Statement:
"While the paper demonstrates the effectiveness of VeriFree on several reasoning benchmarks, it would be beneficial to explore its performance on a wider range of tasks and datasets. This would provide a more comprehensive understanding of the method's generalizability and robustness."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "experiments" section uses datasets like MMLU-Pro, SuperGPQA, GPQA, MATH-500, OlympiadBench, Minerva Math, GSM8K, AMC, AIME24, MATH-500-SimpleRL, MATH-12k, and GPQA.

3. Literature Gap Analysis:
   - The paper does not explicitly discuss the limitations of the chosen datasets or the potential for evaluating on other types of reasoning tasks.

4. Validation Analysis:
   - The reviewer's point is partially valid. The paper uses a reasonable number of datasets, but exploring performance on a wider range of tasks and datasets could further strengthen the generalizability claims.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper uses several datasets, but expanding the range could provide more comprehensive evidence.

1. Weakness Statement:
"The paper could benefit from a more detailed discussion of the computational cost associated with VeriFree. While the authors mention that it reduces the need for a verifier model, it would be helpful to quantify the computational savings and compare them with existing RLVR methods."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "experiments" section mentions the hardware used: "All collected samples from each step are used for one optimization step. The training is conducted on a single node with 8 × H100 GPUs."
   - The "main_idea" mentions: "VeriFree is designed to be versatile and can be applied to a wide range of tasks, including those with single correct answers and those with multiple valid answers."
   - There is no explicit comparison of training time, memory usage, or computational cost with other methods.

3. Literature Gap Analysis:
   - The paper does not cite or compare against works that specifically analyze the computational cost of RLVR methods.

4. Validation Analysis:
   - The reviewer's point is valid. The paper lacks a detailed analysis and comparison of the computational cost of VeriFree with existing RLVR methods.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "experiments" section lacks a computational cost analysis, and the paper does not compare against other methods in this regard.

1. Weakness Statement:
"The paper could also explore the sensitivity of VeriFree to different hyperparameters and training configurations. A more thorough analysis of these factors would provide valuable insights into the practical applicability of the method."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "experiments" section includes an ablation study on "Effects of RLOO" and "Effects of Token Split."
   - There is no explicit discussion on the sensitivity to other hyperparameters or training configurations.

3. Literature Gap Analysis:
   - The paper does not cite works that specifically analyze the hyperparameter sensitivity of RLVR methods.

4. Validation Analysis:
   - The reviewer's point is valid. While the paper includes some ablation studies, a more thorough analysis of hyperparameter sensitivity is missing.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks a detailed hyperparameter sensitivity analysis.

**Synthesis and Reflection:**

Several reviewers raised overlapping concerns, primarily focusing on the lack of detailed analysis regarding computational cost and the limitations of the method in handling noisy or incomplete reasoning traces. Reviewers 1, 2, and 3 all explicitly mentioned the absence of a thorough computational cost analysis, comparing VeriFree with existing RLVR methods. Similarly, Reviewers 1 and 2 highlighted the need for a more in-depth discussion of the method's limitations, particularly concerning the impact of noisy or incomplete reasoning traces.

There's a consensus that while the empirical results are strong, the paper could benefit from a more comprehensive discussion of the practical considerations, such as computational resources and the robustness of the method under various conditions. Reviewer 4 also pointed out the need for exploring the method's performance on a wider range of tasks, which aligns with the idea of a more comprehensive evaluation.

A potential point of divergence is the interpretation of the paper's focus on single-answer settings. Reviewer 1's initial concern about the method's applicability to multi-answer scenarios is valid, as the core formulation and experiments primarily focus on single correct answers. However, the paper does acknowledge this limitation and suggests potential extensions in the ablation study.

Overall, the criticisms are largely valid and well-supported by the paper's content. The reviewers correctly identify areas where the paper could be strengthened through more detailed analysis, a broader discussion of limitations, and potentially additional experiments.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces VeriFree, a novel method for training large language models (LLMs) on general reasoning tasks, addressing a key challenge in reinforcement learning with verifiable rewards (RLVR). The core problem the authors tackle is the impracticality of using external verifier models for complex reasoning tasks, which often lack robustness and are themselves costly to train. VeriFree offers an alternative approach by eliminating the need for a separate verifier model. Instead, it leverages the LLM itself to maximize the probability of generating the correct answer given the reasoning trace and the question. This is achieved through a carefully designed objective function and a gradient estimator that reduces variance compared to existing methods. The authors provide a theoretical analysis showing that VeriFree's gradient estimator has lower variance than those used in previous RLVR methods, which is crucial for stable and efficient training. Empirically, the authors demonstrate the effectiveness of VeriFree through extensive experiments on multiple reasoning benchmarks, including MMLU-Pro, SuperGPQA, and GPQA, as well as mathematical reasoning datasets like MATH-500 and MATH-12k. The results show that VeriFree outperforms existing RLVR methods and achieves state-of-the-art performance on these benchmarks. The paper also includes ablation studies that provide valuable insights into the method's behavior, such as the impact of reward variance reduction and the use of equivalence classes. Overall, VeriFree presents a significant contribution to the field by offering a more practical and efficient approach to training LLMs for complex reasoning tasks, particularly in scenarios where external verifiers are not readily available or are unreliable. The method's ability to achieve strong performance without relying on a separate verifier model is a notable advancement, potentially opening new avenues for training LLMs on a wider range of reasoning tasks. The theoretical grounding and empirical validation of the method further enhance its significance, demonstrating its robustness and effectiveness across diverse reasoning scenarios.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

3.0


## Strengths:

I find several aspects of this paper to be particularly strong. First, the paper addresses a very important problem: how to effectively train LLMs on complex reasoning tasks without relying on expensive and potentially unreliable external verifier models. This is a significant challenge in the field, and VeriFree offers a compelling solution by using the LLM itself as a form of verifier. The core idea of maximizing the probability of the correct answer given the reasoning trace and the question is both elegant and effective. Second, the authors provide a solid theoretical foundation for their method. They demonstrate that the gradient estimator used in VeriFree has lower variance than existing methods, which is crucial for stable and efficient training. This theoretical grounding adds credibility to the proposed approach and provides a deeper understanding of its underlying mechanisms. Third, the empirical results are compelling. The authors conduct extensive experiments on a variety of reasoning benchmarks, including MMLU-Pro, SuperGPQA, and GPQA, as well as mathematical reasoning datasets. The results consistently show that VeriFree outperforms existing RLVR methods and achieves state-of-the-art performance on these benchmarks. This strong empirical validation provides further support for the effectiveness of the proposed method. Finally, the inclusion of ablation studies is a valuable contribution. The authors explore the impact of different components of the method, such as the use of equivalence classes and the reward variance reduction technique. These studies provide valuable insights into the method's behavior and help to understand the factors that contribute to its success. The paper is also generally well-written and easy to follow, with clear explanations of the key concepts and technical details. The authors provide sufficient background information and clearly articulate the motivation behind their work. The experimental setup is well-described, and the results are presented in a clear and concise manner. The inclusion of a detailed discussion of the limitations of the method is also commendable, as it demonstrates a thorough understanding of the proposed approach.


## Weaknesses:

Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, while the paper presents a novel method, it primarily focuses on single-answer reasoning tasks. While the authors acknowledge this limitation and include an ablation study on equivalence classes, a more thorough discussion of the method's applicability to tasks with multiple valid solutions is needed. The core formulation of the objective function and the experimental setup are designed for single correct answers, and the paper lacks a detailed analysis of how the method would perform in scenarios where multiple reasoning traces can lead to the same correct answer. This is a significant limitation, as many real-world reasoning tasks involve multiple valid solutions. The paper does not adequately address the potential for the model to generate incorrect reasoning traces, which could lead to suboptimal performance in such scenarios. This limitation is further compounded by the lack of a detailed discussion on the robustness of the method to noisy or incomplete reasoning traces. The paper does not explore how the method would handle cases where the reasoning trace contains errors or is incomplete, which is a common occurrence in real-world applications. This is a crucial oversight, as the reliability of the reasoning trace is essential for the method's success. Second, the paper lacks a detailed analysis of the computational cost of the proposed method. While the authors mention that VeriFree reduces the need for a verifier model, they do not provide a quantitative comparison of the training time and memory usage with existing RLVR methods. The paper mentions that the training is conducted on a single node with 8 × H100 GPUs, but this information is insufficient to assess the practical applicability of the method. A more thorough analysis of the computational requirements, including a comparison with both RL with verifiable rewards and RL with rule-based rewards, is needed. This analysis should also consider the impact of different model sizes and dataset sizes on the computational cost. The absence of this analysis makes it difficult to assess the practical trade-offs between VeriFree and existing approaches. Third, the paper does not provide a detailed discussion of the limitations of the proposed method, particularly in scenarios where the reasoning trace may be noisy or incomplete. While the ablation study touches upon equivalence classes, a more in-depth analysis of the method's sensitivity to different types of reasoning traces and its robustness to errors in the reasoning process is needed. The paper does not explore techniques to mitigate the impact of noisy or incomplete traces, such as data augmentation or curriculum learning. This lack of discussion is a significant oversight, as the reliability of the reasoning trace is essential for the method's success. Fourth, the paper does not adequately compare VeriFree with RL methods that utilize rule-based rewards. While the paper includes a baseline using a verifier model, it does not directly compare against RL with rule-based rewards using explicit reward functions, without a separate verifier model. This comparison is crucial to understand the trade-offs between the two approaches. The paper should evaluate VeriFree on benchmarks like GPQA and MMLU-Pro, which are commonly used to assess reasoning capabilities, and compare its performance with RL methods that use rule-based rewards. This comparison should not only focus on the final performance but also analyze the learning curves and the sample efficiency of each method. Finally, the paper does not provide sufficient guidance on how to choose appropriate hyperparameters and their impact on the performance of VeriFree. The paper mentions that the method is relatively insensitive to hyperparameters, but it does not include a discussion of the trade-offs between different hyperparameter settings and their impact on the performance of the method. A more thorough analysis of these factors is needed to guide practitioners in applying the method to different tasks and datasets. These weaknesses, while not invalidating the core contributions of the paper, highlight areas where further research and analysis are needed to fully realize the potential of VeriFree.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should extend their discussion on handling multi-answer scenarios. This could involve exploring methods such as sampling multiple reasoning traces and aggregating their probabilities, or incorporating a mechanism to explicitly model the distribution of valid answers. This would significantly broaden the applicability of their method to a wider range of reasoning tasks. Furthermore, a more detailed analysis of the computational cost is needed, including a breakdown of the time and memory requirements for each step of the algorithm, and a comparison with existing RLVR methods. This analysis should also consider the impact of different model sizes and dataset sizes on the computational cost. It would also be beneficial to provide a more thorough discussion of the limitations of the proposed approach, particularly in scenarios where the reasoning trace may be noisy or incomplete. For example, the authors could investigate the robustness of their method to errors in the reasoning trace, and explore techniques to mitigate the impact of such errors. This could involve using a verification mechanism to filter out incorrect reasoning traces or to correct them automatically. Additionally, the authors should discuss the potential for the model to generate incorrect reasoning traces and how this could affect the overall performance. This discussion should include an analysis of the types of errors that the model makes and to explore techniques to mitigate these errors. Second, the authors should include a more detailed comparison with other related methods in the literature, particularly those that also aim to improve the efficiency and robustness of RL-based training. This comparison should not only focus on the performance of the methods but also on their computational cost, robustness to noisy data, and ease of implementation. A more detailed discussion of the similarities and differences between the proposed method and existing approaches would help to clarify the unique contributions of this work. For example, the authors could compare their method with other approaches that use variational inference or other techniques to reduce the variance of the gradient estimator. This would help to highlight the advantages and disadvantages of the proposed method compared to other state-of-the-art techniques. Third, the authors should conduct a more thorough comparison with RL methods that utilize rule-based rewards. Specifically, the authors should evaluate their method on benchmarks like GPQA and MMLU-Pro, which are commonly used to assess reasoning capabilities. This comparison should not only focus on the final performance but also analyze the learning curves and the sample efficiency of each method. It would be valuable to understand how the proposed method compares to RL with rule-based rewards in terms of convergence speed and the ability to generalize to unseen examples. Furthermore, the authors should investigate the impact of different rule-based reward functions on the performance of RL methods, as this could provide insights into the robustness of their approach. This analysis should also include a discussion of the potential for reward hacking in RL with rule-based rewards, and how the proposed method addresses this issue. Fourth, the authors should provide a more detailed analysis of the computational cost of the proposed method. This analysis should include a breakdown of the time and memory requirements for each step of the algorithm, and a comparison with existing RLVR methods. This analysis should also consider the impact of different model sizes and dataset sizes on the computational cost. It would be valuable to understand how the computational cost of the proposed method scales with the size of the model and the dataset. This analysis should include a discussion of the potential for parallelizing the training process to reduce the overall training time. Finally, the authors should provide more clarity on the practical implementation details of the proposed method. For example, how are the reasoning traces generated, and what are the specific parameters used for training? A more detailed description of the experimental setup, including the hardware used and the training procedure, would enhance the reproducibility of the results. Furthermore, it would be beneficial to include an ablation study to analyze the impact of different components of the method on its performance. For instance, how does the performance change when the variance reduction technique is removed? Such an analysis would provide valuable insights into the method's inner workings and help guide future research in this area. By addressing these points, the authors can significantly strengthen their paper and make it more impactful to the broader research community.


## Questions:

Based on my analysis, I have several questions that I believe are crucial for a deeper understanding of the proposed method. First, how does VeriFree perform on tasks that require multi-hop reasoning or common-sense inference? While the current benchmarks demonstrate strong performance, it is crucial to understand how the method scales to more complex reasoning tasks. The authors should consider including experiments on datasets that specifically test these capabilities, such as those involving chain-of-thought reasoning or symbolic manipulation. Second, what is the computational cost of VeriFree compared to existing RLVR methods, and how does it scale with model size and dataset size? The paper mentions that the method reduces the need for a verifier model, but it lacks a detailed analysis of the computational savings and a comparison with other methods. A more thorough analysis of the computational requirements of the method and how it compares to previous methods would be helpful for practitioners. Third, how sensitive is VeriFree to different hyperparameters and training configurations? The paper mentions that the method is relatively insensitive to hyperparameters, but it does not provide a detailed analysis of the impact of different hyperparameter settings and their impact on the performance of the method. A more thorough analysis of these factors would provide valuable insights into the practical applicability of the method. Fourth, how does VeriFree handle noisy or incomplete reasoning traces? The paper does not adequately address the potential for the model to generate incorrect reasoning traces, which could lead to suboptimal performance in scenarios with multiple valid answers. A more detailed discussion of the method's robustness to noisy or incomplete traces is needed. Fifth, how does VeriFree compare with RL on rule-based rewards on benchmarks like GPQA and MMLU-Pro? The paper includes a baseline using a verifier model, but it does not directly compare against RL with rule-based rewards using explicit reward functions. A more thorough comparison with these methods would help to understand the trade-offs between the two approaches. Finally, what are the limitations of the proposed method, and what are the potential avenues for future research? The paper should discuss the potential for the model to generate incorrect reasoning traces and how this could affect the overall performance. This discussion should include an analysis of the types of errors that the model makes and to explore techniques to mitigate these errors. Addressing these questions would provide a more comprehensive understanding of the strengths and limitations of VeriFree and guide future research in this area.


## Rating:

6.5


## Confidence:

3.5


## Decision:

Accept
}