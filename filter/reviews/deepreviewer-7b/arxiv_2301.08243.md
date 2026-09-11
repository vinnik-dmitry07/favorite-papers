I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper proposes a new self-supervised learning method that predicts the representations of various target blocks in the same image given a single context block. The proposed method is simple and efficient, and it can learn high semantic representations without the need for hand-crafted data augmentation. The authors conduct extensive experiments on various tasks, including image classification, object counting, and depth prediction, and demonstrate that their method achieves state-of-the-art results.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The proposed method is simple and efficient, and it can learn high semantic representations without the need for hand-crafted data augmentation.
2. The authors conduct extensive experiments on various tasks, including image classification, object counting, and depth prediction, and demonstrate that their method achieves state-of-the-art results.
3. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the impact of different hyperparameters on the performance of the proposed method. For example, how does the choice of the context block size, the number of target blocks, and the predictor architecture affect the final performance? A more thorough investigation of these parameters would help to understand the sensitivity of the method and provide guidance for practical applications.
2. The paper does not provide a clear explanation of the relationship between the proposed method and existing self-supervised learning methods. It would be helpful to discuss how the proposed method differs from and builds upon previous work, and what are the advantages and disadvantages of the proposed method compared to other methods.
3. The paper does not provide a detailed analysis of the computational cost of the proposed method. It would be helpful to compare the computational cost of the proposed method with other self-supervised learning methods and discuss the scalability of the proposed method for large-scale datasets.

### Suggestions

The paper would benefit from a more in-depth exploration of the hyperparameter space. Specifically, the authors should investigate the impact of varying the size of the context block, which could be done by systematically testing different patch sizes and analyzing the resulting performance on downstream tasks. This analysis should not only focus on the final accuracy but also consider the training stability and convergence speed. Furthermore, the number of target blocks used for prediction should be explored, as this parameter directly influences the amount of information the model is exposed to during training. It would be valuable to see a detailed ablation study that shows how the performance changes with different numbers of target blocks, and whether there is an optimal number for different tasks. The predictor architecture also warrants further investigation. The authors should explore different architectures, such as convolutional networks or transformers, and analyze their impact on the quality of the learned representations. This analysis should include a discussion of the trade-offs between computational cost and performance for different predictor architectures.

To better contextualize the proposed method, the authors should provide a more detailed comparison with existing self-supervised learning techniques. This comparison should go beyond a simple description of the methods and delve into the specific differences in their underlying mechanisms. For example, the authors could discuss how the proposed method's approach of predicting representations of various target blocks given a single context block differs from methods that use contrastive learning or generative approaches. It would be helpful to highlight the specific advantages of the proposed method, such as its ability to learn semantic representations without hand-crafted augmentations, and discuss the limitations. A more thorough comparison would help the reader understand the novelty and contribution of the proposed method in the context of existing literature. The authors should also discuss the potential limitations of the proposed method, such as its sensitivity to specific hyperparameters or its performance on certain types of datasets.

Finally, the paper should include a more detailed analysis of the computational cost of the proposed method. This analysis should include not only the training time but also the memory requirements and the inference time. The authors should compare the computational cost of the proposed method with other self-supervised learning methods and discuss the scalability of the proposed method for large-scale datasets. It would be beneficial to provide a breakdown of the computational cost for different components of the method, such as the context encoder, the predictor, and the loss calculation. This analysis should also consider the impact of different hardware configurations on the computational cost. A thorough analysis of the computational cost would help the reader understand the practical implications of using the proposed method and its suitability for different applications.

### Questions

1. How does the proposed method perform on other types of data, such as video or 3D data?
2. How does the proposed method perform on larger datasets, such as ImageNet-21k or JFT-300M?

### Rating

6

### Confidence

3

**********

## Reviewer 2

### Summary

