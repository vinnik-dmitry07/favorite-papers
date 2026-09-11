I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper proposes a new RLHF algorithm for LLMs, called HICRA, which is designed to focus optimization pressure on high-level planning tokens, which are tokens that are part of Strategic Grams (SGs). SGs are defined as n-grams that function as a single semantic unit to guide the logical flow of the reasoning process. The paper shows that HICRA outperforms existing baselines on several reasoning datasets, and that it can be applied to both text-only and vision-language models.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow, with clear explanations of the proposed method and experimental setup.
- The paper provides a novel perspective on the learning dynamics of LLMs during RL training, and proposes a new algorithm that is specifically designed to take advantage of this perspective.
- The paper provides extensive experimental results on several datasets and models, which demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a clear definition of what constitutes a "strategic token" or a "procedural token", and how these tokens are identified. This makes it difficult to understand the proposed method and to reproduce the results.
- The paper does not provide a clear explanation of how the proposed method is different from existing RLHF algorithms, such as PPO or REINFORCE. It is not clear what specific modifications are made to the RL algorithm to achieve the proposed results.
- The paper does not provide a clear explanation of how the proposed method is applied to vision-language models, and how the visual tokens are treated in the proposed method.
- The paper does not provide a clear explanation of how the proposed method is applied to models with different architectures, such as encoder-decoder models or decoder-only models.
- The paper does not provide a clear explanation of how the proposed method is applied to models with different sizes, such as small, medium, or large models.
- The paper does not provide a clear explanation of how the proposed method is applied to models with different training datasets, such as datasets with different sizes or different domains.
- The paper does not provide a clear explanation of how the proposed method is applied to models with different optimization algorithms, such as Adam or SGD.

### Suggestions

The paper needs to provide a more precise definition of what constitutes a "strategic token" and a "procedural token." The current description is vague and does not provide a clear understanding of how these tokens are identified. For example, are these tokens defined based on their frequency in a corpus, their semantic meaning, or some other criteria? The paper should also provide a concrete example of how these tokens are identified in a given text. Furthermore, the paper should clarify how the proposed method differs from existing RLHF algorithms. It is not sufficient to simply state that the proposed method is designed to focus optimization pressure on high-level planning tokens. The paper should provide a detailed explanation of the specific modifications made to the RL algorithm and how these modifications lead to the observed improvements. For example, how does the HICRA algorithm modify the reward function or the policy update rule compared to standard RL algorithms like PPO or REINFORCE? A more detailed explanation of these differences is needed to understand the novelty of the proposed method.

The paper should also provide a more detailed explanation of how the proposed method is applied to vision-language models. The current description is too brief and does not provide a clear understanding of how the visual tokens are treated. For example, are the visual tokens treated as a separate set of tokens, or are they integrated into the textual tokens? How does the proposed method handle the differences in the visual and textual modalities? The paper should also provide a more detailed explanation of how the proposed method is applied to models with different architectures, such as encoder-decoder models or decoder-only models. The paper should explain how the proposed method is adapted to different model architectures and how the strategic and procedural tokens are identified in these models. For example, in encoder-decoder models, how are the tokens identified as strategic or procedural, given that there is no explicit decoder? The paper should also provide a more detailed explanation of how the proposed method is applied to models with different sizes, such as small, medium, or large models. The paper should explain how the proposed method is adapted to different model sizes and how the strategic and procedural tokens are identified in these models. For example, does the number of strategic tokens change with model size? Finally, the paper should provide a more detailed explanation of how the proposed method is applied to models with different training datasets, such as datasets with different sizes or different domains. The paper should explain how the proposed method is adapted to different datasets and how the strategic and procedural tokens are identified in these datasets. For example, does the frequency of strategic tokens change with the dataset? The paper should also provide a more detailed explanation of how the proposed method is applied to models with different optimization algorithms, such as Adam or SGD. The paper should explain how the proposed method is adapted to different optimization algorithms and how the strategic and procedural tokens are identified in these models. For example, does the learning rate affect the effectiveness of the proposed method?

### Questions

- How are the strategic and procedural tokens identified in the proposed method? Is there a specific algorithm or heuristic used to identify these tokens?
- How does the proposed method differ from existing RLHF algorithms, such as PPO or REINFORCE?
- How is the proposed method applied to vision-language models?
- How is the proposed method applied to models with different architectures, such as encoder-decoder models or decoder-only models?
- How is the proposed method applied to models with different sizes, such as small, medium, or large models?
- How is the proposed method applied to models with different training datasets, such as datasets with different sizes or different domains?
- How is the proposed method applied to models with different optimization algorithms, such as Adam or SGD?

### Rating

5

### Confidence

3

**********

## Reviewer 2

### Summary

This paper proposes a new method for reasoning tasks based on RLHF. It identifies the hierarchical structure of reasoning process and proposes to focus optimization pressure on high-level strategic planning tokens. The experiments on multiple models and tasks show that the proposed method can improve the performance.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. This paper is well-written and easy to follow.
2. The proposed method is simple and effective.
3. The experiments are comprehensive.

### Weaknesses

#### Some Related Works


#### comment

