I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

The paper proposes AdEMAMix, a variant of the Adam optimizer that uses two exponential moving averages (EMAs) of gradients, instead of one as in Adam. The authors argue that using a single EMA has limitations and that using two EMAs can provide better performance. They conduct experiments on language modeling and image classification tasks, showing that AdEMAMix outperforms Adam in terms of training speed and final performance.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.
- The experiments are comprehensive and cover a range of tasks and model sizes.
- The proposed method is simple and easy to implement.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a clear motivation for why using two EMAs is better than using one. The authors claim that one EMA cannot provide sufficient weight to recent gradients, but they do not provide any evidence or theoretical analysis to support this claim. It is not clear why a single EMA with a different hyperparameter setting would not be able to achieve similar results.
- The paper lacks a detailed analysis of the computational overhead of AdEMAMix. While the authors mention that the additional EMA requires additional memory and computation, they do not provide a quantitative analysis of the overhead. It is important to understand the trade-offs between performance gains and computational costs, especially when comparing AdEMAMix to other optimizers.
- The paper does not compare AdEMAMix to other optimizers that use multiple momentum terms, such as Lion and RAdam. These optimizers also use multiple momentum terms, but they do not use EMA. It is important to understand how AdEMAMix compares to these optimizers in terms of performance and computational cost.
- The paper does not provide a clear explanation of how the two EMAs are combined in the update rule. The authors do not explain why they are added together or why this is the optimal way to combine them. It is important to understand the design choices behind the update rule and how they affect the performance of the optimizer.
- The paper does not provide a detailed analysis of the convergence properties of AdEMAMix. While the authors show that AdEMAMix converges faster than Adam, they do not provide a theoretical analysis of the convergence rate. It is important to understand the theoretical properties of the optimizer and how they relate to its performance in practice.

### Suggestions

The paper would benefit from a more thorough investigation into the necessity of using two exponential moving averages (EMAs). While the authors argue that a single EMA struggles to balance recent and older gradients, they do not provide sufficient evidence to support this claim. A more rigorous analysis, perhaps through ablation studies or a theoretical justification, is needed to demonstrate why a single EMA cannot achieve similar performance when tuned appropriately. For example, the authors could explore the effect of varying the decay rate of a single EMA and compare it to the proposed two-EMA approach. This would help to isolate the specific benefits of using two EMAs and justify the added complexity. Furthermore, the authors should provide a more detailed explanation of how the two EMAs are combined in the update rule. The current explanation is insufficient, and it is unclear why the two EMAs are simply added together. A more thorough explanation of the design choices behind the update rule is needed, including a discussion of alternative combination methods and their potential impact on performance. This would help to clarify the motivation behind the proposed approach and make it easier for other researchers to understand and reproduce the results.

In addition to the above points, the paper should include a more comprehensive comparison to other optimizers that use multiple momentum terms, such as Lion and RAdam. While the authors mention these optimizers, they do not provide a detailed comparison of their performance and computational cost. A more thorough comparison would help to contextualize the performance of AdEMAMix and highlight its unique advantages and disadvantages. Specifically, the authors should compare AdEMAMix to these optimizers on a range of tasks and model sizes, and they should also analyze the computational overhead of each optimizer. This would provide a more complete picture of the trade-offs between different optimizers and help to identify the scenarios where AdEMAMix is most effective. Furthermore, the paper should include a more detailed analysis of the convergence properties of AdEMAMix. While the authors show that AdEMAMix converges faster than Adam, they do not provide a theoretical analysis of the convergence rate. A more rigorous analysis of the convergence properties of the optimizer would help to understand its theoretical properties and how they relate to its performance in practice. This could involve analyzing the gradient updates and their impact on the loss function, as well as exploring the conditions under which the optimizer is guaranteed to converge to a local minimum.

Finally, the paper should provide a more detailed analysis of the computational overhead of AdEMAMix. While the authors mention that the additional EMA requires additional memory and computation, they do not provide a quantitative analysis of the overhead. It is important to understand the trade-offs between performance gains and computational costs, especially when comparing AdEMAMix to other optimizers. The authors should provide a breakdown of the computational cost of each component of the optimizer, including the gradient computation, the EMA updates, and the parameter updates. This would help to identify the bottlenecks of the optimizer and suggest potential optimizations. Furthermore, the authors should provide a more detailed analysis of the memory requirements of AdEMAMix, including the memory needed to store the two EMAs and the parameters. This would help to understand the scalability of the optimizer and its suitability for large-scale models.

### Questions

- How does AdEMAMix compare to other optimizers that use multiple momentum terms, such as Lion and RAdam?
- What is the computational overhead of AdEMAMix compared to Adam?
- How does the performance of AdEMAMix vary with different learning rates and batch sizes?
- How does AdEMAMix perform on tasks with different data distributions?

### Rating

3

### Confidence

4

**********

## Reviewer 2

### Summary

The paper proposes AdEMAMix, a novel optimization method that combines two exponential moving averages (EMAs) of gradients to improve the training of deep neural networks. The method addresses the limitations of traditional Adam optimizers by allowing for a balance between recent and older gradients, which can lead to faster convergence and better generalization. The authors demonstrate the effectiveness of AdEMAMix through extensive experiments on language modeling and image classification tasks, showing that it outperforms Adam in terms of both training speed and final performance.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

