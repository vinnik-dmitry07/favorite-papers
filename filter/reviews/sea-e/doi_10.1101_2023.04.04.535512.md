 **Summary:**
The paper explores the use of recurrent neural networks (RNNs) in estimating value directly from observations, without the need for explicit belief state estimation. This approach is contrasted with traditional methods that rely on belief state representations. The authors demonstrate that RNNs can learn to estimate value from observations, which resemble the error signals observed in dopamine neurons during similar tasks. The paper also shows that RNNs can implicitly learn belief-like representations, which are crucial for value estimation in partially observable environments. The study is supported by empirical evidence from rodent behavioral experiments, showing that RNNs can perform value estimation tasks effectively without explicit belief state estimation.

**Strengths:**
- The paper is well-written and clearly articulates the problem, methodology, and results, making it accessible and easy to follow.
- The authors provide a detailed analysis of the RNN's learned representations, showing that they resemble belief states, which is a significant contribution to the field.
- The paper is original in its approach, demonstrating that RNNs can learn belief-like representations without explicit training for this purpose, which is a novel finding.
- The experimental design is robust, with multiple experiments and analyses that support the claims made, including the use of rodent behavioral experiments to validate the findings.
- The paper is well-motivated, addressing the question of whether animals use belief states to estimate value in partially observable environments, and provides a compelling answer through the use of RNNs.

**Weaknesses:**
- The paper's scope is somewhat limited, focusing primarily on a single task and not generalizing to other tasks or environments, which could limit the applicability of the findings.
- The use of RNNs as the only model system might limit the generalizability of the findings to other types of neural networks or architectures.
- The paper does not sufficiently discuss the limitations of its approach, such as the potential for overfitting or the scalability of the RNNs to more complex environments.
- The paper could benefit from a more detailed discussion on the computational efficiency and scalability of the RNNs, particularly in terms of the number of hidden units required for effective value estimation.
- The paper does not adequately address the potential for confounding factors in the rodent behavioral experiments, such as the influence of reward magnitude on the results.

**Questions:**
- Could the authors clarify the role of reward magnitude in the rodent behavioral experiments and its potential influence on the results?
- How does the paper address the issue of overfitting in the RNNs, especially given the complexity of the tasks and the number of hidden units used?
- Can the authors provide more details on the computational efficiency and scalability of the RNNs, particularly in terms of the number of hidden units required for effective value estimation in different environments?
- How does the paper address the potential for confounding factors in the rodent behavioral experiments, and what steps were taken to control for these factors?
- Could the authors discuss the potential for extending the findings to other types of neural networks or architectures, and how the results might generalize to different tasks or environments?

**Soundness:**
3 good

**Presentation:**
3 good

**Contribution:**
3 good

**Rating:**
7 accept

**Paper Decision:**
- Decision: Accept
- Reasons: The paper presents a novel approach to value estimation using RNNs, which is both theoretically interesting and empirically validated. The methodology is sound, and the results are well-supported by empirical evidence. The paper is well-written, making it accessible and easy to follow. The reviewers have highlighted the originality of the approach and the robustness of the experimental design. The paper's contribution to the field is significant, particularly in demonstrating that RNNs can learn belief-like representations without explicit training for this purpose. The decision to accept is based on the paper's originality, methodological soundness, and the significance of its results. The paper is recommended for acceptance, with minor improvements suggested for clarity and presentation in the final version.