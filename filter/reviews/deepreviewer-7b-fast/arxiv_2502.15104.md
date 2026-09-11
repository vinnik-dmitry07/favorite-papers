Of course. I will use Fast Mode for quick thinking. As a professional reviewer, I will directly output a detailed evaluation of this paper. Let me think - Fast Mode means I will directly output a Summary, followed by scores for Soundness, Presentation and Contribution, then provide analysis of Strengths, Weaknesses, Suggestions, and Questions. Finally, I will output the Rating, Confidence and Decision:

\boxed_review{
## Summary:

This paper addresses a significant issue in the application of Centered Kernel Alignment (CKA) for comparing neural representations, particularly in scenarios where the number of stimuli and neurons is limited. The authors identify a bias in existing CKA estimators that arises from finite sample sizes, a problem often encountered in real-world datasets. They propose a novel, unbiased estimator that corrects for both stimulus and neuron sampling, providing a more reliable measure of representation similarity. The theoretical analysis is thorough, and the empirical validation is conducted across diverse datasets, including electrophysiological recordings from the visual cortex and model-to-brain comparisons. The results demonstrate that the proposed estimator yields more accurate and consistent CKA values, especially in low-sample regimes. This work is crucial for advancing the field of neural representation analysis, as it provides a more robust tool for comparing neural and computational models. However, the paper could benefit from a more detailed discussion of the practical implications of the bias, a clearer explanation of the estimator's derivation, and a more comprehensive comparison with existing methods, particularly in the context of model-to-brain alignment and the interpretation of disentanglement metrics.


## Soundness:

3.25


## Presentation:

3.0


## Contribution:

3.25


## Strengths:

I find the paper to be a valuable contribution to the field of neural representation analysis. The authors have identified a critical limitation in the widely used CKA metric, which is the bias introduced by finite sample sizes in both stimuli and neurons. This is a significant issue, especially in neuroscience where datasets are often limited. The proposed estimator is theoretically well-founded, and the authors provide a clear and detailed derivation in the appendix, which I found to be very helpful. The empirical validation is robust, with experiments conducted on both synthetic and real-world datasets, including electrophysiological recordings from the visual cortex. The results are compelling, showing that the proposed estimator yields more accurate and consistent CKA values, particularly in low-sample regimes. The paper also includes a discussion of the practical implications of the bias, such as the underestimation of alignment in model-to-brain comparisons, which is a valuable insight for the community. The authors' approach to addressing the bias is innovative and well-justified, making this a strong and impactful paper.


## Weaknesses:

Despite the paper's strengths, there are several verified limitations that need to be addressed. First, the paper lacks a detailed discussion of the practical implications of the bias in CKA. While the authors mention that the bias can lead to misleading conclusions, such as underestimating the alignment between models and brains, they do not provide concrete examples of how this bias affects the interpretation of CKA values in real-world scenarios. For instance, the paper could benefit from a more thorough exploration of how the magnitude of the bias changes with varying sample sizes and intrinsic dimensionality, and how this impacts the reliability of CKA as a measure of representational similarity. This would help readers understand the practical significance of the proposed unbiased estimator and when it is most applicable. I have a high confidence level in this concern, as the paper's focus is primarily on the theoretical and methodological aspects, with limited practical guidance for users (Section 4, Appendix B.2, and Figure 2).

Second, the paper does not provide a clear and detailed explanation of the derivation of the proposed estimator. While the final formula is presented, the intermediate steps and the rationale behind the specific terms are not sufficiently elaborated. This makes it difficult for readers to understand the underlying principles and the assumptions made in the derivation. For example, the paper could benefit from a step-by-step breakdown of the derivation, including the mathematical operations and the reasoning behind each step. This would not only enhance the clarity of the paper but also provide a foundation for future research and extensions of the proposed method (Section 3, Appendix A).

Third, the paper's comparison with existing methods is limited, particularly in the context of model-to-brain alignment and the interpretation of disentanglement metrics. The authors mention that the bias in CKA can lead to incorrect conclusions about the alignment between models and brains, but they do not provide a detailed comparison with other methods that address this issue, such as those based on representational similarity analysis (RSA) or other alignment techniques. Additionally, the paper could benefit from a more in-depth discussion of the limitations of the proposed method, including scenarios where it might not perform well or where other methods might be more appropriate. This would provide a more balanced and comprehensive view of the proposed method's strengths and weaknesses (Section 4, Figure 5, and Figure 6).

Fourth, the paper's discussion of the results in the context of model-to-brain alignment is somewhat limited. While the authors demonstrate that their estimator provides more reliable CKA values in this context, they do not delve into the specific implications of these findings for model development and validation. For example, the paper could explore how the proposed method can be used to identify the specific aspects of a model that are most similar to the brain, or how it can be used to compare different model architectures and training procedures. This would provide a more compelling motivation for the proposed method and highlight its practical relevance (Section 4, Figure 3).

Finally, the paper's treatment of the disentanglement metric in the context of object categories is somewhat confusing. The authors state that the CKA value between object categories generally decreases over V1, V4, and IT, indicating a gradual semantic disentanglement. However, they do not provide a clear explanation of how this disentanglement is measured and why it is important. A more detailed explanation of the disentanglement metric and its interpretation would be beneficial. Furthermore, the paper could explore the relationship between the proposed CKA estimator and other measures of representational similarity, such as centered kernel alignment (CKA) with different parameter settings, to provide a more comprehensive understanding of the method's performance (Section 4, Figure 5).


## Suggestions:

To enhance the paper's impact and clarity, I recommend several concrete, actionable improvements. First, the authors should provide a more detailed discussion of the practical implications of the bias in CKA. This could include a thorough exploration of how the magnitude of the bias changes with varying sample sizes and intrinsic dimensionality, and how this impacts the reliability of CKA as a measure of representational similarity. The authors could also discuss specific scenarios where the bias is particularly problematic and provide concrete examples of how the proposed unbiased estimator can lead to different conclusions compared to existing methods. This would help readers understand the practical significance of the proposed estimator and when it is most applicable (Section 4, Appendix B.2, and Figure 2).

Second, the authors should provide a more detailed and step-by-step explanation of the derivation of the proposed estimator. This could involve breaking down the mathematical operations and providing a clear rationale for each term in the final formula. The authors could also include a visual representation of the derivation process, such as a flowchart or a series of equations with annotations, to aid in understanding. This would not only enhance the clarity of the paper but also provide a foundation for future research and extensions of the proposed method (Section 3, Appendix A).

Third, the authors should expand the comparison with existing methods, particularly in the context of model-to-brain alignment and the interpretation of disentanglement metrics. This could include a detailed comparison with other methods that address the bias in CKA, such as those based on RSA or other alignment techniques. The authors should also discuss the limitations of their method, including scenarios where it might not perform well or where other methods might be more appropriate. This would provide a more balanced and comprehensive view of the proposed method's strengths and weaknesses (Section 4, Figure 5, and Figure 6).

Fourth, the authors should provide a more in-depth discussion of the results in the context of model-to-brain alignment. This could involve exploring how the proposed method can be used to identify the specific aspects of a model that are most similar to the brain, or how it can be used to compare different model architectures and training procedures. The authors could also discuss the implications of their findings for model development and validation, and how the proposed method can be used to guide the development of more biologically plausible models (Section 4, Figure 3).

Finally, the authors should clarify the treatment of the disentanglement metric in the context of object categories. This could involve a more detailed explanation of how the CKA value between object categories is calculated and why it is important. The authors could also explore the relationship between the proposed CKA estimator and other measures of representational similarity, such as CKA with different parameter settings, to provide a more comprehensive understanding of the method's performance. Additionally, the authors should consider including a discussion of the limitations of using CKA to measure disentanglement, and whether other metrics might be more appropriate in certain contexts (Section 4, Figure 5).


## Questions:

I have a few questions that I believe would help clarify and strengthen the paper. First, how does the proposed estimator perform when the intrinsic dimensionality of the representations is very high, or when the number of stimuli is extremely small? Understanding the limitations of the estimator in these extreme scenarios would provide valuable insights into its robustness and applicability (Section 4, Appendix B.2, and Figure 2).

Second, could the authors provide a more detailed explanation of the practical implications of the bias in CKA? For example, how does the bias affect the interpretation of CKA values in real-world scenarios, and what are the specific scenarios where the proposed unbiased estimator is most beneficial? This would help readers understand the practical significance of the proposed method (Section 4, Appendix B.2, and Figure 2).

Third, how does the proposed estimator compare to other methods that address the bias in CKA, such as those based on RSA or other alignment techniques? A detailed comparison would help readers understand the relative strengths and weaknesses of the proposed method and when it is most appropriate to use it (Section 4, Figure 5, and Figure 6).

Fourth, could the authors provide a more in-depth discussion of the results in the context of model-to-brain alignment? Specifically, how can the proposed method be used to identify the specific aspects of a model that are most similar to the brain, and how can it be used to compare different model architectures and training procedures? This would provide a more compelling motivation for the proposed method and highlight its practical relevance (Section 4, Figure 3).

Finally, could the authors clarify the treatment of the disentanglement metric in the context of object categories? How is the CKA value between object categories calculated, and why is it important? A more detailed explanation of the disentanglement metric and its interpretation would be beneficial, and the authors could also explore the relationship between the proposed CKA estimator and other measures of representational similarity (Section 4, Figure 5).


## Rating:

7.0


## Confidence:

3.25


## Decision:

Accept
}