# Key ML papers from result.json

Source: Telegram "Saved Messages" export (9,375 messages, 2017–2026).
Found 172 unique arXiv papers plus roughly 50 works outside arXiv
(OpenReview, ACL Anthology, Nature/Science/Cell, bioRxiv, lab publications).
The full list with save dates is in `arxiv_dump.txt`; titles and authors are in
`papers_titles.json` and `extra_titles.json`. The "Addendum" sections at the bottom
were compiled after a separate pass over posts from 43 ML channels.

## Canonical works (must-read classics)

| Year | Paper | Link |
| --- | --- | --- |
| 2015 | Deep Reinforcement Learning with Double Q-learning | https://arxiv.org/abs/1509.06461 |
| 2015 | Prioritized Experience Replay | https://arxiv.org/abs/1511.05952 |
| 2015 | Dueling Network Architectures for Deep RL | https://arxiv.org/abs/1511.06581 |
| 2017 | A Distributional Perspective on RL (C51) | https://arxiv.org/abs/1707.06887 |
| 2017 | Rainbow: Combining Improvements in Deep RL | https://arxiv.org/abs/1710.02298 |
| 2017 | Searching for Activation Functions (Swish) | https://arxiv.org/abs/1710.05941 |
| 2018 | Soft Actor-Critic (SAC) | https://arxiv.org/abs/1801.01290 |
| 2018 | Addressing Function Approximation Error in Actor-Critic (TD3) | https://arxiv.org/abs/1802.09477 |
| 2018 | The Lottery Ticket Hypothesis | https://arxiv.org/abs/1803.03635 |
| 2018 | BERT | https://arxiv.org/abs/1810.04805 |
| 2020 | Scaling Laws for Neural Language Models | https://arxiv.org/abs/2001.08361 |
| 2020 | GLU Variants Improve Transformer (SwiGLU) | https://arxiv.org/abs/2002.05202 |
| 2020 | SwAV: Unsupervised Learning by Contrasting Cluster Assignments | https://arxiv.org/abs/2006.09882 |
| 2021 | DINO: Emerging Properties in Self-Supervised ViT | https://arxiv.org/abs/2104.14294 |
| 2023 | LLaMA: Open and Efficient Foundation Language Models | https://arxiv.org/abs/2302.13971 |
| 2023 | I-JEPA (Self-Supervised Learning from Images with JEPA) | https://arxiv.org/abs/2301.08243 |
| 2023 | DINOv2 | https://arxiv.org/abs/2304.07193 |
| 2023 | Are Emergent Abilities of LLMs a Mirage? (NeurIPS best paper) | https://arxiv.org/abs/2304.15004 |

## Reinforcement learning

- Deep Neuroevolution: GAs as an alternative to training RL networks — https://arxiv.org/abs/1712.06567
- Benchmarking Batch Deep RL Algorithms — https://arxiv.org/abs/1910.01708
- First return, then explore (Go-Explore, Nature) — https://arxiv.org/abs/2004.12919
- Offline RL: Tutorial, Review, and Perspectives — https://arxiv.org/abs/2005.01643
- Revisiting Rainbow — https://arxiv.org/abs/2011.14826
- A Minimalist Approach to Offline RL (TD3+BC) — https://arxiv.org/abs/2106.06860
- The Primacy Bias in Deep RL — https://arxiv.org/abs/2205.07802
- For SALE: State-Action Representation Learning — https://arxiv.org/abs/2306.02451
- BBF: Bigger, Better, Faster — Human-level Atari with human-level efficiency — https://arxiv.org/abs/2305.19452
- Beyond The Rainbow: High Performance Deep RL on a Desktop PC — https://arxiv.org/abs/2411.03820
- Towards General-Purpose Model-Free RL (MR.Q) — https://arxiv.org/abs/2501.16142
- In-Context RL for Variable Action Spaces — https://arxiv.org/abs/2312.13327
- Metalearning Continual Learning Algorithms — https://arxiv.org/abs/2312.00276
- DreamerV3: Mastering Diverse Domains through World Models — https://arxiv.org/abs/2301.04104
- The Alberta Plan for AI Research (Sutton) — https://arxiv.org/abs/2208.11173
- CDE: Curiosity-Driven Exploration for RL in LLMs — https://arxiv.org/abs/2509.09675

