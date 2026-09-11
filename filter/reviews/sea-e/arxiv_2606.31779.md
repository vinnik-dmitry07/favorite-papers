 **Summary:**
The paper introduces LOTUS, a novel method for latent chain-of-thought (CoT) reasoning, which utilizes a looped padded Transformer to process multiple latent blocks in parallel, each containing a fixed number of tokens. This method is designed to bridge the gap between latent and explicit CoT reasoning, achieving performance comparable to explicit CoT on the GSM8K benchmark while reducing inference latency. The approach involves a supervision loss that aligns the latent representations with the gold CoT tokens, and an auxiliary decoder for training-time supervision. Extensive experiments and ablation studies are conducted to validate the effectiveness of LOTUS, demonstrating its ability to recover gold CoT steps and perform well on various benchmarks.

**Strengths:**
- The paper addresses a significant problem in the field of latent reasoning, specifically focusing on the gap between latent and explicit CoT reasoning.
- The proposed method, LOTUS, is innovative and well-motivated, providing a novel approach to latent reasoning that is supported by thorough experiments and ablation studies.
- The paper is well-written, making it easy to follow, and the experiments are extensive, covering various aspects of the proposed method.
- The method demonstrates a good balance between accuracy and latency, showing a significant reduction in inference latency compared to explicit CoT methods.
- The paper provides a detailed analysis of the latent representations, showing that they are interpretable and aligned with the gold CoT steps.

**Weaknesses:**
- The paper lacks a detailed comparison with existing methods, particularly in terms of the number of parameters and computational resources used, which could affect the fairness of the comparisons.
- The method's performance on longer CoT chains (>6 steps) is not addressed, which could limit its applicability in more complex reasoning tasks.
- The paper does not discuss the scalability of the method with larger models or different model architectures, which could affect its generalizability.
- Some parts of the paper are not clearly explained, such as the role of the auxiliary decoder and the choice of hyperparameters like the number of latent blocks and the number of tokens per block.
- The paper's claims about the method's ability to recover gold CoT steps and its alignment with the gold CoT are not convincingly supported by the experimental results.

**Questions:**
- Could the authors clarify the role of the auxiliary decoder in the training process and its impact on the model's performance?
- How does the method perform on longer CoT chains, and what are the potential challenges or limitations in scaling the method to larger models or different architectures?
- Can the authors provide more details on the hyperparameter choices, especially the number of latent blocks and tokens per block, and how these choices affect the model's performance?
- How does the method compare in terms of computational resources and parameter count with other methods, and what are the implications of these differences for practical deployment?
- Could the authors elaborate on the method's ability to recover gold CoT steps and its alignment with the gold CoT, particularly in light of the experimental results presented?

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
- Reasons: The paper presents a novel approach to latent reasoning that addresses the gap between latent and explicit CoT reasoning, showing promising results in terms of performance and latency reduction. The method is well-motivated and supported by thorough experiments and ablation studies. While there are concerns about the scalability of the method and the fairness of some comparisons, the paper's contributions are significant enough to warrant acceptance, especially considering the potential of the proposed method to advance the field of latent reasoning. The decision aligns with the reviewers' consensus and the metareview, which highlights the paper's originality and methodological soundness.