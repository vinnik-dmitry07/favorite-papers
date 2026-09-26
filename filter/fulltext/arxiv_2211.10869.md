##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Uni​ [MASK] : Unified Inference in Sequential Decision Problems

###### Abstract

Randomly masking and predicting word tokens has been a successful approach in pre-training language models for a variety of downstream tasks. In this work, we observe that the same idea also applies naturally to sequential decision making, where many well-studied tasks like behavior cloning, offline reinforcement learning, inverse dynamics, and waypoint conditioning correspond to different sequence maskings over a sequence of states, actions, and returns. We introduce the Uni​ [MASK] framework, which provides a unified way to specify models which can be trained on many different sequential decision making tasks. We show that a single Uni​ [MASK] model is often capable of carrying out many tasks with performance similar to or better than single-task models. Additionally, after fine-tuning, our Uni​ [MASK] models consistently outperform comparable single-task models. Our code is publicly available here .

## 1 Introduction

Masked language modeling [ 11 ] is a key technique in natural language processing (NLP). Under this paradigm, models are trained to predict randomly-masked subsets of tokens in a sequence. For example, during training, a BERT model might be asked to predict the missing words in the sentence “yesterday I cooking a ”. Importantly, while unidirectional models like GPT [ 33 ] are trained to predict the next token conditioned only on the left context, bidirectional models trained on this objective learn to model both the left and right context to represent each word token. This leads to richer representations that can then be fine-tuned to excel on a variety of downstream tasks [ 11 ] .

Our work investigates how masked modeling can be a powerful idea in sequential decision problems. Consider a sequence of states s s and actions a a collected across T T timesteps s 1 , a 1 , … , s T , a T s_{1},a_{1},\dots,s_{T},a_{T} . If we consider each state and action as tokens of a sequence (analogous to words in NLP) and mask the last action ( s 1 , a 1 , s 2 , a 2 , s 3 , ) (s_{1},a_{1},s_{2},a_{2},s_{3},\rule{7.11317pt}{0.42677pt}) , then predicting the missing token a 3 a_{3} amounts to a Behavior Cloning prediction with two timesteps of history [ 32 ] , given that this masking corresponds to the inference ℙ ( a 3 | s 1 : 3 , a 1 : 2 ) \mathbb{P}(a_{3}|s_{1:3},a_{1:2}) . From this perspective, training a model to predict missing tokens from all maskings of the form ( s 1 , a 1 , … , s t , , … , ) (s_{1},a_{1},\dots,s_{t},\rule{7.11317pt}{0.42677pt},\dots,\rule{7.11317pt}{0.42677pt}) for all t ∈ [ 1 , … , T ] t\in[1,\dots,T] corresponds to training a Behavior Cloning (BC) model.

In this work, we introduce the Uni​ [MASK] framework: Uni fied Inferences in Sequential Decision Problems via [MASK] ​ings, where inference tasks are expressed as masking schemes . In this framework, commonly-studied tasks such as goal or waypoint conditioned BC [ 12 , 36 ] , offline reinforcement learning (RL) [ 25 ] , forward or inverse dynamics prediction [ 18 , 9 , 6 ] , initial-state inference [ 38 ] , and others are unified under a simple sequence modeling paradigm. In contrast to standard approaches that train a model for each inference task, we show how this framework naturally lends itself to multi-task training: a single Uni​ [MASK] model can be trained to perform a variety of tasks out-of-the-box by appropriately selecting sequence maskings at training time.

We test this framework in a Gridworld navigation task and a continuous control environment. First, we train a Uni​ [MASK] model by sampling from the space of all possible maskings at training time (random masking) and show how this scheme enables a single Uni​ [MASK] model to perform BC, reward-conditioning, waypoint-conditioning, and more by conditioning on the appropriate subsets of states, actions, and rewards. We then systematically analyze how the masking schemes seen at training time affect downstream task performance. Training on random masking generally does not compromise single-task performance, and in fact can outperform models that only train on the task of interest. In the continuous control environment, we confirm that a model trained with random masking and fine-tuned on BC or RL tends to outperform models specialized to those tasks.

Our results suggest that expressing tasks as sequence maskings with the Uni​ [MASK] framework may be a promising unifying approach to building general-purpose models capable of performing many inference tasks in an environment [ 2 ] , or simply offer an avenue for building better-performing single-task models via unified multi-task training.

In summary, our contributions are:

1. We propose a new framework, Uni​ [MASK] , that unifies inference tasks in sequential decision problems as different masking schemes in a sequence modeling paradigm.

2. We demonstrate how randomly sampling masking schemes at training time produces a single multi-inference-task model that can do BC, reward-conditioning, dynamics modeling, and more out-of-the-box.

3. We test how training on many tasks affects single-task performance and show how fine-tuning models trained with random masking consistently outperforms single-task models.

4. We show how the insights we have gained while developing our choice of Uni​ [MASK] architecture can be used to improve other state-of-the-art methods.

## 2 Related Work

Transformer models. The great successes of transformer models [ 41 ] in other domains such as NLP [ 11 , 33 , 3 ] and computer vision [ 13 , 19 ] motivates our work. Using transformers in RL and sequential decision problems has proven difficult due to the instability of training [ 30 ] , but recent work has investigated using transformers in model-based RL [ 6 ] , motion forecasting [ 29 ] , learning from demonstrations [ 34 ] , and teleoperation [ 10 ] . We focus on developing a unifying framework interpreting tasks in sequential decision problems as maskings.

The utility of masked prediction. Work in both NLP [ 11 ] and vision [ 5 , 19 ] have explored how masked prediction is useful as a self-supervision task. In the context of language generation, [ 39 ] provides a framework for thinking about different masking schemes. Recent work has also explored how random masking can be used to do posterior inference in a probabilistic program [ 43 ] .

Sequential decision-making as sequence modeling. Previous and concurrent work [ 7 , 21 , 24 ] shows how to use GPT-style (causally-masked) transformers to directly generate high-reward trajectories in an offline RL setting. We expand our focus to many tasks that a sequence modeling perspective enables, including but not restricted to offline RL. Although previous work has cast doubt on the necessity of using transformers to achieve good results in offline RL [ 14 ] , we note that offline RL [ 25 ] is just one of the various tasks we consider. Concurrent work generalizes the left-to-right masking in the transformer to condition on future trajectory information for tasks like state marginal matching [ 17 ] and multi-agent motion forecasting [ 29 ] . In contrast, we systematically investigate how a single bidirectional transformer can be trained to perform arbitrary downstream tasks in more complex settings than motion forecasting – i.e., we also consider agent actions and rewards in addition to states. The main thing that sets us apart from these works is a systematic view of all tasks that can be represented by this sequence-modeling perspective, and a detailed investigation of how different multi-task training regimes compare.

Prior work on tasks in sequential decision problems. While we use masked prediction as the self-supervision objective, previous work on self-supervised learning for RL has investigated other auxiliary objectives, such as state dynamics prediction [ 37 ] or intrinsic motivation [ 31 ] . Typically, to accomplish the tasks we consider, prior work relies on single-task models: for example, goal-conditioned imitation learning [ 12 ] , RL [ 22 ] , waypoint-conditioning [ 36 ] , property-conditioning [ 45 , 17 ] , or dynamics model learning [ 18 , 9 ] . Other work has focused on training models to perform different “tasks” such as different games in Atari [ 24 ] or different environments and multi-modal prediction tasks [ 35 ] . In contrast, we are interested in performing different inference tasks in a single environment, such as RL and forward dynamics modeling, using sequence modeling as a unifying framework.

## 3 The Uni​ [MASK] Framework

