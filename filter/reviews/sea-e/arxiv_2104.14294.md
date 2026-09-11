 **Summary:**
The paper introduces DINO, a self-supervised learning method for Vision Transformers (ViTs) that leverages a momentum encoder and multi-crop training to enhance the performance of ViTs on various downstream tasks. DINO is designed to improve the quality of features in ViTs, making them suitable for tasks like k-NN classification and retrieval. The methodology involves a dynamic teacher network that is updated using an exponential moving average of the student network, which helps in avoiding collapse and enhancing the learning process. The paper also explores the use of smaller patches in ViTs, which is a novel approach that has been shown to improve performance. The experiments conducted on ImageNet and other datasets demonstrate the effectiveness of DINO, although the paper could benefit from a more detailed discussion on the novelty and the computational efficiency of the method.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation and a well-designed methodology.
- The proposed method, DINO, is simple yet effective, and the results are promising, showing improvements over existing methods.
- The paper includes a comprehensive set of experiments, including ablation studies, which help in understanding the impact of different components of the method.
- The use of a momentum encoder and multi-crop training is highlighted as a significant contribution to the field of self-supervised learning for ViTs.
- The paper provides a detailed analysis of the training dynamics and the role of different components in the method, which is valuable for understanding the method's effectiveness.

**Weaknesses:**
- The paper could benefit from a more detailed discussion on the novelty of the method, particularly in relation to existing works such as BYOL and the use of momentum encoders.
- The computational efficiency of DINO compared to other methods is not discussed, which is a significant concern given the computational demands of ViTs.
- The paper could provide more detailed explanations and justifications for certain design choices, such as the use of a momentum encoder and the choice of hyperparameters.
- The paper lacks a detailed comparison with other self-supervised learning methods, particularly those that use similar components like momentum encoders and multi-crop training.
- The paper does not adequately address the issue of model collapse, which is a known problem in self-supervised learning.
- The paper could benefit from a more comprehensive discussion on the limitations of the method and potential future directions for research.

**Questions:**
- Could the authors clarify the role of the momentum encoder in the method and how it differs from similar components in other methods like BYOL?
- How does the proposed method compare in terms of computational efficiency with other self-supervised learning methods for ViTs?
- Can the authors provide more details on the training dynamics and the role of different components in avoiding model collapse?
- How does the proposed method perform on other datasets beyond ImageNet, and what are the implications for its generalizability?
- Could the authors discuss the potential for extending the method to other architectures, such as ResNet-50, and how this might impact the results?
- What are the potential applications of the method beyond image classification, and how might it be adapted for other tasks like object detection or segmentation?

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
- Reasons: The paper presents a novel approach to self-supervised learning for ViTs, which is both innovative and effective. The use of a momentum encoder and multi-crop training is highlighted as a significant contribution to the field. The paper is well-written, clear, and easy to follow, making it accessible to a broad audience. The experiments conducted are comprehensive, and the results are promising, showing improvements over existing methods. The method's simplicity and effectiveness, along with its potential for broader applications, make it a valuable contribution to the field. However, the paper could benefit from a more detailed discussion on the novelty and a more comprehensive comparison with other methods. The decision to accept is based on the paper's originality, methodological soundness, and the significance of its results, as well as the clarity and logic of its presentation.