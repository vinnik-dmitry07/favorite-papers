##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Are Emergent Abilities of Large Language Models a Mirage?

###### Abstract

Recent work claims that large language models display emergent abilities , abilities not present in smaller-scale models that are present in larger-scale models. What makes emergent abilities intriguing is two-fold: their sharpness , transitioning seemingly instantaneously from not present to present, and their unpredictability , appearing at seemingly unforeseeable model scales. Here, we present an alternative explanation for emergent abilities: that for a particular task and model family, when analyzing fixed model outputs, emergent abilities appear due the researcher’s choice of metric rather than due to fundamental changes in model behavior with scale. Specifically, nonlinear or discontinuous metrics produce apparent emergent abilities, whereas linear or continuous metrics produce smooth, continuous, predictable changes in model performance. We present our alternative explanation in a simple mathematical model, then test it in three complementary ways: we (1) make, test and confirm three predictions on the effect of metric choice using the InstructGPT/GPT-3 family on tasks with claimed emergent abilities, (2) make, test and confirm two predictions about metric choices in a meta-analysis of emergent abilities on BIG-Bench; and (3) show how to choose metrics to produce never-before-seen seemingly emergent abilities in multiple vision tasks across diverse deep networks. Via all three analyses, we provide evidence that alleged emergent abilities evaporate with different metrics or with better statistics, and may not be a fundamental property of scaling AI models.

## 1 Introduction

Emergent properties of complex systems have long been studied across disciplines, from physics to biology to mathematics. The idea of emergence was popularized by Nobel Prize-winning physicist P.W. Anderson’s “More Is Different” ( 1 ) , which argues that as the complexity of a system increases, new properties may materialize that cannot be predicted even from a precise quantitative understanding of the system’s microscopic details. Recently, the idea of emergence gained significant attention in machine learning due to observations that large language models (LLMs) such as GPT ( 3 ) , PaLM ( 6 ) and LaMDA [ 30 ] exhibit so-called “emergent abilities” ( 33 , 8 , 28 , 3 ) (Fig. 1 ).

The term “emergent abilities of LLMs” was recently and crisply defined as “abilities that are not present in smaller-scale models but are present in large-scale models; thus they cannot be predicted by simply extrapolating the performance improvements on smaller-scale models” [ 33 ] . Such emergent abilities were first discovered in the GPT-3 family [ 3 ] . Subsequent work emphasized the discovery, writing that “[although model] performance is predictable at a general level, performance on a specific task can sometimes emerge quite unpredictably and abruptly at scale” [ 8 ] . These quotations collectively identify the two defining properties of emergent abilities in LLMs: 1. Sharpness , transitioning seemingly instantaneously from not present to present

2. Unpredictability , transitioning at seemingly unforeseeable model scales

These emergent abilities have garnered significant interest, raising questions such as: What controls which abilities will emerge? What controls when abilities will emerge? How can we make desirable abilities emerge faster, and ensure undesirable abilities never emerge? These questions are especially pertinent to AI safety and alignment, as emergent abilities forewarn that larger models might one day, without warning, acquire undesired mastery over dangerous capabilities [ 29 , 10 , 17 , 18 ] .