This paper proposes a new self-supervised learning method that predicts the representations of various target blocks in the same image given a single context block. The proposed method is simple and efficient, and it can learn high semantic representations without the need for hand-crafted data augmentation. The authors conduct extensive experiments on various tasks, including image classification, object counting, and depth prediction, and demonstrate that their method achieves state-of-the-art results.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The proposed method is simple and efficient, and it can learn high semantic representations without the need for hand-crafted data augmentation.
2. The authors conduct extensive experiments on various tasks, including image classification, object counting, and depth prediction, and demonstrate that their method achieves state-of-the-art results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the impact of different hyperparameters on the performance of the proposed method. For example, how does the choice of the context block size, the number of target blocks, and the predictor architecture affect the final performance? A more thorough investigation of these parameters would help to understand the sensitivity of the method and provide guidance for practical applications.
2. The paper does not provide a clear explanation of the relationship between the proposed method and existing self-supervised learning methods. It would be helpful to discuss how the proposed method differs from and builds upon previous work, and what are the advantages and disadvantages of the proposed method compared to other methods.
3. The paper does not provide a detailed analysis of the computational cost of the proposed method. It would be helpful to compare the computational cost of the proposed method with other self-supervised learning methods and discuss the scalability of the proposed method for large-scale datasets.

### Suggestions

The paper would benefit from a more in-depth exploration of the hyperparameter space. Specifically, the authors should investigate the impact of varying the size of the context block, which could be done by systematically testing different patch sizes and analyzing the resulting performance on downstream tasks. This analysis should not only focus on the final accuracy but also consider the training stability and convergence speed. Furthermore, the number of target blocks used for prediction should be explored, as this parameter directly influences the amount of information the model is exposed to during training. It would be valuable to see a detailed ablation study that shows how the performance changes with different numbers of target blocks, and whether there is an optimal number for different tasks. The predictor architecture also warrants further investigation. The authors should explore different architectures, such as convolutional networks or transformers, and analyze their impact on the quality of the learned representations. This analysis should include a discussion of the trade-offs between computational cost and performance for different predictor architectures.

To better contextualize the proposed method, the authors should provide a more detailed comparison with existing self-supervised learning techniques. This comparison should go beyond a simple description of the methods and delve into the specific differences in their underlying mechanisms. For example, the authors could discuss how the proposed method's approach of predicting representations of various target blocks given a single context block differs from methods that use contrastive learning or generative approaches. It would be helpful to highlight the specific advantages of the proposed method, such as its ability to learn semantic representations without hand-crafted augmentations, and discuss the limitations. A more thorough comparison would help the reader understand the novelty and contribution of the proposed method in the context of existing literature. The authors should also discuss the potential limitations of the proposed method, such as its sensitivity to specific hyperparameters or its performance on certain types of datasets.

Finally, the paper should include a more detailed analysis of the computational cost of the proposed method. This analysis should include not only the training time but also the memory requirements and the inference time. The authors should compare the computational cost of the proposed method with other self-supervised learning methods and discuss the scalability of the proposed method for large-scale datasets. It would be beneficial to provide a breakdown of the computational cost for different components of the method, such as the context encoder, the predictor, and the loss calculation. This analysis should also consider the impact of different hardware configurations on the computational cost. A thorough analysis of the computational cost would help the reader understand the practical implications of using the proposed method and its suitability for different applications.

### Questions

1. How does the proposed method perform on other types of data, such as video or 3D data?
2. How does the proposed method perform on larger datasets, such as ImageNet-21k or JFT-300M?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper proposes a new self-supervised learning method called I-JEPA, which predicts the representations of various target blocks in the same image given a single context block. The proposed method is simple and efficient, and it can learn high semantic representations without the need for hand-crafted data augmentation. The authors conduct extensive experiments on various tasks, including image classification, object counting, and depth prediction, and demonstrate that their method achieves state-of-the-art results.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The proposed method is simple and efficient, and it can learn high semantic representations without the need for hand-crafted data augmentation.
2. The authors conduct extensive experiments on various tasks, including image classification, object counting, and depth prediction, and demonstrate that their method achieves state-of-the-art results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the impact of different hyperparameters on the performance of the proposed method. For example, how does the choice of the context block size, the number of target blocks, and the predictor architecture affect the final performance? A more thorough investigation of these parameters would help to understand the sensitivity of the method and provide guidance for practical applications.
2. The paper does not provide a clear explanation of the relationship between the proposed method and existing self-supervised learning methods. It would be helpful to discuss how the proposed method differs from and builds upon previous work, and what are the advantages and disadvantages of the proposed method compared to other methods.
3. The paper does not provide a detailed analysis of the computational cost of the proposed method. It would be helpful to compare the computational cost of the proposed method with other self-supervised learning methods and discuss the scalability of the proposed method for large-scale datasets.

