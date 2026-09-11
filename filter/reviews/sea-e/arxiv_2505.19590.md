 **Summary:**
The paper introduces Intuitor, a novel method for training large language models (LLMs) using Reinforcement Learning from Internal Feedback (RLIF), which utilizes a model's own confidence, termed self-certainty, as the sole reward signal. This approach is contrasted with traditional methods that rely on external rewards or labeled data. The method is evaluated on various benchmarks, including mathematical reasoning, code generation, and instruction following, demonstrating competitive performance with supervised RLVR methods and better generalization to out-of-domain tasks. The paper also discusses the potential of RLIF in enabling autonomous AI systems and improving reasoning capabilities without external supervision.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation and a well-defined methodology.
- The proposed method, Intuitor, is innovative and effective, as demonstrated by its ability to match supervised RL performance on in-domain tasks and achieve competitive, sometimes better out-of-domain generalization.
- The paper is well-structured, with a clear introduction, related work, and methodology sections, and the experiments are well-designed and well-executed.
- The use of self-certainty as an intrinsic reward signal is a novel and interesting approach, which has shown promising results in various tasks.
- The paper provides a comprehensive evaluation, including ablation studies, and the results are convincing, demonstrating the effectiveness of the proposed method.

**Weaknesses:**
- The paper lacks a detailed discussion on the limitations of the proposed method, particularly in terms of its scalability and generalization to more complex tasks.
- The paper does not sufficiently differentiate its method from existing works, such as those by Kang et al. (2025), which also use self-certainty as a reward signal.
- The experimental setup is somewhat limited, with only a few models and datasets used, which might not fully demonstrate the generalizability of the method.
- The paper could benefit from a more thorough discussion on the theoretical underpinnings of the self-certainty reward signal and its effectiveness in different contexts.
- There is a lack of clarity in some sections of the paper, particularly in the explanation of certain terms and equations, which could confuse readers.

**Questions:**
- Can the authors clarify the differences between their method and the one proposed by Kang et al. (2025)?
- How does the proposed method perform on more complex tasks, such as those involving more intricate reasoning or natural language understanding?
- Could the authors provide more details on the experimental setup, particularly the choice of models and datasets, and the rationale behind these choices?
- Is there a possibility to include more diverse models and datasets in future experiments to validate the generalizability of the method?
- Can the authors elaborate on the theoretical underpinnings of the self-certainty reward signal and its effectiveness in different contexts?
- How does the method handle the potential for overconfidence in the model's predictions, and what measures are in place to prevent this?

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
- Reasons: The paper presents a novel method, Intuitor, which effectively utilizes self-certainty as an intrinsic reward signal for training LLMs, demonstrating competitive performance on various benchmarks. The method is well-explained, and the paper is well-written, making it accessible and understandable. The experimental results are convincing, showing the method's effectiveness in both in-domain and out-of-domain tasks. Despite some concerns about the novelty and the scope of the experiments, the paper's contributions are significant and warrant acceptance, especially considering the potential impact on the field of LLM training. The decision aligns with the reviewers' consensus and the metareview, which highlights the paper's strengths and the potential for further research in this area.