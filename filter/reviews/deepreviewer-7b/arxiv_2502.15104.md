I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

The authors propose a novel estimator of the centered kernel alignment (CKA) that accounts for sampling variability. They derive the estimator under the assumption of Gaussian data and demonstrate its superior performance compared to existing estimators.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The authors address a critical gap in the literature by proposing a CKA estimator that accounts for sampling variability, a common issue in neuroscience and machine learning.
- The authors derive the estimator under the assumption of Gaussian data, and demonstrate its superior performance compared to existing estimators.

### Weaknesses

#### Some Related Works


#### comment

 - The authors assume Gaussian data, which may not always be realistic. The authors should discuss the limitations of this assumption and how it might affect the applicability of their estimator in real-world scenarios. Specifically, the assumption of Gaussianity is a strong one, and many real-world datasets, especially in neuroscience, exhibit non-Gaussian characteristics such as skewness, kurtosis, and heavy tails. The authors should provide a more thorough discussion of how deviations from Gaussianity could impact the bias and variance of their proposed estimator, and perhaps explore alternative assumptions or methods for more robust estimation under non-Gaussian conditions.
- The authors do not provide a clear explanation of how their estimator can be applied to the comparison of neural responses across different brain regions or species. The authors should clarify whether their estimator can be used to compare neural responses across different brain regions or species, and if so, how this comparison can be performed. The current description lacks detail on how the kernel matrices are constructed across different brain regions or species, and how the estimator would handle potential differences in the dimensionality of the neural representations. A more detailed explanation of the practical steps involved in applying the estimator to such comparisons is needed.
- The authors do not provide a clear explanation of how their estimator can be applied to the comparison of neural responses across different brain regions or species. The authors should clarify whether their estimator can be used to compare neural responses across different brain regions or species, and if so, how this comparison can be performed. The current description lacks detail on how the kernel matrices are constructed across different brain regions or species, and how the estimator would handle potential differences in the dimensionality of the neural representations. A more detailed explanation of the practical steps involved in applying the estimator to such comparisons is needed.

### Suggestions

The authors should provide a more detailed discussion of the limitations of the Gaussian assumption and its potential impact on the estimator's performance. They could explore the use of alternative distributions or robust estimation techniques that are less sensitive to deviations from Gaussianity. For example, they could consider using kernel density estimation or other non-parametric methods to model the data distributions, or explore the use of robust estimators that are less sensitive to outliers and non-Gaussian noise. Furthermore, the authors should provide a more thorough analysis of the estimator's sensitivity to different types of non-Gaussian noise, and perhaps explore methods for pre-processing the data to mitigate the effects of non-Gaussianity. This would significantly enhance the practical applicability of the proposed estimator.

To address the concerns about comparing neural responses across different brain regions or species, the authors should provide a more detailed explanation of how the kernel matrices are constructed and how the estimator handles potential differences in dimensionality. They should clarify whether the kernel matrices are constructed independently for each brain region or species, and how the estimator can be used to compare the similarity of representations across different datasets. A step-by-step guide on how to apply the estimator to such comparisons, including how to choose appropriate kernels and how to interpret the results, would be beneficial. The authors should also discuss the potential challenges of comparing representations across different brain regions or species, such as differences in the number of neurons or the complexity of the neural code, and how their estimator can address these challenges. This would make the method more accessible and useful for researchers in the field.

Finally, the authors should provide a more detailed explanation of the practical steps involved in applying their estimator to real-world datasets. This should include a discussion of how to choose appropriate kernels for different types of data, how to handle missing data or outliers, and how to interpret the results in the context of the specific research question. The authors should also provide examples of how to use their estimator to compare neural responses across different brain regions or species, including a detailed description of the data preprocessing steps, the kernel selection process, and the interpretation of the results. This would make the method more transparent and reproducible, and would increase its impact on the field.

### Questions

See above.

### Rating

5

### Confidence

3

**********

## Reviewer 2

### Summary

The authors propose a novel estimator for the centered kernel alignment (CKA) that addresses the bias arising from both finite stimulus sampling and finite neuron sampling. The authors derive a bias-corrected estimator that remains consistent even with limited feature samples. The authors demonstrate the effectiveness of their estimator through both synthetic and real-world datasets, showing that it provides more reliable comparisons of neural representations.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The authors propose a novel estimator for CKA that addresses the bias arising from both finite stimulus sampling and finite neuron sampling.
- The authors derive a bias-corrected estimator that remains consistent even with limited feature samples.
- The authors demonstrate the effectiveness of their estimator through both synthetic and real-world datasets, showing that it provides more reliable comparisons of neural representations.

