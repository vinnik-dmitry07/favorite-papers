I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper studies the entropy patterns of tokens in the reasoning process of LLMs. The authors find that only a small fraction of tokens exhibit high entropy, while the majority display low entropy. These high-entropy tokens act as "forks" in the reasoning process, guiding the model toward diverse reasoning pathways. The authors also observe that the entropy patterns in CoT reasoning remain consistent across RL-based reasoning trajectories. Building on these findings, the authors propose a new method to improve RL-based training. By retaining policy gradient updates for only the 20% of tokens with the highest entropy, they achieve performance comparable to full-gradient updates on the Qwen3-32B and Qwen3-14B base models, while significantly reducing training time.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a thorough analysis of the entropy patterns of tokens in the reasoning process of LLMs. They demonstrate that the high-entropy tokens are critical for diverse reasoning pathways, and the low-entropy tokens are not very important.
3. The authors propose a new method to improve RL-based training. By retaining policy gradient updates for only the 20% of tokens with the highest entropy, they achieve performance comparable to full-gradient updates on the Qwen3-32B and Qwen3-14B base models, while significantly reducing training time.

### Weaknesses

#### Some Related Works


#### comment

1. The authors only provide the experimental results of the Qwen family models. It is unclear whether the findings can be generalized to other LLMs.
2. The authors only consider the impact of the proportion of high-entropy tokens. The impact of the threshold of high-entropy tokens is not considered.
3. The authors do not provide the code for their experiments.

### Suggestions

The study's focus on the Qwen family of models raises concerns about the generalizability of the findings. While the Qwen models are powerful, it's crucial to determine if the observed entropy patterns and the effectiveness of the proposed method hold true for other large language models with different architectures and training datasets. For instance, models with different attention mechanisms or pre-training objectives might exhibit different token entropy distributions and reasoning patterns. Future work should include experiments on a more diverse set of models, such as the Llama family or models from other major LLM providers, to validate the robustness of the conclusions. This would involve not only replicating the existing experiments but also adapting the methodology to account for potential variations in model behavior. Furthermore, it would be beneficial to explore the impact of different model sizes within the Qwen family to see if the observed trends hold across different scales.

Regarding the exploration of high-entropy tokens, the paper focuses solely on the proportion of these tokens, which is a good starting point. However, a more detailed analysis of the threshold for defining high-entropy tokens is needed. The current approach uses a fixed proportion (20%), but it's possible that the optimal threshold might vary depending on the model size, architecture, or task. A systematic study of different threshold values, perhaps ranging from 10% to 50% in increments of 5%, would provide a more comprehensive understanding of the role of high-entropy tokens. This analysis should also investigate the relationship between the threshold and the overall performance of the model, as well as the impact on training time and resource consumption. It would be valuable to determine if there is a point of diminishing returns, where increasing the proportion of updated tokens beyond a certain threshold yields minimal performance gains.

Finally, the lack of publicly available code hinders the reproducibility and further development of this work. While the authors provide a detailed description of their methodology, the absence of code makes it difficult for other researchers to replicate the experiments and build upon the findings. To address this, the authors should release their code, along with the specific experimental settings and training scripts. This would not only facilitate the verification of the results but also encourage further research in this area. The code should be well-documented and easy to use, allowing other researchers to explore the impact of different parameters and model architectures. Furthermore, providing pre-trained models or checkpoints would enable researchers to quickly test the proposed method without having to train the models from scratch.

### Questions

1. How does the performance of the proposed method change when the proportion of high-entropy tokens is varied?
2. How does the proposed method perform on other LLMs?

### Rating

6

### Confidence

3

**********

## Reviewer 2

### Summary

This paper investigates the entropy patterns of tokens in Chain-of-Thought (CoT) reasoning and finds that only a small subset of tokens exhibit high entropy, acting as "forks" that guide the model toward diverse reasoning pathways. The authors propose a novel method to restrict policy gradient updates to these high-entropy tokens, achieving performance comparable to full-gradient updates while significantly reducing training time. The paper provides a deeper understanding of the role of specific tokens in reasoning processes and offers a more efficient approach to RL-based reasoning training.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper presents a novel perspective on understanding reasoning capabilities in LLMs through the lens of token entropy, which is a unique and insightful approach.
2. The research is well-structured, with clear methodology and detailed experimental results that support the claims made.
3. The proposed method of restricting policy gradient updates to high-entropy tokens is simple yet effective, offering a practical solution for improving RL-based reasoning training.
4. The paper is well-written, with clear explanations and visualizations that make complex concepts accessible to a broad audience.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of the proposed method, such as potential scenarios where it might not be effective.
2. The paper could be improved by including a more comprehensive comparison with existing methods for improving RL-based reasoning training.

### Suggestions

The paper's exploration of token entropy in Chain-of-Thought (CoT) reasoning is a promising direction, but it would be beneficial to delve deeper into the practical limitations of the proposed method. Specifically, the authors should investigate scenarios where restricting policy gradient updates to high-entropy tokens might hinder performance. For instance, in tasks requiring highly deterministic reasoning steps, the low-entropy tokens might be crucial for maintaining accuracy, and skipping updates to these tokens could lead to suboptimal results. A more thorough analysis of the types of reasoning tasks where this method is most effective, and where it might struggle, would provide a more balanced perspective on its applicability. Furthermore, the paper should explore the sensitivity of the method to the choice of the entropy threshold for defining high-entropy tokens. A sensitivity analysis could reveal whether the performance is robust to changes in this parameter or if there is an optimal range for different tasks and model architectures.

To strengthen the paper's contribution, a more comprehensive comparison with existing methods for improving RL-based reasoning training is needed. The authors should not only compare their method against standard RL algorithms but also against other techniques that aim to improve the efficiency or effectiveness of RL training for reasoning tasks. This comparison should include a detailed analysis of the computational costs, convergence rates, and final performance of each method. For example, the authors could compare their method against techniques that use curriculum learning or those that focus on optimizing the reward function. A thorough comparison would help to contextualize the proposed method within the broader landscape of RL-based reasoning research and highlight its unique advantages and disadvantages. This would also help to identify potential areas for future research and development.

