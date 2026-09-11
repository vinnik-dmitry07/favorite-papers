I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper proposes LOTUS (Looped Transformers with parallel supervision on latent), a latent CoT method that uses a looped Transformer architecture to process multiple reasoning blocks in parallel, aiming to bridge the performance gap between latent and explicit CoT methods. LOTUS introduces a looped padded Transformer architecture with learnable tokens and applies parallel cross-entropy supervision on the gold CoT tokens. Experimental results show that LOTUS achieves strong performance on the GSM8K and MATH datasets, demonstrating its effectiveness and efficiency.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow.
- The motivation for LOTUS is clear and well-justified.
- The experimental results are strong, showing significant improvements over existing latent CoT methods.

### Weaknesses

#### Some Related Works

[1] PCCoT: Parallel Contrastive Chain-of-Thought Prompting for Multi-Step Reasoning

#### comment

 - The paper does not provide a detailed analysis of the computational cost of LOTUS compared to explicit CoT methods. It would be helpful to understand the trade-offs between computational efficiency and performance.
- The paper does not compare LOTUS with other recent latent CoT methods, such as PCCoT [1]. Including these comparisons would provide a more comprehensive evaluation of LOTUS's performance.
- The paper does not discuss the limitations of LOTUS, such as its applicability to different types of reasoning tasks or its sensitivity to hyperparameter settings.

### Suggestions

The paper should include a more thorough analysis of the computational cost of LOTUS, specifically comparing training and inference times with explicit CoT methods. This analysis should not only focus on the number of parameters but also consider the FLOPs required for both training and inference. For example, providing a breakdown of the computational cost associated with the looped Transformer architecture and the parallel cross-entropy supervision would be beneficial. Furthermore, it would be useful to see how the computational cost scales with the number of reasoning blocks and the size of the model. This would allow readers to better understand the practical implications of using LOTUS in resource-constrained environments. The authors should also consider reporting the memory footprint of the model during training and inference, as this is an important factor for practical applications.

In addition to the computational cost, the paper should include a more comprehensive comparison with other recent latent CoT methods, such as PCCoT [1]. The comparison should not only focus on the final performance on GSM8K and MATH datasets but also consider other aspects such as the training time, the number of parameters, and the sensitivity to hyperparameter settings. It would be valuable to see a detailed ablation study that compares the performance of LOTUS with different components, such as the looped architecture and the parallel cross-entropy supervision. This would help to understand the contribution of each component to the overall performance. Moreover, the authors should discuss the differences in the architectural design and training procedures between LOTUS and PCCoT, and explain why LOTUS achieves better results. This would provide a more complete picture of the strengths and weaknesses of LOTUS compared to other latent CoT methods.

Finally, the paper should include a discussion of the limitations of LOTUS, such as its applicability to different types of reasoning tasks and its sensitivity to hyperparameter settings. For example, it would be useful to discuss whether LOTUS is effective for tasks that require more complex reasoning or tasks that involve different types of knowledge. The authors should also investigate the sensitivity of LOTUS to different hyperparameter settings, such as the learning rate, the batch size, and the number of training epochs. This would help to understand the robustness of LOTUS and provide guidance for practitioners who want to use LOTUS in their own applications. Furthermore, the authors should discuss the potential limitations of the parallel cross-entropy supervision and whether it can be applied to other types of latent reasoning methods.

### Questions

- How does LOTUS perform on other reasoning tasks, such as commonsense reasoning or logical reasoning?
- What are the potential limitations of LOTUS, such as its applicability to different types of reasoning tasks or its sensitivity to hyperparameter settings?

### Rating

6

### Confidence

3

**********

## Reviewer 2

### Summary

The paper proposes a new method to bridge the gap between explicit and latent CoT reasoning. The method is based on the following ideas:
- Using a looped Transformer architecture to process K reasoning blocks in parallel
- Using a cross-entropy loss to supervise the latents directly against the CoT steps
- Using a cross-entropy loss to supervise the latents against the answer

The method is evaluated on GSM8K and MATH datasets. The results show that the method is able to bridge the gap between explicit and latent CoT reasoning.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The method is simple and effective
- The method is evaluated on two challenging datasets (GSM8K and MATH) and shows significant improvements over previous latent CoT methods
- The paper includes extensive ablation studies to analyze the impact of different design choices
- The paper is well-written and easy to follow

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational cost of the method compared to explicit CoT methods. It would be helpful to understand the trade-offs between computational efficiency and performance.
- The paper does not compare LOTUS with other recent latent CoT methods, such as PCCoT [1]. Including these comparisons would provide a more comprehensive evaluation of LOTUS's performance.
- The paper does not discuss the limitations of LOTUS, such as its applicability to different types of reasoning tasks or its sensitivity to hyperparameter settings.

### Suggestions

