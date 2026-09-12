##### Report GitHub Issue

Content selection saved. Describe the issue below:

# CDE: Curiosity-Driven Exploration for Efficient Reinforcement Learning in Large Language Models

###### Abstract

Reinforcement Learning with Verifiable Rewards (RLVR) is a powerful paradigm for enhancing the reasoning ability of Large Language Models (LLMs). Yet current RLVR methods often explore poorly, leading to premature convergence and entropy collapse. To address this challenge, we introduce Curiosity-Driven Exploration (CDE) , a framework that leverages the model’s own intrinsic sense of curiosity to guide exploration. We formalize curiosity with signals from both the actor and the critic: for the actor, we use perplexity over its generated response, and for the critic, we use the variance of value estimates from a multi-head architecture. Both signals serve as an exploration bonus within the RLVR framework to guide the model. Our theoretical analysis shows that the actor-wise bonus inherently penalizes overconfident errors and promotes diversity among correct responses; moreover, we connect the critic-wise bonus to the well-established count-based exploration bonus in RL. Empirically, our method achieves an approximate +3 point improvement over standard RLVR using GRPO/PPO on AIME benchmarks. Further analysis identifies a calibration collapse mechanism within RLVR, shedding light on common LLM failure modes.

## 1 Introduction

The reasoning ability of Large Language Models (LLMs) has achieved remarkable performance across diverse application domains such as mathematics ( Shao et al., 2024 ) and coding ( Guo et al., 2024 ) . A central challenge in this development is how to efficiently elicit high-quality Chain-of-Thought (CoT) reasoning. A major breakthrough earlier this year was the introduction of reinforcement learning with verifiable rewards (RLVR), a training paradigm in which models are optimized directly using the signal of final-answer correctness. This approach removes the burden of designing and training potentially fragile reward models. Despite the emergence of various RLVR training algorithms, such as GRPO ( Guo et al., 2024 ) and DAPO ( Yu et al., 2025 ) , key issues remain. In particular, problems such as premature convergence and phenomena like entropy collapse ( Cui et al., 2025 ) have been widely observed during training, posing fundamental challenges to the stability and effectiveness of RLVR.

These challenges stem from the classic exploration-exploitation dilemma in reinforcement learning ( Sutton & Barto, 2018 ) . Phenomena like entropy collapse reveal a critical flaw in the training process: it is heavily biased towards exploitation, causing models to converge prematurely instead of sufficiently exploring their environment for better solutions. Although the RL literature encompasses a wide range of exploration strategies, these methods exhibit significant limitations when applied to LLMs. Simple heuristics, including entropy bonuses ( Haarnoja et al., 2018 ) and ϵ \epsilon -greedy policies ( Sutton & Barto, 2018 ) , either injecting randomness to the environment or encouraging the policy to be more stochastic. These methods are either provably suboptimal in theory ( Dann et al., 2022 ) or demonstrate debatable effectiveness in complex environments like Deep RL ( Andrychowicz et al., 2021 ) and LLM-based reasoning ( Cui et al., 2025 ; Shen, 2025 ) . More principled methods are count-based, which incentivize visiting rarely explored state–action pairs. Algorithms such as UCB ( Lai, 1987 ) for multi-armed bandits, LinUCB ( Li et al., 2010 ) , LSVI-UCB ( Jin et al., 2020 ) for linear bandits/MDPs achieve near-optimal exploration guarantees across a variety of settings. However, these methods (i) require computationally intensive operations such as matrix inversion, and (ii) heavily depend on highly expressive representations of state-action pair (reasoning paths), which become impractical for reasoning-focused LLMs with long chains of thought. Thus, developing efficient and scalable exploration methods for LLMs remains a key open challenge.

In our preliminary experiments, we investigate the direct application of count-based exploration methods to the RLVR setting. To avoid the computational burden of matrix inversion, we adopt the SimHash technique ( Tang et al., 2017 ) , which maps the embedding of a CoT response into a discrete hash code, and then uses the visitation frequency of hash cells as pseudo-counts (see Section 3.1 for details). However, as illustrated in Figure 1 , this approach proves problematic: it is difficult to meaningfully characterize a complex CoT reasoning trajectory with a fixed embedding vector. In practice, most responses collapse into the same or neighboring hash grids, leading to a highly concentrated distribution of counts and thus undermining the effectiveness of count-based exploration for RLVR.

In this work, we propose an intuitive approach that leverages the model’s intrinsic sense of curiosity as a guide for exploration. An LLM, having been trained on vast reasoning corpora, develops a sophisticated internal model of what constitutes a familiar versus a novel reasoning pattern. This parallels early childhood development ( Chu & Schulz, 2020 ) , where learning is not driven by a external summary and count of experiences, but is instead propelled by an intrinsic curiosity to explore novel situations. We formalize this principle in our Curiosity-Driven Exploration (CDE) framework, which considers curiosity signals from both the actor and the critic. For the actor, perplexity (PPL) over its generated response serves as the curiosity measure. For the critic, we measure curiosity via the variance of its posterior value distribution. We then approximate this posterior by extending the PPO framework with a multi-head, bootstrapped structure. The curiosity signals are served as an exploration bonus, shaping the reward and advantage functions to effectively guide exploration.

Our theoretical analysis offers further insights into the properties of our method. (i) Theorem 3.1 interprets the proposed perplexity-based bonus, showing that it intrinsically penalizes overconfident errors while encouraging diversity among correct responses. (ii) Theorem 3.2 establishes that in the linear MDP setting, our critic-based exploration bonus is theoretically equivalent to classical count-based bonuses, grounding our approach in established exploration principles.

Our empirical evaluation demonstrates consistent performance gains across four widely used mathematics benchmarks (AIME25, AIME24, AMC23, and MATH), including an approximate +3 point improvement on the challenging AIME benchmarks. Furthermore, our analysis of the training process supports our theoretical findings and reveals a phenomenon we term calibration collapse : under a naive GRPO policy, the model’s confidence progressively decouples from its correctness, while adding PPL bonus mitigates this miscalculation.

## 2 Preliminaries: RLVR, GRPO and PPO

We formulate the language generation process of LLMs as a sequential decision-making problem ( Yu et al., 2025 ; Yue et al., 2025 ) . Specifically, we consider two reinforcement learning algorithms: Group Relative Policy Optimization (GRPO), a critic-free method, and Proximal Policy Optimization (PPO), a canonical actor–critic method. We adopt the training paradigm of Reinforcement Learning with Verifiable Rewards (RLVR) ( Guo et al., 2025 ; Lambert et al., 2024 ) and utilize a rule-based verifier to compare the generated response with the ground truth to judge its correctness.

### 2.1 Group Relative Policy Optimization (GRPO, Shao et al. 2024 )

GRPO is an REINFORCE-style optimization algorithm. Let π θ \pi_{\theta} denote the LLM policy with parameters θ \theta . At each training step, given a prompt q q sampled from the dataset 𝒟 \mathcal{D} , the current policy π θ \pi_{\theta} generates a group of G G candidate outputs { o 1 , o 2 , … , o G } \{o_{1},o_{2},\ldots,o_{G}\} . For each candidate o i o_{i} , we compute its total reward r i = r ⁡ ( o i , q ) r_{i}=r(o_{i},q) .

The advantage for each output is computed by normalizing its reward with respect to the group’s rewards: A i = r i − mean ⁡ ( r 1 , … , r G ) std ⁡ ( r 1 , … , r G ) + δ , A_{i}=\frac{r_{i}-\operatorname{mean}(r_{1},\ldots,r_{G})}{\operatorname{std}(r_{1},\ldots,r_{G})+\delta}, where δ \delta is a small constant for numerical stability. The same advantage A i A_{i} is applied to all tokens in o i o_{i} . Let π θ old \pi_{\theta_{\text{old}}} be the policy from the previous step and π ref \pi_{\text{ref}} the original pre-trained model. GRPO maximizes: ℒ GRPO ( θ ) = 𝔼 q ∼ 𝒟 , { o i } ∼ π θ old [ 1 G ∑ i = 1 G 1 | o i | ∑ t = 1 | o i | ℒ θ ( r ~ i , t , A i ) ] − β D KL ( π θ ∥ π ref ) , \mathcal{L}_{\text{GRPO}}(\theta)=\mathbb{E}_{q\sim\mathcal{D},\{o_{i}\}\sim\pi_{\theta_{\text{old}}}}\left[\frac{1}{G}\sum_{i=1}^{G}\frac{1}{|o_{i}|}\sum_{t=1}^{|o_{i}|}\mathcal{L}_{\theta}(\tilde{r}_{i,t},A_{i})\right]-\beta D_{\text{KL}}\left(\pi_{\theta}\|\pi_{\text{ref}}\right), where the clipped objective is ℒ θ ​ ( r ~ i , t , A i ) = min ⁡ ( r ~ i , t ​ A i , clip ​ ( r ~ i , t , 1 − ε , 1 + ε ) ​ A i ) , r ~ i , t = π θ ​ ( o i , t ∣ q , o i , < t ) π θ old ​ ( o i , t ∣ q , o i , < t ) . \mathcal{L}_{\theta}(\tilde{r}_{i,t},A_{i})=\min\left(\tilde{r}_{i,t}A_{i},\text{clip}(\tilde{r}_{i,t},1-\varepsilon,1+\varepsilon)A_{i}\right),\quad\tilde{r}_{i,t}=\frac{\pi_{\theta}(o_{i,t}\mid q,o_{i,<t})}{\pi_{\theta_{\text{old}}}(o_{i,t}\mid q,o_{i,<t})}. Here, ε \varepsilon and β \beta control the ratio clipping threshold and the KL-penalty strength, respectively. The clipping mitigates large, unstable policy updates, while the KL term constrains deviation from π ref \pi_{\text{ref}} .

### 2.2 Proximal Policy Optimization (PPO, Schulman et al. 2017 )

