I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper presents a controlled weight-space comparison of offline reasoning losses (SFT, RFT, DFT, RIFT, Offline GRPO, DPO) applied to identical math rollouts from a single base model (Qwen3-4B) using attention-only LoRA. The study analyzes the resulting deltas via cosine similarity, principal-angle subspace analysis, linear mode connectivity, and CKA. The findings reveal that SFT, RFT, and RIFT have nearly identical weight deltas, while DFT diverges more significantly in direction. Offline GRPO adds a substantial orthogonal component to the SFT direction, placing it in a near-orthogonal subspace. DPO exhibits a near-orthogonal subspace to SFT, showing a sharp linear-mode barrier and collapsing late-layer CKA values. DPO also reaches the highest accuracy on GSM8K and AIME26. The study also notes that DPO uses a smaller learning rate than other methods. Overall, the paper suggests that the primary difference between losses lies in the direction of the weight update rather than the magnitude.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The study is well-executed, with a controlled setup that includes identical rollouts, the same base model, and attention-only LoRA. This setup allows for a clear comparison of the weight updates across different loss functions.
2. The paper employs multiple analysis techniques, including cosine similarity, principal-angle subspace analysis, linear mode connectivity, and CKA, to provide a comprehensive view of the weight-space differences.
3. The findings are clearly presented and well-supported by the experimental results. The paper effectively communicates the key takeaways, such as the near-identical weight deltas for SFT, RFT, and RIFT, and the significant divergence of DFT.

### Weaknesses

#### Some Related Works


#### comment

1. The study is limited to a single base model (Qwen3-4B) and a specific domain (math reasoning). This narrow scope raises questions about the generalizability of the findings to other models and tasks. The conclusions drawn from this specific setup may not hold true for models with different architectures or for tasks with different characteristics. For instance, models with different pre-training objectives or those trained on datasets with varying levels of noise could exhibit different weight update patterns under the same loss functions. The limited scope of the study restricts the broader applicability of the conclusions.
2. The paper does not provide a detailed analysis of the computational cost associated with each method. This information is crucial for practitioners who need to choose the most efficient method for their specific needs. The lack of computational cost analysis makes it difficult to assess the practical trade-offs between the different methods, especially when considering the computational resources required for training large language models. A detailed analysis should include training time, memory usage, and the number of parameters involved in each method.
3. The paper does not provide a detailed analysis of the computational cost associated with each method. This information is crucial for practitioners who need to choose the most efficient method for their specific needs. The lack of computational cost analysis makes it difficult to assess the practical trade-offs between the different methods, especially when considering the computational resources required for training large language models. A detailed analysis should include training time, memory usage, and the number of parameters involved in each method.

### Suggestions

The study would benefit significantly from expanding the scope of the experiments to include a more diverse set of base models and tasks. This would help to establish the generalizability of the findings and identify potential limitations of the observed weight update patterns. For example, the authors could consider evaluating the methods on models with different architectures, such as encoder-decoder models or models with different pre-training objectives. Additionally, the study could be extended to include tasks beyond math reasoning, such as natural language understanding or text generation. This would provide a more comprehensive understanding of how the different loss functions affect the weight updates in various contexts. Furthermore, it would be beneficial to investigate the impact of different hyperparameters, such as learning rate and batch size, on the observed weight update patterns. This would help to identify the optimal settings for each method and provide a more nuanced understanding of their behavior.

To address the lack of computational cost analysis, the authors should include a detailed comparison of the training time, memory usage, and the number of parameters involved in each method. This analysis should be conducted on the same hardware and with the same datasets to ensure a fair comparison. The authors should also discuss the trade-offs between the different methods in terms of computational cost and performance. For example, they could analyze the relationship between the computational cost and the accuracy of each method. This would help practitioners to choose the most appropriate method for their specific needs. Furthermore, the authors should consider the impact of batch size and learning rate on the computational cost of each method. This would provide a more complete picture of the practical implications of using each method.

Finally, the paper should include a more detailed discussion of the limitations of the study and the potential directions for future research. This discussion should acknowledge the limitations of the current setup and highlight the potential impact of the findings. The authors should also identify the open questions that remain unanswered by the study and suggest specific avenues for future research. For example, they could investigate the effect of different loss functions on the weight updates in different layers of the model. This would provide a more nuanced understanding of the internal mechanisms of the models and their response to different loss functions. Additionally, the authors could explore the use of different evaluation metrics to assess the performance of the different methods. This would provide a more comprehensive evaluation of the methods and their practical implications.

### Questions

1. How do the findings generalize to other base models and tasks? Are there any potential limitations or challenges in applying these conclusions to different contexts?
2. What is the computational cost associated with each method? How do the computational requirements compare across different methods?
3. How do the different loss functions affect the weight updates in different layers of the model? Are there any layer-specific patterns or trends that could provide further insights?

### Rating

5

### Confidence

4

**********

## Reviewer 2

### Summary

This paper compares the weight-space changes induced by different offline reasoning loss functions, including SFT, RFT, RIFT, DFT, Offline GRPO, and DPO. The experiments are conducted on the same math rollouts from a single base model (Qwen3-4B) with attention-only LoRA, and the analysis is performed on the resulting deltas via cosine similarity, principal-angle subspace analysis, linear mode connectivity, and CKA. The findings reveal that SFT, RFT, and RIFT have nearly identical weight deltas, while DFT diverges more significantly in direction. Offline GRPO adds a substantial orthogonal component to the SFT direction, placing it in a near-orthogonal subspace. DPO exhibits a near-orthogonal subspace to SFT, showing a sharp linear-mode barrier and collapsing late-layer CKA values. DPO also reaches the highest accuracy on GSM8K and AIME26. The study also notes that DPO uses a smaller learning rate than other methods.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper provides a comprehensive comparison of different offline reasoning loss functions in terms of their weight-space changes, which is crucial for understanding the mechanisms behind these methods.
- The paper is well-written and easy to follow.
- The paper provides valuable insights into the differences between different offline reasoning loss functions, which can help researchers and practitioners choose the most appropriate method for their specific needs.

