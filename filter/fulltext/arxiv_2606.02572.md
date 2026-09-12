##### Report GitHub Issue

Content selection saved. Describe the issue below:

# VISReg: Variance-Invariance-Sketching Regularization for JEPA training

###### Abstract

Self-supervised learning methods prevent embedding collapse via modeling heuristics or explicit regularization of the embedding space. Among the latter, VICReg decomposes regularization into variance and covariance objectives, offering flexibility and interpretability. However, covariance captures only second-order statistics—encouraging decorrelation but failing to enforce the full distributional shape needed for stable training. Sketching-based methods such as SIGReg address this by aligning embeddings to an isotropic Gaussian, but lack flexibility and suffer from vanishing gradients under collapse. We propose Variance-Invariance-Sketching Regularization (VISReg), which replaces covariance with a Sliced-Wasserstein-based sketching objective that enforces full distributional shape, while retaining a variance term for scale control. By decoupling scale and shape, VISReg combines VICReg’s flexibility with the distributional rigor of sketching methods, providing robust gradients even under collapse. We show that VISReg scales linearly, outperforms existing regularization on low-quality datasets, and is resilient to long-tailed and low-rank regimes. Pre-trained on ImageNet-1K, VISReg achieves state-of-the-art performance on out-of-distribution datasets. Pre-trained on ImageNet-22K, it matches DINOv2’s OOD performance despite the latter using 10 × \times more data (LVD-142M). Project and code: https://haiyuwu.github.io/visreg .

###### Keywords:

## 1 Introduction

Self-supervised learning (SSL) has evolved from contrastive learning ( Chen et al., 2020a ; Chen et al., 2020b ; He et al., 2020 ; Chen et al., 2020c ; Chen et al., 2021 ) to Joint-Embedding Predictive Architectures ( LeCun et al., 2022 ; Assran et al., 2023 ; Caron et al., 2021 ; Zhou et al., 2021 ; Oquab et al., 2024 ; Siméoni et al., 2025 ) , which are more scalable and achieve stronger performance. Despite these advantages, many methods rely on heavy heuristics ( e.g., EMA, frozen layers, teacher-student architectures) to ensure training stability.

To remove such heuristics, VICReg ( Bardes et al., 2022 ) decomposes the training objective into variance, invariance, and covariance optimization. This approach largely reduces the engineering burden while achieving competitive performance. More recently, LeJEPA ( Balestriero & LeCun, 2025 ) proved that sketching the embedding space toward an isotropic Gaussian is an effective principle for ensuring training stability and strong downstream performance, and proposed SIGReg based on the Epps-Pulley test ( Epps & Pulley, 1983 ) and the Cramér-Wold theorem ( Cramér & Wold, 1936 ) to realize this.

However, both methods have clear limitations. VICReg regularizes covariance, which captures only second-order statistics. While this encourages decorrelation, it cannot enforce the full distributional shape of the embedding space—a distribution can match in mean and covariance yet remain far from Gaussian. This makes covariance regularization a comparatively weak proxy for the isotropy that stable, information-rich training requires. On the other hand, SIGReg addresses distributional shape directly through sketching, but it does not decouple scale from shape, limiting flexibility across training regimes. More critically, the gradient of the Epps-Pulley test diminishes as the embedding collapses (Figure 2 ), eventually vanishing entirely—precisely when a strong corrective signal is needed most.

Motivated by these complementary shortcomings, we propose V ariance- I nvariance- S ketching Reg ularization ( VISReg ). VISReg retains the variance term from VICReg to control the scale of the embedding space, but replaces covariance regularization with sketching regularization : we use the Sliced Wasserstein Distance (SWD) ( Bonneel et al., 2015 ) to align the normalized embedding distribution with an isotropic Gaussian prior along random 1D projections, thereby enforcing the full distributional shape. By decoupling scale and shape into separate objectives, VISReg inherits the interpretability and flexibility of VICReg’s decomposed losses while leveraging the distributional rigor of sketching-based methods—and provides a robust gradient signal even under collapse. Combined with a standard invariance loss, VISReg forms a complete, heuristic-free self-supervised learning method.

We compare VISReg with SIGReg, VICReg, and DINO on both standard and low-quality datasets. We find that DINO struggles to learn meaningful embeddings without careful hyperparameter tuning, while VISReg, SIGReg, and VICReg are all robust—but VISReg achieves the highest accuracy and the most stable training, particularly on low-rank and long-tailed datasets. Our hyperparameter analyses further provide clear guidance for methods grounded in the Cramér-Wold theorem.

We evaluate VISReg on linear classification, transfer learning, dense prediction, and image generation guidance, covering both in-domain and out-of-distribution (OOD) settings. We pretrain backbones on ImageNet-1K and evaluate on downstream datasets. First, despite a linear probe accuracy gap relative to the best method on in-domain data, VISReg achieves the best OOD results—one of the most important properties of a useful foundation model. Second, VISReg outperforms DINO ( Caron et al., 2021 ) with the same backbone after fine-tuning on both in-domain and OOD datasets, even though DINO has over 3% higher linear probe accuracy on in-domain data, indicating strong transfer learning capability. Third, a linear segmentation experiment shows VISReg performs on par with DINO for dense prediction, though a gap to the best models ( e.g., MoCoV3 ( Chen et al., 2021 ) , iBOT ( Zhou et al., 2021 ) ) remains. Finally, to test scaling, we pretrain ViT-L/14 on ImageNet-22K ( Ridnik et al., 2021 ) . VISReg achieves results comparable to DINOv2 ( Oquab et al., 2024 ) on OOD datasets, despite the latter being trained on a 10 × \times larger dataset (LVD-142M), demonstrating the strong potential of the VISReg approach.

The contributions of this work are: • We propose VISReg, which replaces the covariance regularization of VICReg with a sketching objective grounded in optimal transport, achieving stronger distributional control, better training stability, and resilience to low-quality datasets.

• We comprehensively analyze the hyperparameter landscape of VISReg and related Cramér-Wold-based methods, providing clear guidance for scaling and training stability within this paradigm.

• We demonstrate that VISReg’s embedding regularization yields superior OOD generalization and strong downstream task performance, broadening the practical utility of self-supervised foundation models.

## 2 Related Work

Contrastive Learning and Sampling Strategies. Early successes in self-supervised learning relied heavily on contrastive objectives, which maximize the similarity between positive pairs while pushing apart negative samples ( Chen et al., 2020a ; He et al., 2020 ; Misra & Maaten, 2020 ) . SimCLR ( Chen et al., 2020a ; Chen et al., 2020b ) demonstrated the importance of strong data augmentation and large batch sizes. To decouple batch size dependency, MoCo ( He et al., 2020 ; Chen et al., 2020c ) introduced a momentum queue to maintain a dynamic dictionary of negative samples. SwAV ( Caron et al., 2020 ) reformulated contrastive learning as an online clustering problem via the Sinkhorn-Knopp algorithm. However, these methods rely on negative pairs or prototypes, introducing sampling bias ( Chuang et al., 2020 ) and computational overhead for hard-negative mining ( Robinson et al., 2021 ) . Like other non-contrastive methods, VISReg eliminates the need for negative sampling entirely.

Masked Image Modeling (MIM). Inspired by BERT ( Devlin et al., 2019 ) in NLP, MIM approaches learn by reconstructing masked inputs. MAE ( He et al., 2022 ) and SimMIM ( Xie et al., 2022 ) operate on pixel-level reconstruction, demonstrating high scalability for fine-tuning tasks. BEiT ( Bao et al., 2022 ) proposes predicting discrete visual tokens. MaskFeat ( Wei et al., 2022 ) reconstructs HOG features to focus on structural information. Despite excelling in transfer learning, MIM methods typically learn lower-level spatial statistics and lag behind joint-embedding methods in linear probing due to weaker semantic linear separability ( Park et al., 2023 ; Baevski et al., 2022 ) .

