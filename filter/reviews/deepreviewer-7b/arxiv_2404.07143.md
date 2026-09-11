I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper proposes a new attention mechanism that uses a fixed-size memory to store and retrieve information from previous segments. The proposed method is called Infini-attention, which is a recurrent attention mechanism that computes both local and global context states and combines them for its output. The authors show that their approach outperforms baseline models on long-context language modeling and summarization tasks.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The proposed method is simple and easy to implement, yet effective in handling long contexts.
- The paper is well-written and easy to follow.
- The experiments are comprehensive and show the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational cost of the proposed method, especially in comparison to the baseline models. It would be helpful to see a breakdown of the time and memory requirements for both training and inference.
- The paper does not provide a detailed analysis of the impact of different hyperparameters on the performance of the proposed method. For example, how does the size of the memory affect the performance? How does the choice of the gating function affect the results?
- The paper does not provide a detailed analysis of the limitations of the proposed method. For example, what are the scenarios where the proposed method is likely to fail? How does the proposed method compare to other memory-augmented neural networks in terms of robustness to noise and adversarial attacks?

### Suggestions

The paper would benefit from a more thorough analysis of the computational overhead introduced by the proposed Infini-attention mechanism. While the authors mention the use of a fixed-size memory, they should provide a detailed breakdown of the time complexity for both the forward and backward passes, especially in comparison to standard attention mechanisms. This analysis should consider the impact of sequence length and memory size on both training and inference time. For instance, providing a table showing the time taken for a specific sequence length and memory size for both training and inference would be beneficial. Furthermore, it would be useful to see a comparison of the memory footprint of the proposed method with baseline models, including the memory required for storing activations and gradients during training and inference. This would help to understand the practical implications of using the proposed method in resource-constrained environments.

To better understand the behavior of the proposed method, the authors should conduct a more extensive ablation study on the hyperparameters. Specifically, the impact of memory size on performance should be investigated more thoroughly. It would be helpful to see a plot showing how the performance changes as the memory size increases, and to identify the point at which the performance saturates. Additionally, the choice of the gating function should be analyzed more rigorously. The authors should compare different gating functions, such as sigmoid, tanh, and linear, and provide a detailed explanation of why the chosen gating function is optimal. It would also be beneficial to explore the impact of other hyperparameters, such as the learning rate and the number of attention heads, on the performance of the proposed method. This would provide a more comprehensive understanding of the method's sensitivity to different hyperparameter settings.

Finally, the paper should include a more detailed discussion of the limitations of the proposed method. The authors should identify specific scenarios where the method is likely to fail, such as when dealing with extremely long sequences or when the memory is corrupted. It would be useful to compare the proposed method to other memory-augmented neural networks in terms of robustness to noise and adversarial attacks. For example, the authors could evaluate the performance of the proposed method when the memory is partially corrupted or when adversarial examples are introduced. This would provide a more complete picture of the method's strengths and weaknesses and help to identify areas for future research.

### Questions

- How does the proposed method scale to even longer sequences, such as those with millions of tokens?
- How does the proposed method handle the case where the memory is corrupted or incomplete?
- How does the proposed method compare to other memory-augmented neural networks in terms of robustness to noise and adversarial attacks?

### Rating

5

### Confidence

4

**********

## Reviewer 2

### Summary

This paper proposes a new attention mechanism, Infini-attention, which can be used to scale up the context length of LLMs. The proposed Infini-attention incorporates a compressive memory into the vanilla attention mechanism. The compressive memory stores the key-value pairs from the previous segments and can be retrieved during the computation of the current segment. The proposed method is evaluated on long-context language modeling and book summarization tasks, and the results show that the proposed method outperforms the baseline models.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The proposed method is simple and easy to understand.
2. The proposed method is evaluated on two tasks, long-context language modeling and book summarization, and the results show that the proposed method outperforms the baseline models.
3. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is not evaluated on more tasks, such as retrieval-augmented generation (RAG) tasks. It is not clear whether the proposed method is effective for RAG tasks.
2. The proposed method is not compared with other methods that can scale up the context length of LLMs, such as RMT and AutoCompressors. It is not clear whether the proposed method is better than these methods.

### Suggestions

