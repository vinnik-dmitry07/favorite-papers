 **Summary:**
The paper investigates how pre-trained large language models (LLMs) perform arithmetic operations, specifically focusing on addition, using Fourier features. The authors demonstrate that MLP layers primarily handle the approximation of the answer's magnitude using low-frequency features, while attention layers perform modular addition using high-frequency features. The study reveals that pre-training is crucial for learning these mechanisms, and the use of pre-trained token embeddings can enhance the model's performance. The paper also explores the role of Fourier features in the token embeddings of numbers, which are crucial for solving addition tasks. The findings suggest that LLMs do not merely memorize answers but actively compute solutions, which is a significant contribution to understanding the internal workings of these models.

**Strengths:**
- The paper provides a novel perspective on how pre-trained LLMs solve addition tasks by leveraging Fourier features, which are crucial for learning to solve addition tasks.
- The authors demonstrate that pre-trained LLMs use Fourier features in complementary ways: MLP layers primarily approximate the magnitude of the answer using low-frequency features, while attention layers primarily perform modular addition using high-frequency features.
- The paper is well-written, clearly explaining the experimental setup and the Fourier analysis framework, making it accessible and understandable.
- The findings are supported by extensive experiments and ablation studies, which validate the claims and provide insights into the role of Fourier features in LLMs.
- The paper is significant as it contributes to the understanding of the internal workings of LLMs, which is crucial for developing more effective and efficient models.

**Weaknesses:**
- The paper's focus on addition tasks might limit the generalizability of the findings to other mathematical operations or more complex tasks.
- The paper does not provide a detailed analysis of the specific Fourier features used by different models, which could affect the accuracy of the results.
- The paper's conclusions might not be applicable to other types of models or tasks, as the findings are specific to the GPT-2-XL model and the addition task.
- The paper does not discuss the limitations of the Fourier analysis framework, which could affect the validity of the conclusions.
- The paper does not include a detailed discussion on the limitations of the Fourier analysis framework, which could affect the validity of the conclusions.

**Questions:**
- How do the authors ensure that the Fourier features are not just a consequence of the training data, but rather an inherent property of the model?
- Can the authors provide more details on the specific Fourier features used by different models and how they affect the model's performance?
- How do the findings of this paper apply to other mathematical operations or more complex tasks, such as multiplication or division?
- Can the authors discuss the limitations of the Fourier analysis framework and how these limitations might affect the conclusions drawn from the study?
- How do the authors plan to extend the analysis to other types of models or tasks, and what implications might this have for the generalizability of the findings?

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
- Reasons: The paper presents a novel and insightful analysis of how pre-trained LLMs perform arithmetic operations using Fourier features. The findings are supported by extensive experiments and provide a new perspective on how these models compute answers, which is crucial for understanding their internal workings. The paper is well-written, clearly explaining the experimental setup and the Fourier analysis framework, making it accessible and understandable. The reviewers have highlighted the paper's contribution to the field and its potential impact on the development of more effective and efficient models. The decision to accept is based on the originality of the approach, methodological soundness, significance of results, and clarity and logic of presentation.