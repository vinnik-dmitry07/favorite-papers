##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Manifold Steering Reveals the Shared Geometry of Neural Network Representation and Behavior

###### Abstract

Neural representations carry rich geometric structure; but does that structure causally shape behavior? To address this question, we intervene along paths through activation space defined by different geometries, and measure the behavioral trajectories they induce. In particular, we test whether interventions that respect the geometry of activation space will yield behaviors close to those the model exhibits naturally. Concretely, we first fit an activation manifold ℳ h \mathcal{M}_{h} to representations and a behavior manifold ℳ y \mathcal{M}_{y} to output probability distributions. We then test the link ℳ h ↔ ℳ y \mathcal{M}_{h}\leftrightarrow\mathcal{M}_{y} via interventions: we find that steering along ℳ h \mathcal{M}_{h} , which we term manifold steering , yields behavioral trajectories that follow ℳ y \mathcal{M}_{y} , while linear steering—which assumes a Euclidean geometry—cuts through off-manifold regions and hence produces unnatural outputs. Moreover, optimizing interventions in activation space to produce paths along ℳ y \mathcal{M}_{y} recovers activation trajectories that trace the curvature of ℳ h \mathcal{M}_{h} . We demonstrate this bidirectional relationship between the geometry of representation and behavior across tasks and modalities. In language models, we use reasoning tasks with cyclic and sequential geometries as well as in-context learning tasks with more complex graph geometries. In a video world model, we use a task with geometry corresponding to physical dynamics. Overall, our work shows that geometry in neural representation is not merely incidental, but is in fact the proper object for enabling principled control via intervention on internals. This recasts the core problem of steering from finding the right direction to finding the right geometry .

## 1 Introduction

A plethora of geometric structures have been documented in neural network representations ( Modell et al., 2025b ; Park et al., 2025b ; Kozlowski et al., 2025 ; Shai et al., 2024b ; Pearce et al., 2025 ; Gurnee et al., 2026 ) . Recent literature has begun to identify the origins of these structures by attributing them back to data statistics shaped by conceptual structure ( Karkada et al., 2026 ; Prieto et al., 2026 ; Park et al., 2025b ; Merullo et al., 2025 ) . However, we have barely begun to understand what causal role these geometric structures play in a model’s computation (cf. Engels et al. 2024 ; Kantamneni and Tegmark 2025 ; Csordás et al. 2024 ; Sarfati et al. 2026 ). We address this question by intervening on model activations under different geometric assumptions and measuring the effect on behavior.

Currently, it is common for activation-based intervention methods to assume a Euclidean geometry for activation space, where steering is performed by adding a steering vector to model activations with a scalar that modulates intervention strength ( Bau et al., 2019 ; Subramani et al., 2022 ; Marks and Tegmark, 2024 ; Panickssery et al., 2024 ; Turner et al., 2024 ; Li et al., 2023 ; Rimsky et al., 2024 ; Chen et al., 2025 ) . This approach is motivated by the linear representation hypothesis (LRH), which posits that neural activations can be decomposed into atomic concepts encoded along single (approximately) orthogonal directions ( Smolensky, 1986 ; Park et al., 2023 ; Elhage et al., 2022b ) . However, linear steering often produces degraded fluency, diversity collapse, and unstable off-target behavior ( Wu et al., 2025 ; Da Silva et al., 2025 ; Bigelow et al., 2025 ; Tan et al., 2024 ; Hao et al., 2025 ; Bhalla et al., 2024 ; Pres et al., 2024 ) , which suggests the assumed Euclidean geometry is inappropriate.

In this work, we advance the hypothesis that representation geometry provides a blueprint for effective steering that will overcome the limitations of the linear approach. Steering is fundamentally about how internal representations control behavior, so to test this hypothesis we must study not only paths through activation space, but also the behavioral trajectories induced by interventions along these paths. Successful steering will produce trajectories that are in line with the model’s natural (unintervened) output distribution. If we are right, then interventions that respect the geometry of internal representations and interventions that respect the geometry of behavior will be one and the same. Motivated by this, we make the following contributions in this work.

• Uncovering isometric geometries in neural network representation and behavior. We use tasks where models output a distribution over a set of concepts with known structure. In each task, we fit an activation manifold ℳ h \mathcal{M}_{h} to internal representations and a behavior manifold ℳ y \mathcal{M}_{y} to model outputs (probability distributions over task-relevant concepts). We show the two geometries are tightly interlinked via a scaled isometry relation: geodesic distances on ℳ h \mathcal{M}_{h} align closely with those on ℳ y \mathcal{M}_{y} , and neither match Euclidean distances.

• Validating the causal role of representation geometry. We perform geometry-aware steering experiments and compare against the baseline of linear steering (see Fig. 1 ). We show linear steering cuts through low-density regions of behavior space and passes through unnatural intermediate distributions; meanwhile, steering along the activation manifold ℳ h \mathcal{M}_{h} yields behavioral trajectories that follow ℳ y \mathcal{M}_{y} closely. In fact, optimizing for paths along ℳ y \mathcal{M}_{y} recovers activation trajectories that trace the curvature of ℳ h \mathcal{M}_{h} , further tightening the link between activation geometry and behavior.

• A theoretical framework for geometry-aware steering. Building on the results above, we formulate steering as a problem of choosing the right geometry for activation space, rather than the right direction . In particular, we argue steering can be defined as the problem of finding a geodesic connecting two points under different activation-space metrics: linear steering assumes a flat metric (Euclidean geometry), steering along the activation manifold uses a metric derived from natural activations, and steering optimized to follow the behavior manifold uses a metric derived from natural behaviors.

We demonstrate these findings hold across modalities and tasks. In large language models, we test geometries from cyclic concepts (weekdays, months; Engels et al. 2024 ; Modell et al. 2025b ), sequential concepts (ages, letters), and multi-dimensional graph structures learned in context ( Park et al., 2025b ) . In a video world model, we test a geometry of physical position in a simulated environment (mountain car; Moore 1990 ; Towers et al. 2024 ). Together, these findings provide evidence for the posited account, and support steering along neural manifolds as the principled form of activation-based intervention.

## 2 The Geometry of Representation and Behavior

### 2.1 Setup

#### Running example.

We will explicate our framework and empirical methods using a running example where a language model is required to reason about the days of the week ( Engels et al., 2024 ) . Specifically, we consider prompts of the form: What day is k k days after z z ? with z ∈ 𝒵 = { Mon , Tue , … , Sun } z\in\mathcal{Z}=\{\mathrm{Mon},\mathrm{Tue},\ldots,\mathrm{Sun}\} and k ∈ { 1 , … , 7 } k\in\{1,\dots,7\} . Given such a prompt, the LM outputs a probability distribution over all possible tokens.

#### Concept geometry.

We draw inspiration from work on conceptual spaces in cognitive science, where conceptual domains, e.g., days of the week, are geometrically enriched with a metric such that distances between points encode similarity and guide patterns of inference ( Shepard 1987 ; Gärdenfors 2000 ; Tenenbaum and Griffiths 2001 ; Bellmund et al. 2018 ; see Fel et al. 2025b ; Lubana et al. 2025 ; Yocum et al. 2025 ; Modell et al. 2025b for related work in interpretability). For example, the days of the week 𝒵 \mathcal{Z} may be organized in a cyclic structure that is captured by a metric d 𝒵 d_{\mathcal{Z}} measuring temporal distance between days, e.g., neighboring days are closer together. Indeed, when humans mistakenly report the current day, they most often confuse it with its neighboring days ( Ellis et al., 2015 ) .

Karkada et al. (2026) and Prieto et al. (2026) show that similarity structure between days of the week is reflected in the statistics of training data, which in turn shape the geometry of internal representations ( Engels et al., 2024 ; Park et al., 2025a ; Modell et al., 2025a ; Prieto et al., 2026 ) . We hypothesize that a model’s output distributions over 𝒵 \mathcal{Z} are similarly shaped by d 𝒵 d_{\mathcal{Z}} : e.g., when asked What day is four days after Monday? , the model concentrates mass on Friday and spreads the remainder onto nearby days like Thursday and Saturday.

#### Notation.

We work with two spaces: the activation space 𝒜 = ℝ n \mathcal{A}=\mathbb{R}^{n} , and the behavior space 𝒴 = Δ | 𝒵 | \mathcal{Y}=\Delta^{|\mathcal{Z}|} , which is the open probability simplex 1 1 1 We require the open simplex { 𝒑 ∈ ℝ > 0 | 𝒵 | : ∑ i p i = 1 } \{\bm{p}\in\mathbb{R}^{|\mathcal{Z}|}_{>0}:\sum_{i}p_{i}=1\} , i.e., strictly positive entries. The closed simplex, which includes faces where some p i = 0 p_{i}=0 , has boundary and corners and is not a smooth manifold. over the conceptual domain 𝒵 \mathcal{Z} , with an additional ‘other’ class for off-concept probability mass. For an input x x , let 𝒑 ⁡ ( x ) ∈ 𝒴 \bm{p}(x)\in\mathcal{Y} denote the model’s output distribution over 𝒵 \mathcal{Z} , given by restricting the full vocabulary distribution of the model to the tokens in 𝒵 \mathcal{Z} , in addition to the ‘other’ class for remaining probability mass. Let 𝒉 ⁡ ( x ) ∈ 𝒜 \bm{h}(x)\in\mathcal{A} denote an activation vector of interest for input x x .

For a class of input queries that share the same answer, e.g., What is two days after Monday? and What is three days after Sunday? , we average the hidden activations and output distributions to produce “activation centroids” and “behavior centroids”, respectively.

#### Experimental tasks.

We perform language model experiments on four tasks, two with cyclic conceptual structure and two with sequential conceptual structure. The cyclic tasks require reasoning about days of the week and months of the year, e.g., What is four months after January? . The sequential tasks require reasoning about letters and ages, e.g., What is four letters after m? or Alice is 7, Bob is 5 years older. How old is Bob? .

### 2.2 Fitting the Manifolds

We fit a smooth manifold within each space to the model’s unintervened activations or outputs for a task: ℳ h ⊆ 𝒜 \mathcal{M}_{h}\subseteq\mathcal{A} , the activation manifold , and ℳ y ⊆ 𝒴 \mathcal{M}_{y}\subseteq\mathcal{Y} , the behavior manifold . To fit the activation manifold ℳ h \mathcal{M}_{h} , we reduce activation vectors 𝒉 ⁡ ( x ) \bm{h}(x) to 64 dimensions via PCA, compute “concept centroids” (e.g., averaging all activations where the correct answer is Wednesday), and fit cubic splines ( Reinsch, 1967 ) through the centroids (see App. A.3 for further spline fitting details). To fit the behavior manifold ℳ y \mathcal{M}_{y} , we follow a similar procedure but first map each centroid from the probability simplex onto Hellinger space via p ↦ p p\mapsto\sqrt{p} . This linearizes the geometry of the simplex: the Hellinger distance between distributions becomes an ordinary Euclidean distance, d H ​ ( p , q ) = 1 2 ​ ‖ p − q ‖ d_{H}(p,q)=\tfrac{1}{\sqrt{2}}\|\sqrt{p}-\sqrt{q}\| , so we can fit splines and compare distributions with standard Euclidean tools while still respecting the underlying probabilistic geometry ( Amari and Nagaoka, 2000 ) . Decoded points are squared back to recover valid distributions (further details, including how we keep the fit on the sphere, are in App. A.4 ). Unless stated otherwise, we use Llama 3.1 8B ( Touvron et al., 2023 ) with activations from layer 28, and visualize manifolds via 3 3 D PCA.

### 2.3 Conceptual Structure Appears in Behavior and Activation Space

We will now begin our investigation into the connection between the activation and behavior manifolds. Before we perform any interventions on internal representations, we examine the structural correspondence between these spaces, and measure whether distances along the two manifolds are proportional (a scaled isometry).

We find that both the activation and behavior manifolds recapitulate conceptual structure (see Figs. 2 , 3 for visualizations). For example, in the case of days of the week, the activations and output distributions are arranged in order around a loop, with Monday adjacent to Tuesday and Sunday, and Thursday on the opposite side (Fig. 2 ). The circle representing days of the week in activation space is already known to exist ( Engels et al., 2024 ; Modell et al., 2025b ; Karkada et al., 2026 ) . However, the circle in behavior space is a novel discovery, and results from sharply-peaked output distributions placing most mass on the target concept, with the remainder concentrated on its neighbors. The correspondence is striking; output distributions and internal activations recover the same cyclic ordering. In contrast, the conceptual structure for the ages and letters task is sequential rather than cyclic, and so both the activations and output distributions for these tasks lie on an open curve (Fig. 3 ).

Going beyond qualitative structural correspondence, we wish to examine the mapping between distances along each manifold. We test this by computing pairwise distances between points in both spaces: geodesic distances d ℳ h ​ ( m i , m j ) d_{\mathcal{M}_{h}}(m_{i},m_{j}) on the activation manifold, and geodesic distances d ℳ y ​ ( p i , p j ) d_{\mathcal{M}_{y}}(p_{i},p_{j}) on the behavior manifold. We compute geodesic distance on ℳ h \mathcal{M}_{h} using cumulative Euclidean distance between points along a geodesic path, and follow the same procedure for geodesic distance on ℳ y \mathcal{M}_{y} , but using cumulative Hellinger distance (see App. A.5 for further details). The two distances are highly correlated ( r = 0.99 r=0.99 weekdays, r = 0.89 r=0.89 months, r = .999 r=.999 letters, r = .999 r=.999 ages) indicating that ℳ h \mathcal{M}_{h} and ℳ y \mathcal{M}_{y} are approximately isometric. Meanwhile, linear paths between the same activation-space points correlate less well with ℳ y \mathcal{M}_{y} geodesics, with the relationship showing clear non-linear patterns ( r = 0.89 r=0.89 weekdays, r = 0.53 r=0.53 months, r = 0.71 r=0.71 letters, r = 0.36 r=0.36 ages).

This correspondence leads to an intuitive hypothesis. ℳ y \mathcal{M}_{y} was fit to unintervened task behavior, so it traces a path through natural output distributions for the model. If the ℳ h ↔ ℳ y \mathcal{M}_{h}\leftrightarrow\mathcal{M}_{y} mapping holds, paths along one manifold should track paths along the other. Interventions in activation space that follow ℳ h \mathcal{M}_{h} should produce natural trajectories along ℳ y \mathcal{M}_{y} . Conversely, activation-space paths that are optimized to produce trajectories on ℳ y \mathcal{M}_{y} should recover ℳ h \mathcal{M}_{h} . Next, we test both directions via intervention: representation to behavior ( ℳ h → ℳ y \mathcal{M}_{h}\rightarrow\mathcal{M}_{y} ) and behavior to representation ( ℳ h ← ℳ y \mathcal{M}_{h}\leftarrow\mathcal{M}_{y} ).

## 3 Connecting Representation and Behavior via Intervention

Now that we have established a correlational correspondence between the activation and behavior manifolds across four tasks, we turn to steering interventions for causal evidence. First, we steer along ℳ h \mathcal{M}_{h} and measure whether output trajectories follow ℳ y \mathcal{M}_{y} (§ 3.2 ). Second, we optimize interventions on internal representations to produce output distributions that follow ℳ y \mathcal{M}_{y} and measure whether the optimized activation trajectory follows ℳ h \mathcal{M}_{h} (§ 3.3 ).

