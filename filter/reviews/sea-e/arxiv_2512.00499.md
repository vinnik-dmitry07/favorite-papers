 **Summary:**
The paper introduces Entropy Importance Sampling Policy Optimization (ESPO), a novel method for optimizing reinforcement learning in large language models (LLMs) by grouping tokens based on entropy and using adaptive clipping to manage exploration and stability. ESPO decomposes sequences into groups using entropy, enabling Entropy Grouping Importance Sampling and Entropy Adaptive Clipping. These techniques aim to address the challenges of gradient underutilization in sequence-level optimization and instability in token-level optimization. The method was tested on mathematical reasoning benchmarks, showing improved performance and stability compared to existing methods. However, concerns were raised about the clarity of the paper's writing, the lack of detailed experimental results, and the potential for overfitting due to the use of a verifier.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation and a novel approach to addressing the challenges of gradient underutilization and instability in sequence-level and token-level optimization.
- The proposed method, ESPO, is simple, intuitive, and effective, showing improved performance on mathematical reasoning benchmarks compared to existing methods.
- The paper provides a comprehensive analysis of the proposed method, including ablation studies that demonstrate the effectiveness of the ESPO's components.
- The use of entropy as a criterion for grouping tokens is innovative and provides a natural way to measure uncertainty and optimize policy learning.
- The experiments are extensive, covering various model scales and architectures, and the results are convincing, showing that ESPO outperforms existing methods in most cases.

**Weaknesses:**
- The paper lacks detailed experimental results, particularly in the main text, which could be improved by including more detailed results in the appendix.
- There are several typographical and grammatical errors that need correction, which could affect the readability and professionalism of the paper.
- The paper could benefit from a more thorough discussion of related work, particularly in the area of entropy-based methods for token grouping.
- The paper does not sufficiently address the potential for overfitting due to the use of a verifier, which could limit the generalizability of the results.
- There is a lack of discussion on the computational efficiency of ESPO compared to other methods, and the paper does not provide a detailed comparison of training times or other efficiency metrics.
- The paper could benefit from a more detailed discussion on the limitations of the proposed method and potential future directions for research.

**Questions:**
- Could the authors clarify the definition and usage of the verifier in the context of the experiments, and discuss the potential for overfitting due to its use?
- How does the proposed method compare in terms of computational efficiency and training time to other methods, especially in large-scale language model training?
- Can the authors provide more detailed results on the performance of the proposed method across different model sizes and architectures, particularly in scenarios where the model capacity is limited?
- How does the proposed method handle the credit assignment problem in reinforcement learning, especially in scenarios where the reward signal is sparse or noisy?
- Could the authors discuss the potential for extending the method to other types of tasks beyond mathematical reasoning, such as dialogue or program synthesis?
- How does the proposed method compare to other entropy-based methods for token grouping, and what are the advantages or disadvantages of using entropy for grouping compared to other methods?

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
- Reasons: The paper presents a novel and effective method for optimizing reinforcement learning in large language models, addressing the challenges of gradient underutilization and instability in existing methods. The method, ESPO, is well-motivated, well-explained, and supported by extensive experiments that demonstrate its effectiveness. While there are concerns about the clarity of the paper and the potential for overfitting due to the use of a verifier, these issues do not significantly detract from the overall strength of the paper. The decision to accept is based on the originality of the method, its methodological soundness, and the significance of its results, despite the need for minor improvements in clarity and presentation.