Finally, the paper would benefit from a more detailed discussion of the computational overhead associated with calculating token entropy. While the authors mention that the entropy calculation is relatively inexpensive, a more precise analysis of the computational cost, especially in the context of large language models, would be valuable. This analysis should include the time and memory requirements for calculating entropy for different model sizes and sequence lengths. Furthermore, the authors should discuss potential strategies for optimizing the entropy calculation process, such as using approximate entropy measures or parallelizing the computation. A more thorough analysis of the computational aspects of the proposed method would provide a more complete picture of its practical feasibility and scalability.

### Questions

1. How does the proposed method perform on tasks that require highly deterministic reasoning steps, where low-entropy tokens might be more important for maintaining accuracy?
2. What is the computational overhead of calculating token entropy, especially for large language models?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper investigates the role of token entropy in the reasoning capabilities of large language models (LLMs) within the Reinforcement Learning with Verifiable Rewards (RLVR) framework. The authors analyze the entropy patterns of Chain-of-Thought (CoT) reasoning and find that only a small subset of tokens exhibit high entropy, which they term "forks" in the reasoning process. These high-entropy tokens are crucial for diverse reasoning pathways, while low-entropy tokens are primarily responsible for maintaining the logical flow of reasoning. The paper demonstrates that by restricting policy gradient updates to only the 20% of high-entropy tokens, the model can achieve performance comparable to full-gradient updates while significantly reducing training time. This finding suggests that RLVR training can be made more efficient by focusing on the most informative tokens.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel perspective on understanding the reasoning capabilities of LLMs by analyzing token entropy patterns in Chain-of-Thought (CoT) reasoning. This approach provides a fresh lens through which to examine the role of individual tokens in the reasoning process.
2. The authors provide a thorough analysis of the entropy patterns in CoT reasoning, identifying a small subset of high-entropy tokens that are critical for diverse reasoning pathways. This analysis is supported by empirical evidence and provides valuable insights into the inner workings of LLMs during reasoning.
3. The paper demonstrates that by restricting policy gradient updates to only the 20% of high-entropy tokens, the model can achieve performance comparable to full-gradient updates while significantly reducing training time. This finding has practical implications for making RLVR training more efficient and scalable.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on the Qwen family of models. It would be beneficial to extend the analysis to other LLM architectures, such as the Llama family, to assess the generalizability of the findings. The observed entropy patterns and the effectiveness of the proposed method might vary across different model architectures and training regimes. For instance, models with different attention mechanisms or pre-training objectives could exhibit different token entropy distributions and reasoning patterns. Therefore, it is crucial to validate the findings on a broader range of models to ensure the robustness of the conclusions.
2. The paper could benefit from a more in-depth discussion of the limitations of the proposed method. For example, it is unclear how the method would perform on tasks that require more complex reasoning or tasks with a higher degree of ambiguity. The current analysis primarily focuses on tasks where the reasoning process is relatively clear and well-defined. However, in real-world scenarios, reasoning can be more nuanced and ambiguous. It would be valuable to explore how the proposed method handles such cases and whether it introduces any biases or limitations in these scenarios. Furthermore, the paper does not discuss the potential impact of the entropy threshold on the performance of the model. A more detailed analysis of how different entropy thresholds affect the model's reasoning capabilities would be beneficial.
3. While the paper demonstrates that restricting updates to high-entropy tokens can improve training efficiency, it does not fully explore the potential trade-offs. For example, it is unclear whether this approach might lead to a loss of generalization or robustness in certain tasks. The paper should include a more comprehensive evaluation of the model's performance on a wider range of tasks to assess the potential trade-offs between efficiency and generalization. It is important to determine if the focus on high-entropy tokens leads to a model that is overly specialized to the training data and fails to generalize well to unseen tasks or scenarios. A more thorough analysis of the model's performance on diverse tasks is needed to fully understand the implications of the proposed method.

### Suggestions

To strengthen the paper, the authors should conduct a more comprehensive evaluation of their method across a wider range of LLM architectures, including models from the Llama family and other prominent families. This would involve not only replicating the existing experiments but also adapting the methodology to account for potential variations in model behavior. For example, models with different attention mechanisms or pre-training objectives might exhibit different token entropy distributions and reasoning patterns. Therefore, it is crucial to validate the findings on a broader range of models to ensure the robustness of the conclusions. Furthermore, the authors should explore the impact of different token entropy thresholds on the model's performance. A sensitivity analysis of the entropy threshold would provide valuable insights into the optimal balance between exploration and exploitation during training. This analysis should include a discussion of how different thresholds affect the model's reasoning capabilities and its ability to generalize to unseen tasks.

In addition to expanding the model evaluation, the authors should also investigate the performance of their method on more complex and ambiguous reasoning tasks. This would involve testing the model on tasks that require more nuanced and flexible reasoning, such as tasks involving natural language understanding, common-sense reasoning, or multi-step problem-solving. The authors should also explore the potential limitations of their method in handling tasks with a higher degree of ambiguity. This analysis should include a discussion of how the proposed method might introduce biases or limitations in these scenarios. Furthermore, the authors should provide a more detailed analysis of the computational cost of their method compared to full-gradient updates. This analysis should include a breakdown of the time and memory requirements for calculating token entropy and updating the model parameters. This would provide a more complete picture of the practical implications of the proposed method.

Finally, the authors should conduct a more thorough evaluation of the model's generalization capabilities. This would involve testing the model on a wider range of tasks and datasets, including those that are significantly different from the training data. The authors should also explore the potential trade-offs between efficiency and generalization. This analysis should include a discussion of whether the focus on high-entropy tokens leads to a model that is overly specialized to the training data and fails to generalize well to unseen tasks or scenarios. A more comprehensive evaluation of the model's performance on diverse tasks is needed to fully understand the implications of the proposed method. This should include a discussion of the potential limitations of the method and suggestions for future research directions.

### Questions

1. How does the proposed method perform on tasks that require more complex reasoning or tasks with a higher degree of ambiguity?
2. What is the computational cost of calculating token entropy compared to full-gradient updates?
3. How does the choice of entropy threshold affect the model's performance and generalization capabilities?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

