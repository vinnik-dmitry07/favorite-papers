 **Summary:**
The paper introduces a novel approach for aligning large language models (LLMs) with human preferences using an intrinsic geometric reward signal termed "stable rank." This metric is derived from the effective dimensionality of hidden states, which is computed by measuring the ratio of total variance to dominant-direction variance. The stable rank is shown to correlate with semantic coherence, information density, and sensitivity to key reasoning structures, as evidenced by its ability to predict human preference and guide best-of-N decoding. The authors propose using stable rank as a reward signal in reinforcement learning, demonstrating its effectiveness through experiments on various benchmarks. Despite some concerns about the novelty of the stable rank concept and the clarity of its mathematical definitions, the paper is generally well-received for its innovative approach and empirical validation.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a clear motivation and a novel approach to using stable rank as a reward signal for LLM alignment.
- The stable rank metric is a simple yet effective method that can be used as a reward signal for reinforcement learning, and it is shown to correlate with semantic coherence, information density, and sensitivity to key reasoning structures.
- The method is evaluated on various benchmarks, including RewardBench, STEM, and mathematical reasoning tasks, demonstrating its effectiveness in improving reasoning accuracy and guiding best-of-N decoding.
- The paper provides a comprehensive evaluation of the stable rank metric, including its correlation with semantic coherence, information density, and sensitivity to key reasoning structures, which are crucial for LLM alignment.
- The method is shown to be effective in improving reasoning accuracy and guiding best-of-N decoding, outperforming both learned reward models and self-evaluation baselines.

**Weaknesses:**
- The paper lacks a detailed discussion on the limitations of the stable rank metric, such as its sensitivity to the choice of hidden layer and its effectiveness in different contexts like self-evaluation and reward hacking.
- The novelty of the stable rank metric is questionable as it is a well-known concept in matrix theory, and the paper does not sufficiently differentiate its application to LLMs from existing literature.
- The paper does not provide sufficient theoretical justification for the use of stable rank as a reward signal in reinforcement learning, and the mathematical definitions and proofs are not clearly explained.
- The paper does not sufficiently address the computational complexity of the stable rank metric, which could be a barrier for practical implementation.
- There is a lack of discussion on the potential negative societal impacts of the proposed method, which is crucial for understanding the broader implications of the research.

**Questions:**
- Can the authors clarify the novelty of their work in using stable rank as a reward signal for LLM alignment, particularly in relation to existing literature on stable rank in matrix theory?
- How does the stable rank metric perform in different contexts, such as self-evaluation and reward hacking?
- Could the authors provide more detailed theoretical justification for the use of stable rank as a reward signal in reinforcement learning, including a proof or mathematical explanation of its effectiveness?
- How does the stable rank metric compare to other existing metrics like perplexity or IPO in terms of effectiveness and computational complexity?
- Can the authors discuss the potential negative societal impacts of their proposed method and how they plan to address these concerns?

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
- Reasons: The paper presents a novel approach to aligning LLMs with human preferences using an intrinsic geometric reward signal, which is both innovative and well-executed. The stable rank metric, while not entirely novel in concept, is effectively applied to LLMs and demonstrates its utility through various benchmarks. The method's ability to guide best-of-N decoding and improve reasoning accuracy is commendable. Despite some concerns about the novelty and clarity in certain sections, the paper is generally well-received for its technical soundness and potential impact on the field. The decision to accept is supported by the metareview, which highlights the paper's contribution to the ongoing discussion on LLM alignment and its practical implications.