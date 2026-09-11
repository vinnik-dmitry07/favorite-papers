 **Summary:**
This paper investigates the implicit world models learned by large language models (LLMs) through a novel evaluation framework that leverages the Myhill-Nerode theorem. The authors propose new metrics for evaluating the coherence of world models, focusing on sequence compression and sequence distinction, which are crucial for assessing the internal world models of LLMs. The study demonstrates these metrics through various applications, including navigation, logic puzzles, and games, showing that existing metrics may not adequately capture the true capabilities of LLMs. The paper also introduces a new dataset of taxi rides in New York City to validate these metrics. The findings suggest that LLMs can perform well on certain tasks despite incoherent world models, which could lead to fragility in solving related but slightly different tasks.

**Strengths:**
- The paper is well-written, clearly articulating the problem and the proposed solution, with a clear and structured presentation.
- The introduction of a new dataset of taxi rides in New York City is a significant contribution, providing a valuable resource for future research.
- The paper effectively demonstrates the limitations of existing metrics for evaluating world models and proposes new metrics that are more robust and insightful.
- The application of the Myhill-Nerode theorem to evaluate the world models of LLMs is innovative and provides a novel approach to assessing the coherence of these models.
- The paper is well-organized, with a clear introduction, detailed methodology, and a comprehensive evaluation across various domains such as navigation, logic puzzles, and games.
- The findings of the study, particularly the incoherence of world models and their impact on model performance, are significant and could lead to new insights and research directions in the field.

**Weaknesses:**
- The paper could benefit from a more detailed explanation of the Myhill-Nerode theorem and its implications, especially for readers not familiar with the concept.
- The evaluation metrics, while innovative, are limited to deterministic finite automata (DFAs), which may not generalize well to more complex or stochastic systems.
- The paper could provide more detailed explanations and examples of how the proposed metrics can be applied in practical scenarios, especially in the context of LLMs.
- The paper lacks a comprehensive discussion on the limitations of the proposed metrics, particularly in terms of their applicability to different types of world models and their scalability to larger or more complex systems.
- There is a need for more experimental validation and comparative analysis with other metrics to establish the superiority or effectiveness of the proposed metrics.
- The paper could benefit from a more detailed discussion on the implications of the findings for the broader community, including potential applications and future research directions.

**Questions:**
- Could you clarify the definition of the Myhill-Nerode boundary and its implications for the evaluation of world models?
- How do the proposed metrics perform when applied to more complex or stochastic systems, such as those found in natural language processing or other domains?
- Can you provide more details on how the metrics can be applied in practical scenarios, especially in the context of LLMs?
- How do the proposed metrics compare to other existing metrics for evaluating world models, and what are the advantages or disadvantages of using these metrics?
- Could you elaborate on the implications of the findings for the broader community, particularly in terms of potential applications and future research directions?
- How do the metrics perform when applied to different types of world models, and what are the limitations or challenges in applying these metrics to more complex or stochastic systems?

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
- Reasons: The paper presents a novel approach to evaluating the implicit world models learned by LLMs, which is both innovative and well-executed. The use of the Myhill-Nerode theorem to develop new metrics for assessing sequence compression and sequence distinction is a significant contribution to the field. The paper is well-written, clearly articulating the problem and the proposed solution, and provides a valuable new dataset for future research. The findings, while limited to deterministic finite automata, are insightful and could lead to new research directions. The paper is technically solid, with a moderate-to-high impact, and the reviewers have unanimously recommended acceptance. The decision to accept is supported by the originality of the approach, the methodological soundness, and the significance of the results, along with the clarity and logic of the presentation.