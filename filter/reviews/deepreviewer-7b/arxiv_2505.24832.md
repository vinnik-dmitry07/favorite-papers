I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper proposes a new definition of memorization that quantifies the amount of information a model stores about a specific data point. The authors use Kolmogorov complexity to define memorization and compression rate to measure it. They estimate Kolmogorov complexity using arithmetic coding and model likelihoods. The paper presents experiments on synthetic and real text datasets to measure memorization capacity and scaling laws for membership inference. The findings suggest that models can memorize up to 3.5-4 bits per parameter and that double descent occurs when models exceed their capacity.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel definition of memorization based on Kolmogorov complexity, which provides a theoretical foundation for measuring unintended memorization.
2. The authors conduct experiments on both synthetic and real text datasets, demonstrating the applicability of their definition across different types of data.
3. The paper provides a comprehensive analysis of the relationship between model capacity, dataset size, and memorization, offering insights into the behavior of language models.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's reliance on Kolmogorov complexity, while theoretically sound, is difficult to compute in practice. The authors use arithmetic coding as an approximation, but the accuracy of this approximation is not thoroughly discussed. The choice of arithmetic coding, while practical, lacks a strong justification compared to other potential compression methods, especially given the existence of more sophisticated lossless compression algorithms that might provide tighter bounds on the Kolmogorov complexity. The paper should include a more detailed analysis of the approximation error introduced by this choice and explore the sensitivity of the results to different compression techniques.
2. The experiments are primarily conducted on synthetic data, which may not fully capture the complexities of real-world text. While the authors do include experiments on real text, the analysis of these experiments could be more in-depth. The paper should provide a more detailed analysis of the memorization patterns observed in real-world text, including a discussion of the types of information that are most likely to be memorized and how this varies across different datasets and model architectures. The current analysis lacks a granular view of memorization in real text, focusing more on aggregate metrics.
3. The paper does not adequately address the potential impact of different training algorithms and data preprocessing techniques on memorization. The paper should include a more thorough investigation of how different training parameters, such as learning rate, batch size, and regularization techniques, affect the memorization capacity of the models. Additionally, the impact of data preprocessing steps, such as tokenization and normalization, should be explored. The current analysis lacks a systematic study of these factors, which are known to influence model behavior.

### Suggestions

The paper should delve deeper into the practical challenges of approximating Kolmogorov complexity. While arithmetic coding is a reasonable starting point, the authors should explore and justify why it is superior to other compression algorithms, especially those that might be more closely aligned with the theoretical definition of Kolmogorov complexity. A detailed analysis of the approximation error introduced by the choice of compression algorithm is crucial. This analysis should include a comparison of the compression rates obtained using different algorithms and a discussion of how these differences might affect the measured memorization capacity. Furthermore, the authors should investigate the sensitivity of their results to variations in the compression algorithm, which would provide a more robust assessment of the proposed memorization metric. This could involve experimenting with different compression methods and analyzing the resulting changes in the measured memorization capacity.

To strengthen the analysis of real-world text, the authors should provide a more granular view of memorization patterns. This could involve analyzing the types of information that are most likely to be memorized, such as specific phrases, entities, or stylistic features. The paper should also explore how these memorization patterns vary across different datasets and model architectures. For example, do models trained on different datasets exhibit different memorization behaviors? Are certain model architectures more prone to memorizing specific types of information? A more detailed analysis of these questions would provide a more comprehensive understanding of memorization in real-world scenarios. The authors could also consider using techniques such as attention visualization to gain insights into which parts of the input are most influential in the model's predictions, which could help identify memorized information.

Finally, the paper should include a more thorough investigation of the impact of training algorithms and data preprocessing techniques on memorization. This should include a systematic study of how different training parameters, such as learning rate, batch size, and regularization techniques, affect the memorization capacity of the models. The authors should also explore the impact of data preprocessing steps, such as tokenization and normalization, on memorization. For example, do different tokenization strategies lead to different memorization behaviors? How does the length of the input text affect memorization? A more comprehensive analysis of these factors would provide a more complete picture of the factors that influence memorization in language models. This could involve conducting experiments with different training parameters and data preprocessing techniques and analyzing the resulting changes in memorization capacity.

### Questions

1. How sensitive are your results to the choice of compression algorithm? Have you explored other compression methods besides arithmetic coding?
2. Can you provide more details on how you estimated the reference model for unintended memorization? How does the choice of reference model affect your results?
3. How do you expect your findings to generalize to larger language models and datasets? Are there any limitations to the current experimental setup that might affect the scalability of your results?

### Rating

6

### Confidence

4

**********

## Reviewer 2

### Summary

This paper proposes a new definition of memorization, which is the information a model has about a specific data point. The authors then use this definition to measure the capacity of modern language models and analyze how membership inference performance scales with model and dataset size.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow.
- The proposed definition of memorization is intuitive and well-motivated.
- The experiments are thorough and provide valuable insights into the behavior of language models.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a clear definition of what constitutes a "sample" in the context of the proposed definition of memorization. It is unclear whether a sample refers to a single data point, a batch of data points, or something else entirely. This ambiguity makes it difficult to interpret the results of the experiments and to compare them with other studies. For instance, if a sample is defined as a single data point, then the reported memorization capacity of 3.5-4 bits per parameter seems extremely high, as it would imply that the model is storing complete information about each individual data point. On the other hand, if a sample is defined as a batch of data points, then the reported capacity seems more reasonable, as it would reflect the model's ability to store information about the joint distribution of the batch. The lack of clarity on this point significantly undermines the interpretability of the results.
- The paper does not provide a clear explanation of how the proposed definition of memorization relates to the existing literature on memorization in machine learning. While the authors mention that their definition is inspired by previous work, they do not clearly articulate how their definition differs from and improves upon existing approaches. For example, the paper could benefit from a discussion of how the proposed definition relates to the concept of "information leakage" in neural networks, or how it compares to the notion of " memorization capacity" as defined in other studies. Without a clear comparison to existing literature, it is difficult to assess the novelty and significance of the proposed definition.

