 **Summary:**
The paper introduces Coconut, a novel method for reasoning in large language models (LLMs) by utilizing the last hidden state of the LLM as a continuous thought representation, which is then fed back as the next input embedding. This approach, termed "continuous thought," allows the model to perform a breadth-first search (BFS) during inference, potentially enhancing reasoning capabilities. The method is evaluated on various datasets, including ProsQA, GSM8k, and ProntoQA, showing promising results in terms of accuracy and efficiency. The paper also introduces a new dataset, ProsQA, specifically designed for this method, and discusses the potential of latent reasoning in LLMs.

**Strengths:**
- The paper introduces a novel approach to reasoning in LLMs by utilizing the last hidden state as a continuous thought representation, which is a significant departure from traditional methods.
- The method is well-motivated, with a clear and well-written presentation that effectively communicates the proposed method and its implications.
- The empirical results are robust, demonstrating the effectiveness of the method across various datasets and tasks, including the newly introduced ProsQA dataset.
- The paper provides a detailed analysis of the reasoning process, including the use of visualizations and ablation studies, which help in understanding the method's operation and its impact on model performance.
- The method's potential for reducing the number of tokens generated during inference is highlighted, which could lead to more efficient reasoning processes.

**Weaknesses:**
- The paper lacks a thorough discussion on the limitations of the proposed method, particularly in terms of its scalability and applicability to different types of reasoning tasks.
- The novelty of the method is questioned, as similar approaches have been explored in previous works, such as those using pause tokens or latent reasoning.
- The paper does not sufficiently address the computational overhead and training efficiency of the proposed method, which could be a significant concern for practical applications.
- There is a lack of clarity in some sections of the paper, particularly in the explanation of the training procedure and the role of the "bot" token in the latent mode.
- The paper could benefit from a more comprehensive comparison with existing methods, including a broader range of baselines and a more detailed discussion on the method's performance relative to these baselines.

**Questions:**
- Can the authors clarify the role and operation of the "bot" token in the latent mode, particularly how it is used to mark the beginning of the latent thought mode?
- How does the proposed method compare to other methods that use pause tokens or latent reasoning, especially in terms of scalability and performance?
- Could the authors provide more details on the computational overhead and training efficiency of the proposed method, including the time and resources required for training and inference?
- How does the method perform on more complex or open-ended reasoning tasks, and what are the implications of using different numbers of continuous thoughts in these scenarios?
- Can the authors elaborate on the method's potential for scaling to pretraining and its generalization across different types of reasoning tasks?

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
- Reasons: The paper presents a novel approach to reasoning in LLMs, which is both innovative and well-executed. The method, Coconut, offers a promising alternative to traditional methods by utilizing the last hidden state as a continuous thought representation, enabling a breadth-first search during inference. The empirical results demonstrate the method's effectiveness across various datasets, and the paper is well-written, making the methodology and results clear and accessible. Despite some concerns regarding the novelty and depth of the discussion on limitations, the overall contribution and impact of the paper justify its acceptance. The decision aligns with the reviewers' consensus and the metareview's recommendation, which highlights the paper's potential to advance the field of LLM reasoning.