## LLMs: architectures, context, training

- Memorizing Transformers — https://arxiv.org/abs/2203.08913
- Hyena Hierarchy — https://arxiv.org/abs/2302.10866
- Unlimiformer: Long-Range Transformers with Unlimited Length Input — https://arxiv.org/abs/2305.01625
- Infini-attention: Leave No Context Behind — https://arxiv.org/abs/2404.07143
- TransformerFAM: Feedback attention is working memory — https://arxiv.org/abs/2404.09173
- xLSTM: Extended Long Short-Term Memory — https://arxiv.org/abs/2405.04517
- ModernBERT — https://arxiv.org/abs/2412.13663
- Kosmos-1: Language Is Not All You Need — https://arxiv.org/abs/2302.14045
- Florence-2 — https://arxiv.org/abs/2311.06242
- Scaling MLPs: A Tale of Inductive Bias — https://arxiv.org/abs/2306.13575
- Neural Networks and the Chomsky Hierarchy — https://arxiv.org/abs/2207.02098

## Reasoning and the "physics" of language models

- Physics of Language Models (series): 1 — https://arxiv.org/abs/2305.13673 · 2.1 — https://arxiv.org/abs/2407.20311 · 3.1 — https://arxiv.org/abs/2309.14316 · 3.2 — https://arxiv.org/abs/2309.14402 · 3.3 (Knowledge Capacity Scaling Laws) — https://arxiv.org/abs/2404.05405
- The Reversal Curse — https://arxiv.org/abs/2309.12288
- Multimodal Chain-of-Thought Reasoning — https://arxiv.org/abs/2302.00923
- Coconut: Reasoning in a Continuous Latent Space — https://arxiv.org/abs/2412.06769
- SIM-CoT: Supervised Implicit Chain-of-Thought — https://arxiv.org/abs/2509.20317
- From Explicit CoT to Implicit CoT — https://arxiv.org/abs/2405.14838
- Arithmetic Without Algorithms: Bag of Heuristics — https://arxiv.org/abs/2410.21272
- LLMs Can't Plan, But Can Help Planning (LLM-Modulo) — https://arxiv.org/abs/2402.01817
- Competitive Programming with Large Reasoning Models (OpenAI o-series) — https://arxiv.org/abs/2502.06807
- Scaling of Search and Learning: A Roadmap to Reproduce o1 — https://arxiv.org/abs/2412.14135
- How do language models learn facts? (DeepMind) — https://arxiv.org/abs/2503.21676
- How Do LLMs Acquire Factual Knowledge During Pretraining? — https://arxiv.org/abs/2406.11813
- Knowledge Mechanisms in LLMs: A Survey — https://arxiv.org/abs/2407.15017
- The Truth is in There: Layer-Selective Rank Reduction (LASER) — https://arxiv.org/abs/2312.13558
- Dissociating language and thought in LLMs — https://arxiv.org/abs/2301.06627
- Emergent Analogical Reasoning in LLMs — https://arxiv.org/abs/2212.09196
- Emergent Capabilities Arise Randomly from Sparse Attention Patterns — https://arxiv.org/abs/2606.25010
- Transcendence: Generative Models Can Outperform The Experts That Train Them — https://arxiv.org/abs/2406.11741
- Evaluating the World Model Implicit in a Generative Model — https://arxiv.org/abs/2406.03689

## Data, training, optimization

