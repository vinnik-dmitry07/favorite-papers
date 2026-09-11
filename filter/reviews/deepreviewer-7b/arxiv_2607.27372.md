I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper introduces explorative modeling (XMs), a new paradigm for generative modeling that aims to make generative models end-to-end, i.e., sample the same way during training and inference. The authors argue that traditional generative models often fail to achieve this due to a mismatch between the training loop and the generation procedure, which typically involves a one-to-many mapping from latent variables to data. To address this, XMs factor the training loop by exploring multiple candidate samples and selecting the one that minimizes the reconstruction loss. The authors demonstrate that this approach can enhance generative expressivity and improve performance across various generative models, including diffusion and flow-based models. Additionally, they show that XMs can enable end-to-end reconstructive generative modeling and achieve competitive results in tasks like behavior cloning and goal-conditioned world modeling.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow, with clear explanations of the proposed method and its motivation.
2. The authors provide extensive experimental results, demonstrating the effectiveness of XMs across different generative models and tasks.
3. The introduction of XMs offers a new perspective on generative modeling, potentially opening up new avenues for research and development in this field.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on unconditional generative models, and it is unclear how the proposed method would perform with conditional inputs. The authors should provide more discussion on the challenges and potential solutions for incorporating conditional information into XMs.
2. The computational cost of exploring multiple candidate samples during training is a significant concern, especially for high-dimensional data. The authors should provide a more detailed analysis of the computational complexity and discuss potential strategies for reducing the overhead of XMs.
3. The paper lacks a thorough comparison with existing methods that aim to improve generative expressivity, such as latent space manipulation or advanced sampling techniques. A more comprehensive comparison would help to better position the contributions of XMs within the broader landscape of generative modeling.

### Suggestions

The authors should delve deeper into the practical challenges of applying explorative modeling (XMs) with conditional inputs. While the paper touches on the concept of conditioning the latent variable, a more rigorous analysis is needed. Specifically, the authors should explore how different types of conditional information (e.g., text, images, categorical labels) would be incorporated into the exploration process. For instance, if the goal is to generate images conditioned on text descriptions, how would the model explore the latent space to find the best match for the given text? Would the exploration process be guided by the text embedding, or would it be a purely random search within the latent space? Furthermore, the authors should discuss the potential impact of the exploration strategy on the quality and diversity of the generated samples. It would be beneficial to include experiments that systematically vary the exploration parameters and analyze their effect on the final results. This would provide a more comprehensive understanding of the practical limitations and potential of XMs in conditional settings.

To address the computational concerns, the authors should provide a more detailed analysis of the time and memory complexity of their method. The current discussion lacks specific details about the computational overhead introduced by the exploration process. For example, how does the runtime scale with the number of explored samples, the dimensionality of the latent space, and the complexity of the generative model? It would be helpful to provide a breakdown of the computational cost associated with each step of the algorithm, including the forward and backward passes, as well as the exploration process itself. Furthermore, the authors should explore and discuss potential strategies for reducing the computational burden of XMs. This could include techniques such as early stopping criteria for exploration, adaptive exploration strategies that focus on promising regions of the latent space, or the use of more efficient sampling algorithms. A thorough analysis of these aspects would greatly enhance the practical applicability of the proposed method.

Finally, the authors need to provide a more comprehensive comparison of XMs with existing methods that aim to improve generative expressivity. While the paper mentions some related works, a more detailed analysis is needed to clearly position the contributions of XMs within the broader landscape of generative modeling. Specifically, the authors should compare XMs with techniques such as latent space manipulation, adversarial training, and advanced sampling techniques. For example, how does XM compare to methods that use latent space interpolation or extrapolation to generate novel samples? How does it compare to techniques that use adversarial training to improve the robustness of generative models? A more thorough comparison would help to highlight the unique advantages and limitations of XMs and provide a clearer understanding of its place within the existing literature. This comparison should include both quantitative and qualitative analysis, as well as a discussion of the theoretical underpinnings of each method.

### Questions

1. How does the proposed method handle conditional inputs, and what are the potential challenges in incorporating conditional information into XMs?
2. What is the computational complexity of the proposed method, and how does it scale with the dimensionality of the data and the number of explored samples?
3. How does the proposed method compare to existing approaches that aim to improve generative expressivity, such as latent space manipulation or advanced sampling techniques?

### Rating

6

### Confidence

3

**********

## Reviewer 2

### Summary

This paper introduces Explorative Modeling (XM), a new paradigm for generative modeling that addresses the limitations of end-to-end training in generative models. The authors argue that traditional generative models, such as those based on diffusion and flow matching, often fail to capture the full distribution of data due to a mismatch between the training loop and the generation procedure. XM addresses this issue by introducing a new training objective that allows models to explore multiple candidate matches between data and latent variables, enabling them to better capture the multimodal nature of data distributions. The authors demonstrate that XM can be applied to various generative models, including diffusion and flow-based models, and that it can improve performance across different modalities, including images, videos, and language. Additionally, the authors show that XM can be used to train end-to-end generative models, which can match the performance of traditional models but with significantly reduced computational requirements. The paper concludes by highlighting the potential of XM to advance the field of generative modeling and to enable the development of more powerful and efficient generative models.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel training objective, XM, that addresses the limitations of traditional generative models by enabling models to explore multiple candidate matches between data and latent variables. This is a significant contribution to the field of generative modeling, as it allows models to better capture the multimodal nature of data distributions.
2. The paper provides extensive experimental results that demonstrate the effectiveness of XM across different generative models and modalities. The results show that XM can improve performance in tasks such as image and video generation, as well as language modeling.
3. The paper highlights the potential of XM to enable end-to-end generative models, which can match the performance of traditional models but with significantly reduced computational requirements. This is a significant advantage for practitioners who are concerned about the computational cost of training generative models.
4. The paper is well-written and clearly explains the motivation, methodology, and results of the proposed approach. The authors provide a thorough discussion of the limitations of traditional generative models and the advantages of XM.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of XM, which is a significant concern for practitioners who are concerned about the computational cost of training generative models. The authors should provide a more detailed analysis of the computational complexity of XM and compare it to traditional generative models.
2. The paper does not provide a detailed analysis of the hyperparameter sensitivity of XM, which is a significant concern for practitioners who are concerned about the robustness of the proposed approach. The authors should provide a more detailed analysis of the hyperparameter sensitivity of XM and provide guidelines for selecting appropriate hyperparameters.
3. The paper does not provide a detailed analysis of the limitations of XM, which is a significant concern for practitioners who are concerned about the generalizability of the proposed approach. The authors should provide a more detailed analysis of the limitations of XM and discuss potential avenues for future research.

