##### Report GitHub Issue

Content selection saved. Describe the issue below:

# AI-rithmetic Thanks: Authors are listed in alphabetical order. Correspondence to {alexbie, tdick, kulesza, pragh, vinodraman, sergeiv}@google.com .

###### Abstract

Modern AI systems have been successfully deployed to win medals at international math competitions, assist with research workflows, and prove novel technical lemmas. However, despite their progress at advanced levels of mathematics, they remain stubbornly bad at basic arithmetic, consistently failing on the simple task of adding two numbers. We present a systematic investigation of this phenomenon. We demonstrate empirically that all frontier models suffer significantly degraded accuracy for integer addition as the number of digits increases. Furthermore, we show that most errors made by these models are highly interpretable and can be attributed to either operand misalignment or a failure to correctly carry; these two error classes explain 87.9%, 62.9%, and 92.4% of Claude Opus 4.1, GPT-5, and Gemini 2.5 Pro errors, respectively. Finally, we show that misalignment errors are frequently related to tokenization, and that carrying errors appear largely as independent random failures.

## 1 Introduction

Dramatic improvements in AI systems have led to surprising new applications in many areas, including advanced mathematics. While computer-assisted proofs have been around since the 4-color theorem of Appel and Haken (1976) , there has been an explosion of progress in the recent years. Large language models from Google and OpenAI have won medals in international competitions, developing proofs to new problems in algebra, geometry, and analysis ( Luong and Lockhart, 2025 ; Wei, 2025 ) . They have been used in research mathematics to find new lemmas, or improve existing proofs ( Gans, 2025 ; Novikov et al., 2025 ; Nagda et al., 2025 ; Georgiev et al., 2025 ) . And mathematicians of all levels of experience, from graduate students to Fields medals winners, are using them to solve open problems and advance the state of the art ( Fountoulakis, 2025 ; Sellke and Yin, 2025 ) .

At the same time, it is widely known (and we confirm here) that these systems are remarkably unreliable at basic arithmetic, sometimes failing to correctly add even two- or three-digit numbers. Similar failures such as an inability to count the number of ‘r’s in “strawberry” or solve simple equations ( shaun.ralston, 2025 ) have also been observed. Of course, this is not inherently contradictory: arithmetic is different from advanced mathematics in many ways. But for humans, these skills are both clearly related and strongly ordered, arithmetic being a simple but critical part of the foundation on which deeper mathematics is built. Therefore, it may seem surprising that AI systems can outperform experts at more “advanced” tasks but fail to keep pace with kindergartners in the “simple” ones.

Accepting that AI systems do not exhibit human-like patterns of performance, we might instead re-imagine them as algorithmic machines performing complex behaviors by composing simple ones (as in, for example, long addition). Indeed, this is the idea behind the current wave of reasoning models trained to perform a series of intermediate operations to reach a final answer. But this compositional view also fails to describe arithmetic performance, which we find is not even monotonic: AI systems are sometimes better at adding longer numbers than shorter ones. Moreover, while bigger models generally perform better than smaller models, all current models make significant numbers of mistakes as the problem size grows, suggesting that scaling alone is not likely to solve the problem, even though only a finite number of simple behaviors need to be learned and orchestrated by the reasoner.

Arithmetic, then, is an interesting case study in how modern AI systems can confound intuitions. In this work, we systematically investigate model behavior on simple integer addition problems, characterizing mistakes and identifying patterns. We find that errors are generally explainable in intuitive terms, offering a view of AI systems that is neither strictly human-like nor purely compositional, but idiosyncratic and dependent on design choices such as tokenization and auto-regression.

While tool use or task-focused training can probably be used to address the specific arithmetic difficulties we discuss here, the larger point is that today’s models still have considerable weaknesses that we cannot fully anticipate. Manually correcting individual deficiencies as they are discovered does not seem like a viable path toward reliable general-purpose systems (if that is the goal). Instead, our aim is to use arithmetic as a convenient probe to understand some of today’s AI failures, and hopefully begin to illuminate larger problems that have yet to be solved.

### 1.1 Summary of Findings

We conduct systematic experiments on a collection of frontier large language models, finding that: • When adding two numbers, all frontier models perform poorly as the length of the numbers increases (Figure 1 ). We also find that performance is not necessarily monotone in length.

