 **Summary:**
The paper investigates on-policy distillation (OPD) in large language models (LLMs), focusing on the conditions that influence its success or failure. Two key factors are identified: the compatibility of thinking patterns between the student and teacher, and the availability of new knowledge in the teacher that the student has not yet learned. The authors propose practical strategies to address these issues, such as off-policy cold start and teacher-aligned prompt selection. They also explore the dynamics of OPD through empirical analysis and token-level mechanisms, highlighting the importance of high-probability token alignment and the impact of prompt templates. The paper provides a comprehensive review of related works and presents a detailed analysis of OPD's effectiveness, offering insights into its practical applications and future research directions.

**Strengths:**
- The paper provides a comprehensive analysis of on-policy distillation (OPD), including its dynamics, mechanisms, and practical recipes, which is crucial for understanding and improving the effectiveness of OPD in large language models (LLMs).
- The authors have identified two key conditions that influence the success or failure of OPD: the compatibility of thinking patterns between the student and teacher, and the availability of new knowledge in the teacher that the student has not yet learned.
- The paper is well-written, clear, and easy to follow, making it accessible to a broad audience.
- The experiments are well-designed and well-executed, providing valuable insights into the behavior of OPD and its impact on the performance of LLMs.
- The paper introduces two practical strategies to address the identified issues in OPD: off-policy cold start and teacher-aligned prompt selection, which can be directly applied to improve the performance of LLMs.
- The paper includes a detailed analysis of the token-level mechanisms of OPD, which is crucial for understanding the underlying mechanisms of OPD and its impact on the performance of LLMs.

**Weaknesses:**
- The paper primarily focuses on mathematical reasoning tasks, which limits the generalizability of the findings to other types of tasks such as open-ended generation or code generation.
- The experiments are limited to a few model families, which may not fully capture the complexity and diversity of real-world LLMs.
- The paper does not provide a theoretical analysis of the conditions for successful OPD, which could enhance the understanding of the underlying mechanisms and provide a more robust framework for practical applications.
- The paper does not discuss the impact of pre-training on OPD, which is a significant factor in the performance of LLMs.
- The paper does not include a discussion on the limitations of the proposed strategies, which could help in understanding the practical challenges and potential drawbacks of implementing these strategies.
- The paper could benefit from a more detailed discussion on the impact of prompt templates on the performance of OPD, as this is a critical factor in practical applications.

**Questions:**
- Can the authors provide more details on the prompt templates used in the experiments, especially how they were selected and their impact on the performance of OPD?
- How does the paper address the potential issues of overfitting or underfitting in the teacher model, which could affect the effectiveness of OPD?
- Could the authors discuss the potential impact of pre-training on OPD, and how this might influence the effectiveness of the strategies proposed in the paper?
- How do the authors ensure the generalizability of the findings to other types of tasks beyond mathematical reasoning?
- Could the authors provide a more detailed theoretical analysis of the conditions for successful OPD, and how this might guide practical applications?
- How do the authors address the potential limitations of their proposed strategies, and what are the practical challenges in implementing these strategies in real-world applications?

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
- Reasons: The paper provides a comprehensive analysis of on-policy distillation (OPD) in large language models (LLMs), identifying key conditions that influence its success or failure. It offers practical strategies to address these issues and contributes to the understanding of OPD dynamics and mechanisms. The paper is well-written, clear, and easy to follow, making it accessible to a broad audience. The experimental design is well-executed, and the findings are valuable for improving the effectiveness of OPD in LLMs. The paper's contribution is significant, and the reviewers have highlighted its potential impact on the field. The decision to accept is based on the paper's originality, methodological soundness, significance of results, and clarity and logic of presentation.