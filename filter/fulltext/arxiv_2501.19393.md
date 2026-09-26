##### Report GitHub Issue

Content selection saved. Describe the issue below:

# s1 : Simple test-time scaling

###### Abstract

Test-time scaling is a promising new approach to language modeling that uses extra test-time compute to improve performance. Recently, OpenAI’s o1 model showed this capability but did not publicly share its methodology, leading to many replication efforts. We seek the simplest approach to achieve test-time scaling and strong reasoning performance. First, we curate a small dataset s1K of 1,000 questions paired with reasoning traces relying on three criteria we validate through ablations: difficulty, diversity, and quality. Second, we develop budget forcing to control test-time compute by forcefully terminating the model’s thinking process or lengthening it by appending “Wait” multiple times to the model’s generation when it tries to end. This can lead the model to double-check its answer, often fixing incorrect reasoning steps. After supervised finetuning the Qwen2.5-32B-Instruct language model on s1K and equipping it with budget forcing, our model s1-32B exceeds o1-preview on competition math questions by up to 27% (MATH and AIME24). Further, scaling s1-32B with budget forcing allows extrapolating beyond its performance without test-time intervention: from 50% to 57% on AIME24. Our model, data, and code are open-source at https://github.com/simplescaling/s1 .

###### Keywords:

## 1 Introduction

Performance improvements of language models (LMs) over the past years have largely relied on scaling up train-time compute using large-scale self-supervised pretraining ( Kaplan et al., 2020 ; Hoffmann et al., 2022 ) . The creation of these powerful models has set the stage for a new scaling paradigm built on top of them: test-time scaling . The aim of this approach is to increase the compute at test time to get better results. There has been much work exploring this idea ( Snell et al., 2024 ; Welleck et al., 2024 ) , and the viability of this paradigm was recently validated by OpenAI o1 ( OpenAI, 2024 ) . o1 has demonstrated strong reasoning performance with consistent gains from scaling test-time compute. OpenAI describes their approach as using large-scale reinforcement learning (RL) implying the use of sizable amounts of data ( OpenAI, 2024 ) . This has led to various attempts to replicate their models relying on techniques like Monte Carlo Tree Search ( Gao et al., 2024b ; Zhang et al., 2024a ) , multi-agent approaches ( Qin et al., 2024 ) , and others ( Wang et al., 2024a ; Huang et al., 2024b ; Huang et al., 2025 ) . Among these approaches, DeepSeek R1 ( DeepSeek-AI et al., 2025 ) has successfully replicated o1-level performance, also employing reinforcement learning via millions of samples and multiple training stages. However, despite the large number of o1 replication attempts, none have openly replicated a clear test-time scaling behavior. Thus, we ask: what is the simplest approach to achieve both test-time scaling and strong reasoning performance?

We show that training on only 1,000 samples with next-token prediction and controlling thinking duration via a simple test-time technique we refer to as budget forcing leads to a strong reasoning model that scales in performance with more test-time compute. Specifically, we construct s1K , which consists of 1,000 carefully curated questions paired with reasoning traces and answers distilled from Gemini Thinking Experimental ( Google, 2024 ) . We perform supervised fine-tuning (SFT) of an off-the-shelf pretrained model on our small dataset requiring just 26 minutes of training on 16 H100 GPUs. After training, we control the amount of test-time compute our model spends using budget forcing : (I) If the model generates more thinking tokens than a desired limit, we forcefully end the thinking process by appending an end-of-thinking token delimiter. Ending the thinking this way makes the model transition to generating its answer. (II) If we want the model to spend more test-time compute on a problem, we suppress the generation of the end-of-thinking token delimiter and instead append “Wait” to the model’s current reasoning trace to encourage more exploration. Equipped with this simple recipe – SFT on 1,000 samples and test-time budget forcing – our model s1-32B exhibits test-time scaling ( Figure 1 ). Further, s1-32B is the most sample-efficient reasoning model and outperforms closed-source models like OpenAI’s o1-preview ( Figure 2 ).

We conduct extensive ablation experiments targeting (a) our selection of 1,000 (1K) reasoning samples and (b) our test-time scaling. For (a) , we find that jointly incorporating difficulty, diversity, and quality measures into our selection algorithm is important. Random selection, selecting samples with the longest reasoning traces, or only selecting maximally diverse samples all lead to significantly worse performance (around − - 30% on AIME24 on average). Training on our full data pool of 59K examples, a superset of s1K , does not offer substantial gains over our 1K selection. This highlights the importance of careful data selection and echoes prior findings for instruction tuning ( Zhou et al., 2023 ) . For (b) , we define desiderata for test-time scaling methods to compare different approaches. Budget forcing leads to the best scaling as it has perfect controllability with a clear positive slope leading to strong performance.

In summary, our contributions are: We develop simple methods for creating a sample-efficient reasoning dataset ( §2 ) and test-time scaling ( §3 ); Based on these we build s1-32B which is competitive with o1-preview ( §4 ); We ablate subtleties of data ( §5.1 ) and test-time scaling ( §5.2 ). We end with a discussion to motivate future work on simple reasoning ( §6 ). Our code, model, and data are open-source at https://github.com/simplescaling/s1 .

## 2 Reasoning data curation to create s1K

In this section, we describe our process for creating a large dataset first in §2.1 and then filtering it down to s1K in §2.2 .

### 2.1 Initial collection of 59K samples

We collect an initial 59,029 questions from 16 sources following three guiding principles. Quality : Datasets should be high-quality; we always inspect samples and ignore datasets with, e.g., poor formatting; Difficulty : Datasets should be challenging and require significant reasoning effort; Diversity : Datasets should stem from various fields to cover different reasoning tasks. We collect datasets of two categories:

#### Curation of existing datasets

Our largest source is NuminaMATH ( LI et al., 2024 ) with 30,660 mathematical problems from online websites. We also include historical AIME problems (1983-2021). To enhance diversity, we add OlympicArena ( Huang et al., 2024a ) with 4,250 questions spanning Astronomy, Biology, Chemistry, Computer Science, Geography, Mathematics, and Physics from various Olympiads. OmniMath ( Gao et al., 2024a ) adds 4,238 competition-level mathematics problems. We also include 2,385 problems from AGIEval ( Zhong et al., 2023 ) , which features questions from standardized tests like SAT and LSAT, covering English, Law, and Logic. We refer to Table 7 in §C for our other sources.

#### New datasets in quantitative reasoning

To complement these existing datasets, we create two original datasets. s1-prob consists of 182 questions from the probability section of Stanford University’s Statistics Department’s PhD Qualifying Exams ( https://statistics.stanford.edu ), accompanied by handwritten solutions that cover difficult proofs. The probability qualifying exam is held yearly and requires professional-level mathematical problem-solving. s1-teasers comprises 23 challenging brain-teasers commonly used in interview questions for quantitative trading positions. Each sample consists of a problem and solution taken from PuzzledQuant ( https://www.puzzledquant.com/ ). We only take examples with the highest difficulty level (”Hard”).

For each question, we generate a reasoning trace and solution using the Google Gemini Flash Thinking API ( Google, 2024 ) extracting its reasoning trace and response. This yields 59K triplets of a question, generated reasoning trace, and generated solution. Examples from our dataset are in §D.2 . We decontaminate all samples against our evaluation questions (MATH500, GPQA Diamond, AIME24; §C.5 ) using 8-grams and deduplicate the data.

### 2.2 Final selection of 1K samples

We could directly train on our pool of 59K questions, however, our goal is to find the simplest approach with minimal resources. Thus, we go through three stages of filtering to arrive at a minimal set of 1,000 samples relying on our three guiding data principles: Quality, Difficulty, and Diversity.

#### Quality

We first remove any questions where we ran into any API errors reducing our dataset to 54,116 samples. Next, we filter out low-quality examples by checking if they contain any string patterns with formatting issues, such as ASCII art diagrams, non-existent image references, or inconsistent question numbering reducing our dataset to 51,581 examples. From this pool, we identify 384 samples for our final 1,000 samples from datasets that we perceive as high-quality and not in need of further filtering (see §C.4 for details).

#### Difficulty

For difficulty, we use two indicators: model performance and reasoning trace length. We evaluate two models on each question: Qwen2.5-7B-Instruct and Qwen2.5-32B-Instruct ( Qwen et al., 2024 ) , with correctness assessed by Claude 3.5 Sonnet comparing each attempt against the reference solution (see §C.3 for the grading protocol). We measure the token length of each reasoning trace to indicate problem difficulty using the Qwen2.5 tokenizer. This relies on the assumption that more difficult problems require more thinking tokens. Based on the grading, we remove questions that either Qwen2.5-7B-Instruct or Qwen2.5-32B-Instruct can solve correctly and thus may be too easy. By using two models we reduce the likelihood of an easy sample slipping through our filtering due to a rare mistake on an easy question of one of the models. This brings our total samples down to 24,496 , setting the stage for the next round of subsampling based on diversity. While filtering with these two models may be optimized for our setup as we will also use Qwen2.5-32B-Instruct as our model to finetune, the idea of model-based filtering generalizes to other setups.

#### Diversity

To quantify diversity, we classify questions into domains using Claude 3.5 Sonnet based on the Mathematics Subject Classification (MSC) system (e.g., geometry, combinatorics, etc.) from the American Mathematical Society. 1 1 1 https://mathscinet.ams.org/mathscinet/msc/msc2020.html The taxonomy focuses on topics in mathematics but also includes other sciences such as biology, physics, and economics. To select our final examples from the pool of 24,496 questions, we first choose one domain uniformly at random. Then, we sample one problem from this domain according to a distribution that favors longer reasoning traces (see §C.4 for details) as motivated in Difficulty . We repeat this process until we have 1,000 total samples spanning 50 domains.

In §5.1 , we will show that using our three criteria in combination is important, as only relying on quality, diversity, or difficulty in isolation leads to worse datasets. Some distilled generations are incorrect, which we allow in our data as we focus on capturing the reasoning process rather than entirely correct solutions. Our grader ( §C.3 ) deems 53.6% correct in s1K and 63.0% in our follow-up s1K-1.1 (see §A ).

## 3 Test-time scaling

### 3.1 Method

We classify test-time scaling methods into 1) Sequential , where later computations depend on earlier ones (e.g., a long reasoning trace), and 2) Parallel , where computations run independently (e.g., majority voting) ( Snell et al., 2024 ; Brown et al., 2024 ) . We focus on sequential scaling as intuitively we believe it should scale better, since later computations can build on intermediate results, allowing for deeper reasoning and iterative refinement. We propose new sequential scaling methods and ways to benchmark them.