• Most observed mistakes are due either to misalignment or close carry errors (Figure 2 ). Misalignment errors are when one of the input operands is incorrectly shifted. Close carry errors are when the model incorrectly carries or fails to carry in borderline cases (that is, where the sum of digits is 9 but the model still carries a 1, or the sum is 10 and the model fails to carry). Misalignment and close carry errors comprise 87.9%, 62.9%, and 92.4% of Claude Opus 4.1, GPT-5, and Gemini 2.5 Pro errors, respectively.

• Further investigation into error classes reveals that: – Misalignment errors are often periodic with respect to argument length, a fact that may be explained by tokenization, especially for models that use multi-digit tokens (Section 4.1 ).

– The occurrence of close carry errors is largely consistent with an independent error model where models err on each close carry independently with probability p p (Section 4.2 ). If an addition problem contains n n close carries, this predicts a ( 1 − p ) n (1-p)^{n} chance of getting the problem correct (i.e., the LeCun (2023) model), and a geometrically distributed first error position.

### 1.2 Related Work

Although language models can perform arithmetic tasks with non-trivial accuracy in certain settings ( Zoph et al., 2022 ; Yang et al., 2023 ; Maltoni and Ferrara, 2024 ) , their failure to generalize and overall poor performance have been widely observed ( Saxton et al., 2019 ; Nogueira et al., 2021 ; Dziri et al., 2023 ; Qian et al., 2023 ; Gambardella et al., 2024 ; Testolin, 2024 ; Yan et al., 2025 ; Loeber, 2024 ) .

Recent work has focused on understanding how AI systems represent numbers or implement arithmetic operations ( Stolfo et al., 2023 ; Dziri et al., 2023 ; Nikankin et al., 2025 ; Deng et al., 2024 ; Zhang et al., 2024 ; Baeumel et al., 2025b ; Levy and Geva, 2025 ; Kantamneni and Tegmark, 2025 ) , as well as how they can be improved. Techniques include prompting or training with chain-of-thought ( Wei et al., 2022 ; Lee et al., 2023 ) , augmenting the model’s abilities with symbolic systems ( Yang et al., 2024 ; Dugan et al., 2024 ) , adding hints or restructuring the problem ( Nogueira et al., 2021 ; Zhou et al., 2023 ) , increasing numerical precision ( Feng et al., 2024 ) , and utilizing improved positional encodings ( Shen et al., 2023 ; McLeish et al., 2024 ; Zhou et al., 2024 ) .

In terms of error analysis, Singh and Strouse (2024) find that enforcing right-to-left tokenization with separators improves accuracy for GPT-4 (which employs multi-digit tokenization), and that errors are highly position-dependent rather than problem difficulty-dependent. In this vein, our analysis uncovers that accuracy is periodic with respect to length (Figure 6 ) for GPT models; furthermore we identify that these tokenization-induced errors are due to misalignment. Baeumel et al. (2025a) analyze close carry errors, attributing them to the inability of models to anticipate cascading carries. They conduct an in-depth analysis on multi-operand, 3-digit addition on smaller models, while we examine two-operand, n n -digit addition and frontier reasoning models. Our focus on operand length leads us to uncover the independent nature of close carry errors. Nikankin et al. (2025) use tools from mechanistic interpretability to identify the exact circuits that pretrained LLMs use to add, observing that an arithmetic problem activates several independent (flawed) mechanisms that contribute to promoting the correct answer. Nikankin et al. (2025) primarily study Llama models, and restrict their focus to answers computed in a single forward pass (e.g. input operands and the output answer are a single 3-digit token).

## 2 Model Performance

In this section, we investigate the performance of frontier LLMs on adding two numbers.

#### Setup.

We use prompts of the form: What is A A + B B ? Write just the answer.

For each length d ∈ { 1 , … , 100 } d\in\{1,\ldots,100\} , we generate 100 prompts by setting A A and B B to be d d -digit numbers chosen independently and uniformly at random from { 10 d − 1 , … , 10 d − 1 } \{10^{d-1},\ldots,10^{d}-1\} . We send each prompt to each model and collect their responses.

