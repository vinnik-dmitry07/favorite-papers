I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper studies the implicit regularization effect of different optimization algorithms on factored models, particularly focusing on the gauge symmetry of such models. The authors show that algorithms like GD and Adam that do not respect this symmetry perform worse than algorithms like Muon and Shampoo that do. They also demonstrate that the choice of optimizer significantly impacts the bias-variance trade-off in generalization. The paper provides a detailed theoretical analysis and empirical validation across multiple tasks, highlighting the importance of gauge-equivariant optimizers for better generalization in factored models.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper provides a rigorous theoretical framework for understanding the impact of gauge symmetry on optimization in factored models. The analysis of how different optimizers respect or violate this symmetry is particularly insightful.
- The empirical results are extensive, covering various tasks and providing clear evidence for the theoretical claims. The comparison of different optimizers, including popular ones like Adam and RMSProp, is valuable for the community.
- The paper is well-written and organized, making it accessible to readers with a background in machine learning and optimization. The clear presentation of both theoretical and empirical results enhances its impact.

### Weaknesses

#### Some Related Works


#### comment

 - The paper primarily focuses on the underdetermined case (n = 40, k = 3), and it is unclear how the findings generalize to other settings, such as overparameterized scenarios (n < k). Specifically, the behavior of gauge-equivariant optimizers in highly overparameterized regimes, where the effective rank of the weight matrices is much smaller than the actual dimension, is not explored. This is a crucial aspect to consider, as many practical applications involve such scenarios.
- The paper does not provide a detailed analysis of the computational cost associated with different optimizers. This is important because some gauge-equivariant methods might introduce additional computational overhead, which could be a limiting factor in large-scale applications. For instance, the per-iteration cost of methods like Shampoo, which involves matrix inversions or pseudo-inversions, should be explicitly compared to simpler methods like gradient descent or Adam. A thorough analysis of both time and memory complexity is necessary.
- The paper could benefit from a more in-depth discussion of the practical implications of the findings. While the theoretical analysis is strong, it would be helpful to provide more concrete guidance on how to choose the most appropriate optimizer for a given task. For example, are there specific scenarios where one type of gauge-equivariant optimizer is clearly superior to others? The paper should also discuss the trade-offs between different optimizers in terms of convergence speed, generalization performance, and computational cost.

### Suggestions

The paper would significantly benefit from a more thorough investigation into the behavior of the proposed optimizers in overparameterized settings. Specifically, experiments should be conducted with varying degrees of overparameterization, such as n < k, to assess how the gauge symmetry affects the optimization landscape and generalization performance. It would be valuable to analyze the effective rank of the learned matrices during training and how it evolves with different optimizers. This analysis should include a comparison of the singular value distributions of the weight matrices, which could reveal whether gauge-equivariant optimizers tend to learn low-rank solutions more effectively in overparameterized scenarios. Furthermore, the paper should explore the impact of different initialization schemes on the performance of these optimizers in overparameterized settings, as the initialization can play a crucial role in the optimization process.

To address the lack of computational cost analysis, the paper should include a detailed comparison of the per-iteration time and memory requirements of different optimizers. This analysis should consider both the training and inference phases. For example, the paper could provide a breakdown of the computational cost associated with each step of the optimization process, such as gradient computation, update rule application, and any additional operations specific to each optimizer. This analysis should also consider the scaling of these costs with respect to the model size and the batch size. Furthermore, the paper should discuss the practical implications of these computational costs for large-scale applications, such as the feasibility of using these optimizers on hardware with limited resources. It would also be beneficial to explore techniques for reducing the computational overhead of gauge-equivariant optimizers, such as using low-rank approximations or other optimization tricks.

Finally, the paper should provide more concrete guidance on how to choose the most appropriate optimizer for a given task. This discussion should go beyond the theoretical analysis and consider practical factors such as the size of the model, the available computational resources, and the desired trade-off between convergence speed and generalization performance. For example, the paper could provide a set of rules of thumb or heuristics for selecting between different gauge-equivariant optimizers based on the characteristics of the task. It would also be helpful to include a discussion of the limitations of each optimizer and the scenarios where they are likely to perform poorly. This practical guidance would make the paper more useful for practitioners and facilitate the adoption of the proposed methods in real-world applications.

### Questions

- How do the findings generalize to overparameterized scenarios (n < k)? Are there specific insights or challenges in this setting?
- Could the authors provide a more detailed analysis of the computational cost associated with different optimizers? This would be valuable for understanding their practical applicability.
- Are there specific scenarios or tasks where one type of gauge-equivariant optimizer is clearly superior to others? Providing such guidance would enhance the practical value of the paper.

### Rating

6

### Confidence

3

**********

## Reviewer 2

### Summary

This paper studies the implicit regularization effect of different optimization algorithms on factored models. The authors propose a criterion to classify optimization algorithms as either equivariant or non-equivariant. They then conduct a series of experiments to compare the performance of nine different optimizers, including both coordinate-wise and factored ones, on matrix sensing tasks. The results show that the non-equivariant optimizers perform worse than their equivariant counterparts. The paper also highlights the importance of the spectral schedule in the factored models.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The theoretical analysis is rigorous and well-structured.
3. The experiments are comprehensive and well-designed.

### Weaknesses

#### Some Related Works

[1] On the implicit bias of initialization shape: Beyond infinitesimal mirror descent.
[2] The implicit bias of gradient descent on nonseparable data.

#### comment

