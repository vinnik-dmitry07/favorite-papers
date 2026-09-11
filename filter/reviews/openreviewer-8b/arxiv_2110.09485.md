# Review

## Summary
This paper argues that interpolation is impossible in high dimensional spaces, where the convex hull of a dataset will almost surely not contain any test points. The authors argue that this has consequences for how we think about generalisation in machine learning.

## Soundness
2

## Presentation
2

## Contribution
1

## Strengths
The paper is well-written and easy to follow. The argument is clear and the experiments support the theoretical results.

## Weaknesses
The main weakness of the paper is that it does not engage with the literature on generalisation and the role of interpolation in it. The claim is not that interpolation is unimportant, but rather that interpolation is not what it is often made out to be in machine learning. There is a large body of work on the role of interpolation in generalisation, which is not discussed in this paper. For example, see [1,2,3,4]. In particular, [1] shows that interpolation can be necessary for good generalisation. Thus, the claim that interpolation is unimportant for generalisation is not supported by the literature. Furthermore, the claim that extrapolation is all that is needed for generalisation is not supported by the literature either. The literature suggests that interpolation can be helpful for generalisation. Thus, the paper's conclusions do not seem to be supported by the literature.

The paper also does not engage with the literature on the geometry of generalisation, which also has a lot to say about the role of interpolation in generalisation. For example, see [5,6]. In particular, [5] shows that the generalisation error is characterised by the geometry of the loss landscape around the optimal parameters. The geometry of the loss landscape is related to the convex hull of the parameter space, which is related to the convex hull of the data (since the parameters are fitted to the data). Thus, the paper's claims about the convex hull of the data have implications for the geometry of the loss landscape and, hence, for generalisation. This literature is not discussed in the paper.

[1] Generalization Error Bounds of Unregularized Empirical Risk Minimization: Two-Step Approach, Alexander Tyurin, Daniil Dvinskikh, Alexey Ignatiev, Evgeny Burnaev, NeurIPS 2021

[2] The Role of Interpolation in Generalization, D. Beaini, A. Montanari, A. Sordoni, F. Babilani, M. Lelarge, M. Mézard, NIPS 2020

[3] Interpolation can be necessary for generalization, D. Beaini, A. Montanari, M. Mézard, A. Sordoni, F. Babilani, NIPS 2019

[4] The generalization error of random features regression: Precise asymptotics and double descent curve, A. Nitanda, S. Tak, Y. Saito, T. Suzuki, NIPS 2020

[5] The Geometry of Generalization and the Role of the Neural Network Overparameterization, S. Frei and P. L. Bartlett, JMLR 2021

[6] The geometry of model selection, S. Frei and P. L. Bartlett, JMLR 2020

## Questions
I do not have any questions.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
1

## Confidence
4