I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper studies the grokking phenomenon on reasoning tasks. The authors find that the grokking phenomenon appears when the ratio between the inferred facts and atomic facts is large, and training data size does not affect the speed of grokking. The authors also find that the generalizing circuit gradually emerges during grokking, and the circuit is more pronounced in the upper layers. The authors further find that the model performs worse in OOD settings for composition but achieves systematicity for comparison.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The authors conduct a detailed analysis of the grokking phenomenon on reasoning tasks, including the ratio between the inferred facts and atomic facts, the generalizing circuit, and the search space. The authors find that the grokking phenomenon appears when the ratio between the inferred facts and atomic facts is large, and training data size does not affect the speed of grokking. The authors also find that the model performs worse in OOD settings for composition but achieves systematicity for comparison. These findings are novel and insightful.
2. The authors provide detailed analysis of the model’s internal mechanisms, including the logit lens and causal tracing. The authors find that the model gradually forms the generalizing circuit during grokking, and the circuit is more pronounced in the upper layers. These findings are interesting and may inspire future research.

### Weaknesses

#### Some Related Works


#### comment

1. The authors do not provide a detailed analysis of the generalizing circuit. The authors only provide a high-level description of the generalizing circuit in the main text and Appendix D. It is unclear how the generalizing circuit is formed and how it contributes to the model's reasoning ability. A more detailed analysis, including the specific mechanisms and interactions within the circuit, is needed to fully understand its role.
2. The authors do not provide a detailed analysis of the search space. The authors only provide a high-level description of the search space in Appendix F. It is unclear how the search space is defined, how it affects the model's performance, and how it relates to the generalizing circuit. A more detailed analysis, including the size, complexity, and structure of the search space, is needed to fully understand its impact on the model's reasoning ability.

### Suggestions

The authors should provide a more detailed analysis of the generalizing circuit, including a step-by-step breakdown of how the circuit is formed and how it contributes to the model's reasoning ability. This analysis should include specific examples of how the circuit operates on different types of reasoning tasks, and how it differs from the circuit in non-grokking models. The authors should also investigate the role of different components within the circuit, such as the attention heads and feedforward layers, in the reasoning process. Furthermore, it would be beneficial to explore how the circuit's structure changes during the grokking process, and how this change contributes to the model's improved generalization ability. This could involve visualizing the circuit's activity during training and inference, and analyzing the activation patterns of different neurons and layers.

Similarly, the authors should provide a more detailed analysis of the search space, including a clear definition of how the search space is defined, how it affects the model's performance, and how it relates to the generalizing circuit. This analysis should include a quantitative assessment of the search space's size, complexity, and structure, and how these factors influence the model's ability to find the correct solution. The authors should also investigate how the search space changes during the grokking process, and how this change contributes to the model's improved generalization ability. This could involve analyzing the model's behavior in different regions of the search space, and identifying the specific features or patterns that the model uses to solve the reasoning tasks. It would also be helpful to compare the search space of the grokking model with that of non-grokking models, to identify the key differences that contribute to the grokking phenomenon.

Finally, the authors should consider exploring the relationship between the generalizing circuit and the search space. It is possible that the generalizing circuit is responsible for guiding the model's search through the search space, and that the structure of the circuit influences the model's ability to find the correct solution. The authors should investigate this relationship by analyzing how the circuit's activity affects the model's exploration of the search space, and how the search space's structure affects the circuit's ability to generalize. This could involve manipulating the circuit's structure or the search space's properties, and observing the resulting changes in the model's performance. A deeper understanding of this relationship could lead to new insights into the mechanisms underlying the grokking phenomenon and the development of more effective reasoning models.

### Questions

1. The authors should provide a detailed analysis of the generalizing circuit, including how the generalizing circuit is formed and how it contributes to the model's reasoning ability. 
2. The authors should provide a detailed analysis of the search space, including how the search space is defined, how it affects the model's performance, and how it relates to the generalizing circuit.

### Rating

6

### Confidence

3

**********

## Reviewer 2

### Summary

This paper investigates the grokking phenomenon in transformers, where models develop implicit reasoning abilities after extended training despite failing to generalize initially. The authors conduct controlled experiments to explore how transformers acquire implicit reasoning, focusing on two tasks: composition and comparison. They find that composition exhibits limited systematicity, while comparison demonstrates robust generalization. The study also reveals that the model's internal mechanisms, specifically the generalizing circuit, play a crucial role in grokking and systematicity. Additionally, the authors propose that enhancing parametric memory could improve the model's generalization capabilities.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper presents a thorough investigation into the grokking phenomenon, providing valuable insights into the internal mechanisms of transformers and their ability to develop implicit reasoning.
2. The controlled experiments are well-designed and effectively demonstrate the different behaviors of transformers in composition and comparison tasks.
3. The paper is well-written and clearly explains the methodology and findings.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on controlled experiments with synthetic data, which may not fully capture the complexities of real-world reasoning tasks. The reliance on synthetic data limits the generalizability of the findings to more complex, nuanced reasoning scenarios encountered in natural language processing. The specific properties of the synthetic data, such as the distribution of facts and the structure of the knowledge graph, might not be representative of the variability found in real-world data, potentially leading to an overestimation of the model's reasoning capabilities.
2. The paper does not explore the potential impact of different model architectures or training strategies on the grokking phenomenon. It is unclear whether the observed grokking behavior is specific to the chosen transformer architecture or if it is a more general phenomenon that can be observed across different model types. The lack of investigation into alternative architectures, such as recurrent neural networks or graph neural networks, leaves open the question of whether the observed grokking is a unique characteristic of transformers or a more general property of neural networks. Furthermore, the paper does not investigate the impact of different training strategies, such as curriculum learning or data augmentation, on the grokking phenomenon.
3. The paper does not provide a comprehensive analysis of the computational resources required for grokking. It would be beneficial to understand the scalability of the grokking phenomenon with respect to model size, training data, and computational resources. The paper lacks a detailed analysis of the computational cost associated with the extended training periods required for grokking to manifest. This includes the number of training steps, the memory requirements for storing model parameters and intermediate activations, and the energy consumption of the training process. Without this information, it is difficult to assess the practical feasibility of achieving grokking in resource-constrained environments.

