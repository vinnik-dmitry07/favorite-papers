 **Summary:**
The paper explores the connection between supervised fine-tuning (SFT) and reinforcement learning (RL) by viewing SFT as a lower bound of the RL objective in a sparse reward setting. It introduces an importance weighted variant, iw-SFT, which optimizes a tighter bound to the RL objective and can improve performance compared to SFT on curated data. The paper demonstrates the effectiveness of iw-SFT through experiments on various benchmarks, including reasoning and control tasks, showing that it can outperform traditional SFT and RL methods in certain scenarios. The authors also discuss the practical implications of these findings, suggesting that iw-SFT could be a valuable tool for improving the performance of large language models (LLMs) and other systems that rely on supervised fine-tuning.

**Strengths:**
- The paper provides a clear and comprehensive explanation of the connection between supervised fine-tuning (SFT) and reinforcement learning (RL), which is crucial for understanding the theoretical underpinnings of these methods.
- The authors have demonstrated that SFT can be seen as optimizing a lower bound on the RL objective in the sparse reward setting, which is a significant contribution to the field.
- The introduction of the importance weighted variant, iw-SFT, offers a novel approach to improving SFT by optimizing a tighter bound to the RL objective, which can lead to better performance in certain scenarios.
- The paper is well-written, making it accessible and easy to follow, which is essential for a broad audience.
- The experiments conducted are thorough and demonstrate the effectiveness of the proposed iw-SFT, showing that it can outperform traditional SFT and RL methods in some cases.
- The paper provides a clear and intuitive explanation of the proposed method, which is crucial for understanding its practical implications and potential applications.

**Weaknesses:**
- The paper could benefit from a more detailed discussion on the limitations and potential negative societal impacts of the proposed method, particularly in terms of its application to large language models (LLMs).
- The experimental results, while promising, are somewhat limited in scope, focusing primarily on a few benchmarks and not comparing the proposed method against a broader range of baselines or in more diverse settings.
- The paper could benefit from a more comprehensive discussion on the practical implications of the proposed method, particularly in terms of its scalability and applicability to different types of datasets and tasks.
- The paper's claims about the superiority of iw-SFT over traditional SFT and RL methods are not consistently supported by the experimental results, which sometimes show only marginal improvements or no significant differences.
- The paper could benefit from a more detailed discussion on the computational costs and scalability of the proposed method, especially in the context of large language models and other complex systems.

**Questions:**
- Could the authors elaborate on the potential negative societal impacts of the proposed method, particularly in the context of large language models?
- How does the proposed method compare to other RL-based methods in terms of computational efficiency and scalability, especially in the context of large language models?
- Could the authors provide more detailed experimental results, including comparisons against a broader range of baselines and in more diverse settings?
- How does the proposed method perform in scenarios where the reference policy is not available, and what are the implications of this for the practical applicability of the method?
- Could the authors discuss the potential applications of the proposed method beyond supervised fine-tuning and reinforcement learning, and how it might be adapted to other domains or tasks?

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
- Reasons: The paper presents a novel perspective on the relationship between supervised fine-tuning and reinforcement learning, which is both theoretically interesting and practically relevant. The proposed method, iw-SFT, offers a tighter bound to the RL objective and shows promising results in various benchmarks. The paper is well-written, making the content accessible and easy to follow, which is crucial for a broad audience. Despite some limitations in the experimental scope and the need for more comprehensive comparisons, the paper's contributions are significant enough to warrant acceptance, especially considering the potential impact on the field. The decision to accept is supported by the metareview, which highlights the paper's originality and methodological soundness.