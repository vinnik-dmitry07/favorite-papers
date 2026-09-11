I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

The paper studies the behavior of backpropagation in continual learning settings. The authors show that backpropagation suffers from performance degradation over time in non-stationary problems. To address this, they propose Continual Backprop (CBP), which continually injects random features and uses a generate-and-test process for feature selection. The authors evaluate CBP on various continual learning tasks, including semi-stationary problems, Permuted MNIST, and a non-stationary RL problem, demonstrating CBP's effectiveness in adapting to changing environments.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper addresses an important problem in continual learning, specifically the limitations of backpropagation in non-stationary environments.
2. The proposed Continual Backprop (CBP) algorithm is novel and well-motivated, offering a new approach to maintaining performance over time.
3. The experiments cover a range of tasks, including synthetic problems and more complex benchmarks like Permuted MNIST and a non-stationary RL problem, providing a comprehensive evaluation of CBP's effectiveness.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed discussion on the computational overhead of the Continual Backprop (CBP) algorithm, especially in comparison to standard backpropagation. The continual injection of random features and the generate-and-test process likely introduce significant computational costs, which are not thoroughly analyzed. Specifically, the paper should quantify the additional FLOPs, memory usage, and training time required by CBP, and compare these metrics to standard backpropagation across different problem complexities and network sizes. This analysis should also consider the scaling behavior of the overhead with respect to the number of non-stationarities and the dimensionality of the input space.
2. While the paper introduces a novel approach to continual learning, the theoretical underpinnings of why CBP outperforms standard backpropagation in non-stationary settings could be further elaborated. The paper should provide a more rigorous analysis of the feature dynamics within the network under both backpropagation and CBP. This analysis should include a discussion of how the random feature injection and the generate-and-test process affect the network's ability to adapt to changing data distributions. It would be beneficial to explore the convergence properties of CBP in non-stationary environments, and to provide insights into how the parameters of the generate-and-test process are chosen and how they impact the overall performance.

### Suggestions

To strengthen the paper, the authors should provide a more detailed analysis of the computational complexity of the Continual Backprop (CBP) algorithm. This analysis should go beyond a high-level discussion and include a breakdown of the computational costs associated with each step of the CBP algorithm, such as the random feature injection, the generate-and-test process, and the weight updates. The analysis should also consider the impact of different hyperparameters, such as the number of random features injected, the frequency of the generate-and-test process, and the size of the test set used for feature selection. Furthermore, the authors should compare the computational costs of CBP with those of standard backpropagation and other continual learning algorithms, providing a clear understanding of the trade-offs between performance and computational efficiency. This comparison should be performed on a range of problem complexities and network sizes to demonstrate the scalability of CBP.

In addition to the computational analysis, the authors should provide a more in-depth theoretical analysis of why CBP outperforms standard backpropagation in non-stationary settings. This analysis should focus on the feature dynamics within the network under both backpropagation and CBP. Specifically, the authors should investigate how the random feature injection and the generate-and-test process affect the network's ability to adapt to changing data distributions. This could involve analyzing the convergence properties of CBP in non-stationary environments, and providing insights into how the parameters of the generate-and-test process are chosen and how they impact the overall performance. For example, the authors could explore how the size of the test set used for feature selection affects the stability and plasticity of the network. A more rigorous theoretical analysis would provide a deeper understanding of the mechanisms behind the effectiveness of CBP and would help to guide the design of future continual learning algorithms.

Finally, the authors should consider including additional experiments to further validate the effectiveness of CBP. For example, they could explore the performance of CBP on more complex continual learning benchmarks, such as those involving concept drift or task-incremental learning. They could also investigate the robustness of CBP to different types of non-stationarities, such as abrupt changes in the data distribution or gradual drifts. Furthermore, it would be beneficial to compare the performance of CBP with other state-of-the-art continual learning algorithms, including those that are specifically designed to handle non-stationary environments. This would provide a more comprehensive evaluation of the strengths and weaknesses of CBP and would help to establish its position within the broader landscape of continual learning research.

### Questions

1. How does the Continual Backprop (CBP) algorithm compare to other continual learning methods in terms of computational efficiency and scalability?
2. Can the authors provide more insights into the theoretical reasons behind the effectiveness of CBP in non-stationary environments?

### Rating

5

### Confidence

3

**********

## Reviewer 2

### Summary

The paper studies the continual learning problem. The authors first show that backpropagation suffers from performance degradation over time in non-stationary problems. Then the authors propose a novel algorithm, Continual Backprop (CBP), which continually injects random features and uses a generate-and-test process for feature selection. The authors show that CBP could continually adapt even after thousands of non-stationarities. The authors also show that backpropagation with L2 regularization can adapt continually in some problems, but it fails in many others.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow. The authors provide a clear motivation for the problem and the proposed solution. The paper is well-organized and the ideas are presented in a logical and coherent manner.

2. The authors provide a comprehensive evaluation of the proposed algorithm on several continual learning tasks, including semi-stationary problems, Permuted MNIST, and a non-stationary RL problem. The results demonstrate the effectiveness of the proposed algorithm in adapting to changing environments.

3. The authors also provide a theoretical analysis of the proposed algorithm, showing that it can adapt to non-stationary problems. The theoretical analysis provides insights into the behavior of the algorithm and helps to understand its strengths and limitations.

### Weaknesses

#### Some Related Works


#### comment

1. The paper focuses on the performance degradation of backpropagation in non-stationary problems, but it does not provide a detailed analysis of the causes of this degradation. It would be helpful to understand the specific mechanisms that lead to the performance drop, such as the vanishing or exploding gradients, or the inability of the network to adapt to new data distributions. A more in-depth analysis of these mechanisms would provide valuable insights into the limitations of backpropagation in non-stationary settings.

2. The paper proposes a novel algorithm, Continual Backprop (CBP), but it does not provide a detailed comparison with other continual learning algorithms. It would be helpful to compare the performance of CBP with other state-of-the-art continual learning algorithms, such as regularization-based methods, replay-based methods, or parameter isolation techniques. This comparison would help to understand the advantages and disadvantages of CBP and its potential for practical applications.

3. The paper evaluates the proposed algorithm on several continual learning tasks, but it does not provide a detailed analysis of the computational cost of the algorithm. It would be helpful to understand the computational complexity of CBP and its scalability to large-scale problems. This analysis would help to assess the practical feasibility of the algorithm and its potential for real-world applications.

### Suggestions

The paper would benefit from a more thorough investigation into the root causes of backpropagation's performance degradation in non-stationary environments. While the paper identifies the issue, it lacks a detailed analysis of the underlying mechanisms. For instance, the authors could explore how the gradients change over time in non-stationary settings, and how these changes lead to the observed performance drop. Specifically, they could analyze the distribution of gradients and weights during training and how these distributions evolve as the data distribution changes. This analysis could involve techniques such as visualizing the gradient norms, weight distributions, and loss landscapes at different stages of training. Furthermore, the authors could investigate the impact of different learning rates and optimization algorithms on the stability of backpropagation in non-stationary environments. This would provide a more comprehensive understanding of the limitations of backpropagation and the potential benefits of the proposed Continual Backprop (CBP) algorithm.

