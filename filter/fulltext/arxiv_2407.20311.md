##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Physics of Language Models: Part 2.1, Grade-School Math and the Hidden Reasoning Process Thanks: Project page + video: https://physics.allen-zhu.com/part-2-grade-school-math/part-2-1 . We would like to thank Lin Xiao, Chunting Zhou for many helpful conversations. We would like to extend special thanks to Lucca Bertoncini, Liao Hu, Caleb Ho, Wil Johnson, Apostolos Kokolis, Parth Malani, Alexander Miller, Junjie Qian and Shubho Sengupta from Meta FAIR; Henry Estela, Rizwan Hashmi, Lucas Noah, and Maxwell Taylor from the Meta Cloud Foundation team; as well as Ian Clark, Gourab De, Anmol Mann, and Max Pfeifer from W&B . Without their invaluable support, the experiments in this paper would not have been possible.

###### Abstract

Recent advances in language models have demonstrated their capability to solve mathematical reasoning problems, achieving near-perfect accuracy on grade-school level math benchmarks like GSM8K. In this paper, we formally study how language models solve these problems. We design a series of controlled experiments to address several fundamental questions: (1) Can language models truly develop reasoning skills, or do they simply memorize templates? (2) What is the model’s hidden (mental) reasoning process? (3) Do models solve math questions using skills similar to or different from humans? (4) Do models trained on GSM8K-like datasets develop reasoning skills beyond those necessary for solving GSM8K problems? (5) What mental process causes models to make reasoning mistakes? (6) How large or deep must a model be to effectively solve GSM8K-level math questions?

Our study uncovers many hidden mechanisms by which language models solve mathematical questions, providing insights that extend beyond current understandings of LLMs.

## 1 Introduction

The field of language models has made significant progress in recent years. Large models like GPT-4 [ 17 ] have shown initial signs of general intelligence [ 8 ] , while smaller models have demonstrated good reasoning abilities by solving challenging coding and math problems [ 15 , 11 , 16 ] .

In this paper, we focus on the ability of small language models to solve grade-school math problems. Unlike previous works that empirically push the accuracy of models on grade-school math benchmarks like GSM8K [ 9 ] and its augmentations (e.g., [ 16 , 22 ] ), we take a more principled approach. We aim to understand the following fundamental questions: 1. How do language models learn to solve grade-school level math problems? Do they just memorize templates, or do they learn reasoning skills similar to humans? Or do they discover new skills to solve the problems?

2. Do models trained solely on grade-school math problems only learn to solve these problems, or do they develop some more general intelligence?

3. How small can a language model be while still solving grade-school math problems? Is depth (number of layers) more important than width (number of neurons per layer), or does only size matter as suggested by practitioners [ 14 ] ?

These questions are fundamental to understanding the intelligence of language models. To study them, it might seem tempting to start with a pre-trained model and fine-tune it on existing datasets like GSM8K or GPT-4 augmented ones (e.g., [ 16 , 22 ] ). However, this approach has significant limitations: • Data contamination. The pretrain data of existing models mostly come from publicly available internet [ 10 ] , which is a pile of mess. We do not know how many math problems are included or their structures. There is significant concern regarding whether the GSM8K benchmark has been leaked to language models’ training datasets [ 22 ] . Even if the exact data is not, the pre-trained model might have seen almost identical questions (e.g., the same problem with different numbers). Thus, this approach cannot answer questions 1-3. We do not know whether a model truly learns the reasoning skills or it simply memorizes problem templates during training. Therefore, we need full control over the model’s pretrain data and must train a language model from scratch. This point has been reiterated recently in [ 3 , 2 ] .

• Solution diversity. The existing fine-tuning data, such as the GSM8K training set, contains only 7.5K grade-school math problems, which is insufficient to train a model from scratch. Although recent works use GPT-4 to augment GSM8K, this is not enough for our purpose. GPT-4 augmented problems might be biased towards a small number of solution templates, since the original GSM8K data has very few (obviously, at most 8K) solution templates. We need a much larger, more diverse set of grade-school math problems .

With these points in mind, we introduce our framework to generate a large set of diverse grade-school math (GSM) problems and use the dataset to train (from scratch) and test a GPT2-like language model. In the framework, we focus on the “logical reasoning” aspect of grade-school math problems, which involves the dependency of parameters in the problem statement, such as “Alice’s apple is three times the sum of Bob’s orange and Charles’s banana.” We use synthetic sentences to reduce the difficulty arising from Common Sense , like “a candle burned for 12 hours at 1 inch per hour” (implying the candle is reducing in length). We also remove the difficulty from pure arithmetic: we only consider integers and arithmetic mod 23 \bmod 23 . 1 1 1 There is a rich literature studying how well language models can learn arithmetic and length generalization, see [ 23 , 13 ] and the references therein. Modern language models are also equipped with retrieval-augmented generation (RAG), allowing arithmetic computations to be delegated to a calculator.

Moreover, our framework ensures that the generated math problems are highly diverse and do not come from a small subset of templates. Even ignoring all the arithmetic, English, variable names, and unused parameters, our problems still have more than 90 trillion solution templates (see Proposition 2.2 ), much larger than the size of GPT2-small (100M). Thus, language models cannot solve the math problems in our case by simply memorizing the solution templates.

In this paper, we use the GPT2 model [ 18 ] , but replace its positional embedding with rotary embedding (RoPE) [ 20 , 7 ] . We still call it GPT2 for brevity. We summarize our main contributions: – Result 2. We demonstrate that the GPT2 model, pretrained on our synthetic dataset, not only achieves 99% accuracy in solving math problems from the same distribution but also out-of-distribution generalizes, such as to those of longer reasoning lengths than any seen during training. This is similar to length generalization in arithmetics [ 6 , 13 ] , however, in our case, the model has never seen any training example of the same length as in test time. This signifies that the model can truly learn some reasoning skill instead of memorizing solution templates.

– Result 3. Crucially, the model can learn to generate shortest solutions, almost always avoiding unnecessary computations. This suggests that the model formulates a plan before it generates, in order to avoid computing any quantities that are not needed towards solving the underlying math problem.

– Result 4. We examine the model’s internal states through probing, introducing six probing tasks to elucidate how the model solves math problems. For instance, we discover the model (mentally!) preprocesses the full set of necessary parameters before it starts any generation. Likewise, humans also do this preprocess although we write this down on scratch pads.

– Result 5. Surprisingly, the model also learns unnecessary, yet important skills after pretraining, such as all-pair dependency. Before any question is asked, it already (mentally!) computes with good accuracy which parameters depend on which, even though some are not needed for solving the math problem . Note that computing all-pair dependency is a skill not needed to fit all the solutions in the training data. To the best of our knowledge, this is the first evidence that a language model can learn useful skills beyond those necessary to fit its pretraining data. 2 2 2 In our case, one can solve all the math problems without computing all-pair dependency. Our pretraining data never includes such information — all the solutions only compute necessary variables. This may be a preliminary signal of where the G in AGI can come from. 3 3 3 Indeed, the skill to sort relationships among in-context objects is a general skill, which may lead to — via instruction fine-tuning — skills for solving other tasks, such as discovering causal relationships, determining the influence of parameter changes, etc.

– Result 6. We explain why mistakes occur. For instance, the model makes systematic errors that can be explained by probing its internal states. Sometimes, these mistakes can be predicted before the model generates answers, making them independent of the random generation process. We connect this to practice, noting that GPT-4/4o also makes similar errors (though we cannot probe their internal states).

– Result 7+8. The depth of the language model is crucial for its reasoning ability. For example, a 16-layer, 576-dim transformer solves harder problems (in reasoning length) than a 4-layer, 1920-dim one, despite the latter being twice as large. This holds even when Chain-of-Thought (CoT) is used. We explain this necessity in depth by the complexity of the mental processes involved. We advocate for the use of controlled, synthetic data as a more principled approach to derive such claims, contrasting with predictions like “only size matters” based on training loss using internet pretrain data [ 14 ] .

While we refrain from overstating that our findings directly apply to foundation models like GPT-4 or more challenging mathematical reasoning tasks, we believe our work significantly advances the understanding of how language models develop their mathematical reasoning skills, and this has to be done in a way different from pushing benchmarks .

## 2 Result 1: Data Generation

Motivation. Recall a standard grade-school math problem in the GSM8K dataset [ 9 ] looks like: Betty is saving money for a new wallet which costs 100. Betty has only half of the money she needs. Her parents decided to give her 15 for that purpose, and her grandparents twice as much as her parents. How much more money does Betty need to buy the wallet? This problem involves multiple parameters whose values are connected through various equalities, such as “Betty’s current money = 0.5 × \times cost of the wallet” and “money given by grandparents = 2 × \times money given by parents.” Motivated by this, we build a GSM8K-like math dataset through a synthetic generation pipeline that captures the dependencies of parameters. We wish to capture at least the following three types of dependencies. 1. Direct dependency ( ♡ \heartsuit ): such as A = 5 × ( X + Y ) A=5\times(X+Y) , so A A can be computed after X X and Y Y .

2. Instance dependency ( ♠ \spadesuit ): such as “every classroom has X chairs, and there are Y classrooms.” Here, the model must infer the total number of chairs by multiplying X by Y.

3. Implicit dependency ( ♣ \clubsuit ): such as “Bob has 3 times more fruits than Alice. Alice has 3 apples, 4 eggs and 2 bananas.” Here, the model must learn that apples and bananas are fruits and egg is not, and “Alice’s fruits” is an abstract parameter derived from the problem statement.

### 2.1 Step 1: Graph Construction and Problem Generation

Hierarchical categorization. We use a layered structure of categories , each contains possible items . For instance, categories = ( School , Classroom , Backpack ) has three layers; category School = { Central High , Riverview High , …}; category Classroom = { Dance Studio , Film Studio , …}; category Backpack = { School Daypack , Messenger Backpack , …}. We prepare 4 predefined hierarchical categorizations, each with 4 layers and 100 items in each layer; this represents the world knowledge.

Structure graph. In each math problem, only specific items exist, leading to a structure graph that outlines what sub-items can appear under what item, see Figure 1 (left). For instance, • Connecting Dance Studio and School Daypack with an edge signifies an instance parameter , ‘‘the number of school daypacks in each dance studio,’’ which is a quantifiable variable that can be assigned. 4 4 4 Even though Central High and Rivierside High can both have (possibly multiple) Dance Studios, for simplicity, we assume that each Dance Studio has the same number of School Daypacks. This captures the instance dependency ( ♠ \spadesuit ) as mentioned above.

• Abstract parameters , like “the total number of classrooms in Central High,” cannot be assigned and are excluded from the structure graph. They reflect implicity dependency ( ♣ \clubsuit ) .

###### Remark 2.1 .

Rather than using simple objects like Alice’s apple or fake items like Items A/B/C/D , this structure allows us to describe abstract parameters and adds 2 levels of complexity to the data: • The model must implicitly learn English concepts, such as a classroom category includes 100 different classroom types. These concepts cannot be derived from individual math problems, as only a limited selection of classrooms will be mentioned in each problem.

