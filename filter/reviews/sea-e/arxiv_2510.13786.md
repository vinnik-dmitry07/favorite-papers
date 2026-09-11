 **Summary:**
The paper presents a comprehensive empirical study on the scaling behavior of reinforcement learning (RL) training for large language models (LLMs), focusing on the design choices that affect the performance and compute efficiency. The authors propose a sigmoidal compute-performance curve to predict the scaling of RL training and introduce a best-practice recipe, ScaleRL, which integrates existing methods to achieve predictable scaling. The study covers a wide range of design choices, including loss aggregation, normalization, curriculum, and off-policy algorithms, and demonstrates the effectiveness of ScaleRL through a large-scale experiment involving 100,000 GPU-hours. The paper also discusses the implications of these findings for the broader RL community and provides a framework for predicting scaling in RL.

**Strengths:**
- The paper provides a comprehensive empirical study on the scaling behavior of reinforcement learning (RL) training for large language models (LLMs), which is crucial for understanding the scaling laws in RL.
- The authors propose a sigmoidal compute-performance curve to predict the scaling of RL training, which is a significant contribution to the field.
- The study covers a wide range of design choices and their effects on the asymptotic performance and compute efficiency, which is beneficial for the RL community.
- The paper is well-written, clear, and easy to follow, making it accessible to a broad audience.
- The proposed ScaleRL recipe is shown to be effective in scaling and predicting validation performance on a single RL run scaled up to 100,000 GPU-hours, demonstrating its practical utility.
- The paper provides a scientific framework for analyzing scaling in RL, which is a significant contribution to the field.

**Weaknesses:**
- The paper lacks a clear explanation of the sigmoidal compute-performance curve and its advantages over other curves, such as power law, which could limit the understanding and applicability of the findings.
- The paper does not sufficiently discuss the limitations of the proposed framework, which could affect the generalizability and applicability of the findings.
- The paper does not provide a detailed discussion on how the findings can be applied to other domains or tasks beyond the current study, which could limit the impact of the research.
- The paper does not include a discussion on the limitations of the proposed framework, which could affect the reliability and applicability of the findings.
- The paper does not provide a detailed discussion on the limitations of the proposed framework, which could affect the reliability and applicability of the findings.
- The paper does not discuss the limitations of the proposed framework, which could affect the reliability and applicability of the findings.

**Questions:**
- Could you provide a detailed explanation of the sigmoidal compute-performance curve and its advantages over other curves, such as power law?
- How can the findings of this study be applied to other domains or tasks beyond the current study?
- What are the limitations of the proposed framework, and how do these limitations affect the reliability and applicability of the findings?
- How does the proposed framework handle the limitations of the RL training process, such as the sensitivity to hyperparameters and the computational demands?
- Can you discuss the potential societal impacts of the proposed framework, particularly in terms of computational resource requirements and the scalability of RL training for LLMs?
- How does the proposed framework compare to other existing methods in terms of computational efficiency and scalability?
- Could you provide more details on the computational resources and infrastructure used in the experiments, including the hardware specifications and the software configurations?
- How does the proposed framework handle the limitations of the RL training process, such as the sensitivity to hyperparameters and the computational demands?

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
- Reasons: The paper presents a significant empirical study on the scaling behavior of RL training for LLMs, which is crucial for understanding the scaling laws in RL. The proposed sigmoidal compute-performance curve provides a novel approach to predicting the scaling of RL training, and the ScaleRL recipe offers a practical solution for achieving predictable scaling. The paper is well-written, clear, and easy to follow, making it accessible to a broad audience. The findings are relevant and have the potential to impact the RL community by providing a framework for predicting scaling in RL. The reviewers have highlighted the paper's contribution to the field and its potential impact, and the decision to accept is based on these factors. However, the paper could benefit from a more detailed discussion on the limitations of the proposed framework and its generalizability to other domains or tasks.