We introduce the Uni​ [MASK] framework. In Section 3.1 we propose a unifying interpretation of inference tasks in sequential decision problems as masking schemes. In Section 3.2 we describe different ways of training Uni​ [MASK] models, and provide hypotheses about their efficacy.

We consider trajectories as sequences of states , actions , and optionally property tokens (e.g. reward ): τ = { ( s 0 , a 0 , p 0 ) , … , ( s T , a T , p T ) } \tau=\{(s_{0},a_{0},p_{0}),\ldots,(s_{T},a_{T},p_{T})\} . 1 1 1 While reward-to-go (or other trajectory statistics) are not necessary, we formulate the most general form to showcase how one can easily condition on additional available properties of a trajectory. Using reward-to-go also enables us to compare our method with previous offline-RL work [ 7 ] .

Motivated by canonical problems in decision-making that involve reward, in most of our analysis we use return-to-go (RTG) as the property (the sum of rewards from timestep t t to the end of the episode): that is, we set p t = R ^ t p_{t}=\hat{R}_{t} where R ^ t = ∑ t ′ = t T r t ′ \hat{R}_{t}=\sum_{t^{\prime}=t}^{T}r_{t^{\prime}} . However, any property of the decision problem can be considered a “property token,” including specific environment conditions being satisfied, the style of the agent, or the performance of the agent (e.g. the reward obtained in the timestep). In order to train on tasks requiring specific properties, one must have labels for them – obtained either programmatically or through human annotators. We demonstrate how our model can be conditioned on a non-reward property in Appendix F .

### 3.1 Tasks as Masking Schemes

In the Uni​ [MASK] framework, we formulate tasks in sequential decision problems as input masking schemes. Formally, a masking scheme specifies which input tokens are masked (determining what tokens are shown to the model for prediction) and which outputs of the model are masked before computing losses (determining which outputs the model should learn to predict). For example, the masking scheme for BC unmasks (conditions on) s 0 : t s_{0:t} and a 0 : t − 1 a_{0:t-1} , and the model must predict a t a_{t} .

In Figure 1 , we illustrate how to unify commonly-studied tasks such as BC, goal and waypoint conditioned imitation, offline RL (reward-conditioned imitation), and dynamics modeling under our proposed representation of tasks as masking schemes. We describe the masking scheme for each of these tasks in detail in Appendix B .

### 3.2 Model Architecture & Training Regimes

For our main experiments, we instantiate our Uni​ [MASK] framework using the BERT architecture [ 11 ] adapted to the sequential decision problem domain, consisting of a positional encoding layer and stacked bidirectional transformer encoder (self-attention) layers (see Figure 2 ). One key difference with the original BERT architecture is that we stack the state, action, and property (e.g. RTG) tokens for each timestep into a single vector. While prior work in sequential decision-making had used timestep encoding [ 7 ] (which can be thought of as concatenating each observation with its environment timestep), we found traditional positional encoding [ 41 , 11 ] to reduce overfitting. For reward-conditioned tasks, in each context window we only feed the first RTG token into the model along with the number of timesteps remaining in the horizon. This information is sufficient for reward-conditioning at inference time, and we found that it outperformed the standard approach of feeding in the RTG token at every timestep [ 7 , 21 ] . See Appendix D for more model details, and Appendix F for experiments with an alternative instantiation of Uni​ [MASK] with a feedforward neural network architecture.

#### 3.2.1 Training regimes

We experiment with four ways to train a Uni​ [MASK] model on masked prediction, illustrated in Figure 3 and described below.

single-task . Training on just one of the masking scheme described in Section 3.1 .

Training a single model on multiple masking schemes: each trajectory snippet is masked according to one of the schemes from Section 3.1 (chosen at random). Intuition: Could allow a single model to perform well on multiple tasks. Additionally, it might outperform single-task on individual tasks, as the model could learn richer representations of the environment from the additional masking schemes.

Training a single model on a fully randomized masking scheme. For each trajectory snippet, first, a masking probability p mask ∈ [ 0 , 1 ] p_{\textrm{mask}}\in[0,1] is sampled uniformly at random; then each state and action token is masked with probability p mask p_{\textrm{mask}} ; lastly, the first RTG token is masked with probability 1 / 2 1/2 and subsequent RTG tokens are always masked (see Appendix C for details). Intuition: Could allow a single model to perform well on any sequence inference task without the need to specify the tasks of interest at training time. The model may learn richer representations than those of multi-task as it must reason about all aspects of the environment.

Fine-tune a model pre-trained in random-mask on a specific masking scheme. Intuition: Performing fine-tuning could allow the model to benefit from the improved representations obtained from random-mask , while specializing to the single task at hand.

#### 3.2.2 Hypotheses

Based on the intuition of the strengths of each training regime, we formulate the following hypotheses:

H1. First training on multiple inference tasks will lead to better performance on individual tasks than only training on that inference task: { multi-task , random-mask , finetune } > single-task \left\{\text{\hyperlink{tr:multi}{{multi-task}}, \hyperlink{tr:random}{{random-mask}}, \hyperlink{tr:finetune}{{finetune}}}\right\}>\text{\hyperlink{tr:single}{{single-task}}} .

Randomized mask training outperforms training on a specific set of tasks: random-mask > multi-task \text{\hyperlink{tr:random}{{random-mask}}}>\text{\hyperlink{tr:multi}{{multi-task}}} .

H1 tests whether models learn richer representations by training on multiple inference tasks. H2 tests a stronger claim: whether training on all possible tasks by randomly sampling masking at training time is better than selecting a set of specific maskings.

## 4 A Unified Model for Any Inference Task

We first demonstrate how random-mask enables a single Uni​ [MASK] model to perform arbitrary inference tasks at test-time on a Gridworld environment, without the need for task-specific output heads or training schemes that are customized for the downstream task. We then show that random-mask does not compromise performance on most specific tasks of interest. Models trained with random-mask achieve comparable or better performance to single-task and multi-task -models, and in fact consistently outperform after additional fine-tuning on the task of interest ( finetune ).

Environment Setup. We design a fully observable 4 × 4 4\times 4 Gridworld in which the agent should move to a fixed goal location behind a locked door with the MiniGrid environment framework [ 8 ] . The agent and key positions are randomized in each episode. The agent receives a reward of 1 1 for each timestep it moves closer to the goal, − 1 -1 if it moves away from the goal, and 0 0 otherwise. We train Uni​ [MASK] models on training trajectories of sequence length T = 10 T=10 from a noisy-rational agent [ 46 ] . More detailed information about the environment is in Appendix E .

### 4.1 One Model to Rule Them All

As shown in Figure 4 , a single Uni​ [MASK] model trained with random-mask can be used for arbitrary inference tasks by conditioning on specific sets of tokens. Unless otherwise indicated, we take the highest probability action from the model a t = arg ⁡ max a t ′ ⁡ ℙ ⁡ ( a t ′ ∣ s 0 , a 0 , … , s t ) a_{t}=\arg\max_{a_{t}^{\prime}}\mathbb{P}(a_{t}^{\prime}\mid s_{0},a_{0},\ldots,s_{t}) , and then query the environment dynamics for the next state s t + 1 s_{t+1} . The model can be used for imitation, reward- and goal-conditioning, or as a forward or inverse dynamics model (when querying for state predictions, as in the backwards inference task). If trajectories are labeled with properties at training time, the model can also be used for property-conditioning. In Figure 6 , we show how the model can also be conditioned on global properties of the trajectory, such as whether the trajectory passes through a certain position at any timestep.

Qualitatively, these results suggest that the model generalizes across masking schemes, since seeing the exact masking corresponding to a particular task at training time is exceedingly rare (out of 2 T × 2 T × 2 2^{T}\times 2^{T}\times 2 possible state, action, and RTG maskings for a sequence of length T T ).

