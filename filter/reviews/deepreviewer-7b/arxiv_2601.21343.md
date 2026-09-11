I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper proposes a new pre-training approach that incorporates safety, factuality, and quality judgments into the pre-training process. Specifically, it uses a post-trained model to rewrite pre-training data and provide judgment signals for reinforcement learning. The results show improvements in generation quality, safety, and factuality.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is a combination of existing techniques, including LLM-as-judge and RL-based pre-training. The paper does not clearly articulate the novelty of the proposed approach beyond combining these techniques. The specific way in which the post-trained model is used for rewriting and judging, and how this differs from existing methods, needs further clarification.
2. The experiments are limited to a single model (Llama2 1.4B) and dataset (RedPajama). It is unclear whether the proposed method would generalize to other model architectures and pre-training datasets. The paper should include experiments on a wider range of models and datasets to demonstrate the robustness of the approach.
3. The paper lacks a detailed analysis of the computational cost associated with the proposed method. The use of a post-trained model for rewriting and judging adds computational overhead, which should be quantified and compared to standard pre-training methods.

### Suggestions

The paper should provide a more detailed explanation of how the proposed method differs from existing techniques, particularly in the context of using a post-trained model for rewriting and judging. A clear articulation of the novelty is crucial. For example, the authors could discuss the specific prompts used for the post-trained model to generate rewrites and judgments, and how these prompts are designed to capture the desired properties (safety, factuality, and quality). Furthermore, a comparison with other methods that use LLMs for similar tasks would help to highlight the unique contributions of this work. The authors should also clarify the specific RL algorithm used and provide details on the reward function, as these choices can significantly impact the performance of the method.

To address the limited experimental scope, the authors should include experiments on a wider range of models and datasets. This would help to demonstrate the generalizability of the proposed method. For example, experiments on models with different architectures (e.g., encoder-decoder models) and datasets with different characteristics (e.g., synthetic data) would be valuable. The paper should also include a detailed analysis of the performance of the proposed method on different types of prompts and inputs. This would help to identify the strengths and weaknesses of the approach and provide insights into its applicability to different scenarios. Additionally, the authors should consider including ablation studies to evaluate the impact of different components of the proposed method, such as the rewriting and judging steps.

Finally, the paper should include a detailed analysis of the computational cost associated with the proposed method. This should include the time and memory requirements for both training and inference. The authors should also compare the computational cost of the proposed method with standard pre-training methods. This analysis is crucial for assessing the practical feasibility of the approach. The authors should also discuss potential strategies for reducing the computational cost of the method, such as using more efficient RL algorithms or optimizing the prompts used for rewriting and judging. A thorough analysis of the computational cost would help to make the paper more impactful and useful for the research community.

### Questions

1. How does the proposed method compare to other pre-training approaches that incorporate safety, factuality, and quality judgments?
2. Can the proposed method be applied to other model architectures and pre-training datasets?

### Rating

5

### Confidence

3

**********

## Reviewer 2

### Summary

This paper proposes a new pre-training method that incorporates safety, factuality, and quality judgments into the pre-training process. The method uses a strong, post-trained model to rewrite pre-training data and judge policy model rollouts, thus using reinforcement earlier in training. Experiments show that this can give strong gains in quality, safety, factuality and reasoning.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is a combination of existing techniques, including LLM-as-judge and RL-based pre-training. The paper does not clearly articulate the novelty of the proposed approach beyond combining these techniques. The specific way in which the post-trained model is used for rewriting and judging, and how this differs from existing methods, needs further clarification.
2. The experiments are limited to a single model (Llama2 1.4B) and dataset (RedPajama). It is unclear whether the proposed method would generalize to other model architectures and pre-training datasets. The paper should include experiments on a wider range of models and datasets to demonstrate the robustness of the approach.
3. The paper lacks a detailed analysis of the computational cost associated with the proposed method. The use of a post-trained model for rewriting and judging adds computational overhead, which should be quantified and compared to standard pre-training methods.

