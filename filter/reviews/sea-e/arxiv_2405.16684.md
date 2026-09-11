 **Summary:**
The paper explores the relationship between data complexity and scaling laws in language models (LMs) by using gzip compression as a measure of data complexity. It introduces a new scaling law that adjusts the trade-off between model size and data size based on the data's compressibility. The authors generate synthetic datasets using probabilistic context-free grammars (PCFGs) to investigate how data complexity affects scaling laws. They find that more complex data requires more compute and a different trade-off between model size and data size. The paper also discusses how this new scaling law could be applied to real-world datasets, although the experiments are primarily conducted on synthetic data.

**Strengths:**
- The paper is well-written, clear, and easy to follow, making it accessible to a broad audience.
- The authors introduce a novel approach to measuring data complexity using gzip compression, which is a significant contribution to the field.
- The paper is original in its exploration of how data complexity affects scaling laws, which is a critical area of research in language model training.
- The use of probabilistic context-free grammars (PCFGs) to generate synthetic datasets is a creative and effective method for studying the relationship between data complexity and scaling laws.
- The paper provides a comprehensive analysis of the relationship between data complexity and scaling laws, which is a significant contribution to the field.

**Weaknesses:**
- The paper primarily uses synthetic data for its experiments, which limits the generalizability of the findings to real-world datasets.
- The paper does not adequately address the potential confounding effects of vocabulary size on the results, which could significantly impact the conclusions drawn.
- The paper's claims about the data-independence of scaling laws are not convincingly supported, as the results suggest that scaling laws are sensitive to data complexity.
- The paper's methodology and results are not clearly explained in some sections, making it difficult for readers to fully understand the implications and contributions of the study.
- The paper does not sufficiently address the limitations of its methodology, such as the potential confounding effects of vocabulary size and the generalizability of the findings to real-world datasets.

**Questions:**
- How does the paper address the potential confounding effects of vocabulary size on the results?
- Could the authors clarify the methodology and results in sections where the explanations are unclear or incomplete?
- How does the paper's methodology compare to other methods for measuring data complexity, such as those based on entropy or other information-theoretic measures?
- Can the authors provide more details on how the scaling laws are affected by the complexity of the data, particularly in relation to the gzip compression method used?
- How does the paper's methodology and results contribute to a better understanding of scaling laws in real-world datasets, and what implications do these findings have for practical applications in language model training?

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
- Reasons: The paper presents a novel approach to measuring data complexity using gzip compression, which is a significant contribution to the field. While the experiments are primarily conducted on synthetic data, the paper provides a compelling argument for the importance of data complexity in scaling laws. The methodology, although limited to synthetic data, is well-explained and contributes to a better understanding of how data complexity affects scaling laws. The paper is well-written and easy to follow, making it accessible to a broad audience. The reviewers have highlighted the need for more experiments on real-world datasets and a deeper exploration of the relationship between data complexity and scaling laws. However, these limitations do not detract from the paper's overall contribution to the field, and the decision to accept is based on the paper's originality, methodological soundness, and significance of results.