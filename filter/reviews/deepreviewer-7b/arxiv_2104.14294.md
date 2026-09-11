I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper explores the self-supervised learning of ViT models and reveals that SSL features contain explicit information about the semantic segmentation of an image, which does not emerge in convolutional networks. The authors also find that these features perform exceptionally well with a simple k-NN classifier. Additionally, they introduce a simple self-supervised approach called DINO, which they interpret as a form of knowledge distillation with no labels. The proposed DINO method achieves state-of-the-art results on ImageNet with a linear evaluation of a ViT-Base model.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a thorough analysis of the self-supervised learning of ViT models.
3. The proposed DINO method achieves state-of-the-art results on ImageNet with a linear evaluation of a ViT-Base model.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a comprehensive comparison with other self-supervised learning methods, particularly those that also utilize ViT models. The absence of a detailed comparison makes it difficult to assess the true novelty and effectiveness of the proposed DINO method relative to existing approaches. For example, a comparison with methods that use contrastive learning or masked image modeling with ViTs would be beneficial.
2. The paper does not provide a thorough analysis of the computational cost and efficiency of the proposed method. While the authors mention that DINO achieves state-of-the-art results, they do not discuss the computational resources required for training and inference, which is a critical factor for practical applications. A comparison of training time, memory usage, and inference speed with other self-supervised methods would be valuable.
3. The paper does not explore the robustness of the proposed method to different datasets and tasks. The evaluation is primarily focused on ImageNet, and it is unclear how well the learned representations generalize to other datasets or tasks, such as object detection or segmentation. An evaluation on a more diverse set of tasks would strengthen the paper's claims.

### Suggestions

To address the lack of comprehensive comparison, the authors should include a more detailed analysis of how DINO compares to other self-supervised learning methods that use ViT models. This should include a comparison of performance on ImageNet, as well as an analysis of the computational cost and efficiency of each method. Specifically, the authors should compare DINO with methods that use contrastive learning, masked image modeling, and other relevant self-supervised techniques. This comparison should not only focus on accuracy but also on other metrics such as training time, memory usage, and inference speed. Furthermore, the authors should provide a detailed analysis of the architectural differences between DINO and other methods, and how these differences contribute to the observed performance. This would help to better understand the strengths and weaknesses of the proposed approach.

To address the lack of analysis on computational cost and efficiency, the authors should include a detailed analysis of the computational resources required for training and inference. This analysis should include a comparison of training time, memory usage, and inference speed with other self-supervised methods. The authors should also discuss the scalability of the proposed method to larger datasets and models. This analysis should be performed on a variety of hardware configurations to provide a comprehensive understanding of the computational requirements. Additionally, the authors should explore techniques to optimize the computational efficiency of the proposed method, such as model pruning or quantization. This would make the proposed method more practical for real-world applications.

To address the lack of exploration of robustness, the authors should evaluate the proposed method on a more diverse set of datasets and tasks. This should include an evaluation on datasets with different characteristics, such as different image resolutions, object categories, and background clutter. The authors should also evaluate the performance of the proposed method on tasks beyond image classification, such as object detection, semantic segmentation, and image retrieval. This would provide a more comprehensive understanding of the generalizability of the learned representations. Furthermore, the authors should analyze the limitations of the proposed method and discuss potential avenues for future research. This would help to identify areas where the proposed method could be improved and extended.

### Questions

1. How does the proposed DINO method compare to other self-supervised learning methods that also utilize ViT models?
2. What is the computational cost and efficiency of the proposed method compared to other self-supervised methods?
3. How robust is the proposed method to different datasets and tasks?

### Rating

6

### Confidence

4

**********

## Reviewer 2

### Summary