PPO is an actor–critic algorithm that maintains both a policy (actor) π θ \pi_{\theta} and a value function (critic) V ϕ V_{\phi} with parameters ϕ \phi , estimating the expected total reward from a given state (prompt and sequence prefix). The advantage function in PPO leverages the critic to reduce variance. Specifically, Generalized Advantage Estimation (GAE) is applied to compute token-level advantages. For an output o i o_{i} with sentence-level reward r i r_{i} , the GAE at token t t is: A i , t = ∑ l = t | o i | ( γ ​ λ ) l − t ​ δ i , l , A_{i,t}=\sum_{l=t}^{|o_{i}|}(\gamma\lambda)^{l-t}\delta_{i,l}, where δ i , l = r i , l + γ ​ V ϕ ​ ( q , o i , ≤ l + 1 ) − V ϕ ​ ( q , o i , ≤ l ) , \delta_{i,l}=r_{i,l}+\gamma V_{\phi}(q,o_{i,\leq l+1})-V_{\phi}(q,o_{i,\leq l}), and in our setting r i , l = 0 r_{i,l}=0 for all non-terminal tokens, with r i , | o i | = r i r_{i,|o_{i}|}=r_{i} . The hyperparameters γ \gamma and λ \lambda are the discount factor and GAE trace-decay, respectively. The PPO objective is: ℒ PPO ( θ , ϕ ) = 𝔼 q ∼ 𝒟 , { o i } ∼ π θ old [ 1 | o i | ∑ t = 1 | o i | [ ℒ θ ( r ~ i , t , A i , t ) − c 1 ℒ ϕ ( q , o i , < t , r i ) ] ] − β D KL ( π θ ∥ π ref ) , \mathcal{L}_{\text{PPO}}(\theta,\phi)=\mathbb{E}_{q\sim\mathcal{D},\{o_{i}\}\sim\pi_{\theta_{\text{old}}}}\Big[\frac{1}{|o_{i}|}\sum_{t=1}^{|o_{i}|}\left[\mathcal{L}_{\theta}(\tilde{r}_{i,t},A_{i,t})-c_{1}\mathcal{L}_{\phi}(q,o_{i,<t},r_{i})\right]\Big]-\beta D_{\text{KL}}\left(\pi_{\theta}\|\pi_{\text{ref}}\right), where ℒ θ \mathcal{L}_{\theta} is as in GRPO but with per-token A i , t A_{i,t} , and the value loss is: ℒ ϕ ​ ( ϕ ) = ( V ϕ ​ ( q , o i , < t ) − r i ) 2 . \mathcal{L}_{\phi}(\phi)=\left(V_{\phi}(q,o_{i,<t})-r_{i}\right)^{2}. In practice, we alternate optimization of the actor ( θ \theta ) and the critic ( ϕ \phi ).

## 3 CDE: Curiosity-Driven Exploration

In this section, we first explore count-based exploration and identify two of its key challenges. To overcome these challenges, we propose Curiosity-Driven Exploration (CDE), a systematic framework that considers curiosity signals from both the actor and the critic. We introduce the detailed formulations of actor and critic curiosity in Section 3.2 and Section 3.3 , respectively.

### 3.1 Challenge of Count-based exploration for RLVR

The core idea of count-based exploration is to measure the occurrence of Chain-of-Thought (CoT) patterns via sentence embeddings, and to assign an exploration bonus to rarely occurred CoTs. While conceptually appealing, this approach faces two major challenges:

• Curse of dimensionality: Classical count-based methods (e.g., LSVI-UCB ( Jin et al., 2020 ) , CFPO ( Cassel & Rosenberg, 2024 ) ) rely on computing the inverse of the covariance matrix Λ t − 1 \Lambda_{t}^{-1} (see Appendix E ) to construct historical visitation ellipsoids. For high-dimensional embeddings, this operation is computationally prohibitive.

To circumvent the need for matrix inversion, we investigated hash-based counts ( Tang et al., 2017 ) (details in Appendix C ), which project sentence embeddings into discrete hash grids and treat grid visitation frequency as a proxy for counts. However, this alternative introduces a second limitation:

• Poor expressiveness of embeddings: As illustrated in Figure 1 , after hash coding, most CoT embeddings collapse into neighboring hash grids. This clustering highlights the limited ability of sentence embeddings to distinguish between diverse reasoning patterns, leading to ineffective exploration.

In this work, we move beyond the paradigm of explicit state–action counts and instead utilize the model’s own measure of novelty. Our approach is motivated by the key intuition that agents, much like children in early cognitive development ( Chu & Schulz, 2020 ) , exhibit a form of curiosity . They respond with confidence when revisiting familiar states or CoT patterns, yet display uncertainty and exploratory behavior when confronted with novel situations. This learning process is not driven by a external count of experiences but is instead propelled by an intrinsic drive to explore. We first detail the implementation of the actor’s curiosity before turning to the critic’s.

### 3.2 Exploration Guided by Actor Curiosity

We model actor curiosity as the actor’s uncertainty about its own actions. Intuitively, a response that is surprising to the actor—i.e., has a low probability under its current policy—likely resides in an underexplored region of its learned distribution.

A natural and computationally efficient measure of this surprise is the perplexity of the actor’s generation. We formalize this as a sentence-level curiosity bonus, defined as the negative average log-probability of a generated sentence o = { o 1 , … , o T } o=\{o_{1},\ldots,o_{T}\} , given a prompt q q : B a ​ c ​ t ​ o ​ r ( q , o ) = − 1 T ∑ t = 1 T log π ( o t | o < t , q ) B_{actor}(q,o)=-\frac{1}{T}\sum_{t=1}^{T}\log\pi(o_{t}|o_{<t},q) (1) where π \pi denotes the actor policy. A higher value for B a ​ c ​ t ​ o ​ r ​ ( q , o ) B_{actor}(q,o) indicates greater surprise and thus a stronger intrinsic reward signal for exploration.

However, practically simply adding this bonus to the original reward can be unstable and sub-optimal. Unconstrained exploration might incentivize the model to generate high-perplexity but low-quality or inaccurate responses (a behavior known as reward hacking), or lead to over-exploration where the policy fails to converge to a stable, high-quality output. To ensure that exploration remains tethered to the primary objective of maximizing the original reward signal, we integrate the bonus using an adaptive clipping mechanism. The total sentence-level reward, r ~ \tilde{r} , is a combination of the original reward signal r ⁡ ( q , o ) r(q,o) and the curiosity bonus B a ​ c ​ t ​ o ​ r ​ ( q , o ) B_{actor}(q,o) , where the bonus is capped relative to the original reward: r ~ ​ ( q , o ) = r ⁡ ( q , o ) + ω t ​ min ⁡ ( | r ⁡ ( q , o ) | κ , α ​ B a ​ c ​ t ​ o ​ r ​ ( q , o ) ) \tilde{r}(q,o)=r(q,o)+{\color[rgb]{1,0,0}\omega_{t}}\min(\frac{|r(q,o)|}{\color[rgb]{0,0,1}\kappa},{\color[rgb]{0,1,0}\alpha}B_{actor}(q,o)) (2)

This formulation promotes exploration by rewarding sentences that the actor finds surprising, while constraining the bonus to remain a fraction of the original reward. In this way, the model is discouraged from trading response quality for novelty. The behavior of this reward function is controlled by three key hyperparameters:

• The bonus weight ω t \omega_{t} is a dynamic coefficient, typically set with an annealing schedule to decrease over the course of training. This allows for more aggressive exploration in the early stages and then gradually shifts focus towards exploitation of high-reward regions as the policy converges.

• The clipping ratio κ \kappa governs the maximum size of the curiosity bonus relative to the original reward. By capping the bonus at | r ⁡ ( q , o ) | / κ |r(q,o)|/\kappa , it ensures the bonus remains a supplement and prevents it from dominating the learning signal. This is particularly crucial when r ⁡ ( q , o ) r(q,o) is negative, as it guarantees the bonus cannot reverse the sign of the reward, maintaining the integrity of the penalty.

• The bonus scaling factor α \alpha normalizes the curiosity bonus B actor ​ ( q , o ) B_{\text{actor}}(q,o) before it is compared to the clipped reward. A higher α \alpha allows the curiosity bonus to reach the clipping threshold more easily, whereas a smaller α \alpha diminishes its potential impact.

#### Intuitions and Theoretical Foundation

While the above formulation specifies how the perplexity bonus is shaped and controlled through its hyperparameters, it is equally important to understand its qualitative effect on model behavior. To build this intuition, we analyze responses along two axes: correctness and actor perplexity. Among these four categories, two require particular attention:

1. Incorrect responses with low PPL indicate that the model is highly confident in its answer, yet the response is wrong. This reflects overfitting and should be penalized.

2. Correct responses with high PPL suggest that the model is less familiar with such answers, but they nevertheless turn out to be successful. This reflects effective exploration and should be encouraged.

As illustrated in Figure 2 , we find out that the PPL bonus intrinsically penalizes confident mistakes while encouraging novel correct responses. For correct responses, those novel responses (with higher PPL) receive a larger positive reward. For incorrect responses, those confident responses (with lower PPL) receive larger penalty as it receives smaller PPL bonus. The following theorem formalizes this intuition; its precise statement and proof are deferred to Appendix D .

###### Theorem 3.1 .

Let π t \pi_{t} denote the policy at training step t. With PPL bonus in Equation ( 1 ), the update to π t + 1 \pi_{t+1} calibrates the policy’s confidence as follows:

(i) Among correct responses, trajectories with higher perplexity receive a larger relative probability increase.

(ii) Among incorrect responses, trajectories with lower perplexity receive a larger relative probability decrease.

Previous analyses distinguish the PPL bonus from the entropy bonus, which is sample-agnostic at the token level. The entropy at any given step depends solely on the policy’s probability distribution and is independent of the token ultimately sampled. Because the calculation considers the entire next-token distribution π θ ​ ( v ∣ q , o < t ) \pi_{\theta}\left(v\mid q,o_{<t}\right) (Equation 3 ), the bonus ℋ t \mathcal{H}_{t} remains constant for any potential outcome (Figure 3 ). Therefore, even when the model makes a high-confidence error by sampling token 1, the entropy bonus fails to penalize that choice. ℋ t = − ∑ v ∈ 𝒱 π θ ( v ∣ q , o < t ) log π θ ( v ∣ q , o < t ) . \mathcal{H}_{t}=-\sum_{v\in\mathcal{V}}\pi_{\theta}\left(v\mid q,o_{<t}\right)\log\pi_{\theta}\left(v\mid q,o_{<t}\right). (3)

### 3.3 Exploration Guided by Critic Curiosity

In contrast to critic-free methods such as REINFORCE and GRPO, the critic (value function) in actor–critic frameworks provides a higher-level understanding of the prompt–response pair by estimating the expected reward-to-go. Since this estimate is learned directly from collected trajectories, its posterior distribution conditioned on the observed data naturally reflects the degree of coverage: regions with dense data yield concentrated (low-variance) posteriors, whereas sparsely sampled regions result in higher uncertainty. Posterior distributions are a well-established means of quantifying predictive uncertainty in deep learning models ( Gal & Ghahramani, 2016 ; Lakshminarayanan et al., 2017 ) . As shown in Figure 4 , the orange curve exhibits lower variance—evidence of better data coverage—whereas the other curve is more dispersed, reflecting greater uncertainty.

To approximate the posterior distribution of value estimates, we adopt the classical bootstrap method ( Davison & Hinkley, 1997 ) , widely used in statistics and increasingly recognized in the RL community as an effective tool for exploration ( Osband et al., 2016 ; Ciosek et al., 2019 ; Bai et al., 2021 ) . We implement this idea through a multi-head critic (upper-left subfigure in Figure 10 ), where K K critics { V ^ 1 , … , V ^ K } \{\widehat{V}_{1},\ldots,\widehat{V}_{K}\} share a common LLM backbone. Each head is trained on a resampled subset of the collected trajectories (bottom subfigure in Figure 10 ), thereby producing an empirical approximation to the posterior distribution.

We then use the standard deviation across the K K heads as a principled curiosity signal, guiding the policy toward regions of high disagreement where the value function remains uncertain and under-explored. In the following theorem, we establish a surprising yet intuitive result: under a Linear MDP assumption, the standard deviation of the bootstrap critics is a consistent estimator of the pseudo-count bonus.

###### Theorem 3.2 .