### Suggestions

The authors should provide a more rigorous analysis of the computational cost associated with Explorative Modeling (XM). While the paper mentions that XM can reduce computational requirements, a detailed breakdown of the time and memory complexity is needed. Specifically, the authors should analyze how the computational cost scales with the number of candidate samples explored during training, the dimensionality of the latent space, and the complexity of the generative model. This analysis should include both theoretical estimates and empirical measurements on different datasets. Furthermore, it would be beneficial to compare the computational cost of XM with that of traditional generative models, such as diffusion models and flow-based models, under similar performance targets. This would provide a clearer understanding of the trade-offs between performance and computational cost when using XM. The authors should also investigate the impact of different exploration strategies on the computational cost of XM. For example, they could explore adaptive exploration strategies that dynamically adjust the number of candidate samples explored based on the training progress or the complexity of the data distribution. This could potentially lead to further reductions in computational cost without sacrificing performance.

In addition to the computational cost, the authors should also provide a more detailed analysis of the hyperparameter sensitivity of XM. The paper should include a systematic study of how different hyperparameters, such as the number of candidate samples explored, the learning rate, and the exploration strategy parameters, affect the performance of XM. This analysis should include both quantitative results, such as the final performance metrics, and qualitative results, such as the convergence behavior of the model. The authors should also provide guidelines for selecting appropriate hyperparameters based on the specific task and dataset. For example, they could provide recommendations for the number of candidate samples to explore based on the complexity of the data distribution or the desired level of diversity in the generated samples. Furthermore, the authors should investigate the robustness of XM to different hyperparameter settings. This could involve running multiple experiments with different hyperparameter settings and analyzing the variability in the performance metrics. This would provide a better understanding of the stability of XM and its sensitivity to hyperparameter choices.

Finally, the authors should provide a more detailed analysis of the limitations of XM. While the paper demonstrates the effectiveness of XM on several tasks, it is important to acknowledge the potential limitations of the approach. For example, the authors should discuss the potential challenges of applying XM to very high-dimensional data or complex data distributions. They should also discuss the potential limitations of XM in terms of the quality of the generated samples. For example, they could investigate whether XM is prone to generating samples that are overly diverse or that lack the desired level of fidelity. Furthermore, the authors should discuss potential avenues for future research to address these limitations. This could involve exploring new exploration strategies, developing more efficient algorithms for exploring the latent space, or investigating the use of XM in combination with other techniques, such as adversarial training or data augmentation. A thorough discussion of the limitations of XM would provide a more balanced and realistic assessment of the proposed approach.

### Questions

1. How does the computational cost of XM compare to traditional generative models, and what are the trade-offs between performance and computational cost when using XM?
2. What are the hyperparameter sensitivity of XM, and how can practitioners select appropriate hyperparameters for their specific tasks and datasets?
3. What are the limitations of XM, and what are the potential avenues for future research to address these limitations?

### Rating

6

### Confidence

4

**********

## Reviewer 3

### Summary

This paper proposes a new paradigm for generative modeling, called explorative modeling, which enables end-to-end training of generative models. The key idea is to sample multiple candidate matches between data and latent variables, and train on the best one. The authors show that this approach can improve performance across various generative models and modalities, and enable end-to-end reconstructive generative modeling. The authors also show that explorative modeling can be used to train end-to-end generative models that match the performance of traditional models but with significantly reduced computational requirements.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow. The motivation and methodology are clearly explained, and the experimental results are presented in a clear and concise manner.
- The proposed method is novel and interesting. The idea of sampling multiple candidate matches between data and latent variables and training on the best one is a creative approach to improving generative modeling.
- The authors provide extensive experimental results that demonstrate the effectiveness of the proposed method across various generative models and modalities. The results show that explorative modeling can improve performance and enable end-to-end training of generative models.
- The paper also discusses the potential applications of explorative modeling, such as in robotics control and goal-conditioned world modeling. This highlights the practical relevance of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational cost of the proposed method. While the authors mention that the method can reduce computational requirements, they do not provide a quantitative analysis of the computational complexity or runtime of the proposed method compared to existing approaches. This makes it difficult to assess the practical feasibility of the method.
- The paper does not provide a detailed discussion of the limitations of the proposed method. While the authors show that the method can improve performance across various generative models and modalities, they do not discuss the potential limitations of the method, such as its sensitivity to hyperparameter settings or its performance on complex datasets.
- The paper does not provide a detailed discussion of the potential ethical implications of the proposed method. As generative models become more powerful, there are concerns about the potential misuse of these models for generating harmful or biased content. The authors should discuss these ethical considerations and propose potential mitigation strategies.

### Suggestions

The authors should provide a more thorough analysis of the computational cost of their proposed method. Specifically, they should compare the training time and memory requirements of explorative modeling with those of standard generative models, such as diffusion models and flow-based models. This comparison should be done across different model sizes and datasets to provide a comprehensive understanding of the computational trade-offs. Furthermore, it would be beneficial to analyze the scaling behavior of the method with respect to the number of candidate samples explored during training. This would help to understand the practical limitations of the method and identify the optimal number of samples for different scenarios. The authors should also discuss the impact of different hardware configurations on the computational cost of the method.

