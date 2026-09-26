##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Self-Improving World Modelling with Latent Actions

###### Abstract

Internal modelling of the world—predicting transitions between previous states X X and next states Y Y under actions Z Z —is essential to reasoning and planning for LLMs and VLMs. Learning such models typically requires costly action-labelled trajectories. We propose SWIRL , a self-improvement framework that learns from state-only sequences by treating actions as a latent variable and alternating between Forward World Modelling (FWM) P θ ​ ( Y | X , Z ) P_{\theta}(Y|X,Z) and an Inverse Dynamics Modelling (IDM) Q ϕ ​ ( Z | X , Y ) Q_{\phi}(Z|X,Y) . SWIRL iterates two phases: (1) Variational Information Maximisation, which updates the FWM to generate next states that maximise conditional mutual information with latent actions given prior states, encouraging identifiable consistency; and (2) ELBO Maximisation, which updates the IDM to explain observed transitions, effectively performing coordinate ascent. Both models are trained with reinforcement learning (specifically, GRPO) with the opposite frozen model’s log-probability as a reward signal. We provide theoretical learnability guarantees for both updates, and evaluate SWIRL on LLMs and VLMs across multiple environments: single-turn and multi-turn open-world visual dynamics and synthetic textual environments for physics, web, and tool calling. SWIRL achieves gains of 16% on Aurora-Bench , 28% on ByteMorph, 16% on WorldPredictionBench , and 14% on StableToolBench . 1 1 1 The code and models developed in this paper will be made available at https://github.com/yfqiu-nlp/swirl .

###### Keywords:

## 1 Introduction

Intrinsic world modelling is a model’s latent understanding of the environment and agent dynamics, i.e., trajectories of states and actions, which enables simulating possible futures without hallucinations. Large foundation models, such as Large Language Models (LLMs) and Vision-Language Models (VLMs), have arguably been shown to internalise world modelling to some extent during their training, thus enabling reasoning and planning without an external, specialised world model ( Vafa et al., 2024 ; Qiu et al., 2024 ; Liu et al., 2025b ; Chen et al., 2025b ; Wang et al., ; Xiong et al., 2026 ) . For example, explicitly training models to predict the results of invoking tools ( Guo et al., 2025b ) or executing code ( Copet et al., 2025 ) significantly enhances tool calling and coding tasks. This ability can also transfer to spatial reasoning tasks ( Qiu et al., 2025 ; Tehenan et al., 2025 ) and reduce hallucinations that contradict external regularities ( Liu et al., 2025a ; Chen et al., 2025b ) .

While promising, the development of robust internal world models faces a significant bottleneck in data scalability. Current approaches rely heavily on execution logs or trajectories where observations are densely annotated with specific actions, because such annotations are naturally available in restricted environments (e.g., logs for tool calling or coding). However, for open-world tasks, collecting manual annotations for every transition is prohibitively expensive and intractable. Moreover, an additional challenge is the inherent ambiguity of inverse dynamics : a transition between two states may be explained by multiple valid actions, making purely supervised learning brittle when data is sparse.

Inspired by recent advances in self-improving learning for other applications ( Wang et al., 2025a ; Wang et al., 2025c ; Jin et al., 2025 ; Mao et al., 2025 ; Jin et al., 2025 ) , we propose SWIRL (Self-improving World modelling with Iterative RL), a reciprocal optimisation framework to enhance the intrinsic world modelling of LLMs and VLMs from state-only sequences where the intermediate action is latent. We formalise world modelling as two components ( Wang et al., 2025b ; Qiu et al., 2025 ; Chen et al., 2025a ) : Forward World Modelling (FWM; predicting the next state y y given current state and latent action x , z x,z ), and Inverse Dynamics Model (IDM; inferring latent action z z given states x , y x,y ). In our reciprocal framework, we optimise the FWM P θ P_{\theta} to generate futures that are consistently identifiable by the IDM, and the IDM Q ϕ Q_{\phi} to infer actions that maximise the likelihood of the state dynamics predicted by the FWM. From a variational inference perspective, we theoretically prove that the optimisation of FWM is equivalent to maximising a lower bound on the Conditional Mutual Information I ⁡ ( Z ; Y ^ | X ) I(Z;\hat{Y}|X) ( Barber and Agakov, 2003 ) between the latent Z Z and future states Y ^ \hat{Y} predicted by the FWM; and that the optimisation of the IDM is equivalent to performing coordinate ascent on the Evidence Lower Bound (ELBO) of the log-likelihood log ⁡ P θ ​ ( Y | X ) \log P_{\theta}(Y|X) . Without relying on ground-truth action annotations, we optimise such a reciprocal framework with Group Relative Policy Optimisation (GRPO; Guo et al. 2025a ). FWM and IDM take alternating roles of policy and reward, iterating until both components converge.

We validate our framework across four distinct environments on six benchmarks: open-world visual dynamics for VLMs on Aurora-Bench , ByteMorph and WorldPredictionBench , synthetic textual worlds on ScienceWorld , web HTML on Mind2Web , and tool calling on StableToolBench for LLMs. Empirical results confirm that our reciprocal self-improving allows models to learn effective dynamics from unlabelled state sequences, outperforming supervised fine-tuning baselines and achieving parity with larger, state-of-the-art models. Our contributions are summarised as follows: • We propose a novel self-improving framework for world modelling in LLMs and VLMs, reciprocally reinforcing FWM and IDM without action annotations.

• We provide a rigorous theoretical proof that SWIRL corresponds to alternating between maximising Variational Mutual Information and Evidence Lower Bound.

• Empirical evidence on six benchmarks across visual, textual, web, tool calling environments demonstrates that SWIRL models effectively self-improve, leading to more enhanced forward world modelling capabilities.

## 2 Related Work

#### Intrinsic World Models.

Recent research has explored whether internalised world models emerge in LLMs and VLMs through careful evaluation. Vafa et al. (2024) assessed whether the models’ representations truly capture coherent world dynamics ( Xiong et al., 2026 ) . Similarly, Tehenan et al. (2025) and Qiu et al. (2024) found evidence that LLMs implicitly encode spatial and temporal relationships to some degree. World modelling also emerges naturally during the pre-training of large unified VLMs ( Deng et al., 2025 ; Cui et al., 2025 ) and from video-based training ( Chen et al., 2025b ; Qiu et al., 2025 ) .

In addition, previous work established that explicit world modelling can boost performance in downstream applications. For instance, Copet et al. (2025) proposed the Coding World Model for programming, and Lehrach et al. (2025) extended this approach to game-playing environments. Modelling the outcomes of function tool calls ( Guo et al., 2025b ) or planning ( Li et al., 2025 ) had similar effects. As a result, dedicated post-training pipelines have been proposed to endow LLMs ( Xie et al., 2025 ) and VLMs ( Xiang et al., 2024 ) with explicit world modelling capabilities. Extensive benchmarks for evaluation have been proposed, including forward and inverse dynamics prediction ( Chen et al., 2025a ; Wang et al., 2025b ; Gao et al., 2025 ) .

#### Self-Improving Learning.

Self-improving learning refers to models learning from their own (possibly curated) signals without external supervision. Huang et al. (2023) showed that LLMs can generate high-confidence answers and fine-tune themselves on these outputs to improve reasoning. Bensal et al. (2025) proposed a self-reflection and reinforcement learning loop where models analyse mistakes and retry, boosting performance on tasks like maths and function calling. Lee et al. () introduce a curriculum in which models iteratively generate and filter correct answers, progressively tackling harder problems, while Zhao et al. (2024) demonstrate that self-synthesised input–output pairs improve classification and generation quality. ( Wang et al., 2025a ) enhance self-improvement capabilities of agents with a skill library. LLM’s coding and unit test generation capabilities can also co-evolve iterating on each other’s outcomes ( Wang et al., 2025c ) . Similarly, VLMs can refine visual and language reasoning using self-generated corrections ( He et al., 2025 ) .

In unified VLMs ( Deng et al., 2025 ; Wu et al., 2024 ; Lin et al., 2025 ; Xiao et al., 2025 ) , understanding performance often exceeds generation ( Shi et al., 2025 ; Ma et al., 2025 ; Qu et al., 2025 ; Zheng et al., 2025 ; Zhang et al., 2025 ) . A common strategy is then to use the understanding head as a critic to guide generation with carefully designed rubrics or heuristics ( Mao et al., 2025 ; Jin et al., 2025 ; Qiu et al., 2026 ) . Unlike these approaches, SWIRL theoretically and empirically proves the effectiveness of utilising the predicted likelihoods from understanding (action prediction) and generation (next state prediction) to establish a reciprocal cycle for VLMs where improvements in the generation head also enhance the understanding head, and vice versa.

## 3 Methodology

### 3.1 Task Formulation

We consider transitions from a source state x ∈ 𝒮 x\in\mathcal{S} to a target state y ∈ 𝒮 y\in\mathcal{S} , mediated by a latent action z ∈ 𝒜 z\in\mathcal{A} . Following Qiu et al. (2025) and Wang et al. (2025b) , we parametrise world modelling using two components: i) Forward World Modelling (FWM) : P θ ​ ( y | x , z ) P_{\theta}(y|x,z) , which predicts the next state given previous state and action; and ii) Inverse-Dynamics Prediction (IDM): Q ϕ ​ ( z | x , y ) Q_{\phi}(z|x,y) , which infers the action given the state transition. The parameters θ \theta and ϕ \phi can be either disjoint or shared.

We consider four classes of environments with different observation–action formulations. In real-world visual environments, observations are pixel-level visual inputs and actions are specified in natural language. We study this setting using unified vision–language models (VLMs) capable of perceiving and generating interleaved image–text sequences. In synthetic textual environments, both observations and actions are expressed purely in language and are governed by an underlying simulator, which we model using large language models (LLMs). In web-based environments, states and actions correspond to raw HTML and interaction logs, respectively, while in tool-use settings, actions are tool calls and observations consist of the conversational context and tool execution outcomes.

### 3.2 SWIRL

#### Intuition.

