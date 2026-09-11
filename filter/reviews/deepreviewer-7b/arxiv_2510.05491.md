I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper introduces NorMuon, an optimization algorithm that combines the orthogonalization approach of Muon with per-neuron adaptive learning rates. The authors demonstrate that NorMuon achieves faster training convergence and improved memory efficiency compared to AdamW and Muon, while maintaining a comparable memory footprint to Muon. The paper also presents a distributed implementation of NorMuon compatible with the FSDP2 framework, which enables efficient training of large language models.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow, with clear explanations of the algorithm and its implementation.
2. The paper provides a comprehensive set of experiments across multiple model scales, demonstrating the effectiveness of NorMuon in various settings.
3. The paper presents a novel approach to combining orthogonalization with per-neuron adaptive learning rates, which is a significant contribution to the field of optimization algorithms.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational overhead of NorMuon compared to other optimizers, such as AdamW and Muon. While the authors claim that NorMuon is more efficient, they do not provide concrete evidence to support this claim. Specifically, the paper lacks a breakdown of the time spent on each step of the algorithm, such as the computation of the orthogonalized updates and the per-neuron adaptive learning rates. This makes it difficult to assess the true computational cost of NorMuon and to understand where the performance gains come from.
2. The paper does not provide a detailed analysis of the memory usage of NorMuon compared to other optimizers, such as AdamW and Muon. While the authors claim that NorMuon is more memory-efficient, they do not provide concrete evidence to support this claim. The paper should include a breakdown of the memory usage for each component of the algorithm, such as the momentum states, the orthogonalized updates, and the per-neuron adaptive learning rates. This would allow for a more precise comparison of the memory usage of NorMuon with other optimizers.
3. The paper does not provide a detailed analysis of the convergence behavior of NorMuon compared to other optimizers, such as AdamW and Muon. While the authors claim that NorMuon converges faster, they do not provide concrete evidence to support this claim. The paper should include a more detailed analysis of the convergence behavior, such as the training loss and the validation loss over time. This would allow for a more precise comparison of the convergence behavior of NorMuon with other optimizers.
4. The paper does not provide a detailed analysis of the sensitivity of NorMuon to hyperparameters, such as the learning rate and the momentum parameters. While the authors claim that NorMuon is robust to hyperparameter choices, they do not provide concrete evidence to support this claim. The paper should include a more detailed analysis of the sensitivity of NorMuon to hyperparameters, such as the learning rate, the momentum parameters, and the per-neuron adaptive learning rates. This would allow for a better understanding of the robustness of NorMuon to hyperparameter choices.
5. The paper does not provide a detailed analysis of the scalability of NorMuon to larger models and datasets. While the authors claim that NorMuon is scalable, they do not provide concrete evidence to support this claim. The paper should include a more detailed analysis of the scalability of NorMuon to larger models and datasets, such as the training time and the memory usage. This would allow for a better understanding of the scalability of NorMuon to larger models and datasets.

### Suggestions

To address the lack of detailed computational analysis, the authors should provide a breakdown of the time spent on each step of the NorMuon algorithm, including the computation of the orthogonalized updates and the per-neuron adaptive learning rates. This analysis should be conducted on different hardware configurations and with different model sizes to understand how the computational cost scales. Furthermore, the authors should compare the computational cost of NorMuon with other optimizers, such as AdamW and Muon, using the same hardware and model sizes. This would provide a more concrete understanding of the computational advantages of NorMuon. The authors should also investigate the impact of different optimization parameters, such as the learning rate and the momentum parameters, on the computational cost of NorMuon. This would help to identify the optimal parameter settings for NorMuon and to understand the trade-offs between computational cost and performance.

To address the lack of detailed memory usage analysis, the authors should provide a breakdown of the memory usage for each component of the NorMuon algorithm, such as the momentum states, the orthogonalized updates, and the per-neuron adaptive learning rates. This analysis should be conducted on different hardware configurations and with different model sizes to understand how the memory usage scales. Furthermore, the authors should compare the memory usage of NorMuon with other optimizers, such as AdamW and Muon, using the same hardware and model sizes. This would provide a more precise understanding of the memory efficiency of NorMuon. The authors should also investigate the impact of different optimization parameters, such as the learning rate and the momentum parameters, on the memory usage of NorMuon. This would help to identify the optimal parameter settings for NorMuon and to understand the trade-offs between memory usage and performance.

To address the lack of detailed convergence analysis, the authors should provide a more detailed analysis of the convergence behavior of NorMuon compared to other optimizers, such as AdamW and Muon. This analysis should include the training loss and the validation loss over time, as well as the convergence rate and the final performance. The authors should also investigate the impact of different optimization parameters, such as the learning rate and the momentum parameters, on the convergence behavior of NorMuon. This would help to identify the optimal parameter settings for NorMuon and to understand the trade-offs between convergence speed and final performance. Furthermore, the authors should compare the convergence behavior of NorMuon with other optimizers on different datasets and model sizes to understand the generalizability of NorMuon.

### Questions

1. Can the authors provide more details on the computational overhead of NorMuon compared to other optimizers, such as AdamW and Muon?
2. Can the authors provide more details on the memory usage of NorMuon compared to other optimizers, such as AdamW and Muon?
3. Can the authors provide more details on the convergence behavior of NorMuon compared to other optimizers, such as AdamW and Muon?
4. Can the authors provide more details on the sensitivity of NorMuon to hyperparameters, such as the learning rate and the momentum parameters?
5. Can the authors provide more details on the scalability of NorMuon to larger models and datasets?

### Rating

5

### Confidence

4

**********

## Reviewer 2

### Summary

This paper proposes NorMuon, a new optimizer that combines the benefits of two recent optimizers, AdamW and Muon. AdamW is a well-known optimizer that is widely used in modern deep learning. Muon is a more recent optimizer that uses orthogonalization to improve the conditioning of the updates. The authors show that NorMuon outperforms both AdamW and Muon on a variety of tasks, including language modeling and image classification. The authors also provide a detailed analysis of the properties of NorMuon, including its convergence rate and its sensitivity to hyperparameters.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow.
- The authors provide a thorough analysis of the properties of NorMuon, including its convergence rate and its sensitivity to hyperparameters.
- NorMuon outperforms both AdamW and Muon on a variety of tasks, including language modeling and image classification.
- NorMuon is a simple and effective optimizer that can be easily integrated into existing deep learning frameworks.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational cost of NorMuon compared to AdamW and Muon. While the authors claim that NorMuon is more efficient, they do not provide concrete evidence to support this claim.
- The paper does not provide a detailed analysis of the memory usage of NorMuon compared to AdamW and Muon. While the authors claim that NorMuon is more memory-efficient, they do not provide concrete evidence to support this claim.
- The paper does not provide a detailed analysis of the convergence rate of NorMuon compared to AdamW and Muon. While the authors claim that NorMuon converges faster, they do not provide concrete evidence to support this claim.
- The paper does not provide a detailed analysis of the sensitivity of NorMuon to hyperparameters compared to AdamW and Muon. While the authors claim that NorMuon is less sensitive to hyperparameters, they do not provide concrete evidence to support this claim.
- The paper does not provide a detailed analysis of the scalability of NorMuon to larger models and datasets. While the authors claim that NorMuon is scalable, they do not provide concrete evidence to support this claim.