### Suggestions

The paper would benefit from a more in-depth exploration of the hyperparameter space. Specifically, the authors should investigate the impact of varying the size of the context block, which could be done by systematically testing different patch sizes and analyzing the resulting performance on downstream tasks. This analysis should not only focus on the final accuracy but also consider the training stability and convergence speed. Furthermore, the number of target blocks used for prediction should be explored, as this parameter directly influences the amount of information the model is exposed to during training. It would be valuable to see a detailed ablation study that shows how the performance changes with different numbers of target blocks, and whether there is an optimal number for different tasks. The predictor architecture also warrants further investigation. The authors should explore different architectures, such as convolutional networks or transformers, and analyze their impact on the quality of the learned representations. This analysis should include a discussion of the trade-offs between computational cost and performance for different predictor architectures.

To better contextualize the proposed method, the authors should provide a more detailed comparison with existing self-supervised learning techniques. This comparison should go beyond a simple description of the methods and delve into the specific differences in their underlying mechanisms. For example, the authors could discuss how the proposed method's approach of predicting representations of various target blocks given a single context block differs from methods that use contrastive learning or generative approaches. It would be helpful to highlight the specific advantages of the proposed method, such as its ability to learn semantic representations without hand-crafted augmentations, and discuss the limitations. A more thorough comparison would help the reader understand the novelty and contribution of the proposed method in the context of existing literature. The authors should also discuss the potential limitations of the proposed method, such as its sensitivity to specific hyperparameters or its performance on certain types of datasets.

Finally, the paper should include a more detailed analysis of the computational cost of the proposed method. This analysis should include not only the training time but also the memory requirements and the inference time. The authors should compare the computational cost of the proposed method with other self-supervised learning methods and discuss the scalability of the proposed method for large-scale datasets. It would be beneficial to provide a breakdown of the computational cost for different components of the method, such as the context encoder, the predictor, and the loss calculation. This analysis should also consider the impact of different hardware configurations on the computational cost. A thorough analysis of the computational cost would help the reader understand the practical implications of using the proposed method and its suitability for different applications.

### Questions

1. How does the proposed method perform on other types of data, such as video or 3D data?
2. How does the proposed method perform on larger datasets, such as ImageNet-21k or JFT-300M?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

This paper proposes a self-supervised learning method called I-JEPA that predicts the representations of various target blocks in the same image given a single context block. The proposed method is simple and efficient, and it can learn high semantic representations without the need for hand-crafted data augmentation. The authors conduct extensive experiments on various tasks, including image classification, object counting, and depth prediction, and demonstrate that their method achieves state-of-the-art results.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and efficient, and it can learn high semantic representations without the need for hand-crafted data augmentation.
3. The authors conduct extensive experiments on various tasks, including image classification, object counting, and depth prediction, and demonstrate that their method achieves state-of-the-art results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the impact of different hyperparameters on the performance of the proposed method. For example, how does the choice of the context block size, the number of target blocks, and the predictor architecture affect the final performance? A more thorough investigation of these parameters would help to understand the sensitivity of the method and provide guidance for practical applications.
2. The paper does not provide a clear explanation of the relationship between the proposed method and existing self-supervised learning methods. It would be helpful to discuss how the proposed method differs from and builds upon previous work, and what are the advantages and disadvantages of the proposed method compared to other methods.
3. The paper does not provide a detailed analysis of the computational cost of the proposed method. It would be helpful to compare the computational cost of the proposed method with other self-supervised learning methods and discuss the scalability of the proposed method for large-scale datasets.

### Suggestions

