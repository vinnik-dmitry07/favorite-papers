I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

The paper presents a novel approach called PoLar (Program-of-Layers) that allows large language models (LLMs) to dynamically adjust their execution paths during inference by skipping or repeating layers. This flexibility enables the model to tailor its computation to each input, potentially leading to more efficient and accurate results. The authors demonstrate that PoLar consistently outperforms standard inference and prior dynamic-depth methods across various mathematical reasoning benchmarks.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The concept of dynamically adjusting LLM execution paths is innovative and offers a new perspective on how models can adapt to different inputs.
- The paper provides extensive empirical evidence showing that PoLar improves accuracy over standard inference and other dynamic-depth methods, particularly on challenging mathematical reasoning tasks.
- PoLar operates without modifying the underlying LLM parameters, making it a practical solution that can be applied to existing models without retraining.

### Weaknesses

#### Some Related Works


#### comment

 - While the paper demonstrates improvements on mathematical reasoning tasks, it is unclear how well PoLar generalizes to other domains or types of tasks. Further evaluation on diverse datasets would strengthen the claims of broad applicability.
- The paper does not thoroughly explore the computational overhead associated with PoLar, especially in terms of inference time and memory usage. A detailed analysis of these factors would be valuable for practical deployment.
- The paper could benefit from a more in-depth discussion of the limitations of PoLar and potential failure cases. Understanding these aspects would provide a more balanced view of the approach.

### Suggestions

The authors should consider expanding their evaluation to include tasks beyond mathematical reasoning. While the current results are promising, it is crucial to demonstrate the general applicability of PoLar across different domains, such as natural language understanding, text generation, or code generation. For example, evaluating PoLar on datasets like GLUE or SuperGLUE, which cover a range of NLP tasks, would provide a more comprehensive understanding of its capabilities and limitations. Similarly, testing on code datasets like HumanEval would be valuable to assess its performance in a different domain. This broader evaluation would help to establish the robustness and versatility of the proposed approach and address concerns about its narrow focus on mathematical reasoning.

Furthermore, a more detailed analysis of the computational overhead of PoLar is necessary. The paper should provide a breakdown of the inference time, including the time spent on program selection and execution, and compare it to the baseline inference time of the original model. This analysis should also consider the memory usage of PoLar, especially during the program selection phase, as this could be a limiting factor for practical deployment. It would be beneficial to analyze how the inference time and memory usage scale with the complexity of the input and the length of the selected program. This detailed analysis would provide a more complete picture of the practical implications of using PoLar and help to identify potential bottlenecks for real-world applications. The authors should also explore potential optimizations to reduce the overhead of PoLar, such as caching or pruning techniques.

Finally, the paper should include a more thorough discussion of the limitations of PoLar and potential failure cases. While the current results are encouraging, it is important to acknowledge the scenarios where PoLar might not perform well. For example, it would be useful to investigate how PoLar behaves on inputs that require very deep or very shallow execution paths. The authors should also explore the sensitivity of PoLar to the choice of hyperparameters, such as the number of layers to skip or repeat. A detailed analysis of these limitations would provide a more balanced view of the approach and help to guide future research. Additionally, it would be beneficial to explore the interpretability of the selected programs, as this could provide insights into the reasoning process of the model and help to identify potential failure cases.

### Questions

- How does PoLar perform on tasks outside of mathematical reasoning? Are there specific domains where it excels or struggles?
- What is the computational overhead of PoLar compared to standard inference? How does it scale with input complexity?
- Are there any specific failure cases or scenarios where PoLar does not perform well? How can these be addressed?
- How sensitive is PoLar to the choice of hyperparameters, such as the number of layers to skip or repeat?

### Rating

6

### Confidence

3

**********

## Reviewer 2

### Summary

