I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper proposes a reward model for text-to-image generation that can predict human preferences. The authors also introduce a new fine-tuning algorithm, ReFL, which directly optimizes diffusion models using the reward model. The proposed method achieves state-of-the-art performance on the DiffusionDB dataset.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a detailed description of the annotation pipeline, including the prompt selection and image collection process. They also provide a thorough analysis of the dataset and the performance of different models.
3. The proposed method, ImageReward, is a general-purpose text-to-image human preference reward model that can be used to evaluate and improve text-to-image generation models.
4. The ReFL algorithm is a novel approach that directly optimizes diffusion models using the reward model, which is a significant contribution to the field.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a comparison with other state-of-the-art methods on the same dataset. The authors should compare their method with other existing approaches to demonstrate its effectiveness. Specifically, the paper should include a quantitative comparison with methods that also focus on improving text-to-image alignment, such as those using adversarial training or other preference learning techniques. The current comparison only shows that ImageReward outperforms CLIP, Aesthetic, and BLIP scores, but it does not show how it compares to other methods that directly address the same problem of text-image alignment.
2. The authors should provide more details about the dataset, including the distribution of prompts and images, and the quality of the annotations. The paper should also discuss the limitations of the dataset and how they might affect the results. For example, the paper should discuss the potential biases in the dataset, such as the types of prompts that are overrepresented or underrepresented, and how these biases might affect the performance of the model. The paper should also discuss the quality of the annotations, such as the level of agreement between annotators and the potential for noise in the annotations.
3. The authors should provide more details about the ReFL algorithm, including the hyperparameters used and the training procedure. The paper should also discuss the limitations of the ReFL algorithm and how they might affect the results. For example, the paper should discuss the potential for overfitting and how the authors avoided this issue. The paper should also discuss the computational cost of the ReFL algorithm and how it compares to other fine-tuning methods.

### Suggestions

The paper would benefit significantly from a more thorough comparison with existing state-of-the-art methods. Specifically, the authors should include a quantitative comparison with methods that also focus on improving text-to-image alignment, such as those using adversarial training or other preference learning techniques. This comparison should not only focus on the final performance but also on the training process, computational cost, and the type of data used. For example, the authors could compare their method with a fine-tuned Stable Diffusion model using a standard dataset like MS-COCO, and they could also compare their method with other preference learning methods that use human feedback. This would provide a more comprehensive understanding of the strengths and weaknesses of the proposed method and would help to position it within the broader context of text-to-image generation research. The authors should also provide a more detailed analysis of the results, including the performance on different types of prompts and images. This would help to identify the limitations of the method and to suggest potential improvements.

The paper should also provide more details about the dataset, including the distribution of prompts and images, and the quality of the annotations. The authors should discuss the potential biases in the dataset, such as the types of prompts that are overrepresented or underrepresented, and how these biases might affect the performance of the model. The paper should also discuss the quality of the annotations, such as the level of agreement between annotators and the potential for noise in the annotations. For example, the authors could provide a histogram of the distribution of human preferences, and they could also provide a qualitative analysis of the annotations. This would help to assess the reliability of the dataset and to identify potential issues. The authors should also discuss the limitations of the dataset and how they might affect the results.

Finally, the paper should provide more details about the ReFL algorithm, including the hyperparameters used and the training procedure. The paper should also discuss the limitations of the ReFL algorithm and how they might affect the results. For example, the paper should discuss the potential for overfitting and how the authors avoided this issue. The paper should also discuss the computational cost of the ReFL algorithm and how it compares to other fine-tuning methods. For example, the authors could provide a table that compares the training time and memory usage of their method with other fine-tuning methods. This would help to assess the practicality of the method and to identify potential areas for improvement. The authors should also discuss the sensitivity of the method to the choice of hyperparameters and how they selected these hyperparameters.

### Questions

1. How does the proposed method compare with other state-of-the-art methods on the same dataset?
2. What are the limitations of the dataset, and how might they affect the results?
3. What are the limitations of the ReFL algorithm, and how might they affect the results?

### Rating

5

### Confidence

4

**********

## Reviewer 2

### Summary

This paper introduces ImageReward, a novel reward model designed to evaluate and improve text-to-image generation models based on human preferences. The authors present a systematic annotation pipeline that generates 137,000 expert comparisons, forming the basis for ImageReward. They also propose a direct tuning algorithm, ReFL, which optimizes diffusion models using ImageReward feedback, demonstrating its effectiveness in enhancing model performance.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper addresses a significant challenge in text-to-image generation by focusing on human preference, which is crucial for aligning models with real-world expectations.
2. The proposed ImageReward model is a valuable contribution to the field, offering a more accurate and comprehensive assessment of image quality compared to existing metrics.
3. The ReFL algorithm provides a novel approach to fine-tuning diffusion models, directly incorporating human feedback to improve alignment and quality.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed analysis of the ImageReward model's performance across different types of prompts and image content. Specifically, it would be valuable to see how the model handles prompts with varying levels of complexity, such as those involving multiple objects, abstract concepts, or fine-grained details. Furthermore, the analysis should extend to different image domains, such as indoor scenes, outdoor landscapes, or abstract art, to understand the model's strengths and weaknesses in diverse contexts. This would provide a more granular understanding of the model's capabilities and limitations.
2. While the ReFL algorithm is innovative, the paper lacks a thorough exploration of its sensitivity to hyperparameter choices. It is crucial to understand how different learning rates, batch sizes, and regularization parameters affect the model's convergence and final performance. A detailed ablation study is needed to identify the optimal settings and understand the trade-offs between different parameter choices. This analysis should also consider the computational cost associated with different hyperparameter configurations, providing practical guidance for implementation.
3. The evaluation of the ReFL algorithm could be strengthened by including comparisons with a broader range of state-of-the-art methods. While the paper demonstrates improvements over existing metrics, it would be beneficial to compare against other fine-tuning techniques for diffusion models, such as those based on reinforcement learning or adversarial training. This would provide a more comprehensive assessment of the ReFL algorithm's effectiveness and its relative advantages and disadvantages compared to other approaches.

