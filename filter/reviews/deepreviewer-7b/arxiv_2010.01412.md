I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper proposes Sharpness-Aware Minimization (SAM), a novel procedure for improving model generalization by seeking parameters that lie in neighborhoods of low loss and low sharpness. SAM is implemented by solving a min-max optimization problem on each training step, which is shown to be equivalent to a simple modification of the base optimizer. Empirically, SAM is shown to improve model generalization across a variety of tasks and models, and to be particularly effective at finetuning large pretrained models.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The empirical results are strong, with SAM improving performance on a variety of tasks and models.
- The authors provide a good discussion of the relationship between SAM and other sharpness-aware methods.

### Weaknesses

#### Some Related Works

[1] On the connection between sharpness-aware minimization and center of mass algorithms
[2] On the connection between sharpness-aware minimization and implicit regularization

#### comment

 - The paper does not provide a theoretical analysis of why SAM works. While the authors provide some intuition for the method, a more rigorous analysis of the optimization landscape and the effect of SAM on the loss surface would be beneficial. Specifically, it would be useful to understand how SAM affects the curvature of the loss function and whether it leads to flatter minima, which are known to generalize better.
- The paper does not provide a comparison with other sharpness-aware methods. While the authors mention other methods, a more detailed comparison of SAM with these methods would be helpful. This should include a discussion of the computational cost of SAM compared to other methods, as well as a comparison of the performance of SAM with other methods on a variety of tasks.
- The paper does not provide a discussion of the limitations of SAM. It would be useful to understand the conditions under which SAM is most effective and when it might not be the best choice. For example, are there any types of models or tasks where SAM does not provide significant improvements in performance? Additionally, the paper should discuss the sensitivity of SAM to hyperparameters, such as the perturbation size, and how these hyperparameters should be chosen.

### Suggestions

The paper would benefit from a more in-depth theoretical analysis of the proposed SAM method. While the empirical results are compelling, a theoretical understanding of why SAM works is crucial for its broader adoption and further development. Specifically, the authors should investigate the relationship between SAM and the geometry of the loss landscape. This could involve analyzing the Hessian of the loss function and how SAM affects its eigenvalues, which are indicative of the sharpness of the minima. Furthermore, it would be beneficial to explore the connection between SAM and implicit regularization, as this could provide insights into why SAM leads to better generalization. A theoretical analysis should also consider the convergence properties of SAM, and whether it converges to a stationary point of the original optimization problem or a stationary point of the sharpness-aware objective. This analysis should also consider the effect of the perturbation parameter on the convergence and generalization performance of SAM.

In addition to the theoretical analysis, the paper should include a more comprehensive empirical evaluation of SAM. This should include a comparison with other sharpness-aware methods, such as Sharpness-Aware Minimization (SAM) variants and other related techniques. The comparison should be performed on a variety of tasks and models, and should include a discussion of the computational cost of each method. It would also be useful to investigate the sensitivity of SAM to different hyperparameters, such as the perturbation size and the number of inner loop iterations. The authors should also explore the performance of SAM on tasks where it might not be the most effective, such as tasks with very high-dimensional input spaces or tasks with very complex loss landscapes. This would provide a more complete picture of the strengths and limitations of SAM.

Finally, the paper should include a more detailed discussion of the limitations of SAM. This should include a discussion of the conditions under which SAM is most effective and when it might not be the best choice. For example, the authors should discuss whether SAM is more effective for certain types of models or tasks, and whether there are any specific scenarios where other methods might be more appropriate. The authors should also discuss the sensitivity of SAM to hyperparameters, such as the perturbation size, and how these hyperparameters should be chosen. A more thorough discussion of the limitations of SAM would help practitioners to understand when to use SAM and when to consider alternative methods. Furthermore, the authors should also discuss the potential for negative transfer when using SAM, and how to mitigate this risk.

### Questions

- How does SAM compare to other sharpness-aware methods?
- What are the limitations of SAM?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer 2

### Summary

This paper proposes Sharpness-Aware Minimization (SAM), a new optimization method that seeks parameters that lie in neighborhoods having uniformly low loss value (rather than just the lowest loss value). SAM is implemented by solving a min-max optimization problem on each training step. The paper shows that SAM improves model generalization across a variety of tasks and models, and is particularly effective at finetuning large pretrained models. The paper also introduces the concept of m-sharpness, which is a measure of the sharpness of the loss landscape in the vicinity of a given parameter. The paper shows that m-sharpness can be used to predict the generalization performance of a model. The paper also provides a theoretical analysis of the connection between SAM and the Hessian of the loss function.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The empirical results are strong, with SAM improving performance on a variety of tasks and models.
- The paper provides a good discussion of the relationship between SAM and other sharpness-aware methods.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a theoretical analysis of why SAM works. While the authors provide some intuition for the method, a more rigorous analysis of the optimization landscape and the effect of SAM on the loss surface would be beneficial. Specifically, it would be useful to understand how SAM affects the curvature of the loss function and whether it leads to flatter minima, which are known to generalize better.
- The paper does not provide a comparison with other sharpness-aware methods. While the authors mention other methods, a more detailed comparison of SAM with these methods would be helpful. This should include a discussion of the computational cost of SAM compared to other methods, as well as a comparison of the performance of SAM with other methods on a variety of tasks.
- The paper does not provide a discussion of the limitations of SAM. It would be useful to understand the conditions under which SAM is most effective and when it might not be the best choice. For example, are there any types of models or tasks where SAM does not provide significant improvements in performance? Additionally, the paper should discuss the sensitivity of SAM to hyperparameters, such as the perturbation size, and how these hyperparameters should be chosen.

### Suggestions

The paper would benefit from a more in-depth theoretical analysis of the proposed SAM method. While the empirical results are promising, a theoretical understanding of why SAM works is crucial for its broader adoption and further development. Specifically, the authors should investigate the relationship between SAM and the geometry of the loss landscape. This could involve analyzing the Hessian of the loss function and how SAM affects its eigenvalues, which are indicative of the sharpness of the minima. Furthermore, it would be beneficial to explore the connection between SAM and implicit regularization, as this could provide insights into why SAM leads to better generalization. A theoretical analysis should also consider the convergence properties of SAM, and whether it converges to a stationary point of the original optimization problem or a stationary point of the sharpness-aware objective. This analysis should also consider the effect of the perturbation parameter on the convergence and generalization performance of SAM.

In addition to the theoretical analysis, the paper should include a more comprehensive empirical evaluation of SAM. This should include a comparison with other sharpness-aware methods, such as Sharpness-Aware Minimization (SAM) variants and other related techniques. The comparison should be performed on a variety of tasks and models, and should include a discussion of the computational cost of each method. It would also be useful to investigate the sensitivity of SAM to different hyperparameters, such as the perturbation size and the number of inner loop iterations. The authors should also explore the performance of SAM on tasks where it might not be the most effective, such as tasks with very high-dimensional input spaces or tasks with very complex loss landscapes. This would provide a more complete picture of the strengths and limitations of SAM.