The paper proposes a method to improve the efficiency of LLM inference by dynamically skipping or repeating transformer layers based on the input. This approach, called PoLar (Program-of-Layers), allows the model to tailor its computation to each input, potentially reducing unnecessary computations and improving performance. The authors demonstrate that PoLar outperforms standard inference and prior dynamic-depth methods, particularly on challenging mathematical reasoning tasks. The method operates without modifying the underlying LLM parameters, making it a practical solution that can be applied to existing models without retraining.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach to inference-time computation control in LLMs, which is a significant contribution to the field. By allowing dynamic skipping or repeating of layers, the authors provide a flexible framework that can adapt to different inputs and tasks.
2. The authors provide extensive empirical evidence to support their claims. They conduct experiments on a range of mathematical reasoning benchmarks and demonstrate that PoLar consistently outperforms standard inference and prior dynamic-depth methods. The results are presented clearly and are well-supported by quantitative data.
3. The paper is well-written and easy to follow. The authors provide a clear explanation of the proposed method, including the technical details and the rationale behind their design choices. The use of figures and tables helps to illustrate the key concepts and results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational overhead associated with PoLar. While the authors claim that the method is efficient, they do not provide any quantitative data on the additional computational cost of the program-of-layers approach. This makes it difficult to assess the practical implications of the method, especially in resource-constrained environments. Specifically, the paper lacks a breakdown of the time spent on operations such as segment boundary determination, operation log-probability computation, and beam search, which are crucial for understanding the overall efficiency of the method. A comparison of the number of floating-point operations (FLOPs) or the actual runtime of PoLar versus standard inference would be beneficial.
2. The paper does not explore the robustness of PoLar to different types of inputs or tasks. While the authors demonstrate that the method works well on mathematical reasoning tasks, it is unclear how it would perform on other types of tasks, such as natural language understanding or text generation. The paper should include experiments on a wider range of tasks to assess the generalizability of the approach. For example, it would be useful to see how PoLar performs on tasks that require more complex reasoning or involve different types of data, such as code or images. The lack of such experiments limits the understanding of the method's applicability.
3. The paper does not provide a detailed analysis of the limitations of PoLar. While the authors acknowledge that the method may not be suitable for all types of tasks, they do not provide a thorough discussion of the scenarios where it might fail or underperform. A more detailed analysis of the limitations of the method would help to guide future research and development. For instance, it would be useful to understand the types of inputs or tasks that are particularly challenging for PoLar, and what factors contribute to these challenges. This would help to identify areas for improvement and potential failure modes.

### Suggestions

To address the lack of detailed computational analysis, the authors should include a more thorough breakdown of the computational costs associated with PoLar. This should include the time spent on segment boundary determination, operation log-probability computation, and beam search. A comparison of the number of floating-point operations (FLOPs) or the actual runtime of PoLar versus standard inference would be beneficial. Furthermore, the authors should provide a more detailed analysis of the memory usage of PoLar, including the memory required for storing the program representations and the intermediate results. This analysis should be conducted for different input lengths and program complexities to understand the scalability of the method. The authors should also investigate the impact of different hyperparameters on the computational overhead of PoLar, such as the number of beam search iterations and the maximum segment length. This would provide a more comprehensive understanding of the trade-offs between accuracy and efficiency.

To enhance the robustness analysis, the authors should conduct experiments on a wider range of tasks beyond mathematical reasoning. This should include tasks such as natural language understanding, text generation, and code generation. For example, the authors could evaluate PoLar on datasets such as GLUE or SuperGLUE for natural language understanding, or on code datasets such as HumanEval. The evaluation should include both accuracy and efficiency metrics, such as the number of layers executed and the inference time. The authors should also investigate the performance of PoLar on tasks that require different types of reasoning, such as logical reasoning or common-sense reasoning. This would help to understand the generalizability of the method and identify potential limitations. Furthermore, the authors should analyze the performance of PoLar on tasks with varying input lengths and complexities to understand its scalability and robustness.

To provide a more comprehensive understanding of the limitations of PoLar, the authors should conduct a more detailed analysis of the scenarios where the method might fail or underperform. This should include an investigation of the types of inputs or tasks that are particularly challenging for PoLar, and what factors contribute to these challenges. For example, the authors could analyze the performance of PoLar on inputs that require very deep or very shallow execution paths, or on tasks that require complex reasoning. The authors should also investigate the impact of different hyperparameters on the performance of PoLar, such as the number of layers to skip or repeat. This would help to identify the limitations of the method and potential areas for improvement. The authors should also discuss the potential failure modes of PoLar, such as the possibility of selecting a suboptimal program or the inability to adapt to certain types of inputs. This would help to guide future research and development.

### Questions

1. How does PoLar perform on tasks outside of mathematical reasoning? Are there specific domains where it excels or struggles?
2. What is the computational overhead of PoLar compared to standard inference? How does it scale with input complexity?
3. Are there any specific failure cases or scenarios where PoLar does not perform well? How can these be addressed?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper proposes a novel inference-time method that allows LLMs to skip or repeat layers to achieve better performance. The authors first demonstrate that such a method can achieve better performance than the original LLMs. Then, they propose a lightweight program-of-layers (PoLar) method that can generate execution programs to achieve better performance. The authors conduct experiments on the DART-Math dataset to show the effectiveness of the proposed method.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The proposed method is novel and interesting.
- The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method is only evaluated on the DART-Math dataset. It would be better to evaluate the proposed method on more datasets.
- The authors do not provide the results of PoLar on the ASDiv and MAWPS datasets, which are also used in the baseline methods.

### Suggestions

