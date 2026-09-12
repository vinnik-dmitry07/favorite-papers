##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Self-Consistency Improves Chain of Thought Reasoning in Language Models

###### Abstract

Chain-of-thought prompting combined with pre-trained large language models has achieved encouraging results on complex reasoning tasks. In this paper, we propose a new decoding strategy, self-consistency , to replace the naive greedy decoding used in chain-of-thought prompting. It first samples a diverse set of reasoning paths instead of only taking the greedy one, and then selects the most consistent answer by marginalizing out the sampled reasoning paths. Self-consistency leverages the intuition that a complex reasoning problem typically admits multiple different ways of thinking leading to its unique correct answer. Our extensive empirical evaluation shows that self-consistency boosts the performance of chain-of-thought prompting with a striking margin on a range of popular arithmetic and commonsense reasoning benchmarks, including GSM8K (+17.9%), SVAMP (+11.0%), AQuA (+12.2%), StrategyQA (+6.4%) and ARC-challenge (+3.9%).

## 1 Introduction

Although language models have demonstrated remarkable success across a range of NLP tasks, their ability to demonstrate reasoning is often seen as a limitation, which cannot be overcome solely by increasing model scale ( Rae et al., 2021 ; BIG-bench collaboration, 2021 , inter alia ) . In an effort to address this shortcoming, Wei et al. (2022) have proposed chain-of-thought prompting , where a language model is prompted to generate a series of short sentences that mimic the reasoning process a person might employ in solving a task. For example, given the question “If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?” , instead of directly responding with “5” , a language model would be prompted to respond with the entire chain-of-thought: “There are 3 cars in the parking lot already. 2 more arrive. Now there are 3 + 2 = 5 cars. The answer is 5.” . It has been observed that chain-of-thought prompting significantly improves model performance across a variety of multi-step reasoning tasks ( Wei et al., 2022 ) .

In this paper, we introduce a novel decoding strategy called self-consistency to replace the greedy decoding strategy used in chain-of-thought prompting ( Wei et al., 2022 ) , that further improves language models’ reasoning performance by a significant margin. Self-consistency leverages the intuition that complex reasoning tasks typically admit multiple reasoning paths that reach a correct answer ( Stanovich & West, 2000 ) . The more that deliberate thinking and analysis is required for a problem ( Evans, 2010 ) , the greater the diversity of reasoning paths that can recover the answer.

Figure 1 illustrates the self-consistency method with an example. We first prompt the language model with chain-of-thought prompting, then instead of greedily decoding the optimal reasoning path, we propose a “sample-and-marginalize” decoding procedure: we first sample from the language model’s decoder to generate a diverse set of reasoning paths; each reasoning path might lead to a different final answer, so we determine the optimal answer by marginalizing out the sampled reasoning paths to find the most consistent answer in the final answer set. Such an approach is analogous to the human experience that if multiple different ways of thinking lead to the same answer, one has greater confidence that the final answer is correct. Compared to other decoding methods, self-consistency avoids the repetitiveness and local-optimality that plague greedy decoding, while mitigating the stochasticity of a single sampled generation.

Self-consistency is far simpler than prior approaches that either train an additional verifier ( Cobbe et al., 2021 ) or train a re-ranker given additional human annotations to improve generation quality ( Thoppilan et al., 2022 ) . Instead, self-consistency is entirely unsupervised , works off-the-shelf with pre-trained language models, requires no additional human annotation, and avoids any additional training, auxiliary models or fine-tuning. Self-consistency also differs from a typical ensemble approach where multiple models are trained and the outputs from each model are aggregated, it acts more like a “self-ensemble” that works on top of a single language model.

We evaluate self-consistency on a wide range of arithmetic and commonsense reasoning tasks over four language models with varying scales: the public UL2-20B ( Tay et al., 2022 ) and GPT-3-175B ( Brown et al., 2020 ) , and two densely-activated decoder-only language models: LaMDA-137B ( Thoppilan et al., 2022 ) and PaLM-540B ( Chowdhery et al., 2022 ) . On all four language models, self-consistency improves over chain-of-thought prompting by a striking margin across all tasks. In particular, when used with PaLM-540B or GPT-3, self-consistency achieves new state-of-the-art levels of performance across arithmetic reasoning tasks, including GSM8K ( Cobbe et al., 2021 ) (+17.9% absolute accuracy gains), SVAMP ( Patel et al., 2021 ) (+11.0%), AQuA ( Ling et al., 2017 ) (+12.2%), and across commonsense reasoning tasks such as StrategyQA ( Geva et al., 2021 ) (+6.4%) and ARC-challenge ( Clark et al., 2018 ) (+3.9%). In additional experiments, we show self-consistency can robustly boost performance on NLP tasks where adding a chain-of-thought might hurt performance compared to standard prompting ( Ye & Durrett, 2022 ) . We also show self-consistency significantly outperforms sample-and-rank, beam search, ensemble-based approaches, and is robust to sampling strategies and imperfect prompts.

## 2 Self-Consistency over Diverse Reasoning Paths

A salient aspect of humanity is that people think differently. It is natural to suppose that in tasks requiring deliberate thinking, there are likely several ways to attack the problem. We propose that such a process can be simulated in language models via sampling from the language model’s decoder. For instance, as shown in Figure 1 , a model can generate several plausible responses to a math question that all arrive at the same correct answer (Outputs 1 and 3). Since language models are not perfect reasoners, the model might also produce an incorrect reasoning path or make a mistake in one of the reasoning steps (e.g., in Output 2), but such solutions are less likely to arrive at the same answer. That is, we hypothesize that correct reasoning processes, even if they are diverse, tend to have greater agreement in their final answer than incorrect processes.

We leverage this intuition by proposing the following self-consistency method. First, a language model is prompted with a set of manually written chain-of-thought exemplars ( Wei et al., 2022 ) . Next, we sample a set of candidate outputs from the language model’s decoder, generating a diverse set of candidate reasoning paths. Self-consistency is compatible with most existing sampling algorithms, including temperature sampling ( Ackley et al., 1985 ; Ficler & Goldberg, 2017 ) , top- k k sampling ( Fan et al., 2018 ; Holtzman et al., 2018 ; Radford et al., 2019 ) , and nucleus sampling ( Holtzman et al., 2020 ) . Finally, we aggregate the answers by marginalizing out the sampled reasoning paths and choosing the answer that is the most consistent among the generated answers.

