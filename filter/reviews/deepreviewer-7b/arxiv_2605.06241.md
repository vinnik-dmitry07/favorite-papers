I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper explores the role of reinforcement learning (RL) in enhancing reasoning capabilities within large language models (LLMs). The authors challenge the prevailing assumption that RL uniquely drives improvements in reasoning, arguing instead that it primarily steers existing abilities rather than fundamentally expanding new ones. Through a detailed token-level analysis, they demonstrate that RL’s benefits are concentrated in sparse, high-entropy decision-making points, where the model is uncertain which reasoning branch to take. This insight leads to the development of ReasonMaxxer, an RL-free method that applies contrastive fine-tuning at these critical decision points, achieving comparable performance to models trained with RL while significantly reducing computational costs.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper presents a novel perspective on the role of RL in LLM reasoning, suggesting that RL primarily functions as a selective policy rather than a mechanism for developing new reasoning pathways. This reframing challenges conventional assumptions and offers a fresh lens through which to evaluate RL’s impact.
- The authors conduct a thorough token-level analysis, identifying specific locations where RL interventions have the most impact. This detailed approach not only supports their claims but also provides actionable insights for future research in efficient model improvement.
- The proposed RL-free method, ReasonMaxxer, demonstrates impressive efficiency, achieving comparable results to RL-trained models with a fraction of the computational resources. This practical outcome has significant implications for reducing the cost and complexity of improving reasoning in LLMs.

### Weaknesses

#### Some Related Works


#### comment

 - The paper’s core argument, while intriguing, could benefit from more rigorous justification. The claim that RL primarily functions as a selective policy rather than a tool for developing new reasoning pathways lacks a deep theoretical underpinning. The authors should provide a more robust theoretical framework that explains why RL’s impact is limited to selective corrections rather than broader improvements. Specifically, the paper needs to articulate why the observed behavior is not simply a consequence of the RL algorithm itself, but rather a fundamental property of how RL interacts with the model's pre-existing knowledge. A more detailed analysis of the reward structure and its influence on the model's learning process is needed to support this claim.
- The token-level analysis, while detailed, could be expanded to include a wider range of models and reasoning tasks. The current scope limits the generalizability of the findings, which may not hold true across different architectures or problem domains. For instance, the analysis does not explore how the identified high-entropy decision points vary across different model sizes or architectures, such as transformer variants with different attention mechanisms. Furthermore, the study should investigate the impact of different reasoning tasks, such as those requiring more complex logical inference or creative problem-solving, to determine the robustness of the findings.
- The proposed ReasonMaxxer method, while efficient, is compared against only a limited set of RL baselines. A broader comparison with other non-RL-based reasoning enhancement techniques would provide a more comprehensive evaluation of its effectiveness. The paper should include comparisons with methods that focus on prompt engineering, retrieval-augmented generation, or other techniques that aim to improve reasoning without relying on RL. This would help to contextualize the performance of ReasonMaxxer and highlight its unique advantages and limitations.

### Suggestions

To strengthen the paper's core argument, the authors should delve deeper into the theoretical underpinnings of why RL appears to act primarily as a selective policy. This could involve a more formal analysis of the RL algorithm's interaction with the model's internal representations and decision boundaries. For example, the authors could explore how the reward signal guides the model's attention to specific tokens, effectively pruning the search space and focusing learning on a limited set of high-entropy decision points. A comparative analysis of different RL algorithms, such as PPO and TRPO, could also shed light on whether the observed behavior is specific to certain RL methods or a more general phenomenon. Furthermore, the authors should investigate the impact of different reward shaping techniques on the model's learning process and the location of high-entropy decision points. This would help to determine whether the selective nature of RL is an inherent property of the algorithm or a consequence of specific reward designs.

To enhance the generalizability of the token-level analysis, the authors should expand their study to include a wider range of models and reasoning tasks. This could involve testing the hypothesis on models with different architectures, such as encoder-decoder models or models with different attention mechanisms. The authors should also explore the impact of different reasoning tasks, such as those requiring more complex logical inference or creative problem-solving. For example, the analysis could be extended to tasks that involve multi-hop reasoning or tasks that require the model to generate novel solutions. This would help to determine whether the identified high-entropy decision points are consistent across different problem domains and model architectures. Additionally, the authors should investigate the relationship between the model's pre-existing knowledge and its susceptibility to RL corrections. This could involve analyzing how the model's internal representations change after RL training and how these changes affect the location of high-entropy decision points.

To provide a more comprehensive evaluation of the ReasonMaxxer method, the authors should compare it against a broader range of non-RL-based reasoning enhancement techniques. This could include methods that focus on prompt engineering, retrieval-augmented generation, or other techniques that aim to improve reasoning without relying on RL. For example, the authors could compare ReasonMaxxer to methods that use chain-of-thought prompting or other forms of in-context learning. This would help to contextualize the performance of ReasonMaxxer and highlight its unique advantages and limitations. Furthermore, the authors should investigate the sensitivity of ReasonMaxxer to different hyperparameter settings and compare its performance to other fine-tuning methods. This would help to determine whether ReasonMaxxer is a robust and reliable method for improving reasoning in LLMs.

### Questions

- How does the proposed ReasonMaxxer method compare to other non-RL-based reasoning enhancement techniques? Are there specific advantages or limitations that make it uniquely suited for certain types of reasoning tasks?
- Can the authors elaborate on the theoretical basis for why RL appears to act primarily as a selective policy rather than a tool for developing new reasoning pathways? Is this behavior consistent across different RL algorithms or reward structures?
- How does the location and nature of high-entropy decision points vary across different model sizes and architectures? Are these points stable across various reasoning tasks, or do they differ significantly depending on the specific problem domain?

### Rating

6

### Confidence

4

**********

## Reviewer 2

### Summary

The authors investigate the role of RL in improving reasoning in LLMs and find that RL primarily steers the model towards correct solutions by correcting minor deviations rather than expanding new reasoning skills. They introduce ReasonMaxxer, an RL-free method that applies contrastive fine-tuning at high-entropy decision points, achieving comparable performance to RL-trained models with significantly reduced computational cost.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a thorough analysis of RL's role in reasoning, identifying key insights into how RL influences model behavior.
3. The proposed method, ReasonMaxxer, demonstrates strong performance with significantly lower computational costs, making it a practical alternative to traditional RL approaches.

### Weaknesses

#### Some Related Works


#### comment

