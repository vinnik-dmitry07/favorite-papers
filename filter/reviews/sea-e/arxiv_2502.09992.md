 **Summary:**
The paper introduces LLaDA, a diffusion model for language modeling that challenges the dominance of autoregressive models (ARMs) by proposing a masked diffusion model (MDM) trained from scratch under the pre-training and supervised fine-tuning (SFT) paradigm. LLaDA employs a forward data masking process and a reverse generation process, using a Transformer to predict masked tokens, which provides a principled generative approach for probabilistic inference by optimizing a likelihood lower bound. The model demonstrates competitive performance across various benchmarks, including math, code, and general tasks, and shows strong scalability and in-context learning capabilities. It also addresses the reversal curse and exhibits impressive instruction-following abilities in case studies, such as multi-turn dialogue.

**Strengths:**
- The paper introduces a novel approach to language modeling using a diffusion model, which challenges the dominance of autoregressive models and provides a fresh perspective on the capabilities of large language models (LLMs).
- The methodology is well-articulated, with clear explanations of the model's architecture, training, and inference processes, making it accessible to readers.
- The paper is well-written, with a clear motivation and a comprehensive evaluation that demonstrates the scalability and effectiveness of the proposed model across various tasks.
- The authors provide a detailed analysis of the model's performance, including comparisons with existing models and a thorough discussion on the model's capabilities and limitations.
- The paper includes a variety of experiments and ablation studies that support the claims made, and the results are convincing, showing the model's effectiveness in handling reversal reasoning tasks.

**Weaknesses:**
- The paper lacks a detailed discussion on the computational cost of the proposed method compared to autoregressive models, which is crucial for understanding the practical implications of using diffusion models.
- There is a lack of clarity in the presentation of the model's architecture and training details, which could make it difficult for readers to fully understand the model's design and implementation.
- The paper does not adequately address the limitations of the model, particularly in terms of its scalability and the potential for further improvements.
- The paper could benefit from more detailed comparisons with other diffusion models, such as those mentioned in related works, to better position the proposed model within the existing literature.
- The paper does not provide sufficient details on the training data and its quality, which is crucial for understanding the model's performance and generalizability.

**Questions:**
- Could the authors provide more details on the computational cost of the proposed method compared to autoregressive models, including the number of FLOPs required for training and inference?
- How does the model handle the reversal curse in other tasks beyond the examples provided in the paper?
- Can the authors clarify the discrepancies in the model's performance on different tasks, particularly the lower performance on some tasks compared to others?
- How does the model's performance compare when using different sampling strategies, such as autoregressive sampling versus pure diffusion sampling?
- Could the authors provide more details on the training data and its quality, including the sources and characteristics of the data used for pre-training and fine-tuning?
- How does the model perform when using different model sizes, and what are the implications of these differences in terms of performance and computational efficiency?

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
- Reasons: The paper presents a compelling alternative to autoregressive models with the LLaDA model, which demonstrates competitive performance across various benchmarks and offers a novel approach to language modeling using diffusion models. The methodology is well-articulated, and the results are convincing, showing the scalability and effectiveness of the proposed model. The paper is well-written and provides a thorough evaluation, making it a valuable contribution to the field. The decision to accept is based on the originality of the approach, methodological soundness, and the significance of the results, despite some concerns regarding the clarity of the presentation and the need for more detailed comparisons with other models.