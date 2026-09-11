I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper addresses the generalization problem in supervised fine-tuning (SFT) for large language models (LLMs) by analyzing the connection between SFT and reinforcement learning (RL). The authors find that SFT implicitly uses a problem-specific reward structure that may hinder generalization. To tackle this, they propose Dynamic Fine-Tuning (DFT), which reweights the SFT objective at each token by its probability, dynamically adjusting the learning focus. DFT is tested across various tasks, including mathematical reasoning, code generation, and multi-modal reasoning, showing improved generalization and performance over standard SFT.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper provides a novel perspective on understanding SFT through the lens of RL, offering a fresh theoretical insight into the limitations of standard SFT.
2. DFT is straightforward to implement, requiring only a single-line change to the SFT loss, yet it yields significant performance improvements across various tasks.
3. The method is tested across multiple domains, including mathematical reasoning, code generation, and multi-modal reasoning, demonstrating its broad applicability and effectiveness.
4. DFT shows competitive results in offline RL settings, suggesting its potential as a versatile fine-tuning strategy.

### Weaknesses

#### Some Related Works


#### comment

1. While the paper provides theoretical insights, the empirical evaluation could be more extensive. Specifically, the paper lacks a thorough analysis of the sensitivity of DFT to its hyperparameters, such as the reweighting factor. A more detailed exploration of how these parameters affect performance across different tasks would strengthen the claims of robustness. Furthermore, the evaluation could benefit from a more diverse set of datasets, particularly those that are more challenging or domain-specific, to fully assess the generalizability of DFT.
2. The paper could benefit from a more detailed comparison with other advanced fine-tuning techniques, such as those that incorporate adaptive learning rates or more sophisticated reward structures. A direct comparison with methods like these would help clarify DFT's unique advantages and limitations. The current comparison is limited to standard SFT and a few basic RL methods, which does not fully contextualize DFT's performance within the broader landscape of fine-tuning approaches. A more comprehensive comparison would include methods that explicitly address generalization, such as those using meta-learning or domain adaptation techniques.
3. The paper does not delve deeply into the computational overhead of DFT compared to standard SFT. While the method is described as straightforward, a detailed analysis of training time, memory usage, and inference costs would be valuable for practical applications. The paper should provide a quantitative comparison of these factors, especially when scaling to larger models and datasets. This is crucial for understanding the practical trade-offs of using DFT in resource-constrained environments.

### Suggestions

To address the limitations in the empirical evaluation, the authors should conduct a more thorough sensitivity analysis of the DFT hyperparameters. This should include a systematic exploration of how different reweighting factors impact performance across various tasks and datasets. For example, the authors could perform a grid search over a range of reweighting values and report the resulting performance metrics, such as accuracy or F1 score. This analysis should also include a discussion of the optimal hyperparameter settings for different types of tasks and datasets. Furthermore, the authors should expand the evaluation to include a more diverse set of datasets, particularly those that are more challenging or domain-specific. This would provide a more robust assessment of the generalizability of DFT. For instance, the authors could include datasets from specialized domains such as medicine, law, or finance, which would test the method's ability to handle diverse data distributions and task requirements. This would also help to identify potential limitations of DFT in specific domains.

To better contextualize DFT's performance, the authors should include a more detailed comparison with other advanced fine-tuning techniques. This comparison should include methods that explicitly address generalization, such as those using meta-learning or domain adaptation techniques. For example, the authors could compare DFT with methods like MAML or domain-adaptive training, which are designed to improve generalization across different tasks or domains. This comparison should not only focus on performance metrics but also on computational costs and implementation complexity. The authors should also consider comparing DFT with methods that incorporate adaptive learning rates or more sophisticated reward structures. This would help to clarify DFT's unique advantages and limitations in the broader landscape of fine-tuning approaches. The comparison should include a discussion of the trade-offs between different methods, such as performance gains versus computational overhead.

Finally, the authors should provide a more detailed analysis of the computational overhead of DFT compared to standard SFT. This analysis should include a quantitative comparison of training time, memory usage, and inference costs. The authors should also discuss the scalability of DFT when scaling to larger models and datasets. For example, the authors could report the training time per epoch and the memory footprint of DFT compared to standard SFT for different model sizes and dataset sizes. This analysis should also include a discussion of the potential bottlenecks in DFT and how they can be addressed. This would provide a more complete understanding of the practical trade-offs of using DFT in resource-constrained environments.

### Questions

1. How does DFT perform on tasks with sparse rewards, and how does it compare to other methods designed for such environments?
2. Can the authors provide more insights into the theoretical underpinnings of why DFT improves generalization in SFT?
3. What are the limitations of DFT, and in which scenarios might it not be the most effective approach?

### Rating

6

### Confidence

4

**********

## Reviewer 2

### Summary

This paper proposes a simple yet effective method, Dynamic Fine-Tuning (DFT), to enhance the generalization capabilities of large language models (LLMs) in Supervised Fine-Tuning (SFT) tasks. The authors begin by analyzing the connection between SFT and reinforcement learning (RL), identifying the sparse reward structure and inverse-probability weighting inherent in SFT. Building on this analysis, they introduce DFT, which dynamically reweights the SFT objective at each token by its probability, effectively addressing the issues of sparse rewards and biased gradients. The paper demonstrates that DFT consistently outperforms standard SFT across various tasks, including mathematical reasoning, code generation, and multi-modal reasoning, and shows competitive results in offline RL settings.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-structured and clearly written, making it easy to follow and understand. The authors provide a comprehensive analysis of the limitations of SFT and effectively motivate the need for DFT. The theoretical framework is well-developed, and the experimental results are presented in a clear and organized manner.

2. The proposed DFT method is simple and easy to implement, requiring only a single-line modification to the SFT loss function. This simplicity makes it a practical and accessible solution for researchers and practitioners looking to improve the generalization capabilities of LLMs.

3. The paper provides extensive empirical evidence to support the effectiveness of DFT. The authors conduct experiments across multiple tasks and models, demonstrating consistent improvements in performance and generalization. The results are well-organized and clearly presented, making it easy to assess the impact of DFT.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on empirical results and lacks a deep theoretical analysis of why DFT outperforms standard SFT. While the authors provide an intuitive explanation based on the sparse reward structure and inverse-probability weighting in SFT, a more rigorous theoretical analysis would strengthen the paper's contribution. Specifically, the paper does not delve into the convergence properties of DFT, or how the dynamic reweighting affects the optimization landscape compared to standard SFT. A more formal analysis of the gradient behavior and its impact on the training dynamics would be beneficial.

2. The paper does not explore the limitations of DFT in detail. While the authors mention that DFT may not be universally beneficial across all scenarios, a more thorough analysis of the scenarios where DFT might fail or underperform would be valuable. For example, it would be useful to investigate the performance of DFT on tasks with very sparse reward signals or in domains where the model's initial knowledge is highly lacking. The paper should also discuss the potential for DFT to introduce instability or oscillations during training, and how these issues might be mitigated.

3. The paper does not provide a detailed analysis of the computational overhead of DFT. While the authors mention that DFT is simple to implement, they do not discuss the computational cost of the dynamic reweighting process, especially for large models and datasets. A comparison of the training time and memory requirements of DFT with standard SFT would be helpful for practitioners who are considering adopting this method. The analysis should also consider the impact of the reweighting on the gradient variance and how this might affect the overall training efficiency.

### Suggestions

To strengthen the theoretical foundation of the paper, the authors should provide a more in-depth analysis of the convergence properties of DFT. This could involve deriving bounds on the convergence rate or analyzing the stability of the optimization process. Specifically, the authors could investigate how the dynamic reweighting affects the gradient norm and the curvature of the loss landscape. Furthermore, it would be beneficial to explore the relationship between the reweighting factor and the generalization performance, potentially through a theoretical analysis or empirical study. This would provide a more rigorous understanding of why DFT works and under what conditions it is most effective. The authors could also consider exploring connections to existing theoretical frameworks in reinforcement learning or optimization theory to provide a more solid theoretical basis for their method.

