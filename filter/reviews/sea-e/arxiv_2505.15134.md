 **Summary:**
The paper explores the application of entropy minimization in large language models (LLMs) across various tasks such as math, physics, and coding, using both supervised and unsupervised methods. The authors propose three methods: EM-FT, EM-RL, and EM-INF, which aim to improve LLM performance by minimizing entropy in different ways. EM-FT uses unlabeled outputs, EM-RL optimizes negative entropy as a reward, and EM-INF adjusts logits during inference without training data or parameter updates. The paper demonstrates that these methods, particularly EM-INF, can enhance LLM performance on complex tasks without labeled data, showing results that are comparable or better than strong baselines. However, the paper also acknowledges the limitations of these methods, such as their effectiveness in scenarios where model confidence does not correlate with correctness and their dependence on the capabilities of the pretrained models.

**Strengths:**
- The paper presents a novel approach to improving the reasoning capabilities of large language models (LLMs) through entropy minimization, which is a significant contribution to the field.
- The methodology is clearly explained, making it easy to understand and replicate, and the experiments are well-designed, showing promising results across various tasks.
- The paper is well-written, with clear explanations of the methods and results, and includes comprehensive evaluations that demonstrate the effectiveness of the proposed methods.
- The authors provide a thorough analysis of the limitations of their approach, which is crucial for understanding the scope and applicability of their findings.
- The paper includes a detailed discussion on the computational efficiency of the proposed methods, which is a critical aspect for practical deployment.

**Weaknesses:**
- The paper lacks a detailed discussion on the limitations of the proposed methods, especially in scenarios where model confidence does not correlate with correctness.
- There is a lack of comparison with other methods that also use entropy minimization, which could provide a clearer picture of the novelty and effectiveness of the proposed methods.
- The paper does not sufficiently discuss the computational requirements of the proposed methods, which could be a significant concern for practical deployment.
- The paper does not provide sufficient details on the implementation of the entropy minimization methods, which could affect the reproducibility and understanding of the results.
- The paper could benefit from a more detailed discussion on the potential negative societal impacts of the proposed methods, especially in terms of bias and fairness.

**Questions:**
- Can the authors provide more details on the computational requirements of the proposed methods, including the time and memory costs?
- How does the proposed method compare to other methods that use entropy minimization, and what are the key differences in terms of effectiveness and efficiency?
- Could the authors provide more details on the implementation of the entropy minimization methods, including the specific algorithms and hyperparameters used?
- How does the proposed method perform on tasks that require reasoning beyond simple math and coding, such as natural language understanding or generation tasks?
- Can the authors clarify the role of the KL regularizer in the EM-RL method and its impact on the results?
- How does the proposed method handle the issue of model confidence not correlating with correctness, and what are the implications for the practical deployment of the method?

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
- Reasons: The paper presents a novel approach to improving LLM performance through entropy minimization, which is supported by empirical evidence showing promising results. The methodology is well-explained, and the paper is generally well-written, making it accessible and understandable. The reviewers have highlighted some concerns regarding the novelty and depth of the analysis, but these do not detract significantly from the paper's contribution to the field. The decision to accept is based on the paper's originality, methodological soundness, and the significance of its results, despite some limitations in the depth of discussion on certain aspects. The decision aligns with the overall positive feedback from the reviewers and the conference's criteria for acceptance.