### Suggestions

To enhance the paper, the authors should consider expanding their experimental setup to include more realistic datasets and tasks. This could involve using datasets with more complex and varied structures, such as those found in natural language processing or knowledge graph reasoning. For example, the authors could explore the use of datasets that involve more complex relationships between entities or tasks that require multi-step reasoning. Additionally, the authors should investigate the impact of different model architectures and training strategies on the grokking phenomenon. This could involve comparing the grokking behavior of transformers with other neural network architectures, such as recurrent neural networks or graph neural networks. Furthermore, the authors should explore the impact of different training strategies, such as curriculum learning or data augmentation, on the grokking phenomenon. This would provide a more comprehensive understanding of the factors that contribute to the emergence of implicit reasoning in transformers. 

Furthermore, the authors should provide a more detailed analysis of the computational resources required for grokking. This should include a breakdown of the number of training steps, the memory requirements for storing model parameters and intermediate activations, and the energy consumption of the training process. This analysis would help to assess the practical feasibility of achieving grokking in resource-constrained environments. The authors could also investigate the relationship between the computational resources required for grokking and the size of the model and the complexity of the task. This would provide valuable insights into the scalability of the grokking phenomenon. For example, the authors could explore whether larger models or more complex tasks require more computational resources to achieve grokking. 

Finally, the authors should consider exploring the limitations of the current approach and discuss potential avenues for future research. This could include investigating the robustness of the grokking phenomenon to adversarial attacks or exploring the use of grokking for other types of reasoning tasks. The authors should also discuss the ethical implications of their findings and the potential for misuse of these techniques. By addressing these limitations and suggesting future research directions, the authors can further strengthen the impact of their work and contribute to the advancement of the field.

### Questions

1. How does the grokking phenomenon scale with model size and training data? Are there specific thresholds beyond which grokking becomes more prominent?
2. What are the computational resources required to achieve grokking? Is it feasible to replicate these findings in resource-constrained environments?
3. How robust is the grokking phenomenon to adversarial attacks or noisy data?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

The paper studies the grokking phenomenon in transformers. The authors study two tasks: composition and comparison. The authors find that transformers can learn implicit reasoning, but this skill is only robustly acquired through extended training far beyond the point of overfitting, a phenomenon called grokking. The authors also find that the model's internal mechanisms, specifically the generalizing circuit, play a crucial role in grokking and systematicity. They also show that a fully grokked transformer can achieve near-perfect accuracy, while a vanilla transformer cannot. The authors also show that the model acquires the same generalizing circuit as in Figure 5 (a), and remarkably, even though not explicitly encouraged/trained to do this, the model successfully infers most of the OOD entities’ attribute values by integrating the observed training facts (Appendix F). The authors also propose that enhancing parametric memory could improve the model's generalization capabilities.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow.
- The paper provides a detailed analysis of the grokking phenomenon in transformers, including the ratio between the inferred facts and atomic facts, the generalizing circuit, and the search space.
- The paper finds that the grokking phenomenon appears when the ratio between the inferred facts and atomic facts is large, and training data size does not affect the speed of grokking.
- The paper finds that the model performs worse in OOD settings for composition but achieves systematicity for comparison.
- The paper provides a mechanistic analysis of the internal mechanisms of the model, including the logit lens and causal tracing.
- The paper finds that the model gradually forms the generalizing circuit during grokking, and the circuit is more pronounced in the upper layers.
- The paper shows that a fully grokked transformer can achieve near-perfect accuracy, while a vanilla transformer cannot.
- The paper proposes that enhancing parametric memory could improve the model's generalization capabilities.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the generalizing circuit. The authors only provide a high-level description of the generalizing circuit in the main text and Appendix D. It is unclear how the generalizing circuit is formed and how it contributes to the model's reasoning ability. A more detailed analysis, including the specific mechanisms and interactions within the circuit, is needed to fully understand its role.
- The paper does not provide a detailed analysis of the search space. The authors only provide a high-level description of the search space in Appendix F. It is unclear how the search space is defined, how it affects the model's performance, and how it relates to the generalizing circuit. A more detailed analysis, including the size, complexity, and structure of the search space, is needed to fully understand its impact on the model's reasoning ability.

### Suggestions

The paper would benefit from a more in-depth exploration of the generalizing circuit. The current description, while providing a high-level overview, lacks the necessary detail to fully grasp its inner workings. Specifically, the authors should elaborate on the precise mechanisms by which information flows through the circuit, including the specific types of connections (e.g., attention heads, feedforward layers) and the transformations applied at each stage. For instance, what specific attention heads are involved in the circuit, and how do they interact to facilitate the transition from atomic facts to higher-level inferences? Furthermore, a detailed analysis of the circuit's activation patterns during both training and inference would be valuable. This could involve visualizing the activation of different neurons or layers within the circuit as the model processes different types of input, providing insights into how the circuit adapts to various reasoning tasks. Such an analysis would move beyond a high-level description and provide a more concrete understanding of the circuit's role in grokking.

