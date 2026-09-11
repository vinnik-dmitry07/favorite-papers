I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper proposes a new paradigm for multi-LLM collaboration, Cache-to-Cache (C2C), which leverages the KV cache in LLMs as a medium for semantic communication. The authors conduct extensive experiments to demonstrate the effectiveness of their approach.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The authors conduct extensive experiments to demonstrate the effectiveness of their approach.
3. The authors provide a detailed analysis of the results, including ablation studies and error analysis.

### Weaknesses

#### Some Related Works


#### comment

1. The authors should provide more details on the implementation of the C2C paradigm, including the specific layers and tokens used for KV cache fusion, and the criteria for selecting these layers and tokens. The lack of clarity on how the KV cache is partitioned and which parts are shared across different models makes it difficult to reproduce the results and understand the practical implications of the proposed method.
2. The authors should provide more details on the training process, including the specific hyperparameters used, the optimization algorithm, and the convergence criteria. The absence of these details makes it challenging to assess the robustness of the training process and the generalizability of the results. For example, what is the learning rate schedule, batch size, and the number of training epochs? How is the loss function defined and optimized?
3. The authors should provide more details on the evaluation metrics used, including how they are calculated and what they measure. The paper should also discuss the limitations of the evaluation metrics and how they might affect the interpretation of the results. For instance, are the metrics sensitive to the length of the generated text, and how do they compare to other commonly used metrics in the field?

### Suggestions

The paper would benefit significantly from a more detailed explanation of the KV cache fusion mechanism. Specifically, the authors should clarify how the KV cache is partitioned across different models and which parts of the cache are shared. For example, are the shared layers the same across all models, or are they selected based on some criteria? What is the impact of different partitioning strategies on the performance of the C2C paradigm? Furthermore, the authors should provide a more in-depth analysis of the token-level fusion process. How are the KV caches from different models aligned and combined? Are there any specific techniques used to handle potential misalignments? A more detailed explanation of these aspects would greatly enhance the clarity and reproducibility of the proposed method.

To improve the reproducibility and robustness of the results, the authors should provide a comprehensive description of the training process. This should include all relevant hyperparameters, such as the learning rate, batch size, and the number of training epochs. The authors should also specify the optimization algorithm used and the convergence criteria. It would be beneficial to include a detailed discussion of the loss function, including how it is defined and optimized. Furthermore, the authors should provide an analysis of the sensitivity of the results to different hyperparameter settings. This would help to establish the robustness of the proposed method and provide a better understanding of the factors that influence its performance. For example, how does the learning rate affect the convergence speed and the final performance of the model? How does the batch size impact the stability of the training process?

Finally, the authors should provide a more thorough discussion of the evaluation metrics used in the paper. They should clearly define how each metric is calculated and what it measures. It is also important to discuss the limitations of the chosen metrics and how they might affect the interpretation of the results. For instance, are the metrics sensitive to the length of the generated text? How do they compare to other commonly used metrics in the field? The authors should also discuss the potential biases of the evaluation metrics and how they might influence the conclusions drawn from the experiments. A more detailed analysis of the evaluation metrics would help to ensure that the results are reliable and meaningful. For example, how do the results change when using different evaluation metrics, and what are the implications of these changes?

### Questions

1. How does the C2C paradigm handle cases where the KV caches from different models have different sizes or structures?
2. How does the C2C paradigm perform when the Sharer and Receiver models have different architectures or sizes?

### Rating

6

### Confidence

3

**********

## Reviewer 2

### Summary

This paper proposes a new paradigm for multi-LLM systems, Cache-to-Cache (C2C), which leverages the KV cache as a medium for semantic communication between LLMs. The authors demonstrate that enriching the KV cache under the same context length can improve response quality, and that different LLMs encode distinct semantic understandings and contextual knowledge of the same input. They also show that a learnable gating mechanism can select the target layers that benefit from cache communication. Experiments show that C2C achieves 6.4-14.2% higher average accuracy than individual models and 3.1-5.4% while delivering an average 2.5× speedup in latency.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach to multi-LLM systems by leveraging the KV cache as a medium for semantic communication, which is a departure from traditional text-based communication methods. This approach is innovative and has the potential to improve the efficiency and effectiveness of multi-LLM systems.
2. The paper provides a thorough analysis of the proposed approach, including experiments on various benchmarks and tasks. The results demonstrate the effectiveness of C2C in improving response quality and reducing latency compared to text-based communication methods.
3. The paper is well-written and easy to understand, with clear explanations of the proposed approach and experimental results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational overhead of the proposed approach, including the cost of KV cache fusion and gating. It would be beneficial to provide a more detailed analysis of the computational cost of the proposed approach, including the cost of KV cache fusion and gating. Specifically, the paper should quantify the additional FLOPs and memory access patterns introduced by the cache fusion and gating mechanisms. This analysis should also consider the impact on different hardware platforms, as the overhead might vary significantly across different architectures.
2. The paper does not explore the potential limitations of the proposed approach, such as the impact of cache size on performance. It would be beneficial to explore the impact of cache size on performance and identify the optimal cache size for different tasks and models. The paper should also discuss the potential for cache eviction strategies and their impact on the overall performance of the system. For example, how does the system handle situations where the cache is full or when the cache becomes outdated?

### Suggestions

The paper should provide a more detailed analysis of the computational overhead introduced by the cache fusion and gating mechanisms. This analysis should include a breakdown of the FLOPs required for each operation, as well as the memory access patterns. It would be beneficial to compare the computational cost of C2C with that of traditional text-based communication methods, not just in terms of latency but also in terms of energy consumption. Furthermore, the analysis should consider the impact of different hardware platforms, such as GPUs with varying memory bandwidth and cache sizes. This would provide a more comprehensive understanding of the practical implications of using C2C in different environments. For example, the paper could analyze how the overhead scales with the number of LLMs in the multi-LLM system and the size of the KV cache.