### 3.1 Steering Intervention Notation

The basic intervention operation entails replacing the model’s activation at a chosen layer with a target activation, and continuing the forward pass. Given a base input x x and a target 𝒉 ⋆ ∈ 𝒜 \bm{h}^{\star}\in\mathcal{A} , we write 𝒑 𝒉 ← 𝒉 ⋆ ​ ( x ) \bm{p}_{\bm{h}\leftarrow\bm{h}^{\star}}(x) for the resulting output distribution. A steering path is a curve 𝝅 : [ 0 , 1 ] → 𝒜 \bm{\pi}:[0,1]\to\mathcal{A} between endpoints 𝒉 0 ⋆ \bm{h}^{\star}_{0} and 𝒉 1 ⋆ \bm{h}^{\star}_{1} , inducing a trajectory 𝒑 𝒉 ← 𝝅 ⁡ ( t ) ​ ( x ) \bm{p}_{\bm{h}\leftarrow\bm{\pi}(t)}(x) through behavior space 𝒴 \mathcal{Y} . The behavioral trajectory will be non-stationary only if the target 𝐡 \mathbf{h} mediates the causal effect from input to output ( Pearl, 2001 ; Vig et al., 2020 ; Mueller et al., 2024 ) .

We consider two strategies, both constructed by interpolation between the endpoints; the strategies differ only in the coordinate system in which the interpolation is taken (Fig. 1 ): 𝝅 lin ​ ( t ) \displaystyle\bm{\pi}_{\mathrm{lin}}(t) = ( 1 − t ) ​ 𝒉 0 ⋆ + t ​ 𝒉 1 ⋆ \displaystyle=(1{-}t)\,\bm{h}^{\star}_{0}+t\,\bm{h}^{\star}_{1} (linear steering); (1) 𝝅 m ​ ( t ) \displaystyle\bm{\pi}_{\mathrm{m}}(t) = 𝒔 ⁡ ( ( 1 − t ) ​ 𝒖 0 + t ​ 𝒖 1 ) , 𝒖 i = 𝒔 − 1 ​ ( 𝒉 i ⋆ ) \displaystyle=\bm{s}\bigl((1{-}t)\,\bm{u}_{0}+t\,\bm{u}_{1}\bigr),\quad\bm{u}_{i}=\bm{s}^{-1}(\bm{h}^{\star}_{i}) (manifold steering). (2) In the above, 𝒔 : ℝ k → 𝒜 \bm{s}:\mathbb{R}^{k}\to\mathcal{A} is a parameterization of ℳ h \mathcal{M}_{h} —the map sending k k -dimensional intrinsic coordinates to the corresponding point on the manifold in the activation space 𝒜 \mathcal{A} . Linear steering (also known as ‘diff-in-means steering’) ( Bau et al., 2018 ; Subramani et al., 2022 ; Turner et al., 2023 ) interpolates in 𝒜 \mathcal{A} directly—the standard additive-vector baseline. Manifold steering interpolates in the intrinsic coordinates of ℳ h \mathcal{M}_{h} and maps the result back through 𝒔 \bm{s} , so 𝝅 m \bm{\pi}_{\mathrm{m}} stays on the activation manifold ℳ h \mathcal{M}_{h} throughout. Each strategy thus corresponds to a different choice of geometry on activation space, which we concretize in § 3.4 .

### 3.2 Steering Along the Activation Manifold Follows the Behavior Manifold

For every pair of start and end values, e.g., from Tuesday to Friday, we steer from the start centroid to the end centroid in activation space using manifold and linear steering with K = 50 K=50 intervention points along each path. We report the average trajectory in behavior space over a set of 16 prompts sampled randomly from the task’s input distribution (Fig. 4 , see App. A.6 for further experimental details). We find that manifold steering produces smooth and ordered behavioral transitions: probability mass shifts steadily through adjacent values of a concept—from Monday to Tuesday to Wednesday to Thursday—while linear steering instead exhibits ‘teleportation’ : mass jumps between non-adjacent concepts as the straight line cuts through the manifold’s interior.

This qualitative evidence is encouraging, but we have yet to examine our key hypothesis that interventions along the activation manifold ℳ h \mathcal{M}_{h} produce natural output trajectories that follow ℳ y \mathcal{M}_{y} . This would mean that outputs produced under manifold steering resemble those produced without intervention. We quantify this via an “energy function”, as described next, under which a natural trajectory is one of low cumulative energy as defined by ℳ y \mathcal{M}_{y} .

#### An Energy-based View of Naturalness.

Energy functions have a long history in machine learning as a way to measure plausibility under a model ( Hopfield, 1982 ; LeCun et al., 2006 ) . These functions assign low values for likely states and high values for unlikely ones, with the standard correspondence E ⁡ ( 𝒙 ) ∝ − log ⁡ p ⁡ ( 𝒙 ) E(\bm{x})\propto-\log p(\bm{x}) giving energy the interpretation of an unnormalized log-density ( Hopfield, 1982 ; LeCun et al., 2006 ; Grathwohl et al., 2019 ; Song and Kingma, 2021 ; Béthune et al., 2025 ) . We adopt the same view here. The model’s output distributions on unintervened forward passes trace out a low-energy region of behavior space (approximately captured by the manifold ℳ y \mathcal{M}_{y} ) and a steering trajectory is natural to the extent it stays within that region. Concretely, given a steering path 𝝅 : [ 0 , 1 ] → 𝒜 \bm{\pi}:[0,1]\to\mathcal{A} , let 𝜸 ​ ( t ) = 𝒑 𝒉 ← 𝝅 ⁡ ( t ) ​ ( 𝒙 ) \bm{\gamma}(t)=\bm{p}_{\bm{h}\leftarrow\bm{\pi}(t)}(\bm{x}) be the behavioral trajectory it induces. We define its cumulative output energy: E BC ​ ( 𝜸 ) = ∫ 0 1 d BC ​ ( 𝜸 ⁡ ( t ) , ℳ y ) ​ 𝑑 t , E_{\text{BC}}(\bm{\gamma})\;=\;\int_{0}^{1}d_{\text{BC}}\!\bigl(\bm{\gamma}(t),\,\mathcal{M}_{y}\bigr)\,dt, (3) where d BC ​ ( 𝒑 , ℳ y ) = inf 𝒒 ∈ ℳ y d BC ​ ( 𝒑 , 𝒒 ) = − log ⁡ ( ∑ i 𝒑 i ​ 𝒒 i ) d_{\text{BC}}(\bm{p},\mathcal{M}_{y})=\inf_{\sqrt{\bm{q}}\in\mathcal{M}_{y}}d_{\text{BC}}(\bm{p},\bm{q})=-\log(\sum_{i}\sqrt{\bm{p}_{i}}\sqrt{\bm{q}_{i}}) is the Bhattacharyya distance to the nearest point on ℳ y \mathcal{M}_{y} , a natural choice given that it is simply the negative log of the dot product in Hellinger space (in which ℳ y \mathcal{M}_{y} is fit). We note that the formulation above is a tractable proxy we use to estimate distance from the model’s natural output distribution, yet it is but one instantiation of a more general framework we develop in § 3.4 . Applying this measure, we find that manifold steering (weekdays E BC = 0.34 ± 0.03 E_{\text{BC}}=0.34\pm 0.03 ; months E BC = 0.36 ± 0.01 E_{\text{BC}}=0.36\pm 0.01 ; letters 2.42 ± 0.07 2.42\pm 0.07 ; ages E BC = 5.21 ± 0.09 E_{\text{BC}}=5.21\pm 0.09 ) produces significantly more natural paths, i.e., lower cumulative energy, than linear steering (weekdays E BC = 0.93 ± 0.11 E_{\text{BC}}=0.93\pm 0.11 ; months E BC = 1.09 ± 0.06 E_{\text{BC}}=1.09\pm 0.06 ; letters 6.95 ± 0.27 6.95\pm 0.27 ; ages E BC = 13.49 ± 0.29 E_{\text{BC}}=13.49\pm 0.29 ); on average, we see an improvement of a factor of 2.8 × 2.8\times , with all statistical comparisons yielding p < 0.001 p<0.001 .

We find further verification of the claim above by visualizing output trajectories in behavior space (Fig. 4 ). Manifold steering consistently traces paths close to ℳ y \mathcal{M}_{y} , while linear steering cuts through regions far from the behavior manifold, yielding less natural outputs. This result provides causal support for the correspondence between activation and output geometry, and establishes manifold steering as a principled form of steering that yields natural behavioral trajectories ( ℳ h → ℳ y \mathcal{M}_{h}\rightarrow\mathcal{M}_{y} ). Next, we explore whether we can find evidence from the opposite direction ( ℳ y → ℳ h \mathcal{M}_{y}\rightarrow\mathcal{M}_{h} ).

### 3.3 Behavior Space Geometry Recovers the Activation Manifold

In this section, we aim to uncover whether steering intervention paths optimized to follow the behavior manifold ℳ y \mathcal{M}_{y} recover the activation manifold ℳ h \mathcal{M}_{h} . To do so, we first take a path π y ∗ \pi_{y}^{*} along ℳ y \mathcal{M}_{y} in behavior space. We work within the layer and the first 32 dimensions of the subspace in which we fit the activation manifold ( 64 64 dimensional PCA), and optimize via L-BFGS for a path in activation space which, upon intervention, induces the behavioral path π y ∗ \pi_{y}^{*} (see App. A.8 for further details regarding the optimization procedure). We call the resulting path in activation space the pullback .

To quantify how faithfully a pullback path in activation space π h pullback \pi_{h}^{\text{pullback}} recapitulates the manifold steering path π h ∗ \pi_{h}^{*} , we report an intrinsic R 2 R^{2} . Both paths are projected into a common subspace given by the singular directions explaining 99 % 99\% of the variance in π h ∗ \pi_{h}^{*} , restricting the comparison to directions where the path actually extends. We then compute the R 2 R^{2} in this subspace, defining the residual at each point of π h pullback \pi_{h}^{\text{pullback}} as its orthogonal closest-point distance to π h ∗ \pi_{h}^{*} . We compute this score for each optimized pullback path π h pullback \pi_{h}^{\text{pullback}} and compare with a linear path baseline (see App. A.9 for more details).

Results are shown in Fig. 5 . We find that the pullback activation paths follow the activation manifold ℳ h \mathcal{M}_{h} more closely than the linear steering path, and resemble the shape of the manifold steering paths of § 3.2 (weekdays R pullback 2 = 0.77 ± 0.03 R^{2}_{\text{pullback}}=0.77\pm 0.03 vs. R linear 2 = 0.42 ± 0.07 R^{2}_{\text{linear}}=0.42\pm 0.07 ; months R pullback 2 = 0.75 ± 0.04 R^{2}_{\text{pullback}}=0.75\pm 0.04 vs. R linear 2 = 0.32 ± 0.05 R^{2}_{\text{linear}}=0.32\pm 0.05 ; ages R pullback 2 = 0.47 ± 0.05 R^{2}_{\text{pullback}}=0.47\pm 0.05 vs. R linear 2 = 0.24 ± 0.01 R^{2}_{\text{linear}}=0.24\pm 0.01 ; letters R pullback 2 = 0.78 ± 0.04 R^{2}_{\text{pullback}}=0.78\pm 0.04 vs. R linear 2 = 0.23 ± 0.03 R^{2}_{\text{linear}}=0.23\pm 0.03 . All statistical comparisons yield p < 0.001 p<0.001 ). Again we see a striking correspondence between representation and behavior; despite being derived from different sources—manifold steering from the density of activations and pullback from the structure of outputs—the two geometries are tightly connected.

Taken together, these results, alongside those of § 3.2 , provide bidirectional support for the connection between activation geometry and behavior. This convergence indicates that ℳ h \mathcal{M}_{h} is a core object in the model’s representation: the geometry of activation space and the geometry of behavior are alternate views of the same underlying conceptual organization.

### 3.4 Unifying Steering Strategies Through Geometry

In the sections above, we analyzed three methods for steering between two points in activation space that each assume a different geometry: linear steering, which assumes a flat Euclidean geometry; manifold steering, which derives a geometry from naturally occurring activations; and pullback steering, which derives a geometry from naturally occurring output distributions. We provided empirical support for our hypothesis that the geometries derived from internal activations and output behaviors are much more similar to each other than the standard Euclidean geometry. We now formalize the question of how to steer as how to choose the right geometry for activation space .

#### The Geometry of Steering:

Consider a Riemannian metric 𝑮 \bm{G} , which assigns an inner product at each point of 𝒜 \mathcal{A} ; together with a path 𝝅 : [ 0 , 1 ] → 𝒜 \bm{\pi}:[0,1]\to\mathcal{A} , this defines the notion of path length as follows. L 𝑮 ​ ( 𝝅 ) = ∫ 0 1 𝝅 ˙ ​ ( t ) ⊤ ​ 𝑮 ​ ( 𝝅 ⁡ ( t ) ) ​ 𝝅 ˙ ​ ( t ) ​ 𝑑 t . L_{\bm{G}}(\bm{\pi})\;=\;\int_{0}^{1}\sqrt{\dot{\bm{\pi}}(t)^{\top}\,\bm{G}(\bm{\pi}(t))\,\dot{\bm{\pi}}(t)}\,dt. (4) Then, a geodesic is defined as the path of minimum length between two endpoints, and each choice of geometry picks out a steering strategy. The strategies of linear steering and manifold steering (§ 3.2 ), written as interpolations in two different coordinate systems (Eqs. 1 , 2 ), are two such choices; the pullback procedure of § 3.3 is a third. Now, we make all three geometries explicit.

###### Definition 1 (Geometries of Steering) .

Let E : 𝒜 → ℝ E:\mathcal{A}\to\mathbb{R} be an energy function such that E ⁡ ( 𝐡 ) ∝ − log ⁡ p ⁡ ( 𝐡 ) E(\bm{h})\propto-\log p(\bm{h}) , and let 𝐠 y \bm{g}_{y} be a chosen Riemannian metric on ℳ y \mathcal{M}_{y} . We define: 𝑮 I \displaystyle\bm{G}_{I} = 𝑰 n , \displaystyle=\bm{I}_{n}, (linear steering) (5) 𝑮 E ​ ( 𝒉 ) \displaystyle\bm{G}_{E}(\bm{h}) = ( α ​ e − E ⁡ ( 𝒉 ) + β ) − 1 ​ 𝑰 n , \displaystyle=\bigl(\alpha\,e^{-E(\bm{h})}+\beta\bigr)^{-1}\bm{I}_{n}, (manifold steering) (6) 𝑮 F ​ ( 𝒉 ) \displaystyle\bm{G}_{F}(\bm{h}) = 𝑱 𝑭 ​ ( 𝒉 ) ⊤ ​ 𝒈 y ​ ( 𝑭 ⁡ ( 𝒉 ) ) ​ 𝑱 𝑭 ​ ( 𝒉 ) + ϵ ​ 𝑰 n , \displaystyle=\bm{J}_{\bm{F}}(\bm{h})^{\top}\,\bm{g}_{y}\bigl(\bm{F}(\bm{h})\bigr)\,\bm{J}_{\bm{F}}(\bm{h})+\epsilon\,\bm{I}_{n}, (pullback) (7) where α , β > 0 \alpha,\beta>0 are calibration constants, ϵ > 0 \epsilon>0 regularizes the pullback, 𝐅 : 𝒜 → 𝒴 \mathbf{F}:\mathcal{A}\to\mathcal{Y} is the function from naturally occurring activations to naturally occurring behaviors, and 𝐠 y \bm{g}_{y} is any Riemannian metric on ℳ y \mathcal{M}_{y} (e.g., the induced Hellinger metric used in our experiments).