Similarly, the analysis of the search space needs significant expansion. The current description is too abstract and lacks the necessary detail to understand its impact on the model's performance. The authors should provide a more precise definition of the search space, including the specific parameters and constraints that define it. For example, what is the dimensionality of the search space, and how does it relate to the model's architecture? Furthermore, the authors should investigate how the search space's properties, such as its size and complexity, affect the model's ability to find the correct solution. This could involve analyzing the model's performance across different search space configurations, such as varying the number of training examples or the complexity of the reasoning tasks. A more detailed analysis of the search space would provide a deeper understanding of why grokking occurs and how it relates to the model's generalization capabilities. It would also be beneficial to explore how the search space changes during the grokking process, and how this change contributes to the model's improved generalization ability.

Finally, the paper should explore the relationship between the generalizing circuit and the search space in more detail. It is unclear how these two concepts interact to enable the model's reasoning ability. The authors should investigate whether the generalizing circuit influences the model's exploration of the search space, and whether the structure of the search space affects the formation of the generalizing circuit. For example, does a more complex search space encourage the formation of a more robust generalizing circuit? Or does a simpler search space lead to a more efficient exploration of the search space, which in turn facilitates the formation of the generalizing circuit? A deeper understanding of this relationship could provide valuable insights into the mechanisms underlying grokking and could potentially lead to new strategies for improving the model's generalization capabilities.

### Questions

- How does the grokking phenomenon scale with model size and training data? Are there specific thresholds beyond which grokking becomes more prominent?
- What are the computational resources required to achieve grokking? Is it feasible to replicate these findings in resource-constrained environments?
- How robust is the grokking phenomenon to adversarial attacks or noisy data?

### Rating

8

### Confidence

3

**********

## Reviewer 4

### Summary

This paper studies the grokking phenomenon in transformers, where models acquire implicit reasoning abilities only after extended training. The authors focus on two tasks: composition and comparison, and find that while composition exhibits limited systematicity, comparison demonstrates strong generalization. They analyze the model's internal mechanisms, identifying a generalizing circuit that emerges during grokking, and propose enhancing parametric memory to improve generalization.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper provides a detailed analysis of the grokking phenomenon, focusing on the role of the generalizing circuit and the impact of parametric memory on generalization.
- The authors use controlled experiments and detailed analyses, such as logit lens and causal tracing, to understand the model's internal mechanisms.
- The paper offers valuable insights into the mechanisms of grokking and the importance of generalizing circuits for systematic reasoning.

### Weaknesses

#### Some Related Works


#### comment

 - The paper primarily focuses on controlled experiments with synthetic data, which may not fully capture the complexities of real-world reasoning tasks. The reliance on synthetic data limits the generalizability of the findings to more complex, nuanced reasoning scenarios encountered in natural language processing. The specific properties of the synthetic data, such as the distribution of facts and the structure of the knowledge graph, might not be representative of the variability found in real-world data, potentially leading to an overestimation of the model's reasoning capabilities.
- The paper does not explore the potential impact of different model architectures or training strategies on the grokking phenomenon. It is unclear whether the observed grokking behavior is specific to the chosen transformer architecture or if it is a more general phenomenon that can be observed across different model types. The lack of investigation into alternative architectures, such as recurrent neural networks or graph neural networks, leaves open the question of whether the observed grokking is a unique characteristic of transformers or a more general property of neural networks. Furthermore, the paper does not investigate the impact of different training strategies, such as curriculum learning or data augmentation, on the grokking phenomenon.
- The paper does not provide a comprehensive analysis of the computational resources required for grokking. It would be beneficial to understand the scalability of the grokking phenomenon with respect to model size, training data, and computational resources. The paper lacks a detailed analysis of the computational cost associated with the extended training periods required for grokking to manifest. This includes the number of training steps, the memory requirements for storing model parameters and intermediate activations, and the energy consumption of the training process. Without this information, it is difficult to assess the practical feasibility of achieving grokking in resource-constrained environments.

### Suggestions

To enhance the paper, the authors should consider expanding their experimental setup to include more realistic datasets and tasks. This could involve using datasets with more complex and varied structures, such as those found in natural language processing or knowledge graph reasoning. For example, the authors could explore the use of datasets that involve more complex relationships between entities or tasks that require multi-step reasoning. Additionally, the authors should investigate the impact of different model architectures and training strategies on the grokking phenomenon. This could involve comparing the grokking behavior of transformers with other neural network architectures, such as recurrent neural networks or graph neural networks. Furthermore, the authors should explore the impact of different training strategies, such as curriculum learning or data augmentation, on the grokking phenomenon. This would provide a more comprehensive understanding of the factors that contribute to the emergence of implicit reasoning in transformers. 

Furthermore, the authors should provide a more detailed analysis of the computational resources required for grokking. This should include a breakdown of the number of training steps, the memory requirements for storing model parameters and intermediate activations, and the energy consumption of the training process. This analysis would help to assess the practical feasibility of achieving grokking in resource-constrained environments. The authors could also investigate the relationship between the computational resources required for grokking and the size of the model and the complexity of the task. This would provide valuable insights into the scalability of the grokking phenomenon. For example, the authors could explore whether larger models or more complex tasks require more computational resources to achieve grokking. 

Finally, the authors should consider exploring the limitations of the current approach and discuss potential avenues for future research. This could include investigating the robustness of the grokking phenomenon to adversarial attacks or exploring the use of grokking for other types of reasoning tasks. The authors should also discuss the ethical implications of their findings and the potential for misuse of these techniques. By addressing these limitations and suggesting future research directions, the authors can further strengthen the impact of their work and contribute to the advancement of the field.

### Questions

- How does the grokking phenomenon scale with model size and training data? Are there specific thresholds beyond which grokking becomes more prominent?
- What are the computational resources required to achieve grokking? Is it feasible to replicate these findings in resource-constrained environments?
- How robust is the grokking phenomenon to adversarial attacks or noisy data?

### Rating

8

### Confidence

4

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers for the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support or refute their claims.