To address the limitations of the proposed approach, the paper should explore the impact of cache size on performance. This could involve conducting experiments with different cache sizes and analyzing the trade-offs between performance and memory usage. The paper should also discuss the potential for cache eviction strategies and their impact on the overall performance of the system. For example, the paper could investigate the use of LRU or LFU policies for cache eviction and analyze their effectiveness in maintaining the quality of the KV cache. The paper should also discuss the potential for adaptive cache sizing, where the cache size is dynamically adjusted based on the task and the available resources. This would allow the system to optimize performance for different scenarios.

Finally, the paper should explore the robustness of the proposed approach to different types of errors and inconsistencies in the KV caches. For example, how does the system handle situations where the KV caches from different LLMs contain conflicting information? The paper could investigate the use of conflict resolution mechanisms and analyze their impact on the overall performance of the system. Additionally, the paper should discuss the potential for using error detection and correction techniques to improve the reliability of the KV cache communication. This would be particularly important in scenarios where the LLMs are operating in noisy or unreliable environments.

### Questions

1. How does the proposed approach handle situations where the KV caches from different LLMs contain errors or inconsistencies?
2. What are the potential limitations of the proposed approach, such as the impact of cache size on performance?

### Rating

6

### Confidence

4

**********

## Reviewer 3

### Summary

This paper introduces Cache-to-Cache (C2C), a novel approach for multi-LLM systems that leverages the key-value (KV) cache as a medium for semantic communication between models. Unlike traditional text-based communication, C2C directly projects and fuses the KV caches from different models to enable direct semantic transfer. The authors demonstrate through experiments that C2C achieves higher accuracy than individual models and improves latency by up to 2.5×. The approach is validated across various benchmarks and model combinations, showcasing its potential for enhancing multi-LLM systems.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper introduces a novel approach, Cache-to-Cache (C2C), which leverages the KV cache as a medium for semantic communication between LLMs. This is a significant departure from traditional text-based communication methods and offers a promising direction for improving multi-LLM systems.
- The paper provides extensive experiments across various benchmarks and model combinations, demonstrating the effectiveness of C2C in improving response quality and reducing latency.
- The paper is well-organized and clearly written, making it easy to understand the proposed approach and the experimental results.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational overhead of the proposed approach, including the cost of KV cache fusion and gating. It would be beneficial to provide a more detailed analysis of the computational cost of the proposed approach, including the cost of KV cache fusion and gating. Specifically, the paper should quantify the additional FLOPs and memory access patterns introduced by the cache fusion and gating mechanisms. This analysis should also consider the impact on different hardware platforms, as the overhead might vary significantly across different architectures.
- The paper does not explore the potential limitations of the proposed approach, such as the impact of cache size on performance. It would be beneficial to explore the impact of cache size on performance and identify the optimal cache size for different tasks and models. The paper should also discuss the potential for cache eviction strategies and their impact on the overall performance of the system. For example, how does the system handle situations where the cache is full or when the cache becomes outdated?

### Suggestions

The paper should include a more thorough analysis of the computational costs associated with the proposed C2C approach. Specifically, the authors should provide a detailed breakdown of the FLOPs required for the KV cache fusion and gating operations. This should include a comparison of the computational cost of C2C with that of traditional text-based communication methods. Furthermore, the analysis should consider the memory access patterns and the impact of different hardware platforms, such as GPUs with varying memory bandwidth and cache sizes. This would provide a more comprehensive understanding of the practical implications of using C2C in different environments. The authors could also explore techniques to optimize the computational efficiency of the C2C approach, such as using sparse matrix operations or hardware acceleration.

To address the limitations of the proposed approach, the paper should include a more detailed analysis of the impact of cache size on performance. The authors should conduct experiments with different cache sizes and analyze the trade-offs between performance and memory usage. This analysis should also consider the impact of cache eviction strategies on the overall performance of the system. For example, the paper could investigate the use of LRU or LFU policies for cache eviction and analyze their effectiveness in maintaining the quality of the KV cache. The authors should also discuss the potential for adaptive cache sizing, where the cache size is dynamically adjusted based on the task and the available resources. This would allow the system to optimize performance for different scenarios.

Finally, the paper should explore the robustness of the proposed approach to different types of errors and inconsistencies in the KV caches. For example, how does the system handle situations where the KV caches from different LLMs contain conflicting information? The paper could investigate the use of conflict resolution mechanisms and analyze their impact on the overall performance of the system. Additionally, the paper should discuss the potential for using error detection and correction techniques to improve the reliability of the KV cache communication. This would be particularly important in scenarios where the LLMs are operating in noisy or unreliable environments. The authors should also consider the impact of different types of errors, such as missing or corrupted cache entries, on the overall performance of the system.

### Questions

- How does the proposed approach handle situations where the KV caches from different LLMs contain errors or inconsistencies?
- What are the potential limitations of the proposed approach, such as the impact of cache size on performance?

### Rating

8

### Confidence

3

**********

## Reviewer 4

### Summary

