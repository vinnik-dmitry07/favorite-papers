I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

The authors propose a new test for comparing two brain dissimilarity matrices. They derive the analytical expression of the variance of the estimated dissimilarity matrices, and use this to derive a new test based on whitening.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

The paper is clearly written and the problem is well motivated. The proposed test seems to perform well in simulations.

### Weaknesses

#### Some Related Works


#### comment

I have no strong objections to the paper, but I think it would be stronger if the authors could provide more justification for the use of whitening. The authors mention that their test is invariant to linear transformations of the dissimilarity matrices, but it would be helpful to elaborate on why this is a desirable property. Specifically, what types of linear transformations are being considered, and why is invariance under these transformations important for the validity or power of the test? It would also be helpful to clarify how the proposed whitening approach compares to other existing methods for handling correlated data in dissimilarity matrix analysis, and what specific advantages it offers over these alternatives.

### Suggestions

To strengthen the paper, the authors should provide a more detailed explanation of the theoretical underpinnings of their whitening approach. This should include a discussion of the assumptions made about the data generating process and how these assumptions relate to the choice of whitening transformation. For example, if the dissimilarity matrices are assumed to be derived from underlying latent variables with a specific covariance structure, this should be explicitly stated and justified. Furthermore, the authors should elaborate on the practical implications of their theoretical results. How does the derived analytical expression for the variance of the estimated dissimilarity matrices translate into a more intuitive understanding of the test's behavior? It would be beneficial to include a concrete example, perhaps using a simplified model, to illustrate how the whitening transformation affects the dissimilarity matrices and why this is beneficial for statistical inference. This would help to bridge the gap between the theoretical derivations and the practical application of the proposed test.

In addition to clarifying the theoretical aspects, the authors should also expand on the practical considerations for applying their test. What are the computational costs associated with the whitening transformation, and how does this scale with the size of the dissimilarity matrices? Are there any specific software packages or libraries that can be used to implement the proposed test? It would also be helpful to discuss the limitations of the proposed approach. For example, under what conditions might the whitening transformation be less effective, or when might alternative methods be more appropriate? Addressing these practical and theoretical limitations would make the paper more robust and useful for a wider audience. Furthermore, a more thorough comparison with existing methods for comparing dissimilarity matrices is needed. The authors should not only compare their method in terms of power and Type I error, but also discuss the computational efficiency and ease of implementation of their approach relative to other methods. This would help to position the proposed method within the broader landscape of dissimilarity matrix analysis.

Finally, the authors should consider including a more detailed discussion of the interpretation of the results obtained using their test. What does a significant test result actually tell us about the underlying neural representations? How should the results be visualized and communicated? Providing concrete examples of how to interpret the results in the context of specific neuroscience research would greatly enhance the practical value of the paper. For instance, if the test is used to compare the representational dissimilarity matrices of different brain regions, how should the differences be interpreted in terms of functional specialization or information processing? This would help to make the paper more accessible to researchers who are not experts in statistical methods for comparing dissimilarity matrices.

### Questions

See above.

### Rating

6

### Confidence

4

**********

## Reviewer 2

### Summary

This paper presents a new test for comparing two brain dissimilarity matrices. The authors derive the analytical expression of the variance of the estimated dissimilarity matrices, and use this to derive a new test based on whitening. They show that this test is invariant to linear transformations of the dissimilarity matrices, and that it performs close to the theoretical optimum, as achieved with the likelihood-ratio test implemented by PCM.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

The paper is well written and the problem is well motivated. The proposed test seems to perform well in simulations.

### Weaknesses

#### Some Related Works


#### comment

I have no strong objections to the paper, but I think it would be stronger if the authors could provide more justification for the use of whitening. The authors mention that their test is invariant to linear transformations of the dissimilarity matrices, but it would be helpful to elaborate on why this is a desirable property. Specifically, what types of linear transformations are being considered, and why is invariance under these transformations important for the validity or power of the test? It would also be helpful to clarify how the proposed whitening approach compares to other existing methods for handling correlated data in dissimilarity matrix analysis, and what specific advantages it offers over these alternatives.

### Suggestions