1. The authors should clarify the meaning of the term "RL" in the abstract and introduction, as it is commonly associated with Reinforcement Learning. The current usage of "RL" is ambiguous and could be misinterpreted by readers familiar with the field.
2. The authors should provide a more detailed description of the oracle intervention experiment, including the specific criteria used to determine the correctness of the model's reasoning at each step. The current description lacks the necessary detail to fully understand the experimental setup and results.
3. The authors should provide a more detailed description of the entropy-based decision point selection process, including the specific parameters used and the rationale behind their selection. The current description lacks the necessary detail to fully understand the method's implementation and its impact on the results.
4. The authors should provide a more detailed description of the training process for ReasonMaxxer, including the specific hyperparameters used and the rationale behind their selection. The current description lacks the necessary detail to fully understand the method's implementation and its impact on the results.
5. The authors should provide a more detailed description of the evaluation metrics used, including the specific criteria used to assess the model's reasoning performance. The current description lacks the necessary detail to fully understand the evaluation process and the results.
6. The authors should provide a more detailed description of the experimental setup, including the specific hardware and software used. The current description lacks the necessary detail to fully understand the experimental environment and its potential impact on the results.
7. The authors should provide a more detailed description of the limitations of their method, including the potential biases and assumptions that may affect the results. The current description lacks the necessary detail to fully understand the method's limitations and potential impact on the results.
8. The authors should provide a more detailed description of the future directions for their research, including the potential applications and extensions of their method. The current description lacks the necessary detail to fully understand the future work and its potential impact.

### Suggestions

The paper would benefit from a more rigorous definition of the term "RL" early in the paper, explicitly stating that it refers to Reinforcement Learning and not to be confused with other uses of the acronym. This is crucial for clarity, especially for readers who are familiar with the field and may initially interpret "RL" in a different context. Furthermore, the authors should clarify the specific type of RL they are using, such as PPO or TRPO, and justify their choice. This would provide a more complete picture of the experimental setup and allow for better comparison with other works in the field. The authors should also provide a more detailed explanation of the reward function used in the RL training process, including how it is designed to encourage the desired behavior and how it is implemented in practice. This would help the reader understand the training process and the rationale behind the design choices.

To improve the clarity of the oracle intervention experiment, the authors should provide a more detailed description of the criteria used to determine the correctness of the model's reasoning at each step. This should include a clear definition of what constitutes a correct reasoning path and how this is evaluated. For example, if the model is generating a chain of reasoning, the authors should specify how they determine if the chain is logically sound and leads to the correct answer. The authors should also provide a more detailed description of the entropy-based decision point selection process, including the specific parameters used and the rationale behind their selection. This should include a discussion of how the entropy is calculated, what threshold is used to select decision points, and how this threshold is determined. The authors should also provide a more detailed description of the training process for ReasonMaxxer, including the specific hyperparameters used and the rationale behind their selection. This should include a discussion of how the hyperparameters are chosen, what their values are, and how they affect the performance of the method. The authors should also provide a more detailed description of the evaluation metrics used, including the specific criteria used to assess the model's reasoning performance. This should include a discussion of how the metrics are calculated and what they measure. The authors should also provide a more detailed description of the experimental setup, including the specific hardware and software used. This should include a discussion of the hardware specifications, the software versions, and any other relevant details that could affect the reproducibility of the results.

Finally, the authors should provide a more detailed description of the limitations of their method, including the potential biases and assumptions that may affect the results. This should include a discussion of the limitations of the method in terms of its applicability to different types of reasoning tasks and its sensitivity to different model architectures. The authors should also provide a more detailed description of the future directions for their research, including the potential applications and extensions of their method. This should include a discussion of how the method could be extended to other types of reasoning tasks and how it could be used to improve the performance of other models. By addressing these points, the authors can significantly improve the clarity, rigor, and impact of their paper.

### Questions

1. Could the authors clarify the specific type of RL used in their experiments (e.g., PPO, TRPO) and justify their choice?
2. How does the proposed method handle potential biases or assumptions that may affect the results?
3. What are the limitations of the proposed method in terms of its applicability to different types of reasoning tasks?
4. How does the performance of ReasonMaxxer compare to other RL-free methods for reasoning enhancement?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper investigates the role of RL in improving reasoning in LLMs. The authors argue that RL primarily steers existing abilities rather than fundamentally expanding new reasoning skills. They conduct a token-level analysis and identify that RL’s beneficial effect is a sparse, predictable, and low-dimensional correction. Based on this insight, they propose ReasonMaxxer, an RL-free method that applies contrastive fine-tuning at these critical decision points, achieving comparable performance to models trained with RL while significantly reducing computational costs.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow. The authors clearly articulate their motivation and methodology, making it accessible to a broad audience.
- The authors conduct a thorough analysis of the RL process at the token level, providing valuable insights into how RL operates. This analysis is both insightful and well-supported by empirical evidence.
- The proposed RL-free method, ReasonMaxxer, demonstrates impressive efficiency, achieving comparable performance to RL-trained models with a fraction of the computational resources. This practical outcome has significant implications for reducing the cost and complexity of improving reasoning in LLMs.

### Weaknesses

#### Some Related Works


#### comment

 - The paper’s core argument, while intriguing, could benefit from more rigorous justification. The claim that RL primarily functions as a selective policy rather than a tool for developing new reasoning pathways lacks a deep theoretical underpinning. The authors should provide a more robust theoretical framework that explains why RL’s impact is limited to selective corrections rather than broader improvements. Specifically, the paper needs to articulate why the observed behavior is not simply a consequence of the RL algorithm itself, but rather a fundamental property of how RL interacts with the model's pre-existing knowledge. A more detailed analysis of the reward structure and its influence on the model's learning process is needed to support this claim.
- The token-level analysis, while detailed, could be expanded to include a wider range of models and reasoning tasks. The current scope limits the generalizability of the findings, which may not hold true across different architectures or problem domains. For instance, the analysis does not explore how the identified high-entropy decision points vary across different model sizes or architectures, such as transformer variants with different attention mechanisms. Furthermore, the study should investigate the impact of different reasoning tasks, such as those requiring more complex logical inference or creative problem-solving, to determine the robustness of the findings.
- The proposed ReasonMaxxer method, while efficient, is compared against only a limited set of RL baselines. A broader comparison with other non-RL-based reasoning enhancement techniques would provide a more comprehensive evaluation of its effectiveness. The paper should include comparisons with methods that focus on prompt engineering, retrieval-augmented generation, or other techniques that aim to improve reasoning without relying on RL. This would help to contextualize the performance of ReasonMaxxer and highlight its unique advantages and limitations.

### Suggestions

To strengthen the theoretical foundation of the paper, the authors should delve deeper into the interaction between the RL algorithm and the model's pre-existing knowledge. This could involve a more detailed analysis of the reward function and its impact on the model's learning trajectory. Specifically, the authors should investigate how the reward signal guides the model's attention to specific tokens, effectively pruning the search space and focusing learning on a limited set of high-entropy decision points. A comparative analysis of different RL algorithms, such as PPO and TRPO, could also shed light on whether the observed behavior is specific to certain RL methods or a more general phenomenon. Furthermore, the authors should explore the impact of different reward shaping techniques on the model's learning process and the location of high-entropy decision points. This would help to determine whether the selective nature of RL is an inherent property of the algorithm or a consequence of specific reward designs. A more rigorous theoretical framework would provide a stronger basis for the paper's claims and enhance its overall impact.

To address the limitations of the token-level analysis, the authors should expand their study to include a wider range of models and reasoning tasks. This could involve testing the hypothesis on models with different architectures, such as encoder-decoder models or models with different attention mechanisms. The authors should also explore the impact of different reasoning tasks, such as those requiring multi-hop reasoning or creative problem-solving, to determine the robustness of their findings. For example, the analysis could be extended to tasks that involve more complex logical inference or tasks that require the model to generate novel solutions. This would help to determine whether the identified high-entropy decision points are consistent across different problem domains and model architectures. Furthermore, the authors should investigate how the location and nature of high-entropy decision points vary across different model sizes and training regimes. This would provide a more comprehensive understanding of the factors that influence the effectiveness of RL in improving reasoning in LLMs.

