 **Summary:**
The paper explores the relationship between transformers and neural representations in the hippocampal formation, specifically focusing on the entorhinal cortex. It introduces a novel approach by integrating recurrent position encodings into transformers, which are shown to replicate the spatial representations observed in the brain, such as grid and band cells. The paper also proposes a new model, TEM-t, which integrates the Tolman-Eichenbaum Machine (TEM) with transformers, aiming to enhance the understanding of hippocampal models and provide insights into the computational role of the hippocampus. The paper further discusses the implications of these findings for broader cognitive domains, suggesting that similar computational principles might apply to other areas of neuroscience.

**Strengths:**
- The paper is well-written and clearly articulates the relationship between transformers and neural representations in the hippocampal formation, providing a novel understanding of the computational role of the hippocampus.
- The authors have shown that transformers with recurrent position encodings can replicate neural representations found in rodent entorhinal cortex and hippocampus, which is a significant contribution to the field.
- The paper offers a novel take on the computational role of the hippocampus and an instantiation of hippocampal indexing theory, which is a significant advancement in the understanding of hippocampal models.
- The paper is well-organized and easy to follow, making it accessible to a broad audience.
- The paper provides a novel insight on the role of positional encodings in transformers, which is crucial for advancing the understanding of transformer models.

**Weaknesses:**
- The paper lacks a clear explanation of the mathematical relationship between the transformer and the current hippocampal models from neuroscience, particularly the Tolman-Eichenbaum Machine (TEM).
- The paper does not adequately address the scalability of the proposed model, TEM-t, to more complex environments or tasks, which limits its applicability.
- The paper's claims about the mathematical relationship between the transformer and TEM are not convincingly supported by empirical evidence, and the experimental results are not convincing enough to substantiate the claims.
- The paper does not sufficiently discuss the limitations of the proposed model, which is crucial for understanding its applicability and potential shortcomings.
- The paper could benefit from a more detailed discussion on the choice of the task and environment, as well as the selection of hyperparameters, which are crucial for the validity of the results.

**Questions:**
- Could the authors clarify the mathematical relationship between the transformer and the current hippocampal models from neuroscience, particularly the Tolman-Eichenbaum Machine (TEM)?
- How does the proposed model, TEM-t, scale to more complex environments or tasks?
- What are the implications of using a causal transformer in the model, and how does it affect the model's performance and scalability?
- Could the authors provide more details on the experimental setup, including the number of trials, the number of environments, and the number of neurons used in the model?
- How does the model perform when trained on different tasks or environments, and what are the implications of these variations on the model's performance?
- Could the authors elaborate on the choice of hyperparameters and their impact on the model's performance?

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
- Reasons: The paper presents a novel approach to understanding the relationship between transformers and neural representations in the hippocampal formation, which is both innovative and relevant to the field. The reviewers have highlighted the clarity and organization of the paper, as well as the potential impact of the findings on the understanding of hippocampal models and broader cognitive domains. However, there are concerns regarding the lack of empirical evidence to support some claims and the need for a more rigorous discussion on the scalability and limitations of the proposed model. Despite these issues, the paper is seen as a valuable contribution to the field, and the reviewers recommend acceptance, particularly as a poster presentation, to allow for further discussion and refinement of the ideas presented.