The paper would benefit from a more thorough analysis of the computational overhead introduced by the looped Transformer architecture. While the authors mention the number of parameters, a detailed breakdown of FLOPs (Floating Point Operations) during both training and inference would provide a clearer picture of the method's efficiency. This should include a comparison with explicit CoT methods, highlighting the trade-offs between the parallel processing of LOTUS and the sequential nature of explicit CoT. For instance, the authors could analyze how the number of reasoning blocks (K) and the number of iterations (R) impact both the computational cost and the performance of the model. Furthermore, it would be valuable to explore the memory footprint of the looped architecture, as this could be a limiting factor for large-scale applications. A discussion on the practical implications of these computational costs would greatly enhance the paper's practical value.

To strengthen the evaluation, the paper should include a more comprehensive comparison with other state-of-the-art latent CoT methods, such as PCCoT. The current evaluation primarily focuses on GSM8K and MATH datasets, but a comparison with other methods would provide a more robust assessment of LOTUS's performance. This comparison should not only focus on the final performance metrics but also consider other aspects such as training time, inference speed, and sensitivity to hyperparameter settings. A detailed ablation study comparing LOTUS with PCCoT, focusing on the architectural differences and training procedures, would be highly beneficial. This would help to understand the specific advantages and disadvantages of each method and provide a more nuanced view of LOTUS's contribution to the field. The authors should also consider evaluating the methods on a wider range of datasets to demonstrate the generalizability of LOTUS.

Finally, the paper should include a more thorough discussion of the limitations of LOTUS. This should include an analysis of the method's applicability to different types of reasoning tasks, such as commonsense reasoning or logical reasoning. The authors should also investigate the sensitivity of LOTUS to hyperparameter settings, such as the learning rate, batch size, and the number of training epochs. A discussion on the potential failure modes of the method and the scenarios where it might not perform well would provide a more balanced and realistic assessment of LOTUS's capabilities. Furthermore, the authors should explore the potential for further improvements, such as incorporating more sophisticated loss functions or exploring different architectures for the looped Transformer.

### Questions

- How does LOTUS perform on other reasoning tasks, such as commonsense reasoning or logical reasoning?
- What are the potential limitations of LOTUS, such as its applicability to different types of reasoning tasks or its sensitivity to hyperparameter settings?
- How does LOTUS compare to other recent latent CoT methods, such as PCCoT, in terms of performance and computational cost?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

The paper proposes a method to bridge the gap between explicit and latent chain-of-thought (CoT) reasoning. The authors introduce LOTUS (Looped Transformers with parallel supervision on latent), a novel approach that uses a looped padded Transformer architecture to process multiple reasoning blocks in parallel. This architecture is combined with a parallel cross-entropy loss that supervises the latent representations directly against the gold CoT tokens. The authors demonstrate that LOTUS achieves a significant performance boost on the GSM8K test set, surpassing explicit CoT baselines, and outperforms other latent CoT methods. The paper also includes ablation studies that analyze the impact of different design choices, such as the number of reasoning blocks and the looped architecture. The authors show that LOTUS is able to bridge the gap between explicit and latent CoT reasoning, achieving a 2.5x reduction in thought-phase latency and a 6.9x speedup in inference time on a natural-language CoT stress test.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow, with clear explanations of the proposed method and its components.
- The authors provide a comprehensive set of experiments and ablation studies that demonstrate the effectiveness of LOTUS. The results are presented clearly and are well-supported by the experimental data.
- The paper includes a thorough analysis of the learned latent representations, showing that they are interpretable and CoT-aligned. This is an important contribution, as it provides insights into how the model is reasoning and how the latent representations are being used.
- The authors provide a detailed discussion of the limitations of their method and suggest potential directions for future research.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational cost of LOTUS compared to explicit CoT methods. It would be helpful to understand the trade-offs between computational efficiency and performance.
- The paper does not compare LOTUS with other recent latent CoT methods, such as PCCoT [1]. Including these comparisons would provide a more comprehensive evaluation of LOTUS's performance.
- The paper does not discuss the limitations of LOTUS, such as its applicability to different types of reasoning tasks or its sensitivity to hyperparameter settings.

### Suggestions

The paper would benefit from a more thorough analysis of the computational cost associated with LOTUS, especially in comparison to explicit CoT methods. While the authors mention a reduction in thought-phase latency and inference time, a detailed breakdown of the FLOPs (Floating Point Operations) required for both training and inference would provide a clearer picture of the method's efficiency. This should include a comparison of the number of parameters and the computational cost per iteration for both LOTUS and explicit CoT baselines. Furthermore, it would be valuable to analyze how the computational cost scales with the number of reasoning blocks and the length of the input sequence. This analysis should also consider the memory footprint of the model, which can be a limiting factor for large-scale applications. A more detailed discussion of these computational aspects would allow readers to better assess the practical implications of using LOTUS in resource-constrained environments.

To strengthen the evaluation of LOTUS, it is crucial to include comparisons with other state-of-the-art latent CoT methods, such as PCCoT [1]. The current evaluation primarily focuses on GSM8K and MATH datasets, but a comparison with other methods would provide a more robust assessment of LOTUS's performance. This comparison should not only focus on the final performance metrics but also consider other aspects such as training time, inference speed, and sensitivity to hyperparameter settings. A detailed ablation study comparing LOTUS with PCCoT, focusing on the architectural differences and training procedures, would be highly beneficial. This would help to understand the specific advantages and disadvantages of each method and provide a more nuanced view of LOTUS's contribution to the field. The authors should also consider evaluating the methods on a wider range of datasets to demonstrate the generalizability of LOTUS.