This paper studies the self-supervised learning of Vision Transformers (ViTs) and finds that SSL features contain explicit information about the semantic segmentation of an image. The authors also find that these features perform exceptionally well with a simple k-NN classifier. Additionally, they introduce a simple self-supervised approach called DINO, which they interpret as a form of knowledge distillation with no labels. The proposed DINO method achieves state-of-the-art results on ImageNet with a linear evaluation of a ViT-Base model.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a thorough analysis of the self-supervised learning of ViT models.
3. The proposed DINO method achieves state-of-the-art results on ImageNet with a linear evaluation of a ViT-Base model.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a comprehensive comparison with other self-supervised learning methods, particularly those that also utilize ViT models. The absence of a detailed comparison makes it difficult to assess the true novelty and effectiveness of the proposed DINO method relative to existing approaches. For example, a comparison with methods that use contrastive learning or masked image modeling with ViTs would be beneficial.
2. The paper does not provide a thorough analysis of the computational cost and efficiency of the proposed method. While the authors mention that DINO achieves state-of-the-art results, they do not discuss the computational resources required for training and inference, which is a critical factor for practical applications. A comparison of training time, memory usage, and inference speed with other self-supervised methods would be valuable.
3. The paper does not explore the robustness of the proposed method to different datasets and tasks. The evaluation is primarily focused on ImageNet, and it is unclear how well the learned representations generalize to other datasets or tasks, such as object detection or segmentation. An evaluation on a more diverse set of tasks would strengthen the paper's claims.

### Suggestions

The paper would benefit significantly from a more detailed comparison with existing self-supervised learning methods, particularly those employing Vision Transformers. The current analysis lacks a thorough benchmark against methods that utilize contrastive learning, masked image modeling, or other relevant techniques. A comprehensive comparison should not only focus on accuracy but also on computational cost, training time, and memory usage. For instance, the authors could compare DINO with methods like SimCLR, MoCo, or BEiT, which are widely used in the field. This would help to contextualize the performance of DINO and highlight its specific advantages and disadvantages. Furthermore, the comparison should include a discussion of the architectural differences between DINO and other methods, and how these differences contribute to the observed performance. This would provide a more nuanced understanding of the proposed approach.

To address the lack of analysis on computational cost and efficiency, the authors should provide a detailed breakdown of the training and inference times, as well as the memory requirements of the proposed method. This analysis should be performed on a variety of hardware configurations to provide a comprehensive understanding of the computational requirements. The authors should also compare the computational cost of DINO with other self-supervised methods, including both training and inference. This comparison should include a discussion of the trade-offs between performance and computational cost. For example, the authors could compare the training time and memory usage of DINO with methods like MoCo or BYOL, which are known for their efficiency. This would help to assess the practicality of DINO for real-world applications. Additionally, the authors should explore techniques to optimize the computational efficiency of the proposed method, such as model pruning or quantization.

Finally, the paper needs to address the robustness of the proposed method to different datasets and tasks. The current evaluation is limited to ImageNet, which is a relatively small and well-studied dataset. To demonstrate the generalizability of the learned representations, the authors should evaluate DINO on a more diverse set of datasets, including those with different characteristics, such as different image resolutions, object categories, and background clutter. Furthermore, the authors should evaluate the performance of DINO on tasks beyond image classification, such as object detection, semantic segmentation, and image retrieval. This would provide a more comprehensive understanding of the capabilities of the proposed method. For example, the authors could evaluate DINO on the COCO dataset for object detection or the Pascal VOC dataset for semantic segmentation. This would help to assess the versatility of the learned representations and their applicability to real-world scenarios.

### Questions

Please see the weakness.

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper investigates the properties of self-supervised learning (SSL) features with Vision Transformer (ViT) architectures. The authors observe that SSL features contain explicit information about the semantic segmentation of an image and perform well with a simple k-NN classifier. They also propose a simple self-supervised approach called DINO, which they interpret as a form of knowledge distillation with no labels. The DINO method achieves state-of-the-art results on ImageNet with a linear evaluation of a ViT-Base model.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a thorough analysis of the self-supervised learning of ViT models.
3. The proposed DINO method achieves state-of-the-art results on ImageNet with a linear evaluation of a ViT-Base model.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a comprehensive comparison with other self-supervised learning methods, particularly those that also utilize ViT models. The absence of a detailed comparison makes it difficult to assess the true novelty and effectiveness of the proposed DINO method relative to existing approaches. For example, a comparison with methods that use contrastive learning or masked image modeling with ViTs would be beneficial.
2. The paper does not provide a thorough analysis of the computational cost and efficiency of the proposed method. While the authors mention that DINO achieves state-of-the-art results, they do not discuss the computational resources required for training and inference, which is a critical factor for practical applications. A comparison of training time, memory usage, and inference speed with other self-supervised methods would be valuable.
3. The paper does not explore the robustness of the proposed method to different datasets and tasks. The evaluation is primarily focused on ImageNet, and it is unclear how well the learned representations generalize to other datasets or tasks, such as object detection or segmentation. An evaluation on a more diverse set of tasks would strengthen the paper's claims.

