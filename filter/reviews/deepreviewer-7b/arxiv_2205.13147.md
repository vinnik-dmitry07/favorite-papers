I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

The paper introduces Matryoshka Representation Learning (MRL), a method that allows for learning representations at different granularities within a single high-dimensional vector. This is achieved by optimizing the original representation vector to produce multiple, progressively smaller vectors, each capable of addressing tasks with varying computational resources. The authors demonstrate the effectiveness of MRL in large-scale classification and retrieval tasks, showing improvements in efficiency and accuracy, especially in resource-constrained environments.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-structured and easy to follow.
- The experiments are thorough, covering multiple tasks and datasets.

### Weaknesses

#### Some Related Works


#### comment

 - The motivation for this work is not clearly articulated. The paper does not adequately explain why a single high-dimensional vector cannot be optimized to produce multiple, progressively smaller vectors, each capable of addressing tasks with varying computational resources. The authors should provide a more detailed explanation of the limitations of existing methods and how MRL overcomes these limitations. Specifically, the paper lacks a clear discussion on the computational cost of training multiple smaller models versus training a single larger model and then performing some form of dimensionality reduction or pruning. A more rigorous comparison of the computational overhead and performance trade-offs is needed.
- The paper does not sufficiently explain why the proposed method is effective. The authors should provide a more detailed analysis of the underlying mechanisms that enable MRL to achieve its results. For example, how does the optimization process ensure that the different granularity representations capture the necessary information? What are the theoretical guarantees or empirical observations that support the claim that MRL can achieve coarse-to-fine representations? The paper would benefit from a more in-depth analysis of the learned representations, perhaps through visualization or probing techniques, to understand how the different granularity representations are related and what information they encode.
- The paper does not discuss the limitations of the proposed method. It is important to acknowledge the potential drawbacks and scenarios where MRL might not perform optimally. For instance, how does the method handle tasks where the optimal representation granularity is not well-defined or varies significantly across different data points? What are the potential failure modes of MRL, and how can these be mitigated? A discussion of the sensitivity of the method to hyperparameter choices and the potential impact of these choices on the final performance is also missing.

### Suggestions

The paper should begin by clearly articulating the specific scenarios where existing representation learning methods fall short, particularly in terms of computational efficiency and adaptability to varying resource constraints. It needs to be explicitly stated why a single high-dimensional vector is insufficient for these scenarios and what the limitations of existing methods are. For example, the authors could discuss the trade-offs between training multiple smaller models and fine-tuning a larger model, highlighting the computational costs and performance implications of each approach. This would provide a strong motivation for the proposed MRL method. Furthermore, the paper should include a more detailed analysis of the computational complexity of MRL compared to existing methods, including both training and inference costs. This analysis should consider the number of parameters, the number of optimization steps, and the computational cost of the projection operations. A clear understanding of these trade-offs is crucial for evaluating the practical applicability of MRL.

To strengthen the explanation of why MRL is effective, the paper should delve deeper into the optimization process and the properties of the learned representations. It should provide a more detailed analysis of how the optimization process ensures that the different granularity representations capture the necessary information. For example, the authors could analyze the gradients during training to understand how the different granularity representations are learned and how they relate to each other. Furthermore, the paper should include a more in-depth analysis of the learned representations, perhaps through visualization or probing techniques, to understand how the different granularity representations are related and what information they encode. This could involve techniques such as t-SNE or UMAP to visualize the representation space, or by probing the representations with simple classifiers to understand what information is captured at each granularity. The paper should also discuss the theoretical underpinnings of MRL, providing insights into why the proposed approach is expected to work and what its limitations are.

Finally, the paper should include a more thorough discussion of the limitations of MRL. This should include a discussion of scenarios where MRL might not perform optimally, such as tasks where the optimal representation granularity is not well-defined or varies significantly across different data points. The authors should also discuss the potential failure modes of MRL and how these can be mitigated. For example, the paper could explore the sensitivity of the method to hyperparameter choices and the potential impact of these choices on the final performance. It would also be beneficial to discuss the computational overhead of MRL, particularly the cost of the projection operations, and how this overhead scales with the number of granularities. A more comprehensive discussion of these limitations would provide a more balanced and realistic assessment of the proposed method.

### Questions

- How does the proposed method compare to other approaches that learn multiple representations for different computational resources? A detailed comparison would help to clarify the novelty and advantages of MRL.
- What are the limitations of the proposed method? How does MRL perform in scenarios where the optimal representation granularity is not well-defined or varies significantly across different data points?

### Rating

6

### Confidence

3

**********

## Reviewer 2

### Summary

This paper proposes a method to learn a Matryoshka ​ Representation, which is a vector of dimensionality d, where the first m components of the vector are an information-rich low-dimensional vector, at no additional cost during inference. The authors propose to learn coarse-to-fine representations that are at least as accurate and rich as independently trained low-dimensional representations. The flexibility within the learned Matryoshka ​ Representations offers: (a) up to 14 × smaller embedding size for ImageNet-1K classification at the same level of accuracy; (b) up to 14 × real-world speed-ups for large-scale retrieval on ImageNet-1K and 4K; and (c) up to 2 % accuracy improvements for long-tail few-shot classification, all while being as robust as the original representations.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

The paper is well-written and easy to follow. The experiments are comprehensive and demonstrate the effectiveness of the proposed method. The authors also provide code and pretrained models to facilitate further research.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method requires training multiple low-dimensional models, which could be computationally expensive. While the authors mention that the additional cost is minimal, a more detailed analysis of the computational overhead, including training time and memory usage, would be beneficial. Specifically, the paper should quantify the increase in training time and memory consumption compared to training a single model of the same final dimensionality. It is also unclear how the number of intermediate dimensions (m) affects the overall training cost and the final performance. A more thorough investigation into the trade-offs between the number of intermediate dimensions, training cost, and performance is needed.

2. The paper does not provide a clear explanation of how the proposed method can be applied to different modalities, such as text and video. The authors mention that the method can be adapted to other modalities, but they do not provide specific details on how this would be achieved. For example, how would the method be applied to text embeddings, and how would the coarse-to-fine representations be learned for video data? A more detailed explanation of the adaptation process for different modalities is necessary to demonstrate the generalizability of the proposed method. The paper should also discuss the potential challenges and limitations of applying the method to different modalities.

3. The paper does not discuss the potential limitations of the proposed method, such as its sensitivity to hyperparameters or its performance on different types of data. A more comprehensive discussion of the limitations of the proposed method is needed to provide a balanced view of its strengths and weaknesses. For example, the paper should discuss how the performance of the method varies with different datasets, different architectures, and different hyperparameter settings. It should also discuss the potential limitations of the method, such as its sensitivity to the choice of the intermediate dimensions (m) and its performance on noisy or adversarial data.

