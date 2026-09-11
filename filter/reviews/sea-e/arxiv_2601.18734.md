 **Summary:**
The paper introduces a novel method called On-Policy Self-Distillation (OPSD), which allows a single model to act as both teacher and student, leveraging ground-truth answers to provide dense token-level supervision on student rollouts. This method is designed to improve the training efficiency of large language models (LLMs) on reasoning tasks by minimizing the per-token divergence between the teacher and student distributions. The approach is evaluated on three competition-level mathematical reasoning tasks, showing that it matches the performance of GRPO with significantly improved token efficiency and outperforms supervised fine-tuning. The paper also includes an ablation study to analyze the impact of different divergence objectives, the effect of student generation length, and the student-teacher generation styles.

**Strengths:**
- The paper introduces a novel approach called On-Policy Self-Distillation (OPSD), which allows a single model to act as both teacher and student, leveraging ground-truth answers to provide dense token-level supervision on student rollouts.
- The method is evaluated on three competition-level mathematical reasoning tasks, demonstrating that it matches the performance of GRPO with significantly improved token efficiency and outperforms supervised fine-tuning.
- The paper includes an ablation study to analyze the impact of different divergence objectives, the effect of student generation length, and student-teacher generation styles.
- The method is simple yet effective, and the experiments are well-designed, showing that OPSD outperforms GRPO and supervised fine-tuning on reasoning tasks.
- The paper is well-written and easy to follow, making it accessible to a broad audience.

**Weaknesses:**
- The paper lacks a clear explanation of why the proposed method is effective, particularly in terms of how the teacher policy is conditioned on privileged information and how this influences the student policy.
- The paper does not provide a detailed comparison with other self-distillation methods, which could help in understanding the unique contributions of OPSD.
- There is a lack of discussion on the limitations of the proposed method, such as its applicability to other types of tasks beyond mathematical reasoning.
- The paper does not include a discussion on the limitations of the proposed method, which could help in understanding its applicability and potential drawbacks.
- The paper does not include a discussion on the limitations of the proposed method, which could help in understanding its applicability and potential drawbacks.

**Questions:**
- Could you provide more details on how the teacher policy is conditioned on privileged information and how this influences the student policy?
- How does the proposed method compare with other self-distillation methods in terms of effectiveness and efficiency?
- Could you provide more details on the limitations of the proposed method and its applicability to other types of tasks beyond mathematical reasoning?
- How does the proposed method compare with other methods in terms of computational cost and efficiency?
- Could you provide more details on the limitations of the proposed method and its potential drawbacks?

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
- Reasons: The paper presents a novel method, OPSD, which allows a single model to act as both teacher and student, leveraging ground-truth answers to provide dense token-level supervision on student rollouts. The method is evaluated on three competition-level mathematical reasoning tasks, demonstrating that it matches the performance of GRPO with significantly improved token efficiency and outperforms supervised fine-tuning. The paper includes an ablation study to analyze the impact of different divergence objectives, the effect of student generation length, and student-teacher generation styles. The method is simple yet effective, and the experiments are well-designed. The paper is well-written and easy to follow. The reviewers have highlighted the novelty and effectiveness of the proposed method, and the paper is recommended for acceptance, particularly as a poster presentation.