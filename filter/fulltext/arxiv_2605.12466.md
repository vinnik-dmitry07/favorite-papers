##### Report GitHub Issue

Content selection saved. Describe the issue below:

\website https://attractor-models.github.io/ \code https://github.com/jacobfa/Attractor \correspondence

# Solve the Loop: Attractor Models for Language and Reasoning

###### Abstract

Looped Transformers offer a promising alternative to purely feed-forward computation by iteratively refining latent representations, improving language modeling and reasoning. Yet recurrent architectures remain unstable to train, costly to optimize and deploy, and constrained to small, fixed recurrence depths. We introduce Attractor Models , in which a backbone module first proposes output embeddings, then an attractor module refines them by solving for the fixed point, with gradients obtained through implicit differentiation. Thus, training memory remains constant in effective depth, and iterations are chosen adaptively by convergence. Empirically, Attractor Models outperform existing models across two regimes, large-scale language-model pretraining and reasoning with tiny models. In language modeling, Attractor Models deliver a Pareto improvement over standard Transformers and stable looped models across sizes, improving perplexity by up to 46.6% and downstream accuracy by up to 19.7% while reducing training cost. Notably, a 770M Attractor Model outperforms a 1.3B Transformer trained on twice as many tokens. On challenging reasoning tasks, we show that our model with only 27M parameters and approximately 1000 examples achieves 91.4% accuracy on Sudoku-Extreme and 93.1% on Maze-Hard, scaling favorably where frontier models like Claude and GPT o3, fail completely, and specialized recursive reasoners collapse at larger sizes. Lastly, we show that Attractor Models exhibit a novel phenomenon, which we call equilibrium internalization : fixed-point training places the model’s initial output embedding near equilibrium, allowing the solver to be removed at inference time with little degradation. Together, these results suggest that Attractor Models make iterative refinement scalable by turning recurrence into a computation the model can learn to internalize.

## 1 Introduction

The modern language-modeling era has been dominated by Transformers ( Vaswani et al., 2017 ) , which produce each token through a fixed feed-forward computation. This recipe has been extraordinarily successful ( OpenAI, 2023 ; Gemini Team, 2023 ; Grattafiori et al., 2024 ; Anthropic, 2024 ; Guo et al., 2025 ) , but it leaves a basic question unresolved: should each token be the product of a single pass of computation, or should a model be able to refine its latent prediction before committing to an output? A growing body of work suggests that such refinement can be powerful. Chain-of-thought reasoning ( Wei et al., 2023 ) can be viewed as one form of such refinement, where a model writes intermediate tokens, feeds them back into its context, and uses them to shape later predictions. Yet this routes computation through the discrete token channel and forces “thinking” to be written down, even when the effect might be to merely refine internal representations.

This limitation has inspired several lines of work on latent (or implicit) thinking and a re-emergence of architectural recurrence, which move thinking away from purely token-level generation. These include universal Transformers ( Dehghani et al., 2019 ) , looped Transformers ( Giannou et al., 2023a ; Yang et al., 2024a ) , recurrent-depth Transformers ( Kohli et al., 2026 ) , looped language models ( Zhu et al., 2025c ) , latent reasoning methods ( Geiping et al., 2025a ; Saunshi et al., 2025a ) , and continuous chain-of-thought approaches ( Hao et al., 2025 ; Mohtashami et al., 2023 ; Zhu et al., 2026 ) . Looped architectures can, in principle, express iterative or algorithmic procedures ( Yang et al., 2024b ; Giannou et al., 2023a ) , emulate additional depth through weight sharing ( Dehghani et al., 2019 ; Zhu et al., 2025c ) , reduce the context-length costs of token-level reasoning, and improve downstream generalization ( Labovich, 2026b ; Fan et al., 2025 ) . Empirically, recent looped language models offer gains in language modeling and reasoning ( Zhu et al., 2025c ; Geiping et al., 2025a ) , and tiny recursive models ( Wang et al., 2025 ; Jolicoeur-Martineau, 2025 ) have shown that recurrence can be useful in hard reasoning tasks in small-data regimes.

The challenge is that recurrence has proven difficult to use as a stable architectural building block. Recurrence is often accompanied by unstable training, large memory requirements that grow linearly with the number of recurrent steps, and significant, sequential compute ( Geiping et al., 2025a ; Zhu et al., 2025c ; Prairie et al., 2026 ) . Training recurrent networks typically requires backpropagation through time (or, depth) and carefully designed stabilization techniques; even then, latent-thinking models remain fragile and difficult to optimize ( Wei et al., 2025 ; Özeren and Aßenmacher, 2025 ; Deng et al., 2026 ; Deng et al., 2025 ; Rizvi-Martel et al., 2026 ) . For training, looped language models tend to require substantially more compute than comparable feed-forward models and can become memory-limited at larger recurrence depths. For instance, Geiping et al. (2025a) reports that training a recurrent model can consume raw FLOPs comparable to those of a feed-forward model ten times larger. At the opposite end of the spectrum, specialized tiny recursive reasoners exhibit a troubling “less is more” behavior and respond negatively to scaling: increasing model size can degrade or even collapse performance ( Jolicoeur-Martineau, 2025 ) .

### 1.1 Contributions

In this work, we design a general-purpose architecture for iterative refinement that is (i) stable to train, (ii) uses constant-memory in the number of refinement steps, (iii) is substantially cheaper to train than explicit unrolling, (iv) is efficient during inference, and (v) achieves a strong performance across both large-scale language modeling and hard reasoning with tiny models.

Refine outputs by solving the loop with Attractor Models. We introduce Attractor Models , a new family of architectures that treat latent refinement as a fixed-point problem in the output embedding space. The model first proposes an initial guess embedding using a non-recurrent backbone module (implemented as a Transformer in ours). A separate, typically smaller, recurrent network then refines this guess (Figure 1 ). Recent mechanistic analyses of looped language models demonstrate that, for the vast majority of tokens, the recurrent trajectory converges to a fixed point ( Blayney et al., 2026 ) . We build directly on this observation and instead of unrolling the loop for a predefined number of steps, we solve for the state to which the loop converges, inspired by Deep Equilibrium Models (DEQ; ( Bai et al., 2019 ) ). The name Attractor Model comes from dynamical systems, where an attractor is a set of states toward which a system evolves. In a sense, Attractor Models can be viewed as thinking before producing each token: the backbone proposes an initial latent prediction, the attractor module refines it to equilibrium, then decodes it into the output distribution.

Attractor Models offer stable, constant-memory, efficient training, and adaptive refinement. Unlike looped LMs, which finitely unroll the recurrent block, Attractor Models solve an equilibrium by treating the prediction target as a fixed-point computation. The number of refinement steps is therefore chosen adaptively according to convergence during both training and inference. We show that the memory cost during training remains constant in the number of iterations; whereas standard looped language models have a linear scaling increase with the number of loops. Our experiments demonstrate that the two-stage structure of Attractor Models, in which the backbone proposes and the attractor refines, enables stable, efficient training and strong performance.

Novel phenomenon: Equilibrium internalization. We observe that despite the fact that Attractor models are trained only with the next-token prediction loss, they learn to make the solver unnecessary. During training, the backbone’s initial prediction moves progressively closer to the fixed point, so fewer refinement steps are needed to reach approximate equilibrium (c.f. Figures 6 and 7 ). We call this phenomenon equilibrium internalization : the model appears to self-distill the iterative refinement process into its own initial output embedding, through a form of automatic curriculum. In this sense, recurrence acts as a moving training target, teaching the backbone where its computation should converge.

Strong performance in large-scale language modeling and hard reasoning with tiny models. Our experiments show that Attractor Models scale across two regimes. In large-scale language modeling, Attractor Models consistently outperform standard Transformers and stable looped language models across small (140M), medium (370M), and large (770M) sizes, delivering a Pareto improvement (Figure 1 ). We show that our models improve validation perplexity, out-of-distribution perplexity on Lambada ( Paperno et al., 2016 ) , and downstream benchmark accuracy while using substantially less training compute than comparable looped baselines. Notably, a 770M-parameter Attractor Model outperforms a 1.3B-parameter Transformer trained on twice as many tokens. Compared to looped LM Parcae ( Prairie et al., 2026 ) , our models use up to 31 % 31\% less training compute, while avoiding the memory growth associated with explicit unrolling. In hard reasoning tasks with tiny models, with only 27M parameters and approximately 1000 training examples, Attractor Models achieve 91.4% accuracy on Sudoku-Extreme and 93.1% on Maze-Hard. In this regime, standard Transformers as well as proprietary frontier models such as DeepSeek R1, Claude, and o3-mini fail completely at 0%, while specialized recursive architectures underperform our model and collapse when scaled. Attractor Models, in contrast, improve with scale.

## 2 Background: Looped Architectures

We begin with background on looped architectures. Let x = ( x 1 , … , x n ) ∈ 𝒱 n x=(x_{1},\ldots,x_{n})\in\mathcal{V}^{n} be an input sequence over vocabulary 𝒱 \mathcal{V} , and let d d denote the model width. Looped models can be written as a composition of three units: a prelude unit x ~ = 𝒫 ⁡ ( x ) ∈ ℝ n × d \tilde{x}=\mathcal{P}(x)\in\mathbb{R}^{n\times d} , which produces an input representation x ~ ∈ ℝ n × d \tilde{x}\in\mathbb{R}^{n\times d} ; a weight-tied recurrent unit h t + 1 = ℛ ⁡ ( h t , x ~ ) h_{t+1}=\mathcal{R}(h_{t},\tilde{x}) , which is applied repeatedly to a latent state h t ∈ ℝ n × d h_{t}\in\mathbb{R}^{n\times d} for T T steps; and a coda unit, which maps the final latent state to output probabilities p = 𝒞 ⁡ ( h T ) ∈ Δ ​ ( 𝒱 ) n p=\mathcal{C}(h_{T})\in\Delta(\mathcal{V})^{n} . Importantly, looped architectures commonly initialize the latent state at an uninformative value , such as h 0 = 0 h_{0}=0 or Gaussian noise h 0 ∼ 𝒩 ⁡ ( 0 , σ 2 ​ I ) h_{0}\sim\mathcal{N}(0,\sigma^{2}I) ( Geiping et al., 2025a ; Prairie et al., 2026 ; Bai et al., 2019 ) . Furthermore, the recurrent step may use the input representation only at the first step ( Zhu et al., 2025c ) . or at every recurrent step ( Geiping et al., 2025a ; Prairie et al., 2026 ) . Such injection may be through addition or concatenation with the recurrent state.

