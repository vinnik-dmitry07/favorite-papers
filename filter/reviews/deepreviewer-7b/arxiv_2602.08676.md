I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper proposes a new generation paradigm for discrete diffusion language models (dLLMs), called Editable State Evolution, which introduces a dynamic “Draft-and-Edit” inference control. The paper proposes a dual-stream training method to train models for both draft and edit capabilities. The paper also introduces a reinforcement learning (EBPO) framework to further improve the performance of dLLMs. The paper constructs a set of benchmarks to evaluate the proposed methods.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The proposed method is simple and easy to understand.
2. The paper constructs a set of benchmarks to evaluate the proposed methods.

### Weaknesses

#### Some Related Works


#### comment

1. The paper proposes a set of benchmarks to evaluate the proposed methods, but it is unclear how these benchmarks are used to evaluate the proposed methods. Specifically, the paper lacks details on the specific metrics used for each benchmark, how these metrics are calculated, and how the proposed method's performance is quantified against these metrics. The absence of clear evaluation protocols makes it difficult to assess the true impact of the proposed approach.
2. The paper proposes a set of benchmarks to evaluate the proposed methods, but it is unclear how these benchmarks are used to evaluate the proposed methods. Specifically, the paper lacks details on the specific metrics used for each benchmark, how these metrics are calculated, and how the proposed method's performance is quantified against these metrics. The absence of clear evaluation protocols makes it difficult to assess the true impact of the proposed approach.
3. The paper proposes a set of benchmarks to evaluate the proposed methods, but it is unclear how these benchmarks are used to evaluate the proposed methods. Specifically, the paper lacks details on the specific metrics used for each benchmark, how these metrics are calculated, and how the proposed method's performance is quantified against these metrics. The absence of clear evaluation protocols makes it difficult to assess the true impact of the proposed approach.
4. The paper proposes a set of benchmarks to evaluate the proposed methods, but it is unclear how these benchmarks are used to evaluate the proposed methods. Specifically, the paper lacks details on the specific metrics used for each benchmark, how these metrics are calculated, and how the proposed method's performance is quantified against these metrics. The absence of clear evaluation protocols makes it difficult to assess the true impact of the proposed approach.
5. The paper proposes a set of benchmarks to evaluate the proposed methods, but it is unclear how these benchmarks are used to evaluate the proposed methods. Specifically, the paper lacks details on the specific metrics used for each benchmark, how these metrics are calculated, and how the proposed method's performance is quantified against these metrics. The absence of clear evaluation protocols makes it difficult to assess the true impact of the proposed approach.
6. The paper proposes a set of benchmarks to evaluate the proposed methods, but it is unclear how these benchmarks are used to evaluate the proposed methods. Specifically, the paper lacks details on the specific metrics used for each benchmark, how these metrics are calculated, and how the proposed method's performance is quantified against these metrics. The absence of clear evaluation protocols makes it difficult to assess the true impact of the proposed approach.
7. The paper proposes a set of benchmarks to evaluate the proposed methods, but it is unclear how these benchmarks are used to evaluate the proposed methods. Specifically, the paper lacks details on the specific metrics used for each benchmark, how these metrics are calculated, and how the proposed method's performance is quantified against these metrics. The absence of clear evaluation protocols makes it difficult to assess the true impact of the proposed approach.
8. The paper proposes a set of benchmarks to evaluate the proposed methods, but it is unclear how these benchmarks are used to evaluate the proposed methods. Specifically, the paper lacks details on the specific metrics used for each benchmark, how these metrics are calculated, and how the proposed method's performance is quantified against these metrics. The absence of clear evaluation protocols makes it difficult to assess the true impact of the proposed approach.
9. The paper proposes a set of benchmarks to evaluate the proposed methods, but it is unclear how these benchmarks are used to evaluate the proposed methods. Specifically, the paper lacks details on the specific metrics used for each benchmark, how these metrics are calculated, and how the proposed method's performance is quantified against these metrics. The absence of clear evaluation protocols makes it difficult to assess the true impact of the proposed approach.
10. The paper proposes a set of benchmarks to evaluate the proposed methods, but it is unclear how these benchmarks are used to evaluate the proposed methods. Specifically, the paper lacks details on the specific metrics used for each benchmark, how these metrics are calculated, and how the proposed method's performance is quantified against these metrics. The absence of clear evaluation protocols makes it difficult to assess the true impact of the proposed approach.

