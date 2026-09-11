 **Summary:**
The paper introduces a novel framework called Mixture-of-Recursions (MoR), which integrates parameter sharing, adaptive recursion depth, and efficient KV caching to enhance the efficiency of language models. MoR dynamically assigns recursion depths to individual tokens, allowing for adaptive computation and memory savings. The framework is evaluated across various model scales, demonstrating improvements in validation loss and few-shot accuracy while reducing training FLOPs and memory footprint. The paper also explores different routing strategies and KV caching methods, aiming to optimize computational efficiency and reduce memory usage. Despite its strengths, the paper is criticized for its limited novelty and lack of comprehensive comparisons with existing methods.

**Strengths:**
- The paper introduces a novel framework called Mixture-of-Recursions (MoR), which effectively unifies parameter sharing, adaptive recursion depth, and efficient KV caching within a single framework.
- MoR's dynamic recursion routing allows for token-specific recursion depths, which is a significant advancement over traditional fixed recursion depths.
- The paper provides extensive empirical validation, demonstrating that MoR outperforms vanilla and recursive baselines across various model scales and computational budgets.
- MoR's routing mechanism facilitates adaptive reasoning along the model's vertical axis, enabling models to efficiently adjust their thinking depth on a per-token basis.
- The paper is well-written, easy to follow, and provides a comprehensive evaluation of the proposed method, including a detailed analysis of its strengths and limitations.

**Weaknesses:**
- The paper lacks a comprehensive comparison with existing methods, particularly in terms of training and inference efficiency, which could provide a more robust evaluation of MoR's effectiveness.
- The novelty of the paper is somewhat limited as it builds upon existing works like recursive transformers and Mixture-of-Depths (MoD).
- The paper does not adequately discuss the limitations of the proposed method, which could provide valuable insights into its practical applicability and potential drawbacks.
- The paper's experimental setup and results are not clearly explained, particularly in the ablation studies, which could benefit from more detailed analysis and clarity.
- There is a lack of discussion on the computational and memory costs associated with the additional routing and caching mechanisms introduced by MoR.
- The paper's claims about the efficiency of MoR are not convincingly supported by the experimental results, which do not consistently demonstrate superior performance over existing methods.

**Questions:**
- Could the authors provide a more detailed comparison with existing methods, particularly in terms of training and inference efficiency, to better establish the effectiveness of MoR?
- How does MoR compare to other methods in terms of computational and memory efficiency, especially when considering the additional routing and caching mechanisms?
- Can the authors clarify the experimental setup and results, particularly in the ablation studies, to better understand the impact of different routing and caching strategies on model performance?
- How does MoR handle the trade-off between computational efficiency and model performance, especially in scenarios where the model's depth is increased?
- Could the authors discuss the limitations of MoR in more detail, including potential drawbacks and challenges in practical deployment?

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
- Reasons: The paper presents a novel framework, Mixture-of-Recursions (MoR), which effectively integrates parameter sharing, adaptive recursion depth, and efficient KV caching to enhance the efficiency of language models. The framework shows promising results in terms of validation loss and few-shot accuracy, while reducing training FLOPs and memory footprint. The paper is well-written, easy to follow, and provides a comprehensive evaluation of the proposed method. However, the reviewers have highlighted some concerns regarding the novelty and the lack of comprehensive comparisons with existing methods. These issues were addressed during the rebuttal phase, and the authors have provided additional results and clarifications. Based on these improvements and the overall positive feedback from the reviewers, the paper is recommended for acceptance, particularly as a poster presentation.