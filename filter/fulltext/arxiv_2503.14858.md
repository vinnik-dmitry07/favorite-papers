##### Report GitHub Issue

Content selection saved. Describe the issue below:

# 1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities

###### Abstract

Scaling up self-supervised learning has driven breakthroughs in language and vision, yet comparable progress has remained elusive in reinforcement learning (RL). In this paper, we study building blocks for self-supervised RL that unlock substantial improvements in scalability, with network depth serving as a critical factor. Whereas most RL papers in recent years have relied on shallow architectures (around 2 – 5 layers), we demonstrate that increasing the depth up to 1024 layers can significantly boost performance. Our experiments are conducted in an unsupervised goal-conditioned setting, where no demonstrations or rewards are provided, so an agent must explore (from scratch) and learn how to maximize the likelihood of reaching commanded goals. Evaluated on simulated locomotion and manipulation tasks, our approach increases performance on the self-supervised contrastive RL algorithm by 2 × 2\times – 50 × 50\times , outperforming other goal-conditioned baselines. Increasing the model depth not only increases success rates but also qualitatively changes the behaviors learned. The project webpage and code can be found here: https://wang-kevin3290.github.io/scaling-crl/ .

## 1 Introduction

While scaling model size has been an effective recipe in many areas of machine learning, its role and impact in reinforcement learning (RL) remain unclear. The typical model size for state-based RL tasks is between 2 to 5 layers ( Raffin et al., 2021 ; Huang et al., 2022 ) . In contrast, it is not uncommon to use very deep networks in other domain areas; Llama 3 ( Dubey et al., 2024 ) and Stable Diffusion 3 ( Esser et al., 2024 ) have hundreds of layers. In fields such as vision ( Radford et al., 2021 ; Zhai et al., 2021 ; Dehghani et al., 2023 ) and language ( Srivastava et al., 2023 ) , models often only acquire the ability to solve certain tasks once they are larger than a critical scale. In the RL setting, many researchers have searched for similar emergent phenomena ( Srivastava et al., 2023 ) , but these papers typically report only small marginal benefits and typically only on tasks where small models already achieve some degree of success ( Nauman et al., 2024b ; Lee et al., 2024 ; Farebrother et al., 2024 ) . A key open question in RL today is whether it is possible to achieve similar jumps in performance by scaling RL networks.

At first glance, it makes sense why training very large RL networks should be difficult: the RL problem provides very few bits of feedback (e.g., only a sparse reward after a long sequence of observations), so the ratio of feedback to parameters is very small. The conventional wisdom ( LeCun, 2016 ) , reflected in many recent models ( Radford, 2018 ; Chen et al., 2020 ; Goyal et al., 2019 ) , has been that large AI systems must be trained primarily in a self-supervised fashion and that RL should only be used to finetune these models. Indeed, many of the recent breakthroughs in other fields have been primarily achieved with self-supervised methods, whether in computer vision ( Caron et al., 2021 ; Radford et al., 2021 ; Liu et al., 2024 ) , NLP ( Srivastava et al., 2023 ) , or multimodal learning ( Zong et al., 2024 ) . Thus, if we hope to scale reinforcement learning methods, self-supervision will likely be a key ingredient.

In this paper, we will study building blocks for scaling reinforcement learning. Our first step is to rethink the conventional wisdom above: “reinforcement learning” and “self-supervised learning” are not diametric learning rules, but rather can be married together into self-supervised RL systems that explore and learn policies without reference to a reward function or demonstrations ( Eysenbach et al., 2021 ; Eysenbach et al., 2022 ; Lee et al., 2022 ) . In this work, we use one of the simplest self-supervised RL algorithms, contrastive RL (CRL) ( Eysenbach et al., 2022 ) . The second step is to recognize the importance of increasing data availability. We will do this by building on recent GPU-accelerated RL frameworks ( Makoviychuk et al., 2021 ; Rutherford et al., 2023 ; Rudin et al., 2022 ; Bortkiewicz et al., 2024 ) . The third step is to increase network depth, using networks that are up to 100 × 100\times deeper than those typically found in prior work. Stabilizing the training of such networks will require incorporating architectural techniques from prior work, including residual connections ( He et al., 2015 ) , layer normalization ( Ba et al., 2016 ) , and Swish activation ( Ramachandran et al., 2018 ) . Our experiments will also study the relative importance of batch size and network width.

The primary contribution of this work is to show that a method that integrates these building blocks into a single RL approach exhibits strong scalability:

• Empirical Scalability: We observe a significant performance increase, more than 20 × 20\times in half of the environments and outperforming other standard goal-conditioned baselines. These performance gains correspond to qualitatively distinct policies that emerge as the scale increases.

• Scaling Depth in Network Architecture: While many prior RL works have primarily focused on increasing network width, they often report limited or even negative returns when expanding depth ( Lee et al., 2024 ; Nauman et al., 2024b ) . In contrast, our approach unlocks the ability to scale along the axis of depth, yielding performance improvements that surpass those from scaling width alone (see Sec. 4 ).

• Empirical Analysis : We conduct an extensive analysis of the key components in our scaling approach, uncovering critical factors and offering new insights.

We anticipate that future research may build on this foundation by uncovering additional building blocks.

## 2 Related Work

Natural Language Processing (NLP) and Computer Vision (CV) have recently converged in adopting similar architectures (i.e. transformers) and shared learning paradigms (i.e self-supervised learning), which together have enabled transformative capabilities of large-scale models ( Vaswani et al., 2017 ; Srivastava et al., 2023 ; Zhai et al., 2021 ; Dehghani et al., 2023 ; Wei et al., 2022 ) . In contrast, achieving similar advancements in reinforcement learning (RL) remains challenging. Several studies have explored the obstacles to scaling large RL models, including parameter underutilization ( Obando-Ceron et al., 2024 ) , plasticity and capacity loss ( Lyle et al., 2024 ; Lyle et al., 2022 ) , data sparsity ( Andrychowicz et al., 2017 ; LeCun, 2016 ) , and training instabilities ( Ota et al., 2021 ; Henderson et al., 2018 ; Van Hasselt et al., 2018 ; Nauman et al., 2024a ) . As a result, current efforts to scale RL models are largely restricted to specific problem domains, such as imitation learning ( Tuyls et al., 2024 ) , multi-agent games ( Neumann and Gros, 2022 ) , language-guided RL ( Driess et al., 2023 ; Ahn et al., 2022 ) , and discrete action spaces ( Obando-Ceron et al., 2024 ; Schwarzer et al., 2023 ) .

Recent approaches suggest several promising directions, including new architectural paradigms ( Obando-Ceron et al., 2024 ) , distributed training approaches ( Ota et al., 2021 ; Espeholt et al., 2018 ) , distributional RL ( Kumar et al., 2023 ) , and distillation ( Team et al., 2023 ) . Compared to these approaches, our method makes a simple extension to an existing self-supervised RL algorithm. The most recent works in this vein include Lee et al. (2024) and Nauman et al. (2024b) , which leverage residual connections to facilitate the training of wider networks. These efforts primarily focus on network width, noting limited gains from additional depth, thus both works use architectures with only four MLP layers. In our method, we find that scaling width indeed improves performance ( Section 4.4 ); however, our approach also enables scaling along depth, proving to be more powerful than width alone.

One notable effort to train deeper networks is described by Farebrother et al. (2024) , who cast value-based RL into a classification problem by discretizing the TD objective into a categorical cross-entropy loss. This approach draws on the conjecture that classification-based methods can be more robust and stable and thus may exhibit better scaling properties than their regressive counterparts ( Torgo and Gama, 1996 ; Farebrother et al., 2024 ) . The CRL algorithm that we use effectively uses a cross-entropy loss as well ( Eysenbach et al., 2022 ) . Its InfoNCE objective is a generalization of the cross-entropy loss, thereby performing RL tasks by effectively classifying whether current states and actions belong to the same or different trajectory that leads toward a goal state. In this vein, our work serves as a second piece of evidence that classification, much like cross-entropy’s role in the scaling success in NLP, could be a potential building block in RL.

## 3 Preliminaries

This section introduces notation and definitions for goal-conditioned RL and contrastive RL. Our focus is on online RL, where a replay buffer stores the most recent trajectories, and the critic is trained in a self-supervised manner.

#### Goal-Conditioned Reinforcement Learning