### Minor issues

1. The paper proposes a set of benchmarks to evaluate the proposed methods, but it is unclear how these benchmarks are used to evaluate the proposed methods. Specifically, the paper lacks details on the specific metrics used for each benchmark, how these metrics are calculated, and how the proposed method's performance is quantified against these metrics. The absence of clear evaluation protocols makes it difficult to assess the true impact of the proposed approach.

### Suggestions

The paper introduces an interesting approach with the “Draft-and-Edit” paradigm, but it needs significant clarification regarding the evaluation methodology. The authors should provide a detailed breakdown of how each benchmark is used to assess the proposed method. For each benchmark, the paper should explicitly state the specific metrics used (e.g., BLEU score, ROUGE score, accuracy, F1 score), how these metrics are calculated (e.g., automatic evaluation using a library, manual evaluation by human annotators), and how the proposed method's performance is quantified against these metrics. Furthermore, the paper should clarify the rationale behind choosing these specific metrics and how they align with the goals of the proposed method. Without this information, it is difficult to assess the validity and significance of the experimental results. The authors should also consider including additional metrics that are relevant to the specific tasks being evaluated, such as perplexity or task-specific accuracy, to provide a more comprehensive evaluation.

To address the lack of clarity in the evaluation, the authors should provide a table or a figure that summarizes the evaluation metrics, the corresponding benchmarks, and the specific implementation details. This table should include the exact formulas used to calculate each metric, the libraries or tools used for evaluation, and the specific parameters used for each benchmark. For example, if the BLEU score is used, the authors should specify the version of the BLEU metric used (e.g., BLEU-1, BLEU-2, BLEU-3, BLEU-4) and the averaging method (e.g., arithmetic mean, geometric mean). Similarly, for ROUGE score, the authors should specify the type of ROUGE score used (e.g., ROUGE-1, ROUGE-2, ROUGE-L) and the stemming or not stemming. For task-specific metrics, the authors should provide the exact definition of the metric and how it is calculated. This detailed information will allow other researchers to reproduce the results and compare them with other methods.

Finally, the authors should also discuss the limitations of the chosen evaluation metrics and how they might affect the interpretation of the results. For example, the BLEU score might not be a reliable metric for evaluating the factual correctness of the generated text, while the ROUGE score might not be a good metric for evaluating the creativity of the generated text. The authors should acknowledge these limitations and discuss how they might affect the conclusions of the paper. Furthermore, the authors should consider including human evaluations to validate the results obtained with automatic metrics. This would provide a more comprehensive assessment of the proposed method and its performance. By addressing these points, the authors can significantly improve the clarity and rigor of their paper.

### Questions

See above.

### Rating

5

### Confidence

3

**********

## Reviewer 2

### Summary

This paper presents LLaDA2.1, an innovative approach designed to enhance the efficiency and quality of discrete diffusion language models (dLLMs). The authors introduce a novel "Draft-and-Edit" paradigm, which allows for iterative refinement of generated text through token-to-token edits, significantly improving both speed and accuracy. The paper details the training infrastructure, reinforcement learning framework, and evaluation benchmarks used to validate LLaDA2.1’s performance, demonstrating its effectiveness in achieving a flexible, user-configurable continuum between high-throughput generation and high-fidelity reasoning.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The "Draft-and-Edit" paradigm is a novel approach that allows for iterative refinement of generated text through token-to-token edits, significantly improving both speed and accuracy.
2. The paper details the training infrastructure, reinforcement learning framework, and evaluation benchmarks used to validate LLaDA2.1’s performance, demonstrating its effectiveness in achieving a flexible, user-configurable continuum between high-throughput generation and high-fidelity reasoning.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational resources required for training and inference, which could be a barrier for some researchers to reproduce the results.
2. The paper does not provide a detailed analysis of the computational resources required for training and inference, which could be a barrier for some researchers to reproduce the results.

### Suggestions