1. The main concern is the novelty of the proposed method. It seems that the proposed method is an application of existing methods to the reasoning task. The proposed method is not a general method for RLHF and can only be applied to reasoning tasks. Specifically, the method relies on identifying "strategic planning tokens" which are task-specific and require manual annotation or sophisticated analysis, limiting its general applicability. The core idea of focusing optimization on specific tokens, while effective for reasoning, lacks a broader theoretical foundation and may not translate well to other RLHF scenarios where such token-level control is not feasible.
2. The authors claim that the proposed method can be applied to VLMs, but there is no experiment to support this. The paper lacks a detailed explanation of how the proposed method would be adapted to VLMs, particularly concerning the handling of visual tokens and the integration of visual information into the RL training loop. The absence of empirical validation on VLMs is a significant gap, especially given the authors' claim of broad applicability.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations of the proposed method, particularly regarding its dependence on task-specific "strategic planning tokens." The authors should explore alternative approaches for identifying these tokens that do not rely on manual annotation or task-specific analysis. For example, they could investigate methods for automatically identifying high-impact tokens based on their semantic role or their contribution to the final outcome. This would significantly enhance the generalizability of the proposed method and make it more applicable to a wider range of RLHF tasks. Furthermore, the authors should provide a more detailed analysis of the theoretical underpinnings of their approach, explaining why focusing optimization pressure on specific tokens leads to improved performance. This could involve exploring connections to existing theories of learning and generalization in reinforcement learning.

To address the lack of experimental validation on VLMs, the authors should provide a detailed description of how their method would be adapted to these models. This should include a discussion of how visual tokens would be treated, whether they would be treated as a separate set of tokens or integrated into the textual tokens. The authors should also discuss the challenges of applying their method to VLMs, such as the need to handle visual information and the potential for increased computational complexity. Furthermore, they should provide a clear roadmap for future experiments, outlining the specific steps that would be taken to validate their method on VLMs. This could include a discussion of the appropriate datasets, evaluation metrics, and baseline models for comparison.

Finally, the authors should consider expanding their experimental evaluation to include a wider range of reasoning tasks and model architectures. This would help to demonstrate the robustness and generalizability of their method. They should also compare their method to other state-of-the-art RLHF techniques for reasoning tasks, providing a more comprehensive analysis of its strengths and weaknesses. This would help to position their work within the broader context of RLHF research and highlight its unique contributions.

### Questions

1. What is the definition of the strategic planning tokens? Can it be applied to other tasks?
2. Can the proposed method be applied to VLMs?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper explores the learning dynamics of large language models (LLMs) during reinforcement learning (RL) training and introduces a novel algorithm called Hierarchy-Aware Credit Assignment (HICRA). The authors observe that RL training for LLMs involves two distinct phases: first, the model focuses on mastering low-level execution skills, and second, it shifts its attention to strategic planning. HICRA leverages this insight by prioritizing optimization pressure on high-level planning tokens, which are identified using a functional proxy for reasoning. The paper demonstrates that HICRA outperforms standard RL algorithms across various text-only and vision-language models, highlighting the importance of strategic planning in advanced reasoning tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper presents a novel approach to RLHF for LLMs, introducing HICRA, which targets optimization pressure on high-level planning tokens.
- The authors provide extensive experimental results, demonstrating HICRA's effectiveness across multiple models and tasks.
- The paper offers a clear and well-structured explanation of the proposed method and its advantages over existing RLHF techniques.

### Weaknesses

#### Some Related Works


#### comment

 - The paper could benefit from a more detailed discussion of the limitations of the proposed approach, particularly in scenarios where the identified strategic planning tokens may not be readily available or easily defined.
- The paper could provide more insights into the computational overhead of HICRA compared to standard RL algorithms.
- The paper could benefit from a more thorough discussion of the sensitivity of HICRA to the choice of hyperparameters, such as the hyperparameter α in the HICRA algorithm.

### Suggestions

The paper should delve deeper into the practical challenges of applying HICRA in scenarios where identifying strategic planning tokens is difficult or impossible. For instance, in tasks that require complex, multi-step reasoning without clear, pre-defined strategic tokens, the effectiveness of HICRA might be significantly reduced. The authors should explore alternative strategies for defining or approximating strategic planning tokens in such cases, perhaps by using techniques like attention mechanisms or by learning a latent representation of strategic actions. Furthermore, the paper should discuss the potential impact of noisy or inaccurate identification of strategic tokens on the overall performance of HICRA. A more thorough analysis of these limitations would provide a more complete picture of the applicability of the proposed method.

To enhance the practical relevance of the paper, a detailed analysis of the computational cost of HICRA compared to standard RL algorithms is crucial. The authors should provide a breakdown of the computational overhead associated with identifying strategic planning tokens and computing the HICRA reward. This analysis should include both time and memory requirements, and should be conducted across different model sizes and datasets. Furthermore, the paper should explore potential optimizations to reduce the computational cost of HICRA, such as using more efficient token identification methods or approximating the HICRA reward. A clear understanding of the computational trade-offs would allow practitioners to make informed decisions about the suitability of HICRA for their specific applications.

Finally, the paper should include a more comprehensive analysis of the sensitivity of HICRA to its hyperparameters, particularly the α parameter. The authors should conduct a systematic study of how different values of α affect the performance of HICRA across various tasks and datasets. This study should include not only the final performance metrics but also the learning curves and the convergence behavior of the algorithm. The paper should also discuss the potential for adaptive hyperparameter tuning, which could further improve the robustness and performance of HICRA. A thorough sensitivity analysis would provide valuable insights into the practical application of the proposed method and would help users to effectively tune the hyperparameters for their specific use cases.

### Questions