We define a goal-conditioned MDP as tuple ℳ g = ( 𝒮 , 𝒜 , p 0 , p , p g , r g , γ ) \mathcal{M}_{g}=(\mathcal{S},\mathcal{A},p_{0},p,p_{g},r_{g},\gamma) , where the agent interacts with the environment to reach arbitrary goals ( Kaelbling, 1993 ; Andrychowicz et al., 2017 ; Blier et al., 2021 ) . At every time step t t , the agent observes state s t ∈ 𝒮 s_{t}\in\mathcal{S} and performs a corresponding action a t ∈ 𝒜 a_{t}\in\mathcal{A} . The agent starts interaction in states sampled from p 0 ​ ( s 0 ) p_{0}(s_{0}) , and the interaction dynamics are defined by the transition probability distribution p ⁡ ( s t + 1 ∣ s t , a t ) p(s_{t+1}\mid s_{t},a_{t}) . Goals g ∈ 𝒢 g\in\mathcal{G} are defined in a goal space 𝒢 \mathcal{G} , which is related to 𝒮 \mathcal{S} via a mapping f : 𝒮 → 𝒢 f:\mathcal{S}\to\mathcal{G} . For example, 𝒢 \mathcal{G} may correspond to a subset of state dimensions. The prior distribution over goals is defined by p g ​ ( g ) p_{g}(g) . The reward function is defined as the probability density of reaching the goal in the next time step r g ​ ( s t , a t ) ≜ ( 1 − γ ) ​ p ​ ( s t + 1 = g ∣ s t , a t ) r_{g}(s_{t},a_{t})\triangleq(1-\gamma)p(s_{t+1}=g\mid s_{t},a_{t}) , with discount factor γ \gamma .

In this setting, the goal-conditioned policy π ⁡ ( a ∣ s , g ) \pi(a\mid s,g) receives both the current observation of the environment as well as a goal. We define the discounted state visitation distribution as p γ π ( ⋅ ∣ ⋅ , g ) ( s ) ≜ ( 1 − γ ) ∑ t = 0 ∞ γ t p t π ( ⋅ ∣ ⋅ , g ) ( s ) p^{\pi\left(\cdot\mid\cdot,g\right)}_{\gamma}(s)\triangleq(1-\gamma)\sum_{t=0}^{\infty}\gamma^{t}p^{\pi\left(\cdot\mid\cdot,g\right)}_{t}(s) , where p t π ​ ( s ) p_{t}^{\pi}(s) is the probability that policy π \pi visits s s after exactly t t steps, when conditioned with g g . This last expression is precisely the Q Q -function of the policy π ( ⋅ ∣ ⋅ , g ) \pi(\cdot\mid\cdot,g) for the reward r g r_{g} : Q g π ( s , a ) ≜ p γ π ( ⋅ ∣ ⋅ , g ) ( g ∣ s , a ) Q^{\pi}_{g}(s,a)\triangleq p^{\pi\left(\cdot\mid\cdot,g\right)}_{\gamma}(g\mid s,a) . The objective is to maximize the expected reward: max π 𝔼 p 0 ( s 0 ) , p g ( g ) , π ( ⋅ ∣ ⋅ , g ) [ ∑ t = 0 ∞ γ t r g ( s t , a t ) ] . \max_{\pi}\mathbb{E}_{p_{0}(s_{0}),p_{g}\left(g\right),\pi\left(\cdot\mid\cdot,g\right)}\left[\sum_{t=0}^{\infty}\gamma^{t}r_{g}\left(s_{t},a_{t}\right)\right]. (1)

#### Contrastive Reinforcement Learning.

Our experiments will use the contrastive RL algorithm ( Eysenbach et al., 2022 ) to solve goal-conditioned problems. Contrastive RL is an actor-critic method; we will use f ϕ , ψ ​ ( s , a , g ) f_{\phi,\psi}(s,a,g) to denote the critic and π θ ​ ( a ∣ s , g ) \pi_{\theta}(a\mid s,g) to denote the policy. The critic is parametrized with two neural networks that return state, action pair embedding ϕ ⁡ ( s , a ) \phi(s,a) and goal embedding ψ ⁡ ( g ) \psi(g) . The critic’s output is defined as the l 2 l^{2} -norm between these embeddings: f ϕ , ψ ​ ( s , a , g ) = ‖ ϕ ⁡ ( s , a ) − ψ ⁡ ( g ) ‖ 2 f_{\phi,\psi}(s,a,g)=\|\phi(s,a)-\psi(g)\|_{2} . The critic is trained with the InfoNCE objective ( Sohn, 2016 ) as in previous works ( Eysenbach et al., 2022 ; Eysenbach et al., 2021 ; Zheng et al., 2023 ; Zheng et al., 2024 ; Myers et al., 2024 ; Bortkiewicz et al., 2024 ) . Training is conducted on batches ℬ \mathcal{B} , where s i , a i , g i {\color[rgb]{0,0.55,0}s_{i},a_{i},g_{i}} represent the state, action, and goal (future state) sampled from the same trajectory, while g j {\color[rgb]{0.75,0,0}g_{j}} represents a goal sampled from a different, random trajectory. The objective function is defined as: min ϕ , ψ 𝔼 ℬ [ − ∑ i = 1 | ℬ | log ( e f ϕ , ψ ​ ( s i , a i , g i ) ∑ j = 1 K e f ϕ , ψ ​ ( s i , a i , g j ) ) ] . \min_{\phi,\psi}\mathbb{E}_{\mathcal{B}}\left[-\sum\nolimits_{{\color[rgb]{0,0.55,0}i=1}}^{|\mathcal{B}|}\log\biggl({\frac{e^{f_{\phi,\psi}({\color[rgb]{0,0.55,0}s_{i}},{\color[rgb]{0,0.55,0}a_{i}},{\color[rgb]{0,0.55,0}g_{i}})}}{\sum\nolimits_{{\color[rgb]{0.75,0,0}j=1}}^{K}e^{f_{\phi,\psi}({\color[rgb]{0,0.55,0}s_{i}},{\color[rgb]{0,0.55,0}a_{i}},{\color[rgb]{0.75,0,0}g_{j}})}}}\biggr)\right].

The policy π θ ​ ( a ∣ s , g ) \pi_{\theta}(a\mid s,g) is trained to maximize the critic: max π θ ⁡ 𝔼 p 0 ​ ( s 0 ) , p ⁡ ( s t + 1 ∣ s t , a t ) , p g ​ ( g ) , π θ ​ ( a ∣ s , g ) ​ [ f ϕ , ψ ​ ( s , a , g ) ] . \max_{\pi_{\theta}}\mathbb{E}_{\begin{subarray}{c}p_{0}(s_{0}),p(s_{t+1}\mid s_{t},a_{t}),\\ p_{g}\left(g\right),\pi_{\theta}(a\mid s,g)\end{subarray}}\left[f_{\phi,\psi}(s,a,g)\right].

#### Residual Connections

We incorporate residual connections ( He et al., 2015 ) into our architecture, following their successful use in RL ( Farebrother et al., 2024 ; Lee et al., 2024 ; Nauman et al., 2024b ) . A residual block transforms a given representation 𝐡 i \mathbf{h}_{i} by adding a learned residual function F i ​ ( 𝐡 i ) F_{i}(\mathbf{h}_{i}) to the original representation. Mathematically, this is expressed as: 𝐡 i + 1 = 𝐡 i + F i ​ ( 𝐡 i ) \mathbf{h}_{i+1}=\mathbf{h}_{i}+F_{i}\left(\mathbf{h}_{i}\right) where 𝐡 i + 1 \mathbf{h}_{i+1} is the output representation, 𝐡 i \mathbf{h}_{i} is the input representation, and F i ​ ( 𝐡 i ) F_{i}(\mathbf{h}_{i}) is a transformation learned through the network (e.g., using one or more layers). The addition ensures that the network learns modifications to the input rather than entirely new transformations, helping to preserve useful features from earlier layers. Residual connections improve gradient propagation by introducing shortcut paths ( He et al., 2016 ; Veit et al., 2016 ) , enabling more effective training of deep models.

## 4 Experiments

### 4.1 Experimental Setup

#### Environments.

All RL experiments use the JaxGCRL codebase ( Bortkiewicz et al., 2024 ) , which facilitates fast online GCRL experiments based on Brax ( Freeman et al., 2021 ) and MJX ( Todorov et al., 2012 ) environments. The specific environments used are a range of locomotion, navigation, and robotic manipulation tasks, for details see Appendix B . We use a sparse reward setting, with r = 1 r=1 only when the agent is in the goal proximity. For evaluation, we measure the number of time steps (out of 1000) that the agent is near the goal. When reporting an algorithm’s performance as a single number, we compute the average score over the last five epochs of training.

#### Architectural Components

We employ residual connections from the ResNet architecture ( He et al., 2015 ) , with each residual block consisting of four repeated units of a Dense layer, a Layer Normalization ( Ba et al., 2016 ) layer, and Swish activation ( Ramachandran et al., 2018 ) . We apply the residual connections immediately following the final activation of the residual block, as shown in Figure 2 . In this paper, we define the depth of the network as the total number of Dense layers across all residual blocks in the architecture. In all experiments, the depth refers to the configuration of the actor network and both critic encoder networks, which are scaled jointly, except for the ablation experiment in Section 4.4 .

### 4.2 Scaling Depth in Contrastive RL

We start by studying how increasing network depth can increase performance. Both the JaxGCRL benchmark and relevant prior work ( Lee et al., 2024 ; Nauman et al., 2024b ; Zheng et al., 2024 ) use MLPs with a depth of 4, and as such we adopt it as our baseline. In contrast, we will study networks of depth 8, 16, 32, and 64. The results in Figure 1 demonstrate that deeper networks achieve significant performance improvements across a diverse range of locomotion, navigation, and manipulation tasks. Compared to the 4-layer models typical in prior work, deeper networks achieve 2 − 5 × 2-5\times gains in robotic manipulation tasks, over 20 × 20\times gains in long-horizon maze tasks such as Ant U4-Maze and Ant U5-Maze, and over 50 × 50\times gains in humanoid-based tasks. The full table of performance increases up to depth 64 is provided in Table 1 .