• The model is required to hierarchically access multiple items to calculate abstract parameters, as opposed to a straightforward retrieval of ‘‘Alice’s apple’’ in the context. 5 5 5 For example, the total number of backpacks in Riverview High in Figure 1 is calculated as i ​ p 1 × a ​ p 1 + i ​ p 2 × a ​ p 2 ip_{1}\times ap_{1}+ip_{2}\times ap_{2} where i ​ p 1 = “Riverview High’s number of Dance Studios” ip_{1}=\textrm{``Riverview High's number of Dance Studios''} , i ​ p 2 = “Riverview High’s number of Film Studios” ip_{2}=\textrm{``Riverview High's number of Film Studios''} , a ​ p 1 = “each Dance Studio’s number of Backpacks” ap_{1}=\textrm{``each Dance Studio's number of Backpacks''} , and a ​ p 2 = “each Film Studio’s number of Backpacks” ap_{2}=\textrm{``each Film Studio's number of Backpacks''} , with i ​ p 1 , i ​ p 2 ip_{1},ip_{2} being instance parameters and a ​ p 1 , a ​ p 2 ap_{1},ap_{2} abstract parameters. Here, the model must not only retrieve i ​ p 1 , i ​ p 2 ip_{1},ip_{2} but also compute a ​ p 1 , a ​ p 2 ap_{1},ap_{2} hierarchically.

Dependency graph. The dependency graph is a directed acyclic graph that outlines the dependency among parameters. For each instance parameter , we choose a random set of (up to 4) parameters it can depend on — including possibly a special vertex 𝖱𝖭𝖦 \mathsf{RNG} representing a random number generator. For instance, if “[param A ] is X X more than the difference of [param B ] and [param C ]” for X X being randomly generated, then we draw edges from B, C and 𝖱𝖭𝖦 \mathsf{RNG} to parameter A. The dependency of abstract parameters is implied by the dependency of instance parameters. This captures direct dependency ( ♡ \heartsuit ) as mentioned above. We give an examples on the right side of Figure 1 , and details for how we randomly generate such dependency graph are in Appendix D.2 .

Problem generation. The problem is articulated by describing the dependency graphs in English, one sentence for each instance parameter. 6 6 6 We use simple English sentence templates to describe the problem, and did not worry about grammar mistakes such as singular vs plural forms. There are other randomness besides the dependency graph, such as when parameter A A depends on B , C B,C it could be A + B A+B or A − B A-B . (Abstract parameters are not described because they are inherited by the structure graph.) We randomly permute the sentence ordering to further increase difficulty. A parameter is selected and asked with a question in the end (or at the beginning). Below is an easy example corresponding to Figure 1 ; a harder example is in Figure 11 . (Problem - Easy) The number of each Riverview High’s Film Studio equals 5 times as much as the sum of each Film Studio’s Backpack and each Dance Studio’s School Daypack. The number of each Film Studio’s School Daypack equals 12 more than the sum of each Film Studio’s Messenger Backpack and each Central High’s Film Studio. The number of each Central High’s Film Studio equals the sum of each Dance Studio’s School Daypack and each Film Studio’s Messenger Backpack. The number of each Riverview High’s Dance Studio equals the sum of each Film Studio’s Backpack, each Film Studio’s Messenger Backpack, each Film Studio’s School Daypack and each Central High’s Backpack. The number of each Dance Studio’s School Daypack equals 17. The number of each Film Studio’s Messenger Backpack equals 13. How many Backpack does Central High have? (2.1)

### 2.2 Step 2: Solution Construction (CoT)

Let solution be a sequence of sentences describing the necessary steps towards solving the given problem, where the sentences follow any topological order — also known as Chain-of-Thought, CoT. For each parameter necessary towards answering the final question, we assign to it a random letter among the 52 choices (a..z or A..Z), and use a sentence to describe its computation: 7 7 7 There are different ways to format the CoT solution. We noted that starting with “Define [param] as X” instead of [intermediate steps] improves the model’s accuracy, so we have adhered to this CoT format. Define [param] as X; [intermediate steps]; so X = … Throughout this paper, we consider arithmetics mod 23 23 to avoid errors from computation involving large numbers. It is perhaps the easiest to directly see a solution example (corresponding to ( 2.1 ) ), and a more involved example is in Figure 11 : (Solution - Easy) Define Dance Studio’s School Daypack as p; so p = 17. Define Film Studio’s Messenger Backpack as W; so W = 13. Define Central High’s Film Studio as B; so B = p + W = 17 + 13 = 7. Define Film Studio’s School Daypack as g; R = W + B = 13 + 7 = 20; so g = 12 + R = 12 + 20 = 9. Define Film Studio’s Backpack as w; so w = g + W = 9 + 13 = 22. Define Central High’s Backpack as c; so c = B * w = 7 * 22 = 16. Answer: 16. (2.2)

We emphasize that: • The solution only contain parameters necessary towards calculating the final query parameter.

• The solution follows the correct logical order: i.e. all the parameters used in the calculation must have appeared and been computed beforehand.

• We break computations to binary ops: g = 12 + 13 + 7 g=12+13+7 is broken into g = 12 + R g=12+R and R = 13 + 7 R=13+7 in the above solution. The number of semicolons “;” equals the number of operations . This reduces the arithmetic complexity of the solution, which is not the focus of this paper. 8 8 8 Even GPT-4 can make mistakes on calculating “3 * (4+10) + 12 * (5+6)” without using external calculator.

### 2.3 Difficulty Control

Although deferring all the pseudocode to Appendix D , we summarize below the main randomness used in the data generation process. This includes the random choice of a hierarchical categorization (i.e., the English part); a structure graph (i.e., the instance parameters); a dependency graph; arithmetic computations on the dependency graph; integer numbers (i.e., the 𝖱𝖭𝖦 \mathsf{RNG} ); problem sentence permutation; and the query parameter.

We use two parameters to control data’s difficulty: ip is the number of instance parameters, and op is the number of solution operations; the data’s difficulty is an increasing function over them. We call our dataset iGSM , to reflect the nature that such synthetic dataset can be of infinite size . We use iGSM op ≤ o ​ p , ip ≤ i ​ p \textsf{iGSM}^{\textsf{op}\leq op,\textsf{ip}\leq ip} to denote the data generated with constraint op ≤ o ​ p \textsf{op}\leq op and ip ≤ i ​ p \textsf{ip}\leq ip , and use iGSM op = o ​ p , ip ≤ i ​ p \textsf{iGSM}^{\textsf{op}=op,\textsf{ip}\leq ip} to denote those restricting to op = o ​ p \textsf{op}=op . 9 9 9 We choose op non-uniformly; for instance, we let op = min ⁡ { t 0 , t 1 } \textsf{op}=\min\{t_{0},t_{1}\} for two random draws t 0 , t 1 ∈ [ o ​ p ] t_{0},t_{1}\in[op] . This ensures that the dataset has more easy data — which makes training faster. (See also similar behavior for arithmetics [ 13 ] .)

### 2.4 Train and Test Datasets

We consider two families of datasets. • In the iGSM-med data family we use ip ≤ 20 \textsf{ip}\leq 20 .

The training data is iGSM-med op ≤ 15 = def iGSM op ≤ 15 , ip ≤ 20 \textsf{iGSM-med}^{\textsf{op}\leq 15}\stackrel{{\scriptstyle\mathrm{\scriptscriptstyle def}}}{{=}}\textsf{iGSM}^{\textsf{op}\leq 15,\textsf{ip}\leq 20} . We evaluate the pretrained model both in-distribution, on iGSM-med op ≤ 15 \textsf{iGSM-med}^{\textsf{op}\leq 15} and iGSM-med op = 15 \textsf{iGSM-med}^{\textsf{op}=15} , and out-of-distribution (OOD), on iGSM-med op = o ​ p \textsf{iGSM-med}^{\textsf{op}=op} for o ​ p ∈ { 20 , 21 , 22 , 23 } op\in\{20,21,22,23\} and iGSM-med op = o ​ p , reask \textsf{iGSM-med}^{\textsf{op}=op,\textsf{reask}} . Here, reask denotes first generating a problem from iGSM-med op = o ​ p \textsf{iGSM-med}^{\textsf{op}=op} and then resampling a query parameter. 10 10 10 Due to the topological nature of our data/solution generation process, reask greatly changes the data distribution and the number of operations needed. It provides an excellent OOD sample for evaluation. Details are in Appendix D .

• In the iGSM-hard data family we use ip ≤ 28 \textsf{ip}\leq 28 . The training data is iGSM-hard op ≤ 21 = def iGSM op ≤ 21 , ip ≤ 28 \textsf{iGSM-hard}^{\textsf{op}\leq 21}\stackrel{{\scriptstyle\mathrm{\scriptscriptstyle def}}}{{=}}\textsf{iGSM}^{\textsf{op}\leq 21,\textsf{ip}\leq 28} . We evaluate the pretrained model both in-distribution, on iGSM-hard op ≤ 21 \textsf{iGSM-hard}^{\textsf{op}\leq 21} and iGSM-hard op = 21 \textsf{iGSM-hard}^{\textsf{op}=21} , and OOD on iGSM-hard op = o ​ p \textsf{iGSM-hard}^{\textsf{op}=op} for o ​ p ∈ { 28 , 29 , 30 , 31 , 32 } op\in\{28,29,30,31,32\} and iGSM-hard op = o ​ p , reask \textsf{iGSM-hard}^{\textsf{op}=op,\textsf{reask}} .

Additionally, we use iGSM-med p ​ q \textsf{iGSM-med}_{pq} to indicate placing the question after the problem and iGSM-med q ​ p \textsf{iGSM-med}_{qp} the other way (similarly for iGSM-hard ). The difficulty of iGSM-med is already quite non-trivial to humans (at least not solvable with few-shot learning using GPT-4/4o, see Figure 2 ).

###### Proposition 2.2 .

Ignoring unused parameters, numerics, sentence orderings, English words, a-z and A-Z letter choices, iGSM-med op = 15 \textsf{iGSM-med}^{\textsf{op}=15} still has at least 7 7 billion solution templates , and iGSM-hard op = 21 \textsf{iGSM-hard}^{\textsf{op}=21} has at least 90 90 trillion solution templates . 11 11 11 A solution template is created by replacing all numbers with ‘0’, substituting variables (a-z or A-Z) with letters in their appearance order, and changing parameters to their types (instance or abstract). For instance, “Define Owl Forest’s Elephant as y; so y = 11. Define Parrot Paradise’s Raccoon as t; so t = y = 11.” becomes “Define Inst as a; so a = 0. Define Inst as b; so b = a = 0.” We use birthday paradox to estimate the number of solution templates. If M M randomly generated problems yield distinct templates, it suggests with good probability that the total number of templates exceeds Ω ⁡ ( M 2 ) \Omega(M^{2}) .

No data contamination. A goal in synthetic math data generation is to prevent data contamination in internet-based math datasets, as noted in [ 22 ] . While it may be impossible to certify that models trained on internet data are free from contamination , in our setting, we can certify this : 1. We perform OOD evaluation such as on op ≥ 28 \textsf{op}\geq 28 while providing only op ≤ 21 \textsf{op}\leq 21 training samples.

2. We train with data whose hash value of solution template (see Footnote 11 ) is < 17 ( mod 23 ) <17\pmod{23} , and test with those ≥ 17 \geq 17 . This ensures no template-level overlap between training and testing .

## 3 Result 2-3: Summarize Model’s Behavior Process

We use the GPT2 architecture [ 18 ] but replacing its absolute positional embedding with rotary embedding [ 20 , 7 ] , yet still referring to it as GPT2 for short. 12 12 12 We also tested with Llama architecture (esp. with gated MLP layers) and did not see any benefit of using it. GPT2-rotary performs no worse than Llama/Mistral for knowledge tasks [ 4 ] . We are currently bounded by resources to repeat all experiments in this paper with other architectures that have minor differences from GPT2-rotary. We mostly stick to the 12-layer, 12-head, 768-dim GPT2 (a.k.a. GPT2-small) for experiments, but we explore larger models in Section 6 . We use a context length of 768 / 1024 for pretraining on iGSM-med / iGSM-hard \textsf{iGSM-med}/\textsf{iGSM-hard} and 2048 for evaluation. More details are in Appendix F .

