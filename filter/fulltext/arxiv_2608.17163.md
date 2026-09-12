##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Q-Learning With World Models

###### Abstract

Off-policy reinforcement learning (RL) has become increasingly sample-efficient, enabling applications such as RL fine-tuning of Vision-Language-Action models into reliable, high-performing policies. World models offer a further lever for sample efficiency, as they predict state changes rather than actions alone, but their success has largely been confined to supervised policy learning. Prior model-based RL methods often optimize the policy or value function directly on imagined rollouts, which is prone to compounding bias and struggles to scale to large, high-dimensional problems such as real-world robotics, a problem that worsens with task horizon and visual complexity. In this work, we instead ask whether we can leverage world models directly on top of standard Q-learning to improve performance, while remaining trained and grounded in the real, online setting. We propose QWM , a framework that leverages world models to perform test-time search over imagined trajectories on top of Q-learning to select high-value actions during both online rollouts and evaluation. Since the policy and value function are trained only on real transitions, QWM avoids compounding model bias while still gaining the sample-efficiency benefits of predictive search. On challenging manipulation benchmarks Robomimic and LIBERO, QWM significantly outperforms strong prior state-of-the-art methods on both sample efficiency and performance.

## 1 Introduction

Recent advances in off-policy reinforcement learning (RL) have substantially improved its sample efficiency, enabling applications such as RL fine-tuning of Vision-Language-Action (VLA) models into highly reliable, high-performing policies ( Intelligence et al., 2025 ; Dong et al., 2026a ) . As RL is applied to increasingly complex scenarios, further gains in sample efficiency become increasingly valuable, if not essential. World models offer a natural lever for closing this gap, as they have the ability to predict changes in state rather than actions alone. So far, however, their success has been largely confined to supervised policy learning. This raises a natural question: is there a simple way to leverage world models to improve the performance of online RL, without resorting to traditional model-based RL approaches that are prone to compounding the world model’s bias into the training process?

Prior work on model-based RL has explored learning a dynamics model and optimizing a policy or value function directly within it ( Hansen et al., 2024 ; Hafner et al., 2024 ) , but scaling this approach to large, high-dimensional problems such as real-world robotics remains difficult: policies trained primarily on rollouts inside an imperfect world model inherit and compound its biases, and this problem worsens as task horizon and visual complexity increase. Rather than using the world model as a substitute for real interaction, we ask whether it can instead sharpen an RL agent that remains trained and grounded in the real, online setting. In this work, we study Q-learning with a world model, where the model serves not as a replacement for environment interaction but as a way for improving performance.

Our key insight is that a learned world model can be used on top of standard Q-learning to enable test-time search over actions by imagining future trajectories, and that this improved action selection alone directly translates into higher performance for Q-learning methods. We propose Q-Learning with World Models ( QWM ), a framework that leverages world models for test-time search directly on top of standard Q-learning. Instead of using the state value function to conduct search as in typically done in model-based RL, the learned Q-function also enables more powerful search to evaluate candidate actions and select the highest-value one before it is executed. This test-time search over actions is applied both during online rollouts, to obtain better data for online RL, and at evaluation time, to act more effectively with the learned policy. Rather than sampling a single action from the policy or sampling multiple actions and selecting the one with the highest Q-value, QWM leverages the imagination capability of world models to select the best action for downstream performance, while avoiding the compounding bias and instability of policies trained inside a learned model.

Our main contribution is QWM , a simple and general framework for leveraging learned world models to improve Q-learning through test-time search. Because the underlying policy and value function are still trained online against real environment transitions, QWM avoids the bias accumulation that afflicts methods relying primarily on imagined rollouts, while still reaping the sample-efficiency benefits such a predictive model can offer at decision time. We evaluate QWM on challenging manipulation benchmarks, Robomimic and LIBERO, across both state-based and visual observation settings, and find that it significantly outperforms strong prior methods on both sample efficiency and performance.

## 2 Related Work

Reinforcement learning with prior data. To improve performance and sample efficiency of online RL, prior works have studied the problem of using an offline dataset to accelerate online learning. Popular approaches involve balancing exploration and exploitation ( Yang et al., 2023 ; Zhang et al., 2023 ; Mark et al., 2023 ) , calibrating value estimates ( Nakamoto et al., 2024 ; Dong et al., 2026c ) , or retaining offline data alongside newly collected online data during fine-tuning ( Vecerik et al., 2018 ; Nair et al., 2021 ; Ball et al., 2023 ; Dong et al., 2025a ; Dong et al., 2025b ) . Offline RL algorithms have also been applied directly to online fine-tuning ( Fujimoto et al., 2019 ; Fujimoto and Gu, 2021 ; Hansen-Estruch et al., 2023 ; Park et al., 2025 ; Dong et al., 2025c ; Dong et al., 2026b ; Dong et al., 2026e ) , where the prior data is first trained with offline RL before obtaining new samples online. Our work differs from these lines of research in that we focus on leveraging prior data through world models to improve online RL, rather than on how prior data is incorporated into the RL objective itself; this makes our approach applicable to any RL fine-tuning algorithm.

Model-based RL. Model-based RL methods learn a dynamics model of the environment and use it for policy or value learning. One family of methods generates additional synthetic transitions by rolling the learned model forward and treats them as if they were real experience ( Sutton, 1991 ; Gu et al., 2016 ; Kalweit and Boedecker, 2017 ; Kurutach et al., 2018 ; Kaiser et al., 2024 ) , or otherwise optimizes the policy directly against imagined trajectories ( Zhang et al., 2019 ; Hafner et al., 2020 ; Hafner et al., 2022 ; Hafner et al., 2024 ; Hafner et al., 2025 ) or through short branched rollouts mixed with real data ( Feinberg et al., 2018 ; Janner et al., 2021 ) . A second family instead uses the learned model only to plan over imagined rollouts with trajectory optimizers such as the cross-entropy method or MPPI ( Nagabandi et al., 2018 ; Ebert et al., 2018 ; Chua et al., 2018 ; Hansen et al., 2022 ; Hansen et al., 2024 ) ; some of these methods further learn a terminal value function to bound the planning horizon ( Hansen et al., 2022 ; Hansen et al., 2024 ; Kim et al., 2026 ) . A third family combines a learned (or known) model with Monte Carlo tree search guided by a learned value function, mainly for discrete-action, densely-simulated domains ( Silver et al., 2017 ; Schrittwieser et al., 2020 ; Ye et al., 2021 ; Schrittwieser et al., 2021 ) , with recent works extending it to continuous control ( Hubert et al., 2021 ; Wang et al., 2024 ) . These methods rely on some combination of having a known dynamics model, discrete actions, or bootstrapping policy and value targets from search statistics computed over model-imagined rollouts. Furthermore, many of these works rely on abundant simulated data, where model error and sample budget are far less of a concern than in real-world, sparse-reward robotic manipulation. Across all of these approaches, the policy or value function trained substantially on model-generated rollouts inherits and compounds the model’s own biases directly into training, an issue that grows with task horizon and visual complexity ( Janner et al., 2021 ; Chua et al., 2018 ; Kaiser et al., 2024 ; Hafner et al., 2020 ) . QWM sidesteps this issue by leveraging the model purely at test-time rather than a source of additional training data on top of standard Q-learning, and train the policy and critic on real data.

#### World models for VLAs.

A closely related line of work applies world models to VLA policies. VLAW ( Guo et al., 2026 ) and World-VLA-Loop ( Liu et al., 2026 ) alternate between fine-tuning world models on real rollouts and using it to generate synthetic training data for policy learning. WMPO ( Zhu et al., 2025 ) and World4RL ( Jiang et al., 2026a ) run on-policy RL directly on imagined rollouts, while WoVR ( Jiang et al., 2026b ) targets the resulting reward hallucination and OOD drift via keyframe-initialized rollouts and policy-aligned co-evolution. RISE ( Yang et al., 2026 ) , World-Gymnast ( Sharma et al., 2026 ) , and GigaBrain-0.5M ( Team et al., 2026 ) score imagined rollouts with a learned progress/value model or VLM and use the resulting rewards for policy-gradient updates. All of these use the world model primarily as a training data generator, which is prone to inheriting compounding bias. SAILOR ( Jain et al., 2025 ) learns a world model and reward model to guide imitation and recover from out-of-support states. QWM can be applied to any RL fine-tuning methods for VLAs with a Q-function, and instead of using the world model to generate data or guide imitation learning, we leverage world models to improve Q-learning at test time.

