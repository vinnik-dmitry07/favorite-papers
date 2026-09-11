 **Summary:**
The paper introduces Unlimiformer, a novel approach to handling long-range dependencies in transformer models by utilizing a k-nearest neighbors (kNN) search to select relevant tokens for cross-attention. This method allows for the handling of unbounded input sequences, improving computational efficiency and potentially enhancing the performance of existing models like BART and Longformer. The methodology involves encoding input sequences in overlapping chunks, storing these encodings in a kNN index, and retrieving relevant keys for attention during decoding. The paper presents several training strategies, including early stopping and random encoding, to optimize the use of the kNN index. The effectiveness of Unlimiformer is demonstrated through experiments on various long-document and book-summarization datasets, showing improvements over existing models. However, concerns are raised about the novelty of the approach, as similar methods have been previously explored, and the paper's empirical results are not consistently superior across all datasets.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation and a well-defined problem statement.
- The proposed method is simple, effective, and efficient, with a novel approach to handling long-range dependencies in transformer models.
- The method is generic and can be applied to any existing encoder-decoder transformer model without modifying the code, making it adaptable to various applications.
- The paper provides a thorough evaluation of the proposed method, demonstrating its effectiveness in improving the performance of existing models like BART and Longformer.
- The method is computationally efficient, with a sublinear time complexity for indexing and retrieval, which is crucial for handling long input sequences.
- The paper includes a detailed analysis of the method's performance and its impact on the attention mechanism, which is insightful and contributes to the understanding of the method's operation.

**Weaknesses:**
- The paper lacks a detailed comparison with existing methods, particularly in terms of computational efficiency and the effectiveness of the retrieval process.
- The novelty of the approach is questionable, as similar methods have been previously explored, such as the use of kNN for attention and the handling of long-range dependencies in transformers.
- The paper's experimental results are not consistently superior across all datasets, raising concerns about the generalizability of the method.
- There is a lack of discussion on the limitations of the method, particularly in terms of its applicability to different types of datasets and its scalability to very large input sequences.
- The paper does not provide a detailed comparison of the computational costs of the proposed method, which is crucial for understanding its practical applicability.
- The paper lacks a detailed discussion on the retrieval process, including the quality of the retrieved keys and the impact of retrieval on the model's performance.

**Questions:**
- Can the authors provide a more detailed comparison of the computational costs of the proposed method, including the time and memory requirements for indexing and retrieval?
- How does the retrieval process affect the model's performance, particularly in terms of the quality of the retrieved keys and their impact on the attention mechanism?
- Could the authors provide more details on the training strategies used, particularly the random encoding and retrieval training, and how these strategies affect the model's performance?
- How does the method perform on other types of datasets, particularly those that do not involve summarization?
- Could the authors discuss the limitations of the method, particularly in terms of its applicability to different types of datasets and its scalability to very large input sequences?
- How does the method compare to other retrieval-augmented models, particularly in terms of computational efficiency and effectiveness?

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
- Reasons: The paper introduces a novel approach to handling long-range dependencies in transformer models, which is both innovative and practical. The method is well-explained, and the experimental results, while not consistently superior, demonstrate a clear improvement over existing models. The paper is well-written, making it accessible and understandable, which is crucial for its dissemination. The reviewers have highlighted some concerns regarding the novelty and the generalizability of the method, but these do not detract significantly from the paper's contributions. The decision to accept is based on the paper's originality, methodological soundness, and the significance of its results, despite some limitations in the empirical evaluation and the need for more comprehensive comparisons.