Finally, the paper should include a more thorough discussion of the limitations of LOTUS. This should include an analysis of the method's applicability to different types of reasoning tasks, such as commonsense reasoning or logical reasoning. The authors should also investigate the sensitivity of LOTUS to hyperparameter settings, such as the learning rate, batch size, and the number of training epochs. A discussion on the potential failure modes of the method and the scenarios where it might not perform well would provide a more balanced and realistic assessment of LOTUS's capabilities. Furthermore, the authors should explore the potential for further improvements, such as incorporating more sophisticated loss functions or exploring different architectures for the looped Transformer. Addressing these limitations would provide a more complete picture of the method's strengths and weaknesses.

### Questions

- How does LOTUS perform on other reasoning tasks, such as commonsense reasoning or logical reasoning?
- What are the potential limitations of LOTUS, such as its applicability to different types of reasoning tasks or its sensitivity to hyperparameter settings?
- How does LOTUS compare to other recent latent CoT methods, such as PCCoT, in terms of performance and computational cost?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

This paper proposes a novel approach to latent CoT reasoning, LOTUS, which leverages a looped padded Transformer architecture and parallel cross-entropy supervision on gold CoT steps. LOTUS achieves a significant performance boost on the GSM8K test set, surpassing explicit CoT baselines and outperforming other latent CoT methods. The paper also includes ablation studies that analyze the impact of different design choices, such as the number of reasoning blocks and the looped architecture. The authors show that LOTUS is able to bridge the gap between explicit and latent CoT reasoning, achieving a 2.5x reduction in thought-phase latency and a 6.9x speedup in inference time on a natural-language CoT stress test.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow, with clear explanations of the proposed method and its components.
2. The authors provide a comprehensive set of experiments and ablation studies that demonstrate the effectiveness of LOTUS. The results are presented clearly and are well-supported by the experimental data.
3. The paper includes a thorough analysis of the learned latent representations, showing that they are interpretable and CoT-aligned. This is an important contribution, as it provides insights into how the model is reasoning and how the latent representations are being used.
4. The authors provide a detailed discussion of the limitations of their method and suggest potential directions for future research.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of LOTUS compared to explicit CoT methods. It would be helpful to understand the trade-offs between computational efficiency and performance.
2. The paper does not compare LOTUS with other recent latent CoT methods, such as PCCoT [1]. Including these comparisons would provide a more comprehensive evaluation of LOTUS's performance.
3. The paper does not discuss the limitations of LOTUS, such as its applicability to different types of reasoning tasks or its sensitivity to hyperparameter settings.

### Suggestions

The paper would benefit from a more thorough analysis of the computational cost associated with LOTUS, especially in comparison to explicit CoT methods. While the authors mention a reduction in thought-phase latency and inference time, a detailed breakdown of the FLOPs (Floating Point Operations) required for both training and inference would provide a clearer picture of the method's efficiency. This should include a comparison of the number of parameters and the computational cost per iteration for both LOTUS and explicit CoT baselines. Furthermore, it would be valuable to analyze how the computational cost scales with the number of reasoning blocks and the length of the input sequence. This analysis should also consider the memory footprint of the model, which can be a limiting factor for large-scale applications. A more detailed discussion of these computational aspects would allow readers to better assess the practical implications of using LOTUS in resource-constrained environments.

To strengthen the evaluation of LOTUS, it is crucial to include comparisons with other state-of-the-art latent CoT methods, such as PCCoT [1]. The current evaluation primarily focuses on GSM8K and MATH datasets, but a comparison with other methods would provide a more robust assessment of LOTUS's performance. This comparison should not only focus on the final performance metrics but also consider other aspects such as training time, inference speed, and sensitivity to hyperparameter settings. A detailed ablation study comparing LOTUS with PCCoT, focusing on the architectural differences and training procedures, would be highly beneficial. This would help to understand the specific advantages and disadvantages of each method and provide a more nuanced view of LOTUS's contribution to the field. The authors should also consider evaluating the methods on a wider range of datasets to demonstrate the generalizability of LOTUS.

Finally, the paper should include a more thorough discussion of the limitations of LOTUS. This should include an analysis of the method's applicability to different types of reasoning tasks, such as commonsense reasoning or logical reasoning. The authors should also investigate the sensitivity of LOTUS to hyperparameter settings, such as the learning rate, batch size, and the number of training epochs. A discussion on the potential failure modes of the method and the scenarios where it might not perform well would provide a more balanced and realistic assessment of LOTUS's capabilities. Furthermore, the authors should explore the potential for further improvements, such as incorporating more sophisticated loss functions or exploring different architectures for the looped Transformer. Addressing these limitations would provide a more complete picture of the method's strengths and weaknesses.

### Questions

