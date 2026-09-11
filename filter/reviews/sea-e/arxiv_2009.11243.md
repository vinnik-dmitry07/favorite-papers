 **Summary:**
The paper introduces a novel hierarchical learned optimizer designed to train neural networks on various tasks without the need for manual hyperparameter tuning. This optimizer, trained on a diverse set of tasks, demonstrates improved generalization and robustness compared to traditional methods. It utilizes a derivative-free optimization method, evolutionary strategies, to manage the computational complexity of the bilevel optimization problem. The optimizer's architecture includes an LSTM network that processes per-tensor and per-parameter features, which are crucial for its effectiveness. The paper also explores the optimizer's performance on a wide range of tasks, including training itself from scratch, and compares it against various baseline optimizers. Despite its strengths, the paper faces criticism for its limited evaluation on large-scale datasets and its computational efficiency.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation and a novel approach to training learned optimizers.
- The proposed method is original and demonstrates significant improvements in generalization and robustness compared to previous works.
- The paper includes a comprehensive evaluation of the proposed method, comparing it against various baseline optimizers and demonstrating its superior performance in terms of generalization and robustness.
- The use of derivative-free optimization and the inclusion of additional task information such as validation loss are innovative approaches that enhance the performance of the learned optimizer.
- The paper's methodology is sound, and the results are convincing, showing that the learned optimizer can generalize well to unseen tasks and even train itself from scratch.

**Weaknesses:**
- The paper lacks a detailed discussion on the computational complexity of the proposed method, which is crucial for understanding its practical applicability.
- The evaluation of the learned optimizer is limited to smaller datasets, and it would be beneficial to see how it performs on larger, more complex datasets such as ImageNet.
- The paper does not provide a detailed comparison of the computational efficiency of the proposed method against other learned optimizers, which could help in understanding its practical advantages.
- The paper could benefit from a more detailed discussion on the limitations of the proposed method, including its scalability and the potential for overfitting to the training distribution.
- The paper's presentation could be improved by providing more detailed explanations of the experimental setup and results, particularly in the appendix.

**Questions:**
- Could the authors provide more details on the computational complexity of the proposed method and how it scales with the size of the training dataset?
- How does the proposed method compare in terms of computational efficiency and practical applicability to other learned optimizers, especially in terms of training time and memory requirements?
- Can the authors elaborate on the limitations of the proposed method and discuss potential strategies for addressing these limitations?
- How does the learned optimizer perform on larger, more complex datasets such as ImageNet, and what are the implications of its performance on such datasets?
- Could the authors provide more details on the experimental setup and results, particularly in the appendix, to enhance the clarity and comprehensibility of the paper?

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
- Reasons: The paper presents a novel and innovative approach to training learned optimizers, which shows promise in improving generalization and robustness. The methodology is sound, and the results are convincing, demonstrating the effectiveness of the proposed optimizer across various tasks. While there are concerns about the computational complexity and the need for more extensive evaluations on larger datasets, the paper's contributions are significant enough to warrant acceptance, especially considering the potential impact on the field. The decision aligns with the reviewers' consensus and the metareview, which highlights the paper's originality and the potential for significant future research.