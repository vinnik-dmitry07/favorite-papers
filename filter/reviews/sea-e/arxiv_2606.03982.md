 **Summary:**
The paper investigates how language models (LMs) compare quantities with measurement units, focusing on the degradation of accuracy near the comparison boundary. It proposes a heuristic-based model that predicts LM preferences based on numerical-difference and unit-scale-difference cues, supported by causal interventions and surrogate models. The study demonstrates that LMs rely on these heuristics to make decisions, rather than converting both expressions into a shared scale. The research is supported by a comprehensive evaluation across various unit systems and language models, showing that LMs struggle with comparisons near the boundary and that this behavior can be explained by the heuristic model.

**Strengths:**
- The paper is well-written and easy to follow, with clear explanations of the experimental setup and results.
- The research question is interesting and relevant, focusing on how language models (LMs) compare quantities with measurement units, which is a novel and significant area of study.
- The study includes a comprehensive evaluation across various unit systems and language models, providing a robust analysis of LM behavior.
- The paper introduces a heuristic-based model that effectively explains LM behavior in comparison tasks, supported by causal interventions and surrogate models.
- The paper provides a detailed analysis of the factors influencing LM behavior, including numerical differences and unit-scale differences, which are crucial for understanding how LMs process and compare quantities.

**Weaknesses:**
- The paper could benefit from a more detailed discussion on how the units are chosen and their impact on the results.
- The experimental setup and the choice of metrics used, such as the Quantity Margin, are not sufficiently explained, which could limit the understanding of the results.
- The paper lacks a discussion on the limitations of the study, such as the generalizability of the findings to other types of LMs or tasks.
- There is a need for more detailed explanations of the experimental setup, including the choice of metrics and the rationale behind the experimental design.
- The paper could benefit from a more thorough discussion of related work, particularly in the area of LM interpretability and unit-aware reasoning.
- The paper could be improved by including more examples and a clearer explanation of the heuristic-based model and its implications.

**Questions:**
- Can the authors clarify the choice of units and their impact on the results?
- How do the authors justify the use of the Quantity Margin as a metric, and could they provide more details on its calculation and interpretation?
- Could the authors provide more examples and detailed explanations of the heuristic-based model, including how it is implemented and what it implies for LM behavior?
- How do the authors address the generalizability of their findings to other types of LMs or tasks?
- Could the authors discuss the limitations of their study in more detail, particularly in relation to the experimental setup and the choice of metrics?
- How do the authors address the potential biases in the data or the experimental setup, and what steps have been taken to mitigate these biases?

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
- Reasons: The paper presents a novel and significant contribution to the field by investigating how language models compare quantities with measurement units, using a heuristic-based model that effectively explains LM behavior. The experimental setup is robust, and the results are well-supported by causal interventions and surrogate models. The paper is well-written and easy to follow, making it accessible to a broad audience. The reviewers have highlighted the paper's originality and the significance of its findings, which could have a substantial impact on the field. The decision to accept is based on the paper's originality, methodological soundness, and the clarity and logic of its presentation. The decision is also influenced by the paper's potential to advance understanding in the area of LM interpretability and unit-aware reasoning.