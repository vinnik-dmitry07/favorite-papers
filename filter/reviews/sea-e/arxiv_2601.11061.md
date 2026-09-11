 **Summary:**
The paper investigates the phenomenon of spurious rewards in Reinforcement Learning with Verifiable Rewards (RLVR) and its impact on Large Language Models (LLMs), specifically focusing on the Qwen2.5 model. It identifies a "Perplexity Paradox" where answer-token perplexity decreases while prompt-side coherence degrades, suggesting the model is bypassing reasoning in favor of memorization. The authors employ mechanistic interpretability tools to pinpoint the Anchor-Adapter circuit, which enables the model to bypass reasoning and directly retrieve memorized solutions under spurious RLVR. This circuit is localized in middle layers (L18-L20) and later layers (L21+), and the paper demonstrates that scaling specific MLP keys within this circuit can steer the model's performance. The paper also discusses potential mitigation strategies, such as adjusting MLP keys to control contamination-driven performance.

**Strengths:**
- The paper provides a comprehensive analysis of the perplexity paradox and the memorization phenomenon in RLVR, which is crucial for understanding the behavior of LLMs under different training conditions.
- The authors have conducted a detailed mechanistic analysis using various tools such as path patching, logit lens, and neural differential equations, which helps in understanding the internal mechanisms of LLMs.
- The paper is well-written, clear, and easy to follow, making it accessible to a broad audience.
- The findings are significant and have implications for the development of more robust and reliable LLMs, particularly in critical domains like mathematics, science, and coding.
- The paper includes a thorough ablation study and mechanistic intervention, which adds depth to the analysis and supports the conclusions drawn.

**Weaknesses:**
- The paper primarily focuses on the Qwen2.5 model, which might limit the generalizability of the findings to other LLMs.
- The paper does not adequately address the potential negative societal impacts of the research, which is a significant omission.
- The paper could benefit from a more detailed discussion on the limitations of the study and the generalizability of the findings to other models or datasets.
- The paper does not sufficiently address the potential for spurious rewards to be intentionally introduced to manipulate model behavior, which could have serious ethical implications.
- The paper's conclusions might be overstated, particularly in terms of the generalizability of the findings beyond the specific model and dataset used.

**Questions:**
- How do the authors ensure that the findings are generalizable to other models and datasets, especially given the specific focus on Qwen2.5?
- Could the authors clarify the potential negative societal impacts of the research and discuss how these might be mitigated?
- How do the authors address the potential for spurious rewards to be intentionally introduced to manipulate model behavior, and what steps can be taken to prevent this?
- Could the authors provide more details on the training procedure for the RLVR-tuned model and the specifics of the reward function used?
- How do the authors justify the choice of the Qwen2.5 model for this study, and what steps were taken to ensure the generalizability of the findings to other models?

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
- Reasons: The paper provides a significant contribution to the understanding of spurious rewards in RLVR and the memorization phenomenon in LLMs, which is crucial for developing more robust and reliable models. The methodological soundness is high, and the findings are well-supported by empirical evidence. The paper is well-written and easy to follow, which enhances its accessibility. The decision to accept is based on the originality of the research, the significance of the results, and the clarity and logic of the presentation. However, the paper could benefit from a more detailed discussion on the limitations and potential negative societal impacts of the research.