Finally, to provide a more comprehensive evaluation of the proposed ReasonMaxxer method, the authors should compare it against a broader range of non-RL-based reasoning enhancement techniques. This could include methods that focus on prompt engineering, retrieval-augmented generation, or other techniques that aim to improve reasoning without relying on RL. For example, the authors could compare ReasonMaxxer to methods that use chain-of-thought prompting or other forms of in-context learning. This would help to contextualize the performance of ReasonMaxxer and highlight its unique advantages and limitations. Furthermore, the authors should investigate the sensitivity of ReasonMaxxer to different hyperparameter settings and compare its performance to other fine-tuning methods. This would help to determine whether ReasonMaxxer is a robust and reliable method for improving reasoning in LLMs. A more comprehensive comparison would provide a more complete picture of the effectiveness of ReasonMaxxer and its potential for practical applications.

### Questions

- How does the proposed ReasonMaxxer method compare to other non-RL-based reasoning enhancement techniques? Are there specific advantages or limitations that make it uniquely suited for certain types of reasoning tasks?
- Can the authors elaborate on the theoretical basis for why RL appears to act primarily as a selective policy rather than a tool for developing new reasoning pathways? Is this behavior consistent across different RL algorithms or reward structures?
- How does the location and nature of high-entropy decision points vary across different model sizes and architectures? Are these points stable across various reasoning tasks, or do they differ significantly depending on the specific problem domain?

### Rating

8

### Confidence

3

**********

## Reviewer 4

### Summary

This paper studies the role of RL in improving reasoning in LLMs. The authors find that RL's benefits are concentrated in sparse, high-entropy decision points where the model is uncertain which reasoning branch to take. They then propose a method called ReasonMaxxer, which applies contrastive fine-tuning at these critical decision points, achieving comparable performance to RL-trained models while using significantly less compute and data.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow.
- The authors conduct a thorough analysis of RL's role in reasoning, identifying key insights into how RL influences model behavior.
- The proposed method, ReasonMaxxer, demonstrates strong performance with significantly lower computational costs, making it a practical alternative to traditional RL approaches.

### Weaknesses

#### Some Related Works


#### comment

 - The paper could benefit from a more detailed discussion of the limitations of the proposed method and potential areas for future research. For example, it would be helpful to explore the sensitivity of ReasonMaxxer to different hyperparameters and model architectures. Specifically, the paper lacks a discussion on how the choice of the contrastive loss function parameters might affect the performance of ReasonMaxxer, and whether these parameters need to be tuned differently for various model sizes or datasets. Furthermore, the paper does not address the potential for overfitting when applying contrastive fine-tuning at high-entropy decision points, and how this might impact the generalization ability of the model on unseen reasoning tasks.
- The authors could provide more details on the specific implementation of the entropy-based decision point selection process. It would be helpful to understand how the entropy threshold is determined and whether this threshold is consistent across different models and datasets. The paper does not specify the exact method used to calculate entropy, nor does it discuss the potential impact of different entropy calculation methods on the selection of decision points. For instance, using a moving average of past entropy values versus a fixed window could lead to different sets of decision points and potentially impact the final performance.
- The paper could include a more comprehensive comparison with existing RL-free methods for reasoning enhancement. While the authors compare against some baselines, a more thorough analysis of the strengths and weaknesses of ReasonMaxxer compared to other approaches would be valuable. This comparison should include not only performance metrics but also computational costs and data requirements. It would be beneficial to see how ReasonMaxxer performs against methods that use techniques like chain-of-thought prompting or other forms of in-context learning, to better understand its relative advantages and disadvantages.

### Suggestions

To strengthen the paper, the authors should include a more detailed analysis of the hyperparameter sensitivity of ReasonMaxxer. Specifically, they should investigate how the choice of contrastive loss function parameters, such as the temperature parameter and the weighting of the contrastive loss, affects the performance of the method. A grid search or a more systematic approach to hyperparameter tuning should be performed, and the results should be reported in the paper. Furthermore, the authors should explore the impact of different entropy calculation methods on the selection of decision points. For example, they could compare the use of a moving average of past entropy values with a fixed window, or with other methods such as exponential moving average. The paper should also discuss the potential for overfitting when applying contrastive fine-tuning at high-entropy decision points, and how this might impact the generalization ability of the model on unseen reasoning tasks. Techniques such as regularization or early stopping could be explored to mitigate this issue.

In addition, the authors should provide a more comprehensive comparison with existing RL-free methods for reasoning enhancement. This comparison should include not only performance metrics but also computational costs and data requirements. The authors should compare ReasonMaxxer against methods that use techniques like chain-of-thought prompting or other forms of in-context learning, to better understand its relative advantages and disadvantages. A detailed analysis of the strengths and weaknesses of ReasonMaxxer compared to other approaches would be valuable, and should include a discussion of the trade-offs between performance, computational cost, and data requirements. This would help to better position ReasonMaxxer within the broader landscape of reasoning enhancement techniques and provide a more complete picture of its practical applicability.

Finally, the authors should discuss the limitations of their method in more detail. This should include a discussion of the potential for overfitting, the sensitivity of the method to hyperparameter choices, and the potential for the method to fail on certain types of reasoning tasks. The authors should also discuss the potential for the method to be extended to other types of reasoning tasks, and the challenges that might need to be addressed. A more thorough discussion of these limitations would help to provide a more balanced and nuanced view of the method's capabilities and limitations, and would help to guide future research in this area.

### Questions

- How does the proposed ReasonMaxxer method compare to other non-RL-based reasoning enhancement techniques? Are there specific advantages or limitations that make it uniquely suited for certain types of reasoning tasks?
- Can the authors elaborate on the theoretical basis for why RL appears to act primarily as a selective policy rather than a tool for developing new reasoning pathways? Is this behavior consistent across different RL algorithms or reward structures?
- How does the location and nature of high-entropy decision points vary across different model sizes and architectures? Are these points stable across various reasoning tasks, or do they differ significantly depending on the specific problem domain?

### Rating

8

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

Plan:
1. Go through each reviewer's comments one by one.
2. For each comment identified as a weakness, find the corresponding section in the paper.
3. Extract evidence (quotes, experimental details, missing citations) to support the reviewer's claim.
4. If the weakness is about missing information, check if that information is indeed absent.
5. If there are conflicting opinions, note them.
6. Finally, conclude whether the weakness is valid, partially valid, or invalid based on the evidence.
**Review 1 Weaknesses:**