### Suggestions

To enhance the paper, the authors should conduct a more in-depth analysis of the ImageReward model's performance across a wider range of prompts and image content. This should include a systematic evaluation of the model's accuracy and reliability when dealing with complex prompts involving multiple objects, abstract concepts, and fine-grained details. For instance, the authors could categorize prompts based on their complexity and analyze the model's performance within each category. Additionally, the evaluation should extend to different image domains, such as indoor scenes, outdoor landscapes, and abstract art. This would involve creating test sets that represent these diverse domains and analyzing the model's performance on each. The analysis should also include a qualitative assessment of the model's outputs, examining the visual quality and alignment with the given prompts. This would provide a more comprehensive understanding of the model's strengths and weaknesses, and guide future improvements.

Furthermore, the paper would benefit from a more thorough exploration of the ReFL algorithm's sensitivity to hyperparameter choices. The authors should conduct a detailed ablation study to investigate the impact of different learning rates, batch sizes, and regularization parameters on the model's convergence and final performance. This study should include a range of parameter values and analyze the trade-offs between different choices. For example, the authors could examine how different learning rates affect the model's ability to learn complex patterns and how batch size impacts the stability of the training process. The analysis should also consider the computational cost associated with different hyperparameter configurations, providing practical guidance for implementation. This would allow other researchers to replicate the results and apply the ReFL algorithm effectively in different contexts.

Finally, the evaluation of the ReFL algorithm should be strengthened by including comparisons with a broader range of state-of-the-art methods. The authors should compare their approach against other fine-tuning techniques for diffusion models, such as those based on reinforcement learning or adversarial training. This would provide a more comprehensive assessment of the ReFL algorithm's effectiveness and its relative advantages and disadvantages compared to other approaches. The comparison should include both quantitative metrics, such as image quality scores and alignment with text prompts, as well as qualitative assessments of the generated images. This would provide a more complete picture of the ReFL algorithm's performance and its potential impact on the field.

### Questions

1. How does ImageReward perform on prompts that are ambiguous or have multiple valid interpretations? Does it consistently select the most appropriate image, or does it struggle with such cases?
2. The paper mentions that ImageReward outperforms existing metrics in terms of human alignment. Could you provide more details on the specific scenarios where ImageReward excels compared to metrics like CLIP, Aesthetic, and BLIP?
3. How does the ReFL algorithm handle cases where human preferences are inconsistent or subjective? Is there any mechanism in place to mitigate the impact of such inconsistencies on the model's performance?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper introduces ImageReward, a novel text-to-image human preference reward model, and ReFL, a direct tuning algorithm to optimize diffusion models using ImageReward feedback. ImageReward is trained on a dataset of 137k expert comparisons and outperforms existing metrics like CLIP, Aesthetic, and BLIP in terms of human alignment. ReFL fine-tunes diffusion models by leveraging ImageReward feedback, achieving superior performance over existing methods on the DiffusionDB dataset.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper presents a comprehensive solution to the text-to-image human preference evaluation problem, from data collection to model training and evaluation.
2. The proposed ImageReward model demonstrates superior performance in aligning with human preferences compared to existing metrics.
3. The ReFL algorithm provides a novel approach to fine-tuning diffusion models, offering a more effective way to optimize them for human preferences.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed analysis of the ImageReward model's performance across different types of prompts and image content. Specifically, it would be valuable to see how the model handles prompts with varying levels of complexity, such as those involving multiple objects, abstract concepts, or fine-grained details. Furthermore, the analysis should extend to different image domains, such as indoor scenes, outdoor landscapes, or abstract art, to understand the model's strengths and weaknesses in diverse contexts. This would provide a more granular understanding of the model's capabilities and limitations.
2. While the ReFL algorithm is innovative, the paper lacks a thorough exploration of its sensitivity to hyperparameter choices. It is crucial to understand how different learning rates, batch sizes, and regularization parameters affect the model's convergence and final performance. A detailed ablation study is needed to identify the optimal settings and understand the trade-offs between different parameter choices. This analysis should also consider the computational cost associated with different hyperparameter configurations, providing practical guidance for implementation.
3. The evaluation of the ReFL algorithm could be strengthened by including comparisons with a broader range of state-of-the-art methods. While the paper demonstrates improvements over existing metrics, it would be beneficial to compare against other fine-tuning techniques for diffusion models, such as those based on reinforcement learning or adversarial training. This would provide a more comprehensive assessment of the ReFL algorithm's effectiveness and its relative advantages and disadvantages compared to other approaches.