In more detail, assume the generated answers 𝐚 i \mathbf{a}_{i} are from a fixed answer set, 𝐚 i ∈ 𝔸 \mathbf{a}_{i}\in\mathbb{A} , where i = 1 , … , m i=1,\ldots,m indexes the m m candidate outputs sampled from the decoder. Given a prompt and a question, self-consistency introduces an additional latent variable 𝐫 i \mathbf{r}_{i} , which is a sequence of tokens representing the reasoning path in the i i -th output, then couples the generation of ( 𝐫 i , 𝐚 i ) (\mathbf{r}_{i},\mathbf{a}_{i}) where 𝐫 i → 𝐚 i \mathbf{r}_{i}\rightarrow\mathbf{a}_{i} , i.e., generating a reasoning path 𝐫 i \mathbf{r}_{i} is optional and only used to reach the final answer 𝐚 i \mathbf{a}_{i} . As an example, consider Output 3 from Figure 1 : the first few sentences “ She eats 3 for breakfast … So she has 9 eggs * $2 = $18. ” constitutes 𝐫 i \mathbf{r}_{i} , while the answer 18 from the last sentence, “ The answer is $18 ”, is parsed as 𝐚 i \mathbf{a}_{i} . 1 1 1 The parser is task dependent. For arithmetic reasoning, we parse the first numerical part as the final answer after the model generates “The answer is ”. For commonsense reasoning, we parse the full string answer as the final answer after the model generates “The answer is ”. Most generated outputs have a consistent format of “{Reasoning paths}. The answer is X.” if we prompt the language model in this format. After sampling multiple ( 𝐫 i , 𝐚 i ) (\mathbf{r}_{i},\mathbf{a}_{i}) from the model’s decoder, self-consistency applies a marginalization over 𝐫 i \mathbf{r}_{i} by taking a majority vote over 𝐚 i \mathbf{a}_{i} , i.e., arg ​ max a ∑ i = 1 m 𝟙 ( 𝐚 i = a ) \argmax_{a}\sum\nolimits_{i=1}^{m}\mathbbm{1}(\mathbf{a}_{i}=a) , or as we defined as the most “consistent” answer among the final answer set.

In Table 1 , we show the test accuracy over a set of reasoning tasks by using different answer aggregation strategies. In addition to majority vote, one can also weight each ( 𝐫 i , 𝐚 i ) (\mathbf{r}_{i},\mathbf{a}_{i}) by P ( 𝐫 i , 𝐚 i ∣ prompt , question ) P(\mathbf{r}_{i},\mathbf{a}_{i}\mid\text{prompt},\text{question}) when aggregating the answers. Note to compute P ( 𝐫 i , 𝐚 i ∣ prompt , question ) P(\mathbf{r}_{i},\mathbf{a}_{i}\mid\text{prompt},\text{question}) , we can either take the unnormalized probability of the model generating ( 𝐫 i , 𝐚 i ) (\mathbf{r}_{i},\mathbf{a}_{i}) given ( prompt , question ) (\text{prompt},\text{question}) , or we can normalize the conditional probability by the output length ( Brown et al., 2020 ) , i.e., P ( 𝐫 i , 𝐚 i ∣ prompt , question ) = exp 1 K ​ ∑ k = 1 K log ⁡ P ⁡ ( t k ∣ prompt , question , t 1 , … , t k − 1 ) , \displaystyle P(\mathbf{r}_{i},\mathbf{a}_{i}\mid\text{prompt},\text{question})=\exp^{\frac{1}{K}\sum_{k=1}^{K}{\log P(t_{k}\mid\text{prompt},\text{question},t_{1},\ldots,t_{k-1})}}, (1) where log ⁡ P ⁡ ( t k ∣ prompt , question , t 1 , … , t k − 1 ) \log P(t_{k}\mid\text{prompt},\text{question},t_{1},\ldots,t_{k-1}) is the log probability of generating the k k -th token t k t_{k} in ( 𝐫 i , 𝐚 i ) (\mathbf{r}_{i},\mathbf{a}_{i}) conditioned on the previous tokens, and K K is the total number of tokens in ( 𝐫 i , 𝐚 i ) (\mathbf{r}_{i},\mathbf{a}_{i}) . In Table 1 , we show that taking the “unweighted sum”, i.e., taking a majority vote directly over 𝐚 i \mathbf{a}_{i} yields a very similar accuracy as aggregating using the “normalized weighted sum”. We took a closer look at the model’s output probabilities and found this is because for each ( 𝐫 i , 𝐚 i ) (\mathbf{r}_{i},\mathbf{a}_{i}) , the normalized conditional probabilities P ( 𝐫 i , 𝐚 i ∣ prompt , question ) P(\mathbf{r}_{i},\mathbf{a}_{i}\mid\text{prompt},\text{question}) are quite close to each other, i.e., the language model regards those generations as ‘‘similarly likely’’. 2 2 2 This also means that the language model is not well calibrated and thus cannot distinguish well between correct solutions and wrong solutions, which also explains why additional re-rankers were trained to better judge the quality of the solutions in previous work ( Cobbe et al., 2021 ; Thoppilan et al., 2022 ) . Additionally, when aggregating the answers, the results in Table 1 show that the “normalized” weighted sum (i.e., Equation 1 ) yields a much higher accuracy compared to its unnormalized counterpart. For completeness, in Table 1 we also report the results by taking a “weighted average”, i.e., each a a gets a score of its weighted sum divided by ∑ i = 1 m 𝟙 ​ ( 𝐚 i = a ) \sum\nolimits_{i=1}^{m}\mathbbm{1}(\mathbf{a}_{i}=a) , which results in a much worse performance.

Self-consistency explores an interesting space between open-ended text generation and optimal text generation with a fixed answer. Reasoning tasks typically have fixed answers, which is why researchers have generally considered greedy decoding approaches ( Radford et al., 2019 ; Wei et al., 2022 ; Chowdhery et al., 2022 ) . However, we have found that even when the desired answer is fixed, introducing diversity in the reasoning processes can be highly beneficial; therefore we leverage sampling, as commonly used for open-ended text generation ( Radford et al., 2019 ; Brown et al., 2020 ; Thoppilan et al., 2022 ) , to achieve this goal. One should note that self-consistency can be applied only to problems where the final answer is from a fixed answer set, but in principle this approach can be extended to open-text generation problems if a good metric of consistency can be defined between multiple generations, e.g., whether two answers agree or contradict each other.

## 3 Experiments

We conducted a series of experiments to compare the proposed self-consistency method with existing approaches on a range of reasoning benchmarks. We find that self-consistency robustly improves reasoning accuracy for every language model considered, spanning a wide range of model scales.

### 3.1 Experiment setup

##### Tasks and datasets.

We evaluate self-consistency on the following reasoning benchmarks. 3 3 3 By default we use the test split for all datasets if the labels are available for evaluation. For CommonsenseQA we use the dev split; for StrategyQA we use the question-only set from BIG-bench collaboration (2021) : https://github.com/google/BIG-bench/tree/main/bigbench/benchmark_tasks/strategyqa . • Arithmetic reasoning . For these tasks, we used the Math Word Problem Repository ( Koncel-Kedziorski et al., 2016 ) , including AddSub ( Hosseini et al., 2014 ) , MultiArith ( Roy & Roth, 2015 ) , and ASDiv ( Miao et al., 2020 ) . We also included AQUA-RAT ( Ling et al., 2017 ) , a recently published benchmark of grade-school-math problems ( Cobbe et al., 2021 , GSM8K;) , and a challenge dataset over math word problems ( Patel et al., 2021 , SVAMP;) .

• Commonsense reasoning . For these tasks, we used CommonsenseQA ( Talmor et al., 2019 ) , StrategyQA ( Geva et al., 2021 ) , and the AI2 Reasoning Challenge (ARC) ( Clark et al., 2018 ) .

• Symbolic Reasoning . We evaluate two symbolic reasoning tasks: last letter concatenation (e.g., the input is “Elon Musk” and the output should be “nk”), and Coinflip (e.g., a coin is heads-up, after a few flips is the coin still heads-up?) from Wei et al. (2022) .

