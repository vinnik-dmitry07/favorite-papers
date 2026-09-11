 **Summary:**
The paper introduces a novel method for comparing representational similarity analysis (RSA) models, focusing on the use of whitened unbiased RDM cosine similarity (WUC) to address biases and correlations in model comparisons. The authors derive analytical expressions for the mean and variance of biased and unbiased estimators of squared Euclidean and Mahalanobis distances, which are used to whiten the RDM estimation errors. The WUC method is shown to improve model selection and robustness to correlated measurement noise. The paper also discusses the theoretical and practical aspects of RSA, including the bias and covariance of distance estimators, and the impact of different noise models on RDM comparisons.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation for the proposed method.
- The methodology is sound, and the paper provides a thorough analysis of the bias and covariance of distance estimators, which is crucial for RSA.
- The paper introduces a new method for comparing RDMs, which is a significant contribution to the field.
- The paper is well-organized and provides a clear explanation of the methodology, including the derivation of the mean and variance of biased and unbiased estimators of squared Euclidean and Mahalanobis distances.
- The paper is well-positioned within the existing literature, and the proposed method is shown to be effective in improving model selection and robustness to correlated measurement noise.

**Weaknesses:**
- The paper could benefit from a more detailed explanation of the assumptions made in the analysis, particularly regarding the normality of measurement noise.
- The paper lacks a comprehensive discussion on the limitations of the proposed method, including its applicability to different types of data and noise models.
- The paper does not provide a detailed comparison of the computational cost of the proposed method with other existing methods, which could be crucial for practical applications.
- The paper could benefit from more extensive simulations to validate the effectiveness of the proposed method across different scenarios and noise conditions.
- The paper could be improved by including more real-data examples to demonstrate the practical applicability of the proposed method.

**Questions:**
- Can the authors clarify the assumptions made in the analysis, particularly regarding the normality of measurement noise?
- How does the proposed method perform when applied to different types of data, such as EEG or MEG data, which may have different noise characteristics?
- Can the authors provide a more detailed comparison of the computational cost of the proposed method with other existing methods?
- How does the proposed method perform in scenarios where the noise is not normally distributed?
- Can the authors provide more real-data examples to demonstrate the practical applicability of the proposed method?
- How does the proposed method compare to other methods in terms of model selection and robustness to correlated measurement noise?

**Soundness:**
3 good

**Presentation:**
3 good

**Contribution:**
3 good

**Rating:**
6 marginally above the acceptance threshold

**Paper Decision:**
- Decision: Accept
- Reasons: The paper presents a novel method for comparing RDMs, which addresses significant issues in RSA such as bias and covariance of distance estimators. The method is well-explained, and the paper is well-written, making it accessible and easy to follow. The methodological soundness is high, and the paper provides a significant contribution to the field by proposing a new method that improves model selection and robustness to correlated measurement noise. The decision to accept is based on the paper's originality, methodological soundness, significance of results, and clarity and logic of presentation. The paper is recommended for acceptance, possibly as a poster presentation to allow for further discussion and feedback.