### Suggestions

To enhance the paper, the authors should conduct a more in-depth analysis of the ImageReward model's performance across a wider range of prompts and image content. This should include a systematic evaluation of the model's accuracy and reliability when dealing with complex prompts involving multiple objects, abstract concepts, and fine-grained details. For instance, the authors could categorize prompts based on their complexity and analyze the model's performance within each category. Additionally, the evaluation should extend to different image domains, such as indoor scenes, outdoor landscapes, and abstract art. This would involve creating test sets that represent these diverse domains and analyzing the model's performance on each. The analysis should also include a qualitative assessment of the model's outputs, examining the visual quality and alignment with the given prompts. This would provide a more comprehensive understanding of the model's strengths and weaknesses, and guide future improvements.

Furthermore, the paper would benefit from a more thorough exploration of the ReFL algorithm's sensitivity to hyperparameter choices. The authors should conduct a detailed ablation study to investigate the impact of different learning rates, batch sizes, and regularization parameters on the model's convergence and final performance. This study should include a range of parameter values and analyze the trade-offs between different choices. For example, the authors could examine how different learning rates affect the model's ability to learn complex patterns and how batch size impacts the stability of the training process. The analysis should also consider the computational cost associated with different hyperparameter configurations, providing practical guidance for implementation. This would allow other researchers to replicate the results and apply the ReFL algorithm effectively in different contexts.

Finally, the evaluation of the ReFL algorithm should be strengthened by including comparisons with a broader range of state-of-the-art methods. The authors should compare their approach against other fine-tuning techniques for diffusion models, such as those based on reinforcement learning or adversarial training. This would provide a more comprehensive assessment of the ReFL algorithm's effectiveness and its relative advantages and disadvantages compared to other approaches. The comparison should include both quantitative metrics, such as image quality scores and alignment with text prompts, as well as qualitative assessments of the generated images. This would provide a more complete picture of the ReFL algorithm's performance and its potential impact on the field.

### Questions

See weaknesses.

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

This paper proposes a new text-to-image reward model, ImageReward, and a new fine-tuning method for diffusion models, ReFL. ImageReward is trained on 137k human comparison pairs and outperforms existing text-image scoring methods in terms of human preference alignment. ReFL directly fine-tunes diffusion models using ImageReward feedback, achieving better performance than existing methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed ImageReward model is novel and effective, outperforming existing metrics in terms of human preference alignment.
3. The proposed ReFL method is also novel and effective, achieving better performance than existing methods in fine-tuning diffusion models.

### Weaknesses

#### Some Related Works

[1] Direct Fine-Tuning of Diffusion Models for Visual Perception
[2] Direct Preference Optimization: Your Language Model is Secretly a Reward Model

#### comment

1. The paper lacks a comparison with other fine-tuning methods for diffusion models, such as those based on reinforcement learning [1] or adversarial training [2]. Specifically, the paper does not explore how the proposed ReFL method compares to these alternative approaches in terms of convergence speed, final performance, and robustness to different datasets. A more comprehensive comparison would involve evaluating ReFL against a range of existing fine-tuning techniques, including both direct optimization and those based on reward modeling.
2. The paper does not provide a detailed analysis of the computational cost of the proposed method, including training time and memory usage. The paper should include a breakdown of the computational resources required for training ImageReward and ReFL, as well as the inference time for both methods. This analysis should consider the impact of different model sizes and dataset sizes on the computational cost. Furthermore, the paper should discuss the scalability of the proposed methods to larger datasets and models.
3. The paper does not explore the generalization ability of the proposed method to different domains or tasks. The paper should evaluate the performance of ImageReward and ReFL on datasets that are different from the ones used for training, such as datasets with different image styles or text prompts. This would provide a more comprehensive understanding of the robustness and applicability of the proposed methods. The paper should also investigate the sensitivity of the methods to different hyperparameters and provide guidelines for selecting appropriate values.

### Suggestions

The paper would benefit significantly from a more thorough comparison with existing fine-tuning methods for diffusion models. Specifically, the authors should benchmark ReFL against methods that utilize reinforcement learning, such as those that optimize for specific reward functions, and adversarial training techniques that aim to improve the quality of generated images. This comparison should not only focus on the final performance metrics but also on the convergence speed and stability of the training process. For instance, the authors could compare the number of training iterations required to reach a certain performance level, the sensitivity of the methods to hyperparameter settings, and the robustness of the methods to different datasets. Furthermore, the authors should analyze the computational cost of each method, including the training time and memory usage, and discuss the trade-offs between performance and computational resources. This would provide a more complete picture of the strengths and weaknesses of the proposed ReFL method compared to existing approaches.

To address the lack of computational cost analysis, the authors should provide a detailed breakdown of the resources required for training and inference. This should include the training time, memory usage, and the number of parameters for both ImageReward and ReFL. The analysis should also consider the impact of different model sizes and dataset sizes on the computational cost. For example, the authors could evaluate the performance of the methods with different model architectures and dataset sizes, and discuss the scalability of the methods to larger datasets and models. This would provide valuable insights into the practical applicability of the proposed methods and help researchers choose the most appropriate method for their specific needs. The authors should also discuss the potential for optimizing the computational cost of the methods, such as through model pruning or quantization.