### Suggestions

The paper should provide a more detailed explanation of how the proposed method differs from existing techniques, particularly in the context of using a post-trained model for rewriting and judging. A clear articulation of the novelty is crucial. For example, the authors could discuss the specific prompts used for the post-trained model to generate rewrites and judgments, and how these prompts are designed to capture the desired properties (safety, factuality, and quality). Furthermore, a comparison with other methods that use LLMs for similar tasks would help to highlight the unique contributions of this work. The authors should also clarify the specific RL algorithm used and provide details on the reward function, as these choices can significantly impact the performance of the method. A more detailed explanation of the method's novelty would significantly strengthen the paper.

To address the limited experimental scope, the authors should include experiments on a wider range of models and datasets. This would help to demonstrate the generalizability of the proposed method. For example, experiments on models with different architectures (e.g., encoder-decoder models) and datasets with different characteristics (e.g., synthetic data) would be valuable. The paper should also include a detailed analysis of the performance of the proposed method on different types of prompts and inputs. This would help to identify the strengths and weaknesses of the approach and provide insights into its applicability to different scenarios. Additionally, the authors should consider including ablation studies to evaluate the impact of different components of the proposed method, such as the rewriting and judging steps. This would help to understand the contribution of each component to the overall performance.

Finally, the paper should include a detailed analysis of the computational cost associated with the proposed method. This should include the time and memory requirements for both training and inference. The authors should also compare the computational cost of the proposed method with standard pre-training methods. This analysis is crucial for assessing the practical feasibility of the approach. The authors should also discuss potential strategies for reducing the computational cost of the method, such as using more efficient RL algorithms or optimizing the prompts used for rewriting and judging. A thorough analysis of the computational cost would help to make the paper more impactful and useful for the research community.

### Questions

See weaknesses.

### Rating

5

### Confidence

3

**********

## Reviewer 3

### Summary

This paper introduces a new pretraining method that incorporates safety, factuality, and quality judgments into the training process. The method uses a strong, post-trained model to rewrite pretraining data and judge policy model rollouts, thus using reinforcement learning earlier in training. Experiments show that this can give strong gains in quality, safety, factuality and reasoning.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is a combination of existing techniques, including LLM-as-judge and RL-based pre-training. The paper does not clearly articulate the novelty of the proposed approach beyond combining these techniques. The specific way in which the post-trained model is used for rewriting and judging, and how this differs from existing methods, needs further clarification.
2. The experiments are limited to a single model (Llama2 1.4B) and dataset (RedPajama). It is unclear whether the proposed method would generalize to other model architectures and pre-training datasets. The paper should include experiments on a wider range of models and datasets to demonstrate the robustness of the approach.
3. The paper lacks a detailed analysis of the computational cost associated with the proposed method. The use of a post-trained model for rewriting and judging adds computational overhead, which should be quantified and compared to standard pre-training methods.

### Suggestions

The paper would benefit from a more detailed explanation of the novelty of the proposed method. While the combination of LLM-as-judge and RL-based pre-training is not novel in itself, the specific way in which the post-trained model is used for rewriting and judging needs to be clearly articulated. The authors should provide a detailed comparison of their approach with existing methods that use LLMs for similar tasks, highlighting the unique aspects of their method. For example, they could discuss how the prompts used for the post-trained model to generate rewrites and judgments are designed, and how these prompts are different from those used in other methods. Furthermore, the authors should clarify the specific RL algorithm used and provide details on the reward function, as these choices can significantly impact the performance of the method. A more detailed explanation of the method's novelty would significantly strengthen the paper.

