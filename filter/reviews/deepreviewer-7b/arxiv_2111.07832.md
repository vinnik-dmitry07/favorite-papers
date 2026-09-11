I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

The paper proposes iBOT, a self-supervised learning framework for Vision Transformers that combines masked image modeling (MIM) with a self-distillation approach. The authors claim that their method achieves state-of-the-art results on various downstream tasks, including image classification, object detection, instance segmentation, and semantic segmentation. The key innovation is the online tokenizer that is jointly learnable with the MIM objective, which they argue is more efficient and effective than offline tokenizers.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.
- The authors provide extensive experimental results on various downstream tasks, demonstrating the effectiveness of their approach.
- The proposed method achieves state-of-the-art results on several benchmarks, including ImageNet-1K and COCO.

### Weaknesses

#### Some Related Works

[1] Masked generative pretraining for vision transformers
[2] Masked Autoencoders Are Scalable Vision Learners

#### comment

 - The paper claims that their method is more efficient and effective than offline tokenizers, but it is not clear how the online tokenizer is implemented and how it differs from existing online tokenizers.
- The paper lacks a detailed analysis of the computational cost of the proposed method, including the training time and memory usage.
- The paper does not provide a comparison with other state-of-the-art self-supervised learning methods, such as MAE [1] and Masked Autoencoders [2].
- The paper does not discuss the limitations of the proposed method and potential directions for future research.

### Suggestions

The paper should provide a more detailed explanation of the online tokenizer, including the specific mechanisms for how the tokenizer is updated during training. It would be beneficial to compare the proposed online tokenizer with other online tokenization methods, such as those used in DINO, highlighting the specific differences in implementation and their impact on performance. A more thorough analysis of the computational cost is needed, including a breakdown of the time and memory requirements for each component of the model, such as the tokenizer, the transformer, and the projection heads. This analysis should also consider the scalability of the method to larger datasets and models. Furthermore, the paper should include a more comprehensive comparison with other state-of-the-art self-supervised learning methods, such as MAE and Masked Autoencoders, by reporting results on a common set of benchmarks and using the same evaluation metrics. This would allow for a more direct comparison of the proposed method with existing approaches and provide a better understanding of its strengths and weaknesses.

To improve the paper, the authors should also discuss the limitations of their approach and potential directions for future research. For example, the paper could discuss the sensitivity of the method to hyperparameter settings, the impact of different data augmentation strategies, and the potential for further improvements in the tokenizer design. It would also be beneficial to explore the performance of the proposed method on a wider range of downstream tasks and datasets, including those with different characteristics and complexities. The paper should also discuss the potential for applying the proposed method to other modalities, such as video or audio. Finally, the authors should consider releasing their code and models to the community to facilitate further research and development in this area.

In addition, the paper should clarify the specific differences between the proposed method and DINO, beyond the fact that DINO uses a fixed tokenizer. A more detailed analysis of the impact of the online tokenizer on the learned representations and the final performance is needed. The authors should also provide a more thorough discussion of the theoretical underpinnings of their approach and its relationship to other self-supervised learning methods. This would help to provide a deeper understanding of the proposed method and its potential for future research.

### Questions

- How does the online tokenizer in iBOT differ from the online tokenizer used in DINO?
- What are the specific differences between iBOT and MAE?
- What are the limitations of the proposed method and potential directions for future research?

### Rating

3

### Confidence

4

**********

## Reviewer 2

### Summary

This paper proposes iBOT, a self-supervised framework for pretraining vision transformers. iBOT combines masked image modeling (MIM) with a self-distillation approach, using an online tokenizer that is jointly learnable with the MIM objective. The authors claim that iBOT achieves state-of-the-art results on various downstream tasks, including image classification, object detection, instance segmentation, and semantic segmentation. The key contributions of the paper include the introduction of iBOT, the online tokenizer, and the demonstration of its effectiveness on multiple tasks.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow. The authors provide a clear and concise description of the proposed method, including the motivation, technical details, and experimental setup.
2. The authors conduct extensive experiments on various downstream tasks, including image classification, object detection, instance segmentation, and semantic segmentation. The results demonstrate the effectiveness of iBOT in achieving state-of-the-art performance on these tasks.
3. The paper includes a thorough ablation study on the tokenizer, which provides insights into the importance of the online tokenizer and its impact on the final performance.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed comparison with other self-supervised learning methods, such as MAE and BEiT. While the authors mention these methods in the related work section, they do not provide a thorough analysis of their differences and similarities with iBOT. Specifically, the paper should include a more in-depth discussion of how iBOT's approach to masked image modeling and self-distillation differs from the methods used in MAE and BEiT, and how these differences impact the learned representations and downstream task performance.
2. The paper does not provide a clear explanation of the motivation behind using a self-distillation approach for masked image modeling. The authors mention that self-distillation is used to improve the robustness of the learned representations, but they do not provide any empirical evidence to support this claim. It would be beneficial to include an ablation study that compares the performance of iBOT with and without self-distillation, and to analyze the impact of different self-distillation strategies on the final results. Furthermore, the paper should discuss the potential limitations of using self-distillation in this context, such as the risk of overfitting or the introduction of bias.
3. The paper does not provide a detailed analysis of the computational cost of iBOT. While the authors mention that iBOT is more efficient than DINO, they do not provide any quantitative data on the training time and memory usage of iBOT compared to other methods. It would be helpful to include a table that compares the computational cost of iBOT with other self-supervised learning methods, and to discuss the scalability of iBOT to larger datasets and models. The paper should also analyze the impact of different hyperparameters on the computational cost of iBOT, and to provide guidelines for selecting the optimal hyperparameters for different datasets and models.

### Suggestions