### Weaknesses

#### Some Related Works


#### comment

 - The paper only compares six offline reasoning loss functions, which may not be sufficient to draw general conclusions about the behavior of all offline reasoning loss functions.
- The paper does not provide a clear explanation of why DPO has a near-orthogonal subspace to SFT. It is not clear what the implications of this near-orthogonality are for the performance of DPO compared to other methods. Specifically, the paper does not explore the potential for DPO to explore different regions of the loss landscape, which could lead to improved generalization or robustness.
- The paper does not discuss the potential limitations of using LoRA for weight updates. While LoRA is a popular technique for efficient fine-tuning, it may not be suitable for all types of reasoning tasks or models. The paper should acknowledge the potential limitations of using LoRA and discuss how these limitations might affect the results.

### Suggestions

The paper would benefit from a more thorough investigation into the behavior of DPO's weight updates. While the observation of near-orthogonality to SFT is interesting, the paper should delve deeper into the implications of this finding. For instance, the authors could analyze the loss landscape around the SFT and DPO solutions to understand why DPO's updates are so different. This could involve visualizing the loss surface or computing the Hessian of the loss function at both points. Furthermore, the paper should explore whether the near-orthogonality is a consistent phenomenon across different tasks and datasets. It would be valuable to see if this behavior is specific to the math reasoning tasks used in the paper or if it generalizes to other types of reasoning problems. The authors could also investigate whether DPO's updates lead to a different exploration of the weight space, potentially explaining its superior performance on certain tasks. This could involve analyzing the trajectory of the weight updates during training or comparing the final weight distributions of DPO and other methods.

To strengthen the paper, the authors should also consider exploring alternative fine-tuning techniques beyond LoRA. While LoRA is computationally efficient, it may not be the most suitable method for all reasoning tasks. The paper should discuss the potential limitations of using LoRA, such as its inability to modify certain layers or its potential to limit the model's capacity to learn complex relationships. The authors could also investigate the impact of different LoRA configurations on the weight updates and the resulting performance. For example, they could vary the rank of the LoRA matrices or the number of trainable parameters. This would provide a more comprehensive understanding of how LoRA affects the behavior of different offline reasoning loss functions. Furthermore, the authors could explore other parameter-efficient fine-tuning techniques, such as adapter layers or prefix tuning, to see if they lead to different results. This would help to determine whether the observed differences between the loss functions are specific to LoRA or if they are more generalizable.

Finally, the paper should provide a more detailed discussion of the implications of the observed weight-space differences for the practical application of these methods. For example, the authors could discuss how the near-orthogonality of DPO to SFT might affect its robustness to adversarial attacks or its ability to generalize to out-of-distribution data. The paper could also explore whether the different weight update patterns lead to different types of errors or biases. This could involve analyzing the model's predictions on specific examples or using techniques such as probing or activation analysis. By providing a more in-depth analysis of the practical implications of the weight-space differences, the paper would be more valuable to researchers and practitioners who are interested in applying these methods to real-world problems.

### Questions

- What are the potential limitations of using LoRA for weight updates, and how might these limitations affect the results?
- How does the near-orthogonality of DPO to SFT affect its performance compared to other methods?
- Are the observed differences in weight-space changes consistent across different tasks and datasets, or are they specific to the math reasoning tasks used in the paper?

### Rating

5

### Confidence

4

**********

## Reviewer 3

### Summary

This paper compares the weight-space changes induced by different offline reasoning loss functions, including SFT, RFT, RIFT, DFT, Offline GRPO, and DPO. The experiments are conducted on the same math rollouts from a single base model (Qwen3-4B) with attention-only LoRA, and the analysis is performed on the resulting deltas via cosine similarity, principal-angle subspace analysis, linear mode connectivity, and CKA. The findings reveal that SFT, RFT, and RIFT have nearly identical weight deltas, while DFT diverges more significantly in direction. Offline GRPO adds a substantial orthogonal component to the SFT direction, placing it in a near-orthogonal subspace. DPO exhibits a near-orthogonal subspace to SFT, showing a sharp linear-mode barrier and collapsing late-layer CKA values. DPO also reaches the highest accuracy on GSM8K and AIME26. The study also notes that DPO uses a smaller learning rate than other methods.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper provides a comprehensive comparison of different offline reasoning loss functions in terms of their weight-space changes, which is crucial for understanding the mechanisms behind these methods.
2. The paper is well-written and easy to follow.
3. The paper provides valuable insights into the differences between different offline reasoning loss functions, which can help researchers and practitioners choose the most appropriate method for their specific needs.

### Weaknesses

#### Some Related Works


#### comment

1. The paper only compares six offline reasoning loss functions, which may not be sufficient to draw general conclusions about the behavior of all offline reasoning loss functions.
2. The paper does not provide a clear explanation of why DPO has a near-orthogonal subspace to SFT. It is not clear what the implications of this near-orthogonality are for the performance of DPO compared to other methods. Specifically, the paper lacks a discussion on the potential for DPO to explore different regions of the loss landscape, which could lead to improved generalization or robustness. The near orthogonality could indicate that DPO is converging to a different local minimum, but this is not explored.
3. The paper does not discuss the potential limitations of using LoRA for weight updates. While LoRA is a popular technique for efficient fine-tuning, it may not be suitable for all types of reasoning tasks or models. The paper should acknowledge the potential limitations of using LoRA and discuss how these limitations might affect the results. For example, LoRA might not be able to effectively modify certain layers or its rank might limit the model's capacity to learn complex relationships.