### Suggestions

The paper would benefit significantly from a more detailed comparison with existing self-supervised learning methods, particularly those employing Vision Transformers. The current analysis lacks a thorough benchmark against methods that utilize contrastive learning, masked image modeling, or other relevant techniques. A comprehensive comparison should not only focus on accuracy but also on computational cost, training time, and memory usage. For instance, the authors could compare DINO with methods like SimCLR, MoCo, or BEiT, which are widely used in the field. This would help to contextualize the performance of DINO and highlight its specific advantages and disadvantages. Furthermore, the comparison should include a discussion of the architectural differences between DINO and other methods, and how these differences contribute to the observed performance. This would provide a more nuanced understanding of the proposed approach.

To address the lack of analysis on computational cost and efficiency, the authors should provide a detailed breakdown of the training and inference times, as well as the memory requirements of the proposed method. This analysis should be performed on a variety of hardware configurations to provide a comprehensive understanding of the computational requirements. The authors should also compare the computational cost of DINO with other self-supervised methods, including both training and inference. This comparison should include a discussion of the trade-offs between performance and computational cost. For example, the authors could compare the training time and memory usage of DINO with methods like MoCo or BYOL, which are known for their efficiency. This would help to assess the practicality of DINO for real-world applications. Additionally, the authors should explore techniques to optimize the computational efficiency of the proposed method, such as model pruning or quantization.

Finally, the paper needs to address the robustness of the proposed method to different datasets and tasks. The current evaluation is limited to ImageNet, which is a relatively small and well-studied dataset. To demonstrate the generalizability of the learned representations, the authors should evaluate DINO on a more diverse set of datasets, including those with different characteristics, such as different image resolutions, object categories, and background clutter. Furthermore, the authors should evaluate the performance of DINO on tasks beyond image classification, such as object detection, semantic segmentation, and image retrieval. This would provide a more comprehensive understanding of the capabilities of the proposed method. For example, the authors could evaluate DINO on the COCO dataset for object detection or the Pascal VOC dataset for semantic segmentation. This would help to assess the versatility of the learned representations and their applicability to real-world scenarios.

### Questions

Please see the weakness.

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

This paper investigates the properties of self-supervised learning (SSL) features with Vision Transformer (ViT) architectures. The authors observe that SSL features contain explicit information about the semantic segmentation of an image and perform well with a simple k-NN classifier. They also propose a simple self-supervised approach called DINO, which they interpret as a form of knowledge distillation with no labels. The DINO method achieves state-of-the-art results on ImageNet with a linear evaluation of a ViT-Base model.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a thorough analysis of the self-supervised learning of ViT models.
3. The proposed DINO method achieves state-of-the-art results on ImageNet with a linear evaluation of a ViT-Base model.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a comprehensive comparison with other self-supervised learning methods, particularly those that also utilize ViT models. The absence of a detailed comparison makes it difficult to assess the true novelty and effectiveness of the proposed DINO method relative to existing approaches. For example, a comparison with methods that use contrastive learning or masked image modeling with ViTs would be beneficial.
2. The paper does not provide a thorough analysis of the computational cost and efficiency of the proposed method. While the authors mention that DINO achieves state-of-the-art results, they do not discuss the computational resources required for training and inference, which is a critical factor for practical applications. A comparison of training time, memory usage, and inference speed with other self-supervised methods would be valuable.
3. The paper does not explore the robustness of the proposed method to different datasets and tasks. The evaluation is primarily focused on ImageNet, and it is unclear how well the learned representations generalize to other datasets or tasks, such as object detection or segmentation. An evaluation on a more diverse set of tasks would strengthen the paper's claims.

### Suggestions