To address the limited experimental scope, the authors should include experiments on a wider range of models and datasets. The current experiments are limited to a single model (Llama2 1.4B) and a single dataset (RedPajama). This makes it difficult to assess the generalizability of the proposed method. The authors should include experiments on models with different architectures, such as encoder-decoder models, and datasets with different characteristics, such as synthetic data. This would help to demonstrate the robustness of the approach. Additionally, the authors should include a detailed analysis of the performance of the proposed method on different types of prompts and inputs. This would help to identify the strengths and weaknesses of the approach and provide insights into its applicability to different scenarios. The inclusion of ablation studies to evaluate the impact of different components of the proposed method, such as the rewriting and judging steps, would also be beneficial.

Finally, the paper should include a detailed analysis of the computational cost associated with the proposed method. The use of a post-trained model for rewriting and judging adds computational overhead, which should be quantified and compared to standard pre-training methods. The authors should provide a detailed breakdown of the computational cost of each step of the method, including the cost of generating rewrites, judging policy model rollouts, and training the policy model. This analysis should also include a comparison of the computational cost of the proposed method with standard pre-training methods. This would help to assess the practical feasibility of the approach and identify potential areas for optimization. The authors should also discuss potential strategies for reducing the computational cost of the method, such as using more efficient RL algorithms or optimizing the prompts used for rewriting and judging.

### Questions

Please see above.

### Rating

5

### Confidence

3

**********

## Reviewer 4

### Summary

The paper proposes a new pre-training method that incorporates safety, factuality, and quality judgments into the pre-training process. The method uses a strong, post-trained model to rewrite pre-training data and judge policy model rollouts, thus using reinforcement learning earlier in training. The experiments show that this approach can give strong gains in quality, safety, factuality, and reasoning.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and effective.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method is a combination of existing techniques, including LLM-as-judge and RL-based pre-training. The paper does not clearly articulate the novelty of the proposed approach beyond combining these techniques. The specific way in which the post-trained model is used for rewriting and judging, and how this differs from existing methods, needs further clarification.
- The experiments are limited to a single model (Llama2 1.4B) and dataset (RedPajama). It is unclear whether the proposed method would generalize to other model architectures and pre-training datasets. The paper should include experiments on a wider range of models and datasets to demonstrate the robustness of the approach.
- The paper lacks a detailed analysis of the computational cost associated with the proposed method. The use of a post-trained model for rewriting and judging adds computational overhead, which should be quantified and compared to standard pre-training methods.

### Suggestions

The paper would benefit from a more detailed explanation of the novelty of the proposed method. While the combination of LLM-as-judge and RL-based pre-training is not novel in itself, the specific way in which the post-trained model is used for rewriting and judging needs to be clearly articulated. The authors should provide a detailed comparison of their approach with existing methods that use LLMs for similar tasks, highlighting the unique aspects of their method. For example, they could discuss how the prompts used for the post-trained model to generate rewrites and judgments are designed, and how these prompts are different from those used in other methods. Furthermore, the authors should clarify the specific RL algorithm used and provide details on the reward function, as these choices can significantly impact the performance of the method. A more detailed explanation of the method's novelty would significantly strengthen the paper.

To address the limited experimental scope, the authors should include experiments on a wider range of models and datasets. The current experiments are limited to a single model (Llama2 1.4B) and a single dataset (RedPajama). This makes it difficult to assess the generalizability of the proposed method. The authors should include experiments on models with different architectures, such as encoder-decoder models, and datasets with different characteristics, such as synthetic data. This would help to demonstrate the robustness of the approach. Additionally, the authors should include a detailed analysis of the performance of the proposed method on different types of prompts and inputs. This would help to identify the strengths and weaknesses of the approach and provide insights into its applicability to different scenarios. The inclusion of ablation studies to evaluate the impact of different components of the proposed method, such as the rewriting and judging steps, would also be beneficial.

Finally, the paper should include a detailed analysis of the computational cost associated with the proposed method. The use of a post-trained model for rewriting and judging adds computational overhead, which should be quantified and compared to standard pre-training methods. The authors should provide a detailed breakdown of the computational cost of each step of the method, including the cost of generating rewrites, judging policy model rollouts, and training the policy model. This analysis should also include a comparison of the computational cost of the proposed method with standard pre-training methods. This would help to assess the practical feasibility of the approach and identify potential areas for optimization. The authors should also discuss potential strategies for reducing the computational cost of the method, such as using more efficient RL algorithms or optimizing the prompts used for rewriting and judging.

