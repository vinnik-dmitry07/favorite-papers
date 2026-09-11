 **Summary:**
The paper investigates the behavior of Activation Oracles (AOs) trained on models fine-tuned with a "taboo word" task, where the model is trained to avoid mentioning a specific word while still representing it internally. The study reveals that AOs trained on such models can develop "blind spots" for the taboo word, failing to recover it despite its presence in the model's internal representations. The authors employ various techniques such as logit lens, layer ablation, and linear probes to analyze the AO's behavior and demonstrate that the blind spot is not due to the absence of the word in the model's representations but rather to the AO's inability to verbalize it. The paper also explores the implications of these findings for the reliability of AOs in interpreting model activations.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation and well-defined research questions.
- The experiments are well-designed, with appropriate controls and clear presentation of results, including the use of logit lens, layer ablation, and linear probes to understand the behavior of Activation Oracles (AOs).
- The paper addresses an important and timely topic, investigating the limitations of AOs in recovering hidden information from models, which is crucial for understanding the reliability of model interpretability tools.
- The paper provides a comprehensive analysis of the limitations of AOs and contributes to the ongoing discussion on the reliability of model interpretability tools.

**Weaknesses:**
- The paper's focus on a single model (Qwen3-8B) limits the generalizability of the findings, and it is unclear whether the observed effects would hold for other models.
- The paper lacks a broader discussion on the limitations of the taboo task and the potential biases it might introduce, which could affect the validity of the results.
- There is a lack of discussion on the potential negative societal impacts of the findings, which could be significant given the implications for model interpretability and security.
- The paper could benefit from a more detailed discussion on the implications of the findings for model interpretability and security, particularly in the context of fine-tuned models.
- The paper does not sufficiently address the potential for the AO to learn to suppress the target concept, which could be a significant limitation in practical applications.

**Questions:**
- Can the authors clarify whether the findings would hold for other models beyond Qwen3-8B?
- How do the authors address the potential biases introduced by the taboo task, and what steps were taken to mitigate these biases in the experimental setup?
- Could the authors discuss the potential negative societal impacts of the findings, particularly in the context of model interpretability and security?
- How does the paper address the possibility that the AO might learn to suppress the target concept, and what implications does this have for the practical application of AOs?
- Could the authors provide more details on the training and evaluation of the AOs, particularly in terms of the specifics of the training data and the evaluation metrics used?

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
- Reasons: The paper presents a novel and significant finding about the limitations of Activation Oracles (AOs) in recovering hidden information from models, which is crucial for understanding the reliability of model interpretability tools. The experiments are well-designed, and the paper is well-written, making the findings clear and accessible. The reviewers have highlighted some concerns regarding the generalizability of the findings and the potential biases introduced by the taboo task. However, these issues do not significantly detract from the paper's contribution to the field, and the overall impact of the findings is seen as high. The decision to accept is based on the originality of the research, methodological soundness, and the significance of the results, despite some concerns about the clarity and depth of the discussion on the limitations and societal impacts of the findings.