The paper would benefit significantly from a more detailed comparison with existing self-supervised learning methods, particularly those employing Vision Transformers. The current analysis lacks a thorough benchmark against methods that utilize contrastive learning, masked image modeling, or other relevant techniques. A comprehensive comparison should not only focus on accuracy but also on computational cost, training time, and memory usage. For instance, the authors could compare DINO with methods like SimCLR, MoCo, or BEiT, which are widely used in the field. This would help to contextualize the performance of DINO and highlight its specific advantages and disadvantages. Furthermore, the comparison should include a discussion of the architectural differences between DINO and other methods, and how these differences contribute to the observed performance. This would provide a more nuanced understanding of the proposed approach.

To address the lack of analysis on computational cost and efficiency, the authors should provide a detailed breakdown of the training and inference times, as well as the memory requirements of the proposed method. This analysis should be performed on a variety of hardware configurations to provide a comprehensive understanding of the computational requirements. The authors should also compare the computational cost of DINO with other self-supervised methods, including both training and inference. This comparison should include a discussion of the trade-offs between performance and computational cost. For example, the authors could compare the training time and memory usage of DINO with methods like MoCo or BYOL, which are known for their efficiency. This would help to assess the practicality of DINO for real-world applications. Additionally, the authors should explore techniques to optimize the computational efficiency of the proposed method, such as model pruning or quantization.

Finally, the paper needs to address the robustness of the proposed method to different datasets and tasks. The current evaluation is limited to ImageNet, which is a relatively small and well-studied dataset. To demonstrate the generalizability of the learned representations, the authors should evaluate DINO on a more diverse set of datasets, including those with different characteristics, such as different image resolutions, object categories, and background clutter. Furthermore, the authors should evaluate the performance of DINO on tasks beyond image classification, such as object detection, semantic segmentation, and image retrieval. This would provide a more comprehensive understanding of the capabilities of the proposed method. For example, the authors could evaluate DINO on the COCO dataset for object detection or the Pascal VOC dataset for semantic segmentation. This would help to assess the versatility of the learned representations and their applicability to real-world scenarios.

### Questions

Please see the weakness.

### Rating

8

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The reviewer has identified three main weaknesses: lack of comprehensive comparison, lack of analysis on computational cost and efficiency, and lack of exploration of robustness. I need to go through each of these and see if the paper provides sufficient information or if the reviewer's criticism is valid.

**Weakness 1: Lack of comprehensive comparison**

*   **Initial Categorization:** Methodological and Experimental. The reviewer is pointing out a gap in the experimental validation by not comparing against a broader set of baselines.
*   **Methodological Verification:** The paper focuses on introducing and analyzing DINO. While it mentions related work in the introduction and related work section, it doesn't have a dedicated "Experiments" section with comparisons. The experiments section focuses on evaluating DINO against other ViT architectures and self-supervised methods using k-NN, not against a wide range of SSL methods.
*   **Experimental Validation:** The "Experiments" section includes comparisons with other SSL frameworks like BYOL and MoCov2, but it doesn't include comparisons with methods that specifically use ViTs with different SSL techniques (e.g., contrastive learning with ViTs, masked image modeling with ViTs).

**Weakness 2: Lack of analysis on computational cost and efficiency**

*   **Initial Categorization:** Experimental. The reviewer is pointing out a missing analysis of the practical implications of the method.
*   **Methodological Verification:** The paper describes the DINO method but doesn't delve into its computational complexity or the cost of training and inference.
*   **Experimental Validation:** The "Experiments" section provides details on training epochs, batch size, and hardware, but there's no mention of training time, inference time, or memory usage. The "Compute Requirements" subsection in the "Ablation Study of DINO" section provides some information, but it's limited to ViT-S/16 and doesn't cover inference or a broader range of models.

**Weakness 3: Lack of exploration of robustness**

*   **Initial Categorization:** Experimental. The reviewer is pointing out a limitation in the experimental evaluation regarding the scope of datasets and tasks.
*   **Methodological Verification:** The paper focuses on image classification and k-NN evaluation. There's no discussion or experimentation on other tasks like object detection or segmentation.
*   **Experimental Validation:** The "Experiments" section primarily focuses on linear evaluation on ImageNet. While there are experiments on ViT instance segmentation and copy detection, these are still within the image understanding domain. There's no evaluation on datasets with different characteristics or tasks beyond image classification.

