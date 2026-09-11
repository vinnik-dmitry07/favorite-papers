I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper provides a theoretical analysis of the JEPA framework for world models. The authors prove that JEPA can only learn a linearly identifiable representation when the latent variables are Gaussian. They also provide a converse result, showing that non-Gaussian latents break linear identifiability. The paper includes empirical validation of the theory through experiments on 2D mixings, 1024-dimensional latents, and pixel-based robotic control.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper provides a rigorous theoretical analysis of the JEPA framework, addressing an important gap in the literature.
2. The authors clearly articulate their assumptions and provide detailed proofs for their theorems.
3. The empirical validation includes experiments across different latent dimensions and data regimes, strengthening the practical relevance of the theory.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's reliance on Gaussian latents may limit its applicability to real-world scenarios where non-Gaussian distributions are common. Specifically, the assumption of Gaussianity is quite strong and may not hold in many complex systems, potentially restricting the practical use of the proposed framework. The analysis does not explore the robustness of the results to deviations from this assumption, which is a critical consideration for real-world applications.
2. The empirical results, while supportive, are limited to relatively simple environments. The 2D mixings and 1024-dimensional latents, while useful for initial validation, do not fully capture the complexity of real-world robotic control tasks. The pixel-based robotic control experiments, while more complex, still may not fully demonstrate the scalability and robustness of the method in highly dynamic and high-dimensional environments. The lack of experiments in more challenging scenarios limits the generalizability of the empirical findings.
3. The paper could benefit from a more detailed discussion of the limitations of the JEPA framework and potential avenues for future research. The analysis does not delve into the computational costs associated with the JEPA framework, which could be a significant factor in practical applications. Furthermore, the paper does not discuss the sensitivity of the results to hyperparameter choices, which could impact the reproducibility and reliability of the empirical findings.

### Suggestions

The paper would benefit from a more thorough investigation into the sensitivity of the JEPA framework to deviations from the Gaussian latent variable assumption. While the theoretical analysis provides a strong foundation, it is crucial to understand how the method performs when the latent variables are not perfectly Gaussian. This could involve experiments with different types of non-Gaussian distributions, such as heavy-tailed or multimodal distributions, to assess the robustness of the linear identifiability results. Furthermore, the authors should explore potential modifications to the JEPA framework that could mitigate the impact of non-Gaussian latents, such as incorporating non-linear transformations or using alternative loss functions. This would significantly enhance the practical applicability of the method in real-world scenarios where the Gaussian assumption is unlikely to hold.

To strengthen the empirical validation, the authors should include experiments in more complex and dynamic environments. This could involve tasks with higher-dimensional state spaces, more complex dynamics, and more diverse types of observations. For example, experiments on simulated robotic manipulation tasks or navigation tasks in complex environments would provide a more rigorous test of the method's scalability and robustness. Additionally, the authors should consider evaluating the performance of the JEPA framework in scenarios where the assumptions of the theoretical analysis are not fully met, such as in the presence of noise or outliers. This would provide a more comprehensive understanding of the method's limitations and its applicability to real-world problems. The inclusion of such experiments would significantly enhance the practical relevance of the paper.

Finally, the paper should include a more detailed discussion of the computational costs associated with the JEPA framework and the sensitivity of the results to hyperparameter choices. This could involve analyzing the time and memory requirements of the method as the dimensionality of the latent space increases, as well as exploring the impact of different hyperparameter settings on the performance of the method. The authors should also discuss potential strategies for mitigating the computational costs, such as using more efficient optimization algorithms or employing techniques for dimensionality reduction. Furthermore, the paper should provide clear guidelines for selecting appropriate hyperparameter values to ensure the reproducibility and reliability of the empirical findings. This would make the paper more useful for practitioners who are interested in applying the JEPA framework to real-world problems.

### Questions

