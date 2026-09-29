##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Equilibrium Reasoners: Learning Attractors Enables Scalable Reasoning

###### Abstract

Scaling test-time compute by iteratively updating a latent state has emerged as a powerful paradigm for reasoning. Yet, the internal mechanisms that enable these iterative models to generalize beyond memorized patterns remain fundamentally unclear. We hypothesize that such generalizable reasoning arises from learning task-conditioned attractors : a latent dynamical system where stable fixed points correspond to valid solutions.

We formalize this process by introducing Equilibrium Reasoners (EqR) . EqR enables test-time scaling without relying on external verifiers or task-specific priors. Instead, our models scale internal dynamics along two axes: depth by running more iterations and breadth by aggregating stochastic trajectories from multiple initializations. Empirically, performance gains from scaling test-time compute are tightly coupled with better convergence to attractors.

This attractor perspective allows neural networks to adaptively allocate test-time compute based on task difficulty. While simple cases converge within 1 to 5 iteration steps, the hardest cases benefit from massive test-time scaling. By unrolling up to an equivalent of 40,000 layers, this scalable latent reasoning boosts accuracy from 2.6% for feedforward models to over 99% on Sudoku-Extreme. We hope our attractor perspective sheds light on scalable reasoning.

###### Keywords:

CMU https://github.com/locuslab/EqR

## 1 Introduction

Scaling is a defining pattern of modern AI systems: accuracy improves with training data, model capacity, and, increasingly, test-time compute . Across settings ranging from search-based game agents ( Silver et al., 2018 ) to chain-of-thought reasoning ( Wei et al., 2022 ) , systems often spend additional inference compute to improve performance.

Yet the opposite can be true, where more test-time compute may yield diminishing returns or even worse performance ( Pipis et al., 2025 ; Ghosal et al., 2025 ; Fu et al., 2026 ; Chen et al., 2025 ) . This suggests that improving reasoning via test-time scaling requires specific internal mechanisms. It raises a basic question: what internal mechanisms enable scalable and generalizable reasoning?

In this work, we study this problem on controlled, structured reasoning benchmarks, where memorization can be separated from generalization. Recent iterative reasoning models, such as HRM and TRM ( Wang et al., 2025 ; Jolicoeur-Martineau, 2025 ) , repeatedly apply a learned module to update latent states and achieve strong results on algorithmic reasoning tasks such as Sudoku and Maze. This repeated update naturally defines a learned dynamical system in latent space for reasoning.

We argue that test-time scaling is effective when a model’s internal attractor landscape aligns with the task-metric landscape: trajectories that achieve stronger convergence should also decode to lower-error answers. Under this view, training then seeks to shape the attractor landscape into a differentiable surrogate aligned with the task metric. This amortizes intrinsically complex reasoning into a finite-capacity network, while leaving adaptive computation to inference. Consequently, inference acts as an adaptive search: scaling up test-time compute reliably drives the latent state toward favorable attractors. In this aligned regime, finding stable fixed points (attractors) is implicitly solving the task, suggesting that stronger convergence yields better performance. The learned dynamics effectively close the capacity-complexity gap, enabling scalable reasoning that generalizes beyond memorization, even with limited data, model capacity, and training budgets.

We view these models as learned fixed-point dynamical systems (akin to a DEQ-style perspective ( Bai et al., 2019 ) ) whose trajectories evolve in latent space toward attractors. This extends the usual fixed-point view from asking whether a state converges to asking what attractor landscape the learned dynamics induce: which attractors exist, whether they are reachable from plausible initializations, and whether they align with the task metric. Under this lens, correct solutions correspond to favorable attractors and failures correspond to spurious attractors; scaling works when additional iterations or restarts guide trajectories into basins of favorable attractors.

Building on this view, we first perform a systematic study of training-time and inference-time design choices for iterative reasoning on controlled tasks, starting from the transition from feedforward computation to weight-tied iteration and then analyzing the training and inference choices that shape the learned attractor landscape. Across Sudoku-Extreme and Maze-Unique, we quantify convergence via the fixed-point residual ∥ f θ ​ ( 𝐳 , 𝐱 ) − 𝐳 ∥ \lVert f_{\theta}(\mathbf{z};\mathbf{x})-\mathbf{z}\rVert and show that lower residual tightly tracks lower prediction error (Fig. 1 ), identifying the key factors that activate generalizable reasoning.

This framing suggests concrete, task-agnostic diagnostics: fixed-point convergence (a.k.a. ∥ f θ ​ ( 𝐳 , 𝐱 ) − 𝐳 ∥ \lVert f_{\theta}(\mathbf{z};\mathbf{x})-\mathbf{z}\rVert ) and how it co-varies with prediction error. It also predicts a characteristic depth–breadth interaction: breadth (more restarts) becomes effective only after sufficient depth enables trajectories to meaningfully explore and settle into attractors, a pattern we observe in Fig. 3 .

Guided by these diagnostics, we introduce two lightweight training interventions, randomized state initialization and path stochasticity via noise injection, to make favorable attractors easier to reach. The resulting dynamics can be scaled along two explicit inference axes: depth ( D D ), the per-trajectory number of unrolled steps, and breadth ( B B ), the number of stochastic trajectories from independent initializations. With two-axis scaled inference and convergence-based selection, EqR substantially outperforms prior iterative reasoning models on these controlled benchmarks, reaching 99.8 % 99.8\% exact accuracy on Sudoku and 93.0 % 93.0\% on Maze 1 1 1 For simplicity, we refer to Sudoku-Extreme as Sudoku and Maze-Unique as Maze throughout the paper. . We hope these analyses help advance a mechanistic understanding of iterative latent reasoning models and how their internal dynamics support scalable reasoning.

## 2 Background and Problem Formulation

We study iterative reasoning models that carry out multi-step computation through iterative updates of a latent state. Given an input 𝐱 ∈ 𝒳 \mathbf{x}\in\mathcal{X} , the model maintains a state 𝐳 k ∈ ℝ n \mathbf{z}_{k}\in\mathbb{R}^{n} and applies a parameterized update operator 𝐳 k + 1 = f θ ​ ( 𝐳 k , 𝐱 ) , \mathbf{z}_{k+1}=f_{\theta}(\mathbf{z}_{k};\mathbf{x}), (1) where k k denotes the iteration index, and θ \theta denotes the model parameters. This update-rule perspective is common in neural networks with iterative computation ( Bai et al., 2019 ; Dehghani et al., 2019 ; Zhu et al., 2025 ; Wang et al., 2025 ; Jolicoeur-Martineau, 2025 ; Hao et al., 2025 ) . These approaches share a common view of test-time scaling through additional applications of the same learned update rule. Starting from an initial state 𝐳 0 ∼ μ 0 ( ⋅ ∣ 𝐱 ) \mathbf{z}_{0}\sim\mu_{0}(\cdot\mid\mathbf{x}) , the model runs K K updates and decodes the final state into a prediction 𝐲 ^ K \hat{\mathbf{y}}_{K} . The task supplies a metric comparing 𝐲 ^ K \hat{\mathbf{y}}_{K} with the target 𝐲 \mathbf{y} . In this work, we focus on iterative reasoning models with fixed-size latent states. Hierarchical Reasoning Models ( Wang et al., 2025 ) and Tiny Recursive Models ( Jolicoeur-Martineau, 2025 ) implement multi-step reasoning by iteratively updating high- and low-level latent states in a nested-loop schedule. For our analysis, the essential commonality is a weight-tied latent dynamical system whose extra computation unfolds in state space.

## 3 From Feedforward Predictors to Iterative Reasoners

We study how a feedforward model can be turned into an iterative model ( Wang et al., 2025 ; Jolicoeur-Martineau, 2025 ) with feedback loops under controlled data and compute, and use this path to analyze the key design choices for training strong iterative models. We ablate the main design axes used by prior works as follows.

#### Weight-tied structure.

The weight-tied design reuses parameters across model layers, replacing additional distinct layers with repeated iterations of the same update block.

#### Truncated gradients.

Full backpropagation through long weight-tied trajectories is costly and multiplies many recurrent Jacobians, which can make the backward dynamics poorly conditioned and the gradient signal unstable. Truncated gradients with detached carry keep the length of forward trajectory but cut the backward graph at segment boundaries. Therefore, each update is optimized through a local trajectory window.

#### Hierarchical iterations.

We then compare single-stream iteration against hierarchical iterations, where two latent states are updated at different frequencies. This separates the effect of weight-tied iteration from the additional two-timescale structure used in HRM/TRM-style models.

#### Supervision placement and optimization schedule.

After choosing the gradient window, one must decide where losses are placed and when parameters are updated. Given a K K -step trajectory { 𝐳 k } k = 1 K \{\mathbf{z}_{k}\}_{k=1}^{K} from iterative models, we compare three schedules: 1) Vanilla , which computes the loss only after the final iteration and updates the parameters once per full trajectory; 2) Trajectory Supervision , which places losses at multiple iterations but accumulates them into a single update at the end of the trajectory; and 3) Segmented Online Training , which splits the trajectory into segments, supervises the end of each segment, and takes an optimizer step immediately. The next segment starts from the current latent state with detached carry, but under the updated parameters. Thus, SOT changes not only where supervision is applied, but also the optimizer time scale: the model is updated along the evolving trajectory rather than only after the full rollout has completed. From an optimization viewpoint, this can be seen as an alternating approximation to an attractor-learning problem: latent updates seek a reachable low-residual state under the current operator, while parameter updates reshape the operator so that these reachable states decode to correct solutions. These schedules can differ substantially in optimization fidelity, training stability, and efficiency. We include detailed discussions in Appendix A.2 .

#### Adaptive computation time (ACT).

We also study adaptive computation via a learned halting mechanism ( Graves, 2017 ) . Let q ^ k = f ϕ ​ ( 𝐳 k ) \hat{q}_{k}=f_{\phi}(\mathbf{z}_{k}) be a halting score and τ = min ⁡ { k ≤ K : q ^ k > δ } , \tau=\min\{k\leq K:\hat{q}_{k}>\delta\}, with τ = K \tau=K if no halt is triggered. We compare different variants, including fixed-depth iteration, oracle halting, and learned halting with an ACT head. The main distinction is whether the halting signal is only predicted or is actually used to allocate variable compute. In the latter case, solved examples leave the batch early while unresolved examples receive further refinement, so ACT acts as a difficulty-aware compute allocation mechanism.

#### Overview.

Together, these axes define the construction path studied in Sec. 6.1 : 1) weight-tied structure converts distinct layers into repeated application of a shared update block; 2) hierarchical iterations test whether two-timescale latent updates add benefits beyond single-stream iteration; 3) truncated gradients stabilize optimization through long weight-tied trajectories by keeping the backward graph local while also reducing memory and compute costs; 4) segmented online training changes where supervision and optimizer updates enter the trajectory; and 5) adaptive computation reallocates iteration budget across examples by difficulty. The main text reports the compact construction path, and we defer full details, results and diagnostics to Appendix A.2 .

## 4 Iterative Models as Attractor Dynamics

This section develops the conceptual framework used by the rest of the paper. We first relax exact fixed-point convergence into an attractor view of iterative inference, then use the resulting landscape modes to explain when depth and breadth scaling should help and what training must shape.

### 4.1 From Fixed-Point Convergence to Attractors

Prior iterative reasoning work already points toward a convergence interpretation: HRM describes its nested latent updates through hierarchical convergence , while TRM cautions that literal fixed-point convergence is too strong because latent residuals can remain nonzero even as they decrease during training ( Wang et al., 2025 ; Jolicoeur-Martineau, 2025 ) . By contrast, we argue that iterative models do converge in a weaker attractor sense: repeated application of the update operator often reduces the residual ‖ f θ ​ ( 𝐳 , 𝐱 ) − 𝐳 ‖ \|f_{\theta}(\mathbf{z};\mathbf{x})-\mathbf{z}\| and improves performance, as illustrated in Fig. 1 . The key point is that this behavior need not be exact fixed-point convergence. Under finite computation, a trajectory may approach a fixed point, settle into a stable region, or enter a bounded recurrent set; when nearby states are drawn toward such a set under repeated updates, it acts as an attractor. We therefore use attractor to describe stable long-run outcomes of the learned dynamics, generalizing the equilibrium perspective used in Deep Equilibrium Models ( Bai et al., 2019 ) .

This attractor view keeps the core convergence claim without requiring convergence to a single exact fixed point: test-time compute is useful when trajectories move toward favorable attractors and lower-residual states within a well-structured internal landscape . A favorable basin suffices.

In this view, the learned trajectory is part of the prediction mechanism: when successive states become more task-consistent as their residuals fall, additional iterations can refine the answer instead of simply adding compute. Feedforward models do not induce such refinement trajectories; in our controlled comparison, they generalize substantially worse than iterative alternatives in Tab. 1 .

Formally, for a data example ( 𝐱 , 𝐲 ) ∼ 𝒟 (\mathbf{x},\mathbf{y})\sim\mathcal{D} , inference induces a trajectory { 𝐳 k } k ≥ 0 \{\mathbf{z}_{k}\}_{k\geq 0} by iterating an update operator f θ ​ ( ⋅ , 𝐱 ) f_{\theta}(\cdot;\mathbf{x}) from the initialization 𝐳 0 ∼ μ 0 ( ⋅ ∣ 𝐱 ) \mathbf{z}_{0}\sim\mu_{0}(\cdot\mid\mathbf{x}) . We write 𝒵 θ ∗ ​ ( 𝐱 ) \mathcal{Z}^{*}_{\theta}(\mathbf{x}) for the stable long-run outcomes of these dynamics (e.g., fixed points or small recurrent sets).