#### Budget forcing

We propose a simple decoding-time intervention by forcing a maximum and/or minimum number of thinking tokens. Specifically, we enforce a maximum token count by simply appending the end-of-thinking token delimiter and optionally “ Final Answer: ” to early exit the thinking stage and make the model provide its current best answer. To enforce a minimum, we suppress the generation of the end-of-thinking token delimiter and optionally append the string “Wait” to the model’s current reasoning trace to encourage the model to reflect on its current generation. Figure 3 contains an example of how this simple approach can lead the model to arrive at a better answer.

#### Baselines

We benchmark budget forcing with: (I) Conditional length-control methods , which rely on telling the model in the prompt how long it should generate for. We group them by granularity into (a) Token-conditional control: We specify an upper bound of thinking tokens in the prompt; (b) Step-conditional control: We specify an upper bound of thinking steps, where each step is around 100 tokens; (c) Class-conditional control: We write two generic prompts that tell the model to either think for a short or long amount of time (see §E.1 for details). (II) Rejection sampling , which samples until a generation fits a predetermined compute budget. This oracle captures the posterior over responses conditioned on its length.

### 3.2 Metrics

We establish a set of desiderata as evaluation metrics to measure test-time scaling across methods. Importantly, we do not only care about the accuracy a method can achieve but also its controllability and test-time scaling slope. For each method we consider, we run a set of evaluations a ∈ 𝒜 a\in\mathcal{A} varying test-time compute on a fixed benchmark, e.g. AIME24. This produces a piece-wise linear function f f with compute as the x-axis measured in thinking tokens and accuracy as the y-axis (see Figure 1 , where the rightmost dot for AIME24 corresponds to f ⁡ ( 7320 ) = 57 % f(7320)=57\% ). We measure three metrics: Control = 1 | 𝒜 | ​ ∑ a ∈ 𝒜 𝕀 ⁡ ( a min ≤ a ≤ a max ) \displaystyle\text{Control}=\frac{1}{|\mathcal{A}|}\sum_{a\in\mathcal{A}}\mathbb{I}(a_{\text{min}}\leq a\leq a_{\text{max}}) (1) where a min , a max a_{\text{min}},a_{\text{max}} refer to a pre-specified minimum and maximum amount of test-time compute; in our case thinking tokens. We usually only constrain a max a_{\text{max}} . As tokens generated correspond to the amount of test-time compute spent, this metric measures the extent to which a method allows controllability over the use of that test-time compute. We report it as a percentage with 100% being perfect control. Scaling = 1 ( | 𝒜 | 2 ) ​ ∑ a , b ∈ 𝒜 b > a f ⁡ ( b ) − f ⁡ ( a ) b − a \displaystyle\text{Scaling}=\frac{1}{\binom{|\mathcal{A}|}{2}}\sum_{\begin{subarray}{c}a,b\in\mathcal{A}\\ b>a\end{subarray}}\frac{f(b)-f(a)}{b-a} (2) Scaling is the average slope of the piece-wise linear function. It must be positive for useful methods and larger is better. Performance = max a ∈ 𝒜 ⁡ f ⁡ ( a ) \displaystyle=\max_{a\in\mathcal{A}}f(a) (3) Performance is simply the maximum performance the method achieves on the benchmark. A method with monotonically increasing scaling achieves 100% performance on any benchmark in the limit. However, the methods we investigate eventually flatten out or further scaling fails due to control or context window limitations.

## 4 Results

### 4.1 Setup

#### Training

We perform supervised finetuning on Qwen2.5-32B-Instruct using s1K to obtain our model s1-32B using basic hyperparameters outlined in §D . Finetuning took 26 minutes on 16 NVIDIA H100 GPUs with PyTorch FSDP.

#### Evaluation

We select three representative reasoning benchmarks widely used in the field: AIME24 ( of America, 2024 ) has 30 problems that were used in the 2024 American Invitational Mathematics Examination (AIME) held from January 31 – February 1, 2024. AIME tests mathematical problem-solving with arithmetic, algebra, counting, geometry, number theory, probability, and other secondary school math topics. High-scoring high school students in the test are invited to participate in the United States of America Mathematics Olympiad (USAMO). All AIME answers are integers ranging from 000 000 to 999 999 , inclusive. Some AIME problems rely on figures that we provide to our model using the vector graphics language Asymptote as it cannot take image inputs. MATH500 ( Hendrycks et al., 2021 ) is a benchmark of competition math problems of varying difficulty. We evaluate on the same 500 samples selected by OpenAI in prior work ( Lightman et al., 2023 ) . GPQA Diamond ( Rein et al., 2023 ) consists of 198 PhD-level science questions from Biology, Chemistry and Physics. Experts with PhDs in the corresponding domains only achieved 69.7% on GPQA Diamond ( OpenAI, 2024 ) . When we write “GPQA” in the context of evaluation in this work, we always refer to the Diamond subset. We build on the “lm-evaluation-harness” framework ( Gao et al., 2021 ; Biderman et al., 2024 ) . Unless otherwise specified, we evaluate with a temperature of 0 (greedy) and measure accuracy (equivalent to pass@1).

#### Other models

We benchmark s1-32B against: OpenAI o1 series ( OpenAI, 2024 ) , closed-source models that popularized test-time scaling; DeepSeek r1 series ( DeepSeek-AI et al., 2025 ) , open-weight reasoning models with up to o1-level performance; Qwen’s QwQ-32B-preview ( Team, 2024 ) , a 32B open-weight reasoning model without disclosed methodology; Sky-T1-32B-Preview ( Team, 2025 ) and Bespoke-32B ( Labs, 2025 ) , open models with open reasoning data distilled from QwQ-32B-preview and r1; Google Gemini 2.0 Flash Thinking Experimental ( Google, 2024 ) , the API that we distill from. As it has no official evaluation scores, we use the Gemini API to benchmark it ourselves. However, the ‘‘recitation error’’ of the Gemini API makes evaluation challenging. 2 2 2 https://github.com/google/generative-ai-docs/issues/257 We circumvent this, by manually inserting all 30 AIME24 questions in its web interface where the error does not appear. However, we leave out MATH500 (500 questions) and GPQA Diamond (198 questions), thus they are N.A. in Table 1 . Our model, s1-32B , is fully open including weights, reasoning data, and code.

### 4.2 Performance

#### Test-time scaling

Figure 1 shows the performance of s1-32B with budget forcing scales with more test-time compute. In Figure 4 (left), we expand the plot from Figure 1 (middle) showing that while we can improve AIME24 performance using our budget forcing technique ( §3 ) and more test-time compute it does eventually flatten out at six times. Suppressing the end-of-thinking token delimiter too often can lead the model into repetitive loops instead of continued reasoning. In Figure 4 (right), we show that after training Qwen2.5-32B-Instruct on our 1,000 samples to produce s1-32B and equipping it with the simple budget forcing technique, it operates in a different scaling paradigm. Scaling test-time compute on the base model via majority voting cannot catch up with the performance of s1-32B which validates our intuition from §3 that sequential scaling is more effective than parallel. We provide example generations of s1-32B in Figure 5 .