##### Language models and prompts.

We evaluate self-consistency over four transformer-based language models with varying scales: • UL2 ( Tay et al., 2022 ) is an encoder-decoder model trained on a mixture of denoisers with 20-billion parameters. UL2 is completely open-sourced 4 4 4 Model checkpoints at https://github.com/google-research/google-research/tree/master/ul2 . and has similar or better performance than GPT-3 on zero-shot SuperGLUE, with only 20B parameters and thus is more compute-friendly;

• GPT-3 ( Brown et al., 2020 ) with 175-billion parameters. We use two public engines code-davinci-001 and code-davinci-002 from the Codex series ( Chen et al., 2021 ) to aid reproducibility; 5 5 5 Public API available at https://openai.com/api/ .

• LaMDA-137B ( Thoppilan et al., 2022 ) is a dense left-to-right, decoder-only language model with 137-billion parameters, pre-trained on a mixture of web documents, dialog data and Wikipedia;

• PaLM-540B ( Chowdhery et al., 2022 ) is a dense left-to-right, decoder-only language model with 540-billion parameters, pre-trained on a high quality corpus of 780 billion tokens with filtered webpages, books, Wikipedia, news articles, source code, and social media conversations.

We perform all experiments in the few-shot setting, without training or fine-tuning the language models. For a fair comparison we use the same prompts as in Wei et al. (2022) : for all arithmetic reasoning tasks we use the same set of 8 manually written exemplars; for each commonsense reasoning task, 4-7 exemplars are randomly chosen from the training set with manually composed chain-of-thought prompts. 6 6 6 Self-consistency is robust to different sets of prompts and we provide a study in Appendix A.1.2 . Full details on the prompts used are given in Appendix A.3 .

##### Sampling scheme.

To sample diverse reasoning paths, we followed similar settings to those suggested in Radford et al. (2019) ; Holtzman et al. (2020) for open-text generation. In particular, for UL2-20B and LaMDA-137B we applied temperature sampling with T = 0.5 T=0.5 and truncated at the top- k k ( k = 40 k=40 ) tokens with the highest probability, for PaLM-540B we applied T = 0.7 , k = 40 T=0.7,k=40 , and for GPT-3 we use T = 0.7 T=0.7 without top- k k truncation. We provide an ablation study in Section 3.5 to show that self-consistency is generally robust to sampling strategies and parameters.

### 3.2 Main Results

We report the results of self-consistency averaged over 10 runs, where we sampled 40 outputs independently from the decoder in each run. The baseline we compare to is chain-of-thought prompting with greedy decoding ( Wei et al., 2022 ) , referred to as CoT-prompting , which has been previously used for decoding in large language models ( Chowdhery et al., 2022 ) .

##### Arithmetic Reasoning

The results are shown in Table 2 . 7 7 7 The standard deviation of self-consistency is ≤ 0.5 \leq 0.5 for all tasks and is thus omitted in the table. Please refer to Figure 2 , Figure 7 and 8 for the standard deviations under varying numbers of sampled paths. Self-consistency improves the arithmetic reasoning performance over all four language models significantly over chain-of-thought prompting. More surprisingly, the gains become more significant when the language model’s scale increases, e.g., we see +3%-6% absolute accuracy improvement over UL2-20B but +9%-23% for LaMDA-137B and GPT-3. For larger models that already achieve high accuracy on most tasks (e.g., GPT-3 and PaLM-540B), self-consistency still contributes significant additional gains with +12%-18% absolute accuracy on tasks like AQuA and GSM8K, and +7%-11% on SVAMP and ASDiv. With self-consistency, we achieve new state-of-the-art results on almost all tasks: despite the fact that self-consistency is unsupervised and task-agnostic, these results compare favorably to existing approaches that require task-specific training, or fine-tuning with thousands of examples (e.g., on GSM8K).

##### Commonsense and Symbolic Reasoning

Table 3 shows the results on commonsense and symbolic reasoning tasks. Similarly, self-consistency yields large gains across all four language models, and obtained SoTA results on 5 out of 6 tasks. For symbolic reasoning, we test the out-of-distribution (OOD) setting where the input prompt contains examples of 2-letters or 2-flips but we test examples of 4-letters and 4-flips (this setting is more challenging as PaLM-540B or GPT-3 can already achieve perfect in-distribution accuracy). In this challenging OOD setting, the gain of self-consistency is still quite significant compared to CoT-prompting with sufficient model sizes.

To show the effect of the number of sampled reasoning paths, we plot the accuracy (mean and standard deviation over 10 runs) with respect to varying numbers of sampled paths (1, 5, 10, 20, 40) in Figure 2 . The results show that sampling a higher number (e.g., 40) of reasoning paths leads to a consistently better performance, further emphasizing the importance of introducing diversity in the reasoning paths. In Table 4 , we show self-consistency yields a richer set of reasoning paths compared to greedy decoding with a few example questions from two tasks.

### 3.3 Self-Consistency Helps When Chain-of-Thought Hurts Performance

Ye & Durrett (2022) show that sometimes chain-of-thought prompting could hurt performance compared to standard prompting in few-shot in-context learning. Here we perform a study using self-consistency to see if it can help fill in the gap, over a set of common NLP tasks, including (1) Closed-Book Question Answering: BoolQ ( Clark et al., 2019 ) , HotpotQA ( Yang et al., 2018 ) , and (2) Natural Language Inference: e-SNLI ( Camburu et al., 2018 ) , ANLI ( Nie et al., 2020 ) and RTE ( Dagan et al., 2005 ; Bar-Haim et al., 2006 ; Giampiccolo et al., 2007 ; Bentivogli et al., 2009 ) .

The results over PaLM-540B are shown in Table 5 . For some tasks (e.g., ANLI-R1, e-SNLI, RTE), adding chain-of-thought does hurt performance compared to standard prompting ( Brown et al., 2020 ) , but self-consistency is able to robustly boost the performance and outperform standard prompting, making it a reliable way to add rationales in few-shot in-context learning for common NLP tasks.

### 3.4 Compare to other existing approaches

We conduct a set of additional studies and show that self-consistency significantly outperforms existing methods including sample-and-rank, beam search, and ensemble-based approaches.

##### Comparison to Sample-and-Rank

One commonly used approach to improve generation quality is sample-and-rank, where multiple sequences are sampled from the decoder and then ranked according to each sequence’s log probability ( Adiwardana et al., 2020 ) . We compare self-consistency with sample-and-rank on GPT-3 code-davinci-001 , by sampling the same number of sequences from the decoder as self-consistency and taking the final answer from the top-ranked sequence. The results are shown in Figure 3 . While sample-and-rank does improve the accuracy with additionally sampled sequences and ranking, the gain is much smaller compared to self-consistency.

##### Comparison to Beam Search

In Table 6 , we compare self-consistency with beam search decoding on the UL2-20B model. For a fair comparison we report the accuracy under the same number of beams and reasoning paths. On both tasks self-consistency outperforms beam search significantly. Note self-consistency can also adopt beam search to decode each reasoning path (results are shown as “Self-consistency using beam search”), but its performance is worse compared to self-consistency with sampling. The reason is that beam search yields a lower diversity in the outputs ( Li & Jurafsky, 2016 ) , while in self-consistency the diversity of the reasoning paths is the key to a better performance.

