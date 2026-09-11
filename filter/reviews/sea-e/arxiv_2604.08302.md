 **Summary:**
The paper introduces DMax, a novel approach to parallel decoding for diffusion language models (dLLMs) that addresses the issue of error accumulation in parallel decoding. DMax utilizes on-policy uniform training (OPUT) to train dLLMs, which enables the model to recover from its own predictions, thereby mitigating error accumulation. This is achieved by interpolating between predicted token embeddings and mask embeddings, allowing for iterative self-revision in the embedding space. The paper also proposes soft parallel decoding, which represents intermediate decoding states as a hybrid of predicted and mask embeddings, enhancing the model's ability to correct errors. The approach is validated through extensive experiments on various benchmarks, showing improvements in tokens per forward (TPF) and tokens per second (TPS) while maintaining accuracy.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation and a novel approach to parallel decoding for diffusion language models (dLLMs).
- The proposed method, DMax, is innovative, combining the strengths of masked diffusion language models (MDLMs) and uniform diffusion language models (UDLMs) to achieve parallel decoding while maintaining accuracy.
- The experiments conducted are extensive, demonstrating the effectiveness of the proposed method across various benchmarks, including GSM8K and MBPP.
- The paper includes a comprehensive ablation study, providing insights into the effectiveness of different components of the proposed method.
- The approach addresses a significant issue in dLLMs, namely error accumulation, and proposes a novel training strategy called On-Policy Uniform Training (OPUT) to mitigate this issue.

**Weaknesses:**
- The paper lacks a detailed discussion on the computational cost of the proposed method compared to other methods like LLaDA-2.0-mini.
- There is a lack of clarity on how the method performs in scenarios with low parallelism, and the paper does not provide results on the MATH500 and ASDIV datasets.
- The paper does not discuss the limitations of the proposed method, which could help in understanding its applicability and potential drawbacks.
- The paper could benefit from a more detailed explanation of the training data construction process, particularly how it affects the model's performance.
- The paper could provide more details on the training and inference time, and how the method performs on different model sizes and datasets.
- The paper does not compare the proposed method with other state-of-the-art methods in terms of accuracy and speed, which could help in understanding the method's relative performance.

**Questions:**
- Could the authors provide more details on the computational cost of the proposed method compared to other methods like LLaDA-2.0-mini?
- How does the method perform in scenarios with low parallelism, and what are the implications for practical applications?
- Could the authors clarify the training data construction process and how it affects the model's performance?
- How does the proposed method compare with other state-of-the-art methods in terms of accuracy and speed?
- Could the authors provide more details on the training and inference time, and how the method performs on different model sizes and datasets?
- How does the proposed method handle the trade-off between accuracy and speed, and what are the implications for practical applications?

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
- Reasons: The paper presents a novel approach to parallel decoding for diffusion language models, addressing the issue of error accumulation effectively through on-policy uniform training and soft parallel decoding. The method is well-received for its innovative approach and the extensive experiments that demonstrate its effectiveness. The paper is well-written and easy to follow, making it accessible to a broad audience. The reviewers have highlighted the paper's contribution to the field and its potential impact. The decision to accept is based on the originality of the approach, methodological soundness, and the significance of the results. The paper is recommended for presentation as a poster to allow for further discussion and feedback from the community.