The paper presents an analysis of token entropy patterns in Chain-of-Thought (CoT) reasoning and proposes a method to improve Reinforcement Learning with Verifiable Rewards (RLVR) by restricting policy gradient updates to high-entropy tokens. The authors find that only a small subset of high-entropy tokens are crucial for diverse reasoning pathways, while low-entropy tokens have minimal impact. By focusing on these high-entropy tokens, the proposed method achieves comparable performance to full-gradient updates while significantly reducing training time. The study provides valuable insights into the role of token entropy in reasoning and offers a more efficient approach to RL-based reasoning training.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel perspective on understanding the reasoning capabilities of large language models (LLMs) by analyzing token entropy patterns in Chain-of-Thought (CoT) reasoning. This approach provides a fresh lens through which to examine the role of individual tokens in the reasoning process.
2. The authors provide a thorough analysis of the entropy patterns in CoT reasoning, identifying a small subset of high-entropy tokens that are critical for diverse reasoning pathways. This analysis is supported by empirical evidence and provides valuable insights into the inner workings of LLMs during reasoning.
3. The paper demonstrates that by restricting policy gradient updates to only the 20% of high-entropy tokens, the model can achieve performance comparable to full-gradient updates while significantly reducing training time. This finding has practical implications for making RLVR training more efficient and scalable.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of the proposed method, such as potential scenarios where it might not be effective.
2. The paper could be improved by including a more comprehensive comparison with existing methods for improving RL-based reasoning training.

### Suggestions

The paper's analysis of token entropy in Chain-of-Thought (CoT) reasoning is a valuable contribution, but it could be strengthened by a more thorough investigation into the practical implications of the identified high-entropy tokens. Specifically, the paper should explore the sensitivity of the proposed method to the selection of these high-entropy tokens. For instance, how does the performance vary when using different percentages of high-entropy tokens, or when using a different method for identifying these tokens? A more detailed analysis of the characteristics of these tokens, such as their semantic content or syntactic role, would also be beneficial. This would provide a deeper understanding of why these tokens are so crucial for reasoning and could potentially lead to more targeted and effective training strategies. Furthermore, the paper should investigate the potential for these high-entropy tokens to be used for other tasks, such as debugging or interpretability, which could further highlight their importance.

To improve the paper's impact, it should include a more comprehensive comparison with existing methods for improving RL-based reasoning training. While the paper demonstrates that restricting policy gradient updates to high-entropy tokens can achieve comparable performance to full-gradient updates, it does not provide a clear picture of how this method compares to other state-of-the-art techniques. For example, the paper could compare its method to techniques that use curriculum learning or those that focus on optimizing the reward function. A detailed comparison should include not only performance metrics but also computational costs, convergence rates, and the robustness of the methods to different hyperparameter settings. This would allow readers to better understand the strengths and weaknesses of the proposed method and its potential for practical applications. The paper should also discuss the limitations of the proposed method, such as potential scenarios where it might not be effective, and provide guidance on when it is most appropriate to use this method.

Finally, the paper should provide more details on the experimental setup and the specific models used in the study. This includes the size and architecture of the models, the datasets used for training and evaluation, and the specific hyperparameters used for training. This information is crucial for reproducibility and for allowing other researchers to build upon the findings of this paper. The paper should also discuss the potential for the proposed method to be applied to other types of reasoning tasks, such as mathematical reasoning or logical inference. This would help to broaden the scope of the paper and highlight the potential for wider impact. Additionally, the paper should explore the potential for using the identified high-entropy tokens for other tasks, such as debugging or interpretability, which could further highlight their importance.

### Questions

1. How does the proposed method perform on tasks that require highly deterministic reasoning steps, where low-entropy tokens might be more important for maintaining accuracy?
2. What is the computational overhead of calculating token entropy, especially for large language models?

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
1. Go through each reviewer's comments one by one.
2. For each weakness identified by the reviewer, find the relevant section in the paper.
3. Extract evidence (quotes, experimental details, missing citations) from the paper to support the weakness.
4. If the weakness is about missing information, confirm that the information is indeed absent.
5. If there are conflicting opinions between reviewers, note them.
6. Finally, summarize the findings for each weakness, stating if it's valid, partially valid, or invalid, along with the confidence level and key evidence.
**Review 1**

1. Weakness Statement:
"The paper could benefit from a more detailed discussion of the limitations of the proposed method, such as potential scenarios where it might not be effective."

2. Evidence Collection:
b) Experiment-related Evidence (if applicable):
   - The paper does not explicitly dedicate a section to discussing the limitations of the proposed method.

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - The reviewer correctly points out the absence of a dedicated limitations section. While the paper discusses the effectiveness of the method, it lacks a thorough exploration of scenarios where it might fail or underperform.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of a dedicated "Limitations" section in the paper.

1. Weakness Statement:
"The paper could be improved by including a more comprehensive comparison with existing methods for improving RL-based reasoning training."

2. Evidence Collection:
b) Experiment-related Evidence (if applicable):
   - The paper primarily compares against the vanilla DAPO method and a version of DAPO with all tokens.
   - The "Related Work" section mentions other RLVR methods but doesn't provide a direct experimental comparison.

3. Literature Gap Analysis:
   - The "Related Work" section mentions several other RLVR methods (e.g., Gandhi et al., 2025; Li et al., 2025; Lin et al., 2024; Yu et al., 2025), but the experimental section doesn't include them as baselines.

4. Validation Analysis:
   - The reviewer's point is valid. The experimental section focuses on comparing against variations of the proposed method and a baseline. A more comprehensive comparison with other established RLVR techniques would strengthen the paper.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Limited baseline comparisons in the experimental section, despite mentioning other RLVR methods in the related work.

1. Weakness Statement:
"The paper's exploration of token entropy in Chain-of-Thought (CoT) reasoning is a valuable contribution, but it could be strengthened by a more thorough investigation into the practical implications of the identified high-entropy tokens. Specifically, the paper should explore the sensitivity of the proposed method to the selection of these high-entropy tokens. For instance, how does the performance vary when using different percentages of high-entropy tokens, or when using a different method for identifying these tokens?"

2. Evidence Collection:
b) Experiment-related Evidence (if applicable):
   - The paper does explore the impact of varying the proportion of high-entropy tokens (Figure 7a).
   - The paper defines high-entropy tokens based on a fixed threshold (top 20%).
   - The paper doesn't explore different methods for identifying high-entropy tokens.

4. Validation Analysis:
   - The reviewer's point is partially valid. The paper does explore the impact of varying the percentage of high-entropy tokens. However, it doesn't investigate different methods for identifying these tokens.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: Figure 7a shows results for varying the percentage of high-entropy tokens, but the method for identifying them is fixed.