#### Test-time scaling and best-of- N N inference.

A substantial body of work has demonstrated that test-time scaling, for example via best-of- N N sampling, can significantly improve the performance of generative models across domains, including autoregressive language models ( Wang et al., 2022 ; Snell et al., 2024 ; Chow et al., 2024 ) , diffusion models ( Ma et al., 2025 ) , and policy learning ( Dong et al., 2025b ; Hansen-Estruch et al., 2023 ; Dong et al., 2026d ; Chen et al., 2023 ) . In most of these settings, candidates are scored independently by a verifier or value function, and only the single best sample is retained, without modeling how a candidate’s near-term consequences unfold. QWM can instead be viewed as a form of test-time scaling in which search evaluates candidates on their predicted downstream value, yielding a substantially better estimate of which actions are best.

## 3 Preliminaries

We consider a Markov decision process (MDP) specified by the tuple { 𝒮 , 𝒜 , ρ , r , γ , T } \{\mathcal{S},\mathcal{A},\rho,r,\gamma,T\} , where 𝒮 \mathcal{S} denotes the state space, 𝒜 \mathcal{A} denotes the action space, ρ ⁡ ( s ) \rho(s) is the distribution over initial states, r : 𝒮 × 𝒜 → ℝ r:\mathcal{S}\times\mathcal{A}\rightarrow\mathbb{R} is the reward function, γ ∈ [ 0 , 1 ) \gamma\in[0,1) is the discount factor, and T ⁡ ( s ′ | s , a ) T(s^{\prime}|s,a) is the transition probabilities governing the environment. The goal of RL is to find a policy π \pi that maximizes the expected discounted return 𝔼 π ​ [ ∑ t = 0 T γ t ​ r ​ ( s t , a t ) ] \mathbb{E}_{\pi}\left[\sum_{t=0}^{T}\gamma^{t}r(s_{t},a_{t})\right] .

In this paper, we study how a learned world model can be used to improve online RL fine-tuning at decision time. Concretely, we assume access to a dataset 𝒟 offline = { ( s , a , r , s ′ ) } \mathcal{D}_{\text{offline}}=\{(s,a,r,s^{\prime})\} of environment transitions – either collected offline or accumulated online – which is used to pretrain a world model M ψ ​ ( s ′ | s , a ) M_{\psi}(s^{\prime}|s,a) that predicts the next state given the current state and action. The world model is used at decision time. During online training, the agent collects tuples ( s t , a t , r t , s t + 1 ) (s_{t},a_{t},r_{t},s_{t+1}) through environment interaction; these are appended to a replay buffer 𝒟 \mathcal{D} and used to update the policy and Q-function toward higher returns. Our central question is how to leverage the world model to improve the performance of Q-learning.

We focus on off-policy RL, where the Q-function estimates the discounted return of the policy given a state and action, and is trained with TD learning: ℒ ⁡ ( ϕ ) = 𝔼 ( s t , a t , s t + 1 ) ∼ 𝒟 ​ [ ( r t + γ ​ Q ϕ ′ ​ ( s t + 1 , a ~ t + 1 ∗ ) − Q ϕ ​ ( s t , a t ) ) 2 ] , \mathcal{L}(\phi)=\mathbb{E}_{(s_{t},a_{t},s_{t+1})\sim\mathcal{D}}\left[\left(r_{t}+\gamma Q_{\phi^{\prime}}(s_{t+1},\tilde{a}^{*}_{t+1})-Q_{\phi}(s_{t},a_{t})\right)^{2}\right], (1) where Q ϕ ′ Q_{\phi^{\prime}} is a target network and a ~ t + 1 ∗ \tilde{a}^{*}_{t+1} is the next action selected by the RL policy. We implement QWM on top of two state-of-the-art off-policy Q-learning algorithms.

EXPO. The first is EXPO ( Dong et al., 2025b ) , a high-performing online RL method that couples a base policy with a lightweight edit policy. EXPO maintains two parameterized policies: a base flow policy—in our case, the base policy π base \pi_{\text{base}} , trained with a supervised loss—and an edit policy π edit \pi_{\text{edit}} , trained to maximize the Q-function: ℒ ⁡ ( π edit ) = − 𝔼 ( s t , a t ) ∼ 𝒟 , a ^ t ∼ π edit ​ [ Q ϕ ​ ( s t , a t + a ^ t ) − α ​ log ⁡ π edit ​ ( a ^ t ∣ s t , a t ) ] . \begin{split}\mathcal{L}(\pi_{\text{edit}})=-\mathbb{E}_{(s_{t},a_{t})\sim\mathcal{D},\;\hat{a}_{t}\sim\pi_{\text{edit}}}\bigl[Q_{\phi}(s_{t},\,a_{t}+\hat{a}_{t})-\alpha\log\pi_{\text{edit}}(\hat{a}_{t}\mid s_{t},a_{t})\bigr].\end{split} (2) The edit policy predicts an edit a ^ t \hat{a}_{t} , clipped to [ − β , β ] [-\beta,\beta] , that is added to the base action a t a_{t} to produce an edited action a ~ t = a t + a ^ t \tilde{a}_{t}=a_{t}+\hat{a}_{t} . This design avoids backpropagating gradients through the base policy while still grounding TD updates in near-optimal actions. The final inference and TD-backup policy is an on-the-fly (OTF) policy that selects the value-maximizing candidate among N N sampled base and edited actions: a ~ ∗ = arg ⁡ max a ∈ ⋃ i = 1 N { a i , a ~ i } ​ Q ϕ ​ ( s , a ) , \tilde{a}^{*}=\underset{a\;\in\;\bigcup_{i=1}^{N}\{a_{i},\,\tilde{a}_{i}\}}{\arg\max}\;Q_{\phi}(s,a), (3) where Q ϕ Q_{\phi} is trained with a standard TD objective.

RLPD. The second is RLPD ( Ball et al., 2023 ) , a sample-efficient off-policy RL algorithm that combines offline and online replay data with high update-to-data (UTD) ratios, an ensemble of critics, and a Gaussian actor. RLPD trains the actor π θ \pi_{\theta} with a SAC-style ( Haarnoja et al., 2018 ) entropy-regularized objective, ℒ ⁡ ( π θ ) = − 𝔼 s t ∼ 𝒟 , a t ∼ π θ ​ [ Q ϕ ​ ( s t , a t ) − α ​ log ⁡ π θ ​ ( a t ∣ s t ) ] , \mathcal{L}(\pi_{\theta})=-\mathbb{E}_{s_{t}\sim\mathcal{D},\;a_{t}\sim\pi_{\theta}}\bigl[Q_{\phi}(s_{t},a_{t})-\alpha\log\pi_{\theta}(a_{t}\mid s_{t})\bigr], (4) and stabilizes the high-UTD critic updates using an ensemble of M M critics with random subsets used for the target computation, together with layer normalization. At each update, transitions are drawn via symmetric sampling, with equal proportions from the offline buffer and the online replay buffer.

## 4 Method

In this section, we present the key component of QWM to leverage world models to perform test-time search for better performance for Q-Learning. We instantiate QWM as a tree search over actions on top of standard Q-learning We first describe the approach for tree search with world models, split into three parts: constructing the search tree ( Section 4.1 ), aggregating the value of expanded nodes into a value for each proposed action ( Section 4.2 ), and searching with the Q-function ( Section 4.3 ); we then discuss implementation details ( Section 4.4 ).

### 4.1 Tree Search With the World Model

Our goal is to construct a tree such that searching over it yields good actions and adequate coverage of possible futures, and is general enough to be compatible with different problem settings. We construct the tree governed by three quantities: the number of actions sampled at each state N N , the number of next states sampled per action K K , and the search depth D D .