### Suggestions

The paper would benefit significantly from a more rigorous comparison of NorMuon against AdamW and Muon, focusing on computational cost, memory usage, convergence rate, and sensitivity to hyperparameters. For instance, the authors should provide a detailed breakdown of the FLOPs required for each optimizer during training, including the cost of the orthogonalization step in Muon and the per-neuron adaptive learning rates in NorMuon. This analysis should be conducted across different model sizes and hardware configurations to provide a comprehensive understanding of the computational trade-offs. Furthermore, the authors should quantify the memory overhead associated with maintaining the second-order momentum and per-neuron adaptive learning rates for NorMuon, and compare this to the memory footprint of AdamW and Muon. This should include a breakdown of memory usage for different components of the optimizers, such as the momentum tensors, the orthogonalization matrices, and the per-neuron scaling factors. Such a detailed analysis would allow for a more informed assessment of the practical benefits of NorMuon in resource-constrained environments.

To strengthen the claims regarding convergence, the authors should present a more detailed analysis of the training loss curves for NorMuon, AdamW, and Muon across different tasks and model sizes. This analysis should include not only the final training loss but also the convergence rate, defined as the number of iterations or epochs required to reach a certain level of performance. The authors should also investigate the impact of different hyperparameters on the convergence behavior of each optimizer, including the learning rate, the momentum parameters, and the parameters related to the per-neuron adaptive learning rates. This analysis should be conducted using a range of hyperparameter values to identify the optimal settings for each optimizer and to assess the robustness of NorMuon to hyperparameter choices. Furthermore, the authors should provide a theoretical analysis of the convergence properties of NorMuon, including a proof of convergence under certain assumptions and a discussion of the conditions under which NorMuon is expected to outperform AdamW and Muon.

Finally, the paper should include a more thorough investigation of the scalability of NorMuon to larger models and datasets. This should include experiments with models that have significantly more parameters than those used in the current study, as well as experiments with datasets that are larger in size and more diverse in nature. The authors should also analyze the scaling behavior of NorMuon with respect to model size and dataset size, including the computational cost and memory usage as a function of these parameters. This analysis should be conducted using a range of hardware configurations to assess the scalability of NorMuon in different computing environments. Furthermore, the authors should compare the performance of NorMuon on larger models and datasets to the performance of AdamW and Muon, to determine whether NorMuon maintains its advantages in more challenging scenarios. This would provide a more comprehensive understanding of the practical applicability of NorMuon in real-world applications.

### Questions

- How does NorMuon compare to AdamW and Muon in terms of computational cost, memory usage, convergence rate, and sensitivity to hyperparameters?
- How does NorMuon scale to larger models and datasets?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper proposes NorMuon, a new optimizer that combines the benefits of Muon and AdamW. Muon uses orthogonalization to improve conditioning of updates, while AdamW uses per-parameter adaptive learning rates. NorMuon integrates these two approaches by maintaining second-order momentum statistics for each neuron and applying row-wise normalization after orthogonalization. The authors develop an efficient distributed implementation of NorMuon compatible with FSDP2, which partitions optimizer states across devices using ZeRO-3 style sharding. They conduct experiments across multiple model scales (124M, 350M, 1.1B, and 5.4B parameters) and demonstrate that NorMuon consistently outperforms both AdamW and Muon in terms of training efficiency and final performance. The paper also provides an analysis of the memory and computational overhead of NorMuon compared to AdamW and Muon, showing that NorMuon achieves comparable memory efficiency to Muon with a small increase in computational cost.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow. The authors clearly explain the motivation for NorMuon, the technical details of the algorithm, and the implementation challenges of the distributed version. The figures and tables are well-designed and effectively communicate the key results.
- The experiments are comprehensive and well-designed. The authors conduct experiments across multiple model scales and compare NorMuon to strong baselines like AdamW and Muon. They also provide detailed ablation studies to justify their design choices, such as the granularity of adaptive learning rates and the positioning of normalization. The results consistently show that NorMuon outperforms the baselines in terms of training efficiency and final performance.
- The paper addresses an important problem in deep learning optimization: how to combine the benefits of different optimizers. NorMuon provides a practical solution that integrates orthogonalization and adaptive learning rates in a way that is both effective and efficient. The authors also provide a detailed analysis of the memory and computational overhead of NorMuon, which is important for practical deployment.

### Weaknesses

#### Some Related Works


#### comment

 - The paper focuses on language modeling tasks, but it is unclear how well NorMuon would generalize to other domains, such as image classification or reinforcement learning. The authors should provide more evidence that NorMuon is effective across a range of tasks.
- The paper does not provide a detailed analysis of the convergence properties of NorMuon. While the authors show that NorMuon converges faster than AdamW and Muon, they do not provide a theoretical analysis of why this is the case. It would be helpful to understand the conditions under which NorMuon is guaranteed to converge and how its convergence rate compares to other optimizers.
- The paper does not provide a detailed analysis of the sensitivity of NorMuon to hyperparameters. While the authors show that NorMuon is robust to some hyperparameter choices, it is unclear how sensitive it is to other hyperparameters, such as the learning rate or the momentum parameters. It would be helpful to provide a more detailed analysis of the hyperparameter tuning process and to identify the optimal hyperparameter settings for different tasks.

### Suggestions

The authors should investigate the performance of NorMuon on a wider range of tasks beyond language modeling. Specifically, experiments on image classification datasets such as CIFAR-10 or ImageNet, and reinforcement learning tasks would be valuable. These tasks have different characteristics than language modeling, such as different data distributions and optimization landscapes, and would provide a more comprehensive evaluation of NorMuon's generalizability. For image classification, the authors could use standard architectures like ResNet or VGG, and for reinforcement learning, they could use OpenAI Gym environments. It would also be beneficial to analyze the behavior of NorMuon in these different settings, looking at metrics like training loss, validation accuracy, and convergence speed. This would help to identify any potential limitations of NorMuon and to guide future research.