The paper introduces an interesting approach to inference-time computation control in LLMs, but its evaluation is limited to a single dataset, which raises concerns about the generalizability of the findings. While the DART-Math dataset is a good starting point, it is crucial to assess the method's performance across a wider range of tasks and datasets. Specifically, the authors should consider evaluating on datasets with different characteristics, such as those involving different types of reasoning or requiring different levels of computational complexity. For example, datasets from the GLUE benchmark or other mathematical reasoning datasets could provide a more comprehensive evaluation. This would help to determine if the observed performance gains are specific to the DART-Math dataset or if they are more broadly applicable. Furthermore, it would be beneficial to analyze the performance of the proposed method on datasets with varying input lengths and complexities to understand its scalability and robustness.

In addition to expanding the dataset evaluation, it is also important to provide a more detailed comparison with existing methods. The authors mention that their method achieves better performance than the original LLMs, but it is not clear how it compares to other inference-time computation control methods. Specifically, the authors should include the results of PoLar on the ASDiv and MAWPS datasets, which are used in the baseline methods. This would allow for a more direct comparison and a better understanding of the advantages and disadvantages of the proposed method. Furthermore, it would be helpful to analyze the computational cost of the proposed method compared to other methods. This would provide a more complete picture of the trade-offs between performance and computational efficiency. The authors should also consider providing an analysis of the types of errors that the proposed method makes, which could provide insights into its strengths and weaknesses.

Finally, the paper would benefit from a more detailed analysis of the proposed method's behavior. For example, it would be useful to understand how the number of skipped or repeated layers affects the performance of the method. The authors should also analyze the impact of different layer selection strategies on the overall performance. This would provide a better understanding of the method's inner workings and could potentially lead to further improvements. Furthermore, it would be beneficial to analyze the sensitivity of the method to different hyperparameters, such as the number of layers to skip or repeat. This would help to understand the robustness of the method and provide guidance on how to tune its parameters for optimal performance.

### Questions

- Could the authors provide the results of PoLar on the ASDiv and MAWPS datasets?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

This paper proposes a novel inference-time method that allows LLMs to skip or repeat layers to achieve better performance. The authors first demonstrate that such a method can achieve better performance than the original LLMs. Then, they propose a lightweight program-of-layers (PoLar) method that can generate execution programs to achieve better performance. The authors conduct experiments on the DART-Math dataset to show the effectiveness of the proposed method.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and interesting.
3. The experiments are comprehensive and well-designed.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is only evaluated on the DART-Math dataset. It would be better to evaluate the proposed method on more datasets.
2. The authors do not provide the results of PoLar on the ASDiv and MAWPS datasets, which are also used in the baseline methods.

### Suggestions

The paper introduces an interesting approach to inference-time computation control in LLMs, but its evaluation is limited to a single dataset, which raises concerns about the generalizability of the findings. While the DART-Math dataset is a good starting point, it is crucial to assess the method's performance across a wider range of tasks and datasets. Specifically, the authors should consider evaluating on datasets with different characteristics, such as those involving different types of reasoning or requiring different levels of computational complexity. For example, datasets from the GLUE benchmark or other mathematical reasoning datasets could provide a more comprehensive evaluation. This would help to determine if the observed performance gains are specific to the DART-Math dataset or if they are more broadly applicable. Furthermore, it would be beneficial to analyze the performance of the proposed method on datasets with varying input lengths and complexities to understand its scalability and robustness.

In addition to expanding the dataset evaluation, it is also important to provide a more detailed comparison with existing methods. The authors mention that their method achieves better performance than the original LLMs, but it is not clear how it compares to other inference-time computation control methods. Specifically, the authors should include the results of PoLar on the ASDiv and MAWPS datasets, which are used in the baseline methods. This would allow for a more direct comparison and a better understanding of the advantages and disadvantages of the proposed method. Furthermore, it would be helpful to analyze the computational cost of the proposed method compared to other methods. This would provide a more complete picture of the trade-offs between performance and computational efficiency. The authors should also consider providing an analysis of the types of errors that the proposed method makes, which could provide insights into its strengths and weaknesses.

Finally, the paper would benefit from a more detailed analysis of the proposed method's behavior. For example, it would be useful to understand how the number of skipped or repeated layers affects the performance of the method. The authors should also analyze the impact of different layer selection strategies on the overall performance. This would provide a better understanding of the method's inner workings and could potentially lead to further improvements. Furthermore, it would be beneficial to analyze the sensitivity of the method to different hyperparameters, such as the number of layers to skip or repeat. This would help to understand the robustness of the method and provide guidance on how to tune its parameters for optimal performance.

### Questions

See weakness

### Rating

8

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers for the provided paper. I need to go through each reviewer's comments and find evidence within the paper to support their claims.

**Plan:**
1. Read each reviewer's weakness.
2. Search the paper for evidence related to the weakness.
3. Categorize the evidence (methodological, experimental).
4. Analyze the evidence and determine if the weakness is valid.
5. Provide a conclusion with a confidence level and key supporting evidence.
**Review 1 Weaknesses:**

