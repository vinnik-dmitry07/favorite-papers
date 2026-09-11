 **Summary:**
The paper introduces a novel approach to generative modeling called Explorative Modeling (XM), which factors the training loop to explore multiple modes of generation. This method is designed to enhance the expressivity of generative models by allowing them to capture multiple modes of the data distribution, which is a significant departure from traditional methods that typically focus on a single mode. The authors demonstrate that this approach can lead to improved performance in various tasks such as image generation, video generation, and language modeling, showing that it can be integrated with existing generative models like diffusion and flow models. The paper also explores the potential of XM in end-to-end training scenarios, suggesting that it could lead to more efficient and effective training processes.

**Strengths:**
- The paper introduces a novel approach to generative modeling that factors the training loop, which is a significant departure from traditional methods that factorize generation.
- The proposed method, Explorative Modeling (XM), is shown to improve performance in various tasks such as image generation, video generation, and language modeling.
- The paper is well-written, clear, and easy to follow, with a clear motivation and a well-structured presentation of the method and results.
- The method is simple yet effective, with a clear explanation of the intuition behind it and a detailed discussion of its potential applications and limitations.
- The paper includes a comprehensive set of experiments that demonstrate the effectiveness of the proposed method across different modalities, including images, videos, and language.
- The authors provide a detailed analysis of the computational and memory costs associated with the proposed method, which is crucial for understanding its practical implications.

**Weaknesses:**
- The paper lacks a detailed comparison with existing methods, particularly in terms of computational efficiency and the number of modes captured.
- The paper does not provide a detailed discussion on the limitations of the proposed method, which could help in understanding its applicability and potential drawbacks.
- The paper does not include a detailed discussion on the scalability of the method, which is crucial for understanding its applicability in large-scale generative models.
- The paper does not provide a detailed discussion on the training costs associated with the proposed method, which could be a significant concern for practical applications.
- The paper does not include a detailed discussion on the potential negative societal impacts of the proposed method, which is an important consideration for any new technology.
- The paper does not include a detailed discussion on the limitations of the proposed method, which could help in understanding its applicability and potential drawbacks.

**Questions:**
- Can the authors provide a more detailed comparison with existing methods, particularly in terms of computational efficiency and the number of modes captured?
- How does the proposed method compare to other methods that aim to improve the expressivity of generative models, such as those that use different training objectives or different model architectures?
- Can the authors provide a more detailed discussion on the limitations of the proposed method, particularly in terms of its applicability and potential drawbacks?
- How does the proposed method scale with the size of the dataset and the complexity of the model?
- Can the authors provide more details on the training costs associated with the proposed method, particularly in terms of computational resources and time?
- Can the authors provide more details on the potential negative societal impacts of the proposed method, and how these impacts might be mitigated?

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
- Reasons: The paper introduces a novel approach to generative modeling that addresses a significant limitation of existing methods by allowing for the capture of multiple modes of the data distribution. The method is shown to be effective in various tasks and can be integrated with existing generative models, making it a valuable contribution to the field. The reviewers have highlighted the paper's clarity, originality, and the potential impact of the proposed method. However, there are concerns about the scalability of the method and the need for a more detailed discussion on the limitations and negative societal impacts. These issues are noted as areas for future work, but do not detract from the overall positive assessment of the paper. The decision to accept is based on the paper's technical soundness, potential impact, and the positive reception by the reviewers.