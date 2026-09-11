 **Summary:**
The paper introduces a novel method for on-policy self-distillation, termed Latent On-Policy Self-Distillation (LOPD), which leverages a learnable latent context to enhance the training of a student policy. This approach allows the student to learn from a set of retrieved trajectories, which are transformed into a latent context that conditions the teacher policy. The method is evaluated across various benchmarks, demonstrating superior performance compared to existing methods. The paper also includes an ablation study to validate the effectiveness of the proposed components. Despite its strengths, the paper has been criticized for its clarity in explaining the method and its experimental setup, particularly in the presentation of equations and the discussion of related work.

**Strengths:**
- The paper introduces a novel approach to on-policy self-distillation by learning a latent context from a set of retrieved trajectories, which is a significant advancement over traditional methods.
- The method is well-motivated and well-explained, with a clear presentation of the methodology and its components.
- The paper is well-written, making it easy to follow, and the experiments are comprehensive, demonstrating the effectiveness of the proposed method across various benchmarks.
- The use of a learnable latent context allows for more effective supervision of the student policy, which is a novel approach in the field of self-distillation.
- The paper includes an ablation study that validates the effectiveness of the proposed components, providing a robust evaluation of the method.

**Weaknesses:**
- The paper lacks clarity in some sections, particularly in the explanation of the method and the experimental setup. Some equations and their explanations are not clear, which could confuse readers.
- The related work section could be improved by including more detailed discussions on how the proposed method differs from existing methods, such as latent computation and on-policy distillation.
- The paper does not sufficiently discuss the limitations of the proposed method, which could help in understanding its applicability and potential drawbacks.
- The paper could benefit from a more detailed discussion on the computational complexity and scalability of the method, especially in relation to the size of the retrieved trajectories.
- The paper does not provide sufficient implementation details, such as the specifics of the retrieval process and the training details, which could be crucial for reproducibility and understanding the method's practical implementation.

**Questions:**
- Could the authors clarify the role and impact of the "privileged margin" in the method, particularly how it affects the learning process and the performance of the student policy?
- How does the proposed method compare to other methods that use latent context, such as those mentioned in the related work section?
- Can the authors provide more details on the computational complexity and scalability of the method, especially in relation to the size of the retrieved trajectories?
- How are the retrieved trajectories selected, and what criteria are used to ensure their relevance and effectiveness in the learning process?
- Could the authors provide more implementation details, such as the specifics of the training process and the architecture used for the student and teacher policies?
- How does the proposed method handle the issue of overfitting, especially since the student policy is trained on the same data used to train the teacher policy?

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
- Reasons: The paper presents a novel approach to on-policy self-distillation that effectively leverages a learnable latent context to enhance the training of a student policy. The method is well-motivated, well-explained, and demonstrates superior performance across various benchmarks. The inclusion of an ablation study further validates the effectiveness of the proposed components. While there are some concerns regarding the clarity of the presentation and the depth of discussion on certain aspects of the method, these do not significantly detract from the overall strength of the paper. The decision to accept is supported by the paper's originality, methodological soundness, and the significant impact it could have on the field of self-distillation. The decision is also influenced by the potential for further improvements suggested by the reviewers, which could be addressed in future revisions.