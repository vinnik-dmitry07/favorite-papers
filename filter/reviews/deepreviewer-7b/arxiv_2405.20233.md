I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

This paper proposes a method to accelerate the grokking phenomenon. Grokking is the sudden generalization after a period of overfitting. The proposed method is based on the observation that the parameter trajectory can be decomposed into two components: fast-varying and slow-varying components. The fast-varying components are responsible for overfitting, while the slow-varying components are responsible for generalization. The proposed method filters the slow-varying components to accelerate generalization. The experiments show that the proposed method can reduce the number of iterations to reach the same accuracy.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The proposed method is simple and easy to implement.
2. The paper is well-written and easy to follow.
3. The experiments are comprehensive and convincing.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is based on the observation that the parameter trajectory can be decomposed into two components: fast-varying and slow-varying components. However, this observation is not novel, as it has been widely used in many other areas, such as physics and signal processing. The paper does not provide a rigorous theoretical justification for why this decomposition is particularly relevant to the grokking phenomenon, beyond the intuitive idea that fast changes lead to overfitting and slow changes lead to generalization. A more formal analysis, perhaps drawing connections to existing work on gradient dynamics and optimization landscapes, would significantly strengthen the theoretical foundation of this work.
2. The proposed method is based on the assumption that the slow-varying components are responsible for generalization. However, this assumption is not always true, as the fast-varying components may also contribute to generalization, especially in the early stages of training. The paper does not explore the potential interactions between the fast and slow components, and how these interactions might affect the generalization performance. A more detailed analysis of the conditions under which the slow components dominate generalization would be beneficial.
3. The experiments are limited to a few specific tasks and datasets. While the results are promising, it is unclear whether the proposed method can generalize to other tasks and datasets, especially those with different characteristics. The paper should include experiments on a wider range of tasks, including those with more complex data distributions and higher dimensionality, to demonstrate the robustness of the proposed method. Furthermore, the paper should also consider comparing the proposed method with other existing techniques for accelerating generalization, to better understand its relative advantages and limitations.

### Suggestions

To address the lack of theoretical justification, the authors should explore connections between their parameter decomposition and existing theories on gradient dynamics and optimization landscapes. For instance, they could investigate how the proposed method affects the curvature of the loss landscape and whether it leads to flatter minima, which are known to be associated with better generalization. A theoretical analysis of the convergence properties of the proposed method, perhaps using tools from dynamical systems theory, would also be valuable. This would provide a more rigorous understanding of why the method works and under what conditions it is expected to be effective. Furthermore, the authors should consider providing a more detailed explanation of the relationship between the proposed method and existing techniques for controlling the learning rate or momentum, as these methods also aim to influence the speed of parameter updates.

To address the assumption that slow-varying components are primarily responsible for generalization, the authors should conduct a more thorough analysis of the interplay between fast and slow components. This could involve visualizing the parameter trajectories in both the fast and slow subspaces, and examining how these trajectories evolve during training. The authors should also investigate whether the fast components contribute to generalization in the early stages of training, and how the proposed method affects this contribution. Furthermore, the authors should explore the possibility of using adaptive filtering techniques that can dynamically adjust the weights of the fast and slow components based on the training progress. This could potentially lead to a more robust and effective method for accelerating generalization.

To improve the generalizability of the experimental results, the authors should conduct experiments on a wider range of tasks and datasets, including those with more complex data distributions and higher dimensionality. They should also consider comparing the proposed method with other existing techniques for accelerating generalization, such as early stopping, learning rate scheduling, and regularization techniques. This would provide a more comprehensive evaluation of the proposed method and help to identify its strengths and weaknesses. Additionally, the authors should provide a more detailed analysis of the computational cost of the proposed method, and compare it with the computational cost of other acceleration techniques. This would help to assess the practical applicability of the proposed method in real-world scenarios.

### Questions

1. Can the proposed method be applied to other optimization algorithms, such as Adam or SGD with momentum?
2. How does the proposed method affect the generalization performance when the training data is noisy or imbalanced?
3. How does the proposed method affect the generalization performance when the model is overparameterized?

### Rating

5

### Confidence

3

**********

## Reviewer 2

### Summary