### Suggestions

To address the ambiguity surrounding the definition of a "sample," the authors should explicitly define what constitutes a sample in the context of their study. This definition should clearly specify whether a sample refers to a single data point, a batch of data points, or some other unit of data. If the definition is based on a single data point, the authors should provide a justification for why this definition is appropriate and discuss the implications of this choice for the interpretation of their results. For example, they could discuss how the reported memorization capacity of 3.5-4 bits per parameter would translate to the amount of information stored about each individual data point. If the definition is based on a batch of data points, the authors should provide a rationale for this choice and discuss how the reported capacity relates to the model's ability to store information about the joint distribution of the batch. Furthermore, the authors should consider conducting experiments with different definitions of a sample to assess the sensitivity of their results to this choice. This would help to clarify the meaning of the reported memorization capacity and to ensure that the results are robust to different interpretations of the definition.

To clarify the relationship between the proposed definition of memorization and existing literature, the authors should provide a more detailed comparison to relevant works. This comparison should not only highlight the differences between the proposed definition and existing approaches but also discuss the advantages and limitations of each approach. For example, the authors could discuss how their definition relates to the concept of "information leakage" in neural networks, which has been explored in other studies. They could also compare their definition to the notion of "memorization capacity" as defined in other studies, highlighting the similarities and differences between these concepts. This comparison should be supported by a discussion of the theoretical underpinnings of each approach and by a review of the empirical evidence that has been reported in the literature. By providing a more comprehensive comparison to existing literature, the authors can better position their work within the broader context of memorization research and highlight the novelty and significance of their proposed definition.

Finally, the authors should consider providing a more detailed analysis of the experimental results. While the paper presents some interesting findings, it would be beneficial to provide a more in-depth analysis of the factors that influence memorization capacity and membership inference performance. For example, the authors could investigate how the size and complexity of the model, the size and diversity of the dataset, and the choice of training algorithm affect these performance metrics. They could also explore the relationship between memorization and generalization, and discuss the implications of their findings for the design of more robust and reliable machine learning models. By providing a more detailed analysis of the experimental results, the authors can further enhance the impact of their work and provide valuable insights into the behavior of language models.

### Questions

- Could you please clarify what you mean by "sample" in the context of your definition of memorization? Does it refer to a single data point, a batch of data points, or something else entirely?
- How does your proposed definition of memorization relate to existing definitions in the literature? What are the key differences and similarities between your approach and previous work?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

The paper proposes a new definition of memorization that quantifies the amount of information a model stores about a specific data point. The authors use Kolmogorov complexity to define memorization and compression rate to measure it. They estimate Kolmogorov complexity using arithmetic coding and model likelihoods. The paper presents experiments on synthetic and real text datasets to measure memorization capacity and scaling laws for membership inference. The findings suggest that models can memorize up to 3.5-4 bits per parameter and that double descent occurs when models exceed their capacity.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper provides a novel definition of memorization that quantifies the amount of information a model stores about a specific data point. This definition is theoretically grounded and provides a principled way to measure unintended memorization.
- The paper presents a comprehensive analysis of the relationship between model capacity, dataset size, and memorization, offering insights into the behavior of language models.
- The paper provides a detailed analysis of the relationship between model capacity, dataset size, and memorization, offering insights into the behavior of language models.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a clear definition of what constitutes a "sample" in the context of the proposed definition of memorization. It is unclear whether a sample refers to a single data point, a batch of data points, or something else entirely. This ambiguity makes it difficult to interpret the results of the experiments and to compare them with other studies. For instance, if a sample is defined as a single data point, then the reported memorization capacity of 3.5-4 bits per parameter seems extremely high, as it would imply that the model is storing complete information about each individual data point. On the other hand, if a sample is defined as a batch of data points, then the reported capacity seems more reasonable, as it would reflect the model's ability to store information about the joint distribution of the batch. The lack of clarity on this point significantly undermines the interpretability of the results.
- The paper does not provide a clear explanation of how the proposed definition of memorization relates to the existing literature on memorization in machine learning. While the authors mention that their definition is inspired by previous work, they do not clearly articulate how their definition differs from and improves upon existing approaches. For example, the paper could benefit from a discussion of how the proposed definition relates to the concept of "information leakage" in neural networks, or how it compares to the notion of " memorization capacity" as defined in other studies. Without a clear comparison to existing literature, it is difficult to assess the novelty and significance of the proposed definition.

### Suggestions

The authors should provide a precise definition of what constitutes a "sample" within the context of their memorization analysis. This definition should explicitly state whether a sample refers to a single data point, a batch of data points, or some other unit of data. If the definition is based on a single data point, the authors should provide a clear justification for this choice and discuss the implications of this choice for the interpretation of their results. For example, they could discuss how the reported memorization capacity of 3.5-4 bits per parameter would translate to the amount of information stored about each individual data point. If the definition is based on a batch of data points, the authors should provide a rationale for this choice and discuss how the reported capacity relates to the model's ability to store information about the joint distribution of the batch. Furthermore, the authors should consider conducting experiments with different definitions of a sample to assess the sensitivity of their results to this choice. This would help to clarify the meaning of the reported memorization capacity and to ensure that the results are robust to different interpretations of the definition.