Models such as Parcae ( Prairie et al., 2026 ) , Huggin ( Geiping et al., 2025a ) , and Ouro ( Zhu et al., 2025c ) differ mainly in how they train, stop, or scale this looped architecture. In particular, the recurrence depth T T is a central design choice in these models. It may be fixed ( Jolicoeur-Martineau, 2025 ) , sampled during training ( Geiping et al., 2025a ; McLeish et al., ; Prairie et al., 2026 ) , or determined by an auxiliary halting mechanism ( Bae et al., 2025b ; Zhu et al., 2025c ) . Training then minimizes an objective averaged over both the data distribution and the chosen recurrence-depth mechanism, typically by backpropagation through depth. Consequently, both training cost and gradient memory are tied to the number of recurrent steps. Furthermore, changing T T at inference introduces a train–test mismatch, since the model is evaluated under a different computation graph than the one used during training, leading to degraded performance.

## 3 Solve the Loop with Attractor Models

As discussed in the previous section, standard looped language models ( Zhu et al., 2025c ; Prairie et al., 2026 ) use weight sharing to recurrently refine a hidden state that is initialized from an uninformative value and based on input embeddings. Predictions are then read out after a finite number of loops ( Prairie et al., 2026 ) , or once an auxiliary halting head becomes confident ( Graves, 2017 ; Zhu et al., 2025c ; Prairie et al., 2026 ) . This design carries three drawbacks: the loop count must be chosen at training time, training memory grows linearly in the number of loops, and accuracy degrades when more loops are run at inference than were seen during training ( Zhu et al., 2025c ) . As a result, recurrence often comes with unstable training, growing memory requirements, and large sequential compute, in some cases approaching the costs of training non-recurrent models ten times larger ( Geiping et al., 2025a ) .

Recent mechanistic analyses of looped language models ( Blayney et al., 2026 ) reveals that for the vast majority of tokens, the recurrent trajectory eventually converges to a fixed point. This suggests that the weight-tied recurrent modules are often approximating an underlying fixed-point computation, doing so through the recursive application of the weight-tied block truncated after T T steps. This observation motivates the design of Attractor Models, which we subsequently describe.

### 3.1 Attractor Model: Backbone and Attractor Modules

Motivated by the fixed-point behavior observed in looped models, we model recurrent refinement as an attractor. Rather than training a model to produce good predictions after a prescribed number of recurrent steps, we define the output as the equilibrium of the refinement process. Attractor Models consist of two modules: the backbone module (typically a larger Transformer network) first proposes a meaningful initial output embedding, and the attractor module (typically a smaller Transformer-based network) then refines this proposal until convergence. This makes the number of refinement steps a solver choice rather than a fixed architectural choice.

We first start by mapping the inputs x x into input embeddings x ~ = E ⁡ ( x ) ∈ ℝ n × d \tilde{x}=E(x)\in\mathbb{R}^{n\times d} , where E E denotes the tied embedding/unembedding. Then, the input embedding is processed by the backbone and attractor modules as described below.

The backbone module proposes an initial “guess ” output embedding. The backbone module 𝒯 θ b \mathcal{T}_{\theta_{b}} maps the input embeddings to an initial proposal: y ~ 0 = 𝒯 θ b ​ ( x ~ ) , where ​ x ~ = E ⁡ ( x ) . \displaystyle\tilde{y}_{0}=\mathcal{T}_{\theta_{b}}(\tilde{x}),\;\;\text{where}\;\;\tilde{x}=E(x). (1) We use y ~ 0 \tilde{y}_{0} as an initialization for the attractor module. Instead of initializing the loop from zero, noise, or an input-side representation, Attractor Models initialize the recurrent computation from a state that is already a coherent prediction embedding. In practice, 𝒯 θ b \mathcal{T}_{\theta_{b}} is a relatively high-capacity causal Transformer, so the refinement begins near a meaningful initialization rather than 0. We find that this makes training our method stable compared to DEQ, which experiences a blow-up in the number of iterations used later in training; whereas our method stabilizes later in training (c.f. Figure 6 (b)).

The attractor module refines the output embedding. The attractor module is a separate weight-tied refinement network 𝒯 θ a \mathcal{T}_{\theta_{a}} . Starting from the backbone proposal y ~ 0 \tilde{y}_{0} , it repeatedly refines the output embedding according to y ~ t + 1 = 𝒯 θ a ​ ( y ~ t , y ~ 0 ) , where ​ y ~ 0 = 𝒯 θ b ​ ( x ~ ) . \displaystyle\tilde{y}_{t+1}=\mathcal{T}_{\theta_{a}}(\tilde{y}_{t},\tilde{y}_{0}),\;\;\text{where}\;\;\tilde{y}_{0}=\mathcal{T}_{\theta_{b}}(\tilde{x}). (2) Here, we persistently inject the initial guess y ~ 0 \tilde{y}_{0} at every refinement step. This persistent injection keeps the attractor proposal-dependent and prevents it from collapsing to a proposal-independent fixed point. We ablate this conditioning mechanism in Section 4 . Importantly, we warm-start the attractor module at an informative proposal y ~ 0 \tilde{y}_{0} , in contrast to existing work that initialize the recurrent state at uninformative values such as zero or Gaussian noise ( Geiping et al., 2025a ; Prairie et al., 2026 ) ; see Table 6 for a comparison.

Rather than rolling out recurrent steps to reach a fixed point, we directly solve for the convergence: 𝒜 θ a ​ ( y ~ ⋆ , y ~ 0 ) ≔ 𝒯 θ a ​ ( y ~ ⋆ , y ~ 0 ) − y ~ ⋆ = 0 ⇒ y ~ ⋆ = RootFind ​ ( 𝒜 θ a ​ ( ⋅ , y ~ 0 ) , y 0 ) . \displaystyle\mathcal{A}_{\theta_{a}}(\tilde{y}^{\star},\tilde{y}_{0})\coloneqq\mathcal{T}_{\theta_{a}}(\tilde{y}^{\star},\tilde{y}_{0})-\tilde{y}^{\star}=0\;\Rightarrow\;\tilde{y}^{\star}\;=\;\texttt{RootFind}\!\left(\mathcal{A}_{\theta_{a}}(\cdot,\tilde{y}_{0});y_{0}\right). (3) In the forward pass, we compute this equilibrium with a root finder initialized at the backbone proposal. In our implementation, the RootFind algorithm uses Anderson acceleration, which combines a small window of past iterates and residuals to reach the fixed point faster than plain recursion. The solver exits when ‖ 𝒜 θ a ​ ( y ~ t , y ~ 0 ) ‖ 2 / ‖ y ~ t ‖ 2 < ε {\|\mathcal{A}_{\theta_{a}}(\tilde{y}_{t},\tilde{y}_{0})\|_{2}}/{\|\tilde{y}_{t}\|_{2}}<\varepsilon or after T max T_{\max} steps. Thus, the computation is controlled by the convergence of the residual rather than by a learned halting head or a preset loop count. In contrast to fixed unrolling, the number of refinement steps can therefore vary at inference time without changing the model. Finally, the equilibrium embedding is decoded with the tied unembedding.

Parameters of the Attractor Models consist of the tied embedding/unembedding matrices, the backbone module, and parameters of the attractor module: θ ≔ ( θ a , θ b , E ) \theta\coloneqq(\theta_{a},\theta_{b},E) . Compared to looped models, Attractor Models change both the starting point and the endpoint of recurrence: we initialize the loop from the output guess from the backbone network y ~ 0 \tilde{y}_{0} , and the decoded state is the attractor y ~ ⋆ \tilde{y}^{\star} rather than a finite unroll.

### 3.2 Training and Inference of Attractor Models

We now describe the training procedure for Attractor Models. We first explain how to differentiate through the fixed-point solver using implicit differentiation, and then show how the model is optimized with the standard cross-entropy language-modeling loss applied to the output y ⋆ y^{\star} .

Backward pass and implicit differentiation. Because Attractor Models define the output embedding as the solution to a fixed-point equation, we differentiate through the equilibrium using the implicit function theorem ( Krantz and Parks, 2002b ) . Let ℒ \mathcal{L} denote the training loss and let v = ∂ ℒ / ∂ y ~ ⋆ v=\partial\mathcal{L}/\partial\tilde{y}^{\star} . Applying the implicit function theorem to 𝒜 θ a ​ ( y ~ ⋆ , y ~ 0 ) = 0 \mathcal{A}_{\theta_{a}}(\tilde{y}^{\star},\tilde{y}_{0})=0 gives ∂ ℒ ∂ θ = u ⊤ ∂ 𝒯 θ a ​ ( y ~ ⋆ , y ~ 0 ) ∂ θ , u = ( I − J y ~ ⊤ ) − 1 v , where J y ~ = ∂ 𝒯 θ a ​ ( y ~ , y ~ 0 ) ∂ y ~ | y ~ = y ~ ⋆ . \displaystyle\frac{\partial\mathcal{L}}{\partial\theta}=u^{\top}\frac{\partial\mathcal{T}_{\theta_{a}}(\tilde{y}^{\star},\tilde{y}_{0})}{\partial\theta},\quad u=\left(I-J_{\tilde{y}}^{\top}\right)^{-1}v,\quad\text{where}\quad J_{\tilde{y}}=\left.\frac{\partial\mathcal{T}_{\theta_{a}}(\tilde{y},\tilde{y}_{0})}{\partial\tilde{y}}\right|_{\tilde{y}=\tilde{y}^{\star}}. (4) The derivative with respect to θ = ( θ a , θ b , E ) \theta=(\theta_{a},\theta_{b},E) includes the direct dependence on the attractor parameters θ a \theta_{a} , as well as the dependence on the initialization y ~ 0 = 𝒯 θ b ​ ( E ⁡ ( x ) ) \tilde{y}_{0}=\mathcal{T}_{\theta_{b}}(E(x)) through the backbone parameters θ b \theta_{b} and the tied embedding parameters E E .

Following prior work on implicit models ( Geng et al., 2022 ; Fung et al., 2021 ) , we use the one-step approximation u ≈ v u\approx v . This avoids the extra linear solve for u u and reduces the backward pass to one vector–Jacobian product through 𝒜 θ a \mathcal{A}_{\theta_{a}} . Since we do not backpropagate through every solver step, memory in the attractor block does not grow with the number of forward iterations. In Section 4 , we show that the Anderson solver yields only marginal quality gains, whereas the one-step approximation enables substantially cheaper training.

