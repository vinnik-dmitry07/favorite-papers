##### Report GitHub Issue

Content selection saved. Describe the issue below:

\DeclareCaptionType listing[Listing][List of Listings]

# From f ⁡ ( x ) f(x) and g ⁡ ( x ) g(x) to f ⁡ ( g ⁡ ( x ) ) f(g(x)) : LLMs Learn New Skills in RL by Composing Old Ones

###### Abstract

Does reinforcement learning (RL) teach large language models (LLMs) genuinely new skills, or does it merely activate existing ones? This question lies at the core of ongoing debates about the role of RL in LLM post-training. On one side, strong empirical results can be achieved with RL even without preceding supervised finetuning; on the other, critics argue that RL contributes little beyond reweighting existing reasoning strategies. This work provides concrete evidence that LLMs can acquire genuinely new skills during RL by composing existing ones, mirroring one of the central mechanisms by which humans acquire new cognitive skills ( Anderson, 1982 ) . To mitigate data contamination and other confounding factors, and to allow precise control over task complexity, we develop a synthetic framework for our investigation. Specifically, we define a skill as the ability to infer the output of a string transformation function f ⁡ ( x ) f(x) given x x . When an LLM has already learned f f and g g prior to RL, our experiments reveal that RL enables it to learn unseen compositions of them h ⁡ ( x ) = g ⁡ ( f ⁡ ( x ) ) h(x)=g(f(x)) . Further, this compositional ability generalizes to more difficult problems such as compositions of > 2 >2 functions unseen during RL training. Our experiments provide surprising evidence that this compositional ability, acquired on the source task, transfers to a different target task. This transfer occurs even though the model has never trained on any compositional problems in the target task, and the only requirement is that the model has acquired the target task’s atomic skills before its RL training on the source. Our qualitative analysis shows that RL fundamentally changes the reasoning behaviors of the models. In contrast, none of the findings is observed in next-token prediction training with the same data. Our systematic experiments provide fresh insights into the learning behaviors of widely-used post-training approaches for LLMs. They suggest the value of building base models with the necessary basic skills.

## 1 Introduction

Reinforcement learning (RL) has achieved broad success in improving large language models (LLMs) on a variety of tasks especially reasoning ( OpenAI, 2024 ; DeepMind, 2025 ) , even directly building upon the base model without any preceding supervised fine-tuning ( DeepSeek-AI et al., 2025 ) . Despite the profound success, recent work finds the exploration of RL is impeded by the entropy collapse phenomenon ( Cui et al., 2025b ; Liu et al., 2025a ; Yu et al., 2025 ) , and the performance gaps between base and RL-trained models diminish as the number of samples ( k k ) increases in pass@ k k evaluations ( Yue et al., 2025 ) . In addition, some argue that the “aha moments” in RL training ( OpenAI, 2024 ; DeepSeek-AI et al., 2025 ) are not emergent but merely the result of amplifying existing cognitive behaviors present in base models ( Gandhi et al., 2025 ; Liu et al., 2025b ; Zhao et al., 2025 ) , which casts shadow on whether LLMs learn new skills during RL training ( Wu et al., 2025a ) . Such observations diverge from established RL findings that predate LLMs, where models were trained from scratch and learned new skills ( Silver et al., 2016 ; Silver et al., 2017 ; OpenAI et al., 2019 ) . The fact that LLMs are pretrained on vast data prior to RL may contribute to these divergences and call for further investigation into the following important research questions: (1) Does RL teach new skills to LLMs? (2) If so, how to incentivize it? (3) Are the skills generalizable? Answering these questions will advance our understanding of LLM learning behaviors and inform the high-stakes trade-off in resource allocation between pretraining and post-training.

We provide concrete evidence that LLMs indeed learn new skills in RL, by composing and generalizing existing skills to solve more complex problems; For such learning to happen, there should be proper incentivization in RL. Our investigation is grounded in the cognitive skill acquisition process by humans, inspired by Anderson (1982) , which argues that humans learn new skills by composing and then internalizing existing ones. Unlike prior works ( Gandhi et al., 2025 ; Yue et al., 2025 ) , we choose to construct a controlled synthetic framework that facilitates: • Decontaminated evaluation : We design a string transformation prediction task with unique functions assigned meaningless identifiers (e.g., func_16 ) to prevent inference from function names. During RL, function definitions are hidden. The tasks will then be unsolvable without going through our atomic skills acquisition training. This setup enables us to investigate the RQs controlling for confounders.

• Well-defined atomic and compositional skills : We define atomic skills as single, non-decomposable transformations, and compositional skills as their nested combinations. For example, given input string x x , func_16( x x ) represents an atomic skill, while func_15(func_16( x x )) requires compositional reasoning.

• Controllable difficulty : As each skill is instantiated as a Python function, we control difficulty of composition through the depth of nesting. As shown in Fig. 1 , the model must perform deductive reasoning to give the output string after a given transformation, e.g., a Level-1 difficulty problem func_16( x x ) and a Level-2 one func_16(func_15( x x )) . Here the difficulty level is determined by the number of atomic functions composed.

With our framework and a two-stage training protocol that separates atomic from compositional skill acquisition, we conduct experiments with Llama-3.1-8B-Instruct ( Dubey et al., 2024 ) and answer the RQs as follows:

• RL teaches new compositional skills. RL on Level-2 problems, receiving only correctness-based outcome rewards without reasoning demonstrations, substantially improves generalization on more difficult problems: performance on unseen Level-3 tasks improves from near-zero to 30%, and Level-4 to 15%. This generalization does not occur in a baseline trained with rejection fine-tuning (RFT) on the same Level-2 problems. This shows that RL enables the acquisition of compositional skills.

• Both RL and compositional incentives are essential for skill acquisition. In contrast to the substantial accuracy improvements from RL on Level-2 compositional problems, RFT on the same data and RL on Level-1 atomic problems both yield little improvements on problems higher than Level-2 (e.g., less than 1% improvement at Level-3). This may explain why Sun et al. (2025) conclude that RL does not promote compositional generalization, as their training includes no explicit incentive for composition.

• The learning achieved by RL generalizes to held-out evaluation, more difficult problems, and even a different task. All findings above are based on held-out evaluation of compositional problems consisting of atomic skills (functions) unseen in RL training. And as aforementioned, models RL-trained on Level 2 problems show non-trivial gains on problems up to Level 4. For cross-task transfer, compositional RL on the string task boosts accuracy on the unseen Level-3 Countdown problems to 35% for a model with the prerequisite Countdown atomic skills.

Our findings challenge the recent view that current RL with verifiable rewards (RLVR) ( Lambert et al., 2025 ) merely utilizes reasoning patterns in base models rather than learning new reasoning abilities ( Yue et al., 2025 ; Wu et al., 2025a ) . This view is based on the observation that the pass@ k k performance gap between RL-trained and base models narrows as k k increases ( Yue et al., 2025 ) . We conjecture that this observation arises, at least in part, from evaluating and RL training on tasks where base models already achieve high pass@ k k , possibly due to pretraining on similar tasks that is beyond the control of most academic researchers; thus RL has little incentive to learn a skill that the base model already has. To confirm this conjecture, our experiments show that RL substantially improves pass@ k k on challenging compositional problems where base model’s pass@ k k is near zero (See Fig. 5 ). This reveals what we term the “reranking illusion,” namely aggregate metrics on mixed-difficulty benchmarks can mask genuine skill acquisition by conflating capabilities of different types. Our qualitative analysis confirms that RL fundamentally changes reasoning behavior. As shown in Fig. 6 , compositional errors, i.e., ignoring composition and misunderstanding function relationships, drop substantially, while failures shift primarily to atomic prediction errors (55%). This behavioral transformation indicates genuine acquisition of compositional skills.

