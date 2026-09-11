 **Summary:**
The paper investigates the overestimation issue in the Q-learning algorithm, focusing on the DQN variant, which is known to overestimate action values. The authors propose an adaptation of the Double Q-learning algorithm, termed Double DQN, to address this issue. They demonstrate that Double DQN significantly reduces overestimation and enhances performance in various Atari 2600 games, showing improvements over the original DQN. The paper also provides theoretical insights into the overestimation problem and empirical evidence supporting the effectiveness of Double DQN.

**Strengths:**
- The paper addresses a significant issue in the field of reinforcement learning (RL) by focusing on the overestimation problem in Q-learning, which is crucial for understanding and improving the performance of RL algorithms.
- The authors provide a clear and concise explanation of the overestimation issue and its impact on RL algorithms, which is helpful for both theoretical and practical understanding.
- The proposed Double DQN algorithm is shown to be effective in reducing overestimation and improving performance in various Atari 2600 games, as demonstrated through empirical results.
- The paper is well-written, making it accessible and easy to follow, which is essential for a broad audience.
- The theoretical analysis provided is robust, offering insights into the overestimation problem and its implications, which is crucial for advancing the field of RL.

**Weaknesses:**
- The paper lacks a detailed discussion on the limitations of the proposed Double DQN algorithm, which is crucial for understanding its applicability and effectiveness in various scenarios.
- The empirical results are not sufficiently comprehensive, as the paper does not include results on all 57 games from the original DQN paper, which could have provided a more complete evaluation of the algorithm's performance.
- The paper does not sufficiently compare Double DQN with other state-of-the-art RL algorithms, which could have provided a clearer picture of its advantages and disadvantages.
- The paper could benefit from a more detailed discussion on the computational complexity and memory requirements of Double DQN compared to other algorithms, which is crucial for practical implementation.
- The paper does not adequately address the generalizability of the findings beyond the specific games tested, which could limit the perceived applicability of the results.

**Questions:**
- Can the authors provide a detailed discussion on the limitations of Double DQN and its applicability in various scenarios?
- Why were only 49 games from the original DQN paper included in the evaluation, and what were the reasons for excluding the remaining games?
- Could the authors provide a more detailed comparison of Double DQN with other state-of-the-art RL algorithms to clarify its advantages and disadvantages?
- How does Double DQN perform in terms of computational complexity and memory requirements compared to other algorithms, and what are the implications of these differences for practical implementation?
- Can the findings of this paper be generalized beyond the specific games tested, and if not, what are the implications of this limitation?

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
- Reasons: The paper addresses a significant issue in the field of RL by investigating the overestimation problem in Q-learning and proposing a solution through Double DQN. The empirical results demonstrate the effectiveness of this approach in reducing overestimation and improving performance in various Atari 2600 games. The paper is well-written, making it accessible and easy to follow, which is essential for a broad audience. Despite some limitations in the comprehensiveness of the empirical results and the discussion on the limitations of Double DQN, the paper provides valuable insights and contributes to the ongoing research in RL. The decision to accept is based on the paper's originality, methodological soundness, and the significance of its results, as well as the clarity and logic of its presentation.