Asymmetric Joint-Embedding Architectures. To avoid collapse without negatives, several methods introduce architectural asymmetry. BYOL ( Grill et al., 2020 ) and SimSiam ( Chen & He, 2021 ) rely on stop-gradient operations and predictor networks to break symmetry. Mean Teacher ( Tarvainen & Valpola, 2017 ) and DINO ( Caron et al., 2021 ; Oquab et al., 2024 ; Siméoni et al., 2025 ) utilize a momentum-updated teacher to stabilize training, with DINO further employing centering and sharpening. OBoW ( Gidaris et al., 2021 ) and MSN ( Assran et al., 2022 ) leverage prototype-based learning with asymmetric updates. Although effective, these methods rely on implicit regularization heuristics, making their non-collapse dynamics theoretically opaque ( Li et al., 2022 ) .

Geometric and Information-Theoretic Regularization. VISReg is most closely related to methods that explicitly regularize the statistical properties of embeddings. Barlow Twins ( Zbontar et al., 2021 ) minimizes redundancy in the cross-correlation matrix between twin networks. W-MSE ( Ermolov et al., 2021 ) projects embeddings onto the unit sphere and performs whitening. VICReg ( Bardes et al., 2022 ) explicitly constrains the variance, invariance, and covariance of embeddings to maximize information content. However, covariance regularization captures only second-order statistics—it encourages decorrelation but cannot enforce the full distributional shape of the embedding space. Moreover, methods like Barlow Twins and VICReg require computing covariance matrices, scaling quadratically as 𝒪 ⁡ ( D 2 ) \mathcal{O}(D^{2}) with embedding dimension D D .

LeJEPA ( Balestriero & LeCun, 2025 ) proved that regularizing the embedding space toward an isotropic Gaussian distribution can maintain stable heuristic-free training, and introduced SIGReg—grounded in the Epps-Pulley test ( Epps & Pulley, 1983 ) —to achieve this. While SIGReg provides stronger distributional control than covariance regularization and scales linearly as 𝒪 ⁡ ( D ) \mathcal{O}(D) , its regulation signal diminishes when the embedding collapses. KerJEPA ( Zimmermann et al., 2025 ) leverages MMD to estimate the regulation of infinite projections, but incurs O ⁡ ( N 2 ) O(N^{2}) complexity in batch size N N . A contemporary work, LpJEPA ( Kuang et al., 2026 ) , proposes Rectified Distribution Matching Regularization (RDMReg) to enforce embedding sparsity.

Our VISReg bridges VICReg and SIGReg: it retains VICReg’s variance term for scale control but replaces the covariance term with a sketching objective based on SWD ( Bonneel et al., 2015 ) , achieving full distributional shape regularization with robust gradients, decoupled scale-shape optimization, and linear complexity—making it well suited for scaling.

## 3 VISReg: Variance-Invariance-Sketching Regularization

VICReg ( Bardes et al., 2022 ) decomposes embedding regularization into variance and covariance terms, providing interpretability and flexibility. However, covariance regularization captures only second-order statistics: it encourages decorrelation among embedding dimensions but cannot enforce the full distributional shape of the embedding space. A distribution can match in mean and covariance yet remain far from the isotropic Gaussian that LeJEPA ( Balestriero & LeCun, 2025 ) proved to be optimal for stable, heuristic-free self-supervised training.

SIGReg ( Balestriero & LeCun, 2025 ) addresses this by directly sketching the embedding distribution toward an isotropic Gaussian via the Epps-Pulley test and the Cramér-Wold theorem. However, we identify two limitations: (1) its gradient diminishes as the embedding collapses (Figure 2 ), vanishing precisely when correction is needed most; and (2) it does not decouple scale from shape, limiting flexibility across training regimes.

VISReg resolves these limitations by replacing VICReg’s covariance term with a sketching objective while retaining the variance term for scale control. By decoupling regularization into distinct scale and shape objectives, VISReg provides robust gradients against collapse, distributional rigor beyond second-order statistics, and the flexibility to reweight objectives for different data regimes.

### 3.1 Regularization Loss

We decouple the regularization into scale and shape components, each operating independently. For simplicity, the number of augmentations V V is omitted from the derivation.

Scale Regularization. We regulate the scale of the embedding space using a variance constraint, following the same intuition as VICReg. Directly minimizing the KL divergence ( Kullback & Leibler, 1951 ) to an isotropic Gaussian prior incurs O ⁡ ( D 3 ) O(D^{3}) complexity. We relax this by factorizing into marginal distributions. Given the centered embedding 𝐙 ^ ∈ ℝ N × D \mathbf{\hat{Z}}\in\mathbb{R}^{N\times D} , the scale loss is: ℒ scale = 1 D ​ ∑ j = 1 D ( 1 − σ j ​ ( 𝐙 ^ ) ) 2 \mathcal{L}_{\mathrm{scale}}=\frac{1}{D}\sum_{j=1}^{D}(1-\sigma_{j}(\mathbf{\hat{Z}}))^{2} (1) where σ j ​ ( ⋅ ) \sigma_{j}(\cdot) denotes the standard deviation of the j j -th dimension. This formulation provides a gradient that approaches a constant during collapse, ensuring a reliable corrective signal.

Shape Regularization. Where VICReg uses covariance to encourage decorrelation—capturing only second-order statistics—we instead sketch the embedding distribution toward an isotropic Gaussian, enforcing full distributional shape. To isolate the geometric structure from magnitude, we normalize 𝐙 ^ \mathbf{\hat{Z}} : 𝐙 ~ = 𝐙 ^ s ​ g ​ ( σ ) + ϵ \mathbf{\widetilde{Z}}=\frac{\mathbf{\hat{Z}}}{sg(\sigma)+\epsilon} (2) The stop-gradient s ​ g ​ ( ⋅ ) sg(\cdot) decouples shape optimization from scale, ensuring gradients from the shape loss do not interfere with variance regulation. Unlike prior uses of stop-gradient as a collapse-prevention heuristic ( Grill et al., 2020 ; Chen & He, 2021 ) , here it serves a principled role in objective decomposition.

To efficiently align the high-dimensional distribution of 𝐙 ~ \mathbf{\widetilde{Z}} with the isotropic Gaussian prior, we leverage the Sliced Wasserstein Distance , grounded in the Cramér-Wold theorem ( Cramér & Wold, 1936 ) :

###### Lemma 3.1 (Cramér-Wold Theorem) .

Let μ \mu and ν \nu be two probability measures on ℝ d \mathbb{R}^{d} . The Radon transform ( Radon, 2005 ) ℛ \mathcal{R} , defined as ℛ ​ μ ​ ( θ , t ) := ∫ ℝ d δ ⁡ ( t − ⟨ x , θ ⟩ ) ​ 𝑑 μ ​ ( x ) \mathcal{R}\mu(\theta,t):=\int_{\mathbb{R}^{d}}\delta(t-\langle x,\theta\rangle)\,d\mu(x) along all directions θ ∈ 𝕊 d − 1 \theta\in\mathbb{S}^{d-1} , is injective. Thus: μ = ν ⇔ ℛ ​ μ ​ ( θ , ⋅ ) = ℛ ​ ν ​ ( θ , ⋅ ) , ∀ θ ∈ 𝕊 d − 1 . \mu=\nu\iff\mathcal{R}\mu(\theta,\cdot)=\mathcal{R}\nu(\theta,\cdot),\quad\forall\theta\in\mathbb{S}^{d-1}. (3)

This allows us to regularize the high-dimensional shape by aligning 1D random projections P k = 𝐙 ~ ​ w k P_{k}=\mathbf{\widetilde{Z}}w_{k} , where w k ∈ ℝ D w_{k}\in\mathbb{R}^{D} . Unlike SIGReg, which operates in the frequency domain via the Epps-Pulley test, we adopt the 2-Wasserstein distance ( 𝒲 2 \mathcal{W}_{2} ) , which admits an efficient closed-form solution in 1D ( Peyré et al., 2019 ; Bonneel et al., 2015 ; Deshpande et al., 2018 ) :

