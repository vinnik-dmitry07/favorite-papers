I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper proposes a novel method for aligning LLMs with human preferences without the need for human annotations. The authors introduce stable rank, a metric that measures the effective dimensionality of the hidden states in an LLM. They demonstrate that stable rank can be used as a zero-shot reward proxy for evaluating the quality of model responses. The authors also propose Stable Rank Group Relative Policy Optimization (SR-GRPO), a reinforcement learning algorithm that uses stable rank as a reward signal for fine-tuning LLMs. The authors evaluate their methods on several benchmarks and show that they outperform existing approaches.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper introduces a novel metric, stable rank, for evaluating the quality of model responses without the need for human annotations. This is a significant contribution to the field of LLM alignment.
- The authors provide extensive empirical evidence to support their claims, including experiments on multiple benchmarks and comparisons with existing approaches.
- The paper is well-written and easy to follow, with clear explanations of the proposed methods and results.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a clear motivation for why stable rank is a good proxy for human preferences. While the authors show that stable rank correlates with response quality, it is not clear why this correlation exists. A more detailed explanation of the theoretical underpinnings of stable rank and its relationship to human preferences would be helpful.
- The paper does not discuss the limitations of stable rank as a proxy for human preferences. For example, it is not clear how stable rank would perform in cases where human preferences are inconsistent or subjective. A discussion of the potential biases and limitations of stable rank would be valuable.
- The paper does not provide a comparison of stable rank with other existing metrics for evaluating model responses. While the authors show that stable rank outperforms existing approaches, it is not clear how it compares to other metrics that are commonly used in the field. A more comprehensive comparison of stable rank with other metrics would be helpful.

### Suggestions

The paper would benefit from a more in-depth analysis of why stable rank correlates with human preferences. While the authors demonstrate a correlation, they do not provide a clear theoretical explanation for this relationship. It would be valuable to explore the mathematical properties of stable rank and how they relate to the characteristics of human-annotated data. For example, do models that generate responses with higher stable rank also exhibit other properties that are commonly associated with high-quality text, such as coherence, fluency, or relevance? A more detailed analysis of these relationships would strengthen the paper's claims and provide a more solid foundation for the use of stable rank as a proxy for human preferences. Furthermore, the authors should consider exploring the sensitivity of stable rank to different model architectures and training procedures. Does stable rank consistently predict human preferences across different models, or are there specific conditions under which it is more or less reliable? Understanding these limitations is crucial for the practical application of the proposed method.

To address the limitations of stable rank, the authors should discuss potential biases and scenarios where it might fail to accurately reflect human preferences. For example, how would stable rank perform when evaluating responses that are ambiguous or open to multiple interpretations? Would it be able to distinguish between responses that are factually correct but not informative, and responses that are informative but not factually correct? Additionally, the authors should consider the impact of different prompt formats and evaluation criteria on the performance of stable rank. How sensitive is stable rank to variations in the way that human preferences are elicited? A more thorough discussion of these limitations would provide a more balanced and nuanced perspective on the proposed method. It would also be beneficial to explore alternative metrics that could complement or augment stable rank, such as metrics based on semantic similarity or diversity. A hybrid approach that combines multiple metrics could potentially provide a more robust and reliable measure of response quality.

Finally, the paper should include a more comprehensive comparison of stable rank with other existing metrics for evaluating model responses. While the authors show that stable rank outperforms existing approaches, it is not clear how it compares to other metrics that are commonly used in the field. For example, how does stable rank compare to metrics based on perplexity, BLEU score, or ROUGE score? A more detailed comparison of stable rank with other metrics would help to contextualize the paper's contributions and highlight its unique advantages and disadvantages. The authors should also consider the computational cost and efficiency of stable rank compared to other metrics. Is stable rank computationally expensive to calculate, and how does its performance scale with the size of the model and the length of the responses? A thorough analysis of these factors would provide a more complete picture of the practical implications of the proposed method.

### Questions

- How does stable rank compare to other existing metrics for evaluating model responses?
- What are the limitations of stable rank as a proxy for human preferences?
- How does stable rank perform in cases where human preferences are inconsistent or subjective?