Concretely, at each decision step, we set the root of the tree to the current state s 0 s_{0} where depth 0 0 represents the root of the tree. Nodes alternate between state layers and action layers, with one state layer followed by one action layer constituting a single level of depth. At a state node at level d d , the tree is expanded by drawing N N candidate actions from the policy, { a d n } n = 1 N ∼ π θ ( ⋅ ∣ s d ) \{a_{d}^{n}\}_{n=1}^{N}\sim\pi_{\theta}(\cdot\mid s_{d}) . At each action node, the tree is expanded and form depth d + 1 d+1 by querying the world model K K times to obtain K K predicted future states, { s d + 1 k } k = 1 K ∼ M ψ ​ ( s d , a d n ) \{s^{k}_{d+1}\}_{k=1}^{K}\sim M_{\psi}(s_{d},a_{d}^{n}) .

We repeat this expansion recursively to depth D D ( Figure 2 ). At the final layer, N leaf N_{\text{leaf}} actions are sampled from the policy. The tree is intended to give a short-horizon prediction of the consequences of an action, not to plan exhaustively – this keeps rollout lengths short enough to prevent the world model’s own prediction error to accumulate.

### 4.2 Aggregating the Value

Rather than scoring only the leaves and propagating value to the initial action, we observe that the value of every state-action pair in the tree is useful for action selection. The value of a node can either be expressed as a function of state-action value Q ϕ Q_{\phi} or a function of state value V ϕ V_{\phi} , each with complementary trade-offs. As such, we express the value of a node as a combination of these two estimators of the same underlying quantity.

State-action value estimator. At depth d d , we can score each of the N N sampled actions a d n ∼ π θ ( ⋅ ∣ s d ) a_{d}^{n}\sim\pi_{\theta}(\cdot\mid s_{d}) directly with the critic, which already estimates the return of the full remaining trajectory: V Q ​ ( d ∣ s d ) = agg n ∈ [ N ] Q ϕ ​ ( s d , a d n ) . V_{Q}\big(d\mid s_{d}\big)\;=\;\operatorname*{agg}_{n\in[N]}\;Q_{\phi}\big(s_{d},\,a_{d}^{n}\big). (5) This estimator is low-variance and independent of the remaining search depth and error from the model, but relies entirely on Q ϕ Q_{\phi} being learned accurately.

State value estimator. We can alternatively estimate using the world model’s predicted per-step reward r ψ ​ ( s d , a d n ) r_{\psi}(s_{d},a_{d}^{n}) and a discounted value of the next state: V r ​ ( d ∣ s d ) = agg n ∈ [ N ] [ agg k ∈ [ K ] [ r ψ ​ ( s d , a d n ) + λ ​ V ​ ( d + 1 ∣ s d + 1 n , k ) ] ] , V_{r}\big(d\mid s_{d}\big)\;=\;\operatorname*{agg}_{n\in[N]}\left[\;\operatorname*{agg}_{k\in[K]}\Big[\,r_{\psi}\big(s_{d},a_{d}^{n}\big)\;+\;\lambda\,V\big(d+1\mid s_{d+1}^{n,k}\big)\Big]\right], (6) where s d + 1 n , k = M ψ ​ ( s d , a d n ) s_{d+1}^{n,k}=M_{\psi}\big(s_{d},a_{d}^{n}\big) and r ψ ​ ( s d , a d n ) r_{\psi}(s_{d},a_{d}^{n}) is the learned reward model. At the final layer, N leaf N_{\text{leaf}} actions are sampled from the policy and there is no rollout left to recurse into, so the leaf value reduces to state value which can be computed as an aggregate over Q-values for actions in that state, V ⁡ ( D ∣ s D ) = agg n ∈ [ N leaf ] Q ϕ ​ ( s D , a D n ) . V\big(D\mid s_{D}\big)\;=\;\operatorname*{agg}_{n\in[N_{\text{leaf}}]}\;Q_{\phi}\big(s_{D},\,a_{D}^{n}\big). (7) The state value estimator exploits the full imagined rollout but compounds world-model error with depth.

Combined node value. The two estimators have complementary failure modes: V Q V_{Q} is depth-independent but blind to the rollout, while V r V_{r} uses the rollout but accumulates simulation error. We take advantage of both estimators to get a combined node value: V ⁡ ( d ∣ s d ) = 1 2 ​ ( V Q ​ ( d ∣ s d ) + V r ​ ( d ∣ s d ) ) V\big(d\mid s_{d}\big)\;=\;\tfrac{1}{2}\Big(V_{Q}\big(d\mid s_{d}\big)+V_{r}\big(d\mid s_{d}\big)\Big) (8) which can be extended to a weighted average α ​ V Q + ( 1 − α ) ​ V r \alpha V_{Q}+(1-\alpha)V_{r} , where α ∈ [ 0 , 1 ] \alpha\in[0,1] .

#### Root value.

The value of each originally sampled root action a 0 n a_{0}^{n} follows the same computation at d = 0 d=0 : Q t ​ s ​ ( s 0 , a 0 n ) = 1 2 ​ ( Q ϕ ​ ( s 0 , a 0 n ) + [ r ψ ​ ( s 0 , a 0 n ) + agg k ∈ [ K ] λ ​ V ​ ( 1 ∣ s 1 k ) ] ) , s 1 k = M ψ ​ ( s 0 , a 0 n ) . Q_{ts}(s_{0},a_{0}^{n})\;=\;\tfrac{1}{2}\left(Q_{\phi}(s_{0},a_{0}^{n})\;+\;\Big[r_{\psi}(s_{0},a_{0}^{n})+\operatorname*{agg}_{k\in[K]}\lambda\,V\big(1\mid s_{1}^{k}\big)\Big]\right),\qquad s_{1}^{k}=M_{\psi}(s_{0},a_{0}^{n}). (9) The action ultimately selected is a max or softmax over the original sampled actions, weighted by their tree-search values Q t ​ s ​ ( s 0 , a 0 n ) Q_{ts}(s_{0},a_{0}^{n}) . We use this search procedure in two places: to select actions during training, and to act at evaluation time.

### 4.3 Searching with the Q-function.

Because the tree grows very large very quickly with depth, due to computational constraints we in practice design a heuristic to select only a subset of nodes to expand and prune the rest using the Q-function as a search policy. Let J J be the number of paths that will be expanded. Let ℬ d \mathcal{B}_{d} denote the surviving set of J J partial paths after pruning at depth d d (with ℬ 0 = { a 0 n } n = 1 N \mathcal{B}_{0}=\{a_{0}^{n}\}^{N}_{n=1} , the single root path under consideration). Each surviving path b ∈ ℬ d b\in\mathcal{B}_{d} carries an accumulated discounted score Σ ⁡ ( b , d ) = ∑ d ′ = 1 d λ d ′ ​ Q ϕ ​ ( s d ′ b , a d ′ b ) , \Sigma(b,d)\;=\;\sum_{d^{\prime}=1}^{d}\lambda^{d^{\prime}}\,Q_{\phi}\big(s_{d^{\prime}}^{b},a_{d^{\prime}}^{b}\big), (10) where ( s d ′ b , a d ′ b ) \big(s_{d^{\prime}}^{b},a_{d^{\prime}}^{b}\big) is the state-action pair visited by path b b at depth d ′ d^{\prime} .

At depth d + 1 d+1 , every surviving path b ∈ ℬ d b\in\mathcal{B}_{d} is expanded into N N candidate children { a d + 1 b , n } n = 1 N ∼ π θ ( ⋅ ∣ s d + 1 b ) \{a_{d+1}^{b,n}\}_{n=1}^{N}\sim\pi_{\theta}(\cdot\mid s_{d+1}^{b}) , each scored by its prospective cumulative sum: Σ ~ ​ ( b , n , d + 1 ) = Σ ⁡ ( b , d ) + λ d + 1 ​ Q ϕ ​ ( s d + 1 b , n , a d + 1 b , n ) . \tilde{\Sigma}(b,n,d+1)\;=\;\Sigma(b,d)\;+\;\lambda^{d+1}\,Q_{\phi}\big(s_{d+1}^{b,n},a_{d+1}^{b,n}\big). (11) The surviving set at depth d + 1 d+1 is the top J J over all candidates, ranked by Equation 11 : ℬ d + 1 = top ​ - J { Σ ~ ( b , n , d + 1 ) : b ∈ ℬ d , n ∈ [ N ] } . \mathcal{B}_{d+1}\;=\;\operatorname*{top\text{-}}J\Big\{\tilde{\Sigma}(b,n,d+1)\;:\;b\in\mathcal{B}_{d},\;n\in[N]\Big\}. (12) At depth D D , each surviving path b ∈ ℬ D − 1 b\in\mathcal{B}_{D-1} samples N leaf N_{\text{leaf}} final actions, whose values are aggregated per-beam: L ⁡ ( b ) = agg n ∈ [ N leaf ] Q ϕ ​ ( s D b , a D b , n ) . L(b)\;=\;\operatorname*{agg}_{n\in[N_{\text{leaf}}]}\;Q_{\phi}\big(s_{D}^{b},a_{D}^{b,n}\big). (13) The root’s tree-search value combines all surviving beams. Intuitively, Equation 12 selects survivors by the additive discounted sum Σ ~ \tilde{\Sigma} . When J J equals the max number of nodes, no candidates are discarded at Equation 12 ( ℬ d \mathcal{B}_{d} always contains all N d N^{d} paths). When J J is less than the max number of nodes, Equation 12 discards candidates at every intermediate depth based on Equation 11 .