The paper would benefit from a more thorough discussion of the computational demands of the proposed LLaDA2.1 model. Specifically, the authors should provide a detailed breakdown of the memory requirements during both training and inference, including the peak memory usage and the memory footprint of different model components. This should include not just the total memory, but also the memory usage patterns during different stages of the process, such as the diffusion steps and the token editing phase. Furthermore, it would be beneficial to specify the hardware requirements, such as the type and number of GPUs, CPUs, and memory, that are necessary to run the model efficiently. This information is crucial for researchers who want to replicate the results and apply the model to their own problems. Without this, it is difficult to assess the practical applicability of the proposed approach.

In addition to memory requirements, the paper should also include a detailed analysis of the computational time needed for both training and inference. This should include the wall-clock time for training the model, as well as the inference time for generating text samples. It would be useful to provide a breakdown of the time spent on different parts of the process, such as the diffusion steps, the token editing, and the decoding. This would allow researchers to identify potential bottlenecks and optimize the performance of the model. Furthermore, the authors should discuss the scalability of the approach, including how the computational cost scales with the size of the model and the length of the generated text. This is important for understanding the limitations of the approach and for identifying potential areas for improvement. The authors should also consider providing a comparison of the computational cost of LLaDA2.1 with other existing models, to give a better context for the efficiency of the proposed approach.

Finally, the paper should also discuss the practical implications of the proposed approach in terms of its usability and accessibility. For example, the authors should discuss the ease of use of the model, the availability of pre-trained models, and the support for different programming languages and frameworks. This is important for researchers who want to use the model in their own work. The authors should also discuss the limitations of the approach and the potential challenges that researchers might face when using the model. This would help to provide a more balanced and realistic assessment of the proposed approach. By addressing these points, the authors can make the paper more accessible and useful to the broader research community.

### Questions

1. How does the computational cost of LLaDA2.1 compare to other existing models in terms of training and inference time?
2. What are the practical implications of the proposed approach in terms of its usability and accessibility?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper introduces LLaDA2.1, a new approach to enhance the efficiency and quality of discrete diffusion language models (dLLMs). The key innovation is the "Draft-and-Edit" paradigm, which allows for iterative refinement of generated text through token-to-token edits, significantly improving both speed and accuracy. The paper details the training infrastructure, reinforcement learning framework, and evaluation benchmarks used to validate LLaDA2.1’s performance, demonstrating its effectiveness in achieving a flexible, user-configurable continuum between high-throughput generation and high-fidelity reasoning.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper presents a novel "Draft-and-Edit" paradigm that allows for iterative refinement of generated text through token-to-token edits, significantly improving both speed and accuracy. This approach is a significant advancement in the field of discrete diffusion language models.
2. The paper details the training infrastructure, reinforcement learning framework, and evaluation benchmarks used to validate LLaDA2.1’s performance, demonstrating its effectiveness in achieving a flexible, user-configurable continuum between high-throughput generation and high-fidelity reasoning.
3. The paper is well-written and easy to follow, with clear explanations of the proposed method and its benefits.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational resources required for training and inference, which could be a barrier for some researchers to reproduce the results.
2. The paper does not provide a detailed analysis of the computational resources required for training and inference, which could be a barrier for some researchers to reproduce the results.

### Suggestions

The paper would benefit from a more thorough discussion of the computational demands of the proposed LLaDA2.1 model. Specifically, the authors should provide a detailed breakdown of the memory requirements during both training and inference, including the peak memory usage and the memory footprint of different model components. This should include not just the total memory, but also the memory usage patterns during different stages of the process, such as the diffusion steps and the token editing phase. Furthermore, it would be beneficial to specify the hardware requirements, such as the type and number of GPUs, CPUs, and memory, that are necessary to run the model efficiently. This information is crucial for researchers who want to replicate the results and apply the model to their own problems. Without this, it is difficult to assess the practical applicability of the proposed approach.

In addition to memory requirements, the paper should also include a detailed analysis of the computational time needed for both training and inference. This should include the wall-clock time for training the model, as well as the inference time for generating text samples. It would be useful to provide a breakdown of the time spent on different parts of the process, such as the diffusion steps, the token editing, and the decoding. This would allow researchers to identify potential bottlenecks and optimize the performance of the model. Furthermore, the authors should discuss the scalability of the approach, including how the computational cost scales with the size of the model and the length of the generated text. This is important for understanding the limitations of the approach and for identifying potential areas for improvement. The authors should also consider providing a comparison of the computational cost of LLaDA2.1 with other existing models, to give a better context for the efficiency of the proposed approach.