1. Weakness Statement:
[The paper does not provide a detailed analysis of the computational overhead associated with PoLar. While the authors claim that the method is efficient, they do not provide any quantitative data on the additional computational cost of the program-of-layers approach. This makes it difficult to assess the practical implications of the method, especially in resource-constrained environments. Specifically, the paper lacks a breakdown of the time spent on operations such as segment boundary determination, operation log-probability computation, and beam search, which are crucial for understanding the overall efficiency of the method. A comparison of the number of floating-point operations (FLOPs) or the actual runtime of PoLar versus standard inference would be beneficial.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions the inference-time program decoding process: "At inference time, execution programs are decoded in two stages. First, segment boundaries are determined deterministically by thresholding the predicted segmentation logits ℓ seg \bm{\ell}^{\text{seg}}. If any resulting segment exceeds the maximum length constraint K max K_{\max} , additional boundaries are inserted to enforce it, yielding segment start positions { s j } \{ s_j \} . Conditioned on this segmentation, we compute operation log-probabilities at each segment start from the predicted logits: log ⁡ p ⁡ ( o j ∣ x , s j ) = log ⁡ Softmax ⁡ ( ℓ s j o p ) [ o j ] . \log p(o_{j} \mid x, s_{j}) = \log \text{Softmax}(\bm{\ell}^{\text{op}}_{s_{j}})[o_{j}]. The final execution program is mapped deterministically to a concrete executed program using the segment-to-path rules in Section 3.1." (Section 3.2)
   - The paper also mentions the use of beam search: "Rather than selecting operations independently via local argmax, we apply a small beam search over segment-level operation choices to account for non-local interactions between segments and to ensure globally consistent execution programs." (Section 3.2)
   - The paper provides an inference-time performance comparison: "Table 4 reports the inference latency on Qwen1.5-MoE-A2.7B-Chat with 24 layers. As shown in Table 4 , the encoder, predictor head, and beam search introduce a total additional overhead of only 3.05 ms, corresponding to 0.8% of a standard forward pass and approximately 0.23 LLM layers. This overhead is small compared with the latency reduction achieved by executing fewer layers. Consequently, PoLar reduces end-to-end latency while improving accuracy: it achieves 0.83 × \times the base runtime on easier inputs and 0.95 × \times on harder inputs. The learned predictor is also lightweight in parameter count: across all evaluated backbones, it contains approximately 2.1M parameters, corresponding to only 0.01%–0.06% of the base LLM size. Full parameter counts are provided in Appendix D.3 ." (Section 4.3)

b) Experiment-related Evidence:
   - Table 4 provides the inference latency of PoLar compared to the base model.

3. Literature Gap Analysis:
   - The paper does not explicitly compare the number of FLOPs.

4. Validation Analysis:
   - The paper does provide some information about the computational overhead, specifically mentioning the additional latency introduced by the predictor and beam search (3.05 ms). It also provides the parameter count of the predictor.
   - However, the reviewer is correct that a more detailed breakdown of the time spent on segment boundary determination, operation log-probability computation, and beam search is missing. The paper provides the total overhead but not the individual components.
   - The paper also lacks a direct comparison of FLOPs or a more granular breakdown of the runtime.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper provides the total additional overhead (3.05 ms) and the parameter count of the predictor but lacks a detailed breakdown of the time spent on individual components and a comparison of FLOPs.

1. Weakness Statement:
[The paper does not explore the robustness of PoLar to different types of inputs or tasks. While the authors demonstrate that the method works well on mathematical reasoning tasks, it is unclear how it would perform on other types of tasks, such as natural language understanding or text generation. The paper should include experiments on a wider range of tasks to assess the generalizability of the approach. For example, it would be useful to see how PoLar performs on tasks that require more complex reasoning or involve different types of data, such as code or images. This broader evaluation would help to establish the robustness and versatility of the proposed approach and address concerns about its narrow focus on mathematical reasoning.]

2. Evidence Collection:
a) Experiment-related Evidence:
   - The paper explicitly states the datasets used for evaluation: "We evaluate PoLar on a range of mathematical reasoning benchmarks using multiple pretrained, instruction-tuned LLMs spanning different architectures and scales: LLaMA-3.2-3B-Instruct , Qwen1.5-MoE-A2.7B-Chat , Qwen2.5-3B-Instruct , and Qwen3-8B ." (Section 4.1)
   - The paper mentions the datasets: "Datasets. We use DART-Math ( Tong et al., 2024 ) , a structured mathematical reasoning dataset with five difficulty levels (DM-1 to DM-5), as in-distribution benchmark. For out-of-distribution (OOD) evaluation, we use ASDiv ( Miao et al., 2020 ) and MAWPS ( Kadlčík et al., 2023 ) , which focus on arithmetic word problems, as well as subject subsets from MMLU-Pro ( Wang et al., 2024 ) spanning mathematics, natural sciences, social sciences, and humanities." (Section 4.1)
   - All the mentioned datasets (DART-Math, ASDiv, MAWPS, MMLU-Pro subsets) are related to mathematical reasoning or natural language understanding (MMLU-Pro).

