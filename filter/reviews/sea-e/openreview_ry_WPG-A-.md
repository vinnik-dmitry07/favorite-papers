 **Summary:**
The paper critically examines the information bottleneck theory of deep learning, which posits that deep networks undergo a compression phase during training, characterized by a decrease in mutual information between the input and hidden layers. The authors challenge this theory by demonstrating that this compression is not a universal phenomenon across different activation functions and training methods. They show that the compression phase is not causally related to generalization and that it can occur even with full batch gradient descent, contradicting the notion that stochasticity is necessary for compression. The paper also explores how different nonlinearities affect the information dynamics in neural networks and how these dynamics relate to generalization performance.

**Strengths:**
- The paper provides a comprehensive analysis of the information dynamics in deep networks, challenging the common belief that deep networks undergo a compression phase during training.
- The authors have conducted extensive experiments and simulations to support their claims, demonstrating that the compression phase is not a universal phenomenon across different activation functions and training methods.
- The paper is well-written, clear, and easy to follow, making it accessible to a broad audience.
- The findings have significant implications for the field of deep learning, potentially leading to new insights and methodologies in the design and training of neural networks.
- The paper is original in its approach, providing a novel perspective on the information bottleneck theory of deep learning.

**Weaknesses:**
- The paper lacks a clear explanation of why the compression phase does not occur in networks with ReLU activations, and why it is not causally related to generalization.
- The paper's findings are not generalizable to other datasets or network architectures beyond those tested, limiting the scope of its applicability.
- The paper does not adequately address the role of noise in the information dynamics of neural networks, which is crucial for understanding the behavior of mutual information during training.
- The paper's experimental setup and the choice of activation functions are not well justified, and the results are not convincingly generalizable across different datasets and network architectures.
- The paper's claims about the causal relationship between compression and generalization are not convincingly supported by the evidence provided.
- The paper's presentation could be improved to better highlight the main contributions and to clarify the experimental setups and results.

**Questions:**
- Can the authors clarify the role of noise in the information dynamics of neural networks, particularly how it affects the mutual information between layers?
- How do the authors explain the observed differences in information dynamics between networks with different activation functions, such as tanh and ReLU?
- Could the authors provide more detailed explanations for the experimental setups and results, especially those that are not clearly described or not well understood?
- How do the authors justify the choice of activation functions and the experimental setups used in their study?
- Can the authors provide more evidence to support their claims about the causal relationship between compression and generalization?
- How do the authors address the concerns about the generalizability of their findings to other datasets and network architectures?

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
- Reasons: The paper provides a significant challenge to the existing theories of deep learning, particularly the information bottleneck theory, by demonstrating that the compression phase is not a universal phenomenon across different activation functions and training methods. The reviewers appreciated the clarity and depth of the experimental results, which are supported by extensive simulations. The paper is well-written and contributes to the understanding of deep learning dynamics. However, the paper could benefit from a more detailed discussion on the role of noise in information dynamics and a broader experimental validation across different datasets and network architectures. The decision to accept is based on the paper's originality, methodological soundness, and the significant impact it could have on the field of deep learning.