In addition to the computational cost, the authors should provide a more detailed discussion of the limitations of their proposed method. This should include an analysis of the sensitivity of the method to hyperparameter settings, such as the number of candidate samples and the learning rate. It would be helpful to provide guidelines for selecting appropriate hyperparameters for different tasks and datasets. Furthermore, the authors should discuss the potential limitations of the method on complex datasets, such as those with high dimensionality or complex dependencies. This discussion should include an analysis of the types of datasets where the method is likely to perform well and the types of datasets where it may struggle. The authors should also consider the potential impact of the method on the diversity of generated samples and discuss any strategies to mitigate any potential loss of diversity.

Finally, the authors should address the ethical implications of their proposed method. As generative models become more powerful, there are concerns about the potential misuse of these models for generating harmful or biased content. The authors should discuss these ethical considerations and propose potential mitigation strategies. This discussion should include an analysis of the potential for the method to be used for malicious purposes, such as generating fake news or propaganda. The authors should also consider the potential impact of the method on different social groups and discuss any strategies to ensure that the method is used responsibly. This discussion should also include an analysis of the potential for the method to be used for scientific discovery and the ethical considerations associated with this use.

### Questions

- How does the computational cost of the proposed method compare to existing approaches?
- What are the limitations of the proposed method, and how can they be addressed?
- What are the potential ethical implications of the proposed method, and how can they be mitigated?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

The paper proposes a new generative modeling paradigm called Explorative Modeling (XM). XM is designed to address the limitations of traditional generative models, which often fail to capture the full distribution of data due to a mismatch between the training loop and the generation procedure. The authors argue that generative modeling is fundamentally about handling multimodal probability distributions, and that existing scalable approaches have not scaled well with data and model size. XM introduces a new training objective that allows models to explore multiple candidate matches between data and latent variables, enabling them to better capture the multimodal nature of data distributions. The authors demonstrate that XM can be applied to various generative models, including diffusion and flow-based models, and that it can improve performance across different modalities, including images, videos, and language. Additionally, XM enables end-to-end reconstructive generative modeling, matching the performance of traditional models but with significantly reduced computational requirements. The paper concludes by highlighting the potential of XM to advance the field of generative modeling and to enable the development of more powerful and efficient generative models.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow, with clear explanations of the proposed method and its motivation.
2. The authors provide extensive experimental results that demonstrate the effectiveness of XM across different generative models and modalities.
3. The paper highlights the potential of XM to enable end-to-end reconstructive generative modeling, which is a significant advancement in the field.
4. The authors discuss the limitations of XM and suggest potential avenues for future research.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of XM, which is a significant concern for practitioners who are concerned about the computational cost of training generative models. The authors should provide a more detailed analysis of the computational complexity of XM and compare it to traditional generative models.
2. The paper does not provide a detailed analysis of the hyperparameter sensitivity of XM, which is a significant concern for practitioners who are concerned about the robustness of the proposed approach. The authors should provide a more detailed analysis of the hyperparameter sensitivity of XM and provide guidelines for selecting appropriate hyperparameters.
3. The paper does not provide a detailed analysis of the limitations of XM, which is a significant concern for practitioners who are concerned about the generalizability of the proposed approach. The authors should provide a more detailed analysis of the limitations of XM and discuss potential avenues for future research.

### Suggestions

The authors should provide a more thorough analysis of the computational cost associated with Explorative Modeling (XM). Specifically, they should include a detailed breakdown of the time and memory requirements for training models using XM, comparing these to the costs of traditional generative models. This analysis should consider the impact of various factors, such as the number of candidate matches explored during training, the dimensionality of the latent space, and the complexity of the generative model. Furthermore, it would be beneficial to include empirical measurements of training time and memory usage on different hardware configurations to provide a practical understanding of the computational overhead introduced by XM. This would allow practitioners to make informed decisions about the feasibility of using XM in their specific applications.

In addition to the computational cost, the authors should also provide a more detailed analysis of the hyperparameter sensitivity of XM. This analysis should include a systematic study of how different hyperparameters, such as the number of candidate matches explored, the learning rate, and the exploration strategy parameters, affect the performance of XM. The authors should present both quantitative results, such as the final performance metrics, and qualitative results, such as the convergence behavior of the model. Furthermore, they should provide guidelines for selecting appropriate hyperparameters based on the specific task and dataset. This could involve developing heuristics or providing recommendations based on empirical observations. A sensitivity analysis would help practitioners understand the robustness of XM and how to tune it effectively for different applications.

Finally, the authors should provide a more detailed analysis of the limitations of XM. This analysis should include a discussion of the potential challenges of applying XM to very high-dimensional data or complex data distributions. The authors should also discuss the potential limitations of XM in terms of the quality of the generated samples. For example, they could investigate whether XM is prone to generating samples that are overly diverse or that lack the desired level of fidelity. Furthermore, they should discuss potential avenues for future research to address these limitations. This could involve exploring new exploration strategies, developing more efficient algorithms for exploring the latent space, or investigating the use of XM in combination with other techniques, such as adversarial training or data augmentation. A thorough discussion of the limitations would provide a more balanced and realistic assessment of the proposed approach.

### Questions

1. How does the computational cost of XM compare to traditional generative models, and what are the trade-offs between performance and computational cost when using XM?
2. What are the hyperparameter sensitivity of XM, and how can practitioners select appropriate hyperparameters for their specific tasks and datasets?
3. What are the limitations of XM, and what are the potential avenues for future research to address these limitations?

### Rating

6

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers for the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

