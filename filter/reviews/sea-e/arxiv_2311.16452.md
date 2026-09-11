 **Summary:**
The paper explores the application of prompt engineering techniques to enhance the performance of GPT-4 on medical question-answering tasks, specifically focusing on the MultiMedQA benchmark. It introduces a method called MedPrompt, which includes dynamic few-shot selection, self-generated chain of thought, and choice shuffling ensemble. The authors demonstrate that this method outperforms existing specialist models and achieves state-of-the-art results on nine medical benchmark datasets. The paper also discusses the generalization of these techniques to other domains and the potential for broader applicability in various fields. However, concerns are raised about the novelty of the method, the lack of detailed analysis on the effectiveness of each component, and the potential for overfitting due to the use of a closed-source model.

**Strengths:**
- The paper is well-written, clearly presenting the motivation, methodology, and results, making it easy to follow and understand.
- The proposed prompting strategy, MedPrompt, is novel and innovative, combining dynamic few-shot selection, self-generated chain of thought, and choice shuffling ensemble, which can be applied to other domains beyond medicine.
- The experiments are comprehensive, including ablation studies that demonstrate the effectiveness of each component of MedPrompt, and the results show that MedPrompt outperforms existing specialist models on medical question-answering tasks.
- The paper discusses the limitations and potential negative societal impacts of the proposed method, which is commendable for its transparency and ethical considerations.
- The methodology is generalizable, as demonstrated by its application to other domains such as nursing and law, showing potential for broader applicability.

**Weaknesses:**
- The paper lacks a detailed analysis of the effectiveness of each component of MedPrompt, particularly the choice of parameters and the impact of different configurations on performance.
- There is a concern about the novelty of the method, as similar techniques have been previously used in other studies, and the paper does not sufficiently differentiate its approach.
- The paper does not provide sufficient details on the implementation of the method, such as the specifics of the prompting strategies and the selection of few-shot examples, which could affect the reproducibility and understanding of the results.
- The use of a closed-source model, GPT-4, raises concerns about the reproducibility and transparency of the results, as the methodology cannot be fully verified or replicated by other researchers.
- The paper does not adequately address the potential for overfitting due to the use of a closed-source model, which could limit the generalizability of the findings.

**Questions:**
- Could you provide more details on the implementation of the MedPrompt method, particularly how the few-shot examples are selected and how the chain of thought is generated?
- How do you ensure that the results are not overfitting to the specifics of the GPT-4 model, and what steps have been taken to validate the generalizability of the findings?
- In the ablation studies, could you clarify the order of introducing each component and the impact of each component on the performance?
- How do you address the potential for overfitting in your methodology, especially given the use of a closed-source model?
- Can you provide more details on the training and testing data used in your experiments, and how you ensure that the model is not overfitting to specific examples or datasets?

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
- Reasons: The paper presents a novel approach to prompt engineering that effectively leverages GPT-4's capabilities to outperform specialist models on medical question-answering tasks. The methodology, while not entirely novel, is well-executed and demonstrates a significant improvement over existing methods. The paper is well-written, making it accessible and understandable, and the results are convincing, showing a clear advantage over state-of-the-art models. However, concerns about the novelty and the potential for overfitting due to the use of a closed-source model are noted. These issues do not significantly detract from the overall strength of the paper, which justifies its acceptance as a poster presentation.