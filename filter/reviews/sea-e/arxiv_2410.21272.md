 **Summary:**
The paper explores the internal mechanisms of large language models (LLMs) in handling arithmetic reasoning tasks, focusing on how these models process and memorize arithmetic operations. The study identifies a set of neurons responsible for arithmetic operations and categorizes them into heuristic types, suggesting that LLMs rely on a "bag of heuristics" rather than robust algorithms or memorization. The authors demonstrate that these heuristics are learned early in the training process and that their effectiveness varies across different layers and neurons. The paper also discusses the limitations of this approach, including potential biases in the heuristic definitions and the generalizability of the findings to other types of tasks or models.

**Strengths:**
- The paper is well-written, clear, and easy to follow, making it accessible to a broad audience.
- The authors provide a detailed analysis of the internal mechanisms of LLMs, focusing on how these models handle arithmetic reasoning tasks.
- The paper introduces a novel approach to understanding LLMs by examining the mechanisms behind arithmetic operations, which is both original and insightful.
- The study is comprehensive, covering various aspects of LLM behavior, including the identification of a circuit responsible for arithmetic calculations, the categorization of neurons into heuristic types, and the analysis of how these heuristics evolve over the course of training.
- The paper includes a robust set of experiments and ablations that provide a detailed view of the mechanisms at play, contributing to a better understanding of how LLMs process arithmetic operations.

**Weaknesses:**
- The paper's focus on arithmetic reasoning limits its applicability to other types of reasoning tasks, which might be more generalizable or relevant to broader applications.
- The definition of heuristics and their categorization is somewhat arbitrary and may not fully capture the complexity or nuance of LLM behavior.
- The paper's conclusions about the reliance on heuristics for arithmetic operations might not generalize to other types of tasks or models, which could limit the broader impact of the findings.
- The paper's methodology, particularly the use of heuristic definitions, could be biased by human interpretation, which might not fully capture the complexity or nuance of LLM behavior.
- The paper's claims about the reliance on heuristics for arithmetic operations might be seen as overly simplistic, as it does not adequately address the potential role of other factors such as memorization or algorithmic processing.

**Questions:**
- Could the authors elaborate on how the heuristic definitions were chosen and whether there is a systematic way to identify these heuristics without human bias?
- How do the heuristics identified in this study compare to those identified in other studies, and what insights can be gained from comparing these across different models or tasks?
- What are the implications of the findings for other types of reasoning tasks, and how might the mechanisms identified in this study be applied or adapted to other domains?
- Could the authors discuss the potential impact of their findings on the design and training of LLMs, particularly in terms of improving their mathematical abilities?
- How do the authors address the potential limitations of their study, such as the generalizability of their findings to other types of tasks or models?

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
- Reasons: The paper provides a detailed and insightful analysis of how LLMs process arithmetic reasoning tasks, using a novel approach that identifies a set of neurons responsible for arithmetic operations and categorizes them into heuristic types. The findings suggest that LLMs rely on a "bag of heuristics" rather than robust algorithms or memorization, which is a significant contribution to the field. The paper is well-written, clear, and includes a robust set of experiments and ablations that support the conclusions. However, the paper's focus on arithmetic reasoning limits its applicability to other types of reasoning tasks, and the definition of heuristics might be biased by human interpretation. Despite these limitations, the paper's methodological soundness, clarity, and originality make it a valuable contribution to the field, warranting acceptance as a poster presentation.