In linear MDPs, the standard deviation across multi-head critics can serve as a consistent estimator for the pseudo-count exploration bonus, ϕ n , h ⊤ ​ Λ n , h − 1 ​ ϕ n , h \sqrt{\phi_{n,h}^{\top}\Lambda_{n,h}^{-1}\phi_{n,h}} , as used in LSVI-UCB ( Jin et al., 2020 ) and CFPO ( Cassel & Rosenberg, 2024 ) , where ϕ n , h = ϕ ⁡ ( s n , h , a n , h ) \phi_{n,h}=\phi(s_{n,h},a_{n,h}) is the feature vector of a state-action pair and Λ n , h = ∑ i = 0 n ϕ i , h ​ ϕ i , h ⊤ + λ ​ I \Lambda_{n,h}=\sum_{i=0}^{n}\phi_{i,h}\phi_{i,h}^{\top}+\lambda I is the coverage matrix.

The rigorous formulation of the linear MDP assumptions and the proof of Theorem 3.2 are provided in Appendix E , while empirical results in Section 4.4 further support this finding. Building on this foundation, we now describe the training procedure of the multi-head PPO algorithm, which follows the standard stages of vanilla PPO: (i) generating trajectories with the actor, (ii) updating the actor, and (iii) updating the critic. The key distinction is that we incorporate the multi-head variance as an exploration bonus, encouraging the policy to visit under-explored regions. A visual illustration of these steps is shown in Figure 5 .

• Actor roll-out: Given a prompt q q , the actor generates a set of responses { o 1 , … , o n } \{o_{1},\ldots,o_{n}\} . Each response is denoted as o i = { o i , 1 , … , o i , | o i | } o_{i}=\{o_{i,1},\ldots,o_{i,|o_{i}|}\} . Correspondingly, we associate each response with a verifiable reward r i r_{i} . For clarity, we focus on the case of a single prompt q q .

• Actor update: In this step, the advantage is estimated as A ^ i , t = ∑ l = t | o i | ( γ ​ λ ) l − t ​ δ ^ i , l ⏟ ≈ A ~ i , t + ω t ​ min ⁡ ( | A ~ i , t | κ , α ​ B critic ​ ( q , o i , ≤ t + 1 ) ) . \widehat{A}_{i,t}=\underbrace{\sum_{l=t}^{|o_{i}|}(\gamma\lambda)^{l-t}\widehat{\delta}_{i,l}}_{\approx\tilde{A}_{i,t}}+{\color[rgb]{1,0,0}\omega_{t}}\min\left(\frac{|\tilde{A}_{i,t}|}{\color[rgb]{0,0,1}\kappa},{\color[rgb]{0,1,0}\alpha}B_{\text{critic}}(q,o_{i,\leq t+1})\right). (4) The advantage consists of two components. The first term, A ~ i , t \tilde{A}_{i,t} , largely follows the standard advantage estimation in PPO, except that we exploit bootstrap estimators by using an ensemble of value functions rather than a single point estimate: δ ^ i , l = r i , l + γ K ​ ∑ j = 1 K V ^ j ​ ( q , o i , ≤ l + 1 ) − 1 K ​ ∑ j = 1 K V ^ j ​ ( q , o i , ≤ l ) . \widehat{\delta}_{i,l}=r_{i,l}+\frac{\gamma}{K}\sum_{j=1}^{K}\widehat{V}_{j}(q,o_{i,\leq l+1})-\frac{1}{K}\sum_{j=1}^{K}\widehat{V}_{j}(q,o_{i,\leq l}). The second term of Equation 4 introduces the multi-head critic bonus ( B critic B_{\text{critic}} ), governed by the bonus weight ω t \omega_{t} , clipping ratio κ \kappa , and scaling factor α \alpha (see discussion following Equation ( 2 ) for interpretation). Specifically, B critic B_{\text{critic}} is defined as the standard deviation across the K K value heads, encouraging exploration by assigning higher bonus to actions leading to uncertain/less-visited regions: B critic ​ ( q , o i , ≤ t + 1 ) = std ​ ( { V ^ j ​ ( q , o i , ≤ t + 1 ) | 1 ≤ j ≤ K } ) . B_{\text{critic}}\left(q,o_{i,\leq t+1}\right)=\text{std}\left(\big\{\widehat{V}_{j}(q,o_{i,\leq t+1})\big|1\leq j\leq K\big\}\right). (5)

• Critic update: We use the collected roll-outs to update the critic. For notational convenience, let the dataset be 𝒟 = { ( q , o i , ≤ t , r i ) | i ∈ [ n ] , t ∈ [ | o i | ] } , \mathcal{D}=\{(q,o_{i,\leq t},r_{i})|i\in[n],t\in[|o_{i}|]\}, (6) consisting of (prompt, partial response, reward) triplets. For each critic head j j , we sample without replacement a subset 𝒟 j ⊂ 𝒟 \mathcal{D}_{j}\subset\mathcal{D} of size | 𝒟 j | = ζ ​ | 𝒟 | |\mathcal{D}_{j}|=\zeta|\mathcal{D}| , where the hyperparameter ζ ∈ ( 0 , 1 ] \zeta\in(0,1] controls the fraction of data assigned per head. Smaller ζ \zeta increases head diversity, while larger ζ \zeta improves sample efficiency. The multi-head critic is then updated with the following bootstrap loss: ℒ ϕ = 1 ζ ​ K ​ | 𝒟 | ​ ∑ j = 1 K ∑ ( q , o , r ) ∈ 𝒟 j ( V ^ j ​ ( q , o ) − r ) 2 . \mathcal{L}_{\phi}=\frac{1}{\zeta K|\mathcal{D}|}\sum_{j=1}^{K}\sum_{(q,o,r)\in\mathcal{D}_{j}}\left(\widehat{V}_{j}(q,o)-r\right)^{2}.

## 4 Experiments

### 4.1 Dataset and Model

In this paper, we adopt DAPO-17K ( Yu et al., 2025 ) for training and evaluate the performance of CDE on four challenging mathematical reasoning benchmarks: MATH ( Hendrycks et al., 2021 ) , AMC23 ( MAA, b ) , AIME24, and AIME25 ( MAA, a ) . These evaluations are designed to assess CDE’s effectiveness in comparison to standard PPO and GRPO algorithms. Due to computational resource constraints, we conduct training with a reduced setting. All experiments are implemented within the Verl framework using the Qwen3-4B-Base model ( Yang et al., 2025 ) . For fair comparison, all the models use the default prompt in DAPO-17K as shown in Appendix B and the implementation details in Appendix A to further elaborate on the training settings.

### 4.2 Main Results

The main results are presented in Table 1 while the training dynamic is presented in Figure 6 . Here PPL bonus denote adding Curiosity bonus on actors as in Equation 2 , K K Heads represents multi-head critic PPO with K K head critics. We report both average Pass@1 accuracy and Pass@16 results on evaluation datasets. The key observations are as follows:

• The PPL bonus further enhances the mathematical reasoning ability of the GRPO method, yielding an average improvement of approximately + 2.4 +2.4 points across datasets and demonstrating consistent superiority. In particular, our method achieves notable gains on Pass@16, surpassing the baseline GRPO by about + 8 +8 points on the AIME24 dataset.

• Across benchmarks, multi-head PPO consistently outperforms vanilla PPO. Using K = 4 K=4 and K = 16 K=16 heads yields average gains of roughly + 2 +2 points, and we observe an around + 10 +10 points of increase in Pass@16 on AIME datasets in many cases.

• The performance of multi-head PPO generally increases with the number of heads K K : with K = 2 K=2 delivers negligible gains over the baseline, and performance increase begin to plateau once K ≥ 4 K\geq 4 , which suggests that a modest number of heads already captures most of the epistemic uncertainty needed.

• As shown in Figure 6 , GRPO with PPL bonus and multi-head PPO increase test accuracy more slowly than baseline PPO/GRPO early in training, then catch up and ultimately surpass them. This pattern is consistent with enhanced exploration: the PPL bonus and head disagreement discourage premature exploitation of spurious high-reward trajectories. As state-action coverage expands, these signals calibrate, enabling a smoother shift to targeted exploitation and yielding higher final accuracy.

### 4.3 Understanding the Effect of the PPL Bonus

In this subsection, we present additional experiments to investigate the role of the PPL bonus, from which we derive the following key findings.

Bonus weight decay is crucial We compare four schedules for the bonus weight ω t \omega_{t} — No decay , Linear , Cosine , and Staircase —as illustrated in Figure 7 , with the performance of models trained under each schedule summarized in Table 2 . Briefly, the No decay schedule maintains strong exploration throughout training, while the Staircase schedule reduces ω t \omega_{t} abruptly, enabling strong exploration in the early phase and then removing the bonus for final convergence. The Linear and Cosine schedules provide intermediate behaviors.

The results in Table 2 underscore two insights: First, decay of the bonus weight is necessary, as all decay schedules outperform the no-decay baseline by enabling a gradual shift from exploration to exploitation. Second, strong exploration in the early phase is crucial, with the staircase scheme proving most effective by sustaining high exploration initially to broaden state–action coverage and then removing the bonus abruptly to allow stable convergence, whereas the gentler cosine and linear decays weaken the signal too soon and thus yield smaller gains.

Analysis of Entropy Dynamics As highlighted in prior work, entropy provides an important lens for understanding exploration ability ( Cui et al., 2025 ) , where a sharp decline in entropy often signals premature convergence and insufficient exploration. Figure 8 illustrates the entropy dynamics of baseline GRPO compared to our proposed methods. First, relative to the baseline, the PPL bonus alleviates entropy collapse, demonstrating its role in promoting exploration. Second, when comparing decay schemes, PPL with No Decay shows persistent fluctuations and fails to converge, whereas Staircase decay yields more stable entropy trajectories. This observation is consistent with our earlier findings that decaying the bonus weight is essential for ensuring stable convergence while still supporting effective exploration.

Analysis of Calibration As shown in Figure 9 , we plot the batch-wise mean response perplexity (PPL), stratified by answer correctness. In subfigure (a), we observe a phenomenon we term calibration collapse : early in naive GRPO training, correct responses have lower PPL (higher confidence) than incorrect ones, but as training progresses this gap shrinks and ultimately vanishes—confidence no longer tracks correctness. By contrast, with a PPL bonus (subfigure (b)), this separation is sustained throughout training.

This pattern is explained by Theorem 3.1 : while both naive GRPO and GRPO with a PPL bonus tend to increase confidence on correct answers, the PPL bonus additionally suppresses confident errors (low-PPL incorrect trajectories), thereby improving calibration.

This finding is original and practically important. Ideally, a trained model should be faithful—confident when its answer is correct and cautious when it is not. Better calibration enhances interpretability and supports inference-time selection strategies such as self-certainty BoN ( Wang et al., 2022 ) and DeepConf ( Fu et al., 2025 ) . It also connects to the growing literature on calibrating LLMs, both during training (e.g., ( Shen et al., 2024 ) ) and at test time (e.g., ( Ulmer et al., 2024 ) ).

### 4.4 Further Analysis of the Multi-Head Critic