###### Lemma 3.2 (1D Wasserstein Closed-Form) .

For one-dimensional distributions, the p p -th Wasserstein distance equals the L p L_{p} distance between quantile functions. For discrete empirical samples of size N N : 𝒲 p p ​ ( μ ^ , ν ^ ) = 1 N ​ ∑ i = 1 N ‖ x ( i ) − y ( i ) ‖ p , \mathcal{W}_{p}^{p}(\hat{\mu},\hat{\nu})=\frac{1}{N}\sum_{i=1}^{N}\|x_{(i)}-y_{(i)}\|^{p}, (4) where x ( i ) x_{(i)} denotes the i i -th order statistic.

Leveraging Lemma 3.2 with p = 2 p=2 , the shape loss is: ℒ shape = 1 K ​ ∑ k = 1 K ‖ sort ⁡ ( 𝐙 ~ ​ w k ) − 𝐪 𝒩 ‖ 2 2 , \mathcal{L}_{\mathrm{shape}}=\frac{1}{K}\sum_{k=1}^{K}\left\|\mathrm{sort}(\mathbf{\widetilde{Z}}w_{k})-\mathbf{q}_{\mathcal{N}}\right\|_{2}^{2}, (5) where sort ⁡ ( ⋅ ) \mathrm{sort}(\cdot) sorts the projected values in each direction, and 𝐪 𝒩 ∈ ℝ N \mathbf{q}_{\mathcal{N}}\in\mathbb{R}^{N} represents the fixed quantiles of the standard Gaussian distribution. This is strictly more expressive than covariance regularization: it enforces not just decorrelation but the full marginal distribution along every projected direction.

Additionally, empirical results suggest that regularizing the embedding center increases training robustness, so we include a centering loss: ℒ center = ‖ μ ‖ 2 2 \mathcal{L}_{\mathrm{center}}=\|\mu\|_{2}^{2} (6) where μ \mu is the batch mean.

###### Proposition 3.3 (VISReg Regularization Objective) .

The regularization loss ℒ Reg \mathcal{L}_{\mathrm{Reg}} optimizes variance and distributional shape independently: ℒ Reg = λ scale ​ ℒ scale + λ shape ​ ℒ shape + λ center ​ ℒ center \mathcal{L}_{\mathrm{Reg}}=\lambda_{\mathrm{scale}}\,\mathcal{L}_{\mathrm{scale}}+\lambda_{\mathrm{shape}}\,\mathcal{L}_{\mathrm{shape}}+\lambda_{\mathrm{center}}\,\mathcal{L}_{\mathrm{center}} (7)

The code is shown in Algorithm 1 . Decoupling introduces three hyperparameters; we conduct ablations in Table 12 . The default λ ∗ = 1 \lambda_{*}=1 works well for high-quality datasets, but increasing the shape loss weight improves performance on low-quality datasets.

For the invariance objective, we follow LeJEPA ( Balestriero & LeCun, 2025 ) : ℒ pred = 1 V ​ ∑ i = 1 V ‖ μ g − z i ‖ 2 2 \mathcal{L}_{\mathrm{pred}}=\frac{1}{V}\sum_{i=1}^{V}\|\mu_{g}-z_{i}\|_{2}^{2} (8) where V V is the number of views, μ g \mu_{g} is the mean embedding of global views, and z i z_{i} includes both global and local view embeddings. The full VISReg objective is: ℒ VISReg = ( 1 − λ ) ​ ℒ pred + λ ​ ℒ Reg \mathcal{L}_{\mathrm{VISReg}}=(1-\lambda)\,\mathcal{L}_{\mathrm{pred}}+\lambda\,\mathcal{L}_{\mathrm{Reg}} (9)

Ablation results for each component are in Section B .

### 3.2 VISReg Is Friendly to Scale Up

One practical advantage inherited from the Cramér-Wold framework is favorable scaling behavior. Due to limited computational resources, we analyze scalability through algorithm complexity, simulated scaling cost, and experiments on a small yet challenging dataset.

###### Definition 3.4 .

Let the input feature 𝐙 ∈ ℝ N × D \mathbf{Z}\in\mathbb{R}^{N\times D} , where N N is the mini-batch size and D D is the projection dimension. The number of random slices is K K .

The complexity of ℒ Reg \mathcal{L}_{\mathrm{Reg}} is dominated by two operations: 𝒞 Reg = O ⁡ ( N ​ D ​ K ) ⏟ projection + O ⁡ ( K ​ N ​ log ⁡ N ) ⏟ sorting \mathcal{C}_{\mathrm{Reg}}=\underbrace{O(NDK)}_{\text{projection}}+\underbrace{O(KN\log N)}_{\text{sorting}} (10) Since log ⁡ N ≪ D \log N\ll D at scale, the effective complexity is: 𝒞 Reg = O ⁡ ( N ​ D ​ K ) \mathcal{C}_{\mathrm{Reg}}=O(NDK) (11) This is linear in all scaling parameters—compared to VICReg’s O ⁡ ( N ​ D 2 ) O(ND^{2}) from covariance computation. We next analyze the effects of batch size N N , projection dimension D D , and number of slices K K .

Analysis in N N . We simulate the running time and memory demand of popular regularization methods ( Zbontar et al., 2021 ; Bardes et al., 2022 ; Balestriero & LeCun, 2025 ) at scale. Since VISReg is based on SWD, we also include vanilla SWD. Figure 3 shows that SWD-based methods are more efficient in both speed and memory. The 17-knot sampling required by the Epps-Pulley test slows SIGReg down. We conclude that VISReg scales efficiently in batch size.

Lemma 3.1 establishes that we can regulate D D -dimensional space by aligning K K 1D slices, so the relationship between K K and D D is important for scaling. We analyze this by reporting the online linear probe accuracy of ViT-S/8 ( Dosovitskiy et al., 2021 ) on ImageNette 1 1 1 https://github.com/fastai/imagenette ( Deng et al., 2009 ) , comparing SIGReg ( Balestriero & LeCun, 2025 ) (CF-based) with SWD ( Bonneel et al., 2015 ) and VISReg (OT-based). Unless stated otherwise, we use a batch size of 256, a learning rate of 10 − 3 10^{-3} without decay, 4 global views with a cropping ratio (0.08, 1). The λ \lambda weights for SIGReg, SWD, and VISReg are 0.02, 0.6, and 0.6, respectively. Models are trained on a single H100 GPU for 800 epochs; we report the highest accuracy.

Analysis in D D . With a sufficient number of slices ( K = 4096 K=4096 ), we vary the projection dimension D D . Figure 4 reveals three patterns: (1) OT-based methods regularize dimensions more efficiently than the CF-based method; (2) with sufficient K K , VISReg learns better semantically meaningful embeddings; (3) K K must exceed D D by a factor C > 1 C>1 for optimal accuracy, and VISReg requires the smallest C C . The third observation suggests that K K cannot be treated as independent of D D , converting the effective complexity from O ⁡ ( N ​ D ​ K ) O(NDK) to O ⁡ ( N ​ D ⋅ C ​ D ) O(ND\cdot CD) . We address this below.

Analysis in K K . Fixing D = 256 D=256 and varying K K , Figure 5 shows: (1) OT-based methods remain robust even at K = 1 8 ​ D K=\frac{1}{8}D ; (2) VISReg is the most robust approach, consistently achieving the highest linear probe accuracy.

Despite VISReg’s robustness, the correlation between K K and D D remains a concern for complexity. Revisiting Lemma 3.2 and Algorithm 1 , we observe that K K random slices are generated independently per GPU, so one can generate C ​ D M \frac{CD}{M} slices on each of M M GPUs to obtain K = C ​ D K=CD total slices. For example, 128 slices per GPU on 8 GPUs should match 1024 slices on one GPU.