This paper proposes a novel method called Cache-to-Cache (C2C) for multi-LLM systems. C2C uses the key-value (KV) cache of one model (Sharer) to enhance the performance of another model (Receiver) by projecting and fusing the Sharer’s KV cache with the Receiver’s. The paper evaluates C2C on four benchmarks and compares it with text-based communication and query routing methods. The results show that C2C outperforms text-based communication by 5-10% and is 2-5 times faster than text-based communication.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach for multi-LLM systems by leveraging the KV cache as a medium for semantic communication. This is a creative and innovative idea that has the potential to significantly improve the efficiency and effectiveness of multi-LLM systems.
2. The paper provides a thorough evaluation of C2C on four benchmarks and compares it with text-based communication and query routing methods. The results demonstrate that C2C outperforms text-based communication by 5-10% and is 2-5 times faster, which is a significant achievement.
3. The paper is well-written and easy to follow. The authors provide clear explanations of the proposed method and the experimental setup. The results are presented in a clear and concise manner, making it easy for readers to understand the findings.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational overhead of the proposed approach, including the cost of KV cache fusion and gating. It would be beneficial to provide a more detailed analysis of the computational cost of the proposed approach, including the cost of KV cache fusion and gating. Specifically, the paper should quantify the additional FLOPs and memory access patterns introduced by the cache fusion and gating mechanisms. This analysis should also consider the impact on different hardware platforms, as the overhead might vary significantly across different architectures.
2. The paper does not explore the potential limitations of the proposed approach, such as the impact of cache size on performance. It would be beneficial to explore the impact of cache size on performance and identify the optimal cache size for different tasks and models. The paper should also discuss the potential for cache eviction strategies and their impact on the overall performance of the system. For example, how does the system handle situations where the cache is full or when the cache becomes outdated?
3. The paper does not discuss the potential impact of the proposed approach on the privacy of the models. It would be beneficial to discuss the potential impact of the proposed approach on the privacy of the models and how to mitigate any potential privacy risks. For example, how does the system handle situations where the KV cache contains sensitive information?
4. The paper does not provide a detailed analysis of the error propagation in the proposed approach. It would be beneficial to provide a detailed analysis of the error propagation in the proposed approach and how it affects the overall performance of the system. For example, how does the system handle situations where the Sharer's KV cache contains errors or inconsistencies?

### Suggestions

The paper would benefit from a more thorough analysis of the computational costs associated with the Cache-to-Cache (C2C) approach. Specifically, the authors should provide a detailed breakdown of the FLOPs required for the KV cache fusion and gating operations. This should include a comparison of the computational cost of C2C with that of traditional text-based communication methods. Furthermore, the analysis should consider the memory access patterns and the impact of different hardware platforms, such as GPUs with varying memory bandwidth and cache sizes. This would provide a more comprehensive understanding of the practical implications of using C2C in different environments. The authors should also explore techniques to optimize the computational efficiency of the C2C approach, such as using sparse matrix operations or hardware acceleration.

In addition to computational costs, the paper should also explore the potential limitations of the proposed approach, such as the impact of cache size on performance. The authors should conduct experiments with different cache sizes and analyze the trade-offs between performance and memory usage. This analysis should also consider the impact of cache eviction strategies on the overall performance of the system. For example, the paper could investigate the use of LRU or LFU policies for cache eviction and analyze their effectiveness in maintaining the quality of the KV cache. The authors should also discuss the potential for adaptive cache sizing, where the cache size is dynamically adjusted based on the task and the available resources. This would allow the system to optimize performance for different scenarios.

Finally, the paper should address the potential impact of the proposed approach on the privacy of the models. The authors should discuss the potential privacy risks associated with the use of the KV cache and how to mitigate these risks. For example, the paper could explore techniques to anonymize or obfuscate the KV cache to protect sensitive information. The authors should also analyze the potential for error propagation in the proposed approach and how it affects the overall performance of the system. This analysis should include a discussion of how the system handles situations where the Sharer's KV cache contains errors or inconsistencies. The paper should also consider the implications of using C2C in scenarios where the models are operating in noisy or unreliable environments.

### Questions

1. How does the proposed approach handle situations where the KV caches from different LLMs contain errors or inconsistencies?
2. What are the potential limitations of the proposed approach, such as the impact of cache size on performance?
3. How does the proposed approach impact the privacy of the models?
4. How does the proposed approach handle situations where the Sharer's KV cache contains errors or inconsistencies?

### Rating

8

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

**Plan:**
1. Go through each reviewer's identified weaknesses one by one.
2. For each weakness, categorize it as theoretical, methodological, experimental, or practical.
3. Find specific evidence in the paper (quotes, table references, section numbers) to support the reviewer's claim.
4. If the weakness is about missing information, point out where the information is indeed missing.
5. If the weakness is about a lack of analysis, confirm that the analysis is indeed lacking.
6. Finally, conclude whether the weakness is valid, partially valid, or invalid based on the evidence found.
**Review 1 Weaknesses:**

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational overhead of the proposed approach, including the cost of KV cache fusion and gating. It would be beneficial to provide a detailed analysis of the computational cost of the proposed approach, including the cost of KV cache fusion and gating. Specifically, the paper should quantify the additional FLOPs and memory access patterns introduced by the cache fusion and gating mechanisms. This analysis should also consider the impact on different hardware platforms, as the overhead might vary significantly across different architectures."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper describes the C2C method in Section 3.3.1, detailing the projection module and the fusion process. However, it does not provide any quantitative analysis of the computational cost.
   - The "Training Scheme" in Section 3.3.4 mentions freezing the Sharer and Receiver models, but doesn't discuss the computational cost of the C2C module itself.
b) Experiment-related Evidence:
   - The "Experiments" section (Section 4) focuses on accuracy and latency improvements. There is no mention of computational cost, FLOPs, or memory access patterns.

3. Literature Gap Analysis:
   - The paper does not cite any works that specifically analyze the computational cost of KV cache operations in multi-LLM systems.

4. Validation Analysis:
   - The reviewer correctly points out the absence of a detailed computational cost analysis. The paper focuses on the benefits of C2C in terms of accuracy and latency but lacks any discussion or quantification of the computational overhead introduced by the proposed method. The reviewer's suggestion to analyze FLOPs, memory access patterns, and the impact on different hardware platforms is valid and would strengthen the paper.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of computational cost analysis in the "Method" and "Experiments" sections.