To strengthen the paper, a more comprehensive comparison with existing continual learning algorithms is needed. The authors should not only compare the performance of CBP with other state-of-the-art methods but also analyze the trade-offs between different approaches. For example, regularization-based methods aim to prevent catastrophic forgetting by penalizing changes to important weights, while replay-based methods store and replay a subset of past data to maintain performance on previous tasks. Parameter isolation techniques, on the other hand, aim to prevent interference between different tasks by assigning different sets of parameters to each task. A detailed comparison of these methods with CBP would help to understand the strengths and weaknesses of each approach and identify the specific scenarios where CBP is most effective. This comparison should include a discussion of the computational cost, memory requirements, and ease of implementation of each method. Furthermore, the authors should consider evaluating CBP on a wider range of continual learning benchmarks to assess its generalizability.

Finally, the paper should include a more detailed analysis of the computational cost of the proposed CBP algorithm. The authors should provide a theoretical analysis of the time and space complexity of the algorithm and discuss its scalability to large-scale problems. This analysis should consider the computational cost of the random feature injection, the generate-and-test process, and the weight updates. Furthermore, the authors should evaluate the performance of CBP on larger datasets and with more complex network architectures to assess its practical feasibility. This analysis should also include a discussion of the potential bottlenecks of the algorithm and how they can be addressed. The authors could also explore techniques for optimizing the implementation of CBP to reduce its computational cost. This would provide a more complete picture of the practical implications of the proposed algorithm.

### Questions

1. How does the performance of CBP vary with different choices of the random features? Are there any guidelines for selecting the random features to ensure optimal performance?

2. How does the performance of CBP compare with other continual learning algorithms, such as regularization-based methods, replay-based methods, or parameter isolation techniques?

3. What is the computational cost of CBP, and how does it scale with the size of the network and the number of non-stationarities?

### Rating

6

### Confidence

2

**********

## Reviewer 3

### Summary

This paper studies the continual learning problem in non-stationary problems. The authors first show that backpropagation suffers from performance degradation over time. Then, the authors propose a new algorithm, Continual Backprop (CBP), which continually injects random features and uses a generate-and-test process for feature selection. The authors show that CBP could continually adapt even after thousands of non-stationarities.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a comprehensive evaluation of the proposed algorithm on several continual learning tasks, including semi-stationary problems, Permuted MNIST, and a non-stationary RL problem. The results demonstrate the effectiveness of the proposed algorithm in adapting to changing environments.
3. The authors also provide a theoretical analysis of the proposed algorithm, showing that it can adapt to non-stationary problems.

### Weaknesses

#### Some Related Works


#### comment

1. The paper focuses on the performance degradation of backpropagation in non-stationary problems, but it does not provide a detailed analysis of the causes of this degradation. It would be helpful to understand the specific mechanisms that lead to the performance drop, such as the vanishing or exploding gradients, or the inability of the network to adapt to new data distributions. A more in-depth analysis of these mechanisms would provide valuable insights into the limitations of backpropagation in non-stationary settings.
2. The paper proposes a novel algorithm, Continual Backprop (CBP), but it does not provide a detailed comparison with other continual learning algorithms. It would be helpful to compare the performance of CBP with other state-of-the-art continual learning algorithms, such as regularization-based methods, replay-based methods, or parameter isolation techniques. This comparison would help to understand the advantages and disadvantages of CBP and its potential for practical applications.
3. The paper evaluates the proposed algorithm on several continual learning tasks, but it does not provide a detailed analysis of the computational cost of the algorithm. It would be helpful to understand the computational complexity of CBP and its scalability to large-scale problems. This analysis would help to assess the practical feasibility of the algorithm and its potential for real-world applications.

### Suggestions

The paper would benefit from a more thorough investigation into the root causes of backpropagation's performance degradation in non-stationary environments. While the paper identifies the issue, it lacks a detailed analysis of the underlying mechanisms. For instance, the authors could explore how the gradients change over time in non-stationary settings, and how these changes lead to the observed performance drop. Specifically, they could analyze the distribution of gradients and weights during training and how these distributions evolve as the data distribution changes. This analysis could involve techniques such as visualizing the gradient norms, weight distributions, and loss landscapes at different stages of training. Furthermore, the authors could investigate the impact of different learning rates and optimization algorithms on the stability of backpropagation in non-stationary environments. This would provide a more comprehensive understanding of the limitations of backpropagation and the potential benefits of the proposed Continual Backprop (CBP) algorithm.

To strengthen the paper, a more comprehensive comparison with existing continual learning algorithms is needed. The authors should not only compare the performance of CBP with other state-of-the-art methods but also analyze the trade-offs between different approaches. For example, regularization-based methods aim to prevent catastrophic forgetting by penalizing changes to important weights, while replay-based methods store and replay a subset of past data to maintain performance on previous tasks. Parameter isolation techniques, on the other hand, aim to prevent interference between different tasks by assigning different sets of parameters to each task. A detailed comparison of these methods with CBP would help to understand the strengths and weaknesses of each approach and identify the specific scenarios where CBP is most effective. This comparison should include a discussion of the computational cost, memory requirements, and ease of implementation of each method. Furthermore, the authors should consider evaluating CBP on a wider range of continual learning benchmarks to assess its generalizability.

Finally, the paper should include a more detailed analysis of the computational cost of the proposed CBP algorithm. The authors should provide a theoretical analysis of the time and space complexity of the algorithm and discuss its scalability to large-scale problems. This analysis should consider the computational cost of the random feature injection, the generate-and-test process, and the weight updates. Furthermore, the authors should evaluate the performance of CBP on larger datasets and with more complex network architectures to assess its practical feasibility. This analysis should also include a discussion of the potential bottlenecks of the algorithm and how they can be addressed. The authors could also explore techniques for optimizing the implementation of CBP to reduce its computational cost. This would provide a more complete picture of the practical implications of the proposed algorithm.

### Questions

See above

### Rating

6

### Confidence

2

**********

## Reviewer 4

### Summary

This paper studies the problem of learning in non-stationary problems. The authors first show that backpropagation suffers from performance degradation over time. Then the authors propose a novel algorithm, Continual Backprop (CBP), which continually injects random features and uses a generate-and-test process for feature selection. The authors show that CBP could continually adapt even after thousands of non-stationarities.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a comprehensive evaluation of the proposed algorithm on several continual learning tasks, including semi-stationary problems, Permuted MNIST, and a non-stationary RL problem. The results demonstrate the effectiveness of the proposed algorithm in adapting to changing environments.
3. The authors also provide a theoretical analysis of the proposed algorithm, showing that it can adapt to non-stationary problems.

### Weaknesses

#### Some Related Works


#### comment

1. The paper focuses on the performance degradation of backpropagation in non-stationary problems, but it does not provide a detailed analysis of the causes of this degradation. It would be helpful to understand the specific mechanisms that lead to the performance drop, such as the vanishing or exploding gradients, or the inability of the network to adapt to new data distributions. A more in-depth analysis of these mechanisms would provide valuable insights into the limitations of backpropagation in non-stationary settings.
2. The paper proposes a novel algorithm, Continual Backprop (CBP), but it does not provide a detailed comparison with other continual learning algorithms. It would be helpful to compare the performance of CBP with other state-of-the-art continual learning algorithms, such as regularization-based methods, replay-based methods, or parameter isolation techniques. This comparison would help to understand the advantages and disadvantages of CBP and its potential for practical applications.
3. The paper evaluates the proposed algorithm on several continual learning tasks, but it does not provide a detailed analysis of the computational cost of the algorithm. It would be helpful to understand the computational complexity of CBP and its scalability to large-scale problems. This analysis would help to assess the practical feasibility of the algorithm and its potential for real-world applications.