Figure 6 confirms this. With one GPU, the accuracy gap between K = 128 K=128 and K = 1024 K=1024 reaches 13.88% for SIGReg, 2.21% for SWD, and 2.44% for VISReg. With 8 GPUs and the same per-GPU K K , the gap shrinks to 0.27%, 0.24%, and 0.22% respectively. Given nondeterministic training, these results support our claim. Thus, K K can remain constant when scaling, preserving the O ⁡ ( N ​ D ​ K ) O(NDK) complexity.

### 3.3 VISReg Is Robust to Low-Quality Datasets

Low-quality datasets pose challenges from many angles. We evaluate on ImageNet-LT ( Liu et al., 2019 ) (long-tailed) and Galaxy10 ( Leung, 2025 ) (low-rank). Training settings follow the previous section except l ​ r = 10 − 4 lr=10^{-4} , K = 4096 K=4096 , D = 256 D=256 , with images resized to 128px. We include DINO ( Caron et al., 2021 ) and VICReg as baselines. Models are trained from scratch for 400 epochs to simulate real-world scenarios where suitable pretrained models do not exist—a common challenge in domains like AI for Science.

ImageNet-LT is a long-tailed variant of ImageNet-1K containing 115K images from 1K classes, categorized into many-shot, medium-shot, and few-shot. Table 1 shows that VISReg outperforms all methods at all levels after adjusting the shape loss weight (details in Table 12 ), whereas DINO fails to learn meaningful embeddings.

Galaxy10 comprises 17,736 galaxy images from 10 classes. We treat it as low-rank because: (1) it has 10 classes with limited training data, below the capacity of ViT-S/8; and (2) most images contain a large ratio of black pixels, limiting useful content. Table 2 shows that all four regularization methods prevent collapse and achieve good accuracy, but DINO struggles to learn meaningful embeddings.

Summary of Analyses. First, VISReg has complexity O ⁡ ( N ​ D ​ K ) O(NDK) , linear in all scaling factors—an improvement over VICReg’s O ⁡ ( N ​ D 2 ) O(ND^{2}) . Second, we observe that K K is correlated with D D by a factor C > 1 C>1 , but prove that distributing slices across M M GPUs resolves this, keeping K K constant at scale. Third, VISReg outperforms existing methods in training efficiency, effectiveness, and robustness. Fourth, VISReg is more resilient to low-quality datasets through loss reweighting—demonstrating the importance of decoupling scale and shape over the monolithic covariance or sketching approaches. All these results confirm that VISReg is a practical and principled regularization method for real-world self-supervised learning.

## 4 Experiment

This section covers the ablation study of hyperparameter settings, the effect of projection dimension on downstream tasks, and comparisons between VISReg and existing methods in linear probe, transfer learning, domain shifting, dense instance prediction, and image generation guidance.

### 4.1 Ablation study

Unlike previous works ( Caron et al., 2021 ; Chen et al., 2021 ; Assran et al., 2023 ) relying on heuristics for training stability, VISReg only has four hyper-parameters to tune. Unless stated otherwise, the training set is ImageNet1K, the backbone is ViT-B/16, the number of slices is 4096 per GPU, the augmentation settings follow LeJEPA ( Balestriero & LeCun, 2025 ) with 2 global views and 6 local views, and the training epoch is 100. We report the online linear probe accuracy on ImageNet1K to analyze the effect of hyper-parameters, as shown in Table 3 .

Effect of λ \lambda . Different from SIGReg, scaling the regularization loss with batch size to maintain the batch size invariance, VISReg is naturally batch invariant, so a large λ \lambda value is needed to ensure the contribution of VISReg in the gradient. For small datasets, e.g., ImageNette and Galaxy10, 0.6 is a good start. For large datasets, e.g., ImageNet1K, 0.9 is a good start.

Effect of learning rate. Similar to the other methods, 5e-4 to 1e-3 is the optimal range for the training on ImageNet1K. When training on a large dataset, 9e-4 is a good start.

Effect of batch size. Grounded in the same theorem as LeJEPA, VISReg is also robust to a small batch size. Different from LeJEPA, the VISReg algorithm in VISReg benefits from a large batch size in regularizing the embedding space. Hence, we recommend reducing λ \lambda when observing a fast accuracy saturation with a large batch size.

Effect of projection dimension. Similar to previous works, we use a 3-layer MLP as the projection layer to apply regularization. Different from previous works, the final projection dimension not only decides the information bandwidth but also the difficulty of the regularization process, i.e., the lower dimension the easier. To investigate the trade-off, we increase the training epochs to 300 and test the model performance under four projection dimension settings.

The investigation includes three aspects: in-domain, OOD, and segmentation. Following the settings in DINOv2 ( Oquab et al., 2024 ) , we run offline linear probe on ImageNet1K and linear segmentation on ADE20K ( Zhou et al., 2017 ) . The full-shot linear probe performance of the other datasets ( Maji et al., 2013 ; Krause et al., 2013 ; Krizhevsky et al., 2009 ; Nilsback & Zisserman, 2008 ; Parkhi et al., 2012 ; Cimpoi et al., 2014 ; Wang et al., 2017 ) is reported for pattern observation.

Starting at the in-domain results, one observation is that a larger projection dimension results in a higher accuracy. With the embedding size 768 of ViT-B/16, projection dimension 512 gives the highest overall accuracy and 64 gives the lowest average accuracy. This indicates that projection dimension can be the bottleneck for in-domain classification. Focusing on the OOD datasets, the observation is that a smaller projection dimension limits the OOD performance, but a larger dimension might lead to over-parameterization and training set memorization. Interestingly, the smallest the projection dimension outperforms the largest one. Lastly, we observe that a smaller projection dimension leads to a better performance on dense instance prediction. We choose 256 as the optimal setting in the training.

### 4.2 General comparison

Linear probe, transfer learning, and domain shifting are three key aspects of evaluating the efficacy of a SSL foundation model. We compare VISReg with seven existing methods that are widely used in the real-world applications. In addition, we add the segmentation and generation tasks to evaluate VISReg on dense instance prediction and semantic meaning guidance for generation.

Datasets. The base training set is ImageNet1K ( Deng et al., 2009 ) . There are 15 datasets used to cover the general comparison experiment. 8 of them are in-domain datasets: FGVC-aircraft ( Maji et al., 2013 ) , Stanford cars ( Krause et al., 2013 ) , Cifar10 & Cifar100 ( Krizhevsky et al., 2009 ) , Oxford 102 flowers ( Nilsback & Zisserman, 2008 ) , Food 101 ( Bossard et al., 2014 ) , Oxford-IIIT Pet ( Parkhi et al., 2012 ) , and ImageNet1K. 6 of them are OOD datasets: Describable Textures Dataset (DTD) ( Cimpoi et al., 2014 ) , Galaxy10 ( Leung, 2025 ) , ChestXRay ( Wang et al., 2017 ) , Aerial Image Dataset (AID) ( Xia et al., 2017 ) , RetinaMNIST ( Liu et al., 2022 ) , and OrganAMNIST ( Bilic et al., 2023 ) . The last dataset is ADE20K ( Zhou et al., 2017 ) for dense instance prediction. The details are in A.3 .

Training settings. We choose two commonly used backbones, ViT-B/16 and ViT-L/14, to run the experiments. ViT-B/16 uses the best hyperparameters in Table 3 and Table 4 . ViT-L/14 is trained with {learning rate=8e-4, λ \lambda =0.7, batch size=512, projection dim=384}. Both backbones are trained for 400 epochs and 4 global + 6 local views are used. The other settings follow LeJEPA ( Balestriero & LeCun, 2025 ) . We directly use the timm package to create the model and load the pre-trained weights.