### Questions

- How does the proposed method compare to other pre-training approaches that incorporate safety, factuality, and quality judgments?
- Can the proposed method be applied to other model architectures and pre-training datasets?

### Rating

6

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The reviewer raises several valid points regarding the novelty, experimental scope, and computational cost of the proposed method. I need to carefully examine the paper to validate these claims with specific evidence.

**Plan:**

1. **Categorize Weaknesses:**  Identify the type of each weakness (novelty, experimental scope, computational cost).
2. **Methodological Verification:**  Examine the method description for evidence supporting or refuting the novelty claims. Look for explicit comparisons to existing techniques.
3. **Experimental Validation:** Check the experimental setup and results for evidence regarding the limited model/dataset scope and the absence of computational cost analysis.
4. **Synthesis and Reflection:**  Summarize the findings and assess the validity of each weakness.

**Weakness 1: Lack of Clarity on Novelty**

*   **Category:** Methodological
*   **Relevant Sections:** Introduction, Method
*   **Potential Misunderstanding:** The reviewer might be expecting a more explicit comparison to existing methods or a clearer articulation of the specific innovations.

**Weakness 2: Limited Experimental Scope**

*   **Category:** Experimental
*   **Relevant Sections:** Experiments
*   **Potential Misunderstanding:** The reviewer might be expecting a broader range of models and datasets to be tested.

**Weakness 3: Lack of Computational Cost Analysis**

*   **Category:** Practical
*   **Relevant Sections:** Method, Experiments
*   **Potential Misunderstanding:** The reviewer might be expecting a quantitative comparison of computational costs.

**Validating Weakness 1: Lack of Clarity on Novelty**

1. **Initial Weakness Categorization:**
    *   **Weakness Statement:** "The proposed method is a combination of existing techniques, including LLM-as-judge and RL-based pre-training. The paper does not clearly articulate the novelty of the proposed approach beyond combining these techniques. The specific way in which the post-trained model is used for rewriting and judging, and how this differs from existing methods, needs further clarification."
    *   **Key Evidence Collection:**
        a) **Method-related Evidence:**
            *   **Direct Quotes:** The introduction mentions "We hypothesize the current training pipeline is a fundamental cause of this issues, and fixing it could rectify some of these failings." and "Our method thus streams the pretraining data and at each step splits it into the most recent N N tokens (termed suffix), conditioned on the remaining earlier context (prefix). The existing post-trained model at this point is prompted to rewrite the suffix to steer away from potential unsafe or otherwise low-quality prefixes towards a high quality suffix, which can be used to pretrain our policy model." This describes the core mechanism but doesn't explicitly highlight novel aspects compared to existing LLM-as-judge or RL methods.
            *   **Related Missing Citations:** While the paper cites works on LLM-as-judge and RL-based pre-training, it doesn't explicitly position its method against these as distinct approaches or highlight specific novel contributions within that context.
        b) **Literature Gap Analysis:** The paper could benefit from a more explicit discussion of how its method differs from existing LLM-as-judge approaches (e.g., in the context of pre-training) and existing RL-based pre-training methods (e.g., in terms of the reward signal or training objective).
    2. **Validation Analysis:**
        *   **Primary Evidence Summary:** The paper describes a method that combines elements of LLM-as-judge and RL-based pre-training. While it outlines the steps, it lacks a clear statement of novelty beyond this combination.
        *   **Supporting Quotes:** The reviewer's statement accurately reflects the paper's structure and content. The method description focuses on the mechanics rather than the unique contribution.
        *   **Impact Assessment:** The lack of clear articulation of novelty makes it harder to understand the paper's contribution to the field.
    3. **Conclusion:**
        *   **Validity status:** Valid
        *   **Confidence level:** High
        *   **Key supporting evidence:** The method description focuses on combining existing techniques without explicitly stating novel contributions.