To address the lack of clarity regarding the relationship to existing literature, the authors should provide a more detailed comparison of their proposed definition of memorization with existing approaches. This comparison should not only highlight the differences between the proposed definition and existing approaches but also discuss the advantages and limitations of each approach. For example, the authors could discuss how their definition relates to the concept of "information leakage" in neural networks, which has been explored in other studies. They could also compare their definition to the notion of "memorization capacity" as defined in other studies, highlighting the similarities and differences between these concepts. This comparison should be supported by a discussion of the theoretical underpinnings of each approach and by a review of the empirical evidence that has been reported in the literature. By providing a more comprehensive comparison to existing literature, the authors can better position their work within the broader context of memorization research and highlight the novelty and significance of their proposed definition.

Finally, the authors should consider providing a more detailed analysis of the experimental results. While the paper presents some interesting findings, it would be beneficial to provide a more in-depth analysis of the factors that influence memorization capacity and membership inference performance. For example, the authors could investigate how the size and complexity of the model, the size and diversity of the dataset, and the choice of training algorithm affect these performance metrics. They could also explore the relationship between memorization and generalization, and discuss the implications of their findings for the design of more robust and reliable machine learning models. By providing a more detailed analysis of the experimental results, the authors can further enhance the impact of their work and provide valuable insights into the behavior of language models.

### Questions

- Could you please clarify what you mean by "sample" in the context of your definition of memorization? Does it refer to a single data point, a batch of data points, or something else entirely?
- How does your proposed definition of memorization relate to existing definitions in the literature? What are the key differences and similarities between your approach and previous work?

### Rating

6

### Confidence

2

**********

## Reviewer 4

### Summary

This paper proposes a new definition of memorization that quantifies the amount of information a model stores about a specific data point. The authors use Kolmogorov complexity to define memorization and compression rate to measure it. They estimate Kolmogorov complexity using arithmetic coding and model likelihoods. The paper presents experiments on synthetic and real text datasets to measure memorization capacity and scaling laws for membership inference. The findings suggest that models can memorize up to 3.5-4 bits per parameter and that double descent occurs when models exceed their capacity.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper introduces a novel definition of memorization based on Kolmogorov complexity, which provides a theoretical foundation for measuring unintended memorization.
- The authors conduct experiments on both synthetic and real text datasets, demonstrating the applicability of their definition across different types of data.
- The paper provides a comprehensive analysis of the relationship between model capacity, dataset size, and memorization, offering insights into the behavior of language models.

### Weaknesses

#### Some Related Works


#### comment

 - The paper's reliance on Kolmogorov complexity, while theoretically sound, is difficult to compute in practice. The authors use arithmetic coding as an approximation, but the accuracy of this approximation is not thoroughly discussed. The choice of arithmetic coding, while practical, lacks a strong justification compared to other potential compression methods, especially given the existence of more sophisticated lossless compression algorithms that might provide tighter bounds on the Kolmogorov complexity. The paper should include a more detailed analysis of the approximation error introduced by this choice and explore the sensitivity of the results to different compression techniques.
- The experiments are primarily conducted on synthetic data, which may not fully capture the complexities of real-world text. While the authors do include experiments on real text, the analysis of these experiments could be more in-depth. The paper should provide a more detailed analysis of the memorization patterns observed in real-world text, including a discussion of the types of information that are most likely to be memorized and how this varies across different datasets and model architectures. The current analysis lacks a granular view of memorization in real text, focusing more on aggregate metrics.
- The paper does not adequately address the potential impact of different training algorithms and data preprocessing techniques on memorization. The paper should include a more thorough investigation of how different training parameters, such as learning rate, batch size, and regularization techniques, affect the memorization capacity of the models. Additionally, the impact of data preprocessing steps, such as tokenization and normalization, should be explored. The current analysis lacks a systematic study of these factors, which are known to influence model behavior.

### Suggestions

The paper would benefit from a more rigorous justification for the choice of arithmetic coding as an approximation for Kolmogorov complexity. While it is a practical method, the paper should include a discussion of its limitations and potential biases. Specifically, the authors should analyze the approximation error introduced by using arithmetic coding and compare it to other potential compression methods. This could involve exploring alternative compression algorithms, such as those based on context models or adaptive coding schemes, and evaluating their impact on the measured memorization capacity. Furthermore, the paper should investigate the sensitivity of the results to different compression techniques, providing a more robust analysis of the proposed metric. This would strengthen the theoretical foundation of the paper and increase confidence in the reported findings.

To enhance the analysis of real-world text, the paper should delve deeper into the specific memorization patterns observed in different datasets and model architectures. This could involve a more granular analysis of the types of information that are most likely to be memorized, such as specific phrases, entities, or stylistic features. The authors should also explore how these memorization patterns vary across different datasets and model architectures, providing a more comprehensive understanding of the factors that influence memorization in real-world scenarios. This could involve analyzing the attention mechanisms of the models to identify which parts of the input are most influential in the model's predictions, which could help to pinpoint the memorized information. Additionally, the paper should consider using techniques such as saliency maps or feature importance analysis to gain further insights into the memorization patterns.

Finally, the paper should include a more systematic investigation of the impact of different training algorithms and data preprocessing techniques on memorization. This could involve conducting experiments with different learning rates, batch sizes, and regularization techniques, and analyzing their effect on the memorization capacity of the models. The authors should also explore the impact of different data preprocessing steps, such as tokenization, normalization, and filtering, on the measured memorization. This would provide a more comprehensive understanding of the factors that influence memorization and would allow for a more robust comparison of different models and training strategies. The paper should also consider using techniques such as ablation studies to isolate the impact of specific training parameters and data preprocessing steps on memorization.

### Questions

- How sensitive are your results to the choice of compression algorithm? Have you explored other compression methods besides arithmetic coding?
- Can you provide more details on how you estimated the reference model for unintended memorization? How does the choice of reference model affect your results?
- How do you expect your findings to generalize to larger language models and datasets? Are there any limitations to the current experimental setup that might affect the scalability of your results?

