 **Summary:**
The paper introduces AdEMAMix, a novel optimizer that combines two exponentially moving averages (EMAs) to enhance the training of large language models (LLMs) and vision transformers (ViTs). AdEMAMix leverages the strengths of both fast and slow EMAs to maintain a balance between recent and older gradients, thereby improving the training efficiency and reducing the forgetting of training data. The methodology is supported by extensive experiments on various models, including LLMs and ViTs, demonstrating its effectiveness in terms of convergence speed, lower minima, and slower forgetting of training data. The paper also discusses the challenges in balancing the weights of recent and older gradients, which is crucial for maintaining a balance between exploration and exploitation in the training process.

**Strengths:**
- The paper is well-written, clear, and easy to follow, making it accessible to a broad audience.
- The proposed method, AdEMAMix, is simple yet effective, combining two EMAs to leverage both recent and older gradients, which is a novel approach.
- The experiments are extensive and demonstrate the effectiveness of the proposed method across various models, including large language models (LLMs) and vision transformers (ViTs).
- The paper provides a theoretical analysis of the proposed method, which is supported by empirical evidence, enhancing the credibility of the findings.
- The methodology is flexible and can be adapted to different scenarios, showing potential for broader applications in the field.

**Weaknesses:**
- The paper lacks a comprehensive comparison with other optimizers like Adafactor, Lion, and Sophia, which could provide a more robust evaluation of the proposed method.
- The paper does not discuss the computational overhead of AdEMAMix, which could be a significant concern for large-scale training.
- The experimental results are not sufficiently convincing, particularly in terms of statistical significance and the absence of error bars, which undermines the reliability of the results.
- The paper does not provide a detailed analysis of the hyperparameters used in the experiments, which could affect the reproducibility and generalizability of the results.
- The paper does not discuss the limitations of the proposed method, which could provide a more balanced view of its applicability and effectiveness.

**Questions:**
- Can the authors provide a more detailed comparison with other optimizers like Adafactor, Lion, and Sophia to better understand the relative advantages of AdEMAMix?
- How does AdEMAMix compare in terms of computational overhead and memory requirements compared to other optimizers?
- Could the authors provide a more detailed analysis of the hyperparameters used in the experiments to enhance the reproducibility and generalizability of the results?
- How does AdEMAMix perform in scenarios where the capacity/data ratio is not as favorable, as suggested by the results in Figure 6?
- Can the authors provide more details on the schedulers used in the experiments, particularly how they are determined and how they affect the performance of AdEMAMix?

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
- Reasons: The paper presents a novel optimizer, AdEMAMix, which effectively leverages both recent and older gradients to improve the training of large language models and vision transformers. The methodology is supported by extensive experiments and theoretical analysis, demonstrating its effectiveness in terms of convergence speed, lower minima, and slower forgetting of training data. The paper is well-written, making it accessible and easy to understand. Despite some concerns regarding the lack of comprehensive comparisons with other optimizers and the absence of error bars in experimental results, the overall contribution and soundness of the paper justify its acceptance. The decision to accept is further supported by the positive feedback from the reviewers and the authors' response to the concerns raised. The paper is recommended for acceptance as a poster, with suggestions for additional comparisons and statistical analysis in future work.