 **Summary:**
The paper investigates the problem of catastrophic forgetting in neural networks by evaluating five distinct methods: regularization, ensembling, rehearsal, dual-memory, and sparse-coding. It employs various datasets including MNIST, CUB-200, and AudioSet, and introduces new metrics to compare these methods. The study reveals that none of the methods completely solve the problem of catastrophic forgetting, suggesting that a combination of these methods might be necessary. However, the paper has been critiqued for its lack of novelty, unclear presentation, and insufficient experimental validation. The methodology is seen as a combination of existing techniques without significant innovation, and the paper's presentation and clarity need improvement.

**Strengths:**
- The paper is well-written and easy to follow, with clear explanations of the methods and experiments.
- It introduces new metrics for measuring catastrophic forgetting, which are useful for evaluating the effectiveness of different methods.
- The paper provides a comprehensive evaluation of various methods for mitigating catastrophic forgetting, including regularization, ensembling, rehearsal, dual-memory, and sparse-coding.
- The experiments are conducted on real-world datasets, which enhances the practical relevance of the study.
- The paper highlights the limitations of existing methods and suggests that a combination of different methods might be necessary to address the problem of catastrophic forgetting.

**Weaknesses:**
- The paper lacks novelty as it primarily combines existing methods without significant innovation.
- The presentation of the paper is unclear and could benefit from better organization and clarity.
- The experimental setup and results are not sufficiently detailed or validated, with some results (e.g., those in Table 2) being unclear or inconsistent.
- The paper does not adequately address the computational costs and memory requirements of the methods being compared, which is crucial for practical applications.
- The paper does not sufficiently discuss the limitations of the proposed methods, nor does it provide a comprehensive review of the existing literature on catastrophic forgetting.
- The paper's claims about the effectiveness of the methods are not convincingly supported by the experimental results, and the results do not clearly demonstrate the superiority of any one method over others.

**Questions:**
- Can the authors clarify the discrepancies in the results, particularly those in Table 2, and explain how the results support the conclusions drawn?
- How do the authors justify the choice of methods and datasets used in the study, and what criteria were used to select these?
- Could the authors provide more detailed explanations of the experimental setup and results, including the computational costs and memory requirements of the different methods?
- How do the authors address the issue of catastrophic forgetting in practical applications, and what are the implications of their findings for real-world systems?
- Can the authors provide a more comprehensive review of the existing literature on catastrophic forgetting, including both its causes and potential solutions?
- How do the authors plan to address the limitations of their study, particularly the lack of novelty and the unclear presentation?

**Soundness:**
2 fair

**Presentation:**
2 fair

**Contribution:**
2 fair

**Rating:**
3 reject, not good enough

**Paper Decision:**
- Decision: Reject
- Reasons: The paper, while addressing an important problem in neural networks, lacks novelty and clarity in its presentation. The methods used are a combination of existing techniques without significant innovation. The experimental setup and results are not convincingly presented, and the paper does not sufficiently address the computational costs and memory requirements of the methods being compared. The paper also does not adequately discuss the limitations of the proposed methods or provide a comprehensive review of the existing literature. These issues, combined with the lack of novelty, lead to the decision to reject the paper.