**Plan:**
1. Go through each reviewer's comments one by one.
2. For each weakness identified by the reviewer, find the relevant section in the paper.
3. Extract evidence (quotes, experimental details, missing citations) from the paper to support the weakness.
4. If the weakness is about missing information, check if that information is indeed absent.
5. If there are conflicting opinions between reviewers, highlight them.
6. Finally, conclude whether the weakness is valid, partially valid, or invalid based on the evidence.
**Review 1 Weaknesses:**

1. Weakness Statement:
"The paper primarily focuses on controlled experiments with synthetic data, which may not fully capture the complexities of real-world reasoning tasks. The reliance on synthetic data limits the generalizability of the findings to more complex, nuanced reasoning scenarios encountered in natural language processing. The specific properties of the synthetic data, such as the distribution of facts and the structure of the knowledge graph, might not be representative of the variability found in real-world data, potentially leading to an overestimation of the model's reasoning capabilities."

2. Evidence Collection:
b) Experiment-related Evidence:
   - "We create a data-generating process consisting of 1) sampling a set of basic atomic facts , and 2) using the atomic facts and latent rules to deduce inferred facts ." (Section 3)
   - "For atomic facts, we generate a random knowledge graph 𝒢 consisting of | ℰ | = 2000 relations, where each entity (as the subject) has 20  random distinct relations that each connects to another random entity (as the object)." (Section 3.1)
   - "For composition, we assume there are | ℰ | = 1000 entities, | 𝒜 | = 20 atomic ID {} elements, and 20 atomic relations, where each attribute 𝑎 ∈ 𝒜 has 20  random distinct relations that each leads to a different target prediction (e.g., r 1 , r 2 , t )" (Section 3.1)
   - "For each atomic fact, we assign a unique token to each relation/entity by default, and also find that the results are robust to different tokenizations (details in Appendix C)." (Section 3.1)

3. Literature Gap Analysis:
   - The paper does not explicitly discuss the limitations of using synthetic data or compare it to real-world data in the context of grokking.

4. Validation Analysis:
   - The paper clearly describes the creation of synthetic data using a defined data-generating process and knowledge graphs. The reviewer correctly points out that this approach might not fully capture the complexities of real-world reasoning tasks. The paper acknowledges the use of synthetic data but doesn't delve into the potential limitations or generalizability concerns.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Description of synthetic data generation process and knowledge graph structure in Section 3.

1. Weakness Statement:
"The paper does not explore the potential impact of different model architectures or training strategies on the grokking phenomenon. It is unclear whether the observed grokking behavior is specific to the chosen transformer architecture or if it is a more general phenomenon that can be observed across different model types. The lack of investigation into alternative architectures, such as recurrent neural networks or graph neural networks, leaves open the question of whether the observed grokking is a unique characteristic of transformers or a more general property of neural networks. Furthermore, the paper does not investigate the impact of different training strategies, such as curriculum learning or data augmentation, on the grokking phenomenon."

2. Evidence Collection:
b) Experiment-related Evidence:
   - "We use a standard decoder-only transformer model as in GPT-2 [50] with 8 8 layers, 768 768 hidden dimensions and 12 12 attention heads (we explore the impact of different model scales in Appendix B )." (Section 3)
   - The paper focuses on a specific transformer architecture and does not mention experiments with other architectures like RNNs or GNNs.
   - The training setup is described in Section 3.2, focusing on AdamW optimizer and learning rate schedule, without exploring variations like curriculum learning or data augmentation.

3. Literature Gap Analysis:
   - While the paper cites GPT-2, it doesn't discuss the broader literature on grokking across different architectures or training strategies.

4. Validation Analysis:
   - The paper explicitly states the use of a standard decoder-only transformer model. There is no mention of experiments with other architectures or training strategies. The reviewer's point about the lack of investigation into these factors is valid.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Description of the model architecture in Section 3 and the lack of mention of other architectures or training strategies.

1. Weakness Statement:
"The paper does not provide a comprehensive analysis of the computational resources required for grokking. It would be beneficial to understand the scalability of the grokking phenomenon with respect to model size, training data, and computational resources. The paper lacks a detailed analysis of the computational cost associated with the extended training periods required for grokking to manifest. This includes the number of training steps, the memory requirements for storing model parameters and intermediate activations, and the energy consumption of the training process. Without this information, it is difficult to assess the practical feasibility of achieving grokking in resource-constrained environments."

2. Evidence Collection:
b) Experiment-related Evidence:
   - "Notably, models are trained for a large number of epochs/steps beyond the point where training performance saturates. More details are in Appendix A ." (Section 3.2)
   - Appendix A mentions "Training was performed for 300,000 steps."
   - The paper does not provide details on memory requirements or energy consumption.

3. Literature Gap Analysis:
   - The paper does not cite works that specifically analyze the computational cost of grokking.

4. Validation Analysis:
   - While the paper mentions the number of training steps in the appendix, it lacks a comprehensive analysis of computational resources, memory requirements, and energy consumption. The reviewer's point about the missing details on scalability and practical feasibility is valid.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: Mention of training steps in Appendix A and the absence of detailed computational resource analysis in the main text.

**Review 2 Weaknesses:**

1. Weakness Statement:
"The authors do not provide a detailed analysis of the generalizing circuit. The authors only provide a high-level description of the generalizing circuit in the main text and Appendix D. It is unclear how the generalizing circuit is formed and how it contributes to the model's reasoning ability. A more detailed analysis, including the specific mechanisms and interactions within the circuit, is needed to fully understand its role."

2. Evidence Collection:
a) Method-related Evidence:
   - "We run a set of causal tracing and logit lens experiments across different model checkpoints throughout training. The discovered generalizing circuit (i.e., the causal computational pathways after grokking) is illustrated in Figure 4 (a)." (Section 3.3)
   - "Specifically, we locate a highly interpretable causal graph consisting of states in layer 0 0 , 5 5 , and 8 8 , where we have pruned away the weak nodes/connections (details in Appendix D )." (Section 3.3)
   - Appendix D provides a high-level description of the generalizing circuit and its components.

