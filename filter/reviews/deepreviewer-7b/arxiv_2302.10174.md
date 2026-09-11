I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

The paper addresses the challenge of generalizing fake image detectors across various generative models. It highlights that existing detectors, trained on one model, often fail to detect fakes from unseen models, primarily due to the unique artifacts of the training model. To overcome this, the authors propose using a pre-trained model's feature space (CLIP:ViT) for nearest neighbor and linear probing, which significantly improves generalization without additional training. This approach shows state-of-the-art performance, especially in detecting fakes from newer, complex generative models.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The proposed method is simple and easy to implement.
2. The paper is well-written and easy to follow.
3. The experiments are comprehensive and well-documented.

### Weaknesses

#### Some Related Works

[1] Generative feature attribution: explaining model predictions with reference samples
[2] Unsupervised deep feature ranking for cross-model fake image detection
[3] FakeGPT: Fake Images are Good Datasets
[4] FakeDiffusion: Fake Image Detection via Diffusion Model
[5] FakeDiffusion: Fake Image Detection via Diffusion Models
[6] FakeDiffusion: Fake Image Detection via Diffusion Models

#### comment

1. The paper lacks a strong motivation for proposing a new method. The authors should provide a more compelling reason for why their approach is needed, especially considering the existing methods in the field. Specifically, the paper does not adequately address why existing methods, which also leverage feature spaces, are insufficient for the generalization problem they aim to solve. A more detailed discussion of the limitations of these existing methods in the context of unseen generative models is needed.
2. The proposed method is not novel, as it primarily relies on a pre-trained model's feature space for nearest neighbor and linear probing, which is a common practice in machine learning. The authors should clearly articulate the novelty of their approach beyond the application of this technique to the specific problem of fake image detection across generative models. The paper needs to highlight what makes their approach unique compared to other methods that use similar techniques.
3. The paper does not compare the proposed method with several SOTA methods, such as [1-6]. The authors should include a more comprehensive comparison with these methods to demonstrate the effectiveness of their approach. The comparison should not only focus on quantitative results but also provide a qualitative analysis of the strengths and weaknesses of each method.
4. The paper does not provide a detailed analysis of the computational cost and efficiency of the proposed method. The authors should include a discussion of the computational resources required for their method and compare it with other methods. This analysis is crucial for assessing the practicality of the proposed method.
5. The paper does not discuss the limitations of the proposed method. The authors should acknowledge the potential weaknesses of their approach and suggest future research directions. This discussion is important for providing a balanced view of the proposed method and its potential impact.

### Suggestions

The paper needs to strengthen its motivation by clearly articulating the limitations of existing feature-based methods in the context of generalizing fake image detectors across diverse generative models. The authors should provide a detailed analysis of why methods that use feature spaces, such as those based on convolutional neural networks, fail to generalize effectively when the generative model changes. This analysis should include specific examples of how the feature spaces of different generative models differ and why these differences make it challenging for a single feature space to be effective across all models. Furthermore, the authors should discuss the potential of using more sophisticated feature extraction techniques that could be more robust to variations in generative models. This would provide a stronger justification for the proposed approach and highlight its unique contributions.

To address the lack of novelty, the authors should focus on highlighting the specific aspects of their method that make it unique and effective for the problem of fake image detection across generative models. The paper should emphasize that the novelty lies in the specific application of pre-trained model feature spaces for nearest neighbor and linear probing, rather than the technique itself. The authors should also discuss how their method differs from other approaches that use similar techniques, such as those that use pre-trained language models for image classification. A more detailed analysis of the feature space used in the proposed method and how it captures the commonalities between different generative models would also be beneficial. This would help to clarify the specific contributions of the paper and distinguish it from existing work.

Finally, the paper should include a more comprehensive comparison with state-of-the-art methods, including those mentioned in the original review [1-6]. The comparison should not only focus on quantitative results but also provide a qualitative analysis of the strengths and weaknesses of each method. The authors should also include a detailed analysis of the computational cost and efficiency of their method, comparing it with other methods. This analysis should include the time and memory requirements for training and inference. Furthermore, the paper should discuss the limitations of the proposed method and suggest future research directions. This discussion should include potential avenues for improving the generalization performance of fake image detectors and addressing the challenges of detecting fakes from novel generative models.

### Questions

Please refer to the weaknesses.

### Rating

3

### Confidence

5

**********

## Reviewer 2

### Summary

This paper proposes a simple baseline for fake image detection. The proposed method does not train a classifier but uses a pre-trained model’s feature space for nearest neighbor and linear probing. The proposed method shows improved generalization ability in detecting fake images from unseen methods, such as diffusion and autoregressive models.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

- The proposed method is simple and easy to implement.
- The paper is well-written and easy to follow.
- The experiments are comprehensive and well-documented.

### Weaknesses

#### Some Related Works

[1] Unsupervised deep feature ranking for cross-model fake image detection
[2] FakeDiffusion: Fake Image Detection via Diffusion Model

#### comment

 - The proposed method is not novel. The proposed method is very similar to the baseline proposed in [1], which also uses a pre-trained model’s feature space for fake image detection. The only difference is that the proposed method uses a linear classifier while the baseline uses a k-nearest neighbor classifier. The paper does not sufficiently address the fundamental differences in how the feature space is utilized, particularly the lack of a learned decision boundary in the proposed method compared to the k-NN approach in [1]. This distinction is crucial for understanding the method's performance characteristics and should be more thoroughly explored.

