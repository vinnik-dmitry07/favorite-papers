 **Summary:**
The paper introduces a novel approach to pre-training large language models (LLMs) using reinforcement learning (RL) from human feedback, specifically focusing on next-token prediction as a reasoning task. This method, termed Reinforcement Pre-Training (RPT), leverages intrinsic rewards derived from the pre-training corpus to minimize reward hacking and promote generalization. The authors demonstrate that RPT improves next-token prediction accuracy and enhances zero-shot performance on various downstream tasks. The approach is evaluated using the OmniMATH dataset and shows promising results, although concerns are raised about the generalizability of the findings due to the limited dataset used.

**Strengths:**
- The paper introduces a novel approach to pre-training large language models (LLMs) using reinforcement learning (RL) from human feedback, which is a significant advancement in the field.
- The proposed method, RPT, is well-motivated and effectively addresses the challenges of scalability and generalization in current RL applications in LLM training.
- The paper is well-written, clear, and easy to follow, with detailed explanations of the methodology and experimental results.
- The experiments demonstrate that RPT significantly improves next-token prediction accuracy and exhibits favorable scaling properties, making it a promising new paradigm for advancing the pre-training of large language models.
- The paper provides a comprehensive evaluation of the proposed method, including a detailed analysis of the reasoning patterns of the model, which is crucial for understanding the effectiveness of the approach.

**Weaknesses:**
- The paper primarily uses the OmniMATH dataset for evaluation, which is a relatively small and specific dataset. The generalizability of the findings to other, more diverse datasets is not thoroughly explored.
- The comparison with other methods is limited, and the paper does not sufficiently discuss the advantages of RPT over other RL methods for LLMs.
- The paper lacks a detailed discussion on the limitations of the proposed method, particularly in terms of its scalability and applicability to different types of datasets.
- The experimental setup and results are not sufficiently robust, with some results (e.g., in Table 3) showing marginal improvements or even declines in performance compared to baseline models.
- The paper does not adequately address the potential for reward hacking in the RPT method, which is a significant concern given the use of rule-based rewards.
- The paper does not sufficiently compare the proposed method with other RL methods for LLMs, which could have provided a more comprehensive understanding of its advantages and limitations.

**Questions:**
- Could the authors provide more details on the generalizability of the findings to other, more diverse datasets?
- How does the proposed method compare to other RL methods for LLMs in terms of performance and scalability?
- Can the authors clarify the differences between RPT and other RL methods, particularly in terms of the reward mechanism and its impact on the model's behavior?
- How does the proposed method address the issue of reward hacking, and what measures have been taken to ensure that the model does not learn to hack the reward system?
- Could the authors provide more detailed results on the scaling properties of RPT, particularly in terms of the model's performance with different amounts of training compute?
- How does the proposed method handle the potential for overfitting, especially in scenarios where the model is trained on a specific dataset?

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
- Reasons: The paper presents a novel approach to pre-training LLMs using RL, which shows promise in improving next-token prediction accuracy and enhancing zero-shot performance on various downstream tasks. The method, while limited in its evaluation to a specific dataset, provides a solid foundation for further research and application in broader contexts. The paper is well-written, clear, and the experimental results are convincing, albeit with some concerns regarding the generalizability and scalability of the findings. The decision to accept is based on the originality of the approach, methodological soundness, and the significance of the results, despite the limitations noted. The paper is recommended for presentation as a poster to allow for further discussion and feedback from the community.