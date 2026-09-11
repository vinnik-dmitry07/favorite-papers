I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper proposes Unlimiformer, a retrieval-based approach to augment pretrained language models to accept inputs of arbitrary length. The approach is based on the idea of performing cross-attention in each layer of the decoder to the top-k keys that are most similar to the query. The keys and values are the hidden states of the encoder. The similarity is computed using the standard dot product between the query and key after encoding them into the same hidden space using a learned linear transformation. The authors show that Unlimiformer improves the performance of BART and PRIMERA on long document summarization and question answering tasks.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

- The paper is well written and easy to follow.
- The method is simple and effective.
- The method is evaluated on a variety of tasks.

### Weaknesses

#### Some Related Works

[1] Longformer: The Long-Document Transformer
[2] Retrieval-augmented language models are in-context learners
[3] Retrieval Head in Generative Language Models

#### comment

 - The method is not novel. The idea of using kNN to augment language models has been explored in prior work [1,2,3]. The main difference is that Unlimiformer performs the kNN in the embedding space instead of the input space, and does not require a separate datastore.
- The evaluation is not comprehensive. The paper only evaluates on summarization and QA tasks. It would be great to evaluate on a wider range of tasks, such as translation and code generation.
- The paper does not provide a comparison with other retrieval-based methods. It would be great to compare with other methods that use retrieval to augment language models.

### Suggestions

The paper's core idea of using k-Nearest Neighbors (kNN) in the embedding space for retrieval augmentation, while presented as novel, needs further justification given existing literature. The authors should more clearly articulate the specific differences in their approach compared to methods that perform kNN in the input space, and those that use external knowledge bases. For instance, while the paper mentions that their method does not require a separate datastore, it does not fully explore the implications of performing kNN in the embedding space. A more detailed analysis of the computational overhead and memory requirements of this approach compared to methods using external knowledge bases would be beneficial. Furthermore, the authors should provide a more thorough discussion of the limitations of their approach, such as the potential for bias in the encoder's embeddings and how this might affect the retrieval process. A more rigorous analysis of the sensitivity of the method to the choice of k and the embedding space is also needed.

To strengthen the evaluation, the authors should expand the range of tasks considered. While summarization and question answering are relevant, the paper would benefit from evaluations on tasks such as translation, code generation, and potentially tasks involving reasoning over structured data. For example, evaluating on a machine translation benchmark would assess the method's ability to handle different linguistic structures and semantic relationships. Similarly, evaluating on code generation tasks would test the method's ability to handle complex logical operations and code-specific knowledge. The authors should also consider using more diverse datasets, including those with varying document lengths and complexities, to better understand the method's robustness and generalizability. Furthermore, a more detailed analysis of the performance gains, including statistical significance tests, would be valuable.

Finally, the paper needs a more comprehensive comparison with existing retrieval-based methods. The authors should not only compare their method with other retrieval-augmented language models but also with methods that use different retrieval strategies, such as those based on sparse retrieval or dense retrieval. A detailed comparison should include an analysis of the trade-offs between performance, computational cost, and memory usage. For example, the authors could compare their method with sparse retrieval methods that use inverted indexes or dense retrieval methods that use vector databases. This would provide a more complete picture of the strengths and weaknesses of their approach and help to position it within the broader landscape of retrieval-augmented language models. The authors should also consider including ablation studies to analyze the impact of different components of their method, such as the choice of the encoder and the kNN algorithm.

### Questions

- How does Unlimiformer compare to other retrieval-based methods? What are the advantages and disadvantages of Unlimiformer compared to other methods?
- How does Unlimiformer perform on tasks other than summarization and QA? For example, translation or code generation?
- How does Unlimiformer compare to other methods that use retrieval to augment language models?

### Rating

5

### Confidence

4

**********

## Reviewer 2

### Summary

The paper proposes a retrieval-based method to handle long context inputs for language models. The method is based on Unlimiformer, which uses a kNN index over the encoder hidden states to retrieve relevant context for each decoder layer. The authors show that Unlimiformer can be applied to existing language models without further training, and can further improve the performance of models when combined with other training strategies.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and effective.
- The authors show that Unlimiformer can be applied to existing language models without further training, and can further improve the performance of models when combined with other training strategies.

