##### Report GitHub Issue

Content selection saved. Describe the issue below:

# gzip Predicts Data-dependent Scaling Laws

###### Abstract

Past work has established scaling laws that predict the performance of a neural language model (LM) as a function of its parameter count and the number of tokens it’s trained on, enabling optimal allocation of a fixed compute budget. Are these scaling laws agnostic to training data as some prior work suggests? We generate training datasets of varying complexities by modulating the syntactic properties of a PCFG, finding that 1) scaling laws are sensitive to differences in data complexity and that 2) gzip , a compression algorithm, is an effective predictor of how data complexity impacts scaling properties. We propose a new data-dependent scaling law for LM’s that accounts for the training data’s gzip -compressibility; its compute-optimal frontier increases in dataset size preference (over parameter count preference) as training data becomes harder to compress.

## 1 Introduction

A neural network’s performance generally increases as more compute is allocated for training. When scaling compute, one must decide whether to increase a model’s parameter count or increase the dataset’s size—these must trade-off within a fixed compute budget. Scaling laws can tell us what specific allocation (i.e. parameters v.s. data) will maximize performance given a compute budget. Much work has explored scaling laws for neural LM’s [ Kaplan et al., 2020 ] , generally concluding that parameter & training token count should be scaled 1-to-1 [ Hoffmann et al., 2022 ] .

However, most prior work on scaling laws for LM’s have been estimated from transformers trained on scraped web text. Of course, this is quite a specific data distribution, so we may naturally ask whether the scaling laws extrapolated from such web text datasets generalize to other distributions. Furthermore, it is generally understood that the art of training data mixture is the ‘secret sauce’ that enables frontier industry labs to continually deliver state-of-the-art LLMs [ Penedo et al., 2024 , Penedo et al., 2023 , Xie et al., 2024 ] . Considering that improving data quality can significantly raise LM performance [ Gunasekar et al., 2023 ] and that scaling laws in reinforcement learning have been shown to scale with game difficulty [ Jones, 2021 ] , we may hypothesize that current LM scaling laws (e.g. Chinchilla [ Hoffmann et al., 2022 ] ) are individual web-text-specific cases of a more general scaling law conditioned on properties of the training data.

Then, what properties of a training dataset of token sequences are neural scaling laws sensitive to? In other words, what can we measure about our data to more accurately predict the optimal compute allocation for training? Furthermore, is data-dependence of scaling laws only of theoretical interest, or can laws be considerably different for real-world datasets?

In order to study these questions, we seek a textual data setting where we can intuitively control its complexity as well as open avenues for information-theoretic understandings of why scaling laws are data-dependent. We therefore settle on probabilistic context-free grammars (PCFG) [ Chomsky, 1956 ] which are relatively naturalistic (can model natural language, code, etc.), controllable in syntactic complexity, and follow some well-understood information-theoretic principles [ Chi, 1999 ] .

We generate 6 datasets of varying complexity by modulating syntactic properties of a PCFG. For each of these datasets, we train LMs of 6 different sizes (4.4M to 1.4B parameters) and record results at 6 different train step counts (100K to 100M tokens). We then fit a scaling law for each dataset [ Muennighoff et al., 2023 ] , finding meaningful shifts in the law’s parameters as syntactic complexity increases. Following prior work on entropy of formal grammars [ Arora et al., 2022 ] , we use median compressibility of each token sequence in a dataset as a measure of complexity that is straightforward to compute with gzip [ Gailly and Adler, 1992 ] .

We find that as the training data becomes less compressible (more complex), the scaling law’s compute-optimal frontier gradually increases its preference for dataset size over parameter count. We then measure the compressibility of real-world code & natural language datasets, showing that the former is considerably more compressible and thus subject to a predictably different scaling law. With some napkin math, we estimate that we could reach the performance of StarCoder [ Li et al., 2023 ] with 24% fewer FLOPs ($278,000 in H100 hours) since our compute-optimal scaling adjusts for data complexity.

## 2 Related Work

### 2.1 Scaling Laws

