I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper proposes a new method for inter-LLM communication, i.e., the activation communication. The authors communicate via activations, which scales up LLMs on new tasks with zero additional parameters and data. The authors also formally quantify the compute savings over natural language communication. The authors also conduct comprehensive experiments to validate the effectiveness of the proposed method.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The proposed method is simple and effective.
2. The authors conduct comprehensive experiments to validate the effectiveness of the proposed method.
3. The authors also formally quantify the compute savings over natural language communication.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of the proposed method is limited. The proposed method is similar to CIPHER (Pham et al., 2024), which communicates the average tokenizer embedding (weighted by the LLM’s next-token probabilities) between models. The authors should discuss the differences between the proposed method and CIPHER.
2. The authors should conduct experiments on larger models, e.g., 70B models.
3. The authors should conduct experiments on more reasoning benchmarks, e.g., MMLU.

### Suggestions

The paper introduces activation communication as a method for inter-LLM communication, which is an interesting approach. However, the paper needs to more clearly differentiate itself from existing methods, particularly CIPHER. While the authors mention that CIPHER uses average tokenizer embeddings, the practical implications of this difference are not fully explored. For instance, how does the proposed method's reliance on specific activation layers affect its robustness and generalizability compared to CIPHER's embedding-based approach? A more detailed analysis of the trade-offs between these approaches, including computational cost and communication efficiency, would be beneficial. Furthermore, the paper should investigate the sensitivity of the proposed method to the choice of activation layers and provide guidelines for selecting optimal layers for different tasks. This would help to establish the practical applicability of the method and provide a more comprehensive understanding of its strengths and limitations.

To strengthen the empirical validation, the authors should conduct experiments on a wider range of model sizes and reasoning benchmarks. While the current experiments provide some evidence of the method's effectiveness, the lack of results on larger models, such as 70B models, raises concerns about its scalability. It is crucial to demonstrate that the proposed method can maintain its performance gains as model size increases, as this is a critical factor for real-world applications. Additionally, expanding the evaluation to include more comprehensive reasoning benchmarks, such as the full MMLU dataset, would provide a more robust assessment of the method's capabilities. The current evaluation is limited in scope and does not fully capture the potential of the proposed method. The authors should also consider evaluating the method on tasks that require more complex reasoning and multi-turn interactions to fully demonstrate its effectiveness.

Finally, the paper should provide a more detailed analysis of the computational overhead associated with activation communication. While the authors mention compute savings, a more precise quantification of the computational cost, including memory usage and inference time, would be valuable. This analysis should also consider the impact of different activation layers and model sizes on the computational overhead. Furthermore, the authors should explore potential optimizations to reduce the computational cost of activation communication, such as model compression or quantization techniques. This would make the method more practical for real-world applications and allow for a more comprehensive comparison with other inter-LLM communication methods. A thorough analysis of these aspects would significantly enhance the paper's contribution and practical relevance.

### Questions

See above.

### Rating

5

### Confidence

4

**********

## Reviewer 2

### Summary

The paper proposes a method for inter-model communication that leverages intermediate activations instead of natural language. The authors demonstrate that this approach can achieve up to 27.0% improvement over natural language communication across various datasets with fewer compute resources.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.

- The proposed method is simple and straightforward, yet it achieves significant improvements over natural language communication.

- The authors provide a detailed analysis of the computational costs associated with their method, demonstrating its efficiency.

- The authors conduct comprehensive experiments across multiple datasets, showcasing the robustness and generalizability of their approach.

### Weaknesses

#### Some Related Works


#### comment

 - The authors should provide a more comprehensive comparison with existing methods, such as natural language communication and other activation-based approaches, to better demonstrate the advantages of their method.

- The authors should provide more details on the experimental setup, including the specific models used, the hyperparameters, and the evaluation metrics. This would help to ensure the reproducibility of their results.

- The authors should discuss the limitations of their method and potential directions for future research. For example, how does the method perform on tasks that require more complex reasoning or multi-turn interactions? What are the potential challenges in scaling the method to larger models or more diverse datasets?

### Suggestions

The paper would benefit from a more rigorous comparison against existing inter-model communication techniques. While the authors compare against natural language communication, a more thorough analysis should include comparisons with other activation-based methods, if any exist, or at least a detailed discussion of why such comparisons are not feasible. For instance, if other methods exist, a comparison should include a table that shows the performance of each method across different datasets, along with a discussion of the computational costs and the specific scenarios where each method excels. This would provide a more complete picture of the advantages and disadvantages of the proposed method. Furthermore, the authors should clarify the specific types of tasks where their method is expected to perform best and where it might struggle. This would help the reader understand the scope and limitations of the proposed approach.

