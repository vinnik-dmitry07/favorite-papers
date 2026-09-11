 **Summary:**
The paper investigates the limitations of Transformers in learning multi-digit multiplication, focusing on the failure of standard fine-tuning (SFT) and the success of Implicit Chain-of-Thought (ICoT) training. The authors reverse-engineer the ICoT model to reveal the mechanisms behind its success, including the use of attention to construct a directed acyclic graph for caching and retrieving pairwise partial products, and the representation of digits using Fourier basis. The paper also introduces an auxiliary loss to guide the model to predict the running sum, enhancing its ability to learn long-range dependencies. The findings suggest that SFT models lack the necessary inductive biases for multi-digit multiplication, and the ICoT model's success is attributed to its ability to encode long-range dependencies.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation and interesting findings.
- The authors have conducted a thorough analysis of the ICoT model, revealing its mechanisms and providing insights into why it succeeds in multi-digit multiplication while standard fine-tuning (SFT) fails.
- The paper introduces an auxiliary loss to guide the model to predict the running sum, which is a novel approach to addressing the limitations of SFT models.
- The use of Fourier basis for digit representation is an innovative approach that adds depth to the understanding of the model's functionality.
- The paper provides a detailed reverse-engineering of the ICoT model, which is a significant contribution to the field.

**Weaknesses:**
- The paper lacks a comprehensive comparison with other models or methods that might also learn long-range dependencies, which could provide a more robust validation of the findings.
- The paper's focus on a specific task (multi-digit multiplication) limits the generalizability of the findings to other tasks or models.
- There is a lack of discussion on the limitations of the proposed auxiliary loss, particularly its applicability to other tasks or models.
- The paper does not adequately address the scalability of the findings to larger or more complex models, which could limit the practical utility of the insights.
- The paper's reliance on the ICoT model's success to draw conclusions about the limitations of SFT models might not be convincing without a more direct comparison or validation.

**Questions:**
- How does the auxiliary loss compare to other methods that might also learn long-range dependencies? Could other methods be more effective or generalizable?
- How does the proposed auxiliary loss perform on other tasks or models? Is it a generalizable solution or specific to the multi-digit multiplication task?
- Can the authors provide more details on the training data format, sample size, and hyperparameters used in the experiments?
- How does the model's performance on multi-digit multiplication compare to other models that have been trained using different methods?
- Could the authors elaborate on the limitations of the proposed auxiliary loss and discuss potential improvements or alternative approaches?
- How does the use of Fourier basis for digit representation contribute to the model's ability to learn long-range dependencies? Could other representations be as effective?

**Soundness:**
3 good

**Presentation:**
3 good

**Contribution:**
3 good

**Rating:**
6 weak accept

**Paper Decision:**
- Decision: Accept
- Reasons: The paper provides a comprehensive analysis of the ICoT model's success in multi-digit multiplication, revealing interesting mechanisms such as the use of attention to construct a directed acyclic graph and the representation of digits using Fourier basis. The introduction of an auxiliary loss to guide the model to predict the running sum is a novel approach that enhances the model's ability to learn long-range dependencies. The paper is well-written, clear, and easy to follow, making it accessible to a broad audience. Despite some concerns about the generalizability of the findings and the limited comparison with other models, the paper's contributions are significant and the methodological soundness is high. The decision to accept is based on the paper's originality, methodological soundness, and the significance of its findings, even though the scope of the study is somewhat limited.