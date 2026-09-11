 **Summary:**
The paper introduces a novel reinforcement learning framework for financial portfolio management, utilizing a deterministic policy gradient method. It employs an ensemble of identical independent evaluators (EIIE) to manage a portfolio of assets, with a focus on transaction costs and a reward function based on logarithmic returns. The framework is tested using historical data from the Poloniex cryptocurrency exchange, demonstrating superior performance over traditional methods. The paper also discusses the challenges of backtesting in a simulated environment and the potential for overfitting. Despite its innovative approach, the paper is criticized for its lack of clarity in presentation and the absence of a comprehensive discussion on the limitations and potential negative societal impacts of the proposed method.

**Strengths:**
- The paper introduces a novel approach to portfolio management using reinforcement learning, which is a significant advancement in the field.
- The methodology is well-explained, with clear and detailed explanations of the approach, including the use of a deterministic policy gradient method and a reward function based on logarithmic returns.
- The paper is well-written, with a clear structure and detailed explanations that make it accessible to readers.
- The experimental results are strong, demonstrating the effectiveness of the proposed method in managing a portfolio of assets.
- The paper addresses the challenges of transaction costs and the impact of these costs on the portfolio's performance, which is a significant contribution to the field.

**Weaknesses:**
- The paper lacks clarity in some sections, particularly in the mathematical formulations and the definitions used, which could confuse readers.
- There is a lack of discussion on the limitations and potential negative societal impacts of the proposed method, which is a significant omission.
- The paper does not adequately address the issue of overfitting, which is a critical concern in backtesting in a simulated environment.
- The paper does not provide sufficient detail on the experimental setup, such as the specifics of the training data and the hyperparameters used, which could affect the reproducibility of the results.
- The paper's reliance on historical data and its assumptions about the market's behavior could limit the generalizability of the findings.
- The paper could benefit from a more comprehensive discussion on the related work and the specific contributions of the proposed method compared to existing approaches.

**Questions:**
- Could the authors clarify the definitions and mathematical formulations used in the paper, particularly in sections where the notation is confusing?
- How does the proposed method address the issue of overfitting, given the limitations of backtesting in a simulated environment?
- What specific data was used for training, and how were the hyperparameters chosen?
- Could the authors provide more details on the experimental setup, including the size and composition of the training set, the number of assets considered, and the frequency of trading?
- How does the proposed method compare to existing approaches in terms of performance and computational efficiency?
- What are the potential negative societal impacts of the proposed method, and how do the authors address these concerns?
- Could the authors provide a more detailed discussion on the limitations of the proposed method and the assumptions made in the analysis?

**Soundness:**
3 good

**Presentation:**
2 fair

**Contribution:**
3 good

**Rating:**
5 marginally below the acceptance threshold

**Paper Decision:**
- Decision: Reject
- Reasons: The paper, while innovative in its approach to portfolio management using reinforcement learning, suffers from significant issues in clarity and presentation. The mathematical formulations and definitions used are not clearly explained, which could confuse readers. The paper also lacks a comprehensive discussion on the limitations and potential negative societal impacts of the proposed method. Additionally, the experimental setup and the discussion on related work are inadequate. These issues, combined with the concerns about the generalizability of the findings due to the reliance on historical data, lead to the decision to reject the paper. The decision aligns with the metareview, which highlights the need for a more rigorous evaluation and clearer presentation to meet the conference standards.