Our findings have important implications for LLM development and highlight RL’s critical role in post-training, particularly its potential for easy-to-hard generalization and cross-task transfer. They call for closer coordination between base model development and post-training strategy from a skill acquisition perspective.

## 2 Background

The Recent Pessimistic View on Whether RL Teaches New Skills to LLMs . RL in LLMs builds on a model pretrained on vast data. While supervised warm-starts are a common technique in traditional RL ( Silver et al., 2016 ; Vinyals et al., 2019 ; De La Cruz Jr et al., 2019 ; Silva and Gombolay, 2021 ) , the large-scale and general-purpose nature of LLM creates a different scenario. On one hand, this strong prior enables base LLM to sample reasonable rollouts and thus perform RL directly without any preceding supervised fine-tuning ( DeepSeek-AI et al., 2025 ; Pan et al., 2025 ; Zeng et al., 2025 ) ; on the other hand, it becomes difficult to distinguish genuine skill acquisition from activation of existing capabilities during RL training.

Recent work tries to investigate this but uses loose definitions of “skill”, often relying on proxies such as the continually increasing frequency of certain reasoning patterns ( Gandhi et al., 2025 ; Zhao et al., 2025 ; Liu et al., 2025b ) or the diminishing gaps between the pass@ k k accuracy of models before and after RL, as shown in the bottom right chart in Fig. 1 ( Yue et al., 2025 ; Liu et al., 2025a ; Wu et al., 2025a ; He et al., 2025 ; Wen et al., 2025 ; Zhu et al., 2025 ) . Although these studies show that RL activates behaviors already present in the base model, they did not directly prove that no new skill is learned during the process. Moreover, the pass@ k k results can be misinterpreted for many reasons: (1) The causal relation between performance and each skill remains unclear, thus it is not guaranteed that everything learned can be translated into improvements in pass@ k k accuracy on downstream tasks. (2) The evaluation tasks only provide an obscure overall view, lacking fine-grained analysis on problems of different difficulty levels or domains. (3) The result is confounded by the possibility that the model has limited room or incentive to learn new skills if it already performs well prior to RL, especially when RL is conducted on data that overlaps with or closely resembles the data used during next-token prediction (NTP) training. ( Wu et al., 2025c ; Shao et al., 2025 ; Wang et al., 2025 ; Cui et al., 2025a ; Yu et al., 2025 ; Liu et al., 2025a ; Wu et al., 2025b ) . Together, these highlight the urgent need for a deeper analysis of tasks through a clean framework, in which the skills are clearly defined and contribute to the performance causally, and evaluated in a finer granularity.

Compositional Learning as a Testbed Grounded in Cognitive Skill Acquisition in Humans . Although the pessimistic conclusions about RL in LLMs from prior works are debatable, they at least indicate that the success of RL depends on strong base models. This motivates our study of skill composition, where RL learns new abilities by leveraging those already acquired by the base model. Compositional reasoning provides an ideal framework for investigating skill acquisition because it naturally separates atomic knowledge, which mirrors how humans learn cognitive skills ( Anderson, 1982 ) . Notably, it is established in cognitive science that both composed skills and the meta-ability to learn composition are non-trivial new skills ( Anderson, 1982 ; Lake et al., 2016 ) . For clarity, we refer to learning new skills as the former throughout this paper. Learning compositional skills helps the model to generalize to more challenging problems and new domains beyond training data, which we will show later. In the field of AI, compositional reasoning has been widely studied before LLMs and has been considered a necessary property of generalization. ( Fodor and Pylyshyn, 1988 ; Lake et al., 2016 ; Andreas et al., 2015 ) . More recently, Yin et al. (2025) achieved compositional improvements through in-context learning rather than RL, while Sun et al. (2025) found that directly RL in atomic skills fails in compositional generalization. Comparing the two works, we conjecture that an explicit incentive to composition is necessary.

## 3 Research Framework

In this work, we define “new skills” as novel reasoning strategies that enable models to solve previously unsolvable problems through systematic combination of existing capabilities. We address three critical research questions: (1) Does RL teach new skills to LLMs? (2) If so, how to incentivize it? (3) Are the learned skills generalizable?

###### Hypothesis 1 (The RL Compositionality Hypothesis) .

Once a model has acquired the necessary atomic, non-decomposable skills for a task through NTP training, RL with proper incentivization can teach the model to learn new skills by composing atomic skills into more complex capabilities.

### 3.1 Task Design: Deductive Reasoning on String Transformation Prediction

To test our hypothesis while avoiding confounders from data contamination and unclear skill boundaries, we design a controlled synthetic task with the following properties: (1) Atomic skills are well defined so that models can learn the fundamental skills separately before RL. Each string transformation function has clear, deterministic behaviors that can be learned independently. (2) Task difficulty can be controlled by adjusting the compositional complexity of the atomic skills, allowing us to test generalization across complexity levels. (3) RL and evaluation tasks do not appear in the LLM pretraining corpus, ensuring that improvements stem from learning rather than memorization.

Task Definition . Specifically, our task involves deductive reasoning on string transformations. Given an input string x x and a composition of deterministic transformation functions such as f ⁡ ( ⋅ ) f(\cdot) and g ⁡ ( ⋅ ) g(\cdot) , models must predict the output string after applying the specified transformation (e.g., y = f ⁡ ( g ⁡ ( x ) ) y=f(g(x)) ). We construct 25 unique string transformation functions as atomic skill spanning various computational patterns including character manipulation, reordering, filtering, and structural modifications (see Appendix § D for complete specifications). To mitigate potential contamination, we assign meaningless identifiers to string functions as shown in Fig. 1 , so that it is impossible to infer the functionality with function names only.

Difficulty Level . We control compositional complexity through Difficulty Levels corresponding to nesting depth, with Level n n involving n n -function composition. For instance, Level 1 involves single function application (e.g., func_16(x) as shown in Fig. 1 ), while Level 2 involves two-function composition (e.g., func_16(func_15(x)) ). The controlled difficulty provides a fine-grained inspection of model performance, rather than a vague overall number as adopted in prior work ( Yue et al., 2025 ; Liu et al., 2025a ; Wu et al., 2025a ) .

### 3.2 Training and Evaluation Protocol

Training consists of two stages to separate atomic skill acquisition from compositional skill learning, simulating realistic post-training pipelines.

Stage 1 Training: Atomic Skills Acquisition via RFT . Models learn “atomic skills” in this stage via rejection fine-tuning Dong et al. (2023) . Specifically, we collect training data by prompting the model with explicit function definitions to generate correct reasoning trajectories. However, we remove these definitions from the prompts during the fine-tuning process. This compels the model to predict the output based solely on the function identifier, ensuring it internalizes the function’s behavior, defined here as the atomic skill, rather than relying on in-context instructions. Crucially, the data collection phase of this stage is the only time models are exposed to the function implementations. An example can be found in Fig. 7 .