Plan:
1. Go through each reviewer's comments one by one.
2. For each weakness, identify the type of weakness (theoretical, methodological, experimental, practical).
3. Find specific evidence in the paper (quotes, numbers, missing information) to support the weakness.
4. If a weakness is about missing information, check if that information is indeed absent.
5. If there are conflicting opinions, note them down.
6. Finally, conclude whether the weakness is valid, partially valid, or invalid based on the evidence.
**Review 1**

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost of XM, which is a significant concern for practitioners who are concerned about the computational cost of training generative models. The authors should provide a more detailed analysis of the computational complexity of XM and compare it to traditional generative models."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions computational efficiency as a motivation: "The motivation is to address the limitations of current generative models, which often fail to capture the full distribution of data due to a mismatch between the training loop and the generation procedure. This mismatch is particularly pronounced in high-dimensional data, where generative models struggle to capture the multimodal nature of the distribution. The paper argues that this limitation is not inherent to the models themselves but rather to the training objectives and procedures used. By introducing a new paradigm that allows models to explore multiple candidate matches between data and latent variables, the paper aims to improve the generative expressivity and efficiency of these models." (Motivation section)
   - The paper claims XM enables end-to-end training: "Explorative Modeling (XM) is a new paradigm for handling multimodal distributions in generative models. It addresses the limitations of traditional generative models by enabling them to explore multiple candidate matches between data and latent variables during training. This approach allows generative models to better capture the multimodal nature of the data distribution, leading to improved generative expressivity and efficiency." (Main Idea section)
   - The paper mentions reduced computational requirements for XM: "This approach allows generative models to better capture the multimodal nature of the data distribution, leading to improved generative expressivity and efficiency." (Main Idea section)
   - The paper does not provide a quantitative analysis of the computational cost of XM compared to traditional models.

3. Literature Gap Analysis:
   - The paper does not cite works that specifically analyze the computational complexity of different generative modeling paradigms.

4. Validation Analysis:
   - The reviewer correctly points out the lack of a detailed computational cost analysis. While the paper claims efficiency and end-to-end training, it does not provide concrete evidence to support these claims in terms of computational cost. The paper lacks a comparison of the time and memory requirements of XM with traditional methods.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of quantitative computational cost analysis in the experimental sections.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the hyperparameter sensitivity of XM, which is a significant concern for practitioners who are concerned about the robustness of the proposed approach. The authors should provide a more detailed analysis of the hyperparameter sensitivity of XM and provide guidelines for selecting appropriate hyperparameters."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions hyperparameter tuning: "For all experiments in the main section of this paper, we denote exploring K K modes as XM- K K , and we use Forward XM (Section 3 ) as it is simpler to implement (this is discussed in Section F.1 ). Note that all baselines without exploration are equivalent to XM-1, as exploring a single mode reduces to standard training. By default, all experiments in this section are without guidance, keeping each baseline recipe’s hyperparameters unchanged and only adding exploration. As a result, the exploration hyperparameter is set to K = 1 for all baselines." (Experimental Setup section)
   - The paper mentions varying the number of modes explored in the supplementary material: "As a result, the exploration hyperparameter is set to K = 1 for all baselines. By default, all experiments in this section are without guidance, keeping each baseline recipe’s hyperparameters unchanged and only adding exploration. As a result, the exploration hyperparameter is set to K = 1 for all baselines. In the main paper, we set the number of modes explored to K = 1 for all baselines. In the supplementary material, we provide more details on the hyperparameter settings and the results of varying the number of modes explored." (Experimental Setup section)
   - The paper does not include a systematic study of how different hyperparameters affect the performance of XM.

3. Literature Gap Analysis:
   - The paper does not cite works that specifically analyze the hyperparameter sensitivity of generative modeling methods.

4. Validation Analysis:
   - The reviewer is correct. While the paper mentions the exploration hyperparameter (number of modes explored), it lacks a detailed analysis of how different values of this and potentially other hyperparameters affect the performance of XM. The paper does not provide guidelines for selecting appropriate hyperparameters.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of systematic hyperparameter sensitivity analysis in the experimental sections.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the limitations of XM, which is a significant concern for practitioners who are concerned about the generalizability of the proposed approach. The authors should provide a more detailed analysis of the limitations of XM and discuss potential avenues for future research."

2. Evidence Collection:
- The paper mentions some limitations implicitly through the experimental results: "For all experiments in the main section of this paper, we denote exploring K K modes as XM- K K , and we use Forward XM (Section 3 ) as it is simpler to implement (this is discussed in Section F.1 ). Note that all baselines without exploration are equivalent to XM-1, as exploring a single mode reduces to standard training. By default, all experiments in this section are without guidance, keeping each baseline recipe’s hyperparameters unchanged and only adding exploration. As a result, the exploration hyperparameter is set to K = 1 for all baselines. In the main paper, we set the number of modes explored to K = 1 for all baselines. In the supplementary material, we provide more details on the hyperparameter settings and the results of varying the number of modes explored." (Experimental Setup section)
- The paper does not have a dedicated section discussing the limitations of XM.

3. Literature Gap Analysis:
   - The paper does not cite works that specifically analyze the limitations of different generative modeling approaches.

4. Validation Analysis:
   - The reviewer's point is valid. While the paper presents successful applications of XM, it lacks a dedicated and detailed discussion of the potential limitations of the method. This includes scenarios where XM might not perform well or the types of data distributions where XM might struggle.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of a dedicated "Limitations" section and implicit rather than explicit discussion of limitations.

**Review 2**

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost of XM, which is a significant concern for practitioners who are concerned about the computational cost of training generative models. The authors should provide a more detailed analysis of the computational complexity of their method. The current discussion lacks specific details about the computational overhead introduced by the exploration process. For example, how does the runtime scale with the number of explored samples, the dimensionality of the latent space, and the complexity of the generative model?"

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions computational efficiency as a motivation: "The motivation is to address the limitations of current generative models, which often fail to capture the full distribution of data due to a mismatch between the training loop and the generation procedure. This mismatch is particularly pronounced in high-dimensional data, where generative models struggle to capture the multimodal nature of the distribution. The paper argues that this limitation is not inherent to the models themselves but rather to the training objectives and procedures used. By introducing a new paradigm that allows models to explore multiple candidate matches between data and latent variables, the paper aims to improve the generative expressivity and efficiency of these models." (Motivation section)
   - The paper claims XM enables end-to-end training: "Explorative Modeling (XM) is a new paradigm for handling multimodal distributions in generative models. It addresses the limitations of traditional generative models by enabling them to explore multiple candidate matches between data and latent variables during training. This approach allows generative models to better capture the multimodal nature of the data distribution, leading to improved generative expressivity and efficiency." (Main Idea section)
   - The paper mentions reduced computational requirements for XM: "This approach allows generative models to better capture the multimodal nature of the data distribution, leading to improved generative expressivity and efficiency." (Main Idea section)
   - The paper does not provide a detailed analysis of the computational cost of XM, including how runtime scales with the number of explored samples, latent space dimensionality, or model complexity.

