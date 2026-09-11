 **Summary:**
The paper introduces DINOv2, a self-supervised learning method for training Vision Transformer (ViT) models on a large-scale dataset, LVD-142M, which is curated from uncurated images using a self-supervised image retrieval system. This methodology aims to improve upon existing methods like DINO and iBOT by incorporating a KoLeo regularizer and a Sinkhorn-Knopp centering technique. The paper also discusses the training efficiency and the environmental impact of the model, comparing it to other self-supervised learning methods and weakly-supervised models. The results show that DINOv2 can outperform these models on various benchmarks, including image classification, semantic segmentation, and depth estimation. However, the paper has been critiqued for its lack of novelty, insufficient comparison with state-of-the-art methods, and unclear presentation in some sections.

**Strengths:**
- The paper is well-written and easy to follow, with a clear presentation of the methodology and results.
- The proposed method achieves strong performance on various downstream tasks, demonstrating the effectiveness of the self-supervised learning approach.
- The paper provides a comprehensive evaluation of the method, including extensive experiments and ablation studies that support the claims made.
- The use of a large-scale dataset and the incorporation of a KoLeo regularizer and a Sinkhorn-Knopp centering technique are highlighted as significant contributions to the field.
- The paper is the first to report the carbon footprint of training a self-supervised model, which is a valuable contribution to the community.

**Weaknesses:**
- The paper lacks a detailed comparison with state-of-the-art methods, particularly in terms of model architecture and training strategies, which could affect the perceived novelty and effectiveness of the proposed method.
- The paper does not sufficiently discuss the limitations and potential negative societal impacts of the proposed method, which is crucial for understanding the broader implications of the research.
- The presentation of the paper could be improved, particularly in the introduction and some sections where the content is not clearly explained or referenced.
- There are concerns about the fairness and accuracy of the comparisons made with other methods, particularly in the evaluation of different model architectures and training strategies.
- The paper does not adequately address the scalability and generalization of the method to other datasets and tasks, which could limit the practical applicability of the findings.

**Questions:**
- Could the authors clarify the specific contributions of each component of the proposed method, particularly the role of the KoLeo regularizer and the Sinkhorn-Knopp centering technique?
- How does the proposed method compare to other state-of-the-art methods in terms of model architecture and training strategies?
- Can the authors provide more details on the data curation process and the selection criteria for the LVD-142M dataset?
- How does the proposed method perform on other datasets and tasks beyond those evaluated in the paper?
- Could the authors discuss the potential negative societal impacts of the proposed method and how these could be mitigated?
- Can the authors provide more details on the training efficiency and memory usage of the proposed method compared to other methods?
- How does the proposed method handle the issue of overfitting, especially in large-scale datasets?

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
- Reasons: The paper presents a novel approach to self-supervised learning that demonstrates strong performance on various benchmarks, showing the potential of this method in training large-scale models. While there are concerns about the novelty and the depth of comparisons with state-of-the-art methods, the paper is technically sound and provides valuable insights into the training efficiency and environmental impact of large-scale models. The decision to accept is based on the overall positive reception of the method's performance and the potential for further research in this area. However, the paper could benefit from a more detailed discussion on the limitations and societal impacts of the proposed method, as well as a broader comparison with other methods to solidify its position in the field.