Downstream task evaluation settings. The linear probe, transfer learning, and linear segmentation experiments use the same settings as DINOv2 ( Oquab et al., 2024 ) . The only difference is that the training epoch of linear probe on downstream datasets is 10. We only compare with the models that are pre-trained on ImageNet1K.

VISReg has a competitive in-domain performance. Table 5 groups the methods based on the heuristics utilization. Within the w/o heuristics group, VISReg has a stronger in-domain performance than MAE ( He et al., 2022 ) and LeJEPA ( Balestriero & LeCun, 2025 ) , achieving 75.7% accuracy with ViT-B/16 and 77.0% accuracy with ViT-L/14 on ImageNet1K. Moreover, VISReg achieves the best average accuracy on downstream datasets. Comparing to the w/ heuristics methods, there is still an accuracy gap. Despite the accuracy gap on in-domain datasets, VISReg indicates a stronger performance on DTD, the only OOD dataset in the table. Note that the ViT-B/16 of VISReg even outperforms the ViT-L and ViT-H of the other methods. This intriguing observation motivates the extended experiments on more OOD datasets.

VISReg has a better OOD performance. Due to the lack of OOD evaluations in previous work, we select 6 datasets from distinct domains: ChestXRay, RetinaMNIST, and OrganAMNIST are from medical domain, Galaxy10 is from space domain, and AID has the aerial images. The results in Table 6 suggest that VISReg helps the model learn more general features than the other methods. Without using training heuristics, VISReg achieves the best average accuracy comparing with all methods and backbone scales. Moreover, after scaling the training set to ImageNet22K, VISReg with ViT-L/14 backbone achieves a comparable accuracy to DINOv2, which was trained with a 10x larger training set. This indicates the generality of the representations learned by VISReg. This advantage also benefits the transfer learning capability.

VISReg has a good transfer learning capability. We conduct a transfer learning experiment on CIFAR10 & CIFAR100, Flowers, ImageNet1K, and Galaxy10. To have a fair comparison with DINO, the backbone is ViT-B/16 and the fine-tuning follows DINO ( Caron et al., 2021 ) implementation. An important observation is that, although VISReg does not have a better linear projection accuracy on in-domain datasets than DINO, the fine-tuning results are consistently higher than both supervised learning ( Touvron et al., 2021 ) and DINO. In addition, the advantage of VISReg on OOD datasets still remains.

VISReg shows an on-par performance on dense instance prediction. Following DINOv2 ( Oquab et al., 2024 ) , we conduct a simple linear segmentation experiment on ADE20K and the mIoU result is reported. Table 8 indicates that, without using any heuristics, VISReg can still provide a good segmentation results. Nevertheless, there is still a large gap comparing with MoCoV3 and iBOT, which is an important aspect that we will work on.

VISReg provides a good guidance to speed up the training of generative models. Another important application of foundation model is to speed up the training process of generative model ( Yu et al., 2025 ; Singh et al., 2025 ) . We use the official code of iREPA ( Singh et al., 2025 ) and run a lightweight training on SiT-B/2 for 100K steps with the features from VISReg and DINO. We use the default settings for both training and generation. The results in Table 9 suggest that VISReg provides useful embeddings.

## 5 Conclusion

This paper proposes VISReg, a self-supervised learning method that does not rely on heuristics for training stability. We present its effectiveness on model scaling, training stability, and training efficiency. In addition, we show that VISReg and its alike method is more robust to low-quality datasets than DINO, which is helpful in real-world applications. Last, we conduct extensive experiments to evaluate its performance in important aspects of a foundation model training method. It is intriguing that VISReg has a stronger performance on OOD data and transfer learning. With this potential, we hope this technical path can enhance the usefulness of the foundation models.

## 6 Acknowledgment

We appreciate Prof. Yann LeCun’s efforts in connecting resources and people to bring this project to fruition.

## References

Assran et al. (2022) Assran, M., Caron, M., Misra, I., Bojanowski, P., Bordes, F., Vincent, P., Joulin, A., Rabbat, M., and Ballas, N. Masked siamese networks for label-efficient learning. In ECCV , 2022.

Assran et al. (2023) Assran, M., Duval, Q., Misra, I., Bojanowski, P., Vincent, P., Rabbat, M., LeCun, Y., and Ballas, N. Self-supervised learning from images with a joint-embedding predictive architecture. In CVPR , 2023.

Baevski et al. (2022) Baevski, A., Hsu, W.-N., Xu, Q., Babu, A., Gu, J., and Auli, M. Data2vec: A general framework for self-supervised learning in speech, vision and language. In ICML , 2022.

Balestriero & LeCun (2025) Balestriero, R. and LeCun, Y. Lejepa: Provable and scalable self-supervised learning without the heuristics. arXiv preprint arXiv:2511.08544 , 2025.

Bao et al. (2022) Bao, H., Dong, L., Piao, S., and Wei, F. BEiT: BERT pre-training of image transformers. In ICLR , 2022.

Bardes et al. (2022) Bardes, A., Ponce, J., and LeCun, Y. Vicreg: Variance-invariance-covariance regularization for self-supervised learning. ICLR , 2022.

Bilic et al. (2023) Bilic, P., Christ, P., Vorontsov, E., and et al. The liver tumor segmentation benchmark (lits). Medical Image Analysis , 2023.

Bonneel et al. (2015) Bonneel, N., Rabin, J., Peyré, G., and Pfister, H. Sliced and radon wasserstein barycenters of measures. Journal of Mathematical Imaging and Vision , 51(1):22–45, 2015.

Bossard et al. (2014) Bossard, L., Guillaumin, M., and Van Gool, L. Food-101 – mining discriminative components with random forests. In ECCV , 2014.

Caron et al. (2020) Caron, M., Misra, I., Mairal, J., Goyal, P., Bojanowski, P., and Joulin, A. Unsupervised learning of visual features by contrasting cluster assignments. NeurIPS , 2020.

Caron et al. (2021) Caron, M., Touvron, H., Misra, I., Jégou, H., Mairal, J., Bojanowski, P., and Joulin, A. Emerging properties in self-supervised vision transformers. In ICCV , 2021.

Chen et al. (2020a) Chen, T., Kornblith, S., Norouzi, M., and Hinton, G. A simple framework for contrastive learning of visual representations. In ICLR , pp. 1597–1607, 2020a.

Chen et al. (2020b) Chen, T., Kornblith, S., Swersky, K., Norouzi, M., and Hinton, G. E. Big self-supervised models are strong semi-supervised learners. Advances in neural information processing systems , 33:22243–22255, 2020b.

Chen & He (2021) Chen, X. and He, K. Exploring simple siamese representation learning. In CVPR , pp. 15750–15758, 2021.

Chen et al. (2020c) Chen, X., Fan, H., Girshick, R., and He, K. Improved baselines with momentum contrastive learning. arXiv preprint arXiv:2003.04297 , 2020c.

Chen et al. (2021) Chen, X., Xie, S., and He, K. An empirical study of training self-supervised vision transformers. In ICCV , pp. 9640–9649, 2021.

Chuang et al. (2020) Chuang, C.-Y., Robinson, J., Lin, Y.-C., Torralba, A., and Jegelka, S. Debiased contrastive learning. NeurIPS , 2020.

Cimpoi et al. (2014) Cimpoi, M., Maji, S., Kokkinos, I., Mohamed, S., and Vedaldi, A. Describing textures in the wild. In CVPR , 2014.

Cramér & Wold (1936) Cramér, H. and Wold, H. Some theorems on distribution functions. Journal of the London Mathematical Society , 1(4):290–294, 1936.

Deng et al. (2009) Deng, J., Dong, W., Socher, R., Li, L.-J., Li, K., and Fei-Fei, L. Imagenet: A large-scale hierarchical image database. In CVPR , 2009.

