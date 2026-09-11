 **Summary:**
The paper introduces Group-in-Group Policy Optimization (GiGPO), a novel reinforcement learning algorithm designed for training large language models (LLMs) in multi-turn decision-making tasks. GiGPO leverages a hierarchical advantage estimation approach, combining macro and micro credit assignment to enhance policy optimization. It groups trajectories based on similar states and computes relative advantages at both episode and step levels, aiming to improve credit assignment and reduce computational overhead. The algorithm is evaluated on various benchmarks, including ALFWorld, WebShop, and search-augmented QA tasks, showing superior performance over existing methods. Despite its strengths, the paper is criticized for its limited evaluation scope and potential scalability issues in highly complex environments.

**Strengths:**
- The paper is well-written, clear, and easy to follow, with a comprehensive related work section that effectively positions the research within the current literature.
- The proposed algorithm, GiGPO, is innovative and well-motivated, addressing the challenge of credit assignment in multi-turn decision-making tasks, which is crucial for training LLMs.
- The empirical results demonstrate the effectiveness of the proposed method, showing improvements over existing methods in various benchmarks.
- The paper includes a detailed ablation study that helps in understanding the contributions of different components of the proposed method.
- GiGPO's ability to provide fine-grained credit signals without requiring additional rollouts or auxiliary models is a significant advantage, making it more efficient and scalable compared to other methods.

**Weaknesses:**
- The paper lacks a detailed comparison with other group-based RL algorithms, which could have provided a clearer understanding of GiGPO's advantages and limitations.
- The evaluation is limited to a few benchmarks, which might not fully demonstrate the generalizability of the proposed method across different environments.
- The paper does not discuss the scalability of the method in highly complex environments, which is a significant concern given the potential for increased noise or subtle differences in state representations.
- There is a lack of discussion on the limitations of the proposed method, which could help in understanding its applicability and potential challenges in real-world scenarios.
- The paper does not provide sufficient details on the computational cost of the proposed method, which is crucial for understanding its practical applicability.

**Questions:**
- Could the authors provide a more detailed comparison with other group-based RL algorithms to better understand the advantages and limitations of GiGPO?
- How does the proposed method perform in more complex environments, such as those with a large number of states or subtle differences between states?
- Can the authors discuss the limitations of the proposed method and provide insights into potential future research directions to address these limitations?
- What are the specific computational costs associated with the proposed method, and how do these costs compare to other methods in terms of efficiency and scalability?
- Could the authors provide more details on the hyperparameter tuning process, particularly how the weighting coefficient ω and the KL penalty β were chosen for different tasks?
- How does the proposed method handle the potential for increased noise or subtle differences in state representations in highly complex environments?

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
- Reasons: The paper introduces a novel and effective algorithm for training LLMs in multi-turn decision-making tasks, addressing the challenge of credit assignment in a scalable and computationally efficient manner. The method's effectiveness is demonstrated through empirical results, which show improvements over existing methods. The paper is well-written, making it accessible and easy to understand. Despite some concerns regarding the limited evaluation scope and potential scalability issues in complex environments, the overall contribution and soundness of the method justify its acceptance. The decision aligns with the reviewers' consensus and the metareview, which highlights the paper's originality, methodological soundness, and significance of results.