Early work established that a neural network’s test error is a power law of training dataset size [ Cortes et al., 1993 ] , model parameter count [ Rosenfeld et al., 2019 ] , and that the relationship holds over many orders of magnitude [ Hestness et al., 2017 ] . Kaplan et al. [2020] applied scaling laws to transformer-based language models and identified a compute-optimal frontier along which parameter & dataset size should be scaled. Hoffmann et al. [2022] propose the Chinchilla scaling laws, finding that Kaplan et al. [2020] and Rae et al. [2021] overparameterized their models and that the compute-optimal frontier requires parameter & dataset size to be scaled equally (rather than parameters scaling at 3x the rate of data).

Sorscher et al. [2022] find that we can reach exponential (rather than power law) scaling on dataset size by pruning out redundant examples that do not provide much information to learn from. Liu and Tegmark [2023] identify a mechanistic explanation of why scaling follows a power law on model width.

Aghajanyan et al. [2023] extend the Chinchilla scaling laws to a variety of modalities such as speech, image-text, and code. Caballero et al. [2023] propose a novel functional form for scaling laws that better models complex non-monotonic behavior and also apply it to several modalities including code. Both these works and Hoffmann et al. [2022] (in Appendix C) find that scaling behavior for code is different than for natural language —code is easier to learn and its compute-optimal frontier prefers parameters slightly over data. Bi et al. [2024] cursorily investigate scaling laws across datasets of different qualities, finding that cleaner & higher quality data results in the “model scaling exponent increasing” because “high-quality data usually implies logical clarity and less predictive difficulty after sufficient training”. However, none of these works identify an underlying general principle that explains why scaling behavior varies across data modalities & complexities (or even just between code and natural language).

Meanwhile, Jones [2021] explores scaling laws in the context of board games, finding that “the compute required for a desired level of performance can be calculated directly from the board size”. If scaling laws smoothly scale with data complexity in the board game setting, do they also smoothly scale with textual data complexity? And how might we measure a text dataset’s complexity?

### 2.2 Syntax & Information Theory

A long history of work in linguistics has sought to apply information-theoretic measures to natural language [ Shannon, 1951 , Cherry et al., 1953 , Harris, 1991 , Piantadosi et al., 2011 ] . Specifically, entropy (a fairly abstract information-theoretic measure) can be operationalized in a number of concrete ways to measure the informational complexity of a linguistic distribution [ Arora et al., 2022 ] . One way to determine the ‘goodness’ of an entropy measure over sequences is whether it grows as the syntactic complexity of a language increases (e.g. more production rules, more non-terminals, longer right-hand sides). While entropy is straightforward to compute in closed-form on simple formal languages (i.e. Type 3 Chomskyan grammars, generated by Finite State Automata) [ Grenander, 1967 , Sánchez et al., 2018 ] , for Context-free (Type 2) grammars, we must estimate entropy from a set of generated samples [ Chi, 1999 , Corazza and Satta, 2007 ] .

Leveraging the widely-recognized relationship between entropy and compression [ Shannon, 1948 , Huffman, 1952 , Ziv and Lempel, 1977 ] , we can use gzip [ Gailly and Adler, 1992 ] , a lossless compression utility that implements DEFLATE [ Deutsch, 1996 ] (a combination of Huffman coding & the Lempel-Ziv algorithm) to estimate the entropy of sampled linguistic sequences.

Delétang et al. [2023] adapt language models as lossless compressors of token sequences and provide new insights on scaling laws from this compression perspective, finding that beyond a critical model size, the compression rate (accounting for parameter count) reverses its improvement. In a somewhat similar vein, Jiang et al. [2023] use gzip with k-Nearest-Neighbors to beat neural text embeddings. Importantly, they both brought to attention the effectiveness of compression algorithms for heuristically measuring the structure learned by language models [ Huang et al., 2024 ] . Another line of recent work investigates the learnability of different languages by LMs, finding that natural languages vary in their learnability [ Cotterell et al., 2018 ] and that LMs struggle to model syntactically ‘impossible’ languages [ Kallini et al., 2024 ] .

## 3 Modulating Data Complexity via Syntactic Properties of a PCFG

Probabilistic Context-Free Grammars (PCFGs) are a fundamental tool in computational linguistics for modeling the syntax of natural languages. A PCFG extends the concept of a standard Context-Free Grammar (CFG) by associating probabilities with its production rules, enabling the representation of language ambiguity and variability in a quantifiable manner. These grammars generate trees where each node represents a syntactic category, and the edges represent production rules applied to generate sentences. When generating sentences from a PCFG, we probabilistically sample sequences of production rules to apply until all leaves of the tree are terminals (actual vocab tokens).