### Weaknesses

#### Some Related Works


#### comment

 - The novelty of the proposed method is limited. The idea of using kNN index to retrieve relevant context for language models has been explored in prior work, such as SLED (Ivgi et al., 2022) and Memorizing Transformers (Wu et al., 2022). The main difference is that Unlimiformer performs the kNN in the embedding space instead of the input space, and does not require a separate datastore. However, the authors do not provide a detailed comparison with these prior works, and it is not clear how Unlimiformer differs from them in terms of implementation and performance.
- The evaluation is not comprehensive. The paper only evaluates on summarization and QA tasks. It would be great to evaluate on a wider range of tasks, such as translation and code generation. The lack of evaluation on diverse tasks makes it difficult to assess the general applicability of the proposed method.
- The paper does not provide a comparison with other retrieval-based methods. It would be great to compare with other methods that use retrieval to augment language models. The absence of such comparisons makes it hard to understand the relative advantages and disadvantages of Unlimiformer.
- The paper does not provide a detailed analysis of the computational cost of Unlimiformer. While the authors mention that the method is efficient, they do not provide a quantitative analysis of the time and memory requirements, especially when dealing with long inputs. This makes it difficult to assess the practical feasibility of the method.

### Suggestions

The paper should provide a more detailed comparison with existing retrieval-based methods for long-context language models. Specifically, the authors should compare Unlimiformer with methods that use sparse retrieval, such as those based on inverted indexes, and dense retrieval, such as those using vector databases. This comparison should include an analysis of the trade-offs between performance, computational cost, and memory usage. For example, the authors could compare the retrieval accuracy, latency, and memory footprint of Unlimiformer with these other methods. This would help to better understand the strengths and weaknesses of the proposed approach and its position within the broader landscape of retrieval-augmented language models. Furthermore, the authors should clarify the specific implementation details of Unlimiformer, such as the choice of the kNN algorithm, the indexing method, and the way the retrieved context is used in the decoder. This would make it easier for other researchers to reproduce the results and build upon this work.

To address the limited evaluation, the authors should expand the experimental evaluation to include a wider range of tasks. This should include tasks such as machine translation, code generation, and question answering over long documents. For each task, the authors should provide a detailed analysis of the performance of Unlimiformer, including the impact of different hyperparameters and training strategies. This would help to better understand the generalizability of the proposed method and its applicability to different domains. In addition, the authors should consider evaluating the method on datasets with varying input lengths to assess its scalability. This would provide insights into the performance of Unlimiformer when dealing with very long inputs, which is a key motivation for the proposed approach. The authors should also provide a more detailed analysis of the computational cost of Unlimiformer, including the time and memory requirements for both training and inference. This analysis should consider the impact of different parameters, such as the number of retrieved tokens and the size of the index. This would help to assess the practical feasibility of the method and its suitability for different applications.

Finally, the authors should provide a more thorough discussion of the limitations of Unlimiformer and potential directions for future research. This should include a discussion of the potential biases introduced by the kNN index and the limitations of the kNN algorithm in capturing long-range dependencies. The authors should also discuss the potential for further improvements, such as the use of more advanced indexing techniques or the incorporation of external knowledge sources. This would help to guide future research in this area and to identify the key challenges that need to be addressed. The authors should also consider the impact of the choice of the encoder on the performance of Unlimiformer. Since the method relies on the encoder hidden states, it is important to understand how the choice of the encoder affects the quality of the retrieved context. This should be investigated through ablation studies and experiments with different encoders.

### Questions

- How does Unlimiformer compare to other retrieval-based methods for long-context language models?
- How does Unlimiformer perform on tasks other than summarization and QA, such as translation and code generation?
- How does Unlimiformer compare to other methods that use retrieval to augment language models?
- What is the computational cost of Unlimiformer, in terms of time and memory requirements?
- What are the limitations of Unlimiformer, and what are the potential directions for future research?

### Rating

5

### Confidence

4

**********

## Reviewer 3

### Summary