The paper introduces an interesting approach to scaling context length in LLMs using a compressive memory mechanism within the attention layer. However, the evaluation is limited in scope, primarily focusing on long-context language modeling and summarization. To strengthen the paper, it is crucial to evaluate the proposed method on retrieval-augmented generation (RAG) tasks. RAG tasks involve retrieving relevant information from an external knowledge base, which requires a flexible and long-context model to effectively access and integrate information. The current evaluation does not demonstrate the method's ability to handle the retrieval and generation process, which is a key application for long-context models. Therefore, the authors should consider evaluating their method on standard RAG benchmarks, such as those using knowledge bases or documents, to demonstrate its practical utility.

Furthermore, the paper lacks a comprehensive comparison with existing methods for scaling context length, particularly RMT and AutoCompressors. While the paper mentions these methods, it does not provide a detailed analysis of their strengths and weaknesses compared to the proposed approach. A thorough comparison should include not only performance metrics but also computational costs, memory requirements, and the ease of implementation. For example, it would be beneficial to analyze the trade-offs between the proposed method and RMT in terms of accuracy, inference speed, and memory footprint. Similarly, a comparison with AutoCompressors should explore the differences in their architectural designs and their impact on the model's ability to handle long contexts. This would provide a more complete understanding of the proposed method's advantages and limitations.

Finally, the paper should provide more details on the implementation of the compressive memory mechanism. Specifically, it would be helpful to understand how the key-value pairs are stored and retrieved during the computation of the current segment. The paper mentions that the compressive memory stores key-value pairs from previous segments, but it does not provide details on the specific data structures used for storage and retrieval. It would also be beneficial to discuss the potential impact of different memory management strategies on the model's performance. For example, how does the choice of memory size affect the trade-off between accuracy and computational cost? Addressing these implementation details would make the paper more reproducible and provide a deeper understanding of the proposed method.

### Questions

1. How does the proposed method perform on retrieval-augmented generation (RAG) tasks?
2. How does the proposed method compare with other methods that can scale up the context length of LLMs, such as RMT and AutoCompressors?

### Rating

5

### Confidence

3

**********

## Reviewer 3

### Summary

This paper introduces Infini-attention, a new attention mechanism designed to scale Transformer-based Large Language Models (LLMs) to infinitely long contexts with bounded memory and computation. The proposed approach integrates a compressive memory module into the vanilla attention mechanism, allowing the model to store and retrieve information from previous segments efficiently. The Infini-attention mechanism combines local and global context states and updates the memory recurrently, enabling the model to process extremely long sequences without significant memory overhead. The authors demonstrate the effectiveness of their approach on long-context language modeling benchmarks, 1M passkey context block retrieval tasks, and 500K length book summarization tasks, showing improvements in perplexity and summarization performance compared to baseline models.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper introduces a novel Infini-attention mechanism that effectively scales Transformer-based LLMs to infinitely long contexts with bounded memory and computation, addressing a significant challenge in the field.
- The proposed approach is supported by theoretical analysis and experimental results, demonstrating its effectiveness in handling long sequences.
- The paper is well-organized and clearly written, making it easy to follow the technical details and contributions.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational cost of the proposed method, especially in comparison to the baseline models. It would be helpful to see a breakdown of the time and memory requirements for both training and inference.
- The paper does not provide a detailed analysis of the impact of different hyperparameters on the performance of the proposed method. For example, how does the size of the memory affect the performance? How does the choice of the gating function affect the results?
- The paper does not provide a detailed analysis of the limitations of the proposed method. For example, what are the scenarios where the proposed method is likely to fail? How does the proposed method compare to other memory-augmented neural networks in terms of robustness to noise and adversarial attacks?

### Suggestions

The paper would benefit from a more thorough analysis of the computational overhead introduced by the Infini-attention mechanism. While the authors claim bounded memory and computation, a detailed breakdown of the time and memory requirements for both training and inference is necessary. This should include a comparison with baseline models, such as standard Transformer models, to quantify the actual overhead. For example, providing a table showing the training time per epoch and inference time per token for different sequence lengths and memory sizes would be very helpful. Furthermore, a more detailed analysis of the memory footprint, including the memory used by the model parameters, the attention cache, and the compressive memory, is needed. This analysis should also consider the impact of different hardware configurations on the computational cost.