We can control the syntactic properties of a PCFG to naturalistically modulate the complexity of a textual dataset that we sample from its generated sentences. Specifically, our PCFG creation function accepts arguments for the number of terminals, number of non-terminals, the maximum length of the right-hand side of a production rule, and the maximum number of production rules allowed for any non-terminal (i.e. if this is 1, a given non-terminal will always lead to the same right-hand side). Intuitively, as each of these values increase, the language’s syntactic complexity also increases.

To create a PCFG from the above arguments, for each non-terminal, we randomly choose its number of productions (RHS options), each of those production’s length, instantiate a production rule by randomly sampling from the terminals & non-terminals, and assign it a probability normalized by the total RHS options for the non-terminal. We then collect all the generated production rules for all the non-terminals and instantiate a grammar using the PCFG package [ Breydo, 2021 ] built on NLTK [ Bird and Loper, 2004 ] .

We can then use the grammar that we have randomly (within given constraints) created to probabilistically sample sentences to construct a dataset of token sequences. To make it easier later to compare training across grammars that produce sentences of different average lengths, we decide to sample sentences into documents of the same token count (our LM’s context length). We sample sentences from our grammar until we’ve filled up the context length, and if we overflow, we simply truncate the sequence.

Sentences are composed of terminals that are just integers and can thus be treated as token IDs for our LM; we concatenate sentences with the unused integer 0, effectively corresponding to a period in natural language. To clarify, we do not generate strings that ‘look’ like natural language and must be tokenized—the PCFG generates sequences of token IDs themselves. Now, we can generate 6 datasets of token sequences with varying complexities from just 6 sets of initial grammatical constraints.

### 3.1 gzip -compressibility Measures Syntactic Complexity

Now we must choose a metric to estimate the complexity of our datasets. While for our PCFG-generated data, we could use a trivial function of its syntactic properties (e.g. number of non-terminals plus median production rule length), we would only be able to apply this metric to datasets where we precisely know the grammar that generated the data. Instead, we need a measure of complexity that we can apply to real-world token sequence datasets so that we can see whether our data-sensitive scaling results on PCFGs generalize to real-world datasets. While one might try to use grammar induction to identify the underlying syntax of a real-world dataset and then compute complexity from its syntactic properties, this is computationally intensive and difficult with noisy web-text data.

Therefore, as explained in Sec. 2.2 , we choose to use a compression algorithm, gzip , to estimate the complexity of a dataset by virtue of considerable theoretical work establishing compressibility − 1 ∝ \text{compressibility}^{-1}\propto entropy [ Shannon, 1948 ] and entropy ∝ \propto syntactic complexity [ Chi, 1999 ] . Specifically, for each token sequence in a sample of 1000 from the dataset, we apply gzip and compute the ratio of the size (in bytes) of the compressed data to the original data. We then compute the median and standard deviation in compressibility, confirming that grammars with higher syntactic complexity result in datasets that are more difficult to compress.

In Tab. 1 , we list the syntactic parameters for each grammar and the compression ratio we measured of token sequences sampled from the grammar. Observe that as non-terminals (grammatical categories), terminals (tokens), right-hand side options, and right-hand side length increase, the gzip -compressibility also increases (i.e. it becomes harder to compress). We plot these datasets alongside natural language & code in Fig. 1 , showing how some PCFG datasets are more similar in complexity to code (the ones that are easier to compress) while others are more similar to natural language.

## 4 Are Scaling Laws Sensitive to Data Complexity?

To identify the scaling law for a dataset, we train a set of models of varying sizes (4.2M, 8.8M, 20.3M, 59.0M, 275.3M, 1.4B parameters; architectural specifics in Tab. 6 ) on varying size subsets of the data (100K, 1M, 5M, 20M, 50M, 100M tokens) and fit a power law on the resulting final losses of all training runs. Most experiments were run on a cluster of 4 Nvidia A100’s with 80 GB VRAM each using PyTorch FSDP [ Paszke et al., 2019 , Zhao et al., 2023 ] . We use a batch size of 32, single epoch training, the A ​ d ​ a ​ m ​ W AdamW optimizer [ Loshchilov and Hutter, 2017 ] , and a learning rate starting from 5 ​ e − 5 5\mathrm{e}{-5} and cosine decayed over the number of train steps [ Loshchilov and Hutter, 2016 ] .