The paper proposes a method to accelerate the grokking phenomenon. The authors observe that the parameter updates of a neural network during training can be decomposed into fast-varying and slow-varying components. The fast-varying components are responsible for the rapid overfitting, while the slow-varying components contribute to generalization. The proposed method amplifies the slow-varying components of the gradients to accelerate the generalization process. The authors demonstrate the effectiveness of their approach through experiments on various tasks, including algorithmic data, MNIST, QM9, and IMDb datasets.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.
- The authors provide a clear and intuitive explanation of the grokking phenomenon and the proposed method.
- The experiments are comprehensive and cover a wide range of tasks and datasets.
- The authors provide a detailed analysis of the experimental results and discuss the limitations of their approach.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method is based on the observation that the parameter updates of a neural network during training can be decomposed into fast-varying and slow-varying components. However, this observation is not novel, as it has been widely used in many other areas, such as physics and signal processing. The paper does not provide a rigorous theoretical justification for why this decomposition is particularly relevant to the grokking phenomenon, beyond the intuitive idea that fast changes lead to overfitting and slow changes lead to generalization. A more formal analysis, perhaps drawing connections to existing work on gradient dynamics and optimization landscapes, would significantly strengthen the theoretical foundation of this work.
- The proposed method is based on the assumption that the slow-varying components are responsible for generalization. However, this assumption is not always true, as the fast-varying components may also contribute to generalization, especially in the early stages of training. The paper does not explore the potential interactions between the fast and slow components, and how these interactions might affect the generalization performance. A more detailed analysis of the conditions under which the slow components dominate generalization would be beneficial.
- The experiments are limited to a few specific tasks and datasets. While the results are promising, it is unclear whether the proposed method can generalize to other tasks and datasets, especially those with different characteristics. The paper should include experiments on a wider range of tasks, including those with more complex data distributions and higher dimensionality, to demonstrate the robustness of the proposed method. Furthermore, the paper should also consider comparing the proposed method with other existing techniques for accelerating generalization, to better understand its relative advantages and limitations.

### Suggestions

The paper would benefit from a more rigorous theoretical analysis of the proposed method. While the intuition behind separating fast and slow components is clear, the paper lacks a formal justification for why this decomposition is particularly relevant to the grokking phenomenon. Specifically, the authors should explore connections to existing theories on gradient dynamics and optimization landscapes. For instance, they could investigate how the proposed method affects the curvature of the loss landscape and whether it leads to flatter minima, which are known to be associated with better generalization. A theoretical analysis of the convergence properties of the proposed method, perhaps using tools from dynamical systems theory, would also be valuable. This would provide a more rigorous understanding of why the method works and under what conditions it is expected to be effective. Furthermore, the authors should consider providing a more detailed explanation of the relationship between the proposed method and existing techniques for controlling the learning rate or momentum, as these methods also aim to influence the speed of parameter updates.

To address the assumption that slow-varying components are primarily responsible for generalization, the authors should conduct a more thorough analysis of the interplay between fast and slow components. This could involve visualizing the parameter trajectories in both the fast and slow subspaces, and examining how these trajectories evolve during training. The authors should also investigate whether the fast components contribute to generalization in the early stages of training, and how the proposed method affects this contribution. Furthermore, the authors should explore the possibility of using adaptive filtering techniques that can dynamically adjust the weights of the fast and slow components based on the training progress. This could potentially lead to a more robust and effective method for accelerating generalization. The paper should also include a discussion of the limitations of the proposed method, and under what conditions it might not be effective.

Finally, the experimental evaluation should be expanded to include a wider range of tasks and datasets. The current experiments are limited to a few specific tasks and datasets, which makes it difficult to assess the generalizability of the proposed method. The authors should include experiments on more complex datasets with higher dimensionality, such as image classification tasks using convolutional neural networks or natural language processing tasks using transformers. Furthermore, the paper should also consider comparing the proposed method with other existing techniques for accelerating generalization, such as early stopping, learning rate scheduling, or regularization techniques. This would provide a more comprehensive evaluation of the proposed method and help to better understand its relative advantages and limitations. The authors should also provide a more detailed analysis of the computational cost of the proposed method, and compare it with the computational cost of other acceleration techniques.

### Questions

- How does the proposed method affect the generalization performance when the training data is noisy or imbalanced?
- How does the proposed method affect the generalization performance when the model is overparameterized?
- How does the proposed method compare with other existing techniques for accelerating generalization, such as early stopping, learning rate scheduling, or regularization techniques?

### Rating

5

### Confidence

4

**********

## Reviewer 3

### Summary

The paper proposes a simple method to accelerate the grokking phenomenon, which is a phenomenon where generalization happens much later than overfitting. The method is based on the observation that the parameter trajectory of a model during training can be decomposed into two components: fast-varying and slow-varying components. The fast-varying components are responsible for overfitting, while the slow-varying components are responsible for generalization. The proposed method amplifies the slow-varying components of the gradients to accelerate the generalization process. The paper demonstrates the effectiveness of the proposed method on several tasks, including algorithmic data, MNIST, QM9, and IMDb datasets.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and easy to implement.
3. The experiments are comprehensive and convincing.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is based on the observation that the parameter trajectory of a model during training can be decomposed into two components: fast-varying and slow-varying components. However, this observation is not novel, as it has been widely used in many other areas, such as physics and signal processing. The paper does not provide a rigorous theoretical justification for why this decomposition is particularly relevant to the grokking phenomenon, beyond the intuitive idea that fast changes lead to overfitting and slow changes lead to generalization. A more formal analysis, perhaps drawing connections to existing work on gradient dynamics and optimization landscapes, would significantly strengthen the theoretical foundation of this work.
2. The proposed method is based on the assumption that the slow-varying components are responsible for generalization. However, this assumption is not always true, as the fast-varying components may also contribute to generalization, especially in the early stages of training. The paper does not explore the potential interactions between the fast and slow components, and how these interactions might affect the generalization performance. A more detailed analysis of the conditions under which the slow components dominate generalization would be beneficial.
3. The experiments are limited to a few specific tasks and datasets. While the results are promising, it is unclear whether the proposed method can generalize to other tasks and datasets, especially those with different characteristics. The paper should include experiments on a wider range of tasks, including those with more complex data distributions and higher dimensionality, to demonstrate the robustness of the proposed method. Furthermore, the paper should also consider comparing the proposed method with other existing techniques for accelerating generalization, to better understand its relative advantages and limitations.

