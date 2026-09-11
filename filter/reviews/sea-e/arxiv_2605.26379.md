 **Summary:**
The paper investigates the identifiability of latent variables in self-supervised learning (SSL) through the lens of Joint Embedding Predictive Architectures (JEPAs), specifically focusing on the LeJEPA method. It establishes that linear identifiability of latent variables is achievable under certain conditions, such as Gaussian latent variables and stationary, additive noise transitions. The paper provides theoretical proofs and empirical validations, showing that LeJEPA can effectively recover latent variables from nonlinear observations. It also explores the implications of these findings for planning and compositional generalization in SSL, suggesting that linear identifiability is crucial for these applications. The paper is well-received for its clear presentation, rigorous theoretical analysis, and comprehensive experimental validation.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation and a well-structured presentation.
- The authors provide a rigorous theoretical analysis of the LeJEPA method, which is both novel and significant, and the results are supported by comprehensive experiments.
- The paper addresses an important question about the identifiability of latent variables in self-supervised learning, which is crucial for understanding the effectiveness of various self-supervised learning methods.
- The theoretical results are well-supported by experiments, and the paper provides a detailed discussion on the limitations of the approach, which is commendable for its transparency and honesty.
- The paper is well-positioned within the current literature, providing a clear and comprehensive review of related work and a detailed discussion on the limitations of the approach.

**Weaknesses:**
- The paper could benefit from a more detailed discussion on the practical implications of the findings, particularly how the results might be applied in real-world scenarios.
- There is a lack of clarity in some sections of the paper, particularly in the definitions and descriptions of certain terms and assumptions, which could confuse readers.
- The paper does not sufficiently discuss the limitations of the assumptions made in the theoretical analysis, which could affect the generalizability of the results.
- The paper could benefit from a more detailed discussion on the practical implications of the findings, particularly in terms of how they might be applied in real-world scenarios.
- The paper could be improved by including more detailed experimental results and a more comprehensive discussion on the practical implications of the findings.

**Questions:**
- Could you clarify the meaning and implications of the term "linear identifiability" as used in the paper?
- How does the paper's approach compare to other methods for learning world models, such as those based on recurrent neural networks?
- Can you provide more details on the practical implications of the findings, particularly in terms of how they might be applied in real-world scenarios?
- How do the assumptions made in the theoretical analysis affect the generalizability of the results, and what are the potential limitations of these assumptions?
- Could you elaborate on the practical implications of the findings, particularly in terms of how they might be used to improve the performance of self-supervised learning methods?

**Soundness:**
4 excellent

**Presentation:**
3 good

**Contribution:**
4 excellent

**Rating:**
8 strong accept

**Paper Decision:**
- Decision: Accept
- Reasons: The paper is well-received for its clear presentation, rigorous theoretical analysis, and comprehensive experimental validation. It addresses a significant question in the field of self-supervised learning and provides valuable insights into the identifiability of latent variables in SSL. The paper's contributions are substantial, and the findings are expected to have a significant impact on the field. The decision to accept is based on the originality, methodological soundness, significance of results, and clarity and logic of presentation.