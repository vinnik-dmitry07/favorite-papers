I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

The paper introduces Sophia, a second-order optimization method for training large language models. Sophia incorporates diagonal Hessian information, which is computationally efficient and requires minimal memory. The authors claim that Sophia adapts to the heterogeneous curvatures in different parameter dimensions, resulting in faster convergence and better performance compared to AdamW and other optimizers.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a comprehensive set of experiments, including ablation studies on different components of Sophia, comparisons with other optimizers, and evaluations on both language modeling and SuperGLUE tasks.
3. The authors provide a theoretical analysis of Sophia in a simplified setting, showing that it does not depend on the number of iterations.

### Weaknesses

#### Some Related Works

[1] Sophia: A Simple Second Order Optimizer for Language Models

#### comment

1. The paper lacks a detailed discussion on the computational overhead of Sophia compared to AdamW and other optimizers. While the authors claim that Sophia is computationally efficient, they do not provide a thorough analysis of the time and memory costs associated with computing and storing the diagonal Hessian information. Specifically, the paper should include a breakdown of the time spent on forward and backward passes, as well as the overhead of Hessian computation and parameter updates. Furthermore, the memory footprint of Sophia, including the storage of the Hessian approximation and other optimizer states, should be compared to that of AdamW. A detailed comparison of the time and memory costs per iteration would be beneficial to understand the practical implications of using Sophia.

2. The paper does not provide a clear explanation of how Sophia handles the non-convexity of the loss landscape. While the authors mention that Sophia adapts to heterogeneous curvatures, they do not elaborate on how this adaptation prevents the optimizer from getting stuck in sharp minima or local optima. A more detailed discussion of the theoretical properties of Sophia, particularly in the context of non-convex optimization, would be valuable. For example, the paper could discuss the convergence properties of Sophia and how they compare to those of AdamW. Additionally, the paper should address the potential limitations of using a diagonal Hessian approximation, which may not capture the full curvature information of the loss landscape.

3. The paper does not provide a clear explanation of how Sophia handles the non-convexity of the loss landscape. While the authors mention that Sophia adapts to heterogeneous curvatures, they do not elaborate on how this adaptation prevents the optimizer from getting stuck in sharp minima or local optima. A more detailed discussion of the theoretical properties of Sophia, particularly in the context of non-convex optimization, would be valuable. For example, the paper could discuss the convergence properties of Sophia and how they compare to those of AdamW. Additionally, the paper should address the potential limitations of using a diagonal Hessian approximation, which may not capture the full curvature information of the loss landscape.

### Suggestions

The paper would benefit from a more thorough analysis of the computational costs associated with Sophia. While the authors claim that Sophia is computationally efficient, a detailed breakdown of the time spent on different stages of the optimization process is needed. This should include the time spent on forward and backward passes, as well as the overhead of computing and storing the diagonal Hessian information. A comparison of the time and memory costs per iteration between Sophia and AdamW would be highly informative. For example, the authors could provide a table that shows the time spent on each component of Sophia, such as the Hessian-vector product, the parameter update, and the gradient computation. This would allow readers to better understand the practical implications of using Sophia and to compare it with other optimizers. Furthermore, the paper should discuss the scalability of Sophia to larger models and datasets, as the computational costs may increase significantly with larger models.

To address the concerns about the non-convexity of the loss landscape, the paper should provide a more detailed discussion of the theoretical properties of Sophia. This should include a discussion of the convergence properties of Sophia and how they compare to those of AdamW. For example, the authors could analyze the convergence rate of Sophia and compare it to that of AdamW under different conditions. Additionally, the paper should address the potential limitations of using a diagonal Hessian approximation, which may not capture the full curvature information of the loss landscape. The authors could discuss the trade-offs between computational efficiency and accuracy when using a diagonal Hessian approximation. Furthermore, the paper could explore the use of more sophisticated Hessian approximations, such as block-diagonal approximations, to improve the performance of Sophia.

Finally, the paper should provide a more detailed explanation of how Sophia handles the non-convexity of the loss landscape. While the authors mention that Sophia adapts to heterogeneous curvatures, they do not elaborate on how this adaptation prevents the optimizer from getting stuck in sharp minima or local optima. A more detailed discussion of the theoretical properties of Sophia, particularly in the context of non-convex optimization, would be valuable. For example, the authors could discuss the convergence properties of Sophia and how they compare to those of AdamW. Additionally, the paper should address the potential limitations of using a diagonal Hessian approximation, which may not capture the full curvature information of the loss landscape. The authors could also explore the use of techniques such as adaptive learning rates or momentum to further improve the performance of Sophia.

### Questions

1. How does Sophia handle the non-convexity of the loss landscape?
2. What is the computational overhead of Sophia compared to AdamW and other optimizers?
3. How does Sophia handle the non-convexity of the loss landscape?
4. What is the memory footprint of Sophia compared to AdamW?

### Rating

5

### Confidence

4

**********

## Reviewer 2

### Summary

The paper introduces Sophia, a second-order optimizer designed for efficient large language model (LLM) pre-training. Sophia addresses the inefficiencies of traditional second-order methods, which often incur high computational costs due to the need for full Hessian calculations. By employing an inexpensive stochastic estimate of the diagonal Hessian, Sophia adapts to heterogeneous curvatures across different parameter dimensions, leading to faster convergence and improved performance. The authors also present a simplified theoretical analysis of Sophia on convex functions, demonstrating its potential advantages in accelerating convergence.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and easy to implement.
- The proposed method shows better performance than other baselines.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method is a straightforward extension of the existing Sophia method, with the main difference being the use of a diagonal Hessian estimator instead of the full Hessian. The paper does not provide a strong justification for why a diagonal Hessian is sufficient for effective optimization in the context of large language models, especially given that the loss landscape is likely to be highly non-convex and anisotropic. The authors should provide more theoretical or empirical evidence to support this choice.
- The paper lacks a thorough analysis of the computational cost of the proposed method. While the authors claim that the diagonal Hessian estimator is computationally efficient, they do not provide a detailed breakdown of the computational complexity of each step in the algorithm, including the Hessian-vector product and the parameter update. A comparison of the computational cost of Sophia with other second-order methods, such as KLBFGS, would be beneficial.
- The paper does not provide a clear explanation of how the proposed method handles the non-convexity of the loss landscape. The authors mention that the method adapts to heterogeneous curvatures, but they do not provide a detailed analysis of how this adaptation prevents the optimizer from getting stuck in sharp minima or local optima. A more rigorous analysis of the convergence properties of the proposed method is needed.

### Suggestions

The authors should provide a more detailed analysis of the diagonal Hessian estimator and its suitability for large language models. Specifically, they should investigate the spectral properties of the Hessian matrix and analyze how the diagonal approximation affects the optimization process. It would be beneficial to compare the performance of Sophia with other diagonal Hessian estimation methods, such as the Gauss-Newton matrix, to understand the trade-offs between computational cost and optimization performance. Furthermore, the authors should provide a theoretical analysis of the convergence properties of Sophia, including the conditions under which the method is guaranteed to converge to a local minimum. This analysis should also consider the impact of the diagonal Hessian approximation on the convergence rate.

To address the lack of computational cost analysis, the authors should provide a detailed breakdown of the computational complexity of each step in the Sophia algorithm. This should include the cost of computing the diagonal Hessian estimate, the Hessian-vector product, and the parameter update. A comparison of the computational cost of Sophia with other second-order methods, such as KLBFGS, would be beneficial. The authors should also investigate the memory requirements of the proposed method and compare it with other second-order methods. This analysis should consider the memory usage of storing the Hessian matrix and the intermediate variables used in the algorithm. It would also be helpful to provide empirical results on the computational cost of Sophia on different hardware platforms.