### Suggestions

The paper would benefit from a more thorough investigation into the behavior of DPO's weight updates. While the observation of near-orthogonality to SFT is interesting, the paper should delve deeper into the implications of this finding. For instance, the authors could analyze the loss landscape around the SFT and DPO solutions to understand why DPO's updates are so different. This could involve visualizing the loss surface or computing the Hessian of the loss function at both points. Furthermore, the paper should explore whether the near-orthogonality is a consistent phenomenon across different tasks and datasets. It would be valuable to see if this behavior is specific to the math reasoning tasks used in the paper or if it generalizes to other types of reasoning problems. The authors could also investigate whether DPO's updates lead to a different exploration of the weight space, potentially explaining its superior performance on certain tasks. This could involve analyzing the trajectory of the weight updates during training or comparing the final weight distributions of DPO and other methods.

To strengthen the paper, the authors should also consider exploring alternative fine-tuning techniques beyond LoRA. While LoRA is computationally efficient, it may not be the most suitable method for all reasoning tasks. The paper should discuss the potential limitations of using LoRA, such as its inability to modify certain layers or its rank limitation on the model's capacity. The authors could also investigate the impact of different LoRA configurations on the weight updates and the resulting performance. For example, they could vary the rank of the LoRA matrices or the number of trainable parameters. This would provide a more comprehensive understanding of how LoRA affects the behavior of different offline reasoning loss functions. Furthermore, the authors could explore other parameter-efficient fine-tuning techniques, such as adapter layers or prefix tuning, to see if they lead to different results. This would help to determine whether the observed differences between the loss functions are specific to LoRA or if they are more generalizable.

Finally, the paper should provide a more detailed discussion of the implications of the observed weight-space differences for the practical application of these methods. For example, the authors could discuss how the near-orthogonality of DPO to SFT might affect its robustness to adversarial attacks or its ability to generalize to out-of-distribution data. The paper could also explore whether the different weight update patterns lead to different types of errors or biases. This could involve analyzing the model's predictions on specific examples or using techniques such as probing or activation analysis. By providing a more in-depth analysis of the practical implications of the weight-space differences, the paper would be more valuable to researchers and practitioners who are interested in applying these methods to real-world problems.

### Questions

1. What are the potential limitations of using LoRA for weight updates, and how might these limitations affect the results?
2. How does the near-orthogonality of DPO to SFT affect its performance compared to other methods?
3. Are the observed differences in weight-space changes consistent across different tasks and datasets, or are they specific to the math reasoning tasks used in the paper?

### Rating

5

### Confidence

3

**********

## Reviewer 4

### Summary

This paper compares the effect of six different offline reasoning loss functions (SFT, RFT, RIFT, DFT, Offline GRPO, DPO) on the weight space of a language model (Qwen3-4B) using attention-only LoRA. The authors analyze the cosine similarity, principal-angle subspace analysis, linear mode connectivity, and CKA of the resulting weight deltas. The results show that SFT, RFT, and RIFT have nearly identical weight deltas, while DFT diverges more significantly in direction. Offline GRPO adds a substantial orthogonal component to the SFT direction, placing it in a near-orthogonal subspace. DPO exhibits a near-orthogonal subspace to SFT, showing a sharp linear-mode barrier and collapsing late-layer CKA values. DPO also reaches the highest accuracy on GSM8K and AIME26.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a comprehensive comparison of the weight space changes induced by different offline reasoning loss functions, which is crucial for understanding the mechanisms behind these methods.
3. The paper includes multiple analysis techniques, including cosine similarity, principal-angle subspace analysis, linear mode connectivity, and CKA, to provide a thorough understanding of the weight space changes.
4. The authors clearly communicate the key takeaways, such as the near-identical weight deltas for SFT, RFT, and RIFT, and the significant divergence of DFT.

### Weaknesses

#### Some Related Works


#### comment

1. The paper only compares six offline reasoning loss functions, which may not be sufficient to draw general conclusions about the behavior of all offline reasoning loss functions.
2. The paper does not provide a clear explanation of why DPO has a near-orthogonal subspace to SFT. It is not clear what the implications of this near-orthogonality are for the performance of DPO compared to other methods. Specifically, the paper lacks a discussion on the potential for DPO to explore different regions of the loss landscape, which could lead to improved generalization or robustness.
3. The paper does not discuss the potential limitations of using LoRA for weight updates. While LoRA is a popular technique for efficient fine-tuning, it may not be suitable for all types of reasoning tasks or models. The paper should acknowledge the potential limitations of using LoRA and discuss how these limitations might affect the results. For example, LoRA might not be able to effectively modify certain layers or its rank might limit the model's capacity to learn complex relationships.

### Suggestions

The study would benefit from a more thorough investigation into the behavior of DPO's weight updates. While the observation of near-orthogonality to SFT is interesting, the paper should delve deeper into the implications of this finding. For instance, the authors could analyze the loss landscape around the SFT and DPO solutions to understand why DPO's updates are so different. This could involve visualizing the loss surface or computing the Hessian of the loss function at both points. Furthermore, the paper should explore whether the near-orthogonality is a consistent phenomenon across different tasks and datasets. It would be valuable to see if this behavior is specific to the math reasoning tasks used in the paper or if it generalizes to other types of reasoning problems. The authors could also investigate whether DPO's updates lead to a different exploration of the weight space, potentially explaining its superior performance on certain tasks. This could involve analyzing the trajectory of the weight updates during training or comparing the final weight distributions of DPO and other methods.

