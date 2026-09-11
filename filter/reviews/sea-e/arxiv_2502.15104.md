 **Summary:**
The paper introduces a novel estimator for the Centered Kernel Alignment (CKA) to address the bias introduced by sampling a subset of neurons, which is a significant issue in both artificial and biological systems. The authors demonstrate that the bias in CKA is influenced by the geometry of high-dimensional representations and propose a new estimator that corrects for both input and feature sampling. This estimator is evaluated on both synthetic and real electrophysiological data from visual cortical areas, showing its effectiveness in revealing how object representations become progressively disentangled across layers in both biological and artificial systems. The paper also discusses the limitations of existing CKA estimators and provides a theoretical analysis of the bias caused by representation geometry.

**Strengths:**
- The paper addresses a significant and relevant problem in the field of neural representation similarity, specifically the bias introduced by sampling a subset of neurons, which is often overlooked in current CKA estimators.
- The paper is well-written, clear, and easy to follow, with a clear motivation and a detailed explanation of the methodology.
- The proposed estimator is theoretically sound and provides a novel approach to correcting for both input and feature sampling, which is crucial for accurate representation alignment.
- The paper includes a thorough theoretical analysis of the bias caused by representation geometry and provides a novel estimator that corrects for both input and feature sampling.
- The empirical results demonstrate the effectiveness of the proposed estimator in revealing how object representations become progressively disentangled across layers in both biological and artificial systems.
- The paper is well-organized, with clear definitions, problem statement, and contributions, making it accessible to a broad audience.

**Weaknesses:**
- The paper lacks a detailed discussion on the limitations of the proposed estimator, particularly in scenarios where the estimator may not perform optimally or where it may introduce new biases.
- The paper could benefit from a more detailed explanation of the theoretical results, especially the bias of the estimator and the assumptions made in the theoretical analysis.
- The paper could be improved by including more detailed explanations of the methodology and results, particularly in the experimental sections where the data and methodology are not sufficiently detailed.
- The paper could benefit from a more comprehensive comparison with other CKA estimators, including a discussion on how the proposed estimator compares in terms of bias and performance.
- The paper could be made more accessible to a broader audience by including more detailed explanations of the methodology and results, particularly in the experimental sections.

**Questions:**
- How does the proposed estimator perform in scenarios where the number of neurons sampled is very small?
- Could you provide more details on the assumptions made in the theoretical analysis, particularly regarding the independence of the neurons and the stimuli?
- How does the proposed estimator compare to other CKA estimators in terms of bias and performance?
- Can you provide a more detailed explanation of the methodology and results, particularly in the experimental sections, to make the paper more accessible to a broader audience?
- How does the proposed estimator handle the bias introduced by non-linear operations on the ℋ H estimates?
- Could you clarify the notation and definitions used in the paper, particularly in equations and sections where the notation is not clear?

**Soundness:**
3 good

**Presentation:**
3 good

**Contribution:**
3 good

**Rating:**
7 accept

**Paper Decision:**
- Decision: Accept
- Reasons: The paper presents a novel estimator for CKA that effectively addresses the bias introduced by sampling a subset of neurons, a significant issue in both artificial and biological systems. The theoretical analysis and empirical validation provided are robust, demonstrating the reliability of the estimator in revealing how object representations become progressively disentangled across layers in both biological and artificial systems. The paper is well-written, clear, and easy to follow, making it accessible to a broad audience. The reviewers have highlighted the paper's contribution to the field and its potential impact on the analysis of neural and computational representations. The decision to accept is based on the originality, methodological soundness, significance of results, and clarity and logic of presentation.