### Suggestions

The paper would benefit from a more detailed analysis of the computational cost associated with the proposed method. The authors should provide a breakdown of the training time and memory usage for each stage of the training process, including the training of the low-dimensional models and the optimization of the coarse-to-fine representations. This analysis should also include a comparison of the computational cost of the proposed method with the cost of training a single model of the same final dimensionality. Furthermore, the authors should investigate the impact of the number of intermediate dimensions (m) on the overall training cost and the final performance. This analysis should include a sensitivity study to determine the optimal number of intermediate dimensions for different datasets and architectures. The authors should also discuss the potential trade-offs between the number of intermediate dimensions, training cost, and performance, and provide guidelines for selecting the appropriate number of intermediate dimensions for different applications.

To address the lack of clarity regarding the applicability of the proposed method to different modalities, the authors should provide a more detailed explanation of how the method can be adapted to text and video data. For text data, the authors should discuss how the coarse-to-fine representations can be learned from text embeddings, and how the method can be used for tasks such as text classification or text retrieval. For video data, the authors should discuss how the method can be applied to video embeddings, and how the coarse-to-fine representations can be learned for video classification or video retrieval. The authors should also discuss the potential challenges and limitations of applying the method to different modalities, such as the need for modality-specific feature extraction and the potential for modality-specific performance variations. A more detailed explanation of the adaptation process for different modalities is necessary to demonstrate the generalizability of the proposed method.

Finally, the paper should include a more comprehensive discussion of the limitations of the proposed method. The authors should discuss how the performance of the method varies with different datasets, different architectures, and different hyperparameter settings. This discussion should include a sensitivity analysis to determine the robustness of the method to different hyperparameter settings. The authors should also discuss the potential limitations of the method, such as its sensitivity to the choice of the intermediate dimensions (m) and its performance on noisy or adversarial data. The paper should also discuss the potential limitations of the method, such as its sensitivity to the choice of the intermediate dimensions (m) and its performance on noisy or adversarial data. A more balanced view of the strengths and weaknesses of the proposed method is needed to provide a complete understanding of its applicability and limitations.

### Questions

1. How does the proposed method compare to other approaches that learn multiple representations for different computational resources? A detailed comparison would help to clarify the novelty and advantages of MRL.

2. What are the potential limitations of the proposed method, such as its sensitivity to hyperparameters or its performance on different types of data?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper introduces a novel method called Matryoshka Representation Learning (MRL), which aims to address the challenge of deploying deep learning models with varying computational resources. The core idea is to learn a representation vector that can be used at different granularities, allowing for adaptive deployment based on available resources. The authors demonstrate the effectiveness of MRL in large-scale classification and retrieval tasks, showing improvements in efficiency and accuracy compared to traditional methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow, with clear explanations of the proposed method and its applications.
2. The authors provide extensive experimental results on various datasets, including ImageNet-1K, JFT-300M, and ALIGN data, demonstrating the effectiveness of MRL in large-scale classification and retrieval tasks.
3. The paper includes a comprehensive ablation study, which helps to understand the impact of different design choices on the performance of MRL.
4. The authors provide code and pretrained models, which will facilitate further research and adoption of MRL.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of MRL, especially in terms of training and inference time. While the authors mention that MRL can reduce the computational cost of inference, they do not provide a quantitative comparison with other methods. Specifically, the paper lacks a breakdown of the time spent on different stages of the MRL process, such as the initial training of the full-dimensional representation and the subsequent projection to lower dimensions. This makes it difficult to assess the practical benefits of MRL in resource-constrained environments.
2. The paper does not provide a detailed analysis of the memory usage of MRL, especially in terms of storage and computation. While the authors claim that MRL can reduce the memory usage of representations, they do not provide a quantitative comparison with other methods. The paper should include a discussion of the memory footprint of the learned representation at different granularities, as well as the memory required for the projection matrices. This is crucial for understanding the scalability of MRL to very large models and datasets.
3. The paper does not provide a detailed analysis of the robustness of MRL to adversarial attacks. While the authors claim that MRL can improve the robustness of representations, they do not provide any experimental results to support this claim. The paper should include a quantitative evaluation of the robustness of MRL to adversarial perturbations, as well as a discussion of the potential vulnerabilities of the method. This is important for ensuring the reliability of MRL in real-world applications.

### Suggestions

The paper would benefit from a more thorough analysis of the computational and memory costs associated with MRL. Specifically, the authors should provide a detailed breakdown of the training time, including the time required to train the full-dimensional representation and the time required to train the projection matrices. This should be compared against the training time of other methods, such as training separate models for different granularities. Furthermore, the paper should include a detailed analysis of the inference time, including the time required to project the representation to different granularities. This should be compared against the inference time of other methods, such as using a single model with a fixed granularity. The authors should also provide a detailed analysis of the memory usage of MRL, including the memory required to store the representation at different granularities and the memory required to store the projection matrices. This should be compared against the memory usage of other methods, such as storing multiple models for different granularities. These analyses should be conducted on a variety of hardware platforms to ensure the results are generalizable.

To address the lack of robustness analysis, the authors should conduct a series of experiments to evaluate the performance of MRL under adversarial attacks. This should include a quantitative evaluation of the robustness of MRL to different types of adversarial perturbations, such as small perturbations, large perturbations, and targeted attacks. The authors should also discuss the potential vulnerabilities of MRL to adversarial attacks and propose methods to mitigate these vulnerabilities. This analysis should be conducted on a variety of datasets and model architectures to ensure the results are generalizable. The authors should also consider using adversarial training techniques to improve the robustness of MRL.

Finally, the paper should include a more detailed discussion of the limitations of MRL. This should include a discussion of the scenarios where MRL may not be effective, such as when the optimal granularity is not well-defined or when the data distribution is highly complex. The authors should also discuss the potential impact of the choice of the granularity on the performance of MRL. This discussion should be supported by experimental results and should provide guidance on how to choose the optimal granularity for different applications. The authors should also discuss the potential impact of the choice of the granularity on the performance of MRL. This discussion should be supported by experimental results and should provide guidance on how to choose the optimal granularity for different applications.

### Questions

1. How does MRL compare to other methods in terms of computational cost and memory usage? Can you provide a quantitative comparison with other methods?
2. How robust is MRL to adversarial attacks? Can you provide any experimental results to support this claim?
3. Can you provide a more detailed discussion of the limitations of MRL? Are there any scenarios where MRL may not be effective?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