### 4.4 Practical Implementation

We instantiate the action-conditioned world model in two forms depending on the observation modality. In practice, because we operate in sparse reward settings where rewards are zero except for the terminal state, we do not learn a reward model on top of the world model. For low-dimensional state observations, we use a deterministic residual dynamics model M ψ ​ ( s t , a t ) = s t + Δ ψ ​ ( s t , a t ) M_{\psi}(s_{t},a_{t})=s_{t}+\Delta_{\psi}(s_{t},a_{t}) implemented as a three-layer MLP with hidden dimension 256. The model takes the Robomimic low-dimensional state representation, including end-effector pose, gripper states, and object features, together with the 7-DoF action as input. It is pretrained offline on demonstration transitions using an MSE objective. For pixel observations, we adapt Wan2.2-TI2V-5B ( Wan et al., 2025 ) into an action-conditioned video world model by introducing an MLP-based action encoder. Specifically, each robot action is mapped into action tokens through a three-layer MLP, which are then concatenated with the text conditioning tokens and provided to the diffusion transformer as additional conditioning inputs. The action encoder and diffusion transformer are jointly fine-tuned while keeping the VAE and text encoder frozen. The model is trained on demonstration video clips with aligned action sequences using the standard Wan2.2 flow-matching objective. During inference, the world model predicts short-horizon future observations conditioned on candidate actions. For LIBERO, we generate 5-frame 128 × 128 128\times 128 video clips, and use the predicted next frame as the subsequent observation for iterative rollout and tree search.

## 5 Experiments

The goal of our experiments is to answer the following core questions:

( Q1) How does QWM perform compared to state-of-the-art model-free and model-based RL methods?

( Q2) How does QWM perform compared to the base method it is implemented on top of?

( Q3) Does QWM scale to a pixel-based setting?

( Q4) What components of QWM are most important for performance?

Environments. We evaluate QWM on challenging robotic manipulation tasks from Robomimic ( Mandlekar et al., 2021 ) and LIBERO ( Liu et al., 2023 ) , where a 7-DoF robot arm is required to complete diverse manipulation behaviors under sparse task-completion rewards. For Robomimic, we consider four tasks: Lift, Can, Square, and Tool Hang. Lift requires the robot to grasp and lift an object; Can requires the robot to grasp a cylindrical object and place it at a target location; Square involves precisely inserting a square nut onto a peg; and Tool Hang is a long-horizon multi-stage assembly task where the robot constructs a stand and hangs a tool. For LIBERO, we evaluate on five tasks following the experimental protocol of prior work ( Dong et al., 2026d ) .

Baselines. We compare against both state-of-the-art model-free algorithms and model-based algorithms. We refer to Section C.4 for details on algorithmic comparisons.

### 5.1 How Does QWM Perform Compared to State-of-the-Art Model-Free and Model-Based RL Methods?

Compared with model-free baselines. Success rates of QWM and model-free baselines in the online settings. QWM outperforms strong model-free baselines in sample efficiency.

Model-free. We compare against strong model-free RL baselines in Section 5.1 , all of which leverage online interaction to learn Q-functions. QWM achieves the strongest performance across all tasks. RLPD, DSRL, QSM, QAM, and FQL each sample a single action from the policy for execution in the environment. While this action is intended to approximately maximize the Q-function, optimization delays and errors prevent it from being truly optimal. QWM instead leverages the world model’s ability to predict future outcomes, performing test-time search over candidate actions and selecting the ones with the best predicted future returns. While IDQL selects actions by sampling multiple candidates and selecting the one with the highest Q-value, it considers only the immediate next action rather than a sequence of future actions, the latter carrying substantially more signal about long-term performance. These results demonstrate that the test-time search in QWM provides benefits complementary to Q-learning, enabling better action selection without substituting online interactions.

Model-based. We further compare QWM with state-of-the-art model-based RL methods TD-MPC2 and EfficientZero V2. We include both sparse and dense reward variants for the model-based algorithms, as many of these methods were designed for dense rewards, and struggles to learn as well in sparse reward settings. We present the results in Figure 3 . QWM achieves consistently stronger performance across the evaluated manipulation tasks, while TD-MPC2 and EfficientZero V2 only obtain non-zero success on Lift for the number of training steps reported. Different from conventional model-based RL methods that incorporate model predictions into policy optimization or learning targets, QWM uses the world model only at test-time search while keeping policy and value learning grounded on real environment transitions. This design allows QWM to leverage future predictions for improved action selection without relying on model-generated trajectories during learning, providing an effective way to combine the predictive capability of world models with online Q-learning while avoiding compounding bias from the world model.

### 5.2 How Does QWM Perform Compared to the Base Method It Is Implemented on Top of?

In this section, we evaluate the performance of QWM compared to the base algorithm it is implemented on. We implement QWM on top of EXPO and RLPD for the paper as representative sample efficient Q-learning algorithms, but QWM can be implemented on other model-free algorithms as well. We start by comparing QWM against EXPO in Figure 4 . QWM consistently improves learning efficiency across Tool Hang, Square, and Can, with particularly pronounced gains on harder tasks such as Tool Hang. Comparing with RLPD as the base algorithm, as shown in Figure 6, using QWM with RLPD consistently improves learning compared to RLPD alone with particularly clear gains in sample efficiency. These findings show that QWM provides consistent benefits across different underlying RL algorithms. At the same time, QWM will benefit from a more sample efficient base algorithm as shown by the results of QWM on top of EXPO compared to QWM on top of RLPD.

### 5.3 Does QWM Scale to a Pixel-Based Setting?

We further evaluate whether the performance gains of QWM extend to high-dimensional visual observations. Due to computational constraints, we use the world model only for sampling during online RL data collection, not for evaluation. As shown in Figure 6 , QWM achieves a clear overall improvement over EXPO. The gains are most evident on Tasks 60, 79, and 29, where QWM learns faster and reaches stronger late-stage performance. On Task 28, both methods eventually attain near-perfect success, but QWM reaches high performance earlier, demonstrating a clear improvement in sample efficiency. As shown in the ablations in Figure 4 , restricting the world model to sampling-only (without evaluation) reduces performance, suggesting the visual results can be even stronger given sufficient compute. Nonetheless, even in this sampling-only setting, QWM consistently improves over the base algorithm, showing that its benefits extend naturally to high-dimensional visual inputs, which are substantially harder to learn a dynamics model from.

### 5.4 What Components of QWM Are Most Important for Performance?

To better understand the significance of different pieces of QWM , we ablate over three key components: (1) the importance of using QWM during online RL sampling, evaluation, or both, (2) the hyperparameters for constructing the tree, and (3) the number of expanded nodes during search to constrain the tree size. We present additional experiments comparing against performing search with only a state value function Appendix B .

Sampling versus evaluation. We first ablate whether QWM is applied during online RL data collection, at evaluation time, or in both. The sampling only variant performs test-time search during online data collection but disables it at evaluation, while the evaluation only variant applies tree search only at evaluation time. The full sampling + evaluation variant uses test-time search in both. As shown in Figure 7 , applying test-time search at both stages provides the strongest and most consistent learning efficiency. The full variant improves faster and more smoothly and reaches high success rates earlier. Sampling-time search affects which transitions are collected and added to the replay buffer, allowing subsequent policy and critic updates to benefit from higher-value online experience. Evaluation-time search, in contrast, directly improves action selection without modifying the learned policy or training data. Performing test-time search at both stages therefore combines improved online experience collection with stronger execution-time action selection, which gives more consistent advantage over either single-stage variant.