In Figure 12 , we present results the same 10 environments, but compared against SAC, SAC+HER, TD3+HER, GCBC, and GCSL. Scaling CRL leads to substantial performance improvements, outperforming all other baselines in 8 out of 10 tasks. The only exception is SAC on the Humanoid Maze environments, where it exhibits greater sample efficiency early on; however, scaled CRL eventually reaches comparable performance. These results highlight that scaling the depth of the CRL algorithm enables state-of-the-art performance in goal-conditioned reinforcement learning.

### 4.3 Emergent Policies Through Depth

A closer examination of the results from the performance curves in Figure 1 reveals a notable pattern: instead of a gradual improvement in performance as depth increases, there are pronounced jumps that occur once a critical depth threshold is reached (also shown in Figure 6 ). The critical depths vary by environment, ranging from 8 layers (e.g. Ant Big Maze) to 64 layers in the Humanoid U-Maze task, with further jumps occurring even at depths of 1024 layers (see the Testing Limits section, Section 4.4 ).

Prompted by this observation, we visualized the learned policies at various depths and found qualitatively distinct skills and behaviors exhibited. This is particularly pronounced in the humanoid-based tasks, as illustrated in Figure 3 . Networks with a depth of 4 exhibit rudimentary policies where the agent either falls or throws itself toward the target. Only at a critical depth of 16 does the agent develop the ability to walk upright into the goal. In the Humanoid U-Maze environment, networks of depth 64 struggle to navigate around the intermediary wall, collapsing on the ground. Remarkably at a depth of 256, the agent learns unique behaviors on Humanoid U-Maze. These behaviors include folding forward into a leveraged position to propel itself over walls and shifting into a seated posture over the intermediary obstacle to worm its way toward the goal (one of these policies is illustrated in the fourth row of Figure 3 ). To the best of our knowledge, this is the first goal-conditioned approach to document such behaviors on the humanoid environment.

### 4.4 What Matters for CRL Scaling

#### Width vs. Depth

Past literature has shown that scaling network width can be effective ( Lee et al., 2024 ; Nauman et al., 2024b ) . In Figure 4 , we find that scaling width is also helpful in our experiments: wider networks consistently outperform narrower networks (depth held constant at 4). However, depth seems to be a more effective axis for scaling: simply doubling the depth to 8 (width held constant at 256) outperforms the widest networks in all three environments. The advantage of depth scaling is most pronounced in the Humanoid environment (observation dimension 268), followed by Ant Big Maze (dimension 29) and Arm Push Easy (dimension 17), suggesting that the comparative benefit may increase with higher observation dimensionality.

Note additionally that the parameter count scales linearly with width but quadratically with depth. For comparison, a network with 4 MLP layers and 2048 hidden units has roughly 35M parameters, while one with a depth of 32 and 256 hidden units has only around 2M. Therefore, when operating under a fixed FLOP compute budget or specific memory constraints, depth scaling may be a more computationally efficient approach to improving network performance.

#### Scaling the Actor vs. Critic Networks

To investigate the role of scaling in the actor and critic networks, Figure 6 presents the final performance for various combinations of actor and critic depths across three environments. Prior work ( Nauman et al., 2024b ; Lee et al., 2024 ) focuses on scaling the critic network, finding that scaling the actor degrades performance. In contrast, while we do find that scaling the critic is more impactful in two of the three environments (Humanoid, Arm Push Easy), our method benefits from scaling the actor network jointly, with one environment (Ant Big Maze) demonstrating actor scaling to be more impactful. Thus, our method suggests that scaling both the actor and critic networks can play a complementary role in enhancing performance.

#### Deep Networks Unlock Batch Size Scaling

Scaling batch size has been well-established in other areas of machine learning ( Chen et al., 2022 ; Zhang et al., 2024 ) . However, this approach has not translated as effectively to reinforcement learning (RL), and prior work has even reported negative impacts on value-based RL ( Obando-Ceron et al., 2023 ) . Indeed, in our experiments, simply increasing the batch size for the original CRL networks yields only marginal differences in performance ( Figure 7 , top left).

At first glance, this might seem counterintuitive: since reinforcement learning typically involves fewer informational bits per piece of training data ( LeCun, 2016 ) , one might expect higher variance in batch loss or gradients, suggesting the need for larger batch sizes to compensate. At the same time, this possibility hinges on whether the model in question can actually make use of a bigger batch size—in domains of ML where scaling has been successful, larger batch sizes usually bring the most benefit when coupled with sufficiently large models ( Zhang et al., 2024 ; Chen et al., 2022 ) . One hypothesis is that the small models traditionally used in RL may obscure the underlying benefits of larger batch size.

To test this hypothesis, we study the effect of increasing the batch size for networks of varying depths. As shown in Figure 7 , scaling the batch size becomes effective as network depth grows. This finding offers evidence that by scaling network capacity, we may simultaneously unlock the benefits of larger batch size, potentially making it an important component in the broader pursuit of scaling self-supervised RL.

#### Training Contrastive RL with 1000+ Layers

We next study whether further increasing depth beyond 64 layers further improves performance. We use the Humanoid maze tasks as these are both the most challenging environments in the benchmark and also seem to benefit from the deepest scaling. The results, shown in Figure 12 , indicate that performance continues to substantially improve as network depth reaches 256 and 1024 layers in the Humanoid U-Maze environment. While we were unable to scale beyond 1024 layers due to computational constraints, we expect to see continued improvements with even greater depths, especially on the most challenging tasks.

### 4.5 Why Scaling Happens

#### Depth Enhances Contrastive Representations

The long-horizon setting has been a long-standing challenge in RL particularly in unsupervised goal-conditioned settings where there is no auxiliary reward feedback ( Gupta et al., 2019 ) . The family of U-Maze environments requires a global understanding of the maze layout for effective navigation. We consider a variant of the Ant U-Maze environment, the U4-maze, in which the agent must initially move in the direction opposite the goal to loop around and ultimately reach it. As shown in Figure 9 , we observe a qualitative difference in the behavior of the shallow network (depth 4) compared to the deep network (depth 64). The visualized Q-values computed from the critic encoder representations reveal that the depth 4 network seemingly relies on Euclidean distance to the goal as a proxy for the Q value, even when a wall obstructs the direct path. In contrast, the depth 64 critic network learns richer representations, enabling it to effectively capture the topology of the maze as visualized by the trail of high Q values along the inner edge. These findings suggest that increasing network depth leads to richer learned representations, enabling deeper networks to better capture environment topology and achieve more comprehensive state-space coverage in a self-supervised manner.

#### Depth Enhances Exploration and Expressivity in a Synergized Way

Our earlier results suggested that deeper networks achieve greater state-action coverage. To better understand why scaling works, we sought to determine to whether improved data alone explains the benefits of scaling, or whether it acts in conjunction with other factors. Thus, we designed an experiment in Figure 8 in which we train three networks in parallel: one network, the “collector," interacts with the environment and writes all experience to a shared replay buffer. Alongside it, two additional "learners", one deep and one shallow, train concurrently. Crucially, these two learners never collect their own data; they train only from the collector’s buffer. This design holds the data distribution constant while varying the model’s capacity, so any performance gap between the deep and shallow learners must come from expressivity rather than exploration. When the collector is deep (e.g., depth 32), across all three environments the deep learner substantially outperforms the shallow one across all three environments, indicating that the expressivity of the deep networks is critical. On the other hand, we repeat the experiment with shallow collectors (e.g., depth 4), which explores less effectively and therefore populates the buffer with low-coverage experience. Here, both the deep and shallow learners struggle and achieve similarly poor performance, which indicates that the deep network’s additional capacity does not overcome the limitations of insufficient data coverage. As such, scaling depth enhances exploration and expressivity in a synergized way: stronger learning capacity drives more extensive exploration, and strong data coverage is essential to fully realize the power of stronger learning capacity. Both aspects jointly contribute to improved performance.

#### Deep Networks Learn to Allocate Greater Representational Capacity to States Near the Goal

In Figure 10 we take a successful trajectory in the Humanoid environment and visualize the embeddings of state-action encoder along this trajectory for both deep vs. shallow networks. While the shallow network (Depth 4) tends to cluster near-goal states tightly together, the deep network produces more "spread out" representations. This distinction is important: in a self-supervised setting, we want our representations to separate states that matter—particularly future or goal-relevant states—from random ones. As such, we want to allocate more representational capacity to such critical regions. This suggests that deep networks may learn to allocate representational capacity more effectively to state regions that matter most for the downstream task.

#### Deeper Networks Enable Partial Experience Stitching