To extract an answer from the model’s response, we remove all commas (to account for different numerical formatting conventions) and then extract the span of digits with the lowest edit distance to the correct sum A + B A+B . We say that the model is correct if the match is exact, and incorrect otherwise. This test is lenient: if the model response includes multiple spans of digits, we consider the response correct if any of them is correct. Table 1 gives examples of several correct and incorrect model responses when the true sum is 1234 .

#### Models.

We test a variety of frontier LLMs, including Claude Opus 4.1, GPT-4o, GPT-5, Gemini 2.5 Flash, Gemini 2.5 Pro, Gemini 2.5 Pro with Code Execution, and Gemma 3 27B. All models tested have been consumer facing at some point in their life cycle.

#### Results.

Figure 1 shows the fraction of correct responses a function of the length d d . With the exception of Gemini 2.5 Pro Code Execution, the accuracy of all models drops significantly below 100% as the number of digits increases. Even at a moderate length of 20, most models exhibit a nontrivial error rate. This suggests that the varieties of architectures, data mixtures, and training practices used by current models are not sufficient for learning to accurately perform basic addition.

Gemini 2.5 Pro with Code Execution’s stronger performance can be attributed to the fact that it usually calculates the sum using short python scripts. Nonetheless, we still observe errors. These occur when the model fails to use the tool or fails to correctly copy the answer calculated by the tool.

## 3 Exploration of Mistakes

Next, we explore the types of mistakes evident in Figure 1 . We find that a significant fraction of mistakes can be explained intuitively.

Recall that when adding a pair of numbers, the canonical long addition algorithm aligns the operands vertically and then computes a sequence of digit sums, one for each column, proceeding from least to most significant position. When a column sum exceeds 9, a one is “carried” to the next (more significant) column.

A large proportion of model mistakes are consistent with one of two natural failure modes during the execution of this algorithm: (1) misalignment, where the digits of one operand are shifted by a few positions in either direction, and (2) close carry failure, where a carry is performed in error when the column sum is 9, or not performed when the column sum is 10. (See below for the details of how we identify such errors.)

Table 2 shows the proportion of all incorrect answers given by each model that are consistent with one of these two error types. Notably, these two types cover 92.4% of Gemini 2.5 Pro’s mistakes, 87.9% of Claude Opus 4.1’s mistakes, and at least 55.6% of every model’s mistakes.

#### Misalignment Errors.

We say that a model’s extracted answer for the sum of A A and B B contains a misalignment error if at least the first 6 digits of the extracted answer match the sum when adding A A and B B with the arguments offset by up to 10 digits in either direction. We limit the test to six digits because models tend to compound their errors as they go, making long misaligned matches unlikely. We require at least six digits to avoid false detections.

More specifically, for each offset s ∈ { − 10 , … , − 1 , 1 , … , 10 } s\in\{-10,\ldots,-1,1,\ldots,10\} , we calculate offsetsum ⁡ ( A , B , s ) = A ⋅ 10 max ⁡ ( 0 , s ) + B ⋅ 10 max ⁡ ( 0 , − s ) \operatorname{offsetsum}(A,B,s)=A\cdot 10^{\max(0,s)}+B\cdot 10^{\max(0,-s)} and calculate the length of the shared prefix between the extracted model answer and offsetsum ⁡ ( A , B , s ) \operatorname{offsetsum}(A,B,s) . We identify the response as a misalignment error if the length is at least 6 and the extracted answer is not equal to one of the arguments. 2 2 2 When the model outputs A A or B B , we do not consider this to be a misalignment error, even though offsetsum ⁡ ( A , B , s ) \operatorname{offsetsum}(A,B,s) typically begins with | s | |s| digits from A A or B B . Note that matching 6 digits for an offset of size at most 10 is unlikely by chance: there are at most 20 distinct 6-digit prefixes obtained from the offset sums, yet approximately 10 6 10^{6} possible prefixes, so the probability of a uniformly drawn answer matching a six-digit prefix is ≈ 0.002 % \approx 0.002\% .

Table 3 shows examples of the prefixes that qualify as misalignment errors for A = 555555 A=555555 and B = 123456 B=123456 .

#### Close Carry Errors.