This paper introduces Matryoshka Representation Learning (MRL), a method that enables the learning of representations of varying capacities within the same high-dimensional vector. The authors propose a novel approach to achieve this by optimizing multiple nested dimensions of the representation, which allows for adaptive deployment based on computational constraints. The paper demonstrates the effectiveness of MRL in large-scale classification and retrieval tasks, showing improvements in efficiency and accuracy compared to traditional methods. The authors also provide a comprehensive evaluation of MRL across various benchmarks, including ImageNet-1K, JFT-300M, and ALIGN data, and discuss its potential applications in web-scale datasets and multi-modal learning.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow, with clear explanations of the proposed method and its applications.
2. The authors provide extensive experimental results on various datasets, including ImageNet-1K, JFT-300M, and ALIGN data, demonstrating the effectiveness of MRL in large-scale classification and retrieval tasks.
3. The paper includes a comprehensive ablation study, which helps to understand the impact of different design choices on the performance of MRL.
4. The authors provide code and pretrained models, which will facilitate further research and adoption of MRL.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of MRL, especially in terms of training and inference time. While the authors mention that MRL can reduce the computational cost of inference, they do not provide a quantitative comparison with other methods. Specifically, the paper lacks a breakdown of the time spent on different stages of the MRL process, such as the initial training of the full-dimensional representation and the subsequent projection to lower dimensions. This makes it difficult to assess the practical benefits of MRL in resource-constrained environments.
2. The paper does not provide a detailed analysis of the memory usage of MRL, especially in terms of storage and computation. While the authors claim that MRL can reduce the memory usage of representations, they do not provide a quantitative comparison with other methods. The paper should include a discussion of the memory footprint of the learned representation at different granularities, as well as the memory required for the projection matrices. This is crucial for understanding the scalability of MRL to very large models and datasets.
3. The paper does not provide a detailed analysis of the robustness of MRL to adversarial attacks. While the authors claim that MRL can improve the robustness of representations, they do not provide any experimental results to support this claim. The paper should include a quantitative evaluation of the robustness of MRL to adversarial perturbations, as well as a discussion of the potential vulnerabilities of the method. This is important for ensuring the reliability of MRL in real-world applications.

### Suggestions

The paper would benefit from a more thorough analysis of the computational and memory costs associated with MRL. Specifically, the authors should provide a detailed breakdown of the training time, including the time required to train the full-dimensional representation and the time required to train the projection matrices. This should be compared against the training time of other methods, such as training separate models for different granularities. Furthermore, the paper should include a detailed analysis of the inference time, including the time required to project the representation to different granularities. This should be compared against the inference time of other methods, such as using a single model with a fixed granularity. The authors should also provide a detailed analysis of the memory usage of MRL, including the memory required to store the representation at different granularities and the memory required to store the projection matrices. This should be compared against the memory usage of other methods, such as storing multiple models for different granularities. These analyses should be conducted on a variety of hardware platforms to ensure the results are generalizable.

To address the lack of robustness analysis, the authors should conduct a series of experiments to evaluate the performance of MRL under adversarial attacks. This should include a quantitative evaluation of the robustness of MRL to different types of adversarial perturbations, such as small perturbations, large perturbations, and targeted attacks. The authors should also discuss the potential vulnerabilities of MRL to adversarial attacks and propose methods to mitigate these vulnerabilities. This analysis should be conducted on a variety of datasets and model architectures to ensure the results are generalizable. The authors should also consider using adversarial training techniques to improve the robustness of MRL.

Finally, the paper should include a more detailed discussion of the limitations of MRL. This should include a discussion of the scenarios where MRL may not be effective, such as when the optimal granularity is not well-defined or when the data distribution is highly complex. The authors should also discuss the potential impact of the choice of the granularity on the performance of MRL. This discussion should be supported by experimental results and should provide guidance on how to choose the optimal granularity for different applications. The authors should also discuss the potential impact of the choice of the granularity on the performance of MRL. This discussion should be supported by experimental results and should provide guidance on how to choose the optimal granularity for different applications.

### Questions

1. How does MRL compare to other methods in terms of computational cost and memory usage? Can you provide a quantitative comparison with other methods?
2. How robust is MRL to adversarial attacks? Can you provide any experimental results to support this claim?
3. Can you provide a more detailed discussion of the limitations of MRL? Are there any scenarios where MRL may not be effective?

### Rating

8

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in a given paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

Plan:
1. Read each reviewer's weakness.
2. Find the corresponding section in the paper.
3. Look for evidence (quotes, numbers, missing information) to support the weakness.
4. If the weakness is about missing information, check if the information is indeed absent.
5. If the weakness is about a claim, check if the claim is supported by evidence in the paper.
6. If there are conflicting opinions, address them in the synthesis.
**Review 1 Weaknesses:**

1. Weakness Statement:
[The paper does not provide a detailed analysis of the computational cost of MRL, especially in terms of training and inference time. While the authors mention that MRL can reduce the computational cost of inference, they do not provide a quantitative comparison with other methods. Specifically, the paper lacks a breakdown of the time spent on different stages of the MRL process, such as the initial training of the full-dimensional representation and the subsequent projection to lower dimensions. This makes it difficult to assess the practical benefits of MRL in resource-constrained environments.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions the efficiency of MRL in the abstract: "MRL enables models to adapt to multiple downstream tasks with varying computational resources by learning coarse-to-fine representations, which are at least as accurate and rich as independently trained low-dimensional representations. The flexibility within the learned Matryoshka ​ Representations offers: (a) up to 14 × smaller embedding size for ImageNet-1K classification at the same accuracy; (b) up to 14 × real-world speed-ups for large-scale retrieval on ImageNet-1K and 4K; and (c) up to 2 % accuracy improvements for long-tail few-shot classification, all while being as robust as the original representations."
   - The introduction states: "By encoding coarse-to-fine-grained representations, which are as accurate as the independently trained counterparts, we learn with minimal overhead a representation that can be deployed adaptively at no additional cost during inference."
   - The main idea section claims: "This approach not only reduces the average dimension of the representations but also maintains or improves the accuracy compared to independently trained low-dimensional models."
   - The method overview states: "MRL learns representations of varying capacities within the same high-dimensional vector through explicit optimization of O(log(d)) nested dimensions. This allows the model to adapt to different downstream tasks and computational constraints without any additional cost during inference."
b) Experiment-related Evidence:
   - The "Classification" experiment section mentions: "The models are trained using a standard cross-entropy loss function. The training process involves optimizing the multi-class classification loss for each nested dimension." However, it does not provide specific training times.
   - The "Retrieval" experiment section mentions: "The models are trained using a standard cross-entropy loss function. The training process involves optimizing the multi-class classification loss for each nested dimension." Again, no specific training times are provided.
   - The "Retrieval" experiment also mentions: "The retrieval performance is evaluated using mean Average Precision (mAP@ 10) and retrieval time." and "The retrieval performance is evaluated using mean Average Precision (mAP@ 10) and retrieval time." but no inference time comparisons are made.