Remark. Attractor Models are implicit equilibrium models in the spirit of DEQs ( Bai et al., 2019 ) , but the equilibrium plays a different role. Classical DEQs replace the prediction network with a hidden-state equilibrium z ⋆ z^{\star} (single-layer), decoded with a separate output head. We instead keep a standard causal Transformer backbone and add an equilibrium refinement block on top of its prediction state. The fixed point lives directly in the tied embedding space, so every iterate { y 0 , y 1 , … , y ⋆ } \{y_{0},y_{1},\ldots,y^{\star}\} is already a representation in the output space that can be decoded. This gives three practical differences: (i) the solver is initialized from a semantically meaningful proposal y ~ 0 \tilde{y}_{0} rather than from an uninformative state such as zero (as in DEQ), (ii) inference can stop according to a residual tolerance ε \varepsilon rather than a fixed depth or learned halting head, and (iii) DEQ shows that scaling the number of DEQ blocks can harm the performance of their method, whereas we allow for an arbitrary depth backbone transformer and show that we can use a variable number of solver blocks.

Training objective and inference. We train Attractor Models with the standard next-token prediction cross-entropy objective applied to the fixed-point output y ⋆ y^{\star} . Inference reuses the same equilibrium computation. Given an input sequence x x , the backbone first produces the proposal y ~ 0 = 𝒯 θ b ​ ( E ⁡ ( x ) ) \tilde{y}_{0}=\mathcal{T}_{\theta_{b}}(E(x)) , the attractor solver computes y ~ ⋆ \tilde{y}^{\star} , and the tied unembedding decodes y ~ ⋆ \tilde{y}^{\star} into next-token probabilities. Peak memory is bounded by a single forward through the attractor module and standard KV-caching applies in the backbone. In principle, the solver tolerance ε \varepsilon and maximum iteration budget T max T_{\max} are inference-time hyperparameters: they can be adjusted without retraining the model, turning test-time computation into a budget for approaching the learned attractor. Interestingly, however, we find that trained Attractor Models often require very little test-time refinement, as we describe in the next section.

### 3.3 Equilibrium Internalization and Stability in Attractor Models

Although Attractor Models define predictions through the equilibrium y ~ ⋆ \tilde{y}^{\star} , we observe a surprising phenomenon: after training, the backbone proposal y ~ 0 \tilde{y}_{0} often lies close to the equilibrium (c.f. Figures 6 and 7 ). We refer to this phenomenon as equilibrium internalization . Intuitively, the attractor module appears to act as a moving teacher for the backbone, resulting in a form of automatic curriculum. Early in training, the proposal y ~ 0 \tilde{y}_{0} may be far from a good prediction, and the solver must perform nontrivial refinement to reach y ~ ⋆ \tilde{y}^{\star} . Since y ~ 0 \tilde{y}_{0} and y ~ ⋆ \tilde{y}^{\star} live in the same tied output-embedding space, gradients through the equilibrium also train the backbone proposal to move toward the state that the solver would have found. Thus, when the backbone is sufficiently expressive, much of the prediction work can be internalized into y ~ 0 \tilde{y}_{0} , leaving the attractor to perform a stable refinement.

Stability. Equilibrium training also biases the recurrent map toward convergent dynamics. The implicit gradient contains the inverse factor ( I − J y ~ ⊤ ) − 1 (I-J_{\tilde{y}}^{\top})^{-1} , which becomes ill-conditioned near non-contractive regimes. This creates a barrier against unstable fixed-point dynamics, unlike fixed-loop training, which can learn trajectories that are accurate only at a prescribed step count and fail under extra inference-time loops. We discuss this contrast in detail in Appendix B.3 . We refer to Appendix B for theoretical analysis of Attractor Models and comparison with finite-loop models.

## 4 Experiments

We evaluate Attractor Models in two regimes. We first study language modeling across model sizes, comparing against parameter-matched Transformers and looped-LM baselines. We evaluate scaling behavior, downstream accuracy, and training efficiency. We also present results on hard reasoning tasks, where we test whether the same fixed-point refinement mechanism improves small models on problems that require iterative computation.

### 4.1 Attractor Models Improve Large-Scale Language Modeling

Setup. We follow the nanochat ( Karpathy, 2025 ) pretraining recipe used by Parcae ( Prairie et al., 2026 ) for its main Transformer comparison, training on FineWeb-Edu ( Penedo et al., 2024 ) . To ensure a fair comparison, all models are matched in parameter count and trained with the same data budget, optimizer, and learning-rate schedule as the Parcae baselines; the only change is the recurrent block. We compare at three scales: 140M, 370M, and 770M parameters. Parcae is a middle-looped language model with prelude, coda, and recurrent blocks. The stability in this model comes from a linear injection that bounds the spectral radius of the recurrence below one. In contrast, our architecture uses standard Transformer blocks followed by a fixed-point iteration block, and lets the solver itself control the effective depth. Detailed hyperparameter settings are in Appendix C .

Parameter Scaling. We demonstrate how large-scale pretraining scales with our model. We evaluate our method on 140M, 370M, and 770M parameters against a parameter-matched Transformer and Parcae, a looped-language model ( Prairie et al., 2026 ) . Our model improves monotonically with scale. Across all three sizes, our method achieves the best validation PPL, Lambada PPL, and CORE accuracy. These results show that our fixed-point refinement scales cleanly with model size, with especially large gains on Lambada, where iterative refinement substantially improves long-context prediction.

Training efficiency: Lower FLOPs. The one-step IFT backward pass keeps training memory constant in the number of solver iterations. The memory of standard looped language models like ( Prairie et al., 2026 ) scales linearly with the number of loops. The total training FLOPs (Figure 4 ) follow the same trend: although every step of our recurrent block costs roughly the same as Parcae’s, our solver typically converges below ε \varepsilon in well under T max T_{\max} steps, so the realized depth during training is lower despite identical T max T_{\max} , yielding 25–31% lower training FLOPs across scales.

Training efficiency: O(1) memory. An additional advantage of our method is that the training memory required stays constant with the number of iterations (Figure 5 ). This is because our implicit backward pass does not need to store the intermediate activations from every recurrent step. In contrast, standard looped language models must backpropagate through each unrolled iteration, causing memory usage to grow linearly with the number of loops.

### 4.2 Attractor Models Lead to Significant Gains in Hard Reasoning Tasks

Beyond language modeling, we train and evaluate Attractor Models on Sudoku-Extreme and Maze-Hard from ( Wang et al., 2025 ; Jolicoeur-Martineau, 2025 ) : two challenging reasoning benchmarks, where non-recurrent Transformers and most frontier LLMs fail.

Setup. We train small models with approximately 1000 training examples for each task and require predicting the full output grid in a single direct forward pass (no autoregressive decoding). We follow the TRM training protocol ( Jolicoeur-Martineau, 2025 ) , using deep-supervision steps.

Method. TRM carries two latents across deep-supervision steps, a current answer y y and a reasoning state z z , and applies a tiny two-layer network T ⁡ ( n + 1 ) T(n{+}1) times per step to update them. We keep this protocol except for the inner update. Specifically, instead of unrolling T ⁡ ( n + 1 ) T(n{+}1) applications, we solve directly for the fixed point of the ( y , z ) (y,z) update with our solver. The initialization is handled by deep supervision itself: the previous step’s ( y , z ) (y,z) initializes the solver at the next step, with a learned embedding at step zero, so we do not use a separate backbone.

We present our results in Table 2 . The fixed-depth Transformer fails on both tasks. HRM (27M) achieves 55.0% and 74.5%, respectively on Sudoku-Extreme and Maze-Hard. TRM is the strongest tiny baseline at 7M, achieving 74.7% and 85.3%, but (counter to the goal of scaling) collapses to 0% on both tasks when scaled to 27M parameters. Our model scales naturally with parameter count. We attribute the difference to the explicit fixed-point objective, which appears to provide regularization that bare iterative refinement lacks at higher capacity.

For the backward pass, we use the phantom-gradient scheme ( Geng et al., 2022 ) rather than the one-step approximation used in the language-modeling experiments. This choice is important in the small-data reasoning regime: with only ∼ \sim 1,000 training examples and much smaller networks, the solver dynamics are more sensitive, and the one-step surrogate can provide too crude a training signal. This is consistent with TRM, which reports that replacing its backward pass with a one-step approximation reduces Sudoku-Extreme accuracy from 87.4% to 56.5% ( Jolicoeur-Martineau, 2025 ) .

This setup is still an instance of our Attractor Model framework, where an output-space representation is iteratively refined to an equilibrium, decoded, and differentiated through implicitly. The only difference is the initialization mechanism. Rather than a Transformer backbone producing y ~ 0 \tilde{y}_{0} from the input, deep supervision supplies the initialization. Specifically, the previous supervision step’s ( y , z ) (y,z) initializes the solver at the next step, with a learned embedding at step zero.

### 4.3 Equilibrium Internalization and Test-Time Behavior

Fixed-point convergence. Figure 6 visualizes convergence in two complementary ways. First, we project the trajectory of the final-position representation onto its first two principal components over 16 iterations. Our method rapidly contracts to a fixed point: iterations 8–16 collapse onto a single attractor. Parcae also moves toward a stable state, but does so more slowly; its trajectory remains noisier and continues to drift through later recurrences. This suggests that while finite-loop language models can exhibit fixed-point-like behavior, explicitly training the loop as a fixed-point problem produces faster and cleaner convergence. Second, we track the number of solver iterations required during training. The DEQ baseline requires increasingly many iterations as optimization progresses, consistent with the observations in the original work ( Bai et al., 2019 ) . In contrast, Attractor Models rapidly converge to the minimum iteration count and remain stable. This behavior provides evidence for equilibrium internalization, where optimization shifts work from the iterative solver into the backbone proposal.

Test-time iterations vs. quality. In Figure 7 , we report validation perplexity, CORE accuracy, and CORE-Extended accuracy as we vary the number of inference iterations T T while holding training fixed. For Parcae, quality improves monotonically from T = 1 T=1 until it plateaus near T = 8 T=8 , indicating that the model relies on repeated test-time refinement. In contrast, our method reaches peak performance at T = 1 T=1 at every scale, and even T = 0 T=0 (decoding the backbone proposal y ~ 0 \tilde{y}_{0} directly through the tied unembedding) is already at or near the converged value.

We attribute this behavior to equilibrium internalization : during training, the backbone learns to produce a proposal y ~ 0 \tilde{y}_{0} that already lies close to the fixed point that the solver would otherwise compute through iteration. Thus, the iterative block still shapes the learned representation during training, but at inference time the model has largely internalized the result of that refinement into its backbone initialization. Strikingly, the backbone-only readout at T = 0 T=0 is already stronger than larger standard Transformers trained without attractor assistance, and matches or exceeds finite-loop baselines that require many test-time recurrences. Concretely, our 140M model at T = 0 T=0 (no solver) matches or improves Parcae 140M at T = 8 T=8 recurrent steps; the same pattern holds at 370M and 770M.

### 4.4 Ablations

For the ablations, we use a 60.3M-parameter version of our model trained on 1B tokens of FineWeb-Edu under the same nanochat configuration. All ablation runs share the same data stream, tokenizer, and optimizer; only the ablated component varies.