The paper introduces a novel approach to momentum by combining two EMAs, which is a creative and well-motivated idea. The authors provide a clear and concise explanation of the method, making it easy to understand. The experimental results are extensive and demonstrate the effectiveness of AdEMAMix across various tasks and model sizes. The paper also includes detailed ablation studies, which help to understand the impact of different components of the method. Overall, the paper is well-written, and the contributions are significant.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a clear motivation for why using two EMAs is better than using one. The authors claim that one EMA cannot provide sufficient weight to recent gradients, but they do not provide any evidence or theoretical analysis to support this claim. It is not clear why a single EMA with a different hyperparameter setting would not be able to achieve similar results.
2. The paper lacks a detailed analysis of the computational overhead of AdEMAMix. While the authors mention that the additional EMA requires additional memory and computation, they do not provide a quantitative analysis of the overhead. It is important to understand the trade-offs between performance gains and computational costs, especially when comparing AdEMAMix to other optimizers.
3. The paper does not compare AdEMAMix to other optimizers that use multiple momentum terms, such as Lion and RAdam. These optimizers also use multiple momentum terms, but they do not use EMA. It is important to understand how AdEMAMix compares to these optimizers in terms of performance and computational cost.
4. The paper does not provide a clear explanation of how the two EMAs are combined in the update rule. The authors do not explain why they are added together or why this is the optimal way to combine them. It is important to understand the design choices behind the update rule and how they affect the performance of the optimizer.
5. The paper does not provide a detailed analysis of the convergence properties of AdEMAMix. While the authors show that AdEMAMix converges faster than Adam, they do not provide a theoretical analysis of the convergence rate. It is important to understand the theoretical properties of the optimizer and how they relate to its performance in practice.

### Suggestions

The paper would benefit from a more rigorous justification for the use of two EMAs. While the authors claim that a single EMA struggles to balance recent and older gradients, this needs to be supported by either theoretical analysis or empirical evidence. For instance, the authors could analyze the eigenvalue spectrum of the Hessian to show that it has a wide range of scales, which would justify the need for a two-EMA approach. Alternatively, they could conduct experiments with a single EMA, varying the decay rate, to demonstrate that it cannot achieve the same performance as AdEMAMix. Without this, the motivation for the proposed method remains unclear. Furthermore, the authors should provide a more detailed explanation of how the two EMAs are combined in the update rule. Simply adding them together is not necessarily the optimal approach. The authors could explore alternative combination methods, such as weighted averaging or adaptive scaling, and analyze their impact on performance. This would provide a more complete understanding of the design choices behind the optimizer and potentially lead to further improvements.

In addition to the above, the paper should include a more comprehensive comparison to other optimizers that use multiple momentum terms. While the authors mention Lion and RAdam, they do not provide a detailed comparison of their performance and computational cost. A thorough comparison would help to contextualize the performance of AdEMAMix and highlight its unique advantages and disadvantages. For example, the authors could compare AdEMAMix to Lion and RAdam on a range of tasks and model sizes, and they could analyze the computational overhead of each optimizer. This would provide a more complete picture of the trade-offs between different optimizers and help to identify the scenarios where AdEMAMix is most effective. Furthermore, the authors should provide a more detailed analysis of the convergence properties of AdEMAMix. While they show that it converges faster than Adam, they do not provide a theoretical analysis of the convergence rate. A theoretical analysis would help to understand the theoretical properties of the optimizer and how they relate to its performance in practice. For example, the authors could analyze the gradient updates and their impact on the loss function, as well as exploring the conditions under which the optimizer is guaranteed to converge to a local minimum.

Finally, the paper should include a more detailed analysis of the computational overhead of AdEMAMix. While the authors mention that the additional EMA requires additional memory and computation, they do not provide a quantitative analysis of the overhead. It is important to understand the trade-offs between performance gains and computational costs, especially when comparing AdEMAMix to other optimizers. The authors could provide a breakdown of the computational cost of each component of the optimizer, including the gradient computation, the EMA updates, and the parameter updates. This would help to identify the bottlenecks of the optimizer and suggest potential optimizations. Furthermore, the authors should provide a more detailed analysis of the memory requirements of AdEMAMix, including the memory needed to store the two EMAs and the parameters. This would help to understand the scalability of the optimizer and its suitability for large-scale models.

### Questions

1. Can you provide a more detailed explanation of why using two EMAs is better than using one? What is the theoretical or empirical evidence to support this claim?
2. Can you provide a detailed analysis of the computational overhead of AdEMAMix? How does it compare to other optimizers in terms of memory and computation?
3. Can you compare AdEMAMix to other optimizers that use multiple momentum terms, such as Lion and RAdam? How does it perform in terms of performance and computational cost?
4. Can you provide a clear explanation of how the two EMAs are combined in the update rule? Why are they simply added together?
5. Can you provide a detailed analysis of the convergence properties of AdEMAMix? What is the theoretical convergence rate?

### Rating

5

### Confidence

4

**********

## Reviewer 3

### Summary

This paper proposes AdEMAMix, a new optimizer that combines two EMA terms to better leverage past gradients. The authors show that this optimizer improves over AdamW in language modeling and image classification tasks, with faster convergence and better generalization.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow
- The proposed optimizer is simple and intuitive
- The authors provide a lot of empirical evidence to support their claims

### Weaknesses

#### Some Related Works


#### comment

 - The authors do not provide a theoretical analysis of why AdEMAMix works better than AdamW. A theoretical analysis would help to understand the underlying mechanisms of the optimizer and provide insights into its behavior.
- The authors do not provide a detailed analysis of the computational cost of AdEMAMix. While the authors mention that the additional EMA term does not significantly increase the computational cost, it would be helpful to have a more detailed analysis of the memory and time requirements of the optimizer.
- The authors do not provide a comparison with other optimizers that use multiple momentum terms, such as Lion and RAdam. It would be helpful to see how AdEMAMix compares to these optimizers in terms of performance and computational cost.

### Suggestions

The paper would benefit significantly from a more in-depth theoretical analysis of AdEMAMix. While the empirical results are promising, a theoretical justification for why the two-EMA approach is superior to a single EMA would greatly enhance the paper's contribution. Specifically, the authors should explore the convergence properties of AdEMAMix and compare them to those of AdamW. This could involve analyzing the gradient updates and their impact on the loss function. Furthermore, it would be beneficial to investigate the relationship between the two EMA terms and how they interact to achieve better performance. For example, the authors could analyze the eigenvalue spectrum of the Hessian to understand the impact of each EMA term on the optimization landscape. A theoretical analysis would not only provide a deeper understanding of the optimizer but also help to identify potential limitations and areas for further improvement.