1. How sensitive is the JEPA framework to deviations from the Gaussian latent variable assumption? Could you provide additional experiments or theoretical insights into the robustness of the linear identifiability results when the latent variables are not perfectly Gaussian?
2. Could you elaborate on the computational costs associated with the JEPA framework, particularly as the dimensionality of the latent space increases? How does the computational cost scale with the number of samples and the dimensionality of the latent space?
3. The paper mentions that the choice of the loss function (e.g., SIGReg, VICReg, InfoNCE) affects identifiability. Could you provide more guidance on how to select the appropriate loss function for a given task? Are there specific characteristics of the data or the environment that should be considered when choosing a loss function?

### Rating

5

### Confidence

3

**********

## Reviewer 2

### Summary

This paper provides a theoretical analysis of the JEPA framework for world models. The authors prove that JEPA can only learn a linearly identifiable representation when the latent variables are Gaussian. They also provide a converse result, showing that non-Gaussian latents break linear identifiability. The paper includes empirical validation of the theory through experiments on 2D mixings, 1024-dimensional latents, and pixel-based robotic control.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

The paper provides a rigorous theoretical analysis of the JEPA framework, addressing an important gap in the literature. The authors clearly articulate their assumptions and provide detailed proofs for their theorems. The empirical validation includes experiments across different latent dimensions and data regimes, strengthening the practical relevance of the theory.

### Weaknesses

#### Some Related Works


#### comment

The paper's reliance on Gaussian latents may limit its applicability to real-world scenarios where non-Gaussian distributions are common. Specifically, the assumption of Gaussianity is quite strong and may not hold in many complex systems, potentially restricting the practical use of the proposed framework. The analysis does not explore the robustness of the results to deviations from this assumption, which is a critical consideration for real-world applications. For instance, the paper does not discuss how the identifiability results would be affected by non-Gaussian latent variables with heavier tails or multiple modes, which are common in many real-world scenarios. Furthermore, the paper does not provide any guidance on how to detect or mitigate the impact of such deviations, which is crucial for practical applications.

### Suggestions

The authors should investigate the robustness of their theoretical results to deviations from the Gaussian assumption. This could involve analyzing the identifiability conditions under different types of non-Gaussian distributions, such as heavy-tailed distributions or mixtures of Gaussians. It would be beneficial to explore how the performance of the JEPA framework degrades as the latent variables deviate from a Gaussian distribution. For example, the authors could conduct experiments using synthetic datasets with non-Gaussian latent variables and analyze the impact on the linear identifiability of the learned representations. This would provide a more comprehensive understanding of the limitations of the proposed framework and its applicability to real-world scenarios. Furthermore, the authors should consider developing methods to detect and mitigate the impact of non-Gaussian latent variables, which could involve using robust statistical techniques or incorporating prior knowledge about the data distribution.

In addition to the theoretical analysis, the authors should also provide more practical guidance on how to apply the JEPA framework in real-world scenarios where the Gaussian assumption may not hold. This could involve providing recommendations on how to choose the appropriate loss function for different types of data and latent variables. For example, the authors could explore the use of alternative loss functions that are more robust to non-Gaussian distributions. Furthermore, the authors should provide practical guidelines on how to select the hyperparameters of the JEPA framework, such as the learning rate and the regularization parameters, to ensure optimal performance in the presence of non-Gaussian latent variables. This would make the framework more accessible and useful for practitioners who are interested in applying it to real-world problems. The authors should also consider providing open-source code and tools to facilitate the use of the JEPA framework.

Finally, the authors should discuss the limitations of their theoretical analysis and the potential impact of these limitations on the practical application of the JEPA framework. This could involve acknowledging that the theoretical results may not hold in all real-world scenarios and that the performance of the framework may degrade when the Gaussian assumption is violated. The authors should also discuss the potential for future research to address these limitations and to develop more robust and practical methods for learning world models. This would help to ensure that the JEPA framework is used appropriately and that its limitations are clearly understood by the research community.

### Questions

How sensitive is the JEPA framework to deviations from the Gaussian latent variable assumption? Could you provide additional experiments or theoretical insights into the robustness of the linear identifiability results when the latent variables are not perfectly Gaussian?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