We discuss the intuitive interpretation of Defn. 1 below.

• The Flat Geometry G I \bm{G}_{I} . Linear steering treats activation space as Euclidean: all directions and regions are equally valid, with Geodesics as straight lines ℓ ⁡ ( t ) = ( 1 − t ) ​ 𝒉 0 + t ​ 𝒉 1 \bm{\ell}(t)=(1{-}t)\,\bm{h}_{0}+t\,\bm{h}_{1} . This geometry thus encodes no knowledge of naturally occurring activation or outputs.

• The Density Geometry G E \bm{G}_{E} . Manifold steering derives a geometry for activation space from naturally occurring internal representations. Specifically, consider the geometry induced from an energy function E ⁡ ( 𝒉 ) ∝ − log ⁡ p ⁡ ( 𝒉 ) E(\bm{h})\propto-\log p(\bm{h}) by rescaling the identity according to local density. Here e − E ⁡ ( 𝒉 ) e^{-E(\bm{h})} plays the role of an unnormalized density: large where activations concentrate (on ℳ h \mathcal{M}_{h} ) and small where they are sparse (off ℳ h \mathcal{M}_{h} ). The inverse makes off-manifold regions expensive and on-manifold movement cheap, with constants α , β > 0 \alpha,\beta>0 calibrating the dynamic range ( Béthune et al., 2025 ) . Geodesics under 𝑮 E \bm{G}_{E} thus follow ℳ h \mathcal{M}_{h} , recovering manifold steering.

• The Pullback Geometry G F \bm{G}_{F} . The steering path given by pullback derives geometric structure from naturally occurring model outputs. Specifically, 𝑮 F \bm{G}_{F} is the pullback of a chosen geometry on ℳ y \mathcal{M}_{y} through the Jacobian of the map from activation space to behavior space 𝑭 : 𝒜 → 𝒴 \bm{F}:\mathcal{A}\to\mathcal{Y} . By construction, path length under 𝑮 F \bm{G}_{F} equals path length of the induced behavioral trajectory along ℳ y \mathcal{M}_{y} (up to a regularization term). Geodesics under 𝑮 F \bm{G}_{F} are therefore activation paths whose induced behavioral trajectories are geodesics on ℳ y \mathcal{M}_{y} —exactly the pullback construction of § 3.3 . The regularization ϵ ​ 𝑰 n \epsilon\,\bm{I}_{n} ensures positive definiteness, since 𝑱 𝑭 \bm{J}_{\bm{F}} has rank at most | 𝒵 | − 1 ≪ n |\mathcal{Z}|-1\ll n ; as ϵ \epsilon tends to 0, the geometry approaches the pure pullback in the range of 𝑱 𝑭 \bm{J}_{\bm{F}} and remains Euclidean in its null space.

Overall, we claim that while the metrics 𝑮 E \bm{G}_{E} and 𝑮 F \bm{G}_{F} are derived from different sources (internal activations and outputs, respectively), they converge on approximately the same paths in activation space (§ 3.3 ). This suggests the manifolds ℳ h \mathcal{M}_{h} and ℳ y \mathcal{M}_{y} are two images of the same conceptual geometry, related by an approximate Riemannian isometry. Consequently, the question of optimally steering model behavior boils down to isolating the geometry of a concept and defining operators to navigate it.

## 4 Manifold Steering Yields Factored Control in Multi-Dimensional Spaces

Our experiments thus far have been limited to one dimensional conceptual spaces arising from training data imbued with real-world structure, i.e., days, months, ages, and letters. In turn, the manifolds we found have been one dimensional curves with a single intrinsic coordinate. Now, we extend our results to a setting with two dimensional conceptual spaces whose geometry are defined via in-context learning. We fit manifolds and show there is a two dimensional intrinsic coordinate system for the manifold, where steering along each coordinate controls an independent dimension of the conceptual space.

#### In-context learning tasks with synthetic conceptual spaces.

Park et al. (2025b) introduce a family of tasks to study the in-context learning of representations (ICLR). For each task, arbitrary tokens are assigned to a discrete graphical structure and language models are supplied with sequences of tokens derived from a random walk on that graph. They show that the statistical patterns in the random walk of tokens induce a reorganization of representations that recapitulates the graphical structure used to generate data. This in turn enables the language model to match the next token distribution, i.e., predict tokens adjacent to the current location of the random walk on the grid. For our two experiments, we assign arbitrary tokens to grid and cylinder graph structures. Thus, the conceptual domain 𝒵 \mathcal{Z} is the set of tokens and the distance metric d 𝒵 d_{\mathcal{Z}} is distance on the graph used to generate the random walk. Fig. 6 (a) shows an example grid and an input prompt generated by a random walk.

#### Manifold fitting.

The ICLR grid manifold ℳ h \mathcal{M}_{h} is topologically described by a two dimensional surface with no holes or tears. The activation geometry of ℳ h \mathcal{M}_{h} is more complex. Its semi-spherical shape shown in Fig. 6 (c) is induced by task statistics: the random walk visits inner sites more frequently than peripheral sites, leading to slight distortions with respect to the ground truth geometry ( Park et al., 2025b ; Yang et al., 2025 ; Karkada et al., 2026 ) . We fit two-dimensional sheets to internal activations and output distributions via thin plate splines (TPS; Duchon 1977 ; Bookstein 1989 ), which can be seen as the 2 2 D analog of the cubic splines used previously. In this case, we use activations corresponding to the last token in the context, and compute centroids according to graph location at a given timestep. Then, TPS finds the smoothest surface interpolating through the centroids (see App. A.3 for further details).

#### Isometry results.

For each ICLR domain, we compute pairwise distance matrices over graph-node centroids under three metrics: Euclidean (linear) distance in the activation subspace, geodesic distance along the fitted activation manifold ℳ h \mathcal{M}_{h} , and geodesic distance along the behavior manifold ℳ y \mathcal{M}_{y} . We find very high correlations between geodesic paths on the activation and behavior manifolds ( r = .99 r=.99 for both the 5 × 5 5\times 5 grid and 9 × 9 9\times 9 cylinder domains) and reduced correlations for linear paths ( 5 × 5 5\times 5 grid r = 0.90 r=0.90 ; 9 × 9 9\times 9 cylinder r = 0.81 r=0.81 ). To further examine these results, we embed each distance matrix with multidimensional scaling (MDS). Fig. 6 (b) shows a clean grid structure in the activation manifold and behavior manifold embeddings, while the linear paths in activation space yield a warped surface. Again, we see the conceptual space recapitulated in both representation and behavior.

#### Manifold vs. Linear steering.

We next test whether the fitted two-dimensional activation manifold affords coherent, factored control over the graph geometry used to generate the ICLR inputs. In particular, we assess whether we can control the position of the random walk input via intervention, and, moreover, whether there is an intrinsic coordinate system where steering along each coordinate independently controls the horizontal and vertical position on the grid. For each ordered pair of nodes, we use manifold steering and linear steering to interpolate between the start and end centroid and average results over 5 input prompts.

The top panel of Fig. 6 (c) shows that manifold steering produces smooth transitions vertically along the steered graph dimension while remaining at the same horizontal position. The bottom panel of Fig. 6 (c) shows similar smooth transitions but along a horizontal dimension while keeping the same vertical position. This demonstrates the manifold has an intrinsic coordinate system corresponding to the two dimensions of the grid, enabling factored control. Furthermore, this shows the smooth and ordered transitions of manifold steering generalize to multi-dimensional spaces. In contrast, linear steering again fails to provide ordered transitions through grid locations, and shows very clear ‘teleportation’ behavior between the endpoint locations along its path.

## 5 Manifold Steering on a Visual World Model: Mountain Car Task

We now ask whether the same principles of geometry-aware steering extend to the visual domain of world models. This question is practically motivated: learned world models that predict future observations from past frames and actions are central to model-based reinforcement learning and robotic planning ( Ha and Schmidhuber, 2018 ; Hafner et al., 2020 ; Team, 2025 ; Black et al., 2024 ) . If the internal representations of such models admit geometric structure, manifold-based steering could provide a principled mechanism for intervening on a model’s behavior through changing its beliefs about the state of the world.

#### Environment and model architecture.

We train a recurrent world model on the Mountain Car environment ( Moore, 1990 ; Sutton and Barto, 2018 ) , a classical control task in which a car must escape a valley by building momentum. The environment has continuous position p ∈ [ − 1.2 , 0.6 ] p\in[-1.2,0.6] , continuous velocity v ∈ [ − 0.07 , 0.07 ] v\in[-0.07,0.07] , and three discrete actions (left, no-op, right). The model predicts the next frame x t + 1 x_{t+1} given the previous frame x t x_{t} and action a t a_{t} (see Fig. 7 (a) for an illustration). The full architecture is shown in Fig. 8 : A convolutional encoder maps each 128 × 128 × 3 128\times 128\times 3 RGB frame to a latent vector, v t v_{t} , which is concatenated with a learned action embedding e ⁡ ( a t ) ∈ ℝ 16 e(a_{t})\in\mathbb{R}^{16} and fed to a Gated Recurrent Unit (GRU; Cho et al. 2014 ): 𝐡 t = GRU ⁡ ( [ v t ; e ⁡ ( a t ) ] , 𝐡 t − 1 ) ∈ ℝ n ; v t = LayerNorm ⁡ ( f enc ​ ( x t ) ) ∈ ℝ n , \mathbf{h}_{t}=\mathrm{GRU}\!\bigl([v_{t};\,e(a_{t})],\;\mathbf{h}_{t-1}\bigr)\in\mathbb{R}^{n};\;\;v_{t}=\mathrm{LayerNorm}\!\bigl(f_{\mathrm{enc}}(x_{t})\bigr)\in\mathbb{R}^{n}, (8) where n = 64 n=64 . A convolutional decoder produces a residual image from the hidden state, yielding the prediction x ^ t + 1 = x t + f dec ​ ( 𝐡 t ) \hat{x}_{t+1}=x_{t}+f_{\mathrm{dec}}(\mathbf{h}_{t}) .

#### Activation and behavior manifold fitting.

For this setting, we consider position to play the role of the conceptual domain 𝒵 = [ p min , p max ] \mathcal{Z}=[p_{\text{min}},p_{\text{max}}] and aim to capture the manifold structure in both activation and behavior space of the vision encoder. To start, we first collect encoder activations from 100 rollouts in the environment (see § B.1 for details) and observe they occupy a curved, low-dimensional manifold ℳ h ⊂ ℝ n \mathcal{M}_{h}\subset\mathbb{R}^{n} (Fig. 7 (c)). We parameterize this manifold by partitioning the position range into bins and fit a smooth spline through the means { μ b } b = 1 B ⊂ ℝ n \{\mu_{b}\}_{b=1}^{B}\subset\mathbb{R}^{n} . For a given input, x x , we compute the output distribution over positions, 𝐩 ⁡ ( x ) \mathbf{p}(x) using the distance of the activations v ⁡ ( x ) v(x) to the centroid for each position: 𝐩 ⁡ ( x ) = softmax ​ ( − ‖ v − μ b ‖ 2 τ ) b = 1 B ∈ Δ B − 1 , \mathbf{p}(x)\;=\;\mathrm{softmax}\!\left(-\frac{\|v-\mu_{b}\|_{2}}{\tau}\right)_{b=1}^{B}\;\in\;\Delta^{B-1}, (9) with temperature τ = 0.5 \tau=0.5 . We follow § 3.2 to parameterize the behavior manifold ℳ y \mathcal{M}_{y} by embedding each bin in Hellinger coordinates on the unit sphere and fit a 1D smoothing spline γ ℳ y : 𝒵 → ℝ B \gamma_{\mathcal{M}_{y}}\colon\mathcal{Z}\to\mathbb{R}^{B} parameterized by position (full details in App. B ). Note that both ℳ h \mathcal{M}_{h} and ℳ y \mathcal{M}_{y} are 1D structures parameterized by the conceptual coordinate p p ; under PCA visualization (Fig. 12 ), both trace closed curves in their respective ambient spaces. The curves are closed because visually distinctive states at the wall, p ≈ − 1.2 p\approx-1.2 , and goal, p ≈ 0.4 p\approx 0.4 , are mapped to neighboring activations.

#### Geometry-aware steering in activation space.

Fig. 7 compares linear (Eq. 1 ) and manifold (Eq. 2 ) steering through K = 20 K=20 waypoints between encoder states corresponding to positions p A = − 0.4 p_{A}=-0.4 and p B = 0.4 p_{B}=0.4 , projected into the first three principal components of encoder space. The geodesic path closely tracks ℳ h \mathcal{M}_{h} , and the corresponding decoded frames display a smooth, coherent progression of the car through intermediate positions. The linear path departs from ℳ h \mathcal{M}_{h} at intermediate points and decoded frames exhibit blurred or ambiguous car placement, reflecting an incoherent superposition. Then, a ‘teleportation’ to the endpoint is observed, analogous to the behavior of linear steering in the language model experiments. Moreover, linear steering causes the probability distribution over position to show greater spread compared to on-manifold paths, yielding the ambiguous car placement seen in intermediate points along the path. Finally, we reproduce the pullback procedure in § C.3 and show that optimizing paths in the output distribution over possible car positions results in activation space paths that closely track the ℳ h \mathcal{M}_{h} (Fig. 12 ).

#### The geometry assumed by linear steering is not faithful to the conceptual ordering.

To make the difference between the two steering metrics visually concrete, we apply multidimensional scaling (MDS) to the pairwise distance matrices induced by three different distance functions over W = 50 W=50 anchor positions evenly spaced along [ p min , p max ] [p_{\text{min}},p_{\text{max}}] (Fig. 7 (b)). Both activation space and behavior space on-manifold distance embeddings recover a clean one-dimensional rainbow ordering of positions, while the linear distance embedding produces a scrambled three-dimensional structure whose colors are visibly out of order. This is because ℳ h \mathcal{M}_{h} folds back on itself in the encoder’s ambient space, so two activations whose underlying positions are far apart can sit arbitrarily close in ambient space. Quantitatively, the Pearson correlation between the two arc-length distance matrices is r = 0.99 r=0.99 , while correlation between activation-space linear paths and behavior manifold arc-length falls to r = 0.06 r=0.06 , confirming that the linear-steering metric is not a faithful proxy for the conceptual ordering that the encoder has learned.

## 6 Related Work

#### Activation Steering and the Linear Representation Hypothesis.