3. Literature Gap Analysis:
   - The paper cites relevant works on mechanistic interpretability, but the depth of analysis of the generalizing circuit could be debated.

4. Validation Analysis:
   - The paper describes the generalizing circuit and provides a visual representation in Figure 4. However, the reviewer's point about the lack of a *detailed* analysis of *how* it's formed and its specific mechanisms is valid. The description in Appendix D is high-level.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Description of the generalizing circuit in Section 3.3 and the high-level nature of the description in Appendix D.

1. Weakness Statement:
"The authors do not provide a detailed analysis of the search space. The authors only provide a high-level description of the search space in Appendix F. It is unclear how the search space is defined, how it affects the model's performance, and how it relates to the generalizing circuit. A more detailed analysis, including the size, complexity, and structure of the search space, is needed to fully understand its impact on the model's reasoning ability."

2. Evidence Collection:
a) Method-related Evidence:
   - "We test the models on queries consisting of derivable (from all training facts) comparisons between OOD entities where any possible proof would involve rules from both Eqs.( 2 ) and Eqs.( 3 )." (Section 3.1)
   - Appendix F provides a high-level description of the search space related to the comparison task.

3. Literature Gap Analysis:
   - The paper doesn't cite specific works on analyzing the search space in the context of grokking.

4. Validation Analysis:
   - The paper describes the search space in Appendix F, focusing on the comparison task. The reviewer's point about the lack of a detailed analysis of the search space's properties (size, complexity, structure) and its relationship to the generalizing circuit is valid.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Description of the search space in Appendix F and the absence of a detailed analysis of its properties and relationship to the generalizing circuit in the main text.

**Review 3 Weaknesses:**

1. Weakness Statement:
"The paper does not provide a detailed analysis of the generalizing circuit. The authors only provide a high-level description of the generalizing circuit in the main text and Appendix D. It is unclear how the generalizing circuit is formed and how it contributes to the model's reasoning ability. A more detailed analysis, including the specific mechanisms and interactions within the circuit, is needed to fully understand its role."

2. Evidence Collection:
a) Method-related Evidence:
   - "We run a set of causal tracing and logit lens experiments across different model checkpoints throughout training. The discovered generalizing circuit (i.e., the causal computational pathways after grokking) is illustrated in Figure 4 (a)." (Section 3.3)
   - "Specifically, we locate a highly interpretable causal graph consisting of states in layer 0 0 , 5 5 , and 8 8 , where we have pruned away the weak nodes/connections (details in Appendix D )." (Section 3.3)
   - Appendix D provides a high-level description of the generalizing circuit and its components.

3. Literature Gap Analysis:
   - The paper cites relevant works on mechanistic interpretability, but the depth of analysis of the generalizing circuit could be debated.

4. Validation Analysis:
   - The paper describes the generalizing circuit and provides a visual representation in Figure 4. However, the reviewer's point about the lack of a *detailed* analysis of *how* it's formed and its specific mechanisms is valid. The description in Appendix D is high-level.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Description of the generalizing circuit in Section 3.3 and the high-level nature of the description in Appendix D.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the search space. The authors only provide a high-level description of the search space in Appendix F. It is unclear how the search space is defined, how it affects the model's performance, and how it relates to the generalizing circuit. A more detailed analysis, including the size, complexity, and structure of the search space, is needed to fully understand its impact on the model's reasoning ability."

2. Evidence Collection:
a) Method-related Evidence:
   - "We test the models on queries consisting of derivable (from all training facts) comparisons between OOD entities where any possible proof would involve rules from both Eqs.( 2 ) and Eqs.( 3 )." (Section 3.1)
   - Appendix F provides a high-level description of the search space related to the comparison task.

3. Literature Gap Analysis:
   - The paper doesn't cite specific works on analyzing the search space in the context of grokking.

4. Validation Analysis:
   - The paper describes the search space in Appendix F, focusing on the comparison task. The reviewer's point about the lack of a detailed analysis of the search space's properties (size, complexity, structure) and its relationship to the generalizing circuit is valid.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Description of the search space in Appendix F and the absence of a detailed analysis of its properties and relationship to the generalizing circuit in the main text.

**Review 4 Weaknesses:**

1. Weakness Statement:
"The paper primarily focuses on controlled experiments with synthetic data, which may not fully capture the complexities of real-world reasoning tasks. The reliance on synthetic data limits the generalizability of the findings to more complex, nuanced reasoning scenarios encountered in natural language processing. The specific properties of the synthetic data, such as the distribution of facts and the structure of the knowledge graph, might not be representative of the variability found in real-world data, potentially leading to an overestimation of the model's reasoning capabilities."

2. Evidence Collection:
b) Experiment-related Evidence:
   - "We create a data-generating process consisting of 1) sampling a set of basic atomic facts , and 2) using the atomic facts and latent rules to deduce inferred facts ." (Section 3)
   - "For atomic facts, we generate a random knowledge graph 𝒢 consisting of | ℰ | = 2000 relations, where each entity (as the subject) has 20  random distinct relations that each connects to another random entity (as the object)." (Section 3.1)
   - "For composition, we assume there are | ℰ | = 1000 entities, | 𝒜 | = 20 atomic ID {} elements, and 20 atomic relations, where each attribute 𝑎 ∈ 𝒜 has 20  random distinct relations that each leads to a different target prediction (e.g., r 1 , r 2 , t )" (Section 3.1)
   - "For each atomic fact, we assign a unique token to each relation/entity by default, and also find that the results are robust to different tokenizations (details in Appendix C)." (Section 3.1)