- How does HICRA perform in scenarios where the definition of strategic planning tokens is ambiguous or unavailable?
- What is the computational overhead of HICRA compared to standard RL algorithms, and how does it scale with model size and dataset complexity?
- How sensitive is HICRA to the choice of hyperparameters, particularly the hyperparameter α in the HICRA algorithm?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

This paper proposes a novel method to improve the reasoning abilities of large language models (LLMs) through reinforcement learning (RL). The authors observe that during RL training, LLMs first refine their low-level skills, such as accuracy in calculations, before advancing to more complex reasoning tasks. They identify two distinct phases in the learning process: a "procedural correctness" phase focused on refining low-level skills and a "strategic planning" phase focused on developing higher-level reasoning strategies. The authors introduce a new algorithm, Hierarchy-Aware Credit Assignment (HICRA), which targets optimization pressure on high-level planning tokens, allowing the model to better explore and refine its strategic planning abilities. HICRA builds on existing RL algorithms by selectively amplifying the learning signal for planning tokens, which are identified using a functional proxy for reasoning. The authors validate HICRA through extensive experiments across various models and reasoning tasks, showing that it outperforms standard RL baselines and offers deeper insights into how reasoning advances through the lens of strategic exploration.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel perspective on the learning dynamics of LLMs during RL training, identifying a clear two-phase process: procedural correctness and strategic planning. This hierarchical view of learning is a significant contribution to the understanding of how LLMs develop reasoning abilities.
2. The proposed HICRA algorithm is well-motivated and builds upon existing RL methods, making it relatively easy to implement and integrate into existing RL training pipelines. The authors provide a clear explanation of how HICRA targets optimization pressure on high-level planning tokens, which is a key innovation in the paper.
3. The paper provides extensive experimental results across various models and reasoning tasks, demonstrating the effectiveness of HICRA over standard RL baselines. The authors also provide detailed analysis of the learning dynamics, including token-level entropy and semantic entropy, which offers valuable insights into how HICRA improves reasoning abilities.
4. The paper is well-written and organized, with clear explanations of the proposed method and experimental setup. The authors also provide a comprehensive discussion of related work and limitations, which helps to contextualize their contributions within the broader field of LLM research.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on text-based reasoning tasks, and it is unclear how well the proposed method would generalize to other types of reasoning tasks, such as multi-modal reasoning or logical reasoning tasks that require symbolic manipulation. The authors should provide more discussion on the potential limitations of HICRA in these contexts and suggest possible extensions or modifications that could be explored in future work.
2. While the paper provides a detailed analysis of the learning dynamics, it would be beneficial to include more visualizations of the model's behavior during training, such as the distribution of planning tokens and the evolution of semantic entropy over time. This would provide a more intuitive understanding of how HICRA affects the model's learning process.
3. The paper could benefit from a more thorough comparison with other state-of-the-art RL methods for LLMs, particularly those that also focus on improving reasoning abilities. A more comprehensive comparison would help to better position HICRA within the existing literature and highlight its unique contributions.
4. The paper does not discuss the computational cost of HICRA in detail, which is an important consideration for practical applications. The authors should provide more information on the training time and memory requirements of HICRA compared to standard RL baselines.

### Suggestions

The authors should consider expanding their experimental evaluation to include a wider range of reasoning tasks, particularly those that involve multi-modal inputs or symbolic reasoning. For example, evaluating HICRA on tasks that require visual reasoning or logical inference would provide a more comprehensive assessment of its generalizability. Specifically, the authors could explore how HICRA performs on tasks that involve understanding and reasoning about spatial relationships in images, or tasks that require logical deduction based on symbolic representations. This would help to identify potential limitations of the current approach and guide future research directions. Furthermore, the authors should investigate the impact of different token selection strategies on the performance of HICRA. For instance, they could explore methods for automatically identifying planning tokens based on their semantic content or their importance in the reasoning process. This would make the method more adaptable to different types of reasoning tasks and reduce the need for manual annotation.

To enhance the analysis of the learning dynamics, the authors should include more detailed visualizations of the model's behavior during training. Specifically, they should provide plots of the distribution of planning tokens over time, as well as the evolution of semantic entropy for both planning and execution tokens. These visualizations would provide a more intuitive understanding of how HICRA affects the model's learning process and how it shifts the focus from low-level skills to high-level strategic planning. Additionally, the authors could investigate the relationship between the magnitude of the credit assignment for planning tokens and the improvement in reasoning performance. This would provide insights into the effectiveness of the proposed method and help to identify potential areas for improvement. The authors should also consider using techniques such as saliency maps to visualize which parts of the input are most influential for planning token selection.

Finally, the authors should provide a more thorough comparison with other state-of-the-art RL methods for LLMs, particularly those that also focus on improving reasoning abilities. This comparison should include a detailed analysis of the strengths and weaknesses of each method, as well as a discussion of the trade-offs between different approaches. The authors should also provide a more detailed analysis of the computational cost of HICRA, including the training time and memory requirements. This information is crucial for practical applications and would help to assess the feasibility of using HICRA in real-world scenarios. The authors should also consider comparing the performance of HICRA with other methods that use different reward shaping techniques, as this could provide further insights into the effectiveness of the proposed approach.

### Questions