Tree-search hyperparameters. We next ablate key hyperparameters for constructing the search tree: search depth D D , recursive discount factor λ \lambda , and the number of action candidates N N . In Figure 7 , we see that search depth has a clearer effect on learning. Depth 2 2 generally provides the strongest performance gain in our experiments, whereas depth 1 1 improves more slowly as a shallow search may not capture enough future consequence to reliably distinguish candidate actions. For tasks requiring longer term planning, higher depths can be beneficial, though making the depth too high could expose the search to additional world-model prediction error and uncertainty. Consequently, a moderate search depth provides a favorable trade-off between incorporating future information and maintaining reliable predictions.

The value aggregation discount factor λ \lambda , which controls how strongly future tree values contribute to the recursive value aggregation in Equation 8 is important for performance and setting λ \lambda too large or too small leads to lower performance, and relatively small to moderate values, particularly λ = 0.2 \lambda=0.2 for our settings, provide the strongest learning efficiency. A larger λ \lambda places greater weight on values propagated from deeper imagined states, making the value aggregation more sensitive to accumulated world-model and value-estimation errors, while an overly small λ \lambda limits the contribution of a deeper search. Overall, the results favor large weighting of short-term estimates with a moderately small future-value weighting.

We next examine the effect of the number of action candidates N N considered at each node of the search tree. Increasing N N allows the search to evaluate a broader set of possible actions before committing to the one that maximizes the recursive value estimate, which in principle should improve the quality of the selected action by reducing the chance that a good candidate is overlooked. Empirically, we find that the number of actions N N that performs the best is dependent on the environment. In general, performance improves as N N increases from very small values, since too few candidates can fail to include actions that meaningfully diverge from one another, limiting the benefit of search altogether. However, the gains from increasing N N diminish beyond a moderate number of candidates, and excessively large N N can even hurt performance, likely because evaluating many candidates amplifies the influence of world-model and value-estimation errors across a larger number of imagined rollouts, while also increasing computational cost with limited additional benefit. We find that a moderate number of action candidates offers the best trade-off between exploration of the action space and robustness to compounding prediction errors, and we adopt this setting as default in our main experiments.

Number of expanded nodes. Lastly, we ablate over the number of expanded nodes in our search heuristic. In Figure 7 , we observe that performance is relatively insensitive to the number of expanded nodes J J , as the heuristic accounts for which paths have the largest value to decide which nodes to keep expanding and which to prune. While this greedy approach does not guarantee finding the highest value paths of the full tree, it provides a good approximation. This suggests that retaining a small number of high-value branches is already sufficient to capture useful candidate futures.

## 6 Discussion

In this paper, we present QWM , a framework for leveraging world models via test-time search over actions on top of Q-learning to improve performance. Rather than using the world model to optimize the policy directly, as in conventional model-based RL, we use it purely at test time both during online rollouts and at evaluation. We show that QWM outperforms strong model-free baselines, while avoiding the compounding model bias that afflicts methods which optimize policies primarily inside a learned world model. Despite these results, QWM has limitations. The tree search introduces non-trivial computational overhead at rollout and evaluation time relative to a standard policy forward pass, which may be prohibitive under tight latency requirements. Additionally, QWM depends on learning a world model, which is an expensive and often challenging to train; while grounding the policy and Q-function in real data prevents bias from the model from compounding, reducing search overhead and obtaining high quality world models remain important future directions.

## 7 Acknowledgments

This work was supported in part by an NSF CAREER award, NSF #1941722 the RAI Institute, ONR grant N00014-22-1-2293, and ONR grant N00014-22-1-2621. This work used the Delta system at the National Center for Supercomputing Applications [award OAC 2005572] through allocation CIS260152 from the Advanced Cyberinfrastructure Coordination Ecosystem: Services & Support (ACCESS) program, which is supported by U.S. National Science Foundation grants #2138259, #2138286, #2138307, #2137603, and #2138296.

## References

Ball et al. (2023) P. J. Ball, L. Smith, I. Kostrikov, and S. Levine Efficient online reinforcement learning with offline data . External Links: 2302.02948 , Link Cited by: §C.4 , §2 , §3 .

Chen et al. (2023) H. Chen, C. Lu, C. Ying, H. Su, and J. Zhu Offline reinforcement learning via high-fidelity generative behavior modeling . External Links: 2209.14548 , Link Cited by: §2 .

Chow et al. (2024) Y. Chow, G. Tennenholtz, I. Gur, V. Zhuang, B. Dai, S. Thiagarajan, C. Boutilier, R. Agarwal, A. Kumar, and A. Faust Inference-aware fine-tuning for best-of-N sampling in large language models . CoRR abs/2412.15287 . External Links: Link , Document Cited by: §2 .

Chua et al. (2018) K. Chua, R. Calandra, R. McAllister, and S. Levine Deep reinforcement learning in a handful of trials using probabilistic dynamics models . In Advances in Neural Information Processing Systems , S. Bengio, H. Wallach, H. Larochelle, K. Grauman, N. Cesa-Bianchi, and R. Garnett (Eds.) , Vol. 31 , pp. . External Links: Link Cited by: §2 .

Dong et al. (2026a) P. Dong, K. Hung, T. Gao, D. Sadigh, and C. Finn EXPO-ft: sample-efficient reinforcement learning finetuning for vision-language-action models . External Links: 2605.25477 , Link Cited by: §1 .

Dong et al. (2026b) P. Dong, K. Hung, A. Swerdlow, D. Sadigh, and C. Finn TQL: scaling q-functions with transformers by preventing attention collapse . External Links: 2602.01439 , Link Cited by: §2 .

Dong et al. (2025a) P. Dong, A. M. Lessing, A. S. Chen, and C. Finn Reinforcement learning via implicit imitation guidance . External Links: 2506.07505 , Link Cited by: §2 .

Dong et al. (2025b) P. Dong, Q. Li, D. Sadigh, and C. Finn EXPO: stable reinforcement learning with expressive policies . External Links: 2507.07986 , Link Cited by: §C.4 , §2 , §2 , §3 .

Dong et al. (2025c) P. Dong, S. Mirchandani, D. Sadigh, and C. Finn What matters for batch online reinforcement learning in robotics? . External Links: 2505.08078 , Link Cited by: §2 .

Dong et al. (2026c) P. Dong, R. Polonsky, D. Sadigh, and C. Finn Do you really need to pretrain q-functions for online rl fine-tuning? . External Links: 2607.27203 , Link Cited by: §2 .

Dong et al. (2026d) P. Dong, A. Swerdlow, D. Sadigh, and C. Finn FASTER: value-guided sampling for fast rl . External Links: 2604.19730 , Link Cited by: §2 , §5 .

Dong et al. (2026e) P. Dong, C. Zheng, C. Finn, D. Sadigh, and B. Eysenbach Value flows . External Links: 2510.07650 , Link Cited by: §2 .

Ebert et al. (2018) F. Ebert, C. Finn, S. Dasari, A. Xie, A. Lee, and S. Levine Visual foresight: model-based deep reinforcement learning for vision-based robotic control . External Links: 1812.00568 , Link Cited by: §2 .

Feinberg et al. (2018) V. Feinberg, A. Wan, I. Stoica, M. I. Jordan, J. E. Gonzalez, and S. Levine Model-based value estimation for efficient model-free reinforcement learning . External Links: 1803.00101 , Link Cited by: §2 .

Fujimoto and Gu (2021) S. Fujimoto and S. S. Gu A minimalist approach to offline reinforcement learning . External Links: 2106.06860 , Link Cited by: §2 .

Fujimoto et al. (2019) S. Fujimoto, D. Meger, and D. Precup Off-policy deep reinforcement learning without exploration . External Links: 1812.02900 , Link Cited by: §2 .

Gu et al. (2016) S. Gu, T. Lillicrap, I. Sutskever, and S. Levine Continuous deep q-learning with model-based acceleration . External Links: 1603.00748 , Link Cited by: §2 .

Guo et al. (2026) Y. Guo, T. Lee, L. X. Shi, J. Chen, P. Liang, and C. Finn VLAW: iterative co-improvement of vision-language-action policy and world model . External Links: 2602.12063 , Link Cited by: §2 .

