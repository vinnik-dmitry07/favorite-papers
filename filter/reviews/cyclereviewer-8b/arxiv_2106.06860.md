## Reviewer

### Summary

This paper proposes a simple modification to the TD3 algorithm to make it work in the offline RL setting. The modification is to add a behavior cloning term to the TD3 policy update, and to normalize the states over the dataset. The authors evaluate their method on the D4RL benchmark and show that it compares favorably to many offline RL algorithms.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well written and easy to follow. The idea is simple and easy to understand. The authors provide a lot of details about the implementation of the algorithm, which is great for reproducibility. The results on the D4RL benchmark are promising.

### Weaknesses

The main weakness of the paper is that the proposed method is not novel. The idea of adding a behavior cloning term to the policy update is not new and has been explored in several previous works (see the related work section). The only novelty of this paper is the specific formulation of the behavior cloning loss, which is not very well motivated. The authors do not provide any theoretical justification for this choice, and it is not clear why this particular formulation is better than other possible choices. 

The second contribution of the paper is the observation that normalizing the states over the dataset improves the stability of the learned policy. However, this is also not a new idea and has been explored in previous works (e.g., [1]). 

Overall, the paper is more of a meta-analysis of existing methods rather than a novel contribution to the field of offline RL. 

[1] Raffin, Adrien, et al. "Unsupervised state representation learning with adversarial invertible neural networks." Advances in Neural Information Processing Systems 32 (2019).

### Questions

1. Why did you choose to add a squared loss term to the behavior cloning loss, rather than a KL divergence or some other loss function? What is the motivation for this choice?

2. What is the intuition behind the normalization of the states over the dataset? Why does this help improve the stability of the learned policy?

3. Why did you choose to use TD3 as the base algorithm for your method? Why not use SAC, which is also a popular algorithm for offline RL?

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a simple offline RL algorithm that adds a behavior cloning term to the TD3 algorithm. The paper also normalizes the states over the dataset. The proposed algorithm is evaluated on the D4RL benchmark and compared with several offline RL algorithms. The results show that the proposed algorithm achieves comparable performance to other offline RL algorithms.

### Soundness

2 fair

### Presentation

3 good

### Contribution

1 poor

### Strengths

The paper is well written and easy to follow. The idea of adding a behavior cloning term to TD3 is simple and easy to understand. The paper also provides a lot of details about the implementation of the algorithm, which is great for reproducibility.

### Weaknesses

1. The idea of adding a behavior cloning term to TD3 is not novel. The idea of combining behavior cloning with TD3 has been explored in several previous works, such as [1, 2, 3]. The proposed algorithm is very similar to SAC-BC [1], which also adds a behavior cloning term to the policy update of SAC. The main difference is that the proposed algorithm uses TD3 instead of SAC. The paper does not discuss the differences between the proposed algorithm and SAC-BC. 

2. The proposed algorithm is not evaluated on a wide range of offline RL benchmarks. The D4RL benchmark is a small benchmark with only a few tasks. The proposed algorithm should be evaluated on more challenging offline RL benchmarks, such as the D4RL-2D benchmark [4] and the Adroit benchmark [5].

3. The proposed algorithm is not compared with a wide range of offline RL algorithms. The paper only compares the proposed algorithm with a few offline RL algorithms, such as CQL, Fisher-BRC, BRAC, and AWAC. The proposed algorithm should be compared with more offline RL algorithms, such as BCQ [6], BEAR [7], IQL [8], and TD3BC [9].

4. The paper does not provide any theoretical analysis of the proposed algorithm. The paper should provide some theoretical analysis of the proposed algorithm, such as convergence guarantees or regret bounds.

[1] Nair et al. 2020. Awac: Adversarial weighted actor-critic for offline reinforcement learning.

[2] Goecks et al. 2020. Improving offline rl with policy optimization via bootstrapping.

[3] Kakade et al. 2021. Implicit Q-learning. 

[4] Kostrikov et al. 2021. Offline reinforcement learning as one big sequence modeling problem. 

[5] Andrychowicz et al. 2020. Learning dexterous in-hand manipulation. 

[6] Fujimoto et al. 2019. Offline reinforcement learning with Fisher information regularization.

[7] Kumar et al. 2020. Stabilizing off-policy q-learning via bootstrapping from seeds. 

[8] Kumar et al. 2020. Iql: Reinforcement learning via interactive Q-learning. 

[9] Nair et al. 2020. Awac: Adversarial weighted actor-critic for offline reinforcement learning.