1. Weakness Statement:
"A more detailed analysis of the characteristics of these tokens, such as their semantic content or syntactic role, would also be beneficial. This would provide a deeper understanding of why these tokens are so crucial for reasoning and could potentially lead to more targeted and effective training strategies."

2. Evidence Collection:
b) Experiment-related Evidence (if applicable):
   - The paper identifies "orking modes" of high-entropy tokens (e.g., "for", "then", "unless").
   - The paper provides examples of these tokens and their corresponding high entropy (Table 1).

4. Validation Analysis:
   - The reviewer's point is partially valid. The paper does provide some analysis of the characteristics of these tokens, such as their syntactic roles. However, a more in-depth analysis of their semantic content could be beneficial.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: Table 1 provides examples of high-entropy tokens and their syntactic roles, but a deeper semantic analysis is missing.

1. Weakness Statement:
"Furthermore, the paper should investigate the potential for these high-entropy tokens to be used for other tasks, such as debugging or interpretability, which could further highlight their importance."

2. Evidence Collection:
   - The paper focuses on the role of high-entropy tokens in improving reasoning performance.

4. Validation Analysis:
   - The reviewer's point is valid. The paper's scope is limited to reasoning, and it doesn't explore the potential of these tokens for other tasks.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper's focus is solely on reasoning performance.

1. Weakness Statement:
"To improve the paper's impact, it should include a more comprehensive comparison with existing methods for improving RL-based reasoning training. While the paper demonstrates that restricting policy gradient updates to high-entropy tokens can achieve comparable performance to full-gradient updates, it does not provide a clear picture of how this method compares to other state-of-the-art techniques. For example, the paper could compare its method to techniques that use curriculum learning or those that focus on optimizing the reward function. A detailed comparison should include not only performance metrics but also computational costs, convergence rates, and the robustness of the methods to different hyperparameter settings."

2. Evidence Collection:
b) Experiment-related Evidence (if applicable):
   - The paper compares against vanilla DAPO and DAPO with all tokens.
   - The paper doesn't include comparisons with methods using curriculum learning or reward function optimization.

3. Literature Gap Analysis:
   - The "Related Work" section mentions other RLVR methods but doesn't provide a direct experimental comparison.

4. Validation Analysis:
   - The reviewer's point is valid. The experimental section lacks a comprehensive comparison with other state-of-the-art techniques for improving RL-based reasoning training.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Limited baseline comparisons in the experimental section.

1. Weakness Statement:
"The paper should also discuss the limitations of the proposed method, such as potential scenarios where it might not be effective, and provide guidance on when it is most appropriate to use this method."

2. Evidence Collection:
   - The paper lacks a dedicated section discussing the limitations.

4. Validation Analysis:
   - The reviewer's point is valid. The paper doesn't explicitly discuss scenarios where the method might be less effective.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of a dedicated "Limitations" section.

1. Weakness Statement:
"Finally, the paper should provide more details on the experimental setup and the specific models used in the study. This includes the size and architecture of the models, the datasets used for training and evaluation, and the specific hyperparameters used for training. This information is crucial for reproducibility and for allowing other researchers to build upon the findings of this paper. The paper should also discuss the potential for the proposed method to be applied to other types of reasoning tasks, such as mathematical reasoning or logical inference. This would help to broaden the scope of the paper and highlight the potential for wider impact. Additionally, the paper should explore the potential for using the identified high-entropy tokens for other tasks, such as debugging or interpretability, which could further highlight their importance."

2. Evidence Collection:
b) Experiment-related Evidence (if applicable):
   - The paper mentions using Qwen3-32B and Qwen3-8B base models.
   - The paper mentions using AIME’24 and AIME’25 for evaluation.
   - The paper mentions using the reasoning model after RLVR training.
   - The paper doesn't provide specific hyperparameter details for the RLVR training.
   - The paper doesn't discuss applying the method to other reasoning tasks like mathematical reasoning or logical inference.
   - The paper doesn't explore using high-entropy tokens for debugging or interpretability.

4. Validation Analysis:
   - The reviewer's point is partially valid. The paper provides some details about the models and datasets used. However, it lacks specific hyperparameter details and a discussion of broader applicability or other task usage.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: Limited hyperparameter details, no discussion of broader applicability or other task usage.

1. Weakness Statement:
"How does the proposed method perform on tasks that require highly deterministic reasoning steps, where low-entropy tokens might be more important for maintaining accuracy?"

2. Evidence Collection:
b) Experiment-related Evidence (if applicable):
   - The paper's experiments focus on Chain-of-Thought reasoning, which often involves some level of stochasticity.
   - The paper doesn't explicitly test on tasks with highly deterministic reasoning.

4. Validation Analysis:
   - The reviewer raises a valid question. The paper's findings might not directly translate to tasks with highly deterministic reasoning.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of experiments on highly deterministic reasoning tasks.

1. Weakness Statement:
"What is the computational overhead of calculating token entropy, especially for large language models?"

2. Evidence Collection:
b) Experiment-related Evidence (if applicable):
   - The paper mentions that calculating entropy is "relatively inexpensive" (Section 5.3).
   - The paper doesn't provide a detailed analysis of the computational cost.

4. Validation Analysis:
   - The reviewer's question is valid. While the paper claims it's inexpensive, a more detailed analysis would be beneficial.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: Medium
   - Key supporting evidence: Lack of detailed computational cost analysis.

**Review 2**

1. Weakness Statement:
"The authors only provide the experimental results of the Qwen family models. It is unclear whether the findings can be generalized to other LLMs."

2. Evidence Collection:
b) Experiment-related Evidence (if applicable):
   - The experiments primarily use the Qwen3-32B and Qwen3-8B base models.
   - The paper includes experiments on the Llama-3.1-8B model (Table 2).

4. Validation Analysis:
   - The reviewer's statement is partially valid. While the primary experiments focus on the Qwen family, the paper does include results on the Llama-3.1-8B model, suggesting some level of generalization.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: Experiments on Qwen models and Llama-3.1-8B, but more diverse models could strengthen the generalization claim.

1. Weakness Statement:
"The authors only consider the impact of the proportion of high-entropy tokens. The impact of the threshold of high-entropy tokens is not considered."

2. Evidence Collection:
b) Experiment-related Evidence (if applicable):
   - The paper uses a fixed threshold of 0.672 for defining high-entropy tokens (Section 3).
   - The paper doesn't explore different thresholds.

