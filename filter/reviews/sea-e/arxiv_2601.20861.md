 **Summary:**
The paper investigates the use of Evolutionary Strategies (ES) for continual learning in large language models (LLMs), focusing on the issue of catastrophic forgetting. The authors compare ES with Gradient Recalibration Optimization (GRPO) and demonstrate that ES exhibits significant catastrophic forgetting, which is attributed to its less sparse updates and larger L2 norms compared to GRPO. The study includes empirical analyses across various datasets and models, showing that ES, while competitive in performance, suffers from severe forgetting. The paper also provides insights into the mechanisms behind these phenomena, suggesting potential avenues for improving ES in continual learning scenarios.

**Strengths:**
- The paper addresses a significant and timely issue in the field of continual learning, specifically focusing on the catastrophic forgetting problem in Evolutionary Strategies (ES) for large language models (LLMs).
- The authors provide a comprehensive empirical analysis, comparing ES with Gradient Recalibration Optimization (GRPO) across multiple datasets and models, demonstrating the forgetting behavior of ES.
- The paper is well-written, clear, and easy to follow, making it accessible to a broad audience.
- The study includes a detailed analysis of the forgetting behavior in ES, which is crucial for understanding the limitations of gradient-free algorithms in continual learning.
- The authors release their codebase and trained models, which is beneficial for reproducibility and further research in the field.

**Weaknesses:**
- The paper does not sufficiently differentiate its contributions from previous works, particularly those by Qiu et al. (2025), which have already explored similar issues with ES in continual learning.
- The paper lacks a thorough discussion on the causes of catastrophic forgetting in ES, which could be better addressed by including a more detailed analysis or additional experiments.
- The empirical results are not convincing, with some inconsistencies noted between the results presented and those reported in previous studies.
- The paper could benefit from a more comprehensive comparison with other gradient-free algorithms and a broader range of datasets to strengthen its claims.
- The paper's focus on a single dataset (Countdown) for evaluating catastrophic forgetting may not fully capture the multifaceted loss of performance in the model.
- The paper could be improved by including more detailed experimental setups and results, such as the number of rollouts and the specifics of the GRPO implementation used.

**Questions:**
- Can the authors clarify the specific contributions of their work beyond those already addressed in previous studies, particularly those by Qiu et al. (2025)?
- How does the paper's findings on catastrophic forgetting in ES compare to other gradient-free algorithms like GRPO, especially in terms of the mechanisms behind forgetting behavior?
- Could the authors provide more detailed experimental setups, such as the number of rollouts and the specific GRPO implementation used, to enhance the reproducibility and transparency of their results?
- How does the paper's findings on catastrophic forgetting in ES apply to other continual learning scenarios, and what implications do these findings have for the broader adoption of ES in such settings?
- The paper mentions that ES updates are less sparse and have larger L2 norms compared to GRPO. Could the authors elaborate on the implications of these findings for the practical application of ES in continual learning?

**Soundness:**
3 good

**Presentation:**
3 good

**Contribution:**
2 fair

**Rating:**
5 marginally below the acceptance threshold

**Paper Decision:**
- Decision: Accept
- Reasons: The paper provides a valuable contribution to the field by highlighting the issue of catastrophic forgetting in ES, which is a significant concern in continual learning. The empirical analysis is comprehensive, and the findings are well-presented, making the paper accessible and understandable. Despite some concerns about the novelty and depth of the contributions, the paper's findings are relevant and could inspire further research in this area. The decision to accept is based on the paper's potential to stimulate discussion and future work, as well as its alignment with the conference theme. However, the paper could benefit from a more thorough discussion on the causes of catastrophic forgetting and a broader range of datasets to strengthen its claims.