The paper would benefit from a more in-depth exploration of the hyperparameter space. Specifically, the authors should investigate the impact of varying the size of the context block, which could be done by systematically testing different patch sizes and analyzing the resulting performance on downstream tasks. This analysis should not only focus on the final accuracy but also consider the training stability and convergence speed. Furthermore, the number of target blocks used for prediction should be explored, as this parameter directly influences the amount of information the model is exposed to during training. It would be valuable to see a detailed ablation study that shows how the performance changes with different numbers of target blocks, and whether there is an optimal number for different tasks. The predictor architecture also warrants further investigation. The authors should explore different architectures, such as convolutional networks or transformers, and analyze their impact on the quality of the learned representations. This analysis should include a discussion of the trade-offs between computational cost and performance for different predictor architectures.

To better contextualize the proposed method, the authors should provide a more detailed comparison with existing self-supervised learning techniques. This comparison should go beyond a simple description of the methods and delve into the specific differences in their underlying mechanisms. For example, the authors could discuss how the proposed method's approach of predicting representations of various target blocks given a single context block differs from methods that use contrastive learning or generative approaches. It would be helpful to highlight the specific advantages of the proposed method, such as its ability to learn semantic representations without hand-crafted augmentations, and discuss the limitations. A more thorough comparison would help the reader understand the novelty and contribution of the proposed method in the context of existing literature. The authors should also discuss the potential limitations of the proposed method, such as its sensitivity to specific hyperparameters or its performance on certain types of datasets.

Finally, the paper should include a more detailed analysis of the computational cost of the proposed method. This analysis should include not only the training time but also the memory requirements and the inference time. The authors should compare the computational cost of the proposed method with other self-supervised learning methods and discuss the scalability of the proposed method for large-scale datasets. It would be beneficial to provide a breakdown of the computational cost for different components of the method, such as the context encoder, the predictor, and the loss calculation. This analysis should also consider the impact of different hardware configurations on the computational cost. A thorough analysis of the computational cost would help the reader understand the practical implications of using the proposed method and its suitability for different applications.

### Questions

1. How does the proposed method perform on other types of data, such as video or 3D data?
2. How does the proposed method perform on larger datasets, such as ImageNet-21k or JFT-300M?

### Rating

6

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The reviewer has identified three main weaknesses: lack of hyperparameter analysis, lack of comparison to existing SSL methods, and lack of computational cost analysis. I need to go through each of these and see if the paper provides sufficient information or if the reviewer's claims are valid.

**Weakness 1: Lack of Hyperparameter Analysis**
- **Type:** Experimental
- **Relevant Sections:** Experiments section, specifically the setup and results for each experiment.
- **Potential Misunderstanding:** The reviewer might be expecting a more formal ablation study section.

**Weakness 2: Lack of Comparison to Existing SSL Methods**
- **Type:** Methodological/Experimental
- **Relevant Sections:** Introduction, Related Work, Method section.
- **Potential Misunderstanding:** The reviewer might be looking for a more detailed, point-by-point comparison of I-JEPA's mechanism to specific SSL methods.

**Weakness 3: Lack of Computational Cost Analysis**
- **Type:** Experimental
- **Relevant Sections:** Experiments section, specifically the implementation details and results.
- **Potential Misunderstanding:** The reviewer might be looking for a more explicit comparison of training time and memory usage with other methods.

**Plan:**
1. Go through each weakness and find supporting evidence or counter-evidence in the provided paper text.
2. For each weakness, provide direct quotes or references to specific sections.
3. Conclude whether the weakness is valid, partially valid, or invalid, and provide a confidence level.
**Reviewer 1 Weaknesses Validation:**

**Weakness 1 Statement:**
The paper lacks a detailed analysis of the impact of different hyperparameters on the performance of the proposed method. For example, how does the choice of the context block size, the number of target blocks, and the predictor architecture affect the final performance? A more thorough investigation of these parameters would help to understand the sensitivity of the method and provide guidance for practical applications.

**Evidence Collection:**
a) Method-related Evidence:
- The paper mentions the context block size: "We denote by B x B the size of the non-overlapping blocks..." (Section 3).
- The number of target blocks is implicitly defined by the sampling process: "We denote by M (possibly overlapping) blocks from the target representations..." (Section 3).
- The predictor architecture is described: "The predictor g ϕ (·, ·) takes as input the output of the context encoder s x and a mask token for each patch we wish to predict, { m j } j ∈ B i , and outputs a patch-level prediction s ^ y ( i ) = { s ^ y j } j ∈ B i ." (Section 3).
- The paper includes an ablation study on masking strategies (Table 6), which touches upon the number of target blocks to some extent.