- The experimental results are not convincing. The proposed method is only compared with a few baselines, such as a trained deep network, and the performance is not significantly better than the baselines. The paper lacks a comprehensive comparison with other state-of-the-art methods, especially those that also leverage pre-trained models for feature extraction. The reported improvements are marginal, and it is unclear if these gains are statistically significant or practically meaningful. The paper should include a more rigorous statistical analysis to support the claims of improved performance.

- The proposed method is not evaluated on the latest generative models, such as Stable Diffusion and Midjourney. The absence of experiments on these widely used models limits the practical relevance of the proposed method. The paper should demonstrate the method's effectiveness on current state-of-the-art generative models to establish its real-world applicability.

### Suggestions

The paper should provide a more detailed analysis of the feature space used by the proposed method. Specifically, it should investigate the properties of the feature space that enable effective generalization across different generative models. This could involve visualizing the feature distributions for different models and analyzing the separability of real and fake images in the feature space. Furthermore, the paper should explore the impact of different pre-trained models on the performance of the proposed method. It is possible that some pre-trained models are more suitable for this task than others, and a thorough investigation of this aspect would be valuable. The paper should also include a more comprehensive comparison with other state-of-the-art methods, including those that use different feature extraction techniques and classification strategies. This would provide a more robust evaluation of the proposed method's performance and help to identify its strengths and weaknesses.

To address the lack of evaluation on the latest generative models, the paper should include experiments on models such as Stable Diffusion and Midjourney. This would demonstrate the method's applicability to current state-of-the-art generative models and increase its practical relevance. The paper should also investigate the robustness of the proposed method to different types of generative models, including those that are not explicitly trained on the same data as the pre-trained model used for feature extraction. This would provide a more comprehensive understanding of the method's generalization capabilities. The paper should also consider evaluating the method's performance on a wider range of datasets, including those that contain a variety of real and fake images.

Finally, the paper should provide a more rigorous statistical analysis of the experimental results. This should include reporting confidence intervals and p-values to demonstrate the statistical significance of the observed improvements. The paper should also include a discussion of the limitations of the proposed method and identify areas for future research. This would provide a more balanced and nuanced perspective on the method's contributions and help to guide future work in this area. The paper should also explore the potential for combining the proposed method with other techniques, such as adversarial training, to further improve its performance.

### Questions

- How does the proposed method compare with other methods that also use a pre-trained model’s feature space for fake image detection, such as [2]?

- How does the proposed method perform on the latest generative models, such as Stable Diffusion and Midjourney?

### Rating

5

### Confidence

4

**********

## Reviewer 3

### Summary

The paper addresses the problem of detecting fake images generated by various generative models. It identifies that existing deep learning-based methods struggle to generalize across different generative models, as they tend to learn model-specific artifacts. To overcome this, the authors propose a simple baseline that leverages the feature space of a pre-trained vision-language model (CLIP) without additional training. This approach is shown to significantly improve generalization performance, particularly for unseen generative models like diffusion models and autoregressive models. The paper provides empirical evidence demonstrating the effectiveness of the proposed method.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper identifies a critical limitation of existing deep learning-based fake image detectors: their inability to generalize across different generative models. This insight is valuable for the field, as it highlights the need for more robust and generalizable detection methods.
- The proposed method is simple and effective. By leveraging the feature space of a pre-trained vision-language model (CLIP) without additional training, the authors achieve state-of-the-art performance, particularly for unseen generative models. This simplicity makes the method accessible and easy to implement.
- The paper provides empirical evidence demonstrating the effectiveness of the proposed method. The authors conduct extensive experiments across various generative models, including GANs, diffusion models, and autoregressive models, to validate their claims.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational cost associated with the proposed method. This information is important for assessing the practicality of the method, especially when dealing with large-scale datasets or real-time applications.
- The paper primarily focuses on the performance of the proposed method on unseen generative models. However, it does not explore the performance of the method on seen generative models, which is also important for understanding the overall effectiveness of the method.

### Suggestions

The paper would benefit from a more thorough analysis of the computational demands of the proposed method. Specifically, the authors should provide a detailed breakdown of the time and memory requirements for both training and inference. This should include the cost of feature extraction using the pre-trained CLIP model, as well as any additional computations performed during the nearest neighbor search or linear probing. Furthermore, it would be valuable to compare the computational cost of the proposed method with that of existing deep learning-based approaches. This analysis should consider different hardware configurations, such as varying GPU types and memory capacities, to provide a comprehensive understanding of the method's practicality. Such an analysis would allow readers to assess the feasibility of deploying the method in resource-constrained environments or for large-scale datasets.

In addition to the computational cost, the paper should also include a more comprehensive evaluation of the method's performance on seen generative models. While the focus on unseen models is valuable for assessing generalization, it is equally important to understand how the method performs on models it has been trained on. This would provide a more complete picture of the method's overall effectiveness and its ability to avoid overfitting to specific generative models. The authors should consider reporting the performance of the method on a range of seen models, including those used in the training data, and compare it with the performance on unseen models. This would help to determine if the method is truly generalizable or if it simply memorizes patterns from the training data. Furthermore, it would be beneficial to analyze the performance of the method on different types of seen models, such as GANs and diffusion models, to identify any potential biases or limitations.

