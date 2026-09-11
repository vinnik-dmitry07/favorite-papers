 **Summary:**
The paper introduces PromptBreeder, a novel method for automatically generating effective task prompts for large language models (LLMs) using an evolutionary algorithm. The approach involves generating a population of task prompts and mutating them using a set of mutation prompts, which are also evolved. The fitness of each prompt is evaluated using a subset of the training data, and the fittest prompts are selected for the next generation. The process is repeated over multiple generations, leading to the evolution of increasingly effective prompts. The method is tested on various datasets, showing improvements over existing prompting strategies like Chain-of-Thought and Plan-and-Solve. However, the paper is criticized for its lack of clarity in explaining the evolutionary process and the absence of a detailed comparison with other prompting methods.

**Strengths:**
- The paper introduces a novel approach to prompt engineering by using an evolutionary algorithm to generate task prompts, which is a significant advancement in the field.
- The method is well-motivated and effectively demonstrates its effectiveness through experiments on various datasets, showing improvements over existing methods.
- The use of LLMs as a mutation operator is innovative and provides a new perspective on prompt evolution.
- The paper is well-written, making it accessible and easy to understand, with clear explanations of the methodology and results.
- The inclusion of a wide range of mutation operators and the use of a binary tournament selection process add depth and robustness to the method.

**Weaknesses:**
- The paper lacks a detailed explanation of the evolutionary process, particularly how the mutation prompts are generated and how they influence the evolution of task prompts.
- There is a lack of comparison with other prompting methods, which makes it difficult to assess the relative effectiveness of the proposed method.
- The paper does not sufficiently address the issue of overfitting, which is a significant concern given the potential for the method to generate prompts that are overly specific to the training data.
- The method's reliance on LLMs for generating prompts raises concerns about the potential for the method to simply replicate existing biases or limitations of the LLMs.
- The paper could benefit from a more detailed analysis of the generated prompts and the evolutionary process, including the impact of different mutation operators and the diversity of the generated prompts.

**Questions:**
- Could you provide more details on how the mutation prompts are generated and how they influence the evolution of task prompts?
- How does the method avoid overfitting, especially given the potential for the generated prompts to be overly specific to the training data?
- Can you clarify the role of the LLM in the evolutionary process and how it influences the generation of prompts?
- How does the method compare to other prompting methods, especially in terms of performance and efficiency?
- Could you provide more examples or case studies of the generated prompts to better understand their quality and diversity?
- What are the implications of using different LLMs for the evolutionary process, and how does this affect the generated prompts and their effectiveness?

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
- Reasons: The paper introduces a novel method for prompt engineering using an evolutionary algorithm, which is a significant contribution to the field. The method shows promise in generating effective prompts for LLMs, as demonstrated by its performance on various datasets. However, the paper could benefit from more detailed explanations of the evolutionary process and a more rigorous comparison with other prompting methods. The decision to accept is based on the novelty of the approach, the method's effectiveness, and the potential for further development and refinement of the method. The decision aligns with the reviewers' recommendations, who suggest that the paper's strengths outweigh its weaknesses, and that the method's potential for future research justifies its acceptance.