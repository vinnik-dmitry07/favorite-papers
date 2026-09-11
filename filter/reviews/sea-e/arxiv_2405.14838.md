 **Summary:**
The paper introduces a novel method for implicit chain-of-thought (CoT) reasoning, termed Stepwise Internalization (SI), which aims to internalize reasoning steps in language models without explicit CoT tokens. This approach involves a curriculum learning process where intermediate CoT tokens are gradually removed, allowing the model to learn to reason implicitly. The method is evaluated on various tasks, including multi-digit multiplication and grade-school math reasoning, showing improvements over existing methods like ICoT-KD. The paper also discusses the potential of this method in reducing computational costs and improving inference speed. However, concerns are raised about the generalizability of the method to more complex tasks and its dependency on specific training data.

**Strengths:**
- The paper introduces a novel approach to implicit CoT reasoning, which is a significant advancement in the field.
- The methodology is well-explained, with clear descriptions of the training process and the use of a curriculum learning approach.
- The paper demonstrates the effectiveness of the proposed method through empirical results, showing improvements over existing methods like ICoT-KD.
- The paper is well-written, making it easy to follow, and includes comprehensive ablation studies that help in understanding the impact of various components of the method.
- The approach is simple yet effective, with a straightforward methodology that is easy to understand and implement.
- The paper provides a thorough evaluation of the method, including comparisons with existing methods and a detailed analysis of the results.

**Weaknesses:**
- The paper primarily focuses on specific tasks like multi-digit multiplication and grade-school math reasoning, which limits the generalizability of the findings.
- The method's dependency on the availability of training data with both lower-digit and higher-digit arithmetic task demonstrations is not adequately addressed.
- The paper lacks a broader evaluation across different types of reasoning tasks, which could have provided a more comprehensive understanding of the method's effectiveness.
- The paper does not discuss the limitations of the proposed method, such as its dependency on the specific training data and the potential for overfitting.
- The paper does not include a comparison with other methods like MathGLM, which could have provided a more robust evaluation of the proposed method.
- The paper does not discuss the potential negative societal impacts of the work, which is a significant omission.

**Questions:**
- Could the authors provide more details on how the method could be adapted to other types of reasoning tasks beyond arithmetic?
- How does the method perform when applied to other types of reasoning tasks, such as those involving natural language processing?
- Could the authors discuss the potential for overfitting in the method, especially given the dependency on specific training data?
- How does the method compare to other methods like MathGLM, particularly in terms of accuracy and computational efficiency?
- Could the authors provide more details on the training process, such as the specifics of the curriculum learning approach and the removal of CoT tokens?
- How does the method handle the potential for instability during training, especially when removing CoT tokens too quickly?

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
- Reasons: The paper presents a novel method for implicit CoT reasoning that shows promise in reducing computational costs and improving inference speed. The method's simplicity and effectiveness, as demonstrated through empirical results, are notable strengths. However, concerns about the generalizability of the method to more complex tasks and its dependency on specific training data are raised. The paper is well-written, making it easy to follow, and the methodology is well-explained. The decision to accept is based on the paper's originality, methodological soundness, and the significance of the results, despite some limitations in the scope of evaluation and potential for broader applicability. The decision aligns with the reviewers' consensus and the AC's recommendation for acceptance, suggesting that the paper should be presented as a poster to allow for further discussion and feedback.