##### Comparison to Ensemble-based Approaches

We further compare self-consistency to ensemble-based methods for few-shot learning. In particular, we consider ensembling by: (1) prompt order permutation: we randomly permute the exemplars in the prompt 40 times to mitigate model’s sensitivity to prompt order ( Zhao et al., 2021 ; Lu et al., 2021 ) ; and (2) multiple sets of prompts ( Gao et al., 2021 ) : we manually write 3 3 different sets of prompts. We took majority vote of the answers from greedy decoding in both approaches as an ensemble. Table 7 shows that compared to self-consistency, existing ensemble-based approaches achieve a much smaller gain. 8 8 8 Self-consistency is compatible with both ensemble approaches and we show the results in Appendix A.1.4 . In addition, note that self-consistency is different from a typical model-ensemble approach, where multiple models are trained and their outputs are aggregated. Self-consistency acts more like a “self-ensemble” on top of a single language model. We additionally show the results of ensembling multiple models in Appendix A.1.3 where the model-ensembles perform much worse compared to self-consistency.

### 3.5 Additional Studies

We conducted a number of additional experiments to analyze different aspects of the self-consistency method, including its robustness to sampling strategies and parameters, and how it works with imperfect prompts and non-natural-language reasoning paths.

##### Self-Consistency is Robust to Sampling Strategies and Scaling

We show self-consistency is robust to sampling strategies and parameters, by varying T T in temperature sampling ( Ackley et al., 1985 ; Ficler & Goldberg, 2017 ) , k k in top- k k sampling ( Fan et al., 2018 ; Holtzman et al., 2018 ; Radford et al., 2019 ) , and p p in nucleus sampling ( Holtzman et al., 2020 ) , over PaLM-540B in Figure 4 (left). Figure 4 (right) shows that self-consistency robustly improves performance across all scales for the LaMDA-137B model series. The gain is relatively lower for smaller models due to certain abilities (e.g., arithmetic) only emerge when the model reaches a sufficient scale ( Brown et al., 2020 ) .

##### Self-Consistency Improves Robustness to Imperfect Prompts

For few-shot learning with manually constructed prompts, human annotators sometimes make minor mistakes when creating the prompts. We further study if self-consistency can help improve a language model’s robustness to imperfect prompts. 9 9 9 We use the same prompts as before, but swap all the numbers in the reasoning paths with random numbers except the final answer, e.g., from “ There are 3 cars in the parking lot already. 2 more arrive. Now there are 3 + 2 = 5 cars. ” to “ There are 7 cars in the parking lot already. 6 more arrive. Now there are 7 + 6 = 5 cars. ”. We show the results in Table 8 : while imperfect prompts decrease accuracy with greedy decoding (17.1 → \rightarrow 14.9), self-consistency can fill in the gaps and robustly improve the results.

Additionally, we found that the consistency (in terms of % of decodes agreeing with the final aggregated answer) is highly correlated with accuracy (Figure 8 , over GSM8K). This suggests that one can use self-consistency to provide an uncertainty estimate of the model in its generated solutions. In other words, one can use low consistency as an indicator that the model has low confidence; i.e., self-consistency confers some ability for the model to “know when it doesn’t know”.

##### Self-Consistency Works for Non-Natural-Language Reasoning Paths and Zero-shot CoT

We also tested the generality of the self-consistency concept to alternative forms of intermediate reasoning like equations (e.g., from “ There are 3 cars in the parking lot already. 2 more arrive. Now there are 3 + 2 = 5 cars. ” to “ 3 + 2 = 5 ”). The results are shown in Table 8 (“Prompt with equations”): self-consistency still improves accuracy by generating intermediate equations; however, compared to generating natural language reasoning paths, the gain is smaller since the equations are much shorter and less opportunity remains for generating diversity in the decoding process. In addition, we tested self-consistency with zero-shot chain-of-thought ( Kojima et al., 2022 ) and show that self-consistency works for zero-shot CoT as well and improves the results significantly (+26.2%) in Table 8 .

## 4 Related work

##### Reasoning in language models.

Language models are known to struggle in Type 2 tasks, such as arithmetic, logical and commonsense reasoning ( Evans, 2010 ) . Previous work has primarily focused on specialized approaches for improving reasoning ( Andor et al., 2019 ; Ran et al., 2019 ; Geva et al., 2020 ; Piękos et al., 2021 ) . Compared to prior work, self-consistency is applicable to a wide range of reasoning tasks without any additional supervision or fine-tuning, while still substantially improving the performance of the chain-of-thought prompting approach proposed in Wei et al. (2022) .

##### Sampling and re-ranking in language models.

Multiple decoding strategies for language models have been proposed in the literature, e.g., temperature sampling ( Ackley et al., 1985 ; Ficler & Goldberg, 2017 ) , top- k k sampling ( Fan et al., 2018 ; Holtzman et al., 2018 ; Radford et al., 2019 ) , nucleus sampling ( Holtzman et al., 2020 ) , minimum Bayes risk decoding ( Eikema & Aziz, 2020 ; Shi et al., 2022 ) , and typical decoding ( Meister et al., 2022 ) . Other work has sought to explicitly promote diversity in the decoding process ( Batra et al., 2012 ; Li et al., 2016 ; Vijayakumar et al., 2018 ) .

Re-ranking is another common approach to improve generation quality in language models ( Adiwardana et al., 2020 ; Shen et al., 2021 ) . Thoppilan et al. (2022) collect additional human annotations to train a re-ranker for response filtering. Cobbe et al. (2021) train a “verifier” to re-rank generated solutions, which substantially improves the solve rate on math tasks compared to just fine-tuning the language model. Elazar et al. (2021) improve the consistency of factual knowledge extraction by extending pre-training with an additional consistency loss. All these methods require either training an additional re-ranker or collecting additional human annotation, while self-consistency requires no additional training, fine-tuning, nor extra data collection.

##### Extract reasoning paths.

Some previous work has considered task-specific approaches for identifying reasoning paths, such as constructing semantic graphs ( Xu et al., 2021a ) , learning an RNN to retrieve reasoning paths over the Wikipedia graph ( Asai et al., 2020 ) , fine-tuning with human annotated reasoning paths on math problems ( Cobbe et al., 2021 ) , or training an extractor with heuristic-based pseudo reasoning paths ( Chen et al., 2019 ) . More recently, the importance of diversity in the reasoning processes has been noticed, but only leveraged via task-specific training, either through an additional QA model over extracted reasoning paths ( Chen et al., 2019 ) , or by the introduction of latent variables in a commonsense knowledge graph ( Yu et al., 2022 ) . Compared to these approaches, self-consistency is far simpler and requires no additional training. The approach we propose simply couples the generation of reasoning paths and a final answer by sampling from the decoder, using aggregation to recover the most consistent answer without additional modules.

##### Consistency in language models.