To strengthen the paper, the authors should provide a more detailed explanation of the theoretical underpinnings of their whitening approach. This should include a discussion of the assumptions made about the data generating process and how these assumptions relate to the choice of whitening transformation. For example, if the dissimilarity matrices are assumed to be derived from underlying latent variables with a specific covariance structure, this should be explicitly stated and justified. Furthermore, the authors should elaborate on the practical implications of their theoretical results. How does the derived analytical expression for the variance of the estimated dissimilarity matrices translate into a more intuitive understanding of the test's behavior? It would be beneficial to include a concrete example, perhaps using a simplified model, to illustrate how the whitening transformation affects the dissimilarity matrices and why this is beneficial for statistical inference. This would help to bridge the gap between the theoretical derivations and the practical application of the proposed test.

In addition to clarifying the theoretical aspects, the authors should also expand on the practical considerations for applying their test. What are the computational costs associated with the whitening transformation, and how does this scale with the size of the dissimilarity matrices? Are there any specific software packages or libraries that can be used to implement the proposed test? It would also be helpful to discuss the limitations of the proposed approach. For example, under what conditions might the whitening transformation be less effective, or when might alternative methods be more appropriate? Addressing these practical and theoretical limitations would make the paper more robust and useful for a wider audience. Furthermore, a more thorough comparison with existing methods for comparing dissimilarity matrices is needed. The authors should not only compare their method in terms of power and Type I error, but also discuss the computational efficiency and ease of implementation of their approach relative to other methods. This would help to position the proposed method within the broader landscape of dissimilarity matrix analysis.

Finally, the authors should consider including a more detailed discussion of the interpretation of the results obtained using their test. What does a significant test result actually tell us about the underlying neural representations? How should the results be visualized and communicated? Providing concrete examples of how to interpret the results in the context of specific neuroscience research would greatly enhance the practical value of the paper. For instance, if the test is used to compare the representational dissimilarity matrices of different brain regions, how should the differences be interpreted in terms of functional specialization or information processing? This would help to make the paper more accessible to researchers who are not experts in statistical methods for comparing dissimilarity matrices.

### Questions

See above.

### Rating

8

### Confidence

3

**********

## Reviewer 3

### Summary

This paper addresses two main issues in RSA: the bias in distance estimates and the correlated dissimilarity estimates. The authors derive the analytical expressions for the mean and variance of both biased and unbiased distance estimates. They also demonstrate that the covariance of dissimilarity estimates can be effectively utilized to enhance model selection in RSA. The authors propose a new criterion called the whitened unbiased RDM cosine similarity (WUC), which is invariant to linear transformations of the dissimilarity matrices and achieves near-optimal model selection performance. The authors validate their approach through simulations and real data applications, demonstrating its effectiveness in improving model selection accuracy compared to existing methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-organized and clearly written, making it easy to follow and understand the methodology and results.
2. The authors provide a thorough theoretical analysis of the bias and variance of distance estimates in RSA, which is a significant contribution to the field.
3. The proposed WUC criterion is novel and addresses the limitations of existing methods by accounting for the covariance structure of dissimilarity estimates.
4. The authors validate their approach through extensive simulations and real data applications, demonstrating its effectiveness in improving model selection accuracy.

### Weaknesses

#### Some Related Works


#### comment

1. The paper assumes that the measurement noise is i.i.d. across conditions, which may not always be the case in real-world scenarios. The authors should discuss the potential impact of non-i.i.d. noise on their results and consider how their method might be adapted to handle such cases. Specifically, the assumption of independence is crucial for the derived analytical expressions, and deviations from this assumption could lead to inaccurate variance estimates and suboptimal model selection. For example, if measurements within a condition are correlated, the effective number of independent samples would be reduced, potentially leading to an underestimation of the true variance. Furthermore, if the noise variance varies across conditions, the derived expressions would not be directly applicable, and a more sophisticated approach would be needed to account for this heteroscedasticity.
2. While the authors claim that the WUC criterion is invariant to linear transformations of the dissimilarity matrices, they do not provide a formal proof of this property. A more rigorous mathematical demonstration would strengthen the theoretical foundation of their method. The invariance should be shown explicitly, demonstrating that the WUC value remains unchanged under any linear transformation of the dissimilarity matrix. This could involve showing that the transformation matrix cancels out in the numerator and denominator of the WUC formula, or that the transformation preserves the cosine similarity between the vectors of dissimilarity estimates. Without a formal proof, the claim of invariance remains somewhat intuitive and lacks the necessary mathematical rigor.