Another key challenge in reinforcement learning is learning policies that can generalize to tasks unseen during training. To evaluate this setting, we designed a modified version of the Ant U-Maze environment. As shown in Figure 11 (top right), the original JaxGCRL benchmark assesses the agent’s performance on the three farthest goal positions located on the opposite side of the wall. However, instead of training on all possible subgoals (a superset of the evaluation state-goal pairs), we modified the setup to train on start-goal pairs that are at most 3 units apart, ensuring that none of the evaluation pairs ever appear in the training set. Figure 11 demonstrates that depth 4 networks show limited generalization, solving only the easiest goal (4 units away from the start). Depth 16 networks achieve moderate success, while depth 64 networks excel, sometimes solving the most challenging goal position. These results suggest that the increasing network depth results in some degree of stitching, combining ≤ \leq 3-unit pairs to navigate the 6-unit span of the U-Maze.

#### The (CRL) Algorithm is Key

In Appendix A , we show that scaled CRL outperforms other baseline goal-conditioned algorithms and advance the SOTA for goal-conditioned RL. We observe that for temporal difference methods (SAC, SAC+HER, TD3+HER), the performance saturates for networks of depth 4, and there is either zero or negative performance gains from deeper networks. This is in line with previous research showing that these methods benefit mainly from width ( Lee et al., 2024 ; Nauman et al., 2024b ) . These results suggest that the self-supervised CRL algorithm is critical.

We also experiment with scaling more self-supervised algorithms, namely Goal-Conditioned Behavioral Cloning (GCBC) and Goal-Conditioned Supervised Learning (GCSL). While these methods yield zero success in certain environments, they show some utility in arm manipulation tasks. Interestingly, even a very simple self-supervised algorithm like GCBC benefits from increased depth. This points to a promising direction for future work of further investigating other self-supervised methods to uncover potentially different or complementary recipes for scaling self-supervised RL.

Finally, recent work has augmented goal-conditioned RL with quasimetric architectures, leveraging the fact that temporal distances satisfy a triangle inequality–based invariance. In Appendix A , we also investigate whether the depth scaling effect persists when applied to these quasimetric networks.

### 4.6 Does Depth Scaling Improve Offline Contrastive RL?

In preliminary experiments, we evaluated depth scaling in the offline goal-conditioned setting using OGBench ( Park et al., 2024 ) . We found little evidence that increasing the network depth of CRL improves performance in this offline setting. To further investigate this, we conducted ablations: (1) scaling critic depth while holding the actor at 4 or 8 layers, and (2) applying cold initialization to the final layers of the critic encoders ( Zheng et al., 2024 ) . In all cases, baseline depth 4 networks often had the highest success. A key direction for future work is to see if our method can be adapted to enable scaling in the offline setting.

## 5 Conclusion

Arguably, much of the success of vision and language models today is due to the emergent capabilities they exhibit from scale ( Srivastava et al., 2023 ) , leading to many systems reducing the RL problem to a vision or language problem. A critical question for large AI models is: where does the data come from? Unlike supervised learning paradigms, RL methods inherently address this by jointly optimizing both the model and the data collection process through exploration. Ultimately, determining effective ways of building RL systems that demonstrate emergent capabilities may be important for transforming the field into one that trains its own large models. We believe that our work is a step towards these systems. By integrating key components for scaling up RL into a single approach, we show that model performance consistently improves as scale increases in complex tasks. In addition, deep models exhibit qualitatively better behaviors which might be interpreted as implicitly acquired skills necessary to reach the goal.

#### Limitations.

The primary limitations of our results are that scaling network depth comes at the cost of compute. An important direction for future work is to study how distributed training might be used to leverage even more compute, and how techniques such as pruning and distillation might be used to decrease the computational costs.

#### Impact Statement

This paper presents work whose goal is to advance the field of Machine Learning. There are many potential societal consequences of our work, none which we feel must be specifically highlighted here.

#### Acknowledgments.

We gratefully acknowledge Nathaniel Chen, Galen Collier, and the full staff of Princeton Research Computing for their invaluable assistance. We also thank Colin Lu for his discussions and contributions to this work. This research was also partially supported by the National Science Centre, Poland (grant no. 2023/51/D/ST6/01609); the Princeton Laboratory for Artificial Intelligence under Award 2025-97; and the Warsaw University of Technology through the Excellence Initiative: Research University (IDUB) program. Finally, we would also like to thank Jens Tuyls and Harshit Sikchi for providing helpful commends and feedback on the manuscript.

## References

Ahn et al. (2022) M. Ahn, A. Brohan, N. Brown, Y. Chebotar, O. Cortes, B. David, C. Finn, K. Gopalakrishnan, K. Hausman, A. Herzog, D. Ho, J. Hsu, J. Ibarz, B. Ichter, A. Irpan, E. Jang, R. J. Ruano, K. Jeffrey, S. Jesmonth, N. Joshi, R. C. Julian, D. Kalashnikov, Y. Kuang, K. Lee, S. Levine, Y. Lu, L. Luu, C. Parada, P. Pastor, J. Quiambao, K. Rao, J. Rettinghouse, D. Reyes, P. Sermanet, N. Sievers, C. Tan, A. Toshev, V. Vanhoucke, F. Xia, T. Xiao, P. Xu, S. Xu, and M. Yan Do as i can, not as i say: grounding language in robotic affordances . Conference on Robot Learning . Cited by: §2 .

Andrychowicz et al. (2017) M. Andrychowicz, F. Wolski, A. Ray, J. Schneider, R. Fong, P. Welinder, B. McGrew, J. Tobin, O. Pieter Abbeel, and W. Zaremba Hindsight Experience Replay . In Neural Information Processing Systems , Vol. 30 . Cited by: §2 , §3 .

Ba et al. (2016) J. L. Ba, J. R. Kiros, and G. E. Hinton Layer normalization . arXiv preprint arXiv: 1607.06450 . Cited by: §1 , §4.1 .

Blier et al. (2021) L. Blier, C. Tallec, and Y. Ollivier Learning Successor States and Goal-Dependent Values: a Mathematical Viewpoint . arXiv . External Links: 2101.07123 Cited by: §3 .

Bortkiewicz et al. (2024) M. Bortkiewicz, W. Pałucki, V. Myers, T. Dziarmaga, T. Arczewski, Ł. Kuciński, and B. Eysenbach Accelerating goal-conditioned rl algorithms and research . arXiv preprint arXiv:2408.11052 . Cited by: Figure 19 , §B.2 , §1 , §3 , §4.1 .

Caron et al. (2021) M. Caron, H. Touvron, I. Misra, H. Jégou, J. Mairal, P. Bojanowski, and A. Joulin Emerging properties in self-supervised vision transformers . arXiv preprint arXiv: 2104.14294 . Cited by: §1 .

Chang et al. (2018) B. Chang, L. Meng, E. Haber, F. Tung, and D. Begert Multi-level residual networks from dynamical systems view . In 6th International Conference on Learning Representations, ICLR 2018, Vancouver, BC, Canada, April 30 - May 3, 2018, Conference Track Proceedings , External Links: Link Cited by: §A.7 .

Chen et al. (2022) C. Chen, J. Zhang, Y. Xu, L. Chen, J. Duan, Y. Chen, S. D. Tran, B. Zeng, and T. Chilimbi Why do we need large batchsizes in contrastive learning? a gradient-bias perspective . In Advances in Neural Information Processing Systems , A. H. Oh, A. Agarwal, D. Belgrave, and K. Cho (Eds.) , External Links: Link Cited by: §4.4 , §4.4 .

Chen et al. (2020) T. Chen, S. Kornblith, K. Swersky, M. Norouzi, and G. E. Hinton Big self-supervised models are strong semi-supervised learners . Advances in neural information processing systems 33 , pp. 22243–22255 . Cited by: §1 .

Dehghani et al. (2023) M. Dehghani, J. Djolonga, B. Mustafa, P. Padlewski, J. Heek, J. Gilmer, A. Steiner, M. Caron, R. Geirhos, I. M. Alabdulmohsin, R. Jenatton, L. Beyer, M. Tschannen, A. Arnab, X. Wang, C. Riquelme, M. Minderer, J. Puigcerver, U. Evci, M. Kumar, S. van Steenkiste, G. F. Elsayed, A. Mahendran, F. Yu, A. Oliver, F. Huot, J. Bastings, M. Collier, A. Gritsenko, V. Birodkar, C. Vasconcelos, Y. Tay, T. Mensink, A. Kolesnikov, F. Paveti’c, D. Tran, T. Kipf, M. Luvci’c, X. Zhai, D. Keysers, J. Harmsen, and N. Houlsby Scaling vision transformers to 22 billion parameters . International Conference on Machine Learning . External Links: Document Cited by: §1 , §2 .

Driess et al. (2023) D. Driess, F. Xia, M. S. M. Sajjadi, C. Lynch, A. Chowdhery, B. Ichter, A. Wahid, J. Tompson, Q. Vuong, T. Yu, W. Huang, Y. Chebotar, P. Sermanet, D. Duckworth, S. Levine, V. Vanhoucke, K. Hausman, M. Toussaint, K. Greff, A. Zeng, I. Mordatch, and P. R. Florence PaLM-e: an embodied multimodal language model . International Conference on Machine Learning . External Links: Document Cited by: §2 .