**Validating Weakness 2: Limited Experimental Scope**

1. **Initial Weakness Categorization:**
    *   **Weakness Statement:** "The experiments are limited to a single model (Llama2 1.4B) and dataset (RedPajama). It is unclear whether the proposed method would generalize to other model architectures and pre-training datasets. The paper should include experiments on a wider range of models and datasets to demonstrate the robustness of the approach."
    *   **Key Evidence Collection:**
        a) **Experimental Evidence:**
            *   **Dataset/setup descriptions:** The "Models and data" section explicitly states: "Models. We primarily use the pretrained Llama2 1.4 billion parameter model as a baseline policy model... Additionally, we conduct pretraining experiments where we train the same model from scratch by first re-initializing the weights. For the sequence pretraining task, we use chunk size N = 128... Both suffix judge and rewriter need to have strong instruction-following capabilities, as such we compare two models: (1) fine-tuned Llama3.1-8B-Instruct (Dubey et al., 2024) ; and (2) prompted GPT-OSS-120B (OpenAI, 2025)." This confirms the use of Llama2 1.4B and Llama3.1-8B-Instruct for evaluation, not just Llama2 1.4B. The datasets used are SlimPajama and RedPajama.
            *   **Results and metrics:** The "Experiments" section details results for both "Continual Pretraining" and "From-scratch Pretraining" settings, using different models and datasets in each.
    2. **Validation Analysis:**
        *   **Primary Evidence Summary:** The reviewer's statement is partially incorrect. The paper *does* include experiments with Llama3.1-8B-Instruct and uses different datasets (SlimPajama and RedPajama) in the continual pretraining setting.
        *   **Supporting Quotes:** The "Models and data" section explicitly mentions the use of Llama3.1-8B-Instruct and the datasets SlimPajama and RedPajama.
        *   **Impact Assessment:** While the primary focus is on Llama2 1.4B, the inclusion of Llama3.1-8B-Instruct and the use of different datasets in the continual pretraining setting address the generalization concern to some extent. However, testing on a broader range of architectures and datasets would further strengthen the findings.
    3. **Conclusion:**
        *   **Validity status:** Partially Valid
        *   **Confidence level:** High
        *   **Key supporting evidence:** The paper uses Llama3.1-8B-Instruct and different datasets in the continual pretraining setting, but the primary focus remains on Llama2 1.4B.

**Validating Weakness 3: Lack of Computational Cost Analysis**