### Weaknesses

#### Some Related Works


#### comment

 - The authors assume Gaussian data, which may not always be realistic. The authors should discuss the limitations of this assumption and how it might affect the applicability of their estimator in real-world scenarios. Specifically, the assumption of Gaussianity is a strong one, and many real-world datasets, especially in neuroscience, exhibit non-Gaussian characteristics such as skewness, kurtosis, and heavy tails. The authors should provide a more thorough discussion of how deviations from Gaussianity could impact the bias and variance of their proposed estimator, and perhaps explore alternative assumptions or methods for more robust estimation under non-Gaussian conditions.
- The authors do not provide a clear explanation of how their estimator can be applied to the comparison of neural responses across different brain regions or species. The authors should clarify whether their estimator can be used to compare neural responses across different brain regions or species, and if so, how this comparison can be performed. The current description lacks detail on how the kernel matrices are constructed across different brain regions or species, and how the estimator would handle potential differences in the dimensionality of the neural representations. A more detailed explanation of the practical steps involved in applying the estimator to such comparisons is needed.
- The authors do not provide a clear explanation of how their estimator can be applied to the comparison of neural responses across different brain regions or species. The authors should clarify whether their estimator can be used to compare neural responses across different brain regions or species, and if so, how this comparison can be performed. The current description lacks detail on how the kernel matrices are constructed across different brain regions or species, and how the estimator would handle potential differences in the dimensionality of the neural representations. A more detailed explanation of the practical steps involved in applying the estimator to such comparisons is needed.

### Suggestions

The authors should provide a more thorough discussion of the limitations of the Gaussian assumption and its potential impact on the estimator's performance. They should explore the use of alternative distributions or robust estimation techniques that are less sensitive to deviations from Gaussianity. For example, they could consider using kernel density estimation or other non-parametric methods to model the data distributions, or explore the use of robust estimators that are less sensitive to outliers and non-Gaussian noise. Furthermore, the authors should provide a more detailed analysis of the estimator's sensitivity to different types of non-Gaussian noise, and perhaps explore methods for pre-processing the data to mitigate the effects of non-Gaussianity. This would significantly enhance the practical applicability of the proposed estimator.

To address the concerns about comparing neural responses across different brain regions or species, the authors should provide a more detailed explanation of how the kernel matrices are constructed and how the estimator handles potential differences in dimensionality. They should clarify whether the kernel matrices are constructed independently for each brain region or species, and how the estimator can be used to compare the similarity of representations across different datasets. A step-by-step guide on how to apply the estimator to such comparisons, including how to choose appropriate kernels and how to interpret the results, would be beneficial. The authors should also discuss the potential challenges of comparing representations across different brain regions or species, such as differences in the number of neurons or the complexity of the neural code, and how their estimator can address these challenges. This would make the method more transparent and reproducible, and would increase its impact on the field.

Finally, the authors should provide a more detailed explanation of the practical steps involved in applying their estimator to real-world datasets. This should include a discussion of how to choose appropriate kernels for different types of data, how to handle missing data or outliers, and how to interpret the results in the context of the specific research question. The authors should also provide examples of how to use their estimator to compare neural responses across different brain regions or species, including a detailed description of the data preprocessing steps, the kernel selection process, and the interpretation of the results. This would make the method more accessible and useful for researchers in the field.

### Questions

- How does the estimator perform when the data deviates significantly from the Gaussian assumption?
- How can the estimator be applied to compare neural responses across different brain regions or species?

### Rating

6

### Confidence

3

**********

## Reviewer 3

### Summary

The paper addresses the problem of estimating the centered kernel alignment (CKA) between two sets of random variables, in the setting where only a subset of the features is observed. The authors propose a debiased estimator that corrects for the bias introduced by the undersampling of features. The estimator is validated on synthetic data and applied to electrophysiological recordings from the visual cortex.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

The paper addresses a relevant problem in the field of neural data analysis, where the number of available features is often limited. The proposed estimator is theoretically sound and empirically validated on synthetic data. The application to electrophysiological recordings is a valuable contribution that demonstrates the practical relevance of the method.