1. Weakness Statement:
"The paper does not explore the potential limitations of the proposed approach, such as the impact of cache size on performance. It would be beneficial to explore the impact of cache size on performance and identify the optimal cache size for different tasks and models. The paper should also discuss the potential for cache eviction strategies and their impact on the overall performance of the system. For example, how does the system handle situations where the cache is full or when the cache becomes outdated?"

2. Evidence Collection:
a) Method-related Evidence:
   - The "Cache Alignment" section (3.3.3) mentions aligning the Sharer and Receiver layers, but doesn't discuss the size of the KV cache or its impact.
   - The "Model Alignment" section (3.3.4) mentions freezing layers and the token alignment strategy, but again, not in the context of cache size.
b) Experiment-related Evidence:
   - The "Scaling Model Sizes" experiment (Section 4.3) varies the Sharer and Receiver models but doesn't systematically explore different sizes of the KV cache within a model.
   - The paper doesn't discuss cache eviction strategies or their implications.

3. Literature Gap Analysis:
   - The paper doesn't cite works on KV cache management strategies in LLMs.

4. Validation Analysis:
   - The reviewer's criticism is valid. The paper lacks an investigation into how the size of the KV cache affects the performance of C2C. The potential for cache eviction and its impact on the system's effectiveness are also not addressed.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of cache size experiments and discussion of cache eviction strategies in the "Experiments" and "Method" sections.

1. Weakness Statement:
"The paper should provide a more detailed analysis of the computational overhead introduced by the cache fusion and gating mechanisms. This analysis should include a breakdown of the FLOPs required for each operation, as well as the memory access patterns. It would be beneficial to compare the computational cost of C2C with that of traditional text-based communication methods, not just in terms of latency but also in terms of energy consumption. Furthermore, the analysis should consider the impact of different hardware platforms, such as GPUs with varying memory bandwidth and cache sizes. This would provide a more comprehensive understanding of the practical implications of using C2C in different environments. For example, the paper could analyze how the overhead scales with the number of LLMs in the multi-LLM system and the size of the KV cache."

2. Evidence Collection:
a) Method-related Evidence:
   - As mentioned before, the "Method" section lacks any quantitative analysis of computational cost.
b) Experiment-related Evidence:
   - The "Experiments" section focuses on accuracy and latency. There is no analysis of FLOPs, memory access patterns, energy consumption, or the impact of different hardware platforms.

3. Literature Gap Analysis:
   - No relevant literature is cited regarding the computational cost of KV cache operations.

4. Validation Analysis:
   - This is a more detailed reiteration of the first weakness, emphasizing the need for a more comprehensive analysis including FLOPs, memory access, energy consumption, and hardware platform impact. The reviewer's suggestions for further analysis are valid and would provide a more complete picture of C2C's practical implications.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of computational cost analysis in the "Method" and "Experiments" sections.

1. Weakness Statement:
"To address the limitations of the proposed approach, the paper should include a more detailed analysis of the impact of cache size on performance. This could involve conducting experiments with different cache sizes and analyzing the trade-offs between performance and memory usage. The paper should also discuss the potential for cache eviction strategies and their impact on the overall performance of the system. For example, the paper could investigate the use of LRU or LFU policies for cache eviction and analyze their effectiveness in maintaining the quality of the KV cache. The paper should also discuss the potential for adaptive cache sizing, where the cache size is dynamically adjusted based on the task and the available resources. This would allow the system to optimize performance for different scenarios."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper describes the KV cache fusion process but doesn't discuss the size of the cache or its impact.
b) Experiment-related Evidence:
   - The experiments do not vary the size of the KV cache. There is no discussion of cache eviction strategies or adaptive cache sizing.

3. Literature Gap Analysis:
   - No relevant literature on KV cache management strategies is cited.

4. Validation Analysis:
   - This is a more detailed reiteration of the second weakness, emphasizing the need for experiments and discussion related to cache size and eviction strategies. The reviewer's suggestions for exploring these aspects are valid and would strengthen the paper.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of cache size experiments and discussion of cache eviction strategies in the "Experiments" and "Method" sections.

1. Weakness Statement:
"Finally, the paper should explore the robustness of the proposed approach to different types of errors and inconsistencies in the KV caches. For example, how does the system handle situations where the KV caches from different LLMs contain conflicting information? The paper could investigate the use of conflict resolution mechanisms and analyze their impact on the overall performance of the system. Additionally, the paper should discuss the potential for using error detection and correction techniques to improve the reliability of the KV cache communication. This would be particularly important in scenarios where the LLMs are operating in noisy or unreliable environments. The authors should also consider the impact of different types of errors, such as missing or corrupted cache entries, on the overall performance of the system."

2. Evidence Collection:
a) Method-related Evidence:
   - The "Cache Fusion" section (3.3.1) describes the projection and fusion process but doesn't address errors or inconsistencies in the input KV caches.
b) Experiment-related Evidence:
   - The experiments assume the input KV caches are correct. There is no evaluation of the system's robustness to errors or inconsistencies.

3. Literature Gap Analysis:
   - The paper does not cite works on conflict resolution or error handling in multi-LLM systems or KV caches.

4. Validation Analysis:
   - The reviewer raises a valid concern about the robustness of C2C to errors and inconsistencies in the KV caches. The paper lacks any discussion or experimental evaluation of this aspect.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of discussion and experiments related to error handling and robustness in the "Method" and "Experiments" sections.

**Review 2 Weaknesses:**