The collection 𝒵 θ ∗ ​ ( 𝐱 ) \mathcal{Z}^{*}_{\theta}(\mathbf{x}) is the model’s attractor landscape . This landscape matters through two axes: task alignment and reachability. Task alignment asks whether the reached attractors decode to correct solutions rather than spurious ones. Reachability asks which attractor a trajectory reaches, and how reliably it does so under different initializations or perturbations. We summarize reachability using breadth and depth : broad attractors are easy to reach from many initial states, while deep attractors are stable once reached.

These two geometric properties map directly to two test-time scaling levers. Depth scaling increases the number of forward iterations D D , giving a single trajectory more opportunities to refine within the basin it has entered. Breadth scaling runs B B independent restarts from initial states { 𝐳 0 ( i ) } i = 1 B \{\mathbf{z}_{0}^{(i)}\}_{i=1}^{B} and aggregates their outputs, increasing coverage over possible basins. We use the number of function evaluations, NFE = D ⋅ B \mathrm{NFE}=D\cdot B , as a compact way to describe inference budgets throughout the scaling experiments.

### 4.2 Landscape Modes and Scaling Implications

The attractor landscape view becomes useful when it predicts how test-time compute should be allocated. Fig. 6 combines task alignment, reachability, and the two scaling levers into four qualitative regimes. Each regime identifies the dominant failure source and therefore predicts whether depth scaling, breadth scaling, or neither should help. 2 2 2 Task error is defined at the sequence level: any token mismatch counts as incorrect. Token-level losses therefore induce a qualitatively different and much noisier landscape than the task-level metric in this setting, so we visualize only the latter.

(a) No correct attractor: all reachable attractors decode to poor task outcomes. The failure is task misalignment rather than insufficient compute, so residual reduction does not translate into task improvement and neither depth nor breadth scaling helps.

(b) Correct and spurious attractors coexist: a correct attractor exists, but inference may converge to competing low-residual, high-error attractors. The failure is basin selection, so breadth scaling is most useful because additional restarts increase the chance of entering the correct basin; depth helps only after the trajectory enters that basin.

(c) Correct but hard to reach: the correct attractor is nearly unique but has a narrow or weak basin. The failure is reachability, so breadth increases the chance of entering the basin and depth can help weakly attracted trajectories settle once they do; gains are limited by basin mass and stability.

(d) Well-aligned landscape: the correct attractor is broad and stable, so residual decay is tightly coupled with task-error reduction. Depth reliably refines trajectories toward the solution, while breadth provides additional coverage but is no longer the main bottleneck.

Thus, depth and breadth are complementary: depth refines a trajectory after it reaches a useful basin, while breadth increases basin coverage, consistent with the depth–breadth interaction in Fig. 3 . Test-time scaling succeeds when correct attractors are both aligned and reachable, motivating the training interventions in Sec. 5 .

## 5 Shaping Attractor Landscapes

Sec. 4.2 shows that test-time scaling is effective when the learned landscape contains correct attractors and inference reaches them reliably. Attractor landscape shaping is therefore the guiding training principle: we want the iterative dynamics to (i) admit correct solutions as stable attractors and (ii) make their basins easy to reach from diverse initial states as test-time compute increases. We now describe how to move generic iterative models toward Equilibrium Reasoners .

We introduce two task-agnostic interventions that do not require external verifiers or hand-crafted search heuristics: (1) randomized state initialization ( RI ), which samples initial latent states rather than model weights to improve coverage under breadth scaling and reduce train–test mismatch, and (2) noise injection (NI), which implements path stochasticity by perturbing each iteration step to mitigate premature trapping and broaden exploration as the iteration budget grows. Algorithm 1 shows the instantiation of the procedure.

### 5.1 Randomized State Initialization

HRM and TRM ( Wang et al., 2025 ; Jolicoeur-Martineau, 2025 ) typically train with a fixed initial state 𝐳 0 \mathbf{z}_{0} shared across trajectories. In contrast, we sample 𝐳 0 ∼ μ 0 ( ⋅ ∣ 𝐱 ) \mathbf{z}_{0}\sim\mu_{0}(\cdot\mid\mathbf{x}) independently for each trajectory. This matches training to breadth scaling at test time, where multiple draws of 𝐳 0 \mathbf{z}_{0} probe different basins. The benefit is twofold: it broadens the regions shaped during training and encourages stable predictions across restarts.

(i) Coverage of correct attractors. With a fixed initializer, learning is constrained to a small state-space neighborhood and tends to shape trajectories only locally. This limits exposure to alternative basins. Randomizing 𝐳 0 \mathbf{z}_{0} expands the explored region during training and increases the likelihood that correct attractors are reachable at inference.

(ii) Stability and path independence. Randomizing 𝐳 0 \mathbf{z}_{0} also promotes consistency across restarts: the same ( 𝐱 , 𝐲 ) (\mathbf{x},\mathbf{y}) is observed under multiple initial states, so divergent predictions are penalized. This encourages path independence ( Anil et al., 2022 ) by aligning predictions across trajectories.

By default, we use a Gaussian μ 0 ( ⋅ ∣ 𝐱 ) \mu_{0}(\cdot\mid\mathbf{x}) with covariance σ 0 ​ I \sigma_{0}I . Appendix A.3 and Appendix A.3 study learnable initializers and initialization scale; we use a fixed Gaussian initializer in the main experiments to isolate stochastic coverage from learned-prior design.

### 5.2 Path Stochasticity via Noise Injection

Random initializations reduce the train–test gap induced by breadth scaling; path noise regularizes how trajectories evolve. This targets modes (b) and (c) in Sec. 4.2 : mild noise can help trajectories enter better basins and avoid premature convergence to incorrect stable states. Thus, RI and NI act on complementary parts of the trajectory: RI broadens where rollouts start, while NI smooths the local dynamics encountered along each rollout.

We augment the iteration with damping and additive noise: 𝐳 k + 1 = 𝐳 k + ( 1 − λ ) ​ r θ ​ ( 𝐳 k , 𝐱 ) + β ​ ε k , \mathbf{z}_{k+1}=\mathbf{z}_{k}+(1-\lambda)\,r_{\theta}(\mathbf{z}_{k};\mathbf{x})+\beta\,\varepsilon_{k}, (2) where ε k ∼ 𝒩 ⁡ ( 0 , I ) \varepsilon_{k}\sim\mathcal{N}(0,I) . Here λ ∈ [ 0 , 1 ) \lambda\in[0,1) controls damping and β ≥ 0 \beta\geq 0 controls the noise magnitude. In other words, we inject isotropic Gaussian noise at each step and use β \beta to control its strength. This preserves the same update architecture while allowing controlled local exploration around the deterministic trajectory. We consider variants with different β \beta and a learnable noise variant in Appendix A.4 . Empirically, mild damping ( λ = 0.05 \lambda=0.05 ) combined with small path noise ( β = 0.01 \beta=0.01 ) performs best among the tested variants. At test time, one can increase β \beta under breadth scaling to foster exploration, analogous to temperature scaling.

## 6 Experiments

We organize the experiments around two questions. First, we ask what ingredients turn a feedforward model into a strong iterative model. Second, based on the iterative backbone, we test whether landscape-shaping interventions improve accuracy and make depth and breadth scaling reliable.

#### Task representation.

Each puzzle is serialized into a token sequence. The input sequence encodes the unsolved puzzle, and the target sequence encodes its solution, as illustrated in Fig. 5 . The sequence length is fixed during inference for a given task, since each task uses a fixed grid size, but it differs across tasks, e.g., Sudoku ( 9 × 9 ) (9\times 9) versus Maze ( 30 × 30 ) (30\times 30) . See more details in Appendix C .

#### Evaluation metrics.

By default, i.e., without breadth scaling, we report exact accuracy , which equals 1 only if all tokens are correct and 0 otherwise. Under breadth scaling with B B independent restarts, we consider three evaluation metrics in this paper: (1) Averaged exact accuracy , the mean exact-match accuracy over the B B restarts ( B = 1 B{=}1 reduces to the standard single run); (2) Top-1 convergence accuracy , which selects the restart with the smallest average residual over the final few iterations ( L = 3 L{=}3 ) and checks whether its prediction is correct; and (3) Majority-vote accuracy , which predicts by majority vote across restarts. Formal definitions are given in Appendix D.3 .

#### Baselines.

For Sec. 6.1 , we begin with a feedforward baseline and then introduce iterative components incrementally. For Sec. 6.2 , we also report HRM ( Wang et al., 2025 ) and TRM ( Jolicoeur-Martineau, 2025 ) baselines without our training interventions or inference extrapolation. For the TRM comparison, the backbone is matched at the block level: we use TRM’s task-specific settings for Sudoku and Maze, and each block has a task-dependent token mixer followed by an MLP. The mixer is an MLP-mixer on Sudoku and self-attention on Maze. This makes the comparison about the training and inference changes on a comparable iterative backbone, instead of a new block architecture. The feedforward baselines use 42 blocks on Sudoku and 15 blocks on Maze; the corresponding weight-tied variants use 2 blocks with 21 iterations and 1 block with 15 iterations, respectively. See Appendix D.1 for full details.

### 6.1 From Feedforward Models to Iterative Models

We study the gain from turning a feedforward model into an iterative one in this section. Tab. 2 starts from a vanilla feedforward predictor and adds weight-tying, long unrolls, hierarchy, and ACT.

Tab. 2 shows a monotonic construction path. Compared with the feedforward baseline under the same budgets, weight-tied models show significant improvement (from 2.6% to 32.6%); when we further scale up the depth with the supervision and update schedule needed to train long unrolls, the performance improves to 74.7% 3 3 3 Scaling the depth of weight-tied models requires a well-designed supervision and optimization schedule. We include the details in Appendix A.2 . . Hierarchical recurrence provides a smaller additional gain in this setting, ACT training allows difficulty-aware allocation of training-time compute per sample, and further improves inference performance to 84.8%. The ACT row has lower training accuracy because the model learns to stop early to prevent overfitting on easier examples while allocating more computation to learn harder ones, which gives the best evaluation accuracy in the construction path. Full ablations, update-schedule variants, ACT diagnostics, FLOPs accounting, and supporting figures are in Appendix A.2 .

#### Summary and takeaway.

Overall, the evidence supports a specific training principle: Weight-tied models create iterative capacity, but realizing that capacity at larger depth requires well-designed training strategies to shape the dynamics so that late-iteration states stay aligned with the task objective under finite stability and memory constraints.

### 6.2 From Iterative Models to Equilibrium Reasoners

Training with the proposed interventions (Sec. 5 ) improves both accuracy and the reliability of test-time scaling, consistent with shaping a more favorable attractor landscape. Across tasks, we observe three consistent effects: (i) higher baseline accuracy without additional test-time compute, (ii) a higher scaling ceiling as inference uses more depth, with further gains when depth is combined with breadth, and (iii) stronger empirical alignment between residual convergence and task correctness, which makes convergence-based selection effective under breadth scaling.

In Tab. 3 , baseline denotes the final TRM-style iterative model from Tab. 2 , before applying randomized state initialization or noise injection. We compare our methods against baselines on Sudoku and Maze in Tab. 3 and Tab. 4 .

Landscape shaping improves accuracy and stability without extra inference compute.

At the training-time compute budget, models trained with randomized state initialization and noise injection consistently outperform the same backbone trained without these interventions. In Tab. 3 , the full RI+NI training improves Sudoku from 84.8 84.8 to 86.4 86.4 and Maze from 44.9 44.9 to 82.2 82.2 , with RI alone already raising Maze accuracy to 68.6 68.6 . These gains hold on both training and evaluation splits, suggesting that correct attractors become reachable for a larger fraction of inputs within the same compute budget (Sec. 4.2 ). The same interventions also improve inference stability, as reflected by stronger path independence (Tab. 12 , Appendix A.4 ).

Shaped landscapes raise the test-time scaling ceiling.

After applying the landscape-shaping interventions, increasing depth first improves within-trajectory refinement, and combining the deeper rollout with breadth scaling further improves coverage across restarts. Tab. 4 makes this effect explicit: at B = 1 B{=}1 , increasing the depth from D = 16 D{=}16 to D = 64 D{=}64 raises EqR from 86.4 86.4 to 93.0 93.0 on Sudoku and from 82.2 82.2 to 88.9 88.9 on Maze. Combining this deeper rollout with breadth scaling ( B = 128 B{=}128 ) further increases accuracy to 99.8 99.8 on Sudoku and 93.0 93.0 on Maze. This pattern suggests that landscape shaping supports both forms of test-time scaling: deeper rollouts improve a single trajectory, while broader restarts cover more attractor basins. This is consistent with the landscape modes in Fig. 6 : interventions primarily mitigate modes (b) and (c) by enlarging correct basins and reducing spurious trapping.

Convergence becomes a reliable selection signal after landscape shaping.

Majority voting and convergence-based selection are both breadth-scaling strategies, but they exploit different signals. Majority voting aggregates decoded outputs, whereas convergence-based selection picks the run with the strongest convergence signal, e.g., the smallest average residual over the final few iterations. After learning a favorable landscape, convergence aligns better with task correctness, so selecting the Top-1 Converged run becomes a reliable and compute-efficient selection rule. We visualize this trend on Sudoku in Fig. 8 : as breadth increases, Top-1 Converged achieves comparable or higher expected accuracy than majority vote for the same number of restarts, with our training interventions.

This selection rule is not universally valid: for the baseline TRM, residual reduction can indicate convergence to spurious attractors, so Top-1 Converged can underperform majority voting. It becomes reliable only after shaping the landscape so residual convergence tracks task error. This distinction is important: convergence is useful here not as a task-agnostic certificate, but as a learned proxy whose reliability depends on the attractor landscape.

#### Summary.