This paper provides a theoretical analysis of the JEPA framework for world models. The authors prove that JEPA can only learn a linearly identifiable representation when the latent variables are Gaussian. They also provide a converse result, showing that non-Gaussian latents break linear identifiability. The paper includes empirical validation of the theory through experiments on 2D mixings, 1024-dimensional latents, and pixel-based robotic control.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

The paper provides a rigorous theoretical analysis of the JEPA framework, addressing an important gap in the literature. The authors clearly articulate their assumptions and provide detailed proofs for their theorems. The empirical validation includes experiments across different latent dimensions and data regimes, strengthening the practical relevance of the theory.

### Weaknesses

#### Some Related Works


#### comment

The paper's reliance on Gaussian latents may limit its applicability to real-world scenarios where non-Gaussian distributions are common. Specifically, the assumption of Gaussianity is quite strong and may not hold in many complex systems, potentially restricting the practical use of the proposed framework. The analysis does not explore the robustness of the results to deviations from this assumption, which is a critical consideration for real-world applications. For instance, the paper does not discuss how the identifiability results would be affected by non-Gaussian latent variables with heavier tails or multiple modes, which are common in many real-world scenarios. Furthermore, the paper does not provide any guidance on how to detect or mitigate the impact of such deviations, which is crucial for practical applications.

### Suggestions

The authors should investigate the robustness of their theoretical results to deviations from the Gaussian assumption. This could involve analyzing the identifiability conditions under different types of non-Gaussian distributions, such as heavy-tailed distributions or mixtures of Gaussians. It would be beneficial to explore how the performance of the JEPA framework degrades as the latent variables deviate from a Gaussian distribution. For example, the authors could conduct experiments using synthetic datasets with non-Gaussian latent variables and analyze the impact on the linear identifiability of the learned representations. This would provide a more comprehensive understanding of the limitations of the proposed framework and its applicability to real-world scenarios. Furthermore, the authors should consider developing methods to detect and mitigate the impact of non-Gaussian latent variables, which could involve using robust statistical techniques or incorporating prior knowledge about the data distribution.

In addition to the theoretical analysis, the authors should also provide more practical guidance on how to apply the JEPA framework in real-world scenarios where the Gaussian assumption may not hold. This could involve providing recommendations on how to choose the appropriate loss function for different types of data and latent variables. For example, the authors could explore the use of alternative loss functions that are more robust to non-Gaussian distributions. Furthermore, the authors should provide practical guidelines on how to select the hyperparameters of the JEPA framework, such as the learning rate and the regularization parameters, to ensure optimal performance in the presence of non-Gaussian latent variables. This would make the framework more accessible and useful for practitioners who are interested in applying it to real-world problems. The authors should also consider providing open-source code and tools to facilitate the use of the JEPA framework.

Finally, the authors should discuss the limitations of their theoretical analysis and the potential impact of these limitations on the practical application of the JEPA framework. This could involve acknowledging that the theoretical results may not hold in all real-world scenarios and that the performance of the framework may degrade when the Gaussian assumption is violated. The authors should also discuss the potential for future research to address these limitations and to develop more robust and practical methods for learning world models. This would help to ensure that the JEPA framework is used appropriately and that its limitations are clearly understood by the research community.

### Questions

How sensitive is the JEPA framework to deviations from the Gaussian latent variable assumption? Could you provide additional experiments or theoretical insights into the robustness of the linear identifiability results when the latent variables are not perfectly Gaussian?

### Rating

6

### Confidence

2

**********

## Reviewer 4

### Summary

This paper provides a theoretical analysis of the JEPA framework for world models. The authors prove that JEPA can only learn a linearly identifiable representation when the latent variables are Gaussian. They also provide a converse result, showing that non-Gaussian latents break linear identifiability. The paper includes empirical validation of the theory through experiments on 2D mixings, 1024-dimensional latents, and pixel-based robotic control.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

The paper provides a rigorous theoretical analysis of the JEPA framework, addressing an important gap in the literature. The authors clearly articulate their assumptions and provide detailed proofs for their theorems. The empirical validation includes experiments across different latent dimensions and data regimes, strengthening the practical relevance of the theory.