Stage 2 Training: Compositional Skill Training via Either RFT or RL . In this stage, models see only function names and compositions, such as func_2(func_16(x)) , with function definitions hidden. See Fig. 8 for examples. This forces reliance on internalized atomic knowledge while learning systematic composition. We compare two approaches: (1) Composition via online RL provides models with binary rewards based on output correctness and updates through Group Relative Preference Optimization (GRPO) Shao et al. (2024) , testing whether RL is necessary for the acquisition of compositional skills. (2) Composition via offline RFT trains models with NTP on correct reasoning trajectories for compositional problems, serving as a baseline to examine whether exposure to compositional examples alone enables composition.

We use Llama-3.1-8B-Instruct, which is identified as a cleaner testbed for RL by recent work ( Shao et al., 2025 ; Agarwal et al., 2025 ; Wu et al., 2025b ) , to further minimize the effect of data contamination besides our string tasks. For more details, please refer to Appendix A .

Held-out, Easy-to-Hard, and Cross-Task Evaluation . We assess generalization using rigorous held-out evaluation. In Stage 1, models are trained on all 25 atomic functions (Appendix D ). In Stage 2, the functions are partitioned into two disjoint sets: the model trains only on compositions from one set, while the other is held out for evaluation. We test model generalization across various difficulty levels, using Countdown ( Gandhi et al., 2024 ; Pan et al., 2025 ) as a testbed for task transfer.

## 4 RL as a Pathway to Generalizable Skill Acquisition

### 4.1 LLMs Acquire New Compositional Skills during RL

Our first experiment directly test our RL Compositionality Hypothesis (Hypothesis 1 ). To do so, we start from an identical Stage 1 base model and apply three different Stage 2 training configurations, allowing us to isolate the impact of incentivizing composition during RL: (1) RL Level 1 , trained only on atomic tasks; (2) RL Level 2 , trained only on two-level compositions; and (3) RL Level 1+2 , trained on a uniform mix. We then evaluate their ability to generalize to held-out tasks from Level 1 up to Level 6, testing whether they can solve problems with unseen function compositions and higher nesting levels than seen in RL training.

As shown in blue curves in Fig. 2 , training on Level 1 alone leads to high accuracy on Level 1, peaking at around 90%, but fails to generalize. Its accuracy on Level 2 task remains below 25%, and on Level 3 through 6, it is consistently near zero . This demonstrates that learning only the atomic skills through RL is insufficient for learning effective composition.

In contrast, incorporating compositional tasks into RL training yields transformative results. Both the RL Level 2 and RL Level 1+2 models demonstrate strong performance to generalize to problems with nesting depths exceeding their training data. On Level 3, their accuracy improves from 5% to around 30%, and from 1% to 15% on Level 4, which are all significant improvements over the RL Level 1 model. And this trend continues on even Level 5, indicating both models learn a generalizable principle of compositional reasoning rather than merely memorizing solutions. This validates our hypothesis that RL can teach genuinely new skills, but only when the training objective explicitly incentivizes their use. These results provide us with evidence to answer RQ1:

### 4.2 RL is the Key Ingredient to the New Compositional Skills

Our previous experiment shows that compositional data is necessary for RL to teach new compositional skills, but can a supervised method, such as RFT, achieve the same results as RL when given the exact same compositional (Level 2) data? To address this question, we train a model with iterative RFT on the same Level 2 problems and conduct a head-to-head comparison against the RL Level 2 model from § 4.1 , with both having started from the identical Stage 1 base model.

The results in Fig. 3 show a significant difference in performance from Fig. 2 . The RFT model’s accuracy is significantly worse than RL across all compositional levels and has only marginal improvement over the first iteration. For example, on Level 3 it never surpasses 2.6%. In contrast, the RL Level 2 model achieves 64% on Level 2 and 27% on Level 3, significantly outperforming the RFT model. Surprisingly, the RFT model attains only 15% accuracy on Level-2 problems. This indicates that RFT fails to generalize even to held-out compositional problems of the same difficulty as its training data, let alone higher difficulties. These results provide the evidence to answer RQ2:

### 4.3 Compositional Skills Learned in RL are Transferable, but Atomic Skills are Prerequisites

While our experiments demonstrate that RL can teach generalizable compositional skills within a task, collecting compositional RL data for every new domain is impractical. We therefore test the transferability of the learned compositional skill. Specifically, we conjecture that RL enables models to compose atomic skills on Task B after learning composition on Task A, if the model has already acquired the necessary atomic skills for Task B.

Experimental Setup. We test this conjecture on the Countdown task, where a model must construct a mathematical expression from a given set of integers to reach a target number (see § E for examples). In Countdown, a Level ℓ \ell task requires the model to construct a mathematical expression using ℓ \ell given integers to reach a target number. The minimum level for Countdown is Level 2. We compare four models to test our hypothesis, as detailed in Tab. 1 . These configurations allow us to compare a “atomic-skill-only” baseline (Multi-Base) against models with either transferred atomic RL (Multi-Base + RL L1) or transferred compositional RL (Multi-Base + RL L1+2), as well as a control model from § 4.1 that has the compositional skill but lacks the necessary atomic knowledge of Countdown (String-Base + RL L1+2). Note that none of the models are trained on Countdown with RL in Stage 2, and are only trained on our string task.

We evaluate these models on unseen, more challenging Countdown problems (Levels 3-5). We report the Avg@32, the average accuracy across 32 responses sampled at temperature 1.0.

Results. The results in Fig. 4 provide clear evidence supporting our hypothesis. The String-Base + RL L1+2 model fails completely. The Multi-Base model achieves reasonable accuracy of approximately 17% at Level 3 but still struggles at higher levels. Multi-Base + RL L1 shows marginal improvement over Multi-Base, increasing accuracy to around 20% at Level 3, with the advantage diminishing on more complex problems. The Multi-Base + RL L1+2 model achieves surprisingly strong performance. It achieves a 35% accuracy at Level 3, outperforming the Multi-Base baseline by more than 18% accuracy. This advantage persists at higher complexities, reaching approximately 6% at Level 4, where other models largely fail and achieve near-zero accuracy. The results show that the compositional skill learned from string transformation transfers to countdown, acting as a meta-skill that enhances the use of the target task’s atomic knowledge. Finally, the comparison between Multi-base + RL and String-Base + RL L1+2 confirms our fundamental assumption that task-specific atomic skills are prerequisites for compositional skills to be effective.

These results may explain recent findings on generalizable RL improvements. For example, Logic-RL ( Xie et al., 2025 ) reports performance gains on mathematical problems after training on logic puzzles, and Guru ( Cheng et al., 2025 ) shows that domains with greater pre-training exposure benefit more from cross-task generalization. We suggest that LLMs have already acquired essential atomic skills through large-scale pre-training, particularly in mathematics and coding. Thus, incentivizing compositional skills through RL in one task helps combine task-specific skills more effectively across domains. In contrast, domains with less pre-training exposure may lack sufficient atomic skills, limiting compositional skill transfer to downstream tasks. With this finding, we answer RQ3:

### 4.4 RL Expanding Performance Limits is Not a False Promise

Our findings strongly suggest that RL can teach compositional skills that are novel to the base model. This directly challenges recent arguments that RL merely “reranks” model responses, distilling pass@ k k performance of the base model into pass@ 1 1 ( Yue et al., 2025 ; Wu et al., 2025a ) . This conclusion is drawn based on a shrinking pass@ k k performance gap between base and RL-tuned models as k k increases. However, we argue this conclusion may stem from two issues: (1) evaluating on mixed-skill benchmarks, therefore an improvement in a specific skill, like composition, can be masked in pass@ k k if other required skills remain a bottleneck, and (2) using RL training that does not properly incentivize the new skill in the first place.

Our controlled framework allows us to dissect both issues. By isolating the compositional skill at varying difficulty levels, we can reliably assess skill acquisition (addressing issue 1), and by comparing different RL training setups (§ 4.1 ), we can test the effect of proper incentivization (addressing issue 2). We compare pass@ 1000 1000 performance at each difficulty level of our test set, selecting k = 1000 k=1000 as a sufficiently large and practically meaningful budget. Larger budgets would become impractical, as any reasonable model could theoretically achieve pass@ ∞ = 1 \infty=1 .

The results are presented in Fig. 5 . Both RL Level 1 and RL Level 1+2 models are trained from RFT base model using RL in Stage 2. The RL Level 1 model, which is not incentivized properly to learn composition, exhibits a similar trend to the RFT base across almost all levels. On easier problems (Levels 1 and 2) where the RFT base model already shows solving potential evidenced by high pass@k, the performance gaps between RL Level 1+2 model and the RFT model shrink as k k increases, aligning with the trends observed in Yue et al. (2025) ; Wu et al. (2025a) . However, a completely different trend is observed on more challenging compositional problems (Levels 3-6). The RL Level 1+2 model’s performance substantially outperforms the RFT base with an increasing gap as k k grows. For example, at Level 5, the performance gap over the RFT base grows from 4% at pass@1 to approximately 25% at pass@1024. This divergence is clear evidence of new skill acquisition. The results suggest that the pessimistic observation of “RL does not push performance limits” in prior work may be explained by the lack of incentive for RL to learn new skills, as the base model already achieves high pass@k performance.

### 4.5 Behavioral Analysis: RL Transforms Failure Modes

While our results show that training with compositional data unlocks promising generalization, a fundamental question remains: do models trained under different setups exhibit different behaviors, or do they simply differ in capability while showing similar failure modes? To investigate this, we analyze the failure modes of different models on Level 3 problems of our string task.

We use Gemini-2.5-Pro to classify responses into five categories: (1) Correct , (2) Ignores Composition (e.g., analyzing only a single function), (3) Incomplete Trace (recognizes composition but terminates early), (4) Incorrect Composition (e.g., misinterprets nesting), and (5) Atomic Error (errors in atomic functions prediction without the above). Categories 2-4 indicate difficulties with handling compositional problems. And while still incorrect, category 5 represents appropriate compositional behavior, as the error is not due to a lack of compositional skill.

We compare four models: RFT Base (after Stage 1 training), RFT Level 2 (after Stage 2 training on Level 2 problems with RFT), RL Level 1 , and RL Level 2 , all from previous sections. The latter three models are all trained from the RFT Base.

Fig. 6 reveals substantial similarities in the failure patterns of RFT Base, RFT Level 2, and RL Level 1 models. Their failures are dominated by ignoring the composition entirely (all > > 50%) and misunderstanding the compositional structure (all > > 35%).

In contrast, the RL Level 2 model demonstrates fundamentally different behaviors. It completely eliminates ”Ignores Composition” errors and correctly solves 28.1% of the problems. Crucially, its primary failure mode becomes “Atomic Error.” This shows that compositional RL not only improves accuracy but teaches models to parse and execute compositional plans, shifting failures from high-level misunderstandings to lower-level execution errors. See § F for examples of different model responses.

## 5 Conclusion

The debate over whether RL can teach LLMs new skills has been clouded by experiments on benchmarks where LLMs already perform well, using coarse-grained metrics that obscure the learning of new capabilities. By stepping back to a cleaner, more controllable experimental environment, our findings provide a clear and optimistic answer: RL can teach genuinely new and powerful skills when the training task properly incentivize composition.

Our work focuses on the paradigm where RL acts upon pre-existing atomic competencies, mirroring the standard practice of carrying out RL based on pre-trained models. While our results show that possessing atomic skills is a sufficient condition for RL to unlock compositional capabilities, we do not claim it is strictly necessary. However, given the inefficiency of random exploration in discovering complex atomic behaviors from scratch, we argue that the synergy between supervised learning for atomic skill acquisition and RL for compositional generalization represents the most commonly adopted and promising path. Our findings suggest that the pessimistic conclusion that RL does not learn new skills may stem from inappropriate evaluation setups rather than fundamental constraints of RL itself. Future work may investigate the open question of whether RL can be scaled to acquire both atomic and compositional skills simultaneously without supervised scaffolding.

## Limitation

One limitation of this work is the reliance on synthetic tasks for evaluation. We deliberately designed our string transformation framework to enable rigorous experiments with well-defined atomic and compositional skills, thus isolating causal learning mechanisms. However, our synthetic tasks may not fully capture the complexity and nuance of real-world reasoning scenarios where skills are less clearly delineated and compositional structures are more varied. We acknowledge that demonstrating these findings in natural reasoning domains, such as mathematical problem-solving, code generation, or scientific reasoning, represents an important direction for future work. Extending these findings to realistic applications remains a valuable open challenge.

## References

Agarwal et al. (2025) S. Agarwal, Z. Zhang, L. Yuan, J. Han, and H. Peng The unreasonable effectiveness of entropy minimization in llm reasoning . ArXiv abs/2505.15134 . External Links: Link Cited by: §3.2 .

Anderson (1982) J. R. Anderson Acquisition of cognitive skill . Psychological Review 89 . Cited by: §1 , §2 , Abstract .

Andreas et al. (2015) J. Andreas, M. Rohrbach, T. Darrell, and D. Klein Neural module networks . 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR) , pp. 39–48 . Cited by: §2 .

Cheng et al. (2025) Z. Cheng, S. Hao, T. Liu, F. Zhou, Y. Xie, F. Yao, Y. Bian, Y. Zhuang, N. Dey, Y. Zha, Y. Gu, K. Zhou, Y. Wang, Y. Li, R. Fan, J. She, C. Gao, A. Saparov, H. Li, T. W. Killian, M. Yurochkin, Z. Liu, E. P. Xing, and Z. Hu Revisiting reinforcement learning for LLM reasoning from A cross-domain perspective . CoRR abs/2506.14965 . External Links: Link , Document , 2506.14965 Cited by: §4.3 .

Cui et al. (2025a) G. Cui, L. Yuan, Z. Wang, H. Wang, W. Li, B. He, Y. Fan, T. Yu, Q. Xu, W. Chen, et al. Process reinforcement through implicit rewards . arXiv preprint arXiv:2502.01456 . Cited by: §2 .