3. Literature Gap Analysis:
   - The paper does not explicitly compare the training time or inference time of MRL with other representation learning methods in the experimental section.

4. Validation Analysis:
   - The paper claims efficiency and reduced computational cost, but it lacks quantitative data to support these claims. While the abstract mentions speed-ups, the experimental sections focus on accuracy metrics and do not provide detailed timing information for training or inference. The reviewer's point about the lack of a breakdown of training time for different stages is valid as the paper doesn't detail the process.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of explicit training and inference time comparisons in the experimental sections, despite claims of efficiency.

1. Weakness Statement:
[The paper does not provide a detailed analysis of the memory usage of MRL, especially in terms of storage and computation. While the authors claim that MRL can reduce the memory usage of representations, they do not provide a quantitative comparison with other methods. The paper should include a discussion of the memory footprint of the learned representation at different granularities, as well as the memory required for the projection matrices. This is crucial for understanding the scalability of MRL to very large models and datasets.]

2. Evidence Collection:
a) Method-related Evidence:
   - The paper mentions the reduction in embedding size in the abstract and main idea sections.
   - The method overview states: "This approach not only reduces the average dimension of the representations but also maintains or improves the accuracy compared to independently trained low-dimensional models."
b) Experiment-related Evidence:
   - The "Classification" experiment section mentions: "The models are trained using a standard cross-entropy loss function. The training process involves optimizing the multi-class classification loss for each nested dimension." It does not discuss memory usage.
   - The "Retrieval" experiment section mentions: "The models are trained using a standard cross-entropy loss function. The training process involves optimizing the multi-class classification loss for each nested dimension." Again, no memory usage information is provided.
   - The "Retrieval" experiment also mentions: "The retrieval performance is evaluated using mean Average Precision (mAP@ 10) and retrieval time." and "The retrieval performance is evaluated using mean Average Precision (mAP@ 10) and retrieval time." but no memory usage comparisons are made.

3. Literature Gap Analysis:
   - The paper does not include a quantitative comparison of memory usage with other methods.

4. Validation Analysis:
   - Similar to the computational cost, the paper claims memory reduction but lacks quantitative evidence. The reviewer correctly points out the absence of a discussion on the memory footprint of the learned representations and projection matrices.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of memory usage data and comparisons in the experimental sections, despite claims of reduced memory footprint.

1. Weakness Statement:
[The paper does not provide a detailed analysis of the robustness of MRL to adversarial attacks. While the authors claim that MRL can improve the robustness of representations, they do not provide any experimental results to support this claim. The paper should include a quantitative evaluation of the robustness of MRL to adversarial perturbations, as well as a discussion of the potential vulnerabilities of the method. This is important for ensuring the reliability of MRL in real-world applications.]

2. Evidence Collection:
a) Method-related Evidence:
   - The abstract mentions: "MRL enables models to adapt to multiple downstream tasks with varying computational resources by learning coarse-to-fine representations, which are at least as accurate and rich as independently trained low-dimensional representations. The flexibility within the learned Matryoshka ​ Representations offers: (a) up to 14 × smaller embedding size for ImageNet-1K classification at the same accuracy; (b) up to 14 × real-world speed-ups for large-scale retrieval on ImageNet-1K and 4K; and (c) up to 2 % accuracy improvements for long-tail few-shot classification, all while being as robust as the original representations."
   - The introduction states: "The flexibility within the learned Matryoshka ​ Representations offers: (a) up to 14 × smaller embedding size for ImageNet-1K classification at the same accuracy; (b) up to 14 × real-world speed-ups for large-scale retrieval on ImageNet-1K and 4K; and (c) up to 2 % accuracy improvements for long-tail few-shot classification, all while being as robust as the original representations."
   - The main idea section claims: "This approach not only reduces the average dimension of the representations but also maintains or improves the accuracy compared to independently trained low-dimensional models."
b) Experiment-related Evidence:
   - The "Classification" experiment section evaluates robustness against standard adversarial attacks (FGSM, PGD) on ImageNet-1K.
   - The "Retrieval" experiment section also evaluates robustness against standard adversarial attacks (FGSM, PGD) on ImageNet-1K.
   - The "Long-tail and few-shot Learning" section evaluates robustness against standard adversarial attacks (FGSM, PGD) on ImageNet-1K.
   - The paper does not explicitly discuss or evaluate robustness against adversarial attacks in the context of the Matryoshka representation itself, but it does evaluate the robustness of the downstream tasks.

3. Literature Gap Analysis:
   - While the paper evaluates robustness of the downstream tasks, it doesn't explicitly analyze the robustness of the learned Matryoshka representation against adversarial attacks.

4. Validation Analysis:
   - The reviewer's point is partially valid. The paper *does* evaluate the robustness of the models trained with MRL against adversarial attacks. However, the reviewer is correct that the paper doesn't explicitly analyze the robustness of the *Matryoshka representation* itself against adversarial attacks. The paper claims robustness, and the experiments show that the downstream tasks are robust, but the internal representation's robustness isn't directly tested.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: Experiments evaluate robustness of downstream tasks, but there's no specific analysis of the robustness of the Matryoshka representation against adversarial attacks.

**Review 2 Weaknesses:**

1. Weakness Statement:
[The motivation for this work is not clearly articulated. The paper does not adequately explain why a single high-dimensional vector cannot be optimized to produce multiple, progressively smaller vectors, each capable of addressing tasks with varying computational resources. The authors should provide a more detailed explanation of the limitations of existing methods and how MRL overcomes these limitations. Specifically, the paper lacks a clear discussion on the computational cost of training multiple smaller models versus training a single larger model and then performing some form of dimensionality reduction or pruning. A more rigorous comparison of the computational overhead and performance trade-offs is needed.]

2. Evidence Collection:
a) Method-related Evidence:
   - The introduction states: "However, the rigidity in these representations forces the use of high-dimensional embedding vectors across multiple tasks despite the varying resource and accuracy constraints that require flexibility."
   - The introduction also mentions: "The need for a flexible representation learning approach that can adapt to different computational resources is evident, as current methods either sacrifice accuracy or increase computational overhead."
   - The motivation section elaborates on the limitations of fixed and fixed feature selection methods and the need for a flexible approach.
b) Experiment-related Evidence:
   - The paper compares MRL with "FF" (fixed feature) and "slimmable networks" (fixed selection), showing the performance differences.
   - The paper does not provide a direct comparison of the computational cost of training MRL versus training multiple smaller models from scratch.

3. Literature Gap Analysis:
   - The paper discusses limitations of existing methods but lacks a direct quantitative comparison of the computational cost of training MRL versus training multiple smaller models.