Haarnoja et al. (2018) T. Haarnoja, A. Zhou, P. Abbeel, and S. Levine Soft actor-critic: off-policy maximum entropy deep reinforcement learning with a stochastic actor . External Links: 1801.01290 , Link Cited by: §3 .

Hafner et al. (2020) D. Hafner, T. Lillicrap, J. Ba, and M. Norouzi Dream to control: learning behaviors by latent imagination . External Links: 1912.01603 , Link Cited by: §2 .

Hafner et al. (2022) D. Hafner, T. Lillicrap, M. Norouzi, and J. Ba Mastering atari with discrete world models . External Links: 2010.02193 , Link Cited by: §2 .

Hafner et al. (2024) D. Hafner, J. Pasukonis, J. Ba, and T. Lillicrap Mastering diverse domains through world models . External Links: 2301.04104 , Link Cited by: §1 , §2 .

Hafner et al. (2025) D. Hafner, W. Yan, and T. Lillicrap Training agents inside of scalable world models . External Links: 2509.24527 , Link Cited by: §2 .

Hansen et al. (2024) N. Hansen, H. Su, and X. Wang Td-mpc2: scalable, robust world models for continuous control . In International Conference on Learning Representations , Vol. 2024 , pp. 47376–47405 . Cited by: §C.4 , §1 , §2 .

Hansen et al. (2022) N. Hansen, X. Wang, and H. Su Temporal difference learning for model predictive control . External Links: 2203.04955 , Link Cited by: §2 .

Hansen-Estruch et al. (2023) P. Hansen-Estruch, I. Kostrikov, M. Janner, J. G. Kuba, and S. Levine IDQL: implicit q-learning as an actor-critic method with diffusion policies . External Links: 2304.10573 , Link Cited by: §C.4 , §2 , §2 .

Hubert et al. (2021) T. Hubert, J. Schrittwieser, I. Antonoglou, M. Barekatain, S. Schmitt, and D. Silver Learning and planning in complex action spaces . External Links: 2104.06303 , Link Cited by: §2 .

Intelligence et al. (2025) P. Intelligence, A. Amin, R. Aniceto, A. Balakrishna, K. Black, K. Conley, G. Connors, J. Darpinian, K. Dhabalia, J. DiCarlo, D. Driess, M. Equi, A. Esmail, Y. Fang, C. Finn, C. Glossop, T. Godden, I. Goryachev, L. Groom, H. Hancock, K. Hausman, G. Hussein, B. Ichter, S. Jakubczak, R. Jen, T. Jones, B. Katz, L. Ke, C. Kuchi, M. Lamb, D. LeBlanc, S. Levine, A. Li-Bell, Y. Lu, V. Mano, M. Mothukuri, S. Nair, K. Pertsch, A. Z. Ren, C. Sharma, L. X. Shi, L. Smith, J. T. Springenberg, K. Stachowicz, W. Stoeckle, A. Swerdlow, J. Tanner, M. Torne, Q. Vuong, A. Walling, H. Wang, B. Williams, S. Yoo, L. Yu, U. Zhilinsky, and Z. Zhou π 0.6 ∗ \pi^{*}_{0.6} : A vla that learns from experience . External Links: 2511.14759 , Link Cited by: §1 .

Jain et al. (2025) A. K. Jain, V. Mohta, S. Kim, A. Bhardwaj, J. Ren, Y. Feng, S. Choudhury, and G. Swamy A smooth sea never made a skilled sailor: robust imitation via learning to search . External Links: 2506.05294 , Link Cited by: §2 .

Janner et al. (2021) M. Janner, J. Fu, M. Zhang, and S. Levine When to trust your model: model-based policy optimization . External Links: 1906.08253 , Link Cited by: §2 .

Jiang et al. (2026a) Z. Jiang, K. Liu, Y. Qin, S. Tian, Y. Zheng, M. Zhou, C. Yu, H. Li, and D. Zhao World4RL: diffusion world models for policy refinement with reinforcement learning for robotic manipulation . External Links: 2509.19080 , Link Cited by: §2 .

Jiang et al. (2026b) Z. Jiang, S. Zhou, Y. Jiang, Z. Huang, M. Wei, Y. Chen, T. Zhou, Z. Guo, H. Lin, Q. Zhang, Y. Wang, H. Li, C. Yu, and D. Zhao WoVR: world models as reliable simulators for post-training vla policies with rl . External Links: 2602.13977 , Link Cited by: §2 .

Kaiser et al. (2024) L. Kaiser, M. Babaeizadeh, P. Milos, B. Osinski, R. H. Campbell, K. Czechowski, D. Erhan, C. Finn, P. Kozakowski, S. Levine, A. Mohiuddin, R. Sepassi, G. Tucker, and H. Michalewski Model-based reinforcement learning for atari . External Links: 1903.00374 , Link Cited by: §2 .

Kalweit and Boedecker (2017) G. Kalweit and J. Boedecker Uncertainty-driven imagination for continuous deep reinforcement learning . In Proceedings of the 1st Annual Conference on Robot Learning , S. Levine, V. Vanhoucke, and K. Goldberg (Eds.) , Proceedings of Machine Learning Research , Vol. 78 , pp. 195–206 . External Links: Link Cited by: §2 .

Kim et al. (2026) M. J. Kim, Y. Gao, T. Lin, Y. Lin, Y. Ge, G. Lam, P. Liang, S. Song, M. Liu, C. Finn, and J. Gu Cosmos policy: fine-tuning video models for visuomotor control and planning . External Links: 2601.16163 , Link Cited by: §2 .

Kurutach et al. (2018) T. Kurutach, I. Clavera, Y. Duan, A. Tamar, and P. Abbeel Model-ensemble trust-region policy optimization . External Links: 1802.10592 , Link Cited by: §2 .

Li and Levine (2026) Q. Li and S. Levine Q-learning with adjoint matching . arXiv preprint arXiv:2601.14234 . Cited by: §C.4 .

Liu et al. (2023) B. Liu, Y. Zhu, C. Gao, Y. Feng, Q. Liu, Y. Zhu, and P. Stone LIBERO: benchmarking knowledge transfer for lifelong robot learning . External Links: 2306.03310 , Link Cited by: §C.2 , §5 .

Liu et al. (2026) X. Liu, Z. Bai, H. Ci, K. Y. Ma, and M. Z. Shou World-vla-loop: closed-loop learning of video world model and vla policy . External Links: 2602.06508 , Link Cited by: §2 .

Ma et al. (2025) N. Ma, S. Tong, H. Jia, H. Hu, Y. Su, M. Zhang, X. Yang, Y. Li, T. Jaakkola, X. Jia, and S. Xie Inference-time scaling for diffusion models beyond scaling denoising steps . CoRR abs/2501.09732 . External Links: Link , Document Cited by: §2 .

Mandlekar et al. (2021) A. Mandlekar, D. Xu, J. Wong, S. Nasiriany, C. Wang, R. Kulkarni, L. Fei-Fei, S. Savarese, Y. Zhu, and R. Martín-Martín What matters in learning from offline human demonstrations for robot manipulation . External Links: 2108.03298 , Link Cited by: §C.2 , §5 .

Mark et al. (2023) M. S. Mark, A. Sharma, F. Tajwar, R. Rafailov, S. Levine, and C. Finn Offline retraining for online rl: decoupled policy learning to mitigate exploration bias . External Links: 2310.08558 , Link Cited by: §2 .

Nagabandi et al. (2018) A. Nagabandi, G. Kahn, R. S. Fearing, and S. Levine Neural network dynamics for model-based deep reinforcement learning with model-free fine-tuning . In 2018 IEEE International Conference on Robotics and Automation (ICRA) , Vol. , pp. 7559–7566 . External Links: Document Cited by: §2 .

Nair et al. (2021) A. Nair, A. Gupta, M. Dalal, and S. Levine AWAC: accelerating online reinforcement learning with offline datasets . External Links: 2006.09359 , Link Cited by: §2 .

Nakamoto et al. (2024) M. Nakamoto, Y. Zhai, A. Singh, M. S. Mark, Y. Ma, C. Finn, A. Kumar, and S. Levine Cal-ql: calibrated offline rl pre-training for efficient online fine-tuning . External Links: 2303.05479 , Link Cited by: §2 .

