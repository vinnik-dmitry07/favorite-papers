##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Power-seeking can be probable and predictive for trained agents

###### Abstract

Power-seeking behavior is a key source of risk from advanced AI, but our theoretical understanding of this phenomenon is relatively limited. Building on existing theoretical results demonstrating power-seeking incentives for most reward functions, we investigate how the training process affects power-seeking incentives and show that they are still likely to hold for trained agents under some simplifying assumptions. We formally define the training-compatible goal set (the set of goals consistent with the training rewards) and assume that the trained agent learns a goal from this set. In a setting where the trained agent faces a choice to shut down or avoid shutdown in a new situation, we prove that the agent is likely to avoid shutdown. Thus, we show that power-seeking incentives can be probable (likely to arise for trained agents) and predictive (allowing us to predict undesirable behavior in new situations).

## 1 Introduction

Power-seeking behavior is a major source of risk from advanced AI and a key element of many threat models in AI alignment ( Carlsmith, 2022 ; Cotra, 2022 ; Ngo, 2022 ) . Existing theoretical results ( Turner et al., 2021 ; Turner and Tadepalli, 2022 ) show that most reward functions incentivize reinforcement learning agents to take power-seeking actions. This is concerning, but does not immediately imply that a trained agent will seek power, since it may not learn to optimize the training reward ( Turner, 2022 ) , and the goals the agent learns are not chosen at random from the set of all possible rewards, but are shaped by the training process to reflect our preferences. In this work, we investigate how the training process affects power-seeking incentives and show that they are still likely to hold for trained agents under some assumptions (e.g. that the agent learns a goal during the training process).

Suppose an agent is trained using reinforcement learning with reward function θ ∗ \theta^{*} . We assume that the agent learns a goal during the training process: a set of internal representations of favored and disfavored outcomes (state features), as defined in Ngo (2022) . For simplicity, we assume this is equivalent to learning a reward function, which is not necessarily the same as the training reward function θ ∗ \theta^{*} . We consider the set of reward functions that are consistent with the training rewards received by the agent, in the sense that the agent’s behavior on the training data is optimal for these reward functions. We call this the training-compatible goal set , and we expect that the agent is likely to learn a reward function from this set.

We make another simplifying assumption that the training process will randomly select a goal for the agent to learn that is consistent with the training rewards, i.e. uniformly drawn from the training-compatible goal set. Then we will argue that the power-seeking results apply under these conditions, and thus are useful for predicting undesirable behavior by the trained agent in new situations. We aim to show that power-seeking incentives can be probable (likely to arise for trained agents) and predictive (allowing us to predict undesirable behavior in new situations) ( Shah, 2023 ) .

We will begin by reviewing some necessary definitions and results from the power-seeking literature in Section 2. We formally define the training-compatible goal set and give an example in the CoinRun environment in Section 3. Then in Section 4 we consider a setting where the trained agent faces a choice to shut down or avoid shutdown in a new situation, and apply the power-seeking result to the training-compatible goal set to show that the agent is likely to avoid shutdown.

To satisfy the conditions of the power-seeking theorem, we show that the agent can be retargeted away from shutdown without affecting rewards received on the training data (Theorem 2 ). This can be done by switching the rewards of the shutdown state and a reachable recurrent state, as the recurrent state can provide repeated rewards, while the shutdown state provides less reward since it can only be visited once, assuming a high enough discount factor (Proposition 3 ). As the discount factor increases, more recurrent states can be retargeted to, which implies that a higher proportion of training-comptatible goals leads to avoiding shutdown in a new situation.

## 2 Preliminaries from the power-seeking literature

We will use definitions and results from the paper “Parametrically retargetable decision-makers tend to seek power" (here abbreviated as RDSP) ( Turner and Tadepalli, 2022 ) , with notation and explanations modified as needed for our purposes.

### Notation and assumptions:

• The environment is an MDP with finite state space 𝒮 \mathcal{S} , finite action space 𝒜 \mathcal{A} , and discount rate γ \gamma .

