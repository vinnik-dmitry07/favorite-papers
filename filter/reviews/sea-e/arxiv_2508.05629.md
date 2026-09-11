 **Summary:**
The paper introduces Dynamic Fine-Tuning (DFT), a novel method aimed at enhancing the generalization of Supervised Fine-Tuning (SFT) in large language models (LLMs) by addressing the issue of sparse rewards in SFT. DFT reweights the gradients based on the probability of tokens, which is akin to importance sampling in reinforcement learning. The method is evaluated across various tasks such as mathematical reasoning, code generation, and multi-modal reasoning, showing improvements over standard SFT. Theoretical insights are provided to justify the method's effectiveness, and the paper includes extensive empirical results to support its claims. Despite its strengths, the paper is criticized for its limited novelty and the need for more comprehensive comparisons with other methods.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation and a well-structured presentation of the methodology.
- The proposed method, Dynamic Fine-Tuning (DFT), is simple yet effective, with a straightforward implementation that can be applied to various tasks.
- The paper provides a clear theoretical analysis of the relationship between SFT and RL, which is a significant contribution to the field.
- Extensive empirical results demonstrate the effectiveness of DFT across multiple tasks and datasets, showing improvements over standard SFT and other baseline methods.
- The paper is well-organized, with a clear structure and logical flow, making it easy for readers to understand the content and the implications of the findings.

**Weaknesses:**
- The paper lacks a comprehensive comparison with other methods, particularly in terms of computational efficiency and the impact of different weighting methods.
- There is a need for more detailed discussion on the limitations of DFT, especially in scenarios where it may not be effective or where it could lead to suboptimal results.
- The paper could benefit from more extensive experiments, including comparisons with other methods like MixCE and GOLD, and evaluations on larger-scale models and more diverse datasets.
- Some sections of the paper, such as the discussion on the limitations of DFT and the comparison with other methods, are not well-integrated into the main text and could be moved to the appendix for better focus.
- The paper could benefit from a more detailed discussion on the theoretical underpinnings of the method, especially in relation to the RL perspective and the implications of the proposed method for broader applications.

**Questions:**
- Could the authors provide more details on the computational efficiency of DFT compared to standard SFT, particularly in terms of training time and resource usage?
- How does the proposed method compare to other methods like MixCE and GOLD, especially in terms of effectiveness and computational efficiency?
- Can the authors provide more insights into the limitations of DFT and scenarios where it may not be effective?
- How does the proposed method perform on larger-scale models, and what are the implications for its applicability in real-world scenarios?
- Could the authors clarify the relationship between the proposed method and other methods that use importance sampling in RL, such as PPO and TRPO?
- How does the proposed method handle the issue of overfitting in SFT, and what are the implications for the model's generalization capabilities?

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
- Reasons: The paper presents a novel method, DFT, that addresses the generalization issues in SFT by reweighting gradients based on token probabilities. The method is supported by both theoretical analysis and extensive empirical results, showing improvements over standard SFT across various tasks. The paper is well-written, clear, and easy to follow, making it accessible to a broad audience. The method's simplicity and effectiveness, coupled with its theoretical justification, make it a significant contribution to the field. However, the paper could benefit from more comprehensive comparisons with other methods and a more detailed discussion on the limitations and implications of the proposed method. Despite these limitations, the paper's strengths outweigh its weaknesses, and the decision to accept is based on the originality of the method, its methodological soundness, and the significance of its results.