Dubey et al. (2024) A. Dubey, A. Jauhri, A. Pandey, A. Kadian, A. Al-Dahle, A. Letman, A. Mathur, A. Schelten, A. Yang, A. Fan, et al. The llama 3 herd of models . arXiv preprint arXiv:2407.21783 . Cited by: §1 .

Espeholt et al. (2018) L. Espeholt, H. Soyer, R. Munos, K. Simonyan, V. Mnih, T. Ward, Y. Doron, V. Firoiu, T. Harley, I. Dunning, et al. Impala: scalable distributed deep-rl with importance weighted actor-learner architectures . In International conference on machine learning , pp. 1407–1416 . Cited by: §2 .

Esser et al. (2024) P. Esser, S. Kulal, A. Blattmann, R. Entezari, J. Müller, H. Saini, Y. Levi, D. Lorenz, A. Sauer, F. Boesel, et al. Scaling rectified flow transformers for high-resolution image synthesis . In Forty-first International Conference on Machine Learning , Cited by: §1 .

Eysenbach et al. (2021) B. Eysenbach, R. Salakhutdinov, and S. Levine C-Learning: Learning to Achieve Goals via Recursive Classification . In International Conference on Learning Representations , Cited by: §1 , §3 .

Eysenbach et al. (2022) B. Eysenbach, T. Zhang, S. Levine, and R. R. Salakhutdinov Contrastive learning as goal-conditioned reinforcement learning . Advances in Neural Information Processing Systems 35 , pp. 35603–35620 . Cited by: §1 , §2 , §3 .

Farebrother et al. (2024) J. Farebrother, J. Orbay, Q. Vuong, A. A. Taïga, Y. Chebotar, T. Xiao, A. Irpan, S. Levine, P. S. Castro, A. Faust, A. Kumar, and R. Agarwal Stop Regressing: Training Value Functions via Classification for Scalable Deep RL . arXiv . Cited by: §1 , §2 , §3 .

Freeman et al. (2021) C. D. Freeman, E. Frey, A. Raichuk, S. Girgin, I. Mordatch, and O. Bachem Brax – a Differentiable Physics Engine for Large Scale Rigid Body Simulation . In NeurIPS Datasets and Benchmarks , External Links: Link Cited by: §4.1 .

Goyal et al. (2019) P. Goyal, D. Mahajan, A. Gupta, and I. Misra Scaling and benchmarking self-supervised visual representation learning . In Proceedings of the ieee/cvf International Conference on computer vision , pp. 6391–6400 . Cited by: §1 .

Gupta et al. (2019) A. Gupta, V. Kumar, C. Lynch, S. Levine, and K. Hausman Relay policy learning: solving long-horizon tasks via imitation and reinforcement learning . Conference on Robot Learning . Cited by: §4.5 .

He et al. (2015) K. He, X. Zhang, S. Ren, and J. Sun Deep residual learning for image recognition . Computer Vision and Pattern Recognition . External Links: Document Cited by: §1 , §3 , §4.1 .

He et al. (2016) K. He, X. Zhang, S. Ren, and J. Sun Identity mappings in deep residual networks . pp. 630–645 . External Links: Document , Link Cited by: §3 .

Henderson et al. (2018) P. Henderson, R. Islam, P. Bachman, J. Pineau, D. Precup, and D. Meger Deep reinforcement learning that matters . In Proceedings of the AAAI conference on artificial intelligence , Vol. 32 . Cited by: §2 .

Huang et al. (2022) S. Huang, R. F. J. Dossa, C. Ye, J. Braga, D. Chakraborty, K. Mehta, and J. G.M. Araújo CleanRL: high-quality single-file implementations of deep reinforcement learning algorithms . Journal of Machine Learning Research 23 ( 274 ), pp. 1–18 . External Links: Link Cited by: §1 .

Kaelbling (1993) L. P. Kaelbling Learning to achieve goals . In IJCAI , Vol. 2 , pp. 1094–8 . Cited by: §3 .

Kumar et al. (2023) A. Kumar, R. Agarwal, X. Geng, G. Tucker, and S. Levine Offline q-learning on diverse multi-task data both scales and generalizes . In The Eleventh International Conference on Learning Representations, ICLR 2023, Kigali, Rwanda, May 1-5, 2023 , External Links: Link Cited by: §2 .

LeCun (2016) Y. LeCun Predictive learning . Note: Invited talk at the 30th Conference on Neural Information Processing Systems (NIPS)Barcelona, Spain External Links: Link Cited by: §1 , §2 , §4.4 .

Lee et al. (2024) H. Lee, D. Hwang, D. Kim, H. Kim, J. J. Tai, K. Subramanian, P. R. Wurman, J. Choo, P. Stone, and T. Seno SimBa: Simplicity Bias for Scaling Up Parameters in Deep Reinforcement Learning . Cited by: §A.2 , 2nd item , §1 , §2 , §3 , Figure 4 , Figure 4 , §4.2 , §4.4 , §4.4 , §4.5 .

Lee et al. (2022) K. Lee, O. Nachum, M. Yang, L. Lee, D. Freeman, W. Xu, S. Guadarrama, I. Fischer, E. Jang, H. Michalewski, and I. Mordatch Multi-Game Decision Transformers . arXiv . Cited by: §1 .

Liu et al. (2023) B. Liu, Y. Feng, Q. Liu, and P. Stone Metric Residual Networks for Sample Efficient Goal-Conditioned Reinforcement Learning . Cited by: §A.4 .

Liu et al. (2024) H. Liu, C. Li, Q. Wu, and Y. J. Lee Visual instruction tuning . Advances in neural information processing systems 36 . Cited by: §1 .

Lyle et al. (2022) C. Lyle, M. Rowland, and W. Dabney Understanding and preventing capacity loss in reinforcement learning . arXiv preprint arXiv:2204.09560 . Cited by: §2 .

Lyle et al. (2024) C. Lyle, Z. Zheng, K. Khetarpal, H. van Hasselt, R. Pascanu, J. Martens, and W. Dabney Disentangling the causes of plasticity loss in neural networks . arXiv preprint arXiv:2402.18762 . Cited by: §2 .

Makoviychuk et al. (2021) V. Makoviychuk, L. Wawrzyniak, Y. Guo, M. Lu, K. Storey, M. Macklin, D. Hoeller, N. Rudin, A. Allshire, A. Handa, et al. Isaac gym: high performance gpu-based physics simulation for robot learning . arXiv preprint arXiv:2108.10470 . Cited by: §1 .

Myers et al. (2024) V. Myers, C. Zheng, A. Dragan, S. Levine, and B. Eysenbach Learning temporal distances: contrastive successor features can provide a metric structure for decision-making . International Conference on Machine Learning . External Links: Document Cited by: §A.4 , §3 .

Nauman et al. (2024a) M. Nauman, M. Bortkiewicz, P. Milos, T. Trzcinski, M. Ostaszewski, and M. Cygan Overestimation, overfitting, and plasticity in actor-critic: the bitter lesson of reinforcement learning . In Forty-first International Conference on Machine Learning, ICML 2024, Vienna, Austria, July 21-27, 2024 , External Links: Link Cited by: §2 .

Nauman et al. (2024b) M. Nauman, M. Ostaszewski, K. Jankowski, P. Miłoś, and M. Cygan Bigger, Regularized, Optimistic: scaling for compute and sample-efficient continuous control . arXiv . Cited by: §A.2 , 2nd item , §1 , §2 , §3 , Figure 4 , Figure 4 , §4.2 , §4.4 , §4.4 , §4.5 .

Neumann and Gros (2022) O. Neumann and C. Gros Scaling laws for a multi-agent reinforcement learning model . arXiv preprint arXiv:2210.00849 . Cited by: §2 .

Obando-Ceron et al. (2023) J. Obando-Ceron, M. G. Bellemare, and P. S. Castro Small batch deep reinforcement learning . Neural Information Processing Systems . Note: Published at NeurIPS 2023 External Links: Link Cited by: §4.4 .

Obando-Ceron et al. (2024) J. Obando-Ceron, G. Sokar, T. Willi, C. Lyle, J. Farebrother, J. N. Foerster, G. Dziugaite, D. Precup, and P. S. Castro Mixtures of experts unlock parameter scaling for deep rl . International Conference on Machine Learning . External Links: Document Cited by: §2 , §2 .

Ota et al. (2021) K. Ota, D. K. Jha, and A. Kanezaki Training larger networks for deep reinforcement learning . arXiv preprint arXiv:2102.07920 . Cited by: §2 , §2 .

Park et al. (2024) S. Park, K. Frans, B. Eysenbach, and S. Levine OGBench: benchmarking offline goal-conditioned rl . arXiv preprint arXiv: 2410.20092 . Cited by: Figure 18 , §4.6 .

Radford et al. (2021) A. Radford, J. W. Kim, C. Hallacy, A. Ramesh, G. Goh, S. Agarwal, G. Sastry, A. Askell, P. Mishkin, J. Clark, G. Krueger, and I. Sutskever Learning transferable visual models from natural language supervision . International Conference on Machine Learning . Cited by: §1 , §1 .

Radford (2018) A. Radford Improving language understanding by generative pre-training . Cited by: §1 .