### 4.2 Future State Predictions

Uses of the random-mask -trained Uni​ [MASK] model are not limited to rolling out new trajectories (requesting inferences about the agent’s next action). One can also request inferences for states and actions further into the future: e.g., “where will the agent be in 3 timesteps ?”. Given a fixed initial set of observed states, we visualize the distribution of predicted states at each timestep in Figure 6 . Since we do not roll out actions, querying the model for the predicted state distribution at a particular timestep marginalizes over missing actions; for example, ℙ ⁡ ( s 1 ∣ s 0 , s 3 , s 6 ) \mathbb{P}(s_{1}\mid s_{0},s_{3},s_{6}) models the possibility that the agent chooses either up or left as the first action. Qualitatively, the state predictions suggest that the model accurately captures the environment dynamics and usual agent behavior; e.g. it correctly models that the agent has equal probability of going up and right at t = 3 t=3 (leading it to the distribution over states at t = 4 t=4 ), and that the agent must be at position (2, 1) at t = 5 t=5 to reach the door at t = 6 t=6 .

### 4.3 Measuring Single-Task Performance

Next, we investigate how a random-mask model performs on individual tasks, in comparison to single-task models trained exclusively on the evaluated task. If we care about a single task (e.g. goal-conditioned imitation), should we train a model simply on that task? Or can there be advantages to training a general model first, and then fine-tuning it to the task of interest? For this set of experiments, we primarily consider validation loss as our measure of performance. Validation loss provides a general way to evaluate how well models fit the distribution of trajectories and transitions, which is what we are concerned with for most inference tasks: i.e., “how well can the network predict the true state or action in the data?”.

In Figure 7 , we report validation loss if the model is trained on one task (or multiple tasks) and evaluated on another task. As expected, models trained on one masking (e.g. BC) perform well when queried on the task they were trained on (as seen on the diagonal), but poorly when queried with another task (e.g. past inference).

First, we find that random-mask training (but not multi-task training) outperforms single-task training on half of the tasks considered, showing that even if one is interested in a single inference task, training on many more tasks can sometimes improve performance. Specializing a model trained with random-mask via finetuning ( finetune ) leads to the best performance, outperforming single-task on all tasks except behavior cloning. This means that even if one is interested in a single inference task, first training on multiple tasks generally improves performance. Overall, these results do not fully support H1 , given multi-task ’s poor performance and random-mask ’s performance which is not consistently better than single-task .

We also find that random-mask training leads to lower loss values on almost all evaluation tasks relative to multi-task , supporting H2 : training on additional inference tasks beyond the specific ones of interest can augment performance.

## 5 Trajectory Generation in a Complex Environment

In addition to Gridworld, we test our method in a partially observable, continuous-state and continuous-action environment, with a larger trajectory horizon (200 timesteps).

### 5.1 Environment Setup

We adapt the Mujoco-physics Maze2D environment [ 16 ] (see Appendix H for figures), in which a point-mass object is placed at a random location in a maze, and the agent is rewarded for moving towards a randomly generated target location (making this task “goal-conditioned by default”). We make this task harder by removing the agent’s velocity information from each timestep’s observation and increasing the amount of initial position randomization. These changes make the environment partially observable, forcing models trained on this data to implicitly infer the agent’s velocity from observed context.

Expert dataset. We want our expert data to have some suboptimality so that reward-conditioning can be tested for better-than-demonstrator performance. We generate a dataset of expert trajectories by rolling out D4RL’s PD controller (which is non-Markovian), and add noise to the actions with zero-mean and 0.5 0.5 variance (which are then clipped to have each dimension between − 1 , 1 -1,1 ). We generate 1000 trajectories of 200 timesteps, of which 900 are used for testing and 100 for validation. For more details on our adapted Maze2D environment and design decisions, see Appendix H .

### 5.2 Models Trained

For the Maze2D evaluations, we focus on test-time reward performance on behavior cloning and offline RL (reward-conditioning) across various architectures and training regimes.

We consider Uni​ [MASK] models trained with the different training regimes: single-task , multi-task , random-mask , and finetune . We additionally consider other architectures, such as a feed-forward NN and Decision Transformer (DT) baselines [ 7 ] . We found that several of our design decisions for Uni​ [MASK] models – using positional encoding instead of timestep encoding, inputting the return-to-go token at the first timestep with the number of timesteps in the horizon – also improved GPT-based models like DT. We call our improved baseline Decision-GPT (for implementation details, see Appendix G ). We train our Decision-GPT model with the single-task training regime. The only meaningful difference between Decision-GPT and a single-task Uni​ [MASK] model is whether the model is GPT- or BERT-based.

For each architecture and applicable training regime, we train separate models to perform behavior cloning and offline RL (reward-conditioning). The only exceptions are Uni​ [MASK] models trained with multi-task (trained to perform BC and RC) and random-mask . We train two sets of such models, for context lengths of 5 and 10 – meaning that during both training and evaluation, the models will respectively only be able to see the last 5 or 10 timesteps of the agent’s interaction with the environment.

### 5.3 Results

We report reward evaluation results for 1000 rollouts in the Maze environment with standard errors across 5 seeds in Table 1 .

The value of pre-training and fine-tuning for Uni​ [MASK] models. We find that fine-tuning is critical for good performance in more complex environments. multi-task performs more-or-less comparably to single-task in behavior cloning and reward conditioning; however, random-mask in this setting obtains significantly lower rewards (counter to H2 ). This suggests that multi-task training can be effective in mostly maintaining reward performance while increasing the breadth of functionality, but training on too many tasks can hurt out-of-the-box performance. However, finetune recovers the performance loss, again out-performing single-task (providing qualified support for H1 ). Surprisingly, for a context length of ten, fine-tuning multi-task does not improve performance as much as fine-tuning the randomly masked model, suggesting that specifically training on random masking might provide benefits for adapting models to individual downstream tasks.

How do Uni​ [MASK] models compare to other architectures? For context length five, we see that multi-task with finetuning and finetune Uni​ [MASK] models perform better than all baselines we consider. However, increasing the context length to ten, we see that Uni​ [MASK] models performs poorly across the board, with the finetuned conditions outperformed by our Decision-GPT baseline. We speculate that this might be related to the documented difficulty of using BERT-like architectures (as that of Uni​ [MASK] models) for sequence generation [ 42 , 28 ] .

Isolating the effect of GPT vs. BERT. In order to investigate the effect of using GPT-like architectures instead of BERT-like ones, we can consider the comparison between single-task Uni​ [MASK] and our Decision-GPT baseline: the main difference between these two models is only whether one uses BERT or GPT as the backbone of the architecture. 2 2 2 We additionally use input-stacking for Uni​ [MASK] – see Appendix D – but in preliminary experiments we found this to not affect performance. We find that while using GPT seems to yield similar (or worse) performance to BERT for context length five, using GPT seems to give an advantage for longer sequence lengths. In particular, note that a larger context length enables GPT to increase performance, while performance worsens for single-task Uni​ [MASK] . This suggests that if one were able to use a GPT architecture and train it with random masking and fine-tuning, it might be possible to get the best of both worlds.

## 6 Limitations and Future Work

Comparison to other specialized models. We show that Uni​ [MASK] outperforms feedforward networks, Decision Transformer models, and for short sequence lengths also our own improved GPT-based baseline. However, we do not compare our models directly to different models in prior work that are specialized for specific tasks (e.g. goal-conditioning models, etc.). While this is a limitation of our work, it is also not our main focus: we propose a unifying framework for a variety of tasks in sequential decision problems, and extensively analyze how different training regimes affect performance.

