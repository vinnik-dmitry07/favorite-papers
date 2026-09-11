 **Summary:**
The paper introduces Vending-Bench, a novel benchmark designed to evaluate the long-term coherence of autonomous agents, specifically focusing on the operation of a vending machine. The benchmark involves agents managing inventory, placing orders, setting prices, and handling daily fees, with the goal of assessing their ability to maintain consistent performance over extended periods. The paper presents a detailed analysis of various large language models (LLMs) and their performance in this environment, highlighting the challenges posed by long-term decision-making and the potential risks associated with AI capabilities. The benchmark is designed to test the agents' ability to manage resources and adapt to changing conditions, with a focus on the long-term coherence and reliability of AI systems.

**Strengths:**
- The paper introduces a novel benchmark, Vending-Bench, which is designed to test the long-term coherence of autonomous agents, specifically focusing on their ability to manage a vending machine over extended periods.
- The benchmark is well-motivated, providing a clear and well-structured presentation of the experiments, which are well-designed to evaluate the performance of large language models (LLMs) in long-term decision-making scenarios.
- The paper is well-written, making it easy to follow, and includes a detailed analysis of the performance of various LLMs, highlighting the challenges and potential risks associated with AI capabilities.
- The benchmark is significant as it addresses the critical issue of long-term coherence in AI systems, which is crucial for ensuring the reliability and safety of AI applications.

**Weaknesses:**
- The paper lacks a clear definition of the problem it aims to solve, which could be improved by providing a more detailed explanation of the specific challenges and risks associated with the long-term coherence of autonomous agents.
- The benchmark's scope is limited, focusing on a single, simplistic task (operating a vending machine), which may not adequately represent the complexity and diversity of real-world scenarios.
- The paper does not sufficiently address the generalizability of the findings, as the results may not be applicable to other types of tasks or environments.
- There is a lack of discussion on the limitations of the work, including the potential for overfitting and the generalizability of the results to other types of tasks or environments.
- The paper does not provide sufficient details on how the benchmark was designed, including the selection of parameters and the rationale behind the design choices, which could affect the reproducibility and applicability of the results.

**Questions:**
- Could you clarify the specific challenges and risks associated with the long-term coherence of autonomous agents that the benchmark aims to address?
- How does the benchmark ensure that the results are not influenced by overfitting, especially given the simplistic nature of the tasks?
- Can you provide more details on how the benchmark was designed, including the selection of parameters and the rationale behind the design choices?
- How does the benchmark ensure that the results are generalizable to other types of tasks or environments, and what steps were taken to validate the benchmark's effectiveness in real-world scenarios?
- Could you discuss the potential impact of the benchmark on the development of AI systems, particularly in terms of improving their long-term coherence and reliability?

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
- Reasons: The paper introduces a novel benchmark, Vending-Bench, which effectively tests the long-term coherence of autonomous agents in a controlled environment. The benchmark is well-designed and provides valuable insights into the capabilities and limitations of LLMs in long-term decision-making scenarios. The paper is well-written, making it accessible and easy to follow, and the results are well-presented, highlighting the challenges and potential risks associated with AI capabilities. The decision to accept is based on the originality of the benchmark, methodological soundness, and the significance of the results, despite some concerns regarding the generalizability of the findings and the need for a broader scope in future work. The paper is recommended for acceptance as a poster to facilitate further discussion and exploration of the benchmark's implications and potential applications.