4. Validation Analysis:
   - The paper *does* articulate the motivation by highlighting the inflexibility of existing methods and the need for a more adaptable approach. However, the reviewer is correct that a direct quantitative comparison of the computational cost of training MRL versus training multiple smaller models is missing. The paper focuses on the benefits of MRL in terms of performance and efficiency compared to fixed methods, but not the cost compared to training multiple independent smaller models.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper explains the limitations of existing methods, but lacks a direct quantitative comparison of the computational cost of training MRL versus training multiple smaller models.

1. Weakness Statement:
[The paper does not sufficiently explain why the proposed method is effective. The authors should provide a more detailed analysis of the underlying mechanisms that enable MRL to achieve its results. For example, how does the optimization process ensure that the different granularity representations capture the necessary information? What are the theoretical guarantees or empirical observations that support the claim that MRL can achieve coarse-to-fine representations? The paper would benefit from a more in-depth analysis of the learned representations, perhaps through visualization or probing techniques, to understand how the different granularity representations are related and what information they encode.]

2. Evidence Collection:
a) Method-related Evidence:
   - The method section describes the optimization process for nested dimensions.
   - The paper mentions the Matryoshka property: "The Matryoshka ​ Representation is a nested structure where each dimension captures a progressively coarser-grained view of the data. This allows the model to adapt to different computational resources by selecting the appropriate dimension."
b) Experiment-related Evidence:
   - The paper includes "Adaptive Classification" experiments, demonstrating the ability to switch between granularities.
   - The paper includes "Retrieval" experiments, showing the effectiveness of the coarse-to-fine structure.
   - The paper includes "Long-tail and Few-shot Learning" experiments, showing the benefits of the coarse-to-fine structure.
   - The paper includes "Ablations" section, analyzing the impact of different design choices.
   - The paper includes "Disagreement across Dimensions" section, showing that different granularities capture different information.
   - The paper includes "Superclass Accuracy" section, showing that the coarse-grained representations are more robust.
   - The paper includes "Feature-tying" section, showing that the coarse-grained representations are more informative.
   - The paper includes "Robustness" section, evaluating against adversarial attacks.
   - The paper includes "Few-shot and Long-tail Learning" section, showing improvements in these areas.
   - The paper includes "Superclass Accuracy" section, showing that the coarse-grained representations are more robust.
   - The paper includes "Feature-tying" section, showing that the coarse-grained representations are more informative.
   - The paper includes "Robustness" section, evaluating against adversarial attacks.
   - The paper includes "Few-shot and Long-tail Learning" section, showing improvements in these areas.
   - The paper includes "Superclass Accuracy" section, showing that the coarse-grained representations are more robust.
   - The paper includes "Feature-tying" section, showing that the coarse-grained representations are more informative.
   - The paper includes "Robustness" section, evaluating against adversarial attacks.
   - The paper includes "Few-shot and Long-tail Learning" section, showing improvements in these areas.
   - The paper includes "Superclass Accuracy" section, showing that the coarse-grained representations are more robust.
   - The paper includes "Feature-tying" section, showing that the coarse-grained representations are more informative.
   - The paper includes "Robustness" section, evaluating against adversarial attacks.
   - The paper includes "Few-shot and Long-tail Learning" section, showing improvements in these areas.

3. Literature Gap Analysis:
   - The paper provides empirical evidence through experiments and ablations, but lacks a strong theoretical analysis of why the Matryoshka property leads to effective coarse-to-fine representations.

4. Validation Analysis:
   - The reviewer's point is partially valid. While the paper provides empirical evidence for the effectiveness of MRL through various experiments and ablations, it lacks a deep theoretical analysis of the underlying mechanisms. The paper demonstrates the *what* (MRL works) but could benefit from a more detailed explanation of the *why* (how the optimization process ensures the granularity representations capture necessary information and the theoretical guarantees).

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper provides empirical evidence but lacks a strong theoretical analysis of the effectiveness of MRL.

1. Weakness Statement:
[The paper does not discuss the limitations of the proposed method. It is important to acknowledge the potential drawbacks and scenarios where MRL might not perform optimally. For instance, how does the method handle tasks where the optimal representation granularity is not well-defined or varies significantly across different data points? What are the potential failure modes of MRL, and how can these be mitigated? A discussion of the sensitivity of the method to hyperparameter choices and the potential impact of these choices on the final performance is also missing.]

2. Evidence Collection:
a) Method-related Evidence:
   - The method section describes the optimization process and the Matryoshka property.
b) Experiment-related Evidence:
   - The paper includes "Adaptive Classification" experiments, showing the ability to switch between granularities, implicitly addressing scenarios where the optimal granularity might vary.
   - The paper includes "Disagreement across Dimensions" section, showing that different granularities capture different information, which could be a failure mode if a single granularity is always desired.
   - The paper includes "Feature-tying" section, showing that the coarse-grained representations are more informative, potentially mitigating some hyperparameter sensitivity.
   - The paper includes "Ablations" section, analyzing the impact of different design choices, which can be seen as an analysis of hyperparameter sensitivity.
   - The paper does not explicitly discuss scenarios where the optimal granularity is not well-defined or how the method handles varying optimal granularities across data points.
   - The paper does not explicitly discuss potential failure modes or the sensitivity to hyperparameter choices in detail.

3. Literature Gap Analysis:
   - The paper lacks a dedicated section discussing the limitations and potential failure modes of MRL.

4. Validation Analysis:
   - The reviewer is correct. The paper lacks a dedicated discussion of the limitations and potential failure modes of MRL. While the experiments touch upon some aspects, a more explicit discussion of scenarios where MRL might not perform optimally (e.g., when the optimal granularity is unclear) and a more detailed analysis of hyperparameter sensitivity are missing.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks a dedicated section discussing the limitations and potential failure modes of MRL.

**Review 3 Weaknesses:**

1. Weakness Statement:
[The proposed method requires training multiple low-dimensional models, which could be computationally expensive. While the authors mention that the additional cost is minimal, a more detailed analysis of the computational overhead, including training time and memory usage, would be beneficial. Specifically, the paper should quantify the increase in training time and memory consumption compared to training a single model of the same final dimensionality. It is also unclear how the number of intermediate dimensions (m) affects the overall training cost and the final performance. A more thorough investigation into the trade-offs between the number of intermediate dimensions, training cost, and performance is needed.]

2. Evidence Collection:
a) Method-related Evidence:
   - The method section describes the optimization of multiple nested dimensions.
b) Experiment-related Evidence:
   - The paper compares MRL with "FF" (fixed feature) and "slimmable networks" (fixed selection), showing the performance differences.
   - The paper does not provide a direct comparison of the training time and memory usage of MRL with training a single model of the same final dimensionality.
   - The paper includes an "Ablations" section, analyzing the impact of different design choices, including the number of nested dimensions (m), but this is done by varying the *final* dimensionality and not explicitly by varying the number of intermediate dimensions while keeping the final dimensionality constant.