We use the following procedure to identify close carry errors. If the correct sum and the extracted model answer are different lengths, we pad the shorter to the left with zeros. Then we compare the extracted answer to the correct answer digit by digit from left to right—although long addition is performed from right to left, LLMs generate tokens autoregressively in the order they appear. When we reach the first digit at which an error occurs, we check if it is consistent with a close carry error: • If the digit is too large by 1 and the column to the right has a correct column sum of 9, then we say it is a close carry error.

• If the digit is too small by 1 and the column to the right has a correct column sum of 10, then it is also a close carry error.

If the response contains no errors, or the first error does not satisfy either case above, then we do not identify it as a close carry error. Table 4 show some examples of the errors that would be considered close carries for small addition problems.

#### Runaway errors.

In addition to misalignment and close carry errors, we observed that some of the models frequently output answers that are much longer than the correct answer (sometimes thousands of digits long). We say that an extracted answer is a runaway error if its length is at least 50% longer than the true answer.

#### Results.

Figure 2 shows how the mistakes made by each model break down into aforementioned mistake types. Since the error types we consider are not mutually exclusive, we classify a model’s response according to the first mistake type it matches in the following order: runaway, misalignment, close carry. 3 3 3 The overlap between error types is low, and the order here does not have a large impact on the results. Among all models, we observe 8081 responses that are only identified as misalignment errors, 9347 that are only identified as close carries, and 543 that are identified as both.

Any mistakes that do not match the conditions for these three error types are classified as “other”. For Claude Opus 4.1, Gemini 2.5 Pro, GPT-4o, and GPT-5, the majority of their mistakes match at least one of the three mistake types. Most of the mistakes made by Claude Opus 4.1 are close carrying errors, while most of the mistakes made by Gemini 2.5 Pro and GPT-5 are misalignment errors.

Figure 3 shows histograms of the edit distance between the extracted model answer and the true answer for mistakes on problems of length 40 to 80. Each histogram bar is colored according to the types of the mistakes. Most models exhibit a bimodal distribution with a significant fraction of the low edit distance mistakes classified as close carry errors and many of the longer edit distance mistakes classified as misalignment errors. This is intuitive since close carry errors are local in nature, while a single misalignment can distort the entire result.

Figure 4 shows that close carry errors are significantly more prevalent than other carrying errors. The heat maps show the frequency of the model’s leftmost error delta (the difference between model’s digit and answer’s digit) and the column sum in the next position. Close carry errors are characterized by having a delta of -1 and next column sum of 10, or a delta of +1 and a next column sum of 9. We see that these combinations are much more frequent than any other combination, although each model has its own unique behaviors as well.

Finally, for misalignment errors, Figure 5 shows histograms of the offsets producing the longest prefix match. Recall that positive offsets correspond to padding the first argument on the right with 0s. With the exception of GPT-5, the models all nearly always have a positive offset. A possible explanation is that it is common practice to write the longer argument first when adding numbers of different lengths. We see that Gemini 2.5 Flash and Pro, and Gemma 3 27B all typically misalign the arguments by a single digit position. On the other hand, GPT-4o and Claude Opus 4.1 favor a 3 3 -digit misalignment. Note that these plots also show some evidence of periodicity in the offset frequencies for some models; we will return to this observation in Section 4.1 .

## 4 Explanation of Mistakes

### 4.1 Tokenization and Misalignment

As observed in Figure 5 , misalignment errors tend to favor certain argument offsets, which vary by model. Here we investigate further and present evidence that misalignment errors may be related to tokenization.

Figure 6 shows the unsmoothed accuracy of GPT-5 (which makes primarily misalignment errors) as a function of the argument length. Particularly for longer arguments, accuracy seems to behave in a periodic way. The right plot splits this curve into three parts, corresponding to lengths that are equivalent to 0, 1, or 2 mod 3. With the shaded regions indicating standard error, it is apparent that the accuracy of GPT-5 is significantly higher for arguments whose length is a multiple of three.

GPT-5 uses the tiktoken tokenizer ( OpenAI, 2025a ; OpenAI, 2025b ) , in which a pre-tokenization regular expression breaks spans of digits into groups of 3 digits, followed by a group containing the remaining 1 or 2 digits if the span length is not a multiple of three. Each of these groups is then represented by a single token. As a consequence, the tokenization of a d d -digit number begins with ⌊ d / 3 ⌋ \lfloor d/3\rfloor tokens that each represent 3-digit strings, followed by a token representing a 1- or 2-digit string if d mod 3 ≠ 0 d\mod 3\neq 0 . Figure 6 therefore suggests that GPT-5 is more likely to make mistakes precisely when 1- or 2-digit tokens are present.

