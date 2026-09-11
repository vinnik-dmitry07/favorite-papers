 **Summary:**
The paper investigates the effectiveness of spurious rewards in reinforcement learning with verifiable rewards (RLVR) for improving the reasoning capabilities of large language models (LLMs). The authors demonstrate that even with random or incorrect rewards, LLMs can exhibit enhanced reasoning performance, particularly in mathematical reasoning tasks. This phenomenon is attributed to the clipping bias in the GRPO algorithm, which amplifies pre-existing behaviors learned during pre-training. The paper also explores how different models respond to these spurious rewards, highlighting the variability in their effectiveness across different model families. The findings suggest that the base model's pre-training significantly influences the outcomes of RLVR, and the effects observed in one model family may not generalize to others.

**Strengths:**
- The paper is well-written, clear, and easy to follow, making complex concepts accessible to a broad audience.
- The authors provide a comprehensive analysis of the impact of spurious rewards on the performance of LLMs, which is a significant and timely topic in the field.
- The paper is original in its approach, offering a novel perspective on the role of spurious rewards in RLVR, which is a relatively new and under-explored area.
- The experiments are well-designed, and the results are well-presented, supporting the claims with detailed analysis and visualizations.
- The paper is well-positioned within the existing literature, providing a thorough review of related work and effectively contextualizing its contributions.

**Weaknesses:**
- The paper's findings may not be generalizable to other types of reasoning tasks beyond mathematical reasoning, which limits the scope of the study.
- The paper lacks a detailed discussion on the limitations and potential negative societal impacts of the proposed methods, which could be crucial for understanding the broader implications of the research.
- The paper could benefit from more detailed explanations and examples of the spurious rewards used in the experiments, particularly how these rewards are generated and their impact on model performance.
- The paper could be improved by including more diverse models in the experiments to better understand the generalizability of the findings across different model architectures and training methodologies.
- The paper's conclusions are somewhat limited by the scope of the study, and the generalizability of the findings to other types of reasoning tasks or different model families is not thoroughly explored.

**Questions:**
- Could the authors clarify the specifics of the spurious rewards used in the experiments, such as how they are generated and what impact they have on model performance?
- How do the authors address the potential negative societal impacts of their findings, particularly in the context of deploying RLVR methods in real-world applications?
- Given the findings on the effectiveness of spurious rewards, how might these insights be applied to improve the training of LLMs in practical scenarios?
- Could the authors elaborate on the potential reasons why spurious rewards are more effective for some model families but not others?
- How do the authors envision the application of their findings in the broader context of RLVR research, particularly in terms of developing more robust and effective RLVR methods?

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
- Reasons: The paper presents a compelling case for the effectiveness of spurious rewards in RLVR, providing valuable insights into the dynamics of model training and the role of pre-existing behaviors. The findings are well-supported by experimental evidence and offer a fresh perspective on the use of spurious rewards, which is a significant contribution to the field. Despite some concerns about the generalizability of the findings and the need for more diverse model testing, the paper is well-written, clearly presented, and offers a solid technical foundation for further research. The decision to accept is supported by the paper's originality, methodological soundness, and the significance of its results, which are expected to stimulate further discussion and research in the area of RLVR.