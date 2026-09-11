# Review

## Summary
This paper proposes a deep reinforcement learning approach for financial trading. The authors propose a Markov Decision Process (MDP) model for the financial trading task and solve it with the state-of-the-art deep recurrent Q-network (DRQN) algorithm. The authors propose several modifications to the existing learning algorithm to make it more suitable under the financial trading setting, including using a substantially small replay memory, developing an action augmentation technique, and sampling a longer sequence for recurrent neural network training. The authors combine all of the above into a complete online learning algorithm and validate their approach on the spot foreign exchange market.

## Soundness
2

## Presentation
2

## Contribution
2

## Strengths
1. The paper is well-written and easy to follow.
2. The paper proposes a novel approach to financial trading using deep reinforcement learning, which is a relatively new and unexplored area in the field.
3. The paper provides a thorough evaluation of the proposed algorithm on the spot foreign exchange market, and shows positive results under most simulation settings.

## Weaknesses
1. The paper does not provide a detailed comparison with other existing methods for financial trading, such as technical analysis, fundamental analysis, or other machine learning-based approaches.
2. The paper does not provide a detailed analysis of the risks associated with financial trading, such as drawdowns or volatility.
3. The paper does not provide a detailed analysis of the generalization ability of the proposed algorithm to other financial markets or asset classes, such as stocks, bonds, or commodities.
4. The paper does not provide a detailed analysis of the computational resources required to implement the proposed algorithm, such as memory or processing power.
5. The paper does not provide a detailed analysis of the scalability of the proposed algorithm to larger or more complex financial trading scenarios.

## Questions
1. How does the proposed algorithm compare to other existing methods for financial trading, such as technical analysis, fundamental analysis, or other machine learning-based approaches?
2. What are the risks associated with using the proposed algorithm for financial trading, such as drawdowns or volatility?
3. How well does the proposed algorithm generalize to other financial markets or asset classes, such as stocks, bonds, or commodities?
4. What are the computational resources required to implement the proposed algorithm, such as memory or processing power?
5. How scalable is the proposed algorithm to larger or more complex financial trading scenarios?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4