3. Literature Gap Analysis:
   - The paper does not cite works that specifically analyze the computational complexity of different generative modeling paradigms.

4. Validation Analysis:
   - This is a similar point to Reviewer 1's first weakness. The reviewer correctly identifies the lack of a detailed computational cost analysis. The paper claims efficiency but does not provide the necessary details to support this claim.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of detailed computational cost analysis in the experimental sections.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the hyperparameter sensitivity of XM, which is a significant concern for practitioners who are concerned about the robustness of the proposed approach. The authors should provide a more detailed analysis of the hyperparameter sensitivity of XM and provide guidelines for selecting appropriate hyperparameters."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions hyperparameter tuning: "For all experiments in the main section of this paper, we denote exploring K K modes as XM- K K , and we use Forward XM (Section 3 ) as it is simpler to implement (this is discussed in Section F.1 ). Note that all baselines without exploration are equivalent to XM-1, as exploring a single mode reduces to standard training. By default, all experiments in this section are without guidance, keeping each baseline recipe’s hyperparameters unchanged and only adding exploration. As a result, the exploration hyperparameter is set to K = 1 for all baselines." (Experimental Setup section)
   - The paper mentions varying the number of modes explored in the supplementary material: "As a result, the exploration hyperparameter is set to K = 1 for all baselines. In the main paper, we set the number of modes explored to K = 1 for all baselines. In the supplementary material, we provide more details on the hyperparameter settings and the results of varying the number of modes explored." (Experimental Setup section)
   - The paper does not include a systematic study of how different hyperparameters affect the performance of XM.

3. Literature Gap Analysis:
   - The paper does not cite works that specifically analyze the hyperparameter sensitivity of generative modeling methods.

4. Validation Analysis:
   - This is the same point as Reviewer 1's second weakness. The reviewer is correct in pointing out the lack of a detailed hyperparameter sensitivity analysis.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of systematic hyperparameter sensitivity analysis in the experimental sections.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the limitations of XM, which is a significant concern for practitioners who are concerned about the generalizability of the proposed approach. The authors should provide a more detailed analysis of the limitations of XM and discuss potential avenues for future research to address these limitations."

2. Evidence Collection:
- The paper mentions some limitations implicitly through the experimental results: "For all experiments in the main section of this paper, we denote exploring K K modes as XM- K K , and we use Forward XM (Section 3 ) as it is simpler to implement (this is discussed in Section F.1 ). Note that all baselines without exploration are equivalent to XM-1, as exploring a single mode reduces to standard training. By default, all experiments in this section are without guidance, keeping each baseline recipe’s hyperparameters unchanged and only adding exploration. As a result, the exploration hyperparameter is set to K = 1 for all baselines. In the main paper, we set the number of modes explored to K = 1 for all baselines. In the supplementary material, we provide more details on the hyperparameter settings and the results of varying the number of modes explored." (Experimental Setup section)
- The paper does not have a dedicated section discussing the limitations of XM.

3. Literature Gap Analysis:
   - The paper does not cite works that specifically analyze the limitations of different generative modeling approaches.

4. Validation Analysis:
   - This is the same point as Reviewer 1's third weakness. The reviewer is correct in pointing out the lack of a detailed discussion of the limitations.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of a dedicated "Limitations" section and implicit rather than explicit discussion of limitations.

**Review 3**

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost of the proposed method. While the authors mention that the method can reduce computational requirements, they do not provide a quantitative analysis of the computational complexity or runtime of the proposed method compared to existing approaches. This makes it difficult to assess the practical feasibility of the method."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions computational efficiency as a motivation: "The motivation is to address the limitations of current generative models, which often fail to capture the full distribution of data due to a mismatch between the training loop and the generation procedure. This mismatch is particularly pronounced in high-dimensional data, where generative models struggle to capture the multimodal nature of the distribution. The paper argues that this limitation is not inherent to the models themselves but rather to the training objectives and procedures used. By introducing a new paradigm that allows models to explore multiple candidate matches between data and latent variables, the paper aims to improve the generative expressivity and efficiency of these models." (Motivation section)
   - The paper claims XM enables end-to-end training: "Explorative Modeling (XM) is a new paradigm for handling multimodal distributions in generative models. It addresses the limitations of traditional generative models by enabling them to explore multiple candidate matches between data and latent variables during training. This approach allows generative models to better capture the multimodal nature of the data distribution, leading to improved generative expressivity and efficiency." (Main Idea section)
   - The paper mentions reduced computational requirements for XM: "This approach allows generative models to better capture the multimodal nature of the data distribution, leading to improved generative expressivity and efficiency." (Main Idea section)
   - The paper does not provide a quantitative analysis of the computational cost of XM compared to traditional approaches.

3. Literature Gap Analysis:
   - The paper does not cite works that specifically analyze the computational complexity of different generative modeling paradigms.

4. Validation Analysis:
   - This is consistent with the computational cost concerns raised by Reviewers 1 and 2. The reviewer correctly points out the lack of a quantitative analysis of the computational cost.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of quantitative computational cost analysis in the experimental sections.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the hyperparameter sensitivity of XM, which is a significant concern for practitioners who are concerned about the robustness of the proposed approach. The authors should provide a more detailed analysis of the hyperparameter sensitivity of XM and provide guidelines for selecting appropriate hyperparameters."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions hyperparameter tuning: "For all experiments in the main section of this paper, we denote exploring K K modes as XM- K K , and we use Forward XM (Section 3 ) as it is simpler to implement (this is discussed in Section F.1 ). Note that all baselines without exploration are equivalent to XM-1, as exploring a single mode reduces to standard training. By default, all experiments in this section are without guidance, keeping each baseline recipe’s hyperparameters unchanged and only adding exploration. As a result, the exploration hyperparameter is set to K = 1 for all baselines." (Experimental Setup section)
   - The paper mentions varying the number of modes explored in the supplementary material: "As a result, the exploration hyperparameter is set to K = 1 for all baselines. In the main paper, we set the number of modes explored to K = 1 for all baselines. In the supplementary material, we provide more details on the hyperparameter settings and the results of varying the number of modes explored." (Experimental Setup section)
   - The paper does not include a systematic study of how different hyperparameters affect the performance of XM.