Overall, the results suggest that the proposed interventions improve baseline accuracy and stability, raise the test-time scaling ceiling across depth and breadth, and strengthen convergence–correctness alignment. As a result, convergence becomes a more reliable selection signal under breadth scaling, offering a more efficient alternative to majority voting once the landscape is well shaped. Additional experiments in Appendix A.5 show that the same recipe also improves Mini-ARC performance and transfers to a Transformer backbone.

### 6.3 Adaptive Computation for Budget-Elastic Inference

So far, our scaling experiments have applied the same test-time budget to every task instance, regardless of difficulty. However, applying a massive, static compute budget universally is highly inefficient. As our landscape analysis suggests, instance difficulty is highly heterogeneous: simple problems quickly fall into favorable attractors, whereas complex ones require extensive iterative refinement. To systematically optimize the compute-accuracy Pareto frontier, we resort to elastic budget inference guided by a learned halting policy ( Jolicoeur-Martineau, 2025 ) . By equipping EqR with a learned halting head, the model dynamically tracks its internal state and terminates computation early upon converging to an attractor, so additional compute is allocated mainly to instances that remain unresolved.

We use a fixed-size inference queue for batching: halted samples are replaced immediately to keep utilization high while preserving per-sample stopping. This allows ACT to convert sample-wise dynamic halting into an actual reduction in the average number of function evaluations (Avg. NFE) at inference time.

Tab. 5 shows that ACT substantially reduces Avg. NFE with only minor accuracy changes: at D = 1024 D{=}1024 , Avg. NFE drops from 1024.0 1024.0 to 58.7 58.7 ( 17.4 × 17.4\times fewer evaluations) while accuracy changes from 96.1 96.1 to 95.3 95.3 ; under breadth scaling ( 64,128 ) (64,128) , Avg. NFE drops from 8192.0 8192.0 to 1400.6 1400.6 ( 5.8 × 5.8\times fewer evaluations) while accuracy changes from 97.9 97.9 to 97.4 97.4 . This suggests most instances terminate early, while a small fraction require long runs. Fig. 7 shows the same effect at the accuracy–compute frontier: EqR+ACT reaches the matched accuracy target with 11.34 × 11.34\times fewer NFEs than the baseline.

Together with earlier scaling results, this spans both ends of compute: large-budget scaling and budget-elastic efficiency. The halting objective’s training-side effect was analyzed in Tab. 8 ( 8(e) ); here we focus on ACT’s inference-side compute–accuracy trade-off.

## 7 Related Work

#### Iterative weight-tied models.

Iterative models apply an update operator repeatedly to refine a latent state, with representative works including weight-tied Transformers such as the Universal Transformer and related variants ( Dehghani et al., 2019 ; Graves, 2017 ; Chowdhury and Caragea, 2025 ; Heo et al., 2025 ) . Deep Equilibrium Models ( Bai et al., 2019 ) take this idea to the implicit limit by defining representations as fixed points, followed by extensive work on convergence diagnostics, stability, and more efficient training methods ( Bai et al., 2021 ; Geng et al., 2021a ; Geng et al., 2021b ; Gu et al., 2020 ; Anil et al., 2022 ; Fung et al., 2022 ) and practical tooling such as TorchDEQ ( Geng and Kolter, 2023 ) .

Path-independent equilibrium models make this connection more explicit: when iterative inference converges to the same fixed point regardless of the trajectory or initialization, additional test-time steps can reliably refine toward a well-defined representation ( Anil et al., 2022 ) . Our setting relaxes the requirement of a globally unique fixed point: we instead ask whether finite rollouts and restarts concentrate around solution-aligned attractors, making path independence both a diagnostic and a property encouraged by our intervention.

Recent weight-tied models further show that iterative latent computation is becoming an active scaling direction across language and visual reasoning ( Geiping et al., 2025 ; Zhu et al., 2025 ; Prairie et al., 2026 ; Song et al., 2026 ; Bae et al., 2025 ; Shu et al., 2026 ) . In parallel, the HRM series of works shows that such iterative models have strong performance over complex and structured reasoning tasks ( Wang et al., 2025 ; Jolicoeur-Martineau, 2025 ; Gao et al., 2025 ) . These finite iterative computations still induce a latent dynamical system; we study whether training can shape their trajectories toward solution-aligned attractors, enabling scalable gains from additional test-time compute.

#### Compute allocation in weight-tied models.

For weight-tied models, test-time compute allocation asks how many iterations to spend, where to spend them, and whether the same budget should be used uniformly or adapted across inputs. One line of work studies iteration or recurrent-depth scaling, showing that applying a weight-tied module more times at test time can improve performance beyond the training regime ( Schwarzschild et al., 2021 ; Geiping et al., 2025 ; Prairie et al., 2026 ; Shu et al., 2026 ) . A second line focuses on adaptive allocation, using mechanisms such as token-wise depth ( Song et al., 2026 ) , learned recurrence mixtures ( Bae et al., 2025 ) , adaptive halting ( Graves, 2017 ) , or elastic-depth budget conditioning ( Jeddi et al., 2026 ) to spend different amounts of computation across tokens, examples, or compute budgets. Recent compute-allocation diagnostics ( Moosa et al., 2026 ) and selective latent iterations on hard tokens ( Fu et al., 2025 ) further ask whether adaptive policies allocate compute to genuinely hard tokens rather than merely reducing average depth. These model-specific mechanisms connect to a broader inference-time scaling lesson: additional computation is most useful when allocated to informative candidates, states, or search branches rather than spent uniformly ( Snell et al., 2025 ; Yang et al., 2025 ; Ghosal et al., 2025 ) . In our work, we use depth scaling and breadth scaling to verify that scaling far beyond the training regime can substantially improve performance. We then close the efficiency side by learning a halting module following Graves (2017) , which cuts inference cost by allocating fewer iterations to easier inputs while preserving most of the scaling gains.

## 8 Conclusion

In this work, we present an attractor-based perspective on test-time scaling in iterative reasoning models. Trajectory diagnostics show that depth and breadth help when learned attractors are aligned with the task metric and reachable from diverse initial states. Guided by this view, randomized initialization and path noise reshape the latent landscape, improving the coverage and stability of correct attractors on Sudoku and Maze and making additional computation more reliable. The broader implication is that iterative latent reasoning models should be evaluated not only by final accuracy, but also by whether their internal dynamics make correct solutions stable, reachable, and selectable. We hope these diagnostics and interventions provide a step toward a more mechanistic understanding of scalable iterative reasoning.

Appendix

A Additional Results, Analyses, and Findings . A

A.1 Attractor Formulation and Residual Diagnostics . A.1

A.2 Training-Dynamics Ablations and Diagnostics . A.2

A.3 Additional Experiments on Randomized State Initialization . A.3

A.4 Additional Experiments on Path Stochasticity . A.4

A.5 Generalization Beyond the Main Setting . A.5

A.6 Seed Stability Diagnostics . A.6

B Qualitative Study . B

C Dataset Details and Task Definitions . C

C.1 Dataset and Benchmark Specifications . C.1

C.2 Datasets and Task Definitions Shape Attractor Landscapes . C.2

D Method and Experimental Details . D

D.1 Architecture and Hyperparameters . D.1

D.2 Learning-Rate Control for Feedforward Baselines . D.2

D.3 Evaluation Metrics . D.3

D.4 Compute Accounting for Iterative Inference . D.4

E Extended Related Work and Discussion . E

## References

Anil et al. (2022) C. Anil, A. Pokle, K. Liang, J. Treutlein, Y. Wu, S. Bai, Z. Kolter, and R. Grosse Path independent equilibrium models can better exploit test-time computation . In Advances in Neural Information Processing Systems , Vol. 35 . Cited by: Appendix E , §5.1 , §7 , §7 .

Bae et al. (2025) S. Bae, Y. Kim, R. Bayat, S. Kim, J. Ha, T. Schuster, A. Fisch, H. Harutyunyan, Z. Ji, A. Courville, and S. Yun Mixture-of-recursions: learning dynamic recursive depths for adaptive token-level computation . In Advances in Neural Information Processing Systems , Cited by: §7 , §7 .

Bai et al. (2019) S. Bai, J. Z. Kolter, and V. Koltun Deep equilibrium models . In Advances in Neural Information Processing Systems , Vol. 32 . Cited by: §A.1 , Appendix E , §1 , §2 , §4.1 , §7 .

Bai et al. (2021) S. Bai, V. Koltun, and J. Z. Kolter Stabilizing equilibrium models by jacobian regularization . In Proceedings of the 38th International Conference on Machine Learning , Proceedings of Machine Learning Research , Vol. 139 , pp. 554–565 . Cited by: §A.1 , §7 .

Blayney et al. (2026) H. Blayney, A. Arroyo, J. Obando-Ceron, P. S. Castro, A. Courville, M. M. Bronstein, and X. Dong A mechanistic analysis of looped reasoning language models . External Links: 2604.11791 Cited by: Appendix E .

Chen et al. (2025) H. Chen, Y. Lei, D. Zhang, B. Ke, D. Zhu, X. Chen, Y. Lu, Z. Huang, S. Feng, J. He, Y. Sun, H. Wu, and H. Wang MatryoshkaThinking: recursive test-time scaling enables efficient reasoning . External Links: 2510.10293 Cited by: §1 .

Chowdhury and Caragea (2025) J. R. Chowdhury and C. Caragea Investigating recurrent transformers with dynamic halt . External Links: 2402.00976 Cited by: §7 .

Chu et al. (2026) Y. Chu, M. Shao, Y. Liu, B. Hao, Y. Lin, J. Wang, and R. Wang SPOT: span-level pause-of-thought for efficient and interpretable latent reasoning in large language models . External Links: 2603.06222 Cited by: Appendix E .

Dehghani et al. (2019) M. Dehghani, S. Gouws, O. Vinyals, J. Uszkoreit, and Ł. Kaiser Universal transformers . In International Conference on Learning Representations , Cited by: §A.1 , §2 , §7 .

Everett et al. (2024) K. E. Everett, L. Xiao, M. Wortsman, A. A. Alemi, R. Novak, P. J. Liu, I. Gur, J. Sohl-Dickstein, L. P. Kaelbling, J. Lee, and J. Pennington Scaling exponents across parameterizations and optimizers . In Forty-first International Conference on Machine Learning , Cited by: Table 17 .

Foret et al. (2021) P. Foret, A. Kleiner, H. Mobahi, and B. Neyshabur Sharpness-aware minimization for efficiently improving generalization . In International Conference on Learning Representations , Cited by: Appendix E .

Fu et al. (2025) T. Fu, Y. You, Z. Chen, G. Dai, H. Yang, and Y. Wang Think-at-hard: selective latent iterations to improve reasoning language models . External Links: 2511.08577 Cited by: §7 .

Fu et al. (2026) Y. Fu, X. Wang, H. Zhang, Y. Tian, and J. Zhao Deep think with confidence . In International Conference on Learning Representations , Cited by: §1 .

Fung et al. (2022) S. W. Fung, H. Heaton, Q. Li, D. McKenzie, S. Osher, and W. Yin JFB: jacobian-free backpropagation for implicit networks . In Proceedings of the AAAI Conference on Artificial Intelligence , Vol. 36 , pp. 6648–6656 . External Links: Document Cited by: §A.1 , Appendix E , §7 .

Gao et al. (2025) Z. Gao, L. Chen, Y. Xiao, H. Xing, R. Tao, H. Luo, J. Zhou, and B. Dai Universal reasoning model . External Links: 2512.14693 Cited by: Appendix E , Table 1 , §7 .

Geiping et al. (2025) J. Geiping, S. McLeish, N. Jain, J. Kirchenbauer, S. Singh, B. R. Bartoldson, B. Kailkhura, A. Bhatele, and T. Goldstein Scaling up test-time compute with latent reasoning: a recurrent depth approach . In Advances in Neural Information Processing Systems , Cited by: §A.1 , Appendix E , §7 , §7 .

Geng et al. (2021a) Z. Geng, M. Guo, H. Chen, X. Li, K. Wei, and Z. Lin Is attention better than matrix decomposition? . In International Conference on Learning Representations , Cited by: §A.1 , Appendix E , §7 .

Geng and Kolter (2023) Z. Geng and J. Z. Kolter TorchDEQ: a library for deep equilibrium models . External Links: 2310.18605 Cited by: §7 .

Geng et al. (2021b) Z. Geng, X. Zhang, S. Bai, Y. Wang, and Z. Lin On training implicit models . In Advances in Neural Information Processing Systems , Vol. 34 , pp. 24247–24260 . Cited by: §A.1 , Appendix E , §7 .

Ghosal et al. (2025) S. S. Ghosal, S. Chakraborty, A. Reddy, Y. Lu, M. Wang, D. Manocha, F. Huang, M. Ghavamzadeh, and A. S. Bedi Does thinking more always help? mirage of test-time scaling in reasoning models . In Advances in Neural Information Processing Systems , Cited by: §1 , §7 .

Giannou et al. (2023) A. Giannou, S. Rajput, J. Sohn, K. Lee, J. D. Lee, and D. Papailiopoulos Looped transformers as programmable computers . In Proceedings of the 40th International Conference on Machine Learning , Proceedings of Machine Learning Research , Vol. 202 , pp. 11398–11442 . Cited by: Appendix E .

Goyal et al. (2024) S. Goyal, Z. Ji, A. S. Rawat, A. K. Menon, S. Kumar, and V. Nagarajan Think before you speak: training language models with pause tokens . In International Conference on Learning Representations , Cited by: Appendix E .

Graves (2017) A. Graves Adaptive computation time for recurrent neural networks . External Links: 1603.08983 Cited by: §3 , §7 , §7 .