3. Literature Gap Analysis:
   - No missing citations related to the types of tasks.

4. Validation Analysis:
   - The reviewer is correct that the experiments are primarily focused on mathematical reasoning tasks, with some OOD evaluation on natural language understanding tasks (ASDiv, MAWPS) and a subset of MMLU-Pro.
   - The paper does not include experiments on tasks like natural language understanding (beyond the OOD datasets), text generation, or code generation.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper explicitly lists the datasets used for evaluation, and all of them are either mathematical reasoning datasets or subsets of MMLU-Pro, which is a natural language understanding benchmark. There are no experiments on tasks like text generation or code generation.

1. Weakness Statement:
[The paper does not provide a detailed analysis of the limitations of PoLar. While the current results are encouraging, it is important to acknowledge the scenarios where it might not perform well. For example, it would be useful to investigate how PoLar behaves on inputs that require very deep or very shallow execution paths. The authors should also explore the sensitivity of PoLar to the choice of hyperparameters, such as the number of layers to skip or repeat. A detailed analysis of these limitations would provide a more balanced view of the approach and help to guide future research. Additionally, it would be beneficial to explore the interpretability of the selected programs, as this could provide insights into the reasoning process of the model and help to identify potential failure cases.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions the maximum segment length K_max: "We set K max = 4 based on empirical evidence. Finding 4 execution programs that allow for the shortest execution and/or skipping the maximum number of layers generally increases the accuracy in every setting reported in Table 1 ." (Section 3.1)
   - The paper mentions the beam search size: "We set the beam size to 5 for all experiments." (Section 3.2)

b) Experiment-related Evidence:
   - The paper includes an analysis of execution depth: "Figure 8 (a) shows that 57.7% of successful top-5 candidates have execution programs that use fewer unique layers than a standard forward pass, indicating that the gains arise from better latent execution within the frozen model." (Section 4.2)
   - The paper includes an analysis of the number of repeated layers: "Figure 8 (b) shows that the fraction of solvable inputs that require deeper programs increases with dataset difficulty for most models. As task difficulty grows, valid execution programs become more constrained and increasingly rely on non-trivial execution strategies rather than standard inference." (Section 4.2)

3. Literature Gap Analysis:
   - No missing citations related to limitations or interpretability.

4. Validation Analysis:
   - The reviewer is correct that the paper lacks a detailed analysis of the limitations of PoLar.
   - While the paper shows that PoLar can achieve better accuracy with fewer layers on average, it doesn't explicitly analyze scenarios where PoLar might fail or underperform, such as inputs requiring very deep or very shallow execution paths.
   - The paper mentions the hyperparameters K_max and beam size but doesn't provide a sensitivity analysis of these parameters.
   - The paper does not include an analysis of the interpretability of the selected programs.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks explicit analysis of failure cases, sensitivity to hyperparameters (K_max, beam size), and interpretability of the selected programs.

**Review 2 Weaknesses:**

1. Weakness Statement:
[- While the paper demonstrates improvements on mathematical reasoning tasks, it is unclear how well PoLar generalizes to other domains or types of tasks. Further evaluation on diverse datasets would strengthen the claims of broad applicability.]

2. Evidence Collection: (Same as Review 1, Weakness 2)

3. Literature Gap Analysis: (Same as Review 1, Weakness 2)

4. Validation Analysis: (Same as Review 1, Weakness 2)

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: (Same as Review 1, Weakness 2)

1. Weakness Statement:
[- The paper does not thoroughly explore the computational overhead associated with PoLar, especially in terms of inference time and memory usage. A detailed analysis of these factors would be valuable for practical deployment.]

2. Evidence Collection: (Same as Review 1, Weakness 1)

3. Literature Gap Analysis: (Same as Review 1, Weakness 1)

4. Validation Analysis: (Same as Review 1, Weakness 1)

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: (Same as Review 1, Weakness 1)

1. Weakness Statement:
[- The paper could benefit from a more in-depth discussion of the limitations of PoLar and potential failure cases. Understanding these aspects would provide a more balanced view of the approach.]

2. Evidence Collection: (Same as Review 1, Weakness 3)

3. Literature Gap Analysis: (Same as Review 1, Weakness 3)

4. Validation Analysis: (Same as Review 1, Weakness 3)

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: (Same as Review 1, Weakness 3)

**Review 3 Weaknesses:**

