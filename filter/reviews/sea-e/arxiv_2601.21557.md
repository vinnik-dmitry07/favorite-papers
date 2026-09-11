 **Summary:**
The paper introduces Meta Context Engineering (MCE), a novel framework for context engineering that employs a bi-level optimization approach to co-evolve context artifacts and skills. MCE utilizes a meta-level agent that iteratively refines skills, such as executable instructions and code, to optimize context, while a base-level agent executes these skills to learn from training rollouts and construct context. The framework is evaluated across five diverse domains, demonstrating significant improvements over existing methods in terms of context adaptability, efficiency, and transferability. MCE's methodology involves a bi-level optimization process where the meta-level agent refines skills, and the base-level agent executes these skills to learn from training rollouts and construct context. The paper also includes comprehensive evaluations across five domains, four LLMs, and both offline and online settings, showcasing MCE's effectiveness in various scenarios.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation and a well-defined problem formulation.
- The proposed method, Meta Context Engineering (MCE), is innovative and well-motivated, with a novel approach to context engineering that involves a bi-level optimization process.
- MCE is evaluated across five diverse domains, demonstrating significant improvements over existing methods in terms of context adaptability, efficiency, and transferability.
- The paper includes a comprehensive evaluation, covering both offline and online settings, and includes a detailed analysis of the evolved skills, which provides valuable insights into the capabilities of the meta-level agent.
- The methodology is clearly explained, and the paper includes a detailed description of the experiments, making it easy to reproduce the results.

**Weaknesses:**
- The paper lacks a detailed discussion on the limitations of the proposed method, which could help in understanding its applicability and potential drawbacks.
- The paper does not provide sufficient details on the implementation of the meta-level agent, which could limit the reproducibility of the results.
- There is a lack of comparison with other context engineering methods, which could provide a more comprehensive evaluation of the proposed method.
- The paper does not discuss the limitations of the proposed method, which could help in understanding its applicability and potential drawbacks.
- The paper does not provide sufficient details on the implementation of the meta-level agent, which could limit the reproducibility of the results.
- The paper lacks a detailed discussion on the limitations of the proposed method, which could help in understanding its applicability and potential drawbacks.
- The paper does not discuss the limitations of the proposed method, which could help in understanding its applicability and potential drawbacks.
- The paper does not discuss the limitations of the proposed method, which could help in understanding its applicability and potential drawbacks.

**Questions:**
- Can the authors provide more details on the implementation of the meta-level agent, including the specifics of how it is trained and how it generates new skills?
- How does the proposed method compare to other context engineering methods, particularly in terms of performance and efficiency?
- Could the authors provide more details on the limitations of the proposed method and discuss potential scenarios where it might not be the most effective approach?
- How does the proposed method handle the transfer of skills across different tasks or domains, and what are the implications of this transfer in terms of performance and generalization?
- Could the authors provide more details on the computational resources required to implement the proposed method, including the hardware and software requirements?
- How does the proposed method handle the transfer of skills across different tasks or domains, and what are the implications of this transfer in terms of performance and generalization?
- Could the authors provide more details on the computational resources required to implement the proposed method, including the hardware and software requirements?

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
- Reasons: The paper presents a novel and innovative approach to context engineering, utilizing a bi-level optimization process to co-evolve context artifacts and skills. The methodology is well-explained, and the results demonstrate significant improvements over existing methods in terms of context adaptability, efficiency, and transferability. The paper is well-written, clear, and easy to follow, with a clear motivation and a well-defined problem formulation. The comprehensive evaluations across five domains, four LLMs, and both offline and online settings provide strong evidence of the method's effectiveness. The paper also includes a detailed analysis of the evolved skills, which provides valuable insights into the capabilities of the meta-level agent. The decision to accept is based on the paper's originality, methodological soundness, significance of results, and clarity and logic of presentation.