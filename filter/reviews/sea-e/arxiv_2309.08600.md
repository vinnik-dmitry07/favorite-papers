 **Summary:**
The paper introduces a novel method using sparse autoencoders to identify and extract monosemantic features from language models, aiming to address the issue of polysemanticity in neural networks. The proposed method involves training an autoencoder with a sparsity penalty on the hidden activations to learn a set of directions in the activation space that can reconstruct the original activations from a sparse linear combination of these directions. This approach is evaluated on the Pythia-70M language model, demonstrating that the learned features are more interpretable and monosemantic than those identified by other methods. The paper also explores the application of these features in causal mediation analysis, showing that they can be used to identify causally important features for a specific task.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation and a novel approach to addressing the problem of polysemanticity in neural networks.
- The proposed method is simple, effective, and demonstrated to be more interpretable than other methods, as shown in Figure 2.
- The method is scalable and can be applied to large language models, which is a significant advantage in the field.
- The paper includes a thorough evaluation of the proposed method, including comparisons with other methods and a detailed analysis of the learned features.
- The authors have provided a detailed discussion on the limitations of their work and potential future directions, which is commendable for transparency and reproducibility.

**Weaknesses:**
- The paper lacks a detailed discussion on the limitations of the proposed method, particularly in terms of its applicability to different types of neural networks and its scalability to larger models.
- The paper could benefit from more detailed explanations and examples of how the learned features can be used for targeted model editing, as mentioned in Section 5.2.
- The paper does not sufficiently compare the proposed method with other existing methods for feature disentanglement, which could provide a more robust evaluation of the proposed approach.
- The paper could benefit from a more detailed discussion on the computational complexity and resource requirements of the proposed method, especially in relation to other methods.
- The paper could be improved by providing more detailed examples and case studies to illustrate the practical applications of the learned features.

**Questions:**
- How does the proposed method compare to other methods for feature disentanglement, particularly in terms of performance and scalability?
- Can the authors provide more detailed examples and case studies to illustrate the practical applications of the learned features?
- How does the proposed method perform on other types of neural networks, such as convolutional neural networks or recurrent neural networks?
- How does the computational complexity and resource requirements of the proposed method compare to other methods for feature disentanglement?
- Can the authors provide more details on how the learned features can be used for targeted model editing, and what specific benefits this provides over other methods?
- How does the paper address the issue of polysemanticity in neural networks, particularly in relation to the superposition of features?

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
- Reasons: The paper presents a novel method for identifying monosemantic features in language models using sparse autoencoders, which is a significant contribution to the field of interpretability in neural networks. The method is well-explained, and the results demonstrate its effectiveness in improving interpretability. The paper is well-written, clear, and easy to follow, making it accessible to a broad audience. The method's scalability and potential for application to large language models are also highlighted. However, the paper could benefit from a more detailed discussion on the limitations and potential applications of the proposed method, as well as comparisons with other methods for feature disentanglement. The decision to accept is based on the paper's originality, methodological soundness, and the significance of its results, despite some concerns about the depth of discussion on limitations and potential applications.