 **Summary:**
The paper introduces a method for adapting pretrained decoder-only large language models (LLMs) to encoder-decoder models, aiming to balance quality and efficiency. The authors explore different pretraining objectives and initialization techniques to optimize the model's performance. The proposed method involves initializing the encoder with weights from the decoder and then fine-tuning the entire model. The experiments, conducted on various benchmarks including pretraining, instruction tuning, and SuperGLUE, demonstrate that the adapted encoder-decoder models can achieve comparable or better performance than their decoder-only counterparts. However, the paper is criticized for its limited novelty and the lack of comprehensive experimental validation, particularly in terms of the scalability and generalizability of the findings.

**Strengths:**
- The paper addresses an important and relevant problem by exploring the adaptation of pretrained decoder-only LLMs to encoder-decoder models, which is crucial for achieving a better quality-efficiency trade-off.
- The authors have conducted extensive experiments to evaluate the effectiveness of their method, demonstrating that the adapted encoder-decoder models can achieve comparable or better performance than their decoder-only counterparts.
- The paper is well-written, making it easy to follow, and the experiments are comprehensive, covering various pretraining objectives and initialization techniques.
- The methodology is simple and effective, with a focus on reducing the demand for computation by adapting pretrained decoder-only LLMs to encoder-decoder models.
- The paper provides a detailed analysis of the impact of different pretraining objectives and initialization techniques on the performance of encoder-decoder models.

**Weaknesses:**
- The paper lacks a clear motivation for the research, and the methodology does not provide significant novelty as similar approaches have been explored in previous studies.
- The experiments are limited in scope, focusing primarily on the Gemma 2 model and not sufficiently validating the scalability and generalizability of the findings across different model families.
- There is a lack of detailed analysis on the impact of different pretraining objectives and initialization techniques on the performance of encoder-decoder models, and the paper does not explore the potential benefits of combining different pretraining objectives.
- The paper does not adequately address the limitations of the proposed method, such as the potential for overfitting and the need for more comprehensive experiments to validate the effectiveness of the proposed method.
- The paper could benefit from a more rigorous experimental validation, including a broader range of model families and a more detailed analysis of the impact of different pretraining objectives and initialization techniques.

**Questions:**
- Can the authors provide more details on the experimental setup, particularly the specifics of the pretraining and instruction tuning processes used in the experiments?
- How does the proposed method compare to other methods for adapting pretrained decoder-only LLMs to encoder-decoder models, such as those proposed in the "AdaptLLM" paper?
- What are the specific advantages of the proposed method over other existing methods, and how does it address the limitations of previous approaches?
- Could the authors provide more details on the experimental results, particularly the performance of the encoder-decoder models on different benchmarks and the impact of different pretraining objectives and initialization techniques?
- How does the proposed method perform in terms of inference speed, and what are the potential implications for practical deployment scenarios?

**Soundness:**
3 good

**Presentation:**
3 good

**Contribution:**
3 good

**Rating:**
5 marginally below the acceptance threshold

**Paper Decision:**
- Decision: Accept
- Reasons: The paper presents a method for adapting pretrained decoder-only LLMs to encoder-decoder models, which is a significant contribution to the field. The experiments, while not exhaustive, demonstrate the effectiveness of the proposed method in achieving a better quality-efficiency trade-off. The paper is well-written and clear, making it accessible to readers. However, the novelty of the method is limited, and the experimental validation is not comprehensive enough to fully support the claims made. The decision to accept is based on the paper's relevance and the potential impact of the proposed method, but with the understanding that the authors need to address the concerns regarding the novelty and the depth of experimental validation in the final version.