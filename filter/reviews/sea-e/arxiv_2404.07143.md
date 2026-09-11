 **Summary:**
The paper introduces a novel attention mechanism, Infini-attention, designed to handle infinitely long inputs by integrating a compressive memory into the vanilla attention mechanism. This mechanism, which combines masked local attention and long-term linear attention, is aimed at improving the scalability of Transformer-based Large Language Models (LLMs) to extremely long inputs without increasing memory and computational costs. The authors demonstrate the effectiveness of this approach through experiments on various benchmarks, including long-context language modeling, passkey context block retrieval, and book summarization tasks. The methodology is evaluated against existing models like Transformer-XL and Memorizing Transformers, showing improvements in perplexity and other metrics. However, concerns are raised about the novelty of the approach, as it appears to be a combination of existing techniques without significant innovation.

**Strengths:**
- The paper is well-written, making it easy to follow and understand.
- The proposed Infini-attention mechanism is novel and innovative, combining masked local attention and long-term linear attention in a single Transformer block, which is a significant advancement in the field.
- The method achieves impressive results on long-context language modeling benchmarks and is demonstrated to be effective in long-context language modeling tasks.
- The paper provides a comprehensive evaluation of the proposed method, including a comparison with existing models like Transformer-XL and Memorizing Transformers, and demonstrates the effectiveness of the approach through experiments on various benchmarks.
- The method is simple and efficient, with a focus on scalability and efficiency, which is crucial for handling extremely long inputs in Transformer-based LLMs.

**Weaknesses:**
- The paper lacks a clear explanation of the novelty and the specific contributions of the proposed Infini-attention mechanism. It is unclear how this mechanism differs from existing models like Transformer-XL and Memorizing Transformers.
- The paper does not provide a detailed analysis of the computational complexity and memory usage of the proposed method, which is crucial for understanding its practical applicability and efficiency.
- The experiments are limited to specific benchmarks and do not include a broader range of tasks or datasets, which could have provided a more comprehensive evaluation of the method's effectiveness.
- The paper does not discuss the limitations of the proposed method, which is essential for understanding its applicability and potential drawbacks.
- The paper could benefit from a more detailed discussion on the design choices and the rationale behind the specific modifications made to the attention layer.

**Questions:**
- Could the authors clarify the specific contributions of the proposed Infini-attention mechanism and how it differs from existing models like Transformer-XL and Memorizing Transformers?
- How does the proposed method compare in terms of computational complexity and memory usage to other existing methods for handling long contexts in LLMs?
- Can the authors provide a more detailed analysis of the experimental results, particularly the performance on the passkey retrieval task and the book summarization task?
- How does the method perform when scaled up to larger models, and what are the potential limitations or challenges in scaling up the method?
- Could the authors discuss the potential applications of the proposed method beyond the specific tasks evaluated in the paper?
- How does the method handle the issue of attention sink, which is a common challenge in long-context modeling?

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
- Reasons: The paper introduces a novel attention mechanism, Infini-attention, which effectively addresses the challenge of handling infinitely long inputs in Transformer-based LLMs. The method is well-evaluated against existing models and demonstrates improvements in perplexity and other metrics. Despite some concerns regarding the novelty and the depth of experimental validation, the paper is well-written, easy to follow, and presents a significant contribution to the field. The decision to accept is supported by the paper's originality, methodological soundness, and the significance of its results, even though the presentation and contribution scores are slightly lower. The decision aligns with the overall positive reception of the paper by the reviewers and the conference organizers.