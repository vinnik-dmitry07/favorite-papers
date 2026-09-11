 **Summary:**
The paper investigates the implicit reasoning capabilities of transformer-based language models, focusing on the phenomenon of "grokking" where models learn to reason implicitly over parametric knowledge. It introduces a novel dataset for evaluating reasoning tasks, specifically focusing on two-hop composition and comparison, and demonstrates that transformers can learn implicit reasoning through extended training beyond overfitting. The study reveals that transformers can generalize effectively in certain scenarios, such as comparison, but struggle with composition and out-of-distribution examples. The paper also explores the internal mechanisms of transformers during training, showing how they form generalizing circuits and the impact of these circuits on systematicity. The authors suggest that these findings could guide future research in improving transformer architectures for implicit reasoning.

**Strengths:**
- The paper introduces a novel dataset for evaluating reasoning tasks, which is a significant contribution to the field.
- The study of implicit reasoning in transformers is a timely and relevant topic, and the paper provides a comprehensive analysis of the phenomenon of "grokking" in transformers.
- The paper is well-written, clear, and easy to follow, making it accessible to a broad audience.
- The experiments are well-designed, with a focus on the impact of data distribution on generalization, which is a novel approach.
- The paper provides a detailed analysis of the internal mechanisms of transformers during training, which is a significant contribution to the understanding of transformer behavior.
- The findings suggest that transformers can learn implicit reasoning through extended training, which is a valuable insight for improving transformer architectures.

**Weaknesses:**
- The paper's focus on only two types of reasoning tasks (composition and comparison) limits the generalizability of the findings to other types of reasoning tasks.
- The paper's claims about the limitations of transformers in implicit reasoning are not convincingly supported by the data, and the results are not robustly generalizable to other tasks or models.
- The paper's analysis of the internal mechanisms of transformers during training is limited to a single model architecture (GPT-2), which may not be representative of other transformer architectures.
- The paper's conclusions about the limitations of transformers in implicit reasoning are not convincingly supported by the data, and the results are not robustly generalizable to other tasks or models.
- The paper's claims about the impact of data distribution on generalization are not convincingly supported by the data, and the results are not robustly generalizable to other tasks or models.
- The paper's claims about the impact of data distribution on generalization are not convincingly supported by the data, and the results are not robustly generalizable to other tasks or models.

**Questions:**
- Could the authors clarify the definition of "atomic" and "inferred" facts in the context of their study?
- How does the paper's findings relate to the concept of "implicit reasoning" as it is commonly used in the literature?
- Can the authors provide more details on the experimental setup, particularly the training and evaluation of the models?
- How do the authors justify the choice of the GPT-2 model for their study, and what implications does this have for the generalizability of their findings?
- Could the authors provide more details on the experimental setup, particularly the training and evaluation of the models?
- How do the authors address the limitations of their study, particularly the generalizability of their findings to other tasks or models?

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
- Reasons: The paper presents a novel dataset and a comprehensive analysis of implicit reasoning in transformers, which is a significant contribution to the field. The findings, while not groundbreaking, provide valuable insights into the capabilities and limitations of transformers in implicit reasoning, which is a critical area of research in AI. The presentation of the paper is clear and well-structured, making it accessible to a broad audience. The paper's experimental design is robust, and the analysis of the internal mechanisms of transformers during training is thorough. Despite some limitations in the generalizability of the findings and the need for more diverse model architectures, the paper's contributions are substantial and warrant acceptance, particularly as a poster presentation at the conference.