In addition to the computational cost, a more detailed analysis of the impact of hyperparameters is crucial. The paper should explore the sensitivity of the model's performance to different memory sizes, gating function parameters, and other relevant hyperparameters. For instance, how does the performance change when the memory size is significantly reduced or increased? What is the optimal range for the gating function parameters? The authors should also investigate the impact of different compressive memory update mechanisms on the model's performance. This analysis should include ablation studies to isolate the impact of each hyperparameter. Furthermore, the paper should provide a discussion on the trade-offs between performance and computational cost when selecting these hyperparameters.

Finally, the paper should include a more detailed discussion of the limitations of the proposed method. The authors should identify specific scenarios where the method is likely to fail, such as when dealing with extremely long sequences or when the compressive memory is corrupted. A comparison with other memory-augmented neural networks in terms of robustness to noise and adversarial attacks is also needed. For example, how does the proposed method perform when the compressive memory is partially corrupted or when the input sequence contains adversarial examples? The authors should also discuss the potential limitations of the proposed method in terms of scalability and generalization to different types of tasks.

### Questions

- How does the proposed method perform on retrieval-augmented generation (RAG) tasks?
- How does the proposed method compare with other methods that can scale up the context length of LLMs, such as RMT and AutoCompressors?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

This paper introduces a new attention mechanism called Infini-attention, designed to scale Transformer-based LLMs to infinitely long contexts with bounded memory and computation. The Infini-attention incorporates a compressive memory module that stores and retrieves information from previous segments, allowing the model to process extremely long sequences without significant memory overhead. The approach combines local and global context states and updates the memory recurrently, enabling the model to handle long sequences efficiently. Experiments on long-context language modeling benchmarks, 1M passkey context block retrieval tasks, and 500K length book summarization tasks demonstrate that Infini-attention outperforms baseline models while maintaining 114x less memory parameters than the Memorizing Transformer model with a vector retrieval-based KV memory with length of 65K at its 9th layer.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The proposed Infini-attention mechanism is novel and addresses the challenge of scaling Transformer-based LLMs to infinitely long contexts with bounded memory and computation. The integration of a compressive memory module that stores and retrieves information from previous segments is a significant contribution to the field.
2. The paper is well-written and easy to follow. The authors provide a clear explanation of the proposed method, including the mathematical formulations and implementation details. The use of figures and tables helps to illustrate the key concepts and results.
3. The experiments are comprehensive and demonstrate the effectiveness of the proposed method. The results show that Infini-attention outperforms baseline models on long-context language modeling benchmarks, 1M passkey context block retrieval tasks, and 500K length book summarization tasks. The paper also provides a detailed analysis of the results, including the impact of different hyperparameters and the comparison with other memory-augmented neural networks.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of the proposed method, especially in comparison to the baseline models. It would be helpful to see a breakdown of the time and memory requirements for both training and inference. Specifically, the paper lacks a discussion on the impact of sequence length on the computational cost, which is a critical factor for long-context models. The analysis should include not only the overall training and inference times but also the memory footprint during these processes, including the memory used by the model parameters, the attention cache, and the compressive memory.
2. The paper does not provide a detailed analysis of the impact of different hyperparameters on the performance of the proposed method. For example, how does the size of the memory affect the performance? How does the choice of the gating function affect the results? The paper should include a sensitivity analysis of these hyperparameters, showing how the performance varies with different values. This analysis should also discuss the trade-offs between performance and computational cost when selecting these hyperparameters. For instance, a larger memory might lead to better performance but also higher computational cost.
3. The paper does not provide a detailed analysis of the limitations of the proposed method. For example, what are the scenarios where the proposed method is likely to fail? How does the proposed method compare to other memory-augmented neural networks in terms of robustness to noise and adversarial attacks? The paper should discuss the potential failure modes of the proposed method, such as when the compressive memory is corrupted or when the input sequence contains adversarial examples. It should also compare the robustness of the proposed method with other memory-augmented neural networks.

### Suggestions

The paper would benefit from a more thorough analysis of the computational cost associated with the proposed Infini-attention mechanism. Specifically, the authors should provide a detailed breakdown of the time and memory requirements for both training and inference, including a comparison with baseline models. This analysis should not only focus on the overall time and memory consumption but also on how these costs scale with increasing sequence lengths. For instance, the authors could present a graph showing the training time per epoch and inference time per token as a function of sequence length, both for Infini-attention and for baseline models like Transformer-XL and Memorizing Transformers. Furthermore, the memory usage should be analyzed in terms of model parameters, attention cache, and compressive memory, to provide a comprehensive understanding of the memory footprint. This would allow readers to better assess the practical applicability of the proposed method in resource-constrained environments.