1. Weakness Statement:
"The authors should provide more details on the implementation of the C2C paradigm, including the specific layers and tokens used for KV cache fusion, and the criteria for selecting these layers and tokens. The lack of clarity on how the KV cache is partitioned and which parts are shared across different models makes it difficult to reproduce the results and understand the practical implications of the proposed method."

2. Evidence Collection:
a) Method-related Evidence:
   - The "Cache Fusion" section (3.3.1) states: "During the decoding phase, with the current token y_i and caches from the input and the generated prefix, the next token is predicted as y_i + 1 = P_{f}(C_{[,|E|:|E|+|X|]}(X) + F_{G}(C_{G}))". This indicates that the entire KV caches are used.
   - The "Model Alignment" section (3.3.4) mentions aligning layers based on token alignment, but the specific layers and tokens are not detailed in the main method description. Appendix A.1.1 provides more details on layer alignment.

3. Literature Gap Analysis:
   - Not applicable here.

4. Validation Analysis:
   - The reviewer is partially correct. While the main method description doesn't explicitly state that the entire KV cache is used, Appendix A.1.1 clarifies this. However, the criteria for selecting layers for alignment and the specific tokens used for fusion are not detailed in the main text, making it harder to understand the practical implementation.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: Main text lacks specific details on layer and token selection for fusion, while Appendix A.1.1 provides more information.

1. Weakness Statement:
"The authors should provide more details on the training process, including the specific hyperparameters used, the optimization algorithm, and the convergence criteria. The absence of these details makes it challenging to assess the robustness of the training process and the generalizability of the results. For example, what is the learning rate schedule, batch size, and the number of training epochs? How is the loss function defined and optimized?"

2. Evidence Collection:
a) Method-related Evidence:
   - The "Training Scheme" section (3.3.4) mentions freezing models, using standard next-token prediction loss, and employing a residual integration strategy. However, specific hyperparameters, optimization algorithm details, and convergence criteria are not provided in the main text.
b) Experiment-related Evidence:
   - Appendix A.3.2 provides some training details, including learning rate, batch size, and number of epochs.

3. Literature Gap Analysis:
   - Not applicable here.

4. Validation Analysis:
   - The reviewer is partially correct. While the main text lacks specific training details, Appendix A.3.2 provides some of this information. However, the reviewer's point about the absence of these details in the main text remains valid, as it hinders the assessment of the training process's robustness and generalizability.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: Lack of specific training details in the main text, but some details are provided in Appendix A.3.2.

1. Weakness Statement:
"The authors should provide more details on the evaluation metrics used, including how they are calculated and what they measure. The paper should also discuss the limitations of the evaluation metrics and how they might affect the interpretation of the results. For instance, are the metrics sensitive to the length of the generated text, and how do they compare to other commonly used metrics in the field?"

2. Evidence Collection:
a) Experiment-related Evidence:
   - The "Evaluation settings" section (4.1) states: "We use average accuracy as the performance metric. We use text generation and answer extraction as the evaluation mode for C2C and baselines, with the max generation length set to 64 for multi-choice benchmarks. All experiments are conducted in the zero-shot setting with zero generation temperature to ensure reproducibility."
   - The paper doesn't explicitly discuss the limitations of using average accuracy or compare it to other metrics like BLEU or ROUGE.

3. Literature Gap Analysis:
   - Not applicable here.

4. Validation Analysis:
   - The reviewer is correct. The paper primarily uses average accuracy and doesn't delve into the limitations of this metric or compare it to other commonly used evaluation metrics in NLP. The sensitivity of accuracy to text length is also not discussed.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper states the use of average accuracy without discussing its limitations or comparison to other metrics.

**Review 3 Weaknesses:**

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational overhead of the proposed approach, including the cost of KV cache fusion and gating. It would be beneficial to provide a more detailed analysis of the computational cost of the proposed approach, including the cost of KV cache fusion and gating. Specifically, the paper should quantify the additional FLOPs and memory access patterns introduced by the cache fusion and gating mechanisms. This analysis should also consider the impact on different hardware platforms, as the overhead might vary significantly across different architectures."

2. Evidence Collection:
   - This is the same weakness identified by Reviewer 1, and the evidence and analysis are the same. Please refer to the analysis for Reviewer 1's first weakness.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1's first weakness.

1. Weakness Statement:
"The paper does not explore the potential limitations of the proposed approach, such as the impact of cache size on performance. It would be beneficial to explore the impact of cache size on performance and identify the optimal cache size for different tasks and models. The paper should also discuss the potential for cache eviction strategies and their impact on the overall performance of the system. For example, how does the system handle situations where the cache is full or when the cache becomes outdated?"

2. Evidence Collection:
   - This is the same weakness identified by Reviewer 1, and the evidence and analysis are the same. Please refer to the analysis for Reviewer 1's second weakness.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1's second weakness.

1. Weakness Statement:
"The paper should provide a more detailed analysis of the computational overhead introduced by the cache fusion and gating mechanisms. This analysis should include a breakdown of the FLOPs required for each operation, as well as the memory access patterns. It would be beneficial to compare the computational cost of C2C with that of traditional text-based communication methods, not just in terms of latency but also in terms of energy consumption. Furthermore, the analysis should consider the impact of different hardware platforms, such as GPUs with varying memory bandwidth and cache sizes. This would provide a more comprehensive understanding of the practical implications of using C2C in different environments. For example, the paper could analyze how the overhead scales with the number of LLMs in the multi-LLM system and the size of the KV cache."

2. Evidence Collection:
   - This is a more detailed reiteration of the first weakness, emphasizing the need for a more comprehensive analysis including FLOPs, memory access, energy consumption, and hardware platform impact. The reviewer's suggestions for further analysis are valid and would provide a more complete picture of C2C's practical implications.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1's first weakness.