- Cyclical Learning Rates — https://arxiv.org/abs/1506.01186
- Super-Convergence (one-cycle) — https://arxiv.org/abs/1708.07120
- Lion: Symbolic Discovery of Optimization Algorithms — https://arxiv.org/abs/2302.06675
- The Road Less Scheduled (Schedule-Free) — https://arxiv.org/abs/2405.15682
- The AdEMAMix Optimizer — https://arxiv.org/abs/2409.03137
- Learned optimizers: training an optimizer with itself — https://arxiv.org/abs/2009.11243 · https://arxiv.org/abs/2002.11887
- Grokfast: Accelerated Grokking — https://arxiv.org/abs/2405.20233
- How much do language models memorize? — https://arxiv.org/abs/2505.24832
- Emergent properties with repeated examples (FAIR) — https://arxiv.org/abs/2410.07041
- Perplexed by Perplexity: Data Pruning With Small Reference Models — https://arxiv.org/abs/2405.20541
- gzip Predicts Data-dependent Scaling Laws — https://arxiv.org/abs/2405.16684
- Scaling Laws for Reward Model Overoptimization — https://arxiv.org/abs/2210.10760
- Learning in High Dimension Always Amounts to Extrapolation — https://arxiv.org/abs/2110.09485
- Learning Vision from Models Rivals Learning Vision from Data — https://arxiv.org/abs/2312.17742

## Self-supervised learning and vision

- A Cookbook of Self-Supervised Learning — https://arxiv.org/abs/2304.12210
- To Compress or Not to Compress: SSL and Information Theory — https://arxiv.org/abs/2304.09355
- iBOT: Image BERT Pre-Training with Online Tokenizer — https://arxiv.org/abs/2111.07832
- BEiT-3: Image as a Foreign Language — https://arxiv.org/abs/2208.10442
- VISReg: Variance-Invariance-Sketching Regularization for JEPA — https://arxiv.org/abs/2606.02572
- Latent Consistency Models — https://arxiv.org/abs/2310.04378
- Tune-A-Video — https://arxiv.org/abs/2212.11565
- Emu: Enhancing Image Generation with Photogenic Needles — https://arxiv.org/abs/2309.15807
- ImageReward — https://arxiv.org/abs/2304.05977
- Towards Universal Fake Image Detectors — https://arxiv.org/abs/2302.10174

## Retrieval, embeddings, benchmarks

- BIG-bench: Beyond the Imitation Game — https://arxiv.org/abs/2206.04615
- Large Dual Encoders Are Generalizable Retrievers (GTR) — https://arxiv.org/abs/2112.07899
- INSTRUCTOR: One Embedder, Any Task — https://arxiv.org/abs/2212.09741
- DSP: Demonstrate-Search-Predict (precursor of DSPy) — https://arxiv.org/abs/2212.14024
- Gist Tokens: Learning to Compress Prompts — https://arxiv.org/abs/2304.08467
- Promptbreeder: Self-Referential Self-Improvement — https://arxiv.org/abs/2309.16797
- Rainbow Teaming — https://arxiv.org/abs/2402.16822
- Medprompt: Can Generalist Foundation Models Outcompete Special-Purpose Tuning? — https://arxiv.org/abs/2311.16452
- StrategyQA: Did Aristotle Use a Laptop? — https://arxiv.org/abs/2101.02235
- Artifacts or Abduction: multiple-choice questions without the question — https://arxiv.org/abs/2402.12483
- MLE-bench: Evaluating ML Agents on ML Engineering — https://arxiv.org/abs/2410.07095
- CEO-Bench: Can Agents Play the Long Game? — https://arxiv.org/abs/2606.18543
- People cannot distinguish GPT-4 from a human in a Turing test — https://arxiv.org/abs/2405.08007

## Agents, open-endedness, AGI

- Open-Endedness is Essential for Artificial Superhuman Intelligence — https://arxiv.org/abs/2406.04268
- A Definition of Open-Ended Learning Problems — https://arxiv.org/abs/2311.00344
- Levels of AGI (DeepMind) — https://arxiv.org/abs/2311.02462
- AlphaGo Moment for Model Architecture Discovery — https://arxiv.org/abs/2507.18074
- Self-Improvements in Modern Agentic Systems: A Survey (Schmidhuber) — https://arxiv.org/abs/2607.13104
- What Does It Take to Be a Good AI Research Agent? — https://arxiv.org/abs/2511.15593
- Harnessing Agentic Evolution — https://arxiv.org/abs/2605.13821 · Hyperagents — https://arxiv.org/abs/2603.19461
- Competition and Attraction Improve Model Fusion (Sakana AI) — https://arxiv.org/abs/2508.16204
- Learning Formal Mathematics From Intrinsic Motivation — https://arxiv.org/abs/2407.00695