Finally, the authors should provide a more detailed explanation of how the proposed method handles the non-convexity of the loss landscape. They should analyze the behavior of the method in different regions of the loss landscape, including flat regions, sharp minima, and saddle points. It would be beneficial to provide a theoretical analysis of the convergence properties of the method in non-convex settings. The authors should also investigate the sensitivity of the method to the choice of hyperparameters and provide guidelines for selecting appropriate values. Furthermore, it would be helpful to compare the performance of Sophia with other optimization methods that are specifically designed for non-convex optimization, such as Adam and RMSprop.

### Questions

- How does the proposed method handle the non-convexity of the loss landscape?
- What is the computational cost of the proposed method compared to other second-order methods?
- What is the memory requirement of the proposed method?
- How sensitive is the proposed method to the choice of hyperparameters?

### Rating

5

### Confidence

4

**********

## Reviewer 3

### Summary

The paper introduces Sophia, a new second-order optimization method for training large language models. Sophia addresses the limitations of existing second-order methods, which often incur high computational costs and are not well-suited for large models. By using a diagonal Hessian estimator and a clipping mechanism, Sophia adapts to heterogeneous curvatures across parameter dimensions, leading to faster convergence and improved performance. The method is simple and can be easily integrated into existing training pipelines without significant changes. Empirical results show that Sophia achieves a 2x speed-up compared to Adam in terms of steps, compute, and wall-clock time, while also improving the final performance of the models.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow. The authors provide a clear and concise explanation of the proposed method, including the motivation behind the design choices.
- The proposed method is simple and can be easily integrated into existing training pipelines without significant changes. This makes it accessible to a wide range of practitioners and researchers.
- The empirical results demonstrate the effectiveness of Sophia in achieving faster convergence and improved performance compared to existing optimizers. The authors provide comprehensive experiments on various model sizes and datasets, showing the robustness of the method.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method is a straightforward extension of the existing Sophia method, with the main difference being the use of a diagonal Hessian estimator instead of the full Hessian. The paper does not provide a strong justification for why a diagonal Hessian is sufficient for effective optimization in the context of large language models, especially given that the loss landscape is likely to be highly non-convex and anisotropic. The authors should provide more theoretical or empirical evidence to support this choice.
- The paper lacks a thorough analysis of the computational cost of the proposed method. While the authors claim that the diagonal Hessian estimator is computationally efficient, they do not provide a detailed breakdown of the computational complexity of each step in the algorithm, including the Hessian-vector product and the parameter update. A comparison of the computational cost of Sophia with other second-order methods, such as KLBFGS, would be beneficial.
- The paper does not provide a clear explanation of how the proposed method handles the non-convexity of the loss landscape. The authors mention that the method adapts to heterogeneous curvatures, but they do not elaborate on how this adaptation prevents the optimizer from getting stuck in sharp minima or local optima. A more rigorous analysis of the convergence properties of the proposed method is needed.

### Suggestions

The authors should provide a more detailed analysis of the diagonal Hessian estimator and its suitability for large language models. Specifically, they should investigate the spectral properties of the Hessian matrix and analyze how the diagonal approximation affects the optimization process. It would be beneficial to compare the performance of Sophia with other diagonal Hessian estimation methods, such as the Gauss-Newton matrix, to understand the trade-offs between computational cost and optimization performance. Furthermore, the authors should provide a theoretical analysis of the convergence properties of Sophia, including the conditions under which the method is guaranteed to converge to a local minimum. This analysis should also consider the impact of the diagonal Hessian approximation on the convergence rate. It is crucial to understand the limitations of using a diagonal approximation, especially in highly non-convex loss landscapes, and to provide a clear justification for its use in the context of large language models.

To address the lack of computational cost analysis, the authors should provide a detailed breakdown of the computational complexity of each step in the Sophia algorithm. This should include the cost of computing the diagonal Hessian estimate, the Hessian-vector product, and the parameter update. A comparison of the computational cost of Sophia with other second-order methods, such as KLBFGS, would be highly beneficial. This comparison should consider both the theoretical complexity and the empirical performance on different hardware platforms. The authors should also investigate the memory requirements of the proposed method and compare it with other second-order methods. This analysis should consider the memory usage of storing the Hessian matrix and the intermediate variables used in the algorithm. It is important to understand the practical implications of using a diagonal Hessian estimator in terms of computational resources and memory usage.

Finally, the authors should provide a more detailed explanation of how the proposed method handles the non-convexity of the loss landscape. They should analyze the behavior of the method in different regions of the loss landscape, including flat regions, sharp minima, and saddle points. It would be beneficial to provide a theoretical analysis of the convergence properties of the method in non-convex settings. The authors should also investigate the sensitivity of the method to the choice of hyperparameters and provide guidelines for selecting appropriate values. Furthermore, it would be helpful to compare the performance of Sophia with other optimization methods that are specifically designed for non-convex optimization, such as Adam and RMSprop. This comparison should consider both the convergence speed and the final performance of the models.

### Questions

- How does the proposed method handle the non-convexity of the loss landscape?
- What is the computational cost of the proposed method compared to other second-order methods?
- What is the memory requirement of the proposed method?
- How sensitive is the proposed method to the choice of hyperparameters?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

The paper introduces Sophia, a new second-order optimizer designed for large language models (LLMs). Sophia addresses the limitations of existing second-order methods, such as high computational costs and limited applicability to large models, by using a diagonal Hessian estimator and a clipping mechanism. The proposed method adapts to heterogeneous curvatures across parameter dimensions, leading to faster convergence and improved performance. The authors provide theoretical analyses of Sophia on convex functions and demonstrate its effectiveness through extensive experiments on language modeling and SuperGLUE tasks, showing that Sophia achieves a 2x speedup compared to AdamW and other optimizers.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow, with a clear motivation and a well-structured presentation of the proposed method.
- The proposed method is simple and easy to implement, making it accessible to a wide range of practitioners.
- The paper provides a comprehensive set of experiments, including ablation studies on different components of Sophia, comparisons with other optimizers, and evaluations on both language modeling and SuperGLUE tasks.
- The paper includes a theoretical analysis of Sophia on convex functions, which provides insights into the convergence properties of the method.

### Weaknesses

#### Some Related Works

[1] On the relationship between Hessian and Fisher information matrices in stochastic gradient descent
[2] A second-order stochastic optimization framework for language modeling

#### comment

 - The paper does not provide a detailed comparison of Sophia with other second-order methods, such as KLBFGS, in terms of computational cost and memory usage. While the authors mention that Sophia is computationally efficient, they do not provide a quantitative analysis of the trade-offs between computational cost and performance. A more detailed comparison with other second-order methods would be beneficial to understand the advantages and limitations of Sophia.
- The paper does not provide a detailed analysis of the convergence properties of Sophia in non-convex settings. While the authors provide a theoretical analysis on convex functions, it is not clear how the method performs in practice on non-convex loss landscapes, which are common in deep learning. A more detailed analysis of the convergence properties of Sophia in non-convex settings would be beneficial to understand the limitations of the method.
- The paper does not provide a detailed discussion of the limitations of Sophia, such as its sensitivity to hyperparameters and its performance on different types of models. A more detailed discussion of the limitations of the method would be beneficial to understand its applicability and limitations.
- The paper does not provide a detailed discussion of the relationship between the Hessian and the Fisher information matrix, which is relevant to the proposed method. A more detailed discussion of the relationship between the Hessian and the Fisher information matrix would be beneficial to understand the theoretical properties of the method.
- The paper does not provide a detailed discussion of the relationship between the proposed method and other second-order methods, such as those based on the Gauss-Newton matrix. A more detailed discussion of the relationship between the proposed method and other second-order methods would be beneficial to understand the novelty of the method.
- The paper does not provide a detailed discussion of the relationship between the proposed method and other second-order methods, such as those based on the Gauss-Newton matrix. A more detailed discussion of the relationship between the proposed method and other second-order methods would be beneficial to understand the novelty of the method.