SWIRL alternates between two tightly coupled optimisation phases. In the first phase, we optimise the Forward World Model (FWM), P θ P_{\theta} , to generate future states that are identifiable by the Inverse Dynamics Model (IDM). This enforces identifiability in forward prediction. In Eq. 2 below, we prove that this objective is equivalent to maximising a variational lower bound on the conditional mutual information I ⁡ ( Z ; Y ^ | X ) I(Z;\hat{Y}|X) ( Barber and Agakov, 2003 ) , encouraging the predicted futures Y ^ \hat{Y} to retain maximal information about the underlying latent actions Z Z .

In the second phase, we optimise the IDM, Q ϕ Q_{\phi} , to improve data fidelity by inferring actions that best explain the observed state transitions under the learned FWM. We formally justify this step by proving that the resulting objective corresponds to maximising the Evidence Lower Bound (ELBO) of the inverse model (see Eq. 5 below).

#### Objectives.

As depicted in Algorithm 1 , we rely only on state-only sequences ( x t , y t + 1 ) (x_{t},y_{t+1}) as data. In the first phase of each iteration of SWIRL , we optimise FWM as a policy based on the frozen IDM rewards. Let P θ P_{\theta} denote the FWM policy parametrised by θ \theta . For each training step in GRPO ( Guo et al., 2025a ) , we first sample a latent action z t ∼ Q ϕ ( ⋅ ∣ x t , y t ) z_{t}\sim Q_{\phi}(\cdot\mid x_{t},y_{t}) from the IDM. Then, we sample a group of G G rollouts { y ^ t + 1 ( k ) } k = 1 G \{\hat{y}_{t+1}^{(k)}\}_{k=1}^{G} from P θ ( ⋅ ∣ x t , z t ) P_{\theta}(\cdot\mid x_{t},z_{t}) . To evaluate their quality, we use a frozen IDM model Q ϕ Q_{\phi} prompted for the IDM task, which estimates the likelihood of the action z t z_{t} given the generated transition: P π ϕ ​ ( z t ∣ x t , y ^ t + 1 ( k ) ) . P_{\pi_{\phi}}(z_{t}\mid x_{t},\hat{y}_{t+1}^{(k)}). The reward for the k k -th rollout is defined as r k = log ⁡ Q ϕ ​ ( z t ∣ x t , y ^ t + 1 ( k ) ) . r_{k}=\log Q_{\phi}(z_{t}\mid x_{t},\hat{y}_{t+1}^{(k)}). This reward enforces that a predicted future is considered plausible only if IDM can retrospectively explain the action that led to the predicted state. We then optimise P θ P_{\theta} to maximise the advantage induced by these rewards.

After the FWM policy converges, we invert the optimisation direction to refine the IDM. In this phase, the optimised FWM model is frozen and used as the reward signal. The policy Q ϕ Q_{\phi} is prompted for the IDM task, generating action candidates { z ^ t ( i ) } i = 1 G \{\hat{z}_{t}^{(i)}\}_{i=1}^{G} given a state transition ( x t , y t + 1 ) (x_{t},y_{t+1}) . Each candidate action is evaluated by querying the FWM for the likelihood of the target observation: r k = log ⁡ P π θ ​ ( y t + 1 ∣ x t , z ^ t ( k ) ) . r_{k}=\log P_{\pi_{\theta}}(y_{t+1}\mid x_{t},\hat{z}_{t}^{(k)}). This reward favours data fidelity with respect to the state transition. We alternate between FWM and IDM optimisation phases, swapping the roles of policy and reward model until convergence. This reciprocal training paradigm ensures that improvements in forward prediction directly enhance action inference by the inverse dynamic model, and vice versa, driving the system toward a globally consistent both given all unlabelled observations.

### 3.3 Theoretical Analysis

Phase I encourages that generated futures are distinguishable (high mutual information), allowing the FWM to produce distinct outcomes for varied latent actions. Phase II encourages that inferred actions are plausible (high likelihood), allowing the IDM to map transitions to actions that the FWM can reproduce.

#### Phase I: FWM optimisation via Variational Information Maximisation.

In this phase, we freeze ϕ \phi and update θ \theta to generate next states y ^ \hat{y} that are identifiable by the inference model. We formalise this as maximising the Conditional Mutual Information (CMI) I ⁡ ( Z ; Y ^ | X ) I(Z;\hat{Y}|X) with respect to the empirical belief distribution of the model. Let P ~ ​ ( z | x ) ≜ 𝔼 y ∼ 𝒟 ⁡ ( y | x ) ​ [ Q ϕ ​ ( z | x , y ) ] \tilde{P}(z|x)\triangleq\mathbb{E}_{y\sim\mathcal{D}(y|x)}[Q_{\phi}(z|x,y)] denote the marginal distribution of latent actions inferred by the IDM over the dataset.

###### Theorem 3.1 (FWM Lower Bound) .

Optimising the FWM to maximise the log-probability assigned to generated samples by the frozen IDM maximises a variational lower bound on the Conditional Mutual Information I P ~ ​ ( Z ; Y ^ | X ) I_{\tilde{P}}(Z;\hat{Y}|X) defined over the empirical belief distribution P ~ ​ ( z | x ) \tilde{P}(z|x) .

###### Proof.

The mutual information under the data-induced joint distribution P ⁡ ( x ) ​ P ~ ​ ( z | x ) ​ P θ ​ ( y ^ | x , z ) P(x)\tilde{P}(z|x)P_{\theta}(\hat{y}|x,z) is: I ⁡ ( Z ; Y ^ | X ) = 𝔼 x ∼ 𝒟 ​ [ H P ~ ​ ( Z | X ) − H ⁡ ( Z | Y ^ , X ) ] . I(Z;\hat{Y}|X)=\mathbb{E}_{x\sim\mathcal{D}}\left[H_{\tilde{P}}(Z|X)-H(Z|\hat{Y},X)\right]. (1) The entropy of the latent belief H P ~ ​ ( Z | X ) H_{\tilde{P}}(Z|X) depends only on the frozen IDM and data distribution, and is thus constant w.r.t. θ \theta . Maximising CMI is therefore equivalent to minimizing the conditional entropy H ⁡ ( Z | Y ^ , X ) H(Z|\hat{Y},X) . We use the variational posterior Q ϕ ​ ( z | x , y ^ ) Q_{\phi}(z|x,\hat{y}) as a proxy for the intractable true posterior P θ ​ ( z | y ^ , x ) P_{\theta}(z|\hat{y},x) ( Barber and Agakov, 2003 ) to bound the entropy term: − H \displaystyle-H ( Z | Y ^ , X ) = 𝔼 x , z ∼ P ~ , y ^ ∼ P θ ​ [ log ⁡ P θ ​ ( z | y ^ , x ) ] \displaystyle(Z|\hat{Y},X)=\mathbb{E}_{x,z\sim\tilde{P},\hat{y}\sim P_{\theta}}[\log P_{\theta}(z|\hat{y},x)] (2) ≥ 𝔼 x ∼ 𝒟 𝔼 z ∼ P ~ ​ ( z | x ) 𝔼 y ^ ∼ P θ ( ⋅ | x , z ) [ log Q ϕ ( z | x , y ^ ) ] . \displaystyle\geq\mathbb{E}_{x\sim\mathcal{D}}\mathbb{E}_{z\sim\tilde{P}(z|x)}\mathbb{E}_{\hat{y}\sim P_{\theta}(\cdot|x,z)}[\log Q_{\phi}(z|x,\hat{y})]. Substituting the definition of P ~ ​ ( z | x ) \tilde{P}(z|x) creates the following objective: 𝒥 ( θ ) = 𝔼 ( x , y ) ∼ 𝒟 𝔼 z ∼ Q ϕ ( ⋅ | x , y ) 𝔼 y ^ ∼ P θ ( ⋅ | x , z ) [ log Q ϕ ( z | x , y ^ ) ] . \mathcal{J}(\theta)=\mathbb{E}_{(x,y)\sim\mathcal{D}}\mathbb{E}_{z\sim Q_{\phi}(\cdot|x,y)}\mathbb{E}_{\hat{y}\sim P_{\theta}(\cdot|x,z)}[{\log Q_{\phi}(z|x,\hat{y})}]. (3) This matches Algorithm 1 : we sample trajectories ( x , y ) (x,y) , infer z z using the IDM, rollout y ^ \hat{y} using the FWM, and reward the FWM with the IDM’s log likelihood. The gradient of Eq. 3 is ∇ θ 𝒥 ( θ ) = 𝔼 ( x , y ) ∼ 𝒟 𝔼 z ∼ Q ϕ ( ⋅ | x , y ) 𝔼 y ^ ∼ P θ ( ⋅ | x , z ) [ log Q ϕ ( z ∣ x , y ^ ) ∇ θ log P θ ( y ^ ∣ x , z ) ] \nabla_{\theta}\mathcal{J}(\theta)=\mathbb{E}_{(x,y)\sim\mathcal{D}}\mathbb{E}_{z\sim Q_{\phi}(\cdot|x,y)}\mathbb{E}_{\hat{y}\sim P_{\theta}(\cdot|x,z)}[\log Q_{\phi}(z\mid x,\hat{y})\nabla_{\theta}\log P_{\theta}(\hat{y}\mid x,z)] , for which Group Relative Policy Optimisation (GRPO) offers an estimator: ∇ θ 𝒥 ^ GRPO ​ ( θ ) = 1 G ​ ∑ k = 1 G A k F ​ ∇ θ ​ log ⁡ P θ ​ ( y ^ k ∣ x , z ) , \widehat{\nabla_{\theta}\mathcal{J}}_{\text{GRPO}}(\theta)=\frac{1}{G}\sum_{k=1}^{G}A^{\text{F}}_{k}\nabla_{\theta}\log P_{\theta}(\hat{y}_{k}\mid x,z), (4) where A k A_{k} are the group-relative advantages derived from rewards R k = log ⁡ Q ϕ ​ ( z ∣ x , y ^ k ) R_{k}=\log Q_{\phi}(z\mid x,\hat{y}_{k}) . ∎

#### Phase II: IDM optimisation via ELBO Maximisation.