We isolate the contribution of (i) the location of the equilibrium and its initialization (Table 3 ), (ii) the additive injection of c c (Table 4 ), (iii) and the one-step backward approximation (Table 5 ). All ablations train a 60.3M-parameter model on 1B tokens of FineWeb-Edu under the same nanochat setup, with all other hyperparameters fixed.

Comparison to DEQ. Table 3 compares Attractor Models against a parameter-matched DEQ ( Bai et al., 2019 ) . The DEQ baseline solves for a hidden-state equilibrium initialized from an uninformative state and decodes it with a separate output head. Tying the unembedding closes part of the gap (Val. PPL 42.18 → 38.74 42.18\to 38.74 ), but the largest improvement comes from matching the equilibrium to the design of Attractor Models: the fixed point is placed directly in the tied output-embedding space and the root finder is initialized from the backbone proposal y ~ 0 = 𝒯 θ b ​ ( E ⁡ ( x ) ) \tilde{y}_{0}=\mathcal{T}_{\theta_{b}}(E(x)) ( → 34.05 \to 34.05 ).

This proposal gives the solver a meaningful, input-dependent starting point rather than requiring the recurrent block to construct the representation from scratch. As a result, the Attractor Model reaches the same residual tolerance in 1.7 × 1.7\times fewer iterations while also achieving lower perplexity. We view this as evidence of equilibrium internalization : the backbone learns to produce an output-side proposal y ~ 0 \tilde{y}_{0} that already lies close to the eventual equilibrium y ~ ⋆ \tilde{y}^{\star} , making the subsequent attractor refinement both easier and faster.

Proposal injection. Table 4 ablates how the backbone proposal y ~ 0 \tilde{y}_{0} is provided to the attractor. We use proposal injection to denote how y ~ 0 \tilde{y}_{0} enters the recurrent refinement map, and persistent injection to denote providing y ~ 0 \tilde{y}_{0} at every refinement step rather than only through the initial state.

When the proposal is used only for initialization, y ~ t = 0 = y ~ 0 \tilde{y}_{t=0}=\tilde{y}_{0} and y ~ t + 1 = 𝒯 θ a ​ ( y ~ t ) \tilde{y}_{t+1}=\mathcal{T}_{\theta_{a}}(\tilde{y}_{t}) , the recurrent update no longer depends on the input after the first state. Consequently, the fixed point can become proposal-independent, and only 12.4% of validation tokens converge within T max T_{\max} . Persistent injection by concatenation, y ~ t + 1 = 𝒯 θ a ​ ( [ y ~ t ; y ~ 0 ] ) \tilde{y}_{t+1}=\mathcal{T}_{\theta_{a}}([\tilde{y}_{t};\tilde{y}_{0}]) , restores proposal-dependence and recovers much of the quality, but makes the refinement problem harder: convergence is slower (11.2 vs. 8.4 average iterations) and perplexity is worse (36.81 vs. 34.05). Additive proposal injection, y ~ t + 1 = 𝒯 θ a ​ ( y ~ t , y ~ 0 ) \tilde{y}_{t+1}=\mathcal{T}_{\theta_{a}}(\tilde{y}_{t},\tilde{y}_{0}) , provides the backbone proposal at every step while keeping the refinement map simple and well-conditioned, yielding the best results across all three metrics.

Backward pass. In table 5 , we compare the one-step backward approximation against full implicit differentiation (Anderson on the linear system ( I − J y ~ ⊤ ) ​ u = v (I-J_{\tilde{y}}^{\top})u=v ) and the phantom gradient ( Geng et al., 2022 ) unroll. Full IFT improves PPL by only 0.14 while increasing peak training memory by 4.8 × 4.8\times and step time by 2.7 × 2.7\times ; phantom gradient lies in between. The one-step approximation allows relatively cheap training cost while maintaining nearly all of the original performance of a full backward gradient computation.

Initialization ablation. Table 6 isolates the effect of the solver initialization. Starting the attractor solve from an uninformative state, either zero or Gaussian noise, substantially degrades both quality and convergence. In contrast, initializing from the backbone proposal y ~ 0 = 𝒯 θ b ​ ( E ⁡ ( x ) ) \tilde{y}_{0}=\mathcal{T}_{\theta_{b}}(E(x)) gives the solver a meaningful output-side starting point, yielding lower perplexity, fewer iterations, and higher downstream accuracy. This supports our hypothesis that the refinement should begin near a coherent prediction embedding rather than constructing one from scratch.

## 5 Conclusion and Future Work

In this work, we propose Attractor Models, a new family of architectures that first produce meaningful prediction embeddings and then refine them through an attractor module by solving for a fixed point. This formulation makes recurrent refinement stable, memory-efficient, and adaptive, while avoiding the cost of explicit unrolling and achieving strong results across both large-scale language modeling and hard reasoning with tiny models. In stark contrast to prior looped language models, training Attractor Models gives rise to equilibrium internalization: the model learns to make the very refinement procedure that trained it largely unnecessary at inference time. Interesting directions for future work is to further study the equilibrium internalization phenomenon and the differences between Attractor Models and finite-loop recurrence.

Acknowledgements. The authors gratefully acknowledge generous support from Coefficient Giving.

## References

Anderson (1965) D. G. Anderson Iterative procedures for nonlinear integral equations . Journal of the ACM 12 ( 4 ), pp. 547–560 . External Links: Document Cited by: Appendix A , §B.2 .

Anthropic (2024) Anthropic The claude 3 model family: Opus, Sonnet, Haiku . Note: Model card External Links: Link Cited by: §1 .

Bae et al. (2025a) S. Bae, A. Fisch, H. Harutyunyan, Z. Ji, S. Kim, and T. Schuster Relaxed recursive transformers: effective parameter sharing with layer-wise lora . External Links: 2410.20672 , Link Cited by: Appendix A .

Bae et al. (2025b) S. Bae, Y. Kim, R. Bayat, S. Kim, J. Ha, T. Schuster, A. Fisch, H. Harutyunyan, Z. Ji, A. Courville, and S. Yun Mixture-of-recursions: learning dynamic recursive depths for adaptive token-level computation . External Links: 2507.10524 , Link Cited by: Appendix A , §2 .

Bai et al. (2019) S. Bai, J. Z. Kolter, and V. Koltun Deep equilibrium models . In Advances in Neural Information Processing Systems 32 (NeurIPS 2019) , Cited by: Appendix A , §1.1 , §2 , §3.2 , §4.3 , §4.4 , Table 3 .

Bai et al. (2020) S. Bai, V. Koltun, and J. Z. Kolter Multiscale deep equilibrium models . In Advances in Neural Information Processing Systems , Vol. 33 . External Links: Link Cited by: §B.1 .

Bai et al. (2021) S. Bai, V. Koltun, and J. Z. Kolter Stabilizing equilibrium models by jacobian regularization . External Links: 2106.14342 , Link Cited by: §B.2 .

Blayney et al. (2026) H. Blayney, Á. Arroyo, J. Obando-Ceron, P. S. Castro, A. Courville, M. M. Bronstein, and X. Dong A mechanistic analysis of looped reasoning language models . External Links: 2604.11791 , Link Cited by: Appendix A , §B.3.4 , §1.1 , §3 .

Cameron et al. (2026) C. Cameron, W. Wang, N. Ivanov, A. Bhattacharyya, D. Chételat, and Y. Zhang One step forward and k steps back: better reasoning with denoising recursion models . External Links: 2604.18839 , Link Cited by: Appendix A .

Chen et al. (2025) Y. Chen, J. Shang, Z. Zhang, Y. Xie, J. Sheng, T. Liu, S. Wang, Y. Sun, H. Wu, and H. Wang Inner thinking transformer: leveraging dynamic depth scaling to foster adaptive internal thinking . External Links: 2502.13842 , Link Cited by: Appendix A .

Dabre and Fujita (2018) R. Dabre and A. Fujita Recurrent stacking of layers for compact neural machine translation models . External Links: 1807.05353 , Link Cited by: Appendix A .

Dehghani et al. (2019) M. Dehghani, S. Gouws, O. Vinyals, J. Uszkoreit, and Ł. Kaiser Universal transformers . External Links: 1807.03819 , Link Cited by: Appendix A , §1 .

Deng et al. (2025) J. Deng, L. Pang, Z. Wei, S. Xu, Z. Duan, K. Xu, Y. Song, H. Shen, and X. Cheng Latent reasoning in LLMs as a vocabulary-space superposition . arXiv preprint arXiv:2510.15522 . Cited by: §1 .

Deng et al. (2026) J. Deng, Z. Wei, L. Pang, J. Wu, S. Xu, Z. Duan, and H. Shen Latent-GRPO: Group relative policy optimization for latent reasoning . arXiv preprint arXiv:2604.27998 . Cited by: §1 .

Fan et al. (2025) Y. Fan, Y. Du, K. Ramchandran, and K. Lee Looped transformers for length generalization . External Links: 2409.15647 , Link Cited by: §1 .

Fleuret (2025) F. Fleuret The free transformer . External Links: 2510.17558 , Link Cited by: Appendix A .

Fu et al. (2026) T. Fu, Y. You, Z. Chen, G. Dai, H. Yang, and Y. Wang Think-at-hard: selective latent iterations to improve reasoning language models . External Links: 2511.08577 , Link Cited by: Appendix A .

Fung et al. (2021) S. W. Fung, H. Heaton, Q. Li, D. McKenzie, S. Osher, and W. Yin JFB: jacobian-free backpropagation for implicit networks . External Links: 2103.12803 , Link Cited by: Appendix A , §3.2 , Table 5 .

Gatmiry et al. (2024a) K. Gatmiry, N. Saunshi, S. J. Reddi, S. Jegelka, and S. Kumar Can looped transformers learn to implement multi-step gradient descent for in-context learning? . In International Conference on Machine Learning , pp. 15130–15152 . Cited by: Appendix A .

Gatmiry et al. (2024b) K. Gatmiry, N. Saunshi, S. J. Reddi, S. Jegelka, and S. Kumar On the role of depth and looping for in-context learning with task diversity . External Links: 2410.21698 , Link Cited by: Appendix A .

Geiping et al. (2025a) J. Geiping, S. McLeish, N. Jain, J. Kirchenbauer, S. Singh, B. R. Bartoldson, B. Kailkhura, A. Bhatele, and T. Goldstein Scaling up test-time compute with latent reasoning: a recurrent depth approach . External Links: 2502.05171 , Link Cited by: Appendix A , §1 , §1 , §2 , §2 , §3.1 , §3 .

Geiping et al. (2025b) J. Geiping, X. Yang, and G. Su Efficient parallel samplers for recurrent-depth models and their connection to diffusion language models . External Links: 2510.14961 , Link Cited by: Appendix A .