1. Weakness Statement:
"The paper’s core argument, while intriguing, could benefit from more rigorous justification. The claim that RL primarily functions as a selective policy rather than a tool for developing new reasoning pathways lacks a deep theoretical underpinning. The authors should provide a more robust theoretical framework that explains why RL’s impact is limited to selective corrections rather than broader improvements. Specifically, the paper needs to articulate why the observed behavior is not simply a consequence of the RL algorithm itself, but rather a fundamental property of how RL interacts with the model's pre-existing knowledge. A more detailed analysis of the reward structure and its influence on the model's learning process is needed to support this claim."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper introduces the idea of RL acting as a "selective policy" in the "main_idea" section: "The paper introduces ReasonMaxxer, a method that applies contrastive fine-tuning at high-entropy decision points to improve reasoning in LLMs, challenging the conventional view that RL optimizes models to explore new reasoning strategies."
   - The "main_idea" section also states: "This suggests that the benefits of RL are concentrated in a small fraction of the model's decision space, rather than being a fundamental change in the model's reasoning capabilities."
   - The "method" section describes the oracle intervention as "a technique to validate the RL model's ability to correct the model's reasoning trajectory at decision points." This implies RL is correcting existing behavior.
   - The "method" section also states: "The oracle intervention is a technique to validate the RL model's ability to correct the model's reasoning trajectory at decision points." This suggests RL is correcting existing behavior.
   - The paper does not provide a deep theoretical analysis of why RL's impact is limited to selective corrections.

b) Experiment-related Evidence:
   - The paper presents empirical evidence in Figure 1 and Table 2 supporting the claim that RL's benefits are concentrated at high-entropy decision points.
   - The paper does not include experiments that directly analyze the reward structure's influence on the model's learning process.

3. Literature Gap Analysis:
   - The paper cites works that support the idea that RL primarily steers existing abilities (Wang et al., Davis and Recht, Zhang et al., Park et al.). However, it doesn't provide a novel theoretical framework explaining *why* this is the case.

4. Validation Analysis:
   - Primary evidence suggests the paper's core argument is based on empirical observation and the behavior of RL as a selective intervention. While the paper cites related work, it doesn't offer a deep theoretical explanation for the observed behavior. The reviewer correctly points out the lack of a robust theoretical framework.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of a deep theoretical analysis explaining why RL acts as a selective policy beyond empirical observation.

1. Weakness Statement:
"The token-level analysis, while detailed, could be expanded to include a wider range of models and reasoning tasks. The current scope limits the generalizability of the findings, which may not hold true across different architectures or problem domains. For instance, the analysis does not explore how the identified high-entropy decision points vary across different model sizes or architectures, such as transformer variants with different attention mechanisms. Furthermore, the study should investigate the impact of different reasoning tasks, such as those requiring more complex logical inference or creative problem-solving, to determine the robustness of the findings."

2. Evidence Collection:
a) Method-related Evidence:
   - The "method" section describes the token-level analysis focusing on the four base/RL-tuned pairs introduced in Section 2.3.
   - The paper mentions the models used: Qwen2.5-1.5B, GPT-3.5, GPT-4, and Mistral-7B, but the token-level analysis is presented within the context of the specific base/RL-tuned pairs.

b) Experiment-related Evidence:
   - Figure 1 and Table 2 present the results of the token-level analysis for these specific pairs.
   - The paper does not include experiments analyzing high-entropy decision points across a wider range of models or different reasoning tasks.

3. Literature Gap Analysis:
   - The paper does not cite works that specifically analyze the consistency of high-entropy decision points across different model architectures or reasoning tasks.

4. Validation Analysis:
   - The paper's token-level analysis is indeed limited to the specific base/RL-tuned pairs. The reviewer's point about the limited scope and potential impact on generalizability is valid.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The token-level analysis is performed on a limited set of base/RL-tuned pairs.

1. Weakness Statement:
"The proposed ReasonMaxxer method, while efficient, is compared against only a limited set of RL baselines. A broader comparison with other non-RL-based reasoning enhancement techniques would provide a more comprehensive evaluation of its effectiveness. The paper should include comparisons with methods that focus on prompt engineering, retrieval-augmented generation, or other techniques that aim to improve reasoning without relying on RL. This would help to contextualize the performance of ReasonMaxxer and highlight its unique advantages and limitations."

2. Evidence Collection:
a) Experiment-related Evidence:
   - The "experiments" section lists the baselines used for comparison: SimpleRL-Zoo, DeepScaleR, and STaR.
   - The paper does not include comparisons with methods like prompt engineering or retrieval-augmented generation.

3. Literature Gap Analysis:
   - The "related_work" section mentions prompt engineering and retrieval-augmented generation but doesn't include them as experimental baselines.

4. Validation Analysis:
   - The reviewer is correct that the experimental evaluation primarily focuses on comparisons with RL-based methods. Including other non-RL baselines would provide a broader context for evaluating ReasonMaxxer's effectiveness.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The experimental section only compares ReasonMaxxer against other RL-based methods.

**Review 2 Weaknesses:**

1. Weakness Statement:
"The paper could benefit from a more detailed discussion of the limitations of the proposed method and potential areas for future research. For example, it would be helpful to explore the sensitivity of ReasonMaxxer to different hyperparameters and model architectures. Specifically, the paper lacks a discussion on how the choice of the contrastive loss function parameters might affect the performance of ReasonMaxxer, and whether these parameters need to be tuned differently for various model sizes or datasets. Furthermore, the paper does not address the potential for overfitting when applying contrastive fine-tuning at high-entropy decision points, and how this might impact the generalization ability of the model on unseen reasoning tasks."

2. Evidence Collection:
a) Method-related Evidence:
   - The "method" section describes the contrastive loss function but does not delve into the sensitivity to its parameters.
   - The paper mentions the use of LoRA for fine-tuning but doesn't discuss its sensitivity to LoRA hyperparameters.

b) Experiment-related Evidence:
   - The "experiments" section provides details on the training configuration for ReasonMaxxer but doesn't include a sensitivity analysis of its hyperparameters.
   - The paper does not explicitly address the potential for overfitting or the generalization ability beyond the tested datasets.

3. Literature Gap Analysis:
   - While the paper cites LoRA, it doesn't discuss literature on the sensitivity of LoRA or contrastive learning to hyperparameters.

4. Validation Analysis:
   - The reviewer correctly points out the lack of a detailed discussion on the limitations of ReasonMaxxer, including hyperparameter sensitivity and potential overfitting.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks a dedicated section or experiments discussing the sensitivity of ReasonMaxxer's hyperparameters and potential overfitting.

1. Weakness Statement:
"The authors could provide more details on the specific implementation of the entropy-based decision point selection process. It would be helpful to understand how the entropy threshold is determined and whether this threshold is consistent across different models and datasets. The paper does not specify the exact method used to calculate entropy, nor does it discuss the potential impact of different entropy calculation methods on the selection of decision points. For instance, using a moving average of past entropy values versus a fixed window could lead to different sets of decision points and potentially impact the final performance."

2. Evidence Collection:
a) Method-related Evidence:
   - The "method" section describes the entropy-based selection process: "The entropy of a token is calculated as H_t = - Σ p_i log p_i, where p_i is the probability of token i appearing in the model's output. A threshold τ is set to identify decision points where the entropy exceeds this value."
   - The paper mentions "a threshold τ is set to identify decision points where the entropy exceeds this value" but does not specify how this threshold is determined or if it's consistent across models/datasets.
   - The paper does not detail the specific method used to calculate entropy (e.g., per token, per sequence, etc.).