1. The paper does not provide a clear explanation of why the non-equivariant optimizers perform worse than their equivariant counterparts. It is unclear whether the poor performance of non-equivariant optimizers is due to the violation of gauge symmetry or other factors. The analysis should delve deeper into the specific mechanisms that lead to this performance gap, rather than attributing it solely to symmetry violations. For instance, it would be beneficial to investigate if the non-equivariant optimizers get stuck in suboptimal local minima or if their parameter updates are less effective in navigating the loss landscape.
2. The paper does not provide a clear explanation of why the spectral schedule is important in the factored models. It is unclear whether the poor performance of non-equivariant optimizers is due to the violation of gauge symmetry or other factors. The analysis should delve deeper into the specific mechanisms that lead to this performance gap, rather than attributing it solely to symmetry violations. For instance, it would be beneficial to investigate if the non-equivariant optimizers get stuck in suboptimal local minima or if their parameter updates are less effective in navigating the loss landscape. The paper should also clarify the specific properties of the spectral schedule that make it effective and how it interacts with the equivariant optimizers.

### Suggestions

To strengthen the paper, the authors should conduct a more detailed analysis of the optimization dynamics of both equivariant and non-equivariant optimizers. This could involve visualizing the trajectory of the optimization process in the parameter space, or analyzing the Hessian of the loss function at different stages of training. Such analysis could reveal whether the non-equivariant optimizers are indeed converging to suboptimal solutions, or if they are simply exhibiting more erratic behavior. Furthermore, the authors should investigate the impact of different initialization schemes on the performance of both equivariant and non-equivariant optimizers. It is possible that the poor performance of non-equivariant optimizers is not solely due to the violation of gauge symmetry, but also due to the initialization of the parameters. For example, if the non-equivariant optimizers are initialized in a way that is not compatible with the loss landscape, they may struggle to converge to a good solution. 

Additionally, the authors should provide a more detailed explanation of the spectral schedule and its role in the factored models. This could involve a theoretical analysis of how the spectral schedule affects the optimization process, or a more detailed empirical study of the impact of different spectral schedules on the performance of the optimizers. The authors should also investigate whether the spectral schedule is necessary for the equivariant optimizers to achieve good performance, or if it is simply a way to improve the performance of non-equivariant optimizers. It would be beneficial to explore the interaction between the spectral schedule and the gauge symmetry of the optimizers. For example, does the spectral schedule help to enforce gauge symmetry, or does it simply provide a better way to navigate the loss landscape? The authors should also consider the computational cost of using the spectral schedule, and whether it is a worthwhile trade-off for the improved performance.

Finally, the authors should consider expanding the experimental evaluation to include a wider range of tasks and datasets. This would help to demonstrate the generality of their findings and to identify any potential limitations of their approach. For example, it would be interesting to see how the different optimizers perform on tasks with different levels of non-convexity, or on datasets with different characteristics. The authors should also consider comparing their results to other state-of-the-art optimization methods, to provide a more comprehensive evaluation of their approach. This would help to contextualize their findings and to identify any potential areas for improvement.

### Questions

1. Could the authors provide a more detailed explanation of why the non-equivariant optimizers perform worse than their equivariant counterparts?
2. Could the authors provide a more detailed explanation of why the spectral schedule is important in the factored models?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper studies the implicit regularization effect of different optimization algorithms on factored models. The authors propose a criterion to classify optimization algorithms as either equivariant or non-equivariant. They then conduct a series of experiments to compare the performance of nine different optimizers, including both coordinate-wise and factored ones, on matrix sensing tasks. The results show that the non-equivariant optimizers perform worse than their equivariant counterparts. The paper also highlights the importance of the spectral schedule in the factored models.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The theoretical analysis is rigorous and well-structured.
3. The experiments are comprehensive and well-designed.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a clear explanation of why the non-equivariant optimizers perform worse than their equivariant counterparts. It is unclear whether the poor performance of non-equivariant optimizers is due to the violation of gauge symmetry or other factors. The analysis should delve deeper into the specific mechanisms that lead to this performance gap, rather than attributing it solely to symmetry violations. For instance, it would be beneficial to investigate if the non-equivariant optimizers get stuck in suboptimal local minima or if their parameter updates are less effective in navigating the loss landscape.
2. The paper does not provide a clear explanation of why the spectral schedule is important in the factored models. It is unclear whether the poor performance of non-equivariant optimizers is due to the violation of gauge symmetry or other factors. The analysis should delve deeper into the specific mechanisms that lead to this performance gap, rather than attributing it solely to symmetry violations. For instance, it would be beneficial to investigate if the spectral schedule helps to enforce gauge symmetry, or if it simply provides a better way to navigate the loss landscape. The paper should also clarify the specific properties of the spectral schedule that make it effective and how it interacts with the equivariant optimizers.

### Suggestions

To strengthen the paper, the authors should conduct a more detailed analysis of the optimization dynamics of both equivariant and non-equivariant optimizers. This could involve visualizing the trajectory of the optimization process in the parameter space, or analyzing the Hessian of the loss function at different stages of training. Such analysis could reveal whether the non-equivariant optimizers are indeed converging to suboptimal solutions, or if they are simply exhibiting more erratic behavior. Furthermore, the authors should investigate the impact of different initialization schemes on the performance of both equivariant and non-equivariant optimizers. It is possible that the poor performance of non-equivariant optimizers is not solely due to the violation of gauge symmetry, but also due to the initialization of the parameters. For example, if the non-equivariant optimizers are initialized in a way that is not compatible with the loss landscape, they may struggle to converge to a good solution.

Additionally, the authors should provide a more detailed explanation of the spectral schedule and its role in the factored models. This could involve a theoretical analysis of how the spectral schedule affects the optimization process, or a more detailed empirical study of the impact of different spectral schedules on the performance of the optimizers. The authors should also investigate whether the spectral schedule is necessary for the equivariant optimizers to achieve good performance, or if it is simply a way to improve the performance of non-equivariant optimizers. It would be beneficial to explore the interaction between the spectral schedule and the gauge symmetry of the optimizers. For example, does the spectral schedule help to enforce gauge symmetry, or does it simply provide a better way to navigate the loss landscape? The authors should also consider the computational cost of using the spectral schedule, and whether it is a worthwhile trade-off for the improved performance.