3. Literature Gap Analysis:
   - The paper does not explicitly discuss the limitations of using synthetic data or compare it to real-world data in the context of grokking.

4. Validation Analysis:
   - The paper clearly describes the creation of synthetic data using a defined data-generating process and knowledge graphs. The reviewer correctly points out that this approach might not fully capture the complexities of real-world reasoning tasks. The paper acknowledges the use of synthetic data but doesn't delve into the potential limitations or generalizability concerns.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Description of synthetic data generation process and knowledge graph structure in Section 3.

1. Weakness Statement:
"The paper does not explore the potential impact of different model architectures or training strategies on the grokking phenomenon. It is unclear whether the observed grokking behavior is specific to the chosen transformer architecture or if it is a more general phenomenon that can be observed across different model types. The lack of investigation into alternative architectures, such as recurrent neural networks or graph neural networks, leaves open the question of whether the observed grokking is a unique characteristic of transformers or a more general property of neural networks. Furthermore, the paper does not investigate the impact of different training strategies, such as curriculum learning or data augmentation, on the grokking phenomenon."

2. Evidence Collection:
b) Experiment-related Evidence:
   - "We use a standard decoder-only transformer model as in GPT-2 [50] with 8 8 layers, 768 768 hidden dimensions and 12 12 attention heads (we explore the impact of different model scales in Appendix B )." (Section 3)
   - The paper focuses on a specific transformer architecture and does not mention experiments with other architectures like RNNs or GNNs.
   - The training setup is described in Section 3.2, focusing on AdamW optimizer and learning rate schedule, without exploring variations like curriculum learning or data augmentation.

3. Literature Gap Analysis:
   - While the paper cites GPT-2, it doesn't discuss the broader literature on grokking across different architectures or training strategies.

4. Validation Analysis:
   - The paper explicitly states the use of a standard decoder-only transformer model. There is no mention of experiments with other architectures or training strategies. The reviewer's point about the lack of investigation into these factors is valid.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Description of the model architecture in Section 3 and the lack of mention of other architectures or training strategies.

1. Weakness Statement:
"The paper does not provide a comprehensive analysis of the computational resources required for grokking. It would be beneficial to understand the scalability of the grokking phenomenon with respect to model size, training data, and computational resources. The paper lacks a detailed analysis of the computational cost associated with the extended training periods required for grokking to manifest. This includes the number of training steps, the memory requirements for storing model parameters and intermediate activations, and the energy consumption of the training process. Without this information, it is difficult to assess the practical feasibility of achieving grokking in resource-constrained environments."

2. Evidence Collection:
b) Experiment-related Evidence:
   - "Notably, models are trained for a large number of epochs/steps beyond the point where training performance saturates. More details are in Appendix A ." (Section 3.2)
   - Appendix A mentions "Training was performed for 300,000 steps."
   - The paper does not provide details on memory requirements or energy consumption.

3. Literature Gap Analysis:
   - The paper does not cite works that specifically analyze the computational cost of grokking.

4. Validation Analysis:
   - While the paper mentions the number of training steps in the appendix, it lacks a comprehensive analysis of computational resources, memory requirements, and energy consumption. The reviewer's point about the missing details on scalability and practical feasibility is valid.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: Mention of training steps in Appendix A and the absence of detailed computational resource analysis in the main text.

**Synthesis and Reflection:**

All reviewers raise valid concerns about the paper's methodology and the generalizability of its findings. There is a consensus across reviewers regarding the limitations of using synthetic data and the lack of exploration of different model architectures and training strategies. Reviewers 2 and 3 specifically point out the need for a more detailed analysis of the generalizing circuit and the search space, which are currently presented at a high level. Reviewer 4 echoes the concern about synthetic data and the lack of computational resource analysis. There are no significant contradictions between the reviewers' opinions; they largely converge on similar areas for improvement.

**Final Conclusion:**

All identified weaknesses are valid and supported by evidence from the paper. The primary areas for improvement are:

- **Methodological Limitations:** The reliance on synthetic data and the lack of exploration of other model architectures and training strategies.
- **Analytical Depth:** The need for a more detailed analysis of the generalizing circuit and the search space.
- **Practical Considerations:** The absence of a comprehensive analysis of computational resources and scalability.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper presents a compelling investigation into the phenomenon of grokking in transformer models, specifically focusing on their ability to develop implicit reasoning skills. The authors explore this phenomenon through controlled experiments using synthetic datasets designed to simulate two distinct reasoning tasks: composition and comparison. The core contribution of this work lies in its detailed analysis of the factors that influence the emergence of grokking, particularly the role of the model's internal mechanisms. The authors demonstrate that grokking, which manifests as a sudden shift from poor to good generalization after extended training, is not solely dependent on the amount of training data but rather on the ratio between inferred and atomic facts. This finding challenges the conventional understanding of generalization in machine learning. Furthermore, the study reveals that the model acquires systematic reasoning, characterized by robust generalization, primarily during the grokking phase for the composition task, while the comparison task demonstrates systematicity only after achieving out-of-distribution (OOD) generalization. This suggests that the nature of the reasoning task significantly impacts the model's ability to generalize systematically. A key methodological approach employed in this study is the mechanistic analysis of the model's internal processes. The authors identify a generalizing circuit, a specific set of computational pathways within the transformer, that emerges during grokking and is crucial for systematic reasoning. They employ techniques such as logit lens and causal tracing to map the flow of information and the activation patterns of different neurons, providing insights into how the model processes and integrates information to perform the reasoning tasks. The paper also proposes that enhancing parametric memory, which is closely tied to the generalizing circuit, could improve the model's generalization capabilities. This hypothesis is supported by the observation that models with a more developed generalizing circuit exhibit better systematicity in their reasoning. Overall, this paper makes a significant contribution to our understanding of grokking by providing a detailed analysis of the underlying mechanisms and the factors that influence its emergence. The findings have implications for the development of more robust and generalizable AI models and highlight the importance of understanding the internal workings of neural networks to improve their performance.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

