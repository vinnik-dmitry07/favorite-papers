 **Summary:**
The paper investigates the extrapolation capabilities of neural networks, focusing on both feedforward and graph neural networks (GNNs). It provides theoretical insights into the extrapolation behavior of ReLU MLPs, showing that they converge to linear functions in the Neural Tangent Kernel (NTK) regime. The study further explores how GNNs, such as those with min-aggregation, can effectively extrapolate in certain tasks, particularly those involving dynamic programming. The paper also discusses the conditions under which MLPs and GNNs can extrapolate well, emphasizing the importance of diverse training distributions and the encoding of task-specific non-linearities. The theoretical framework is supported by empirical evidence, demonstrating the practical implications of these findings.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear structure that makes it accessible to a broad audience.
- The study of extrapolation in neural networks is an important and relevant topic, and the paper provides a novel perspective on the extrapolation capabilities of MLPs and GNNs.
- The paper provides both theoretical insights and empirical evidence, which are well-supported by the results and analysis.
- The paper is original in its approach, particularly in the analysis of extrapolation in the context of neural networks, and offers a fresh perspective on the limitations and potential of neural networks in extrapolating beyond their training data.
- The paper is well-organized, with a clear presentation of the problem and a logical flow of ideas, making it easy to follow and understand.

**Weaknesses:**
- The paper primarily focuses on the behavior of ReLU MLPs in the NTK regime, which may not generalize well to other activation functions or different network architectures.
- The empirical results are somewhat limited, focusing on specific tasks and datasets, which may not fully demonstrate the generalizability of the findings.
- The paper could benefit from a more comprehensive discussion on the limitations of the results and the assumptions made, particularly regarding the generalizability of the findings to other types of neural networks and datasets.
- There is a lack of discussion on the practical implications of the theoretical results, which could be more clearly articulated to enhance the paper's impact.
- The paper could be improved by including more diverse datasets and tasks to better demonstrate the generalizability of the findings.

**Questions:**
- Can the results be extended to other activation functions or different network architectures?
- How do the findings relate to other out-of-distribution settings, such as domain adaptation or self-supervised learning?
- What are the practical implications of the theoretical results, and how can they be applied in real-world scenarios?
- How does the paper address the limitations discussed, particularly the assumptions made and the generalizability of the results?
- Could the authors provide more detailed examples or case studies to illustrate the practical applications of the theoretical insights?

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
- Reasons: The paper provides a significant contribution to the understanding of extrapolation in neural networks, particularly in the context of MLPs and GNNs. It offers both theoretical insights and empirical evidence, which are well-supported and clearly presented. The paper is well-received by the reviewers, who appreciate its originality and the clarity of its presentation. The decision to accept is based on the paper's originality, methodological soundness, and the significance of its results, as well as the clarity and logic of its presentation. The decision aligns with the overall positive feedback from the reviewers and the conference's criteria for acceptance.