This paper proposes Unlimiformer, a retrieval-based approach to augment pretrained language models to accept inputs of unbounded length at test time. Unlimiformer uses a single kNN index over the hidden states of all input tokens to retrieve the top-k keys, instead of attending to every key. The authors show that Unlimiformer improves pretrained models such as BART and PRIMERA on long document summarization and question-answering tasks, without additional training.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and effective.
- The authors conduct extensive experiments to demonstrate the effectiveness of Unlimiformer.

### Weaknesses

#### Some Related Works

[1] Retrieval-augmented language models are in-context learners.
[2] Retrieval-augmented language models are in-context learners.

#### comment

 - The novelty of the proposed method is limited. The idea of using kNN to augment language models has been explored in prior work [1,2]. The main difference is that Unlimiformer performs the kNN in the embedding space instead of the input space, and does not require a separate datastore. However, the authors do not provide a detailed comparison with these prior works, and it is not clear how Unlimiformer differs from them in terms of implementation and performance.
- The evaluation is not comprehensive. The paper only evaluates on summarization and QA tasks. It would be great to evaluate on a wider range of tasks, such as translation and code generation.
- The paper does not provide a comparison with other retrieval-based methods. It would be great to compare with other methods that use retrieval to augment language models.

### Suggestions

The paper would benefit from a more thorough comparison with existing retrieval-augmented language models. Specifically, the authors should provide a detailed analysis of the differences in implementation, such as the indexing method, the kNN algorithm used, and the way the retrieved context is integrated into the decoder. A quantitative comparison of performance, including metrics like ROUGE and BLEU for summarization tasks, and accuracy for QA tasks, would be valuable. Furthermore, the authors should investigate the computational cost of their approach compared to other retrieval methods, including the time required for indexing, retrieval, and decoding. This would help to understand the trade-offs between performance and efficiency.

To address the limited evaluation, the authors should expand their experiments to include a wider range of tasks. For example, they could evaluate their method on machine translation tasks using datasets like WMT, or on code generation tasks using datasets like HumanEval. These tasks would provide a more comprehensive assessment of the method's generalizability and robustness. In addition, the authors should consider evaluating their method on tasks that require different types of reasoning, such as logical inference or commonsense reasoning. This would help to understand the strengths and weaknesses of their approach in different scenarios. The authors should also provide a detailed analysis of the results, including error analysis and ablation studies, to understand the factors that contribute to the performance of their method.

Finally, the authors should provide a more detailed discussion of the limitations of their approach. For example, they should discuss the potential biases introduced by the kNN index and the limitations of the kNN algorithm in capturing long-range dependencies. They should also discuss the potential for overfitting to the training data and the generalizability of their method to unseen data. Furthermore, the authors should explore potential avenues for future research, such as incorporating external knowledge sources or using more advanced indexing techniques. This would help to position their work within the broader context of retrieval-augmented language models and to identify promising directions for future research.

### Questions

- How does Unlimiformer compare to other retrieval-based methods for long-context language models?
- How does Unlimiformer perform on tasks other than summarization and QA, such as translation and code generation?
- How does Unlimiformer compare to other methods that use retrieval to augment language models?

### Rating

5

### Confidence

4

**********

## Reviewer 4

### Summary

This paper proposes Unlimiformer, a retrieval-based approach to augment pretrained language models to accept inputs of unbounded length at test time. The approach is based on the idea of performing cross-attention in each layer of the decoder to the top-k keys that are most similar to the query. The keys and values are the hidden states of the encoder. The similarity is computed using the standard dot product between the query and key after encoding them into the same hidden space using a learned linear transformation. The method is evaluated on several long-document and book-summarization benchmarks having inputs of up to 500k tokens, and shows that it can improve existing models, even without further training.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well written and easy to follow.
2. The proposed method is simple and effective.
3. The method is evaluated on a variety of tasks.

### Weaknesses

#### Some Related Works

[1] Retrieval-Augmented Language Models are In-Context Learners
[2] Retrieval-augmented language models are in-context learners

#### comment

1. The novelty of the proposed method is limited. The idea of using kNN to augment language models has been explored in prior work [1,2]. The main difference is that Unlimiformer performs the kNN in the embedding space instead of the input space, and does not require a separate datastore. However, the authors do not provide a detailed comparison with these prior works, and it is not clear how Unlimiformer differs from them in terms of implementation and performance.
2. The evaluation is not comprehensive. The paper only evaluates on summarization and QA tasks. It would be great to evaluate on a wider range of tasks, such as translation and code generation.
3. The paper does not provide a comparison with other retrieval-based methods. It would be great to compare with other methods that use retrieval to augment language models.

