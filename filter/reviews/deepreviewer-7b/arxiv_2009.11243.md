I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper trains a learned optimizer on a large number of tasks to achieve better generalization. The authors use derivative-free optimization to optimize the hyperparameters of the learned optimizer. The authors show that the learned optimizer generalizes well to unseen tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow.
- The paper trains a learned optimizer on a large number of tasks to achieve better generalization.
- The authors use derivative-free optimization to optimize the hyperparameters of the learned optimizer.

### Weaknesses

#### Some Related Works


#### comment

 - The paper trains a learned optimizer on a large number of tasks to achieve better generalization. The authors use derivative-free optimization to optimize the hyperparameters of the learned optimizer. The authors show that the learned optimizer generalizes well to unseen tasks.

- The paper trains a learned optimizer on a large number of tasks to achieve better generalization. The authors use derivative-free optimization to optimize the hyperparameters of the learned optimizer. The authors show that the learned optimizer generalizes well to unseen tasks.

- The paper trains a learned optimizer on a large number of tasks to achieve better generalization. The authors use derivative-free optimization to optimize the hyperparameters of the learned optimizer. The authors show that the learned optimizer generalizes well to unseen tasks.

- The paper trains a learned optimizer on a large number of tasks to achieve better generalization. The authors use derivative-free optimization to optimize the hyperparameters of the learned optimizer. The authors show that the learned optimizer generalizes well to unseen tasks.

### Suggestions

The paper's core idea of training a learned optimizer on a diverse set of tasks to improve generalization is promising, but the current implementation and evaluation could be significantly strengthened. The use of derivative-free optimization, while potentially beneficial for hyperparameter tuning, introduces a layer of complexity that needs to be carefully addressed. The authors should provide more details on the specific derivative-free optimization algorithm used, including its convergence properties and computational cost. Furthermore, a more thorough analysis of the learned optimizer's architecture and its components is needed. For example, what is the rationale behind the chosen LSTM architecture? How does the per-parameter feedforward network contribute to performance? A more detailed ablation study, beyond the one presented, would be beneficial to understand the contribution of each component. Specifically, the impact of different LSTM cell types, activation functions, and network depths should be explored. This would provide a more complete picture of the learned optimizer's inner workings and allow for more informed design choices in future work.

To further enhance the paper, the authors should consider a more rigorous evaluation protocol. While the current experiments demonstrate generalization to unseen tasks, the scope of these tasks could be expanded. The authors should consider evaluating the learned optimizer on a wider range of tasks with varying complexities and data modalities. This would provide a more robust assessment of the learned optimizer's generalization capabilities. Additionally, the paper would benefit from a comparison against a broader set of baselines, including other learned optimizers and adaptive learning rate methods. This would help to contextualize the performance of the proposed approach and highlight its advantages and limitations. The authors should also investigate the sensitivity of the learned optimizer to different training data distributions and sizes. This would provide insights into the robustness of the learned optimizer and its applicability to real-world scenarios.

Finally, the paper should include a more detailed discussion of the computational cost associated with training and deploying the learned optimizer. The authors should quantify the training time and memory requirements, and compare them to those of traditional optimizers. This is crucial for assessing the practical feasibility of the proposed approach. Furthermore, the authors should discuss the potential for optimizing the learned optimizer's architecture and training procedure to reduce its computational footprint. This could involve techniques such as pruning, quantization, or knowledge distillation. Addressing these points would significantly strengthen the paper and make it more impactful for the research community.

### Questions

- How does the performance of the learned optimizer compare to other learned optimizers and adaptive learning rate methods on a wider range of tasks?
- What is the computational cost of training and deploying the learned optimizer compared to traditional optimizers?
- How does the performance of the learned optimizer vary with different training data distributions and sizes?

### Rating

6

### Confidence

3

**********

## Reviewer 2

### Summary

This paper proposes a new learned optimizer that is trained on a large dataset of tasks. The authors show that this learned optimizer generalizes well to unseen tasks and can be used to train models from scratch. The authors also show that the learned optimizer can adapt to changes in the task distribution and can be used to train models with different architectures.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

The paper is well-written and easy to follow. The authors provide a good overview of the related work and clearly state the contributions of their paper. The authors also provide a good explanation of the methodology and the experimental setup. The authors provide a good analysis of the results and discuss the limitations of their work.

### Weaknesses

#### Some Related Works


#### comment

The paper does not provide a detailed analysis of the learned optimizer's performance on different types of tasks. It would be interesting to see how the learned optimizer performs on tasks with different characteristics, such as tasks with different levels of complexity, different data modalities, or different optimization landscapes. The authors should also provide a more detailed analysis of the learned optimizer's hyperparameters and how they affect its performance. It would be useful to see how the learned optimizer's performance varies with different hyperparameter settings and whether there are any optimal hyperparameter values for different types of tasks. Furthermore, the paper lacks a comparison with other learned optimizers. It would be beneficial to see how the proposed learned optimizer compares to other state-of-the-art learned optimizers in terms of performance, computational cost, and generalization ability. The authors should also discuss the limitations of their approach and potential directions for future research. For example, how does the learned optimizer perform when the training data is limited or noisy? How does the learned optimizer scale to very large models or datasets? Addressing these questions would provide a more complete picture of the learned optimizer's capabilities and limitations.

### Suggestions

