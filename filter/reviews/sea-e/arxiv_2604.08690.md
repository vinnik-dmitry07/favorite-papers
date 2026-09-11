 **Summary:**
The paper introduces a novel method called Skip-Connected Policy Optimization (SKPO) for training large language models (LLMs) in reinforcement learning with verifiable rewards (RLVR). SKPO decomposes the reasoning process into upstream and downstream phases, employing a skip connection between them to maintain exploration freedom while leveraging upstream reasoning. The upstream phase generates early-stopped reasoning segments and receives Monte Carlo rewards aggregated from downstream continuations, while the downstream phase maintains group-relative optimization. SKPO is evaluated on various benchmarks, demonstrating improvements over existing methods like GRPO and other state-of-the-art algorithms. The method's effectiveness is validated through extensive experiments and ablation studies, showing that SKPO can enhance intermediate-step quality and outperform other algorithms in mathematical reasoning tasks.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation and strong experimental results.
- The proposed method is novel and effective, showing improvements over existing methods like GRPO and other state-of-the-art algorithms.
- The experiments are comprehensive, including ablation studies and analysis of implicit advantages, which demonstrate the effectiveness of the proposed method.
- The paper provides a detailed analysis of the proposed method, including a clear explanation of the upstream and downstream phases and the use of a skip connection to balance exploration freedom and upstream influence.
- The method is evaluated on various benchmarks, showing significant improvements over existing methods, and the results are supported by extensive experiments and ablation studies.

**Weaknesses:**
- The paper lacks a detailed discussion on the limitations of the proposed method, which could provide a more comprehensive understanding of its applicability and potential challenges.
- There is a need for more detailed explanations and examples of the skip connection and its impact on the model's performance.
- The paper could benefit from a more thorough discussion on the choice of parameters such as the number of rollouts and the split position, and how these choices affect the model's performance.
- The paper does not provide a detailed comparison with other state-of-the-art methods, such as those that use different reward structures or optimization techniques.
- The paper could benefit from a more detailed analysis of the computational costs and the impact of different parameter settings on the model's performance.

**Questions:**
- Can the authors provide more details on the limitations of the proposed method and how these might affect its applicability in different scenarios?
- How does the skip connection specifically impact the model's performance, and can the authors provide examples or additional details to illustrate its effects?
- Could the authors clarify the choice of parameters such as the number of rollouts and the split position, and how these choices were determined?
- How does the proposed method compare to other state-of-the-art methods that use different reward structures or optimization techniques?
- Can the authors provide a more detailed analysis of the computational costs and the impact of different parameter settings on the model's performance?

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
- Reasons: The paper presents a novel method, SKPO, which effectively decomposes the reasoning process into upstream and downstream phases, leveraging a skip connection to balance exploration freedom and upstream influence. The method is evaluated on various benchmarks and shows significant improvements over existing methods, supported by extensive experiments and ablation studies. The paper is well-written, clear, and easy to follow, making it accessible to a broad audience. The method's novelty and effectiveness, combined with its potential impact on the field, justify its acceptance. The decision is further supported by the positive feedback from reviewers and the paper's contribution to advancing the understanding and application of reinforcement learning in large language models.