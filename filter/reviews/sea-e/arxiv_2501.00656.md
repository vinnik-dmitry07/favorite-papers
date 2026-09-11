 **Summary:**
The paper introduces OLMo-2, an open-source language model that builds upon the OLMo-0424 model, incorporating various improvements such as new model architectures, training recipes, and data curation strategies. The authors have made significant efforts to enhance training stability and efficiency, using a new data mix called Dolmino Mix 1124 and a modified training pipeline. The model's performance is evaluated on various benchmarks, showing improvements over previous models, although the paper lacks a thorough comparison with state-of-the-art models and does not include a detailed discussion on the limitations and societal impacts of the model.

**Strengths:**
- The paper provides a detailed analysis of the training process, including the identification and resolution of issues such as repeated n-grams, which can lead to training instability.
- The authors have made significant efforts to improve training stability and efficiency, which is crucial for large-scale language model training.
- The paper is well-written, clear, and easy to follow, making it accessible to a broad audience.
- The authors have released all training artifacts, including model weights, training data, training code, training logs, and thousands of intermediate checkpoints, which is a significant contribution to the community.
- The paper includes a detailed analysis of the training process, which is beneficial for understanding the challenges and solutions in training large language models.
- The authors have made significant efforts to improve training stability and efficiency, which is crucial for large-scale language model training.

**Weaknesses:**
- The paper lacks a thorough comparison with state-of-the-art models, which limits the understanding of the model's performance relative to the latest advancements in the field.
- The paper does not include a detailed discussion on the limitations and societal impacts of the model, which is crucial for understanding the model's potential negative consequences.
- The paper does not provide a detailed discussion on the computational resources required for training and inference, which is essential for reproducibility and scalability.
- The paper does not include a detailed discussion on the model's performance on various benchmarks, which is necessary for a comprehensive evaluation of the model's capabilities.
- The paper does not include a detailed discussion on the model's performance on various benchmarks, which is necessary for a comprehensive evaluation of the model's capabilities.
- The paper does not include a detailed discussion on the model's performance on various benchmarks, which is necessary for a comprehensive evaluation of the model's capabilities.

**Questions:**
- Could the authors provide a more detailed comparison with state-of-the-art models to better understand the model's performance relative to the latest advancements in the field?
- Could the authors provide a more detailed discussion on the limitations and societal impacts of the model?
- Could the authors provide a more detailed discussion on the computational resources required for training and inference, including the hardware used and the training and inference time?
- Could the authors provide a more detailed discussion on the model's performance on various benchmarks, including both automatic and human evaluations?
- Could the authors provide a more detailed discussion on how the model's performance varies with different training data, including the impact of different data sources and the effects of data curation strategies?
- Could the authors provide a more detailed discussion on how the model's performance varies with different training data, including the impact of different data sources and the effects of data curation strategies?

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
- Reasons: The paper presents a significant advancement in the field of open-source language models by introducing OLMo-2, which addresses training stability and efficiency issues. The model's performance is evaluated on various benchmarks, showing improvements over previous models. The paper is well-written, clear, and provides detailed insights into the training process, which is beneficial for the community. Despite some limitations such as a lack of thorough comparison with state-of-the-art models and a detailed discussion on the limitations and societal impacts, the paper's contributions are substantial and justify its acceptance. The decision to accept is also supported by the paper's transparency in releasing all training artifacts, which is crucial for reproducibility and further research.