### Weaknesses

#### Some Related Works


#### comment

The paper's reliance on Gaussian latents may limit its applicability to real-world scenarios where non-Gaussian distributions are common. Specifically, the assumption of Gaussianity is quite strong and may not hold in many complex systems, potentially restricting the practical use of the proposed framework. The analysis does not explore the robustness of the results to deviations from this assumption, which is a critical consideration for real-world applications. For instance, the paper does not discuss how the identifiability results would be affected by non-Gaussian latent variables with heavier tails or multiple modes, which are common in many real-world scenarios. Furthermore, the paper does not provide any guidance on how to detect or mitigate the impact of such deviations, which is crucial for practical applications.

### Suggestions

The authors should investigate the robustness of their theoretical results to deviations from the Gaussian assumption. This could involve analyzing the identifiability conditions under different types of non-Gaussian distributions, such as heavy-tailed distributions or mixtures of Gaussians. It would be beneficial to explore how the performance of the JEPA framework degrades as the latent variables deviate from a Gaussian distribution. For example, the authors could conduct experiments using synthetic datasets with non-Gaussian latent variables and analyze the impact on the linear identifiability of the learned representations. This would provide a more comprehensive understanding of the limitations of the proposed framework and its applicability to real-world scenarios. Furthermore, the authors should consider developing methods to detect and mitigate the impact of non-Gaussian latent variables, which could involve using robust statistical techniques or incorporating prior knowledge about the data distribution.

In addition to the theoretical analysis, the authors should also provide more practical guidance on how to apply the JEPA framework in real-world scenarios where the Gaussian assumption may not hold. This could involve providing recommendations on how to choose the appropriate loss function for different types of data and latent variables. For example, the authors could explore the use of alternative loss functions that are more robust to non-Gaussian distributions. Furthermore, the authors should provide practical guidelines on how to select the hyperparameters of the JEPA framework, such as the learning rate and the regularization parameters, to ensure optimal performance in the presence of non-Gaussian latent variables. This would make the framework more accessible and useful for practitioners who are interested in applying it to real-world problems. The authors should also consider providing open-source code and tools to facilitate the use of the JEPA framework.

Finally, the authors should discuss the limitations of their theoretical analysis and the potential impact of these limitations on the practical application of the JEPA framework. This could involve acknowledging that the theoretical results may not hold in all real-world scenarios and that the performance of the framework may degrade when the Gaussian assumption is violated. The authors should also discuss the potential for future research to address these limitations and to develop more robust and practical methods for learning world models. This would help to ensure that the JEPA framework is used appropriately and that its limitations are clearly understood by the research community.

### Questions

How sensitive is the JEPA framework to deviations from the Gaussian latent variable assumption? Could you provide additional experiments or theoretical insights into the robustness of the linear identifiability results when the latent variables are not perfectly Gaussian?

### Rating

8

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The reviewer has identified a key weakness: the reliance on Gaussian latents and the lack of exploration into the framework's robustness to deviations from this assumption. I need to examine the paper to see if this is a valid concern and if the reviewer's suggestions are reasonable.

**Plan:**
1. Locate the section where the Gaussian assumption is explicitly stated and justified.
2. Analyze the theoretical proofs to see if they rely heavily on this assumption.
3. Check the experimental setup to see if any experiments were conducted with non-Gaussian latents.
4. Evaluate if the discussion section acknowledges the limitations imposed by the Gaussian assumption.
5. Assess if the reviewer's suggestions are feasible given the paper's content.
**Reviewer Weakness Statement:**

"The paper's reliance on Gaussian latents may limit its applicability to real-world scenarios where non-Gaussian distributions are common. Specifically, the assumption of Gaussianity is quite strong and may not hold in many complex systems, potentially restricting the practical use of the proposed framework. The analysis does not explore the robustness of the results to deviations from this assumption, which is a critical consideration for real-world applications. For instance, the paper does not discuss how the identifiability results would be affected by non-Gaussian latent variables with heavier tails or multiple modes, which are common in many real-world scenarios. Furthermore, the paper does not provide any guidance on how to detect or mitigate the impact of such deviations, which is crucial for practical applications."