Analysis of Dynamics of B critic B_{\text{critic}} We further examine the dynamics of the multi-head exploration bonus B critic B_{\text{critic}} by tracking its average value over the course of training. Specifically, for each training step, given the roll-outs 𝒟 \mathcal{D} defined in Equation 6 , we compute the average B critic B_{\text{critic}} across (prompt, partial response, reward) triplets within 𝒟 \mathcal{D} . As shown in sub-figure (a) of Figure 10 , this average decreases steadily as training progresses. The decline reflects that, with more training, similar trajectories are revisited more frequently, leading to reduced disagreement among critic heads. This phenomenon provides empirical support for interpreting the multi-head bonus as analogous to count-based exploration measures.

In sub-figure (b) of Figure 10 , we present a cross-dataset analysis by calculating the average standard deviation of the value estimates across different questions. Specifically, we evaluate three datasets: the training set (DAPO-17K), the in-domain validation set (AMC23), and the out-of-domain validation set GPQA ( Rein et al., 2023 ) . We observe that the training set exhibits a smaller standard deviation compared to both the in-domain and out-of-domain validation sets. This pattern aligns with the intuition that multi-head critics tend to show stronger disagreement on data that is less frequently encountered during training.

Analysis of sub-sample fraction ζ \zeta during critic update Additionally, we examine the sensitivity of the critic update to the hyperparameter ζ \zeta (sub-sample fraction). We vary ζ \zeta under two configurations—critics with 16 heads and with 4 heads—and compare ζ ∈ { 0.5 , 1 } \zeta\in\{0.5,1\} . As shown in Table 3 , while a larger number of heads benefits from a larger sub-sample fraction, the overall performance is stable across settings. The model demonstrates robustness to the masking fraction ζ \zeta , achieving similar results for both values tested (0.5 and 1.0).

## 5 Related Work

### 5.1 Reinforcement Learning (RL) for LLM reasoning

Reinforcement Learning is a central technique for advancing the reasoning capabilities of LLMs. Initial approaches relied on reward models that provided either outcome-based supervision, focusing on the final answer ( Cobbe et al., 2021 ) , or process-based supervision, evaluating intermediate reasoning steps ( Uesato et al., 2022 ) . To navigate more complex problem spaces, these foundational reward strategies were often augmented with search algorithms such as MCTS ( Feng et al., 2023 ; Tian et al., 2024 ; Chen et al., 2024 ; Wang et al., 2024c ) and Q* ( Wang et al., 2024b ; Wang et al., 2024a ) . More recently, RLVR ( Lambert et al., 2024 ) has emerged as a powerful alternative, demonstrating significant performance on complex reasoning tasks in mathematics and coding ( Guo et al., 2025 ) . Consequently, a growing body of work seeks to apply RLVR to diverse domains, including multi-modal reasoning ( Wang et al., 2025 ; Li et al., 2025 ) , logical reasoning ( Zhou et al., 2025 ) , search engine use ( Jin et al., 2025 ; Xiong et al., 2025 ) , and information extraction ( Dai et al., 2025b ) . Parallel efforts aim to improve upon the standard RLVR paradigm with techniques such as mixture-of-thought ( Zheng et al., 2025a ) , self-evolving ( Huang et al., 2025 ) , parallel thinking ( Zheng et al., 2025b ) . Despite these advances, persistent concerns remain regarding robustness ( Dai et al., 2025a ; Zhao et al., 2025 ) , calibration ( Shen et al., 2024 ) , and a lack of exploration evidenced by entropy collapse ( Cui et al., 2025 ; Shen, 2025 ) , highlighting the need for more principled training approaches.

### 5.2 Efficient exploration

Efficient exploration is a central challenge in Reinforcement Learning (RL), which aim to balance between exploration and exploitation ( Sutton & Barto, 2018 ; Weng, 2020 ; Amin et al., 2021 ) . Many foundational approaches are heuristic-based, such as Gaussian noise ( Lillicrap et al., 2015 ) or the ϵ \epsilon -greedy method ( Sutton & Barto, 2018 ) . Entropy regularization is a more principled heuristic, which encourages the policy to be more stochastic. While simple to implement, these methods are often undirected—they promote pure randomness. Consequently, they can be suboptimal ( Dann et al., 2022 ) with no significant gains in complex Deep RL ( Andrychowicz et al., 2021 ) or LLM training ( Cui et al., 2025 ; Shen, 2025 ) .

In contrast, a major class of methods incentivizes exploration by adding exploration bonus to guide the agent toward novel or uncertain parts of the environment. Count-based approaches like UCB ( Lai, 1987 ) , LinUCB ( Li et al., 2010 ) , and LSVI-UCB ( Jin et al., 2020 ) use pseudo-counts of state-action visitations to encourage exploring rarely visited areas, achieving near-optimal theoretical guarantees in bandits and linear MDPs. Similarly, prediction-based methods such as ICM ( Pathak et al., 2017 ) and RND ( Burda et al., 2018 ) use the error from a predictive model as a bonus, rewarding the agent for reaching states that are difficult to predict. Applying these guided exploration principles is a growing field in LLM. For instance, Bai et al. (2025) incorporate a count-based bonus into the RLHF process by introducing a coin flipping module. Gao et al. (2025) draws inspiration from RND by adding an auxiliary noise prediction network. However, both methods rely on expressive representations of long COT trajectories and introduce additional modules, which complicates the training framework. In contrast, CDE uses intrinsic curiosity signals from the actor and critics, requiring only minimal modifications to the framework and yielding efficient exploration both theoretically and empirically.

## 6 Conclusion and Future Work

We have presented Curiosity-Driven Exploration, an efficient technique that enhances agent learning by incorporating curiosity signals from both the actor and the critic. Our approach is notably lightweight, demanding only minor modifications to the original training architecture. Its effectiveness is demonstrated by consistent accuracy improvements over strong baselines on a suite of challenging mathematical reasoning benchmarks, with these empirical results strongly corroborating our underlying theoretical framework and intuition.

The calibration collapse revealed in our analysis aligns with recent findings on the root causes of LLM hallucination ( Kalai et al., 2025 ) , pointing to a promising avenue for future work. We hypothesize that the underlying source of this collapse is the reward design of RLVR training. Specifically, RLVR with outcome reward prioritizes correct final outcomes at the expense of rigorous intermediate reasoning. Our experiments shed light on this direction by demonstrating that an alternative multi-perspective reward design (e.g., the PPL bonus) can be valuable for guiding the RLVR process more effectively.

## References

Amin et al. (2021) Susan Amin, Maziar Gomrokchi, Harsh Satija, Herke Van Hoof, and Doina Precup. A survey of exploration methods in reinforcement learning. arXiv preprint arXiv:2109.00157 , 2021.

Andrychowicz et al. (2021) Marcin Andrychowicz, Anton Raichuk, Piotr Stańczyk, Manu Orsini, Sertan Girgin, Raphaël Marinier, Leonard Hussenot, Matthieu Geist, Olivier Pietquin, Marcin Michalski, et al. What matters for on-policy deep actor-critic methods? a large-scale study. In International conference on learning representations , 2021.

Bai et al. (2021) Chenjia Bai, Lingxiao Wang, Lei Han, Jianye Hao, Animesh Garg, Peng Liu, and Zhaoran Wang. Principled exploration via optimistic bootstrapping and backward induction. In International Conference on Machine Learning , pp. 577–587. PMLR, 2021.

Bai et al. (2025) Chenjia Bai, Yang Zhang, Shuang Qiu, Qiaosheng Zhang, Kang Xu, and Xuelong Li. Online preference alignment for language models via count-based exploration. arXiv preprint arXiv:2501.12735 , 2025.

Burda et al. (2018) Yuri Burda, Harrison Edwards, Amos Storkey, and Oleg Klimov. Exploration by random network distillation. arXiv preprint arXiv:1810.12894 , 2018.

Cassel & Rosenberg (2024) Asaf Cassel and Aviv Rosenberg. Warm-up free policy optimization: Improved regret in linear markov decision processes. Advances in Neural Information Processing Systems , 37:3275–3303, 2024.

Chen et al. (2024) Guoxin Chen, Minpeng Liao, Chengxi Li, and Kai Fan. Alphamath almost zero: process supervision without process. Advances in Neural Information Processing Systems , 37:27689–27724, 2024.

Chu & Schulz (2020) Junyi Chu and Laura E Schulz. Play, curiosity, and cognition. Annual Review of Developmental Psychology , 2(1):317–343, 2020.

Ciosek et al. (2019) Kamil Ciosek, Quan Vuong, Robert Loftin, and Katja Hofmann. Better exploration with optimistic actor critic. Advances in Neural Information Processing Systems , 32, 2019.

Cobbe et al. (2021) Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, et al. Training verifiers to solve math word problems. arXiv preprint arXiv:2110.14168 , 2021.

Cui et al. (2025) Ganqu Cui, Yuchen Zhang, Jiacheng Chen, Lifan Yuan, Zhi Wang, Yuxin Zuo, Haozhan Li, Yuchen Fan, Huayu Chen, Weize Chen, et al. The entropy mechanism of reinforcement learning for reasoning language models. arXiv preprint arXiv:2505.22617 , 2025.

Dai et al. (2025a) Runpeng Dai, Run Yang, Fan Zhou, and Hongtu Zhu. Breach in the shield: Unveiling the vulnerabilities of large language models. arXiv preprint arXiv:2504.03714 , 2025a.

Dai et al. (2025b) Runpeng Dai, Tong Zheng, Run Yang, Kaixian Yu, and Hongtu Zhu. R1-re: Cross-domain relation extraction with rlvr. arXiv preprint arXiv:2507.04642 , 2025b.

Dann et al. (2022) Chris Dann, Yishay Mansour, Mehryar Mohri, Ayush Sekhari, and Karthik Sridharan. Guarantees for epsilon-greedy reinforcement learning with function approximation. In International conference on machine learning , pp. 4666–4689. PMLR, 2022.

Davison & Hinkley (1997) Anthony Christopher Davison and David Victor Hinkley. Bootstrap methods and their application . Number 1. Cambridge university press, 1997.

Feng et al. (2023) Xidong Feng, Ziyu Wan, Muning Wen, Stephen Marcus McAleer, Ying Wen, Weinan Zhang, and Jun Wang. Alphazero-like tree-search can guide large language model decoding and training. arXiv preprint arXiv:2309.17179 , 2023.

Fu et al. (2025) Yichao Fu, Xuewei Wang, Yuandong Tian, and Jiawei Zhao. Deep think with confidence. arXiv preprint arXiv:2508.15260 , 2025.

Gal & Ghahramani (2016) Yarin Gal and Zoubin Ghahramani. Dropout as a bayesian approximation: Representing model uncertainty in deep learning. In international conference on machine learning , pp. 1050–1059. PMLR, 2016.

Gao et al. (2025) Jingtong Gao, Ling Pan, Yejing Wang, Rui Zhong, Chi Lu, Qingpeng Cai, Peng Jiang, and Xiangyu Zhao. Navigate the unknown: Enhancing llm reasoning with intrinsic motivation guided exploration. arXiv preprint arXiv:2505.17621 , 2025.

Guo et al. (2024) Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, YK Li, et al. Deepseek-coder: When the large language model meets programming–the rise of code intelligence. arXiv preprint arXiv:2401.14196 , 2024.