### Rating

8

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in a given paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

Here's my plan:
1. **Iterate through each reviewer's comments.**
2. **For each comment identified as a weakness:**
    - **Categorize the weakness:** Is it about the method, experiments, or something else?
    - **Find supporting evidence in the paper:** Look for direct quotes, descriptions of methods or experiments, or missing information.
    - **Analyze the evidence:** Does the evidence directly support the reviewer's claim? Are there any nuances or counterarguments within the paper itself?
    - **Formulate a validation conclusion:** Is the weakness valid, partially valid, or invalid based on the evidence?
    - **Assess confidence:** How confident am I in my assessment based on the strength of the evidence?
**Review 1 Weaknesses:**

1. Weakness Statement:
"The paper does not provide a clear definition of what constitutes a "sample" in the context of the proposed definition of memorization. It is unclear whether a sample refers to a single data point, a batch of data points, or something else entirely. This ambiguity makes it difficult to interpret the results of the experiments and to compare them with other studies. For instance, if a sample is defined as a single data point, then the reported memorization capacity of 3.5-4 bits per parameter seems extremely high, as it would imply that the model is storing complete information about each individual data point. On the other hand, if a sample is defined as a batch of data points, then the reported capacity seems more reasonable, as it would reflect the model's ability to store information about the joint distribution of the batch. The lack of clarity on this point significantly undermines the interpretability of the results."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper introduces the concept of "unintended memorization" and then defines "intended and unintended memorization" in Section 2.2.
   - Definition 5 (Unintended Memorization) refers to a "data sample $\xi$".
   - The paper states in the Introduction: "For example, one recent state-of-the-art model ( Dubey et al., 2024 ) has 8 billion parameters (around 32 KB on disk) but is trained on 15 trillion tokens (around 7 TB on disk)."
   - In the "Measuring Unintended Memorization" experiment setup, it mentions "datasets of varying sizes" and refers to "text sequences" as data points.
   - In the "Disentangling Unintended Memorization from Generalization" experiment setup, it mentions "datasets of varying sizes" and refers to "text sequences" as data points.
   - In the "Scaling Laws for Membership Inference" experiment setup, it mentions "datasets of varying sizes" and refers to "text sequences" as data points.

b) Experiment-related Evidence:
   - The experimental setups consistently refer to "text sequences" as the data being processed by the model.

3. Literature Gap Analysis:
   - The paper does not explicitly define "sample" in the context of its experiments.

4. Validation Analysis:
   - The reviewer correctly points out the ambiguity. While the paper uses terms like "text sequence" and "dataset," it doesn't explicitly define what constitutes a "sample" in the context of its experiments. The experiments measure the amount of information a model knows about a "data sample," but the nature of this "sample" (single data point, batch, etc.) is not clearly stated. This lack of clarity makes it difficult to interpret the reported memorization capacity and compare it with other studies that might use different definitions of "sample."

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper uses the term "data sample" without a clear definition, leading to ambiguity in the interpretation of the results.

1. Weakness Statement:
"The paper does not provide a clear explanation of how the proposed definition of memorization relates to the existing literature on memorization in machine learning. While the authors mention that their definition is inspired by previous work, they do not clearly articulate how their definition differs from and improves upon existing approaches. For example, the paper could benefit from a discussion of how the proposed definition relates to the concept of "information leakage" in neural networks, or how it compares to the notion of " memorization capacity" as defined in other studies. Without a clear comparison to existing literature, it is difficult to assess the novelty and significance of the proposed definition."

2. Evidence Collection:
a) Method-related Evidence:
   - The Introduction mentions: "Most research approaches this problem either through the lens of extraction, aiming to recover full training datapoints from model weights, or membership inference, classifying whether a training point was present in the training data of a given model."
   - The Introduction also states: "These constraints allow us to estimate information content using model likelihoods."
   - Section 2.1 discusses "Memorization, intended and unintended," defining unintended memorization as the information a model retains about a specific dataset.
   - Section 2.2 introduces the concept of "unintended memorization" and defines it using Kolmogorov complexity and compression rate.
   - The Related Work section mentions: "We are the first to measure a clear upper-bound in model capacity using per-sample entropy measurements."

3. Literature Gap Analysis:
   - While the paper mentions related concepts like membership inference and extraction, it doesn't provide a detailed comparison of its definition of memorization with existing definitions in the literature. It doesn't explicitly discuss how its approach relates to or differs from "information leakage" or "memorization capacity" as defined in other works.

4. Validation Analysis:
   - The reviewer's criticism is valid. While the paper introduces a novel definition based on Kolmogorov complexity, it lacks a thorough discussion of how this definition relates to and differs from existing notions of memorization in the literature. The paper mentions related areas but doesn't delve into a comparative analysis. This omission makes it difficult to understand the novelty and significance of the proposed definition within the broader context of memorization research.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks a detailed comparison of its definition of memorization with existing literature, making it difficult to assess its novelty.

**Review 2 Weaknesses:**

1. Weakness Statement:
"The paper's reliance on Kolmogorov complexity, while theoretically sound, is difficult to compute in practice. The authors use arithmetic coding as an approximation, but the accuracy of this approximation is not thoroughly discussed. The choice of arithmetic coding, while practical, lacks a strong justification compared to other potential compression methods, especially given the existence of more sophisticated lossless compression algorithms that might provide tighter bounds on the Kolmogorov complexity. The paper should include a more detailed analysis of the approximation error introduced by this choice and explore the sensitivity of the results to different compression techniques."

2. Evidence Collection:
a) Method-related Evidence:
   - Section 2.2 states: "We adopt arithmetic coding as the most natural compression algorithm for language."
   - The paper acknowledges the theoretical connection to Kolmogorov complexity but uses arithmetic coding as a practical approximation.
   - The paper does not provide a detailed justification for choosing arithmetic coding over other compression methods or an analysis of the approximation error.