### Rating

6

### Confidence

3

**********

## Reviewer 2

### Summary

This paper proposes to use stable rank, a metric that measures the effective dimensionality of hidden states, as an intrinsic reward signal for reinforcement learning. The authors show that stable rank correlates with response quality and can be used to improve reasoning across multiple benchmarks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide extensive experiments to support their claims.
3. The proposed method is simple and effective.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a strong motivation for why stable rank is a good proxy for human preferences. While the authors show that stable rank correlates with response quality, it is not clear why this correlation exists. A more detailed explanation of the theoretical underpinnings of stable rank and its relationship to human preferences would be helpful.
2. The paper does not discuss the limitations of stable rank as a proxy for human preferences. For example, it is not clear how stable rank would perform in cases where human preferences are inconsistent or subjective. A discussion of the potential biases and limitations of stable rank would be valuable.
3. The paper does not provide a comparison of stable rank with other existing metrics for evaluating model responses. While the authors show that stable rank outperforms existing approaches, it is not clear how it compares to other metrics that are commonly used in the field. A more comprehensive comparison of stable rank with other metrics would be helpful.

### Suggestions

The authors should delve deeper into the theoretical justification for using stable rank as a proxy for human preference. While the empirical results are promising, a more rigorous explanation of why the effective dimensionality of hidden states correlates with response quality is needed. For instance, they could explore the connection between stable rank and other measures of text complexity or information content. Furthermore, it would be beneficial to analyze the specific types of errors that stable rank is able to capture, and how these errors relate to human preferences. A more detailed analysis of the relationship between stable rank and human judgments would strengthen the paper's claims.

To address the limitations of stable rank, the authors should conduct experiments that specifically test its robustness to variations in human preferences. This could involve using datasets with varying levels of subjectivity or ambiguity, or by introducing controlled variations in the evaluation criteria. The authors should also discuss the potential biases that might be introduced by using stable rank as a proxy for human preferences. For example, are there specific types of responses that are more likely to be favored by stable rank, even if they are not preferred by humans? A thorough discussion of these limitations would provide a more balanced and nuanced perspective on the proposed method. It would also be useful to explore the sensitivity of stable rank to different model architectures and training procedures.

Finally, the authors should provide a more comprehensive comparison of stable rank with other existing metrics for evaluating model responses. This comparison should not only focus on the performance of different metrics on various benchmarks, but also on their computational cost, ease of implementation, and interpretability. For example, how does stable rank compare to metrics based on perplexity, BLEU score, or ROUGE score in terms of these factors? A more detailed analysis of the strengths and weaknesses of different metrics would help to contextualize the contribution of stable rank and provide a more complete picture of the landscape of response evaluation metrics.

### Questions

1. How does stable rank compare to other existing metrics for evaluating model responses?
2. What are the limitations of stable rank as a proxy for human preferences?
3. How does stable rank perform in cases where human preferences are inconsistent or subjective?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper introduces stable rank, a novel intrinsic reward signal for reinforcement learning, which leverages the effective dimensionality of hidden states to measure quality without external supervision. The authors demonstrate that stable rank correlates with response quality and can improve reasoning performance across multiple benchmarks. They also propose Stable Rank Group Relative Policy Optimization (SR-GRPO), which uses stable rank as a reward signal for reinforcement learning. The authors validate their approach on several benchmarks, showing that it outperforms existing methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper introduces a novel and theoretically grounded approach to reward design for reinforcement learning, which is a significant contribution to the field.
- The authors provide extensive empirical evidence to support their claims, including experiments on multiple benchmarks and comparisons with existing approaches.
- The paper is well-written and easy to follow, with clear explanations of the proposed methods and results.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a strong motivation for why stable rank is a good proxy for human preferences. While the authors show that stable rank correlates with response quality, it is not clear why this correlation exists. A more detailed explanation of the theoretical underpinnings of stable rank and its relationship to human preferences would be helpful.
- The paper does not discuss the limitations of stable rank as a proxy for human preferences. For example, it is not clear how stable rank would perform in cases where human preferences are inconsistent or subjective. A discussion of the potential biases and limitations of stable rank would be valuable.
- The paper does not provide a comparison of stable rank with other existing metrics for evaluating model responses. While the authors show that stable rank outperforms existing approaches, it is not clear how it compares to other metrics that are commonly used in the field. A more comprehensive comparison of stable rank with other metrics would be helpful.