To investigate whether this phenomenon explains misalignment errors more generally, we plot in Figure 7 the discrete Fourier transform of the misalignment error rate as a function of length for all of the models. As expected, we see a large magnitude for the frequency 1 / 3 \nicefrac{{1}}{{3}} for GPT-5, corresponding to the reduced error rate on lengths divisible by 3. In addition, we see pronounced spikes at 1 / 3 \nicefrac{{1}}{{3}} for GPT-4o, which also uses a 3-digit tokenizer ( OpenAI, 2025b ) , and Claude Opus 4.1, for which we find strong evidence of using a similar tokenization scheme. 4 4 4 Specifically, when querying the count_tokens API for claude-opus-4-1-20250805 ( Anthropic, 2025 ) , the increase in returned token count as a function of the number of digits d d is precisely ⌈ d / 3 ⌉ \lceil d/3\rceil , matching GPT-5 and GPT-4o. Meanwhile, we see no spikes at 1 / 3 \nicefrac{{1}}{{3}} for the other models, for which we find strong evidence that they tokenize digits individually. 5 5 5 Gemma 3’s tokenizer tokenizes digits individually ( Google, 2025 ) . For evidence that Gemini 2.5 tokenizes digits individually: Gemma Team (2025) reports using the same tokenizer as Gemini 2; and the count_tokens API for Gemini 2.5 Pro and Flash reports an increase of d d tokens when passed a d d -digit number.

These results suggest that misalignment errors may be exacerbated when operands are encoded with tokens containing variable numbers of digits. However, we also note that models using single-digit tokenizers tended to exhibit more misalignment errors overall, so it may be that longer tokens actually help to reduce misalignment errors, and this effect is muted when mixed-length tokens are used.

### 4.2 Independence and Close Carry Errors

As shown by Figure 3 , close carry errors are “local” in the sense that they tend to produce small overall edit distance between the model output and the correct answer. This suggests that an error made on one close carry may be relatively independent of other mistakes during the computation. Here we propose a simple one-parameter stochastic model of close carry errors, and show that it often matches the observed patterns of mistakes.

Assume a given addition problem involves n n close carries. We imagine that the model proceeds from left to right, producing the correct output digit at each position that does not involve a close carry. Upon reaching a close carry position, the model flips a coin and makes a close carry error with probability p p . If it makes an error, then the answer will be incorrect. If it does not make an error, it proceeds and, on reaching the next close carry position, flips another independent coin with the same bias p p . Continuing in this way, the model will ultimately produce a correct answer with probability ( 1 − p ) n (1-p)^{n} .

To assess whether this stochastic process is representative of the behavior of real models, we first choose a target of n = 15 n=15 close carries and then select only addition problems with exactly n n close carries. (In general, approximately 20% of columns produce a close carry, so the selected problems have a typical length of d = 75 d=75 .) For each model, we set p p so that the predicted error matches the observed error rate on these problems, including only problems for which the model either made a close carry error or was correct. We then examine, for each selected problem, the number of successful close carries before the first carry error, comparing the distribution observed empirically with the one predicted by the stochastic model. As shown in Figure 8 , the two distributions are often closely (though not perfectly) aligned.

These results are consistent with the idea that some models make close carry errors in a simple, independent way, and do not correlate errors across positions. This is particularly true for Gemma 3 27B. However, not every model’s behavior is fully explained in this way. In particular, several of the models show a lower propensity to make a mistake at the final close carry position, which is consistent with a general increase in accuracy for the lowest-order digits.

## 5 Discussion

Recent work has studied the representational power of neural networks (and transformer architectures in particular) ( Weiss et al., 2021 ; Schnabel et al., 2025 ; Sanford et al., 2024 ) . While the specific modeling choices vary, basic arithmetic generally falls in the class of tasks that can be solved exactly using modern architectures. In fact, addition is one of the examples used to explain how to “think like a transformer” ( Weiss et al., 2021 ) .

