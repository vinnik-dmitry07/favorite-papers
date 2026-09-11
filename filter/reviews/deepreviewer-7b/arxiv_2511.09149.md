I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper proposes a novel framework called Interlat, which enables inter-agent communication entirely in latent space, addressing the limitations of language-based communication in multi-agent systems. Interlat leverages the continuous last hidden states of LLMs as a representation of the agent's thought and implements inter-agent communication through these latent states. The framework includes a supervised objective that explicitly encourages the interpretation and utilization of task-relevant latent information. Additionally, Interlat incorporates a compressed latent message to reduce inference latency and maintain competitive performance through an efficient information-preserving mechanism. The authors demonstrate the effectiveness of Interlat in a two-agent sender-receiver scenario, showing that it outperforms both fine-tuned chain-of-thought (CoT) prompting and single-agent baselines, even across heterogeneous models. The results highlight Interlat’s potential as a feasible paradigm for future research in multi-agent systems.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow, with clear explanations of the proposed framework and its components.
2. The authors conduct a comprehensive set of experiments to evaluate Interlat, including comparisons with various baselines and ablation studies to analyze the impact of different components. The results demonstrate the effectiveness of Interlat in enhancing multi-agent communication and improving task performance.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed discussion of the limitations of Interlat, such as its applicability to different types of tasks or its scalability to larger multi-agent systems. Specifically, the paper does not address how the performance of Interlat might vary with different task complexities, such as tasks requiring long-term dependencies or complex reasoning. Furthermore, the scalability of the approach to systems with more than two agents is not explored, leaving open questions about its practical applicability in more complex scenarios. 
2. The paper does not provide a thorough comparison with existing methods for multi-agent communication, particularly those that also leverage latent representations. While the paper mentions related work, it does not provide a detailed analysis of how Interlat differs from or improves upon these methods. A more comprehensive comparison would help to clarify the unique contributions of Interlat and its potential advantages over existing approaches. 
3. The paper does not discuss the potential ethical implications of using Interlat, such as the risk of misuse or unintended consequences in multi-agent systems. A discussion of these ethical considerations would be important for ensuring the responsible development and deployment of Interlat. 
4. The paper does not provide a detailed analysis of the computational cost of Interlat, including the time and memory requirements for training and inference. This information is crucial for assessing the practical feasibility of the approach and for comparing it with other methods.

### Suggestions

The paper would benefit from a more thorough investigation into the limitations of the proposed Interlat framework. Specifically, the authors should explore how the performance of Interlat varies with different task complexities. For example, it would be valuable to test the framework on tasks that require long-term dependencies, such as those involving planning or sequential decision-making, and compare its performance with tasks that are more localized in time and space. Additionally, the authors should investigate the scalability of Interlat to larger multi-agent systems. This could involve experiments with more than two agents to determine whether the performance gains observed in the current setup hold true in more complex scenarios. Furthermore, the authors should analyze the computational cost of Interlat in detail, including the time and memory requirements for training and inference. This analysis should also consider the impact of different hyperparameter settings on the computational cost and performance of the framework. 

To strengthen the paper, the authors should provide a more detailed comparison of Interlat with existing methods for multi-agent communication, particularly those that also leverage latent representations. This comparison should not only focus on the performance of different methods but also on their underlying mechanisms and assumptions. For example, the authors could compare Interlat with methods that use attention mechanisms to facilitate communication between agents, or with methods that use graph-based representations to model the relationships between agents. This would help to clarify the unique contributions of Interlat and its potential advantages over existing approaches. The authors should also discuss the potential ethical implications of using Interlat, such as the risk of misuse or unintended consequences in multi-agent systems. This discussion should consider the potential for Interlat to be used for harmful purposes, such as manipulating other agents or controlling their behavior. 

Finally, the authors should provide a more detailed analysis of the information preservation mechanism used in Interlat. While the paper mentions that the framework uses a compressed latent message to reduce inference latency and maintain competitive performance, it does not provide a clear explanation of how this mechanism works. The authors should provide a more detailed description of the compression and decompression processes, and they should analyze the impact of different compression techniques on the performance of the framework. This analysis should also consider the trade-off between the compression rate and the performance of the framework. Furthermore, the authors should investigate the robustness of the information preservation mechanism to different types of perturbations, such as noise or adversarial attacks.

### Questions

1. How does Interlat perform on tasks that require long-term dependencies or complex reasoning?
2. How does the performance of Interlat scale with the number of agents in a multi-agent system?
3. What is the computational cost of Interlat, and how does it compare with other methods for multi-agent communication?
4. What are the potential ethical implications of using Interlat, and how can they be mitigated?
5. How does the information preservation mechanism in Interlat work, and what are its limitations?

### Rating

5

### Confidence

3

**********

## Reviewer 2

### Summary

