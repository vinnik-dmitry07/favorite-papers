 **Summary:**
The paper explores the use of white-box probes to detect deception in language models, focusing on the internal activations of models to distinguish between honest and deceptive responses. It employs a variety of datasets, including those with contrasting instructions and roleplaying scenarios, to evaluate the effectiveness of these probes. The paper also compares the performance of these probes with black-box models and discusses their generalization to more complex and realistic scenarios. Despite the innovative approach, the paper faces criticism for its limited evaluation scope, potential biases in labeling, and the generalizability of the findings.

**Strengths:**
- The paper addresses a significant and timely issue of detecting deception in large language models (LLMs), which is crucial for ensuring the safety and reliability of AI systems.
- The methodology is well-explained, with clear descriptions of the datasets used and the training and evaluation of the probes.
- The paper includes a variety of datasets and evaluation metrics, which provide a comprehensive assessment of the probes' effectiveness.
- The paper is well-written, with clear and concise explanations of the experiments and results, making it accessible and understandable.
- The authors have made their code and data publicly available, which supports reproducibility and transparency in research.

**Weaknesses:**
- The paper lacks a detailed discussion on the limitations of the probes, particularly in terms of their generalizability and the potential for spurious correlations.
- The evaluation of the probes is limited to a few datasets and does not include a broader range of scenarios or models, which could affect the robustness of the findings.
- There are concerns about the accuracy and reliability of the labeling process, which is crucial for the validity of the results.
- The paper does not adequately address the potential biases in the labeling process, which could influence the effectiveness of the probes.
- The paper could benefit from a more thorough discussion on the implications of the findings, particularly in terms of the practical applications and broader societal impacts of the research.

**Questions:**
- How do the authors ensure the accuracy and reliability of the labeling process, especially given the potential for bias or error in human annotation?
- Could the authors provide more details on how they addressed potential biases in the labeling process, such as the use of automated tools or inter-annotator agreement metrics?
- How do the authors plan to address the potential for spurious correlations in the probes, and what steps are being taken to ensure the robustness of the findings?
- In light of the limitations in the evaluation scope, how do the authors plan to expand the testing of the probes to more diverse scenarios and models?
- Could the authors provide more detailed examples or case studies to illustrate the practical applications of the probes in real-world scenarios?

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
- Reasons: The paper presents a novel approach to detecting deception in language models using white-box probes, which is both timely and relevant. The methodology is well-explained, and the results, while not perfect, demonstrate a promising direction for future research. The paper's contribution to the field is significant, and the decision to accept is supported by the overall positive reception of the methodology and the potential for further development and application. However, the decision is tempered by concerns about the limited evaluation scope and the potential for biases in the labeling process, which could affect the generalizability and reliability of the findings. The decision to accept is also influenced by the paper's potential to stimulate further research and discussion in the community.