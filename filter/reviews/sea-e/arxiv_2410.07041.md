 **Summary:**
The paper explores the impact of repeated examples on the performance of transformer models, specifically focusing on tasks such as computing the greatest common divisor, modular multiplication, and eigenvalue estimation. The study demonstrates that models trained on smaller, repeated datasets can outperform those trained on larger, non-repeated datasets. This effect is attributed to the "two-set training" method, where a subset of examples is repeated during training, which enhances learning speed and performance. The paper also investigates the benefits of this method across different model sizes and training budgets, showing that it can lead to emergent properties in models.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation and a well-structured presentation of the results.
- The experiments are well-designed, and the results are convincing, showing that repetition of training examples can lead to better performance.
- The paper introduces an interesting phenomenon where models trained on a small set of repeated examples can outperform models trained on a larger set of examples, which is a novel contribution to the field.
- The paper provides a clear explanation of the experimental setup and results, which are supported by a variety of experiments, including ablation studies.
- The findings are significant and have implications for the field of deep learning, particularly in the context of data repetition and its impact on model performance.

**Weaknesses:**
- The paper lacks a thorough discussion on the limitations of the study, which could help in understanding the scope and applicability of the findings.
- The paper does not compare its results with existing methods such as curriculum learning, which could provide a more comprehensive understanding of the effectiveness of the proposed methods.
- The paper does not discuss the potential negative societal impacts of the findings, which could be a significant concern for some readers.
- The paper's claims about the generalizability of the findings to larger models or more complex tasks are not convincingly supported by the evidence presented.
- The paper does not adequately address the potential negative effects of data repetition on model performance, particularly in terms of overfitting or the emergence of biases.
- The paper could benefit from a more detailed discussion on the computational costs associated with the proposed methods, especially in terms of training time and resource usage.

**Questions:**
- Can the authors clarify whether the findings can be generalized to larger models or more complex tasks? If not, what are the specific limitations of the study?
- How do the authors address the potential negative impacts of data repetition on model performance, particularly in terms of overfitting or the emergence of biases?
- Could the authors provide more details on the computational costs associated with the proposed methods, including training time and resource usage?
- How do the authors ensure that the models are not overfitting to the repeated examples, especially in scenarios where the repetition rate is high?
- Can the authors discuss the potential negative societal impacts of the findings, particularly in terms of the implications for fairness and bias in machine learning models?
- How do the authors explain the observed differences in performance between models trained on different sets of examples, especially in terms of the impact of data repetition on model performance?

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
- Reasons: The paper presents a compelling case for the benefits of repeated examples in training transformer models, demonstrating that this approach can lead to improved performance and learning speed. The experimental setup is well-designed, and the results are convincingly presented. The paper's contribution to the field is significant, particularly in challenging the conventional wisdom about the need for diverse training data. The decision to accept is based on the paper's originality, methodological soundness, and the significance of its results, despite some concerns about the generalizability of the findings and the potential negative societal impacts. The decision to present the paper as a poster allows for further discussion and exploration of these issues.