In addition to the computational cost, the paper should include a more detailed sensitivity analysis of the hyperparameters. The authors should investigate how the size of the compressive memory affects the performance of the model, including both accuracy and computational cost. For example, the authors could present a graph showing the performance (e.g., perplexity or accuracy) as a function of memory size, and also show the corresponding training and inference times. This analysis should also explore the impact of different gating functions on the results, providing a clear understanding of the trade-offs between performance and computational cost. The authors should also discuss the optimal range for these hyperparameters and provide guidelines for selecting appropriate values for different tasks and resource constraints. This would make the proposed method more practical and easier to adopt.

Finally, the paper should include a more detailed discussion of the limitations of the proposed method. The authors should identify specific scenarios where the method is likely to fail, such as when the compressive memory is corrupted or when the input sequence contains adversarial examples. The paper should also compare the robustness of the proposed method with other memory-augmented neural networks, discussing the potential vulnerabilities of the proposed method and how they can be mitigated. For example, the authors could evaluate the performance of the proposed method on datasets with noisy or adversarial inputs and compare it with the performance of other memory-augmented models. This would provide a more comprehensive understanding of the strengths and weaknesses of the proposed method and help readers to better assess its applicability in different scenarios.

### Questions

1. How does the proposed method perform on retrieval-augmented generation (RAG) tasks?
2. How does the proposed method compare with other methods that can scale up the context length of LLMs, such as RMT and AutoCompressors?

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
1. Read each reviewer's weakness.
2. Find the corresponding section in the paper.
3. Look for evidence (quotes, numbers, missing information) to support the weakness.
4. If the weakness is about missing information, check if the information is indeed absent.
5. If there are conflicting opinions, note them.
6. Summarize the evidence and conclude if the weakness is valid, partially valid, or invalid.
**Review 1 Weaknesses:**

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost of the proposed method, especially in comparison to the baseline models. It would be helpful to see a breakdown of the time and memory requirements for both training and inference."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions "bounded memory and computation" in the abstract and introduction.
   - The method section describes the Infini-attention mechanism but lacks specific computational complexity analysis.
b) Experiment-related Evidence:
   - The "Implementation details" section mentions "segment chunking" and "gradient checkpoint" to save memory, but doesn't provide a detailed breakdown of time and memory requirements.
   - The "Results" section presents perplexity and accuracy scores but lacks information on training and inference times or memory usage.

3. Literature Gap Analysis:
   - The paper compares against baselines like Transformer-XL and Memorizing Transformers in terms of perplexity and accuracy but doesn't cite works that specifically analyze the computational cost of attention mechanisms or memory-augmented models.

4. Validation Analysis:
   - The paper claims bounded memory and computation but doesn't provide quantitative evidence to support this claim. The experimental section focuses on accuracy and perplexity without reporting computational costs. The mention of "gradient checkpoint" hints at memory optimization but doesn't quantify its impact.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of quantitative analysis of training/inference time and memory usage in the experimental section, despite claims of bounded resources.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the impact of different hyperparameters on the performance of the proposed method. For example, how does the size of the memory affect the performance? How does the choice of the gating function affect the results?"

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions the "Infini-attention" mechanism and the "Linear+Delta" gating function in the "Method" section.
   - The "Implementation details" section mentions the segment length (N=2048) and input sequence length (32K for training, 1M for evaluation), but doesn't discuss how these were chosen or their impact.
b) Experiment-related Evidence:
   - The "Long-Context Language Modeling" experiment uses a segment length of 2048 and mentions "input sequence length of 32K for training" and "1M for evaluation," but doesn't show how varying these parameters affects performance.
   - The paper doesn't include ablation studies on the memory size or the gating function.

3. Literature Gap Analysis:
   - While the paper cites works on compressive memory, it doesn't cite works that specifically analyze the impact of hyperparameters in such mechanisms.

4. Validation Analysis:
   - The paper describes the method and shows results, but it lacks a systematic analysis of how different hyperparameters, such as memory size or the choice of gating function, influence the performance. The experimental section doesn't include ablation studies to address this.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of ablation studies on key hyperparameters like memory size and gating function, and lack of discussion on how these parameters were chosen.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the limitations of the proposed method. For example, what are the scenarios where the proposed method is likely to fail? How does the proposed method compare to other memory-augmented neural networks in terms of robustness to noise and adversarial attacks?"