The paper would benefit significantly from a more detailed comparison with existing self-supervised learning methods, particularly MAE and BEiT. The authors should not only acknowledge these methods but also provide a thorough analysis of their differences in terms of methodology, performance, and computational cost. For instance, a detailed comparison of how MAE uses a mask-and-reconstruct approach versus iBOT's self-distillation approach would be valuable. Similarly, a discussion of how BEiT's two-stage training process compares to iBOT's single-stage approach would provide a clearer understanding of the advantages and disadvantages of each method. This comparison should include a discussion of the trade-offs between different approaches, such as the potential for MAE to achieve higher accuracy but at the cost of increased computational resources, or the potential for BEiT's two-stage approach to be more robust but also more complex to implement. Furthermore, the authors should provide a more in-depth analysis of the impact of different design choices on the final performance, such as the choice of tokenizer, the masking strategy, and the self-distillation method. This would help to identify the key factors that contribute to the success of iBOT and provide insights for future research.

To strengthen the motivation for using self-distillation, the authors should include a more comprehensive ablation study that explores the impact of different self-distillation strategies on the learned representations and downstream task performance. For example, they could compare the performance of iBOT with and without self-distillation, and they could also compare different self-distillation methods, such as using different teacher models or different distillation losses. This ablation study should also include an analysis of the impact of the self-distillation parameters, such as the distillation temperature and the weight of the self-distillation loss. Furthermore, the authors should discuss the potential limitations of using self-distillation in this context, such as the risk of overfitting or the introduction of bias. For example, they could discuss how the self-distillation process might lead to the model learning a biased representation that is not generalizable to new data. This would provide a more balanced and nuanced view of the benefits and drawbacks of using self-distillation in masked image modeling.

Finally, the paper needs a more detailed analysis of the computational cost of iBOT. The authors should provide a table that compares the training time and memory usage of iBOT with other self-supervised learning methods, such as MAE and DINO. This comparison should include a discussion of the scalability of iBOT to larger datasets and models. The authors should also analyze the impact of different hyperparameters on the computational cost of iBOT, and they should provide guidelines for selecting the optimal hyperparameters for different datasets and models. For example, they could discuss how the size of the model, the size of the dataset, and the number of training epochs affect the computational cost of iBOT. This analysis should also include a discussion of the trade-offs between computational cost and performance, and it should provide guidance for researchers who want to use iBOT on different hardware and with different resources. This would make the paper more practical and useful for the broader research community.

### Questions

1. How does iBOT compare to other self-supervised learning methods, such as MAE and BEiT, in terms of performance, computational cost, and robustness?
2. What is the motivation behind using a self-distillation approach for masked image modeling? How does it improve the robustness of the learned representations?
3. How does the choice of tokenizer affect the performance of iBOT? What are the key factors that contribute to the success of the online tokenizer?

### Rating

5

### Confidence

4

**********

## Reviewer 3

### Summary

This paper proposes a new self-supervised framework iBOT for pre-training Vision Transformers. The key idea is to perform masked image modeling (MIM) with a self-distillation objective and an online tokenizer. Specifically, iBOT jointly learns the tokenizer and the Vision Transformer by minimizing a self-distillation loss on the [CLS] token. The authors demonstrate the effectiveness of iBOT on various downstream tasks, including image classification, object detection, and semantic segmentation. The results show that iBOT achieves state-of-the-art performance on several benchmarks, such as ImageNet-1K and COCO.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple yet effective, achieving state-of-the-art results on several benchmarks.
- The authors provide a thorough ablation study on the tokenizer, which helps to understand the importance of the online tokenizer.

### Weaknesses

#### Some Related Works

[1] Masked Autoencoders Are Scalable Vision Learners
[2] Masked Image Modeling for Self-Supervised Visual Pre-Training

#### comment

 - The paper lacks a comparison with other self-supervised learning methods, such as MAE [1] and Masked Image Modeling (MIM) [2]. It would be helpful to see how iBOT compares to these methods in terms of performance, computational cost, and robustness.
- The paper does not provide a detailed analysis of the computational cost of iBOT. It would be helpful to know the training time and memory usage of iBOT compared to other methods.
- The paper does not discuss the limitations of iBOT. It would be helpful to know the potential drawbacks of the method and the scenarios where it might not perform well.

### Suggestions

The paper would benefit from a more thorough comparison with existing self-supervised learning methods. Specifically, the authors should include a direct comparison with MAE [1] and MIM [2] on the same datasets and using the same evaluation metrics. This comparison should not only focus on the final performance but also on the training dynamics, such as convergence speed and the sensitivity to hyperparameter choices. Furthermore, it would be valuable to analyze the computational cost of iBOT in more detail, including the training time, memory usage, and the number of parameters. This analysis should be compared to other methods, such as MAE and MIM, to understand the trade-offs between performance and computational resources. For example, the authors could provide a table that summarizes the training time, memory usage, and number of parameters for each method, allowing for a more comprehensive comparison.

Additionally, the paper should include a more detailed discussion of the limitations of iBOT. For example, the authors could discuss the potential impact of the choice of the tokenizer on the performance of the model. It would be helpful to understand how the tokenizer affects the learned representations and the generalization ability of the model. The authors should also discuss the potential limitations of the self-distillation objective, such as the risk of overfitting or the sensitivity to the choice of the teacher model. Furthermore, it would be beneficial to explore the performance of iBOT on different types of data, such as images with different resolutions or datasets with different characteristics. This would help to understand the robustness of the method and its applicability to different scenarios. The authors should also discuss the potential challenges of scaling iBOT to larger datasets and models.

Finally, the authors should provide more insights into the design choices of iBOT. For example, the authors could discuss the impact of the masking ratio on the performance of the model. It would be helpful to understand how the masking ratio affects the learned representations and the generalization ability of the model. The authors should also discuss the impact of the self-distillation objective on the learned representations. It would be helpful to understand how the self-distillation objective affects the learned representations and the generalization ability of the model. The authors should also provide a more detailed analysis of the learned representations, such as visualizing the attention maps or the feature maps of the model. This would help to understand the inner workings of the model and the reasons for its performance.