### Suggestions

The paper would benefit from a more thorough comparison with existing retrieval-augmented language models. Specifically, the authors should provide a detailed analysis of the differences in implementation, such as the indexing method, the kNN algorithm used, and the way the retrieved context is integrated into the decoder. A quantitative comparison of performance, including metrics like ROUGE and BLEU for summarization tasks, and accuracy for QA tasks, would be valuable. Furthermore, the authors should investigate the computational cost of their approach compared to other retrieval methods, including the time required for indexing, retrieval, and decoding. This would help to understand the trade-offs between performance and efficiency. It is also important to clarify the specific advantages of performing kNN in the embedding space compared to the input space, and provide empirical evidence to support these claims.

To address the limited evaluation, the authors should expand their experiments to include a wider range of tasks. For example, they could evaluate their method on machine translation tasks using datasets like WMT, or on code generation tasks using datasets like HumanEval. These tasks would provide a more comprehensive assessment of the method's generalizability and robustness. In addition, the authors should consider evaluating their method on tasks that require different types of reasoning, such as logical inference or commonsense reasoning. This would help to understand the strengths and weaknesses of their approach in different scenarios. The authors should also provide a detailed analysis of the results, including error analysis and ablation studies, to understand the factors that contribute to the performance of their method. For example, it would be useful to see how the performance varies with the number of retrieved tokens, and how the choice of the kNN algorithm affects the results.

Finally, the paper should include a more detailed discussion of the limitations of the proposed approach. For example, the authors should discuss the potential biases introduced by the kNN index and the limitations of the kNN algorithm in capturing long-range dependencies. They should also discuss the potential for overfitting to the training data and the generalizability of their method to unseen data. Furthermore, the authors should explore potential avenues for future research, such as incorporating external knowledge sources or using more advanced indexing techniques. This would help to position their work within the broader context of retrieval-augmented language models and to identify promising directions for future research. It is also important to clarify the specific scenarios where the proposed method is most effective, and to identify the types of tasks where it is likely to perform well.

### Questions

1. How does Unlimiformer compare to other retrieval-based methods for long-context language models?
2. How does Unlimiformer perform on tasks other than summarization and QA, such as translation and code generation?
3. How does Unlimiformer compare to other methods that use retrieval to augment language models?

### Rating

5

### Confidence

4

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers for the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

**Plan:**
1. Go through each reviewer's comments one by one.
2. For each comment identified as a weakness, find supporting evidence from the paper.
3. Categorize the weakness (theoretical, methodological, experimental, practical).
4. Provide direct quotes and section references as evidence.
5. If a weakness is not supported by the paper, explain why.
6. Synthesize the findings and provide a conclusion on the validity of each weakness.
**Review 1**

1. Weakness Statement:
"The method is not novel. The idea of using kNN to augment language models has been explored in prior work [1,2,3]. The main difference is that Unlimiformer performs the kNN in the embedding space instead of the input space, and does not require a separate datastore. However, the authors do not provide a detailed comparison with these prior works, and it is not clear how Unlimiformer differs from them in terms of implementation and performance."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper states in the Introduction: "We introduce Unlimiformer, a retrieval-based approach to augment pretrained language models to accept inputs of unbounded length at test time. Given a long input sequence, Unlimiformer constructs a k k -nearest-neighbor ( k k NN) index over the hidden states of all input tokens. Then, every standard cross-attention head in every decoder layer queries the k k NN index, such that the k k NN distances are the attention dot-product scores, and attends only to the top- k k input tokens." (Section 1)
   - The paper also mentions: "In contrast, Memorizing Transformers ( Wu et al., 2022 ) add additional weights, and thus cannot easily leverage pretrained LMs, while Unlimiformer is fully non-parametric and can improve performance without fine-tuning; further, Wu et al. (2022) apply their memory layer to only a single decoder layer." (Section 1)
   - The paper further elaborates on the difference: "Instead, we present a different order of computing the well-known transformer attention formula, which allows us to store a single index across all attention heads and all decoder layers, without changing the mathematical definition of the transformer’s standard dot-product attention." (Section 1)
   - The paper also states: "So, not surprisingly, Wu et al. (2022) apply their memory layer to only a single decoder layer." (Section 1)