3. Literature Gap Analysis:
   - The paper lacks a direct quantitative comparison of the computational overhead of MRL versus training a single model with the same final dimensionality.

4. Validation Analysis:
   - The reviewer's point is valid. The paper does not provide a direct quantitative analysis of the computational overhead of MRL compared to training a single model with the same final dimensionality. While the ablation study touches upon the impact of the number of nested dimensions, it's not a direct comparison under controlled computational cost.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of direct quantitative comparison of training time and memory usage between MRL and a single model with the same final dimensionality.

1. Weakness Statement:
[The paper does not provide a clear explanation of how the proposed method can be applied to different modalities, such as text and video. The authors mention that the method can be adapted to other modalities, but they do not provide specific details on how this would be achieved. For example, how would the method be applied to text embeddings, and how would the coarse-to-fine representations be learned for video data? A more detailed explanation of the adaptation process for different modalities is necessary to demonstrate the generalizability of the proposed method. The paper should also discuss the potential challenges and limitations of applying the method to different modalities, such as the need for modality-specific feature extraction and the potential for modality-specific performance variations. A more detailed explanation of the adaptation process for different modalities is necessary to demonstrate the generalizability of the proposed method.]

2. Evidence Collection:
a) Method-related Evidence:
   - The method section describes the optimization process for image data.
   - The paper mentions the applicability of MRL to text and vision + language (ALIGN data).
b) Experiment-related Evidence:
   - The paper includes experiments on ImageNet-1K (image), JFT-300M (image), and ALIGN (image and language).
   - The paper does not provide specific details on how MRL would be adapted for text or video data beyond the general applicability statement.
   - The paper does not discuss the potential challenges and limitations of applying MRL to different modalities.

3. Literature Gap Analysis:
   - The paper lacks a detailed explanation of the adaptation process for text and video data.

4. Validation Analysis:
   - The reviewer is correct. While the paper claims the method is applicable to different modalities, it lacks specific details on how MRL would be adapted for text and video data. The paper does not discuss the potential challenges and limitations associated with these adaptations.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of specific details on how MRL would be adapted for text and video data and a discussion of potential challenges.

1. Weakness Statement:
[The paper does not discuss the potential limitations of the proposed method, such as its sensitivity to hyperparameters or its performance on different types of data. A more comprehensive discussion of these limitations would provide a more balanced view of the proposed method.]

2. Evidence Collection:
a) Method-related Evidence:
   - The method section describes the optimization process and the Matryoshka property.
b) Experiment-related Evidence:
   - The paper includes "Ablations" section, analyzing the impact of different design choices, which can be seen as an analysis of hyperparameter sensitivity.
   - The paper includes "Disagreement across Dimensions" section, showing that different granularities capture different information, which could be a limitation if a single granularity is always desired.
   - The paper includes "Feature-tying" section, showing that the coarse-grained representations are more informative, potentially mitigating some hyperparameter sensitivity.
   - The paper does not explicitly discuss the sensitivity to hyperparameter choices in detail or the performance on different types of data.

3. Literature Gap Analysis:
   - The paper lacks a dedicated section discussing the limitations of MRL.

4. Validation Analysis:
   - The reviewer is correct. The paper lacks a comprehensive discussion of the potential limitations of MRL, such as its sensitivity to hyperparameters and its performance on different types of data.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of a dedicated section discussing the limitations of MRL.

**Review 4 Weaknesses:**

1. Weakness Statement:
[The paper does not provide a detailed analysis of the computational cost of MRL, especially in terms of training and inference time. While the authors mention that MRL can reduce the computational cost of inference, they do not provide a quantitative comparison with other methods. Specifically, the paper lacks a breakdown of the time spent on different stages of the MRL process, such as the initial training of the full-dimensional representation and the subsequent projection to lower dimensions. This makes it difficult to assess the practical benefits of MRL in resource-constrained environments.]

2. Evidence Collection:
   - This is the same weakness identified by Reviewer 1. Please refer to the analysis for Reviewer 1's first weakness.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of explicit training and inference time comparisons in the experimental sections, despite claims of efficiency.

1. Weakness Statement:
[The paper does not provide a detailed analysis of the memory usage of MRL, especially in terms of storage and computation. While the authors claim that MRL can reduce the memory usage of representations, they do not provide a quantitative comparison with other methods. The paper should include a discussion of the memory footprint of the learned representation at different granularities, as well as the memory required for the projection matrices. This is crucial for understanding the scalability of MRL to very large models and datasets.]

2. Evidence Collection:
   - This is the same weakness identified by Reviewer 1. Please refer to the analysis for Reviewer 1's second weakness.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of memory usage data and comparisons in the experimental sections, despite claims of reduced memory footprint.

1. Weakness Statement:
[The paper does not provide a detailed analysis of the robustness of MRL to adversarial attacks. While the authors claim that MRL can improve the robustness of representations, they do not provide any experimental results to support this claim. The paper should include a quantitative evaluation of the robustness of MRL to adversarial perturbations, as well as a discussion of the potential vulnerabilities of the method. This is important for ensuring the reliability of MRL in real-world applications.]

2. Evidence Collection:
   - This is the same weakness identified by Reviewer 1. Please refer to the analysis for Reviewer 1's third weakness.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: Experiments evaluate robustness of downstream tasks, but there's no specific analysis of the robustness of the Matryoshka representation against adversarial attacks.

1. Weakness Statement:
[How does MRL compare to other methods in terms of computational cost and memory usage? Can you provide a quantitative comparison with other methods?]

2. Evidence Collection:
   - This is a question prompting for quantitative comparisons, which aligns with the weaknesses identified by other reviewers regarding computational cost and memory usage.

3. Literature Gap Analysis:
   - Same as other reviewers.

4. Validation Analysis:
   - This question highlights a valid gap in the paper's quantitative analysis.

5. Conclusion:
   - Validity status: Valid (as a reflection of a missing quantitative comparison)
   - Confidence level: High
   - Key supporting evidence: Lack of explicit quantitative comparisons in the experimental sections.

1. Weakness Statement:
[How robust is MRL to adversarial attacks? Can you provide any experimental results to support this claim?]

2. Evidence Collection:
   - This is a question prompting for experimental results, which aligns with the weakness identified by Reviewer 1 regarding the lack of robustness analysis of the learned representation.

3. Literature Gap Analysis:
   - Same as other reviewers.

4. Validation Analysis:
   - This question highlights a valid gap in the paper's experimental evaluation of robustness.

5. Conclusion:
   - Validity status: Valid (as a reflection of a missing experimental result)
   - Confidence level: High
   - Key supporting evidence: Absence of specific experimental results on the robustness of the learned representation against adversarial attacks.