To strengthen the theoretical analysis, the authors should explore the convergence properties of NorMuon in more detail. While the empirical results are promising, a theoretical understanding of why NorMuon converges faster than AdamW and Muon would be valuable. This could involve analyzing the optimization landscape and the behavior of the algorithm in different regions. For example, the authors could investigate the eigenvalues of the Hessian matrix and how they are affected by NorMuon's orthogonalization and adaptive learning rate mechanisms. Additionally, it would be helpful to compare the convergence rate of NorMuon to other optimizers, such as LAMB, which is known to have good convergence properties. This could involve deriving bounds on the convergence rate or conducting experiments with different learning rates and batch sizes. A more rigorous theoretical analysis would provide a deeper understanding of NorMuon's behavior and its potential limitations.

Finally, the authors should provide a more detailed analysis of the sensitivity of NorMuon to hyperparameters. While the authors show that NorMuon is robust to some hyperparameter choices, it is unclear how sensitive it is to other hyperparameters, such as the learning rate, momentum parameters, and the parameters related to the per-neuron adaptive learning rates. The authors should conduct a more systematic hyperparameter tuning process and identify the optimal hyperparameter settings for different tasks. This could involve using techniques like grid search or Bayesian optimization. It would also be helpful to analyze the impact of different hyperparameter settings on the convergence rate and the final performance of NorMuon. This would provide a more complete picture of NorMuon's behavior and help practitioners to effectively use it in different settings.

### Questions

- How does NorMuon perform on other tasks, such as image classification or reinforcement learning?
- What are the theoretical properties of NorMuon? How does it compare to other optimizers in terms of convergence rate and stability?
- How sensitive is NorMuon to hyperparameters? Are there any best practices for tuning the hyperparameters?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

The paper proposes NorMuon, a new optimizer that combines the benefits of Muon and AdamW. Muon uses orthogonalization to improve the conditioning of updates, while AdamW uses per-parameter adaptive learning rates. NorMuon integrates these two approaches by maintaining second-order momentum statistics for each neuron and applying row-wise normalization after orthogonalization. The authors develop an efficient distributed implementation of NorMuon compatible with the FSDP2 framework, which partitions optimizer states across devices. They conduct experiments across multiple model scales and demonstrate that NorMuon consistently outperforms both AdamW and Muon in terms of training efficiency and final performance. The paper also provides an analysis of the memory and computational overhead of NorMuon compared to AdamW and Muon, showing that NorMuon achieves comparable memory efficiency to Muon with a small increase in computational cost.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow. The authors clearly explain the motivation for NorMuon, the technical details of the algorithm, and the implementation challenges of the distributed version. The figures and tables are well-designed and effectively communicate the key results.
- The experiments are comprehensive and well-designed. The authors conduct experiments across multiple model scales and compare NorMuon to strong baselines like AdamW and Muon. They also provide detailed ablation studies to justify their design choices, such as the granularity of adaptive learning rates and the positioning of normalization. The results consistently show that NorMuon outperforms the baselines in terms of training efficiency and final performance.
- The paper addresses an important problem in deep learning optimization: how to combine the benefits of different optimizers. NorMuon provides a practical solution that integrates orthogonalization and adaptive learning rates in a way that is both effective and efficient. The authors also provide a detailed analysis of the memory and computational overhead of NorMuon, which is important for practical deployment.

### Weaknesses

#### Some Related Works


#### comment

 - The paper focuses on language modeling tasks, but it is unclear how well NorMuon would generalize to other domains, such as image classification or reinforcement learning. The authors should provide more evidence that NorMuon is effective across a range of tasks.
- The paper does not provide a detailed analysis of the convergence properties of NorMuon. While the authors show that NorMuon converges faster than AdamW and Muon, they do not provide a theoretical analysis of why this is the case. It would be helpful to understand the conditions under which NorMuon is guaranteed to converge and how its convergence rate compares to other optimizers.
- The paper does not provide a detailed analysis of the sensitivity of NorMuon to hyperparameters. While the authors show that NorMuon is robust to some hyperparameter choices, it is unclear how sensitive it is to other hyperparameters, such as the learning rate or the momentum parameters. It would be helpful to provide a more detailed analysis of the hyperparameter tuning process and to identify the optimal hyperparameter settings for different tasks.

### Suggestions

The authors should investigate the performance of NorMuon on a wider range of tasks beyond language modeling. Specifically, experiments on image classification datasets such as CIFAR-10 or ImageNet, and reinforcement learning tasks would be valuable. These tasks have different characteristics than language modeling, such as different data distributions and optimization landscapes, and would provide a more comprehensive evaluation of NorMuon's generalizability. For image classification, the authors could use standard architectures like ResNet or VGG, and for reinforcement learning, they could use OpenAI Gym environments. It would also be beneficial to analyze the behavior of NorMuon in these different settings, looking at metrics like training loss, validation accuracy, and convergence speed. This would help to identify any potential limitations of NorMuon and to guide future research.

To strengthen the theoretical analysis, the authors should explore the convergence properties of NorMuon in more detail. While the empirical results are promising, a theoretical understanding of why NorMuon converges faster than AdamW and Muon would be valuable. This could involve analyzing the optimization landscape and the behavior of the algorithm in different regions. For example, the authors could investigate the eigenvalues of the Hessian matrix and how they are affected by NorMuon's orthogonalization and adaptive learning rate mechanisms. Additionally, it would be helpful to compare the convergence rate of NorMuon to other optimizers, such as LAMB, which is known to have good convergence properties. This could involve deriving bounds on the convergence rate or conducting experiments with different learning rates and batch sizes. A more rigorous theoretical analysis would provide a deeper understanding of NorMuon's behavior and its potential limitations.

Finally, the authors should provide a more detailed analysis of the sensitivity of NorMuon to hyperparameters. While the authors show that NorMuon is robust to some hyperparameter choices, it is unclear how sensitive it is to other hyperparameters, such as the learning rate, momentum parameters, and the parameters related to the per-neuron adaptive learning rates. The authors should conduct a more systematic hyperparameter tuning process and identify the optimal hyperparameter settings for different tasks. This could involve using techniques like grid search or Bayesian optimization. It would also be helpful to analyze the impact of different hyperparameter settings on the convergence rate and the final performance of NorMuon. This would provide a more complete picture of NorMuon's behavior and help practitioners to effectively use it in different settings.