Guo et al. (2025) Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. arXiv preprint arXiv:2501.12948 , 2025.

Haarnoja et al. (2018) Tuomas Haarnoja, Aurick Zhou, Pieter Abbeel, and Sergey Levine. Soft actor-critic: Off-policy maximum entropy deep reinforcement learning with a stochastic actor. In International conference on machine learning , pp. 1861–1870. Pmlr, 2018.

Hendrycks et al. (2021) Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. Measuring mathematical problem solving with the math dataset. arXiv preprint arXiv:2103.03874 , 2021.

Huang et al. (2025) Chengsong Huang, Wenhao Yu, Xiaoyang Wang, Hongming Zhang, Zongxia Li, Ruosen Li, Jiaxin Huang, Haitao Mi, and Dong Yu. R-zero: Self-evolving reasoning llm from zero data. arXiv preprint arXiv:2508.05004 , 2025.

Jin et al. (2025) Bowen Jin, Hansi Zeng, Zhenrui Yue, Jinsung Yoon, Sercan Arik, Dong Wang, Hamed Zamani, and Jiawei Han. Search-r1: Training llms to reason and leverage search engines with reinforcement learning. arXiv preprint arXiv:2503.09516 , 2025.

Jin et al. (2020) Chi Jin, Zhuoran Yang, Zhaoran Wang, and Michael I Jordan. Provably efficient reinforcement learning with linear function approximation. In Conference on learning theory , pp. 2137–2143. PMLR, 2020.

Kalai et al. (2025) Adam Tauman Kalai, Ofir Nachum, Santosh S. Vempala, and Edwin Zhang. Why language models hallucinate, 2025. URL https://openai.com/index/why-language-models-hallucinate/ .

Lai (1987) Tze Leung Lai. Adaptive treatment allocation and the multi-armed bandit problem. The annals of statistics , pp. 1091–1114, 1987.

Lakshminarayanan et al. (2017) Balaji Lakshminarayanan, Alexander Pritzel, and Charles Blundell. Simple and scalable predictive uncertainty estimation using deep ensembles. Advances in neural information processing systems , 30, 2017.

Lambert et al. (2024) Nathan Lambert, Jacob Morrison, Valentina Pyatkin, Shengyi Huang, Hamish Ivison, Faeze Brahman, Lester James V Miranda, Alisa Liu, Nouha Dziri, Shane Lyu, et al. Tulu 3: Pushing frontiers in open language model post-training. arXiv preprint arXiv:2411.15124 , 2024.

Li et al. (2010) Lihong Li, Wei Chu, John Langford, and Robert E Schapire. A contextual-bandit approach to personalized news article recommendation. In Proceedings of the 19th international conference on World wide web , pp. 661–670, 2010.

Li et al. (2025) Zongxia Li, Wenhao Yu, Chengsong Huang, Rui Liu, Zhenwen Liang, Fuxiao Liu, Jingxi Che, Dian Yu, Jordan Boyd-Graber, Haitao Mi, et al. Self-rewarding vision-language model via reasoning decomposition. arXiv preprint arXiv:2508.19652 , 2025.

Lillicrap et al. (2015) Timothy P Lillicrap, Jonathan J Hunt, Alexander Pritzel, Nicolas Heess, Tom Erez, Yuval Tassa, David Silver, and Daan Wierstra. Continuous control with deep reinforcement learning. arXiv preprint arXiv:1509.02971 , 2015.

MAA (a) MAA. American invitational mathematics examination (AIME). Mathematics Competition Series, n.d.a. URL https://maa.org/math-competitions/aime .

MAA (b) MAA. American mathematics competitions (AMC 10/12). Mathematics Competition Series, n.d.b. URL https://maa.org/math-competitions/amc .

Osband et al. (2016) Ian Osband, Charles Blundell, Alexander Pritzel, and Benjamin Van Roy. Deep exploration via bootstrapped dqn. Advances in neural information processing systems , 29, 2016.

Pathak et al. (2017) Deepak Pathak, Pulkit Agrawal, Alexei A Efros, and Trevor Darrell. Curiosity-driven exploration by self-supervised prediction. In International conference on machine learning , pp. 2778–2787. PMLR, 2017.

Rein et al. (2023) David Rein, Betty Li Hou, Asa Cooper Stickland, Jackson Petty, Richard Yuanzhe Pang, Julien Dirani, Julian Michael, and Samuel R Bowman. Gpqa: A graduate-level google-proof q&a benchmark. arXiv preprint arXiv:2311.12022 , 2023.

Schulman et al. (2017) John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. arXiv preprint arXiv:1707.06347 , 2017.

Shao et al. (2024) Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li, Y Wu, et al. Deepseekmath: Pushing the limits of mathematical reasoning in open language models. arXiv preprint arXiv:2402.03300 , 2024.

Shen (2025) Han Shen. On entropy control in llm-rl algorithms. arXiv preprint arXiv:2509.03493 , 2025.

Shen et al. (2024) Maohao Shen, Subhro Das, Kristjan Greenewald, Prasanna Sattigeri, Gregory Wornell, and Soumya Ghosh. Thermometer: Towards universal calibration for large language models. arXiv preprint arXiv:2403.08819 , 2024.

Sutton & Barto (2018) Richard S Sutton and Andrew G Barto. Reinforcement Learning: An Introduction . MIT press, 2018.

Tang et al. (2017) Haoran Tang, Rein Houthooft, Davis Foote, Adam Stooke, OpenAI Xi Chen, Yan Duan, John Schulman, Filip DeTurck, and Pieter Abbeel. # exploration: A study of count-based exploration for deep reinforcement learning. Advances in neural information processing systems , 30, 2017.

Tian et al. (2024) Ye Tian, Baolin Peng, Linfeng Song, Lifeng Jin, Dian Yu, Lei Han, Haitao Mi, and Dong Yu. Toward self-improvement of llms via imagination, searching, and criticizing. Advances in Neural Information Processing Systems , 37:52723–52748, 2024.

Uesato et al. (2022) Jonathan Uesato, Nate Kushman, Ramana Kumar, Francis Song, Noah Siegel, Lisa Wang, Antonia Creswell, Geoffrey Irving, and Irina Higgins. Solving math word problems with process-and outcome-based feedback. arXiv preprint arXiv:2211.14275 , 2022.

Ulmer et al. (2024) Dennis Ulmer, Martin Gubri, Hwaran Lee, Sangdoo Yun, and Seong Joon Oh. Calibrating large language models using their generations only. arXiv preprint arXiv:2403.05973 , 2024.

Wang et al. (2024a) Ante Wang, Linfeng Song, Ye Tian, Baolin Peng, Dian Yu, Haitao Mi, Jinsong Su, and Dong Yu. Litesearch: Efficacious tree search for llm. arXiv preprint arXiv:2407.00320 , 2024a.

Wang et al. (2024b) Chaojie Wang, Yanchen Deng, Zhiyi Lyu, Liang Zeng, Jujie He, Shuicheng Yan, and Bo An. Q*: Improving multi-step reasoning for llms with deliberative planning. arXiv preprint arXiv:2406.14283 , 2024b.

Wang et al. (2025) Haozhe Wang, Chao Qu, Zuming Huang, Wei Chu, Fangzhen Lin, and Wenhu Chen. Vl-rethinker: Incentivizing self-reflection of vision-language models with reinforcement learning. arXiv preprint arXiv:2504.08837 , 2025.

Wang et al. (2024c) Xiyao Wang, Linfeng Song, Ye Tian, Dian Yu, Baolin Peng, Haitao Mi, Furong Huang, and Dong Yu. Towards self-improvement of llms via mcts: Leveraging stepwise knowledge with curriculum preference learning. arXiv preprint arXiv:2410.06508 , 2024c.

Wang et al. (2022) Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. Self-consistency improves chain of thought reasoning in language models. arXiv preprint arXiv:2203.11171 , 2022.

Weng (2020) Lilian Weng. Exploration strategies in deep reinforcement learning. lilianweng.github.io , Jun 2020. URL https://lilianweng.github.io/posts/2020-06-07-exploration-drl/ .

Xiong et al. (2025) Guangzhi Xiong, Qiao Jin, Xiao Wang, Yin Fang, Haolin Liu, Yifan Yang, Fangyuan Chen, Zhixing Song, Dengyu Wang, Minjia Zhang, et al. Rag-gym: Optimizing reasoning and search agents with process supervision. arXiv preprint arXiv:2502.13957 , 2025.

Yang et al. (2025) An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao, Chengen Huang, Chenxu Lv, et al. Qwen3 technical report. arXiv preprint arXiv:2505.09388 , 2025.

Yu et al. (2025) Qiying Yu, Zheng Zhang, Ruofei Zhu, Yufeng Yuan, Xiaochen Zuo, Yu Yue, Weinan Dai, Tiantian Fan, Gaohong Liu, Lingjun Liu, et al. Dapo: An open-source llm reinforcement learning system at scale. arXiv preprint arXiv:2503.14476 , 2025.

Yue et al. (2025) Yu Yue, Yufeng Yuan, Qiying Yu, Xiaochen Zuo, Ruofei Zhu, Wenyuan Xu, Jiaze Chen, Chengyi Wang, TianTian Fan, Zhengyin Du, et al. Vapo: Efficient and reliable reinforcement learning for advanced reasoning tasks. arXiv preprint arXiv:2504.05118 , 2025.

Zhao et al. (2025) Yulai Zhao, Haolin Liu, Dian Yu, SY Kung, Haitao Mi, and Dong Yu. One token to fool llm-as-a-judge. arXiv preprint arXiv:2507.08794 , 2025.

Zheng et al. (2025a) Tong Zheng, Lichang Chen, Simeng Han, R Thomas McCoy, and Heng Huang. Learning to reason via mixture-of-thought for logical reasoning. arXiv preprint arXiv:2505.15817 , 2025a.

Zheng et al. (2025b) Tong Zheng, Hongming Zhang, Wenhao Yu, Xiaoyang Wang, Xinyu Yang, Runpeng Dai, Rui Liu, Huiwen Bao, Chengsong Huang, Heng Huang, and Dong Yu. Parallel-r1: Towards parallel thinking via reinforcement learning. 2025b. URL https://api.semanticscholar.org/CorpusID:281218689 .

Zhou et al. (2025) Yujun Zhou, Jiayi Ye, Zipeng Ling, Yufei Han, Yue Huang, Haomin Zhuang, Zhenwen Liang, Kehan Guo, Taicheng Guo, Xiangqi Wang, et al. Dissecting logical reasoning in llms: A fine-grained evaluation and supervision study. arXiv preprint arXiv:2506.04810 , 2025.

## Appendix A Training Details

We use verl as the training framework 1 1 1 https://github.com/volcengine/verl . Configurations for training CDE and baseline models are listed in Table 4 .

## Appendix B Prompt

Figure 11: The prompt for RLVR training.

## Appendix C Details on Hash-based pseudo count