Gemini Team (2023) Gemini Team Gemini: A family of highly capable multimodal models . arXiv preprint arXiv:2312.11805 . Cited by: §1 .

Geng et al. (2022) Z. Geng, X. Zhang, S. Bai, Y. Wang, and Z. Lin On training implicit models . External Links: 2111.05177 , Link Cited by: Appendix A , §3.2 , §4.2 , §4.4 , Table 5 .

Ghugare et al. (2026) R. Ghugare, M. Bortkiewicz, A. Ziarko, and B. Eysenbach On the role of iterative computation in reinforcement learning . External Links: 2602.05999 , Link Cited by: Appendix A .

Giannou et al. (2023a) A. Giannou, S. Rajput, J. Sohn, K. Lee, J. D. Lee, and D. Papailiopoulos Looped transformers as programmable computers . In International Conference on Machine Learning , pp. 11398–11442 . Cited by: §1 .

Giannou et al. (2023b) A. Giannou, S. Rajput, J. Sohn, K. Lee, J. D. Lee, and D. Papailiopoulos Looped transformers as programmable computers . External Links: 2301.13196 , Link Cited by: Appendix A .

Goyal et al. (2026) S. Goyal, S. Agrawal, G. G. Anil, P. Jain, S. Paul, and A. Kusupati ELT: elastic looped transformers for visual generation . External Links: 2604.09168 , Link Cited by: Appendix A .

Grattafiori et al. (2024) A. Grattafiori, A. Dubey, A. Jauhri, A. Pandey, A. Kadian, A. Al-Dahle, A. Letman, A. Mathur, A. Schelten, A. Vaughan, et al. The Llama 3 herd of models . In Neural Information Processing Systems , Cited by: §1 .

Graves (2017) A. Graves Adaptive computation time for recurrent neural networks . External Links: 1603.08983 , Link Cited by: §3 .

Guo et al. (2025) D. Guo, D. Yang, H. Zhang, J. Song, P. Wang, Q. Zhu, R. Xu, R. Zhang, S. Ma, X. Bi, X. Zhang, X. Yu, Y. Wu, Z. F. Wu, Z. Gou, Z. Shao, Z. Li, Z. Gao, A. Liu, B. Xue, B. Wang, B. Wu, B. Feng, C. Lu, C. Zhao, C. Deng, C. Ruan, D. Dai, D. Chen, D. Ji, E. Li, F. Lin, F. Dai, F. Luo, G. Hao, G. Chen, G. Li, H. Zhang, H. Xu, H. Ding, H. Gao, H. Qu, H. Li, J. Guo, J. Li, J. Chen, J. Yuan, J. Tu, J. Qiu, J. Li, J. L. Cai, J. Ni, J. Liang, J. Chen, K. Dong, K. Hu, K. You, K. Gao, K. Guan, K. Huang, K. Yu, L. Wang, L. Zhang, L. Zhao, L. Wang, L. Zhang, L. Xu, L. Xia, M. Zhang, M. Zhang, M. Tang, M. Zhou, M. Li, M. Wang, M. Li, N. Tian, P. Huang, P. Zhang, Q. Wang, Q. Chen, Q. Du, R. Ge, R. Zhang, R. Pan, R. Wang, R. J. Chen, R. L. Jin, R. Chen, S. Lu, S. Zhou, S. Chen, S. Ye, S. Wang, S. Yu, S. Zhou, S. Pan, S. S. Li, S. Zhou, S. Wu, T. Yun, T. Pei, T. Sun, T. Wang, W. Zeng, W. Liu, W. Liang, W. Gao, W. Yu, W. Zhang, W. L. Xiao, W. An, X. Liu, X. Wang, X. Chen, X. Nie, X. Cheng, X. Liu, X. Xie, X. Liu, X. Yang, X. Li, X. Su, X. Lin, X. Q. Li, X. Jin, X. Shen, X. Chen, X. Sun, X. Wang, X. Song, X. Zhou, X. Wang, X. Shan, Y. K. Li, Y. Q. Wang, Y. X. Wei, Y. Zhang, Y. Xu, Y. Li, Y. Zhao, Y. Sun, Y. Wang, Y. Yu, Y. Zhang, Y. Shi, Y. Xiong, Y. He, Y. Piao, Y. Wang, Y. Tan, Y. Ma, Y. Liu, Y. Guo, Y. Ou, Y. Wang, Y. Gong, Y. Zou, Y. He, Y. Xiong, Y. Luo, Y. You, Y. Liu, Y. Zhou, Y. X. Zhu, Y. Huang, Y. Li, Y. Zheng, Y. Zhu, Y. Ma, Y. Tang, Y. Zha, Y. Yan, Z. Z. Ren, Z. Ren, Z. Sha, Z. Fu, Z. Xu, Z. Xie, Z. Zhang, Z. Hao, Z. Ma, Z. Yan, Z. Wu, Z. Gu, Z. Zhu, Z. Liu, Z. Li, Z. Xie, Z. Song, Z. Pan, Z. Huang, Z. Xu, Z. Zhang, and Z. Zhang DeepSeek-r1 incentivizes reasoning in llms through reinforcement learning . Nature 645 ( 8081 ), pp. 633–638 . External Links: ISSN 1476-4687 , Link , Document Cited by: §1 .

Han (2026) S. Han Hierarchical vs. flat iteration in shared-weight transformers . External Links: 2604.14442 , Link Cited by: Appendix A .

Hao et al. (2025) S. Hao, S. Sukhbaatar, D. Su, X. Li, Z. Hu, J. Weston, and Y. Tian Training large language models to reason in a continuous latent space . External Links: 2412.06769 , Link Cited by: Appendix A , §1 .

Hu et al. (2025) E. S. Hu, K. Ahn, Q. Liu, H. Xu, M. Tomar, A. Langford, J. Teoh, B. Xu, D. Yan, D. Jayaraman, A. Lamb, and J. Langford The belief state transformer . External Links: 2410.23506 , Link Cited by: Appendix A .

Huang et al. (2025) J. Huang, Z. Wang, and J. D. Lee Transformers learn to implement multi-step gradient descent with chain of thought . External Links: 2502.21212 , Link Cited by: Appendix A .

Inan et al. (2017) H. Inan, K. Khosravi, and R. Socher Tying word vectors and word classifiers: a loss framework for language modeling . External Links: 1611.01462 , Link Cited by: Appendix A .

Jeddi et al. (2026) A. Jeddi, M. Ciccone, and B. Taati LoopFormer: elastic-depth looped transformers for latent reasoning via shortcut modulation . External Links: 2602.11451 , Link Cited by: Appendix A .

Jolicoeur-Martineau (2025) A. Jolicoeur-Martineau Less is more: recursive reasoning with tiny networks . External Links: 2510.04871 , Link Cited by: Appendix A , §1 , §1 , §2 , §4.2 , §4.2 , §4.2 .

Kaiser and Sutskever (2016) Ł. Kaiser and I. Sutskever Neural gpus learn algorithms . External Links: 1511.08228 , Link Cited by: Appendix A .

Karpathy (2025) A. Karpathy Nanochat: the best chatgpt that $100 can buy . GitHub . External Links: Link Cited by: §4.1 .

Knupp et al. (2026a) J. Knupp, J. H. Metzen, J. Bohn, G. Groh, and K. Kersting Depth-Recurrent Attention Mixtures: Giving latent reasoning the attention it deserves . arXiv preprint arXiv:2601.21582 . Cited by: Appendix A .

Knupp et al. (2026b) J. Knupp, J. H. Metzen, J. Bohn, G. Groh, and K. Kersting Depth-recurrent attention mixtures: giving latent reasoning the attention it deserves . External Links: 2601.21582 , Link Cited by: Appendix A .

Kohli et al. (2026) H. Kohli, S. Parthasarathy, H. Sun, and Y. Yao Loop, think, & generalize: implicit reasoning in recurrent-depth transformers . External Links: 2604.07822 , Link Cited by: §1 .

Komisarczyk et al. (2026) M. Komisarczyk, S. Mathur, M. Kraus, S. Natarajan, and K. Kersting Recursive inference machines for neural reasoning . External Links: 2603.05234 , Link Cited by: Appendix A .

Krantz and Parks (2002a) S. G. Krantz and H. R. Parks The implicit function theorem: history, theory, and applications . Birkhäuser , Boston, MA . External Links: Document , ISBN 978-0-8176-4285-3 Cited by: §B.1 .

Krantz and Parks (2002b) S. G. Krantz and H. R. Parks The implicit function theorem: history, theory, and applications . Vol. 202 , Springer . Cited by: §3.2 .

Labovich (2026a) A. Labovich Stability and generalization in looped transformers . External Links: 2604.15259 , Link Cited by: Appendix A .

Labovich (2026b) A. Labovich Stability and generalization in looped transformers . External Links: 2604.15259 , Link Cited by: Appendix A , §1 .

Lan et al. (2020) Z. Lan, M. Chen, S. Goodman, K. Gimpel, P. Sharma, and R. Soricut ALBERT: a lite bert for self-supervised learning of language representations . External Links: 1909.11942 , Link Cited by: Appendix A .

[50] S. M. McLeish, A. Li, J. Kirchenbauer, D. S. Kalra, B. R. Bartoldson, B. Kailkhura, A. Schwarzschild, J. Geiping, M. Goldblum, and T. Goldstein Teaching pretrained language models to think deeper with retrofitted recurrence . In NeurIPS 2025 Workshop on Efficient Reasoning , Cited by: Appendix A , §2 .

Merrill and Sabharwal (2026) W. Merrill and A. Sabharwal A little depth goes a long way: The expressive power of log-depth transformers . Advances in Neural Information Processing Systems 38 , pp. 95315–95339 . Cited by: Appendix A .

Merrill and Sabharwal (2025) W. Merrill and A. Sabharwal A little depth goes a long way: the expressive power of log-depth transformers . External Links: 2503.03961 , Link Cited by: Appendix A .

Mohtashami et al. (2023) A. Mohtashami, M. Pagliardini, and M. Jaggi CoTFormer: More tokens with attention make up for less depth . In Workshop on Advancing Neural Network Training: Computational Efficiency, Scalability, and Resource Optimization (WANT@ NeurIPS 2023) , Cited by: §1 .

Moosa et al. (2026) I. M. Moosa, S. Lohit, Y. Wang, M. Chatterjee, and W. Yin Understanding dynamic compute allocation in recurrent transformers . External Links: 2602.08864 , Link Cited by: Appendix A .

OpenAI (2023) OpenAI GPT-4 technical report . arXiv preprint arXiv:2303.08774 . Cited by: §1 .

Özeren and Aßenmacher (2025) E. Özeren and M. Aßenmacher Reinforcement learning for latent-space thinking in LLMs . arXiv preprint arXiv:2512.11816 . Cited by: §1 .