To strengthen the paper, the authors should also consider exploring alternative fine-tuning techniques beyond LoRA. While LoRA is computationally efficient, it may not be the most suitable method for all reasoning tasks. The paper should discuss the potential limitations of using LoRA, such as its inability to modify certain layers or its rank limitation on the model's capacity. The authors could also investigate the impact of different LoRA configurations on the weight updates and the resulting performance. For example, they could vary the rank of the LoRA matrices or the number of trainable parameters. This would provide a more comprehensive understanding of how LoRA affects the behavior of different offline reasoning loss functions. Furthermore, the authors could explore other parameter-efficient fine-tuning techniques, such as adapter layers or prefix tuning, to see if they lead to different results. This would help to determine whether the observed differences between the loss functions are specific to LoRA or if they are more generalizable.

Finally, the paper should provide a more detailed discussion of the implications of the observed weight-space differences for the practical application of these methods. For example, the authors could discuss how the near-orthogonality of DPO to SFT might affect its robustness to adversarial attacks or its ability to generalize to out-of-distribution data. The paper could also explore whether the different weight update patterns lead to different types of errors or biases. This could involve analyzing the model's predictions on specific examples or using techniques such as probing or activation analysis. By providing a more in-depth analysis of the practical implications of the weight-space differences, the paper would be more valuable to researchers and practitioners who are interested in applying these methods to real-world problems.

### Questions

1. What are the potential limitations of using LoRA for weight updates, and how might these limitations affect the results?
2. How does the near-orthogonality of DPO to SFT affect its performance compared to other methods?
3. Are the observed differences in weight-space changes consistent across different tasks and datasets, or are they specific to the math reasoning tasks used in the paper?

### Rating

6

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in a given paper. I need to go through each reviewer's comments and check if the criticism is valid based on the content of the paper.

Here's my plan:
1. **Parse each reviewer's comments.**
2. **For each weakness identified by a reviewer:**
    - **Locate the relevant section in the paper.**
    - **Find evidence (or lack thereof) to support the reviewer's claim.**
    - **Categorize the weakness.**
    - **Provide a validation analysis with evidence.**
    - **Conclude on the validity of the weakness.**
**Review 1 Weaknesses:**

1. Weakness Statement:
"The paper only compares six offline reasoning loss functions, which may not be sufficient to draw general conclusions about the behavior of all offline reasoning loss functions."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper explicitly states in the "Setup" section: "We present a controlled weight-space comparison of offline reasoning losses: identical rollouts, identical base model (Qwen3-4B-Instruct), shared LoRA initialization, six methods (DPO, RFT, DFT, RIFT, Offline GRPO, DPO)..." This confirms that only six methods were compared.

3. Literature Gap Analysis:
   - The paper does not explicitly discuss the limitations of the number of methods chosen or cite literature on the generalizability of findings across different offline RL methods.

4. Validation Analysis:
   - Primary evidence: The paper clearly lists the six methods used for comparison.
   - Supporting quotes: "six methods (DPO, RFT, DFT, RIFT, Offline GRPO, DPO)"
   - Impact assessment: The limited number of methods could restrict the generalizability of the conclusions.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Explicit listing of the six compared methods.

1. Weakness Statement:
"The paper does not provide a clear explanation of why DPO has a near-orthogonal subspace to SFT. It is not clear what the implications of this near-orthogonality are for the performance of DPO compared to other methods. Specifically, the paper lacks a discussion on the potential for DPO to explore different regions of the loss landscape, which could lead to improved generalization or robustness."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper describes the weight-space analysis in the "Results" section, specifically in "3.2 Weight-space analysis". It presents the cosine similarity matrix and discusses the near-orthogonality of DPO to SFT and Offline GRPO.
   - The paper states: "DPO is orthogonal to everything: cosine to SFT, RFT, and RIFT all fall in [ 0.057 , 0.065 ] [0.057, 0.065] . The DPO training uses a 10 × 10\times smaller learning rate, so its norm/accuracy gaps are entangled with the optimizer setting and correlation worth a LR-matched follow-up, not a causal claim."
b) Experiment-related Evidence:
   - The paper presents the cosine similarity values in Figure 1 and discusses the near-orthogonality in the "Results" section.

3. Literature Gap Analysis:
   - The paper does not cite specific literature on the implications of weight-space orthogonality for generalization or robustness in the context of DPO.

4. Validation Analysis:
   - Primary evidence: The paper identifies the near-orthogonality but doesn't delve into the *reasons* behind it or the *implications* for DPO's performance.
   - Supporting quotes: "DPO is orthogonal to everything: cosine to SFT, RFT, and RIFT all fall in [ 0.057 , 0.065 ] [0.057, 0.065] ."
   - Impact assessment: The lack of explanation and discussion weakens the understanding of DPO's behavior.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper's observation of near-orthogonality without a detailed explanation or discussion of implications.