b) Experiment-related Evidence:
   - The paper reports specific values for unintended memorization based on the arithmetic coding approximation.

3. Literature Gap Analysis:
   - The paper cites works that use arithmetic coding for similar purposes (e.g., Schwarzchild et al., 2024), but it doesn't provide a comparative analysis of different compression methods in the context of measuring Kolmogorov complexity.

4. Validation Analysis:
   - The reviewer raises a valid concern. The paper uses arithmetic coding as an approximation of Kolmogorov complexity, but it doesn't thoroughly justify this choice or analyze the potential approximation error. Given the existence of other compression algorithms, the reviewer's point about the lack of justification and error analysis is well-founded. This omission weakens the robustness of the proposed metric.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper uses arithmetic coding without a detailed justification or analysis of the approximation error compared to other compression methods.

1. Weakness Statement:
"The experiments are primarily conducted on synthetic data, which may not fully capture the complexities of real-world text. While the authors do include experiments on real text, the analysis of these experiments could be more in-depth. The paper should provide a more detailed analysis of the memorization patterns observed in real-world text, including a discussion of the types of information that are most likely to be memorized and how this varies across different datasets and model architectures. The current analysis lacks a granular view of memorization in real text, focusing more on aggregate metrics."

2. Evidence Collection:
a) Experiment-related Evidence:
   - The "Disentangling Unintended Memorization from Generalization" experiment uses "real text datasets."
   - The "Scaling Laws for Membership Inference" experiment uses "real text datasets."
   - The "results" sections for these experiments provide aggregate metrics like "MemEx score" and "F1 score" but lack a detailed analysis of specific memorization patterns or information types.

3. Literature Gap Analysis:
   - The paper doesn't include a detailed qualitative analysis of memorization patterns in real-world text, comparing them to the findings from synthetic data.

4. Validation Analysis:
   - The reviewer's point is valid. While the paper includes experiments on real text, the analysis focuses on aggregate metrics. A more in-depth analysis of the specific types of information memorized in real-world text, and how this compares to the findings from synthetic data, would strengthen the paper.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The analysis of real text experiments focuses on aggregate metrics, lacking a detailed examination of specific memorization patterns.

1. Weakness Statement:
"The paper does not adequately address the potential impact of different training algorithms and data preprocessing techniques on memorization. The paper should include a more thorough investigation of how different training parameters, such as learning rate, batch size, and regularization techniques, affect the memorization capacity of the models. Additionally, the impact of data preprocessing steps, such as tokenization and normalization, should be explored. The current analysis lacks a systematic study of these factors, which are known to influence model behavior."

2. Evidence Collection:
a) Experiment-related Evidence:
   - The "Model Capacity Estimation" experiment mentions training models with different numbers of layers and hidden dimensions.
   - The "Disentangling Unintended Memorization from Generalization" experiment mentions training on synthetic and real text datasets.
   - The paper does not systematically vary training parameters like learning rate, batch size, or regularization techniques, nor does it explore the impact of different data preprocessing steps.

3. Literature Gap Analysis:
   - The paper doesn't cite or discuss literature that specifically investigates the impact of training algorithms and data preprocessing on unintended memorization.

4. Validation Analysis:
   - The reviewer's criticism is valid. The paper primarily focuses on model architecture and dataset size when measuring memorization capacity. It lacks a systematic investigation into how different training algorithms, data preprocessing techniques, and training parameters influence the measured memorization.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks a systematic study of the impact of training algorithms, data preprocessing, and training parameters on memorization.

**Review 3 Weaknesses:**

1. Weakness Statement:
"The paper does not provide a clear definition of what constitutes a "sample" in the context of the proposed definition of memorization. It is unclear whether a sample refers to a single data point, a batch of data points, or something else entirely. This ambiguity makes it difficult to interpret the results of the experiments and to compare them with other studies. For instance, if a sample is defined as a single data point, then the reported memorization capacity of 3.5-4 bits per parameter seems extremely high, as it would imply that the model is storing complete information about each individual data point. On the other hand, if a sample is defined as a batch of data points, then the reported capacity seems more reasonable, as it would reflect the model's ability to store information about the joint distribution of the batch. The lack of clarity on this point significantly undermines the interpretability of the results."

2. Evidence Collection:
    - This is the same weakness identified by Reviewer 1. Please see the validation for Reviewer 1, Weakness 1.

3. Literature Gap Analysis:
    - Same as Reviewer 1, Weakness 1.

4. Validation Analysis:
    - Same as Reviewer 1, Weakness 1.

5. Conclusion:
    - Validity status: Valid
    - Confidence level: High
    - Key supporting evidence: The paper uses the term "data sample" without a clear definition, leading to ambiguity in the interpretation of the results.

1. Weakness Statement:
"The paper does not provide a clear explanation of how the proposed definition of memorization relates to existing definitions in the literature. While the authors mention that their definition is inspired by previous work, they do not clearly articulate how their definition differs from and improves upon existing approaches. For example, the paper could benefit from a discussion of how the proposed definition relates to the concept of "information leakage" in neural networks, or how it compares to the notion of " memorization capacity" as defined in other studies. Without a clear comparison to existing literature, it is difficult to assess the novelty and significance of the proposed definition."

2. Evidence Collection:
    - This is the same weakness identified by Reviewer 1. Please see the validation for Reviewer 1, Weakness 2.

3. Literature Gap Analysis:
    - Same as Reviewer 1, Weakness 2.

4. Validation Analysis:
    - Same as Reviewer 1, Weakness 2.