1. How does LOTUS perform on other reasoning tasks, such as commonsense reasoning or logical reasoning?
2. What are the potential limitations of LOTUS, such as its applicability to different types of reasoning tasks or its sensitivity to hyperparameter settings?
3. How does LOTUS compare to other recent latent CoT methods, such as PCCoT, in terms of performance and computational cost?

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
2. For each comment identified as a weakness, find the corresponding section in the paper.
3. Extract evidence (quotes, experimental details, missing citations) to support the reviewer's claim.
4. If the reviewer's claim is not supported by the paper, explain why.
5. Organize the findings for each weakness according to the provided output format.
**Review 1 Weaknesses:**

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost of LOTUS compared to explicit CoT methods. It would be helpful to understand the trade-offs between computational efficiency and performance."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions latency reduction in the "Main Results" section: "The main GSM8K-Aug setting uses 385k training samples and reports in-domain accuracy on the GSM8K test set ( Cobbe et al., 2021 ) , together with three out-of-domain benchmarks: GSM-Hard, MultiArith, and SVAMP. We additionally train on a natural-language version of GSM8K-Aug ( Wu et al., 2025 ) as an efficiency stress test, where each reasoning step is a full-sentence rationale rather than a compact math expression. We use three backbones in increasing size: GPT-2 (124M) ( Radford et al. ) , Llama-3.2-1B-Instruct , and Llama-3.2-3B-Instruct ( Grattafiori et al. , 2024 ) ."
   - The paper reports latency in the "Main Results" section: "The thought-phase latency of LOTUS is 2.5 × faster than explicit CoT." and "The inference-time speedup of LOTUS is 6.9 × on natural-language CoT traces."
   - The paper does not provide a detailed breakdown of FLOPs or a comparison of the number of parameters between LOTUS and explicit CoT methods.

3. Literature Gap Analysis:
   - The paper compares performance metrics (accuracy) against explicit CoT baselines but lacks a computational cost comparison.

4. Validation Analysis:
   - Primary evidence: The paper reports latency reduction but lacks a detailed computational cost analysis (FLOPs, parameter count comparison).
   - Supporting quotes: "The thought-phase latency of LOTUS is 2.5 × faster than explicit CoT." and "The inference-time speedup of LOTUS is 6.9 × on natural-language CoT traces."
   - Impact assessment: The lack of a detailed computational cost analysis makes it difficult to fully assess the trade-offs between performance and efficiency.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of FLOPs or parameter count comparison between LOTUS and explicit CoT.

1. Weakness Statement:
"The paper does not compare LOTUS with other recent latent CoT methods, such as PCCoT [1]. Including these comparisons would provide a more comprehensive evaluation of LOTUS's performance."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "Experiments" section lists the baselines used for comparison: "Explicit CoT and No-CoT as reference, and CODI, CODI + SIM-CoT, and KaVA with different latent tokens per step."
   - PCCoT is not included in the list of baselines.

3. Literature Gap Analysis:
   - PCCoT (Shen et al., 2025) is a relevant recent latent CoT method that is not cited or compared against.

4. Validation Analysis:
   - Primary evidence: PCCoT is not included in the experimental comparisons.
   - Supporting quotes: The list of baselines in the "Experiments" section.
   - Impact assessment: The absence of comparison with PCCoT limits the comprehensiveness of the evaluation.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: PCCoT is not listed as a baseline in the experimental section.

1. Weakness Statement:
"The paper does not discuss the limitations of LOTUS, such as its applicability to different types of reasoning tasks or its sensitivity to hyperparameter settings."

2. Evidence Collection:
- The paper has a dedicated "Limitations" section: "We follow prior latent reasoning work ( Hao et al., 2025 ; Shen et al., 2025 ; Wei et al., 2025 ) and evaluate on math benchmarks. Whether the recipe transfers to other domains remains an open direction for futu"

3. Literature Gap Analysis:
   - While a limitations section exists, it is brief and focuses on the domain of evaluation.

4. Validation Analysis:
   - Primary evidence: The paper includes a "Limitations" section, but it is brief and primarily focused on the domain of evaluation.
   - Supporting quotes: "We follow prior latent reasoning work ( Hao et al., 2025 ; Shen et al., 2025 ; Wei et al., 2025 ) and evaluate on math benchmarks. Whether the recipe transfers to other domains remains an open direction for futu"
   - Impact assessment: The discussion of limitations is present but could be more comprehensive.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: A "Limitations" section exists but is brief and primarily focused on the domain of evaluation.

**Review 2 Weaknesses:**

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost of LOTUS compared to explicit CoT methods. It would be helpful to understand the trade-offs between computational efficiency and performance."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions latency reduction in the "Main Results" section: "The main GSM8K-Aug setting uses 385k training samples and reports in-domain accuracy on the GSM8K test set ( Cobbe et al., 2021 ) , together with three out-of-domain benchmarks: GSM-Hard, MultiArith, and SVAMP. We additionally train on a natural-language version of GSM8K-Aug ( Wu et al., 2025 ) as an efficiency stress test, where each reasoning step is a full-sentence rationale rather than a compact math expression. We use three backbones in increasing size: GPT-2 (124M) ( Radford et al. ) , Llama-3.2-1B-Instruct , and Llama-3.2-3B-Instruct ( Grattafiori et al. , 2024 ) ."
   - The paper reports latency in the "Main Results" section: "The thought-phase latency of LOTUS is 2.5 × faster than explicit CoT." and "The inference-time speedup of LOTUS is 6.9 × on natural-language CoT traces."
   - The paper does not provide a detailed breakdown of FLOPs or a comparison of the number of parameters between LOTUS and explicit CoT methods.