Paperno et al. (2016) D. Paperno, G. Kruszewski, A. Lazaridou, N. Q. Pham, R. Bernardi, S. Pezzelle, M. Baroni, G. Boleda, and R. Fernández The LAMBADA dataset: word prediction requiring a broad discourse context . In Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , Berlin, Germany , pp. 1525–1534 . External Links: Document , Link Cited by: §1.1 .

Pappone et al. (2025) F. Pappone, D. Crisostomi, and E. Rodolà Two-scale latent dynamics for recurrent-depth transformers . External Links: 2509.23314 , Link Cited by: Appendix A .

Penedo et al. (2024) G. Penedo, H. Kydlíček, L. B. allal, A. Lozhkov, M. Mitchell, C. Raffel, L. V. Werra, and T. Wolf The fineweb datasets: decanting the web for the finest text data at scale . External Links: 2406.17557 , Link Cited by: §4.1 .

Prairie et al. (2026) H. Prairie, Z. Novack, T. Berg-Kirkpatrick, and D. Y. Fu Parcae: scaling laws for stable looped language models . External Links: 2604.12946 , Link Cited by: Appendix A , §1.1 , §1 , §2 , §2 , §3.1 , §3 , §4.1 , §4.1 , §4.1 .

Press and Wolf (2017) O. Press and L. Wolf Using the output embedding to improve language models . In Proceedings of the 15th Conference of the European Chapter of the Association for Computational Linguistics: Volume 2, Short Papers , pp. 157–163 . Cited by: Appendix A .

Rauba et al. (2026) P. Rauba, C. Fanconi, and M. van der Schaar Tiny autoregressive recursive models . External Links: 2603.08082 , Link Cited by: Appendix A .

Rizvi-Martel et al. (2026) M. Rizvi-Martel, G. Rabusseau, and M. Mosbach The illusion of superposition? A principled analysis of latent thinking in language models . arXiv preprint arXiv:2604.06374 . Cited by: §1 .

Sapunov (2026a) G. Sapunov Universal transformers need memory: depth-state trade-offs in adaptive recursive reasoning . External Links: 2604.21999 , Link Cited by: Appendix A .

Sapunov (2026b) G. Sapunov Universal transformers need memory: depth-state trade-offs in adaptive recursive reasoning . External Links: 2604.21999 , Link Cited by: Appendix A .

Saunshi et al. (2025a) N. Saunshi, N. Dikkala, Z. Li, S. Kumar, and S. J. Reddi Reasoning with latent thoughts: on the power of looped transformers . External Links: 2502.17416 , Link Cited by: Appendix A , §1 .

Saunshi et al. (2025b) N. Saunshi, N. Dikkala, Z. Li, S. Kumar, and S. J. Reddi Reasoning with latent thoughts: on the power of looped transformers . External Links: 2502.17416 , Link Cited by: Appendix A .

Song et al. (2026a) S. Song, H. Li, Z. Wang, B. Zeng, F. Song, Y. Wang, Z. J. Xu, Z. He, and Z. Lin AdaPonderLM: Gated pondering language models with token-wise adaptive depth . arXiv preprint arXiv:2603.01914 . Cited by: Appendix A .

Song et al. (2026b) S. Song, H. Li, Z. Wang, B. Zeng, F. Song, Y. Wang, Z. J. Xu, Z. He, and Z. Lin AdaPonderLM: gated pondering language models with token-wise adaptive depth . External Links: 2603.01914 , Link Cited by: Appendix A .

Takase and Kiyono (2023) S. Takase and S. Kiyono Lessons on parameter sharing across layers in transformers . External Links: 2104.06022 , Link Cited by: Appendix A .

Tang et al. (2026) G. Tang, S. Jiang, H. Chang, N. Chen, Y. Li, H. Fan, J. Li, M. Liu, and B. Qin LoopRPT: reinforcement pre-training for looped language models . External Links: 2603.19714 , Link Cited by: Appendix A .

Teoh et al. (2025) J. Teoh, M. Tomar, K. Ahn, E. S. Hu, P. Sharma, R. Islam, A. Lamb, and J. Langford Next-latent prediction transformers learn compact world models . External Links: 2511.05963 , Link Cited by: Appendix A .

Tur et al. (2026) Y. Tur, J. Naghiyev, H. Fang, W. Tsai, J. Duan, D. Fox, and R. Krishna Recurrent-depth vla: implicit test-time compute scaling of vision-language-action models via latent iterative reasoning . External Links: 2602.07845 , Link Cited by: Appendix A .

Vaswani et al. (2017) A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. Kaiser, and I. Polosukhin Attention is all you need . In Advances in Neural Information Processing Systems 30 , pp. 5998–6008 . Cited by: §1 .

Wang et al. (2025) G. Wang, J. Li, Y. Sun, X. Chen, C. Liu, Y. Wu, M. Lu, S. Song, and Y. A. Yadkori Hierarchical reasoning model . External Links: 2506.21734 , Link Cited by: Appendix A , §1 , §4.2 .

Wei et al. (2023) J. Wei, X. Wang, D. Schuurmans, M. Bosma, B. Ichter, F. Xia, E. Chi, Q. Le, and D. Zhou Chain-of-thought prompting elicits reasoning in large language models . External Links: 2201.11903 , Link Cited by: §1 .

Wei et al. (2025) X. Wei, X. Liu, Y. Zang, X. Dong, Y. Cao, J. Wang, X. Qiu, and D. Lin SIM-cot: supervised implicit chain-of-thought . External Links: 2509.20317 , Link Cited by: §1 .

Williams and Tureci (2026) J. Williams and E. Tureci Prioritize the process, not just the outcome: rewarding latent thought trajectories improves reasoning in looped language models . External Links: 2602.10520 , Link Cited by: Appendix A .

Wu et al. (2025) B. Wu, M. Chen, X. Luo, S. Yan, Q. Yu, F. Xia, T. Zhang, H. Zhan, Z. Zhong, X. Zhou, S. Qiao, and X. Bin Parallel loop transformer for efficient test-time computation scaling . External Links: 2510.24824 , Link Cited by: Appendix A .

Xu and Sato (2025a) K. Xu and I. Sato On expressive power of looped transformers: theoretical analysis and enhancement via timestep encoding . External Links: 2410.01405 , Link Cited by: Appendix A .

Xu and Sato (2025b) K. Xu and I. Sato On expressive power of looped transformers: theoretical analysis and enhancement via timestep encoding . External Links: 2410.01405 , Link Cited by: Appendix A .

Xu and Sato (2026) K. Xu and I. Sato A formal comparison between chain of thought and latent thought . External Links: 2509.25239 , Link Cited by: Appendix A .

Yang et al. (2024a) L. Yang, K. Lee, R. Nowak, and D. Papailiopoulos Looped transformers are better at learning learning algorithms . External Links: 2311.12424 , Link Cited by: Appendix A , §1 .

Yang et al. (2024b) L. Yang, K. Lee, R. Nowak, and D. Papailiopoulos Looped transformers are better at learning learning algorithms . External Links: 2311.12424 , Link Cited by: §1 .

Yang et al. (2024c) L. Yang, K. Lee, R. Nowak, and D. Papailiopoulos Looped transformers are better at learning learning algorithms . External Links: 2311.12424 , Link Cited by: Appendix A .

Zeitoun et al. (2026a) A. Zeitoun, L. Torroba-Hennigen, and Y. Kim Hyperloop transformers . arXiv preprint arXiv:2604.21254 . Cited by: Appendix A .

Zeitoun et al. (2026b) A. Zeitoun, L. Torroba-Hennigen, and Y. Kim Hyperloop transformers . External Links: 2604.21254 , Link Cited by: Appendix A .

Zeng et al. (2026) B. Zeng, S. Song, S. Huang, Y. Wang, H. Li, Z. He, X. Wang, Z. Li, and Z. Lin PonderLM: pretraining language models to ponder in continuous space . External Links: 2505.20674 , Link Cited by: Appendix A .

[89] X. Zhang, H. Wu, G. He, J. Shen, B. Lyu, and Z. Zhu MoDr: Mixture-of-depth-recurrent transformers for test-time reasoning . In The Fourteenth International Conference on Learning Representations , Cited by: Appendix A .

Zhang et al. (2026) X. Zhang, H. Wu, G. He, J. Shen, B. Lyu, and Z. Zhu MoDr: mixture-of-depth-recurrent transformers for test-time reasoning . In The Fourteenth International Conference on Learning Representations , External Links: Link Cited by: Appendix A .

[91] Y. Zheng, X. Wang, L. Ren, and C. Wei ChainGPT: Dual-reasoning model with recurrent depth and multi-rank state updates . In The Fourteenth International Conference on Learning Representations , Cited by: Appendix A .

Zheng et al. (2026) Y. Zheng, X. Wang, L. Ren, and C. Wei ChainGPT: dual-reasoning model with recurrent depth and multi-rank state updates . In The Fourteenth International Conference on Learning Representations , External Links: Link Cited by: Appendix A .

Zhou et al. (2025) C. Zhou, C. Yang, Y. Hu, C. Wang, C. Zhang, M. Zhang, L. Mackey, T. Jaakkola, S. Bates, and D. Zhang Coevolutionary continuous discrete diffusion: make your diffusion language model a latent reasoner . arXiv preprint arXiv:2510.03206 . Cited by: Appendix A .

Zhu et al. (2026) H. Zhu, S. Hao, Z. Hu, J. Jiao, S. J. Russell, and Y. Tian Reasoning by superposition: A theoretical perspective on chain of continuous thought . Advances in Neural Information Processing Systems 38 , pp. 79931–79963 . Cited by: §1 .

Zhu et al. (2025a) H. Zhu, S. Hao, Z. Hu, J. Jiao, S. Russell, and Y. Tian Emergence of superposition: Unveiling the training dynamics of chain of continuous thought . arXiv preprint arXiv:2509.23365 . Cited by: Appendix A .

Zhu et al. (2025b) H. Zhu, S. Hao, Z. Hu, J. Jiao, S. Russell, and Y. Tian Reasoning by superposition: a theoretical perspective on chain of continuous thought . External Links: 2505.12514 , Link Cited by: Appendix A .

Zhu et al. (2025c) R. Zhu, Z. Wang, K. Hua, T. Zhang, Z. Li, H. Que, B. Wei, Z. Wen, F. Yin, H. Xing, L. Li, J. Shi, K. Ma, S. Li, T. Kergan, A. Smith, X. Qu, M. Hui, B. Wu, Q. Min, H. Huang, X. Zhou, W. Ye, J. Liu, J. Yang, Y. Shi, C. Lin, E. Zhao, T. Cai, G. Zhang, W. Huang, Y. Bengio, and J. Eshraghian Scaling latent reasoning via looped language models . External Links: 2510.25741 , Link Cited by: Appendix A , Appendix A , §B.2 , §1 , §1 , §2 , §2 , §3 .

