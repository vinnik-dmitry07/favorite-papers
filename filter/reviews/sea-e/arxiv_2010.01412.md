 **Summary:**
The paper introduces Sharpness-Aware Minimization (SAM), a novel method aimed at improving model generalization by minimizing both training loss and loss sharpness. SAM is designed to prevent models from converging to sharp minima, which are often associated with overfitting. The method is supported by a theoretical framework that connects loss sharpness to generalization, and is empirically evaluated across various datasets and models, showing improvements in generalization performance. The paper also discusses the computational efficiency of SAM, which is crucial for its practical application. Despite its strengths, the paper has been criticized for its lack of clarity in certain sections, particularly in the explanation of the m-sharpness and the choice of hyperparameters.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation and a well-designed algorithm.
- The proposed method, SAM, is novel and effective, as demonstrated by its ability to improve generalization performance across various datasets and models.
- The paper provides a theoretical analysis that connects loss sharpness to generalization, which is a significant contribution to the field.
- The empirical results are strong, showing that SAM can improve generalization performance on a variety of datasets and models.
- The paper is well-presented, with clear figures and a clear explanation of the methodology, which makes it accessible to a broad audience.

**Weaknesses:**
- The paper lacks a detailed discussion on the computational cost of SAM, which is crucial for understanding its practical applicability.
- The choice of hyperparameters, particularly the value of ρ, is not well-justified, and the sensitivity of the method to these parameters is not adequately explored.
- The paper could benefit from a more detailed discussion on the limitations of SAM, including its potential impact on training time and its effectiveness in different scenarios.
- The paper does not adequately address the scalability of SAM to larger models, which is a significant concern for its practical application.
- The paper could benefit from a more comprehensive comparison with existing methods, particularly those that address similar issues in model generalization.
- The paper contains some typographical errors and could benefit from a more thorough proofreading.

**Questions:**
- Could you provide more details on the computational cost of SAM, including the time and memory required for training?
- How does the choice of ρ affect the performance of SAM, and what are the optimal values for different datasets and models?
- Can you provide more details on the scalability of SAM to larger models, and what are the potential challenges in implementing SAM on larger models?
- How does SAM compare to other methods that address similar issues in model generalization, such as those that use different regularization terms or optimization strategies?
- Could you clarify the definition and role of m in the m-sharpness measure, and how it affects the generalization performance?
- How does SAM perform in scenarios where the training data is noisy or biased, and what are the implications of these conditions on the generalization performance?

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
- Reasons: The paper presents a novel method, SAM, that effectively improves model generalization by minimizing both training loss and loss sharpness. The method is supported by a theoretical framework and empirical evidence, demonstrating its effectiveness across various datasets and models. The paper is well-written, clear, and easy to follow, making it accessible to a broad audience. However, the paper could benefit from a more detailed discussion on the computational cost and scalability of SAM, as well as a more comprehensive comparison with existing methods. The decision to accept is based on the paper's originality, methodological soundness, and the significance of its results, despite some concerns regarding clarity and presentation in certain sections.