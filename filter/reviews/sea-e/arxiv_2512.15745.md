 **Summary:**
The paper introduces LLaDA2.0, a novel approach to training large-scale discrete diffusion language models (dLLMs) by converting pre-trained auto-regressive (AR) models into dLLMs using a three-phase training strategy. This strategy involves a warm-up phase for increasing block sizes, a stable phase for full-sequence diffusion training, and a decay phase for reverting to compact block diffusion. The paper also incorporates a document-level attention mask to prevent spurious connections across unrelated texts and employs a top-k checkpoint merge strategy for generalization. The models, available in 16B and 100B parameter sizes, are evaluated on a diverse set of benchmarks, showing competitive performance with AR models. The paper also discusses the challenges and solutions in training dLLMs, including inference speed and parallel decoding, and provides insights into the training and inference infrastructure used.

**Strengths:**
- The paper presents a novel approach to training large-scale discrete diffusion language models (dLLMs) by converting pre-trained auto-regressive (AR) models, which is a significant advancement in the field.
- The methodology is well-explained, with clear descriptions of the training pipeline, including the Warmup-Stable-Decay (WSD) strategy, which is a novel contribution to the field.
- The paper is well-written, making it accessible and understandable, with comprehensive evaluations on a diverse set of benchmarks, demonstrating the effectiveness of the proposed method.
- The authors have released the models and training code, which is a valuable contribution to the community, facilitating further research and development in this area.
- The paper provides a detailed analysis of the training and inference infrastructure used, which is crucial for understanding the practical implementation of the proposed methods.
- The proposed method achieves competitive performance with state-of-the-art AR models, and the models are available in both 16B and 100B parameter sizes, which can be beneficial for various applications.

**Weaknesses:**
- The paper lacks a detailed comparison with other dLLMs, such as Dream-7B and RND-1, which could provide a clearer understanding of the advantages and limitations of the proposed method.
- The evaluation metrics used are not clearly defined, which could lead to confusion about the performance claims made in the paper.
- There is a lack of discussion on the limitations of the proposed method, which is crucial for understanding the scope and applicability of the findings.
- The paper does not provide a detailed analysis of the training and inference costs, which could help in understanding the practical feasibility of the proposed method.
- The paper does not discuss the limitations of the proposed method, which is crucial for understanding the scope and applicability of the findings.
- The paper does not include a discussion on the limitations of the proposed method, which is crucial for understanding the scope and applicability of the findings.

**Questions:**
- Could the authors provide a more detailed comparison with other dLLMs, such as Dream-7B and RND-1, to clarify the advantages and limitations of the proposed method?
- Can the authors clarify the evaluation metrics used in the paper to ensure a better understanding of the performance claims?
- How do the authors address the limitations of the proposed method, and what are the potential areas for future research to overcome these limitations?
- Could the authors provide more details on the training and inference costs associated with the proposed method, including computational resources, time, and financial costs?
- How does the proposed method compare in terms of inference speed and parallel decoding with other dLLMs, especially those that use different training strategies?
- Can the authors discuss the potential impact of the proposed method on the development of large-scale dLLMs, and what are the implications for the broader research community?

**Soundness:**
3 good

**Presentation:**
3 good

**Contribution:**
3 good

**Rating:**
7 accept, but needs minor improvements

**Paper Decision:**
- Decision: Accept
- Reasons: The paper presents a significant advancement in the field of training large-scale discrete diffusion language models by converting pre-trained auto-regressive models, which is a novel approach. The methodology is well-explained, and the models are available, which is beneficial for further research. The paper is well-received by the reviewers, who appreciate the novelty and the practical implications of the proposed method. The reviewers suggest minor improvements in the clarity of the evaluation metrics and a more detailed discussion on the limitations and potential future work. The decision to accept is based on the paper's originality, methodological soundness, significance of results, and clarity and logic of presentation.