**Synthesis and Reflection:**

The reviewer's criticisms are valid. The paper lacks a comprehensive comparison with a broader range of self-supervised learning methods, especially those using ViTs. It also doesn't provide a detailed analysis of the computational cost and efficiency of DINO. Finally, the evaluation is primarily focused on image classification and doesn't explore the robustness of the learned representations on other tasks or datasets.
**Review 1 Weakness Analysis:**

1. **Weakness Statement:**
    [The paper lacks a comprehensive comparison with other self-supervised learning methods, particularly those that also utilize ViT models. The absence of a detailed comparison makes it difficult to assess the true novelty and effectiveness of the proposed DINO method relative to existing approaches. For example, a comparison with methods that use contrastive learning or masked image modeling with ViTs would be beneficial.]

    **Evidence Collection:**
    a) Method-related Evidence: The paper introduces DINO and compares it to other SSL frameworks like BYOL and MoCov2 in the "Comparing with the same architecture" section of the Experiments. However, these comparisons are limited to architectural differences (ResNet-50 vs. ViT-small) rather than different SSL *techniques* within ViT architectures.
    b) Experiment-related Evidence: The "Comparing with the same architecture" experiment compares DINO (ViT-small) with BYOL (ViT-small) and MoCov2 (ViT-small). The "Comparing across architectures" experiment compares DINO (ViT-small) with supervised ViT models and other SSL frameworks using ResNet-50. There are no experiments directly comparing DINO with other SSL methods that also utilize ViT models and employ different SSL techniques like contrastive learning or masked image modeling.

    **Literature Gap Analysis:**
    The paper cites relevant SSL works like BYOL and MoCov2, but it doesn't explicitly position DINO against other ViT-based SSL methods that might use techniques like contrastive learning or masked image modeling. Methods like SimCLR or BEiT, which are relevant to ViT-based SSL, are not included as direct baselines in the experimental section.

    **Validation Analysis:**
    The reviewer's criticism is valid. While the paper compares DINO against other SSL frameworks, the comparison is primarily focused on architectural differences within the ViT family. It lacks a direct comparison with other SSL methods that also utilize ViT architectures but employ different self-supervised learning techniques. This makes it difficult to fully assess the novelty and effectiveness of DINO relative to the broader landscape of ViT-based SSL.

    **Conclusion:**
    Validity status: **Valid**
    Confidence level: **High**
    Key supporting evidence: The experimental section lacks direct comparisons with ViT-based SSL methods employing contrastive learning or masked image modeling techniques.

2. **Weakness Statement:**
    [The paper does not provide a thorough analysis of the computational cost and efficiency of the proposed method. While the authors mention that DINO achieves state-of-the-art results, they do not discuss the computational resources required for training and inference, which is a critical factor for practical applications. A comparison of training time, memory usage, and inference speed with other self-supervised methods would be valuable.]

    **Evidence Collection:**
    a) Method-related Evidence: The paper describes the DINO method and its components (momentum encoder, projection head, cross-entropy loss) but doesn't provide a detailed analysis of its computational complexity.
    b) Experiment-related Evidence: The "Compute Requirements" subsection in the "Ablation Study of DINO" section provides some information on training time and batch size, but it's limited to ViT-S/16. There is no systematic analysis of training time, inference speed, or memory usage compared to other SSL methods. The paper mentions hardware specifications (1024 GPUs), but not the specific training time or inference speed.

    **Literature Gap Analysis:** While the paper cites relevant SSL works, it doesn't include a comparative analysis of the computational cost of DINO against these methods.

    **Validation Analysis:** The reviewer's criticism is valid. The paper lacks a thorough analysis of the computational cost and efficiency of DINO. While it mentions achieving state-of-the-art results, it doesn't provide the necessary details about training time, inference speed, and memory usage, especially in comparison to other SSL methods. This information is crucial for assessing the practical applicability of DINO.

    **Conclusion:**
    Validity status: **Valid**
    Confidence level: **High**
    Key supporting evidence: The paper lacks a systematic analysis of training time, inference speed, and memory usage compared to other SSL methods.

