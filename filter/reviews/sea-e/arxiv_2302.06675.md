 **Summary:**
The paper introduces a novel method for automatic discovery of optimization algorithms, specifically focusing on the development of a new optimizer named Lion, which is compared against existing optimizers like Adam and Adafactor across various tasks such as image classification, vision-language contrastive learning, diffusion models, and language modeling. The Lion optimizer is described as a simplified version of AdamW, with a focus on memory efficiency and generalization capabilities. The authors employ a program search approach to discover Lion, utilizing techniques like evolutionary search with warm-start and restart, abstract execution, funnel selection, and program simplification. The paper presents extensive experiments demonstrating Lion's performance across different tasks, showcasing its potential in practical applications.

**Strengths:**
- The paper introduces a novel approach to automatically discovering optimization algorithms, which is a significant contribution to the field of AutoML.
- The proposed Lion algorithm is described as simple, effective, and memory-efficient, with a focus on generalization capabilities.
- The paper is well-written, clear, and easy to follow, with extensive experiments that demonstrate the effectiveness of Lion across various tasks and datasets.
- The methodology includes a comprehensive search space, including a wide range of functions, which allows for the discovery of a variety of optimizers.
- The paper includes a thorough evaluation of the Lion algorithm, comparing it against existing optimizers and demonstrating its superior performance in many cases.
- The program search approach used in the paper is novel and interesting, potentially opening up new avenues for optimization algorithm discovery.

**Weaknesses:**
- The paper lacks a detailed comparison with other optimizers like AdaBelief and RAdam, which could provide a more comprehensive understanding of Lion's performance.
- The paper does not discuss the limitations of the Lion algorithm, which could provide valuable insights into its applicability and potential drawbacks.
- The paper could benefit from a more detailed discussion on the limitations of the search space, particularly how it might impact the discovery of more complex or novel optimizers.
- The evaluation of Lion is limited to a few datasets and tasks, which might not fully demonstrate its generalization capabilities across different domains.
- The paper does not provide a detailed discussion on the limitations of the search process, which could affect the reliability and reproducibility of the results.
- The paper could benefit from a more detailed discussion on the limitations of the program search approach, particularly how it might impact the discovery of more complex or novel optimizers.

**Questions:**
- Could the authors provide a more detailed comparison with other optimizers like AdaBelief and RAdam to better understand Lion's performance in different scenarios?
- How does the Lion algorithm compare to other optimizers in terms of computational efficiency and memory usage, especially in large-scale training scenarios?
- Can the authors discuss the limitations of the Lion algorithm and provide examples or scenarios where it might not perform as well as other optimizers?
- How does the program search approach compare to other methods for optimizer discovery, and what are the advantages and disadvantages of each approach?
- Could the authors provide more details on the search process, particularly how the search space is defined and how the optimization algorithm is encoded as a program?
- How does the Lion algorithm handle different types of neural networks, such as recurrent neural networks (RNNs) or transformers, and how does its performance compare to other optimizers in these scenarios?

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
- Reasons: The paper presents a novel method for automatic discovery of optimization algorithms, which is a significant contribution to the field of AutoML. The proposed Lion optimizer shows promising results across various tasks, demonstrating its effectiveness and generalization capabilities. The paper is well-written, clear, and includes extensive experiments that support the claims made. The reviewers have highlighted the novelty of the approach and the potential impact of the Lion optimizer on practical applications. However, there are suggestions for further comparisons with other optimizers and a more detailed discussion on the limitations of the search space and the Lion algorithm. These suggestions could be addressed in future revisions to strengthen the paper's contribution and impact.