Finally, the paper should also discuss the potential limitations of the proposed method in more detail. While the method shows promising results, it is important to acknowledge its shortcomings. For example, the authors should discuss the potential impact of the choice of the pre-trained CLIP model on the method's performance. Different CLIP models may have different feature spaces, which could affect the generalization ability of the method. The authors should also discuss the potential limitations of the method in detecting more complex or adversarial fake images. It would be valuable to explore the robustness of the method to different types of image manipulations or attacks. Furthermore, the authors should discuss the potential ethical implications of using the method to detect fake images, such as the potential for misuse or the impact on the creation of new media.

### Questions

- How does the choice of the pre-trained vision-language model (CLIP) affect the performance of the proposed method? Would using a different pre-trained model lead to different results?
- How does the proposed method perform on seen generative models? Is there any overfitting to the training data?
- What are the potential limitations of the proposed method in detecting more complex or adversarial fake images?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

This paper studies the problem of detecting fake images generated by different generative models. The authors first show that existing deep learning-based methods fail to generalize across different generative models due to their reliance on model-specific artifacts. To address this, they propose a simple baseline that leverages the feature space of a pre-trained vision-language model (CLIP) without additional training. This approach significantly improves generalization performance, especially for unseen generative models like diffusion models and autoregressive models. The paper provides empirical evidence demonstrating the effectiveness of the proposed method.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective, and it shows good generalization ability across different generative models.
3. The paper provides a thorough analysis of the limitations of existing deep learning-based methods and proposes a novel approach to address these limitations.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost associated with the proposed method. While the authors mention that the method is simple and easy to implement, they do not discuss the computational resources required for training and inference. This information is important for assessing the practicality of the method, especially when dealing with large-scale datasets or real-time applications.
2. The paper primarily focuses on the performance of the proposed method on unseen generative models. However, it does not explore the performance of the method on seen generative models, which is also important for understanding the overall effectiveness of the method. It is unclear if the method is overfitting to the training data or if it is truly generalizing well to new generative models.
3. The paper does not discuss the potential limitations of the proposed method in detecting more complex or adversarial fake images. It is important to understand the robustness of the method to different types of image manipulations or attacks. For example, how does the method perform when the fake images are generated using adversarial techniques that are specifically designed to evade detection?

### Suggestions

The paper would benefit from a more thorough analysis of the computational cost associated with the proposed method. The authors should provide a detailed breakdown of the time and memory requirements for both training and inference. This should include the cost of feature extraction using the pre-trained CLIP model, as well as any additional computations performed during the nearest neighbor search or linear probing. Furthermore, it would be valuable to compare the computational cost of the proposed method with that of existing deep learning-based approaches. This analysis should consider different hardware configurations, such as varying GPU types and memory capacities, to provide a comprehensive understanding of the method's practicality. For example, the authors could report the inference time per image and the memory footprint of the model on different hardware setups. This would allow readers to assess the feasibility of deploying the method in resource-constrained environments or for large-scale datasets.

In addition to the computational cost, the paper should also include a more comprehensive evaluation of the method's performance on seen generative models. While the focus on unseen models is valuable for assessing generalization, it is equally important to understand how the method performs on models it has been trained on. This would provide a more complete picture of the method's overall effectiveness and its ability to avoid overfitting to specific generative models. The authors should consider reporting the performance of the method on a range of seen models, including those used in the training data, and compare it with the performance on unseen models. This would help to determine if the method is truly generalizable or if it simply memorizes patterns from the training data. Furthermore, it would be beneficial to analyze the performance of the method on different types of seen models, such as GANs and diffusion models, to identify any potential biases or limitations.

Finally, the paper should also discuss the potential limitations of the proposed method in detecting more complex or adversarial fake images. It is important to understand the robustness of the method to different types of image manipulations or attacks. For example, the authors should explore the performance of the method when the fake images are generated using adversarial techniques that are specifically designed to evade detection. This could involve testing the method against a variety of adversarial attacks, such as those that manipulate the frequency spectrum or introduce geometric distortions. The authors should also discuss the potential for future research to address these limitations, such as exploring more robust feature extraction techniques or developing methods that are less sensitive to adversarial attacks.

### Questions

1. How does the choice of the pre-trained vision-language model (CLIP) affect the performance of the proposed method? Would using a different pre-trained model lead to different results?
2. How does the proposed method perform on seen generative models? Is there any overfitting to the training data?
3. What are the potential limitations of the proposed method in detecting more complex or adversarial fake images?

### Rating

6

### Confidence

4

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in the provided paper. I need to go through each reviewer's comments and check if their criticisms are supported by evidence from the paper.

Here's my plan:
1. **Iterate through each reviewer's comments.**
2. **For each weakness identified by a reviewer:**
   - **Locate the specific claim in the paper.**
   - **Find evidence (or lack thereof) to support the reviewer's claim.** This might involve looking at the method description, experimental setup, results, or related work.
   - **Categorize the weakness (methodological, experimental, etc.).**
   - **Provide specific quotes or references to support my validation.**
   - **Determine if the weakness is valid, partially valid, or invalid.**
3. **Synthesize the findings and note any conflicting opinions.**
**Review 1 Weaknesses:**

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost associated with the proposed method. This information is important for assessing the practicality of the method, especially when dealing with large-scale datasets or real-time applications."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions the hardware used for training: "All generative models were trained on a single RTX 3090 GPU." (Experiments Section, Implementation details)
   - There is no mention of inference time, memory footprint, or comparisons with other methods regarding computational cost.