As intuitively expected, the more compressible a dataset is (lower compressibility ratio), the faster that models regardless of size will converge (Fig. 2 ). While this shows that we need more compute to model more complex datasets (which is in and of itself notable), we need more evidence to determine if the compute-optimal frontier directionally shifts based on data complexity. To establish such a non-trivial sensitivity of scaling laws to data complexity, we need to compute the law for each dataset and examine its fitted parameters.

### 4.1 Computing Data-sensitive Scaling Laws from gzip -compressibility

The scaling law functional form proposed by Hoffmann et al. [2022] predicts training loss as a function of model & dataset size:

L ⁡ ( N , D ) = E + A N α + B D β L(N,D)=E+\dfrac{A}{N^{\alpha}}+\dfrac{B}{D^{\beta}} (1)

where N N is the model’s parameter count and D D is the training dataset’s token count. They claim that E E captures the “entropy of natural text” (their Sec. 3.3) and that scaling laws are “independent of dataset” (their App. C). However, when we fit this function on the training results for each of our PCFG datasets (leveraging the helpful open-source implementation of Muennighoff et al. [2023] ), we find considerably different laws for each dataset (Tab. 2 ).

The scaling law induces a compute-optimal frontier for parameter count derived by Kaplan et al. [2020] & Hoffmann et al. [2022] and simplifiable as:

N o ​ p ​ t ​ ( C ) = ( α ​ A β ​ B ​ ( C 6 ) β ) 1 α + β N_{opt}(C)=\left(\dfrac{\alpha A}{\beta B}\left(\dfrac{C}{6}\right)^{\beta}\right)^{\dfrac{1}{\alpha+\beta}} (2)

where C C is a compute budget in FLOPs. We plot this compute-optimal frontier for Chinchilla as well as our fitted law for each PCFG dataset in Fig. 3 . From a cursory glance, we can see that the frontier of our fitted law progressively becomes more data-preferent as data becomes harder to compress, crossing over Chinchilla’s 1-to-1 frontier at some point 0.23 < gzip -compressibility < 0.45 0.23<\texttt{gzip}\text{-compressibility}<0.45 .

In order to predict scaling law parameters from a dataset’s compressibility, let us fit a simple linear regression on the fitted scaling law parameters for each dataset. Recall from Sec. 3.1 that we compute the compressibility H H of a dataset 𝑫 \boldsymbol{D} by taking the average ratio of compressed bits to original bits for each element d d :

H ⁡ ( 𝑫 ) = 1 ‖ 𝑫 ‖ ​ ∑ d ∈ 𝑫 ‖ gzip ​ ( d ) ‖ ‖ d ‖ H(\boldsymbol{D})=\dfrac{1}{||\boldsymbol{D}||}\sum_{d\in\boldsymbol{D}}\dfrac{||\texttt{gzip}(d)||}{||d||} (3)

So once we’ve fit lines to predict each parameter (E, A, B, α \alpha , β \beta ) from H H , we can re-define each parameter as a function of compressibility:

∀ x ∈ { E , A , B , α , β } : x ⁡ ( H ) = m x ​ H + n x \forall x\in\{E,A,B,\alpha,\beta\}:x(H)=m_{x}H+n_{x} (4)

where m x m_{x} and n x n_{x} are just our fitted linear regressions’ parameters. These fitted values (along with the regressions’ p p -values) are presented in Tab. 3 and the linear regressions are visualized in Fig. 4 . They’re all pretty much monotonically decreasing at different rates with an interesting α \alpha - β \beta intercept at H ≈ 0.27 H\approx 0.27 . It’s also interesting to note that E E , originally set as the constant ‘entropy of natural language’, is the only parameter that loosely increases with H H (though not significantly)—our proxy for complexity or entropy.

Now, we can reparameterize Eq. 1 as a function of compressibility H H :

L ⁡ ( N , D , H ) = E ⁡ ( H ) + A ⁡ ( H ) N α ⁡ ( H ) + B ⁡ ( H ) D β ⁡ ( H ) L(N,D,H)=E(H)+\dfrac{A(H)}{N^{\alpha(H)}}+\dfrac{B(H)}{D^{\beta(H)}} (5)

