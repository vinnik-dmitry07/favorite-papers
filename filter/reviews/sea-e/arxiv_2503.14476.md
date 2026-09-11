 **Summary:**
The paper introduces DAPO, a novel reinforcement learning algorithm designed for large language models (LLMs) specifically tailored for the AIME dataset. DAPO integrates several modifications to GRPO, including a token-level policy gradient loss, dynamic sampling, and overlong reward shaping, aiming to address issues like entropy collapse and reward noise. The algorithm's effectiveness is demonstrated through experiments on AIME, showing improvements over existing methods. The paper is notable for its open-source nature, providing access to the code and datasets, which is crucial for reproducibility and further research in the field.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation and a well-structured presentation.
- The proposed algorithm, DAPO, is a novel approach that addresses key issues in large-scale LLM RL, such as entropy collapse and reward noise, through innovative techniques like dynamic sampling and token-level policy gradient loss.
- The paper provides a detailed analysis of the training dynamics and includes a comprehensive set of experiments that demonstrate the effectiveness of the proposed methods.
- The open-source nature of the paper, including the release of the training code and dataset, enhances reproducibility and supports future research in the field.
- The paper includes a thorough discussion of the training dynamics, which is crucial for understanding the complexities of training large language models using reinforcement learning.

**Weaknesses:**
- The paper primarily focuses on the AIME dataset, which limits the generalizability of the findings to other datasets or tasks.
- The paper lacks a comprehensive discussion on the limitations of the proposed methods and does not provide a detailed comparison with other state-of-the-art methods, which could undermine the claims of superiority.
- The paper does not sufficiently discuss the computational complexity or the scalability of the proposed methods, which are crucial for understanding their applicability in real-world scenarios.
- The paper does not provide a detailed analysis of the failure cases or the societal impact of the proposed methods, which are essential for a comprehensive understanding of the technology's implications.
- The paper could benefit from a more detailed discussion on the hyperparameter settings and their impact on the results, as well as a more rigorous experimental validation to support the claims made.

**Questions:**
- Could the authors provide more details on the computational complexity and scalability of the proposed methods, especially in terms of their applicability to larger or more complex datasets?
- How do the authors ensure the generalizability of their findings beyond the AIME dataset, and what steps have been taken to validate the effectiveness of the proposed methods on other datasets or tasks?
- Can the authors provide a more detailed comparison with other state-of-the-art methods, including a discussion on the specific advantages and disadvantages of each approach?
- How do the authors address the issue of overfitting, especially given the observations of little correlation between final reward on the training set and accuracy on the validation set?
- Could the authors provide more details on the hyperparameter settings used in the experiments and their impact on the results?
- What are the failure cases or scenarios where the proposed methods might not be effective, and how do the authors plan to address these issues in future research?

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
- Reasons: The paper introduces a novel reinforcement learning algorithm, DAPO, which addresses key issues in large language model training, particularly on the AIME dataset. The methodology is well-explained, and the paper is well-written, making it accessible and understandable. The open-source nature of the paper, including the release of the training code and dataset, is a significant contribution to the field, enhancing reproducibility and supporting future research. Despite some concerns regarding the generalizability of the findings and the need for more comprehensive comparisons with other methods, the paper's contributions are substantial and warrant acceptance, especially considering the potential impact on the field.