In the second phase, we freeze θ \theta and optimise ϕ \phi . The goal is to infer actions z z that explain the transition ( x , y ) (x,y) in the FWM dynamics, while staying close to the valid prior. We treat the initialised model at each iteration as an informative prior P ⁡ ( z | x ) ≜ π ref ​ ( z | x ) P(z|x)\triangleq\pi_{\text{ref}}(z|x) . This corresponds to maximising the Evidence Lower Bound (ELBO).

###### Theorem 3.2 (IDM Lower Bound) .

Optimising the IDM via the KL-regularised policy gradient objective, with reward R = log ⁡ P θ ​ ( y | x , z ) R=\log P_{\theta}(y|x,z) , β = 1 \beta=1 , reference policy π ref \pi_{\mathrm{ref}} maximises the ELBO objective where the prior is defined by π ref \pi_{\mathrm{ref}} .

###### Proof.

We seek to maximise the marginal log-likelihood log ⁡ P θ ​ ( y | x ) \log P_{\theta}(y|x) . By introducing the variational distribution Q ϕ ​ ( z | x , y ) Q_{\phi}(z|x,y) and the informative prior P ⁡ ( z | x ) = π ref ​ ( z | x ) P(z|x)=\pi_{\text{ref}}(z|x) , we derive the ELBO: log ⁡ P θ ​ ( y | x ) = log ⁡ 𝔼 z ∼ Q ϕ ​ [ P θ ​ ( y | x , z ) ​ P ​ ( z | x ) Q ϕ ​ ( z | x , y ) ] ≥ 𝔼 z ∼ Q ϕ ( ⋅ | x , y ) [ log P θ ( y | x , z ) ] − D KL ( Q ϕ ( z | x , y ) | | P ( z | x ) ) ≜ ℒ ELBO . \begin{split}\log P_{\theta}(y|x)&=\log\mathbb{E}_{z\sim Q_{\phi}}\left[\frac{P_{\theta}(y|x,z)P(z|x)}{Q_{\phi}(z|x,y)}\right]\\ &\geq\mathbb{E}_{z\sim Q_{\phi}(\cdot|x,y)}\left[\log P_{\theta}(y|x,z)\right]\\ &-D_{\mathrm{KL}}(Q_{\phi}(z|x,y)\,||\,P(z|x))\triangleq\mathcal{L}_{\text{ELBO}}.\end{split} The KL-regularised policy gradient objective is defined as the expected reward subject to a KL constraint weighted with β = 1 \beta=1 against the reference policy: 2 2 2 In practice, we may allow β \beta to be tunable for adjusting the deviation against the reference policy, as the common practice in GRPO. 𝒥 ⁡ ( ϕ ) = 𝔼 z ∼ Q ϕ ​ [ R ⁡ ( x , z , y ) ] − D KL ( Q ϕ ( ⋅ | x , y ) | | π ref ( ⋅ | x ) ) . \displaystyle\begin{split}\mathcal{J}(\phi)&=\mathbb{E}_{z\sim Q_{\phi}}[R(x,z,y)]\\ &-D_{\mathrm{KL}}(Q_{\phi}(\cdot|x,y)||\pi_{\text{ref}}(\cdot|x)).\end{split} (5) By setting the reward R ⁡ ( x , z , y ) = log ⁡ P θ ​ ( y | x , z ) R(x,z,y)=\log P_{\theta}(y|x,z) and identifying the prior P ⁡ ( z | x ) P(z|x) with the reference policy π ref ​ ( z | x ) \pi_{\text{ref}}(z|x) , we observe that 𝒥 ⁡ ( ϕ ) ≡ ℒ ELBO \mathcal{J}(\phi)\equiv\mathcal{L}_{\text{ELBO}} . We again use the GRPO as the estimator to perform coordinate ascent on the ELBO. ∎

## 4 Experiments and Results

### 4.1 Experimental Setup

#### Models.

We choose Liquid ( Wu et al., 2024 ) as our base VLM as the publicly best 7B-size unified VLM with an autoregressive architecture. The medium size limits the scale requirements for the compute infrastructure, and the autoregressive nature allows for applying GRPO off-the-shelf (without ad-hoc adaptations for diffusion-based generation). For text-based environments, we use Qwen-2.5-3B-Instruct ( Qwen Team, 2024 ) , a competitive mid-size LLM.

#### SFT Warm-up.

Since our base VLMs/LLMs are general-purpose, they lack the specific interface capabilities required for environments (e.g., Liquid cannot natively predict image conditioning on both image and textual action). Prior to SWIRL , we conduct an initial SFT, which is strictly viewed as policy initialisation to ensure the model outputs valid actions and states; without this, a random policy would generate outputs rendering RL exploration impossible (as evidenced by Liquid’s poor zero-shot performance in GEdit-Bench in Appendix C ). For VLMs, we utilise image editing mixtures from Pico-banana-400K ( Qian et al., 2025 ) and Aurora ( Krojer et al., 2024 ) . 3 3 3 As a sanity check, we report the zero-shot and SFT performance of Liquid on GEdit-Bench compared to other VLMs in Appendix C . For LLMs, we fine-tune on the half of environment-specific episodes, and remain the rest discarding the annotated actions for SWIRL .

#### Iterative RL.

For SWIRL , we first conduct controlled experiments on the unlabelled video mixture from UCF-101 ( Soomro et al., 2012 ) , Movement-in-Times ( Monfort et al., 2019 ) , Kinetics700 ( Kay et al., 2017 ) , limiting training to the first phase IDM → \rightarrow FWM of SWIRL . This setup enables strict comparison with the bootstrapping baseline of Qiu et al. (2025) and allows us to observe stable convergence within a single epoch. After this controlled phase, we scale training by uniformly sampling 30K videos per iteration from a large-scale unlabelled video corpus, VidGen-1M ( Tan et al., 2024 ) . We extract the frame pairs from videos as in ( Chen et al., 2025d ) . Each iteration is trained for one epoch, and the model alternates between FWM and IDM optimisation phases as described in Section 3.2 . This protocol ensures a clean comparison to baselines in ( Qiu et al., 2025 ) while measuring the improvement across iterations.

#### Benchmarks.

We evaluate visual world modelling under two settings. Firstly, for single-turn next-observation prediction, we use Aurora-Bench and ByteMorph , both of which formulate dynamics prediction as action-conditioned image editing tasks with a strong emphasis on correctness in action-centric dynamics. Secondly, to evaluate long-horizon world modelling, we adopt WorldPredictionBench , which supports multi-step rollouts of up to four future observations across five subtasks, enabling a comprehensive assessment of FWM consistency.

To validate the generalisation of SWIRL , we conduct experiments across three grounded environments on LLM, each is a unique scheme of state transition. We utilise ScienceWorld ( Wang et al., 2022 ) to evaluate physical dynamics, where LLM must predict the textual consequences of scientific actions within a simulated world. We also employ Mind2Web ( Deng et al., 2023 ) , which challenges the model to forecast the updated HTML DOM tree following user interactions (e.g., clicks) on web elements. Finally, we assess functional tool dynamics via StableToolBench ( Guo et al., 2024 ) , where the objective is to simulate the execution output of API calls conditioned on the current conversational state and the invoked tool.

#### Baselines.

For visual world modelling, we compare SWIRL against a directly fine-tuned Liquid model ( SFT ). We reproduce two strong baselines from Qiu et al. (2025) : Test-time Verification , which selects the best sample from the fine-tuned Liquid based on IDM scores, and Bootstrap , which fine-tunes Liquid on silver data annotated by the IDM. We also include specialised diffusion-based image editing models, including GoT ( Fang et al., 2025 ) , SmartEdit ( Huang et al., 2024 ) , InstructPix2Pix ( Brooks et al., 2023 ) , and the Chameleon model family, following the protocol of Qiu et al. (2025) . To position our approach against recent (larger or diffusion-based) unified VLMs, we also evaluate BAGEL ( Deng et al., 2025 ) , OmniGen ( Xiao et al., 2025 ) , OmniGen2 ( Wu et al., 2025 ) , BLIP3o-NEXT ( Chen et al., 2025c ) , and UniWorld-V1 ( Lin et al., 2025 ) .

For text-based environments, prior work under this formulation is limited. We therefore primarily compare against SFT baselines and larger LLMs to ensure a fair comparison.

#### Evaluation Metrics.

For visual forward world modelling, we adopt GPT-4o-as-a-judge for holistic evaluation, following ( Qiu et al., 2025 ; Fang et al., 2025 ) with a 10-point scheme. We also report DiscEdit (DE) and CLIP scores for Aurora-Bench as in ( Krojer et al., 2024 ) . For text environments, we use BLEU, BERTScore, and ROUGE-L.

### 4.2 Single-turn Visual Dynamics Prediction

#### Aurora-Bench .

We present the quantitative evaluation of visual world modelling on Aurora-Bench in Table 1 . We compare SWIRL against state-of-the-art unified VLMs, specialised diffusion-based editing models, and ablations of our method. The primary comparison of interest is against Liquid-SFT, our direct supervised fine-tuning baseline. As highlighted in blue, SWIRL delivers consistent and significant improvements across all five benchmarks. Compared to the baselines from ( Qiu et al., 2025 ) , SWIRL surpasses the bootstrapping strategy using IDM to synthesise trajectories from unlabelled videos, and computation-heavy inference techniques like Test-time Verification (with up to N = 8 N=8 samples). Our best iterative strategy raises the average GPT-4o evaluation score from 4.36 (SFT) to 5.06, which also outperforms the non-iterative supervision from IDM only ( SWIRL (IDM → \rightarrow FWM) ) at 4.83, indicating the effectiveness of SWIRL by alternating policy and reward roles between FWM and IDM. Furthermore, despite starting from a weaker base model such as Liquid, and relying on a more lightweight post-training, 4 4 4 We use only around 400K samples from ( Qian et al., 2025 ; Krojer et al., 2024 ) to initialise the editing ability of Liquid. SWIRL remains highly competitive with other state-of-the-art unified VLMs such as OmniGen2 and BAGEL, while substantially outperforming diffusion-based editors like InstructPix2Pix. Qualitative examples for SWIRL are presented in Appendix J .

