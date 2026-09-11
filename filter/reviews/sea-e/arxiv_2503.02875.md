 **Summary:**
The paper introduces Unsupervised Prefix Fine-Tuning (UPFT), a novel method for enhancing the reasoning capabilities of large language models (LLMs) without requiring labeled data or extensive sampling. UPFT leverages the observation of Prefix Self-Consistency, where different solution trajectories share a common initial reasoning phase, to fine-tune models on minimal prefixes. This approach reduces training and inference times significantly, showing competitive performance on reasoning benchmarks. The methodology is supported by extensive experiments that demonstrate the effectiveness of UPFT in improving reasoning capabilities while reducing computational costs.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation and a well-defined problem statement.
- The proposed method is simple, effective, and efficient, with a novel approach to unsupervised fine-tuning that leverages the observation of Prefix Self-Consistency.
- The paper includes comprehensive experiments that demonstrate the effectiveness of the proposed method, showing that it outperforms traditional full-token fine-tuning and achieves performance comparable to supervised approaches like RFT with significantly reduced training and inference times.
- The methodology is supported by a solid theoretical foundation, and the paper provides a detailed explanation of the methodology, including the mathematical derivation of the proposed method.
- The paper includes a detailed analysis of the method's performance, including a comparison with other methods like RFT and V-STaR, and an ablation study on the impact of hyperparameters.

**Weaknesses:**
- The paper lacks a detailed discussion on the limitations of the proposed method, including the potential impact of different prefix lengths and the generalizability of the method to other types of reasoning tasks.
- There is a lack of clarity in the experimental setup, particularly in the description of the datasets used and the details of the experimental setup, which could affect the reproducibility of the results.
- The paper could benefit from a more thorough discussion of related work, especially in the context of unsupervised learning and the comparison with other methods like RFT and V-STaR.
- Some figures and tables in the paper are not clearly explained or labeled, which could confuse readers.
- The paper could benefit from a more detailed discussion of the computational efficiency and memory requirements of the proposed method, especially in comparison to other methods.

**Questions:**
- Can the authors clarify the experimental setup, particularly the datasets used and the details of the experimental conditions?
- How does the proposed method perform on other types of reasoning tasks beyond mathematical reasoning?
- Could the authors provide more details on the computational efficiency and memory requirements of the proposed method, especially in comparison to other methods?
- What are the specific contributions of the proposed method compared to existing methods like RFT and V-STaR?
- How does the proposed method handle the potential for catastrophic forgetting in the reasoning structures of the model?
- Can the authors provide more details on the selection and curation of the U-Hard dataset, particularly how it maximizes the potential of UPFT?
- How does the proposed method compare in terms of computational efficiency and memory requirements to other methods, especially in large-scale applications?

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
- Reasons: The paper presents a novel and effective method for enhancing the reasoning capabilities of large language models without requiring labeled data or extensive sampling. The method leverages the observation of Prefix Self-Consistency to fine-tune models on minimal prefixes, reducing training and inference times significantly. The paper is well-written, clear, and supported by extensive experiments that demonstrate the effectiveness of the proposed method. The methodology is novel, and the paper provides a solid theoretical foundation and a detailed explanation of the methodology. The reviewers have highlighted the paper's contributions and the potential impact of the work, suggesting that it is a significant contribution to the field. The decision to accept is based on the originality, methodological soundness, significance of results, and clarity and logic of presentation.