Gu et al. (2020) F. Gu, H. Chang, W. Zhu, S. Sojoudi, and L. E. Ghaoui Implicit graph neural networks . In Advances in Neural Information Processing Systems , Vol. 33 , pp. 11984–11995 . Cited by: §A.1 , Appendix E , §7 .

Guo et al. (2024) X. Guo, J. Liu, M. Cui, J. Li, H. Yang, and D. Huang InitNO: boosting text-to-image diffusion models via initial noise optimization . In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition , pp. 9380–9389 . Cited by: §A.3 .

Hao et al. (2025) S. Hao, S. Sukhbaatar, D. Su, X. Li, Z. Hu, J. Weston, and Y. Tian Training large language models to reason in a continuous latent space . In Conference on Language Modeling , Cited by: Appendix E , §2 .

Heo et al. (2025) J. Heo, E. Fozilov, H. Song, and T. Kim RingFormer: rethinking recurrent transformer with adaptive level signals . In Findings of the Association for Computational Linguistics: EMNLP 2025 , pp. 21675–21686 . External Links: Document Cited by: §7 .

Hochreiter and Schmidhuber (1997) S. Hochreiter and J. Schmidhuber Flat Minima . Neural Computation 9 ( 1 ), pp. 1–42 . External Links: Document Cited by: Appendix E .

Huang (2026) B. Huang Loop-Model FLOPs and memory in an ablation chain . Note: Blog post External Links: Link Cited by: §A.2 , Table 9 .

Jeddi et al. (2026) A. Jeddi, M. Ciccone, and B. Taati LoopFormer: elastic-depth looped transformers for latent reasoning via shortcut modulation . In International Conference on Learning Representations , Cited by: §7 .

Jolicoeur-Martineau (2025) A. Jolicoeur-Martineau Less is more: recursive reasoning with tiny networks . External Links: 2510.04871 Cited by: Appendix E , Table 1 , §1 , §2 , §3 , §4.1 , §5.1 , §6 , §6.3 , §7 .

Kim et al. (2022) S. Kim, P. Phunyaphibarn, D. Ahn, and S. Kim Playgrounds for abstraction and reasoning . In NeurIPS 2022 Workshop on Neuro Causal and Symbolic AI (nCSI) , Cited by: §A.5 .

Kingma and Ba (2015) D. P. Kingma and J. Ba Adam: a method for stochastic optimization . In International Conference on Learning Representations , Cited by: Table 17 .

Kirin (2026) J. Kirin Relational preference encoding in looped transformer internal states . External Links: 2604.09870 Cited by: Appendix E .

Kohli et al. (2026) H. Kohli, S. Parthasarathy, H. Sun, and Y. Yao Loop, think, & generalize: implicit reasoning in recurrent-depth transformers . External Links: 2604.07822 Cited by: Appendix E .

Labovich (2026) A. Labovich Stability and generalization in looped transformers . External Links: 2604.15259 Cited by: Appendix E .

Lehnert et al. (2024) L. Lehnert, S. Sukhbaatar, D. Su, Q. Zheng, P. Mcvay, M. Rabbat, and Y. Tian Beyond a*: better planning with transformers via search dynamics bootstrapping . In Conference on Language Modeling , Cited by: §C.1 , §C.2 .

Liu et al. (2026) Y. Liu, S. Kangaslahti, Z. Liu, and J. Gore Inverse depth scaling from most layers being similar . External Links: 2602.05970 Cited by: Appendix E .

Lu et al. (2025) W. Lu, Y. Yang, K. Lee, Y. Li, and E. Liu Latent chain-of-thought? decoding the depth-recurrent transformer . External Links: 2507.02199 Cited by: Appendix E .

Merrill and Sabharwal (2024) W. Merrill and A. Sabharwal The expressive power of transformers with chain of thought . In International Conference on Learning Representations , Cited by: Appendix E .

Moosa et al. (2026) I. M. Moosa, S. Lohit, Y. Wang, M. Chatterjee, and W. Yin Understanding dynamic compute allocation in recurrent transformers . External Links: 2602.08864 Cited by: §7 .

Pappone et al. (2025) F. Pappone, D. Crisostomi, and E. Rodolà Two-scale latent dynamics for recurrent-depth transformers . External Links: 2509.23314 Cited by: Appendix E .

Pipis et al. (2025) C. Pipis, S. Garg, V. Kontonis, V. Shrivastava, A. Krishnamurthy, and D. Papailiopoulos Wait, wait, wait… why do reasoning models loop? . External Links: 2512.12895 Cited by: §1 .

Prairie et al. (2026) H. Prairie, Z. Novack, T. Berg-Kirkpatrick, and D. Y. Fu Parcae: scaling laws for stable looped language models . External Links: 2604.12946 Cited by: Appendix E , §7 , §7 .

Ren and Liu (2026) Z. Ren and Z. Liu Are your reasoning models reasoning or guessing? a mechanistic analysis of hierarchical reasoning models . External Links: 2601.10679 Cited by: Appendix E .

Saunshi et al. (2025) N. Saunshi, N. Dikkala, Z. Li, S. Kumar, and S. J. Reddi Reasoning with latent thoughts: on the power of looped transformers . In International Conference on Learning Representations , Cited by: Appendix E .

Schwarzschild et al. (2021) A. Schwarzschild, E. Borgnia, A. Gupta, F. Huang, U. Vishkin, M. Goldblum, and T. Goldstein Can you learn an algorithm? generalizing from easy to hard problems with recurrent networks . External Links: 2106.04537 Cited by: §7 .

Schwethelm et al. (2026) K. Schwethelm, D. Rueckert, and G. Kaissis How much is one recurrence worth? iso-depth scaling laws for looped language models . External Links: 2604.21106 Cited by: Appendix E .

Shu et al. (2026) W. Shu, X. Qiu, R. Zhu, H. H. Chen, Y. Liu, and H. Yang LoopViT: scaling visual arc with looped transformers . External Links: 2602.02156 Cited by: Appendix E , §7 , §7 .

Silver et al. (2018) D. Silver, T. Hubert, J. Schrittwieser, I. Antonoglou, M. Lai, A. Guez, M. Lanctot, L. Sifre, D. Kumaran, T. Graepel, T. Lillicrap, K. Simonyan, and D. Hassabis A general reinforcement learning algorithm that masters chess, shogi, and go through self-play . Science 362 ( 6419 ), pp. 1140–1144 . External Links: Document Cited by: §1 .

Snell et al. (2025) C. Snell, J. Lee, K. Xu, and A. Kumar Scaling llm test-time compute optimally can be more effective than scaling model parameters . In International Conference on Learning Representations , Cited by: §7 .

Song et al. (2026) S. Song, H. Li, Z. Wang, B. Zeng, F. Song, Y. Wang, Z. J. Xu, Z. He, and Z. Lin AdaPonderLM: gated pondering language models with token-wise adaptive depth . External Links: 2603.01914 Cited by: §7 , §7 .

Wang et al. (2025) G. Wang, J. Li, Y. Sun, X. Chen, C. Liu, Y. Wu, M. Lu, S. Song, and Y. A. Yadkori Hierarchical reasoning model . External Links: 2506.21734 Cited by: §C.1 , Table 16 , Table 16 , Appendix E , Table 1 , §1 , §2 , §3 , §4.1 , §5.1 , §6 , §7 .

Wei et al. (2022) J. Wei, X. Wang, D. Schuurmans, M. Bosma, B. Ichter, F. Xia, E. Chi, Q. Le, and D. Zhou Chain-of-thought prompting elicits reasoning in large language models . In Advances in Neural Information Processing Systems , Vol. 35 . Cited by: §1 .

Wei et al. (2026) X. Wei, X. Liu, Y. Zang, X. Dong, Y. Cao, J. Wang, X. Qiu, and D. Lin SIM-cot: supervised implicit chain-of-thought . In International Conference on Learning Representations , Cited by: Appendix E .

Wu et al. (2024) T. Wu, C. Si, Y. Jiang, Z. Huang, and Z. Liu FreeInit: bridging initialization gap in video diffusion models . In Computer Vision – ECCV 2024 , pp. 378–394 . External Links: Document Cited by: §A.3 .

Xu and Sato (2025) K. Xu and I. Sato On expressive power of looped transformers: theoretical analysis and enhancement via timestep encoding . In Proceedings of the 42nd International Conference on Machine Learning , Cited by: Appendix E .

Xu et al. (2025a) Y. Xu, X. Guo, Z. Zeng, and C. Miao SoftCoT++: test-time scaling with soft chain-of-thought reasoning . External Links: 2505.11484 Cited by: Appendix E .

Xu et al. (2025b) Y. Xu, X. Guo, Z. Zeng, and C. Miao SoftCoT: soft chain-of-thought for efficient reasoning with llms . In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics , pp. 23336–23351 . External Links: Document Cited by: Appendix E .

Yang et al. (2024) L. Yang, K. Lee, R. Nowak, and D. Papailiopoulos Looped transformers are better at learning learning algorithms . In International Conference on Learning Representations , Cited by: Appendix E .

Yang et al. (2025) W. Yang, S. Ma, Y. Lin, and F. Wei Towards thinking-optimal scaling of test-time compute for llm reasoning . In Advances in Neural Information Processing Systems , Cited by: §7 .

You et al. (2025) R. You, Y. Li, M. Liu, W. Wang, L. Nie, and W. Li Parallel test-time scaling for latent reasoning models . External Links: 2510.07745 Cited by: Appendix E .

Zeng et al. (2025) B. Zeng, H. Li, S. Song, Y. Wang, Z. Wang, Z. He, X. Wang, and Z. Lin PonderLM-2: pretraining llm with latent thoughts in continuous space . External Links: 2509.23184 Cited by: Appendix E .

Zeng et al. (2026) B. Zeng, S. Song, S. Huang, Y. Wang, H. Li, Z. He, X. Wang, Z. Li, and Z. Lin PonderLM: pretraining language models to ponder in continuous space . In International Conference on Learning Representations , Cited by: Appendix E .

Zhou et al. (2025) Z. Zhou, S. Shao, L. Bai, S. Zhang, Z. Xu, B. Han, and Z. Xie Golden noise for diffusion models: a learning framework . External Links: 2411.09502 Cited by: §A.3 .

Zhu et al. (2025) R. Zhu, Z. Wang, K. Hua, T. Zhang, Z. Li, H. Que, B. Wei, Z. Wen, F. Yin, H. Xing, et al. Scaling latent reasoning via looped language models . External Links: 2510.25741 Cited by: Appendix E , §2 , §7 .

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .

## Appendix A Additional Results, Analyses, and Findings

This section extends the findings in the main text through additional analyses and experiments, including a residual-diagnostic formulation, training-dynamics ablations from feedforward models to weight-tied iterative models, ablations of training interventions on initialization and path stochasticity, generalization beyond the main setting, and seed stability.

### A.1 Attractor Formulation and Residual Diagnostics

This subsection isolates the attractor formulation and residual diagnostics used to interpret the training ablations below.

A useful idealization of attractor learning follows the DEQ view of an input-conditioned equilibrium layer ( Bai et al., 2019 ) : min θ , 𝐳 ⁡ ℓ θ ​ ( 𝐳 , 𝐱 , 𝐲 ) s.t. R θ ​ ( 𝐳 , 𝐱 ) = 𝐳 − f θ ​ ( 𝐳 , 𝐱 ) = 0 . \min_{\theta,\mathbf{z}}\;\ell_{\theta}(\mathbf{z};\mathbf{x},\mathbf{y})\qquad\text{s.t.}\qquad R_{\theta}(\mathbf{z};\mathbf{x})=\mathbf{z}-f_{\theta}(\mathbf{z};\mathbf{x})=0. (3) The constraint says that the supervised latent state should be a fixed point of the current update operator. This differs from the Universal Transformer formulation ( Dehghani et al., 2019 ) , where input token embeddings initialize the recurrent state and the shared block is iterated over that state. Here the update is written as an input-conditioned solver f θ ​ ( 𝐳 , 𝐱 ) f_{\theta}(\mathbf{z};\mathbf{x}) : the problem data 𝐱 \mathbf{x} remains available as an external condition at every solver step, as in DEQs and recent recurrent-depth models ( Geiping et al., 2025 ) . In our setting, however, the relevant object is not a globally unique fixed point, but a reachable attractor or low-residual state reached from an initialization 𝐳 0 \mathbf{z}_{0} by iterative computation. We can therefore write the practical surrogate as a bilevel optimization problem: min θ \displaystyle\min_{\theta} 𝔼 ( 𝐱 , 𝐲 ) , 𝐳 0 ​ [ ℓ θ ​ ( 𝐳 θ ⋆ ​ ( 𝐱 , 𝐳 0 ) , 𝐱 , 𝐲 ) ] \displaystyle\mathbb{E}_{(\mathbf{x},\mathbf{y}),\mathbf{z}_{0}}\bigl[\ell_{\theta}(\mathbf{z}^{\star}_{\theta}(\mathbf{x},\mathbf{z}_{0});\mathbf{x},\mathbf{y})\bigr] (4) s . t . \displaystyle\mathrm{s.t.} 𝐳 ⋆ θ ( 𝐱 , 𝐳 0 ) := Solve ( D ) θ ( 𝐳 0 ; 𝐱 ) , ‖ 𝐳 ⋆ θ − f θ ( 𝐳 ⋆ θ ; 𝐱 ) ‖ 2 ≤ ε res . \displaystyle\mathbf{z}^{\star}_{\theta}(\mathbf{x},\mathbf{z}_{0}):=\operatorname{Solve}^{(D)}_{\theta}(\mathbf{z}_{0};\mathbf{x}),\quad\left\|\mathbf{z}^{\star}_{\theta}-f_{\theta}(\mathbf{z}^{\star}_{\theta};\mathbf{x})\right\|_{2}\leq\varepsilon_{\mathrm{res}}. where ℓ θ ​ ( 𝐳 , 𝐱 , 𝐲 ) \ell_{\theta}(\mathbf{z};\mathbf{x},\mathbf{y}) denotes the supervised loss evaluated from latent state 𝐳 \mathbf{z} , Solve θ ( D ) \operatorname{Solve}^{(D)}_{\theta} denotes a D D -step lower-level rollout induced by repeated applications of f θ f_{\theta} , and ε res \varepsilon_{\mathrm{res}} is the residual tolerance for the reached state.