However, our evidence suggests that modern LLMs are not finding reliable implementations for addition, instead resorting to error-prone strategies that give poor results and exhibit design-dependent idiosyncrasies. Bigger models tend to perform better, but are dominated by a simple calculator, especially as the number of digits grows beyond 50. If we expect intelligent systems to perform this basic operation without falling back on specialized tools, then we will need new model designs, data sources, and training strategies.

Of course, arithmetic is itself just an example. Success at arithmetic is easy to measure, and we have ready expectations about how an intelligent system ought to perform. But today’s AI systems fail in many unique ways, some of which may be similarly easy to characterize and understand, and others which may be hard to delineate or even see clearly at all. Perhaps LLMs are simply not the right tools for tasks where it is important to identify a single correct answer. Or perhaps even “soft” probabilistic reasoning is too much to expect in complex settings. But we will need a clearer understanding of these boundaries and how to move beyond them if we want to develop robust AI deployments that consistently meet our expectations.

## References

Anthropic (2025) Anthropic Token counting . Note: https://platform.claude.com/docs/en/build-with-claude/token-counting Accessed on Jan. 28, 2026 Cited by: footnote 4 .

Appel and Haken (1976) K. Appel and W. Haken Every planar map is four colorable . Bulletin of the American Mathematical Society 82 ( 5 ), pp. 711 – 712 . Cited by: §1 .

Baeumel et al. (2025a) T. Baeumel, J. V. Genabith, and S. Ostermann The lookahead limitation: why multi-operand addition is hard for LLMs . In Proceedings of the 8th BlackboxNLP Workshop: Analyzing and Interpreting Neural Networks for NLP , Suzhou, China , pp. 250–262 . External Links: Link , Document Cited by: §1.2 .

Baeumel et al. (2025b) T. Baeumel, D. Gurgurov, Y. a. Ghussin, J. van Genabith, and S. Ostermann Modular arithmetic: language models solve math digit by digit . arXiv preprint arXiv:2508.02513 . Cited by: §1.2 .

Deng et al. (2024) C. Deng, Z. Li, R. Xie, R. Chang, and H. Chen Language models are symbolic learners in arithmetic . arXiv preprint arXiv:2410.15580 . Cited by: §1.2 .

Dugan et al. (2024) O. Dugan, D. Jiménez-Benetó, C. Loh, Z. Chen, R. Dangovski, and M. Soljacic OccamLLM: fast and exact language model arithmetic in a single step . Advances in Neural Information Processing Systems 37 , pp. 35665–35699 . Cited by: §1.2 .

Dziri et al. (2023) N. Dziri, X. Lu, M. Sclar, X. L. Li, L. Jiang, B. Y. Lin, S. Welleck, P. West, C. Bhagavatula, R. Le Bras, et al. Faith and fate: limits of transformers on compositionality . Advances in Neural Information Processing Systems 36 , pp. 70293–70332 . Cited by: §1.2 , §1.2 .

Feng et al. (2024) G. Feng, K. Yang, Y. Gu, X. Ai, S. Luo, J. Sun, D. He, Z. Li, and L. Wang How numerical precision affects mathematical reasoning capabilities of llms . arXiv preprint arXiv:2410.13857 . Cited by: §1.2 .

Fountoulakis (2025) K. Fountoulakis GPT-5.2 solves our colt 2022 open problem: “running time complexity of accelerated l1-regularized pagerank” using a standard accelerated gradient algorithm and a complementarity margin assumption. . Note: https://x.com/kfountou/status/2000957773584974298 Cited by: §1 .

Gambardella et al. (2024) A. Gambardella, Y. Iwasawa, and Y. Matsuo Language models do hard arithmetic tasks easily and hardly do easy arithmetic tasks . arXiv preprint arXiv:2406.02356 . Cited by: §1.2 .

Gans (2025) J. S. Gans The efficient market hypothesis when time travel is possible . Economics Letters 248 , pp. 112209 . External Links: ISSN 0165-1765 , Document , Link Cited by: §1 .

Gemma Team (2025) Gemma Team Gemma 3 technical report . External Links: 2503.19786 , Link Cited by: footnote 5 .