Activation steering protocols ( Bau et al., 2018 ; Subramani et al., 2022 ; Marks and Tegmark, 2023 ; Panickssery et al., 2024 ; Turner et al., 2024 ) are often motivated by the linear representation hypothesis (LRH)—a geometric assumption on model representations ( Smolensky, 1986 ; Elhage et al., 2022a ; Park et al., 2023 ; Costa et al., 2025 ; Zheng et al., 2025 ) . In particular, LRH argues neural networks encode concepts, i.e., latent variables underlying the data distribution ( Wang et al., 2023b ; Rajendran et al., 2024a ; Rajendran et al., 2024b ; Okawa et al., 2024 ) , along directions. This motivates tools like linear probing ( Belinkov, 2022 ; Guerner et al., 2023 ) and sparse autoencoders ( Cunningham et al., 2023 ; Bricken et al., 2023 ; Gao et al., 2025 ; Bussmann et al., 2024 ; Fel et al., 2025a ) . In the case where the representation geometry for a concept truly aligns with LRH, Bigelow et al. (2025) showed the effects of activation steering on model behavior can be accurately captured by a linear increase in concept log-probability. However, in the general scenario where geometry of representations does not abide by LRH, the effects of linear steering protocols are less clear. Recent work has started to fill this gap: e.g., work by Rodriguez et al. (2025) ; Ravfogel et al. (2022) has shown that linear steering protocols match the first moments of the current output distribution produced by the model with the target distribution; however, the effects on higher order moments can be unconstrained and adversarial (see results by Sarfati et al. (2026) ), possibly explaining why it produces incoherent outputs.

In contrast, when the representation geometry is fully respected, our work shows that steering smoothly interpolates the source and the target distributions. Prior work has shown similar results to this effect in narrow domains, e.g., Engels et al. (2024) ablate representations and write the days-of-the-week circle directly and Kantamneni and Tegmark (2025) follow a similar protocol for a helix representing numbers, but they lack a more general account of how representation geometry and output behavior map on to each other. The closest work to ours is the contemporary paper by Park et al. (2026) , who study a toy model where the representation-to-output distribution mapping is described via a simple softmax operation.

#### Activation Geometry and its Origins.

A large body of recent work has shown neural networks encode concepts along nonlinear, curved geometries embedded in low-dimensional subspaces across both modalities and architectures ( Fel et al., 2025b ; Pearce et al., 2025 ; Yocum et al., 2025 ; Modell et al., 2025a ; Lubana et al., 2025 ; Costa et al., 2025 ; Park et al., 2025b ; Engels et al., 2024 ; Karkada et al., 2026 ; Shai et al., 2024a ; Shai et al., 2026 ; Saxe et al., 2019 ; Park et al., 2025c ; Morwani et al., 2024 ; Kantamneni and Tegmark, 2025 ; Song and Zhong, 2023 ; Zhou et al., 2025 ; Maheswaranathan et al., 2019 ) . While earlier work ( Saxe et al., 2019 ; Arora et al., 2018 ; Park et al., 2023 ; Yocum et al., 2025 ) concretized, in toy settings, how structure in the data-generating process imposes geometric constraints on a neural network’s representations, only recently have such accounts been extended to make predictions about the geometry of neural representations at scale (e.g., Merullo et al. (2025) ). Karkada et al. (2026) and Korchinski et al. (2025) argue that symmetries in data statistics enforce geometries best suited for reflecting the uncertainty of the distribution in a model’s representation (cf. Prieto et al. 2026 ), and offer plausible accounts for the formation of representations in-context, as shown by works such as Park et al. (2025a) and Lepori et al. (2026) .

#### Causal Analysis of Neural Networks.

Several works have convincingly argued that tools like probing or visualization of representations are insufficient to make claims about model behavior, i.e., artifacts produced via these tools can yield misleading explanations for why a model behaves the way it does ( Geiger et al., 2020 ; Belinkov, 2022 ; Bolukbasi et al., 2021 ; Saphra and Wiegreffe, 2024 ) . As such, a vast array of research has used intervention on activations to study model internals ( Li et al., 2017 ; Giulianelli et al., 2018 ; Cammarata et al., 2020 ; Elazar et al., 2020 ; Ravfogel et al., 2022 ; Ravfogel et al., 2023a ; Ravfogel et al., 2023b ; Belrose et al., 2023 ; Geva et al., 2023 ; Meng et al., 2022 ; Meng et al., 2023 ; Vig et al., 2020 ; Geiger et al., 2020 ; Davies et al., 2023 ; Stolfo et al., 2023 ; Guerner et al., 2023 ; Wang et al., 2023a ; Todd et al., 2024 ; Arora et al., 2024 ; Huang et al., 2024 ; Feng and Steinhardt, 2024 ; Mueller et al., 2025 ; Prakash et al., 2025 ; Gur-Arieh et al., 2025 ; Grant et al., 2025 ; Rodriguez et al., 2024 ) . This interpretability research leverages the frameworks of causal mediation ( Pearl, 2001 ; Vig et al., 2020 ; Mueller et al., 2026 ) and causal abstraction ( Rubenstein et al., 2017 ; Beckers and Halpern, 2019 ; Geiger et al., 2021 ; Geiger et al., 2025a ; Geiger et al., 2025b ) to ground understanding of model internals in the theory of causality ( Hume, 1748 ; Pearl, 1999 ; Spirtes et al., 2000 ) .

## 7 Discussion

#### Geometry-aware steering reveals the shared structure of behavior and representation.

We build out an empirical phenomenology that relates structure in activation space to the model output behavior. First, we show an isometry between representations and behavior manifolds, i.e., distance between two points on the activation manifold ℳ h \mathcal{M}_{h} aligns with distance between the distributions induced by those points on the behavior manifold ℳ y \mathcal{M}_{y} . Second, we show that steering representations along geodesics on ℳ h \mathcal{M}_{h} induces smooth, coherent transitions in behavior that follow geodesics on ℳ y \mathcal{M}_{y} . Third, we show that optimizing interventions to produce behaviors following geodesics on ℳ y \mathcal{M}_{y} recover trajectories in activation space that follow ℳ h \mathcal{M}_{h} . Thus, we establish a causal bridge between representation and behavior that reveals shared structure reflecting underlying conceptual geometry.

Our results also suggest that pathologies of linear steering—brittleness, incoherence, off-target effects ( Wu et al., 2025 ; Bigelow et al., 2025 ; Da Silva et al., 2025 ; Bhalla et al., 2024 ; Tan et al., 2024 ) —stem from the mismatch between assumed flat geometry and the true curved geometry of representation space, rather than an inherent challenge with representation-based intervention. This reframes the challenge of steering from “finding the right direction” to “finding the right geometry”.

#### Where does the shared geometry of behavior and representation come from?

While we do not study the origins of the shared geometry between behavior and representation, our experimental results are consistent with the hypothesis that conceptual structure constrains the geometry of both representation and behavior. While data statistics shape the geometry of neural representations ( Merullo et al., 2025 ; Karkada et al., 2026 ; Prieto et al., 2026 ) , this fails to explain how geometric structure is formed for out-of-distribution inputs. For example, our in-context learning tasks (Sec. 4 ) have synthetically defined geometries that imbue tokens with contextual meaning that is wildly different from the meaning learned during training. As such, the model must form novel representations and produce novel behaviors. The fact that we are able to establish a shared geometry for representation and behavior in these novel in-context learning tasks suggests that regardless of how training data statistics inform the geometries seen in the model, the output behavior is now computationally constrained by the activation geometry (see the contemporary work by Yocum et al. (2025) for a formalization of this claim).

#### Intrinsic coordinates of representation manifolds as units of causal analysis.

Mueller et al. (2024) frames the field of mechanistic interpretability as being on a quest to discover a primitive unit of representation best suited for the causal analysis of neural network internals. Causal abstraction provides a theoretical framework for defining such units of analysis ( Geiger et al., 2025a ; Geiger et al., 2025b ) , however Sutter et al. (2025) point out that allowing arbitrarily complex units admits degenerate solutions. Our work suggests a path toward both answering Mueller et al. (2024) and addressing the problem identified by Sutter et al. (2025) : the appropriate units of causal analysis are intrinsic coordinates on manifolds in activation space, and fitting these manifolds to naturally occurring activations provides a constraint that helps rule out degenerate solutions (cf. Grant et al. 2026 ).

## 8 Future Work and Limitations

The goal of our paper was to understand the role of geometry in neural networks and, subsequently, use this understanding to concretize what it means to steer model behavior via representations. We have shown that the geometry of neural network representations provides a blueprint for effective control. When interventions respect the geometry of activation space, the change in behavior is smooth and coherent; when they ignore it, they risk producing states with no natural behavioral counterpart. While we believe our results have enabled significant progress towards the motivating goals, there are remaining limitations that need to be addressed in future work.

• Expanding experimental validation to more complex domains. To illustrate our arguments, we focused on simple settings for which the concept of interest had a well-defined domain (e.g., weekdays), and the expected task outputs are the concepts themselves, therefore the conceptual geometry is directly displayed in the outputs. To further validate the claims posited in this paper, future work is needed to explore more abstract concepts, e.g., refusals ( Arditi et al., 2024 ) , sycophancy ( Vennemeyer et al., 2025 ) , and persuasion ( Costello et al., 2026 ) . For such concepts, output behavior will likely reflect conceptual structure in subtler ways, and it remains to be tested whether the conceptual geometry of such concepts can be inferred from behavior and related to representations as we did in this work. Moreover, in these more complex cases, it is unclear what are the right primitives for a representational account; we may need a notion of dynamics over manifolds, a view of representation as an aggregation of several geometric structures (similar to results seen by Fel et al. (2025b) in a vision context), or perhaps an altogether different object. Even if geometry is the right substrate to work with, we emphasize the simplicity of our domains allowed us to easily isolate the target concept’s geometry via synthetic, template-based text. Moving to more complex scenarios will require isolating the geometry of concepts from in-the-wild data.

• Moving from token to sequence-level outputs. Another way in which our tasks are simplified is our focus on the next-token distribution. This makes analysis feasible and helps avoid the combinatorial complexity involved in studying multi-token sequences. The obvious way to expand from our work’s token-level focus to sequence-level focus involves formalizing arguments in the language of “beliefs”, i.e., latent variables underlying the posterior predictive induced by a model in response to an input ( Bigelow et al., 2023 ; Bigelow et al., 2025 ; Wurgaft et al., 2025 ) . Correspondingly, what we expect to see via geometry-aware interventions is the nature of output sequences produced by a model will change as we perform steering: e.g., navigating the geometry of sycophancy (were it to exist) should allow us to alter the extent or type of sycophancy exhibited in model outputs; however, this property will be latent, rather than a concrete token-level change.

• Fitting the geometry. While we used a specific protocol to fit the observed geometries ( Bookstein, 1989 ) , we note there is a rich literature on fitting low-dimensional manifolds ( Coifman and Lafon, 2006 ; Brand, 2002 ; Schölkopf et al., 1997 ; Roweis and Saul, 2000 ; Jones, 2024 ; Jones and Lanners, 2026 ; Meilă and Zhang, 2023 ) . Critically, beyond just fitting the manifold, what we seek is an operator that allows us to navigate the manifold. For the domains analyzed in this work, we have ground-truth knowledge about how different states of the concept relate to each other, which allows us to define intrinsic coordinates for spline fitting. An unsupervised protocol would however significantly broaden the applicability of our methods.

• Manipulating intermediate algorithmic variables. All of our experiments are about manipulating the output behavior of neural networks directly. However, the most interesting control protocols will require manipulating intermediate quantities that mediate the flow of information from input to output, e.g., an image model determining the shape of an object in service of predicting its weight.

## Acknowledgments

The authors thank David Klindt, David Bau, Thomas Icard, Jing Huang, and the Mechanisms team at Goodfire for helpful conversations during the course of this project.

## References

Amari and Nagaoka (2000) S. Amari and H. Nagaoka Methods of information geometry . Vol. 191 , American Mathematical Soc. . Cited by: §2.2 .

Arditi et al. (2024) A. Arditi, O. Obeso, A. Syed, D. Paleka, N. Panickssery, W. Gurnee, and N. Nanda Refusal in language models is mediated by a single direction . Advances in Neural Information Processing Systems 37 , pp. 136037–136083 . Cited by: 1st item .

Arora et al. (2024) A. Arora, D. Jurafsky, and C. Potts CausalGym: benchmarking causal interpretability methods on linguistic tasks . In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , L. Ku, A. Martins, and V. Srikumar (Eds.) , Bangkok, Thailand , pp. 14638–14663 . External Links: Link Cited by: §6 .

Arora et al. (2018) S. Arora, Y. Li, Y. Liang, T. Ma, and A. Risteski Linear algebraic structure of word senses, with applications to polysemy . Transactions of the Association for Computational Linguistics 6 , pp. 483–495 . External Links: Link , Document Cited by: §6 .

Bau et al. (2018) A. Bau, Y. Belinkov, H. Sajjad, N. Durrani, F. Dalvi, and J. Glass Identifying and controlling important neurons in neural machine translation . External Links: 1811.01157 , Link Cited by: §3.1 , §6 .

Bau et al. (2019) A. Bau, Y. Belinkov, H. Sajjad, N. Durrani, F. Dalvi, and J. Glass Identifying and controlling important neurons in neural machine translation . In International Conference on Learning Representations , External Links: Link Cited by: §1 .

Beckers and Halpern (2019) S. Beckers and J. Halpern Abstracting causal models . In AAAI Conference on Artificial Intelligence , Cited by: §6 .

Belinkov (2022) Y. Belinkov Probing classifiers: promises, shortcomings, and advances . Computational Linguistics 48 ( 1 ), pp. 207–219 . Cited by: §6 , §6 .

Bellmund et al. (2018) J. L. Bellmund, P. Gärdenfors, E. I. Moser, and C. F. Doeller Navigating cognition: spatial codes for human thinking . Science 362 ( 6415 ), pp. eaat6766 . Cited by: §2.1 .

Belrose et al. (2023) N. Belrose, D. Schneider-Joseph, S. Ravfogel, R. Cotterell, E. Raff, and S. Biderman LEACE: perfect linear concept erasure in closed form . In Advances in Neural Information Processing Systems 36: Annual Conference on Neural Information Processing Systems 2023, NeurIPS 2023, New Orleans, LA, USA, December 10 - 16, 2023 , A. Oh, T. Naumann, A. Globerson, K. Saenko, M. Hardt, and S. Levine (Eds.) , External Links: Link Cited by: §6 .

Béthune et al. (2025) L. Béthune, D. Vigouroux, Y. Du, R. VanRullen, T. Serre, and V. Boutin Follow the energy, find the path: riemannian metrics from energy-based models . ArXiv e-print . Cited by: 2nd item , §3.2 .

Bhalla et al. (2024) U. Bhalla, S. Srinivas, A. Ghandeharioun, and H. Lakkaraju Towards unifying interpretability and control: evaluation via intervention . ArXiv e-print . Cited by: §1 , §7 .

Bigelow et al. (2023) E. J. Bigelow, E. S. Lubana, R. P. Dick, H. Tanaka, and T. D. Ullman In-context learning dynamics with random binary sequences . arXiv preprint arXiv:2310.17639 . Cited by: 2nd item .

Bigelow et al. (2025) E. Bigelow, D. Wurgaft, Y. Wang, N. Goodman, T. Ullman, H. Tanaka, and E. S. Lubana Belief dynamics reveal the dual nature of in-context learning and activation steering . External Links: 2511.00617 , Link Cited by: §1 , §6 , §7 , 2nd item .

Black et al. (2024) K. Black, N. Brown, D. Driess, A. Esmail, M. Equi, C. Finn, N. Fusai, L. Groom, K. Hausman, B. Ichter, S. Jakubczak, T. Jones, K. Ke, S. Levine, A. Li-Bell, M. Mothukuri, S. Nair, K. Pertsch, L. Shi, J. Tanner, Q. Vuong, A. Walling, H. Wang, and U. Zhilinsky π 0 \pi_{0} : A vision-language-action flow model for general robot control . arXiv preprint arXiv:2410.24164 . Cited by: §5 .

