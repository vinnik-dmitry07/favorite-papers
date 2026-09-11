 **Summary:**
The paper introduces a novel prioritized replay mechanism for experience replay in reinforcement learning, specifically designed for DQN algorithms. This method prioritizes transitions with high TD error, which are expected to contribute significantly to learning. The authors propose a stochastic sampling method to balance the importance of different transitions, and demonstrate the effectiveness of this approach through experiments on the Atari benchmark. The paper also discusses the potential of this method in other domains such as supervised learning and off-policy RL. However, concerns were raised about the novelty of the approach, the lack of comprehensive experimental validation, and the clarity of the presentation.

**Strengths:**
- The paper is well-written, easy to follow, and provides a clear motivation for the proposed method.
- The proposed method is simple, intuitive, and effective, as demonstrated by its performance on the Atari benchmark.
- The paper includes a thorough discussion of prioritized replay and its potential applications in various domains, including supervised learning and off-policy RL.
- The authors have conducted extensive experiments to evaluate the performance of their method, showing that it can improve performance in many Atari games.
- The paper provides a detailed analysis of the performance of the proposed method, including a comparison with uniform sampling and a discussion on the impact of different hyperparameters.

**Weaknesses:**
- The paper lacks a comprehensive comparison with other prioritized replay methods, which limits the evaluation of the proposed method's effectiveness.
- The experimental results are not convincing, particularly in terms of the statistical significance of the improvements and the generalizability of the results across different environments.
- The paper does not adequately address the scalability of the method to larger environments or the impact of different hyperparameters on its performance.
- The paper's claims about the novelty of the method are questionable, as similar methods have been previously proposed in the literature.
- The presentation of the paper could be improved, particularly in terms of clarity and organization, especially in the experimental results section.
- There is a lack of discussion on the limitations of the proposed method, which is crucial for understanding its applicability and effectiveness in different scenarios.

**Questions:**
- Can the authors clarify the definition and role of the exponent α in the paper, especially in relation to the priority of transitions?
- How does the proposed method compare with other prioritized replay methods, such as those mentioned in the literature?
- Could the authors provide more details on the experimental setup, including the hyperparameters used and the statistical significance of the results?
- How does the method perform in larger environments, such as those with more complex state and action spaces?
- Can the authors discuss the potential limitations of the proposed method and how these might affect its applicability in different scenarios?
- How does the method handle the trade-off between exploration and exploitation, especially in environments where the optimal policy is not known?
- Could the authors provide more details on the implementation of the method, including the specifics of the binary heap data structure and the sampling from the priority queue?

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
- Reasons: The paper presents a novel approach to prioritized replay in reinforcement learning, which is well-received for its simplicity and effectiveness, as demonstrated through experiments on the Atari benchmark. Despite some concerns regarding the novelty and the depth of experimental validation, the reviewers generally agree that the paper is well-written and contributes to the field by proposing a method that could potentially improve learning efficiency in RL algorithms. The decision to accept is based on the paper's potential to advance the understanding and application of prioritized replay in RL, and the overall positive reception of the method by the reviewers. However, the decision is tempered by the need for more comprehensive experimental validation and a clearer presentation of the results to solidify the claims made in the paper.