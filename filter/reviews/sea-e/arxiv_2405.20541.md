 **Summary:**
The paper investigates the use of perplexity-based data pruning for improving the performance of large language models (LLMs) by training smaller models on a subset of the pretraining data and selecting samples based on their perplexity scores. The methodology is tested across various datasets, including Pile and Dolma, and demonstrates that this approach can lead to significant improvements in downstream task performance and training efficiency. The paper also explores the impact of different pruning strategies and dataset compositions on the effectiveness of perplexity-based pruning. However, it lacks a comprehensive theoretical analysis and comparison with other data pruning methods, which could enhance its contribution to the field.

**Strengths:**
- The paper is well-written, easy to follow, and provides a clear and concise presentation of the methodology and results.
- The empirical results are strong, demonstrating that perplexity-based pruning can lead to significant improvements in downstream task performance and training efficiency.
- The paper is original in its approach to using perplexity as a metric for data pruning, which is a novel and interesting idea.
- The experiments are well-designed, and the paper is well-organized, making it easy to understand the contributions and the experimental setup.
- The paper provides a comprehensive evaluation of the proposed method, including various datasets and model sizes, which supports the robustness of the findings.

**Weaknesses:**
- The paper lacks a comprehensive theoretical analysis, which could provide deeper insights into the effectiveness of perplexity-based pruning.
- The comparison with other data pruning methods is insufficient, which could help in understanding the relative advantages and disadvantages of the proposed method.
- The paper does not provide sufficient details on the training and evaluation of the reference model, which is crucial for understanding the methodology.
- The paper could benefit from a more detailed discussion on the limitations of the proposed method, including potential negative societal impacts and ethical considerations.
- The paper does not adequately address the computational cost of training the reference model, which could be a significant barrier for practical implementation.
- The paper's claims about the superiority of perplexity-based pruning over other methods are not sufficiently supported by the experimental results.

**Questions:**
- Can the authors provide a more detailed explanation of why perplexity-based pruning is effective, perhaps through a theoretical analysis or additional experiments?
- How does the proposed method compare to other data pruning methods, and what are the specific advantages and disadvantages of using perplexity as a metric?
- Could the authors clarify the training and evaluation of the reference model, including the details of the training data, hyperparameters, and evaluation metrics used?
- How does the proposed method perform in different training regimes, such as over-training or data-constrained settings?
- Can the authors provide more details on the computational cost of training the reference model and discuss potential strategies for reducing this cost?
- How does the proposed method handle the potential for biased estimators in the pruned datasets, and what steps are taken to mitigate these biases?

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
- Reasons: The paper presents a novel approach to data pruning using perplexity, which shows promising results in improving the performance of large language models. The methodology is well-explained, and the empirical results are robust, demonstrating the effectiveness of the proposed method. The paper is well-written and easy to follow, making it accessible to a broad audience. However, the paper could benefit from a more comprehensive theoretical analysis and a more detailed comparison with other data pruning methods. Despite these limitations, the paper's contributions are significant enough to warrant acceptance, particularly in the context of its novel approach and the empirical evidence provided. The decision to accept is further supported by the positive feedback from reviewers, who noted the paper's originality and the potential impact of the findings on the field.