b) Experiment-related Evidence:
   - The "experiments" section mentions the entropy threshold (τ = 1.2) used for Mistral-7B but doesn't specify how this threshold was chosen or if it's consistent across other models.

3. Literature Gap Analysis:
   - The paper cites works that use entropy-based methods, but it doesn't discuss the specific choices and their implications in detail.

4. Validation Analysis:
   - The reviewer is correct that the paper lacks details on how the entropy threshold is determined and the method for calculating entropy. The potential impact of different entropy calculation methods is also not discussed.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks details on the threshold determination and entropy calculation method.

1. Weakness Statement:
"The paper could include a more comprehensive comparison with existing RL-free methods for reasoning enhancement. While the authors compare against some baselines, a more thorough analysis of the strengths and weaknesses of ReasonMaxxer compared to other approaches would be valuable. This comparison should include not only performance metrics but also computational costs and data requirements. It would be beneficial to see how ReasonMaxxer performs against methods that use techniques like chain-of-thought prompting or other forms of in-context learning, to better understand its relative advantages and disadvantages."

2. Evidence Collection:
a) Experiment-related Evidence:
   - The "experiments" section compares ReasonMaxxer against RL-based baselines.
   - The paper does not include comparisons with RL-free methods like chain-of-thought prompting or other in-context learning techniques.

3. Literature Gap Analysis:
   - The "related_work" section mentions some RL-free methods but doesn't include them as experimental baselines.

4. Validation Analysis:
   - The reviewer's point about the need for a more comprehensive comparison with a broader range of RL-free methods is valid.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The experimental section lacks comparisons with a wide range of RL-free reasoning enhancement techniques.

**Review 3 Weaknesses:**

1. Weakness Statement:
"The authors should clarify the meaning of the term "RL" in the abstract and introduction, as it is commonly associated with Reinforcement Learning. The current usage of "RL" is ambiguous and could be misinterpreted by readers familiar with the field and may initially interpret "RL" in a different context. Furthermore, the authors should clarify the specific type of RL they are using, such as PPO or TRPO, and justify their choice. This would provide a more complete picture of the experimental setup and allow for better comparison with other works in the field. The authors should also provide a more detailed explanation of the reward function used in the RL training process, including how it is designed to encourage the desired behavior and how it is implemented in practice. This would help the reader understand the training process and the rationale behind the design choices."

2. Evidence Collection:
a) Method-related Evidence:
   - The abstract mentions "reinforcement learning with verifiable rewards (RLVR)".
   - The introduction mentions "reinforcement learning with verifiable rewards (RLVR)".
   - The paper does not explicitly define what type of RL is used (e.g., PPO, TRPO) or justify the choice.
   - The paper describes the reward function in the "method" section: "The reward function is designed to encourage tokens leading to correct answers while penalizing those that lead to incorrect ones." However, it doesn't provide the exact mathematical formulation or implementation details.

3. Literature Gap Analysis:
   - While the paper cites works on RL in LLMs, it doesn't specify the RL algorithms used in those works for direct comparison.

4. Validation Analysis:
   - The reviewer is correct that the initial usage of "RL" could be ambiguous. The lack of specification of the RL algorithm and reward function details is also a valid point.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper uses "RL" without specifying the algorithm and provides a high-level description of the reward function without implementation details.

1. Weakness Statement:
"To improve the clarity of the oracle intervention experiment, the authors should provide a more detailed description of the criteria used to determine the correctness of the model's reasoning at each step. The current description lacks the necessary detail to fully understand the experimental setup and results."

2. Evidence Collection:
a) Method-related Evidence:
   - The "method" section describes the oracle intervention: "The oracle intervention involves re-encoding the model's outputs at the decision points using the same base model and comparing each token to the correct answer."
   - The paper states: "The oracle intervention reveals that the RL model's performance is not solely due to the base model's capabilities but is also influenced by the RL policy's corrective signals."
   - The paper does not provide specific criteria for determining correctness beyond the comparison with the correct answer.

3. Literature Gap Analysis:
   - The paper cites works on oracle intervention but doesn't provide detailed implementation specifics.

4. Validation Analysis:
   - The reviewer is correct that the description of the correctness criteria could be more detailed.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper mentions comparing with the correct answer but lacks specific details on the correctness criteria.

1. Weakness Statement:
"The authors should provide a more detailed description of the entropy-based decision point selection process, including the specific parameters used and the rationale behind their selection. This should include a discussion of how the entropy is calculated, what threshold is used to select decision points, and how this threshold is determined. The authors should also provide a more detailed description of the training process for ReasonMaxxer, including the specific hyperparameters used and the rationale behind their selection. This should include a discussion of how the hyperparameters are chosen, what their values are, and how they affect the performance of the method. The current description lacks the necessary detail to fully understand the method's implementation and its potential impact on the results."

2. Evidence Collection:
a) Method-related Evidence:
   - The "method" section describes the entropy-based selection: "The entropy of a token is calculated as H_t = - Σ p_i log p_i, where p_i is the probability of token i appearing in the model's output. A threshold τ is set to identify decision points where the entropy exceeds this value."
   - The paper mentions the threshold τ = 1.2 for Mistral-7B but doesn't detail how this threshold was chosen or if it's consistent.
   - The paper describes the training process for ReasonMaxxer but lacks specific hyperparameter details and rationale.

b) Experiment-related Evidence:
   - The "experiments" section provides some training details but lacks comprehensive hyperparameter information.

3. Literature Gap Analysis:
   - The paper cites works on entropy-based methods but doesn't provide detailed implementation specifics.

4. Validation Analysis:
   - The reviewer is correct that the paper lacks detailed descriptions of the entropy threshold selection, hyperparameter choices, and their rationale.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks specific details on entropy threshold selection and hyperparameter choices for ReasonMaxxer.

1. Weakness Statement:
"The authors should provide a more detailed description of the evaluation metrics used, including the specific criteria used to assess the model's reasoning performance. The current description lacks the necessary detail to fully understand the evaluation process and the results."

2. Evidence Collection:
a) Experiment-related Evidence:
   - The "experiments" section mentions the evaluation metric: "We evaluate on MATH-500 with deterministic decoding ( T = 0 ) and greedy decoding ( T = 0.5 ) to reduce variance; for all other benchmarks we report standard pass@1 from a single generation."
   - The paper does not provide a detailed explanation of the "standard pass@1" metric or the specific criteria used for evaluation beyond the number of correct answers.

3. Literature Gap Analysis:
   - The paper cites benchmarks but doesn't elaborate on the evaluation metrics used for those benchmarks.

4. Validation Analysis:
   - The reviewer is correct that the description of the evaluation metrics could be more detailed.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper mentions the evaluation metric but lacks a detailed explanation of its criteria.

1. Weakness Statement:
"The authors should provide a more detailed description of the experimental setup, including the specific hardware and software used. This should include a discussion of the hardware specifications, the software versions, and any other relevant details that could affect the reproducibility of the results."