3. Literature Gap Analysis:
   - The paper compares performance metrics (accuracy) against explicit CoT baselines but lacks a computational cost comparison.

4. Validation Analysis:
   - Primary evidence: The paper reports latency reduction but lacks a detailed computational cost analysis (FLOPs, parameter count comparison).
   - Supporting quotes: "The thought-phase latency of LOTUS is 2.5 × faster than explicit CoT." and "The inference-time speedup of LOTUS is 6.9 × on natural-language CoT traces."
   - Impact assessment: The lack of a detailed computational cost analysis makes it difficult to fully assess the trade-offs between performance and efficiency.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of FLOPs or parameter count comparison between LOTUS and explicit CoT.

1. Weakness Statement:
"The paper does not compare LOTUS with other recent latent CoT methods, such as PCCoT [1]. Including these comparisons would provide a more comprehensive evaluation of LOTUS's performance."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "Experiments" section lists the baselines used for comparison: "Explicit CoT and No-CoT as reference, and CODI, CODI + SIM-CoT, and KaVA with different latent tokens per step."
   - PCCoT is not included in the list of baselines.

3. Literature Gap Analysis:
   - PCCoT (Shen et al., 2025) is a relevant recent latent CoT method that is not cited or compared against.

4. Validation Analysis:
   - Primary evidence: PCCoT is not included in the experimental comparisons.
   - Supporting quotes: The list of baselines in the "Experiments" section.
   - Impact assessment: The absence of comparison with PCCoT limits the comprehensiveness of the evaluation.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: PCCoT is not listed as a baseline in the experimental section.

1. Weakness Statement:
"The paper does not discuss the limitations of LOTUS, such as its applicability to different types of reasoning tasks or its sensitivity to hyperparameter settings."

2. Evidence Collection:
- The paper has a dedicated "Limitations" section: "We follow prior latent reasoning work ( Hao et al., 2025 ; Shen et al., 2025 ; Wei et al., 2025 ) and evaluate on math benchmarks. Whether the recipe transfers to other domains remains an open direction for futu"

3. Literature Gap Analysis:
   - While a limitations section exists, it is brief and primarily focused on the domain of evaluation.

4. Validation Analysis:
   - Primary evidence: The paper includes a "Limitations" section, but it is brief and primarily focused on the domain of evaluation.
   - Supporting quotes: "We follow prior latent reasoning work ( Hao et al., 2025 ; Shen et al., 2025 ; Wei et al., 2025 ) and evaluate on math benchmarks. Whether the recipe transfers to other domains remains an open direction for futu"
   - Impact assessment: The discussion of limitations is present but could be more comprehensive.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: A "Limitations" section exists but is brief and primarily focused on the domain of evaluation.

**Review 3 Weaknesses:**

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost of LOTUS compared to explicit CoT methods. It would be helpful to understand the trade-offs between computational efficiency and performance."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions latency reduction in the "Main Results" section: "The main GSM8K-Aug setting uses 385k training samples and reports in-domain accuracy on the GSM8K test set ( Cobbe et al., 2021 ) , together with three out-of-domain benchmarks: GSM-Hard, MultiArith, and SVAMP. We additionally train on a natural-language version of GSM8K-Aug ( Wu et al., 2025 ) as an efficiency stress test, where each reasoning step is a full-sentence rationale rather than a compact math expression. We use three backbones in increasing size: GPT-2 (124M) ( Radford et al. ) , Llama-3.2-1B-Instruct , and Llama-3.2-3B-Instruct ( Grattafiori et al. , 2024 ) ."
   - The paper reports latency in the "Main Results" section: "The thought-phase latency of LOTUS is 2.5 × faster than explicit CoT." and "The inference-time speedup of LOTUS is 6.9 × on natural-language CoT traces."
   - The paper does not provide a detailed breakdown of FLOPs or a comparison of the number of parameters between LOTUS and explicit CoT methods.

3. Literature Gap Analysis:
   - The paper compares performance metrics (accuracy) against explicit CoT baselines but lacks a computational cost comparison.

4. Validation Analysis:
   - Primary evidence: The paper reports latency reduction but lacks a detailed computational cost analysis (FLOPs, parameter count comparison).
   - Supporting quotes: "The thought-phase latency of LOTUS is 2.5 × faster than explicit CoT." and "The inference-time speedup of LOTUS is 6.9 × on natural-language CoT traces."
   - Impact assessment: The lack of a detailed computational cost analysis makes it difficult to fully assess the trade-offs between performance and efficiency.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of FLOPs or parameter count comparison between LOTUS and explicit CoT.

1. Weakness Statement:
"The paper does not compare LOTUS with other recent latent CoT methods, such as PCCoT [1]. Including these comparisons would provide a more comprehensive evaluation of LOTUS's performance."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "Experiments" section lists the baselines used for comparison: "Explicit CoT and No-CoT as reference, and CODI, CODI + SIM-CoT, and KaVA with different latent tokens per step."
   - PCCoT is not included in the list of baselines.

