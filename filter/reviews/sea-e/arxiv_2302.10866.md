 **Summary:**
The paper introduces Hyena, a novel attention-free architecture for large language models (LLMs) that utilizes a combination of implicitly parametrized long convolutions and data-controlled gating. This architecture aims to address the quadratic complexity of attention mechanisms in LLMs by replacing them with a subquadratic alternative. The authors claim that Hyena can achieve comparable performance to attention-based models with significantly reduced computational costs. The paper presents various experiments across different tasks, including language modeling and image classification, demonstrating the effectiveness of Hyena in handling long sequences and reducing computational requirements. However, concerns were raised regarding the clarity of the paper's presentation, the lack of comprehensive comparisons with other attention-free models, and the need for more detailed experimental results and theoretical analysis.

**Strengths:**
- The paper introduces a novel attention-free architecture for large language models (LLMs) that utilizes implicitly parametrized long convolutions and data-controlled gating, which is a significant advancement in the field.
- The proposed Hyena architecture is shown to be effective in handling long sequences, reducing computational requirements, and achieving comparable performance to attention-based models.
- The paper is well-written, with clear explanations of the proposed method and its implementation, making it accessible to readers.
- The experiments conducted are extensive, covering various tasks such as language modeling, image classification, and recall/induction benchmarks, demonstrating the versatility and effectiveness of the Hyena architecture.
- The paper provides a thorough analysis of the computational complexity and efficiency of the Hyena architecture, which is crucial for understanding its practical implications.

**Weaknesses:**
- The paper lacks a detailed comparison with other attention-free models such as AFT, GSS, and H3, which could help in understanding the relative advantages and disadvantages of the Hyena architecture.
- The presentation of the paper could be improved, particularly in terms of clarity and organization, especially in the introduction and related work sections.
- The paper does not provide a detailed discussion on the limitations of the Hyena architecture, which could help in understanding its applicability and potential drawbacks.
- There is a lack of comprehensive experimental results, especially in terms of training details and hyperparameter settings, which could affect the reproducibility and comparability of the results.
- The paper does not include a detailed discussion on the scalability of the Hyena architecture to larger model sizes or different types of tasks, which could limit its practical applicability.

**Questions:**
- Could the authors provide a more detailed comparison with other attention-free models such as AFT, GSS, and H3, including a discussion on the relative advantages and disadvantages of each approach?
- How does the Hyena architecture perform in terms of inference speed and memory usage compared to attention-based models, and what are the implications for practical deployment?
- Can the authors provide more detailed experimental results, including training details and hyperparameter settings, to enhance the reproducibility and comparability of the results?
- How does the Hyena architecture scale to larger model sizes, and what are the potential challenges or limitations in applying it to different types of tasks or domains?
- Could the authors clarify the role and impact of the FFN in the Hyena architecture, particularly in terms of its contribution to the overall performance and computational efficiency?

**Soundness:**
3 good

**Presentation:**
2 fair

**Contribution:**
3 good

**Rating:**
6 marginally above the acceptance threshold

**Paper Decision:**
- Decision: Accept
- Reasons: The paper introduces a novel attention-free architecture for LLMs that addresses the quadratic complexity of attention mechanisms, which is a significant issue in large-scale models. The proposed Hyena architecture shows promising results in reducing computational requirements while maintaining comparable performance to attention-based models. The paper is well-written, with clear explanations and extensive experiments that demonstrate the effectiveness of the proposed method. However, there are concerns about the clarity of presentation, the lack of comprehensive comparisons with other attention-free models, and the need for more detailed experimental results and theoretical analysis. Despite these shortcomings, the paper's contributions are substantial enough to warrant acceptance, particularly in a poster format where the presentation issues may be less critical. The decision to accept is also supported by the positive feedback from reviewers regarding the novelty and potential impact of the work.