In addition to the theoretical analysis, the authors should provide a more detailed analysis of the computational cost of AdEMAMix. While the authors mention that the additional EMA term does not significantly increase the computational cost, it would be helpful to have a more precise analysis of the memory and time requirements of the optimizer. This analysis should include a breakdown of the computational cost of each step in the algorithm, including the gradient computation, the EMA updates, and the parameter updates. Furthermore, the authors should compare the computational cost of AdEMAMix with that of AdamW and other optimizers. This comparison should consider both the training time and the memory usage. It would also be helpful to analyze the scalability of AdEMAMix with respect to the model size and the batch size. This analysis would provide a more complete picture of the practical implications of using AdEMAMix in real-world applications.

Finally, the authors should provide a more comprehensive comparison with other optimizers that use multiple momentum terms, such as Lion and RAdam. While the authors mention these optimizers, they do not provide a detailed comparison of their performance and computational cost. It would be helpful to see how AdEMAMix compares to these optimizers in terms of both training time and final performance. This comparison should include a variety of tasks and model sizes. Furthermore, the authors should discuss the potential advantages and disadvantages of AdEMAMix compared to these other optimizers. This would provide a more complete understanding of the landscape of optimizers and help to position AdEMAMix within this landscape. The authors should also consider including a discussion of the potential limitations of AdEMAMix and areas for future research.

### Questions

- How does AdEMAMix compare to other optimizers that use multiple momentum terms, such as Lion and RAdam?
- Can you provide a theoretical analysis of why AdEMAMix works better than AdamW?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

The paper proposes AdEMAMix, a new optimizer that leverages two exponential moving averages (EMAs) to improve the training of deep neural networks. The authors argue that a single EMA cannot effectively balance the contributions of recent and older gradients, leading to suboptimal performance. AdEMAMix addresses this limitation by combining two EMAs: a fast EMA with a large decay rate and a slow EMA with a small decay rate. The fast EMA captures recent gradient information, while the slow EMA retains information from older gradients. The two EMAs are combined linearly, with the fast EMA having a larger weight. The authors demonstrate the effectiveness of AdEMAMix through experiments on language modeling and image classification tasks, showing that it outperforms AdamW in terms of both training speed and final performance. The paper also highlights the benefits of AdEMAMix in terms of faster convergence and improved generalization.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow. The authors clearly explain the motivation behind AdEMAMix and provide a detailed description of the method. The experimental setup is well-defined, and the results are presented in a clear and concise manner. The paper also includes a thorough discussion of the limitations of the proposed method and potential areas for future research.

2. The proposed method is simple and easy to implement. The authors provide a clear and concise algorithm for AdEMAMix, which can be readily adopted by other researchers. The method does not require significant modifications to existing codebases, making it accessible to a wide range of users.

3. The paper provides a comprehensive evaluation of AdEMAMix on a variety of tasks, including language modeling and image classification. The experiments are well-designed and demonstrate the effectiveness of the proposed method. The authors also provide a detailed analysis of the results, highlighting the strengths and limitations of AdEMAMix.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a theoretical analysis of the convergence properties of AdEMAMix. While the empirical results are promising, a theoretical analysis would provide a deeper understanding of the method's behavior and limitations. Specifically, it would be beneficial to analyze the conditions under which AdEMAMix converges to a local minimum, and how the choice of the two EMA parameters affects this convergence. Furthermore, the paper lacks a discussion on the potential for oscillations or divergence, especially when the fast EMA is heavily weighted compared to the slow EMA.

2. The paper does not explore the sensitivity of AdEMAMix to different hyperparameters. While the authors provide some analysis of the impact of the EMA parameters, a more comprehensive sensitivity analysis would be beneficial. This should include a systematic exploration of the learning rate, batch size, and other relevant hyperparameters, to determine the robustness of the method and identify optimal settings for different tasks. The paper should also discuss the potential for overfitting when using AdEMAMix, and how to mitigate this risk.

3. The paper does not compare AdEMAMix with other optimizers that use multiple momentum terms, such as Lion and RAdam. While the authors mention these optimizers, they do not provide a detailed comparison of their performance and computational cost. A more thorough comparison would help to contextualize the contributions of AdEMAMix and highlight its unique advantages and disadvantages. Specifically, it would be useful to see how AdEMAMix performs against these optimizers in terms of training time, memory usage, and generalization performance.

### Suggestions

The paper would benefit from a more rigorous theoretical analysis of AdEMAMix's convergence properties. While empirical results are valuable, a theoretical framework would provide a deeper understanding of the method's behavior. Specifically, the authors should investigate the conditions under which AdEMAMix converges to a local minimum, and how the choice of the two EMA parameters affects this convergence. This analysis should consider the interaction between the fast and slow EMAs, and how their combined effect influences the optimization landscape. Furthermore, the authors should explore the potential for oscillations or divergence, especially when the fast EMA is heavily weighted compared to the slow EMA. This could involve analyzing the eigenvalues of the Hessian matrix or using techniques from dynamical systems theory to understand the stability of the optimization process. A theoretical analysis would also help to identify the limitations of the method and guide future research directions.

To address the lack of sensitivity analysis, the authors should conduct a more comprehensive study of AdEMAMix's hyperparameter robustness. This should include a systematic exploration of the learning rate, batch size, and other relevant hyperparameters, to determine the optimal settings for different tasks. The authors should also investigate the potential for overfitting when using AdEMAMix, and how to mitigate this risk. This could involve using techniques such as early stopping, regularization, or dropout. Furthermore, the authors should provide practical guidelines for tuning the hyperparameters of AdEMAMix, based on their experimental findings. This would make the method more accessible to other researchers and facilitate its adoption in practice. The sensitivity analysis should also consider the interaction between different hyperparameters, to identify potential conflicts or synergies.

