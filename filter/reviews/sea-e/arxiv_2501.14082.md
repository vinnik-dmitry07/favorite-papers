 **Summary:**
The paper introduces a novel method for communication between language models (LMs) using activations from intermediate layers, aiming to enhance reasoning abilities and reduce computational costs compared to natural language communication. This method involves combining activations from different LMs and passing them through the next layer, which is shown to improve performance on various tasks, including multi-player coordination games and reasoning benchmarks. The approach is evaluated across different model sizes and architectures, demonstrating its effectiveness and efficiency. However, concerns are raised about the generalizability of the method, particularly in scenarios where the models are not trained on similar data or have different architectures.

**Strengths:**
- The paper presents a novel approach to communication between language models using activations from intermediate layers, which is a significant departure from traditional natural language communication.
- The method is shown to be effective in improving performance on various tasks, including multi-player coordination games and reasoning benchmarks, demonstrating its practical utility.
- The paper is well-written, clear, and easy to follow, making it accessible to a broad audience.
- The method is computationally efficient, which is crucial for large language models (LLMs) that are known for their high computational demands.
- The paper includes a comprehensive evaluation across different model sizes and architectures, which helps to establish the robustness and generalizability of the method.
- The authors provide a detailed analysis of the compute savings achieved by their method, which is a valuable contribution to the field.

**Weaknesses:**
- The paper lacks a detailed comparison with other activation-based methods, such as CALM, which could provide a better understanding of the relative advantages and disadvantages of the proposed method.
- The method's generalizability is questionable, particularly in scenarios where the models are not trained on similar data or have different architectures.
- The paper does not sufficiently address the issue of interpretability, which is a significant concern for many applications of LLMs.
- The method's effectiveness is not convincingly demonstrated in all scenarios, particularly in more complex or varied tasks, which raises questions about its robustness.
- The paper does not sufficiently discuss the limitations of the method, such as the requirement for aligned embedding spaces between models, which could limit its applicability in practical scenarios.
- The paper could benefit from a more detailed discussion on the computational efficiency of the method, particularly in terms of the number of forward passes required and the impact on inference speed.

**Questions:**
- How does the proposed method compare to other activation-based methods, such as CALM?
- Can the method be adapted to work with different model architectures, such as those used in the LLaMA family?
- How does the method perform in scenarios where the models are not trained on similar data or have different architectures?
- What are the specific advantages of using activations from intermediate layers over other types of representations, such as token embeddings?
- How does the method handle the issue of interpretability, particularly in scenarios where the activations are not easily interpretable?
- Can the method be adapted to work with different types of LLMs, such as those trained on different datasets or with different training strategies?
- How does the method perform in more complex or varied tasks, such as those involving multiple rounds of communication or more complex prompts?

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
- Reasons: The paper presents a novel and potentially impactful approach to inter-model communication using activations from intermediate layers, which shows promise in improving performance and reducing computational costs. The method is well-evaluated across various tasks and model sizes, demonstrating its effectiveness and efficiency. However, concerns about its generalizability and the need for further comparisons with other methods were noted. The decision to accept is based on the paper's originality, methodological soundness, and the significant contributions it makes to the field, despite some limitations in its scope and potential applicability in all scenarios. The decision aligns with the reviewers' consensus and the metareview, which highlights the paper's potential impact and the need for further refinement and testing in broader and more varied settings.