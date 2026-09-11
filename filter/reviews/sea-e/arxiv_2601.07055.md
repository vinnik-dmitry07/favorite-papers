 **Summary:**
The paper introduces Dr. Zero, a novel framework for self-evolving search agents that do not require human-annotated training data. This framework leverages a proposer-solver setup where the proposer generates increasingly challenging questions, and the solver optimizes its responses using relative policy optimization. The approach is designed to minimize computational costs by clustering similar questions, thereby reducing the need for extensive data. The framework is evaluated against various QA benchmarks, showing competitive performance against supervised agents. However, concerns were raised about the clarity of the methodology, the novelty of the approach, and the fairness of the comparisons made.

**Strengths:**
- The paper is well-written, with clear explanations of the proposed methodology and its implementation.
- The approach of using a proposer-solver setup to generate and optimize questions is innovative and shows promise in reducing the need for extensive data.
- The paper is well-motivated, addressing the issue of data scarcity in training LLMs and proposing a method to generate questions without human-annotated data.
- The proposed method of using hop-grouped relative policy optimization (HRPO) is novel and effective, reducing computational costs by clustering similar questions.
- The paper provides extensive experimental results demonstrating the effectiveness of the proposed method, showing that it can match or surpass the performance of supervised search agents on several QA benchmarks.
- The paper is well-organized, making it easy to follow, and includes a detailed analysis of the training dynamics and performance across different iterations.

**Weaknesses:**
- The paper lacks clarity in explaining the methodology, particularly in the details of how the proposer generates questions and how the solver optimizes its responses.
- The novelty of the approach is questionable, as it resembles existing methods like R-Zero and SQLM, with similarities in the proposer-solver setup and the use of self-evolving language models.
- The paper does not adequately address the issue of reward hacking in the proposed method, which could lead to biased or ineffective training.
- There are concerns about the fairness of the comparisons made, particularly with the baselines, which may not be directly comparable due to differences in training data and methodologies.
- The paper does not sufficiently discuss the limitations of the proposed method, such as its applicability to different types of tasks and the potential for overfitting to the training data.
- The paper could benefit from more detailed explanations of the experimental setup, including the specifics of the search engine used and the generation of questions by the proposer.

**Questions:**
- Can the authors clarify how the proposer generates questions and how the solver optimizes its responses, particularly in terms of the specific algorithms and methodologies used?
- How does the proposed method address the issue of reward hacking, and what measures have been taken to ensure that the training remains effective and unbiased?
- Could the authors provide more details on the experimental setup, including the specifics of the search engine used and the generation of questions by the proposer?
- How does the proposed method perform when applied to different types of tasks, and what are the implications of using a different search engine or a different base model?
- Can the authors discuss the potential for overfitting to the training data and how this might affect the generalizability of the results?
- How does the proposed method compare to other data-free methods, particularly in terms of computational efficiency and performance?

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
- Reasons: The paper introduces a novel framework for self-evolving search agents that addresses the challenge of data scarcity in training LLMs. The methodology is innovative, showing promise in reducing computational costs and improving performance on QA benchmarks. Despite some concerns about clarity and novelty, the paper is well-received for its technical soundness and potential impact on the field. The decision to accept is based on the paper's originality, methodological soundness, and the significance of its results, as well as the clarity and logic of its presentation. The decision is also influenced by the positive feedback from reviewers, who have highlighted the paper's contributions and potential for further research.