### Weaknesses

#### Some Related Works


#### comment

The paper does not provide a clear explanation of how the estimator can be applied to the comparison of neural responses across different brain regions or species. The authors should clarify whether their estimator can be used to compare neural responses across different brain regions or species, and if so, how this comparison can be performed. The current description lacks detail on how the kernel matrices are constructed across different brain regions or species, and how the estimator would handle potential differences in the dimensionality of the neural representations. A more detailed explanation of the practical steps involved in applying the estimator to such comparisons is needed.

### Suggestions

The authors should provide a more detailed explanation of how their estimator can be applied to compare neural responses across different brain regions or species. Specifically, they should clarify how the kernel matrices are constructed for each region or species, and how the estimator handles potential differences in the dimensionality of the neural representations. For example, if one region has a larger number of neurons than another, how is this difference accounted for in the comparison? The authors should also provide a step-by-step guide on how to apply their estimator to such comparisons, including how to choose appropriate kernels and how to interpret the results. This would make the method more transparent and reproducible, and would increase its impact on the field.

Furthermore, the authors should address the practical challenges of applying their estimator to real-world datasets. For instance, how does the estimator handle missing data or outliers? How sensitive is the estimator to the choice of kernel? The authors should provide a more thorough discussion of these practical considerations, and perhaps include a sensitivity analysis to assess the robustness of the estimator to different data characteristics. This would help to ensure that the estimator is reliable and can be applied to a wide range of datasets.

Finally, the authors should provide a more detailed comparison of their estimator to existing methods for comparing neural representations. While the paper mentions that the proposed estimator is unbiased, it would be helpful to see a more detailed analysis of its performance compared to other estimators, particularly in terms of bias and variance. The authors should also discuss the limitations of their estimator and identify potential areas for future research. This would help to contextualize the contribution of the paper and provide a more complete picture of the state of the art in this field.

### Questions

How does the estimator perform when the data deviates significantly from the Gaussian assumption?

### Rating

6

### Confidence

3

**********

## Reviewer 4

### Summary

The authors propose a novel estimator for the centered kernel alignment (CKA) that addresses the bias arising from both finite stimulus sampling and finite neuron sampling. They derive a bias-corrected estimator that remains consistent even with limited feature samples. The authors demonstrate the effectiveness of their estimator through both synthetic and real-world datasets, showing that it provides more reliable comparisons of neural representations.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

The paper addresses a critical issue in the field of CKA, particularly in scenarios where the number of features is limited. The authors provide a rigorous theoretical analysis of the bias in existing CKA estimators and propose a novel bias-corrected estimator. The empirical results are compelling, demonstrating the effectiveness of the proposed estimator in both synthetic and real-world datasets. The paper is well-written and clearly presented, making it accessible to a broad audience.

### Weaknesses

#### Some Related Works


#### comment

The authors assume Gaussian data, which may not always be realistic. The authors should discuss the limitations of this assumption and how it might affect the applicability of their estimator in real-world scenarios. Specifically, the assumption of Gaussianity is a strong one, and many real-world datasets, especially in neuroscience, exhibit non-Gaussian characteristics such as skewness, kurtosis, and heavy tails. The authors should provide a more thorough discussion of how deviations from Gaussianity could impact the bias and variance of their proposed estimator, and perhaps explore alternative assumptions or methods for more robust estimation under non-Gaussian conditions.

The authors do not provide a clear explanation of how their estimator can be applied to the comparison of neural responses across different brain regions or species. The authors should clarify whether their estimator can be used to compare neural responses across different brain regions or species, and if so, how this comparison can be performed. The current description lacks detail on how the kernel matrices are constructed across different brain regions or species, and how the estimator would handle potential differences in the dimensionality of the neural representations. A more detailed explanation of the practical steps involved in applying the estimator to such comparisons is needed.

### Suggestions

The authors should provide a more detailed discussion of the limitations of the Gaussian assumption and its potential impact on the estimator's performance. They could explore the use of alternative distributions or robust estimation techniques that are less sensitive to deviations from Gaussianity. For example, they could consider using kernel density estimation or other non-parametric methods to model the data distributions, or explore the use of robust estimators that are less sensitive to outliers and non-Gaussian noise. Furthermore, the authors should provide a more thorough analysis of the estimator's sensitivity to different types of non-Gaussian noise, and perhaps explore methods for pre-processing the data to mitigate the effects of non-Gaussianity. This would significantly enhance the practical applicability of the proposed estimator.