#### Sample-efficiency

In Figure 2 (right) and Table 1 we compare s1-32B with other models. We find that s1-32B is the most sample-efficient open data reasoning model. It performs significantly better than our base model (Qwen2.5-32B-Instruct) despite just training it on an additional 1,000 samples. The concurrently released r1-32B shows stronger performance than s1-32B while also only using SFT ( DeepSeek-AI et al., 2025 ) . However, it is trained on 800 × \times more reasoning samples. It is an open question whether one can achieve their performance with just 1,000 samples. Finally, our model nearly matches Gemini 2.0 Thinking on AIME24. As the data for s1-32B is distilled from Gemini 2.0, this shows our distillation procedure was likely effective.

## 5 Ablations

### 5.1 Data Quantity, Diversity, and Difficulty

In §2 we outlined our three guiding principles in curating s1K : Quality, Difficulty, and Diversity. Here we test the importance of combining them and the overall efficacy of our selection. Only Quality (1K-random) : After obtaining our high-quality reasoning chains from Gemini, we select 1,000 samples at random; not relying on our difficulty and diversity filtering at all. Table 2 shows this approach performs much worse than s1K across all benchmarks. Only Diversity (1K-diverse) : For this dataset, we sample uniformly across domains to maximize diversity disregarding any notion of difficulty. This approach also leads to poor performance similar to 1K-random. Only Difficulty (1K-longest) : Here we rely on one of our difficulty indicators introduced in §2 by selecting the 1,000 samples with the longest reasoning traces. This approach significantly boosts GPQA performance but overall still falls short of using s1K . Maximize Quantity : Finally, we compare with just training on all of our 59K samples, a superset of all the 1K-sample versions. This leads to a strong model but uses much more resources. To finetune on 59K samples, we use 394 H100 GPU hours while s1-32B only required 7 H100 GPU hours. Moreover, relying only on s1K is extremely competitive as shown in §2 . Overall, combining all three criteria – Quality , Difficulty , Diversity – via our methodology in §2 is key for sample-efficient reasoning training.

### 5.2 Test-time scaling methods

#### Budget forcing

In Table 3 we compare the test-time scaling methods we have introduced in §3 . Overall, we find that budget forcing provides perfect control, good scaling, and leads to our best AIME24 score. Thus, this is the method we use for s1-32B in Figure 1 and in §4 . In Table 4 , we compare different strings for extrapolating performance. We find that “Wait” generally gives the best performance.

Class-conditional control We provide benchmark scores for this method in §E.1 and summarize three findings here: (1) Token-conditional control fails without budget forcing, as our model cannot reliably count tokens - even when trained to do so. (2) Under step-conditional control, the model generates a similar total number of tokens when given different step targets, as the model goes from few steps with many tokens per step, to many steps with few tokens in each step. Thus, the model learns to hack its way around the compute constraint making the controllability of this method mediocre. (3) Class-conditional control can work - telling a model to simply think longer can increase its test-time compute and performance, which leads good scaling in Table 3 .

#### Rejection sampling

Surprisingly, we find that simply sampling until the generation fits a specific length leads to an inverse scaling trend as depicted in Figure 6 . In §E.2 we inspect a question, which was answered correctly by the model when rejection sampling for ≤ 4000 \leq 4000 , but not for the ≤ 8000 \leq 8000 token setting. In the ≤ 4000 \leq 4000 setting the model directly jumps to the correct approach, while for the ≤ 8000 \leq 8000 setting it backtracks a lot. We hypothesize that there is a correlation such that shorter generations tend to be the ones where the model was on the right track from the start, whereas longer ones tend to be ones where the model made mistakes and thus backtracks or questions itself. This leads to longer samples often being wrong when rejection sampling and thus the inverse scaling trend.

## 6 Discussion and related work

### 6.1 Sample-efficient reasoning

#### Models

There are a number of concurrent efforts to build models that replicate the performance of o1 ( OpenAI, 2024 ) . For example, DeepSeek-r1 and k1.5 ( DeepSeek-AI et al., 2025 ; Team et al., 2025 ) are built with reinforcement learning methods, while others rely on SFT using tens of thousands of distilled examples ( Team, 2025 ; Xu et al., 2025 ; Labs, 2025 ) . We show that SFT on only 1,000 examples suffices to build a competitive reasoning model matching o1-preview and produces a model that lies on the pareto frontier ( Figure 2 ). Further, we introduce budget forcing which combined with our reasoning model leads to the first reproduction of OpenAI’s test-time scaling curves ( OpenAI, 2024 ) . Why does supervised finetuning on just 1,000 samples lead to such performance gains? We hypothesize that the model is already exposed to large amounts of reasoning data during pretraining which spans trillions of tokens. Thus, the ability to perform reasoning is already present in our model. Our sample-efficient finetuning stage just activates it and we scale it further at test time with budget forcing. This is similar to the ”Superficial Alignment Hypothesis” presented in LIMA ( Zhou et al., 2023 ) , where the authors find that 1,000 examples can be sufficient to align a model to adhere to user preferences.

#### Benchmarks and methods

To evaluate and push the limits of these models, increasingly challenging benchmarks have been introduced, such as Olympiad-level science competitions ( He et al., 2024 ; Jain et al., 2024 ; Zhong et al., 2023 ) and others ( Srivastava et al., 2023 ; Glazer et al., 2024 ; Su et al., 2024 ; Kim et al., 2024 ; Phan et al., 2025 ) . To enhance models’ performance on reasoning-related tasks, researchers have pursued several strategies: Prior works have explored continuing training language models on specialized corpora related to mathematics and science ( Azerbayev et al., 2023 ; Yang et al., 2024 ) , sometimes even synthetically generated data ( Yu et al., 2024 ) . Others have developed training methodologies specifically aimed at reasoning performance ( Zelikman et al., 2022 ; Zelikman et al., 2024 ; Luo et al., 2025 ; Yuan et al., 2025 ; Wu et al., 2024a ) . Another significant line of work focuses on prompting-based methods to elicit and improve reasoning abilities, including methods like Chain-of-Thought prompting ( Wei et al., 2023 ; Yao et al., 2023a ; Yao et al., 2023b ; Bi et al., 2023 ; Fu et al., 2023 ; Zhang et al., 2024b ; Xiang et al., 2025 ; Hu et al., 2024 ; Diao et al., 2024 ) . These combined efforts aim to advance the reasoning ability of language models, enabling them to handle more complex and abstract tasks effectively.

### 6.2 Test-time scaling

#### Methods

As we introduce in §3 , we differentiate two methods to scale test-time compute: parallel and sequential . The former relies on multiple solution attempts generated in parallel and selecting the best outcome via specific criteria. These criteria include choosing the most frequent response for majority voting or the best response based on an external reward for Best-of-N ( Brown et al., 2024 ; Irvine et al., 2023 ; Levi, 2024 ) . Unlike repeated sampling, previous sequential scaling methods let the model generate solution attempts sequentially based on previous attempts, allowing it to refine each attempt based on previous outcomes ( Snell et al., 2024 ; Hou et al., 2025 ; Lee et al., 2025 ) . Tree-based search methods ( Gandhi et al., 2024 ; Wu et al., 2024b ) offer a hybrid approach between sequential and parallel scaling, such as Monte-Carlo Tree Search (MCTS) ( Liu et al., 2024 ; Zhang et al., 2023 ; Zhou et al., 2024 ; Choi et al., 2023 ) and guided beam search ( Xie et al., 2023 ) . REBASE ( Wu et al., 2024b ) employs a process reward model to balance exploitation and pruning during tree search. Empirically, REBASE has been shown to outperform sampling-based methods and MCTS ( Wu et al., 2024b ) . Reward models ( Lightman et al., 2023 ; Wang et al., 2024b ; Wang et al., 2024c ) play a key role in these methods. They come in two variants: outcome reward models and process reward models. Outcome reward models ( Xin et al., 2024 ; Ankner et al., 2024 ) assign a score to complete solutions and are particularly useful in Best-of-N selection, while process reward models ( Lightman et al., 2023 ; Wang et al., 2024b ; Wu et al., 2024b ) assess individual reasoning steps and are effective in guiding tree-based search methods.

#### Limits to further test-time scaling

We have shown that budget forcing allows extrapolating test-time compute in §4 , e.g., improving AIME24 performance from 50% to 57%. However, it has two key limitations when scaling further: it eventually flattens out ( Figure 4 ), and the context window of the underlying language model constrains it. Despite these constraints, our work shows test-time scaling across a wide range of accuracies ( Figure 1 ), partly because scaling down test-time compute behaves predictably and does not suffer from these constraints.