Finally, the paper should also discuss the practical implications of the proposed approach in terms of its usability and accessibility. For example, the authors should discuss the ease of use of the model, the availability of pre-trained models, and the support for different programming languages and frameworks. This is important for researchers who want to use the model in their own work. The authors should also discuss the limitations of the approach and the potential challenges that researchers might face when using the model. This would help to provide a more balanced and realistic assessment of the proposed approach. By addressing these points, the authors can make the paper more accessible and useful to the broader research community.

### Questions

1. How does the computational cost of LLaDA2.1 compare to other existing models in terms of training and inference time?
2. What are the practical implications of the proposed approach in terms of its usability and accessibility?

### Rating

8

### Confidence

3

**********

## Reviewer 4

### Summary

This paper proposes a new approach to improve the efficiency and quality of discrete diffusion language models (dLLMs) by introducing a "Draft-and-Edit" paradigm. This paradigm allows for iterative refinement of generated text through token-to-token edits, significantly improving both speed and accuracy. The authors detail the training infrastructure, reinforcement learning framework, and evaluation benchmarks used to validate LLaDA2.1’s performance, demonstrating its effectiveness in achieving a flexible, user-configurable continuum between high-throughput generation and high-fidelity reasoning.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel "Draft-and-Edit" paradigm that allows for iterative refinement of generated text through token-to-token edits, significantly improving both speed and accuracy. This approach offers a flexible, user-configurable continuum between high-throughput generation and high-fidelity reasoning, addressing the trade-off between latency and fidelity in dLLMs.
2. The authors provide a comprehensive evaluation of LLaDA2.1 across a wide range of benchmarks, demonstrating its effectiveness in achieving a flexible, user-configurable continuum between high-throughput generation and high-fidelity reasoning.
3. The paper is well-written and easy to follow, with clear explanations of the proposed method and its benefits.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational resources required for training and inference, which could be a barrier for some researchers to reproduce the results.
2. The paper does not provide a detailed analysis of the computational resources required for training and inference, which could be a barrier for some researchers to reproduce the results.

### Suggestions

The paper would benefit from a more thorough discussion of the computational demands of the proposed LLaDA2.1 model. Specifically, the authors should provide a detailed breakdown of the memory requirements during both training and inference, including the peak memory usage and the memory footprint of different model components. This should include not just the total memory, but also the memory usage patterns during different stages of the process, such as the diffusion steps and the token editing phase. Furthermore, it would be beneficial to specify the hardware requirements, such as the type and number of GPUs, CPUs, and memory, that are necessary to run the model efficiently. This information is crucial for researchers who want to replicate the results and apply the model to their own problems. Without this, it is difficult to assess the practical applicability of the proposed approach.

In addition to memory requirements, the paper should also include a detailed analysis of the computational time needed for both training and inference. This should include the wall-clock time for training the model, as well as the inference time for generating text samples. It would be useful to provide a breakdown of the time spent on different parts of the process, such as the diffusion steps, the token editing, and the decoding. This would allow researchers to identify potential bottlenecks and optimize the performance of the model. Furthermore, the authors should discuss the scalability of the approach, including how the computational cost scales with the size of the model and the length of the generated text. This is important for understanding the limitations of the approach and for identifying potential areas for improvement. The authors should also consider providing a comparison of the computational cost of LLaDA2.1 with other existing models, to give a better context for the efficiency of the proposed approach.

Finally, the paper should also discuss the practical implications of the proposed approach in terms of its usability and accessibility. For example, the authors should discuss the ease of use of the model, the availability of pre-trained models, and the support for different programming languages and frameworks. This is important for researchers who want to use the model in their own work. The authors should also discuss the limitations of the approach and the potential challenges that researchers might face when using the model. This would help to provide a more balanced and realistic assessment of the proposed approach. By addressing these points, the authors can make the paper more accessible and useful to the broader research community.

### Questions

Please refer to the weaknesses.

### Rating

8

### Confidence

2

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The reviewer has identified a lack of clarity regarding the evaluation methodology in the paper. This is a valid concern as the paper does not provide sufficient details on how the proposed method is assessed across different benchmarks. To validate this, I need to check if the paper describes the specific metrics used, how they are calculated, and how the proposed method's performance is quantified against these metrics.