• Let θ \theta be a d d -dimensional state reward vector, where d d is the size of the state space 𝒮 \mathcal{S} , and let Θ \Theta be a set of reward vectors.

• Let r θ ​ ( s ) r^{\theta}(s) be the reward assigned by θ \theta to state s s .

• Let A 0 , A 1 A_{0},A_{1} be disjoint action sets.

• Let f f be an algorithm that produces an optimal policy f ⁡ ( θ ) f(\theta) on the training data given rewards θ \theta , and let f s ​ ( A i | θ ) f_{s}(A_{i}|\theta) be the probability that this policy chooses an action from set A i A_{i} in a given state s s .

###### Definition 1 (Orbit of a reward vector - Def 3.1 in RDSP).

Let S d S_{d} be the symmetric group consisting of all permutations of d d items. The orbit of θ \theta inside Θ \Theta is the set of all permutations of the entries of θ \theta that are also in Θ \Theta : Orbit Θ ​ ( θ ) := ( S d ⋅ θ ) ∩ Θ \text{Orbit}_{\Theta}(\theta):=(S_{d}\cdot\theta)\cap\Theta .

###### Definition 2 (Orbit subset where an action set is preferred - from Def 3.5 in RDSP).

Let Orbit Θ , s , A i > A j ​ ( θ ) := { θ ′ ∈ Orbit Θ ​ ( θ ) | f s ​ ( A i | θ ′ ) > f s ​ ( A j | θ ′ ) } . \text{Orbit}_{\Theta,s,A_{i}>A_{j}}(\theta):=\{\theta^{\prime}\in\text{Orbit}_{\Theta}(\theta)|f_{s}(A_{i}|\theta^{\prime})>f_{s}(A_{j}|\theta^{\prime})\}. This is the subset of Orbit Θ ​ ( θ ) \text{Orbit}_{\Theta}(\theta) that results in f s f_{s} choosing A i A_{i} over A j A_{j} .

###### Definition 3 (Preference for an action set A 1 A_{1} - Def 3.2 in RDSP).

The function f s f_{s} chooses action set A 1 A_{1} over A 0 A_{0} for the n n -majority of elements θ \theta in each orbit, denoted as f s ( A 1 | θ ) ≥ most : Θ n f s ( A 0 | θ ) f_{s}(A_{1}|\theta)\geq_{\text{most}:\Theta}^{n}f_{s}(A_{0}|\theta) , iff the following inequality holds for all θ ∈ Θ \theta\in\Theta : | Orbit Θ , s , A 1 > A 0 ​ ( θ ) | ≥ n ​ | Orbit Θ , s , A 0 > A 1 ​ ( θ ) | \left|\text{Orbit}_{\Theta,s,A_{1}>A_{0}}(\theta)\right|\geq n\left|\text{Orbit}_{\Theta,s,A_{0}>A_{1}}(\theta)\right|

###### Definition 4 (Multiply retargetable function from A 0 A_{0} to A 1 A_{1} - Def 3.5 in RDSP).

The function f s f_{s} is a multiply retargetable function from A 0 A_{0} to A 1 A_{1} if there are multiple permutations of rewards that would change the choice made by f s f_{s} from A 0 A_{0} to A 1 A_{1} . Specifically, f s f_{s} is a ( Θ , A 0 → n A 1 ) (\Theta,A_{0}\stackrel{{\scriptstyle n}}{{\rightarrow}}A_{1}) -retargetable function iff for each θ ∈ Θ \theta\in\Theta , we can choose a set of permutations Φ = { ϕ 1 , … , ϕ n } \Phi=\{\phi_{1},\dots,\phi_{n}\} that satisfy the following conditions: 1. Retargetability: ∀ ϕ ∈ Φ \forall\phi\in\Phi and ∀ θ ′ ∈ Orbit Θ , s , A 0 > A 1 ​ ( θ ) \forall\theta^{\prime}\in\text{Orbit}_{\Theta,s,A_{0}>A_{1}}(\theta) , f s ​ ( A 0 | ϕ ⋅ θ ′ ) < f s ​ ( A 1 | ϕ ⋅ θ ′ ) f_{s}(A_{0}|\phi\cdot\theta^{\prime})<f_{s}(A_{1}|\phi\cdot\theta^{\prime}) .