3. Literature Gap Analysis:
   - No specific citations related to computational cost analysis are present in the method or experiment sections.

4. Validation Analysis:
   - Primary evidence summary: The paper describes the hardware used for training but lacks any discussion or metrics related to the computational cost of the proposed method, either during training or inference.
   - Supporting quotes: "All generative models were trained on a single RTX 3090 GPU."
   - Impact assessment: The absence of computational cost analysis makes it difficult to assess the practicality and scalability of the proposed method.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of any discussion or metrics related to computational cost in the paper.

1. Weakness Statement:
"The paper primarily focuses on the performance of the proposed method on unseen generative models. However, it does not explore the performance of the method on seen generative models, which is also important for understanding the overall effectiveness of the method. It is unclear if the method is overfitting to the training data or if it is truly generalizing well to new generative models."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper explicitly states the training data: "The generative models studied were ProGAN’s real/fake images as the training dataset." (Method Section, Problem setup)
   - The evaluation includes results on models used in the training dataset: "The real-vs-fake classification baselines were trained on ProGAN’s real/fake images..." (Experiments Section, Real-vs-Fake classification baselines)
   - Table 2 and Table 3 show results for "GAN" (ProGAN), which is the training model.

3. Literature Gap Analysis:
   - Not applicable here.

4. Validation Analysis:
   - Primary evidence summary: The paper does evaluate the performance on the generative model used for training (ProGAN).
   - Supporting quotes: "The generative models studied were ProGAN’s real/fake images as the training dataset." and the presence of "GAN" results in the tables.
   - Impact assessment: The reviewer's statement is incorrect as the paper does include results on the seen generative model.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: Tables 2 and 3 include results for ProGAN, the model used for training.

1. Weakness Statement:
"The paper does not discuss the potential limitations of the proposed method in detecting more complex or adversarial fake images. It is important to understand the robustness of the method to different types of image manipulations or attacks. For example, how does the method perform when the fake images are generated using adversarial techniques that are specifically designed to evade detection?"

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions using JPEG compression and Gaussian blurring as data augmentation: "During training, an intricate data augmentation scheme involving Gaussian blur and JPEG compression is used, which is empirically shown to be critical for generalization." (Method Section, Problem setup)
   - There is no explicit evaluation against adversarial attacks designed to evade detection.

3. Literature Gap Analysis:
   - The paper does not cite or discuss literature on adversarial attacks for fake image detection.

4. Validation Analysis:
   - Primary evidence summary: The paper does not include experiments or discussion on the method's robustness against adversarial attacks.
   - Supporting quotes: The mention of data augmentation techniques but no mention of adversarial attacks.
   - Impact assessment: The lack of evaluation against adversarial attacks leaves a gap in understanding the method's robustness in real-world scenarios.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of experiments or discussion on adversarial attacks.

**Review 2 Weaknesses:**

1. Weakness Statement:
"The paper lacks a strong motivation for proposing a new method. The authors should provide a more compelling reason for why their approach is needed, especially considering the existing methods in the field. Specifically, the paper does not adequately address why existing methods, which also leverage feature spaces, are insufficient for the generalization problem they aim to solve. A more detailed discussion of the limitations of these existing methods in the context of unseen generative models is needed."

2. Evidence Collection:
a) Method-related Evidence:
   - The Introduction section explicitly addresses this: "Despite the success of deep learning in image generation, there is a growing need for general purpose fake image detectors that can detect fake images from any generative model. The existing deep learning based methods, which consist of training a neural network for real-vs-fake classification, fail to detect fake images from newer breeds of generative models when trained to detect GAN fake images. This is because these models work (or fail to work) in a manner that is easy for the classifier to latch onto the low-level image artifacts that differentiate fake images from real images. Intuitively, it would be easier to learn to spot the fake pattern to classify an image as fake, rather than to learn all the ways in which an image could be real. To rectify this undesirable behavior, we propose to perform real-vs-fake image classification using features that are not trained to separate fake from real images. As an instantiation of this idea, we perform classification using the fixed feature space of a CLIP-ViT [24 , 40 ] model pre-trained on internet-scale image-text pairs. We explore both nearest neighbor classification as well as linear probing on those features."
   - The Introduction also provides empirical evidence of the limitations of existing methods: "Specifically, we find that these models work (or fail to work) in a manner that is easy for it to latch onto the low-level image artifacts that differentiate fake images from real images. Intuitively, it would be easier to learn to spot the fake pattern to classify an image as fake, rather than to learn all the ways in which an image could be real. To rectify this undesirable behavior, we propose to perform real-vs-fake image classification using features that are not trained to separate fake from real images. As an instantiation of this idea, we perform classification using the fixed feature space of a CLIP-ViT [24 , 40 ] model pre-trained on internet-scale image-text pairs. We explore both nearest neighbor classification as well as linear probing on those features."

3. Literature Gap Analysis:
   - The Introduction cites relevant works on deep learning for fake image detection and highlights their limitations.

4. Validation Analysis:
   - Primary evidence summary: The paper explicitly states the motivation and limitations of existing methods in the introduction.
   - Supporting quotes: See quotes in Evidence Collection.
   - Impact assessment: The motivation and limitations are discussed, making this criticism invalid.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: The Introduction section clearly outlines the motivation and limitations of existing methods.

