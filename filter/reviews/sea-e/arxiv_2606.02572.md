 **Summary:**
The paper introduces Variance-Invariance-Sketching Regularization (VISReg), a novel method for self-supervised learning that combines the benefits of VICReg and SIGReg. VISReg replaces the covariance regularization of VICReg with a sketching objective based on Sliced Wasserstein Distance, aiming to align the normalized embedding distribution with an isotropic Gaussian prior along random 1D projections. This approach allows for the decoupling of scale and shape, providing robust gradients even under collapse. The method is evaluated on various datasets, showing improvements over existing methods in terms of generalization and robustness. However, concerns are raised regarding the clarity of the method's motivation and the empirical evidence supporting its advantages over existing methods.

**Strengths:**
- The paper is well-written, with clear and concise explanations of the proposed method and its advantages over existing methods.
- The method is simple, effective, and easy to implement, with a focus on robustness and scalability.
- The paper includes a comprehensive analysis of the hyperparameter landscape, providing clear guidance for scaling and training stability within the proposed paradigm.
- The method achieves state-of-the-art performance on out-of-distribution datasets, demonstrating its effectiveness in real-world applications.
- The paper is well-organized, with a clear presentation of the method and its advantages, and includes a detailed analysis of the hyperparameter landscape.

**Weaknesses:**
- The paper lacks a detailed comparison with other relevant methods such as VICReg and SIGReg, particularly in terms of computational complexity and empirical performance.
- There is a lack of clarity in the motivation behind the proposed method, particularly in how it addresses the limitations of existing methods like VICReg and SIGReg.
- The paper does not provide sufficient empirical evidence to support the claims of the method's advantages over existing methods, particularly in terms of computational efficiency and robustness.
- The paper could benefit from a more detailed discussion on the limitations of the proposed method and how these might impact its practical application.
- There are several typos and minor errors in the manuscript that need correction.

**Questions:**
- Could the authors provide a more detailed comparison with VICReg and SIGReg, particularly in terms of computational complexity and empirical performance?
- How does the proposed method address the limitations of VICReg and SIGReg, and what are the specific advantages of VISReg over these methods?
- Can the authors clarify the motivation behind the proposed method and how it addresses the specific challenges in self-supervised learning?
- How does the method perform in scenarios where the embedding collapses, and what are the implications of this for the robustness of the model?
- Could the authors provide more details on the computational efficiency of the method, particularly in terms of runtime and memory usage?
- How does the method perform in terms of generalization to different datasets and domains, and what are the implications of this for its practical application?

**Soundness:**
3 good

**Presentation:**
3 good

**Contribution:**
3 good

**Rating:**
7 accept, but needs minor improvements

**Paper Decision:**
- Decision: Accept
- Reasons: The paper introduces a novel method, VISReg, which addresses the limitations of existing methods in self-supervised learning by combining the benefits of VICReg and SIGReg. The method is well-received for its simplicity, effectiveness, and scalability. The paper is well-written and provides a clear explanation of the method and its advantages. However, concerns are raised regarding the clarity of the motivation and the empirical evidence supporting the method's advantages. The decision to accept is based on the overall positive reception of the method and its potential impact on the field, but with the recommendation for minor improvements in clarity and empirical validation.