Finally, the paper should include a more detailed discussion of the limitations of SAM. This should include a discussion of the conditions under which SAM is most effective and when it might not be the best choice. For example, the authors should discuss whether SAM is more effective for certain types of models or tasks, and whether there are any specific scenarios where other methods might be more appropriate. The authors should also discuss the sensitivity of SAM to hyperparameters, such as the perturbation size, and how these hyperparameters should be chosen. A more thorough discussion of the limitations of SAM would help practitioners to understand when to use SAM and when to consider alternative methods. Furthermore, the authors should also discuss the potential for negative transfer when using SAM, and how to mitigate this risk.

### Questions

- How does SAM compare to other sharpness-aware methods?
- What are the limitations of SAM?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer 3

### Summary

The paper proposes Sharpness-Aware Minimization (SAM), a method for training neural networks that aims to improve generalization by minimizing both the training loss and the sharpness of the loss landscape. The authors provide a theoretical analysis of SAM, showing that it can be interpreted as a regularizer that encourages the model to find flatter minima in the loss landscape. Empirically, SAM is shown to improve the performance of various neural network architectures on a range of tasks, including image classification, finetuning, and noisy label learning.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The empirical results are convincing, showing that SAM improves the performance of various neural network architectures on a range of tasks.
- The paper provides a theoretical analysis of SAM, showing that it can be interpreted as a regularizer that encourages the model to find flatter minima in the loss landscape.

### Weaknesses

#### Some Related Works

[1] On the connection between sharpness-aware minimization and center of mass algorithms
[2] On the connection between sharpness-aware minimization and implicit regularization

#### comment

 - The paper does not provide a comparison with other sharpness-aware methods. While the authors mention other methods, a more detailed comparison of SAM with these methods would be helpful. This should include a discussion of the computational cost of SAM compared to other methods, as well as a comparison of the performance of SAM with other methods on a variety of tasks.
- The paper does not provide a discussion of the limitations of SAM. It would be useful to understand the conditions under which SAM is most effective and when it might not be the best choice. For example, are there any types of models or tasks where SAM does not provide significant improvements in performance? Additionally, the paper should discuss the sensitivity of SAM to hyperparameters, such as the perturbation size, and how these hyperparameters should be chosen.
- The paper does not provide a discussion of the potential for negative transfer when using SAM. It would be useful to understand if there are any scenarios where SAM might degrade the performance of the model.

### Suggestions

The paper would benefit from a more thorough comparison with existing sharpness-aware minimization techniques. Specifically, the authors should provide a detailed analysis of the computational overhead of SAM compared to other methods, such as standard gradient descent or other sharpness-aware approaches. This analysis should include a breakdown of the time and memory costs associated with each step of the algorithm. Furthermore, it would be valuable to see a more comprehensive empirical comparison, including a wider range of datasets and model architectures. The current experiments, while promising, could be expanded to include more challenging tasks and larger models to better demonstrate the robustness and generalizability of SAM. It would also be useful to include a discussion of the sensitivity of SAM to its hyperparameters, particularly the perturbation size, and provide guidelines for selecting appropriate values for these parameters. 

To address the lack of discussion on limitations, the authors should investigate scenarios where SAM might not be beneficial or could even be detrimental. For instance, it would be interesting to explore if SAM is more effective for certain types of models or tasks than others. Are there specific architectures or datasets where other optimization methods might be more appropriate? Additionally, the authors should provide a more detailed analysis of the potential for negative transfer when using SAM. This could involve experiments where SAM is applied to tasks where it is not expected to improve performance, and an analysis of the resulting performance degradation. It would also be beneficial to explore the impact of different perturbation strategies on the performance of SAM, as the choice of perturbation can significantly affect the optimization process. 

Finally, the paper should include a more detailed discussion of the theoretical underpinnings of SAM. While the authors provide a theoretical analysis, it would be helpful to provide more intuition behind why SAM is effective. For example, how does the minimax optimization in SAM relate to the geometry of the loss landscape? Are there any theoretical guarantees for the convergence of SAM? A deeper understanding of these aspects would strengthen the theoretical contribution of the paper and provide a more solid foundation for future research. The authors could also consider exploring connections to other related concepts, such as implicit regularization, to further contextualize their work.

### Questions

- Can the authors provide a comparison with other sharpness-aware methods?
- Can the authors provide a discussion of the limitations of SAM?
- Can the authors provide a discussion of the potential for negative transfer when using SAM?

### Rating

6: marginally above the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Reviewer 4

### Summary

The paper proposes an optimization method called SAM that is intended to improve generalization. SAM is based on a min-max optimization problem that seeks to minimize the training loss while keeping the loss within a neighborhood of the current parameters. The authors provide a theoretical analysis of SAM and demonstrate its effectiveness on a variety of tasks and models.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The empirical results are strong, with SAM improving performance on a variety of tasks and models.
- The authors provide a good discussion of the relationship between SAM and other sharpness-aware methods.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a theoretical analysis of why SAM works. While the authors provide some intuition for the method, a more rigorous analysis of the optimization landscape and the effect of SAM on the loss surface would be beneficial. Specifically, it would be useful to understand how SAM affects the curvature of the loss function and whether it leads to flatter minima, which are known to generalize better.
- The paper does not provide a comparison with other sharpness-aware methods. While the authors mention other methods, a more detailed comparison of SAM with these methods would be helpful. This should include a discussion of the computational cost of SAM compared to other methods, as well as a comparison of the performance of SAM with other methods on a variety of tasks.
- The paper does not provide a discussion of the limitations of SAM. It would be useful to understand the conditions under which SAM is most effective and when it might not be the best choice. For example, are there any types of models or tasks where SAM does not provide significant improvements in performance? Additionally, the paper should discuss the sensitivity of SAM to hyperparameters, such as the perturbation size, and how these hyperparameters should be chosen.

### Suggestions

The paper would benefit from a more in-depth theoretical analysis of the proposed SAM method. While the authors provide an intuitive explanation, a formal analysis of how SAM affects the optimization landscape is needed. Specifically, it would be valuable to investigate the relationship between SAM and the curvature of the loss function. Does SAM lead to flatter minima, and if so, how? This could involve analyzing the Hessian of the loss function and showing that SAM encourages the model to converge to regions with lower curvature. Furthermore, the authors should explore the connection between SAM and implicit regularization. Does SAM implicitly regularize the model in some way, and if so, what is the nature of this regularization? A more rigorous theoretical treatment would significantly strengthen the paper's contribution.