### Suggestions

The paper would benefit from a more thorough comparison with existing second-order optimization methods, particularly KLBFGS. While the authors claim computational efficiency, a detailed analysis of the computational cost, including time and memory requirements, is needed. This should include a breakdown of the operations involved in Sophia and how they compare to those in KLBFGS. For instance, the paper should quantify the overhead of computing the diagonal Hessian estimator and the clipping mechanism, and compare it to the cost of the line search in KLBFGS. Furthermore, the paper should provide a more detailed analysis of the memory usage of Sophia, especially in comparison to other second-order methods. This analysis should consider the memory footprint of storing the Hessian approximation and intermediate variables. A quantitative comparison of these aspects would provide a clearer understanding of the practical trade-offs between Sophia and other methods.

To strengthen the theoretical analysis, the paper should include a more detailed discussion of the convergence properties of Sophia in non-convex settings. While the authors provide a theoretical analysis on convex functions, it is crucial to understand how the method behaves in practice on non-convex loss landscapes. This could involve analyzing the behavior of the method in regions of the loss landscape with varying curvature and sharpness. The paper should also discuss the potential limitations of the method in non-convex settings, such as the possibility of getting stuck in local minima or saddle points. Furthermore, the paper should explore the relationship between the Hessian and the Fisher information matrix, which is relevant to the proposed method. A more detailed discussion of this relationship would provide a deeper understanding of the theoretical properties of the method and its connection to other optimization techniques. This discussion should include a comparison of the computational cost and convergence properties of using the Hessian versus the Fisher information matrix.

Finally, the paper should provide a more detailed discussion of the limitations of Sophia, such as its sensitivity to hyperparameters and its performance on different types of models. The paper should also discuss the potential challenges of applying Sophia to very large models and datasets. This discussion should include an analysis of the scalability of the method and its potential limitations in such scenarios. Furthermore, the paper should explore the relationship between the proposed method and other second-order methods, such as those based on the Gauss-Newton matrix. A more detailed discussion of the relationship between the proposed method and other second-order methods would be beneficial to understand the novelty of the method. This discussion should include a comparison of the computational cost, memory usage, and convergence properties of Sophia and other second-order methods. This would help to clarify the unique contributions of the proposed method and its potential advantages over existing techniques.

### Questions

- How does the proposed method compare with other second-order methods, such as KLBFGS, in terms of computational cost and memory usage?
- What are the convergence properties of Sophia in non-convex settings?
- What are the limitations of Sophia, such as its sensitivity to hyperparameters and its performance on different types of models?
- How does the proposed method relate to other second-order methods, such as those based on the Gauss-Newton matrix?

### Rating

6

### Confidence

4

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in a given paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

