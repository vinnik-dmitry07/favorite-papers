 **Summary:**
The paper investigates the performance of large language models (LLMs) in multiple-choice question answering (MCQA) when only the choices are provided, without the original question. The study examines various hypotheses including memorization, choice dynamics, and abductive question inference to understand the LLMs' behavior in such scenarios. The authors find that LLMs can infer the original question from the choices and use this information to answer correctly, suggesting that their performance is not solely due to memorization or surface-level shortcuts. The research is based on experiments with open-source LLMs and involves a thorough analysis of LLM behavior in MCQA settings, highlighting the need for more robust baselines and fair evaluations in MCQA benchmarks.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear structure and logical flow.
- The research question is timely and relevant, addressing the use of LLMs in MCQA tasks and the potential for artifacts in evaluating these models.
- The experiments are comprehensive and well-designed, providing a thorough analysis of LLM behavior in MCQA settings.
- The paper introduces a novel method of using LLMs to infer the original question from the choices, which is an interesting approach to understanding LLM decision-making.
- The findings are significant and contribute to the understanding of LLM behavior in MCQA tasks, particularly in the context of artifact exploitation and the use of LLMs to infer questions from choices.

**Weaknesses:**
- The paper lacks a detailed discussion on the limitations of the study, particularly the generalizability of the findings to other LLMs and datasets.
- The experimental setup and the use of few-shot examples might not fully represent real-world scenarios, and the results might not generalize well to different LLM configurations or datasets.
- The paper does not sufficiently address the potential for LLMs to exploit artifacts in MCQA tasks, which could limit the validity of the conclusions drawn.
- The paper could benefit from a more detailed discussion on the potential negative societal impacts of the findings, particularly in the context of LLM evaluations.
- The paper does not sufficiently address the potential for LLMs to exploit artifacts in MCQA tasks, which could limit the validity of the conclusions drawn.

**Questions:**
- Can the authors provide more details on the generalizability of the findings to other LLMs and datasets?
- How do the authors ensure that the conclusions drawn from the study are not overly influenced by the specific LLMs or datasets used?
- Could the authors elaborate on the potential negative societal impacts of the findings, particularly in the context of LLM evaluations?
- How do the authors address the potential for LLMs to exploit artifacts in MCQA tasks, and what steps can be taken to mitigate this issue?
- Could the authors discuss the potential implications of their findings for the design of more robust MCQA benchmarks and evaluations?

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
- Reasons: The paper provides a comprehensive analysis of LLM behavior in MCQA tasks, addressing the potential for artifact exploitation and the use of LLMs to infer questions from choices. The findings are significant and contribute to the understanding of LLM behavior in MCQA settings. The paper is well-written, clear, and easy to follow, making it accessible to a broad audience. Despite some limitations in the experimental setup and generalizability of the findings, the paper's contributions are substantial and warrant acceptance, particularly as a poster presentation at the conference.