1. How does the performance of HICRA vary across different types of reasoning tasks, such as multi-modal reasoning or logical reasoning tasks that require symbolic manipulation? Are there specific types of tasks where HICRA performs particularly well or poorly?
2. What is the impact of the hyperparameter α on the performance of HICRA? How sensitive is the method to different values of α, and what are the guidelines for selecting an appropriate value?
3. How does the computational cost of HICRA compare to standard RL baselines? Are there any specific optimizations that could be applied to reduce the computational overhead of HICRA?

### Rating

8

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in a given paper. I need to go through each reviewer's comments and find evidence in the paper that supports their claims. I will categorize the weaknesses and then look for specific quotes, experimental details, or missing information in the paper to back up the reviewers' points.

Here's a plan:
1. Go through each reviewer's comments one by one.
2. For each comment identified as a weakness, try to find supporting evidence in the paper.
3. If the weakness is about the method, I will look for issues in the description of HICRA, the definition of strategic planning tokens, or the connection to existing RL methods.
4. If the weakness is about the experiments, I will look for missing details about the datasets, baselines, metrics, or implementation.
5. If the weakness is about the writing or clarity, I will note specific instances in the paper.
6. Finally, I will synthesize the findings and provide a conclusion for each weakness, indicating if it's valid, partially valid, or invalid, along with a confidence level and key supporting evidence.
**Review 1 Weaknesses:**

1. Weakness Statement:
"The paper does not provide a clear definition of what constitutes a "strategic token" or a "procedural token", and how these tokens are identified. This makes it difficult to understand the proposed method and to reproduce the results."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper introduces "strategic planning Tokens" in the "main_idea" section: "The learning process is characterized by a two-phase dynamic: initially, the model focuses on procedural correctness, and then it shifts to strategic planning."
   - The definition of strategic planning tokens is provided in the "main_idea" and "method" sections: "These tokens are identified using a functional proxy, which is a set of n-grams that function as a single semantic unit to guide the logical flow of the reasoning process." and "The functional proxy is constructed using a semantic clustering approach to identify groups of n-grams that are semantically equivalent."
   - The paper provides an example of a functional proxy: "For example, in a mathematical reasoning task, a functional proxy might be the set of n-grams that represent basic arithmetic operations."
   - The paper also describes the identification process: "The identification of these clusters is based on the frequency of the n-grams in the corpus and the semantic similarity between them."

3. Literature Gap Analysis:
   - The paper cites works related to hierarchical reasoning and cognitive architecture, which implicitly support the concept of strategic planning tokens.

4. Validation Analysis:
   - While the paper defines strategic planning tokens and the method for their identification, the reviewer might find the explanation insufficient for complete clarity and ease of reproduction. The process involves semantic clustering, which could benefit from more detailed explanation or a concrete algorithm.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper defines strategic planning tokens and the identification process, but the explanation could be more detailed for easier reproduction.

1. Weakness Statement:
"The paper does not provide a clear explanation of how the proposed method is different from existing RLHF algorithms, such as PPO or REINFORCE. It is not clear what specific modifications are made to the RL algorithm to achieve the proposed results."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper introduces HICRA as a modification of the GRPO framework: "Building on our functional proxy for reasoning, we examine the learning dynamics of RL for LLM reasoning and finds an intriguing parallel with human-like hierarchical reasoning. The core mechanism of HICRA engineers more effective exploration by reshaping the policy update’s target distribution. A standard policy gradient (Williams, 2004) update nudges the policy π θ o l d toward an implicit target distribution π ∗ , defined by the advantage function described as follows (the derivation is included in the appendix): π ∗ ​ ( o i , t ) ∝ π θ o l d ​ ( o i , t ) exp ​ ( A ^ i , t ) where α ∈ ( 0 , 1 ) is a hyperparameter controlling the amplification intensity (we use α = 0.2 in our experiments). HICRA, pronounced “high-krah”, modifies this advantage to prioritize planning tokens. Let 𝒮 i be the set of indices corresponding to planning tokens within trajectory 𝒐 i , identified using the method in Section 2.1. We define the HICRA advantage as: A ^ i , t HICRA = { A ^ i , t + α ⋅ | A ^ i , t | if ​ t ∈ 𝒮 i A ^ i , t if ​ t ∉ 𝒮 i }"
   - The paper explicitly states that HICRA builds upon GRPO: "Our empirical analysis reveals a fundamental insight: RL does not train models de novo. It fine-tunes base models already imbued with priors from pre-training on vast corpora of human-written solutions. These solutions inherently encodes the hierarchical structure of human reasoning – a highly efficient cognitive strategy evolved under biological constraints. This prompts us to ask: does RL unlock advanced reasoning by (re-)discovering this hierarchical structure? If the primary driver for advanced reasoning is the mastery of high-level strategic planning, then current agnostic credit assignment methods used in the prevailing GRPO ( Guo et al., 2025 ) and its variants ( Yu et al., 2025 ; Liu et al., 2025b ; Wang et al., 2025c ) are fundamentally inefficient, as they dilute optimization pressure across all tokens rather than concentrating it where it matters most."

4. Validation Analysis:
   - The paper clearly explains that HICRA modifies the standard GRPO algorithm by adjusting the advantage function to prioritize planning tokens. This modification is the key difference.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: The paper explicitly describes the modification to the GRPO algorithm in the method section.

