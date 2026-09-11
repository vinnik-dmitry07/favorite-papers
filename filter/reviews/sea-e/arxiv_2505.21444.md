 **Summary:**
The paper explores the application of self-training in large language models (LLMs) through a novel method called Self-Rewarded Training (SRT), which utilizes majority voting as a self-feedback mechanism. This approach allows LLMs to learn from their own judgments, potentially improving their reasoning performance and generating better quality feedback for the next RL iteration. However, the paper also highlights the risks of reward hacking and model collapse when training is prolonged. The experiments are conducted on both synthetic and real reasoning tasks, demonstrating the effectiveness of SRT in improving model performance. The paper also discusses the potential for curriculum-based self-training to enable models to climb progressively harder tasks without ground-truth labels.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation and a well-designed experimental setup.
- The experiments are comprehensive, covering various aspects of the proposed method, and the results are convincing, demonstrating the effectiveness of the proposed method.
- The paper introduces a novel approach to self-training in LLMs using majority voting as a self-feedback mechanism, which is a significant contribution to the field.
- The findings are well-supported by empirical evidence, showing that the proposed method can improve model performance and provide better quality feedback for the next RL iteration.
- The paper provides a detailed analysis of the limitations of the self-training paradigm, highlighting the critical challenge of feedback design and calling for future research to address this issue.

**Weaknesses:**
- The paper lacks a detailed discussion on the limitations of the proposed method, particularly the potential for reward hacking and model collapse.
- The experiments are limited to reasoning tasks, and it is unclear whether the proposed method can be generalized to other types of tasks.
- The paper does not compare the proposed method with other self-improvement methods, which could provide a more comprehensive understanding of its effectiveness.
- The paper does not discuss the computational efficiency of the proposed method, which is crucial for practical applications.
- The paper does not provide a detailed discussion on the limitations of the proposed method, particularly the potential for reward hacking and model collapse.
- The paper does not compare the proposed method with other self-improvement methods, which could provide a more comprehensive understanding of its effectiveness.
- The paper does not discuss the computational efficiency of the proposed method, which is crucial for practical applications.

**Questions:**
- Can the proposed method be generalized to other types of tasks beyond reasoning?
- How does the proposed method compare with other self-improvement methods in terms of effectiveness and computational efficiency?
- What are the specific reasons for the model collapse observed in the experiments, and how can this be prevented or mitigated?
- How does the proposed method compare with other methods that use majority voting as a self-feedback mechanism, particularly in terms of computational efficiency and effectiveness?
- Can the authors provide more details on the computational efficiency of the proposed method, especially in terms of training time and resource requirements?
- How does the proposed method handle the potential for reward hacking, and what steps can be taken to prevent or mitigate this issue?

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
- Reasons: The paper presents a novel approach to self-training in LLMs using majority voting as a self-feedback mechanism, which is both innovative and well-executed. The experiments are comprehensive and demonstrate the effectiveness of the proposed method, showing improvements in model performance and the ability to generate better quality feedback for the next RL iteration. The paper also addresses the critical challenge of feedback design and calls for future research to address this issue. The reviewers appreciate the clarity and depth of the paper, and the experimental results are convincing. The decision to accept is based on the originality of the approach, methodological soundness, and the significance of the results. The paper is recommended for acceptance, with minor improvements suggested for clarity and depth in certain sections.