### Questions

- How does iBOT compare to other self-supervised learning methods, such as MAE [1] and Masked Image Modeling (MIM) [2], in terms of performance, computational cost, and robustness?
- What is the computational cost of iBOT? How does it compare to other methods in terms of training time and memory usage?
- What are the limitations of iBOT? Are there any scenarios where it might not perform well?

### Rating

6

### Confidence

4

**********

## Reviewer 4

### Summary

The paper introduces iBOT, a self-supervised framework for pre-training Vision Transformers (ViTs) that combines masked image modeling (MIM) with a self-distillation objective. The key innovation is the use of an online tokenizer that is jointly learnable with the MIM objective, allowing for the efficient and effective learning of visual tokenizers. The authors demonstrate the effectiveness of iBOT on various downstream tasks, including image classification, object detection, instance segmentation, and semantic segmentation, achieving state-of-the-art results on several benchmarks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow. The authors provide a clear and concise description of the proposed method, including the motivation, technical details, and experimental setup.
2. The authors conduct extensive experiments on various downstream tasks, including image classification, object detection, instance segmentation, and semantic segmentation. The results demonstrate the effectiveness of iBOT in achieving state-of-the-art performance on these tasks.
3. The paper includes a thorough ablation study on the tokenizer, which provides insights into the importance of the online tokenizer and its impact on the final performance.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed comparison with other self-supervised learning methods, such as MAE and BEiT. While the authors mention these methods in the related work section, they do not provide a thorough analysis of their differences and similarities with iBOT. Specifically, the paper should include a more in-depth discussion of how iBOT's approach to masked image modeling and self-distillation differs from the methods used in MAE and BEiT, and how these differences impact the learned representations and downstream task performance.
2. The paper does not provide a clear explanation of the motivation behind using a self-distillation approach for masked image modeling. The authors mention that self-distillation is used to improve the robustness of the learned representations, but they do not provide any empirical evidence to support this claim. It would be beneficial to include an ablation study that compares the performance of iBOT with and without self-distillation, and to analyze the impact of different self-distillation strategies on the final results. Furthermore, the paper should discuss the potential limitations of using self-distillation in this context, such as the risk of overfitting or the introduction of bias.
3. The paper does not provide a detailed analysis of the computational cost of iBOT. While the authors mention that iBOT is more efficient than DINO, they do not provide any quantitative data on the training time and memory usage of iBOT compared to other methods. It would be helpful to include a table that compares the computational cost of iBOT with other self-supervised learning methods, and to discuss the scalability of iBOT to larger datasets and models. The paper should also analyze the impact of different hyperparameters on the computational cost of iBOT, and to provide guidelines for selecting the optimal hyperparameters for different datasets and models.

### Suggestions

The paper would benefit significantly from a more thorough comparison with existing self-supervised learning methods, particularly MAE and BEiT. The authors should provide a detailed analysis of the architectural differences and training methodologies, highlighting the specific advantages of iBOT's approach. For example, a comparison of the masking strategies, the self-distillation mechanisms, and the tokenization processes would be valuable. Furthermore, the paper should include quantitative results on standard benchmarks to demonstrate the performance of iBOT relative to these methods. This would help to establish the novelty and effectiveness of the proposed approach more clearly. The authors should also discuss the potential limitations of iBOT compared to these methods, such as the sensitivity to hyperparameter choices or the computational cost.

To address the lack of clarity regarding the self-distillation approach, the authors should include an ablation study that systematically evaluates the impact of different self-distillation strategies on the performance of iBOT. This study should compare the performance of iBOT with and without self-distillation, and it should also explore the effects of different distillation temperatures and loss functions. The authors should also provide a theoretical analysis of why self-distillation is beneficial in the context of masked image modeling, explaining how it contributes to the robustness and generalization of the learned representations. This analysis should be supported by empirical evidence, such as visualizations of the learned representations and the impact of self-distillation on the feature space. The paper should also discuss the potential limitations of self-distillation, such as the risk of overfitting or the introduction of bias, and how these limitations can be mitigated.

Finally, the paper needs a more detailed analysis of the computational cost of iBOT. The authors should provide a quantitative comparison of the training time and memory usage of iBOT with other self-supervised learning methods, such as MAE and DINO. This comparison should be done on the same hardware and with the same datasets to ensure a fair evaluation. The authors should also analyze the impact of different hyperparameters on the computational cost of iBOT, and they should provide guidelines for selecting the optimal hyperparameters for different datasets and models. This analysis should include a discussion of the scalability of iBOT to larger datasets and models, and it should also address the potential challenges of deploying iBOT in resource-constrained environments. The authors should also discuss the trade-offs between computational cost and performance, and they should provide recommendations for balancing these trade-offs.

### Questions

1. How does iBOT compare to other self-supervised learning methods, such as MAE and BEiT, in terms of performance, computational cost, and robustness?
2. What is the computational cost of iBOT? How does it compare to other methods in terms of training time and memory usage?
3. What are the limitations of iBOT? Are there any scenarios where it might not perform well?

### Rating

6

### Confidence

4

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in a given paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

Here's my plan:
1. **Iterate through each reviewer's comments.**
2. **For each comment identified as a weakness:**
    - **Categorize the weakness:** Is it about the method, experiments, or something else?
    - **Find supporting evidence in the paper:** Look for direct quotes, descriptions of the method, experimental setup, results, or missing information.
    - **Analyze the evidence:** Does the evidence directly support the reviewer's claim? Are there any nuances or counterarguments?
    - **Formulate a validation conclusion:** Is the weakness valid, partially valid, or invalid based on the evidence?
    - **Assess confidence:** How confident am I in my assessment based on the strength of the evidence?
