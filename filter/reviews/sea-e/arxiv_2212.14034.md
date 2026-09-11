 **Summary:**
The paper explores the training of a transformer-based language model from scratch within a single day using a single GPU, focusing on modifications to the architecture, training setup, and dataset to optimize performance. The authors investigate various aspects such as model size, data selection, and training strategies to achieve competitive results with BERT on the GLUE benchmark. The study also examines the impact of different modifications on the training process and the resulting model performance, providing insights into the challenges and opportunities of training large language models with limited resources.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation and a well-defined problem statement.
- It provides a comprehensive analysis of the training process for a single-day training of a language model, including modifications to the architecture, training setup, and dataset.
- The paper includes a detailed ablation study that systematically evaluates the impact of different modifications on the model's performance.
- The authors have conducted extensive experiments and provide detailed analysis and discussion, which are supported by comprehensive experiments and analysis.
- The paper is well-organized, with a clear structure and logical flow, making it easy for readers to follow and understand the content.
- The study includes a variety of datasets and models, which enhances the generalizability of the findings.

**Weaknesses:**
- The paper lacks a detailed discussion on the limitations of the study, particularly in terms of the scalability of the findings to larger models or different training setups.
- There is a lack of comparison with other models or methods, which could help in understanding the relative performance of the proposed approach.
- The paper does not provide sufficient details on the hardware used for the experiments, which could affect the reproducibility and generalizability of the results.
- The paper could benefit from more detailed explanations and justifications for the choices made in the experimental setup, particularly in sections where the rationale behind certain decisions is not clear.
- The paper does not adequately address the potential negative societal impacts of the research, which could be a significant concern for some readers.

**Questions:**
- Could the authors provide more details on the hardware used for the experiments, including the specific GPU model and its capabilities?
- How does the performance of the model compare when using different pre-training objectives, such as masked language modeling versus other objectives?
- Can the authors clarify the rationale behind the choices made in the experimental setup, particularly in sections where the reasoning is not clear?
- How do the findings of this study generalize to other models or training setups, and what are the limitations of the proposed approach?
- Could the authors discuss the potential negative societal impacts of their research and how they are addressing these concerns?

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
- Reasons: The paper presents a novel approach to training a language model within a single day using a single GPU, which is a significant contribution to the field. The methodology is well-explained, and the results are convincingly demonstrated, showing that it is possible to achieve competitive results with BERT using this approach. The paper is well-written, clear, and easy to follow, making it accessible to a broad audience. The experimental setup is robust, and the findings are well-supported by the data. The decision to accept is based on the originality of the approach, methodological soundness, significance of results, and clarity and logic of presentation. The paper is recommended for acceptance, particularly as a poster presentation, to allow for further discussion and exploration of the findings.