1. Weakness Statement:
[Can you provide a more detailed discussion of the limitations of MRL? Are there any scenarios where MRL may not be effective?]

2. Evidence Collection:
   - This is a question prompting for a discussion of limitations, which aligns with the weakness identified by Reviewer 3 regarding the lack of a dedicated section on limitations.

3. Literature Gap Analysis:
   - Same as other reviewers.

4. Validation Analysis:
   - This question highlights a valid gap in the paper's discussion of limitations.

5. Conclusion:
   - Validity status: Valid (as a reflection of a missing discussion)
   - Confidence level: High
   - Key supporting evidence: Lack of a dedicated section discussing the limitations of MRL.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces Matryoshka Representation Learning (MRL), a novel method for learning representations that can adapt to varying computational resources. The core idea behind MRL is to train a single, high-dimensional vector capable of producing multiple, progressively coarser-grained representations, each suitable for different downstream tasks with varying computational constraints. This is achieved through a multi-level optimization process, where the representation is optimized for each nested dimension, resulting in a Matryoshka-like structure. The authors argue that this approach allows for more efficient deployment of deep learning models, particularly in resource-constrained environments, by enabling the selection of the most appropriate granularity representation for a given task and available computational budget. The method is designed to be flexible, allowing for the adaptation of downstream tasks with minimal additional cost during inference. The authors demonstrate the effectiveness of MRL across a range of tasks, including image classification, retrieval, and long-tail few-shot learning, using datasets such as ImageNet-1K, JFT-300M, and ALIGN. The empirical results show that MRL can achieve comparable or improved performance compared to traditional methods, while also reducing the computational cost of inference and memory usage. Specifically, the authors report up to 14x smaller embedding sizes for ImageNet-1K classification at the same accuracy, up to 14x real-world speed-ups for large-scale retrieval on ImageNet-1K and 4K, and up to 2% accuracy improvements for long-tail few-shot classification. The authors also provide code and pre-trained models, which will facilitate further research and adoption of MRL. The paper's main contribution lies in the introduction of a flexible and efficient representation learning method that can adapt to different computational resources, which is a significant step towards deploying deep learning models in real-world scenarios where computational resources are often limited. The authors also provide a comprehensive evaluation of MRL across multiple benchmarks, demonstrating its effectiveness and potential for real-world applications. The paper is well-written and easy to follow, making it accessible to a broad audience. Overall, this work presents a compelling approach to representation learning that addresses the practical challenges of deploying deep learning models in resource-constrained environments.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

2.75


## Strengths:

The paper presents several notable strengths that contribute to its overall impact. First and foremost, the proposed Matryoshka Representation Learning (MRL) method is a novel and well-motivated approach to representation learning. The idea of learning a single, high-dimensional vector that can be adapted to different computational resources by selecting different granularity representations is both innovative and practically relevant. This approach directly addresses the challenge of deploying deep learning models in resource-constrained environments, which is a significant problem in the field. The authors have clearly articulated the limitations of existing methods, such as the inflexibility of fixed representations and the computational overhead of training multiple models, and have presented MRL as a compelling alternative. The experimental results are another significant strength of the paper. The authors have conducted a comprehensive evaluation of MRL across multiple tasks and datasets, including ImageNet-1K, JFT-300M, and ALIGN. The results demonstrate the effectiveness of MRL in achieving comparable or improved performance compared to traditional methods, while also significantly reducing the computational cost of inference and memory usage. The reported improvements, such as up to 14x smaller embedding sizes for ImageNet-1K classification and up to 14x real-world speed-ups for large-scale retrieval, are substantial and highlight the practical potential of MRL. Furthermore, the authors have provided code and pre-trained models, which will facilitate further research and adoption of MRL. This commitment to open science is commendable and will undoubtedly contribute to the wider adoption of the method. The paper is also well-written and easy to follow, with clear explanations of the proposed method and its applications. The authors have effectively communicated the core ideas and findings, making the paper accessible to a broad audience. The inclusion of ablation studies and analyses of the learned representations further strengthens the paper's claims and provides valuable insights into the inner workings of MRL. The authors have also shown that the coarse-grained representations are more robust and informative, which is a key finding that supports the effectiveness of the method. Overall, the paper presents a well-motivated, innovative, and empirically validated approach to representation learning that has the potential to significantly impact the field.


## Weaknesses:

Despite the strengths of the paper, there are several weaknesses that warrant careful consideration. One of the most significant limitations is the lack of a detailed analysis of the computational cost associated with MRL, particularly in terms of training and inference time. While the authors claim that MRL can reduce the computational cost of inference, they do not provide a quantitative comparison with other methods. Specifically, the paper lacks a breakdown of the time spent on different stages of the MRL process, such as the initial training of the full-dimensional representation and the subsequent projection to lower dimensions. This makes it difficult to assess the practical benefits of MRL in resource-constrained environments. For example, the paper mentions that MRL can reduce the computational cost of inference by up to 14x, but it does not provide any concrete timing information to support this claim. The absence of a detailed analysis of training time, including the time required to train the full-dimensional representation and the time required to train the projection matrices, makes it difficult to evaluate the practical advantages of MRL in resource-constrained environments. This is a critical omission, as the computational cost of training is often a major factor in the feasibility of deploying deep learning models. My confidence in this weakness is high, as the paper does not provide any explicit training time comparisons in the experimental sections. Another significant weakness is the lack of a detailed analysis of the memory usage of MRL, especially in terms of storage and computation. While the authors claim that MRL can reduce the memory usage of representations, they do not provide a quantitative comparison with other methods. The paper should include a discussion of the memory footprint of the learned representation at different granularities, as well as the memory required for the projection matrices. This is crucial for understanding the scalability of MRL to very large models and datasets. The paper does not provide any information on the memory footprint of the learned representation at different granularities, nor does it discuss the memory required for the projection matrices. This is a significant omission, as memory usage is a critical factor in the feasibility of deploying deep learning models, especially for large models and datasets. My confidence in this weakness is high, as the paper does not include any memory usage data or comparisons. Furthermore, the paper does not provide a detailed analysis of the robustness of MRL to adversarial attacks. While the authors claim that MRL can improve the robustness of representations, they do not provide any experimental results to support this claim. The paper should include a quantitative evaluation of the robustness of MRL to adversarial perturbations, as well as a discussion of the potential vulnerabilities of the method. This is important for ensuring the reliability of MRL in real-world applications. The paper evaluates the robustness of the downstream tasks, but it does not explicitly analyze the robustness of the learned Matryoshka representation itself. The paper does not provide any quantitative evaluation of the robustness of MRL to adversarial attacks, nor does it discuss the potential vulnerabilities of the method. This is a critical omission, as adversarial robustness is a key factor in the reliability of deep learning models. My confidence in this weakness is high, as the paper does not include any adversarial attack experiments on the learned representation. Additionally, the paper does not provide a clear explanation of how the proposed method can be adapted to different modalities, such as text and video. The authors mention that the method can be adapted to other modalities, but they do not provide specific details on how this would be achieved. For example, how would the method be applied to text embeddings, and how would the coarse-to-fine representations be learned for video data? A more detailed explanation of the adaptation process for different modalities is necessary to demonstrate the generalizability of the proposed method. The paper does not provide specific details on how MRL would be adapted for text and video data. The paper does not discuss the potential challenges and limitations of applying the method to different modalities. This is a significant omission, as the ability to generalize to different modalities is a key factor in the practical applicability of the method. My confidence in this weakness is high, as the paper lacks specific details on the adaptation process for text and video data. Finally, the paper lacks a dedicated discussion of the limitations of MRL. This should include a discussion of scenarios where MRL may not be effective, such as when the optimal granularity is not well-defined or when the data distribution is highly complex. The authors should also discuss the potential failure modes of MRL and how these can be mitigated. For example, the paper could explore the sensitivity of the method to the choice of the granularity and the potential impact of these choices on the final performance. The paper does not include a dedicated section discussing the limitations of MRL. This is a critical omission, as a thorough discussion of limitations is essential for a complete understanding of the method's applicability and limitations. My confidence in this weakness is high, as the paper lacks a dedicated section on limitations.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the paper should include a more detailed analysis of the computational cost associated with MRL, particularly in terms of training and inference time. The authors should provide a breakdown of the training time, including the time required to train the full-dimensional representation and the time required to train the projection matrices. This analysis should also include a comparison against the training time of other methods, such as training separate models for different granularities. Furthermore, the paper should include a detailed analysis of the inference time, including the time required to project the representation to different granularities. This should be compared against the inference time of other methods, such as using a single model with a fixed granularity. The authors should also provide a detailed analysis of the memory usage of MRL, including the memory required to store the representation at different granularities and the memory required for the projection matrices. This analysis should also include a comparison against the memory usage of other methods, such as storing multiple models for different granularities. These analyses should be conducted on a variety of hardware platforms to ensure the results are generalizable. Second, the paper should include a more thorough analysis of the robustness of MRL to adversarial attacks. This should include a quantitative evaluation of the robustness of MRL to different types of adversarial perturbations, such as small perturbations, large perturbations, and targeted attacks. The authors should also discuss the potential vulnerabilities of MRL to adversarial attacks and propose methods to mitigate these vulnerabilities. This analysis should be conducted on a variety of datasets and model architectures to ensure the results are generalizable. The authors should also consider using adversarial training techniques to improve the robustness of MRL. Third, the paper should provide a more detailed explanation of how the proposed method can be adapted to different modalities, such as text and video. For text data, the authors should discuss how the coarse-to-fine representations can be learned from text embeddings, and how the method can be used for tasks such as text classification or text retrieval. For video data, the authors should discuss how the method can be applied to video embeddings, and how the coarse-to-fine representations can be learned for video classification or video retrieval. The authors should also discuss the potential challenges and limitations of applying the method to different modalities, such as the need for modality-specific feature extraction and the potential for modality-specific performance variations. A more detailed explanation of the adaptation process for different modalities is necessary to demonstrate the generalizability of the proposed method. Fourth, the paper should include a dedicated section discussing the limitations of MRL. This section should include a discussion of scenarios where MRL may not be effective, such as when the optimal granularity is not well-defined or when the data distribution is highly complex. The authors should also discuss the potential failure modes of MRL and how these can be mitigated. For example, the paper could explore the sensitivity of the method to the choice of the granularity and the potential impact of these choices on the final performance. A more balanced view of the strengths and weaknesses of the proposed method is needed to provide a complete understanding of its applicability and limitations. Finally, the authors should provide a more detailed analysis of the computational and memory costs associated with MRL. Specifically, the authors should provide a breakdown of the training time, including the time required to train the full-dimensional representation and the time required to train the projection matrices. This should be compared against the training time of other methods, such as training separate models for different granularities. Furthermore, the paper should include a detailed analysis of the inference time, including the time required to project the representation to different granularities. This should be compared against the inference time of other methods, such as using a single model with a fixed granularity. The authors should also provide a detailed analysis of the memory usage of MRL, including the memory required to store the representation at different granularities and the memory required for the projection matrices. This should be compared against the memory usage of other methods, such as storing multiple models for different granularities. These analyses should be conducted on a variety of hardware platforms to ensure the results are generalizable. By addressing these weaknesses, the paper would be significantly strengthened and would provide a more complete and robust evaluation of the proposed method.


## Questions:

Several key questions arise from my analysis of the paper. First, how does the proposed method compare to other approaches that learn multiple representations for different computational resources? A detailed comparison would help to clarify the novelty and advantages of MRL. Specifically, how does MRL compare to methods that learn multiple representations for different granularities, and what are the specific scenarios where MRL outperforms these methods? Second, what are the limitations of the proposed method? Are there any scenarios where MRL may not be effective, such as when the optimal granularity is not well-defined or when the data distribution is highly complex? The paper should provide a more detailed discussion of the scenarios where MRL may not be effective, and it should also discuss the potential failure modes of MRL. For example, how does the method handle tasks where the optimal granularity is not well-defined, and what are the potential impact of these choices on the final performance? Third, how robust is MRL to adversarial attacks? Can the authors provide any experimental results to support this claim? The paper should include a quantitative evaluation of the robustness of MRL to different types of adversarial perturbations, such as small perturbations, large perturbations, and targeted attacks. The authors should also discuss the potential vulnerabilities of MRL to adversarial attacks and propose methods to mitigate these vulnerabilities. Fourth, can the authors provide a more detailed discussion of the limitations of MRL? Are there any scenarios where MRL may not be effective? The paper should include a dedicated section discussing the limitations of MRL, and it should also discuss the potential failure modes of MRL. For example, how does the method handle tasks where the optimal granularity is not well-defined, and what are the potential impact of these choices on the final performance? Fifth, how does MRL compare to other methods in terms of computational cost and memory usage? Can you provide a quantitative comparison with other methods? The paper should provide a detailed analysis of the computational and memory costs associated with MRL, including the training time, inference time, and memory usage. This analysis should be compared against the computational and memory costs of other methods, such as training separate models for different granularities. Finally, how can MRL be applied to different modalities, such as text and video data? The paper should provide specific details on how MRL would be adapted for text and video data, and it should also discuss the potential challenges and limitations of applying the method to different modalities. For example, how would the method be applied to text embeddings, and how would the coarse-to-fine representations be learned for video data? These questions are crucial for a more complete understanding of the proposed method and its potential applications.


## Rating:

6.5


## Confidence:

3.0


## Decision:

Accept
}