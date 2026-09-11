 **Summary:**
The paper introduces SwAV, a novel unsupervised learning method for visual feature extraction that leverages a contrastive learning approach without requiring pairwise feature comparisons. It utilizes a clustering-based method to assign codes to different views of the same image, thereby improving the scalability and efficiency of contrastive learning. The method also introduces a multi-crop strategy that uses low-resolution crops to augment views without increasing computational overhead. SwAV has been validated on ImageNet, achieving state-of-the-art results and outperforming supervised pretraining on various downstream tasks. The paper also discusses the potential of SwAV in large-scale pretraining scenarios and its application to other datasets.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation and a novel approach to contrastive learning that does not require pairwise comparisons.
- The proposed method, SwAV, is innovative in its use of clustering-based self-supervised learning, which is shown to be effective in improving performance over existing methods like SimCLR and DeepCluster.
- The paper includes comprehensive experiments that demonstrate the effectiveness of SwAV, particularly in large-scale pretraining scenarios, and shows that it outperforms supervised pretraining on various downstream tasks.
- The introduction of a multi-crop strategy is a significant contribution, enhancing the method's applicability and performance across different datasets and architectures.
- The paper provides a thorough analysis of the method's performance under different conditions, such as varying batch sizes and training epochs, which helps in understanding the method's robustness and scalability.

**Weaknesses:**
- The paper lacks a detailed discussion on the computational efficiency of SwAV compared to other methods like SimCLR, particularly in terms of memory and computational requirements.
- The experimental results are not sufficiently compared with other recent methods, such as MoCoV2 and other clustering-based methods, which could provide a clearer picture of SwAV's performance relative to the state-of-the-art.
- The paper does not adequately address the scalability of SwAV to larger datasets or architectures, which could be crucial for its practical application in real-world scenarios.
- There is a lack of discussion on the limitations of the proposed method, particularly in terms of its applicability to different datasets and its potential impact on model performance.
- The paper does not include a detailed comparison of the computational overhead of the multi-crop strategy, which could be a significant factor in its practical implementation.

**Questions:**
- Could you provide a more detailed comparison of the computational efficiency of SwAV with other methods like SimCLR, particularly in terms of memory and computational requirements?
- How does SwAV perform when applied to other datasets beyond ImageNet, and what are the implications for its performance and scalability in these contexts?
- Could you elaborate on the scalability of SwAV to larger datasets and architectures, and discuss any potential challenges or limitations in this regard?
- How does the multi-crop strategy affect the computational overhead and the model's performance, particularly in terms of the number of crops used and their resolution?
- Could you provide more details on the training parameters, such as the number of epochs and the batch size used in the experiments, to better understand the method's performance under different conditions?

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
- Reasons: The paper presents a novel and effective approach to unsupervised learning of visual features, which is both scalable and efficient. The methodology is well-explained, and the results are convincing, showing that SwAV outperforms existing methods on various benchmarks. The introduction of the multi-crop strategy is a significant contribution that enhances the method's applicability and performance. The paper is well-written, making it accessible and easy to understand. The reviewers have highlighted the need for more detailed comparisons and discussions on the limitations and scalability of the method, which could be addressed in future work. Overall, the paper is a solid contribution to the field of unsupervised learning and is recommended for acceptance.