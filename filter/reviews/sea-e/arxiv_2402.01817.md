 **Summary:**
The paper explores the limitations of Large Language Models (LLMs) in planning and reasoning tasks, particularly in generating executable plans and verifying their correctness. It argues that LLMs, while capable of generating plans, cannot ensure their executability or correctness without external verification. The authors propose a framework called LLM-Modulo, which integrates LLMs with external model-based verifiers to enhance planning capabilities. This framework allows LLMs to generate plans, which are then verified by external critics, thus improving the overall planning process. The paper also discusses the limitations of LLMs in planning and verification tasks and provides a comprehensive review of related literature.

**Strengths:**
- The paper provides a comprehensive review of the literature on planning and reasoning with Large Language Models (LLMs), highlighting the limitations of LLMs in planning and verification tasks.
- It introduces the LLM-Modulo framework, which integrates LLMs with external model-based verifiers to enhance planning capabilities, providing a novel approach to leveraging LLMs in planning and reasoning.
- The paper is well-written, clear, and easy to follow, with a clear motivation and a well-structured presentation of the proposed framework.
- The proposed framework is a significant contribution to the field, as it addresses the limitations of LLMs in planning and reasoning tasks and provides a practical solution by integrating LLMs with external model-based verifiers.
- The paper is timely and relevant, as it addresses the current interest in using LLMs for planning and reasoning tasks.

**Weaknesses:**
- The paper lacks a detailed discussion on the limitations of the LLM-Modulo framework, particularly in terms of its scalability and applicability to more complex planning problems.
- There is a lack of empirical evidence to support the claims made about the limitations of LLMs in planning and verification tasks.
- The paper does not provide a detailed discussion on the computational complexity of the proposed framework and its scalability to more complex planning problems.
- The paper does not sufficiently discuss the limitations of the proposed framework, such as its inability to handle complex planning problems without human intervention.
- The paper could benefit from a more detailed discussion on how the framework handles the integration of LLMs with external model-based verifiers, particularly in terms of ensuring the correctness and completeness of the plans generated.

**Questions:**
- Can the authors provide more details on the limitations of the LLM-Modulo framework, particularly in terms of its scalability and applicability to more complex planning problems?
- How does the framework handle the integration of LLMs with external model-based verifiers, and what mechanisms are in place to ensure the correctness and completeness of the plans generated?
- Could the authors provide more empirical evidence to support the claims made about the limitations of LLMs in planning and verification tasks?
- How does the proposed framework compare to other neuro-symbolic approaches that integrate LLMs with symbolic planning systems?
- Can the authors discuss the potential societal impacts of using LLMs in planning and reasoning tasks, particularly in terms of automating decision-making processes?

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
- Reasons: The paper provides a clear and well-articulated argument about the limitations of LLMs in planning and reasoning tasks, and proposes a novel framework, LLM-Modulo, to address these limitations. The framework integrates LLMs with external model-based verifiers, enhancing the planning capabilities of LLMs. The paper is well-written, clear, and easy to follow, making it accessible to a broad audience. The reviewers have highlighted the paper's contribution to the field and its potential impact on the development of more effective planning systems. The decision to accept the paper is based on its originality, methodological soundness, significance of results, and clarity and logic of presentation.