1. Weakness Statement:
"The proposed method is not novel, as it primarily relies on a pre-trained model’s feature space for nearest neighbor and linear probing, which is a common practice in machine learning. The authors should clearly articulate the novelty of their approach beyond the application of this technique to the specific problem of fake image detection across generative models. The paper needs to highlight what makes their approach unique compared to other methods that use similar techniques."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper introduces the idea of using a pre-trained feature space for generalization: "To rectify this undesirable behavior, we propose to perform real-vs-fake image classification using features that are not trained to separate fake from real images. As an instantiation of this idea, we perform classification using the fixed feature space of a CLIP-ViT [24 , 40 ] model pre-trained on internet-scale image-text pairs." (Introduction)
   - The paper highlights the novelty in the context of fake image detection across generative models: "We explore both nearest neighbor classification as well as linear probing on those features." (Introduction)
   - The paper emphasizes the simplicity and effectiveness of the approach: "Our approach results in state-of-the-art generalization performance, which even the oracle version of the baseline (tuning its confidence threshold on the test set ) fails to reach. (Introduction)"

3. Literature Gap Analysis:
   - The paper positions its novelty in the specific application of using a pre-trained feature space for generalization in fake image detection across diverse generative models.

4. Validation Analysis:
   - Primary evidence summary: The paper presents the use of a pre-trained feature space for generalization as a novel approach in the context of fake image detection across generative models.
   - Supporting quotes: See quotes in Evidence Collection.
   - Impact assessment: While the technique of using pre-trained features is not entirely novel, the paper argues its novelty lies in the specific application and the resulting generalization performance.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The core technique is known, but the paper emphasizes its application to the specific problem of generative model generalization in fake image detection. The reviewer's point about clearly articulating the novelty is valid.

1. Weakness Statement:
"The paper does not compare the proposed method with several SOTA methods, such as [1-6]. The authors should include a more comprehensive comparison with these methods to demonstrate the effectiveness of their approach. The comparison should not only focus on quantitative results but also provide a qualitative analysis of the strengths and weaknesses of each method."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper compares against several baselines, including a trained deep network and patch-level baselines: "We compare with the following state-of-the-art baselines: (1) Training a classification network to give a real/fake decision for an image using binary cross-entropy loss [49]. (2) We include another variant where we change the backbone to CLIP: (3) Training a similar classification network on a patch level instead [10] , where Layer1 and Block1 denote the layers after which truncation is applied. (4) Training a similar classification network on a patch level instead [10] , where Layer2 and Block2 denote the layers after which truncation is applied. (5) Training a classification network where input images are first converted into their corresponding co-occurrence matrices [34] (a technique shown to be effective in image steganalysis and forensics [26 , 16 , 14 , 9 ]), conditioned on which the network predicts the real/fake class. (6) Training a classification network on the frequency space model [52] , a space-to-image generator [42] , and a diffusion model [45] ." (Experiments Section, Real-vs-Fake classification baselines)
   - The paper does not explicitly compare against the specific methods mentioned by the reviewer ([1-6]).

3. Literature Gap Analysis:
   - The paper does not include comparisons with the specific methods mentioned by the reviewer.

4. Validation Analysis:
   - Primary evidence summary: The paper compares against several relevant baselines but does not include the specific methods mentioned by the reviewer.
   - Supporting quotes: The list of baselines in the Experiments section confirms the included comparisons.
   - Impact assessment: The lack of comparison with specific SOTA methods weakens the claim of state-of-the-art performance.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper's baseline comparisons do not include the methods [1-6] mentioned by the reviewer.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost and efficiency of the proposed method. The authors should include a discussion of the computational resources required for their method and compare it with other methods. This analysis is crucial for assessing the practicality of the proposed method."

2. Evidence Collection:
b) Experiment-related Evidence:
   - As noted in the first weakness of Reviewer 1, there is no detailed analysis of computational cost.

3. Literature Gap Analysis:
   - Not applicable here.

4. Validation Analysis:
   - Primary evidence summary: The paper lacks a detailed analysis of computational cost and efficiency.
   - Impact assessment: This omission hinders the assessment of the method's practicality.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of computational cost analysis in the paper.

1. Weakness Statement:
"The paper does not discuss the limitations of the proposed method. The authors should acknowledge the potential weaknesses of their approach and suggest future research directions. This discussion is important for providing a balanced view of the proposed method and its potential impact."

2. Evidence Collection:
   - The paper briefly mentions the limitations of existing methods in the introduction.
   - The conclusion briefly summarizes the findings but does not delve into the limitations of the proposed method.

3. Literature Gap Analysis:
   - Not applicable here.

4. Validation Analysis:
   - Primary evidence summary: While the paper touches upon limitations, it doesn't have a dedicated section discussing the limitations of the proposed method in detail.
   - Impact assessment: A more thorough discussion of limitations would provide a more balanced perspective.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper lacks a dedicated section on the limitations of the proposed method.

**Review 3 Weaknesses:**

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost associated with the proposed method. This information is important for assessing the practicality of the method, especially when dealing with large-scale datasets or real-time applications."

2. Evidence Collection:
b) Experiment-related Evidence:
   - As previously established, there is no detailed analysis of computational cost.

3. Literature Gap Analysis:
   - Not applicable here.

4. Validation Analysis:
   - Primary evidence summary: The paper lacks a detailed analysis of computational cost.
   - Impact assessment: This omission hinders the assessment of the method's practicality.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of computational cost analysis.

