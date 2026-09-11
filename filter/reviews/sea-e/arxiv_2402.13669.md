 **Summary:**
The paper introduces Self-Distillation Fine-Tuning (SDFT), a novel method aimed at mitigating catastrophic forgetting during the fine-tuning of large language models (LLMs). SDFT involves generating a distilled dataset by prompting the LLM to rewrite responses from the target dataset, which is then used as a surrogate target for fine-tuning. This method aims to maintain the original distribution of the LLM, thereby preserving its capabilities and reducing the risk of forgetting. The paper presents experiments across various benchmarks, demonstrating the effectiveness of SDFT in reducing forgetting and improving performance on downstream tasks, while maintaining the model's general instruction-following abilities. However, concerns were raised about the novelty of the approach, the clarity of the method's impact on forgetting, and the need for more rigorous comparisons with existing methods.

**Strengths:**
- The paper is well-organized, easy to follow, and provides a comprehensive evaluation of the proposed method, SDFT, across various benchmarks, demonstrating its effectiveness in reducing forgetting and improving performance on downstream tasks.
- The method is simple and effective, requiring minimal modifications to existing fine-tuning pipelines, making it accessible and practical for real-world applications.
- The paper addresses a significant issue in the field of large language models (LLMs) by focusing on reducing catastrophic forgetting during fine-tuning, which is crucial for maintaining the capabilities of LLMs.
- The proposed method is novel and innovative, utilizing a self-distillation approach that generates a distilled dataset from the model itself, which is then used to fine-tune the model, potentially reducing the need for extensive retraining.
- The paper provides a detailed analysis of the impact of distribution shift on catastrophic forgetting and demonstrates the robustness of the SDFT method across different model scales and architectures.

**Weaknesses:**
- The paper lacks a clear definition and quantification of catastrophic forgetting, which makes it difficult to assess the effectiveness of the proposed method in addressing this issue.
- The novelty of the approach is questionable as similar methods have been previously explored, such as using the model's own outputs as targets for fine-tuning.
- The paper does not adequately address the computational overhead and resource requirements of the SDFT method, which could be a significant limitation for practical deployment.
- The paper does not provide a detailed comparison with existing methods, such as Self-Play Fine-tuning, which could have strengthened the argument for the superiority of the proposed method.
- The paper could benefit from a more rigorous evaluation, including a broader range of datasets and a more comprehensive analysis of the impact of different parameters on the effectiveness of the SDFT method.
- There are concerns about the potential for the model to learn to generate incorrect answers, which could undermine the effectiveness of the SDFT method.

**Questions:**
- Can the authors clarify the definition and quantification of catastrophic forgetting used in the paper and how it was measured?
- How does the SDFT method compare to other existing methods for reducing catastrophic forgetting in LLMs, such as Self-Play Fine-tuning?
- What are the specific computational and resource requirements of the SDFT method, and how do these compare to other fine-tuning methods?
- How does the SDFT method perform when applied to larger or more complex models, and what are the implications for its effectiveness and resource requirements?
- Can the authors provide more details on the experimental setup and results, particularly in the appendix, to enhance the reproducibility and transparency of the research?
- How does the SDFT method handle the potential for the model to learn to generate incorrect answers, and what measures are in place to prevent or mitigate this issue?

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
- Reasons: The paper introduces a novel method, SDFT, which addresses the issue of catastrophic forgetting in LLMs by generating a distilled dataset that maintains the original distribution of the LLM. The method is supported by extensive experiments that demonstrate its effectiveness in reducing forgetting and improving performance on downstream tasks. While there are concerns about the novelty and clarity of the method's impact on forgetting, the paper is well-organized, easy to follow, and provides a comprehensive evaluation. The decision to accept is based on the paper's contribution to the field, the soundness of the methodology, and the potential impact of the research. The decision is also influenced by the paper's clarity and logical presentation, which are commendable. However, the paper could benefit from a more rigorous comparison with existing methods and a clearer definition and quantification of catastrophic forgetting.