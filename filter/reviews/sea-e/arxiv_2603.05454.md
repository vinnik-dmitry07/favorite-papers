 **Summary:**
The paper introduces the Longest Stable Prefix (LSP) scheduler, a novel approach to inference in Diffusion Language Models (DLMs) that addresses the bottleneck of scattered acceptance, which fractures the Key-Value (KV) cache and destroys memory locality. LSP evaluates token stability via a single forward pass, identifies a contiguous left-aligned block of stable predictions, and snaps its boundary to natural linguistic or structural delimiters before committing. This method reduces token flip rates and denoiser calls, accelerating inference while maintaining or slightly improving output quality. Extensive evaluations on LLaDA-8B and Dream-7B demonstrate that LSP significantly reduces end-to-end latency and memory traffic, making it a promising method for improving the efficiency of DLM inference.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation and a well-explained methodology.
- The proposed LSP scheduler is simple, effective, and model-agnostic, applicable to any diffusion model, making it a versatile tool for improving inference efficiency.
- The paper provides a thorough evaluation of the LSP scheduler, demonstrating its effectiveness in reducing end-to-end latency and memory traffic while maintaining or slightly improving output quality compared to strong parallel baselines.
- The authors have conducted extensive ablation studies to validate the importance of each of the core design components of the LSP scheduler, providing a robust foundation for its implementation and application.
- The paper is well-organized, with a clear structure and a comprehensive literature review that positions the work well within the current research landscape.

**Weaknesses:**
- The paper lacks a detailed discussion on the limitations of the proposed method, which could provide a more balanced view of its applicability and effectiveness.
- The evaluation of the LSP scheduler is limited to two models (LLaDA-8B and Dream-7B), which might not fully demonstrate the generalizability of the method across different model architectures and sizes.
- The paper does not discuss the computational cost of the LSP scheduler, which could be a significant concern for large-scale DLMs.
- There is a lack of discussion on the scalability of the LSP scheduler with larger models, which could affect its practical applicability in real-world scenarios.
- The paper does not provide a detailed discussion on the potential negative societal impacts of the proposed method, which could be a concern for some readers.
- The paper could benefit from a more detailed discussion on the potential limitations and challenges of the LSP scheduler, such as its applicability to different types of tasks and its scalability with larger models.

**Questions:**
- Could the authors provide more details on the computational cost of the LSP scheduler, especially in comparison to other methods like Scattered-Margin?
- How does the LSP scheduler perform with larger models, and what are the potential challenges or limitations in scaling it up?
- Is there a way to adapt the LSP scheduler for bidirectional in-filling tasks, and how might this affect its performance?
- How does the LSP scheduler compare to other methods like Prophet in terms of computational efficiency and output quality?
- Can the authors provide more details on the scalability of the LSP scheduler with larger models, and discuss any potential challenges or limitations in scaling it up?
- Is there a possibility to extend the LSP scheduler to support "stable islands" for bidirectional in-filling, and how might this affect its performance?

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
- Reasons: The paper presents a novel and effective approach to inference in Diffusion Language Models, addressing a significant bottleneck in the scattered acceptance process. The LSP scheduler, as proposed, demonstrates a significant improvement in inference speed while maintaining or slightly improving output quality. The methodology is well-explained, and the evaluations are robust, showing the effectiveness of the approach across different models and tasks. The paper is well-written, clear, and easy to follow, making it accessible to a broad audience. The reviewers have highlighted the simplicity and effectiveness of the LSP scheduler, and the paper's contribution to the field is significant. The decision to accept is based on the originality of the approach, methodological soundness, and the significance of the results, along with the clarity and logic of the presentation.