In this paper, we call into question the claim that LLMs possess emergent abilities, by which we specifically mean sharp and unpredictable changes in model outputs as a function of model scale on specific tasks. Our doubt stems from the observation that emergent abilities seem to appear only under metrics that nonlinearly or discontinuously scale any model’s per-token error rate. For instance, as we later show, > 92 % >92\% of emergent abilities on BIG-Bench tasks [ 28 ] (hand-annotated by [ 32 ] ) appear under either of these two metrics: Multiple Choice Grade = def { 1 if highest probability mass on correct option 0 otherwise \displaystyle\defeq\,\begin{cases}1&\text{if highest probability mass on correct option}\\ 0&\text{otherwise}\end{cases} Exact String Match = def { 1 if output string exactly matches target string 0 otherwise \displaystyle\defeq\,\begin{cases}1&\text{if output string exactly matches target string}\\ 0&\text{otherwise}\end{cases}

This raises the possibility of an alternative explanation for the origin of LLMs’ emergent abilities: sharp and unpredictable changes might be induced by the researcher’s choice of measurement, even though the model family’s per-token error rate changes smoothly, continuously and predictably with increasing scale. Specifically, our alternative posits that emergent abilities are a mirage caused primarily by the researcher choosing a metric that nonlinearly or discontinuously deforms per-token error rates, and secondarily by possessing too few test data to accurately estimate the performance of smaller models, thereby causing smaller models to appear wholly unable to perform the task.

To communicate our alternative explanation, we present it as a simple mathematical model and demonstrate how it quantitatively reproduces the evidence offered in support of emergent abilities of LLMs. We then test our alternative explanation in three complementary ways: 1. We make, test and confirm three predictions based on our alternative hypotheses using the InstructGPT [ 24 ] / GPT-3 [ 3 ] model family.

2. We meta-analyze published benchmarks [ 28 , 33 ] to reveal that emergent abilities only appear for specific metrics, not for model families on particular tasks, and that changing the metric causes the emergence phenomenon to evaporate.

3. We induce never-before-seen, seemingly emergent abilities in multiple architectures across various vision tasks by intentionally changing the metrics used for evaluation.

## 2 Alternative Explanation for Emergent Abilities

How might smooth, continuous, predictable changes in model family performance appear sharp and unpredictable? The answer is that the researcher’s choice of a nonlinear or discontinuous metric can distort the model family’s performance to appear sharp and unpredictable.

To expound, suppose that within a model family, the test loss falls smoothly, continuously and predictably with the number of model parameters. One reason to believe this is the phenomenon known as neural scaling laws: empirical observations that deep networks exhibit power law scaling in the test loss as a function of training dataset size, number of parameters or compute ( 13 , 27 , 11 , 16 , 9 , 12 , 15 , 34 , 14 , 7 , 26 ) . For concreteness, suppose we have a model family of different numbers of parameters N > 0 N>0 and assume that each model’s per-token cross entropy falls as a power law with the number of parameters N N for constants c > 0 , α < 0 c>0,\alpha<0 (Fig. 2 A):

ℒ C ​ E ​ ( N ) = ( N c ) α \mathcal{L}_{CE}(N)=\Big(\frac{N}{c}\Big)^{\alpha}

To be clear, we do not require this particular functional form to hold; rather, we use it for illustrative purposes. Let V V denote the set of possible tokens, p ∈ Δ | V | − 1 p\in\Delta^{|V|-1} denote the true but unknown probability distribution, and p ^ N ∈ Δ | V | − 1 \hat{p}_{N}\in\Delta^{|V|-1} denote the N N -parameter model’s predicted probability distribution. The per-token cross entropy as a function of number of parameters N N is:

ℒ C ​ E ​ ( N ) ​ = def − ∑ v ∈ V p ⁡ ( v ) ​ log ⁡ p ^ N ​ ( v ) \mathcal{L}_{CE}(N)\;\defeq\;-\sum_{v\in V}p(v)\log\hat{p}_{N}(v)

In practice, p p is unknown, so we substitute a one-hot distribution of the observed token v ∗ v^{*} :

ℒ C ​ E ​ ( N ) = − log ⁡ p ^ N ​ ( v ∗ ) \mathcal{L}_{CE}(N)=-\log\hat{p}_{N}(v^{*})

A model with N N parameters then has a per-token probability of selecting the correct token (Fig. 2 B):

p ⁡ ( single token correct ) = exp ⁡ ( − ℒ C ​ E ​ ( N ) ) = exp ⁡ ( − ( N / c ) α ) p(\text{single token correct})=\exp\Big(-\mathcal{L}_{CE}(N)\Big)=\exp\Big(-(N/c)^{\alpha}\Big)

Suppose the researcher then chooses a metric that requires selecting L L tokens correctly. For example, our task might be L L -digit integer addition, and a model’s output is scored 1 1 if all L L output digits exactly match all target digits with no additions, deletions or substitutions, 0 0 otherwise. If the probability each token is correct is independent 1 1 1 While the independence assumption is not true, the approximation yields results qualitatively matching the observed emergence claims. , the probability of scoring 1 1 is:

Accuracy ​ ( N ) ≈ p N ​ ( single token correct ) num. of tokens = exp ⁡ ( − ( N / c ) α ) L \text{Accuracy}(N)\approx p_{N}(\text{single token correct})^{\text{num. of tokens}}=\exp\Big(-(N/c)^{\alpha}\Big)^{L}

This choice of metric nonlinearly scales performance with increasing token sequence length. When plotting performance on a linear-log plot, one sees a sharp, unpredictable emergent ability on longer sequences (Fig. 2 C) that closely matches claimed emergent abilities (inset). What happens if the researcher switches from a nonlinear metric like Accuracy, under which the per-token error rate scales geometrically in target length (App. A.3 ), to an approximately linear metric like Token Edit Distance, under which the per-token error rate scales quasi-linearly in target length (App. A.2 )?

Token Edit Distance ​ ( N ) ≈ L ⁡ ( 1 − p N ​ ( single token correct ) ) = L ⁡ ( 1 − exp ⁡ ( − ( N / c ) α ) ) \text{Token Edit Distance}(N)\approx L\,\Big(1-p_{N}(\text{single token correct})\Big)=L\,\Big(1-\exp\big(-(N/c)^{\alpha}\big)\Big)

The linear metric reveals smooth, continuous, predictable changes in model performance (Fig. 2 E). Similarly, if the researcher uses a discontinuous metric like Multiple Choice Grade, the researcher can find emergent abilities (Fig. 2 D), but switching to a continuous metric like Brier Score removes the emergent ability (Fig. 2 F). In summary, sharp and unpredictable changes with increasing scale can be fully explained by three interpretable factors: (1) the researcher choosing a metric that nonlinearly or discontinuously scales the per-token error rate, (2) having insufficient resolution to estimate model performance in the smaller parameter regime, with resolution 2 2 2 Resolution is defined as “The smallest interval measurable by a scientific instrument; the resolving power.” set by 1 / test dataset size 1/\text{test dataset size} , and (3) insufficiently sampling the larger parameter regime.

## 3 Analyzing InstructGPT/GPT-3’s Emergent Arithmetic Abilities

Previous papers prominently claimed the GPT [ 3 , 24 ] family 3 3 3 As of 2023-03-15, 4 models with 350M, 1.3B, 6.7B, 175B parameters are available via the OpenAI API. displays emergent abilities at integer arithmetic tasks [ 8 , 28 , 33 ] (Fig. 2 E). We chose these tasks as they were prominently presented [ 3 , 8 , 28 , 33 ] , and we focused on the GPT family due to it being publicly queryable. As explained mathematically and visually in Sec. 2 , our alternative explanation makes three predictions: 1. Changing the metric from a nonlinear or discontinuous metric (Fig. 2 CD) to a linear or continuous metric (Fig. 2 EF) should reveal smooth, continuous, predictable performance improvement with model scale.

2. For nonlinear metrics, increasing the resolution of measured model performance by increasing the test dataset size should reveal smooth, continuous, predictable model improvements commensurate with the predictable nonlinear effect of the chosen metric .

3. Regardless of metric, increasing the target string length should predictably affect the model’s performance as a function of the length-1 target performance: approximately geometrically for accuracy and approximately quasilinearly for token edit distance.

To test these predictions, we collected outputs from the InstructGPT/GPT-3 family on two tasks: 2-shot multiplication between two 2-digit integers and 2-shot addition between two 4-digit integers.

#### Prediction: Emergent Abilities Disappear With Different Metrics

On both arithmetic tasks, the GPT family displays emergent abilities if the target has 4 or 5 digits and if the metric is Accuracy (Fig. 3 , top) [ 3 , 8 , 33 ] . However, if one changes from nonlinear Accuracy to linear Token Edit Distance while keeping the models’ outputs fixed , the family’s performance smoothly, continuously and predictably improves with increasing scale (Fig. 3 , bottom). This confirms our first prediction and supports our alternative explanation that the source of emergent abilities is the researcher’s choice of metric, not changes in the model family’s outputs . We also observe that under Token Edit Distance, increasing the length of the target string from 1 to 5 predictably decreases the family’s performance in an approximately quasilinear manner, confirming the first half of our third prediction.

#### Prediction: Emergent Abilities Disappear With Better Statistics

We next tested our second prediction: that even on nonlinear metrics such as accuracy, smaller models do not have zero accuracy, but rather have non-zero above-chance accuracy commensurate with choosing to use accuracy as the metric . In order to accurately measure models’ accuracy, we increased the resolution by generating additional test data, and found that on both arithmetic tasks, all models in the InstructGPT/GPT-3 family achieve above-chance accuracy (Fig. 4 ). This confirms our second prediction. We also observe that as the target string length increases, the accuracy falls approximately geometrically with the length of the target string, confirming the second half of our third prediction. These results additionally demonstrate that the researcher’s choice of metric has the effect that one should predict accuracy to have, i.e., geometric decay with the target length.

## 4 Meta-Analysis of Claimed Emergent Abilities

Analyzing the GPT family is possible because the models are publicly queryable. However, other model families claimed to exhibit emergent abilities are not publicly queryable, nor are their generated outputs publicly available, meaning we are limited to analyzing the published results themselves [ 8 , 33 , 32 ] . Our alternative explanation makes two predictions. 1. At the “population level” of Task-Metric-Model Family triplets, emergent abilities should appear predominantly on specific metrics , not task-model family pairs, and specifically with nonlinear and/or discontinuous metrics.

2. On individual Task-Metric-Model Family triplets that display an emergent ability, changing the metric to a linear and/or continuous metric should remove the emergent ability.

To test these predictions, we used to claimed emergent abilities on BIG-Bench [ 28 , 33 ] due to the benchmark being pertinent and publicly available.

#### Prediction: Emergent Abilities Should Appear with Metrics, not Task-Model Families

If emergent abilities are real, one should expect task-model family pairs to show emergence for all reasonable metrics. However, if our alternative explanation is correct, we should expect emergent abilities to appear only under certain metrics. To test this, we analyzed on which metrics emergent abilities appear. To determine whether a task-metric-model family triplet exhibits a possible emergent ability, we used a metric from previous work [ 28 ] . Letting y i ∈ ℝ y_{i}\in\mathbb{R} denote model performance at model scales x i ∈ ℝ x_{i}\in\mathbb{R} , sorted such that x i < x i + 1 x_{i}<x_{i+1} , the emergence score is: Emergence Score ​ ( { ( x n , y n ) } n = 1 N ) = def sign ​ ( arg ⁡ max i ​ y i − arg ⁡ min i ​ y i ) ​ ( max i ⁡ y i − min i ⁡ y i ) Median ​ ( { ( y i − y i − 1 ) 2 } i ) \text{Emergence Score}\Big(\Big\{(x_{n},y_{n})\Big\}_{n=1}^{N}\Big)\quad\defeq\quad\frac{\text{sign}(\arg\max_{i}y_{i}-\arg\min_{i}y_{i})(\max_{i}y_{i}-\min_{i}y_{i})}{\sqrt{\text{Median}(\{(y_{i}-y_{i-1})^{2}\}_{i})}} (1)

We found that most metrics used in BIG-Bench have zero task-model family pairs that exhibit emergent abilities: of the 39 preferred metrics in BIG-Bench, at most 5 display emergence (Fig. 5 A). Many of the 5 are nonlinear and/or discontinuous, e.g., Exact String Match, Multiple Choice Grade, ROUGE-L-Sum (App. A.4 ). Notably, because BIG-Bench often scores models on tasks using multiple metrics, the lack of emergent abilities under other metrics suggests that emergent abilities do not appear when model outputs are scored using other metrics.

Because emergence score only suggests emergence, we also analyzed hand-annotated task-metric-model family triplets [ 32 ] , which revealed emergent abilities appear with 4 / 39 4/39 metrics (Fig. 5 B), and 2 metrics account for > 92 % >92\% of claimed emergent abilities (Fig. 5 C): Multiple Choice Grade and Exact String Match. Multiple Choice Grade is discontinuous, and Exact String Match is nonlinear.

#### Prediction: Changing Metric Removes Emergent Abilities

To test our second prediction, we focused on the LaMDA family [ 30 ] because its outputs are available through BIG-Bench. For our analysis, we identified tasks on which LaMDA displays emergent abilities with Multiple Choice Grade, then asked whether LaMDA still displays emergent abilities on the same tasks with a different BIG-Bench metric: Brier Score [ 2 ] . Brier Score is a strictly proper scoring rule for predictions of mutually exclusive outcomes; for a binary outcome, the Brier Score simplifies to the mean squared error between the outcome and its predicted probability mass. LaMDA’s emergent abilities on the discontinuous Multiple Choice Grade disappeared when we changed the metric to the continuous Brier Score (Fig. 6 ). These results support our alternative explanation that emergent abilities are induced by the chosen metric.

## 5 Inducing Emergent Abilities in Networks on Vision Tasks

To demonstrate how emergent abilities can be induced by the researcher’s choice of metric, we show how to produce emergent abilities in deep networks of various architectures: fully connected, convolutional, self-attentional. We focus on vision tasks because abrupt transitions in vision models’ capabilities have not been observed to the best of our knowledge; this is one reason why emergence in large language models is considered so interesting. For the convolutional example, see App. B .

#### Emergent Reconstruction of CIFAR100 Natural Images by Nonlinear Autoencoders

We first induce an emergent ability to reconstruct images in shallow (i.e., single hidden layer) nonlinear autoencoders trained on CIFAR100 natural images [ 19 ] . To emphasize that the sharpness of the metric is responsible for emergent abilities, and to show that sharpness extends to metrics beyond Accuracy, we intentionally define a discontinuous metric that measures a network’s ability to reconstruct a dataset as the average number of test data with squared reconstruction error below threshold c c : Reconstruction c ( { x n } n = 1 N ) = def 1 N ∑ n 𝕀 [ | | x n − x ^ n | | 2 < c ] \text{Reconstruction}_{c}\Big(\{x_{n}\}_{n=1}^{N}\Big)\;\defeq\;\frac{1}{N}\sum_{n}\mathbb{I}\Big[||x_{n}-\hat{x}_{n}||^{2}<c\Big] (2) where 𝕀 ⁡ ( ⋅ ) \mathbb{I}(\cdot) denotes an indicator variable and x ^ n \hat{x}_{n} is the autoencoder’s reconstruction of x n x_{n} . The autoencoder family displays smoothly decreasing squared reconstruction error as the number of bottleneck units increases (Fig. 7 B). Under our newly defined Reconstruction c metric and for particular choices of c c , the autoencoder family exhibits a sharp and seemingly unpredictable image reconstruction ability (Fig. 7 C) that qualitatively matches published emergent abilities (Fig. 7 A).

#### Emergent Classification of Omniglot Characters by Autoregressive Transformers

We next induce emergent abilities in Transformers [ 31 ] trained to autoregressively classify Omniglot handwritten characters [ 20 ] , in a setup inspired by recent work [ 5 ] : Omniglot images are embedded by convolutional layers, then sequences of embedded image-image class label pairs are fed into decoder-only transformers. We measure image classification performance on sequences of length L ∈ [ 1 , 5 ] L\in[1,5] , again via subset accuracy : 1 1 if all L L images are classified correctly (Fig. 8 B), 0 otherwise. Causal transformers display a seemingly emergent ability to correctly classify Omniglot handwritten characters (Fig. 8 C) that qualitatively matches published emergent abilities (Fig. 8 A).

## 6 Related Work

Srivastava et al. [ 28 ] observed that while accuracy at a particular task can empirically appear sharp and unpredictable, cross entropy does not; the authors then hypothesized that emergent abilities may be partially attributed to the metric. Our paper converts their discussion into precise predictions, then quantitatively tests the predictions to reveal that: metric choice is likely wholly responsible for emergent abilities; well-known and widely-used metrics (including ones already used by [ 28 ] ) capture graded improvements; emergent abilities do not appear only for tasks involving multiple steps, and indeed appear most commonly on the discontinuous Multiple Choice Grade; metric choice can be used to induce emergent abilities in a novel domain (vision) in diverse architectures and tasks.

Caballero et al. [ 4 ] explain emergence by assuming a piece-wise power law functional form; under this view, emergent abilities are real, caused by a change in the governing power law. In contrast, our work suggests that emergent abilities are induced by the researcher, even under a single power law. Michaud et al. [ 25 ] posit that emergent abilities may be real under strong data assumptions.

## 7 Discussion

Our paper presents an alternative explanation for claimed emergent abilities of large language models. For a fixed task and a fixed model family, the researcher can choose a metric to create an emergent ability or choose a metric to ablate an emergent ability. Ergo, emergent abilities may be creations of the researcher’s choices, not a fundamental property of the model family on the specific task. We emphasize that nothing in this paper should be interpreted as claiming that large language models cannot display emergent abilities; rather, our message is that previously claimed emergent abilities in [ 3 , 8 , 28 , 33 ] might likely be a mirage induced by researcher analyses.

Our paper has several implications. Firstly, a task and a metric are distinct and meaningful choices when constructing a benchmark. Secondly, when choosing metric(s), one should consider the metric’s effect on the per-token error rate and adapt their measuring process accordingly, e.g., if one chooses accuracy, one should make sure to have sufficient data to accurately measure accuracy to avoid the risk of drawing invalid scientific conclusions. Thirdly, when making claims about capabilities of large models, including proper controls is critical. In this particular setting, emergent abilities claims are possibly infected by a failure to control for multiple comparisons. In BIG-Bench alone, there are ≥ \geq 220 tasks, ∼ 40 \sim 40 metrics per task, ∼ 10 \sim 10 model families, for a total of ∼ 10 6 \sim 10^{6} task-metric-model family triplets, meaning probability that no task-metric-model family triplet exhibits an emergent ability by random chance might be small. Fourthly, scientific progress can be hampered when models and their outputs are not made public for independent scientific investigation.

## References

[1] Philip W Anderson. More is different: broken symmetry and the nature of the hierarchical structure of science. Science , 177(4047):393–396, 1972.

[2] Glenn W Brier et al. Verification of forecasts expressed in terms of probability. Monthly weather review , 78(1):1–3, 1950.

[3] Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are few-shot learners. Advances in neural information processing systems , 33:1877–1901, 2020.

[4] Ethan Caballero, Kshitij Gupta, Irina Rish, and David Krueger. Broken neural scaling laws. arXiv preprint arXiv:2210.14891 , 2022.

[5] Stephanie CY Chan, Adam Santoro, Andrew Kyle Lampinen, Jane X Wang, Aaditya K Singh, Pierre Harvey Richemond, James McClelland, and Felix Hill. Data distributional properties drive emergent in-context learning in transformers. In Advances in Neural Information Processing Systems , 2022.

[6] Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung, Charles Sutton, Sebastian Gehrmann, et al. Palm: Scaling language modeling with pathways. arXiv preprint arXiv:2204.02311 , 2022.

[7] Aidan Clark, Diego De Las Casas, Aurelia Guy, Arthur Mensch, Michela Paganini, Jordan Hoffmann, Bogdan Damoc, Blake Hechtman, Trevor Cai, Sebastian Borgeaud, et al. Unified scaling laws for routed language models. In International Conference on Machine Learning , pages 4057–4086. PMLR, 2022.

[8] Deep Ganguli, Danny Hernandez, Liane Lovitt, Amanda Askell, Yuntao Bai, Anna Chen, Tom Conerly, Nova Dassarma, Dawn Drain, Nelson Elhage, et al. Predictability and surprise in large generative models. In 2022 ACM Conference on Fairness, Accountability, and Transparency , pages 1747–1764, 2022.

[9] Mitchell A Gordon, Kevin Duh, and Jared Kaplan. Data and parameter scaling laws for neural machine translation. In Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing , pages 5915–5922, 2021.

[10] Dan Hendrycks. Detecting emergent behavior. 2022.

[11] Tom Henighan, Jared Kaplan, Mor Katz, Mark Chen, Christopher Hesse, Jacob Jackson, Heewoo Jun, Tom B Brown, Prafulla Dhariwal, Scott Gray, et al. Scaling laws for autoregressive generative modeling. arXiv preprint arXiv:2010.14701 , 2020.

[12] Danny Hernandez, Jared Kaplan, Tom Henighan, and Sam McCandlish. Scaling laws for transfer. arXiv preprint arXiv:2102.01293 , 2021.

[13] Joel Hestness, Sharan Narang, Newsha Ardalani, Gregory Diamos, Heewoo Jun, Hassan Kianinejad, Md Patwary, Mostofa Ali, Yang Yang, and Yanqi Zhou. Deep learning scaling is predictable, empirically. arXiv preprint arXiv:1712.00409 , 2017.

[14] Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, et al. Training compute-optimal large language models. arXiv preprint arXiv:2203.15556 , 2022.

[15] Andy L Jones. Scaling scaling laws with board games. arXiv preprint arXiv:2104.03113 , 2021.

[16] Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, and Dario Amodei. Scaling laws for neural language models. arXiv preprint arXiv:2001.08361 , 2020.

[17] Victoria Krakovna, Vikrant Varma, Ramana Kumar, and Mary Phuong. Refining the sharp left turn threat model, part 1: claims and mechanisms. 2022.

[18] Victoria Krakovna, Vikrant Varma, Ramana Kumar, and Mary Phuong. Refining the sharp left turn threat model, part 2: applying alignment techniques. 2022.

[19] Alex Krizhevsky. Learning multiple layers of features from tiny images. Technical report, 2009.

[20] Brenden M Lake, Ruslan Salakhutdinov, and Joshua B Tenenbaum. Human-level concept learning through probabilistic program induction. Science , 350(6266):1332–1338, 2015.

[21] Yann LeCun. The mnist database of handwritten digits. http://yann. lecun. com/exdb/mnist/ , 1998.

[22] Yann LeCun, Léon Bottou, Yoshua Bengio, and Patrick Haffner. Gradient-based learning applied to document recognition. Proceedings of the IEEE , 86(11):2278–2324, 1998.

[23] Chin-Yew Lin. Rouge: A package for automatic evaluation of summaries. In Text summarization branches out , pages 74–81, 2004.

[24] Ryan Lowe and Jan Leike. Aligning language models to follow instructions. 2022.

[25] Eric J. Michaud, Ziming Liu, Uzay Girit, and Max Tegmark. The quantization model of neural scaling, 2023.

[26] Oren Neumann and Claudius Gros. Scaling laws for a multi-agent reinforcement learning model. arXiv preprint arXiv:2210.00849 , 2022.

[27] Jonathan S Rosenfeld, Amir Rosenfeld, Yonatan Belinkov, and Nir Shavit. A constructive prediction of the generalization error across scales. arXiv preprint arXiv:1909.12673 , 2019.

[28] Aarohi Srivastava, Abhinav Rastogi, Abhishek Rao, Abu Awal Md Shoeb, Abubakar Abid, Adam Fisch, Adam R Brown, Adam Santoro, Aditya Gupta, Adrià Garriga-Alonso, et al. Beyond the imitation game: Quantifying and extrapolating the capabilities of language models. arXiv preprint arXiv:2206.04615 , 2022.

[29] Jacob Steinhardt. Future ml systems will be qualitatively different. 2022.

[30] Romal Thoppilan, Daniel De Freitas, Jamie Hall, Noam Shazeer, Apoorv Kulshreshtha, Heng-Tze Cheng, Alicia Jin, Taylor Bos, Leslie Baker, Yu Du, et al. Lamda: Language models for dialog applications. arXiv preprint arXiv:2201.08239 , 2022.

[31] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, and Illia Polosukhin. Attention is all you need. Advances in neural information processing systems , 30, 2017.

[32] Jason Wei. 137 emergent abilities of large language models. 2022.

[33] Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma, Denny Zhou, Donald Metzler, et al. Emergent abilities of large language models. arXiv preprint arXiv:2206.07682 , 2022.

[34] Xiaohua Zhai, Alexander Kolesnikov, Neil Houlsby, and Lucas Beyer. Scaling vision transformers. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition , pages 12104–12113, 2022.

## Appendix A Approximate Behavior of Metrics on Sequential Data

How do different metrics behave when used to measure autoregressive model outputs? Precisely answering this question is tricky and possibly analytically unsolvable, so we provide an approximate answer here.

Notationally, we consider N N test data of length L L (here, length is measured in tokens) with targets denoted t n ​ = def ( t n1 , t n2 , … ​ t nL ) t_{n}\defeq(t_{n1},t_{n2},...t_{nL}) , the autoregressive model has a true-but-unknown per-token error probability of ϵ ∈ [ 0 , 1 ] \epsilon\in[0,1] and the model outputs prediction t ^ n ​ = def ( t ^ n1 , t ^ n2 , … ​ t ^ nL ) \hat{t}_{n}\defeq(\hat{t}_{n1},\hat{t}_{n2},...\hat{t}_{nL}) . This assumes that the model’s per-token error probability is constant, which is empirically false, but modeling the complex dependencies of errors is beyond our scope.

### A.1 Per-Token Error Probability is Resolution-Limited

Note that because we have N N test data, each of length L L , our resolution for viewing the per-token error probability ϵ \epsilon is limited by 1 / N ​ L 1/NL . Here, resolution refers to “the smallest interval measurable by a scientific instrument; the resolving power.” To explain what resolution means via an example, suppose one wants to measure a coin’s probability of yielding heads. After a single coin flip, only two outcomes are possible (H, T), so the resolution-limited probability of heads is either 0 0 or 1 1 . After two coin flips, four outcomes are possible (HH, HT, TH, TT), so the resolution-limited probability of heads is now one of 0 , 0.5 , 1 0,0.5,1 . After F F coin flips, we can only resolve the coin’s probability of yielding heads up to 1 / F 1/F . Consequently, we introduce a resolution-limited notation: ⌊ a ⌉ b ​ = def a rounded to the nearest integer multiple of 1 / b \lfloor a\rceil_{b}\defeq\text{$a$ rounded to the nearest integer multiple of $1/b$} (3)

### A.2 Token Edit Distance

We first consider an adaptation of the Levenshtein (string edit) distance for models that function on tokens rather than characters, an adaptation we term the token edit distance . The token edit distance between two token sequences t n , t n ^ t_{n},\hat{t_{n}} is defined as the integer number of additions, deletions or substitutions necessary to transform t n t_{n} into t ^ n \hat{t}_{n} (or vice versa).

Token Edit Distance ​ ( t n , t ^ n ) \displaystyle\text{Token Edit Distance}(t_{n},\hat{t}_{n}) = def Num Substitutions + Num. Additions + Num. Deletions \displaystyle\defeq\text{Num Substitutions}+\text{Num. Additions}+\text{Num. Deletions} (4) = ∑ ℓ = 1 L 𝕀 [ t n ​ ℓ ≠ t ^ n ​ ℓ ] + Num. Additions + Num. Deletions \displaystyle=\sum_{\ell=1}^{L}\mathbb{I}[t_{n\ell}\neq\hat{t}_{n\ell}]+\text{Num. Additions}+\text{Num. Deletions} (5) ≥ ∑ ℓ = 1 L 𝕀 [ t n ​ ℓ ≠ t ^ n ​ ℓ ] \displaystyle\geq\sum_{\ell=1}^{L}\mathbb{I}[t_{n\ell}\neq\hat{t}_{n\ell}] (6)

The expected token edit distance is therefore:

𝔼 ⁡ [ Token Edit Distance ​ ( t n , t ^ n ) ] \displaystyle\mathbb{E}[\text{Token Edit Distance}(t_{n},\hat{t}_{n})] ≥ 𝔼 [ ∑ ℓ = 1 L 𝕀 [ t n ​ ℓ ≠ t ^ n ​ ℓ ] ] \displaystyle\geq\mathbb{E}[\sum_{\ell=1}^{L}\mathbb{I}[t_{n\ell}\neq\hat{t}_{n\ell}]] (7) = ∑ ℓ = 1 L p ⁡ ( t n ​ ℓ ≠ t ^ n ​ ℓ ) \displaystyle=\sum_{\ell=1}^{L}p(t_{n\ell}\neq\hat{t}_{n\ell}) (8) ≈ L ⁡ ( 1 − ϵ ) \displaystyle\approx L(1-\epsilon) (9)

The resolution-limited expected token edit distance is therefore:

⌊ 𝔼 ⁡ [ Token Edit Distance ​ ( t n , t ^ n ) ] ⌉ N ​ L ≥ L ⁡ ( 1 − ⌊ ϵ ⌉ N ​ L ) \lfloor\mathbb{E}[\text{Token Edit Distance}(t_{n},\hat{t}_{n})]\rceil_{NL}\geq L\Big(1-\lfloor\epsilon\rceil_{NL}\Big) (10)

From this, we see that the expected token edit distance scales approximately linearly with the resolution-limited per-token probability. The real rate is slightly higher than linear because additions and deletions contribute an additional non-negative cost, but modeling this requires a model of how likely the model is to overproduce or underproduce tokens, which is something we do not currently possess.

### A.3 Accuracy

Accuracy ​ ( t n , t ^ n ) \displaystyle\text{Accuracy}(t_{n},\hat{t}_{n}) = def 𝕀 [ No additions ] 𝕀 [ No deletions ] ∏ l = 1 L 𝕀 [ t nl = t ^ nl ] \displaystyle\defeq\mathbb{I}[\text{No additions}]\,\mathbb{I}[\text{No deletions}]\,\prod_{l=1}^{L}\mathbb{I}[t_{nl}=\hat{t}_{nl}] (11) ≈ ∏ l = 1 L 𝕀 [ t n ​ l = t ^ n ​ l ] \displaystyle\approx\prod_{l=1}^{L}\mathbb{I}[t_{nl}=\hat{t}_{nl}] (12)

As with the Token Edit Distance (App. A.3 ), we ignore how likely the language model is to overproduce or underproduce tokens because we do not have a good model of this process. Continuing along,

𝔼 ⁡ [ log ⁡ Accuracy ] \displaystyle\mathbb{E}[\log\text{Accuracy}] = ∑ l 𝔼 [ log 𝕀 [ t n ​ l = t ^ n ​ l ] ] \displaystyle=\sum_{l}\mathbb{E}[\log\mathbb{I}[t_{nl}=\hat{t}_{nl}]] (13) ≤ ∑ l log 𝔼 [ 𝕀 [ t n ​ l = t ^ n ​ l ] ] \displaystyle\leq\sum_{l}\log\mathbb{E}[\mathbb{I}[t_{nl}=\hat{t}_{nl}]] (14) ≈ L ​ log ⁡ ( 1 − ϵ ) \displaystyle\approx L\log(1-\epsilon) (15)

Taking an approximation that would make most mathematicians cry:

𝔼 ⁡ [ Accuracy ] \displaystyle\mathbb{E}[\text{Accuracy}] ≈ exp ⁡ ( 𝔼 ⁡ [ log ⁡ Accuracy ] ) \displaystyle\approx\exp(\mathbb{E}[\log\text{Accuracy}]) (16) = ( 1 − ϵ ) L \displaystyle=(1-\epsilon)^{L} (17)

This reveals that accuracy approximately falls geometrically with target token length. The resolution-limited expected accuracy is therefore:

⌊ 𝔼 ⁡ [ Accuracy ] ⌉ N ​ L = ⌊ ( 1 − ϵ ) L ⌉ N ​ L \lfloor\mathbb{E}[\text{Accuracy}]\rceil_{NL}=\lfloor(1-\epsilon)^{L}\rceil_{NL} (19)

From this we can see that choosing a nonlinear metric like Accuracy is affected significantly more by limited resolution because Accuracy forces one to distinguish quantities that decay rapidly.

### A.4 ROUGE-L-Sum

Another BIG-Bench metric [ 28 ] is ROUGE-L-Sum [ 23 ] , a metric based on the longest common subsequence (LCS) between two sequences. Section 3.2 of [ 23 ] gives the exact definition, but the key property is that ROUGE-L-Sum measures the “union” LCS, which means “stitching” together LCSs across the candidate and multiple references. As explained in the original paper: if the candidate sequence is c = w 1 ​ w 2 ​ w 3 ​ w 4 ​ w 5 c=w_{1}w_{2}w_{3}w_{4}w_{5} , and if there are two reference sequences r 1 = w 1 ​ w 2 ​ w 6 ​ w 7 ​ w 8 r_{1}=w_{1}w_{2}w_{6}w_{7}w_{8} and r 2 = w 1 ​ w 3 ​ w 8 ​ w 9 ​ w 5 r_{2}=w_{1}w_{3}w_{8}w_{9}w_{5} , then L ​ C ​ S ​ ( r 1 , c ) = w 1 ​ w 2 LCS(r_{1},c)=w_{1}w_{2} and L ​ C ​ S ​ ( r 2 , c ) = w 1 ​ w 3 ​ w 5 LCS(r_{2},c)=w_{1}w_{3}w_{5} , then the union -LCS of c , r 1 , r 2 c,r_{1},r_{2} is w 1 ​ w 2 ​ w 3 ​ w 5 w_{1}w_{2}w_{3}w_{5} , with length 4. Intuitively, this disproportionately benefits models with smaller error rates because their mistakes can be “stitched” across multiple references; this is confirmed in simulation (Fig. 9 ).

## Appendix B Inducing Emergent Abilities in Networks on Vision Tasks

### B.1 Emergent Classification of MNIST Handwritten Digits by Convolutional Networks

We begin by inducing an emergent classification ability in a LeNet convolutional neural network family [ 22 ] , trained on the MNIST handwritten digits dataset [ 21 ] . This family displays smoothly increasing test accuracy as the number of parameters increase (Fig. 10 B). To emulate the accuracy metric used by emergence papers [ 8 , 33 , 28 ] , we use subset accuracy : 1 if the network classifies K K out of K K (independent) test data correctly, 0 otherwise. Under this definition of accuracy, the model family displays an “emergent” ability to correctly classify sets of MNIST digits as K K increases from 1 1 to 5 5 , especially when combined with sparse sampling of model sizes (Fig. 10 C). This convolutional family’s emergent classification ability qualitatively matches published emergent abilities, e.g., at the BIG-Bench Grounded Mappings task [ 33 ] (Fig. 10 A).

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