#### Fixed-point residual as a local convergence diagnostic.

The formulation clarifies why residual is a meaningful diagnostic under local stability. Suppose the reached basin contains a fixed point 𝐳 ⋆ = f θ ​ ( 𝐳 ⋆ , 𝐱 ) \mathbf{z}^{\star}=f_{\theta}(\mathbf{z}^{\star};\mathbf{x}) , and f θ f_{\theta} is L L -Lipschitz in that basin for some L < 1 L<1 . Then ‖ 𝐳 − 𝐳 ⋆ ‖ \displaystyle\|\mathbf{z}-\mathbf{z}^{\star}\| ≤ ‖ 𝐳 − f θ ​ ( 𝐳 , 𝐱 ) ‖ + ‖ f θ ​ ( 𝐳 , 𝐱 ) − f θ ​ ( 𝐳 ⋆ , 𝐱 ) ‖ \displaystyle\leq\|\mathbf{z}-f_{\theta}(\mathbf{z};\mathbf{x})\|+\|f_{\theta}(\mathbf{z};\mathbf{x})-f_{\theta}(\mathbf{z}^{\star};\mathbf{x})\| (5) ≤ ‖ R θ ​ ( 𝐳 , 𝐱 ) ‖ + L ​ ‖ 𝐳 − 𝐳 ⋆ ‖ , \displaystyle\leq\|R_{\theta}(\mathbf{z};\mathbf{x})\|+L\|\mathbf{z}-\mathbf{z}^{\star}\|, so ‖ 𝐳 − 𝐳 ⋆ ‖ ≤ ‖ R θ ​ ( 𝐳 , 𝐱 ) ‖ / ( 1 − L ) \|\mathbf{z}-\mathbf{z}^{\star}\|\leq\|R_{\theta}(\mathbf{z};\mathbf{x})\|/(1-L) . Thus, inside a stable basin, small residual implies closeness to the local attractor. To connect residual to correctness, one also needs an output margin. Let s θ , i , a ​ ( 𝐳 , 𝐱 ) s_{\theta,i,a}(\mathbf{z};\mathbf{x}) be the logit for assigning label a a at output location i i , and suppose 𝐳 ⋆ \mathbf{z}^{\star} decodes to the correct output 𝐲 \mathbf{y} . Define the minimum margin at the attractor by γ ⁡ ( 𝐳 ⋆ ) = min i ⁡ [ s θ , i , y i ​ ( 𝐳 ⋆ , 𝐱 ) − max a ≠ y i ⁡ s θ , i , a ​ ( 𝐳 ⋆ , 𝐱 ) ] . \gamma(\mathbf{z}^{\star})=\min_{i}\left[s_{\theta,i,y_{i}}(\mathbf{z}^{\star};\mathbf{x})-\max_{a\neq y_{i}}s_{\theta,i,a}(\mathbf{z}^{\star};\mathbf{x})\right]. (6) If γ ⁡ ( 𝐳 ⋆ ) > 0 \gamma(\mathbf{z}^{\star})>0 and each true-versus-competing logit gap is G gap G_{\mathrm{gap}} -Lipschitz in the same basin, then states within distance γ ⁡ ( 𝐳 ⋆ ) / G gap \gamma(\mathbf{z}^{\star})/G_{\mathrm{gap}} decode correctly. Combining this margin condition with Eq. 5 , a sufficient residual condition is ‖ R θ ​ ( 𝐳 , 𝐱 ) ‖ < ( 1 − L ) ​ γ ⁡ ( 𝐳 ⋆ ) G gap ⟹ 𝐲 ^ θ ​ ( 𝐳 , 𝐱 ) = 𝐲 . \|R_{\theta}(\mathbf{z};\mathbf{x})\|<(1-L)\frac{\gamma(\mathbf{z}^{\star})}{G_{\mathrm{gap}}}\quad\Longrightarrow\quad\hat{\mathbf{y}}_{\theta}(\mathbf{z};\mathbf{x})=\mathbf{y}. (7) Thus residual is a correctness proxy only under local stability, a correct attractor, and positive output margin; low residual near a spurious or low-margin attractor still certifies convergence, not correctness.

#### Implicit gradient conditioning.

The same formulation also clarifies why exact implicit gradient computation through long attractor solvers can be unstable. Let J 𝐳 = ∂ 𝐳 f θ ​ ( 𝐳 ⋆ , 𝐱 ) J_{\mathbf{z}}=\partial_{\mathbf{z}}f_{\theta}(\mathbf{z}^{\star};\mathbf{x}) and J θ = ∂ θ f θ ​ ( 𝐳 ⋆ , 𝐱 ) J_{\theta}=\partial_{\theta}f_{\theta}(\mathbf{z}^{\star};\mathbf{x}) . At an exact locally isolated fixed point, differentiating R θ ​ ( 𝐳 ⋆ , 𝐱 ) = 0 R_{\theta}(\mathbf{z}^{\star};\mathbf{x})=0 for fixed 𝐱 \mathbf{x} gives ( I − J 𝐳 ) ​ d ​ 𝐳 ⋆ = J θ ​ d ​ θ , d ​ 𝐳 ⋆ d ​ θ = ( I − J 𝐳 ) − 1 ​ J θ , (I-J_{\mathbf{z}})\,d\mathbf{z}^{\star}=J_{\theta}\,d\theta,\qquad\frac{d\mathbf{z}^{\star}}{d\theta}=(I-J_{\mathbf{z}})^{-1}J_{\theta}, (8) with Jacobians evaluated at ( 𝐳 ⋆ , θ , 𝐱 ) (\mathbf{z}^{\star},\theta,\mathbf{x}) . Thus, solver sensitivity is controlled by the resolvent ( I − J 𝐳 ) − 1 (I-J_{\mathbf{z}})^{-1} : when this operator is poorly conditioned, small parameter changes can cause large attractor shifts, and approximation errors in the lower-level solve can be amplified in the implicit gradient. This conditioning issue is a standard concern in implicit-layer training, where prior work studies Jacobian regularization, monotone or well-posed operators, and approximate or Jacobian-free backward passes ( Bai et al., 2021 ; Geng et al., 2021a ; Geng et al., 2021b ; Gu et al., 2020 ; Fung et al., 2022 ) . The role of truncation and SOT is therefore not only to reduce memory and compute, but also to keep optimization local while the latent trajectory tracks a changing attractor landscape.

### A.2 From Feedforward Models to Iterative Models: Training-Dynamics Ablations and Diagnostics

This subsection expands the construction path from feedforward models to weight-tied iterative models in Sec. 6.1 , Tab. 2 , using the design axes introduced in Sec. 3 , on Sudoku tasks. The full ablations cover weight-tied structure, hierarchical iterations, gradient truncation, supervision and optimization schedules, adaptive computation variants, and FLOPs and memory accounting. For weight-tied models, we follow the configurations of TRM listed in Tab. 17 . For a fair comparison, the Sudoku feedforward baseline uses 42 distinct blocks, matching equivalent-layer budget N eq = 42 N_{\mathrm{eq}}=42 of the corresponding weight-tied iterative model (Appendix D.4 ). Throughout this subsection, an iteration means one outer-loop step or segment, which may itself contain repeated applications. We count these through equivalent-layer evaluations. A trajectory with D D iterations contains D D outer-loop segments, and an iteration-depth multiplier scales the number of segments rather than the individual layer applications inside each segment.

Iterative models are fundamentally different from feedforward models.

Tab. 8 ( 8(a) ) shows that introducing a weight-tied iterative model improves substantially over the vanilla feedforward baseline on Sudoku (2.6% → \rightarrow 32.6%); Fig. 9 further shows the corresponding training/evaluation error curves on Sudoku, under matched layer-evaluation budgets. The curves show a more nuanced trade-off than a simple train–evaluation gap: at its best-evaluation checkpoint, the 2-iteration weight-tied model reduces both training and evaluation error relative to the feedforward depth baseline; among iterative models, increasing the iteration steps then raises the training error while reducing the evaluation error. Tab. 6 records this checkpoint-level comparison for the four plotted runs.

Thus, a weight-tied parameterization creates useful iterative capacity: under the matched layer-evaluation budget, the feedforward model underperforms in both training and evaluation, whereas replacing independent layers with repeated applications of shared parameters yields better generalization and a smaller train–evaluation mismatch. However, this capacity remains insufficient under the current budget, motivating the depth-scaling and additional training-dynamics ablations below.

Iteration steps induce a trade-off between alignment and feasibility.

Larger iterations (depth) are desirable because they can move states closer to stable, solution-aligned attractors; however, they also make training less feasible. As shown in Tab. 8 ( 8(b) ), doubling the iteration depth is already helpful, improving Sudoku from 32.6% to 51.3%. The natural next step is to scale this trajectory to a much larger depth multiplier (e.g., 16 × 16\times ), but the full-gradient backpropagation through the long trajectory is memory-prohibitive and recurrent-gradient products can explode or vanish. Detaching the carried state before the terminal loss makes the 16 × 16\times run feasible: the backward graph covers only the final local transition, and with a stronger learning rate and lower weight decay this terminal-loss recipe with detached carry reaches 51.8%. However, the gain over the 2 × 2\times setting is marginal relative to the additional computation, indicating that simply extending the terminal-loss trajectory with detached carry is not an efficient way to leverage the potential of long iterations. This motivates a more careful choice of supervision placement and optimization schedule.

The local residual and implicit gradient conditions behind this interpretation are separated in Appendix A.1 ; here we focus on the training-dynamics evidence.

Segmented online training alternates latent-state and parameter updates.

The weak gain from terminal-loss training with detached carry suggests that feasibility is not the only issue: once gradients are detached along most of the trajectory, the intermediate carried states receive little direct supervision. A natural compensation is therefore to add loss anchors along the long trajectory, so that more carried states are trained while each backward graph remains local. As introduced in Sec. 3 , we call this trajectory supervision (an offline deep-supervision schedule): the model evaluates losses at multiple carried states, ℒ off ​ ( θ ) = 1 M ​ ∑ m = 1 M ℓ θ ​ ( 𝐳 t m , 𝐱 , 𝐲 ) , 𝐳 k + 1 = f θ ​ ( 𝐳 k , 𝐱 ) , \mathcal{L}_{\mathrm{off}}(\theta)=\frac{1}{M}\sum_{m=1}^{M}\ell_{\theta}(\mathbf{z}_{t_{m}};\mathbf{x},\mathbf{y}),\qquad\mathbf{z}_{k+1}=f_{\theta}(\mathbf{z}_{k};\mathbf{x}), (9) and updates the parameters only after the full trajectory has been processed. This keeps training cost controlled and helps restore supervision along the trajectory.

However, offline trajectory supervision creates a stale-trajectory mismatch. With parameters held fixed while anchors are collected, several transient lower-level iterates are all asked to match the same upper-level target before the operator has been updated. The resulting objective can behave like average-state matching: it rewards moving an aggregate of those states toward the target, even when that aggregate lies off the trajectory reachable by the updated operator. Thus, extra anchors provide more local supervision, but they can also pull the learned dynamics toward a target that is not reachable under the updated operator.

SOT instead alternates the two levels. For a segment of h h function evaluations, 𝐳 s \mathbf{z}_{s} denotes the detached carried state from the previous segment, while the current segment remains gradient-tracked: 𝐳 ~ s + 1 ​ ( θ ) \displaystyle\tilde{\mathbf{z}}_{s+1}(\theta) = f θ ( h ) ​ ( 𝐳 s , 𝐱 ) , \displaystyle=f_{\theta}^{(h)}(\mathbf{z}_{s};\mathbf{x}), (10) g s \displaystyle g_{s} = ∇ θ ℓ θ ​ ( 𝐳 ~ s + 1 ​ ( θ ) , 𝐱 , 𝐲 ) | θ = θ s , \displaystyle=\nabla_{\theta}\ell_{\theta}(\tilde{\mathbf{z}}_{s+1}(\theta);\mathbf{x},\mathbf{y})\big|_{\theta=\theta_{s}}, θ s + 1 \displaystyle\theta_{s+1} = θ s − η g s , 𝐳 s + 1 = stopgrad ( 𝐳 ~ s + 1 ( θ s ) ) . \displaystyle=\theta_{s}-\eta g_{s},\qquad\mathbf{z}_{s+1}=\operatorname{stopgrad}(\tilde{\mathbf{z}}_{s+1}(\theta_{s})). The next latent segment is then generated under the updated parameters θ s + 1 \theta_{s+1} . Each segment first takes a lower-level corrector step in latent space, then takes an upper-level parameter step that reshapes the operator. This alternating view is natural because changing θ \theta changes the attractor landscape, while advancing 𝐳 \mathbf{z} reveals which basin the current operator can actually reach. If the h h -step local solver contracts errors by a factor ρ < 1 \rho<1 near the current attractor and the local attractor map has sensitivity κ θ ≈ ∥ ( I − J 𝐳 , s ) − 1 ​ J θ , s ∥ \kappa_{\theta}\approx\lVert(I-J_{\mathbf{z},s})^{-1}J_{\theta,s}\rVert , where J 𝐳 , s J_{\mathbf{z},s} and J θ , s J_{\theta,s} are the corresponding local Jacobians at segment s s , then the carried-state tracking error e s = ∥ 𝐳 s − 𝐳 θ s ⋆ ∥ e_{s}=\lVert\mathbf{z}_{s}-\mathbf{z}^{\star}_{\theta_{s}}\rVert obeys the bound e s + 1 \displaystyle e_{s+1} = ∥ f θ s ( h ) ​ ( 𝐳 s , 𝐱 ) − 𝐳 θ s + 1 ⋆ ∥ \displaystyle=\lVert f_{\theta_{s}}^{(h)}(\mathbf{z}_{s};\mathbf{x})-\mathbf{z}^{\star}_{\theta_{s+1}}\rVert (11) ≤ ∥ f θ s ( h ) ​ ( 𝐳 s , 𝐱 ) − 𝐳 θ s ⋆ ∥ + ∥ 𝐳 θ s ⋆ − 𝐳 θ s + 1 ⋆ ∥ \displaystyle\leq\lVert f_{\theta_{s}}^{(h)}(\mathbf{z}_{s};\mathbf{x})-\mathbf{z}^{\star}_{\theta_{s}}\rVert+\lVert\mathbf{z}^{\star}_{\theta_{s}}-\mathbf{z}^{\star}_{\theta_{s+1}}\rVert ≲ ρ ​ e s + κ θ ​ ∥ θ s + 1 − θ s ∥ . \displaystyle\lesssim\rho e_{s}+\kappa_{\theta}\lVert\theta_{s+1}-\theta_{s}\rVert.