Some prior work has shown that language models can suffer from inconsistency in conversation ( Adiwardana et al., 2020 ) , explanation generation ( Camburu et al., 2020 ) , and factual knowledge extraction ( Elazar et al., 2021 ) . Welleck et al. (2020) use “consistency” to refer to generating an infinite-length sequence in recurrent language models. Nye et al. (2021) improve the logical consistency of samples from a System 1 model by adding a System 2-inspired logical reasoning module. In this paper we focus on a slightly different notion of “consistency”, i.e., utilizing answer consistency among diverse reasoning paths to improve accuracy.

## 5 Conclusion and Discussion

We introduced a simple yet effective method called self-consistency, and observed that it significantly improves accuracy in a range of arithmetic and commonsense reasoning tasks, across four large language models with varying scales. Beyond accuracy gains, self-consistency is also useful for collecting rationales when performing reasoning tasks with language models, and for providing uncertainty estimates and improved calibration of language model outputs.

One limitation of self-consistency is that it incurs more computation cost. In practice people can try a small number of paths (e.g., 5 or 10) as a starting point to realize most of the gains while not incurring too much cost, as in most cases the performance saturates quickly (Figure 2 ). As part of future work, one could use self-consistency to generate better supervised data to fine-tune the model, such that the model can give more accurate predictions in a single inference run after fine-tuning. In addition, we observed that language models can sometimes generate incorrect or nonsensical reasoning paths (e.g., the StrategyQA example in Table 4 , the two population numbers are not exactly correct), and further work is needed to better ground models’ rationale generations.

## Reproducibility Statement

In experiments, we included four different language models with varying scales. Two of them are public models: UL2 is a completely open-sourced model with model checkpoints available at https://github.com/google-research/google-research/tree/master/ul2 ; GPT-3 is also a public model with public API available at https://openai.com/api/ . For GPT-3, we have included two public engines (“code-davinci-001” and “code-davinci-002”) to further aid reproducibility, as Codex is currently free so anyone can reproduce the results. In addition, as our results make use of LaMDA-137B and PaLM-540B that are not publicly available, we provide the exact input prompts for all tasks in Appendix A.3 (and note that we do not perform any finetuning and only apply prompting to off-the-shelf language models).

## Ethics Statement

As we stated in the discussion, language models can sometimes generate nonsensical or non-factual reasoning paths, so one should use language models’ outputs with extra caution. We deal with reasoning tasks mostly and the generated rationales are only used for inspecting how a model reaches its answer. One could potentially use the generated rationales to further check why the model makes certain mistakes or whether the model contains any biases when performing a certain task. For language model in real-world use, further work is needed to better ground models’ predictions and improve model’s factuality and safety, to ensure the models do not cause harms to users.

## References

Ackley et al. (1985) David H. Ackley, Geoffrey E. Hinton, and Terrence J. Sejnowski. A learning algorithm for boltzmann machines. Cognitive Science , 9(1):147–169, 1985. ISSN 0364-0213. URL https://www.sciencedirect.com/science/article/pii/S0364021385800124 .

Adiwardana et al. (2020) Daniel Adiwardana, Minh-Thang Luong, David R. So, Jamie Hall, Noah Fiedel, Romal Thoppilan, Zi Yang, Apoorv Kulshreshtha, Gaurav Nemade, Yifeng Lu, and Quoc V. Le. Towards a human-like open-domain chatbot, 2020.

Amini et al. (2019) Aida Amini, Saadia Gabriel, Shanchuan Lin, Rik Koncel-Kedziorski, Yejin Choi, and Hannaneh Hajishirzi. MathQA: Towards interpretable math word problem solving with operation-based formalisms. In Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers) , pp. 2357–2367. Association for Computational Linguistics, June 2019. URL https://aclanthology.org/N19-1245 .

Andor et al. (2019) Daniel Andor, Luheng He, Kenton Lee, and Emily Pitler. Giving BERT a calculator: Finding operations and arguments with reading comprehension. In Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP) , 2019. URL https://aclanthology.org/D19-1609 .

Asai et al. (2020) Akari Asai, Kazuma Hashimoto, Hannaneh Hajishirzi, Richard Socher, and Caiming Xiong. Learning to retrieve reasoning paths over wikipedia graph for question answering. In International Conference on Learning Representations , 2020. URL https://openreview.net/forum?id=SJgVHkrYDH .

Bar-Haim et al. (2006) Roy Bar-Haim, Ido Dagan, Bill Dolan, Lisa Ferro, Danilo Giampiccolo, Bernardo Magnini, and Idan Szpektor. The second pascal recognising textual entailment challenge. In Proceedings of the second PASCAL challenges workshop on recognising textual entailment , 2006.

Batra et al. (2012) Dhruv Batra, Payman Yadollahpour, Abner Guzman-Rivera, and Gregory Shakhnarovich. Diverse m-best solutions in markov random fields. In Proceedings of the 12th European Conference on Computer Vision - Volume Part V , ECCV’12, pp. 1–16, Berlin, Heidelberg, 2012. Springer-Verlag. ISBN 9783642337147. URL https://doi.org/10.1007/978-3-642-33715-4_1 .

Bentivogli et al. (2009) Luisa Bentivogli, Peter Clark, Ido Dagan, and Danilo Giampiccolo. The fifth pascal recognizing textual entailment challenge. In TAC , 2009.

BIG-bench collaboration (2021) BIG-bench collaboration. Beyond the imitation game: Measuring and extrapolating the capabilities of language models. In preparation , 2021. URL https://github.com/google/BIG-bench/ .

Brown et al. (2020) Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel Ziegler, Jeffrey Wu, Clemens Winter, Chris Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei. Language models are few-shot learners. In Advances in Neural Information Processing Systems , 2020. URL https://proceedings.neurips.cc/paper/2020/file/1457c0d6bfcb4967418bfb8ac142f64a-Paper.pdf .

Camburu et al. (2018) Oana-Maria Camburu, Tim Rocktäschel, Thomas Lukasiewicz, and Phil Blunsom. e-snli: Natural language inference with natural language explanations. In S. Bengio, H. Wallach, H. Larochelle, K. Grauman, N. Cesa-Bianchi, and R. Garnett (eds.), Advances in Neural Information Processing Systems 31 , pp. 9539–9549. Curran Associates, Inc., 2018. URL http://papers.nips.cc/paper/8163-e-snli-natural-language-inference-with-natural-language-explanations.pdf .

Camburu et al. (2020) Oana-Maria Camburu, Brendan Shillingford, Pasquale Minervini, Thomas Lukasiewicz, and Phil Blunsom. Make up your mind! adversarial generation of inconsistent natural language explanations. In Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics , pp. 4157–4165, Online, July 2020. Association for Computational Linguistics. doi: 10.18653/v1/2020.acl-main.382 . URL https://aclanthology.org/2020.acl-main.382 .

Chen et al. (2019) Jifan Chen, Shih-Ting Lin, and Greg Durrett. Multi-hop question answering via reasoning chains. CoRR , abs/1910.02610, 2019. URL http://arxiv.org/abs/1910.02610 .

Chen et al. (2021) Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de Oliveira Pinto, Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman, et al. Evaluating large language models trained on code. arXiv preprint arXiv:2107.03374 , 2021.