1. Weakness Statement:
[The proposed method is only evaluated on the DART-Math dataset. It would be better to evaluate the proposed method on more datasets.]

2. Evidence Collection: (Same as Review 1, Weakness 2)

3. Literature Gap Analysis: (Same as Review 1, Weakness 2)

4. Validation Analysis: (Same as Review 1, Weakness 2)

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: (Same as Review 1, Weakness 2)

1. Weakness Statement:
[The authors do not provide the results of PoLar on the ASDiv and MAWPS datasets, which are also used in the baseline methods.]

2. Evidence Collection:
a) Experiment-related Evidence:
   - The paper states the datasets used: "Datasets. We use DART-Math ( Tong et al., 2024 ) , a structured mathematical reasoning dataset with five difficulty levels (DM-1 to DM-5), as in-distribution benchmark. For out-of-distribution (OOD) evaluation, we use ASDiv ( Miao et al., 2020 ) and MAWPS ( Kadlčík et al., 2023 ) , which focus on arithmetic word problems, as well as subject subsets from MMLU-Pro ( Wang et al., 2024 ) spanning mathematics, natural sciences, social sciences, and humanities." (Section 4.1)
   - The results section includes tables with results for DART-Math, ASDiv, and MAWPS: "Table 2 reports pass@ k k accuracy , defined as the probability that at least one of the top- k k candidates produces a correct answer. For PoLar , the k k candidates correspond to the top- k k predicted execution programs selected via beam search. For sampling-based baselines, k k corresponds to the number of stochastic decoding samples. Unless otherwise stated, OOD results are reported using pass@1." (Section 4.2)

3. Literature Gap Analysis:
   - No missing citations related to datasets.

4. Validation Analysis:
   - The reviewer is incorrect. The paper *does* provide results for PoLar on the ASDiv and MAWPS datasets in Table 2.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: Table 2 in the paper presents the results for PoLar on ASDiv and MAWPS.

**Review 4 Weaknesses:**

1. Weakness Statement:
[The paper does not provide a detailed analysis of the computational overhead associated with PoLar. While the authors claim that the method is efficient, they do not provide any quantitative data on the additional computational cost of the program-of-layers approach. This makes it difficult to assess the practical implications of the method, especially in resource-constrained environments. Specifically, the paper lacks a breakdown of the time spent on operations such as segment boundary determination, operation log-probability computation, and beam search, which are crucial for understanding the overall efficiency of the method. A comparison of the number of floating-point operations (FLOPs) or the actual runtime of PoLar versus standard inference would be beneficial.]

2. Evidence Collection: (Same as Review 1, Weakness 1 and Review 3, Weakness 1)

3. Literature Gap Analysis: (Same as Review 1, Weakness 1 and Review 3, Weakness 1)

4. Validation Analysis: (Same as Review 1, Weakness 1 and Review 3, Weakness 1)

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: (Same as Review 1, Weakness 1 and Review 3, Weakness 1)

1. Weakness Statement:
[The paper does not explore the robustness of PoLar to different types of inputs or tasks. While the authors demonstrate that the method works well on mathematical reasoning tasks, it is unclear how it would perform on other types of tasks, such as natural language understanding or text generation. The paper should include experiments on a wider range of tasks to assess the generalizability of the approach. For example, it would be useful to see how PoLar performs on tasks that require more complex reasoning or involve different types of data, such as code or images. This broader evaluation would help to establish the robustness and versatility of the proposed approach and address concerns about its narrow focus on mathematical reasoning.]

2. Evidence Collection: (Same as Review 1, Weakness 2)

3. Literature Gap Analysis: (Same as Review 1, Weakness 2)

4. Validation Analysis: (Same as Review 1, Weakness 2)

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: (Same as Review 1, Weakness 2)

1. Weakness Statement:
[The paper does not provide a detailed analysis of the limitations of PoLar. While the current results are encouraging, it is important to acknowledge the scenarios where it might not perform well. For example, it would be useful to investigate how PoLar behaves on inputs that require very deep or very shallow execution paths. The authors should also explore the sensitivity of PoLar to the choice of hyperparameters, such as the number of layers to skip or repeat. A detailed analysis of these limitations would provide a more balanced view of the approach and help to guide future research. Additionally, it would be beneficial to explore the interpretability of the selected programs, as this could provide insights into the reasoning process of the model and help to identify potential failure cases.]

2. Evidence Collection: (Same as Review 1, Weakness 3)

3. Literature Gap Analysis: (Same as Review 1, Weakness 3)

