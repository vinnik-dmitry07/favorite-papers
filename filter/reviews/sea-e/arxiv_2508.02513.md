 **Summary:**
The paper investigates the internal mechanisms of large language models (LLMs) in solving simple arithmetic tasks, focusing on how these models represent and process numbers digit by digit. It introduces a methodology using Fisher Score-based feature selection and causal interventions to identify and validate digit-position-specific arithmetic circuits within MLP neurons. These circuits are shown to operate independently across different digit positions, with the ability to alter model predictions selectively. The study also explores the modular nature of these circuits, suggesting that they are not influenced by model size or tokenization strategy. The paper provides evidence for these circuits' existence and causal role in arithmetic tasks, contributing to a better understanding of LLMs' internal mechanisms.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation and a clear methodology.
- The authors provide a detailed explanation of their methodology, including the use of Fisher Score-based feature selection and causal interventions to identify and validate digit-position-specific arithmetic circuits.
- The paper is original in its approach, using a novel methodology to study the internal mechanisms of large language models (LLMs) in solving simple arithmetic tasks.
- The findings are significant and contribute to a better understanding of how LLMs perform arithmetic tasks, showing that these tasks are not merely heuristics but involve structured, compositional arithmetic processes.
- The paper is reproducible, with all code and data provided, and the experiments are well-designed and well-executed.
- The paper provides a detailed analysis of the internal mechanisms of LLMs, which is crucial for understanding the capabilities and limitations of these models.

**Weaknesses:**
- The paper could benefit from more detailed explanations of the methodology, particularly in sections where the methodology is introduced.
- The paper lacks a comprehensive discussion on the limitations of the methodology and the potential biases in the data used.
- The paper could benefit from a more detailed discussion on the implications of the findings for broader applications of LLMs in arithmetic reasoning.
- The paper could be improved by including more complex arithmetic tasks and different types of models to validate the generalizability of the findings.
- The paper could benefit from a more detailed discussion on the implications of the findings for the development of more effective and efficient LLMs for arithmetic reasoning.
- The paper could be improved by including more detailed visualizations and explanations of the results, particularly in figures and tables, to enhance the clarity and impact of the findings.

**Questions:**
- Could the authors provide more detailed explanations of the methodology, particularly in the introduction of the methodology?
- How do the authors address potential biases in the data used in their experiments?
- How do the authors ensure the generalizability of their findings to more complex arithmetic tasks and different types of models?
- Could the authors discuss the implications of their findings for the development of more effective and efficient LLMs for arithmetic reasoning?
- Could the authors provide more detailed visualizations and explanations of the results, particularly in figures and tables, to enhance the clarity and impact of the findings?
- How do the authors ensure that the methodology is robust and unbiased, especially in the selection of neurons and the interpretation of results?

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
- Reasons: The paper presents a novel methodology using Fisher Score-based feature selection and causal interventions to identify and validate digit-position-specific arithmetic circuits within MLP neurons, providing a significant contribution to the understanding of how LLMs perform arithmetic tasks. The methodology is well-explained, and the findings are robust and supported by detailed experiments. The paper is well-written, clear, and easy to follow, making it accessible to a broad audience. The reviewers have highlighted the originality and significance of the paper, and the methodology is sound and the presentation is clear. The paper is also reproducible, which is crucial for advancing the field. The decision to accept is based on the originality, methodological soundness, significance of results, and clarity and logic of presentation.