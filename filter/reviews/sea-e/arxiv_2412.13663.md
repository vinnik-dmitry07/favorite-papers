 **Summary:**
The paper introduces ModernBERT, an encoder-only model designed for both classification and retrieval tasks. ModernBERT leverages recent advancements in transformer architectures, including GeGLU, RoPE, and alternating attention, to achieve state-of-the-art performance on various benchmarks. It is trained on a large dataset of 2 trillion tokens, which allows for a sequence length of 8192 tokens, a significant improvement over previous models. ModernBERT's efficiency is highlighted by its ability to process long sequences quickly and its compatibility with modern hardware like GPUs. The model's design is hardware-aware, optimizing for inference on common GPUs. Despite its strengths, the paper is criticized for its limited novelty and the lack of detailed ablation studies, which could better clarify the contributions of individual components.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a comprehensive evaluation across various tasks such as GLUE, retrieval, and code-related tasks.
- ModernBERT achieves state-of-the-art performance on a wide range of benchmarks, including GLUE, retrieval, and code-related tasks, demonstrating its effectiveness across different domains.
- The model is efficient in terms of inference speed, which is crucial for practical applications, and it is compatible with modern hardware like GPUs, enhancing its utility.
- The paper includes a thorough analysis of the model's performance and efficiency, providing insights into the benefits of using a large-scale pretraining dataset and the impact of different model architectures.
- The authors have made the codebase available, which is beneficial for further research and development in the field.

**Weaknesses:**
- The paper lacks novelty as it primarily combines existing techniques without significant innovation. The contributions are seen as incremental rather than groundbreaking.
- There is a lack of detailed ablation studies, which could help clarify the specific contributions of each component of ModernBERT and provide a deeper understanding of its design.
- The paper does not adequately address the limitations of the model, particularly concerning its generalization to other languages and its potential biases due to the training data.
- The paper could benefit from a more thorough discussion on the impact of different model architectures and training strategies, as well as a more detailed comparison with other models like GTE-en-MLM.
- There is a need for more comprehensive evaluations, especially on larger datasets and more diverse tasks, to fully demonstrate the model's capabilities and limitations.

**Questions:**
- Can the authors provide more details on the specific contributions of each component of ModernBERT, particularly in terms of performance improvements and efficiency gains?
- How does ModernBERT handle different languages beyond English, and what are the plans for adapting it to other languages?
- Could the authors elaborate on the design choices, such as the use of GeGLU and RoPE, and how these contribute to the model's performance and efficiency?
- How does ModernBERT compare to other models like GTE-en-MLM, especially in terms of training data, model architecture, and performance metrics?
- What are the plans for future research and development of ModernBERT, and how do the authors plan to address the identified limitations and potential biases in the model?

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
- Reasons: The paper presents a well-executed and efficient encoder-only model, ModernBERT, which demonstrates state-of-the-art performance on various benchmarks and is compatible with modern hardware. Despite some concerns about the novelty and the depth of the ablation studies, the paper is technically solid and provides valuable insights into the design of efficient transformer models for retrieval tasks. The decision to accept is supported by the overall positive reception of the paper's contributions and its potential impact on the field. The decision aligns with the metareview, which highlights the paper's strengths and the incremental nature of its contributions.