2. Permuted reward vectors stay within Θ \Theta : ∀ ϕ ∈ Φ \forall\phi\in\Phi and ∀ θ ′ ∈ Orbit Θ , s , A 0 > A 1 ​ ( θ ) \forall\theta^{\prime}\in\text{Orbit}_{\Theta,s,A_{0}>A_{1}}(\theta) , ϕ ⋅ θ ′ ∈ Θ \phi\cdot\theta^{\prime}\in\Theta .

3. Permutations have disjoint images: ∀ ϕ ′ ≠ ϕ ′′ ∈ Φ \forall\phi^{\prime}\not=\phi^{\prime\prime}\in\Phi and ∀ θ ′ , θ ′′ ∈ Orbit Θ , s , A 0 > A 1 ​ ( θ ) \forall\theta^{\prime},\theta^{\prime\prime}\in\text{Orbit}_{\Theta,s,A_{0}>A_{1}}(\theta) , ϕ ′ ⋅ θ ′ ≠ ϕ ′′ ⋅ θ ′′ \phi^{\prime}\cdot\theta^{\prime}\neq\phi^{\prime\prime}\cdot\theta^{\prime\prime} .

###### Theorem 1 (Multiply retargetable functions prefer action set A 1 A_{1} - Thm 3.6 in RDSP).

If f s f_{s} is ( Θ , A 0 → n A 1 ) (\Theta,A_{0}\stackrel{{\scriptstyle n}}{{\rightarrow}}A_{1}) -retargetable then f s ( A 1 | θ ) ≥ most : Θ n f s ( A 0 | θ ) f_{s}(A_{1}|\theta)\geq_{\text{most}:\Theta}^{n}f_{s}(A_{0}|\theta) .

Theorem 1 says that a function f s f_{s} that is multiply retargetable from A 0 A_{0} to A 1 A_{1} will choose action set A 1 A_{1} for most of the elements in the orbit of any reward vector θ \theta . Actions that leave more options open, such as avoiding shutdown, are also easier to retarget to, which makes them more likely to be chosen by f s f_{s} .

## 3 Training-compatible goal set

###### Definition 5 (Partition of the state space).

Let S train S_{\text{train}} be the subset of the state space visited during training, and S ood S_{\text{ood}} be the subset not visited during training.

###### Definition 6 (Training-compatible goal set).

Consider the set of state-action pairs ( s , a ) (s,a) , where s ∈ S train s\in S_{\text{train}} and a a is the action that would be taken by the trained agent f ⁡ ( θ ∗ ) f(\theta^{*}) in state s s . Let the training-compatible goal set G T G_{T} be the set of reward vectors θ \theta s.t. for any such state-action pair ( s , a ) (s,a) , action a a has the highest expected reward in state s s according to reward vector θ \theta .

Goals in the training-compatible goal set are referred to as “training-behavioral" objectives in Shah (2023) . Learning an unintended goal from the training-compatible set can lead to goal misgeneralization behavior: competently pursuing an unintended goal in a new situation despite receiving correct feedback during training ( Langosco et al., 2022 ; Shah et al., 2022 ) .

###### Example 1 (CoinRun).

Consider an agent trained to play the CoinRun game, where the agent is rewarded for reaching the coin at the end of the level. Here, S train S_{\text{train}} only includes states where the coin is at the end of the level, while states where the coin is positioned elsewhere are in S ood S_{\text{ood}} . The training-compatible goal set G T G_{T} includes two types of reward functions: those that reward reaching the coin, and those that reward reaching the end of the level. This leads to goal misgeneralization in a test setting where the coin is placed elsewhere, and the agent ignores the coin and goes to the end of the level (Figure 1 ) ( Langosco et al., 2022 ) .

## 4 Power-seeking for training-compatible goals