1. Weakness Statement:
"To address the limitations of the proposed approach, the paper should include a more detailed analysis of the impact of cache size on performance. This could involve conducting experiments with different cache sizes and analyzing the trade-offs between performance and memory usage. The paper should also discuss the potential for cache eviction strategies and their impact on the overall performance of the system. For example, the paper could investigate the use of LRU or LFU policies for cache eviction and analyze their effectiveness in maintaining the quality of the KV cache. The paper should also discuss the potential for adaptive cache sizing, where the cache size is dynamically adjusted based on the task and the available resources. This would allow the system to optimize performance for different scenarios."

2. Evidence Collection:
   - This is the same weakness identified by Reviewer 1, and the evidence and analysis are the same. Please refer to the analysis for Reviewer 1's second weakness.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1's second weakness.

1. Weakness Statement:
"Finally, the paper should explore the robustness of the proposed approach to different types of errors and inconsistencies in the KV caches. For example, how does the system handle situations where the KV caches from different LLMs contain conflicting information? The paper could investigate the use of conflict resolution mechanisms and analyze their impact on the overall performance of the system. Additionally, the paper should discuss the potential for using error detection and correction techniques to improve the reliability of the KV cache communication. This would be particularly important in scenarios where the LLMs are operating in noisy or unreliable environments. The authors should also consider the impact of different types of errors, such as missing or corrupted cache entries, on the overall performance of the system."

2. Evidence Collection:
   - This is the same weakness identified by Reviewer 1, and the evidence and analysis are the same. Please refer to the analysis for Reviewer 1's fourth weakness.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1's fourth weakness.

**Review 4 Weaknesses:**

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational overhead of the proposed approach, including the cost of KV cache fusion and gating. It would be beneficial to provide a more detailed analysis of the computational cost of the proposed approach, including the cost of KV cache fusion and gating. Specifically, the paper should quantify the additional FLOPs and memory access patterns introduced by the cache fusion and gating mechanisms. This analysis should also consider the impact on different hardware platforms, as the overhead might vary significantly across different architectures."

2. Evidence Collection:
   - This is the same weakness identified by Reviewer 1 and 3, and the evidence and analysis are the same. Please refer to the analysis for Reviewer 1's first weakness.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1's first weakness.

1. Weakness Statement:
"The paper does not explore the potential limitations of the proposed approach, such as the impact of cache size on performance. It would be beneficial to explore the impact of cache size on performance and identify the optimal cache size for different tasks and models. The paper should also discuss the potential for cache eviction strategies and their impact on the overall performance of the system. For example, how does the system handle situations where the cache is full or when the cache becomes outdated?"

2. Evidence Collection:
   - This is the same weakness identified by Reviewer 1 and 3, and the evidence and analysis are the same. Please refer to the analysis for Reviewer 1's second weakness.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1's second weakness.

1. Weakness Statement:
"The paper does not discuss the potential impact of the proposed approach on the privacy of the models. It would be beneficial to discuss the potential impact of the proposed approach on the privacy of the models and how to mitigate any potential privacy risks. For example, how does the system handle situations where the KV cache contains sensitive information?"

2. Evidence Collection:
a) Method-related Evidence:
   - The "Method" section does not discuss privacy implications.
b) Experiment-related Evidence:
   - The "Experiments" section does not include any privacy-related evaluations or discussions.

3. Literature Gap Analysis:
   - The paper does not cite works on KV cache privacy or security.

4. Validation Analysis:
   - The reviewer raises a valid concern about the privacy implications of sharing KV caches. The paper lacks any discussion or analysis of this aspect.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of privacy discussion in the "Method" and "Experiments" sections.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the error propagation in the proposed approach. It would be beneficial to provide a detailed analysis of the error propagation in the proposed approach and how it affects the overall performance of the system. For example, how does the system handle situations where the Sharer's KV cache contains errors or inconsistencies?"

2. Evidence Collection:
a) Method-related Evidence:
   - The "Cache Fusion" section (3.3.1) describes the projection and fusion process but doesn't address errors or inconsistencies in the input KV caches.
b) Experiment-related Evidence:
   - The experiments assume the input KV caches are correct. There is no evaluation of the system's robustness to errors or inconsistencies.

3. Literature Gap Analysis:
   - The paper does not cite works on error propagation in multi-LLM systems or KV caches.

4. Validation Analysis:
   - This is the same weakness identified by Reviewer 1's fourth weakness, and the evidence and analysis are the same.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of error propagation analysis in the "Method" and "Experiments" sections.

**Synthesis and Reflection:**

After analyzing the weaknesses identified by the four reviewers, several recurring themes emerge:

*   **Computational Overhead:** All reviewers implicitly or explicitly point out the lack of a detailed analysis of the computational cost associated with the C2C approach. This includes FLOPs, memory access patterns, and the impact on different hardware platforms.
*   **Cache Size and Limitations:** Reviewers 1, 3, and 4 all raise concerns about the impact of cache size on performance and the potential for cache eviction strategies. Reviewer 1 also suggests exploring the optimal cache size.
*   **Robustness and Error Handling:** Reviewers 1 and 4 highlight the need for an analysis of the system's robustness to errors and inconsistencies in the KV caches. This includes how the system handles conflicting information or corrupted caches.
*   **Missing Details:** Reviewer 2 points out the lack of specific details regarding the implementation of the C2C paradigm and the training process.

There are no significant contradictions between the reviewers' opinions. They largely converge on the key areas where the paper could be strengthened.

**Distinguishing Valid from Invalid Criticisms:**

