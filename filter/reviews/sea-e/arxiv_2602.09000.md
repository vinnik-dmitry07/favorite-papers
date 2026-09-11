 **Summary:**
The paper introduces a novel method called Iterative Group Relative Policy Optimization (iGRPO), which extends the Group Relative Policy Optimization (GRPO) method by incorporating a self-feedback mechanism. This method involves two stages: in the first stage, multiple drafts are generated and evaluated, and the best one is selected. In the second stage, the selected draft is used to condition the next generation of drafts, which are then evaluated and refined. The iGRPO method is tested across various mathematical reasoning benchmarks and shows consistent improvements over GRPO and other baseline methods. The paper also includes theoretical analysis and empirical evidence to support the effectiveness of iGRPO.

**Strengths:**
- The paper is well-written, clear, and easy to understand, with a clear motivation and a well-designed methodology.
- The proposed method, iGRPO, is simple yet effective, and the experiments are comprehensive, including ablations that demonstrate the effectiveness of the method.
- The paper provides a theoretical analysis of the proposed method, which is useful for understanding its operation.
- The method is novel and shows good performance on mathematical reasoning tasks, with a simple yet effective approach that is easy to implement.
- The paper is well-organized and the writing is clear, making it accessible to readers.

**Weaknesses:**
- The paper lacks a detailed discussion on the limitations of the proposed method, which could help in understanding its applicability and potential drawbacks.
- The experimental setup and results are not sufficiently detailed, particularly in terms of the specifics of the experiments and the statistical significance of the results.
- The paper does not adequately compare the proposed method with other relevant baselines, such as those mentioned in related works, which could have provided a more robust evaluation of the method.
- The paper could benefit from a more thorough discussion of the computational costs and the efficiency of the method, especially in terms of the number of samples required for optimal performance.
- The paper could be improved by including more detailed visualizations and explanations of the experimental results, particularly in the appendix.

**Questions:**
- Can the authors provide more details on the experimental setup, such as the specifics of the datasets used and the training conditions?
- How does the proposed method compare with other baselines, particularly those mentioned in related works?
- Could the authors clarify the computational costs and efficiency of the method, especially in terms of the number of samples required for optimal performance?
- How does the method perform in terms of generalization to other tasks beyond mathematical reasoning?
- Could the authors provide more detailed visualizations or explanations of the experimental results, particularly in the appendix?
- How does the method handle the potential for overfitting, especially in scenarios where the model is trained on a single dataset?

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
- Reasons: The paper presents a novel method, iGRPO, which extends GRPO by incorporating a self-feedback mechanism, showing consistent improvements over GRPO and other baseline methods. The method is well-explained, and the experiments are comprehensive, including ablations that demonstrate the effectiveness of the method. The paper is well-written, clear, and easy to understand, making it accessible to readers. The decision to accept is based on the originality of the method, methodological soundness, significance of results, and clarity and logic of presentation. However, the paper could benefit from a more detailed discussion on the limitations of the proposed method and a more thorough comparison with other baselines. The decision to accept is also influenced by the overall positive feedback from the reviewers, who have highlighted the paper's strengths and the potential impact of the method.