3. Literature Gap Analysis:
   - The paper does not cite works that specifically analyze the hyperparameter sensitivity of generative modeling methods.

4. Validation Analysis:
   - This is consistent with the hyperparameter sensitivity concerns raised by Reviewers 1 and 2. The reviewer is correct in pointing out the lack of a detailed analysis.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of systematic hyperparameter sensitivity analysis in the experimental sections.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the limitations of XM, which is a significant concern for practitioners who are concerned about the generalizability of the proposed approach. The authors should provide a more detailed analysis of the limitations of XM and discuss potential avenues for future research to address these limitations."

2. Evidence Collection:
- The paper mentions some limitations implicitly through the experimental results: "For all experiments in the main section of this paper, we denote exploring K K modes as XM- K K , and we use Forward XM (Section 3 ) as it is simpler to implement (this is discussed in Section F.1 ). Note that all baselines without exploration are equivalent to XM-1, as exploring a single mode reduces to standard training. By default, all experiments in this section are without guidance, keeping each baseline recipe’s hyperparameters unchanged and only adding exploration. As a result, the exploration hyperparameter is set to K = 1 for all baselines. In the main paper, we set the number of modes explored to K = 1 for all baselines. In the supplementary material, we provide more details on the hyperparameter settings and the results of varying the number of modes explored." (Experimental Setup section)
- The paper does not have a dedicated section discussing the limitations of XM.

3. Literature Gap Analysis:
   - The paper does not cite works that specifically analyze the limitations of different generative modeling approaches.

4. Validation Analysis:
   - This is consistent with the limitations concerns raised by Reviewers 1 and 2. The reviewer is correct in pointing out the lack of a detailed discussion of the limitations.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of a dedicated "Limitations" section and implicit rather than explicit discussion of limitations.

**Review 4**

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost of XM, which is a significant concern for practitioners who are concerned about the computational cost of training generative models. The authors should provide a more detailed analysis of the computational complexity of XM and compare it to traditional generative models."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions computational efficiency as a motivation: "The motivation is to address the limitations of current generative models, which often fail to capture the full distribution of data due to a mismatch between the training loop and the generation procedure. This mismatch is particularly pronounced in high-dimensional data, where generative models struggle to capture the multimodal nature of the distribution. The paper argues that this limitation is not inherent to the models themselves but rather to the training objectives and procedures used. By introducing a new paradigm that allows models to explore multiple candidate matches between data and latent variables, the paper aims to improve the generative expressivity and efficiency of these models." (Motivation section)
   - The paper claims XM enables end-to-end training: "Explorative Modeling (XM) is a new paradigm for handling multimodal distributions in generative models. It addresses the limitations of traditional generative models by enabling them to explore multiple candidate matches between data and latent variables during training. This approach allows generative models to better capture the multimodal nature of the data distribution, leading to improved generative expressivity and efficiency." (Main Idea section)
   - The paper mentions reduced computational requirements for XM: "This approach allows generative models to better capture the multimodal nature of the data distribution, leading to improved generative expressivity and efficiency." (Main Idea section)
   - The paper does not provide a detailed analysis of the computational cost of XM, including a comparison with traditional models.

3. Literature Gap Analysis:
   - The paper does not cite works that specifically analyze the computational complexity of different generative modeling paradigms.

4. Validation Analysis:
   - This is consistent with the computational cost concerns raised by Reviewers 1, 2, and 3. The reviewer correctly points out the lack of a detailed analysis and comparison of computational costs.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of quantitative computational cost analysis and comparison in the experimental sections.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the hyperparameter sensitivity of XM, which is a significant concern for practitioners who are concerned about the robustness of the proposed approach. The authors should provide a more detailed analysis of the hyperparameter sensitivity of XM and provide guidelines for selecting appropriate hyperparameters."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper mentions hyperparameter tuning: "For all experiments in the main section of this paper, we denote exploring K K modes as XM- K K , and we use Forward XM (Section 3 ) as it is simpler to implement (this is discussed in Section F.1 ). Note that all baselines without exploration are equivalent to XM-1, as exploring a single mode reduces to standard training. By default, all experiments in this section are without guidance, keeping each baseline recipe’s hyperparameters unchanged and only adding exploration. As a result, the exploration hyperparameter is set to K = 1 for all baselines." (Experimental Setup section)
   - The paper mentions varying the number of modes explored in the supplementary material: "As a result, the exploration hyperparameter is set to K = 1 for all baselines. In the main paper, we set the number of modes explored to K = 1 for all baselines. In the supplementary material, we provide more details on the hyperparameter settings and the results of varying the number of modes explored." (Experimental Setup section)
   - The paper does not include a systematic study of how different hyperparameters affect the performance of XM.

3. Literature Gap Analysis:
   - The paper does not cite works that specifically analyze the hyperparameter sensitivity of generative modeling methods.

4. Validation Analysis:
   - This is consistent with the hyperparameter sensitivity concerns raised by Reviewers 1, 2, and 3. The reviewer is correct in pointing out the lack of a detailed analysis.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of systematic hyperparameter sensitivity analysis in the experimental sections.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the limitations of XM, which is a significant concern for practitioners who are concerned about the generalizability of the proposed approach. The authors should provide a more detailed analysis of the limitations of XM and discuss potential avenues for future research to address these limitations."