1. Weakness Statement:
"The paper does not discuss the potential limitations of using LoRA for weight updates. While LoRA is a popular technique for efficient fine-tuning, it may not be suitable for all types of reasoning tasks or models. The paper should acknowledge the potential limitations of using LoRA and discuss how these limitations might affect the results. For example, LoRA might not be able to effectively modify certain layers or its rank might limit the model's capacity to learn complex relationships."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper states in the "Setup" section: "Qwen3-4B-Instruct-2507, LoRA on attention projections ( q,k,v,o_proj ; rank 32 32 , α = 64 α{ = 64 , dropout 0 0 ; 144 modules over 36 36 layers)."
   - The paper also mentions: "The LoRA delta Δ A \Delta A ΔA is gauge-invariant, so its cosine is genuine."
b) Experiment-related Evidence:
   - The paper uses LoRA consistently across all methods.

3. Literature Gap Analysis:
   - The paper does not cite literature discussing the limitations of LoRA in specific contexts or its impact on different types of fine-tuning.

4. Validation Analysis:
   - Primary evidence: The paper uses LoRA without discussing its potential limitations.
   - Supporting quotes: "LoRA on attention projections ( q,k,v,o_proj ; rank 32 32 , α = 64 α{ = 64 , dropout 0 0 ; 144 modules over 36 36 layers)."
   - Impact assessment: The lack of discussion on LoRA limitations leaves a gap in understanding the scope and potential biases of the findings.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper's exclusive use of LoRA without discussing its limitations.

**Review 2 Weaknesses:**

1. Weakness Statement:
"The study is limited to a single base model (Qwen3-4B) and a specific domain (math reasoning). This narrow scope raises questions about the generalizability of the findings to other models and tasks. The conclusions drawn from this specific setup may not hold true for models with different architectures or for tasks with different characteristics. For instance, models with different pre-training objectives or those trained on datasets with varying levels of noise could exhibit different weight update patterns under the same loss functions. The limited scope of the study restricts the broader applicability of the conclusions."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper explicitly states in the "Setup" section: "All methods share one set of rollouts, identical base model (Qwen3-4B-Instruct), shared LoRA initialization, six methods (DPO, RFT, DFT, RIFT, Offline GRPO, DPO)..."
   - The paper uses "DeepScaleR prompts ( ∼ 40 {~\sim}40 k verified math ( Agentica, 2025 ) ), teacher DeepSeek-V4-Flash, K = 4 K{= 4} CoT completions/prompt, binary math-verify reward." for math reasoning tasks.

3. Literature Gap Analysis:
   - The paper does not discuss the limitations of using a single base model and a specific task domain or cite literature on the generalizability of findings across different models and tasks.

4. Validation Analysis:
   - Primary evidence: The paper clearly states the use of a single base model and a specific task domain.
   - Supporting quotes: "identical base model (Qwen3-4B-Instruct)", "DeepScaleR prompts ( ∼ 40 {~\sim}40 k verified math ( Agentica, 2025 ) )..."
   - Impact assessment: The limited scope restricts the generalizability of the findings.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Explicit mention of the single base model and task domain.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost associated with each method. This information is crucial for practitioners who need to choose the most efficient method for their specific needs. The lack of computational cost analysis makes it difficult to assess the practical trade-offs between the different methods, especially when considering the computational resources required for training large language models. A detailed analysis should include training time, memory usage, and the number of parameters involved in each method."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper provides details about the hardware and software environment in the "Setup" section: "All methods share one set of rollouts, identical base model (Qwen3-4B-Instruct), shared LoRA initialization, six methods (DPO, RFT, DFT, RIFT, Offline GRPO, DPO)..."
   - The paper mentions the LoRA rank and learning rate but does not provide a detailed analysis of training time, memory usage, or the number of trainable parameters for each method.

3. Literature Gap Analysis:
   - The paper does not cite literature on computational cost analysis for different offline RL methods.

4. Validation Analysis:
   - Primary evidence: The paper lacks a detailed analysis of computational costs.
   - Supporting quotes: The paper describes the setup but doesn't quantify the computational resources required for each method.
   - Impact assessment: The lack of computational cost analysis makes it difficult to assess the practical trade-offs of the methods.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of detailed computational cost analysis in the paper.

**Review 3 Weaknesses:**

1. Weakness Statement:
"The paper only compares six offline reasoning loss functions, which may not be sufficient to draw general conclusions about the behavior of all offline reasoning loss functions."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper explicitly states in the "Setup" section: "We present a controlled weight-space comparison of offline reasoning losses: identical rollouts, identical base model (Qwen3-4B-Instruct), shared LoRA initialization, six methods (DPO, RFT, DFT, RIFT, Offline GRPO, DPO)..." This confirms that only six methods were compared.

3. Literature Gap Analysis:
   - The paper does not explicitly discuss the limitations of the number of methods chosen or cite literature on the generalizability of findings across different offline RL methods.

4. Validation Analysis:
   - Primary evidence: The paper clearly lists the six methods used for comparison.
   - Supporting quotes: "six methods (DPO, RFT, DFT, RIFT, Offline GRPO, DPO)"
   - Impact assessment: The limited number of methods could restrict the generalizability of the conclusions.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Explicit listing of the six compared methods.

1. Weakness Statement:
"The paper does not provide a clear explanation of why DPO has a near-orthogonal subspace to SFT. It is not clear what the implications of this near-orthogonality are for the performance of DPO compared to other methods. Specifically, the paper lacks a discussion on the potential for DPO to explore different regions of the loss landscape, which could lead to improved generalization or robustness."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper describes the weight-space analysis in the "Results" section, specifically in "3.2 Weight-space analysis". It presents the cosine similarity matrix and discusses the near-orthogonality of DPO to SFT and Offline GRPO.
   - The paper states: "DPO is orthogonal to everything: cosine to SFT, RFT, and RIFT all fall in [ 0.057 , 0.065 ] [0.057, 0.065] . The DPO training uses a 10 × 10\times smaller learning rate, so its norm/accuracy gaps are entangled with the optimizer setting and correlation worth a LR-matched follow-up, not a causal claim."