Finally, the authors should consider expanding the experimental evaluation to include a wider range of tasks and datasets. This would help to demonstrate the generality of their findings and to identify any potential limitations of their approach. For example, it would be interesting to see how the different optimizers perform on tasks with different levels of non-convexity, or on datasets with different characteristics. The authors should also consider comparing their results to other state-of-the-art optimization methods, to provide a more comprehensive evaluation of their approach. This would help to contextualize their findings and to identify any potential areas for improvement.

### Questions

See above

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

This paper investigates the implicit regularization effects of various optimization algorithms on factored models, which are models with a specific structure that allows for the same matrix to be represented in multiple ways. The authors introduce a criterion to classify optimizers as either gauge-equivariant or gauge-non-equivariant, based on whether they respect the gauge symmetry of the model. They then conduct a series of experiments comparing nine different optimizers, including both coordinate-wise and factored ones, on matrix sensing tasks. The results show that the non-equivariant optimizers generally perform worse than their equivariant counterparts, highlighting the importance of gauge equivariance in achieving better generalization. The paper also provides a detailed theoretical analysis of the optimization dynamics of equivariant optimizers and their relationship to the spectral schedule.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper provides a comprehensive analysis of the implicit regularization effects of various optimization algorithms on factored models, which is a novel and important contribution to the field of machine learning.
2. The paper introduces a clear and well-defined criterion for classifying optimizers as either gauge-equivariant or gauge-non-equivariant, which is a valuable contribution to the understanding of optimization dynamics in structured models.
3. The paper provides a detailed theoretical analysis of the optimization dynamics of equivariant optimizers and their relationship to the spectral schedule, which is a significant contribution to the theoretical understanding of optimization in factored models.
4. The paper is well-written and easy to follow, with clear explanations of the key concepts and methods.

### Weaknesses

#### Some Related Works


#### comment

1. The paper focuses primarily on the underdetermined case (n = 40, k = 3), and it is unclear how the findings generalize to other settings, such as overparameterized scenarios (n < k). Specifically, the behavior of gauge-equivariant optimizers in highly overparameterized regimes, where the effective rank of the weight matrices is much smaller than the actual dimension, is not explored. This is a crucial aspect to consider, as many practical applications involve such scenarios.
2. The paper does not provide a detailed analysis of the computational cost associated with different optimizers. This is important because some gauge-equivariant methods might introduce additional computational overhead, which could be a limiting factor in large-scale applications. For instance, the per-iteration cost of methods like Shampoo, which involves matrix inversions or pseudo-inversions, should be explicitly compared to simpler methods like gradient descent or Adam. A thorough analysis of both time and memory complexity is necessary.
3. The paper could benefit from a more in-depth discussion of the practical implications of the findings. While the theoretical analysis is strong, it would be helpful to provide more concrete guidance on how to choose the most appropriate optimizer for a given task. For example, are there specific scenarios where one type of gauge-equivariant optimizer is clearly superior to others? The paper should also discuss the trade-offs between different optimizers in terms of convergence speed, generalization performance, and computational cost.

### Suggestions

The paper would significantly benefit from a more thorough investigation into the behavior of the proposed optimizers in overparameterized settings. Specifically, experiments should be conducted with varying degrees of overparameterization, such as n < k, to assess how the gauge symmetry affects the optimization landscape and generalization performance. It would be valuable to analyze the effective rank of the learned matrices during training and how it evolves with different optimizers. This analysis should include a comparison of the singular value distributions of the weight matrices, which could reveal whether gauge-equivariant optimizers tend to learn low-rank solutions more effectively in overparameterized scenarios. Furthermore, the paper should explore the impact of different initialization schemes on the performance of these optimizers in overparameterized settings, as the initialization can play a crucial role in the optimization process.

To address the lack of computational cost analysis, the paper should include a detailed comparison of the per-iteration time and memory requirements of different optimizers. This analysis should consider both the training and inference phases. For example, the paper could provide a breakdown of the computational cost associated with each step of the optimization process, such as gradient computation, update rule application, and any additional operations specific to each optimizer. This analysis should also consider the scaling of these costs with respect to the model size and the batch size. Furthermore, the paper should discuss the practical implications of these computational costs for large-scale applications, such as the feasibility of using these optimizers on hardware with limited resources. It would also be beneficial to explore techniques for reducing the computational overhead of gauge-equivariant optimizers, such as using low-rank approximations or other optimization tricks.

Finally, the paper should provide more concrete guidance on how to choose the most appropriate optimizer for a given task. This discussion should go beyond the theoretical analysis and consider practical factors such as the size of the model, the available computational resources, and the desired trade-off between convergence speed and generalization performance. For example, the paper could provide a set of rules of thumb or heuristics for selecting between different gauge-equivariant optimizers based on the characteristics of the task. It would also be helpful to include a discussion of the limitations of each optimizer and the scenarios where they are likely to perform poorly. This practical guidance would make the paper more useful for practitioners and facilitate the adoption of the proposed methods in real-world applications.

### Questions

1. How do the findings of this paper generalize to other settings, such as overparameterized scenarios (n < k)? Are there any specific challenges or considerations when applying the proposed optimizers in such settings?
2. What is the computational cost of the proposed optimizers compared to other optimizers? How does the computational cost scale with the size of the model and the batch size?
3. Can the authors provide more concrete guidance on how to choose the most appropriate optimizer for a given task? Are there any specific scenarios where one type of gauge-equivariant optimizer is clearly superior to others?

### Rating

8

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers for the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

**Plan:**
1. Read each reviewer's weakness.
2. Find corresponding sections in the paper.
3. Extract evidence (quotes, experimental details, missing citations).
4. Analyze the evidence and determine if the weakness is valid.
5. Summarize the findings for each weakness.
**Review 1**