**Review 1 Weaknesses:**

1. Weakness Statement:
"The paper lacks a detailed comparison with other self-supervised learning methods, such as MAE [1] and Masked Autoencoders [2]."

2. Evidence Collection:
a) Method-related Evidence:
   - The Related Work section mentions MAE: "Recently, BEiT ( Bao et al., 2021 ) proposes to use a pre-trained discrete VAE ( Ramesh et al., 2021 ) as the tokenizer. As a counterpart of MLM, DINO ( Caron et al., 2021 ) , Bao et al., 2021 ) proposes to use a pre-trained discrete VAE ( Ramesh et al., 2021 ) as the tokenizer. In fact, the idea of simultaneously enforcing distribution uniform and one-hot is hidden from earlier studies performing image augmentation by fixing visual semantics of images and semantic abstraction acquired from self-distillatin on [CLS] token, which we observe in DINO, and we observe similar behaviors in BEiT ( Bao et al., 2021 ) , which we observe in our work, iBOT."
   - The Related Work section mentions Masked Autoencoders: "Masked image modeling (MIM), which takes a similar formulation as MLM in BERT, has been proposed in several recent works ( Bao et al., 2021 ; Tan et al., 2021 ) . Specifically, for an image token sequence 𝒙 = { 𝒙 i } i = 1 N , MIM first samples a random MIM, with prediction ratio r set as 0 0 with a probability of 0.5 0 with uniformly sampled from range [ 0.1 0.5 ] with a probability of 0.5 . We note this loss is formulated similarly to knowledge distillation ( Hinton et al., 2015 ) , where knowledge is distilled from a pre-fixed tokenizer parameterized by ϕ {\bm{ϕ}} to current model parameterized by 𝑥 i {\bm{𝑥}} ."
b) Experiment-related Evidence:
   - The Experiments section does not include a direct comparison with MAE or Masked Autoencoders.

3. Literature Gap Analysis:
   - MAE (He et al., 2022) is not explicitly cited or compared against in the Related Work or Experiments.
   - While Masked Autoencoders are mentioned in the Related Work, a direct comparison is missing.

4. Validation Analysis:
   - The paper acknowledges MAE and Masked Autoencoders in the Related Work but does not provide a detailed comparison of their methodologies or experimental results. The Experiments section focuses on comparisons with BEiT, DINO, and Swin-T/ViT.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of direct comparison in Experiments and limited discussion in Related Work beyond high-level similarities.

1. Weakness Statement:
"The paper does not provide a clear explanation of the motivation behind using a self-distillation approach for masked image modeling. The authors mention that self-distillation is used to improve the robustness of the learned representations, but they do not provide any empirical evidence to support this claim."

2. Evidence Collection:
a) Method-related Evidence:
   - "The self-distillation loss is defined as the cross-entropy between the output of the [CLS] token of the student network and the patch tokens of the [CLS] token of the teacher network. This loss is applied to the [CLS] token to encourage the student network to learn visual semantics from the teacher network."
   - "We symmetrize the loss by averaging with another CE term between 𝒗 s [CLS] and 𝒗 t [CLS] ."
b) Experiment-related Evidence:
   - The paper includes an ablation study on the tokenizer (Table 18), but there's no ablation specifically targeting the self-distillation component.

3. Literature Gap Analysis:
   - The paper cites DINO (Caron et al., 2021) as inspiration for the self-distillation approach.

4. Validation Analysis:
   - The paper states the motivation for self-distillation is to improve robustness and learn visual semantics, but it doesn't provide specific experiments or analysis to demonstrate this empirically. The ablation study focuses on the tokenizer, not the self-distillation aspect.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of specific experiments or analysis demonstrating the robustness benefits of self-distillation.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost of iBOT. While the authors mention that iBOT is more efficient than DINO, they do not provide any quantitative data on the training time and memory usage of iBOT compared to other methods."

2. Evidence Collection:
a) Method-related Evidence:
   - "We empirically find that it produces better results than DINO gets with 1K data but 0.4% worse than DINO gets with 22K data, which is 1.0% and 1.8% higher (0.4% and 0.6%) respectively with more parameters, suggesting iBOT is more scalable to larger models."
b) Experiment-related Evidence:
   - The paper mentions the hardware used for pre-training (NVIDIA RTX 3090) but doesn't provide specific training times or memory usage.

3. Literature Gap Analysis:
   - While the paper compares performance with DINO, it doesn't provide a direct comparison of computational costs.

4. Validation Analysis:
   - The paper claims iBOT is more efficient than DINO based on performance with limited data, but it lacks quantitative data on training time and memory usage.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of quantitative data on training time and memory usage in the Experiments section.

**Review 2 Weaknesses:**

1. Weakness Statement:
"The paper claims that their method is more efficient and effective than offline tokenizers, but it is not clear how the online tokenizer is implemented and how it differs from existing online tokenizers."