4. Validation Analysis: (Same as Review 1, Weakness 3)

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: (Same as Review 1, Weakness 3)
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces PoLar (Program-of-Layers), a novel inference-time method designed to enhance the performance of large language models (LLMs) by dynamically adjusting their execution paths. The core idea behind PoLar is to allow LLMs to skip or repeat layers during inference, effectively tailoring the computation to each input. This flexibility is achieved through a lightweight predictor that generates execution programs, which dictate the specific sequence of layers to be executed for a given input. The authors propose that this approach enables LLMs to adapt their computation to each input, potentially leading to more efficient and accurate results. The method operates without modifying the underlying LLM parameters, making it a practical solution that can be readily applied to existing models. The authors conduct extensive experiments on a range of mathematical reasoning benchmarks, including DART-Math, ASDiv, and MAWPS, demonstrating that PoLar consistently outperforms standard inference and prior dynamic-depth methods. The empirical results show that PoLar can achieve better performance with fewer layers on average, suggesting that it can find more efficient execution paths for complex mathematical reasoning tasks. The authors also provide an analysis of the learned execution programs, showing that they often use fewer unique layers than a standard forward pass, indicating that the gains arise from better latent execution within the frozen model. The paper also includes an analysis of the computational overhead of PoLar, showing that the additional latency introduced by the predictor and beam search is relatively small compared to the latency reduction achieved by executing fewer layers. Overall, the paper presents a compelling approach to dynamic inference in LLMs, with strong empirical results and a clear methodology. However, as I will discuss in the following sections, there are several limitations and areas for improvement that warrant further investigation. The paper's contribution lies in its novel approach to dynamic inference, its practical implementation, and its strong empirical validation on mathematical reasoning tasks. However, the lack of a detailed analysis of computational overhead, the limited evaluation on diverse datasets, and the absence of a thorough discussion of limitations and failure cases are significant concerns that need to be addressed to fully assess the practical applicability and generalizability of the proposed method.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

2.75


## Strengths:

The primary strength of this paper lies in its innovative approach to dynamic inference in large language models. The concept of allowing LLMs to skip or repeat layers during execution, effectively creating a 'program-of-layers,' is a novel and promising direction for improving both the efficiency and accuracy of inference. This approach is particularly compelling because it allows the model to adapt its computation to each input, potentially leading to more tailored and efficient processing. The authors' decision to keep the underlying LLM parameters frozen is another significant strength. By not modifying the pre-trained model, the method ensures that it can be readily applied to existing models without requiring extensive retraining or computational resources. This practical aspect is crucial for the widespread adoption of the method. Furthermore, the empirical results presented in the paper are compelling. The authors demonstrate that PoLar consistently outperforms standard inference and prior dynamic-depth methods on a range of mathematical reasoning benchmarks. The fact that PoLar achieves better performance with fewer layers on average suggests that it can effectively identify and utilize more efficient execution paths for complex mathematical reasoning tasks. The analysis of the learned execution programs, showing that they often use fewer unique layers than a standard forward pass, further supports this claim. The paper is also well-written and easy to follow, with a clear explanation of the proposed method and the experimental setup. The use of figures and tables effectively illustrates the key concepts and results. The authors also provide a detailed analysis of the computational overhead of PoLar, showing that the additional latency introduced by the predictor and beam search is relatively small compared to the latency reduction achieved by executing fewer layers. This analysis is crucial for assessing the practical implications of the method. Finally, the authors' use of multiple pretrained, instruction-tuned LLMs spanning different architectures and scales strengthens the generalizability of their findings. The fact that PoLar performs well across different models suggests that the method is robust and not specific to a particular architecture or training regime. Overall, the paper presents a strong and well-supported argument for the effectiveness of PoLar as a dynamic inference method for LLMs.


## Weaknesses:

Despite the strengths of the proposed method, there are several weaknesses that I have identified through my analysis. First, while the paper claims that PoLar is efficient, it lacks a detailed analysis of the computational overhead associated with the program-of-layers approach. Although the authors provide the additional latency introduced by the predictor and beam search (3.05 ms), they do not offer a breakdown of the time spent on individual operations such as segment boundary determination, operation log-probability computation, and beam search. This lack of detailed analysis makes it difficult to assess the practical implications of the method, especially in resource-constrained environments. Furthermore, the paper does not include a comparison of the number of floating-point operations (FLOPs) or a more granular breakdown of the runtime, which would be beneficial for a more comprehensive understanding of the computational cost. This is a significant limitation, as it is crucial to understand the trade-offs between accuracy and efficiency. My confidence in this weakness is high, as the paper explicitly mentions the additional overhead but does not provide a detailed breakdown of its components. Second, the paper's evaluation is primarily focused on mathematical reasoning tasks, with some out-of-distribution (OOD) evaluation on ASDiv and MAWPS. While the authors demonstrate that PoLar works well on these tasks, it is unclear how it would perform on other types of tasks, such as natural language understanding, text generation, or code generation. The paper does not include experiments on a wider range of tasks to assess the generalizability of the approach. This narrow focus on mathematical reasoning limits the scope of the paper's conclusions and raises questions about the applicability of PoLar to other domains. My confidence in this weakness is high, as the paper explicitly lists the datasets used for evaluation, and all of them are either mathematical reasoning datasets or subsets of MMLU-Pro, which is a natural language understanding benchmark. There are no experiments on tasks like text generation or code generation. Third, the paper does not provide a detailed analysis of the limitations of PoLar. While the authors demonstrate that the method works well on mathematical reasoning tasks, they do not explicitly analyze scenarios where it might fail or underperform, such as inputs requiring very deep or very shallow execution paths. The paper also lacks a sensitivity analysis of the hyperparameters, such as the number of layers to skip or repeat, and it does not explore the interpretability of the selected programs. This lack of analysis makes it difficult to understand the scenarios where PoLar might not perform well and provides a balanced view of the approach. My confidence in this weakness is high, as the paper lacks explicit analysis of failure cases, sensitivity to hyperparameters, and interpretability of the selected programs. Finally, while the paper provides results for PoLar on ASDiv and MAWPS, it does not include an analysis of the interpretability of the selected programs. Understanding these programs could provide insights into the reasoning process of the model and help to identify potential failure cases. This is a missed opportunity, as the interpretability of the selected programs could provide valuable insights into the method's behavior. My confidence in this weakness is high, as the paper does not include any analysis of the interpretability of the selected programs.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should conduct a more detailed analysis of the computational overhead associated with PoLar. This should include a breakdown of the time spent on individual operations, such as segment boundary determination, operation log-probability computation, and beam search. A comparison of the number of floating-point operations (FLOPs) or a more granular breakdown of the runtime would also be beneficial. This detailed analysis would provide a more complete picture of the trade-offs between accuracy and efficiency and help to identify potential bottlenecks for real-world applications. Second, the authors should expand the evaluation of PoLar to include a wider range of tasks beyond mathematical reasoning. This should include tasks such as natural language understanding, text generation, and code generation. For example, the authors could evaluate PoLar on datasets like GLUE or SuperGLUE for natural language understanding, or on code datasets like HumanEval. This broader evaluation would help to establish the robustness and versatility of the proposed approach and address concerns about its narrow focus on mathematical reasoning. Third, the authors should conduct a more thorough analysis of the limitations of PoLar. This should include an investigation of scenarios where the method might fail or underperform, such as inputs requiring very deep or very shallow execution paths. The authors should also explore the sensitivity of PoLar to the choice of hyperparameters, such as the number of layers to skip or repeat. This sensitivity analysis would help to understand the robustness of the method and provide guidance on how to tune its parameters for optimal performance. Furthermore, the authors should explore the interpretability of the selected programs. This could involve analyzing the structure of the generated execution programs and understanding how they relate to the input and the reasoning process of the model. This analysis could provide insights into the strengths and weaknesses of the method and help to identify potential failure cases. Finally, the authors should provide a more detailed analysis of the types of errors that PoLar makes. This could involve analyzing the performance of PoLar on inputs that require very deep or very shallow execution paths, or on tasks that require complex reasoning. The authors should also investigate the impact of different hyperparameters on the performance of PoLar, such as the number of layers to skip or repeat. This would help to identify the limitations of the method and potential areas for improvement. In summary, these suggestions aim to provide a more comprehensive understanding of the proposed method, its limitations, and its potential for practical applications.


## Questions:

Based on my analysis, I have several questions that I believe are crucial for a deeper understanding of the proposed method. First, how does PoLar perform on tasks outside of mathematical reasoning? Are there specific domains where it excels or struggles? This question is important because the current evaluation is heavily focused on mathematical reasoning, and it is unclear how well the method would generalize to other types of tasks. Second, what is the computational overhead of PoLar compared to standard inference? How does it scale with input complexity? This question is important because the paper claims that the method is efficient, but it lacks a detailed analysis of the computational cost. Understanding the scalability of the method is crucial for assessing its practical applicability. Third, are there any specific failure cases or scenarios where PoLar does not perform well? How can these be addressed? This question is important because the paper does not provide a detailed analysis of the limitations of the method, and it is crucial to understand the scenarios where it might fail. Fourth, how sensitive is PoLar to the choice of hyperparameters, such as the number of layers to skip or repeat? This question is important because the paper does not provide a sensitivity analysis of these parameters, and it is crucial to understand how they affect the performance of the method. Finally, how interpretable are the selected programs? Can insights from these programs help to identify potential failure cases? This question is important because the paper does not provide an analysis of the interpretability of the selected programs, and it is crucial to understand how they relate to the reasoning process of the model. These questions aim to address the key uncertainties and limitations of the proposed method and to provide a more comprehensive understanding of its behavior and potential.


## Rating:

6.5


## Confidence:

3.0


## Decision:

Accept
}