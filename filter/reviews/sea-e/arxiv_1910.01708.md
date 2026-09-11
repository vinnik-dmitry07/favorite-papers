 **Summary:**
The paper investigates the performance of various off-policy and batch reinforcement learning algorithms in the Atari domain, specifically focusing on the batch setting where agents learn from a fixed dataset without interacting with the environment. It benchmarks several algorithms including BCQ, KL-Control, and DQN, and introduces a discrete variant of BCQ to address the challenges of batch learning. The paper demonstrates that the proposed BCQ outperforms other algorithms in this setting, although it underperforms compared to online DQN and the behavioral policy. The study also explores the extrapolation error in batch settings and its impact on algorithm performance.

**Strengths:**
- The paper addresses an important and relevant problem in the field of reinforcement learning, specifically the application of off-policy and batch reinforcement learning algorithms in discrete action spaces.
- The introduction of a discrete variant of BCQ is a significant contribution to the field, providing a novel approach to address the challenges of batch learning.
- The paper is well-written, clear, and easy to follow, making it accessible to a broad audience.
- The experimental setup is well-designed, comparing various algorithms under a unified setting, which is crucial for understanding the performance of different methods in similar conditions.
- The paper provides a comprehensive review of existing batch reinforcement learning algorithms, which is beneficial for readers seeking a deeper understanding of the current state of the field.

**Weaknesses:**
- The paper lacks a thorough analysis of the extrapolation error in batch settings, which is a significant issue in this context. More detailed exploration of this error and its impact on algorithm performance would strengthen the paper.
- The paper does not sufficiently differentiate its contributions from previous works, particularly in terms of novelty and methodological advancements.
- The experimental setup is limited to a single behavioral policy, which may not fully capture the complexity and variability of real-world scenarios.
- The paper does not adequately address the scalability of the proposed methods to more complex environments or the generalizability of the findings to other domains.
- The paper could benefit from a more rigorous comparison with other baselines, such as those mentioned in the review, to provide a more comprehensive evaluation of the proposed methods.

**Questions:**
- Could the authors provide more details on the extrapolation error observed in batch settings and its impact on algorithm performance?
- How does the proposed BCQ variant compare to other batch reinforcement learning algorithms like BEAR-QL and SPIBB-DQN, especially in terms of performance and computational efficiency?
- What are the specific advantages of the discrete BCQ over other methods like DQN, especially in terms of computational requirements and performance?
- How does the paper address the issue of hyperparameter tuning, which is crucial for the performance of many batch reinforcement learning algorithms?
- Can the authors clarify the discrepancies in performance between the proposed BCQ and the baseline algorithms, particularly in terms of the experimental setup and the choice of hyperparameters?

**Soundness:**
3 good

**Presentation:**
3 good

**Contribution:**
2 fair

**Rating:**
6 marginally above the acceptance threshold

**Paper Decision:**
- Decision: Accept
- Reasons: The paper presents a well-structured benchmarking study that contributes to the understanding of batch reinforcement learning in discrete action spaces. The introduction of a discrete variant of BCQ is a significant contribution, and the paper is well-written and easy to follow. Despite some limitations such as the lack of a thorough analysis of extrapolation error and the need for more comprehensive comparisons with other baselines, the paper provides valuable insights into the performance of various algorithms in batch settings. The decision to accept is based on the paper's originality, methodological soundness, and the significance of its results, although it requires minor improvements to address the noted weaknesses.