### Questions

- How does NorMuon perform on other tasks, such as image classification or reinforcement learning?
- What are the theoretical properties of NorMuon? How does it compare to other optimizers in terms of convergence rate and stability?
- How sensitive is NorMuon to hyperparameters? Are there any best practices for tuning the hyperparameters?

### Rating

8

### Confidence

4

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in the provided paper. I need to go through each reviewer's comments and check if the criticism is valid based on the content of the paper.

Plan:
1. Go through each reviewer's identified weaknesses.
2. For each weakness, find supporting evidence or counter-evidence from the paper.
3. Categorize the evidence based on whether it relates to method or experiments.
4. If the weakness is about missing information, check if that information is indeed absent.
5. Finally, conclude whether the weakness is valid, partially valid, or invalid, and provide a confidence level based on the strength of the evidence.
**Review 1 Weaknesses:**

1. Weakness Statement: The paper focuses on language modeling tasks, but it is unclear how well NorMuon would generalize to other domains, such as image classification or reinforcement learning. The authors should provide more evidence that NorMuon is effective across a range of tasks.

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper explicitly states in the "Experiments" section that they conduct experiments on "language modeling" tasks. The "Modded-NanoGPT" experiment is described as a "linear rule from prior works for scaling the architectural shape" and is also framed as a language modeling task.
   - The "Main results" section focuses on language modeling performance metrics like "validation loss" and "perplexity".
   - The "Experiments on Modded-NanoGPT" section also uses "validation loss" as the metric.

3. Literature Gap Analysis:
   - The paper does not include experiments on image classification or reinforcement learning tasks.

4. Validation Analysis:
   - The paper's experimental section is solely focused on language modeling tasks. There is no evidence presented to demonstrate NorMuon's performance on other domains like image classification or reinforcement learning.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "Experiments" section explicitly mentions and evaluates NorMuon on language modeling tasks only.

1. Weakness Statement: The paper does not provide a detailed analysis of the convergence properties of NorMuon. While the authors show that NorMuon converges faster than AdamW and Muon, they do not provide a theoretical analysis of why this is the case. It would be helpful to understand the conditions under which NorMuon is guaranteed to converge and how its convergence rate compares to other optimizers.

2. Evidence Collection:
a) Method-related Evidence:
   - The "Method" section describes the algorithm and its components but does not include any theoretical analysis of convergence.
b) Experiment-related Evidence:
   - The "Main results" section mentions that NorMuon "consistently outperforms both AdamW and Muon in terms of training efficiency and final performance" and provides training loss curves in Figure 2, showing faster convergence for NorMuon.
   - The "Ablation studies" section provides some analysis of the impact of different components on performance, but not a theoretical convergence analysis.

3. Literature Gap Analysis:
   - The paper does not cite any theoretical works that analyze the convergence properties of optimizers combining adaptive learning rates and orthogonalization.

4. Validation Analysis:
   - The paper empirically demonstrates faster convergence but lacks a theoretical analysis explaining why NorMuon achieves this. There is no discussion of conditions for convergence or a comparison of convergence rates with other optimizers from a theoretical standpoint.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "Method" section lacks theoretical analysis, and the "Main results" section only shows empirical evidence of faster convergence without theoretical backing.

1. Weakness Statement: The paper does not provide a detailed analysis of the sensitivity of NorMuon to hyperparameters. While the authors show that NorMuon is robust to some hyperparameter choices, it is unclear how sensitive it is to other hyperparameters, such as the learning rate or the momentum parameters. It would be helpful to provide a more detailed analysis of the hyperparameter tuning process and to identify the optimal hyperparameter settings for different tasks.

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "Hyperparameters" subsection in the "Experiments" section mentions the specific hyperparameters used for each experiment (AdamW, Muon, NorMuon) and the base learning rate schedule.
   - The "Ablation studies" section includes an ablation study on the granularity of adaptive learning rates and the positioning of normalization, but it doesn't systematically explore the sensitivity to other hyperparameters like learning rate or momentum.
   - The "Computational and Memory Overhead Analysis" section discusses the impact of Muon's orthogonalization but doesn't delve into hyperparameter sensitivity.

3. Literature Gap Analysis:
   - The paper doesn't cite specific methodologies for hyperparameter sensitivity analysis.

4. Validation Analysis:
   - While the paper mentions specific hyperparameters and shows some robustness to them, there isn't a dedicated section or detailed analysis exploring the sensitivity of NorMuon's performance to variations in hyperparameters like learning rate or momentum. The ablation studies focus on the granularity of adaptive learning rates and normalization position.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "Hyperparameters" section lists the used hyperparameters, but there's no systematic analysis of their sensitivity.

**Review 2 Weaknesses:**

1. Weakness Statement: The paper does not provide a detailed analysis of the computational overhead of NorMuon compared to other optimizers, such as AdamW and Muon. While the authors claim that NorMuon is more efficient, they do not provide concrete evidence to support this claim. Specifically, the paper lacks a breakdown of the time spent on each step of the algorithm, such as the computation of the orthogonalized updates and the per-neuron adaptive learning rates. This makes it difficult to assess the true computational cost of NorMuon and to understand where the performance gains come from.

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "Computational and Memory Overhead Analysis" section provides a "3% increase in training step time compared to AdamW" and a "33% increase in memory overhead compared to AdamW or Muon".
   - Table 2 provides a "Breakdown of computational and memory requirements" comparing NorMuon, AdamW, and Muon.
   - The section "Wall-Clock Performance" mentions "Figure 4 presents the validation loss as a function of wall-clock training time" and states "Despite the additional computation required for orthogonalization and neuron-wise normalization, NorMuon maintains substantial performance advantages over AdamW."

3. Literature Gap Analysis:
   - The paper does not cite specific methodologies for detailed computational overhead analysis.

4. Validation Analysis:
   - The paper provides quantitative comparisons of training step time and memory overhead between NorMuon and the baselines. It also mentions the wall-clock performance, showing NorMuon's efficiency in terms of time to reach a certain loss. However, it does not provide a detailed breakdown of the time spent on individual steps like orthogonalization and normalization.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper provides overall computational overhead metrics but lacks a granular breakdown of time spent on specific steps.