To address the limitations of DFT, the authors should conduct a more comprehensive empirical evaluation across a wider range of tasks and datasets. This should include tasks with varying degrees of reward sparsity, different types of input data, and different levels of model knowledge. For example, the authors could evaluate DFT on tasks with very sparse reward signals, such as those found in complex reasoning or planning problems. They could also investigate the performance of DFT on tasks where the model's initial knowledge is highly lacking, such as in low-resource languages or specialized domains. Additionally, the authors should analyze the sensitivity of DFT to hyperparameter settings and provide guidelines for selecting appropriate values. This would help practitioners to effectively apply DFT in different scenarios. The authors should also investigate the potential for DFT to introduce instability or oscillations during training, and how these issues might be mitigated.

Finally, the authors should provide a more detailed analysis of the computational overhead of DFT. This should include a comparison of the training time and memory requirements of DFT with standard SFT, as well as an analysis of the impact of the reweighting on the gradient variance. The authors could also explore techniques for reducing the computational cost of DFT, such as using approximations or heuristics for the dynamic reweighting process. This would make DFT more practical for large-scale applications. The authors should also discuss the scalability of DFT to larger models and datasets, and provide insights into how the computational cost might be managed in these scenarios. This analysis should be supported by empirical results and should provide clear guidance for practitioners who are considering adopting DFT.

### Questions

1. Could the authors provide a more detailed theoretical analysis of why DFT outperforms standard SFT? Specifically, how does the dynamic reweighting affect the convergence properties and generalization performance of the model?

2. What are the limitations of DFT, and in which scenarios might it not be the most effective approach? Could the authors provide more insights into the potential failure cases of DFT?

3. What is the computational overhead of DFT compared to standard SFT? How does the dynamic reweighting process affect the training time and memory requirements, especially for large models and datasets?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper proposes a simple yet effective method, Dynamic Fine-Tuning (DFT), to improve the generalization capabilities of supervised fine-tuning (SFT) for large language models (LLMs). The authors identify the sparse reward structure and inverse-probability weighting inherent in SFT, which can hinder generalization. They then propose DFT, which dynamically reweights the SFT objective at each token by its probability, effectively addressing these issues. The paper demonstrates that DFT consistently outperforms standard SFT across various tasks, including mathematical reasoning, code generation, and multi-modal reasoning, and shows competitive results in offline RL settings.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper provides a novel perspective on understanding SFT through the lens of RL, offering a fresh theoretical insight into the limitations of standard SFT.
2. DFT is straightforward to implement, requiring only a single-line change to the SFT loss, yet it yields significant performance improvements across various tasks.
3. The method is tested across multiple domains, including mathematical reasoning, code generation, and multi-modal reasoning, demonstrating its broad applicability and effectiveness.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on empirical results and lacks a deep theoretical analysis of why DFT outperforms standard SFT. While the authors provide an intuitive explanation based on the sparse reward structure and inverse-probability weighting in SFT, a more rigorous theoretical analysis would strengthen the paper's contribution. Specifically, the paper does not explore the convergence properties of DFT, or how the dynamic reweighting affects the optimization landscape compared to standard SFT. A more formal analysis of the gradient behavior and its impact on the training dynamics would be beneficial.
2. The paper does not explore the limitations of DFT in detail. While the authors mention that DFT may not be universally beneficial across all scenarios, a more thorough analysis of the scenarios where DFT might fail or underperform would be valuable. For example, it would be useful to investigate the performance of DFT on tasks with very sparse reward signals or in domains where the model's initial knowledge is highly lacking. The paper should also discuss the potential for DFT to introduce instability or oscillations during training, and how these issues might be mitigated.
3. The paper does not provide a detailed analysis of the computational overhead of DFT. While the authors mention that DFT is simple to implement, they do not discuss the computational cost of the dynamic reweighting process, especially for large models and datasets. A comparison of the training time and memory requirements of DFT with standard SFT would be helpful for practitioners who are considering adopting this method. The analysis should also consider the impact of the reweighting on the gradient variance and how this might affect the overall training efficiency.

### Suggestions

To strengthen the theoretical foundation of the paper, the authors should provide a more in-depth analysis of the convergence properties of DFT. This could involve deriving bounds on the convergence rate or analyzing the stability of the optimization process. Specifically, the authors could investigate how the dynamic reweighting affects the gradient norm and the curvature of the loss landscape. Furthermore, it would be beneficial to explore the relationship between the reweighting factor and the generalization performance, potentially through a theoretical analysis or empirical study. This would provide a more rigorous understanding of why DFT works and under what conditions it is most effective. The authors could also consider exploring connections to existing theoretical frameworks in reinforcement learning or optimization theory to provide a more solid theoretical basis for their method.

To address the limitations of DFT, the authors should conduct a more comprehensive empirical evaluation across a wider range of tasks and datasets. This should include tasks with varying degrees of reward sparsity, different types of input data, and different levels of model knowledge. For example, the authors could evaluate DFT on tasks with very sparse reward signals, such as those found in complex reasoning or planning problems. They could also investigate the performance of DFT on tasks where the model's initial knowledge is highly lacking, such as in low-resource languages or specialized domains. Additionally, the authors should analyze the sensitivity of DFT to hyperparameter settings and provide guidelines for selecting appropriate values. This would help practitioners to effectively apply DFT in different scenarios. The authors should also investigate the potential for DFT to introduce instability or oscillations during training, and how these issues might be mitigated.

Finally, the authors should provide a more detailed analysis of the computational overhead of DFT. This should include a comparison of the training time and memory requirements of DFT with standard SFT, as well as an analysis of the impact of the reweighting on the gradient variance. The authors could also explore techniques for reducing the computational cost of DFT, such as using approximations or heuristics for the dynamic reweighting process. This would make DFT more practical for large-scale applications. The authors should also discuss the scalability of DFT to larger models and datasets, and provide insights into how the computational cost might be managed in these scenarios. This analysis should be supported by empirical results and should provide clear guidance for practitioners who are considering adopting DFT.

### Questions

1. Could the authors provide a more detailed theoretical analysis of why DFT outperforms standard SFT? Specifically, how does the dynamic reweighting affect the convergence properties and generalization performance of the model?
2. What are the limitations of DFT, and in which scenarios might it not be the most effective approach? Could the authors provide more insights into the potential failure cases of DFT?
3. What is the computational overhead of DFT compared to standard SFT? How does the dynamic reweighting process affect the training time and memory requirements, especially for large models and datasets?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

