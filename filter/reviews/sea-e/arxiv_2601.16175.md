 **Summary:**
The paper introduces TTT-Discover, a novel approach to test-time training that leverages reinforcement learning to optimize a single solution for a given problem, rather than focusing on generalization across a set of problems. This method, applied to various domains including mathematics, GPU kernel engineering, algorithm design, and biology, demonstrates significant improvements over existing state-of-the-art methods. TTT-Discover utilizes a novel objective function and a PUCT-inspired reuse routine to enhance the learning process, showing superior performance in several benchmarks. The paper also discusses the challenges and limitations of the approach, including the need for further exploration and comparison with other methods.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation and a well-structured presentation that effectively communicates the main ideas and contributions.
- The proposed method, TTT-Discover, is novel and innovative, particularly in its application of reinforcement learning to optimize a single solution at test time, which is a significant departure from traditional methods.
- The paper demonstrates significant improvements in performance across various domains, including mathematics, GPU kernel engineering, algorithm design, and biology, showing that the method is effective in real-world applications.
- The methodology is well-explained, with a clear description of the problem, the approach, and the results, which is supported by thorough evaluations and comparisons to existing methods.
- The paper provides a comprehensive evaluation, including a detailed analysis of the method's performance and a comparison with existing methods, which helps in understanding the method's strengths and limitations.

**Weaknesses:**
- The paper lacks a detailed discussion on the limitations of the proposed method, which could have provided a more balanced view of its capabilities and challenges.
- There is a lack of comparison with other methods, particularly those that use similar approaches, which could have helped in understanding the method's relative performance and advantages.
- The paper does not provide sufficient details on the computational resources required for the experiments, which could be crucial for reproducibility and scalability assessments.
- The paper could benefit from a more thorough discussion on the generalizability of the method across different domains and the potential impact of domain-specific factors on its performance.
- There is a need for more detailed explanations and justifications for the choices made in the methodology, particularly in the design of the objective function and the reuse routine.

**Questions:**
- Could you provide more details on the computational resources required for the experiments, including the hardware used and the time taken for each experiment?
- How does the method perform when applied to problems with sparse or binary rewards, or in non-verifiable domains?
- Can you elaborate on the choice of the objective function and the reuse routine, and how these choices affect the performance and generalizability of the method?
- How does the method compare to other methods that use similar approaches, particularly in terms of performance and computational efficiency?
- Could you provide more details on the experimental setup, including the specifics of the hardware and software used, and the conditions under which the experiments were conducted?
- How does the method handle the trade-off between exploration and exploitation, especially in scenarios where the model might be overly focused on known solutions?

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
- Reasons: The paper presents a novel approach to test-time training that shows significant improvements over existing methods across various domains. The methodology is well-explained, and the results are convincing, supported by thorough evaluations and comparisons. The paper is well-written, making it accessible and easy to follow. The reviewers highlighted the novelty of the approach and the effectiveness of the method in achieving state-of-the-art results. Despite some concerns regarding the generalizability and the need for more comparisons with other methods, the paper's contributions are substantial and warrant acceptance, particularly in a poster format to allow for further discussion and exploration of the method's potential.