Finally, the paper should include a more detailed comparison of AdEMAMix with other optimizers that use multiple momentum terms, such as Lion and RAdam. This comparison should include a thorough evaluation of their performance and computational cost, in terms of training time, memory usage, and generalization performance. The authors should also discuss the potential advantages and disadvantages of AdEMAMix compared to these optimizers, and identify the specific scenarios where AdEMAMix is most effective. This comparison should be based on a variety of tasks and datasets, to ensure the generalizability of the findings. The authors should also consider the potential for combining AdEMAMix with other optimization techniques, such as adaptive learning rate methods or second-order optimization algorithms, to further improve its performance.

### Questions

1. How does the choice of the two EMA parameters affect the convergence properties of AdEMAMix? Are there any theoretical guarantees for the convergence of the method?

2. How sensitive is AdEMAMix to different hyperparameters, such as the learning rate, batch size, and other relevant parameters? Are there any practical guidelines for tuning these hyperparameters?

3. How does AdEMAMix compare to other optimizers that use multiple momentum terms, such as Lion and RAdam? Are there any specific scenarios where AdEMAMix is expected to outperform these optimizers?

### Rating

6

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers for the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

**Plan:**
1. Go through each reviewer's comments one by one.
2. For each comment identified as a weakness, find the corresponding section in the paper.
3. Extract evidence (quotes, experimental details, missing citations) to support the reviewer's claim.
4. If the weakness is about missing information, confirm that the information is indeed absent.
5. If there are conflicting opinions, note them down.
6. Finally, summarize the findings for each weakness, stating if it's valid, partially valid, or invalid, along with the confidence level and key evidence.
**Review 1 Weaknesses:**

1. Weakness Statement:
"The paper does not provide a clear motivation for why using two EMAs is better than using one. The authors claim that one EMA cannot provide sufficient weight to recent gradients, but they do not provide any evidence or theoretical analysis to support this claim. It is not clear why a single EMA with a different hyperparameter setting would not be able to achieve similar results."

2. Evidence Collection:
a) Method-related Evidence:
   - "The use of a single EMA can lead to a loss of information from older gradients, which can hinder the model's ability to adapt to new information. This is because the EMA decays the influence of older gradients over time, making it difficult to retain information from the distant past." (Motivation section)
   - "For this reason, we propose AdEMAMix, which balances the importance of recent and distant gradients." (Motivation section)
   - "The proposed method, AdEMAMix, addresses this limitation by combining two EMA terms: a fast EMA with a large decay rate (β3) and a slow EMA with a small decay rate (β1)." (Method: Overview)
   - "The fast EMA captures recent gradient information, while the slow EMA retains information from older gradients." (Method: Overview)
   - "To prevent the bias induced by the initial β1 = 0, we progressively increase the values of β3 and α in AdEMAMix." (Method: Scheduler)
   - "We find α ∈ [ 4 , 10 ] \alpha\in[4,10] to work well in practice." (Method: Scheduler)
   - "We show in App. C.1.6 that using β1 = 0 \beta_1 = 0 initially works well, at the cost of potentially less stable training." (Method: Scheduler)

b) Experiment-related Evidence:
   - The paper shows improved performance with AdEMAMix compared to AdamW, suggesting the two-EMA approach is beneficial. However, it doesn't directly compare against a single EMA with varying decay rates.

3. Literature Gap Analysis:
   - The paper cites works that use EMAs (Polyak, 1964; Nesterov, 1983) but doesn't provide a theoretical justification for why two EMAs are superior to one in this specific context.

4. Validation Analysis:
   - The paper motivates the use of two EMAs by stating that a single EMA can lose information from older gradients. While this is a reasonable intuition, the paper lacks a formal theoretical analysis or empirical evidence (through ablation studies) to definitively prove that a single EMA cannot achieve similar performance with optimal hyperparameter tuning. The authors mention progressively increasing the values of β3 and α, which implicitly explores different single EMA scenarios, but a direct comparison is missing.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper states the limitation of a single EMA but doesn't provide theoretical or direct empirical evidence to support the claim that two EMAs are inherently better.

1. Weakness Statement:
"The paper lacks a detailed analysis of the computational overhead of AdEMAMix. While the authors mention that the additional EMA requires additional memory and computation, they do not provide a quantitative analysis of the overhead. It is important to understand the trade-offs between performance gains and computational costs, especially when comparing AdEMAMix to other optimizers."

2. Evidence Collection:
a) Method-related Evidence:
   - "To keep a high sensitivity to recent gradients, while also incorporating information from older gradients, we add a second EMA (changes compared to AdamW are in Blue): { γ 1 = [ γ 1 + β 2 γ 2 ] / [ 1 − β 2 ] , γ 2 = [ γ 2 + β 3 γ 3 ] / [ 1 − β 3 ] , γ 3 = [ γ 3 + β 2 γ 4 ] , γ 4 = [ γ 4 + λ γ 4 ] ." (Method: AdEMAMix)
   - "In our experiments, while the values of β 1 , β 2 \beta_1, \beta_2 are kept similar to those of equation AdamW , we often use β 3 = 0 . 9999 \beta_3 = 0.9999 . We find α ∈ [ 4 , 10 ] \alpha\in[4,10] to work well in practice." (Method: Scheduler)

b) Experiment-related Evidence:
   - "In Fig. 5(a) we plot the time required to train our 110 110 M and 1.3 1.3 B parameter models for 256 256k iterations. We observe that the impact of using an additional EMA on the training speed is negligible. If we were to train new models with a fix time budget, the extra iterations of the baseline would not be sufficient to close the gap." (Experiments: Results: Training Speed Comparison)
   - "Moreover—when considering larger distributed setups—it is worth noting that AdEMAMix is not increasing communication (gradient reduction) over Adam. Therefore, we expect the runtime overhead of AdEMAMix to shrink in those settings, as data movements occupy a larger fraction of the total runtime." (Experiments: Results: Training Speed Comparison)

3. Literature Gap Analysis:
   - The paper mentions the increased memory cost of AdEMAMix: "We believe this issue is of lesser consequences as Fully-Sharded-Data-Parallel (FSDP) can always be used to distribute the optimizer states across compute nodes. In the cases where memory remains an issue, one mitigation strategy could be to apply factorization strategies as in Shazeer & Stern (2018) ; Zhao et al. (2020)." (Conclusion)