Deshpande et al. (2018) Deshpande, I., Zhang, Z., and Schwing, A. G. Generative modeling using the sliced wasserstein distance. In CVPR , pp. 3483–3491, 2018.

Devlin et al. (2019) Devlin, J., Chang, M.-W., Lee, K., and Toutanova, K. Bert: Pre-training of deep bidirectional transformers for language understanding. In Proceedings of the 2019 conference of the North American chapter of the association for computational linguistics: human language technologies, volume 1 (long and short papers) , pp. 4171–4186, 2019.

Dhariwal & Nichol (2021) Dhariwal, P. and Nichol, A. Diffusion models beat gans on image synthesis. Advances in neural information processing systems , 34:8780–8794, 2021.

Dosovitskiy et al. (2021) Dosovitskiy, A., Beyer, L., Kolesnikov, A., Weissenborn, D., Zhai, X., Unterthiner, T., Dehghani, M., Minderer, M., Heigold, G., Gelly, S., Uszkoreit, J., and Houlsby, N. An image is worth 16x16 words: Transformers for image recognition at scale. In ICLR , 2021.

Epps & Pulley (1983) Epps, T. W. and Pulley, L. B. A test for normality based on the empirical characteristic function. Biometrika , 70(3):723–726, 1983.

Ermolov et al. (2021) Ermolov, A., Siarohin, A., Sangineto, E., and Sebe, N. Whitening for self-supervised representation learning. In International conference on machine learning , pp. 3015–3024. PMLR, 2021.

Gidaris et al. (2021) Gidaris, S., Bursuc, A., Puy, G., Komodakis, N., Cord, M., and Pérez, P. Obow: Online bag-of-visual-words generation for self-supervised learning. In CVPR , 2021.

Grill et al. (2020) Grill, J.-B., Strub, F., Altché, F., Tallec, C., Richemond, P., Buchatskaya, E., Doersch, C., Avila Pires, B., Guo, Z., Gheshlaghi Azar, M., et al. Bootstrap your own latent-a new approach to self-supervised learning. NeurIPS , pp. 21271–21284, 2020.

He et al. (2020) He, K., Fan, H., Wu, Y., Xie, S., and Girshick, R. Momentum contrast for unsupervised visual representation learning. In CVPR , 2020.

He et al. (2022) He, K., Chen, X., Xie, S., Li, Y., Dollár, P., and Girshick, R. Masked autoencoders are scalable vision learners. In CVPR , 2022.

Krause et al. (2013) Krause, J., Stark, M., Deng, J., and Fei-Fei, L. 3d object representations for fine-grained categorization. In 3dRR , 2013.

Krizhevsky et al. (2009) Krizhevsky, A., Hinton, G., et al. Learning multiple layers of features from tiny images. 2009.

Kuang et al. (2026) Kuang, Y., Dagade, Y., Rudner, T. G., Balestriero, R., and LeCun, Y. Rectified lpjepa: Joint-embedding predictive architectures with sparse and maximum-entropy representations. arXiv preprint arXiv:2602.01456 , 2026.

Kullback & Leibler (1951) Kullback, S. and Leibler, R. A. On information and sufficiency. The annals of mathematical statistics , 22(1):79–86, 1951.

LeCun et al. (2022) LeCun, Y. et al. A path towards autonomous machine intelligence version 0.9. 2, 2022-06-27. Open Review , 2022.

Leung (2025) Leung, H. Galaxy10 DECaLS Dataset. https://astronn.readthedocs.io/en/latest/galaxy10.html , 2025. Accessed: 2026-01-11.

Li et al. (2022) Li, A. C., Efros, A. A., and Pathak, D. Understanding collapse in non-contrastive siamese representation learning. In ECCV , 2022.

Liu et al. (2022) Liu, R., Wang, X., Wu, Q., and et al. Deepdrid: Diabetic retinopathy—grading and image quality estimation challenge. Patterns , 2022.

Liu et al. (2019) Liu, Z., Miao, Z., Zhan, X., Wang, J., Gong, B., and Yu, S. X. Large-scale long-tailed recognition in an open world. In CVPR , 2019.

Maji et al. (2013) Maji, S., Rahtu, E., Kannala, J., Blaschko, M., and Vedaldi, A. Fine-grained visual classification of aircraft. arXiv preprint arXiv:1306.5151 , 2013.

Misra & Maaten (2020) Misra, I. and Maaten, L. v. d. Self-supervised learning of pretext-invariant representations. In CVPR , 2020.

Nilsback & Zisserman (2008) Nilsback, M.-E. and Zisserman, A. Automated flower classification over a large number of classes. In ICVGIP , 2008.

Oquab et al. (2024) Oquab, M., Darcet, T., Moutakanni, T., Vo, H., Szafraniec, M., Khalidov, V., Fernandez, P., Haziza, D., Massa, F., El-Nouby, A., et al. Dinov2: Learning robust visual features without supervision. T-MLR , 2024.

Park et al. (2023) Park, N., Kim, W., Heo, B., Kim, T., and Yun, S. What do self-supervised vision transformers learn? ICLR , 2023.

Parkhi et al. (2012) Parkhi, O. M., Vedaldi, A., Zisserman, A., and Jawahar, C. Cats and dogs. In CVPR , 2012.

Peyré et al. (2019) Peyré, G., Cuturi, M., et al. Computational optimal transport: With applications to data science. Foundations and Trends® in Machine Learning , 11(5-6):355–607, 2019.

Radon (2005) Radon, J. 1.1 über die bestimmung von funktionen durch ihre integralwerte längs gewisser mannigfaltigkeiten. Classic papers in modern diagnostic radiology , 5(21):124, 2005.

Ridnik et al. (2021) Ridnik, T., Ben-Baruch, E., Noy, A., and Zelnik-Manor, L. Imagenet-21k pretraining for the masses. arXiv preprint arXiv:2104.10972 , 2021.

Robinson et al. (2021) Robinson, J., Chuang, C.-Y., Sra, S., and Jegelka, S. Contrastive learning with hard negative samples. ICLR , 2021.

Siméoni et al. (2025) Siméoni, O., Vo, H. V., Seitzer, M., Baldassarre, F., Oquab, M., Jose, C., Khalidov, V., Szafraniec, M., Yi, S., Ramamonjisoa, M., et al. Dinov3. arXiv preprint arXiv:2508.10104 , 2025.

Singh et al. (2025) Singh, J., Leng, X., Wu, Z., Zheng, L., Zhang, R., Shechtman, E., and Xie, S. What matters for representation alignment: Global information or spatial structure? arXiv preprint arXiv:2512.10794 , 2025.

Tarvainen & Valpola (2017) Tarvainen, A. and Valpola, H. Mean teachers are better role models: Weight-averaged consistency targets improve semi-supervised deep learning results. Advances in neural information processing systems , 30, 2017.

Touvron et al. (2021) Touvron, H., Cord, M., Douze, M., Massa, F., Sablayrolles, A., and Jégou, H. Training data-efficient image transformers & distillation through attention. In ICML , 2021.

Wang et al. (2017) Wang, X., Peng, Y., Lu, L., Lu, Z., Bagheri, M., and Summers, R. M. Chestx-ray8: Hospital-scale chest x-ray database and benchmarks on weakly-supervised classification and localization of common thorax diseases. In CVPR , 2017.

Wei et al. (2022) Wei, C., Fan, H., Xie, S., Wu, C.-Y., Yuille, A., and Feichtenhofer, C. Masked feature prediction for self-supervised visual pre-training. In CVPR , 2022.

Xia et al. (2017) Xia, G.-S., Hu, J., Hu, F., Shi, B., Bai, X., Zhong, Y., Zhang, L., and Lu, X. Aid: A benchmark data set for performance evaluation of aerial scene classification. IEEE Trans. Geosci. Remote Sens. , 2017.