2.75


## Strengths:

This paper demonstrates several notable strengths, primarily in its rigorous experimental design and in-depth analysis of the grokking phenomenon. The controlled experiments, conducted using synthetic data, allow for a focused examination of the model's learning dynamics. I found the meticulous approach to manipulating the ratio between inferred and atomic facts to be particularly insightful. This allowed the authors to isolate the critical factor that drives grokking, as they discovered that the model's generalizing ability is not solely dependent on the amount of training data but rather on the ratio of these two types of facts. This finding is a significant contribution to our understanding of how transformers learn and generalize. The paper's detailed analysis of the model's internal mechanisms is another key strength. The authors employ logit lens and causal tracing to map the flow of information within the model and to identify the specific neurons and pathways that are involved in the reasoning process. This mechanistic approach provides a deeper understanding of how the model processes and integrates information to perform the reasoning tasks. The identification of the generalizing circuit, a specific set of computational pathways that emerges during grokking, is a particularly important contribution. The authors provide a clear description of this circuit and demonstrate its crucial role in systematic reasoning. The paper's exploration of the differences in generalization between the composition and comparison tasks is also noteworthy. The finding that the model acquires systematic reasoning for the composition task primarily during the grokking phase, while the comparison task demonstrates systematicity only after achieving OOD generalization, highlights the task-specific nature of the model's learning process. This suggests that the nature of the reasoning task significantly impacts the model's ability to generalize systematically. Furthermore, the paper's hypothesis that enhancing parametric memory, which is closely tied to the generalizing circuit, could improve the model's generalization capabilities is a valuable insight. This hypothesis provides a concrete direction for future research aimed at improving the model's performance. Overall, the paper's strengths lie in its rigorous methodology, in-depth analysis, and its valuable insights into the mechanisms underlying grokking. The findings have implications for the development of more robust and generalizable AI models and highlight the importance of understanding the internal workings of neural networks to improve their performance.


## Weaknesses:

While this paper presents a compelling analysis of the grokking phenomenon, several limitations warrant careful consideration. A primary concern, independently validated by multiple reviewers, is the paper's reliance on synthetic data. The authors generate synthetic datasets using a defined data-generating process and knowledge graphs, which, while allowing for controlled experiments, may not fully capture the complexities of real-world reasoning tasks. As the paper states, "We create a data-generating process consisting of 1) sampling a set of basic atomic facts , and 2) using the atomic facts and latent rules to deduce inferred facts ." (Section 3). This approach, while enabling the study of specific properties of transformers, raises questions about the generalizability of the findings to more complex, nuanced reasoning scenarios encountered in natural language processing. The specific properties of the synthetic data, such as the distribution of facts and the structure of the knowledge graph, might not be representative of the variability found in real-world data, potentially leading to an overestimation of the model's reasoning capabilities. This limitation is further supported by the fact that the paper acknowledges the use of synthetic data but does not delve into the potential limitations or generalizability concerns. Another significant weakness, also independently validated, is the lack of exploration of different model architectures and training strategies. The paper focuses on a specific decoder-only transformer model, as stated in Section 3, "We use a standard decoder-only transformer model as in GPT-2 [50] with 8 8 layers, 768 768 hidden dimensions and 12 12 attention heads (we explore the impact of different model scales in Appendix B )." The absence of experiments with other architectures, such as recurrent neural networks or graph neural networks, leaves open the question of whether the observed grokking behavior is specific to the chosen transformer architecture or a more general phenomenon that can be observed across different model types. Furthermore, the paper does not investigate the impact of different training strategies, such as curriculum learning or data augmentation, on the grokking phenomenon. This lack of investigation into these factors limits the scope of the findings and raises questions about the robustness of the observed grokking phenomenon. The paper also lacks a comprehensive analysis of the computational resources required for grokking. While the authors mention in Section 3.2 that "Notably, models are trained for a large number of epochs/steps beyond the point where training performance saturates. More details are in Appendix A ." Appendix A states that "Training was performed for 300,000 steps." However, the paper does not provide details on memory requirements, energy consumption, or the number of training steps required for grokking to manifest. This lack of information makes it difficult to assess the practical feasibility of achieving grokking in resource-constrained environments. The paper's analysis of the generalizing circuit, while providing a high-level description, lacks the necessary detail to fully understand its inner workings. As stated in Section 3.3, "We run a set of causal tracing and logit lens experiments across different model checkpoints throughout training. The discovered generalizing circuit (i.e., the causal computational pathways after grokking) is illustrated in Figure 4 (a)." and Appendix D, "Specifically, we locate a highly interpretable causal graph consisting of states in layer 0 0 , 5 5 , and 8 8 , where we have pruned away the weak nodes/connections (details in Appendix D ).", the description of the generalizing circuit is high-level and does not delve into the specific mechanisms by which information flows through the circuit, including the specific types of connections (e.g., attention heads, feedforward layers) and the transformations applied at each stage. Similarly, the analysis of the search space, as described in Appendix F, is also high-level and lacks the necessary detail to understand its size, complexity, and structure, and how it affects the model's performance. The paper also does not provide a detailed analysis of the computational resources required for grokking. While the authors mention the number of training steps in Appendix A, they do not provide details on memory requirements, energy consumption, or the number of training steps required for grokking to manifest. This lack of information makes it difficult to assess the practical feasibility of achieving grokking in resource-constrained environments. Finally, the paper's analysis of the search space is also high-level and lacks the necessary detail to understand its size, complexity, and structure, and how it affects the model's performance. The paper describes the search space in Appendix F, focusing on the comparison task, but does not provide a detailed analysis of its properties (size, complexity, structure) and its relationship to the generalizing circuit. These limitations, while not invalidating the paper's findings, highlight areas where further research is needed to fully understand the grokking phenomenon and its implications.


