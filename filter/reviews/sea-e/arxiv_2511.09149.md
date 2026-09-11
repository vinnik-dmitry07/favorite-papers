 **Summary:**
The paper introduces INTERLAT, a novel method for inter-agent communication in latent space, which leverages the last hidden states of a language model to transmit information between agents. This approach aims to improve communication efficiency and task performance by reducing the need for discrete tokens and enabling parallel reasoning. The method involves a compression process that allows for the transmission of compressed latent states, which can be decomposed into token embeddings and latent states for processing by a trainable self-attention and projection layer. The paper presents experiments on the ALFWorld benchmark, demonstrating that INTERLAT outperforms traditional methods like CoT and single-agent baselines. However, concerns were raised about the scalability of the method to larger agent teams and the potential for overfitting due to the use of similar models for both sender and receiver.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation and a novel approach to inter-agent communication in latent space.
- The method is innovative, enabling agents to communicate entirely in latent space, which is a significant advancement in the field of multi-agent systems.
- The experimental results are strong, demonstrating the effectiveness of the proposed method in improving task performance and communication efficiency.
- The paper is well-organized, with a clear presentation of the methodology and results, and includes comprehensive ablation studies and a detailed analysis of the training dynamics.
- The method's potential for reducing communication latency and improving task performance is highlighted, with a focus on the use of latent communication to enable parallel reasoning and reduce the need for discrete tokens.

**Weaknesses:**
- The paper lacks a detailed discussion on the scalability of the method to larger agent teams, which is a significant limitation given the potential for overfitting due to the use of similar models for both sender and receiver.
- The evaluation is limited to a single benchmark, which may not fully demonstrate the generalizability of the method across different scenarios and environments.
- The paper does not discuss the potential societal impacts of the proposed method, which could be significant given the potential for misuse or unintended consequences.
- The paper does not provide a detailed comparison with other methods for latent communication, which could help in understanding the relative advantages and disadvantages of the proposed method.
- The method's reliance on the availability of last-layer hidden states, which may not always be accessible in real-world scenarios, limits its applicability.

**Questions:**
- How does the method perform when scaled to larger agent teams? What are the potential challenges and limitations in such scenarios?
- Can the method be adapted to handle scenarios where the sender and receiver models are not identical? How might this affect the performance and scalability of the method?
- How does the method compare to other methods for latent communication in terms of performance, efficiency, and scalability?
- Could you provide more details on the training dynamics, particularly how the actor model learns to interpret latent communication effectively?
- How does the method handle the potential for overfitting due to the use of similar models for both sender and receiver?
- Can the method be adapted to handle scenarios where the sender and receiver models are not identical? How might this affect the performance and scalability of the method?
- How does the method ensure that the latent states transmitted between agents are not overly similar, which could lead to a lack of diversity in the information being communicated?

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
- Reasons: The paper presents a novel and innovative approach to inter-agent communication in latent space, which is a significant advancement in the field of multi-agent systems. The method is well-articulated, with clear experimental results demonstrating its effectiveness. While there are concerns about the scalability of the method to larger agent teams and the potential for overfitting, these are addressed in the paper, and the authors have provided a detailed response in the rebuttal. The decision to accept is based on the paper's originality, methodological soundness, and the significant impact it could have on the field. The decision is also supported by the positive feedback from the reviewers and the metareview, which highlights the paper's contribution to the understanding of latent communication in multi-agent systems.