**Evidence Collection:**

a) Method-related Evidence:
- **Explicit Assumption Statement:**  The paper explicitly states the Gaussian assumption in the "Main Idea" section: "We consider a broad class of worlds with Gaussian latent variables and positive pairs from a stationary process with independent, additive-noise transitions."  This is further detailed in the "World Models" component of the "Method" section: "The world model is characterized by three assumptions: (1) Independent latent variables are the evaluations of a stochastic process, (2) Stationary process with independent, additive-noise transitions, and (3) Gaussian latent variables."
- **Justification for Gaussianity:** The motivation section mentions: "The need for a theoretical foundation for self-supervised learning (SSL) in world models is evident, as current methods often rely on implicit assumptions that may not hold in practice." While this motivates the need for theory, it doesn't explicitly justify the Gaussian assumption. However, the "Method" section elaborates on the choice: "The choice of Gaussian distributions is motivated by the central limit theorem, which suggests that the sum of many small, independent perturbations tends toward a Gaussian distribution. This choice simplifies the analysis and provides a tractable framework for studying identifiability."  The connection to the central limit theorem is mentioned in the "Gaussian World: Hermite Polynomials" component of the "Method" section: "For Gaussian worlds, the eigenfunctions are the Hermite polynomials, which are the natural orthogonal basis for functions of Gaussian variables."

b) Experiment-related Evidence:
- **Latent Space Setup:** The "Latent Space Experiments" section describes the setup: "We sample latents z ∼ N (0, I2 ) and apply four nonlinear mixing functions..." This confirms that the experiments primarily use Gaussian latent variables.
- **Gaussian Latent Variable Assumption in Experiments:** The "Latent-Distribution Sweep" experiment explicitly tests the "Gaussian latent variable assumption" by comparing performance on OU processes (which imply Gaussianity) with real trajectories. The setup states: "We test the Gaussian latent variable assumption by comparing the performance of the JEPA framework on OU processes with that on real robot trajectories."  The results show a significant performance difference, supporting the reviewer's point about the importance of the Gaussian assumption.

3. Literature Gap Analysis:
- The reviewer suggests exploring the robustness to deviations from Gaussianity. While the paper cites relevant works on SSL and JEPA, it doesn't explicitly discuss or cite literature on the robustness of similar frameworks to non-Gaussian assumptions.

4. Validation Analysis:
- **Primary evidence summary:** The paper explicitly assumes Gaussian latent variables and provides a justification based on the central limit theorem. The experimental design includes a test specifically addressing the Gaussian assumption. The reviewer correctly points out the lack of exploration into the framework's behavior with non-Gaussian latents.
- **Supporting quotes:**
    - "The world model is characterized by three assumptions: (1) Independent latent variables are the evaluations of a stochastic process, (2) Stationary process with independent, additive-noise transitions, and (3) Gaussian latent variables." (Method -> World Models)
    - "For Gaussian worlds, the eigenfunctions are the Hermite polynomials, which are the natural orthogonal basis for functions of Gaussian variables." (Method -> Gaussian World: Hermite Polynomials)
    - "We test the Gaussian latent variable assumption by comparing the performance of the JEPA framework on OU processes with that on real robot trajectories." (Experiments -> Latent-Distribution Sweep -> Setup)
- **Impact assessment:** The reviewer's criticism is valid. The paper's strong reliance on the Gaussian assumption, without exploring its limitations or providing guidance on handling non-Gaussian cases, is a significant gap. This limits the practical applicability of the theoretical findings.

5. Conclusion:
- Validity status: **Valid**
- Confidence level: **High**
- Key supporting evidence: Explicit statement of the Gaussian assumption in the method, experimental validation of this assumption, and the absence of discussion or experiments with non-Gaussian latents.

**Reviewer Suggestions Analysis:**

The reviewer's suggestions are directly related to the identified weakness. They propose investigating the robustness to deviations from the Gaussian assumption, providing more practical guidance, and discussing the limitations.