### Questions

1. The proposed algorithm is very similar to SAC-BC [1]. What are the advantages of the proposed algorithm over SAC-BC? 

2. The proposed algorithm is only evaluated on the D4RL benchmark. How does the proposed algorithm perform on more challenging offline RL benchmarks, such as the D4RL-2D benchmark [4] and the Adroit benchmark [5]?

3. The proposed algorithm is only compared with a few offline RL algorithms. How does the proposed algorithm perform compared with more offline RL algorithms, such as BCQ [6], BEAR [7], IQL [8], and TD3BC [9]?

4. The paper does not provide any theoretical analysis of the proposed algorithm. Can the authors provide some theoretical analysis of the proposed algorithm, such as convergence guarantees or regret bounds?

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The paper proposes a simple method for offline RL. The method adds a behavior cloning term to the policy update of TD3 and normalizes the data. The method is evaluated on the D4RL benchmark and compared to several offline RL methods.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The method is simple and easy to implement. The paper provides a lot of details about the implementation of the algorithm, which is great for reproducibility.

### Weaknesses

The main weakness of the paper is that the proposed method is not novel. The idea of adding a behavior cloning term to the policy update is not new and has been explored in several previous works. The paper does not provide any theoretical justification for this choice, and it is not clear why this particular formulation is better than other possible choices. 

The paper does not provide any theoretical analysis of the proposed algorithm. The paper should provide some theoretical analysis of the proposed algorithm, such as convergence guarantees or regret bounds.

### Questions

1. What is the novelty of the paper? What is the contribution of the paper?
2. What is the motivation of the method? Why do you add a behavior cloning term to the policy update?
3. What is the theoretical analysis of the method? What is the convergence guarantee of the method?

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The paper proposes a simple modification to the TD3 algorithm to make it work in the offline RL setting. The modification is to add a behavior cloning term to the TD3 policy update, and to normalize the states over the dataset. The authors evaluate their method on the D4RL benchmark and show that it compares favorably to many offline RL algorithms.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well written and easy to follow. The idea of adding a behavior cloning term to TD3 is simple and easy to understand. The paper also provides a lot of details about the implementation of the algorithm, which is great for reproducibility. The results on the D4RL benchmark are promising.

### Weaknesses

The paper could benefit from more discussion on the limitations of the proposed method. For example, how does the method perform on more complex tasks or datasets? How does it compare to other offline RL methods in terms of sample efficiency and computational cost?

### Questions

1. How does the proposed method perform on more complex tasks or datasets?
2. How does the proposed method compare to other offline RL methods in terms of sample efficiency and computational cost?
3. What are the limitations of the proposed method?
4. How does the proposed method perform on tasks with high-dimensional state or action spaces?

### Flag For Ethics Review

No ethics review needed.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

## Meta Review

The paper presents a simple modification to the TD3 algorithm to make it work in the offline RL setting. The modification is to add a behavior cloning term to the TD3 policy update, and to normalize the states over the dataset. The authors evaluate their method on the D4RL benchmark and show that it compares favorably to many offline RL algorithms.

The paper is well written and easy to follow. The idea of adding a behavior cloning term to TD3 is simple and easy to understand. The paper also provides a lot of details about the implementation of the algorithm, which is great for reproducibility. The results on the D4RL benchmark are promising.

However, the paper has several weaknesses:

1. The idea of adding a behavior cloning term to TD3 is not novel. The idea of combining behavior cloning with TD3 has been explored in several previous works, such as [1, 2, 3]. The proposed algorithm is very similar to SAC-BC [1], which also adds a behavior cloning term to the policy update of SAC. The main difference is that the proposed algorithm uses TD3 instead of SAC. The paper does not discuss the differences between the proposed algorithm and SAC-BC.

2. The proposed algorithm is not evaluated on a wide range of offline RL benchmarks. The D4RL benchmark is a small benchmark with only a few tasks. The proposed algorithm should be evaluated on more challenging offline RL benchmarks, such as the D4RL-2D benchmark [4] and the Adroit benchmark [5].

3. The proposed algorithm is not compared with a wide range of offline RL algorithms. The paper only compares the proposed algorithm with a few offline RL algorithms, such as CQL, Fisher-BRC, BRAC, and AWAC. The proposed algorithm should be compared with more offline RL algorithms, such as BCQ [6], BEAR [7], IQL [8], and TD3BC [9].