This paper introduces Interlat, a novel framework that enables inter-agent communication entirely in latent space, addressing limitations of language-based communication in multi-agent systems. Unlike traditional methods that rely on natural language, Interlat leverages the continuous last hidden states of large language models (LLMs) as a representation of an agent's thought. The framework includes a supervised objective that encourages the interpretation and utilization of task-relevant latent information, and a compressed latent message to reduce inference latency while maintaining competitive performance. Experiments in a two-agent sender-receiver scenario demonstrate that Interlat outperforms both fine-tuned chain-of-thought (CoT) prompting and single-agent baselines, even across heterogeneous models. The results highlight Interlat’s potential as a feasible paradigm for future research in multi-agent systems.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. This paper proposes a novel approach to multi-agent communication by leveraging the continuous last hidden states of LLMs as a representation of an agent's thought for direct communication, which is a creative and innovative idea.
2. The paper is well-organized and clearly written, making it easy to follow the methodology and results. The figures and tables are well-designed and effectively illustrate the key concepts and findings.
3. The authors provide a thorough experimental evaluation of the proposed method, including comparisons with various baselines and ablation studies. The results demonstrate the effectiveness of the proposed method in improving multi-agent communication performance.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational cost associated with the proposed method. Specifically, the paper does not provide a breakdown of the computational resources required for training and inference, such as the number of parameters, FLOPs, and memory usage. This information is crucial for assessing the practical feasibility of the method, especially when scaling to larger models and more complex multi-agent systems. The absence of this analysis makes it difficult to evaluate the trade-offs between performance gains and computational overhead.
2. The paper does not provide a comprehensive comparison with existing methods for multi-agent communication. While the paper compares the proposed method with some baselines, it does not compare with other state-of-the-art methods in the field, such as those based on graph neural networks or attention mechanisms. A more comprehensive comparison would help to better understand the strengths and weaknesses of the proposed method and its position in the broader landscape of multi-agent communication techniques. The lack of comparison with relevant methods makes it hard to assess the novelty and effectiveness of the proposed approach.

### Suggestions

The paper should include a detailed analysis of the computational cost associated with the proposed Interlat framework. This analysis should include a breakdown of the computational resources required for both training and inference, such as the number of parameters, FLOPs, and memory usage. It would be beneficial to provide a comparison of these metrics with the baseline methods used in the experiments. This would allow readers to better understand the trade-offs between performance gains and computational overhead. Furthermore, the authors should discuss the scalability of the method with respect to model size and the number of agents. This would help to assess the practical applicability of the method in real-world scenarios.

To strengthen the evaluation, the authors should include a more comprehensive comparison with existing methods for multi-agent communication. This should include a comparison with state-of-the-art methods that use different communication mechanisms, such as graph neural networks or attention mechanisms. The comparison should not only focus on performance metrics but also on other aspects such as communication efficiency, robustness, and scalability. The authors should also discuss the limitations of the proposed method and identify potential areas for future research. This would provide a more complete picture of the method's strengths and weaknesses and help to guide future research in this area.

Finally, the authors should provide more details on the implementation of the proposed method. This should include details on the specific model architectures used, the training procedures, and the hyperparameter settings. This would allow other researchers to reproduce the results and build upon the proposed method. The authors should also discuss the sensitivity of the method to different hyperparameter settings and provide guidelines for selecting appropriate values. This would make the method more accessible and easier to use for other researchers.

### Questions

1. How does the proposed method scale with the number of agents in a multi-agent system?
2. What is the impact of different model architectures on the performance of the proposed method?
3. How does the proposed method handle situations where the agents have different levels of expertise or knowledge?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper proposes a novel framework called Interlat that enables inter-agent communication entirely in latent space. The authors address the limitations of natural language-based communication in multi-agent systems, particularly the constraints imposed by downsampling rich, internal latent states into discrete tokens. Interlat leverages the continuous last hidden states of an LLM as a representation of its thought for direct communication, allowing for more expressive and information-preserving interactions. The framework includes a supervised objective that encourages the interpretation and utilization of task-relevant latent information, and a compressed latent message to reduce inference latency while maintaining competitive performance through an efficient information-preserving mechanism. The authors conduct experiments in a two-agent sender-receiver scenario, demonstrating that Interlat outperforms both fine-tuned chain-of-thought (CoT) prompting and single-agent baselines, even across heterogeneous models.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow, with clear explanations of the proposed framework and its components.
- The authors conduct a comprehensive set of experiments to evaluate Interlat, including comparisons with various baselines and ablation studies to analyze the impact of different components.
- The results demonstrate the effectiveness of Interlat in enhancing multi-agent communication and improving task performance.
- The authors provide a detailed analysis of the information preservation mechanism used in Interlat, including a head-coverage statistic and a comparison with other compression techniques.

### Weaknesses

#### Some Related Works


#### comment

 - The paper primarily focuses on a controlled two-agent setting, evaluated on one embodied interactive benchmark (ALFWorld) and one non-interactive symbolic reasoning benchmark (MATH). While these benchmarks provide a good starting point, they do not fully capture the diversity of real-world multi-agent systems, such as settings with larger teams, dynamic role assignments, long-horizon collaboration, or richer environments involving tool use and external memory. The lack of experiments in more complex scenarios limits the generalizability of the findings.
- The approach assumes access to internal model representations, specifically last-layer hidden states, in order to enable latent communication. This assumption may not hold for closed-source or API-only models, where hidden states are inaccessible. As a result, the current formulation of Interlat is primarily applicable to open or inspectable models, and extending latent communication to restricted-access settings is an open challenge.

### Suggestions