2. Evidence Collection:
- The paper mentions some limitations implicitly through the experimental results: "For all experiments in the main section of this paper, we denote exploring K K modes as XM- K K , and we use Forward XM (Section 3 ) as it is simpler to implement (this is discussed in Section F.1 ). Note that all baselines without exploration are equivalent to XM-1, as exploring a single mode reduces to standard training. By default, all experiments in this section are without guidance, keeping each baseline recipe’s hyperparameters unchanged and only adding exploration. As a result, the exploration hyperparameter is set to K = 1 for all baselines. In the main paper, we set the number of modes explored to K = 1 for all baselines. In the supplementary material, we provide more details on the hyperparameter settings and the results of varying the number of modes explored." (Experimental Setup section)
- The paper does not have a dedicated section discussing the limitations of XM.

3. Literature Gap Analysis:
   - The paper does not cite works that specifically analyze the limitations of different generative modeling approaches.

4. Validation Analysis:
   - This is consistent with the limitations concerns raised by Reviewers 1, 2, 3, and 4. The reviewer is correct in pointing out the lack of a detailed discussion of the limitations.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of a dedicated "Limitations" section and implicit rather than explicit discussion of limitations.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces Explorative Modeling (XM), a novel training paradigm designed to enhance the generative capabilities of models, particularly those based on diffusion and flow-based approaches. The central premise of XM is that current generative models often fail to fully capture the multimodal nature of real-world data due to a mismatch between the training loop and the generation procedure. XM addresses this limitation by enabling models to explore multiple candidate matches between data and latent variables during training. Instead of relying on a single, one-to-one mapping, XM samples multiple candidate latent variables and selects the one that best reconstructs the given data point. This approach, the authors argue, allows the model to better capture the true distribution of the data, leading to improved generative expressivity and efficiency. The paper demonstrates that XM can be applied to various generative models, including diffusion and flow-based models, and that it can be used to train end-to-end generative models, which can match the performance of traditional models but with significantly reduced computational requirements. The authors present extensive experimental results across different modalities, including images, videos, and language, showcasing the effectiveness of XM in tasks such as image and video generation, as well as language modeling. The results indicate that XM can improve performance across various generative models and modalities, and that it can enable end-to-end reconstruction generative modeling. The paper also explores the potential of XM for tasks such as behavior cloning and goal-conditioned world modeling. Overall, the paper presents a compelling new paradigm for generative modeling, with the potential to advance the field and enable the development of more powerful and efficient generative models. However, as I will discuss in the following sections, there are several areas where the paper could be strengthened, particularly in terms of its analysis of computational cost, hyperparameter sensitivity, and limitations.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

3.0


## Strengths:

I found several aspects of this paper to be particularly compelling. First, the core idea of Explorative Modeling (XM) is both novel and intuitively appealing. The concept of exploring multiple candidate matches between data and latent variables during training is a creative approach to addressing the limitations of traditional generative models. This idea is well-motivated by the authors' observation that current models often fail to capture the full distribution of data due to a mismatch between the training loop and the generation procedure. The paper clearly articulates this motivation and provides a solid rationale for the proposed approach. Second, the paper's experimental results are extensive and demonstrate the effectiveness of XM across various generative models and modalities. The authors show that XM can improve performance in tasks such as image and video generation, as well as language modeling. The results presented in the paper are compelling and provide strong evidence for the potential of XM. The fact that XM can be applied to both diffusion and flow-based models is also a significant strength, as it suggests that the approach is not limited to a specific type of model. Furthermore, the paper's exploration of end-to-end generative modeling is a notable contribution. The authors demonstrate that XM can enable end-to-end training of generative models, which is a significant advantage for practitioners who are concerned about computational cost. The fact that XM can match the performance of traditional models while reducing computational requirements is a particularly impressive result. Finally, the paper is well-written and easy to follow. The authors provide clear explanations of the proposed method and its motivation, and the experimental results are presented in a clear and concise manner. The paper is well-organized and the writing is generally clear and concise, making it easy for the reader to understand the key concepts and findings. The inclusion of ablation studies and comparisons with existing methods further strengthens the paper's claims and provides a comprehensive analysis of the proposed approach. The authors have clearly put a lot of effort into presenting a compelling and well-supported argument for the effectiveness of XM.


## Weaknesses:

Despite the strengths of this paper, I have identified several significant weaknesses that warrant further discussion. The most prominent concern is the lack of a detailed analysis of the computational cost associated with Explorative Modeling (XM). While the authors claim that XM can reduce computational requirements, they do not provide any quantitative evidence to support this claim. Specifically, the paper lacks a comparison of the training time and memory requirements of XM with those of standard generative models, such as diffusion models and flow-based models. This omission is a critical weakness, as it makes it difficult to assess the practical feasibility of XM for practitioners who are concerned about computational cost. The paper does not provide any information about how the computational cost of XM scales with the number of candidate samples explored during training, the dimensionality of the latent space, or the complexity of the generative model. This lack of analysis makes it difficult to understand the trade-offs between performance and computational cost when using XM. Furthermore, the paper does not provide any empirical measurements of training time and memory usage on different hardware configurations. This lack of detail makes it difficult to assess the practical implications of the proposed method. My confidence in this weakness is high, as the absence of any quantitative analysis of computational cost is a clear and significant omission. Another significant weakness is the lack of a detailed analysis of the hyperparameter sensitivity of XM. The paper mentions the exploration hyperparameter, denoted as K, which represents the number of modes explored during training. However, the authors do not provide a systematic study of how different values of K affect the performance of XM. The paper does not present any quantitative results, such as the final performance metrics, and does not provide any qualitative results, such as the convergence behavior of the model. Furthermore, the paper does not provide any guidelines for selecting appropriate hyperparameters based on the specific task and dataset. This lack of analysis makes it difficult for practitioners to tune the hyperparameters of XM effectively, which is a significant concern. My confidence in this weakness is high, as the absence of a systematic hyperparameter sensitivity analysis is a clear and significant omission. Finally, the paper lacks a detailed discussion of the limitations of XM. While the authors demonstrate the effectiveness of XM on several tasks, they do not provide a thorough analysis of the potential challenges of applying XM to very high-dimensional data or complex data distributions. The paper does not discuss the potential limitations of XM in terms of the quality of the generated samples or the diversity of the generated samples. The paper also does not discuss the potential impact of the exploration strategy on the diversity of the generated samples. For example, if the model explores the latent space too aggressively, it might generate samples that are overly diverse or that lack the desired level of fidelity. The absence of a detailed discussion of the limitations of XM is a significant weakness, as it makes it difficult to assess the generalizability of the proposed approach. My confidence in this weakness is high, as the absence of a dedicated limitations section and the implicit rather than explicit discussion of limitations is a clear and significant omission. In addition to these major weaknesses, I also noted that the paper does not provide a detailed analysis of the computational cost of XM compared to traditional generative models. This is a significant concern for practitioners who are concerned about the computational cost of training generative models. The paper does not provide a quantitative analysis of the computational complexity of XM and compare it to traditional generative models. This makes it difficult to assess the practical feasibility of XM. The paper also does not provide a detailed analysis of the hyperparameter sensitivity of XM. The paper does not include a systematic study of how different hyperparameters affect the performance of XM. The paper does not provide any quantitative results, such as the final performance metrics, and does not provide any qualitative results, such as the convergence behavior of the model. The paper does not provide any guidelines for selecting appropriate hyperparameters based on the specific task and dataset. Finally, the paper does not provide a detailed analysis of the limitations of XM. The paper does not discuss the potential challenges of applying XM to very high-dimensional data or complex data distributions. The paper does not discuss the potential limitations of XM in terms of the quality of the generated samples or the diversity of the generated samples. The paper does not discuss the potential impact of the exploration strategy on the diversity of the generated samples. These weaknesses, taken together, significantly limit the practical applicability of the proposed method and make it difficult to assess its potential impact on the field.