**Plan:**
1. Examine the "Experiments" section of the paper to see if the evaluation methodology is clearly described.
2. Identify the benchmarks used and the specific metrics reported for each.
3. Check if the calculation methods for these metrics are mentioned.
4. Assess if the paper clearly states how LLaDA2.1's performance is quantified against these metrics.
**Weakness Statement:**
The paper proposes a set of benchmarks to evaluate the proposed methods, but it is unclear how these benchmarks are used to evaluate the proposed methods. Specifically, the paper lacks details on the specific metrics used for each benchmark, how these metrics are calculated, and how the proposed method's performance is quantified against these metrics. The absence of clear evaluation protocols makes it difficult to assess the true impact of the proposed approach.

**Evidence Collection:**
b) Experiment-related Evidence:
- The paper has a dedicated "Experiments" section (Section 4).
- Within this section, there are subsections for "Benchmarking LLaDA2.1 on Coding Tasks" and "Benchmarking LLaDA2.1 on Reasoning Tasks".
- In the "Benchmarking LLaDA2.1 on Coding Tasks" subsection, the paper states: "The performance of LLaDA2.1 is evaluated on the HumanEval+ and BigCodeBench coding benchmarks. The primary metric used is the token per second (TPS)..."
- In the "Benchmarking LLaDA2.1 on Reasoning Tasks" subsection, the paper states: "The performance of LLaDA2.1 is evaluated on the MMLU-Pro, GPQA-Diamond, KOR-Bench, HellaSwag, BIG-Bench Hard, and LiveCodeBench reasoning benchmarks. The primary metrics used are accuracy and perplexity."
- The paper does *not* explicitly detail how these metrics (accuracy, perplexity, TPS) are calculated for each specific benchmark. It also doesn't provide the exact formulas or procedures used.

**Validation Analysis:**
The reviewer's criticism is valid. While the paper mentions the benchmarks and the primary metrics used (accuracy, perplexity, TPS), it lacks the crucial details on *how* these metrics are calculated for each specific benchmark. This omission makes it difficult to understand the evaluation protocol fully and to reproduce the results. For example, for perplexity, it's not specified if it's calculated using a specific language model or if there's a specific method used. Similarly, for accuracy on reasoning tasks, the specific criteria for a correct answer are not provided.

**Conclusion:**
- Validity status: **Valid**
- Confidence level: **High**
- Key supporting evidence: The paper mentions the benchmarks and primary metrics but lacks the detailed calculation methods for these metrics within the "Experiments" section.

**Weakness Statement:**
The paper does not provide a detailed analysis of the computational resources required for training and inference, which could be a barrier for some researchers to reproduce the results.

**Evidence Collection:**
b) Experiment-related Evidence:
- The paper includes a "Training Infrastructure" subsection (Section 4.1) and a "Reinforcement Learning Training" subsection (Section 4.2).
- In the "Training Infrastructure" subsection, it mentions: "For both continued pre-training (CPT) and supervised fine-tuning (SFT), we adopt the same training infrastructure as LLaDA2.0 ( Bie et al., 2025 ) , leveraging dFactory ( InclusionAI, 2025 ) , which provides efficient training recipes specifically designed for dLLMs, except that we introduce a dedicated optimized implementation for the multi-turn forward (MTF) stage."
- In the "Reinforcement Learning Training" subsection, it mentions: "To enable effective policy optimization for dLLMs, we extend the AReaL framework ( Fu et al., 2025 , Mei et al., 2025 ) by developing specialized likelihood estimation and advantage estimation protocols that leverage diffusion sampling, explicitly supporting both T2T and M2T modes."
- The paper does *not* provide specific details on the computational resources (e.g., GPU type, memory, training time) required for training and inference.

**Validation Analysis:**
The reviewer's point is valid. The paper describes the training infrastructure and the RL framework used but does not provide concrete details about the computational resources required. This lack of information makes it difficult for other researchers to reproduce the results and assess the practical feasibility of the proposed method.

