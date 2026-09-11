 **Summary:**
The paper introduces Single-stream Policy Optimization (SPO), a novel approach to optimize policy gradients in Large Language Models (LLMs) by replacing group-based methods with a single-stream method. SPO employs a KL-adaptive value tracker to estimate the success probability of prompts, normalizes advantages globally across the batch, and uses prioritized sampling for adaptive curriculum. This method aims to address the limitations of group-based methods, such as frequent degenerate groups and synchronization barriers, by providing a more stable, low-variance learning signal. The paper presents empirical results demonstrating that SPO outperforms Group Relative Policy Optimization (GRPO) across various math benchmarks, showing improvements in signal efficiency and stability.

**Strengths:**
- The paper is well-written, clear, and easy to follow, making it accessible to a broad audience.
- The proposed method, Single-stream Policy Optimization (SPO), is a principled approach that addresses the limitations of group-based methods in LLMs, specifically the frequent degenerate groups and synchronization barriers.
- SPO is shown to outperform GRPO on various math benchmarks, demonstrating its effectiveness in practical applications.
- The paper provides a detailed analysis of the advantages of SPO over GRPO, including signal efficiency and stability, and presents empirical results that support these claims.
- The use of a Bayesian tracker to estimate the success probability of prompts and the global advantage normalization scheme are innovative and contribute to the stability and efficiency of the learning process.

**Weaknesses:**
- The paper lacks a detailed comparison with other recent methods like A*PO, which could provide a more comprehensive evaluation of SPO's performance.
- The experimental results are limited to a single model (Qwen3-8B), which may not generalize well to other models.
- The paper does not discuss the limitations of SPO in detail, which could help in understanding its applicability and potential drawbacks.
- There is a lack of discussion on the scalability of SPO with larger models, which is crucial for its practical implementation in real-world scenarios.
- The paper does not provide a detailed analysis of the computational cost of SPO compared to GRPO, which could be important for understanding the efficiency of the proposed method.
- The paper could benefit from a more detailed discussion on the limitations of the group-based methods and how SPO addresses these limitations.

**Questions:**
- Could the authors provide a more detailed comparison with other recent methods like A*PO to provide a more comprehensive evaluation of SPO's performance?
- How does SPO perform with larger models, and what are the potential challenges or limitations in scaling up the method?
- What are the specific computational costs of SPO compared to GRPO, and how do these costs impact the practical implementation of the method?
- Can the authors discuss the limitations of SPO in more detail, including potential drawbacks or challenges in its implementation?
- How does SPO perform in scenarios where the reward is not binary, and what modifications, if any, are necessary for such scenarios?
- Could the authors provide a more detailed discussion on the limitations of group-based methods and how SPO addresses these limitations?

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
- Reasons: The paper introduces a novel approach to optimize policy gradients in LLMs, addressing the limitations of group-based methods with a single-stream method that provides a more stable, low-variance learning signal. The empirical results demonstrate that SPO outperforms GRPO on various math benchmarks, showing improvements in signal efficiency and stability. The paper is well-written, clear, and easy to follow, making it accessible to a broad audience. The methodological soundness and significance of the results are evident, and the paper contributes to the field by proposing a more efficient and effective approach to policy optimization in LLMs. The decision to accept is based on the originality of the approach, methodological soundness, significance of results, and clarity and logic of presentation.