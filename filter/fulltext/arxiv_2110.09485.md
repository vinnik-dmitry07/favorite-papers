##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Learning in High Dimension Always Amounts to Extrapolation

###### Abstract

The notion of interpolation and extrapolation is fundamental in various fields from deep learning to function approximation. Interpolation occurs for a sample 𝒙 \boldsymbol{x} whenever this sample falls inside or on the boundary of the given dataset’s convex hull. Extrapolation occurs when 𝒙 \boldsymbol{x} falls outside of that convex hull. One fundamental (mis)conception is that state-of-the-art algorithms work so well because of their ability to correctly interpolate training data. A second (mis)conception is that interpolation happens throughout tasks and datasets, in fact, many intuitions and theories rely on that assumption. We empirically and theoretically argue against those two points and demonstrate that on any high-dimensional ( > > 100) dataset, interpolation almost surely never happens. Those results challenge the validity of our current interpolation/extrapolation definition as an indicator of generalization performances.

## 1 Introduction

The origin of the interpolation and extrapolation notions are hard to trace back. Kolmogoroff, (1941) ; Wiener, (1949) defined extrapolation as predicting the future (realization) of a stationary Gaussian process based on past and current realizations. Conversely, interpolation was defined as predicting the possible realization of such process at a time position lying in-between observations, i.e., interpolation resamples the past. Various research communities have formalized those definitions as follows.

###### Definition 1 .

Interpolation occurs for a sample 𝒙 \boldsymbol{x} whenever this sample belongs to the convex hull of a set of samples 𝑿 ≜ { 𝒙 1 , … , 𝒙 N } \boldsymbol{X}\triangleq\{\boldsymbol{x}_{1},\dots,\boldsymbol{x}_{N}\} , if not, extrapolation occurs.

From the above definition, it is reasonable to assume extrapolation as being a more intricate task than interpolation. After all, interpolation guarantees that the sample lies within the dataset’s convex hull, while extrapolation leaves the entire remaining space as a valid sample position. Those terms have been ported as-is to various fields such as function approximation ( DeVore,, 1998 ) or machine learning ( Bishop,, 2006 ) , and an increasing amount of research papers in deep learning provide results and intuitions relying on data interpolation ( Belkin et al.,, 2018 ; Bietti and Mairal,, 2019 ; Adlam and Pennington,, 2020 ) . Beyond those, the following adage “as an algorithm transitions from interpolation to extrapolation, as its performance decreases” is commonly agreed upon. Before going further, we insist that throughout this manuscript, interpolation is to be understood as characterizing the data geometry as per Def. 1 . This is not to be mistaken with the often employed “interpolation regime” of models which occur whenever the latter has 0 0 training loss on the data ( Chatterji et al.,, 2021 ) . We shall see that interpolation/extrapolation and generalization performances do not seem as tightly related as previously thought.

Our goal in this paper is to demonstrate both theoretically and empirically for both synthetic and real data that interpolation almost surely never occurs in high-dimensional spaces ( > 100 >100 ) regardless of the underlying intrinsic dimension of the data manifold . That is, given the realistic amount of data that can be carried by current computational capacities, it is extremely unlikely that a newly observed sample lies in the convex hull of that dataset. Hence, we claim that • currently employed/deployed models are extrapolating

• given the super-human performances achieved by those models, extrapolation regime is not necessarily to be avoided, and is not an indicator of generalization performances

This paper is organized as follows. We first provide below (Thm. 1 ) an important theoretical result that has been derived in the context of Uniform samples from an hyper-ball. In that case, the probability of a new sample to be in interpolation regime from a dataset goes to 0 0 as the dimension d d increases unless the number of dataset samples grows exponentially with d d . This will allow to introduce notations and intuitions. We then directly provide empirical evidences in Sec. 2 using standard dataset where we demonstrate that even when considering a subset of the data dimensions, the probability to interpolate goes exponentially quickly to 0 0 with the number of considered dimensions. We conclude with Sec. 3 by providing existing theoretical results describing the probability that new samples are in interpolation or extrapolation regimes in more specific scenarios.

###### Theorem 1 ( Bárány and Füredi, (1988) ) .

