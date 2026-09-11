 **Summary:**
The paper introduces XBridge, a novel communication protocol for heterogeneous multi-agent large language models (LLMs) that addresses the entity grounding problem in cross-architecture communication. XBridge consists of two mechanisms: Lexical Anchor Mapping (LAM) and Latent Enrichment Bridge (LEB). LAM maps the sender's original context tokens to the receiver's vocabulary, preserving entity identity, while LEB allows the receiver to query the sender's hidden states for contextual enrichment. The protocol is evaluated across three model families and seven benchmarks, showing significant improvements in F1 score and latency compared to text-based communication and same-architecture settings. Despite its strengths, the paper is criticized for its limited evaluation scope, lack of comparison with state-of-the-art methods, and potential issues with the novelty and clarity of its contributions.

**Strengths:**
- The paper addresses a significant and relevant problem in the field of multi-agent systems, focusing on the communication between heterogeneous LLMs, which is crucial for advancing AI applications.
- The proposed XBridge protocol is well-motivated, clearly described, and evaluated on multiple model families and benchmarks, demonstrating its effectiveness in preserving entity identity and reducing latency.
- The paper is well-written, making it easy to follow, and includes detailed experimental results that showcase the effectiveness of the proposed methods.
- The authors provide a comprehensive analysis of the entity grounding problem in heterogeneous LLM communication, which is a novel and significant contribution to the field.
- The paper includes a detailed analysis of the proposed methods, such as the Lexical Anchor Mapping (LAM) and Latent Enrichment Bridge (LEB), which are well-explained and demonstrate their effectiveness through experiments.

**Weaknesses:**
- The paper lacks a thorough comparison with state-of-the-art methods, which could provide a better understanding of the proposed method's relative performance and novelty.
- The evaluation scope is limited to only three model families and seven benchmarks, which might not be sufficient to convincingly demonstrate the generalizability of the proposed methods.
- The paper does not clearly articulate the novelty of the proposed methods, particularly the Latent Enrichment Bridge (LEB), which appears to be a simple cross-attention mechanism.
- The paper does not discuss the limitations of the proposed methods, which could provide a more balanced view of the research.
- The paper's claims about the entity grounding problem and the effectiveness of the proposed methods are not adequately supported by experimental evidence, particularly in scenarios involving different model families.
- The paper's presentation could be improved by better integrating figures and tables into the main text, and by providing more detailed explanations of the experimental setups and results.

**Questions:**
- Could the authors clarify how the entity grounding problem is specifically addressed by the proposed methods, particularly in scenarios involving different model families?
- How does the proposed method compare to other state-of-the-art methods in terms of performance and efficiency?
- Can the authors provide more details on the experimental setup, such as the specifics of the training data and the evaluation metrics used?
- How does the proposed method perform in scenarios involving more than two model families, and what are the implications for the scalability and generalizability of the findings?
- Could the authors elaborate on the novelty of the proposed methods, particularly the Latent Enrichment Bridge (LEB), and how it differs from existing methods?
- How does the proposed method handle scenarios where the sender and receiver models have different architectures, and what are the implications for the effectiveness and applicability of the method?

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
- Reasons: The paper introduces a novel communication protocol, XBridge, which addresses the entity grounding problem in heterogeneous multi-agent LLM systems. The method is well-motivated, clearly described, and evaluated on multiple model families and benchmarks, demonstrating its effectiveness in preserving entity identity and reducing latency. While the evaluation scope is limited, and the paper lacks a thorough comparison with state-of-the-art methods, the novelty and potential impact of the proposed method justify its acceptance, especially considering the significant improvements in F1 score and latency. The decision aligns with the metareview, which highlights the paper's contribution to the field and recommends acceptance, suggesting that the authors address the concerns raised in the reviews in the final version.