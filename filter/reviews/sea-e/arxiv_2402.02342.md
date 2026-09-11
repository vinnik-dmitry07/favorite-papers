 **Summary:**
The paper introduces MetaOptimize, a novel framework designed to optimize meta-parameters, specifically learning rates, during training. The methodology involves a discounted sum of future losses to minimize the regret of step sizes, which is updated dynamically using a backward-view update. MetaOptimize can be integrated with various first-order optimization algorithms and can handle block-wise adjustments of learning rates. The paper provides theoretical insights and empirical evidence demonstrating the effectiveness of MetaOptimize across diverse machine learning tasks, showing improvements over existing methods. However, it also acknowledges the limitations and potential improvements, such as the need for further exploration of Hessian-based methods and the generalization of the approach to discrete meta-parameters.

**Strengths:**
- The paper introduces a novel framework, MetaOptimize, which optimizes meta-parameters, particularly learning rates, during training, offering a dynamic approach that adjusts step sizes on the fly to minimize a specific form of regret that considers the long-term impact of step sizes on training.
- The framework is general and can wrap around any first-order optimization algorithm, making it versatile and applicable to a wide range of machine learning tasks.
- The paper provides a comprehensive theoretical analysis of the proposed method, including detailed derivations and proofs, which enhance the credibility and depth of the research.
- The empirical results demonstrate the effectiveness of the proposed method, showing improvements over existing methods in various machine learning tasks.
- The paper is well-written, making it easy to follow, and includes a detailed discussion on the limitations and future works, which shows a thoughtful consideration of the broader implications and potential improvements.

**Weaknesses:**
- The paper lacks a clear comparison with other state-of-the-art methods, which could help in understanding the relative performance and advantages of the proposed method.
- The paper does not discuss the computational complexity of the proposed algorithm, which is crucial for understanding its practical applicability and efficiency.
- The experimental results are not convincingly superior to existing methods, particularly in scenarios where the proposed method underperforms significantly, such as in the ImageNet dataset.
- The paper does not adequately address the scalability of the proposed method, especially in large-scale or complex datasets, which could limit its practical application.
- There is a lack of discussion on the limitations of the proposed method, which could help in understanding its applicability and potential drawbacks.
- The paper does not provide sufficient details on the experimental setup, such as the specifics of the datasets used and the hyperparameters tuned for the baseline methods, which could affect the reproducibility and generalizability of the results.

**Questions:**
- Could you clarify the computational complexity of the proposed algorithm?
- How does the proposed method compare with other state-of-the-art methods in terms of performance and efficiency?
- Can you provide more details on the experimental setup, particularly the specifics of the datasets used and the hyperparameters tuned for the baseline methods?
- How does the proposed method handle the scalability issues, especially in large-scale or complex datasets?
- Can the proposed method be applied to discrete meta-parameters, such as batch size or network layer count?
- What are the potential applications of the proposed method beyond continual learning?
- How does the proposed method perform in scenarios where the discount factor γ is set to 1, and what are the implications of this setting?

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
- Reasons: The paper presents a novel approach to optimizing meta-parameters during training, which is both theoretically sound and empirically validated. The methodology, while complex, is well-explained, and the experimental results demonstrate its effectiveness in diverse machine learning tasks. The paper also acknowledges its limitations and discusses potential improvements, which shows a commitment to ongoing research. Despite some concerns regarding the computational complexity and scalability, the paper's contributions to the field of meta-parameter optimization are significant and warrant acceptance, especially considering the potential for further development and application in various machine learning scenarios.