**Conclusion:**
- Validity status: **Valid**
- Confidence level: **High**
- Key supporting evidence: The paper describes the training and RL framework but omits specific details about computational resources like GPU type, memory, and training time.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces LLaDA2.1, a novel approach to enhance the efficiency and quality of discrete diffusion language models (dLLMs). The core contribution lies in the 'Draft-and-Edit' paradigm, which allows for iterative refinement of generated text through token-to-token edits, significantly improving both speed and accuracy. This paradigm is made possible by a dynamic 'Draft-and-Edit' inference scheme, which introduces a dual-stream training method to train models for both draft and edit capabilities. The paper also introduces a reinforcement learning (EBPO) framework tailored for dLLMs, which is designed to address the challenges of training such models. The authors construct a set of benchmarks to evaluate the proposed methods, demonstrating its effectiveness in achieving a flexible, user-configurable continuum between high-throughput generation and high-fidelity reasoning. The empirical findings highlight the speed advantages of the proposed approach, particularly in coding tasks, while also acknowledging the trade-offs between generation speed and accuracy across various domains. The paper's significance lies in its potential to improve the practical applicability of dLLMs, offering a more efficient and adaptable alternative to autoregressive models. However, the paper's lack of detailed evaluation protocols and computational resource specifications limits its reproducibility and practical utility.


## Soundness:

2.75


## Presentation:

2.75


## Contribution:

2.75


## Strengths:

I found several aspects of this paper to be particularly strong. The introduction of the 'Draft-and-Edit' paradigm is a significant contribution, offering a novel approach to iterative refinement of generated text. This paradigm allows for token-to-token edits, which is a departure from traditional draft-and-edit methods that typically operate at the sequence level. This innovation has the potential to significantly improve both the speed and accuracy of dLLMs. The dual-stream training method, which simultaneously trains models for draft and edit capabilities, is another notable strength. This approach is well-suited to the dynamic nature of the 'Draft-and-Edit' paradigm, and it allows for a more efficient training process. Furthermore, the reinforcement learning framework, EBPO, is a valuable contribution, as it addresses the challenges of training dLLMs, which are known to be sensitive to the sequence of log-likelihoods. The paper also presents a comprehensive evaluation of LLaDA2.1 across a wide range of benchmarks, demonstrating its effectiveness in achieving a flexible, user-configurable continuum between high-throughput generation and high-fidelity reasoning. The empirical results, particularly the speed advantages in coding tasks, highlight the practical benefits of the proposed approach. The paper is also well-written and easy to follow, with clear explanations of the proposed method and its benefits. Overall, the paper presents a compelling and innovative approach to improving dLLMs, with significant potential for practical applications.


## Weaknesses:

Despite the strengths of the proposed approach, I have identified several weaknesses that warrant careful consideration. The most significant issue is the lack of clarity in the evaluation methodology. While the paper mentions the benchmarks used and the primary metrics, it fails to provide the specific details on how these metrics are calculated for each benchmark. For instance, the paper states that the primary metric for coding tasks is token per second (TPS), but it does not explain how TPS is calculated for each specific coding benchmark. Similarly, for reasoning tasks, the paper mentions accuracy and perplexity, but it does not specify the exact criteria for accuracy or the method used to calculate perplexity. This lack of detail makes it difficult to understand the evaluation protocol fully and to reproduce the results. The absence of clear evaluation protocols is a major limitation, as it hinders the ability of other researchers to validate the findings and build upon the proposed approach. My confidence in this assessment is high, as the paper consistently lacks these crucial details throughout the 'Experiments' section. Another significant weakness is the absence of a detailed analysis of the computational resources required for training and inference. The paper describes the training infrastructure and the RL framework used, but it does not provide specific details about the computational resources, such as the type and number of GPUs, CPUs, and memory, that are necessary to run the model efficiently. This lack of information makes it difficult for other researchers to reproduce the results and assess the practical applicability of the proposed approach. The computational cost of the model is a crucial factor in determining its feasibility, and the absence of this information is a significant limitation. My confidence in this assessment is also high, as the paper consistently omits these details throughout the 'Experiments' section. These two weaknesses, the lack of detailed evaluation protocols and the absence of computational resource specifications, significantly impact the reproducibility and practical utility of the research. The lack of clarity in the evaluation methodology makes it difficult to assess the true impact of the proposed approach, while the absence of computational resource information limits the ability of other researchers to replicate the results and assess the practical applicability of the model. These issues need to be addressed to ensure the validity and usefulness of the research.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First and foremost, the paper needs to provide a detailed breakdown of the evaluation metrics used for each benchmark. This should include the specific metrics used (e.g., BLEU score, ROUGE score, accuracy, F1 score), how these metrics are calculated (e.g., automatic evaluation using a library, manual evaluation by human annotators), and the specific parameters used for each benchmark. For example, if the BLEU score is used, the paper should specify the version of the BLEU metric used (e.g., BLEU-1, BLEU-2, BLEU-3, BLEU-4) and the averaging method (e.g., arithmetic mean, geometric mean). Similarly, for ROUGE score, the paper should specify the type of ROUGE score used (e.g., ROUGE-1, ROUGE-2, ROUGE-L) and the stemming or not stemming. For task-specific metrics, the paper should provide the exact definition of the metric and how it is calculated. This detailed information will allow other researchers to reproduce the results and validate the findings. I also recommend including additional metrics that are relevant to the specific tasks being evaluated, such as perplexity or task-specific accuracy, to provide a more comprehensive evaluation. This will help to provide a more robust assessment of the proposed method's performance. Second, the paper should provide a detailed analysis of the computational resources required for training and inference. This should include the memory requirements during both training and inference, including the peak memory usage and the memory footprint of different model components. The paper should also specify the hardware requirements, such as the type and number of GPUs, CPUs, and memory, that are necessary to run the model efficiently. This information is crucial for researchers who want to replicate the results and apply the model to their own problems. Without this, it is difficult to assess the practical applicability of the proposed approach. Furthermore, the paper should include a detailed analysis of the computational time needed for both training and inference. This should include the wall-clock time for training the model, as well as the inference time for generating text samples. It would be useful to provide a breakdown of the time spent on different parts of the process, such as the diffusion steps, the token editing, and the decoding. This would allow researchers to identify potential bottlenecks and optimize the performance of the model. The authors should also discuss the scalability of the approach, including how the computational cost scales with the size of the model and the length of the generated text. This is important for understanding the limitations of the approach and for identifying potential areas for improvement. The authors should also consider providing a comparison of the computational cost of LLaDA2.1 with other existing models, to give a better context for the efficiency of the proposed approach. Finally, the paper should also discuss the practical implications of the proposed approach in terms of its usability and accessibility. For example, the authors should discuss the ease of use of the model, the availability of pre-trained models, and the support for different programming languages and frameworks. This is important for researchers who want to use the model in their own work. The authors should also discuss the limitations of the approach and the potential challenges that researchers might face when using the model. This would help to provide a more balanced and realistic assessment of the proposed approach. By addressing these points, the authors can make the paper more accessible and useful to the broader research community.


## Questions:

I have several questions that arise from my analysis of the paper. First, how does the computational cost of LLaDA2.1 compare to other existing models in terms of training and inference time? While the paper highlights the speed advantages of the proposed approach in certain tasks, it does not provide a direct comparison of the computational cost with other models. This information is crucial for assessing the practical applicability of the model. Second, what are the practical implications of the proposed approach in terms of its usability and accessibility? The paper does not discuss the ease of use of the model, the availability of pre-trained models, or the support for different programming languages and frameworks. This information is important for researchers who want to use the model in their own work. Third, how does the performance of LLaDA2.1 vary across different domains, and what are the potential challenges that researchers might face when using the model in different contexts? The paper presents results across a range of benchmarks, but it does not provide a detailed analysis of the performance variations across different domains. This information is important for understanding the limitations of the approach and for identifying potential areas for improvement. Fourth, what are the specific criteria used to determine the thresholds for the draft and edit modes, and how do these thresholds affect the performance of the model? The paper introduces the concepts of 'Speedy Mode' and 'Quality Mode' but does not provide a detailed explanation of how the thresholds for these modes are determined. This information is important for understanding the behavior of the model and for optimizing its performance. Finally, what are the limitations of the proposed approach, and what are the potential areas for future research? The paper does not explicitly discuss the limitations of the approach or the potential challenges that researchers might face when using the model. This information is important for understanding the scope of the research and for identifying potential areas for future work. These questions are crucial for a comprehensive understanding of the proposed approach and its practical implications.


## Rating:

7.0


## Confidence:

2.75


## Decision:

Accept
}