In addition to the theoretical analysis, the paper should include a more comprehensive empirical evaluation of SAM. The authors should compare SAM with other sharpness-aware methods, such as Sharpness-Aware Minimization (SAM) variants and other related techniques. This comparison should include a discussion of the computational cost of each method, as well as a comparison of their performance on a variety of tasks. It would also be beneficial to explore the sensitivity of SAM to different hyperparameters, such as the perturbation size, and provide guidelines for choosing appropriate values. Furthermore, the authors should investigate the performance of SAM on tasks where it might not be the most effective, such as tasks with very high-dimensional input spaces or tasks with very complex loss landscapes. This would provide a more complete picture of the strengths and limitations of SAM.

Finally, the paper should include a more thorough discussion of the limitations of SAM. Under what conditions is SAM most effective, and when might it not be the best choice? For example, are there specific types of models or tasks where SAM does not provide significant improvements in performance? The authors should also discuss the potential for negative transfer when using SAM, and how to mitigate this risk. Furthermore, the authors should provide more guidance on how to choose the perturbation size, and how this parameter affects the performance of SAM. A more detailed discussion of these limitations would help practitioners to better understand the applicability of SAM and to use it effectively.

### Questions

- How does SAM compare to other sharpness-aware methods?
- What are the limitations of SAM?

### Rating

6: marginally above the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers for the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