Chowdhery et al. (2022) Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung, Charles Sutton, Sebastian Gehrmann, Parker Schuh, Kensen Shi, Sasha Tsvyashchenko, Joshua Maynez, Abhishek Rao, Parker Barnes, Yi Tay, Noam Shazeer, Vinodkumar Prabhakaran, Emily Reif, Nan Du, Ben Hutchinson, Reiner Pope, James Bradbury, Jacob Austin, Michael Isard, Guy Gur-Ari, Pengcheng Yin, Toju Duke, Anselm Levskaya, Sanjay Ghemawat, Sunipa Dev, Henryk Michalewski, Xavier Garcia, Vedant Misra, Kevin Robinson, Liam Fedus, Denny Zhou, Daphne Ippolito, David Luan, Hyeontaek Lim, Barret Zoph, Alexander Spiridonov, Ryan Sepassi, David Dohan, Shivani Agrawal, Mark Omernick, Andrew M. Dai, Thanumalayan Sankaranarayana Pillai, Marie Pellat, Aitor Lewkowycz, Erica Moreira, Rewon Child, Oleksandr Polozov, Katherine Lee, Zongwei Zhou, Xuezhi Wang, Brennan Saeta, Mark Diaz, Orhan Firat, Michele Catasta, Jason Wei, Kathy Meier-Hellstern, Douglas Eck, Jeff Dean, Slav Petrov, and Noah Fiedel. Palm: Scaling language modeling with pathways, 2022. URL https://arxiv.org/abs/2204.02311 .

Clark et al. (2019) Christopher Clark, Kenton Lee, Ming-Wei Chang, Tom Kwiatkowski, Michael Collins, and Kristina Toutanova. Boolq: Exploring the surprising difficulty of natural yes/no questions. In NAACL , 2019.

Clark et al. (2018) Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot, Ashish Sabharwal, Carissa Schoenick, and Oyvind Tafjord. Think you have solved question answering? try arc, the ai2 reasoning challenge. ArXiv , abs/1803.05457, 2018.

Cobbe et al. (2021) Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, Christopher Hesse, and John Schulman. Training verifiers to solve math word problems, 2021.

Dagan et al. (2005) Ido Dagan, Oren Glickman, and Bernardo Magnini. The pascal recognising textual entailment challenge. In Machine Learning Challenges Workshop , pp. 177–190. Springer, 2005.

Eikema & Aziz (2020) Bryan Eikema and Wilker Aziz. Is MAP decoding all you need? the inadequacy of the mode in neural machine translation. In Proceedings of the 28th International Conference on Computational Linguistics , pp. 4506–4520, Barcelona, Spain (Online), December 2020. International Committee on Computational Linguistics. URL https://aclanthology.org/2020.coling-main.398 .

Elazar et al. (2021) Yanai Elazar, Nora Kassner, Shauli Ravfogel, Abhilasha Ravichander, Eduard Hovy, Hinrich Schütze, and Yoav Goldberg. Measuring and improving consistency in pretrained language models. Transactions of the Association for Computational Linguistics , 9:1012–1031, 2021. doi: 10.1162/tacl_a_00410 . URL https://aclanthology.org/2021.tacl-1.60 .

Evans (2010) Jonathan St BT Evans. Intuition and reasoning: A dual-process perspective. Psychological Inquiry , 21(4):313–326, 2010.

Fan et al. (2018) Angela Fan, Mike Lewis, and Yann Dauphin. Hierarchical neural story generation. In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , pp. 889–898, Melbourne, Australia, July 2018. Association for Computational Linguistics. doi: 10.18653/v1/P18-1082 . URL https://aclanthology.org/P18-1082 .

Ficler & Goldberg (2017) Jessica Ficler and Yoav Goldberg. Controlling linguistic style aspects in neural language generation. In Proceedings of the Workshop on Stylistic Variation , pp. 94–104, Copenhagen, Denmark, September 2017. Association for Computational Linguistics. doi: 10.18653/v1/W17-4912 . URL https://aclanthology.org/W17-4912 .

Gao et al. (2021) Tianyu Gao, Adam Fisch, and Danqi Chen. Making pre-trained language models better few-shot learners. In Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers) , pp. 3816–3830, Online, August 2021. Association for Computational Linguistics. doi: 10.18653/v1/2021.acl-long.295 . URL https://aclanthology.org/2021.acl-long.295 .

Geva et al. (2020) Mor Geva, Ankit Gupta, and Jonathan Berant. Injecting numerical reasoning skills into language models. In Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics , 2020. doi: 10.18653/v1/2020.acl-main.89 . URL https://aclanthology.org/2020.acl-main.89 .

Geva et al. (2021) Mor Geva, Daniel Khashabi, Elad Segal, Tushar Khot, Dan Roth, and Jonathan Berant. Did aristotle use a laptop? A question answering benchmark with implicit reasoning strategies. Transactions of the Association for Computational Linguistics , 2021. URL https://aclanthology.org/2021.tacl-1.21 .

Giampiccolo et al. (2007) Danilo Giampiccolo, Bernardo Magnini, Ido Dagan, and Bill Dolan. The third pascal recognizing textual entailment challenge. In Proceedings of the ACL-PASCAL workshop on textual entailment and paraphrasing , pp. 1–9. Association for Computational Linguistics, 2007.

Holtzman et al. (2018) Ari Holtzman, Jan Buys, Maxwell Forbes, Antoine Bosselut, David Golub, and Yejin Choi. Learning to write with cooperative discriminators. In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , pp. 1638–1649, Melbourne, Australia, July 2018. Association for Computational Linguistics. doi: 10.18653/v1/P18-1152 . URL https://aclanthology.org/P18-1152 .

Holtzman et al. (2020) Ari Holtzman, Jan Buys, Li Du, Maxwell Forbes, and Yejin Choi. The curious case of neural text degeneration. In International Conference on Learning Representations , 2020. URL https://openreview.net/forum?id=rygGQyrFvH .

Hosseini et al. (2014) Mohammad Javad Hosseini, Hannaneh Hajishirzi, Oren Etzioni, and Nate Kushman. Learning to solve arithmetic word problems with verb categorization. In Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP) , 2014. doi: 10.3115/v1/D14-1058 . URL https://aclanthology.org/D14-1058 .

Khashabi et al. (2020) Daniel Khashabi, Sewon Min, Tushar Khot, Ashish Sabharwal, Oyvind Tafjord, Peter Clark, and Hannaneh Hajishirzi. UNIFIEDQA: Crossing format boundaries with a single QA system. In Findings of the Association for Computational Linguistics: EMNLP 2020 , pp. 1896–1907, Online, November 2020. Association for Computational Linguistics. doi: 10.18653/v1/2020.findings-emnlp.171 . URL https://aclanthology.org/2020.findings-emnlp.171 .

Kojima et al. (2022) Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yutaka Matsuo, and Yusuke Iwasawa. Large language models are zero-shot reasoners. In Alice H. Oh, Alekh Agarwal, Danielle Belgrave, and Kyunghyun Cho (eds.), Advances in Neural Information Processing Systems , 2022. URL https://openreview.net/forum?id=e2TBb5y0yFf .

Koncel-Kedziorski et al. (2016) Rik Koncel-Kedziorski, Subhro Roy, Aida Amini, Nate Kushman, and Hannaneh Hajishirzi. MAWPS: A math word problem repository. In Proceedings of the 2016 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies , 2016. doi: 10.18653/v1/N16-1136 . URL https://aclanthology.org/N16-1136 .