Georgiev et al. (2025) B. Georgiev, J. Gómez-Serrano, T. Tao, and A. Z. Wagner Mathematical exploration and discovery at scale . External Links: 2511.02864 , Link Cited by: §1 .

Google (2025) Google Tokenizer . Note: https://gemma-llm.readthedocs.io/en/latest/colab_tokenizer.html Accessed on Jan. 28, 2026 Cited by: footnote 5 .

Kantamneni and Tegmark (2025) S. Kantamneni and M. Tegmark Language models use trigonometry to do addition . arXiv preprint arXiv:2502.00873 . Cited by: §1.2 .

LeCun (2023) Y. LeCun Unpopular opinion about ar-llms . Note: https://x.com/ylecun/status/1640122342570336267 Cited by: 2nd item .

Lee et al. (2023) N. Lee, K. Sreenivasan, J. D. Lee, K. Lee, and D. Papailiopoulos Teaching arithmetic to small transformers . arXiv preprint arXiv:2307.03381 . Cited by: §1.2 .

Levy and Geva (2025) A. A. Levy and M. Geva Language models encode numbers using digit representations in base 10 . In Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 2: Short Papers) , pp. 385–395 . Cited by: §1.2 .

Loeber (2024) J. Loeber External Links: Link Cited by: §1.2 .

Luong and Lockhart (2025) T. Luong and E. Lockhart External Links: Link Cited by: §1 .

Maltoni and Ferrara (2024) D. Maltoni and M. Ferrara Arithmetic with language models: from memorization to computation . Neural Networks 179 , pp. 106550 . Cited by: §1.2 .

McLeish et al. (2024) S. McLeish, A. Bansal, A. Stein, N. Jain, J. Kirchenbauer, B. Bartoldson, B. Kailkhura, A. Bhatele, J. Geiping, A. Schwarzschild, et al. Transformers can do arithmetic with the right embeddings . Advances in Neural Information Processing Systems 37 , pp. 108012–108041 . Cited by: §1.2 .

Nagda et al. (2025) A. Nagda, P. Raghavan, and A. Thakurta Reinforced generation of combinatorial structures: applications to complexity theory . External Links: 2509.18057 , Link Cited by: §1 .

Nikankin et al. (2025) Y. Nikankin, A. Reusch, A. Mueller, and Y. Belinkov Arithmetic without algorithms: language models solve math with a bag of heuristics . In The Thirteenth International Conference on Learning Representations , External Links: Link Cited by: §1.2 , §1.2 .

Nogueira et al. (2021) R. Nogueira, Z. Jiang, and J. Lin Investigating the limitations of transformers with simple arithmetic tasks . arXiv preprint arXiv:2102.13019 . Cited by: §1.2 , §1.2 .

Novikov et al. (2025) A. Novikov, N. Vũ, M. Eisenberger, E. Dupont, P. Huang, A. Z. Wagner, S. Shirobokov, B. Kozlovskii, F. J. R. Ruiz, A. Mehrabian, M. P. Kumar, A. See, S. Chaudhuri, G. Holland, A. Davies, S. Nowozin, P. Kohli, and M. Balog AlphaEvolve: a coding agent for scientific and algorithmic discovery . External Links: 2506.13131 , Link Cited by: §1 .

OpenAI (2025a) OpenAI Tiktoken . GitHub . Note: https://github.com/openai/tiktoken Release 0.12.0, Accessed on Nov. 3, 2025 Cited by: §4.1 .

OpenAI (2025b) OpenAI Tokenizer . Note: https://platform.openai.com/tokenizer Accessed on Jan. 28, 2026 Cited by: §4.1 , §4.1 .

Qian et al. (2023) J. Qian, H. Wang, Z. Li, S. Li, and X. Yan Limitations of language models in arithmetic and symbolic induction . In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , pp. 9285–9298 . Cited by: §1.2 .

Sanford et al. (2024) C. Sanford, D. Hsu, and M. Telgarsky Transformers, parallel computation, and logarithmic depth . External Links: 2402.09268 , Link Cited by: §5 .

Saxton et al. (2019) D. Saxton, E. Grefenstette, F. Hill, and P. Kohli Analysing mathematical reasoning abilities of neural models . arXiv preprint arXiv:1904.01557 . Cited by: §1.2 .

