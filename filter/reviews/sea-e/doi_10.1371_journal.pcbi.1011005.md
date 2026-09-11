 **Summary:**
The paper explores the use of spiking neurons in causal inference and learning, focusing on how the discontinuous nature of spiking can be leveraged to estimate causal effects. The authors propose a method that uses the thresholded response of a neuron to estimate its unique contribution to a reward signal, separating it from other neurons whose activity it may be correlated with. This method is inspired by methods from econometrics and is tested in simple models, showing that it can be used to approximate gradient descent-based learning. The paper also discusses how this approach might be applicable to more complex tasks and networks, although the current experiments are limited to simple models.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear and well-motivated problem statement.
- The idea of using spiking neurons to estimate causal effects is novel and interesting, potentially providing a new perspective on how neurons in the brain might perform causal inference.
- The paper is well-supported by both theoretical and empirical evidence, with clear figures and a logical flow of ideas.
- The authors have provided a clear explanation of the methodology and its implications, which is helpful for understanding the proposed approach.
- The paper is timely and relevant, addressing an important problem in the field of computational neuroscience.

**Weaknesses:**
- The paper lacks a thorough discussion of related work, particularly in the area of causal inference and spiking neural networks, which could have provided a richer context for the research.
- The experimental setup is limited to simple models, which may not fully demonstrate the applicability of the proposed method to more complex tasks or networks.
- The paper could benefit from a more detailed discussion on the limitations of the proposed method and how it might be extended to more complex scenarios.
- There is a lack of discussion on the biological plausibility of the proposed method, which could be a significant concern for some readers.
- The paper could be improved by including more detailed explanations of the mathematical derivations and the assumptions made in the models.

**Questions:**
- Can the authors clarify the assumptions made in the models and how they relate to the biological plausibility of the proposed method?
- How does the proposed method compare to other methods for credit assignment in spiking neural networks, such as those based on spike-time-dependent plasticity?
- Could the authors provide more details on the biological plausibility of the proposed method, particularly in terms of how it might be implemented in real neural networks?
- How does the method perform in more complex tasks or networks, and what are the limitations of its applicability?
- Could the authors discuss the potential implications of their findings for the field of computational neuroscience, particularly in terms of how it might influence our understanding of neural network dynamics and learning?

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
- Reasons: The paper presents a novel approach to causal inference using spiking neurons, which is both theoretically interesting and potentially biologically plausible. The methodology is well-explained, and the paper is well-written, making it accessible and easy to follow. The experimental results, while limited to simple models, provide a solid foundation for further exploration of this approach in more complex scenarios. The paper's contribution to the field is significant, as it offers a new perspective on how neurons might perform causal inference, which is a critical aspect of neural network dynamics and learning. The decision to accept is based on the paper's originality, methodological soundness, and the significance of its results, despite some concerns regarding the scope of the experiments and the need for more extensive biological validation.