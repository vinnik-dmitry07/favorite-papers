 **Summary:**
The paper investigates the "Reversal Curse" phenomenon in large language models (LLMs), where models trained on statements of the form "A is B" do not generalize to the reverse form "B is A" without in-context examples. The authors demonstrate this through experiments using GPT-3 and Llama-1, showing that models struggle to answer questions where the order of entities is reversed. The paper also discusses potential explanations for this behavior, including the order of data presentation and the model's inability to learn bidirectional associations. Despite the novelty of the observation, the paper is criticized for its limited scope, lack of comprehensive experiments, and potential overclaiming of the "curse" phenomenon.

**Strengths:**
- The paper is well-written, with clear and concise language that effectively communicates the main ideas and findings.
- The observation of the "Reversal Curse" is novel and interesting, providing a significant contribution to the understanding of large language models (LLMs).
- The experiments are well-designed, with clear motivations and detailed explanations, which help to support the claims made.
- The paper includes a thorough discussion of related work, which contextualizes the findings within the existing literature.
- The authors have conducted a comprehensive set of experiments, including finetuning and testing with different model sizes and families, which demonstrates a rigorous approach to validation.
- The paper is well-organized, with a clear structure and logical flow, which aids in understanding the content.

**Weaknesses:**
- The paper lacks a comprehensive evaluation of the "Reversal Curse" phenomenon, particularly in terms of its generalizability to other types of statements and its impact on different model architectures and training methods.
- The experiments are limited in scope, focusing primarily on fictitious statements and not sufficiently exploring the effects of training data order or the use of in-context learning.
- The paper overclaims the "curse" phenomenon, potentially misleading readers about the scope and implications of the findings.
- There is a lack of discussion on the potential societal impacts of the findings, which could be a significant limitation for practical applications.
- The paper does not sufficiently address the potential biases in the training data, which could influence the results and the generalizability of the findings.
- The paper could benefit from a more detailed discussion on the limitations of the experiments and the potential implications of the findings for different types of LLMs and training methods.

**Questions:**
- Could the authors clarify the specifics of the experiments, particularly the number of seeds used and the statistical significance of the results?
- How does the "Reversal Curse" phenomenon manifest in different types of statements, such as those involving logical implications, spatial relationships, or n-place relations?
- What are the implications of the findings for the development and deployment of LLMs in practical applications?
- How does the "Reversal Curse" phenomenon relate to other biases in LLMs, such as those related to gender, race, or other demographic factors?
- Could the authors provide more details on the experimental setup, including the specifics of the training data and the model configurations used?
- How might the findings be applied to improve the training and deployment of LLMs, particularly in terms of mitigating the "Reversal Curse" phenomenon?

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
- Reasons: The paper presents a novel and intriguing observation about the "Reversal Curse" in LLMs, which is supported by well-designed experiments. The observation is significant and contributes to the understanding of LLM behavior. However, the paper is criticized for its limited scope and potential overclaiming of the "curse" phenomenon. Despite these limitations, the paper is considered a valuable contribution to the field, and its findings could inform future research and development in LLM training. The decision to accept is based on the novelty of the observation, the rigor of the experiments, and the potential impact on the field, despite the noted limitations.