Plan:
1. Read each reviewer's weakness.
2. Find the corresponding section in the paper.
3. Look for evidence (quotes, formulas, missing information) to support the weakness.
4. If the weakness is about missing information, check if the information is indeed absent.
5. If the weakness is about a claim, check if the claim is supported by evidence.
6. If there are conflicting opinions, note them.
7. Summarize the evidence and conclude if the weakness is valid, partially valid, or invalid.
```json
[
  {
    "Weakness Statement": "The paper lacks a detailed discussion on the computational overhead of Sophia compared to AdamW and other optimizers. While the authors claim that Sophia is computationally efficient, they do not provide a thorough analysis of the time and memory costs associated with computing and storing the diagonal Hessian information. Specifically, the paper should include a breakdown of the time spent on forward and backward passes, as well as the overhead of Hessian computation and parameter updates. Furthermore, the memory footprint of Sophia, including the storage of the Hessian approximation and other optimizer states, should be compared to that of AdamW. A detailed comparison of the time and memory costs per iteration would be beneficial to understand the practical implications of using Sophia.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        {
          "quote": "The update rule for Sophia is given by: \n\\begin{equation} \\label{eq: Sophia} \\theta_{t + 1} \\leftarrow \\theta_{t} - \\eta \\cdot \\text{ Sophia}(\\theta_{t}, \\mathcal{L}) \\end{equation}",
          "section": "Method"
        },
        {
          "quote": " Sophia uses a diagonal Hessian estimator, which is a simplified version of the full Hessian matrix. The diagonal Hessian is computed using a moving average of the gradients over a small number of steps. The update rule for Sophia is given by: \n\\begin{equation} \\label{eq: Sophia} \\theta_{t + 1} \\leftarrow \\theta_{t} - \\eta \\cdot \\text{ Sophia}(\\theta_{t}, \\mathcal{L}) \\end{equation}",
          "section": "Method"
        },
        {
          "quote": " Sophia is a lightweight second-order optimizer that uses a diagonal Hessian estimator and a clipping mechanism to control the worst-case update size. The optimizer is designed to be computationally efficient and can be easily integrated into existing training pipelines.",
          "section": "Method"
        },
        {
          "quote": " Sophia is a lightweight second-order optimizer that uses a diagonal Hessian estimator and a clipping mechanism to control the worst-case update size. The optimizer is designed to be computationally efficient and can be easily integrated into existing training pipelines. Sophia's computational efficiency is demonstrated through extensive experiments, showing that it achieves a 2x speedup compared to AdamW in terms of steps, total compute, and wall-clock time.",
          "section": "Method"
        }
      ],
      "b) Experiment-related Evidence": [
        {
          "quote": "We compare the total compute (TFLOPs) per step, the wall-clock time on A100 GPUs, and the memory usage of Sophia and AdamW.",
          "section": "Experiments"
        },
        {
          "quote": "Table 1: Comparison of Total Compute (TFLOPs), Wall-clock Time, and Memory Usage per Step for Sophia and AdamW on GPT-2 (125M) and GPT-NeoX (1.5B) models.",
          "section": "Experiments"
        },
        {
          "quote": "Table 1 shows that Sophia achieves a 2x speedup in terms of steps, total compute, and wall-clock time compared to AdamW. The memory usage of Sophia is comparable to AdamW, with a slight increase due to the storage of the diagonal Hessian information.",
          "section": "Experiments"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper claims computational efficiency and provides experimental results comparing Sophia to AdamW in terms of steps, total compute, and wall-clock time. It also mentions memory usage comparison in Table 1.",
      "Supporting quotes": [
        "The optimizer is designed to be computationally efficient...",
        "Sophia's computational efficiency is demonstrated through extensive experiments, showing that it achieves a 2x speedup compared to AdamW...",
        "Table 1: Comparison of Total Compute (TFLOPs), Wall-clock Time, and Memory Usage per Step for Sophia and AdamW..."
      ],
      "Impact assessment": "While the paper claims computational efficiency and provides some comparative data, it lacks a detailed breakdown of the computational cost of each step, including Hessian-vector product and parameter update, and doesn't explicitly compare memory footprint beyond the table."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper claims computational efficiency and provides some comparative data, but lacks a detailed breakdown of computational costs and a comprehensive memory footprint comparison."
    }
  },
  {
    "Weakness Statement": "The paper does not provide a clear explanation of how Sophia handles the non-convexity of the loss landscape. While the authors mention that Sophia adapts to heterogeneous curvatures, they do not elaborate on how this adaptation prevents the optimizer from getting stuck in sharp minima or local optima. A more detailed discussion of the theoretical properties of Sophia, particularly in the context of non-convex optimization, would be valuable. For example, the paper could discuss the convergence properties of Sophia and how they compare to those of AdamW. Additionally, the paper should address the potential limitations of using a diagonal Hessian approximation, which may not capture the full curvature information of the loss landscape. The authors could discuss the trade-offs between computational efficiency and accuracy when using a diagonal Hessian approximation. Furthermore, the paper could explore the use of more sophisticated Hessian approximations, such as block-diagonal approximations, to improve the performance of Sophia.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        {
          "quote": "We use θ t to denote the parameter at time step t t . At each step, we sample a mini-batch from the data distribution and calculate the mini-batch loss, denoted by L t ⟨ 1 ⟩ . We denote by g t the gradient of L t ⟨ 1 ⟩ with respect to the same run-time step t t . Let m t ← β 1 ⟨ h t / max ⁡ { γ ⋅ h t , ϵ } , ϵ ) and if t ⟨ mod ⁡ k = 1 ; else h t = h t − 1 . At time step t t with t ⟨ mod ⁡ k = 1 , the estimator returns an estimate h t of the diagonal of the Hessian of the mini-batch loss.",
          "section": "Method"
        },
        {
          "quote": "In the context of neural networks, past works have found that the second derivative of L 1 ( θ , ( x , y ) ) = L 1 / 2 ( x , y ) + L 2 / 2 ( x , y ) where L 1 ( θ , ( x , y ) ) has the well-known Gauss-Newton decomposition ( Ortega & Rheinboldt, 2000 ; Schraudolph, 2002 ) (which is a simple consequence of the chain rule), because ℋ 1 ( θ , x ) has the well-known Gauss-Newton decomposition ( Ortega & Rheinboldt, 2000 ; Schraudolph, 2002 ; Chen, 2011 ) and used as pre-conditioners in second-order optimizers ( Botev & Le Cun, 2017 ; Martens, 2020 ; Gargiani et al., 2020 ) . Following this line of work, we build an unbiased estimator for the diagonal of the Gauss-Newton matrix, which is a biased estimator for the diagonal of the Hessian.",
          "section": "Method"
        },
        {
          "quote": "We introduce two diagonal Hessian estimators, both of which have memory and run-time costs similar to computing a gradient (up to constant factors).",
          "section": "Method"
        },
        {
          "quote": "Option 1: Hutchinson’s unbiased estimator. For any loss function ℓ ⁡ ( θ , ( x , y ) ) , the Hutchinson’s estimator ( Hutchinson, 1989 ; Roosta & Ascher, 2015 ; Yao et al., 2021 ) first draws u ⁡ ( θ , x ) ∼ U ⁡ ( R d ) , and then outputs h ^ = u ⊙ ( ∇ 2 ℓ ⁡ ( θ , x ) ) ⊙ u , where ⊙ denotes the element-wise product, and ∇ 2 ℓ ⁡ ( θ , x ) ⊙ u is the product of the Hessian with the vector u u . The Hutchinson’s estimator is an unbiased estimator for the diagonal of the Hessian, because 𝔼 ⁡ [ h ^ ] = diag ⁡ ( ∇ 2 ℓ ⁡ ( θ , x ) ) .",
          "section": "Method"
        },
        {
          "quote": "Option 2: Gauss-Newton-Bartlett (GNB) estimator. We leverage the structure of the loss to design a biased stochastic estimator for the diagonal of the Gauss-Newton matrix, following Schraudolph (2002) ; Martens (2020) ; Wei et al. (2020) . Suppose ℓ ⁡ ( θ , ( x , y ) ) is a loss function on parameters θ ∈ ℝ d , and ℓ ⁡ ( θ , ( x , y ) ) = ℓ ⁡ ( θ , x ) + ℓ ⁡ ( θ , y ) . The Hessian of ℓ ⁡ ( θ , ( x , y ) ) (w.r.t to variable θ ) has the well-known Gauss-Newton decomposition ( Ortega & Rheinboldt, 2000 ) , which is a simple consequence of the chain rule, and used as pre-conditioners in second-order optimizers ( Botev & Le Cun, 2017 ; Martens, 2020 ; Gargiani et al., 2020 ) . Following this line of work, we build an unbiased estimator for the diagonal of the Gauss-Newton matrix for the Hessian of the mini-batch loss is given by: J θ = 1 2 ∇ 2 ℓ ce ( f ⁡ ( θ , x ) , y ) ⋅ S ⋅ J θ f ( θ , x ) ⋅ S T + J θ ce ( f ⁡ ( θ , x ) , y ) ⋅ ∇ θ ℓ ce ( f ⁡ ( θ , x ) , y ) .",
          "section": "Method"
        }
      ],
      "b) Experiment-related Evidence": [
        {
          "quote": "We name the algorithm using the Hutchinson’s unbiased estimator and the GNB estimator as Sophia-H and Sophia-G, respectively.",
          "section": "Experiments"
        },
        {
          "quote": "We compare Sophia and AdamW on auto-regressive language modeling with GPT-2 ( Radford et al., 2019 ) of model sizes ranging from 125M to 770M, and GPT NeoX ( Black et al., 2022 ) of sizes 1.5B and 6.6B. Results indicate that Sophia is 2x faster than AdamW in number of steps, total compute, and wall-clock time (see Figure 1 (a)&(b)). Moreover, the scaling law based on the number of parameters in Sophia is in favor of Sophia over AdamW—the gap between Sophia and AdamW with 13B parameters is larger than the gap with 350M parameters (see Figure 1 (c)).",
          "section": "Experiments"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper mentions the diagonal Hessian estimator and its memory and runtime costs being similar to a gradient. It also discusses the Gauss-Newton decomposition and mentions using it as a pre-conditioner. The experiments compare Sophia-H and Sophia-G with AdamW.",
      "Supporting quotes": [
        "We introduce two diagonal Hessian estimators...",
        "Option 1: Hutchinson’s unbiased estimator...",
        "Option 2: Gauss-Newton-Bartlett (GNB) estimator...",
        "We compare Sophia and AdamW..."
      ],
      "Impact assessment": "While the paper describes the diagonal Hessian estimator and mentions the Gauss-Newton decomposition, it doesn't provide a detailed theoretical analysis of how this handles non-convexity or the convergence properties in non-convex settings. The experimental section compares Sophia-H and Sophia-G with AdamW but doesn't delve into the theoretical implications of using a diagonal Hessian approximation in non-convex landscapes."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper describes the diagonal Hessian estimator and mentions the Gauss-Newton decomposition but lacks a detailed theoretical analysis of non-convexity and convergence properties."
    }
  },
  {
    "Weakness Statement": "The paper does not provide a strong justification for why a diagonal Hessian is sufficient for effective optimization in the context of large language models, especially given that the loss landscape is likely to be highly non-convex and anisotropic. The authors should provide more theoretical or empirical evidence to support this choice.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        {
          "quote": "We introduce two diagonal Hessian estimators, both of which have memory and run-time costs similar to computing a gradient (up to constant factors).",
          "section": "Method"
        },
        {
          "quote": "The update rule for Sophia is given by: \n\\begin{equation} \\label{eq: Sophia} \\theta_{t + 1} \\leftarrow \\theta_{t} - \\eta \\cdot \\text{ Sophia}(\\theta_{t}, \\mathcal{L}) \\end{equation}",
          "section": "Method"
        },
        {
          "quote": " Sophia is a lightweight second-order optimizer that uses a diagonal Hessian estimator and a clipping mechanism to control the worst-case update size. The optimizer is designed to be computationally efficient and can be easily integrated into existing training pipelines.",
          "section": "Method"
        }
      ],
      "b) Experiment-related Evidence": [
        {
          "quote": "We compare Sophia and AdamW on auto-regressive language modeling with GPT-2 ( Radford et al., 2019 ) of model sizes ranging from 125M to 770M, and GPT NeoX ( Black et al., 2022 ) of sizes 1.5B and 6.6B. Results indicate that Sophia is 2x faster than AdamW in number of steps, total compute, and wall-clock time (see Figure 1 (a)&(b)). Moreover, the scaling law based on the number of parameters in Sophia is in favor of Sophia over AdamW—the gap between Sophia and AdamW with 13B parameters is larger than the gap with 350M parameters (see Figure 1 (c)).",
          "section": "Experiments"
        },
        {
          "quote": "We name the algorithm using the Hutchinson’s unbiased estimator and the GNB estimator as Sophia-H and Sophia-G, respectively.",
          "section": "Experiments"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper introduces the diagonal Hessian estimator and compares Sophia-H and Sophia-G with AdamW. The experimental results show faster convergence for Sophia.",
      "Supporting quotes": [
        "We introduce two diagonal Hessian estimators...",
        "The update rule for Sophia is given by:...",
        "Sophia is a lightweight second-order optimizer that uses a diagonal Hessian estimator...",
        "We compare Sophia and AdamW...",
        "We name the algorithm using the Hutchinson’s unbiased estimator and the GNB estimator as Sophia-H and Sophia-G, respectively."
      ],
      "Impact assessment": "The paper justifies the use of a diagonal Hessian by showing empirical improvements over AdamW. However, it lacks a strong theoretical justification for why a diagonal approximation is sufficient for the complex, non-convex loss landscapes of large language models. The paper doesn't provide theoretical analysis or specific empirical evidence (beyond the overall performance) to support this choice."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper lacks a strong theoretical justification for using a diagonal Hessian estimator for large language models with non-convex loss landscapes, relying primarily on empirical results."
    }
  },
  {
    "Weakness Statement": "The paper lacks a thorough analysis of the computational cost of the proposed method. While the authors claim that the diagonal Hessian estimator is computationally efficient, they do not provide a detailed breakdown of the computational complexity of each step in the algorithm, including the Hessian-vector product and the parameter update. A comparison of the computational cost of Sophia with other second-order methods, such as KLBFGS, would be beneficial.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        {
          "quote": "The update rule for Sophia is given by: \n\\begin{equation} \\label{eq: Sophia} \\theta_{t + 1} \\leftarrow \\theta_{t} - \\eta \\cdot \\text{ Sophia}(\\theta_{t}, \\mathcal{L}) \\end{equation}",
          "section": "Method"
        },
        {
          "quote": " Sophia uses a diagonal Hessian estimator, which is a simplified version of the full Hessian matrix. The diagonal Hessian is computed using a moving average of the gradients over a small number of steps. The update rule for Sophia is given by: \n\\begin{equation} \\label{eq: Sophia} \\theta_{t + 1} \\leftarrow \\theta_{t} - \\eta \\cdot \\text{ Sophia}(\\theta_{t}, \\mathcal{L}) \\end{equation}",
          "section": "Method"
        },
        {
          "quote": " Sophia is a lightweight second-order optimizer that uses a diagonal Hessian estimator and a clipping mechanism to control the worst-case update size. The optimizer is designed to be computationally efficient and can be easily integrated into existing training pipelines.",
          "section": "Method"
        },
        {
          "quote": " Sophia is a lightweight second-order optimizer that uses a diagonal Hessian estimator and a clipping mechanism to control the worst-case update size. The optimizer is designed to be computationally efficient and can be easily integrated into existing training pipelines. Sophia's computational efficiency is demonstrated through extensive experiments, showing that it achieves a 2x speedup compared to AdamW in terms of steps, total compute, and wall-clock time.",
          "section": "Method"
        }
      ],
      "b) Experiment-related Evidence": [
        {
          "quote": "We compare the total compute (TFLOPs) per step, the wall-clock time on A100 GPUs, and the memory usage of Sophia and AdamW.",
          "section": "Experiments"
        },
        {
          "quote": "Table 1: Comparison of Total Compute (TFLOPs), Wall-clock Time, and Memory Usage per Step for Sophia and AdamW on GPT-2 (125M) and GPT-NeoX (1.5B) models.",
          "section": "Experiments"
        },
        {
          "quote": "Table 1 shows that Sophia achieves a 2x speedup in terms of steps, total compute, and wall-clock time compared to AdamW.",
          "section": "Experiments"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper claims computational efficiency and provides experimental results comparing Sophia to AdamW in terms of steps, total compute, and wall-clock time. It also mentions memory usage comparison in Table 1.",
      "Supporting quotes": [
        "The optimizer is designed to be computationally efficient...",
        "Sophia's computational efficiency is demonstrated through extensive experiments, showing that it achieves a 2x speedup compared to AdamW...",
        "Table 1: Comparison of Total Compute (TFLOPs), Wall-clock Time, and Memory Usage per Step for Sophia and AdamW..."
      ],
      "Impact assessment": "While the paper claims computational efficiency and provides some comparative data, it lacks a detailed breakdown of the computational cost of each step, including Hessian-vector product and parameter update, and doesn't explicitly compare memory footprint beyond the table."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper claims computational efficiency and provides some comparative data, but lacks a detailed breakdown of computational costs and a comprehensive memory footprint comparison."
    }
  },
  {
    "Weakness Statement": "The paper does not provide a clear explanation of how the proposed method handles the non-convexity of the loss landscape. They mention that the method adapts to heterogeneous curvatures, but they do not elaborate on how this adaptation prevents the optimizer from getting stuck in sharp minima or local optima. A more detailed discussion of the theoretical properties of Sophia, particularly in the context of non-convex optimization, would be valuable. For example, the paper could discuss the convergence properties of Sophia and how they compare to those of AdamW. Additionally, the paper should address the potential limitations of using a diagonal Hessian approximation, which may not capture the full curvature information of the loss landscape. The authors could discuss the trade-offs between computational efficiency and accuracy when using a diagonal Hessian approximation. Furthermore, the paper could explore the use of more sophisticated Hessian approximations, such as block-diagonal approximations, to improve the performance of Sophia.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        {
          "quote": "We use θ t to denote the parameter at time step t t . At each step, we sample a mini-batch from the data distribution and calculate the mini-batch loss, denoted by L t ⟨ 1 ⟩ . We denote by g t the gradient of L t ⟨ 1 ⟩ with respect to the same run-time step t t . Let m t ← β 1 ⟨ h t / max ⁡ { γ ⋅ h t , ϵ } , ϵ ) and if t ⟨ mod ⁡ k = 1 ; else h t = h t − 1 . At time step t t with t ⟨ mod ⁡ k = 1 , the estimator returns an estimate h t of the diagonal of the Hessian of the mini-batch loss.",
          "section": "Method"
        },
        {
          "quote": "In the context of neural networks, past works have found that the second derivative of L 1 ( θ , ( x , y ) ) = L 1 / 2 ( x , y ) + L 2 / 2 ( x , y ) where L 1 ( θ , ( x , y ) ) has the well-known Gauss-Newton decomposition ( Ortega & Rheinboldt, 2000 ; Schraudolph, 2002 ) (which is a simple consequence of the chain rule), because ℋ 1 ( θ , x ) has the well-known Gauss-Newton decomposition ( Ortega & Rheinboldt, 2000 ; Schraudolph, 2002 ; Chen, 2011 ) and used as pre-conditioners in second-order optimizers ( Botev & Le Cun, 2017 ; Martens, 2020 ; Gargiani et al., 2020 ) . Following this line of work, we build an unbiased estimator for the diagonal of the Gauss-Newton matrix, which is a biased estimator for the diagonal of the Hessian.",
          "section": "Method"
        },
        {
          "quote": "We introduce two diagonal Hessian estimators, both of which have memory and run-time costs similar to computing a gradient (up to constant factors).",
          "section": "Method"
        }
      ],
      "b) Experiment-related Evidence": [
        {
          "quote": "We compare Sophia and AdamW on auto-regressive language modeling with GPT-2 ( Radford et al., 2019 ) of model sizes ranging from 125M to 770M, and GPT NeoX ( Black et al., 2022 ) of sizes 1.5B and 6.6B. Results indicate that Sophia is 2x faster than AdamW in number of steps, total compute, and wall-clock time (see Figure 1 (a)&(b)). Moreover, the scaling law based on the number of parameters in Sophia is in favor of Sophia over AdamW—the gap between Sophia and AdamW with 13B parameters is larger than the gap with 350M parameters (see Figure 1 (c)).",
          "section": "Experiments"
        },
        {
          "quote": "We name the algorithm using the Hutchinson’s unbiased estimator and the GNB estimator as Sophia-H and Sophia-G, respectively.",
          "section": "Experiments"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper introduces the diagonal Hessian estimator and mentions the Gauss-Newton decomposition. The experiments compare Sophia-H and Sophia-G with AdamW. The paper claims computational efficiency and shows empirical improvements.",
      "Supporting quotes": [
        "We introduce two diagonal Hessian estimators...",
        "The update rule for Sophia is given by:...",
        "Sophia is a lightweight second-order optimizer that uses a diagonal Hessian estimator...",
        "We compare Sophia and AdamW...",
        "We name the algorithm using the Hutchinson’s unbiased estimator and the GNB estimator as Sophia-H and Sophia-G, respectively."
      ],
      "Impact assessment": "The paper lacks a detailed theoretical analysis of how the diagonal Hessian estimator handles non-convexity or the convergence properties in non-convex settings. The experimental section compares Sophia-H and Sophia-G with AdamW but doesn't delve into the theoretical implications of using a diagonal Hessian approximation in non-convex landscapes."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper describes the diagonal Hessian estimator and mentions the Gauss-Newton decomposition but lacks a detailed theoretical analysis of non-convexity and convergence properties."
    }
  },
  {
    "Weakness Statement": "How does the proposed method handle the non-convexity of the loss landscape?",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        {
          "quote": "We use θ t to denote the parameter at time step t t . At each step, we sample a mini-batch from the data distribution and calculate the mini-batch loss, denoted by L t ⟨ 1 ⟩ . We denote by g t the gradient of L t ⟨ 1 ⟩ with respect to the same run-time step t t . Let m t ← β 1 ⟨ h t / max ⁡ { γ ⋅ h t , ϵ } , ϵ ) and if t ⟨ mod ⁡ k = 1 ; else h t = h t − 1 . At time step t t with t ⟨ mod ⁡ k = 1 , the estimator returns an estimate h t of the diagonal of the Hessian of the mini-batch loss.",
          "section": "Method"
        },
        {
          "quote": "In the context of neural networks, past works have found that the second derivative of L 1 ( θ , ( x , y ) ) = L 1 / 2 ( x , y ) + L 2 / 2 ( x , y ) where L 1 ( θ , ( x , y ) ) has the well-known Gauss-Newton decomposition ( Ortega & Rheinboldt, 2000 ; Schraudolph, 2002 ) (which is a simple consequence of the chain rule), because ℋ 1 ( θ , x ) has the well-known Gauss-Newton decomposition ( Ortega & Rheinboldt, 2000 ; Schraudolph, 2002 ; Chen, 2011 ) and used as pre-conditioners in second-order optimizers ( Botev & Le Cun, 2017 ; Martens, 2020 ; Gargiani et al., 2020 ) . Following this line of work, we build an unbiased estimator for the diagonal of the Gauss-Newton matrix, which is a biased estimator for the diagonal of the Hessian.",
          "section": "Method"
        },
        {
          "quote": "We introduce two diagonal Hessian estimators, both of which have memory and run-time costs similar to computing a gradient (up to constant factors).",
          "section": "Method"
        }
      ],
      "b) Experiment-related Evidence": [
        {
          "quote": "We compare Sophia and AdamW on auto-regressive language modeling with GPT-2 ( Radford et al., 2019 ) of model sizes ranging from 125M to 770M, and GPT NeoX ( Black et al., 2022 ) of sizes 1.5B and 6.6B. Results indicate that Sophia is 2x faster than AdamW in number of steps, total compute, and wall-clock time (see Figure 1 (a)&(b)). Moreover, the scaling law based on the number of parameters in Sophia is in favor of Sophia over AdamW—the gap between Sophia and AdamW with 13B parameters is larger than the gap with 350M parameters (see Figure 1 (c)).",
          "section": "Experiments"
        },
        {
          "quote": "We name the algorithm using the Hutchinson’s unbiased estimator and the GNB estimator as Sophia-H and Sophia-G, respectively.",
          "section": "Experiments"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper introduces the diagonal Hessian estimator and mentions the Gauss-Newton decomposition. The experiments compare Sophia-H and Sophia-G with AdamW. The paper claims computational efficiency and shows empirical improvements.",
      "Supporting quotes": [
        "We introduce two diagonal Hessian estimators...",
        "The update rule for Sophia is given by:...",
        "Sophia is a lightweight second-order optimizer that uses a diagonal Hessian estimator...",
        "We compare Sophia and AdamW...",
        "We name the algorithm using the Hutchinson’s unbiased estimator and the GNB estimator as Sophia-H and Sophia-G, respectively."
      ],
      "Impact assessment": "The paper lacks a detailed theoretical analysis of how the diagonal Hessian estimator handles non-convexity or the convergence properties in non-convex settings. The experimental section compares Sophia-H and Sophia-G with AdamW but doesn't delve into the theoretical implications of using a diagonal Hessian approximation in non-convex landscapes."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper describes the diagonal Hessian estimator and mentions the Gauss-Newton decomposition but lacks a detailed theoretical analysis of non-convexity and convergence properties."
    }
  },
  {
    "Weakness Statement": "How does the proposed method relate to other second-order methods, such as KLBFGS, in terms of computational cost and memory usage?",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        {
          "quote": "The update rule for Sophia is given by: \n\\begin{equation} \\label{eq: Sophia} \\theta_{t + 1} \\leftarrow \\theta_{t} - \\eta \\cdot \\text{ Sophia}(\\theta_{t}, \\mathcal{L}) \\end{equation}",
          "section": "Method"
        },
        {
          "quote": " Sophia is a lightweight second-order optimizer that uses a diagonal Hessian estimator and a clipping mechanism to control the worst-case update size. The optimizer is designed to be computationally efficient and can be easily integrated into existing training pipelines.",
          "section": "Method"
        },
        {
          "quote": "We compare the total compute (TFLOPs) per step, the wall-clock time on A100 GPUs, and the memory usage of Sophia and AdamW.",
          "section": "Experiments"
        },
        {
          "quote": "Table 1: Comparison of Total Compute (TFLOPs), Wall-clock Time, and Memory Usage per Step for Sophia and AdamW on GPT-2 (125M) and GPT-NeoX (1.5B) models.",
          "section": "Experiments"
        }
      ],
      "b) Experiment-related Evidence": [
        {
          "quote": "We compare Sophia and AdamW on auto-regressive language modeling with GPT-2 ( Radford et al., 2019 ) of model sizes ranging from 125M to 770M, and GPT NeoX ( Black et al., 2022 ) of sizes 1.5B and 6.6B. Results indicate that Sophia is 2x faster than AdamW in number of steps, total compute, and wall-clock time (see Figure 1 (a)&(b)). Moreover, the scaling law based on the number of parameters in Sophia is in favor of Sophia over AdamW—the gap between Sophia and AdamW with 13B parameters is larger than the gap with 350M parameters (see Figure 1 (c)).",
          "section": "Experiments"
        },
        {
          "quote": "We name the algorithm using the Hutchinson’s unbiased estimator and the GNB estimator as Sophia-H and Sophia-G, respectively.",
          "section": "Experiments"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper claims computational efficiency and shows empirical improvements over AdamW. It provides a comparison of memory usage in Table 1.",
      "Supporting quotes": [
        "The optimizer is designed to be computationally efficient...",
        "Sophia's computational efficiency is demonstrated through extensive experiments...",
        "Table 1: Comparison of Total Compute (TFLOPs), Wall-clock Time, and Memory Usage per Step for Sophia and AdamW..."
      ],
      "Impact assessment": "The paper claims computational efficiency and provides experimental results comparing Sophia to AdamW in terms of steps, total compute, and wall-clock time. It also includes a table comparing memory usage. However, it lacks a direct comparison with other second-order methods like KLBFGS in terms of computational cost and memory usage."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper claims computational efficiency and provides experimental results comparing Sophia to AdamW, but lacks a direct comparison with other second-order methods like KLBFGS."
    }
  },
  {
    "Weakness Statement": "How does the proposed method relate to other second-order methods, such as those based on the Gauss-Newton matrix,?",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        {
          "quote": "In the context of neural networks, past works have found that the second derivative of L 1 ( θ , ( x , y ) ) = L 1 / 2 ( x , y ) + L 2 / 2 ( x , y ) where L 1 ( θ , ( x , y ) ) has the well-known Gauss-Newton decomposition ( Ortega & Rheinboldt, 2000 ; Schraudolph, 2002 ) (which is a simple consequence of the chain rule), because ℋ 1 ( θ , x ) has the well-known Gauss-Newton decomposition ( Ortega & Rheinboldt, 2000 ; Schraudolph, 2002 ; Chen, 2011 ) and used as pre-conditioners in second-order optimizers ( Botev & Le Cun, 2017 ; Martens, 2020 ; Gargiani et al., 2020 ) . Following this line of work, we build an unbiased estimator for the diagonal of the Gauss-Newton matrix, which is a biased estimator for the diagonal of the Hessian.",
          "section": "Method"
        },
        {
          "quote": "We introduce two diagonal Hessian estimators, both of which have memory and run-time costs similar to computing a gradient (up to constant factors).",
          "section": "Method"
        }
      ],
      "b) Experiment-related Evidence": [
        {
          "quote": "We name the algorithm using the Hutchinson’s unbiased estimator and the GNB estimator as Sophia-H and Sophia-G, respectively.",
          "section": "Experiments"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper mentions the Gauss-Newton decomposition and uses it as a basis for its estimator. It introduces two diagonal Hessian estimators.",
      "Supporting quotes": [
        "In the context of neural networks, past works have found that the second derivative of L 1 ( θ , ( x , y ) ) = L 1 / 2 ( x , y ) + L 2 / 2 ( x , y ) where L 1 ( θ , ( x , y ) ) has the well-known Gauss-Newton decomposition ( Ortega & Rheinboldt, 2000 ; Schraudolph, 2002 ) (which is a simple consequence of the chain rule), because ℋ 1 ( θ , x ) has the well-known Gauss-Newton decomposition ( Ortega & Rheinboldt, 2000 ; Schraudolph, 2002 ; Chen, 2011 ) and used as pre-conditioners in second-order optimizers ( Botev & Le Cun, 2017 ; Martens, 2020 ; Gargiani et al., 2020 ) . Following this line of work, we build an unbiased estimator for the diagonal of the Gauss-Newton matrix, which is a biased estimator for the diagonal of the Hessian.",
        "We introduce two diagonal Hessian estimators, both of which have memory and run-time costs similar to computing a gradient (up to constant factors)."
      ],
      "Impact assessment": "The paper explicitly mentions the Gauss-Newton decomposition and uses it as a basis for its estimator. It introduces two diagonal Hessian estimators. However, it doesn't provide a detailed comparison of Sophia with other second-order methods specifically based on the Gauss-Newton matrix, such as those mentioned in the related work section."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper mentions the Gauss-Newton decomposition and uses it as a basis for its estimator, but lacks a detailed comparison with other second-order methods specifically based on the Gauss-Newton matrix."
    }
  },
  {
    "Weakness Statement": "The paper lacks a detailed comparison of Sophia with other second-order methods, such as KLBFGS, in terms of computational cost and memory usage. While the authors claim computational efficiency, a detailed}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces Sophia, a novel second-order optimization method designed for training large language models. The core idea behind Sophia is to adapt to heterogeneous curvatures across different parameter dimensions by using a diagonal Hessian estimator. This approach aims to address the inefficiencies of traditional second-order methods, which often incur high computational costs due to the need for full Hessian calculations. The authors propose a simplified diagonal Hessian estimator, which is computationally efficient and can be easily integrated into existing training pipelines. The method operates by estimating the diagonal of the Hessian matrix using a moving average of gradients over a small number of steps, and then using this estimate to precondition the gradient update. The paper presents a theoretical analysis of Sophia on convex functions, demonstrating its convergence properties. Empirically, the authors evaluate Sophia on language modeling tasks using GPT-2 and GPT-NeoX models, comparing its performance against AdamW and other optimizers. The results show that Sophia achieves a 2x speedup in terms of steps, total compute, and wall-clock time, while also improving the final performance of the models. The authors also explore two variants of Sophia, Sophia-H and Sophia-G, based on different diagonal Hessian estimators, and compare their performance. Overall, the paper presents a promising approach to efficient second-order optimization for large language models, with strong empirical results and a clear motivation for its design choices. However, as I will discuss in detail, there are several areas where the paper could be strengthened with more rigorous analysis and comparisons.


## Soundness:

2.75


## Presentation:

3.0


## Contribution:

2.25


## Strengths:

I found several aspects of this paper to be particularly strong. First, the core idea of using a diagonal Hessian estimator to adapt to heterogeneous curvatures across parameter dimensions is both simple and elegant. This approach allows Sophia to achieve faster convergence and improved performance without the high computational cost associated with full Hessian calculations. The authors clearly articulate the motivation behind their design choices, making it easy to understand the rationale behind the proposed method. The paper is also well-written and easy to follow, with a clear presentation of the proposed method, the experimental setup, and the results. The authors provide a comprehensive set of experiments, including ablation studies on different components of Sophia, comparisons with other optimizers, and evaluations on both language modeling and SuperGLUE tasks. The empirical results are compelling, demonstrating that Sophia achieves a 2x speedup in terms of steps, total compute, and wall-clock time compared to AdamW, while also improving the final performance of the models. The inclusion of a theoretical analysis on convex functions, while limited, provides some insights into the convergence properties of the method. Finally, the authors provide a clear and concise explanation of the proposed method, making it accessible to a wide range of practitioners. The use of a diagonal Hessian estimator is a practical approach that addresses the computational challenges associated with second-order optimization, and the empirical results demonstrate its effectiveness in training large language models.


## Weaknesses:

Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, while the authors claim that Sophia is computationally efficient, they do not provide a detailed breakdown of the computational cost of each step in the algorithm. Specifically, the paper lacks a detailed analysis of the time spent on forward and backward passes, as well as the overhead of Hessian computation and parameter updates. This lack of a granular analysis makes it difficult to fully assess the practical implications of using Sophia, especially in comparison to other second-order methods. For example, the paper does not quantify the overhead of computing the diagonal Hessian estimate, the Hessian-vector product, and the parameter update, and compare it to that of methods like KLBFGS. This is a significant omission, as the computational cost of these steps can be substantial. The paper also lacks a detailed comparison of the computational cost of Sophia with other second-order methods, such as KLBFGS, in terms of both theoretical complexity and empirical performance on different hardware platforms. This makes it difficult to understand the practical trade-offs between Sophia and other methods. My confidence in this weakness is high, as the paper explicitly claims computational efficiency but does not provide a detailed breakdown of the computational costs of each step. 

Second, the paper does not provide a strong justification for why a diagonal Hessian is sufficient for effective optimization in the context of large language models, especially given that the loss landscape is likely to be highly non-convex and anisotropic. The authors mention that Sophia adapts to heterogeneous curvatures, but they do not elaborate on how this adaptation prevents the optimizer from getting stuck in sharp minima or local optima. While the paper introduces the diagonal Hessian estimator and mentions the Gauss-Newton decomposition, it lacks a strong theoretical justification for why a diagonal approximation is sufficient for the complex, non-convex loss landscapes of large language models. The paper does not provide theoretical or empirical evidence to support this choice. This is a significant limitation, as the diagonal Hessian approximation may not capture the full curvature information of the loss landscape, potentially leading to suboptimal optimization. My confidence in this weakness is high, as the paper lacks a strong theoretical justification for using a diagonal Hessian estimator for large language models with non-convex loss landscapes, relying primarily on empirical results.

Third, the paper lacks a detailed analysis of the convergence properties of Sophia in non-convex settings. While the authors provide a theoretical analysis on convex functions, it is not clear how the method behaves in practice on non-convex loss landscapes, which are common in deep learning. The paper does not discuss the potential limitations of using a diagonal Hessian approximation, which may not capture the full curvature information of the loss landscape. The authors could discuss the trade-offs between computational efficiency and accuracy when using a diagonal Hessian approximation. Furthermore, the paper does not explore the use of more sophisticated Hessian approximations, such as block-diagonal approximations, to improve the performance of Sophia. This is a significant omission, as the convergence properties of Sophia in non-convex settings are not well understood. My confidence in this weakness is high, as the paper lacks a detailed theoretical analysis of non-convexity and convergence properties, and does not compare against more sophisticated Hessian approximations.

Finally, the paper does not provide a detailed comparison of Sophia with other second-order methods, such as KLBFGS, in terms of computational cost and memory usage. While the authors claim computational efficiency, they do not provide a quantitative comparison of the computational cost of Sophia with other second-order methods. This makes it difficult to understand the practical trade-offs between Sophia and other methods. My confidence in this weakness is high, as the paper lacks a direct comparison with other second-order methods like KLBFGS in terms of computational cost and memory usage.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should provide a more detailed analysis of the computational costs associated with Sophia. This should include a breakdown of the time spent on different stages of the optimization process, including the forward and backward passes, as well as the overhead of Hessian computation and parameter updates. A comparison of the computational cost of Sophia with other second-order methods, such as KLBFGS, would be highly informative. This comparison should consider both the theoretical complexity and the empirical performance on different hardware platforms. For instance, the paper should quantify the overhead of computing the diagonal Hessian estimate, the Hessian-vector product, and the parameter update. A comparison of the computational cost of Sophia with other second-order methods would be highly informative. This comparison should consider both the theoretical complexity and the empirical performance on different hardware platforms. For example, the paper could provide a table that shows the time spent on each component of Sophia, such as the Hessian-vector product, and compare it to that of other second-order methods. This would allow readers to better understand the practical implications of using Sophia and to compare it with other methods. Furthermore, the paper should investigate the memory requirements of Sophia, including the storage of the Hessian approximation and the intermediate variables used in the algorithm. A comparison of the memory usage of Sophia with other second-order methods would be beneficial. This analysis should consider the memory usage of storing the Hessian approximation and the intermediate variables used in the algorithm. It is important to understand the practical implications of using a diagonal Hessian approximation in terms of memory usage. It would also be helpful to provide empirical results on the computational cost of Sophia on different hardware platforms. This would provide a more comprehensive understanding of the practical trade-offs between Sophia and other methods.

Second, the authors should provide a more detailed analysis of the diagonal Hessian estimator and its suitability for large language models. Specifically, they should investigate the spectral properties of the Hessian matrix and analyze how the diagonal approximation affects the optimization process. It would be beneficial to compare the performance of Sophia with other diagonal Hessian estimation methods, such as the Gauss-Newton matrix, to understand the trade-offs between computational efficiency and optimization performance. Furthermore, the authors should provide a theoretical analysis of the convergence properties of Sophia, including the conditions under which the method is guaranteed to converge to a local minimum. This analysis should also consider the impact of the diagonal Hessian approximation on the convergence rate. The authors should also address the potential limitations of using a diagonal Hessian approximation, which may not capture the full curvature information of the loss landscape. The authors could discuss the trade-offs between computational efficiency and accuracy when using a diagonal Hessian approximation. Furthermore, the paper should explore the use of more sophisticated Hessian approximations, such as block-diagonal approximations, to improve the performance of Sophia.

Finally, the authors should provide a more detailed explanation of how Sophia handles the non-convexity of the loss landscape. They should analyze the behavior of the method in different regions of the loss landscape, including flat regions, sharp minima, and saddle points. It would be beneficial to provide a theoretical analysis of the convergence properties of Sophia and how they compare to those of AdamW. Additionally, the paper should address the potential limitations of using a diagonal Hessian approximation, which may not capture the full curvature information of the loss landscape. The authors could discuss the trade-offs between computational efficiency and accuracy when using a diagonal Hessian approximation. Furthermore, the paper should explore the use of more sophisticated Hessian approximations, such as block-diagonal approximations, to improve the performance of Sophia. By addressing these points, the authors can significantly strengthen their work and provide a more comprehensive understanding of the proposed method.


## Questions:

I have several questions that arise from my analysis of this paper. First, how does the proposed method compare with other second-order methods, such as KLBFGS, in terms of computational cost and memory usage? While the paper claims computational efficiency, it does not provide a detailed comparison of the computational cost of Sophia with other second-order methods. This makes it difficult to understand the practical trade-offs between Sophia and other methods. Second, how does the proposed method relate to other second-order methods, such as those based on the Gauss-Newton matrix? The paper mentions the Gauss-Newton decomposition and uses it as a basis for its estimator, but it does not provide a detailed comparison of Sophia with other second-order methods specifically based on the Gauss-Newton matrix. This makes it difficult to understand the unique contributions of Sophia in the context of other second-order methods. Third, what is the computational overhead of Sophia compared to other second-order methods? The paper claims computational efficiency, but it does not provide a detailed analysis of the computational cost of each step in the algorithm. This makes it difficult to fully assess the practical implications of using Sophia, especially in comparison to other second-order methods. Fourth, how does the proposed method handle the non-convexity of the loss landscape? The paper mentions that Sophia adapts to heterogeneous curvatures, but it does not elaborate on how this adaptation prevents the optimizer from getting stuck in sharp minima or local optima. This is a significant limitation, as the diagonal Hessian approximation may not capture the full curvature information of the loss landscape, potentially leading to suboptimal optimization. Finally, what are the limitations of using a diagonal Hessian approximation, and how can these limitations be addressed? The paper does not provide a detailed analysis of the potential limitations of using a diagonal Hessian approximation, which may not capture the full curvature information of the loss landscape. This makes it difficult to understand the potential drawbacks of the proposed method.


## Rating:

5.5


## Confidence:

3.75


## Decision:

Reject
}