b) Experiment-related Evidence:
   - The paper presents the cosine similarity values in Figure 1 and discusses the near-orthogonality in the "Results" section.

3. Literature Gap Analysis:
   - The paper does not cite specific literature on the implications of weight-space orthogonality for generalization or robustness in the context of DPO.

4. Validation Analysis:
   - Primary evidence: The paper identifies the near-orthogonality but doesn't delve into the *reasons* behind it or the *implications* for DPO's performance.
   - Supporting quotes: "DPO is orthogonal to everything: cosine to SFT, RFT, and RIFT all fall in [ 0.057 , 0.065 ] [0.057, 0.065] ."
   - Impact assessment: The lack of explanation and discussion weakens the understanding of DPO's behavior.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper's observation of near-orthogonality without a detailed explanation or discussion of implications.

1. Weakness Statement:
"The paper does not discuss the potential limitations of using LoRA for weight updates. While LoRA is a popular technique for efficient fine-tuning, it may not be suitable for all types of reasoning tasks or models. The paper should acknowledge the potential limitations of using LoRA and discuss how these limitations might affect the results. For example, LoRA might not be able to effectively modify certain layers or its rank might limit the model's capacity to learn complex relationships."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper states in the "Setup" section: "Qwen3-4B-Instruct-2507, LoRA on attention projections ( q,k,v,o_proj ; rank 32 32 , α = 64 α{ = 64 , dropout 0 0 ; 144 modules over 36 36 layers)."
   - The paper also mentions: "The LoRA delta Δ A \Delta A ΔA is gauge-invariant, so its cosine is genuine."
b) Experiment-related Evidence:
   - The paper uses LoRA consistently across all methods.

3. Literature Gap Analysis:
   - The paper does not cite literature discussing the limitations of LoRA in specific contexts or its impact on different types of fine-tuning.

4. Validation Analysis:
   - Primary evidence: The paper uses LoRA without discussing its potential limitations.
   - Supporting quotes: "LoRA on attention projections ( q,k,v,o_proj ; rank 32 32 , α = 64 α{ = 64 , dropout 0 0 ; 144 modules over 36 36 layers)."
   - Impact assessment: The lack of discussion on LoRA limitations leaves a gap in understanding the scope and potential biases of the findings.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper's exclusive use of LoRA without discussing its limitations.

**Review 4 Weaknesses:**

1. Weakness Statement:
"The paper only compares six offline reasoning loss functions, which may not be sufficient to draw general conclusions about the behavior of all offline reasoning loss functions."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper explicitly states in the "Setup" section: "We present a controlled weight-space comparison of offline reasoning losses: identical rollouts, identical base model (Qwen3-4B-Instruct), shared LoRA initialization, six methods (DPO, RFT, DFT, RIFT, Offline GRPO, DPO)..." This confirms that only six methods were compared.

3. Literature Gap Analysis:
   - The paper does not explicitly discuss the limitations of the number of methods chosen or cite literature on the generalizability of findings across different offline RL methods.

4. Validation Analysis:
   - Primary evidence: The paper clearly lists the six methods used for comparison.
   - Supporting quotes: "six methods (DPO, RFT, DFT, RIFT, Offline GRPO, DPO)"
   - Impact assessment: The limited number of methods could restrict the generalizability of the conclusions.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Explicit listing of the six compared methods.

1. Weakness Statement:
"The paper does not provide a clear explanation of why DPO has a near-orthogonal subspace to SFT. It is not clear what the implications of this near-orthogonality are for the performance of DPO compared to other methods. Specifically, the paper lacks a discussion on the potential for DPO to explore different regions of the loss landscape, which could lead to improved generalization or robustness."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper describes the weight-space analysis in the "Results" section, specifically in "3.2 Weight-space analysis". It presents the cosine similarity matrix and discusses the near-orthogonality of DPO to SFT and Offline GRPO.
   - The paper states: "DPO is orthogonal to everything: cosine to SFT, RFT, and RIFT all fall in [ 0.057 , 0.065 ] [0.057, 0.065] . The DPO training uses a 10 × 10\times smaller learning rate, so its norm/accuracy gaps are entangled with the optimizer setting and correlation worth a LR-matched follow-up, not a causal claim."
b) Experiment-related Evidence:
   - The paper presents the cosine similarity values in Figure 1 and discusses the near-orthogonality in the "Results" section.

3. Literature Gap Analysis:
   - The paper does not cite specific literature on the implications of weight-space orthogonality for generalization or robustness in the context of DPO.

4. Validation Analysis:
   - Primary evidence: The paper identifies the near-orthogonality but doesn't delve into the *reasons* behind it or the *implications* for DPO's performance.
   - Supporting quotes: "DPO is orthogonal to everything: cosine to SFT, RFT, and RIFT all fall in [ 0.057 , 0.065 ] [0.057, 0.065] ."
   - Impact assessment: The lack of explanation and discussion weakens the understanding of DPO's behavior.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper's observation of near-orthogonality without a detailed explanation or discussion of implications.