### Suggestions

The paper introduces an interesting approach to accelerate grokking by focusing on amplifying slow-varying components of the gradient. However, the theoretical justification for this approach needs further strengthening. While the intuition behind separating fast and slow components is clear, the paper lacks a rigorous analysis of why this decomposition is particularly relevant to the grokking phenomenon. Specifically, the authors should explore connections to existing theories on gradient dynamics and optimization landscapes. For instance, how does the proposed method affect the curvature of the loss landscape and whether it leads to flatter minima, which are known to be associated with better generalization? A more formal analysis, perhaps using tools from dynamical systems theory, would significantly enhance the theoretical foundation of this work. Furthermore, the paper should provide a more detailed explanation of the relationship between the proposed method and existing techniques for controlling the learning rate or momentum, as these methods also aim to influence the speed of parameter updates.

To address the assumption that slow-varying components are primarily responsible for generalization, the authors should conduct a more thorough analysis of the interplay between fast and slow components. This could involve visualizing the parameter trajectories in both the fast and slow subspaces and examining how these trajectories evolve during training. The authors should also investigate whether the fast components contribute to generalization in the early stages of training, and how the proposed method affects this contribution. Furthermore, the authors should explore the possibility of using adaptive filtering techniques that can dynamically adjust the weights of the fast and slow components based on the training progress. This could potentially lead to a more robust and effective method for accelerating generalization. The paper should also include a discussion of the limitations of the proposed method, and under what conditions it might not be effective.

Finally, the experimental evaluation should be expanded to include a wider range of tasks and datasets. The current experiments are limited to a few specific tasks and datasets, which makes it difficult to assess the generalizability of the proposed method. The authors should include experiments on more complex datasets with higher dimensionality, such as image classification tasks using convolutional neural networks or natural language processing tasks using transformers. Furthermore, the paper should also consider comparing the proposed method with other existing techniques for accelerating generalization, such as early stopping, learning rate scheduling, or regularization techniques. This would provide a more comprehensive evaluation of the proposed method and help to better understand its relative advantages and limitations. The authors should also provide a more detailed analysis of the computational cost of the proposed method, and compare it with the computational cost of other acceleration techniques.

### Questions

1. How does the proposed method affect the generalization performance when the training data is noisy or imbalanced?
2. How does the proposed method affect the generalization performance when the model is overparameterized?
3. How does the proposed method compare with other existing techniques for accelerating generalization, such as early stopping, learning rate scheduling, or regularization techniques?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

This paper proposes a method to accelerate the grokking phenomenon in neural networks. The authors observe that the parameter updates during training can be decomposed into fast-varying and slow-varying components. They propose amplifying the slow-varying components of the gradients to accelerate generalization. The method is evaluated on several tasks, including algorithmic data, MNIST, QM9, and IMDb datasets, demonstrating significant improvements in convergence speed.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and easy to implement.
- The experiments are comprehensive and convincing.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method is based on the observation that the parameter trajectory of a model during training can be decomposed into two components: fast-varying and slow-varying components. However, this observation is not novel, as it has been widely used in many other areas, such as physics and signal processing. The paper does not provide a rigorous theoretical justification for why this decomposition is particularly relevant to the grokking phenomenon, beyond the intuitive idea that fast changes lead to overfitting and slow changes lead to generalization. A more formal analysis, perhaps drawing connections to existing work on gradient dynamics and optimization landscapes, would significantly strengthen the theoretical foundation of this work.
- The proposed method is based on the assumption that the slow-varying components are responsible for generalization. However, this assumption is not always true, as the fast-varying components may also contribute to generalization, especially in the early stages of training. The paper does not explore the potential interactions between the fast and slow components, and how these interactions might affect the generalization performance. A more detailed analysis of the conditions under which the slow components dominate generalization would be beneficial.
- The experiments are limited to a few specific tasks and datasets. While the results are promising, it is unclear whether the proposed method can generalize to other tasks and datasets, especially those with different characteristics. The paper should include experiments on a wider range of tasks, including those with more complex data distributions and higher dimensionality, to demonstrate the robustness of the proposed method. Furthermore, the paper should also consider comparing the proposed method with other existing techniques for accelerating generalization, to better understand its relative advantages and limitations.

### Suggestions

To strengthen the theoretical foundation of the proposed method, the authors should delve deeper into the mathematical properties of the parameter updates. Specifically, they could analyze the eigenvalue spectrum of the Hessian matrix of the loss function to understand the curvature of the loss landscape and how the proposed method affects it. This would provide a more rigorous justification for why amplifying the slow-varying components leads to faster generalization. Furthermore, the authors could explore the relationship between the proposed method and existing optimization techniques, such as momentum-based methods, to provide a more comprehensive understanding of its behavior. A theoretical analysis of the convergence properties of the proposed method would also be valuable, potentially using tools from dynamical systems theory to analyze the stability and convergence rate of the algorithm.

