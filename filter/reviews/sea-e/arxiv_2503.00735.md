 **Summary:**
The paper introduces LADDER, a novel framework that enables large language models (LLMs) to autonomously improve their problem-solving capabilities through recursive problem decomposition and reinforcement learning. LADDER generates and solves progressively simpler variants of complex problems, leveraging a model's own capabilities to create a natural difficulty gradient. This approach is demonstrated to improve the performance of LLMs on mathematical integration tasks, achieving significant improvements over existing methods. The paper also introduces TTRL, a test-time reinforcement learning method that further enhances performance by generating problem variants during inference and applying reinforcement learning to refine the model's solutions. The framework is evaluated on the MIT Integration Bee, demonstrating its effectiveness in handling complex mathematical problems.

**Strengths:**
- The paper is well-written, making it easy to follow and understand the proposed methodology.
- The approach of using a model to generate its own training data is innovative and shows promise in enhancing the capabilities of large language models (LLMs).
- The paper demonstrates significant improvements in mathematical reasoning tasks, particularly in the domain of mathematical integration, where the Llama 3.2 3B model's accuracy increases from 1% to 82% on undergraduate-level integration problems.
- The methodology is novel and interesting, with a focus on self-improvement through recursive problem decomposition and reinforcement learning, which is a significant advancement in the field.
- The paper is well-structured, with clear explanations of the methodology and its components, and includes a comprehensive discussion of related work.
- The experimental results show a clear improvement in performance, demonstrating the effectiveness of the proposed method.

**Weaknesses:**
- The paper lacks a detailed discussion on the limitations of the proposed method, which is crucial for understanding its applicability and potential drawbacks.
- The evaluation is limited to a single problem type, which might not fully demonstrate the generalizability of the proposed method.
- The paper does not discuss the limitations of the verification method used, which could affect the reliability of the results.
- There is a lack of clarity in the presentation of the experimental setup, particularly in the description of the training and test sets, which could affect the reproducibility of the results.
- The paper does not compare the proposed method with other state-of-the-art methods, which could help in understanding its relative effectiveness.
- The method's reliance on the model's ability to generate valid variants of problems might limit its applicability to domains where such generation is difficult or impossible.
- The paper does not discuss the computational cost of the proposed method, which could be a significant concern for practical applications.

**Questions:**
- Could you provide more details on the limitations of the proposed method and how they might affect its applicability in different domains?
- How does the proposed method compare with other state-of-the-art methods in terms of performance and efficiency?
- Could you clarify the experimental setup, particularly the training and test sets, to ensure reproducibility of the results?
- How does the proposed method handle the verification of solutions, especially in cases where the verification method might not be 100% accurate?
- Can you discuss the potential impact of the proposed method on the development of AI systems, particularly in terms of its scalability and applicability to other domains?
- How does the proposed method handle the generation of variants that are not valid or are too difficult for the model to solve, and what strategies are used to ensure the quality of the generated variants?
- Could you provide more details on the computational cost of the proposed method and how it scales with the size and complexity of the problems being solved?

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
- Reasons: The paper presents a novel and innovative approach to improving the problem-solving capabilities of LLMs through recursive problem decomposition and reinforcement learning. The methodology is well-articulated, and the experimental results demonstrate significant improvements in mathematical reasoning tasks. The paper also introduces TTRL, a test-time reinforcement learning method that further enhances performance by generating problem variants during inference and applying reinforcement learning to refine the model's solutions. Despite some limitations, such as the lack of a broader evaluation and discussion on the limitations of the verification method, the paper's contributions are substantial and warrant acceptance, particularly as a poster presentation. The decision aligns with the reviewers' consensus and the metareview, which highlights the paper's originality, methodological soundness, and the significance of its results.