b) Experiment-related Evidence:
- The paper mentions the resolution used for pretraining: "All I-JEPA models are trained at resolution 224 × 224 pixels..." (Section 5).
- There is no explicit ablation study on varying the context block size or the number of target blocks.

3. Literature Gap Analysis:
- While the paper cites relevant works in self-supervised learning, it doesn't explicitly cite literature on hyperparameter sensitivity analysis in the context of SSL.

4. Validation Analysis:
- The reviewer is correct that the paper lacks a dedicated ablation study systematically varying key hyperparameters like context block size and the number of target blocks. While the paper describes these components and includes an ablation on masking strategies, it doesn't explore the impact of different sizes or numbers on performance. The predictor architecture is described, but there's no ablation on different architectures. This limits the understanding of the method's sensitivity and optimal configuration.

5. Conclusion:
- Validity status: **Valid**
- Confidence level: **High**
- Key supporting evidence: The paper describes the hyperparameters but lacks experiments systematically varying them to analyze their impact on performance.

**Weakness 2 Statement:**
The paper does not provide a clear explanation of the relationship between the proposed method and existing self-supervised learning methods. It would be helpful to discuss how the proposed method differs from and builds upon previous work, and what are the advantages and disadvantages of the proposed method compared to other methods.

**Evidence Collection:**
a) Method-related Evidence:
- The introduction mentions related work: "In contrast to Joint-Embedding Architectures, JEPAs do not seek representations invariant to a set of hand-crafted data augmentations, but instead seek representations that are predictive of each other when conditioned on additional information 𝒛 ." (Section 2).
- The introduction also contrasts I-JEPA with other methods: "In contrast to Joint-Embedding Architectures, I-JEPA makes use of abstract prediction targets for which unnecessary pixel-level details are potentially eliminated, thereby leading the model to learn more semantic features. Another core design choice to guide I-JEPA towards producing semantic representations is the proposed multi-block masking strategy. Specifically, we demonstrate the importance of predicting sufficiently large target blocks in the image, using an informative (spatially distributed) context block." (Section 2).
- The related work section provides a brief overview of different SSL approaches (Image-based, Generative, Joint-Embedding).

b) Experiment-related Evidence:
- The paper includes comparisons with several existing SSL methods (MAE, Context Autoencoders, data2vec, SimMIM, iBOT, DINO, MSN, EMA) in the experiments section.

3. Literature Gap Analysis:
- The paper cites relevant works in SSL.

4. Validation Analysis:
- The reviewer's claim is partially valid. The paper does discuss the differences between I-JEPA and other SSL methods, particularly emphasizing the use of abstract prediction targets and the multi-block masking strategy. It also highlights the differences from Joint-Embedding Architectures. Furthermore, the experimental section directly compares I-JEPA's performance against several existing methods. However, the explanation could be more detailed and explicitly highlight the advantages and disadvantages of I-JEPA compared to each specific method in the related work section, rather than just mentioning the differences.

5. Conclusion:
- Validity status: **Partially Valid**
- Confidence level: **High**
- Key supporting evidence: The paper mentions differences and includes experimental comparisons, but the explanation of the relationship and advantages/disadvantages could be more explicit and detailed.

**Weakness 3 Statement:**
The paper does not provide a detailed analysis of the computational cost of the proposed method. It would be helpful to compare the computational cost of the proposed method with other self-supervised learning methods and discuss the scalability of the proposed method for large-scale datasets.

**Evidence Collection:**
a) Method-related Evidence:
- The paper mentions the use of Vision Transformers (ViT) as the context and predictor encoders (Section 3).

b) Experiment-related Evidence:
- The paper includes a section on "Model Efficiency" (Section 7.1) which provides training time comparisons.
- Table 7 shows the number of parameters and FLOPs.
- Figure 5 shows a comparison of semi-supervised evaluation on 1% ImageNet-1K as a function of GPU hours.
- The paper mentions the training time for I-JEPA (27 hours) and DINO (5x longer).
- The paper mentions the number of A100 GPUs used (75 for I-JEPA, 1 for DINO).

