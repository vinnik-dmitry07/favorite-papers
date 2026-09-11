 **Summary:**
The paper investigates the optimization of step sizes in continual learning, focusing on the limitations of existing methods like RMSProp and Adam. It proposes a new approach using the Incremental-Delta-Bar-Delta (IDBD) algorithm, which optimizes step sizes based on the objective function. The paper demonstrates that IDBD can outperform RMSProp and Adam in certain scenarios, particularly in weight-flipping and rate-tracking problems. However, it also highlights the sensitivity of IDBD to the meta-step-size parameter and its limited applicability to deep neural networks. The paper suggests that combining normalization and optimization could lead to better step-size adaptation methods in deep networks, but it lacks a comprehensive evaluation on deep networks and does not sufficiently address the computational complexity and sensitivity of IDBD.

**Strengths:**
- The paper is well-written and easy to follow, with clear explanations of the proposed method and its differences from existing methods.
- The authors provide a good analysis of the limitations of existing methods like RMSProp and Adam, and introduce a novel approach using IDBD to optimize step sizes in continual learning.
- The paper presents a clear and intuitive explanation of the IDBD algorithm, which is a significant contribution to the field.
- The experimental results show that IDBD outperforms RMSProp and Adam in certain scenarios, demonstrating its effectiveness.

**Weaknesses:**
- The paper lacks a comprehensive evaluation on deep neural networks, which is a significant limitation given the widespread use of deep networks in continual learning.
- The sensitivity of IDBD to the meta-step-size parameter is not adequately addressed, which could limit its practical application.
- The paper does not sufficiently compare IDBD with other step-size adaptation methods, such as AdaGain, which could provide a more comprehensive evaluation of IDBD's performance.
- The computational complexity of IDBD is not discussed, which is crucial for understanding its practical applicability in deep learning scenarios.
- The paper does not provide a detailed discussion on how IDBD can be extended to deep neural networks, which is a critical aspect for broader applicability.
- The paper does not include a discussion on the limitations of IDBD, which could help in understanding its scope and applicability.

**Questions:**
- Can the authors provide a more detailed discussion on how IDBD can be extended to deep neural networks?
- How does IDBD compare to other step-size adaptation methods, such as AdaGain?
- Can the authors clarify the computational complexity of IDBD and discuss its practical implications in deep learning scenarios?
- How sensitive is IDBD to the meta-step-size parameter, and what measures can be taken to mitigate this sensitivity?
- Could the authors provide a more comprehensive evaluation of IDBD on deep neural networks to validate its effectiveness in more complex scenarios?
- Is there a possibility to combine IDBD with other step-size adaptation methods to improve its performance and applicability?

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
- Reasons: The paper presents an interesting approach to optimizing step sizes in continual learning, but it has significant limitations that prevent its acceptance. The main concerns include the lack of comprehensive evaluation on deep neural networks, the sensitivity of IDBD to the meta-step-size parameter, and the limited discussion on computational complexity. The paper also fails to sufficiently compare IDBD with other step-size adaptation methods and does not provide a detailed discussion on its limitations. These issues, combined with the overall fairness of the presentation and contribution, lead to the decision to reject the paper.