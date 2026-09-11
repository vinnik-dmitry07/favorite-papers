 **Summary:**
The paper investigates the performance of large language models (LLMs) in handling multi-operand addition, focusing on the heuristic used by LLMs to predict the first digit of the result. The authors propose that LLMs rely on a one-digit lookahead strategy, which is effective for two-operand addition but inadequate for multi-operand cases due to the complexity of carry-over logic. The paper presents empirical evidence through probing experiments and digit-wise accuracy evaluations, demonstrating that LLMs struggle with multi-operand addition. The authors also discuss the impact of tokenization strategies on arithmetic performance and the inherent limitations of LLMs in handling more complex numerical reasoning.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear and concise presentation of the problem and the proposed solution.
- The authors provide a novel insight into the heuristic used by LLMs in handling multi-operand addition, which is a significant contribution to the field.
- The paper includes a comprehensive set of experiments that demonstrate the effectiveness of the proposed heuristic in explaining the performance of LLMs in arithmetic tasks.
- The findings are supported by a detailed analysis of the impact of tokenization strategies on arithmetic performance, which adds depth to the understanding of LLM limitations.
- The paper is well-organized, with clear figures and tables that aid in understanding the results and the methodology used.

**Weaknesses:**
- The paper lacks a discussion on the limitations of the proposed heuristic, particularly in terms of its applicability to other arithmetic operations and its impact on general language generation tasks.
- The experiments are limited to the addition task, and it is unclear whether the proposed heuristic would hold for other arithmetic operations such as subtraction.
- The paper does not provide a detailed discussion on the potential reasons for the observed performance drop in LLMs, which could be due to factors other than the heuristic used.
- The paper could benefit from a more thorough discussion on the implications of the findings and potential future directions for research.
- The paper does not address the potential impact of the heuristic on other tasks beyond arithmetic, which could be a significant limitation if the heuristic is found to affect general language generation tasks.

**Questions:**
- How does the proposed heuristic perform in other arithmetic operations, such as subtraction?
- Could the authors provide a more detailed discussion on the limitations of the proposed heuristic and its potential impact on other tasks beyond arithmetic?
- How does the heuristic perform in zero-shot and one-shot settings, and what are the implications of these settings for the effectiveness of the heuristic?
- Can the authors provide more detailed experimental results, such as the accuracy of predicting the first digit of the result in multi-operand addition, to support the claims made in the paper?
- How does the heuristic perform in larger models within the same family, and what are the implications of this for the scalability of the findings?
- Could the authors provide a more detailed discussion on the potential reasons for the observed performance drop in LLMs, and how this relates to the heuristic used?

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
- Reasons: The paper provides a valuable contribution to the understanding of LLMs' performance in arithmetic tasks, specifically focusing on the heuristic used by LLMs in multi-operand addition. The empirical evidence presented supports the proposed heuristic, and the paper is well-written and easy to follow. The findings are significant and could guide future research on improving LLMs' performance in arithmetic tasks. The reviewers have highlighted the paper's clarity, the novelty of the insights, and the thoroughness of the experiments. However, the paper could benefit from a more detailed discussion on the limitations of the proposed heuristic and its impact on other tasks beyond arithmetic. The decision to accept is based on the paper's originality, methodological soundness, and the significance of the results, with the recommendation for a poster presentation to allow for further discussion and feedback.