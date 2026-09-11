 **Summary:**
The paper explores the dynamics of looped transformer models, specifically focusing on the recurrent blocks within these models. It investigates how these blocks organize computational stages and how they behave during inference, comparing them to feedforward models. The study reveals that looped transformers exhibit similar stages of inference to feedforward models, suggesting that these stages are emergent rather than a result of training biases. The paper also examines the impact of architectural choices such as input injection and recurrent block size on the emergence and stability of these stages. The findings suggest that looped transformers can self-organize into multiple different mixing stages in recurrent depth, which resemble feedforward stages, and that these stages are beneficial for language modeling even when applied repeatedly in recurrent depth.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation and a comprehensive literature review.
- The authors provide a detailed analysis of the stages of inference in looped transformers, which is both novel and insightful.
- The paper includes a variety of experiments that demonstrate the emergence of stages of inference in looped transformers, which are not explicitly encouraged by the training process.
- The findings are supported by a range of experiments, including those on randomly initialized models, which show that the behavior observed in trained models is likely to generalize to cyclic behavior in untrained models.
- The paper provides a detailed analysis of the impact of different architectural choices on the emergence and stability of stages of inference in looped transformers.

**Weaknesses:**
- The paper lacks a clear definition and explanation of the stages of inference, which are crucial for understanding the paper's main findings.
- The paper does not provide a detailed explanation of why self-organization into stages of inference occurs in looped transformers, which is a significant gap in the analysis.
- The paper's scope is limited to looped transformers, which might not be representative of all transformer models, and the generalizability of the findings to other types of transformers is not discussed.
- The paper does not include a discussion on the limitations of the findings, which could affect the credibility of the results.
- There is a lack of discussion on the practical implications of the findings, particularly in terms of how they could be applied to improve the design of looped transformers.

**Questions:**
- Can the authors provide a clearer definition and explanation of the stages of inference, and how they are identified and measured in the experiments?
- How do the authors explain the self-organization into stages of inference in looped transformers, and what are the underlying mechanisms that drive this behavior?
- Could the authors discuss the generalizability of the findings to other types of transformer models, and how the results might apply to these models?
- How do the authors address the limitations of their findings, and what are the potential implications of these limitations for the practical application of the results?
- Could the authors provide more detailed experimental results, such as the ColSum concentration for different models and the impact of different architectural choices on the emergence and stability of stages of inference?

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
- Reasons: The paper provides a novel and insightful analysis of looped transformer models, revealing how these models organize computational stages and behave during inference. The findings, although limited to looped transformers, offer valuable insights into the dynamics of these models and suggest that stages of inference are emergent rather than a result of training biases. The paper is well-written, clearly presented, and contributes to the understanding of looped transformers, which is a significant area of interest in the field. The decision to accept is based on the paper's originality, methodological soundness, and the significance of its findings, despite some limitations in scope and generalizability. The reviewers have highlighted the need for a more detailed discussion on the practical implications of the findings and the limitations of the study, which should be addressed in future work.