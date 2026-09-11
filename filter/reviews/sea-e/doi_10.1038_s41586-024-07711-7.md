 **Summary:**
The paper explores the phenomenon of plasticity loss in deep learning models, particularly in continual learning settings. The authors demonstrate that standard deep learning methods, such as those using backpropagation, gradually lose their ability to learn new tasks effectively, leading to a decline in performance. This issue is attributed to the uniformity and inactivity of neurons in the network, which reduces the diversity of representations. To address this, the paper introduces a novel algorithm called continual backpropagation, which periodically reinitializes a fraction of the least-used neurons to maintain plasticity. This approach is tested across various datasets and learning scenarios, including supervised and reinforcement learning, showing that continual backpropagation can effectively mitigate plasticity loss.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation and a well-structured presentation of the results.
- The experiments are extensive and cover a wide range of settings, including supervised and reinforcement learning, and different datasets, which demonstrates the robustness of the findings.
- The paper provides a thorough analysis of the causes of plasticity loss in deep learning, including the increase in the fraction of dead units and the growth of network weights.
- The proposed method of continual backpropagation is novel and effective, as shown by its ability to maintain plasticity in deep learning models.
- The paper is significant in its contribution to the field of continual learning, addressing a critical issue of plasticity loss and proposing a practical solution.

**Weaknesses:**
- The paper lacks a detailed discussion on the limitations of the proposed method, particularly in terms of its applicability to different network architectures and the scalability of the results.
- There is a lack of comparison with other continual learning algorithms, which could have provided a more comprehensive evaluation of the proposed method.
- The paper does not sufficiently address the computational cost of the continual backpropagation algorithm, which could be a significant drawback in practical applications.
- The paper could benefit from a more detailed discussion on the theoretical underpinnings of the plasticity loss observed in deep learning models.
- The paper could be improved by including more detailed experimental results and comparisons, particularly in terms of the performance of continual backpropagation on different datasets and architectures.

**Questions:**
- Could the authors provide more details on the computational cost of the continual backpropagation algorithm and compare it with other continual learning algorithms?
- How does the continual backpropagation algorithm perform on different network architectures, such as convolutional networks?
- Could the authors provide more detailed experimental results, including the performance of continual backpropagation on different datasets and the impact of varying hyperparameters?
- How does the continual backpropagation algorithm compare to other methods that maintain plasticity in deep learning models, such as those using L2 regularization or other methods?
- Can the authors discuss the theoretical implications of their findings and the potential for further research in this area?

**Soundness:**
3 good

**Presentation:**
3 good

**Contribution:**
3 good

**Rating:**
8 accept, good paper

**Paper Decision:**
- Decision: Accept
- Reasons: The paper presents a significant contribution to the field of continual learning by identifying the issue of plasticity loss in deep learning models and proposing a novel algorithm, continual backpropagation, to address this issue. The experimental results are robust and demonstrate the effectiveness of the proposed method across various settings. The paper is well-written, clear, and provides a thorough analysis of the causes of plasticity loss. The decision to accept is based on the originality of the approach, the methodological soundness, and the significance of the results. The paper is recommended for acceptance, possibly as a poster presentation to allow for further discussion and feedback.