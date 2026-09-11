 **Summary:**
The paper introduces a novel approach to harness engineering for coding agents, focusing on the observability of harness components and their interactions with the environment. The proposed method, termed Agentic Harness Engineering (AHE), utilizes a closed-loop system that includes a decoupled harness substrate, an agent debugger, and an evolve agent, to optimize the harness components for coding agents. This approach aims to improve the performance of coding agents by enhancing the observability of harness components, which is crucial for understanding and addressing the complex interactions between the agents and their environments. The paper presents empirical results demonstrating the effectiveness of AHE in improving the performance of coding agents on benchmarks like Terminal-Bench 2 and SWE-bench-verified.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation and a well-structured presentation of the methodology.
- The proposed method, AHE, is novel and innovative, providing a new approach to harness engineering for coding agents that is observability-driven.
- The paper includes comprehensive experiments that demonstrate the effectiveness of AHE in improving the performance of coding agents, as evidenced by the results presented.
- The methodology is well-explained, making it easy to understand and replicate, and the paper provides a detailed analysis of the results, including ablation studies that help in understanding the contributions of different components of the system.
- The paper is significant in its contribution to the field of harness engineering, which is crucial for the development and deployment of coding agents.

**Weaknesses:**
- The paper lacks a detailed discussion on the limitations of the proposed method, which could help in understanding the scope and applicability of the findings.
- There is a lack of clarity on the specifics of how the evolve agent operates, particularly in terms of its decision-making process and the criteria used for adding, modifying, or removing components.
- The paper could benefit from a more detailed discussion on the design choices made in the implementation of AHE, including the choice of GPT-5.4 as the base model and the rationale behind the design of the evolve agent.
- The paper does not sufficiently address the scalability of the proposed method, especially in terms of its applicability to larger, more complex systems or different types of coding agents.
- The paper could benefit from a more detailed discussion on the potential negative societal impacts of the proposed method, particularly in terms of its potential to automate jobs traditionally performed by human coders.

**Questions:**
- Could you provide more details on the specifics of how the evolve agent operates, including the decision-making process and the criteria used for adding, modifying, or removing components?
- How does the proposed method compare to other existing methods for harness engineering, particularly in terms of its effectiveness and efficiency?
- What are the specific design choices made in the implementation of AHE, and what were the considerations behind these choices?
- How does the proposed method handle the scalability issues that might arise when applied to larger, more complex systems or different types of coding agents?
- Could you provide more details on the potential negative societal impacts of the proposed method, particularly in terms of its potential to automate jobs traditionally performed by human coders?
- How does the proposed method ensure the reliability and robustness of the evolved harnesses, especially in terms of their ability to handle unexpected or unforeseen scenarios?

**Soundness:**
3 good

**Presentation:**
3 good

**Contribution:**
3 good

**Rating:**
7 accept, but needs minor improvements

**Paper Decision:**
- Decision: Accept
- Reasons: The paper presents a novel approach to harness engineering for coding agents, focusing on observability and automation. The methodology is well-explained, and the empirical results demonstrate the effectiveness of the proposed method. The paper is well-written and easy to follow, making it accessible to a broad audience. The reviewers have highlighted some concerns regarding the scalability and applicability of the method, but these are not significant enough to warrant rejection. The paper is technically solid, with a moderate-to-high impact, and is recommended for acceptance, particularly as a poster presentation.