3. Literature Gap Analysis:
- Not applicable here.

4. Validation Analysis:
- The reviewer's claim is partially valid. The paper does provide some analysis of computational cost, including training time comparisons with DINO and a breakdown of FLOPs and parameters. It also shows the efficiency gains in terms of GPU hours for semi-supervised learning. However, it lacks a direct comparison of training time and memory usage with *all* the baseline methods listed in the experiments section. While the training time is compared to DINO, a more comprehensive comparison across all baselines would strengthen the analysis. The scalability is discussed in the context of the 1% ImageNet-1K experiment, but a more explicit discussion of scalability to even larger datasets could be beneficial.

5. Conclusion:
- Validity status: **Partially Valid**
- Confidence level: **High**
- Key supporting evidence: The paper provides some computational cost analysis (training time vs. DINO, FLOPs/parameters), but lacks a comprehensive comparison with all baselines and a more explicit discussion of scalability.

**Reviewer Questions Validation:**

**Question 1:**
How does the proposed method perform on other types of data, such as video or 3D data?

**Evidence Collection:**
a) Method-related Evidence:
- The method is described in the context of image data (Section 3).

b) Experiment-related Evidence:
- The experiments are conducted on image datasets (ImageNet, Clevr, Clevr-Dist).

3. Literature Gap Analysis:
- Not applicable.

4. Validation Analysis:
- The paper focuses on image data. There is no experimental evaluation or discussion of applying I-JEPA to video or 3D data.

5. Conclusion:
- Validity status: **Valid** (as a question highlighting a missing aspect)
- Confidence level: **High**
- Key supporting evidence: The paper's focus is explicitly on image data, and no experiments on other data types are presented.

**Question 2:**
How does the proposed method perform on larger datasets, such as ImageNet-21k or JFT-300M?

**Evidence Collection:**
a) Experiment-related Evidence:
- The paper includes experiments on ImageNet-1K and ImageNet-22K.
- The paper mentions training on ImageNet using 16 A100 GPUs in under 72 hours to achieve strong downstream performance across a wide range of tasks (Introduction).

3. Literature Gap Analysis:
- Not applicable.

4. Validation Analysis:
- The paper does include experiments on larger datasets like ImageNet-22K. It doesn't explicitly mention ImageNet-21k or JFT-300M. The mention of training on ImageNet-1K with strong performance suggests the method's capability on large datasets.

5. Conclusion:
- Validity status: **Partially Valid** (as a question highlighting a potential area for further exploration, but the paper does include experiments on a larger dataset)
- Confidence level: **High**
- Key supporting evidence: The paper includes experiments on ImageNet-22K, addressing part of the question. The absence of ImageNet-21k and JFT-300M results makes the question valid in that specific context.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces I-JEPA, a novel self-supervised learning method that predicts the representations of various target blocks within an image, given a single context block. This approach contrasts with traditional methods that often rely on hand-crafted data augmentations or pixel-level reconstruction. The core idea behind I-JEPA is to leverage a joint-embedding architecture where the context encoder maps the context block into a feature space, and a predictor network, conditioned on this context, generates the representations of multiple target blocks. This process encourages the model to learn semantic features by predicting the representation of different parts of the image based on a single reference point. The authors emphasize that by operating in the representation space, I-JEPA can learn high-level semantic information without the need for explicit pixel-level supervision or extensive data augmentation. The method is designed to be efficient, utilizing Vision Transformers (ViT) for both the context and predictor encoders. The training process involves sampling a context block from an image and then predicting the representations of multiple target blocks, which are randomly sampled and overlapping. The predictor network is trained to minimize the distance between the predicted representations and the actual representations of the target blocks. The authors conduct extensive experiments on various image classification, object counting, and depth prediction tasks, demonstrating that I-JEPA achieves state-of-the-art results. Specifically, they show that I-JEPA outperforms several existing self-supervised learning methods, including MAE, Context Autoencoders, data2vec, SimMIM, iBOT, DINO, MSN, and EMA, on datasets such as ImageNet-1K and ImageNet-22K. The paper also includes an analysis of the computational cost of I-JEPA, showing that it is more efficient than some other self-supervised methods, such as DINO, in terms of training time. Furthermore, the authors explore the impact of different hyperparameters, such as the context block size and the number of target blocks, on the performance of the method, although this analysis is not as comprehensive as it could be. Overall, the paper presents a compelling approach to self-supervised learning that is both effective and efficient, offering a valuable contribution to the field.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

