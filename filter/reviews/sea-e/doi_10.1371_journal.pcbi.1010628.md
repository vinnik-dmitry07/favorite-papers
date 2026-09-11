 **Summary:**
The paper explores the phenomenon of catastrophic forgetting in spiking neural networks (SNNs) using a reinforcement learning approach. It investigates how sleep-like mechanisms, such as unsupervised STDP, can mitigate forgetting by allowing the network to reactivate and replay memories during offline periods. The study employs a 3-layer SNN trained on two complementary tasks, demonstrating that interleaving training with sleep-like periods can prevent catastrophic forgetting. The authors propose that this approach aligns with how the brain manages multiple tasks, suggesting that sleep might play a crucial role in memory consolidation and learning in neural networks.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear and concise presentation of the findings.
- The study addresses a significant and relevant problem in the field of neural networks, specifically focusing on the phenomenon of catastrophic forgetting.
- The experimental setup is well-designed, with a focus on a 3-layer SNN that effectively demonstrates the proposed mechanisms.
- The paper provides a detailed analysis of the synaptic weights and their dynamics, which is crucial for understanding the underlying mechanisms of the observed effects.
- The paper is original in its approach, combining reinforcement learning with STDP and unsupervised learning during sleep, which is a novel contribution to the field.
- The paper is well-motivated by the biological plausibility of the mechanisms used, which enhances its relevance and applicability to real-world neural systems.

**Weaknesses:**
- The paper lacks a comprehensive discussion on the limitations of the study, which could help in understanding the scope and applicability of the findings.
- The experimental setup and the choice of parameters, such as the number of layers and the specific STDP rules used, are not sufficiently justified or explained.
- The paper does not include a comparison with other methods for mitigating catastrophic forgetting, which could provide a more robust evaluation of the proposed approach.
- The paper could benefit from a more detailed discussion on the biological plausibility of the mechanisms used, particularly in relation to the specific STDP rules and the sleep-like mechanisms.
- The paper does not sufficiently address the scalability of the proposed mechanisms to larger or more complex networks, which is a critical concern for practical applications.
- The paper could benefit from a more rigorous analysis of the synaptic weights and their dynamics, particularly in terms of how they relate to the observed effects and the underlying mechanisms.

**Questions:**
- Could you clarify the role and significance of the non-functional center neuron in the output layer?
- How does the paper address the issue of catastrophic forgetting in the context of larger or more complex networks?
- Could you provide more details on the specific STDP rules used and their biological plausibility?
- How do the authors justify the choice of parameters, such as the number of layers and the duration of sleep periods, in the context of the biological plausibility of the model?
- Could you elaborate on the decision to use a specific STDP rule for sleep and how it contributes to the observed effects?
- How does the paper address the potential limitations and challenges in scaling the proposed mechanisms to larger or more complex networks?
- Could you provide more details on the biological plausibility of the mechanisms used, particularly in relation to the specific STDP rules and the sleep-like mechanisms?

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
- Reasons: The paper presents a novel approach to addressing catastrophic forgetting in spiking neural networks by integrating sleep-like mechanisms, which is both biologically plausible and theoretically sound. The experimental setup is well-designed, and the results are clearly presented, supporting the claims made. The paper also contributes to the ongoing discussion on the role of sleep in neural network learning and memory consolidation. However, the paper could benefit from a more detailed discussion on the limitations and potential challenges in scaling the proposed mechanisms to larger or more complex networks. The decision to accept is based on the paper's originality, methodological soundness, and the significance of its results, despite some concerns regarding the presentation and depth of discussion in certain areas.