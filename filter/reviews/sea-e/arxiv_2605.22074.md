 **Summary:**
The paper introduces a novel curriculum reinforcement learning (CRL) framework named SCRL, designed to enhance the training of large language models (LLMs) in mathematical reasoning tasks. SCRL decomposes hard problems into a sequence of verifiable subproblems, enabling process-level supervision within a single on-policy rollout. This framework includes a subproblem-level normalization technique for fine-grained credit assignment, which is crucial for training LLMs to solve challenging problems. Theoretical analysis and empirical results demonstrate that SCRL effectively lifts hard problems out of gradient dead zones, showing significant improvements over existing baselines. The paper is well-structured, with clear theoretical and empirical validations, and includes a detailed analysis of the subproblem decomposition and its impact on gradient recovery.

**Strengths:**
- The paper is well-organized, with clear and detailed explanations of the proposed method, making it easy to follow and understand.
- Theoretical analysis is robust, providing a strong foundation for the proposed method, and the empirical results are convincing, showing significant improvements over existing baselines.
- The paper introduces a novel method for curriculum reinforcement learning (CRL) that effectively addresses the challenge of hard problem solving by decomposing problems into a sequence of verifiable subproblems.
- The use of subproblem-level normalization is innovative, enabling fine-grained credit assignment without the need for external rubrics or additional reward models.
- The paper includes a comprehensive analysis of the subproblem decomposition and its impact on gradient recovery, which is crucial for understanding the effectiveness of the proposed method.

**Weaknesses:**
- The paper lacks a detailed discussion on the limitations of the proposed method, which could provide a more balanced view of its applicability and effectiveness.
- The evaluation is limited to mathematical reasoning tasks, and it's unclear whether the method can be applied to other types of reasoning tasks such as commonsense reasoning or question answering.
- The paper does not provide a detailed analysis of the computational cost of the proposed method, which could be a significant concern for practical deployment.
- The paper could benefit from a more detailed discussion on the choice of subproblem difficulty and its impact on the performance of the method.
- The paper does not include a discussion on the potential negative societal impacts of the proposed method, which is an important consideration for any new technology.

**Questions:**
- Could the authors provide a detailed discussion on the limitations of the proposed method and its applicability to other types of reasoning tasks?
- How does the computational cost of the proposed method compare to existing methods, and what are the implications for practical deployment?
- Can the authors provide more details on the choice of subproblem difficulty and its impact on the performance of the method?
- How does the proposed method compare to other methods that use subproblems for curriculum learning, such as those mentioned in related works?
- Could the authors provide a more detailed discussion on the potential negative societal impacts of the proposed method, and how these impacts might be mitigated?

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
- Reasons: The paper presents a novel and effective approach to curriculum reinforcement learning for mathematical reasoning tasks, demonstrating significant improvements over existing baselines. The methodology is well-explained, and the theoretical analysis is robust, providing a strong foundation for the proposed method. The empirical results are convincing, showing that the proposed method can effectively lift hard problems out of gradient dead zones. The paper is well-structured, making it easy to follow, and the inclusion of subproblem-level normalization is a significant contribution to the field. The decision to accept is based on the originality of the approach, methodological soundness, and the significance of the results. The paper is recommended for acceptance, particularly as a poster presentation, to facilitate further discussion and exploration of the proposed method.