Longer context lengths. One limitation in our experimentation is the relatively short context lengths used. We found that longer context lengths negatively affect the Uni​ [MASK] models’ performance. In part, this could be addressed by designing masking schemes tailored to specific test-time tasks (see Appendix C ), or using principled masking schemes [ 26 ] . However, this degradation may be attributed to our use of a BERT-like (rather than GPT-like) architecture, which seems less compatible with longer sequence lengths. A clear avenue of future work would therefore be to get the “best of both worlds”: long sequences and benefits of random-mask pre-training by using a GPT-like architectures, with our random-mask and finetune training regimes. This requires finding ways to make GPT act like a bidirectional model. Recent methods in NLP might offer a useful starting point [ 1 , 15 ] , as has been explored by concurrent work to ours [ 27 ] .

Comparison to other applications of masked prediction and sequence models for sequential decision making. In concurrent work, MaskDP [ 27 ] has also applied masked prediction to sequential decision-making. Similarly to Uni​ [MASK] , MaskDP pre-trains a bidirectional transformer to predict randomly-masked token sequences corresponding to states and actions in a Markovian decision process. The main difference between our works is that we are more interested in comparing the performance between different training regimes, and testing the performance limits of having a single set of weights to perform a large variety of tasks out of the box. MaskDP instead focuses on getting the best performance possible on a smaller subset of classic tasks (e.g. having separate architecture choices for RL). Future work could more systematically investigate the differences in our methods, e.g. how the MaskDP encoder-decoder architecture fares on multi-task performance as measured in our work. In addition, other architectural choices could be explored: in order to speed up training time efficiency, one could try to substitute BERT for XLNet or NADE-style approaches [ 44 , 40 ] . Finally, another exciting direction for future work is determining whether the benefits obtained from random-mask (or even multi-task ) apply to other types of inferences more generally (e.g. Bayes Networks); alternatively, even trivially extending the approach to multi-agent settings (for which token-stacking could prove more valuable), could enable interesting masking-enabled queries [ 29 ] .

## 7 Conclusion

Broader impacts. The prospect of very large “foundation models” [ 2 ] becoming the norm for sequential problems (in addition to language) raises concerns, in that it de-democratizes development and usage [ 23 ] . We use significantly smaller models and computational power than similar works, leaving open the option to have more modestly-sized environment-specific foundation models. However, we acknowledge that this works still encourages this trend.

Summary. In this work we propose Uni​ [MASK] , a framework for flexibly defining and training models which: 1) are naturally able to represent any inference task and support multi-task training in sequential decision problems, 2) match or surpass the performance of the corresponding single-task models after multi-task pre-training, and almost always surpasses them after fine-tuning.

## Acknowledgments and Disclosure of Funding

We’d like to thank Miltos Allamanis, Panagiotis Tigas, Kevin Lu, Scott Emmons, Cassidy Laidlaw, and the members of the Deep Reinforcement Learning for Games team (MSR Cambridge), the Center for Human-Compatible AI, and the InterAct Lab for helpful discussions at various stages of the project. We also thank anonymous reviewers for their helpful comments. This work was partially supported by Open Philanthropy and NSF CAREER.

## References

[1] Armen Aghajanyan, Bernie Huang, Candace Ross, Vladimir Karpukhin, Hu Xu, Naman Goyal, Dmytro Okhonko, Mandar Joshi, Gargi Ghosh, Mike Lewis, and Luke Zettlemoyer. CM3: A causal masked multimodal model of the internet. CoRR , abs/2201.07520, 2022. URL https://arxiv.org/abs/2201.07520 .

[2] Rishi Bommasani, Drew A. Hudson, Ehsan Adeli, Russ Altman, Simran Arora, Sydney von Arx, Michael S. Bernstein, Jeannette Bohg, Antoine Bosselut, Emma Brunskill, Erik Brynjolfsson, Shyamal Buch, Dallas Card, Rodrigo Castellon, Niladri S. Chatterji, Annie S. Chen, Kathleen Creel, Jared Quincy Davis, Dorottya Demszky, Chris Donahue, Moussa Doumbouya, Esin Durmus, Stefano Ermon, John Etchemendy, Kawin Ethayarajh, Li Fei-Fei, Chelsea Finn, Trevor Gale, Lauren Gillespie, Karan Goel, Noah D. Goodman, Shelby Grossman, Neel Guha, Tatsunori Hashimoto, Peter Henderson, John Hewitt, Daniel E. Ho, Jenny Hong, Kyle Hsu, Jing Huang, Thomas Icard, Saahil Jain, Dan Jurafsky, Pratyusha Kalluri, Siddharth Karamcheti, Geoff Keeling, Fereshte Khani, Omar Khattab, Pang Wei Koh, Mark S. Krass, Ranjay Krishna, Rohith Kuditipudi, and et al. On the opportunities and risks of foundation models. CoRR , abs/2108.07258, 2021. URL https://arxiv.org/abs/2108.07258 .

[3] Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei. Language models are few-shot learners. In Hugo Larochelle, Marc’Aurelio Ranzato, Raia Hadsell, Maria-Florina Balcan, and Hsuan-Tien Lin, editors, Advances in Neural Information Processing Systems 33: Annual Conference on Neural Information Processing Systems 2020, NeurIPS 2020, December 6-12, 2020, virtual , 2020. URL https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html .

[4] Micah Carroll, Orr Paradise, Jessy Lin, Raluca Georgescu, Mingfei Sun, David Bignell, Stephanie Milani, Katja Hofmann, Matthew Hausknecht, Anca Dragan, and Sam Devlin. Codebase for “Uni[MASK]: Unified Inference in Sequential Decision Problems”. https://github.com/micahcarroll/uniMASK , 2022. URL https://github.com/micahcarroll/uniMASK .

[5] Huiwen Chang, Han Zhang, Lu Jiang, Ce Liu, and William T. Freeman. MaskGIT: Masked generative image transformer. In IEEE/CVF Conference on Computer Vision and Pattern Recognition, CVPR 2022, New Orleans, LA, USA, June 18-24, 2022 , pages 11305–11315. IEEE, 2022. doi: 10.1109/CVPR52688.2022.01103 . URL https://doi.org/10.1109/CVPR52688.2022.01103 .

[6] Chang Chen, Yi-Fu Wu, Jaesik Yoon, and Sungjin Ahn. TransDreamer: Reinforcement learning with transformer world models. CoRR , abs/2202.09481, 2022. URL https://arxiv.org/abs/2202.09481 .

[7] Lili Chen, Kevin Lu, Aravind Rajeswaran, Kimin Lee, Aditya Grover, Michael Laskin, Pieter Abbeel, Aravind Srinivas, and Igor Mordatch. Decision Transformer: Reinforcement learning via sequence modeling. In Marc’Aurelio Ranzato, Alina Beygelzimer, Yann N. Dauphin, Percy Liang, and Jennifer Wortman Vaughan, editors, Advances in Neural Information Processing Systems 34: Annual Conference on Neural Information Processing Systems 2021, NeurIPS 2021, December 6-14, 2021, virtual , pages 15084–15097, 2021. URL https://proceedings.neurips.cc/paper/2021/hash/7f489f642a0ddb10272b5c31057f0663-Abstract.html .

[8] Maxime Chevalier-Boisvert, Lucas Willems, and Suman Pal. Minimalistic gridworld environment for openai gym. https://github.com/maximecb/gym-minigrid , 2018.

[9] Paul F. Christiano, Zain Shah, Igor Mordatch, Jonas Schneider, Trevor Blackwell, Joshua Tobin, Pieter Abbeel, and Wojciech Zaremba. Transfer from simulation to real world through learning deep inverse dynamics model. CoRR , abs/1610.03518, 2016. URL http://arxiv.org/abs/1610.03518 .