Continuing test-time scaling will require approaches that can further extrapolate test-time compute. How can we get such extrapolation? There may be improvements to budget forcing such as rotating through different strings, not only “Wait”, or combining it with frequency penalties or higher temperature to avoid repetitive loops. An exciting direction for future work is also researching whether applying budget forcing to a reasoning model trained with reinforcement learning yields better extrapolation; or if RL allows for new ways of test-time scaling beyond budget forcing. Our work defines the right metrics ( §3.2 ) – Control, Scaling, and Performance – to enable future research and progress on extrapolating test-time compute.

#### Parallel scaling as a solution

Parallel scaling offers one solution to the limits of sequential scaling, thus we augment our sequentially scaled model with two methods: (I) Majority voting: After generating k k solutions, the final solution is the most frequent one across generations; (II) Tree search via REBASE : We use the REBASE process reward model, which is initialized from LLaMA-34B and further finetuned on a synthetic process reward modeling dataset ( Wu et al., 2024b ) . We then aggregate the solutions generated by REBASE via majority voting. As shown in Figure 7 , augmenting our model with REBASE scales better than majority voting, and even sequential scaling in this scenario. However, REBASE requires an additional forward pass at each step for the reward model adding some computation overhead. For sequential scaling, when prompted to use up to 512 steps, for 12 out of the 30 evaluation questions the model generates a response that exceeds the context window leading to a large performance drop. Overall, we find that these parallel scaling methods complement sequential scaling thus they offer an avenue for scaling test-time compute even further; beyond fixed context windows.

## Impact Statement

Language models with strong reasoning capabilities have the potential to greatly enhance human productivity, from assisting in complex decision-making to driving scientific breakthroughs. However, recent advances in reasoning, such as OpenAI’s o1 and DeepSeek’s r1, lack transparency, limiting broader research progress. Our work aims to push the frontier of reasoning in a fully open manner, fostering innovation and collaboration to accelerate advancements that ultimately benefit society.

## Acknowledgements

We thank Ryan Marten for generating traces from DeepSeek r1 for s1.1 using Bespoke Curator ( Marten et al., 2025 ) . This work was partly conducted using the Stanford Marlowe GPU cluster ( Kapfer et al., 2025 ) , made possible by financial support from Stanford University. We thank Alexander M. Rush, Andrew Ilyas, Banghua Zhu, Chenglei Si, Chunting Zhou, John Yang, Ludwig Schmidt, Samy Jelassi, Suhas Kotha, Tengyu Ma, Xuechen Li, Yu Sun, and Yue Zhang for very constructive discussions.

## References

Ankner et al. (2024) Ankner, Z., Paul, M., Cui, B., Chang, J. D., and Ammanabrolu, P. Critique-out-loud reward models, 2024. URL https://arxiv.org/abs/2408.11791 .

Arora et al. (2023) Arora, D., Singh, H. G., and Mausam. Have llms advanced enough? a challenging problem solving benchmark for large language models, 2023. URL https://arxiv.org/abs/2305.15074 .

Azerbayev et al. (2023) Azerbayev, Z., Schoelkopf, H., Paster, K., Santos, M. D., McAleer, S., Jiang, A. Q., Deng, J., Biderman, S., and Welleck, S. Llemma: An open language model for mathematics, 2023.

Bi et al. (2023) Bi, Z., Zhang, N., Jiang, Y., Deng, S., Zheng, G., and Chen, H. When do program-of-thoughts work for reasoning?, 2023. URL https://arxiv.org/abs/2308.15452 .

Biderman et al. (2024) Biderman, S., Schoelkopf, H., Sutawika, L., Gao, L., Tow, J., Abbasi, B., Aji, A. F., Ammanamanchi, P. S., Black, S., Clive, J., DiPofi, A., Etxaniz, J., Fattori, B., Forde, J. Z., Foster, C., Hsu, J., Jaiswal, M., Lee, W. Y., Li, H., Lovering, C., Muennighoff, N., Pavlick, E., Phang, J., Skowron, A., Tan, S., Tang, X., Wang, K. A., Winata, G. I., Yvon, F., and Zou, A. Lessons from the trenches on reproducible evaluation of language models, 2024.

Brown et al. (2024) Brown, B., Juravsky, J., Ehrlich, R., Clark, R., Le, Q. V., Ré, C., and Mirhoseini, A. Large language monkeys: Scaling inference compute with repeated sampling, 2024. URL https://arxiv.org/abs/2407.21787 .

Cesista (2024) Cesista, F. L. Multimodal structured generation: Cvpr’s 2nd mmfm challenge technical report, 2024. URL https://arxiv.org/abs/2406.11403 .

Chen et al. (2023) Chen, W., Yin, M., Ku, M., Lu, P., Wan, Y., Ma, X., Xu, J., Wang, X., and Xia, T. Theoremqa: A theorem-driven question answering dataset, 2023. URL https://arxiv.org/abs/2305.12524 .

Choi et al. (2023) Choi, S., Fang, T., Wang, Z., and Song, Y. Kcts: Knowledge-constrained tree search decoding with token-level hallucination detection, 2023. URL https://arxiv.org/abs/2310.09044 .

DeepSeek-AI et al. (2025) DeepSeek-AI, Guo, D., Yang, D., Zhang, H., Song, J., Zhang, R., Xu, R., Zhu, Q., Ma, S., Wang, P., Bi, X., Zhang, X., Yu, X., Wu, Y., Wu, Z. F., Gou, Z., Shao, Z., Li, Z., Gao, Z., Liu, A., Xue, B., Wang, B., Wu, B., Feng, B., Lu, C., Zhao, C., Deng, C., Zhang, C., Ruan, C., Dai, D., Chen, D., Ji, D., Li, E., Lin, F., Dai, F., Luo, F., Hao, G., Chen, G., Li, G., Zhang, H., Bao, H., Xu, H., Wang, H., Ding, H., Xin, H., Gao, H., Qu, H., Li, H., Guo, J., Li, J., Wang, J., Chen, J., Yuan, J., Qiu, J., Li, J., Cai, J. L., Ni, J., Liang, J., Chen, J., Dong, K., Hu, K., Gao, K., Guan, K., Huang, K., Yu, K., Wang, L., Zhang, L., Zhao, L., Wang, L., Zhang, L., Xu, L., Xia, L., Zhang, M., Zhang, M., Tang, M., Li, M., Wang, M., Li, M., Tian, N., Huang, P., Zhang, P., Wang, Q., Chen, Q., Du, Q., Ge, R., Zhang, R., Pan, R., Wang, R., Chen, R. J., Jin, R. L., Chen, R., Lu, S., Zhou, S., Chen, S., Ye, S., Wang, S., Yu, S., Zhou, S., Pan, S., Li, S. S., Zhou, S., Wu, S., Ye, S., Yun, T., Pei, T., Sun, T., Wang, T., Zeng, W., Zhao, W., Liu, W., Liang, W., Gao, W., Yu, W., Zhang, W., Xiao, W. L., An, W., Liu, X., Wang, X., Chen, X., Nie, X., Cheng, X., Liu, X., Xie, X., Liu, X., Yang, X., Li, X., Su, X., Lin, X., Li, X. Q., Jin, X., Shen, X., Chen, X., Sun, X., Wang, X., Song, X., Zhou, X., Wang, X., Shan, X., Li, Y. K., Wang, Y. Q., Wei, Y. X., Zhang, Y., Xu, Y., Li, Y., Zhao, Y., Sun, Y., Wang, Y., Yu, Y., Zhang, Y., Shi, Y., Xiong, Y., He, Y., Piao, Y., Wang, Y., Tan, Y., Ma, Y., Liu, Y., Guo, Y., Ou, Y., Wang, Y., Gong, Y., Zou, Y., He, Y., Xiong, Y., Luo, Y., You, Y., Liu, Y., Zhou, Y., Zhu, Y. X., Xu, Y., Huang, Y., Li, Y., Zheng, Y., Zhu, Y., Ma, Y., Tang, Y., Zha, Y., Yan, Y., Ren, Z. Z., Ren, Z., Sha, Z., Fu, Z., Xu, Z., Xie, Z., Zhang, Z., Hao, Z., Ma, Z., Yan, Z., Wu, Z., Gu, Z., Zhu, Z., Liu, Z., Li, Z., Xie, Z., Song, Z., Pan, Z., Huang, Z., Xu, Z., Zhang, Z., and Zhang, Z. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning, 2025. URL https://arxiv.org/abs/2501.12948 .

Diao et al. (2024) Diao, S., Wang, P., Lin, Y., Pan, R., Liu, X., and Zhang, T. Active prompting with chain-of-thought for large language models, 2024. URL https://arxiv.org/abs/2302.12246 .

