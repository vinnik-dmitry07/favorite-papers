 **Summary:**
The paper investigates the reasoning hierarchy in large language models (LLMs) trained with reinforcement learning from human feedback (RLHF). It introduces a novel algorithm, Hierarchy-Aware Credit Assignment (HICRA), which focuses on optimizing high-level planning tokens to enhance strategic reasoning in LLMs. The authors propose that LLMs undergo a two-phase learning process, initially focusing on low-level procedural skills and later transitioning to high-level strategic planning. The paper validates these findings through extensive experiments, demonstrating that HICRA outperforms existing methods like GRPO. It also explores the concept of "aha moments" and their correlation with the emergence of strategic planning in LLMs.

**Strengths:**
- The paper introduces a novel approach to understanding the reasoning hierarchy in LLMs, which is a significant contribution to the field.
- The proposed algorithm, HICRA, is well-motivated and effectively demonstrated through extensive experiments, showing superior performance compared to baseline methods.
- The paper is well-written, clear, and easy to follow, making complex concepts accessible to a broad audience.
- The authors provide a comprehensive analysis of the learning dynamics of LLMs, which is crucial for understanding the behavior of LLMs in complex reasoning tasks.
- The paper includes a detailed analysis of the learning dynamics of LLMs, which is beneficial for future research and development in the field.

**Weaknesses:**
- The paper lacks a detailed discussion on the limitations of the proposed method, which could help in understanding the scope and applicability of the findings.
- The definition of "planning tokens" is somewhat arbitrary and could benefit from a more rigorous definition or justification.
- The paper could benefit from a more thorough discussion on the relationship between the proposed method and other existing methods, such as those that use high-entropy tokens as decision points.
- There is a lack of clarity in some sections of the paper, particularly in the definitions and explanations of terms and concepts.
- The paper could benefit from a more detailed discussion on the computational complexity and scalability of the proposed method, especially in larger models.
- The paper's claims about the universality of the reasoning hierarchy in complex reasoning tasks are not well-supported and could benefit from more empirical evidence.

**Questions:**
- Can the authors provide more details on the computational complexity and scalability of the proposed method, especially in larger models?
- How does the proposed method compare to other methods that use high-entropy tokens as decision points?
- Could the authors clarify the definition and role of "planning tokens" in the context of the proposed method?
- How does the proposed method handle the trade-off between exploration and exploitation in the context of LLM reasoning?
- Could the authors elaborate on the relationship between the proposed method and other existing methods, particularly in terms of their contributions to the field?
- How does the proposed method address the issue of strategic errors in LLMs, and what are the implications of these errors for the overall performance of the model?

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
- Reasons: The paper presents a novel approach to understanding and enhancing strategic reasoning in LLMs through the use of a hierarchical credit assignment algorithm. The methodology is well-supported by extensive experiments, demonstrating the effectiveness of the proposed algorithm over existing methods. The paper is well-written, clear, and contributes significantly to the understanding of LLM reasoning dynamics. The reviewers appreciated the novelty of the approach and the clarity of the presentation. The decision to accept is based on the paper's originality, methodological soundness, and the significant impact it could have on the field.