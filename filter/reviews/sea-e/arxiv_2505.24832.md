 **Summary:**
The paper investigates the memorization capacity of language models by proposing a novel method that decomposes memorization into unintended and intended components. It introduces a new metric, Kolmogorov memorization, which is used to quantify the amount of information a model retains from a dataset. The authors demonstrate that this metric can be estimated using arithmetic coding, which is then applied to measure the memorization capacity of various language models. The study explores how this capacity scales with model size and dataset size, providing insights into the relationship between model capacity and memorization. The paper also discusses the implications of these findings for understanding the behavior of large language models and the potential for improving model training and evaluation.

**Strengths:**
- The paper introduces a novel method to measure the memorization capacity of language models using Kolmogorov complexity, which is a significant contribution to the field.
- The authors provide a clear and well-structured presentation of their methodology and results, making the paper accessible and understandable.
- The paper addresses an important and timely topic, focusing on the memorization capacity of large language models, which is a critical issue in the context of data privacy and model performance.
- The proposed method is theoretically sound and offers a practical approach to estimating memorization capacity, which is supported by a range of experiments and validations.
- The paper provides a comprehensive discussion on the limitations and potential improvements of the proposed method, which enhances its credibility and applicability.

**Weaknesses:**
- The paper could benefit from a more detailed discussion on the limitations and potential biases in the estimation of Kolmogorov complexity, especially in relation to the choice of reference models.
- The experimental setup and results, particularly in Section 3.2, are not clearly explained, making it difficult to replicate or understand the results fully.
- The paper's claims about the capacity of language models are not convincingly supported by the data presented, and there is a lack of detailed analysis or discussion on the implications of these findings.
- The paper's focus on synthetic data and the use of arithmetic coding as the primary method for estimating Kolmogorov complexity may limit the generalizability of the results to real-world scenarios.
- There is a need for more rigorous testing and validation of the proposed method, particularly in terms of its applicability to different types of data and model architectures.

**Questions:**
- How does the choice of reference model affect the estimation of Kolmogorov complexity, and what are the potential biases introduced by using different reference models?
- Can you clarify the experimental setup and results in Section 3.2, particularly the choice of parameters and the implications of these choices for the results?
- How does the proposed method compare to other existing methods for measuring memorization capacity, and what are the advantages or disadvantages of using Kolmogorov complexity over other approaches?
- What are the implications of the findings regarding the capacity of language models, and how do these findings impact the design and training of large language models?
- Could you provide more details on the experimental setup and results, particularly in terms of the datasets used and the conditions under which the experiments were conducted?

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
- Reasons: The paper presents a novel method for measuring the memorization capacity of language models, which is a significant contribution to the field. The method, based on Kolmogorov complexity, is well-explained and supported by a range of experiments. The paper is well-written, clear, and provides valuable insights into the behavior of large language models. Despite some concerns regarding the experimental setup and the generalizability of the results, the paper's contributions outweigh these limitations. The decision to accept is supported by the paper's originality, methodological soundness, and the significance of its results.