This paper proposes a simple yet effective method, Dynamic Fine-Tuning (DFT), to improve the generalization capabilities of supervised fine-tuning (SFT) for large language models (LLMs). The authors identify the sparse reward structure and inverse-probability weighting inherent in SFT, which can hinder generalization. They then propose DFT, which dynamically reweights the SFT objective at each token by its probability, effectively addressing these issues. The paper demonstrates that DFT consistently outperforms standard SFT across various tasks, including mathematical reasoning, code generation, and multi-modal reasoning, and shows competitive results in offline RL settings.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-structured and clearly written, making it easy to follow and understand. The authors provide a comprehensive analysis of the limitations of SFT and effectively motivate the need for DFT. The theoretical framework is well-developed, and the experimental results are presented in a clear and organized manner.
2. The proposed DFT method is simple and easy to implement, requiring only a single-line modification to the SFT loss function. This simplicity makes it a practical and accessible solution for researchers and practitioners looking to improve the generalization capabilities of LLMs.
3. The paper provides extensive empirical evidence to support the effectiveness of DFT. The authors conduct experiments across multiple tasks and models, demonstrating consistent improvements in performance and generalization. The results are well-organized and clearly presented, making it easy to assess the impact of DFT.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on empirical results and lacks a deep theoretical analysis of why DFT outperforms standard SFT. While the authors provide an intuitive explanation based on the sparse reward structure and inverse-probability weighting in SFT, a more rigorous theoretical analysis would strengthen the paper's contribution. Specifically, the paper does not delve into the convergence properties of DFT, or how the dynamic reweighting affects the optimization landscape compared to standard SFT. A more formal analysis of the gradient behavior and its impact on the training dynamics would be beneficial.
2. The paper does not explore the limitations of DFT in detail. While the authors mention that DFT may not be universally beneficial across all scenarios, a more thorough analysis of the scenarios where DFT might fail or underperform would be valuable. For example, it would be useful to investigate the performance of DFT on tasks with very sparse reward signals or in domains where the model's initial knowledge is highly lacking. The paper should also discuss the potential for DFT to introduce instability or oscillations during training, and how these issues might be mitigated.
3. The paper does not provide a detailed analysis of the computational overhead of DFT. While the authors mention that DFT is simple to implement, they do not discuss the computational cost of the dynamic reweighting process, especially for large models and datasets. A comparison of the training time and memory requirements of DFT with standard SFT would be helpful for practitioners who are considering adopting this method. The analysis should also consider the impact of the reweighting on the gradient variance and how this might affect the overall training efficiency.

### Suggestions

To strengthen the theoretical foundation of the paper, the authors should provide a more in-depth analysis of the convergence properties of DFT. This could involve deriving bounds on the convergence rate or analyzing the stability of the optimization process. Specifically, the authors could investigate how the dynamic reweighting affects the gradient norm and the curvature of the loss landscape. Furthermore, it would be beneficial to explore the relationship between the reweighting factor and the generalization performance, potentially through a theoretical analysis or empirical study. This would provide a more rigorous understanding of why DFT works and under what conditions it is most effective. The authors could also consider exploring connections to existing theoretical frameworks in reinforcement learning or optimization theory to provide a more solid theoretical basis for their method.

To address the limitations of DFT, the authors should conduct a more comprehensive empirical evaluation across a wider range of tasks and datasets. This should include tasks with varying degrees of reward sparsity, different types of input data, and different levels of model knowledge. For example, the authors could evaluate DFT on tasks with very sparse reward signals, such as those found in complex reasoning or planning problems. They could also investigate the performance of DFT on tasks where the model's initial knowledge is highly lacking, such as in low-resource languages or specialized domains. Additionally, the authors should analyze the sensitivity of DFT to hyperparameter settings and provide guidelines for selecting appropriate values. This would help practitioners to effectively apply DFT in different scenarios. The authors should also investigate the potential for DFT to introduce instability or oscillations during training, and how these issues might be mitigated.

Finally, the authors should provide a more detailed analysis of the computational overhead of DFT. This should include a comparison of the training time and memory requirements of DFT with standard SFT, as well as an analysis of the impact of the reweighting on the gradient variance. The authors could also explore techniques for reducing the computational cost of DFT, such as using approximations or heuristics for the dynamic reweighting process. This would make DFT more practical for large-scale applications. The authors should also discuss the scalability of DFT to larger models and datasets, and provide insights into how the computational cost might be managed in these scenarios. This analysis should be supported by empirical results and should provide clear guidance for practitioners who are considering adopting DFT.

### Questions

1. Could the authors provide a more detailed theoretical analysis of why DFT outperforms standard SFT? Specifically, how does the dynamic reweighting affect the convergence properties and generalization performance of the model?
2. What are the limitations of DFT, and in which scenarios might it not be the most effective approach? Could the authors provide more insights into the potential failure cases of DFT?
3. What is the computational overhead of DFT compared to standard SFT? How does the dynamic reweighting process affect the training time and memory requirements, especially for large models and datasets?

### Rating

8

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers for the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