4. Validation Analysis:
   - The paper acknowledges the increased memory requirements due to the additional EMA. It also provides a qualitative analysis of the training time overhead, stating it's negligible in most scenarios and even shrinking in larger distributed setups. However, it lacks a quantitative analysis of the computational cost in terms of FLOPs or a detailed breakdown of memory usage.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper mentions increased memory and provides a qualitative analysis of training time, but lacks a quantitative computational overhead analysis.

1. Weakness Statement:
"The paper does not compare AdEMAMix to other optimizers that use multiple momentum terms, such as Lion and RAdam. These optimizers also use multiple momentum terms, but they do not use EMA. It is important to understand how AdEMAMix compares to these optimizers in terms of performance and computational cost."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper focuses on the EMA-based approach and doesn't discuss or compare with optimizers like Lion or RAdam.

b) Experiment-related Evidence:
   - The baselines used are AdamW and AdEMAMix itself. There are no experiments comparing AdEMAMix to Lion or RAdam.

3. Literature Gap Analysis:
   - The Related Work section mentions Lion but doesn't provide a detailed comparison of its mechanisms or performance against AdEMAMix.

4. Validation Analysis:
   - The paper's experimental section only includes AdamW as a baseline. While Lion is mentioned in the related work, there's no empirical comparison to assess the relative performance and computational cost of AdEMAMix.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The experimental section lacks a comparison with optimizers like Lion and RAdam.

1. Weakness Statement:
"The paper does not provide a clear explanation of how the two EMAs are combined in the update rule. The authors do not explain why they are added together or why this is the optimal way to combine them. It is important to understand the design choices behind the update rule and how they affect the performance of the optimizer."

2. Evidence Collection:
a) Method-related Evidence:
   - "The final weight update is then computed as: { m ^ 1 ( t ) = β 1 m 1 ( t − 1 ) + ( 1 − β 1 ) m g ( t ) , m ^ 2 ( t ) = β 3 m 2 ( t − 1 ) + ( 1 − β 3 ) m g ( t ) , m ^ ( t ) = β 2 m ^ 1 ( t ) + ( 1 − β 2 ) m ^ 2 ( t ) , m ( t ) = m ^ ( t ) + γ ( g ^ 1 ( t ) + α m ^ 2 ( t ) ) ." (Method: AdEMAMix)
   - "With Tackling early training instabilities. Early training instabilities are commonplace when training deep models, and empirically motivated the introduction of methods such as learning rate warmup and gradient clipping. Gilmer et al. (2022) show how the use of learning rate warmup can be justified from a curvature perspective; allowing the iterates to move to parts of the optimization landscape where larger learning rates are stable. While we use learning rate warmup in all our experiments, we still noticed AdEMAMix models using a large β 3 \beta_3 \ would diverge early. This, despite not using bias correction over γ 2 \gamma_2 . Moreover—when considering larger distributed setups—we expect the runtime overhead of AdEMAMix to shrink in those settings, as data movements occupy a larger fraction of the total runtime. A more significant overhead is in terms of memory when β 1 ≠ 0 \beta_1 \neq 0 . We show in App. C.1.4 that using β 1 = 0 \beta_1 = 0 often works, at the cost of potentially less stable training." (Method: Scheduler)

4. Validation Analysis:
   - The paper explicitly states that the two EMAs are added together in the update rule. It also provides a brief explanation for this design choice, linking it to the need to balance recent and older gradients. However, it doesn't delve into why this specific combination is optimal or explore alternative combination methods.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper shows the addition of the two EMAs in the update rule and provides a brief justification, but lacks a detailed explanation of why this is the optimal approach.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the convergence properties of AdEMAMix. While the authors show that AdEMAMix converges faster than AdamW, they do not provide a theoretical analysis of the convergence rate. It is important to understand the theoretical properties of the optimizer and how they relate to its performance in practice. This could involve analyzing the gradient updates and their impact on the loss function, as well as exploring the conditions under which the optimizer is guaranteed to converge to a local minimum."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper focuses on the practical performance of AdEMAMix and doesn't include a formal convergence analysis.

b) Experiment-related Evidence:
   - The paper shows faster convergence in terms of training loss and validation loss, but lacks a theoretical analysis of the convergence rate.

3. Literature Gap Analysis:
   - The paper doesn't cite theoretical works on the convergence of optimizers with multiple EMAs.

4. Validation Analysis:
   - The paper primarily presents empirical evidence of faster convergence. It lacks a theoretical analysis of the convergence properties of AdEMAMix, such as deriving convergence rates or proving convergence under certain conditions.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper lacks a theoretical analysis of the convergence properties of AdEMAMix.

**Review 2 Weaknesses:**

1. Weakness Statement:
"The paper does not provide a clear motivation for why using two EMAs is better than using one. The authors claim that one EMA cannot provide sufficient weight to recent gradients, but they do not provide any evidence or theoretical analysis to support this claim. It is not clear why a single EMA with a different hyperparameter setting would not be able to achieve similar results."

2. Evidence Collection:
   - This is the same weakness as identified by Reviewer 1. Please see the analysis for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1.

1. Weakness Statement:
"The paper lacks a detailed analysis of the computational overhead of AdEMAMix. While the authors mention that the additional EMA requires additional memory and computation, they do not provide a quantitative analysis of the overhead. It is important to understand the trade-offs between performance gains and computational costs, especially when comparing AdEMAMix to other optimizers."

2. Evidence Collection:
   - This is the same weakness as identified by Reviewer 1. Please see the analysis for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1.

1. Weakness Statement:
"The paper does not compare AdEMAMix to other optimizers that use multiple momentum terms, such as Lion and RAdam. While the authors mention these optimizers, they do not provide a detailed comparison of their performance and computational cost. A more thorough comparison would help to contextualize the contributions of AdEMAMix and highlight its unique advantages and disadvantages. Specifically, it would be useful to see how AdEMAMix compares to these optimizers in terms of both training time and final performance."

