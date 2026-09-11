 **Summary:**
The paper introduces a novel sampling algorithm that leverages the power distribution to enhance the reasoning capabilities of large language models (LLMs) without requiring additional training. This method, which is training-free and dataset-free, utilizes MCMC sampling to generate high-likelihood sequences from base models, matching or surpassing the performance of models trained with reinforcement learning (RL) on various benchmarks. The approach avoids the collapse in diversity that is common in RL-posttraining, demonstrating its effectiveness on tasks like MATH500, HumanEval, and GPQA. The paper also discusses the theoretical underpinnings of the method, comparing it to existing approaches like low-temperature sampling and GRPO.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation and a novel approach to eliciting reasoning capabilities from base models at inference time.
- The proposed method, which is training-free, dataset-free, and verifier-free, is simple yet effective, achieving single-shot reasoning capabilities on par with those from RL on in-domain reasoning tasks and even outperforming on out-of-domain reasoning tasks.
- The method avoids the collapse in diversity that is characteristic of RL-posttraining, maintaining sample diversity.
- The paper provides a detailed analysis of the proposed method, including a comparison with GRPO, and demonstrates its effectiveness through extensive experiments on various benchmarks.
- The paper is well-organized, with a clear structure and a detailed appendix that provides additional information on the methodology and results.

**Weaknesses:**
- The paper lacks a thorough comparison with other sampling methods, particularly those that use different sampling strategies or distributions.
- The method's effectiveness is not clearly demonstrated across a wide range of tasks, as the experiments are limited to a few specific tasks.
- The paper does not discuss the limitations of the proposed method, such as its applicability to different model architectures or the potential impact of different sampling strategies.
- The paper does not provide a detailed analysis of the computational cost or the scalability of the method, which could be crucial for practical implementation.
- The paper does not provide a detailed discussion on how the method performs on different model architectures or how it scales with different model sizes.
- The paper does not discuss the limitations of the proposed method, which could help in understanding its applicability and potential drawbacks.

**Questions:**
- Could the authors provide a more detailed comparison with other sampling methods, particularly those that use different sampling strategies or distributions?
- How does the proposed method perform on a wider range of tasks, and what are the implications of this for its generalizability?
- Can the authors discuss the limitations of the proposed method and how these might affect its practical application?
- How does the proposed method scale with different model architectures and sizes, and what are the computational costs associated with its implementation?
- Could the authors provide more details on the computational cost and the scalability of the method, especially in terms of the number of tokens generated and the inference time?
- How does the method perform on different model architectures, and what are the implications of this for its applicability across different LLM families?

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
- Reasons: The paper presents a novel and effective method for enhancing the reasoning capabilities of LLMs without additional training, which is a significant contribution to the field. The method is well-explained, and the experiments demonstrate its effectiveness on various benchmarks. The paper is well-written, clear, and easy to follow, making it accessible to a broad audience. The method's simplicity and its ability to match or surpass the performance of models trained with RL are notable. The paper also addresses the issue of diversity collapse in RL-posttraining, which is a significant concern in the field. The decision to accept is based on the paper's originality, methodological soundness, significance of results, and clarity and logic of presentation.