### Suggestions

The authors should provide a more thorough analysis of why stable rank correlates with human preferences. While the empirical results are promising, a deeper theoretical explanation is needed to justify the use of stable rank as a proxy for human judgment. This could involve exploring the mathematical properties of stable rank and how they relate to the characteristics of human-annotated data. For example, do models that generate responses with higher stable rank also exhibit other properties that are commonly associated with high-quality text, such as coherence, fluency, or relevance? A more detailed analysis of these relationships would strengthen the paper's claims and provide a more solid foundation for the use of stable rank as a reward signal. Furthermore, the authors should investigate the sensitivity of stable rank to different model architectures and training procedures. Does stable rank consistently predict human preferences across different models, or are there specific conditions under which it is more or less reliable? Understanding these limitations is crucial for the practical application of the proposed method.

To address the limitations of stable rank, the authors should conduct experiments that specifically test its robustness to variations in human preferences. This could involve using datasets with varying levels of subjectivity or ambiguity, or by introducing controlled variations in the evaluation criteria. The authors should also discuss the potential biases that might be introduced by using stable rank as a proxy for human preferences. For example, are there specific types of responses that are more likely to be favored by stable rank, even if they are not preferred by humans? A thorough discussion of these limitations would provide a more balanced and nuanced perspective on the proposed method. It would also be useful to explore the sensitivity of stable rank to different model architectures and training procedures. Does stable rank consistently predict human preferences across different models, or are there specific conditions under which it is more or less reliable? Understanding these limitations is crucial for the practical application of the proposed method.

Finally, the authors should provide a more comprehensive comparison of stable rank with other existing metrics for evaluating model responses. This comparison should not only focus on the performance of different metrics on various benchmarks, but also on their computational cost, ease of implementation, and interpretability. For example, how does stable rank compare to metrics based on perplexity, BLEU score, or ROUGE score in terms of these factors? A more detailed analysis of the strengths and weaknesses of different metrics would help to contextualize the contribution of stable rank and provide a more complete picture of the landscape of response evaluation metrics. The authors should also consider the potential for combining stable rank with other metrics to create a more robust and reliable evaluation framework.

### Questions

- How does stable rank compare to other existing metrics for evaluating model responses?
- What are the limitations of stable rank as a proxy for human preferences?
- How does stable rank perform in cases where human preferences are inconsistent or subjective?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

This paper proposes a new approach to aligning LLMs with human preferences by leveraging the stable rank of hidden states. The authors introduce Stable Rank Group Relative Policy Optimization (SR-GRPO), a method that uses stable rank as a reward signal for reinforcement learning. They demonstrate that stable rank can be used as a zero-shot reward proxy and improves reasoning across multiple benchmarks, outperforming both learned reward models and self-evaluation baselines.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper introduces a novel approach to reward design for reinforcement learning, which is a significant contribution to the field.
- The authors provide extensive empirical evidence to support their claims, including experiments on multiple benchmarks and comparisons with existing approaches.
- The paper is well-written and easy to follow, with clear explanations of the proposed methods and results.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a strong motivation for why stable rank is a good proxy for human preferences. While the authors show that stable rank correlates with response quality, it is not clear why this correlation exists. A more detailed explanation of the theoretical underpinnings of stable rank and its relationship to human preferences would be helpful.
- The paper does not discuss the limitations of stable rank as a proxy for human preferences. For example, it is not clear how stable rank would perform in cases where human preferences are inconsistent or subjective. A discussion of the potential biases and limitations of stable rank would be valuable.
- The paper does not provide a comparison of stable rank with other existing metrics for evaluating model responses. While the authors show that stable rank outperforms existing approaches, it is not clear how it compares to other metrics that are commonly used in the field. A more comprehensive comparison of stable rank with other metrics would be helpful.

