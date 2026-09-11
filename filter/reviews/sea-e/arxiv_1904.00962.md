 **Summary:**
The paper introduces a novel optimization algorithm, LAMB, which builds upon existing methods like LARS and Adam to enhance the training of large-scale deep neural networks, particularly in large batch settings. The algorithm employs layer-wise adaptive learning rates and normalization techniques to manage the size of the gradient updates, thereby improving the convergence and performance of models like BERT and ResNet-50. Theoretical analysis and empirical results demonstrate the algorithm's effectiveness in reducing training times significantly, although the paper's novelty and the scope of its theoretical contributions are questioned.

**Strengths:**
- The paper is well-written, clear, and easy to follow, making it accessible to a broad audience.
- The proposed method is simple, effective, and easy to implement, with minimal hyperparameter tuning required.
- The paper provides a comprehensive empirical evaluation, demonstrating the method's effectiveness across various tasks and datasets.
- Theoretical analysis is provided, which supports the proposed method's convergence to a stationary point in nonconvex settings.
- The paper addresses a significant and relevant problem in training large-scale deep neural networks, which is of high interest to the community.
- The method's simplicity and ease of implementation make it a valuable contribution to the field.

**Weaknesses:**
- The paper lacks a detailed comparison with other large batch optimization methods, which could have provided a clearer understanding of the method's advantages.
- The theoretical analysis is limited, and the convergence rate analysis is not thoroughly discussed, which could affect the understanding of the method's effectiveness.
- The novelty of the proposed method is questioned, as it appears to be a combination of existing methods like LARS and Adam, with limited new theoretical insights.
- The paper does not adequately address the scalability of the method beyond the specific settings tested, which could limit its applicability in more diverse scenarios.
- There is a lack of discussion on the limitations of the proposed method, which is crucial for understanding its scope and applicability.
- The paper could benefit from more detailed experimental results, including the impact of different hyperparameters and the convergence behavior of the method under varying conditions.

**Questions:**
- Can the authors provide a detailed comparison with other large batch optimization methods, including the hyperparameter settings used in these comparisons?
- How does the proposed method compare in terms of convergence rate and theoretical insights with other existing methods like LARS and Adam?
- Could the authors elaborate on the scalability of the method beyond the specific settings tested and discuss any potential limitations or challenges in applying the method to other scenarios?
- What are the specific advantages of the proposed method over existing methods like LARS, particularly in terms of convergence behavior and practical performance?
- How does the method handle the scalability of the learning rate across different layers, and what are the implications of this approach?
- Could the authors provide more detailed experimental results, including the impact of different hyperparameters and the convergence behavior of the method under varying conditions?

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
- Reasons: The paper presents a novel optimization algorithm, LAMB, which addresses the challenge of training large-scale deep neural networks using large batch sizes. The method's simplicity, effectiveness, and ease of implementation are highlighted, with theoretical analysis supporting its convergence to a stationary point in nonconvex settings. The empirical results demonstrate significant improvements in training times, which is crucial for practical applications. Despite some concerns regarding the novelty and the scope of theoretical contributions, the paper's practical impact and the clarity of presentation justify its acceptance. The decision aligns with the metareview, which acknowledges the paper's contribution to the field and recommends its acceptance for presentation as a poster.