To address the lack of detailed analysis on different task types, the authors should consider a more granular evaluation of their learned optimizer. Instead of just reporting average performance across all tasks, they could categorize tasks based on their characteristics (e.g., complexity, data modality, optimization landscape) and report performance metrics separately for each category. For example, they could evaluate the optimizer on tasks with varying degrees of non-convexity, tasks with different data modalities (e.g., images, text, time series), and tasks with different optimization landscapes (e.g., sparse, dense). This would provide a more nuanced understanding of the optimizer's strengths and weaknesses. Furthermore, the authors should investigate the sensitivity of the learned optimizer to its hyperparameters. They could perform a hyperparameter search, varying key parameters such as learning rate, batch size, and optimizer architecture, and report how these parameters affect performance across different task types. This analysis could reveal optimal hyperparameter settings for different task categories and provide insights into the optimizer's robustness. It would also be beneficial to analyze the learned optimizer's internal representations and how they adapt to different tasks. This could provide a deeper understanding of the learned optimization process and potentially lead to more efficient and effective optimizers.

To address the lack of comparison with other learned optimizers, the authors should include a more comprehensive benchmark against existing state-of-the-art learned optimizers. This benchmark should not only compare performance metrics but also consider computational cost, memory usage, and generalization ability. The authors should select a diverse set of learned optimizers that represent different approaches to learned optimization, such as those based on recurrent neural networks, transformers, or other architectures. They should also ensure that the comparison is fair by using the same training data, evaluation protocol, and hardware. The authors should also discuss the limitations of their approach in more detail. For example, they could investigate how the learned optimizer performs when the training data is limited or noisy, which is a common challenge in real-world applications. They could also explore how the optimizer scales to very large models or datasets, which is crucial for its applicability to large-scale machine learning problems. Furthermore, the authors should discuss potential future research directions, such as improving the generalization ability of the learned optimizer to unseen tasks, reducing its computational cost, and extending it to other machine learning domains.

### Questions

How does the learned optimizer perform on tasks with different characteristics, such as tasks with different levels of complexity, different data modalities, or different optimization landscapes?
What are the optimal hyperparameter settings for the learned optimizer, and how do these settings vary across different types of tasks?
How does the learned optimizer compare to other learned optimizers in terms of performance, computational cost, and generalization ability?
How does the learned optimizer perform when the training data is limited or noisy?
How does the learned optimizer scale to very large models or datasets?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper trains a learned optimizer on a large number of tasks, making use of TaskSet dataset and a new outer-optimization algorithm. The authors show that the learned optimizer generalizes well to unseen tasks, and can be used to train models from scratch.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well written and easy to follow. The authors provide a clear motivation for their work and a detailed explanation of their methodology.
- The authors provide a comprehensive set of experiments, including comparisons with several baseline optimizers and ablation studies on the components of their learned optimizer. The results are presented clearly and are well supported by the experimental evidence.
- The authors provide a detailed discussion of the limitations of their work and potential directions for future research.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the learned optimizer's performance on different types of tasks. It would be interesting to see how the learned optimizer performs on tasks with different characteristics, such as tasks with different levels of complexity, different data modalities, or different optimization landscapes. Specifically, the paper lacks a breakdown of performance across tasks with varying degrees of non-convexity, different data distributions, and different optimization difficulties. This makes it hard to assess the generalizability of the learned optimizer.
- The authors should also provide a more detailed analysis of the learned optimizer's hyperparameters and how they affect its performance. It would be useful to see how the learned optimizer's performance varies with different hyperparameter settings and whether there are any optimal hyperparameter values for different types of tasks. The paper does not explore the sensitivity of the learned optimizer to its own hyperparameters, such as the learning rate, the number of layers, or the size of the hidden states. This makes it difficult to understand the robustness of the learned optimizer and its potential for practical use.
- Furthermore, the paper lacks a comparison with other learned optimizers. It would be beneficial to see how the proposed learned optimizer compares to other state-of-the-art learned optimizers in terms of performance, computational cost, and generalization ability. The paper should include a comparison with other learned optimizers that are specifically designed for optimization tasks, not just general learned models. This would provide a better understanding of the advantages and disadvantages of the proposed approach.

### Suggestions

To address the lack of detailed analysis on different task types, the authors should categorize the tasks in the TaskSet dataset based on their characteristics, such as complexity, data modality, and optimization landscape. For example, they could group tasks by the number of local minima, the smoothness of the loss surface, or the presence of specific data modalities. Then, they should report the performance of the learned optimizer on each category, allowing for a more granular understanding of its strengths and weaknesses. Furthermore, the authors should investigate the correlation between task characteristics and the optimizer's performance. This could involve techniques such as correlation analysis or feature importance analysis to identify which task properties are most influential on the optimizer's behavior. This would provide valuable insights into the generalizability of the learned optimizer and its potential for use in new domains.

To address the lack of analysis on the learned optimizer's hyperparameters, the authors should perform a thorough sensitivity analysis. This could involve varying key hyperparameters, such as the learning rate, the number of layers, and the size of the hidden states, and observing their impact on performance across different task categories. The authors should also explore the use of techniques such as Bayesian optimization or random search to identify optimal hyperparameter settings for different task types. This would provide a better understanding of the robustness of the learned optimizer and its potential for practical use. Furthermore, the authors should investigate whether the optimal hyperparameters are consistent across different task categories or whether they need to be tuned for each specific task. This would provide insights into the transferability of the learned optimizer's architecture.

Finally, to address the lack of comparison with other learned optimizers, the authors should include a comprehensive benchmark against state-of-the-art learned optimizers that are specifically designed for optimization tasks. This benchmark should include a variety of optimizers, such as those based on recurrent neural networks, transformers, or other architectures. The authors should compare the performance, computational cost, and generalization ability of the proposed learned optimizer with these other optimizers. This would provide a better understanding of the advantages and disadvantages of the proposed approach and its potential for practical use. The authors should also discuss the limitations of the TaskSet dataset and how it might affect the generalizability of the learned optimizer. This would provide a more complete picture of the learned optimizer's capabilities and limitations.

### Questions

- How does the learned optimizer perform on tasks with different characteristics, such as tasks with different levels of complexity, different data modalities, or different optimization landscapes?
- What are the optimal hyperparameter settings for the learned optimizer, and how do these settings vary across different types of tasks?
- How does the learned optimizer compare to other learned optimizers in terms of performance, computational cost, and generalization ability?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