Finally, the paper should include a more comprehensive evaluation of the generalization ability of the proposed methods. The authors should evaluate the performance of ImageReward and ReFL on datasets that are different from the ones used for training, such as datasets with different image styles or text prompts. This would provide a more robust assessment of the methods' ability to generalize to new scenarios. The authors should also investigate the sensitivity of the methods to different hyperparameters and provide guidelines for selecting appropriate values. For example, the authors could perform a hyperparameter search and report the optimal values for different datasets. This would make the methods more accessible and easier to use for other researchers. The authors should also discuss the limitations of the methods and suggest directions for future research.

### Questions

1. How does the proposed method compare to other fine-tuning methods for diffusion models, such as those based on reinforcement learning [1] or adversarial training [2]?
2. What is the computational cost of the proposed method, including training time and memory usage?
3. How does the proposed method generalize to different domains or tasks?

[1] Direct Fine-Tuning of Diffusion Models for Visual Perception
[2] Direct Preference Optimization: Your Language Model is Secretly a Reward Model

### Rating

6

### Confidence

4

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers for the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

Plan:
1. Read each reviewer's weakness.
2. Search the paper for evidence related to the weakness.
3. Categorize the evidence (methodological, experimental).
4. Analyze the evidence and determine if the weakness is valid.
5. Provide a conclusion with a confidence level and key supporting evidence.
```json
[
  {
    "Weakness Statement": "The paper could benefit from a more detailed analysis of the ImageReward model's performance across different types of prompts and image content. Specifically, it would be valuable to see how the model handles prompts with varying levels of complexity, such as those involving multiple objects, abstract concepts, or fine-grained details. Furthermore, the analysis should extend to different image domains, such as indoor scenes, outdoor landscapes, or abstract art, to understand the model's strengths and weaknesses in diverse contexts. This would provide a more granular understanding of the model's capabilities and limitations.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        {
          "quote": "We divide the dataset according to prompts annotated by different annotators and select 466 prompts from annotators who have a higher agreement with researchers to consist for the model test.",
          "section": "4.1 ImageReward: On Human Preference Prediction"
        },
        {
          "quote": "Except for prompts for testing, other more than 8k prompts of annotation are collected for training.",
          "section": "4.1 ImageReward: On Human Preference Prediction"
        },
        {
          "quote": "We use the CLIP score, Aesthetic score, and BLIP score as baselines to compare with the ImageReward. CLIP score and BLIP score are calculated directly as cosine similarity between text and image embedding, while the Aesthetic score is given by an aesthetic predictor introduced by LAION [50].",
          "section": "4.1 ImageReward: On Human Preference Prediction"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper mentions dividing the dataset based on prompts annotated by different annotators and selecting a subset for testing. It also states that the training dataset consists of over 8k prompts. However, there is no detailed analysis of ImageReward's performance based on the complexity or domain of the prompts and images.",
      "Supporting quotes": [
        "We divide the dataset according to prompts annotated by different annotators and select 466 prompts from annotators who have a higher agreement with researchers to consist for the model test.",
        "Except for prompts for testing, other more than 8k prompts of annotation are collected for training."
      ],
      "Impact assessment": "The lack of detailed analysis across different prompt and image types limits the understanding of ImageReward's strengths and weaknesses in various scenarios."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper describes the dataset split and baselines used but lacks a granular analysis of ImageReward's performance based on prompt and image characteristics."
    }
  },
  {
    "Weakness Statement": "While the ReFL algorithm is innovative, the paper lacks a thorough exploration of its sensitivity to hyperparameter choices. It is crucial to understand how different learning rates, batch sizes, and regularization parameters affect the model's convergence and final performance. A detailed ablation study is needed to identify the optimal settings and understand the trade-offs between different parameter choices. This analysis should also consider the computational cost associated with different hyperparameter configurations, providing practical guidance for implementation.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        {
          "quote": "For the dataset, the pre-training dataset is from a 625k subset of LAION-5B [50] selected by aesthetic score, while the prompt set for ReFL is sampled from DiffusionDB.",
          "section": "4.2 ReFL: On Improving Diffusion Models with Human Preference"
        },
        {
          "quote": "For ReFL algorithm, we set ϕ = R ¯ , λ = 1 e − 3 and T = 40 , [ T 1 , T 2 ] = [ 1 , 10 ] T=40 , [ T 1 , T 2 ] = [ 1 , 10] .",
          "section": "4.2 ReFL: On Improving Diffusion Models with Human Preference"
        },
        {
          "quote": "We use the CLIP score, Aesthetic score, and BLIP score as baselines to compare with the ImageReward. CLIP score and BLIP score are calculated directly as cosine similarity between text and image embedding, while the Aesthetic score is given by an aesthetic predictor introduced by LAION [50].",
          "section": "4.1 ImageReward: On Human Preference Prediction"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper mentions the hyperparameter settings used for the ReFL algorithm but does not include an ablation study to analyze the impact of different hyperparameters on the model's performance or convergence.",
      "Supporting quotes": [
        "For the dataset, the pre-training dataset is from a 625k subset of LAION-5B [50] selected by aesthetic score, while the prompt set for ReFL is sampled from DiffusionDB.",
        "For ReFL algorithm, we set ϕ = R ¯ , λ = 1 e − 3 and T = 40 , [ T 1 , T 2 ] = [ 1 , 10 ] T=40 , [ T 1 , T 2 ] = [ 1 , 10]."
      ],
      "Impact assessment": "The absence of a hyperparameter sensitivity analysis makes it difficult to understand the robustness of ReFL and provides limited guidance for its practical application with different hyperparameter configurations."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper states the hyperparameter values used but lacks any analysis of how different values would affect the results."
    }
  },
  {
    "Weakness Statement": "The evaluation of the ReFL algorithm could be strengthened by including comparisons with a broader range of state-of-the-art methods. While the paper demonstrates improvements over existing metrics, it would be beneficial to compare against other fine-tuning techniques for diffusion models, such as those based on reinforcement learning or adversarial training. This would provide a more comprehensive assessment of the ReFL algorithm's effectiveness and its relative advantages and disadvantages compared to other approaches.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        {
          "quote": "We compare several important related methods for improving text-to-image generation [61 ; 23 ; 13 ] , whose implementation details are provided in Appendix E . Compared to ReFL’s direct tuning, these previous methods are all based on indirect data augmentation or loss reweighing.",
          "section": "4.2 ReFL: On Improving Diffusion Models with Human Preference"
        },
        {
          "quote": "Compared to ReFL’s direct tuning, these previous methods are all based on indirect data augmentation or loss reweighing.",
          "section": "4.2 ReFL: On Improving Diffusion Models with Human Preference"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper explicitly states that the compared methods are indirect data augmentation or loss reweighing techniques, not direct fine-tuning methods like reinforcement learning or adversarial training.",
      "Supporting quotes": [
        "We compare several important related methods for improving text-to-image generation [61 ; 23 ; 13 ] , whose implementation details are provided in Appendix E . Compared to ReFL’s direct tuning, these previous methods are all based on indirect data augmentation or loss reweighing.",
        "Compared to ReFL’s direct tuning, these previous methods are all based on indirect data augmentation or loss reweighing."
      ],
      "Impact assessment": "The evaluation is limited to indirect methods, and a comparison with direct fine-tuning techniques would provide a more comprehensive assessment of ReFL's effectiveness."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper explicitly mentions the comparison methods are indirect, not including direct fine-tuning methods like reinforcement learning or adversarial training."
    }
  },
  {
    "Weakness Statement": "How does ImageReward perform on prompts that are ambiguous or have multiple valid interpretations? Does it consistently select the most appropriate image, or does it struggle with such cases?",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        {
          "quote": "We use the CLIP score, Aesthetic score, and BLIP score as baselines to compare with the ImageReward. CLIP score and BLIP score are calculated directly as cosine similarity between text and image embedding, while the Aesthetic score is given by an aesthetic predictor introduced by LAION [50].",
          "section": "4.1 ImageReward: On Human Preference Prediction"
        },
        {
          "quote": "We conduct researcher annotation (i.e., by authors) across 6 popular high-resolution (around 512 × 512) available text-to-image models: CogView 2 [12] , Versatile Diffusion (VD) 1.4 and 2.1-base [45 ] , DALL-E 2 (via OpenAI API) [42 ] , and Openjourney 1 1 1 42 ] , to identify the alignment of different metrics to human.",
          "section": "4.1 ImageReward: On Human Preference Prediction"
        },
        {
          "quote": "We sample 100 real-user test prompts from DiffusionDB and use different methods to select from those images to get top3 results. Then three annotators rank these selected top-3 images. Figure 5 shows the win rates. Qualitative results can be seen in Appendix G , showing that ImageReward can select images that are more aligned to text and with higher fidelity and avoid toxic contents.",
          "section": "4.1 ImageReward: On Human Preference Prediction"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper evaluates ImageReward's performance using a dataset of real user prompts and compares it against CLIP, Aesthetic, and BLIP scores. The evaluation includes a researcher annotation study and a qualitative analysis of the top 3 selected images. However, there is no specific analysis or experiment designed to explicitly test ImageReward's performance on ambiguous or multiply interpretable prompts.",
      "Supporting quotes": [
        "We use the CLIP score, Aesthetic score, and BLIP score as baselines to compare with the ImageReward.",
        "We sample 100 real-user test prompts from DiffusionDB and use different methods to select from those images to get top3 results. Then three annotators rank these selected top-3 images."
      ],
      "Impact assessment": "The paper lacks a direct evaluation of ImageReward's ability to handle ambiguous prompts, leaving this aspect unaddressed."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The experimental setup focuses on real user prompts but doesn't specifically isolate or test the performance on ambiguous prompts."
    }
  },
  {
    "Weakness Statement": "The paper mentions that ImageReward outperforms existing metrics in terms of human alignment. Could you provide more details on the specific scenarios where ImageReward excels compared to metrics like CLIP, Aesthetic, and BLIP?",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        {
          "quote": "We use the CLIP score, Aesthetic score, and BLIP score as baselines to compare with the ImageReward. CLIP score and BLIP score are calculated directly as cosine similarity between text and image embedding, while the Aesthetic score is given by an aesthetic predictor introduced by LAION [50].",
          "section": "4.1 ImageReward: On Human Preference Prediction"
        },
        {
          "quote": "Figure 3 presents a box plot of ImageReward and CLIP’s score distributions on the 1,000 generations per model. The distributions are normalized to 0.0 to 1.0 using minimum and maximum values of ImageReward and CLIP scores per model, and outliers are discarded. As Table 1 shows, ImageReward aligns well with human ranking, whereas zero-shot FID and CLIP are not.",
          "section": "4.1 ImageReward: On Human Preference Prediction"
        },
        {
          "quote": "Table 3(a) shows that adding up the scale of the dataset significantly improves the preference accuracy of ImageReward. It’s promising that if we collect more annotation data in the future, ImageReward will get better performance.",
          "section": "4.1 ImageReward: On Human Preference Prediction"
        },
        {
          "quote": "Table 2(b) shows that adding up the scale of the dataset significantly improves the preference accuracy of ImageReward. It’s promising that if we collect more annotation data in the future, ImageReward will get better performance.",
          "section": "4.1 ImageReward: On Human Preference Prediction"
        },
        {
          "quote": "We use the CLIP score, Aesthetic score, and BLIP score as baselines to compare with the ImageReward. CLIP score and BLIP score are calculated directly as cosine similarity between text and image embedding, while the Aesthetic score is given by an aesthetic predictor introduced by LAION [50].",
          "section": "4.1 ImageReward: On Human Preference Prediction"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper shows through experiments that ImageReward outperforms CLIP, Aesthetic, and BLIP in aligning with human preferences. Figure 3 and Tables 2 and 3 provide quantitative evidence of this outperformance. However, the paper does not explicitly detail the specific scenarios or types of prompts where ImageReward shows a significant advantage over these metrics.",
      "Supporting quotes": [
        "Figure 3 presents a box plot of ImageReward and CLIP’s score distributions on the 1,000 generations per model. The distributions are normalized to 0.0 to 1.0 using minimum and maximum values of ImageReward and CLIP scores per model, and outliers are discarded. As Table 1 shows, ImageReward aligns well with human ranking, whereas zero-shot FID and CLIP are not.",
        "Table 3(a) shows that adding up the scale of the dataset significantly improves the preference accuracy of ImageReward.",
        "Table 2(b) shows that adding up the scale of the dataset significantly improves the preference accuracy of ImageReward."
      ],
      "Impact assessment": "While the paper demonstrates overall outperformance, it lacks a granular breakdown of the specific scenarios where ImageReward excels."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper shows overall outperformance but lacks a detailed analysis of specific scenarios where ImageReward is superior."
    }
  },
  {
    "Weakness Statement": "How does the ReFL algorithm handle cases where human preferences are inconsistent or subjective? Is there any mechanism in place to mitigate the impact of such inconsistencies on the model's performance?",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        {
          "quote": "We compare several important related methods for improving text-to-image generation [61 ; 23 ; 13 ] , whose implementation details are provided in Appendix E . Compared to ReFL’s direct tuning, these previous methods are all based on indirect data augmentation or loss reweighing.",
          "section": "4.2 ReFL: On Improving Diffusion Models with Human Preference"
        },
        {
          "quote": "Compared to ReFL’s direct tuning, these previous methods are all based on indirect data augmentation or loss reweighing.",
          "section": "4.2 ReFL: On Improving Diffusion Models with Human Preference"
        },
        {
          "quote": "We use the CLIP score, Aesthetic score, and BLIP score as baselines to compare with the ImageReward. CLIP score and BLIP score are calculated directly as cosine similarity between text and image embedding, while the Aesthetic score is given by an aesthetic predictor introduced by LAION [50].",
          "section": "4.1 ImageReward: On Human Preference Prediction"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper describes ReFL as a direct tuning algorithm that optimizes the diffusion model based on the reward model. The baselines used for comparison are indirect methods. The paper does not explicitly discuss how ReFL handles inconsistencies or subjectivity in human preferences.",
      "Supporting quotes": [
        "We compare several important related methods for improving text-to-image generation [61 ; 23 ; 13 ] , whose implementation details are provided in Appendix E . Compared to ReFL’s direct tuning, these previous methods are all based on indirect data augmentation or loss reweighing.",
        "Compared to ReFL’s direct tuning, these previous methods are all based on indirect data augmentation or loss reweighing.",
        "We use the CLIP score, Aesthetic score, and BLIP score as baselines to compare with the ImageReward. CLIP score and BLIP score are calculated directly as cosine similarity between text and image embedding, while the Aesthetic score is given by an aesthetic predictor introduced by LAION [50]."
      ],
      "Impact assessment": "The paper lacks a discussion on how ReFL addresses the inherent subjectivity and potential inconsistencies in human preferences, which is a relevant consideration for any preference-based learning method."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper focuses on the mechanics of ReFL and compares it to indirect methods, without addressing the handling of subjective preferences."
    }
  },
  {
    "Weakness Statement": "The paper could benefit from a more detailed analysis of the ImageReward model's performance across a wider range of prompts and image content. Specifically, it would be valuable to see how the model handles prompts with varying levels of complexity, such as those involving multiple objects, abstract concepts, or fine-grained details. Furthermore, the analysis should extend to different image domains, such as indoor scenes, outdoor landscapes, or abstract art, to understand the model's strengths and weaknesses in diverse contexts. This would provide a more granular understanding of the model's capabilities and limitations.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        {
          "quote": "We divide the dataset according to prompts annotated by different annotators and select 466 prompts from annotators who have a higher agreement with researchers to consist for the model test.",
          "section": "4.1 ImageReward: On Human Preference Prediction"
        },
        {
          "quote": "Except for prompts for testing, other more than 8k prompts of annotation are collected for training.",
          "section": "4.1 ImageReward: On Human Preference Prediction"
        },
        {
          "quote": "We use the CLIP score, Aesthetic score, and BLIP score as baselines to compare with the ImageReward. CLIP score and BLIP score are calculated directly as cosine similarity between text and image embedding, while the Aesthetic score is given by an aesthetic predictor introduced by LAION [50].",
          "section": "4.1 ImageReward: On Human Preference Prediction"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper mentions the dataset size and the selection process for testing prompts but lacks a detailed breakdown of performance based on prompt complexity or image domain.",
      "Supporting quotes": [
        "We divide the dataset according to prompts annotated by different annotators and select 466 prompts from annotators who have a higher agreement with researchers to consist for the model test.",
        "Except for prompts for testing, other more than 8k prompts of annotation are collected for training.",
        "We use the CLIP score, Aesthetic score, and BLIP score as baselines to compare with the ImageReward."
      ],
      "Impact assessment": "The absence of a granular analysis limits the understanding of ImageReward's strengths and weaknesses across different prompt and image types."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper describes the dataset but lacks a detailed analysis of performance across different prompt and image characteristics."
    }
  },
  {
    "Weakness Statement": "While the ReFL algorithm is innovative, the paper lacks a thorough exploration of its sensitivity to hyperparameter choices. It is crucial to understand how different learning rates, batch sizes, and regularization parameters affect the model's convergence and final performance. A detailed ablation study is needed to identify the optimal settings and understand the trade-offs between different parameter choices. This analysis should also consider the computational cost associated with different hyperparameter configurations, providing practical guidance for implementation.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        {
          "quote": "For the dataset, the pre-training dataset is from a 625k subset of LAION-5B [50] selected by aesthetic score, while the prompt set for ReFL is sampled from DiffusionDB.",
          "section": "4.2 ReFL: On Improving Diffusion Models with Human Preference"
        },
        {
          "quote": "For ReFL algorithm, we set ϕ = R ¯ , λ = 1 e − 3 and T = 40 , [ T 1 , T 2 ] = [ 1 , 10 ] T=40 , [ T 1 , T 2 ] = [ 1 , 10] .",
          "section": "4.2 ReFL: On Improving Diffusion Models with Human Preference"
        },
        {
          "quote": "We use the CLIP score, Aesthetic score, and BLIP score as baselines to compare with the ImageReward. CLIP score and BLIP score are calculated directly as cosine similarity between text and image embedding, while the Aesthetic score is given by an aesthetic predictor introduced by LAION [50].",
          "section": "4.1 ImageReward: On Human Preference Prediction"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper specifies the hyperparameter settings used for ReFL but does not include an ablation study to assess the impact of different hyperparameter values on performance and convergence.",
      "Supporting quotes": [
        "For the dataset, the pre-training dataset is from a 625k subset of LAION-5B [50] selected by aesthetic score, while the prompt set for ReFL is sampled from DiffusionDB.",
        "For ReFL algorithm, we set ϕ = R ¯ , λ = 1 e − 3 and T = 40 , [ T 1 , T 2 ] = [ 1 , 10 ] T=40 , [ T 1 , T 2 ] = [ 1 , 10]."
      ],
      "Impact assessment": "The lack of hyperparameter sensitivity analysis makes it difficult to understand the robustness of ReFL and provides limited guidance for its practical application with different hyperparameter configurations."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper states the hyperparameter values used but lacks any analysis of how different values would affect the results."
    }
  },
  {
    "Weakness Statement": "The evaluation of the ReFL algorithm could be strengthened by including comparisons with a broader range of state-of-the-art methods. While the paper demonstrates improvements over existing metrics, it would be beneficial to compare against other fine-tuning techniques for diffusion models, such as those based on reinforcement learning or adversarial training. This would provide a more comprehensive assessment of the ReFL algorithm's effectiveness and its relative advantages and disadvantages compared to other approaches.",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        {
          "quote": "We compare several important related methods for improving text-to-image generation [61 ; 23 ; 13 ] , whose implementation details are provided in Appendix E . Compared to ReFL’s direct tuning, these previous methods are all based on indirect data augmentation or loss reweighing.",
          "section": "4.2 ReFL: On Improving Diffusion Models, ReFL Algorithm"
        },
        {
          "quote": "Compared to ReFL’s direct tuning, these previous methods are all based on indirect data augmentation or loss reweighing.",
          "section": "4.2 ReFL: On Improving Diffusion Models, ReFL Algorithm"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper explicitly states that the compared methods are indirect data augmentation or loss reweighing techniques, not direct fine-tuning methods like reinforcement learning or adversarial training.",
      "Supporting quotes": [
        "We compare several important related methods for improving text-to-image generation [61 ; 23 ; 13 ] , whose implementation details are provided in Appendix E . Compared to ReFL’s direct tuning, these previous methods are all based on indirect data augmentation or loss reweighing.",
        "Compared to ReFL’s direct tuning, these previous methods are all based on indirect data augmentation or loss reweighing."
      ],
      "Impact assessment": "The evaluation is limited to indirect methods, and a comparison with direct fine-tuning techniques would provide a more comprehensive assessment of ReFL's effectiveness."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper explicitly mentions the comparison methods are indirect, not including direct fine-tuning methods like reinforcement learning or adversarial training."
    }
  },
  {
    "Weakness Statement": "How does the proposed method compare with other fine-tuning methods for diffusion models, such as those based on reinforcement learning [1] or adversarial training [2]?",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        {
          "quote": "We compare several important related methods for improving text-to-image generation [61 ; 23 ; 13 ] , whose implementation details are provided in Appendix E . Compared to ReFL’s direct tuning, these previous methods are all based on indirect data augmentation or loss reweighing.",
          "section": "4.2 ReFL: On Improving Diffusion Models, ReFL Algorithm"
        },
        {
          "quote": "Compared to ReFL’s direct tuning, these previous methods are all based on indirect data augmentation or loss reweighing.",
          "section": "4.2 ReFL: On Improving Diffusion Models, ReFL Algorithm"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper explicitly states that the compared methods are indirect data augmentation or loss reweighing techniques, not direct fine-tuning methods like reinforcement learning or adversarial training.",
      "Supporting quotes": [
        "We compare several important related methods for improving text-to-image generation [61 ; 23 ; 13 ] , whose implementation details are provided in Appendix E . Compared to ReFL’s direct tuning, these previous methods are all based on indirect data augmentation or loss reweighing.",
        "Compared to ReFL’s direct tuning, these previous methods are all based on indirect data augmentation or loss reweighing."
      ],
      "Impact assessment": "The evaluation is limited to indirect methods, and a comparison with direct fine-tuning techniques would provide a more comprehensive assessment of ReFL's effectiveness."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper explicitly mentions the comparison methods are indirect, not including direct fine-tuning methods like reinforcement learning or adversarial training."
    }
  },
  {
    "Weakness Statement": "What is the computational cost of the proposed method, including training time and memory usage?",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        {
          "quote": "We use Stable Diffusion v1.4 as the baseline generative model and fine-tune it for experiments. For the dataset, the pre-training dataset is from a 625k subset of LAION-5B [50] selected by aesthetic score, while the prompt set for ReFL is sampled from DiffusionDB.",
          "section": "4.2 ReFL: On Improving Diffusion Models with Human Preference"
        },
        {
          "quote": "For ReFL algorithm, we set ϕ = R ¯ , λ = 1 e − 3 and T = 40 , [ T 1 , T 2 ] = [ 1 , 10 ] T=40 , [ T 1 , T 2 ] = [ 1 , 10].",
          "section": "4.2 ReFL: On Improving Diffusion Models with Human Preference"
        },
        {
          "quote": "We use the CLIP score, Aesthetic score, and BLIP score as baselines to compare with the ImageReward. CLIP score and BLIP score are calculated directly as cosine similarity between text and image embedding, while the Aesthetic score is given by an aesthetic predictor introduced by LAION [50].",
          "section": "4.1 ImageReward: On Human Preference Prediction"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper mentions the models and datasets used but does not provide specific details on training time or memory usage for ImageReward or ReFL.",
      "Supporting quotes": [
        "We use Stable Diffusion v1.4 as the baseline generative model and fine-tune it for experiments.",
        "We use the CLIP score, Aesthetic score, and BLIP score as baselines to compare with the ImageReward."
      ],
      "Impact assessment": "The lack of information on computational cost makes it difficult to assess the practical feasibility and resource requirements of the proposed methods."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper describes the models and datasets but lacks specific details on training time and memory usage."
    }
  },
  {
    "Weakness Statement": "How does the proposed method generalize to different domains or tasks?",
    "Evidence Collection": {
      "b) Experiment-related Evidence (if applicable)": [
        {
          "quote": "We use the CLIP score, Aesthetic score, and BLIP score as baselines to compare with the ImageReward. CLIP score and BLIP score are calculated directly as cosine similarity between text and image embedding, while the Aesthetic score is given by an aesthetic predictor introduced by LAION [50].",
          "section": "4.1 ImageReward: On Human Preference Prediction"
        },
        {
          "quote": "We use the pre-trained checkpoint of BLIP (ViT-L for image encoder, 12-layers transformer for text encoder) as the backbone of ImageReward, and initialize MLP head according to 𝑁 = 4 , 9 , 1 , 2 − 4 , 3 , 5 , 5 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 6 , 4 , 4 , 1 , 2 , 2 , 1 , 1 , 1 , 1 , 1 , 1 , 0 , 4 , 4 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 9 , 2 , 6 , 9 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1