Bolukbasi et al. (2021) T. Bolukbasi, A. Pearce, A. Yuan, A. Coenen, E. Reif, F. Viégas, and M. Wattenberg An interpretability illusion for bert . arXiv preprint arXiv:2104.07143 . Cited by: §6 .

Bookstein (1989) F.L. Bookstein Principal warps: thin-plate splines and the decomposition of deformations . IEEE Transactions on Pattern Analysis and Machine Intelligence 11 ( 6 ), pp. 567–585 . External Links: Document Cited by: §A.3 , §4 , 3rd item .

Brand (2002) M. Brand Charting a manifold . Advances in neural information processing systems 15 . Cited by: 3rd item .

Bricken et al. (2023) T. Bricken, A. Templeton, J. Batson, B. Chen, A. Jermyn, T. Conerly, N. Turner, C. Anil, C. Denison, A. Askell, R. Lasenby, Y. Wu, S. Kravec, N. Schiefer, T. Maxwell, N. Joseph, Z. Hatfield-Dodds, A. Tamkin, K. Nguyen, B. McLean, J. E. Burke, T. Hume, S. Carter, T. Henighan, and C. Olah Towards monosemanticity: decomposing language models with dictionary learning . Transformer Circuits Thread . Cited by: §6 .

Bussmann et al. (2024) B. Bussmann, P. Leask, and N. Nanda Batchtopk sparse autoencoders . ArXiv e-print . Cited by: §6 .

Cammarata et al. (2020) N. Cammarata, S. Carter, G. Goh, C. Olah, M. Petrov, L. Schubert, C. Voss, B. Egan, and S. K. Lim Thread: circuits . Distill . Note: https://distill.pub/2020/circuits External Links: Document Cited by: §6 .

Chen et al. (2025) R. Chen, A. Arditi, H. Sleight, O. Evans, and J. Lindsey Persona vectors: monitoring and controlling character traits in language models . arXiv preprint arXiv:2507.21509 . Cited by: §1 .

Cho et al. (2014) K. Cho, B. van Merriënboer, C. Gulcehre, D. Bahdanau, F. Bougares, H. Schwenk, and Y. Bengio Learning phrase representations using RNN encoder-decoder for statistical machine translation . arXiv preprint arXiv:1406.1078 . Cited by: §5 .

Coifman and Lafon (2006) R. R. Coifman and S. Lafon Diffusion maps . Applied and computational harmonic analysis 21 ( 1 ), pp. 5–30 . Cited by: 3rd item .

Costa et al. (2025) V. Costa, T. Fel, E. S. Lubana, B. Tolooshams, and D. Ba From flat to hierarchical: extracting sparse representations with matching pursuit . Advances in Neural Information Processing Systems (NeurIPS) . Cited by: §6 , §6 .

Costello et al. (2026) T. H. Costello, K. Pelrine, M. Kowal, A. A. Arechar, J. Godbout, A. Gleave, D. Rand, and G. Pennycook Large language models can effectively convince people to believe conspiracies . arXiv preprint arXiv:2601.05050 . Cited by: 1st item .

Csordás et al. (2024) R. Csordás, C. Potts, C. D. Manning, and A. Geiger Recurrent neural networks learn to store and generate sequences using non-linear representations . arXiv preprint arXiv:2408.10920 . Cited by: §1 .

Cunningham et al. (2023) H. Cunningham, A. Ewart, L. Riggs, R. Huben, and L. Sharkey Sparse autoencoders find highly interpretable features in language models . ArXiv e-print . Cited by: §6 .

Da Silva et al. (2025) P. Q. Da Silva, H. Sethuraman, D. Rajagopal, H. Hajishirzi, and S. Kumar Steering off course: reliability challenges in steering language models . arXiv preprint arXiv:2504.04635 . Cited by: §1 , §7 .

Davies et al. (2023) X. Davies, M. Nadeau, N. Prakash, T. R. Shaham, and D. Bau Discovering variable binding circuitry with desiderata . CoRR abs/2307.03637 . External Links: Link , Document , 2307.03637 Cited by: §6 .

Duchon (1977) J. Duchon Splines minimizing rotation-invariant semi-norms in sobolev spaces . In Constructive Theory of Functions of Several Variables , W. Schempp and K. Zeller (Eds.) , Berlin, Heidelberg , pp. 85–100 . External Links: ISBN 978-3-540-37496-1 Cited by: §A.3 , §4 .

Elazar et al. (2020) Y. Elazar, S. Ravfogel, A. Jacovi, and Y. Goldberg Amnesic probing: behavioral explanation with amnesic counterfactuals . In Proceedings of the 2020 EMNLP Workshop BlackboxNLP: Analyzing and Interpreting Neural Networks for NLP , External Links: Document Cited by: §6 .

Elhage et al. (2022a) N. Elhage, T. Hume, C. Olsson, N. Schiefer, T. Henighan, S. Kravec, Z. Hatfield-Dodds, R. Lasenby, D. Drain, C. Chen, R. Grosse, S. McCandlish, J. Kaplan, D. Amodei, M. Wattenberg, and C. Olah Toy models of superposition . Transformer Circuits Thread . Cited by: §6 .

Elhage et al. (2022b) N. Elhage, T. Hume, C. Olsson, N. Schiefer, T. Henighan, S. Kravec, Z. Hatfield-Dodds, R. Lasenby, D. Drain, C. Chen, et al. Toy models of superposition . arXiv preprint arXiv:2209.10652 . Cited by: §1 .

Ellis et al. (2015) D. A. Ellis, R. Wiseman, and R. Jenkins Mental representations of weekdays . PloS one 10 ( 8 ), pp. e0134555 . Cited by: §2.1 .

Engels et al. (2024) J. Engels, E. J. Michaud, I. Liao, W. Gurnee, and M. Tegmark Not all language model features are one-dimensionally linear . arXiv preprint arXiv:2405.14860 . Cited by: §1 , §1 , §2.1 , §2.1 , §2.3 , §6 , §6 .

Fel et al. (2025a) T. Fel, E. S. Lubana, J. S. Prince, M. Kowal, V. Boutin, I. Papadimitriou, B. Wang, M. Wattenberg, D. Ba, and T. Konkle Archetypal sae: adaptive and stable dictionary learning for concept extraction in large vision models . Proceedings of the International Conference on Machine Learning (ICML) . Cited by: §6 .

Fel et al. (2025b) T. Fel, B. Wang, M. A. Lepori, M. Kowal, A. Lee, R. Balestriero, S. Joseph, E. S. Lubana, T. Konkle, D. Ba, et al. Into the rabbit hull: from task-relevant concepts in dino to minkowski geometry . arXiv preprint arXiv:2510.08638 . Cited by: §2.1 , §6 , 1st item .

Feng and Steinhardt (2024) J. Feng and J. Steinhardt How do language models bind entities in context? . In The Twelfth International Conference on Learning Representations , External Links: Link Cited by: §6 .

Gao et al. (2025) L. Gao, T. D. la Tour, H. Tillman, G. Goh, R. Troll, A. Radford, I. Sutskever, J. Leike, and J. Wu Scaling and evaluating sparse autoencoders . Proceedings of the International Conference on Learning Representations (ICLR) . Cited by: §6 .

Gärdenfors (2000) P. Gärdenfors Conceptual spaces: the geometry of thought . The MIT Press . External Links: ISBN 9780262273558 , Document , Link Cited by: §2.1 .

Geiger et al. (2025a) A. Geiger, D. Ibeling, A. Zur, M. Chaudhary, S. Chauhan, J. Huang, A. Arora, Z. Wu, N. Goodman, C. Potts, and T. Icard Causal abstraction: a theoretical foundation for mechanistic interpretability . Journal of Machine Learning Research . External Links: Link Cited by: §6 , §7 .

Geiger et al. (2025b) A. Geiger, D. Ibeling, A. Zur, M. Chaudhary, S. Chauhan, J. Huang, A. Arora, Z. Wu, N. Goodman, C. Potts, and T. Icard Causal abstraction: a theoretical foundation for mechanistic interpretability . Journal of Machine Learning Research 26 ( 83 ), pp. 1–64 . External Links: Link Cited by: §6 , §7 .

Geiger et al. (2021) A. Geiger, H. Lu, T. Icard, and C. Potts Causal abstractions of neural networks . In Proceedings of the 35th International Conference on Neural Information Processing Systems , NIPS ’21 , Red Hook, NY, USA . External Links: ISBN 9781713845393 Cited by: §6 .

Geiger et al. (2020) A. Geiger, K. Richardson, and C. Potts Neural natural language inference models partially embed theories of lexical entailment and negation . In Proceedings of the Third BlackboxNLP Workshop on Analyzing and Interpreting Neural Networks for NLP , A. Alishahi, Y. Belinkov, G. Chrupała, D. Hupkes, Y. Pinter, and H. Sajjad (Eds.) , Online , pp. 163–173 . External Links: Link , Document Cited by: §6 .

Geva et al. (2023) M. Geva, J. Bastings, K. Filippova, and A. Globerson Dissecting recall of factual associations in auto-regressive language models . External Links: 2304.14767 , Link Cited by: §6 .

Giulianelli et al. (2018) M. Giulianelli, J. Harding, F. Mohnert, D. Hupkes, and W. Zuidema Under the hood: using diagnostic classifiers to investigate and improve how language models track agreement information . In Proceedings of the 2018 EMNLP Workshop BlackboxNLP: Analyzing and Interpreting Neural Networks for NLP , T. Linzen, G. Chrupała, and A. Alishahi (Eds.) , Brussels, Belgium , pp. 240–248 . External Links: Link , Document Cited by: §6 .

Grant et al. (2025) S. Grant, N. D. Goodman, and J. L. McClelland Emergent symbol-like number variables in artificial neural networks . External Links: 2501.06141 , Link Cited by: §6 .

Grant et al. (2026) S. Grant, S. J. Han, A. R. Tartaglini, and C. Potts Addressing divergent representations from causal interventions on neural networks . External Links: 2511.04638 , Link Cited by: §7 .

Grathwohl et al. (2019) W. Grathwohl, K. Wang, J. Jacobsen, D. Duvenaud, M. Norouzi, and K. Swersky Your classifier is secretly an energy based model and you should treat it like one . ArXiv e-print . Cited by: §3.2 .

Guerner et al. (2023) C. Guerner, A. Svete, T. Liu, A. Warstadt, and R. Cotterell A geometric notion of causal probing . CoRR abs/2307.15054 . External Links: Link , Document , 2307.15054 Cited by: §6 , §6 .

Gur-Arieh et al. (2025) Y. Gur-Arieh, R. Mayan, C. Agassy, A. Geiger, and M. Geva Enhancing automated interpretability with output-centric feature descriptions . In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , External Links: Link Cited by: §6 .

Gurnee et al. (2026) W. Gurnee, E. Ameisen, I. Kauvar, J. Tarng, A. Pearce, C. Olah, and J. Batson When models manipulate manifolds: the geometry of a counting task . arXiv preprint arXiv:2601.04480 . Cited by: §1 .

Ha and Schmidhuber (2018) D. Ha and J. Schmidhuber World models . In Advances in Neural Information Processing Systems , Cited by: §5 .

Hafner et al. (2020) D. Hafner, T. Lillicrap, J. Ba, and M. Norouzi Dream to control: learning behaviors by latent imagination . In International Conference on Learning Representations , Cited by: §5 .

Hao et al. (2025) Y. Hao, A. Panda, S. Shabalin, and S. A. R. Ali Patterns and mechanisms of contrastive activation engineering . arXiv preprint arXiv:2505.03189 . Cited by: §1 .

Hopfield (1982) J. J. Hopfield Neural networks and physical systems with emergent collective computational abilities. . Proceedings of the national academy of sciences . Cited by: §3.2 .

Huang et al. (2024) J. Huang, Z. Wu, C. Potts, M. Geva, and A. Geiger RAVEL: evaluating interpretability methods on disentangling language model representations . In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , External Links: Link Cited by: §6 .

Hume (1748) D. Hume An enquiry concerning human understanding . A. Millar , London . Cited by: §6 .

Jones and Lanners (2026) I. Jones and D. Lanners Computing diffusion geometry . arXiv preprint arXiv:2602.06006 . Cited by: 3rd item .

Jones (2024) I. Jones Diffusion geometry . arXiv preprint arXiv:2405.10858 . Cited by: 3rd item .

Kantamneni and Tegmark (2025) S. Kantamneni and M. Tegmark Language models use trigonometry to do addition . External Links: 2502.00873 , Link Cited by: §1 , §6 , §6 .

Karkada et al. (2026) D. Karkada, D. J. Korchinski, A. Nava, M. Wyart, and Y. Bahri Symmetry in language statistics shapes the geometry of model representations . External Links: 2602.15029 , Link Cited by: §1 , §2.1 , §2.3 , §4 , §6 , §7 .

Korchinski et al. (2025) D. J. Korchinski, D. Karkada, Y. Bahri, and M. Wyart On the emergence of linear analogies in word embeddings . arXiv preprint arXiv:2505.18651 . Cited by: §6 .

Kozlowski et al. (2025) A. C. Kozlowski, C. Dai, and A. Boutyline Semantic structure in large language model embeddings . External Links: 2508.10003 , Link Cited by: §1 .

LeCun et al. (2006) Y. LeCun, S. Chopra, R. Hadsell, M. Ranzato, F. Huang, et al. A tutorial on energy-based learning . Predicting structured data . Cited by: §3.2 .

Lepori et al. (2026) M. A. Lepori, T. Linzen, A. Yuan, and K. Filippova Language models struggle to use representations learned in-context . arXiv preprint arXiv:2602.04212 . Cited by: §6 .

Li et al. (2017) J. Li, W. Monroe, and D. Jurafsky Understanding neural networks through representation erasure . External Links: 1612.08220 , Link Cited by: §6 .

Li et al. (2023) K. Li, O. Patel, F. Viégas, H. Pfister, and M. Wattenberg Inference-time intervention: eliciting truthful answers from a language model . In Proceedings of the 37th International Conference on Neural Information Processing Systems , NIPS ’23 , Red Hook, NY, USA . Cited by: §1 .

Lubana et al. (2025) E. S. Lubana, C. Rager, S. S. R. Hindupur, V. Costa, G. Tuckute, O. Patel, S. K. Murthy, T. Fel, D. Wurgaft, E. J. Bigelow, et al. Priors in time: missing inductive biases for language model interpretability . arXiv preprint arXiv:2511.01836 . Cited by: §2.1 , §6 .

Maheswaranathan et al. (2019) N. Maheswaranathan, A. Williams, M. Golub, S. Ganguli, and D. Sussillo Universality and individuality in neural dynamics across large populations of recurrent networks . Advances in neural information processing systems 32 . Cited by: §6 .

Marks and Tegmark (2023) S. Marks and M. Tegmark The geometry of truth: emergent linear structure in large language model representations of true/false datasets . External Links: 2310.06824 Cited by: §6 .

Marks and Tegmark (2024) S. Marks and M. Tegmark The geometry of truth: emergent linear structure in large language model representations of true/false datasets . External Links: 2310.06824 , Link Cited by: §1 .

Meilă and Zhang (2023) M. Meilă and H. Zhang Manifold learning: what, how, and why . External Links: 2311.03757 , Link Cited by: 3rd item .