Result 2: accuracy. After sufficient pre-training, we give the model a problem from the test set (without solution) and let it continue to generate (allegedly a solution followed by an answer). Because we have restricted ourselves to a fixed solution format, language models can learn the format easily, allowing us to write a solution parser to check if the solution is fully correct. 13 13 13 We check not only the correctness of the final answer 0..22 but also the calculations and parameter dependencies. Language models can learn very complex syntactics, see [ 1 ] and the references therein. Result 2 . Figure 3 shows that GPT2 performs well when pretrained using iGSM-med or iGSM-hard data, even when evaluated out-of-distribution on harder (i.e., larger op ) math problems. Thus, the model can truly learn some reasoning skill instead of memorizing solution templates. 14 14 14 Llama (of the same model size) gives similar performance, but we refrain from repeating all the experiments with another model. We are not interested in small model differences in this theoretical study; instead, we care more about the general behavior of (autoregressive) language models. This could be reminiscent of language models’ length generalization capability on arithmetic computations [ 23 , 13 ] ; however, in our case, op captures the “reasoning length” in grade-school math, and our model has never seen any training example of the same length as in test time. 15 15 15 Some others such as Anil et al. [6] start with a transformer pre-trained on internet data; while the transformer may not have seen the same task during training, it’s possible that the model has seen other tasks with the same (or even longer) length and learned to transfer from there.

Such accuracies also indicate that our iGSM data families are indeed good for pretraining purpose, allowing us to investigate how LLMs can solve grade-school math problems.

Result 3: solution redundancy. We examine whether GPT2 achieves high accuracy by • brute-forcedly computing all the parameters during generation (a “level-0” reasoning skill), or

• computing only necessary parameters to give shortest solutions (a “level-1” reasoning skill).

Recall our iGSM (pretrain) data only contains necessary solution steps (i.e., CoT) to simulate what we see in textbook solutions for math problems. For instance, if a problem describes X =3+2, E =3+X, Y =X+2 and asks for the value of Y, then a shortest solution would be “X =3+2=5 and Y =X+2 =7” without ever computing E.

Result 3 . Figure 4 shows that GPT2 predominantly solves the iGSM problems with a “level-1” reasoning skill, avoiding unnecessary computations, even when evaluated out-of-distribution. This finding is significant as it suggests that, unlike humans who usually rely on “backward reasoning” and a scratch pad to write down necessary parameters by backtracking the dependencies from the question [ 19 ] , the language model can directly generate shortest solutions without using a scratch pad. But, how does it achieve so? We shall investigate in the next section.

## 4 Result 4-5: Discover Model’s Mental Process

To understand how the model learns to solve math problems, we propose studying the following probing tasks, which align closely with human problem-solving strategies: • nece ​ ( A ) \texttt{nece}(A) : if parameter A A is necessary for computing the answer.

• dep ​ ( A , B ) \texttt{dep}(A,B) : if parameter A A (recursively) depends on parameter B B given the problem statement.

• known ​ ( A ) \texttt{known}(A) : if parameter A A has already been computed.

• value ​ ( A ) \texttt{value}(A) : the value of parameter A A (a number between 0-22, or 23 if known ​ ( A ) = false \texttt{known}(A)=\mathrm{false} ).

• can_next ​ ( A ) \texttt{can\_next}(A) : if A A can be computed in the next solution sentence (namely, its predecessors have all been calculated). Note that A A might not be necessary to answer the question.

• nece_next ​ ( A ) \texttt{nece\_next}(A) : if parameter A A satisfies both can_next ​ ( A ) \texttt{can\_next}(A) and nece ​ ( A ) \texttt{nece}(A) .

For a model to generate the shortest solutions, it must identify nece ​ ( A ) \texttt{nece}(A) for all A A ’s in its mental process. This is because whether nece ​ ( A ) \texttt{nece}(A) is true directly corresponds to whether there is a solution sentence to compute A A . However, how early does the model recognize this, and how is it stored? Similarly, does it recognize dependencies between parameters ( dep )? If so, how early is this mental process completed? Moreover, in the middle of solution generation , does the model keep track of each parameter A A ’s value at all times ( value , known )? Does the model mentally know all possible parameters A A that are ready to compute in the next sentence ( can_next )? Or does it only focus on A A that is both ready and necessary ( nece_next )?

This section proposes probing technique to answer all of these questions.

### 4.1 V-Probing: A Nearly-Linear Probing Method

As illustrated in Figure 5 , we conduct probing at the end of the problem description for the dep task, and end of the question description nece task. 16 16 16 If the problem format is qp (question asked before the problem) then we probe nece and dep both after the problem description. For other tasks, we probe them at the end of every solution sentence (including the start of the first solution sentence).

Recall that standard linear probing involves freezing a pretrained language model and checking if a property is linearly encoded at a hidden layer (usually the last layer) for a given token position. This is done by introducing a trainable linear classifier on the hidden states and performing a lightweight finetuning task for this property (see [ 12 ] and references therein).

Our setting is more complex because the properties have one or two conditional variables, A A and B B , described in plain English. To handle this, we truncate the math problems to the probing position and append tokens [START] and [END] around the descriptions of A A (or A , B A,B ). We then probe from the token position of [END] to see if the property is linearly encoded at the last layer.

Unlike standard linear probing, to account for the input change, we introduce a small trainable rank-8 (linear) update on the input embedding layer. We freeze the pretrained language model and finetune both the linear classifier and the rank-8 update for the desired property. We refer to this as V(ariable)-probing and provide details in Appendix B . An illustration of the nece ​ ( A ) \texttt{nece}(A) probing task is shown in Figure 6 .

We compute the V-probing accuracies on a language model pretrained from iGSM and compare them with the V-probing accuracies on a randomly-initialized transformer model. If the former accuracies are significantly higher, we conclude that the probing signals must have (or be very close to having) come from the pretrained weights, rather than the (lightweight) finetuning stage.

### 4.2 Probing Results and Findings

We present our probing results in Figure 7 . The probing accuracies are high for all the tasks, compared to majority guess and random-model probing — except for the very hard OOD cases (i.e., for large op where the model’s generation accuracies fall down to 80% anyways in Figure 3 ),

Result 4: model solves math problems like humans. We make the following observations: • When generating solutions, the model not only remembers which parameters have been computed and which have not ( value , known \texttt{value},\texttt{known} ) but also knows which parameters can be computed next ( can_next , nece_next \texttt{can\_next},\texttt{nece\_next} ). These abilities ensure that the model can solve the given math problem step by step, similar to human problem-solving skills.

• By the end of the problem description, the model already knows the full list of necessary parameters ( nece ). This indicates that the model has learned to plan ahead , identifying necessary parameters before starting to generate the solution. This aligns with human behavior, except that the model plans mentally while humans typically write this down. This further confirms that the model reaches the “level-1” reasoning skill discussed in Section 3 .

###### Remark 4.1 .

The mental process described can be compared to (out-of-context) knowledge manipulation [ 2 ] , which involves retrieving factual knowledge and performing single-step computations (e.g., retrieving two people’s birth dates to determine who was born earlier). Allen-Zhu and Li [2] found that even single-step computations cannot be performed mentally without a substantial number of pretrain samples. In contrast, this paper studies in-context reasoning and demonstrates that the model can execute very complex mental calculations.

Result 5: model learns beyond human reasoning skills. Remarkably, the model learns dep ​ ( A , B ) \texttt{dep}(A,B) and can_next ​ ( A ) \texttt{can\_next}(A) , even for parameters A A not necessary for answering the question, as shown in Figure 7(b) . This differs from human problem-solving, where we typically use backward reasoning from the question to identify necessary parameters, often overlooking unnecessary ones [ 19 ] . In contrast, language models can pre-compute the all-pair dependency graph dep ​ ( A , B ) \texttt{dep}(A,B) mentally even before a question is asked. We consider this a “level-2” reasoning skill that is very different from human behavior or mental processes.

Thus, although this skill is not needed for solving the math problems and although no pretrain data teaches the model to compute “all-pair dependency” — fitting the data only requires computing necessary parameters — the model still discovers it after training. This enables the model to sort relationships among the things it hears, a skill that can be useful for future tasks (via instruction fine-tuning). To our knowledge, this may be the first evidence of a language model acquiring skills beyond those needed for learning its pretrain data; and this may be a preliminary signal of where the G in AGI can come from (generalizing to skills not taught in the pretrain data).

Corollary: the backward thinking process. A key question for AGI success is whether the “backward thinking process” (e.g., “because I want to compute X, but X depends on Y and Y depends on Z, so let me compute Z first”) needs to be explicitly included in the training data. This differs from CoT, where CoT breaks down complex computations into simpler steps, but planning is still required to decide which step to compute first.

Our findings suggest that, at least for grade-school math problems, with abundant data, this backward thinking process can be autonomously learned through language modeling, without needing to be directly included in the training data.

## 5 Result 6: Explain Model’s Mistakes

We further examine the relationship between our probing results and the model’s generated solutions, focusing on two questions: (1) When does the model answer correctly but include unnecessary parameters? (2) What causes incorrect answers? We aim to determine if such erroneous behavior of the model aligns with errors in the model’s mental process (via probing).

For the first question, given the model rarely produces solutions longer than necessary (see Figure 4 ), we turned to out-of-distribution reask data for evaluation. 17 17 17 Recall this re-samples a query after generating the problem, leading to a different set of necessary parameters. On this data, pretrained models produce an average of ∼ 0.5 \sim 0.5 unnecessary parameters per solution even for op = 32 \textsf{op}=32 (see Figure 4 ). We examined if these unnecessary parameters A A were incorrectly predicted as nece ​ ( A ) = true \texttt{nece}(A)=\mathrm{true} in the probing task. Figure 8(a) reveals that this is often indeed the case, thus language models produce solutions with unnecessary steps due to errors in their mental planning phase .

For the second question, we focused on the model’s wrong solutions and their first wrong parameters . (Using synthetic data, we can easily identify such parameters.) Our findings in Figure 8(b) show that the model’s errors mainly stem from incorrectly predicting nece_next ​ ( A ) \texttt{nece\_next}(A) or can_next ​ ( A ) \texttt{can\_next}(A) as true in its internal states when such A A ’s are not ready for computation. 18 18 18 In Figure 8(b) , we focus on these “first wrong parameters” with correct label being can_next ​ ( A ) = false \texttt{can\_next}(A)=\mathrm{false} or nece_next ​ ( A ) = false \texttt{nece\_next}(A)=\mathrm{false} and present the probability that their probing also correctly predicts false \mathrm{false} . Low accuracy indicates that the model “thought” these parameters were ready for computation, but they were not. Result 6 ( Figure 8 ) . Combining these, we conclude: • Many reasoning mistakes made by the language model are systematic, stemming from errors in its mental process , not merely random from the generation process. • Some of the model’s mistakes can be discovered by probing its inner states even before the model opens its mouth (i.e., before it says the first solution step).

We also observe that GPT-4/4o makes similar mistakes by outputting unnecessary parameters or insisting on computing parameters A A with can_next ​ ( A ) = false \texttt{can\_next}(A)=\mathrm{false} (see Appendix G ). This further hints that our findings may be applicable more broadly.

## 6 Result 7-8: Depth vs. Reasoning Length

Our controlled dataset enables a systematic exploration of the relationship between a language model’s depth and its reasoning length.