5. Conclusion:
    - Validity status: Valid
    - Confidence level: High
    - Key supporting evidence: The paper lacks a detailed comparison of its definition of memorization with existing literature, making it difficult to assess its novelty.

**Review 4 Weaknesses:**

1. Weakness Statement:
"The paper does not provide a clear definition of what constitutes a "sample" in the context of the proposed definition of memorization. It is unclear whether a sample refers to a single data point, a batch of data points, or something else entirely. This ambiguity makes it difficult to interpret the results of the experiments and to compare them with other studies. For instance, if a sample is defined as a single data point, then the reported memorization capacity of 3.5-4 bits per parameter seems extremely high, as it would imply that the model is storing complete information about each individual data point. On the other hand, if a sample is defined as a batch of data points, then the reported capacity seems more reasonable, as it would reflect the model's ability to store information about the joint distribution of the batch. The lack of clarity on this point significantly undermines the interpretability of the results."

2. Evidence Collection:
    - This is the same weakness identified by Reviewer 1 and Reviewer 3. Please see the validation for Reviewer 1, Weakness 1.

3. Literature Gap Analysis:
    - Same as Reviewer 1, Weakness 1.

4. Validation Analysis:
    - Same as Reviewer 1, Weakness 1.

5. Conclusion:
    - Validity status: Valid
    - Confidence level: High
    - Key supporting evidence: The paper uses the term "data sample" without a clear definition, leading to ambiguity in the interpretation of the results.

1. Weakness Statement:
"The paper does not provide a clear explanation of how the proposed definition of memorization relates to existing definitions in the literature. While the authors mention that their definition is inspired by previous work, they do not clearly articulate how their definition differs from and improves upon existing approaches. For example, the paper could benefit from a discussion of how the proposed definition relates to the concept of "information leakage" in neural networks, or how it compares to the notion of " memorization capacity" as defined in other studies. Without a clear comparison to existing literature, it is difficult to assess the novelty and significance of the proposed definition."

2. Evidence Collection:
    - This is the same weakness identified by Reviewer 1 and Reviewer 3. Please see the validation for Reviewer 1, Weakness 2.

3. Literature Gap Analysis:
    - Same as Reviewer 1, Weakness 2.

4. Validation Analysis:
    - Same as Reviewer 1, Weakness 2.

5. Conclusion:
    - Validity status: Valid
    - Confidence level: High
    - Key supporting evidence: The paper lacks a detailed comparison of its definition of memorization with existing literature, making it difficult to assess its novelty.

1. Weakness Statement:
"The paper's reliance on Kolmogorov complexity, while theoretically sound, is difficult to compute in practice. The authors use arithmetic coding as an approximation, but the accuracy of this approximation is not thoroughly discussed. The choice of arithmetic coding, while practical, lacks a strong justification compared to other potential compression methods, especially given the existence of more sophisticated lossless compression algorithms that might provide tighter bounds on the Kolmogorov complexity. The paper should include a more detailed analysis of the approximation error introduced by this choice and explore the sensitivity of the results to different compression techniques."

2. Evidence Collection:
    - This is the same weakness identified by Reviewer 2. Please see the validation for Reviewer 2, Weakness 1.

3. Literature Gap Analysis:
    - Same as Reviewer 2, Weakness 1.

4. Validation Analysis:
    - Same as Reviewer 2, Weakness 1.

5. Conclusion:
    - Validity status: Valid
    - Confidence level: High
    - Key supporting evidence: The paper uses arithmetic coding without a detailed justification or analysis of the approximation error compared to other compression methods.

1. Weakness Statement:
"The experiments are primarily conducted on synthetic data, which may not fully capture the complexities of real-world text. While the authors do include experiments on real text, the analysis of these experiments could be more in-depth. The paper should provide a more detailed analysis of the memorization patterns observed in real-world text, including a discussion of the types of information that are most likely to be memorized and how this varies across different datasets and model architectures. The current analysis lacks a granular view of memorization in real text, focusing more on aggregate metrics."

2. Evidence Collection:
    - This is the same weakness identified by Reviewer 2. Please see the validation for Reviewer 2, Weakness 2.

3. Literature Gap Analysis:
    - Same as Reviewer 2, Weakness 2.

4. Validation Analysis:
    - Same as Reviewer 2, Weakness 2.

5. Conclusion:
    - Validity status: Valid
    - Confidence level: High
    - Key supporting evidence: The analysis of real text experiments focuses on aggregate metrics, lacking a detailed examination of specific memorization patterns.

1. Weakness Statement:
"The paper does not adequately address the potential impact of different training algorithms and data preprocessing techniques on memorization. The paper should include a more thorough investigation of how different training parameters, such as learning rate, batch size, and regularization techniques, affect the memorization capacity of the models. Additionally, the impact of data preprocessing steps, such as tokenization and normalization, should be explored. The current analysis lacks a systematic study of these factors, which are known to influence model behavior."

2. Evidence Collection:
    - This is the same weakness identified by Reviewer 2. Please see the validation for Reviewer 2, Weakness 3.

3. Literature Gap Analysis:
    - Same as Reviewer 2, Weakness 3.

4. Validation Analysis:
    - Same as Reviewer 2, Weakness 3.

5. Conclusion:
    - Validity status: Valid
    - Confidence level: High
    - Key supporting evidence: The paper lacks a systematic study of the impact of training algorithms, data preprocessing, and training parameters on memorization.

**Synthesis and Reflection:**

After analyzing the weaknesses identified by the four reviewers, several recurring themes emerge. All reviewers express concerns about the ambiguity surrounding the definition of a "sample" in the context of the proposed memorization metric. This lack of clarity significantly impacts the interpretability of the results and their comparability with other studies. Reviewers 1, 3, and 4 all highlight this issue, indicating a strong and consistent weakness in the paper.