### Suggestions

The authors should consider expanding their discussion on the limitations of the i.i.d. noise assumption. They could explore the use of robust statistical methods that are less sensitive to deviations from this assumption. For instance, they could investigate the use of sandwich estimators or other robust variance estimators that can account for heteroscedasticity and autocorrelation in the noise. Furthermore, they could consider a simulation study that explicitly examines the performance of their method under various non-i.i.d. noise conditions, such as correlated noise or heteroscedastic noise. This would provide a more comprehensive understanding of the robustness of their approach and identify potential areas for improvement. The authors could also explore the use of pre-whitening techniques to transform the data into a space where the noise is approximately i.i.d., before applying their method. This could involve estimating the noise covariance matrix and using it to transform the data, thereby mitigating the impact of non-i.i.d. noise.

To strengthen the theoretical foundation of their method, the authors should provide a formal mathematical proof of the invariance of the WUC criterion under linear transformations. This proof should clearly demonstrate that the WUC value remains unchanged when the dissimilarity matrix is transformed by any invertible linear transformation. The proof should explicitly show how the transformation matrix cancels out in the numerator and denominator of the WUC formula, or how the transformation preserves the cosine similarity between the vectors of dissimilarity estimates. This would provide a more rigorous justification for the use of the WUC criterion and enhance the credibility of their method. The authors could also discuss the implications of this invariance property for the interpretation of the results. For example, they could explain how the invariance ensures that the WUC criterion provides a consistent measure of model fit, regardless of the specific linear transformation applied to the dissimilarity matrix.

Finally, the authors should consider providing more practical guidance on how to choose the number of partitions (M) in their simulations. While they mention that the method is robust to the choice of M, they do not provide specific recommendations for selecting an appropriate value. They could explore the relationship between the number of partitions and the accuracy of their method, and provide guidelines for choosing M based on the characteristics of the data. For example, they could investigate the impact of the number of partitions on the variance of the distance estimates and the power of the model selection criterion. This would provide valuable practical guidance for researchers who want to apply their method to their own data. Furthermore, they could explore the use of cross-validation techniques to select the optimal number of partitions, which could further improve the robustness of their method.

### Questions

1. How does the proposed method handle non-i.i.d. measurement noise, and what are the potential implications for the results?
2. Could the authors provide a formal proof of the invariance of the WUC criterion under linear transformations of the dissimilarity matrices?
3. How should the number of partitions (M) be chosen in the simulations, and what is the impact of this choice on the accuracy of the method?

### Rating

8

### Confidence

3

**********

## Reviewer 4

### Summary

The paper addresses two main issues in RSA: the bias in distance estimates and the correlated dissimilarity estimates. The authors derive the analytical expressions for the mean and variance of both biased and unbiased distance estimates. They also demonstrate that the covariance of dissimilarity estimates can be effectively utilized to enhance model selection in RSA. The authors propose a new criterion called the whitened unbiased RDM cosine similarity (WUC), which is invariant to linear transformations of the dissimilarity matrices and achieves near-optimal model selection performance. The authors validate their approach through simulations and real data applications, demonstrating its effectiveness in improving model selection accuracy compared to existing methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

The paper is well-organized and clearly written, making it easy to follow and understand the methodology and results. The authors provide a thorough theoretical analysis of the bias and variance of distance estimates in RSA, which is a significant contribution to the field. The proposed WUC criterion is novel and addresses the limitations of existing methods by accounting for the covariance structure of dissimilarity estimates. The authors validate their approach through extensive simulations and real data applications, demonstrating its effectiveness in improving model selection accuracy compared to existing methods.

### Weaknesses

#### Some Related Works


#### comment

The paper assumes that the measurement noise is i.i.d. across conditions, which may not always be the case in real-world scenarios. The authors should discuss the potential impact of non-i.i.d. noise on their results and consider how their method might be adapted to handle such cases. Specifically, the assumption of independence is crucial for the derived analytical expressions, and deviations from this assumption could lead to inaccurate variance estimates and suboptimal model selection. For example, if measurements within a condition are correlated, the effective number of independent samples would be reduced, potentially leading to an underestimation of the true variance. Furthermore, if the noise variance varies across conditions, the derived expressions would not be directly applicable, and a more sophisticated approach would be needed to account for this heteroscedasticity.

