 **Summary:**
The paper introduces a novel method called Self-Distillation Fine-Tuning (SDFT), which enables on-policy learning directly from demonstrations, leveraging in-context learning to generate on-policy training signals that preserve prior capabilities while acquiring new skills. SDFT is evaluated across various continual learning settings, demonstrating superior performance in skill learning and knowledge acquisition tasks compared to supervised fine-tuning. The methodology involves using a demonstration-conditioned model as a teacher, which generates on-policy training signals that preserve prior capabilities while acquiring new skills. The paper also discusses the theoretical underpinnings of the method and provides empirical evidence of its effectiveness.

**Strengths:**
- The paper introduces a novel method called Self-Distillation Fine-Tuning (SDFT), which enables on-policy learning directly from demonstrations, leveraging in-context learning to generate on-policy training signals that preserve prior capabilities while acquiring new skills.
- The method is evaluated in two continual learning settings: skill learning and knowledge acquisition, demonstrating superior performance compared to supervised learning.
- The paper is well-written, clear, and easy to follow, with a clear motivation and a logical flow of ideas.
- The experiments are well-designed, and the results are convincing, showing that the proposed method outperforms supervised fine-tuning in continual learning settings.
- The paper provides a clear explanation of the method and its implementation, including the use of an exponential moving average (EMA) of the student parameters for the teacher and the use of a logit-level loss between the teacher and the students.
- The paper also discusses the limitations of the method, including the requirement for a strong in-context learning ability in the base model and the potential for the student to inherit spurious linguistic patterns from the teacher.

**Weaknesses:**
- The paper lacks a detailed discussion on the computational cost of the proposed method compared to other methods, which could be crucial for practical implementation.
- The paper does not discuss the limitations of the method in detail, which could help in understanding the scope and applicability of the proposed method.
- The paper does not provide a detailed discussion on the scalability of the method with different model sizes and the impact of the number of demonstrations on the performance of the method.
- The paper does not discuss the limitations of the method in detail, which could help in understanding the scope and applicability of the proposed method.
- The paper does not compare the proposed method with other similar methods, which could provide a better understanding of its advantages and disadvantages.
- The paper does not discuss the limitations of the method in detail, which could help in understanding the scope and applicability of the proposed method.

**Questions:**
- Can the authors provide a detailed discussion on the computational cost of the proposed method compared to other methods?
- How does the method perform with different model sizes, and what is the impact of the number of demonstrations on the performance of the method?
- Can the authors provide a detailed discussion on the limitations of the method and the scope of its applicability?
- How does the proposed method compare with other similar methods in terms of performance and efficiency?
- Can the authors provide a detailed discussion on the limitations of the method and the scope of its applicability?
- Can the authors provide a detailed discussion on the limitations of the method and the scope of its applicability?

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
- Reasons: The paper presents a novel method, Self-Distillation Fine-Tuning (SDFT), which addresses the challenge of continual learning by enabling on-policy learning directly from demonstrations. The method is evaluated in various continual learning settings and shows superior performance compared to supervised learning. The paper is well-written, clear, and easy to follow, with a clear motivation and a logical flow of ideas. The methodology is novel and provides a significant contribution to the field of continual learning. The reviewers have highlighted the method's effectiveness and the clarity of the paper, supporting its acceptance. The decision to accept is based on the originality of the method, methodological soundness, significance of results, and clarity and logic of presentation.