1. Weakness Statement: The paper does not provide a detailed analysis of the memory usage of NorMuon compared to other optimizers, such as AdamW and Muon. While the authors claim that NorMuon is more memory-efficient, they do not provide concrete evidence to support this claim. The paper should include a breakdown of the memory usage for each component of the algorithm, such as the momentum states, the orthogonalized updates, and the per-neuron adaptive learning rates. This would allow for a more precise comparison of the memory usage of NorMuon with other optimizers.

2. Evidence Collection:
b) Experiment-related Evidence:
   - Table 2 provides a "Breakdown of computational and memory requirements" comparing NorMuon, AdamW, and Muon. This table includes "m (first-order momentum)", "v (second-order momentum)", " NorMuon", and "AdamW", "Muon".
   - The "Computational and Memory Overhead Analysis" section explicitly states, "Table 2 provides a breakdown of the computational and memory requirements for each optimizer. NorMuon maintains Muon’s memory efficiency."

3. Literature Gap Analysis:
   - The paper does not cite specific methodologies for detailed memory usage analysis.

4. Validation Analysis:
   - The paper explicitly provides a breakdown of memory usage for NorMuon and the baselines in Table 2, directly contradicting the claim that NorMuon is not memory-efficient.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: Table 2 in the paper provides a detailed breakdown of memory usage.

1. Weakness Statement: The paper does not provide a detailed analysis of the convergence behavior of NorMuon compared to other optimizers, such as AdamW and Muon. While the authors claim that NorMuon converges faster, they do not provide concrete evidence to support this claim. The paper should include a more detailed analysis of the convergence behavior, such as the training loss and the validation loss over time. This would allow for a more precise comparison of the convergence behavior of NorMuon with other optimizers.

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "Main results" section states, " NorMuon consistently outperforms both AdamW and Muon in terms of training efficiency and final performance."
   - Figure 2 shows "Validation loss curve across different model scales" for NorMuon, AdamW, and Muon.
   - The "Ablation studies" section includes an analysis of the impact of different components on performance, implicitly relating to convergence.

3. Literature Gap Analysis:
   - The paper does not cite specific methodologies for detailed convergence analysis.

4. Validation Analysis:
   - The paper provides training loss curves in Figure 2, directly supporting the claim of faster convergence for NorMuon. The "Main results" section also explicitly states the outperformance in terms of training efficiency.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: Figure 2 presents training loss curves, and the "Main results" section explicitly claims faster convergence.

1. Weakness Statement: The paper does not provide a detailed analysis of the sensitivity of NorMuon to hyperparameters, such as the learning rate and the momentum parameters. While the authors claim that NorMuon is less sensitive to hyperparameters, they do not provide concrete evidence to support this claim. The paper should include a more detailed analysis of the sensitivity of NorMuon to hyperparameters, such as the learning rate, the momentum parameters, and the per-neuron adaptive learning rates. This would help to identify the optimal parameter settings for NorMuon and to understand the trade-offs between convergence speed and final performance.

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "Hyperparameters" subsection lists the specific hyperparameters used.
   - The "Ablation studies" section includes an ablation study on the granularity of adaptive learning rates and the positioning of normalization, but not a systematic sensitivity analysis of learning rate or momentum.

3. Literature Gap Analysis:
   - The paper doesn't cite specific methodologies for hyperparameter sensitivity analysis.

4. Validation Analysis:
   - Similar to Reviewer 1, this reviewer points out the lack of a systematic analysis of hyperparameter sensitivity. While the paper shows some robustness, it doesn't provide a detailed analysis of how NorMuon's performance changes with different hyperparameter settings.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks a dedicated section or detailed analysis exploring the sensitivity of NorMuon's performance to variations in hyperparameters like learning rate or momentum.

**Review 3 Weaknesses:**

1. Weakness Statement: The paper does not provide a detailed analysis of the computational cost of NorMuon compared to other optimizers, such as AdamW and Muon. While the authors claim that NorMuon is more efficient, they do not provide concrete evidence to support this claim. Specifically, the paper lacks a breakdown of the FLOPs required for each optimizer during training, including the cost of the orthogonalization step in Muon and the per-neuron adaptive learning rates in NorMuon. This makes it difficult to assess the true computational cost of NorMuon and to understand where the performance gains come from.

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "Computational and Memory Overhead Analysis" section provides a "3% increase in training step time compared to AdamW" and a "33% increase in memory overhead compared to AdamW or Muon".
   - Table 2 provides a "Breakdown of computational and memory requirements" comparing NorMuon, AdamW, and Muon.
   - The section "Wall-Clock Performance" mentions "Despite the additional computation required for orthogonalization and neuron-wise normalization, NorMuon maintains substantial performance advantages over AdamW."

3. Literature Gap Analysis:
   - The paper does not cite specific methodologies for detailed computational cost analysis.

4. Validation Analysis:
   - Similar to Reviewer 2, this reviewer notes the lack of a detailed computational cost analysis, specifically mentioning the absence of FLOPs breakdown. However, the paper does provide overall training step time and memory overhead comparisons.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper provides overall computational overhead metrics but lacks a granular breakdown of FLOPs for each step.

1. Weakness Statement: The paper does not provide a detailed analysis of the memory usage of NorMuon compared to other optimizers, such as AdamW and Muon. While the authors claim that NorMuon is more memory-efficient, they do not provide concrete evidence to support this claim. The paper should include a breakdown of the memory usage for each component of the algorithm, such as the momentum states, the orthogonalized updates, and the per-neuron adaptive learning rates. This would allow for a more precise comparison of the memory usage of NorMuon with other optimizers.

2. Evidence Collection:
b) Experiment-related Evidence:
   - Table 2 provides a "Breakdown of computational and memory requirements" comparing NorMuon, AdamW, and Muon. This table includes "m (first-order momentum)", "v (second-order momentum)", " NorMuon", and "AdamW", "Muon".
   - The "Computational and Memory Overhead Analysis" section explicitly states, "Table 2 provides a breakdown of the computational and memory requirements for each optimizer. NorMuon maintains Muon’s memory efficiency."

3. Literature Gap Analysis:
   - The paper does not cite specific methodologies for detailed memory usage analysis.

4. Validation Analysis:
   - This is the same point raised by Reviewer 2 regarding memory usage. The paper explicitly provides a breakdown of memory usage in Table 2.

5. Conclusion:
   - Validity status: Invalid
   - Confidence level: High
   - Key supporting evidence: Table 2 in the paper provides a detailed breakdown of memory usage.