#### ByteMorph .

As the ByteMorph results in Table 2 show, all variants of SWIRL substantially raise the Average score over the Liquid-SFT baseline, e.g. SWIRL Iterative goes from 43.38 to 53.77 ( + 26.4 +26.4 %). Performance on global camera control ( Camera Zoom/Motion ) remains comparable. This is expected since the unlabelled in-the-wild videos used during the RL phase (e.g., VIDGEN-1M) are predominantly static and provide limited supervision for camera control. In contrast, SWIRL yields pronounced improvements on Object/Human Motion and Interaction , indicating effective learning of fine-grained dynamics. Notably, SWIRL matches the performance of larger or more heavily supervised VLMs (e.g., BAGEL and UniWorld-v1).

### 4.3 Multi-turn Visual Dynamics Prediction

#### WorldPredictionBench .

To assess long-horizon world modelling in addition to single-step prediction, we evaluate performance on WorldPredictionBench . The model must predict future observations autoregressively up to T = 6 T=6 time steps, using its own previous predictions as context. This setup tests the model’s ability to maintain physical consistency and resist the compounding covariate shift inherent in sequential generation. Table 3 summarises the GPT-4o-as-a-judge scores across all subsets in WorldPredictionBench .

The best variant of our models demonstrates a significant improvement in temporal consistency compared to Liquid-SFT. While SFT yields competitive performance at the immediate next step ( T = 1 T=1 ), it suffers from rapid degradation as the horizon increases, dropping from a score of 3.09 to 0.97 by T = 6 T=6 . In contrast, SWIRL ( Iterative ) maintains significantly higher fidelity throughout the rollout trajectory, achieving a +14.4% relative improvement over the baseline at T = 6 T=6 (1.11). We also remark that repeated self-improvement is not beneficial in this dataset, as performance peaks at the first iteration (IDM → \rightarrow FWM).

### 4.4 Textual Environments

Table 4 shows the quantitative evaluation on textual environments. When applied to Qwen-2.5-3B-Instruct in physical and digital simulation environments ( ScienceWorld and Mind2Web ), both SWIRL and SFT are near-saturation in semantic accuracy ( > > 92 BERTScore) and comparable in exact lexical matching (ROUGE-L). The advantage of our approach becomes most pronounced in StableToolBench , which requires the simulation of API execution outcomes. Here, we observe substantial improvements in generalisation capabilities, with our method surpassing SFT by +4.03 BLEU on ID-Low and +3.69 BLEU on ID-Medium splits. This establishes a new state-of-the-art for this model scale, outperforming also significantly larger open-weight instruction models (e.g., Qwen-2.5-32B, DeepSeek-7B). Overall, this suggests that the SWIRL can generalise to internalise complex API dynamics effectively for LLMs.

### 4.5 Analysis

#### Iterative RL.

We run an analysis to determine the potential for cumulative gain through iterative self-improvement beyond the first round. Figure 2 tracks the training dynamics across three iterations, where each iteration consists of updating the FWM using the current IDM as a reward (Phase I), followed by updating the IDM using the improved FWM as a reward (Phase II). We observe a clear virtuous cycle : enhancing the FWM’s forecasting capability enables it to provide a more robust verification for action prediction, which in turn yields a more precise reward signal for the subsequent FWM updates. The reward curves demonstrate that FWM and IDM in a separate-weight setup improve the training rewards effectively, and their optimisation converges with GRPO.

#### RL vs SFT.

To isolate the contribution of the optimisation objective, we compare SWIRL against direct SFT using the same set of unlabelled videos initially annotated by our IDM model. As shown in Figure 3 with details in F , SWIRL significantly outperforms the SFT baselines (both continued training and data merging), which stagnate or degrade as data scales. We attribute this disparity to the inherent ambiguity of visual dynamics and action verbalisation. SFT enforces a strict token-level imitation of the IDM’s specific pseudo-labels; however, a single visual transition often corresponds to multiple valid descriptions. Forcing the model to mimic one specific verbalisation can lead to overfitting noise and suppressing valid alternative predictions. In contrast, our GRPO framework effectively relaxes this constraint by encouraging consistency assessed by IDM, rather than exact replication. By exploring the FWM’s rollout space and action trajectories that the IDM model recognises as physically plausible, SWIRL learns a more robust and generalisable FWM that is not limited by the specific phrasing of the teacher annotations.

#### Sharing θ \theta and ϕ \phi .

We study the trade-off between parameter efficiency and training stability by comparing shared- and separate-weight designs (Figure 2 bottom and Table 1 ). Using separate weights yields stable optimisation, with the IDM score improving monotonically from 6.37 to 6.57 over three iterations (Figure 2 , Left). In contrast, shared weights ( θ = ϕ \theta=\phi ) reduce memory footprint but introduce instability, as reflected by a performance drop at Iteration 3 (to ∼ \sim 6.52).

This instability is also reflected in downstream performance: on Aurora-Bench , shared weights slightly underperform the separate variant (5.06 vs. 5; Table 1 ), and on long-horizon evaluation (Table 3 ), the shared model consistently lags behind (e.g., 1.74 vs. 1.68 overall). We attribute this gap to gradient interference between the heterogeneous objectives of FWM (visual generation) and IDM (inferring the linguistic action), suggesting that more robust unification mechanisms are needed to effectively share representations across modalities ( Shi et al., 2025 ; Ma et al., 2025 ; Qu et al., 2025 ; Zheng et al., 2025 ) .

## 5 Conclusion

We introduce SWIRL , a unified framework for enabling VLMs and LLMs to intrinsically model future states conditioned on the current state and latent actions, without relying on human-annotated trajectories. By interpreting actions as latent variables and alternately optimising forward world modelling and inverse dynamics modelling objectives with GRPO, our method induces self-improving world modelling purely from unlabelled data. We provide theoretical guarantees establishing the learnability of each optimisation phase, formally linking our objectives to variational mutual information bounds and evidence lower bounds. Empirically, we demonstrate the effectiveness of SWIRL across diverse settings, including real-world visual dynamics with VLMs and textual environments (physical and digital simulations and tool calling) with LLMs, validating its generality.

## Impact Statement

This paper presents SWIRL , a framework that enables LLMs and VLMs to self-improve their internal world models using unlabelled data. By reducing reliance on expensive human-annotated trajectories, our work advances the efficiency and accessibility of training capable reasoning agents. This has positive implications for the development of general-purpose assistants that can better understand physical dynamics and digital environments.

However, we acknowledge potential societal consequences associated with these capabilities. First, our method utilises self-improving loops on unlabelled “in-the-wild” data. Without human curation, there is a risk that the model may internalise, reinforce, or amplify biases and harmful patterns present in the raw distribution of web and video data. Future work employing this framework should incorporate safety filters or constitutional AI principles within the reward mechanism to mitigate this risk.

Second, the improvements in Visual Dynamics Prediction and Web HTML interaction imply a step forward in generative video capabilities and autonomous web agents. While these advancements aid in creative tools and automation, they also lower the barrier for generating deepfakes or creating agents capable of bypassing web-based security measures (e.g., CAPTCHAs) or conducting automated interactions at scale. We emphasise the necessity of developing robust detection tools for synthetic media and implementing strict access controls and guardrails for autonomous agents operating in real-world web environments.

## Acknowledgements

This work is supported by the ERC Starting Grant AToM-FM (101222956) awarded to Edoardo M. Ponti. The authors acknowledge the use of resources provided by the Isambard-AI National AI Research Resource (AIRR). Isambard-AI is operated by the University of Bristol and is funded by the UK Government’s Department for Science, Innovation and Technology (DSIT) via UK Research and Innovation; and the Science and Technology Facilities Council [ST/AIRR/I-A-I/1023] ( McIntosh-Smith et al., 2024 ) .

## References

Barber and Agakov (2003) D. Barber and F. Agakov The im algorithm: a variational approach to information maximization . In Proceedings of the 17th International Conference on Neural Information Processing Systems , NIPS’03 , Cambridge, MA, USA , pp. 201–208 . Cited by: §1 , §3.2 , §3.3 .

Bensal et al. (2025) S. Bensal, U. Jamil, C. Bryant, M. Russak, K. Kamble, D. Mozolevskyi, M. Ali, and W. AlShikh Reflect, retry, reward: self-improving llms via reinforcement learning . arXiv preprint arXiv:2505.24726 . Cited by: §2 .

Brooks et al. (2023) T. Brooks, A. Holynski, and A. A. Efros InstructPix2Pix: learning to follow image editing instructions . In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition , pp. 18392–18402 . Cited by: §4.1 .

Chang et al. (2025) D. Chang, M. Cao, Y. Shi, B. Liu, S. Cai, S. Zhou, W. Huang, G. Wetzstein, M. Soleymani, and P. Wang ByteMorph: benchmarking instruction-guided image editing with non-rigid motions . arXiv preprint arXiv:2506.03107 . Cited by: §B.2 .

Chen et al. (2025a) D. Chen, W. Chung, Y. Bang, Z. Ji, and P. Fung WorldPrediction: a benchmark for high-level world modeling and long-horizon procedural planning . arXiv preprint arXiv:2506.04363 . Cited by: §B.2 , §1 , §2 .

Chen et al. (2025b) D. Chen, T. Moutakanni, W. Chung, Y. Bang, Z. Ji, A. Bolourchi, and P. Fung Planning with reasoning using vision language world model . arXiv preprint arXiv:2509.02722 . Cited by: §1 , §2 .

Chen et al. (2025c) J. Chen, L. Xue, Z. Xu, X. Pan, S. Yang, C. Qin, A. Yan, H. Zhou, Z. Chen, L. Huang, et al. Blip3o-next: next frontier of native image generation . arXiv preprint arXiv:2510.15857 . Cited by: §4.1 .

