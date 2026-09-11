 **Summary:**
The paper investigates the effectiveness of alternative learning rate schedules for large language model (LLM) training, specifically focusing on a constant learning rate with a cooldown phase. This approach is contrasted with the traditional cosine learning rate schedule, which is commonly used in the field. The authors demonstrate that the constant learning rate schedule, when combined with a cooldown, can achieve similar performance to the cosine schedule, potentially reducing the computational cost and complexity of training. The study also explores the use of stochastic weight averaging (SWA) and a schedule-free optimizer (SFO) to further enhance the training process. The paper provides empirical evidence that these methods can be as effective as the cosine schedule while reducing the number of training runs required, thus making scaling experiments more efficient.

**Strengths:**
- The paper presents a novel approach to training large language models (LLMs) by proposing a constant learning rate with a cooldown phase, which is a significant departure from the traditional cosine learning rate schedule.
- The methodology is supported by a comprehensive set of experiments across different model sizes and training durations, demonstrating the effectiveness and reliability of the proposed approach.
- The paper is well-written, clear, and easy to follow, making it accessible to a broad audience.
- The findings have practical implications, particularly in reducing the number of training runs required for scaling experiments, which is a significant contribution to the field.
- The paper is well-motivated, with a clear focus on reducing the complexity of scaling experiments and improving the efficiency of training.

**Weaknesses:**
- The paper lacks a detailed discussion on the computational cost of the proposed method, which is crucial for understanding its practical applicability.
- The experimental results are not sufficiently robust, with some figures (e.g., Figure 10) showing significant fluctuations that could affect the reliability of the results.
- The paper does not adequately address the impact of the cooldown phase on the overall training process, particularly in terms of its effectiveness and the potential for improved performance.
- There is a lack of discussion on the limitations of the proposed method, which could help in understanding its applicability and scope.
- The paper does not provide a detailed analysis of the optimization landscape during the cooldown phase, which is crucial for understanding the behavior of the model during this period.
- The paper does not compare the proposed method with other state-of-the-art methods, which could help in understanding its relative performance and effectiveness.

**Questions:**
- Could the authors provide a more detailed discussion on the computational cost of the proposed method, including the number of training runs and the overall computational resources required?
- How does the proposed method perform in terms of convergence speed and stability compared to the cosine learning rate schedule?
- Can the authors provide a more detailed analysis of the optimization landscape during the cooldown phase, particularly in terms of the loss surface and the behavior of the model parameters?
- How does the proposed method compare with other state-of-the-art methods in terms of performance and efficiency?
- Could the authors clarify the discrepancies in the results shown in Figure 10 and discuss the potential impact of these fluctuations on the reliability of the results?
- How does the proposed method perform in terms of generalization to different data distributions, and what are the implications of this for the practical application of the method?

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
- Reasons: The paper presents a novel approach to training LLMs by challenging the traditional cosine learning rate schedule with a constant learning rate and cooldown phase. The experimental results demonstrate that this approach can achieve similar performance with reduced computational cost, making it a significant contribution to the field. The methodology is well-supported by empirical evidence and the paper is well-written, making it accessible and easy to follow. Despite some concerns regarding the robustness of the results and the need for a more detailed discussion on the computational cost, the paper's novelty and potential impact on the field justify its acceptance. The decision to accept is further supported by the positive feedback from the reviewers and the paper's alignment with the conference's themes.