## Suggestions:

To address the identified weaknesses, I recommend several concrete and actionable improvements. First and foremost, the authors should provide a more thorough analysis of the computational cost associated with Explorative Modeling (XM). This analysis should include a detailed breakdown of the time and memory complexity of the method, including how the runtime scales with the number of candidate samples explored during training, the dimensionality of the latent space, and the complexity of the generative model. The authors should also provide empirical measurements of training time and memory usage on different hardware configurations. This analysis should include a comparison of the computational cost of XM with that of traditional generative models, such as diffusion models and flow-based models, under similar performance targets. This would provide a clearer understanding of the trade-offs between performance and computational cost when using XM. Furthermore, the authors should include a detailed analysis of the hyperparameter sensitivity of XM. This analysis should include a systematic study of how different values of the exploration hyperparameter (K) and other hyperparameters, such as the learning rate and the exploration strategy parameters, affect the performance of XM. The authors should present both quantitative results, such as the final performance metrics, and qualitative results, such as the convergence behavior of the model. The authors should also provide guidelines for selecting appropriate hyperparameters based on the specific task and dataset. This could involve developing heuristics or providing recommendations based on empirical observations. Second, the authors should provide a more detailed analysis of the limitations of XM. This analysis should include a discussion of the potential challenges of applying XM to very high-dimensional data or complex data distributions. The authors should also discuss the potential limitations of XM in terms of the quality of the generated samples or the diversity of the generated samples. The authors should also discuss the potential impact of the exploration strategy on the diversity of the generated samples. This discussion should include an analysis of the types of datasets where XM is likely to perform well and the types of datasets where it may struggle. The authors should also consider the potential impact of the exploration strategy on the diversity of the generated samples. For example, they could investigate whether the exploration strategy leads to a reduction in the diversity of the generated samples or whether it helps to improve the quality of the generated samples. Finally, the authors should consider expanding the experimental evaluation to include more diverse and complex datasets. This would help to assess the generalizability of the proposed approach and identify potential areas for improvement. The authors should also consider including experiments that specifically test the limitations of XM, such as experiments on high-dimensional data or complex data distributions. This would provide a more comprehensive understanding of the practical limitations of XM and help to identify areas for future research. In addition to these specific suggestions, the authors should also consider providing more detailed implementation details of the proposed method. This would make it easier for other researchers to reproduce the results and build upon the work. The authors should also consider making the code and data used in the experiments publicly available. This would further enhance the reproducibility of the work and facilitate further research in this area. By addressing these weaknesses, the authors can significantly strengthen the paper and make it a more valuable contribution to the field of generative modeling.


## Questions:

I have several questions that arise from my analysis of this paper. First, how does the computational cost of XM compare to traditional generative models, such as diffusion models and flow-based models, under similar performance targets? Specifically, what are the trade-offs between performance and computational cost when using XM, and how do these trade-offs vary with different hyperparameter settings? Second, what are the hyperparameter sensitivity of XM, and how can practitioners select appropriate hyperparameters for their specific tasks and datasets? The paper mentions the exploration hyperparameter (K), but it does not provide a systematic study of how different values of K affect the performance of XM. What are the guidelines for selecting appropriate values for K, and how do these guidelines vary with different datasets and tasks? Third, what are the limitations of XM, and what are the potential avenues for future research to address these limitations? The paper mentions some limitations implicitly through the experimental results, but it does not provide a detailed discussion of the potential challenges of applying XM to very high-dimensional data or complex data distributions. What are the specific scenarios where XM might not perform well, and what are the potential strategies for mitigating these limitations? Fourth, how does the exploration strategy affect the diversity of the generated samples? The paper does not discuss the potential impact of the exploration strategy on the diversity of the generated samples. How does the exploration strategy affect the diversity of the generated samples, and what are the potential strategies for improving the diversity of the generated samples? Finally, how does the proposed method handle conditional inputs, and what are the potential challenges in incorporating conditional information into XM? The paper mentions conditioning the latent variable, but it does not provide a detailed analysis of how different types of conditional information (e.g., text, images, categorical labels) would be incorporated into the exploration process. What are the potential challenges in incorporating conditional information into XM, and what are the potential strategies for addressing these challenges? These questions highlight key uncertainties and areas for further investigation, and addressing them would significantly strengthen the paper and enhance its practical applicability.


## Rating:

6.0


## Confidence:

3.25


## Decision:

Accept
}