Chen et al. (2025d) X. Chen, Z. Zhang, H. Zhang, Y. Zhou, S. Y. Kim, Q. Liu, Y. Li, J. Zhang, N. Zhao, Y. Wang, et al. Unireal: universal image generation and editing via learning real-world dynamics . In Proceedings of the Computer Vision and Pattern Recognition Conference , pp. 12501–12511 . Cited by: §4.1 .

Copet et al. (2025) J. Copet, Q. Carbonneaux, G. Cohen, J. Gehring, J. Kahn, J. Kossen, F. Kreuk, E. McMilin, M. Meyer, Y. Wei, et al. Cwm: an open-weights llm for research on code generation with world models . arXiv preprint arXiv:2510.02387 . Cited by: §1 , §2 .

Cui et al. (2025) Y. Cui, H. Chen, H. Deng, X. Huang, X. Li, J. Liu, Y. Liu, Z. Luo, J. Wang, W. Wang, et al. Emu3. 5: native multimodal models are world learners . arXiv preprint arXiv:2510.26583 . Cited by: §2 .

Deng et al. (2025) C. Deng, D. Zhu, K. Li, C. Gou, F. Li, Z. Wang, S. Zhong, W. Yu, X. Nie, Z. Song, et al. Emerging properties in unified multimodal pretraining . arXiv preprint arXiv:2505.14683 . Cited by: §B.2 , §2 , §2 , §4.1 .

Deng et al. (2023) X. Deng, Y. Gu, B. Zheng, S. Chen, S. Stevens, B. Wang, H. Sun, and Y. Su Mind2web: towards a generalist agent for the web . Advances in Neural Information Processing Systems 36 , pp. 28091–28114 . Cited by: §4.1 .

Fang et al. (2025) R. Fang, C. Duan, K. Wang, L. Huang, H. Li, S. Yan, H. Tian, X. Zeng, R. Zhao, J. Dai, et al. GoT: unleashing reasoning capability of multimodal large language model for visual generation and editing . arXiv preprint arXiv:2503.10639 . Cited by: §4.1 , §4.1 .

Gao et al. (2025) Q. Gao, X. Pi, K. Liu, J. Chen, R. Yang, X. Huang, X. Fang, L. Sun, G. Kishore, B. Ai, et al. Do vision-language models have internal world models? towards an atomic evaluation . arXiv preprint arXiv:2506.21876 . Cited by: §2 .

Guo et al. (2025a) D. Guo, D. Yang, H. Zhang, J. Song, R. Zhang, R. Xu, Q. Zhu, S. Ma, P. Wang, X. Bi, et al. Deepseek-r1: incentivizing reasoning capability in llms via reinforcement learning . arXiv preprint arXiv:2501.12948 . Cited by: §1 , §3.2 .

Guo et al. (2025b) S. Guo, O. D. Domingues, R. Avalos, A. Courville, and F. Strub Sample, predict, then proceed: self-verification sampling for tool use of llms . arXiv preprint arXiv:2506.02918 . Cited by: §1 , §2 .

Guo et al. (2024) Z. Guo, S. Cheng, H. Wang, S. Liang, Y. Qin, P. Li, Z. Liu, M. Sun, and Y. Liu Stabletoolbench: towards stable large-scale benchmarking on tool learning of large language models . arXiv preprint arXiv:2403.07714 . Cited by: §4.1 , Table 4 , Table 4 .

He et al. (2025) J. He, H. Lin, Q. Wang, Y. R. Fung, and H. Ji Self-correction is more than refinement: a learning framework for visual and language reasoning tasks . In Findings of the Association for Computational Linguistics: ACL 2025 , pp. 6405–6421 . Cited by: §2 .

Huang et al. (2023) J. Huang, S. Gu, L. Hou, Y. Wu, X. Wang, H. Yu, and J. Han Large language models can self-improve . In Proceedings of the 2023 conference on empirical methods in natural language processing , pp. 1051–1068 . Cited by: §2 .

Huang et al. (2024) Y. Huang, L. Xie, X. Wang, Z. Yuan, X. Cun, Y. Ge, J. Zhou, C. Dong, R. Huang, R. Zhang, et al. SmartEdit: exploring complex instruction-based image editing with multimodal large language models . In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition , pp. 8362–8371 . Cited by: §4.1 .

Jin et al. (2025) W. Jin, Y. Niu, J. Liao, C. Duan, A. Li, S. Gao, and X. Liu Srum: fine-grained self-rewarding for unified multimodal models . arXiv preprint arXiv:2510.12784 . Cited by: §1 , §2 .

Kay et al. (2017) W. Kay, J. Carreira, K. Simonyan, B. Zhang, C. Hillier, S. Vijayanarasimhan, F. Viola, T. Green, T. Back, P. Natsev, et al. The kinetics human action video dataset . arXiv preprint arXiv:1705.06950 . Cited by: §4.1 .

Krojer et al. (2024) B. Krojer, D. Vattikonda, L. Lara, V. Jampani, E. Portelance, C. Pal, and S. Reddy Learning Action and Reasoning-Centric Image Editing from Videos and Simulations . In NeurIPS , Note: Spotlight Paper External Links: Link Cited by: Appendix C , §4.1 , §4.1 , footnote 4 .

[24] N. Lee, Z. Cai, A. Schwarzschild, K. Lee, and D. Papailiopoulos Self-improving transformers overcome easy-to-hard and length generalization challenges . In Forty-second International Conference on Machine Learning , Cited by: §2 .

Lehrach et al. (2025) W. Lehrach, D. Hennes, M. Lazaro-Gredilla, X. Lou, C. Wendelken, Z. Li, A. Dedieu, J. Grau-Moya, M. Lanctot, A. Iscen, et al. Code world models for general game playing . arXiv preprint arXiv:2510.04542 . Cited by: §2 .

Li et al. (2025) Y. Li, H. Wang, J. Qiu, Z. Yin, D. Zhang, C. Qian, Z. Li, P. Ma, G. Chen, H. Ji, et al. From word to world: can large language models be implicit text-based world models? . arXiv preprint arXiv:2512.18832 . Cited by: §2 .

Lin et al. (2025) B. Lin, Z. Li, X. Cheng, Y. Niu, Y. Ye, X. He, S. Yuan, W. Yu, S. Wang, Y. Ge, et al. Uniworld: high-resolution semantic encoders for unified visual understanding and generation . arXiv preprint arXiv:2506.03147 . Cited by: §2 , §4.1 .

Liu et al. (2025a) E. Liu, V. Gangal, C. Zou, X. Huang, M. Yu, A. Chang, Z. Tao, S. Kumar, and S. Y. Feng A unified definition of hallucination, or: it’s the world model, stupid . arXiv preprint arXiv:2512.21577 . Cited by: §1 .

Liu et al. (2025b) Z. Liu, Z. Huan, X. Wang, J. Lyu, J. Tao, X. Li, F. Huang, and H. Xu World models with hints of large language models for goal achieving . In Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers) , pp. 50–72 . Cited by: §1 .

Ma et al. (2025) C. Ma, Y. Jiang, J. Wu, J. Yang, X. Yu, Z. Yuan, B. Peng, and X. Qi Unitok: a unified tokenizer for visual generation and understanding . arXiv preprint arXiv:2502.20321 . Cited by: §2 , §4.5 .

Mao et al. (2025) W. Mao, Z. Yang, and M. Z. Shou UniRL: self-improving unified multimodal models via supervised and reinforcement learning . arXiv preprint arXiv:2505.23380 . Cited by: §1 , §2 .

McIntosh-Smith et al. (2024) S. McIntosh-Smith, S. R. Alam, and C. Woods Isambard-ai: a leadership class supercomputer optimised specifically for artificial intelligence . External Links: 2410.11199 , Link Cited by: Acknowledgements .

Monfort et al. (2019) M. Monfort, A. Andonian, B. Zhou, K. Ramakrishnan, S. A. Bargal, T. Yan, L. Brown, Q. Fan, D. Gutfruend, C. Vondrick, et al. Moments in time dataset: one million videos for event understanding . IEEE Transactions on Pattern Analysis and Machine Intelligence , pp. 1–8 . External Links: ISSN 0162-8828 , Document Cited by: §4.1 .

Qian et al. (2025) Y. Qian, E. Bocek-Rivele, L. Song, J. Tong, Y. Yang, J. Lu, W. Hu, and Z. Gan Pico-banana-400k: a large-scale dataset for text-guided image editing . arXiv preprint arXiv:2510.19808 . Cited by: §B.1 , Appendix C , §4.1 , footnote 4 .

Qiu et al. (2026) X. Qiu, H. Jia, Z. Zeng, S. Shen, C. Meng, Y. Yang, and L. Zhu Unified generation and self-verification for vision-language models via advantage decoupled preference optimization . arXiv preprint arXiv:2601.01483 . Cited by: §2 .

Qiu et al. (2024) Y. Qiu, Z. Zhao, Y. Ziser, A. Korhonen, E. Ponti, and S. B. Cohen Are large language model temporally grounded? . In Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers) , pp. 7057–7076 . Cited by: §1 , §2 .

Qiu et al. (2025) Y. Qiu, Y. Ziser, A. Korhonen, S. B. Cohen, and E. M. Ponti Bootstrapping world models from dynamics models in multimodal foundation models . arXiv preprint arXiv:2506.06006 . Cited by: §1 , §1 , §2 , §3.1 , §4.1 , §4.1 , §4.1 , §4.2 .

Qu et al. (2025) L. Qu, H. Zhang, Y. Liu, X. Wang, Y. Jiang, Y. Gao, H. Ye, D. K. Du, Z. Yuan, and X. Wu Tokenflow: unified image tokenizer for multimodal understanding and generation . In Proceedings of the Computer Vision and Pattern Recognition Conference , pp. 2545–2555 . Cited by: §2 , §4.5 .

Qwen Team (2024) Qwen Team Qwen2 technical report . arXiv preprint arXiv:2407.10671 . Cited by: §4.1 .

Shi et al. (2025) Y. Shi, Y. Dong, Y. Ding, Y. Wang, X. Zhu, S. Zhou, W. Liu, H. Tian, R. Wang, H. Wang, et al. Realunify: do unified models truly benefit from unification? a comprehensive benchmark . arXiv preprint arXiv:2509.24897 . Cited by: §2 , §4.5 .

