# Review

## Summary
The paper proposes a simple method for setting the learning rate of a neural network. Instead of using a fixed learning rate or a monotonically decreasing learning rate, the authors propose to use a cyclical learning rate, i.e., the learning rate cyclically varies between some "reasonable" boundary values. The authors demonstrate the effectiveness of the proposed method on several datasets and architectures.

## Soundness
2

## Presentation
1

## Contribution
1

## Strengths
The paper is easy to follow.

## Weaknesses
1. The paper is not well-written. The paper contains many typos and grammatical errors. For example, "A deep neural network is typically updated by stochastic gradient descent and the parameters θ (weights) are updated by ...", "Experiments with numerous functional forms, such as a triangular window (linear), a Welch window (parabolic) and a Hann window (sinusoidal) all produced equivalent results", "An intuitive understanding of why CLR methods work comes from considering the loss function topology", etc.

2. The paper lacks novelty. The idea of cyclical learning rate is not new. For example, [1] proposed a similar method. The authors should discuss the differences between the proposed method and existing methods and demonstrate the superiority of the proposed method.

3. The paper lacks theoretical analysis. The authors should provide some theoretical analysis to show why the proposed method works.

4. The paper lacks ablation studies. The authors should conduct ablation studies to show the effectiveness of each component of the proposed method.

5. The paper lacks comparison with state-of-the-art methods. The authors should compare the proposed method with more state-of-the-art methods to demonstrate its effectiveness.

[1] Smith, Samuel L., et al. "On the Origin and Effectiveness of Cyclical Learning Rates." International Conference on Learning Representations. 2021.

## Questions
See Weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4