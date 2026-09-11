 **Summary:**
The paper introduces HarnessDev, a novel benchmark aimed at evaluating the ability of large language models (LLMs) to construct and evolve their own agent harnesses. This benchmark consists of two stages: Creation and Evolution. In the Creation stage, LLMs develop a harness from scratch using a weak seed, and in the Evolution stage, they iteratively refine the harness based on feedback from downstream tasks. The benchmark covers six creator LLMs and four domains, providing a comprehensive evaluation of harness development. The paper also explores the performance of these harnesses against human-engineered references and discusses the efficiency and effectiveness of the generated harnesses. Despite some limitations in the scope and depth of evaluation, the paper offers valuable insights into the capabilities of LLMs in developing harnesses and their impact on task performance.

**Strengths:**
- The paper introduces a novel benchmark, HarnessDev, which evaluates the ability of large language models (LLMs) to construct and evolve their own agent harnesses, a significant and under-explored area in the field.
- The benchmark is well-designed, with a clear and detailed description of the evaluation setup, including the development environment, the evaluation protocol, and the metrics used.
- The paper provides a comprehensive evaluation of six creator LLMs across four domains, covering a wide range of scenarios and use cases.
- The results are thorough and well-presented, with detailed analysis and insights into the performance of the generated harnesses, their efficiency, and their effectiveness in improving task performance.
- The paper is well-written, with clear explanations of the methodology and results, making it accessible and understandable to a broad audience.

**Weaknesses:**
- The paper lacks a detailed discussion on the limitations of the benchmark, which could help in understanding the scope and applicability of the results.
- There is a lack of comparison with other benchmarks, which could help in understanding the relative strengths and weaknesses of HarnessDev.
- The paper does not provide a detailed analysis of the specific strategies used by the LLMs to develop the harnesses, which could provide valuable insights into the learning process.
- The paper does not include a discussion on the potential negative societal impacts of the work, which could be a significant concern for some readers.
- The evaluation is limited to a few domains, which might not fully represent the capabilities of the LLMs across a broader range of applications.
- The paper could benefit from a more detailed discussion on the transferability of the harnesses across different domains and the generalizability of the findings.

**Questions:**
- Can the authors provide more details on the specific strategies used by the LLMs to develop the harnesses, and how these strategies might vary across different domains or tasks?
- How do the results of HarnessDev compare to other benchmarks in terms of the effectiveness and efficiency of the generated harnesses?
- Could the authors discuss the potential negative societal impacts of the work, and how these might be mitigated or addressed?
- How transferable are the harnesses developed by the LLMs across different domains or applications?
- Could the authors provide more details on the development environment and the specific tools used to evaluate the harnesses, and how these might influence the results?
- How does the paper address the issue of overfitting in the harnesses, and what steps were taken to ensure that the results are not biased by the specific tools or environments used?

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
- Reasons: The paper introduces a novel benchmark, HarnessDev, which evaluates the ability of LLMs to construct and evolve their own agent harnesses, a significant and under-explored area in the field. The benchmark is well-designed, with a clear and detailed description of the evaluation setup, and the results are thorough and well-presented. The paper provides valuable insights into the capabilities of LLMs in developing harnesses and their impact on task performance. The decision to accept is based on the originality of the benchmark, the methodological soundness, and the significance of the results, as well as the clarity and logic of the presentation. The paper is a strong contribution to the field and should be highlighted at the conference.