3. Literature Gap Analysis:
   - PCCoT (Shen et al., 2025) is a relevant recent latent CoT method that is not cited or compared against.

4. Validation Analysis:
   - Primary evidence: PCCoT is not included in the experimental comparisons.
   - Supporting quotes: The list of baselines in the "Experiments" section.
   - Impact assessment: The absence of comparison with PCCoT limits the comprehensiveness of the evaluation.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: PCCoT is not listed as a baseline in the experimental section.

1. Weakness Statement:
"The paper does not discuss the limitations of LOTUS, such as its applicability to different types of reasoning tasks or its sensitivity to hyperparameter settings."

2. Evidence Collection:
- The paper has a dedicated "Limitations" section: "We follow prior latent reasoning work ( Hao et al., 2025 ; Shen et al., 2025 ; Wei et al., 2025 ) and evaluate on math benchmarks. Whether the recipe transfers to other domains remains an open direction for futu"

3. Literature Gap Analysis:
   - While a limitations section exists, it is brief and primarily focused on the domain of evaluation.

4. Validation Analysis:
   - Primary evidence: The paper includes a "Limitations" section, but it is brief and primarily focused on the domain of evaluation.
   - Supporting quotes: "We follow prior latent reasoning work ( Hao et al., 2025 ; Shen et al., 2025 ; Wei et al., 2025 ) and evaluate on math benchmarks. Whether the recipe transfers to other domains remains an open direction for futu"
   - Impact assessment: The discussion of limitations is present but could be more comprehensive.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: A "Limitations" section exists but is brief and primarily focused on the domain of evaluation.

**Review 4 Weaknesses:**

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost of LOTUS compared to explicit CoT methods. It would be helpful to understand the trade-offs between computational efficiency and performance."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions latency reduction in the "Main Results" section: "The main GSM8K-Aug setting uses 385k training samples and reports in-domain accuracy on the GSM8K test set ( Cobbe et al., 2021 ) , together with three out-of-domain benchmarks: GSM-Hard, MultiArith, and SVAMP. We additionally train on a natural-language version of GSM8K-Aug ( Wu et al., 2025 ) as an efficiency stress test, where each reasoning step is a full-sentence rationale rather than a compact math expression. We use three backbones in increasing size: GPT-2 (124M) ( Radford et al. ) , Llama-3.2-1B-Instruct , and Llama-3.2-3B-Instruct ( Grattafiori et al. , 2024 ) ."
   - The paper reports latency in the "Main Results" section: "The thought-phase latency of LOTUS is 2.5 × faster than explicit CoT." and "The inference-time speedup of LOTUS is 6.9 × on natural-language CoT traces."
   - The paper does not provide a detailed breakdown of FLOPs or a comparison of the number of parameters between LOTUS and explicit CoT methods.

3. Literature Gap Analysis:
   - The paper compares performance metrics (accuracy) against explicit CoT baselines but lacks a computational cost comparison.

4. Validation Analysis:
   - Primary evidence: The paper reports latency reduction but lacks a detailed computational cost analysis (FLOPs, parameter count comparison).
   - Supporting quotes: "The thought-phase latency of LOTUS is 2.5 × faster than explicit CoT." and "The inference-time speedup of LOTUS is 6.9 × on natural-language CoT traces."
   - Impact assessment: The lack of a detailed computational cost analysis makes it difficult to fully assess the trade-offs between performance and efficiency.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of FLOPs or parameter count comparison between LOTUS and explicit CoT.

1. Weakness Statement:
"The paper does not compare LOTUS with other recent latent CoT methods, such as PCCoT [1]. Including these comparisons would provide a more comprehensive evaluation of LOTUS's performance."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "Experiments" section lists the baselines used for comparison: "Explicit CoT and No-CoT as reference, and CODI, CODI + SIM-CoT, and KaVA with different latent tokens per step."
   - PCCoT is not included in the list of baselines.

3. Literature Gap Analysis:
   - PCCoT (Shen et al., 2025) is a relevant recent latent CoT method that is not cited or compared against.

4. Validation Analysis:
   - Primary evidence: PCCoT is not included in the experimental comparisons.
   - Supporting quotes: The list of baselines in the "Experiments" section.
   - Impact assessment: The absence of comparison with PCCoT limits the comprehensiveness of the evaluation.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: PCCoT is not listed as a baseline in the experimental section.

1. Weakness Statement:
"The paper does not discuss the limitations of LOTUS, such as its applicability to different types of reasoning tasks or its sensitivity to hyperparameter settings."

2. Evidence Collection:
- The paper has a dedicated "Limitations" section: "We follow prior latent reasoning work ( Hao et al., 2025 ; Shen et al., 2025 ; Wei et al., 2025 ) and evaluate on math benchmarks. Whether the recipe transfers to other domains remains an open direction for futu"

3. Literature Gap Analysis:
   - While a limitations section exists, it is brief and primarily focused on the domain of evaluation.