Lan et al. (2021) Yihuai Lan, Lei Wang, Qiyuan Zhang, Yunshi Lan, Bing Tian Dai, Yan Wang, Dongxiang Zhang, and Ee-Peng Lim. MWPToolkit: An open-source framework for deep learning-based math word problem solvers. arXiv preprint arXiv:2109.00799 , 2021. URL https://arxiv.org/abs/2109.00799 .

Li & Jurafsky (2016) Jiwei Li and Dan Jurafsky. Mutual information and diverse decoding improve neural machine translation, 2016. URL https://arxiv.org/abs/1601.00372 .

Li et al. (2016) Jiwei Li, Will Monroe, and Dan Jurafsky. A simple, fast diverse decoding algorithm for neural generation. CoRR , abs/1611.08562, 2016. URL http://arxiv.org/abs/1611.08562 .

Ling et al. (2017) Wang Ling, Dani Yogatama, Chris Dyer, and Phil Blunsom. Program induction by rationale generation: Learning to solve and explain algebraic word problems. In Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , 2017. doi: 10.18653/v1/P17-1015 . URL https://aclanthology.org/P17-1015 .

Lu et al. (2021) Yao Lu, Max Bartolo, Alastair Moore, Sebastian Riedel, and Pontus Stenetorp. Fantastically ordered prompts and where to find them: Overcoming few-shot prompt order sensitivity. ArXiv , abs/2104.08786, 2021.

Meister et al. (2022) Clara Meister, Tiago Pimentel, Gian Wiher, and Ryan Cotterell. Typical decoding for natural language generation. arXiv preprint arXiv:2202.00666 , 2022.

Miao et al. (2020) Shen Yun Miao, Chao Chun Liang, and Keh Yih Su. A diverse corpus for evaluating and developing English math word problem solvers. In Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics , 2020. URL https://aclanthology.org/2020.acl-main.92 .

Nie et al. (2020) Yixin Nie, Adina Williams, Emily Dinan, Mohit Bansal, Jason Weston, and Douwe Kiela. Adversarial NLI: A new benchmark for natural language understanding. In Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics . Association for Computational Linguistics, 2020.

Nye et al. (2021) Maxwell Nye, Michael Henry Tessler, Joshua B. Tenenbaum, and Brenden M. Lake. Improving coherence and consistency in neural sequence models with dual-system, neuro-symbolic reasoning. In A. Beygelzimer, Y. Dauphin, P. Liang, and J. Wortman Vaughan (eds.), Advances in Neural Information Processing Systems , 2021. URL https://openreview.net/forum?id=uyKk_avJ-p4 .

Patel et al. (2021) Arkil Patel, Satwik Bhattamishra, and Navin Goyal. Are NLP models really able to solve simple math word problems? In Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies , pp. 2080–2094, Online, June 2021. Association for Computational Linguistics. doi: 10.18653/v1/2021.naacl-main.168 . URL https://aclanthology.org/2021.naacl-main.168 .

Pi et al. (2022) Xinyu Pi, Qian Liu, Bei Chen, Morteza Ziyadi, Zeqi Lin, Yan Gao, Qiang Fu, Jian-Guang Lou, and Weizhu Chen. Reasoning like program executors, 2022.

Piękos et al. (2021) Piotr Piękos, Mateusz Malinowski, and Henryk Michalewski. Measuring and improving BERT’s mathematical abilities by predicting the order of reasoning. In Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 2: Short Papers) , 2021. doi: 10.18653/v1/2021.acl-short.49 . URL https://aclanthology.org/2021.acl-short.49 .

Radford et al. (2019) Alec Radford, Jeff Wu, Rewon Child, David Luan, Dario Amodei, and Ilya Sutskever. Language models are unsupervised multitask learners. 2019.

Rae et al. (2021) Jack W Rae, Sebastian Borgeaud, Trevor Cai, Katie Millican, Jordan Hoffmann, Francis Song, John Aslanides, Sarah Henderson, Roman Ring, Susannah Young, et al. Scaling language models: Methods, analysis & insights from training gopher. arXiv preprint arXiv:2112.11446 , 2021.

Ran et al. (2019) Qiu Ran, Yankai Lin, Peng Li, Jie Zhou, and Zhiyuan Liu. NumNet: Machine reading comprehension with numerical reasoning. In Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP) , 2019. doi: 10.18653/v1/D19-1251 . URL https://aclanthology.org/D19-1251 .

Roy & Roth (2015) Subhro Roy and Dan Roth. Solving general arithmetic word problems. In Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing , 2015. doi: 10.18653/v1/D15-1202 . URL https://aclanthology.org/D15-1202 .

Shen et al. (2021) Jianhao Shen, Yichun Yin, Lin Li, Lifeng Shang, Xin Jiang, Ming Zhang, and Qun Liu. Generate & rank: A multi-task framework for math word problems. In Findings of the Association for Computational Linguistics: EMNLP 2021 , pp. 2269–2279, Punta Cana, Dominican Republic, November 2021. Association for Computational Linguistics. URL https://aclanthology.org/2021.findings-emnlp.195 .

Shi et al. (2022) Freda Shi, Daniel Fried, Marjan Ghazvininejad, Luke Zettlemoyer, and Sida I. Wang. Natural language to code translation with execution. In Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing , pp. 3533–3546, Abu Dhabi, United Arab Emirates, December 2022. Association for Computational Linguistics. URL https://aclanthology.org/2022.emnlp-main.231 .

Stanovich & West (2000) Keith E Stanovich and Richard F West. Individual differences in reasoning: Implications for the rationality debate? Behavioral and brain sciences , 23(5):645–665, 2000. URL https://pubmed.ncbi.nlm.nih.gov/11301544/ .

Talmor et al. (2019) Alon Talmor, Jonathan Herzig, Nicholas Lourie, and Jonathan Berant. CommonsenseQA: A question answering challenge targeting commonsense knowledge. In Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers) , 2019. URL https://aclanthology.org/N19-1421 .

Tay et al. (2022) Yi Tay, Mostafa Dehghani, Vinh Q. Tran, Xavier Garcia, Jason Wei, Xuezhi Wang, Hyung Won Chung, Dara Bahri, Tal Schuster, Steven Zheng, Denny Zhou, Neil Houlsby, and Donald Metzler. Unifying language learning paradigms, 2022. URL https://arxiv.org/abs/2205.05131 .

Thoppilan et al. (2022) Romal Thoppilan, Daniel De Freitas, Jamie Hall, Noam Shazeer, Apoorv Kulshreshtha, Heng-Tze Cheng, Alicia Jin, Taylor Bos, Leslie Baker, Yu Du, et al. Lamda: Language models for dialog applications. arXiv preprint arXiv:2201.08239 , 2022. URL https://arxiv.org/abs/2201.08239 .

Vijayakumar et al. (2018) Ashwin Vijayakumar, Michael Cogswell, Ramprasaath Selvaraju, Qing Sun, Stefan Lee, David Crandall, and Dhruv Batra. Diverse beam search for improved description of complex scenes. Proceedings of the AAAI Conference on Artificial Intelligence , 32, Apr. 2018. URL https://ojs.aaai.org/index.php/AAAI/article/view/12340 .