2. Evidence Collection:
   - This is the same weakness as identified by Reviewer 1. Please see the analysis for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1.

1. Weakness Statement:
"The paper does not provide a clear explanation of how the two EMAs are combined in the update rule. The authors do not explain why they are added together or why this is the optimal way to combine them. It is important to understand the design choices behind the update rule and how they affect the performance of the optimizer."

2. Evidence Collection:
   - This is the same weakness as identified by Reviewer 1. Please see the analysis for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the convergence properties of AdEMAMix. While the authors show that AdEMAMix converges faster than AdamW, they do not provide a theoretical analysis of the convergence rate. It is important to understand the theoretical properties of the optimizer and how they relate to its performance in practice. This could involve analyzing the gradient updates and their impact on the loss function, as well as exploring the conditions under which the optimizer is guaranteed to converge to a local minimum."

2. Evidence Collection:
   - This is the same weakness as identified by Reviewer 1. Please see the analysis for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1.

4. Validation Analysis:
   - Same as Reviewer 1.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1.

**Review 3 Weaknesses:**

1. Weakness Statement:
"The authors do not provide a theoretical analysis of why AdEMAMix works better than AdamW. A theoretical analysis would help to understand the underlying mechanisms of the optimizer and provide insights into its behavior."

2. Evidence Collection:
   - This is the same weakness as identified by Reviewer 1 and Reviewer 2. Please see the analysis for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1 and Reviewer 2.

4. Validation Analysis:
   - Same as Reviewer 1 and Reviewer 2.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1 and Reviewer 2.

1. Weakness Statement:
"The authors do not provide a detailed analysis of the computational cost of AdEMAMix. While the authors mention that the additional EMA requires additional memory and computation, they do not provide a quantitative analysis of the overhead. It is important to understand the trade-offs between performance gains and computational costs, especially when comparing AdEMAMix to other optimizers."

2. Evidence Collection:
   - This is the same weakness as identified by Reviewer 1 and Reviewer 2. Please see the analysis for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1 and Reviewer 2.

4. Validation Analysis:
   - Same as Reviewer 1 and Reviewer 2.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1 and Reviewer 2.

1. Weakness Statement:
"The authors do not compare AdEMAMix to other optimizers that use multiple momentum terms, such as Lion and RAdam. While the authors mention these optimizers, they do not provide a detailed comparison of their performance and computational cost. A more thorough comparison would help to contextualize the contributions of AdEMAMix and highlight its unique advantages and disadvantages. Specifically, it would be useful to see how AdEMAMix performs against these optimizers in terms of both training time and final performance."

2. Evidence Collection:
   - This is the same weakness as identified by Reviewer 1, Reviewer 2, and Reviewer 4. Please see the analysis for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1, Reviewer 2, and Reviewer 4.

4. Validation Analysis:
   - Same as Reviewer 1, Reviewer 2, and Reviewer 4.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1, Reviewer 2, and Reviewer 4.

1. Weakness Statement:
"The paper does not provide a clear explanation of how the two EMAs are combined in the update rule. The authors do not explain why they are added together or why this is the optimal way to combine them. It is important to understand the design choices behind the update rule and how they affect the performance of the optimizer."

2. Evidence Collection:
   - This is the same weakness as identified by Reviewer 1, Reviewer 2, and Reviewer 4. Please see the analysis for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1, Reviewer 2, and Reviewer 4.

4. Validation Analysis:
   - Same as Reviewer 1, Reviewer 2, and Reviewer 4.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1, Reviewer 2, and Reviewer 4.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the convergence properties of AdEMAMix. While the authors show that AdEMAMix converges faster than AdamW, they do not provide a theoretical analysis of the convergence rate. It is important to understand the theoretical properties of the optimizer and how they relate to its performance in practice. This could involve analyzing the gradient updates and their impact on the loss function, as well as exploring the conditions under which the optimizer is guaranteed to converge to a local minimum."

2. Evidence Collection:
   - This is the same weakness as identified by Reviewer 1, Reviewer 2, and Reviewer 4. Please see the analysis for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 1, Reviewer 2, and Reviewer 4.

4. Validation Analysis:
   - Same as Reviewer 1, Reviewer 2, and Reviewer 4.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1, Reviewer 2, and Reviewer 4.

**Review 4 Weaknesses:**

1. Weakness Statement:
"The paper does not provide a theoretical analysis of why AdEMAMix works better than AdamW. A theoretical analysis would help to understand the underlying mechanisms of the optimizer and provide insights into its behavior."

2. Evidence Collection:
   - This is the same weakness as identified by Reviewer 3. Please see the analysis for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 3.

4. Validation Analysis:
   - Same as Reviewer 3.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 3.

1. Weakness Statement:
"The authors do not provide a detailed analysis of the computational cost of AdEMAMix. While the authors mention that the additional EMA requires additional memory and computation, they do not provide a quantitative analysis of the overhead. It is important to understand the trade-offs between performance gains and computational costs, especially when comparing AdEMAMix to other optimizers."

2. Evidence Collection:
   - This is the same weakness as identified by Reviewer 3. Please see the analysis for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 3.

4. Validation Analysis:
   - Same as Reviewer 3.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 3.

1. Weakness Statement:
"The authors do not compare AdEMAMix to other optimizers that use multiple momentum terms, such as Lion and RAdam. While the authors mention these optimizers, they do not provide a detailed comparison of their performance and computational cost. A more thorough comparison would help to contextualize the contributions of AdEMAMix and highlight its unique advantages and disadvantages. Specifically, it would be useful to see how AdEMAMix performs against these optimizers in terms of both training time and final performance."

2. Evidence Collection:
   - This is the same weakness as identified by Reviewer 4. Please see the analysis for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 4.

4. Validation Analysis:
   - Same as Reviewer 4.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 4.