2. Evidence Collection:
a) Method-related Evidence:
   - The paper focuses on the advantages of the proposed method.
b) Experiment-related Evidence:
   - The experiments are conducted on standard benchmarks and don't include tests for robustness to noise or adversarial attacks.

3. Literature Gap Analysis:
   - The paper compares against some memory-augmented models but doesn't delve into a comparative analysis of their robustness properties.

4. Validation Analysis:
   - The paper primarily focuses on demonstrating the effectiveness of the method on standard tasks. It lacks a discussion of potential failure scenarios or a comparative analysis of robustness against other memory-augmented models.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of discussion on failure scenarios and robustness analysis compared to other memory-augmented models.

**Review 2 Weaknesses:**

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost of the proposed method, especially in comparison to the baseline models. It would be helpful to see a breakdown of the time and memory requirements for both training and inference."

2. Evidence Collection:
   - This is the same weakness as Reviewer 1, Weakness 1. Please see the evidence collected for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1, Weakness 1.

4. Validation Analysis:
   - Same as Reviewer 1, Weakness 1.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1, Weakness 1.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the impact of different hyperparameters on the performance of the proposed method. For example, how does the size of the memory affect the performance? How does the choice of the gating function affect the results?"

2. Evidence Collection:
   - This is the same weakness as Reviewer 1, Weakness 2. Please see the evidence collected for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1, Weakness 2.

4. Validation Analysis:
   - Same as Reviewer 1, Weakness 2.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1, Weakness 2.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the limitations of the proposed method. For example, what are the scenarios where the proposed method is likely to fail? How does the proposed method compare to other memory-augmented neural networks in terms of robustness to noise and adversarial attacks?"

2. Evidence Collection:
   - This is the same weakness as Reviewer 1, Weakness 3. Please see the evidence collected for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1, Weakness 3.

4. Validation Analysis:
   - Same as Reviewer 1, Weakness 3.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1, Weakness 3.

**Review 3 Weaknesses:**

1. Weakness Statement:
"The paper does not evaluate on more tasks, such as retrieval-augmented generation (RAG) tasks. It is not clear whether the proposed method is effective for RAG tasks."

2. Evidence Collection:
a) Experiment-related Evidence:
   - The "Experiments" section details evaluations on "Long-Context Language Modeling," "1M Passkey Retrieval," and "500K Length Book Summarization."
   - RAG tasks are not included in the evaluation.

3. Literature Gap Analysis:
   - RAG is a common application for models with long context understanding, and the paper doesn't justify its exclusion.

4. Validation Analysis:
   - The paper's evaluation is limited to language modeling and summarization. It doesn't demonstrate the method's effectiveness in a RAG setting, where the ability to access and utilize information from external sources is crucial.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of RAG tasks in the experimental evaluation.

1. Weakness Statement:
"The proposed method is not compared with other methods that can scale up the context length of LLMs, such as RMT and AutoCompressors. It is not clear whether the proposed method is better than these methods."

2. Evidence Collection:
a) Experiment-related Evidence:
   - The "Long-Context Language Modeling" experiment compares against "Transformer-XL" and "Memorizing Transformer."
   - RMT and AutoCompressors are not included as baselines.

3. Literature Gap Analysis:
   - RMT and AutoCompressors are relevant methods for long-context modeling, and their absence weakens the comparative analysis.

4. Validation Analysis:
   - While the paper compares against Transformer-XL and Memorizing Transformers, it doesn't include comparisons with other established methods like RMT and AutoCompressors, making it difficult to assess the relative performance of Infini-attention.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of comparison with RMT and AutoCompressors in the experimental section.

**Review 4 Weaknesses:**

1. Weakness Statement:
"The proposed method is not evaluated on more tasks, such as retrieval-augmented generation (RAG) tasks. It is not clear whether the proposed method is effective for RAG tasks."

2. Evidence Collection:
   - This is the same weakness as Reviewer 3, Weakness 1. Please see the evidence collected for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 3, Weakness 1.

4. Validation Analysis:
   - Same as Reviewer 3, Weakness 1.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 3, Weakness 1.