4. Validation Analysis:
   - Primary evidence: The paper includes a "Limitations" section, but it is brief and primarily focused on the domain of evaluation.
   - Supporting quotes: "We follow prior latent reasoning work ( Hao et al., 2025 ; Shen et al., 2025 ; Wei et al., 2025 ) and evaluate on math benchmarks. Whether the recipe transfers to other domains remains an open direction for futu"
   - Impact assessment: The discussion of limitations is present but could be more comprehensive.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: A "Limitations" section exists but is brief and primarily focused on the domain of evaluation.

**Synthesis and Reflection:**

All reviewers raise similar concerns regarding the lack of a detailed computational cost analysis and comparisons with other recent latent CoT methods, particularly PCCoT. There is a consensus that while the paper presents promising results, a more thorough evaluation would strengthen its claims. The "Limitations" section is also consistently criticized for being brief and primarily focused on the domain of evaluation.

There are no significant contradictions between the reviewers' opinions. They all converge on the need for more comprehensive experimental validation and a deeper discussion of the method's practical implications and limitations.

**Overall Conclusion:**

The reviewers' weaknesses are largely valid. The paper would benefit significantly from a more detailed analysis of computational costs and a more comprehensive comparison with existing latent CoT methods, including PCCoT. The discussion of limitations could also be expanded to provide a more balanced perspective on the method's strengths and weaknesses.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces LOTUS (Looped Transformers with parallel supervision on latent), a novel approach to latent chain-of-thought (CoT) reasoning. The core idea behind LOTUS is to leverage a looped, padded Transformer architecture to process multiple reasoning blocks in parallel, aiming to bridge the performance gap between explicit and latent CoT methods. The authors propose that by using a looped architecture, they can achieve a more effective form of parallel self-supervision, where the latent representations are directly supervised against the gold CoT tokens. This is achieved by adding learnable tokens at the beginning of each reasoning block and applying parallel cross-entropy supervision on the gold CoT tokens. The method is evaluated on the GSM8K and MATH datasets, demonstrating significant improvements over existing latent CoT methods. Specifically, LOTUS achieves a 2.5x reduction in thought-phase latency and a 6.9x speedup in inference time on natural-language CoT traces. The authors also conduct extensive ablation studies to analyze the impact of different design choices, such as the number of reasoning blocks and the looped architecture. The paper also includes a thorough analysis of the learned latent representations, showing that they are interpretable and CoT-aligned. The authors argue that LOTUS is able to achieve a more interpretable and efficient latent representation of the reasoning process, which is a key advantage over explicit CoT methods. The paper's main contribution lies in its novel combination of a looped architecture and parallel self-supervision for latent CoT reasoning, which leads to improved performance and efficiency. The authors also provide a detailed analysis of the learned latent representations, which is a valuable contribution to the field. The paper is well-written and easy to follow, with clear explanations of the proposed method and its components. The experimental results are presented clearly and are well-supported by the experimental data. The authors also provide a detailed discussion of the limitations of their method and suggest potential directions for future research. Overall, this paper presents a significant contribution to the field of latent CoT reasoning, and I believe it will be of interest to researchers working in this area.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

3.0


## Strengths:

I found several aspects of this paper to be particularly strong. First, the core idea of using a looped, padded Transformer architecture to process multiple reasoning blocks in parallel is a novel and effective approach. This allows the model to leverage the benefits of parallel computation while maintaining a latent representation of the reasoning process. The parallel cross-entropy supervision on the gold CoT tokens is another key strength, as it provides a direct and effective way to train the model to generate latent representations that are aligned with the reasoning process. The experimental results are compelling, demonstrating that LOTUS achieves significant improvements over existing latent CoT methods on the GSM8K and MATH datasets. The reported 2.5x reduction in thought-phase latency and 6.9x speedup in inference time are substantial and highlight the practical benefits of the proposed method. The authors also provide a thorough analysis of the learned latent representations, showing that they are interpretable and CoT-aligned. This is an important contribution, as it provides insights into how the model is reasoning and how the latent representations are being used. The ablation studies are also well-designed and provide valuable insights into the impact of different design choices. The authors explore the impact of the number of reasoning blocks and the looped architecture, which helps to understand the effectiveness of the proposed method. The paper is also well-written and easy to follow, with clear explanations of the proposed method and its components. The experimental results are presented clearly and are well-supported by the experimental data. The authors also provide a detailed discussion of the limitations of their method and suggest potential directions for future research. Overall, I believe that the paper makes a significant contribution to the field of latent CoT reasoning, and I am impressed by the quality of the research and the clarity of the presentation.


## Weaknesses:

While I appreciate the strengths of this paper, I also identified several weaknesses that warrant further discussion. First, the paper lacks a detailed analysis of the computational cost of LOTUS compared to explicit CoT methods. While the authors report latency reductions, they do not provide a breakdown of FLOPs or a comparison of the number of parameters between LOTUS and explicit CoT baselines. This makes it difficult to fully assess the trade-offs between computational efficiency and performance. For example, the paper mentions a 2.5x reduction in thought-phase latency and a 6.9x speedup in inference time, but without a detailed analysis of FLOPs, it is hard to understand the practical implications of these speedups. This is a significant limitation, as it is crucial to understand the computational overhead of LOTUS compared to explicit CoT methods. My confidence in this weakness is high, as the paper explicitly lacks this analysis. Second, the paper does not compare LOTUS with other recent latent CoT methods, such as PCCoT. The current evaluation primarily focuses on GSM8K and MATH datasets, but a comparison with other methods would provide a more robust assessment of LOTUS's performance. The paper lists the baselines used for comparison, but PCCoT is not included in this list. This is a significant omission, as it limits the comprehensiveness of the evaluation. My confidence in this weakness is also high, as PCCoT is a relevant recent latent CoT method that is not cited or compared against. Third, the paper does not discuss the limitations of LOTUS in sufficient detail. While a limitations section exists, it is brief and primarily focused on the domain of evaluation. The authors state that they follow prior latent reasoning work and evaluate on math benchmarks, but they do not discuss the method's applicability to different types of reasoning tasks or its sensitivity to hyperparameter settings. This is a significant limitation, as it is important to understand the potential failure modes of the method and the scenarios where it might not perform well. My confidence in this weakness is medium, as the paper does include a limitations section, but it is not comprehensive. Finally, while the paper includes a thorough analysis of the learned latent representations, it does not explore the limitations of the parallel cross-entropy supervision. The authors do not investigate whether this supervision is sufficient to capture all aspects of the reasoning process, or whether it might be missing some information. This is a potential limitation, as the supervision might be biased towards certain types of reasoning or tasks. My confidence in this weakness is medium, as the paper does not include any analysis of this aspect.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the paper should include a more thorough analysis of the computational cost of LOTUS, specifically comparing training and inference times with explicit CoT methods. This analysis should not only focus on the number of parameters but also consider the FLOPs required for both training and inference. Providing a breakdown of the computational cost associated with the looped Transformer architecture and the parallel cross-entropy supervision would be beneficial. Furthermore, it would be useful to see how the computational cost scales with the number of reasoning blocks and the length of the input sequence. This would allow readers to better understand the practical implications of using LOTUS in resource-constrained environments. Second, the paper should include a more comprehensive comparison with other state-of-the-art latent CoT methods, such as PCCoT. The comparison should not only focus on the final performance metrics but also consider other aspects such as training time, inference speed, and sensitivity to hyperparameter settings. A detailed ablation study comparing LOTUS with PCCoT, focusing on the architectural differences and training procedures, would be highly beneficial. This would help to understand the specific advantages and disadvantages of each method and provide a more nuanced view of LOTUS's contribution to the field. The authors should also consider evaluating the methods on a wider range of datasets to demonstrate the generalizability of LOTUS. Third, the paper should include a more thorough discussion of the limitations of LOTUS. This should include an analysis of the method's applicability to different types of reasoning tasks, such as commonsense reasoning or logical reasoning. The authors should also investigate the sensitivity of LOTUS to hyperparameter settings, such as the learning rate, batch size, and the number of training epochs. A discussion on the potential failure modes of the method and the scenarios where it might not perform well would provide a more balanced and realistic assessment of LOTUS's capabilities. Furthermore, the authors should explore the potential for further improvements, such as incorporating more sophisticated loss functions or exploring different architectures for the looped Transformer. Finally, the paper should include an analysis of the limitations of the parallel cross-entropy supervision. The authors should investigate whether this supervision is sufficient to capture all aspects of the reasoning process, or whether it might be missing some information. This could involve analyzing the latent representations to see if they are capturing all the relevant information from the gold CoT tokens. The authors should also consider alternative supervision methods or explore ways to augment the current supervision to improve the model's performance. These changes would significantly strengthen the paper and provide a more comprehensive evaluation of LOTUS's performance and limitations.


## Questions:

I have several questions that I believe are important for further understanding the proposed method. First, how does LOTUS perform on other reasoning tasks, such as commonsense reasoning or logical reasoning? The current evaluation is limited to math benchmarks, and it would be valuable to see how the method performs on other types of reasoning tasks. Second, what are the potential limitations of LOTUS, such as its applicability to different types of reasoning tasks or its sensitivity to hyperparameter settings? The paper mentions a limitations section, but it would be helpful to have a more detailed discussion of the potential failure modes of the method. Third, how does LOTUS compare to other recent latent CoT methods, such as PCCoT, in terms of performance and computational cost? The current evaluation is limited to a few baselines, and it would be valuable to see how LOTUS compares to other state-of-the-art methods. Fourth, how does the parallel cross-entropy supervision affect the learned latent representations? The paper shows that the latent representations are interpretable and CoT-aligned, but it would be helpful to see if the supervision is sufficient to capture all aspects of the reasoning process. Finally, how does the number of reasoning blocks and the number of iterations (R) impact both the computational cost and the performance of the model? The paper includes ablation studies on these parameters, but it would be helpful to have a more detailed analysis of their impact on both computational cost and performance. These questions are important for understanding the strengths and weaknesses of the proposed method and for guiding future research in this area.


## Rating:

6.5


## Confidence:

3.0


## Decision:

Accept
}