b) Experiment-related Evidence:
   - The paper includes a "Low-cost training methods: Applying Unlimiformer at validation or test-time only" section (Section 3.1) which describes a method to apply Unlimiformer without fine-tuning.
   - The paper includes a "Long-range training methods: Applying Unlimiformer directly" section (Section 3.2) which describes a method to apply Unlimiformer during training.
3. Literature Gap Analysis:
   - The paper cites Wu et al. (2022) (Memorizing Transformers) as related work.
   - The paper mentions SLED (Ivgi et al., 2022) in the Related Work section (Section 7) as a method that performs kNN in the embedding space.
4. Validation Analysis:
   - The reviewer is correct that the core idea of using kNN for retrieval augmentation exists in prior work, specifically mentioning SLED and Memorizing Transformers. The paper acknowledges Memorizing Transformers but argues for the novelty of performing kNN in the embedding space and not requiring a separate datastore. However, the paper does not provide a detailed comparison of the implementation differences and performance trade-offs with these prior works.
5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper acknowledges Memorizing Transformers but lacks a detailed comparison of implementation and performance differences. The paper does mention SLED but doesn't provide a thorough comparison.

1. Weakness Statement:
"The evaluation is not comprehensive. The paper only evaluates on summarization and QA tasks. It would be great to evaluate on a wider range of tasks, such as translation and code generation."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper evaluates on "Long Document Summarization" (Section 4.1) using GovReport, SummScreen, and BookSum datasets.
   - The paper evaluates on "Book Summarization" (Section 4.2) using the BookSum dataset.
   - The paper evaluates on "Question-Answering" (Section 4.3) using SCROLLS benchmark datasets.
3. Literature Gap Analysis:
   - There is no mention of evaluation on translation or code generation tasks.
4. Validation Analysis:
   - The reviewer is correct. The paper's evaluation is limited to summarization and question-answering tasks. It does not include evaluations on tasks like translation or code generation.
5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "Experiments" section (Section 4) only details evaluations on summarization and QA datasets.

1. Weakness Statement:
"The paper does not provide a comparison with other retrieval-based methods. It would be great to compare with other methods that use retrieval to augment language models."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper compares against BART and PRIMERA as baselines (Section 4).
   - The paper includes experiments with "Random-encoded training" (Section 4.2) which can be seen as a form of retrieval, but it's not a direct comparison with established retrieval-based methods.
3. Literature Gap Analysis:
   - There is no explicit comparison with methods like SLED or other standard retrieval-augmented language models in the experimental results.
4. Validation Analysis:
   - The reviewer is correct. The paper lacks a direct comparison with other established retrieval-based methods for language models.
5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "Experiments" section (Section 4) does not include comparisons with methods like SLED or other retrieval-augmented language models.

**Review 2**

1. Weakness Statement:
"The novelty of the proposed method is limited. The idea of using kNN to augment language models has been explored in prior work [1,2]. The main difference is that Unlimiformer performs the kNN in the embedding space instead of the input space, and does not require a separate datastore. However, the authors do not provide a detailed comparison with these prior works, and it is not clear how Unlimiformer differs from them in terms of implementation and performance."

2. Evidence Collection:
   - This is the same as the first weakness identified by Reviewer 1. Please see the analysis for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1.

1. Weakness Statement:
"The evaluation is not comprehensive. The paper only evaluates on summarization and QA tasks. It would be great to evaluate on a wider range of tasks, such as translation and code generation."

2. Evidence Collection:
   - This is the same as the second weakness identified by Reviewer 1. Please see the analysis for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1.

1. Weakness Statement:
"The paper does not provide a comparison with other retrieval-based methods. It would be great to compare with other methods that use retrieval to augment language models."

2. Evidence Collection:
   - This is the same as the third weakness identified by Reviewer 1. Please see the analysis for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1.

**Review 3**