To enhance the reproducibility of the results, the authors should provide a detailed description of the experimental setup. This should include the specific models used for each task, the hyperparameters used for training and evaluation, and the exact evaluation metrics used. For example, if the models are Llama models, the specific version and size should be mentioned. The authors should also specify the optimization algorithm used, the learning rate, and any other relevant training details. Furthermore, the authors should provide the code and the data used in the experiments to allow other researchers to reproduce their results. This would increase the credibility of the paper and allow other researchers to build upon their work. The authors should also discuss the sensitivity of their method to different hyperparameters and provide guidelines for selecting the optimal hyperparameters for different tasks.

Finally, the authors should discuss the limitations of their method and potential directions for future research. This should include a discussion of the potential challenges in scaling the method to larger models or more diverse datasets. For example, the authors should discuss the computational cost of extracting and processing activations from larger models and how this might affect the scalability of their method. The authors should also discuss the potential challenges in applying their method to tasks that require more complex reasoning or multi-turn interactions. This would help the reader understand the scope and limitations of the proposed approach and identify potential areas for future research. The authors should also discuss the potential ethical implications of their method, such as the potential for bias or misuse.

### Questions

- How does the proposed method perform on tasks that require more complex reasoning or multi-turn interactions?

- What are the potential challenges in scaling the method to larger models or more diverse datasets?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper introduces a novel approach to inter-model communication that leverages activations instead of natural language. The authors propose a method where one model communicates via activations to another, which can then use these activations to enhance its own computation. This approach scales up LLMs on new tasks with zero additional parameters and data, and saves a substantial amount of compute. The authors validate their method through comprehensive experiments on multi-player coordination games and reasoning benchmarks, demonstrating up to 27.0% improvement over natural language communication across datasets with < 1/4 the compute.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper introduces a novel approach to inter-model communication that leverages activations instead of natural language, which is a fresh perspective on how to communicate between LLMs.
- The authors provide a formal analysis of the compute savings over natural language communication, which is a valuable contribution.
- The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the limitations of the proposed method, such as the potential for information loss or the impact of model size on performance.
- The paper does not compare the proposed method with other state-of-the-art methods for inter-model communication, such as multi-agent debate or collaborative reasoning.
- The paper does not discuss the potential ethical implications of the proposed method, such as the potential for bias or misuse.

### Suggestions

The paper would benefit from a more thorough investigation into the limitations of the activation-based communication method. Specifically, the authors should explore the potential for information loss during the activation transfer process. This could involve analyzing the rank of the activation matrices or examining the information content of the transferred activations using techniques like singular value decomposition. Furthermore, the impact of model size on the effectiveness of the proposed method should be investigated. It would be valuable to see experiments with models of varying sizes to understand how the communication performance scales with model capacity. This analysis should also consider the computational cost associated with extracting and processing activations, especially for larger models. A detailed analysis of these limitations would provide a more complete picture of the method's applicability and potential drawbacks.

To strengthen the paper, the authors should include a more comprehensive comparison with existing inter-model communication techniques. While the paper mentions multi-agent debate and collaborative reasoning, it lacks a detailed empirical comparison. The authors should implement and evaluate these methods on the same datasets used in their experiments to provide a more robust assessment of the proposed method's advantages and disadvantages. This comparison should not only focus on performance metrics but also consider computational cost and communication overhead. Furthermore, the authors should explore the potential of combining their method with other communication techniques to achieve even better performance. For example, they could investigate whether the proposed method can be used in conjunction with multi-agent debate to further improve reasoning capabilities. Such an analysis would provide a more nuanced understanding of the method's potential and its place within the broader landscape of inter-model communication.

Finally, the paper should address the potential ethical implications of the proposed method. The authors should discuss the potential for bias in the transferred activations and how this could be mitigated. They should also consider the potential for misuse of the method, such as in adversarial settings. A discussion of these ethical considerations would add a valuable dimension to the paper and demonstrate a responsible approach to research. This discussion should also consider the potential for the method to be used in sensitive applications, such as those involving personal data or sensitive decision-making. By addressing these ethical concerns, the authors can enhance the credibility and impact of their work.

### Questions

- How does the proposed method perform with different model architectures and sizes?
- How does the proposed method compare to other state-of-the-art methods for inter-model communication, such as multi-agent debate or collaborative reasoning?
- What are the potential ethical implications of the proposed method, and how can they be addressed?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

The paper presents a novel approach to inter-model communication in large language models (LLMs) by leveraging activations instead of natural language. This method enables more efficient and effective communication between LLMs, scaling up the models on new tasks with zero additional parameters and data. The authors demonstrate that this activation-based communication can achieve up to 27.0% improvement over natural language communication across various datasets, using fewer compute resources. The paper also provides a formal analysis of the compute savings over natural language communication, highlighting the potential of activations as an alternative to natural language for inter-model communication.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach to inter-model communication that leverages activations instead of natural language, which is a fresh perspective on how to communicate between LLMs.
2. The authors provide a formal analysis of the compute savings over natural language communication, which is a valuable contribution.
3. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the limitations of the proposed method, such as the potential for information loss or the impact of model size on performance.
2. The paper does not compare the proposed method with other state-of-the-art methods for inter-model communication, such as multi-agent debate or collaborative reasoning.
3. The paper does not discuss the potential ethical implications of the proposed method, such as the potential for bias or misuse.