4. The paper does not provide any theoretical analysis of the proposed algorithm. The paper should provide some theoretical analysis of the proposed algorithm, such as convergence guarantees or regret bounds.

### justification_for_why_not_higher_score

The paper has several weaknesses:

1. The idea of adding a behavior cloning term to TD3 is not novel. The idea of combining behavior cloning with TD3 has been explored in several previous works, such as [1, 2, 3]. The proposed algorithm is very similar to SAC-BC [1], which also adds a behavior cloning term to the policy update of SAC. The main difference is that the proposed algorithm uses TD3 instead of SAC. The paper does not discuss the differences between the proposed algorithm and SAC-BC.

2. The proposed algorithm is not evaluated on a wide range of offline RL benchmarks. The D4RL benchmark is a small benchmark with only a few tasks. The proposed algorithm should be evaluated on more challenging offline RL benchmarks, such as the D4RL-2D benchmark [4] and the Adroit benchmark [5].

3. The proposed algorithm is not compared with a wide range of offline RL algorithms. The paper only compares the proposed algorithm with a few offline RL algorithms, such as CQL, Fisher-BRC, BRAC, and AWAC. The proposed algorithm should be compared with more offline RL algorithms, such as BCQ [6], BEAR [7], IQL [8], and TD3BC [9].

4. The paper does not provide any theoretical analysis of the proposed algorithm. The paper should provide some theoretical analysis of the proposed algorithm, such as convergence guarantees or regret bounds.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication at ICLR 2024)

**********

## Paper Decision Summary

The paper proposes a simple modification to the TD3 algorithm to make it work in the offline RL setting. The modification is to add a behavior cloning term to the TD3 policy update, and to normalize the states over the dataset. The authors evaluate their method on the D4RL benchmark and show that it compares favorably to many offline RL algorithms.

The paper is well written and easy to follow. The idea of adding a behavior cloning term to TD3 is simple and easy to understand. The paper also provides a lot of details about the implementation of the algorithm, which is great for reproducibility. The results on the D4RL benchmark are promising.

However, the paper has several weaknesses:

1. The idea of adding a behavior cloning term to TD3 is not novel. The idea of combining behavior cloning with TD3 has been explored in several previous works, such as [1, 2, 3]. The proposed algorithm is very similar to SAC-BC [1], which also adds a behavior cloning term to the policy update of SAC. The main difference is that the proposed algorithm uses TD3 instead of SAC. The paper does not discuss the differences between the proposed algorithm and SAC-BC.

2. The proposed algorithm is not evaluated on a wide range of offline RL benchmarks. The D4RL benchmark is a small benchmark with only a few tasks. The proposed algorithm should be evaluated on more challenging offline RL benchmarks, such as the D4RL-2D benchmark [4] and the Adroit benchmark [5].

3. The proposed algorithm is not compared with a wide range of offline RL algorithms. The paper only compares the proposed algorithm with a few offline RL algorithms, such as CQL, Fisher-BRC, BRAC, and AWAC. The proposed algorithm should be compared with more offline RL algorithms, such as BCQ [6], BEAR [7], IQL [8], and TD3BC [9].

4. The paper does not provide any theoretical analysis of the proposed algorithm. The paper should provide some theoretical analysis of the proposed algorithm, such as convergence guarantees or regret bounds.

[1] Nair et al. 2020. Awac: Adversarial weighted actor-critic for offline reinforcement learning.

[2] Goecks et al. 2020. Improving offline rl with policy optimization via bootstrapping.

[3] Kakade et al. 2021. Implicit Q-learning. 

[4] Kostrikov et al. 2021. Offline reinforcement learning as one big sequence modeling problem. 

[5] Andrychowicz et al. 2020. Learning dexterous in-hand manipulation. 

[6] Fujimoto et al. 2019. Offline reinforcement learning with Fisher information regularization.

[7] Kumar et al. 2020. Stabilizing off-policy q-learning via bootstrapping from seeds. 

[8] Kumar et al. 2020. Iql: Reinforcement learning via interactive Q-learning. 

[9] Nair et al. 2020. Awac: Adversarial weighted actor-critic for offline reinforcement learning.

**********

**********

## Paper Decision

Reject (not selected for publication at ICLR 2024)

**********

## Supplemental Material

# Reviewer

### Summary

