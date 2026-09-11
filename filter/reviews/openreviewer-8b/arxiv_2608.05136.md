# Review

## Summary
This paper studies the implicit bias of optimization algorithms on factored models. Specifically, the authors focus on the gauge symmetry of the objective function $L(U, V) = f(UV^\top)$, where $U, V \in \mathbb{R}^{n \times k}$ and $k \geq \mathrm{rank}(L)$.

They show that the update rule is equivariant if and only if it takes the form $\Delta = H(GG^\top)\Delta$ for some preconditioner $H$ (Theorem 4.5). They also show that gradient descent, Polyak momentum, Adam with a shared scalar second moment, Muon’s matrix sign update, and Shampoo’s Kronecker preconditioner with damping are all equivariant, while Adam, RMSProp, signSGD, and Lion are not.

The authors conduct experiments on matrix sensing without weight decay, showing that all optimizers are driven to interpolation. They separate the nine considered update rules into two classes by their recovery error (equivariant $0.00$-$0.29$ and coordinate-wise $0.42$-$0.57$). They also construct a parameterized family of update rules interpolating between coordinate-wise and shared-scalar preconditioning, showing that recovery and effective rank improve monotonically.

Finally, the authors demonstrate that the same gauge symmetry applies to attention heads in transformers. They train twin transformers with identical inputs and architectures but different gauge, showing that Adam diverges at the first step, while SGD and scalar-Adam do not.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow. The authors provide clear explanations of the concepts and results.
2. The theoretical results are solid and well-supported by the experiments. The authors provide detailed proofs and comprehensive experimental results.
3. The results have implications for our understanding of optimization algorithms on factored models and their performance in practical applications.

## Weaknesses
1. The authors could provide more intuition for Theorem 4.5 and its proof. Specifically, why does the update have to be a left preconditioner whose only input is the Gram matrix?
2. The authors could provide more details on the experimental setup and hyperparameter tuning. Specifically, what learning rates were used for the different optimizers? How were they chosen?
3. The authors could provide more discussion on the practical implications of their results. Specifically, how can the results be used to improve the performance of optimization algorithms in practice?

## Questions
1. Can the results be generalized to other types of factored models beyond the square case considered in the paper?
2. How do the results change when weight decay is included in the objective function?
3. How do the results change when the objective function is not invariant under gauge transformations?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4