1. Weakness Statement:
"The proposed method is not compared with other methods that can scale up the context length of LLMs, such as RMT and AutoCompressors. It is not clear whether the proposed method is better than these methods."

2. Evidence Collection:
   - This is the same weakness as Reviewer 3, Weakness 2. Please see the evidence collected for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 3, Weakness 2.

4. Validation Analysis:
   - Same as Reviewer 3, Weakness 2.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 3, Weakness 2.

**Synthesis and Reflection:**

The reviewers have raised several consistent concerns regarding the paper. The most prominent weakness is the lack of a detailed analysis of the computational cost of the proposed method compared to baselines. Reviewers 1 and 2 both pointed this out, and the evidence from the paper confirms this omission. The paper claims bounded resources but doesn't provide quantitative evidence.

Another recurring weakness is the limited scope of the experimental evaluation. Reviewers 3 and 4 both noted the absence of RAG tasks, which are a natural application for long-context models. Reviewer 3 also pointed out the lack of comparison with RMT and AutoCompressors, which are relevant baselines for long-context modeling.

Reviewer 1 and 2 also highlighted the lack of a detailed analysis of hyperparameter sensitivity, specifically the impact of memory size and gating function. The paper describes the method and shows results but doesn't include ablation studies to explore these aspects.

Finally, Reviewer 1 and 2 both noted the absence of a discussion on the limitations of the proposed method, such as scenarios where it might fail or its robustness to noise and adversarial attacks. The paper focuses on the positive aspects of the method.

There are no significant contradictions between the reviewers' opinions. They largely converge on the need for more detailed computational analysis, a broader experimental evaluation including RAG tasks and relevant baselines, and a more thorough analysis of hyperparameter sensitivity and limitations.

**Final Conclusion:**

All the identified weaknesses are valid and supported by the evidence within the paper. The reviewers have highlighted key areas where the paper could be strengthened through more detailed analysis and a more comprehensive experimental evaluation.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces Infini-attention, a novel attention mechanism designed to address the challenges of processing extremely long sequences in Transformer-based Large Language Models (LLMs) while maintaining computational efficiency. The core idea revolves around integrating a compressive memory module into the standard attention mechanism. This allows the model to store and retrieve information from previous segments, effectively extending the context window without a proportional increase in computational cost. The proposed method combines local and global context states, updating the memory recurrently, enabling the model to process long sequences in a streaming fashion. The authors evaluate their approach on three tasks: long-context language modeling, a passkey retrieval task designed to assess the model's ability to recall information from distant parts of the input sequence, and book summarization. The empirical results demonstrate that Infini-attention outperforms baseline models, such as Transformer-XL and Memorizing Transformers, on these tasks, while using fewer parameters. Specifically, the paper claims that Infini-attention achieves comparable performance to these baselines while using significantly less memory, highlighting its potential for scaling LLMs to longer contexts. The authors emphasize the bounded memory and computation nature of their approach, suggesting it is suitable for handling infinitely long contexts. The method's novelty lies in its integration of a compressive memory module with the standard attention mechanism, allowing for efficient processing of long sequences. The experimental results, while promising, are primarily focused on demonstrating the method's effectiveness on tasks designed to test long-context capabilities. However, the paper lacks a thorough analysis of the computational overhead, the impact of hyperparameters, and the limitations of the proposed method. The paper's overall significance lies in its attempt to tackle the long-standing challenge of scaling LLMs to longer contexts, which is crucial for many real-world applications. However, the lack of a detailed analysis and comparison with other methods limits the conclusions that can be drawn about the method's true potential and advantages.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

2.5


## Strengths:

The primary strength of this paper lies in its introduction of the Infini-attention mechanism, a conceptually simple yet potentially powerful approach to handling long sequences in LLMs. The integration of a compressive memory module into the standard attention mechanism is a novel contribution that addresses the computational challenges associated with processing long contexts. The method's ability to store and retrieve information from previous segments without a proportional increase in computational cost is a significant advantage. The paper is well-written and easy to follow, making the proposed method accessible to a broad audience. The authors provide a clear explanation of the Infini-attention mechanism, including the mathematical formulations and implementation details. The use of figures and tables helps to illustrate the key concepts and results. The experimental results, while not exhaustive, demonstrate the effectiveness of the proposed method on the chosen tasks. The paper shows that Infini-attention outperforms baseline models, such as Transformer-XL and Memorizing Transformers, on long-context language modeling, passkey retrieval, and book summarization tasks. The authors also highlight the reduced memory footprint of their approach compared to Memorizing Transformers, which is a crucial aspect for scaling LLMs to longer contexts. The paper's focus on bounded memory and computation is a significant contribution, as it addresses a key limitation of traditional Transformer models. The authors' claim that their method can handle infinitely long contexts is a bold one, and the experimental results provide some support for this claim. The simplicity of the proposed method is another strength, as it makes it easier to implement and integrate into existing LLM architectures. The paper's overall contribution is significant, as it presents a novel approach to a critical problem in the field of LLMs. The method's potential to enable the use of LLMs in applications that require processing long sequences is a valuable contribution to the field.