3. **Weakness Statement:**
    [The paper does not explore the robustness of the proposed method to different datasets and tasks. The evaluation is primarily focused on ImageNet, and it is unclear how well the learned representations generalize to other datasets or tasks, such as object detection or segmentation. An evaluation on a more diverse set of tasks would strengthen the paper's claims.]

    **Evidence Collection:**
    a) Method-related Evidence: The paper focuses on the self-supervised learning of ViT features and the application of DINO. The method description doesn't inherently limit its applicability to specific datasets or tasks.
    b) Experiment-related Evidence: The "Experiments" section primarily focuses on linear evaluation on ImageNet. While there are experiments on ViT instance segmentation and copy detection, these are still within the image understanding domain. There is no evaluation on datasets with different characteristics (e.g., different image resolutions, object categories, background clutter) or on tasks beyond image classification.

    **Literature Gap Analysis:** The paper doesn't discuss the generalizability of its findings to different datasets or tasks compared to other SSL methods.

    **Validation Analysis:** The reviewer's criticism is partially valid. While the paper does explore ViT instance segmentation and copy detection, the primary focus and the majority of the experiments are on ImageNet for linear evaluation. The robustness to different datasets and tasks beyond image classification is not thoroughly explored.

    **Conclusion:**
    Validity status: **Partially Valid**
    Confidence level: **Medium**
    Key supporting evidence: The primary evaluation is on ImageNet for linear classification. While other tasks are explored, the generalization to diverse datasets is not explicitly tested.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper delves into the self-supervised learning (SSL) capabilities of Vision Transformers (ViTs), a relatively novel area of exploration given the prevalence of CNNs in the field. The authors present a comprehensive analysis of ViT features, revealing that these features inherently contain explicit information about the semantic segmentation of images. This is a significant finding, as it suggests that ViTs, unlike CNNs, are not just implicitly learning representations but are actually encoding spatial information within their feature vectors. Furthermore, the authors demonstrate that these features perform exceptionally well when used with a simple k-Nearest Neighbors (k-NN) classifier, indicating that the learned representations are already highly discriminative and transferable. To further enhance the performance of ViTs in self-supervised learning, the authors introduce a novel approach called DINO (Distillation with No Labels). DINO leverages a teacher-student framework, where a momentum encoder acts as the teacher, guiding the learning process of a student network. This method is inspired by knowledge distillation techniques but is adapted for the self-supervised setting without explicit labels. The paper presents a thorough evaluation of DINO, showing that it achieves state-of-the-art results on the ImageNet dataset with a linear evaluation of a ViT-Base model. The authors also explore the impact of various design choices within the DINO framework, such as the choice of teacher network and the impact of different projection heads. The core contribution of this work lies in its detailed analysis of ViT features, the demonstration of their utility for semantic segmentation, and the introduction of the DINO method, which provides a simple yet effective approach for self-supervised learning with ViTs. The findings suggest that ViTs are a promising avenue for self-supervised learning, and the DINO method offers a practical way to leverage their potential. The paper's analysis of ViT features and the introduction of DINO represent a significant step forward in the field of self-supervised learning, particularly for vision tasks. The authors' work highlights the importance of exploring non-CNN architectures for self-supervised learning and provides a strong foundation for future research in this area. The paper is well-written and easy to follow, making the complex concepts accessible to a broad audience. The experimental results are compelling and provide strong evidence for the effectiveness of the proposed methods. Overall, this paper makes a valuable contribution to the field of self-supervised learning and provides a solid basis for further research into the use of ViTs for this purpose.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

3.0


## Strengths:

This paper presents several notable strengths that contribute to its overall impact and significance. First, the authors provide a thorough and insightful analysis of the self-supervised learning capabilities of Vision Transformers (ViTs). This analysis goes beyond simply demonstrating that ViTs can learn representations; it delves into the nature of these representations, revealing that they inherently contain explicit information about the semantic segmentation of images. This is a significant finding, as it suggests that ViTs are not just implicitly learning representations but are actually encoding spatial information within their feature vectors. This insight is crucial for understanding the potential of ViTs in self-supervised learning. Second, the authors demonstrate that these ViT features perform exceptionally well with a simple k-NN classifier. This finding is compelling because it suggests that the learned representations are already highly discriminative and transferable, which is a desirable property for self-supervised learning methods. The fact that a simple k-NN classifier can achieve such high performance indicates that the features are not only complex but also well-structured and informative. Third, the introduction of the DINO method is a significant contribution. DINO leverages a teacher-student framework, where a momentum encoder acts as the teacher, guiding the learning process of a student network. This approach is inspired by knowledge distillation techniques but is adapted for the self-supervised setting without explicit labels. The DINO method achieves state-of-the-art results on the ImageNet dataset with a linear evaluation of a ViT-Base model, demonstrating its effectiveness and potential. The authors also provide a detailed analysis of the DINO method, exploring the impact of various design choices within the framework. This thorough analysis makes the paper a valuable resource for researchers interested in self-supervised learning with ViTs. Finally, the paper is well-written and easy to follow. The authors present their findings in a clear and concise manner, making the complex concepts accessible to a broad audience. The experimental results are compelling and provide strong evidence for the effectiveness of the proposed methods. The paper's strengths lie in its insightful analysis of ViT features, the demonstration of their utility for semantic segmentation, the introduction of the DINO method, and the overall clarity and organization of the presentation.


## Weaknesses:

While this paper presents valuable contributions, there are several weaknesses that warrant careful consideration. The most significant limitation, as identified by multiple reviewers, is the lack of a comprehensive comparison with other self-supervised learning methods, particularly those that also utilize ViT models. While the paper compares DINO against other SSL frameworks like BYOL and MoCov2, these comparisons are primarily focused on architectural differences within the ViT family. The paper does not include a direct comparison with other SSL methods that also employ ViT architectures but use different self-supervised learning techniques, such as contrastive learning or masked image modeling. For instance, methods like SimCLR or BEiT, which are relevant to ViT-based SSL, are not included as direct baselines in the experimental section. This absence makes it difficult to fully assess the novelty and effectiveness of DINO relative to the broader landscape of ViT-based SSL. The paper's experimental section focuses on comparing DINO with other SSL frameworks using the same ViT architecture, but it does not explore how DINO compares to methods that use different SSL techniques within ViT models. This lack of comparison limits the ability to understand the specific advantages and disadvantages of DINO compared to existing approaches. This is a high-confidence issue, as the experimental section clearly lacks these comparisons. The second major weakness is the lack of a thorough analysis of the computational cost and efficiency of the proposed method. While the authors mention that DINO achieves state-of-the-art results, they do not discuss the computational resources required for training and inference. The paper provides some information on training time and batch size in the "Compute Requirements" subsection of the "Ablation Study of DINO" section, but this analysis is limited to ViT-S/16 and does not cover inference or a broader range of models. There is no systematic analysis of training time, inference speed, or memory usage compared to other SSL methods. This lack of analysis makes it difficult to assess the practical applicability of DINO, especially for real-world applications where computational resources are often limited. The paper mentions hardware specifications (1024 GPUs), but not the specific training time or inference speed. This is a high-confidence issue, as the paper clearly lacks a systematic analysis of computational cost. Finally, while the paper does explore ViT instance segmentation and copy detection, the primary focus and the majority of the experiments are on ImageNet for linear evaluation. The robustness of the learned representations to different datasets and tasks beyond image classification is not thoroughly explored. The paper does not evaluate DINO on datasets with different characteristics, such as different image resolutions, object categories, or background clutter. Furthermore, the evaluation is primarily focused on image classification and does not explore the performance of DINO on tasks beyond image classification, such as object detection or semantic segmentation. This limits the generalizability of the findings and raises questions about the versatility of the learned representations. While the paper does include experiments on ViT instance segmentation and copy detection, the primary focus on ImageNet for linear evaluation and the lack of evaluation on a more diverse set of tasks are limitations. This is a medium-confidence issue, as the paper does include some evaluation beyond image classification, but the scope is limited.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should include a more detailed comparison with existing self-supervised learning methods, particularly those employing Vision Transformers. This should not only focus on accuracy but also on computational cost, training time, and memory usage. Specifically, the authors should compare DINO with methods like SimCLR, MoCo, or BEiT, which are widely used in the field. This comparison should not only focus on accuracy but also on computational cost, training time, and memory usage. For instance, the authors could compare DINO with methods like SimCLR, MoCo, or BEiT, which are widely used in the field. This would help to contextualize the performance of DINO and highlight its specific advantages and disadvantages. Furthermore, the comparison should include a discussion of the architectural differences between DINO and other methods, and how these differences contribute to the observed performance. This would provide a more nuanced understanding of the proposed approach. Second, to address the lack of analysis on computational cost and efficiency, the authors should provide a detailed breakdown of the training and inference times, as well as the memory requirements of the proposed method. This analysis should be performed on a variety of hardware configurations to provide a comprehensive understanding of the computational requirements. The authors should also compare the computational cost of DINO with other self-supervised methods, including both training and inference. This comparison should include a discussion of the trade-offs between performance and computational cost. For example, the authors could compare the training time and memory usage of DINO with methods like MoCo or BYOL, which are known for their efficiency. This would help to assess the practicality of DINO for real-world applications. Additionally, the authors should explore techniques to optimize the computational efficiency of the proposed method, such as model pruning or quantization. Third, the paper needs to address the robustness of the proposed method to different datasets and tasks. The current evaluation is limited to ImageNet, which is a relatively small and well-studied dataset. To demonstrate the generalizability of the learned representations, the authors should evaluate DINO on a more diverse set of datasets, including those with different characteristics, such as different image resolutions, object categories, and background clutter. Furthermore, the authors should evaluate the performance of DINO on tasks beyond image classification, such as object detection, semantic segmentation, and image retrieval. This would provide a more comprehensive understanding of the capabilities of the proposed method. For example, the authors could evaluate DINO on the COCO dataset for object detection or the Pascal VOC dataset for semantic segmentation. This would help to assess the versatility of the learned representations and their applicability to real-world scenarios. Furthermore, the authors should analyze the limitations of the proposed method and discuss potential avenues for future research. This would help to identify areas where the proposed method could be improved and extended. These suggestions are concrete, actionable, and directly address the identified weaknesses, aiming to enhance the paper's overall impact and practical applicability.