To address the assumption that slow-varying components are primarily responsible for generalization, the authors should conduct a more thorough analysis of the interplay between fast and slow components. This could involve visualizing the parameter trajectories in both the fast and slow subspaces and examining how these trajectories evolve during training. The authors should also investigate whether the fast components contribute to generalization in the early stages of training, and how the proposed method affects this contribution. Furthermore, the authors should explore adaptive filtering techniques that can dynamically adjust the weights of the fast and slow components based on the training progress. This could potentially lead to a more robust and effective method for accelerating generalization. The authors should also consider using techniques such as spectral analysis to quantify the contribution of each component to the overall parameter update.

Finally, the authors should expand the experimental evaluation to include a wider range of tasks and datasets. This should include tasks with more complex data distributions and higher dimensionality, such as image classification tasks using convolutional neural networks or natural language processing tasks using transformers. The authors should also compare the proposed method with other existing techniques for accelerating generalization, such as early stopping, learning rate scheduling, or regularization techniques. This would provide a more comprehensive evaluation of the proposed method and help to better understand its relative advantages and limitations. The authors should also provide a more detailed analysis of the computational cost of the proposed method, and compare it with the computational cost of other acceleration techniques.

### Questions

Please refer to the weaknesses section.

### Rating

6

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers for the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

Plan:
1. Read each reviewer's weakness.
2. Find the relevant section in the paper.
3. Extract evidence (quotes, formulas, experimental details) to support the weakness.
4. If the weakness is about missing information, confirm that the information is indeed absent.
5. Synthesize the findings and conclude whether the weakness is valid, partially valid, or invalid.
**Review 1 Weaknesses:**

1. Weakness Statement:
"The proposed method is based on the observation that the parameter trajectory of a model during training can be decomposed into two components: fast-varying and slow-varying components. However, this observation is not novel, as it has been widely used in many other areas, such as physics and signal processing. The paper does not provide a rigorous theoretical justification for why this decomposition is particularly relevant to the grokking phenomenon, beyond the intuitive idea that fast changes lead to overfitting and slow changes lead to generalization. A more formal analysis, perhaps drawing connections to existing work on gradient dynamics and optimization landscapes, would significantly strengthen the theoretical foundation of this work."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper introduces the decomposition in the "Method" section, specifically in the "Filter Design" subsection: "The parameter update function u(t) can be decomposed into two components: the fast-varying component and the slow-varying component. The fast-varying component is responsible for the rapid overfitting, while the slow-varying component contributes to the generalization."
   - The paper does not provide a formal mathematical proof or derivation for this decomposition in the context of grokking.
   - The paper mentions the intuition behind the decomposition: "The parameter update function u(t) can be decomposed into two components: the fast-varying component and the slow-varying component. The fast-varying component is responsible for the rapid overfitting, while the slow-varying component contributes to the generalization."
b) Literature Gap Analysis:
   - The paper cites works related to grokking and optimization techniques but does not explicitly connect the parameter decomposition to established theories in physics or signal processing that use similar concepts.

3. Validation Analysis:
   - The reviewer correctly points out that the decomposition idea is not novel. The paper itself acknowledges the intuition behind the separation.
   - The paper lacks a rigorous theoretical justification connecting this decomposition to the specific dynamics of the grokking phenomenon. It relies on the intuitive explanation that fast changes lead to overfitting and slow changes lead to generalization.
   - The suggestion to connect to gradient dynamics and optimization landscapes is valid, as the paper does not delve into these areas for a deeper theoretical grounding.

4. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of formal proof for the decomposition in the context of grokking, intuitive explanation rather than rigorous theory, no connection to theories in related fields.

1. Weakness Statement:
"The proposed method is based on the assumption that the slow-varying components are responsible for generalization. However, this assumption is not always true, as the fast-varying components may also contribute to generalization, especially in the early stages of training. The paper does not explore the potential interactions between the fast and slow components, and how these interactions might affect the generalization performance. A more detailed analysis of the conditions under which the slow components dominate generalization would be beneficial."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper states in the "Filter Design" subsection: "The slow-varying component is responsible for generalization."
   - The paper does not provide a detailed analysis of the interplay between fast and slow components.
   - The paper does not explore scenarios where fast components might contribute to generalization.
b) Experimental Validation:
   - The experiments focus on demonstrating the overall acceleration of generalization by amplifying the slow-varying component.
   - There is no specific experiment designed to analyze the contribution of fast components to generalization or the conditions under which slow components dominate.

3. Validation Analysis:
   - The reviewer accurately identifies the assumption that slow components are primarily responsible for generalization.
   - The paper's methodology and experiments are structured around this assumption.
   - The lack of analysis on the potential contributions of fast components and their interactions with slow components is a valid weakness.

4. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Explicit statement about slow components being responsible for generalization, lack of analysis on fast component contributions or their interactions.

1. Weakness Statement:
"The experiments are limited to a few specific tasks and datasets. While the results are promising, it is unclear whether the proposed method can generalize to other tasks and datasets, especially those with different characteristics. The paper should include experiments on a wider range of tasks, including those with more complex data distributions and higher dimensionality, to demonstrate the robustness of the proposed method. Furthermore, the paper should also consider comparing the proposed method with other existing techniques for accelerating generalization, to better understand its relative advantages and limitations."

2. Evidence Collection:
a) Experimental Validation:
   - The paper presents experiments on "Algorithmic Data", "MNIST", "QM9", and "IMDb".
   - While these cover different domains, the reviewer suggests expanding to more complex datasets and potentially including comparisons with a broader range of acceleration techniques.
   - The "Experiments" section details the setup for each dataset and task.
   - The "Related Work" section mentions other acceleration techniques like early stopping and learning rate scheduling, but these are not directly compared in the experimental section.

3. Validation Analysis:
   - The reviewer's point about the limited number of tasks and datasets is valid. While the chosen datasets are diverse, exploring more complex scenarios would strengthen the generalizability claims.
   - The lack of direct comparison with other acceleration techniques in the experiments is also a valid point. While the paper mentions these techniques in related work, empirical comparison would provide a clearer picture of the proposed method's advantages.

4. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Limited number of datasets in the experiments, absence of direct comparison with other acceleration techniques in the experimental results.

**Review 2 Weaknesses:**

1. Weakness Statement:
"The proposed method is based on the observation that the parameter trajectory of a model during training can be decomposed into two components: fast-varying and slow-varying components. However, this observation is not novel, as it has been widely used in many other areas, such as physics and signal processing. The paper does not provide a rigorous theoretical justification for why this decomposition is particularly relevant to the grokking phenomenon, beyond the intuitive idea that fast changes lead to overfitting and slow changes lead to generalization. A more formal analysis, perhaps drawing connections to existing work on gradient dynamics and optimization landscapes, would significantly strengthen the theoretical foundation of this work."

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's first point. Please see the validation for that point.

3. Validation Analysis:
   - Same as Reviewer 1's first point.

4. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1's first point.

1. Weakness Statement:
"The proposed method is based on the assumption that the slow-varying components are responsible for generalization. However, this assumption is not always true, as the fast-varying components may also contribute to generalization, especially in the early stages of training. The paper does not explore the potential interactions between the fast and slow components, and how these interactions might affect the generalization performance. A more detailed analysis of the conditions under which the slow components dominate generalization would be beneficial."

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's second point. Please see the validation for that point.

3. Validation Analysis:
   - Same as Reviewer 1's second point.

4. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1's second point.

1. Weakness Statement:
"The experiments are limited to a few specific tasks and datasets. While the results are promising, it is unclear whether the proposed method can generalize to other tasks and datasets, especially those with different characteristics. The paper should include experiments on a wider range of tasks, including those with more complex data distributions and higher dimensionality, to demonstrate the robustness of the proposed method. Furthermore, the paper should also consider comparing the proposed method with other existing techniques for accelerating generalization, to better understand its relative advantages and limitations."

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's third point. Please see the validation for that point.

3. Validation Analysis:
   - Same as Reviewer 1's third point.

4. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1's third point.

**Review 3 Weaknesses:**

1. Weakness Statement:
"The proposed method is based on the observation that the parameter trajectory of a model during training can be decomposed into two components: fast-varying and slow-varying components. However, this observation is not novel, as it has been widely used in many other areas, such as physics and signal processing. The paper does not provide a rigorous theoretical justification for why this decomposition is particularly relevant to the grokking phenomenon, beyond the intuitive idea that fast changes lead to overfitting and slow changes lead to generalization. A more formal analysis, perhaps drawing connections to existing work on gradient dynamics and optimization landscapes, would significantly strengthen the theoretical foundation of this work."

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's first point. Please see the validation for that point.

3. Validation Analysis:
   - Same as Reviewer 1's first point.

4. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1's first point.

1. Weakness Statement:
"The proposed method is based on the assumption that the slow-varying components are responsible for generalization. However, this assumption is not always true, as the fast-varying components may also contribute to generalization, especially in the early stages of training. The paper does not explore the potential interactions between the fast and slow components, and how these interactions might affect the generalization performance. A more detailed analysis of the conditions under which the slow components dominate generalization would be beneficial."

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's second point. Please see the validation for that point.

3. Validation Analysis:
   - Same as Reviewer 1's second point.

4. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1's second point.

1. Weakness Statement:
"The experiments are limited to a few specific tasks and datasets. While the results are promising, it is unclear whether the proposed method can generalize to other tasks and datasets, especially those with different characteristics. The paper should include experiments on a wider range of tasks, including those with more complex data distributions and higher dimensionality, to demonstrate the robustness of the proposed method. Furthermore, the paper should also consider comparing the proposed method with other existing techniques for accelerating generalization, to better understand its relative advantages and limitations."

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's third point. Please see the validation for that point.