Raffin et al. (2021) A. Raffin, A. Hill, A. Gleave, A. Kanervisto, M. Ernestus, and N. Dormann Stable-baselines3: reliable reinforcement learning implementations . Journal of Machine Learning Research 22 ( 268 ), pp. 1–8 . External Links: Link Cited by: §1 .

Ramachandran et al. (2018) P. Ramachandran, B. Zoph, and Q. V. Le Searching for activation functions . In 6th International Conference on Learning Representations, ICLR 2018, Vancouver, BC, Canada, April 30 - May 3, 2018, Workshop Track Proceedings , External Links: Link Cited by: §1 , §4.1 .

Rudin et al. (2022) N. Rudin, D. Hoeller, P. Reist, and M. Hutter Learning to walk in minutes using massively parallel deep reinforcement learning . In Conference on Robot Learning , pp. 91–100 . Cited by: §1 .

Rutherford et al. (2023) A. Rutherford, B. Ellis, M. Gallici, J. Cook, A. Lupu, G. Ingvarsson, T. Willi, A. Khan, C. S. de Witt, A. Souly, et al. JaxMARL: multi-agent rl environments and algorithms in jax . arXiv preprint arXiv:2311.10090 . Cited by: §1 .

Schwarzer et al. (2023) M. Schwarzer, J. S. Obando-Ceron, A. C. Courville, M. G. Bellemare, R. Agarwal, and P. S. Castro Bigger, better, faster: human-level atari with human-level efficiency . In International Conference on Machine Learning, ICML 2023, 23-29 July 2023, Honolulu, Hawaii, USA , A. Krause, E. Brunskill, K. Cho, B. Engelhardt, S. Sabato, and J. Scarlett (Eds.) , Proceedings of Machine Learning Research , Vol. 202 , pp. 30365–30380 . External Links: Link Cited by: §2 .

Sohn (2016) K. Sohn Improved Deep Metric Learning With Multi-Class N-Pair Loss Objective . In Neural Information Processing Systems , Vol. 29 . Cited by: §3 .

Srivastava et al. (2023) A. Srivastava, A. Rastogi, A. Rao, et al. Beyond the imitation game: quantifying and extrapolating the capabilities of language models . Trans. Mach. Learn. Res. . Cited by: §1 , §1 , §2 , §5 .

Team et al. (2023) A. A. Team, J. Bauer, K. Baumli, S. Baveja, F. Behbahani, A. Bhoopchand, N. Bradley-Schmieg, M. Chang, N. Clay, A. Collister, et al. Human-timescale adaptation in an open-ended task space . arXiv preprint arXiv:2301.07608 . Cited by: §2 .

Todorov et al. (2012) E. Todorov, T. Erez, and Y. Tassa Mujoco: a Physics Engine for Model-Based Control . In IEEE/RSJ International Conference on Intelligent Robots and Systems , pp. 5026–5033 . Cited by: §4.1 .

Torgo and Gama (1996) L. Torgo and J. Gama Regression by classification . In Advances in Artificial Intelligence: 13th Brazilian Symposium on Artificial Intelligence, SBIA’96 Curitiba, Brazil, October 23–25, 1996 Proceedings 13 , pp. 51–60 . Cited by: §2 .

Tuyls et al. (2024) J. Tuyls, D. Madeka, K. Torkkola, D. Foster, K. Narasimhan, and S. Kakade Scaling Laws for Imitation Learning in Single-Agent Games . arXiv . Cited by: §2 .

Van Hasselt et al. (2018) H. Van Hasselt, Y. Doron, F. Strub, M. Hessel, N. Sonnerat, and J. Modayil Deep reinforcement learning and the deadly triad . arXiv preprint arXiv:1812.02648 . Cited by: §2 .

Vaswani et al. (2017) A. Vaswani, N. M. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. Kaiser, and I. Polosukhin Attention is all you need . nips . Cited by: §2 .

Veit et al. (2016) A. Veit, M. Wilber, and S. Belongie Residual networks behave like ensembles of relatively shallow networks . arXiv preprint arXiv: 1605.06431 . Cited by: §3 .

Wang et al. (2023a) T. Wang, A. Torralba, P. Isola, and A. Zhang Optimal goal-reaching reinforcement learning via quasimetric learning . In International Conference on Machine Learning, ICML 2023, 23-29 July 2023, Honolulu, Hawaii, USA , A. Krause, E. Brunskill, K. Cho, B. Engelhardt, S. Sabato, and J. Scarlett (Eds.) , Proceedings of Machine Learning Research , Vol. 202 , pp. 36411–36430 . External Links: Link Cited by: §A.4 .

Wang et al. (2023b) T. Wang, A. Torralba, P. Isola, and A. Zhang Optimal goal-reaching reinforcement learning via quasimetric learning . External Links: 2304.01203 , Link Cited by: §A.3 .

Wei et al. (2022) J. Wei, Y. Tay, R. Bommasani, C. Raffel, B. Zoph, S. Borgeaud, D. Yogatama, M. Bosma, D. Zhou, D. Metzler, E. H. Chi, T. Hashimoto, O. Vinyals, P. Liang, J. Dean, and W. Fedus Emergent abilities of large language models . Trans. Mach. Learn. Res. . External Links: Document Cited by: §2 .

Zhai et al. (2021) X. Zhai, A. Kolesnikov, N. Houlsby, and L. Beyer Scaling vision transformers . Computer Vision and Pattern Recognition . External Links: Document Cited by: §1 , §2 .

Zhang et al. (2024) H. Zhang, D. Morwani, N. Vyas, J. Wu, D. Zou, U. Ghai, D. Foster, and S. Kakade How does critical batch size scale in pre-training? . arXiv preprint arXiv: 2410.21676 . Cited by: §4.4 , §4.4 .

Zheng et al. (2024) C. Zheng, B. Eysenbach, H. Walke, P. Yin, K. Fang, R. Salakhutdinov, and S. Levine Stabilizing Contrastive RL: Techniques for Offline Goal Reaching . In International Conference on Learning Representations , Cited by: §3 , §4.2 , §4.6 .

Zheng et al. (2023) C. Zheng, R. Salakhutdinov, and B. Eysenbach Contrastive Difference Predictive Coding . In Twelfth International Conference on Learning Representations , Cited by: §3 .

Zong et al. (2024) Y. Zong, O. M. Aodha, and T. Hospedales Self-supervised multimodal learning: a survey . External Links: 2304.01008 , Link Cited by: §1 .

## Appendix A Additional Experiments

### A.1 Scaled CRL Outperforms All Other Baselines on 8 out of 10 Environments

In Figure 1 , we demonstrated that increasing the depth of the CRL algorithm leads to significant performance improvements over the original CRL (see also Table 1 ). Here, we show that these gains translate to state-of-the-art results in online goal-conditioned RL, with Scaled CRL outperforming both standard TD-based methods such as SAC, SAC+HER, and TD3+HER, as well as self-supervised imitation-based approaches like GCBC and GCSL.

### A.2 The CRL Algorithm is Key: Depth Scaling is Not Effective on Other Baselines

Next, we investigate whether increasing network depth in the baseline algorithms yields similar performance improvements as observed in CRL. We find that SAC, SAC+HER, and TD3+HER do not benefit from depths beyond four layers, which is consistent with prior findings ( Lee et al., 2024 ; Nauman et al., 2024b ) . Additionally, GCSL and GCBC fail to achieve any meaningful performance on the Humanoid and Ant Big Maze tasks. Interestingly, we do observe one exception, as GCBC exhibits improved performance with increased depth in the Arm Push Easy environment.

### A.3 Additional Scaling Experiments: Offline GCBC, BC, and QRL

We further investigate several additional scaling experiments. As shown in Figure 14 , our approach successfully scales with depth in the offline GCBC setting on the antmaze-medium-stitch task from OGBench. We find that our the combination of layer normalization, residual connections, and Swish activations is critical, suggesting that our architectural choices may be applied to unlock depth scaling in other algorithms and settings. We also attempt to scale depth for behavioral cloning and the QRL ( Wang et al., 2023b ) algorithm—in both of these cases, however, we observe negative results.

### A.4 Can Depth Scaling also be Effective for Quasimetric Architectures?

Prior work ( Wang et al., 2023a ; Liu et al., 2023 ) has found that temporal distances satisfy an important invariance property, suggesting the use of quasimetric architectures when learning temporal distances. Our next experiment tests whether changing the architecture affects the scaling properties of self-supervised RL. Specifically, we use the CMD-1 algorithm ( Myers et al., 2024 ) , which employs a backward NCE loss with MRN representations. The results indicate that scaling benefits are not limited to a single neural network parametrization. However, MRN’s poor performance on the Ant U5-Maze task suggests further innovation is needed for consistent scaling with quasimetric models.

### A.5 Additional Architectural Ablations: Layer Norm and Swish Activation

We conduct ablation experiments to validate the architectural choices of layer norm and swish activation. Figure 16 shows that removing layer normalization performs significantly worse. Additionally, scaling with ReLU significantly hampers scalability. These results, along with Figure 6 show that all of our architectural components—residual connections, layer norm, and swish activations—are jointly essential to unlocking the full performance of depth scaling.