Wei et al. (2022) Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc Le, and Denny Zhou. Chain of thought prompting elicits reasoning in large language models. Conference on Neural Information Processing Systems (NeurIPS) , 2022. URL https://arxiv.org/pdf/2201.11903 .

Welleck et al. (2020) Sean Welleck, Ilia Kulikov, Jaedeok Kim, Richard Yuanzhe Pang, and Kyunghyun Cho. Consistency of a recurrent language model with respect to incomplete decoding. In Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP) , pp. 5553–5568, Online, November 2020. Association for Computational Linguistics. doi: 10.18653/v1/2020.emnlp-main.448 . URL https://aclanthology.org/2020.emnlp-main.448 .

Xu et al. (2021a) Weiwen Xu, Yang Deng, Huihui Zhang, Deng Cai, and Wai Lam. Exploiting reasoning chains for multi-hop science question answering. In Findings of the Association for Computational Linguistics: EMNLP 2021 , pp. 1143–1156, Punta Cana, Dominican Republic, November 2021a. Association for Computational Linguistics. URL https://aclanthology.org/2021.findings-emnlp.99 .

Xu et al. (2021b) Yichong Xu, Chenguang Zhu, Shuohang Wang, Siqi Sun, Hao Cheng, Xiaodong Liu, Jianfeng Gao, Pengcheng He, Michael Zeng, and Xuedong Huang. Human parity on commonsenseqa: Augmenting self-attention with external attention, 2021b. URL https://arxiv.org/abs/2112.03254 .

Yang et al. (2018) Zhilin Yang, Peng Qi, Saizheng Zhang, Yoshua Bengio, William Cohen, Ruslan Salakhutdinov, and Christopher D. Manning. HotpotQA: A dataset for diverse, explainable multi-hop question answering. In Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing , pp. 2369–2380, Brussels, Belgium, October-November 2018. Association for Computational Linguistics. doi: 10.18653/v1/D18-1259 . URL https://aclanthology.org/D18-1259 .

Ye & Durrett (2022) Xi Ye and Greg Durrett. The unreliability of explanations in few-shot prompting for textual reasoning. In Alice H. Oh, Alekh Agarwal, Danielle Belgrave, and Kyunghyun Cho (eds.), Advances in Neural Information Processing Systems , 2022. URL https://openreview.net/forum?id=Bct2f8fRd8S .

Yu et al. (2022) Wenhao Yu, Chenguang Zhu, Lianhui Qin, Zhihan Zhang, Tong Zhao, and Meng Jiang. Diversifying content generation for commonsense reasoning with mixture of knowledge graph experts. In Findings of Annual Meeting of the Association for Computational Linguistics (ACL) , 2022.

Zhao et al. (2021) Zihao Zhao, Eric Wallace, Shi Feng, Dan Klein, and Sameer Singh. Calibrate before use: Improving few-shot performance of language models. In Marina Meila and Tong Zhang (eds.), Proceedings of the 38th International Conference on Machine Learning , volume 139 of Proceedings of Machine Learning Research . PMLR, 2021. URL https://proceedings.mlr.press/v139/zhao21c.html .

## Appendix A Appendix

### A.1 Additional Experiment Results

#### A.1.1 Robustness to Sampling Strategies and Parameters

In Figure 6 we ablate the results with respect to different sampling strategies and parameters by varying T T in temperature sampling and k k in Top- k k sampling, on LaMDA-137B. We show that self-consistency is robust to various sampling strategies and parameters.

In Figure 7 and Figure 8 , we show the results of self-consistency compared with greedy decoding a single path over LaMDA-137B and PaLM-540B, respectively. Self-consistency improves over greedy decode by a quite significant margin on both models, on top of high accuracy already achieved by scaling up model sizes.

We further show additional sampled reasoning paths from the LaMDA-137B model in Table 12 , and sampled reasoning paths from the PaLM-540B model in Table 13 . We see that the diversity in the additionally sampled reasoning paths indeed helps the model arrive at a more correct final answer after aggregation.

#### A.1.2 Robustness to different sets of prompts

In Table 9 , we further show that self-consistency is quite robust to different sets of input prompts. We manually wrote 3 different sets of chain-of-thought as prompts to the model. Across all sets of prompts, self-consistency yields consistent gains over the original CoT approach.

#### A.1.3 Compared to model ensembles

Additionally, we provide results of directly ensembling the outputs from multiple language models . The results are shown in Table 10 , by greedily decoding sequences from 3 language models and taking the majority vote (averaged over 10 runs). Note this is a typical ensemble approach (averaging over the predictions over multiple models) and it achieves a performance significantly worse than self-consistency (self-consistency over PaLM-540B gets an accuracy of 74.4%), as lower-capacity models drag down the performance of higher-capacity models. In addition, this approach is limited in two ways: 1) It requires multiple models for an ensemble which might not always be available, while self-consistency only requires one single model to “self-ensemble”; 2) If one of the models is much weaker, it can actually hurt the final performance.

#### A.1.4 Combining self-consistency with other ensembling strategies

Self-consistency is completely compatible with other ensemble strategies, although the gains achieved by self-consistency are significantly higher than other ensemble strategies (and can “override” the performance gains achieved by other ensemble strategies). We further performed experiments and include the results in Table 11 (for a fair comparison, we use 40 sets of prompts, or 40 prompt permutations to compare with self-consistency with 40 paths, all experiments are based on PaLM-540B).

### A.2 Details on Resources and Inference

For all four language models we perform prompting-based inference only. For UL2 we use TPU v3 (2x2 configuration, 4 chips, 8 cores). For GPT-3 models the experiments are done though the public API. 10 10 10 https://beta.openai.com/docs/api-reference/making-requests For LaMDA-137B we use TPU v3 (8x8 configuration, 64 chips, 128 cores). For PaLM-540B we use TPU v4 (4x4x12 configuration, 192 chips, 384 cores). Most inference jobs take 1 to 4 hours (over about 1,000 examples) for each task on UL2 and LaMDA-137B, and about 2 to 12 hours on PaLM-540B. Some tasks (e.g., commonsense reasoning) take longer but do not exceed 2 days for each task.

For GPT-3 models, we use 128 max tokens for all methods, without frequency penalty or presence penalty. For all models, we take the generated outputs until the start of the next “Q:" to parse the final answers, consistent with our prompting format.

### A.3 Full Sets of Prompts

We list the full details of the prompts used for two newly-introduced datasets, AQUA-RAT ( Ling et al., 2017 ) and AI2 Reasoning Challenge (ARC) ( Clark et al., 2018 ) , where we manually composed the example chain-of-thought in this paper, in Table 14 and Table 15 , respectively.

As additional information, we also list the exact set of prompts used for all arithmetic reasoning tasks in Table 17 , since there are multiple sets of prompts introduced in Wei et al. (2022) . The prompts for CommonsenseQA and StrategyQA are the same as used in Wei et al. (2022) .

We provide the exact prompts used for common NLP tasks in the following tables as well, including NLI (Table 18 , Table 19 , Table 20 ) and Closed-Book Question-Answering tasks (Table 16 , Table 21 ).

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