This paper proposes a learned optimizer that is trained on a large dataset of tasks. The authors show that this learned optimizer generalizes well to unseen tasks and can be used to train models from scratch. The authors also show that the learned optimizer can adapt to changes in the task distribution and can be used to train models with different architectures.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a good overview of the related work and clearly state the contributions of their paper.
3. The authors also provide a good explanation of the methodology and the experimental setup.
4. The authors provide a good analysis of the results and discuss the limitations of their work.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the learned optimizer's performance on different types of tasks. It would be interesting to see how the learned optimizer performs on tasks with different characteristics, such as tasks with different levels of complexity, different data modalities, or different optimization landscapes. Specifically, the paper lacks a breakdown of performance across tasks with varying degrees of non-convexity, different data distributions, and different optimization difficulties. This makes it hard to assess the generalizability of the learned optimizer.
2. The authors should also provide a more detailed analysis of the learned optimizer's hyperparameters and how they affect its performance. It would be useful to see how the learned optimizer's performance varies with different hyperparameter settings and whether there are any optimal hyperparameter values for different types of tasks. The paper does not explore the sensitivity of the learned optimizer to its own hyperparameters, such as the learning rate, the number of layers, or the size of the hidden states. This makes it difficult to understand the robustness of the learned optimizer and its potential for practical use.
3. Furthermore, the paper lacks a comparison with other learned optimizers. It would be beneficial to see how the proposed learned optimizer compares to other state-of-the-art learned optimizers in terms of performance, computational cost, and generalization ability. The paper should include a comparison with other learned optimizers that are specifically designed for optimization tasks, not just general learned models. This would provide a better understanding of the advantages and disadvantages of the proposed approach.

### Suggestions

To address the lack of detailed analysis on different task types, the authors should categorize the tasks in the TaskSet dataset based on their characteristics, such as complexity, data modality, and optimization landscape. For example, they could group tasks by the number of local minima, the smoothness of the loss surface, or the presence of specific data modalities. Then, they should report the performance of the learned optimizer on each category, allowing for a more granular understanding of its strengths and weaknesses. Furthermore, the authors should investigate the correlation between task characteristics and the optimizer's performance. This could involve techniques such as correlation analysis or feature importance analysis to identify which task properties are most influential on the optimizer's behavior. This would provide valuable insights into the generalizability of the learned optimizer and its potential for use in new domains.

To address the lack of analysis on the learned optimizer's hyperparameters, the authors should perform a thorough sensitivity analysis. This could involve varying key hyperparameters, such as the learning rate, the number of layers, and the size of the hidden states, and observing their impact on performance across different task categories. The authors should also explore the use of techniques such as Bayesian optimization or random search to identify optimal hyperparameter settings for different task types. This would provide a better understanding of the robustness of the learned optimizer and its potential for practical use. Furthermore, the authors should investigate whether the optimal hyperparameters are consistent across different task categories or whether they need to be tuned for each specific task. This would provide insights into the transferability of the learned optimizer's architecture.

Finally, to address the lack of comparison with other learned optimizers, the authors should include a comprehensive benchmark against state-of-the-art learned optimizers that are specifically designed for optimization tasks. This benchmark should include a variety of optimizers, such as those based on recurrent neural networks, transformers, or other architectures. The authors should compare the performance, computational cost, and generalization ability of the proposed learned optimizer with these other optimizers. This would provide a better understanding of the advantages and disadvantages of the proposed approach and its potential for practical use. The authors should also discuss the limitations of the TaskSet dataset and how it might affect the generalizability of the learned optimizer. This would provide a more complete picture of the learned optimizer's capabilities and limitations.

### Questions

1. How does the learned optimizer perform on tasks with different characteristics, such as tasks with different levels of complexity, different data modalities, or different optimization landscapes?
2. What are the optimal hyperparameter settings for the learned optimizer, and how do these settings vary across different types of tasks?
3. How does the learned optimizer compare to other learned optimizers in terms of performance, computational cost, and generalization ability?

### Rating

6

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in a given paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

Here's my plan:
1. **Go through each reviewer's comments one by one.**
2. **For each weakness identified by the reviewer, locate the relevant section in the paper.**
3. **Find specific evidence (quotes, numbers, missing information) to support the reviewer's claim.**
4. **If the weakness is valid, summarize the evidence.**
5. **If the weakness is not valid, explain why based on the paper's content.**
6. **Pay attention to potential overlaps or contradictions between different reviewers' comments.**
**Review 1**

1. Weakness Statement:
"The paper trains a learned optimizer on a large number of tasks to achieve better generalization. The authors use derivative-free optimization to optimize the hyperparameters of the learned optimizer. The authors show that the learned optimizer generalizes well to unseen tasks."

2. Evidence Collection:
a) Method-related Evidence:
   - "To train the optimizer, we minimize an outer-loss that quantifies the performance of the optimizer. This is defined as the mean of the inner- and outer- losses computed on inner- validation set for some number of unrolled steps, averaged over inner-tasks in the outer-training taskset. Although this outer-loss is differentiable, it is costly to compute the outer-gradient (which involves backpropagating through the unrolled optimization). In addition, the outer-loss surface is badly conditioned and extremely non-smooth [ 14 ] , making it difficult to optimize. We deal with these issues by using derivative-free optimization–specifically, evolutionary strategies (ES) [ 20 ] –to minimize the outer-loss, obviating the need to compute derivatives through the unrolled optimization process." (Section 3.1)
   - "Initial unroll lengths were chosen to balance communication cost between parallel workers (when updating optimizer parameters) with the computational cost of unrolling on individual workers (when estimating the local gradient with ES). We start outer-training by sampling unroll steps uniformly from 240-360 steps. When performance saturates, we continue training with Persistent Evolotionary Strategies (PES) [ 21 ] . PES provides an unbiased estimate of the outer-gradient over the entire inner task, but at the cost of higher variance gradients." (Section 3.1)