### A.6 Can We Integrate Novel Architectural Innovations from the Emerging RL Scaling Literature?

Recently, Simba-v2 proposed a new architecture for scalable RL. Its key innovation is the replacement of layer normalization with hyperspherical normalization, which projects network weights onto the unit-norm hypersphere after each gradient update. As shown, the same depth-scaling trends hold when adding hyperspherical normalization to our architecture, and it further improves the sample efficiency of depth scaling. This demonstrates that our method can naturally incorporate new architectural innovations emerging in the RL scaling literature.

### A.7 Residuals Norms in Deep Networks

Prior work has noted decreasing residual activation norms in deeper layers ( Chang et al., 2018 ) . We investigate whether this pattern also holds in our setting. For the critic, the trend is generally evident, especially in very deep architectures (e.g., depth 256). The effect is not as pronounced in the actor.

### A.8 Scaling Depth for Offline Goal-conditioned RL

## Appendix B Experimental Details

### B.1 Environment Setup and Hyperparameters

Our experiments use the JaxGCRL suite of GPU-accelerated environments, visualized in Figure 19 , and a contrastive RL algorithm with hyperparameters reported in Table 7 . In particular, we use 10 environments, namely: ant_big_maze, ant_hardest_maze, arm_binpick_hard, arm_push_easy, arm_push_hard, humanoid, humanoid_big_maze, humanoid_u_maze, ant_u4_maze, ant_u5_maze .

### B.2 Python Environment Differences

In all plots presented in the paper, we used MJX 3.2.6 and Brax 0.10.1 to ensure a fair and consistent comparison. During development, we noticed discrepancies in physics behavior between the environment versions we employed (the CleanRL version of JaxGCRL) and the version recommended in a more recent commit of JaxGCRL ( Bortkiewicz et al., 2024 ) . Upon examination, the performance differences (shown in Figure 20 ) stem from a difference in versions in the MJX and Brax packages. Nonetheless, in both sets of MJX and Brax versions, performance scales monotonically with depth.

### B.3 Wall-clock Time of Our Approach

We report the wall-clock time of our approach in Table 3 . The table shows results for depths of 4, 8, 16, 32, and 64 across all ten environments, and for the Humanoid U-Maze environment, scaling up to 1024 layers. Overall, wall-clock time increases approximately linearly with depth beyond a certain point.

### B.4 Wall-clock Time: Comparison to Baselines

Since the baselines use standard sized networks, naturally our scaled approach incurs higher raw wall-clock time per environment step ( Table 5 ). However, a more practical metric is the time required to reach a given performance level. As shown in Table 6 , our approach outperforms the strongest baseline, SAC, in 7 of 10 environments while requiring less wall-clock time.

## NeurIPS Paper Checklist

1. Claims

Question: Do the main claims made in the abstract and introduction accurately reflect the paper’s contributions and scope?

Answer: [Yes]

Justification: The abstract contains 3 main claims: (1) Depth scaled to 1024 layers; (2) Performance increases 2-50x on CRL and outperforms other goal-conditioned baselines. (3) These performance gains leads to qualitatively new learned behaviors. Each of these claims are clearly substantiated in the main text in Section 4.

Guidelines: • The answer NA means that the abstract and introduction do not include the claims made in the paper.

• The abstract and/or introduction should clearly state the claims made, including the contributions made in the paper and important assumptions and limitations. A No or NA answer to this question will not be perceived well by the reviewers.

• The claims made should match theoretical and experimental results, and reflect how much the results can be expected to generalize to other settings.

• It is fine to include aspirational goals as motivation as long as it is clear that these goals are not attained by the paper.

2. Limitations

Question: Does the paper discuss the limitations of the work performed by the authors?

Answer: [Yes]

Justification: We included a Limitations section that describes the main limitation of our paper, which is latency of deep networks. We also multiple times in the paper demarcated where our research can be extended by future work.

Guidelines: • The answer NA means that the paper has no limitation while the answer No means that the paper has limitations, but those are not discussed in the paper.

• The authors are encouraged to create a separate "Limitations" section in their paper.

• The paper should point out any strong assumptions and how robust the results are to violations of these assumptions (e.g., independence assumptions, noiseless settings, model well-specification, asymptotic approximations only holding locally). The authors should reflect on how these assumptions might be violated in practice and what the implications would be.

• The authors should reflect on the scope of the claims made, e.g., if the approach was only tested on a few datasets or with a few runs. In general, empirical results often depend on implicit assumptions, which should be articulated.

• The authors should reflect on the factors that influence the performance of the approach. For example, a facial recognition algorithm may perform poorly when image resolution is low or images are taken in low lighting. Or a speech-to-text system might not be used reliably to provide closed captions for online lectures because it fails to handle technical jargon.

• The authors should discuss the computational efficiency of the proposed algorithms and how they scale with dataset size.

• If applicable, the authors should discuss possible limitations of their approach to address problems of privacy and fairness.

• While the authors might fear that complete honesty about limitations might be used by reviewers as grounds for rejection, a worse outcome might be that reviewers discover limitations that aren’t acknowledged in the paper. The authors should use their best judgment and recognize that individual actions in favor of transparency play an important role in developing norms that preserve the integrity of the community. Reviewers will be specifically instructed to not penalize honesty concerning limitations.

3. Theory assumptions and proofs

Question: For each theoretical result, does the paper provide the full set of assumptions and a complete (and correct) proof?

Answer: [N/A]

Justification: This is an empirical paper. As such, no theoretical results that require assumptions or proofs.

Guidelines: • The answer NA means that the paper does not include theoretical results.

• All the theorems, formulas, and proofs in the paper should be numbered and cross-referenced.

• All assumptions should be clearly stated or referenced in the statement of any theorems.

• The proofs can either appear in the main paper or the supplemental material, but if they appear in the supplemental material, the authors are encouraged to provide a short proof sketch to provide intuition.

• Inversely, any informal proof provided in the core of the paper should be complemented by formal proofs provided in appendix or supplemental material.

• Theorems and Lemmas that the proof relies upon should be properly referenced.

4. Experimental result reproducibility

Question: Does the paper fully disclose all the information needed to reproduce the main experimental results of the paper to the extent that it affects the main claims and/or conclusions of the paper (regardless of whether the code and data are provided or not)?

Answer: [Yes]

Justification: Yes, documentation for reproducing the experiments is included alongside the anonymous code.

Guidelines: • The answer NA means that the paper does not include experiments.

• If the paper includes experiments, a No answer to this question will not be perceived well by the reviewers: Making the paper reproducible is important, regardless of whether the code and data are provided or not.

• If the contribution is a dataset and/or model, the authors should describe the steps taken to make their results reproducible or verifiable.

• Depending on the contribution, reproducibility can be accomplished in various ways. For example, if the contribution is a novel architecture, describing the architecture fully might suffice, or if the contribution is a specific model and empirical evaluation, it may be necessary to either make it possible for others to replicate the model with the same dataset, or provide access to the model. In general. releasing code and data is often one good way to accomplish this, but reproducibility can also be provided via detailed instructions for how to replicate the results, access to a hosted model (e.g., in the case of a large language model), releasing of a model checkpoint, or other means that are appropriate to the research performed.

• While NeurIPS does not require releasing code, the conference does require all submissions to provide some reasonable avenue for reproducibility, which may depend on the nature of the contribution. For example (a) If the contribution is primarily a new algorithm, the paper should make it clear how to reproduce that algorithm.

(b) If the contribution is primarily a new model architecture, the paper should describe the architecture clearly and fully.

(c) If the contribution is a new model (e.g., a large language model), then there should either be a way to access this model for reproducing the results or a way to reproduce the model (e.g., with an open-source dataset or instructions for how to construct the dataset).

(d) We recognize that reproducibility may be tricky in some cases, in which case authors are welcome to describe the particular way they provide for reproducibility. In the case of closed-source models, it may be that access to the model is limited in some way (e.g., to registered users), but it should be possible for other researchers to have some path to reproducing or verifying the results.

5. Open access to data and code

Question: Does the paper provide open access to the data and code, with sufficient instructions to faithfully reproduce the main experimental results, as described in supplemental material?

Answer: [Yes]

Justification: See link to anonymous code in Abstract.

Guidelines: • The answer NA means that paper does not include experiments requiring code.

