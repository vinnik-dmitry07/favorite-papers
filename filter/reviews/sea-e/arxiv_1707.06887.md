 **Summary:**
The paper introduces a novel distributional perspective in reinforcement learning (RL) by focusing on the distribution of returns rather than the expected value. It presents a distributional Bellman operator that models the distribution of returns, demonstrating its theoretical properties and practical applications using a new algorithm, Categorical DQN. This algorithm, which models the distribution of returns using a categorical distribution, shows improved performance on Atari games compared to traditional methods like DQN. The paper also discusses the theoretical underpinnings of the distributional approach, including its stability and convergence properties. Despite the theoretical insights and empirical results, the paper has been critiqued for its clarity in explaining the practical benefits and the necessity of the distributional approach over traditional methods.

**Strengths:**
- The paper introduces a novel distributional perspective in reinforcement learning, which is a significant departure from the traditional approach of modeling expected values.
- The theoretical analysis provided is robust, with a clear exposition of the distributional Bellman operator and its properties.
- The empirical results are compelling, showing that the proposed algorithm, Categorical DQN, outperforms existing methods like DQN, Double DQN, and Dueling DQN.
- The paper is well-written, with clear explanations of the theoretical results and empirical findings, making it accessible to readers.
- The distributional approach offers a new way of modeling uncertainty in reinforcement learning, which is a significant contribution to the field.

**Weaknesses:**
- The paper lacks a clear explanation of the practical benefits of modeling the distribution of returns over the expected value, which could limit the understanding of the proposed method's utility.
- The empirical results, while promising, do not convincingly demonstrate the superiority of the distributional approach over traditional methods in all scenarios.
- The paper could benefit from a more rigorous comparison with existing distributional RL methods, such as those using the Wasserstein metric, to establish the superiority of the proposed method.
- The theoretical analysis, particularly the discussion on the contraction property of the distributional Bellman operator, is not sufficiently clear or novel, which could undermine the paper's contribution.
- The paper's presentation could be improved to better highlight the novelty and significance of the results, particularly in the abstract and introduction sections.

**Questions:**
- Could the authors clarify the practical benefits of modeling the distribution of returns over the expected value, especially in terms of algorithmic design and performance?
- How does the proposed method compare to other distributional RL methods, particularly those using the Wasserstein metric?
- In the empirical results, why does the performance of C51 sometimes lag behind that of DQN, and what are the implications of this observation?
- Can the authors provide a more detailed explanation of the theoretical results, particularly the contraction property of the distributional Bellman operator, to make the paper more accessible to readers?
- How does the proposed method handle the issue of instability in the control setting, as discussed in Section 3.4?
- Could the authors elaborate on the choice of the Wasserstein metric over other metrics like the KL divergence, and how this choice impacts the theoretical analysis?

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
- Reasons: The paper presents a novel approach to reinforcement learning by focusing on the distribution of returns rather than the expected value. The theoretical analysis and empirical results support the effectiveness of this approach, showing that the proposed algorithm, Categorical DQN, outperforms traditional methods in certain scenarios. While the paper has been critiqued for its clarity in explaining the practical benefits and the necessity of the distributional approach, the overall contribution is seen as significant and the methodological soundness is high. The decision to accept is based on the originality of the approach, the methodological soundness, and the significance of the results, despite some concerns about the clarity and depth of the presentation.