Cui et al. (2025b) G. Cui, Y. Zhang, J. Chen, L. Yuan, Z. Wang, Y. Zuo, H. Li, Y. Fan, H. Chen, W. Chen, Z. Liu, H. Peng, L. Bai, W. Ouyang, Y. Cheng, B. Zhou, and N. Ding The entropy mechanism of reinforcement learning for reasoning language models . CoRR abs/2505.22617 . External Links: Link , Document , 2505.22617 Cited by: §1 .

De La Cruz Jr et al. (2019) G. V. De La Cruz Jr, Y. Du, and M. E. Taylor Pre-training with non-expert human demonstration for deep reinforcement learning . The Knowledge Engineering Review 34 , pp. e10 . Cited by: §2 .

DeepMind (2025) G. DeepMind Gemini 2.5: pushing the frontier with advanced reasoning, multimodality, long context, and next generation agentic capabilities . ArXiv abs/2507.06261 . Cited by: §1 .

DeepSeek-AI et al. (2025) DeepSeek-AI, D. Guo, D. Yang, H. Zhang, J. Song, R. Zhang, R. Xu, Q. Zhu, S. Ma, P. Wang, X. Bi, X. Zhang, X. Yu, Y. Wu, Z. F. Wu, Z. Gou, Z. Shao, Z. Li, Z. Gao, A. Liu, B. Xue, B. Wang, B. Wu, B. Feng, C. Lu, C. Zhao, C. Deng, C. Zhang, C. Ruan, D. Dai, D. Chen, D. Ji, E. Li, F. Lin, F. Dai, F. Luo, G. Hao, G. Chen, G. Li, H. Zhang, H. Bao, H. Xu, H. Wang, H. Ding, H. Xin, H. Gao, H. Qu, H. Li, J. Guo, J. Li, J. Wang, J. Chen, J. Yuan, J. Qiu, J. Li, J. Cai, J. Ni, J. Liang, J. Chen, K. Dong, K. Hu, K. Gao, K. Guan, K. Huang, K. Yu, L. Wang, L. Zhang, L. Zhao, L. Wang, L. Zhang, L. Xu, L. Xia, M. Zhang, M. Zhang, M. Tang, M. Li, M. Wang, M. Li, N. Tian, P. Huang, P. Zhang, Q. Wang, Q. Chen, Q. Du, R. Ge, R. Zhang, R. Pan, R. Wang, R. J. Chen, R. Jin, R. Chen, S. Lu, S. Zhou, S. Chen, S. Ye, S. Wang, S. Yu, S. Zhou, S. Pan, S. S. Li, S. Zhou, S. Wu, T. Yun, T. Pei, T. Sun, T. Wang, W. Zeng, W. Zhao, W. Liu, W. Liang, W. Gao, W. Yu, W. Zhang, W. Xiao, W. An, X. Liu, X. Wang, X. Chen, X. Nie, X. Cheng, X. Liu, X. Xie, X. Liu, X. Yang, X. Li, X. Su, X. Lin, X. Q. Li, X. Jin, X. Shen, X. Chen, X. Sun, X. Wang, X. Song, X. Zhou, X. Wang, X. Shan, Y. K. Li, Y. Q. Wang, Y. X. Wei, Y. Zhang, Y. Xu, Y. Li, Y. Zhao, Y. Sun, Y. Wang, Y. Yu, Y. Zhang, Y. Shi, Y. Xiong, Y. He, Y. Piao, Y. Wang, Y. Tan, Y. Ma, Y. Liu, Y. Guo, Y. Ou, Y. Wang, Y. Gong, Y. Zou, Y. He, Y. Xiong, Y. Luo, Y. You, Y. Liu, Y. Zhou, Y. X. Zhu, Y. Huang, Y. Li, Y. Zheng, Y. Zhu, Y. Ma, Y. Tang, Y. Zha, Y. Yan, Z. Ren, Z. Ren, Z. Sha, Z. Fu, Z. Xu, Z. Xie, Z. Zhang, Z. Hao, Z. Ma, Z. Yan, Z. Wu, Z. Gu, Z. Zhu, Z. Liu, Z. Li, Z. Xie, Z. Song, Z. Pan, Z. Huang, Z. Xu, Z. Zhang, and Z. Zhang DeepSeek-r1: incentivizing reasoning capability in llms via reinforcement learning . Nature 645 . Cited by: §1 , §2 .

Dong et al. (2023) H. Dong, W. Xiong, D. Goyal, R. Pan, S. Diao, J. Zhang, K. Shum, and T. Zhang RAFT: reward ranked finetuning for generative foundation model alignment . ArXiv abs/2304.06767 . Cited by: §3.2 .

