 **Summary:**
The paper introduces Elastic Looped Transformers (ELT), a novel architecture that integrates a parameter-efficient looped transformer with a distillation mechanism to enhance the efficiency of visual generation models. ELT allows for dynamic adjustment of the number of loops during inference, enabling adaptability to different computational environments. The authors propose a training method called Intra-Loop Self Distillation (ILSD) to ensure consistency across different loop depths. ELT is evaluated on both image and video generation tasks, showing competitive results with fewer parameters and improved efficiency. The paper also discusses the potential of ELT in reducing computational costs and improving the efficiency of generative models.

**Strengths:**
- The proposed method is straightforward and easy to understand, with a clear and well-written paper that effectively communicates the ideas.
- The paper introduces a novel approach to looped transformers, which is a significant contribution to the field of visual generation.
- The methodology is well-motivated and well-supported by experiments, demonstrating the effectiveness of the proposed method.
- The paper is well-organized and provides comprehensive experiments, including both image and video generation tasks, showcasing the versatility of the proposed method.
- The use of intra-loop self-distillation is innovative, allowing for the training of models that can be dynamically scaled during inference, which is a significant advantage over traditional models.
- The paper addresses an important problem in the field of generative models, focusing on reducing computational costs while maintaining or improving performance, which is a significant challenge in the community.

**Weaknesses:**
- The paper lacks a detailed comparison with other parameter-efficient methods, which could have strengthened the argument for the superiority of the proposed method.
- The experiments are limited to specific datasets and resolutions, which may not fully demonstrate the generalizability of the method.
- The paper does not provide sufficient details on the training process, particularly the computational overhead and the specifics of the training algorithms.
- The paper does not discuss the limitations of the proposed method, which could help in understanding its applicability and potential challenges.
- The paper does not include a discussion on the limitations of the proposed method, which could help in understanding its applicability and potential challenges.
- The paper could benefit from a more detailed discussion on the scalability of the method, especially in terms of the number of loops and their impact on performance.

**Questions:**
- Can the authors provide more details on the training process, including the computational overhead and the specifics of the training algorithms?
- How does the proposed method compare to other parameter-efficient methods, particularly in terms of performance and efficiency?
- Could the authors provide more examples of the generated images and videos to better demonstrate the capabilities of the proposed method?
- How does the proposed method perform on larger datasets or at higher resolutions?
- Can the authors discuss the limitations of the proposed method and provide insights into potential future research directions?
- How does the proposed method perform in terms of training time and memory requirements compared to other methods?
- Can the authors provide more details on the scalability of the method, particularly in terms of the number of loops and their impact on performance?

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
- Reasons: The paper presents a novel and promising approach to looped transformers, which is well-received by the reviewers for its simplicity, effectiveness, and potential for reducing computational costs in generative models. The method's ability to dynamically adjust the number of loops during inference is particularly noteworthy, as it allows for adaptability to different computational environments. The paper is well-written, clearly communicating the ideas and results, and includes comprehensive experiments that demonstrate the method's effectiveness. The reviewers suggest that the paper could benefit from more detailed comparisons with other parameter-efficient methods and a broader range of experiments to fully demonstrate the method's capabilities. However, these are minor issues that do not detract from the paper's overall strength and contribution to the field. The decision to accept is based on the paper's originality, methodological soundness, and the significance of its results, as well as the clarity and logic of its presentation.