1. Weakness Statement: To strengthen the claims regarding convergence, the authors should provide a more detailed analysis of the convergence behavior of NorMuon compared to other optimizers, such as AdamW and Muon. This analysis should include the training loss and the validation loss over time, as well as the convergence rate and the final performance. The authors should also investigate the impact of different hyperparameters on the convergence behavior of each optimizer, including the learning rate, the momentum parameters, and the parameters related to the per-neuron adaptive learning rates. This would help to identify the optimal parameter settings for each optimizer and to understand the trade-offs between convergence speed and final performance.

2. Evidence Collection:
b) Experiment-related Evidence:
   - Figure 2 shows the "Validation loss curve across different model scales" for NorMuon, AdamW, and Muon.
   - The "Main results" section states, " NorMuon consistently outperforms both AdamW and Muon in terms of training efficiency and final performance."
   - The "Ablation studies" section includes an analysis of the impact of different components on performance.

3. Literature Gap Analysis:
   - The paper does not cite specific methodologies for detailed convergence analysis.

4. Validation Analysis:
   - Similar to the previous points, this reviewer reiterates the need for a more detailed convergence analysis, including the impact of hyperparameters. The paper does provide training loss curves and claims outperformance, but lacks a deeper dive into the convergence rate and hyperparameter sensitivity.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper provides training loss curves but lacks a detailed analysis of convergence rate and hyperparameter impact on convergence.

1. Weakness Statement: Finally, the paper should include a more thorough investigation of the scalability of NorMuon to larger models and datasets. This should include experiments with models that have significantly more parameters than those used in the current study, as well as experiments with datasets that are larger in size and more diverse in nature. The authors should also analyze the scaling behavior of NorMuon with respect to model size and dataset size, including the computational cost and memory usage as a function of these parameters. This analysis should be conducted using a range of hardware configurations to assess the scalability of NorMuon in different computing environments. Furthermore, the authors should compare the performance of NorMuon on larger models and datasets to the performance of AdamW and Muon, to determine whether NorMuon maintains its advantages in more challenging scenarios. This would provide a more comprehensive understanding of the practical applicability of NorMuon in real-world applications.

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "Experiments on 1.1B and 5.4B Models" section presents results for models with 1.1B and 5.4B parameters.
   - The "Modded-NanoGPT" experiment uses a 124M parameter model.
   - The paper does not explicitly analyze the scaling behavior as a function of model size and dataset size, nor does it vary hardware configurations systematically.

3. Literature Gap Analysis:
   - The paper does not cite specific methodologies for scalability analysis.

4. Validation Analysis:
   - While the paper includes experiments on models larger than the base 124M, it doesn't provide a systematic analysis of how NorMuon's performance scales with increasing model size and dataset size, nor does it analyze the computational cost and memory usage as a function of these parameters.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks a systematic analysis of NorMuon's scalability with respect to model and dataset size, including computational cost and memory usage.

**Review 4 Weaknesses:**

1. Weakness Statement: The paper focuses on language modeling tasks, but it is unclear how well NorMuon would generalize to other domains, such as image classification or reinforcement learning. The authors should provide more evidence that NorMuon is effective across a range of tasks.

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper explicitly states in the "Experiments" section that they conduct experiments on "language modeling" tasks. The "Modded-NanoGPT" experiment is described as a "linear rule from prior works for scaling the architectural shape" and is also framed as a language modeling task.
   - The "Main results" section focuses on language modeling performance metrics like "validation loss" and "perplexity".
   - The "Experiments on Modded-NanoGPT" section also uses "validation loss" as the metric.

3. Literature Gap Analysis:
   - The paper does not include experiments on image classification or reinforcement learning tasks.

4. Validation Analysis:
   - The paper's experimental section is solely focused on language modeling tasks. There is no evidence presented to demonstrate NorMuon's performance on other domains like image classification or reinforcement learning.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "Experiments" section explicitly mentions and evaluates NorMuon on language modeling tasks only.

1. Weakness Statement: The paper does not provide a detailed analysis of the convergence properties of NorMuon. While the authors show that NorMuon converges faster than AdamW and Muon, they do not provide a theoretical analysis of why this is the case. It would be helpful to understand the conditions under which NorMuon is guaranteed to converge and how its convergence rate compares to other optimizers.

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "Main results" section mentions that NorMuon "consistently outperforms both AdamW and Muon in terms of training efficiency and final performance" and provides training loss curves in Figure 2, showing faster convergence for NorMuon.
   - The "Ablation studies" section provides some analysis of the impact of different components on performance, but not a theoretical convergence analysis.

3. Literature Gap Analysis:
   - The paper does not cite any theoretical works that analyze the convergence properties of optimizers combining adaptive learning rates and orthogonalization.

4. Validation Analysis:
   - The paper empirically demonstrates faster convergence but lacks a theoretical analysis explaining why NorMuon achieves this. There is no discussion of conditions for convergence or a comparison of convergence rates with other optimizers from a theoretical standpoint.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "Method" section lacks theoretical analysis, and the "Main results" section only shows empirical evidence of faster convergence without theoretical backing.

1. Weakness Statement: The paper does not provide a detailed analysis of the sensitivity of NorMuon to hyperparameters. While the authors show that NorMuon is robust to some hyperparameter choices, it is unclear how sensitive it is to other hyperparameters, such as the learning rate or the momentum parameters. It would be helpful to provide a more detailed analysis of the hyperparameter tuning process and to identify the optimal hyperparameter settings for different tasks.

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "Hyperparameters" subsection in the "Experiments" section mentions the specific hyperparameters used for each experiment (AdamW, Muon, NorMuon) and the base learning rate schedule.
   - The "Ablation studies" section includes an ablation study on the granularity of adaptive learning rates and the positioning of normalization, but it doesn't systematically explore the sensitivity to other hyperparameters like learning rate or momentum.
   - The "Computational and Memory Overhead Analysis" section discusses the impact of Muon's orthogonalization but doesn't delve into hyperparameter sensitivity.

3. Literature Gap Analysis:
   - The paper doesn't cite specific methodologies for hyperparameter sensitivity analysis.

4. Validation Analysis:
   - Similar to Reviewer 1 and 2, this reviewer points out the lack of a systematic analysis of hyperparameter sensitivity. While the paper shows some robustness, it doesn't provide a detailed analysis of how NorMuon's performance changes with different hyperparameter settings.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The "Hyperparameters" section lists the used hyperparameters, but there's no systematic analysis of their sensitivity.

**Synthesis and Reflection:**

Several reviewers independently identified similar weaknesses, indicating a strong consensus on these issues. The most prominent recurring themes are:

*   **Lack of Generalization Evidence:** Reviewers 1 and 4 both pointed out the exclusive focus on language modeling tasks, raising concerns about NorMuon's performance in other domains.
*   **Insufficient Theoretical Analysis:** Reviewers 1 and 4 highlighted the absence of a detailed theoretical analysis of NorMuon's convergence properties and the conditions for convergence.
*   **Limited Hyperparameter Sensitivity Analysis:** Reviewers 1, 2, and 4 all noted the lack of a systematic investigation into how NorMuon's performance is affected by different hyperparameter settings.

There was a minor conflict in the interpretation of the computational overhead analysis. Reviewer 2 found the analysis insufficient, while Reviewer 3 acknowledged the provided comparisons but suggested a need for a more granular breakdown (FLOPs). However, both agree that the paper provides *some* analysis of computational cost, just not in the level of detail Reviewer 2 expected.

The memory usage analysis was consistently found to be invalid, as Table 2 in the paper provides the necessary breakdown.

The convergence analysis was also a point of contention. Reviewer 3 and 4 felt the analysis was insufficient, while Reviewer 2 acknowledged the training loss curves but suggested a need for a more detailed analysis of convergence rate and hyperparameter impact. Again, this highlights a difference in the depth of analysis expected.

**Conclusion:**

The majority of the identified weaknesses are valid and supported by the paper's content. The key areas for improvement are:

1. **Expanding Experimental Evaluation:** Include experiments on diverse tasks beyond language modeling.
2. **Strengthening Theoretical Analysis:** Provide a theoretical justification for NorMuon's convergence properties.
3. **Conducting Detailed Hyperparameter Analysis:** Systematically explore the sensitivity of NorMuon to various hyperparameters.

The criticism regarding memory usage is invalid, and the criticism regarding computational overhead is partially valid, depending on the level of granularity desired.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces NorMuon, a novel optimization algorithm designed to enhance the training efficiency of large language models. The core idea behind NorMuon is to integrate the strengths of two existing approaches: Muon, which employs orthogonalization to improve the conditioning of update directions, and AdamW, which uses per-parameter adaptive learning rates. NorMuon achieves this by maintaining both second-order momentum statistics, similar to AdamW, and row-wise normalization statistics after orthogonalization, akin to Muon. This combination aims to address the imbalance in condition numbers across the network, which can hinder the effectiveness of standard optimizers. The authors develop a distributed implementation of NorMuon compatible with the FSDP2 framework, enabling efficient training of large models. The empirical evaluation of NorMuon is conducted across a range of model scales, from 124 million to 5.4 billion parameters, and on various tasks, including language modeling and image classification (Modded-NanoGPT). The results consistently demonstrate that NorMuon outperforms both AdamW and Muon in terms of training efficiency and final performance. Specifically, NorMuon achieves faster training convergence and better final performance, while maintaining a comparable memory footprint to Muon. The authors also provide ablation studies to justify their design choices, such as the granularity of adaptive learning rates and the positioning of normalization. The paper also includes a detailed analysis of the computational and memory overhead of NorMuon compared to AdamW and Muon, showing that NorMuon has a small increase in computational cost but maintains the same memory footprint as Muon. Overall, the paper presents a well-motivated and empirically validated approach to combining orthogonalization and adaptive learning rates, offering a practical solution for training large language models. The authors provide a clear and well-structured presentation of their method, making it accessible to a broad audience. The empirical results are compelling, demonstrating the effectiveness of NorMuon across a range of model scales and tasks. The distributed implementation of NorMuon is also a significant contribution, enabling the practical application of the method to large-scale models. While the paper has some limitations, as I will discuss in the following sections, it makes a valuable contribution to the field of optimization for deep learning.


## Soundness:

2.75


## Presentation:

3.0


## Contribution:

2.75


## Strengths:

The paper's primary strength lies in its clear and well-structured presentation of the NorMuon algorithm. The authors effectively articulate the motivation behind NorMuon, highlighting the limitations of existing optimizers and the potential benefits of combining orthogonalization and adaptive learning rates. The method itself is technically sound, with a clear description of the algorithm and its implementation. The integration of second-order momentum statistics, similar to AdamW, and row-wise normalization statistics after orthogonalization, similar to Muon, is a novel approach that addresses the imbalance in condition numbers across the network. The empirical evaluation of NorMuon is another significant strength of the paper. The authors conduct experiments across a range of model scales and tasks, demonstrating the effectiveness of NorMuon in various settings. The results consistently show that NorMuon outperforms both AdamW and Muon in terms of training efficiency and final performance. The inclusion of ablation studies further strengthens the empirical findings, justifying the design choices made in the algorithm. The authors also provide a detailed analysis of the computational and memory overhead of NorMuon compared to AdamW and Muon, showing that NorMuon has a small increase in computational cost but maintains the same memory footprint as Muon. This is a crucial aspect of the paper, as it demonstrates the practical applicability of NorMuon for training large models. The distributed implementation of NorMuon is another significant contribution. The authors develop an efficient distributed implementation compatible with the FSDP2 framework, enabling the practical application of the method to large-scale models. This is an important step towards making NorMuon a widely used optimization algorithm. The paper also addresses an important problem in deep learning optimization: how to combine the benefits of different optimizers. NorMuon provides a practical solution that integrates orthogonalization and adaptive learning rates in a way that is both effective and efficient. The authors also provide a detailed analysis of the memory and computational overhead of NorMuon, which is important for practical deployment. The paper is well-written and easy to follow, with clear explanations of the algorithm and the experimental setup. The figures and tables are well-designed and effectively communicate the key results. The authors also provide a detailed description of the experimental setup, including the hyperparameters used for each experiment. This makes it easy for other researchers to reproduce the results and build upon the work presented in the paper. Overall, the paper makes a valuable contribution to the field of optimization for deep learning, and the NorMuon algorithm is a promising approach for training large language models.


## Weaknesses:

While the paper presents a compelling approach to optimization, several weaknesses need to be addressed. First, the paper's experimental evaluation is primarily focused on language modeling tasks, with the Modded-NanoGPT experiment also framed as a language modeling task. As I verified, the paper explicitly states that the experiments are conducted on language modeling tasks, and the metrics used, such as validation loss and perplexity, are standard for language modeling. This lack of evaluation on other domains, such as image classification or reinforcement learning, raises concerns about the generalizability of NorMuon. The paper does not provide any evidence that NorMuon would perform well on tasks with different characteristics than language modeling, such as different data distributions and optimization landscapes. This is a significant limitation, as it is unclear whether NorMuon would be suitable for a wide range of applications. My confidence in this limitation is high, as the paper explicitly states the focus on language modeling tasks and does not include any results on other domains. Second, the paper lacks a detailed theoretical analysis of NorMuon's convergence properties. While the empirical results show that NorMuon converges faster than AdamW and Muon, the paper does not provide a theoretical explanation for why this is the case. The paper does not cite any theoretical works that analyze the convergence properties of optimizers combining adaptive learning rates and orthogonalization. This lack of theoretical analysis is a significant weakness, as it is unclear under what conditions NorMuon is guaranteed to converge and how its convergence rate compares to other optimizers from a theoretical standpoint. My confidence in this limitation is high, as the paper does not include any theoretical analysis of convergence. Third, the paper does not provide a detailed analysis of the sensitivity of NorMuon to hyperparameters. While the authors show that NorMuon is robust to some hyperparameter choices, it is unclear how sensitive it is to other hyperparameters, such as the learning rate, momentum parameters, and the parameters related to the per-neuron adaptive learning rates. The paper does not include a systematic hyperparameter tuning process or identify the optimal hyperparameter settings for different tasks. This lack of sensitivity analysis is a significant weakness, as it is unclear how to best tune NorMuon for different applications. My confidence in this limitation is high, as the paper does not include any systematic analysis of hyperparameter sensitivity. Fourth, while the paper provides some analysis of the computational overhead of NorMuon, it lacks a detailed breakdown of the time spent on each step of the algorithm, such as the computation of the orthogonalized updates and the per-neuron adaptive learning rates. The paper claims that NorMuon is more efficient than AdamW and Muon, but it does not provide a detailed analysis of the computational cost of each step. This makes it difficult to assess the true computational cost of NorMuon and to understand where the performance gains come from. My confidence in this limitation is medium, as the paper provides overall computational overhead metrics but lacks a granular breakdown of FLOPs for each step. Finally, while the paper provides a breakdown of memory usage for NorMuon, AdamW, and Muon in Table 2, the paper does not include a detailed analysis of the memory usage of NorMuon compared to other optimizers, such as LAMB. This is a minor weakness, as the paper does provide some information on memory usage, but it could be more detailed. My confidence in this limitation is medium, as the paper does provide some information on memory usage, but it could be more detailed.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should expand the experimental evaluation of NorMuon to include a wider range of tasks beyond language modeling. Specifically, experiments on image classification datasets such as CIFAR-10 or ImageNet, and reinforcement learning tasks would be valuable. These tasks have different characteristics than language modeling, such as different data distributions and optimization landscapes, and would provide a more comprehensive evaluation of NorMuon's generalizability. For image classification, the authors could use standard architectures like ResNet or VGG, and for reinforcement learning, they could use OpenAI Gym environments. It would also be beneficial to analyze the behavior of NorMuon in these different settings, looking at metrics like training loss, validation accuracy, and convergence speed. This would help to identify any potential limitations of NorMuon and to guide future research. Second, the authors should provide a more detailed theoretical analysis of NorMuon's convergence properties. This could involve analyzing the optimization landscape and the behavior of the algorithm in different regions. For example, the authors could investigate the eigenvalues of the Hessian matrix and how they are affected by NorMuon's orthogonalization and adaptive learning rate mechanisms. Additionally, it would be helpful to compare the convergence rate of NorMuon to other optimizers, such as LAMB, which is known to have good convergence properties. This could involve deriving bounds on the convergence rate or conducting experiments with different learning rates and batch sizes. A more rigorous theoretical analysis would provide a deeper understanding of NorMuon's behavior and its potential limitations. Third, the authors should provide a more detailed analysis of the sensitivity of NorMuon to hyperparameters. This could involve using techniques like grid search or Bayesian optimization to identify the optimal hyperparameter settings for different tasks. It would also be helpful to analyze the impact of different hyperparameter settings on the convergence rate and the final performance of NorMuon. This would provide a more complete picture of NorMuon's behavior and help practitioners to effectively use it in different settings. Fourth, the authors should provide a more detailed analysis of the computational cost of NorMuon, including a breakdown of the FLOPs required for each step of the algorithm, such as the computation of the orthogonalized updates and the per-neuron adaptive learning rates. This analysis should be conducted on different hardware configurations and with different model sizes to understand how the computational cost scales. Furthermore, the authors should quantify the memory overhead associated with maintaining the second-order momentum and per-neuron adaptive learning rates for NorMuon, and compare this to the memory footprint of AdamW and Muon. This would provide a more precise understanding of the computational trade-offs of NorMuon. Finally, the authors should provide a more detailed analysis of the memory usage of NorMuon compared to other optimizers, such as LAMB. This analysis should include a breakdown of the memory usage for each component of the algorithm, such as the momentum states, the orthogonalized updates, and the per-neuron adaptive learning rates. This would allow for a more precise comparison of the memory usage of NorMuon with other optimizers.


## Questions:

Based on my analysis, I have several questions that I believe are important for further understanding the NorMuon algorithm. First, how does NorMuon perform on other tasks, such as image classification or reinforcement learning? The paper's experimental evaluation is primarily focused on language modeling, and it is unclear whether NorMuon would generalize to other domains. I would like to see more evidence that NorMuon is effective across a range of tasks. Second, what are the theoretical properties of NorMuon? How does it compare to other optimizers in terms of convergence rate and stability? The paper lacks a detailed theoretical analysis of NorMuon's convergence properties, and I would like to understand the conditions under which NorMuon is guaranteed to converge and how its convergence rate compares to other optimizers. Third, how sensitive is NorMuon to hyperparameters? Are there any best practices for tuning the hyperparameters? The paper does not provide a systematic analysis of hyperparameter sensitivity, and I would like to understand how to best tune NorMuon for different applications. Fourth, can the authors provide more details on the computational overhead of NorMuon compared to other optimizers, such as AdamW and Muon? The paper provides some overall computational overhead metrics, but I would like to see a more detailed breakdown of the FLOPs required for each step of the algorithm. Finally, what is the memory usage of NorMuon compared to other optimizers, such as LAMB? The paper provides some information on memory usage, but I would like to see a more detailed comparison of the memory footprint of NorMuon with other optimizers. These questions are important for understanding the practical applicability of NorMuon and for guiding future research in this area.


## Rating:

6.25


## Confidence:

3.5


## Decision:

Accept
}