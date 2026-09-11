 **Summary:**
The paper investigates the dynamics of factual knowledge acquisition during the pretraining of large language models (LLMs) by introducing a novel dataset and metrics to analyze the memorization and generalization of factual knowledge. The study explores how LLMs acquire and retain factual knowledge through various training conditions such as knowledge injection scenarios, pretraining stages, model sizes, and training batch sizes. Key findings include the accumulation of factual knowledge through micro-acquisitions, the relationship between training steps and forgetting of acquired knowledge, and the impact of deduplication and batch size on knowledge retention. The paper also discusses the implications of these findings for the design of pretraining strategies and the understanding of LLM behavior.

**Strengths:**
- The paper introduces a novel dataset and metrics specifically designed for analyzing the dynamics of factual knowledge acquisition in LLMs, which is a significant contribution to the field.
- The experimental setup is well-designed, with a comprehensive analysis of the impact of various training conditions on factual knowledge acquisition.
- The paper is well-written, clear, and easy to follow, with a clear motivation and a logical flow of ideas.
- The findings provide valuable insights into the mechanisms of factual knowledge acquisition in LLMs, which are crucial for understanding the behavior and performance of these models.
- The paper includes a detailed analysis of the impact of different training conditions, such as knowledge injection scenarios, pretraining stages, model sizes, and training batch sizes, on factual knowledge acquisition.
- The authors have conducted a thorough analysis of the impact of different training conditions on factual knowledge acquisition, which is crucial for understanding the behavior and performance of LLMs.

**Weaknesses:**
- The paper lacks a detailed discussion on the limitations of the proposed dataset and metrics, which could affect the generalizability and applicability of the findings.
- The paper does not adequately address the potential negative societal impacts of the work, which is a significant omission in the ethical considerations section.
- The paper could benefit from a more detailed discussion on the potential negative societal impacts of the work, particularly in relation to the use of LLMs for factual knowledge acquisition.
- The paper does not provide a detailed analysis of the impact of different types of factual knowledge (e.g., common vs. long-tail knowledge) on the acquisition dynamics, which could be a significant limitation.
- The paper does not discuss the potential negative societal impacts of the work, which is a significant omission in the ethical considerations section.
- The paper does not provide a detailed analysis of the impact of different types of factual knowledge (e.g., common vs. long-tail knowledge) on the acquisition dynamics, which could be a significant limitation.

**Questions:**
- Could you provide more details on the construction of the Fictional Knowledge dataset, particularly how the passages are generated and how the injected knowledge is selected?
- How do the findings of this study compare to other methods of factual knowledge injection, such as injecting knowledge in the form of questions or using different types of factual knowledge?
- Could you clarify the definition and role of the "local acquisition maxima" in the context of the experiments, and how it affects the interpretation of the results?
- How does the paper address the potential negative societal impacts of the work, particularly in relation to the use of LLMs for factual knowledge acquisition?
- Could you provide more details on the potential negative societal impacts of the work, particularly in relation to the use of LLMs for factual knowledge acquisition?
- How do the findings of this study generalize to other types of factual knowledge, and what are the implications for the design of pretraining strategies to improve factual knowledge acquisition in LLMs?

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
- Reasons: The paper presents a comprehensive analysis of factual knowledge acquisition in LLMs, introducing a novel dataset and metrics that significantly advance the understanding of how LLMs acquire and retain factual knowledge. The findings are well-supported by experiments and provide valuable insights into the dynamics of factual knowledge acquisition. The paper is well-written, clear, and easy to follow, making it accessible to a broad audience. The reviewers have highlighted the importance of the study and the potential impact on the field. However, there are concerns about the generalizability of the findings and the potential negative societal impacts, which need to be addressed in future work. Despite these limitations, the paper is recommended for acceptance due to its significant contributions to the understanding of LLM behavior and its potential to guide future research in this area.