The core idea is to map a full prompt–response trajectory to a compact hash that serves as a pseudo-state for exploration. Given a prompt–response pair ( q , o ) (q,o) with tokenized sequences q = { q 1 , … , q D } q=\{q_{1},\ldots,q_{D}\} and o = { o 1 , … , o T } o=\{o_{1},\ldots,o_{T}\} , let the model produce last-layer hidden states 𝕙 = { h 1 , … , h D + T } \mathbb{h}=\{h_{1},\ldots,h_{D+T}\} , h i ∈ ℝ d h_{i}\in\mathbb{R}^{d} . We form a trajectory embedding h q , o ∈ ℝ d h_{q,o}\in\mathbb{R}^{d} from 𝕙 \mathbb{h} via one of: (i) h D + T h_{D+T} ; (ii) h D + T − 1 h_{D+T-1} ; or (iii) mean pooling 1 D + T ​ ∑ i = 1 D + T h i \frac{1}{D+T}\sum_{i=1}^{D+T}h_{i} . With a random projection matrix A ∈ ℝ k × d A\in\mathbb{R}^{k\times d} (rows drawn i.i.d. from 𝒩 ⁡ ( 0 , I ) \mathcal{N}(0,I) or Rademacher), we compute a k k -bit SimHash code ϕ ⁡ ( q , o ) = sign ⁡ ( A ​ h q , o ) ∈ { − 1 , + 1 } k , \phi(q,o)=\operatorname{sign}\!\big(Ah_{q,o}\big)\in\{-1,+1\}^{k}, and map it to a bucket index b = bucket ⁡ ( ϕ ) ∈ { 0 , … , 2 k − 1 } b=\mathrm{bucket}(\phi)\in\{0,\ldots,2^{k}-1\} . Let n ⁡ ( b ) n(b) be the visitation count of bucket b b . We apply intrinsic reward shaping to encourage rarely visited trajectories: r ~ ​ ( q , o ) = r ⁡ ( q , o ) + ω t ​ β t n ⁡ ( b ) , \tilde{r}(q,o)=r(q,o)+\omega_{t}\frac{\beta_{t}}{\sqrt{n(b)}}, where β t \beta_{t} is the weight for exploration bonus a. This yields an efficient, matrix-inversion–free intrinsic bonus that scales linearly in k ​ d kd per sample, following Tang et al. (2017) .

## Appendix D Proof for Calibration Theorem

Define r ~ t ​ ( q , o ) = r ⁡ ( q , o ) + b t ​ ( q , o ) \tilde{r}_{t}(q,o)=r(q,o)+b_{t}(q,o) where b t ​ ( q , o ) = ω ​ min ⁡ { κ ​ | r ⁡ ( q , o ) | , − α T o ​ log ⁡ π t ​ ( o | q ) } b_{t}(q,o)=\omega\min\{\kappa|r(q,o)|,-\frac{\alpha}{T_{o}}\log\pi_{t}(o|q)\} is a bonus function where T o T_{o} is the length of response o o . Note that ω \omega is a redundant variable in theory because we can write b t ​ ( q , o ) = min ⁡ { κ ′ ​ | r ⁡ ( q , o ) | , − α T o ​ log ⁡ π t ​ ( o | q ) } b_{t}(q,o)=\min\{\kappa^{\prime}|r(q,o)|,-\frac{\alpha}{T_{o}}\log\pi_{t}(o|q)\} with κ ′ = ω ​ κ \kappa^{\prime}=\omega\kappa and α ′ = ω ​ α \alpha^{\prime}=\omega\alpha . Given that r ⁡ ( x , y ) ∈ { 1 , − 1 } r(x,y)\in\{1,-1\} , it suffices to consider b t ​ ( q , o ) = min ⁡ { κ , − α T o ​ log ⁡ π t ​ ( o | q ) } b_{t}(q,o)=\min\{\kappa,-\frac{\alpha}{T_{o}}\log\pi_{t}(o|q)\} . Thus, as long as we use κ < 1 \kappa<1 , we have sign ​ ( r ~ t ​ ( q , o ) ) = sign ​ ( r ⁡ ( q , o ) ) \text{sign}(\tilde{r}_{t}(q,o))=\text{sign}(r(q,o)) . The introduce of bonus does not change the sign of the original correctness reward.

Consider single step policy optimization π t + 1 ( ⋅ | q ) = arg max π { ∑ o π ( o | q ) r ~ t ( q , o ) − 1 η KL ( π ( ⋅ | q ) ∥ π t ( ⋅ | q ) ) } , \displaystyle\pi_{t+1}(\cdot|q)=\arg\max_{\pi}\left\{\sum_{o}\pi(o|q)\tilde{r}_{t}(q,o)-\frac{1}{\eta}\text{KL}\left(\pi(\cdot|q)\|\pi_{t}(\cdot|q)\right)\right\}, which has closed-form solution π t + 1 ​ ( o | q ) = π t ​ ( o | q ) ​ exp ⁡ ( η ​ r ~ t ​ ( q , o ) ) ∑ o ′ π t ​ ( o ′ | q ) ​ exp ⁡ ( η ​ r ~ t ​ ( q , o ′ ) ) . \displaystyle\pi_{t+1}(o|q)=\frac{\pi_{t}(o|q)\exp\left(\eta\tilde{r}_{t}(q,o)\right)}{\sum_{o^{\prime}}\pi_{t}(o^{\prime}|q)\exp\left(\eta\tilde{r}_{t}(q,o^{\prime})\right)}. For any question q q and response o o . Define Z ⁡ ( q ) = ∑ o ′ π t ​ ( o ′ | q ) ​ exp ⁡ ( η ​ r ~ t ​ ( q , o ′ ) ) Z(q)=\sum_{o^{\prime}}\pi_{t}(o^{\prime}|q)\exp\left(\eta\tilde{r}_{t}(q,o^{\prime})\right) , we have log ⁡ π t + 1 ​ ( o | q ) = log ⁡ π t ​ ( o | q ) + η ​ r ~ t ​ ( q , o ) − log ⁡ ( Z ⁡ ( q ) ) . \displaystyle\log\pi_{t+1}(o|q)=\log\pi_{t}(o|q)+\eta\tilde{r}_{t}(q,o)-\log\left(Z(q)\right). Define Δ t ​ ( o | q ) = log ⁡ π t + 1 ​ ( o | q ) − log ⁡ π t ​ ( o | q ) \Delta_{t}(o|q)=\log\pi_{t+1}(o|q)-\log\pi_{t}(o|q) as the change of likelihood of response o o under question q q at update step t t . For two correct response o 1 + o^{+}_{1} and o 2 + o^{+}_{2} with length T o 1 + T_{o^{+}_{1}} and T o 2 + T_{o^{+}_{2}} , and − α T o 1 + ​ log ⁡ π t ​ ( o 1 + | q ) ≥ − α T o 2 + ​ log ⁡ π t ​ ( o 2 + | q ) -\frac{\alpha}{T_{o^{+}_{1}}}\log\pi_{t}(o^{+}_{1}|q)\geq-\frac{\alpha}{T_{o^{+}_{2}}}\log\pi_{t}(o^{+}_{2}|q) (i.e. o 1 + o_{1}^{+} has larger perplexity), we have Δ t ​ ( o 1 + | q ) − Δ t ​ ( o 2 + | q ) \displaystyle\Delta_{t}(o^{+}_{1}|q)-\Delta_{t}(o^{+}_{2}|q) = r ~ t ​ ( q , o 1 + ) − r ~ t ​ ( q , o 2 + ) \displaystyle=\tilde{r}_{t}(q,o^{+}_{1})-\tilde{r}_{t}(q,o^{+}_{2}) = b t ​ ( q , o 1 + ) − b t ​ ( q , o 2 + ) \displaystyle=b_{t}(q,o^{+}_{1})-b_{t}(q,o^{+}_{2}) = min ⁡ { κ , − α T o 1 + ​ log ⁡ π t ​ ( o 1 + | q ) } − min ⁡ { κ , − α T o 2 + ​ log ⁡ π t ​ ( o 2 + | q ) } \displaystyle=\min\{\kappa,-\frac{\alpha}{T_{o^{+}_{1}}}\log\pi_{t}(o^{+}_{1}|q)\}-\min\{\kappa,-\frac{\alpha}{T_{o^{+}_{2}}}\log\pi_{t}(o^{+}_{2}|q)\} ≥ 0 \displaystyle\geq 0

Similarly, for two incorrect response o 1 − o^{-}_{1} and o 2 − o^{-}_{2} with − α T o 1 − ​ log ⁡ π t ​ ( o 1 − | q ) ≥ − α T o 2 − ​ log ⁡ π t ​ ( o 2 − | q ) -\frac{\alpha}{T_{o^{-}_{1}}}\log\pi_{t}(o^{-}_{1}|q)\geq-\frac{\alpha}{T_{o^{-}_{2}}}\log\pi_{t}(o^{-}_{2}|q) (i.e. o 1 − o_{1}^{-} has larger perplexity), we have Δ t ​ ( o 1 − | q ) − Δ t ​ ( o 2 − | q ) ≥ 0 \Delta_{t}(o^{-}_{1}|q)-\Delta_{t}(o^{-}_{2}|q)\geq 0 .

Specifically, given a question q q , for any response ( o 1 , o 2 ) (o_{1},o_{2}) that has the same correctness label and − α T o 1 ​ log ⁡ π t ​ ( o 1 | q ) ≥ − α T o 2 ​ log ⁡ π t ​ ( o 2 | q ) -\frac{\alpha}{T_{o_{1}}}\log\pi_{t}(o_{1}|q)\geq-\frac{\alpha}{T_{o_{2}}}\log\pi_{t}(o_{2}|q) , we have • If r ~ t ​ ( q , o 1 ) ≥ 1 η ​ log ⁡ ( Z ⁡ ( q ) ) \tilde{r}_{t}(q,o_{1})\geq\frac{1}{\eta}\log\left(Z(q)\right) and r ~ t ​ ( q , o 2 ) ≥ 1 η ​ log ⁡ ( Z ⁡ ( q ) ) \tilde{r}_{t}(q,o_{2})\geq\frac{1}{\eta}\log\left(Z(q)\right) , then Δ t ​ ( o 1 | q ) ≥ 0 \Delta_{t}(o_{1}|q)\geq 0 and Δ t ​ ( o 2 | q ) ≥ 0 \Delta_{t}(o_{2}|q)\geq 0 but o 1 o_{1} has more likelihood increase.

• If r ~ t ​ ( q , o 1 ) ≥ 1 η ​ log ⁡ ( Z ⁡ ( q ) ) \tilde{r}_{t}(q,o_{1})\geq\frac{1}{\eta}\log\left(Z(q)\right) and r ~ t ​ ( q , o 2 ) < 1 η ​ log ⁡ ( Z ⁡ ( q ) ) \tilde{r}_{t}(q,o_{2})<\frac{1}{\eta}\log\left(Z(q)\right) , then Δ t ​ ( o 1 | q ) ≥ 0 \Delta_{t}(o_{1}|q)\geq 0 and Δ t ​ ( o 2 | q ) < 0 \Delta_{t}(o_{2}|q)<0 where o 1 o_{1} ’s likelihood increase but o 2 o_{2} ’s likelihood decrease.