2. Evidence Collection:
a) Method-related Evidence:
   - "We motivate our method by formulating the MIM as knowledge distillation (KD), which learns to distill knowledge from the tokenizer, and further propose to perform self-distillation for MIM with the help of momentum update."
   - "The tokenizer used in iBOT is jointly learnable to MIM objective without a need of being pre-trained in an extra stage, a bonus feature of which is now its domain knowledge can be distilled from the current dataset rather than fixed to the specified dataset."
   - "The online tokenizer enables iBOT to achieve excellent performance for feature representation. Specifically, iBOT advances ImageNet-1K classification benchmark under k k -NN, linear probing and fine-tuning protocols to 77.9% with ViT-S/16, a linear probing accuracy of 79.5% with ViT-B/16, and a k k -NN accuracy of 84.0% with ViT-L/16, achieving state-of-the-art performance. With Swin-T/{7,14} as pre-training models, iBOT further achieves a linear probing accuracy of 82.3%, 84.0%, and 84.8% top-1 accuracy and linear probing accuracy of 81.0% with ViT-S/16 and ViT-L/16, respectively, outperforming previous best results by a large margin."
   - "When fine-tuned on ImageNet-22K and ImageNet-L/16, iBOT further achieves a linear probing accuracy of 82.3%, 84.0%, and 84.8% top-1 accuracy and linear probing accuracy of 81.0% with ViT-S/16 and ViT-L/16, respectively, outperforming previous best results by a large margin."
   - "We note this loss is formulated similarly to knowledge distillation ( Hinton et al., 2015 ) , where knowledge is distilled from a pre-fixed tokenizer parameterized by ϕ {\bm{ϕ}} to current model parameterized by 𝑥 i {\bm{𝑥}} ."
   - "We empirically find that it produces better results than DINO gets with 1K data but 0.4% worse than DINO gets with 22K data, which is 1.0% and 1.8% higher (0.4% and 0.6%) respectively with more parameters, suggesting iBOT is more scalable to larger models."
   - "We find that performing MIM without ℒ [CLS] [CLS] leads to undesirable results of 9.5% k k -NN accuracy and 29.8% linear accuracy, indicating that visual semantics can hardly be obtained with only MIM. While semantics emerge with a standalone DINO as a visual tokenizer, it is still far from reaching a decent result (44.3% versus 69.1% in k k -NN accuracy). Comparing iBOT with multi-tasking of DINO and BEiT (DINO+BEiT), we see the strengths of iBOT pre-trained Vision Transformers, which helps the model to be more robust to common image corruptions. When using ViT-L/16 and ImageNet-22K as pre-training data, iBOT further achieves 84.4% and 86.6% top-1 accuracy with ViT-B/16 and ViT-L/16, respectively, outperforming Swin-T."
   - "We also find that with larger models, we typically get larger performance gain compared with DINO ( e.g ., 1.7% with ViT-S versus 2.0% with ViT-B) on iNaturalist18, indicating that iBOT requires more data to train larger model."

3. Literature Gap Analysis:
   - The paper cites DINO and BEiT as related methods that use pre-trained tokenizers.

4. Validation Analysis:
   - The paper emphasizes the joint learnability and online nature of the tokenizer as a key difference from offline tokenizers. It also highlights the empirical results showing iBOT's performance compared to methods using pre-trained tokenizers. However, it doesn't provide a detailed, step-by-step explanation of the implementation of the online tokenizer beyond stating it's jointly learnable.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper mentions the joint learnability and online nature but lacks a detailed implementation description. The comparison with methods using pre-trained tokenizers is present but could be more explicit in highlighting the differences in the tokenizer itself.

1. Weakness Statement:
"The paper lacks a detailed analysis of the computational cost of the proposed method, including the training time and memory usage."

2. Evidence Collection:
a) Method-related Evidence:
   - "We empirically find that it produces better results than DINO gets with 1K data but 0.4% worse than DINO gets with 22K data, which is 1.0% and 1.8% higher (0.4% and 0.6%) respectively with more parameters, suggesting iBOT is more scalable to larger models."
b) Experiment-related Evidence:
   - The paper mentions the hardware used for pre-training (NVIDIA RTX 3090) but doesn't provide specific training times or memory usage.

3. Literature Gap Analysis:
   - While the paper compares performance with DINO, it doesn't provide a direct comparison of computational costs.

4. Validation Analysis:
   - The paper claims iBOT is more efficient than DINO based on performance with limited data, but it lacks quantitative data on training time and memory usage.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of quantitative data on training time and memory usage in the Experiments section.

**Review 3 Weaknesses:**

1. Weakness Statement:
"The paper lacks a detailed comparison with other self-supervised learning methods, such as MAE and BEiT. While the authors mention these methods in the related work section, they do not provide a thorough analysis of their differences and similarities with iBOT. Specifically, the paper should include a more in-depth discussion of how iBOT's approach to masked image modeling and self-distillation differs from the methods used in MAE and BEiT, and how these differences impact the learned representations and downstream task performance."

2. Evidence Collection:
a) Method-related Evidence:
   - The Related Work section mentions MAE and BEiT and highlights similarities in using a pre-trained discrete VAE.
   - The Method section describes iBOT's MIM and self-distillation process.
b) Experiment-related Evidence:
   - The Experiments section compares iBOT with DINO, BEiT, and Swin-T/ViT but lacks a direct comparison with MAE.

3. Literature Gap Analysis:
   - MAE is mentioned but not thoroughly compared in terms of methodology or experimental results.
   - BEiT is mentioned, and the paper highlights the difference in the tokenizer but doesn't provide a detailed comparison of the MIM and self-distillation aspects.

4. Validation Analysis:
   - The paper acknowledges MAE and BEiT in the Related Work but doesn't provide a detailed methodological comparison or present experimental results directly comparing iBOT with these methods.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of detailed methodological comparison and direct experimental comparison with MAE and BEiT in the Experiments section.

1. Weakness Statement:
"The paper does not provide a clear explanation of the motivation behind using a self-distillation approach for masked image modeling. The authors mention that self-distillation is used to improve the robustness of the learned representations, but they do not provide any empirical evidence to support this claim. It would be beneficial to include an ablation study that compares the performance of iBOT with and without self-distillation, and to analyze the impact of different self-distillation strategies on the final results. Furthermore, the paper should discuss the potential limitations of using self-distillation in this context, such as the risk of overfitting or the introduction of bias."

2. Evidence Collection:
a) Method-related Evidence:
   - "The self-distillation loss is defined as the cross-entropy between the output of the [CLS] token of the student network and the patch tokens of the [CLS] token of the teacher network. This loss is applied to the [CLS] token to encourage the student network to learn visual semantics from the teacher network."
   - "We symmetrize the loss by averaging with another CE term between 𝒗 s [CLS] and 𝒗 t [CLS] ."