1. **Initial Weakness Categorization:**
    *   **Weakness Statement:** "The paper lacks a detailed analysis of the computational cost associated with the proposed method. The use of a post-trained model for rewriting and judging adds computational overhead, which should be quantified and compared to standard pre-training methods."
    *   **Key Evidence Collection:**
        a) **Method-related Evidence:** The "Policy Model Training" section mentions using "online DPO ( Qi et al., 2024 ; 5.0e-06 constant learning rate. min ratio 0.1 0.1 , and 100 100 warmup steps. The maximum sequence length is set to 2048 tokens, and the model generates N = 128 new tokens for each rollout." and "For online DPO, we consider: (i) suffix vs 1 rollout, (ii) rewrite vs. 1 rollout, (iii) suffix vs. 16 rollouts; and (iv) 16 rollouts only." This describes the training process but doesn't provide computational cost details.
        b) **Experimental Evidence:** The "Implementation" subsections in the "Experiments" section provide details about the hardware and training parameters but do not include any metrics related to computational cost (e.g., training time, GPU hours).
    2. **Validation Analysis:**
        *   **Primary Evidence Summary:** The reviewer's statement is valid. The paper describes the method and provides experimental details but lacks any analysis or reporting of the computational cost associated with the proposed approach.
        *   **Supporting Quotes:** The method description focuses on the algorithmic steps, and the experimental setup details hardware and parameters but omits cost analysis.
        *   **Impact Assessment:** The absence of computational cost analysis makes it difficult to assess the practical feasibility and efficiency of the proposed method compared to standard pre-training.
    3. **Conclusion:**
        *   **Validity status:** Valid
        *   **Confidence level:** High
        *   **Key supporting evidence:** The paper lacks any discussion or metrics related to the computational cost of the proposed method.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces a novel pre-training approach designed to enhance the quality, safety, and factuality of language models by incorporating a post-trained model into the pre-training loop. The core idea revolves around using a strong, pre-trained language model to both rewrite the input context and to judge the quality of generated outputs. This is achieved by framing pre-training as a sequence prediction task, where the model predicts the next token within a sliding window of context. The key innovation lies in the use of the post-trained model to generate 'suffixes' – high-quality continuations of the input context, effectively acting as a form of guided pre-training. These suffixes are then used to train the policy model, which is the model being pre-trained. The post-trained model also serves as a judge, evaluating the quality of the model's own generated outputs, which are then used as 'rollouts' in a reinforcement learning framework. The authors explore various combinations of using the post-trained model for rewriting and judging, and they demonstrate that this approach leads to significant improvements in generation quality, safety, and factuality compared to standard pre-training methods. The experiments are conducted using the Llama2 1.4B model, with some additional experiments using Llama3.1-8B-Instruct in a 'from-scratch' pre-training setting. The results show that the proposed method, particularly when using a fine-tuned Llama3.1-8B-Instruct model as the post-trained judge, achieves substantial gains in various evaluation metrics. The paper also includes ablation studies to analyze the impact of different components of the proposed method, such as the number of rollouts used for training. Overall, the paper presents a compelling approach to pre-training that leverages a post-trained model to guide the learning process, resulting in improved model performance across multiple dimensions. However, as I will discuss in the following sections, there are some limitations in the novelty of the approach, the scope of the experiments, and the lack of a detailed computational cost analysis that need to be addressed to fully validate its potential.


## Soundness:

2.75


## Presentation:

2.75


## Contribution:

2.5


## Strengths:

The paper's primary strength lies in its clear and well-structured presentation of the proposed method. The authors articulate the core idea of using a post-trained model to guide pre-training in a way that is easy to understand and follow. The approach of framing pre-training as a sequence prediction task, with the post-trained model acting as a suffix rewriter and a quality judge, is both intuitive and effective. The experimental results, particularly those obtained using the Llama3.1-8B-Instruct model as the post-trained judge, demonstrate a significant improvement in generation quality, safety, and factuality. This is a compelling empirical achievement that highlights the potential of the proposed method. Furthermore, the inclusion of ablation studies provides valuable insights into the impact of different components of the approach, such as the number of rollouts used for training. The paper also explores different configurations for the post-trained model, including fine-tuned and prompted versions, which adds to the robustness of the findings. The authors also provide a detailed description of the experimental setup, including the datasets used and the training parameters, which allows for reproducibility. The paper's focus on addressing the critical issues of safety, factuality, and quality in pre-training is also a significant strength. These are areas that have been largely overlooked in previous research, and the proposed method offers a promising solution to these challenges. The use of a post-trained model to rewrite the input context and to judge the quality of generated outputs is a novel approach that has the potential to significantly improve the performance of language models. The paper's clear writing style and well-organized structure make it easy to read and understand, which is a significant strength in itself. The authors also provide a good overview of the related work, which helps to contextualize their contributions. The paper's focus on practical applications and its potential to improve the performance of language models in real-world settings is also a significant strength. The proposed method is relatively simple to implement, which makes it accessible to a wide range of researchers and practitioners. Overall, the paper presents a compelling approach to pre-training that has the potential to significantly improve the performance of language models across multiple dimensions.


## Weaknesses:

While the paper presents a compelling approach, several weaknesses need to be addressed. First, the paper does not clearly articulate the novelty of the proposed method beyond combining existing techniques. While the authors frame their approach as a novel way to integrate post-trained model rewrites and judgments into the pre-training pipeline, the specific way in which the post-trained model is used for rewriting and judging, and how this differs from existing methods, needs further clarification. The paper describes the core mechanism of using a post-trained model to rewrite the input context and to judge the quality of generated outputs, but it does not explicitly highlight novel aspects compared to existing LLM-as-judge or RL methods. The paper cites works on LLM-as-judge and RL-based pre-training, but it does not explicitly position its method against these as distinct approaches or highlight specific novel contributions within that context. This lack of clear articulation of novelty makes it difficult to understand the paper's contribution to the field. The paper also lacks a detailed analysis of the computational cost associated with the proposed method. The use of a post-trained model for rewriting and judging adds computational overhead, which should be quantified and compared to standard pre-training methods. The authors describe the method and provide experimental details about the hardware and training parameters but do not include any metrics related to computational cost, such as training time or GPU hours. This absence of computational cost analysis makes it difficult to assess the practical feasibility and efficiency of the proposed method compared to standard pre-training. The paper also lacks a detailed explanation of how the proposed method differs from existing techniques, particularly in the context of using a post-trained model for rewriting and judging. While the paper describes the steps of the method, it does not provide a clear articulation of the novelty of the proposed approach beyond combining these techniques. The authors should discuss the specific prompts used for the post-trained model to generate rewrites and judgments, and how these prompts are designed to capture the desired properties (safety, factuality, and quality). Furthermore, a comparison with other methods that use LLMs for similar tasks would help to highlight the unique contributions of this work. The authors should also clarify the specific RL algorithm used and provide details on the reward function, as these choices can significantly impact the performance of the method. A more detailed explanation of the method's novelty would significantly strengthen the paper. The paper also needs to include experiments on a wider range of models and datasets. While the paper includes experiments with Llama3.1-8B-Instruct and uses different datasets (SlimPajama and RedPajama) in the continual pretraining setting, the primary focus is on Llama2 1.4B. The paper should include experiments on models with different architectures, such as encoder-decoder models, and datasets with different characteristics, such as synthetic data. This would help to demonstrate the robustness of the approach. Additionally, the authors should include a detailed analysis of the performance of the proposed method on different types of prompts and inputs. This would help to identify the strengths and weaknesses of the approach and provide insights into its applicability to different scenarios. The inclusion of ablation studies to evaluate the impact of different components of the proposed method, such as the rewriting and judging steps, would also be beneficial. Finally, the paper should include a detailed analysis of the computational cost associated with the proposed method. This should include the time and memory requirements for both training and inference. The authors should also compare the computational cost of the proposed method with standard pre-training methods. This analysis is crucial for assessing the practical feasibility of the approach and identifying potential areas for optimization. The authors should also discuss potential strategies for reducing the computational cost of the method, such as using more efficient RL algorithms or optimizing the prompts used for rewriting and judging. The lack of a detailed analysis of the computational cost makes it difficult to assess the practical feasibility and efficiency of the proposed method compared to standard pre-training.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the paper needs to provide a more detailed explanation of the novelty of the proposed method. While the combination of LLM-as-judge and RL-based pre-training is not novel in itself, the specific way in which the post-trained model is used for rewriting and judging needs to be clearly articulated. The authors should provide a detailed comparison of their approach with existing methods that use LLMs for similar tasks, highlighting the unique aspects of their method. For example, they could discuss how the prompts used for the post-trained model to generate rewrites and judgments are designed, and how these prompts are different from those used in other methods. Furthermore, a comparison with other methods that use LLMs for similar tasks would help to highlight the unique contributions of this work. The authors should also clarify the specific RL algorithm used and provide details on the reward function, as these choices can significantly impact the performance of the method. A more detailed explanation of the method's novelty would significantly strengthen the paper. Second, to address the limited experimental scope, the authors should include experiments on a wider range of models and datasets. This would help to demonstrate the generalizability of the proposed method. For example, experiments on models with different architectures (e.g., encoder-decoder models) and datasets with different characteristics (e.g., synthetic data) would be valuable. The paper should also include a detailed analysis of the performance of the proposed method on different types of prompts and inputs. This would help to identify the strengths and weaknesses of the approach and provide insights into its applicability to different scenarios. Additionally, the authors should consider including ablation studies to evaluate the impact of different components of the proposed method, such as the rewriting and judging steps. This would help to understand the contribution of each component to the overall performance. The inclusion of these additional experiments would help to demonstrate the robustness of the approach. Third, the paper should include a detailed analysis of the computational cost associated with the proposed method. This should include the time and memory requirements for both training and inference. The authors should also compare the computational cost of the proposed method with standard pre-training methods. This analysis is crucial for assessing the practical feasibility of the approach and identifying potential areas for optimization. The authors should also discuss potential strategies for reducing the computational cost of the method, such as using more efficient RL algorithms or optimizing the prompts used for rewriting and judging. A thorough analysis of the computational cost would help to make the paper more impactful and useful for the research community. Finally, the paper should include a more detailed explanation of the method's novelty. While the combination of LLM-as-judge and RL-based pre-training is not novel in itself, the specific way in which the post-trained model is used for rewriting and judging needs to be clearly articulated. The authors should provide a detailed comparison of their approach with existing methods that use LLMs for similar tasks, highlighting the unique aspects of their method. For example, they could discuss how the prompts used for the post-trained model to generate rewrites and judgments are designed, and how these prompts are different from those used in other methods. Furthermore, a comparison with other methods that use LLMs for similar tasks would help to highlight the unique contributions of this work. The authors should also clarify the specific RL algorithm used and provide details on the reward function, as these choices can significantly impact the performance of the method. A more detailed explanation of the method's novelty would significantly strengthen the paper.