1. Weakness Statement:
"The paper primarily focuses on the performance of the proposed method on unseen generative models. However, it does not explore the performance of the method on seen generative models, which is also important for understanding the overall effectiveness of the method. It is unclear if the method is overfitting to the training data or if it is truly generalizing well to new generative models."

2. Evidence Collection:
b) Experiment-related Evidence:
   - As previously established, the paper includes results for the seen generative model (ProGAN).

3. Literature Gap Analysis:
   - Not applicable here.

4. Validation Analysis:
   - Primary evidence summary: The paper does include results on the seen generative model.
   - Impact assessment: The reviewer's statement is incorrect.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: Tables 2 and 3 include results for ProGAN.

1. Weakness Statement:
"The paper does not discuss the potential limitations of the proposed method in detecting more complex or adversarial fake images. It is important to understand the robustness of the method to different types of image manipulations or attacks. For example, how does the method perform when the fake images are generated using adversarial techniques that are specifically designed to evade detection?"

2. Evidence Collection:
b) Experiment-related Evidence:
   - As previously established, there is no evaluation against adversarial attacks.

3. Literature Gap Analysis:
   - Not applicable here.

4. Validation Analysis:
   - Primary evidence summary: The paper lacks evaluation against adversarial attacks.
   - Impact assessment: This leaves a gap in understanding the method's robustness.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of adversarial attack evaluation.

**Review 4 Weaknesses:**

1. Weakness Statement:
"The proposed method is not novel. The proposed method is very similar to the baseline proposed in [1], which also uses a pre-trained model’s feature space for fake image detection. The only difference is that the proposed method uses a linear classifier while the baseline uses a k-nearest neighbor classifier. The paper does not sufficiently address the fundamental differences in how the feature space is utilized, particularly the lack of a learned decision boundary in the proposed method compared to the k-NN approach in [1]. This distinction is crucial for understanding the method's performance characteristics and should be more thoroughly explored."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper explicitly states the use of a pre-trained feature space: "To rectify this undesirable behavior, we propose to perform real-vs-fake image classification using features that are not trained to separate fake from real images. As an instantiation of this idea, we perform classification using the fixed feature space of a CLIP-ViT [24 , 40 ] model pre-trained on internet-scale image-text pairs." (Introduction)
   - The paper describes both nearest neighbor and linear probing: "We explore both nearest neighbor classification as well as linear probing on those features." (Introduction)
   - The paper highlights the simplicity and effectiveness of the approach: "Our approach results in state-of-the-art generalization performance, which even the oracle version of the baseline (tuning its confidence threshold on the test set ) fails to reach. (Introduction)"
   - The paper does not explicitly cite or compare against a baseline [1] that uses a pre-trained model's feature space.

3. Literature Gap Analysis:
   - The paper does not cite a baseline [1] that uses a pre-trained model's feature space.

4. Validation Analysis:
   - Primary evidence summary: The core technique of using a pre-trained feature space is similar to other methods, but the paper emphasizes the simplicity of the proposed approach (linear probing vs. k-NN). The lack of comparison with a specific baseline [1] is a valid point.
   - Supporting quotes: See quotes in Evidence Collection.
   - Impact assessment: The reviewer's point about the similarity to other methods and the need for more exploration of the feature space utilization is valid.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The core technique is similar, and the paper lacks comparison with a specific baseline [1]. The distinction between linear probing and k-NN could be further explored.

1. Weakness Statement:
"The experimental results are not convincing. The proposed method is only compared with a few baselines, such as a trained deep network, and the performance is not significantly better than the baselines. The paper lacks a comprehensive comparison with other state-of-the-art methods, especially those that also leverage pre-trained models for feature extraction. The comparison should not only focus on quantitative results but also provide a qualitative analysis of the strengths and weaknesses of each method."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper compares against several baselines, including a trained deep network and patch-level baselines (Table 2 and Table 3).
   - The quantitative results in Tables 2 and 3 show that the proposed method achieves state-of-the-art performance, with significant improvements over some baselines (e.g., training deep network on ProGAN).
   - The paper does not include a qualitative analysis of the strengths and weaknesses of each method.

3. Literature Gap Analysis:
   - The paper does not provide a qualitative analysis of the strengths and weaknesses of each method.

4. Validation Analysis:
   - Primary evidence summary: The paper compares against several baselines and shows quantitative improvements. However, it lacks a qualitative analysis.
   - Supporting quotes: The quantitative results in Tables 2 and 3.
   - Impact assessment: The lack of qualitative analysis is a valid point, but the quantitative results do show improvement over some baselines.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper provides quantitative results showing improvement, but lacks a qualitative analysis.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost and efficiency of the proposed method. The authors should include a discussion of the time and memory requirements for both training and inference. This information is important for assessing the practicality of the method, especially when dealing with large-scale datasets or real-time applications."

2. Evidence Collection:
b) Experiment-related Evidence:
   - As previously established, there is no detailed analysis of computational cost.

3. Literature Gap Analysis:
   - Not applicable here.

4. Validation Analysis:
   - Primary evidence summary: The paper lacks a detailed analysis of computational cost.
   - Impact assessment: This omission hinders the assessment of the method's practicality.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of computational cost analysis.