3. Literature Gap Analysis:
   - The paper cites [20] for ES and [21] for PES.

4. Validation Analysis:
   - The reviewer accurately summarizes the paper's approach of training a learned optimizer on a large number of tasks and using derivative-free optimization (ES and PES) to train it.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Direct quotes from Section 3.1 describing the training process and the use of derivative-free optimization.

1. Weakness Statement:
"The authors use derivative-free optimization to optimize the hyperparameters of the learned optimizer. The authors show that the learned optimizer generalizes well to unseen tasks."

2. Evidence Collection:
a) Method-related Evidence:
   - "To train the optimizer, we minimize an outer-loss that quantifies the performance of the optimizer. This is defined as the mean of the inner- and outer- losses computed on inner- validation set for some number of unrolled steps, averaged over inner-tasks in the outer-training taskset. Although this outer-loss is differentiable, it is costly to compute the outer-gradient (which involves backpropagating through the unrolled optimization). In addition, the outer-loss surface is badly conditioned and extremely non-smooth [ 14 ] , making it difficult to optimize. We deal with these issues by using derivative-free optimization–specifically, evolutionary strategies (ES) [ 20 ] –to minimize the outer-loss, obviating the need to compute derivatives through the unrolled optimization process." (Section 3.1)
   - "Initial unroll lengths were chosen to balance communication cost between parallel workers (when updating optimizer parameters) with the computational cost of unrolling on individual workers (when estimating the local gradient with ES). We start outer-training by sampling unroll steps uniformly from 240-360 steps. When performance saturates, we continue training with Persistent Evolotionary Strategies (PES) [ 21 ] . PES provides an unbiased estimate of the outer-gradient over the entire inner task, but at the cost of higher variance gradients." (Section 3.1)

3. Literature Gap Analysis:
   - The paper cites [20] for ES and [21] for PES.

4. Validation Analysis:
   - The reviewer accurately summarizes the paper's approach of training the learned optimizer using derivative-free optimization.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Direct quotes from Section 3.1 describing the training process and the use of derivative-free optimization.

1. Weakness Statement:
"The authors show that the learned optimizer generalizes well to unseen tasks."

2. Evidence Collection:
b) Experiment-related Evidence:
   - "To test this type of generalization, we trained fully connected neural networks on CIFAR-10 and MNIST, and swept three model hyperparameters: the number of hidden units per layer (network width), the batch size, and the number of training examples (dataset size, formed by subsampling the full dataset)." (Section 4.4)
   - "As we vary the number of hidden units (left column) or batch size (middle column), the learned optimizer generalizes outside of the range of hidden units used during training (indicated by the shaded regions). In addition, the learned optimizer matches the performance of the best learning rate tuned Adam optimizer. On CIFAR-10, as we move further away from the outer-training task distribution, the learned optimizer diverges. For dataset size (right column), we find that the learned optimizer is more sensitive to the amount of data present (performance drops off more quickly as the dataset size decreases)." (Section 4.4)
   - "For CIFAR-10, we find that the learned optimizer achieves similar performance as the baselines but does not overfit later in inner-training. For ImageNet, we find that the learned optimizer performs slightly worse." (Section 4.5)

4. Validation Analysis:
   - The reviewer accurately summarizes the paper's demonstration of generalization to unseen tasks, specifically in Section 4.4 and 4.5.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Direct quotes from Sections 4.4 and 4.5 describing the experiments on generalization to unseen tasks.

**Review 2**

1. Weakness Statement:
"The paper does not provide a detailed analysis of the learned optimizer's performance on different types of tasks. It would be interesting to see how the learned optimizer performs on tasks with different characteristics, such as tasks with different levels of complexity, different data modalities, or different optimization landscapes. Specifically, the paper lacks a breakdown of performance across tasks with varying degrees of non-convexity, different data distributions, and different optimization difficulties. This makes it hard to assess the generalizability of the learned optimizer."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper evaluates the learned optimizer on a variety of tasks from the TaskSet dataset, including RNNs, CNNs, masked auto-regressive flows, fully connected networks, language modeling, variational autoencoders, and simple 2D test functions (Section 3.2).
   - The paper also evaluates the learned optimizer on large-scale machine learning tasks like CIFAR-10 and ImageNet (Section 4.4 and 4.5).
   - The paper evaluates the learned optimizer on large-scale problems with different architectures (ResNet V2 and Transformer V2) (Section 4.5).
   - The paper evaluates the learned optimizer on large-scale problems with different dataset sizes (CIFAR-10 and MNIST) (Section 4.4).

4. Validation Analysis:
   - While the paper doesn't explicitly categorize tasks by complexity, non-convexity, data distribution, or optimization landscape, it does evaluate the learned optimizer across a diverse set of tasks and datasets. The reviewer's point about a more granular analysis based on specific task characteristics is valid.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper presents results on various tasks, but lacks a specific analysis based on the characteristics mentioned by the reviewer.