Schnabel et al. (2025) T. Schnabel, K. Tomlinson, A. Swaminathan, and J. Neville Lost in transmission: when and why llms fail to reason globally . External Links: 2505.08140 , Link Cited by: §5 .

Sellke and Yin (2025) M. Sellke and S. Yin On learning-curve monotonicity for maximum likelihood estimators . External Links: 2512.10220 , Link Cited by: §1 .

shaun.ralston (2025) shaun.ralston External Links: Link Cited by: §1 .

Shen et al. (2023) R. Shen, S. Bubeck, R. Eldan, Y. T. Lee, Y. Li, and Y. Zhang Positional description matters for transformers arithmetic . arXiv preprint arXiv:2311.14737 . Cited by: §1.2 .

Singh and Strouse (2024) A. K. Singh and D. Strouse Tokenization counts: the impact of tokenization on arithmetic in frontier llms . External Links: 2402.14903 , Link Cited by: §1.2 .

Stolfo et al. (2023) A. Stolfo, Y. Belinkov, and M. Sachan A mechanistic interpretation of arithmetic reasoning in language models using causal mediation analysis . arXiv preprint arXiv:2305.15054 . Cited by: §1.2 .

Testolin (2024) A. Testolin Can neural networks do arithmetic? a survey on the elementary numerical skills of state-of-the-art deep learning models . Applied Sciences 14 ( 2 ), pp. 744 . Cited by: §1.2 .

Wei (2025) A. Wei ”1/N I’m excited to share that our latest @OpenAI experimental reasoning LLM has achieved a longstanding grand challenge in AI: gold medal-level performance on the world’s most prestigious math competition—the International Math Olympiad (IMO).” . Note: https://x.com/alexwei_/status/1946477742855532918 Cited by: §1 .

Wei et al. (2022) J. Wei, X. Wang, D. Schuurmans, M. Bosma, F. Xia, E. Chi, Q. V. Le, D. Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models . Advances in neural information processing systems 35 , pp. 24824–24837 . Cited by: §1.2 .

Weiss et al. (2021) G. Weiss, Y. Goldberg, and E. Yahav Thinking like transformers . External Links: 2106.06981 , Link Cited by: §5 .

Yan et al. (2025) Y. Yan, Y. Lu, R. Xu, and Z. Lan Do large language models truly grasp addition? a rule-focused diagnostic using two-integer arithmetic . In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing , pp. 13478–13494 . Cited by: §1.2 .

Yang et al. (2024) X. Yang, B. Chen, and Y. Tam Arithmetic reasoning with llm: prolog generation & permutation . arXiv preprint arXiv:2405.17893 . Cited by: §1.2 .

Yang et al. (2023) Z. Yang, M. Ding, Q. Lv, Z. Jiang, Z. He, Y. Guo, J. Bai, and J. Tang Gpt can solve mathematical problems without a calculator . arXiv preprint arXiv:2309.03241 . Cited by: §1.2 .

Zhang et al. (2024) W. Zhang, C. Wan, Y. Zhang, Y. Cheung, X. Tian, X. Shen, and J. Ye Interpreting and improving large language models in arithmetic calculation . arXiv preprint arXiv:2409.01659 . Cited by: §1.2 .

Zhou et al. (2023) H. Zhou, A. Bradley, E. Littwin, N. Razin, O. Saremi, J. Susskind, S. Bengio, and P. Nakkiran What algorithms can transformers learn? a study in length generalization . arXiv preprint arXiv:2310.16028 . Cited by: §1.2 .

Zhou et al. (2024) Y. Zhou, U. Alon, X. Chen, X. Wang, R. Agarwal, and D. Zhou Transformers can achieve length generalization but not robustly . arXiv preprint arXiv:2402.09371 . Cited by: §1.2 .

Zoph et al. (2022) B. Zoph, C. Raffel, D. Schuurmans, D. Yogatama, D. Zhou, D. Metzler, E. H. Chi, J. Wei, J. Dean, L. B. Fedus, M. P. Bosma, O. Vinyals, P. Liang, S. Borgeaud, T. B. Hashimoto, and Y. Tay Emergent abilities of large language models . TMLR . Cited by: §1.2 .

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