Dubey et al. (2024) Dubey, A., Jauhri, A., Pandey, A., Kadian, A., Al-Dahle, A., Letman, A., Mathur, A., Schelten, A., Yang, A., Fan, A., Goyal, A., Hartshorn, A., Yang, A., Mitra, A., Sravankumar, A., Korenev, A., Hinsvark, A., Rao, A., Zhang, A., Rodriguez, A., Gregerson, A., et al. The llama 3 herd of models, 2024. URL https://arxiv.org/abs/2407.21783 .

Fu et al. (2023) Fu, Y., Peng, H., Sabharwal, A., Clark, P., and Khot, T. Complexity-based prompting for multi-step reasoning, 2023. URL https://arxiv.org/abs/2210.00720 .

Gandhi et al. (2024) Gandhi, K., Lee, D., Grand, G., Liu, M., Cheng, W., Sharma, A., and Goodman, N. D. Stream of search (sos): Learning to search in language, 2024. URL https://arxiv.org/abs/2404.03683 .

Gao et al. (2024a) Gao, B., Song, F., Yang, Z., Cai, Z., Miao, Y., Dong, Q., Li, L., Ma, C., Chen, L., Xu, R., Tang, Z., Wang, B., Zan, D., Quan, S., Zhang, G., Sha, L., Zhang, Y., Ren, X., Liu, T., and Chang, B. Omni-math: A universal olympiad level mathematic benchmark for large language models, 2024a. URL https://arxiv.org/abs/2410.07985 .

Gao et al. (2021) Gao, L., Tow, J., Biderman, S., Black, S., DiPofi, A., Foster, C., Golding, L., Hsu, J., McDonell, K., Muennighoff, N., Phang, J., Reynolds, L., Tang, E., Thite, A., Wang, B., Wang, K., and Zou, A. A framework for few-shot language model evaluation, September 2021. URL https://doi.org/10.5281/zenodo.5371628 .

Gao et al. (2024b) Gao, Z., Niu, B., He, X., Xu, H., Liu, H., Liu, A., Hu, X., and Wen, L. Interpretable contrastive monte carlo tree search reasoning, 2024b. URL https://arxiv.org/abs/2410.01707 .

Glazer et al. (2024) Glazer, E., Erdil, E., Besiroglu, T., Chicharro, D., Chen, E., Gunning, A., Olsson, C. F., Denain, J.-S., Ho, A., de Oliveira Santos, E., Järviniemi, O., Barnett, M., Sandler, R., Vrzala, M., Sevilla, J., Ren, Q., Pratt, E., Levine, L., Barkley, G., Stewart, N., Grechuk, B., Grechuk, T., Enugandla, S. V., and Wildon, M. Frontiermath: A benchmark for evaluating advanced mathematical reasoning in ai, 2024. URL https://arxiv.org/abs/2411.04872 .

Google (2024) Google. Gemini 2.0 flash thinking mode (gemini-2.0-flash-thinking-exp-1219), December 2024. URL https://cloud.google.com/vertex-ai/generative-ai/docs/thinking-mode .

Groeneveld et al. (2024) Groeneveld, D., Beltagy, I., Walsh, P., Bhagia, A., Kinney, R., Tafjord, O., Jha, A. H., Ivison, H., Magnusson, I., Wang, Y., Arora, S., Atkinson, D., Authur, R., Chandu, K. R., Cohan, A., Dumas, J., Elazar, Y., Gu, Y., Hessel, J., Khot, T., Merrill, W., Morrison, J., Muennighoff, N., Naik, A., Nam, C., Peters, M. E., Pyatkin, V., Ravichander, A., Schwenk, D., Shah, S., Smith, W., Strubell, E., Subramani, N., Wortsman, M., Dasigi, P., Lambert, N., Richardson, K., Zettlemoyer, L., Dodge, J., Lo, K., Soldaini, L., Smith, N. A., and Hajishirzi, H. Olmo: Accelerating the science of language models, 2024.

He et al. (2024) He, C., Luo, R., Bai, Y., Hu, S., Thai, Z. L., Shen, J., Hu, J., Han, X., Huang, Y., Zhang, Y., Liu, J., Qi, L., Liu, Z., and Sun, M. Olympiadbench: A challenging benchmark for promoting agi with olympiad-level bilingual multimodal scientific problems, 2024. URL https://arxiv.org/abs/2402.14008 .

Hendrycks et al. (2021) Hendrycks, D., Burns, C., Kadavath, S., Arora, A., Basart, S., Tang, E., Song, D., and Steinhardt, J. Measuring mathematical problem solving with the math dataset, 2021. URL https://arxiv.org/abs/2103.03874 .

Hoffmann et al. (2022) Hoffmann, J., Borgeaud, S., Mensch, A., Buchatskaya, E., Cai, T., Rutherford, E., de Las Casas, D., Hendricks, L. A., Welbl, J., Clark, A., Hennigan, T., Noland, E., Millican, K., van den Driessche, G., Damoc, B., Guy, A., Osindero, S., Simonyan, K., Elsen, E., Rae, J. W., Vinyals, O., and Sifre, L. Training compute-optimal large language models, 2022. URL https://arxiv.org/abs/2203.15556 .

Hou et al. (2025) Hou, Z., Lv, X., Lu, R., Zhang, J., Li, Y., Yao, Z., Li, J., Tang, J., and Dong, Y. Advancing language model reasoning through reinforcement learning and inference scaling, 2025. URL https://arxiv.org/abs/2501.11651 .

Hu et al. (2024) Hu, Y., Shi, W., Fu, X., Roth, D., Ostendorf, M., Zettlemoyer, L., Smith, N. A., and Krishna, R. Visual sketchpad: Sketching as a visual chain of thought for multimodal language models, 2024. URL https://arxiv.org/abs/2406.09403 .

Huang et al. (2024a) Huang, Z., Wang, Z., Xia, S., Li, X., Zou, H., Xu, R., Fan, R.-Z., Ye, L., Chern, E., Ye, Y., Zhang, Y., Yang, Y., Wu, T., Wang, B., Sun, S., Xiao, Y., Li, Y., Zhou, F., Chern, S., Qin, Y., Ma, Y., Su, J., Liu, Y., Zheng, Y., Zhang, S., Lin, D., Qiao, Y., and Liu, P. Olympicarena: Benchmarking multi-discipline cognitive reasoning for superintelligent ai, 2024a. URL https://arxiv.org/abs/2406.12753 .

Huang et al. (2024b) Huang, Z., Zou, H., Li, X., Liu, Y., Zheng, Y., Chern, E., Xia, S., Qin, Y., Yuan, W., and Liu, P. O1 replication journey – part 2: Surpassing o1-preview through simple distillation, big progress or bitter lesson?, 2024b. URL https://arxiv.org/abs/2411.16489 .

Huang et al. (2025) Huang, Z., Geng, G., Hua, S., Huang, Z., Zou, H., Zhang, S., Liu, P., and Zhang, X. O1 replication journey – part 3: Inference-time scaling for medical reasoning, 2025. URL https://arxiv.org/abs/2501.06458 .

Irvine et al. (2023) Irvine, R., Boubert, D., Raina, V., Liusie, A., Zhu, Z., Mudupalli, V., Korshuk, A., Liu, Z., Cremer, F., Assassi, V., Beauchamp, C.-C., Lu, X., Rialan, T., and Beauchamp, W. Rewarding chatbots for real-world engagement with millions of users, 2023. URL https://arxiv.org/abs/2303.06135 .

Jain et al. (2024) Jain, N., Han, K., Gu, A., Li, W.-D., Yan, F., Zhang, T., Wang, S., Solar-Lezama, A., Sen, K., and Stoica, I. Livecodebench: Holistic and contamination free evaluation of large language models for code, 2024. URL https://arxiv.org/abs/2403.07974 .

Kapfer et al. (2025) Kapfer, C., Stine, K., Narasimhan, B., Mentzel, C., and Candes, E. Marlowe: Stanford’s gpu-based computational instrument, January 2025. URL https://doi.org/10.5281/zenodo.14751899 .

Kaplan et al. (2020) Kaplan, J., McCandlish, S., Henighan, T., Brown, T. B., Chess, B., Child, R., Gray, S., Radford, A., Wu, J., and Amodei, D. Scaling laws for neural language models, 2020. URL https://arxiv.org/abs/2001.08361 .

Kim et al. (2024) Kim, E., Suk, J., Kim, S., Muennighoff, N., Kim, D., and Oh, A. Llm-as-an-interviewer: Beyond static testing through dynamic llm evaluation, 2024. URL https://arxiv.org/abs/2412.10424 .

Kwon et al. (2023) Kwon, W., Li, Z., Zhuang, S., Sheng, Y., Zheng, L., Yu, C. H., Gonzalez, J. E., Zhang, H., and Stoica, I. Efficient memory management for large language model serving with pagedattention, 2023. URL https://arxiv.org/abs/2309.06180 .