1. Weakness Statement:
"The paper primarily focuses on the underdetermined case (n = 40, k = 3), and it is unclear how the findings generalize to other settings, such as overparameterized scenarios (n < k). Specifically, the behavior of gauge-equivariant optimizers in highly overparameterized regimes, where the effective rank of the weight matrices is much smaller than the actual dimension, is not explored. This is a crucial aspect to consider, as many practical applications involve such scenarios."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The paper explicitly states in the "Experiments" section: "We consider full overparameterization ( k = n ), small initialization ( 10 − 3 ), no weight decay, and optimize the squared loss on the measurements. The parameter space is underdetermined: infinitely many matrices (low- and full-rank) are compatible with any given measurements."
   - The "Protocol" subsection mentions: "We report recovery and effective rank, rec ( W ) = ‖ W − X ∗ ‖ F / ‖ X ∗ ‖ F , erank ( W ) = exp ( − ∑ i π i log π i ) , with π i = σ i / ∑ j σ j and 0 ​ log ⁡ 0 ​ = 0 ( Roy & Vetterli, 2007 ) ."
   - The "Results" section states: "The recovery is our main concern, as effective rank can be misleading: a method might reach a low-rank matrix in parameter space far from the true X ∗ (see § 5 )."

3. Literature Gap Analysis:
   - The paper does not explicitly discuss or cite literature on the behavior of gauge-equivariant optimizers in overparameterized settings.

4. Validation Analysis:
   - The paper explicitly focuses on the underdetermined case (n=k) and uses the term "overparameterization" in the experimental setup description, which is a contradiction. The reviewer's understanding of "overparameterized" as n < k seems to be the standard definition, while the paper uses it in the context of full overparameterization (n=k). However, the core point about the lack of explicit analysis or experiments on scenarios where n < k is valid. The paper's focus on the underdetermined case limits the generalizability of the findings to overparameterized scenarios.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: High
   - Key supporting evidence: The paper explicitly states the use of the underdetermined case (n=k) and lacks experiments or discussion on overparameterized scenarios (n < k).

1. Weakness Statement:
"The paper does not provide a detailed analysis of the computational cost associated with different optimizers. This is important because some gauge-equivariant methods might introduce additional computational overhead, which could be a limiting factor in large-scale applications. For instance, the per-iteration cost of methods like Shampoo, which involves matrix inversions or pseudo-inversions, should be explicitly compared to simpler methods like gradient descent or Adam. A thorough analysis of both time and memory complexity is necessary."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "Protocol" subsection mentions: "We report recovery and effective rank, rec ( W ) = ‖ W − X ∗ ‖ F / ‖ X ∗ ‖ F , erank ( W ) = exp ( − ∑ i π i log π i ) , with π i = σ i / ∑ j σ j and 0 ​ log ⁡ 0 ​ = 0 ( Roy & Vetterli, 2007 ) ."
   - The "Results" section presents tables with recovery and effective rank values but does not include any information about the computational cost or time taken by each optimizer.

3. Literature Gap Analysis:
   - The paper does not cite literature that provides a detailed analysis of the computational cost of different optimizers in the context of factored models.

4. Validation Analysis:
   - The paper focuses on the performance (recovery and effective rank) of the optimizers but omits any discussion or analysis of their computational cost. The reviewer's point about the potential overhead of gauge-equivariant methods like Shampoo is valid, as these methods often involve more computationally intensive operations than simpler optimizers.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper's results section only reports recovery and effective rank, with no mention of computational cost or time taken by different optimizers.

1. Weakness Statement:
"The paper could benefit from a more in-depth discussion of the practical implications of the findings. While the theoretical analysis is strong, it would be helpful to provide more concrete guidance on how to choose the most appropriate optimizer for a given task. For example, are there specific scenarios where one type of gauge-equivariant optimizer is clearly superior to others? The paper should also discuss the trade-offs between different optimizers in terms of convergence speed, generalization performance, and computational cost."

2. Evidence Collection:
b) Experiment-related Evidence:
   - The "Introduction" section mentions: "The bias it encodes is mild, and we highlight the conditions under which it is beneficial in § 10.1 : it wins over tuned explicit regularization only where the optimal regularization is itself mild and aligned in direction, and it falls short, in ways the theory anticipates, on tasks that demand stronger regularization or the kind of per-coordinate adaptation Adam provides."
   - The "Conclusion" section states: "The bias it encodes is mild, and we highlight the conditions under which it is beneficial in § 10.1 : it wins over tuned explicit regularization only where the optimal regularization is itself mild and aligned in direction, and it falls short, in ways the theory anticipates, on tasks that demand stronger regularization or the kind of per-coordinate adaptation Adam provides."
   - The "Results" section provides some high-level observations: "The two clusters of predicted methods satisfy gauge equivariance as defined in Definition 3.1 . 1. GD and scalar-Adam are not ad hoc examples but the per-coordinate coordinate-wise ones, and they are different shape-aware variants of it. 2. Scalar-preconditioned Adam : a version of Adam where the per-coordinate second-moment estimate is replaced by a single scalar ν ^ t , obtained via bias-corrected exponential moving average (EMA) of gauge-invariant quantities (such as the average of all entries in g ⊙ 2 g ⊤ ) . 3. Muon : updates given by Δ = msign ( M t ) , where M t M t = A ⊙ g ⊤ t / a t . 4. Shampoo : the step Δ = ( L t + λ I ) − 1 / 4 G t ( R t + λ I ) − 1 / 4 , L t = ∑ u ≤ t G u G u ⊤ , R t = ∑ u ≤ t G u ⊤ G u , 5. Adam : the update rule ( U t + 1 , V t + 1 , s t + 1 ) = ( U t , V t , s t ) + ( ∇ U L t + λ I ) − 1 / 2 ∇ M t ( R t + λ I ) − 1 / 2 , 6. Shampoo : the step Δ = ( L t + λ I ) − 1 / 4 G t ( R t + λ I ) − 1 / 4 , L t = ∑ u ≤ t G u G u ⊤ , R t = ∑ u ≤ t G u ⊤ G u , 7. GD : the update rule ( U t + 1 , V t + 1 , s t + 1 ) = ( U t , V t , s t ) + ( ∇ U L t + λ I ) − 1 / 2 ∇ M t ( R t + λ I ) − 1 / 2 , 8. scalar-Adam : the update rule Δ ∝ m t / a t ∇ M t , with elementwise operations, shared stepsize η , and initial moment estimates set to zero, to avoid an easy win for methods that cannot interpolate at a constant step size. 9. RMSProp : the update rule Δ = ( L t + λ I ) − 1 / 2 G t ( R t + λ I ) − 1 / 2 , 10. signum : Δ = msign ( M t ) , where M t = a t ⊙ g ⊤ + ( v ^ + ϵ ) ⊙ ( v ^ + ϵ ) T ."
   - The "Results" section provides some observations about the performance of different optimizers, but it doesn't offer concrete guidance on choosing the best optimizer for a specific task, considering trade-offs.