4. Validation Analysis:
   - The reviewer's point is valid. The paper focuses on the proportion of high-entropy tokens and doesn't investigate the impact of different entropy thresholds.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Fixed entropy threshold used in the experiments.

1. Weakness Statement:
"The authors do not provide the code for their experiments."

2. Evidence Collection:
   - The paper does not mention the availability of code.

4. Validation Analysis:
   - The reviewer's point is valid. The paper doesn't mention code availability.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of a code availability statement.

1. Weakness Statement:
"How does the performance of the proposed method change when the proportion of high-entropy tokens is varied?"

2. Evidence Collection:
b) Experiment-related Evidence (if applicable):
   - Figure 7a shows the impact of varying the proportion of high-entropy tokens.

4. Validation Analysis:
   - The reviewer's question is addressed by the paper.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: Figure 7a directly addresses this question.

1. Weakness Statement:
"How does the proposed method perform on other LLMs?"

2. Evidence Collection:
b) Experiment-related Evidence (if applicable):
   - The paper includes experiments on the Llama-3.1-8B model (Table 2).

4. Validation Analysis:
   - The reviewer's question is partially addressed by the inclusion of the Llama model.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: Experiments on Llama-3.1-8B, but more diverse models would be beneficial.

**Review 3**

1. Weakness Statement:
"The paper could benefit from a more detailed discussion of the limitations of the proposed method, such as potential scenarios where it might not be effective."

2. Evidence Collection:
   - The paper lacks a dedicated "Limitations" section.

4. Validation Analysis:
   - The reviewer's point is valid. The paper doesn't explicitly discuss limitations.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of a dedicated "Limitations" section.

1. Weakness Statement:
"The paper could be improved by including a more comprehensive comparison with existing methods for improving RL-based reasoning training."

2. Evidence Collection:
   - The experimental section primarily compares against variations of the proposed method and a baseline.

4. Validation Analysis:
   - The reviewer's point is valid. The comparison is limited.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Limited baseline comparisons in the experimental section.

1. Weakness Statement:
"The paper's exploration of token entropy in Chain-of-Thought (CoT) reasoning is a valuable contribution, but it could be strengthened by a more thorough investigation into the practical implications of the identified high-entropy tokens. Specifically, the paper should explore the sensitivity of the proposed method to the selection of these high-entropy tokens. For instance, how does the performance vary when using different percentages of high-entropy tokens, or when using a different method for identifying these tokens?"

2. Evidence Collection:
b) Experiment-related Evidence (if applicable):
   - Figure 7a shows the impact of varying the percentage of high-entropy tokens.
   - The paper uses a fixed method for identifying high-entropy tokens (entropy threshold).

4. Validation Analysis:
   - The reviewer's point is partially valid. The paper explores the impact of varying the percentage but not different identification methods.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: Figure 7a shows varying percentages, but the identification method is fixed.

1. Weakness Statement:
"A more detailed analysis of the characteristics of these tokens, such as their semantic content or syntactic role, would also be beneficial. This would provide a deeper understanding of why these tokens are so crucial for reasoning and could potentially lead to more targeted and effective training strategies."

2. Evidence Collection:
b) Experiment-related Evidence (if applicable):
   - Table 1 provides examples of high-entropy tokens and their syntactic roles.

4. Validation Analysis:
   - The reviewer's point is partially valid. Table 1 provides some syntactic analysis, but a deeper semantic analysis is missing.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: Table 1 provides syntactic examples, but deeper semantic analysis is lacking.

1. Weakness Statement:
"Furthermore, the paper should investigate the potential for these high-entropy tokens to be used for other tasks, such as debugging or interpretability, which could further highlight their importance."

2. Evidence Collection:
   - The paper focuses on improving reasoning performance.

4. Validation Analysis:
   - The reviewer's point is valid. The paper doesn't explore other tasks.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper's focus is solely on reasoning.

1. Weakness Statement:
"To improve the paper's impact, it should include a more comprehensive comparison with existing methods for improving RL-based reasoning training. While the paper demonstrates that restricting policy gradient updates to high-entropy tokens can achieve comparable performance to full-gradient updates, it does not provide a clear picture of how this method compares to other state-of-the-art techniques. For example, the paper could compare its method to techniques that use curriculum learning or those that focus on optimizing the reward function. A detailed comparison should include not only performance metrics but also computational costs, convergence rates, and the robustness of the methods to different hyperparameter settings."

2. Evidence Collection:
   - The experimental section lacks comparisons with methods using curriculum learning or reward function optimization.

4. Validation Analysis:
   - The reviewer's point is valid. The comparison is limited.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Limited baseline comparisons in the experimental section.

1. Weakness Statement:
"The paper should also discuss the limitations of the proposed method, such as potential scenarios where it might not be effective, and provide guidance on when it is most appropriate to use this method."

2. Evidence Collection:
   - The paper lacks a dedicated "Limitations" section.

4. Validation Analysis:
   - The reviewer's point is valid. The paper doesn't discuss limitations.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of a dedicated "Limitations" section.

1. Weakness Statement:
"Finally, the paper should provide more details on the experimental setup and the specific models used in the study. This includes the size and architecture of the models, the datasets used for training and evaluation, and the specific hyperparameters used for training. This information is crucial for reproducibility and for allowing other researchers to build upon the findings of this paper. The paper should also discuss the potential for the proposed method to be applied to other types of reasoning tasks, such as mathematical reasoning or logical inference. This would help to broaden the scope of the paper and highlight the potential for wider impact. Additionally, the paper should explore the potential for using the identified high-entropy tokens for other tasks, such as debugging or interpretability, which could further highlight their importance."

2. Evidence Collection:
b) Experiment-related Evidence (if applicable):
   - The paper mentions the model sizes and architectures (Qwen3-32B, Qwen3-8B, Llama-3.1-8B).
   - The paper mentions the datasets used (AIME'24, AIME'25).
   - The paper mentions using the reasoning model after RLVR training.
   - The paper lacks specific hyperparameter details for the RLVR training.
   - The paper doesn't discuss applying the method to other reasoning tasks or using high-entropy tokens for debugging/interpretability.

4. Validation Analysis:
   - The reviewer's point is partially valid. Some experimental details are provided, but hyperparameter details and broader applicability are missing.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: Limited hyperparameter details, no discussion of broader applicability.