Soomro et al. (2012) K. Soomro, A. R. Zamir, and M. Shah UCF101: a dataset of 101 human actions classes from videos in the wild . arXiv preprint arXiv:1212.0402 . Cited by: §4.1 .

Tan et al. (2024) Z. Tan, X. Yang, L. Qin, and H. Li Vidgen-1m: a large-scale dataset for text-to-video generation . arXiv preprint arXiv:2408.02629 . Cited by: §4.1 .

Tehenan et al. (2025) M. Tehenan, C. B. Moya, T. Long, and G. Lin Linear spatial world models emerge in large language models . arXiv preprint arXiv:2506.02996 . Cited by: §1 , §2 .

Vafa et al. (2024) K. Vafa, J. Y. Chen, A. Rambachan, J. Kleinberg, and S. Mullainathan Evaluating the world model implicit in a generative model . Advances in Neural Information Processing Systems 37 , pp. 26941–26975 . Cited by: §1 , §2 .

Wang et al. (2025a) J. Wang, Q. Yan, Y. Wang, Y. Tian, S. S. Mishra, Z. Xu, M. Gandhi, P. Xu, and L. L. Cheong Reinforcement learning for self-improving agent with skill library . arXiv preprint arXiv:2512.17102 . Cited by: §1 , §2 .

[46] K. Wang, P. Zhang, Z. Wang, Y. Gao, L. Li, Q. Wang, H. Chen, Y. Lu, Z. Yang, L. Wang, et al. VAGEN: reinforcing world model reasoning for multi-turn vlm agents . In The Thirty-ninth Annual Conference on Neural Information Processing Systems , Cited by: §1 .

Wang et al. (2025b) Q. Wang, W. Huang, Y. Zhou, H. Yin, T. Bao, J. Lyu, W. Liu, R. Zhang, J. Wu, L. Fei-Fei, et al. ENACT: evaluating embodied cognition with world modeling of egocentric interaction . arXiv preprint arXiv:2511.20937 . Cited by: §1 , §2 , §3.1 .

Wang et al. (2022) R. Wang, P. Jansen, M. Côté, and P. Ammanabrolu Scienceworld: is your agent smarter than a 5th grader? . arXiv preprint arXiv:2203.07540 . Cited by: §4.1 .

Wang et al. (2025c) Y. Wang, L. Yang, Y. Tian, K. Shen, and M. Wang CURE: co-evolving coders and unit testers via reinforcement learning . In The Thirty-ninth Annual Conference on Neural Information Processing Systems , Cited by: §1 , §2 .

Wu et al. (2025) C. Wu, P. Zheng, R. Yan, S. Xiao, X. Luo, Y. Wang, W. Li, X. Jiang, Y. Liu, J. Zhou, Z. Liu, Z. Xia, C. Li, H. Deng, J. Wang, K. Luo, B. Zhang, D. Lian, X. Wang, Z. Wang, T. Huang, and Z. Liu OmniGen2: exploration to advanced multimodal generation . arXiv preprint arXiv:2506.18871 . Cited by: §4.1 .

Wu et al. (2024) J. Wu, Y. Jiang, C. Ma, Y. Liu, H. Zhao, Z. Yuan, S. Bai, and X. Bai Liquid: language models are scalable and unified multi-modal generators . arXiv preprint arXiv:2412.04332 . Cited by: §B.1 , §2 , §4.1 .

Xiang et al. (2024) J. Xiang, G. Liu, Y. Gu, Q. Gao, Y. Ning, Y. Zha, Z. Feng, T. Tao, S. Hao, Y. Shi, et al. Pandora: towards general world model with natural language actions and video states . arXiv preprint arXiv:2406.09455 . Cited by: §2 .

Xiao et al. (2025) S. Xiao, Y. Wang, J. Zhou, H. Yuan, X. Xing, R. Yan, C. Li, S. Wang, T. Huang, and Z. Liu Omnigen: unified image generation . In Proceedings of the Computer Vision and Pattern Recognition Conference , pp. 13294–13304 . Cited by: §2 , §4.1 .

Xie et al. (2025) K. Xie, I. Yang, J. Gunerli, and M. Riedl Making large language models into world models with precondition and effect knowledge . In Proceedings of the 31st International Conference on Computational Linguistics , pp. 7532–7545 . Cited by: §2 .

Xiong et al. (2026) Z. Xiong, X. Ye, B. Yaman, S. Cheng, Y. Lu, J. Luo, N. Jacobs, and L. Ren UniDrive-wm: unified understanding, planning and generation world model for autonomous driving . arXiv preprint arXiv:2601.04453 . Cited by: §1 , §2 .

Zhang et al. (2025) J. Zhang, T. Li, L. Li, Z. Yang, and Y. Cheng Are unified vision-language models necessary: generalization across understanding and generation . arXiv preprint arXiv:2505.23043 . Cited by: §2 .

Zhao et al. (2024) C. Zhao, X. Jia, V. Viswanathan, T. Wu, and G. Neubig Self-guide: better task-specific instruction following via self-synthetic finetuning . arXiv preprint arXiv:2407.12874 . Cited by: §2 .

Zheng et al. (2025) D. Zheng, M. Zhang, H. Li, K. Zou, H. Liu, Z. Guo, K. Feng, Y. Liu, Y. Luo, Y. Feng, et al. Architecture decoupling is not all you need for unified multimodal model . arXiv preprint arXiv:2511.22663 . Cited by: §2 , §4.5 .

## Appendix A Theoretical Derivation

In this section, we provide the detailed theoretical justification for SWIRL . We formalise the interaction between the Forward World Modelling (FWM) and Inverse Dynamics Model (IDM) as an alternating maximisation of Identifiability (via Variational Mutual Information) and Data Fidelity (via the Evidence Lower Bound).

We define the following notation: • x ∈ 𝒮 x\in\mathcal{S} : The source observation (current state s t s_{t} ).

• y ∈ 𝒮 y\in\mathcal{S} : The ground-truth target observation (next state s t + 1 s_{t+1} ), distributed according to the data distribution 𝒟 ⁡ ( y | x ) \mathcal{D}(y|x) .

• y ^ ∈ 𝒮 \hat{y}\in\mathcal{S} : A generated target observation sampled from the forward model.

• z ∈ 𝒜 z\in\mathcal{A} : The latent action driving the transition.

We employ two parametrised models: 1. Forward World Modelling (FWM): P θ ​ ( y ^ | x , z ) P_{\theta}(\hat{y}|x,z) , parametrised by θ \theta . FWM parametrised the environment’s transition distribution.

2. Inverse Dynamics Model (IDM): Q ϕ ​ ( z | x , y ) Q_{\phi}(z|x,y) , parametrised by ϕ \phi . IDM parametrised an approximate posterior over latent actions given a state transition.

### A.1 Phase I: Learnability of the Forward Model (FWM)

In the first phase, we freeze the IDM parameters ϕ \phi and optimise the FWM parameters θ \theta . Our objective is to generate trajectories y ^ \hat{y} that are identifiable by the inference model. We formalise this as maximising the Conditional Mutual Information (CMI) between the latent action Z Z and the generated observation Y ^ \hat{Y} , conditioned on the source state X X .

Crucially, in our algorithm, the latent actions Z Z used for training are not sampled from a fixed uninformative prior, but are inferred from the ground-truth data using the current IDM. We denote this Empirical Belief Distribution as P ~ ​ ( z | x ) \tilde{P}(z|x) : P ~ ​ ( z | x ) ≜ 𝔼 y ∼ 𝒟 ⁡ ( y | x ) ​ [ Q ϕ ​ ( z | x , y ) ] \tilde{P}(z|x)\triangleq\mathbb{E}_{y\sim\mathcal{D}(y|x)}\left[Q_{\phi}(z|x,y)\right] (6)

###### Theorem A.1 .

Optimising the FWM to maximise the likelihood assigned by the frozen IDM to generated samples maximises a Variational Lower Bound of the Conditional Mutual Information I P ~ ​ ( Z ; Y ^ | X ) I_{\tilde{P}}(Z;\hat{Y}|X) defined over the empirical belief distribution.

###### Proof.

The Conditional Mutual Information under the joint distribution induced by the data and the frozen IDM is: I P ~ ​ ( Z ; Y ^ | X ) = H P ~ ​ ( Z | X ) − H ⁡ ( Z | Y ^ , X ) I_{\tilde{P}}(Z;\hat{Y}|X)=H_{\tilde{P}}(Z|X)-H(Z|\hat{Y},X) (7)

The term H P ~ ​ ( Z | X ) H_{\tilde{P}}(Z|X) is the entropy of the marginal distribution of actions inferred from the dataset. Since ϕ \phi is frozen in this phase and the dataset 𝒟 \mathcal{D} is fixed, P ~ ​ ( z | x ) \tilde{P}(z|x) is constant with respect to θ \theta . Therefore, maximising the mutual information is equivalent to minimizing the conditional entropy H ⁡ ( Z | Y ^ , X ) H(Z|\hat{Y},X) .

The conditional entropy is defined as: H ⁡ ( Z | Y ^ , X ) \displaystyle H(Z|\hat{Y},X) = − 𝔼 x ∼ 𝒟 𝔼 z ∼ P ~ ​ ( z | x ) 𝔼 y ^ ∼ P θ ( ⋅ | x , z ) [ log P ( z | y ^ , x ) ] \displaystyle=-\mathbb{E}_{x\sim\mathcal{D}}\mathbb{E}_{z\sim\tilde{P}(z|x)}\mathbb{E}_{\hat{y}\sim P_{\theta}(\cdot|x,z)}\left[\log P(z|\hat{y},x)\right] (8)