• If r ~ t ​ ( q , o 1 ) < 1 η ​ log ⁡ ( Z ⁡ ( q ) ) \tilde{r}_{t}(q,o_{1})<\frac{1}{\eta}\log\left(Z(q)\right) and r ~ t ​ ( q , o 2 ) < 1 η ​ log ⁡ ( Z ⁡ ( q ) ) \tilde{r}_{t}(q,o_{2})<\frac{1}{\eta}\log\left(Z(q)\right) , then Δ t ​ ( o 1 | q ) < 0 \Delta_{t}(o_{1}|q)<0 and Δ t ​ ( o 1 | q ) < 0 \Delta_{t}(o_{1}|q)<0 but o 1 o_{1} has less likelihood decrease.

• It is impossible that r ~ t ​ ( q , o 1 ) < 1 η ​ log ⁡ ( Z ⁡ ( q ) ) \tilde{r}_{t}(q,o_{1})<\frac{1}{\eta}\log\left(Z(q)\right) and r ~ t ​ ( q , o 2 ) ≥ 1 η ​ log ⁡ ( Z ⁡ ( q ) ) \tilde{r}_{t}(q,o_{2})\geq\frac{1}{\eta}\log\left(Z(q)\right) given that ( o 1 , o 2 ) (o_{1},o_{2}) has the same correctness label and − α T o 1 ​ log ⁡ π t ​ ( o 1 | q ) ≥ − α T o 2 ​ log ⁡ π t ​ ( o 2 | q ) -\frac{\alpha}{T_{o_{1}}}\log\pi_{t}(o_{1}|q)\geq-\frac{\alpha}{T_{o_{2}}}\log\pi_{t}(o_{2}|q) .

## Appendix E Proof for Consistency of Multi-head Critic Bonus

Linear MDP and Assumptions

###### Assumption E.1 (Linear MDP) .

We consider finite horizon ℳ = ( 𝒮 , 𝒜 , R , P , H ) \mathcal{M}=(\mathcal{S},\mathcal{A},R,P,H) with horizon H H , state space 𝒮 \mathcal{S} , action space 𝒜 \mathcal{A} , reward function R : 𝒮 × 𝒜 → ℝ R:\mathcal{S}\times\mathcal{A}\rightarrow\mathbb{R} , and transition P : 𝒮 × 𝒜 → 𝒮 P:\mathcal{S}\times\mathcal{A}\rightarrow\mathcal{S} such that there exists a known feature ϕ ∈ ℝ d \phi\in\mathbb{R}^{d} and unknown features θ , ψ ∈ ℝ d \theta,\psi\in\mathbb{R}^{d} to ensure R ⁡ ( s , a ) = ϕ ​ ( s , a ) ⊤ ​ θ P ⁡ ( s ′ | s , a ) = ϕ ​ ( s , a ) ⊤ ​ ψ ​ ( s ′ ) . \displaystyle R(s,a)=\phi(s,a)^{\top}\theta\quad\quad P(s^{\prime}|s,a)=\phi(s,a)^{\top}\psi(s^{\prime}). Without loss of generality, we assume ‖ ϕ ⁡ ( s , a ) ‖ ≤ 1 \|\phi(s,a)\|\leq 1 for all ( s , a ) (s,a) , and ‖ ψ ⁡ ( s ′ ) ‖ ≤ d , ‖ θ ‖ 2 ≤ d \|\psi(s^{\prime})\|\leq\sqrt{d},\|\theta\|_{2}\leq\sqrt{d} .

###### Lemma E.2 (Proposition 2.3 in Jin et al. (2020) ) .

For linear MDPs that satisfy Assumption E.1 , there exists w h ⋆ ∈ ℝ d w_{h}^{\star}\in\mathbb{R}^{d} such that Q h π ( s , a ) := 𝔼 [ ∑ t = h H r t | s h = s , a h = a ] = ϕ ( s , a ) ⊤ w h ⋆ . Q_{h}^{\pi}(s,a):=\mathbb{E}\Big[\sum_{t=h}^{H}r_{t}\big|s_{h}=s,a_{h}=a\Big]=\phi(s,a)^{\top}w_{h}^{\star}.

The linearity of Q Q -functions enables using regression technique to solve it. Consider a dataset with n n observations 𝒟 = { s i , h , a i , h , G i , h } i = 1 n \mathcal{D}=\{s_{i,h},a_{i,h},G_{i,h}\}_{i=1}^{n} where G i , h G_{i,h} is the Monte-Carlo return. Let ϕ i , h = ϕ ⁡ ( s i , h , a i , h ) \phi_{i,h}=\phi(s_{i,h},a_{i,h}) and denote the regression noise as ε i , h = G i , h − ϕ i , h ⊤ ​ w h ⋆ \varepsilon_{i,h}=G_{i,h}-\phi_{i,h}^{\top}w_{h}^{\star} . We impose the following assumptions.

(A1) 𝔼 ⁡ [ ε i , h ∣ ϕ i , h ] = 0 \mathbb{E}[\varepsilon_{i,h}\mid\phi_{i,h}]=0 and { ( ε i , h ) } i = 1 n \{(\varepsilon_{i,h})\}_{i=1}^{n} are i.i.d. σ 2 \sigma^{2} –sub-Gaussian for each fixed h h ;

(A2) 1 n ​ ∑ i = 1 n ϕ i , h ​ ϕ i , h ⊤ → ℙ Σ t ≻ 0 \frac{1}{n}\sum_{i=1}^{n}\phi_{i,h}\phi_{i,h}^{\top}\xrightarrow{\mathbb{P}}\Sigma_{t}\succ 0

Jin et al. (2020) shows that doing value iteration on optimistically estimated Q function can achieve near-optimal regret for linear MDP, where the optimistic Q function is the combination of linear regression estimation and exploration bonus b n , h = β ​ ϕ n , h ⊤ ​ Λ n , h − 1 ​ ϕ n , h b_{n,h}=\beta\sqrt{\phi_{n,h}^{\top}\Lambda^{-1}_{n,h}\phi_{n,h}} , where Λ n , h = λ ​ I + ∑ i = 1 n ϕ i , h ​ ϕ i , h ⊤ \Lambda_{n,h}=\lambda I+\sum_{i=1}^{n}\phi_{i,h}\phi_{i,h}^{\top} and β \beta is some constant. Below we will formally connect our bootstrapped bonus with this term.

Formulation of the bootstrap multi-head critic

We accommodate the bootstrap multi-head into the linear-MDP setting. For any time step h h , we sample K K mini-batches { S k ⊂ [ n ] } k = 1 K \{S_{k}\subset[n]\}_{k=1}^{K} of size m = ζ ​ n m=\zeta n uniformly without replacement from 𝒟 \mathcal{D} and construct the ridge estimator as follows w ^ n , h ( k ) = arg ⁡ min ⁡ ∑ r ∈ S k w ⁡ ( G r , h − ϕ r , h ⊤ ​ w ) 2 + ζ ​ λ ​ ‖ w ‖ 2 . \widehat{w}_{n,h}^{(k)}=\arg\min_{w}\sum_{r\in S_{k}}(G_{r,h}-\phi_{r,h}^{\top}w)^{2}+\zeta\lambda\|w\|^{2}. For any feature ϕ ∈ ℝ d \phi\in\mathbb{R}^{d} , we define the bootstrap multi-head bonus as b h , K boot ​ ( ϕ ) = std ​ ( { ϕ ⊤ ​ w ^ n , h ( k ) | 1 ≤ k ≤ K } ) . b^{\text{boot}}_{h,K}(\phi)=\text{std}\left(\big\{\phi^{\top}\widehat{w}_{n,h}^{(k)}\big|1\leq k\leq K\big\}\right).

Elliptical (“count-based”) bonus in ( Jin et al., 2020 ) . The ridge estimator is constructed using all data across n n trajectories as follows w ^ n , h = arg ⁡ min ⁡ ∑ i = 1 n w ⁡ ( G i , h − ϕ i , h ⊤ ​ w ) 2 + ζ ​ λ ​ ‖ w ‖ 2 . \widehat{w}_{n,h}=\arg\min_{w}\sum_{i=1}^{n}(G_{i,h}-\phi_{i,h}^{\top}w)^{2}+\zeta\lambda\|w\|^{2}. For any query feature ϕ ∈ ℝ d \phi\in\mathbb{R}^{d} , the bonus term is b h cnt ​ ( ϕ ) = ϕ ⊤ ​ Λ n , h − 1 ​ ϕ b^{\text{cnt}}_{h}(\phi)=\sqrt{\phi^{\top}\Lambda_{n,h}^{-1}\phi} .

#### Formal Version and Proof of Theorem 3.2

###### Theorem E.3 .

Under Assumption E.1 and assumptions (A1)–(A2), for any fixed time-step h h and query ϕ ∈ ℝ d \phi\in\mathbb{R}^{d} , b h , K boot ​ ( ϕ ) → K → ∞ , n → ∞ ℙ β ​ ϕ ⊤ ​ Λ n , h − 1 ​ ϕ , b^{\text{boot}}_{h,K}(\phi)\xrightarrow[\ K\to\infty,\ n\to\infty\ ]{\ \mathbb{P}\ }\beta\sqrt{\phi^{\top}\Lambda_{n,h}^{-1}\phi}, where β \beta is some constant.

###### Proof.

For any time-step h h and S k ⊂ [ n ] S_{k}\subset[n] , we have the explicit solution of the ridge regression w ^ n , h = Λ n , h − 1 ​ ∑ i = 1 n ϕ i , h ​ G i , h . \widehat{w}_{n,h}=\Lambda_{n,h}^{-1}\sum_{i=1}^{n}\phi_{i,h}G_{i,h}. Conditioning on X h = [ ϕ 1 , h ⊤ ; … ; ϕ n , h ⊤ ] X_{h}=[\phi_{1,h}^{\top};\ldots;\phi_{n,h}^{\top}] , the conditional variance of the estimator is Var ​ ( ϕ ⊤ ​ w ^ n , h ∣ X h ) = σ 2 ​ ϕ ⊤ ​ ( Λ n , h − 1 − λ ​ Λ n , h − 2 ) ​ ϕ . \text{Var}\big(\phi^{\top}\widehat{w}_{n,h}\mid X_{h}\big)=\sigma^{2}\phi^{\top}\Big(\Lambda_{n,h}^{-1}-\lambda\Lambda_{n,h}^{-2}\Big)\phi. From Assumption (A2), we have ‖ Λ n , h − 1 ‖ op = O p ​ ( 1 / n ) \|\Lambda_{n,h}^{-1}\|_{\mathrm{op}}=O_{p}(1/n) , therefore ϕ ⊤ ​ Λ n , h − 1 ​ ϕ ≤ ‖ ϕ ‖ 2 ​ ‖ Λ n , h − 1 ‖ op = O p ​ ( 1 / n ) ​ and ​ ϕ ⊤ ​ Λ n , h − 2 ​ ϕ = O p ​ ( 1 / n 2 ) , \phi^{\top}\Lambda_{n,h}^{-1}\phi\leq\|\phi\|^{2}\,\|\Lambda_{n,h}^{-1}\|_{\mathrm{op}}=O_{p}(1/n)~~\text{and}~~\phi^{\top}\Lambda_{n,h}^{-2}\phi=O_{p}(1/n^{2}), and n ​ ϕ ⊤ ​ ( Λ n , h − 1 − λ ​ Λ n , h − 2 ) ​ ϕ − n ​ ϕ ⊤ ​ Λ n , h − 1 ​ ϕ = − n ​ λ ​ ϕ ⊤ ​ Λ n , h − 2 ​ ϕ → ℙ 0 . n\phi^{\top}\Big(\Lambda_{n,h}^{-1}-\lambda\Lambda_{n,h}^{-2}\Big)\phi-n\phi^{\top}\Lambda_{n,h}^{-1}\phi=-n\lambda\phi^{\top}\Lambda_{n,h}^{-2}\phi\xrightarrow{\mathbb{P}}0. Therefore, we have ϕ ⊤ ​ ( Λ n , h − 1 − λ ​ Λ n , h − 2 ) ​ ϕ → ℙ ϕ ⊤ ​ Λ n , h − 1 ​ ϕ . \phi^{\top}\Big(\Lambda_{n,h}^{-1}-\lambda\Lambda_{n,h}^{-2}\Big)\phi\xrightarrow{\mathbb{P}}\phi^{\top}\Lambda_{n,h}^{-1}\phi.