However, since our experiments are considerably smaller scale and primarily on PCFG data, we also present a form of our data-dependent scaling law as an adjustment of Chinchilla, where ε \varepsilon is the weightage of our adjustment for the gzip -compressibility of the training data (and prime ( ′ ) parameters are the Chinchilla constants).

L ⁡ ( N , D , H ) = ( 1 − ε ) ​ E ′ + ε ​ E ​ ( H ) + ( 1 − ε ) ​ A ′ + ε ​ A ​ ( H ) N ( 1 − ε ) ​ α ′ + ε ​ α ​ ( H ) + ( 1 − ε ) ​ B ′ + ε ​ B ​ ( H ) D ( 1 − ε ) ​ β ′ + ε ​ β ​ ( H ) L(N,D,H)=(1-\varepsilon)E^{\prime}+\varepsilon E(H)+\dfrac{(1-\varepsilon)A^{\prime}+\varepsilon A(H)}{N^{(1-\varepsilon)\alpha^{\prime}+\varepsilon\alpha(H)}}+\dfrac{(1-\varepsilon)B^{\prime}+\varepsilon B(H)}{D^{(1-\varepsilon)\beta^{\prime}+\varepsilon\beta(H)}} (6)

### 4.2 Eliminating Syntactic Parameters as a Confounder of Compressibility

Given just the above experiments, we have not addressed the possibility that our compressibility measure is confounded by some underlying syntactic property (e.g. vocab size). To address this concern, in Fig. 5 we provide results showing that when holding vocab size steady and changing other syntactic properties (Tab. 4 ), gzip -compressibility still predicts scaling law parameter shifts (with an even stronger correlation than in the increasing vocab size setting).

We also empirically show the contrapositive in Fig. 6 , demonstrating that when we widely vary syntactic properties (Tab. 5 ) but such that the datasets’ final gzip -compressibility are all the same, there is no significant shift in scaling law parameters.

Although the intersection behavior observed in Fig. 4 is not observed in the iso-vocab case (Fig. 5 ), the steeper negative slope of α \alpha v.s. β \beta (and A A v.s. B B ) implies the same phenomenon of increased data-preference as gzip -compressibility grows.

Thus we have shown that scaling laws are dependent on training data and gzip -compressibility is a strong predictor of how data complexity will impact scaling properties. We provide fitted coefficients (Tab. 3 ) for predicting scaling parameters as a function of H H ( gzip -compressibility), and offer an adjustment-based formulation (Eq. 6 ) of the data-dependent scaling law to make our small scale synthetic experiments more adaptable to training frontier models.

## 5 Discussion

We have shown that the Chinchilla scaling law [ Hoffmann et al., 2022 ] and similar laws that claim to be data-agnostic are in fact web-text-specific instances of a broader family of scaling laws sensitive to information-theoretic measures of training data. Not only do datasets that are difficult to compress (regardless of syntactic specifics) require more compute, they also require a different trade-off between model size & data.

Why does a dataset with a certain level of compressibility H H result in the specific scaling parameters that it does? And why does increased gzip -compressibility result in increased preference for data over parameter count? These questions warrant further exploration from a theoretical perspective—we hope to leverage connections between syntax & information theory to answer this question in future work.

On the empirical side, an especially promising avenue is in LM’s for code since code datasets have significantly lower gzip -compressibility than natural language. Therefore, we can expect the compute-optimal scaling law for code to have stronger parameter-preference than Chinchilla. We are currently running experiments at 1.92e19 FLOPs (some gzip -compressibility analysis in Fig. 8 and preliminary runs in Fig. 9 ) to compare performance based on Chinchilla’s allocation and our data-adjusted scaling law’s (Eq. 6 ) allocation. As highlighted in Sec. 1 , scaling up this finding could save $278,000 in H100 hours when training a single relatively small (6B parameter) code-generation model.

Beyond a deeper theoretical understanding of scaling laws & more optimal compute allocation for code-generation LMs, our findings also open possibilities for using compressibility as a metric in training data filtering, curriculum learning ordering, and fine-tuning data requirement estimation. Anecdotally, we have heard from researchers at frontier AI labs that compression algorithms are already used in production for filtering LLM training data.

