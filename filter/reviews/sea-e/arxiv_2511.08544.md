 **Summary:**
The paper introduces LeJEPA, a novel self-supervised learning method that optimizes the embedding distribution to be isotropic Gaussian, aiming to minimize prediction risk across various downstream tasks. This approach is supported by a new regularization term, SIGReg, which is designed to enforce this distribution. The method is evaluated across multiple datasets and architectures, showing competitive performance and stability across hyperparameters and domains. Theoretical analysis supports the choice of isotropic Gaussian as the optimal distribution, and the paper provides a comprehensive evaluation of the method's effectiveness and scalability. However, concerns are raised about the novelty of the method, the clarity of the writing, and the depth of the experimental validation, particularly in terms of the number of datasets and architectures tested.

**Strengths:**
- The paper presents a novel approach to self-supervised learning (SSL) by focusing on the optimal embedding distribution, which is a significant contribution to the field.
- The methodology is well-supported by theoretical analysis, which is both rigorous and well-explained, enhancing the credibility of the proposed approach.
- The paper is well-written, making it accessible and easy to follow, with clear explanations of the methodology and its implications.
- The experimental results are comprehensive and demonstrate the effectiveness of the proposed method across various datasets and architectures, showing competitive performance and stability.
- The paper is well-motivated, with a clear explanation of the rationale behind the proposed method, which is both intuitive and well-supported by empirical evidence.

**Weaknesses:**
- The paper could benefit from a more detailed discussion on the choice of the isotropic Gaussian distribution, particularly in terms of its practical implications and the theoretical justification for its superiority over other distributions.
- There is a lack of novelty in the methodology, as the use of isotropic Gaussian for SSL is not new and has been explored in previous works.
- The paper does not adequately address the limitations of the proposed method, which could include the potential for overfitting or the impact of hyperparameter choices on performance.
- The experimental validation is limited to a few datasets and architectures, which might not sufficiently demonstrate the generalizability of the method across different domains or models.
- The paper could benefit from a clearer presentation and better organization, particularly in the introduction and the presentation of technical details.
- There are several typographical errors and inconsistencies in the paper that need to be corrected for clarity and professionalism.

**Questions:**
- Could the authors provide a more detailed analysis of the practical implications of using an isotropic Gaussian distribution in SSL?
- How does the proposed method compare to other recent SSL methods, particularly those that use different distributions or regularization techniques?
- Could the authors elaborate on the choice of hyperparameters and their impact on the performance of the method?
- In terms of the experimental validation, could the authors consider expanding the number of datasets and architectures to provide a more comprehensive evaluation of the method's effectiveness?
- How does the proposed method address the issue of overfitting, which is a common challenge in SSL?
- Could the authors clarify the notations and definitions used in the paper to improve readability and understanding?

**Soundness:**
3 good

**Presentation:**
3 good

**Contribution:**
3 good

**Rating:**
6 weak accept

**Paper Decision:**
- Decision: Accept
- Reasons: The paper presents a novel approach to self-supervised learning, supported by both theoretical analysis and empirical evidence. The method, LeJEPA, offers a new perspective on optimizing embedding distributions for SSL, which is a significant contribution to the field. Despite some concerns regarding the novelty and the depth of experimental validation, the paper is well-written, easy to follow, and provides a comprehensive evaluation of the method's effectiveness and scalability. The decision to accept is based on the paper's originality, methodological soundness, and the significance of its results, even though it requires minor improvements in clarity and presentation.