Meng et al. (2022) K. Meng, D. Bau, A. Andonian, and Y. Belinkov Locating and editing factual associations in GPT . Advances in Neural Information Processing Systems 36 . Note: arXiv:2202.05262 Cited by: §6 .

Meng et al. (2023) K. Meng, A. S. Sharma, A. J. Andonian, Y. Belinkov, and D. Bau Mass-editing memory in a transformer . In The Eleventh International Conference on Learning Representations, ICLR 2023, Kigali, Rwanda, May 1-5, 2023 , External Links: Link Cited by: §6 .

Merullo et al. (2025) J. Merullo, N. A. Smith, S. Wiegreffe, and Y. Elazar On linear representations and pretraining data frequency in language models . External Links: 2504.12459 , Link Cited by: §1 , §6 , §7 .

Modell et al. (2025a) A. Modell, P. Rubin-Delanchy, and N. Whiteley The origins of representation manifolds in large language models . External Links: 2505.18235 , Link Cited by: §2.1 , §6 .

Modell et al. (2025b) A. Modell, P. Rubin-Delanchy, and N. Whiteley The origins of representation manifolds in large language models . External Links: 2505.18235 , Link Cited by: §1 , §1 , §2.1 , §2.3 .

Moore (1990) A. W. Moore Efficient memory-based learning for robot control . Ph.D. Thesis , University of Cambridge . Cited by: §1 , Figure 7 , §5 .

Morwani et al. (2024) D. Morwani, B. L. Edelman, C. Oncescu, R. Zhao, and S. M. Kakade Feature emergence via margin maximization: case studies in algebraic tasks . In The Twelfth International Conference on Learning Representations , Cited by: §6 .

Mueller et al. (2024) A. Mueller, J. Brinkmann, M. L. Li, S. Marks, K. Pal, N. Prakash, C. Rager, A. Sankaranarayanan, A. S. Sharma, J. Sun, E. Todd, D. Bau, and Y. Belinkov The quest for the right mediator: A history, survey, and theoretical grounding of causal interpretability . CoRR abs/2408.01416 . External Links: Link , Document , 2408.01416 Cited by: §3.1 , §7 .

Mueller et al. (2026) A. Mueller, J. Brinkmann, M. Li, S. Marks, K. Pal, N. Prakash, C. Rager, A. Sankaranarayanan, A. S. Sharma, J. Sun, E. Todd, D. Bau, and Y. Belinkov The quest for the right mediator: surveying mechanistic interpretability for nlp through the lens of causal mediation analysis . Computational Linguistics , pp. 1–48 . External Links: ISSN 0891-2017 , Document , Link , https://direct.mit.edu/coli/article-pdf/doi/10.1162/COLI.a.572/2554934/coli.a.572.pdf Cited by: §6 .

Mueller et al. (2025) A. Mueller, A. Geiger, S. Wiegreffe, D. Arad, I. Arcuschin, A. Belfki, Y. S. Chan, J. Fiotto-Kaufman, T. Haklay, M. Hanna, J. Huang, R. Gupta, Y. Nikankin, H. Orgad, N. Prakash, A. Reusch, A. Sankaranarayanan, S. Shao, A. Stolfo, M. Tutek, A. Zur, D. Bau, and Y. Belinkov MIB: a mechanistic interpretability benchmark . External Links: 2504.13151 , Link Cited by: §6 .

Okawa et al. (2024) M. Okawa, E. S. Lubana, R. P. Dick, and H. Tanaka Compositional abilities emerge multiplicatively: exploring diffusion models on a synthetic task . External Links: 2310.09336 Cited by: §6 .

Panickssery et al. (2024) N. Panickssery, N. Gabrieli, J. Schulz, M. Tong, E. Hubinger, and A. M. Turner Steering llama 2 via contrastive activation addition . External Links: 2312.06681 , Link Cited by: §1 , §6 .

Park et al. (2025a) C. F. Park, A. Lee, E. S. Lubana, Y. Yang, M. Okawa, K. Nishi, M. Wattenberg, and H. Tanaka ICLR: in-context learning of representations . In International Conference on Learning Representations , Y. Yue, A. Garg, N. Peng, F. Sha, and R. Yu (Eds.) , Vol. 2025 , pp. 53258–53284 . External Links: Link Cited by: §2.1 , §6 .

Park et al. (2025b) C. F. Park, A. Lee, E. S. Lubana, Y. Yang, M. Okawa, K. Nishi, M. Wattenberg, and H. Tanaka ICLR: in-context learning of representations . In The Thirteenth International Conference on Learning Representations , Cited by: §A.1 , §1 , §1 , Figure 6 , §4 , §4 , §6 .

Park et al. (2025c) K. Park, Y. J. Choe, Y. Jiang, and V. Veitch The geometry of categorical and hierarchical concepts in large language models . Proceedings of the International Conference on Learning Representations (ICLR) . Cited by: §6 .

Park et al. (2023) K. Park, Y. J. Choe, and V. Veitch The linear representation hypothesis and the geometry of large language models . arXiv preprint arXiv:2311.03658 . Cited by: §1 , §6 , §6 .

Park et al. (2026) K. Park, T. Nief, Y. J. Choe, and V. Veitch The information geometry of softmax: probing and steering . arXiv preprint arXiv:2602.15293 . Cited by: §6 .

Pearce et al. (2025) M. Pearce, E. Simon, M. Byun, and D. Balsam Finding the tree of life in evo 2 . Goodfire . Note: Correspondence to michael@goodfire.ai Cited by: §1 , §6 .

Pearl (1999) J. Pearl Probabilities of causation: three counterfactual interpretations and their identification . Synthese 121 ( 1 ), pp. 93–149 . Cited by: §6 .

Pearl (2001) J. Pearl Direct and indirect effects . External Links: 1301.2300 , Link Cited by: §3.1 , §6 .

Prakash et al. (2025) N. Prakash, N. Shapira, A. S. Sharma, C. Riedl, Y. Belinkov, T. R. Shaham, D. Bau, and A. Geiger Language models use lookbacks to track beliefs . External Links: 2505.14685 , Link Cited by: §6 .

Pres et al. (2024) I. Pres, L. Ruis, E. S. Lubana, and D. Krueger Towards reliable evaluation of behavior steering interventions in llms . arXiv preprint arXiv:2410.17245 . Cited by: §1 .

Prieto et al. (2026) L. Prieto, E. Stevinson, M. Barsbey, T. Birdal, and P. A. M. Mediano Correlations in the data lead to semantically rich feature geometry under superposition . In The Fourteenth International Conference on Learning Representations , External Links: Link Cited by: §1 , §2.1 , §6 , §7 .

Rajendran et al. (2024a) G. Rajendran, S. Buchholz, B. Aragam, B. Schölkopf, and P. Ravikumar From causal to concept-based representation learning . Advances in Neural Information Processing Systems 37 , pp. 101250–101296 . Cited by: §6 .

Rajendran et al. (2024b) G. Rajendran, S. Buchholz, B. Aragam, B. Schölkopf, and P. Ravikumar Learning interpretable concepts: unifying causal representation learning and foundation models . arXiv preprint arXiv:2402.09236 . Cited by: §6 .

Ravfogel et al. (2023a) S. Ravfogel, Y. Goldberg, and R. Cotterell Log-linear guardedness and its implications . In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), ACL 2023, Toronto, Canada, July 9-14, 2023 , A. Rogers, J. L. Boyd-Graber, and N. Okazaki (Eds.) , pp. 9413–9431 . External Links: Link , Document Cited by: §6 .

Ravfogel et al. (2022) S. Ravfogel, M. Twiton, Y. Goldberg, and R. Cotterell Linear adversarial concept erasure . External Links: 2201.12091 Cited by: §6 , §6 .

Ravfogel et al. (2023b) S. Ravfogel, F. Vargas, Y. Goldberg, and R. Cotterell Kernelized concept erasure . External Links: 2201.12191 Cited by: §6 .

Reinsch (1967) C. H. Reinsch Smoothing by spline functions . Numerische mathematik 10 ( 3 ), pp. 177–183 . Cited by: §A.3 , §2.2 .

Rimsky et al. (2024) N. Rimsky, N. Gabrieli, J. Schulz, M. Tong, E. Hubinger, and A. Turner Steering llama 2 via contrastive activation addition . In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , L. Ku, A. Martins, and V. Srikumar (Eds.) , Bangkok, Thailand , pp. 15504–15522 . External Links: Link , Document Cited by: §1 .

Rodriguez et al. (2024) J. D. Rodriguez, A. Mueller, and K. Misra Characterizing the role of similarity in the property inferences of language models . CoRR abs/2410.22590 . External Links: Link , Document , 2410.22590 Cited by: §6 .

Rodriguez et al. (2025) P. Rodriguez, A. Blaas, M. Klein, L. Zappella, N. Apostoloff, M. Cuturi, and X. Suau Controlling language and diffusion models by transporting activations . In The Thirteenth International Conference on Learning Representations, ICLR 2025, Singapore, April 24-28, 2025 , External Links: Link Cited by: §6 .

Roweis and Saul (2000) S. T. Roweis and L. K. Saul Nonlinear dimensionality reduction by locally linear embedding . science 290 ( 5500 ), pp. 2323–2326 . Cited by: 3rd item .

Rubenstein et al. (2017) P. K. Rubenstein, S. Weichwald, S. Bongers, J. M. Mooij, D. Janzing, M. Grosse-Wentrup, and B. Schölkopf Causal consistency of structural equation models . In Proceedings of the 33rd Conference on Uncertainty in Artificial Intelligence (UAI) , Cited by: §6 .

Saphra and Wiegreffe (2024) N. Saphra and S. Wiegreffe Mechanistic? . CoRR abs/2410.09087 . External Links: Link , Document , 2410.09087 Cited by: §6 .

Sarfati et al. (2026) R. Sarfati, E. Bigelow, D. Wurgaft, J. Merullo, A. Geiger, O. Lewis, T. McGrath, and E. S. Lubana The shape of beliefs: geometry, dynamics, and interventions along representation manifolds of language models’ posteriors . External Links: 2602.02315 , Link Cited by: §1 , §6 .

Saxe et al. (2019) A. M. Saxe, J. L. McClelland, and S. Ganguli A mathematical theory of semantic development in deep neural networks . Proceedings of the National Academy of Sciences 116 ( 23 ), pp. 11537–11546 . Cited by: §6 .

Schölkopf et al. (1997) B. Schölkopf, A. Smola, and K. Müller Kernel principal component analysis . In International conference on artificial neural networks , pp. 583–588 . Cited by: 3rd item .

Shai et al. (2026) A. Shai, L. Amdahl-Culleton, C. L. Christensen, H. R. Bigelow, F. E. Rosas, A. B. Boyd, E. A. Alt, K. J. Ray, and P. M. Riechers Transformers learn factored representations . External Links: 2602.02385 , Link Cited by: §6 .

Shai et al. (2024a) A. S. Shai, S. E. Marzen, L. Teixeira, A. G. Oldenziel, and P. M. Riechers Transformers represent belief state geometry in their residual stream . Advances in Neural Information Processing Systems 37 , pp. 75012–75034 . Cited by: §6 .

Shai et al. (2024b) A. S. Shai, S. E. Marzen, L. Teixeira, A. G. Oldenziel, and P. M. Riechers Transformers represent belief state geometry in their residual stream . External Links: 2405.15943 , Link Cited by: §1 .

Shepard (1987) R. N. Shepard Toward a universal law of generalization for psychological science . Science 237 ( 4820 ), pp. 1317–1323 . Cited by: §2.1 .

Smolensky (1986) P. Smolensky Neural and conceptual interpretation of pdp models . In Parallel Distributed Processing: Explorations in the Microstructure, Vol. 2: Psychological and Biological Models , pp. 390–431 . External Links: ISBN 0262631105 Cited by: §1 , §6 .

Song and Zhong (2023) J. Song and Y. Zhong Uncovering hidden geometry in transformers via disentangling position and context . arXiv preprint arXiv:2310.04861 . Cited by: §6 .

Song and Kingma (2021) Y. Song and D. P. Kingma How to train your energy-based models . ArXiv e-print . Cited by: §3.2 .

Spirtes et al. (2000) P. Spirtes, C. Glymour, and R. Scheines Causation, prediction, and search . MIT Press . Cited by: §6 .

Stolfo et al. (2023) A. Stolfo, Y. Belinkov, and M. Sachan A mechanistic interpretation of arithmetic reasoning in language models using causal mediation analysis . In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, EMNLP 2023, Singapore, December 6-10, 2023 , H. Bouamor, J. Pino, and K. Bali (Eds.) , pp. 7035–7052 . External Links: Link , Document Cited by: §6 .

Subramani et al. (2022) N. Subramani, N. Suresh, and M. Peters Extracting latent steering vectors from pretrained language models . In Findings of the Association for Computational Linguistics: ACL 2022 , S. Muresan, P. Nakov, and A. Villavicencio (Eds.) , Dublin, Ireland , pp. 566–581 . External Links: Link , Document Cited by: §1 , §3.1 , §6 .

Sutter et al. (2025) D. Sutter, J. Minder, T. Hofmann, and T. Pimentel The non-linear representation dilemma: is causal abstraction enough for mechanistic interpretability? . External Links: 2507.08802 , Link Cited by: §7 .

Sutton and Barto (2018) R. S. Sutton and A. G. Barto Reinforcement learning: an introduction . 2nd edition , MIT Press . Cited by: Figure 7 , §5 .

Tan et al. (2024) D. Tan, D. Chanin, A. Lynch, B. Paige, D. Kanoulas, A. Garriga-Alonso, and R. Kirk Analysing the generalisation and reliability of steering vectors . Advances in Neural Information Processing Systems 37 , pp. 139179–139212 . Cited by: §1 , §7 .

Team (2025) G. A. Team GEN-0: embodied foundation models that scale with physical interaction . Generalist AI Blog . Note: https://generalistai.com/blog/nov-04-2025-GEN-0 Cited by: §5 .

Tenenbaum and Griffiths (2001) J. B. Tenenbaum and T. L. Griffiths Generalization, similarity, and bayesian inference . Behavioral and brain sciences 24 ( 4 ), pp. 629–640 . Cited by: §2.1 .

Todd et al. (2024) E. Todd, M. L. Li, A. S. Sharma, A. Mueller, B. C. Wallace, and D. Bau Function vectors in large language models . In The Twelfth International Conference on Learning Representations, ICLR 2024, Vienna, Austria, May 7-11, 2024 , External Links: Link Cited by: §6 .

Touvron et al. (2023) H. Touvron, T. Lavril, G. Izacard, X. Martinet, M. Lachaux, T. Lacroix, B. Rozière, N. Goyal, E. Hambro, F. Azhar, et al. Llama: open and efficient foundation language models . arXiv preprint arXiv:2302.13971 . Cited by: §A.2 , §2.2 .

Towers et al. (2024) M. Towers, A. Kwiatkowski, J. Terry, J. U. Balis, G. De Cola, T. Deleu, M. Goulão, A. Kallinteris, M. Krimmel, A. KG, et al. Gymnasium: a standard interface for reinforcement learning environments . arXiv preprint arXiv:2407.17032 . Cited by: §1 .

Turner et al. (2024) A. M. Turner, L. Thiergart, G. Leech, D. Udell, J. J. Vazquez, U. Mini, and M. MacDiarmid Steering language models with activation engineering . External Links: 2308.10248 , Link Cited by: §1 , §6 .