1. Weakness Statement:
"The paper does not discuss the potential limitations of using LoRA for weight updates. While LoRA is a popular technique for efficient fine-tuning, it may not be suitable for all types of reasoning tasks or models. The paper should acknowledge the potential limitations of using LoRA and discuss how these limitations might affect the results. For example, LoRA might not be able to effectively modify certain layers or its rank might limit the model's capacity to learn complex relationships."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper states in the "Setup" section: "Qwen3-4B-Instruct-2507, LoRA on attention projections ( q,k,v,o_proj ; rank 32 32 , α = 64 α{ = 64 , dropout 0 0 ; 144 modules over 36 36 layers)."
   - The paper also mentions: "The LoRA delta Δ A \Delta A ΔA is gauge-invariant, so its cosine is genuine."
b) Experiment-related Evidence:
   - The paper uses LoRA consistently across all methods.

3. Literature Gap Analysis:
   - The paper does not cite literature discussing the limitations of LoRA in specific contexts or its impact on different types of fine-tuning.

4. Validation Analysis:
   - Primary evidence: The paper uses LoRA without discussing its potential limitations.
   - Supporting quotes: "LoRA on attention projections ( q,k,v,o_proj ; rank 32 32 , α = 64 α{ = 64 , dropout 0 0 ; 144 modules over 36 36 layers)."
   - Impact assessment: The lack of discussion on LoRA limitations leaves a gap in understanding the scope and potential biases of the findings.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper's exclusive use of LoRA without discussing its limitations.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper presents a controlled study comparing the weight-space changes induced by various offline reasoning loss functions, namely SFT, RFT, RIFT, DFT, Offline GRPO, and DPO, when applied to a shared set of math rollouts from a single base model, Qwen3-4B. The authors employ a consistent experimental setup, utilizing attention-only LoRA for weight updates, to ensure a fair comparison. The analysis is conducted across two distinct datasets: GSM8K and AIME26. The core methodology revolves around analyzing the cosine similarity, principal-angle subspace analysis, linear mode connectivity, and Centered Kernel Alignment (CKA) of the resulting weight deltas. The key empirical finding is that SFT, RFT, and RIFT exhibit nearly identical weight deltas, while DFT diverges more significantly in direction. Offline GRPO's weight delta is found to be orthogonal to that of SFT, suggesting a substantial departure from the direction of the SFT update. DPO, while achieving the highest accuracy on the two datasets, has a weight delta that is also orthogonal to SFT, though not as strongly as Offline GRPO. The authors also note that DPO uses a smaller learning rate than other methods, which they acknowledge complicates a direct causal interpretation of the results. Overall, the paper suggests that the primary difference between the losses lies in the direction of the weight update, rather than the magnitude, and that DPO's performance may be linked to its orthogonal update direction. The study provides valuable insights into the mechanisms behind these methods, highlighting the importance of weight-space analysis in understanding the behavior of offline reasoning loss functions. However, the study is limited by its narrow scope, which focuses on a single base model and a specific task domain, and by its lack of discussion of the potential limitations of using LoRA for weight updates. Despite these limitations, the paper offers a controlled and detailed analysis of the weight-space differences between these methods, which is a valuable contribution to the field.


## Soundness:

2.75


## Presentation:

3.0


## Contribution:

2.0


## Strengths:

This paper's primary strength lies in its controlled experimental design, which allows for a detailed comparison of the weight-space changes induced by different offline reasoning loss functions. By using identical math rollouts, a shared base model, and consistent LoRA initialization, the authors have created a clean environment for isolating the effects of the different loss functions. This approach is commendable as it minimizes confounding factors and allows for a more precise analysis of the weight updates. The use of multiple analysis techniques, including cosine similarity, principal-angle subspace analysis, linear mode connectivity, and CKA, provides a comprehensive view of the weight-space differences. This multi-faceted approach strengthens the validity of the findings and offers a more nuanced understanding of the weight-space changes. Furthermore, the paper clearly communicates its key takeaways, such as the near-identical weight deltas for SFT, RFT, and RIFT, and the significant divergence of DFT. The authors also acknowledge the smaller learning rate used by DPO, which is a sign of awareness of the nuances of the results. The paper's focus on weight-space analysis is a valuable contribution to the field, as it provides a deeper understanding of the mechanisms behind these methods. The authors have successfully demonstrated that the primary difference between the losses lies in the direction of the weight update, rather than the magnitude, which is a significant finding. The paper is also well-written and easy to follow, making it accessible to a broad audience. The authors have clearly articulated their methodology and findings, which facilitates the understanding of the study's contributions. The inclusion of multiple analysis techniques and the clear communication of key findings make this paper a valuable contribution to the field of offline reasoning loss functions.


## Weaknesses:

While this paper presents a valuable analysis of weight-space changes, several limitations warrant careful consideration. First, the study's scope is limited by the use of a single base model, Qwen3-4B, and a specific task domain, namely math reasoning. As I have verified, the paper explicitly states that all methods share the same base model and that the experiments are conducted on math rollouts. This narrow scope raises concerns about the generalizability of the findings to other models and tasks. The conclusions drawn from this specific setup may not hold true for models with different architectures or for tasks with different characteristics. For instance, models with different pre-training objectives or those trained on datasets with varying levels of noise could exhibit different weight update patterns under the same loss functions. This limitation significantly restricts the broader applicability of the conclusions. Second, the paper does not provide a clear explanation of why DPO has a near-orthogonal subspace to SFT. While the paper observes this phenomenon, it does not delve into the reasons behind it or discuss the potential implications for DPO's performance. As I have confirmed, the paper states that DPO is orthogonal to SFT, RFT, and RIFT, but it does not explain why this orthogonality exists or what it means for the loss landscape. This lack of explanation weakens the understanding of DPO's behavior and its relationship to other methods. Furthermore, the paper does not discuss the potential for DPO to explore different regions of the loss landscape, which could lead to improved generalization or robustness. This is a significant oversight, as understanding the exploration capabilities of different methods is crucial for practical applications. Third, the paper does not discuss the potential limitations of using LoRA for weight updates. While LoRA is a popular technique for efficient fine-tuning, it may not be suitable for all types of reasoning tasks or models. The paper uses LoRA consistently across all methods without acknowledging its limitations. As I have verified, the paper states that it uses LoRA on attention projections with a specific rank and learning rate, but it does not discuss the potential limitations of this approach. This omission leaves a gap in understanding the scope and potential biases of the findings. For example, LoRA might not be able to effectively modify certain layers or its rank might limit the model's capacity to learn complex relationships. Finally, the paper lacks a detailed analysis of the computational cost associated with each method. This information is crucial for practitioners who need to choose the most efficient method for their specific needs. The paper provides details about the hardware and software environment, but it does not include a detailed analysis of training time, memory usage, or the number of parameters involved in each method. As I have confirmed, the paper does not provide a detailed analysis of computational costs, which makes it difficult to assess the practical trade-offs between the different methods. These limitations, taken together, significantly impact the generalizability and practical applicability of the paper's findings.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the study should be extended to include a more diverse set of base models and tasks. This would help to establish the generalizability of the findings and identify potential limitations of the observed weight update patterns. For example, the authors could consider evaluating the methods on models with different architectures, such as encoder-decoder models or models with different pre-training objectives. Additionally, the study could be extended to include tasks beyond math reasoning, such as natural language understanding or text generation. This would provide a more comprehensive understanding of how the different loss functions affect the weight updates in various contexts. Furthermore, it would be beneficial to investigate the impact of different hyperparameters, such as learning rate and batch size, on the observed weight update patterns. This would help to identify the optimal settings for each method and provide a more nuanced understanding of their behavior. Second, to address the lack of explanation for the near-orthogonality of DPO to SFT, the authors should conduct a more thorough investigation into the behavior of DPO's weight updates. This could involve analyzing the loss landscape around the SFT and DPO solutions to understand why DPO's updates are so different. This could involve visualizing the loss surface or computing the Hessian of the loss function at both points. Furthermore, the paper should explore whether the near-orthogonality is a consistent phenomenon across different tasks and datasets. It would be valuable to see if this behavior is specific to the math reasoning tasks used in the paper or if it generalizes to other types of reasoning problems. The authors could also investigate whether DPO's updates lead to a different exploration of the weight space, potentially explaining its superior performance on certain tasks. This could involve analyzing the trajectory of the weight updates during training or comparing the final weight distributions of DPO and other methods. Third, the authors should consider exploring alternative fine-tuning techniques beyond LoRA. While LoRA is computationally efficient, it may not be the most suitable method for all reasoning tasks. The paper should discuss the potential limitations of using LoRA, such as its inability to modify certain layers or its rank limitation on the model's capacity. The authors could also investigate the impact of different LoRA configurations on the weight updates and the resulting performance. For example, they could vary the rank of the LoRA matrices or the number of trainable parameters. This would provide a more comprehensive understanding of how LoRA affects the behavior of different offline reasoning loss functions. Furthermore, the authors could explore other parameter-efficient fine-tuning techniques, such as adapter layers or prefix tuning, to see if they lead to different results. This would help to determine whether the observed differences between the loss functions are specific to LoRA or if they are more generalizable. Finally, the paper should include a detailed comparison of the training time, memory usage, and the number of parameters involved in each method. This analysis should be conducted on the same hardware and with the same datasets to ensure a fair comparison. The authors should also discuss the trade-offs between the different methods in terms of computational cost and performance. For example, they could analyze the relationship between the computational cost and the accuracy of each method. This would help practitioners to choose the most appropriate method for their specific needs. Furthermore, the authors should consider the impact of batch size and learning rate on the computational cost of each method. This would provide a more complete picture of the practical implications of using each method.


## Questions:

Several key questions arise from my analysis of this paper. First, what are the potential limitations of using LoRA for weight updates, and how might these limitations affect the results? The paper does not discuss the potential limitations of using LoRA, such as its inability to modify certain layers or its rank limitation on the model's capacity. A more detailed discussion of these limitations and their potential impact on the results would be valuable. Second, how does the near-orthogonality of DPO to SFT affect its performance compared to other methods? The paper does not provide a clear explanation of why DPO has a near-orthogonal subspace to SFT, nor does it discuss the potential implications for its performance. A more detailed analysis of this phenomenon and its impact on DPO's performance would be beneficial. Third, are the observed differences in weight-space changes consistent across different tasks and datasets, or are they specific to the math reasoning tasks used in the paper? The paper focuses on math reasoning tasks, and it is unclear whether the observed differences in weight-space changes would generalize to other tasks and datasets. A more thorough investigation into the generalizability of these findings would be valuable. Fourth, what are the potential practical implications of the observed weight-space differences for the practical application of these methods? The paper does not discuss how the near-orthogonality of DPO to SFT might affect its robustness to adversarial attacks or its ability to generalize to out-of-distribution data. A more detailed analysis of the practical implications of the weight-space differences would be valuable for researchers and practitioners who are interested in applying these methods to real-world problems. Finally, what are the potential limitations of using a single base model and a specific task domain for this study? The paper uses a single base model, Qwen3-4B, and focuses on math reasoning tasks. It is unclear whether the observed differences in weight-space changes would generalize to other models and tasks. A more detailed discussion of the limitations of the study and the potential biases of the findings would be valuable.


## Rating:

5.25


## Confidence:

3.5


## Decision:

Reject
}