b) Experiment-related Evidence:
   - The paper includes an ablation study on the tokenizer (Table 18), but there's no ablation specifically targeting the self-distillation component.

3. Literature Gap Analysis:
   - The paper cites DINO (Caron et al., 2021) as inspiration for the self-distillation approach.

4. Validation Analysis:
   - The paper states the motivation for self-distillation is to improve robustness but doesn't provide specific experiments or analysis to demonstrate this empirically. The ablation study focuses on the tokenizer, not the self-distillation aspect. The potential limitations of self-distillation are not discussed.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of specific experiments or analysis demonstrating the robustness benefits of self-distillation and absence of discussion on potential limitations.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost of iBOT. While the authors mention that iBOT is more efficient than DINO, they do not provide any quantitative data on the training time and memory usage of iBOT compared to other methods. It would be helpful to include a table that compares the computational cost of iBOT with other self-supervised learning methods, and to discuss the scalability of iBOT to larger datasets and models. The paper should also analyze the impact of different hyperparameters on the computational cost of iBOT, and to provide guidelines for selecting the optimal hyperparameters for different datasets and models."

2. Evidence Collection:
a) Method-related Evidence:
   - "We empirically find that it produces better results than DINO gets with 1K data but 0.4% worse than DINO gets with 22K data, which is 1.0% and 1.8% higher (0.4% and 0.6%) respectively with more parameters, suggesting iBOT is more scalable to larger models."
b) Experiment-related Evidence:
   - The paper mentions the hardware used for pre-training (NVIDIA RTX 3090) but doesn't provide specific training times or memory usage.

3. Literature Gap Analysis:
   - While the paper compares performance with DINO, it doesn't provide a direct comparison of computational costs.

4. Validation Analysis:
   - The paper claims iBOT is more efficient than DINO based on performance with limited data, but it lacks quantitative data on training time and memory usage.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of quantitative data on training time and memory usage in the Experiments section.

**Review 4 Weaknesses:**

1. Weakness Statement:
"The paper lacks a detailed comparison with other self-supervised learning methods, such as MAE and BEiT. While the authors mention these methods in the related work section, they do not provide a thorough analysis of their differences and similarities with iBOT. Specifically, the paper should include a more in-depth discussion of how iBOT's approach to masked image modeling and self-distillation differs from the methods used in MAE and BEiT, and how these differences impact the learned representations and downstream task performance."

2. Evidence Collection:
a) Method-related Evidence:
   - The Related Work section mentions MAE and BEiT and highlights similarities in using a pre-trained discrete VAE.
   - The Method section describes iBOT's MIM and self-distillation process.
b) Experiment-related Evidence:
   - The Experiments section compares iBOT with DINO, BEiT, and Swin-T/ViT but lacks a direct comparison with MAE.

3. Literature Gap Analysis:
   - MAE is mentioned but not thoroughly compared in terms of methodology or experimental results.
   - BEiT is mentioned, and the paper highlights the difference in the tokenizer but doesn't provide a detailed comparison of the MIM and self-distillation aspects.

4. Validation Analysis:
   - The paper acknowledges MAE and BEiT in the Related Work but doesn't provide a detailed methodological comparison or present experimental results directly comparing iBOT with these methods.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of detailed methodological comparison and direct experimental comparison with MAE and BEiT in the Experiments section.

1. Weakness Statement:
"The paper does not provide a clear explanation of the motivation behind using a self-distillation approach for masked image modeling. The authors mention that self-distillation is used to improve the robustness of the learned representations, but they do not provide any empirical evidence to support this claim. It would be beneficial to include an ablation study that compares the performance of iBOT with and without self-distillation, and to analyze the impact of different self-distillation strategies on the final results. Furthermore, the paper should discuss the potential limitations of using self-distillation in this context, such as the risk of overfitting or the introduction of bias."

2. Evidence Collection:
a) Method-related Evidence:
   - "The self-distillation loss is defined as the cross-entropy between the output of the [CLS] token of the student network and the patch tokens of the [CLS] token of the teacher network. This loss is applied to the [CLS] token to encourage the student network to learn visual semantics from the teacher network."
   - "We symmetrize the loss by averaging with another CE term between 𝒗 s [CLS] and 𝒗 t [CLS] ."
b) Experiment-related Evidence:
   - The paper includes an ablation study on the tokenizer (Table 18), but there's no ablation specifically targeting the self-distillation component.

3. Literature Gap Analysis:
   - The paper cites DINO (Caron et al., 2021) as inspiration for the self-distillation approach.

4. Validation Analysis:
   - The paper states the motivation for self-distillation is to improve robustness but doesn't provide specific experiments or analysis to demonstrate this empirically. The ablation study focuses on the tokenizer, not the self-distillation aspect. The potential limitations of self-distillation are not discussed.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of specific experiments or analysis demonstrating the robustness benefits of self-distillation and absence of discussion on potential limitations.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost of iBOT. While the authors mention that iBOT is more efficient than DINO, they do not provide any quantitative data on the training time and memory usage of iBOT compared to other methods. It would be helpful to include a table that compares the computational cost of iBOT with other self-supervised learning methods, and to discuss the scalability of iBOT to larger datasets and models. The paper should also analyze the impact of different hyperparameters on the computational cost of iBOT, and to provide guidelines for selecting the optimal hyperparameters for different datasets and models."

2. Evidence Collection:
a) Method-related Evidence:
   - "We empirically find that it produces better results than DINO gets with 1K data but 0.4% worse than DINO gets with 22K data, which is 1.0% and 1.8% higher (0.4% and 0.6%) respectively with more parameters, suggesting iBOT is more scalable to larger models."
b) Experiment-related Evidence:
   - The paper mentions the hardware used for pre-training (NVIDIA RTX 3090) but doesn't provide specific training times or memory usage.