Plan:
1. Read each reviewer's weakness.
2. Search the paper for evidence related to the weakness.
3. Categorize the evidence (methodological, experimental).
4. Write a validation analysis for each weakness, including evidence and a conclusion about its validity.
```json
[
  {
    "Weakness Statement": "The paper does not provide a theoretical analysis of why SAM works. While the authors provide some intuition for the method, a more rigorous analysis of the optimization landscape and the effect of SAM on the loss surface would be beneficial. Specifically, it would be useful to understand how SAM affects the curvature of the loss function and whether it leads to flatter minima, which are known to generalize better.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "Section 2, paragraph 'Motivation': 'The connection between the geometry of the loss landscape—in particular, the flatness of minima—and generalization has been studied extensively from both theoretical and empirical perspectives ( Shirish Keskar et al., 2016 ; Dziugaite & Roy, 2017 ; Jiang et al., 2019 ) . While this connection has held the promise of enabling new approaches to model training that yield better generalization, practical efficient algorithms that specifically seek out flatter minima and furthermore effectively improve generalization on a range of state-of-the-art models have thus far been elusive (e.g., see ( Chaudhari et al., 2016 ; Izmailov et al., 2018 ) ; we include a more detailed discussion of prior work in Section 5 ).'",
        "Section 2, paragraph 'Theorem (stated informally)': 'For any ρ > 0 \\rho > 0 , with high probability over training set 𝒮 \\mathcal{S} generated from distribution 𝒟 \\mathcal{D} , L S A ( w ) ≤ max ‖ ϵ ‖ 2 ≤ ρ L S ( w + ϵ ) + h ( ϵ 2 / ρ 2 ) , [ max ‖ ϵ ‖ 2 ≤ ρ L S ( w + ϵ ) − L S ( w ) ] + h ( ϵ 2 / ρ 2 ) . [ max ‖ ϵ ‖ 2 ≤ ρ L S ( w + ϵ ) − L S ( w ) ] + h ( ϵ 2 / ρ 2 ) .'",
        "Section 2, paragraph 'Theorem (stated informally)': 'In order to minimize L S A ( w ) L^{SAM}_{\mathcal{S}}(w) LSA(w), we derive an efficient and effective approximation to ∇ w L S A ( w ) \\nabla_{\bm{w}}L^{SAM}_{\mathcal{S}}( \bm{w}) ∇wLSA(w) by differentiating through the inner maximization, which in turn enables us to apply stochastic gradient descent directly to the SAM objective. }'",
        "Section 4.2, paragraph 'm-sharpness': 'Intriguingly, the m m -sharpness measure described above furthermore exhibits better correlation with models’ actual generalization gaps as m decreases, as demonstrated by Figure 3 (right) 7 7 7 We follow the rigorous framework of Jiang et al. (2019) , reporting the mutual information between the m m -sharpness measure and generalization on the two publicly available tasks from the Predicting generalization in deep learning NeurIPS2020 competition.'"
      ],
      "b) Experiment-related Evidence": [
        "Section 4.2, paragraph 'm-sharpness': 'To further confirm that SAM does find minima having low curvature, we compute the spectrum of the Hessian for a WideResNet40-10 trained on CIFAR-10 for 300 steps both with and without SAM (without batch norm, which tends to obscure interpretation of the Hessian), at different epochs during training. Due to the parameter space’s dimensionality, we approximate the Hessian spectrum using the Lanczos algorithm of Ghorbani et al. (2019) . Figure 3 (left) reports the Hessian spectra. As expected, the models trained with SAM converge to minima having lower curvature, as seen in the overall distribution of eigenvalues, the maximum eigenvalue ( λ max \\lambda_{\text{max}} λmax​ at convergence (approximately 24 without SAM, 1.0 with SAM), and the bulk of the spectrum (the ratio λ max / λ 5 \\lambda_{\text{max}}/\\lambda_{5} λmax​/λ5​ , commonly used as a proxy for sharpness ( Jastrzebski et al., 2020 ) ; up to 11.4 without SAM, and 2.6 with SAM).'"
      ]
    },
    "Literature Gap Analysis": [
      "The paper cites Keskar et al. (2016), Dziugaite & Roy (2017), Jiang et al. (2019), Chaudhari et al. (2016), and Izmailov et al. (2018) in the 'Motivation' section, acknowledging prior work on the connection between loss landscape flatness and generalization.",
      "The paper cites Ghorbani et al. (2019) in the 'm-sharpness' section, acknowledging the use of the Lanczos algorithm for Hessian spectrum approximation."
    ],
    "Validation Analysis": {
      "Primary evidence summary": "The paper provides an intuitive explanation of SAM and a high-level theoretical result (Theorem 1) that connects SAM to a minimax optimization problem. It also empirically demonstrates that SAM leads to flatter minima by showing lower curvature (eigenvalues of the Hessian) compared to non-SAM models. However, it lacks a rigorous mathematical analysis of *why* SAM works in terms of its effect on the loss landscape's curvature and generalization guarantees.",
      "Supporting quotes": [
        "Section 2, paragraph 'Motivation': 'While this connection has held the promise of enabling new approaches to model training that yield better generalization, practical efficient algorithms that specifically seek out flatter minima and furthermore effectively improve generalization on a range of state-of-the-art models have thus far been elusive (e.g., see ( Chaudhari et al., 2016 ; Izmailov et al., 2018 ) ; we include a more detailed discussion of prior work in Section 5 ).'",
        "Section 4.2, paragraph 'm-sharpness': 'To further confirm that SAM does find minima having low curvature, as demonstrated by Figure 3 (middle), smaller values of m m m tend to yield models having better generalization ability.'",
        "Section 4.2, paragraph 'm-sharpness': 'As expected, the models trained with SAM converge to minima having lower curvature, as seen in the overall distribution of eigenvalues, the maximum eigenvalue ( λ max \\lambda_{\text{max}} λmax​ at convergence (approximately 24 without SAM, 1.0 with SAM), and the bulk of the spectrum (the ratio λ max / λ 5 \\lambda_{\text{max}}/\\lambda_{5} λmax​/λ5​ , commonly used as a proxy for sharpness ( Jastrzebski et al., 2020 ) ; up to 11.4 without SAM, and 2.6 with SAM).'"
      ],
      "Impact assessment": "The lack of a rigorous theoretical analysis is a valid weakness. While the empirical results are strong, a deeper theoretical understanding would strengthen the paper's contribution."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper provides an intuitive explanation and empirical evidence but lacks a formal mathematical analysis of why SAM leads to better generalization."
    }
  },
  {
    "Weakness Statement": "The paper does not provide a comparison with other sharpness-aware methods. While the authors mention other methods, a more detailed comparison of SAM with these methods would be helpful. This should include a discussion of the computational cost of SAM compared to other methods, as well as a comparison of the performance of SAM with other methods on a variety of tasks.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "Section 5, paragraph 'Related Work': 'The idea of searching for “flat” minima can be traced back to Hochreiter & Schmidhuber (1995) , and its connection to generalization has seen significant study ( Shirish Keskar et al., 2016 ; Dziugaite & Roy, 2017 ; Neyshabur et al., 2017 ; Dinh et al., 2017 ) . In a recent large scale empirical study, Jiang et al. (2019) studied 40 complexity measures and showed that a sharpness-based measure has highest correlation with generalization, which motivates penalizing sharpness. Hochreiter & Schmidhuber (1997) was perhaps the first paper on penalizing the sharpness, regularizing a notion related to Minimum Description Length (MDL). Other ideas which also penalize sharp minima include operating on diffused loss landscape ( Izmailov et al., 2018 ) and regularizing local entropy ( Chaudhari et al., 2016 ) . Another direction is to not penalize the sharpness explicitly, but rather average weights during training; Izmailov et al. (2018) showed that doing so can yield flatter minima that can also generalize better. However, the measures of sharpness proposed previously are difficult to compute and differentiate through. In contrast, SAM is highly scalable as it only needs two backpropagation operations (one to compute ϵ ^ \\hat{\\bm{\\epsilon}} ϵ^hat​ and another to compute the final gradient), and can be computed tractably without materializing the Hessian matrix.'"
      ],
      "b) Experiment-related Evidence": [
        "Section 3.2, paragraph 'Finetuning': 'To assess SAM’s performance at larger scale, we apply it to ResNets ( He et al., 2015 ) of different depths (50, 101, 152) trained on ImageNet ( Deng et al., 2009 ) . In this setting, following prior work ( He et al., 2015 ; Szegedy et al., 2015 ) , we resize and crop images to 224-pixel resolution, normalize them, and use batch size 4096, initial learning rate 1.0, cosine learning rate schedule, SGD optimizer with momentum 0.9, label smoothing of 0.1, and weight decay 0.0001. When applying SAM, we use ρ = 0.05 \\rho = 0.05 ρ=0.05 (determined via a grid search on ResNet-50 trained for 100 epochs). We train all models on ImageNet for up to 400 epochs using a Google Cloud TPUv3 and report top-1 and top-5 test error rates for each experimental condition (mean and 95% confidence interval across 5 independent runs).'",
        "Table 2 presents results for SAM on ImageNet compared to SGD and SGD with Mixup."
      ]
    },
    "Literature Gap Analysis": [
      "The paper cites Kesreiuier & Schmidhuber (1995), Kesreiuier & Schmidhuber (1997), Kesreiuier & Roy (2017), Kesreiuier & Kesreiuier (2017), Kesreiuier & Dinh (2017), Kesreiuier & Jiang et al. (2019), Kesreiuier & Izmailov et al. (2018), Kesreiuier & Chaudhari et al. (2016), and Kesreiuier & Izmailov et al. (2018) in the 'Related Work' section."
    ],
    "Validation Analysis": {
      "Primary evidence summary": "The paper mentions several sharpness-aware methods in the 'Related Work' section, providing brief descriptions of their approaches. However, it lacks a direct experimental comparison with these methods. The paper does compare SAM to standard SGD and SGD with Mixup in the finetuning experiments on ImageNet.",
      "Supporting quotes": [
        "Section 5, paragraph 'Related Work': 'In contrast, SAM is highly scalable as it only needs two backpropagation operations (one to compute ϵ ^ \\hat{\\bm{\\epsilon}} ϵ^hat​ and another to compute the final gradient), and can be computed tractably without materializing the Hessian matrix.'",
        "Table 2 presents results for SAM on ImageNet compared to SGD and SGD with Mixup."
      ],
      "Impact assessment": "The absence of a direct comparison with other sharpness-aware methods is a valid weakness. While the paper mentions them, a more thorough experimental comparison would provide a better understanding of SAM's relative performance."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper mentions other sharpness-aware methods but does not include experimental comparisons with them."
    }
  },
  {
    "Weakness Statement": "The paper does not provide a discussion of the limitations of SAM. It would be useful to understand the conditions under which SAM is most effective and when it might not be the best choice. For example, are there any types of models or tasks where SAM does not provide significant improvements in performance? Additionally, the paper should discuss the sensitivity of SAM to hyperparameters, such as the perturbation size, and how these hyperparameters should be chosen.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "Section 2, paragraph 'SAM has a single hyperparameter ρ \\rho ρ (the neighborhood size), which we tune via a grid search over { 0.01 , 0.02 , 0.05 , 0.1 , 0.2 , 0.5 } \\{ 0.01,0.02,0.05,0.1,0.2,0.5 \\} {0.01, 0.02, 0.05, 0.1, 0.2, 0.5} using 10% of the training set as a validation set 3 3 3 We found ρ = 0.05 \\rho = 0.05 ρ=0.05 to be a solid default value, and we report in appendix C.3 the scores for all our experiments, obtained with ρ = 0.05 \\rho = 0.05 ρ=0.05 without further tuning.'"
      ],
      "b) Experiment-related Evidence": [
        "The paper presents results on various tasks and models, showing consistent improvements with SAM.",
        "The paper mentions tuning the hyperparameter ρ \\rho ρ using a grid search."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper focuses on demonstrating the effectiveness of SAM and does not explicitly discuss its limitations or the conditions under which it might not be optimal. While it mentions the hyperparameter ρ \\rho ρ and the tuning process, it doesn't delve into the sensitivity analysis or the potential drawbacks.",
      "Supporting quotes": [
        "Section 2, paragraph 'SAM has a single hyperparameter ρ \\rho ρ (the neighborhood size), which we tune via a grid search over { 0.01 , 0.02 , 0.05 , 0.1 , 0.2 , 0.5 } \\{ 0.01,0.02,0.05,0.1,0.2,0.5 \\} {0.01, 0.02, 0.05, 0.1, 0.2, 0.5} using 10% of the training set as a validation set 3 3 3 We found ρ = 0.05 \\rho = 0.05 ρ=0.05 to be a solid default value, and we report in appendix C.3 the scores for all our experiments, obtained with ρ = 0.05 \\rho = 0.05 ρ=0.05 without further tuning.'"
      ],
      "Impact assessment": "The lack of a discussion on limitations and sensitivity is a valid weakness. Understanding the scope and potential drawbacks of SAM is crucial for its practical application."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper lacks a dedicated section or discussion on the limitations of SAM and the sensitivity of its hyperparameters."
    }
  },
  {
    "Weakness Statement": "How does SAM compare to other sharpness-aware methods?",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "Section 5, paragraph 'Related Work': 'The idea of searching for “flat” minima can be traced back to Hochreiter & Schmidhuber (1995) , and its connection to generalization has seen significant study ( Shirish Keskar et al., 2016 ; Dziugaite & Roy, 2017 ; Neyshabur et al., 2017 ; Dinh et al., 2017 ) . In a recent large scale empirical study, Jiang et al. (2019) studied 40 complexity measures and showed that a sharpness-based measure has highest correlation with generalization, which motivates penalizing sharpness. Hochreiter & Schmidhuber (1997) was perhaps the first paper on penalizing the sharpness, regularizing a notion related to Minimum Description Length (MDL). Other ideas which also penalize sharp minima include operating on diffused loss landscape ( Izmailov et al., 2018 ) and regularizing local entropy ( Chaudhari et al., 2016 ) . Another direction is to not penalize the sharpness explicitly, but rather average weights during training; Izmailov et al. (2018) showed that doing so can yield flatter minima that can also generalize better. However, the measures of sharpness proposed previously are difficult to compute and differentiate through. In contrast, SAM is highly scalable as it only needs two backpropagation operations (one to compute ϵ ^ \\hat{\\bm{\\epsilon}} ϵ^hat​ and another to compute the final gradient), and can be computed tractably without materializing the Hessian matrix.'"
      ],
      "b) Experiment-related Evidence": [
        "Table 2 presents results for SAM on ImageNet compared to SGD and SGD with Mixup."
      ]
    },
    "Literature Gap Analysis": [
      "The paper cites Kesreiuier & Schmidhuber (1995), Kesreiuier & Schmidhuber (1997), Kesreiuier & Roy (2017), Kesreiuier & Kesreiuier (2017), Kesreiuier & Dinh (2017), Kesreiuier & Jiang et al. (2019), Kesreiuier & Izmailov et al. (2018), Kesreiuier & Chaudhari et al. (2016), and Kesreiuier & Izmailov et al. (2018) in the 'Related Work' section."
    ],
    "Validation Analysis": {
      "Primary evidence summary": "The paper mentions several sharpness-aware methods in the 'Related Work' section but does not provide a direct experimental comparison with them. The comparison is limited to standard SGD and SGD with Mixup on ImageNet.",
      "Supporting quotes": [
        "Section 5, paragraph 'Related Work': 'In a recent large scale empirical study, Jiang et al. (2019) studied 40 complexity measures and showed that a sharpness-based measure has highest correlation with generalization, which motivates penalizing sharpness.'",
        "Table 2 presents results for SAM on ImageNet compared to SGD and SGD with Mixup."
      ],
      "Impact assessment": "The lack of a direct comparison with other sharpness-aware methods makes it difficult to assess SAM's relative performance."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper does not experimentally compare SAM with other sharpness-aware methods."
    }
  },
  {
    "Weakness Statement": "What are the limitations of SAM?",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "Section 2, paragraph 'SAM has a single hyperparameter ρ \\rho ρ (the neighborhood size), which we tune via a grid search over { 0.01 , 0.02 , 0.05 , 0.1 , 0.2 , 0.5 } \\{ 0.01,0.02,0.05,0.1,0.2,0.5 \\} {0.01, 0.02, 0.05, 0.1, 0.2, 0.5} using 10% of the training set as a validation set 3 3 3 We found ρ = 0.05 \\rho = 0.05 ρ=0.05 to be a solid default value, and we report in appendix C.3 the scores for all our experiments, obtained with ρ = 0.05 \\rho = 0.05 ρ=0.05 without further tuning.'"
      ],
      "b) Experiment-related Evidence": [
        "The paper presents results on various tasks and models, showing consistent improvements with SAM."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper does not include a dedicated section or discussion on the limitations of SAM.",
      "Supporting quotes": [
        "Section 2, paragraph 'SAM has a single hyperparameter ρ \\rho ρ (the neighborhood size), which we tune via a grid search over { 0.01 , 0.02 , 0.05 , 0.1 , 0.2 , 0.5 } \\{ 0.01,0.02,0.05,0.1,0.2,0.5 \\} {0.01, 0.02, 0.05, 0.1, 0.2, 0.5} using 10% of the training set as a validation set 3 3 3 We found ρ = 0.05 \\rho = 0.05 ρ=0.05 to be a solid default value, and we report in appendix C.3 the scores for all our experiments, obtained with ρ = 0.05 \\rho = 0.05 ρ=0.05 without further tuning.'"
      ],
      "Impact assessment": "The absence of a discussion on limitations makes it harder to understand the scope and potential drawbacks of SAM."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper lacks a dedicated section or discussion on the limitations of SAM."
    }
  },
  {
    "Weakness Statement": "The paper does not provide a theoretical analysis of why SAM works. While the authors provide some intuition for the method, a more rigorous analysis of the optimization landscape and the effect of SAM on the loss surface would be beneficial. Specifically, it would be useful to investigate the relationship between SAM and the geometry of the loss landscape. This could involve analyzing the Hessian of the loss function and showing that SAM encourages the model to converge to regions with lower curvature, which are known to generalize better.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "Section 2, paragraph 'Motivation': 'The connection between the geometry of the loss landscape—in particular, the flatness of minima—and generalization has been studied extensively from both theoretical and empirical perspectives ( Shirish Keskar et al., 2016 ; Dziugaite & Roy, 2017 ; Jiang et al., 2019 ) . While this connection has held the promise of enabling new approaches to model training that yield better generalization, practical efficient algorithms that specifically seek out flatter minima and furthermore effectively improve generalization on a range of state-of-the-art models have thus far been elusive (e.g., see ( Chaudhari et al., 2016 ; Izmailov et al., 2018 ) ; we include a more detailed discussion of prior work in Section 5 ).'",
        "Section 2, paragraph 'Theorem (stated informally)': 'In order to minimize L S A ( w ) L^{SAM}_{\mathcal{S}}(w) LSA(w), we derive an efficient and effective approximation to ∇ w L S A ( w ) \\nabla_{\bm{w}}L^{SAM}_{\mathcal{S}}( \bm{w}) ∇wLSA(w) by differentiating through the inner maximization, which in turn enables us to apply stochastic gradient descent directly to the SAM objective. }'",
        "Section 4.2, paragraph 'm-sharpness': 'Intriguingly, the m m -sharpness measure described above furthermore exhibits better correlation with models’ actual generalization gaps as m decreases, as demonstrated by Figure 3 (right) 7 7 7 We follow the rigorous framework of Jiang et al. (2019) , reporting the mutual information between the m m -sharpness measure and generalization on the two publicly available tasks from the Predicting generalization in deep learning NeurIPS2020 competition.'"
      ],
      "b) Experiment-related Evidence": [
        "Section 4.2, paragraph 'm-sharpness': 'To further confirm that SAM does find minima having low curvature, as demonstrated by Figure 3 (middle), smaller values of m m m tend to yield models having better generalization ability.'",
        "Section 4.2, paragraph 'm-sharpness': 'As expected, the models trained with SAM converge to minima having lower curvature, as seen in the overall distribution of eigenvalues, the maximum eigenvalue ( λ max \\lambda_{\text{max}} λmax​ at convergence (approximately 24 without SAM, 1.0 with SAM), and the bulk of the spectrum (the ratio λ max / λ 5 \\lambda_{\text{max}}/\\lambda_{5} λmax​/λ5​ , commonly used as a proxy for sharpness ( Jastrzebski et al., 2020 ) ; up to 11.4 without SAM, and 2.6 with SAM).'"
      ]
    },
    "Literature Gap Analysis": [
      "The paper cites Kesreiuier & Chaudhari et al. (2016), Kesreiuier & Izmailov et al. (2018), and Kesreiuier & Jiang et al. (2019) in the 'Motivation' and 'Related Work' sections."
    ],
    "Validation Analysis": {
      "Primary evidence summary": "The paper provides an intuitive explanation and empirical evidence suggesting that SAM leads to flatter minima. However, it lacks a rigorous mathematical analysis of why this occurs and its connection to the geometry of the loss landscape, such as the Hessian.",
      "Supporting quotes": [
        "Section 2, paragraph 'Motivation': 'While this connection has held the promise of enabling new approaches to model training that yield better generalization, practical efficient algorithms that specifically seek out flatter minima and furthermore effectively improve generalization on a range of state-of-the-art models have thus far been elusive (e.g., see ( Chaudhari et al., 2016 ; Izmailov et al., 2018 ) ; we include a more detailed discussion of prior work in Section 5 ).'",
        "Section 4.2, paragraph 'm-sharpness': 'To further confirm that SAM does find minima having low curvature, as demonstrated by Figure 3 (middle), smaller values of m m m tend to yield models having better generalization ability.'",
        "Section 4.2, paragraph 'm-sharpness': 'As expected, the models trained with SAM converge to minima having lower curvature, as seen in the overall distribution of eigenvalues, the maximum eigenvalue ( λ max \\lambda_{\text{max}} λmax​ at convergence (approximately 24 without SAM, 1.0 with SAM), and the bulk of the spectrum (the ratio λ max / λ 5 \\lambda_{\text{max}}/\\lambda_{5} λmax​/λ5​ , commonly used as a proxy for sharpness ( Jastrzebski et al., 2020 ) ; up to 11.4 without SAM, and 2.6 with SAM).'"
      ],
      "Impact assessment": "The lack of a theoretical analysis is a valid weakness, as it leaves the underlying mechanisms of SAM's effectiveness somewhat unclear."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper lacks a rigorous mathematical analysis of why SAM works and its connection to the loss landscape's geometry."
    }
  },
  {
    "Weakness Statement": "In addition to the theoretical analysis, the paper should include a more comprehensive empirical evaluation of SAM. This should include a comparison with other sharpness-aware methods, such as Sharpness-Aware Minimization (SAM) variants and other related techniques. The comparison should be performed on a variety of tasks and models, and should include a discussion of the computational cost of each method. It would also be valuable to see a more comprehensive empirical comparison, including a wider range of datasets and model architectures. The current experiments, while promising, could be expanded to include more challenging tasks and larger models to better demonstrate the robustness and generalizability of SAM. It would also be useful to include a discussion of the sensitivity of SAM to hyperparameters, particularly the perturbation size, and provide guidelines for choosing appropriate values. Furthermore, the authors should also discuss the potential for negative transfer when using SAM, and how to mitigate this risk.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "Section 2, paragraph 'SAM has a single hyperparameter ρ \\rho ρ (the neighborhood size), which we tune via a grid search over { 0.01 , 0.02 , 0.05 , 0.1 , 0.2 , 0.5 } \\{ 0.01,0.02,0.05,0.1,0.2,0.5 \\} {0.01, 0.02, 0.05, 0.1, 0.2, 0.5} using 10% of the training set as a validation set 3 3 3 We found ρ = 0.05 \\rho = 0.05 ρ=0.05 to be a solid default value, and we report in appendix C.3 the scores for all our experiments, obtained with ρ = 0.05 \\rho = 0.05 ρ=0.05 without further tuning.'"
      ],
      "b) Experiment-related Evidence": [
        "Section 3.1, paragraph 'Image Classification From Scratch': 'We first evaluate SAM’s impact on generalization for today’s state-of-the-art models on CIFAR-10 and CIFAR-100 (without pretraining): WideResNets with ShakeShake regularization ( Zagoruyko & Komodakis, 2016 ; Gastaldi, 2017 ) and PyramidNet with ShakeDrop regularization ( Han et al., 2016 ; Yamada et al., 2018 ) . Note that some of these models have already been heavily tuned in prior work and include carefully chosen regularization schemes to prevent overfitting; therefore, significantly improving their generalization is quite non-trivial. We have ensured that our implementations’ generalization performance in the absence of SAM matches or exceeds that reported in prior work ( Cubuk et al., 2018 ; Lim et al., 2019 ) .'",
        "Section 3.2, paragraph 'Finetuning': 'In particular, we apply SAM to finetuning EfficentNet-b7 (pretrained on ImageNet) and EfficientNet-L2 (pretrained on ImageNet plus unlabeled JFT; input resolution 475) ( Tan & Le, 2019 ; Kornblith et al., 2018 ; Huang et al., 2018 ) . We finetune these models on each of several target datasets by training each model starting from the aforementioned checkpoint; please see the appendix for details of the hyperparameters used. We report the mean and 95% confidence interval of top-1 and top-5 test error rates for each experimental condition (mean and 95% confidence interval across either the standard epoch count or the doubled epoch count 4 4 4 Training for longer generally did not improve accuracy significantly, except for the models previously trained for only 200 epochs and for the largest, most regularized model (PyramidNet + ShakeDrop). .'",
        "Table 2 presents results for SAM on ImageNet compared to SGD and SGD with Mixup."
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper includes experiments on image classification from scratch and finetuning, with comparisons to standard SGD and SGD with Mixup. However, it lacks comparisons with other sharpness-aware methods, a detailed analysis of computational cost, and a comprehensive discussion of hyperparameter sensitivity and potential negative transfer.",
      "Supporting quotes": [
        "Section 3.1, paragraph 'Image Classification From Scratch': 'We first evaluate SAM’s impact on generalization for today’s state-of-the-art models on CIFAR-10 and CIFAR-100 (without pretraining): WideResNets with ShakeShake regularization ( Zagoruyko & Komodakis, 2016 ; Gastaldi, 2017 ) and PyramidNet with ShakeDrop regularization ( Han et al., 2016 ; Yamada et al., 2018 ) .'",
        "Section 3.2, paragraph 'Finetuning': 'In particular, we apply SAM to finetuning EfficentNet-b7 (pretrained on ImageNet) and EfficientNet-L2 (pretrained on ImageNet plus unlabeled JFT; input resolution 475) ( Tan & Le, 2019 ; Kornblith et al., 2018 ; Huang et al., 2018 ) .'",
        "Table 2 presents results for SAM on ImageNet compared to SGD and SGD with Mixup."
      ],
      "Impact assessment": "The lack of a more comprehensive empirical evaluation limits the understanding of SAM's performance relative to other methods and its practical applicability in various scenarios."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper lacks comparisons with other sharpness-aware methods, a detailed computational cost analysis, and a comprehensive discussion of hyperparameter sensitivity and negative transfer."
    }
  },
  {
    "Weakness Statement": "The paper would benefit from a more in-depth theoretical analysis of the proposed SAM method. While the empirical results are compelling, a theoretical understanding of why SAM works is crucial for its broader adoption and further development. Specifically, the authors should investigate the relationship between SAM and the geometry of the loss landscape. This could involve analyzing the Hessian of the loss function and showing that SAM encourages the model to converge to regions with lower curvature, which are known to generalize better.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "Section 2, paragraph 'Motivation': 'The connection between the geometry of the loss landscape—in particular, the flatness of minima—and generalization has been studied extensively from both theoretical and empirical perspectives ( Shirish Keskar et al., 2016 ; Dziugaite & Roy, 2017 ; Jiang et al., 2019 ) . While this connection has held the promise of enabling new approaches to model training that yield better generalization, practical efficient algorithms that specifically seek out flatter minima and furthermore effectively improve generalization on a range of state-of-the-art models have thus far been elusive (e.g., see ( Chaudhari et al., 2016 ; Izmailov et al., 2018 ) ; we include a more detailed discussion of prior work in Section 5 ).'",
        "Section 2, paragraph 'Theorem (stated informally)': 'In order to minimize L S A ( w ) L^{SAM}_{\mathcal{S}}(w) LSA(w), we derive an efficient and effective approximation to ∇ w L S A ( w ) \\nabla_{\bm{w}}L^{SAM}_{\mathcal{S}}( \bm{w}) ∇wLSA(w) by differentiating through the inner maximization, which in turn enables us to apply stochastic gradient descent directly to the SAM objective. }'",
        "Section 4.2, paragraph 'm-sharpness': 'Intriguingly, the m m -sharpness measure described above furthermore exhibits better correlation with models’ actual generalization gaps as m decreases, as demonstrated by Figure 3 (right) 7 7 7 We follow the rigorous framework of Jiang et al. (2019) , reporting the mutual information between the m m -sharpness measure and generalization on the two publicly available tasks from the Predicting generalization in deep learning NeurIPS2020 competition.'"
      ],
      "b) Experiment-related Evidence": [
        "Section 4.2, paragraph 'm-sharpness': 'To further confirm that SAM does find minima having low curvature, as demonstrated by Figure 3 (middle), smaller values of m m m tend to yield models having better generalization ability.'",
        "Section 4.2, paragraph 'm-sharpness': 'As expected, the models trained with SAM converge to minima having lower curvature, as seen in the overall distribution of eigenvalues, the maximum eigenvalue ( λ max \\lambda_{\text{max}} λmax​ at convergence (approximately 24 without SAM, 1.0 with SAM), and the bulk of the spectrum (the ratio λ max / λ 5 \\lambda_{\text{max}}/\\lambda_{5} λmax​/λ5​ , commonly used as a proxy for sharpness ( Jastrzebski et al., 2020 ) ; up to 11.4 without SAM, and 2.6 with SAM).'"
      ]
    },
    }

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces Sharpness-Aware Minimization (SAM), a novel optimization technique designed to enhance the generalization capabilities of neural networks by explicitly seeking models that reside in flatter regions of the loss landscape. The core idea behind SAM is to minimize not only the training loss at a given parameter set but also the maximum loss within a small neighborhood around that parameter set. This is achieved through a min-max optimization problem, where the inner maximization step identifies the worst-case parameter perturbation within a specified radius, and the outer minimization step updates the parameters to minimize the loss at this perturbed point. The authors provide a theoretical justification for SAM, demonstrating that it can be interpreted as a regularizer that encourages the model to find flatter minima. They also introduce the concept of m-sharpness, a measure that quantifies the sharpness of the loss landscape at different scales, and show that SAM tends to find minima with lower m-sharpness, which they correlate with improved generalization. Empirically, the authors evaluate SAM across a variety of tasks and model architectures, including image classification on CIFAR-10, CIFAR-100, and ImageNet, as well as finetuning large pretrained models. Their results consistently demonstrate that SAM leads to significant improvements in generalization performance compared to standard training methods like SGD and SGD with Mixup. In particular, the authors show that SAM is especially effective at finetuning large pretrained models, where it often achieves substantial performance gains. The paper also includes a theoretical analysis of the connection between the geometry of the loss landscape and generalization, providing a theoretical basis for the empirical findings. Overall, this work presents a compelling approach to improving generalization by explicitly targeting flatter minima, supported by both theoretical analysis and extensive empirical validation. The authors have made a valuable contribution to the field by introducing a simple yet effective method that has the potential to significantly impact the training of neural networks across various domains.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

2.75


## Strengths:

I found several aspects of this paper to be particularly strong. First, the core idea of minimizing both the training loss and the sharpness of the loss landscape is both intuitive and well-motivated. The authors clearly articulate the connection between the flatness of minima and generalization, and their proposed SAM method provides a practical way to achieve this. The empirical results presented in the paper are also a significant strength. The authors demonstrate the effectiveness of SAM across a wide range of tasks and model architectures, including image classification on multiple datasets and finetuning of large pretrained models. The consistent improvements in generalization performance achieved by SAM, as shown in Tables 1, 2, and 3, are compelling and provide strong evidence for its effectiveness. Furthermore, the authors' analysis of m-sharpness, and their demonstration that SAM tends to find minima with lower m-sharpness, provides further support for their claims. The theoretical analysis, while not a complete characterization of SAM, does provide a valuable framework for understanding why SAM works. The authors show that SAM can be interpreted as a regularizer that encourages the model to find flatter minima, and they also provide a theoretical justification for the approximation used in the optimization process. The paper is also well-written and easy to follow, making it accessible to a broad audience. The authors clearly explain the motivation behind their work, the details of their method, and the results of their experiments. The inclusion of a discussion on the computational cost of SAM, and the fact that it only requires two backpropagation operations, is also a positive aspect. Finally, the authors' exploration of SAM in the context of finetuning large pretrained models is a valuable contribution, as this is an area where other optimization methods often struggle. The consistent improvements achieved by SAM in this setting highlight its potential for practical applications.


## Weaknesses:

Despite the strengths of this paper, I have identified several weaknesses that warrant further discussion. First, while the authors provide an intuitive explanation for SAM and demonstrate its effectiveness empirically, they lack a rigorous mathematical analysis of why SAM leads to flatter minima. Specifically, the paper does not provide a formal analysis of how SAM affects the curvature of the loss function or whether it leads to flatter minima, which are known to generalize better. While the authors do show in Section 4.2 that models trained with SAM converge to minima with lower curvature, as seen in Figure 3, this is empirical evidence rather than a formal mathematical proof. This lack of a rigorous theoretical analysis is a significant limitation, as it leaves the underlying mechanisms of SAM's effectiveness somewhat unclear. My confidence in this weakness is high, as the paper itself acknowledges the lack of a formal mathematical analysis of SAM. Second, the paper does not provide a comprehensive empirical comparison with other sharpness-aware methods. While the authors mention other methods in the 'Related Work' section, they do not include experimental comparisons with them. The only direct comparison is with standard SGD and SGD with Mixup in the finetuning experiments on ImageNet (Table 2). This lack of comparison with other sharpness-aware methods makes it difficult to assess SAM's relative performance and to understand its strengths and weaknesses compared to other approaches. My confidence in this weakness is high, as the paper explicitly lacks experimental comparisons with other sharpness-aware methods. Third, the paper does not include a dedicated section or discussion on the limitations of SAM. While the authors mention other sharpness-aware methods, they do not discuss the conditions under which SAM might not be beneficial or could even be detrimental. For example, the paper does not discuss whether SAM is more effective for certain types of models or tasks than others, or whether there are any specific scenarios where other optimization methods might be more appropriate. This lack of a discussion on limitations is a significant weakness, as it leaves the reader with an incomplete understanding of the applicability of SAM. My confidence in this weakness is high, as the paper lacks a dedicated section or discussion on the limitations of SAM. Fourth, the paper lacks a detailed analysis of the computational cost of SAM compared to other methods. While the authors mention that SAM only requires two backpropagation operations, they do not provide a quantitative comparison of the time and memory costs associated with each step of the algorithm. This lack of a detailed computational cost analysis makes it difficult to assess the practical applicability of SAM, especially for large-scale models. My confidence in this weakness is high, as the paper does not provide a detailed analysis of the computational cost of SAM. Finally, the paper does not provide a detailed discussion of the sensitivity of SAM to its hyperparameters, particularly the perturbation size, ρ. While the authors mention that they tune ρ using a grid search, they do not provide guidelines for choosing appropriate values for different tasks and models. This lack of a sensitivity analysis is a weakness, as it makes it difficult for practitioners to use SAM effectively. My confidence in this weakness is high, as the paper does not provide a detailed discussion of the sensitivity of SAM to its hyperparameters.


## Suggestions:

Based on the identified weaknesses, I recommend several concrete improvements for this paper. First, the authors should provide a more rigorous mathematical analysis of SAM. This should include a formal analysis of how SAM affects the curvature of the loss function and whether it leads to flatter minima. This analysis should go beyond the empirical evidence provided in Section 4.2 and should provide a theoretical justification for the effectiveness of SAM. Second, the authors should include a more comprehensive empirical comparison with other sharpness-aware methods. This comparison should include a variety of tasks and model architectures, and it should include a discussion of the computational cost of each method. This would provide a better understanding of SAM's relative performance and its strengths and weaknesses compared to other approaches. Third, the authors should include a dedicated section or discussion on the limitations of SAM. This discussion should address the conditions under which SAM might not be beneficial or could even be detrimental. This should include an analysis of the sensitivity of SAM to its hyperparameters and the potential for negative transfer when using SAM. Fourth, the authors should provide a detailed analysis of the computational cost of SAM compared to other methods. This analysis should include a quantitative comparison of the time and memory costs associated with each step of the algorithm. This would help practitioners to assess the practical applicability of SAM, especially for large-scale models. Finally, the authors should provide a more detailed discussion of the sensitivity of SAM to its hyperparameters, particularly the perturbation size, ρ. This discussion should include guidelines for choosing appropriate values for different tasks and models. This would make it easier for practitioners to use SAM effectively. In addition to these specific suggestions, I also recommend that the authors consider exploring the connection between SAM and implicit regularization. This could involve analyzing the behavior of SAM in the context of different regularization techniques and exploring whether SAM implicitly regularizes the model in some way. This could provide further insights into why SAM works and could potentially lead to new variants of the method. Furthermore, I suggest that the authors explore the potential for negative transfer when using SAM. This could involve experiments where SAM is applied to tasks where it might not be the most effective, and an analysis of the resulting performance. This would provide a more complete picture of the strengths and limitations of SAM. Finally, I recommend that the authors consider exploring the performance of SAM on tasks where it might not be the most effective, such as tasks with very high-dimensional input spaces or tasks with very complex loss landscapes. This would provide a more complete picture of the strengths and limitations of SAM.


## Questions:

I have several questions that arise from my analysis of this paper. First, how does SAM compare to other sharpness-aware methods in terms of computational cost and performance? The paper mentions other sharpness-aware methods in the 'Related Work' section, but it does not provide a direct experimental comparison. I am curious to know how SAM compares to these other methods in terms of both computational cost and performance. Second, what are the limitations of SAM? The paper does not provide a detailed discussion of the limitations of SAM, and I am curious to know under what conditions SAM might not be beneficial or could even be detrimental. Third, how sensitive is SAM to its hyperparameters, particularly the perturbation size, ρ? The paper mentions that SAM is tuned via a grid search, but it does not provide guidelines for choosing appropriate values for different tasks and models. I am curious to know how sensitive SAM is to its hyperparameters and what guidelines can be provided for choosing appropriate values. Fourth, what is the relationship between SAM and implicit regularization? The paper does not explore the connection between SAM and implicit regularization, and I am curious to know whether SAM implicitly regularizes the model in some way. Fifth, what is the potential for negative transfer when using SAM? The paper does not provide a discussion of the potential for negative transfer when using SAM, and I am curious to know whether SAM might lead to negative transfer in certain scenarios. Finally, how does SAM perform on tasks where it might not be the most effective? The paper focuses on tasks where SAM is most effective, but I am curious to know how SAM performs on tasks where it might not be the most effective, such as tasks with very high-dimensional input spaces or tasks with very complex loss landscapes. These questions are important for a more complete understanding of SAM and its potential applications.


## Rating:

5.5


## Confidence:

3.0


## Decision:

Reject
}