Labs (2025) Labs, B. Bespoke-stratos: The unreasonable effectiveness of reasoning distillation, 2025. URL https://hf.co/bespokelabs/Bespoke-Stratos-32B . Accessed: 2025-01-22.

Lee et al. (2025) Lee, K.-H., Fischer, I., Wu, Y.-H., Marwood, D., Baluja, S., Schuurmans, D., and Chen, X. Evolving deeper llm thinking, 2025. URL https://arxiv.org/abs/2501.09891 .

Levi (2024) Levi, N. A simple model of inference scaling laws, 2024. URL https://arxiv.org/abs/2410.16377 .

LI et al. (2024) LI, J., Beeching, E., Tunstall, L., Lipkin, B., Soletskyi, R., Huang, S. C., Rasul, K., Yu, L., Jiang, A., Shen, Z., Qin, Z., Dong, B., Zhou, L., Fleureau, Y., Lample, G., and Polu, S. Numinamath, 2024. URL https://github.com/project-numina/aimo-progress-prize/blob/main/report/numina_dataset.pdf .

Lightman et al. (2023) Lightman, H., Kosaraju, V., Burda, Y., Edwards, H., Baker, B., Lee, T., Leike, J., Schulman, J., Sutskever, I., and Cobbe, K. Let’s verify step by step, 2023. URL https://arxiv.org/abs/2305.20050 .

Ling et al. (2017) Ling, W., Yogatama, D., Dyer, C., and Blunsom, P. Program induction by rationale generation : Learning to solve and explain algebraic word problems, 2017. URL https://arxiv.org/abs/1705.04146 .

Liu et al. (2020) Liu, J., Cui, L., Liu, H., Huang, D., Wang, Y., and Zhang, Y. Logiqa: A challenge dataset for machine reading comprehension with logical reasoning, 2020. URL https://arxiv.org/abs/2007.08124 .

Liu et al. (2024) Liu, J., Cohen, A., Pasunuru, R., Choi, Y., Hajishirzi, H., and Celikyilmaz, A. Don’t throw away your value model! generating more preferable text with value-guided monte-carlo tree search decoding, 2024. URL https://arxiv.org/abs/2309.15028 .

Loshchilov & Hutter (2019) Loshchilov, I. and Hutter, F. Decoupled weight decay regularization, 2019.

Luo et al. (2025) Luo, H., Sun, Q., Xu, C., Zhao, P., Lou, J., Tao, C., Geng, X., Lin, Q., Chen, S., Tang, Y., and Zhang, D. Wizardmath: Empowering mathematical reasoning for large language models via reinforced evol-instruct, 2025. URL https://arxiv.org/abs/2308.09583 .

Marten et al. (2025) Marten, R., Vu, T., Ji, C. C.-J., Sharma, K., Pimpalgaonkar, S., Dimakis, A., and Sathiamoorthy, M. Curator: A tool for synthetic data creation. https://github.com/bespokelabsai/curator , January 2025.

Muennighoff et al. (2024) Muennighoff, N., Soldaini, L., Groeneveld, D., Lo, K., Morrison, J., Min, S., Shi, W., Walsh, P., Tafjord, O., Lambert, N., Gu, Y., Arora, S., Bhagia, A., Schwenk, D., Wadden, D., Wettig, A., Hui, B., Dettmers, T., Kiela, D., Farhadi, A., Smith, N. A., Koh, P. W., Singh, A., and Hajishirzi, H. Olmoe: Open mixture-of-experts language models, 2024. URL https://arxiv.org/abs/2409.02060 .

of America (2024) of America, M. A. Aime, February 2024. URL https://artofproblemsolving.com/wiki/index.php/AIME_Problems_and_Solutions/ .

OpenAI (2024) OpenAI. Learning to reason with llms, September 2024. URL https://openai.com/index/learning-to-reason-with-llms/ .

OpenAI (2025) OpenAI. Openai o3-mini, 2025. URL https://openai.com/index/openai-o3-mini/ . Accessed: 2025-02-24.

Phan et al. (2025) Phan, L., Gatti, A., Han, Z., Li, N., Hu, J., Zhang, H., Shi, S., Choi, M., Agrawal, A., Chopra, A., et al. Humanity’s last exam, 2025. URL https://arxiv.org/abs/2501.14249 .

Qin et al. (2024) Qin, Y., Li, X., Zou, H., Liu, Y., Xia, S., Huang, Z., Ye, Y., Yuan, W., Liu, H., Li, Y., and Liu, P. O1 replication journey: A strategic progress report – part 1, 2024. URL https://arxiv.org/abs/2410.18982 .

Qwen et al. (2024) Qwen, :, Yang, A., Yang, B., Zhang, B., Hui, B., Zheng, B., Yu, B., Li, C., Liu, D., Huang, F., Wei, H., Lin, H., Yang, J., Tu, J., Zhang, J., Yang, J., Yang, J., Zhou, J., Lin, J., Dang, K., Lu, K., Bao, K., Yang, K., Yu, L., Li, M., Xue, M., Zhang, P., Zhu, Q., Men, R., Lin, R., Li, T., Xia, T., Ren, X., Ren, X., Fan, Y., Su, Y., Zhang, Y., Wan, Y., Liu, Y., Cui, Z., Zhang, Z., and Qiu, Z. Qwen2.5 technical report, 2024. URL https://arxiv.org/abs/2412.15115 .

Rein et al. (2023) Rein, D., Hou, B. L., Stickland, A. C., Petty, J., Pang, R. Y., Dirani, J., Michael, J., and Bowman, S. R. Gpqa: A graduate-level google-proof q&a benchmark, 2023. URL https://arxiv.org/abs/2311.12022 .

Shi et al. (2024) Shi, Q., Tang, M., Narasimhan, K., and Yao, S. Can language models solve olympiad programming?, 2024. URL https://arxiv.org/abs/2404.10952 .

Snell et al. (2024) Snell, C., Lee, J., Xu, K., and Kumar, A. Scaling llm test-time compute optimally can be more effective than scaling model parameters, 2024. URL https://arxiv.org/abs/2408.03314 .

Srivastava et al. (2023) Srivastava, A., Rastogi, A., Rao, A., Shoeb, A. A. M., Abid, A., Fisch, A., Brown, A. R., Santoro, A., Gupta, A., Garriga-Alonso, A., et al. Beyond the imitation game: Quantifying and extrapolating the capabilities of language models, 2023.

Su et al. (2024) Su, H., Yen, H., Xia, M., Shi, W., Muennighoff, N., yu Wang, H., Liu, H., Shi, Q., Siegel, Z. S., Tang, M., Sun, R., Yoon, J., Arik, S. O., Chen, D., and Yu, T. Bright: A realistic and challenging benchmark for reasoning-intensive retrieval, 2024. URL https://arxiv.org/abs/2407.12883 .

Sun et al. (2024) Sun, L., Han, Y., Zhao, Z., Ma, D., Shen, Z., Chen, B., Chen, L., and Yu, K. Scieval: A multi-level large language model evaluation benchmark for scientific research, 2024. URL https://arxiv.org/abs/2308.13149 .

Team et al. (2025) Team, K., Du, A., Gao, B., Xing, B., Jiang, C., Chen, C., Li, C., Xiao, C., Du, C., Liao, C., Tang, C., Wang, C., Zhang, D., Yuan, E., Lu, E., Tang, F., Sung, F., Wei, G., Lai, G., Guo, H., Zhu, H., Ding, H., Hu, H., Yang, H., Zhang, H., Yao, H., Zhao, H., Lu, H., Li, H., Yu, H., Gao, H., Zheng, H., Yuan, H., Chen, J., Guo, J., Su, J., Wang, J., Zhao, J., Zhang, J., Liu, J., Yan, J., Wu, J., Shi, L., Ye, L., Yu, L., Dong, M., Zhang, N., Ma, N., Pan, Q., Gong, Q., Liu, S., Ma, S., Wei, S., Cao, S., Huang, S., Jiang, T., Gao, W., Xiong, W., He, W., Huang, W., Wu, W., He, W., Wei, X., Jia, X., Wu, X., Xu, X., Zu, X., Zhou, X., Pan, X., Charles, Y., Li, Y., Hu, Y., Liu, Y., Chen, Y., Wang, Y., Liu, Y., Qin, Y., Liu, Y., Yang, Y., Bao, Y., Du, Y., Wu, Y., Wang, Y., Zhou, Z., Wang, Z., Li, Z., Zhu, Z., Zhang, Z., Wang, Z., Yang, Z., Huang, Z., Huang, Z., Xu, Z., and Yang, Z. Kimi k1.5: Scaling reinforcement learning with llms, 2025. URL https://arxiv.org/abs/2501.12599 .