## Appendix A Related Work

Looped and recurrent language models. Weight-tied recurrence has re-emerged as an alternative to deeper feed-forward stacks ( Press and Wolf, 2017 ; Inan et al., 2017 ; Kaiser and Sutskever, 2016 ; Lan et al., 2020 ; Dabre and Fujita, 2018 ; Takase and Kiyono, 2023 ; Bae et al., 2025a ) . Universal Transformers share a single block across depth ( Dehghani et al., 2019 ; Sapunov, 2026a ; Sapunov, 2026b ) , while looped and recurrent language models iterate a recurrent update on a hidden state to enable latent reasoning ( Zhu et al., 2025c ; Prairie et al., 2026 ; Geiping et al., 2025a ; Bae et al., 2025b ; Zheng et al., ; Zhang et al., ; Song et al., 2026a ; Knupp et al., 2026a ; Zeitoun et al., 2026a ; McLeish et al., ; Zheng et al., 2026 ; Zhang et al., 2026 ; Song et al., 2026b ; Moosa et al., 2026 ; Knupp et al., 2026b ; Wu et al., 2025 ; Zeitoun et al., 2026b ; Pappone et al., 2025 ; Rauba et al., 2026 ; Zeng et al., 2026 ; Tur et al., 2026 ; Komisarczyk et al., 2026 ; Ghugare et al., 2026 ; Cameron et al., 2026 ; Williams and Tureci, 2026 ; Han, 2026 ; Goyal et al., 2026 ; Tang et al., 2026 ) . Latent (implicit) reasoning methods such as Coconut ( Hao et al., 2025 ) and related methods ( Teoh et al., 2025 ; Chen et al., 2025 ; Xu and Sato, 2026 ; Jeddi et al., 2026 ; Fu et al., 2026 ; Zhou et al., 2025 ; Geiping et al., 2025b ; Hu et al., 2025 ; Fleuret, 2025 ) perform reasoning in continuous representation space rather than through chain-of-thought tokens. These approaches unroll the loop for a fixed number of steps at training time, causing training memory to grow linearly in depth, coupling inference iterations to training, and often degrading quality when iterations are extended at test time ( Zhu et al., 2025c ) . From theoretical and mechanistic analysis perspectives, looped and continuous thinking models have shown to offer benefits over non-recurrent models ( Yang et al., 2024a ; Labovich, 2026b ; Saunshi et al., 2025a ; Xu and Sato, 2025a ; Saunshi et al., 2025b ; Giannou et al., 2023b ; Yang et al., 2024c ; Gatmiry et al., 2024b ; Huang et al., 2025 ; Xu and Sato, 2025b ; Merrill and Sabharwal, 2025 ; Labovich, 2026a ; Zhu et al., 2025b ; Zhu et al., 2025a ; Gatmiry et al., 2024a ; Merrill and Sabharwal, 2026 ) . Mechanistic analysis shows that the recurrent updates of looped LMs in fact converge to a fixed point for the vast majority of tokens, directly motivating our formulation ( Blayney et al., 2026 ) .

Implicit fixed-point models. Deep Equilibrium Models (DEQs) replace finite unrolling with a fixed-point equation z ⋆ = f θ ​ ( z ⋆ , x ) z^{\star}=f_{\theta}(z^{\star},x) and train through it via implicit differentiation, decoupling effective depth from training memory ( Bai et al., 2019 ) . Solvers typically use Anderson acceleration ( Anderson, 1965 ) , with backward passes ranging from full implicit differentiation to cheap surrogates such as one-step ( Fung et al., 2021 ) and phantom ( Geng et al., 2022 ) gradients. Standard DEQs solve for a hidden state initialized from zero and decode through a separate output head. In Attractor Models, the equilibrium instead lives in the tied output-embedding space and is warm-started from a meaningful backbone prediction; we find this structure essential for stable training at language-modeling scale and show it gives rise to equilibrium internalization (Section 4.3 ).

Tiny recursive reasoners. On small-data algorithmic benchmarks such as Sudoku and maze solving, hierarchical and tiny recursive networks (HRM, TRM) ( Wang et al., 2025 ; Jolicoeur-Martineau, 2025 ) achieve strong accuracy with few parameters, but exhibit a “less is more” behavior where performance collapses as model size grows ( Jolicoeur-Martineau, 2025 ) . Attractor Models retain the iterative-refinement benefit of these architectures while scaling cleanly with parameter count).

Positioning. Looped LMs couple three quantities through unrolled BPTT: inference depth, training depth, and training memory ( Zhu et al., 2025c ) . Attractor Models decouple all three: the equilibrium is defined by a residual equation in output-embedding space, the number of solver evaluations is chosen adaptively by tolerance ε \varepsilon , and training memory in the recurrent block is constant in effective depth. Empirically, this combines the strengths of feed-forward and recurrent models—better perplexity than parameter-matched Transformers, 25–31% lower training FLOPs and constant memory relative to looped LMs, and clean scaling on hard reasoning where specialized recursive networks collapse.

## Appendix B Theory of Looped and Attractor Models

### B.1 Well-posedness and the implicit gradient

Fix an input x x and parameters θ \theta . Throughout this section, we write F ⁡ ( y ) ≜ f θ ​ ( y , E ⁡ ( x ) ) F(y)\triangleq f_{\theta}(y,E(x)) for brevity, so that the fixed-point equation y ⋆ = f θ ​ ( y ⋆ , E ⁡ ( x ) ) y^{\star}=f_{\theta}(y^{\star},E(x)) becomes y ⋆ = F ⁡ ( y ⋆ ) y^{\star}=F(y^{\star}) . Let J F ​ ( y ) ≜ ∂ F / ∂ y J_{F}(y)\triangleq\partial F/\partial y denote the Jacobian of F F with respect to its state input. We work in a generic norm ∥ ⋅ ∥ \|\cdot\| on ℝ L × d \mathbb{R}^{L\times d} and its induced operator norm; for concreteness, can take both to be Frobenius and spectral, respectively. Assumptions are borrowed from ( Bai et al., 2020 ; Krantz and Parks, 2002a ) .

###### Assumption 1 (Local contraction) .

There exist a point y ¯ ∈ ℝ L × d \bar{y}\in\mathbb{R}^{L\times d} , a radius r > 0 r>0 , and a constant L ∈ [ 0 , 1 ) L\in[0,1) such that 1. F F maps the closed ball B r ​ ( y ¯ ) ≜ { y : ‖ y − y ¯ ‖ ≤ r } B_{r}(\bar{y})\triangleq\{y:\|y-\bar{y}\|\leq r\} into itself, and

2. F F is L L -Lipschitz on B r ​ ( y ¯ ) B_{r}(\bar{y}) : ‖ F ⁡ ( y ) − F ⁡ ( y ′ ) ‖ ≤ L ​ ‖ y − y ′ ‖ for all ​ y , y ′ ∈ B r ​ ( y ¯ ) . \|F(y)-F(y^{\prime})\|\;\leq\;L\,\|y-y^{\prime}\|\qquad\text{for all }y,y^{\prime}\in B_{r}(\bar{y}).

When F F is continuously differentiable, a sufficient form of (ii) is sup y ∈ B r ​ ( y ¯ ) ‖ J F ​ ( y ) ‖ ≤ L \sup_{y\in B_{r}(\bar{y})}\|J_{F}(y)\|\leq L .

###### Theorem 1 (Well-posedness and implicit gradient) .

Under Assumption 1 , the following hold. 1. Existence and uniqueness: There is a unique y ⋆ ∈ B r ​ ( y ¯ ) y^{\star}\in B_{r}(\bar{y}) with y ⋆ = F ⁡ ( y ⋆ ) y^{\star}=F(y^{\star}) .

2. The picard iteration converges linearly: For any y 0 ∈ B r ​ ( y ¯ ) y_{0}\in B_{r}(\bar{y}) , the iterates y k + 1 = F ⁡ ( y k ) y_{k+1}=F(y_{k}) remain in B r ​ ( y ¯ ) B_{r}(\bar{y}) and satisfy ‖ y k − y ⋆ ‖ ≤ L k ​ ‖ y 0 − y ⋆ ‖ . \|y_{k}-y^{\star}\|\;\leq\;L^{k}\,\|y_{0}-y^{\star}\|. (5)

3. Validity of the implicit gradient: If F F is continuously differentiable on B r ​ ( y ¯ ) B_{r}(\bar{y}) , then I − J F ​ ( y ⋆ ) I-J_{F}(y^{\star}) is invertible, y ⋆ y^{\star} depends continuously differentiably on θ \theta in a neighborhood of the current parameters, and ∂ y ⋆ ∂ θ = ( I − J F ​ ( y ⋆ ) ) − 1 ​ ∂ f θ ∂ θ | y ⋆ . \frac{\partial y^{\star}}{\partial\theta}\;=\;\bigl(I-J_{F}(y^{\star})\bigr)^{-1}\left.\frac{\partial f_{\theta}}{\partial\theta}\right|_{y^{\star}}. (6)

###### Proof.

Parts (i) and (ii) follow from the Banach fixed-point theorem applied to the contraction F F on the closed (hence complete) ball B r ( y ¯ ) ⊂ ( ℝ L × d , ∥ ⋅ ∥ ) B_{r}(\bar{y})\subset(\mathbb{R}^{L\times d},\|\cdot\|) .

For (iii), Lipschitz continuity with constant L L gives ‖ J F ​ ( y ⋆ ) ‖ ≤ L < 1 \|J_{F}(y^{\star})\|\leq L<1 , so the spectral radius satisfies ρ ⁡ ( J F ​ ( y ⋆ ) ) ≤ ‖ J F ​ ( y ⋆ ) ‖ < 1 \rho(J_{F}(y^{\star}))\leq\|J_{F}(y^{\star})\|<1 . The Neumann series ∑ k ≥ 0 J F ​ ( y ⋆ ) k \sum_{k\geq 0}J_{F}(y^{\star})^{k} therefore converges to ( I − J F ​ ( y ⋆ ) ) − 1 (I-J_{F}(y^{\star}))^{-1} , and in particular I − J F ​ ( y ⋆ ) I-J_{F}(y^{\star}) is invertible. Define G ⁡ ( y , θ ) ≜ f θ ​ ( y , E ⁡ ( x ) ) − y G(y,\theta)\triangleq f_{\theta}(y,E(x))-y , which is C 1 C^{1} in both arguments and satisfies G ⁡ ( y ⋆ , θ ) = 0 G(y^{\star},\theta)=0 with

