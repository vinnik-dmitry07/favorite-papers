 **Summary:**
The paper introduces Cache-to-Cache (C2C), a novel approach for inter-model communication in multi-Large Language Model (LLM) systems. C2C leverages key-value caches to facilitate direct semantic transfer between models, improving performance and efficiency over traditional text-based communication methods. The method involves projecting and fusing the caches of source and target models, with a learnable gating mechanism to selectively incorporate beneficial layers. The approach is demonstrated to achieve higher accuracy and faster inference times across various LLMs and tasks, showcasing its potential for enhancing multi-LLM systems.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation and a well-designed method.
- The proposed method is simple, effective, and well-motivated, with a focus on using key-value caches for inter-model communication, which is a novel approach.
- The paper includes comprehensive ablation studies and analysis, demonstrating the effectiveness of the proposed method and its components.
- The experiments are conducted on a variety of models and tasks, showing consistent improvements over baselines and providing detailed analysis of the method's behavior.
- The paper introduces a new paradigm for direct semantic communication between LLMs, which is a significant contribution to the field.

**Weaknesses:**
- The paper lacks a detailed comparison with other multi-LLM communication methods, such as those mentioned in the related work section.
- The paper does not discuss the limitations of the proposed method, such as its applicability to different model sizes and the potential for overfitting to specific training sets.
- The paper does not provide a detailed analysis of the computational cost of the proposed method, which is crucial for practical implementation.
- The paper does not compare the proposed method with other recent related works, such as those that use key-value caches for inference acceleration.
- The paper does not discuss the potential negative societal impacts of the proposed method, which is a standard requirement for ethical considerations.

**Questions:**
- Could you provide a comparison with other multi-LLM communication methods, such as those mentioned in the related work section?
- How does the proposed method perform when applied to different model sizes, and what are the implications for overfitting to specific training sets?
- What is the computational cost of the proposed method, and how does it compare to other inference acceleration methods?
- Can you discuss the potential negative societal impacts of the proposed method, and how these might be mitigated?
- How does the proposed method compare to other recent related works that use key-value caches for inference acceleration?

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
- Reasons: The paper introduces a novel and effective method for inter-model communication in multi-LLM systems, which is supported by thorough experiments and analysis. The approach of using key-value caches for direct semantic transfer is innovative and has shown significant improvements in performance and efficiency. The paper is well-written, making it accessible and easy to understand, and the experimental results are convincing. The reviewers have highlighted the novelty and potential impact of the proposed method, and the authors have addressed the concerns raised in the rebuttal. The decision to accept is based on the paper's originality, methodological soundness, significance of results, and clarity and logic of presentation.