Another major point of concern is the reliance on Kolmogorov complexity and the use of arithmetic coding as an approximation. Reviewers 1 and 2 specifically point out the lack of justification for this choice and the absence of a thorough error analysis. This raises questions about the accuracy and robustness of the proposed metric.

The experimental analysis is also a point of criticism. Reviewers 2 and 4 note that the experiments on real-world data lack in-depth analysis of memorization patterns, focusing more on aggregate metrics. Reviewer 2 also points out the limited exploration of the impact of training algorithms and data preprocessing.

There are no significant contradictions between the reviewers' opinions. They largely converge on the key areas needing improvement.

**Distinguishing Valid from Invalid Criticisms:**

All the identified weaknesses appear to be **valid**. The reviewers provide specific evidence from the paper to support their claims, pointing to missing definitions, lack of justification for methodological choices, and limitations in the experimental analysis.

**Overall Conclusion:**

The reviewers have identified several valid weaknesses in the paper. The most significant issues are the ambiguity in the definition of "sample," the lack of justification and error analysis for using arithmetic coding as an approximation of Kolmogorov complexity, and the limited depth of analysis in the experiments, particularly regarding real-world data and the impact of training factors. Addressing these weaknesses would significantly strengthen the paper.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces a novel definition of memorization in machine learning models, quantifying the amount of information a model stores about a specific data point. The authors leverage Kolmogorov complexity, approximated using arithmetic coding and model likelihoods, to define and measure unintended memorization. They estimate the capacity of modern language models and analyze the relationship between model capacity, dataset size, and memorization, providing insights into the behavior of these models. The core contribution lies in the theoretical foundation for measuring unintended memorization, which is defined as the information a model retains about a specific dataset. The authors propose a method to disentangle unintended memorization from generalization, and they explore the scaling laws for membership inference. The empirical findings suggest that models can memorize up to 3.5-4 bits per parameter, and that double descent occurs when models exceed their capacity. The paper presents experiments on both synthetic and real text datasets, demonstrating the applicability of their definition across different types of data. The authors also explore the impact of different training algorithms and data preprocessing techniques on memorization, although this aspect is not as thoroughly investigated as the others. Overall, the paper offers a comprehensive analysis of memorization, providing valuable insights into the behavior of language models and their potential for storing unintended information. The authors' approach is theoretically grounded, and their empirical results are compelling, although there are some limitations that need to be addressed to further strengthen the paper's conclusions.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

3.0


## Strengths:

I find several aspects of this paper to be particularly strong. First, the introduction of a novel definition of memorization based on Kolmogorov complexity is a significant contribution. This definition provides a theoretical foundation for measuring unintended memorization, which is a crucial aspect of understanding how language models learn and generalize. The authors' approach of using arithmetic coding as an approximation of Kolmogorov complexity is a practical way to estimate this theoretical concept, and it allows for empirical analysis of memorization in language models. The paper's comprehensive analysis of the relationship between model capacity, dataset size, and memorization is another strength. The authors provide a detailed analysis of how these factors influence the amount of information a model stores about a specific data point, offering valuable insights into the behavior of language models. The experiments on both synthetic and real text datasets are well-designed and demonstrate the applicability of the proposed definition across different types of data. The paper also provides a clear and concise explanation of the proposed definition of memorization, making it accessible to a broad audience. The authors' exploration of the scaling laws for membership inference is another notable contribution, providing a deeper understanding of the factors that influence memorization. Finally, the paper is well-written and easy to follow, making it a pleasure to read and understand. The authors have successfully presented a complex topic in a clear and engaging manner, which is a testament to their writing skills.


## Weaknesses:

Despite the strengths of this paper, I have identified several weaknesses that warrant careful consideration. The most significant issue is the lack of a clear definition of what constitutes a "sample" within the context of the proposed definition of memorization. The paper uses the term "data sample" without explicitly stating whether it refers to a single data point, a batch of data points, or some other unit of data. This ambiguity makes it difficult to interpret the reported memorization capacity of 3.5-4 bits per parameter. For example, if a sample is defined as a single data point, the reported capacity seems extremely high, as it would imply that the model is storing complete information about each individual data point. Conversely, if a sample is defined as a batch of data points, the reported capacity seems more reasonable. This lack of clarity undermines the interpretability of the results and makes it difficult to compare them with other studies that might use different definitions of "sample." My confidence in this weakness is high, as it is directly observable from the paper's text and is a fundamental issue that affects the entire analysis. 

Another significant weakness is the lack of a thorough comparison of the proposed definition of memorization with existing literature. While the authors mention that their definition is inspired by previous work, they do not clearly articulate how their definition differs from and improves upon existing approaches. For instance, the paper could benefit from a discussion of how the proposed definition relates to the concept of "information leakage" in neural networks, or how it compares to the notion of "memorization capacity" as defined in other studies. Without a clear comparison to existing literature, it is difficult to assess the novelty and significance of the proposed definition. This omission makes it challenging to position the work within the broader context of memorization research and to understand its unique contributions. My confidence in this weakness is also high, as it is a clear gap in the paper's discussion of related work. 

Furthermore, the paper's reliance on Kolmogorov complexity, while theoretically sound, is difficult to compute in practice. The authors use arithmetic coding as an approximation, but the accuracy of this approximation is not thoroughly discussed. The choice of arithmetic coding, while practical, lacks a strong justification compared to other potential compression methods, especially given the existence of more sophisticated lossless compression algorithms that might provide tighter bounds on the Kolmogorov complexity. The paper should include a more detailed analysis of the approximation error introduced by using arithmetic coding and explore the sensitivity of the results to different compression techniques. This omission weakens the robustness of the proposed metric and raises questions about the reliability of the reported memorization capacity. My confidence in this weakness is high, as it is a clear methodological limitation that is not adequately addressed in the paper. 