1. Weakness Statement:
"The novelty of the proposed method is limited. The idea of using kNN to augment language models has been explored in prior work [1,2]. The main difference is that Unlimiformer performs the kNN in the embedding space instead of the input space, and does not require a separate datastore. However, the authors do not provide a detailed comparison with these prior works, and it is not clear how Unlimiformer differs from them in terms of implementation and performance."

2. Evidence Collection:
   - This is the same as the first weakness identified by Reviewer 1. Please see the analysis for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1.

1. Weakness Statement:
"The evaluation is not comprehensive. The paper only evaluates on summarization and QA tasks. It would be great to evaluate on a wider range of tasks, such as translation and code generation."

2. Evidence Collection:
   - This is the same as the second weakness identified by Reviewer 1. Please see the analysis for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1.

1. Weakness Statement:
"The paper does not provide a comparison with other retrieval-based methods. It would be great to compare with other methods that use retrieval to augment language models."

2. Evidence Collection:
   - This is the same as the third weakness identified by Reviewer 1. Please see the analysis for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1.

**Review 4**

1. Weakness Statement:
"The novelty of the proposed method is limited. The idea of using kNN to augment language models has been explored in prior work [1,2]. The main difference is that Unlimiformer performs the kNN in the embedding space instead of the input space, and does not require a separate datastore. However, the authors do not provide a detailed comparison with these prior works, and it is not clear how Unlimiformer differs from them in terms of implementation and performance."

2. Evidence Collection:
   - This is the same as the first weakness identified by Reviewer 1. Please see the analysis for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1.

1. Weakness Statement:
"The evaluation is not comprehensive. The paper only evaluates on summarization and QA tasks. It would be great to evaluate on a wider range of tasks, such as translation and code generation."

2. Evidence Collection:
   - This is the same as the second weakness identified by Reviewer 1. Please see the analysis for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1.

1. Weakness Statement:
"The paper does not provide a comparison with other retrieval-based methods. It would be great to compare with other methods that use retrieval to augment language models."

2. Evidence Collection:
   - This is the same as the third weakness identified by Reviewer 1. Please see the analysis for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1.

**Synthesis and Reflection:**

All reviewers raise similar concerns regarding the novelty of the proposed method, the comprehensiveness of the evaluation, and the lack of comparison with existing retrieval-based methods. Reviewers 1, 2, and 3 all point out that the core idea of using kNN for retrieval augmentation is not entirely novel, citing prior work like SLED and Memorizing Transformers. They highlight the difference in performing kNN in the embedding space versus the input space, but argue that this distinction is not sufficiently emphasized or explored in terms of its impact and novelty.

The most significant point of criticism revolves around the evaluation. All reviewers note that the evaluation is limited to summarization and question-answering tasks. They suggest expanding the evaluation to include tasks like translation and code generation to provide a more comprehensive assessment of the method's generalizability and effectiveness.

Furthermore, all reviewers express a lack of comparison with other retrieval-based methods. They argue that the paper would be strengthened by including experimental comparisons with methods like SLED or other standard retrieval-augmented language models. This would help to contextualize the performance of Unlimiformer and highlight its specific advantages or disadvantages.

There are no significant contradictions between the reviewers' opinions. They largely converge on the same key weaknesses: limited novelty, narrow evaluation scope, and lack of comparative analysis with existing retrieval methods.

**Final Conclusion:**

The reviewers' weaknesses are largely valid and well-supported by the paper's content. The paper could be strengthened by a more thorough discussion of related work, a more comprehensive evaluation, and a direct comparison with other retrieval-based methods.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces Unlimiformer, a retrieval-based approach designed to extend the input length capabilities of pre-trained language models without requiring additional training. The core idea revolves around constructing a k-Nearest Neighbors (kNN) index over the hidden states of the input sequence. During decoding, this index is used to retrieve the most relevant keys, which are then used to compute the attention scores, effectively limiting the attention mechanism to the most similar input tokens. This approach allows the model to theoretically process arbitrarily long inputs, as the retrieval process dynamically selects the most relevant context. The authors demonstrate that Unlimiformer can be applied to existing language models like BART and PRIMERA, enhancing their performance on long document summarization and question-answering tasks. The method is presented as a non-parametric approach, meaning that the retrieval index is constructed from the input data itself and does not require additional learnable parameters. The authors explore two main training strategies: applying Unlimiformer at validation or test time, and applying it directly during training. The empirical results show that Unlimiformer can improve the performance of base models on the selected tasks, particularly when combined with additional training strategies. The paper also includes an analysis of the computational cost of the method, showing that it is efficient, especially when compared to methods that require storing the entire input in memory. Overall, the paper presents a simple yet effective method for extending the context window of language models, with the potential to be applied to a wide range of tasks. However, as I will discuss in detail, the paper has some limitations that need to be addressed to fully realize its potential.


