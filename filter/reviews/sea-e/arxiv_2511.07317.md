 **Summary:**
The paper introduces RLVE, a novel approach to scaling up reinforcement learning for language models (LMs) using adaptive verifiable environments. RLVE dynamically adjusts the difficulty of the environment based on the model's performance, ensuring that the learning signals remain strong throughout the training process. The authors have developed RLVE-Gym, a large-scale suite of 400 verifiable environments, which are used to train models on a variety of reasoning benchmarks. The approach is evaluated against existing methods and shows significant improvements in generalizable reasoning capabilities. The paper also discusses the challenges of scaling up RL training for LMs and proposes a method to address these challenges by adapting the difficulty of the environment to the model's capabilities.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation and a logical structure that makes it accessible to readers.
- The proposed method of using adaptive verifiable environments to scale up RL training for LMs is innovative and addresses the challenge of static data distributions in RL training.
- The experiments are well-designed, with a focus on evaluating the method's effectiveness in improving generalizable reasoning capabilities, and the results are convincing.
- The paper introduces a novel approach to scaling up RL training by dynamically adjusting the difficulty of the environment, which is a significant advancement over traditional methods.
- The methodology is supported by a large-scale suite of 400 verifiable environments, which are carefully designed and provide algorithmically verifiable rewards, enhancing the reliability and effectiveness of the training.

**Weaknesses:**
- The paper lacks a discussion on the limitations of the proposed method, particularly in terms of its applicability to non-verifiable environments and its scalability to larger models.
- The evaluation of the method is limited to a small set of environments, which may not fully demonstrate its effectiveness across a broader range of tasks.
- The paper does not adequately address the computational costs associated with the method, which could be a significant barrier for practical implementation.
- The method's reliance on manual environment engineering raises concerns about its scalability and the feasibility of extending it to a broader range of tasks.
- The paper does not sufficiently discuss the potential negative societal impacts of the proposed method, which could be significant given the potential applications in areas like autonomous systems and AI safety.

**Questions:**
- How does the proposed method compare to other methods that use non-verifiable environments, particularly in terms of effectiveness and scalability?
- Can the method be adapted to work with larger models, and what are the potential challenges or limitations in doing so?
- How does the method handle the trade-off between computational cost and performance improvement, particularly in scenarios where the computational cost is high?
- Is there a way to automate the environment engineering process to make it more scalable and applicable to a broader range of tasks?
- How does the method ensure that the generated problems are not biased or unfair, especially in scenarios where the model's performance might influence the difficulty of the problems?
- Can the method be adapted to work with other types of RL algorithms, or is it specifically designed for the DAPO algorithm?

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
- Reasons: The paper introduces a novel approach to scaling up RL training for LMs using adaptive verifiable environments, which addresses the challenge of static data distributions in RL training. The method is well-received for its innovative approach and the large-scale suite of 400 verifiable environments, which are carefully designed to provide algorithmically verifiable rewards. The experiments conducted demonstrate the effectiveness of the method in improving generalizable reasoning capabilities. The paper is well-written, clear, and easy to follow, making it accessible to readers. The method's contribution to the field is significant, and the potential impact on the development of RL systems for LMs is substantial. The decision to accept is based on the paper's originality, methodological soundness, significance of results, and clarity and logic of presentation.