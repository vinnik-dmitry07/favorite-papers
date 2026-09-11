 **Summary:**
The paper introduces VeriFree, a novel method for training large language models (LLMs) in general reasoning tasks without the need for rule-based or model-based verifiers. VeriFree optimizes the probability of generating the correct answer directly, which is a departure from traditional methods that rely on verifier models. This approach is shown to be effective in enhancing the reasoning capabilities of LLMs across various benchmarks, including MMLU-Pro, GPQA, SuperGPQA, and math-related benchmarks. The paper also discusses the computational efficiency and robustness of VeriFree compared to traditional methods, demonstrating its potential to reduce computational requirements and improve performance.

**Strengths:**
- The paper is well-written, making it easy to follow and understand the proposed methodology.
- The proposed method, VeriFree, is novel and innovative, providing a new approach to training LLMs for general reasoning tasks without the need for verifier models.
- VeriFree demonstrates significant improvements in performance across various benchmarks, showing its effectiveness in enhancing the reasoning capabilities of LLMs.
- The method is computationally efficient, requiring fewer computational resources compared to traditional methods that rely on verifier models.
- The paper provides a thorough analysis of the proposed method, including a detailed derivation of the VeriFree objective and a discussion on the variance reduction of the estimator.
- The experiments are well-designed, demonstrating the effectiveness of VeriFree in improving the reasoning capabilities of LLMs.

**Weaknesses:**
- The paper lacks a detailed discussion on how the method handles multiple correct answers, which is a significant limitation in real-world applications.
- The paper does not provide a detailed analysis of the computational overhead introduced by VeriFree compared to traditional methods, which could be crucial for understanding its practical applicability.
- The paper does not include a discussion on the potential societal impacts of the proposed method, which is an important consideration for any new technology.
- The paper does not provide a detailed analysis of the limitations of the proposed method, which could help in understanding its scope and applicability.
- The paper does not include a discussion on how the method handles the potential for reward hacking, which is a significant concern in the context of LLM training.
- The paper does not include a discussion on how the method handles the potential for overfitting to the training data, which is a common issue in LLM training.

**Questions:**
- Can the authors provide more details on how VeriFree handles multiple correct answers? How does it ensure that the model does not get stuck in a local optimum where only one correct answer is generated?
- How does the computational overhead of VeriFree compare to traditional methods? What are the specific computational requirements of VeriFree, and how do they compare to those of traditional methods?
- Can the authors provide a detailed analysis of the potential societal impacts of VeriFree? How might this method be used in ways that could have negative societal impacts, and how can these impacts be mitigated?
- How does VeriFree handle the potential for reward hacking? What steps have been taken to ensure that the model does not learn to generate answers that are correct in form but not in substance?
- Can the authors provide a detailed analysis of the limitations of VeriFree? What are the specific scenarios where VeriFree might not be effective, and how can these scenarios be avoided?
- How does VeriFree handle the potential for overfitting to the training data? What steps have been taken to ensure that the model does not learn to generate answers that are correct only in the training data and not in general?

**Soundness:**
3 good

**Presentation:**
3 good

**Contribution:**
3 good

**Rating:**
8 accept, good paper

**Paper Decision:**
- Decision: Accept
- Reasons: The paper presents a novel and effective method for training LLMs in general reasoning tasks without the need for verifier models, which is a significant advancement in the field. The method, VeriFree, is shown to be computationally efficient and effective in enhancing the reasoning capabilities of LLMs across various benchmarks. The paper is well-written and provides a thorough analysis of the proposed method, making it a valuable contribution to the field. The reviewers have highlighted some limitations and suggested areas for improvement, which the authors have addressed in their rebuttal. The decision to accept is based on the paper's originality, methodological soundness, significance of results, and clarity and logic of presentation.