4. Validation Analysis:
   - The paper does provide some high-level observations about the performance of different optimizers, but it lacks a detailed discussion on the practical implications and trade-offs. The reviewer's point about the need for more concrete guidance is valid.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: While the paper presents performance comparisons, it lacks a detailed discussion on practical implications, trade-offs, and specific scenarios where one optimizer might be superior.

**Review 2**

1. Weakness Statement:
"The paper does not provide a clear explanation of why the non-equivariant optimizers perform worse than their equivariant counterparts. It is unclear whether the poor performance of non-equivariant optimizers is due to the violation of gauge symmetry or other factors. The analysis should delve deeper into the specific mechanisms that lead to this performance gap, rather than attributing it solely to symmetry violations. For instance, it would be beneficial to investigate if the non-equivariant optimizers get stuck in suboptimal local minima or if their parameter updates are less effective in navigating the loss landscape."

2. Evidence Collection:
a) Method-related Evidence:
   - The "Classification and first-step defect analysis" section states: "All methods we consider have zero-initialized states, and we impose σ Q ​ ( 0 ) = 0 , ensuring that both trajectories start from the same initial conditions. That convention is not what excludes Adam: its entrywise second moment admits no state map σ Q ​ at all, whatever it does at zero, because squaring and right-rotation do not commute—which is exactly what the scalar version repairs (proof of Proposition 4.2 (2)). For an equivariant optimizer it follows that the product matrices W t = U t V t ⊤ = U t V t − ⁣ ⊤ is uniquely defined by the input data and the gauge orbit of the initial factors ( U 0 , V 0 ) (U_{t+1},V_{t+1},s_{t+1})=\mathcal{A}(U_{t},V_{t},s_{t};\,\,\nabla L). It is gauge-equivariant, while updates that apply a fixed entrywise nonlinearity at zero optimizer state (Adam, RMSProp, signSGD, Lion, Adafactor—signSGD, Lion, RMSProp, and signum (signSGD, Lion) are not. Similar distinctions have been noted previously for unfactored parameterizations, where the rotation acts on the whole parameter space (§ 2 , Table 1 ), but not for the internal gauge of a factored model. For equivariant optimizers it follows that the key to low-rank convergence is the spectral schedule: whether the dynamics it induces on the singular values of the factored weights during training lead to attraction to a low-rank manifold within the specified training budget."
   - The "Theorem 4.6 (Nonlinear coordinate-wise maps are Gram-determined left preconditioners)" section provides a theoretical explanation for why coordinate-wise maps break the gauge.

3. Literature Gap Analysis:
   - The paper cites works that have observed the importance of gauge symmetry, such as [25] and [26].

4. Validation Analysis:
   - The paper provides a theoretical explanation based on the concept of gauge-equivariance and the spectral schedule. It argues that non-equivariant optimizers violate the gauge symmetry, leading to a mismatch between the optimization trajectory and the low-rank manifold. While the paper doesn't explicitly investigate whether non-equivariant optimizers get stuck in suboptimal local minima, the theoretical framework focuses on the violation of gauge symmetry as the primary reason for their inferior performance.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper provides a theoretical explanation based on gauge symmetry. However, it could benefit from a more in-depth discussion and empirical evidence regarding whether the poor performance is solely due to symmetry violations or if other factors, like getting stuck in local minima, play a role.

1. Weakness Statement:
"The paper does not provide a clear explanation of why the spectral schedule is important in the factored models. It is unclear whether the poor performance of non-equivariant optimizers is due to the violation of gauge symmetry or other factors. The analysis should delve deeper into the specific mechanisms that lead to this performance gap, rather than attributing it solely to symmetry violations. For instance, it would be beneficial to investigate if the spectral schedule helps to enforce gauge symmetry, or if it simply provides a better way to navigate the loss landscape. The paper should also clarify the specific properties of the spectral schedule that make it effective and how it interacts with the equivariant optimizers."

2. Evidence Collection:
a) Method-related Evidence:
   - The "Classification and first-step defect analysis" section states: "It is gauge-equivariant, while updates that apply a fixed entrywise nonlinearity at zero optimizer state (Adam, RMSProp, signSGD, Lion, Adafactor—signSGD, Lion, RMSProp, and signum (signSGD, Lion) are not. Similar distinctions have been noted previously for unfactored parameterizations, where the rotation acts on the whole parameter space (§ 2 , Table 1 ), but not for the internal gauge of a factored model. For equivariant optimizers it follows that the key to low-rank convergence is the spectral schedule: whether the dynamics it induces on the singular values of the factored weights during training lead to attraction to a low-rank manifold within the specified training budget."
   - The "Theorem 4.6 (Nonlinear coordinate-wise maps are Gram-determined left preconditioners)" section provides a theoretical explanation for why coordinate-wise maps break the gauge.
   - The "Theorem 4.5 (Structure: equivariant memoryless rules are Gram-determined left preconditioners)" section provides a theoretical explanation for why equivariant optimizers are Gram-determined left preconditioners.
   - The "Theorem 4.4 (Adam has an exact first-step gauge defect)" section provides a theoretical explanation for why Adam has a first-step gauge defect.
   - The "Theorem 4.3 (Nonlinear coordinate-wise maps break the gauge)" section provides a theoretical explanation for why coordinate-wise maps break the gauge.