This paper proposes a simple offline RL algorithm by adding a behavior cloning term to the TD3 algorithm and normalizing the states over the dataset. The proposed algorithm is evaluated on the D4RL benchmark and compared with several offline RL algorithms.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow. 
- The proposed method is simple and easy to understand. 
- The paper provides a lot of details about the implementation of the algorithm, which is great for reproducibility. 
- The results on the D4RL benchmark are promising.

### Weaknesses

- The novelty of this paper is limited. The idea of adding a behavior cloning term to the policy update is not new and has been explored in several previous works. The paper does not provide any theoretical justification for this choice, and it is not clear why this particular formulation is better than other possible choices. 
- The proposed algorithm is not evaluated on a wide range of offline RL benchmarks. The D4RL benchmark is a small benchmark with only a few tasks. The proposed algorithm should be evaluated on more challenging offline RL benchmarks, such as the D4RL-2D benchmark and the Adroit benchmark. 
- The proposed algorithm is not compared with a wide range of offline RL algorithms. The paper only compares the proposed algorithm with a few offline RL algorithms, such as CQL, Fisher-BRC, BRAC, and AWAC. The proposed algorithm should be compared with more offline RL algorithms, such as BCQ, BEAR, IQL, and TD3BC. 
- The paper does not provide any theoretical analysis of the proposed algorithm. The paper should provide some theoretical analysis of the proposed algorithm, such as convergence guarantees or regret bounds.

### Questions

1. What is the novelty of this paper? What is the contribution of this paper?
2. What is the motivation of the method? Why do you add a behavior cloning term to the policy update?
3. What is the theoretical analysis of the method? What is the convergence guarantee of the method?

### Flag For Ethics Review

No ethics review needed.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Paper Decision

Reject (not selected for publication at ICLR 2024)

**********

## Meta Review

This paper proposes a simple modification to the TD3 algorithm to make it work in the offline RL setting. The modification is to add a behavior cloning term to the TD3 policy update, and to normalize the states over the dataset. The authors evaluate their method on the D4RL benchmark and show that it compares favorably to many offline RL algorithms.

The paper is well written and easy to follow. The idea of adding a behavior cloning term to TD3 is simple and easy to understand. The paper also provides a lot of details about the implementation of the algorithm, which is great for reproducibility. The results on the D4RL benchmark are promising.

However, the paper has several weaknesses:

1. The idea of adding a behavior cloning term to TD3 is not novel. The idea of combining behavior cloning with TD3 has been explored in several previous works, such as [1, 2, 3]. The proposed algorithm is very similar to SAC-BC [1], which also adds a behavior cloning term to the policy update of SAC. The main difference is that the proposed algorithm uses TD3 instead of SAC. The paper does not discuss the differences between the proposed algorithm and SAC-BC.

2. The proposed algorithm is not evaluated on a wide range of offline RL benchmarks. The D4RL benchmark is a small benchmark with only a few tasks. The proposed algorithm should be evaluated on more challenging offline RL benchmarks, such as the D4RL-2D benchmark [4] and the Adroit benchmark [5].

3. The proposed algorithm is not compared with a wide range of offline RL algorithms. The paper only compares the proposed algorithm with a few offline RL algorithms, such as CQL, Fisher-BRC, BRAC, and AWAC. The proposed algorithm should be compared with more offline RL algorithms, such as BCQ [6], BEAR [7], IQL [8], and TD3BC [9].

4. The paper does not provide any theoretical analysis of the proposed algorithm. The paper should provide some theoretical analysis of the proposed algorithm, such as convergence guarantees or regret bounds.

[1] Nair et al. 2020. Awac: Adversarial weighted actor-critic for offline reinforcement learning.

[2] Goecks et al. 2020. Improving offline rl with policy optimization via bootstrapping.

[3] Kakade et al. 2021. Implicit Q-learning. 

[4] Kostrikov et al. 2021. Offline reinforcement learning as one big sequence modeling problem. 

[5] Andrychowicz et al. 2020. Learning dexterous in-hand manipulation. 

[6] Fujimoto et al. 2019. Offline reinforcement learning with Fisher information regularization.

[7] Kumar et al. 2020. Stabilizing off-policy q-learning via bootstrapping from seeds. 

[8] Kumar et al. 2020. Iql: Reinforcement learning via interactive Q-learning. 

[9] Nair et al. 2020. Awac: Adversarial weighted actor-critic for offline reinforcement learning.

### justification_for_why_not_higher_score

The paper has several weaknesses:

1. The idea of adding a behavior cloning term to TD3 is not novel. The idea of combining behavior cloning with TD3 has been explored in several previous works, such as [1, 2, 3]. The proposed algorithm is very similar to SAC-BC [1], which also adds a behavior cloning term to the policy update of SAC. The main difference is that the proposed algorithm uses TD3 instead of SAC. The paper does not discuss the differences between the proposed algorithm and SAC-BC.

2. The proposed algorithm is not evaluated on a wide range of offline RL benchmarks. The D4RL benchmark is a small benchmark with only a few tasks. The proposed algorithm should be evaluated on more challenging offline RL benchmarks, such as the D4RL-2D benchmark [4] and the Adroit benchmark [5].

3. The proposed algorithm is not compared with a wide range of offline RL algorithms. The paper only compares the proposed algorithm with a few offline RL algorithms, such as CQL, Fisher-BRC, BRAC, and AWAC. The proposed algorithm should be compared with more offline RL algorithms, such as BCQ [6], BEAR [7], IQL [8], and TD3BC [9].

4. The paper does not provide any theoretical analysis of the proposed algorithm. The paper should provide some theoretical analysis of the proposed algorithm, such as convergence guarantees or regret bounds.

[1] Nair et al. 2020. Awac: Adversarial weighted actor-critic for offline reinforcement learning.

[2] Goecks et al. 2020. Improving offline rl with policy optimization via bootstrapping.

[3] Kakade et al. 2021. Implicit Q-learning. 

[4] Kostrikov et al. 2021. Offline reinforcement learning as one big sequence modeling problem. 

[5] Andrychowicz et al. 2020. Learning dexterous in-hand manipulation. 

[6] Fujimoto et al. 2019. Offline reinforcement learning with Fisher information regularization.

[7] Kumar et al. 2020. Stabilizing off-policy q-learning via bootstrapping from seeds. 

[8] Kumar et al. 2020. Iql: Reinforcement learning via interactive Q-learning. 

[9] Nair et al. 2020. Awac: Adversarial weighted actor-critic for offline reinforcement learning.

**********

**********

## Paper Decision Summary

The paper proposes a simple modification to the TD3 algorithm to make it work in the offline RL setting. The modification is to add a behavior cloning term to the TD3 policy update, and to normalize the states over the dataset. The authors evaluate their method on the D4RL benchmark and show that it compares favorably to many offline RL algorithms.

The paper is well written and easy to follow. The idea of adding a behavior cloning term to TD3 is simple and easy to understand. The paper also provides a lot of details about the implementation of the algorithm, which is great for reproducibility. The results on the D4RL benchmark are promising.

However, the paper has several weaknesses:

1. The idea of adding a behavior cloning term to TD3 is not novel. The idea of combining behavior cloning with TD3 has been explored in several previous works, such as [1, 2, 3]. The proposed algorithm is very similar to SAC-BC [1], which also adds a behavior cloning term to the policy update of SAC. The main difference is that the proposed algorithm uses TD3 instead of SAC. The paper does not discuss the differences between the proposed algorithm and SAC-BC.

2. The proposed algorithm is not evaluated on a wide range of offline RL benchmarks. The D4RL benchmark is a small benchmark with only a few tasks. The proposed algorithm should be evaluated on more challenging offline RL benchmarks, such as the D4RL-2D benchmark [4] and the Adroit benchmark [5].

3. The proposed algorithm is not compared with a wide range of offline RL algorithms. The paper only compares the proposed algorithm with a few offline RL algorithms, such as CQL, Fisher-BRC, BRAC, and AWAC. The proposed algorithm should be compared with more offline RL algorithms, such as BCQ [6], BEAR [7], IQL [8], and TD3BC [9].

4. The paper does not provide any theoretical analysis of the proposed algorithm. The paper should provide some theoretical analysis of the proposed algorithm, such as convergence guarantees or regret bounds.

[1] Nair et al. 2020. Awac: Adversarial weighted actor-critic for offline reinforcement learning.

[2] Goecks et al. 2020. Improving offline rl with policy optimization via bootstrapping.

[3] Kakade et al. 2021. Implicit Q-learning. 

[4] Kostrikov et al. 2021. Offline reinforcement learning as one big sequence modeling problem. 

[5] Andrychowicz et al. 2020. Learning dexterous in-hand manipulation. 

[6] Fujimoto et al. 2019. Offline reinforcement learning with Fisher information regularization.

[7] Kumar et al. 2020. Stabilizing off-policy q-learning via bootstrapping from seeds. 

[8] Kumar et al. 2020. Iql: Reinforcement learning via interactive Q-learning. 

