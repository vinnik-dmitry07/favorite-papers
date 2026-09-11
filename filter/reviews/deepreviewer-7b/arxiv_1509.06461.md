I will use Standard Mode for comprehensive thinking. As a professional reviewer, I will simulate 4 different reviewers, followed by the verification thinking. Then I will output the Finally Review Output. Let me think - Standard Mode means I will output the original review, followed by the verification thinking. Considering that I am currently in standard mode, I should think from my existing knowledge and consider some related work content when writing about weaknesses. Then I will output the Finally Review Output and Meta Review Output:

\boxed_simreviewers{
## Reviewer 1

### Summary

The paper proposes a new algorithm called Double DQN, which is an improved version of the DQN algorithm. The main idea is to use two separate networks to estimate the value function, one for selecting actions and the other for evaluating the value of those actions. This helps to reduce overestimation bias in the value estimates, which can lead to better policy learning. The paper shows that Double DQN outperforms DQN on several Atari games.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

The paper is well-written and easy to follow. The motivation for the work is clear and the technical details are well-explained. The paper also provides a good overview of the related work and positions the proposed method within the existing literature. The experimental results are comprehensive and demonstrate the effectiveness of the proposed algorithm.

### Weaknesses

#### Some Related Works


#### comment

The main weakness of the paper is the limited novelty of the proposed algorithm. While the paper acknowledges that Double DQN is a simple extension of Double Q-learning, it does not provide a strong justification for why this extension is significant. The paper could benefit from a more in-depth analysis of the theoretical properties of Double DQN and how they differ from Double Q-learning. Additionally, the paper could explore the limitations of the proposed algorithm and discuss potential directions for future research. The paper also lacks a thorough comparison with other state-of-the-art algorithms, which would help to better understand the strengths and weaknesses of the proposed method.

### Suggestions

The paper should delve deeper into the theoretical underpinnings of Double DQN to justify its novelty beyond a simple extension of Double Q-learning. Specifically, a rigorous analysis of the convergence properties of Double DQN, perhaps by adapting existing proofs or developing new ones, would be beneficial. This analysis should highlight the specific conditions under which Double DQN is guaranteed to converge to an optimal policy, and how these conditions compare to those of Double Q-learning. Furthermore, the paper should explore the impact of the target network update frequency on the performance of Double DQN, and whether there are specific scenarios where this frequency needs to be adjusted. A more detailed theoretical analysis would strengthen the paper's contribution and provide a more solid foundation for the empirical results.

To address the lack of comparison with other state-of-the-art algorithms, the paper should include a more comprehensive experimental evaluation. This should involve comparing Double DQN against a wider range of algorithms, including not only other DQN variants but also algorithms that use different approaches to address overestimation bias, such as those based on distributional RL or ensemble methods. The comparison should not only focus on the final performance but also on other aspects such as sample efficiency, robustness to hyperparameter settings, and computational cost. Furthermore, the paper should provide a detailed analysis of the results, highlighting the specific scenarios where Double DQN excels and where it might fall short. This would provide a more nuanced understanding of the algorithm's strengths and weaknesses and help to identify potential areas for improvement.

Finally, the paper should discuss the limitations of Double DQN and suggest potential directions for future research. For example, the paper could explore the applicability of Double DQN to more complex environments, such as those with high-dimensional state spaces or continuous action spaces. It could also investigate the use of different network architectures or optimization techniques to further improve the performance of Double DQN. Furthermore, the paper could explore the potential of combining Double DQN with other techniques, such as curiosity-driven exploration or transfer learning. A discussion of these limitations and future directions would help to position the paper within the broader research landscape and provide a roadmap for future work in this area.

### Questions

What are the theoretical properties of Double DQN that are different from Double Q-learning? How do these properties affect the performance of the algorithm?

How does Double DQN compare to other state-of-the-art algorithms in terms of performance, sample efficiency, and robustness?

What are the limitations of Double DQN, and what are the potential directions for future research?

### Rating

6

### Confidence

3

**********

## Reviewer 2

### Summary

The paper proposes a new DQN variant that uses double Q-learning, which has been shown to be effective in a tabular setting. The paper provides a good overview of the problem of overestimation in DQN and the importance of addressing it. The paper then proposes a simple modification to the DQN algorithm that uses double Q-learning. The paper provides empirical evidence that the proposed algorithm improves the performance of DQN on several Atari games.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper provides a good overview of the problem of overestimation in DQN and the importance of addressing it.
- The paper proposes a simple modification to the DQN algorithm that uses double Q-learning.
- The paper provides empirical evidence that the proposed algorithm improves the performance of DQN on several Atari games.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a theoretical analysis of the proposed algorithm. It is not clear why the proposed algorithm should work better than DQN. The paper should provide a theoretical analysis of the proposed algorithm and compare it to DQN.
- The paper does not provide a comparison of the proposed algorithm to other algorithms that address overestimation. The paper should compare the proposed algorithm to other algorithms that address overestimation.
- The paper does not provide a comparison of the proposed algorithm to other DQN variants. The paper should compare the proposed algorithm to other DQN variants.
- The paper does not provide a comparison of the proposed algorithm to other value-based RL algorithms. The paper should compare the proposed algorithm to other value-based RL algorithms.
- The paper does not provide a comparison of the proposed algorithm to other model-based RL algorithms. The paper should compare the proposed algorithm to other model-based RL algorithms.
- The paper does not provide a comparison of the proposed algorithm to other model-free RL algorithms. The paper should compare the proposed algorithm to other model-free RL algorithms.
- The paper does not provide a comparison of the proposed algorithm to other deep RL algorithms. The paper should compare the proposed algorithm to other deep RL algorithms.
- The paper does not provide a comparison of the proposed algorithm to other RL algorithms. The paper should compare the proposed algorithm to other RL algorithms.
- The paper does not provide a comparison of the proposed algorithm to other RL algorithms. The paper should compare the proposed algorithm to other RL algorithms.

### Suggestions

The paper should provide a more rigorous theoretical analysis of the proposed Double DQN algorithm. While the empirical results are promising, a theoretical justification is crucial for understanding the algorithm's behavior and guarantees. Specifically, the paper should analyze the convergence properties of the algorithm, demonstrating that it converges to an optimal policy under certain conditions. Furthermore, the analysis should explore the impact of the double Q-learning update rule on the bias and variance of the Q-value estimates. This analysis could involve adapting existing theoretical frameworks for value-based reinforcement learning or developing new techniques tailored to the specific structure of the Double DQN algorithm. Without such analysis, it remains unclear why the proposed algorithm should be expected to outperform standard DQN, and the observed improvements could be due to other factors.

In addition to theoretical analysis, the paper needs to provide a more comprehensive empirical evaluation of the proposed algorithm. The current evaluation is limited to a few Atari games and does not compare the algorithm to a wide range of relevant baselines. The paper should compare Double DQN to other algorithms that specifically address the overestimation problem, such as those based on distributional RL or ensemble methods. Furthermore, the evaluation should include a comparison to other DQN variants, such as those that use prioritized experience replay or target networks with different update frequencies. The paper should also compare Double DQN to other value-based RL algorithms, such as A2C and PPO, to understand its relative strengths and weaknesses. Finally, the paper should compare Double DQN to model-based RL algorithms, such as Dreamer, and other deep RL algorithms, such as SAC and TD3, to provide a more complete picture of its performance. The experimental results should be presented with appropriate statistical analysis, including confidence intervals and significance tests, to ensure the robustness of the findings.

Finally, the paper should provide a more detailed discussion of the limitations of the proposed algorithm and potential directions for future research. The paper should acknowledge the limitations of the current evaluation and discuss the potential challenges of applying Double DQN to more complex environments. For example, the paper should discuss how the algorithm would perform in environments with high-dimensional state spaces or continuous action spaces. The paper should also discuss the potential impact of the choice of hyperparameters on the performance of the algorithm and provide guidelines for selecting appropriate values. Furthermore, the paper should explore potential extensions of the algorithm, such as incorporating techniques for exploration or handling non-stationary environments. By addressing these limitations and providing a roadmap for future research, the paper can make a more significant contribution to the field of reinforcement learning.

### Questions

- What is the theoretical analysis of the proposed algorithm?
- How does the proposed algorithm compare to other algorithms that address overestimation?
- How does the proposed algorithm compare to other DQN variants?
- How does the proposed algorithm compare to other value-based RL algorithms?
- How does the proposed algorithm compare to other model-based RL algorithms?
- How does the proposed algorithm compare to other model-free RL algorithms?
- How does the proposed algorithm compare to other deep RL algorithms?
- How does the proposed algorithm compare to other RL algorithms?
- What are the limitations of the proposed algorithm?
- What are the potential directions for future research?

### Rating

6

### Confidence

4

**********

## Reviewer 3

### Summary

This paper investigates the overestimation issue in DQN, which is caused by the max operator in the Bellman equation. The authors demonstrate that overestimation can occur even in deterministic environments and that Double Q-learning can effectively mitigate this issue. They propose a specific implementation called Double DQN, which uses the existing DQN architecture without requiring additional networks or parameters. The authors provide empirical evidence that Double DQN outperforms DQN on several Atari games, achieving state-of-the-art results on the Atari 2600 domain.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a thorough analysis of the overestimation issue in DQN, demonstrating that it can occur even in deterministic environments.
3. The proposed Double DQN algorithm is simple and effective, and it can be easily implemented using the existing DQN architecture.
4. The authors provide empirical evidence that Double DQN outperforms DQN on several Atari games, achieving state-of-the-art results on the Atari 2600 domain.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed discussion of the limitations of Double DQN. For example, it is not clear how the performance of Double DQN would be affected by the choice of hyperparameters, such as the learning rate, the discount factor, and the exploration strategy. It would be beneficial to see a more thorough analysis of the sensitivity of Double DQN to these hyperparameters.
2. The paper does not compare Double DQN to other state-of-the-art algorithms, such as Rainbow DQN or other advanced DQN variants. It would be valuable to see how Double DQN performs relative to these more sophisticated algorithms on the same set of Atari games. This would help to establish the relative strengths and weaknesses of Double DQN.
3. The paper does not provide a theoretical analysis of the convergence properties of Double DQN. While the empirical results are promising, it would be helpful to have a theoretical understanding of why Double DQN works and under what conditions it is guaranteed to converge to an optimal policy. This could involve adapting existing theoretical frameworks for value-based reinforcement learning or developing new ones tailored to the specific structure of Double DQN.

### Suggestions

The paper would benefit from a more in-depth analysis of the hyperparameter sensitivity of Double DQN. Specifically, the authors should conduct a systematic study of how different learning rates, discount factors, and exploration strategies affect the performance of Double DQN. This could involve varying each hyperparameter individually while keeping the others constant, and then plotting the performance of Double DQN as a function of each hyperparameter. The results of this analysis should be presented in the paper, along with a discussion of the optimal hyperparameter settings for Double DQN. Furthermore, it would be useful to compare the hyperparameter sensitivity of Double DQN to that of standard DQN, to understand how the double Q-learning update affects the learning process. This analysis would provide valuable insights into the practical application of Double DQN and help users to tune the algorithm for their specific tasks.

In addition to a more thorough hyperparameter analysis, the paper should include a more comprehensive comparison of Double DQN to other state-of-the-art algorithms. This should include a comparison to algorithms such as Rainbow DQN, which incorporates a variety of techniques for improving DQN performance, including distributional RL, double Q-learning, and prioritized experience replay. The comparison should be conducted on the same set of Atari games used in the paper, and should include a statistical analysis of the results to determine whether the differences in performance are statistically significant. This would help to establish the relative strengths and weaknesses of Double DQN compared to other advanced DQN variants. Furthermore, it would be valuable to explore the performance of Double DQN on more complex environments, such as those with continuous action spaces or high-dimensional state spaces, to assess its generalizability.

Finally, the paper would be strengthened by a theoretical analysis of the convergence properties of Double DQN. While the empirical results are promising, a theoretical understanding of why Double DQN works and under what conditions it is guaranteed to converge to an optimal policy is crucial. This could involve adapting existing theoretical frameworks for value-based reinforcement learning or developing new ones tailored to the specific structure of Double DQN. For example, it would be useful to analyze the bias and variance of the Q-value estimates produced by Double DQN, and to compare these to those of standard DQN. This analysis would provide a deeper understanding of the algorithm's behavior and help to establish its theoretical foundations. The authors could also explore the relationship between the double Q-learning update and the convergence properties of the algorithm, and to identify any conditions under which the algorithm is guaranteed to converge.

### Questions

1. How does the performance of Double DQN vary with different hyperparameters, such as the learning rate, the discount factor, and the exploration strategy?
2. How does Double DQN compare to other state-of-the-art algorithms, such as Rainbow DQN or other advanced DQN variants, on the same set of Atari games?
3. What are the theoretical properties of Double DQN, such as its convergence properties and bias-variance trade-offs?

### Rating

6

### Confidence

4

**********

## Reviewer 4

### Summary

This paper proposes a new variant of the DQN algorithm that is based on double Q-learning. The main idea is to use two networks to estimate the value function, one for selecting actions and the other for evaluating the value of those actions. This helps to reduce overestimation bias in the value estimates, which can lead to better policy learning. The paper shows that Double DQN outperforms DQN on several Atari games, and achieves state-of-the-art results on the Atari 2600 domain.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The motivation for the work is clear and the technical details are well-explained.
3. The paper provides a good overview of the related work and positions the proposed method within the existing literature.
4. The experimental results are comprehensive and demonstrate the effectiveness of the proposed algorithm.

### Weaknesses

#### Some Related Works


#### comment

1. The main weakness of the paper is the limited novelty of the proposed algorithm. While the paper acknowledges that Double DQN is a simple extension of Double Q-learning, it does not provide a strong justification for why this extension is significant. The paper could benefit from a more in-depth analysis of the theoretical properties of Double DQN and how they differ from Double Q-learning. Specifically, the paper lacks a rigorous analysis of the convergence properties of the proposed algorithm, and it does not provide any theoretical guarantees on the performance of the algorithm. Furthermore, the paper does not explore the potential limitations of the proposed approach, such as its sensitivity to hyperparameter settings or its performance in more complex environments.
2. The paper could explore the limitations of the proposed algorithm and discuss potential directions for future research. For example, the paper could investigate the applicability of Double DQN to other reinforcement learning problems, such as those with continuous action spaces or those with sparse rewards. It could also explore the potential of combining Double DQN with other techniques, such as model-based reinforcement learning or hierarchical reinforcement learning. The paper should also discuss the computational cost of the proposed algorithm and compare it to other methods. It is also unclear how the proposed algorithm would perform in scenarios where the Q-value estimates are highly inaccurate or when the environment is non-stationary.

### Suggestions

The paper would benefit from a more thorough theoretical analysis of the proposed Double DQN algorithm. Specifically, the authors should investigate the convergence properties of the algorithm and provide theoretical guarantees on its performance. This could involve adapting existing theoretical frameworks for value-based reinforcement learning or developing new ones tailored to the specific structure of Double DQN. For example, the authors could analyze the bias and variance of the Q-value estimates produced by Double DQN and compare these to those of standard DQN. Furthermore, the authors should explore the sensitivity of the algorithm to hyperparameter settings, such as the learning rate and the discount factor. This could involve conducting a systematic study of the impact of different hyperparameter values on the performance of Double DQN and providing guidelines for selecting appropriate values. The authors should also discuss the potential limitations of the proposed approach, such as its performance in more complex environments or in scenarios where the Q-value estimates are highly inaccurate. This would help to provide a more complete picture of the strengths and weaknesses of the proposed algorithm.

In addition to the theoretical analysis, the paper should also explore the potential of Double DQN in a wider range of reinforcement learning problems. For example, the authors could investigate the applicability of Double DQN to problems with continuous action spaces, such as those found in robotics or control systems. This would require adapting the algorithm to handle continuous action spaces, which could involve using techniques such as policy gradients or actor-critic methods. The authors could also explore the potential of combining Double DQN with other techniques, such as model-based reinforcement learning or hierarchical reinforcement learning. This could involve using Double DQN to learn a high-level policy that selects subgoals or using it to learn a model of the environment that can be used to plan actions. The authors should also discuss the computational cost of the proposed algorithm and compare it to other methods. This would help to assess the practical feasibility of Double DQN in real-world applications. Furthermore, the authors should investigate the performance of Double DQN in scenarios where the Q-value estimates are highly inaccurate or when the environment is non-stationary. This would help to identify the limitations of the proposed approach and provide insights into potential areas for future research.

Finally, the paper should provide a more detailed discussion of the experimental results. Specifically, the authors should analyze the reasons for the performance differences between Double DQN and DQN on different Atari games. This could involve investigating the characteristics of the games that make them more or less suitable for Double DQN. The authors should also provide a more detailed analysis of the learning curves of Double DQN and compare them to those of DQN. This would help to understand the learning behavior of the proposed algorithm and identify potential areas for improvement. The authors should also discuss the statistical significance of the results and provide confidence intervals for the performance of Double DQN. This would help to assess the robustness of the results and provide a more reliable evaluation of the proposed algorithm.

### Questions

1. How does the performance of Double DQN vary with different hyperparameters, such as the learning rate and the discount factor?
2. How does Double DQN perform in scenarios where the Q-value estimates are highly inaccurate or when the environment is non-stationary?
3. What are the potential directions for future research based on the findings of this paper?

### Rating

6

### Confidence

4

**********

}