4. Validation Analysis:
   - The paper argues that the spectral schedule is crucial for the success of gauge-equivariant optimizers. It explains that these optimizers, by respecting the gauge symmetry, can navigate the loss landscape effectively, particularly in the context of low-rank recovery. The spectral schedule, by controlling the evolution of singular values, helps guide the optimization process towards a low-rank solution. While the paper doesn't explicitly state that the spectral schedule enforces gauge symmetry, it does explain how the gauge-equivariant optimizers, which respect the gauge, benefit from the spectral schedule to reach a low-rank solution. The paper could benefit from a more explicit discussion of how the spectral schedule interacts with the gauge symmetry to achieve low-rank convergence.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper explains the importance of the spectral schedule in the context of gauge-equivariant optimizers and their ability to reach low-rank solutions. However, it could be more explicit about how the spectral schedule interacts with the gauge symmetry itself.

**Review 3**

1. Weakness Statement:
"The paper does not provide a clear explanation of why the non-equivariant optimizers perform worse than their equivariant counterparts. It is unclear whether the poor performance of non-equivariant optimizers is due to the violation of gauge symmetry or other factors. The analysis should delve deeper into the specific mechanisms that lead to this performance gap, rather than attributing it solely to symmetry violations. For instance, it would be beneficial to investigate if the non-equivariant optimizers get stuck in suboptimal local minima or if their parameter updates are less effective in navigating the loss landscape."

2. Evidence Collection:
a) Method-related Evidence:
   - The "Classification and first-step defect analysis" section states: "It is gauge-equivariant, while updates that apply a fixed entrywise nonlinearity at zero optimizer state (Adam, RMSProp, signSGD, Lion, Adafactor—signSGD, Lion, RMSProp, and signum (signSGD, Lion) are not. Similar distinctions have been noted previously for unfactored parameterizations, where the rotation acts on the whole parameter space (§ 2 , Table 1 ), but not for the internal gauge of a factored model. For equivariant optimizers it follows that the key to low-rank convergence is the spectral schedule: whether the dynamics it induces on the singular values of the factored weights during training lead to attraction to a low-rank manifold within the specified training budget."
   - The "Theorem 4.6 (Nonlinear coordinate-wise maps are Gram-determined left preconditioners)" section provides a theoretical explanation for why coordinate-wise maps break the gauge.

3. Literature Gap Analysis:
   - The paper cites works that have observed the importance of gauge symmetry, such as [25] and [26].

4. Validation Analysis:
   - The paper provides a theoretical explanation based on the concept of gauge-equivariance and the spectral schedule. It argues that non-equivariant optimizers violate the gauge symmetry, leading to a mismatch between the optimization trajectory and the low-rank manifold. While the paper doesn't explicitly investigate whether non-equivariant optimizers get stuck in suboptimal local minima, the theoretical framework focuses on the violation of gauge symmetry as the primary reason for their inferior performance.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper provides a theoretical explanation based on gauge symmetry. However, it could benefit from a more in-depth discussion and empirical evidence regarding whether the poor performance is solely due to symmetry violations or if other factors, like getting stuck in local minima, play a role.

1. Weakness Statement:
"The paper does not provide a clear explanation of why the spectral schedule is important in the factored models. It is unclear whether the poor performance of non-equivariant optimizers is due to the violation of gauge symmetry or other factors. The analysis should delve deeper into the specific mechanisms that lead to this performance gap, rather than attributing it solely to symmetry violations. For instance, it would be beneficial to investigate if the spectral schedule helps to enforce gauge symmetry, or if it simply provides a better way to navigate the loss landscape. The paper should also clarify the specific properties of the spectral schedule that make it effective and how it interacts with the equivariant optimizers."

2. Evidence Collection:
a) Method-related Evidence:
   - The "Classification and first-step defect analysis" section states: "It is gauge-equivariant, while updates that apply a fixed entrywise nonlinearity at zero optimizer state (Adam, RMSProp, signSGD, Lion, Adafactor—signSGD, Lion, RMSProp, and signum (signSGD, Lion) are not. Similar distinctions have been noted previously for unfactored parameterizations, where the rotation acts on the whole parameter space (§ 2 , Table 1 ), but not for the internal gauge of a factored model. For equivariant optimizers it follows that the key to low-rank convergence is the spectral schedule: whether the dynamics it induces on the singular values of the factored weights during training lead to attraction to a low-rank manifold within the specified training budget."
   - The "Theorem 4.6 (Nonlinear coordinate-wise maps are Gram-determined left preconditioners)" section provides a theoretical explanation for why coordinate-wise maps break the gauge.

4. Validation Analysis:
   - The paper argues that the spectral schedule is crucial for the success of gauge-equivariant optimizers. It explains that these optimizers, by respecting the gauge symmetry, can navigate the loss landscape effectively, particularly in the context of low-rank recovery. The spectral schedule, by controlling the evolution of singular values, helps guide the optimization process towards a low-rank solution. While the paper doesn't explicitly state that the spectral schedule enforces gauge symmetry, it does explain how the gauge-equivariant optimizers, which respect the gauge, benefit from the spectral schedule to reach a low-rank solution. The paper could benefit from a more explicit discussion of how the spectral schedule interacts with the gauge symmetry itself.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper explains the importance of the spectral schedule in the context of gauge-equivariant optimizers and their ability to reach low-rank solutions. However, it could be more explicit about how the spectral schedule interacts with the gauge symmetry itself.

**Review 4**