3. Validation Analysis:
   - Same as Reviewer 1's third point.

4. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1's third point.

**Review 4 Weaknesses:**

1. Weakness Statement:
"The proposed method is based on the observation that the parameter trajectory of a model during training can be decomposed into two components: fast-varying and slow-varying components. However, this observation is not novel, as it has been widely used in many other areas, such as physics and signal processing. The paper does not provide a rigorous theoretical justification for why this decomposition is particularly relevant to the grokking phenomenon, beyond the intuitive idea that fast changes lead to overfitting and slow changes lead to generalization. A more formal analysis, perhaps drawing connections to existing work on gradient dynamics and optimization landscapes, would significantly strengthen the theoretical foundation of this work."

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's first point. Please see the validation for that point.

3. Validation Analysis:
   - Same as Reviewer 1's first point.

4. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1's first point.

1. Weakness Statement:
"The proposed method is based on the assumption that the slow-varying components are responsible for generalization. However, this assumption is not always true, as the fast-varying components may also contribute to generalization, especially in the early stages of training. The paper does not explore the potential interactions between the fast and slow components, and how these interactions might affect the generalization performance. A more detailed analysis of the conditions under which the slow components dominate generalization would be beneficial."

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's second point. Please see the validation for that point.

3. Validation Analysis:
   - Same as Reviewer 1's second point.

4. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1's second point.

1. Weakness Statement:
"The experiments are limited to a few specific tasks and datasets. While the results are promising, it is unclear whether the proposed method can generalize to other tasks and datasets, especially those with different characteristics. The paper should include experiments on a wider range of tasks, including those with more complex data distributions and higher dimensionality, to demonstrate the robustness of the proposed method. Furthermore, the paper should also consider comparing the proposed method with other existing techniques for accelerating generalization, to better understand its relative advantages and limitations."

2. Evidence Collection:
   - This is the same weakness as Reviewer 1's third point. Please see the validation for that point.

3. Validation Analysis:
   - Same as Reviewer 1's third point.

4. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 1's third point.

1. Weakness Statement:
"How does the proposed method affect the generalization performance when the training data is noisy or imbalanced?"

2. Evidence Collection:
   - The paper does not include experiments or analysis on the robustness of the method to noisy or imbalanced training data.

3. Validation Analysis:
   - The reviewer correctly identifies a missing experimental analysis. The paper focuses on standard datasets but does not explore the impact of data quality.

4. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Absence of experiments or analysis on noisy or imbalanced data.

1. Weakness Statement:
"How does the proposed method affect the generalization performance when the model is overparameterized?"

2. Evidence Collection:
   - The paper includes experiments on MNIST with a two-layer ReLU-MLP, which has more parameters than the number of training samples (overparameterized). However, it doesn't systematically explore the effect of varying degrees of overparameterization.

3. Validation Analysis:
   - While the paper touches on overparameterization with MNIST, it doesn't provide a comprehensive analysis of how the method performs under different levels of overparameterization.

4. Conclusion:
   - Validity status: Partially Valid
   - Confidence level: Medium
   - Key supporting evidence: MNIST experiment with overparameterized model, but lack of systematic analysis.

1. Weakness Statement:
"How does the proposed method compare with other existing techniques for accelerating generalization, such as early stopping, learning rate scheduling, or regularization techniques?"

2. Evidence Collection:
   - The "Experiments" section compares the proposed method with the baseline algorithm (Algorithm 1) but does not include direct comparisons with other acceleration techniques like early stopping or learning rate scheduling.

3. Validation Analysis:
   - The reviewer correctly points out the lack of direct comparison with other acceleration techniques. While related techniques are mentioned in the "Related Work", empirical comparison is missing.

4. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Lack of direct experimental comparison with other acceleration techniques.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces a novel method aimed at accelerating the grokking phenomenon in neural networks, a phenomenon characterized by a significant delay between overfitting and generalization. The authors' core observation is that the parameter trajectory of a neural network during training can be decomposed into two distinct components: a fast-varying component responsible for rapid overfitting and a slow-varying component crucial for generalization. Based on this insight, they propose a filtering technique that amplifies the slow-varying component of the gradients, thereby accelerating the generalization process. The method is implemented by applying a low-pass filter to the gradient updates, effectively emphasizing the slowly varying components that are believed to drive generalization. The authors demonstrate the effectiveness of their approach through a series of experiments on various tasks, including algorithmic data, MNIST, QM9, and IMDb datasets. These experiments show that the proposed method can significantly reduce the number of iterations required to achieve a given level of generalization, thereby accelerating the grokking phenomenon. The paper's main contribution lies in its novel interpretation of the parameter trajectory and the proposed filtering technique, which offers a new perspective on the dynamics of neural network training and generalization. The authors present a clear and intuitive explanation of their method, making it accessible to a broad audience. The experimental results, while promising, are limited to a few specific tasks and datasets, and the paper lacks a rigorous theoretical analysis of the proposed method. Despite these limitations, the paper provides a valuable contribution to the understanding of the grokking phenomenon and offers a promising direction for future research in this area. The authors' approach is simple to implement and can be easily integrated into existing training pipelines, making it a practical solution for accelerating the training of neural networks. The paper's findings suggest that carefully analyzing the frequency components of gradient updates can lead to more efficient training algorithms, and the proposed method provides a concrete example of this approach. Overall, the paper presents a well-motivated and clearly articulated method for accelerating grokking, supported by empirical evidence. However, the lack of theoretical justification and limited experimental scope raise questions about the generalizability and robustness of the proposed method, which are addressed in the following sections.