Recent studies have demonstrated that for knowledge storage and extraction, only model size matters (even for 2-layer transformers) [ 4 ] . Furthermore, both the seminal scaling-law paper by OpenAI [ 14 ] and theoretical studies in deep learning [ 5 ] suggest that model depth/width might have a minimal impact universally. Contrary to these findings, we present evidence that 19 19 19 Math reasoning data only occupies a tiny fraction of pretraining data for language models, thus one might not observe a difference if we only look at the perplexity as in the original scaling law paper [ 14 ] .

Result 7 ( Figure 9 ) . Language model depth is crucial for mathematical reasoning.

Specifically, we experimented with models of depths 4/8/12/16/20 and two sizes (a smaller size 1 and a larger size 2). 20 20 20 GPT2- ℓ \ell - h h represents an ℓ \ell -layer, h h -head, 64 ​ h 64h -dimensional GPT2 model. Size-1 models are GPT2-4-21, GPT2-8-15, GPT2-12-12, GPT2-16-10, GPT2-20-9, with similar parameter counts; size-2 models are GPT2-4-30, GPT2-8-21, GPT2-12-17, GPT2-16-15, GPT2-20-13, approximately twice the size of size-1 models. From Figure 9 , we observe that a 4-layer transformer, even with 1920 hidden dimensions, underperforms on our math datasets. Conversely, deeper but smaller models, such as a 20-layer 576-dim, perform very well. Comparing accuracies vertically reveals a clear correlation between model depth and performance. Thus, we infer that depth is likely essential for reasoning tasks, such as solving grade-school math problems.

Next, we try to reveal “why” this happens. We delved into how depth influences math problem-solving skills through the nece probing task, focusing on necessary parameters at distance t t from the query parameter, for t ∈ { 1 , 2 , … , 8 } t\in\{1,2,\dots,8\} . These parameters all have nece ​ ( A ) = true \texttt{nece}(A)=\mathrm{true} , but we can probe the model to see how correct they are at predicting nece ​ ( A ) \texttt{nece}(A) at different hidden layers.

Figure 10 shows our result. It reveals a correlation between the model’s layer hierarchy, reasoning accuracy, and mental reasoning depth . Shallower layers excel at predicting nece ​ ( A ) \texttt{nece}(A) for parameters A A closer to the query, whereas deeper layers are more accurate and can predict nece ​ ( A ) \texttt{nece}(A) for parameters further from the query. This suggests that the model employs layer-by-layer reasoning during the planning phase to recursively identify all parameters the query depends on, and:

Result 8 ( Figure 10 + 14 ) . The depth of a language model is crucial, likely due to the complexity of its hidden (mental) reasoning processes. A t t -step mental reasoning, such as mentally computing nece ​ ( A ) \texttt{nece}(A) for parameters A A that are a distance t t from the query, may require deeper models for larger t t , assuming all other hyperparameters remain constant.

We make two disclaimers here. First, if the “backward thinking process” is added as CoT to the data (see the end of Section 4.2 ), then deep mental thinking is no longer required, reducing the language model’s depth requirement. However, in practice, many such “thinking processes” may not be included in standard math solutions or languages in general.

Second, the above claim does not imply that “a t t -step mental thinking requires a depth- t t transformer”. It is plausible for a single transformer layer (containing many sub-layers) to implement t > 1 t>1 mental thinking steps, though possibly with reduced accuracy as t t increases. We refrain from providing an exact correlation in this paper, as it heavily depends on the data distribution.

## 7 Conclusion

We use a synthetic setting to demonstrate that language models can learn to solve grade-school math problems through true generalization, rather than relying on data contamination or template memorization. We develop probing techniques to examine the models’ hidden reasoning processes. Our findings reveal that these models can learn math skills aligned with human cognitive processes, as well as “new thinking processes” not present in the training data. Additionally, we propose a method to predict a model’s errors before it begins to solve a problem and to explain why models make mistakes when they occur. Based on this discovery, we write a separate paper to improve language models’ math reasoning accuracy [ 21 ] . We also provide a principled approach to connect the model’s depth to its capable reasoning length. We believe this research opens doors to study the mathematical reasoning skills of language models from a different angle compared to pushing math benchmarks.

One may argue that iGSM may be very different from the pretrain data that modern LLMs use. While this may be true, we are looking into the future. Recall, even GPT-4/4o of today cannot few-shot learn to solve iGSM-med op = 11 \textsf{iGSM-med}^{\textsf{op}=11} (see Figure 2 ). From this perspective, it is reasonable to believe that future versions of LLMs will rely on synthetic math pretrain data to improve their reasoning skills. While one may not directly use iGSM , it is tempting to use existing LLMs (such as Llama-3) to turn iGSM into more natural formats while keeping the logical chains. On the other hand, we have discovered that models trained purely on the iGSM data make similar mistakes compared to GPT-4/4o (see Section 5 and Appendix G ). This further confirms that our findings do connect to practice, regarding the model’s hidden reasoning process.

Finally, Part 2 of this work series focuses on how language models solve grade-school math problems (including Part 2.2 [ 21 ] ). We also cover how language models learn language structures in Part 1 [ 1 ] (in particular, how they mentally perform dynamical programming), and learn world knowledge in Part 3 [ 3 , 2 , 4 ] .

Appendix

## References

[1] Zeyuan Allen-Zhu and Yuanzhi Li. Physics of Language Models: Part 1, Learning Hierarchical Language Structures. ArXiv e-prints , abs/2305.13673, May 2023a. Full version available at http://arxiv.org/abs/2305.13673 .

[2] Zeyuan Allen-Zhu and Yuanzhi Li. Physics of Language Models: Part 3.2, Knowledge Manipulation. ArXiv e-prints , abs/2309.14402, September 2023b. Full version available at http://arxiv.org/abs/2309.14402 .

[3] Zeyuan Allen-Zhu and Yuanzhi Li. Physics of Language Models: Part 3.1, Knowledge Storage and Extraction. In ICML , 2024a. Full version available at http://arxiv.org/abs/2309.14316 .

[4] Zeyuan Allen-Zhu and Yuanzhi Li. Physics of Language Models: Part 3.3, Knowledge Capacity Scaling Laws. ArXiv e-prints , abs/2404.05405, April 2024b. Full version available at http://arxiv.org/abs/2404.05405 .

[5] Zeyuan Allen-Zhu, Yuanzhi Li, and Zhao Song. A convergence theory for deep learning via over-parameterization. In ICML , 2019. Full version available at http://arxiv.org/abs/1811.03962 .

[6] Cem Anil, Yuhuai Wu, Anders Andreassen, Aitor Lewkowycz, Vedant Misra, Vinay Ramasesh, Ambrose Slone, Guy Gur-Ari, Ethan Dyer, and Behnam Neyshabur. Exploring length generalization in large language models. Advances in Neural Information Processing Systems , 35:38546–38556, 2022.

[7] Sid Black, Stella Biderman, Eric Hallahan, Quentin Anthony, Leo Gao, Laurence Golding, Horace He, Connor Leahy, Kyle McDonell, Jason Phang, Michael Pieler, USVSN Sai Prashanth, Shivanshu Purohit, Laria Reynolds, Jonathan Tow, Ben Wang, and Samuel Weinbach. GPT-NeoX-20B: An open-source autoregressive language model. In Proceedings of the ACL Workshop on Challenges & Perspectives in Creating Large Language Models , 2022. URL https://arxiv.org/abs/2204.06745 .

[8] Sébastien Bubeck, Varun Chandrasekaran, Ronen Eldan, Johannes Gehrke, Eric Horvitz, Ece Kamar, Peter Lee, Yin Tat Lee, Yuanzhi Li, Scott Lundberg, et al. Sparks of artificial general intelligence: Early experiments with gpt-4. arXiv preprint arXiv:2303.12712 , 2023.

[9] Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, et al. Training verifiers to solve math word problems. arXiv preprint arXiv:2110.14168 , 2021.

[10] Leo Gao, Stella Biderman, Sid Black, Laurence Golding, Travis Hoppe, Charles Foster, Jason Phang, Horace He, Anish Thite, Noa Nabeshima, et al. The pile: An 800gb dataset of diverse text for language modeling. arXiv preprint arXiv:2101.00027 , 2020.

[11] Suriya Gunasekar, Yi Zhang, Jyoti Aneja, Caio César Teodoro Mendes, Allie Del Giorno, Sivakanth Gopi, Mojan Javaheripi, Piero Kauffmann, Gustavo de Rosa, Olli Saarikivi, et al. Textbooks are all you need. arXiv preprint arXiv:2306.11644 , 2023.

[12] John Hewitt and Christopher D. Manning. A structural probe for finding syntax in word representations. In Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers) , pages 4129–4138, Minneapolis, Minnesota, June 2019. Association for Computational Linguistics. doi: 10.18653/v1/N19-1419 . URL https://aclanthology.org/N19-1419 .

[13] Samy Jelassi, Stéphane d’Ascoli, Carles Domingo-Enrich, Yuhuai Wu, Yuanzhi Li, and François Charton. Length generalization in arithmetic transformers. arXiv preprint arXiv:2306.15400 , 2023.

[14] Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, and Dario Amodei. Scaling laws for neural language models. arXiv preprint arXiv:2001.08361 , 2020.

[15] Yuanzhi Li, Sébastien Bubeck, Ronen Eldan, Allie Del Giorno, Suriya Gunasekar, and Yin Tat Lee. Textbooks are all you need ii: phi-1.5 technical report. arXiv preprint arXiv:2309.05463 , 2023.

[16] Bingbin Liu, Sebastien Bubeck, Ronen Eldan, Janardhan Kulkarni, Yuanzhi Li, Anh Nguyen, Rachel Ward, and Yi Zhang. TinyGSM: achieving > 80 % >80\% on GSM8k with small language models. arXiv preprint arXiv:2312.09241 , 2023.

[17] OpenAI. Gpt-4 technical report, 2023.

[18] Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, Ilya Sutskever, et al. Language models are unsupervised multitask learners. OpenAI blog , 1(8):9, 2019.

[19] Lance J Rips. The psychology of proof: Deductive reasoning in human thinking . Mit Press, 1994.

[20] Jianlin Su, Yu Lu, Shengfeng Pan, Bo Wen, and Yunfeng Liu. Roformer: Enhanced transformer with rotary position embedding, 2021.

[21] Tian Ye, Zicheng Xu, Yuanzhi Li, and Zeyuan Allen-Zhu. Physics of Language Models: Part 2.2, How to Learn From Mistakes on Grade-School Math Problems. arXiv preprint arXiv:xxxx.xxxxx , 2024. to appear.

[22] Hugh Zhang, Jeff Da, Dean Lee, Vaughn Robinson, Catherine Wu, Will Song, Tiffany Zhao, Pranav Raja, Dylan Slack, Qin Lyu, et al. A careful examination of large language model performance on grade school arithmetic. arXiv preprint arXiv:2405.00332 , 2024.

[23] Hattie Zhou, Arwen Bradley, Etai Littwin, Noam Razin, Omid Saremi, Josh Susskind, Samy Bengio, and Preetum Nakkiran. What algorithms can transformers learn? a study in length generalization. arXiv preprint arXiv:2310.16028 , 2023.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .

## Appendix A Result 1 — An Example in iGSM-hard with op = 21 \textsf{op}=21

## Appendix B Results 4-5 — Details on V-probing

Recall that we wish to conduct probing at the end of the problem description for the nece and dep tasks (before the solution for nece ; before the solution or even the question for dep ). For other tasks, we probe at the end of every solution sentence (including the start of the first solution sentence). The goal is to freeze a pretrained language model, then introduce a very small number of additional trainable parameters on top of it, and finetune them for each probing task.