Plan:
1. Go through each reviewer's comments one by one.
2. For each comment identified as a weakness, find the corresponding section in the paper.
3. Extract evidence (quotes, experimental setup, missing information) from the paper to support the reviewer's claim.
4. If the reviewer mentions missing literature, identify the specific area and check if the paper cites relevant works.
5. Synthesize the evidence and conclude whether the weakness is valid, partially valid, or invalid.
```json
[
  {
    "Weakness Statement": "The paper primarily focuses on empirical results and lacks a deep theoretical analysis of why DFT outperforms standard SFT. While the authors provide an intuitive explanation based on the sparse reward structure and inverse-probability weighting in SFT, a more rigorous theoretical analysis would strengthen the paper's contribution. Specifically, the paper does not delve into the convergence properties of DFT, or how the dynamic reweighting affects the optimization landscape compared to standard SFT. A more formal analysis of the gradient behavior and its impact on the training dynamics would be beneficial.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "We show that the gradient update in SFT can be interpreted as a form of policy gradient with a specific, implicitly defined reward under certain assumptions. Crucially, this reward is (i) sparse, and (ii) inversely proportional to the model’s probability of expert actions (see equation 6 ). As a result, when the model assigns low probability to expert actions, the resulting weight becomes excessively large, introducing an ill-posed reward structure and unstable optimization ( Pascanu et al., 2013 ; Yang et al., 2019 ) .",
        "Building on this insight, we propose Dynamic Fine-Tuning (DFT), a principled fix. Our method rescales the SFT objective at each token by its probability, canceling the distortion introduced by inverse-probability weighting.",
        "The resulting “dynamically fine-tuned” gradient is then\n\n∇θL_DFT(θ) = − 𝔼x∼𝒟 [ sg ( 1 w ) ⋅ w ( y ∣ x ) ∇θlog πθ(y ∣ x) r ( x , y ) ] . (8)\n\nwhere sg ⁡ ( ⋅ ) ∘ πθ( y ∣ x ) now becomes a simple reweighted loss, called Dynamic Fine-tuning (DFT).\n\nL_DFT ( θ ) = 𝔼 ( x , y ∆ ) [ − sg ⁡ ( π θ ( y ⋆ ∣ x ) ) ⋅ w ( y ∣ x ) ∇ θ log π θ ( y ∣ x ) ] . (9)",
        "Note that the reward of this corrected SFT (in RL form), i.e., DFT, now becomes 1 uniformly for all expert trajectory. This is akin to contemporary verification based reward approach RLVR ( DeepSeek-AI et al., 2025 ) that assigns uniform reward to all correct samples. Consequently, it avoids over-concentration on specific low-probability reference tokens, leading to more stable updates and improved generalization without introducing any additional sampling or reward models."
      ],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper provides an intuitive explanation of why DFT works by linking it to the sparse reward structure and inverse-probability weighting in SFT. It explains that DFT addresses the issue of large weights when the model assigns low probability to expert actions. The method section describes the mathematical formulation of DFT and its gradient update. The experimental section demonstrates the effectiveness of DFT through empirical results.",
      "Supporting quotes": [
        "We show that the gradient update in SFT can be interpreted as a form of policy gradient with a specific, implicitly defined reward under certain assumptions.",
        "Building on this insight, we propose Dynamic Fine-Tuning (DFT), a principled fix.",
        "The resulting “dynamically fine-tuned” gradient is then\n\n∇θL_DFT(θ) = − 𝔼x∼𝒟 [ sg ( 1 w ) ⋅ w ( y ∣ x ) ∇θlog πθ(y ∣ x) r ( x , y ) ] . (8)\n\nwhere sg ⁡ ( ⋅ ) ∘ πθ( y ∣ x ) now becomes a simple reweighted loss, called Dynamic Fine-tuning (DFT).",
        "Note that the reward of this corrected SFT (in RL form), i.e., DFT, now becomes 1 uniformly for all expert trajectory."
      ],
      "Impact assessment": "While the paper provides a high-level explanation and demonstrates empirical success, it lacks a deep theoretical analysis of the convergence properties of DFT or a formal analysis of how the dynamic reweighting affects the optimization landscape compared to standard SFT. The reviewer's point about the lack of a rigorous theoretical analysis is valid."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper focuses on the intuition behind DFT and its empirical validation but does not provide a formal theoretical analysis of its convergence properties or a detailed comparison of its optimization landscape with SFT."
    }
  },
  {
    "Weakness Statement": "The paper does not explore the limitations of DFT in detail. While the authors mention that DFT may not be universally beneficial across all scenarios, a more thorough analysis of the scenarios where DFT might fail or underperform would be valuable. For example, it would be useful to investigate the performance of DFT on tasks with very sparse reward signals or in domains where the model's initial knowledge is highly lacking. The paper should also discuss the potential for DFT to introduce instability or oscillations during training, and how these issues might be mitigated.",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": [
        "While DFT consistently outperforms SFT on reasoning-heavy tasks, it may not always be the better choice, particularly in factual knowledge domains. We conduct an exploratory experiment on the Natural Questions dataset ( Kwiatkowski et al., 2019 ) , which consists of real-user, open-domain factual queries grounded in Wikipedia articles.",
        "In this setting, we find that SFT improves performance from 31.24% to 36.62%, while DFT unexpectedly reduces it to 30.14%."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper includes an experiment on the Natural Questions dataset, which is a factual knowledge domain, and shows that DFT underperforms SFT in this specific scenario. This partially addresses the reviewer's point about limitations in certain scenarios.",
      "Supporting quotes": [
        "While DFT consistently outperforms SFT on reasoning-heavy tasks, it may not always be the better choice, particularly in factual knowledge domains.",
        "In this setting, we find that SFT improves performance from 31.24% to 36.62%, while DFT unexpectedly reduces it to 30.14%."
      ],
      "Impact assessment": "The paper does acknowledge a limitation of DFT in the context of factual knowledge domains. However, the reviewer's point about a more thorough analysis of scenarios where DFT might fail or underperform, including tasks with very sparse reward signals or domains with low initial knowledge, is partially valid as the paper only provides one example of underperformance. The paper also doesn't explicitly discuss potential instability or oscillations during training with DFT."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper includes an experiment showing DFT's underperformance in factual knowledge domains, but lacks a broader analysis of failure scenarios and doesn't explicitly address potential training instability."
    }
  },
  {
    "Weakness Statement": "The paper does not provide a detailed analysis of the computational overhead of DFT. While the authors mention that DFT is simple to implement, they do not discuss the computational cost of the dynamic reweighting process, especially for large models and datasets. A comparison of the training time and memory requirements of DFT with standard SFT would be helpful for practitioners who are considering adopting this method. The analysis should also consider the impact of the reweighting on the gradient variance and how this might affect the overall training efficiency.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "The resulting “dynamically fine-tuned” gradient is then\n\n∇θL_DFT(θ) = − 𝔼x∼𝒟 [ sg ( 1 w ) ⋅ w ( y ∣ x ) ∇θlog πθ(y ∣ x) r ( x , y ) ] . (8)\n\nwhere sg ⁡ ( ⋅ ) ∘ πθ( y ∣ x ) now becomes a simple reweighted loss, called Dynamic Fine-tuning (DFT).\n\nL_DFT ( θ ) = 𝔼 ( x , y ∆ ) [ − sg ⁡ ( π θ ( y ⋆ ∣ x ) ) ⋅ w ( y ∣ x ) ∇ θ log π θ ( y ∣ x ) ] . (9)"
      ],
      "b) Experiment-related Evidence": [
        "We set the mini-batch size to 256 and the maximum input length to 2048 tokens.",
        "The learning rate follows a cosine decay schedule with a warm-up ratio of 0.1.",
        "We set the number of response n = 4 for GRAND2 and Λ = 4 for GRAND2-Coder."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper describes the mathematical formulation of DFT, which involves a dynamic reweighting step. However, it does not provide any explicit analysis or measurements of the computational overhead associated with this reweighting process.",
      "Supporting quotes": [
        "The resulting “dynamically fine-tuned” gradient is then\n\n∇θL_DFT(θ) = − 𝔼x∼𝒟 [ sg ( 1 w ) ⋅ w ( y ∣ x ) ∇θlog πθ(y ∣ x) r ( x , y ) ] . (8)\n\nwhere sg ⁡ ( ⋅ ) ∘ πθ( y ∣ x ) now becomes a simple reweighted loss, called Dynamic Fine-tuning (DFT)."
      ],
      "Impact assessment": "The reviewer's point about the lack of a detailed analysis of the computational overhead of DFT is valid. The paper focuses on the conceptual simplicity and empirical effectiveness of DFT but does not delve into the computational costs associated with the dynamic reweighting, which is a crucial aspect for practical application, especially with large models and datasets."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper describes the DFT method but lacks any quantitative analysis or discussion regarding the computational cost of the dynamic reweighting process."
    }
  },
  {
    "Weakness Statement": "How does DFT perform on tasks with sparse rewards, and how does it compare to other methods designed for such environments?",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "We show that the gradient update in SFT can be interpreted as a form of policy gradient with a specific, implicitly defined reward under certain assumptions. Crucially, this reward is (i) sparse, and (ii) inversely proportional to the model’s probability of expert actions (see equation 6 ). As a result, when the model assigns low probability to expert actions, the resulting weight becomes excessively large, introducing an ill-posed reward structure and unstable optimization ( Pascanu et al., 2013 ; Yang et al., 2019 ) ."
      ],
      "b) Experiment-related Evidence": [
        "DFT consistently yields average accuracy improvements over base models compared to standard SFT across all benchmarks. Table 1 shows that, for Qwen2.5-Math-1.5B, DFT achieves an average gain of +15.66 points over the base model, which is over 5.9 × larger than the +2.09 point improvement from SFT. This pattern generalizes across other model families and sizes: LLaMA-3.2-3B benefits from a +3.46 point gain with DFT, exceeding the SFT gain (+2.05) by approximately 1.4 × ; LLaMA-3.1-8B achieves +10.02 from DFT, surpassing SFT’s +5.33 by 1.88 × ; DeepSeekMath-7B sees a +15.51 point improvement via DFT, which is 1.58 × larger than SFT’s +7.18; and Qwen2.5-Math-7B reaches a +15.90 point gain, nearly 3.8 × larger than the SFT improvement of +2.37."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper argues that SFT has a sparse reward structure and that DFT addresses this by reweighting. The experimental results show significant improvements across various tasks, including mathematical reasoning, which can be considered a form of sparse reward environment where the correct answer is a small subset of possibilities. The comparison is primarily against standard SFT, not other methods specifically designed for sparse reward environments.",
      "Supporting quotes": [
        "We show that the gradient update in SFT can be interpreted as a form of policy gradient with a specific, implicitly defined reward under certain assumptions. Crucially, this reward is (i) sparse, and (ii) inversely proportional to the model’s probability of expert actions (see equation 6 ).",
        "DFT consistently yields average accuracy improvements over base models compared to standard SFT across all benchmarks."
      ],
      "Impact assessment": "The reviewer's question is valid in that while the paper argues for DFT's effectiveness in sparse reward settings and shows improvements over SFT, it doesn't directly compare DFT against methods specifically designed for such environments. The paper focuses on the general benefits of DFT over standard SFT."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper argues for DFT's suitability for sparse reward settings and shows improvements over SFT, but lacks a direct comparison to methods specifically designed for sparse rewards."
    }
  },
  {
    "Weakness Statement": "Can the authors provide more insights into the theoretical underpinnings of why DFT improves generalization in SFT?",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "We show that the gradient update in SFT can be interpreted as a form of policy gradient with a specific, implicitly defined reward under certain assumptions. Crucially, this reward is (i) sparse, and (ii) inversely proportional to the model’s probability of expert actions (see equation 6 ). As a result, when the model assigns low probability to expert actions, the resulting weight becomes excessively large, introducing an ill-posed reward structure and unstable optimization ( Pascanu et al., 2013 ; Yang et al., 2019 ) .",
        "Building on this insight, we propose Dynamic Fine-Tuning (DFT), a principled fix. Our method rescales the SFT objective at each token by its probability, canceling the distortion introduced by inverse-probability weighting.",
        "The resulting “dynamically fine-tuned” gradient is then\n\n∇θL_DFT(θ) = − 𝔼x∼𝒟 [ sg ( 1 w ) ⋅ w ( y ∣ x ) ∇θlog πθ(y ∣ x) r ( x , y ) ] . (8)\n\nwhere sg ⁡ ( ⋅ ) ∘ πθ( y ∣ x ) now becomes a simple reweighted loss, called Dynamic Fine-tuning (DFT).\n\nL_DFT ( θ ) = 𝔼 ( x , y ∆ ) [ − sg ⁡ ( π θ ( y ⋆ ∣ x ) ) ⋅ w ( y ∣ x ) ∇ θ log π θ ( y ∣ x ) ] . (9)",
        "Note that the reward of this corrected SFT (in RL form), i.e., DFT, now becomes 1 uniformly for all expert trajectory. This is akin to contemporary verification based reward approach RLVR ( DeepSeek-AI et al., 2025 ) that assigns uniform reward to all correct samples. Consequently, it avoids over-concentration on specific low-probability reference tokens, leading to more stable updates and improved generalization without introducing any additional sampling or reward models."
      ],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper provides a theoretical justification for DFT by interpreting the SFT gradient update as a form of policy gradient with a sparse, inverse-probability-weighted reward. It argues that this reward structure leads to unstable optimization, and DFT addresses this by reweighting the objective, resulting in a uniform reward for expert trajectories.",
      "Supporting quotes": [
        "We show that the gradient update in SFT can be interpreted as a form of policy gradient with a specific, implicitly defined reward under certain assumptions.",
        "Crucially, this reward is (i) sparse, and (ii) inversely proportional to the model’s probability of expert actions (see equation 6 ).",
        "As a result, when the model assigns low probability to expert actions, the resulting weight becomes excessively large, introducing an ill-posed reward structure and unstable optimization",
        "Note that the reward of this corrected SFT (in RL form), i.e., DFT, now becomes 1 uniformly for all expert trajectory."
      ],
      "Impact assessment": "The paper offers a theoretical explanation for why DFT improves generalization by linking it to the properties of the SFT reward structure and how DFT mitigates the issues arising from that structure. However, the reviewer's question suggests a desire for even deeper or more intuitive insights, which the paper might not fully address."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper provides a theoretical framework explaining DFT's benefits based on the SFT reward structure, but the depth of theoretical insight might be considered limited by the reviewer."
    }
  },
  {
    "Weakness Statement": "What are the limitations of DFT, and in which scenarios might it not be the most effective approach?",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": [
        "While DFT consistently outperforms SFT on reasoning-heavy tasks, it may not always be the better choice, particularly in factual knowledge domains. We conduct an exploratory experiment on the Natural Questions dataset ( Kwiatkowski et al., 2019 ) , which consists of real-user, open-domain factual queries grounded in Wikipedia articles.",
        "In this setting, we find that SFT improves performance from 31.24% to 36.62%, while DFT unexpectedly reduces it to 30.14%."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper acknowledges the limitation of DFT in the context of factual knowledge domains, where it underperforms SFT. This suggests that the limitations of DFT are not solely theoretical but also manifest in practical applications.",
      "Supporting quotes": [
        "While DFT consistently outperforms SFT on reasoning-heavy tasks, it may not always be the better choice, particularly in factual knowledge domains.",
        "In this setting, we find that SFT improves performance from 31.24% to 36.62%, while DFT unexpectedly reduces it to 30.14%."
      ],
      "Impact assessment": "The paper does identify one specific scenario where DFT is not the most effective approach. However, as with the previous reviewer's comment, a more comprehensive discussion of limitations across various scenarios could be beneficial."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper identifies factual knowledge domains as a scenario where DFT underperforms SFT, indicating a limitation, but a broader discussion of limitations is lacking."
    }
  },
  {
    "Weakness Statement": "What is the computational overhead of DFT compared to standard SFT? How does the dynamic reweighting process affect the training time and memory requirements, especially for large models and datasets?",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "The resulting “dynamically fine-tuned” gradient is then\n\n∇θL_DFT(θ) = − 𝔼x∼𝒟 [ sg ( 1 w ) ⋅ w ( y ∣ x ) ∇θlog πθ(y ∣ x) r ( x , y ) ] . (8)\n\nwhere sg ⁡ ( ⋅ ) ∘ πθ( y ∣ x ) now becomes a simple reweighted loss, called Dynamic Fine-tuning (DFT)."
      ],
      "b) Experiment-related Evidence": [
        "We set the mini-batch size to 256 and the maximum input length to 2048 tokens.",
        "The learning rate follows a cosine decay schedule with a warm-up ratio of 0.1."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper describes the DFT method, which involves dynamic reweighting. However, it does not provide any quantitative analysis of the computational cost associated with this reweighting process.",
      "Supporting quotes": [
        "The resulting “dynamically fine-tuned” gradient is then\n\n∇θL_DFT(θ) = − 𝔼x∼𝒟 [ sg ( 1 w ) ⋅ w ( y ∣ x ) ∇θlog πθ(y ∣ x) r ( x , y ) ] . (8)"
      ],
      "Impact assessment": "The reviewer's question about the computational overhead of DFT is valid. The paper focuses on the conceptual simplicity and empirical effectiveness of DFT but lacks a detailed analysis of the computational costs associated with the dynamic reweighting, which is a crucial aspect for practical application, especially with large models and datasets."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper describes the DFT method but lacks any quantitative analysis or discussion regarding the computational cost of the dynamic reweighting process."
    }
  },
  {
    "Weakness Statement": "Could the authors provide a more detailed theoretical analysis of why DFT outperforms standard SFT? Specifically, how does the dynamic reweighting affect the convergence properties and generalization performance of the model?",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "We show that the gradient update in SFT can be interpreted as a form of policy gradient with a specific, implicitly defined reward under certain assumptions. Crucially, this reward is (i) sparse, and (ii) inversely proportional to the model’s probability of expert actions (see equation 6 ). As a result, when the model assigns low probability to expert actions, the resulting weight becomes excessively large, introducing an ill-posed reward structure and unstable optimization ( Pascanu et al., 2013 ; Yang et al., 2019 ) .",
        "Building on this insight, we propose Dynamic Fine-Tuning (DFT), a principled fix. Our method rescales the SFT objective at each token by its probability, canceling the distortion introduced by inverse-probability weighting.",
        "The resulting “dynamically fine-tuned” gradient is then\n\n∇θL_DFT(θ) = − 𝔼x∼𝒟 [ sg ( 1 w ) ⋅ w ( y ∣ x ) ∇θlog πθ(y ∣ x) r ( x , y ) ] . (8)\n\nwhere sg ⁡ ( ⋅ ) ∘ πθ( y ∣ x ) now becomes a simple reweighted loss, called Dynamic Fine-tuning (DFT).\n\nL_DFT ( θ ) = 𝔼 ( x , y ∆ ) [ − sg ⁡ ( π θ ( y ⋆ ∣ x ) ) ⋅ w ( y ∣ x ) ∇ θ log π θ ( y ∣ x ) ] . (9)",
        "Note that the reward of this corrected SFT (in RL form), i.e., DFT, now becomes 1 uniformly for all expert trajectory. This is akin to contemporary verification based reward approach RLVR ( DeepSeek-AI et al., 2025 ) that assigns uniform reward to all correct samples. Consequently, it avoids over-concentration on specific low-probability reference tokens, leading to more stable updates and improved generalization without introducing any additional sampling or reward models."
      ],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper provides a theoretical analysis by interpreting SFT as a policy gradient with a sparse, inverse-probability-weighted reward. It argues that this structure leads to unstable optimization and that DFT addresses this by reweighting, resulting in a uniform reward for expert trajectories. However, the analysis doesn't delve into the specific impact on convergence properties or provide a formal proof of generalization improvement.",
      "Supporting quotes": [
        "We show that the gradient update in SFT can be interpreted as a form of policy gradient with a specific, implicitly defined reward under certain assumptions.",
        "As a result, when the model assigns low probability to expert actions, the resulting weight becomes excessively large, introducing an ill-posed reward structure and unstable optimization",
        "Note that the reward of this corrected SFT (in RL form), i.e., DFT, now becomes 1 uniformly for all expert trajectory."
      ],
      "Impact assessment": "The reviewer's point is valid. While the paper offers a theoretical justification for DFT's effectiveness, it lacks a detailed analysis of how the dynamic reweighting specifically affects convergence and generalization, such as through the lens of optimization theory or learning theory."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper provides a theoretical framework but lacks a detailed analysis of the impact of DFT's dynamic reweighting on convergence and generalization properties."
    }
  },
  {
    "Weakness Statement": "What are the limitations of DFT, and in which scenarios might it not be the most effective approach? Could the authors provide more insights into the potential failure cases of DFT?",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": [
        "While DFT consistently outperforms SFT on reasoning-heavy tasks, it may not always be the better choice, particularly in factual knowledge domains. We conduct an exploratory experiment on the Natural Questions dataset ( Kwiatkowski et al., 2019 ) , which consists of real-user, open-domain factual queries grounded in Wikipedia articles.",
        "In this setting, we find that SFT improves performance from 31.24% to 36.62%, while DFT unexpectedly reduces it to 30.14%."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper identifies one specific scenario (factual knowledge domains) where DFT underperforms SFT. This suggests a limitation of DFT in certain domains. However, the paper does not provide a comprehensive analysis of potential failure cases or scenarios where DFT might be ineffective.",
      "Supporting quotes": [
        "While DFT consistently outperforms SFT on reasoning-heavy tasks, it may not always be the better choice, particularly in factual knowledge domains.",
        "In this setting, we find that SFT improves performance from 31.24% to 36.62%, while DFT unexpectedly reduces it to 30.14%."
      ],
      "Impact assessment": "The reviewer's point is valid. While the paper acknowledges one limitation, a more thorough discussion of potential failure cases and scenarios where DFT might not be the best choice would strengthen the paper."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper identifies one failure case but lacks a broader discussion of potential failure scenarios for DFT."
    }
  },
  {
    "Weakness Statement": "What is the computational overhead of DFT compared to standard SFT? How does the dynamic reweighting process affect the training time and memory requirements, especially for large models and datasets?",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "The resulting “dynamically fine-tuned” gradient is then\n\n∇θL_DFT(θ) = − 𝔼x∼𝒟 [ sg ( 1 w ) ⋅ w ( y ∣ x ) ∇θlog πθ(y ∣ x) r ( x , y ) ] . (8)\n\nwhere sg ⁡ ( ⋅ ) ∘ πθ( y ∣ x ) now becomes a simple reweighted loss, called Dynamic Fine-tuning (DFT)."
      ],
      "b) Experiment-related Evidence": [
        "We set the mini-batch size to 256 and the maximum input length to 2048 tokens.",
        "The learning rate follows a cosine decay schedule with a warm-up ratio of 0.1."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper describes the DFT method, which involves dynamic reweighting. However, it does not provide any quantitative analysis of the computational cost associated with this reweighting process.",
      "Supporting quotes": [
        "The resulting “dynamically fine-tuned” gradient is then\n\n∇θL_DFT(θ) = − 𝔼x∼𝒟 [ sg ( 1 w ) ⋅ w ( y ∣ x ) ∇θlog πθ(y ∣ x) r ( x , y ) ] . (8)"
      ],
      "Impact assessment": "The reviewer's question about the computational overhead of DFT is valid. The paper focuses on the conceptual simplicity and empirical effectiveness of DFT but lacks a detailed analysis of the computational costs associated with the dynamic reweighting, which is a crucial aspect for practical application, especially with large models and datasets."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper describes the DFT method but lacks any quantitative analysis or discussion regarding the computational cost of the dynamic reweighting process."
    }
  },
  {
    "Weakness Statement": "The paper primarily focuses on empirical results and lacks a deep theoretical analysis of why DFT outperforms standard SFT. While the authors provide an intuitive explanation based on the sparse reward structure and inverse-probability weighting in SFT, a more rigorous theoretical analysis would strengthen the paper's contribution. Specifically, the paper does not delve into the convergence properties of DFT, or how the dynamic reweighting affects the optimization landscape compared to standard SFT. A more formal analysis of the gradient behavior and its impact on the training dynamics would be beneficial.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "We show that the gradient update in SFT can be interpreted as a form of policy gradient with a specific, implicitly defined reward under certain assumptions. Crucially, this reward is (i) sparse, and (ii) inversely proportional to the model’s probability of expert actions (see equation 6 ). As a result, when the model assigns low probability to expert actions, the resulting weight becomes excessively large, introducing an ill-posed reward structure and unstable optimization ( Pascanu et al., 2013 ; Yang et al., 2019 ) .",
        "Building on this insight, we propose Dynamic Fine-Tuning (DFT), a principled fix. Our method rescales the SFT objective at each token by its probability, canceling the distortion introduced by inverse-probability weighting.",
        "The resulting “dynamically fine-tuned” gradient is then\n\n∇θL_DFT(θ) = − 𝔼x∼𝒟 [ sg ( 1 w ) ⋅ w ( y ∣ x ) ∇θlog πθ(y ∣ x) r ( x , y ) ] . (8)\n\nwhere sg ⁡ ( ⋅ ) ∘ πθ( y ∣ x ) now becomes a simple reweighted loss, called Dynamic Fine-tuning (DFT).\n\nL_DFT ( θ ) = 𝔼 ( x , y ∆ ) [ − sg ⁡ ( π θ ( y ⋆ ∣ x ) ) ⋅ w ( y ∣ x ) ∇ θ log π θ ( y ∣ x ) ] . (9)",
        "Note that the reward of this corrected SFT (in RL form), i.e., DFT, now becomes 1 uniformly for all expert trajectory. This is akin to contemporary verification based reward approach RLVR ( DeepSeek-AI et al., 2025 ) that assigns uniform reward to all correct samples. Consequently, it avoids over-concentration on specific low-probability reference tokens, leading to more stable updates and improved generalization without introducing any additional sampling or reward models."
      ],
      "b) Experiment-related Evidence": []
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper provides an intuitive explanation linking SFT to policy gradients with sparse, inverse-probability-weighted rewards. It argues that DFT addresses the issues arising from this structure. However, it lacks a rigorous theoretical analysis of DFT's convergence properties or a formal comparison of its optimization landscape with SFT.",
      "Supporting quotes": [
        "We show that the gradient update in SFT can be interpreted as a form of policy gradient with a specific, implicitly defined reward under certain assumptions.",
        "Crucially, this reward is (i) sparse, and (ii) inversely proportional to the model’s probability of expert actions (see equation 6 ).",
        "As a result, when the model assigns low probability to expert actions, the resulting weight becomes excessively large, introducing an ill-posed reward structure and unstable optimization",
        "Note that the reward of this corrected SFT (in RL form), i.e., DFT, now becomes 1 uniformly for all expert trajectory."
      ],
      "Impact assessment": "The reviewer's assessment is accurate. The paper's theoretical analysis is primarily intuitive and lacks the depth of a formal theoretical treatment, particularly regarding convergence and optimization landscape."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper's theoretical analysis is primarily intuitive and lacks a rigorous examination of DFT's convergence properties or a formal comparison of its optimization landscape with SFT."
    }
  },
  {
    "Weakness Statement": "The paper does not explore the limitations of DFT in detail. While the authors mention that DFT may not be universally beneficial across all scenarios, a more thorough analysis of the scenarios where DFT might fail or underperform would be valuable. For example, it would be useful to investigate the performance of DFT on tasks with very sparse reward signals or in domains where the model's initial knowledge is highly lacking. The paper should also discuss the potential for DFT to introduce instability or oscillations during training, and how these issues might be mitigated.",
    "Evidence Collection": {
      "a) Method-related Evidence": [],
      "b) Experiment-related Evidence": [
        "While DFT consistently outperforms SFT on reasoning-heavy tasks, it may not always be the better choice, particularly in factual knowledge domains. We conduct an exploratory experiment on the Natural Questions dataset ( Kwiatkowski et al., 2019 ) , which consists of real-user, open-domain factual queries grounded in Wikipedia articles.",
        "In this setting, we find that SFT improves performance from 31.24% to 36.62%, while DFT unexpectedly reduces it to 30.14%."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper acknowledges a limitation of DFT in factual knowledge domains. However, it doesn't provide a comprehensive analysis of failure scenarios or potential instabilities, such as oscillations, or explore performance on tasks with very sparse rewards.",
      "Supporting quotes": [
        "While DFT consistently outperforms SFT on reasoning-heavy tasks, it may not always be the better choice, particularly in factual knowledge domains.",
        "In this setting, we find that SFT improves performance from 31.24% to 36.62%, while DFT unexpectedly reduces it to 30.14%."
      ],
      "Impact assessment": "The reviewer's point is valid. The paper's discussion of limitations is somewhat limited, and a more thorough investigation of failure cases, potential instabilities, and performance in sparse reward scenarios would be beneficial."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper acknowledges one failure case but lacks a broader discussion of potential failure scenarios, instability, or performance in sparse reward settings."
    }
  },
  {
    "Weakness Statement": "Finally, the authors should provide a more detailed analysis of the computational overhead of DFT. This should include a comparison of the training time and memory requirements of DFT with standard SFT, as well as an analysis of the impact of the reweighting on the gradient variance. The authors could also explore techniques for reducing the computational cost of DFT, such as using approximations or heuristics for the dynamic reweighting process. This would make DFT more practical for large-scale applications. The authors should also discuss the scalability of DFT to larger models and datasets, and provide insights into how the computational cost might be managed in these scenarios. This analysis should be supported by empirical results and should provide clear guidance for practitioners who are considering adopting DFT.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "The resulting “dynamically fine-tuned” gradient is then\n\n∇θL_DFT(θ) = − 𝔼x∼𝒟 [ sg ( 1 w ) ⋅ w ( y ∣ x ) ∇θlog πθ(y ∣ x) r ( x , y ) ] . (8)\n\nwhere sg ⁡ ( ⋅ ) ∘ πθ( y ∣ x ) now becomes a simple reweighted loss, called Dynamic Fine-tuning (DFT)."
      ],
      "b) Experiment-related Evidence": [
        "We set the mini-batch size to 256 and the maximum input length to 2048 tokens.",
        "The learning rate follows a cosine decay schedule with a warm-up ratio of 0.1."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper describes the DFT method, which involves dynamic reweighting. However, it does not provide any quantitative analysis of the computational cost associated with this reweighting process, nor does it compare training time and memory requirements with SFT, analyze gradient variance, or discuss techniques for reducing computational cost.",
      "Supporting quotes": [
        "The resulting “dynamically fine-tuned” gradient is then\n\n∇θL_DFT(θ) = − 𝔼x∼𝒟 [ sg ( 1 w ) ⋅ w ( y ∣ x ) ∇θlog πθ(y ∣ x) r ( x , y ) ] . (8)"
      ],
      "Impact assessment": "The reviewer's point}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces Dynamic Fine-Tuning (DFT), a novel method designed to enhance the generalization capabilities of large language models (LLMs) through Supervised Fine-Tuning (SFT). The authors begin by analyzing the limitations of standard SFT, framing it as a policy gradient with an ill-posed, sparse reward structure and inverse-probability weighting inherent in its objective function. They argue that this structure leads to unstable optimization and suboptimal performance, particularly in tasks with sparse rewards. To address this, DFT dynamically reweights the SFT objective at each token by its probability, effectively canceling out the inverse-probability weighting and resulting in a more stable and well-behaved learning process. The core idea is that by reweighting the loss based on the model's own probability distribution over tokens, the optimization landscape becomes smoother and less prone to instability. The authors demonstrate the effectiveness of DFT across a range of tasks, including mathematical reasoning, code generation, and multi-modal reasoning, showing consistent improvements over standard SFT. Furthermore, they explore the applicability of DFT in offline RL settings, where it outperforms standard offline RL algorithms. The method is presented as a simple, easy-to-implement modification to the SFT loss, requiring only a single-line change to the existing SFT formulation. The empirical results are compelling, with DFT consistently outperforming SFT across various tasks and models. The authors also provide a theoretical interpretation of DFT, linking it to policy gradients and sparse rewards, which adds to the understanding of why it works. Overall, the paper presents a well-motivated and empirically validated approach to improving the generalization of LLMs through SFT, offering a practical and accessible solution to a common problem in the field. The authors' approach of viewing SFT through the lens of reinforcement learning provides a fresh perspective on the challenges of training LLMs and offers a promising direction for future research.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

3.0


## Strengths:

I find several aspects of this paper to be particularly strong. First, the paper provides a novel perspective on Supervised Fine-Tuning (SFT) by interpreting it through the lens of reinforcement learning. This approach allows the authors to identify the sparse reward structure and inverse-probability weighting inherent in SFT, which are key to understanding the limitations of standard SFT. This theoretical framing is not only insightful but also provides a solid foundation for the proposed Dynamic Fine-Tuning (DFT) method. The core idea of DFT, which involves dynamically reweighting the SFT objective based on the model's probability distribution, is both simple and effective. This simplicity makes DFT easy to implement, requiring only a single-line modification to the standard SFT loss, which is a significant practical advantage. The empirical results presented in the paper are also compelling. The authors demonstrate the effectiveness of DFT across a wide range of tasks, including mathematical reasoning, code generation, and multi-modal reasoning, consistently showing improvements over standard SFT. The fact that DFT outperforms standard SFT across various tasks and models, including Qwen and LLaMA, highlights its broad applicability and effectiveness. The paper also explores the applicability of DFT in offline RL settings, where it outperforms standard offline RL algorithms, further demonstrating the versatility of the method. The authors' ability to connect the theoretical insights with practical results is a testament to the strength of their approach. The paper is also well-structured and clearly written, making it easy to follow and understand. The authors provide a comprehensive analysis of the limitations of SFT and effectively motivate the need for DFT. The theoretical framework is well-developed, and the experimental results are presented in a clear and organized manner. The paper's contribution is significant, offering a practical and theoretically grounded method for improving the generalization of LLMs through SFT. The simplicity of the method, its broad applicability, and the strong empirical results make this a valuable contribution to the field.


## Weaknesses:

Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, while the paper provides an intuitive explanation for why SFT suffers from sparse rewards and inverse-probability weighting, it lacks a deep theoretical analysis of the convergence properties of DFT or a formal comparison of its optimization landscape with SFT. The authors argue that DFT addresses the issues arising from the sparse reward structure and inverse-probability weighting in SFT, but they do not delve into how the dynamic reweighting affects the gradient norm and the curvature of the loss landscape. This lack of a rigorous theoretical analysis limits our understanding of why DFT works and under what conditions it is most effective. Specifically, the paper does not provide a formal analysis of how the dynamic reweighting affects the optimization process, and how it might lead to a more stable and efficient learning process. This is a significant limitation, as it leaves open questions about the theoretical underpinnings of DFT. My confidence in this weakness is high, as the paper's theoretical analysis is primarily intuitive and lacks the depth of a formal theoretical treatment. Second, the paper does not provide a detailed analysis of the computational overhead of DFT. While the authors mention that DFT is simple to implement, they do not discuss the computational cost of the dynamic reweighting process, especially for large models and datasets. The paper lacks any quantitative analysis of the training time and memory requirements of DFT compared to standard SFT, and it does not analyze the impact of the reweighting on the gradient variance. This is a significant omission, as it is crucial to understand the practical implications of using DFT, especially in resource-constrained environments. My confidence in this weakness is high, as the paper focuses on the conceptual simplicity and empirical effectiveness of DFT but lacks any quantitative analysis or discussion regarding the computational cost of the dynamic reweighting process. Third, the paper does not provide a comprehensive analysis of the limitations of DFT. While the authors acknowledge that DFT may not be universally beneficial across all scenarios, they do not thoroughly explore the scenarios where DFT might fail or underperform. The paper does not investigate the performance of DFT on tasks with very sparse reward signals or in domains where the model's initial knowledge is highly lacking. The paper also does not discuss the potential for DFT to introduce instability or oscillations during training, and how these issues might be mitigated. My confidence in this weakness is high, as the paper's discussion of limitations is somewhat limited, and a more thorough investigation of failure cases, potential instabilities, and performance in sparse reward settings would be beneficial. Fourth, the paper does not provide a direct comparison of DFT against methods specifically designed for sparse reward environments. While the paper argues that SFT has a sparse reward structure, it does not compare DFT against other methods that are explicitly designed for such environments. This makes it difficult to assess the unique advantages of DFT in the context of sparse rewards. My confidence in this weakness is high, as the paper focuses on the general benefits of DFT over standard SFT, but lacks a direct comparison to methods specifically designed for sparse reward environments. Finally, the paper does not provide a detailed analysis of the theoretical underpinnings of why DFT outperforms standard SFT. While the paper provides an intuitive explanation based on the sparse reward structure and inverse-probability weighting in SFT, it lacks a more rigorous theoretical analysis of how the dynamic reweighting affects the convergence properties and generalization performance of the model. My confidence in this weakness is high, as the paper's theoretical analysis is primarily intuitive and lacks a rigorous examination of DFT's convergence properties or a formal comparison of its optimization landscape with SFT.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should provide a more in-depth analysis of the convergence properties of DFT. This could involve deriving bounds on the convergence rate or analyzing the stability of the optimization process. Specifically, the authors could investigate how the dynamic reweighting affects the gradient norm and the curvature of the loss landscape. Furthermore, it would be beneficial to explore the relationship between the reweighting factor and the generalization performance, potentially through a theoretical analysis or empirical study. This would provide a more rigorous understanding of why DFT works and under what conditions it is most effective. The authors could also consider exploring connections to existing theoretical frameworks in reinforcement learning or optimization theory to provide a more solid theoretical basis for their method. Second, the authors should provide a more detailed analysis of the computational overhead of DFT. This should include a comparison of the training time and memory requirements of DFT with standard SFT, as well as an analysis of the impact of the reweighting on the gradient variance. The authors could also explore techniques for reducing the computational cost of DFT, such as using approximations or heuristics for the dynamic reweighting process. This would make DFT more practical for large-scale applications. The authors should also discuss the scalability of DFT to larger models and datasets, and provide insights into how the computational cost might be managed in these scenarios. This analysis should be supported by empirical results and should provide clear guidance for practitioners who are considering adopting DFT. Third, the authors should conduct a more comprehensive empirical evaluation across a wider range of tasks and datasets. This should include tasks with varying degrees of reward sparsity, different types of input data, and different levels of model knowledge. For example, the authors could evaluate DFT on tasks with very sparse reward signals, such as those found in low-resource languages or specialized domains. They could also investigate the performance of DFT on tasks where the model's initial knowledge is highly lacking, such as in low-resource languages or specialized domains. Additionally, the authors should analyze the sensitivity of DFT to hyperparameter settings and provide guidelines for selecting appropriate values. This would help practitioners to effectively apply DFT in different scenarios. The authors should also investigate the potential for DFT to introduce instability or oscillations during training, and how these issues might be mitigated. Fourth, the authors should include a more detailed comparison of DFT with other methods designed for sparse reward environments. This comparison should include a discussion of the trade-offs between different methods, such as performance gains versus computational overhead. The authors should also consider comparing DFT with methods that incorporate adaptive learning rates or more sophisticated reward structures. This would help to clarify DFT's unique advantages and limitations in the broader landscape of fine-tuning approaches. Finally, the authors should provide a more detailed theoretical analysis of why DFT outperforms standard SFT. This could involve a more formal analysis of the gradient behavior and its impact on the training dynamics. The authors should also explore connections to existing theoretical frameworks in reinforcement learning or optimization theory to provide a more solid theoretical basis for their method. This would provide a more rigorous understanding of why DFT works and under what conditions it is most effective.


## Questions:

I have several questions that arise from my analysis of this paper. First, could the authors provide a more detailed theoretical analysis of why DFT outperforms standard SFT? Specifically, how does the dynamic reweighting affect the convergence properties and generalization performance of the model? While the paper provides an intuitive explanation based on the sparse reward structure and inverse-probability weighting in SFT, it lacks a more rigorous theoretical analysis of how the dynamic reweighting affects the optimization process. Second, what are the limitations of DFT, and in which scenarios might it not be the most effective approach? While the paper acknowledges that DFT may not be universally beneficial across all scenarios, it does not provide a comprehensive analysis of the scenarios where DFT might fail or underperform. For example, it would be useful to investigate the performance of DFT on tasks with very sparse reward signals or in domains where the model's initial knowledge is highly lacking. Third, what is the computational overhead of DFT compared to standard SFT? How does the dynamic reweighting process affect the training time and memory requirements, especially for large models and datasets? The paper does not provide any quantitative analysis of the computational cost associated with the dynamic reweighting, which is a crucial aspect for practical application, especially with large models and datasets. Fourth, what is the impact of the dynamic reweighting process on the training time and memory requirements, especially for large models and datasets? How does the reweighting process affect the gradient variance? The paper does not provide a detailed analysis of the impact of the reweighting on the training dynamics, which is important for understanding the practical implications of using DFT. Finally, how does DFT compare to other methods designed for sparse reward environments? The paper does not provide a direct comparison of DFT against methods specifically designed for sparse reward environments, which makes it difficult to assess the unique advantages of DFT in the context of sparse rewards. These questions target key uncertainties in the paper and seek clarification on core methodological choices and assumptions.


## Rating:

6.4


## Confidence:

3.2


## Decision:

Accept
}