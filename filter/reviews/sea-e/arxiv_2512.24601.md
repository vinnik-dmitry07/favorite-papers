 **Summary:**
The paper introduces Recursive Language Models (RLMs), a novel inference-time scaling technique that allows large language models (LLMs) to process arbitrarily long prompts by treating them as part of an external environment. This approach enables LLMs to programmatically examine, decompose, and recursively call themselves over snippets of the prompt, thereby extending their context window beyond typical limits. The RLM framework is evaluated across various tasks and models, demonstrating its ability to handle long-context reasoning effectively, outperforming traditional LLMs in some cases. The paper also explores the use of RLMs in recursive calls and their impact on performance, providing insights into their potential for handling complex, long-context tasks.

**Strengths:**
- The paper introduces a novel approach to handling long contexts in LLMs by treating prompts as part of an external environment, which is a significant advancement in the field.
- The proposed Recursive Language Model (RLM) framework is well-motivated, well-explained, and evaluated across various tasks, showing promising results.
- The paper is well-written, clear, and easy to understand, making it accessible to a broad audience.
- The experiments are well-designed, showing that RLM can handle long-context tasks effectively and outperform vanilla LLMs in some cases.
- The paper provides a detailed analysis of the RLM trajectories, which is insightful and adds depth to the understanding of the model's behavior.

**Weaknesses:**
- The paper lacks a detailed discussion on the limitations of the proposed RLM framework, which is crucial for understanding its applicability and potential drawbacks.
- The evaluation of the RLM framework is limited to a few models, which might not fully demonstrate its effectiveness across different models.
- The paper does not provide a detailed comparison of the inference costs of RLM with other methods, which is essential for understanding its practical applicability.
- The paper does not discuss the limitations of the proposed method, such as the potential for recursive calls to become unbounded or the impact of the REPL on performance.
- The paper does not provide a detailed analysis of the RLM trajectories, which could be more insightful if presented in a tabular format.
- The paper does not discuss the limitations of the proposed method, such as the potential for recursive calls to become unbounded or the impact of the REPL on performance.

**Questions:**
- How does the RLM framework compare in terms of inference costs with other methods, especially in scenarios where the context is very long?
- Can the authors provide a detailed discussion on the limitations of the RLM framework, including potential drawbacks and scenarios where it might not be effective?
- How does the RLM framework perform when compared to other methods in terms of handling long-context tasks?
- Could the authors provide a more detailed analysis of the RLM trajectories, perhaps in a tabular format, to better understand the model's behavior?
- How does the RLM framework handle the potential for recursive calls to become unbounded, and what measures are in place to prevent this?
- Can the authors discuss the impact of the REPL on the performance of the RLM framework, and how this might affect the results?

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
- Reasons: The paper introduces a novel approach to handling long contexts in LLMs, which is both innovative and well-explained. The experimental results demonstrate the effectiveness of the proposed Recursive Language Models (RLMs) in handling long-context tasks, outperforming traditional LLMs in some cases. The paper is well-written, clear, and provides a detailed analysis of the RLM trajectories, which adds depth to the understanding of the model's behavior. The reviewers have highlighted the paper's contribution to the field and its potential for future research. The decision to accept is based on the originality of the approach, methodological soundness, and the significance of the results. The paper is recommended for acceptance as a poster, with minor improvements suggested for clarity and presentation.