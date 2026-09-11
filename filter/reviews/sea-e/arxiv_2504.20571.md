 **Summary:**
The paper explores the effectiveness of reinforcement learning with verifiable rewards (RLVR) using a single training example, a concept termed 1-shot RLVR. This approach is demonstrated to enhance mathematical reasoning capabilities in large language models (LLMs) by improving performance on benchmarks like MATH500 and AIME. The paper also investigates the impact of historical variance scores in data selection and the role of entropy loss in post-saturation generalization. The results indicate that 1-shot RLVR can achieve performance comparable to traditional methods using thousands of examples, suggesting that the base model's reasoning capabilities can be significantly improved with minimal training data.

**Strengths:**
- The paper presents a novel approach to reducing the training dataset for RLVR, showing that a single example can achieve similar performance to using thousands of examples.
- The findings are supported by a thorough analysis of the historical variance score and its impact on data selection, which is a significant contribution to the field.
- The paper is well-written, clear, and easy to follow, making the complex concepts accessible to a broad audience.
- The experiments are well-designed, and the results are convincing, demonstrating the effectiveness of the proposed method.
- The paper introduces interesting phenomena such as post-saturation generalization, which is a valuable contribution to the understanding of RLVR.
- The paper provides a detailed analysis of the impact of different components of the RL loss function, which is crucial for understanding the effectiveness of the proposed method.

**Weaknesses:**
- The paper lacks a detailed discussion on the limitations of the proposed method, particularly in terms of its applicability to other types of reasoning tasks beyond mathematics.
- The paper does not sufficiently compare the proposed method with other existing methods, such as those using different RL algorithms or different types of rewards.
- The paper could benefit from a more comprehensive discussion on the generalizability of the findings across different LLMs and RL algorithms.
- The paper does not sufficiently address the issue of overfitting, which is a significant concern in RLVR.
- The paper does not provide sufficient evidence to support the claim that the base model already possesses significant reasoning capabilities, which is a critical assumption underlying the study.
- The paper could benefit from a more detailed discussion on the role of the entropy loss in post-saturation generalization, as it is a key component of the proposed method.

**Questions:**
- Can the authors provide more details on the historical variance score and its impact on data selection? How does this score influence the performance of the model?
- How does the proposed method compare with other existing methods, particularly in terms of computational efficiency and performance on different types of reasoning tasks?
- Could the authors clarify the role of the entropy loss in post-saturation generalization? Is it a necessary component, or could other methods achieve similar results?
- How does the proposed method perform when applied to other types of reasoning tasks beyond mathematics? Are there any specific types of reasoning tasks where the method might not be effective?
- Could the authors provide more evidence to support the claim that the base model already possesses significant reasoning capabilities? How does this assumption hold up under different testing conditions?
- How does the proposed method handle overfitting, particularly in the context of RLVR? What measures can be taken to prevent or mitigate overfitting?

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
- Reasons: The paper presents a novel approach to RLVR using a single training example, demonstrating its effectiveness in enhancing mathematical reasoning capabilities in LLMs. The methodology is well-explained, and the results are convincing, showing that the proposed method can achieve performance comparable to traditional methods using thousands of examples. The paper also addresses interesting phenomena such as post-saturation generalization, which is a significant contribution to the field. While there are concerns about the generalizability of the findings and the need for more comprehensive comparisons with other methods, the paper is well-written, clearly presented, and provides valuable insights into the use of RLVR with minimal training data. The decision to accept is based on the paper's originality, methodological soundness, and the significance of its results, as well as the clarity and logic of its presentation.