The authors should consider expanding their experimental evaluation to include more complex multi-agent scenarios. Specifically, they could explore settings with a larger number of agents, dynamic role assignments, and more intricate communication patterns. For example, they could investigate how Interlat performs in a collaborative task where agents need to coordinate their actions over a longer time horizon, or in a scenario where agents have different levels of expertise and need to communicate effectively despite these differences. Furthermore, they could explore the use of more realistic environments that involve tool use and external memory, which would provide a more comprehensive evaluation of the framework's capabilities. This would help to demonstrate the robustness and generalizability of Interlat in more realistic and challenging settings.

To address the limitation of assuming access to internal model representations, the authors could explore alternative approaches that do not rely on this assumption. For example, they could investigate methods for extracting latent representations from model outputs or using techniques such as adversarial training to learn representations that are robust to changes in the model architecture. Another approach could involve using a shared latent space that is learned jointly by all agents, which would allow them to communicate without requiring access to each other's internal representations. This would make the framework more applicable to a wider range of scenarios, including those where agents are deployed on different platforms or have limited access to each other's internal states. The authors should also discuss the potential limitations of their approach in scenarios where the internal representations are not well-aligned or where there are significant differences in the way that different models process information.

Finally, the authors should provide a more detailed analysis of the computational cost of their approach, particularly in comparison to other multi-agent communication methods. This analysis should include a breakdown of the time and memory requirements for training and inference, as well as a discussion of the scalability of the approach to larger multi-agent systems. It would also be beneficial to compare the computational cost of Interlat with other methods that use different communication mechanisms, such as language-based communication or graph-based communication. This would help to provide a more complete picture of the trade-offs between performance and computational cost, and would allow practitioners to make informed decisions about which approach is most suitable for their specific needs.

### Questions

- How does the performance of Interlat scale with the number of agents in a multi-agent system?
- What is the computational cost of Interlat compared to other multi-agent communication methods?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

This paper proposes a novel framework called Interlat, which enables inter-agent communication entirely in latent space. The authors address the limitations of natural language-based communication in multi-agent systems, particularly the downsampling of rich, internal latent states into discrete tokens. Interlat leverages the continuous last hidden states of an LLM as a representation of its thought for direct communication, allowing for more expressive and information-preserving interactions. The framework includes a supervised objective that encourages the interpretation and utilization of task-relevant latent information, and a compressed latent message to reduce inference latency while maintaining competitive performance through an efficient information-preserving mechanism. The authors conduct experiments in a two-agent sender-receiver scenario, demonstrating that Interlat outperforms both fine-tuned chain-of-thought (CoT) prompting and single-agent baselines, even across heterogeneous models. The results highlight Interlat’s potential as a feasible paradigm for future research in multi-agent systems.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

The paper is well-written and easy to follow, with clear explanations of the proposed framework and its components. The authors conduct a comprehensive set of experiments to evaluate Interlat, including comparisons with various baselines and ablation studies to analyze the impact of different components. The results demonstrate the effectiveness of Interlat in enhancing multi-agent communication and improving task performance. The authors provide a detailed analysis of the information preservation mechanism used in Interlat, including a head-coverage statistic and a comparison with other compression techniques.

### Weaknesses

#### Some Related Works


#### comment

The paper primarily focuses on a controlled two-agent setting, evaluated on one embodied interactive benchmark (ALFWorld) and one non-interactive symbolic reasoning benchmark (MATH). While these benchmarks provide a good starting point, they do not fully capture the diversity of real-world multi-agent systems, such as settings with larger teams, dynamic role assignments, long-horizon collaboration, or richer environments involving tool use and external memory. The lack of experiments in more complex scenarios limits the generalizability of the findings.

The approach assumes access to internal model representations, specifically last-layer hidden states, in order to enable latent communication. This assumption may not hold for closed-source or API-only models, where hidden states are inaccessible. As a result, the current formulation of Interlat is primarily applicable to open or inspectable models, and extending latent communication to restricted-access settings is an open challenge.

### Suggestions

The authors should consider expanding their experimental evaluation to include more complex multi-agent scenarios. Specifically, they could explore settings with a larger number of agents, dynamic role assignments, and more intricate communication patterns. For example, they could investigate how Interlat performs in a collaborative task where agents need to coordinate their actions over a longer time horizon, or in a scenario where agents have different levels of expertise and need to communicate effectively despite these differences. Furthermore, they could explore the use of more realistic environments that involve tool use and external memory, which would provide a more comprehensive evaluation of the framework's capabilities. This would help to demonstrate the robustness and generalizability of Interlat in more realistic and challenging settings.

To address the limitation of assuming access to internal model representations, the authors could explore alternative approaches that do not rely on this assumption. For example, they could investigate methods for extracting latent representations from model outputs or using techniques such as adversarial training to learn representations that are robust to changes in the model architecture. Another approach could involve using a shared latent space that is learned jointly by all agents, which would allow them to communicate without requiring access to each other's internal representations. This would make the framework more applicable to a wider range of scenarios, including those where agents are deployed on different platforms or have limited access to each other's internal states. The authors should also discuss the potential limitations of their approach in scenarios where the internal representations are not well-aligned or where there are significant differences in the way that different models process information.

Finally, the authors should provide a more detailed analysis of the computational cost of their approach, particularly in comparison to other multi-agent communication methods. This analysis should include a breakdown of the time and memory requirements for training and inference, as well as a discussion of the scalability of the approach to larger multi-agent systems. It would also be beneficial to compare the computational cost of Interlat with other methods that use different communication mechanisms, such as language-based communication or graph-based communication. This would help to provide a more complete picture of the trade-offs between performance and computational cost, and would allow practitioners to make informed decisions about which approach is most suitable for their specific needs.