## Soundness:

2.25


## Presentation:

3.0


## Contribution:

2.0


## Strengths:

I found several aspects of this paper to be commendable. First, the proposed method is conceptually simple and easy to understand. The idea of using a kNN index over the hidden states to retrieve relevant keys for attention is straightforward, and the implementation details are clearly presented. This simplicity makes the method accessible and potentially easy to adopt by other researchers. Second, the method is effective in practice. The experimental results demonstrate that Unlimiformer can improve the performance of base models on long document summarization and question-answering tasks. The fact that the method can be applied to existing language models without requiring additional training is a significant advantage, as it allows for easy integration into existing workflows. Third, the authors provide a clear analysis of the computational cost of the method, showing that it is efficient and scalable. The paper also includes an ablation study that explores the impact of different training strategies, which is valuable for understanding the method's behavior. Finally, the paper is well-written and easy to follow, which makes it accessible to a broad audience. The authors clearly articulate the problem they are addressing, the proposed solution, and the experimental results. The paper is well-organized, and the figures and tables are clear and informative. These strengths highlight the potential of the Unlimiformer approach and its contribution to the field of long-context language modeling.


## Weaknesses:

Despite the strengths of the proposed method, I have identified several weaknesses that need to be addressed. First, the novelty of the method is limited. As pointed out by multiple reviewers, the core idea of using kNN to augment language models has been explored in prior work, such as SLED and Memorizing Transformers. While the authors claim that their method performs kNN in the embedding space rather than the input space, and that it does not require a separate datastore, these differences are not sufficiently explored or justified. The paper does not provide a detailed comparison of the implementation differences, such as the indexing method, the kNN algorithm used, and the way the retrieved context is integrated into the decoder. This lack of a thorough comparison makes it difficult to assess the true novelty and contribution of Unlimiformer. The paper mentions that their method does not require a separate datastore, but it does not fully explain how this is achieved or what the implications are for memory usage and computational cost. This lack of clarity undermines the claim of efficiency. My confidence in this assessment is high, as the paper itself acknowledges the existence of related work but fails to provide a detailed comparison. Second, the evaluation is not comprehensive. The paper only evaluates the method on summarization and question-answering tasks. It does not include evaluations on tasks such as translation or code generation, which are important for assessing the generalizability of the method. The lack of evaluation on a wider range of tasks makes it difficult to determine the applicability of Unlimiformer to different domains. For example, the paper does not explore how the method performs on tasks that require different types of reasoning or that involve different linguistic structures. This limited evaluation scope restricts the conclusions that can be drawn about the method's effectiveness. My confidence in this assessment is high, as the paper explicitly states the tasks used for evaluation, and they do not include translation or code generation. Third, the paper does not provide a comparison with other retrieval-based methods. While the paper compares against BART and PRIMERA as baselines, it does not include a direct comparison with other established retrieval-augmented language models, such as SLED or other similar methods. This lack of comparison makes it difficult to assess the relative advantages and disadvantages of Unlimiformer. The paper does not provide a quantitative comparison of performance, including metrics like ROUGE and BLEU for summarization tasks, and accuracy for QA tasks. This lack of comparison makes it difficult to understand how Unlimiformer performs relative to other methods. My confidence in this assessment is high, as the paper does not include any experimental results that directly compare Unlimiformer with other retrieval-based methods. Finally, the paper does not provide a detailed analysis of the computational cost of the method. While the paper includes an analysis of the computational cost, it does not provide a quantitative analysis of the time and memory requirements, especially when dealing with long inputs. This lack of analysis makes it difficult to assess the practical feasibility of the method. The paper does not provide a detailed breakdown of the computational cost, including the time required for indexing, retrieval, and decoding. This lack of analysis makes it difficult to understand the trade-offs between performance and efficiency. My confidence in this assessment is high, as the paper does not provide a detailed quantitative analysis of the computational cost.