This separates the two effects: latent correction reduces the first term, while the parameter update contributes the attractor shift in the second term. Compared with trajectory supervision under detached carry, SOT therefore keeps supervision closer to the currently reachable trajectory instead of optimizing many stale anchors before any parameter update occurs.

The diagnostics below test this interpretation. They first show that early anchors can conflict with the detached trajectory, and then show that SOT turns the same long-rollout supervision into a much more effective training procedure.

Together, Fig. 11 and Tab. 7 show that intermediate anchors are not uniformly harmful: anchors over the full trajectory include early transient states and reduce accuracy from 51.8% to 47.1% relative to terminal-loss supervision, whereas anchors restricted to the late trajectory can improve performance. We interpret the late-anchor gain through the attractor-alignment view: if solution alignment is mediated by attractor basins, the same target loss has a different meaning before and after the trajectory reaches the basin. The residual trace gives a concrete proxy for this split: after the sharp early drop, later states lie on a more stable part of the rollout, so supervising them creates less conflict with the model’s own dynamics.

Supervision Anchors Acc. terminal loss 16 16 51.80 full anchors 1 : 16 1{:}16 47.10 late anchors 8 : 16 8{:}16 51.36 late anchors 12 : 16 12{:}16 57.50

Before the trajectory enters a solution-aligned basin, supervision on intermediate states mainly acts as coarse guidance, and its local gradients can be unreliable because they are attached to transient states rather than to a stable solution. After the trajectory enters the basin, the same target supervision becomes more trustworthy because the local state is already near the solution attractor. Late anchors therefore concentrate gradient signal in the regime where the gradients are aligned with the desired attractor. Under this view, if several late anchors all lie in the attractor basin, accumulating or upweighting those late losses behaves like a larger effective step size on reliable gradients, instead of amplifying noisy early-trajectory gradients. For each anchor range in Tab. 7 , we report the best accuracy over learning rates { 10 − 3 , 5 × 10 − 4 , 10 − 4 , 5 × 10 − 5 } \{10^{-3},5{\times}10^{-4},10^{-4},5{\times}10^{-5}\} and weight decays { 0.1 , 0.5 , 1.0 } \{0.1,0.5,1.0\} .

The SOT rows give the direct evidence for the alternating formulation. As shown in Tab. 8 ( 8(c) ), switching from trajectory supervision at 16 × 16\times to SOT at 16 × 16\times improves Sudoku from 47.1% to 74.7% under the same nominal depth multiplier. The gain is therefore not explained by adding anchors alone: the key change is that parameter updates are interleaved with latent-state updates, so later trajectory segments are generated by the current operator rather than by stale parameters. SOT can further reduce memory and compute cost when combined with in-segment gradient truncation, which shortens the backward graph inside each segment. Tab. 8 ( 8(d) ) shows that this truncation interacts strongly with the latent structure. In the single-latent setting, in-segment truncation reduces Sudoku-Extreme accuracy from 74.7% to 67.2%. With hierarchical iterations, however, the same truncation improves accuracy from 69.8% to 75.4%. This reversal suggests that hierarchical iterations shape the training dynamics differently from the single-latent update, an interaction we discuss in the next finding.

Hierarchical iterations change performance, but their effect is difficult to decouple from the training recipe.

Hierarchical iterations interact with other training strategies. As shown in Tab. 8 ( 8(d) ), without in-segment truncation, the single-latent model is stronger on Sudoku, whereas with truncation the hierarchical variant becomes stronger. The Adaptive Computation Time (ACT) ablation rows in Tab. 8 ( 8(e) ) show a second interaction with the halting mechanism. With learned ACT, the hierarchical latent model reaches 84.8% on Sudoku, while the corresponding single-latent 𝐳 \mathbf{z} variant reaches 73.9%. Thus, hierarchy is not a standalone switch; its effect depends on the surrounding training recipe. We also observed that the relative performance of hierarchical iterations compared with the single-latent model depends on the task.

Adaptive Computation Time (ACT) changes training dynamics through learned halting.

The halting mechanism is not only for efficiency: when applied to the training of iterative models, it also shapes the training dynamics, and different halting signals lead to different outcomes. As shown in Tab. 8 ( 8(e) ), oracle (ground-truth-based) halting collapses the hierarchical model from 75.4% to 13.6% on Sudoku, whereas a learned ACT head improves the result from 75.4% without it to 84.8% in this setting. Furthermore, we find that training a learned ACT head, even when the predicted halting signal is not used for dynamic early exit during training, can mitigate overfitting, as shown in Fig. 12 ( Training Head + No Early Halt vs. No Early Halt).

This hierarchy dependence is one reason we report ACT as part of the training-dynamics recipe rather than as a purely inference-side add-on.

Cost accounting explains why long-trajectory training is feasible.

Tab. 9 gives the symbolic cost accounting behind these choices. The key distinction is between the length of the forward trajectory and the length of the backward graph. Let T T denote the number of outer-loop steps covered by a long trajectory. We write C ⁡ ( ⋅ ) C(\cdot) for the backward and parameter-update cost per optimizer interval and M ⁡ ( ⋅ ) M(\cdot) for the retained training memory per optimizer interval. The resulting accounting separates the effects of detached carry and truncation, which reduce backward and memory pressure, from SOT, which changes when the optimizer update happens. A more detailed derivation of this symbolic cost accounting is available in a separate blog post ( Huang, 2026 ) . For the remaining local terms, we use: Backward and parameter-update costs c ℓ c_{\ell} One local loss/head backward. c B c_{B} Segment parameter-backward. c B trunc c_{B}^{\mathrm{trunc}} Truncated segment parameter-backward. c J c_{J} Temporal state-backward through a segment. c θ c_{\theta} Extra shared-gradient accumulation. c u c_{u} Parameter update for one recurrent block. Retained memory terms a f a_{f} Activation memory for one segment. a ℓ a_{\ell} Activation memory for one loss/head branch. a f det a_{f}^{\mathrm{det}} Segment activation after detached carry. a f trunc a_{f}^{\mathrm{trunc}} Segment activation under truncation. P P Parameter-side memory for one recurrent block. These terms come from the local loop backward equations. For one segment transition 𝐳 s + 1 = f θ ​ ( 𝐳 s , 𝐱 ) \mathbf{z}_{s+1}=f_{\theta}(\mathbf{z}_{s};\mathbf{x}) , define J s \displaystyle J_{s} = ∂ 𝐳 s + 1 ∂ 𝐳 s , \displaystyle=\frac{\partial\mathbf{z}_{s+1}}{\partial\mathbf{z}_{s}}, B s \displaystyle B_{s} = ∂ 𝐳 s + 1 ∂ θ , \displaystyle=\frac{\partial\mathbf{z}_{s+1}}{\partial\theta}, (12) 𝐳 ¯ s \displaystyle\bar{\mathbf{z}}_{s} = J s ⊤ ​ 𝐳 ¯ s + 1 , \displaystyle=J_{s}^{\top}\bar{\mathbf{z}}_{s+1}, ∇ θ ( s ) ​ ℒ \displaystyle\nabla_{\theta}^{(s)}\mathcal{L} = B s ⊤ ​ 𝐳 ¯ s + 1 , \displaystyle=B_{s}^{\top}\bar{\mathbf{z}}_{s+1}, where the second line uses column adjoints and 𝐳 ¯ s + 1 = d ​ ℒ / d ​ 𝐳 s + 1 \bar{\mathbf{z}}_{s+1}=d\mathcal{L}/d\mathbf{z}_{s+1} is the incoming adjoint. Thus c J c_{J} denotes the temporal state-backward vector–Jacobian product through J s J_{s} , while c B c_{B} denotes the segment parameter-backward vector–Jacobian product through B s B_{s} . For shared recurrent weights, the step-local parameter contributions ∇ θ ( s ) ​ ℒ \nabla_{\theta}^{(s)}\mathcal{L} are accumulated into a shared gradient buffer, which gives the c θ c_{\theta} term. These equations are a notation device for cost accounting; standard autograd need not materialize J s J_{s} or B s B_{s} explicitly. With this notation, full-gradient training through a weight-tied trajectory has C full ​ ( T ) \displaystyle C_{\mathrm{full}}(T) = c ℓ + T ​ c B + ( T − 1 ) ​ c J + ( T − 1 ) ​ c θ + c u , \displaystyle=c_{\ell}+Tc_{B}+(T-1)c_{J}+(T-1)c_{\theta}+c_{u}, (13) M full ​ ( T ) \displaystyle M_{\mathrm{full}}(T) = T ​ a f + a ℓ + P . \displaystyle=Ta_{f}+a_{\ell}+P. (14) Detached carry keeps the forward trajectory long but removes the temporal state-backward chain. For terminal-loss training with detached carry, only the final local transition contributes to the backward graph: C det ​ ( T ) \displaystyle C_{\mathrm{det}}(T) = c ℓ + c B + c u , \displaystyle=c_{\ell}+c_{B}+c_{u}, (15) M det ​ ( T ) \displaystyle M_{\mathrm{det}}(T) = a f det + a ℓ + P . \displaystyle=a_{f}^{\mathrm{det}}+a_{\ell}+P. (16) SOT then changes the optimizer interval itself from a full T T -step trajectory to one outer-loop step: C SOT \displaystyle C_{\mathrm{SOT}} = c ℓ + c B + c u , \displaystyle=c_{\ell}+c_{B}+c_{u}, M SOT \displaystyle M_{\mathrm{SOT}} = a f det + a ℓ + P , \displaystyle=a_{f}^{\mathrm{det}}+a_{\ell}+P, (17) C SOT + trunc \displaystyle C_{\mathrm{SOT+trunc}} = c ℓ + c B trunc + c u , \displaystyle=c_{\ell}+c_{B}^{\mathrm{trunc}}+c_{u}, M SOT + trunc \displaystyle M_{\mathrm{SOT+trunc}} = a f trunc + a ℓ + P . \displaystyle=a_{f}^{\mathrm{trunc}}+a_{\ell}+P. (18)

Notes. The local symbols follow the surrounding text and the derivation in Huang (2026) . Only the final local transition contributes to the backward graph in the terminal-loss detached-carry row. The trajectory-supervision row uses the offline end-of-trajectory loss accumulation contract. Depth-independent constants outside the recurrent chain are omitted; a fixed 16 ​ L 16L -step training horizon is obtained by multiplying by the number of intervals needed to cover 16 ​ L 16L outer-loop steps.

### A.3 Additional Experiments on Randomized State Initialization

This section provides supporting ablations for randomized state initialization ( RI ) in Sec. 5.1 . The main text uses simple zero-mean Gaussian initial states to improve coverage over attractor basins under depth–breadth scaling. Here we ask two narrower questions: whether replacing this simple stochastic prior with an input-conditioned learnable initializer is beneficial, and how sensitive the method is to the Gaussian noise scale. The results support the main-text design choice: simple randomized initialization is effective, while the tested learnable initializer and scale tuning do not change the central conclusion.

#### Learnable initial state.

A body of work on diffusion models suggests that the choice of initialization can significantly affect generation quality, and that learning a better initialization than standard Gaussian noise can be beneficial. For example, Zhou et al. (2025) proposes golden noise , where an auxiliary network learns to transform Gaussian noise into a prompt-conditioned initialization that improves alignment. Related approaches include directly optimizing the initial noise at inference time ( Guo et al., 2024 ) , as well as reducing the initialization gap in video diffusion models through structured initialization schemes ( Wu et al., 2024 ) . These results motivate a natural question in our setting: whether learning the initial latent state 𝐳 0 \mathbf{z}_{0} can similarly improve iterative reasoning models.

Instead of sampling 𝐳 0 ∼ 𝒩 ⁡ ( 0 , σ 0 ​ I ) \mathbf{z}_{0}\sim\mathcal{N}(0,\sigma_{0}I) , we consider a simple learnable initialization scheme. Specifically, we introduce an input-conditioned 2-layer MLP g ϕ g_{\phi} that predicts the initial state 𝐳 0 = g ϕ ​ ( 𝐱 ) \mathbf{z}_{0}=g_{\phi}(\mathbf{x}) , and train ϕ \phi jointly with the rest of the model parameters under the same training objective. This can be viewed as learning a conditional prior over the initial latent state.

#### Empirical observation.

