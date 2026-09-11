 **Summary:**
The paper introduces DeepSeekMath, a pre-trained model for mathematical reasoning, leveraging a large-scale corpus of 120B math tokens sourced from Common Crawl. The model is trained using a variant of Proximal Policy Optimization (PPO) named Group Relative Policy Optimization (GRPO), which optimizes memory usage and mathematical reasoning capabilities. The model is evaluated on various benchmarks, including GSM8K, MATH, and MMLU, demonstrating strong performance. The paper also discusses the effectiveness of different training methods such as supervised fine-tuning, reinforcement learning, and instruction tuning, and provides insights into the impact of different data sources on model performance.

**Strengths:**
- The paper introduces a large-scale corpus of 120B math tokens, which is a significant contribution to the field.
- The model, DeepSeekMath, is evaluated on multiple benchmarks and demonstrates strong performance, outperforming existing models in some cases.
- The paper provides a detailed analysis of different training methods, including supervised fine-tuning, reinforcement learning, and instruction tuning, and discusses the impact of different data sources on model performance.
- The use of Group Relative Policy Optimization (GRPO) is highlighted as a novel approach that enhances mathematical reasoning capabilities while optimizing memory usage.
- The paper is well-written, easy to follow, and provides a comprehensive evaluation of the model's performance across various benchmarks.

**Weaknesses:**
- The paper lacks a detailed discussion on the limitations of the model, particularly in terms of its performance on geometry and theorem-proof tasks.
- There is a lack of clarity in the presentation of results, particularly in tables and figures, which could benefit from better organization and clearer labeling.
- The paper does not sufficiently address the generalization ability of the model, especially in out-of-distribution scenarios.
- The paper does not provide a detailed comparison with other models, such as GPT-4, which could help in understanding the model's relative performance.
- The paper could benefit from a more detailed discussion on the data selection process and the potential biases introduced by the data collection pipeline.
- The paper does not sufficiently address the potential societal impacts of the model, which is a significant omission in the discussion section.

**Questions:**
- Can the authors clarify the performance of the model on geometry and theorem-proof tasks, and discuss potential reasons for its weaker performance in these areas?
- How does the model perform when trained on a mixture of code and math tokens? Could the authors provide more details on the specific training settings used in this scenario?
- Could the authors provide more details on the data selection process, particularly how the model was trained on a mixture of code and math tokens?
- In the context of the GRPO algorithm, how does the model handle the gradient coefficient adjustment based on the reward value provided by the reward model?
- How does the model perform on out-of-distribution scenarios, and what measures have been taken to address the potential for overfitting to the training data?
- Could the authors provide more details on the computational resources required for training the model, including the hardware used and the training time?
- How does the model handle the potential for data contamination from benchmarks, and what steps were taken to mitigate this risk?

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
- Reasons: The paper presents a novel approach to mathematical reasoning using a large-scale corpus and a variant of PPO, GRPO, which optimizes memory usage and mathematical reasoning capabilities. The model is evaluated on various benchmarks and demonstrates strong performance, outperforming existing models in some cases. The paper is well-written, easy to follow, and provides a comprehensive evaluation of the model's performance. The introduction of a large-scale corpus of 120B math tokens is a significant contribution to the field. However, the paper could benefit from a more detailed discussion on the limitations of the model, particularly in terms of its performance on geometry and theorem-proof tasks. The presentation of results could also be improved for better clarity and organization. Despite these limitations, the paper is accepted for presentation as a poster to allow for further discussion and feedback on these areas.