- **"Investigate the robustness of their theoretical results to deviations from the Gaussian latent variable assumption. This could involve analyzing the identifiability conditions under different types of non-Gaussian distributions, such as heavy-tailed distributions or mixtures of Gaussians. It would be beneficial to explore how the performance of the JEPA framework degrades as the latent variables deviate from a Gaussian distribution. For example, the authors could conduct experiments using synthetic datasets with non-Gaussian latent variables and analyze the impact on the linear identifiability of the learned representations. This would provide a more comprehensive understanding of the limitations of the proposed framework and its applicability to real-world scenarios. Furthermore, the authors should consider developing methods to detect and mitigate the impact of such deviations, which could involve using robust statistical techniques or incorporating prior knowledge about the data distribution."** - This directly addresses the identified weakness and is a valid suggestion for future work.
- **"Provide more practical guidance on how to apply the JEPA framework in real-world scenarios where the Gaussian assumption may not hold. This could involve providing recommendations on how to choose the appropriate loss function for different types of data and latent variables. For example, the authors could explore the use of alternative loss functions that are more robust to non-Gaussian distributions. Furthermore, the authors should provide practical guidelines on how to select the hyperparameters of the JEPA framework, such as the learning rate and the regularization parameters, to ensure optimal performance in the presence of non-Gaussian latent variables. This would make the framework more accessible and useful for practitioners who are interested in applying it to real-world problems. The authors should also consider providing open-source code and tools to facilitate the use of the JEPA framework."** - This is a valid suggestion for improving the practical applicability of the framework.
- **"Finally, the authors should discuss the limitations of their theoretical analysis and the potential impact of these limitations on the practical application of the JEPA framework. This could involve acknowledging that the theoretical results may not hold in all real-world scenarios and that the performance of the framework may degrade when the Gaussian assumption is violated. The authors should also discuss the potential for future research to address these limitations and to develop more robust and practical methods for learning world models. This would help to ensure that the JEPA framework is used appropriately and that its limitations are clearly understood by the research community."** - This is a crucial point for responsible research and a valid suggestion for the discussion section.

**Conclusion on Reviewer Weaknesses:**

All aspects of the reviewer's weakness statement are validly supported by the paper's content. The paper's strong reliance on the Gaussian assumption without exploring its limitations is a significant gap.

**Final Conclusion:**

The reviewer's identification of the paper's reliance on the Gaussian assumption and the lack of exploration into its robustness is a valid and significant weakness. The suggestions provided by the reviewer are pertinent and would strengthen the paper's practical relevance and impact.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper delves into the theoretical underpinnings of the JEPA framework for world models, a critical area given the increasing importance of self-supervised learning (SSL) in robotics and other sequential decision-making tasks. The authors' core contribution lies in establishing a rigorous mathematical framework to analyze the identifiability of latent representations learned by JEPA. Specifically, they demonstrate that JEPA can only learn a linearly identifiable representation when the latent variables are Gaussian. This is a significant result as it provides a fundamental limit on the capabilities of the JEPA framework. The authors further show that when the latent variables deviate from Gaussianity, linear identifiability breaks down, highlighting the importance of the Gaussian assumption. The methodology employed is primarily theoretical, involving detailed mathematical proofs and analysis of the JEPA framework under various assumptions about the latent space. The authors analyze the framework's behavior under different conditions, including linear mixing of latents, 1024-dimensional latents, and pixel-based robotic control. These experiments are designed to validate the theoretical findings and demonstrate the practical relevance of the analysis. The main empirical findings confirm the theoretical predictions, showing that JEPA can only achieve linear identifiability when the latent variables are Gaussian. The experiments also demonstrate that when the latent variables are non-Gaussian, the framework fails to achieve linear identifiability. The overall significance of this work lies in providing a theoretical foundation for understanding the limitations of JEPA and the importance of the Gaussian assumption in achieving linear identifiability. This work is a valuable contribution to the field, offering a deeper understanding of the theoretical underpinnings of SSL in world models and providing a basis for future research in this area. The authors' analysis is rigorous and well-supported by their experiments, making a strong case for the importance of their findings. The paper is well-written and clearly presents the theoretical framework and experimental results, making it accessible to researchers in the field.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

