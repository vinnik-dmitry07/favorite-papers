 **Summary:**
The paper investigates whether reinforcement learning (RL) can enhance the compositional reasoning abilities of large language models (LLMs) by training them on a synthetic dataset of string transformations. The study uses a two-stage training process, where the first stage focuses on learning atomic skills via rejection fine-tuning, and the second stage introduces compositional skills through either RL or rejection fine-tuning (RFT). The paper demonstrates that RL can teach new compositional skills, which generalize to unseen compositions and transfer to different tasks, showing that these skills are not merely a re-ranking of existing capabilities. The experiments are conducted on a controlled dataset, which allows for precise control over task complexity and the evaluation of skill acquisition. However, the paper's findings are limited to the specific dataset and do not convincingly demonstrate the generalizability of the results to real-world applications.

**Strengths:**
- The paper addresses a significant and timely question regarding the role of reinforcement learning (RL) in enhancing the compositional reasoning abilities of large language models (LLMs), which is crucial for understanding the capabilities of LLMs in complex problem-solving scenarios.
- The study is well-structured and easy to follow, with clear and concise writing that effectively communicates the research questions and findings.
- The experiments are well-designed, with a focus on controlled tasks that allow for precise control over task complexity and the evaluation of skill acquisition.
- The paper provides a comprehensive analysis of the learning behaviors of widely-used post-training approaches for LLMs, which is valuable for understanding the effectiveness of different training methods.
- The findings challenge the recent view that RL with verifiable rewards (RLVR) merely utilizes reasoning patterns in base models, suggesting that RL can indeed teach new reasoning abilities.
- The paper is well-written, with a clear and concise structure that effectively communicates the research questions and findings.

**Weaknesses:**
- The paper's reliance on a synthetic dataset raises concerns about the generalizability of the findings to real-world applications. The dataset, while useful for controlled experiments, may not fully capture the complexity and nuance of real-world reasoning scenarios where skills are less clearly delineated and compositional structures are more varied.
- The paper's claims about the generalizability of the learned skills are not convincingly supported by the experiments. The experiments primarily focus on the Countdown task, which may not adequately demonstrate the transferability of the skills to other domains.
- The paper's conclusions about the necessity of atomic skills for compositional reasoning are not convincingly supported by the data. The experiments do not clearly demonstrate that the model's performance on the Countdown task is due to the transfer of atomic skills or simply the model's ability to learn new skills from scratch.
- The paper's use of a synthetic dataset and its reliance on a specific training method (RL) may limit the applicability of the findings to other types of models or training methods.
- The paper's claims about the necessity of RL for skill acquisition are not convincingly supported by the data, and the comparison with other methods like RFT is not sufficiently robust to establish the superiority of RL.

**Questions:**
- How do the authors ensure that the skills learned in the synthetic dataset generalize to real-world applications?
- Can the authors provide more evidence or examples to support the claim that the skills learned in the synthetic dataset transfer to other domains?
- How do the authors address the potential confounding factors in the experiments, such as the influence of the model's pre-training on the results?
- Could the authors clarify the role of RL in skill acquisition and how it compares to other methods like RFT?
- How do the authors define and measure the "aha moments" in RL training, and what evidence do they have that these moments are not simply a result of amplifying existing cognitive behaviors present in the base models?
- Can the authors provide more details on the training process, such as the specifics of the RL algorithm used and the training hyperparameters?

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
- Reasons: The paper presents a well-structured and well-executed study that addresses a significant and timely question about the role of reinforcement learning in enhancing the compositional reasoning abilities of large language models. The experiments are well-designed, and the findings are clearly communicated, making a strong case for the potential of RL to teach new skills to LLMs. While the paper's reliance on a synthetic dataset and its limited generalizability are noted as concerns, the overall contribution and the soundness of the methodology support its acceptance. The decision to accept is also influenced by the paper's potential to stimulate further research in this area and its alignment with the conference's focus on innovative and impactful contributions to the field.