 **Summary:**
The paper introduces Test-Time Reinforcement Learning (TTRL), a novel method for training large language models (LLMs) using reinforcement learning on unlabeled data. TTRL employs a majority voting reward function to estimate labels and compute rewards, which are then used to update model parameters. The method is evaluated across various datasets and models, showing consistent improvements in performance. The core idea is to use the majority voting of model outputs as a proxy for ground truth labels, which are then used to compute rewards for training. The paper also discusses the limitations and potential future directions of TTRL, including its scalability and applicability to different types of tasks.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation and a novel approach to test-time training using reinforcement learning.
- The proposed method, TTRL, is simple yet effective, with strong results demonstrated across various models and tasks, showing a significant improvement in performance.
- The paper provides a comprehensive evaluation and analysis, including ablation studies and comparisons with other methods, which supports the robustness and effectiveness of the proposed method.
- The use of majority voting as a reward function is innovative and provides a novel approach to training LLMs without labeled data.
- The paper is well-organized, with clear figures and a logical structure that makes it easy to understand the methodology and results.

**Weaknesses:**
- The paper lacks a detailed discussion on the limitations of TTRL, particularly in terms of its applicability to different types of tasks and its scalability to larger datasets and models.
- The novelty of the method is questioned, as it appears to be a combination of existing techniques without significant innovation.
- The paper does not provide sufficient details on the experimental setup, such as the specifics of the reward function and the training parameters, which could affect the reproducibility and understanding of the results.
- The paper could benefit from a more thorough discussion on the potential negative societal impacts of the proposed method.
- There is a lack of comparison with more recent and relevant works in the field, which could provide a better context for the contributions of the paper.
- The paper does not adequately address the potential for reward hacking, which could undermine the effectiveness of the method.

**Questions:**
- Can the authors clarify the specifics of the reward function, particularly how it is computed and how it affects the training dynamics?
- How does the proposed method compare to other test-time training methods, especially in terms of performance and training dynamics?
- Could the authors provide more details on the experimental setup, such as the training parameters and the specifics of the majority voting process?
- How does the proposed method handle the potential for reward hacking, and what steps have been taken to mitigate this risk?
- Can the authors discuss the potential negative societal impacts of the proposed method, and how these might be mitigated or addressed?
- How does the proposed method scale to larger datasets and models, and what are the potential challenges and limitations in such scenarios?

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
- Reasons: The paper presents a novel and effective method for training LLMs using reinforcement learning on unlabeled data, which is a significant contribution to the field. The method is well-explained, and the results are robust, showing consistent improvements across various models and tasks. The paper is well-written and easy to follow, making it accessible to a broad audience. However, there are some concerns about the novelty and depth of the method, as well as the potential for reward hacking. The decision to accept is based on the paper's potential impact and the overall positive reception by the reviewers, who suggest that these issues could be addressed in future work. The decision also aligns with the metareview, which highlights the paper's strengths and potential for further development.