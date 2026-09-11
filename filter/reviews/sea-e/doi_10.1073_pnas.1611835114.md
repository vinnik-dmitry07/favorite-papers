 **Summary:**
The paper introduces Elastic Weight Consolidation (EWC), a novel method aimed at mitigating catastrophic forgetting in neural networks during continual learning. EWC operates by assigning different weights to different parameters based on their importance for specific tasks, thereby preventing the network from forgetting previously learned information. The method is tested on both supervised and reinforcement learning tasks, showing promising results in preventing forgetting while allowing the network to adapt to new tasks. The approach is supported by theoretical justification and empirical evidence, demonstrating its effectiveness in various scenarios. However, concerns are raised about the scalability of the method to more complex tasks and its practical applicability in real-world scenarios.

**Strengths:**
- The paper is well-written and easy to follow, with clear explanations of the methodology and its application to both supervised and reinforcement learning tasks.
- The methodology is novel and innovative, providing a new approach to addressing the catastrophic forgetting problem in neural networks.
- The paper is supported by comprehensive experiments that demonstrate the effectiveness of the proposed method in preventing forgetting and learning new tasks.
- The use of a Fisher information matrix to weight the importance of parameters is a novel and interesting approach.
- The paper is well-organized, with clear figures and detailed experimental setups, which enhance the understanding of the proposed method.
- The method is shown to be effective in both supervised and reinforcement learning settings, and is scalable to a large number of tasks.

**Weaknesses:**
- The paper lacks a detailed discussion on the limitations of the proposed method, particularly in terms of its scalability and applicability to more complex tasks.
- There is a lack of comparison with other methods for continual learning, which could provide a better understanding of the relative performance of the proposed method.
- The paper does not provide a clear explanation of how the method handles the trade-off between forgetting and learning new tasks, which is crucial for understanding its effectiveness.
- The experimental setup and results are not sufficiently detailed, particularly in the reinforcement learning experiments, which makes it difficult to assess the robustness and generalizability of the findings.
- The paper does not adequately address the computational overhead of the proposed method, which could be a significant concern for practical applications.
- The paper could benefit from a more detailed discussion on the biological plausibility of the method, especially in relation to the biological processes it is modeled after.

**Questions:**
- Can the authors clarify how the method handles the trade-off between forgetting and learning new tasks, and provide more details on how this trade-off is managed in practice?
- How does the method perform when applied to more complex tasks, such as those involving natural images or more complex sequential decision-making tasks?
- Could the authors provide more details on the experimental setup and results, particularly in the reinforcement learning experiments, to better understand the robustness and generalizability of the findings?
- How does the method compare to other methods for continual learning, and what are the specific advantages and disadvantages of the proposed method compared to these alternatives?
- Can the authors provide more details on the computational overhead of the proposed method, and discuss potential strategies for reducing this overhead in practical applications?
- How does the method perform when applied to different types of neural network architectures, such as convolutional neural networks or recurrent neural networks?
- Could the authors provide more details on the biological plausibility of the method, and discuss how closely it aligns with the biological processes it is modeled after?

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
- Reasons: The paper presents a novel method for mitigating catastrophic forgetting in neural networks, which is supported by both theoretical justification and empirical evidence. The method is shown to be effective in preventing forgetting while allowing the network to adapt to new tasks, which is a significant contribution to the field of continual learning. Despite some concerns about scalability and practical applicability, the paper is well-written, easy to follow, and provides a comprehensive evaluation of the proposed method. The decision to accept is based on the originality of the approach, methodological soundness, and the significance of the results, as well as the clarity and logic of the presentation. The decision is also influenced by the potential impact of the work on the field, which is highlighted by the paper's innovative approach and the robustness of the experimental results.