### Suggestions

The authors should delve deeper into the theoretical justification for using stable rank as a proxy for human preference. While the empirical results are promising, a more rigorous explanation of why the effective dimensionality of hidden states correlates with response quality is needed. For instance, they could explore the connection between stable rank and other measures of text complexity or information content. Furthermore, it would be beneficial to analyze the specific types of errors that stable rank is able to capture, and how these errors relate to human preferences. A more detailed analysis of the relationship between stable rank and human judgments would strengthen the paper's claims.

To address the limitations of stable rank, the authors should conduct experiments that specifically test its robustness to variations in human preferences. This could involve using datasets with varying levels of subjectivity or ambiguity, or by introducing controlled variations in the evaluation criteria. The authors should also discuss the potential biases that might be introduced by using stable rank as a proxy for human preferences. For example, are there specific types of responses that are more likely to be favored by stable rank, even if they are not preferred by humans? A thorough discussion of these limitations would provide a more balanced and nuanced perspective on the proposed method. It would also be useful to explore the sensitivity of stable rank to different model architectures and training procedures.

Finally, the authors should provide a more comprehensive comparison of stable rank with other existing metrics for evaluating model responses. This comparison should not only focus on the performance of different metrics on various benchmarks, but also on their computational cost, ease of implementation, and interpretability. For example, how does stable rank compare to metrics based on perplexity, BLEU score, or ROUGE score in terms of these factors? A more detailed analysis of the strengths and weaknesses of different metrics would help to contextualize the contribution of stable rank and provide a more complete picture of the landscape of response evaluation metrics. The authors should also consider the potential for combining stable rank with other metrics to create a more robust and reliable evaluation framework.

### Questions

- How does stable rank compare to other existing metrics for evaluating model responses?
- What are the limitations of stable rank as a proxy for human preferences?
- How does stable rank perform in cases where human preferences are inconsistent or subjective?

### Rating

8

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The reviewer has identified three main weaknesses: lack of motivation for stable rank as a proxy, lack of discussion on limitations, and lack of comparison with other metrics. I need to go through the paper and see if these criticisms are valid and supported by the content.

**Weakness 1: Lack of motivation for stable rank as a proxy**

*   **Initial Categorization:** Methodological. The reviewer is questioning the theoretical basis for using stable rank.
*   **Method-related Evidence:**
    *   The paper introduces stable rank in the "main_idea" and "method" sections.
    *   The motivation is stated as: "However, existing methods for aligning LLMs with human preferences face significant limitations, including reliance on external supervision, reward hacking, and poor scalability. These limitations motivate the need for a novel, intrinsic, and scalable approach to reward design that leverages the internal geometric properties of LLM hidden states."
    *   The paper argues that "high-quality generations should maintain higher effective dimensionality, while low-quality outputs exhibit rank collapse."
    *   The connection to human preferences is made through the "zero-shot reward proxy" concept, where "stable rank measures the effective dimensionality of hidden states by computing the ratio of total variance to dominant-direction variance in the hidden-state representation. It balances representational richness with coherence, capturing quality through how information spreads across the embedding space."
*   **Literature Gap Analysis:** The paper cites works related to the softmax bottleneck (Yang et al., 2018; Godey et al., 2024) and representation collapse (Gao et al., 2019), which provide some theoretical grounding for the idea that high-dimensional representations are better for capturing information.
*   **Validation Analysis:** The reviewer is correct that the paper doesn't provide a *deep* theoretical dive into *why* stable rank *specifically* correlates with human preferences. The paper focuses more on the geometric intuition and the empirical validation. While the motivation for using it as a proxy is stated (intrinsic, scalable), the *why* is less explored theoretically.
*   **Conclusion:** Partially Valid. Confidence: High. The paper states the motivation but lacks a deep theoretical explanation of the correlation with human preferences.

**Weakness 2: Lack of discussion on limitations**