[10] Henry M. Clever, Ankur Handa, Hammad Mazhar, Kevin Parker, Omer Shapira, Qian Wan, Yashraj S. Narang, Iretiayo Akinola, Maya Cakmak, and Dieter Fox. Assistive Tele-op: Leveraging transformers to collect robotic task demonstrations. CoRR , abs/2112.05129, 2021. URL https://arxiv.org/abs/2112.05129 .

[11] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. BERT: pre-training of deep bidirectional transformers for language understanding. In Jill Burstein, Christy Doran, and Thamar Solorio, editors, Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, NAACL-HLT 2019, Minneapolis, MN, USA, June 2-7, 2019, Volume 1 (Long and Short Papers) , pages 4171–4186. Association for Computational Linguistics, 2019. doi: 10.18653/v1/n19-1423 . URL https://doi.org/10.18653/v1/n19-1423 .

[12] Yiming Ding, Carlos Florensa, Pieter Abbeel, and Mariano Phielipp. Goal-conditioned imitation learning. In Hanna M. Wallach, Hugo Larochelle, Alina Beygelzimer, Florence d’Alché-Buc, Emily B. Fox, and Roman Garnett, editors, Advances in Neural Information Processing Systems 32: Annual Conference on Neural Information Processing Systems 2019, NeurIPS 2019, December 8-14, 2019, Vancouver, BC, Canada , pages 15298–15309, 2019. URL https://proceedings.neurips.cc/paper/2019/hash/c8d3a760ebab631565f8509d84b3b3f1-Abstract.html .

[13] Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, Jakob Uszkoreit, and Neil Houlsby. An image is worth 16x16 words: Transformers for image recognition at scale. In 9th International Conference on Learning Representations, ICLR 2021, Virtual Event, Austria, May 3-7, 2021 . OpenReview.net, 2021. URL https://openreview.net/forum?id=YicbFdNTTy .

[14] Scott Emmons, Benjamin Eysenbach, Ilya Kostrikov, and Sergey Levine. Rvs: What is essential for offline RL via supervised learning? In The Tenth International Conference on Learning Representations, ICLR 2022, Virtual Event, April 25-29, 2022 . OpenReview.net, 2022. URL https://openreview.net/forum?id=S874XAIpkR- .

[15] Daniel Fried, Armen Aghajanyan, Jessy Lin, Sida Wang, Eric Wallace, Freda Shi, Ruiqi Zhong, Wen-tau Yih, Luke Zettlemoyer, and Mike Lewis. Incoder: A generative model for code infilling and synthesis. CoRR , abs/2204.05999, 2022. doi: 10.48550/arXiv.2204.05999 . URL https://doi.org/10.48550/arXiv.2204.05999 .

[16] Justin Fu, Aviral Kumar, Ofir Nachum, George Tucker, and Sergey Levine. D4RL: datasets for deep data-driven reinforcement learning. CoRR , abs/2004.07219, 2020. URL https://arxiv.org/abs/2004.07219 .

[17] Hiroki Furuta, Yutaka Matsuo, and Shixiang Shane Gu. Generalized decision transformer for offline hindsight information matching. In The Tenth International Conference on Learning Representations, ICLR 2022, Virtual Event, April 25-29, 2022 . OpenReview.net, 2022. URL https://openreview.net/forum?id=CAjxVodl_v .

[18] David Ha and Jürgen Schmidhuber. World models. CoRR , abs/1803.10122, 2018. URL http://arxiv.org/abs/1803.10122 .

[19] Kaiming He, Xinlei Chen, Saining Xie, Yanghao Li, Piotr Dollár, and Ross B. Girshick. Masked autoencoders are scalable vision learners. In IEEE/CVF Conference on Computer Vision and Pattern Recognition, CVPR 2022, New Orleans, LA, USA, June 18-24, 2022 , pages 15979–15988. IEEE, 2022. doi: 10.1109/CVPR52688.2022.01553 . URL https://doi.org/10.1109/CVPR52688.2022.01553 .

[20] L’eonard Hussenot, Marcin Andrychowicz, Damien Vincent, Robert Dadashi, Anton Raichuk, Lukasz Stafiniak, Sertan Girgin, Raphaël Marinier, Nikola Momchev, Sabela Ramos, Manu Orsini, Olivier Bachem, Matthieu Geist, and Olivier Pietquin. Hyperparameter selection for imitation learning. In ICML , 2021.

[21] Michael Janner, Qiyang Li, and Sergey Levine. Offline reinforcement learning as one big sequence modeling problem. In Marc’Aurelio Ranzato, Alina Beygelzimer, Yann N. Dauphin, Percy Liang, and Jennifer Wortman Vaughan, editors, Advances in Neural Information Processing Systems 34: Annual Conference on Neural Information Processing Systems 2021, NeurIPS 2021, December 6-14, 2021, virtual , pages 1273–1286, 2021. URL https://proceedings.neurips.cc/paper/2021/hash/099fe6b0b444c23836c4a5d07346082b-Abstract.html .

[22] Leslie Pack Kaelbling. Learning to achieve goals. In Ruzena Bajcsy, editor, Proceedings of the 13th International Joint Conference on Artificial Intelligence. Chambéry, France, August 28 - September 3, 1993 , pages 1094–1099. Morgan Kaufmann, 1993.

[23] Pratyusha Kalluri. Don’t ask if artificial intelligence is good or fair, ask how it shifts power. Nature , 583(7815):169–169, July 2020. doi: 10.1038/d41586-020-02003-2 . URL https://doi.org/10.1038/d41586-020-02003-2 .

[24] Kuang-Huei Lee, Ofir Nachum, Mengjiao Yang, Lisa Lee, Daniel Freeman, Winnie Xu, Sergio Guadarrama, Ian Fischer, Eric Jang, Henryk Michalewski, and Igor Mordatch. Multi-game decision transformers. CoRR , abs/2205.15241, 2022. doi: 10.48550/arXiv.2205.15241 . URL https://doi.org/10.48550/arXiv.2205.15241 .

[25] Sergey Levine, Aviral Kumar, George Tucker, and Justin Fu. Offline reinforcement learning: Tutorial, review, and perspectives on open problems. CoRR , abs/2005.01643, 2020. URL https://arxiv.org/abs/2005.01643 .

[26] Yoav Levine, Barak Lenz, Opher Lieber, Omri Abend, Kevin Leyton-Brown, Moshe Tennenholtz, and Yoav Shoham. PMI-Masking: Principled masking of correlated spans. In 9th International Conference on Learning Representations, ICLR 2021, Virtual Event, Austria, May 3-7, 2021 . OpenReview.net, 2021. URL https://openreview.net/forum?id=3Aoft6NWFej .

[27] Fangchen Liu, Hao Liu, Aditya Grover, and Pieter Abbeel. Masked autoencoding for scalable and generalizable decision making. In Advances in Neural Information Processing Systems 36: Annual Conference on Neural Information Processing Systems 2022, NeurIPS 2022, November, 2022, New Orleans, LA, USA , 2022.

[28] Elman Mansimov, Alex Wang, and Kyunghyun Cho. A generalized framework of sequence generation with application to undirected sequence models. CoRR , abs/1905.12790, 2019. URL http://arxiv.org/abs/1905.12790 .

[29] Jiquan Ngiam, Benjamin Caine, Vijay Vasudevan, Zhengdong Zhang, Hao-Tien Lewis Chiang, Jeffrey Ling, Rebecca Roelofs, Alex Bewley, Chenxi Liu, Ashish Venugopal, David Weiss, Benjamin Sapp, Zhifeng Chen, and Jonathon Shlens. Scene transformer: A unified multi-task model for behavior prediction and planning. CoRR , abs/2106.08417, 2021. URL https://arxiv.org/abs/2106.08417 .