Team (2025) Team, N. Sky-t1: Fully open-source reasoning model with o1-preview performance in $450 budget, 2025. URL https://novasky-ai.github.io/posts/sky-t1 . Accessed: 2025-01-09.

Team (2024) Team, Q. Qwq: Reflect deeply on the boundaries of the unknown, November 2024. URL https://qwenlm.github.io/blog/qwq-32b-preview/ .

Wang et al. (2024a) Wang, J., Meng, F., Liang, Y., and Zhou, J. Drt-o1: Optimized deep reasoning translation via long chain-of-thought, 2024a. URL https://arxiv.org/abs/2412.17498 .

Wang et al. (2024b) Wang, P., Li, L., Shao, Z., Xu, R. X., Dai, D., Li, Y., Chen, D., Wu, Y., and Sui, Z. Math-shepherd: Verify and reinforce llms step-by-step without human annotations, 2024b. URL https://arxiv.org/abs/2312.08935 .

Wang et al. (2021) Wang, S., Liu, Z., Zhong, W., Zhou, M., Wei, Z., Chen, Z., and Duan, N. From lsat: The progress and challenges of complex reasoning, 2021. URL https://arxiv.org/abs/2108.00648 .

Wang et al. (2024c) Wang, Z., Dong, Y., Delalleau, O., Zeng, J., Shen, G., Egert, D., Zhang, J. J., Sreedhar, M. N., and Kuchaiev, O. Helpsteer2: Open-source dataset for training top-performing reward models, 2024c. URL https://arxiv.org/abs/2406.08673 .

Wei et al. (2023) Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le, Q., and Zhou, D. Chain-of-thought prompting elicits reasoning in large language models, 2023. URL https://arxiv.org/abs/2201.11903 .

Welleck et al. (2024) Welleck, S., Bertsch, A., Finlayson, M., Schoelkopf, H., Xie, A., Neubig, G., Kulikov, I., and Harchaoui, Z. From decoding to meta-generation: Inference-time algorithms for large language models, 2024. URL https://arxiv.org/abs/2406.16838 .

Wu et al. (2024a) Wu, T., Lan, J., Yuan, W., Jiao, J., Weston, J., and Sukhbaatar, S. Thinking llms: General instruction following with thought generation, 2024a. URL https://arxiv.org/abs/2410.10630 .

Wu et al. (2024b) Wu, Y., Sun, Z., Li, S., Welleck, S., and Yang, Y. Inference scaling laws: An empirical analysis of compute-optimal inference for problem-solving with language models, 2024b. URL https://arxiv.org/abs/2408.00724 .

Xiang et al. (2025) Xiang, V., Snell, C., Gandhi, K., Albalak, A., Singh, A., Blagden, C., Phung, D., Rafailov, R., Lile, N., Mahan, D., Castricato, L., Franken, J.-P., Haber, N., and Finn, C. Towards system 2 reasoning in llms: Learning how to think with meta chain-of-thought, 2025. URL https://arxiv.org/abs/2501.04682 .

Xie et al. (2023) Xie, Y., Kawaguchi, K., Zhao, Y., Zhao, X., Kan, M.-Y., He, J., and Xie, Q. Self-evaluation guided beam search for reasoning, 2023. URL https://arxiv.org/abs/2305.00633 .

Xin et al. (2024) Xin, H., Guo, D., Shao, Z., Ren, Z., Zhu, Q., Liu, B., Ruan, C., Li, W., and Liang, X. Deepseek-prover: Advancing theorem proving in llms through large-scale synthetic data, 2024. URL https://arxiv.org/abs/2405.14333 .

Xu et al. (2025) Xu, H., Wu, X., Wang, W., Li, Z., Zheng, D., Chen, B., Hu, Y., Kang, S., Ji, J., Zhang, Y., Guo, Z., Yang, Y., Zhang, M., and Zhang, D. Redstar: Does scaling long-cot data unlock better slow-reasoning systems?, 2025. URL https://arxiv.org/abs/2501.11284 .

Yang et al. (2024) Yang, Z., Band, N., Li, S., Candès, E., and Hashimoto, T. Synthetic continued pretraining, 2024. URL https://arxiv.org/abs/2409.07431 .

Yao et al. (2023a) Yao, S., Yu, D., Zhao, J., Shafran, I., Griffiths, T. L., Cao, Y., and Narasimhan, K. Tree of thoughts: Deliberate problem solving with large language models, 2023a. URL https://arxiv.org/abs/2305.10601 .

Yao et al. (2023b) Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., and Cao, Y. React: Synergizing reasoning and acting in language models, 2023b. URL https://arxiv.org/abs/2210.03629 .

Ye et al. (2025a) Ye, Y., Huang, Z., Xiao, Y., Chern, E., Xia, S., and Liu, P. Limo: Less is more for reasoning, 2025a. URL https://arxiv.org/abs/2502.03387 .

Ye et al. (2025b) Ye, Y., Xiao, Y., Mi, T., and Liu, P. Aime-preview: A rigorous and immediate evaluation framework for advanced mathematical reasoning. https://github.com/GAIR-NLP/AIME-Preview , 2025b. GitHub repository.

Yu et al. (2024) Yu, L., Jiang, W., Shi, H., Yu, J., Liu, Z., Zhang, Y., Kwok, J. T., Li, Z., Weller, A., and Liu, W. Metamath: Bootstrap your own mathematical questions for large language models, 2024. URL https://arxiv.org/abs/2309.12284 .

Yuan et al. (2025) Yuan, S., Chen, Z., Xi, Z., Ye, J., Du, Z., and Chen, J. Agent-r: Training language model agents to reflect via iterative self-training, 2025. URL https://arxiv.org/abs/2501.11425 .

Zelikman et al. (2022) Zelikman, E., Wu, Y., Mu, J., and Goodman, N. D. Star: Bootstrapping reasoning with reasoning, 2022. URL https://arxiv.org/abs/2203.14465 .

Zelikman et al. (2024) Zelikman, E., Harik, G., Shao, Y., Jayasiri, V., Haber, N., and Goodman, N. D. Quiet-star: Language models can teach themselves to think before speaking, 2024. URL https://arxiv.org/abs/2403.09629 .

Zhang & Chen (2024) Zhang, H. and Chen, C. Test-time compute scaling laws, 2024. URL https://github.com/hughbzhang/o1_inference_scaling_laws .

Zhang et al. (2023) Zhang, S., Chen, Z., Shen, Y., Ding, M., Tenenbaum, J. B., and Gan, C. Planning with large language models for code generation, 2023. URL https://arxiv.org/abs/2303.05510 .

Zhang et al. (2024a) Zhang, Y., Wu, S., Yang, Y., Shu, J., Xiao, J., Kong, C., and Sang, J. o1-coder: an o1 replication for coding, 2024a. URL https://arxiv.org/abs/2412.00154 .

Zhang et al. (2024b) Zhang, Y., Yang, J., Yuan, Y., and Yao, A. C.-C. Cumulative reasoning with large language models, 2024b. URL https://arxiv.org/abs/2308.04371 .

Zhong et al. (2019) Zhong, H., Xiao, C., Tu, C., Zhang, T., Liu, Z., and Sun, M. Jec-qa: A legal-domain question answering dataset, 2019. URL https://arxiv.org/abs/1911.12011 .

Zhong et al. (2023) Zhong, W., Cui, R., Guo, Y., Liang, Y., Lu, S., Wang, Y., Saied, A., Chen, W., and Duan, N. Agieval: A human-centric benchmark for evaluating foundation models, 2023. URL https://arxiv.org/abs/2304.06364 .

Zhou et al. (2024) Zhou, A., Yan, K., Shlapentokh-Rothman, M., Wang, H., and Wang, Y.-X. Language agent tree search unifies reasoning acting and planning in language models, 2024. URL https://arxiv.org/abs/2310.04406 .

Zhou et al. (2023) Zhou, C., Liu, P., Xu, P., Iyer, S., Sun, J., Mao, Y., Ma, X., Efrat, A., Yu, P., Yu, L., Zhang, S., Ghosh, G., Lewis, M., Zettlemoyer, L., and Levy, O. Lima: Less is more for alignment, 2023. URL https://arxiv.org/abs/2305.11206 .

## Appendix A s1.1

Seven days after our release of s1, we released s1.1. We regenerated traces for our 1,000 samples in s1K using DeepSeek r1 ( DeepSeek-AI et al., 2025 ) to create s1K-1.1 . We use the same training procedure to train our model s1.1 . Other updates since our launch include the release of o3 ( OpenAI, 2025 ) , LIMO ( Ye et al., 2025a ) , and AIME 2025. We consider all these new developments in Table 5 . We find that s1.1 performs significantly better than s1. We also tried distilling from Claude 3.7, which led to worse performance than from r1 (not reported).

