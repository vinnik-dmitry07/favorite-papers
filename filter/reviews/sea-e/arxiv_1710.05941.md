 **Summary:**
The paper introduces a novel activation function named SWiSH, which is a composition of a sigmoid function and a linear function, discovered through automated search techniques. The authors conducted extensive experiments to validate the effectiveness of SWiSH, comparing it against other activation functions such as ReLU, ELU, and GELU. The paper presents a comprehensive evaluation of SWiSH across various datasets and models, demonstrating its superiority in some cases. However, the paper has been critiqued for its limited novelty, as the SWiSH function is a combination of existing functions, and the methodology used for its discovery is not sufficiently detailed. The paper also lacks a thorough discussion on the theoretical underpinnings of SWiSH and its generalizability across different architectures and datasets.

**Strengths:**
- The paper is well-written, clear, and easy to follow, making it accessible to a broad audience.
- The proposed activation function, SWiSH, is simple, intuitive, and easy to implement, requiring only a single line of code change.
- The paper provides a comprehensive evaluation of SWiSH across various datasets and models, demonstrating its effectiveness and generalizability.
- The discovery of SWiSH through automated search is a novel approach that could potentially lead to the discovery of other effective components in neural networks.
- The paper includes a thorough evaluation of SWiSH, comparing it against other activation functions and demonstrating its superiority in some cases.

**Weaknesses:**
- The paper lacks a detailed discussion on the theoretical properties of SWiSH, such as its derivatives and their impact on gradient flow.
- The methodology used for discovering SWiSH is not sufficiently detailed, making it difficult to replicate or understand the search process.
- The paper primarily focuses on the ResNet architecture, limiting the generalizability of the findings to other architectures like Transformers.
- The paper does not provide sufficient evidence to support the claim that SWiSH is superior to other activation functions across all datasets and models.
- The paper could benefit from a more detailed discussion on the limitations of SWiSH and its potential drawbacks, such as its performance on certain datasets like ImageNet.
- The paper lacks a comparison with other recently proposed activation functions, which could have provided a more comprehensive evaluation of SWiSH.

**Questions:**
- Could the authors provide more details on the methodology used for discovering SWiSH, including the specific search algorithm and the criteria used for selecting candidate activation functions?
- How does the gradient flow through SWiSH compare to other activation functions, particularly in terms of its impact on optimization?
- Can the authors provide evidence or theoretical support for the claim that SWiSH is superior to other activation functions across all datasets and models?
- How does the performance of SWiSH compare to other activation functions on datasets like ImageNet, where it underperforms?
- Could the authors discuss the potential limitations of SWiSH and its generalizability to other architectures and datasets?
- How does the performance of SWiSH compare to other recently proposed activation functions, and what are the implications of these comparisons for the practical application of SWiSH?

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
- Reasons: The paper introduces a novel activation function, SWiSH, which shows promising results in various experiments. The methodology, while not entirely novel, is well-executed, and the paper is clearly written, making it accessible to a broad audience. The paper's contribution is significant in demonstrating the effectiveness of SWiSH across different datasets and models, although it could benefit from a more detailed discussion on the theoretical underpinnings and generalizability of the findings. The decision to accept is supported by the paper's originality in applying automated search techniques to discover a new activation function and its potential impact on the field. However, the paper should be revised to address the concerns regarding its novelty and the need for more comprehensive evaluations across different architectures and datasets.