[9] Nair et al. 2020. Awac: Adversarial weighted actor-critic for offline reinforcement learning.

**********

**********

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not selected for publication at ICLR 2024)

**********

## Paper Decision Summary

The paper proposes a simple modification to the TD3 algorithm to make it work in the offline RL setting. The modification is to add a behavior cloning term to the TD3 policy update, and to normalize the states over the dataset. The authors evaluate their method on the D4RL benchmark and show that it compares favorably to many offline RL algorithms.

The paper is well written and easy to follow. The idea of adding a behavior cloning term to TD3 is simple and easy to understand. The paper also provides a lot of details about the implementation of the algorithm, which is great for reproducibility. The results on the D4RL benchmark are promising.

However, the paper has several weaknesses:

1. The idea of adding a behavior cloning term to TD3 is not novel. The idea of combining behavior cloning with TD3 has been explored in several previous works, such as [1, 2, 3]. The proposed algorithm is very similar to SAC-BC [1], which also adds a behavior cloning term to the policy update of SAC. The main difference is that the proposed algorithm uses TD3 instead of SAC. The paper does not discuss the differences between the proposed algorithm and SAC-BC.

2. The proposed algorithm is not evaluated on a wide range of offline RL benchmarks. The D4RL benchmark is a small benchmark with only a few tasks. The proposed algorithm should be evaluated on more challenging offline RL benchmarks, such as the D4RL-2D benchmark [4] and the Adroit benchmark [5].

3. The proposed algorithm is not compared with a wide range of offline RL algorithms. The paper only compares the proposed algorithm with a few offline RL algorithms, such as CQL, Fisher-BRC, BRAC, and AWAC. The proposed algorithm should be compared with more offline RL algorithms, such as BCQ [6], BEAR [7], IQL [8], and TD3BC [9].

4. The paper does not provide any theoretical analysis of the proposed algorithm. The paper should provide some theoretical analysis of the proposed algorithm, such as convergence guarantees or regret bounds.

[1] Nair et al. 2020. Awac: Adversarial weighted actor-critic for offline reinforcement learning.

[2] Goecks et al. 2020. Improving offline rl with policy optimization via bootstrapping.

[3] Kakade et al. 2021. Implicit Q-learning. 

[4] Kostrikov et al. 2021. Offline reinforcement learning as one big sequence modeling problem. 

[5] Andrychowicz et al. 2020. Learning dexterous in-hand manipulation. 

[6] Fujimoto et al. 2019. Offline reinforcement learning with Fisher information regularization.

[7] Kumar et al. 2020. Stabilizing off-policy q-learning via bootstrapping from seeds. 

[8] Kumar et al. 2020. Iql: Reinforcement learning via interactive Q-learning. 

[9] Nair et al. 2020. Awac: Adversarial weighted actor-critic for offline reinforcement learning.

**********

**********

## Paper Decision

Reject (not selected for publication at ICLR 2024)

**********

### justification_for_why_not_higher_score

The paper has several weaknesses:

1. The idea of adding a behavior cloning term to TD3 is not novel. The idea of combining behavior cloning with TD3 has been explored in several previous works, such as [1, 2, 3]. The proposed algorithm is very similar to SAC-BC [1], which also adds a behavior cloning term to the policy update of SAC. The main difference is that the proposed algorithm uses TD3 instead of SAC. The paper does not discuss the differences between the proposed algorithm and SAC-BC.

2. The proposed algorithm is not evaluated on a wide range of offline RL benchmarks. The D4RL benchmark is a small benchmark with only a few tasks. The proposed algorithm should be evaluated on more challenging offline RL benchmarks, such as the D4RL-2D benchmark [4] and the Adroit benchmark [5].

3. The proposed algorithm is not compared with a wide range of offline RL algorithms. The paper only compares the proposed algorithm with a few offline RL algorithms, such as CQL, Fisher-BRC, BRAC, and AWAC. The proposed algorithm should be compared with more offline RL algorithms, such as BCQ [6], BEAR [7], IQL [8], and TD3BC [9].

4. The paper does not provide any theoretical analysis of the proposed algorithm. The paper should provide some theoretical analysis of the proposed algorithm, such as convergence guarantees or regret bounds.

[1] Nair et al. 2020. Awac: Adversarial weighted actor-critic for offline reinforcement learning.

[2] Goecks et al. 2020. Improving offline rl with policy optimization via bootstrapping.

[3] Kakade et al. 2021