2. Evidence Collection:
a) Experiment-related Evidence:
   - The "experiments" section mentions the hardware: "All baselines are trained on NVIDIA RTX Pro 6000 (96 GB) GPUs using RunPod on-demand pricing and include rollout generation, entropy scoring, the τ sweep, and checkpoint selection."
   - The paper does not provide specific software versions or other implementation details that could affect reproducibility.

3. Literature Gap Analysis:
   - The paper cites hardware specifications but doesn't provide software details.

4. Validation Analysis:
   - The reviewer is correct that the description of the experimental setup lacks details on software versions and other implementation specifics.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper provides hardware details but lacks software version information and other implementation specifics.

1. Weakness Statement:
"The authors should provide a more detailed description of the limitations of their method, including the potential biases and assumptions that may affect the results. This should include a discussion of the limitations of the method in terms of its applicability to different types of reasoning tasks and its sensitivity to different model architectures. The current description lacks the necessary detail to fully understand the method's limitations and potential impact on the results."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper briefly mentions the focus on four base/RL-tuned pairs in the "experiments" section.

b) Experiment-related Evidence:
   - The paper does not include a dedicated section discussing the limitations of ReasonMaxxer.

3. Literature Gap Analysis:
   - The paper does not cite works that discuss the limitations of similar methods in detail.

4. Validation Analysis:
   - The reviewer is correct that the paper lacks a detailed discussion of the limitations of ReasonMaxxer.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks a dedicated section or detailed discussion on the limitations of ReasonMaxxer.

1. Weakness Statement:
"The authors should provide a more detailed description of the future directions for their research, including the potential applications and extensions of their method. This should include a discussion of how the method could be extended to other types of reasoning tasks and how it could be used to improve the performance of other models. This would help to determine whether the method is consistent across different problem domains and its sensitivity to different model architectures. The current description lacks the necessary detail to fully understand the future work and its potential impact."

2. Evidence Collection:
a) Conclusion Section:
   - The conclusion mentions future work: "Recognizing this simplicity opens the door to a generation of far more efficient post-training methods. Recognizing this simplicity opens the door to a generation of far more efficient post-training methods. Acknowledging this simplicity opens the door to a generation of far more efficient post-training methods."
   - The conclusion does not provide specific details on future directions, applications, or extensions of the method.

3. Literature Gap Analysis:
   - The paper does not cite works that discuss future research directions in detail.

4. Validation Analysis:
   - The reviewer is correct that the description of future directions is brief and lacks specific details.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: Medium
   - Key supporting evidence: The conclusion mentions future work but lacks specific details.

**Review 4 Weaknesses:**

1. Weakness Statement:
"The paper’s core argument, while intriguing, could benefit from more rigorous justification. The claim that RL primarily functions as a selective policy rather than a tool for developing new reasoning pathways lacks a deep theoretical underpinning. The authors should provide a more robust theoretical framework that explains why RL’s impact is limited to selective corrections rather than broader improvements. Specifically, the paper needs to articulate why the observed behavior is not simply a consequence of the RL algorithm itself, but rather a fundamental property of how RL interacts with the model's pre-existing knowledge. A more detailed analysis of the reward function and its influence on the model's learning process is needed to support this claim."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper introduces the idea of RL acting as a "selective policy" in the "main_idea" section: "The paper introduces ReasonMaxxer, a method that applies contrastive fine-tuning at high-entropy decision points to improve reasoning in LLMs, challenging the conventional view that RL optimizes models to explore new reasoning strategies."
   - The "main_idea" section also states: "This suggests that the benefits of RL are concentrated in a small fraction of the model's decision space, rather than being a fundamental change in the model's reasoning capabilities."
   - The paper does not provide a deep theoretical analysis of why RL's impact is limited to selective corrections.

b) Experiment-related Evidence:
   - The paper presents empirical evidence in Figure 1 and Table 2 supporting the claim that RL's benefits are concentrated at high-entropy decision points.
   - The paper does not include experiments analyzing the reward function's influence on the model's learning process.

3. Literature Gap Analysis:
   - The paper cites works that support the idea that RL primarily steers existing abilities, but it doesn't offer a novel theoretical framework explaining *why* this is the case.

4. Validation Analysis:
   - The reviewer's point about the lack of a deep theoretical underpinning is valid, as discussed in the validation of Reviewer 1's first weakness.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper's core argument relies on empirical observation and cited works, lacking a novel theoretical framework.

1. Weakness Statement:
"The token-level analysis, while detailed, could be expanded to include a wider range of models and reasoning tasks. The current scope limits the generalizability of the findings, which may not hold true across different architectures or problem domains. For instance, the analysis does not explore how the identified high-entropy decision points vary across different model sizes or architectures, such as transformer variants with different attention mechanisms. Furthermore, the study should investigate the impact of different reasoning tasks, such as those requiring more complex logical inference or creative problem-solving, to determine the robustness of the findings."

2. Evidence Collection:
a) Method-related Evidence:
   - The "method" section describes the token-level analysis focusing on the four base/RL-tuned pairs introduced in Section 2.3.

b) Experiment-related Evidence:
   - Figure 1 and Table 2 present the results of the token-level analysis for these specific pairs.
   - The paper does not include experiments analyzing high-entropy decision points across a wider range of models or different reasoning tasks.

3. Literature Gap Analysis:
   - The paper does not cite works that specifically analyze the consistency of high-entropy decision points across different model architectures or reasoning tasks.

4. Validation Analysis:
   - The reviewer's point about the limited scope of the token-level analysis is valid, as discussed in the validation of Reviewer 1's second weakness.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The token-level analysis is performed on a limited set of base/RL-tuned pairs.

1. Weakness Statement:
"The proposed ReasonMaxxer method, while efficient, is compared against only a limited set of RL baselines. A broader comparison with other non-RL-based reasoning enhancement techniques would provide a more comprehensive evaluation of its effectiveness. The paper should include comparisons with methods that focus on prompt engineering, retrieval-augmented generation, or other techniques that aim to improve reasoning without relying on RL. This would help to contextualize the performance of ReasonMaxxer and highlight its unique advantages and limitations."

2. Evidence Collection:
a) Experiment-related Evidence:
   - The "experiments" section lists the baselines used for comparison: SimpleRL-Zoo, DeepScaleR, and STaR.
   - The paper does not include comparisons with methods like prompt engineering or retrieval-augmented generation.

3. Literature Gap Analysis:
   - The "related_work" section mentions prompt engineering and retrieval-augmented generation but doesn't include them as experimental baselines.

4. Validation Analysis:
   - The reviewer's point about the limited set of RL baselines is valid, as discussed in the validation of Reviewer 1's third weakness.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The experimental section only compares ReasonMaxxer against other RL-based methods.

**Synthesis and Reflection:**

After analyzing the reviewer comments and comparing them with the paper's content, several recurring themes emerge:

*   **Lack of Deep Theoretical Justification:** Multiple reviewers (R1, R4) point out that the paper's core argument about RL acting as a selective policy lacks a robust theoretical framework. The paper relies more on empirical evidence and cited works than on developing a novel theoretical explanation.
*   **Limited Scope of Analysis:** Reviewers (R1, R2, R4) consistently highlight the limited scope of the token-level analysis and the comparison with only RL-based baselines. The paper focuses on a specific set of models and reasoning tasks, and the generalizability of the findings is questioned.
*   **Missing Implementation Details:** Reviewers (R3) identify a lack of detail in the description of the oracle intervention, entropy-based decision point selection, evaluation metrics, experimental setup, and hyperparameter choices.
*   **Need for Broader Evaluation:** Reviewers (R2, R3) suggest a more comprehensive evaluation by including comparisons with a wider range of RL-free reasoning enhancement techniques.
*   **Limited Discussion of Limitations:** Reviewers (R2, R3) note the absence of a detailed discussion on the limitations of the proposed ReasonMaxxer method, including hyperparameter sensitivity, potential for overfitting, and applicability across different model architectures and tasks.

There are no significant contradictions between the reviewers' opinions. They largely converge on the need for more theoretical depth, broader empirical validation, and more detailed methodological explanations.

**Conclusion:**

Based on the evidence collected, the majority of the weaknesses identified by the reviewers are **valid**. The paper could be significantly strengthened by addressing these points through more rigorous theoretical analysis, expanding the scope of the empirical evaluation, providing more detailed methodological descriptions, and discussing the limitations of the proposed method more thoroughly.

**Confidence Level: High** for the validity of the major weaknesses, as there is clear evidence from the paper to support these criticisms.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper presents a compelling investigation into the role of Reinforcement Learning (RL) in enhancing the reasoning capabilities of Large Language Models (LLMs). The authors challenge the prevailing notion that RL is a panacea for improving reasoning, instead demonstrating that its benefits are often localized to specific decision points within the model's reasoning trajectory. This finding suggests that RL primarily functions as a selective policy, guiding the model towards correct answers by correcting minor deviations rather than fundamentally expanding the model's reasoning abilities. To further explore this, the authors conduct a detailed token-level analysis, identifying that RL's impact is concentrated in sparse, high-entropy decision points where the model is uncertain. This analysis leads to the proposal of ReasonMaxxer, an RL-free method that applies contrastive fine-tuning at these critical decision points. The authors show that ReasonMaxxer achieves comparable performance to RL-trained models, with significantly reduced computational costs, making it a practical alternative for improving reasoning in LLMs. The core of the paper lies in its empirical findings, which are supported by a series of well-designed experiments. The authors analyze the behavior of RL across multiple models and reasoning tasks, providing a thorough analysis of the RL process at the token level. They demonstrate that RL's benefits are concentrated in a small fraction of the model's decision space, rather than being a fundamental change in the model's reasoning capabilities. This insight is crucial for understanding the limitations of RL and for developing more efficient methods for improving reasoning in LLMs. The proposed ReasonMaxxer method is a practical and effective alternative to RL, offering a computationally cheaper way to improve reasoning in LLMs. The paper's overall significance lies in its challenge to the conventional wisdom surrounding RL and its demonstration of a more efficient and targeted approach to improving reasoning in LLMs. By highlighting the localized nature of RL's impact, the authors pave the way for more focused and efficient methods for enhancing the reasoning abilities of these models. The paper's findings have important implications for the development of future LLMs and for the application of RL in other areas of machine learning.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

2.75


## Strengths:

This paper has several notable strengths that contribute to its overall impact and significance. First and foremost, the paper presents a novel perspective on the role of RL in LLM reasoning. Instead of viewing RL as a tool for developing new reasoning pathways, the authors demonstrate that it primarily functions as a selective policy, correcting minor deviations rather than fundamentally expanding the model's reasoning abilities. This reframing of RL's role is a significant contribution to the field and challenges the conventional understanding of its impact on LLMs. The authors' token-level analysis is another key strength of the paper. By examining the behavior of RL at the token level, they provide a detailed and insightful view of how RL influences model behavior. This analysis is both novel and well-supported by empirical evidence, demonstrating that RL's benefits are concentrated in a small fraction of the model's decision space. This finding is crucial for understanding the limitations of RL and for developing more efficient methods for improving reasoning in LLMs. The proposed ReasonMaxxer method is a practical and effective alternative to RL, offering a computationally cheaper way to improve reasoning in LLMs. The authors demonstrate that ReasonMaxxer achieves comparable performance to RL-trained models, while using significantly less computational resources. This makes it a practical and valuable tool for improving reasoning in LLMs, particularly in resource-constrained settings. The paper is also well-written and easy to follow, making it accessible to a broad audience. The authors clearly articulate their motivation, methodology, and findings, and they provide a thorough explanation of the experimental setup and results. The use of clear and concise language enhances the paper's overall impact and makes it easier for readers to understand the key contributions. Finally, the paper's findings have important implications for the development of future LLMs and for the application of RL in other areas of machine learning. The authors' work highlights the need for a more targeted and efficient approach to improving reasoning in LLMs, and their proposed ReasonMaxxer method provides a valuable step in this direction. The paper's overall contribution is significant, and it has the potential to influence future research in this area.


## Weaknesses:

Despite its strengths, this paper has several weaknesses that warrant careful consideration. A primary concern is the lack of a deep theoretical underpinning for the claim that RL primarily functions as a selective policy. While the authors present compelling empirical evidence, they do not provide a robust theoretical framework that explains why RL's impact is limited to selective corrections rather than broader improvements. The paper cites works that support the idea that RL primarily steers existing abilities, but it does not offer a novel theoretical explanation for this phenomenon. This lack of a theoretical foundation weakens the paper's overall argument and leaves open the possibility that the observed behavior is simply a consequence of the RL algorithm itself, rather than a fundamental property of how RL interacts with the model's pre-existing knowledge. This is a significant limitation, as it undermines the paper's core claim and makes it difficult to generalize the findings to other contexts. My confidence in this weakness is high, as it is directly evident from the paper's lack of theoretical analysis and the absence of citations to relevant theoretical frameworks. Another significant weakness is the limited scope of the token-level analysis. The analysis is conducted on a specific set of base/RL-tuned pairs, and the paper does not explore how the identified high-entropy decision points vary across different model sizes or architectures, such as transformer variants with different attention mechanisms. Furthermore, the study does not investigate the impact of different reasoning tasks, such as those requiring more complex logical inference or creative problem-solving. This narrow focus limits the generalizability of the findings, and it is unclear whether the identified high-entropy decision points are consistent across different problem domains and model architectures. This is a major limitation, as it restricts the applicability of the paper's conclusions and raises questions about the robustness of the findings. My confidence in this weakness is high, as it is directly evident from the paper's limited scope of analysis and the lack of experiments on diverse models and tasks. The paper also suffers from a lack of detail in several key areas. The description of the oracle intervention experiment lacks specific details on the correctness criteria used to determine the model's reasoning at each step. The paper mentions that the model is re-encoding the outputs using the same base model and comparing each token to the correct answer, but it does not provide a detailed explanation of how the correctness is assessed. This lack of detail makes it difficult to fully understand the experimental setup and the results. Additionally, the paper lacks a detailed description of the entropy-based decision point selection process. While the paper mentions the use of entropy to identify high-entropy decision points, it does not specify how the entropy threshold is determined or if it is consistent across different models and datasets. The paper also does not provide a detailed description of the training process for ReasonMaxxer, including the specific hyperparameters used and the rationale behind their selection. The paper mentions the use of LoRA for fine-tuning, but it does not provide the specific parameters used or the rationale behind their selection. These omissions make it difficult to reproduce the results and to fully understand the method's implementation. My confidence in this weakness is high, as it is directly evident from the paper's lack of detailed descriptions in these areas. Furthermore, the paper's experimental evaluation is limited by the comparison with only a few RL-based baselines. The paper does not include comparisons with other non-RL-based reasoning enhancement techniques, such as methods that focus on prompt engineering, retrieval-augmented generation, or other techniques that aim to improve reasoning without relying on RL. This limited comparison makes it difficult to contextualize the performance of ReasonMaxxer and to assess its unique advantages and limitations. The paper should include comparisons with a broader range of methods to provide a more comprehensive evaluation of its effectiveness. My confidence in this weakness is high, as it is directly evident from the paper's limited set of baselines. Finally, the paper lacks a detailed discussion of the limitations of the proposed ReasonMaxxer method. The paper does not address the potential for overfitting when applying contrastive fine-tuning at high-entropy decision points, nor does it discuss the sensitivity of the method to different hyperparameter choices. The paper also does not address the potential for the method to fail on certain types of reasoning tasks. This lack of a detailed discussion of limitations makes it difficult to fully understand the method's capabilities and limitations and to guide future research in this area. My confidence in this weakness is high, as it is directly evident from the paper's lack of a dedicated section or detailed discussion on the limitations of ReasonMaxxer.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should develop a more robust theoretical framework to explain why RL appears to act primarily as a selective policy. This could involve a more detailed analysis of the reward structure and its influence on the model's learning process. For example, the authors could explore how the reward signal guides the model's attention to specific tokens, effectively pruning the search space and focusing learning on a limited set of high-entropy decision points. A comparative analysis of different RL algorithms, such as PPO and TRPO, could also shed light on whether the observed behavior is specific to certain RL methods or a more general phenomenon. Furthermore, the authors should investigate the impact of different reward shaping techniques on the model's learning process and the location of high-entropy decision points. This would help to determine whether the selective nature of RL is an inherent property of the algorithm or a consequence of specific reward designs. Second, to address the limitations of the token-level analysis, the authors should expand their study to include a wider range of models and reasoning tasks. This could involve testing the hypothesis on models with different architectures, such as encoder-decoder models or models with different attention mechanisms. The authors should also explore the impact of different reasoning tasks, such as those requiring more complex logical inference or creative problem-solving, to determine the robustness of their findings. For example, the analysis could be extended to tasks that involve multi-hop reasoning or tasks that require the model to generate novel solutions. This would help to determine whether the identified high-entropy decision points are consistent across different problem domains and model architectures. Additionally, the authors should investigate the relationship between the model's pre-existing knowledge and its susceptibility to RL corrections. This could involve analyzing how the model's internal representations change after RL training and how these changes affect the location of high-entropy decision points. Third, the authors should provide a more detailed description of the oracle intervention experiment, including the specific criteria used to determine the correctness of the model's reasoning at each step. This should include a clear definition of what constitutes a correct reasoning path and how this is evaluated. For example, if the model is generating a chain of reasoning, the authors should specify whether the chain is logically sound and leads to the correct answer. The authors should also provide a more detailed description of the entropy-based decision point selection process, including the specific parameters used and the rationale behind their selection. This should include a discussion of how the entropy is calculated, what threshold is used to select decision points, and how this threshold is determined. The authors should also provide a more detailed description of the training process for ReasonMaxxer, including the specific hyperparameters used and the rationale behind their selection. This should include a discussion of how the hyperparameters are chosen, what their values are, and how they affect the performance of the method. The authors should also provide a more detailed description of the evaluation metrics used, including the specific criteria used to assess the model's reasoning performance. This should include a discussion of how the metrics are calculated and what they measure. The authors should also provide a more detailed description of the experimental setup, including the specific hardware and software used. This should include a discussion of the hardware specifications, the software versions, and any other relevant details that could affect the reproducibility of the results. Finally, the authors should include a more comprehensive comparison with existing RL-free methods for reasoning enhancement. This could include methods that focus on prompt engineering, retrieval-augmented generation, or other techniques that aim to improve reasoning without relying on RL. For example, the authors could compare ReasonMaxxer to methods that use chain-of-thought prompting or other forms of in-context learning. This would help to contextualize the performance of ReasonMaxxer and highlight its unique advantages and limitations. Furthermore, the authors should investigate the sensitivity of ReasonMaxxer to different hyperparameter settings and compare its performance to other fine-tuning methods. This would help to determine whether ReasonMaxxer is a robust and reliable method for improving reasoning in LLMs. A more comprehensive comparison would provide a more complete picture of the effectiveness of ReasonMaxxer and its potential for practical applications. Finally, the authors should include a dedicated section discussing the limitations of the proposed method, including the potential for overfitting, the sensitivity to hyperparameter choices, and the potential for the method to fail on certain types of reasoning tasks. This would help to provide a more balanced and nuanced view of the method's capabilities and limitations, and would guide future research in this area.


## Questions:

Based on my analysis, I have several questions that I believe are crucial for a deeper understanding of the paper's findings and methodology. First, how does the proposed ReasonMaxxer method compare to other non-RL-based reasoning enhancement techniques? Are there specific advantages or limitations that make it uniquely suited for certain types of reasoning tasks? This question is important because it would help to contextualize the performance of ReasonMaxxer and highlight its unique contributions compared to other methods that do not rely on RL. Second, can the authors elaborate on the theoretical basis for why RL appears to act primarily as a selective policy rather than a tool for developing new reasoning pathways? Is this behavior consistent across different RL algorithms or reward structures? This question is important because it would help to clarify the underlying mechanisms that drive the observed behavior and would provide a more robust theoretical foundation for the paper's claims. Third, how does the location and nature of high-entropy decision points vary across different model sizes and architectures? Are these points stable across various reasoning tasks, or do they differ significantly depending on the specific problem domain? This question is important because it would help to determine the generalizability of the findings and would provide a more nuanced understanding of the factors that influence the effectiveness of RL in improving reasoning in LLMs. Fourth, what is the sensitivity of ReasonMaxxer to different hyperparameter settings, and how does this performance compare to other fine-tuning methods? This question is important because it would help to determine whether ReasonMaxxer is a robust and reliable method for improving reasoning in LLMs. Fifth, how does the proposed method handle potential biases or assumptions that may affect the results? This question is important because it would help to ensure that the findings are not biased and that the method is applicable to a wider range of scenarios. Finally, what are the limitations of the proposed method in terms of its applicability to different types of reasoning tasks and its sensitivity to different model architectures? This question is important because it would help to determine the scope of the method's applicability and would guide future research in this area. These questions are crucial for a comprehensive understanding of the paper's findings and for guiding future research in this area.


## Rating:

7.0


## Confidence:

3.25


## Decision:

Accept
}