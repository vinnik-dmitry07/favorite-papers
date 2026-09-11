 **Summary:**
The paper introduces On-Policy Representation Distillation (OPRD), a novel approach to on-policy distillation that focuses on aligning student and teacher representations across selected layers, rather than just the output layer. This method aims to address the limitations of traditional output-space distillation by providing a deterministic per-sample gradient, reducing variance, and exposing structural information that is typically discarded. OPRD is evaluated on various benchmarks, showing improvements over existing methods in terms of performance, efficiency, and memory usage. The paper also introduces OPRD-Bridge, a cross-architecture extension that aligns representations across different architectures, further enhancing the applicability of the method.

**Strengths:**
- The paper is well-written, easy to follow, and provides a clear motivation for the proposed method.
- The proposed method, OPRD, is novel and provides a deterministic per-sample gradient, which is a significant improvement over traditional output-space distillation.
- The method is evaluated on various benchmarks, showing improvements over existing methods in terms of performance, efficiency, and memory usage.
- The paper provides a theoretical analysis of the method, which helps in understanding its effectiveness and the reasons behind its performance.
- The method is well-motivated and the experiments are well-designed, providing a comprehensive evaluation of the proposed method.

**Weaknesses:**
- The paper could benefit from a more detailed discussion on the limitations of the proposed method, especially in terms of its applicability to different types of models and its potential impact on the training process.
- The paper lacks a detailed discussion on the computational complexity of the proposed method, which is crucial for understanding its practical implications.
- The paper could benefit from a more thorough comparison with other methods, including a discussion on how the proposed method performs in different scenarios and against different baselines.
- The paper could provide more insights into the training dynamics and the impact of the proposed method on the training process, especially in terms of convergence and stability.
- The paper could benefit from a more detailed discussion on the scalability of the proposed method, especially in terms of its applicability to larger models and more complex tasks.

**Questions:**
- How does the proposed method perform when applied to different types of models, such as those with different architectures or different training histories?
- Can the authors provide more insights into the computational complexity of the proposed method, especially in terms of its scalability and efficiency?
- How does the proposed method compare to other methods in terms of its impact on the training process, particularly in terms of convergence and stability?
- Can the authors provide more details on the experimental setup, such as the specifics of the training data and the training parameters used in the experiments?
- How does the proposed method perform in different scenarios, such as when applied to different types of tasks or when used with different types of models?
- Can the authors provide more details on the implementation of the proposed method, including any specific challenges or limitations they encountered during its development?

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
- Reasons: The paper introduces a novel method, OPRD, which addresses the limitations of traditional output-space distillation by focusing on aligning student and teacher representations across selected layers. The method is well-motivated, well-written, and provides a theoretical analysis that supports its effectiveness. The experiments demonstrate the method's superior performance over existing methods in terms of performance, efficiency, and memory usage. The paper also introduces OPRD-Bridge, a cross-architecture extension that further enhances the applicability of the method. The reviewers have highlighted the paper's clarity, originality, and the method's practical utility. The decision to accept is based on the paper's contribution to the field, its sound methodology, and the positive feedback from the reviewers.