The call-to-action here is not per se to use our data-dependent scaling law to decide how to spend your next million dollars of compute, but rather to begin investigating whether performance discrepancies between models trained on different datasets are explainable by simple information-theoretic measures (e.g. gzip -compressibility) of training data. If so (as experienced by Bi et al. [2024] ), it may be worth building systems to dynamically determine compute allocation for each training dataset, with the general rule of thumb that easy-to-compress datasets prefer parameters and hard-to-compress datasets prefer data.

## 6 Limitations

The work presented here is restricted to the synthetic PCFG setting and does not yet explicitly show generalization to predicting different scaling properties of real-world datasets. Our method of modulating training data complexity by varying syntactic properties of a PCFG, though naturalistic, is fairly specific and may still be prone to confounders. In addition, there are features of training data that affect scaling but appear to not be modeled well by gzip -compressibility. Alternative compression algorithms & information-theoretic measures of training data were not tested though they likely all broadly correlate with gzip -compressibility.

## 7 Acknowledgements

We are grateful to Alon Albalak, Rylan Schaeffer, Charlie Snell, Ethan Caballero, Martin Ziqiao Ma, Sankeerth Rao Karingula, Guillaume Lample, Vibhu Sapra, Aryaman Arora, Tristan Thrush, and several anonymous Twitter users for their thorough reviews & feedback on drafts of this paper.

This work was also sponsored by generous compute grants from Luke Piette (RunPod), Kye Gomez (Swarms), Vincent Weisser & Johannes Hagemann (Prime Intellect), and of course the rest of my team at Reworkd—Asim Shrestha & Adam Watkins.

## References

Aghajanyan et al. [2023] Armen Aghajanyan, Lili Yu, Alexis Conneau, Wei-Ning Hsu, Karen Hambardzumyan, Susan Zhang, Stephen Roller, Naman Goyal, Omer Levy, and Luke Zettlemoyer. Scaling laws for generative mixed-modal language models. In International Conference on Machine Learning , pages 265–279. PMLR, 2023.

Arora et al. [2022] Aryaman Arora, Clara Meister, and Ryan Cotterell. Estimating the entropy of linguistic distributions. In Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers) , pages 175–195, 2022.

Bi et al. [2024] Xiao Bi, Deli Chen, Guanting Chen, Shanhuang Chen, Damai Dai, Chengqi Deng, Honghui Ding, Kai Dong, Qiushi Du, Zhe Fu, et al. Deepseek llm: Scaling open-source language models with longtermism. arXiv preprint arXiv:2401.02954 , 2024.

Bird and Loper [2004] Steven Bird and Edward Loper. NLTK: The natural language toolkit. In Proceedings of the ACL Interactive Poster and Demonstration Sessions , pages 214–217, Barcelona, Spain, July 2004. Association for Computational Linguistics. URL https://aclanthology.org/P04-3031 .

Breydo [2021] Thomas Breydo. thomasbreydo/pcfg . 8 2021. URL https://github.com/thomasbreydo/pcfg .

Caballero et al. [2023] Ethan Caballero, Kshitij Gupta, Irina Rish, and David Krueger. Broken neural scaling laws. In ICLR 2023 Workshop on Mathematical and Empirical Understanding of Foundation Models , 2023.

Cherry et al. [1953] E Colin Cherry, Morris Halle, and Roman Jakobson. Toward the logical description of languages in their phonemic aspect. Language , pages 34–46, 1953.

Chi [1999] Zhiyi Chi. Statistical properties of probabilistic context-free grammars. Computational Linguistics , 25(1):131–160, 1999. URL https://aclanthology.org/J99-1004 .

Chomsky [1956] Noam Chomsky. Three models for the description of language. IRE Transactions on information theory , 2(3):113–124, 1956.

Corazza and Satta [2007] Anna Corazza and Giorgio Satta. Probabilistic context-free grammars estimated from infinite distributions. IEEE transactions on pattern analysis and machine intelligence , 29(8):1379–1393, 2007.

Cortes et al. [1993] Corinna Cortes, Lawrence D Jackel, Sara Solla, Vladimir Vapnik, and John Denker. Learning curves: Asymptotic values and rate of convergence. Advances in neural information processing systems , 6, 1993.

