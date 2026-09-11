 **Summary:**
The paper introduces Go-Explore, a novel reinforcement learning algorithm designed to address the challenges of exploration in sparse reward environments. It employs a two-phase approach: first, it explores by returning to previously visited states and then extending trajectories, and second, it robustifies the learned policy using a learning from demonstrations algorithm. The method is evaluated across various benchmarks, including Atari games and a robotic manipulation task, demonstrating superior performance over existing methods. The authors argue that this approach overcomes challenges like detachment and derailment, which are critical for effective exploration in complex environments. The paper also discusses the potential of Go-Explore in real-world applications, although its applicability and the practicality of its components are questioned.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation and a well-structured presentation of the method.
- The proposed method, Go-Explore, is novel and effective, showing superior performance compared to state-of-the-art methods in various environments such as Atari games and a robotic manipulation task.
- The method is well-motivated and addresses significant challenges in reinforcement learning, particularly the issues of detachment and derailment, which are crucial for effective exploration in complex environments.
- The paper provides a thorough evaluation, including a comparison with state-of-the-art methods and a detailed analysis of the results, which supports the claims made about the effectiveness of the proposed method.
- The method is flexible and can be adapted to different environments, which enhances its applicability and potential for broader use.

**Weaknesses:**
- The paper lacks a detailed discussion on the limitations of the proposed method, which is crucial for understanding its applicability and potential drawbacks.
- The paper's evaluation is somewhat limited, focusing primarily on specific environments and not sufficiently exploring the generalizability of the method across different domains.
- The paper does not sufficiently address the computational cost of the method, which is a significant concern given the potential for high computational demands.
- There is a lack of clarity in the presentation of certain components of the method, such as the robustification phase and the policy-based Go-Explore, which could benefit from more detailed explanations.
- The paper does not adequately address the potential societal impacts of the proposed method, which is a critical consideration for any technology that could be deployed in real-world applications.
- The paper could benefit from a more detailed discussion on the theoretical underpinnings of the method, particularly in relation to existing theories and models.

**Questions:**
- Can the authors provide more details on the limitations of the proposed method and how these might affect its practical applicability?
- How does the method perform in environments where the reward structure is more complex or where the reward function is not well-defined?
- Could the authors clarify the computational cost of the method and discuss potential strategies for reducing this cost without compromising performance?
- In the context of the policy-based Go-Explore, how does the method ensure that the policy is robust and effective in real-world scenarios, particularly in environments where the reward function might not be well-defined or where there are significant variations in the environment?
- How does the method handle the potential for overfitting to the exploration phase, and what measures are in place to prevent this?
- Could the authors provide more details on the theoretical underpinnings of the method and how it relates to existing theories and models in reinforcement learning?

**Soundness:**
3 good

**Presentation:**
3 good

**Contribution:**
3 good

**Rating:**
7 accept, but needs minor improvements

**Paper Decision:**
- Decision: Accept
- Reasons: The paper presents a novel and effective approach to exploration in reinforcement learning, addressing significant challenges in the field. The method, Go-Explore, is well-evaluated and shows superior performance compared to existing methods. The paper is well-written and clearly presents the method and its results. However, there are concerns about the generalizability of the method and the potential for overfitting, which could be addressed with more extensive evaluations and a deeper discussion on the limitations and societal impacts of the proposed method. The decision to accept is based on the paper's originality, methodological soundness, and the significance of its results, although there is a need for minor improvements in clarity and depth of discussion.