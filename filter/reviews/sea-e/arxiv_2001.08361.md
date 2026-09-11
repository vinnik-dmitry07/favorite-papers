 **Summary:**
The paper presents a comprehensive empirical study on the scaling laws of neural language models, focusing on the relationship between model size, dataset size, and compute used for training. The authors find that the loss scales as a power-law with these factors, with some trends spanning over seven orders of magnitude. The study also explores the effects of model architecture details, showing that network width or depth have minimal effects within a certain range. The paper proposes a simple equation to determine the optimal allocation of a fixed compute budget, suggesting that larger models are more sample-efficient and that optimally compute-efficient training involves training very large models on a relatively modest amount of data. The findings are supported by extensive experiments and theoretical analysis, providing valuable insights into the scaling behaviors of large language models.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation and a well-structured presentation of the results.
- The experimental results are extensive, covering a wide range of model sizes and datasets, and the authors provide a detailed analysis of the scaling laws for language model performance.
- The paper introduces a simple equation to determine the optimal allocation of a fixed compute budget, which is a significant contribution to the field.
- The findings are supported by extensive experiments and theoretical analysis, providing valuable insights into the scaling behaviors of large language models.
- The paper is a significant contribution to the understanding of scaling laws for large language models, which is crucial for the development of more efficient and effective models.

**Weaknesses:**
- The paper lacks a clear discussion on the limitations of the findings, which could help readers understand the scope and applicability of the results.
- The paper could benefit from more detailed discussions on the implications of the findings for practical applications, such as the development of more efficient and effective models.
- The paper does not provide a detailed discussion on the limitations of the experiments, which could help readers understand the assumptions and constraints of the study.
- The paper could benefit from a more thorough discussion on the theoretical underpinnings of the observed scaling laws, particularly in relation to the size of the training data and the computational resources used.
- The paper could be improved by including more detailed discussions on the implications of the findings for the design and training of large language models, including the potential for automated model size selection based on compute budgets.

**Questions:**
- Could the authors provide more detailed discussions on the limitations of the experiments, including the assumptions and constraints of the study?
- How do the findings of this paper relate to the scaling laws for other types of models, such as image models?
- Could the authors discuss the implications of the findings for the design and training of large language models, particularly in terms of optimizing the use of computational resources?
- How do the findings of this paper compare to other recent studies on scaling laws for large language models?
- Could the authors provide more detailed discussions on the theoretical underpinnings of the observed scaling laws, particularly in relation to the size of the training data and the computational resources used?

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
- Reasons: The paper provides a significant contribution to the understanding of scaling laws for large language models, which is crucial for the development of more efficient and effective models. The experimental results are extensive and well-supported by theoretical analysis, demonstrating a power-law relationship between model size, dataset size, and compute used for training. The findings are clearly presented and the paper is well-written, making it accessible and easy to follow. The reviewers have highlighted the paper's originality, methodological soundness, and the significance of its results, which support its acceptance. The decision to accept is further supported by the clarity and logic of the presentation, and the potential high impact of the paper on the field.