 **Summary:**
The paper introduces SC-GRPO, a novel method for token-level credit assignment in reinforcement learning with verifiable rewards (RLVR). SC-GRPO leverages a self-conditioned teacher constructed from verified trajectories to assign credit based on KL divergence, improving performance over existing methods like GRPO, DAPO, and OPD. The method uses a self-conditioned teacher to condition on verified trajectories, which is then used to weight the GRPO gradient based on the KL divergence between the student and teacher distributions. The paper presents extensive experiments across various benchmarks, demonstrating the effectiveness of the proposed method. However, concerns were raised about the clarity of the paper, particularly in the presentation of the methodology and the experimental results, which could benefit from further clarification.

**Strengths:**
- The paper introduces a novel approach to token-level credit assignment in RLVR, which is a significant contribution to the field.
- The methodology is well-explained, with clear and detailed explanations of the proposed method and its implementation.
- The paper is well-written, making it easy to follow and understand, with a clear presentation of the results and methodology.
- Extensive experiments are conducted across multiple benchmarks, demonstrating the effectiveness of the proposed method.
- The paper provides a comprehensive analysis of the proposed method, including a detailed ablation study and a thorough analysis of the results.
- The use of KL divergence as a multiplicative weight on GRPO gradients is a novel approach that enhances the method's effectiveness.

**Weaknesses:**
- The paper could benefit from better clarity and organization, particularly in the presentation of the methodology and the experimental results.
- There are several typos and grammatical errors throughout the paper that need to be corrected.
- The paper lacks a detailed comparison with the original GRPO method, which could help in understanding the improvements made by the proposed method.
- The paper does not sufficiently discuss the limitations of the proposed method, which could affect the generalizability and applicability of the findings.
- The paper could benefit from a more detailed discussion on the computational overhead and the scalability of the proposed method, especially in terms of its applicability to larger models and more complex tasks.
- The paper could provide more detailed explanations of the experimental setup and the results, including the selection of hyperparameters and the impact of different settings on the results.

**Questions:**
- Can the authors clarify the differences between the proposed method and the original GRPO method, particularly in terms of the use of KL divergence and the group routing strategy?
- How does the proposed method compare to other methods like REINFORCE++ in terms of performance and computational efficiency?
- Could the authors provide more details on the selection of hyperparameters and their impact on the results?
- How does the proposed method perform on longer sequences, and what are the implications of using different normalization thresholds?
- Can the authors provide more detailed explanations of the experimental setup and the results, including the selection of hyperparameters and the impact of different settings on the results?
- How does the proposed method handle the computational overhead, and what are the implications for scalability to larger models and more complex tasks?

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
- Reasons: The paper presents a novel approach to token-level credit assignment in RLVR, which is a significant contribution to the field. The method, SC-GRPO, shows promising results across multiple benchmarks, demonstrating its effectiveness and robustness. The reviewers appreciated the clarity of the paper and the thoroughness of the experiments. However, concerns were raised about the clarity of the presentation and the need for more detailed comparisons with existing methods. The decision to accept is based on the paper's originality, methodological soundness, and the significant impact it could have on the field. The decision also takes into account the potential for further improvements suggested by the reviewers, which could enhance the paper's clarity and impact.