Park et al. (2025) S. Park, Q. Li, and S. Levine Flow q-learning . External Links: 2502.02538 , Link Cited by: §C.4 , §2 .

Peng et al. (2019) X. B. Peng, A. Kumar, G. Zhang, and S. Levine Advantage-weighted regression: simple and scalable off-policy reinforcement learning . External Links: 1910.00177 , Link Cited by: Appendix B .

Psenka et al. (2024) M. Psenka, A. Escontrela, P. Abbeel, and Y. Ma Learning a diffusion model policy from rewards via q-score matching . In Proceedings of the 41st International Conference on Machine Learning , R. Salakhutdinov, Z. Kolter, K. Heller, A. Weller, N. Oliver, J. Scarlett, and F. Berkenkamp (Eds.) , Proceedings of Machine Learning Research , Vol. 235 , pp. 41163–41182 . External Links: Link Cited by: §C.4 .

Schrittwieser et al. (2020) J. Schrittwieser, I. Antonoglou, T. Hubert, K. Simonyan, L. Sifre, S. Schmitt, A. Guez, E. Lockhart, D. Hassabis, T. Graepel, T. Lillicrap, and D. Silver Mastering atari, go, chess and shogi by planning with a learned model . Nature 588 ( 7839 ), pp. 604–609 . External Links: ISSN 1476-4687 , Link , Document Cited by: §2 .

Schrittwieser et al. (2021) J. Schrittwieser, T. Hubert, A. Mandhane, M. Barekatain, I. Antonoglou, and D. Silver Online and offline reinforcement learning by planning with a learned model . External Links: 2104.06294 , Link Cited by: §2 .

Sharma et al. (2026) A. K. Sharma, Y. Sun, N. Lu, Y. Zhang, J. Liu, and S. Yang World-gymnast: training robots with reinforcement learning in a world model . External Links: 2602.02454 , Link Cited by: §2 .

Silver et al. (2017) D. Silver, T. Hubert, J. Schrittwieser, I. Antonoglou, M. Lai, A. Guez, M. Lanctot, L. Sifre, D. Kumaran, T. Graepel, T. Lillicrap, K. Simonyan, and D. Hassabis Mastering chess and shogi by self-play with a general reinforcement learning algorithm . External Links: 1712.01815 , Link Cited by: §2 .

Snell et al. (2024) C. Snell, J. Lee, K. Xu, and A. Kumar Scaling LLM test-time compute optimally can be more effective than scaling model parameters . CoRR abs/2408.03314 . External Links: Link , Document Cited by: §2 .

Sutton (1991) R. S. Sutton Dyna, an integrated architecture for learning, planning, and reacting . SIGART Bull. 2 ( 4 ), pp. 160–163 . External Links: ISSN 0163-5719 , Link , Document Cited by: §2 .

Team et al. (2026) G. Team, B. Wang, B. Li, C. Ni, G. Huang, G. Zhao, H. Li, J. Li, J. Lv, J. Liu, L. Feng, M. Yu, P. Li, Q. Deng, T. Liu, X. Zhou, X. Chen, X. Wang, Y. Wang, Y. Li, Y. Nie, Y. Li, Y. Zhou, Y. Ye, Z. Liu, and Z. Zhu GigaBrain-0.5m*: a vla that learns from world model-based reinforcement learning . External Links: 2602.12099 , Link Cited by: §2 .

Vecerik et al. (2018) M. Vecerik, T. Hester, J. Scholz, F. Wang, O. Pietquin, B. Piot, N. Heess, T. Rothörl, T. Lampe, and M. Riedmiller Leveraging demonstrations for deep reinforcement learning on robotics problems with sparse rewards . External Links: 1707.08817 , Link Cited by: §2 .

Wagenmaker et al. (2025) A. Wagenmaker, M. Nakamoto, Y. Zhang, S. Park, W. Yagoub, A. Nagabandi, A. Gupta, and S. Levine Steering your diffusion policy with latent space reinforcement learning . External Links: 2506.15799 , Link Cited by: §C.4 .

Wan et al. (2025) T. Wan, A. Wang, B. Ai, B. Wen, C. Mao, C. Xie, D. Chen, F. Yu, H. Zhao, J. Yang, J. Zeng, J. Wang, J. Zhang, J. Zhou, J. Wang, J. Chen, K. Zhu, K. Zhao, K. Yan, L. Huang, M. Feng, N. Zhang, P. Li, P. Wu, R. Chu, R. Feng, S. Zhang, S. Sun, T. Fang, T. Wang, T. Gui, T. Weng, T. Shen, W. Lin, W. Wang, W. Wang, W. Zhou, W. Wang, W. Shen, W. Yu, X. Shi, X. Huang, X. Xu, Y. Kou, Y. Lv, Y. Li, Y. Liu, Y. Wang, Y. Zhang, Y. Huang, Y. Li, Y. Wu, Y. Liu, Y. Pan, Y. Zheng, Y. Hong, Y. Shi, Y. Feng, Z. Jiang, Z. Han, Z. Wu, and Z. Liu Wan: open and advanced large-scale video generative models . arXiv preprint arXiv:2503.20314 . Cited by: §4.4 .

Wang et al. (2024) S. Wang, S. Liu, W. Ye, J. You, and Y. Gao EfficientZero v2: mastering discrete and continuous control with limited data . In Proceedings of the 41st International Conference on Machine Learning , R. Salakhutdinov, Z. Kolter, K. Heller, A. Weller, N. Oliver, J. Scarlett, and F. Berkenkamp (Eds.) , Proceedings of Machine Learning Research , Vol. 235 , pp. 51041–51062 . External Links: Link Cited by: §C.4 , §2 .

Wang et al. (2022) X. Wang, J. Wei, D. Schuurmans, Q. V. Le, E. H. Chi, S. Narang, A. Chowdhery, and D. Zhou Self-consistency improves chain of thought reasoning in language models . CoRR abs/2203.11171 . External Links: Link , Document Cited by: §2 .

Yang et al. (2023) H. Yang, C. Yu, P. Sun, and S. Chen Hybrid policy optimization from imperfect demonstrations . In Advances in Neural Information Processing Systems (NeurIPS) , Vol. 36 , pp. 4653–4663 . Cited by: §2 .

Yang et al. (2026) J. Yang, K. Lin, J. Li, W. Zhang, T. Lin, L. Wu, Z. Su, H. Zhao, Y. Zhang, L. Chen, P. Luo, X. Yue, and H. Li RISE: self-improving robot policy with compositional world model . External Links: 2602.11075 , Link Cited by: §2 .

Ye et al. (2021) W. Ye, S. Liu, T. Kurutach, P. Abbeel, and Y. Gao Mastering atari games with limited data . External Links: 2111.00210 , Link Cited by: §2 .

Zhang et al. (2023) H. Zhang, W. Xu, and H. Yu Policy expansion for bridging offline-to-online reinforcement learning . External Links: 2302.00935 , Link Cited by: §2 .

Zhang et al. (2019) M. Zhang, S. Vikram, L. Smith, P. Abbeel, M. J. Johnson, and S. Levine SOLAR: deep structured representations for model-based reinforcement learning . External Links: 1808.09105 , Link Cited by: §2 .

Zhu et al. (2025) F. Zhu, Z. Yan, Z. Hong, Q. Shou, X. Ma, and S. Guo WMPO: world model-based policy optimization for vision-language-action models . External Links: 2511.09515 , Link Cited by: §2 .

## Appendix A Author Contributions

PD conceived the idea, devised the algorithm, and led the project. PD implemented the initial prototype, ran experiments, provided hands-on guidance on all experiments, and analyzed and interpreted the results. PD also wrote and positioned the paper. YJ led maintenance of the research codebase, conducted experiments, and produced the figures and videos. CF and DS contributed to the research design, advised the project, edited and positioned the paper.

## Appendix B Additional Experiments

To isolate the benefit of performing test-time search with a Q Q -function, we compare against a variant that learns only a state value function V V and searches with it. Here we fit V V , form an advantage estimate, and optimize the policy by advantage-weighted regression ( Peng et al., 2019 ) . We evaluate this variant both as the edit policy within EXPO and as a standalone method. Results are reported in Figure 8 and Figure 9 . Searching with V V substantially underperforms searching on top of Q-learning across all settings. We attribute this to two factors: the Q-function supplies an additional action-conditioned estimator that V V alone cannot provide, which yields a stronger estimator overall, and the underlying Q Q -learning base algorithm is itself stronger. These results motivate leveraging world models for Q-learning rather than performing search with V V as typically done with model-based RL.