1. Weakness Statement:
"How does the proposed method perform on tasks that require highly deterministic reasoning steps, where low-entropy tokens might be more important for maintaining accuracy?"

2. Evidence Collection:
   - The paper's experiments focus on Chain-of-Thought reasoning.
   - The paper doesn't explicitly test on highly deterministic reasoning tasks.

4. Validation Analysis:
   - The reviewer raises a valid question about the method's applicability to deterministic tasks.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of experiments on deterministic reasoning tasks.

1. Weakness Statement:
"What is the computational overhead of calculating token entropy, especially for large language models?"

2. Evidence Collection:
   - The paper mentions that calculating entropy is "relatively inexpensive."
   - The paper lacks a detailed computational cost analysis.

4. Validation Analysis:
   - The reviewer's question is valid, and the paper lacks a detailed analysis.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: Medium
   - Key supporting evidence: Lack of detailed computational cost analysis.

**Review 4**

1. Weakness Statement:
"The paper primarily focuses on the Qwen family of models. It would be beneficial to extend the analysis to other LLM architectures, such as the Llama family, to assess the generalizability of the findings. The observed entropy patterns and the effectiveness of the proposed method might vary across different model architectures and training regimes. For instance, models with different attention mechanisms or pre-training objectives could exhibit different token entropy distributions and reasoning patterns. Therefore, it is crucial to validate the findings on a broader range of models to ensure the robustness of the conclusions."

2. Evidence Collection:
b) Experiment-related Evidence (if applicable):
   - The primary experiments focus on the Qwen family.
   - The paper includes experiments on the Llama-3.1-8B model (Table 2).

4. Validation Analysis:
   - The reviewer's point is partially valid. While the primary focus is on Qwen, the inclusion of Llama-3.1-8B provides some evidence of generalizability, but more diverse models would strengthen the claim.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: Experiments on Qwen and Llama-3.1-8B, but more diverse models would be ideal.

1. Weakness Statement:
"The paper could benefit from a more in-depth discussion of the limitations of the proposed method. For example, it is unclear how the method would perform on tasks that require more complex reasoning or tasks with a higher degree of ambiguity. The current analysis primarily focuses on tasks where the reasoning process is relatively clear and well-defined. However, in real-world scenarios, reasoning can be more nuanced and ambiguous. It would be valuable to explore how the proposed method handles such cases and whether it introduces any biases or limitations in these scenarios. Furthermore, the paper does not discuss the potential impact of the entropy threshold on the performance of the model. A more detailed analysis of how different entropy thresholds affect the model's reasoning capabilities would be beneficial."

2. Evidence Collection:
   - The paper lacks a dedicated "Limitations" section.
   - The paper doesn't explicitly test on tasks with complex or ambiguous reasoning.
   - The paper uses a fixed entropy threshold.

4. Validation Analysis:
   - The reviewer's point is valid. The paper lacks a dedicated discussion of limitations, doesn't test on complex/ambiguous tasks, and doesn't analyze the impact of the entropy threshold.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of a dedicated "Limitations" section, no experiments on complex/ambiguous tasks, and fixed entropy threshold.

1. Weakness Statement:
"While the paper demonstrates that restricting updates to high-entropy tokens can improve training efficiency, it does not fully explore the potential trade-offs. For example, it is unclear whether this approach might lead to a loss of generalization or robustness in certain tasks. The paper should include a more comprehensive evaluation of the model's performance on a wider range of tasks to assess the potential trade-offs between efficiency and generalization. It is important to determine if the focus on high-entropy tokens leads to a model that is overly specialized to the training data and fails to generalize well to unseen tasks or scenarios. A more thorough analysis of the model's performance on diverse tasks is needed to fully understand the implications of the proposed method."

2. Evidence Collection:
b) Experiment-related Evidence (if applicable):
   - The paper evaluates on AIME'24 and AIME'25, which are reasoning-focused tasks.
   - The paper doesn't evaluate on a wider range of tasks to assess generalization and robustness.

4. Validation Analysis:
   - The reviewer's point is valid. The evaluation is limited to reasoning tasks, and the potential trade-offs regarding generalization and robustness are not fully explored.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Evaluation limited to reasoning tasks, no explicit assessment of generalization/robustness trade-offs.

1. Weakness Statement:
"How does the proposed method perform on tasks that require more complex reasoning or tasks with a higher degree of ambiguity?"

2. Evidence Collection:
b) Experiment-related Evidence (if applicable):
   - The paper's experiments focus on Chain-of-Thought reasoning, which is generally well-defined.
   - The paper doesn't include experiments on tasks with complex or ambiguous reasoning.

4. Validation Analysis:
   - The reviewer's question is valid, and the paper lacks such experiments.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of experiments on complex/ambiguous reasoning tasks.

1. Weakness Statement:
"What is the computational overhead of calculating token entropy, especially for large language models?"

2. Evidence Collection:
   - The paper mentions that calculating entropy is "relatively inexpensive."
   - The paper lacks a detailed computational cost analysis.

4. Validation Analysis:
   - The reviewer's question is valid, and the paper lacks a detailed analysis.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: Medium
   - Key supporting evidence: Lack of detailed computational cost analysis.

**Synthesis and Reflection:**

Several reviewers raised overlapping concerns, particularly regarding the limited scope of the experimental validation and the lack of a dedicated "Limitations" section. Reviewers 1, 2, 3, and 4 all pointed out that the paper primarily focuses on the Qwen family of models and that the evaluation is limited to Chain-of-Thought reasoning tasks. This raises questions about the generalizability of the findings to other LLM architectures and reasoning tasks. The absence of a dedicated "Limitations" section, as noted by Reviewers 1, 2, and 3, is a significant oversight, as it doesn't provide a balanced perspective on the method's applicability and potential drawbacks. Reviewers 1 and 3 also highlighted the need for a more comprehensive comparison with existing methods, which is currently lacking in the experimental section.

There's a consensus that the paper could benefit from a more in-depth analysis of the characteristics of high-entropy tokens (Reviewer 1) and a more thorough investigation into the practical implications of the identified tokens (Reviewer 1 and 3). The suggestion to explore different methods for identifying these tokens (Reviewer 1) and the impact of varying the entropy threshold (Reviewer 2 and 3) are valuable points for future research.

The computational overhead of calculating token entropy is a recurring concern (Reviewers 1, 3, and 4), with the paper lacking a detailed analysis. The question of how the method performs on highly deterministic reasoning tasks (Reviewers 1 and 2) is also a valid point, as the current experiments don't address this scenario.