## AI safety and consciousness

- Optimal Policies Tend to Seek Power — https://arxiv.org/abs/1912.01683
- Parametrically Retargetable Decision-Makers Tend To Seek Power — https://arxiv.org/abs/2206.13477
- Is Power-Seeking AI an Existential Risk? — https://arxiv.org/abs/2206.13353
- Power-seeking can be probable and predictive for trained agents — https://arxiv.org/abs/2304.06528
- Consciousness in AI: Insights from the Science of Consciousness — https://arxiv.org/abs/2308.08708
- Could a Large Language Model be Conscious? (Chalmers) — https://arxiv.org/abs/2303.07103
- Palatable Conceptions of Disembodied Being (Shanahan) — https://arxiv.org/abs/2503.16348

## Time series

- Chronos: Learning the Language of Time Series — https://arxiv.org/abs/2403.07815
- TimesFM: A decoder-only foundation model for time-series forecasting — https://arxiv.org/abs/2310.10688
- Lag-Llama — https://arxiv.org/abs/2310.08278
- Time-LLM — https://arxiv.org/abs/2310.01728
- LLMTime: LLMs Are Zero-Shot Time Series Forecasters — https://arxiv.org/abs/2310.07820
- Informer — https://arxiv.org/abs/2012.07436
- PromptCast — https://arxiv.org/abs/2210.08964
- Deep learning for time series classification: a review — https://arxiv.org/abs/1809.04356
- Time Series Classification from Scratch (strong baseline) — https://arxiv.org/abs/1611.06455
- Survey of Deep Learning and Foundation Models for TS Forecasting — https://arxiv.org/abs/2401.13912

## NeuroAI