### Questions

How does the performance of Interlat scale with the number of agents in a multi-agent system?

What is the computational cost of Interlat compared to other multi-agent communication methods?

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
2. For each comment identified as a weakness, find supporting evidence from the paper.
3. If the weakness is about the method, look for issues in the description of the algorithm, mathematical formulations, missing citations, etc.
4. If the weakness is about the experiments, look for issues in the dataset description, implementation details, missing baselines, evaluation metrics, etc.
5. If the weakness is about practical limitations, look for mentions of computational cost, scalability, or applicability to closed-source models.
6. If there are conflicting opinions between reviewers, address them in the synthesis.
**Review 1 Weaknesses:**

1. Weakness Statement:
"The paper primarily focuses on a controlled two-agent setting, evaluated on one embodied interactive benchmark (ALFWorld) and one non-interactive symbolic reasoning benchmark (MATH). While these benchmarks provide a good starting point, they do not fully capture the diversity of real-world multi-agent systems, such as settings with larger teams, dynamic role assignments, long-horizon collaboration, or richer environments involving tool use and external memory. The lack of experiments in more complex scenarios limits the generalizability of the findings."

2. Evidence Collection:
b) Experiment-related Evidence:
   - Dataset/setup descriptions: "We evaluate our approach on Alfworld ( Shridhar et al., 2020 ) , and MATH Hendrycks et al. (2021) . For Alfworld, training is conducted using data from Song et al. (2024) . Qwen2LLaMA uses latents from Qwen2.5-7B to train LLaMA3.1-8B-Base Dubey et al. (2024) and LLaMA3.1-8B-Base Dubey et al. (2024) are employed as reasoning models in the information compression experiments." (Section 5)
   - The paper explicitly mentions using Alfworld and MATH, which are single-agent benchmarks. The experiments are conducted in a two-agent sender-receiver scenario.

3. Literature Gap Analysis:
   - While the paper mentions the complexity of multi-agent systems in the motivation, it doesn't include experiments on more complex multi-agent benchmarks.

4. Validation Analysis:
   - The reviewer correctly points out that the experiments are limited to a two-agent setting and specific benchmarks. The paper doesn't explore scenarios with larger teams, dynamic role assignments, or long-horizon collaboration. The environments used are also relatively simple compared to real-world multi-agent systems.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper explicitly states the use of Alfworld and MATH, which are single-agent benchmarks, and focuses on a two-agent scenario.

1. Weakness Statement:
"The approach assumes access to internal model representations, specifically last-layer hidden states, in order to enable latent communication. This assumption may not hold for closed-source or API-only models, where hidden states are inaccessible. As a result, the current formulation of Interlat is primarily applicable to open or inspectable models, and extending latent communication to restricted-access settings is an open challenge."

2. Evidence Collection:
a) Method-related Evidence:
   - "In this work, we propose Interlat, a novel framework that realizes this vision by enabling inter-agent communication entirely in latent space. Rather than transmitting discrete tokens decoded by the language head, Interlat directly transmits the temporally aligned last hidden states, which we termed latent communication." (Section 3)
   - "For each decoding step ℓ = 1 , … , L \ell=1:m L=T \litet{S S ​ = [ s 1 , … , s T } s=( s 1 , … , s L ) , where s un + ℓ = x m + ℓ , h 1 , h 2 , … , h L , e i + 1 = E i + 1 ( h i ) , where e i + 1 ∝ A i + 1 ( h i ) , generated by the trainable light-weight self-attention and a projection layer as a communication adapter for rescaling and interpretation." (Section 3.1)
   - "The latent communications are processed by a trainable light-weight self-attention and a projection layer as a communication adapter for rescaling and interpretation." (Section 3.1)
   - "We use base models as reasoning models in the information compression experiments." (Section 5.1)

3. Literature Gap Analysis:
   - The paper doesn't discuss methods for extracting latent representations from closed-source models.

4. Validation Analysis:
   - The method description clearly states that the framework operates on the last hidden states of the LLMs. The experimental setup confirms the use of open-source models. The reviewer's concern about the applicability to closed-source models is valid as the current implementation relies on direct access to internal states.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The method description explicitly mentions using the last hidden states, and the experiments use open-source models.

**Review 2 Weaknesses:**

1. Weakness Statement:
"The paper lacks a detailed discussion of the limitations of Interlat, such as its applicability to different types of tasks or its scalability to larger multi-agent systems. Specifically, the paper does not address how the performance of Interlat might vary with different task complexities, such as tasks requiring long-term dependencies or complex reasoning. Furthermore, the scalability of the approach to systems with more than two agents is not explored, leaving open questions about its practical applicability in more complex scenarios."

2. Evidence Collection:
- The paper focuses on the benefits and performance of Interlat in the tested scenarios.
- There is no dedicated section discussing the limitations of the approach.

3. Literature Gap Analysis:
   - While the paper compares against baselines, it doesn't explicitly discuss the inherent limitations of the proposed method.

4. Validation Analysis:
   - The reviewer is correct. The paper primarily highlights the advantages of Interlat without a thorough discussion of its limitations regarding task complexity or scalability to larger systems.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks a dedicated section or explicit discussion on the limitations of Interlat.