## Appendix C Experiment Details

### C.1 Hyperparameters

For the state-based Robomimic experiments, QWM and all model-free baselines follow the same online RL protocol, including identical demonstration sources, online interaction budgets, and optimization settings. Unless otherwise specified, all methods start online training after 5,000 environment steps, use an offline data ratio of 0.5, do not perform additional offline pretraining, and use an update-to-data (UTD) ratio of 20 with batch size 256. For Q-learning-based methods, we use a critic TD discount γ = 0.99 \gamma=0.99 and a target network update coefficient τ = 0.005 \tau=0.005 . Importantly, γ \gamma is used only in the Bellman TD backup of the critic and is distinct from the tree-search discount λ \lambda , which controls the contribution of deeper future values during search. For EfficientZero V2, we follow the official training protocol provided by the authors and use its recommended UTD ratio of 0.4.

#### QWM -specific hyperparameters.

We instantiate QWM on top of two base RL algorithms, EXPO and RLPD. For both variants, the original policy and critic optimization procedures are kept unchanged, while world-model-guided tree search is additionally used for action selection during online interaction and evaluation.

At each state node, the policy proposes N N candidate actions, and each action is evaluated through K K world-model predictions. To control the size of the search tree, we retain at most J J partial paths during intermediate expansion, following the pruning procedure described in Section 4.4 . We use max aggregation for both intermediate-node values and leaf values. Specifically, intermediate-node aggregation combines the values of candidate actions and their predicted future states in the recursive value computation in Equation 8 , while leaf aggregation combines the N leaf N_{\text{leaf}} Q-values sampled at the final search depth in Equation 7 . The same max aggregation is used when combining world-model branches in the root action score. The tree-search settings are summarized in Table 2 . Here, λ \lambda is used only within the tree-search value recursion and is independent of the critic TD discount γ \gamma . We note that this λ \lambda removes the factor of 1 2 \frac{1}{2} in Equation 9 and Equation 8 , and to exactly match the equations the λ \lambda in the table should be multiplied by 1 2 \frac{1}{2} .

### C.2 Environments

We evaluate QWM on two widely used robotic manipulation benchmarks: Robomimic ( Mandlekar et al., 2021 ) and LIBERO ( Liu et al., 2023 ) . These benchmarks provide diverse manipulation tasks with human-collected demonstrations and are commonly used to evaluate offline-to-online robot learning algorithms.

Robomimic. For state-based experiments, we evaluate QWM on four manipulation tasks from Robomimic: Lift, Can, Square, and Tool Hang. These tasks cover diverse manipulation capabilities, including object grasping and lifting, object relocation, precise insertion, and long-horizon assembly. We use the low-dimensional state observations provided by Robomimic, consisting of robot proprioception and object-related features, including end-effector pose, gripper states, and object states. The action space is a 7-DoF operational space control (OSC) command.

Following prior work, we use different demonstration settings for different tasks. Lift uses a 10-episode subset of the original dataset to create a more challenging evaluation setting, Can uses the multi-human (MH) dataset, and Square and Tool Hang use the standard proficient-human (PH) split. The PH dataset contains demonstrations collected by a single proficient teleoperator, while the MH dataset contains demonstrations collected by multiple teleoperators with varying levels of expertise. All experiments follow the standard Robomimic evaluation protocol and report online success rates.

LIBERO. For pixel-based experiments, we evaluate QWM on five tasks from the LIBERO benchmark. LIBERO is a language-conditioned lifelong robot learning benchmark designed to evaluate knowledge transfer and generalization in robotic manipulation. It contains diverse manipulation tasks with different object configurations, spatial arrangements, and task semantics.

We follow the task selection and evaluation protocol used in prior work and evaluate on five representative tasks (Task 60, Task 79, Task 29, Task 28, and Task 2). The agent receives RGB observations from the robot cameras and generates actions conditioned on visual observations and task instructions. We use the standard LIBERO simulation setup and report online success rates averaged over evaluation episodes.

### C.3 Additional World Model Details and Prediction Quality

We provide additional training and inference details for the world models used in our experiments. For the state-based experiments, the dynamics model is pretrained offline on demonstration transitions ( s , a , s ′ ) (s,a,s^{\prime}) using an MSE objective with Adam, a learning rate of 3 × 10 − 4 3\times 10^{-4} , batch size 256, and 100k gradient steps, and is kept fixed throughout subsequent policy and critic optimization. For the vision-based experiments, we fine-tune the action-conditioned Wan2.2-TI2V-5B world model on demonstration videos paired with aligned raw action sequences. Before training, video clips are encoded once by the frozen Wan2.2 VAE and text prompts are encoded by the frozen umT5-XXL encoder, allowing both representations to be cached and removed from the training loop. We then jointly fine-tune the diffusion transformer and action encoder using the standard Wan2.2 flow-matching objective, while keeping the VAE and text encoder frozen. Training uses AdamW with a learning rate of 1 × 10 − 5 1\times 10^{-5} , a per-GPU batch size of 1 on 8 GPUs, bfloat16 precision, gradient checkpointing, and 200k gradient steps. For LIBERO, we train on 5-frame 128 × 128 128\times 128 clips and model the agent-view and wrist-camera observations as two video streams. During tree search, however, each world-model query advances the rollout by only one step: we use the second frame of the generated clip as the predicted next observation, and then condition a new generation on this prediction for subsequent tree expansion. At inference time, we use 1 denoising step. To examine the next-step generation quality of the resulting world model, Figure 10 compares the generated next observation with the corresponding ground-truth next observation conditioned on the same current observation and action. The predictions capture the task-relevant changes in robot configuration and object motion at the next step, supporting their use as predicted future observations during tree search.

### C.4 Comparisons

We evaluate QWM against both state-of-the-art model-free algorithms and model-based algorithms, as while QWM uses a learned model, it does not use data from the model for training and is trained on top of standard Q-learning.

Model-free baselines. The first set of comparisons is against state-of-the-art model-free algorithms. As QWM learns with only data in the real world instead of from the model, we compare against other such methods to evaluate effectiveness.

EXPO ( Dong et al., 2025b ) . EXPO jointly learns an expressive base policy and a lightweight edit policy, where the edit policy transforms actions sampled from the base policy toward higher-value distributions.

IDQL ( Hansen-Estruch et al., 2023 ) . IDQL trains a diffusion policy through behavior modeling and performs implicit policy extraction using best-of- N N sampling, selecting the candidate action with the highest Q-value.

RLPD ( Ball et al., 2023 ) . RLPD is a sample-efficient off-policy RL method that leverages replay data with high update-to-data ratios, critic ensembles, and a Gaussian policy.

QSM ( Psenka et al., 2024 ) . QSM incorporates gradients from the learned Q-function into the diffusion training objective, guiding the denoising process toward high-value actions through score matching.

DSRL ( Wagenmaker et al., 2025 ) . DSRL adapts a frozen diffusion-based behavior cloning policy by performing reinforcement learning over the initial noise used for action generation, learning a policy that predicts the noise seed.

QAM ( Li and Levine, 2026 ) . QAM uses adjoint matching to propagate value gradients through the diffusion trajectory and constructs policy optimization objectives based on the learned Q-function.

FQL ( Park et al., 2025 ) . FQL trains a one-step flow policy to maximize Q-values learned with a temporal-difference objective, while regularizing the policy toward a behavior-cloned flow policy.

Model-based baselines. The second category of comparison methods consists of model-based RL algorithms, which similarly learn a dynamics model but, unlike our approach, use this model directly for training.

TD-MPC2 ( Hansen et al., 2024 ) . TD-MPC2 learns an implicit latent world model and performs short-horizon MPPI planning in latent space. It evaluates sampled action sequences using predicted rewards and bootstrapped terminal values, with a learned maximum-entropy policy prior guiding the sampling process.

EfficientZero V2 ( Wang et al., 2024 ) . EfficientZero V2 learns a MuZero-style latent world model and performs Sampling-based Gumbel tree search for both discrete and continuous control. The search provides bootstrapped policy and value targets that are reused for policy and value training.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