Before moving to b h , K boot ​ ( ϕ ) b^{\text{boot}}_{h,K}(\phi) , we define the following quantities Δ ​ Σ = 1 ζ ​ ∑ r ∈ S k ϕ r , h ​ ϕ r , h ⊤ − ∑ i = 1 n ϕ i , h ​ ϕ i , h ⊤ , b = ∑ i = 1 n ϕ i , h ​ G i , h , b s = 1 ζ ​ ∑ r ∈ S k ϕ r , h ​ G r , h , Δ ​ b = b s − b . \Delta\Sigma=\frac{1}{\zeta}\sum_{r\in S_{k}}\phi_{r,h}\phi_{r,h}^{\top}-\sum_{i=1}^{n}\phi_{i,h}\phi_{i,h}^{\top},\quad b=\sum_{i=1}^{n}\phi_{i,h}G_{i,h},\quad b_{s}=\frac{1}{\zeta}\sum_{r\in S_{k}}\phi_{r,h}G_{r,h},\quad\Delta b=b_{s}-b. Since Σ t ≻ 0 \Sigma_{t}\succ 0 , matrix Bernstein for sampling without replacement yields ‖ Δ ​ Σ ‖ op = O p ​ ( n ) \|\Delta\Sigma\|_{\mathrm{op}}=O_{p}(\sqrt{n}) . Use the expansion ( Λ n , h + Δ ​ Σ ) − 1 = Λ n , h − 1 − Λ n , h − 1 ​ Δ ​ Σ ​ Λ n , h − 1 + R Σ , ‖ R Σ ‖ op = O p ​ ( ‖ Λ n , h − 1 ‖ op 3 ​ ‖ Δ ​ Σ ‖ op 2 ) = O p ​ ( 1 / n 2 ) . (\Lambda_{n,h}+\Delta\Sigma)^{-1}=\Lambda_{n,h}^{-1}-\Lambda_{n,h}^{-1}\Delta\Sigma\Lambda_{n,h}^{-1}+R_{\Sigma},\quad\|R_{\Sigma}\|_{\mathrm{op}}=O_{p}(\|\Lambda_{n,h}^{-1}\|_{\mathrm{op}}^{3}\|\Delta\Sigma\|_{\mathrm{op}}^{2})=O_{p}(1/n^{2}).

The k k -th bootstrap ridge solution is w ^ n , h ( k ) = ( Λ n , h + Δ ​ Σ ) − 1 ​ b s . \widehat{w}^{(k)}_{n,h}=(\Lambda_{n,h}+\Delta\Sigma)^{-1}b_{s}. Subtracting w ^ n , h = Λ n , h − 1 ​ b \widehat{w}_{n,h}=\Lambda_{n,h}^{-1}b and inserting the expansion, w ^ ( k ) n , h − w ^ n , h = Λ n , h − 1 ​ Δ ​ b − Λ n , h − 1 ​ Δ ​ Σ ​ w ^ n , h ⏟ first order + ( − Λ n , h − 1 ​ Δ ​ Σ ​ Λ n , h − 1 ​ Δ ​ b + R Σ ​ b s ) ⏟ = : r n . \widehat{w}^{(k)}_{n,h}-\widehat{w}_{n,h}=\underbrace{\Lambda_{n,h}^{-1}\Delta b-\Lambda_{n,h}^{-1}\Delta\Sigma\,\widehat{w}_{n,h}}_{\text{first order}}+\underbrace{\big(-\Lambda_{n,h}^{-1}\Delta\Sigma\Lambda_{n,h}^{-1}\Delta b+R_{\Sigma}b_{s}\big)}_{=:r_{n}}. Since G i , h = ϕ i , h ⊤ ​ w h + ϵ i , h G_{i,h}=\phi_{i,h}^{\top}w_{h}+\epsilon_{i,h} , for any ϕ \phi we have ϕ ⊤ ​ ( w ^ n , h ( k ) − w ^ n , h ) = ϕ ⊤ ​ Λ n , h − 1 ​ ( 1 ζ ​ ∑ r ∈ S k ϕ r , h ​ ϵ r , h − ∑ i = 1 n ϕ i , h ​ ϵ i , h ) + ϕ ⊤ ​ Λ n , h − 1 ​ Δ ​ Σ ​ ( w h ⋆ − w ^ n , h ) + ϕ ⊤ ​ r n . \phi^{\top}(\widehat{w}^{(k)}_{n,h}-\widehat{w}_{n,h})=\phi^{\top}\Lambda_{n,h}^{-1}\Big(\frac{1}{\zeta}\sum_{r\in S_{k}}\phi_{r,h}\epsilon_{r,h}-\sum_{i=1}^{n}\phi_{i,h}\epsilon_{i,h}\Big)+\phi^{\top}\Lambda_{n,h}^{-1}\Delta\Sigma(w_{h}^{\star}-\widehat{w}_{n,h})+\phi^{\top}r_{n}. (7) From standard results for ridge regression, we have ‖ w h ⋆ − w ^ n , h ‖ 2 = O ℙ ​ ( 1 / n ) \|w_{h}^{\star}-\widehat{w}_{n,h}\|_{2}=O_{\mathbb{P}}(1/\sqrt{n}) , thus we have the second term ϕ ⊤ ​ Λ n , h − 1 ​ Δ ​ Σ ​ ( w h ⋆ − w ^ n , h ) = O ℙ ​ ( 1 / n ) \phi^{\top}\Lambda_{n,h}^{-1}\Delta\Sigma(w_{h}^{\star}-\widehat{w}_{n,h})=O_{\mathbb{P}}(1/n) . Similarly, for the last term we have ϕ ⊤ ​ r n ≤ ‖ ϕ ‖ ​ ( ‖ Λ n , h − 1 ‖ op 2 ​ ‖ Δ ​ Σ ‖ op ​ ‖ Δ ​ b ‖ op + ‖ Δ ​ Σ ‖ op ​ ‖ b s ‖ op ) = O ℙ ​ ( 1 / n ) . \phi^{\top}r_{n}\leq\|\phi\|\left(\|\Lambda_{n,h}^{-1}\|^{2}_{\mathrm{op}}\|\Delta\Sigma\|_{\mathrm{op}}\|\Delta b\|_{\mathrm{op}}+\|\Delta\Sigma\|_{\mathrm{op}}\|b_{s}\|_{\mathrm{op}}\right)=O_{\mathbb{P}}(1/n). Therefore, both terms are negligible at the ⋅ \sqrt{\cdot} scale. Condition on ( X h , { ϵ i , h } i = 1 n ) (X_{h},\{\epsilon_{i,h}\}_{i=1}^{n}) the only randomness comes from S S . By finite-population sampling theory, Var ∗ ​ ( 1 ζ ​ ∑ r ∈ S ϕ r , h ​ ϵ r , h ) = 1 − ζ ζ ​ ∑ i = 1 n ϕ i , h ​ ϕ i , h ⊤ ​ σ 2 . \text{Var}^{*}\Big(\frac{1}{\zeta}\sum_{r\in S}\phi_{r,h}\epsilon_{r,h}\Big)=\frac{1-\zeta}{\zeta}\sum_{i=1}^{n}\phi_{i,h}\phi_{i,h}^{\top}\sigma^{2}. Therefore, Var ∗ ​ ( ϕ ⊤ ​ ( w ^ n , h ( k ) − w ^ n , h ) ) \displaystyle\text{Var}^{*}\Big(\phi^{\top}(\widehat{w}^{(k)}_{n,h}-\widehat{w}_{n,h})\Big) = 1 − ζ ζ ​ σ 2 ​ ϕ ⊤ ​ Λ n , h − 1 ​ ( ∑ i = 1 n ϕ i , h ​ ϕ i , h ⊤ ) ​ Λ n , h − 1 ​ ϕ + o ℙ ​ ( 1 / n ) \displaystyle=\frac{1-\zeta}{\zeta}\sigma^{2}\phi^{\top}\Lambda_{n,h}^{-1}\Big(\sum_{i=1}^{n}\phi_{i,h}\phi_{i,h}^{\top}\Big)\Lambda_{n,h}^{-1}\phi+o_{\mathbb{P}}\big(1/n\big) = 1 − ζ ζ ​ σ 2 ​ ϕ ⊤ ​ ( Λ n , h − 1 − λ ​ Λ n , h − 2 ) ​ ϕ + o ℙ ​ ( 1 / n ) \displaystyle=\frac{1-\zeta}{\zeta}\sigma^{2}\phi^{\top}\Big(\Lambda_{n,h}^{-1}-\lambda\Lambda_{n,h}^{-2}\Big)\phi+o_{\mathbb{P}}\big(1/n\big) = 1 − ζ ζ ​ σ 2 ​ ϕ ⊤ ​ Λ n , h − 1 ​ ϕ + o ℙ ​ ( 1 / n ) \displaystyle=\frac{1-\zeta}{\zeta}\sigma^{2}\phi^{\top}\Lambda_{n,h}^{-1}\phi+o_{\mathbb{P}}\big(1/n\big)

Finally, by the conditional strong law of large numbers, we have b h , K boot ( ϕ ) = std ( { ϕ ⊤ w ^ n , h ( k ) | 1 ≤ k ≤ K } ) → a.s. Var ∗ ​ ( ϕ ⊤ ​ w ^ n , h ( k ) ) → ℙ 1 − ζ ζ σ ϕ ⊤ ​ Λ n , h − 1 ​ ϕ . b^{\text{boot}}_{h,K}(\phi)=\text{std}\left(\big\{\phi^{\top}\widehat{w}_{n,h}^{(k)}\big|1\leq k\leq K\big\}\right)\to_{\text{a.s.}}\sqrt{\text{Var}^{*}(\phi^{\top}\widehat{w}_{n,h}^{(k)})}\xrightarrow{\mathbb{P}}\sqrt{\frac{1-\zeta}{\zeta}}\sigma\sqrt{\phi^{\top}\Lambda_{n,h}^{-1}\phi}. ∎

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