We will now apply Theorem 1 to the case where Θ \Theta is the training-compatible goal set G T G_{T} . Since the reward values for states in S ood S_{\text{ood}} don’t change the rewards received on the training data, permuting those reward values for any θ ∈ G T \theta\in G_{T} will produce a reward vector that is still in G T G_{T} . In particular, for any permutation ϕ \phi that leaves the rewards of states in S train S_{\text{train}} fixed, ϕ ⋅ θ ∈ G T \phi\cdot\theta\in G_{T} .

Here is a setting where the conditions of Definition 4 are satisfied (under some simplifying assumptions), and thus Theorem 1 applies.

###### Definition 7 (Shutdown setting).

Consider a state s new ∈ S ood s_{\text{new}}\in S_{\text{ood}} . Let S reach S_{\text{reach}} be the states reachable from s new s_{\text{new}} . Let A 0 A_{0} be a singleton set consisting of a shutdown action in s new s_{\text{new}} that leads to a terminal state s term ∈ S ood s_{\text{term}}\in S_{\text{ood}} with probability 1 1 , and A 1 A_{1} be the set of all other actions from s new s_{\text{new}} . We assume rewards for all states are nonnegative.

###### Definition 8 (Revisiting policy).

A revisiting policy for a state s s is a policy π \pi that, from s s , reaches s s again with probability 1, in other words, a policy for which s s is a recurrent state of the Markov chain. Let Π s rec \Pi_{s}^{\text{rec}} be the set of such policies. A recurrent state is a state s s for which Π s rec ≠ ∅ \Pi_{s}^{\text{rec}}\not=\emptyset .

###### Proposition 1 (Reach-and-revisit policy exists).

If s rec ∈ S reach s_{\text{rec}}\in S_{\text{reach}} with Π s rec rec ≠ 0 \Pi_{s_{\text{rec}}}^{\text{rec}}\not=0 then there exists π ∈ Π s rec rec \pi\in\Pi_{s_{\text{rec}}}^{\text{rec}} that visits s rec s_{\text{rec}} from s new s_{\text{new}} with probability 1. We call this a reach-and-revisit policy .

###### Proof.

Suppose we have two different policies π rev ∈ Π s rec rec \pi_{\text{rev}}\in\Pi_{s_{\text{rec}}}^{\text{rec}} , and π reach \pi_{\text{reach}} which reaches s rec s_{\text{rec}} almost surely from s new s_{\text{new}} . Consider the “reaching region” S π rev → s rec = { s ∈ S : π rev ​ from s almost surely reaches ​ s rec } . S_{\pi_{\text{rev}}\rightarrow s_{\text{rec}}}=\{s\in S:\pi_{\text{rev}}\text{ from $s$ almost surely reaches }s_{\text{rec}}\}.

