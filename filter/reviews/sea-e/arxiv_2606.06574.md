 **Summary:**
The paper introduces a novel method called Program-of-Layers (PoLar), which dynamically adjusts the execution of pretrained language models (LLMs) by selectively skipping or repeating layers during inference. This approach is aimed at improving the efficiency and accuracy of LLMs by adapting to the complexity of the input, thereby reducing computational overhead and enhancing performance on mathematical reasoning benchmarks. The method is evaluated on various LLMs and benchmarks, showing consistent improvements over standard inference and prior dynamic-depth methods. The paper also discusses the potential for this method to generalize to out-of-distribution (OOD) scenarios, although the evaluation on such scenarios is limited.

**Strengths:**
- The paper introduces an innovative approach to dynamic inference in large language models (LLMs) by predicting input-specific execution programs, which can be skipped or repeated, without modifying model parameters.
- The method is evaluated on various LLMs and benchmarks, demonstrating consistent improvements over standard inference and prior dynamic-depth methods.
- The paper is well-written, clearly presenting the methodology and results, and includes a comprehensive evaluation across multiple datasets, including out-of-distribution (OOD) scenarios.
- The proposed method is computationally efficient, requiring minimal additional computational overhead and reducing end-to-end latency.
- The paper provides a novel perspective on the latent computation capacity of LLMs, showing that fixed-depth execution captures only a narrow subset of their latent reasoning capacity.
- The method's ability to generalize to OOD scenarios and its potential for reducing computational costs and energy consumption are highlighted.

**Weaknesses:**
- The paper lacks a detailed discussion on the limitations of the proposed method, particularly in terms of its applicability to different types of tasks and its scalability to larger models.
- The evaluation primarily focuses on mathematical reasoning benchmarks, which may not fully demonstrate the method's effectiveness on more complex or varied tasks.
- The paper does not provide a detailed comparison with other dynamic inference methods, such as those that use different routing policies or architectural modifications.
- The method's effectiveness in handling long sequences or complex tasks is not thoroughly evaluated, raising concerns about its scalability and applicability in real-world scenarios.
- The paper does not discuss the potential negative societal impacts of the proposed method, which could be significant given the potential for misuse in generating misleading or harmful content.
- The paper's reliance on Monte Carlo Tree Search (MCTS) for program discovery and its use of a limited set of operations (skip, keep, repeat) may limit the method's expressiveness and flexibility.

**Questions:**
- Can the authors provide more details on the limitations of the proposed method, particularly in terms of its applicability to different types of tasks and its scalability to larger models?
- How does the method perform on more complex or varied tasks beyond mathematical reasoning?
- Could the authors provide a more detailed comparison with other dynamic inference methods, such as those that use different routing policies or architectural modifications?
- How does the proposed method handle long sequences or complex tasks, and what are the implications for its scalability and applicability in real-world scenarios?
- Can the authors discuss the potential negative societal impacts of the proposed method and how these might be mitigated?
- How does the method's performance compare when using different numbers of k candidates, and what are the implications for computational efficiency and accuracy?
- Could the authors provide more details on the training and inference times for the PoLar method, and how these compare to other methods like DR.LLM?

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
- Reasons: The paper presents a novel and effective method for dynamic inference in LLMs, which is both technically sound and has a high impact on at least one sub-area. The method's ability to adapt to the complexity of inputs and reduce computational overhead while maintaining accuracy is commendable. The paper is well-written, clearly presenting the methodology and results, and includes a comprehensive evaluation across multiple datasets, including out-of-distribution scenarios. The reviewers have highlighted the method's potential for reducing computational costs and energy consumption, making it a significant contribution to the field. The decision to accept is based on the paper's originality, methodological soundness, significance of results, and clarity and logic of presentation.