2.75


## Strengths:

This paper presents several notable strengths that contribute to its overall significance. First and foremost, the authors provide a rigorous theoretical analysis of the JEPA framework, addressing a critical gap in the literature. This is a substantial contribution as it moves beyond empirical observations to establish a solid mathematical foundation for understanding the behavior of JEPA. The authors' ability to formally prove that JEPA can only learn a linearly identifiable representation when the latent variables are Gaussian is a key achievement. This result is not only theoretically interesting but also has practical implications for the design and application of JEPA-based world models. The paper's clarity is another significant strength. The authors clearly articulate their assumptions and provide detailed proofs for their theorems, making the theoretical analysis accessible to a broad audience. The use of Hermite polynomials to characterize the linear identifiability of Gaussian latent variables is a particularly insightful approach. The experimental validation is also a strong point of the paper. The authors conduct experiments across different latent dimensions and data regimes, strengthening the practical relevance of their theory. The experiments on linear mixing of latents, 1024-dimensional latents, and pixel-based robotic control provide compelling evidence for the theoretical findings. The authors also demonstrate a good understanding of the limitations of their analysis and acknowledge the importance of the Gaussian assumption. The paper's focus on a fundamental problem in SSL, namely the identifiability of latent representations, is also a strength. This is a crucial area of research, and the authors' work provides a valuable contribution to this field. The paper's overall organization is logical and well-structured, making it easy for the reader to follow the authors' arguments and understand their findings. The authors' ability to connect their theoretical results with empirical evidence is also a notable strength, demonstrating the practical relevance of their analysis. The paper's focus on a fundamental problem in SSL, namely the identifiability of latent representations, is also a strength. This is a crucial area of research, and the authors' work provides a valuable contribution to this field.


## Weaknesses:

While this paper makes significant contributions, there is a notable weakness that I have verified through my analysis. The paper's reliance on the assumption of Gaussian latent variables is a significant limitation. The authors explicitly state in the 'Main Idea' section that they consider a broad class of worlds with Gaussian latent variables and positive pairs from a stationary process with independent, additive-noise transitions. This assumption is further elaborated in the 'Method' section, where the authors state that the world model is characterized by three assumptions, one of which is that the latent variables are Gaussian. The authors justify this assumption by citing the central limit theorem, suggesting that the sum of many small, independent perturbations tends toward a Gaussian distribution. However, this justification is not universally applicable, and real-world latent variables often exhibit non-Gaussian distributions. The paper does not explore the robustness of the theoretical results to deviations from this assumption. This is a critical oversight, as it limits the practical applicability of the framework. The authors do not discuss how the identifiability results would be affected by non-Gaussian latent variables with heavier tails or multiple modes, which are common in many real-world scenarios. Furthermore, the paper does not provide any guidance on how to detect or mitigate the impact of such deviations, which is crucial for practical applications. This limitation is evident throughout the paper, from the theoretical analysis to the experimental validation. The experiments primarily focus on Gaussian latent variables, and the 'Latent-Distribution Sweep' experiment specifically tests the Gaussian latent variable assumption by comparing the performance of the JEPA framework on OU processes (which imply Gaussianity) with that on real robot trajectories. The results of this experiment clearly show a significant performance difference, highlighting the importance of the Gaussian assumption. The lack of exploration into non-Gaussian latent variables is a significant gap in the paper's analysis, and I have high confidence in this assessment based on the explicit assumptions stated in the paper and the absence of any discussion or experiments with non-Gaussian latents. The practical implications of this limitation are substantial, as it restricts the applicability of the theoretical findings to real-world scenarios where the Gaussian assumption is unlikely to hold. This weakness significantly impacts the overall practical relevance of the paper, and I believe it is a critical point that needs to be addressed in future work.


## Suggestions:

To address the identified weakness regarding the Gaussian latent variable assumption, I recommend several concrete and actionable improvements. First and foremost, the authors should conduct a thorough investigation into the robustness of their theoretical results to deviations from the Gaussian assumption. This could involve analyzing the identifiability conditions under different types of non-Gaussian distributions, such as heavy-tailed distributions or mixtures of Gaussians. It would be beneficial to explore how the performance of the JEPA framework degrades as the latent variables deviate from a Gaussian distribution. For example, the authors could conduct experiments using synthetic datasets with non-Gaussian latent variables and analyze the impact on the linear identifiability of the learned representations. This would provide a more comprehensive understanding of the limitations of the proposed framework and its applicability to real-world scenarios. Furthermore, the authors should consider developing methods to detect and mitigate the impact of non-Gaussian latent variables. This could involve using robust statistical techniques or incorporating prior knowledge about the data distribution. The authors should also explore alternative loss functions that are more robust to non-Gaussian distributions. This would make the framework more adaptable to real-world scenarios where the Gaussian assumption is unlikely to hold. In addition to the theoretical analysis, the authors should also provide more practical guidance on how to apply the JEPA framework in real-world scenarios where the Gaussian assumption may not hold. This could involve providing recommendations on how to choose the appropriate loss function for different types of data and latent variables. For example, the authors could explore the use of alternative loss functions that are more robust to non-Gaussian distributions. Furthermore, the authors should provide practical guidelines on how to select the hyperparameters of the JEPA framework, such as the learning rate and the regularization parameters, to ensure optimal performance in the presence of non-Gaussian latent variables. This would make the framework more accessible and useful for practitioners who are interested in applying it to real-world problems. The authors should also consider providing open-source code and tools to facilitate the use of the JEPA framework. Finally, the authors should discuss the limitations of their theoretical analysis and the potential impact of these limitations on the practical application of the JEPA framework. This could involve acknowledging that the theoretical results may not hold in all real-world scenarios and that the performance of the framework may degrade when the Gaussian assumption is violated. The authors should also discuss the potential for future research to address these limitations and to develop more robust and practical methods for learning world models. This would help to ensure that the JEPA framework is used appropriately and that its limitations are clearly understood by the research community. These suggestions are directly linked to the identified weakness and are aimed at improving the practical applicability and robustness of the framework.


## Questions:

Based on my analysis, I have several questions that I believe are crucial for further understanding and development of this work. First, how sensitive is the JEPA framework to deviations from the Gaussian latent variable assumption? Could you provide additional experiments or theoretical insights into the robustness of the linear identifiability results when the latent variables are not perfectly Gaussian? This question directly addresses the core weakness of the paper and seeks clarification on the framework's limitations. Second, could you elaborate on the computational costs associated with the JEPA framework, particularly as the dimensionality of the latent space increases? How does the computational cost scale with the number of samples and the dimensionality of the latent space? This question is important for understanding the practical feasibility of the framework in real-world applications. Third, the paper mentions that the choice of the loss function (e.g., SIGReg, VICReg, InfoNCE) affects identifiability. Could you provide more guidance on how to select the appropriate loss function for a given task? Are there specific characteristics of the data or the environment that should be considered when choosing a loss function? This question seeks to clarify the practical implications of the theoretical findings and provide guidance for real-world applications. Fourth, the paper's theoretical analysis is based on the assumption of Gaussian latent variables. What are the potential implications of this assumption for the practical application of the JEPA framework? How might the framework's performance be affected in scenarios where the latent variables are not Gaussian? This question seeks to understand the limitations of the theoretical analysis and its practical relevance. Finally, the paper does not discuss the potential for future research to address the limitations of the Gaussian assumption. What are the most promising directions for future research in this area? How might we develop more robust and practical methods for learning world models that do not rely on the Gaussian assumption? This question seeks to identify future research directions and to contribute to the development of more robust and practical methods for learning world models. These questions are aimed at clarifying key uncertainties and guiding future research in this area.


## Rating:

6.25


## Confidence:

2.75


## Decision:

Accept
}