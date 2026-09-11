 **Summary:**
The paper introduces two new variants of LSTM, sLSTM and mLSTM, aimed at addressing the limitations of traditional LSTMs in language modeling. sLSTM utilizes a scalar memory and a scalar update rule, focusing on revising storage decisions, while mLSTM employs a matrix memory and a covariance update rule for parallelization. These modifications are intended to enhance LSTM's capabilities, particularly in handling rare tokens and improving parallelizability. The authors propose integrating these variants into residual block modules, forming xLSTM, which is evaluated against state-of-the-art models like Transformers and other LSTMs. Despite the innovative approach, concerns are raised about the novelty and the empirical evidence supporting the claims of improvement over existing models.

**Strengths:**
- The paper is well-written, with clear and concise explanations of the proposed methods, making it accessible and easy to understand.
- The authors have identified and addressed the limitations of LSTMs, particularly in language modeling, and proposed innovative solutions to overcome these limitations.
- The introduction of sLSTM and mLSTM, which are novel modifications to the LSTM architecture, shows potential for improving the capabilities of LSTMs in handling rare tokens and parallelization.
- The paper provides a comprehensive analysis of the limitations of LSTMs and proposes modifications to address these issues, which are supported by theoretical and empirical evidence.
- The authors have demonstrated the effectiveness of their proposed methods through experiments, showing that xLSTM can perform competitively with state-of-the-art models in language modeling tasks.

**Weaknesses:**
- The paper lacks a clear motivation for the proposed modifications, particularly the need for a scalar memory and scalar update rule, which are not convincingly justified.
- The paper does not adequately compare the proposed methods with existing solutions, such as attention mechanisms and other LSTM variants, which could have provided a more robust evaluation of the proposed methods.
- The experimental results are not convincing, with some results showing inferior performance compared to existing models like LSTM and Transformers.
- The paper suffers from poor presentation, with small fonts and unclear figures, which makes it difficult to read and understand.
- The paper does not sufficiently address the scalability of the proposed methods, particularly in terms of computational efficiency and scalability to larger models.
- There is a lack of discussion on the limitations of the proposed methods, which is crucial for understanding the scope and applicability of the findings.

**Questions:**
- Could the authors clarify the motivation behind the choice of a scalar memory and scalar update rule in sLSTM?
- How does the proposed method compare to other LSTM variants and attention mechanisms in terms of performance and efficiency?
- Can the authors provide more details on the experimental setup, particularly the training and evaluation procedures, to ensure reproducibility?
- How do the authors address the scalability issues, especially in terms of computational efficiency and scalability to larger models?
- Could the authors discuss the limitations of their proposed methods and how these might affect their applicability in different scenarios?
- Why was the decision made to abandon memory mixing in mLSTM, and what are the implications of this choice?
- Can the authors provide more detailed comparisons with other models, such as Transformers and other LSTM variants, to better understand the relative performance of their proposed methods?

**Soundness:**
2 fair

**Presentation:**
2 fair

**Contribution:**
2 fair

**Rating:**
4 possibly reject, but has redeeming facets

**Paper Decision:**
- Decision: Reject
- Reasons: The paper, while introducing innovative modifications to the LSTM architecture, lacks sufficient empirical evidence to support its claims of improvement over existing models. The reviewers have pointed out that the experimental results do not convincingly demonstrate the superiority of the proposed methods over state-of-the-art models. Additionally, the paper suffers from poor presentation, which makes it difficult to read and understand, and lacks a thorough comparison with existing solutions. The metareview also highlights these issues, suggesting that the paper needs significant revisions to address these concerns before it can be considered for publication.