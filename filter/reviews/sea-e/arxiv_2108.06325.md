 **Summary:**
The paper investigates the performance of backpropagation in continual learning settings, particularly focusing on the degradation of backpropagation's ability to adapt over time. The authors propose a novel algorithm, Continual Backprop (CBP), which continuously injects random features alongside gradient descent using a generate-and-test process. This approach aims to address the issue of backpropagation's effectiveness in non-stationary environments by maintaining the benefits of random initialization throughout the learning process. The paper presents experiments across various continual learning tasks, including semi-stationary supervised learning, online permuted MNIST, and non-stationary reinforcement learning, demonstrating the utility of CBP in adapting to changing conditions. However, concerns are raised about the practicality of the proposed method, the clarity of the experimental setup, and the robustness of the results, particularly in more complex and realistic scenarios.

**Strengths:**
- The paper addresses the significant issue of backpropagation's inability to adapt in non-stationary environments, which is crucial for continual learning.
- The proposed Continual Backprop (CBP) algorithm is innovative, utilizing a generate-and-test process to maintain the benefits of random initialization throughout learning, which is a novel approach.
- The paper is well-written, clear, and easy to follow, making it accessible to a broad audience.
- The experiments conducted are comprehensive, covering various continual learning tasks and demonstrating the utility of CBP in adapting to changing conditions.
- The paper provides a thorough analysis of the performance of backpropagation in continual learning, which is a significant contribution to the field.

**Weaknesses:**
- The paper lacks a clear and concise summary of the proposed method, which could make it difficult for readers to grasp the core contributions quickly.
- The experimental setup and results are not convincingly robust or practical. The experiments are limited to simple and idealized scenarios, and the results are not convincingly superior to existing methods like L2 regularization.
- The paper does not adequately address the issue of catastrophic forgetting, which is a significant challenge in continual learning.
- The paper's claims about the degradation of backpropagation's ability to adapt over time are not well-supported by the experiments, and the results are not convincingly superior to existing methods.
- The paper's presentation could be improved, particularly in terms of clarity and organization, especially in the experimental sections.
- The paper does not sufficiently discuss the limitations of the proposed method, which is crucial for understanding its applicability and potential drawbacks.

**Questions:**
- Can the authors clarify the experimental setup, particularly the number of non-stationarities and the specifics of how the experiments were conducted?
- How does the proposed method compare to other continual learning methods, especially in terms of performance and practical applicability?
- Could the authors provide more details on the generate-and-test process and the utility measures used in the CBP algorithm?
- How does the paper address the issue of catastrophic forgetting, and what are the implications of this for the practical application of the proposed method?
- Can the authors provide more detailed results and comparisons, especially in more complex and realistic scenarios, to better demonstrate the effectiveness of the CBP algorithm?
- How does the paper ensure that the proposed method is scalable and practical for real-world applications, particularly in terms of computational resources and memory requirements?

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
- Reasons: The paper, while addressing an interesting problem and proposing a novel approach, suffers from significant issues in practicality, clarity, and robustness of the experimental results. The proposed method, while innovative, lacks a clear demonstration of its practical utility and effectiveness in more complex and realistic scenarios. The experimental setup and results are not convincingly robust, and the paper does not adequately address the issue of catastrophic forgetting, which is crucial in continual learning. Furthermore, the presentation of the paper could be improved to better communicate the contributions and findings to the audience. These issues lead to the decision to reject the paper at this stage.