• Please see the NeurIPS code and data submission guidelines ( https://nips.cc/public/guides/CodeSubmissionPolicy ) for more details.

• While we encourage the release of code and data, we understand that this might not be possible, so “No” is an acceptable answer. Papers cannot be rejected simply for not including code, unless this is central to the contribution (e.g., for a new open-source benchmark).

• The instructions should contain the exact command and environment needed to run to reproduce the results. See the NeurIPS code and data submission guidelines ( https://nips.cc/public/guides/CodeSubmissionPolicy ) for more details.

• The authors should provide instructions on data access and preparation, including how to access the raw data, preprocessed data, intermediate data, and generated data, etc.

• The authors should provide scripts to reproduce all experimental results for the new proposed method and baselines. If only a subset of experiments are reproducible, they should state which ones are omitted from the script and why.

• At submission time, to preserve anonymity, the authors should release anonymized versions (if applicable).

• Providing as much information as possible in supplemental material (appended to the paper) is recommended, but including URLs to data and code is permitted.

6. Experimental setting/details

Question: Does the paper specify all the training and test details (e.g., data splits, hyperparameters, how they were chosen, type of optimizer, etc.) necessary to understand the results?

Answer: [Yes]

Justification: See Experiments section and Appendix on Experimental Details

Guidelines: • The answer NA means that the paper does not include experiments.

• The experimental setting should be presented in the core of the paper to a level of detail that is necessary to appreciate the results and make sense of them.

• The full details can be provided either with the code, in appendix, or as supplemental material.

7. Experiment statistical significance

Question: Does the paper report error bars suitably and correctly defined or other appropriate information about the statistical significance of the experiments?

Answer: [Yes]

Justification: Error bars in figures depict one standard error across random seeds. We used 5 seeds in Figure 1. For other figures in the main text, we could only run 3 seeds because of computational constraints.

Guidelines: • The answer NA means that the paper does not include experiments.

• The authors should answer "Yes" if the results are accompanied by error bars, confidence intervals, or statistical significance tests, at least for the experiments that support the main claims of the paper.

• The factors of variability that the error bars are capturing should be clearly stated (for example, train/test split, initialization, random drawing of some parameter, or overall run with given experimental conditions).

• The method for calculating the error bars should be explained (closed form formula, call to a library function, bootstrap, etc.)

• The assumptions made should be given (e.g., Normally distributed errors).

• It should be clear whether the error bar is the standard deviation or the standard error of the mean.

• It is OK to report 1-sigma error bars, but one should state it. The authors should preferably report a 2-sigma error bar than state that they have a 96% CI, if the hypothesis of Normality of errors is not verified.

• For asymmetric distributions, the authors should be careful not to show in tables or figures symmetric error bars that would yield results that are out of range (e.g. negative error rates).

• If error bars are reported in tables or plots, The authors should explain in the text how they were calculated and reference the corresponding figures or tables in the text.

8. Experiments compute resources

Question: For each experiment, does the paper provide sufficient information on the computer resources (type of compute workers, memory, time of execution) needed to reproduce the experiments?

Answer: [Yes]

Justification: Compute resources are detailed in the appendix.

Guidelines: • The answer NA means that the paper does not include experiments.

• The paper should indicate the type of compute workers CPU or GPU, internal cluster, or cloud provider, including relevant memory and storage.

• The paper should provide the amount of compute required for each of the individual experimental runs as well as estimate the total compute.

• The paper should disclose whether the full research project required more compute than the experiments reported in the paper (e.g., preliminary or failed experiments that didn’t make it into the paper).

9. Code of ethics

Question: Does the research conducted in the paper conform, in every respect, with the NeurIPS Code of Ethics https://neurips.cc/public/EthicsGuidelines ?

Answer: [Yes]

Justification: No known violations of the Code of Ethics.

Guidelines: • The answer NA means that the authors have not reviewed the NeurIPS Code of Ethics.

• If the authors answer No, they should explain the special circumstances that require a deviation from the Code of Ethics.

• The authors should make sure to preserve anonymity (e.g., if there is a special consideration due to laws or regulations in their jurisdiction).

10. Broader impacts

Question: Does the paper discuss both potential positive societal impacts and negative societal impacts of the work performed?

Answer: [Yes]

Justification: The Conclusion notes that there are no immediately societal impacts of the work.

Guidelines: • The answer NA means that there is no societal impact of the work performed.

• If the authors answer NA or No, they should explain why their work has no societal impact or why the paper does not address societal impact.

• Examples of negative societal impacts include potential malicious or unintended uses (e.g., disinformation, generating fake profiles, surveillance), fairness considerations (e.g., deployment of technologies that could make decisions that unfairly impact specific groups), privacy considerations, and security considerations.

• The conference expects that many papers will be foundational research and not tied to particular applications, let alone deployments. However, if there is a direct path to any negative applications, the authors should point it out. For example, it is legitimate to point out that an improvement in the quality of generative models could be used to generate deepfakes for disinformation. On the other hand, it is not needed to point out that a generic algorithm for optimizing neural networks could enable people to train models that generate Deepfakes faster.

• The authors should consider possible harms that could arise when the technology is being used as intended and functioning correctly, harms that could arise when the technology is being used as intended but gives incorrect results, and harms following from (intentional or unintentional) misuse of the technology.

• If there are negative societal impacts, the authors could also discuss possible mitigation strategies (e.g., gated release of models, providing defenses in addition to attacks, mechanisms for monitoring misuse, mechanisms to monitor how a system learns from feedback over time, improving the efficiency and accessibility of ML).

11. Safeguards

Question: Does the paper describe safeguards that have been put in place for responsible release of data or models that have a high risk for misuse (e.g., pretrained language models, image generators, or scraped datasets)?

Answer: [N/A]

Justification: No immediate impact to high-risk applications.

Guidelines: • The answer NA means that the paper poses no such risks.

• Released models that have a high risk for misuse or dual-use should be released with necessary safeguards to allow for controlled use of the model, for example by requiring that users adhere to usage guidelines or restrictions to access the model or implementing safety filters.

• Datasets that have been scraped from the Internet could pose safety risks. The authors should describe how they avoided releasing unsafe images.

• We recognize that providing effective safeguards is challenging, and many papers do not require this, but we encourage authors to take this into account and make a best faith effort.

12. Licenses for existing assets

Question: Are the creators or original owners of assets (e.g., code, data, models), used in the paper, properly credited and are the license and terms of use explicitly mentioned and properly respected?

Answer: [N/A]

Justification: Benchmarks used are appropriately cited in the main text.

Guidelines: • The answer NA means that the paper does not use existing assets.

• The authors should cite the original paper that produced the code package or dataset.

• The authors should state which version of the asset is used and, if possible, include a URL.

• The name of the license (e.g., CC-BY 4.0) should be included for each asset.

• For scraped data from a particular source (e.g., website), the copyright and terms of service of that source should be provided.

• If assets are released, the license, copyright information, and terms of use in the package should be provided. For popular datasets, paperswithcode.com/datasets has curated licenses for some datasets. Their licensing guide can help determine the license of a dataset.

• For existing datasets that are re-packaged, both the original license and the license of the derived asset (if it has changed) should be provided.

• If this information is not available online, the authors are encouraged to reach out to the asset’s creators.

13. New assets

Question: Are new assets introduced in the paper well documented and is the documentation provided alongside the assets?

Answer: [N/A]

Justification: Datasets and benchmark used are all from prior work and appropriately cited.

Guidelines: • The answer NA means that the paper does not release new assets.

• Researchers should communicate the details of the dataset/code/model as part of their submissions via structured templates. This includes details about training, license, limitations, etc.

• The paper should discuss whether and how consent was obtained from people whose asset is used.

• At submission time, remember to anonymize your assets (if applicable). You can either create an anonymized URL or include an anonymized zip file.

14. Crowdsourcing and research with human subjects

Question: For crowdsourcing experiments and research with human subjects, does the paper include the full text of instructions given to participants and screenshots, if applicable, as well as details about compensation (if any)?

Answer: [N/A]

Justification: No crowdsourcing experiments.

Guidelines: • The answer NA means that the paper does not involve crowdsourcing nor research with human subjects.

• Including this information in the supplemental material is fine, but if the main contribution of the paper involves human subjects, then as much detail as possible should be included in the main paper.

• According to the NeurIPS Code of Ethics, workers involved in data collection, curation, or other labor should be paid at least the minimum wage in the country of the data collector.

15. Institutional review board (IRB) approvals or equivalent for research with human subjects

Question: Does the paper describe potential risks incurred by study participants, whether such risks were disclosed to the subjects, and whether Institutional Review Board (IRB) approvals (or an equivalent approval/review based on the requirements of your country or institution) were obtained?

Answer: [N/A]

Justification: No human subject experiments

Guidelines: • The answer NA means that the paper does not involve crowdsourcing nor research with human subjects.

• Depending on the country in which research is conducted, IRB approval (or equivalent) may be required for any human subjects research. If you obtained IRB approval, you should clearly state this in the paper.

• We recognize that the procedures for this may vary significantly between institutions and locations, and we expect authors to adhere to the NeurIPS Code of Ethics and the guidelines for their institution.

• For initial submissions, do not include any information that would break anonymity (if applicable), such as the institution conducting the review.

16. Declaration of LLM usage

Question: Does the paper describe the usage of LLMs if it is an important, original, or non-standard component of the core methods in this research? Note that if the LLM is used only for writing, editing, or formatting purposes and does not impact the core methodology, scientific rigorousness, or originality of the research, declaration is not required.

Answer: [N/A]

Justification: LLMs were not used in writing the paper, and were only used for occasional code debugging.

Guidelines: • The answer NA means that the core method development in this research does not involve LLMs as any important, original, or non-standard components.

• Please refer to our LLM policy ( https://neurips.cc/Conferences/2025/LLM ) for what should or should not be described.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
