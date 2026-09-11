 **Summary:**
The paper introduces NorMuon, a novel optimizer that combines the orthogonalization capabilities of Muon with the adaptive learning rates of Adam, aiming to improve training efficiency and reduce computational costs in large language models (LLMs). NorMuon maintains a balance between orthogonalization and adaptive learning rates, which are typically seen as conflicting approaches. The authors demonstrate that NorMuon outperforms both Adam and Muon in terms of training efficiency and memory footprint, particularly in large-scale models. The paper also presents a distributed implementation of NorMuon under the FSDP2 framework, which facilitates efficient orthogonalization computations across devices. The experimental results show that NorMuon significantly improves training efficiency, with up to 21.74% better efficiency than Adam and 11.31% improvement over Muon in a 1.1B pretraining setting.

**Strengths:**
- The paper introduces NorMuon, a novel optimizer that combines the orthogonalization capabilities of Muon with the adaptive learning rates of Adam, which is a significant advancement in the field of optimizer design for large-scale deep learning.
- The authors provide a clear and detailed explanation of the proposed method, including a well-structured algorithm and a comprehensive analysis of the computational and memory overheads.
- The paper is well-written, making it easy to follow, and includes a detailed analysis of the computational and memory overheads of NorMuon, which is crucial for understanding its practical applicability.
- The experimental results demonstrate that NorMuon outperforms both Adam and Muon in terms of training efficiency and memory footprint, particularly in large-scale models, indicating its potential for practical deployment.
- The paper includes a detailed analysis of the properties of the update matrices from different optimizers during pretraining, which provides valuable insights into the behavior of the optimizers and the impact of the proposed method.

**Weaknesses:**
- The paper lacks a detailed discussion on the limitations of NorMuon, which is crucial for understanding the scope and applicability of the proposed method.
- The paper does not provide a detailed comparison with other optimizers like Lion and GaLore, which could have provided a more comprehensive evaluation of NorMuon's performance.
- The paper does not include a comparison of training time or a detailed analysis of the computational and memory overheads of NorMuon, which could have provided a more robust evaluation of its practical applicability.
- The paper does not include a discussion on the limitations of the proposed method, which could help in understanding the scope and applicability of the proposed method.
- The paper does not include a discussion on the limitations of the proposed method, which could help in understanding the scope and applicability of the proposed method.

**Questions:**
- Could you elaborate on the limitations of NorMuon and scenarios where it might not be the most effective optimizer?
- How does NorMuon perform in terms of training time compared to other optimizers like Adam and Muon?
- Can you provide a more detailed comparison of NorMuon with other optimizers like Lion and GaLore, particularly in terms of computational and memory overheads?
- What are the specific advantages of NorMuon over other optimizers in terms of training efficiency and memory footprint?
- Can you provide more details on the computational and memory overheads of NorMuon, particularly in terms of how these overheads scale with model size and training data size?
- How does the proposed method handle the issue of neuron norms becoming too large during training, and what are the implications of this on the overall training process?

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
- Reasons: The paper presents a novel optimizer, NorMuon, which effectively combines the orthogonalization capabilities of Muon with the adaptive learning rates of Adam, demonstrating significant improvements in training efficiency and memory footprint. The experimental results are robust, showing that NorMuon outperforms both Adam and Muon in terms of training efficiency and memory usage. The paper is well-written, making it accessible and easy to understand, and includes a detailed analysis of the computational and memory overheads. The proposed distributed implementation under the FSDP2 framework is innovative and practical, addressing the challenges of large-scale training. Despite some limitations such as the lack of a detailed discussion on the limitations of NorMuon and a more comprehensive comparison with other optimizers, the paper's contributions are significant and the methodological soundness and clarity of presentation are commendable. The decision to accept is based on the originality of the approach, the methodological soundness, and the significance of the results, as well as the clarity and logic of the presentation.