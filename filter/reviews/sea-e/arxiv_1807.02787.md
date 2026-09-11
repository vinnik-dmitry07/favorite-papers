 **Summary:**
The paper introduces a novel approach to financial trading using deep reinforcement learning, specifically a modified version of the deep Q-network (DRQN) algorithm. The authors propose a new action augmentation technique to mitigate the need for random exploration and a smaller replay memory, which is more suitable for the financial trading setting. The methodology is tested on the spot foreign exchange market, demonstrating positive results with an average annual return of 6.4%. The paper also discusses the challenges of applying deep reinforcement learning to financial trading, such as the lack of a clear baseline, data availability, and the need for exploration strategies. Despite these strengths, the paper suffers from several weaknesses including a lack of clarity in methodological details, insufficient comparisons with existing methods, and a limited scope of experiments.

**Strengths:**
- The paper introduces a novel approach to applying deep reinforcement learning to financial trading, which is a significant and relevant problem in the field.
- The authors propose a new action augmentation technique that mitigates the need for random exploration in the financial trading environment, which is a novel contribution to the field.
- The paper is well-written, making it easy to follow, and the authors provide a clear and detailed description of the proposed method.
- The paper demonstrates the effectiveness of the proposed method through empirical results on 12 currency pairs, showing positive results under most simulation settings.
- The authors provide a comprehensive discussion on the challenges of applying deep reinforcement learning to financial trading, which is a valuable contribution to the field.

**Weaknesses:**
- The paper lacks a clear description of the methodology, particularly in sections 2.3 and 2.5.1, which are crucial for understanding the proposed modifications to the DRQN algorithm.
- The paper does not sufficiently compare the proposed method with existing methods, which limits the ability to assess the novelty and effectiveness of the proposed approach.
- The experiments are limited in scope, focusing only on the spot foreign exchange market, which may not generalize well to other financial markets.
- The paper does not adequately address the exploration strategy in the financial trading setting, which is a significant challenge in this domain.
- The paper lacks a detailed discussion on the limitations of the proposed method, which is necessary for a complete understanding of its applicability and effectiveness.
- The paper could benefit from a more comprehensive literature review and a more rigorous evaluation against existing methods to establish the effectiveness and novelty of the proposed approach.

**Questions:**
- Could the authors clarify the methodology, particularly in sections 2.3 and 2.5.1, to provide a clearer explanation of the proposed modifications to the DRQN algorithm?
- How does the proposed action augmentation technique compare to other exploration strategies in the financial trading setting?
- Can the authors provide a more detailed discussion on the limitations of the proposed method and how these limitations affect the applicability and effectiveness of the approach?
- How does the proposed method perform in different financial markets beyond the spot foreign exchange market?
- Could the authors provide a more detailed comparison with existing methods to establish the effectiveness and novelty of the proposed approach?
- How does the proposed method handle the exploration-exploitation trade-off in the financial trading setting, especially in the context of the zero market impact hypothesis?

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
- Reasons: The paper, while introducing an interesting approach to financial trading using deep reinforcement learning, suffers from significant weaknesses. The methodology is not clearly described, and the experiments are limited in scope, focusing only on the spot foreign exchange market. The paper also lacks a thorough comparison with existing methods and fails to adequately address the exploration strategy in the financial trading setting. Furthermore, the paper does not sufficiently discuss the limitations of the proposed method, which is crucial for understanding its applicability and effectiveness. These issues lead to a decision to reject the paper.