*   **Initial Categorization:** Methodological. The reviewer is pointing out the absence of a discussion on the shortcomings of the proposed method.
*   **Method-related Evidence:** The paper primarily focuses on the strengths and empirical results of stable rank.
*   **Literature Gap Analysis:**  While the paper mentions limitations of existing methods, it doesn't explicitly discuss the limitations of stable rank itself.
*   **Validation Analysis:** The reviewer's point is valid. The paper doesn't delve into scenarios where stable rank might fail or be less effective. The "Summary" section briefly mentions "moderate correlation with text quality metrics," hinting at a limitation, but it's not explored in detail.
*   **Conclusion:** Valid. Confidence: High. The paper lacks a dedicated discussion on the limitations of stable rank.

**Weakness 3: Lack of comparison with other metrics**

*   **Initial Categorization:** Experimental. The reviewer is criticizing the lack of a comprehensive comparison with existing evaluation metrics.
*   **Method-related Evidence:** The "Experiments" section includes comparisons with "Pointwise Scoring," "Pairwise Comparison," and " IPO" for zero-shot reward proxy evaluation, and "Skywork-Reward-V2-Qwen3-1.7B," "Self-Reward," and "Perplexity" for Best-of-N sampling.
*   **Literature Gap Analysis:** The paper does compare against some existing methods, but it doesn't provide a broad comparison with a wider range of text quality metrics like BLEU, ROUGE, or more advanced semantic similarity measures.
*   **Validation Analysis:** The reviewer is correct. While the paper compares against some baselines, a more comprehensive comparison with a broader set of text quality metrics would strengthen the evaluation.
*   **Conclusion:** Valid. Confidence: High. The paper lacks a comprehensive comparison with other text quality metrics.

**Synthesis and Reflection:**

All three weaknesses identified by the reviewer are valid to varying degrees. The lack of deep theoretical motivation for stable rank as a proxy for human preferences is a valid point. The paper focuses on the geometric intuition and empirical results but doesn't fully explore the theoretical underpinnings of the correlation. The lack of a dedicated discussion on the limitations of stable rank is also valid. While the paper hints at a correlation with text quality metrics, it doesn't thoroughly explore scenarios where stable rank might fail. Finally, the lack of a comprehensive comparison with other text quality metrics is a valid criticism. While the paper includes some comparisons, a broader evaluation against a wider range of metrics would be beneficial.

There are no conflicting opinions between the reviewer and the paper's content. The reviewer's suggestions for improvement are well-aligned with the identified weaknesses.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces Stable Rank, a novel intrinsic reward signal for reinforcement learning that leverages the effective dimensionality of hidden states to measure the quality of model responses without relying on external human annotations. The authors propose that stable rank, derived from the singular value decomposition of hidden states, captures the richness and coherence of generated text by quantifying the effective dimensionality of the representation. This metric is presented as a zero-shot reward proxy, capable of evaluating the quality of model responses directly from the hidden states. The core idea is that higher-quality generations maintain higher effective dimensionality, while low-quality outputs exhibit rank collapse. The authors demonstrate the utility of Stable Rank in two main ways: first, as a reward signal for reinforcement learning, where it is used to fine-tune language models, and second, as a zero-shot evaluation metric, where it is used to assess the quality of model-generated text. In the reinforcement learning setting, the authors introduce Stable Rank Group Relative Policy Optimization (SR-GRPO), an algorithm that uses Stable Rank to guide the policy learning process. They show that SR-GRPO outperforms existing methods on several reasoning benchmarks. In the zero-shot evaluation setting, they show that Stable Rank correlates well with human judgments of text quality, outperforming several baselines, including perplexity and self-evaluation methods. The authors conduct extensive experiments to validate their approach, using multiple models and datasets. They show that Stable Rank is effective in both reward modeling and zero-shot evaluation, and that SR-GRPO is a robust and scalable method for aligning language models with human preferences. The paper's main contribution is the introduction of Stable Rank as a novel, intrinsic reward signal for reinforcement learning, and its application to the problem of aligning language models with human preferences. The authors demonstrate the effectiveness of their approach through a series of well-designed experiments, providing a valuable contribution to the field of natural language processing.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

2.75


## Strengths:

I find several aspects of this paper to be particularly strong. First, the introduction of Stable Rank as an intrinsic reward signal is a novel and significant contribution. The idea of using the effective dimensionality of hidden states as a measure of text quality is both elegant and intuitive. It provides a way to evaluate the quality of model responses without relying on external human annotations, which is a major advantage. The authors' theoretical motivation, which connects Stable Rank to the concepts of representational richness and coherence, is also compelling. They argue that high-quality generations should maintain higher effective dimensionality, while low-quality outputs exhibit rank collapse, and this is supported by their empirical results. The paper is also well-written and easy to follow, with clear explanations of the proposed methods and results. The authors provide a comprehensive set of experiments to support their claims, including comparisons with several baselines and evaluations on multiple benchmarks. The fact that Stable Rank correlates well with human judgments of text quality is a particularly strong result, demonstrating the practical relevance of their approach. Furthermore, the introduction of SR-GRPO, a reinforcement learning algorithm that uses Stable Rank as a reward signal, is a valuable contribution. The authors show that SR-GRPO outperforms existing methods on several reasoning benchmarks, demonstrating the effectiveness of their approach in a practical setting. The fact that Stable Rank is effective in both reward modeling and zero-shot evaluation is also a significant strength of the paper. Finally, the authors' focus on scalability and robustness is commendable. They demonstrate that their approach is effective across multiple models and datasets, which is a crucial consideration for real-world applications.


## Weaknesses:

While I find the paper to be generally strong, there are several weaknesses that I believe warrant further discussion. First, the paper lacks a deep theoretical motivation for why stable rank is a good proxy for human preferences. While the authors provide a geometric intuition and empirical evidence, they do not fully explain why the effective dimensionality of hidden states correlates with response quality as perceived by humans. The paper states that stable rank measures the effective dimensionality of hidden states by computing the ratio of total variance to dominant-direction variance in the hidden-state representation. It balances representational richness with coherence, capturing quality through how information spreads across the embedding space. However, this explanation is somewhat abstract and does not provide a clear theoretical link to human preferences. The paper argues that high-quality generations should maintain higher effective dimensionality, while low-quality outputs exhibit rank collapse, but it does not delve into the specific properties of human-annotated data that make stable rank a suitable proxy. This lack of a strong theoretical foundation makes it difficult to fully understand the underlying mechanisms of the proposed method. My confidence in this weakness is high, as the paper's motivation is primarily empirical, and a deeper theoretical analysis is missing. Second, the paper does not adequately discuss the limitations of stable rank as a proxy for human preferences. While the authors show that stable rank correlates with response quality, they do not explore the potential biases or scenarios where it might fail to accurately reflect human preferences. For example, the paper does not discuss how stable rank would perform in cases where human preferences are inconsistent or subjective. It is possible that stable rank might favor certain types of responses that are not preferred by humans, and the paper does not address this possibility. The paper also does not discuss the potential for stable rank to be sensitive to different model architectures and training procedures. It is possible that stable rank might consistently predict human preferences across different models, or that it might be more or less reliable depending on the specific training data and objectives. The paper's lack of a discussion on these limitations is a significant weakness. My confidence in this weakness is high, as the paper does not include any experiments that specifically test the robustness of stable rank to variations in human preferences or different model architectures. Finally, the paper does not provide a comprehensive comparison of stable rank with other existing metrics for evaluating model responses. While the authors show that stable rank outperforms several baselines, they do not compare it to a wider range of text quality metrics, such as BLEU, ROUGE, or more advanced semantic similarity measures. This lack of a comprehensive comparison makes it difficult to contextualize the contribution of stable rank and to understand its strengths and weaknesses relative to other approaches. The paper does compare against Pointwise Scoring, Pairwise Comparison, and IPO for zero-shot reward proxy evaluation, and Skywork-Reward-V2-Qwen3-1.7B, Self-Reward, and Perplexity for Best-of-N sampling, but it does not include a more extensive comparison with other text quality metrics. This omission is a significant weakness, as it limits the ability to fully assess the value of the proposed method. My confidence in this weakness is high, as the paper's experimental section does not include a comprehensive comparison with a wide range of text quality metrics.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should delve deeper into the theoretical justification for using stable rank as a proxy for human preference. While the empirical results are promising, a more rigorous explanation of why the effective dimensionality of hidden states correlates with response quality is needed. This could involve exploring the mathematical properties of stable rank and how they relate to the characteristics of human-annotated data. For example, do models that generate responses with higher stable rank also exhibit other properties that are commonly associated with high-quality text, such as coherence, fluency, or relevance? A more detailed analysis of these relationships would strengthen the paper's claims and provide a more solid foundation for the use of stable rank as a reward signal. Furthermore, the authors should investigate the sensitivity of stable rank to different model architectures and training procedures. Does stable rank consistently predict human preferences across different models, or are there specific conditions under which it is more or less reliable? Understanding these limitations is crucial for the practical application of the proposed method. Second, the authors should conduct experiments that specifically test the robustness of stable rank to variations in human preferences. This could involve using datasets with varying levels of subjectivity or ambiguity, or by introducing controlled variations in the evaluation criteria. The authors should also discuss the potential biases that might be introduced by using stable rank as a proxy for human preferences. For example, are there specific types of responses that are more likely to be favored by stable rank, even if they are not preferred by humans? A thorough discussion of these limitations would provide a more balanced and nuanced perspective on the proposed method. It would also be useful to explore the sensitivity of stable rank to different model architectures and training procedures. Does stable rank consistently predict human preferences across different models, or are there specific conditions under which it is more or less reliable? Understanding these limitations is crucial for the practical application of the proposed method. Third, the authors should provide a more comprehensive comparison of stable rank with other existing metrics for evaluating model responses. This comparison should not only focus on the performance of different metrics on various benchmarks, but also on their computational cost, ease of implementation, and interpretability. For example, how does stable rank compare to metrics based on perplexity, BLEU score, or ROUGE score in terms of these factors? A more detailed analysis of the strengths and weaknesses of different metrics would help to contextualize the contribution of stable rank and provide a more complete picture of the landscape of response evaluation metrics. The authors should also consider the potential for combining stable rank with other metrics to create a more robust and reliable evaluation framework. Finally, the authors should explore alternative metrics that could complement or augment stable rank. While stable rank is a promising approach, it is not clear how it compares to other metrics that are commonly used in the field. A more comprehensive comparison of stable rank with other metrics would help to contextualize the paper's contributions and highlight its unique advantages and disadvantages. The authors should also consider the potential for combining stable rank with other metrics to create a more robust and reliable evaluation framework.