1. Weakness Statement:
"The paper does not provide a thorough comparison with existing methods for multi-agent communication, particularly those that also leverage latent representations. While the paper mentions related work, it does not provide a detailed analysis of how Interlat differs from or improves upon these methods. A more comprehensive comparison would help to clarify the unique contributions of Interlat and its potential advantages over existing approaches."

2. Evidence Collection:
- The "Related Work" section (Section 2) discusses latent reasoning in LLMs and multi-agent communication.
- The "Experiments" section (Section 5) compares Interlat against CoT prompting and single-agent baselines.

3. Literature Gap Analysis:
   - While the paper mentions related work, the comparison in the experimental section is limited to task performance metrics.

4. Validation Analysis:
   - The reviewer has a point. While the paper mentions related work, the experimental comparison is primarily focused on task performance. A more detailed comparison of the mechanisms and assumptions of Interlat with other latent-based communication methods would be beneficial.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper mentions related work but the experimental comparison is limited to task performance.

1. Weakness Statement:
"The paper does not discuss the potential ethical implications of using Interlat, such as the risk of misuse or unintended consequences in multi-agent systems. A discussion of these ethical considerations would be important for ensuring the responsible development and deployment of Interlat."

2. Evidence Collection:
- The paper focuses on the technical aspects and performance of the proposed method.
- There is no section dedicated to ethical considerations.

3. Literature Gap Analysis:
   - The paper doesn't cite any works on the ethical implications of multi-agent systems or latent communication.

4. Validation Analysis:
   - The reviewer is correct. The paper lacks a discussion on the ethical implications of the proposed method.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks a dedicated section or discussion on ethical implications.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost of Interlat, including the time and memory requirements for training and inference. This information is crucial for assessing the practical feasibility of the approach and for comparing it with other methods."

2. Evidence Collection:
- The paper mentions the hardware used for experiments (NVIDIA A5000 GPUs) but doesn't provide detailed time and memory requirements.

3. Literature Gap Analysis:
   - There is no comparison of computational costs with other methods.

4. Validation Analysis:
   - The reviewer is correct. The paper lacks a detailed analysis of the computational cost of Interlat.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper doesn't provide detailed time and memory requirements for training and inference.

**Review 3 Weaknesses:**

1. Weakness Statement:
"The paper primarily focuses on a controlled two-agent setting, evaluated on one embodied interactive benchmark (ALFWorld) and one non-interactive symbolic reasoning benchmark (MATH). While these benchmarks provide a good starting point, they do not fully capture the diversity of real-world multi-agent systems, such as settings with larger teams, dynamic role assignments, long-horizon collaboration, or richer environments involving tool use and external memory. The lack of experiments in more complex scenarios limits the generalizability of the findings."

2. Evidence Collection:
b) Experiment-related Evidence:
   - Dataset/setup descriptions: "We evaluate our approach on Alfworld ( Shridhar et al., 2020 ) , and MATH Hendrycks et al. (2021) . For Alfworld, training is conducted using data from Song et al. (2024) . Qwen2LLaMA uses latents from Qwen2.5-7B to train LLaMA3.1-8B-Base Dubey et al. (2024) and LLaMA3.1-8B-Base Dubey et al. (2024) are employed as reasoning models in the information compression experiments." (Section 5)
   - The paper explicitly mentions using Alfworld and MATH, which are single-agent benchmarks. The experiments are conducted in a two-agent sender-receiver scenario.

3. Literature Gap Analysis:
   - While the paper mentions the complexity of multi-agent systems in the motivation, it doesn't include experiments on more complex multi-agent benchmarks.

4. Validation Analysis:
   - This is the same weakness identified by Reviewer 1, and the validation remains the same.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper explicitly states the use of Alfworld and MATH, which are single-agent benchmarks, and focuses on a two-agent scenario.

1. Weakness Statement:
"The approach assumes access to internal model representations, specifically last-layer hidden states, in order to enable latent communication. This assumption may not hold for closed-source or API-only models, where hidden states are inaccessible. As a result, the current formulation of Interlat is primarily applicable to open or inspectable models, and extending latent communication to restricted-access settings is an open challenge."

2. Evidence Collection:
a) Method-related Evidence:
   - "In this work, we propose Interlat, a novel framework that realizes this vision by enabling inter-agent communication entirely in latent space. Rather than transmitting discrete tokens decoded by the language head, Interlat directly transmits the temporally aligned last hidden states, which we termed latent communication." (Section 3)
   - "For each decoding step ℓ = 1 , … , L \ell=1:m L=T \litet{S S ​ = [ s 1 , … , s T } s=( s 1 , … , s L ) , where s un + ℓ = x m + ℓ , h 1 , h 2 , … , h L , e i + 1 = E i + 1 ( h i ) , generated by the trainable light-weight self-attention and a projection layer as a communication adapter for rescaling and interpretation." (Section 3.1)
   - "The latent communications are processed by a trainable light-weight self-attention and a projection layer as a communication adapter for rescaling and interpretation." (Section 3.1)
   - "We use base models as reasoning models in the information compression experiments." (Section 5.1)

3. Literature Gap Analysis:
   - The paper doesn't discuss methods for extracting latent representations from closed-source models.

4. Validation Analysis:
   - This is the same weakness identified by Reviewer 1, and the validation remains the same.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The method description explicitly mentions using the last hidden states, and the experiments use open-source models.