### Suggestions

The authors should consider expanding their discussion on the limitations of the i.i.d. noise assumption. They could explore the use of robust statistical methods that are less sensitive to deviations from this assumption. For instance, they could investigate the use of sandwich estimators or other robust variance estimators that can account for heteroscedasticity and autocorrelation in the noise. Furthermore, they could consider a simulation study that explicitly examines the performance of their method under various non-i.i.d. noise conditions, such as correlated noise or heteroscedastic noise. This would provide a more comprehensive understanding of the robustness of their approach and identify potential areas for improvement. The authors could also explore the use of pre-whitening techniques to transform the data into a space where the noise is approximately i.i.d., before applying their method. This could involve estimating the noise covariance matrix and using it to transform the data, thereby mitigating the impact of non-i.i.d. noise.

To strengthen the theoretical foundation of their method, the authors should provide a formal mathematical proof of the invariance of the WUC criterion under linear transformations of the dissimilarity matrices. This proof should clearly demonstrate that the WUC value remains unchanged when the dissimilarity matrix is transformed by any invertible linear transformation. The proof should explicitly show how the transformation matrix cancels out in the numerator and denominator of the WUC formula, or how the transformation preserves the cosine similarity between the vectors of dissimilarity estimates. This would provide a more rigorous justification for the use of the WUC criterion and enhance the credibility of their method. The authors could also discuss the implications of this invariance property for the interpretation of the results. For example, they could explain how the invariance ensures that the WUC criterion provides a consistent measure of model fit, regardless of the specific linear transformation applied to the dissimilarity matrix.

Finally, the authors should consider providing more practical guidance on how to choose the number of partitions (M) in their simulations. While they mention that the method is robust to the choice of M, they do not provide specific recommendations for selecting an appropriate value. They could explore the relationship between the number of partitions and the accuracy of their method, and provide guidelines for choosing M based on the characteristics of the data. For example, they could investigate the impact of the number of partitions on the variance of the distance estimates and the power of the model selection criterion. This would provide valuable practical guidance for researchers who want to apply their method to their own data. Furthermore, they could explore the use of cross-validation techniques to select the optimal number of partitions, which could further improve the robustness of their method.

### Questions

How does the proposed method handle non-i.i.d. measurement noise, and what are the potential implications for the results?

### Rating

8

### Confidence

3

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers in a given paper. I need to go through each reviewer's comments and check if the criticism is valid based on the content of the paper.

Here's my plan:
1. **Parse the paper content:** Understand the methodology, experiments, and results.
2. **Go through each reviewer's comments:**
   - Identify the specific weakness mentioned.
   - Search for evidence in the paper to support or refute the weakness.
   - Categorize the weakness (theoretical, methodological, experimental, practical).
   - Provide quotes and section references as evidence.
   - Assess the validity of the weakness.
3. **Synthesize the findings:** Look for overlapping criticisms and any conflicting opinions.
**Review 1 Weaknesses:**

