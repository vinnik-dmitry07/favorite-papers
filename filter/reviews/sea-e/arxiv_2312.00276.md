 **Summary:**
The paper introduces Automated Continual Learning (ACL), a novel approach to continual learning that utilizes self-referential neural networks to metalearn their own in-context continual learning algorithms. ACL is designed to address the challenges of catastrophic forgetting by encoding continual learning desiderata into its metalearning objectives. The method is evaluated on various benchmarks, including Split-MNIST, and shows promising results in preventing catastrophic forgetting. However, the paper's experimental evaluation is limited, and the generalization of the proposed method to more complex datasets and real-world applications is not thoroughly explored. The method's novelty is questioned due to its similarity to existing methods, and the paper's presentation and clarity need improvement.

**Strengths:**
- The paper introduces a novel approach to continual learning by training self-referential neural networks to metalearn their own in-context continual learning algorithms, which is a significant advancement in the field.
- The methodology is well-explained, with clear and detailed descriptions of the proposed method, including the use of self-referential weight matrices and the metalearning objectives.
- The paper provides a comprehensive evaluation of the proposed method, including a variety of experiments that demonstrate the effectiveness of the ACL method in preventing catastrophic forgetting.
- The paper is well-written, making it accessible and easy to follow, with a clear structure and logical flow that enhances understanding.
- The authors have made their code publicly available, which is a commendable effort towards reproducibility and transparency in research.

**Weaknesses:**
- The paper lacks a detailed comparison with existing methods, particularly in terms of performance metrics and methodological approaches. This makes it difficult to assess the true novelty and effectiveness of the proposed method.
- The experimental evaluation is limited to simple datasets, which may not fully demonstrate the generalization capabilities of the proposed method.
- The paper does not provide sufficient details on the experimental setup, such as the training and testing data splits, which could affect the reproducibility and reliability of the results.
- The paper's presentation and clarity could be improved, particularly in the introduction and background sections, where the motivation and relevance of the work are not clearly articulated.
- The paper's contribution to the field is questioned due to its similarity to existing methods, particularly those that use self-referential weight matrices for continual learning.
- The paper does not adequately address the limitations of the proposed method, such as its applicability to more complex datasets and its generalization to real-world applications.

**Questions:**
- Can the authors provide a more detailed comparison with existing methods, including a discussion on how the proposed method differs from and improves upon these existing approaches?
- How does the proposed method perform on more complex datasets, such as CIFAR-100, and how does it compare to other methods in these settings?
- Can the authors provide more details on the experimental setup, including the training and testing data splits, to enhance the reproducibility and reliability of the results?
- How does the proposed method handle the challenges of domain and length generalization in continual learning?
- Could the authors clarify the role and impact of the "4-learning rate version" in the proposed method, and how it affects the performance and generalization of the model?
- How does the proposed method compare to other methods in terms of computational efficiency and scalability, especially when applied to larger and more complex datasets?

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
- Reasons: The paper introduces a novel approach to continual learning that addresses the problem of catastrophic forgetting through the use of self-referential neural networks. The method is well-explained and evaluated on various benchmarks, showing promising results. However, the experimental evaluation is limited, and the paper could benefit from a more detailed comparison with existing methods and a broader evaluation on more complex datasets. The decision to accept is based on the paper's novel approach, the clarity of its presentation, and the potential impact of the proposed method in the field of continual learning. The decision also considers the paper's contribution to the ongoing research in the area and the need for further exploration and validation of the proposed method in more complex and varied settings.