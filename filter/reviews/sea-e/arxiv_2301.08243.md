 **Summary:**
The paper introduces a novel self-supervised learning method for image representation, termed Image-based Joint-Embedding Predictive Architecture (I-JEPA). This method involves predicting the representation of target blocks from a single context block, which is a departure from traditional methods that rely on hand-crafted data augmentations. The approach leverages a joint-embedding predictive architecture to learn semantic image representations, which are then evaluated on various downstream tasks such as linear probing, semi-supervised learning, and transfer learning. The method is shown to be scalable and efficient, with competitive performance on various benchmarks. However, concerns were raised about the novelty of the method and the clarity of its presentation, particularly in the explanation of certain technical aspects and the comparison with existing methods.

**Strengths:**
- The paper is well-written, with clear and well-structured content that effectively communicates the main ideas and results.
- The proposed method, I-JEPA, is simple yet effective, and the experiments conducted are extensive, demonstrating the method's scalability and efficiency.
- The method achieves good performance on various downstream tasks, including image classification, semi-supervised learning, and transfer learning, showing its versatility and applicability.
- The method's scalability is highlighted by its ability to be trained on larger datasets and models, which enhances its practical utility.
- The paper provides a detailed analysis of the method's performance and efficiency, including a comparison with other methods and an ablation study that helps in understanding the method's components.

**Weaknesses:**
- The paper lacks a clear explanation of the technical contributions and the rationale behind certain design choices, such as the masking strategy and the use of an exponential moving average target-encoder.
- The novelty of the method is questioned, as it appears to be a combination of existing methods like data2vec and context autoencoders, with limited technical innovation.
- The paper could benefit from more detailed visualizations and explanations of the predictor's outputs and the masking strategy to enhance understanding of the method's operation.
- There are inconsistencies and potential errors in the paper, such as typographical errors and unclear descriptions of the masking strategy and its impact on performance.
- The paper could be more comprehensive in its literature review and comparison with existing methods, particularly in explaining how it differs from or improves upon these methods.

**Questions:**
- Could the authors clarify the technical contributions of their method and how it differs from existing methods like data2vec and context autoencoders?
- How does the method perform when using different masking strategies, such as rasterized masking or random masking?
- Can the authors provide more detailed visualizations and explanations of the predictor's outputs and the masking strategy to help understand the method's operation?
- How does the method handle the potential for overfitting, especially in the context of the masking strategy?
- Could the authors elaborate on the method's scalability and efficiency, particularly in comparison to other methods that use different architectures or training strategies?
- How does the method perform when trained on different datasets or with different model architectures, and what are the implications for its generalizability and applicability?

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
- Reasons: The paper presents a novel approach to self-supervised learning from images, which is technically sound and shows competitive performance on various benchmarks. Despite some concerns about the novelty and clarity of presentation, the method's simplicity and scalability are highlighted as significant strengths. The decision to accept is supported by the paper's potential to contribute to the field, as it offers a new perspective on learning semantic image representations without relying on hand-crafted data augmentations. The decision is also influenced by the paper's overall positive reception, with reviewers acknowledging its potential impact and the method's practical utility.