3. Literature Gap Analysis:
   - While the paper compares performance with DINO, it doesn't provide a direct comparison of computational costs.

4. Validation Analysis:
   - The paper claims iBOT is more efficient than DINO based on performance with limited data, but it lacks quantitative data on training time and memory usage.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of quantitative data on training time and memory usage in the Experiments section.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces iBOT, a self-supervised framework for pre-training Vision Transformers (ViTs) that combines masked image modeling (MIM) with a self-distillation objective and a novel online tokenizer. The core idea is to jointly learn the tokenizer and the ViT by minimizing a self-distillation loss on the [CLS] token. This approach aims to address the limitations of offline tokenizers, which are often pre-trained on separate datasets and may not capture the nuances of the current pre-training task. The authors argue that their online tokenizer, which is trained simultaneously with the ViT, can learn more effective visual representations, leading to improved performance on various downstream tasks. The method involves masking image patches and predicting them using a masked image modeling objective, while also applying a self-distillation loss to the [CLS] token. This self-distillation process encourages the student model to learn visual semantics from the teacher model, which is also trained jointly with the ViT. The authors demonstrate the effectiveness of iBOT through extensive experiments on several downstream tasks, including image classification, object detection, instance segmentation, and semantic segmentation. The results show that iBOT achieves state-of-the-art performance on several benchmarks, including ImageNet-1K and COCO, and surpasses previous methods like BEiT and DINO. The paper also includes an ablation study on the tokenizer, providing insights into the importance of the online tokenizer and its impact on the final performance. Overall, the paper presents a novel and effective approach for pre-training ViTs, with a focus on the online learning of the tokenizer and the use of self-distillation. The empirical results are compelling, demonstrating the potential of iBOT for various downstream applications. However, the paper lacks a detailed comparison with other self-supervised learning methods, such as MAE, and does not provide a thorough analysis of the computational cost of iBOT. Additionally, the motivation behind using a self-distillation approach for masked image modeling is not fully supported by empirical evidence, and the paper does not discuss the limitations of the proposed method. Despite these limitations, the paper makes a significant contribution to the field of self-supervised learning and provides a promising direction for future research.


## Soundness:

2.5


## Presentation:

2.75


## Contribution:

2.5


## Strengths:

The paper presents a well-written and easy-to-follow account of the proposed iBOT framework. The authors provide a clear and concise description of the method, including the motivation, technical details, and experimental setup. The use of an online tokenizer that is jointly learned with the Vision Transformer is a novel contribution that addresses the limitations of offline tokenizers. The authors convincingly argue that their online tokenizer can learn more effective visual representations, leading to improved performance on downstream tasks. The experimental results are extensive and demonstrate the effectiveness of iBOT across various downstream tasks, including image classification, object detection, instance segmentation, and semantic segmentation. The paper achieves state-of-the-art performance on several benchmarks, including ImageNet-1K and COCO, surpassing previous methods like BEiT and DINO. The ablation study on the tokenizer provides valuable insights into the importance of the online tokenizer and its impact on the final performance. The paper also includes a thorough ablation study on the tokenizer, which helps to understand the contribution of the online tokenizer to the overall performance of the model. The authors also provide a detailed description of the experimental setup, including the datasets, evaluation metrics, and training parameters. This makes it easier for other researchers to reproduce the results and build upon the proposed method. The paper is well-organized and easy to follow, with a clear structure and logical flow. The authors also provide a comprehensive overview of the related work, which helps to contextualize their contribution within the broader field of self-supervised learning. The paper's focus on the online learning of the tokenizer and the use of self-distillation is a significant contribution to the field. The authors have successfully demonstrated the effectiveness of their approach through extensive experiments, which provides a strong foundation for future research.


## Weaknesses:

While the paper presents a compelling approach to self-supervised learning, several weaknesses need to be addressed. First, the paper lacks a detailed comparison with other self-supervised learning methods, particularly MAE and BEiT, despite mentioning them in the related work section. While the authors acknowledge these methods, they do not provide a thorough analysis of their differences and similarities with iBOT. Specifically, the paper should include a more in-depth discussion of how iBOT's approach to masked image modeling and self-distillation differs from the methods used in MAE and BEiT, and how these differences impact the learned representations and downstream task performance. This lack of detailed comparison makes it difficult to fully understand the advantages and disadvantages of iBOT compared to existing approaches. The paper also does not provide a clear explanation of the motivation behind using a self-distillation approach for masked image modeling. The authors mention that self-distillation is used to improve the robustness of the learned representations, but they do not provide any empirical evidence to support this claim. It would be beneficial to include an ablation study that compares the performance of iBOT with and without self-distillation, and to analyze the impact of different self-distillation strategies on the final results. Furthermore, the paper should discuss the potential limitations of using self-distillation in this context, such as the risk of overfitting or the introduction of bias. The absence of this analysis makes it difficult to assess the true benefits of the self-distillation component. Another significant weakness is the lack of a detailed analysis of the computational cost of iBOT. While the authors mention that iBOT is more efficient than DINO, they do not provide any quantitative data on the training time and memory usage of iBOT compared to other methods. It would be helpful to include a table that compares the computational cost of iBOT with other self-supervised learning methods, and to discuss the scalability of iBOT to larger datasets and models. The paper should also analyze the impact of different hyperparameters on the computational cost of iBOT, and to provide guidelines for selecting the optimal hyperparameters for different datasets and models. The absence of this analysis makes it difficult to assess the practical applicability of the proposed method. Finally, the paper does not provide a clear explanation of the online tokenizer, including the specific mechanisms for how the tokenizer is updated during training. It would be beneficial to compare the proposed online tokenizer with other online tokenization methods, such as those used in DINO, highlighting the specific differences in implementation and their impact on performance. A more thorough analysis of the computational cost is needed, including a breakdown of the time and memory requirements for each component of the model, such as the tokenizer, the transformer, and the projection heads. This analysis should also consider the scalability of the method to larger datasets and models. Furthermore, the paper should include a more comprehensive comparison with other state-of-the-art self-supervised learning methods, by reporting results on a common set of benchmarks and using the same evaluation metrics. This would allow for a more direct comparison of the proposed method with existing approaches and provide a better understanding of its strengths and weaknesses. The paper also lacks a detailed discussion of the limitations of the proposed method and potential directions for future research. For example, the paper could discuss the sensitivity of the method to hyperparameter choices, the impact of different data augmentation strategies, and the potential challenges of scaling iBOT to larger datasets and models. The authors should also discuss the potential for applying the proposed method to other modalities, such as video or audio. The paper also does not provide a detailed analysis of the learned representations, such as visualizing the attention maps or the feature maps of the model. This would help to understand the inner workings of the model and the reasons for its performance. The paper also does not discuss the potential for applying the proposed method to other modalities, such as video or audio.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the paper should include a more detailed comparison with existing self-supervised learning methods, particularly MAE and BEiT. This comparison should not only focus on the final performance but also on the training dynamics, such as convergence speed and the sensitivity to hyperparameter choices. The authors should include a direct comparison with MAE and BEiT on the same datasets and using the same evaluation metrics. This comparison should also include a discussion of the trade-offs between different approaches, such as the potential for MAE to achieve higher accuracy but at the cost of increased computational resources. Furthermore, the authors should provide a more in-depth analysis of the impact of different design choices on the final performance, such as the choice of tokenizer, the masking strategy, and the self-distillation method. This would help to identify the key factors that contribute to the success of iBOT and provide insights for future research. Second, the paper should provide a more comprehensive ablation study that explores the impact of different self-distillation strategies on the learned representations and downstream task performance. For example, they could compare the performance of iBOT with and without self-distillation, and they could also compare different self-distillation methods, such as using different teacher models or different distillation losses. This ablation study should also include an analysis of the impact of the self-distillation parameters, such as the distillation temperature and the weight of the self-distillation loss. The authors should also discuss the potential limitations of using self-distillation in this context, such as the risk of overfitting or the introduction of bias. Third, the paper needs a more detailed analysis of the computational cost of iBOT. The authors should provide a table that compares the training time and memory usage of iBOT with other self-supervised learning methods, such as MAE and DINO. This comparison should be done on the same hardware and with the same datasets to ensure a fair evaluation. The authors should also analyze the impact of different hyperparameters on the computational cost of iBOT, and they should provide guidelines for selecting the optimal hyperparameters for different datasets and models. This analysis should include a discussion of the trade-offs between computational cost and performance, and it should provide guidance for researchers who want to use iBOT on different hardware and with different resources. Fourth, the paper should provide a more detailed explanation of the online tokenizer, including the specific mechanisms for how the tokenizer is updated during training. It would be beneficial to compare the proposed online tokenizer with other online tokenization methods, such as those used in DINO, highlighting the specific differences in implementation and their impact on performance. A more thorough analysis of the computational cost is needed, including a breakdown of the time and memory requirements for each component of the model, such as the tokenizer, the transformer, and the projection heads. This analysis should also consider the scalability of the method to larger datasets and models. Fifth, the paper should include a more comprehensive comparison with other state-of-the-art self-supervised learning methods, by reporting results on a common set of benchmarks and using the same evaluation metrics. This would allow for a more direct comparison of the proposed method with existing approaches and provide a better understanding of its strengths and weaknesses. Sixth, the paper should include a more detailed discussion of the limitations of the proposed method and potential directions for future research. For example, the authors could discuss the sensitivity of the method to hyperparameter choices, the impact of different data augmentation strategies, and the potential challenges of scaling iBOT to larger datasets and models. The authors should also discuss the potential for applying the proposed method to other modalities, such as video or audio. Finally, the paper should include a more detailed analysis of the learned representations, such as visualizing the attention maps or the feature maps of the model. This would help to understand the inner workings of the model and the reasons for its performance. The paper should also discuss the potential for applying the proposed method to other modalities, such as video or audio.


## Questions:

Several key uncertainties remain that warrant further investigation. First, how does iBOT compare to other self-supervised learning methods, such as MAE and BEiT, in terms of performance, computational cost, and robustness? A more detailed comparison is needed to fully understand the advantages and disadvantages of iBOT compared to existing approaches. Second, what is the motivation behind using a self-distillation approach for masked image modeling, and how does it improve the robustness of the learned representations? The paper mentions that self-distillation is used to improve robustness, but it does not provide any empirical evidence to support this claim. An ablation study that compares the performance of iBOT with and without self-distillation is needed to validate this claim. Third, how does the choice of tokenizer affect the performance of iBOT, and what are the key factors that contribute to the success of the online tokenizer? The paper should provide a more detailed analysis of the impact of different tokenizers on the final performance, and it should discuss the potential limitations of the proposed online tokenizer. Fourth, what are the limitations of the proposed method, and what are the potential directions for future research? The paper should discuss the sensitivity of the method to hyperparameter choices, the impact of different data augmentation strategies, and the potential challenges of scaling iBOT to larger datasets and models. The authors should also discuss the potential for applying the proposed method to other modalities, such as video or audio. Fifth, how does the computational cost of iBOT compare to other self-supervised learning methods, and what are the trade-offs between computational cost and performance? A more detailed analysis of the computational cost is needed, including a breakdown of the time and memory requirements for each component of the model. Finally, what are the key differences between iBOT and MAE, and what are the key differences between iBOT and DINO? A more detailed analysis of the architectural differences and training methodologies is needed to understand the advantages and disadvantages of each method.


## Rating:

5.0


## Confidence:

4.0


## Decision:

Reject
}