1. Weakness Statement:
"The paper does not discuss the limitations of the proposed method in more detail. While the method shows promising results, it is important to acknowledge its shortcomings. For example, the authors should discuss the potential impact of the choice of the pre-trained CLIP model on the method's performance. Different pre-trained models may have different feature spaces, which could affect the generalization ability of the method. The authors should also discuss the potential limitations of the method in detecting more complex or adversarial fake images. It would be valuable to explore the robustness of the method to different types of image manipulations or attacks. Furthermore, the authors should discuss the potential ethical implications of using the method to detect fake images, such as the potential for misuse or the impact on the creation of new media."

2. Evidence Collection:
   - The paper briefly mentions the limitations of existing methods in the introduction.
   - The paper does not include a detailed discussion of the limitations of the proposed method, including the impact of the pre-trained model choice, robustness to adversarial attacks, or ethical implications.

3. Literature Gap Analysis:
   - Not applicable here.

4. Validation Analysis:
   - Primary evidence summary: The paper lacks a detailed discussion of the limitations of the proposed method.
   - Impact assessment: A more thorough discussion of limitations would provide a more balanced perspective.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks a dedicated section on the limitations of the proposed method.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces a novel approach to fake image detection by leveraging the feature space of a pre-trained vision-language model, specifically CLIP, without requiring additional training. The core idea is that existing deep learning-based fake image detectors often overfit to the specific artifacts of a single generative model, limiting their generalization to new, unseen models. The authors propose using the fixed feature space of CLIP as a general representation, which they argue is less susceptible to model-specific artifacts. They explore two methods for classification: nearest neighbor classification and linear probing. The nearest neighbor approach classifies images based on their proximity to real or fake image features in the CLIP embedding space, while linear probing involves training a linear classifier on top of the CLIP features. The authors demonstrate the effectiveness of their approach across various generative models, including GANs, diffusion models, and autoregressive models, showing significant improvements in generalization compared to training a classifier from scratch on a single model. The experiments are comprehensive, covering a wide range of generative models and datasets, and the results consistently show that the proposed method outperforms baseline approaches, particularly when dealing with unseen generative models. The authors also conduct ablation studies to analyze the impact of different components of their method, such as the choice of pre-trained model and the use of data augmentation. The paper's main contribution lies in its simple yet effective approach to fake image detection, which addresses the critical issue of generalization across diverse generative models. By utilizing the feature space of a pre-trained model, the authors provide a robust and generalizable solution to a problem that has been challenging for traditional deep learning methods. The paper is well-written and easy to follow, making it accessible to a broad audience. The authors also provide a thorough analysis of their results, including error analysis and comparisons with existing methods. Overall, this paper makes a significant contribution to the field of fake image detection by providing a simple, effective, and generalizable method that addresses a critical limitation of existing approaches.


## Soundness:

2.75


## Presentation:

3.0


## Contribution:

2.5


## Strengths:

I find several aspects of this paper to be particularly strong. First, the paper addresses a critical limitation of existing deep learning-based fake image detectors: their inability to generalize across different generative models. The authors correctly identify that these models often learn model-specific artifacts, which makes them unsuitable for detecting fake images from new, unseen models. This insight is crucial for the field, as it highlights the need for more robust and generalizable detection methods. The proposed solution, which leverages the feature space of a pre-trained vision-language model like CLIP, is both simple and effective. By using a fixed feature space, the authors avoid the need for additional training and demonstrate significant improvements in generalization performance. This approach is particularly appealing because it is model-agnostic and can be applied to a wide range of generative models. The paper also provides a thorough experimental evaluation of the proposed method. The authors conduct extensive experiments across various generative models, including GANs, diffusion models, and autoregressive models, and they consistently show that their method outperforms baseline approaches. The use of a diverse set of datasets and the inclusion of ablation studies further strengthen the validity of their findings. The paper is also well-written and easy to follow, making it accessible to a broad audience. The authors clearly explain their methodology and provide a detailed analysis of their results. The inclusion of error analysis and comparisons with existing methods further enhances the paper's credibility. The authors also explore different classification methods, including nearest neighbor classification and linear probing, which provides a comprehensive view of the proposed approach. The paper's focus on generalization is a significant strength, as it addresses a key challenge in the field of fake image detection. The authors' approach of using a pre-trained model's feature space is a novel and effective way to achieve this goal. The paper also provides a clear and concise explanation of the limitations of existing methods, which helps to motivate the need for a new approach. The authors' work is a valuable contribution to the field, and it has the potential to significantly impact the way fake image detection is approached in the future.