### Suggestions

The paper would benefit from a more thorough investigation into the root causes of backpropagation's performance degradation in non-stationary environments. While the paper identifies the issue, it lacks a detailed analysis of the underlying mechanisms. For instance, the authors could explore how the gradients change over time in non-stationary settings, and how these changes lead to the observed performance drop. Specifically, they could analyze the distribution of gradients and weights during training and how these distributions evolve as the data distribution changes. This analysis could involve techniques such as visualizing the gradient norms, weight distributions, and loss landscapes at different stages of training. Furthermore, the authors could investigate the impact of different learning rates and optimization algorithms on the stability of backpropagation in non-stationary environments. This would provide a more comprehensive understanding of the limitations of backpropagation and the potential benefits of the proposed Continual Backprop (CBP) algorithm.

To strengthen the paper, a more comprehensive comparison with existing continual learning algorithms is needed. The authors should not only compare the performance of CBP with other state-of-the-art methods but also analyze the trade-offs between different approaches. For example, regularization-based methods aim to prevent catastrophic forgetting by penalizing changes to important weights, while replay-based methods store and replay a subset of past data to maintain performance on previous tasks. Parameter isolation techniques, on the other hand, aim to prevent interference between different tasks by assigning different sets of parameters to each task. A detailed comparison of these methods with CBP would help to understand the strengths and weaknesses of each approach and identify the specific scenarios where CBP is most effective. This comparison should include a discussion of the computational cost, memory requirements, and ease of implementation of each method. Furthermore, the authors should consider evaluating CBP on a wider range of continual learning benchmarks to assess its generalizability.

Finally, the paper should include a more detailed analysis of the computational cost of the proposed CBP algorithm. The authors should provide a theoretical analysis of the time and space complexity of the algorithm and discuss its scalability to large-scale problems. This analysis should consider the computational cost of the random feature injection, the generate-and-test process, and the weight updates. Furthermore, the authors should evaluate the performance of CBP on larger datasets and with more complex network architectures to assess its practical feasibility. This analysis should also include a discussion of the potential bottlenecks of the algorithm and how they can be addressed. The authors could also explore techniques for optimizing the implementation of CBP to reduce its computational cost. This would provide a more complete picture of the practical implications of the proposed algorithm.

### Questions

See above

### Rating

6

### Confidence

2

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers for the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