[30] Emilio Parisotto, H. Francis Song, Jack W. Rae, Razvan Pascanu, Çaglar Gülçehre, Siddhant M. Jayakumar, Max Jaderberg, Raphaël Lopez Kaufman, Aidan Clark, Seb Noury, Matthew M. Botvinick, Nicolas Heess, and Raia Hadsell. Stabilizing transformers for reinforcement learning. In Proceedings of the 37th International Conference on Machine Learning, ICML 2020, 13-18 July 2020, Virtual Event , volume 119 of Proceedings of Machine Learning Research , pages 7487–7498. PMLR, 2020. URL http://proceedings.mlr.press/v119/parisotto20a.html .

[31] Deepak Pathak, Pulkit Agrawal, Alexei A. Efros, and Trevor Darrell. Curiosity-driven exploration by self-supervised prediction. In Doina Precup and Yee Whye Teh, editors, Proceedings of the 34th International Conference on Machine Learning, ICML 2017, Sydney, NSW, Australia, 6-11 August 2017 , volume 70 of Proceedings of Machine Learning Research , pages 2778–2787. PMLR, 2017. URL http://proceedings.mlr.press/v70/pathak17a.html .

[32] Dean Pomerleau. Efficient training of artificial neural networks for autonomous navigation. Neural Comput. , 3(1):88–97, 1991. doi: 10.1162/neco.1991.3.1.88 . URL https://doi.org/10.1162/neco.1991.3.1.88 .

[33] Alec Radford, Karthik Narasimhan, Tim Salimans, and Ilya Sutskever. Improving language understanding by generative pre-training. https://openai.com/blog/language-unsupervised/ , 2018.

[34] Gabriel Recchia. Teaching autoregressive language models complex tasks by demonstration. CoRR , abs/2109.02102, 2021. URL https://arxiv.org/abs/2109.02102 .

[35] Scott E. Reed, Konrad Zolna, Emilio Parisotto, Sergio Gomez Colmenarejo, Alexander Novikov, Gabriel Barth-Maron, Mai Gimenez, Yury Sulsky, Jackie Kay, Jost Tobias Springenberg, Tom Eccles, Jake Bruce, Ali Razavi, Ashley Edwards, Nicolas Heess, Yutian Chen, Raia Hadsell, Oriol Vinyals, Mahyar Bordbar, and Nando de Freitas. A generalist agent. CoRR , abs/2205.06175, 2022. doi: 10.48550/arXiv.2205.06175 . URL https://doi.org/10.48550/arXiv.2205.06175 .

[36] Nicholas Rhinehart, Rowan McAllister, Kris Kitani, and Sergey Levine. PRECOG: PREdiction conditioned on goals in visual multi-agent settings. In 2019 IEEE/CVF International Conference on Computer Vision, ICCV 2019, Seoul, Korea (South), October 27 - November 2, 2019 , pages 2821–2830. IEEE, 2019. doi: 10.1109/ICCV.2019.00291 . URL https://doi.org/10.1109/ICCV.2019.00291 .

[37] Ramanan Sekar, Oleh Rybkin, Kostas Daniilidis, Pieter Abbeel, Danijar Hafner, and Deepak Pathak. Planning to explore via self-supervised world models. In Proceedings of the 37th International Conference on Machine Learning, ICML 2020, 13-18 July 2020, Virtual Event , volume 119 of Proceedings of Machine Learning Research , pages 8583–8592. PMLR, 2020. URL http://proceedings.mlr.press/v119/sekar20a.html .

[38] Rohin Shah, Dmitrii Krasheninnikov, Jordan Alexander, Pieter Abbeel, and Anca D. Dragan. Preferences implicit in the state of the world. In 7th International Conference on Learning Representations, ICLR 2019, New Orleans, LA, USA, May 6-9, 2019 . OpenReview.net, 2019. URL https://openreview.net/forum?id=rkevMnRqYQ .

[39] Yi Tay, Mostafa Dehghani, Vinh Q. Tran, Xavier Garcia, Dara Bahri, Tal Schuster, Huaixiu Steven Zheng, Neil Houlsby, and Donald Metzler. Unifying language learning paradigms. CoRR , abs/2205.05131, 2022. doi: 10.48550/arXiv.2205.05131 . URL https://doi.org/10.48550/arXiv.2205.05131 .

[40] Benigno Uria, Marc-Alexandre Côté, Karol Gregor, Iain Murray, and Hugo Larochelle. Neural autoregressive distribution estimation. J. Mach. Learn. Res. , 17:205:1–205:37, 2016. URL http://jmlr.org/papers/v17/16-272.html .

[41] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin. Attention is all you need. In Isabelle Guyon, Ulrike von Luxburg, Samy Bengio, Hanna M. Wallach, Rob Fergus, S. V. N. Vishwanathan, and Roman Garnett, editors, Advances in Neural Information Processing Systems 30: Annual Conference on Neural Information Processing Systems 2017, December 4-9, 2017, Long Beach, CA, USA , pages 5998–6008, 2017. URL https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html .

[42] Alex Wang and Kyunghyun Cho. BERT has a mouth, and it must speak: BERT as a markov random field language model. CoRR , abs/1902.04094, 2019. URL http://arxiv.org/abs/1902.04094 .

[43] Mike Wu and Noah D. Goodman. Foundation posteriors for approximate probabilistic inference. CoRR , abs/2205.09735, 2022. doi: 10.48550/arXiv.2205.09735 . URL https://doi.org/10.48550/arXiv.2205.09735 .

[44] Zhilin Yang, Zihang Dai, Yiming Yang, Jaime G. Carbonell, Ruslan Salakhutdinov, and Quoc V. Le. XLNet: Generalized autoregressive pretraining for language understanding. In Hanna M. Wallach, Hugo Larochelle, Alina Beygelzimer, Florence d’Alché-Buc, Emily B. Fox, and Roman Garnett, editors, Advances in Neural Information Processing Systems 32: Annual Conference on Neural Information Processing Systems 2019, NeurIPS 2019, December 8-14, 2019, Vancouver, BC, Canada , pages 5754–5764, 2019. URL https://proceedings.neurips.cc/paper/2019/hash/dc6a7e655d7e5840e66733e9ee67cc69-Abstract.html .

[45] Eric Zhan, Albert Tseng, Yisong Yue, Adith Swaminathan, and Matthew J. Hausknecht. Learning calibratable policies using programmatic style-consistency. In Proceedings of the 37th International Conference on Machine Learning, ICML 2020, 13-18 July 2020, Virtual Event , volume 119 of Proceedings of Machine Learning Research , pages 11001–11011. PMLR, 2020. URL http://proceedings.mlr.press/v119/zhan20a.html .

[46] Brian D. Ziebart, Andrew L. Maas, J. Andrew Bagnell, and Anind K. Dey. Maximum entropy inverse reinforcement learning. In Dieter Fox and Carla P. Gomes, editors, Proceedings of the Twenty-Third AAAI Conference on Artificial Intelligence, AAAI 2008, Chicago, Illinois, USA, July 13-17, 2008 , pages 1433–1438. AAAI Press, 2008. URL http://www.aaai.org/Library/AAAI/2008/aaai08-227.php .

## Appendix A Code

Our codebase can be found in [ 4 ] . Our code uses assets from gym-minigrid [ 8 , Apache License 2.0] , Decision Transformer [ 7 , MIT License] , and D4RL [ 16 , Apache License 2.0] .

## Appendix B Training regimes

Each batch is made of many randomly sampled trajectory snippets. Across the tasks depicted in Figure 1 , for each snippet τ t : t + k \tau_{t:t+k} we describe the input masking and predicted outputs in detail:

• Behavioral Cloning. Select i ∈ [ 0 , k ] i\in[0,k] uniformly. Feed s t : t + i , a t : t + i − 1 s_{t:t+i},a_{t:t+i-1} to the network (include no actions if i = 0 i=0 ), with all other tokens masked out. Have the network only predict the next missing action a i a_{i} .

• Goal-Conditioned imitation. Same as BC, but s t + k s_{t+k} is always unmasked.

• Reward-Conditioned imitation (Offline-RL). Same as BC, but return-to-go R ^ t \hat{R}_{t} is always unmasked.

• Waypoint-Conditioned imitation. Same as BC, but a subset of intermediate states are always unmasked as waypoints or subgoals.

• Future inference. Same as BC, but the model is trained to predict all future states and actions, rather than only the next missing action.

• Past inference. Select i ∈ [ 1 , k ] i\in[1,k] uniformly. Feed s t + i : t + k , a t + i : t + k s_{t+i:t+k},a_{t+i:t+k} to the network, with all other tokens masked out. Have the network predict all previous states and actions s t : t + i − 1 , a t : t + i − 1 s_{t:t+i-1},a_{t:t+i-1} .

• Forward dynamics. Select i ∈ [ 0 , k − 1 ] i\in[0,k-1] uniformly. Give the network the current state and action s t + i , a t + i s_{t+i},a_{t+i} , and have it predict the next state s t + i + 1 s_{t+i+1} . In theory, this could enable to handle also non-Markovian dynamics (we did not test this).

• Inverse dynamics. Select i ∈ [ 1 , k ] i\in[1,k] uniformly. Give the network the current state and previous action s t + i , a t + i − 1 s_{t+i},a_{t+i-1} , and have it predict the previous state s t + i − 1 s_{t+i-1} .

• All the above (ALL). Randomly select one of the above masking schemes and apply it to the current sequence. This is a simple way of performing multi-task training.

• Random masking (RND). As we mention in section 3.1 , for each trajectory snippet, first, a masking probability p mask ∈ [ 0 , 1 ] p_{\textrm{mask}}\in[0,1] is sampled uniformly at random; then each state and action token is masked with probability p mask p_{\textrm{mask}} ; lastly, the first RTG token is masked with probability 1 / 2 1/2 and subsequent RTG tokens are masked always (see Appendix C for additional details). Randomly using the return-to-go in this fashion enables the model to perform both reward-conditioned and non-reward-conditioned tasks at inference time.

## Appendix C The random masking scheme

Given the significance of random-mask in our work, let us take a closer look at the choices made in constructing this masking scheme.

A straightforward randomized masking would be to simply mask each of the state and action tokens with some fixed probability (in other words, fixing p mask = p p_{\textrm{mask}}=p for some constant p p rather than sampling it from [ 0 , 1 ] [0,1] ). Indeed, this is a common masking scheme in NLP uses of BERT. However, in this scheme, the number of masked tokens is distributed as Binomial ​ ( k , p ) \textrm{Binomial}(k,p) where k k is the context length. Then, the probability of almost fully-masked (or fully-unmasking) a trajectory snipped is exponentially small in k k . This is an issue for us, since there are many meaningful tasks that require most tokens to be masked (past prediction) or unmasked (behavior cloning).

Our alternative distribution resolves this problem. In this distribution (described in the first paragraph of this subsection), the number of masked tokens is uniform in [ 0 , k ] [0,k] . 3 3 3 See, for example, https://math.stackexchange.com/q/282347 . In particular the tails are not exponentially small in k k . Empirically, we found that this distribution works much better than the straightforward distribution described in the previous paragraph.

## Appendix D Model architecture

Input stacking. An important hyperparameter for transformer models is what dimension to use self-attention over. Previous work applies it across states, actions, and rewards as separate tokens (or even individual state and action dimensions) [ 7 , 21 ] ; this can increase the effective sequence length that we would need to input a trajectory snippet of length k k : for example if treating states, actions, and rewards separately (have self-attention act on each independently), the sequence length would be 3 ​ k 3k . While this is not an issue for the short context windows we use in our experiments, this seems wasteful: the main bottleneck for transformer models is usually the computational cost of self-attention, which scales quadratically in the sequence length.

To obviate this problem, we stack states, actions, and rewards for each timestep, treating them as single inputs. This way, we are making self-attention happen only across timesteps, reducing the self-attention sequence length required to k k . This also seems like a potentially advantageous inductive bias for improving performance. Though we did not test this systematically, preliminary experiments did show that input stacking sometimes reduced validation loss.

Return-to-go conditioning.

Unlike previous work that considers return-to-go conditioning [ 7 ] , we do not provide the model with many return-to-go tokens (one for each timestep). Providing just the first token should be sufficient for the model to interpret the return-to-go request (as, if necessary, the model can compute the remaining return to go in later steps). We found that this reduced overfitting for both single-task reward-conditioned training, or for random-mask training.

Positional/timestep encoding.

When conditioning on return-to-go tokens (i.e. for reward-conditioning), it is fundamental for the model to have information about what the time-horizon the specified return-to-go should be achieved by. To provide the model with this information [ 7 ] uses a “timestep encoding” instead of the standard positional encoding used in transformers: this consists of adding information to each input token which allows the model to identify to which trajectory-timestep such tokens correspond to.

One large downside of this is that adding timestep information directly in this manner greatly increases the tendency of the model to overfit. To obviate this problem, we use positional encoding (which only provides the model with information about the relative position of each token within each trajectory snippet τ t : t + k \tau_{t:t+k} ). However, making the change to positional-encoding in isolation would remove trajectory-level timestep information from the return-to-go token (the problem that “timestep encoding” was introduced to solve). To address this, we change the form of the return-to-go token to a tuple containing return-to-go and the current timestep, and find this to work well in practice.

## Appendix E Minigrid experiments

Below we delineate some more details about our custom DoorKey Minigrid environment.

Training dataset.

We train Uni​ [MASK] models on training trajectories of sequence length T = 10 T=10 from a noisy-rational agent [ 46 ] which takes the optimal action most of the time, but has some chance of making mistakes proportional to their sub-optimality. More specifically, the agent takes the optimal action with probability a ∼ p ⁡ ( a ) ∝ exp ⁡ ( C ⁡ ( a ) ) a\sim p(a)\propto\exp(C(a)) where C ⁡ ( a ) = 1 C(a)=1 if the distance to the current goal (key or final goal) decreases, − 1 -1 if it increases, and 0 0 otherwise.

Environment.

The state and action spaces are both represented as discrete inputs: there are 4 actions, corresponding to the 4 possible movement directions (up, right, down, left); taking each action will move the agent in the corresponding direction unless 1) the agent is facing a wall, 2) the agent is facing the locked door without a key. Stepping on the key location tile picks up the key. The state is represented as two one-hot encoded position vectors—the agent position and the key position (which is equivalent to the agent position once the key has been picked up). Both agent and key position have 16 possible values, some of which are never seen in the data (e.g. the agent position coinciding with a wall location). Together, such vectors are sufficient to have full observability for the task—as seeing the key location coincide with the agent location informs the model that the agent is holding the key, and if the agent is holding the key it can open the locked door. Once the agent is holding the key, whether the door is open or closed is irrelevant.

Having the states and actions be discrete enables all model predictions to be done on a discrete space—which is particularly convenient as it enables the trained models to output any distribution over predicted states and actions, which can be easily visualized such as in Figure 6 .

As the DoorKey environment have discrete actions and states, we use the softmax-cross-entropy loss over all predictions.

Fixing prediction inconsistencies.