## Weaknesses:

Despite the promising aspects of the Infini-attention mechanism, several weaknesses significantly limit the paper's conclusions. First, and most critically, the paper lacks a detailed analysis of the computational cost associated with the proposed method. While the authors claim that Infini-attention has bounded memory and computation, there is no quantitative evidence to support this claim. The paper does not provide a breakdown of the time and memory requirements for both training and inference, nor does it compare these costs with baseline models. This omission is a major limitation, as it makes it difficult to assess the practical applicability of the method. For example, the paper mentions the use of gradient checkpointing to save memory, but it does not quantify the impact of this technique on memory usage or training time. This lack of analysis makes it impossible to determine whether the method is truly computationally efficient, or if the performance gains come at the expense of increased computational cost. The absence of a detailed computational analysis is a significant oversight, as it prevents a thorough evaluation of the method's practical value. My confidence in this weakness is high, as the paper explicitly claims bounded resources but provides no supporting evidence. Second, the paper does not include a detailed analysis of the impact of different hyperparameters on the performance of the proposed method. The paper introduces the Infini-attention mechanism and the Linear+Delta gating function, but it does not explore the sensitivity of the method to different hyperparameter settings. For example, the paper does not investigate how the size of the compressive memory affects the performance, or how the choice of the gating function impacts the results. The paper also lacks ablation studies on key hyperparameters, such as the memory size and the gating function parameters. This lack of analysis makes it difficult to understand the behavior of the method and to identify the optimal hyperparameter settings. The absence of a hyperparameter sensitivity analysis is a significant limitation, as it prevents a thorough understanding of the method's behavior and its robustness to different settings. My confidence in this weakness is high, as the paper does not include any ablation studies or sensitivity analyses. Third, the paper does not provide a detailed analysis of the limitations of the proposed method. The authors do not identify specific scenarios where the method is likely to fail, nor do they compare its robustness to noise and adversarial attacks with other memory-augmented neural networks. The paper focuses primarily on demonstrating the method's effectiveness on the chosen tasks, but it does not address its potential weaknesses. This lack of analysis makes it difficult to assess the method's practical applicability and its limitations. The absence of a discussion of limitations is a significant oversight, as it prevents a thorough evaluation of the method's strengths and weaknesses. My confidence in this weakness is high, as the paper does not include any discussion of limitations. Fourth, the paper's experimental evaluation is limited in scope. The paper does not include evaluations on retrieval-augmented generation (RAG) tasks, which are a natural application for models with long context understanding. The paper's evaluation is limited to language modeling and summarization tasks, but it does not demonstrate the method's effectiveness in a RAG setting, where the ability to access and utilize information from external sources is crucial. This lack of evaluation on RAG tasks is a significant limitation, as it prevents a thorough assessment of the method's practical applicability. My confidence in this weakness is high, as the paper does not include any RAG tasks in its evaluation. Finally, the paper does not compare the proposed method with other methods that can scale up the context length of LLMs, such as RMT and AutoCompressors. While the paper compares against Transformer-XL and Memorizing Transformers, it does not include comparisons with other established methods for long-context modeling. This lack of comparison makes it difficult to assess the relative performance of Infini-attention and its advantages over other methods. The absence of comparisons with RMT and AutoCompressors is a significant limitation, as it prevents a thorough evaluation of the method's performance. My confidence in this weakness is high, as the paper does not include any comparisons with these methods.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the paper must include a detailed analysis of the computational cost of the proposed method. This analysis should include a breakdown of the time and memory requirements for both training and inference, and it should compare these costs with baseline models. The analysis should consider the impact of sequence length on computational cost, and it should provide a clear understanding of the practical implications of using the proposed method. For example, the paper should provide a table showing the training time per epoch and inference time per token for different sequence lengths and memory sizes. This analysis should also include a comparison of the memory footprint of the proposed method with baseline models, including the memory used by the model parameters, the attention cache, and the compressive memory. This would allow readers to better assess the practical applicability of the proposed method. Second, the paper should include a more detailed analysis of the impact of hyperparameters on the performance of the proposed method. This analysis should include ablation studies on key hyperparameters, such as the size of the compressive memory, the gating function parameters, and other relevant hyperparameters. The paper should explore the sensitivity of the method to different hyperparameter settings and identify the optimal range for each hyperparameter. For example, the paper should investigate how the performance changes as the memory size is varied, and it should provide a clear explanation of why the chosen gating function is optimal. The analysis should also include a discussion of the trade-offs between performance and computational cost when selecting these hyperparameters. This would provide a more comprehensive understanding of the method's behavior and its robustness to different settings. Third, the paper should include a more detailed discussion of the limitations of the proposed method. The authors should identify specific scenarios where the method is likely to fail, such as when the compressive memory is corrupted or when the input sequence contains adversarial examples. The paper should also compare the robustness of the proposed method with other memory-augmented neural networks, discussing the potential vulnerabilities of the proposed method and how they can be mitigated. For example, the paper could evaluate the performance of the proposed method on datasets with noisy or adversarial inputs and compare it with the performance of other memory-augmented models. This would provide a more comprehensive understanding of the method's strengths and weaknesses and help readers to better assess its practical applicability. Fourth, the paper should include evaluations on retrieval-augmented generation (RAG) tasks. RAG is a natural application for long-context models, and it would be valuable to see how the proposed method performs in this setting. The paper should evaluate the method's ability to retrieve relevant information from an external knowledge base and integrate it into the generation process. This would provide a more comprehensive assessment of the method's practical applicability. Finally, the paper should include comparisons with other methods that can scale up the context length of LLMs, such as RMT and AutoCompressors. This would provide a more complete picture of the method's advantages and limitations compared to other memory-augmented neural networks. The paper should compare the performance of the proposed method with these baselines on the chosen tasks, and it should discuss the trade-offs between performance and computational cost. This would allow readers to better assess the relative performance of the proposed method and its advantages over other methods. By addressing these weaknesses, the paper would be significantly strengthened and would provide a more comprehensive and robust evaluation of the proposed method.