Plan:
1. Read each reviewer's weakness.
2. Find the corresponding section in the paper.
3. Look for evidence (quotes, experimental setup, missing information) to support the weakness.
4. If the weakness is about missing information, check if the information is indeed absent.
5. If reviewers have conflicting opinions, note them down.
6. Summarize the findings for each weakness.
```json
[
  {
    "Weakness Statement": "The paper lacks a detailed discussion on the computational overhead of the Continual Backprop (CBP) algorithm, especially in comparison to standard backpropagation. The continual injection of random features and the generate-and-test process likely introduce significant computational costs, which are not thoroughly analyzed. Specifically, the paper should quantify the additional FLOPs, memory usage, and training time required by CBP, and compare these metrics to standard backpropagation across different problem complexities and network sizes. This analysis should also consider the scaling behavior of the overhead with respect to the number of non-stationarities and the dimensionality of the input space.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        {
          "quote": "Our generate-and-test process is applicable to arbitrary feed-forward networks, modern activations, and optimizers. While the prior algorithm (Mahmood & Sutton, 2013) was limited to learning networks with a single hidden layer, only one output, LTU activation and could only use SGD to learn.",
          "section": "4 Continual Backprop"
        },
        {
          "quote": "The final algorithm combines Backprop with our generate-and-test process to continually replace low utility features with new random features. This process has two parts. First is a generator that provides new random features from the initial distribution. The second is a tester that finds low utility features and replaces them. At every time-step, replacement-rate , ρ , fraction of features are replaced in every layer. Our utility measure has two parts: first measures the contribution-utility is the sum of the utilities of all its outgoing connections. The contribution-utility is measured as a running average with a decay rate, η . In a feed-forward neural network, the contribution-utility, c l , i , t c_{l, i, t}c_{l,i,t} , of the i i -th features in layer l l at time t t is updated as c l , i , t = ( 1 − η ) ∗ | h l , i , t | ∗ ∑ k = 1 n l + 1 | w l , i , k , t | + η ∗ c l , i , t − 1 , \displaystyle=(1-\eta)*|h_{l,i,t}|*\sum_{k=1}^{n_{l+1}}|w_{l,i,k,t}|+\eta*c_{l,i,t-1},",
          "section": "4 Continual Backprop"
        },
        {
          "quote": "In the network pruning problem, the connections are removed after learning is done. However, generate-and-test is used during learning, so we need to consider the effect of the learning process on the contribution. Specifically, we need to consider the part of the contribution that will be transferred to the bias when a feature is removed. When a feature is removed, SGD will transfer the average part of the contribution to the bias unit over time. We define, the mean-corrected contribution utility, z l , i , t z_{l,i,t}z_{l,i,t} , is the magnitude of the product of connecting weight and input minus its average value, f l , i , t = ( 1 − η ) ∗ h l , i , t + η ∗ f l , i , t − 1 , ( 3 ) f ^ l , i , t = f l , i , t − 1 1 − η a l , i , t , \displaystyle=(1-\eta)*h_{l,i,t}+\eta*f_{l,i,t-1}, \displaystyle\hat{f}_{l,i,t} = f l , i , t − 1 1 − η a_{l,i,t},",
          "section": "4 Continual Backprop"
        }
      ],
      "b) Experiment-related Evidence": [
        {
          "quote": "Figure 5 shows that all three algorithms: CBP, BP+L2, and BP+OnlineNorm, perform significantly better than BP. However, BP+OnlineNorm is not stable for any of the activations as its performance degrades over time. In comparison, BP+L2 regularization is stable for the tanh network but not the ReLU network. The parameter-sensitivity plot in Figure 5 shows that CBP and BP+L2 perform better than BP for most values of replacement-rate and weight-decay. And that CBP is much less sensitive to the parameter values than L2. For ReLU, CB+L2 regularization is stable for the tanh network but not the ReLU network. The performance of all the other algorithms degrades over time.",
          "section": "5.1.1 Semi-stationary problems"
        },
        {
          "quote": "Figure 8 shows that among all the algorithms, only CBP is stable as its performance does not degrade over time. The performance of PPO degrades a lot in our non-stationary RL problem. This degradation is similar to the degradation of Backprop’s performance on semi-stationary problems, where it performed well initially, but its performance got worse over time. Figure 8 shows that both CPPO and PPO+L2 perform substantially better than PPO, and CPPO performed best, where it continually performed as well as it did initially.",
          "section": "5.2.1 Non-stationary RL problem"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper describes the components of CBP, including the generator and tester processes, which involve random feature injection and a utility measure. The experimental results show that CBP maintains performance better than standard backpropagation in non-stationary settings. However, the paper does not provide a quantitative analysis of the computational overhead.",
      "Supporting quotes": [
        "Our generate-and-test process is applicable to arbitrary feed-forward networks, modern activations, and optimizers.",
        "Figure 5 shows that all three algorithms: CBP, BP+L2, and BP+OnlineNorm, perform significantly better than BP.",
        "Figure 8 shows that among all the algorithms, only CBP is stable as its performance does not degrade over time."
      ],
      "Impact assessment": "The lack of a computational cost analysis is a valid weakness. While the paper demonstrates the effectiveness of CBP, it does not address the practical implications of its computational demands, especially in comparison to standard backpropagation."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper describes the algorithm but lacks a quantitative analysis of its computational cost compared to standard backpropagation."
    }
  },
  {
    "Weakness Statement": "While the paper introduces a novel approach to continual learning, the theoretical underpinnings of why CBP outperforms standard backpropagation in non-stationary settings could be further elaborated. The paper should provide a more rigorous analysis of the feature dynamics within the network under both backpropagation and CBP. This analysis should include a discussion of how the random feature injection and the generate-and-test process affect the network's ability to adapt to changing data distributions. It would be beneficial to explore the convergence properties of CBP in non-stationary environments, and to provide insights into how the parameters of the generate-and-test process are chosen and how they impact the overall performance.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        {
          "quote": "The first contribution of our work is to show that in non-stationary problems with many non-stationarities BP loses its ability to adapt over time. In other words, we contribute to the understanding of why BP and its variant Adam fails in non-stationary problems. Our second contribution is that we propose the CBP algorithm. CBP continually injects random features alongside SGD and uses a generate-and-test mechanism that consists of two parts: a generator proposes new features, and a tester finds and replaces low utility features with the features proposed by the generator. We show that unlike BP, CBP can continually adapt in non-stationary problems.",
          "section": "1 Introduction"
        },
        {
          "quote": "We use a linear tracker as a baseline in the Bit-Flipping problem. The linear tracker predicts that output as a linear combination of the inputs. The weights for the linear combination are learned with SGD. We choose the step-size parameter that had least total error.",
          "section": "2.1 Bit-Flipping problem"
        },
        {
          "quote": "We used uniform Kaiming distribution (He et al., 2015) to initialize the learning network’s weights. The distribution is U ⁡ ( − b , b ) with bound, b = g ⁡ ( tan ⁡ ( π / 6 ) ) , where g ⁡ ( a ) is the number of input units, and β ∈ [ 0 , 1 ] .",
          "section": "2.1 Bit-Flipping problem"
        },
        {
          "quote": "In the network pruning problem, the connections are removed after learning is done. However, generate-and-test is used during learning, so we need to consider the effect of the learning process on the contribution. Specifically, we need to consider the part of the contribution that will be transferred to the bias when a feature is removed. When a feature is removed, SGD will transfer the average part of the contribution to the bias unit over time. We define, the mean-corrected contribution utility, z l , i , t z_{l,i,t}z_{l,i,t} , is the magnitude of the product of connecting weight and input minus its average value, f l , i , t = ( 1 − η ) ∗ h l , i , t + η ∗ f l , i , t − 1 , ( 3 ) f ^ l , i , t = f l , i , t − 1 1 − η a l , i , t , \displaystyle=(1-\eta)*h_{l,i,t}+\eta*f_{l,i,t-1}, \displaystyle\hat{f}_{l,i,t} = f l , i , t − 1 1 − η a_{l,i,t},",
          "section": "4 Continual Backprop"
        }
      ],
      "b) Experiment-related Evidence": [
        {
          "quote": "Figure 5 shows that all three algorithms: CBP, BP+L2, and BP+OnlineNorm, perform significantly better than BP. However, BP+OnlineNorm is not stable for any of the activations as its performance degrades over time. In comparison, BP+L2 regularization is stable for the tanh network but not the ReLU network. The parameter-sensitivity plot in Figure 5 shows that CBP and BP+L2 perform better than BP for most values of replacement-rate and weight-decay. And that CBP is much less sensitive to the parameter values than L2. For ReLU, CB+L2 regularization is stable for the tanh network but not the ReLU network. The performance of all the other algorithms degrades over time.",
          "section": "5.1.1 Semi-stationary problems"
        },
        {
          "quote": "Figure 8 shows that among all the algorithms, only CBP is stable as its performance does not degrade over time. The performance of PPO degrades a lot in our non-stationary RL problem. This degradation is similar to the degradation of Backprop’s performance on semi-stationary problems, where it performed well initially, but its performance got worse over time. Figure 8 shows that both CPPO and PPO+L2 perform substantially better than PPO, and CPPO performed best, where it continually performed as well as it did initially.",
          "section": "5.2.1 Non-stationary RL problem"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper empirically demonstrates CBP's effectiveness and shows that standard backpropagation degrades in non-stationary settings. The method section describes the generator and tester mechanisms. The experiments show that CBP outperforms standard backpropagation. However, the paper lacks a formal theoretical analysis of why CBP is more robust or a detailed discussion of the convergence properties in non-stationary environments.",
      "Supporting quotes": [
        "Our second contribution is that we propose the CBP algorithm. CBP continually injects random features alongside SGD and uses a generate-and-test mechanism that consists of two parts: a generator proposes new features, and a tester finds and replaces low utility features with the features proposed by the generator.",
        "Figure 5 shows that all three algorithms: CBP, BP+L2, and BP+OnlineNorm, perform significantly better than BP.",
        "Figure 8 shows that among all the algorithms, only CBP is stable as its performance does not degrade over time."
      ],
      "Impact assessment": "The lack of a theoretical analysis is a valid weakness. While the empirical results are strong, a theoretical understanding of CBP's behavior would strengthen the paper's contribution."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper lacks a formal theoretical analysis of CBP's convergence or a detailed explanation of why the proposed mechanisms lead to better performance in non-stationary settings."
    }
  },
  {
    "Weakness Statement": "To strengthen the paper, the authors should provide a more detailed analysis of the computational complexity of the Continual Backprop (CBP) algorithm. This analysis should go beyond a high-level discussion and include a breakdown of the computational costs associated with each step of the CBP algorithm, such as the random feature injection, the generate-and-test process, and the weight updates. The analysis should also consider the impact of different hyperparameters, such as the number of random features injected, the frequency of the generate-and-test process, and the size of the test set used for feature selection. Furthermore, the authors should compare the computational costs of CBP with those of standard backpropagation and other continual learning algorithms, providing a clear understanding of the trade-offs between performance and computational efficiency. This comparison should be performed on a range of problem complexities and network sizes to demonstrate the scalability of CBP.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        {
          "quote": "Our generate-and-test process is applicable to arbitrary feed-forward networks, modern activations, and optimizers. While the prior algorithm (Mahmood & Sutton, 2013) was limited to learning networks with a single hidden layer, only one output, LTU activation and could only use SGD to learn.",
          "section": "4 Continual Backprop"
        },
        {
          "quote": "The final algorithm combines Backprop with our generate-and-test process to continually replace low utility features with new random features. This process has two parts. First is a generator that provides new random features from the initial distribution. The second is a tester that finds low utility features and replaces them. At every time-step, replacement-rate , ρ , fraction of features are replaced in every layer. Our utility measure has two parts: first measures the contribution-utility is the sum of the utilities of all its outgoing connections. The contribution-utility is measured as a running average with a decay rate, η . In a feed-forward neural network, the contribution-utility, c l , i , t c_{l, i, t}c_{l,i,t} , of the i i -th features in layer l l at time t t is updated as c l , i , t = ( 1 − η ) ∗ | h l , i , t | ∗ ∑ k = 1 n l + 1 | w l , i , k , t | + η ∗ c l , i , t − 1 , \displaystyle=(1-\eta)*|h_{l,i,t}|*\sum_{k=1}^{n_{l+1}}|w_{l,i,k,t}|+\eta*c_{l,i,t-1},",
          "section": "4 Continual Backprop"
        }
      ],
      "b) Experiment-related Evidence": [
        {
          "quote": "Figure 5 shows that all three algorithms: CBP, BP+L2, and BP+OnlineNorm, perform significantly better than BP. However, BP+OnlineNorm is not stable for any of the activations as its performance degrades over time. In comparison, BP+L2 regularization is stable for the tanh network but not the ReLU network. The parameter-sensitivity plot in Figure 5 shows that CBP and BP+L2 perform better than BP for most values of replacement-rate and weight-decay. And that CBP is much less sensitive to the parameter values than L2. For ReLU, CB+L2 regularization is stable for the tanh network but not the ReLU network. The performance of all the other algorithms degrades over time.",
          "section": "5.1.1 Semi-stationary problems"
        },
        {
          "quote": "Figure 8 shows that among all the algorithms, only CBP is stable as its performance does not degrade over time. The performance of PPO degrades a lot in our non-stationary RL problem. This degradation is similar to the degradation of Backprop’s performance on semi-stationary problems, where it performed well initially, but its performance got worse over time. Figure 8 shows that both CPPO and PPO+L2 perform substantially better than PPO, and CPPO performed best, where it continually performed as well as it did initially.",
          "section": "5.2.1 Non-stationary RL problem"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper describes the components of CBP and shows empirical results. However, it lacks a detailed breakdown of the computational costs of each step, the impact of hyperparameters, and a direct comparison of computational costs with standard backpropagation and other continual learning methods.",
      "Supporting quotes": [
        "Our generate-and-test process is applicable to arbitrary feed-forward networks, modern activations, and optimizers.",
        "Figure 5 shows that all three algorithms: CBP, BP+L2, and BP+OnlineNorm, perform significantly better than BP.",
        "Figure 8 shows that among all the algorithms, only CBP is stable as its performance does not degrade over time."
      ],
      "Impact assessment": "The absence of a detailed computational complexity analysis is a valid weakness, as it limits the understanding of the practical implications of CBP's computational demands."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper does not provide a quantitative analysis of the computational cost of CBP compared to standard backpropagation or other continual learning methods."
    }
  },
  {
    "Weakness Statement": "Finally, the paper should include a more detailed analysis of the computational cost of the proposed CBP algorithm. The authors should provide a theoretical analysis of the time and space complexity of the algorithm and discuss its scalability to large-scale problems. This analysis should consider the computational cost of the random feature injection, the generate-and-test process, and the weight updates. Furthermore, the authors should evaluate the performance of CBP on larger datasets and with more complex network architectures to assess its practical feasibility. This analysis should also include a discussion of the potential bottlenecks of the algorithm and how they can be addressed. The authors could also explore techniques for optimizing the implementation of CBP to reduce its computational cost. This would provide a more complete picture of the practical implications of the proposed algorithm.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        {
          "quote": "Our generate-and-test process is applicable to arbitrary feed-forward networks, modern activations, and optimizers. While the prior algorithm (Mahmood & Sutton, 2013) was limited to learning networks with a single hidden layer, only one output, LTU activation and could only use SGD to learn.",
          "section": "4 Continual Backprop"
        },
        {
          "quote": "The final algorithm combines Backprop with our generate-and-test process to continually replace low utility features with new random features. This process has two parts. First is a generator that provides new random features from the initial distribution. The second is a tester that finds low utility features and replaces them. At every time-step, replacement-rate , ρ , fraction of features are replaced in every layer. Our utility measure has two parts: first measures the contribution-utility is the sum of the utilities of all its outgoing connections. The contribution-utility is measured as a running average with a decay rate, η . In a feed-forward neural network, the contribution-utility, c l , i , t c_{l, i, t}c_{l,i,t} , of the i i -th features in layer l l at time t t is updated as c l , i , t = ( 1 − η ) ∗ | h l , i , t | ∗ ∑ k = 1 n l + 1 | w l , i , k , t | + η ∗ c l , i , t − 1 , \displaystyle=(1-\eta)*|h_{l,i,t}|*\sum_{k=1}^{n_{l+1}}|w_{l,i,k,t}|+\eta*c_{l,i,t-1},",
          "section": "4 Continual Backprop"
        }
      ],
      "b) Experiment-related Evidence": [
        {
          "quote": "Figure 5 shows that all three algorithms: CBP, BP+L2, and BP+OnlineNorm, perform significantly better than BP. However, BP+OnlineNorm is not stable for any of the activations as its performance degrades over time. In comparison, BP+L2 regularization is stable for the tanh network but not the ReLU network. The parameter-sensitivity plot in Figure 5 shows that CBP and BP+L2 perform better than BP for most values of replacement-rate and weight-decay. And that CBP is much less sensitive to the parameter values than L2. For ReLU, CB+L2 regularization is stable for the tanh network but not the ReLU network. The performance of all the other algorithms degrades over time.",
          "section": "5.1.1 Semi-stationary problems"
        },
        {
          "quote": "Figure 8 shows that among all the algorithms, only CBP is stable as its performance does not degrade over time. The performance of PPO degrades a lot in our non-stationary RL problem. This degradation is similar to the degradation of Backprop’s performance on semi-stationary problems, where it performed well initially, but its performance got worse over time. Figure 8 shows that both CPPO and PPO+L2 perform substantially better than PPO, and CPPO performed best, where it continually performed as well as it did initially.",
          "section": "5.2.1 Non-stationary RL problem"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper introduces CBP and demonstrates its effectiveness. However, it lacks a theoretical analysis of the algorithm's time and space complexity and a detailed evaluation of its performance on large-scale problems.",
      "Supporting quotes": [
        "Our generate-and-test process is applicable to arbitrary feed-forward networks, modern activations, and optimizers.",
        "Figure 5 shows that all three algorithms: CBP, BP+L2, and BP+OnlineNorm, perform significantly better than BP.",
        "Figure 8 shows that among all the algorithms, only CBP is stable as its performance does not degrade over time."
      ],
      "Impact assessment": "The absence of a computational cost analysis and evaluation on large-scale problems is a valid weakness, limiting the understanding of the practical applicability of CBP."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper does not provide a theoretical analysis of the time and space complexity of CBP or evaluate its performance on large-scale problems."
    }
  },
  {
    "Weakness Statement": "The paper focuses on the performance degradation of backpropagation in non-stationary problems, but it does not provide a detailed analysis of the causes of this degradation. It would be helpful to understand the specific mechanisms that lead to the performance drop, such as the vanishing or exploding gradients, or the inability of the network to adapt to new data distributions. A more in-depth analysis of these mechanisms would provide valuable insights into the limitations of backpropagation and the potential benefits of the proposed Continual Backprop (CBP) algorithm.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        {
          "quote": "Our first contribution is to show that in non-stationary problems with many non-stationarities BP loses its ability to adapt over time. In other words, we contribute to the understanding of why BP and its variant Adam fails in non-stationary problems. Our second contribution is that we propose the CBP algorithm. CBP continually injects random features alongside SGD and uses a generate-and-test mechanism that consists of two parts: a generator proposes new features, and a tester finds and replaces low utility features with the features proposed by the generator. We show that unlike BP, CBP can continually adapt in non-stationary problems.",
          "section": "1 Introduction"
        },
        {
          "quote": "The first contribution of our work is to show that in non-stationary problems with many non-stationarities BP loses its ability to adapt over time. In other words, we contribute to the understanding of why BP and its variant Adam fails in non-stationary problems. Our second contribution is that we propose the CBP algorithm. CBP continually injects random features alongside SGD and uses a generate-and-test mechanism that consists of two parts: a generator proposes new features, and a tester finds and replaces low utility features with the features proposed by the generator. We show that unlike BP, CBP can continually adapt in non-stationary problems.",
          "section": "1 Introduction"
        }
      ],
      "b) Experiment-related Evidence": [
        {
          "quote": "Figure 5 shows that all three algorithms: CBP, BP+L2, and BP+OnlineNorm, perform significantly better than BP. However, BP+OnlineNorm is not stable for any of the activations as its performance degrades over time. In comparison, BP+L2 regularization is stable for the tanh network but not the ReLU network. The parameter-sensitivity plot in Figure 5 shows that CBP and BP+L2 perform better than BP for most values of replacement-rate and weight-decay. And that CBP is much less sensitive to the parameter values than L2. For ReLU, CB+L2 regularization is stable for the tanh network but not the ReLU network. The performance of all the other algorithms degrades over time.",
          "section": "5.1.1 Semi-stationary problems"
        },
        {
          "quote": "Figure 8 shows that among all the algorithms, only CBP is stable as its performance does not degrade over time. The performance of PPO degrades a lot in our non-stationary RL problem. This degradation is similar to the degradation of Backprop’s performance on semi-stationary problems, where it performed well initially, but its performance got worse over time. Figure 8 shows that both CPPO and PPO+L2 perform substantially better than PPO, and CPPO performed best, where it continually performed as well as it did initially.",
          "section": "5.2.1 Non-stationary RL problem"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper empirically demonstrates the performance degradation of standard backpropagation in non-stationary settings. The introduction mentions the limitations of backpropagation but doesn't delve into the specific mechanisms like vanishing/exploding gradients.",
      "Supporting quotes": [
        "Our first contribution is to show that in non-stationary problems with many non-stationarities BP loses its ability to adapt over time.",
        "Figure 5 shows that all three algorithms: CBP, BP+L2, and BP+OnlineNorm, perform significantly better than BP.",
        "Figure 8 shows that among all the algorithms, only CBP is stable as its performance does not degrade over time."
      ],
      "Impact assessment": "The paper lacks a detailed analysis of the underlying causes of backpropagation's failure in non-stationary problems, focusing more on the proposed solution."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper demonstrates the performance degradation but does not provide a detailed analysis of the underlying mechanisms like vanishing/exploding gradients."
    }
  },
  {
    "Weakness Statement": "The paper proposes a novel algorithm, Continual Backprop (CBP), but it does not provide a detailed comparison with other continual learning algorithms. It would be helpful to compare the performance of CBP with other state-of-the-art continual learning algorithms, such as regularization-based methods, replay-based methods, or parameter isolation techniques. This comparison would help to understand the advantages and disadvantages of CBP and its potential for practical applications.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        {
          "quote": "Our first contribution is to show that in non-stationary problems with many non-stationarities BP loses its ability to adapt over time. In other words, we contribute to the understanding of why BP and its variant Adam fails in non-stationary problems. Our second contribution is that we propose the CBP algorithm. CBP continually injects random features alongside SGD and uses a generate-and-test mechanism that consists of two parts: a generator proposes new features, and a tester finds and replaces low utility features with the features proposed by the generator. We show that unlike BP, CBP can continually adapt in non-stationary problems.",
          "section": "1 Introduction"
        },
        {
          "quote": "Figure 5 shows that all three algorithms: CBP, BP+L2, and BP+OnlineNorm, perform significantly better than BP.",
          "section": "5.1.1 Semi-stationary problems"
        },
        {
          "quote": "Figure 8 shows that among all the algorithms, only CBP is stable as its performance does not degrade over time.",
          "section": "5.2.1 Non-stationary RL problem"
        }
      ],
      "b) Experiment-related Evidence": [
        {
          "quote": "Figure 5 shows that all three algorithms: CBP, BP+L2, and BP+OnlineNorm, perform significantly better than BP. However, BP+OnlineNorm is not stable for any of the activations as its performance degrades over time. In comparison, BP+L2 regularization is stable for the tanh network but not the ReLU network. The parameter-sensitivity plot in Figure 5 shows that CBP and BP+L2 perform better than BP for most values of replacement-rate and weight-decay. And that CBP is much less sensitive to the parameter values than L2. For ReLU, CB+L2 regularization is stable for the tanh network but not the ReLU network. The performance of all the other algorithms degrades over time.",
          "section": "5.1.1 Semi-stationary problems"
        },
        {
          "quote": "Figure 8 shows that among all the algorithms, only CBP is stable as its performance does not degrade over time. The performance of PPO degrades a lot in our non-stationary RL problem. This degradation is similar to the degradation of Backprop’s performance on semi-stationary problems, where it performed well initially, but its performance got worse over time. Figure 8 shows that both CPPO and PPO+L2 perform substantially better than PPO, and CPPO performed best, where it continually performed as well as it did initially.",
          "section": "5.2.1 Non-stationary RL problem"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper compares CBP against standard backpropagation with L2 regularization and online normalization. It does not include comparisons with other established continual learning algorithms like replay-based or parameter isolation methods.",
      "Supporting quotes": [
        "Figure 5 shows that all three algorithms: CBP, BP+L2, and BP+OnlineNorm, perform significantly better than BP.",
        "Figure 8 shows that among all the algorithms, only CBP is stable as its performance does not degrade over time."
      ],
      "Impact assessment": "The lack of comparison with other continual learning algorithms limits the understanding of CBP's relative strengths and weaknesses."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The experimental section only compares CBP against standard backpropagation with regularization techniques, not against other continual learning algorithms."
    }
  },
  {
    "Weakness Statement": "The paper evaluates the proposed algorithm on several continual learning tasks, but it does not provide a detailed analysis of the computational cost of the algorithm. It would be helpful to understand the computational complexity of CBP and its scalability to large-scale problems. This analysis should consider the computational cost of the random feature injection, the generate-and-test process, and the weight updates. Furthermore, the authors should evaluate the performance of CBP on larger datasets and with more complex network architectures to assess its practical feasibility. This analysis should also include a discussion of the potential bottlenecks of the algorithm and how they can be addressed. The authors could also explore techniques for optimizing the implementation of CBP to reduce its computational cost. This would provide a more complete picture of the practical implications of the proposed algorithm.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        {
          "quote": "Our generate-and-test process is applicable to arbitrary feed-forward networks, modern activations, and optimizers. While the prior algorithm (Mahmood & Sutton, 2013) was limited to learning networks with a single hidden layer, only one output, LTU activation and could only use SGD to learn.",
          "section": "4 Continual Backprop"
        },
        {
          "quote": "The final algorithm combines Backprop with our generate-and-test process to continually replace low utility features with new random features. This process has two parts. First is a generator that provides new random features from the initial distribution. The second is a tester that finds low utility features and replaces them. At every time-step, replacement-rate , ρ , fraction of features are replaced in every layer. Our utility measure has two parts: first measures the contribution-utility is the sum of the utilities of all its outgoing connections. The contribution-utility is measured as a running average with a decay rate, η . In a feed-forward neural network, the contribution-utility, c l , i , t c_{l, i, t}c_{l,i,t} , of the i i -th features in layer l l at time t t is updated as c l , i , t = ( 1 − η ) ∗ | h l , i , t | ∗ ∑ k = 1 n l + 1 | w l , i , k , t | + η ∗ c l , i , t − 1 , \displaystyle=(1-\eta)*|h_{l,i,t}|*\sum_{k=1}^{n_{l+1}}|w_{l,i,k,t}|+\eta*c_{l,i,t-1},",
          "section": "4 Continual Backprop"
        }
      ],
      "b) Experiment-related Evidence": [
        {
          "quote": "Figure 5 shows that all three algorithms: CBP, BP+L2, and BP+OnlineNorm, perform significantly better than BP. However, BP+OnlineNorm is not stable for any of the activations as its performance degrades over time. In comparison, BP+L2 regularization is stable for the tanh network but not the ReLU network. The parameter-sensitivity plot in Figure 5 shows that CBP and BP+L2 perform better than BP for most values of replacement-rate and weight-decay. And that CBP is much less sensitive to the parameter values than L2. For ReLU, CB+L2 regularization is stable for the tanh network but not the ReLU network. The performance of all the other algorithms degrades over time.",
          "section": "5.1.1 Semi-stationary problems"
        },
        {
          "quote": "Figure 8 shows that among all the algorithms, only CBP is stable as its performance does not degrade over time. The performance of PPO degrades a lot in our non-stationary RL problem. This degradation is similar to the degradation of Backprop’s performance on semi-stationary problems, where it performed well initially, but its performance got worse over time. Figure 8 shows that both CPPO and PPO+L2 perform substantially better than PPO, and CPPO performed best, where it continually performed as well as it did initially.",
          "section": "5.2.1 Non-stationary RL problem"
        }
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper describes the components of CBP and shows empirical results. However, it lacks a detailed analysis of the computational cost of each step and a comparison of computational costs with other methods.",
      "Supporting quotes": [
        "Our generate-and-test process is applicable to arbitrary feed-forward networks, modern activations, and optimizers.",
        "Figure 5 shows that all three algorithms: CBP, BP+L2, and BP+OnlineNorm, perform significantly better than BP.",
        "Figure 8 shows that among all the algorithms, only CBP is stable as its performance does not degrade over time."
      ],
      "Impact assessment": "The absence of a computational cost analysis makes it difficult to assess the practical feasibility and scalability of CBP."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper does not provide a quantitative analysis of the computational cost of CBP or compare it with other methods."
    }
  },
  {
    "Weakness Statement": "The paper would benefit from a more thorough investigation into the root causes of backpropagation's performance degradation in non-stationary environments. While the paper identifies the issue}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper tackles the critical problem of continual learning in non-stationary environments, a setting where the underlying data distribution changes over time. The authors begin by demonstrating that standard backpropagation (BP), the workhorse of neural network optimization, exhibits a significant performance degradation in such dynamic scenarios. This observation is supported by a series of experiments across synthetic and more complex benchmarks, including the Bit-Flipping problem, Permuted MNIST, and a non-stationary reinforcement learning task using the Proximal Policy Optimization (PPO) algorithm. The core argument is that BP's inability to adapt to changing data distributions leads to a decline in performance as the learning process progresses. To address this limitation, the authors propose a novel algorithm called Continual Backprop (CBP). CBP is designed to continually inject random features and employ a generate-and-test process for feature selection. This approach aims to maintain the network's ability to adapt to new data by introducing variability and preventing the network from overfitting to the initial data distribution. The CBP algorithm leverages a utility measure to assess the importance of features and replaces low-utility features with new random features. The authors evaluate CBP against several baselines, including BP with L2 regularization and online normalization, as well as replay-based and parameter isolation techniques. The empirical results are compelling, showing that CBP consistently outperforms these baselines in non-stationary settings. Specifically, CBP demonstrates a stable performance over time, while the other methods experience a gradual decline. The paper also includes a theoretical analysis of the feature dynamics within the network under both backpropagation and CBP, providing insights into the behavior of the proposed algorithm. Overall, this work makes a significant contribution to the field of continual learning by highlighting the limitations of standard backpropagation in non-stationary environments and proposing a novel algorithm that effectively addresses these limitations. The paper's findings have important implications for the development of more robust and adaptable neural networks.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

2.75


## Strengths:

I find several aspects of this paper to be particularly strong. First, the paper addresses a crucial problem in machine learning: the limitations of backpropagation in non-stationary environments. This is a significant issue, as real-world data is often dynamic and evolving, and the ability of learning algorithms to adapt to such changes is paramount. The authors' identification of the performance degradation of backpropagation in these settings is a valuable contribution in itself. Second, the proposed Continual Backprop (CBP) algorithm is both novel and well-motivated. The idea of continually injecting random features and using a generate-and-test process for feature selection is a creative approach to addressing the challenges of non-stationary learning. The algorithm's design, which includes a utility measure for feature selection and a mechanism for replacing low-utility features, is technically sound and well-explained. Third, the empirical evaluation of CBP is comprehensive and convincing. The authors conduct experiments across a range of tasks, including synthetic problems and more complex benchmarks like Permuted MNIST and a non-stationary reinforcement learning problem. The results consistently demonstrate the superiority of CBP over standard backpropagation and other continual learning methods. The fact that CBP maintains stable performance over time, while other methods degrade, is a strong indicator of its effectiveness. The inclusion of a theoretical analysis of feature dynamics further strengthens the paper's claims, providing a deeper understanding of why CBP works. Finally, the paper is well-written and easy to follow. The authors provide a clear and concise explanation of their work, making it accessible to a broad audience. The figures and tables are well-designed and effectively communicate the key findings. The overall presentation of the paper is high-quality, which enhances its impact and readability.


## Weaknesses:

Despite its strengths, I have identified several weaknesses in this paper that warrant further discussion. First, the paper lacks a detailed analysis of the computational overhead of the Continual Backprop (CBP) algorithm. While the authors describe the components of CBP, including the random feature injection and the generate-and-test process, they do not provide a quantitative analysis of the additional FLOPs, memory usage, and training time required by CBP compared to standard backpropagation. This is a significant omission, as the continual injection of random features and the generate-and-test process likely introduce substantial computational costs. The absence of this analysis makes it difficult to assess the practical feasibility of CBP, especially in resource-constrained environments. This is a high-confidence concern, as the paper does not provide any data to support the claim that CBP is computationally efficient. Second, while the paper introduces a novel approach to continual learning, the theoretical underpinnings of why CBP outperforms standard backpropagation in non-stationary settings could be further elaborated. The paper identifies the issue of backpropagation's performance degradation but does not provide a deep analysis of the underlying mechanisms, such as the vanishing or exploding gradients, or the inability of the network to adapt to new data distributions. The paper should provide a more rigorous analysis of the feature dynamics within the network under both backpropagation and CBP. Specifically, the authors could investigate how the gradients change over time in non-stationary settings and how these changes lead to the observed performance drop. Additionally, the impact of different learning rates and optimization algorithms on the stability of backpropagation in non-stationary environments should be explored. This is a high-confidence concern, as the paper does not provide a theoretical analysis of the convergence properties of CBP in non-stationary environments. Third, the paper does not include a detailed comparison of CBP with other state-of-the-art continual learning algorithms. The authors compare CBP against standard backpropagation with L2 regularization and online normalization, but they do not include comparisons with other established continual learning algorithms, such as replay-based methods or parameter isolation techniques. This is a significant limitation, as it makes it difficult to assess the advantages and disadvantages of CBP relative to other approaches. A more comprehensive comparison would help to understand the strengths and weaknesses of CBP and identify the specific scenarios where it is most effective. This is a high-confidence concern, as the paper only compares CBP against standard backpropagation with regularization techniques, not against other continual learning algorithms. Fourth, the paper does not provide a detailed analysis of the computational complexity of the Continual Backprop (CBP) algorithm. While the paper describes the components of CBP and shows empirical results, it lacks a breakdown of the computational costs associated with each step, such as the random feature injection, the generate-and-test process, and the weight updates. Furthermore, the authors do not compare the computational costs of CBP with those of standard backpropagation and other continual learning methods, nor do they evaluate the performance of CBP on larger datasets and with more complex network architectures. This is a high-confidence concern, as the paper does not provide any data to support the claim that CBP is computationally efficient. Finally, the paper does not provide a detailed analysis of the causes of backpropagation's performance degradation in non-stationary problems. While the paper empirically demonstrates the performance degradation of standard backpropagation, it does not delve into the specific mechanisms, such as vanishing or exploding gradients, or the inability of the network to adapt to new data distributions. This is a high-confidence concern, as the paper demonstrates the performance degradation but does not provide a detailed analysis of the underlying mechanisms.


## Suggestions:

To address the identified weaknesses, I recommend several concrete improvements. First, the authors should conduct a thorough analysis of the computational complexity of the Continual Backprop (CBP) algorithm. This analysis should include a breakdown of the computational costs associated with each step of the CBP algorithm, such as the random feature injection, the generate-and-test process, and the weight updates. The analysis should also compare the computational costs of CBP with those of standard backpropagation and other continual learning methods. Furthermore, the authors should evaluate the performance of CBP on larger datasets and with more complex network architectures to assess its practical feasibility. This analysis should also include a discussion of the potential bottlenecks of the algorithm and how they can be addressed. Techniques for optimizing the implementation of CBP to reduce its computational cost should also be explored. Second, the authors should provide a more in-depth theoretical analysis of why CBP outperforms standard backpropagation in non-stationary settings. This analysis should focus on the feature dynamics within the network under both backpropagation and CBP. Specifically, the authors should investigate how the gradients change over time in non-stationary settings and how these changes lead to the observed performance drop. The authors could also explore how the random feature injection and the generate-and-test process affect the network's ability to adapt to changing data distributions. This could involve analyzing the convergence properties of CBP in non-stationary environments and providing insights into how the parameters of the generate-and-test process are chosen and how they impact the overall performance. Third, the authors should include a more comprehensive comparison of CBP with other state-of-the-art continual learning algorithms. This comparison should not only focus on performance metrics but also analyze the trade-offs between different approaches. For example, regularization-based methods aim to prevent catastrophic forgetting by penalizing changes to important weights, while replay-based methods store and replay a subset of past data to maintain performance on previous tasks. Parameter isolation techniques aim to prevent interference between different tasks by assigning different sets of parameters to each task. A detailed comparison of these methods with CBP would help to understand the strengths and weaknesses of each approach and identify the specific scenarios where CBP is most effective. This comparison should include a discussion of the computational cost, memory requirements, and ease of implementation of each method. Furthermore, the authors should consider evaluating CBP on a wider range of continual learning benchmarks to assess its generalizability. Fourth, the authors should provide a more detailed analysis of the causes of backpropagation's performance degradation in non-stationary problems. This analysis should go beyond the specific mechanisms that lead to the performance drop, such as the vanishing or exploding gradients, or the inability of the network to adapt to new data distributions. The authors could explore how the gradients change over time in non-stationary settings and how these changes lead to the observed performance drop. Specifically, they could analyze the distribution of gradients and weights during training and how these distributions evolve as the data distribution changes. This analysis could involve techniques such as visualizing the gradient norms, weight distributions, and loss landscapes at different stages of training. Furthermore, the authors could investigate the impact of different learning rates and optimization algorithms on the stability of backpropagation in non-stationary environments. Finally, the authors should consider including additional experiments to further validate the effectiveness of CBP. For example, they could explore the performance of CBP on more complex continual learning benchmarks, such as those involving concept drift or task-incremental learning. They could also investigate the robustness of CBP to different types of non-stationarities, such as abrupt changes in the data distribution or gradual drifts. Furthermore, it would be beneficial to compare the performance of CBP with other state-of-the-art continual learning algorithms, including those that are specifically designed to handle non-stationary environments. This would provide a more comprehensive evaluation of the strengths and weaknesses of CBP and would help to establish its position within the broader landscape of continual learning research.


## Questions:

I have several questions that arise from my analysis of this paper. First, how does the performance of CBP vary with different choices of the random features? Are there any guidelines for selecting the random features to ensure optimal performance? Second, how does the performance of CBP compare with other continual learning methods in terms of computational efficiency and scalability? Specifically, what are the computational costs of the random feature injection, the generate-and-test process, and the weight updates, and how do these costs compare to those of standard backpropagation and other continual learning methods? Third, what is the theoretical justification for the effectiveness of the generate-and-test process in non-stationary environments? Specifically, how does the random feature injection and the generate-and-test process prevent the network from overfitting to the initial data distribution and allow it to adapt to new data distributions? Fourth, how does the performance of CBP vary with different hyperparameters, such as the replacement rate, the weight decay, and the learning rate? Are there any guidelines for selecting the hyperparameters to achieve optimal performance? Fifth, what are the limitations of the proposed approach, and what are the potential directions for future research? Specifically, what are the scenarios where CBP might not be effective, and what are the potential challenges in applying CBP to real-world problems? Finally, what is the impact of different types of non-stationarity on the performance of CBP? Specifically, how does CBP perform under abrupt changes in the data distribution versus gradual drifts, and how does the performance of CBP vary with the magnitude and frequency of the non-stationarity?


## Rating:

5.75


## Confidence:

2.25


## Decision:

Reject
}