In our experiments, learning the initialization does not improve the training or held-out evaluation accuracy curves under the protocol used here. Tab. 10 reports the held-out exact accuracy of the TRM baseline, TRM with randomized state initialization (TRM + RI), and TRM with a learnable initializer 𝐳 0 = g ϕ ​ ( 𝐱 ) \mathbf{z}_{0}=g_{\phi}(\mathbf{x}) . The learnable initializer reaches 83.99 % 83.99\% exact accuracy at 50k training steps, compared with 86.03 % 86.03\% for TRM + RI and 84.06 % 84.06\% for the TRM baseline. Thus, the tested input-conditioned initializer does not improve over simple randomized initialization, and it also does not provide a reliable gain over the baseline TRM.

Across the full set of evaluated checkpoints up to 50k training steps, the learnable initializer never exceeds TRM + RI on held-out exact accuracy, and its best checkpoint remains slightly below the 50k result of the TRM baseline.

#### Scope and limitations.

Since we do not conduct further analysis or ablations on alternative initialization parameterizations, architecture designs, objectives, or regularization strategies, we do not make stronger claims about the general effectiveness of learnable initializations in iterative reasoning models. A more systematic study of initialization priors in latent state space is left for future work.

#### Randomness scale.

In the main text, we instantiate RI with zero-mean Gaussian initial states. This section examines how the scale of this initialization randomness affects TRM performance.

TRM maintains two latent spaces, a high-level latent 𝐳 H \mathbf{z}_{H} and a low-level latent 𝐳 L \mathbf{z}_{L} . We therefore vary the noise scale for each latent separately by sampling 𝐳 H ∼ 𝒩 ⁡ ( 0 , σ H ​ I ) \mathbf{z}_{H}\sim\mathcal{N}(0,\sigma_{H}I) and 𝐳 L ∼ 𝒩 ⁡ ( 0 , σ L ​ I ) \mathbf{z}_{L}\sim\mathcal{N}(0,\sigma_{L}I) . When a noise scale is not explicitly specified, we use the default σ = 1 \sigma=1 . Setting σ = 0 \sigma=0 corresponds to a deterministic (fixed) initialization.

Overall, randomized state initialization can improve performance over the deterministic fixed-initialization run in this sweep, and the choice of noise scale matters. For example, randomizing only 𝐳 H \mathbf{z}_{H} (setting σ H = 1 , σ L = 0 \sigma_{H}=1,\sigma_{L}=0 ) improves exact accuracy from 84.06 % 84.06\% to 86.29 % 86.29\% , and randomizing only 𝐳 L \mathbf{z}_{L} (setting σ H = 0 , σ L = 1 \sigma_{H}=0,\sigma_{L}=1 ) improves it to 86.25 % 86.25\% . For the joint sweep, the evaluated settings with σ H = 1 \sigma_{H}=1 achieve exact accuracies 86.03 % 86.03\% , 86.83 % 86.83\% , 87.30 % 87.30\% , and 86.85 % 86.85\% for σ L ∈ { 1 , 4 , 8 , 16 } \sigma_{L}\in\{1,4,8,16\} , respectively. Fixing σ L = 1 \sigma_{L}=1 and increasing σ H \sigma_{H} gives 86.03 % 86.03\% , 86.38 % 86.38\% , 86.08 % 86.08\% , and 86.29 % 86.29\% for σ H ∈ { 1 , 4 , 8 , 16 } \sigma_{H}\in\{1,4,8,16\} . Among the tested settings, the best performance is achieved by combining moderate noise on 𝐳 H \mathbf{z}_{H} with a larger noise scale on 𝐳 L \mathbf{z}_{L} , peaking at σ H = 1 , σ L = 8 \sigma_{H}=1,\sigma_{L}=8 with exact accuracy 87.30 % 87.30\% . These observations are consistent with the view that initialization randomness is most helpful when it places the iterative dynamics within basins that lead to correct solutions, whereas overly large perturbations may not further improve (and can slightly reduce) accuracy.

Due to limited computational resources, we report results from a single run for each configuration and do not include variance estimates across multiple random seeds. A more systematic study of variability across runs and a denser sweep of noise scales are left for future work.

### A.4 Additional Experiments on Path Stochasticity

As shown in Eq. 2 , we introduce path stochasticity by injecting step-wise noise into the iterative update, 𝐳 k + 1 = 𝐳 k + ( 1 − λ ) ​ r θ ​ ( 𝐳 k , 𝐱 ) + β ​ ε k \mathbf{z}_{k+1}=\mathbf{z}_{k}+(1-\lambda)\,r_{\theta}(\mathbf{z}_{k};\mathbf{x})+\beta\,\varepsilon_{k} , where ε k ∼ 𝒩 ⁡ ( 0 , I ) \varepsilon_{k}\sim\mathcal{N}(0,I) by default.

Tab. 12 reports a brief ablation over the fixed Gaussian noise scale β \beta , along with a learned-noise variant. Moderate Gaussian noise yields comparable performance to the default setting, whereas overly large noise can slightly reduce evaluation accuracy. Although the learned-noise variant performs best in this small ablation, Tab. 13 shows that it does not consistently improve when the number of stochastic samples or restarts S S is increased. We therefore use fixed Gaussian noise by default and keep learned noise as an ablation rather than adding extra noise parameters to the main method.

### A.5 Generalization Beyond the Main Setting

We further test whether the proposed training-and-scaling recipe is tied to the main Sudoku-Extreme and Maze-Unique settings. Tab. 14 reports two complementary checks: performance on Mini-ARC ( Kim et al., 2022 ) , and transfer from the Sudoku MLP-token-mixer backbone to a self-attention Transformer backbone.

On Mini-ARC, EqR reaches 55.28 % 55.28\% exact accuracy, improving over both HRM ( 44.85 % 44.85\% ) and TRM ( 48.35 % 48.35\% ). On Sudoku-Extreme, the same pattern appears across two token mixers. For the MLP-token-mixer backbone used in the main Sudoku setting, the training interventions improve accuracy from 84.1 % 84.1\% to 86.4 % 86.4\% , and inference scaling raises it further to 99.8 % 99.8\% . For the Transformer backbone, the corresponding numbers are 72.0 % 72.0\% , 74.7 % 74.7\% , and 95.9 % 95.9\% . These results suggest that the gains are not limited to the main Sudoku-Extreme and Maze-Unique experiments, nor to the specific MLP-token-mixer backbone used in the standard Sudoku-Extreme setup.

### A.6 Seed Stability Diagnostics

We check whether the same-budget gain is stable across independent random seeds for EqR. Across five seeds at 50k training steps, the baseline reaches 84.33 ± 0.59 % 84.33\pm 0.59\% exact accuracy (95% CI: [83.59, 85.07]), whereas EqR reaches 86.18 ± 0.44 % 86.18\pm 0.44\% (95% CI: [85.63, 86.72]). Thus, EqR remains higher than the baseline at the same budget and shows slightly lower seed-to-seed variation.

## Appendix B Qualitative Study

Fig. 13 visualizes one TRM reasoning trajectory on a Sudoku-Extreme puzzle. Each panel decodes the model’s current latent state into a full Sudoku grid after one iteration step. Early iterations already propose many correct entries, but later iterations continue to revise both correct and incorrect cells. The circled cell illustrates this non-monotonic behavior: the decoded value alternates across several candidates before the trajectory eventually settles into a consistent solution.

## Appendix C Dataset Details and Task Definitions

This appendix defines the dataset variants and task conventions used throughout our experiments, with particular attention to the distinction between the original Maze-1k benchmark and our uniquely solvable Maze-Unique setting.

### C.1 Dataset and Benchmark Specifications

#### Sudoku-Extreme

Sudoku-Extreme ( Wang et al., 2025 ) is a benchmark of exceptionally challenging 9 × 9 9\times 9 Sudoku instances designed to stress long-horizon constraint satisfaction. According to the HRM paper, it remains difficult even for strong modern reasoning models such as DeepSeek-R1 and Claude 3.7 8k. We reuse the code and data released with the Sudoku-Extreme dataset from HRM ( Wang et al., 2025 ) .

Sudoku-Lite. As shown in Tab. 16(a) , the validation set of Sudoku-Extreme is very large. To improve evaluation efficiency, we introduce a subset of 2048 cases sampled uniformly at random from Sudoku-Extreme, which we term Sudoku-Lite.

Tab. 15 compares exact accuracy on Sudoku-Extreme and Sudoku-Lite. Across multiple model variants, performance on Sudoku-Lite is slightly worse, suggesting that this smaller evaluation subset is not an easier benchmark for current models.

Dataset TRM HRM EqR Sudoku-Extreme 84.1 61.0 86.4 Sudoku-Lite 82.0 57.8 84.3

Maze-1k. Maze-1k evaluates shortest-path prediction on a 30 × 30 30\times 30 grid with obstacle cells. The benchmark follows the instance-generation procedure of Lehnert et al. (2024) , as used by HRM. Many instances admit multiple shortest paths, while the released dataset provides one labeled path per input; Fig. 14(a) shows a representative example.

Maze-Unique. We construct Maze-Unique as a controlled 30 × 30 30\times 30 variant in which every retained instance has a unique shortest path. Each maze is generated as a perfect maze, i.e., a tree-structured grid with a single simple path between any pair of cells. For each maze, we repeatedly sample start-goal pairs, compute the shortest-path length, retain pairs within the target length range, and de-duplicate mazes across the training and test splits. The final dataset contains 1,000 training instances and 1,000 test instances. As shown in Tab. 16(b) , this filtering does not make the task shorter by path length: Maze-Unique has a slightly larger average shortest-path length than Maze-1k. A concrete example is shown in Fig. 14(b) .

#### Naming convention.

In the main text, for simplicity, Sudoku denotes Sudoku-Extreme and Maze denotes Maze-Unique, matching the shorthand introduced in Sec. 6 . Sudoku-Extreme is the full HRM benchmark used for the main Sudoku results, Sudoku-Lite is our 2048-example evaluation subset sampled from Sudoku-Extreme, Maze-1k is the original ambiguous shortest-path benchmark used by HRM/TRM, and Maze-Unique is our uniquely solvable maze benchmark used for the main Maze results.

### C.2 Datasets and Task Definitions Shape Attractor Landscapes

We find that when the dataset is ill-defined with respect to the training target, attractor dynamics cannot be learned reliably. On the original Maze-1k dataset used in the HRM and TRM papers, iterative models fail to exhibit stable test-time scaling, and training remains unstable even after extensive hyperparameter tuning.

The root cause is label ambiguity rather than model capacity or optimization. The Maze-1k task is defined as finding a shortest path from start to goal, yet for most of the mazes in this dataset the shortest path is not unique (see Fig. 14(a) ). Despite this, the dataset provides only a single target trajectory per maze, effectively casting a one-to-many task as a one-to-one supervised learning problem. According to the HRM paper, this dataset is generated using the codebase of Lehnert et al. (2024) . That work explicitly distinguishes two variants of maze-style planning data. In the deterministic variant, the search procedure is fixed and produces a unique trace and solution for each maze. In the non-deterministic variant, randomized tie-breaking during search yields multiple equally valid shortest paths for the same maze input. For the non-deterministic variant, Lehnert et al. (2024) therefore report any-correct or any-optimal metrics, acknowledging that multiple outputs should be considered correct.

In contrast, HRM and TRM are trained on non-unique Maze-1k data using token-level cross entropy against a single provided trajectory, creating a mismatch between the training objective and the task. From a landscape perspective, the task admits multiple correct attractors, yet the loss artificially designates one arbitrary attractor as the sole target and penalizes all others. Consequently, the learned attractor landscape is misaligned with correctness: nearby trajectories may converge to alternative valid paths that nonetheless incur non-negligible loss, yielding multiple shallow and competing attractors. This destroys stable depth scaling, and randomized state initialization or noise injection becomes counterproductive, as improving coverage or stability of one attractor can degrade performance when there are actually multiple valid attractors.

To isolate this effect, we construct Maze-Unique, where each maze admits a unique shortest path. Under this setting, supervision aligns with the task structure, and iterative models recover stable attractor dynamics and meaningful test-time scaling behavior. When scaling up depth at test time, we found that models trained on Maze-Unique improve as NFE increases, whereas models trained on the original Maze-1k dataset stay flat or slightly degrade. While direct metric comparisons across datasets are not meaningful due to differences in model size and setup, the qualitative difference in stability and scaling behavior is clear.

The dataset fundamentally determines the geometry of both the optimization objective and the learned attractor landscape. When a task admits multiple valid solutions, imposing single-solution supervision makes learning ill-posed. This misspecification prevents stable attractor landscapes from forming and, as a result, breaks test-time scaling.

## Appendix D Method and Experimental Details

This section collects the implementation, hyperparameter, baseline-tuning, and evaluation details needed to reproduce and interpret the experimental results.

### D.1 Architecture and Hyperparameters

Here we introduce the hyperparameters used in the experiments. For Sudoku-Extreme, we follow the architecture used in the TRM paper, keeping the model components and training procedure identical unless otherwise specified.

For Maze-Unique, we deliberately reduce model capacity by decreasing the number of layers from 2 to 1 and the hidden dimension from 512 to 128. We find that larger models can reach near-perfect performance on this task, which makes the effects of different test-time-scaling variants difficult to observe. By constraining model capacity, we encourage the model to rely on iterative refinement, making the attractor dynamics easier to study. Detailed configurations are shown in Tab. 17 .

### D.2 Learning-Rate Control for Feedforward Baselines