∂ G ∂ y | y ⋆ = J F ​ ( y ⋆ ) − I , \left.\frac{\partial G}{\partial y}\right|_{y^{\star}}\;=\;J_{F}(y^{\star})-I, (7)

which is invertible. The implicit function theorem applied to G = 0 G=0 yields a unique C 1 C^{1} map θ ↦ y ⋆ ​ ( θ ) \theta\mapsto y^{\star}(\theta) in a neighborhood of the current parameters, with

∂ y ⋆ ∂ θ = − ( ∂ G ∂ y ) − 1 ​ ∂ G ∂ θ = ( I − J F ​ ( y ⋆ ) ) − 1 ​ ∂ f θ ∂ θ | y ⋆ . \frac{\partial y^{\star}}{\partial\theta}\;=\;-\left(\frac{\partial G}{\partial y}\right)^{-1}\frac{\partial G}{\partial\theta}\;=\;\bigl(I-J_{F}(y^{\star})\bigr)^{-1}\left.\frac{\partial f_{\theta}}{\partial\theta}\right|_{y^{\star}}. (8)

∎

Equation ( 6 ) is exactly the gradient computed in the backward pass of Section 3 . The linear solve is convergent for the same reason: since ‖ J F ⊤ ​ ( y ⋆ ) ‖ = ‖ J F ​ ( y ⋆ ) ‖ ≤ L < 1 \|J_{F}^{\top}(y^{\star})\|=\|J_{F}(y^{\star})\|\leq L<1 , the Neumann iteration u ← J F ⊤ ​ ( y ⋆ ) ​ u + v u\leftarrow J_{F}^{\top}(y^{\star})\,u+v converges geometrically with rate L L to the unique solution u = ( I − J F ⊤ ​ ( y ⋆ ) ) − 1 ​ v u=(I-J_{F}^{\top}(y^{\star}))^{-1}v .

### B.2 Looped language models are fixed-point iterators

A LoopLM ( Zhu et al., 2025c ) of depth T T with the same weight-tied block f θ f_{\theta} and warm start y 0 = E ⁡ ( x ) y_{0}=E(x) produces y T loop ≜ F ( T ) ​ ( E ⁡ ( x ) ) = F ∘ F ∘ ⋯ ∘ F ⏟ T ​ times ​ ( E ⁡ ( x ) ) . y_{T}^{\mathrm{loop}}\;\triangleq\;F^{(T)}\bigl(E(x)\bigr)\;=\;\underbrace{F\circ F\circ\cdots\circ F}_{T\text{ times}}\bigl(E(x)\bigr). (9)

This is exactly T T Picard iterations of our residual g θ ​ ( ⋅ , x ) g_{\theta}(\cdot,x) warm-started from the input embedding. See the following corollary:

###### Corollary 1 (LoopLM as a truncated approximation) .

Suppose Assumption 1 holds and the warm start E ​ ( x ) ∈ B r ​ ( y ¯ ) E(x)\in B_{r}(\bar{y}) . Then for every T ≥ 0 T\geq 0 , ‖ y T loop − y ⋆ ‖ ≤ L T ​ ‖ E ⁡ ( x ) − y ⋆ ‖ . \|y_{T}^{\mathrm{loop}}-y^{\star}\|\;\leq\;L^{T}\,\|E(x)-y^{\star}\|. (10) In particular, y T loop → y ⋆ y_{T}^{\mathrm{loop}}\to y^{\star} as T → ∞ T\to\infty , and the discrepancy between a LoopLM of depth T T and our model decays geometrically in T T .

###### Proof.

Apply Theorem 1 (ii) with y 0 = E ⁡ ( x ) y_{0}=E(x) . ∎

Two consequences are worth highlighting:

The limit: Our fixed-point model is the T → ∞ T\to\infty limit of LoopLM with shared parameters. Training a LoopLM at any finite depth T T implicitly trains an approximation to the same equilibrium y ⋆ y^{\star} , with the approximation error controlled by ( 10 ).

The iteration count at inference: Picard iteration converges at the linear rate L L . Our forward pass uses Anderson acceleration, which under standard regularity conditions converges superlinearly near y ⋆ y^{\star} ( Anderson, 1965 ) . To reach a target residual tolerance ε \varepsilon , the root finder therefore typically requires fewer evaluations of f θ f_{\theta} than the unroll depth T T a LoopLM would need for a comparable residual. The exact crossover depends on L L and on the solver hyperparameters.

Caveat: Assumption 1 is local and is not guaranteed to hold for an arbitrarily trained transformer block. In our experiments, we generally notice that ‖ J F ​ ( y ⋆ ) ‖ ≤ L < 1 \|J_{F}(y^{\star})\|\leq L<1 , the authors of DEQ also find that using a regularizer on the Jacobian to enforce this helps ( Bai et al., 2021 ) .

### B.3 Where looped language models fall short

#### B.3.1 Attractor Models

The initialization y ~ 0 \tilde{y}_{0} and the fixed point y ~ ⋆ \tilde{y}^{\star} live in the same tied output-embedding space, so either can be decoded by the unembedding E ⊤ E^{\top} . The loss depends only on y ~ ⋆ \tilde{y}^{\star} , and the implicit gradient with respect to the backbone parameters is ∇ θ b ℒ = u ⊤ ​ J y ~ 0 ​ ∇ θ b y ~ 0 , u = ( I − J y ~ ⊤ ) − 1 ​ v . \nabla_{\theta_{b}}\mathcal{L}\;=\;u^{\top}J_{\tilde{y}_{0}}\,\nabla_{\theta_{b}}\tilde{y}_{0},\qquad u=(I-J_{\tilde{y}}^{\top})^{-1}v. Thus, the loss may be viewed as a function of the backbone’s output embedding: perturbations in y ~ 0 \tilde{y}_{0} affect ℒ \mathcal{L} by perturbing y ~ ⋆ \tilde{y}^{\star} in the same space. The backbone is therefore optimized as a standalone next-token predictor whose embedding is decoded by E ⊤ E^{\top} .

When the backbone has strictly greater capacity than the weight-tied attractor, the joint optimum places the prediction work in the backbone. Consequently, y ~ 0 ​ ( x , θ b ⋆ ) \tilde{y}_{0}(x;\theta_{b}^{\star}) approaches the loss-minimizing embedding. The fixed-point constraint 𝒯 θ a ⋆ ​ ( y ~ ⋆ , y ~ 0 ) = y ~ ⋆ \mathcal{T}_{\theta_{a}^{\star}}(\tilde{y}^{\star},\tilde{y}_{0})=\tilde{y}^{\star} is then consistent only when y ~ ⋆ = y ~ 0 \tilde{y}^{\star}=\tilde{y}_{0} , yielding 𝒯 θ a ⋆ ​ ( y ~ 0 , y ~ 0 ) = y ~ 0 . \mathcal{T}_{\theta_{a}^{\star}}(\tilde{y}_{0},\tilde{y}_{0})=\tilde{y}_{0}.

#### B.3.2 Standard looped LMs

In standard looped language models, the latent initialization h 0 h_{0} is uninformative, typically zero or noise, and occupies the role of a hidden state rather than an output embedding. Decoding h 0 ​ E ⊤ h_{0}E^{\top} is therefore not meaningful.

Gradients instead flow by backpropagation through time along the unrolled trajectory ( h 0 , … , h T ) (h_{0},\dots,h_{T}) . There is no term in this gradient that drives h 0 h_{0} toward the loss-bearing final state h T h_{T} in embedding distance: the initialization is fixed by the architecture and is not produced by a separately trained predictor. ∎

#### B.3.3 Implicit-Gradient Barrier

The implicit gradient ∇ θ ℒ ∞ = v ⊤ ​ ( I − J g ⊤ ) − 1 ​ ∂ θ g \nabla_{\theta}\mathcal{L}_{\infty}=v^{\top}(I-J_{g}^{\top})^{-1}\partial_{\theta}g contains the factor ( I − J g ) − 1 (I-J_{g})^{-1} . This inverse is undefined when 1 ∈ σ ⁡ ( J g ) 1\in\sigma(J_{g}) , and its operator norm scales as ‖ ( I − J g ) − 1 ‖ ∼ dist ​ ( 1 , σ ⁡ ( J g ) ) − 1 \|(I-J_{g})^{-1}\|\sim\mathrm{dist}(1,\sigma(J_{g}))^{-1} near such a singularity.

Along any continuous gradient-descent path, the eigenvalues of J g ​ ( y ⋆ , θ ) J_{g}(y^{\star};\theta) vary continuously. Therefore, for the dominant eigenvalue to leave the unit disk through + 1 +1 —the canonical loss-of-contraction route for residual iteration maps—it must approach 1 1 . This forces ‖ ( I − J g ) − 1 ‖ → ∞ \|(I-J_{g})^{-1}\|\to\infty .

Unless v v is orthogonal to the offending eigendirection, a codimension-one and hence non-generic condition, the gradient norm diverges. The descent step therefore blows up before the boundary can be crossed, confining θ \theta to the contractive region { ρ ( J g ) < 1 } \{\rho(J_{g})<1\} .

For exits through complex eigenvalues, the same conclusion holds under the one-step JFB approximation, since the truncated Neumann series ∑ k ( J g ⊤ ) k \sum_{k}(J_{g}^{\top})^{k} diverges as ρ ⁡ ( J g ) → 1 \rho(J_{g})\to 1 . ∎

#### B.3.4 Interpretation

Fixed-loop training has no inherent mechanism that favors contractive iterations. An optimum in which g θ g_{\theta} perturbs the embedding for K K steps and only happens to land accurately at step K K is a valid fixed-loop solution. These are precisely the solutions that fail when extra loops are run at inference.

Equilibrium training cannot reach such solutions, because the implicit gradient creates a barrier of diverging gradients around non-contractive regions. As a result, the trajectory of θ \theta is confined to the regime in which the solver converges, the one-step gradient is a descent direction, and additional iterations remain stable.

The mechanistic observation ( Blayney et al., 2026 ) that fixed points emerge only late in standard looped training is consistent with this picture: the loss landscape contains a basin near contractive solutions, but only equilibrium training applies pressure toward that basin from the beginning of training.

## Appendix C Hyperparamter and Experimental Settings

We use NVIDIA H200 GPUs for all of our experiments.

† \dagger At 770M, Attractor Model uses AdamW LR 5 × 10 − 3 5\times 10^{-3} and Muon LR 6 × 10 − 3 6\times 10^{-3} ; Transformer/Parcae use 6 × 10 − 3 6\times 10^{-3} / 8 × 10 − 3 8\times 10^{-3} . ‡ \ddagger Gradient checkpointing enabled for 770M Attractor Model and Parcae; disabled for Transformer. ⋆ \star torch.compile enabled for Transformer and Parcae; disabled for Attractor Model (implicit-gradient hooks are not compile-compatible).

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
