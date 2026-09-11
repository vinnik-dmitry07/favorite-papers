 **Summary:**
The paper introduces a novel approach to learning rate scheduling, termed "cyclical learning rates," which varies the learning rate between predefined bounds, typically between a small and a larger value. This method is demonstrated to be effective across various architectures and datasets, including CIFAR-10, CIFAR-100, and ImageNet, showing improved performance over fixed learning rates. The authors propose a method to estimate these bounds using a small number of training epochs, which simplifies the process of hyperparameter tuning. Despite its practical utility and the empirical evidence provided, the paper lacks a theoretical analysis and a broader range of experiments to fully substantiate its claims.

**Strengths:**
- The paper introduces a novel approach to learning rate scheduling that is simple, effective, and practical, requiring minimal computational overhead.
- The method is demonstrated to be effective across various architectures and datasets, showing improved performance over fixed learning rates.
- The paper is well-written, easy to follow, and provides a clear explanation of the method and its implementation.
- The method is simple to implement and can be easily combined with other learning rate schedules, offering a flexible approach to optimizing neural network training.
- The paper includes a comprehensive set of experiments that demonstrate the effectiveness of the proposed method across different architectures and datasets.

**Weaknesses:**
- The paper lacks a theoretical analysis of why the proposed method works, which could strengthen the paper's claims and provide a deeper understanding of its effectiveness.
- The experiments are limited to a few datasets and architectures, which may not fully demonstrate the generalizability of the method.
- The paper does not provide a detailed discussion on how the method performs in different scenarios, such as on larger or more complex datasets, or with different types of neural networks.
- The paper lacks a comparison with other learning rate scheduling methods, which could provide a more robust evaluation of the proposed method's effectiveness.
- The paper could benefit from a more thorough discussion on the potential limitations of the method and how it might perform in different scenarios.

**Questions:**
- Can the authors provide a theoretical analysis of why the proposed method works, or discuss any potential theoretical insights that could help explain its effectiveness?
- How does the method perform on larger or more complex datasets, such as ImageNet?
- Have the authors considered combining the cyclical learning rate method with other learning rate scheduling methods, such as those that adapt the learning rate over time based on the training data?
- Could the authors discuss the potential limitations of the method and how it might perform in different scenarios, such as with different types of neural networks or on different datasets?
- Would it be possible to include a comparison with other learning rate scheduling methods to provide a more robust evaluation of the proposed method's effectiveness?

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
- Reasons: The paper presents a novel and practical approach to learning rate scheduling that is supported by empirical evidence across various datasets and architectures. While the paper lacks a theoretical analysis, it is well-written, easy to follow, and provides a clear explanation of the method and its implementation. The method's simplicity and effectiveness, as demonstrated by the experiments, make it a valuable contribution to the field. The decision to accept is based on the paper's practical utility and the empirical evidence provided, despite the lack of a theoretical analysis and broader range of experiments.