1. Weakness Statement:
"I have no strong objections to the paper, but I think it would be stronger if the authors could provide more justification for the use of whitening. The authors mention that their test is invariant to linear transformations of the dissimilarity matrices, but it would be helpful to elaborate on why this is a desirable property. Specifically, what types of linear transformations are being considered, and why is invariance under these transformations important for the validity or power of the test? It would also be helpful to clarify how the proposed whitening approach compares to other existing methods for handling correlated data in dissimilarity matrix analysis, and what specific advantages it offers over these alternatives."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper introduces whitening in the " Whitened Unbiased RDM Cosine Similarity (WUC)" section.
   - Quote: "Specifically, we suggest using the covariance structure of the distances under the assumption that all distances are zero. In this case the variance simplifies to
   Var ⁡ ( d ~ ) = c ⁡ ( 𝚵 ∘ 𝚵 ) = c ​ 𝚅 , where c c is a proportionality constant that is not important for most applications. Note that noise correlations between different channels (or voxels in fMRI) would only influence c c , but not 𝚅 . Thus, the whitened RDM cosine similarity is related to the RV coefficient [ 11 ] , which is also known as the linear Centered Kernel Alignment (CKA, [ 12 ] )."
   - Quote: "To improve model inference, we should therefore use the covariance matrix to transform the elements of the RDM into a whitened space, in which all dimensions are measured independently and with the same variance. Originally [ 19 ] , we had suggested using the full expression for the covariance (Eq. 29 ), and to take this covariance matrix into account for model comparison, we can pre-multiply them with 𝐕 − 1 2 ."
   - The paper mentions invariance in the " Whitened Unbiased RDM Cosine Similarity (WUC)" section.
   - Quote: "The whitened unbiased RDM cosine similarity is related to the linear Centered Kernel Alignment (CKA, [ 12 ] ), but extends this to incorporate a whitened version of the dissimilarity estimates. The linear CKA is a normalized version of the Hilbert-Schmidt independence criterion (HSIC [ 24 ] ) between two sets of multivariate patterns. Here we have the special linear case, where the similarity is calculated between the elements of the two pattern vectors (see methods):"
   - The paper compares against PCM in the " Inference of the WUC" section.
   - Quote: "In addition to the RSA-based methods, we also used Pattern Component Modeling (PCM) [ 14 , 19 ] , which directly compares the marginal likelihood of the data given the models, under the assumption that both signal and noise are normally distributed. For such data, PCM implements the likelihood-ratio test between models. For the case of our simulations, where all assumptions hold, PCM therefore implements the optimal inference procedure [ 13 ] and provides an upper performance bound for any model-comparison technique."

3. Literature Gap Analysis:
   - The paper cites the original CKA paper [12] and the PCM paper [14, 19].

4. Validation Analysis:
   - The reviewer correctly points out the lack of explicit justification for the use of whitening beyond its connection to CKA. While the paper mentions the goal of transforming to a whitened space with independent and identically distributed dimensions, it doesn't elaborate on *why* this is a desirable property in the context of RSA model comparison.
   - The paper does explain the invariance property but doesn't explicitly detail the types of linear transformations considered or why invariance is important.
   - The paper compares against PCM, which is a method that handles correlated data, but doesn't provide a detailed comparison of the whitening approach's specific advantages over other methods for handling correlated data in RSA.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper describes the whitening process and its connection to CKA but lacks a deeper explanation of the rationale behind it and a detailed comparison with other methods for handling correlated data.

**Review 2 Weaknesses:**

1. Weakness Statement:
"The paper assumes that the measurement noise is i.i.d. across conditions, which may not always be the case in real-world scenarios. The authors should discuss the potential impact of non-i.i.d. noise on their results and consider how their method might be adapted to handle such cases. Specifically, the assumption of independence is crucial for the derived analytical expressions, and deviations from this assumption could lead to inaccurate variance estimates and suboptimal model selection. For example, if measurements within a condition are correlated, the effective number of independent samples would be reduced, potentially leading to an underestimation of the true variance. Furthermore, if the noise variance varies across conditions, the derived expressions would not be directly applicable, and a more sophisticated approach would be needed to account for this heteroscedasticity."

2. Evidence Collection:
a) Method-related Evidence:
   - The paper explicitly states the assumption of i.i.d. noise in the "Bias and variance of distance estimates" section.
   - Quote: "In an experiment with K conditions, we have a total of K ⁡ ( K − 1 ) / 2 ≡ D unique pairwise distances."
   - Quote: "The measurement errors can come from any distribution. Across the different partitions, the measured activity patterns are assumed to have covariance 𝚆 K ( 𝜋 ) between conditions, and a covariance 𝚀 𝜋 ( 𝐁 ) would only influence c 𝜋 ."
   - The derivation of the variance in equations (7), (10), (13), and (17) relies on the i.i.d. noise assumption.

3. Literature Gap Analysis:
   - The paper does not cite literature that specifically addresses the impact of non-i.i.d. noise in RSA or methods to handle it.

4. Validation Analysis:
   - The reviewer correctly identifies the strong assumption of i.i.d. noise as a potential limitation.
   - The paper's derivations and the WUC formula are based on this assumption.
   - The reviewer's explanation of the potential impact of correlated noise (reduced effective sample size) and heteroscedastic noise (inapplicable derived expressions) is accurate.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: The paper explicitly states the i.i.d. noise assumption, and the mathematical derivations rely on this assumption, making the reviewer's concerns about the impact of non-i.i.d. noise valid.

**Review 3 Weaknesses:**