Dubey et al. (2024) A. Dubey, A. Jauhri, A. Pandey, A. Kadian, A. Al-Dahle, A. Letman, A. Mathur, A. Schelten, A. Yang, A. Fan, A. Goyal, A. S. Hartshorn, A. Yang, A. Mitra, A. Sravankumar, A. Korenev, A. Hinsvark, A. Rao, A. Zhang, A. Rodriguez, A. Gregerson, A. Spataru, B. Rozière, B. Biron, B. Tang, B. Chern, C. Caucheteux, C. Nayak, C. Bi, C. Marra, C. McConnell, C. Keller, C. Touret, C. Wu, C. Wong, C. C. Ferrer, C. Nikolaidis, D. Allonsius, D. Song, D. Pintz, D. Livshits, D. Esiobu, D. Choudhary, D. Mahajan, D. Garcia-Olano, D. Perino, D. Hupkes, E. Lakomkin, E. A. AlBadawy, E. Lobanova, E. Dinan, E. M. Smith, F. Radenovic, F. Zhang, G. Synnaeve, G. Lee, G. L. Anderson, G. Nail, G. Mialon, G. Pang, G. Cucurell, H. Nguyen, H. Korevaar, H. Xu, H. Touvron, I. Zarov, I. A. Ibarra, I. M. Kloumann, I. Misra, I. Evtimov, J. Copet, J. Lee, J. Geffert, J. Vranes, J. Park, J. Mahadeokar, J. Shah, J. van der Linde, J. Billock, J. Hong, J. Lee, J. Fu, J. Chi, J. Huang, J. Liu, J. Wang, J. Yu, J. Bitton, J. Spisak, J. Park, J. Rocca, J. Johnstun, J. Saxe, J. Jia, K. V. Alwala, K. Upasani, K. Plawiak, K. Li, K. neth Heafield, K. R. Stone, K. El-Arini, K. Iyer, K. Malik, K. Chiu, K. Bhalla, L. Rantala-Yeary, L. van der Maaten, L. Chen, L. Tan, L. Jenkins, L. Martin, L. Madaan, L. Malo, L. Blecher, L. Landzaat, L. de Oliveira, M. Muzzi, M. Pasupuleti, M. Singh, M. Paluri, M. Kardas, M. Oldham, M. Rita, M. Pavlova, M. H. M. Kambadur, M. Lewis, M. Si, M. K. Singh, M. Hassan, N. Goyal, N. Torabi, N. Bashlykov, N. Bogoychev, N. S. Chatterji, O. Duchenne, O. cCelebi, P. Alrassy, P. Zhang, P. Li, P. Vasić, P. Weng, P. Bhargava, P. Dubal, P. Krishnan, P. S. Koura, P. Xu, Q. He, Q. Dong, R. Srinivasan, R. Ganapathy, R. Calderer, R. S. Cabral, R. Stojnic, R. Raileanu, R. Girdhar, R. Patel, R. Sauvestre, R. Polidoro, R. Sumbaly, R. Taylor, R. Silva, R. Hou, R. Wang, S. Hosseini, S. Chennabasappa, S. Singh, S. Bell, S. S. Kim, S. Edunov, S. Nie, S. Narang, S. C. Raparthy, S. Shen, S. Wan, S. Bhosale, S. Zhang, S. Vandenhende, S. Batra, S. Whitman, S. Sootla, S. Collot, S. Gururangan, S. Borodinsky, T. Herman, T. Fowler, T. Sheasha, T. Georgiou, T. Scialom, T. Speckbacher, T. Mihaylov, T. Xiao, U. Karn, V. Goswami, V. Gupta, V. Ramanathan, V. Kerkez, V. Gonguet, V. Do, V. Vogeti, V. Petrovic, W. Chu, W. Xiong, W. Fu, W. Meers, X. Martinet, X. Wang, X. E. Tan, X. Xie, X. Jia, X. Wang, Y. Goldschlag, Y. Gaur, Y. Babaei, Y. Wen, Y. Song, Y. Zhang, Y. Li, Y. Mao, Z. D. Coudert, Z. Yan, Z. Chen, Z. Papakipos, A. K. Singh, A. Grattafiori, A. Jain, A. Kelsey, A. Shajnfeld, A. Gangidi, A. Victoria, A. Goldstand, A. Menon, A. Sharma, A. Boesenberg, A. Vaughan, A. Baevski, A. Feinstein, A. Kallet, A. Sangani, A. Yunus, A. Lupu, A. Alvarado, A. Caples, A. Gu, A. Ho, A. Poulton, A. Ryan, A. Ramchandani, A. Franco, A. Saraf, A. Chowdhury, A. Gabriel, A. Bharambe, A. Eisenman, A. Yazdan, B. James, B. Maurer, B. Leonhardi, P. (. Huang, B. Loyd, B. de Paola, B. Paranjape, B. Liu, B. Wu, B. Ni, B. Hancock, B. Wasti, B. Spence, B. Stojkovic, B. Gamido, B. Montalvo, C. Parker, C. Burton, C. Mejia, C. Wang, C. Kim, C. Zhou, C. Hu, C. Chu, C. Cai, C. Tindal, C. Feichtenhofer, D. Civin, D. Beaty, D. Kreymer, S. Li, D. Wyatt, D. Adkins, D. Xu, D. Testuggine, D. David, D. Parikh, D. Liskovich, D. Foss, D. Wang, D. Le, D. Holland, E. Dowling, E. Jamil, E. Montgomery, E. Presani, E. Hahn, E. Wood, E. Brinkman, E. Arcaute, E. Dunbar, E. Smothers, F. Sun, F. Kreuk, F. Tian, F. Ozgenel, F. Caggioni, F. Guzm’an, F. J. Kanayet, F. Seide, G. M. Florez, G. Schwarz, G. Badeer, G. Swee, G. Halpern, G. Thattai, G. Herman, G. G. Sizov, G. Zhang, G. Lakshminarayanan, H. Shojanazeri, H. Zou, H. Wang, H. Zha, H. Habeeb, H. Rudolph, H. Suk, H. Aspegren, H. Goldman, I. Molybog, I. Tufanov, I. Veliche, I. Gat, J. Weissman, J. Geboski, J. Kohli, J. Asher, J. Gaya, J. Marcus, J. Tang, J. Chan, J. Zhen, J. Reizenstein, J. Teboul, J. Zhong, J. Jin, J. Yang, J. Cummings, J. Carvill, J. Shepard, J. McPhie, J. Torres, J. Ginsburg, J. Wang, K. Wu, U. KamHou, K. Saxena, K. Prasad, K. Khandelwal, K. Zand, K. Matosich, K. Veeraraghavan, K. Michelena, K. Li, K. Huang, K. Chawla, K. Lakhotia, K. Huang, L. Chen, L. Garg, A. Lavender, L. Silva, L. Bell, L. Zhang, L. Guo, L. Yu, L. Moshkovich, L. Wehrstedt, M. Khabsa, M. Avalani, M. Bhatt, M. Tsimpoukelli, M. Mankus, M. Hasson, M. Lennie, M. Reso, M. Groshev, M. Naumov, M. Lathi, M. Keneally, M. L. Seltzer, M. Valko, M. Restrepo, M. Patel, M. Vyatskov, M. Samvelyan, M. Clark, M. Macey, M. Wang, M. J. Hermoso, M. Metanat, M. Rastegari, M. Bansal, N. Santhanam, N. Parks, N. White, N. Bawa, N. Singhal, N. Egebo, N. Usunier, N. P. Laptev, N. Dong, N. Zhang, N. Cheng, O. Chernoguz, O. Hart, O. Salpekar, O. Kalinli, P. Kent, P. Parekh, P. Saab, P. Balaji, P. Rittner, P. Bontrager, P. Roux, P. Dollár, P. Zvyagina, P. Ratanchandani, P. Yuvraj, Q. Liang, R. Alao, R. Rodriguez, R. Ayub, R. Murthy, R. Nayani, R. Mitra, R. Li, R. Hogan, R. Battey, R. Wang, R. Maheswari, R. Howes, R. Rinott, S. J. Bondu, S. Datta, S. Chugh, S. Hunt, S. Dhillon, S. Sidorov, S. Pan, S. Verma, S. Yamamoto, S. Ramaswamy, S. Lindsay, S. Feng, S. Lin, S. C. Zha, S. Shankar, S. Zhang, S. Wang, S. Agarwal, S. Sajuyigbe, S. Chintala, S. Max, S. Chen, S. Kehoe, S. Satterfield, S. Govindaprasad, S. K. Gupta, S. Cho, S. Virk, S. Subramanian, S. Choudhury, S. Goldman, T. Remez, T. Glaser, T. Best, T. Kohler, T. Robinson, T. Li, T. Zhang, T. Matthews, T. Chou, T. Shaked, V. Vontimitta, V. Ajayi, V. Montanez, V. Mohan, V. S. Kumar, V. Mangla, V. Ionescu, V. A. Poenaru, V. T. Mihailescu, V. Ivanov, W. Li, W. Wang, W. Jiang, W. Bouaziz, W. Constable, X. Tang, X. Wang, X. Wu, X. Wang, X. Xia, X. Wu, X. Gao, Y. Chen, Y. Hu, Y. Jia, Y. Qi, Y. Li, Y. Zhang, Y. Zhang, Y. Adi, Y. Nam, Y. Wang, Y. Hao, Y. Qian, Y. He, Z. Rait, Z. DeVito, Z. Rosnbrick, Z. Wen, Z. Yang, and Z. Zhao The llama 3 herd of models . ArXiv abs/2407.21783 . Cited by: §1 .

Fodor and Pylyshyn (1988) J. A. Fodor and Z. W. Pylyshyn Connectionism and cognitive architecture: a critical analysis . Cognition 28 , pp. 3–71 . Cited by: §2 .

Gandhi et al. (2025) K. Gandhi, A. Chakravarthy, A. Singh, nathan lile, and N. D. Goodman Cognitive behaviors that enable self-improving reasoners, or, four habits of highly effective stars . COLM . Cited by: §1 , §1 , §2 .

Gandhi et al. (2024) K. Gandhi, D. Lee, G. Grand, M. Liu, W. Cheng, A. Sharma, and N. D. Goodman Stream of search (sos): learning to search in language . ArXiv abs/2404.03683 . Cited by: §3.2 .

He et al. (2025) A. He, D. Fried, and S. Welleck Rewarding the unlikely: lifting grpo beyond distribution sharpening . arXiv preprint arXiv:2506.02355 . Cited by: §2 .

Lake et al. (2016) B. M. Lake, T. D. Ullman, J. B. Tenenbaum, and S. J. Gershman Building machines that learn and think like people . CoRR abs/1604.00289 . Cited by: §2 .

Lambert et al. (2025) N. Lambert, J. D. Morrison, V. Pyatkin, S. Huang, H. Ivison, F. Brahman, L. J. V. Miranda, A. Liu, N. Dziri, X. Lyu, Y. Gu, S. Malik, V. Graf, J. D. Hwang, J. Yang, R. L. Bras, O. Tafjord, C. Wilhelm, L. Soldaini, N. A. Smith, Y. Wang, P. Dasigi, and H. Hajishirzi TÜlu 3: pushing frontiers in open language model post-training . COLM . Cited by: §1 .

Liu et al. (2025a) M. Liu, S. Diao, X. Lu, J. Hu, X. Dong, Y. Choi, J. Kautz, and Y. Dong ProRL: prolonged reinforcement learning expands reasoning boundaries in large language models . CoRR abs/2505.24864 . External Links: Link , Document , 2505.24864 Cited by: §1 , §2 , §3.1 .

Liu et al. (2025b) Z. Liu, C. Chen, W. Li, P. Qi, T. Pang, C. Du, W. S. Lee, and M. Lin Understanding r1-zero-like training: A critical perspective . COLM . Cited by: §1 , §2 .

OpenAI et al. (2019) OpenAI, I. Akkaya, M. Andrychowicz, M. Chociej, M. Litwin, B. McGrew, A. Petron, A. Paino, M. Plappert, G. Powell, R. Ribas, J. Schneider, N. Tezak, J. Tworek, P. Welinder, L. Weng, Q. Yuan, W. Zaremba, and L. Zhang Solving rubik’s cube with a robot hand . CoRR abs/1910.07113 . External Links: Link , 1910.07113 Cited by: §1 .

OpenAI (2024) OpenAI OpenAI o1 system card . ArXiv . Cited by: §1 .

Pan et al. (2025) J. Pan, J. Zhang, X. Wang, L. Yuan, H. Peng, and A. Suhr TinyZero . Note: https://github.com/Jiayi-Pan/TinyZeroAccessed: 2025-01-24 Cited by: §2 , §3.2 .

Shao et al. (2025) R. Shao, S. S. Li, R. Xin, S. Geng, Y. Wang, S. Oh, S. S. Du, N. Lambert, S. Min, R. Krishna, Y. Tsvetkov, H. Hajishirzi, P. W. Koh, and L. S. Zettlemoyer Spurious rewards: rethinking training signals in rlvr . ArXiv abs/2506.10947 . Cited by: §2 , §3.2 .

Shao et al. (2024) Z. Shao, P. Wang, Q. Zhu, R. Xu, J. Song, M. Zhang, Y. K. Li, Y. Wu, and D. Guo DeepSeekMath: pushing the limits of mathematical reasoning in open language models . ArXiv abs/2402.03300 . Cited by: §3.2 .

Silva and Gombolay (2021) A. Silva and M. Gombolay Encoding human domain knowledge to warm start reinforcement learning . In Proceedings of the AAAI conference on artificial intelligence , Vol. 35 , pp. 5042–5050 . Cited by: §2 .

Silver et al. (2016) D. Silver, A. Huang, C. J. Maddison, A. Guez, L. Sifre, G. van den Driessche, J. Schrittwieser, I. Antonoglou, V. Panneershelvam, M. Lanctot, S. Dieleman, D. Grewe, J. Nham, N. Kalchbrenner, I. Sutskever, T. P. Lillicrap, M. Leach, K. Kavukcuoglu, T. Graepel, and D. Hassabis Mastering the game of go with deep neural networks and tree search . Nat. 529 ( 7587 ), pp. 484–489 . External Links: Link , Document Cited by: §1 , §2 .

Silver et al. (2017) D. Silver, T. Hubert, J. Schrittwieser, I. Antonoglou, M. Lai, A. Guez, M. Lanctot, L. Sifre, D. Kumaran, T. Graepel, T. P. Lillicrap, K. Simonyan, and D. Hassabis Mastering chess and shogi by self-play with a general reinforcement learning algorithm . CoRR abs/1712.01815 . External Links: Link , 1712.01815 Cited by: §1 .

Sun et al. (2025) Y. Sun, S. Hu, G. Zhou, K. Zheng, H. Hajishirzi, N. Dziri, and D. X. Song OMEGA: can llms reason outside the box in math? evaluating exploratory, compositional, and transformative generalization . ArXiv abs/2506.18880 . Cited by: 2nd item , §2 .

Vinyals et al. (2019) O. Vinyals, I. Babuschkin, W. M. Czarnecki, M. Mathieu, A. Dudzik, J. Chung, D. H. Choi, R. Powell, T. Ewalds, P. Georgiev, J. Oh, D. Horgan, M. Kroiss, I. Danihelka, A. Huang, L. Sifre, T. Cai, J. P. Agapiou, M. Jaderberg, A. S. Vezhnevets, R. Leblond, T. Pohlen, V. Dalibard, D. Budden, Y. Sulsky, J. Molloy, T. L. Paine, Çaglar Gülçehre, Z. Wang, T. Pfaff, Y. Wu, R. Ring, D. Yogatama, D. Wünsch, K. McKinney, O. Smith, T. Schaul, T. P. Lillicrap, K. Kavukcuoglu, D. Hassabis, C. Apps, and D. Silver Grandmaster level in starcraft II using multi-agent reinforcement learning . Nat. 575 ( 7782 ), pp. 350–354 . External Links: Link , Document Cited by: §2 .

Wang et al. (2025) Y. Wang, Q. Yang, Z. Zeng, L. Ren, L. Liu, B. Peng, H. Cheng, X. He, K. Wang, J. Gao, et al. Reinforcement learning for reasoning in large language models with one training example . arXiv preprint arXiv:2504.20571 . Cited by: §2 .

Wen et al. (2025) X. Wen, Z. Liu, S. Zheng, Z. Xu, S. Ye, Z. Wu, X. Liang, Y. Wang, J. Li, Z. Miao, et al. Reinforcement learning with verifiable rewards implicitly incentivizes correct reasoning in base llms . arXiv preprint arXiv:2506.14245 . Cited by: §2 .

Wu et al. (2025a) F. Wu, W. Xuan, X. Lu, Z. Harchaoui, and Y. Choi The invisible leash: why RLVR may not escape its origin . CoRR abs/2507.14843 . External Links: Link , Document , 2507.14843 Cited by: §1 , §1 , §2 , §3.1 , §4.4 , §4.4 .

Wu et al. (2025b) H. Wu, C. Wang, W. Zhao, and J. He Mirage or method? how model-task alignment induces divergent rl conclusions . External Links: Link Cited by: §2 , §3.2 .

Wu et al. (2025c) M. Wu, Z. Zhang, Q. Dong, Z. Xi, J. Zhao, S. Jin, X. Fan, Y. Zhou, H. Lv, M. Zhang, et al. Reasoning or memorization? unreliable results of reinforcement learning due to data contamination . arXiv preprint arXiv:2507.10532 . Cited by: §2 .

Xie et al. (2025) T. Xie, Z. Gao, Q. Ren, H. Luo, Y. Hong, B. Dai, J. Zhou, K. Qiu, Z. Wu, and C. Luo Logic-rl: unleashing LLM reasoning with rule-based reinforcement learning . CoRR abs/2502.14768 . External Links: Link , Document , 2502.14768 Cited by: §4.3 .

Yin et al. (2025) F. Yin, Z. L. Liu, L. Leqi, X. Ye, and G. Durrett Learning composable chains-of-thought . ArXiv abs/2505.22635 . Cited by: §2 .

Yu et al. (2025) Q. Yu, Z. Zhang, R. Zhu, Y. Yuan, X. Zuo, Y. Yue, T. Fan, G. Liu, L. Liu, X. Liu, H. Lin, Z. Lin, B. Ma, G. Sheng, Y. Tong, C. Zhang, M. Zhang, W. Zhang, H. Zhu, J. Zhu, J. Chen, J. Chen, C. Wang, H. Yu, W. Dai, Y. Song, X. Wei, H. Zhou, J. Liu, W. Ma, Y. Zhang, L. Yan, M. Qiao, Y. Wu, and M. Wang DAPO: an open-source LLM reinforcement learning system at scale . CoRR abs/2503.14476 . External Links: Link , Document , 2503.14476 Cited by: §A.2 , §1 , §2 .

Yue et al. (2025) Y. Yue, Z. Chen, R. Lu, A. Zhao, Z. Wang, S. Song, and G. Huang Does reinforcement learning really incentivize reasoning capacity in llms beyond the base model? . ArXiv . Cited by: §1 , §1 , §1 , §2 , §3.1 , §4.4 , §4.4 .

Zeng et al. (2025) W. Zeng, Y. Huang, Q. Liu, W. Liu, K. He, Z. Ma, and J. He SimpleRL-zoo: investigating and taming zero reinforcement learning for open base models in the wild . CoRR abs/2503.18892 . External Links: Link , Document , 2503.18892 Cited by: §2 .

Zhao et al. (2025) R. Zhao, A. Meterez, S. M. Kakade, C. Pehlevan, S. Jelassi, and E. Malach Echo chamber: RL post-training amplifies behaviors learned in pretraining . CoRR abs/2504.07912 . External Links: Link , Document , 2504.07912 Cited by: §1 , §2 .

Zhu et al. (2025) X. Zhu, M. Xia, Z. Wei, W. Chen, D. Chen, and Y. Meng The surprising effectiveness of negative reinforcement in llm reasoning . arXiv preprint arXiv:2506.01347 . Cited by: §2 .

## Appendix A Training Details

### A.1 Stage 1

All models in our experiments, except for the Multi-Base variants in § 4.3 , start from the same Stage 1 base model. The process for creating this model is detailed below.

#### Data Generation.

We first generate 50k Level-1 problems by randomly sampling a function and a string input (length 3 to 10). For each problem, we collect 10 responses from the Llama-3.1-8B-Instruct model (temperature 1.0, max length 8192). To focus training on problems the model finds non-trivial, we discard any problems where the base model achieves 100% accuracy. We then collect all remaining correct responses to form the SFT dataset. Before fine-tuning, we remove the function definitions from the prompts, keeping only the function identifier and the input. This results in around 116k training instances.

#### Rejection Fine-Tuning.

We fine-tune the model for 2 epochs with a learning rate of 2 × 10 − 5 2\times 10^{-5} and a global batch size of 128. Other hyperparameters follow the default settings provided by the veRL framework 1 1 1 https://github.com/volcengine/verl .

### A.2 Stage 2

#### Data Generation.

The problems used in Stage 2 are created using a similar process as in Stage 1, with the critical differences being that function definitions are hidden and problems can involve composition. For Level-2 problems, we randomly select and compose two functions. Example prompts for Stage 1 vs. Stage 2 can be found in Appendix C . For the Level 1 only and Level 2 only dataset, we create 50k problems. For the Level 1+2 mixed configuration, we create 25k problems for each level and combine them.

#### Reinforcement Learning.

For RL experiments, we use DAPO ( Yu et al., 2025 ) as the optimization algorithm. We enforce a strictly on-policy setup by setting both the training batch size and mini-batch size to 16. For each prompt, we generate 16 rollouts using a sampling temperature of 1.0 and a maximum response length of 8192. During training, we filter out any problems for which all rollouts are correct or all are incorrect. We use a learning rate of 1 × 10 − 6 1\times 10^{-6} and set the coefficients for both KL divergence and entropy loss to 0.

#### Rejection Fine-Tuning.

For the iterative RFT baseline, we use a learning rate of 2 × 10 − 5 2\times 10^{-5} and a batch size of 128. The process is iterative: the model from the previous iteration is used to generate a new set of rollouts. These rollouts are then filtered for correctness to construct a new SFT dataset, following the same procedure used in Stage 1. The model is then trained on this new dataset to produce the model for the next iteration.

## Appendix B Evaluation Details

#### String Transformation Prediction Task.

For the string transformation prediction task, the evaluation set consists of 256 randomly generated problems for each level from 1 to 8, resulting in a total of 2048 test problems. During evaluation, we generate responses using a sampling temperature of 1.0 and a maximum response length of 8192 tokens.

#### Countdown Task.

The evaluation set for the Countdown task consists of 128 problems for each level. The evaluation setup is the same as evaluating on the string transformation prediction task.

## Appendix C Example Prompts for Stage 1 and Stage 2

Here we present the example prompts used in our experiments. Fig. 7 shows the prompt used for Stage 1 data generation, where the function definition is provided to guide the model. However, during the actual Stage 1 training (and throughout Stage 2), this definition is removed, forcing the model to rely on the internalized atomic skills associated with the function identifier. Fig. 8 shows the prompt used for Stage 1 and Stage 2 training.

## Appendix D A Complete List of String Transformation Functions

Here we provide the full list of string functions we use. Note that we replace the function names with meaningless identifiers such as func_1 in our experiment.

## Appendix E Example for Countdown Task

## Appendix F Model Response Examples

The following sections contain the complete, unfolded responses from each model for the case studies.

### F.1 Full Responses to the Level 2 Problem

### F.2 Full Responses to the Level 3 Problem

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