To rule out the possibility that feedforward baselines underperform due to suboptimal learning-rate choices, we sweep three learning rates { 5 × 10 − 4 , 5 × 10 − 5 , 1 × 10 − 4 } \{5\times 10^{-4},\,5\times 10^{-5},\,1\times 10^{-4}\} and inspect the resulting training and evaluation trajectories. Across this sweep, learning-rate tuning does not remove the feedforward generalization gap: the feedforward models can fit the training set, but evaluation accuracy remains extremely low. In particular, the 4-layer MLP moves from underfitting at the smallest learning rate to high training accuracy at larger learning rates, whereas the 16-layer MLP fits the training set across all three learning rates. This indicates that the feedforward baselines mainly memorize the Sudoku-Extreme training distribution rather than learning a structure that generalizes.

### D.3 Evaluation Metrics

This subsection collects the formal definitions of the evaluation metrics used in Sec. 6 .

#### Averaged exact acc.

We report averaged exact acc. under B B independent restarts: AccAvg ( B ; 𝐱 ) ≔ 1 B ∑ i = 1 B 𝟏 { y ^ ( i ) ( 𝐱 ) = 𝐲 } . \mathrm{AccAvg}(B;\mathbf{x})\;\coloneqq\;\frac{1}{B}\sum_{i=1}^{B}\mathbf{1}\{\hat{y}^{(i)}(\mathbf{x})=\mathbf{y}\}. (19) When B = 1 B=1 , this reduces to standard single-run accuracy.

#### Top-1 convergence accuracy.

Given B B independent restarts and T T iteration steps, we select the trajectory whose final states exhibit the strongest convergence, measured by the mean residual over the last L L iterations, r T , L ( i ) ​ ( 𝐱 ) = 1 L ​ ∑ t = T − L + 1 T ‖ f θ ​ ( 𝐳 t ( i ) , 𝐱 ) − 𝐳 t ( i ) ‖ . r_{T,L}^{(i)}(\mathbf{x})=\frac{1}{L}\sum_{t=T-L+1}^{T}\bigl\|f_{\theta}(\mathbf{z}_{t}^{(i)};\mathbf{x})-\mathbf{z}_{t}^{(i)}\bigr\|. We then report whether the corresponding prediction is correct: Top1Conv ( B ; 𝐱 ) ≔ { 𝐲 ^ ( i ⋆ ) ( 𝐱 ) = 𝐲 } , \mathrm{Top1Conv}(B;\mathbf{x})\;\coloneqq\;\mathbf{1}\!\left\{\hat{\mathbf{y}}^{(i^{\star})}(\mathbf{x})=\mathbf{y}\right\}, (20) where i ⋆ ∈ arg ⁡ min i ∈ { 1 , … , B } ​ r T , L ( i ) ​ ( 𝐱 ) i^{\star}\in\arg\min_{i\in\{1,\dots,B\}}r_{T,L}^{(i)}(\mathbf{x}) . Unless otherwise stated, we use a convergence window of L = 3 L=3 iterations.

#### Majority vote accuracy.

As a complementary baseline under breadth scaling, we report majority vote accuracy over the B B independent restarts, MajVote ( B ; 𝐱 ) ≔ { mode ( { ^ 𝐲 ( i ) ( 𝐱 ) } i = 1 B ) = 𝐲 } . \mathrm{MajVote}(B;\mathbf{x})\;\coloneqq\;\mathbf{1}\!\left\{\mathrm{mode}\big(\{\hat{}\mathbf{y}^{(i)}(\mathbf{x})\}_{i=1}^{B}\big)=\mathbf{y}\right\}. (21)

#### Path independence across restarts.

We quantify inference stability by measuring how sensitive accuracy is to restart randomness. For an input 𝐱 \mathbf{x} , let Acc ¯ B ​ ( 𝐱 ) \bar{\mathrm{Acc}}_{B}(\mathbf{x}) denote the mean exact accuracy over B B independent restarts. We define Δ PI ​ ( B ) ≔ 𝔼 𝐱 ​ [ | Acc ¯ B ​ ( 𝐱 ) − Acc ¯ 1 ​ ( 𝐱 ) | ] . \Delta_{\mathrm{PI}}(B)\;\coloneqq\;\mathbb{E}_{\mathbf{x}}\!\left[\left|\bar{\mathrm{Acc}}_{B}(\mathbf{x})-\bar{\mathrm{Acc}}_{1}(\mathbf{x})\right|\right]. (22) Smaller Δ PI ​ ( B ) \Delta_{\mathrm{PI}}(B) indicates stronger path independence.

### D.4 Compute Accounting for Iterative Inference

We count iterations at the outer-loop level unless noted otherwise. We use D D for the number of outer iterations in one trajectory and B B for the number of independent restarts. We use the number of function evaluations, NFE = D ⋅ B \mathrm{NFE}=D\cdot B , to describe inference budgets; each function evaluation corresponds to one outer-loop iteration.

One outer-loop iteration can contain several real layer applications. For Sudoku-Extreme, the update function applies two real layers over 21 inner loops, so one outer iteration corresponds to N eq = 2 ⋅ 21 = 42 N_{\mathrm{eq}}=2\cdot 21=42 equivalent layers. A single trajectory with D = 1024 D=1024 therefore reaches D ⋅ N eq = 1024 ⋅ 42 = 43,008 D\cdot N_{\mathrm{eq}}=1024\cdot 42=43{,}008 equivalent layer evaluations. This is the source of the “over 40,000 layers” statement in the main text.

Breadth scaling multiplies the total budget, but it does not change the depth of any individual trajectory. For total equivalent-layer accounting, NLE = D ⋅ B ⋅ N eq \mathrm{NLE}=D\cdot B\cdot N_{\mathrm{eq}} . The best Sudoku-Extreme result in Tab. 4 uses D = 64 D=64 and B = 128 B=128 , i.e., 8192 8192 function evaluations and 64 ⋅ 128 ⋅ 42 = 344,064 64\cdot 128\cdot 42=344{,}064 total equivalent layer evaluations. We describe this setting as two-axis scaled inference rather than a 344k-depth unroll, since each trajectory still has depth D = 64 D=64 .

## Appendix E Extended Related Work and Discussion

This appendix expands the related work discussion in the main text.

#### Deep Equilibrium Models.

Our framework is closely related to implicit models, especially Deep Equilibrium Models (DEQs) ( Bai et al., 2019 ) . Related work extends this implicit view through path-independent equilibria for exploiting test-time computation ( Anil et al., 2022 ) and practical training methods for implicit models ( Geng et al., 2021a ; Geng et al., 2021b ; Fung et al., 2022 ; Gu et al., 2020 ) . Rather than stacking a fixed number of explicit layers, a DEQ defines the representation as the fixed point of a weight-tied nonlinear transformation. Concretely, a DEQ solves for an equilibrium 𝐳 ⋆ \mathbf{z}^{\star} satisfying 𝐳 ⋆ = f θ ​ ( 𝐳 ⋆ , 𝐱 ) \mathbf{z}^{\star}=f_{\theta}(\mathbf{z}^{\star};\mathbf{x}) . Under convergence, this can be viewed as the implicit limit of an infinitely deep weight-tied network.

We borrow the same fixed-point vocabulary, but study a different question. DEQ work primarily uses convergence to an equilibrium as a representation-learning and training device; our goal is to understand when the learned latent space dynamics make convergence reliable for solving a task. In our setting, reaching some fixed point is not enough: the model must shape a landscape whose large, stable basins correspond to correct solutions rather than spurious or unstable attractors. Thus attractor coverage, stability, and basin size provide a language for explaining why iterative reasoning succeeds, fails, or benefits from additional inference-time updates.

#### Latent reasoning models.

We use latent reasoning models to refer to methods that spend additional computation in latent space before emitting externally visible tokens or final predictions. This latent computation can be organized along two axes. The vertical axis increases computation by repeatedly updating a latent state with weight-tied iterations, as in weight-tied language models ( Geiping et al., 2025 ; Zhu et al., 2025 ) , PonderLM ( Zeng et al., 2026 ) , Parcae ( Prairie et al., 2026 ) , LoopViT ( Shu et al., 2026 ) , and the HRM/TRM/URM line of structured reasoners ( Wang et al., 2025 ; Jolicoeur-Martineau, 2025 ; Gao et al., 2025 ) . The horizontal axis inserts additional latent positions before a visible output: pause tokens delay answer extraction while the decoder processes extra hidden vectors ( Goyal et al., 2024 ) , Coconut feeds the last hidden state back as a continuous thought ( Hao et al., 2025 ) , SoftCoT and SoftCoT++ construct soft thought tokens for efficient or diverse continuous-space reasoning ( Xu et al., 2025b ; Xu et al., 2025a ) , and PonderLM-2 pretrains latent thoughts before actual token prediction ( Zeng et al., 2025 ) . Recent implicit-CoT variants further supervise, align, or score these latent tokens to reduce collapse and improve interpretability or parallel test-time scaling ( Wei et al., 2026 ; Chu et al., 2026 ; You et al., 2025 ) . These horizontal methods internalize or compress chain-of-thought-like computation into latent tokens, whereas our work focuses on the vertical fixed-state dynamics of iterative reasoners: we ask when extra updates help by studying whether training shapes a solution-aligned attractor landscape, rather than treating iteration count or hierarchy alone as the source of generalization.

#### Theoretical and mechanistic analyses of weight-tied iteration.

A useful way to organize this line of work is as a progression from what weight-tied iteration can compute, to what one more iteration is worth, and finally to what hidden-state mechanisms make iteration succeed or fail. The first question is computational: programmable-computer constructions show that a shallow weight-tied Transformer can emulate counters, branches, function calls, and small instruction-set programs when the sequence supplies both instructions and memory ( Giannou et al., 2023 ) . Learning-algorithm experiments show that adding iteration lets a Transformer fit data with accuracy comparable to a much larger standard Transformer ( Yang et al., 2024 ) . Expressivity analysis then identifies limits that are specific to repeated shared blocks and shows that timestep encodings recover additional iteration-dependent behavior ( Xu and Sato, 2025 ) . Latent-thought theory makes the same point from the reasoning side: on synthetic tasks where effective depth is the scarce resource, iterating a small block can approximate a much deeper non-weight-tied model ( Saunshi et al., 2025 ) . Together, these results justify treating iterations as real computation, but they do not yet say which trajectories through state space are reliable.

The second question is resource accounting: how much does an iteration buy, and what state must be preserved across iterations? Iso-depth scaling estimates that one extra iteration is only partially equivalent to adding a fresh layer ( Schwethelm et al., 2026 ) , while inverse-depth scaling argues that ordinary LLM depth can look like many similar layers averaging errors rather than composing qualitatively different transformations ( Liu et al., 2026 ) . Circuit-complexity analyses make the analogous point for horizontal token-space computation: intermediate decoding steps can serve as recurrent state, giving decoder-only Transformers more formal power as the chain-of-thought budget grows ( Merrill and Sabharwal, 2024 ) . This line makes iteration a measurable compute resource, but it still mostly reasons about capacity, scaling, memory, or stopping rules instead of the geometry of correct and incorrect solution states.

The third question is mechanistic: what structure appears in the latent states themselves? Controlled implicit-reasoning experiments show systematic generalization, depth extrapolation, and overthinking as the number of iterations changes ( Kohli et al., 2026 ) . Mechanistic analyses of weight-tied reasoning language models find cyclic trajectories approaching distinct fixed points, with attention behavior stabilizing across iterations ( Blayney et al., 2026 ) . Preference probes show that pairwise differences between iteration states can encode relational signals ( Kirin, 2026 ) , while latent-chain-of-thought probes caution that hidden states need not be directly readable as natural-language reasoning traces ( Lu et al., 2025 ) . Closest to our vocabulary, fixed-point analyses characterize stability through reachability, input-dependence, and geometry ( Labovich, 2026 ) , and two-scale trajectory studies distinguish small within-block refinements from larger cross-block drift ( Pappone et al., 2025 ) . Concurrent HRM analysis also links failures to fixed-point violations and multiple fixed points, but its strongest Sudoku gains rely on data augmentation, input perturbation, and model bootstrapping ( Ren and Liu, 2026 ) . Our work takes the next step: we directly measure the attractor landscape of finite-iteration, fixed-state weight-tied models, relate residual-state updates to iteration steps, and explain failure modes as trajectories entering unstable or wrong basins. We then use this landscape view to ask which training interventions reshape the basins, why those changes raise the inference-time upper bound, and how learned stopping can save compute without discarding the iterations that actually move a trajectory toward a correct attractor.

#### Flat minima.

The connection between the geometry of the loss landscape and a model’s generalization ability is a long-standing area of research. A central hypothesis, dating back to the work of Hochreiter and Schmidhuber (1997) , posits that optimizers that converge to “flat” minima in the parameter space tend to produce models that generalize better than those that converge to “sharp” minima. The intuition is that a flat region of the loss landscape is more robust to small perturbations in the model’s weights, such as those caused by shifts between the training and test data distributions. This idea has been revitalized by modern optimization methods like Sharpness-Aware Minimization (SAM) ( Foret et al., 2021 ) . SAM formalizes this intuition into a min-max optimization objective that explicitly searches for parameters residing in neighborhoods with uniformly low loss values. By doing so, SAM encourages convergence to flatter regions of the parameter landscape, leading to improvements in generalization across various benchmarks.

Our work translates this concept of robustness from parameter space to state space. While SAM seeks solutions that are stable with respect to perturbations of the model weights θ \theta , our framework seeks attractors that are stable with respect to perturbations of the latent state 𝐳 \mathbf{z} . The path stochasticity we introduce during training (section 5.2 ) serves a similar purpose to the perturbation step in SAM: it forces the model to learn an update function f θ f_{\theta} that defines a smooth and robust attractor landscape, where trajectories reliably converge to the correct solution despite noise. In essence, we are searching for “flat minima” in the landscape of the state-space dynamics, not just in the landscape of the training loss.