1. Weakness Statement:
"The paper assumes that the measurement noise is i.i.d. across conditions, which may not always be the case in real-world scenarios. The authors should discuss the potential impact of non-i.i.d. noise on their results and consider how their method might be adapted to handle such cases. Specifically, the assumption of independence is crucial for the derived analytical expressions, and deviations from this assumption could lead to inaccurate variance estimates and suboptimal model selection. For example, if measurements within a condition are correlated, the effective number of independent samples would be reduced, potentially leading to an underestimation of the true variance. Furthermore, if the noise variance varies across conditions, the derived expressions would not be directly applicable, and a more sophisticated approach would be needed to account for this heteroscedasticity."

2. Evidence Collection:
   - This is the same weakness identified by Reviewer 2. Please see the validation for Reviewer 2's first weakness.

3. Literature Gap Analysis:
   - Same as Reviewer 2.

4. Validation Analysis:
   - Same as Reviewer 2.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 2.

**Review 4 Weaknesses:**

1. Weakness Statement:
"The paper assumes that the measurement noise is i.i.d. across conditions, which may not always be the case in real-world scenarios. The authors should discuss the potential impact of non-i.i.d. noise on their results and consider how their method might be adapted to handle such cases. Specifically, the assumption of independence is crucial for the derived analytical expressions, and deviations from this assumption could lead to inaccurate variance estimates and suboptimal model selection. For example, if measurements within a condition are correlated, the effective number of independent samples would be reduced, potentially leading to an underestimation of the true variance. Furthermore, if the noise variance varies across conditions, the derived expressions would not be directly applicable, and a more sophisticated approach would be needed to account for this heteroscedasticity."

2. Evidence Collection:
   - This is the same weakness identified by Reviewer 2 and Reviewer 3. Please see the validation for Reviewer 2's first weakness.

3. Literature Gap Analysis:
   - Same as Reviewer 2.

4. Validation Analysis:
   - Same as Reviewer 2.

5. Conclusion:
   - Validity status: Valid
   - Confidence level: High
   - Key supporting evidence: Same as Reviewer 2.

**Synthesis and Reflection:**

All reviewers who raised concerns about the i.i.d. noise assumption identified the same fundamental weakness in the paper. They correctly point out that this is a strong assumption that might not hold in real-world scenarios and could lead to inaccurate results. The reviewers also suggest exploring the impact of non-i.i.d. noise and potential adaptations to the method. Reviewer 1 asks for more justification of the whitening approach, which is a valid point as the paper could elaborate more on the theoretical benefits and comparisons to other methods. Reviewer 2 asks for a formal proof of invariance, which is a standard expectation for theoretical contributions. Reviewer 3 asks for more practical guidance on choosing the number of partitions, which is a practical consideration for implementation.

There are no conflicting opinions among the reviewers regarding the identified weaknesses. The criticisms are consistent and focus on the limitations of the i.i.d. noise assumption and the need for more justification and practical guidance.

**Final Conclusion:**

All identified weaknesses are valid and well-supported by the paper's content. The primary concerns revolve around the i.i.d. noise assumption, the need for more justification of the whitening approach, the lack of a formal proof of invariance, and the need for more practical guidance on parameter selection.
}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper addresses a critical issue in Representational Similarity Analysis (RSA), specifically the bias and correlation in distance estimates, which can significantly impact the accuracy of model selection. The authors derive the analytical expressions for the mean and variance of both biased and unbiased distance estimates, demonstrating that the covariance of dissimilarity estimates can be effectively utilized to enhance model selection in RSA. They propose a new criterion called the whitened unbiased RDM cosine similarity (WUC), which is invariant to linear transformations of the dissimilarity matrices and achieves near-optimal model selection performance. The paper is well-organized and clearly written, making it accessible to both theoretical and applied researchers in the field. The authors validate their approach through extensive simulations and real data applications, showing its effectiveness in improving model selection accuracy compared to existing methods. However, the paper's strong assumption of independent and identically distributed (i.i.d.) noise across conditions is a significant limitation, and the justification for the whitening approach could be more detailed. Additionally, the paper could benefit from a formal proof of the invariance of the WUC criterion and more practical guidance on choosing the number of partitions in simulations.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

3.0


## Strengths:

The paper is well-organized and clearly written, which greatly enhances its readability and accessibility. The problem it addresses is well-motivated, and the proposed solution is both innovative and theoretically sound. The authors provide a thorough theoretical analysis of the bias and variance of distance estimates in RSA, which is a significant contribution to the field. The derived analytical expressions for the mean and variance of biased and unbiased distance estimates are novel and offer a deeper understanding of the statistical properties of RSA dissimilarity measures. The whitened unbiased RDM cosine similarity (WUC) criterion is a key innovation, as it is invariant to linear transformations of the dissimilarity matrices, a property that is particularly useful in RSA model comparison. The authors also validate their approach through extensive simulations and real data applications, demonstrating its effectiveness in improving model selection accuracy. The paper's clear and concise writing style, along with its well-structured sections, makes it a valuable resource for researchers interested in advancing the methodology of RSA. The authors' attention to detail in the derivations and their thorough validation of the WUC criterion are commendable and provide a solid foundation for future research in this area.


## Weaknesses:

One of the most significant limitations of the paper is the assumption that the measurement noise is i.i.d. across conditions. This assumption is crucial for the derived analytical expressions, and its violation could lead to inaccurate variance estimates and suboptimal model selection. The paper does not discuss the potential impact of non-i.i.d. noise, such as correlated noise within a condition or heteroscedastic noise across conditions, which are common in real-world scenarios. For instance, if measurements within a condition are correlated, the effective number of independent samples would be reduced, potentially leading to an underestimation of the true variance. Similarly, if the noise variance varies across conditions, the derived expressions would not be directly applicable, and a more sophisticated approach would be needed to account for this heteroscedasticity. This limitation is particularly concerning because it affects the robustness and generalizability of the proposed method. The authors should explore the use of robust statistical methods, such as sandwich estimators or other robust variance estimators, to handle these cases. Additionally, a simulation study that explicitly examines the performance of the method under various non-i.i.d. noise conditions would provide a more comprehensive understanding of its limitations and strengths (confidence level: high, key supporting evidence: explicit assumption of i.i.d. noise in the 'Bias and variance of distance estimates' section and the reliance on this assumption in the derived variance formulas).