Specifically, we take a pretrained language model, e.g., pretrained from the iGSM-hard training data. We freeze its parameters completely except for adding a trainable rank- r r update on the embedding layer to account for the task change (from next-token prediction to probing). Throughout this paper we use a small value r = 8 r=8 . We feed this network with training data that are the same as iGSM-hard , but truncated at exactly the position we wish to probe. Importantly, we append such inputs with a special starting token [START] along with a parameter name (or two names, if it is the dep ​ ( A , B ) \texttt{dep}(A,B) task). We then extract the hidden states of the last token position at the last transformer layer, and add a trainable linear layer (a.k.a. linear head) to perform classification for one of the six probing tasks.

This probing method is illustrated in Figure 13 . We call it V(ariable)-Probing, because it can take an arbitrary number of variables (i.e., parameters in this paper) to allow us to perform functional probing inside the transformer.

Note, if it were only a trainable linear head such probing would be called linear probing [ 12 ] . Unlike traditional linear probing, we are adding a small low-rank update on the model’s embedding layer. This is arguably the minimum change needed (to account for the task change, for special tokens like [START] [MID] [END] , etc.) in order to perform any non-trivial probing. This is related but different from the nearly-linear probing methods introduced in Allen-Zhu and Li [1] , Allen-Zhu and Li [3] , because they do not support taking variables as probing inputs. 21 21 21 In Allen-Zhu and Li [1] , Allen-Zhu and Li [3] , the authors are interested in probing the model’s behavior via fixed classification tasks (such as a 100-class classification task) given data that are identical or nearly-identical to the pretrain data. In this paper, we are interested in the model’s behavior with respect to given variables (such as parameter names, which can have ∼ 100 ​ k \sim 100k possibilities); and we append such variable names to the input to make the training inputs appear very different from the original pretrain data.

Unbalanced probing tasks. Our probing accuracies for the six tasks were presented in Figure 7 . However, we notice that the dep and nece_next tasks have unbalanced labels — even guessing “all false \mathrm{false} ” would give 83% accuracy for dep ​ ( A , B ) \texttt{dep}(A,B) and 92 % 92\% for nece_next ​ ( A ) \texttt{nece\_next}(A) . For such reason, we also present their probing accuracies restricted to positives/negatives labels separately in Figure 12 .

## Appendix C Result 8 — Additional Figure

## Appendix D Result 1 Details — Math Data Generation

Our math data generation process consists of first generating the structure graph (see Figure 1 and 11 left), which defines the set of parameters we shall use; then generating the dependency graph (see Figure 1 and 11 right), which defines the arithmetic relationship between the parameters; and finally generating the English problem and solution descriptions.

Notations. In this section, to make the description concise, when we say “randomly sampling” in the pseudocode, we mean uniform random unless otherwise noted. Whenever we consider a (directed) graph G G , slightly abusing notation, we write a ∈ G a\in G to indicate that a a is a vertex in G G and ( a → b ) ∈ 𝖦 (a\to b)\in{\mathsf{G}} to indicate that there is an edge from a a to b b in G G .

### D.1 Generate Structure Graph

Recall the structure graph (see Figure 1 and 11 left) describes the set of possible items (nodes) and instance parameter (edges) that we shall rely on to construct our math problem.

We use G 𝗌 G_{\mathsf{s}} to denote such structure graph, and it is generated G 𝗌 = DrawStructure ​ ( e , d , w 0 , w 1 ) G_{\mathsf{s}}=\mathtt{\hyperref@@ii[alg:structure-graph]{DrawStructure}}(e,d,w_{0},w_{1}) from a random distribution defined with hyperparameters e , d , w 0 , w 1 ∈ ℕ e,d,w_{0},w_{1}\in\mathbb{N} . At a high level, we construct G 𝗌 G_{\mathsf{s}} so that it has d d layers, e e edges, and each layer has between w 0 w_{0} and w 1 w_{1} items.

Specifically, suppose l i ∈ { w 0 , w 0 + 1 , … , w 1 } l_{i}\in\{w_{0},w_{0}+1,\dots,w_{1}\} represents the number of items for each layer i i . In this configuration, one must have at least e − = l 2 + ⋯ + l d e^{-}=l_{2}+\cdots+l_{d} edges to ensure the graph is “connected”, and at most e + = l 1 ​ l 2 + ⋯ + l d − 1 ​ l d e^{+}=l_{1}l_{2}+\cdots+l_{d-1}l_{d} edges. Using this formula, we first randomly choose a configuration ( l 1 , … , l d ) (l_{1},\dots,l_{d}) so that e − ≤ e ≤ e + e^{-}\leq e\leq e^{+} for the given parameter e e . Then, after the configuration is chosen, we randomly generate edges accordingly. Details are given in Algorithm 1 .

#### D.1.1 Attach English

As described in Section 2.1 , we have prepared 4 predefined hierarchical categorizations, each of them with 4 total layers of categories: ⬇

In each of the above 16 categories, we have prepared around 100 items (further decomposed into 5 sub-categories). Below is a showcase of them:

Now, given a constructed structure graph G 𝗌 G_{\mathsf{s}} , we first randomly pick one of the four categorizations, then randomly pick d ∈ { 2 , 3 , 4 } d\in\{2,3,4\} consecutive layers of categories, next randomly pick one of the five subcategories, and finally pick l i l_{i} random item names in this subcategory for each layer i i .

At this point, we have constructed G 𝗌 G_{\mathsf{s}} as well as added English names to each of its node, just like Figure 1 and 11 (left).

### D.2 Generate Dependency Graph

A structure graph G 𝗌 G_{\mathsf{s}} defines the set of possible parameters we consider, while a dependency graph defines how these parameters depend on each other. We use an edge a → b a\to b to indicate that parameter b b depends on a a ; there is a special vertex 𝖱𝖭𝖦 \mathsf{RNG} and it can happen that 𝖱𝖭𝖦 → b \mathsf{RNG}\to b . What an abstract parameter depends on is inherited from the structure graph G 𝗌 G_{\mathsf{s}} . For each instance parameter, we shall randomly add edges to indicate what parameters it depends on.

High-level plan. We shall use G 𝖽 G_{\mathsf{d}} to denote the dependency graph, we start from an empty graph and then add vertices/edges incrementally and randomly. Our process is as follows: • Generate a necessary dependency graph G 𝖽 𝗇𝖾𝖼𝖾 G_{\mathsf{d}}^{\mathsf{nece}} which covers all the vertices and nodes that are necessary for the computation of the query parameter. – Generate necessary abstract parameters (and add parameters they depend on); call this graph G 𝖽 𝗇𝖾𝖼𝖾𝟣 G_{\mathsf{d}}^{\mathsf{nece1}} .

– Generate necessary instance parameters and add them to G 𝖽 𝗇𝖾𝖼𝖾𝟣 G_{\mathsf{d}}^{\mathsf{nece1}} ; call this graph G 𝖽 𝗇𝖾𝖼𝖾𝟤 G_{\mathsf{d}}^{\mathsf{nece2}} .

– Generate a topological order for parameters G 𝖽 𝗇𝖾𝖼𝖾𝟤 G_{\mathsf{d}}^{\mathsf{nece2}} and ensure all of them are necessary towards computing the query parameter (which is the last one in this tropologic order). During this process, we shall add additional edges from G 𝖽 𝗇𝖾𝖼𝖾𝟤 G_{\mathsf{d}}^{\mathsf{nece2}} to create G 𝖽 𝗇𝖾𝖼𝖾𝟥 G_{\mathsf{d}}^{\mathsf{nece3}} .

– Generate additional necessary edges and add them to G 𝖽 𝗇𝖾𝖼𝖾𝟥 G_{\mathsf{d}}^{\mathsf{nece3}} ; call this graph G 𝖽 𝗇𝖾𝖼𝖾 G_{\mathsf{d}}^{\mathsf{nece}} .

• Add to G 𝖽 𝗇𝖾𝖼𝖾 G_{\mathsf{d}}^{\mathsf{nece}} all the remaining (unnecessary) parameters and edges to form G 𝖽 G_{\mathsf{d}} .

At a high level, our problem description shall solely depend on G 𝖽 G_{\mathsf{d}} — by describing each instance parameter in it using a sentence, and our solution description shall solely depend on G 𝖽 𝗇𝖾𝖼𝖾 G_{\mathsf{d}}^{\mathsf{nece}} — by describing the computation of each parameter in it using a sentence.

Before we proceed with the construction let us formally introduce:

###### Definition D.1 (operation) .