Turner et al. (2023) A. M. Turner, L. Thiergart, D. Udell, G. Leech, U. Mini, and M. MacDiarmid Activation addition: steering language models without optimization . External Links: 2308.10248 Cited by: §3.1 .

Vennemeyer et al. (2025) D. Vennemeyer, P. A. Duong, T. Zhan, and T. Jiang Sycophancy is not one thing: causal separation of sycophantic behaviors in llms . arXiv preprint arXiv:2509.21305 . Cited by: 1st item .

Vig et al. (2020) J. Vig, S. Gehrmann, Y. Belinkov, S. Qian, D. Nevo, Y. Singer, and S. Shieber Investigating gender bias in language models using causal mediation analysis . In Advances in Neural Information Processing Systems , H. Larochelle, M. Ranzato, R. Hadsell, M.F. Balcan, and H. Lin (Eds.) , Vol. 33 , pp. 12388–12401 . External Links: Link Cited by: §3.1 , §6 .

Wang et al. (2023a) K. R. Wang, A. Variengien, A. Conmy, B. Shlegeris, and J. Steinhardt Interpretability in the wild: a circuit for indirect object identification in GPT-2 small . In The Eleventh International Conference on Learning Representations , External Links: Link Cited by: §6 .

Wang et al. (2023b) Z. Wang, L. Gui, J. Negrea, and V. Veitch Concept algebra for score-based conditional model . In ICML 2023 Workshop on Structured Probabilistic Inference { \{ \ \backslash & } \} Generative Modeling , Cited by: §6 .

Wu et al. (2025) Z. Wu, A. Arora, A. Geiger, Z. Wang, J. Huang, D. Jurafsky, C. D. Manning, and C. Potts AxBench: steering llms? even simple baselines outperform sparse autoencoders . External Links: 2501.17148 , Link Cited by: §1 , §7 .

Wurgaft et al. (2025) D. Wurgaft, E. S. Lubana, C. F. Park, H. Tanaka, G. Reddy, and N. D. Goodman In-context learning strategies emerge rationally . External Links: 2506.17859 , Link Cited by: 2nd item .

Yang et al. (2025) Y. Yang, H. Tanaka, and W. Hu Provable low-frequency bias of in-context learning of representations . arXiv preprint arXiv:2507.13540 . Cited by: §4 .

Yocum et al. (2025) J. Yocum, C. Allen, B. Olshausen, and S. Russell Neural manifold geometry encodes feature fields . In NeurIPS 2025 Workshop on Symmetry and Geometry in Neural Representations , Cited by: §2.1 , §6 , §7 .

Zheng et al. (2025) C. Zheng, N. Beltran-Velez, S. Karlekar, C. Shi, A. Nazaret, A. Mallik, A. Feder, and D. M. Blei Model directions, not words: mechanistic topic models using sparse autoencoders . arXiv preprint arXiv:2507.23220 . Cited by: §6 .

Zhou et al. (2025) T. Zhou, D. Fu, M. Soltanolkotabi, R. Jia, and V. Sharan FoNE: precise single-token number embeddings via fourier features . arXiv preprint arXiv:2502.09741 . Cited by: §6 .

## Appendix A Experimental Details for Language Tasks

This Appendix describes the procedures behind the experiments of Sections § 2 , § 3 , and § 4 . The following section (Appendix § B ) will provide details for the mountain-car experiment in § 5 .

### A.1 Tasks and Datasets

#### Natural domain tasks.

We use four natural-domain addition tasks: weekdays and months (cyclic), and letters and ages (sequential). The full templates and entity sets are listed in Table 1 . For each task, we enumerate every (entity, increment) pair whose result lies in the task’s target set, dropping pairs whose result would fall outside it (e.g. letters past Z, or ages outside [ 10,100 ] [10,100] ). The reported activations and output distributions are computed at the answer-token position, and concept centroids are obtained by averaging across all prompts whose ground-truth result is the same value of 𝒵 \mathcal{Z} .

#### In-context learning of representations.

For the multi-dimensional setting of § 4 , we use the in-context learning of representations (ICLR) family of Park et al. (2025b) : arbitrary tokens corresponding to nouns (e.g., ”film”, ”rain”) are assigned to the nodes of a graph, and prompts are random walks on that graph. We study a 5 × 5 5\times 5 grid and a 9 × 9 9\times 9 cylinder, with random walks of 2048 2048 entity tokens. As in Park et al. (2025b) ’s setup, the random walks we sample do not allow backtracking, which we find aids models in learning the underlying structure.

### A.2 Model, Intervention Site, and Output Distribution

We investigate Llama 3.1 8B ( Touvron et al., 2023 ) activations at layer 28 in bfloat16 for all tasks. All interventions are performed on the residual stream at the last-token position. We chose to examine a late layer of the model to ensure that concept geometries are fully computed.

For an input x x , the output distribution 𝒑 ⁡ ( x ) ∈ 𝒴 \bm{p}(x)\in\mathcal{Y} used throughout the paper is constructed as follows: we softmax over the full vocabulary logit distribution and aggregate probability mass over each concept value’s variant token spellings (e.g. the tokens ‘ Monday’ , ‘Monday’ , and ‘monday’ are all summed into the Monday entry). The remaining probability mass on tokens not associated with any concept value is collected into a single ‘other’ bin, yielding a distribution on the open simplex Δ | 𝒵 | \Delta^{|\mathcal{Z}|} over | 𝒵 | + 1 |\mathcal{Z}|+1 classes.

### A.3 Fitting the Activation Manifold ℳ h \mathcal{M}_{h}

To identify the activation manifold ℳ h \mathcal{M}_{h} , we first obtain points in full activation space and transform them into a 64-dimensional subspace obtained via PCA over the activations 𝒉 ⁡ ( x ) \bm{h}(x) across all prompts in the task. The manifold lives entirely in the 64-dimensional PCA subspace; the orthogonal complement is preserved during all subsequent interventions (§ A.6 ).

We compute concept centroids c i c_{i} as the mean of the projected activations across all prompts whose ground-truth result equals the i i -th concept value, and fit a smooth interpolant through them. For the four natural-domain tasks the interpolant is a one-dimensional cubic spline ( Reinsch, 1967 ) : a natural cubic spline (with vanishing second derivatives at the endpoints) for the sequential tasks (letters, ages), and a periodic cubic spline for the cyclic tasks (weekdays, months) so that the curve closes smoothly. For the sequential tasks we use the ground-truth ordinal index of each concept as its intrinsic coordinate. For the cyclic tasks the centroids form a near-circular loop in the top two principal components of the activation subspace, so we instead derive the intrinsic coordinate θ = atan2 ⁡ ( PC 2 , PC 1 ) \theta=\operatorname{atan2}(\mathrm{PC}_{2},\mathrm{PC}_{1}) in an unsupervised manner.

The interpolant for the ICLR tasks is a thin-plate spline (TPS; Duchon (1977) ; Bookstein (1989) ), a multi-dimensional generalisation of the cubic spline which minimizes the bending energy ∫ ‖ ∇ 2 f ‖ 2 \int\|\nabla^{2}f\|^{2} . Thin-plate splines map points in a lower-dimensional intrinsic space to the full ambient space. The TPS parameterisation requires a choice of intrinsic coordinates for the centroids. We use the ground-truth graph coordinates of each node in the ICLR task as intrinsic coordinates. Both the grid and cylinder tasks use the standard TPS kernel r 2 ​ log ⁡ r r^{2}\log r ; for the cylinder, which has both a linear and a periodic dimension, we additionally apply a ghost-point procedure where each control point is duplicated at one period above and below its θ \theta value (and we drop the linear-in- θ \theta polynomial column) to enforce closure across the periodic dimension. In every case the spline interpolates the centroids exactly, so ℳ h \mathcal{M}_{h} passes through every c i c_{i} .

### A.4 Fitting the Behavior Manifold ℳ y \mathcal{M}_{y}

Behavior centroids b i = 𝒑 ¯ i b_{i}=\bar{\bm{p}}_{i} are computed analogously to the activation centroids, by averaging the model’s output distributions across all prompts whose ground-truth result equals the i i -th concept value. Because the probability simplex is not a proper metric space, we map each centroid into Hellinger coordinates via b i ↦ b i b_{i}\mapsto\sqrt{b_{i}} , placing it on the non-negative orthant of the unit ℓ 2 \ell_{2} sphere in ℝ | 𝒵 | + 1 \mathbb{R}^{|\mathcal{Z}|+1} . We then fit the same family of splines used for ℳ h \mathcal{M}_{h} to the Hellinger-embedded centroids: a 1D cubic spline (natural or periodic) for the natural-domain tasks, and a thin-plate spline for the ICLR tasks. Analogous to the activation manifold, the fit passes exactly through every b i \sqrt{b_{i}} and we do not apply a smoothing penalty.

The spline is fit in Euclidean space, but valid b i \sqrt{b_{i}} points lie on a curved sphere. A naive fit to their ambient coordinates would leave the sphere between centroids, and an off-sphere vector does not square to a valid distribution. We therefore fit the spline in the tangent plane of the sphere at a base point b ∗ b_{*} – a flat space that touches the sphere at b ∗ b_{*} – and lift back to the sphere at decode time.

We take b ∗ b_{*} to be the Euclidean mean of { b i } \{\sqrt{b_{i}}\} , re-normalized to unit length; because every b i \sqrt{b_{i}} lies in the non-negative orthant, so does b ∗ b_{*} . The log-map t i = log b ∗ ⁡ ( b i ) t_{i}=\log_{b_{*}}\!(\sqrt{b_{i}}) projects each centroid onto the tangent plane: it returns a vector whose direction points from b ∗ b_{*} along the geodesic to b i \sqrt{b_{i}} and whose length equals that geodesic distance. We fit the spline to the tangent vectors { t i } \{t_{i}\} . To decode at a query coordinate u u , we evaluate the spline to obtain a tangent vector t t and apply the exponential map exp b ∗ ⁡ ( t ) \exp_{b_{*}}(t) , the inverse of the log-map: it walks distance ‖ t ‖ \|t\| along the geodesic on the sphere starting at b ∗ b_{*} in direction t t . The result is unit-norm by construction, so ℳ y \mathcal{M}_{y} stays on the sphere everywhere, and because exp b ∗ ∘ log b ∗ \exp_{b_{*}}\!\circ\log_{b_{*}} is the identity on the sphere, the decoded curve passes through every b i \sqrt{b_{i}} exactly.

### A.5 Geodesic Distances and the Isometry Test

To compute the geodesic distance d ℳ h ​ ( c i , c j ) d_{\mathcal{M}_{h}}(c_{i},c_{j}) between two concept centroids, we discretize the line segment between 𝒔 − 1 ​ ( c i ) \bm{s}^{-1}(c_{i}) and 𝒔 − 1 ​ ( c j ) \bm{s}^{-1}(c_{j}) in intrinsic coordinates into 150 equal sub-intervals, decode each waypoint through 𝒔 \bm{s} , and accumulate consecutive ambient distances. Each waypoint therefore lies on ℳ h \mathcal{M}_{h} by construction, and the resulting arc length is measured in the 64-dimensional PCA subspace in which the manifold lives, with the Euclidean norm as the ambient norm. For the behavior manifold ℳ y \mathcal{M}_{y} we follow the same procedure but compute distances in the full sqrt-probability ambient space ℝ | 𝒵 | + 1 \mathbb{R}^{|\mathcal{Z}|+1} rather than a PCA-reduced subspace, using the Hellinger distance d H ​ ( p , q ) = 1 2 ​ ‖ p − q ‖ 2 d_{H}(p,q)=\tfrac{1}{\sqrt{2}}\|\sqrt{p}-\sqrt{q}\|_{2} directly on the sqrt-embedded waypoints.

The isometry score reported in § 2 is the Pearson correlation between the upper-triangular entries of the resulting pairwise distance matrices. We augment the W W centroid vertices with K K interior points sampled at equally spaced fractions of the u-space geodesic between each centroid pair, decoded onto the manifold via 𝒔 \bm{s} so that every vertex lives on ℳ h \mathcal{M}_{h} or ℳ y \mathcal{M}_{y} . We choose K K so that the vertex set is dense enough to probe the geometry between centroids: K = 4 K=4 for weekdays ( W = 7 W=7 ); K = 1 K=1 for months ( W = 12 W=12 ), alphabet ( W = 24 W=24 , letters C ​ – ​ Z C\text{--}Z ), and the grid 5 × 5 5{\times}5 task ( W = 25 W=25 ); and K = 0 K=0 for age ( W = 91 W=91 , ages 10 ​ – ​ 100 10\text{--}100 ) and the cylinder 9 × 9 9{\times}9 task ( W = 81 W=81 ), whose centroids are already dense. We then correlate every off-diagonal pair in the full vertex set except those whose two vertices lie on a common centroid-pair geodesic, since those distances are sub-arcs of the same geodesic and would inflate the correlation by construction. To visualise the resulting pairwise structure, we embed each distance matrix into three dimensions via classical multidimensional scaling, as shown in Figs. 2 , 3 , and 6 .

### A.6 Steering Interventions

For each pair of concept values ( z a , z b ) (z_{a},z_{b}) , we steer the model from the centroid c a c_{a} to the centroid c b c_{b} via a path of K = 50 K=50 waypoints. We use a fixed set of base prompts sampled randomly from the task’s input distribution (the prompts’ ground-truth results vary, and the same set is reused across all pairs): 16 16 prompts for the natural-domain tasks and 5 5 for the ICLR tasks. At each waypoint 𝝅 ⁡ ( t ) \bm{\pi}(t) , we intervene at the last-token residual-stream activation of the target layer and continue the forward pass to obtain 𝒑 𝒉 ← 𝝅 ⁡ ( t ) ​ ( x ) \bm{p}_{\bm{h}\leftarrow\bm{\pi}(t)}(x) . Every reported behavioral trajectory is the pointwise mean over the base prompts. We use up to 50 randomly-sampled pairs per task. On the smaller-domain tasks where W ⋅ ( W − 1 ) < 50 W\cdot(W-1)<50 , all pairs are used.

The two steering strategies differ both in how the waypoints 𝝅 ⁡ ( t ) \bm{\pi}(t) are constructed and in what the intervention replaces (Eqs. 1 , 2 ). For manifold steering, c a , c b c_{a},c_{b} live in intrinsic coordinates and the path is the manifold geodesic between them; at each waypoint we decode 𝝅 ⁡ ( t ) \bm{\pi}(t) onto ℳ h \mathcal{M}_{h} in the 64-dimensional PCA subspace, lift it back to the residual-stream basis via the PCA inverse, and combine it with the prompt’s unchanged off-subspace residual – so the steered activation differs from the base only in its top-64 PCA components. For linear steering, c a , c b c_{a},c_{b} are the raw activation centroids in the full residual stream, the path is the straight line between them, and the entire residual-stream activation is replaced by 𝝅 ⁡ ( t ) \bm{\pi}(t) at each step.

### A.7 Naturalness Metric