**Review 4 Weaknesses:**

1. Weakness Statement:
"The paper lacks a detailed analysis of the computational cost associated with the proposed method. Specifically, the paper does not provide a breakdown of the computational resources required for training and inference, such as the number of parameters, FLOPs, and memory usage. This information is crucial for assessing the practical feasibility of the method, especially when scaling to larger models and more complex multi-agent systems. The absence of this analysis makes it difficult to evaluate the trade-offs between performance gains and computational overhead."

2. Evidence Collection:
- The paper mentions the hardware used for experiments (NVIDIA A5000 GPUs) but doesn't provide detailed time and memory requirements.

3. Literature Gap Analysis:
   - There is no comparison of computational costs with other methods.

4. Validation Analysis:
   - This is the same weakness identified by Reviewer 2, and the validation remains the same.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper doesn't provide detailed time and memory requirements for training and inference.

1. Weakness Statement:
"The paper does not provide a comprehensive comparison with existing methods for multi-agent communication. While the paper compares the proposed method with some baselines, it does not compare with other state-of-the-art methods in the field, such as those based on graph neural networks or attention mechanisms. A more comprehensive comparison would help to better understand the strengths and weaknesses of the proposed method and its position in the broader landscape of multi-agent communication techniques. The lack of comparison with relevant methods makes it hard to assess the novelty and effectiveness of the proposed approach."

2. Evidence Collection:
- The "Experiments" section (Section 5) compares Interlat against CoT prompting and single-agent baselines.

3. Literature Gap Analysis:
   - While the paper mentions related work, the experimental comparison is limited to task performance metrics.

4. Validation Analysis:
   - This is the same weakness identified by Reviewer 2, and the validation remains the same.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper mentions related work but the experimental comparison is limited to task performance.

1. Weakness Statement:
"How does the performance of Interlat scale with the number of agents in a multi-agent system?"

2. Evidence Collection:
- The paper focuses on a two-agent setting.

3. Literature Gap Analysis:
   - The paper doesn't discuss the scalability to larger multi-agent systems.

4. Validation Analysis:
   - This is a valid question that the paper doesn't address.

5. Conclusion:
   - Validity status: Valid (as a question highlighting a missing analysis)
   - Confidence level: High
   - Key supporting evidence: The paper's experiments are limited to a two-agent setting.

1. Weakness Statement:
"What is the computational cost of Interlat compared to other multi-agent communication methods?"

2. Evidence Collection:
- The paper doesn't provide a detailed analysis of the computational cost of Interlat or compare it to other methods.

3. Literature Gap Analysis:
   - There is no comparison of computational costs.

4. Validation Analysis:
   - This is a valid question that the paper doesn't address.

5. Conclusion:
   - Validity status: Valid (as a question highlighting a missing analysis)
   - Confidence level: High
   - Key supporting evidence: The paper lacks a detailed analysis of the computational cost.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces Interlat, a novel framework designed to facilitate inter-agent communication entirely within the latent space of Large Language Models (LLMs). The core idea is to move away from traditional natural language-based communication, which the authors argue is limited by the downsampling of rich, internal latent states into discrete tokens. Instead, Interlat leverages the continuous last hidden states of LLMs as a representation of an agent's thought process, enabling more expressive and information-preserving interactions. The framework incorporates a supervised objective that encourages the interpretation and utilization of task-relevant latent information, and a compressed latent message to reduce inference latency while maintaining competitive performance. The authors conduct experiments in a two-agent sender-receiver scenario, demonstrating that Interlat outperforms both fine-tuned chain-of-thought (CoT) prompting and single-agent baselines, even across heterogeneous models. The results highlight Interlat’s potential as a feasible paradigm for future research in multi-agent systems. Specifically, the method involves transmitting the last hidden states of the LLM, which are then processed by a trainable communication adapter consisting of a light-weight self-attention mechanism and a projection layer. The framework is trained using a combination of a cross-entropy loss on the receiver's output, a separation loss to encourage the use of task-relevant latent information, and a preference loss to select the most effective communication strategy. The authors also explore the use of Interlat for information compression, demonstrating that it can reduce the inference latency while maintaining competitive performance through an efficient information-preserving mechanism. The experimental results show that Interlat achieves higher accuracy and better performance compared to the baselines in the sender-receiver task, and also demonstrate the effectiveness of the information preservation mechanism. Overall, the paper presents a compelling approach to multi-agent communication that addresses some of the limitations of natural language-based communication, and provides a promising direction for future research in this area. However, as I will discuss in the following sections, there are several limitations that need to be addressed in order to fully realize the potential of this approach.


## Soundness:

2.75


## Presentation:

3.0


## Contribution:

2.75


## Strengths:

The primary strength of this paper lies in its innovative approach to multi-agent communication. By shifting the focus from natural language to latent space communication, the authors have introduced a method that addresses the limitations of language-based communication, particularly the information loss caused by downsampling. This is a creative and novel idea that has the potential to open up new avenues for research in multi-agent systems. The paper is also well-written and easy to follow, with clear explanations of the proposed framework and its components. The authors have done a commendable job of presenting the method in a way that is accessible to a broad audience, and the figures and tables are well-designed and effectively illustrate the key concepts and findings. Furthermore, the authors have conducted a comprehensive set of experiments to evaluate Interlat, including comparisons with various baselines and ablation studies. The results demonstrate the effectiveness of Interlat in enhancing multi-agent communication and improving task performance, which is a significant achievement. The authors also provide a detailed analysis of the information preservation mechanism used in Interlat, including a head-coverage statistic and a comparison with other compression techniques. This analysis provides valuable insights into the inner workings of the framework and helps to explain its effectiveness. The use of a supervised objective that explicitly encourages the interpretation and utilization of task-relevant latent information is another notable strength of the paper. This objective helps to ensure that the agents are communicating effectively and that the receiver is able to extract the necessary information to perform the task. The authors also demonstrate the effectiveness of Interlat in a two-agent sender-receiver scenario, which is a good starting point for further research in this area. The results show that Interlat outperforms both fine-tuned chain-of-thought (CoT) prompting and single-agent baselines, even across heterogeneous models. This is a significant achievement, as it demonstrates the robustness and generalizability of the framework. Finally, the paper's focus on addressing the limitations of natural language-based communication is a valuable contribution to the field. The authors have identified a key challenge in multi-agent systems and have proposed a novel approach that has the potential to overcome this challenge. Overall, the paper presents a well-executed and innovative approach to multi-agent communication that has the potential to make a significant impact on the field.


## Weaknesses:

Despite the strengths of the proposed approach, there are several weaknesses that need to be addressed. First, the paper's experimental evaluation is limited in scope. The authors primarily focus on a controlled two-agent setting, evaluated on the Alfworld and MATH benchmarks. While these benchmarks provide a good starting point, they do not fully capture the diversity of real-world multi-agent systems. Specifically, the experiments are conducted in a single-agent setting, and the multi-agent scenario is limited to a sender-receiver setup. This lack of experiments in more complex scenarios, such as settings with larger teams, dynamic role assignments, long-horizon collaboration, or richer environments involving tool use and external memory, limits the generalizability of the findings. As Reviewer 1 correctly points out, the paper does not explore scenarios with larger teams, dynamic role assignments, or long-horizon collaboration. This is a significant limitation, as real-world multi-agent systems often involve more complex interactions and coordination. The absence of experiments in more complex scenarios makes it difficult to assess the robustness and generalizability of Interlat in more realistic and challenging settings. My analysis confirms that the paper explicitly states the use of Alfworld and MATH, which are single-agent benchmarks, and focuses on a two-agent scenario. This limitation is significant because it restricts the applicability of the findings to more complex multi-agent systems. Second, the approach assumes access to internal model representations, specifically the last-layer hidden states, in order to enable latent communication. This assumption may not hold for closed-source or API-only models, where hidden states are inaccessible. As Reviewer 1 and Reviewer 3 both note, this assumption limits the applicability of the current formulation of Interlat to open or inspectable models. The paper does not explore alternative approaches that do not rely on this assumption, such as methods for extracting latent representations from model outputs or using techniques such as adversarial training to learn representations that are robust to changes in the model architecture. This is a significant limitation because it restricts the use of Interlat in many real-world scenarios where access to model internals is not possible. My analysis confirms that the method description explicitly mentions using the last hidden states, and the experiments use open-source models. This limitation is significant because it restricts the applicability of the findings to more realistic scenarios. Third, the paper lacks a detailed analysis of the computational cost associated with the proposed method. While the paper mentions the hardware used for experiments, it does not provide a breakdown of the computational resources required for training and inference, such as the number of parameters, FLOPs, and memory usage. This information is crucial for assessing the practical feasibility of the approach, especially when scaling to larger models and more complex multi-agent systems. As Reviewer 2 and Reviewer 4 correctly point out, the absence of this analysis makes it difficult to evaluate the trade-offs between performance gains and computational overhead. My analysis confirms that the paper does not provide detailed time and memory requirements for training and inference. This limitation is significant because it makes it difficult to assess the practical feasibility of the approach. Fourth, the paper does not provide a comprehensive comparison with existing methods for multi-agent communication. While the paper mentions related work, the experimental comparison is primarily focused on task performance metrics. A more detailed comparison of the mechanisms and assumptions of Interlat with other latent-based communication methods would be beneficial. As Reviewer 2 notes, a more thorough comparison would help to clarify the unique contributions of Interlat and its potential advantages over existing approaches. My analysis confirms that the paper mentions related work but the experimental comparison is limited to task performance. This limitation is significant because it makes it difficult to assess the novelty and effectiveness of the proposed approach. Fifth, the paper does not discuss the potential ethical implications of using Interlat, such as the risk of misuse or unintended consequences in multi-agent systems. As Reviewer 2 points out, a discussion of these ethical considerations would be important for ensuring the responsible development and deployment of Interlat. My analysis confirms that the paper lacks a dedicated section or discussion on ethical implications. This limitation is significant because it raises important ethical considerations that need to be addressed. Finally, the paper does not discuss the limitations of Interlat, such as its applicability to different types of tasks or its scalability to larger multi-agent systems. Specifically, the paper does not address how the performance of Interlat might vary with different task complexities, such as tasks requiring long-term dependencies or complex reasoning. Furthermore, the scalability of the approach to systems with more than two agents is not explored, leaving open questions about its practical applicability in more complex scenarios. As Reviewer 2 correctly points out, the paper primarily highlights the advantages of Interlat without a thorough discussion of its limitations regarding task complexity or scalability to larger systems. My analysis confirms that the paper lacks a dedicated section or explicit discussion on the limitations of Interlat. This limitation is significant because it restricts the understanding of the applicability of the approach.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should expand their experimental evaluation to include more complex multi-agent scenarios. Specifically, they could explore settings with a larger number of agents, dynamic role assignments, and more intricate communication patterns. For example, they could investigate how Interlat performs in a collaborative task where agents need to coordinate their actions over a longer time horizon, or in a scenario where agents have different levels of expertise and need to communicate effectively despite these differences. Furthermore, they could explore the use of more realistic environments that involve tool use and external memory, which would provide a more comprehensive evaluation of the framework's capabilities. This would help to demonstrate the robustness and generalizability of Interlat in more realistic and challenging settings. Second, to address the limitation of assuming access to internal model representations, the authors could explore alternative approaches that do not rely on this assumption. For example, they could investigate methods for extracting latent representations from model outputs or using techniques such as adversarial training to learn representations that are robust to changes in the model architecture. Another approach could involve using a shared latent space that is learned jointly by all agents, which would allow them to communicate without requiring access to each other's internal representations. This would make the framework more applicable to a wider range of scenarios, including those where agents are deployed on different platforms or have limited access to each other's internal states. The authors should also discuss the potential limitations of their approach in scenarios where the internal representations are not well-aligned or where there are significant differences in the way that different models process information. Third, the authors should provide a more detailed analysis of the computational cost associated with the proposed method. This analysis should include a breakdown of the computational resources required for both training and inference, such as the number of parameters, FLOPs, and memory usage. It would be beneficial to provide a comparison of these metrics with the baseline methods used in the experiments. This would allow readers to better understand the trade-offs between performance gains and computational overhead. Furthermore, the authors should discuss the scalability of the method with respect to model size and the number of agents. This would help to assess the practical applicability of the method in real-world scenarios. Fourth, the authors should provide a more detailed comparison of Interlat with existing methods for multi-agent communication, particularly those that also leverage latent representations. This comparison should not only focus on performance metrics but also on other aspects such as communication efficiency, robustness, and scalability. The authors should also discuss the limitations of the proposed method and identify potential areas for future research. This would provide a more complete picture of the method's strengths and weaknesses and help to guide future research in this area. Fifth, the authors should include a discussion of the potential ethical implications of using Interlat, such as the risk of misuse or unintended consequences in multi-agent systems. This discussion should consider the potential for Interlat to be used for harmful purposes, such as manipulating other agents or controlling their behavior. The authors should also discuss the potential for Interlat to be used in ways that could lead to unintended consequences, such as the creation of artificial intelligence systems that are difficult to control or understand. Finally, the authors should provide a more detailed discussion of the limitations of the proposed Interlat framework. Specifically, the authors should explore how the performance of Interlat varies with different task complexities. For example, it would be valuable to test the framework on tasks that require long-term dependencies, such as those involving planning or sequential decision-making, and compare its performance with tasks that are more localized in time and space. Additionally, the authors should investigate the scalability of the approach to larger multi-agent systems. This could involve experiments with more than two agents to determine whether the performance gains observed in the current setup hold true in more complex scenarios. Furthermore, the authors should analyze the computational cost of Interlat in detail, including the time and memory requirements for training and inference. This analysis should also consider the impact of different hyperparameter settings on the computational cost and performance of the framework. This would allow readers to better understand the trade-offs between performance gains and computational overhead.