In backwards inference, we note that sometimes the predicted state at the previous timestep may not be consistent with the dynamics of the environment or the observed states. In cases where the prediction is inconsistent with environment dynamics, we re-sample the prediction (rejection sampling). In cases where the prediction is inconsistent with the observed variables, we simply return the trajectory even though it may not be consistent with the conditioned states, although rejection sampling could also have been performed here.

Hyperparameters.

For each model and task, hyperparameters were obtained with a random-search method, which sweeped over batch sizes ( 50,100 50,100 ), token embedding dimensions ( 32 32 , 64 64 , or 128 128 ), number of layers ( 2 2 , 3 3 , or 4 4 ), number of heads ( 4 4 , 8 8 , or 16 16 ), state loss re-scaling factors ( 1 1 , 0.5 0.5 , or 0.1 0.1 ), dropout ( 0 0 or 0.1 0.1 ), and learning rates (selected log uniformly between 10 − 5 10^{-5} and 10 − 3 10^{-3} ). With number of layers, we refer to attention layers for transformers, and hidden layers for feedforward models. Optimal hyperparameter choice is reported in Table 2 .

Each model was trained using the Torch implementation of the Adam optimizer. Training was performed over 6000 6000 epochs with early stopping over the validation loss. Action:State loss indicates the relative re-scaling of the losses of actions and state predictions: we found it to sometimes be useful to offset the larger loss values of state predictions relative to action predictions (due to their larger dimensionality).

Each finetune model used the same hyperparameters as its corresponding single-task model, with the learning rate lowered to 5 × 10 − 6 5\times 10^{-6} or 10 − 5 10^{-5} , and the number of epochs to 500 500 – 6000 6000 , depending on the task.

One thing to keep in mind is that while we search for hyperparameters which minimize the validation loss, this will not always correlate perfectly with reward, as showcased by prior work [ 20 ] .

Computational cost.

Models were trained and evaluated on an on-premise server. The server has 256 AMD EPYC 7763 64-Core CPUs and 8 NVIDIA RTX A4000 GPUs. Running the experiments necessary to generate each of the heatmaps in the “Detailed heatmaps” section of Appendix F took approximately ten hours. We were rarely able to fully utilize the server (since it is shared with other projects), but we estimate that with full parallelization the models and data for each heatmap would take roughly half an hour to generate.

## Appendix F Additional Minigrid experiments

State-action distributions on MiniGrid

We visualize the distribution of states and actions for trajectories sampled from the model, conditioned on the initial state (essentially, looking at the transition frequencies of BC-sampled trajectories). As seen in Figure 8 , the model learns to match the underlying distribution of trajectories of the agent (as can be verified by comparing to held-out data).

Detailed heatmaps

We report below more validation-loss results from the Minigrid experiments. This section expands on Figure 7 by adding comparison to two baseline models: Decision Transformers (DT), and Uni​ [MASK] model implemented with a Multi-layer Perceptron architecture (trained with the same maskings as our transformer). We also vary the amount of data used to train each model (50, 1000, and the original 500 number of trajectories). We see that notwithstanding the differences in dataset size, the trends and relative orderings of performance between models tend to stay the same.

All results are reported across six random seeds. All standard deviations are on the order of or smaller than 0.01 0.01 , except for about four cells (in each data regime) with especially high mean losses. See Figures 9 , 10 , 11 , 12 , 13 and 14 .

From these results, we see that using Decision Transformer in this context tends to slightly underperform relative to single-task Uni​ [MASK] models on the two tasks considered: Behavior Cloning and Reward-Conditioning. We also see that using an MLP architecture for one’s Uni​ [MASK] model leads to significantly worse performance than using our BERT-like transformer architecture: we suspect that this is due to the attention mechanism, which better lends itself to cleanly ignoring or using masked and unmasked information in the input.

Decision Transformer with BC training.

When reporting performance for Behavior Cloning using Decision Transformer (DT), we are training a DT model without inputting return-to-go information at training time. This ensures that the model should be trying to directly imitate the expert, rather than trying to achieve any specific reward. This is also the case for Appendix H .

## Appendix G Our Decision-GPT model

To obtain our Decision-GPT model, we use a standard GPT architecture (i.e. using a transformer decoder with causal self-attention), but incorporate the return-to-go and positional encoding design choices we used for Uni​ [MASK] models (which are described in Appendix D ). This is to form an improved baseline from a simple GPT model.

## Appendix H Maze2D experiments

Choice of environment.

We initially set out to compare the performance of Uni​ [MASK] on the same continuous control tasks used in [ 7 ] . However, after consulting with the authors of [ 7 ] , we decided not to use the classic Mujoco control environments and associated D4RL datasets [ 16 ] .

We list some of the issues with the D4RL datasets and classic control environments here: 1) given that the expert datasets were generated from Markovian policies and that these Mujoco environments are Markovian themselves, there is no direct reason for why sequence models should provide any benefit (although some benefit is observed in practice); 2) we noticed that completely overfitting a single trajectory with an MLP was sufficient for obtaining relatively good reward performance, indicating that such environments do not have enough inherent randomness to be a good indicator as to the generalization of trained policies – which is what we ultimately care about.

We tried to address these points in modifying the Maze2D environment. By choosing an environment in which the start and goal location are randomized, overfitting is not a viable strategy for generalization: memorizing a single trajectory in this setup leads to extremely poor performance.

As an additional detail, we modify the original environment reward to be dense, so that the reward at every timestep is given by the distance covered towards the goal.

See Figure 15 for example initializations of the environment.

Training.

As the Maze2D environment has continuous actions and states, we use an L2 loss over all predictions. Each model was trained using the Torch implementation of the Adam optimizer. Training was performed for 2000 2000 epochs with early stopping over the evaluation reward.

In reward-conditioned evaluation, choosing reasonable return-to-go (RTG) tokens on which to condition is non-trivial: asking for large reward in cases in which the goal is very close to the starting state leads to impossible-to-satisfy queries. Conversely, using the average reward as the goal return-to-go might be too conservative for easy initializations in which the point mass object can traverse most of the maze. To obviate this problem, we try to automatically determine what a reasonable RTG is at evaluation time using the following method: 1) reset the environment (leading to a random initial state); 2) find the trajectory in the dataset which has the most similar initial state (which also includes information about the goal location), and its total reward R R ; 3) Condition on an RTG of 1.1 × R 1.1\times R . We found this behaves as intended qualitatively.

Hyperparameters.

For each model and task, hyperparameters were obtained with a random-search method, which sweeped over batch sizes ( 50,100,200 50,100,200 ), token embedding dimensions ( 64,128 64,128 ), number of layers ( 2 2 , 3 3 , or 4 4 ), number of heads ( 8 8 , 16 16 ), state loss re-scaling factors ( 1 1 , 0.5 0.5 , 0 0 ), and learning rates (selected log uniformly between 10 − 5 10^{-5} and 10 − 3 10^{-3} ). With number of layers, we refer to attention layers for transformers, and hidden layers for feedforward models.

Given that we found little difference between various hyperparameters across model types, the same set of hyperparameters was used across all conditions. The final hyperparameters are as follows: 10 − 4 10^{-4} learning rate, 100 100 batch size, 128 128 embedding dimension, 4 4 layers, 16 16 attention heads, and a state loss re-scaling factor of 1 1 (equivalent to no re-scaling).

Similarly to the Minigrid experiments, each finetune model used the same hyperparameters as its corresponding single-task model, with the learning rate lowered to 8 × 10 − 5 8\times 10^{-5} , and the number of epochs lowered to 600 600 .

Computational cost.

We used the same compute infrastructure for our Maze2D experiments as in the Minigrid experiments (described in Appendix E ). A training run in Maze2D takes approximately 4 hours on our server, but more than 20 runs can be run in parallel. In total, running all runs for Table 1 should take on the order of 10 hours when using our setup in parallel.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