1. Weakness Statement:
"The paper does not provide a clear explanation of how the proposed method is applied to vision-language models, and how the visual tokens are treated in the proposed method."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions experiments on VLMs in the "experiments" section: "We evaluate HICRA on a suite of challenging text-only and vision-language models, including Qwen2.5-7B (Yang et al., 2024 ) , Qwen3-4B ( Yang et al., 2025 ) , LLama-3.1-8B ( Grattafiori et al., 2024 ) , and VLMs like Qwen2.5-VL-7b ( Yang et al., 2024 ) and MiMO-VL-7B ( Xiaomi, 2025 ) , covering both base and instruction-tuned variants."
   - The paper states that the same functional proxy is used for both text-only and vision-language models: "The same functional proxy is used for both text-only and vision-language models, ensuring a consistent evaluation of the method's effectiveness across different model types."
   - The paper does not explicitly detail how visual tokens are treated. It assumes that the functional proxy, which is based on textual n-grams, can be applied to the textual component of the VLMs.

4. Validation Analysis:
   - The paper mentions applying HICRA to VLMs and using the same functional proxy. However, it lacks specific details on how visual tokens are handled within the HICRA framework. It's unclear if the visual tokens are treated as a separate set or integrated into the textual processing.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper mentions VLM experiments and the use of the same functional proxy, but lacks details on the treatment of visual tokens.

1. Weakness Statement:
"The paper does not provide a clear explanation of how the proposed method is applied to models with different architectures, such as encoder-decoder models or decoder-only models."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper lists the models used in the experiments, which include both decoder-only (LLama-3.1-8B, Qwen2.5-7B, Qwen3-4B) and encoder-decoder (Qwen2.5-VL-7b, MiMO-VL-7B) architectures.
   - The paper does not explicitly detail how the architecture affects the application of HICRA.

4. Validation Analysis:
   - While the paper shows experiments on different architectures, it doesn't explain how HICRA adapts to these differences. The core idea of focusing on planning tokens should be applicable, but the implementation details might vary.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: Experiments on different architectures are present, but the adaptation of HICRA is not explained.

1. Weakness Statement:
"The paper does not provide a clear explanation of how the proposed method is applied to models with different sizes, such as small, medium, or large models."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper lists models of varying sizes (e.g., Qwen2.5-7B, Qwen3-4B, LLama-3.1-8B).
   - The paper does not explicitly discuss how model size affects the application of HICRA or if any adjustments were made for different sizes.

4. Validation Analysis:
   - The paper shows experiments on models of different sizes, but it doesn't explain if the HICRA method or its implementation are affected by model size.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: Experiments on different sizes are present, but the impact on HICRA is not discussed.

1. Weakness Statement:
"The paper does not provide a clear explanation of how the proposed method is applied to models with different training datasets, such as datasets with different sizes or different domains."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions using open-source models and evaluating on established reasoning datasets (DAPO, DeepSeekR, etc.).
   - The paper does not explicitly discuss the impact of different training datasets on the application of HICRA.

4. Validation Analysis:
   - The paper shows experiments on models trained with different datasets, but it doesn't explain how HICRA interacts with or is affected by these datasets.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: Experiments on different datasets are present, but the interaction with HICRA is not discussed.

1. Weakness Statement:
"The paper does not provide a clear explanation of how the proposed method is applied to models with different optimization algorithms, such as Adam or SGD."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions GRPO as a baseline, which is an optimization algorithm.
   - The paper does not explicitly state whether HICRA is compatible with different optimization algorithms or if it is tied to GRPO.

4. Validation Analysis:
   - The paper focuses on GRPO as the base RL algorithm and doesn't discuss the compatibility of HICRA with other optimizers.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper focuses on GRPO and doesn't discuss compatibility with other optimizers.

**Review 2 Weaknesses:**

1. Weakness Statement:
"The paper primarily focuses on text-based reasoning tasks, and it is unclear how well the proposed method would generalize to other types of reasoning tasks, such as multi-modal reasoning or logical reasoning tasks that require symbolic manipulation. The authors should provide more discussion on the potential limitations of HICRA in these contexts and suggest possible extensions or modifications that could be explored in future work."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper includes experiments on VLMs, which involve multi-modal reasoning.
   - The paper does not explicitly discuss logical reasoning tasks requiring symbolic manipulation.

4. Validation Analysis:
   - The paper demonstrates results on VLMs, addressing multi-modal reasoning. However, it lacks discussion on the applicability to purely symbolic logical reasoning and potential limitations.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: Experiments on VLMs are present, but discussion on symbolic reasoning is missing.

1. Weakness Statement:
"While the paper provides a detailed analysis of the learning dynamics, it would be beneficial to include more visualizations of the model's behavior during training, such as the distribution of planning tokens and the evolution of semantic entropy over time. This would provide a more intuitive understanding of how HICRA affects the model's learning process."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper includes Figure 3, which shows the evolution of semantic entropy over training.
   - The paper does not include visualizations of the distribution of planning tokens over time.

4. Validation Analysis:
   - The paper does include one visualization of semantic entropy, but lacks visualizations of the distribution of planning tokens.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: Semantic entropy visualization is present, but planning token distribution is missing.

1. Weakness Statement:
"The paper could benefit from a more thorough comparison with other state-of-the-art RL methods for LLMs, particularly those that also focus on improving reasoning abilities. A more comprehensive comparison would help to better position HICRA within the existing literature and highlight its unique contributions."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper compares HICRA with the base model, GRPO, and Entropy Regularization.
   - The paper does not compare against other state-of-the-art RL methods specifically designed for improving reasoning in LLMs.