Given a d d -dimensional dataset 𝑿 ≜ { 𝒙 1 , … , 𝒙 N } \boldsymbol{X}\triangleq\{\boldsymbol{x}_{1},\dots,\boldsymbol{x}_{N}\} with i.i.d. samples uniformly drawn from an hyperball, the probability that a new sample 𝒙 \boldsymbol{x} is in interpolation regime (recall Def. 1 ) has the following asymptotic behavior lim d → ∞ p ⁡ ( 𝒙 ∈ Hull ​ ( 𝑿 ) ⏟ interpolation ) = { 1 ⇔ N > d − 1 ​ 2 d / 2 0 ⇔ N < d − 1 ​ 2 d / 2 \lim_{d\rightarrow\infty}p(\underbrace{\boldsymbol{x}\in\text{Hull}(\boldsymbol{X})}_{\text{interpolation}})=\begin{cases}1\iff N>d^{-1}2^{d/2}\\ 0\iff N<d^{-1}2^{d/2}\\ \end{cases}

## 2 Interpolation is Doomed by the Curse of Dimensionality

In this section we propose various experiments supporting the need for exponentially large dataset to maintain interpolation, as per Thm. 1 , for non Gaussian data. First, we demonstrate in Sec. 2.1 the role of the underlying data manifold intrinsic dimension along with the role of the dimension of the smallest affine subspace that include the data manifold. As we will see from carefully designed datasets, only the latter has an impact on the probability of new samples being in an interpolation regime. We then move to real datasets in Sec. 2.2 and demonstrate that both in the data space or in various embedding spaces, current test set samples are all in extrapolation regime from their corresponding training set.

### 2.1 The Role of the Intrinsic, Ambient and Convex Hull Dimensions

d ∗ = d d^{*}=d

log ⁡ ( N ) \log(N)

p ​ ( 𝒙 ∈ Hull ​ ( 𝑿 ) ) p(\boldsymbol{x}\in\text{Hull}(\boldsymbol{X}))

d ∗ = 1 d^{*}=1 , nonlinear log ⁡ ( N ) \log(N)

d ∗ = 4 d^{*}=4 , linear log ⁡ ( N ) \log(N)

The first stage of our study consists in carefully understanding not only the role of the ambient dimension i.e. the dimension of the space in which the data lives, but also the role of the underlying data manifold intrinsic dimension i.e. the number of variables needed in a minimal representation of the data ( Bennett,, 1965 ) , and the dimension of the smallest affine subspace that includes all the data manifold.

In fact, one could argue that data such as images might lie on a low dimensional manifold and thus hope that interpolation occurs regardless of the high-dimensional ambient space. As we demonstrate in Fig. 1 , this intuition would be misleading. In fact, the underlying manifold dimension does not help even in the extreme case of having a 1 1 -dimensional manifold. What matters however, is the dimension d ∗ d^{*} of the smallest affine subspace that includes all the data manifold, or equivalently, the dimension of the convex hull of the data. As such, in the presence of a nonlinear manifold, we can see that the exponential requirement from Thm. 1 in the number of samples required to preserve a constant probability to be in interpolation grows exponentially with d ∗ d^{*} . In fact, with the intrinsic dimension ( d ∗ d^{*} ) constant, increasing the ambient space dimension ( d d ) has no impact on the number of samples needed to maintain interpolation regime as can be seen on the right of Fig. 1 . We thus conclude that for one to increase the probability to be in an interpolation regime, one should control d ∗ d^{*} , and not the manifold underlying dimension not the ambient space dimension .

N N

dimension index z z

We now propose to extend those insights to real data where the exact same behavior occurs across datasets.

### 2.2 Real Datasets and Embeddings are no Exception

The previous section explored the cases of synthetic data with varying ambient, intrinsic, and convex hull dimensions. This provided valuable insights e.g. the key quantity of interest lies in the dimension of the smallest affine subspace containing the data. For real dataset however, one could argue that some natural properties of such manifolds help in being in an interpolation regime. Furthermore, one could argue that once embedded in a suitable and non-degenerate latent space, e.g. from a learned deep network, interpolation occurs. As we will see through various experiments, even with real datasets and various popular embeddings, interpolation remains an elusive goal that becomes exponentially difficult to reach as the dimension grows.

Proportion of test set in interpolation regime

considered number of dimensions ( d ) (d)

MNIST CIFAR10 IMAGENET

considered number of sub-image dimensions (d)

considered number of principal components

Test set extrapolation in pixel-space. We first propose in Fig. 3 to study the proportion of the test set that is in interpolation regime from the train set for MNIST, CIFAR and Imagenet. To grasp the impact of the dimensionality of the data we propose to compute this proportion with varying number of dimensions obtained from two strategies. First, we only keep a specified amount of dimensions from the center of the images, second, we smooth and subsample the images. The former has the benefit of preserving the manifold geometry whilst only considering a limited amount of dimensions, the latter preserves the overall geometry of the manifold while removing the high-frequency structures (details of the image) and compressing the information on fewer dimensions. In both cases and throughout datasets, we see that despite the data manifold geometry held by natural images, finding samples in interpolation regime becomes exponentially difficult with respect to the considered data dimension .

Test set extrapolation in embedding-space. Given the above, one could argue that the key interest of machine learning is not to perform interpolation in the data space, but rather in a (learned) latent space. In fact, a DN provides a data embedding, then, in that space, a linear classifier (for example) solves the problem at hand, possibly in an interpolation regime. We thus provide in Tab. 1 the proportion of the test set that is in interpolation regime when considering different embedding spaces. We observed that embedding-spaces provide seemingly organized representations (with linear separability of the classes), yet, interpolation remains an elusive goal even for embedding-spaces of only 30 30 dimensions . Hence current deep learning methods operate almost surely in an extrapolation regime in both the data space, and their embedding space.

Test set extrapolation in dimensionality-reduction-space. The last set of experiments deals with the use of (non)linear dimensionality reduction techniques to visualize high-dimensional dataset. We pose the following question: is the interpolation/extrapolation information preserved by commonly employed dimensionality reduction techniques? To unequivocally answer this question, we create a data that consists of the 2 d 2^{d} vertices of an hypercube in d d dimensions for d = 8 , 12 d=8,12 . Those dataset have the specificity that any sample is in extrapolation regime with respect to the other samples. We propose in Fig. 5 the 2 2 -dimensional representations of those vertices using 8 8 different popular dimensionality reduction techniques: locally linear embedding ( Roweis and Saul,, 2000 ) denoted as LLE, modified LLE ( Zhang and Wang,, 2007 ) , Hessian eigenmaps ( Donoho and Grimes,, 2003 ) denoted as Hessian LLE, Laplacian eigenmaps ( Belkin and Niyogi,, 2003 ) denoted as SE, isomap ( Balasubramanian et al.,, 2002 ) , t-distributed stochastic neighbor embedding ( Van der Maaten and Hinton,, 2008 ) denoted as t-SNE, local tangent space alignment ( Zhang and Zha,, 2004 ) referred as LTSA, Multidimensional scaling ( Kruskal,, 1964 ) denoted as MDS. We observe that dimensionality reduction methods loose the interpolation/extrapolation information and lead to visual misconceptions significantly skewed towards interpolation .

Johnson–Lindenstrauss (di)lemma One last important setting concerns dimensionality reduction techniques that preserve -to some extent- the pairwise distances of the samples. Such techniques are often coined low-distortion embeddings, one of which follows from the Johnson–Lindenstrauss lemma (JLL) ( Johnson and Lindenstrauss,, 1984 ) . In short, the JLL guarantees the existence of a linear mapping f f with input dimension d d and output dimension d JLL ≥ 24 3 ​ ϵ 2 − 2 ​ ϵ 3 ​ log ⁡ ( N ) d_{\rm JLL}\geq\frac{24}{3\epsilon^{2}-2\epsilon^{3}}\log(N) with N N the size of the dataset such that the pairwise distances after projection will be within a 1 ± ϵ 1\pm\epsilon factor of the original distances. Different bounds have emerged based on different proofs of the JLL (see Dasgupta and Gupta, (2003) for a survey). Interestingly, as per Thm. 1 , the experiments from Fig. 1 and Fig. 3 , the dataset size must be of order 2 d 2^{d} to ensure that samples in the test set be in interpolation regime. In the JLL setting, this translates into d JLL > 24 3 ​ ϵ 2 − 2 ​ ϵ 3 ​ d > d d_{\rm JLL}>\frac{24}{3\epsilon^{2}-2\epsilon^{3}}d>d . In other words, if a dataset size N N is exponential with the dimension d d (required to have new samples in interpolation regime) then d JLL > d d_{\rm JLL}>d and JLL does not provide any dimensionality reduction .

We propose in the next section for the interested reader a brief collection of theoretical results that have also reached the conclusion that in high-dimensional spaces, exponentially large datasets are required to maintain the probability for a new sample to be in interpolation regimes.

## 3 Theoretical Quantification of Interpolation Probabilities

The previous section focuses on empirically evaluating the probability that a new sample falls into the convex hull of a given dataset and studied various settings concluding that interpolation suffers from the curse of dimensionality and is thus difficult to achieve in high-dimensional settings. As the convex hull is simply a polytope, we shall first refer the reader to Spielman and Teng, (2004) for a thorough study between various properties of such polytopes and their relation to the data dimension. We then provide some milestone theoretical results on computing the probability that samples are in interpolation/extrapolation regime, a problem often named as the convex position problem.

###### Definition 2 (Convex position problem) .

For a convex body K K in the space, let p ⁡ ( n , K ) p(n,K) denote the probability that n n random, independent, and uniform points from K K are in convex position, that is, none of the samples lies in the convex hull of the others.

Note that with this formulation, p ⁡ ( n , K ) p(n,K) describes the probability that any point in the set of samples is in extrapolation regime. Characterization of p ⁡ ( n , K ) p(n,K) for many 2 2 -dimensional bodies K K such as parallelograms and non-flat triangles are given below.

###### Theorem 2 ( Valtr, (1995) ; Valtr, (1996) ) .

The probability p ⁡ ( n , K ) p(n,K) for a parallelogram or a triangle is given by p ⁡ ( n , parallelogram ⏟ extrapolation ) = ( ( 2 ​ n − 2 n − 1 ) / n ! ) 2 and p ⁡ ( n , triangle ⏟ extrapolation ) = 2 n ​ ( 3 ​ n − 3 ) ! ( n − 1 ) ! 3 ( 2 n ) ! . \displaystyle p(\underbrace{n,{\rm parallelogram}}_{\text{extrapolation}})=\left(\begin{pmatrix}2n-2\\ n-1\end{pmatrix}/n!\right)^{2}\hskip 14.22636pt\text{ and }\hskip 14.22636ptp(\underbrace{n,{\rm triangle}}_{\text{extrapolation}})=\frac{2^{n}(3n-3)!}{(n-1)!^{3}(2n)!}.

Going to higher dimensional spaces has seen more challenging progresses making many existing results only valid in the limiting setting and when considering K K to be an hypersphere, as given in Thm. 1 and in the following result.

###### Theorem 3 ( Buchta, (1986) ) .

The probability p ⁡ ( n , K ) p(n,K) for K K a d d -dimensional hyperball B d B^{d} and n n growing linearly with d d has the following limit behavior , ∀ m > 3 , lim d → ∞ p ⁡ ( d + m , B d ⏟ extrapolation ) = 1 \forall m>3,\lim_{d\rightarrow\infty}p(\underbrace{d+m,B^{d}}_{\text{extrapolation}})=1

The above result effectively demonstrates that when sampling uniformly from an hyperball, the probability that all the points are in convex position (any sample lies outside of the other samples’ convex hull) is 1 1 when the number of samples grows linearly with the dimension, even when adding an arbitrary constant number of samples m m . This result nicely complements the one provided in Thm. 1 which was originally conjectured by Buchta, (1986) a few years prior being proven by Bárány and Füredi, (1988) . More recently, a non asymptotic result has been obtained characterizing p ⁡ ( n , K ) p(n,K) when the samples are obtained from Gaussian distributions.

###### Theorem 4 ( Kabluchko and Zaporozhets, (2020) ) .

Let 𝑿 \boldsymbol{X} consist of N N i.i.d. d d -dimensional samples from 𝒩 ⁡ ( 0 , I d ) \mathcal{N}(0,I_{d}) with N ≥ d + 1 N\geq d+1 , then for every σ ≥ 0 \sigma\geq 0 the probability that a new sample 𝒙 ∼ 𝒩 ⁡ ( 0 , σ 2 ​ I ​ d ) \boldsymbol{x}\sim\mathcal{N}(0,\sigma^{2}Id) is in extrapolation regime is given by p ⁡ ( 𝒙 ∉ Hull ​ ( 𝑿 ) ⏟ extrapolation ) = 2 ​ ( b N , d − 1 ​ ( σ 2 ) + b N , d − 3 ​ ( σ 2 ) + … ) \displaystyle p(\underbrace{\boldsymbol{x}\not\in\text{Hull}(\boldsymbol{X})}_{\text{extrapolation}})=2(b_{N,d-1}(\sigma^{2})+b_{N,d-3}(\sigma^{2})+\dots) with b n , k ( σ 2 ) = ( n k ) g k ( − σ 2 1 + k ​ σ 2 ) g n − k ( σ 2 1 + k ​ σ 2 ) , g n ( r ) = 1 2 ​ π ∫ − ∞ ∞ Φ n ( r x ) e − x 2 / 2 d x \displaystyle b_{n,k}(\sigma^{2})=\begin{pmatrix}n\\ k\end{pmatrix}g_{k}\left(-\frac{\sigma^{2}}{1+k\sigma^{2}}\right)g_{n-k}\left(\frac{\sigma^{2}}{1+k\sigma^{2}}\right),\;\;g_{n}(r)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\Phi^{n}\left(\sqrt{r}x\right)e^{-x^{2}/2}dx where r = i ​ − r \sqrt{r}=i\sqrt{-r} if r < 0 r<0 and b N , k = 0 b_{N,k}=0 for k ∉ { 0 , 1 , … , N } k\not\in\{0,1,\dots,N\} .

The above theorem provides the analytical quantities governing the probability to be in interpolation regime. Lastly, Majumdar et al., (2010) consider the case where the samples are obtained from random walks and obtain similar interpolation behaviors. There remain many avenues to provide specific results when the data belong to lower dimensional manifolds, or to consider anisotropic distributions.

## 4 Conclusion

Interpolation and extrapolation, as per Def. 1 , provide an intuitive geometrical characterization on the location of new samples with respect to a given dataset. Those terms are commonly used as geometrical proxy to predict a model’s performances on unseen samples and many have reached the conclusion that a model’s generalization performance depends on how a model interpolates. In other words, how accurate is a model within a dataset’s convex-hull defines its generalization performances. In this paper, we proposed to debunk this (mis)conception. In particular, we opposed the use of interpolation and extrapolation as indicators of generalization performances by demonstrating both from existing theoretical results and from thorough experiments that, in order to maintain interpolation for new samples, the dataset size should grow exponentially with respect to the data dimension. In short, the behavior of a model within a training set’s convex hull barely impacts that model’s generalization performance since new samples lie almost surely outside of that convex hull . This observation holds whether we are considering the original data space, or embeddings. We believe that those observations open the door to constructing better suited geometrical definitions of interpolation and extrapolation that align with generalization performances, especially in the context of high-dimensional data.

## References

Adlam and Pennington, (2020) Adlam, B. and Pennington, J. (2020). The neural tangent kernel in high dimensions: Triple descent and a multi-scale theory of generalization. In International Conference on Machine Learning , pages 74–84. PMLR.

Balasubramanian et al., (2002) Balasubramanian, M., Schwartz, E. L., Tenenbaum, J. B., de Silva, V., and Langford, J. C. (2002). The isomap algorithm and topological stability. Science , 295(5552):7–7.

Bárány and Füredi, (1988) Bárány, I. and Füredi, Z. (1988). On the shape of the convex hull of random points. Probability theory and related fields , 77(2):231–240.

Belkin et al., (2018) Belkin, M., Ma, S., and Mandal, S. (2018). To understand deep learning we need to understand kernel learning. In International Conference on Machine Learning , pages 541–549. PMLR.

Belkin and Niyogi, (2003) Belkin, M. and Niyogi, P. (2003). Laplacian eigenmaps for dimensionality reduction and data representation. Neural computation , 15(6):1373–1396.

Bennett, (1965) Bennett, R. S. (1965). Representation and analysis of signals part xxi. the intrinsic dimensionality of signal collections. Technical report, Johns Hopkins University.

Bietti and Mairal, (2019) Bietti, A. and Mairal, J. (2019). On the inductive bias of neural tangent kernels. arXiv preprint arXiv:1905.12173 .

Bishop, (2006) Bishop, C. M. (2006). Pattern recognition. Machine learning , 128(9).

Buchta, (1986) Buchta, C. (1986). On a conjecture of re miles about the convex hull of random points. Monatshefte für Mathematik , 102(2):91–102.

Chatterji et al., (2021) Chatterji, N. S., Long, P. M., and Bartlett, P. L. (2021). When does gradient descent with logistic loss find interpolating two-layer networks? Journal of Machine Learning Research , 22(159):1–48.

Dasgupta and Gupta, (2003) Dasgupta, S. and Gupta, A. (2003). An elementary proof of a theorem of johnson and lindenstrauss. Random Structures & Algorithms , 22(1):60–65.

DeVore, (1998) DeVore, R. A. (1998). Nonlinear approximation. Acta numerica , 7:51–150.

Donoho and Grimes, (2003) Donoho, D. L. and Grimes, C. (2003). Hessian eigenmaps: Locally linear embedding techniques for high-dimensional data. Proceedings of the National Academy of Sciences , 100(10):5591–5596.

Johnson and Lindenstrauss, (1984) Johnson, W. B. and Lindenstrauss, J. (1984). Extensions of lipschitz mappings into a hilbert space 26. Contemporary mathematics , 26.

Kabluchko and Zaporozhets, (2020) Kabluchko, Z. and Zaporozhets, D. (2020). Absorption probabilities for gaussian polytopes and regular spherical simplices. Advances in Applied Probability , 52(2):588–616.

Kolmogoroff, (1941) Kolmogoroff, A. (1941). Interpolation und extrapolation von stationaren zufalligen folgen. Izvestiya Rossiiskoi Akademii Nauk. Seriya Matematicheskaya , 5(1):3–14.

Kruskal, (1964) Kruskal, J. B. (1964). Multidimensional scaling by optimizing goodness of fit to a nonmetric hypothesis. Psychometrika , 29(1):1–27.

Majumdar et al., (2010) Majumdar, S. N., Comtet, A., and Randon-Furling, J. (2010). Random convex hulls and extreme value statistics. Journal of Statistical Physics , 138(6):955–1009.

Roweis and Saul, (2000) Roweis, S. T. and Saul, L. K. (2000). Nonlinear dimensionality reduction by locally linear embedding. science , 290(5500):2323–2326.

Spielman and Teng, (2004) Spielman, D. A. and Teng, S.-H. (2004). Smoothed analysis of algorithms: Why the simplex algorithm usually takes polynomial time. Journal of the ACM (JACM) , 51(3):385–463.

Valtr, (1995) Valtr, P. (1995). Probability thatn random points are in convex position. Discrete & Computational Geometry , 13(3-4):637–643.

Valtr, (1996) Valtr, P. (1996). The probability that n random points in a triangle are in convex position. Combinatorica , 16(4):567–573.

Van der Maaten and Hinton, (2008) Van der Maaten, L. and Hinton, G. (2008). Visualizing data using t-sne. Journal of machine learning research , 9(11).

Wiener, (1949) Wiener, N. (1949). Extrapolation, interpolation, and smoothing of stationary time series, with engineering applications.

Zhang and Wang, (2007) Zhang, Z. and Wang, J. (2007). Mlle: Modified locally linear embedding using multiple weights. In Advances in neural information processing systems , pages 1593–1600. Citeseer.

Zhang and Zha, (2004) Zhang, Z. and Zha, H. (2004). Principal manifolds and nonlinear dimensionality reduction via tangent space alignment. SIAM journal on scientific computing , 26(1):313–338.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