Xie et al. (2022) Xie, Z., Zhang, Z., Cao, Y., Lin, Y., Bao, J., Yao, Z., Dai, Q., and Hu, H. Simmim: A simple framework for masked image modeling. In CVPR , 2022.

Yu et al. (2025) Yu, S., Kwak, S., Jang, H., Jeong, J., Huang, J., Shin, J., and Xie, S. Representation alignment for generation: Training diffusion transformers is easier than you think. ICLR , 2025.

Zbontar et al. (2021) Zbontar, J., Jing, L., Misra, I., LeCun, Y., and Deny, S. Barlow twins: Self-supervised learning via redundancy reduction. In ICML , pp. 12310–12320. PMLR, 2021.

Zhou et al. (2017) Zhou, B., Zhao, H., Puig, X., Fidler, S., Barriuso, A., and Torralba, A. Scene parsing through ade20k dataset. In CVPR , 2017.

Zhou et al. (2021) Zhou, J., Wei, C., Wang, H., Shen, W., Xie, C., Yuille, A., and Kong, T. ibot: Image bert pre-training with online tokenizer. ICLR , 2021.

Zimmermann et al. (2025) Zimmermann, E., Wiltzer, H., Szeto, J., Alvarez-Melis, D., and Mackey, L. Kerjepa: Kernel discrepancies for euclidean self-supervised learning. arXiv preprint arXiv:2512.19605 , 2025.

## Appendix A Implementation details

### A.1 Training details

Pretraining on ImageNet-1K. We pretrain two model variants on ImageNet-1K ( Deng et al., 2009 ) (1.28M training images): VISReg-B (ViT-B/16, 86M parameters) and VISReg-L (ViT-L/14, 304M parameters). Both models are trained from scratch using the VISReg regularization objective and timm for backbones.

We adopt DINO-style multi-crop augmentation ( Caron et al., 2021 ) : each image produces N g = 4 N_{g}{=}4 global crops ( 224 × 224 224{\times}224 , scale [ 0.3 , 1.0 ] [0.3,1.0] ) and N l = 6 N_{l}{=}6 local crops ( 96 × 96 96{\times}96 for ViT-B, 98 × 98 98{\times}98 for ViT-L, scale [ 0.05 , 0.3 ] [0.05,0.3] ), yielding 10 views per image. Augmentations include random horizontal flip, color jitter ( p = 0.8 p{=}0.8 ), random grayscale ( p = 0.2 p{=}0.2 ), Gaussian blur ( p = 0.5 p{=}0.5 ), and random solarize ( p = 0.2 p{=}0.2 ).

We use AdamW with weight decay 5 × 10 − 2 5{\times}10^{-2} and bfloat16 mixed precision. The learning rate follows a linear warmup over 5 epochs then cosine annealing to lr max / 1000 \mathrm{lr}_{\max}/1000 . Projections are produced by a 3-layer MLP ( 2048 → 2048 → d p 2048\to 2048\to d_{p} ) with batch normalization and GELU activations, applied to the concatenated CLS tokens from the last two backbone layers.

VISReg-B uses learning rate 9 × 10 − 4 9{\times}10^{-4} , λ = 0.9 \lambda{=}0.9 , projection dimension d p = 256 d_{p}{=}256 , K = 2048 K{=}2048 random projections for VISReg, and per-GPU batch size 16 (effective batch size 512 across 32 GPUs). VISReg-L uses learning rate 8 × 10 − 4 8{\times}10^{-4} , λ = 0.7 \lambda{=}0.7 , d p = 384 d_{p}{=}384 , K = 4096 K{=}4096 random projections, and per-GPU batch size 16 (effective batch size 512 across 32 GPUs). Both models are trained for 400 epochs on 32 NVIDIA H100 80GB GPUs (4 nodes × \times 8 GPUs) using HuggingFace Accelerate for distributed training, requiring approximately 1,120 and 2,060 GPU-hours for ViT-B and ViT-L, respectively.

Pretraining on ImageNet-22K. We additionally pretrain VISReg on ImageNet-22K ( Deng et al., 2009 ) (14.2M images) with ViT-L/14 for 100 epochs on 16 NVIDIA H100 80GB GPUs (4 nodes × \times 4 GPUs). The multi-crop strategy uses N g = 2 N_{g}{=}2 global crops and N l = 8 N_{l}{=}8 local crops ( 98 × 98 98{\times}98 ), still yielding 10 views per image. We use per-GPU batch size 64 (effective batch size 1,024), learning rate 8 × 10 − 4 8{\times}10^{-4} , λ = 0.8 \lambda{=}0.8 , d p = 384 d_{p}{=}384 , and K = 4096 K{=}4096 random projections. All other settings (optimizer, scheduler, projector architecture) follow the ImageNet-1K configuration. Training requires approximately 2,720 GPU-hours.

### A.2 Testing details

Downstream classification. We evaluate pretrained representations on 8 classification benchmarks following the DINOv2 linear evaluation protocol ( Oquab et al., 2024 ) : DTD ( Cimpoi et al., 2014 ) , FGVC-Aircraft ( Maji et al., 2013 ) , Stanford Cars ( Krause et al., 2013 ) , CIFAR-10, CIFAR-100 ( Krizhevsky et al., 2009 ) , Oxford Flowers-102 ( Nilsback & Zisserman, 2008 ) , Food-101 ( Bossard et al., 2014 ) , and Oxford-IIIT Pets ( Parkhi et al., 2012 ) . We additionally evaluate on 6 out-of-distribution benchmarks: DTD, Galaxy10 ( Leung, 2025 ) , AID ( Xia et al., 2017 ) , NIH ChestX-ray ( Wang et al., 2017 ) , RetinaMNIST, and OrganAMNIST ( Bilic et al., 2023 ) . The details of each dataset can be found under A.3 .

For all classification tasks, we freeze the pretrained encoder and extract features by concatenating the CLS tokens from the last 4 transformer layers, yielding a feature vector of dimension 4 × d embed 4\times d_{\mathrm{embed}} (3,072 for ViT-B, 4,096 for ViT-L). A linear classifier with SyncBatchNorm is trained on top of these frozen features using SGD with momentum 0.9, no weight decay, and cosine annealing for 10 epochs with batch size 32. We perform a grid search over 13 base learning rates scaled by the linear scaling rule (effective batch size / 256), and report the best test accuracy. All images are resized to 224 × 224 224{\times}224 with standard ImageNet normalization.

ImageNet-1K linear probe. For ImageNet-1K linear evaluation, we follow the same frozen-feature protocol but with a dedicated multi-head implementation for efficiency. A multi-head linear classifier with shared SyncBatchNorm trains 10 independent heads in parallel (one per learning rate), for 100 epochs using SGD with momentum 0.9, no weight decay, and per-step cosine annealing. Training uses bfloat16 mixed precision on 8 GPUs with per-GPU batch size 32 (effective batch size 256). Standard ImageNet evaluation preprocessing is applied: random resized crop to 224 × 224 224{\times}224 for training, resize to 256 then center crop to 224 for validation. The best accuracy across all heads on the 50K validation set is reported.

Semantic segmentation. We evaluate on ADE20K ( Zhou et al., 2017 ) (150 classes) using a linear segmentation probe. A single 1 × 1 1{\times}1 convolution with SyncBatchNorm is trained on frozen patch features from the last transformer layer. Training uses AdamW with learning rate 2 × 10 − 3 2{\times}10^{-3} , polynomial LR decay (power 0.9), batch size 16, and image size 518 × 518 518{\times}518 (for patch-14 models) or 512 × 512 512{\times}512 (for patch-16 models) for 40 epochs. We report mean intersection-over-union (mIoU) on the validation set.

### A.3 Datasets

We evaluate our pre-trained models on a diverse set of 15 datasets spanning multiple domains, tasks, and difficulty levels. The following sections describe each dataset in detail.

