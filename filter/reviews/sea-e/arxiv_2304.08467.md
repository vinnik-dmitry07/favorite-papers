 **Summary:**
The paper introduces "gisting," a method for compressing prompts into a smaller set of "gist" tokens, aiming to reduce computational overhead and improve efficiency in language model (LM) training. This method involves training a model to predict gist tokens, which are then used to compress prompts, allowing for faster and more efficient processing. The approach is tested on models like LLaMA-7B and FLAN-T5-XXL, showing significant reductions in FLOPs and latency, along with some storage savings. However, the paper's novelty is questioned as it seems to resemble existing methods like prefix-tuning and context distillation. The method's effectiveness is demonstrated through experiments, but the paper's contribution is seen as limited due to its simplicity and similarity to existing techniques.

**Strengths:**
- The paper is well-written, clear, and easy to follow, making it accessible to a broad audience.
- The proposed method of gisting is simple yet effective, with significant reductions in FLOPs and latency, as well as some storage savings.
- The paper provides a comprehensive evaluation of the method, including both automated and human evaluations, which helps in validating the effectiveness of the proposed approach.
- The method is novel in its application to prompt compression, which is a significant issue in large language models (LLMs).
- The paper is well-organized, with clear figures and tables that aid in understanding the content.

**Weaknesses:**
- The paper lacks a detailed comparison with existing methods such as prefix-tuning and context distillation, which could have provided a clearer picture of the method's advantages and disadvantages.
- The paper does not sufficiently address the novelty of the method, as it appears to be a combination of existing techniques like prefix-tuning and context distillation.
- The paper's experimental results are not convincing, with some results showing only marginal improvements or even decreases in performance.
- The paper does not adequately address the limitations of the method, such as the potential for overfitting and the impact of different prompt lengths on performance.
- The paper's claims about the method's ability to generalize to unseen tasks are not convincingly supported by the experimental results.

**Questions:**
- Can the authors clarify the differences between gisting and other methods like prefix-tuning and context distillation, especially in terms of their contributions to the field?
- How does the method perform when applied to different types of prompts, such as those with varying lengths or complexities?
- Could the authors provide more detailed comparisons with existing methods to better establish the method's advantages and disadvantages?
- How does the method handle the potential for overfitting, especially when using a single gist token?
- Can the authors provide more detailed results on the performance of the method under different conditions, such as varying prompt lengths or different types of tasks?

**Soundness:**
2 fair

**Presentation:**
3 good

**Contribution:**
2 fair

**Rating:**
5 marginally below the acceptance threshold

**Paper Decision:**
- Decision: Reject
- Reasons: The paper, while presenting a potentially useful method for prompt compression, falls short in terms of novelty and depth of contribution. The method, although effective in reducing computational overhead, is seen as a combination of existing techniques rather than a significant advancement. The paper also lacks a thorough comparison with existing methods and does not sufficiently address the limitations of the proposed approach. The decision to reject is supported by the metareview, which highlights the need for more extensive comparisons and a clearer demonstration of the method's advantages over existing techniques.