Cotterell et al. [2018] Ryan Cotterell, Sabrina J. Mielke, Jason Eisner, and Brian Roark. Are all languages equally hard to language-model? In Marilyn Walker, Heng Ji, and Amanda Stent, editors, Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 2 (Short Papers) , pages 536–541, New Orleans, Louisiana, June 2018. Association for Computational Linguistics. doi: 10.18653/v1/N18-2085 . URL https://aclanthology.org/N18-2085 .

Delétang et al. [2023] Grégoire Delétang, Anian Ruoss, Paul-Ambroise Duquenne, Elliot Catt, Tim Genewein, Christopher Mattern, Jordi Grau-Moya, Li Kevin Wenliang, Matthew Aitchison, Laurent Orseau, et al. Language modeling is compression. arXiv preprint arXiv:2309.10668 , 2023.

Deutsch [1996] Peter Deutsch. Deflate compressed data format specification version 1.3. Technical report, 1996.

Gailly and Adler [1992] Jean-loup Gailly and Mark Adler. Gnu gzip. GNU Operating System , 1992.

Grenander [1967] Ulf Grenander. Syntax-controlled probabilities . Division of Applied Mathematics, Brown University, 1967.

Gunasekar et al. [2023] Suriya Gunasekar, Yi Zhang, Jyoti Aneja, Caio César Teodoro Mendes, Allie Del Giorno, Sivakanth Gopi, Mojan Javaheripi, Piero Kauffmann, Gustavo de Rosa, Olli Saarikivi, et al. Textbooks are all you need. arXiv preprint arXiv:2306.11644 , 2023.

Harris [1991] Zellig Harris. A theory of language and information: a mathematical approach . Oxford University Press, 1991.

Hestness et al. [2017] Joel Hestness, Sharan Narang, Newsha Ardalani, Gregory Diamos, Heewoo Jun, Hassan Kianinejad, Md Mostofa Ali Patwary, Yang Yang, and Yanqi Zhou. Deep learning scaling is predictable, empirically. arXiv preprint arXiv:1712.00409 , 2017.

Hoffmann et al. [2022] Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, et al. Training compute-optimal large language models. arXiv preprint arXiv:2203.15556 , 2022.

Huang et al. [2024] Yuzhen Huang, Jinghan Zhang, Zifei Shan, and Junxian He. Compression represents intelligence linearly. arXiv preprint arXiv:2404.09937 , 2024.

Huffman [1952] David A Huffman. A method for the construction of minimum-redundancy codes. Proceedings of the IRE , 40(9):1098–1101, 1952.

Jiang et al. [2023] Zhiying Jiang, Matthew Yang, Mikhail Tsirlin, Raphael Tang, Yiqin Dai, and Jimmy Lin. “low-resource” text classification: A parameter-free classification method with compressors. In Anna Rogers, Jordan Boyd-Graber, and Naoaki Okazaki, editors, Findings of the Association for Computational Linguistics: ACL 2023 , pages 6810–6828, Toronto, Canada, July 2023. Association for Computational Linguistics. doi: 10.18653/v1/2023.findings-acl.426 . URL https://aclanthology.org/2023.findings-acl.426 .

Jones [2021] Andy L Jones. Scaling scaling laws with board games. arXiv preprint arXiv:2104.03113 , 2021.

Kallini et al. [2024] Julie Kallini, Isabel Papadimitriou, Richard Futrell, Kyle Mahowald, and Christopher Potts. Mission: Impossible language models. arXiv preprint arXiv:2401.06416 , 2024.

Kaplan et al. [2020] Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, and Dario Amodei. Scaling laws for neural language models. arXiv preprint arXiv:2001.08361 , 2020.

Li et al. [2023] Raymond Li, Loubna Ben Allal, Yangtian Zi, Niklas Muennighoff, Denis Kocetkov, Chenghao Mou, Marc Marone, Christopher Akiki, Jia Li, Jenny Chim, et al. Starcoder: may the source be with you! arXiv preprint arXiv:2305.06161 , 2023.

Liu and Tegmark [2023] Ziming Liu and Max Tegmark. A neural scaling law from lottery ticket ensembling. arXiv preprint arXiv:2310.02258 , 2023.

Loshchilov and Hutter [2016] Ilya Loshchilov and Frank Hutter. Sgdr: Stochastic gradient descent with warm restarts. arXiv preprint arXiv:1608.03983 , 2016.