The request for more details on the experimental setup (Reviewer 2) is partially addressed by the inclusion of results on the Llama-3.1-8B model, but more comprehensive details would still be beneficial for reproducibility.

**Conclusion:**

Based on the evidence collected, the majority of the weaknesses identified by the reviewers are valid. The paper would be significantly strengthened by:

*   **Expanding the experimental validation to include a more diverse set of LLM architectures and reasoning tasks.**
*   **Adding a dedicated "Limitations" section to discuss the method's potential drawbacks and scenarios where it might not be effective.**
*   **Conducting a more comprehensive comparison with existing methods for improving RL-based reasoning training.**
*   **Providing a more detailed analysis of the computational cost of calculating token entropy.**
*   **Exploring the performance of the method on highly deterministic reasoning tasks.**
*   **Including more details on the experimental setup and hyperparameters.**

The reviewers' feedback provides valuable insights for improving the paper's rigor, completeness, and impact.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces a novel perspective on understanding the reasoning capabilities of large language models (LLMs) by analyzing token entropy patterns within Chain-of-Thought (CoT) reasoning. The authors propose that only a small subset of tokens, which they term 'high-entropy tokens,' are crucial for diverse reasoning pathways, while the majority of tokens, labeled as 'low-entropy tokens,' are primarily responsible for maintaining the logical flow of reasoning. The core methodological approach involves quantifying token entropy at each step of the CoT reasoning process and then restricting policy gradient updates to only the high-entropy tokens. This selective update strategy, they argue, achieves comparable performance to full-gradient updates while significantly reducing training time. The authors demonstrate this on the AIME reasoning benchmark, showing that by focusing on the 20% of tokens with the highest entropy, they can achieve performance comparable to full gradient updates on the Qwen3-32B and Qwen3-8B base models, as well as the Llama-3.1-8B model. The paper's main empirical finding is that high-entropy tokens are critical for diverse reasoning pathways, while low-entropy tokens are more important for maintaining the logical flow of reasoning. This finding is supported by experiments that show that the entropy patterns in CoT reasoning remain consistent across different RL-based reasoning trajectories. The authors also demonstrate that by restricting policy gradient updates to only the high-entropy tokens, they can achieve comparable performance to full-gradient updates while significantly reducing training time. The overall significance of this work lies in its novel perspective on understanding the reasoning capabilities of LLMs through the lens of token entropy, and its potential for making RL-based reasoning training more efficient and scalable. By focusing on the most informative tokens, the proposed method offers a promising approach for improving the performance of LLMs on complex reasoning tasks. The paper's findings suggest that not all tokens contribute equally to the reasoning process, and that focusing on the most informative ones can lead to more efficient and effective training. This work contributes to a deeper understanding of how LLMs perform reasoning and provides a practical method for improving their performance.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

3.0


## Strengths:

This paper presents a compelling and innovative approach to understanding and improving the reasoning capabilities of large language models. The core strength of the work lies in its novel perspective of analyzing token entropy within Chain-of-Thought (CoT) reasoning. By identifying a small subset of high-entropy tokens that are critical for diverse reasoning pathways, the authors provide a fresh lens through which to examine the internal workings of LLMs during reasoning. This approach offers a valuable contribution to the field by shifting the focus from individual tokens to the collective behavior of tokens during reasoning. The empirical findings are also a significant strength of the paper. The authors demonstrate that by restricting policy gradient updates to only the high-entropy tokens, they can achieve performance comparable to full-gradient updates while significantly reducing training time. This is a practical and impactful result, as it suggests a more efficient way to train LLMs for reasoning tasks. The experiments, conducted on the AIME reasoning benchmark, provide strong evidence for the effectiveness of the proposed method. The authors show that the method can be applied to different LLM architectures, including the Qwen3-32B and Qwen3-8B base models, as well as the Llama-3.1-8B model, indicating a degree of generalizability. The paper is also well-written and easy to follow, with clear explanations of the methodology and results. The use of visualizations, such as the entropy patterns in CoT reasoning, helps to illustrate the key findings and makes the paper accessible to a broad audience. The authors also provide a thorough analysis of the entropy patterns, identifying a small subset of high-entropy tokens that are critical for diverse reasoning pathways. This analysis is supported by empirical evidence and provides valuable insights into the internal workings of LLMs during reasoning. The paper's focus on making RL-based reasoning training more efficient and scalable is also a significant strength. By restricting policy gradient updates to only the high-entropy tokens, the authors demonstrate a practical approach for improving the performance of LLMs on complex reasoning tasks. This is particularly important as the field of LLMs continues to grow and become more complex. The paper's overall contribution lies in its novel perspective on understanding the reasoning capabilities of LLMs through the lens of token entropy, and its potential for making RL-based reasoning training more efficient and scalable. The authors have successfully demonstrated the practical implications of their findings, and the paper has the potential to inspire further research in this area.


## Weaknesses:

While this paper presents a novel and promising approach, several limitations warrant careful consideration. A primary concern is the lack of a dedicated 'Limitations' section. While the paper discusses the method's effectiveness, it does not explicitly address scenarios where the method might fail or underperform. This omission makes it difficult to fully assess the robustness of the proposed approach and its potential drawbacks. For example, the paper does not explore how the method would perform on tasks that require more complex reasoning or tasks with a higher degree of ambiguity. This is a significant oversight, as real-world reasoning tasks often involve a mix of simple and complex steps, and the method's performance on such tasks is unclear. The absence of this discussion limits the paper's ability to provide a balanced perspective on the method's applicability. Furthermore, the paper's experimental validation is primarily focused on the Qwen family of models, with limited exploration of other LLM architectures. While the paper includes results on the Llama-3.1-8B model, the primary focus on Qwen models raises concerns about the generalizability of the findings. It is unclear whether the observed entropy patterns and the effectiveness of the proposed method would hold true for other LLMs with different architectures and training regimes. For instance, models with different attention mechanisms or pre-training objectives could exhibit different token entropy distributions and reasoning patterns. The paper does not provide sufficient evidence to support the claim that the findings are broadly applicable to the LLM landscape. This limitation is significant, as it restricts the scope of the paper's conclusions and raises questions about the method's robustness across different models. The paper also lacks a comprehensive comparison with existing methods for improving RL-based reasoning training. While the paper demonstrates that restricting policy gradient updates to high-entropy tokens can achieve comparable performance to full-gradient updates, it does not provide a clear picture of how this method compares to other state-of-the-art techniques. For example, the paper does not compare its method to techniques that use curriculum learning or those that focus on optimizing the reward function. This lack of comparison makes it difficult to assess the relative strengths and weaknesses of the proposed method and its potential for practical applications. The paper also does not provide a detailed analysis of the computational cost of calculating token entropy. While the paper mentions that calculating entropy is 'relatively inexpensive,' it does not provide a detailed analysis of the computational overhead, especially for large language models. This is a significant limitation, as the computational cost of calculating token entropy could become a bottleneck for large models. The paper's focus on the proportion of high-entropy tokens is also a limitation. While the paper explores the impact of varying the percentage of high-entropy tokens, it does not investigate the impact of different methods for identifying these tokens. The paper uses a fixed threshold of 0.672 for defining high-entropy tokens, but it does not explore the sensitivity of the results to this threshold. This is a significant oversight, as the choice of threshold could potentially impact the performance of the method. The paper also does not explore the potential of the identified high-entropy tokens for other tasks, such as debugging or interpretability. While the paper focuses on improving reasoning performance, it does not investigate the potential of these tokens for other tasks. This is a missed opportunity, as the high-entropy tokens might have other valuable properties that could be leveraged for different purposes. Finally, the paper does not provide the code for their experiments, which limits the reproducibility of the results. This is a significant limitation, as it makes it difficult for other researchers to build upon the findings of this paper. The lack of code availability also raises concerns about the transparency and rigor of the research. In summary, the paper's limitations include the absence of a dedicated 'Limitations' section, the limited scope of experimental validation, the lack of comparison with existing methods, the lack of detailed computational cost analysis, the limited exploration of the entropy threshold, the lack of investigation into other tasks, and the lack of code availability. These limitations significantly impact the paper's conclusions and raise questions about the generalizability and practical applicability of the proposed method. My confidence in these identified weaknesses is high, as they are directly supported by the paper's content and the absence of certain analyses.


## Suggestions:

To address the identified weaknesses, I recommend several concrete and actionable improvements. First and foremost, the authors should include a dedicated 'Limitations' section in the paper. This section should explicitly discuss the potential scenarios where the proposed method might not be effective or might underperform. This would provide a more balanced and nuanced perspective on the method's applicability and potential drawbacks. The authors should also expand the experimental validation to include a more diverse set of LLM architectures and reasoning tasks. This should include models with different architectures, such as the Llama family and other prominent families, as well as models with different training regimes. This would provide stronger evidence for the robustness and generalizability of the conclusions. The authors should also conduct a more comprehensive comparison with existing methods for improving RL-based reasoning training. This should include a detailed analysis of the computational costs, convergence rates, and the robustness of the methods to different hyperparameter settings. This would allow readers to better understand the strengths and weaknesses of the proposed method and its potential for practical applications. The authors should also provide a more detailed analysis of the computational cost of calculating token entropy. This should include a breakdown of the time and memory requirements for calculating entropy for different model sizes and sequence lengths. This would provide a more complete picture of the practical feasibility of the proposed method. The authors should also investigate the sensitivity of the method to the selection of high-entropy tokens. This should include an exploration of different methods for identifying these tokens, as well as an analysis of the impact of different entropy thresholds on the model's performance. This would provide a deeper understanding of why these tokens are so crucial for reasoning and could potentially lead to more targeted and effective training strategies. The authors should also explore the potential of the identified high-entropy tokens for other tasks, such as debugging or interpretability. This could involve using the high-entropy tokens to gain insights into the model's reasoning process or to identify potential areas for improvement. This would further highlight the importance of these tokens and could potentially lead to more targeted and effective training strategies. Finally, the authors should release the code for their experiments. This would allow other researchers to reproduce the results and build upon the findings of this paper. This would also increase the transparency and rigor of the research. By addressing these suggestions, the authors can significantly strengthen the paper and make it a more valuable contribution to the field. These changes would provide a more comprehensive and nuanced analysis of the proposed method, and would make the paper more accessible and useful to the broader research community.


## Questions:

Several key questions arise from my analysis of this paper, focusing on the core methodological choices and assumptions. First, how does the proposed method perform on tasks that require highly deterministic reasoning steps, where low-entropy tokens might be more important for maintaining accuracy? The paper's experiments primarily focus on Chain-of-Thought reasoning, which often involves some level of stochasticity. It is unclear how the method would perform on tasks with a higher degree of determinism, where the reasoning process is more linear and less reliant on diverse exploration. Second, what is the computational overhead of calculating token entropy, especially for large language models? The paper mentions that calculating entropy is 'relatively inexpensive,' but it does not provide a detailed analysis of the computational cost. A more thorough analysis of the time and memory requirements for calculating entropy would be beneficial, especially for large models. Third, how does the choice of the entropy threshold affect the performance of the model? The paper uses a fixed threshold of 0.672 for defining high-entropy tokens, but it does not explore the sensitivity of the results to this threshold. A more detailed analysis of the impact of different entropy thresholds would be valuable. Fourth, how does the proposed method compare to techniques that use curriculum learning or those that focus on optimizing the reward function? The paper does not provide a clear picture of how the proposed method compares to other state-of-the-art techniques for improving RL-based reasoning training. A more detailed comparison would be beneficial. Fifth, how does the proposed method perform on tasks that require more complex reasoning or tasks with a higher degree of ambiguity? The paper's experiments focus on relatively well-defined reasoning tasks. It is unclear how the method would perform on tasks with more complex or ambiguous reasoning patterns. Sixth, what are the potential applications of the identified high-entropy tokens beyond improving reasoning performance? The paper focuses on improving reasoning performance, but it does not explore the potential of these tokens for other tasks, such as debugging or interpretability. Finally, what are the specific hyperparameters used for the RLVR training? The paper mentions that the method is applied after RLVR training, but it does not provide specific details about the hyperparameters used for this training. This information is crucial for reproducibility and for allowing other researchers to build upon the findings of this paper. These questions highlight key uncertainties and areas for further investigation, and addressing them would significantly strengthen the paper and provide a more complete understanding of the proposed method.


## Rating:

6.5


## Confidence:

3.0


## Decision:

Accept
}