### Suggestions

The paper would benefit from a more thorough investigation into the limitations of the activation-based communication method. Specifically, the authors should explore the potential for information loss during the activation transfer process. This could involve analyzing the rank of the activation matrices or examining the information content of the transferred activations using techniques like singular value decomposition. Furthermore, the impact of model size on the effectiveness of the proposed method should be investigated. It would be valuable to see experiments with models of varying sizes to understand how the communication performance scales with model capacity. This analysis should also consider the computational cost associated with extracting and processing activations, especially for larger models. A detailed analysis of these limitations would provide a more complete picture of the method's applicability and potential drawbacks.

To strengthen the paper, the authors should include a more comprehensive comparison with existing inter-model communication techniques. While the paper mentions multi-agent debate and collaborative reasoning, it lacks a detailed empirical comparison. The authors should implement and evaluate these methods on the same datasets used in their experiments to provide a more robust assessment of the proposed method's advantages and disadvantages. This comparison should not only focus on performance metrics but also consider computational cost and communication overhead. Furthermore, the authors should explore the potential of combining their method with other communication techniques to achieve even better performance. For example, they could investigate whether the proposed method can be used in conjunction with multi-agent debate to further improve reasoning capabilities. Such an analysis would provide a more nuanced understanding of the method's potential and its place within the broader landscape of inter-model communication.

Finally, the paper should address the potential ethical implications of the proposed method. The authors should discuss the potential for bias in the transferred activations and how this could be mitigated. They should also consider the potential for misuse of the method, such as in adversarial settings. A discussion of these ethical considerations would add a valuable dimension to the paper and demonstrate a responsible approach to research. This discussion should also consider the potential for the method to be used in sensitive applications, such as those involving personal data or sensitive decision-making. By addressing these ethical concerns, the authors can enhance the credibility and impact of their work.

### Questions

1. How does the proposed method perform with different model architectures and sizes?
2. How does the proposed method compare to other state-of-the-art methods for inter-model communication, such as multi-agent debate or collaborative reasoning?
3. What are the potential ethical implications of the proposed method, and how can they be addressed?

### Rating

8

### Confidence

2

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in the provided paper. I need to go through each reviewer's comments and check if their criticisms are valid based on the content of the paper.

**Plan:**
1. Go through each reviewer's comments one by one.
2. For each weakness identified by the reviewer, find evidence in the paper to support or refute the claim.
3. Categorize the weakness (theoretical, methodological, experimental, practical).
4. Provide direct quotes and section references as evidence.
5. Conclude whether the weakness is valid, partially valid, or invalid, and provide a confidence level.
**Review 1 Weaknesses:**

1. Weakness Statement:
[The paper does not provide a detailed analysis of the limitations of the proposed method, such as the potential for information loss or the impact of model size on performance.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions the assumption of aligned embeddings: "First, when not using the learned model-specific mapping discussed in Section 3.1 , our method requires both models to have aligned embedding spaces, such that the activation of one model roughly retains its meaning in the other’s activation space (note that unlike past works such as Pham et al. (2024) we do not require shared tokenizers or aligned vocabularies, only aligned embeddings)." (Section 3.3)
   - The paper acknowledges the need for a mapping function when embeddings are not aligned: "In practice, we find that 𝑊 can be learned using a task-agnostic (depends only on the models A and B ) linear layer that projects 𝑎 to B ’s activation space. Note that this introduces zero additional task-specific parameters and data, as we propose learning this “mapping matrix” 𝑊 only once for each model pair ( A , B ) (A,B) using general text, e.g. sequences from A A and/or B B ’s pretraining data mixes." (Section 3.3)
b) Experiment-related Evidence:
   - The paper tests on different model sizes (3B and 8B LLaMA models) in the reasoning benchmarks experiment (Table 3).
   - The paper notes the performance difference based on the mapping function: "Based on these results (shown in Figure 2 ) as well as Table 2 , we fix k = j = 26 and f f = = 𝑟𝑒𝑠𝑡𝑙𝑜𝑐𝑎𝑙𝑑𝑒 𝑚𝑎𝑡𝑐ℎ𝑖𝑛𝑔 of 𝐴 to B B , we see even further gains of 2.6 − 50.0 % over vanilla AC for four of the seven datasets." (Section 4.2) and "While we fix A A as the smaller model and B B as the larger model in Table 3 (so as to ensure decoding happens with the presumably more capable model), this need not be the case; swapping A A and B B yields results of 81.5 ± 0.0 and 61.0 ± 4.8 on Biographies and GSM8k respectively (without the linear layer)." (Section 4.2)

