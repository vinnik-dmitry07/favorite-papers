 **Summary:**
The paper investigates the challenges and potential improvements in on-policy distillation (OPD) by critically examining the use of sampled-token log-ratio for distribution matching. It highlights the limitations of this approach, particularly in long rollouts where the prefix may deviate from the teacher's typical support, leading to biased and unstable training signals. The authors propose a novel approach, termed "truncated reverse-KL," which compares teacher and student distributions over a teacher-supported token set at each prefix. This method aims to address the issues of imbalanced token-level supervision, unreliable teacher guidance on student-generated prefixes, and tokenizer or special-token mismatch. The paper presents a theoretical analysis and empirical evidence demonstrating the effectiveness of this approach over traditional OPD methods.

**Strengths:**
- The paper provides a comprehensive analysis of the challenges in on-policy distillation (OPD) and proposes a novel approach to address these issues, which is supported by both theoretical analysis and empirical evidence.
- The authors have identified three failure modes of sampled-token OPD and proposed a new objective that addresses these issues, showing significant improvements in optimization stability and performance.
- The paper is well-written, clear, and easy to follow, making it accessible to a broad audience.
- The proposed method is simple, intuitive, and has been tested on multiple tasks, demonstrating its effectiveness in improving performance.
- The paper provides a detailed analysis of the issues with the current OPD methods and proposes a novel approach to address these issues, which is a significant contribution to the field.

**Weaknesses:**
- The paper lacks a detailed discussion on the limitations of the proposed method, particularly in scenarios where the method might not be as effective.
- The empirical evaluation is limited to a single model, which might not fully demonstrate the generalizability of the findings.
- The paper could benefit from a more thorough discussion on the computational cost and scalability of the proposed method, especially in comparison to other methods like off-policy distillation.
- The paper does not sufficiently address how the method performs in scenarios where the student model's output is significantly different from the teacher model's, which could affect the reliability of the teacher's guidance.
- The paper does not provide a detailed discussion on the potential societal impacts of the proposed method, which could be a significant concern for some applications.

**Questions:**
- How does the proposed method perform in scenarios where the student model's output is significantly different from the teacher model's, and what measures can be taken to ensure the reliability of the teacher's guidance in such cases?
- Can the authors provide more details on the computational cost and scalability of the proposed method, especially in comparison to other methods like off-policy distillation?
- How does the proposed method compare to other methods like off-policy distillation in terms of performance and computational efficiency?
- Could the authors elaborate on the potential societal impacts of the proposed method, particularly in applications where the model's outputs could have significant real-world consequences?
- How does the proposed method perform in scenarios where the student model's output is not well-aligned with the teacher model's, and what are the implications of this misalignment for the effectiveness of the distillation process?

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
- Reasons: The paper presents a novel approach to on-policy distillation that addresses significant issues with the current methods, particularly in long rollouts where the prefix may deviate from the teacher's typical support. The proposed method, "truncated reverse-KL," shows promising results in improving optimization stability and performance, as evidenced by both theoretical analysis and empirical evidence. The paper is well-written, clear, and easy to follow, making it accessible to a broad audience. Despite some concerns regarding the limited empirical evaluation and potential limitations in scenarios where the student model's output significantly differs from the teacher model's, the paper's contributions are significant enough to warrant acceptance, especially given the potential impact on the field of on-policy distillation.