Additionally, the experiments are primarily conducted on synthetic data, which may not fully capture the complexities of real-world text. While the authors do include experiments on real text, the analysis of these experiments could be more in-depth. The paper should provide a more detailed analysis of the memorization patterns observed in real-world text, including a discussion of the types of information that are most likely to be memorized and how this varies across different datasets and model architectures. The current analysis lacks a granular view of memorization in real text, focusing more on aggregate metrics. This limitation makes it difficult to assess the generalizability of the findings to real-world scenarios. My confidence in this weakness is high, as it is a clear limitation in the experimental design. 

Finally, the paper does not adequately address the potential impact of different training algorithms and data preprocessing techniques on memorization. The paper should include a more thorough investigation of how different training parameters, such as learning rate, batch size, and regularization techniques, affect the memorization capacity of the models. Additionally, the impact of data preprocessing steps, such as tokenization and normalization, should be explored. The current analysis lacks a systematic study of these factors, which are known to influence model behavior. This omission limits the paper's ability to provide a comprehensive understanding of the factors that influence memorization. My confidence in this weakness is high, as it is a clear gap in the experimental analysis.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First and foremost, the authors should provide a precise definition of what constitutes a "sample" within the context of their study. This definition should clearly specify whether a sample refers to a single data point, a batch of data points, or some other unit of data. If the definition is based on a single data point, the authors should provide a justification for why this definition is appropriate and discuss the implications of this choice for the interpretation of their results. For example, they could discuss how the reported memorization capacity of 3.5-4 bits per parameter would translate to the amount of information stored about each individual data point. If the definition is based on a batch of data points, the authors should provide a rationale for this choice and discuss how the reported capacity relates to the model's ability to store information about the joint distribution of the batch. Furthermore, the authors should consider conducting experiments with different definitions of a sample to assess the sensitivity of their results to this choice. This would help to clarify the meaning of the reported memorization capacity and to ensure that the results are robust to different interpretations of the definition. 

Second, the authors should provide a more detailed comparison of their proposed definition of memorization with existing approaches. This comparison should not only highlight the differences between the proposed approach and existing approaches but also discuss the advantages and limitations of each approach. For example, the authors could discuss how their definition relates to the concept of "information leakage" in neural networks, which has been explored in other studies. They could also compare their definition to the notion of "memorization capacity" as defined in other studies, highlighting the similarities and differences between these concepts. This comparison should be supported by a discussion of the theoretical underpinnings of each approach and by a review of the empirical evidence that has been reported in the literature. By providing a more comprehensive comparison to existing literature, the authors can better position their work within the broader context of memorization research and highlight the novelty and significance of their proposed definition. 

Third, the authors should provide a more detailed analysis of the approximation error introduced by using arithmetic coding as an approximation for Kolmogorov complexity. This analysis should include a comparison of the compression rates obtained using different algorithms and a discussion of how these differences might affect the measured memorization capacity. Furthermore, the authors should investigate the sensitivity of their results to variations in the compression algorithm, which would provide a more robust assessment of the proposed metric. This could involve experimenting with different compression methods and analyzing the resulting changes in the measured memorization capacity. 

Fourth, to strengthen the analysis of real-world text, the authors should provide a more granular view of memorization patterns. This could involve a more detailed analysis of the types of information that are most likely to be memorized, such as specific phrases, entities, or stylistic features. The authors should also explore how these memorization patterns vary across different datasets and model architectures. For example, do models trained on different datasets exhibit different memorization behaviors? Are certain model architectures more prone to memorizing specific types of information? A more detailed analysis of these questions would provide a more comprehensive understanding of memorization in real-world scenarios. The authors could also consider using techniques such as attention visualization to gain insights into which parts of the input are most influential in the model's predictions, which could help to pinpoint the memorized information. 

Finally, the paper should include a more thorough investigation of the impact of different training algorithms and data preprocessing techniques on memorization. This should include a systematic study of how different training parameters, such as learning rate, batch size, and regularization techniques, affect the memorization capacity of the models. The authors should also explore the impact of different data preprocessing steps, such as tokenization, normalization, and filtering, on memorization. This would provide a more comprehensive understanding of the factors that influence memorization and would allow for a more robust comparison of different models and training strategies. By addressing these weaknesses, the authors can significantly strengthen the paper and enhance its impact on the field of memorization research.


## Questions:

I have several questions that arise from my analysis of the paper. First, how sensitive are the results to the choice of compression algorithm? Have the authors explored other compression methods besides arithmetic coding, and if so, how do these methods compare in terms of the measured memorization capacity? This question is crucial because the choice of compression algorithm can significantly impact the measured memorization capacity, and a more thorough analysis of this aspect would strengthen the paper's findings. Second, can the authors provide more details on how they estimated the reference model for unintended memorization? How does the choice of reference model affect the results, and what are the limitations of the current approach? This question is important because the choice of reference model can significantly influence the measured memorization capacity, and a more detailed discussion of this aspect would enhance the paper's analysis. Third, how do the authors expect their findings to generalize to larger language models and datasets? Are there any limitations to the current experimental setup that might affect the scalability of their results? This question is important because the paper's findings are based on relatively small models and datasets, and it is unclear how well these results would generalize to larger models and datasets. Finally, how do the authors expect their findings to generalize to larger language models and datasets? Are there any limitations to the current experimental setup that might affect the scalability of their results? This question is important because the paper's findings are based on relatively small models and datasets, and it is unclear how well these results would generalize to larger models and datasets. Addressing these questions would provide a more comprehensive understanding of the paper's findings and their implications for the field of memorization research.


## Rating:

6.5


## Confidence:

3.0


## Decision:

Accept
}