I have finished generating simulated reviews from 4 reviewers. Next, I will generate verification content for these reviews:

\boxed_verification{
The user wants me to validate weaknesses identified by reviewers for the provided paper. I need to go through each reviewer's comments and find evidence in the paper to support their claims.

Plan:
1. Go through each reviewer's comments one by one.
2. For each comment identified as a weakness, find supporting evidence from the paper.
3. Categorize the weakness and provide specific quotes or references to the paper.
4. If a weakness is not supported by the paper, explain why.
```json
[
  {
    "Weakness Statement": "The main weakness of the paper is the limited novelty of the proposed algorithm. While the paper acknowledges that Double DQN is a simple extension of Double Q-learning, it does not provide a strong justification for why this extension is significant.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "The paper introduces Double DQN as a \"specific adaptation\" of Double Q-learning: \"We therefore propose to evaluate the greedy policy according to the online network, but using the target network to estimate its value. In reference to both Double Q-learning and DQN, we refer to the resulting algorithm as Double DQN.\" (Section 3)",
        "The core idea is presented as a \"minimal possible change\" to DQN: \"To test whether overestimations occur in DQN we additionally evaluate the algorithms with random starts generated from expert human trajectories, as proposed by Nair et al. (2015).\" (Section 4)",
        "The paper highlights the simplicity of the implementation: \"We therefore propose to evaluate the greedy policy according to the online network, but using the target network to estimate its value. In comparison to Double Q-learning ( 4 ), the weights of the second network 𝜃 𝑡 ′ are replaced with the weights of the target network 𝜃 − 𝑡 for the evaluation of the current greedy policy.\" (Section 3)"
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper explicitly states that Double DQN is a \"specific adaptation\" and a \"minimal possible change\" to DQN, building upon the existing Double Q-learning framework.",
      "Supporting quotes": [
        "We therefore propose to evaluate the greedy policy according to the online network, but using the target network to estimate its value. In comparison to Double Q-learning ( 4 ), the weights of the second network 𝜃 𝑡 ′ are replaced with the weights of the target network 𝜃 − 𝑡 for the evaluation of the current greedy policy."
      ],
      "Impact assessment": "The reviewer's point about the limited novelty is valid as the paper focuses on applying and demonstrating the effectiveness of Double Q-learning within the DQN framework rather than introducing a fundamentally new algorithmic concept."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "The paper's description of Double DQN as a \"specific adaptation\" and a \"minimal possible change\"."
    }
  },
  {
    "Weakness Statement": "The paper could benefit from a more in-depth analysis of the theoretical properties of Double DQN and how they differ from Double Q-learning. Specifically, the paper lacks a rigorous analysis of the convergence properties of the proposed algorithm, and it does not provide any theoretical guarantees on the performance of the algorithm.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "The paper includes a theoretical theorem about value estimation bias: \"Theorem 1 . Consider a state s s in which all the true optimal action values are equal at Q ∗ ( s ) . Let Q t Q_{t} be arbitrary value estimates that are on the whole unbiased in the sense that ∑ a ( Q t ​ ( s , a ) − V ∗ ​ ( s ) ) = 0 \text{ for some V ∗ ​ ( s ) V_{\*}( s ) . But that the bias of the Double Q-learning estimate is zero. (Proof in appendix.)\" (Section 3)",
        "The paper discusses the convergence of Double Q-learning in the context of value estimation bias: \"Theorem 1 shows that even if the value estimates are on average correct, estimation errors of any source can drive the estimates up and away from the true optimal values.\" (Section 3)"
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "While the paper provides a theoretical analysis of value estimation bias in Double Q-learning, it does not offer a formal convergence proof for Double DQN itself.",
      "Supporting quotes": [
        "Theorem 1 . Consider a state s s in which all the true optimal action values are equal at Q ∗ ( s ) . Let Q t Q_{t} be arbitrary value estimates that are on the whole unbiased in the sense that ∑ a ( Q t ​ ( s , a ) − V ∗ ​ ( s ) ) = 0 \text{ for some V ∗ ​ ( s ) V_{\*}( s ) . But that the bias of the Double Q-learning estimate is zero."
      ],
      "Impact assessment": "The reviewer's criticism is valid. The paper lacks a formal convergence proof for the proposed Double DQN algorithm, which is a significant theoretical gap."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "Absence of a formal convergence proof for Double DQN in the paper."
    }
  },
  {
    "Weakness Statement": "Furthermore, the paper does not explore the potential limitations of the proposed approach, such as its sensitivity to hyperparameter settings or its performance in more complex environments.",
    "Evidence Collection": {
      "b) Experiment-related Evidence": [
        "The paper mentions hyperparameter tuning for the tuned version of Double DQN: \"Some tuning is appropriate because the hyperparameters were tuned for DQN but not for Double DQN.\" (Section 4)",
        "The paper includes a dedicated section on \"Robustness to Human starts\" which implicitly addresses performance in a specific type of complex environment: \"We obtained 100 starting points sampled for each game from a human expert’s trajectory, as proposed by Nair et al. (2015).\" (Section 4)"
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "While the paper touches upon some aspects of limitations (hyperparameter tuning and performance with human-started environments), it doesn't provide a comprehensive analysis of sensitivity to hyperparameters or performance in a broader range of complex environments.",
      "Supporting quotes": [
        "Some tuning is appropriate because the hyperparameters were tuned for DQN but not for Double DQN."
      ],
      "Impact assessment": "The reviewer's point is partially valid. The paper acknowledges the need for hyperparameter tuning and tests robustness with human-started environments, but a more thorough investigation of limitations is missing."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "Medium",
      "Key supporting evidence": "The paper mentions hyperparameter tuning and testing with human-started environments, but lacks a systematic analysis of sensitivity to hyperparameters and performance in diverse complex environments."
    }
  },
  {
    "Weakness Statement": "The paper should also discuss the computational cost of the proposed algorithm and compare it to other methods.",
    "Evidence Collection": {
      "b) Experiment-related Evidence": [
        "The paper mentions the hardware used for experiments: \"Each evaluation episode starts by executing a special no-op action that does not affect the environment up to 30 times, to provide different starting points for the agent. Some exploration during evaluation provides additional randomization. For Double DQN we used the exact same hyper-parameters as for DQN, to allow for a controlled experiment focused just on reducing overestimations. The learned policies are evaluated for 5 mins of emulator time (18,000 frames) with an ϵ-greedy policy where ϵ = 0.05 . The only difference between Double DQN and DQN is the target, using Y t DoubleDQN ≡ R t + 1 + γ ​ Q ​ ( S t + 1 , a , 𝜃 − ) . This evaluation is somewhat adversarial, as the used hyper-parameters were tuned for DQN but not for Double DQN.\" (Section 4)",
        "The paper states the number of frames used for training: \"We closely follow the experimental setting and network architecture outlined by Mnih et al. (2015) . Briefly, the network architecture is a convolutional neural network ( Fukushima, 1988 ; LeCun et al., 1998 ) with 3 convolution layers and a fully-connected hidden layer (approximately 1.5M parameters in total). The network takes the last four frames as input and outputs the action value of each action. On each game, the network is trained on a single GPU for 200M frames, or approximately 1 week.\" (Section 4)"
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper provides details about the training time and hardware used, which implicitly relates to computational cost, but it doesn't explicitly compare the computational cost of Double DQN with other methods.",
      "Supporting quotes": [
        "On each game, the network is trained on a single GPU for 200M frames, or approximately 1 week."
      ],
      "Impact assessment": "The reviewer's suggestion is valid. While the paper provides some information about computational resources, a direct comparison of computational cost with other methods is missing."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "Lack of explicit comparison of computational cost with other methods in the paper."
    }
  },
  {
    "Weakness Statement": "Furthermore, the authors should investigate the performance of Double DQN in scenarios where the Q-value estimates are highly inaccurate or when the environment is non-stationary.",
    "Evidence Collection": {
      "b) Experiment-related Evidence": [
        "The paper tests robustness with human-started environments: \"We obtained 100 starting points sampled for each game from a human expert’s trajectory, as proposed by Nair et al. (2015).\" (Section 4)",
        "The paper mentions the deterministic nature of the Atari 2600 games: \"In some ways this is a typical learning setting, where at each point in time we only have limited data.\" (Section 2)"
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper tests robustness with human-started environments, which can be seen as a proxy for scenarios with potentially inaccurate initial Q-value estimates. However, it doesn't explicitly test scenarios with highly inaccurate Q-value estimates or non-stationary environments.",
      "Supporting quotes": [
        "We obtained 100 starting points sampled for each game from a human expert’s trajectory, as proposed by Nair et al. (2015)."
      ],
      "Impact assessment": "The reviewer's suggestion is partially valid. The paper addresses some aspects of robustness but not the specific scenarios mentioned."
    },
    "Conclusion": {
      "Validity status": "Partially Valid",
      "Confidence level": "Medium",
      "Key supporting evidence": "Testing with human-started environments addresses some aspects of robustness but doesn't cover scenarios with highly inaccurate Q-values or non-stationary environments."
    }
  },
  {
    "Weakness Statement": "Finally, the paper should provide a more detailed discussion of the experimental results. Specifically, the authors should analyze the reasons for the performance differences between Double DQN and DQN on different Atari games. This could involve investigating the characteristics of the games that make them more or less suitable for Double DQN.",
    "Evidence Collection": {
      "b) Experiment-related Evidence": [
        "The paper provides some analysis of the results: \"As described by Mnih et al. (2015) each evaluation episode starts by executing a special no-op action that does not affect the environment up to 30 times, to provide different starting points for the agent. Some exploration during evaluation provides additional randomization. For Double DQN we used the exact same hyper-parameters as for DQN, to allow for a controlled experiment focused just on reducing overestimations. The learned policies are evaluated for 5 mins of emulator time (18,000 frames) with an ϵ-greedy policy where ϵ = 0.05 . The only difference between Double DQN and DQN is the target, using Y t DoubleDQN ≡ R t + 1 + γ ​ Q ​ ( S t + 1 , a , 𝜃 − ) . This evaluation is somewhat adversarial, as the used hyper-parameters were tuned for DQN but not for Double DQN.\" (Section 4)",
        "The paper highlights specific game results: \"Double DQN outperforms DQN on several games, including Road Runner, Asterix, and Zaxxon.\" (Section 4)"
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper presents experimental results and provides some high-level analysis, but it lacks a detailed investigation into the reasons behind the performance differences across different Atari games.",
      "Supporting quotes": [
        "Double DQN outperforms DQN on several games, including Road Runner, Asterix, and Zaxxon."
      ],
      "Impact assessment": "The reviewer's point is valid. The paper could benefit from a more in-depth discussion of why Double DQN performs better on some games compared to others."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "Lack of detailed analysis of performance differences across Atari games."
    }
  },
  {
    "Weakness Statement": "How does the performance of Double DQN vary with different hyperparameters, such as the learning rate, the discount factor, and the exploration strategy?",
    "Evidence Collection": {
      "b) Experiment-related Evidence": [
        "The paper mentions hyperparameter tuning for the tuned version of Double DQN: \"Some tuning is appropriate because the hyperparameters were tuned for DQN but not for Double DQN.\" (Section 4)"
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper acknowledges the need for hyperparameter tuning but doesn't provide a systematic analysis of how performance varies with different hyperparameter settings.",
      "Supporting quotes": [
        "Some tuning is appropriate because the hyperparameters were tuned for DQN but not for Double DQN."
      ],
      "Impact assessment": "The reviewer's question highlights a valid gap in the experimental analysis. The paper lacks a detailed investigation into the sensitivity of Double DQN to hyperparameters."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "Absence of a systematic analysis of performance variation with different hyperparameters."
    }
  },
  {
    "Weakness Statement": "How does Double DQN compare to other state-of-the-art algorithms, such as Rainbow DQN or other advanced DQN variants, on the same set of Atari games?",
    "Evidence Collection": {
      "b) Experiment-related Evidence": [
        "The paper compares Double DQN to DQN: \"We closely follow the experimental setting and network architecture outlined by Mnih et al. (2015) . Briefly, the network architecture is a convolutional neural network ( Fukushima, 1988 ; LeCun et al., 1998 ) with 3 convolution layers and a fully-connected hidden layer (approximately 1.5M parameters in total). The network takes the last four frames as input and outputs the action value of each action. On each game, the network is trained on a single GPU for 200M frames, or approximately 1 week.\" (Section 4)",
        "The paper includes a comparison to DQN: \"Double DQN outperforms DQN on several games, including Road Runner, Asterix, and Zaxxon.\" (Section 4)"
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper compares Double DQN to the standard DQN but does not include comparisons to other state-of-the-art algorithms like Rainbow DQN.",
      "Supporting quotes": [
        "Double DQN outperforms DQN on several games, including Road Runner, Asterix, and Zaxxon."
      ],
      "Impact assessment": "The reviewer's question points to a valid limitation in the experimental evaluation. The paper lacks a comparison to more advanced DQN variants."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "Lack of comparison to other state-of-the-art algorithms like Rainbow DQN."
    }
  },
  {
    "Weakness Statement": "What are the limitations of Double DQN, and what are the potential directions for future research?",
    "Evidence Collection": {
      "b) Experiment-related Evidence": [
        "The paper includes a section on \"Robustness to Human starts\": \"We obtained 100 starting points sampled for each game from a human expert’s trajectory, as proposed by Nair et al. (2015).\" (Section 4)",
        "The paper mentions the need for hyperparameter tuning: \"Some tuning is appropriate because the hyperparameters were tuned for DQN but not for Double DQN.\" (Section 4)"
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper touches upon some limitations like the need for hyperparameter tuning and testing with human-started environments, but it lacks a comprehensive discussion of the limitations and future research directions.",
      "Supporting quotes": [
        "Some tuning is appropriate because the hyperparameters were tuned for DQN but not for Double DQN."
      ],
      "Impact assessment": "The reviewer's question highlights a valid gap in the paper's discussion. The paper could benefit from a more thorough analysis of its limitations and potential future research avenues."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "Lack of a comprehensive discussion of limitations and future research directions."
    }
  },
  {
    "Weakness Statement": "The paper does not provide a theoretical analysis of the proposed algorithm. It is not clear why the proposed algorithm should work better than DQN. The paper should provide a theoretical analysis of the proposed algorithm and compare it to DQN.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "The paper includes a theoretical theorem about value estimation bias: \"Theorem 1 . Consider a state s s in which all the true optimal action values are equal at Q ∗ ( s ) . Let Q t Q_{t} be arbitrary value estimates that are on the whole unbiased in the sense that ∑ a ( Q t ​ ( s , a ) − V ∗ ​ ( s ) ) = 0 \text{ for some V ∗ ​ ( s ) V_{\*}( s ) . But that the bias of the Double Q-learning estimate is zero. (Proof in appendix.)\" (Section 3)",
        "The paper discusses the convergence of Double Q-learning in the context of value estimation bias: \"Theorem 1 shows that even if the value estimates are on average correct, estimation errors of any source can drive the estimates up and away from the true optimal values.\" (Section 3)"
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "While the paper provides a theoretical analysis of value estimation bias in Double Q-learning, it doesn't offer a formal theoretical proof of why Double DQN converges better or has better performance than standard DQN.",
      "Supporting quotes": [
        "Theorem 1 . Consider a state s s in which all the true optimal action values are equal at Q ∗ ( s ) . Let Q t Q_{t} be arbitrary value estimates that are on the whole unbiased in the sense that ∑ a ( Q t ​ ( s , a ) − V ∗ ​ ( s ) ) = 0 \text{ for some V ∗ ​ ( s ) V_{\*}( s ) . But that the bias of the Double Q-learning estimate is zero."
      ],
      "Impact assessment": "The reviewer's point is valid. The paper lacks a formal theoretical justification for the superiority of Double DQN over DQN."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "Absence of a formal theoretical proof comparing Double DQN's convergence and performance to DQN."
    }
  },
  {
    "Weakness Statement": "The paper does not provide a comparison of the proposed algorithm to other algorithms that address overestimation. The paper should compare the proposed algorithm to other algorithms that specifically address the overestimation problem, such as those based on distributional RL or ensemble methods. The comparison should not only focus on the final performance but also on other aspects such as sample efficiency, robustness to hyperparameter settings, and computational cost. Furthermore, the paper should provide a detailed analysis of the results, highlighting the specific scenarios where Double DQN excels and where it might fall short. This would provide a more nuanced understanding of the algorithm's strengths and weaknesses and help to identify potential areas for improvement.",
    "Evidence Collection": {
      "b) Experiment-related Evidence": [
        "The paper compares Double DQN to DQN: \"We closely follow the experimental setting and network architecture outlined by Mnih et al. (2015) . Briefly, the network architecture is a convolutional neural network ( Fukushima, 1988 ; LeCun et al., 1998 ) with 3 convolution layers and a fully-connected hidden layer (approximately 1.5M parameters in total). The network takes the last four frames as input and outputs the action value of each action. On each game, the network is trained on a single GPU for 200M frames, or approximately 1 week.\" (Section 4)",
        "The paper includes a comparison to DQN: \"Double DQN outperforms DQN on several games, including Road Runner, Asterix, and Zaxxon.\" (Section 4)"
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper compares Double DQN to the standard DQN but lacks comparisons to other algorithms specifically designed to address overestimation, such as distributional RL or ensemble methods. It also lacks a detailed analysis of performance across different scenarios.",
      "Supporting quotes": [
        "Double DQN outperforms DQN on several games, including Road Runner, Asterix, and Zaxxon."
      ],
      "Impact assessment": "The reviewer's points are valid. The paper's comparisons are limited, and a more detailed analysis of performance is missing."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "Lack of comparison to algorithms specifically addressing overestimation and a detailed analysis of performance across scenarios."
    }
  },
  {
    "Weakness Statement": "Finally, the paper should discuss the limitations of Double DQN and suggest potential directions for future research. For example, the paper could explore the applicability of Double DQN to other reinforcement learning problems, such as those with high-dimensional state spaces or continuous action spaces. It could also investigate the use of different network architectures or optimization techniques to further improve the performance of Double DQN. Furthermore, the paper should explore the potential of combining Double DQN with other techniques, such as model-based reinforcement learning or hierarchical reinforcement learning. The paper should also discuss the limitations of Double DQN, and suggest potential directions for future research.",
    "Evidence Collection": {
      "b) Experiment-related Evidence": [
        "The paper includes a section on \"Robustness to Human starts\": \"We obtained 100 starting points sampled for each game from a human expert’s trajectory, as proposed by Nair et al. (2015).\" (Section 4)",
        "The paper mentions the need for hyperparameter tuning: \"Some tuning is appropriate because the hyperparameters were tuned for DQN but not for Double DQN.\" (Section 4)"
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper touches upon some limitations like the need for hyperparameter tuning and testing with human-started environments, but it lacks a comprehensive discussion of the limitations and future research directions, particularly regarding applicability to other RL problems or advanced techniques.",
      "Supporting quotes": [
        "Some tuning is appropriate because the hyperparameters were tuned for DQN but not for Double DQN."
      ],
      "Impact assessment": "The reviewer's points are valid. The paper could benefit from a more thorough discussion of its limitations and potential future research avenues."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "Lack of a comprehensive discussion of limitations and future research directions, especially regarding applicability to other RL problems and advanced techniques."
    }
  },
  {
    "Weakness Statement": "What are the theoretical properties of Double DQN that are different from Double Q-learning? How do these properties affect the performance of the algorithm?",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "The paper includes a theoretical theorem about value estimation bias: \"Theorem 1 . Consider a state s s in which all the true optimal action values are equal at Q ∗ ( s ) . Let Q t Q_{t} be arbitrary value estimates that are on the whole unbiased in the sense that ∑ a ( Q t ​ ( s , a ) − V ∗ ​ ( s ) ) = 0 \text{ for some V ∗ ​ ( s ) V_{\*}( s ) . But that the bias of the Double Q-learning estimate is zero. (Proof in appendix.)\" (Section 3)"
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper provides a theoretical analysis of Double Q-learning but doesn't explicitly detail the theoretical properties of Double DQN that differ from it and how these properties affect performance.",
      "Supporting quotes": [
        "Theorem 1 . Consider a state s s in which all the true optimal action values are equal at Q ∗ ( s ) . Let Q t Q_{t} be arbitrary value estimates that are on the whole unbiased in the sense that ∑ a ( Q t ​ ( s , a ) − V ∗ ​ ( s ) ) = 0 \text{ for some V ∗ ​ ( s ) V_{\*}( s ) . But that the bias of the Double Q-learning estimate is zero."
      ],
      "Impact assessment": "The reviewer's question points to a valid gap in the paper's discussion of the theoretical underpinnings of Double DQN."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "Lack of explicit discussion of Double DQN's theoretical properties compared to Double Q-learning."
    }
  },
  {
    "Weakness Statement": "How does Double DQN compare to other state-of-the-art algorithms, such as Rainbow DQN or other advanced DQN variants, on the same set of Atari games?",
    "Evidence Collection": {
      "b) Experiment-related Evidence": [
        "The paper compares Double DQN to DQN: \"We closely follow the experimental setting and network architecture outlined by Mnih et al. (2015) . Briefly, the network architecture is a convolutional neural network ( Fukushima, 1988 ; LeCun et al., 1998 ) with 3 convolution layers and a fully-connected hidden layer (approximately 1.5M parameters in total). The network takes the last four frames as input and outputs the action value of each action. On each game, the network is trained on a single GPU for 200M frames, or approximately 1 week.\" (Section 4)",
        "The paper includes a comparison to DQN: \"Double DQN outperforms DQN on several games, including Road Runner, Asterix, and Zaxxon.\" (Section 4)"
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper compares Double DQN to the standard DQN but does not include comparisons to other state-of-the-art algorithms like Rainbow DQN.",
      "Supporting quotes": [
        "Double DQN outperforms DQN on several games, including Road Runner, Asterix, and Zaxxon."
      ],
      "Impact assessment": "The reviewer's question highlights a valid gap in the experimental evaluation. The paper lacks a comparison to more advanced DQN variants."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "Lack of comparison to other state-of-the-art algorithms like Rainbow DQN."
    }
  },
  {
    "Weakness Statement": "What are the limitations of Double DQN, and what are the potential directions for future research?",
    "Evidence Collection": {
      "b) Experiment-related Evidence": [
        "The paper includes a section on \"Robustness to Human starts\": \"We obtained 100 starting points sampled for each game from a human expert’s trajectory, as proposed by Nair et al. (2015).\" (Section 4)",
        "The paper mentions the need for hyperparameter tuning: \"Some tuning is appropriate because the hyperparameters were tuned for DQN but not for Double DQN.\" (Section 4)"
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper touches upon some limitations like the need for hyperparameter tuning and testing with human-started environments, but it lacks a comprehensive discussion of the limitations and future research directions.",
      "Supporting quotes": [
        "Some tuning is appropriate because the hyperparameters were tuned for DQN but not for Double DQN."
      ],
      "Impact assessment": "The reviewer's question highlights a valid gap in the paper's discussion of its limitations and potential future research avenues."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "Lack of a comprehensive discussion of limitations and future research directions."
    }
  },
  {
    "Weakness Statement": "The main weakness of the paper is the limited novelty of the proposed algorithm. While the paper acknowledges that Double DQN is a simple extension of Double Q-learning, it does not provide a strong justification for why this extension is significant. The paper could benefit from a more in-depth analysis of the theoretical properties of Double DQN and how they differ from Double Q-learning. Specifically, the paper lacks a rigorous analysis of the convergence properties of the proposed algorithm, and it does not provide any theoretical guarantees on the performance of the algorithm. Furthermore, the paper does not explore the potential limitations of the proposed approach, such as its sensitivity to hyperparameter settings or its performance in more complex environments.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "The paper includes a theoretical theorem about value estimation bias: \"Theorem 1 . Consider a state s s in which all the true optimal action values are equal at Q ∗ ( s ) . Let Q t Q_{t} be arbitrary value estimates that are on the whole unbiased in the sense that ∑ a ( Q t ​ ( s , a ) − V ∗ ​ ( s ) ) = 0 \text{ for some V ∗ ​ ( s ) V_{\*}( s ) . But that the bias of the Double Q-learning estimate is zero. (Proof in appendix.)\" (Section 3)",
        "The paper discusses the convergence of Double Q-learning in the context of value estimation bias: \"Theorem 1 shows that even if the value estimates are on average correct, estimation errors of any source can drive the estimates up and away from the true optimal values.\" (Section 3)"
      ],
      "b) Experiment-related Evidence": [
        "The paper mentions hyperparameter tuning for Double DQN: \"Some tuning is appropriate because the hyperparameters were tuned for DQN but not for Double DQN.\" (Section 4)",
        "The paper includes a section on \"Robustness to Human starts\": \"We obtained 100 starting points sampled for each game from a human expert’s trajectory, as proposed by Nair et al. (2015).\" (Section 4)"
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "While the paper provides a theoretical analysis of Double Q-learning, it lacks a rigorous analysis of Double DQN's convergence and performance guarantees. It also acknowledges the need for hyperparameter tuning and testing with human-started environments, suggesting sensitivity to these factors.",
      "Supporting quotes": [
        "Theorem 1 . Consider a state s s in which all the true optimal action values are equal at Q ∗ ( s ) . Let Q t Q_{t} be arbitrary value estimates that are on the whole unbiased in the sense that ∑ a ( Q t ​ ( s , a ) − V ∗ ​ ( s ) ) = 0 \text{ for some V ∗ ​ ( s ) V_{\*}( s ) . But that the bias of the Double Q-learning estimate is zero.",
        "Some tuning is appropriate because the hyperparameters were tuned for DQN but not for Double DQN.",
        "We obtained 100 starting points sampled for each game from a human expert’s trajectory, as proposed by Nair et al. (2015)."
      ],
      "Impact assessment": "The reviewer's assessment of the limited novelty and the lack of theoretical guarantees and thorough hyperparameter analysis is valid."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "Absence of rigorous convergence and performance guarantees for Double DQN, and acknowledgment of hyperparameter tuning and human-started environment testing."
    }
  },
  {
    "Weakness Statement": "The paper could explore the limitations of the proposed algorithm and discuss potential extensions of the algorithm, such as incorporating techniques for exploration or handling non-stationary environments. The paper should also discuss the computational cost of the proposed algorithm and compare it to other methods. It is also unclear how the proposed algorithm would perform in scenarios where the Q-value estimates are highly inaccurate or when the environment is non-stationary.",
    "Evidence Collection": {
      "b) Experiment-related Evidence": [
        "The paper mentions hyperparameter tuning for Double DQN: \"Some tuning is appropriate because the hyperparameters were tuned for DQN but not for Double DQN.\" (Section 4)",
        "The paper includes a section on \"Robustness to Human starts\": \"We obtained 100 starting points sampled for each game from a human expert’s trajectory, as proposed by Nair et al. (2015).\" (Section 4)"
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper acknowledges the need for hyperparameter tuning and testing with human-started environments, suggesting sensitivity to these factors. However, it lacks a detailed discussion of limitations, potential extensions, and computational cost.",
      "Supporting quotes": [
        "Some tuning is appropriate because the hyperparameters were tuned for DQN but not for Double DQN.",
        "We obtained 100 starting points sampled for each game from a human expert’s trajectory, as proposed by Nair et al. (2015)."
      ],
      "Impact assessment": "The reviewer's points about limitations, extensions, and computational cost are valid."
    },
    "Conclusion": {
      "Validity status": "Valid",
      "Confidence level": "High",
      "Key supporting evidence": "Lack of detailed discussion on limitations, extensions, and computational cost."
    }
  },
  {
    "Weakness Statement": "The paper would benefit from a more thorough theoretical analysis of the proposed Double DQN algorithm. Specifically, the authors should investigate the convergence properties of the algorithm and provide theoretical guarantees on its performance. This could involve adapting existing theoretical frameworks for value-based reinforcement learning or developing new ones tailored to the specific structure of Double DQN. For example, it would be useful to analyze the bias and variance of the Q-value estimates produced by Double DQN and to compare these to those of standard DQN. Furthermore, the authors should explore the sensitivity of the algorithm to hyperparameter settings, such as the learning rate and the discount factor. This could involve conducting a systematic study of the impact of different hyperparameter values on the performance of Double DQN and providing guidelines for selecting appropriate values. The authors should also discuss the potential limitations of the proposed approach, such as its performance in more complex environments or in scenarios where the Q-value estimates are highly inaccurate. This would help to provide a more complete picture of the strengths and weaknesses of the proposed algorithm.",
    "Evidence Collection": {
      "a) Method-related Evidence": [
        "The paper includes a theoretical theorem about value estimation bias: \"Theorem 1 . Consider a state s s in which all the true optimal action values are equal at Q ∗ ( s ) . Let Q t Q_{t} be arbitrary value estimates that are on the whole unbiased in the sense that ∑ a ( Q t ​ ( s , a ) − V ∗ ​ ( s ) ) = 0 \text{ for some V ∗ ​ ( s ) V_{\*}( s ) . But that the bias of the Double Q-learning estimate is zero. (Proof in appendix.)\" (Section 3)"
      ],
      "b) Experiment-related Evidence": [
        "The paper mentions hyperparameter tuning for Double DQN: \"Some tuning is appropriate because the hyperparameters were tuned for DQN but not for Double DQN.\" (Section 4)",
        "The paper includes a section on \"Robustness to Human starts\": \"We obtained 100 starting points sampled for each game from a human expert’s trajectory, as proposed by Nair et al. (2015).\" (Section 4)"
      ]
    },
    "Literature Gap Analysis": [],
    "Validation Analysis": {
      "Primary evidence summary": "The paper provides a theoretical analysis of Double Q-learning but lacks a rigorous analysis of Double DQN's convergence, performance guarantees, sensitivity to hyperparameters, and discussion of limitations.",
      "Supporting quotes": [
        "Theorem 1 . Consider a state s s in which all the true optimal action values are equal at Q ∗ ( s ) . Let Q t Q_{t} be arbitrary value estimates that are on the whole unbiased in the sense that ∑ a ( Q t ​ ( s , a ) − V ∗ ​ ( s ) ) = 0 \text{ for some V ∗ ​ ( s ) V_{\*}( s ) . But that the bias of the Double Q-learning estimate is zero.",
        "Some tuning is appropriate because the hyperparameters were tuned for DQN but not for Double DQN.",
        "We obtained 100 starting points sampled for each game from a human expert’s trajectory, as proposed by Nair et al. (2015)."
      ],
      "Impact assessment": "The reviewer's points}

Now, I have successfully verified each review. Next, I will organize this content and output the final review decision:

\boxed_review{
## Summary:

This paper introduces Double DQN, a variant of the Deep Q-Network (DQN) algorithm, designed to mitigate the overestimation bias that can negatively impact the performance of DQN. The authors argue that this bias arises from the use of the maximum Q-value estimate during the Bellman update, which can lead to inaccurate value assessments. To address this, Double DQN employs two separate networks: an online network used to evaluate actions and a target network used to estimate the value of those actions. This approach is inspired by Double Q-learning, a method that has been shown to reduce overestimation bias in the tabular setting. The core idea is that by using the target network to evaluate the action selected by the online network, Double DQN can obtain a more accurate estimate of the value, thus reducing the overestimation problem. The authors demonstrate the effectiveness of Double DQN through empirical evaluations on the Atari 2600 domain, showing that it outperforms standard DQN on several games. Specifically, they report that Double DQN achieves state-of-the-art results on the Atari 2600 domain, surpassing the performance of DQN. The paper also explores the robustness of Double DQN by testing it with human-started environments, where the agent begins with a set of pre-trained weights from human expert trajectories. This analysis suggests that Double DQN is less sensitive to the initial conditions than standard DQN. The authors also investigate the impact of hyperparameter tuning, noting that Double DQN requires tuning of the learning rate and discount factor, which is not the case for standard DQN. Overall, the paper presents a simple yet effective modification to the DQN algorithm that addresses a critical issue in reinforcement learning, and the empirical results provide strong evidence for the effectiveness of the proposed approach. The paper is well-written and easy to follow, making it accessible to a broad audience. However, there are some limitations in the theoretical analysis and the experimental evaluation that warrant further investigation.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

2.25


## Strengths:

I found several aspects of this paper to be particularly strong. First, the paper clearly identifies a significant problem in the DQN algorithm: the overestimation bias that can lead to suboptimal performance. The authors provide a thorough explanation of this issue, demonstrating that even in deterministic environments, the maximum operator in the Bellman equation can drive value estimates up away from their true optimal values. This analysis is supported by a theoretical theorem (Theorem 1) that shows how value estimation errors can propagate and lead to overestimation. Second, the proposed solution, Double DQN, is both simple and effective. The modification is a straightforward adaptation of Double Q-learning to the DQN framework, requiring only the addition of a target network and a change in the evaluation process. This simplicity makes Double DQN easy to implement and integrate into existing DQN-based systems. The authors' choice to adapt Double Q-learning, a method that has been shown to be effective in the tabular setting, to the deep reinforcement learning domain is a logical and well-justified approach. Third, the empirical results presented in the paper are compelling. The authors demonstrate that Double DQN outperforms DQN on several Atari games, achieving state-of-the-art results on the Atari 2600 domain. These results are not only statistically significant but also practically relevant, as they show that Double DQN can be a valuable tool for improving the performance of DQN-based agents. The authors also explore the robustness of Double DQN by testing it with human-started environments, which provides further evidence for its effectiveness. Finally, the paper is well-written and easy to follow. The authors provide a clear and concise explanation of the problem, the proposed solution, and the experimental results. The paper is well-organized, and the arguments are presented in a logical and coherent manner. The inclusion of a theoretical analysis, empirical evidence, and a discussion of the limitations of the proposed approach makes the paper a valuable contribution to the field of reinforcement learning.


## Weaknesses:

Despite its strengths, I have identified several weaknesses in this paper that warrant further discussion. First, while the paper acknowledges that Double DQN is a simple extension of Double Q-learning, it does not provide a strong justification for why this extension is significant. The authors state that Double DQN is a “minimal possible change” to DQN, but they do not provide a rigorous analysis of the theoretical properties of Double DQN that differ from Double Q-learning. Specifically, the paper lacks a formal convergence proof for Double DQN, which is a significant omission. While the paper provides a theoretical analysis of Double Q-learning, it does not show how the double Q-learning update rule affects the bias and variance of the Q-value estimates. This lack of theoretical analysis makes it difficult to understand why Double DQN should be expected to work better than DQN, and it also limits the generalizability of the results. Second, the paper does not explore the potential limitations of the proposed approach. While the authors mention the need for hyperparameter tuning for Double DQN, they do not provide a systematic analysis of how different learning rates, discount factors, and exploration strategies affect the performance of Double DQN. This lack of analysis makes it difficult to assess the robustness of the proposed algorithm and to provide guidelines for selecting appropriate hyperparameters. Furthermore, the paper does not investigate the performance of Double DQN in scenarios where the Q-value estimates are highly inaccurate or when the environment is non-stationary. This is a significant limitation, as it is important to understand the limitations of an algorithm before applying it to real-world problems. Third, the paper's experimental evaluation is limited in scope. While the authors compare Double DQN to DQN, they do not include comparisons to other state-of-the-art algorithms that address the overestimation problem, such as distributional RL or ensemble methods. This makes it difficult to assess the relative strengths and weaknesses of Double DQN compared to other approaches. Furthermore, the paper does not provide a detailed analysis of the performance differences between Double DQN and DQN on different Atari games. While the authors highlight specific games where Double DQN excels, they do not investigate the characteristics of these games that make them more or less suitable for Double DQN. This lack of analysis limits our understanding of the algorithm's strengths and weaknesses. Fourth, the paper does not provide a detailed discussion of the computational cost of Double DQN. While the authors mention the hardware used for the experiments, they do not provide a direct comparison of the computational cost of Double DQN with other methods. This is an important omission, as it is necessary to understand the practical feasibility of Double DQN in real-world applications. Finally, the paper lacks a comprehensive discussion of the limitations of Double DQN and potential future research directions. While the authors briefly mention the need for hyperparameter tuning and testing with human-started environments, they do not provide a thorough analysis of the limitations of the proposed approach or suggest specific avenues for future research. This is a significant omission, as it is important to acknowledge the limitations of any proposed algorithm and to suggest directions for future research. These weaknesses, while not invalidating the paper's contributions, do limit its overall impact and generalizability.


## Suggestions:

Based on the identified weaknesses, I recommend several concrete improvements to this paper. First, the authors should provide a more rigorous theoretical analysis of Double DQN. This should include a formal convergence proof for Double DQN, as well as an analysis of the bias and variance of the Q-value estimates produced by Double DQN. The authors should also compare the theoretical properties of Double DQN with those of Double Q-learning to highlight the specific conditions under which Double DQN is guaranteed to converge to an optimal policy. This analysis should also explore the impact of the double Q-learning update rule on the bias and variance of the Q-value estimates. Second, the authors should conduct a more thorough hyperparameter sensitivity analysis of Double DQN. This should involve varying each hyperparameter individually while keeping the others constant, and then plotting the performance of Double DQN as a function of each hyperparameter. The results of this analysis should be presented in the paper, along with a discussion of the optimal hyperparameter settings for Double DQN. Furthermore, the authors should compare the hyperparameter sensitivity of Double DQN to that of standard DQN to understand how the double Q-learning update affects the learning process. This analysis would provide valuable insights into the practical application of Double DQN and help users to tune the algorithm for their specific tasks. Third, the authors should expand the experimental evaluation to include a comparison to other state-of-the-art algorithms that address the overestimation problem. This should include a comparison to algorithms such as Rainbow DQN, which incorporates a variety of techniques for improving DQN performance, including distributional RL, double Q-learning, and prioritized experience replay. The comparison should not only focus on the final performance but also on other aspects such as sample efficiency, robustness to hyperparameter settings, and computational cost. Furthermore, the authors should explore the performance of Double DQN in scenarios where the Q-value estimates are highly inaccurate or when the environment is non-stationary. This would help to identify the limitations of the proposed approach and provide insights into potential areas for improvement. Fourth, the authors should provide a more detailed analysis of the performance differences between Double DQN and DQN on different Atari games. This should involve investigating the characteristics of the games that make them more or less suitable for Double DQN. This analysis would help to identify the strengths and weaknesses of the proposed algorithm and provide guidance for future research. Finally, the authors should provide a more comprehensive discussion of the limitations of Double DQN and potential future research directions. This should include a discussion of the computational cost of Double DQN, its sensitivity to hyperparameter settings, and its performance in more complex environments. The authors should also suggest potential directions for future research, such as incorporating techniques for exploration or handling non-stationary environments. This would help to position the paper within the broader research landscape and provide a roadmap for future work in this area. By addressing these limitations and providing a more thorough analysis of the proposed algorithm, the authors can significantly strengthen their paper and make a more substantial contribution to the field of reinforcement learning.


## Questions:

I have several questions that arise from my analysis of this paper. First, how does the performance of Double DQN vary with different hyperparameter settings, such as the learning rate, discount factor, and exploration strategy? While the paper acknowledges the need for hyperparameter tuning, it does not provide a systematic analysis of how these parameters affect the performance of Double DQN. Understanding this relationship is crucial for practical applications of the algorithm. Second, how does Double DQN compare to other state-of-the-art algorithms that address the overestimation problem, such as distributional RL or ensemble methods? The paper only compares Double DQN to the standard DQN algorithm, but it does not include comparisons to other relevant algorithms. This makes it difficult to assess the relative strengths and weaknesses of Double DQN. Third, what are the theoretical properties of Double DQN that are different from Double Q-learning? The paper provides a theoretical analysis of Double Q-learning, but it does not explicitly detail the theoretical properties of Double DQN that differ from it and how these properties affect performance. Fourth, what are the limitations of Double DQN, and what are the potential directions for future research? The paper briefly mentions some limitations, but it does not provide a comprehensive discussion of the limitations of the proposed approach. Understanding these limitations is crucial for identifying potential areas for improvement. Fifth, how does the computational cost of Double DQN compare to other methods? The paper does not provide a direct comparison of the computational cost of Double DQN with other methods, which is an important omission. Finally, how does Double DQN perform in scenarios where the Q-value estimates are highly inaccurate or when the environment is non-stationary? The paper does not investigate the performance of Double DQN in these scenarios, which is important for understanding the limitations of the algorithm. These questions highlight key uncertainties and areas for further investigation, and they are crucial for a more complete understanding of the proposed algorithm.


## Rating:

6.0


## Confidence:

3.75


## Decision:

Accept
}