## Questions:

Based on my analysis, I have several questions that I believe are important for further understanding the proposed method. First, how does the performance of Interlat scale with the number of agents in a multi-agent system? The paper focuses on a two-agent setting, but it is unclear how the framework would perform in scenarios with a larger number of agents. This is a critical question because real-world multi-agent systems often involve more than two agents, and it is important to understand the scalability of the approach. Second, what is the computational cost of Interlat compared to other multi-agent communication methods? The paper does not provide a detailed analysis of the computational cost, and it is important to understand the trade-offs between performance gains and computational overhead. This is a critical question because it will determine the practical feasibility of the approach in real-world scenarios. Third, how does the information preservation mechanism in Interlat work, and what are its limitations? While the paper provides a head-coverage statistic and a comparison with other compression techniques, it would be beneficial to have a more detailed explanation of the mechanism and its limitations. This is important because the information preservation mechanism is a key component of the framework, and it is important to understand its strengths and weaknesses. Fourth, how does Interlat perform on tasks that require long-term dependencies or complex reasoning? The paper focuses on relatively simple tasks, and it is unclear how the framework would perform on more complex tasks that require long-term planning or sequential decision-making. This is a critical question because real-world multi-agent systems often involve tasks that require complex reasoning and planning. Fifth, how does the performance of Interlat vary with different model architectures? The paper uses Qwen2LLaMA as the base model, but it is unclear how the framework would perform with other models, especially closed-source or API-only models where hidden states are inaccessible. This is a critical question because it will determine the applicability of the approach to a wider range of scenarios. Finally, what are the potential ethical implications of using Interlat, such as the risk of misuse or unintended consequences in multi-agent systems? The paper does not discuss the ethical considerations, and it is important to address these issues to ensure the responsible development and deployment of the approach. These questions are important for further understanding the proposed method and its potential applications.


## Rating:

6.25


## Confidence:

3.0


## Decision:

Reject
}