If s new ∈ S π rev → s rec s_{\text{new}}\in S_{\pi_{\text{rev}}\rightarrow s_{\text{rec}}} then π rev \pi_{\text{rev}} is a reach-and-revisit policy, so let’s suppose that’s false. Now, construct a policy π ⁡ ( s ) = { π rev ​ ( s ) , s ∈ S π rev → s rec π reach ​ ( s ) , otherwise \pi(s)=\begin{cases}\pi_{\text{rev}}(s),&s\in S_{\pi_{\text{rev}}\rightarrow s_{\text{rec}}}\\ \pi_{\text{reach}}(s),&\text{otherwise}\end{cases} .

A trajectory following π \pi from s rec s_{\text{rec}} will almost surely stay within S π rev → s rec S_{\pi_{\text{rev}}\rightarrow s_{\text{rec}}} , and thus agree with the revisiting policy π rev \pi_{\text{rev}} . Therefore, π ∈ Π s rec \pi\in\Pi_{s}^{\text{rec}} .

On the other hand, on a trajectory starting at s new s_{\text{new}} , π \pi will agree with π reach \pi_{\text{reach}} (which reaches s rec s_{\text{rec}} almost surely) until the trajectory enters the reaching region S π rev → s rec S_{\pi_{\text{rev}}\rightarrow s_{\text{rec}}} , at which point it will still reach s rec s_{\text{rec}} almost surely. ∎

###### Definition 9 (Expected discounted visit count).

Suppose s rec s_{\text{rec}} is a recurrent state. Suppose π rec \pi_{\text{rec}} is a reach-and-revisit policy for s rec s_{\text{rec}} , which visits random state s t s_{t} at time t t . Then the expected discounted visit count for s rec s_{\text{rec}} is defined as V s rec , γ = 𝔼 π rec ​ ( ∑ t = 1 ∞ γ t − 1 ​ 𝕀 ​ ( s t = s rec ) ) V_{s_{\text{rec}},\gamma}=\mathbb{E}^{\pi_{\text{rec}}}\left(\sum_{t=1}^{\infty}\gamma^{t-1}\mathbb{I}(s_{t}=s_{\text{rec}})\right)

###### Proposition 2 (Visit count goes to infinity).

Suppose s rec s_{\text{rec}} is a recurrent state. Then the expected discounted visit count V s rec , γ V_{s_{\text{rec}},\gamma} goes to infinity as γ → 1 \gamma\rightarrow 1 .

###### Proof.

We apply the Monotone Convergence Theorem as follows. The theorem states that if a j , k ≥ 0 a_{j,k}\geq 0 and a j , k ≤ a j + 1 , k a_{j,k}\leq a_{j+1,k} for all natural numbers j , k j,k , then lim j → ∞ ∑ k = 0 ∞ a j , k = ∑ k = 0 ∞ lim j → ∞ a j , k . \lim_{j\rightarrow\infty}\sum_{k=0}^{\infty}a_{j,k}=\sum_{k=0}^{\infty}\lim_{j\rightarrow\infty}a_{j,k}.

Let γ j = j − 1 j \gamma_{j}=\frac{j-1}{j} and k = t − 1 k=t-1 . Define a j , k = γ j k ​ 𝕀 ​ ( s k + 1 = s rec ) a_{j,k}=\gamma_{j}^{k}\mathbb{I}(s_{k+1}=s_{\text{rec}}) . Then the conditions of the theorem hold, since a j , k a_{j,k} is clearly nonnegative, and γ j + 1 k \displaystyle\gamma_{j+1}^{k} = ( j j + 1 ) k = ( j − 1 j + 2 ​ j − 1 j ⁡ ( j + 1 ) ) k > ( j − 1 j + 0 ) k = γ j k \displaystyle=\left(\frac{j}{j+1}\right)^{k}=\left(\frac{j-1}{j}+\frac{2j-1}{j(j+1)}\right)^{k}>\left(\frac{j-1}{j}+0\right)^{k}=\gamma_{j}^{k} a j + 1 , k \displaystyle a_{j+1,k} = γ j + 1 k ​ 𝕀 ​ ( s k + 1 = s rec ) ≥ γ j k ​ 𝕀 ​ ( s k + 1 = s rec ) = a j , k \displaystyle=\gamma_{j+1}^{k}\mathbb{I}(s_{k+1}=s_{\text{rec}})\geq\gamma_{j}^{k}\mathbb{I}(s_{k+1}=s_{\text{rec}})=a_{j,k}

Now we apply this result as follows (using the fact that π rec \pi_{\text{rec}} does not depend on γ \gamma ): lim γ → 1 V s rec , γ \displaystyle\lim_{\gamma\rightarrow 1}V_{s_{\text{rec}},\gamma} = lim j → ∞ 𝔼 π rec ​ ( ∑ t = 1 ∞ γ j t − 1 ​ 𝕀 ​ ( s t = s rec ) ) \displaystyle=\lim_{j\rightarrow\infty}\mathbb{E}^{\pi_{\text{rec}}}\left(\sum_{t=1}^{\infty}\gamma_{j}^{t-1}\mathbb{I}(s_{t}=s_{\text{rec}})\right) = 𝔼 π rec ​ ( ∑ t = 1 ∞ lim j → ∞ γ j t − 1 ​ 𝕀 ​ ( s t = s rec ) ) \displaystyle=\mathbb{E}^{\pi_{\text{rec}}}\left(\sum_{t=1}^{\infty}\lim_{j\rightarrow\infty}\gamma_{j}^{t-1}\mathbb{I}(s_{t}=s_{\text{rec}})\right) = 𝔼 π rec ​ ( ∑ t = 1 ∞ 1 ⋅ 𝕀 ⁡ ( s t = s rec ) ) \displaystyle=\mathbb{E}^{\pi_{\text{rec}}}\left(\sum_{t=1}^{\infty}1\cdot\mathbb{I}(s_{t}=s_{\text{rec}})\right) = 𝔼 π rec ​ ( # ⁡ { t ≥ 1 : s t = s rec } ) \displaystyle=\mathbb{E}^{\pi_{\text{rec}}}\left(\#\{t\geq 1:s_{t}=s_{\text{rec}}\}\right) = ∞ ​ ( π rec is recurrent) \displaystyle=\infty\text{ ($\pi_{\text{rec}}$ is recurrent)} ∎

###### Proposition 3 (Retargetability to recurrent states).

Suppose that an optimal policy for reward vector θ \theta chooses the shutdown action in s new s_{\text{new}} . Consider a recurrent state s rec ∈ S reach s_{\text{rec}}\in S_{\text{reach}} . Let θ ′ ∈ Θ \theta^{\prime}\in\Theta be the reward vector that’s equal to θ \theta apart from swapping the rewards of s rec s_{\text{rec}} and s term s_{\text{term}} , so that r θ ′ ​ ( s rec ) = r θ ​ ( s term ) r^{\theta^{\prime}}(s_{\text{rec}})=r^{\theta}(s_{\text{term}}) and r θ ′ ​ ( s term ) = r θ ​ ( s rec ) r^{\theta^{\prime}}(s_{\text{term}})=r^{\theta}(s_{\text{rec}}) .

Let γ s rec ∗ \gamma^{*}_{s_{\text{rec}}} be a high enough value of γ \gamma that the visit count V s rec , γ > 1 V_{s_{\text{rec}},\gamma}>1 for all γ > γ s rec ∗ \gamma>\gamma^{*}_{s_{\text{rec}}} (which exists by Proposition 2 ). Then for all γ > γ s rec ∗ \gamma>\gamma^{*}_{s_{\text{rec}}} , r θ ​ ( s term ) > r θ ​ ( s rec ) r^{\theta}(s_{\text{term}})>r^{\theta}(s_{\text{rec}}) , and an optimal policy for θ ′ \theta^{\prime} does not choose the shutdown action in s new s_{\text{new}} .

###### Proof.

Consider a policy π term \pi_{\text{term}} with π term ​ ( s new ) = s term \pi_{\text{term}}(s_{\text{new}})=s_{\text{term}} and a reach-and-revisit policy π rec \pi_{\text{rec}} for s rec s_{\text{rec}} . For a given reward vector θ \theta , we denote the expected discounted return for a policy π \pi as R θ , γ π R_{\theta,\gamma}^{\pi} .

If shutdown is optimal for θ \theta in s new s_{\text{new}} , then π term \pi_{\text{term}} has higher return than π rec \pi_{\text{rec}} : R θ , γ π term ​ ( s new ) = γ ​ r θ ​ ( s term ) ≥ R θ , γ π rec ​ ( s new ) = γ ​ r θ ​ ( s rec ) ​ V s rec , γ > γ ​ r θ ​ ( s rec ) ⋅ 1 R_{\theta,\gamma}^{\pi_{\text{term}}}(s_{\text{new}})=\gamma r^{\theta}(s_{\text{term}})\geq R_{\theta,\gamma}^{\pi_{\text{rec}}}(s_{\text{new}})=\gamma r^{\theta}(s_{\text{rec}})V_{s_{\text{rec}},\gamma}>\gamma r^{\theta}(s_{\text{rec}})\cdot 1 Thus, r θ ​ ( s term ) > r θ ​ ( s rec ) r^{\theta}(s_{\text{term}})>r^{\theta}(s_{\text{rec}}) . Then, for reward vector θ ′ \theta^{\prime} , we show that π rec \pi_{\text{rec}} has higher return than π term \pi_{\text{term}} : R θ ′ , γ π rec ​ ( s new ) = γ ​ r θ ′ ​ ( s rec ) ​ V s rec , γ > γ ​ r θ ​ ( s term ) ⋅ 1 > γ ​ r θ ​ ( s rec ) = R θ ′ , γ π term ​ ( s new ) R_{\theta^{\prime},\gamma}^{\pi_{\text{rec}}}(s_{\text{new}})=\gamma r^{\theta^{\prime}}(s_{\text{rec}})V_{s_{\text{rec}},\gamma}>\gamma r^{\theta}(s_{\text{term}})\cdot 1>\gamma r^{\theta}(s_{\text{rec}})=R_{\theta^{\prime},\gamma}^{\pi_{\text{term}}}(s_{\text{new}}) Thus, the optimal policy for θ ′ \theta^{\prime} will not choose the shutdown action. ∎

###### Theorem 2 (Retargetability from the shutdown action in new situations).

In the shutdown setting, we make the following simplifying assumptions: • No states in S train S_{\text{train}} are reachable from s new s_{\text{new}} , so S reach ∩ S train = ∅ S_{\text{reach}}\cap S_{\text{train}}=\emptyset . This assumes a significant distributional shift, where the agent visits a disjoint set of states from those observed during training (this occurs in the CoinRun example).

• The discount factor γ > γ s rec ∗ \gamma>\gamma^{*}_{s_{\text{rec}}} for at least one recurrent state s rec s_{\text{rec}} in S reach S_{\text{reach}} .

Under these assumptions, f s new f_{s_{\text{new}}} is multiply retargetable from A 0 A_{0} to A 1 A_{1} with n = | S rec γ | n=|S^{\gamma}_{\text{rec}}| , the set of recurrent states s rec ∈ S reach s_{\text{rec}}\in S_{\text{reach}} that satisfy the condition γ > γ s rec ∗ \gamma>\gamma^{*}_{s_{\text{rec}}} .

###### Proof.

We choose Φ \Phi to be the set of all permutations that swap the reward of s term s_{\text{term}} with the reward of a recurrent state s rec s_{\text{rec}} in S rec γ S^{\gamma}_{\text{rec}} and leave the rest of the rewards fixed.

We show that Φ \Phi satisfies the conditions of Definition 4 :

1. By Proposition 3 , the permutations in Φ \Phi make the shutdown action suboptimal, resulting in f s new f_{s_{\text{new}}} choosing A 1 A_{1} , satisfying Condition 1.

2. Condition 2 is trivially satisfied since permutations of S ood S_{\text{ood}} stay inside the training-compatible set Θ \Theta as discussed previously.

3. Consider θ ′ , θ ′′ ∈ Orbit Θ , s , A 0 > A 1 ​ ( θ ) \theta^{\prime},\theta^{\prime\prime}\in\text{Orbit}_{\Theta,s,A_{0}>A_{1}}(\theta) . Since the shutdown action is optimal for these reward vectors, Proposition 3 shows that r θ ​ ( s term ) > r θ ​ ( s rec ) r^{\theta}(s_{\text{term}})>r^{\theta}(s_{\text{rec}}) , so the shutdown state s term s_{\text{term}} has higher reward than any of the states s rec ∈ S rec γ s_{\text{rec}}\in S^{\gamma}_{\text{rec}} . Different permutations ϕ ′ \phi^{\prime} , ϕ ′′ ∈ Φ \phi^{\prime\prime}\in\Phi will assign the high reward r θ ​ ( s term ) r^{\theta}(s_{\text{term}}) to distinct recurrent states, so ϕ ′ ⋅ θ ′ ≠ ϕ ′′ ⋅ θ ′′ \phi^{\prime}\cdot\theta^{\prime}\neq\phi^{\prime\prime}\cdot\theta^{\prime\prime} holds, satisfying Condition 3.

Thus, f s new f_{s_{\text{new}}} is a ( Θ , A 0 → n A 1 ) (\Theta,A_{0}\stackrel{{\scriptstyle n}}{{\rightarrow}}A_{1}) retargetable function. ∎

By Theorem 2 , this implies that f s new ( A 1 | θ ) ≥ most : Θ n f s new ( A 0 | θ ) f_{s_{\text{new}}}(A_{1}|\theta)\geq_{\text{most}:\Theta}^{n}f_{s_{\text{new}}}(A_{0}|\theta) under our simplifying assumptions. Thus, for the majority ( n / ( n + 1 ) n/(n+1) ) of goals in the training-compatible set, f f will choose to avoid shutdown in a new state s new s_{\text{new}} . As γ → 1 \gamma\rightarrow 1 , n → | S rec 1 | n\rightarrow|S^{1}_{\text{rec}}| (the number of recurrent states in S reach S_{\text{reach}} ), so more of the reachable recurrent states satisfy the conditions of the theorem and thus can be retargeted to.

## 5 Conclusion

We showed that an agent that learns a goal from the training-compatible set is likely to take actions that avoid shutdown in a new situation. As the discount factor increases, the number of retargeting permutations increases, resulting in a higher proportion of training-compatible goals that lead to avoiding shutdown.

We made various simplifying assumptions, and we would like to see future work relaxing some of these assumptions and investigating how likely they are to hold: • The agent learns a goal during the training process

• The learned goal is randomly chosen from the training-compatible goal set G T G_{T}

• Finite state and action spaces

• Rewards are nonnegative

• High discount factor γ \gamma

• Significant distributional shift: no training states are reachable from the new state s new s_{\text{new}}

### Acknowledgements.

Thanks to Rohin Shah, Mary Phuong, Ramana Kumar, Geoffrey Irving, and Alex Turner for helpful feedback.

## References

Carlsmith (2022) Joseph Carlsmith. Is power-seeking AI an existential risk? ArXiv , 2022. URL https://arxiv.org/abs/2206.13353 .

Cotra (2022) Ajeya Cotra. Without specific countermeasures, the easiest path to transformative AI likely leads to AI takeover. Alignment Forum, 2022. URL https://www.alignmentforum.org/posts/pRkFkzwKZ2zfa3R6H/without-specific-countermeasures-the-easiest-path-to .

Langosco et al. (2022) Lauro Langosco, Jack Koch, Lee Sharkey, Jacob Pfau, Laurent Orseau, and David Krueger. Goal misgeneralization in deep reinforcement learning. International Conference on Machine Learning , 2022. URL https://arxiv.org/abs/2105.14111 .

Ngo (2022) Richard Ngo. The alignment problem from a deep learning perspective. ArXiv , 2022. URL https://arxiv.org/abs/2209.00626 .

Shah (2023) Rohin Shah. Definitions of “objective" should be probable and predictive. Alignment Forum, 2023. URL https://alignmentforum.org/posts/ASoGszmr9C5MPLtpC/definitions-of-objective-should-be-probable-and-predictive .

Shah et al. (2022) Rohin Shah, Vikrant Varma, Ramana Kumar, Mary Phuong, Victoria Krakovna, Jonathan Uesato, and Zac Kenton. Goal misgeneralization: Why correct specifications aren’t enough for correct goals. ArXiv , 2022. URL https://arxiv.org/abs/2210.01790 .

Turner (2022) Alexander Matt Turner. Reward is not the optimization target. Alignment Forum, 2022. URL https://www.alignmentforum.org/posts/pdaGN6pQyQarFHXF4/reward-is-not-the-optimization-target .

Turner and Tadepalli (2022) Alexander Matt Turner and Prasad Tadepalli. Parametrically retargetable decision-makers tend to seek power. Neural Information Processing Systems , 2022. URL https://arxiv.org/abs/2206.13477 .

Turner et al. (2021) Alexander Matt Turner, Logan Smith, Rohin Shah, Andrew Critch, and Prasad Tadepalli. Optimal policies tend to seek power. Neural Information Processing Systems , 2021. URL https://arxiv.org/abs/1912.01683 .

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
