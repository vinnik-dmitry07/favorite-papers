 **Summary:**
The paper introduces LiveMathematicianBench, a novel benchmark designed to evaluate the mathematical reasoning capabilities of large language models (LLMs) using theorem statements from recently published arXiv papers. The benchmark is structured around a taxonomy of 13 problem categories, each with specific question generation methods to ensure the questions are not easily solved by surface-level matching. The evaluation process includes a proof-sketch-guided distractor generation pipeline to enhance the benchmark's sensitivity to genuine mathematical understanding. The benchmark is evaluated using state-of-the-art models, showing that even the best models struggle with the questions, highlighting the need for more advanced mathematical reasoning capabilities in LLMs.

**Strengths:**
- The paper introduces a novel benchmark, LiveMathematicianBench, which is designed to evaluate mathematical reasoning capabilities of large language models (LLMs) using theorem statements from recently published arXiv papers.
- The benchmark is structured around a taxonomy of 13 problem categories, each with specific question generation methods, which ensures that the questions are not easily solved by surface-level matching.
- The paper proposes a proof-sketch-guided distractor generation pipeline, which enhances the benchmark's sensitivity to genuine mathematical understanding rather than surface-level answer matching.
- The benchmark is evaluated using state-of-the-art models, showing that even the best models struggle with the questions, highlighting the need for more advanced mathematical reasoning capabilities in LLMs.
- The paper is well-written, making it easy to follow, and the evaluation process is transparent, with detailed explanations of the benchmark construction and evaluation protocols.
- The benchmark is designed to be contamination-resistant, which is crucial for evaluating the mathematical reasoning capabilities of LLMs in a realistic and unbiased manner.

**Weaknesses:**
- The paper lacks a detailed discussion on the limitations of the benchmark, which could help in understanding the scope and applicability of the results.
- The paper does not provide a detailed discussion on the limitations of the LLM-based extractor used in the benchmark, which could affect the quality and reliability of the extracted theorems.
- The paper does not discuss the potential societal impacts of the benchmark, which is an important consideration for any new technology.
- The paper does not provide a detailed discussion on the limitations of the LLM-based classifier used in the benchmark, which could affect the accuracy and reliability of the logical taxonomy of theorems.
- The paper does not discuss the potential limitations of the proof-sketch-guided distractor generation pipeline, which could affect the validity and reliability of the distractors generated.
- The paper does not discuss the potential limitations of the substitution-resistant evaluation mechanism, which could affect the validity and reliability of the results.
- The paper does not discuss the potential limitations of the dual-mode protocol used in the benchmark, which could affect the validity and reliability of the results.
- The paper does not discuss the potential limitations of the methodology used in the benchmark, which could affect the validity and reliability of the results.

**Questions:**
- Could the authors provide more details on the limitations of the benchmark and how they plan to address these limitations in future work?
- How does the benchmark handle the potential for contamination from pre-training corpora, especially in the context of the arXiv papers used in the benchmark?
- Could the authors provide more details on the limitations of the LLM-based extractor and how they ensure the quality and reliability of the extracted theorems?
- Could the authors provide more details on the limitations of the LLM-based classifier and how they ensure the accuracy and reliability of the logical taxonomy of theorems?
- Could the authors provide more details on the limitations of the proof-sketch-guided distractor generation pipeline and how they ensure the validity and reliability of the distractors generated?
- Could the authors provide more details on the limitations of the substitution-resistant evaluation mechanism and how they ensure the validity and reliability of the results?
- Could the authors provide more details on the limitations of the dual-mode protocol and how they ensure the validity and reliability of the results?
- Could the authors provide more details on the limitations of the methodology used in the benchmark and how they ensure the validity and reliability of the results?

**Soundness:**
3 good

**Presentation:**
3 good

**Contribution:**
3 good

**Rating:**
8 accept, good paper

**Paper Decision:**
- Decision: Accept
- Reasons: The paper presents a significant contribution to the field by introducing a novel benchmark, LiveMathematicianBench, which effectively evaluates the mathematical reasoning capabilities of LLMs using theorem statements from recently published arXiv papers. The benchmark's structure, which includes a taxonomy of 13 problem categories and a proof-sketch-guided distractor generation pipeline, makes it a valuable tool for assessing the genuine mathematical understanding of LLMs. The paper is well-written, making it easy to follow, and the evaluation process is transparent, which enhances the credibility of the results. The benchmark's potential for real-world applications in scientific workflows and its ability to challenge the current state-of-the-art models make it a valuable contribution to the field. However, the paper could benefit from a more detailed discussion on the limitations of the benchmark and the potential societal impacts of the work. Despite these limitations, the paper's strengths outweigh its weaknesses, making it a good fit for acceptance, particularly as a poster presentation at the conference.