Another area where the paper could be strengthened is the justification for the use of whitening. While the authors mention that their test is invariant to linear transformations of the dissimilarity matrices, they do not provide a detailed explanation of why this is a desirable property. Specifically, the paper could elaborate on the types of linear transformations being considered and why invariance under these transformations is important for the validity or power of the test. The whitening approach is presented as a way to handle correlated data, but the paper does not clarify how the proposed whitening approach compares to other existing methods for handling correlated data in dissimilarity matrix analysis, such as methods that use regularization or dimensionality reduction techniques. A more thorough comparison with these alternatives would help to position the proposed method within the broader landscape of dissimilarity matrix analysis and highlight its unique advantages (confidence level: high, key supporting evidence: the paper's brief mention of invariance and the lack of detailed comparison with other methods).

Finally, the paper could benefit from a formal mathematical proof of the invariance of the WUC criterion under linear transformations of the dissimilarity matrices. The authors state that the WUC is invariant, but a rigorous proof would strengthen the theoretical foundation of their method. This proof should clearly demonstrate that the WUC value remains unchanged when the dissimilarity matrix is transformed by any invertible linear transformation. The proof should explicitly show how the transformation matrix cancels out in the numerator and denominator of the WUC formula, or how the transformation preserves the cosine similarity between the vectors of dissimilarity estimates. Without a formal proof, the claim of invariance remains somewhat intuitive and lacks the necessary mathematical rigor (confidence level: high, key supporting evidence: the paper's statement of invariance without a formal proof).


## Suggestions:

To address the limitations of the i.i.d. noise assumption, the authors should consider expanding their discussion to include the potential impact of non-i.i.d. noise on their results. They could explore the use of robust statistical methods, such as sandwich estimators or other robust variance estimators, that are less sensitive to deviations from the i.i.d. assumption. For instance, they could investigate the use of cluster-robust standard errors or other techniques that account for correlated noise within a condition. A simulation study that explicitly examines the performance of their method under various non-i.i.d. noise conditions, such as correlated noise or heteroscedastic noise, would provide a more comprehensive understanding of the robustness of their approach and identify potential areas for improvement. The authors could also explore the use of pre-whitening techniques to transform the data into a space where the noise is approximately i.i.d., before applying their method. This could involve estimating the noise covariance matrix and using it to transform the data, thereby mitigating the impact of non-i.i.d. noise (confidence level: high, key supporting evidence: the explicit assumption of i.i.d. noise and the need for more robust methods in real-world scenarios).

To strengthen the justification for the whitening approach, the authors should provide a more detailed explanation of the theoretical underpinnings of their method. This should include a discussion of the assumptions made about the data generating process and how these assumptions relate to the choice of whitening transformation. For example, if the dissimilarity matrices are assumed to be derived from underlying latent variables with a specific covariance structure, this should be explicitly stated and justified. The authors should also elaborate on the practical implications of their theoretical results, such as how the derived analytical expressions translate into a more intuitive understanding of the test's behavior. This would help to bridge the gap between the theoretical derivations and the practical application of the proposed test. Additionally, a concrete example, perhaps using a simplified model, to illustrate how the whitening transformation affects the dissimilarity matrices and why this is beneficial for statistical inference would be valuable (confidence level: high, key supporting evidence: the need for more detailed justification of the whitening approach).

In addition to clarifying the theoretical aspects, the authors should also expand on the practical considerations for applying their test. What are the computational costs associated with the whitening transformation, and how does this scale with the size of the dissimilarity matrices? Are there any specific software packages or libraries that can be used to implement the proposed test? It would also be helpful to discuss the limitations of the proposed approach. For example, under what conditions might the whitening transformation be less effective, or when might alternative methods be more appropriate? Addressing these practical and theoretical limitations would make the paper more robust and useful for a wider audience. Furthermore, a more thorough comparison with existing methods for comparing dissimilarity matrices is needed. The authors should not only compare their method in terms of power and Type I error but also discuss the computational efficiency and ease of implementation of their approach relative to other methods. This would help to position the proposed method within the broader landscape of dissimilarity matrix analysis (confidence level: high, key supporting evidence: the need for more practical guidance and a broader comparison with existing methods).

Finally, the authors should consider providing more practical guidance on how to choose the number of partitions (M) in their simulations. While they mention that the method is robust to the choice of M, they do not provide specific recommendations for selecting an appropriate value. They could explore the relationship between the number of partitions and the accuracy of their method, and provide guidelines for choosing M based on the characteristics of the data. For example, they could investigate the impact of the number of partitions on the variance of the distance estimates and the power of the model selection criterion. This would provide valuable practical guidance for researchers who want to apply their method to their own data. Furthermore, they could explore the use of cross-validation techniques to select the optimal number of partitions, which could further improve the robustness of their method (confidence level: high, key supporting evidence: the lack of specific guidance on choosing M and the potential for improvement using cross-validation).


## Questions:

1. How does the proposed method handle non-i.i.d. measurement noise, and what are the potential implications for the results? Specifically, if measurements within a condition are correlated, how does the method account for this, and what is the impact on the variance estimates and model selection accuracy?

2. Could the authors provide a formal mathematical proof of the invariance of the WUC criterion under linear transformations of the dissimilarity matrices? This proof should clearly demonstrate that the WUC value remains unchanged when the dissimilarity matrix is transformed by any invertible linear transformation, and how the transformation matrix cancels out in the numerator and denominator of the WUC formula.

3. How should the number of partitions (M) be chosen in the simulations, and what is the impact of this choice on the accuracy of the method? Specifically, how does the number of partitions affect the variance of the distance estimates and the power of the model selection criterion, and what are the guidelines for selecting an appropriate value based on the characteristics of the data?

4. How does the proposed whitening approach compare to other existing methods for handling correlated data in dissimilarity matrix analysis, such as regularization techniques or dimensionality reduction methods? What specific advantages does the whitening approach offer over these alternatives, and in what scenarios might one method be preferred over another?

5. Could the authors provide a more detailed discussion of the interpretation of the results obtained using their test? How should the results be visualized and communicated, and what are the practical implications for researchers who are not experts in statistical methods for comparing dissimilarity matrices? For instance, if the test is used to compare the representational dissimilarity matrices of different brain regions, how should the differences be interpreted in terms of functional specialization or information processing?


## Rating:

7.5


## Confidence:

3.25


## Decision:

Accept
}