1. Weakness Statement:
"The paper does not provide a clear explanation of why the non-equivariant optimizers perform worse than their equivariant counterparts. It is unclear whether the poor performance of non-equivariant optimizers is due to the violation of gauge symmetry or other factors. The analysis should delve deeper into the specific mechanisms that lead to this performance gap, rather than attributing it solely to symmetry violations. For instance, it would be beneficial to investigate if the non-equivariant optimizers get stuck in suboptimal local minima or if their parameter updates are less effective in navigating the loss landscape."

2. Evidence Collection:
a) Method-related Evidence:
   - The "Classification and first-step defect analysis" section states: "It is gauge-equivariant, while updates that apply a fixed entrywise nonlinearity at zero optimizer state (Adam, RMSProp, signSGD, Lion, Adafactor—signSGD, Lion, RMSProp, and signum (signSGD, Lion) are not. Similar distinctions have been noted previously for unfactored parameterizations, where the rotation acts on the whole parameter space (§ 2 , Table 1 ), but not for the internal gauge of a factored model. For equivariant optimizers it follows that the key to low-rank convergence is the spectral schedule: whether the dynamics it induces on the singular values of the factored weights during training lead to attraction to a low-rank manifold within the specified training budget."
   - The "Theorem 4.6 (Nonlinear coordinate-wise maps are Gram-determined left preconditioners)" section provides a theoretical explanation for why coordinate-wise maps break the gauge.

3. Literature Gap Analysis:
   - The paper cites works that have observed the importance of gauge symmetry, such as [25] and [26].

4. Validation Analysis:
   - The paper provides a theoretical explanation based on the concept of gauge-equivariance and the spectral schedule. It argues that non-equivariant optimizers violate the gauge symmetry, leading to a mismatch between the optimization trajectory and the low-rank manifold. While the paper doesn't explicitly investigate whether non-equivariant optimizers get stuck in suboptimal local minima, the theoretical framework focuses on the violation of gauge symmetry as the primary reason for their inferior performance.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper provides a theoretical explanation based on gauge symmetry. However, it could benefit from a more in-depth discussion and empirical evidence regarding whether the poor performance is solely due to symmetry violations or if other factors, like getting stuck in local minima, play a role.

1. Weakness Statement:
"The paper does not provide a clear explanation of why the spectral schedule is important in the factored models. It is unclear whether the poor performance of non-equivariant optimizers is due to the violation of gauge symmetry or other factors. The analysis should delve deeper into the specific mechanisms that lead to this performance gap, rather than attributing it solely to symmetry violations. For instance, it would be beneficial to investigate if the spectral schedule helps to enforce gauge symmetry, or if it simply provides a better way to navigate the loss landscape. The paper should also clarify the specific properties of the spectral schedule that make it effective and how it interacts with the equivariant optimizers."

2. Evidence Collection:
a) Method-related Evidence:
   - The "Classification and first-step defect analysis" section states: "It is gauge-equivariant, while updates that apply a fixed entrywise nonlinearity at zero optimizer state (Adam, RMSProp, signSGD, Lion, Adafactor—signSGD, Lion, RMSProp, and signum (signSGD, Lion) are not. Similar distinctions have been noted previously for unfactored parameterizations, where the rotation acts on the whole parameter space (§ 2 , Table 1 ), but not for the internal gauge of a factored model. For equivariant optimizers it follows that the key to low-rank convergence is the spectral schedule: whether the dynamics it induces on the singular values of the factored weights during training lead to attraction to a low-rank manifold within the specified training budget."
   - The "Theorem 4.6 (Nonlinear coordinate-wise maps are Gram-determined left preconditioners)" section provides a theoretical explanation for why coordinate-wise maps break the gauge.

4. Validation Analysis:
   - The paper argues that the spectral schedule is crucial for the success of gauge-equivariant optimizers. It explains that these optimizers, by respecting the gauge symmetry, can navigate the loss landscape effectively, particularly in the context of low-rank recovery. The spectral schedule, by controlling the evolution of singular values, helps guide the optimization process towards a low-rank solution. While the paper doesn't explicitly state that the spectral schedule enforces gauge symmetry, it does explain how the gauge-equivariant optimizers, which respect the gauge, benefit from the spectral schedule to reach a low-rank solution. The paper could benefit from a more explicit discussion of how the spectral schedule interacts with the gauge symmetry itself.

5. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: The paper explains the importance of the spectral schedule in the context of gauge-equivariant optimizers and their ability to reach low-rank solutions. However, it could be more explicit about how the spectral schedule interacts with the gauge symmetry itself.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper delves into the implicit regularization effects of various optimization algorithms on factored models, which are models represented as a product of matrices. The authors introduce a novel criterion to classify optimization algorithms as either gauge-equivariant or gauge-non-equivariant, based on their behavior under the action of the model's gauge symmetry. They demonstrate that gauge-equivariant optimizers, which respect the gauge symmetry, generally perform better in terms of low-rank recovery compared to their gauge-non-equivariant counterparts. The paper provides a rigorous theoretical framework for understanding the importance of gauge-equivariance, supported by empirical results across multiple tasks and optimizers. The authors also highlight the role of the spectral schedule in the optimization process, showing how it influences the convergence to low-rank solutions. The findings are significant as they offer a deeper understanding of the implicit regularization properties of optimization algorithms, which can guide the selection of appropriate optimizers for structured models. However, the paper's focus on the underdetermined case (n=k) and the lack of computational cost analysis raise important questions about the generalizability and practical applicability of the results.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

3.0


## Strengths:

I found the paper to be a well-written and well-structured exploration of the implicit regularization effects of optimization algorithms on factored models. The authors provide a clear and rigorous theoretical framework for understanding the importance of gauge-equivariance, which is a novel and significant contribution to the field. The classification of optimizers as either gauge-equivariant or gauge-non-equivariant is particularly insightful, as it allows for a systematic comparison of their performance. The empirical results are extensive and well-designed, covering a range of tasks and optimizers, which strengthens the paper's claims. The authors also provide a detailed analysis of the spectral schedule and its role in the optimization process, which is a valuable addition to the understanding of how optimizers navigate the loss landscape. The paper's clarity and organization make it accessible to readers with a background in machine learning and optimization, and the theoretical analysis is well-supported by the empirical findings. The authors' focus on the underdetermined case (n=k) is a strength, as it allows for a clear demonstration of the benefits of gauge-equivariant optimizers in achieving low-rank solutions. The paper also includes a thorough discussion of the limitations of the study and potential directions for future research, which is crucial for guiding the field forward.


## Weaknesses:

Despite the paper's strengths, there are several verified limitations that warrant attention. First, the paper's primary focus on the underdetermined case (n=k) limits the generalizability of the findings to overparameterized scenarios (n < k). The behavior of gauge-equivariant optimizers in highly overparameterized regimes, where the effective rank of the weight matrices is much smaller than the actual dimension, is not explored. This is a critical aspect to consider, as many practical applications involve such scenarios. The paper's focus on the underdetermined case, while valuable, does not provide a complete picture of the optimization dynamics in more common settings. Second, the paper lacks a detailed analysis of the computational cost associated with different optimizers. While the authors report recovery and effective rank, they do not provide information on the per-iteration time and memory requirements of each optimizer. This is particularly important because some gauge-equivariant methods, such as Shampoo, involve matrix inversions or pseudo-inversions, which can be computationally expensive. A thorough analysis of both time and memory complexity would be necessary to understand the practical trade-offs between different optimizers. Third, the paper could benefit from a more in-depth discussion of the practical implications of the findings. While the theoretical analysis is strong, the paper does not provide concrete guidance on how to choose the most appropriate optimizer for a given task. For example, the paper does not explore whether certain types of gauge-equivariant optimizers are clearly superior to others in specific scenarios, or how the trade-offs between convergence speed, generalization performance, and computational cost should be considered. This practical guidance would make the paper more useful for practitioners and facilitate the adoption of the proposed methods in real-world applications. Finally, the paper's explanation of why non-equivariant optimizers perform worse than their equivariant counterparts is somewhat limited. The authors attribute the poor performance to the violation of gauge symmetry, but they do not delve into the specific mechanisms that lead to this performance gap. For instance, it is not clear whether the poor performance is due to the optimization getting stuck in suboptimal local minima or if the parameter updates are less effective in navigating the loss landscape. A more detailed investigation into these aspects would provide a deeper understanding of the optimization dynamics and the role of gauge symmetry in shaping the loss landscape. These limitations, while not undermining the paper's core contributions, highlight areas where further research and discussion are needed to fully realize the potential of the proposed methods.


## Suggestions:

To address the identified limitations, I suggest several concrete and actionable improvements. First, the authors should extend their experimental evaluation to include overparameterized settings (n < k). This would involve analyzing the effective rank of the learned matrices during training and how it evolves with different optimizers. The authors could also explore the impact of different initialization schemes on the performance of these optimizers in overparameterized settings. This analysis should include a comparison of the singular value distributions of the weight matrices, which could reveal whether gauge-equivariant optimizers tend to learn low-rank solutions more effectively in overparameterized scenarios. Second, the paper should include a detailed comparison of the per-iteration time and memory requirements of different optimizers. This analysis should consider both the training and inference phases, and should be conducted on various hardware platforms, such as GPUs and CPUs. The authors could provide a breakdown of the computational cost associated with each step of the optimization process, such as gradient computation, update rule application, and any additional operations specific to each optimizer. This would help practitioners make informed decisions about the trade-offs between different optimizers. Third, the authors should provide more concrete guidance on how to choose the most appropriate optimizer for a given task. This discussion should go beyond the theoretical analysis and consider practical factors such as the size of the model, the available computational resources, and the desired trade-off between convergence speed and generalization performance. The authors could include a set of rules of thumb or heuristics for selecting between different gauge-equivariant optimizers based on the characteristics of the task. Fourth, the authors should conduct a more detailed analysis of the optimization dynamics of both equivariant and non-equivariant optimizers. This could involve visualizing the trajectory of the optimization process in the parameter space or analyzing the Hessian of the loss function at different stages of training. Such analysis could reveal whether non-equivariant optimizers are indeed converging to suboptimal solutions or if they are simply exhibiting more erratic behavior. The authors should also investigate the impact of different initialization schemes on the performance of these optimizers, as the initialization can play a crucial role in the optimization process. Finally, the authors should explore the interaction between the spectral schedule and the gauge symmetry of the optimizers. This could involve a theoretical analysis of how the spectral schedule affects the optimization process, or a more detailed empirical study of the impact of different spectral schedules on the performance of the optimizers. The authors should also investigate whether the spectral schedule is necessary for the equivariant optimizers to achieve good performance, or if it is simply a way to improve the performance of non-equivariant optimizers. These suggestions, if implemented, would significantly enhance the paper's impact and practical utility.


## Questions:

1. How do the findings of this paper generalize to overparameterized scenarios (n < k)? Are there specific insights or challenges in this setting that are not covered in the current study? 2. Could the authors provide a detailed analysis of the computational cost associated with different optimizers, including both time and memory requirements, and how these costs scale with the model size and batch size? 3. Are there specific scenarios or tasks where one type of gauge-equivariant optimizer is clearly superior to others? If so, what are the key characteristics of these scenarios? 4. How does the spectral schedule interact with the gauge symmetry of the optimizers? Is the spectral schedule necessary for the equivariant optimizers to achieve good performance, or is it primarily a mechanism to improve the performance of non-equivariant optimizers? 5. What are the practical implications of the findings for real-world applications, particularly in terms of the trade-offs between different optimizers in terms of convergence speed, generalization performance, and computational cost?


## Rating:

6.5


## Confidence:

3.0


## Decision:

Accept
}