All the identified weaknesses appear to be **valid**. The reviewers have pointed out genuine gaps in the paper's analysis and experimental evaluation. While some reviewers rephrased the same concerns (e.g., Reviewer 1's first and second weaknesses are similar), the underlying criticisms about missing computational analysis, cache size impact, robustness, and implementation details are consistently raised.

**Overall Conclusion:**

The reviewers have collectively identified several valid weaknesses in the paper, primarily concerning the lack of detailed analysis in certain areas. The most significant concerns revolve around the computational overhead, the impact of cache size, the robustness of the system to errors, and the level of detail provided in the implementation and training descriptions. Addressing these weaknesses would significantly strengthen the paper.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces Cache-to-Cache (C2C), a novel multi-LLM communication paradigm that leverages the key-value (KV) cache as a medium for semantic communication between Large Language Models (LLMs). Unlike traditional text-based communication, C2C directly projects and fuses the KV caches from a Sharer model into the cache of a Receiver model, enabling direct semantic transfer of information. The authors demonstrate that this approach achieves higher accuracy and reduced latency compared to text-based communication methods. The core idea is that the KV cache, which stores key-value pairs of tokens from previous interactions, contains rich semantic information that can be leveraged for inter-LLM communication. The C2C method involves a projection module that transforms the Sharer's KV cache into a format compatible with the Receiver's cache, followed by a fusion process that combines the projected Sharer cache with the Receiver's existing cache. A learnable gating mechanism is also incorporated to selectively integrate the Sharer's information. The authors conduct extensive experiments across various benchmarks and model combinations, comparing C2C against text-based communication and query routing methods. The results show that C2C consistently outperforms text-based communication in terms of accuracy and achieves a 2.5x speedup in latency. The paper also explores the impact of different model combinations and cache sizes on the performance of C2C. The findings suggest that C2C offers a promising alternative to traditional text-based communication for multi-LLM systems, potentially leading to more efficient and effective collaboration among LLMs. The authors also discuss the potential for future research, such as exploring different projection and fusion techniques, and applying C2C to more complex multi-agent scenarios. Overall, the paper presents a compelling case for the use of KV cache fusion as a viable approach for inter-LLM communication, with significant implications for the development of more efficient and effective multi-LLM systems.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

3.0


## Strengths:

The primary strength of this paper lies in its introduction of a novel approach to multi-LLM communication that moves beyond traditional text-based methods. By leveraging the KV cache as a medium for semantic communication, the authors have opened up a new avenue for inter-LLM interaction. This is a significant departure from conventional techniques and has the potential to improve the efficiency and effectiveness of multi-LLM systems. The idea of directly projecting and fusing KV caches is innovative and has the potential to significantly improve the performance of multi-LLM systems. The paper provides extensive experimental evidence to support the effectiveness of the C2C approach. The results consistently show that C2C outperforms text-based communication methods in terms of accuracy and achieves a 2.5x speedup in latency. This is a substantial achievement and demonstrates the practical value of the proposed method. The authors also explore the impact of different model combinations and cache sizes on the performance of C2C, providing valuable insights into the behavior of the system. The paper is well-organized and clearly written, making it easy to understand the proposed approach and the experimental results. The authors provide clear explanations of the C2C method and the experimental setup, which enhances the reproducibility of the work. The inclusion of a learnable gating mechanism is another strength of the paper. This mechanism allows the system to selectively integrate the Sharer's information, which can improve the overall performance of the C2C approach. The paper also discusses the potential for future research, such as exploring different projection and fusion techniques, and applying C2C to more complex multi-agent scenarios. This demonstrates the authors' commitment to further developing and refining the C2C approach. The paper's focus on practical applications of multi-LLM systems is also a strength. The authors demonstrate the potential of C2C to improve the efficiency and effectiveness of real-world multi-LLM applications. The paper's contribution to the field of multi-LLM systems is significant, and the C2C approach has the potential to be widely adopted in future research and applications.


## Weaknesses:

Despite the strengths of the paper, there are several notable weaknesses that need to be addressed. The most significant concern is the lack of a detailed analysis of the computational overhead introduced by the C2C approach. While the paper demonstrates that C2C achieves better accuracy and reduced latency compared to text-based communication, it fails to provide a quantitative analysis of the computational cost associated with the proposed method. Specifically, the paper does not quantify the additional FLOPs and memory access patterns introduced by the cache fusion and gating mechanisms. This is a critical omission, as the computational cost of C2C could potentially offset the performance gains achieved through reduced latency. Without a detailed analysis of the computational overhead, it is difficult to assess the practical implications of using C2C in different environments. The paper also lacks a thorough exploration of the impact of cache size on performance. The authors do not conduct experiments with different cache sizes and analyze the trade-offs between performance and memory usage. This is a significant limitation, as the optimal cache size for different tasks and models may vary. The paper also does not discuss the potential for cache eviction strategies and their impact on the overall performance of the system. For example, the paper does not investigate the use of LRU or LFU policies for cache eviction and analyze their effectiveness in maintaining the quality of the KV cache. The absence of this analysis makes it difficult to understand how the system handles situations where the cache is full or when the cache becomes outdated. Furthermore, the paper does not address the robustness of the proposed approach to different types of errors and inconsistencies in the KV caches. The experiments assume that the input KV caches are correct, but in real-world scenarios, the KV caches from different LLMs may contain conflicting information or be corrupted. The paper does not investigate how the system handles situations where the KV caches from different LLMs contain conflicting information, nor does it discuss the use of conflict resolution mechanisms. The paper also lacks a detailed analysis of the error propagation in the proposed approach. The authors do not analyze how the system handles situations where the Sharer's KV cache contains errors or inconsistencies. This is a critical omission, as errors in the Sharer's cache could propagate through the system and affect the overall performance. The paper also lacks specific details regarding the implementation of the C2C paradigm. While the main method description does not explicitly state that the entire KV cache is used, Appendix A.1.1 clarifies this. However, the criteria for selecting layers for alignment and the specific tokens used for fusion are not detailed in the main text, making it harder to understand the practical implementation. The paper also lacks specific details regarding the training process. While the main text lacks specific training details, Appendix A.3.2 provides some of this information. However, the reviewer's point about the absence of these details in the main text remains valid, as it hinders the assessment of the training process's robustness and generalizability. The paper primarily uses average accuracy as the performance metric, without discussing the limitations of this metric or comparing it to other commonly used metrics in the field. The sensitivity of accuracy to text length is also not discussed. Finally, the paper does not discuss the potential impact of the proposed approach on the privacy of the models. The paper lacks any discussion or analysis of this aspect. These weaknesses, taken together, significantly limit the practical implications of the paper and raise questions about the robustness and generalizability of the proposed approach. My confidence in these identified weaknesses is high, as they are based on a direct examination of the paper's content and the absence of key analyses and discussions.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First and foremost, the paper needs to include a detailed analysis of the computational overhead introduced by the C2C approach. This analysis should quantify the additional FLOPs and memory access patterns associated with the cache fusion and gating mechanisms. This should include a comparison of the computational cost of C2C with that of traditional text-based communication methods, not just in terms of latency but also in terms of energy consumption. The analysis should also consider the impact of different hardware platforms, such as GPUs with varying memory bandwidth and cache sizes. This would provide a more comprehensive understanding of the practical implications of using C2C in different environments. Second, the paper should conduct experiments with different cache sizes and analyze the trade-offs between performance and memory usage. This analysis should also consider the impact of cache eviction strategies on the overall performance of the system. For example, the paper could investigate the use of LRU or LFU policies for cache eviction and analyze their effectiveness in maintaining the quality of the KV cache. The authors should also discuss the potential for adaptive cache sizing, where the cache size is dynamically adjusted based on the task and the available resources. Third, the paper should explore the robustness of the proposed approach to different types of errors and inconsistencies in the KV caches. This could involve investigating the use of conflict resolution mechanisms and analyzing their impact on the overall performance of the system. The authors should also consider the impact of different types of errors, such as missing or corrupted cache entries, on the overall performance of the system. Fourth, the paper should provide a more detailed analysis of the error propagation in the proposed approach. This analysis should include a discussion of how the system handles situations where the Sharer's KV cache contains errors or inconsistencies. The authors should also consider the implications of using C2C in scenarios where the LLMs are operating in noisy or unreliable environments. Fifth, the paper should provide more specific details regarding the implementation of the C2C paradigm. This should include a detailed description of the layers and tokens used for KV cache fusion, as well as the criteria for selecting these layers and tokens. The authors should also provide a more in-depth analysis of the token-level fusion process. Sixth, the paper should provide more specific details regarding the training process. This should include a comprehensive description of the training process, including all relevant hyperparameters, such as the learning rate, batch size, and the number of training epochs. The authors should also specify the optimization algorithm used and the convergence criteria. Furthermore, the authors should provide an analysis of the sensitivity of the results to different hyperparameter settings. Seventh, the paper should provide a more thorough discussion of the evaluation metrics used in the paper. They should clearly define how each metric is calculated and what it measures. It is also important to discuss the limitations of the chosen metrics and how they might affect the interpretation of the results. For instance, are the metrics sensitive to the length of the generated text? How do they compare to other commonly used metrics in the field? The authors should also discuss the potential biases of the evaluation metrics and how they might influence the conclusions drawn from the experiments. Finally, the paper should discuss the potential impact of the proposed approach on the privacy of the models. The authors should discuss the potential privacy risks associated with the use of the KV cache and how to mitigate these risks. For example, the paper could explore techniques to anonymize or obfuscate the KV cache to protect sensitive information. The authors should also analyze the potential for error detection and correction techniques to improve the reliability of the KV cache communication. By addressing these weaknesses, the paper can be significantly strengthened and its practical implications can be better understood.


## Questions:

Based on my analysis, I have several questions that I believe are critical for further understanding the C2C approach. First, how does the proposed approach handle situations where the KV caches from different LLMs contain errors or inconsistencies? Specifically, what mechanisms are in place to mitigate the impact of these errors on the overall performance of the system? Second, what are the potential limitations of the proposed approach, such as the impact of cache size on performance? How does the system determine the optimal cache size for different tasks and models? Are there any adaptive cache sizing strategies that could be used to optimize performance for different scenarios? Third, how does the C2C approach impact the privacy of the models? What are the potential privacy risks associated with the use of the KV cache, and how can these risks be mitigated? Fourth, how does the proposed approach handle situations where the Sharer's KV cache contains errors or corrupted entries? What mechanisms are in place to ensure the integrity of the KV cache and prevent the propagation of errors through the system? Fifth, what is the computational overhead of the C2C approach, and how does it compare to traditional text-based communication methods? What are the FLOPs required for the KV cache fusion and gating operations, and how do these operations scale with the size of the KV cache and the number of LLMs in the multi-LLM system? Sixth, how does the proposed approach perform when the KV caches from different models have different sizes or structures? What are the potential challenges of aligning and fusing KV caches from different models, and how can these challenges be addressed? Seventh, what are the specific layers and tokens used for KV cache fusion, and how are these layers and tokens selected? What is the impact of different layer and token selection strategies on the performance of the C2C approach? Finally, what are the potential limitations of the proposed approach, such as the impact of different types of errors, such as missing or corrupted cache entries, on the overall performance of the system? How can these limitations be addressed to ensure the robustness of the C2C approach in real-world scenarios?


## Rating:

7.0


## Confidence:

3.25


## Decision:

Accept
}