2.75


## Strengths:

I find several aspects of this paper to be particularly strong. First, the core idea of I-JEPA, which is to predict the representations of various target blocks given a single context block, is both simple and elegant. This approach effectively circumvents the need for hand-crafted data augmentations, which are often a significant burden in traditional self-supervised learning methods. By operating in the representation space, I-JEPA is able to learn high-level semantic features, which is a significant advantage. The method's efficiency is another notable strength. The use of Vision Transformers (ViT) as the context and predictor encoders allows for fast processing of image data, and the authors demonstrate that I-JEPA achieves strong performance with relatively few computational resources. The experimental results are also compelling. The paper presents extensive evaluations on various tasks, including image classification, object counting, and depth prediction, and consistently shows that I-JEPA achieves state-of-the-art results compared to several existing self-supervised learning methods. This demonstrates the robustness and generalizability of the proposed approach. The authors also include an analysis of the computational cost of I-JEPA, showing that it is more efficient than some other self-supervised methods, such as DINO, in terms of training time. This is a valuable contribution, as it highlights the practical advantages of I-JEPA. Finally, the paper is well-written and easy to follow, making it accessible to a broad audience. The authors clearly explain the method, the experimental setup, and the results, which is crucial for the reproducibility and impact of the work. The inclusion of an ablation study on masking strategies, although not as comprehensive as it could be, also adds to the overall strength of the paper. The authors' focus on learning semantic representations without explicit data augmentation is a significant contribution to the field of self-supervised learning.


## Weaknesses:

While I appreciate the strengths of this paper, I have identified several weaknesses that warrant further consideration. First, the paper lacks a detailed analysis of the impact of different hyperparameters on the performance of the proposed method. Specifically, the authors do not systematically investigate the effect of varying the size of the context block, the number of target blocks, and the predictor architecture. While the paper describes these components, there is no ablation study that explores how these parameters affect the final performance. For example, the context block size is mentioned as 'B x B' (Section 3), but the paper does not explore the impact of different values of B. Similarly, the number of target blocks is implicitly defined by the sampling process, but there is no analysis of how the number of target blocks affects the model's ability to learn semantic representations. The predictor architecture is also described, but there is no ablation study that explores different architectures. This lack of systematic analysis makes it difficult to understand the sensitivity of the method to these parameters and provides limited guidance for practical applications. This is a significant limitation, as it leaves open the question of how to best configure I-JEPA for different tasks and datasets. My confidence in this weakness is high, as the paper clearly lacks the experimental evidence to support the claim that these parameters have a negligible impact on performance. Second, while the paper does discuss the differences between I-JEPA and existing self-supervised learning methods, the explanation could be more detailed and explicit. The paper mentions that I-JEPA makes use of abstract prediction targets to eliminate unnecessary pixel-level details, leading to the learning of more semantic features (Section 2). It also highlights the importance of predicting sufficiently large target blocks using an informative context block. However, the paper does not provide a comprehensive comparison with each specific SSL method in the related work section, nor does it explicitly highlight the advantages and disadvantages of I-JEPA compared to each method. While the experimental section does include comparisons with several existing SSL methods, the paper could benefit from a more in-depth discussion of how I-JEPA's approach differs from and builds upon previous work. This lack of a detailed comparison makes it difficult to fully understand the novelty and contribution of I-JEPA in the context of existing literature. My confidence in this weakness is high, as the paper's discussion of related work is not as detailed as it could be. Finally, the paper does not provide a detailed analysis of the computational cost of the proposed method. While the paper includes some analysis of computational cost, including training time comparisons with DINO and a breakdown of FLOPs and parameters (Section 7.1), it lacks a direct comparison of training time and memory usage with *all* the baseline methods listed in the experiments section. The paper mentions that I-JEPA requires less compute than pixel-reconstruction methods and achieves comparable performance, but it does not provide a comprehensive analysis of the computational cost of I-JEPA compared to all the baselines. While the training time is compared to DINO, a more comprehensive comparison across all baselines would strengthen the analysis. Furthermore, the paper does not explicitly discuss the scalability of I-JEPA to even larger datasets, such as ImageNet-21k or JFT-300M. This lack of a detailed computational cost analysis and a discussion of scalability limits the practical implications of the work. My confidence in this weakness is high, as the paper's analysis of computational cost is not as comprehensive as it could be.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should conduct a more thorough investigation of the hyperparameter space. Specifically, they should systematically vary the size of the context block, the number of target blocks, and the predictor architecture to understand their impact on the performance of I-JEPA. This analysis should not only focus on the final accuracy but also consider the training stability and convergence speed. For example, the authors could conduct ablation studies by varying the context block size and analyzing the resulting performance on downstream tasks. They should also explore different predictor architectures, such as convolutional networks or transformers, and analyze their impact on the quality of the learned representations. This analysis should include a discussion of the trade-offs between computational cost and performance for different predictor architectures. Second, the authors should provide a more detailed comparison with existing self-supervised learning techniques. This comparison should go beyond a simple description of the methods and delve into the specific differences in their underlying mechanisms. For example, the authors could discuss how the proposed method's approach of predicting representations of various target blocks given a single context block differs from methods that use contrastive learning or generative approaches. It would be helpful to highlight the specific advantages of the proposed method, such as its ability to learn semantic representations without hand-crafted augmentations, and discuss the limitations. A more thorough comparison would help the reader understand the novelty and contribution of the proposed method in the context of existing literature. The authors should also discuss the potential limitations of the proposed method, such as its sensitivity to specific hyperparameters or its performance on certain types of datasets. Finally, the paper should include a more detailed analysis of the computational cost of the proposed method. This analysis should include not only the training time but also the memory requirements and the inference time. The authors should compare the computational cost of the proposed method with other self-supervised learning methods and discuss the scalability of the proposed method for large-scale datasets. It would be beneficial to provide a breakdown of the computational cost for different components of the method, such as the context encoder, the predictor, and the loss calculation. This analysis should also consider the impact of different hardware configurations on the computational cost. A thorough analysis of the computational cost would help the reader understand the practical implications of using the proposed method and its suitability for different applications. In summary, these suggestions aim to provide a more comprehensive understanding of the method's behavior, its relationship to existing work, and its practical implications.


## Questions:

I have several questions that arise from my analysis of the paper. First, how does the performance of I-JEPA vary with different context block sizes? The paper mentions the context block size as a key parameter, but it does not provide any experimental results that systematically explore the impact of different sizes. Understanding how the context block size affects the model's ability to learn semantic representations is crucial for practical applications. Second, what is the optimal number of target blocks to predict for a given task? The paper uses a multi-block masking strategy, but it does not provide any analysis of how the number of target blocks affects the performance of I-JEPA. It would be valuable to understand the trade-offs between predicting more target blocks and the computational cost. Third, how does the predictor architecture affect the performance of I-JEPA? The paper uses a specific predictor architecture, but it does not explore the impact of different architectures. It would be interesting to see how different predictor architectures, such as convolutional networks or transformers, affect the quality of the learned representations. Fourth, how does I-JEPA perform on other types of data, such as video or 3D data? The paper focuses on image data, but it would be valuable to understand how I-JEPA could be applied to other types of data. Finally, how does the performance of I-JEPA scale to larger datasets, such as ImageNet-21k or JFT-300M? The paper includes experiments on ImageNet-22K, but it does not explicitly address the scalability of I-JEPA to even larger datasets. Understanding how I-JEPA performs on larger datasets is crucial for its practical applications. These questions target key uncertainties in the paper and seek clarification on critical assumptions and methodological choices.


## Rating:

6.0


## Confidence:

3.0


## Decision:

Reject
}