- Toward Next-Generation AI: Catalyzing the NeuroAI Revolution — https://arxiv.org/abs/2210.08340
- This is how the Neocortex Learns (O'Reilly) — https://arxiv.org/abs/2606.08720
- Attractor and integrator networks in the brain — https://arxiv.org/abs/2112.03978
- From Tokens to Thoughts: How LLMs and Humans Trade Compression for Meaning — https://arxiv.org/abs/2505.17117

## Addendum: works without a direct arXiv link

Found on a second pass over posts from the listed channels — they were cited
via OpenReview, HuggingFace Papers, ACL Anthology, DOI, or lab blogs.

### The big ones that were least worth missing

- **A Path Towards Autonomous Machine Intelligence** (LeCun, 2022) — the position paper
  on JEPA and world models, published only on OpenReview:
  https://openreview.net/forum?id=BZ5a1r-kVsf
- **Loss of plasticity in deep continual learning** (Sutton et al., Nature 2024) —
  https://doi.org/10.1038/s41586-024-07711-7
- **Weak-to-strong generalization** (OpenAI SuperAlignment, Sutskever among the authors) —
  https://openai.com/research/weak-to-strong-generalization
- **Robust agents learn causal world models** (ICLR 2024 best paper) —
  https://openreview.net/forum?id=pOoKI3ouv1
- **1000 Layer Networks for Self-Supervised RL** (NeurIPS 2025 Best Paper) —
  https://openreview.net/forum?id=s0JVsx3bx1
- **Language is primarily a tool for communication rather than thought**
  (Fedorenko et al., Nature 2024) — https://doi.org/10.1038/s41586-024-07522-w
- **Nested Learning** (Google, NeurIPS 2025) — nested levels of optimization against
  catastrophic forgetting; the export contains only the Data Secrets summary of 2025-11-08
- **Tracing thoughts of a language model / Circuit tracing** (Anthropic, 2025) —
  https://www.anthropic.com/research/tracing-thoughts-language-model
- **Mapping the mind of a large language model** (Anthropic, SAE interpretability) —
  https://www.anthropic.com/news/mapping-mind-language-model

### New arXiv papers (arrived via HuggingFace Papers)

- Your Transformer is Secretly Linear (ACL 2024, AIRI) — https://arxiv.org/abs/2405.12250
- rStar-Math: Small LLMs Can Master Math Reasoning — https://arxiv.org/abs/2501.04519
- The GAN is dead; long live the GAN! (R3GAN) — https://arxiv.org/abs/2501.05441
- Deep Learning Interviews (problem collection) — https://arxiv.org/abs/2201.00650

### OpenReview

- Sample-Efficient RL by Breaking the Replay Ratio Barrier (ICLR 2023 oral, precursor of BBF)
  — https://openreview.net/forum?id=OpC-9aBBVJe
- Large Language Models Still Can't Plan / PlanBench (Kambhampati, NeurIPS 2022)
  — https://openreview.net/forum?id=wUU-7XTL5XO
- On the Information Bottleneck Theory of Deep Learning (Saxe et al., ICLR 2018)
  — https://openreview.net/forum?id=ry_WPG-A-
- Grokking Group Multiplication with Cosets (ICML 2024) —
  https://openreview.net/forum?id=hcQfTsVnBo
- Meta-Reinforcement Learning with Zero-Shot RL — https://openreview.net/forum?id=XyGJJ4FPoX
- How much can language models memorize? (ICML 2026 award versions) —
  https://openreview.net/forum?id=bA6BgSbaUi · https://openreview.net/forum?id=NhU661EZ9C

### ACL Anthology / PapersWithCode

- PRIMERA: Pyramid-based Masked Sentence Pre-training — https://aclanthology.org/2022.acl-long.360/
- Super-NaturalInstructions (1600+ NLP tasks) — https://aclanthology.org/2022.emnlp-main.340/
- A System for Answering Simple Questions in Multiple Languages — https://aclanthology.org/2023.acl-demo.51/
- INVESTORBENCH: a financial benchmark for LLM agents — https://aclanthology.org/2025.acl-long.126/
- N-BEATS and DeepAR — https://paperswithcode.com/paper/n-beats-neural-basis-expansion-analysis-for ·
  https://paperswithcode.com/paper/deepar-probabilistic-forecasting-with
- Optimizing Millions of Hyperparameters by Implicit Differentiation —
  https://paperswithcode.com/paper/optimizing-millions-of-hyperparameters-by

### Lab publications (not on arXiv)

- Code Llama (Meta) — https://ai.meta.com/research/publications/code-llama-open-foundation-models-for-code/
- Large Concept Models: language modeling in a sentence representation space (Meta) —
  https://ai.meta.com/research/publications/large-concept-models-language-modeling-in-a-sentence-representation-space/
- Deep Double Descent (OpenAI) — https://openai.com/index/deep-double-descent/
- ShinkaEvolve — an open-source counterpart to AlphaEvolve (Sakana AI) — https://sakana.ai/shinka-evolve/
- EMU Video: Factorizing Text-to-Video Generation (Meta) —
  https://ai.meta.com/blog/emu-text-to-video-generation-image-editing-research/
- Training compute of frontier models grows 4–5x/year (Epoch AI) —
  https://epochai.org/blog/training-compute-of-frontier-ai-models-grows-by-4-5x-per-year

### Neuroscience and biology (mostly Neuroexistentialism, Axis of Ordinary)

- Attractor and integrator networks in the brain (Nat Rev Neurosci 2022) — 10.1038/s41583-022-00642-0
- Correspondence between neuroevolution and gradient descent (Nat Commun 2021) — 10.1038/s41467-021-26568-2
- A social path to human-like artificial intelligence (Nat Mach Intell 2023) — 10.1038/s42256-023-00754-x
- Neural spiking for causal inference and learning (PLOS Comp Biol 2023) — 10.1371/journal.pcbi.1011005
- Why mathematics is set to be revolutionized by AI (Nature 2024) — 10.1038/d41586-024-01413-w
- Emergence of belief-like representations through RL (bioRxiv) — 10.1101/2023.04.04.535512
- MetaWorm: an integrative model of the C. elegans brain and body (bioRxiv) — 10.1101/2024.02.22.581686
- Photonic computing: 10.1038/s41566-024-01394-2 · 10.1038/s41377-022-00717-8

## Addendum 2: exhaustive pass over non-arXiv sources

All 938 domains and 28 PDF links in the export were checked. Below is what genuinely
qualifies as research work and did not make it into the earlier sections.

### Classics that are not on arXiv

- **Long Short-Term Memory** (Hochreiter & Schmidhuber, Neural Computation, 1997) —
  https://direct.mit.edu/neco/article-abstract/9/8/1735/6109/Long-Short-Term-Memory
- **Learning to Forget: Continual Prediction with LSTM** (Gers et al., 2000) —
  https://direct.mit.edu/neco/article-abstract/12/10/2451/6415/Learning-to-Forget-Continual-Prediction-with-LSTM
- The most cited neural nets of the 20th century (Schmidhuber's overview) —
  https://people.idsia.ch/~juergen/most-cited-neural-nets.html

### Anthropic: interpretability on transformer-circuits.pub

- Circuit tracing / attribution graphs, the methods part —
  https://transformer-circuits.pub/2025/attribution-graphs/methods.html
- Attribution graphs, the "biology" of the model: specific Claude mechanisms examined —
  https://transformer-circuits.pub/2025/attribution-graphs/biology.html

### Nested Learning (Google)

- The paper PDF itself — https://abehrouz.github.io/files/NL.pdf
- Blog post describing the paradigm and the HOPE model —
  https://research.google/blog/introducing-nested-learning-a-new-ml-paradigm-for-continual-learning/

### Works that arrived via project pages

- Self-RAG — https://selfrag.github.io/
- DIAMOND: a diffusion world model that plays CS:GO — https://diamond-wm.github.io/
- AudioPaLM: an LLM that can speak and listen — https://google-research.github.io/seanet/audiopalm/examples/
- Voicebox (Meta, speech generation) — https://ai.facebook.com/blog/voicebox-generative-ai-model-speech/
- Perfusion (NVIDIA) — https://research.nvidia.com/labs/par/Perfusion/ ·
  HyperDreamBooth — https://hyperdreambooth.github.io/
- MineDojo — https://minedojo.org/
- Schema: a symbolic world model for ARC-AGI-3 — http://schema-harness.github.io

### Financial ML

- The "Virtue of Complexity" debate (Kelly, Malamud & Zhou versus Nagel's critique):
  https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5239006 ·
  https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5346842 ·
  https://voices.uchicago.edu/stefannagel/files/2025/07/Complexity_2.pdf ·
  https://bfi.uchicago.edu/wp-content/uploads/2025/08/BFI_WP_2025-104.pdf
- Deep Adaptive Input Normalization for price forecasting from Limit Order Book data —
  https://www.researchgate.net/publication/331273826
- An Intelligent Financial Portfolio Trading Strategy using Deep Q-Learning —
  https://www.groundai.com/project/an-intelligent-financial-portfolio-trading-strategy-using-deep-q-learning8432/3
- Learning to Replicate Expert Judgment in Financial Tasks (Thinking Machines) —
  https://thinkingmachines.ai/news/learning-to-replicate-expert-judgment-in-financial-tasks/

### Miscellaneous

- Machine Learning for Ancient Languages: A Survey (Computational Linguistics, MIT Press) —
  https://direct.mit.edu/coli/article/doi/10.1162/coli_a_00481/116160/
- ADAM Optimization with Adaptive Batch Selection / AdamCB (ICLR 2025) —
  https://iclr.cc/virtual/2025/poster/30565
- Characterizing emergent phenomena in LLMs (Google Research) —
  https://ai.googleblog.com/2022/11/characterizing-emergent-phenomena-in.html
- Few-shot tool use doesn't really work yet (Google Research) —
  https://research.google/blog/few-shot-tool-use-doesnt-really-work-yet/
- Deep learning models might be secretly almost linear (LessWrong; echoes
  "Your Transformer is Secretly Linear") —
  https://www.lesswrong.com/posts/JSWF2ZLt6YahyAauE/../deep-learning-models-might-be-secretly-almost-linear
- How much LLM training data is there, in the limit? —
  https://www.educatingsilicon.com/2024/05/09/how-much-llm-training-data-is-there-in-the-limit/
- CogPGT: a genetic predictor of IQ — https://herasight-project.webflow.io/technical-paper/cogpgt-1
- Orbifold Tutte embeddings (geometry processing) —
  https://www.semanticscholar.org/paper/4165542ba777ea63facc7ea9866f43ba63f054ae

### Books and long-form texts (not papers, but relevant)

- Deep Learning: Foundations and Concepts, Bishop & Bishop —
  https://link.springer.com/book/10.1007/978-3-031-45468-4
- Neuroevolution book — https://neuroevolutionbook.com/ · RLHF book — https://rlhfbook.com/
- Situational Awareness (Aschenbrenner) — https://situational-awareness.ai ·
  AI 2027 (Kokotajlo) — https://ai-2027.com/

## Addendum 3: added manually

Open-ended evolution and self-improvement:

- AI-GAs: AI-generating algorithms, an alternate paradigm for producing general AI
  (Jeff Clune, 2019) — https://arxiv.org/abs/1905.10985
- Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents (2025) —
  https://arxiv.org/abs/2505.22954
- Competition and Attraction Improve Model Fusion (Sakana AI) — https://arxiv.org/abs/2508.16204
- Continuous Thought Machines (Sakana AI): synchronization of neural activity over time
  as the representation — https://pub.sakana.ai/ctm/

Reasoning mechanisms and model introspection:

- Emergent Hierarchical Reasoning in LLMs through Reinforcement Learning —
  https://arxiv.org/abs/2509.03646
- Grokked Transformers are Implicit Reasoners: A Mechanistic Journey to the Edge of
  Generalization — https://arxiv.org/abs/2405.15071
- Language Models Are Capable of Metacognitive Monitoring and Control of Their Internal
  Activations — https://arxiv.org/abs/2505.13763
- Language Models Use Trigonometry to Do Addition (Kantamneni & Tegmark) —
  https://arxiv.org/abs/2502.00873
- Emergent Introspective Awareness in Large Language Models (Anthropic, October 2025) —
  https://transformer-circuits.pub/2025/introspection/index.html

Neuroscience and consciousness:

- Relating transformers to models and neural representations of the hippocampal formation
  (Whittington et al.) — https://arxiv.org/abs/2112.04035
- Is my red your red? Evaluating structural correspondences of color qualia
  (iScience 2025, unsupervised alignment via optimal transport) —
  https://www.cell.com/iscience/fulltext/S2589-0042(25)00289-5

Other:

- Reinforcement Learning Textbook (Sergey Ivanov) — https://arxiv.org/abs/2201.09746
- Position: LLMs can't jump — https://openreview.net/pdf?id=klU4737opt
  (title taken from search results; the OpenReview page is behind bot protection)

## Other (niche/applied)

Finance and trading: RL for portfolio management (https://arxiv.org/abs/1706.10059), Financial Trading as a Game (https://arxiv.org/abs/1807.02787), a review of DL in market forecasting (https://arxiv.org/abs/2003.01859).
3D and graphics: ShapeFlow, 3DSNet, 3DStyleNet, Isometric Multi-Shape Matching, Stylizing 3D Scene (2006.07982, 2011.13388, 2108.12958, 2012.02689, 2105.13016).
Hardware: TPU v4 (https://arxiv.org/abs/2304.01433), optical matrix multiplication (https://arxiv.org/abs/2309.10232).
