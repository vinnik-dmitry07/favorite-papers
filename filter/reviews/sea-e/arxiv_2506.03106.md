 **Summary:**
The paper introduces Critique-GRPO, an online reinforcement learning framework that integrates natural language feedback with numerical rewards to enhance the reasoning capabilities of large language models (LLMs). This approach, which includes a critique-guided refinement mechanism, is designed to address the limitations of purely numerical feedback, such as performance plateaus, ineffective spontaneous self-reflection, and persistent failures. The framework is evaluated across eight reasoning tasks and demonstrates significant improvements over existing supervised and RL-based fine-tuning methods. The authors argue that this integration of natural language feedback with numerical rewards can lead to more effective self-reflection and learning from critiques, thereby improving the performance of LLMs.

**Strengths:**
- The paper addresses a significant and relevant problem in the field of large language models (LLMs) by integrating natural language feedback with numerical rewards, which is a novel approach.
- The proposed framework, Critique-GRPO, is well-articulated, with clear explanations of its components and their integration, making it accessible and understandable.
- The paper is well-written, with a clear structure and logical flow, enhancing its readability and comprehension.
- The experiments conducted are robust and demonstrate the effectiveness of the proposed method, showing significant improvements over existing methods in various reasoning tasks.
- The paper provides a comprehensive analysis of the limitations of numerical feedback and the potential of natural language feedback, which is both insightful and valuable for the community.
- The inclusion of detailed analyses and ablation studies supports the claims made and provides a deeper understanding of the proposed method's effectiveness.

**Weaknesses:**
- The paper lacks a detailed discussion on the limitations of the proposed framework, which could provide a more balanced view and help in understanding the scope and applicability of the work.
- There is a need for more clarity and detail in the presentation of the methodology, particularly in the integration of natural language feedback with numerical rewards and the refinement process.
- The paper could benefit from a more thorough discussion on the computational efficiency and scalability of the proposed method, especially in terms of the computational resources required and the scalability with larger models.
- The paper's evaluation could be enhanced by including more diverse reasoning tasks and comparing the results with a broader range of models and methods, including more recent and relevant works.
- The paper's reliance on a single dataset for evaluation may limit the generalizability of the findings, and it would be beneficial to see how the method performs on other datasets.
- The paper could benefit from a more detailed discussion on the limitations of the current work and potential future directions for research.

**Questions:**
- Can the authors provide more details on the computational efficiency and scalability of the proposed method? How does it perform with larger models, and what are the computational resources required?
- How does the proposed method compare to other recent works that have explored similar ideas, such as those mentioned in the review?
- Could the authors clarify the integration of natural language feedback with numerical rewards and the refinement process, particularly how the feedback is integrated and how it influences the model's performance?
- What are the specific advantages of using natural language feedback over other forms of feedback, such as dense intermediate rewards?
- How does the proposed method perform on other datasets, and what are the implications of using different datasets for evaluation?
- Can the authors provide more details on the limitations of the current work and potential future directions for research?

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
- Reasons: The paper presents a novel approach to integrating natural language feedback with numerical rewards to enhance the reasoning capabilities of LLMs, addressing significant limitations of purely numerical feedback. The proposed framework, Critique-GRPO, is well-articulated and demonstrates significant improvements over existing methods in various reasoning tasks. The paper is well-written, with clear explanations and robust experiments that support the claims made. The integration of natural language feedback with numerical rewards is a significant contribution to the field, and the paper provides valuable insights into the potential of this approach. The decision to accept is based on the originality, methodological soundness, significance of results, and clarity and logic of presentation.