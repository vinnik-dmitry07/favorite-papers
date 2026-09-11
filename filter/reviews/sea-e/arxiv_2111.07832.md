 **Summary:**
The paper introduces iBOT, a novel self-supervised framework for masked image modeling using an online tokenizer. This approach allows for the simultaneous training of the tokenizer and the model, which is a significant departure from traditional methods that require pre-training the tokenizer separately. The framework is evaluated on various downstream tasks such as image classification, object detection, and semantic segmentation, demonstrating competitive performance and robustness against common image corruptions. The methodology involves self-distillation on masked patch tokens and the class token, aiming to capture visual semantics. The paper also includes extensive experiments and ablation studies to validate the effectiveness of the proposed method.

**Strengths:**
- The paper introduces a novel approach to masked image modeling using an online tokenizer, which is a significant departure from traditional methods that require pre-training the tokenizer separately.
- The methodology is well-explained, with clear and detailed descriptions of the proposed method and its components.
- The paper presents extensive experiments and ablation studies that validate the effectiveness of the proposed method, showing improvements in performance and robustness.
- The visualization of attention maps and semantic patterns is well-executed, providing a clear demonstration of the method's capabilities.
- The paper is well-written, making it easy to follow, and includes a comprehensive literature review and comparison with existing methods.
- The proposed method achieves state-of-the-art results on various downstream tasks, demonstrating its effectiveness.

**Weaknesses:**
- The paper lacks a detailed comparison with other methods like BEiT and DINO, particularly in terms of the tokenizer's performance and the impact of different tokenization strategies.
- The paper could benefit from a more detailed discussion on the limitations of the proposed method and potential areas for future research.
- The paper does not sufficiently discuss the computational cost of the proposed method, which could be a significant concern for practical applications.
- There is a lack of clarity in the description of the online tokenizer and its role in the training process, which could confuse readers.
- The paper could benefit from a more thorough discussion on the scalability and generalizability of the method across different datasets and architectures.
- The paper does not sufficiently address the potential negative societal impacts of the proposed method.

**Questions:**
- Could the authors clarify the role and impact of the online tokenizer in the training process?
- How does the proposed method compare in terms of computational cost and training time with other methods like BEiT and DINO?
- Can the authors provide more details on the scalability and generalizability of the method across different datasets and architectures?
- How does the proposed method perform when applied to other datasets or architectures beyond those tested in the study?
- Could the authors discuss the potential negative societal impacts of the proposed method and how these might be mitigated?
- Can the authors provide more details on the limitations of the proposed method and potential areas for future research?

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
- Reasons: The paper presents a novel approach to masked image modeling using an online tokenizer, which is a significant departure from traditional methods. The methodology is well-explained, and the experiments and ablation studies validate the effectiveness of the proposed method. The paper achieves state-of-the-art results on various downstream tasks, demonstrating its effectiveness. The reviewers have highlighted the clarity of the paper and the novelty of the approach. However, concerns were raised about the lack of detailed comparison with other methods and the computational cost of the proposed method. These issues were addressed in the rebuttal, and the authors have provided additional results and clarifications. Based on these improvements, the paper is recommended for acceptance as a poster presentation.