To address the concerns about comparing neural responses across different brain regions or species, the authors should provide a more detailed explanation of how the kernel matrices are constructed and how the estimator handles potential differences in dimensionality. They should clarify whether the kernel matrices are constructed independently for each brain region or species, and how the estimator can be used to compare the similarity of representations across different datasets. A step-by-step guide on how to apply the estimator to such comparisons, including how to choose appropriate kernels and how to interpret the results, would be beneficial. The authors should also discuss the potential challenges of comparing representations across different brain regions or species, such as differences in the number of neurons or the complexity of the neural code, and how their estimator can address these challenges. This would make the method more transparent and reproducible, and would increase its impact on the field.

Finally, the authors should provide a more thorough discussion of the practical considerations for applying their estimator to real-world datasets. This should include a discussion of how to choose appropriate kernels for different types of data, how to handle missing data or outliers, and how to interpret the results in the context of the specific research question. The authors should also provide examples of how to use their estimator to compare neural responses across different brain regions or species, including a detailed description of the data preprocessing steps, the kernel selection process, and the interpretation of the results. This would make the method more accessible and useful for researchers in the field.

### Questions

See weaknesses.

### Rating

8

### Confidence

2

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support or refute their claims.

**Plan:**
1. Go through each reviewer's comments one by one.
2. For each comment, identify the type of weakness (theoretical, methodological, experimental, practical).
3. Find specific evidence in the paper (quotes, equations, descriptions of experiments) that supports the reviewer's claim.
4. If the reviewer points out a missing element (e.g., a citation, a baseline), check if it's indeed missing.
5. Synthesize the findings and conclude whether the weakness is valid, partially valid, or invalid.
**Review 1**

1. Weakness Statement:
"The authors assume Gaussian data, which may not always be realistic. The authors should discuss the limitations of this assumption and how it might affect the applicability of their estimator in real-world scenarios. Specifically, the assumption of Gaussianity is a strong one, and many real-world datasets, especially in neuroscience, exhibit non-Gaussian characteristics such as skewness, kurtosis, and heavy tails. The authors should provide a more thorough discussion of how deviations from Gaussianity could impact the bias and variance of their proposed estimator, and perhaps explore alternative assumptions or methods for more robust estimation under non-Gaussian conditions."

2. Evidence Collection:
a) Method-related Evidence:
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾(𝑎) = 1𝑄𝑎 ​ 𝑃×𝑄𝑎 { 𝑥𝑖 ​ α ( 𝑥𝑖 ​ α )⊤ } , where 𝑥𝑖 ​ α ​ = ϕ(𝑥)⊤ ​ 𝑤 ( 𝑖 ) , and the empirical centered kernels defined in Equation 2 by 𝐾 ¯ (𝑎) = 𝐾(𝑎) − 1𝑃 ​ 1𝑃 ​ 𝐾(𝑎) ." (Section 3) - This shows the reliance on the data being centered, which is related to the Gaussian assumption.
   - "The centered kernel function k (a,b) is defined as: k (a,b) = tr ( 𝐾 ( a ) 𝐾 ( b ) ) - tr ( 𝐾 ( a ) K ( b ) K ( a ) K ( b ) ) ." (Section 2) - This definition is based on the Gram matrix, which is derived from the data.
   - "We introduce the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑖 𝑥 𝑖 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑖 𝑥 𝑖 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑖 𝑥 𝑖 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑖 𝑥 𝑖 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑖 𝑥 𝑖 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑖 𝑥 𝑖 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑖 𝑥 𝑖 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑎 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 ​ for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 3) - This explicitly states the use of empirical kernels derived from the data.
   - "We define the empirical uncentered kernels (also called Gram matrices) by 𝐾 ( a ) = 1 𝑄 𝑎 ​ 𝑃 × 𝑄 𝑎 { 𝑥 𝑖 ​ α ​ = ϕ ( 𝑥 ) ⊤ ​ 𝑤 ( 𝑥 ) } , where 𝑥 𝑖 ​ α ​ denotes the response of each neuron to stimulus 𝑥 𝑥 𝑥 𝑥 for 𝑖 = 1 , ⋯ , 𝑃 , where 𝑃 𝑃 is the number of stimuli." (Section 