## Questions:

Several key questions arise from my analysis of this paper, focusing on the core methodological choices and assumptions. First, how does the proposed DINO method compare to other self-supervised learning methods that also utilize ViT models, particularly those that employ contrastive learning or masked image modeling? The paper compares DINO to other SSL frameworks, but it lacks a direct comparison with methods that use different SSL techniques within ViT models. A more detailed comparison would help to contextualize the performance of DINO and highlight its specific advantages and disadvantages. Second, what is the computational cost and efficiency of the proposed method compared to other self-supervised methods? The paper provides some information on training time and batch size, but it lacks a systematic analysis of training time, inference speed, and memory usage compared to other SSL methods. A more detailed analysis of the computational cost would be valuable for assessing the practical applicability of DINO. Third, how robust are the learned representations to different datasets and tasks beyond image classification? The primary evaluation is on ImageNet, and while the paper explores ViT instance segmentation and copy detection, it does not evaluate DINO on a more diverse set of datasets or on tasks beyond image classification. A more thorough evaluation of the robustness of the learned representations would be valuable for assessing the generalizability of the proposed method. Fourth, what are the specific architectural differences between DINO and other SSL methods that contribute to the observed performance? The paper describes the DINO method but does not delve into the specific architectural choices that contribute to its performance. A more detailed analysis of the architectural differences would be valuable for understanding the underlying mechanisms of DINO. Finally, what are the limitations of the proposed method, and what are the potential avenues for future research? The paper does not explicitly discuss the limitations of DINO or potential avenues for future research. A more detailed discussion of the limitations would be valuable for identifying areas where the proposed method could be improved and extended. These questions are designed to target the core methodological choices and assumptions of the paper, aiming to clarify the uncertainties and provide a more comprehensive understanding of the proposed method.


## Rating:

6.5


## Confidence:

3.25


## Decision:

Accept
}