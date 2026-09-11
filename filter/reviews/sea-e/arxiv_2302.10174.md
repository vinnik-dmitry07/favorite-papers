 **Summary:**
The paper explores the limitations of existing methods in detecting fake images from unseen generative models, focusing on the asymmetric detection of fake images from GANs versus diffusion models. It proposes a novel approach using a feature space not explicitly trained for real-vs-fake classification, employing nearest neighbor and linear probing methods. The method leverages pre-trained vision-language models like CLIP to demonstrate superior generalization performance across various generative models, including diffusion models. The paper also discusses the limitations of current methods, such as their inability to generalize effectively to unseen generative models, and proposes a new method that could potentially address these issues.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation and a well-structured presentation.
- The authors provide a thorough analysis of the limitations of existing methods and propose a novel approach that addresses these limitations.
- The proposed method is simple yet effective, using a pre-trained vision-language model (CLIP) to extract features, which are then used for nearest neighbor classification and linear probing.
- The paper includes a comprehensive evaluation of the proposed method, comparing it to state-of-the-art baselines and demonstrating its effectiveness in detecting fake images from a variety of generative models.
- The method's generalization performance is robust, as shown in experiments, and it is not sensitive to the choice of hyperparameters.
- The paper is well-organized, with clear explanations of the methodology and results, and includes detailed visualizations and ablation studies that support the claims.

**Weaknesses:**
- The paper lacks a detailed discussion on the limitations of the proposed method, particularly in terms of its generalizability and robustness to different types of generative models and data distributions.
- The paper does not provide a detailed comparison with state-of-the-art methods in terms of computational efficiency and scalability, which could be crucial for practical applications.
- The paper could benefit from a more comprehensive discussion on the societal impact of the proposed method, especially in terms of potential biases and ethical considerations.
- The paper does not sufficiently address the limitations of the baseline methods, which could affect the perceived novelty and effectiveness of the proposed method.
- The paper could benefit from a more detailed discussion on the choice of hyperparameters and their impact on the results.

**Questions:**
- Can the authors provide more details on the computational efficiency and scalability of the proposed method, especially in terms of training and inference times?
- How does the proposed method perform when applied to other types of generative models, such as Variational Autoencoders (VAEs) and normalizing flows?
- Could the authors discuss the potential biases and ethical considerations of the proposed method, particularly in terms of its impact on underrepresented groups and its potential for misuse?
- How does the proposed method handle the issue of overfitting to the training data, especially in scenarios where the training data is limited?
- Can the authors provide more details on the choice of hyperparameters and their impact on the results, particularly in terms of the number of neighbors used in the nearest neighbor classification and the size of the training dataset?
- How does the proposed method perform when applied to different types of data distributions, such as those found in different domains or with different levels of noise or corruption?

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
- Reasons: The paper presents a novel approach to detecting fake images from unseen generative models, which is a significant problem in the field of image forensics. The method, which uses a feature space not explicitly trained for real-vs-fake classification, demonstrates superior generalization performance across various generative models. The paper is well-written, clear, and includes comprehensive evaluations that support the claims made. The reviewers have highlighted the simplicity and effectiveness of the method, along with its potential for practical applications. The decision to accept is based on the originality of the approach, methodological soundness, and the significance of the results. The paper is also commended for its clarity and logic of presentation.