3. Literature Gap Analysis:
   - The related work section mentions some RL methods for LLMs but doesn't provide a direct comparison in the experimental section.

4. Validation Analysis:
   - The paper compares against relevant baselines but could include a broader comparison with other state-of-the-art reasoning-focused RL methods.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The experimental section lacks comparison with a broader range of state-of-the-art reasoning-focused RL methods.

1. Weakness Statement:
"The paper does not discuss the computational cost of HICRA in detail, which is an important consideration for practical applications. The authors should provide more information on the training time and memory requirements of HICRA compared to standard RL baselines."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions using the same training implementation details as the baselines.
   - The paper does not provide specific details on training time or memory requirements for HICRA.

4. Validation Analysis:
   - The paper lacks a detailed discussion of the computational cost of HICRA.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper does not provide details on training time and memory requirements for HICRA.

**Review 3 Weaknesses:**

1. Weakness Statement:
"The paper could benefit from a more detailed discussion of the limitations of the proposed approach, particularly in scenarios where the identified strategic planning tokens may not be readily available or easily defined."

2. Evidence Collection:
   - The paper defines strategic planning tokens based on a functional proxy.
   - The paper does not explicitly discuss scenarios where this definition might be problematic or where strategic planning tokens are not easily defined.

4. Validation Analysis:
   - The paper lacks a detailed discussion of the limitations related to the definition and availability of strategic planning tokens.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks a detailed discussion of limitations related to the definition of strategic planning tokens.

1. Weakness Statement:
"The paper could provide more insights into the computational overhead of HICRA compared to standard RL algorithms."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions using the same training implementation details as the baselines.
   - The paper does not provide specific details on the computational overhead of HICRA.

4. Validation Analysis:
   - The paper lacks a detailed discussion of the computational overhead of HICRA.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper does not provide details on the computational overhead of HICRA.

1. Weakness Statement:
"The paper could benefit from a more thorough discussion of the sensitivity of HICRA to the choice of hyperparameters, particularly the hyperparameter α in the HICRA algorithm."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions using α = 0.2 in the experiments.
   - The paper does not include a sensitivity analysis of the hyperparameter α.

4. Validation Analysis:
   - The paper lacks a thorough discussion of the sensitivity of HICRA to the hyperparameter α.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper does not include a sensitivity analysis of the hyperparameter α.

**Review 4 Weaknesses:**

1. Weakness Statement:
"The main concern is the novelty of the proposed method. It seems that the proposed method is an application of existing methods to the reasoning task. The proposed method is not a general method for RLHF and can only be applied to reasoning tasks. Specifically, the method relies on identifying "strategic planning tokens" which are task-specific and require manual annotation or sophisticated analysis, limiting its general applicability. The core idea of focusing optimization pressure on specific tokens, while effective for reasoning, lacks a broader theoretical foundation and may not translate well to other RLHF scenarios where such token-level control is not feasible."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper introduces HICRA as a novel algorithm.
   - The paper defines strategic planning tokens based on a functional proxy, which is task-specific.
   - The paper does not claim that HICRA is a general RLHF method applicable to all tasks.

4. Validation Analysis:
   - The reviewer's concern about novelty is subjective. However, the point about the task-specificity of strategic planning tokens and the limited theoretical foundation is valid.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The method relies on task-specific strategic planning tokens, and the theoretical foundation is primarily within the context of reasoning.

1. Weakness Statement:
"The authors claim that the proposed method can be applied to VLMs, but there is no experiment to support this. The paper lacks a detailed explanation of how the proposed method would be adapted to VLMs, particularly concerning the handling of visual tokens and the integration of visual information into the RL training loop. The absence of empirical validation on VLMs is a significant gap, especially given the authors' claim of broad applicability."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper includes experiments on VLMs.
   - The paper does not provide a detailed explanation of how visual tokens are handled within HICRA.

4. Validation Analysis:
   - The reviewer's claim about the lack of VLM experiments is incorrect. However, the lack of detail on handling visual tokens is a valid point.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: Experiments on VLMs are present, but details on handling visual tokens are missing.

1. Weakness Statement:
"What is the definition of the strategic planning tokens? Can it be applied to other tasks?"

2. Evidence Collection:
a) Method-related Evidence:
   - The paper defines strategic planning tokens based on a functional proxy.
   - The paper does not explicitly state if this definition can be applied to other tasks.

4. Validation Analysis:
   - The definition is provided, but the generalizability to other tasks is not discussed.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The definition is provided, but generalizability is not discussed.

1. Weakness Statement:
"Can the proposed method be applied to VLMs?"

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper includes experiments on VLMs.

