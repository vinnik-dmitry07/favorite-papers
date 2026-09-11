 **Summary:**
The paper introduces SIM-CoT, a novel method aimed at enhancing the performance of implicit Chain-of-Thought (CoT) models by integrating step-level supervision during training. This approach aligns each implicit token with its corresponding explicit reasoning step, thereby stabilizing the training process and improving the interpretability of implicit reasoning. The methodology involves the use of an auxiliary decoder to project latent tokens onto an explicit reasoning vocabulary, which is removed during inference to maintain efficiency. SIM-CoT has been tested on various models, including GPT-2 and LLaMA, and has shown significant improvements in in-domain accuracy and out-of-domain stability. The paper also includes extensive ablation studies and experiments to validate the effectiveness of the proposed method.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation and a well-defined problem.
- The proposed method, SIM-CoT, is novel and innovative, providing a new approach to implicit CoT methods by integrating step-level supervision during training.
- The method is simple, efficient, and effective, with strong empirical results that demonstrate its effectiveness in improving the performance of implicit CoT methods.
- The paper includes comprehensive ablation studies and experiments, which validate the effectiveness of the proposed method and provide insights into its impact on different model sizes.
- The use of an auxiliary decoder to align implicit tokens with explicit reasoning steps is a novel and effective approach that enhances the interpretability of implicit reasoning.

**Weaknesses:**
- The paper lacks a detailed comparison with other implicit CoT methods, particularly those that do not use step-level supervision, which could provide a clearer understanding of the advantages of SIM-CoT.
- The paper does not discuss the limitations of the proposed method, which could provide a more balanced view of its capabilities and potential challenges.
- The paper could benefit from more detailed analysis and discussion of the results, particularly in the main text rather than relegating some content to the appendix.
- The paper does not address the scalability of the method to larger models, which could limit its applicability in more complex or larger-scale scenarios.
- The paper could benefit from a more thorough discussion of the limitations of the proposed method, particularly in terms of its scalability and applicability to different types of reasoning tasks.

**Questions:**
- Can the authors provide a more detailed comparison with other implicit CoT methods, particularly those that do not use step-level supervision?
- How does the proposed method perform when scaled to larger models, and what are the potential challenges or limitations in doing so?
- Could the authors discuss the potential limitations of the proposed method and how they might affect its practical application?
- How does the method perform when applied to different types of reasoning tasks, such as those involving natural language processing or more complex mathematical problems?
- Can the authors provide more detailed insights into the training process and the role of the auxiliary decoder in aligning implicit tokens with explicit reasoning steps?

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
- Reasons: The paper introduces a novel method, SIM-CoT, which effectively addresses the instability issues in implicit CoT models by integrating step-level supervision during training. The method is well-received for its clarity, simplicity, and empirical effectiveness. The reviewers have highlighted the paper's clear presentation, novel approach, and strong experimental results. Despite some concerns regarding the scalability of the method to larger models and the depth of comparison with other methods, the overall consensus is that the paper makes a valuable contribution to the field and should be accepted, particularly in a poster format to allow for further discussion and refinement.