1. Weakness Statement:
"The authors should also provide a more detailed analysis of the learned optimizer's hyperparameters and how they affect its performance. It would be useful to see how the learned optimizer's performance varies with different hyperparameter settings and whether there are any optimal hyperparameter values for different types of tasks. The paper does not explore the sensitivity of the learned optimizer to its own hyperparameters, such as the learning rate, the number of layers, or the size of the hidden states. This makes it difficult to understand the robustness of the learned optimizer and its potential for practical use."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper describes the architecture of the learned optimizer, including the hierarchical LSTM structure, per-parameter LSTM, and per-tensor feedforward network (Section 3.3).
b) Experiment-related Evidence:
   - The paper mentions the number of layers in the LSTM (24 layers) and the hidden dimension (128) in the per-tensor feedforward network (Section 3.3).
   - The paper mentions the number of unrolling steps (240-360) (Section 3.1).
   - The paper mentions the use of 1024 multi-core CPU workers (Section 3.1).
   - The paper mentions the use of 1000 different hyperparameter values for the baseline optimizers (Section 4.1).
   - The paper mentions the use of random search for hyperparameter optimization (Section 4.1).
   - The paper mentions the use of antithetic sampling and train-test splits (Section 4.1).
   - The paper mentions the use of 1000 different hyperparameter values for the learned optimizer (Section 3.3).

4. Validation Analysis:
   - The reviewer is correct that the paper doesn't provide a detailed analysis of the sensitivity of the learned optimizer's performance to its own hyperparameters. While the paper describes the architecture, it doesn't explore how different architectural choices or hyperparameters within the optimizer affect its performance across different tasks.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper describes the architecture but lacks a systematic analysis of its hyperparameters.

1. Weakness Statement:
"Furthermore, the paper lacks a comparison with other learned optimizers. It would be beneficial to see how the proposed learned optimizer compares to other state-of-the-art learned optimizers in terms of performance, computational cost, and generalization ability. The paper should include a comparison with other learned optimizers that are specifically designed for optimization tasks, not just general learned models. This would provide a better understanding of the advantages and disadvantages of the proposed approach and its potential for practical use."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper compares the learned optimizer with Adam, Adam8p, and Adam10p (Section 4.2).
   - The paper compares the learned optimizer with AdamLR, Adam8p, and Adam10p (Section 4.3).
   - The paper compares the learned optimizer with opt_list and opt_list (Section 4.4).
   - The paper compares the learned optimizer with Adam, Momentum, and SGD (Section 4.5).

4. Validation Analysis:
   - The reviewer's statement is inaccurate. The paper does include comparisons with several learned optimizers in different experimental sections.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: Sections 4.2, 4.3, 4.4, and 4.5 explicitly compare the proposed learned optimizer with other learned optimizers.

**Review 3**

1. Weakness Statement:
"The paper does not provide a detailed analysis of the learned optimizer's performance on different types of tasks. It would be interesting to see how the learned optimizer performs on tasks with different characteristics, such as tasks with different levels of complexity, different data modalities, or different optimization landscapes. Specifically, the paper lacks a breakdown of performance across tasks with varying degrees of non-convexity, different data distributions, and different optimization difficulties. This makes it hard to assess the generalizability of the learned optimizer."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper evaluates the learned optimizer on a variety of tasks from the TaskSet dataset, including RNNs, CNNs, masked auto-regressive flows, fully connected networks, language modeling, variational autoencoders, and simple 2D test functions (Section 3.2).
   - The paper also evaluates the learned optimizer on large-scale machine learning tasks like CIFAR-10 and ImageNet (Section 4.4 and 4.5).
   - The paper evaluates the learned optimizer on large-scale problems with different architectures (ResNet V2 and Transformer V2) (Section 4.5).
   - The paper evaluates the learned optimizer on large-scale problems with different dataset sizes (CIFAR-10 and MNIST) (Section 4.4).

4. Validation Analysis:
   - Similar to Reviewer 2, this reviewer also points out the lack of a detailed analysis based on specific task characteristics. The paper demonstrates generalization across different tasks, but doesn't deeply analyze performance based on task complexity, data modality, or optimization landscape.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper shows results on various tasks, but lacks a specific analysis based on the characteristics mentioned by the reviewer.

1. Weakness Statement:
"The authors should also provide a more detailed analysis of the learned optimizer's hyperparameters and how they affect its performance. It would be useful to see how the learned optimizer's performance varies with different hyperparameter settings and whether there are any optimal hyperparameter values for different types of tasks. The paper does not explore the sensitivity of the learned optimizer to its own hyperparameters, such as the learning rate, the number of layers, or the size of the hidden states. This makes it difficult to understand the robustness of the learned optimizer and its potential for practical use."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper describes the architecture of the learned optimizer, including the hierarchical LSTM structure, per-parameter LSTM, and per-tensor feedforward network (Section 3.3).
b) Experiment-related Evidence:
   - The paper mentions the number of layers in the LSTM (24 layers) and the hidden dimension (128) in the per-tensor feedforward network (Section 3.3).
   - The paper mentions the number of unrolling steps (240-360) (Section 3.1).
   - The paper mentions the use of 1024 multi-core CPU workers (Section 3.1).
   - The paper mentions the use of 1000 different hyperparameter values for the baseline optimizers (Section 4.1).
   - The paper mentions the use of random search for hyperparameter optimization (Section 4.1).
   - The paper mentions the use of antithetic sampling and train-test splits (Section 4.1).
   - The paper mentions the use of 1000 different hyperparameter values for the learned optimizer (Section 3.3).

4. Validation Analysis:
   - This reviewer also correctly points out the lack of a detailed analysis of the learned optimizer's hyperparameters. The paper describes the architecture but doesn't explore the sensitivity of performance to its own hyperparameters.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper describes the architecture but lacks a systematic analysis of its hyperparameters.

1. Weakness Statement:
"Furthermore, the paper lacks a comparison with other learned optimizers. It would be beneficial to see how the proposed learned optimizer compares to other state-of-the-art learned optimizers in terms of performance, computational cost, and generalization ability. The paper should include a comparison with other learned optimizers that are specifically designed for optimization tasks, not just general learned models. This would provide a better understanding of the advantages and disadvantages of the proposed approach and its potential for practical use."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper compares the learned optimizer with Adam, Adam8p, and Adam10p (Section 4.2).
   - The paper compares the learned optimizer with AdamLR, Adam8p, and Adam10p (Section 4.3).
   - The paper compares the learned optimizer with opt_list and opt_list (Section 4.4).
   - The paper compares the learned optimizer with Adam, Momentum, and SGD (Section 4.5).

