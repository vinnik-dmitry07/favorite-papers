 **Summary:**
The paper introduces Group Sequence Policy Optimization (GSPO), a novel reinforcement learning algorithm designed to address the instability issues in training large language models, particularly in the context of Mixture-of-Experts (MoE) models. GSPO modifies the GRPO algorithm by replacing token-level importance ratios with sequence-level importance ratios, aiming to improve training stability and efficiency. This change is supported by theoretical and empirical evidence, showing that GSPO outperforms GRPO in various benchmarks and scenarios. The paper also discusses the practical implications of GSPO in real-world applications, such as in the Qwen3 models. Despite its strengths, the paper is criticized for its limited novelty and the lack of comprehensive experiments, particularly in terms of comparing GSPO with other algorithms and exploring its performance in different settings.

**Strengths:**
- The paper is well-written, easy to follow, and provides a clear explanation of the proposed algorithm, GSPO, and its modifications to GRPO.
- The motivation behind the proposed algorithm is well-articulated, and the paper is structured to effectively communicate the key ideas and contributions.
- The empirical results are promising, showing that GSPO outperforms GRPO in terms of training stability, efficiency, and performance.
- The paper includes a detailed gradient analysis, which helps in understanding the algorithm's behavior and effectiveness.
- The proposed algorithm, GSPO, is innovative and addresses a significant issue in the field of reinforcement learning for language models, specifically the instability in training large models.

**Weaknesses:**
- The paper lacks a comprehensive comparison with other algorithms, particularly those that use sequence-level importance ratios, which could have provided a more robust validation of GSPO's effectiveness.
- The experiments are limited in scope, focusing primarily on the Qwen3 model and not exploring how GSPO performs with other models or in different settings.
- The paper does not sufficiently discuss the limitations of the proposed algorithm, which could help in understanding its applicability and potential drawbacks.
- The paper could benefit from a more detailed discussion on the computational complexity and memory requirements of GSPO compared to GRPO.
- The paper does not provide sufficient empirical evidence to support the claims made about the stability and efficiency of GSPO, particularly in terms of its impact on the stability of Mixture-of-Experts (MoE) training.

**Questions:**
- Could the authors provide a more detailed comparison of GSPO with other algorithms that use sequence-level importance ratios?
- How does GSPO perform when applied to other models, and what are the key findings?
- Can the authors discuss the limitations of GSPO and provide more empirical evidence to support the claims made about its stability and efficiency?
- How does GSPO compare in terms of computational complexity and memory requirements compared to GRPO?
- Could the authors clarify the experimental setup, particularly the use of different clipping ranges for GSPO and GRPO, and the impact of these differences on the results?
- How does the proposed algorithm handle the issue of model collapse, and what are the implications for the stability and convergence of the training process?

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
- Reasons: The paper introduces a novel algorithm, GSPO, which addresses a significant issue in training large language models, particularly in the context of MoE models. The algorithm's modification from GRPO to GSPO, focusing on sequence-level importance ratios, is supported by both theoretical and empirical evidence, showing improvements in training stability and efficiency. The paper is well-written, making it accessible and easy to understand. However, the paper could benefit from a more comprehensive comparison with other algorithms and a broader range of experiments to validate its claims more robustly. Despite these limitations, the paper's contribution to the field and its potential impact justify its acceptance, particularly as a poster presentation.