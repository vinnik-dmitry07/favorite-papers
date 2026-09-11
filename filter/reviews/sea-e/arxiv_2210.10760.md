 **Summary:**
The paper investigates the phenomenon of overoptimization in reinforcement learning (RL) and best-of-n (BoN) sampling, focusing on the use of proxy reward models trained on human feedback. It explores the relationship between the KL divergence between the initial and optimized policies and the gold reward model score, using a synthetic setup to study the effects of various factors such as the size of the reward model dataset, the number of reward model and policy parameters, and the coefficient of the KL penalty. The authors find that the gold reward model score changes differently depending on the optimization method and that the coefficients of the functional forms for the gold reward model score scale smoothly with the number of reward model parameters. The paper also discusses the implications of these findings for theoretical considerations in AI alignment.

**Strengths:**
- The paper is well-written, with clear and detailed explanations, making it easy to follow.
- The authors conduct a comprehensive set of experiments, which are well-documented, and the results are well-presented, making the paper a valuable resource for understanding overoptimization in RL.
- The paper addresses an important and timely problem, focusing on the overoptimization of reward models, which is a significant issue in AI alignment.
- The experiments are well-designed, and the results are clearly presented, contributing to a better understanding of the relationship between the gold reward model score and the KL divergence between the initial and optimized policies.
- The paper provides a novel approach to studying overoptimization by using a synthetic setup, which allows for a more controlled and systematic analysis of the phenomenon.

**Weaknesses:**
- The paper could benefit from more detailed explanations of the experimental setup, particularly the synthetic setup and the choice of parameters such as the number of synthetic comparisons and the size of the reward model.
- The paper lacks a clear definition and discussion of the gold standard reward model, which is crucial for understanding the experimental results.
- The paper does not sufficiently discuss the limitations of the synthetic setup, which might not fully capture the complexities of real-world scenarios.
- There is a lack of discussion on the choice of KL divergence as a metric for measuring overoptimization, and the paper could benefit from a more thorough analysis of the functional forms for the gold reward model score.
- The paper's claims about the generalizability of the results to real-world scenarios are not convincingly supported, and the paper could benefit from more empirical evidence or theoretical analysis to strengthen these claims.

**Questions:**
- How do the authors justify the choice of KL divergence as a metric for measuring overoptimization, and what are the implications of using other metrics like MSE or MAE?
- Could the authors provide more details on the synthetic setup, particularly the choice of parameters and the rationale behind the experimental design?
- How do the authors address the potential limitations of the synthetic setup, and what steps have been taken to ensure that the results generalize to real-world scenarios?
- What are the implications of the functional forms for the gold reward model score, and how do these forms help in understanding the behavior of the reward model?
- Could the authors clarify the role and definition of the gold standard reward model, and discuss how it influences the experimental results?
- How do the authors address the potential for overoptimization in real-world scenarios, and what steps can be taken to mitigate this issue in practical applications of RL from human feedback?

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
- Reasons: The paper presents a well-structured and comprehensive study on the overoptimization of reward models in RL, using a synthetic setup to explore the relationship between the gold reward model score and the KL divergence between the initial and optimized policies. The experimental results are thorough and well-documented, providing valuable insights into the behavior of reward models under different optimization conditions. The paper is also commended for its clarity and the depth of its analysis, which contributes to a better understanding of the phenomenon of overoptimization in RL. Despite some concerns regarding the generalizability of the results to real-world scenarios, the paper is seen as a significant contribution to the field and is recommended for acceptance, particularly in a poster format to facilitate further discussion and exploration of the findings.