4. Validation Analysis:
   - As with Reviewer 2, this reviewer's statement is incorrect. The paper does include comparisons with several learned optimizers.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: Sections 4.2, 4.3, 4.4, and 4.5 explicitly compare the proposed learned optimizer with other learned optimizers.

**Review 4**

1. Weakness Statement:
"The paper does not provide a detailed analysis of the learned optimizer's performance on different types of tasks. It would be interesting to see how the learned optimizer performs on tasks with different characteristics, such as tasks with different levels of complexity, different data modalities, or different optimization landscapes. Specifically, the paper lacks a breakdown of performance across tasks with varying degrees of non-convexity, different data distributions, and different optimization difficulties. This makes it hard to assess the generalizability of the learned optimizer."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper evaluates the learned optimizer on a variety of tasks from the TaskSet dataset, including RNNs, CNNs, masked auto-regressive flows, fully connected networks, language modeling, variational autoencoders, and simple 2D test functions (Section 3.2).
   - The paper also evaluates the learned optimizer on large-scale machine learning tasks like CIFAR-10 and ImageNet (Section 4.4 and 4.5).
   - The paper evaluates the learned optimizer on large-scale problems with different architectures (ResNet V2 and Transformer V2) (Section 4.5).
   - The paper evaluates the learned optimizer on large-scale problems with different dataset sizes (CIFAR-10 and MNIST) (Section 4.4).

4. Validation Analysis:
   - Similar to previous reviewers, this reviewer also points out the lack of a detailed analysis based on specific task characteristics.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper shows results on various tasks, but lacks a specific analysis based on the characteristics mentioned by the reviewer.

1. Weakness Statement:
"The authors should also provide a more detailed analysis of the learned optimizer's hyperparameters and how they affect its performance. It would be useful to see how the learned optimizer's performance varies with different hyperparameter settings and whether there are any optimal hyperparameter values for different types of tasks. The paper does not explore the sensitivity of the learned optimizer to its own hyperparameters, such as the learning rate, the number of layers, or the size of the hidden states. This makes it difficult to understand the robustness of the learned optimizer and its potential for practical use."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper describes the architecture of the learned optimizer, including the hierarchical LSTM structure, per-parameter LSTM, and per-tensor feedforward network (Section 3.3).
b) Experiment-related Evidence:
   - The paper mentions the number of layers in the LSTM (24 layers) and the hidden dimension (128) in the per-tensor feedforward network (Section 3.3).
   - The paper mentions the number of unrolling steps (240-360) (Section 3.1).
   - The paper mentions the use of 1024 multi-core CPU workers (Section 3.1).
   - The paper mentions the use of 1000 different hyperparameter values for the baseline optimizers (Section 4.1).
   - The paper mentions the use of random search for hyperparameter optimization (Section 4.1).
   - The paper mentions the use of antithetic sampling and train-test splits (Section 4.1).
   - The paper mentions the use of 1000 different hyperparameter values for the learned optimizer (Section 3.3).

4. Validation Analysis:
   - This reviewer also correctly identifies the lack of a detailed analysis of the learned optimizer's hyperparameters.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper describes the architecture but lacks a systematic analysis of its hyperparameters.

1. Weakness Statement:
"Furthermore, the paper lacks a comparison with other learned optimizers. It would be beneficial to see how the proposed learned optimizer compares to other state-of-the-art learned optimizers in terms of performance, computational cost, and generalization ability. The paper should include a comparison with other learned optimizers that are specifically designed for optimization tasks, not just general learned models. This would provide a better understanding of the advantages and disadvantages of the proposed approach and its potential for practical use."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper compares the learned optimizer with Adam, Adam8p, and Adam10p (Section 4.2).
   - The paper compares the learned optimizer with AdamLR, Adam8p, and Adam10p (Section 4.3).
   - The paper compares the learned optimizer with opt_list and opt_list (Section 4.4).
   - The paper compares the learned optimizer with Adam, Momentum, and SGD (Section 4.5).

4. Validation Analysis:
   - As previously established, this reviewer's statement is incorrect.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: Sections 4.2, 4.3, 4.4, and 4.5 explicitly compare the proposed learned optimizer with other learned optimizers.

1. Weakness Statement:
"How does the learned optimizer perform on tasks with different characteristics, such as tasks with different levels of complexity, different data modalities, or different optimization landscapes?"

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper evaluates the learned optimizer on a variety of tasks from the TaskSet dataset, including RNNs, CNNs, masked auto-regressive flows, fully connected networks, language modeling, variational autoencoders, and simple 2D test functions (Section 3.2).
   - The paper also evaluates the learned optimizer on large-scale machine learning tasks like CIFAR-10 and ImageNet (Section 4.4 and 4.5).
   - The paper evaluates the learned optimizer on large-scale problems with different architectures (ResNet V2 and Transformer V2) (Section 4.5).
   - The paper evaluates the learned optimizer on large-scale problems with different dataset sizes (CIFAR-10 and MNIST) (Section 4.4).

4. Validation Analysis:
   - While the paper doesn't explicitly categorize tasks by complexity, data modality, or optimization landscape, it does evaluate the learned optimizer across a diverse set of tasks and datasets. The reviewer's question highlights the lack of a detailed analysis based on these specific characteristics.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper presents results on various tasks, but lacks a specific analysis based on the characteristics mentioned by the reviewer.

1. Weakness Statement:
"What are the optimal hyperparameter settings for the learned optimizer, and how do these settings vary across different types of tasks?"