ImageNet-1k ( Deng et al., 2009 ) is a large-scale object recognition dataset containing 1,281,167 training images and 50,000 validation images across 1,000 classes, representing diverse natural objects, animals, and scenes from the natural world.

CIFAR-10 ( Krizhevsky et al., 2009 ) is a 10-class object classification dataset with 50,000 training and 10,000 test images at 32 × 32 32\times 32 resolution, covering categories like airplanes, cars, birds, cats, and other common objects.

CIFAR-100 ( Krizhevsky et al., 2009 ) is a fine-grained object classification dataset with 50,000 training and 10,000 test images at 32 × 32 32\times 32 resolution, containing 100 classes organized into 20 supercategories including various vehicles, animals, and household items.

Stanford Cars ( Krause et al., 2013 ) is a fine-grained vehicle classification dataset with 8,144 training and 8,041 test images covering 196 car models from 98 manufacturers, spanning decades of automotive design from 1950 to 2012.

Galaxy10 ( Leung, 2025 ) is an astronomical image classification dataset with 17,736 images classifying galaxies into 10 morphological categories (disturbed, merging, spiral, elliptical, etc.) from the DECaLS survey.

Food-101 ( Bossard et al., 2014 ) is a food classification dataset with 75,750 training and 25,250 validation images covering 101 food categories including dishes like pizza, sushi, hamburger, and various international cuisines.

Oxford-IIIT Pets ( Parkhi et al., 2012 ) is a pet breed classification dataset with 3,680 training and 3,669 test images covering 37 cat and dog breeds, requiring fine-grained distinction between similar-looking breeds.

NIH Chest X-ray ( Wang et al., 2017 ) is a multi-label medical image classification dataset comprising 112,120 total images, where each chest radiograph may contain multiple pathology labels from 14 disease categories including pneumonia, cardiomegaly, and pleural effusion.

RetinaMNIST ( Liu et al., 2022 ) is a medical image classification dataset with 1,080 training, 120 validation, and 400 test retinal fundus images classifying diabetic retinopathy into 5 severity grades.

OrganAMNIST ( Bilic et al., 2023 ) is a medical image classification dataset with 34,581 training, 6,491 validation, and 17,778 test CT axial slices classifying 11 body organ types including liver, kidney, spleen, and heart.

Oxford Flowers 102 ( Nilsback & Zisserman, 2008 ) is a fine-grained plant classification dataset with 1,020 training, 1,020 validation, and 6,149 test images covering 102 flower species with 40-258 images per class.

Describable Textures (DTD) ( Cimpoi et al., 2014 ) is a texture classification dataset with 1,880 training, 1,880 validation, and 1,880 test images across 47 texture categories (e.g., braided, dotted, fibrous) following a 10-fold cross-validation protocol.

FGVC-Aircraft ( Maji et al., 2013 ) is a fine-grained aircraft classification dataset with 6,667 trainval and 3,333 test images covering 100 aircraft variants from the FGVC-Aircraft 2013b benchmark.

AID ( Xia et al., 2017 ) is a remote sensing scene classification dataset with 10,000 images across 30 aerial scene categories including airports, beaches, forests, and urban areas, using a 10%/90% train/test split for SSL evaluation.

ADE20K ( Zhou et al., 2017 ) is a semantic segmentation dataset with 20,210 training and 2,000 validation images, containing pixel-level annotations for 150 semantic classes including objects, parts, and materials across indoor and outdoor scenes.

## Appendix B Additional ablations

Our additional ablations focus on VISReg design, including the necessity of scale, shape, center loss, the necessity of applying gradient detachment between scale and shape loss, and the effect of the loss weight on each component. We include a long-tailed dataset (ImageNet-LT), a low-rank dataset (Galaxy10), and a normal dataset (Imagenette) to cover a wider range of application scenarios. All experiments use a ViT-S/8 backbone at 128 × 128 128{\times}128 resolution with 4 augmented views, learning rate 10 − 3 10^{-3} , per-GPU batch size 32 across 8 GPUs (effective batch 256), λ = 0.6 \lambda=0.6 , projection dimension 256, and K = 4096 K{=}4096 random projections. ImageNet-LT and Galaxy10 train for 400 epochs; Imagenette for 800.

### B.1 Effect of decoupled components in training.

First, we knocked out each contribution of scale, shape, and center in the training to understand the effectiveness of each part. Since the result on ImageNette has shown a clear pattern, ImageNet-LT and Galaxy are not included. Table 11 shows that both scale and shape loss significantly impact the learning process: 1) Without scale loss, there is a 71.02% decrease in accuracy; Without shape loss, there is a 58.4% decrease in accuracy. As for the center loss, the accuracy difference is 0.41% in the final accuracy, but importantly, it increases the convergence speed. Hence, all three components are necessary.

Second, we check the usefulness of applying detachment between scale loss and shape loss. The general observation from Table 11 is that, despite the minor improvement, detachment helps the model achieve a higher performance across all three datasets. Therefore, we choose to use it across all the experiments.

### B.2 Effect of decoupled components in different training set scenarios.

We ablate the ratio between the three DSSO loss components, i.e. , scale, shape, and center, while keeping the total weight constant ( λ scale + λ shape + λ center = 3 \lambda_{\text{scale}}+\lambda_{\text{shape}}+\lambda_{\text{center}}=3 ) so that λ \lambda alone controls the overall regularization magnitude.

The shape component is the most impactful of the three DSSO objectives. On ImageNet-LT and Galaxy10, shifting weight toward shape monotonically improves accuracy, with shape 4:1 outperforming the equal baseline by +3.2% and +1.3%, respectively. Conversely, emphasizing scale or center consistently degrades performance, with scale 4:1 producing the largest drops (-4.6% on ImageNet-LT, -2.7% on Galaxy10). This suggests that a higher shape regularization helps the learning on low-quality datasets. However, the result on Imagenette shows that the default setting is the best choice. Other imbalanced ratio across three factors largely reduces the learning effectiveness.

## Appendix C Visualizations

### C.1 VISReg loss indicates the performance

Strong correlation between loss and online probe accuracy is a important advantage of the theorem proposed by LeJEPA ( Balestriero & LeCun, 2025 ) . We calculate the Pearson correlation between loss and online probe accuracy of the ViT-L training on ImageNet1K, as shown in Figure 7 . The pronounced -0.996 correlation show the loss curve can be used to reflect the learning curve of the model.

### C.2 Further comparison with DINOv1 on image and video.

#### PCA Feature Visualization.

To qualitatively compare the learned representations, we visualize patch-level features from different ViT encoders using PCA coloring. For each input image, we extract the spatial patch token features from the last layer of the encoder, yielding a feature map of shape H p × W p × C H_{p}\times W_{p}\times C , where H p H_{p} and W p W_{p} are the patch grid dimensions and C C is the embedding dimension. We flatten this to an N × C N\times C matrix ( N = H p × W p N=H_{p}\times W_{p} ) and apply PCA to reduce it to three components, which are then interpreted as RGB channels. Each component is independently normalized to [ 0 , 1 ] [0,1] via min–max scaling, and the resulting H p × W p × 3 H_{p}\times W_{p}\times 3 map is bilinearly upsampled to the original image resolution for display. Since PCA components are determined only up to permutation and sign, direct comparison between models requires alignment. We compute the 3 × 3 3\times 3 Pearson correlation matrix between the PCA components of a reference model ( i.e. , DINO ViT-B/16 ( Caron et al., 2021 ) ) and the target model ( i.e. , VISReg ViT-B/16), then solve the optimal assignment using the Hungarian algorithm on − | corr | -\lvert\mathrm{corr}\rvert . The matched target components are reordered accordingly and flipped in sign where the correlation is negative, ensuring consistent color semantics across models. For video visualizations, PCA is fit jointly on the patch features from all frames to ensure temporal consistency of the color mapping. Both Figure 9 and Figure 8 indicates that VISReg helps model learn more granular details than DINO.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