1. Weakness Statement:
"The paper does not provide a clear explanation of how the two EMAs are combined in the update rule. The authors do not explain why they are added together or why this is the optimal way to combine them. It is important to understand the design choices behind the update rule and how they affect the performance of the optimizer."

2. Evidence Collection:
   - This is the same weakness as identified by Reviewer 4. Please see the analysis for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 4.

4. Validation Analysis:
   - Same as Reviewer 4.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 4.

1. Weakness Statement:
"The paper does not provide a detailed analysis of the convergence properties of AdEMAMix. While the authors show that AdEMAMix converges faster than AdamW, they do not provide a theoretical analysis of the convergence rate. It is important to understand the theoretical properties of the optimizer and how they relate to its performance in practice. This could involve analyzing the gradient updates and their impact on the loss function, as well as exploring the conditions under which the optimizer is guaranteed to converge to a local minimum."

2. Evidence Collection:
   - This is the same weakness as identified by Reviewer 4. Please see the analysis for that point.

3. Literature Gap Analysis:
   - Same as Reviewer 4.

4. Validation Analysis:
   - Same as Reviewer 4.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 4.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces AdEMAMix, a novel optimization algorithm that extends the AdamW optimizer by incorporating two exponential moving averages (EMAs) of gradients, aiming to balance the contributions of recent and older gradients. The core idea is that a single EMA, particularly one with a high decay rate, may not effectively capture information from distant past gradients, leading to suboptimal performance. AdEMAMix addresses this by using a fast EMA with a large decay rate to capture recent gradient information and a slow EMA with a small decay rate to retain information from older gradients. These two EMAs are then combined linearly, with the fast EMA having a larger weight. The authors motivate this approach by arguing that a single EMA tends to lose information from older gradients over time, which can hinder the model's ability to adapt to new information. They demonstrate the effectiveness of AdEMAMix through extensive experiments on language modeling and image classification tasks, showing that it outperforms AdamW in terms of both training speed and final performance. The empirical results are compelling, with AdEMAMix achieving faster convergence and better generalization across various model sizes and datasets. The authors also explore the impact of different hyperparameters, such as the decay rates of the EMAs and the learning rate, and provide ablation studies to understand the contribution of each component of AdEMAMix. They further investigate the sensitivity of the method to different learning rates and batch sizes. The paper also includes a discussion of the computational overhead of AdEMAMix, noting that it requires additional memory and computation compared to AdamW, but that this overhead is negligible in most scenarios and shrinks in larger distributed setups. Overall, the paper presents a well-motivated and empirically validated approach to improving the performance of AdamW by incorporating a dual-EMA mechanism. The authors provide a clear and concise explanation of the method, along with detailed experimental results and ablation studies, making the paper accessible and easy to follow. The work is significant because it offers a simple yet effective way to improve the training of deep neural networks, with potential applications in various domains.


## Soundness:

2.75


## Presentation:

2.75


## Contribution:

2.75


## Strengths:

The primary strength of this paper lies in its introduction of a simple yet effective modification to the AdamW optimizer, AdEMAMix, which leverages two exponential moving averages to capture both recent and older gradient information. This approach is well-motivated, addressing a potential limitation of the single EMA used in AdamW. The authors provide a clear and concise explanation of the method, making it easy to understand and implement. The experimental results are comprehensive, covering a range of tasks and model sizes, and consistently demonstrate the superiority of AdEMAMix over AdamW. The paper also includes detailed ablation studies, which help to understand the impact of different hyperparameters and the contribution of each component of AdEMAMix. The authors also explore the sensitivity of the method to different learning rates and batch sizes, providing valuable insights into the robustness of the approach. Furthermore, the paper acknowledges the computational overhead of AdEMAMix and provides a qualitative analysis of its impact, showing that it is negligible in most scenarios and shrinks in larger distributed setups. The paper is well-written and easy to follow, making it accessible to a wide audience. The authors also provide a clear explanation of the scheduler used to adjust the decay rates of the EMAs, which is crucial for the performance of the method. The paper's contributions are significant, offering a simple yet effective way to improve the training of deep neural networks, with potential applications in various domains. The authors also provide a detailed analysis of the results, which is crucial for understanding the behavior of the optimizer. The paper also includes a discussion of the limitations of the proposed method and potential areas for future research, which is a sign of good scientific practice. The authors also provide a clear and concise explanation of the method, along with detailed experimental results and ablation studies, making the paper accessible and easy to follow. The paper's contributions are significant, offering a simple yet effective way to improve the training of deep neural networks, with potential applications in various domains.


## Weaknesses:

Despite the strengths of the paper, several weaknesses warrant careful consideration. A primary concern is the lack of a rigorous theoretical justification for the use of two EMAs. While the authors motivate their approach by arguing that a single EMA cannot effectively capture both recent and older gradient information, they do not provide a formal analysis or empirical evidence to support this claim. Specifically, the paper lacks a theoretical analysis or a direct comparison against a single EMA with varying decay rates to definitively prove that a single EMA cannot achieve similar performance with optimal hyperparameter tuning. The authors claim that a single EMA 'cannot provide sufficient weight to recent gradients,' but this claim is not supported by either theoretical analysis or empirical evidence. This absence of a theoretical foundation weakens the motivation for the proposed method and leaves open the possibility that a single EMA with a carefully chosen hyperparameter could achieve similar results. The paper also lacks a detailed analysis of the computational overhead of AdEMAMix. While the authors mention that the additional EMA requires additional memory and computation, they do not provide a quantitative analysis of the overhead. It is important to understand the trade-offs between performance gains and computational costs, especially when comparing AdEMAMix to other optimizers. The paper provides a qualitative analysis of the training time overhead, stating that it is negligible in most scenarios and shrinks in larger distributed setups, but it lacks a precise analysis of the memory and time requirements of AdEMAMix, including a breakdown of the computational cost of each step in the algorithm, including the gradient computation, the EMA updates, and the parameter updates. This lack of a detailed analysis makes it difficult to assess the practical implications of using AdEMAMix in resource-constrained environments. Furthermore, the paper does not provide a detailed comparison of AdEMAMix with other optimizers that use multiple momentum terms, such as Lion and RAdam. While the authors mention these optimizers, they do not provide a detailed comparison of their performance and computational cost. This lack of a thorough comparison makes it difficult to contextualize the contributions of AdEMAMix and highlight its unique advantages and disadvantages. The paper's experimental section only includes AdamW as a baseline, and while Lion is mentioned in the related work, there's no empirical comparison to assess the relative performance and computational cost of AdEMAMix. This lack of comparison limits the paper's ability to demonstrate the unique advantages of AdEMAMix over other optimizers that use multiple momentum terms. The paper also lacks a clear explanation of how the two EMAs are combined in the update rule. While the authors state that the two EMAs are added together, they do not explain why this is the optimal way to combine them or explore alternative combination methods. The authors do not provide a detailed explanation of the design choices behind the update rule and how they affect the performance of the optimizer. Finally, the paper does not provide a detailed analysis of the convergence properties of AdEMAMix. While the authors show that AdEMAMix converges faster than AdamW, they do not provide a theoretical analysis of the convergence rate. It is important to understand the theoretical properties of the optimizer and how they relate to its performance in practice. This could involve analyzing the gradient updates and their impact on the loss function, as well as exploring the conditions under which the optimizer is guaranteed to converge to a local minimum. The paper primarily presents empirical evidence of faster convergence, but lacks a theoretical analysis of the convergence properties of AdEMAMix, such as deriving convergence rates or proving convergence under certain conditions. This lack of a theoretical analysis limits the paper's ability to provide a deeper understanding of the optimizer's behavior and its theoretical properties.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should provide a more rigorous theoretical justification for the use of two EMAs. This could involve analyzing the eigenvalue spectrum of the Hessian to understand the impact of each EMA term on the optimization landscape. Alternatively, they could conduct experiments with a single EMA, varying the decay rate, to demonstrate that it cannot achieve the same performance as AdEMAMix. This would help to isolate the specific benefits of using two EMAs and justify the added complexity. Second, the authors should provide a more detailed analysis of the computational overhead of AdEMAMix. This analysis should include a breakdown of the computational cost of each step in the algorithm, including the gradient computation, the EMA updates, and the parameter updates. This would help to identify the bottlenecks of the optimizer and suggest potential optimizations. Furthermore, the authors should provide a more detailed analysis of the memory requirements of AdEMAMix, including the memory needed to store the two EMAs and the parameters. This would help to understand the scalability of the optimizer and its suitability for large-scale models. Third, the authors should include a more comprehensive comparison to other optimizers that use multiple momentum terms, such as Lion and RAdam. This comparison should include a detailed analysis of their performance and computational cost. This would help to contextualize the contributions of AdEMAMix and highlight its unique advantages and disadvantages. Specifically, the authors should compare AdEMAMix to Lion and RAdam on a range of tasks and model sizes, and they should also analyze the computational overhead of each optimizer. This would provide a more complete picture of the trade-offs between different optimizers and help to identify the scenarios where AdEMAMix is most effective. Fourth, the authors should provide a more detailed explanation of how the two EMAs are combined in the update rule. This should include a discussion of alternative combination methods and their potential impact on performance. This would help to clarify the design choices behind the optimizer and provide a more complete understanding of its behavior. Fifth, the authors should provide a more detailed analysis of the convergence properties of AdEMAMix. This could involve analyzing the gradient updates and their impact on the loss function, as well as exploring the conditions under which the optimizer is guaranteed to converge to a local minimum. This analysis could also involve investigating the eigenvalue spectrum of the Hessian to understand the impact of each EMA term on the optimization landscape. A theoretical analysis would not only provide a deeper understanding of the optimizer but also help to identify potential limitations and areas for further improvement. Finally, the authors should provide a more detailed analysis of the sensitivity of AdEMAMix to different hyperparameters, such as the learning rate, batch size, and other relevant parameters. This should include a systematic exploration of the learning rate and batch size, to determine the optimal settings for different tasks. The authors should also investigate the potential for overfitting when using AdEMAMix, and how to mitigate this risk. This could involve using techniques such as early stopping, regularization, or dropout. Furthermore, the authors should provide a more detailed analysis of the memory requirements of AdEMAMix, including the memory needed to store the two EMAs and the parameters. This would help to understand the scalability of the optimizer and its suitability for large-scale models.


## Questions:

Several key questions remain after my analysis of this paper. First, can the authors provide a more detailed explanation of why using two EMAs is better than using one? What is the theoretical or empirical evidence to support this claim? Specifically, why is a single EMA unable to capture both recent and older gradient information effectively? Second, can the authors provide a detailed analysis of the computational overhead of AdEMAMix? How does it compare to other optimizers in terms of memory and computation? What is the precise breakdown of the computational cost of each step in the algorithm? Third, can the authors provide a clear explanation of how the two EMAs are combined in the update rule? Why are they added together, and why is this the optimal way to combine them? Are there any other combination methods that could be explored? Fourth, can the authors provide a detailed analysis of the convergence properties of AdEMAMix? What is the theoretical convergence rate, and what are the conditions under which the optimizer is guaranteed to converge to a local minimum? Fifth, can the authors provide a more detailed comparison of AdEMAMix with other optimizers that use multiple momentum terms, such as Lion and RAdam? How does it perform in terms of performance and computational cost? What are the specific scenarios where AdEMAMix is expected to outperform these optimizers? Sixth, can the authors provide a more detailed analysis of the sensitivity of AdEMAMix to different hyperparameters, such as the learning rate, batch size, and other relevant parameters? Are there any practical guidelines for tuning these hyperparameters? Finally, can the authors provide a more detailed analysis of the potential for overfitting when using AdEMAMix, and how to mitigate this risk? These questions target the core methodological choices and assumptions of the paper, and addressing them would significantly strengthen the paper's contributions.


## Rating:

5.0


## Confidence:

3.5


## Decision:

Reject
}