2. Evidence Collection:
a) Method-related Evidence:
   - The paper describes the architecture of the learned optimizer, including the hierarchical LSTM structure, per-parameter LSTM, and per-tensor feedforward network (Section 3.3).
b) Experiment-related Evidence:
   - The paper mentions the number of layers in the LSTM (24 layers) and the hidden dimension (128) in the per-tensor feedforward network (Section 3.3).
   - The paper mentions the number of unrolling steps (240-360) (Section 3.1).
   - The paper mentions the use of 1000 different hyperparameter values for the learned optimizer (Section 3.3).

4. Validation Analysis:
   - The paper describes the architecture and mentions the hyperparameters used, but it doesn't provide a detailed analysis of optimal hyperparameter settings or how they vary across tasks.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper describes the architecture and mentions hyperparameters but lacks a detailed analysis of optimal settings and their variation.

1. Weakness Statement:
"How does the learned optimizer compare to other learned optimizers in terms of performance, computational cost, and generalization ability?"

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper compares the learned optimizer with Adam, Adam8p, and Adam10p (Section 4.2).
   - The paper compares the learned optimizer with AdamLR, Adam8p, and Adam10p (Section 4.3).
   - The paper compares the learned optimizer with opt_list and opt_list (Section 4.4).
   - The paper compares the learned optimizer with Adam, Momentum, and SGD (Section 4.5).

4. Validation Analysis:
   - The paper does include comparisons with several learned optimizers.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: Sections 4.2, 4.3, 4.4, and 4.5 explicitly compare the proposed learned optimizer with other learned optimizers.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces a novel approach to learning optimizers by training a neural network to mimic the behavior of established optimization algorithms, such as Adam, across a diverse set of tasks. The core idea is to leverage the TaskSet dataset, which comprises a wide range of optimization problems, to enable the learned optimizer to generalize effectively to unseen tasks. The authors employ derivative-free optimization techniques, specifically evolutionary strategies (ES) and its variant Persistent Evolutionary Strategies (PES), to train the learned optimizer. This choice is motivated by the computational challenges associated with backpropagating through unrolled optimization steps, which is necessary for training the learned optimizer. The learned optimizer itself is a hierarchical LSTM architecture, designed to process the sequence of iterates generated during optimization. This architecture includes a per-parameter LSTM and a per-tensor feedforward network, which are intended to capture both the temporal dependencies in the optimization trajectory and the local context of the parameters. The authors conduct extensive experiments to evaluate the performance of the learned optimizer. They compare it against hand-designed optimizers on tasks within the TaskSet dataset, as well as on large-scale machine learning tasks such as CIFAR-10 and ImageNet. The results demonstrate that the learned optimizer can achieve comparable or better performance than hand-designed optimizers, particularly when trained on a large and diverse set of tasks. Furthermore, the authors show that the learned optimizer can be used to train models from scratch and can adapt to changes in the task distribution and different architectures. The paper also explores the generalization capabilities of the learned optimizer by evaluating its performance on tasks with varying numbers of training examples and different dataset sizes. The authors find that the learned optimizer generalizes well to some extent, but its performance degrades as the dataset size decreases. Overall, this work presents a compelling approach to learning optimizers, demonstrating the potential of learned optimizers to outperform hand-designed ones and to adapt to a variety of optimization tasks. The use of derivative-free optimization for training the learned optimizer is a key methodological choice that enables the approach to scale to large numbers of unrolled steps. The empirical findings highlight the potential of this approach for automating the design of optimization algorithms and for improving the performance of machine learning models.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

3.0


## Strengths:

This paper presents several notable strengths that contribute to its overall significance. First, the core idea of training a learned optimizer on a large and diverse set of tasks is a promising approach to automating the design of optimization algorithms. The use of the TaskSet dataset, which encompasses a wide range of optimization problems, is a key factor in the success of this approach. The authors demonstrate that the learned optimizer can generalize well to unseen tasks, which is a crucial requirement for any practical optimization algorithm. The empirical results presented in the paper are compelling, showing that the learned optimizer can achieve comparable or better performance than hand-designed optimizers on a variety of tasks. The experiments on large-scale machine learning tasks, such as CIFAR-10 and ImageNet, further validate the effectiveness of the learned optimizer. The authors also explore the generalization capabilities of the learned optimizer by evaluating its performance on tasks with varying numbers of training examples and different dataset sizes. The fact that the learned optimizer can adapt to changes in the task distribution and different architectures is another significant strength of this work. The use of derivative-free optimization techniques, specifically evolutionary strategies (ES) and Persistent Evolutionary Strategies (PES), to train the learned optimizer is a key methodological choice that enables the approach to scale to large numbers of unrolled steps. This is a significant technical innovation that allows the learned optimizer to be trained on a large and diverse set of tasks. The hierarchical LSTM architecture used for the learned optimizer is also a notable contribution. This architecture is designed to capture both the temporal dependencies in the optimization trajectory and the local context of the parameters. The paper is well-written and easy to follow, and the authors provide a clear motivation for their work and a detailed explanation of their methodology. The authors also provide a good analysis of the results and discuss the limitations of their work. The inclusion of ablation studies and comparisons with several baseline optimizers further strengthens the paper's claims. Overall, the paper presents a well-executed and well-motivated study that makes a significant contribution to the field of optimization.


## Weaknesses:

While this paper presents a compelling approach to learning optimizers, there are several weaknesses that warrant careful consideration. One significant limitation is the lack of a detailed analysis of the learned optimizer's performance on tasks with varying characteristics. While the paper evaluates the learned optimizer on a diverse set of tasks, it does not provide a breakdown of performance across tasks with different levels of complexity, data modalities, or optimization landscapes. Specifically, the paper lacks a systematic analysis of how the learned optimizer's performance varies with different task characteristics, such as the number of local minima, the smoothness of the loss surface, or the presence of specific data modalities. This makes it difficult to assess the generalizability of the learned optimizer and to understand the specific scenarios in which it performs best. The paper also lacks a detailed analysis of the learned optimizer's hyperparameters and how they affect its performance. While the paper describes the architecture of the learned optimizer, it does not explore the sensitivity of the learned optimizer to its own hyperparameters, such as the learning rate, the number of layers, or the size of the hidden states. This makes it difficult to understand the robustness of the learned optimizer and its potential for practical use. The paper mentions using 1000 different hyperparameter values for the learned optimizer, but it does not provide any analysis of how these hyperparameters were tuned or how they affect the performance of the learned optimizer across different task types. Furthermore, the paper does not provide a detailed comparison with other learned optimizers that are specifically designed for optimization tasks. While the paper does compare the learned optimizer with several hand-designed optimizers, it does not include a comparison with other state-of-the-art learned optimizers that are specifically designed for optimization tasks. This makes it difficult to assess the advantages and disadvantages of the proposed approach and its potential for practical use. The paper should include a comparison with other learned optimizers that are specifically designed for optimization tasks, not just general learned models. This would provide a better understanding of the advantages and disadvantages of the proposed approach and its potential for practical use. Finally, the paper does not provide a detailed discussion of the computational cost associated with training and deploying the learned optimizer. The authors should quantify the training time and memory requirements, and compare them to those of traditional optimizers. This is crucial for assessing the practical feasibility of the proposed approach. The paper should also discuss the potential for optimizing the learned optimizer's architecture and training procedure to reduce its computational footprint. These limitations, while not invalidating the core contributions of the paper, do highlight areas where further research is needed to fully realize the potential of learned optimizers.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should conduct a more granular evaluation of the learned optimizer's performance on tasks with varying characteristics. Instead of just reporting average performance across all tasks, they should categorize tasks based on their complexity, data modality, and optimization landscape. For example, they could group tasks by the number of local minima, the smoothness of the loss surface, or the presence of specific data modalities. Then, they should report the performance of the learned optimizer on each category, allowing for a more granular understanding of its strengths and weaknesses. Furthermore, the authors should investigate the correlation between task characteristics and the optimizer's performance. This could involve techniques such as correlation analysis or feature importance analysis to identify which task properties are most influential on the optimizer's behavior. This would provide valuable insights into the generalizability of the learned optimizer and its potential for use in new domains. Second, to address the lack of analysis on the learned optimizer's hyperparameters, the authors should perform a thorough sensitivity analysis. This could involve varying key hyperparameters, such as the learning rate, the number of layers, and the size of the hidden states, and observing their impact on performance across different task categories. The authors should also explore the use of techniques such as Bayesian optimization or random search to identify optimal hyperparameter settings for different task types. This would provide a better understanding of the robustness of the learned optimizer and its potential for practical use. Furthermore, the authors should investigate whether the optimal hyperparameters are consistent across different task categories or whether they need to be tuned for each specific task. This would provide insights into the transferability of the learned optimizer's architecture. Third, the authors should include a comprehensive benchmark against state-of-the-art learned optimizers that are specifically designed for optimization tasks. This benchmark should not only compare performance metrics but also consider computational cost, memory usage, and generalization ability. The authors should select a diverse set of learned optimizers, such as those based on recurrent neural networks, transformers, or other architectures. They should also ensure that the comparison is fair by using the same training data, evaluation protocol, and hardware. The authors should also discuss the limitations of the TaskSet dataset and how it might affect the generalizability of the learned optimizer. This would provide a more complete picture of the learned optimizer's capabilities and limitations. Finally, the authors should provide a more detailed discussion of the computational cost associated with training and deploying the learned optimizer. The authors should quantify the training time and memory requirements, and compare them to those of traditional optimizers. This is crucial for assessing the practical feasibility of the proposed approach. The authors should also discuss the potential for optimizing the learned optimizer's architecture and training procedure to reduce its computational footprint. These improvements would significantly strengthen the paper and provide a more complete understanding of the learned optimizer's capabilities and limitations.


## Questions:

Several key questions arise from my analysis of this paper. First, how does the learned optimizer perform on tasks with different characteristics, such as tasks with varying levels of complexity, different data modalities, or different optimization landscapes? While the paper evaluates the learned optimizer on a diverse set of tasks, it lacks a detailed analysis of performance based on these specific characteristics. Understanding how the learned optimizer adapts to different task properties is crucial for assessing its generalizability. Second, what are the optimal hyperparameter settings for the learned optimizer, and how do these settings vary across different types of tasks? The paper describes the architecture of the learned optimizer but does not provide a detailed analysis of its hyperparameters or how they affect its performance. It is important to understand the sensitivity of the learned optimizer to its own hyperparameters and whether there are any optimal hyperparameter values for different types of tasks. Third, how does the learned optimizer compare to other learned optimizers in terms of performance, computational cost, and generalization ability? The paper compares the learned optimizer with hand-designed optimizers but does not include a comparison with other state-of-the-art learned optimizers that are specifically designed for optimization tasks. A more comprehensive comparison would provide a better understanding of the advantages and disadvantages of the proposed approach and its potential for practical use. Fourth, what is the computational cost of training and deploying the learned optimizer compared to traditional optimizers? The paper does not provide a detailed discussion of the computational cost associated with training and deploying the learned optimizer. This is crucial for assessing the practical feasibility of the proposed approach. Finally, how does the performance of the learned optimizer vary with different training data distributions and sizes? The paper evaluates the learned optimizer on large-scale machine learning tasks like CIFAR-10 and ImageNet, but it does not explore how the performance of the learned optimizer varies with different training data distributions and sizes. Understanding how the learned optimizer performs when the training data is limited or noisy is crucial for its applicability to real-world scenarios.


## Rating:

6.0


## Confidence:

3.0


## Decision:

Accept
}