## Suggestions:

To address the identified weaknesses, I recommend several improvements. First, the authors should provide a more detailed comparison with existing retrieval-augmented language models. Specifically, they should compare Unlimiformer with methods that use sparse retrieval, such as those based on inverted indexes, and dense retrieval methods. This comparison should include an analysis of the trade-offs between performance, computational cost, and memory usage. For example, the authors could compare the retrieval accuracy, latency, and memory footprint of Unlimiformer with these other methods. This would help to better understand the strengths and weaknesses of the proposed approach and its position within the broader landscape of retrieval-augmented language models. Furthermore, the authors should clarify the specific implementation details of Unlimiformer, such as the choice of the kNN algorithm, the indexing method, and the way the retrieved context is integrated into the decoder. This would make it easier for other researchers to reproduce the results and build upon this work. Second, the authors should expand their experimental evaluation to include a wider range of tasks. This should include tasks such as machine translation, code generation, and question answering over long documents. For each task, the authors should provide a detailed analysis of the performance of Unlimiformer, including the impact of different hyperparameters and training strategies. This would help to better understand the generalizability of the proposed method and its applicability to different domains. In addition, the authors should consider evaluating their method on tasks that require different types of reasoning, such as logical inference or commonsense reasoning. This would help to understand the strengths and weaknesses of their approach in different scenarios. The authors should also provide a detailed analysis of the results, including error analysis and ablation studies, to understand the factors that contribute to the performance of their method. Third, the authors should provide a more detailed analysis of the computational cost of Unlimiformer. This analysis should consider the impact of different parameters, such as the number of retrieved tokens and the size of the index. This would help to assess the practical feasibility of the method and its suitability for different applications. The authors should also provide a more detailed analysis of the memory requirements of the method, especially when dealing with long inputs. This would help to understand the trade-offs between performance and efficiency. Finally, the authors should provide a more thorough discussion of the limitations of Unlimiformer and potential directions for future research. This should include a discussion of the potential biases introduced by the kNN index and the limitations of the kNN algorithm in capturing long-range dependencies. The authors should also discuss the potential for overfitting to the training data and the generalizability of their method to unseen data. Furthermore, the authors should explore potential avenues for future research, such as incorporating external knowledge sources or using more advanced indexing techniques. This would help to position their work within the broader context of retrieval-augmented language models and to identify promising directions for future research. By addressing these points, the authors can significantly strengthen their paper and make a more substantial contribution to the field.


## Questions:

I have several questions regarding the methodology and results presented in this paper. First, how does Unlimiformer compare to other retrieval-based methods for long-context language models, such as SLED or other similar approaches, in terms of both performance and computational cost? A direct comparison with these methods would help to better understand the specific advantages and disadvantages of Unlimiformer. Second, how does Unlimiformer perform on tasks other than summarization and question-answering, such as translation or code generation? The lack of evaluation on these tasks limits our understanding of the method's generalizability. Third, how does Unlimiformer compare to other methods that use retrieval to augment language models? The paper does not provide a direct comparison with these methods, which makes it difficult to assess the relative performance of Unlimiformer. Fourth, what is the computational cost of Unlimiformer, in terms of time and memory requirements, especially when dealing with long inputs? The paper provides a general analysis of computational cost, but it lacks a detailed quantitative analysis. Fifth, what are the limitations of Unlimiformer, and what are the potential directions for future research? The paper does not provide a thorough discussion of the limitations of the method, which makes it difficult to understand its potential for further development. Finally, how does the choice of the kNN algorithm and the indexing method affect the performance of Unlimiformer? The paper does not provide a detailed analysis of these implementation choices, which makes it difficult to understand the factors that contribute to the method's performance. Addressing these questions would help to clarify the strengths and weaknesses of the proposed method and to identify areas for future research.


## Rating:

5.0


## Confidence:

4.0


## Decision:

Reject
}