Loshchilov and Hutter [2017] Ilya Loshchilov and Frank Hutter. Decoupled weight decay regularization. arXiv preprint arXiv:1711.05101 , 2017.

Muennighoff et al. [2023] Niklas Muennighoff, Alexander Rush, Boaz Barak, Teven Le Scao, Nouamane Tazi, Aleksandra Piktus, Sampo Pyysalo, Thomas Wolf, and Colin A Raffel. Scaling data-constrained language models. Advances in Neural Information Processing Systems , 36, 2023.

Paszke et al. [2019] Adam Paszke, Sam Gross, Francisco Massa, Adam Lerer, James Bradbury, Gregory Chanan, Trevor Killeen, Zeming Lin, Natalia Gimelshein, Luca Antiga, et al. Pytorch: An imperative style, high-performance deep learning library. Advances in neural information processing systems , 32, 2019.

Penedo et al. [2023] Guilherme Penedo, Quentin Malartic, Daniel Hesslow, Ruxandra Cojocaru, Alessandro Cappelli, Hamza Alobeidli, Baptiste Pannier, Ebtesam Almazrouei, and Julien Launay. The refinedweb dataset for falcon llm: outperforming curated corpora with web data, and web data only. arXiv preprint arXiv:2306.01116 , 2023.

Penedo et al. [2024] Guilherme Penedo, Hynek Kydlíček, Leandro von Werra, and Thomas Wolf. Fineweb, 2024. URL https://huggingface.co/datasets/HuggingFaceFW/fineweb .

Piantadosi et al. [2011] Steven T Piantadosi, Harry Tily, and Edward Gibson. Word lengths are optimized for efficient communication. Proceedings of the National Academy of Sciences , 108(9):3526–3529, 2011.

Rae et al. [2021] Jack W Rae, Sebastian Borgeaud, Trevor Cai, Katie Millican, Jordan Hoffmann, Francis Song, John Aslanides, Sarah Henderson, Roman Ring, Susannah Young, et al. Scaling language models: Methods, analysis & insights from training gopher. arXiv preprint arXiv:2112.11446 , 2021.

Rosenfeld et al. [2019] Jonathan S Rosenfeld, Amir Rosenfeld, Yonatan Belinkov, and Nir Shavit. A constructive prediction of the generalization error across scales. arXiv preprint arXiv:1909.12673 , 2019.

Sánchez et al. [2018] Joan Andreu Sánchez, Martha Alicia Rocha, Verónica Romero, and Mauricio Villegas. On the derivational entropy of left-to-right probabilistic finite-state automata and hidden Markov models. Computational Linguistics , 44(1):17–37, April 2018. doi: 10.1162/COLI_a_00306 . URL https://aclanthology.org/J18-1002 .

Shannon [1951] Claude E Shannon. Prediction and entropy of printed english. Bell system technical journal , 30(1):50–64, 1951.

Shannon [1948] Claude Elwood Shannon. A mathematical theory of communication. The Bell system technical journal , 27(3):379–423, 1948.

Sorscher et al. [2022] Ben Sorscher, Robert Geirhos, Shashank Shekhar, Surya Ganguli, and Ari Morcos. Beyond neural scaling laws: beating power law scaling via data pruning. Advances in Neural Information Processing Systems , 35:19523–19536, 2022.

Xie et al. [2024] Sang Michael Xie, Hieu Pham, Xuanyi Dong, Nan Du, Hanxiao Liu, Yifeng Lu, Percy S Liang, Quoc V Le, Tengyu Ma, and Adams Wei Yu. Doremi: Optimizing data mixtures speeds up language model pretraining. Advances in Neural Information Processing Systems , 36, 2024.

Zhao et al. [2023] Yanli Zhao, Andrew Gu, Rohan Varma, Liang Luo, Chien-Chin Huang, Min Xu, Less Wright, Hamid Shojanazeri, Myle Ott, Sam Shleifer, et al. Pytorch fsdp: experiences on scaling fully sharded data parallel. arXiv preprint arXiv:2304.11277 , 2023.

Ziv and Lempel [1977] Jacob Ziv and Abraham Lempel. A universal algorithm for sequential data compression. IEEE Transactions on information theory , 23(3):337–343, 1977.

## Appendix A Appendix

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