## Appendix B Evaluation determinism

We run our evaluations using vLLM ( Kwon et al., 2023 ) as it is faster than the alternatives we tried. However, we find that even when using the same random seeds and greedy sampling, evaluation scores can change significantly across runs: • Different batch sizes causing different results see https://github.com/vllm-project/vllm/issues/5898

• Continuing generations causing different results see https://github.com/vllm-project/vllm/issues/11783

• Changes in tensor parallelism causing different results

As our model generates long reasoning traces prior to its answer, small numeric changes can snowball into large differences. We encounter many generations that are exactly the same for thousands of tokens and then suddenly differ in one token eventually ending up with an entirely different answer. To partly counter this issue we generally run our final evaluations using full precision unless otherwise indicated.

## Appendix C s1K details

### C.1 s1K summary

### C.2 Dataset composition for full 59K questions

### C.3 s1K grading prompt

To grade whether an example is correct for our dataset selection in §2 , we use the prompt in Figure 8 . We grade using Claude 3.5 except for the correctness among the final 1,000 samples, which we graded with Claude 3.7.

### C.4 s1K diversity selection

Algorithm 1 provides our algorithm for selecting data in our diversity selection stage. As mentioned in §2 , we also include samples from some specific benchmarks we perceive as high-quality. None of the samples overlap with our final evaluation.

### C.5 Decontamination

We filter all samples by checking for an 8-gram overlap between the selected examples and the evaluation benchmarks: MATH500, GPTQA Diamond, and AIME24. We exclude questions with more than an 8-gram overlap.

## Appendix D Training details

We take a model that has already been pretrained and instruction tuned and further finetune it for reasoning. Specifically, we use Qwen2.5-32B-Instruct ( Qwen et al., 2024 ) , which on math tasks generally matches or outperforms the larger Qwen2.5-72B-Instruct ( Qwen et al., 2024 ) or other open models ( Dubey et al., 2024 ; Groeneveld et al., 2024 ; Muennighoff et al., 2024 ) . We use token delimiters to separate the thinking stage from the answering stage. We enclose the thinking stage with <|im_start|>think and <|im_start|>answer ; both preceded and followed by a newline. Samples from our dataset are in §D.2 . We use basic fine-tuning hyperparameters: we train for 5 epochs with a batch size of 16 for a total of 315 gradient steps. We train in bfloat16 precision with a learning rate of 1 ​ e − 5 1e-5 warmed up linearly for 5% (16 steps) and then decayed to 0 over the rest of training (299 steps) following a cosine schedule. We use the AdamW optimizer ( Loshchilov & Hutter, 2019 ) with β 1 = 0.9 , β 2 = 0.95 \beta_{1}=0.9,\beta_{2}=0.95 and weight decay of 1 ​ e − 4 1e-4 . We do not compute loss on questions, only on reasoning traces and solutions. We ensure the sequence length is large enough to avoid cutting off any samples; a setting we ablate in §D.1 . The training takes just 26 minutes on 16 NVIDIA H100 GPUs.

### D.1 Training Ablations: Sequence length

Besides our scaling ablations in §5.2 , the main training hyperparameter we ablate is the sequence length used during training. We find that a shorter training sequence length leads to longer reasoning traces at test time. This is because when training with a shorter sequence length the answer section of the training sample is more commonly cut off. Inversely, when the training sequence length is longer, more samples appear in their entirety with the section where the model answers. Thus the model receives more gradient updates where it learns to generate an answer following its chain. This in turn leads to a higher log probability of the answer section at any point during the generation and thus shorter reasoning traces at test time. Performance-wise, we also find that the model trained with a longer sequence length performs better. Thus we opt for the longest training sequence length as it leads to better performance and makes inference more efficient by leading to shorter reasoning traces.

### D.2 Training Samples

, Table 10 , Table 11 contain training samples from s1K .

## Appendix E Test-time scaling details

### E.1 Sequential scaling ablations

#### Token-conditional control

One general approach is to simply tell a model in the prompt precisely how many tokens it should generate. Ideally, the model can keep track of its token count and adjust its generation to finish within the desired limits. We experiment with this approach by training a model with token instructions using the format in Figure 10 (left). We bucket the lengths of the reasoning traces from our 1,000 training examples into powers of two (rounded upwards) and add a corresponding instruction to the user prompt. For example, if the instruction says “Think for up to 2048 tokens”, then the reasoning trace has anywhere between 1024 and 2048 tokens. In Table 12 , we show that after training the model hardly follows the token instruction. It does sometimes generate more tokens when given a higher limit but often overshoots the limit. This may not be unique to our model as prior work suggests that OpenAI o1-mini can also not follow token instructions ( Zhang & Chen, 2024 ) . To prevent exceeding the limit, we test budget forcing the thinking to end once the limit is reached. This leads to perfect control ( Table 12 (lower)). With budget forcing, the scaling trend is also clearer as the model can no longer overshoot the limit when given a small thinking budget. This leads to better test-time scaling values for Token Prompting + budget forcing in Table 3 . To compute Control reported in Table 3 for token-conditional control variants we divide the number of times the thinking tokens in Table 12 are less than the upper limit by the total evaluations (2/5 for without intervention; 5/5 for with intervention).

#### Step-conditional control

Token instructions fail as current models cannot count tokens. To accommodate this lack of capability, we experiment with making the counting more coarse-grained. We partition the reasoning traces into steps and ask the model to think for a specific number of steps rather than tokens. We split our reasoning traces on double newlines into steps, which we find act as intuitive separators based on manual inspection of samples. We bucket our training samples into powers of 2 depending on their number of steps and add a corresponding step instruction following the format in Figure 10 (right). This format is based on early experiments, where we found the model to be more likely to adhere to the step limit when counting down (“3 steps left…2 steps left”) rather than counting up (“Step2…Step3…”). This is likely because if counting down, the final step is always 1, which will act as a strong prior to the model to finish its generation. If counting up, the final step before the answer varies, thus if the model does not remember the original step instruction, it may fail to stop. We conclude the following from our results in Table 13 : (1) The model still struggles to adhere to the step limit. The model sometimes simply continues counting into negative steps, e.g. “-1 steps left”. To solve this issue, we automatically stop the thinking process once 0 steps are reached and then force the model to transition to answering mode by appending the answer token delimiter ( §3 ). This leads to perfect step adherence (lower half of Table 13 ), yet problems remain. (2) The model compensates for fewer steps by making each step longer. For example, when forced to use up to 16 steps vs 256 steps, the model generates an average of 96 tokens per step vs 56. Despite this issue, more steps still clearly correlate with more total thinking tokens in Table 13 and better performance leading to a positive slope (3) Step instructions are more costly than other methods. The step delimiters require around 6 tokens each which for e.g. 64 steps adds up to a total of around 380 tokens. When ignoring the step delimiters in token counts as in Table 13 , the model still requires 7551 thinking tokens on average to achieve only 33.3% on AIME24. To compute Control reported in Table 3 for step-conditional control variants, we first decide that 100 tokens are an upper limit per step and then multiply this number by the steps instructed to arrive at a proxy total token limit, e.g. 1600 for 16 steps instructed. We then check whether the thinking tokens in Table 13 fit within the respective limit for each evaluation run (3/5 for without intervention; 5/5 for with intervention). For the model in Figure 7 , we use a model with step-conditional control trained on an earlier version of our data and using an earlier version of our evaluation codebase.

#### Class-conditional control

OpenAI exposes test-time compute control to users via a ‘‘reasoning_effort’’ API parameter with three possible settings: low, medium, and high. 3 3 3 https://github.com/openai/openai-python/blob/44d6210f101abedeb2dd68507fcffcb329df70ea/src/openai/types/chat/completion_create_params.py#L172 The OpenAI documentation also states that “Reducing reasoning effort can result in faster responses and fewer tokens used on reasoning in a response.” suggesting that they are unable to control test-time compute with guarantees. Thus, maybe OpenAI simply adjusts the prompt or system instruction depending on the reasoning effort desired. In Table 14 , we show that separate prompts for short and long thinking allow us to control thinking time to some extent: Prompting the model to think for longer leads to longer thinking. However, it does not reliably improve performance and control is not precise. The current adherence to control may suffice when we only have three classes, but it might not scale to finer-grained classes. To compute Control reported in Table 3 for this method, we assume that prompting the model to think for a short time in Table 14 should produce fewer tokens than the default for AIME24, while the long prompt should produce more. As 8033 > 6109 8033>6109 and 9651 > 6109 9651>6109 , one out of two follows our expected control thus Control is 50%.

### E.2 Examples for rejection sampling ablation

## Appendix F Version Control

V2 → V3 (2025-03): • Added §A

• Added number of correct samples in §2

V1 → V2 (2025-02): • Added citations and other small writing changes

7

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