## Questions:

Several key questions remain unanswered by the paper, and addressing these would significantly enhance the understanding of the proposed method. First, how does the proposed method perform on retrieval-augmented generation (RAG) tasks? The paper does not include any evaluations on RAG tasks, and it would be valuable to see how the method performs in this setting. Specifically, how does the method handle the retrieval of relevant information from an external knowledge base and integrate it into the generation process? Second, how does the proposed method compare to other methods that can scale up the context length of LLMs, such as RMT and AutoCompressors? The paper does not include comparisons with these methods, and it would be valuable to see how the proposed method performs relative to these baselines on the chosen tasks. What are the trade-offs between performance and computational cost when choosing these methods? Third, what are the specific scenarios where the proposed method is likely to fail? The paper does not include a detailed discussion of the limitations of the method, and it would be valuable to understand the conditions under which the method is likely to fail. For example, how does the method perform when the compressive memory is corrupted or when the input sequence contains adversarial examples? Fourth, what is the impact of different hyperparameters on the performance of the proposed method? The paper does not include a detailed analysis of the sensitivity of the method to different hyperparameter settings, and it would be valuable to understand how the performance changes as the memory size is varied or the gating function parameters are changed. What is the optimal range for each hyperparameter, and what are the trade-offs between performance and computational cost when selecting these hyperparameters? Fifth, what is the computational cost of the proposed method compared to baseline models? The paper claims that the method has bounded memory and computation, but it does not provide quantitative evidence to support this claim. It would be valuable to see a detailed breakdown of the time and memory requirements for both training and inference, including a comparison with baseline models. What is the training time per epoch and inference time per token for different sequence lengths and memory sizes? What is the memory footprint of the proposed method, including the memory used by the model parameters, the attention cache, and the compressive memory? Addressing these questions would provide a more comprehensive understanding of the proposed method and its practical applicability.


## Rating:

6.0


## Confidence:

3.25


## Decision:

Reject
}