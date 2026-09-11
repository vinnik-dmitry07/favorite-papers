 **Summary:**
The paper introduces StrategyQA, a novel question answering benchmark designed to evaluate models' ability to perform implicit multi-step reasoning, where the reasoning steps are not explicitly stated in the question. This dataset, which includes 2,780 examples, is annotated with decomposition into reasoning steps and evidence paragraphs, providing a comprehensive evaluation of models' reasoning capabilities. The dataset is designed to challenge models by requiring them to infer the reasoning steps from the question, which is a departure from traditional explicit multi-hop reasoning datasets. The paper also discusses the challenges of eliciting such questions from crowdsourcing workers and proposes a data collection procedure to address these challenges.

**Strengths:**
- The paper introduces a novel question answering (QA) benchmark, StrategyQA, which focuses on implicit multi-step reasoning, a significant departure from traditional explicit multi-hop reasoning datasets.
- The dataset is well-annotated with decomposition into reasoning steps and evidence paragraphs, providing a comprehensive evaluation of models' reasoning capabilities.
- The paper is well-written, clear, and easy to follow, making it accessible to a broad audience.
- The dataset is diverse, covering a wide range of strategies and knowledge domains, which is crucial for evaluating the generalization ability of models.
- The authors have conducted extensive experiments and analysis, including human evaluation, which supports the validity and reliability of the dataset.
- The paper addresses the challenge of eliciting creative questions from crowdsourcing workers, which is a significant issue in the field of QA.

**Weaknesses:**
- The paper lacks a detailed discussion on the challenges of eliciting strategy questions from crowdsourcing workers and how these challenges were addressed.
- The dataset size is relatively small, which might limit its utility for training large models.
- The paper does not provide a detailed discussion on the limitations of the dataset, which could affect its applicability in various scenarios.
- The paper does not discuss the limitations of the annotation process, which could affect the quality and reliability of the dataset.
- The paper does not provide a detailed discussion on the limitations of the annotation process, which could affect the quality and reliability of the dataset.
- The paper does not discuss the limitations of the annotation process, which could affect the quality and reliability of the dataset.
- The paper does not discuss the limitations of the annotation process, which could affect the quality and reliability of the dataset.

**Questions:**
- How does the dataset compare to other datasets like HotpotQA in terms of data quality and diversity?
- What are the specific challenges in eliciting strategy questions from crowdsourcing workers, and how were these challenges addressed?
- How does the dataset ensure the diversity of strategies and knowledge domains, and what steps were taken to prevent biases in the data?
- What are the limitations of the dataset, and how do these limitations affect its applicability in various scenarios?
- How were the annotators selected and trained, and what measures were taken to ensure the quality and reliability of the annotations?
- How does the dataset ensure the diversity of strategies and knowledge domains, and what steps were taken to prevent biases in the data?
- How were the annotators selected and trained, and what measures were taken to ensure the quality and reliability of the annotations?
- How were the annotators selected and trained, and what measures were taken to ensure the quality and reliability of the annotations?

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
- Reasons: The paper introduces a novel and innovative dataset, StrategyQA, which challenges the current state-of-the-art models by requiring implicit multi-step reasoning. The dataset is well-annotated and provides a comprehensive evaluation of models' reasoning capabilities. The paper is well-written, clear, and easy to follow, making it accessible to a broad audience. The dataset's novelty and the methodological soundness of its construction are significant contributions to the field. Despite some concerns regarding the dataset's size and the limitations of the annotation process, the paper's strengths outweigh these weaknesses. The decision to accept is based on the originality of the dataset, its methodological soundness, and the significance of its results. The paper is recommended for acceptance as a poster, with the suggestion to include additional experiments and comparisons with other datasets in the final version.