 **Summary:**
The paper introduces Q-Learning with World Models (QWM), a novel approach that integrates world models with Q-learning to enhance sample efficiency in reinforcement learning (RL) tasks. QWM leverages a world model to perform test-time search over imagined trajectories, selecting high-value actions during both online rollouts and evaluation. This method is evaluated on the Robomimic and LIBERO benchmarks, demonstrating significant improvements over existing methods. The approach involves constructing a search tree with multiple actions and states, evaluating each node using a Q-function, and pruning nodes based on their value. The paper also discusses the computational overhead and the need for high-quality world models, which are critical for the method's effectiveness.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation for using world models to improve sample efficiency in reinforcement learning tasks.
- The proposed method, Q-Learning with World Models (QWM), is novel and innovative, combining the strengths of world models with Q-learning to enhance performance.
- The paper provides a comprehensive evaluation of the proposed method, comparing it against various baselines and demonstrating its effectiveness in improving sample efficiency.
- The use of a world model to enhance Q-learning is a novel approach that has the potential to significantly impact the field of reinforcement learning.
- The paper is well-organized, with a clear structure and logical flow, making it easy to understand the proposed method and its implications.

**Weaknesses:**
- The paper lacks a detailed discussion on the computational overhead of the proposed method, which could be a significant limitation in practical applications.
- There is a lack of clarity regarding the specifics of the world model used, such as its architecture and training details, which could affect the reproducibility and understanding of the results.
- The paper does not adequately address the limitations of the proposed method, particularly the need for high-quality world models and the potential for compounding model bias.
- The paper could benefit from a more detailed discussion on the scalability of the method, especially in terms of the number of actions and the complexity of the tasks.
- There are some minor issues with the presentation, such as unclear notation and a lack of clarity in some sections, which could be improved for better comprehension.

**Questions:**
- Could the authors provide a more detailed discussion on the computational overhead of the proposed method?
- How does the proposed method compare to other model-based RL methods, particularly in terms of computational efficiency and sample efficiency?
- Can the authors elaborate on the specifics of the world model used, including its architecture and training details?
- How does the proposed method handle the potential for compounding model bias, and what steps are taken to mitigate this risk?
- Could the authors clarify the notation and terminology used in the paper to improve readability and understanding?
- How does the proposed method scale with an increasing number of actions, and what are the implications for the complexity of the tasks?

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
- Reasons: The paper presents a novel approach to integrating world models with Q-learning, which shows promise in improving sample efficiency in reinforcement learning tasks. The method is well-evaluated on standard benchmarks and demonstrates significant improvements over existing methods. The paper is well-written and the methodology is clear, making it accessible to a broad audience. However, there are concerns about the computational overhead and the need for high-quality world models, which could limit the practical applicability of the method. The decision to accept is based on the paper's novelty, methodological soundness, and the significant impact it could have on the field of reinforcement learning. The decision also aligns with the reviewers' consensus that the paper is a good fit for a poster presentation at the conference.