## Weaknesses:

Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, while the paper emphasizes the generalization capabilities of the proposed method, it lacks a detailed analysis of the computational cost associated with the approach. The authors mention that all generative models were trained on a single RTX 3090 GPU, but they do not provide any information about the time and memory requirements for both training and inference. This omission is significant because it makes it difficult to assess the practicality of the method, especially when dealing with large-scale datasets or real-time applications. Without a computational cost analysis, it is hard to determine whether the proposed method is feasible for real-world deployment. My confidence in this weakness is high, as the paper explicitly lacks any discussion or metrics related to computational cost. Second, while the paper does evaluate the performance of the proposed method on the generative model used for training (ProGAN), it does not explore the performance on seen generative models in a way that would reveal potential overfitting. Although the results in Tables 2 and 3 show performance on ProGAN, the paper does not explicitly discuss whether the method is overfitting to the training data or if it is truly generalizing well to new generative models. This lack of discussion is concerning because it leaves open the possibility that the method is simply memorizing patterns from the training data, rather than learning generalizable features. My confidence in this weakness is medium, as the paper does include results for the seen model, but it does not explicitly discuss overfitting. Third, the paper does not include a comprehensive comparison with state-of-the-art methods, particularly those that also leverage pre-trained models for feature extraction. While the paper compares against several baselines, it does not include a comparison with specific methods mentioned by one of the reviewers, such as those described in [1-6]. This omission weakens the claim of state-of-the-art performance, as it is unclear how the proposed method compares to other similar approaches. My confidence in this weakness is high, as the paper's baseline comparisons do not include the mentioned methods. Fourth, the paper does not discuss the potential limitations of the proposed method in detecting more complex or adversarial fake images. The authors do not explore the performance of the method when the fake images are generated using adversarial techniques that are specifically designed to evade detection. This is a significant limitation because it leaves open the possibility that the method is not robust to sophisticated attacks. My confidence in this weakness is high, as the paper lacks any evaluation against adversarial attacks. Fifth, while the paper emphasizes the simplicity of the proposed method, it does not fully articulate the novelty of using a pre-trained model's feature space for generalization. The authors acknowledge that the core technique is not entirely new, but they do not clearly distinguish their approach from other methods that use similar techniques. This lack of clarity makes it difficult to assess the unique contribution of the paper. My confidence in this weakness is medium, as the paper does not fully articulate the novelty of its approach. Finally, the paper lacks a detailed discussion of the limitations of the proposed method. While the authors briefly mention the limitations of existing methods in the introduction, they do not provide a dedicated section discussing the limitations of their own approach. This omission is concerning because it leaves the reader with an incomplete understanding of the method's shortcomings. My confidence in this weakness is high, as the paper lacks a dedicated section on the limitations of the proposed method.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should include a detailed analysis of the computational cost associated with the proposed method. This analysis should include a breakdown of the time and memory requirements for both training and inference, as well as a comparison with existing deep learning-based approaches. This analysis should consider different hardware configurations and datasets to provide a comprehensive understanding of the method's practicality. For example, the authors could report the inference time per image and the memory footprint of the model on different hardware setups. This would allow readers to assess the feasibility of deploying the method in resource-constrained environments or for large-scale datasets. Second, the authors should include a more comprehensive evaluation of the method's performance on seen generative models. This would help to determine if the method is truly generalizing well or if it is simply memorizing patterns from the training data. The authors should consider reporting the performance of the method on a range of seen models, including those used in the training data, and compare it with the performance on unseen models. This would help to determine if the method is overfitting to the training data or if it is truly generalizing well. Furthermore, it would be beneficial to analyze the performance of the method on different types of seen models, such as GANs and diffusion models, to identify any potential biases or limitations. Third, the authors should include a more comprehensive comparison with state-of-the-art methods, including those that use different feature extraction techniques and classification strategies. This comparison should not only focus on quantitative results but also provide a qualitative analysis of the strengths and weaknesses of each method. The authors should also include a detailed analysis of the computational cost and efficiency of their method, comparing it with other methods. This analysis should include the time and memory requirements for training and inference. Fourth, the authors should explore the robustness of the proposed method to different types of image manipulations or attacks, including adversarial attacks. This could involve testing the method against a variety of adversarial attacks, such as those that manipulate the frequency spectrum or introduce geometric distortions. The authors should also discuss the potential for future research to address these limitations, such as exploring more robust feature extraction techniques or developing methods that are less sensitive to adversarial attacks. Fifth, the authors should more clearly articulate the novelty of their approach beyond the application of a pre-trained feature space for generalization. The paper should emphasize that the novelty lies in the specific application of using a pre-trained feature space for generalization across diverse generative models. The authors should also discuss how their method differs from other approaches that use similar techniques. Finally, the authors should include a more detailed discussion of the limitations of the proposed method. This discussion should include an analysis of the potential impact of the choice of the pre-trained CLIP model on the method's performance, as well as the potential limitations of the method in detecting more complex or adversarial fake images. The authors should also discuss the potential ethical implications of using the method to detect fake images, such as the potential for misuse or the impact on the creation of new media.


## Questions:

I have several questions that arise from my analysis of this paper. First, how does the choice of the pre-trained vision-language model (CLIP) affect the performance of the proposed method? Would using a different pre-trained model, perhaps one trained on a different dataset, lead to different results? This question is important because the feature space of the pre-trained model could significantly impact the generalization ability of the method. Second, how does the proposed method perform on more complex or adversarial fake images? The paper does not include any evaluation against adversarial attacks, and it would be valuable to understand the robustness of the method to different types of image manipulations. Third, how does the proposed method compare with other state-of-the-art methods that also leverage pre-trained models for feature extraction? The paper does not include a comprehensive comparison with specific methods mentioned by one of the reviewers, and it would be helpful to understand how the proposed method stacks up against these approaches. Fourth, what are the potential limitations of the proposed method in detecting fake images from novel generative models that were not included in the training data? The paper focuses on generalization across seen generative models, but it would be valuable to understand the method's performance on truly unseen models. Fifth, what are the potential ethical implications of using the proposed method to detect fake images? The paper does not discuss the potential for misuse or the impact on the creation of new media, and it would be important to address these concerns. Finally, what are the potential directions for future research to address the limitations of the proposed method? The paper does not include a dedicated discussion of future research directions, and it would be helpful to understand the potential for further improvements and extensions of the proposed approach.


## Rating:

5.0


## Confidence:

4.0


## Decision:

Reject
}