The true posterior P ⁡ ( z | y ^ , x ) P(z|\hat{y},x) is intractable as it requires marginalising over the action space. We utilise the frozen IDM Q ϕ ​ ( z | x , y ^ ) Q_{\phi}(z|x,\hat{y}) as a variational approximation. By the non-negativity of the KL divergence D KL ( P ( z | y ^ , x ) | | Q ϕ ( z | x , y ^ ) ) ≥ 0 D_{\mathrm{KL}}(P(z|\hat{y},x)||Q_{\phi}(z|x,\hat{y}))\geq 0 , we have the lower bound: 𝔼 y ^ ​ [ log ⁡ P ⁡ ( z | y ^ , x ) ] ≥ 𝔼 y ^ ​ [ log ⁡ Q ϕ ​ ( z | x , y ^ ) ] \mathbb{E}_{\hat{y}}[\log P(z|\hat{y},x)]\geq\mathbb{E}_{\hat{y}}[\log Q_{\phi}(z|x,\hat{y})] (9)

Substituting this into the entropy term yields the variational lower bound for the CMI: I P ~ ​ ( Z ; Y ^ | X ) \displaystyle I_{\tilde{P}}(Z;\hat{Y}|X) ≥ H P ~ ( Z | X ) + 𝔼 x ∼ 𝒟 𝔼 z ∼ P ~ ​ ( z | x ) 𝔼 y ^ ∼ P θ ( ⋅ | x , z ) [ log Q ϕ ( z | x , y ^ ) ] \displaystyle\geq H_{\tilde{P}}(Z|X)+\mathbb{E}_{x\sim\mathcal{D}}\mathbb{E}_{z\sim\tilde{P}(z|x)}\mathbb{E}_{\hat{y}\sim P_{\theta}(\cdot|x,z)}\left[\log Q_{\phi}(z|x,\hat{y})\right] (10)

Expanding the definition of P ~ ​ ( z | x ) \tilde{P}(z|x) from Eq. (1), the optimization objective becomes: 𝒥 FWM ( θ ) = 𝔼 x ∼ 𝒟 𝔼 y ∼ 𝒟 ⁡ ( y | x ) [ 𝔼 z ∼ Q ϕ ( ⋅ | x , y ) [ 𝔼 y ^ ∼ P θ ( ⋅ | x , z ) [ log Q ϕ ( z | x , y ^ ) ] ] ] \mathcal{J}_{\text{FWM}}(\theta)=\mathbb{E}_{x\sim\mathcal{D}}\mathbb{E}_{y\sim\mathcal{D}(y|x)}\left[\mathbb{E}_{z\sim Q_{\phi}(\cdot|x,y)}\left[\mathbb{E}_{\hat{y}\sim P_{\theta}(\cdot|x,z)}\left[\log Q_{\phi}(z|x,\hat{y})\right]\right]\right] (11)

∎

### A.2 Phase II: Learnability of the Inverse Model (IDM)

In the second phase, we freeze θ \theta and optimise the IDM parameters ϕ \phi . We seek to maximise the log-likelihood of the observed ground-truth dynamics log ⁡ P θ ​ ( y | x ) \log P_{\theta}(y|x) (Data Fidelity). We model this via the Evidence Lower Bound (ELBO), treating the initialised policy at the start of the iteration as the reference prior, denoted π ref ​ ( z | x ) \pi_{\mathrm{ref}}(z|x) .

###### Theorem A.2 .

Optimising the IDM via the KL-regularised policy gradient objective with reward R ⁡ ( x , z , y ) = log ⁡ P θ ​ ( y | x , z ) R(x,z,y)=\log P_{\theta}(y|x,z) , β = 1 \beta=1 , and reference policy π ref \pi_{\mathrm{ref}} maximises the Evidence Lower Bound (ELBO).

###### Proof.

We express the marginal log-likelihood of the data by introducing the variational distribution Q ϕ ​ ( z | x , y ) Q_{\phi}(z|x,y) : log ⁡ P θ ​ ( y | x ) \displaystyle\log P_{\theta}(y|x) = log ∑ z ∈ 𝒜 P θ ( y | x , z ) π ref ( z | x ) \displaystyle=\log\sum_{z\in\mathcal{A}}P_{\theta}(y|x,z)\pi_{\mathrm{ref}}(z|x) = log 𝔼 z ∼ Q ϕ ( ⋅ | x , y ) [ P θ ​ ( y | x , z ) ​ π ref ​ ( z | x ) Q ϕ ​ ( z | x , y ) ] \displaystyle=\log\mathbb{E}_{z\sim Q_{\phi}(\cdot|x,y)}\left[\frac{P_{\theta}(y|x,z)\pi_{\mathrm{ref}}(z|x)}{Q_{\phi}(z|x,y)}\right] (12)

Applying Jensen’s inequality (concavity of log): log ⁡ P θ ​ ( y | x ) \displaystyle\log P_{\theta}(y|x) ≥ 𝔼 z ∼ Q ϕ ​ [ log ⁡ P θ ​ ( y | x , z ) + log ⁡ π ref ​ ( z | x ) − log ⁡ Q ϕ ​ ( z | x , y ) ] \displaystyle\geq\mathbb{E}_{z\sim Q_{\phi}}\left[\log P_{\theta}(y|x,z)+\log\pi_{\mathrm{ref}}(z|x)-\log Q_{\phi}(z|x,y)\right] = 𝔼 z ∼ Q ϕ [ log P θ ( y | x , z ) ] − D KL ( Q ϕ ( z | x , y ) | | π ref ( z | x ) ) \displaystyle=\mathbb{E}_{z\sim Q_{\phi}}\left[\log P_{\theta}(y|x,z)\right]-D_{\mathrm{KL}}(Q_{\phi}(z|x,y)\,||\,\pi_{\mathrm{ref}}(z|x)) (13)

This is the standard Evidence Lower Bound. The KL-regularised policy gradient objective (Phase II) is defined as: 𝒥 ( ϕ ) = 𝔼 z ∼ Q ϕ ( ⋅ | x , y ) [ R ( x , z , y ) ] − β D KL ( Q ϕ ( ⋅ | x , y ) | | π ref ( ⋅ | x ) ) \mathcal{J}(\phi)=\mathbb{E}_{z\sim Q_{\phi}(\cdot|x,y)}\left[R(x,z,y)\right]-\beta\,D_{\mathrm{KL}}(Q_{\phi}(\cdot|x,y)\,||\,\pi_{\mathrm{ref}}(\cdot|x)) (14)

By setting the reward to the FWM log-likelihood, R = log ⁡ P θ ​ ( y | x , z ) R=\log P_{\theta}(y|x,z) , we observe that: 𝒥 ​ ( ϕ ) ≡ ELBO ​ ( ϕ ) \mathcal{J}(\phi)\equiv\text{ELBO}(\phi) (15)

Thus, the IDM update step performs coordinate ascent on the evidence lower bound of the data likelihood, ensuring the inferred actions explain the ground-truth transitions under the current forward dynamics. ∎

## Appendix B Implementation Details

### B.1 Hyperparameters

For the Liquid-SFT model, we fine-tune Liquid-7B ( Wu et al., 2024 ) on Pico-banana-400K ( Qian et al., 2025 ) and Aurora ’s training set. Training is performed for 5 epochs with a batch size of 128. We use a learning rate of 2 × 10 − 5 2\times 10^{-5} with a cosine learning rate schedule, allocating 5% of the total training steps for warm-up.

For the non-iterative setup ( SWIRL (IDM → \rightarrow FWM) ), the model is trained with a batch size of 64 and a learning rate of 1 × 10 − 6 1\times 10^{-6} . A cosine learning rate schedule with 100 warm-up steps is applied. GRPO is used with a rollout size of 8 and a KL regularization coefficient β = 0.1 \beta=0.1 .

For the iterative setup ( SWIRL (Iterative) ), we use a batch size of 128 and a learning rate of 2 × 10 − 7 2\times 10^{-7} , together with a cosine schedule and 50 warm-up steps. In the SWIRL (Iterative + Share) variant, the learning rate is increased to 5 × 10 − 7 5\times 10^{-7} while all other settings remain unchanged. In both iterative GRPO setups, we set the decoding temperature to 0.75 and Top- P P to 0.96 to control the quality of predicted futures. Additionally, we apply a logit processor to constrain Liquid’s generation to image tokens for FWM and textual tokens for IDM.

For LLM experiments on StableToolBench , we fine-tune models using GRPO with DeepSpeed for memory-efficient distributed training. Optimization is performed with a learning rate of 5 × 10 − 5 5\times 10^{-5} under a cosine learning rate schedule with 25 warm-up steps, using an effective batch size of 128. For each prompt, we sample 64 rollouts. The maximum prompt and completion lengths are set to 8,126 and 4,096 tokens, respectively. Unless otherwise specified, we use a KL regularization coefficient of β = 0.1 \beta=0.1 . During GRPO rollout, we set the decoding temperature to 0.7 and Top- P P to 0.96. For Mind2Web and ScienceWorld , we adopt the same configuration, except that the maximum prompt and completion lengths are both set to 4,096 tokens, and the number of GRPO rollouts is reduced to 16.

For VLM experiments, training is conducted using DeepSpeed on 32 NVIDIA H200 140GB GPUs for FWM and 8 NVIDIA H200 140GB GPUs for IDM. For LLM experiments, both FWM and IDM are trained on 8 NVIDIA Grace-Hopper (GH100) GPUs.

### B.2 Evaluation Prompt for GPT-4o as a Judge

For Aurora-Bench , we use the same prompt as in Deng et al. (2025) . For ByteMorph , we employ the official GPT-4o judge template provided by Chang et al. (2025) . Since WorldPredictionBench ( Chen et al., 2025a ) does not natively support multi-turn image editing evaluation, we adopt the prompt template shown in Figure 4 . This template is designed to balance the penalties for directly copying the source image and for excessive editing.

## Appendix C Sanity Check Results for General Image Editing.

Table 5 reports a sanity-check evaluation of general image editing performance on GEdit-Bench . Although Liquid does not have native image editing support by design, we find that after our supervised fine-tuning (SFT) pipeline, using a mixture of Aurora ( Krojer et al., 2024 ) and Pico-banana-400K ( Qian et al., 2025 ) , the resulting model (Liquid-SFT) acquires functional image editing behaviour. We illustrate the qualitative examples for general image editing in Figure 5 .