## Questions:

I have several questions that I believe would help to further clarify the paper's contributions and limitations. First, how does stable rank compare to other existing metrics for evaluating model responses, such as BLEU score, ROUGE score, or semantic similarity measures? While the paper compares against some baselines, a more comprehensive comparison with a wider range of text quality metrics would be valuable. Second, what are the limitations of stable rank as a proxy for human preferences? The paper does not discuss the potential biases or scenarios where stable rank might fail to accurately reflect human preferences. It would be helpful to understand the specific types of errors that stable rank is able to capture, and how these errors relate to human preferences. Third, how does stable rank perform in cases where human preferences are inconsistent or subjective? The paper does not explore the robustness of stable rank to variations in human preferences. It would be valuable to understand how stable rank would perform in scenarios where there is no clear consensus among human annotators. Fourth, how does stable rank compare to other intrinsic reward signals for reinforcement learning? The paper introduces Stable Rank as an intrinsic reward signal, but it does not compare it to other intrinsic reward signals, such as those based on information gain or novelty. A comparison with other intrinsic reward signals would help to contextualize the contribution of stable rank and to understand its strengths and weaknesses relative to other approaches. Finally, what are the computational costs of stable rank compared to other metrics? The paper does not discuss the computational cost of stable rank, which is an important factor for practical applications. It would be helpful to understand the computational overhead associated with computing stable rank and how it compares to other metrics. Addressing these questions would provide a more complete understanding of the proposed method and its limitations.


## Rating:

6.5


## Confidence:

3.0


## Decision:

Accept
}