The cumulative output energy E BC E_{\text{BC}} of § 3.2 (Eq. 3 ) is computed as the sum of the Bhattacharyya distances D BC ( 𝜸 ( t ) , ℳ y ) = − log ∑ i γ i ​ ( t ) ​ q i ​ ( t ) D_{\text{BC}}(\bm{\gamma}(t),\mathcal{M}_{y})=-\log\sum_{i}\sqrt{\gamma_{i}(t)\,q_{i}(t)} between the induced output distribution at each of the K = 50 K=50 waypoints along steering paths and the closest point q ⁡ ( t ) q(t) on ℳ y \mathcal{M}_{y} . We use the Bhattacharyya distance because ℳ y \mathcal{M}_{y} is fit in Hellinger geometry and the two are tightly related, D BC = − log ⁡ ( 1 − d H 2 ) D_{\text{BC}}=-\log(1-d_{H}^{2}) , so D BC D_{\text{BC}} stays inside the same geometry the manifold was constructed in. For each of the up to 50 sampled centroid pairs, we average the per-waypoint cumulative sum across the base prompts to obtain one scalar per pair, and report the mean and standard error of these per-pair scalars.

### A.8 Pullback Optimization

The pullback procedure of § 3.3 consists of two stages. First, we fix a behavioral target by evaluating the spline geodesic on ℳ y \mathcal{M}_{y} between the two behavior centroids b a b_{a} and b b b_{b} at K = 20 K=20 uniform fractions, yielding a sequence of target distributions 𝒑 ^ t ∈ ℳ y \hat{\bm{p}}_{t}\in\mathcal{M}_{y} . Second, we optimize an activation-space path π h pullback \pi_{h}^{\text{pullback}} which, when used to intervene at each waypoint, induces a behavioral trajectory matching 𝒑 ^ 0 : K \hat{\bm{p}}_{0:K} .

#### Path Parameterization.

We parameterise π h pullback \pi_{h}^{\text{pullback}} as a one-dimensional natural cubic spline through 10 control vectors at uniform t t -positions, all of which are optimisation variables. The path is evaluated at the same K = 20 K=20 uniform fractions used to generate the target. Each control vector is restricted to the first 32 PCA components of the 64-dimensional subspace; the remaining 32 components, together with the orthogonal residual, are held at the base prompt’s activation values during the intervention. We note that the linear and manifold-steering paths used as comparisons span the full 64-dimensional subspace, so the pullback optimization is operating within a strictly smaller search space.

#### Loss and optimizer.

The loss at each waypoint t t is the squared Hellinger distance d H 2 ​ ( 𝒑 𝒉 ← 𝝅 ⁡ ( t ) ​ ( x n ) , 𝒑 ^ t ) d_{H}^{2}(\bm{p}_{\bm{h}\leftarrow\bm{\pi}(t)}(x_{n}),\hat{\bm{p}}_{t}) between the induced output distribution and the target, averaged over 16 base prompts { x n } \{x_{n}\} sampled freshly per pair, each conditioned on ground-truth z a z_{a} (in contrast to the steering setup of § A.6 , where a fixed unfiltered set is reused across pairs). We minimize the sum of these per-waypoint losses with L-BFGS using strong-Wolfe line search, running 50 outer steps with up to 5 inner iterations each. The optimization is initialized by linearly interpolating between the two centroids in the 32-dimensional subspace and then sampling the resulting line at the 10 control- t t positions. We stop early when the relative change in loss between two consecutive outer steps falls below 10 − 3 10^{-3} . We disable the path-norm regularizer for weekdays; on the other three natural-domain tasks we add a small regularizer that penalizes deviations of ‖ 𝝅 ⁡ ( t ) ‖ \|\bm{\pi}(t)\| from the linear interpolation between the endpoint centroid norms | c a | , | c b | |c_{a}|,|c_{b}| . We use weight 10 − 3 10^{-3} for age and 5 × 10 − 4 5\times 10^{-4} for months and alphabet. This discourages the optimizer from drifting into a high-norm shortcut basin.

### A.9 Pullback Recovery R 2 R^{2}

To compare the optimised pullback path π h pullback \pi_{h}^{\text{pullback}} to the manifold-steering path π h ∗ \pi_{h}^{*} along ℳ h \mathcal{M}_{h} , we project both into the SVD basis of π h ∗ \pi_{h}^{*} that captures at least 99 % 99\% of π h ∗ \pi_{h}^{*} ’s variance. In this basis we define the residual at each pullback waypoint as its orthogonal closest-point distance to π h ∗ \pi_{h}^{*} , and report R 2 = 1 − ∑ t ‖ π h pullback ​ ( t ) − proj π h ∗ ​ π h pullback ​ ( t ) ‖ 2 ∑ t ‖ π h pullback ​ ( t ) − π ¯ h pullback ‖ 2 . R^{2}\;=\;1-\frac{\sum_{t}\|\pi_{h}^{\text{pullback}}(t)-\mathrm{proj}_{\pi_{h}^{*}}\pi_{h}^{\text{pullback}}(t)\|^{2}}{\sum_{t}\|\pi_{h}^{\text{pullback}}(t)-\bar{\pi}_{h}^{\text{pullback}}\|^{2}}. The linear baseline used in the same comparison is the straight chord between c a c_{a} and c b c_{b} in the 64-dimensional PCA subspace—not the linear-steering trajectory after intervention. As in § A.7 , the values reported in § 3.3 are mean ± \pm standard error across the per-pair scalars, with p p -values from paired t t -tests against the linear baseline.

## Appendix B Experimental Details for the Vision Task

This section contains additional details on the experiment from § 5 .

### B.1 Mountain Car.

#### Data collection.

To recover the encoder’s position manifold we harvest activations on 100 100 rollouts collected in MountainCar-v0 (max 200 200 steps per episode) under a mixed stochastic policy chosen to give broad coverage of the position-velocity state space. At the start of each episode we sample one of two policies: with probability 0.7 0.7 , a noisy momentum policy that pushes in the direction of the current velocity but, at each step, replaces the action with a uniform random action with probability 0.4 0.4 ; with probability 0.3 0.3 , an oscillating square-wave policy that alternates between full-left and full-right thrust on a fixed period sampled uniformly from { 5 , … , 25 } \{5,\dots,25\} steps. We then pass each rendered frame through the trained encoder, label the resulting activation with the underlying ground-truth position, and fit the manifold to this collection of position-labelled activations.

#### Manifold fitting.

To parameterize the activation manifold, ℳ \mathcal{M} , we partition the position range into B = 100 B=100 bins, compute the mean encoder output per occupied bin, and fit a smoothing spline γ ℳ : [ 0 , 1 ] → ℳ \gamma_{\mathcal{M}}\colon[0,1]\to\mathcal{M} through these means (one univariate spline per coordinate, weighted by the square root of bin counts to regularize sparse regions). We additionally verify via linear probing that the encoder representations z t z_{t} encode the ground-truth physics: a Ridge regression probe recovers position with R 2 ≈ 0.95 R^{2}\approx 0.95 and velocity with R 2 ≈ 0.90 R^{2}\approx 0.90 . A three-component PCA of the encoder outputs reveals the spline γ ℳ \gamma_{\mathcal{M}} as a curve that closely tracks the data manifold, while the chord ℓ \ell between the same endpoints cuts through its interior.

To parameterize the behavior manifold, ℳ y \mathcal{M}_{y} , discretize 𝒵 \mathcal{Z} into B B bins with centers { μ b } b = 1 B ⊂ ℝ n \{\mu_{b}\}_{b=1}^{B}\subset\mathbb{R}^{n} obtained by evaluating the activation-manifold spline at B B evenly spaced positions, μ b = γ ℳ ​ ( p b ) \mu_{b}=\gamma_{\mathcal{M}}(p_{b}) . The mapping to behavior is F ⁡ ( z ) = softmax ​ ( − ‖ z − μ b ‖ 2 τ ) b = 1 B ∈ Δ B − 1 , F(z)\;=\;\mathrm{softmax}\!\left(-\frac{\|z-\mu_{b}\|_{2}}{\tau}\right)_{b=1}^{B}\;\in\;\Delta^{B-1}, (10) with temperature τ = 0.5 \tau=0.5 . F F is a smooth, deterministic map from activations to position distributions. We use B = 128 B=128 , which makes F F ’s Jacobian full column-rank, ensuring the inverse problem has a locally unique solution. For each bin i i , the natural centroid on the behavior manifold is the model’s average output distribution conditioned on samples in that bin: b i = 𝔼 ⁡ [ F ⁡ ( z ) ∣ bin ⁡ ( z ) = i ] ∈ Δ B − 1 . b_{i}\;=\;\mathbb{E}\!\left[F(z)\mid\mathrm{bin}(z)=i\right]\;\in\;\Delta^{B-1}. (11) Because the bin grid is dense relative to the data manifold’s intrinsic dimension, b i b_{i} is well-defined for all bins. We embed each b i b_{i} in Hellinger coordinates h i = b i h_{i}=\sqrt{b_{i}} on the unit sphere of ℝ B \mathbb{R}^{B} and fit a 1D smoothing spline γ ℳ y : 𝒵 → ℝ B \gamma_{\mathcal{M}_{y}}\colon\mathcal{Z}\to\mathbb{R}^{B} through { h i } \{h_{i}\} parameterized by position. This is the behavior manifold ℳ y \mathcal{M}_{y} .

## Appendix C Additional Results

### C.1 In-Context Learning of Representations.

In addition to results provided in the main text, we test a 9 × 9 9\times 9 cylinder in the ICLR domains, and find that despite the added complexity of a periodic dimension and substantially more graph nodes, when Llama 3.1 8B is provided sufficient context (2048 tokens in this case), it reaches above 80 % 80\% neighborhood accuracy (probability mass on valid neighbors). We fit a manifold and steer along this domain, finding that the result of factored control generalizes beyond the graph domain.

### C.2 Manifold steering allows manipulation of uncertainty without loss of structure.

To examine multi-dimensional concepts in known domains, we partition weekday addition centroids by addition value ( 1 1 – 5 5 , 6 6 – 10 10 , 11 11 – 15 15 , 16 16 – 20 20 ), revealing concentric circles along a second manifold dimension forming a cylinder-like structure (Fig. 11 ). Manifold steering along the circular dimension maintains ordered weekday transitions with increasing entropy per group. This suggests manifold geometry can serve as a handle for calibrating model confidence in a controlled fashion. The experiment was conducted with Llama 3.1 3.1 70 70 B layer 70 70 .

### C.3 Mountain Car

#### Structural Correspondence between ℳ h \mathcal{M}_{h} and ℳ y \mathcal{M}_{y} .

If ℳ h \mathcal{M}_{h} encodes the model’s predictive distributions over 𝒵 \mathcal{Z} , then ℳ h \mathcal{M}_{h} and ℳ y \mathcal{M}_{y} should be approximately isometric—distances along one manifold should correlate with distances along the other. We test this by sampling W = 50 W=50 anchor positions inside the shared parameter range and computing pairwise arc lengths along each manifold: d ℳ ​ ( p i , p j ) = ∫ p i p j ‖ γ ℳ h ′ ​ ( p ) ‖ 2 ​ 𝑑 p , d ℳ y ​ ( p i , p j ) = 1 2 ​ ∫ p i p j ‖ γ ℳ y ′ ​ ( p ) ‖ 2 ​ 𝑑 p , d_{\mathcal{M}}(p_{i},p_{j})=\int_{p_{i}}^{p_{j}}\|\gamma_{\mathcal{M}_{h}}^{\prime}(p)\|_{2}\,dp,\quad d_{\mathcal{M}_{y}}(p_{i},p_{j})=\frac{1}{\sqrt{2}}\int_{p_{i}}^{p_{j}}\|\gamma_{\mathcal{M}_{y}}^{\prime}(p)\|_{2}\,dp, (12) where the 1 / 2 1/\sqrt{2} on the behavior side converts the Euclidean integral in Hellinger ambient space to Hellinger units. The Pearson correlation between { d ℳ h ​ ( p i , p j ) } \{d_{\mathcal{M}_{h}}(p_{i},p_{j})\} and { d ℳ y ​ ( p i , p j ) } \{d_{\mathcal{M}_{y}}(p_{i},p_{j})\} over all ( 50 2 ) = 1225 \binom{50}{2}=1225 pairs is r = 0.996 r=\mathbf{0.996} ; the chord distances used by linear steering correlate far less ( r = 0.06 r=0.06 between activation chord and behavior arc length), since chords cut across the encoder loop and are structurally divorced from the encoded conceptual geometry.

#### Pullback: Behavior space steering.

Having established the bottom-up direction in Fig. 7 , i.e., paths along ℳ h \mathcal{M}_{h} produce behavior trajectories on ℳ y \mathcal{M}_{y} , We now test the top-down direction: starting from a behaviorally-natural trajectory in ℳ y \mathcal{M}_{y} , do we naturally recover an activation path that traces ℳ h \mathcal{M}_{h} ? For each endpoint pair ( p a , p b ) (p_{a},p_{b}) we construct the conformal behavior target γ ^ α \hat{\gamma}_{\alpha} via the procedure of § 3.3 (geodesic on the simplex under cost c ⁡ ( p ) = exp ⁡ ( α ⋅ d H ​ ( p , ℳ y ) ) c(p)=\exp(\alpha\cdot d_{H}(p,\mathcal{M}_{y})) ). We then optimize an activation path π α = ( v 0 , … , v K ) \pi_{\alpha}=(v_{0},\dots,v_{K}) in ℝ n \mathbb{R}^{n} to minimize L ⁡ ( π ) = ∑ t = 0 K ‖ F ⁡ ( v t ) − γ ^ α ​ ( t ) ‖ 2 2 . L(\pi)\;=\;\sum_{t=0}^{K}\bigl\|\sqrt{F(v_{t})}-\sqrt{\hat{\gamma}_{\alpha}(t)}\bigr\|_{2}^{2}. (13) Following the language-model setup, all K + 1 K+1 waypoints (including endpoints) are free parameters, initialized at the linear chord and optimized jointly via L-BFGS with strong-Wolfe line search. We use K = 30 K=30 waypoints and run independent optimizations for each of 30 endpoint pairs.

Across all 30 endpoint pairs, the pullback paths π α \pi_{\alpha} closely trace ℳ h \mathcal{M}_{h} (Fig. 12 ): The mean Euclidean distance from π \pi to ℳ h \mathcal{M}_{h} , averaged over waypoints and pairs: linear ​ chord : 2.22 , geometric ⁡ ( ℳ h ) : 0.20 , pullback : 0.29 . \mathrm{linear\ chord}\!:\;\;2.22,\qquad\mathrm{geometric}\;(\mathcal{M}_{h})\!:\;\;0.20,\qquad\mathrm{pullback}\!:\;\;0.29. The pullback path is at 95.4 % \mathbf{95.4\%} of the chord-to-geometric recovery and dominates the chord baseline on 30 / 30 30/30 pairs. The aggregate degradation is concentrated on pairs with one endpoint at the extreme wall position ( p ≈ − 1.2 p\approx-1.2 ), where the encoder geometry has tighter curvature; on the remaining ∼ \sim 20 pairs, π ∞ \pi_{\infty} is essentially indistinguishable from ℳ h \mathcal{M}_{h} itself. The α \alpha -sweep traces the same family of trajectories observed in the language-model experiments: at α = 0 \alpha=0 the conformal target is the unrestricted Hellinger geodesic on the simplex, and the recovered π 0 \pi_{0} leaves ℳ h \mathcal{M}_{h} in order to match this off-manifold target; as α \alpha grows the target is pushed onto ℳ y \mathcal{M}_{y} and the recovered π α \pi_{\alpha} correspondingly tracks ℳ h \mathcal{M}_{h} .

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