Concretely, Liquid without SFT indicates a totally failure in GEdit-Bench , indicating the necessarily in the warm-up stage before SWIRL . Liquid-SFT achieves non-trivial scores in both semantic alignment and perceptual quality, confirming that the model can follow image editing instructions and produce coherent visual outputs. While Liquid-SFT remains significantly behind state-of-the-art proprietary and public image editing models, this result is not intended to be competitive; rather, it serves as a capability verification that our SFT pipeline successfully activates basic visual editing skills in a base model not originally designed for this task.

We emphasise that this capability plays an important role as a warm-up stage for subsequent world modelling objectives. In later stages, the model is trained to (i) predict the next visual observation given the current state (forward world modelling), and (ii) perform inverse dynamics modelling (IDM), where the model receives a pair of observations and predicts the intervening action in language. The ability to perform instruction-followed image transformations provides a minimal but necessary foundation for these more structured visual–temporal reasoning tasks.

Finally, the ablation study highlights the importance of Pico-banana-400K in our data mixture. Removing this component leads to a consistent degradation across all metrics (average score dropping from 3.06 to 2.43), indicating that Pico-banana provides critical signal for stabilising and enriching visual instruction-following behaviour. This result suggests that even for non-native capabilities, carefully curated visual editing data is essential for preserving functional performance after SFT.

We include the qualitative examples produced by our approach for general image editing in Figure 5 .

## Appendix D IDM Analysis

#### Aurora-Bench Evaluation.

To validate the reliability of our reward mechanism, we evaluate the Inverse Dynamics Model (IDM) performance directly on Aurora-Bench (Table 6 ). A fundamental premise of our framework is that inferring the action responsible for a state transition (IDM) is a more tractable task than generating high-dimensional future states (FWM). The results support this hypothesis: the IDM model achieves high action prediction accuracy (6.38 out of 10 as GPT score), serving as a strong discriminator. Additionally, we observe that the iterative paradigm can also leverage the reward signal from FWM, effectively improving GPT4o scores from 6.38 to 6.58 as our best approach. This stability is vital for our self-improving, ensuring that the reward signal remains informative and accurately penalises physical inconsistencies.

#### Interpretability of Latent Actions and Reward Hacking.

A potential concern in learning with the latent actions is reward hacking, where actions might degenerate into short, distinctive ciphers (e.g., single keywords or artifacts) to be hacked for an easier optimisable FWM. We analyse the evolution of complexities of the generated actions across three iterations for SWIRL in Figure 6 .

Contrary to the hypothesis of reward collapse, we observe that the uniqueness of generated actions remains consistently high ( > 94 % >94\% ) across all iterations for both shared and separate weight configurations. The similar observation happens for naturalness that the predicted actions are quite stably natural (as evidenced by the predicted perplexity of an LLM, GPT-2) throughout SWIRL ’s training iterations, without collapsing into any unnatural artifacts that could be easily hacked by FWM or IDM. Looking into the lengths of predicted actions, the model does not "shortcut" by generating brief tokens as well; instead, the average action length (around 16.8 16.8 tokens) consistently exceeds the ground truth average (around 7.2 7.2 tokens). This indicates that the IDM learns to provide more descriptive and detailed instructions to ensure the transition is consistently identifiable, rather than drifting into a simplified cipher. Qualitative inspection confirms that predictions remain physically meaningful and there is no model collapse happening on SWIRL (e.g., "tearing paper into two pieces", "Swap the positions of the two objects.", "turning a bottle upside down" ), preserving natural language interpretability.

## Appendix E Inference-time Verification

As a sanity check for SWIRL , we investigate the validity of the coverage hypothesis intrinsic to our GRPO formulation. For the IDM reward to effectively guide learning, the set of sampled rollouts must contain at least one candidate that sufficiently approximates the ground-truth future state. We evaluate the "Best-of- N N " performance of Liquid-SFT, where the candidate with the highest GPT4o score is selected, by scaling the number of rollouts N N . In Table 1 , we observe a monotonic improvement for inference-time verification as N N increases, confirming that the base policy possesses the latent capability to generate high-fidelity transitions in multiple rollouts. This finding empirically validates our training premise: expanding the rollout space should increases the likelihood of capturing valid transitions, thereby providing the IDM discriminator with the necessary high-quality positive examples to reinforce.

## Appendix F Detailed Results for Comparing SFT and SWIRL .

Table 7 presents a detailed comparison between SWIRL and two supervised fine-tuning baselines under controlled data budgets. Across all five benchmarks and all training sample counts, RL consistently exhibits superior data efficiency compared to both SFT-Continue and SFT-Merge . While SFT baselines often plateau or even degrade as more samples are introduced, RL shows a clear trend of performance improvement as additional data becomes available.

Notably, RL begins to outperform SFT at relatively small data scales (6.4K samples) and the performance gap widens as training proceeds. On Action Genome, Something, and Whatsup, Kubric, which emphasises structured physical dynamics, RL achieves the strongest or near-strongest performance at every scale, indicating that reward-guided optimisation better captures latent world structure than direct imitation.

Aggregated across all benchmarks, RL achieves the highest average score at every data scale, with gains becoming increasingly pronounced at larger budgets (4.27 → 4.73). These results suggest that RL not only improves final performance but also utilises limited data more effectively, aligning with our hypothesis that IDM’s rewarding mechanism provides a stronger inductive bias for intrinsic world modeling than purely supervised objectives.

## Appendix G Detailed Results for WorldPredictionBench

Table 8 presents a granular analysis of predictive performance across six consecutive autoregressive turns on WorldPredictionBench . This evaluation creates a challenging stress test for temporal consistency, as errors generated in early turns compound over the predictive horizon.

We observe two primary trends. First, as expected, all models exhibit performance decay as the horizon increases ( N N decreases as tasks are completed or fail). However, a clear divergence emerges between training paradigms. The direct supervised baseline ( Liquid-SFT ) suffers from rapid degradation, dropping from an overall score of 3.09 in Turn 1 to 1.17 by Turn 4. In contrast, our proposed SWIRL demonstrate significantly improved robustness against this compounding error. The Ours (Best) configuration, maintains a score of 1.59 at Turn 4. This indicates that the reciprocal cycle does not merely memorise single-step transitions but internalises more robust physical dynamics that persist over long-horizon rollouts. While large-scale unified models like Bagel provide a high upper bound, our method close the gap compared to SFT baseline.

## Appendix H Detailed Results for Iterative Results

Table 9 examines the iterative training dynamics of Forward World Modeling (FWM) and Inverse Dynamics Modeling (IDM) under two architectural choices: using separate weights for the FWM and IDM versus shared weights. We report results across three training iterations to highlight peak performance and learning progression.

The separate-weight configuration achieves the highest peak FWM performance, with Iteration 1 attaining the best average FWM score (5.06) and consistently strong results across all benchmarks. In particular, gains on MagicBrush, Action Genome, and Something indicate that decoupling the FWM and IDM allows each component to specialise more effectively, leading to higher-quality forward predictions when the system is optimally aligned.

While the shared-weight setup exhibits competitive and stable behaviour, it does not surpass the peak generative performance achieved by the separate-weight model. Notably, although IDM accuracy continues to improve slightly in later iterations for both settings, the separate-weight design reaches its optimal balance between FWM quality and IDM alignment earlier in training. This suggests that architectural decoupling enables more expressive forward modeling, even if later iterations yield diminishing returns.

Overall, these results indicate that separating FWM and IDM parameters is advantageous for maximising peak forward world modelling performance, motivating our choice of the separate-weight configuration in the main experiments where peak capability is the primary objective.

## Appendix I Ablation on GRPO Rollout Size.

We analyse the effect of rollout size. The group size G G is a critical hyperparameter in GRPO, as it governs the accuracy of the baseline estimation and the diversity of the exploration within each optimisation step. We empirically evaluate G ∈ { 8 , 16 , 32 , 64 } G\in\{8,16,32,64\} across Aurora-Bench , with results summarised in Table 10 . We observe that scaling the rollout size generally improves model performance, achieving a peak average score of 4.90 at G = 64 G=64 . We attribute this to the reduced variance in advantage estimation: a larger pool of generations provides a more robust approximation of the expected return, enabling the policy to distinguish high-quality trajectories more effectively. Notably, while G = 64 G=64 yields the best absolute performance—particularly in complex environments like Kubric, the smaller configuration of G = 16 G=16 remains highly competitive (4.80 avg.) while requiring much less memory and compute during the generation phase.

## Appendix J Qualitative Examples

We provide some qualitative examples in Figure 7 to illustrate the visual predictions of SWIRL across three distinct benchmarks: Aurora-Bench , ByteMorph , and WorldPredictionBench .

Aurora-Bench . The top panel demonstrates results on the AURORA benchmark, covering various subsets such as MagicBrush, Something, Emu, Kubric, and Whatsup. These examples highlight the model’s capability to perform diverse action-centric image editing tasks, ranging from the general editing (e.g., Add a supernova explosion in the sky ) and background replacement (e.g., changing to Yellowstone National Park ) to precise geometric transformations and spatial reasoning. For instance, in the Something and Kubric subsets, the model successfully executes actions concerning physical regularities like flip the bottle upside down and distinct spatial rearrangements like moving a specific plate to the left .

ByteMorph . The middle panel displays qualitative results for ByteMorph , focusing on fine-grained control over camera and object dynamics. We visualise three distinct categories: Camera Zoom, Camera Motion, and Object Motion. The results show the model’s ability to synthesise coherent view changes, such as zooming out to reveal context (e.g., the coastline and a second boat ) or shifting the camera angle upward. Additionally, the Object Motion example demonstrates the generation of localised movement, specifically raising an animal’s head while maintaining scene consistency.

WorldPredictionBench . The bottom panel illustrates long-horizon predictions on the WorldPredictionBench . Here, we show multi-step predictions where the model generates subsequent states based on the previous predicted image as the context and textual action descriptions. The examples depict long-horizon consistency in procedural tasks, such as replacing a car key battery (Start → Put in battery → Close cover) and arranging bedding (Start → Take out cover → Arrange nicely).

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