## Soundness:

2.75


## Presentation:

3.0


## Contribution:

2.0


## Strengths:

The paper's primary strength lies in its clear and intuitive explanation of the proposed method. The authors effectively articulate the core idea of decomposing the parameter trajectory into fast and slow components and then amplifying the slow-varying component to accelerate generalization. This approach is both conceptually simple and practically implementable, making it a valuable contribution to the field. The method itself, which involves applying a low-pass filter to the gradient updates, is straightforward to understand and can be easily integrated into existing training pipelines. This simplicity is a significant advantage, as it allows researchers and practitioners to readily adopt and experiment with the proposed technique. Furthermore, the paper is well-written and easy to follow, which enhances its accessibility to a broad audience. The authors present their ideas in a logical and coherent manner, making it easy to grasp the underlying concepts and the proposed approach. The experimental results, while limited in scope, are promising and demonstrate the potential of the method to accelerate the grokking phenomenon. The authors have conducted experiments on a variety of tasks, including algorithmic data, MNIST, QM9, and IMDb datasets, which provides a reasonable basis for evaluating the effectiveness of their approach. The results consistently show that the proposed method can significantly reduce the number of iterations required to achieve a given level of generalization, thereby accelerating the training process. This empirical evidence supports the authors' claim that amplifying the slow-varying component of the gradients can lead to faster generalization. The paper also provides a clear motivation for the proposed method, drawing on the observation that overfitting occurs rapidly in the early stages of training, while generalization is achieved later. This motivation is well-supported by the existing literature on the grokking phenomenon, which highlights the importance of understanding the dynamics of neural network training and generalization. The authors' approach of focusing on the slow-varying components of the gradients is a novel contribution to the field, and it offers a new perspective on the underlying mechanisms of generalization. The paper's focus on a practical and easily implementable method is also a strength, as it makes the proposed approach accessible to a wider range of researchers and practitioners. The authors' work provides a valuable starting point for further research into the optimization dynamics of neural networks and the factors that contribute to generalization.


## Weaknesses:

Despite its strengths, the paper suffers from several significant weaknesses that limit its overall impact and generalizability. A primary concern is the lack of a rigorous theoretical justification for the proposed method. While the authors provide an intuitive explanation for why amplifying the slow-varying components of the gradients might lead to faster generalization, they do not offer a formal analysis or connect their approach to existing theories on gradient dynamics and optimization landscapes. Specifically, the paper does not delve into connections to existing theories on gradient dynamics and optimization landscapes, such as those found in physics and signal processing. The decomposition of the parameter trajectory into fast and slow components is presented as an observation, not a novel theoretical contribution, and the paper lacks a formal mathematical proof or derivation for this decomposition in the context of grokking. This absence of a rigorous theoretical foundation weakens the paper's claims and makes it difficult to assess the generalizability of the proposed method. The authors rely on an intuitive explanation that fast changes lead to overfitting and slow changes lead to generalization, but this explanation is not supported by a formal analysis. This lack of theoretical grounding makes it difficult to understand why the method works and under what conditions it might be expected to be effective. My confidence in this weakness is high, as the paper explicitly lacks the necessary mathematical derivations and connections to existing theories. Another significant weakness is the assumption that the slow-varying components are primarily responsible for generalization. While the paper states this assumption as a basis for their method, it does not explore the potential interactions between the fast and slow components, nor does it analyze whether the fast components might contribute to generalization, especially in the early stages of training. The paper does not provide a detailed analysis of the interplay between fast and slow components, and it does not investigate whether the fast components contribute to generalization in the early stages of training. This assumption is not always true, and the paper's methodology and experiments are structured around this assumption, which limits the scope of the proposed method. The lack of analysis on the potential contributions of fast components and their interactions with slow components is a valid weakness. My confidence in this weakness is high, as the paper explicitly states the assumption and lacks any analysis of the fast components. Furthermore, the experimental evaluation is limited in scope. The paper presents experiments on a few specific tasks and datasets, including algorithmic data, MNIST, QM9, and IMDb. While these results are promising, it is unclear whether the proposed method can generalize to other tasks and datasets, especially those with different characteristics. The paper lacks experiments on more complex datasets with higher dimensionality, such as image classification tasks using convolutional neural networks or natural language processing tasks using transformers. This limited experimental scope raises concerns about the robustness and generalizability of the proposed method. The paper also lacks a direct comparison with other existing techniques for accelerating generalization, such as early stopping, learning rate scheduling, or regularization techniques. While the paper mentions these techniques in the related work section, it does not provide any empirical comparison. This lack of comparison makes it difficult to assess the relative advantages and limitations of the proposed method. My confidence in this weakness is high, as the paper explicitly lacks the necessary experiments and comparisons. Finally, the paper does not address the impact of noisy or imbalanced training data on the proposed method. The paper focuses on standard datasets but does not explore the robustness of the method to data quality. This is a significant limitation, as real-world datasets are often noisy or imbalanced, and the method's performance in such scenarios is unclear. My confidence in this weakness is high, as the paper explicitly lacks any experiments or analysis on noisy or imbalanced data.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should strengthen the theoretical foundation of their method by providing a more rigorous analysis of the proposed decomposition and its connection to existing theories on gradient dynamics and optimization landscapes. This could involve exploring connections to existing theories on gradient dynamics and optimization landscapes, such as those found in physics and signal processing. The authors should investigate how the proposed method affects the curvature of the loss landscape and whether it leads to flatter minima, which are known to be associated with better generalization. A theoretical analysis of the convergence properties of the proposed method, perhaps using tools from dynamical systems theory, would also be valuable. This would provide a more rigorous understanding of why the method works and under what conditions it is expected to be effective. Furthermore, the authors should consider providing a more detailed explanation of the relationship between the proposed method and existing techniques for controlling the learning rate or momentum, as these methods also aim to influence the speed of parameter updates. Second, to address the assumption that slow-varying components are primarily responsible for generalization, the authors should conduct a more thorough analysis of the interplay between fast and slow components. This could involve visualizing the parameter trajectories in both the fast and slow subspaces and examining how these trajectories evolve during training. The authors should also investigate whether the fast components contribute to generalization in the early stages of training, and how the proposed method affects this contribution. Furthermore, the authors should explore adaptive filtering techniques that can dynamically adjust the weights of the fast and slow components based on the training progress. This could potentially lead to a more robust and effective method for accelerating generalization. The paper should also include a discussion of the limitations of the proposed method, and under what conditions it might not be effective. Third, the experimental evaluation should be expanded to include a wider range of tasks and datasets. This should include tasks with more complex data distributions and higher dimensionality, such as image classification tasks using convolutional neural networks or natural language processing tasks using transformers. The authors should also consider comparing the proposed method with other existing techniques for accelerating generalization, such as early stopping, learning rate scheduling, or regularization techniques. This would provide a more comprehensive evaluation of the proposed method and help to better understand its relative advantages and limitations. The authors should also provide a more detailed analysis of the computational cost of the proposed method, and compare it with the computational cost of other acceleration techniques. Finally, the authors should investigate the impact of noisy or imbalanced training data on the proposed method. This could involve conducting experiments on datasets with varying levels of noise and imbalance, and analyzing how the method's performance is affected. This would provide a more comprehensive evaluation of the proposed method and help to better understand its robustness. In summary, the authors should focus on strengthening the theoretical foundation of their method, analyzing the interplay between fast and slow components, expanding the experimental evaluation to include more complex datasets and tasks, and investigating the impact of data quality on the method's performance. These improvements would significantly enhance the paper's contribution and make it more robust and generalizable.


## Questions:

Several key questions arise from my analysis of this paper. First, how does the proposed method affect the generalization performance when the training data is noisy or imbalanced? The paper does not include experiments or analysis on the robustness of the method to data quality, and it would be valuable to understand how the method performs under these conditions. Second, how does the proposed method affect the generalization performance when the model is overparameterized? While the paper includes experiments on MNIST with a two-layer ReLU-MLP, which has more parameters than the number of training samples, it does not systematically explore the effect of varying degrees of overparameterization. It would be important to understand how the method performs under different levels of overparameterization. Third, how does the proposed method compare with other existing techniques for accelerating generalization, such as early stopping, learning rate scheduling, or regularization techniques? The paper mentions these techniques in the related work section, but it does not provide any empirical comparison. It would be valuable to understand the relative advantages and limitations of the proposed method compared to these other techniques. Fourth, can the proposed method be applied to other optimization algorithms, such as Adam or SGD with momentum? The paper focuses on first-order optimization algorithms, but it would be interesting to explore the applicability of the method to other optimization algorithms. Fifth, how does the proposed method affect the generalization performance when the training data is noisy or imbalanced? This question is related to the first question, but it specifically focuses on the impact of noisy or imbalanced data. Sixth, how does the proposed method affect the generalization performance when the model is overparameterized? This question is related to the second question, but it specifically focuses on the impact of overparameterization. Seventh, how does the proposed method compare with other existing techniques for accelerating generalization, such as early stopping, learning rate scheduling, or regularization techniques? This question is related to the third question, but it specifically focuses on the empirical comparison. Finally, what is the computational cost of the proposed method, and how does it compare with the computational cost of other acceleration techniques? The paper does not provide a detailed analysis of the computational cost of the proposed method, and it would be valuable to understand its practical implications. These questions highlight key uncertainties and areas for further investigation, and they are crucial for understanding the full potential and limitations of the proposed method.


## Rating:

5.5


## Confidence:

3.25


## Decision:

Reject
}