Given any dependency graph G 𝖽 G_{\mathsf{d}} , • For an (abstract or instance) parameter a ∈ G 𝖽 a\in G_{\mathsf{d}} that has in-degree t ≥ 0 t\geq 0 , we define 𝗈𝗉 G 𝖽 ​ ( a ) = def max ⁡ { 1 , t − 1 } \mathsf{op}_{G_{\mathsf{d}}}(a)\stackrel{{\scriptstyle\mathrm{\scriptscriptstyle def}}}{{=}}\max\{1,t-1\} which is the number of operations needed to compute a a . 22 22 22 For instance, in Figure 1 , a = “Riverview High’s total number of Backpacks” a=\text{``Riverview High's total number of Backpacks''} is equal to i ​ p 1 × a ​ p 1 + i ​ p 2 × a ​ p 2 ip_{1}\times ap_{1}+ip_{2}\times ap_{2} for i ​ p 1 = “Riverview High’s number of Dance Studios” ip_{1}=\textrm{``Riverview High's number of Dance Studios''} , i ​ p 2 = “Riverview High’s number of Film Studios” ip_{2}=\textrm{``Riverview High's number of Film Studios''} , a ​ p 1 = “each Dance Studio’s number of Backpacks” ap_{1}=\textrm{``each Dance Studio's number of Backpacks''} , a ​ p 2 = “each Film Studio’ number of Backpacks” ap_{2}=\textrm{``each Film Studio' number of Backpacks''} , where i ​ p 1 , i ​ p 2 ip_{1},ip_{2} are instance parameters and a ​ p 1 , a ​ p 2 ap_{1},ap_{2} are abstract parameters. In this case, this abstract parameter depends on 4 other parameters, and requires 3 arithmetic operations.

• We use 𝗈𝗉 ⁡ ( G 𝖽 ) = def ∑ a ∈ G 𝖽 ∖ { 𝖱𝖭𝖦 } 𝗈𝗉 G 𝖽 ​ ( a ) \mathsf{op}(G_{\mathsf{d}})\stackrel{{\scriptstyle\mathrm{\scriptscriptstyle def}}}{{=}}\sum_{a\in G_{\mathsf{d}}\setminus\{\mathsf{RNG}\}}\mathsf{op}_{G_{\mathsf{d}}}(a) to denote the total number of (arithmetic) operations needed to compute all the parameters in G 𝖽 G_{\mathsf{d}} .

###### Remark D.2 .

In our final design of G 𝖽 G_{\mathsf{d}} , we shall ensure that each parameter (except the special vertex 𝖱𝖭𝖦 \mathsf{RNG} ) has in-degree at least 1 1 ; however, during the construction process since we add edges incrementally, some (instance) parameter may temporarily have in-degree 0 0 . For notation simplicity, we still say 𝗈𝗉 G 𝖽 ​ ( a ) = max ⁡ { 1 , − 1 } = 1 \mathsf{op}_{G_{\mathsf{d}}}(a)=\max\{1,-1\}=1 in such a case.

Hyperparameters. We use hyperparameters 1 ≤ n ≤ m ≤ s 1\leq n\leq m\leq s to control the difficulty of G 𝖽 G_{\mathsf{d}} . • we shall ensure 𝗈𝗉 ⁡ ( G 𝖽 𝗇𝖾𝖼𝖾𝟣 ) ≤ n \mathsf{op}(G_{\mathsf{d}}^{\mathsf{nece1}})\leq n and is as close as possible to n n ;

• we shall ensure 𝗈𝗉 ⁡ ( G 𝖽 𝗇𝖾𝖼𝖾𝟥 ) = 𝗈𝗉 ⁡ ( G 𝖽 𝗇𝖾𝖼𝖾𝟤 ) ≤ m \mathsf{op}(G_{\mathsf{d}}^{\mathsf{nece3}})=\mathsf{op}(G_{\mathsf{d}}^{\mathsf{nece2}})\leq m and is as close as possible to m m ;

• we shall ensure 𝗈𝗉 ⁡ ( G 𝖽 𝗇𝖾𝖼𝖾 ) = s \mathsf{op}(G_{\mathsf{d}}^{\mathsf{nece}})=s is exact.

In other words, hyperparameter s s controls exactly how many operations are needed to compute the query parameter, which is the primary factor controlling the problem’s difficulty.

#### D.2.1 Construction of G 𝖽 𝗇𝖾𝖼𝖾𝟣 , G 𝖽 𝗇𝖾𝖼𝖾𝟤 G_{\mathsf{d}}^{\mathsf{nece1}},G_{\mathsf{d}}^{\mathsf{nece2}}

Given a structure graph G 𝗌 G_{\mathsf{s}} , recall its edges represent all the instance parameters we shall use. Its abstract parameters are those ones that describe quantities across 1 or multiple layers: for instance in Figure 1 , Central High ’s number of Classrooms is across 1 layer, and Central High ’s number of Backpacks is across 2 layers. We define this number as the difficulty level of abstract parameters.

With this notion, our construction of G 𝖽 𝗇𝖾𝖼𝖾𝟣 G_{\mathsf{d}}^{\mathsf{nece1}} and G 𝖽 𝗇𝖾𝖼𝖾𝟤 G_{\mathsf{d}}^{\mathsf{nece2}} are described together in Algorithm 2 .

At a high level, we try to incrementally and randomly add abstract parameters to G 𝖽 𝗇𝖾𝖼𝖾𝟣 G_{\mathsf{d}}^{\mathsf{nece1}} while maintaining 𝗈𝗉 ⁡ ( G 𝖽 𝗇𝖾𝖼𝖾𝟣 ) ≤ n \mathsf{op}(G_{\mathsf{d}}^{\mathsf{nece1}})\leq n . We cannot make this exact equality because when adding a single abstract parameter requires also (recursively) adding all the other parameters it may depend on. We tried to prioritize adding abstract parameters with higher difficulty levels. Once we finish constructing G 𝖽 𝗇𝖾𝖼𝖾𝟣 G_{\mathsf{d}}^{\mathsf{nece1}} , we randomly add additional instance parameters from G 𝗌 G_{\mathsf{s}} to make it G 𝖽 𝗇𝖾𝖼𝖾𝟤 G_{\mathsf{d}}^{\mathsf{nece2}} .

#### D.2.2 Construction of G 𝖽 𝗇𝖾𝖼𝖾𝟥 G_{\mathsf{d}}^{\mathsf{nece3}}

Our goal next is to select a random 𝚚𝚞𝚎𝚛𝚢 \mathtt{query} parameter in G 𝖽 𝗇𝖾𝖼𝖾𝟤 G_{\mathsf{d}}^{\mathsf{nece2}} and construct a random topological ordering 𝚃𝚘𝚙𝚘 \mathtt{Topo} for all the parameters in G 𝖽 𝗇𝖾𝖼𝖾𝟤 G_{\mathsf{d}}^{\mathsf{nece2}} , so as to ensure that all the parameters are necessary towards the computation of 𝚚𝚞𝚎𝚛𝚢 \mathtt{query} .

We start with 𝚃𝚘𝚙𝚘 = [ 𝚚𝚞𝚎𝚛𝚢 ] \mathtt{Topo}=[\mathtt{query}] and append parameters to its left one by one. During this process, we may also introduce new edges randomly; we start with G 𝖽 𝗇𝖾𝖼𝖾𝟥 = G 𝖽 𝗇𝖾𝖼𝖾𝟤 G_{\mathsf{d}}^{\mathsf{nece3}}=G_{\mathsf{d}}^{\mathsf{nece2}} and add edges incrementally. This process may not always succeed — sometimes the created topological ordering cannot make all the parameters necessary towards the computation of the 𝚚𝚞𝚎𝚛𝚢 \mathtt{query} . If this happens we declare a failure. 23 23 23 The outside pseudocode, which comes later, shall go back to regenerate the structure graph and start again.

We introduce two notions (we use G 𝖽 𝗇𝖾𝖼𝖾𝟥 ∖ 𝚃𝚘𝚙𝚘 G_{\mathsf{d}}^{\mathsf{nece3}}\setminus\mathtt{Topo} to denote the set of vertices in G 𝖽 𝗇𝖾𝖼𝖾𝟥 G_{\mathsf{d}}^{\mathsf{nece3}} that are not in 𝚃𝚘𝚙𝚘 \mathtt{Topo} ): • 𝖭𝖾𝗑𝗍𝟣 G 𝖽 𝗇𝖾𝖼𝖾𝟥 ​ ( 𝚃𝚘𝚙𝚘 ) = def { a ∈ G 𝖽 𝗇𝖾𝖼𝖾𝟥 ∖ 𝚃𝚘𝚙𝚘 ∣ ∃ ( a → b ) ∈ G 𝖽 𝗇𝖾𝖼𝖾𝟥 ​ for some b ∈ 𝚃𝚘𝚙𝚘 } \mathsf{Next1}_{G_{\mathsf{d}}^{\mathsf{nece3}}}(\mathtt{Topo})\stackrel{{\scriptstyle\mathrm{\scriptscriptstyle def}}}{{=}}\big\{a\in G_{\mathsf{d}}^{\mathsf{nece3}}\setminus\mathtt{Topo}\mid\exists(a\to b)\in G_{\mathsf{d}}^{\mathsf{nece3}}\text{ for some $b\in\mathtt{Topo}$}\big\}

Intuitively, if a ∉ 𝖭𝖾𝗑𝗍𝟣 ⁡ ( 𝚃𝚘𝚙𝚘 ) a\not\in\mathsf{Next1}(\mathtt{Topo}) then we cannot immediately append a a to the front of 𝚃𝚘𝚙𝚘 \mathtt{Topo} , because it is not yet necessary towards the computation of 𝚚𝚞𝚎𝚛𝚢 \mathtt{query} .

• 𝖭𝖾𝗑𝗍𝟤 G 𝖽 𝗇𝖾𝖼𝖾𝟥 ​ ( 𝚃𝚘𝚙𝚘 ) = def { a ∈ G 𝖽 𝗇𝖾𝖼𝖾𝟥 ∖ 𝚃𝚘𝚙𝚘 ∣ ∄ ⁡ ( a → b ) ∈ G 𝖽 𝗇𝖾𝖼𝖾𝟥 ​ for any b ∈ G 𝖽 𝗇𝖾𝖼𝖾𝟥 ∖ 𝚃𝚘𝚙𝚘 } \mathsf{Next2}_{G_{\mathsf{d}}^{\mathsf{nece3}}}(\mathtt{Topo})\stackrel{{\scriptstyle\mathrm{\scriptscriptstyle def}}}{{=}}\big\{a\in G_{\mathsf{d}}^{\mathsf{nece3}}\setminus\mathtt{Topo}\mid\nexists(a\to b)\in G_{\mathsf{d}}^{\mathsf{nece3}}\text{ for any $b\in G_{\mathsf{d}}^{\mathsf{nece3}}\setminus\mathtt{Topo}$}\big\} Intuitively, if a ∉ 𝖭𝖾𝗑𝗍𝟤 G 𝖽 𝗇𝖾𝖼𝖾𝟥 ​ ( 𝚃𝚘𝚙𝚘 ) a\not\in\mathsf{Next2}_{G_{\mathsf{d}}^{\mathsf{nece3}}}(\mathtt{Topo}) then we cannot immediately append a a to the front of 𝚃𝚘𝚙𝚘 \mathtt{Topo} , because some other parameter depends on it and is not yet added to 𝚃𝚘𝚙𝚘 \mathtt{Topo} . (Obviously we always have 𝖭𝖾𝗑𝗍𝟤 G 𝖽 𝗇𝖾𝖼𝖾𝟥 ​ ( 𝚃𝚘𝚙𝚘 ) ≠ ∅ \mathsf{Next2}_{G_{\mathsf{d}}^{\mathsf{nece3}}}(\mathtt{Topo})\neq\varnothing unless G 𝖽 𝗇𝖾𝖼𝖾𝟥 ∖ 𝚃𝚘𝚙𝚘 = ∅ G_{\mathsf{d}}^{\mathsf{nece3}}\setminus\mathtt{Topo}=\varnothing so we are done.)

Our generation algorithm is now easy to describe: we keep adding parameters that are in 𝖭𝖾𝗑𝗍𝟣 G 𝖽 𝗇𝖾𝖼𝖾𝟥 ​ ( 𝚃𝚘𝚙𝚘 ) ∩ 𝖭𝖾𝗑𝗍𝟤 G 𝖽 𝗇𝖾𝖼𝖾𝟥 ​ ( 𝚃𝚘𝚙𝚘 ) \mathsf{Next1}_{G_{\mathsf{d}}^{\mathsf{nece3}}}(\mathtt{Topo})\cap\mathsf{Next2}_{G_{\mathsf{d}}^{\mathsf{nece3}}}(\mathtt{Topo}) to the front of 𝚃𝚘𝚙𝚘 \mathtt{Topo} ; and if we get stuck, we introduce new edges to G 𝖽 𝗇𝖾𝖼𝖾𝟥 G_{\mathsf{d}}^{\mathsf{nece3}} (or declare failure). The pseudocode is in Algorithm 3 .

###### Proposition D.3 .

Every instance parameter in G 𝖽 𝗇𝖾𝖼𝖾𝟥 G_{\mathsf{d}}^{\mathsf{nece3}} has in-degree ≤ 1 \leq 1 and thus 𝗈𝗉 ⁡ ( G 𝖽 𝗇𝖾𝖼𝖾𝟥 ) = 𝗈𝗉 ⁡ ( G 𝖽 𝗇𝖾𝖼𝖾𝟤 ) \mathsf{op}(G_{\mathsf{d}}^{\mathsf{nece3}})=\mathsf{op}(G_{\mathsf{d}}^{\mathsf{nece2}}) .

###### Remark D.4 .

In Line 11 and Line 15 of Algorithm 3 , when randomly selecting 𝚙𝚊𝚛𝚊𝚖 1 \mathtt{param}_{1} from a set, instead of doing so uniformly at random, to improve the algorithm’s success rate and the problem’s difficulty level, we introduce a discursion that that biases slightly towards abstract parameters and parameters already in 𝖭𝖾𝗑𝗍𝟣 G 𝖽 𝗇𝖾𝖼𝖾𝟥 ​ ( 𝚃𝚘𝚙𝚘 ) \mathsf{Next1}_{G_{\mathsf{d}}^{\mathsf{nece3}}}(\mathtt{Topo}) . 24 24 24 For those who are interested, abstract parameters are the keys to cause the generation process to fail, because once they become 𝚙𝚊𝚛𝚊𝚖 0 \mathtt{param}_{0} we cannot add edges 𝚙𝚊𝚛𝚊𝚖 1 → 𝚙𝚊𝚛𝚊𝚖 0 \mathtt{param}_{1}\to\mathtt{param}_{0} ; so we had better select them earlier than later (thus put them at the back of 𝚃𝚘𝚙𝚘 \mathtt{Topo} ). On the other hand, for 𝚙𝚊𝚛𝚊𝚖 1 \mathtt{param}_{1} that is already in 𝖭𝖾𝗑𝗍𝟣 G 𝖽 𝗇𝖾𝖼𝖾𝟥 ​ ( 𝚃𝚘𝚙𝚘 ) \mathsf{Next1}_{G_{\mathsf{d}}^{\mathsf{nece3}}}(\mathtt{Topo}) , adding this edge 𝚙𝚊𝚛𝚊𝚖 1 → 𝚙𝚊𝚛𝚊𝚖 0 \mathtt{param}_{1}\to\mathtt{param}_{0} does not further change it; this can help us create a problem whose solution “depth” is higher. Specifically, we first generate g ∼ 𝒩 ⁡ ( 0 , 1 ) g\sim\mathcal{N}(0,1) a random Gaussian, then define 𝚠𝚎𝚒𝚐𝚑𝚝 ⁡ ( a ) = ( 𝟙 a is abstract + 𝟙 a ∈ 𝖭𝖾𝗑𝗍𝟣 G 𝖽 𝗇𝖾𝖼𝖾𝟥 ​ ( 𝚃𝚘𝚙𝚘 ) ) ⋅ | g | \mathtt{weight}(a)=\big(\mathds{1}_{\text{$a$ is abstract}}+\mathds{1}_{a\in\mathsf{Next1}_{G_{\mathsf{d}}^{\mathsf{nece3}}}(\mathtt{Topo})}\big)\cdot|g| , and then sample a a with a probability ∝ e 𝚠𝚎𝚒𝚐𝚑𝚝 ⁡ ( a ) \propto e^{\mathtt{weight}(a)} .

#### D.2.3 Construction of G 𝖽 𝗇𝖾𝖼𝖾 G_{\mathsf{d}}^{\mathsf{nece}}

So far we have created G 𝖽 𝗇𝖾𝖼𝖾𝟥 G_{\mathsf{d}}^{\mathsf{nece3}} and 𝚃𝚘𝚙𝚘 \mathtt{Topo} with the property that every instance parameter in G 𝖽 𝗇𝖾𝖼𝖾𝟥 G_{\mathsf{d}}^{\mathsf{nece3}} has in-degree ≤ 1 \leq 1 . In the next step, we add additional dependency edges to make in-degree to be a random number between 1 1 and 4 4 . We do so by introducing additional edges; and we also introduce an additional vertex 𝖱𝖭𝖦 \mathsf{RNG} . This is our final necessary dependency graph G 𝖽 𝗇𝖾𝖼𝖾 G_{\mathsf{d}}^{\mathsf{nece}} .

Our pseudocode is given in Algorithm 4 . In this step, we shall make sure 𝗈𝗉 ⁡ ( G 𝖽 𝗇𝖾𝖼𝖾 ) = s \mathsf{op}(G_{\mathsf{d}}^{\mathsf{nece}})=s is exact (and declare failure if this is not possible). We do so to precisely control the solution’s difficulty (so that when we evaluate the model, we can choose to evaluate it on problems with a fixed value of s s ).

#### D.2.4 Construction of G 𝖽 G_{\mathsf{d}}

Finally, once we have G 𝖽 𝗇𝖾𝖼𝖾 G_{\mathsf{d}}^{\mathsf{nece}} the necessary dependency graph, we are left to add unnecessary dependency edges (and unnecessary parameters) to form the complete G 𝖽 G_{\mathsf{d}} .

During this process, we shall add all the remaining instance parameters from G 𝗌 G_{\mathsf{s}} into G 𝖽 G_{\mathsf{d}} . When adding each of them, we randomly select the parameters that it shall depend on from all the previously known parameters. 26 26 26 In fact, we do slightly smarter than the most naive approach. If one simply lets each newly added unnecessary parameter to depend, randomly among all the parameters that have already been added to G 𝖽 G_{\mathsf{d}} , then those unnecessary parameters will likely appear towards the end of the topological order. For such reason, we give it 0.5 probability to depend only on a set 𝙸𝚗𝚍𝙻𝚒𝚜𝚝 \mathtt{IndList} , which consists of newly-added, unnecessary parmaeters, that do not depend on G 𝖽 G_{\mathsf{d}} . This way, the unnecessary parameters can also appear to the front of the tropologic order. Note that during this process, we may also introduce new, unnecessary abstract parameters, see the full pseudocode in Algorithm 5 .

###### Remark D.5 .

G 𝖽 G_{\mathsf{d}} consists of all the instance and query parameters in G 𝗌 G_{\mathsf{s}} and the abstract parameters they may (recursively) depend on. There may exist abstract parameters that can be described in G 𝗌 G_{\mathsf{s}} that are not present in G 𝖽 G_{\mathsf{d}} ; but all the instance parameters in G 𝗌 G_{\mathsf{s}} shall be present in G 𝖽 G_{\mathsf{d}} .

### D.3 Generate English: Problem, Question and Solution

At this point, we have constructed a dependency graph G 𝗌 G_{\mathsf{s}} where each instance parameter a ∈ G 𝗌 a\in G_{\mathsf{s}} may depend on between 1 and 4 other vertices (could be abstract, instance parameters or 𝖱𝖭𝖦 \mathsf{RNG} ). We have not yet introduced how a a should be computed, and we do this using a random process 𝙶𝚎𝚗𝚂𝚎𝚗𝚝𝚎𝚗𝚌𝚎 ⁡ ( G 𝖽 , a ) \mathtt{GenSentence}(G_{\mathsf{d}},a) in Algorithm 6 .

Problem description. The problem description simply consists of listing over all instance parameters a ∈ G 𝖽 a\in G_{\mathsf{d}} and call 𝙶𝚎𝚗𝚂𝚎𝚗𝚝𝚎𝚗𝚌𝚎 ⁡ ( G 𝖽 , a ) \mathtt{GenSentence}(G_{\mathsf{d}},a) . We then randomly shuffle the sentences to make the problem hard. Please note the descriptions of abstract parameters are not present in the problem description, because they are inherited from the hierarchical categorization. This is our attempt to make our math data also capture some English meaning, that is the model also needs to learn what items are in each category, and which category is above another category, etc. This is some knowledge that cannot be learned by reading one problem — it must be learned after reading sufficiently many data.

Question description. Our query parameter can be either an instance or abstract parameter, and it is the last element in 𝚃𝚘𝚙𝚘 \mathtt{Topo} . We use a single sentence to ask for its value “How many… does… have?” and we put this question either at the front or at the end of the problem description (depending on the data type).

Solution description. We generate the solution text, by going over all the (instance or abstract) parameters in 𝚃𝚘𝚙𝚘 \mathtt{Topo} in its correct order , and generate a single sentence to compute each parameter. This process is straightforward but notationally heavy, we describe it below by examples.

• Given any instance parameter a ∈ 𝚃𝚘𝚙𝚘 a\in\mathtt{Topo} , suppose for instance a a is 7 times the sum of parameters b , c , d b,c,d . Because of the topological order, the parameters b , c , d b,c,d must have already defined with variable names, denoted as v ​ a ​ r b , v ​ a ​ r c , v ​ a ​ r d var_{b},var_{c},var_{d} . Then we define solution string of a a as “ Define [name of a] as v ​ a ​ r 0 ; v ​ a ​ r 1 = v ​ a ​ r b + v ​ a ​ r c = ⋯ ; v ​ a ​ r 2 = v ​ a ​ r 1 + v ​ a ​ r d = ⋯ ; so v ​ a ​ r 0 = 7 × v ​ a ​ r 2 = ⋯ .” \text{``{Define} [name of a] {as} $var_{0}$; $var_{1}=var_{b}+var_{c}=\cdots$ ; $var_{2}=var_{1}+var_{d}=\cdots$; }\\ \text{{so} $var_{0}=7\times var_{2}=\cdots$.''} Here, the arithmetic computation is decomposed into 2-ary operations step by step separated with semicolons (so 𝗈𝗉 G 𝖽 ​ ( a ) \mathsf{op}_{G_{\mathsf{d}}}(a) is exactly the number of semicolons). The v ​ a ​ r 0 , v ​ a ​ r 1 , v ​ a ​ r 2 var_{0},var_{1},var_{2} are three new (but distinct) random variables and their names are between a-z or A-Z and have 52 possible random choices. The “ ⋯ \cdots ” ignores the math calculations.

• Given an abstract parameter a ∈ 𝚃𝚘𝚙𝚘 a\in\mathtt{Topo} , suppose for instance a = b × c + d × e + f × g a=b\times c+d\times e+f\times g then we similarly define its solution text as “ Define [name of a] as v ​ a ​ r 0 ; v ​ a ​ r 1 = v ​ a ​ r b × v ​ a ​ r c = ⋯ ; v ​ a ​ r 2 = v ​ a ​ r d × v ​ a ​ r e = ⋯ ; “ v ​ a ​ r 3 = v ​ a ​ r f × v ​ a ​ r g = ⋯ ; v ​ a ​ r 4 = v ​ a ​ r 1 + v ​ a ​ r 2 = ⋯ ; so v ​ a ​ r 0 = v ​ a ​ r 3 + v ​ a ​ r 4 = ⋯ .” \text{``{Define} [name of a] {as} $var_{0}$; $var_{1}=var_{b}\times var_{c}=\cdots$ ; $var_{2}=var_{d}\times var_{e}=\cdots$; }\\ \text{``$var_{3}=var_{f}\times var_{g}=\cdots$ ; $var_{4}=var_{1}+var_{2}=\cdots$; }\text{{so} $var_{0}=var_{3}+var_{4}=\cdots$.''} Above, once again v ​ a ​ r 0 , v ​ a ​ r 1 , v ​ a ​ r 2 , v ​ a ​ r 3 , v ​ a ​ r 4 var_{0},var_{1},var_{2},var_{3},var_{4} are new (but distinct) random variable names from a-z or A-Z, and we break down the computation into 2-ary operations.

With the above examples in mind, and combining those with real examples in Figure 11 , it should be very clear how the solution texts are generated.

###### Remark D.6 .

𝗈𝗉 ⁡ ( G 𝖽 𝗇𝖾𝖼𝖾 ) \mathsf{op}(G_{\mathsf{d}}^{\mathsf{nece}}) is equal to the total number of semicolons in the solution text, because it represents the total (and minimum!) number of arithmetic operations needed to compute the final query parameter.

### D.4 Putting Altogether

We put together our data generation process for the structure graph G 𝗌 G_{\mathsf{s}} and the dependency graph G 𝖽 G_{\mathsf{d}} (along with G 𝖽 𝗇𝖾𝖼𝖾 , 𝚃𝚘𝚙𝚘 G_{\mathsf{d}}^{\mathsf{nece}},\mathtt{Topo} ) in Algorithm 7 .

In particular, we use global parameters ip max \textsf{ip}_{\max} and op max \textsf{op}_{\max} : the former controls the maximum number of instance parameters, and the latter controls the maximum number of solution operations. We select n , m , s n,m,s based on op max \textsf{op}_{\max} (to ensure that 1 ≤ n ≤ m ≤ s ≤ op max 1\leq n\leq m\leq s\leq\textsf{op}_{\max} ), and d , e , w 0 , w 1 d,e,w_{0},w_{1} based on ip max \textsf{ip}_{\max} and s s . We also provide a boolean switch f ​ o ​ r ​ c ​ e force and when 𝖿𝗈𝗋𝖼𝖾 = true \mathsf{force}=\mathrm{true} , we shall force s = op max s=\textsf{op}_{\max} so that the generated math problem will have its solution to be of exactly op max \textsf{op}_{\max} operations.

We define datasets • iGSM op ≤ op max , ip ≤ ip max \textsf{iGSM}^{\textsf{op}\leq\textsf{op}_{\max},\textsf{ip}\leq\textsf{ip}_{\max}} as the process of invoking DrawAll ​ ( op max , ip max , 𝖿𝗈𝗋𝖼𝖾 = false ) \mathtt{\hyperref@@ii[alg:dependency-graph]{DrawAll}}(\textsf{op}_{\max},\textsf{ip}_{\max},\mathsf{force}=\mathrm{false}) .

• iGSM op = op max , ip ≤ ip max \textsf{iGSM}^{\textsf{op}=\textsf{op}_{\max},\textsf{ip}\leq\textsf{ip}_{\max}} as the process of invoking DrawAll ​ ( op max , ip max , 𝖿𝗈𝗋𝖼𝖾 = true ) \mathtt{\hyperref@@ii[alg:dependency-graph]{DrawAll}}(\textsf{op}_{\max},\textsf{ip}_{\max},\mathsf{force}=\mathrm{true}) .

Using this language: • The training data iGSM-med is iGSM op ≤ 15 , ip ≤ 20 \textsf{iGSM}^{\textsf{op}\leq 15,\textsf{ip}\leq 20} ;

• The eval data of iGSM-med additionally includes iGSM op = o ​ p , ip ≤ 20 \textsf{iGSM}^{\textsf{op}=op,\textsf{ip}\leq 20} for o ​ p ∈ { 15 , 20 , 21 , 22 , 23 } op\in\{15,20,21,22,23\} ;

• The training data iGSM-hard is iGSM op ≤ 21 , ip ≤ 28 \textsf{iGSM}^{\textsf{op}\leq 21,\textsf{ip}\leq 28} ;

• The eval data of iGSM-hard additionally includes iGSM op = o ​ p , ip ≤ 28 \textsf{iGSM}^{\textsf{op}=op,\textsf{ip}\leq 28} for o ​ p ∈ { 21 , 28 , 29 , 30 , 31 , 32 } op\in\{21,28,29,30,31,32\} .

###### Remark D.7 .

During training (regardless of pretrain or finetune for probing tasks), we only use those data whose hash value of their solution template (see Footnote 11 ) is < 17 ( mod 23 ) <17\pmod{23} , and during evaluation we only use those whose hash value is ≥ 17 ( mod 23 ) \geq 17\pmod{23} . This ensures a strict separation between train and test data (even in terms of their solution templates).

###### Remark D.8 .

In Algorithm 7 , we chose s = min ⁡ { t 0 , t 1 } s=\min\{t_{0},t_{1}\} , where t 0 t_{0} and t 1 t_{1} are two random integers between 1 1 and op max \textsf{op}_{\max} . This choice encourages more easier math problems in the pretrain data, which we found improves the model’s learning.

## Appendix E Data Details: Probing Data Preparation

We describe here how we prepare the probing data. We generate math data according to Appendix D .

For each problem and each probing task (such as nece ​ ( A ) \texttt{nece}(A) , dep ​ ( A , B ) \texttt{dep}(A,B) , etc), we need to specify two things: at which position to probe and what parameters A A (or A , B A,B ) to probe. • For nece and dep , the probing always takes place at the end of the problem (and question) description, so there is no choice to be made; for value , can_next , nece_next tasks, the probing can take place at the end of each sentence in the solution for (including the beginning of the first solution sentence), and we uniformly at random make such choices.

• Each parameter A A (or B B ) can be uniformly at random chosen from the set of all (instance or abstract) parameters in our dependency graph G 𝖽 G_{\mathsf{d}} (with the only requirement that A ≠ B A\neq B ).

In the end, we make sure for each problem and each probing task, we make at most 10 such random choices (over the position and the choice of parameters) and sample without replacement.

Just like in the pretrain data, we prepare our probing data so that only problems with hash values of their solution template (see Footnote 11 ) where the hash < 17 ( mod 23 ) <17\pmod{23} are included in the training set, and the rest are used for testing.

## Appendix F Experiment Details

Model. We use the GPT2 architecture [ 18 ] , replacing its absolute positional embedding with modern rotary positional embedding [ 20 , 7 ] , still referred to as GPT2 for short. (We also played with the Llama architecture (especially with gated MLP layers) aand did not see any benefit of using it. This GPT2 performs comparably to Llama/Mistral at least for knowledge tasks [ 4 ] .)

Let GPT2- ℓ \ell - h h denote an ℓ \ell -layer, h h -head, 64 ​ h 64h -dim GPT2 model. We primarily use GPT2-12-12 (a.k.a. GPT2-small) in this paper, but in Section 6 we explore larger models with different widths and depths. Our size-1 models are GPT2-4-21, GPT2-8-15, GPT2-12-12, GPT2-16-10, GPT2-20-9, roughly the same size as GPT2-small. Our size-2 models are GPT2-4-30, GPT2-8-21, GPT2-12-17, GPT2-16-15, GPT2-20-13, roughly twice the size of GPT2-small. We use a context length of 768/1024 for language model pretraining on iGSM-med / iGSM-hard \textsf{iGSM-med}/\textsf{iGSM-hard} and a context length of 2048 for evaluation.

Data size. For both pretraining and finetuning, we did not limit the amount of training data; we generated new data on-the-fly. We do not explore sample complexity in this paper, such as the number of math problems needed to achieve a certain level of accuracy, as it would complicate the main message of this paper.

### F.1 Pretrain Experiment Details

Pretrain parameters. We used the AdamW optimizer with mixed-precision fp16, β = ( 0.9 , 0.98 ) \beta=(0.9,0.98) , cosine learning rate decay (down to 0.01x of peak learning rate in the end), and 1000 steps of linear ramp-up. We used a mixture of V100/A100 GPUs, but the GPU specifications are not relevant here. 27 27 27 A 128-GPU job with batch size 1 each would be identical to a 32-GPU job with batch size 4 each. For all of our pretrain experiments: • On the iGSM-med datasets, we used a (peak) learning rate 0.002 0.002 , weight decay of 0.05 0.05 , batch size of 512, context length of 768, and trained for 100,000 100,000 steps.

• On the iGSM-hard datasets, we used a (peak) learning rate 0.002 0.002 , weight decay of 0.03 0.03 , batch size of 256, context length of 1024, and trained for 200,000 200,000 steps.

Our pretrain data is constructed by randomly generating math problems (and solutions), concatenating them together, and truncating them (in the right) to fit within the 768 or 1024-sized context window. If a problem is longer than the context window size, we discard it (this happens very rarely).

Test-time parameters. When evaluating on test data, we use context length 2048 for both iGSM-med and iGSM-hard . We use either beam=1 and dosample=False (greedy) or beam=4 and dosample=True (beam-search multinomial sampling) to present test accuracies. We discover it is better to keep dosample=False while beam=1 and dosample=True while beam=4 . We also tried larger beam sizes and found no further improvements.

Accuracy statistics. Our main accuracies are presented in Figure 3 , where each entry is averaged over 4096 math problems of that type. Our accuracies are not simply from comparing the answer integers (between 0 and 22); instead we have written a parser to make sure the model’s intermediate solution steps are fully-correct.

For the “redundancy” experiment Figure 4 , we tested each model again with 4096 math problems in each case and presented the results among fully-correct solutions. For this figure, we present beam=1 for cleanness and the results for beam=4 are almost completely identical.

For the “depth matters” experiment Figure 9 , because we care about the (relatively small) accuracy differences across models, we pretrain using two different random seeds, and evaluate with both beam=1/4 ; we then present the best accuracies in each entry with respect to the 2 seeds and 2 beam choices. The accuracies are again over 4096 math problems.

### F.2 V-probing

Our V-probing was first introduced in Section 4.1 with more details given in Section B . It is a fine-tuning process upon the pretrained language model, with an additional linear head on the output layer, and a small rank- r r update on the input (embedding) layer. The pretrained model is freezed, and only this linear head and the rank- r r update are trainable parameters during the fine-tuning.

Recall we use r = 8 r=8 in this paper (in contrast, the hidden dimension of GPT-12-12 is 768). This small value of r r ensures if probing accuracy is high, it mostly comes from the pretrained model and not the additional trainable parameters.

For V-probing, we use the same configurations as pretrain, except that:

• For V-probing on the iGSM-med datasets, we used a learning rate of 0.002 0.002 (with no ramp-up, linear decay down to 0), weight decay of 0.01 0.01 , batch size of 256, and trained for 100,000 100,000 steps.

• For V-probing on the iGSM-hard datasets, we used a learning rate of 0.002 0.002 (with no ramp-up, linear decay down to 0), weight decay of 0.01 0.01 , batch size of 128, and trained for 100,000 100,000 steps.

V-probing statistics. In Figure 7(a) , Figure 7(b) , Figure 12 , Figure 8(a) , and Figure 8(b) , we tested at least 4096 random problem-parameter pairs in each cell . In Figure 8(a) and Figure 8(b) , when evaluating probing results on GPT-2 model’s generated correct or wrong solutions, we used beam=1 and dosample=False (greedy) for generation. (Results are similar for beam=4 .)

In our layer-wise nece ​ ( A ) \texttt{nece}(A) probing experiments ( Figure 10 and Figure 14 ), we tested at least 73728 random problem-parameter pairs in each case and then divided the results into bins based on the parameter A A ’s distances to the queries.

## Appendix G Failure Examples on GPT-4 / GPT-4o

In Figure 2 , we conduct few-shot experiments using the latest versions of GPT-4 turbo (2024-04-09) and GPT-4o (2024-05-13) models to evaluate their accuracies on our iGSM-med p ​ q \textsf{iGSM-med}_{pq} dataset, with respect to different op ∈ { 2 , 3 , … , 20 } \textsf{op}\in\{2,3,\dots,20\} .

To ensure meaningful evaluation: • We replaced mod 23 \bmod{23} with mod 5 \bmod{5} to ensure that any errors are not due to arithmetic mistakes. We also provided a few arithmetic computation examples.

• We minimized English diversity to ensure that any errors are not due to misunderstanding the problem description. Specifically, – We fixed a simple categorization ( School , Classroom , Backpack , Stationerys ) (\textsf{School},\textsf{Classroom},\textsf{Backpack},\textsf{Stationerys}) , with only four items in each category.

– We provided an English background paragraph to fully describe the structure graph (i.e., which item has which subitem), as well as the number of items in each category. The math problem is preceded by this background paragraph.

• We provided five-shot problem/solution examples to ensure that GPT-4 understands how to solve such math problems step by step.

We did not verify each step of GPT-4’s solution but checked if the final output number (between 0 and 4) matched the correct answer. The accuracy results are presented in Figure 2 . It shows that the GPT-4o model is almost randomly guessing for op ≥ 11 \textsf{op}\geq 11 , and GPT-4 turbo for op ≥ 9 \textsf{op}\geq 9 .

Furthermore, Figure 15 shows that when the GPT-4/4o models fail to answer the math problems, it is mostly not due to format errors or misunderstanding of the problem. Instead, just like what we discovered in Section 5 , GPT-4/4o fail also because they compute unnecessary parameters (i.e., nece ​ ( A ) = false \texttt{nece}(A)=\mathrm{false} ) or compute parameters that are not yet ready to be computed (i.e., can_next ​ ( A ) = false \texttt{can\_next}(A)=\mathrm{false} ). This further confirms that our findings do connect to practice, regarding the model’s hidden reasoning process.