3. Literature Gap Analysis:
   - The paper cites Pham et al. (2024) and discusses the difference in embedding alignment.

4. Validation Analysis:
   - The paper acknowledges the requirement of aligned embedding spaces and the need for a mapping function when they are not aligned. This implicitly addresses the potential for information loss.
   - The experiments with different model sizes provide some insight into the impact of model size on performance.
   - The paper does not explicitly analyze the *degree* of information loss or provide a detailed theoretical analysis of the limitations beyond the requirement of aligned embeddings.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper mentions the requirement of aligned embeddings and the use of a mapping function. It also tests on different model sizes. However, a deeper analysis of information loss is missing.

1. Weakness Statement:
[The paper does not compare the proposed method with other state-of-the-art methods for inter-model communication, such as multi-agent debate or collaborative reasoning.]

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper explicitly compares against "Single Model" and "Natural Language Debate (NL)" in the experiments (Sections 4.1 and 4.2).
   - The paper mentions multi-agent debate in the related work: "Multi-agent debate introduced by Du et al. (2023)..." (Section 2)

3. Literature Gap Analysis:
   - The paper cites Du et al. (2023) for multi-agent debate.

4. Validation Analysis:
   - The paper *does* compare against a form of multi-agent communication (natural language debate).
   - However, it does not include a direct experimental comparison with the specific implementation of multi-agent debate by Du et al. (2023) or other methods focused on collaborative reasoning.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper compares against natural language debate. However, it lacks a direct experimental comparison with other state-of-the-art methods like the specific multi-agent debate framework.

1. Weakness Statement:
[The paper does not discuss the potential ethical implications of the proposed method, such as the potential for bias or misuse.]

2. Evidence Collection:
   - A search for "ethical" or "bias" within the paper yields no results.

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - The paper does not include a section or discussion on the ethical implications of the proposed method.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks any discussion on ethical implications.

**Review 2 Weaknesses:**