## Questions:

Several key questions arise from my analysis of this paper. First, how does the proposed method compare to other pre-training approaches that incorporate safety, factuality, and quality judgments? The paper focuses on a specific combination of LLM-as-judge and RL-based pre-training, but it does not explicitly compare its approach to other methods that use similar techniques. A more detailed comparison would help to contextualize the paper's contributions and highlight its unique aspects. Second, can the proposed method be applied to other model architectures and pre-training datasets? The primary focus of the paper is on Llama2 1.4B and Llama3.1-8B-Instruct, but it is unclear whether the method would generalize to other model architectures or datasets. A more detailed analysis of the method's performance on different types of models and datasets would be valuable. Third, what is the specific impact of the rewriting and judging steps on the overall performance of the method? The paper includes ablation studies, but it would be helpful to have a more detailed analysis of the contribution of each component to the overall performance. This would help to understand the strengths and weaknesses of the approach and identify areas for further improvement. Fourth, what are the specific prompts used for the post-trained model to generate rewrites and judgments, and how were these prompts designed? The paper describes the use of a post-trained model, but it does not provide detailed information about the prompts used to generate rewrites and judgments. A more detailed explanation of the prompts would help to understand the specific way in which the post-trained model is used for rewriting and judging. Fifth, what is the specific RL algorithm used, and what is the reward function? The paper mentions the use of online DPO, but it does not provide detailed information about the specific RL algorithm and reward function used. A more detailed explanation of these aspects would help to understand the specific implementation of the method. Finally, what is the computational cost of the proposed method, and how does it compare to standard pre-training methods? The paper does not include any analysis of the computational cost of the proposed method, which makes it difficult to assess its practical feasibility. A more detailed analysis of the computational cost would be valuable for understanding the trade-offs between performance and efficiency.


## Rating:

5.25


## Confidence:

3.0


## Decision:

Reject
}