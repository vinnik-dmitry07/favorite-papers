 **Summary:**
The paper investigates the role of reinforcement learning (RL) in improving reasoning capabilities in large language models (LLMs) by focusing on the sparse and predictable nature of RL's beneficial footprint. The authors demonstrate that RL primarily affects a small fraction of token positions, typically those with high entropy, where the model is uncertain about the next token. This observation leads to the development of a novel RL-free method called ReasonMaxxer, which uses contrastive loss at entropy-gated decision points to achieve comparable or better performance than RL-trained models. The method is evaluated across multiple model families and reasoning benchmarks, showing that it can match or surpass RL performance with significantly reduced training costs.

**Strengths:**
- The paper provides a comprehensive analysis of the token-level impact of RL on LLMs, demonstrating that RL primarily affects a small fraction of token positions and is predictable, focusing on high-entropy decision points.
- The authors introduce a novel RL-free method, ReasonMaxxer, which applies contrastive loss at entropy-gated decision points using base model rollouts, achieving comparable or better performance than RL-trained models while reducing training costs.
- The paper is well-written, clear, and easy to follow, with a clear motivation and a well-structured presentation of the findings.
- The experimental results are robust and convincing, showing that the proposed method can achieve comparable or better performance than RL-trained models with significantly reduced training costs.
- The paper provides a detailed analysis of the token-level impact of RL, which is a significant contribution to the field.

**Weaknesses:**
- The paper lacks a thorough analysis of the limitations of the proposed method, particularly in terms of its applicability to other types of reasoning tasks beyond math reasoning.
- The paper does not discuss the potential negative societal impacts of the proposed method, which could be a significant concern for some readers.
- The paper does not compare the proposed method with other RL-free methods that might also achieve similar results, which could provide a more comprehensive evaluation of the proposed method.
- The paper does not provide a detailed discussion on the limitations of the proposed method, which could help in understanding its practical applicability and potential challenges.
- The paper could benefit from a more detailed discussion on the limitations of the proposed method, particularly in terms of its scalability and applicability to different types of reasoning tasks.

**Questions:**
- Can the proposed method be applied to other types of reasoning tasks beyond math reasoning? If so, how does it perform in these domains?
- How does the proposed method compare to other RL-free methods in terms of performance and computational efficiency?
- What are the potential negative societal impacts of the proposed method, and how can these be mitigated?
- Could the authors provide a more detailed discussion on the limitations of the proposed method, particularly in terms of its scalability and applicability to different types of reasoning tasks?
- How does the proposed method compare to other methods that use RL for reasoning tasks, and what are the specific advantages of the proposed method over these approaches?

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
- Reasons: The paper presents a novel and significant contribution to the field by demonstrating that RL's beneficial footprint is sparse and predictable, focusing on high-entropy decision points. The proposed RL-free method, ReasonMaxxer, matches or surpasses RL performance while reducing training costs by three orders of magnitude. The paper is well-written, clear, and easy to follow, with a comprehensive analysis of the token-level impact of RL. The experimental results are robust and convincing, showing that the proposed method can achieve comparable or better performance than RL-trained models with significantly reduced training costs. The paper is a valuable contribution to the field and should be accepted for presentation at the conference.