1. Weakness Statement:
[The novelty of the proposed method is limited. The proposed method is similar to CIPHER (Pham et al., 2024), which communicates the average tokenizer embedding (weighted by the LLM’s next-token probabilities) between models. The authors should discuss the differences between the proposed method and CIPHER.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions CIPHER in the related work: "A related class of methods involves spending extra test-time compute reasoning in latent space ( Geiping et al., 2025 ; Hao et al., 2024 ) . Such latent reasoning approaches involving doing ”chain-of-thought in activation space,” e.g. by grafting LM activations into other layers/later forward passes through the same model (e.g., a form of “recurrent AC” within a single model); our approach can be viewed as doing exactly the same thing, but instead ”outsourcing” the CoT to another model (and thus reaping benefits from greater diversity of thoughts/reasoning paths from distinct models)." (Section 2)
   - The paper distinguishes itself by communicating activations, not just embeddings: "In contrast, CIPHER and activation communication solve this problem, as some notion of model confidence is being communicated along with its next-token prediction (over the entire vocabulary)." (Section 3.3)
   - The paper explicitly states the difference in the function used for communication: "Communicating activations, then, can be thought of as communicating a strict superset of {next-token prediction, belief over entire vocabulary}, as activations of late-enough layers essentially encode the model’s entire knowledge about the provided context as well as its predicted completion and confidence in that completion (see Figures 1 and 7 in Hewitt & Manning (2019) and Hernandez et al. (2024) , respectively, which show that linear probes tasked with predicting certain output characteristics from a Transformer’s intermediate layer embeddings of its input work poorly for early layers, extremely well after around the halfway point of computation, but then probe accuracy drops closer to the final layers). 2 2 2 Note one important critique of multiagent debate: that in cases where multiple agents are uncertain about the answer, there is no reason why referencing other agents’ answers would generate more factual reasoning. Both CIPHER and activation communication solve this problem, as some notion of model confidence is being communicated along with its next-token prediction." (Section 3.3)

3. Literature Gap Analysis:
   - The paper cites Pham et al. (2024) (CIPHER).

4. Validation Analysis:
   - The paper acknowledges the existence of CIPHER and other latent space methods.
   - The paper explicitly discusses the difference in communicating activations versus embeddings and argues that activations contain more information relevant to reasoning.
   - While the paper mentions CIPHER, it could further elaborate on the specific differences in implementation and communication strategy.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper discusses CIPHER and highlights the difference in communication type (activations vs. embeddings). However, a more detailed comparison of the implementation and communication strategies could be beneficial.

1. Weakness Statement:
[The authors should conduct experiments on larger models, e.g., 70B models.]

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper's largest model used is 8B parameters (LLaMA 3.1).
   - The paper mentions testing on models from the LLaMA family (3.2 and 3.1) (Section 4.1).

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - The paper's experiments are limited to models up to 8B parameters.
   - Testing on larger models like 70B would provide further evidence of scalability.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper does not include experiments on models larger than 8B parameters.

1. Weakness Statement:
[The authors should conduct experiments on more reasoning benchmarks, e.g., MMLU.]

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper uses Biographies, GSM8k, 5 datasets from MMLU, and High School Psychology as reasoning benchmarks (Section 4.2).
   - The paper explicitly mentions using a subset of MMLU: "In experiments involving the mapping matrix 𝑊 , we instantiate 𝑊 ∈ ℝ 4096 × 3072 using Xavier initialization and train for 10 10 epochs on a dataset of 3072 3072 sentences 3 3 3 We use batch size 32 32 and the Adam optimizer with learning rate 0.001 0.001 ." (Section 4.2)

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - The paper uses a subset of MMLU, which is a standard benchmark.
   - While more datasets from MMLU could be included, the current selection is reasonable.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper uses a subset of MMLU. While more datasets could strengthen the evaluation, the current selection is not entirely lacking.

**Review 3 Weaknesses:**

1. Weakness Statement:
[- The paper does not provide a detailed analysis of the limitations of the proposed method, such as the potential for information loss or the impact of model size on performance.]

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's first point. Please see the analysis for that point.

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - Same as Reviewer 1's first point.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper mentions the requirement of aligned embeddings and the use of a mapping function. It also tests on different model sizes. However, a deeper analysis of information loss is missing.

1. Weakness Statement:
[- The paper does not compare the proposed method with other state-of-the-art methods for inter-model communication, such as multi-agent debate or collaborative reasoning.]

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's second point. Please see the analysis for that point.

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - Same as Reviewer 1's second point.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper compares against natural language debate. However, it lacks a direct experimental comparison with other state-of-the-art methods like the specific implementation of multi-agent debate.

1. Weakness Statement:
[- The paper does not discuss the potential ethical implications of the proposed method, such as the potential for bias or misuse.]

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's third point. Please see the analysis for that point.

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - Same as Reviewer 1's third point.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks any discussion on ethical implications.

**Review 4 Weaknesses:**

1. Weakness Statement:
[- The authors should provide a more comprehensive comparison with existing methods, such as natural language communication and other activation-based approaches, to better demonstrate the advantages of their method.]

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper compares against "Single Model" and "Natural Language Debate (NL)" (Sections 4.1 and 4.2).
   - The paper mentions activation-based methods in the related work: "A related class of methods involves spending extra test-time compute reasoning in latent space ( Geiping et al., 2025 ; Hao et al., 2024 ) ." (Section 2)

3. Literature Gap Analysis:
   - The paper cites Geiping et al. (2025) and Hao et al. (2024) as examples of latent space methods.

4. Validation Analysis:
   - The paper does compare against natural language communication.
   - The paper acknowledges the existence of other activation-based methods but doesn't provide a direct experimental comparison.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper compares against natural language debate. However, it lacks a direct experimental comparison with other activation-based methods.

1. Weakness Statement:
[- The authors should provide more details on the experimental setup, including the specific models used, the hyperparameters, and the evaluation metrics. This would help to ensure the reproducibility of their results.]

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions using LLaMA models (3.2 and 3.1) (Section 4.1).
   - The paper mentions using the Adam optimizer with a learning rate of 0.001 (Section 4.2).
   - The paper mentions using batch size 32 (Section 4.2).
   - The paper defines the evaluation metrics (accuracy for reasoning tasks, exact string match for multi-player coordination games) (Section 4.1).
   - The paper mentions using Xavier initialization for the mapping matrix (Section 4.2).

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - The paper provides details about the models, optimizer, learning rate, batch size, and evaluation metrics.
   - However, specific hyperparameters for the activation replacement function (e.g., the function itself, any associated parameters) are not explicitly stated.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper provides some experimental details but lacks specific hyperparameters for the activation replacement function.

1. Weakness Statement:
[- The authors should discuss the limitations of their method and potential directions for future research. For example, how does the method perform on tasks that require more complex reasoning or multi-turn interactions? What are the potential challenges in scaling the method to larger models or more diverse datasets?]

2. Evidence Collection:
   - The paper briefly mentions limitations in the conclusion: "While we fix A A as the smaller model and B B as the larger model in Table 3 (so as to ensure decoding happens with the presumably more capable model), this need not be the case; swapping A A and B B yields results of 81.5 ± 0.0 and 61.0 ± 4.8 on Biographies and GSM8k respectively (without the linear layer)." (Section 4.2) and "While we fix k = j = 26 and f f = = 𝑟𝑒𝑠𝑡𝑙𝑜𝑐𝑎𝑙𝑑𝑒 𝑚𝑎𝑡𝑐ℎ𝑖𝑛𝑔 of 𝐴 to B B , we see even further gains of 2.6 − 50.0 % over vanilla AC for four of the seven datasets." (Section 4.2).
   - The paper suggests future work: "There are some limitations to this method. First, when not using the learned model-specific mapping discussed in Section 3.1 , our method requires both models to have aligned embedding spaces, such that the activation of one model roughly retains its meaning in the other’s activation space (note that unlike past works such as Pham et al. (2024) we do not require shared tokenizers or aligned vocabularies, only aligned embeddings)." (Section 4.3) and "Second, this method requires access to embeddings and will not work with black-box API access; however exploring API-only approaches is highly limiting, and recent releases of powerful open-source models ( Dubey et al., 2024 ) merit the development of embedding-based techniques." (Section 4.3).

3. Literature Gap Analysis:
   - N/A

4. Validation Analysis:
   - The paper briefly touches upon some limitations and suggests future research directions.
   - However, it doesn't explicitly discuss performance on complex reasoning or multi-turn interactions, or the challenges of scaling to larger models or more diverse datasets in detail.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper mentions some limitations and future work, but lacks a detailed discussion on performance on complex tasks, multi-turn interactions, and scaling challenges.

**Synthesis and Reflection:**

After analyzing the reviewers' comments and comparing them against the paper's content, several key points emerge:

* **Novelty and Comparison to CIPHER:** Reviewers 2 and 4 both point out the need for a more thorough comparison with CIPHER, specifically highlighting the differences in communication strategy and the use of activations versus embeddings. While the paper mentions CIPHER, a more detailed discussion of the practical implications and implementation differences would be beneficial.

* **Limitations and Ethical Considerations:** Reviewers 1, 2, and 3 all raise concerns about the limitations of the proposed method. Reviewer 1 asks for a deeper analysis of information loss and the impact of model size. Reviewer 2 notes the lack of discussion on ethical implications. The paper acknowledges the requirement of aligned embeddings and uses a mapping function, but a more rigorous analysis of information loss is missing. The absence of any discussion on ethical considerations is a significant oversight.

* **Experimental Details and Scope:** Reviewers 1, 2, and 4 suggest improvements to the experimental setup and evaluation. Reviewer 1 suggests more reasoning benchmarks and testing on larger models. Reviewer 2 suggests a more detailed comparison with other inter-model communication methods. Reviewer 4 suggests more details on hyperparameters and a discussion of limitations regarding task complexity and scalability. The paper provides some experimental details, but more comprehensive information and a deeper discussion of limitations would strengthen the paper.

* **Comparison to Multi-Agent Debate:** Reviewers 1 and 4 note the need for a more direct comparison with multi-agent debate. While the paper compares against natural language debate, a direct comparison with the specific implementation of multi-agent debate would provide a more comprehensive evaluation.

**Resolution of Conflicting Opinions:**

There aren't significant conflicting opinions among the reviewers. The main areas of focus are the need for more detailed comparisons, a deeper analysis of limitations, and a discussion of ethical considerations.

**Distinguishing Valid from Invalid Criticisms:**

Most of the criticisms are valid or partially valid, indicating areas where the paper could be improved. The main valid criticisms revolve around the lack of a thorough comparison with existing methods (especially CIPHER and multi-agent debate), the absence of a detailed analysis of information loss and ethical implications, and the need for more comprehensive experimental details and a deeper discussion of limitations.

**Summary of Validated Weaknesses:**

* **Limited Comparison with CIPHER:** The paper could provide a more detailed comparison of the proposed method with CIPHER, focusing on the differences in communication strategy and the implications of using activations versus embeddings.
* **Lack of Information Loss Analysis:** The paper lacks a detailed analysis of information loss during the activation transfer process.
* **Missing Ethical Considerations:** The paper does not discuss potential ethical implications of the proposed method, such as bias or misuse.
* **Need for More Experimental Details:** The paper could provide more specific hyperparameters for the activation replacement function and a more comprehensive discussion of the experimental setup.
* **Insufficient Discussion of Limitations:** The paper could benefit from a more in-depth discussion of the limitations of the method, including performance on complex tasks, multi-turn interactions, and scalability to larger models.
* **Limited Comparison with Multi-Agent Debate:** The paper could include a more direct experimental comparison with the specific implementation of multi-agent debate.

**Conclusion:**

The reviewers have identified several valid weaknesses in the paper. The primary areas for improvement are a more thorough comparison with existing methods, a deeper analysis of limitations and ethical considerations, and more comprehensive experimental details. Addressing these weaknesses would significantly strengthen the paper's contribution and impact.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces a novel approach to inter-model communication in large language models (LLMs), termed activation communication (AC). Unlike traditional methods that rely on natural language for interaction, AC leverages the intermediate activation states of neural networks to transfer information between different LLMs. The core idea is to embed post-layer k activations from one model into the activations of another model, which can then be used to enhance the computation or reasoning capabilities of the receiving model. This method aims to circumvent the limitations of natural language, which can be cumbersome and computationally expensive, especially for complex tasks. The authors propose a mechanism where a smaller model's activation is mapped to a larger model's activation space using a learned linear transformation. This transformation is trained on a subset of the multi-player coordination games and reasoning benchmarks used in the experiments. The paper provides a formal analysis of the compute savings achieved by AC compared to natural language communication, demonstrating that AC can achieve up to 27.0% improvement with fewer compute resources. The empirical evaluation includes comprehensive experiments on multi-player coordination games and reasoning benchmarks, using LLaMA models of varying sizes (3B and 8B parameters). The results show that AC outperforms natural language communication and single-model baselines, particularly on reasoning tasks. The authors also explore the impact of different activation mapping functions and model sizes on the performance of AC. Overall, the paper presents a compelling alternative to natural language communication for inter-model interaction, offering a promising direction for future research in multi-agent LLM systems. The key contributions include the novel use of activations for inter-model communication, the formal analysis of compute savings, and the comprehensive empirical validation of the proposed method. The paper's findings suggest that AC could be a valuable technique for enhancing the collaborative capabilities of LLMs, especially in resource-constrained environments.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

2.5


## Strengths:

I find several aspects of this paper to be particularly strong. First and foremost, the core idea of leveraging activations for inter-model communication is both novel and compelling. This approach offers a fresh perspective on how to enable interaction between LLMs, moving beyond the limitations of natural language. The authors have successfully identified a key bottleneck in multi-model collaboration—the computational cost and verbosity of natural language—and have proposed a more efficient alternative. The formal analysis of compute savings is another significant strength. The authors provide a clear and rigorous analysis of the computational benefits of AC, demonstrating that it can achieve substantial performance gains with significantly fewer resources compared to natural language communication. This analysis is crucial for understanding the practical implications of the proposed method and for justifying its potential for real-world applications. The empirical validation of the method is also commendable. The authors have conducted comprehensive experiments on a variety of tasks, including multi-player coordination games and reasoning benchmarks. The results consistently show that AC outperforms natural language communication and single-model baselines, providing strong evidence for the effectiveness of the proposed approach. The use of different model sizes (3B and 8B parameters) and activation mapping functions further enhances the robustness of the experimental findings. The paper is also well-written and easy to follow. The authors have clearly explained the proposed method, the experimental setup, and the results. The paper is structured logically, making it accessible to a broad audience. The authors have also made an effort to compare their method with relevant baselines, such as natural language communication, which helps to contextualize the contributions of their work. Finally, the paper's focus on resource efficiency is particularly relevant in the context of the growing demand for large-scale AI models. By demonstrating that AC can achieve significant performance gains with fewer computational resources, the authors have made a valuable contribution to the field of multi-agent LLM systems.


## Weaknesses:

Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, while the paper introduces the concept of aligned embeddings as a requirement for the method, it does not provide a detailed analysis of the potential for information loss during the activation transfer process. Although the authors mention that the requirement of aligned embeddings is a way to avoid information loss, this is not rigorously analyzed. The paper lacks a quantitative assessment of the rank of the activation matrices or an examination of the information content of the transferred activations using techniques like singular value decomposition. This lack of analysis makes it difficult to fully understand the trade-offs involved in using activations for communication. My confidence in this weakness is high, as the paper does not include any experiments or analysis to quantify the information content of the transferred activations. Second, the paper does not provide a comprehensive comparison with other state-of-the-art methods for inter-model communication, such as multi-agent debate or collaborative reasoning. While the paper mentions multi-agent debate in the related work section, it does not include a direct experimental comparison. The authors only compare against natural language debate, which is a limited comparison. This lack of comparison makes it difficult to assess the relative advantages and disadvantages of the proposed method compared to other existing approaches. My confidence in this weakness is high, as the paper does not include any experimental results comparing against other inter-model communication techniques. Third, the paper does not discuss the potential ethical implications of the proposed method. The authors do not address the potential for bias in the transferred activations or the possibility of misuse of the method. This is a significant oversight, as the use of LLMs in sensitive applications requires careful consideration of ethical issues. My confidence in this weakness is high, as the paper contains no discussion of ethical considerations. Fourth, while the paper provides some experimental details, it lacks specific hyperparameters for the activation replacement function. The authors mention using Xavier initialization for the mapping matrix, but they do not provide details about the function itself or any associated parameters. This lack of detail makes it difficult to reproduce the results and to fully understand the behavior of the method. My confidence in this weakness is medium, as the paper provides some experimental details but lacks specific hyperparameters for the activation replacement function. Fifth, the paper does not provide a detailed discussion of the limitations of the method. While the authors mention the requirement of aligned embeddings and the use of a mapping function, they do not discuss the potential challenges in scaling the method to larger models or more diverse datasets. The paper also does not discuss the performance of the method on tasks that require more complex reasoning or multi-turn interactions. My confidence in this weakness is medium, as the paper mentions some limitations but lacks a detailed discussion of performance on complex tasks and scalability. Finally, the paper does not include experiments on larger models, such as 70B parameter models. This limits the generalizability of the results and raises questions about the scalability of the method. My confidence in this weakness is high, as the paper's experiments are limited to models up to 8B parameters.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should conduct a more thorough investigation into the limitations of the activation-based communication method. Specifically, they should explore the potential for information loss during the activation transfer process. This could involve analyzing the rank of the activation matrices or examining the information content of the transferred activations using techniques like singular value decomposition. Furthermore, the impact of model size on the effectiveness of the proposed method should be investigated. It would be valuable to see experiments with models of varying sizes to understand how the communication performance scales with model capacity. This analysis should also consider the computational cost associated with extracting and processing activations, especially for larger models. A detailed analysis of these limitations would provide a more complete picture of the method's applicability and potential drawbacks. Second, the authors should include a more comprehensive comparison with existing inter-model communication techniques. While the paper mentions multi-agent debate and collaborative reasoning, it lacks a detailed empirical comparison. The authors should implement and evaluate these methods on the same datasets used in their experiments to provide a more robust assessment of the proposed method's advantages and disadvantages. This comparison should not only focus on performance metrics but also consider computational cost and communication overhead. Furthermore, the authors should explore the potential of combining their method with other communication techniques to achieve even better performance. For example, they could investigate whether the proposed method can be used in conjunction with multi-agent debate to further improve reasoning capabilities. Such an analysis would provide a more nuanced understanding of the method's potential and its place within the broader landscape of inter-model communication. Third, the authors should address the potential ethical implications of the proposed method. The authors should discuss the potential for bias in the transferred activations and how this could be mitigated. They should also consider the potential for misuse of the method, such as in adversarial settings. A discussion of these ethical considerations would add a valuable dimension to the paper and demonstrate a responsible approach to research. This discussion should also consider the potential for the method to be used in sensitive applications, such as those involving personal data or sensitive decision-making. By addressing these ethical considerations, the authors can enhance the credibility and impact of their work. Fourth, the authors should provide more detailed experimental information, including the specific models used for each task, the hyperparameters used for training and evaluation, and the exact evaluation metrics used. For example, if the models are Llama models, the specific version and size should be mentioned. The authors should also specify the optimization algorithm used, the learning rate, and any other relevant training details. Furthermore, the authors should provide the code and the data used in the experiments to allow other researchers to reproduce their results. This would increase the credibility of the paper and allow other researchers to build upon their work. The authors should also discuss the sensitivity of their method to different hyperparameters and provide guidelines for selecting the optimal hyperparameters for different tasks. Fifth, the authors should discuss the limitations of their method and potential directions for future research. This should include a discussion of the potential challenges in scaling the method to larger models or more diverse datasets. For example, the authors should discuss the computational cost of extracting and processing activations from larger models and how this might affect the scalability of their method. The authors should also discuss the potential challenges in applying their method to tasks that require more complex reasoning or multi-turn interactions. This would help the reader understand the scope and limitations of the proposed approach and identify potential areas for future research. Finally, the authors should conduct experiments on larger models, such as 70B parameter models, to demonstrate the scalability of their method. This would provide more evidence of the method's applicability and potential for real-world use.


## Questions:

I have several questions that arise from my analysis of this paper. First, how does the proposed method perform on tasks that require more complex reasoning or multi-turn interactions? The paper focuses on single-turn reasoning tasks, but it is unclear how the method would scale to more complex scenarios. Second, what are the potential challenges in scaling the method to larger models or more diverse datasets? The paper does not provide a detailed discussion of the computational cost associated with extracting and processing activations from larger models, and it is unclear how the method would perform on datasets with more diverse characteristics. Third, how does the method compare to other state-of-the-art methods for inter-model communication, such as multi-agent debate or collaborative reasoning? The paper only compares against natural language debate, and it is unclear how the proposed method would perform against other advanced techniques. Fourth, what are the potential ethical implications of the proposed method, such as the potential for bias or misuse? The paper does not discuss these issues, and it is important to consider the potential societal impact of the method. Fifth, how sensitive is the method to the choice of activation mapping function? The paper uses a learned linear layer for the mapping function, but it is unclear how the performance of the method would be affected by different choices of mapping functions. Sixth, how does the method perform on tasks that require more than just reasoning, such as creative writing or code generation? The paper focuses on reasoning tasks, and it is unclear how the method would perform on other types of tasks. Finally, what are the potential applications of the proposed method beyond the specific tasks used in the paper? The paper focuses on reasoning tasks, but it is unclear how the method could be applied to other domains or applications.


## Rating:

6.25


## Confidence:

3.0


## Decision:

Accept
}