## Suggestions:

To enhance the paper, several concrete improvements can be made. First and foremost, the authors should expand their experimental setup to include more realistic datasets and tasks. This could involve using datasets with more complex and varied structures, such as those found in natural language processing or knowledge graph reasoning. For example, the authors could explore the use of datasets that involve more complex relationships between entities or tasks that require multi-step reasoning. Additionally, the authors should investigate the impact of different model architectures and training strategies on the grokking phenomenon. This could involve comparing the grokking behavior of transformers with other neural network architectures, such as recurrent neural networks or graph neural networks. Furthermore, the authors should explore the impact of different training strategies, such as curriculum learning or data augmentation, on the grokking phenomenon. This would provide a more comprehensive understanding of the factors that contribute to the emergence of implicit reasoning in transformers. The authors should also provide a more detailed analysis of the computational resources required for grokking. This should include a breakdown of the number of training steps, the memory requirements for storing model parameters and intermediate activations, and the energy consumption of the training process. This analysis would help to assess the practical feasibility of achieving grokking in resource-constrained environments. The authors could also investigate the relationship between the computational resources required for grokking and the size of the model and the complexity of the task. For example, the authors could explore whether larger models or more complex tasks require more computational resources to achieve grokking. To enhance the paper, the authors should provide a more in-depth exploration of the generalizing circuit. The current description, while providing a high-level overview, lacks the necessary detail to fully grasp its inner workings. Specifically, the authors should elaborate on the precise mechanisms by which information flows through the circuit, including the specific types of connections (e.g., attention heads, feedforward layers) and the transformations applied at each stage. For instance, what specific attention heads are involved in the circuit, and how do they interact to facilitate the transition from atomic facts to higher-level inferences? Furthermore, a detailed analysis of the circuit's activation patterns during both training and inference would be valuable. This could involve visualizing the activation of different neurons or layers within the circuit as the model processes different types of input, providing insights into how the circuit adapts to various reasoning tasks. Such an analysis would move beyond a high-level description and provide a more concrete understanding of the circuit's role in grokking. Similarly, the analysis of the search space needs significant expansion. The current description is too abstract and lacks the necessary detail to understand its impact on the model's performance. The authors should provide a more precise definition of the search space, including the specific parameters and constraints that define it. For example, what is the dimensionality of the search space, and how does it relate to the model's architecture? Furthermore, the authors should investigate how the search space's properties, such as its size and complexity, affect the model's ability to find the correct solution. This could involve analyzing the model's performance across different search space configurations, such as varying the number of training examples or the complexity of the reasoning tasks. A more detailed analysis of the search space would provide a deeper understanding of why grokking occurs and how it relates to the model's generalization capabilities. It would also be beneficial to explore how the search space changes during the grokking process, and how this change contributes to the model's improved generalization ability. This could involve visualizing the search space's evolution during training and analyzing the model's behavior in different regions of the search space. It would also be helpful to compare the search space of the grokking model with that of non-grokking models, to identify the key differences that contribute to the emergence of implicit reasoning in transformers. Finally, the authors should explore the relationship between the generalizing circuit and the search space in more detail. It is unclear how these two concepts interact to enable the model's reasoning ability. The authors should investigate whether the generalizing circuit influences the model's exploration of the search space, and whether the structure of the search space affects the formation of the generalizing circuit. For example, does a more complex search space encourage the formation of a more robust generalizing circuit? Or does a simpler search space lead to a more efficient exploration of the search space, which in turn facilitates the formation of the generalizing circuit? A deeper understanding of this relationship could provide valuable insights into the mechanisms underlying grokking and could potentially lead to new strategies for improving the model's generalization capabilities.


## Questions:

Several key questions arise from my analysis of this paper. First, how does the grokking phenomenon scale with model size and training data? Are there specific thresholds beyond which grokking becomes more prominent, and are these thresholds consistent across different model architectures? The paper does not explore the relationship between model size and training data and the emergence of grokking, and it would be valuable to understand if there are specific thresholds beyond which grokking becomes more prominent. Second, what are the computational resources required to achieve grokking? Is it feasible to replicate these findings in resource-constrained environments? The paper lacks a detailed analysis of the computational resources required for grokking, and it would be beneficial to understand the practical feasibility of achieving grokking in resource-constrained environments. Third, how robust is the grokking phenomenon to adversarial attacks or noisy data? The paper does not explore the robustness of the grokking phenomenon to adversarial attacks or noisy data, and it would be valuable to understand if the model's ability to generalize after grokking is affected by such perturbations. Fourth, how does the grokking phenomenon relate to other reasoning tasks beyond composition and comparison? The paper focuses on two specific tasks, and it would be interesting to explore whether the same grokking phenomenon occurs in other types of reasoning tasks. Fifth, what are the specific mechanisms by which information flows through the generalizing circuit, and how do these mechanisms contribute to the model's reasoning ability? The paper provides a high-level description of the generalizing circuit, and it would be valuable to understand the specific mechanisms by which information flows through the circuit, including the specific types of connections and the transformations applied at each stage. Sixth, what is the dimensionality of the search space, and how does it relate to the model's architecture? The paper does not provide a precise definition of the search space, and it would be beneficial to understand the properties of the search space, such as its size and complexity, and how it affects the model's ability to find the correct solution. Finally, how does the generalizing circuit influence the model's exploration of the search space, and does the structure of the search space affect the formation of the generalizing circuit? The paper does not explore the relationship between the generalizing circuit and the search space in detail, and it would be valuable to understand how these two concepts interact to enable the model's reasoning ability.


## Rating:

7.0


## Confidence:

3.25


## Decision:

Accept
}