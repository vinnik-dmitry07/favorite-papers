 **Summary:**
The paper introduces a novel approach to training deep neural networks for reinforcement learning using a genetic algorithm (GA), demonstrating its effectiveness on challenging tasks such as Atari and humanoid locomotion. The authors employ a compact encoding technique to represent neural network parameters, which is crucial for distributed training. The GA is shown to perform competitively with other methods like DQN, A3C, and ES, and even surpasses them in certain tasks. The paper also explores the use of novelty search to enhance exploration in deceptive environments. Despite some concerns about the novelty and the depth of the experimental validation, the paper is well-written, clear, and presents a significant contribution to the field by demonstrating the potential of GAs in deep RL.

**Strengths:**
- The paper is well-written, clear, and easy to follow, making it accessible to a broad audience.
- The experiments are well-designed, with a good selection of baselines and a thorough evaluation of the proposed methods.
- The results are surprising and interesting, showing that GAs can perform well in deep RL, even surpassing the performance of other methods in some tasks.
- The paper introduces a novel compact encoding technique that is crucial for distributed training and reduces the size of the GA's representation.
- The paper provides a good overview of the current state of the art in deep RL and compares the proposed method with various other approaches, including random search.
- The use of novelty search in deceptive environments is a significant contribution, showing that GAs can be effective in such scenarios.

**Weaknesses:**
- The paper lacks a detailed discussion on the limitations of the proposed method, which could help in understanding its applicability and performance in different scenarios.
- There is a need for more detailed experimental results, particularly in the appendix, to support the claims made in the main text.
- The paper could benefit from a more thorough discussion on the computational resources required for training, as this is a significant aspect of the proposed method.
- The novelty of the approach is questionable, as the use of GAs for RL and the compact encoding technique have been previously explored.
- The paper could benefit from a more detailed discussion on the hyperparameter settings used in the experiments, as these are crucial for reproducibility and understanding the results.
- The paper could be improved by including more diverse baselines, such as evolution strategies, to provide a more comprehensive comparison.

**Questions:**
- Could the authors provide more details on the computational resources required for training, including the number of GPUs used and the time taken for each experiment?
- How does the proposed method compare to other evolutionary algorithms, particularly those that use different mutation operators or different selection strategies?
- Can the authors clarify the role of random search in the experiments and how it was implemented?
- How does the proposed method compare to other recent works that have explored similar approaches, such as those using evolutionary algorithms for architecture search?
- Could the authors provide more detailed experimental results, particularly in the appendix, to support the claims made in the main text?
- How were the hyperparameters for the GA tuned, and what impact do these settings have on the performance of the method?

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
- Reasons: The paper presents a novel approach to training deep neural networks for reinforcement learning using a genetic algorithm, demonstrating its effectiveness on challenging tasks such as Atari and humanoid locomotion. The method's simplicity and the compact encoding technique for distributed training are significant contributions to the field. Despite some concerns about the novelty and the depth of the experimental validation, the paper is well-written, clear, and provides a valuable contribution to the ongoing research in deep RL. The decision to accept is based on the paper's originality, methodological soundness, and the significance of its results, as well as the clarity and logic of its presentation.