 **Summary:**
The paper investigates the role of token entropy in the reasoning capabilities of large language models (LLMs) through a novel perspective of token entropy patterns. It identifies that only a small fraction of tokens exhibit high entropy, which are crucial forks that guide the model towards diverse reasoning pathways. The study reveals that RLVR largely adheres to the base model's entropy patterns, primarily adjusting the entropy of high-entropy tokens. The paper proposes a method to restrict policy gradient updates to forking tokens, demonstrating significant performance improvements on the AIME benchmark. The findings suggest that high-entropy minority tokens play a significant role in RLVR, potentially surpassing the 80/20 rule by using only 20% of the tokens while maintaining comparable performance.

**Strengths:**
- The paper introduces a novel perspective on analyzing the reasoning capabilities of LLMs through the lens of token entropy patterns, which is a significant advancement in understanding the mechanisms of RLVR.
- The authors have conducted a comprehensive analysis of token entropy patterns in Chain-of-Thought (CoT) reasoning, providing insights into how different tokens influence reasoning performance.
- The paper is well-written, easy to follow, and presents a clear and logical structure, making it accessible to a broad audience.
- The findings are supported by a robust experimental setup, including the use of a large dataset of 10^6 tokens for analysis, which adds credibility to the results.
- The paper provides a detailed analysis of the evolution of token entropy during RLVR training, highlighting the significance of high-entropy tokens in RLVR.
- The proposed method of restricting policy gradient updates to forking tokens is innovative and shows significant performance improvements, even surpassing full-gradient updates in some cases.

**Weaknesses:**
- The paper lacks a detailed explanation of the experimental setup, particularly how the entropy threshold was determined and the rationale behind the choice of 20% of tokens for analysis.
- The paper does not provide a detailed comparison with other RLVR algorithms, which could help in understanding the generalizability of the findings.
- The paper does not discuss the limitations of its approach, which could include the potential impact of different RLVR algorithms on the results and the generalizability of the findings to other types of tasks or models.
- The paper does not include a discussion on the limitations of its approach, which could include the potential impact of different RLVR algorithms on the results and the generalizability of the findings to other types of tasks or models.
- The paper could benefit from a more detailed discussion on the limitations of its approach and how the findings might be influenced by different RLVR algorithms or other factors.

**Questions:**
- Could you provide more details on how the entropy threshold was determined and the rationale behind the choice of 20% of tokens for analysis?
- How does the proposed method compare with other RLVR algorithms, and what are the implications of these comparisons for the generalizability of the findings?
- Could you discuss the potential impact of different RLVR algorithms on the results and the generalizability of the findings to other types of tasks or models?
- How might the findings be influenced by the specific RLVR algorithm used, and what steps were taken to ensure the robustness of the results across different algorithms?
- Could you clarify the role of high-entropy tokens in the reasoning process and how they contribute to the model's performance?
- How does the paper's findings relate to the generalization capabilities of RLVR, and what implications might this have for the practical application of RLVR in real-world scenarios?

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
- Reasons: The paper provides a novel perspective on the role of token entropy in RLVR, which is a significant advancement in understanding the mechanisms of reasoning in LLMs. The experimental setup is robust, and the findings are supported by a comprehensive analysis of token entropy patterns. The proposed method of restricting policy gradient updates to forking tokens shows significant performance improvements, which is a valuable contribution to the field. The paper is well-written, easy to follow, and presents a clear and logical structure, making it accessible to a broad audience. The reviewers have highlighted the paper's originality, methodological soundness, and the significance of its results, which are supported by a thorough analysis and experimental evidence. The decision to accept is based on the paper's originality, methodological soundness, and the significance of its results, which are supported by a thorough analysis and experimental evidence.