4. Validation Analysis:
   - The paper provides experimental evidence of applying HICRA to VLMs.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: Experiments on VLMs are included.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces Hierarchy-Aware Credit Assignment (HICRA), a novel reinforcement learning from human feedback (RLHF) algorithm designed to enhance the reasoning abilities of large language models (LLMs). The authors propose that the learning process for LLMs involves a two-phase dynamic: an initial phase focused on procedural correctness, where the model masters low-level skills such as accurate calculations, and a subsequent phase focused on strategic planning, where the model learns to develop higher-level reasoning strategies. HICRA leverages this insight by prioritizing the learning of planning tokens, which are identified using a functional proxy—a set of n-grams that function as a single semantic unit to guide the logical flow of the reasoning process. The core mechanism of HICRA involves modifying the advantage function in the Generalized Proximal Policy Optimization (GRPO) algorithm, amplifying the learning signal for planning tokens to encourage exploration of more complex reasoning strategies. The authors validate HICRA through extensive experiments across various models, including text-only and vision-language models, and demonstrate that it outperforms standard RL baselines and other credit assignment methods. The empirical results show that HICRA leads to improved performance on reasoning tasks, and the authors provide detailed analysis of the learning dynamics, including token-level entropy and semantic entropy, which offer valuable insights into how HICRA improves reasoning abilities. The paper's main contribution lies in its novel perspective on the learning dynamics of LLMs during RL training, identifying a hierarchical structure in reasoning, and proposing a targeted credit assignment method that aligns with this structure. The authors also provide a clear explanation of how HICRA modifies the GRPO algorithm and how it can be applied to different types of models and tasks. Overall, this work presents a significant step towards understanding and improving the reasoning capabilities of LLMs through a more targeted and efficient RL training approach.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

2.5


## Strengths:

I find several aspects of this paper to be particularly strong. First, the paper's core contribution lies in its novel perspective on the learning dynamics of LLMs during RL training. The authors' identification of a hierarchical structure in reasoning, with distinct phases for procedural correctness and strategic planning, is a significant contribution to the field. This hierarchical view provides a valuable framework for understanding how LLMs develop reasoning abilities and offers a new direction for improving their performance. Second, the proposed HICRA algorithm is well-motivated and builds upon existing RL methods, specifically GRPO, in a clear and logical manner. The modification of the advantage function to prioritize planning tokens is a key innovation, and the authors provide a detailed explanation of how this modification is implemented. The paper also includes extensive experimental results across various models and reasoning tasks, which demonstrate the effectiveness of HICRA over standard RL baselines. The authors' analysis of the learning dynamics, including token-level entropy and semantic entropy, provides valuable insights into how HICRA improves reasoning abilities. The paper is also well-written and organized, with clear explanations of the proposed method and experimental setup. The authors also provide a comprehensive discussion of related work and limitations, which helps to contextualize their contributions within the broader field of LLM research. Finally, the paper's focus on a practical and implementable method, HICRA, makes it a valuable contribution to the field. The authors have successfully translated their theoretical insights into a concrete algorithm that can be readily applied to existing LLMs, which is a significant strength of this work.


## Weaknesses:

Despite its strengths, I have identified several weaknesses in this paper that warrant further discussion. First, while the paper defines strategic planning tokens and the method for their identification, the explanation could be more detailed for easier reproduction. The paper states that these tokens are identified using a functional proxy, which is a set of n-grams that function as a single semantic unit, and that this identification is based on the frequency of the n-grams in the corpus and the semantic similarity between them. However, the paper lacks a concrete algorithm or a more detailed explanation of how this identification process is implemented. This lack of clarity makes it difficult to fully understand the proposed method and to reproduce the results. My confidence in this weakness is medium, as the paper does provide a definition and a high-level description, but lacks the necessary detail for full reproducibility. Second, the paper does not provide a clear explanation of how the proposed method is applied to models with different architectures, such as encoder-decoder models or decoder-only models. While the paper shows experiments on different architectures, it doesn't explain how HICRA adapts to these differences. The core idea of focusing on planning tokens should be applicable, but the implementation details might vary. This lack of explanation makes it difficult to understand the generalizability of the method. My confidence in this weakness is medium, as the paper shows experiments on different architectures, but doesn't explain the adaptation of HICRA. Third, the paper lacks a detailed discussion of the limitations of the proposed approach, particularly in scenarios where the identified strategic planning tokens may not be readily available or easily defined. The paper defines strategic planning tokens based on a functional proxy, which is task-specific. This reliance on task-specific tokens limits the general applicability of the method. The paper does not discuss scenarios where this definition might be problematic or where strategic planning tokens are not easily defined. My confidence in this weakness is high, as the paper lacks a detailed discussion of limitations related to the definition of strategic planning tokens. Fourth, the paper does not provide a thorough comparison with other state-of-the-art RL methods for LLMs, particularly those that also focus on improving reasoning abilities. The paper compares HICRA with the base model, GRPO, and Entropy Regularization. While these are relevant baselines, the paper could benefit from a more comprehensive comparison with other state-of-the-art RL methods specifically designed for improving reasoning in LLMs. This lack of comparison makes it difficult to position HICRA within the existing literature and highlight its unique contributions. My confidence in this weakness is high, as the experimental section lacks comparison with a broader range of state-of-the-art reasoning-focused RL methods. Fifth, the paper does not discuss the computational cost of HICRA in detail. The paper mentions using the same training implementation details as the baselines, but it does not provide specific details on the training time or memory requirements for HICRA compared to standard RL baselines. This lack of information is a significant consideration for practical applications. My confidence in this weakness is high, as the paper does not provide details on the computational overhead of HICRA. Sixth, the paper could benefit from a more thorough discussion of the sensitivity of HICRA to the choice of hyperparameters, particularly the hyperparameter α in the HICRA algorithm. The paper mentions using α = 0.2 in the experiments, but it does not include a sensitivity analysis of the hyperparameter α. This lack of analysis makes it difficult to understand the robustness and performance of HICRA under different hyperparameter settings. My confidence in this weakness is high, as the paper does not include a sensitivity analysis of the hyperparameter α. Finally, while the paper includes experiments on VLMs, it lacks a detailed explanation of how visual tokens are handled within HICRA. The paper assumes that the functional proxy, which is based on textual n-grams, can be applied to the textual component of the VLMs. However, it's unclear if the visual tokens are treated as a separate set or integrated into the textual processing. This lack of detail makes it difficult to understand how HICRA is applied to VLMs. My confidence in this weakness is medium, as the paper mentions VLM experiments and the use of the same functional proxy, but lacks details on the treatment of visual tokens.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the paper should provide a more precise definition of what constitutes a 'strategic token' and a 'procedural token.' The current description is vague and does not provide a clear understanding of how these tokens are identified. For example, are these tokens defined based on their frequency in a corpus, their semantic meaning, or some other criteria? The paper should also provide a concrete example of how these tokens are identified in a given text. Furthermore, the paper should clarify how the proposed method differs from existing RLHF algorithms. It is not sufficient to simply state that the proposed method is designed to focus optimization pressure on high-level planning tokens. The paper should provide a detailed explanation of the specific modifications made to the RL algorithm and how these modifications lead to the observed improvements. For example, how does the HICRA algorithm modify the reward function or the policy update rule compared to standard RL algorithms like PPO or REINFORCE? A more detailed explanation of these differences is needed to understand the novelty of the proposed method. Second, the paper should provide a more detailed explanation of how the proposed method is applied to vision-language models. The current description is too brief and does not provide a clear understanding of how the visual tokens are treated. For example, are the visual tokens treated as a separate set of tokens, or are they integrated into the textual tokens? How does the proposed method handle the differences in the visual and textual modalities? The paper should also provide a more detailed explanation of how the visual tokens are treated. For example, are the visual tokens treated as a separate set of tokens or are they integrated into the textual tokens? How does the proposed method handle the differences in the visual and textual modalities? The paper should also provide a more detailed explanation of how the proposed method is applied to models with different architectures, such as encoder-decoder models or decoder-only models. The paper should explain how the proposed method is adapted to different model architectures and how the strategic and procedural tokens are identified in these models. For example, in encoder-decoder models, how are the tokens identified as strategic or procedural, given that there is no explicit decoder? The paper should also discuss the challenges of applying HICRA to models with different sizes and training datasets. The paper should explain how the proposed method is adapted to different datasets and how the strategic and procedural tokens are identified in these datasets. For example, does the number of strategic tokens change with model size? Finally, the paper should provide a more detailed analysis of the computational cost of HICRA compared to standard RL baselines. The authors should provide more information on the training time and memory requirements of HICRA compared to standard RL baselines. This information is crucial for practical applications and would help to assess the feasibility of using HICRA in real-world scenarios. The authors should also consider comparing the performance of HICRA with other state-of-the-art RL methods for LLMs, particularly those that also focus on improving reasoning abilities. This comparison should include a detailed analysis of the strengths and weaknesses of each method, as well as a discussion of the trade-offs between different approaches. This would help to position HICRA within the broader context of RLHF research and highlight its unique contributions. Finally, the paper should include a more thorough discussion of the sensitivity of HICRA to the choice of hyperparameters, particularly the hyperparameter α. The authors should conduct a systematic study of how different values of α affect the performance of HICRA across various tasks and datasets. This study should include not only the final performance metrics but also the learning curves and the convergence behavior of the algorithm. The paper should also discuss the potential for adaptive hyperparameter tuning, which could further improve the robustness and performance of HICRA. A more detailed analysis of these limitations would provide valuable insights into the practical application of the proposed method and would help users to effectively tune the hyperparameters for their specific use cases.


## Questions:

I have several questions that arise from my analysis of this paper. First, how does HICRA perform in scenarios where the definition of strategic planning tokens is ambiguous or unavailable? The paper's reliance on a functional proxy, which is task-specific, raises concerns about its applicability in situations where this proxy cannot be easily defined or where the task is too novel. Second, what is the computational overhead of HICRA compared to standard RL baselines? The paper mentions using the same training implementation details as the baselines, but it does not provide specific details on the training time or memory requirements for HICRA. This lack of information makes it difficult to assess the practical feasibility of the method. Third, how sensitive is HICRA to the choice of hyperparameters, particularly the hyperparameter α? The paper mentions using α = 0.2 in the experiments, but it does not include a sensitivity analysis of the hyperparameter α. This lack of analysis makes it difficult to understand the robustness and performance of HICRA under different hyperparameter settings. Fourth, how are the visual tokens treated in vision-language models? The paper mentions experiments on VLMs, but it lacks a detailed explanation of how visual tokens are handled within HICRA. It's unclear if the visual tokens are treated as a separate set of tokens or are integrated into the textual processing. Fifth, how does HICRA perform on multi-modal reasoning tasks that require logical inference based on symbolic representations? The paper includes experiments on VLMs, which involve multi-modal reasoning, but it does not explicitly discuss how HICRA performs on tasks that require logical reasoning based on symbolic representations. Finally, how does the performance of HICRA vary across different types of reasoning tasks, such as multi-modal reasoning or logical reasoning tasks that require symbolic manipulation? The paper includes experiments on VLMs, which involve multi-modal reasoning, but it does not explicitly discuss how HICRA performs on tasks that require logical reasoning based on symbolic representations. These questions target key uncertainties in the paper's methodology and assumptions, and seeking clarification on these points would further strengthen the paper's contributions.


## Rating:

6.25


## Confidence:

3.0


## Decision:

Reject
}