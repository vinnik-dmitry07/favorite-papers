##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Dissociating language and thought in large language models

###### Abstract

Large Language Models (LLMs) have come closest among all models to date to mastering human language, yet opinions about their linguistic and cognitive capabilities remain split. Here, we evaluate LLMs using a distinction between formal linguistic competence—knowledge of linguistic rules and patterns—and functional linguistic competence—understanding and using language in the world. We ground this distinction in human neuroscience, which has shown that formal and functional competence rely on different neural mechanisms. Although LLMs are surprisingly good at formal competence, their performance on functional competence tasks remains spotty and often requires specialized fine-tuning and/or coupling with external modules. We posit that models that use language in humanlike ways would need to master both of these competence types, which, in turn, could require the emergence of mechanisms specialized for formal linguistic competence, distinct from functional competence.

* The two lead authors contributed equally to this work.

A Preprint August 24, 2026

Keywords : Large Language Models, language and thought, cognitive neuroscience, linguistic competence, computational modeling

## The language-thought conflation

When we hear a sentence, we typically assume that it was produced by a rational, thinking agent (another person). The sentences that people generate in day-to-day conversations are based on their world knowledge (“Not all birds can fly.”), their reasoning abilities (“You’re 15, you can’t go to a bar.”), and their goals (“Would you give me a ride, please?”). Thus, we often use other people’s statements as a window into their minds.

In 1950, Alan Turing leveraged this tight relationship between language and thought to propose his famous test [ 1 ] . The Turing test uses language as an interface to cognition, allowing a human participant to probe the knowledge and reasoning capacities of two conversation partners to determine which of them is a human and which is a machine. Although the utility of the Turing test has since been questioned, it has undoubtedly shaped the way society today thinks of machine intelligence [ 2 ] .

The popularity of the Turing test, combined with the language-thought coupling in everyday life, has led to several common fallacies related to the language-thought relationship. One fallacy is that an entity (be it a human or a machine) that is good at language must also be good at thinking. If an entity generates long coherent stretches of text, it must possess rich knowledge and reasoning capacities. Let’s call this the “good at language -> good at thought” fallacy. This fallacy has come to the forefront due to the recent rise of Large Language Models (LLMs; see Glossary), including OpenAI’s GPT models, Anthropic’s Claude, and more open alternatives [ 3 ] like Meta’s LLaMa models and EleutherAI’s GPT-J. LLMs today can produce text that is difficult to distinguish from human output, outperform humans at some text comprehension tasks [ 4 , 5 ] , and show superhuman performance on next-word prediction [ 6 ] . As a result, claims have emerged—both in the popular press and in the academic literature—that LLMs are not only a major advance in language processing, but are also showing “sparks of artificial general intelligence” [ 7 ] . However, when evaluating LLMs’ capabilities, it is important to distinguish between their ability to think and their linguistic ability. The “good at language -> good at thought” fallacy makes it easy to confuse the two, leading people to mistakenly attribute intelligence and intentionality to even the most basic dialog systems (e.g., the chatbot Eliza from the 1960s [ 8 ] ).

The contrapositive of this fallacy is that a model that is bad at thinking must also be a bad model of language. Let’s call this the “bad at thought -> bad at language” fallacy. LLMs are commonly criticized for their lack of consistent, generalizable world knowledge [ 9 ] , lack of commonsense reasoning abilities [ 10 ] , and failure to understand what an utterance is really about [ 11 ] . Based on this evidence, some critics suggest that the models’ failure to produce linguistic output that fully captures the richness and sophistication of human thought means that they are not good models of human language .

Both the “good at language -> good at thought” and the “bad at thought -> bad at language” fallacies stem from the conflation of language and thought. This conflation is unsurprising: it is still novel, and thus uncanny, to encounter an entity that generates fluent sentences despite lacking a human identity. Thus, our heuristics for understanding what a language model is doing—heuristics that emerged from our language experience with other humans—are broken.

To mitigate the language-thought conflation fallacies, we propose to systematically distinguish between two kinds of linguistic competence: formal linguistic competence -the knowledge of rules and statistical regularities of language—and functional linguistic competence —the ability to use language in real-world situations. Our motivation for the formal/functional distinction comes from the human brain, where these skills are robustly dissociable. Both formal and functional linguistic competence are essential components of human language use: an effective communicator needs to both generate grammatical, meaningful utterances and strategically use those utterances to achieve diverse, context-dependent goals [ 12 , 13 ] .

Armed with this distinction, we evaluate the capabilities of contemporary LLMs and argue that LLMs exhibit a gap between formal and functional competence skills: for modern LLMs, formal competence in English is near human-level, whereas their functional competence remains patchy, with results depending on specific functional competence domains and on tasks within those domains. Moreover, whereas formal linguistic competence in LLMs improves drastically with the amount of training data, functional linguistic competence improvements with scale are less consistent, such that LLM developers have now shifted away from simple scaling-up of the language prediction task to more specialized methods targeting behaviors of interest (e.g., Reinforcement Learning from Human Feedback: RLHF [ 14 ] ) or coupling an LLM with external specialized modules (leading to so-called “augmented language models”; [ 15 ] ).

Therefore, we posit that the next-word prediction objective allows a model to master formal but not necessarily functional linguistic competence. What is required for mastery of functional competence is harder to pin down, in part because so much of human cognition (commonsense reasoning, scientific knowledge, everyday knowledge) can be conveyed through language and thus learned from language —even if these capacities are not themselves inherently linguistic. As a result, language models acquire a variety of non-linguistic capacities. But the ultimate ceiling for functional competence depends on important open questions about the information contained in the linguistic signal and the mechanisms used to leverage that information, as we discuss.

In the rest of the paper, we develop a framework for evaluating the competence of modern language models from a cognitive science perspective. In the first section, we elaborate on the constructs of formal and functional linguistic competence and motivate this distinction based on the evidence from human neuroscience. In the second section, we discuss the successes of LLMs in achieving formal linguistic competence, showing that models trained on word-in-context prediction capture numerous complex linguistic phenomena. In the third section, we consider several domains required for functional linguistic competence—formal reasoning, world knowledge, situation modeling, and social cognition—on which today’s LLMs often fail, or at least perform worse than humans. In the fourth section, we discuss the implications of our framework for building and evaluating future models of language and thought before summarizing our key conclusions in the final section.

## Formal vs. functional linguistic competence

### What does linguistic competence entail?

#### Formal linguistic competence

We define formal linguistic competence as a set of capacities required to produce and comprehend a given language. Broadly, being formally competent means getting the form of language right: knowing which strings could be valid words of a language (e.g., bnick cannot be a word in English but blick can [ 16 ] ), how to productively combine morphemes to form novel words (e.g., Barack Obama-less-ness but not Barack Obama-ness-less [ 17 ] ), learning enough about word meanings to know which words can go in which slots in a sentence [ 18 ] , and knowing how to combine words into valid sentences.

Because of its centrality in the history of linguistics, it is the last of these (forming words into sentences) that we focus on in our discussion of formal competence. Most users of Standard Written English say, “The dogs in my bedroom are asleep” rather than “The dogs in my bedroom is asleep”, because the verb “to be” must match the number of the noun that is the subject of the sentence (“the dogs”), even though that verb is closer to an intervening, singular noun (“bedroom”). Linguistic competence also requires exquisite sensitivity to the regularitiesof idiosyncratic linguistic constructions. For instance, although English speakers know not to use the indefinite article “a” with plural nouns—making a phrase like “a days” ill-formed—they also know that it is allowed in a special construction where an adjective and a numeral intervene: “a beautiful five days in New York” [ 19 , 20 ] .

Human language users likely learn rules, plus thousands of idiosyncratic constructions [ 21 ] , through some combination of sophisticated statistical learning [ 22 , 23 , 24 ] and innate conceptual and/or linguistic machinery [ 25 , 26 , 27 ] . The result is the human ability to understand and produce grammatical and coherent linguistic utterances.

#### Functional linguistic competence

In addition to being competent in the rules and statistical regularities of language, a competent language user uses language to accomplish goals in the world [ 28 , 12 , 29 ] : to talk about things that can be seen or felt or heard, to reason about diverse topics; to make requests; to cajole, prevaricate, and flatter. People use language in tandem with other perceptual and cognitive systems, such as our senses and our memory, and deploy words as part of a broader communication framework supported by our sophisticated social skills. A formal language system in isolation is useless unless it can interface with the rest of perception, cognition, and action.

The capacities required to use language to do things in the world are distinct from formal competence and depend crucially on non-linguistic cognition (Figure 1 ). Thus, we define functional linguistic competence as non-language-specific cognitive functions that are required when using language in tandem with non-language-specific capacities in real-world circumstances.

### Motivation for the distinction between formal vs. functional linguistic competence

Our motivation for the distinction between formal and functional linguistic competence comes from what we know about the architecture of the human mind. In humans, language is robustly dissociated from the rest of high-level cognition, as well as from perception and action. Below we briefly summarize a body of evidence from cognitive science and neuroscience that supports this dissociation.

#### The language network supports language processing in the human brain

Human language processing draws on a set of interconnected brain areas in the frontal and temporal lobes (typically in the left hemisphere). This language network supports both comprehension (spoken, written, and signed) [ 30 , 31 , 32 , 33 ] and production [ 34 , 35 ] ; is sensitive to linguistic regularities at multiple levels: from phonological/sub-lexical [ 36 ] to phrase/sentence level [ 37 , 38 ] ; and supports linguistic operations related both to the processing of word meanings and to combinatorial semantic and syntactic processing [ 38 , 35 ] . Damage to the language network leads to linguistic deficits [ 39 , 40 ] . This tight link between the language network and language function indicates that these brain regions are responsible for language processing in humans.

#### The language network does not support non-linguistic cognition

The language network is remarkably selective for language. Evidence of a strong dissociation between language processing and non-linguistic abilities comes from two main sources: a) functional brain imaging studies of neurotypical adults, and b) behavioral investigations of individuals with aphasia—a language impairment typically caused by a stroke or degeneration.

Brain imaging techniques like functional MRI (fMRI) are used to observe real-time activity in the language network in healthy individuals. Given its high spatial resolution, fMRI is well-suited to study whether any two cognitive abilities draw on the same brain structures. For example, to ask whether language and mathematical reasoning recruit the same brain areas, we can have participants perform a language task and a math task while in an MRI scanner and then test whether brain regions that are active during language processing are also active when participants solve a math problem. This approach reveals that the language network is extremely selective for language processing: it responds reliably when people listen to, read, or generate sentences, but not when they perform arithmetic tasks, engage in logical reasoning, understand computer programs, listen to music, categorize objects or events, reason about people’s mental states, or process non-verbal communicative information like facial expressions or gestures [ 41 , 42 , 43 , 44 , 37 , 45 , 46 , 47 , 48 ] .

Studies of individuals with aphasia provide a unique opportunity for testing which cognitive capacities rely on linguistic representations. Of particular interest are cases of ‘global aphasia’, which affects both production and comprehension. Individuals with global aphasia exhibit severe linguistic deficits that spare nothing but a small set of words. If some aspects of non-linguistic cognition draw on the same resources as language, then individuals with severe linguistic deficits should invariably exhibit impaired performance on the relevant non-linguistic tasks. However, despite the nearly complete loss of linguistic abilities, individuals with severe aphasia can have intact non-linguistic cognitive abilities: they can play chess, solve arithmetic problems, leverage their world knowledge to perform diverse tasks, reason about cause and effect, and navigate complex social situations [ 49 ] .

In summary, evidence from brain imaging studies and from individuals with aphasia is remarkably consistent: the mechanisms that process language in the human brain do not support non-linguistic cognitive tasks. This sharp dissociation suggests that, in examining language models’ functionality, we should separate their linguistic abilities from their abstract knowledge and reasoning abilities, which can be probed—–and perhaps even learned–—through a linguistic interface, but which require more than formal linguistic competence.

## LLMs have largely mastered formal linguistic competence in English

In a 2019 interview, Chomsky remarked [ 50 ] : “We have to ask here a certain question: is [deep learning] engineering or is it science? […] On engineering grounds, it’s kind of worth having, like a bulldozer. Does it tell you anything about human language? Zero.” The view that deep learning models are not of scientific interest remains common in linguistics, and, despite many arguments for integrating such models into research on human language processing and acquisition [ 51 , 52 , 53 ] and a chorus of arguments that they should be taken seriously as linguistic and cognitive models [ 54 , 55 , 56 ] , their integration into language research still encounters resistance.

In this section, we evaluate the performance of LLMs qua language models by asking whether these models have made progress towards achieving formal linguistic competence–the kind of competence supported by the language-selective network in the human brain. We argue that LLMs have turned out to be surprisingly successful at mastering formal competence—qualitatively different in their formal linguistic capacities from models from before roughly 2018 in a way that was predicted by few practitioners in the field, and which was unexpected given longstanding claims that grammatically competent systems would require strong language-specific priors. With surprise comes information: models’ successes are informative for linguistic theorizing.

### Statistical language models: some fundamentals

LLMs arose from several earlier approaches in computational linguistics, including statistical language modeling, word embeddings, and connectionism (an earlier term for the approach that morphed into today’s deep learning). Similar to earlier statistical language models, LLMs are usually first trained on a word prediction task (the same task used for training n-gram models going back to Shannon’s work in the mid-20th century; see [ 57 ] for historical overview). Similar to approaches in distributional semantics and word embeddings (for overviews, see [ 58 , 59 ] ), LLMs represent linguistic information as vectors in a high-dimensional space. Similar to earlier connectionist approaches [ 60 , 61 ] , LLMs are neural networks — a class of machine learning systems that was originally inspired by the human brain and learns its parameters from the input data. All of these approaches stand in contrast to models that use explicit, structured hierarchical representations of syntactic rules (see [ 62 ] for a discussion of these two divergent paradigms).

N-grams and word embedding models achieved some success in various domains in natural language processing (e.g., spelling correction, spam classification, sentiment analysis). However, they never approached human-level performance on general language tasks like text generation, leading to claims that purely statistical approaches would never be able to capture the richness of natural language, particularly in complex syntactic, morphological, and semantic domains [ 63 , e.g.,] . For instance, it has been claimed that statistical approaches, which use linear strings of words as input, are in principle unable to learn rare and complex syntactic features that require representing phrases and sentences hierarchically [ 64 ] . This pessimism is now challenged by LLMs.

LLMs are typically first trained on a training set constructed from a massive amount of text from the web. During pretraining , LLMs have a simple objective: predict a held-out token (the basic unit in LLMs—often but not always corresponding to words or morphemes [ 65 ] ) based on a fixed number of previous tokens. The predicted token is then compared with the ground truth (which token actually occurred in that sentence), and the error signal is propagated back through the model to update its many parameters. The token prediction objective is often used as a pretraining step, and the model is then fine-tuned for a more specific task.

Although it is tempting [ 66 ] to move the goalposts and focus on what these models are still unable to do, we argue that the remarkable advances in LLMs’ ability to capture various linguistic phenomena should not be overlooked. Significant formal linguistic abilities arise in models on the scale of GPT-2 or BERT and seem to plateau at a high level in contemporary LLMs (Box 3.1 ).

Box 1. The path toward formal linguistic competence When did LLMs achieve formal linguistic competence? Table I shows text generations from an n-gram model, an RNN (a recurrent neural network, which were state-of-the-art language models in the mid-2010s, before transformers), GPT-2, GPT-3, and GPT-4. The n-gram model and RNN clearly fail to show formal linguistic competence: the sentences are not grammatical or sensible. In contrast, GPT-2 (a model produced just 8 years after the RNN in Row 2) generates grammatical output: the verbs agree with their subjects, parts of speech are used appropriately, relatively complex syntactic constructions like the relative clause “that has nothing to do with who we are” is appropriately tied to a noun phrase. However, compared to the GPT-3 and GPT-4 output, it makes less sense: what does “everything about being with people” mean? Finally, the outputs of GPT-3 and GPT-4 are both grammatical and semantically coherent, such that they can plausibly be taken for answers generated by a human. Table I . Examples of texts generated by increasingly more advanced language models in response to a prompt “The meaning of life is…” (following [ 67 ] and using their example verbatim in Row 2). Starting with GPT-2, outputs are grammatical and largely use the rules and patterns of English (formal linguistic competence). Model Text 3-gram model trained on Moby Dick The meaning of life is gulped and gone, bleeds with keenest anguish at the same muteness of humanity over all creations. Just so with Ahab, ’says I;’ look here you sabbee me, has every reason to be served. RNN from [ 67 ] The meaning of life is the tradition of the ancient human reproduction: it is less favorable to the good boy for when to remove her bigger. In the show’s agreement unanimously resurfaced. GPT-2 [ 68 ] The meaning of life is something simple that has nothing to do with who we are. Everything about being with people is tied to those characteristics, and people are just machines. GPT-3 davinci-002 [ 69 ] The meaning of life is a mystery to us all, and a question that will never be answered. Life is what we make of it, and it’s up to each of us to find our own meaning in life. GPT-4 (via ChatGPT interface) The meaning of life is subjective and varies greatly depending on personal beliefs, values, and experiences. Some people find meaning in relationships, personal achievements, or spiritual beliefs, while others may see it as a journey of self-discovery, learning, or contributing to the greater good.

Box 2. What about semantics? Does semantics fall under formal or functional linguistic competence? The answer depends on what kind of semantics we are talking about. One meaning of semantics, often associated with compositional and lexical semantics, concerns the way that meaning is derived from words and their combinations. We consider this aspect part of formal linguistic competence. Indeed, the language network in the brain responds both to lexical semantics, i.e., retrieving the meaning of individual words, and to compositional semantics, i.e., constructing the meaning of multi-word utterances [ 38 ] . Insofar as LLMs are highly sensitive to lexical and combinatorial semantics, they parallel the language network. The second meaning of semantics is something closer to“general conceptual knowledge” (used in contexts such as “non-verbal semantics”, e.g., extracting the meaning of a picture). This definition is closely related to the notion of world knowledge, which we discuss in our section on world knowledge. Given the fact that conceptual knowledge and reasoning does not have to operate over linguistic inputs but is nonetheless essential for fluent language use, we classify it under functional linguistic competence.

### Large language models learn core aspects of human language processing

For LLMs to be useful as models of language processing in humans, we must be convinced that the models encode the abstract phonological, morphological, syntactic, and semantic rules that characterize human language (see Box 3.1 for a distinction between “linguistic” and conceptual semantics). Although interesting differences exist between linguistic processing in LLMs and humans [ 70 , 71 ] , there are also important similarities. Here, we review evidence that LLMs succeed as models of formal linguistic competence. We focus primarily on syntax, showing evidence of mastery on grammatical benchmarks as well as evidence for emergent syntactic structure in LLMs. But similar successes, both in performance and emergent structure, have been shown in other linguistic domains (e.g., emergent phonological structure [ 72 ] , productive generation of morphologically complex neologisms [ 73 ] , rich lexical semantic information [ 74 ] , etc.).

#### LLMs perform well on benchmarks of diverse linguistic phenomena

By being trained for word prediction, transformer models learn a lot about the structure of language, including linguistic features that, even recently, were thought to be beyond the scope of statistical models. These models have succeeded not just on tests of general language understanding developed by the NLP community (e.g., GLUE tasks [ 75 ] ), but, critically for our purposes, on tests of linguistic competence in English and other languages with massive corpora available (see Box 3 for discussion of lower-resourced languages).

The benchmark BLiMP [ 76 ] , for instance, contains minimal pairs of grammatical vs. ungrammatical sentences across a diverse range of complex linguistic phenomena like filler-gap dependencies (“Bert knew what many writers find” vs. “*Bert knew that many writers find”) and negative polarity items (“The truck has clearly tipped over” vs. “*The truck has ever tipped over”). Strikingly, a model [ 77 ] submitted to the BabyLM challenge [ 78 ] achieved 86% on BLiMP (cf. human baseline of 89%) despite being trained on an amount of data comparable to what a human child might be exposed to (see Box 3). Models achieve similarly impressive results on other linguistic benchmarks like SyntaxGym [ 79 ] , and there are now dozens of investigations of specific complex linguistic phenomena (some of which we discuss below).

#### LLMs learn hierarchical structure

In human languages, words are combined to make compositional meanings. In a multi-word sentence, the individual words’ meanings do not simply get added linearly one by one. Instead, they can be combined hierarchically into tree-like structures.

The hierarchical structure in language manifests in many ways. One prominent example is non-local feature agreement. In English and many other languages, verbs agree with their subjects. For instance, a plural subject uses the verb “are”, whereas a singular subject uses “is”. A bigram model, which simply stores frequencies of two-word strings, could learn that “The keys are on the table” is more probable than “The keys is on the table” by knowing that “keys are” is more common than “keys is”. But such a model would not be able to learn that the subject and verb agree even if arbitrarily far apart: for instance, “The keys to the old, wooden kitchen cabinet are on the table” has six intervening words between the subject and verb, and yet “are” still agrees with “keys” and not with “cabinet”. However, a model that learns the underlying hierarchical structure of English should be able to keep track of this long-distance subject-verb dependency [ 80 ] .

Today’s LLMs perform long-distance number agreement well above chance, preferring the grammatical over a non-grammatical sentence continuation even in the presence of intervening distractor words [ 81 , 82 ] , although some earlier models can be distracted by frequency effects (such as differences in the frequency between the singular and plural forms [ 83 ] ). In a similar vein, LLMs can handle other constructions that require complex hierarchy, like filler-gap dependencies [ 84 ] . Finally, studies that examine the internal geometry of the models’ sentence representations [ 85 ] , studies that causally intervene on models’ internal representations [ 86 ] , and studies that turn on and off specific model “neurons” [ 87 , 88 ] have provided mechanistic insights into how an LLM might represent hierarchical structure and establish non-local structural dependencies.

#### LLMs learn linguistic abstractions

Following [ 89 ] , we define an abstraction as a generalized linguistic representation—–such as a part-of-speech category (e.g., noun or verb) or grammatical role (e.g., subject or object)–—that goes beyond simple storage of input and allows for generalization. The very notion of subject-verb agreement, outlined in the previous section, relies on the abstract categories of subject and verb. As described in [ 81 ] , in a sentence like “dogs in the neighborhood often… (bark/barks)”, a model might learn a shallow version of the agreement rule, namely, that the collocation of “dogs” and “bark” in the same sentence is more common than “dogs” and barks”. However, a model that has an abstract representation of categories like grammatical subject, grammatical number, and verb should be able to handle long-distance number agreement even for novel combinations of words.

One way to test a model’s knowledge of abstract rules is by using semantically nonsensical sentences, like “The colorless green ideas I ate with the chair… (sleep/sleeps)”. Models have been shown to perform the agreement task well in several languages, even on these semantically anomalous sentences [ 81 ] .

An even more stringent test for linguistic abstraction asks whether LLMs can apply morphosyntactic rules to novel words. A study of BERT’s abstraction capabilities [ 90 ] showed that BERT has some ability to generalize grammatical categories. They give the model novel words, used in phrases, as input (e.g., “the blick” where blick is likely a noun and “they dax” where dax is likely a verb) and test whether, based on the input, the model can generalize the part-of-speech category (e.g., assign a higher score to “I went to a blick” than to “I went to a dax”). They conclude that BERT succeeds partially at this task: it does learn to generalize, but only after repeated examples [but see 91 , 92 , for ways in which the word itself affects compositional ability] . Models also seem to (often) be able to use novel words appropriately [ 69 , 73 ] .

A large body of work has tested linguistic abstraction in LLMs using a method called probing [ 93 , 94 ] . In this literature, a classifier is often trained to take as input internal model representations and then predict as output an abstract category, such as part-of-speech or dependency role. The logic of the probe is to test whether these abstract categories can be successfully recovered from the internal model states. Using this approach, it has been claimed that LLMs “rediscover the classical NLP pipeline” [ 95 ] , learning at various layers features like part-of-speech categories, parses, named entities, and semantic roles (although see [ 96 ] ).

Importantly, a human-like language model is not expected to rely solely on abstract rules. Humans use diverse cues in their language learning and processing that sometimes override or conflict with strict hierarchical syntactic processing [ 97 , 98 , e.g.,] . Humans also rely, to varying extents, on memorizing previously seen input, as opposed to purely applying abstract rules [ 89 , 21 ] . Thus, when evaluating formal competence in LLMs, it is essential to directly compare their performance with that of humans [ 99 ] . For instance, a re-examination [ 100 ] of an earlier study [ 101 ] showed that apparent syntactic agreement deficits in GPT-2 occurred on instances that were also challenging for humans. Overall, LLMs clearly learn some linguistic abstraction, even if the degree of that abstraction remains a matter of debate (as it does for humans).

#### LLMs learn constructions

Recent evidence suggests that LLMs learn syntactic constructions [ 102 , 103 , 104 ] . These constructions can be idiosyncratic, lexically sensitive, and relatively rare, such as “a beautiful five days in Austin” [ 105 ] . LLMs also show some amount of sensitivity to the Preposing in Prepositional Phrase construction (“Surprising though it may be…”), even when the gap crosses a finite clause boundary (“Surprising though I know it may be”) [ 106 ] . They achieve this sensitivity even though such examples crossing the finite clause boundary are vanishingly rare: only 58 examples out of 7 billion sentences in a corpus. The fact that models can learn that some vanishingly rare constructions are grammatical, whereas other equally rare constructions are not, suggests that LLMs meaningfully learn something about syntax.

Models are also sensitive to the form of the comparative correlative “the better the syntax, the better the semantics” [ 107 ] . However, this sensitivity does not mean that they are sensitive to the semantic implications of the construction. Indeed, it appears that inferences based on these sentences can be a challenge (e.g., knowing that if I say “the better the syntax, the better the semantics” and then tell you that the syntax is better, this means the semantics is better). This asymmetry nicely illustrates the formal/functional distinction: the model clearly knows how to use the construction and get the form right without necessarily being able to access the intended meaning. We discuss these issues in more detail in later sections.

### LLMs are predictive of activity in the human language network

As discussed above, language processing in humans relies on a dedicated brain network. This network exhibits all the hallmarks of formal linguistic competence: it is sensitive to abstract hierarchical rules in isolated phrases and sentences [ 31 , 108 , 109 , 110 ] , in naturalistic narratives [ 111 , 112 , 113 , 114 ] , and in syntactically well-formed but semantically empty ("jabberwocky") stimuli [ 31 , 49 , 109 ] . The language network is also sensitive to specific word co-occurrences [ 111 , e.g., as evidenced by sensitivity to n-gram surprisal; ] , indicating that it learns not only the rules, but also the patterns of language. The language network’s selectivity for linguistic vs. non-linguistic inputs, along with its sensitivity to linguistic rules and patterns, allows us to operationalize formal linguistic competence as a set of computations that in humans take place within the language network.

If LLMs and the human language network perform similar computations to achieve formal linguistic competence, we expect to observe similarities in their internal organization (see [ 55 ] for similar arguments in the domain of vision). And indeed, LLMs and the human language network exhibit non-trivial similarities.

First, the internal architecture of LLMs resembles that of the language network. Both operate at the level of abstract linguistic units (words/tokens) rather than modality-specific representations, such as pixels or acoustic waveforms, and combine these unit-level representations into composite representations of phrases and sentences. Neither system shows clear spatial segregation for syntactic and semantic processing (LLMs: [ 95 , 115 ] ; brain: [ 38 , 114 ] ), indicating that these processes are tightly functionally coupled in both.

Second, one can establish a direct mapping between internal LLM representations and neural activity patterns within the language network. This mapping can be successfully used to predict brain responses to novel sentences and words in previously unseen contexts [ 116 , 117 , 118 ] . This similarity between sentence activation patterns in LLMs and the brain is suggestive of similar representational mechanisms that support computations in these systems.

We do not claim that the correspondence between LLMs and the language network is one-to-one. For instance, LLMs learn patterns outside traditional human linguistic competency, such as predicting newline characters [ 119 ] . Nevertheless, the fact that internal representations learned by contemporary LLMs contain sufficient information to predict the language network’s responses to diverse linguistic strings indicates at least some correspondence between LLMs’ representations and those in the language network.

### Using LLMs as models of formal linguistic competence in humans

LLMs today generate highly coherent, grammatical texts that can be indistinguishable from human output. In doing so, they exhibit knowledge of hierarchical structure and linguistic abstractions, while resembling human brain responses during language processing. These models are not perfect learners of abstract linguistic rules, but neither are humans. We therefore conclude that LLMs possess substantial formal linguistic competence, at least in English.

LLMs have already overturned claims about the fundamental impossibility of acquiring certain linguistic knowledge—including hierarchical structure and abstract categories—from the statistics of linguistic input alone [ 120 ] . If language modeling continues to improve (including learning from more realistic kinds and amounts of data; Box 3.4 ), this would allow testing more general versions of this “poverty of the stimulus” argument [ 121 ] , including specific tests of what inductive biases might be necessary to successfully learn the rules and statistical regularities of human language. As such, LLMs have substantial value in the scientific study of language learning and processing.

### Excessive reliance on statistical regularities

### Unrealistic amounts of training data

### Insufficient tests on languages other than English

## Non-augmented LLMs fall short on functional linguistic competence

Real-life language use is impossible without non-linguistic cognitive skills. Understanding a sentence, reasoning about its implications, and deciding how to respond all rely on cognitive capacities that go beyond formal competence. In this section, we ask: how good are contemporary LLMs at functional linguistic competence?

We focus on four key capacities that are not language-specific but are nevertheless crucial for language use in real-life settings: i) formal reasoning—a host of abilities including logical and mathematical reasoning, computational thinking, and novel problem solving; ii) world knowledge—factual and commonsense knowledge about agents, objects, properties, actions, events, and ideas; iii) situation modeling—the dynamic tracking of objects, agents, and events as a narrative/conversation unfolds over time; and iv) social reasoning—understanding the social context of linguistic exchanges. An average conversation requires the use of all these capacities, yet none of them are specific to language use.

For each domain, we first describe its neural mechanisms in humans and then discuss how well contemporary LLMs have mastered the domain. We conclude that, unlike formal competence, functional competence of LLMs is uneven, often requiring specialized fine-tuning and/or lacking human-like robustness and generality. In Box 4 , we highlight the importance of properly evaluating LLMs; evaluation issues can occur in studies of either formal or functional competence, but we believe they have led to a particularly large amount of overclaiming about models’ functional competence.

### A. Fine-tuning on the task and the challenge of closed models

### B. Generalizable, robust performance

### Formal Reasoning

Language allows people to discuss highly abstract ideas, turn ideas into scientific and philosophical theories, construct logical syllogisms, and engage in formal debates. Unsurprisingly, language is often considered a cornerstone of complex reasoning [ 136 , 137 ] . However, neuroscience provides evidence that language and formal reasoning dissociate in cognitive systems, and so a model that has mastered formal linguistic competence will not necessarily exhibit logical reasoning abilities.

Humans. Despite their close interplay, language and reasoning rely on distinct cognitive and neural systems. Unlike language, formal reasoning engages brain regions known as the multiple demand network [ 138 ] , named so because these regions are engaged in many cognitively demanding tasks: logic [ 47 ] , mathematical reasoning [ 41 ] , physical reasoning [ 139 ] , and computer code comprehension [ 140 , 46 ] . Human patient studies have provided causal evidence for the role of the multiple demand network in logical reasoning by showing that the amount of damage to these regions correlates negatively with performance on standard tests of fluid intelligence [ 141 , 142 ] . Importantly, the multiple demand network supports reasoning even when the task is presented linguistically [ 41 , 140 , 47 ] — similar to how LLMs receive their prompts.

LLMs. Multiple studies have pointed out LLMs’ limitations on tasks requiring formal reasoning, such as math problems. GPT-3 performs well on two-digit addition and subtraction but not on more complex tasks, such as three-digit addition or two-digit multiplication [ 69 ] . GPT-4 similarly shows good performance on small-digit but not large-digit mathematical operations [ 143 ] . Reasoning tests that break common co-occurrence patterns in the input or require multi-step operations also lead to model failure [ 144 , 145 ] .

The most commonly cited reason for these failures is the failure of artificial neural nets to generalize to patterns outside their training distribution [ 145 , 146 ] . This generalization gap can be partially bridged by “chain of thought” approaches, whereby a model is prompted to generate intermediate computation steps before arriving at an answer [ 147 ] . However, even these approaches do not lead to foolproof results [ 143 ] . Thus, more and more researchers pair LLMs with external modules that can carry out structural logical and mathematical computations, such as the Mathematica plugin [ 148 ] or a probabilistic reasoning engine [ 149 ] . The shift toward augmenting LLMs with reasoning-specific modules is consistent with evidence from neuroscience: language and formal reasoning are distinct cognitive capacities that work best when they are supported by separate processing mechanisms.

### World models 1: factual and commonsense knowledge

A commonly debated capacity in LLMs is their ability to leverage internal world models [ 150 , 149 ] . We break down the notion of world models into two components: world knowledge (factual and commonsense, this section) and situation tracking (the ability to maintain and update information about objects, agents, etc.; next section).

Humans. Evidence from neuroscience shows a dissociation between linguistic and semantic (world) knowledge. Individuals with language deficits may struggle to produce grammatical utterances and retrieve contextually appropriate words, but their ability to reason about objects and events presented non-linguistically often remains intact [ 151 , 42 ] . On the other hand, individuals who suffer from semantic dementia (a neurodegenerative disorder) retain the ability to speak but struggle with tasks that rely on world knowledge (e.g., knowing that pumpkins are typically orange) even when the stimuli are presented non-verbally as pictures [ 152 ] . Thus, linguistic and semantic knowledge can be disentangled.

LLMs. LLMs have access to a wealth of knowledge about the world: word co-occurrence patterns in texts on the web contain both factual information (e.g., who was the first man on the moon) and commonsense information (e.g., the taste of lemon) [ 153 ] . If this information can be effectively extracted, LLMs would be able to serve as off-the-shelf knowledge bases [ 154 ] . However, world knowledge contained in LLM representations suffers from several major shortcomings.

First, LLMs routinely generate false statements, informally known as “hallucinations”. This observation is unsurprising: their training objective is to generate plausible sentence continuations, with no reference to the underlying factual correctness of the resulting claims. Some developers have fine-tuned LLMs to provide links to sources that back up their claims; however, those citations can also be inaccurate [ 155 ] .

Second, LLM outputs are often inconsistent: the same prompt phrased in different ways can elicit different responses [ 156 ] . They can also get “distracted” by intervening information, e.g., an irrelevant claim inserted between a premise and a conclusion [ 92 ] .

Third, commonsense knowledge is often underrepresented in language corpora: people are much more likely to communicate new or unusual information rather than commonly known facts [ 157 ] . As a result, LLMs can struggle on commonsense knowledge benchmarks [ 158 ] , especially once low-level statistical cues are controlled for [ 9 ] .

And fourth, explicitly stated factual knowledge is easy to access but hard to maintain, requiring constant updates; for instance, the answer to “Who is the current president of the US?” will change every 4 or 8 years. Whereas humans can update their knowledge representations via a single sentence, updating world knowledge in LLMs requires locating and editing this particular bit of knowledge in their internal parameters-a non-trivial task [ 159 ] , especially because these edits should affect some other bits of knowledge (e.g., that the previously current president is now the past president) but leave many other facts unaffected [ 160 ] .

A more human-like approach to world knowledge representation might require dissociating linguistic representation/processing and world knowledge storage/updates. Such approaches exist [ 161 , e.g.,] but have not yet reached dominance in the field, typically because of relatively low coverage of existing knowledge bases. Although we cannot rely on LLMs alone for accurate world knowledge claims, we might use them as a starting point for constructing detailed knowledge bases [ 162 ] and commonsense schemata [ 163 ] .

### World models 2: situation tracking

People can follow the plot of a story that spans multiple chapters or even multiple books. We can also remember many details weeks or months after a conversation. We accomplish these feats by leveraging language inputs to create a "situation model" — a mental model of entities, relations between them, and a sequence of states they had been in or events they had participated in [ 164 ] . Does the language network in humans construct a situation model based on its inputs? And how good are LLMs at building and updating situation models over time?

Humans. The language network in humans does not appear to track structure above the clause level [ 165 , 166 ] . Instead, integration of meaning over longer periods of time likely takes place within the so-called default network [ 167 ] . Crucially, the default network tracks both linguistic and non-linguistic narratives [ 168 ] , indicating that situation modeling is not a language-specific skill.

LLMs. Situation modeling in LLMs faces two main challenges: (1) extracting information from many sentences in a row; (2) integrating incoming inputs to appropriately update information about entities and their states.

The first problem is currently being tackled by continuously increasing the models’ context window, i.e., the number of words they can process in one go. This approach will inevitably run into computational challenges: when summarizing a book, having a model that simultaneously attends to each word in that book is vastly inefficient (although see some attempts to overcome this issue, e.g., [ 169 ] ). A human-like solution to this problem might include hierarchical processing, e.g., generating a summary for each chapter and then for the whole book (for related approaches, see 170 , 171 ).

Even when LLMs operate over shorter spans of text that easily fit inside their context windows, the question is: can they update their internal representations to track changes in the world? Some evidence suggests that they can [ 172 ] , although LLMs make characteristically non-human-like mistakes when it comes to situation modeling: for instance, their outputs can refer to non-existent discourse entities (“Arthur doesn’t own a dog. The dog is brown.” [ 173 ] ). Thus, whether robust situation model building over shorter span of text is feasible using an LLM-only architecture remains a matter of debate.

### Social reasoning

“Water!”

Wittgenstein famously used single-word utterances like this to show that linguistic meaning radically depends on context. Although this word’s literal meaning is straightforward, the intended meanings are more varied. Is the word being gasped by a thirsty person in the desert? By a hiker warning his friend of a hidden stream? An impatient diner talking to a waiter? Work in cognitive science and linguistics has come to recognize that these context-dependent aspects of language are not just peripheral but a central part of human language production and understanding [ 28 , 12 ] .

The set of skills required to infer the intended meaning of an utterance beyond its literal content is known as pragmatics. Pragmatics likely engages a variety of neural mechanisms [ 174 , 175 , 176 ] , including both the language network and other brain regions. Thus, different types of pragmatic reasoning can be classified either as formal or as functional competence. Here, we focus on one core functional competence capacity required for pragmatics: social reasoning.

Humans. A wealth of neuroscientific evidence shows that the human brain has dedicated machinery for processing social information [ 44 , 177 ] . The most relevant to our current discussion is the theory of mind network [ 178 ] , a set of brain regions that are engaged when their owner is attempting to infer somebody’s mental state (with our without the use of language; [ 179 , 180 ] ). The specific contributions of the theory of mind network to language understanding can be divided into two broad categories. First, just like other functionally specialized brain modules, it is engaged when processing semantic content that is specifically related to its domain: narratives that require inferring the mental state of the characters engage the theory of mind network [ 180 ] , and texts that require inferring the characters’ intentions evoke greater activity than those that do not [ 181 , 182 ] . Second, the theory of mind network is engaged more strongly during nonliteral language comprehension, including phenomena like jokes, sarcasm, indirect speech, and conversational implicature [ 183 , 176 ] —in other words, in situations where understanding the meaning of an utterance requires inferring the intentions of the speaker. Thus, successful language understanding relies on our broader, non-language-specific social inference skills.

LLMs. Recent models, trained with RLHF, have shown strong performance in interpreting non-literal utterances, such as metaphors and polite deceits, suggesting they can reach human or near-human performance on at least some pragmatic tasks [ 184 ] . That said, LLMs exhibit uneven performance across pragmatic domains: their ability to interpret sarcasm or to complete jokes was limited even as their metaphor comprehension abilities soared [ 184 ] . Overall, at least some forms of pragmatic inference might be acquired via targeted fine-tuning. It remains an open question whether aspects of pragmatics that are easiest for LLMs are those that are supported by the language network in humans.

LLMs’ ability to solve theory of mind tasks has been subject to particular controversy. These tasks require both social knowledge and the ability to maintain a situation model. A typical example would feature character X moving an object from location A to location B while character Y is not around and so, does not see the move. The goal is to predict the true location of the object (location B) and the location where character Y believes the object is (location A). A bold claim that instruction-tuned LLMs have mastered theory-of-mind tasks [ 185 ] was quickly countered by a demonstration that including basic controls (such as character Y being told about the true object location) brought LLM performance to below-chance levels [ 186 ] . Several other studies have identified limitations in LLM performance on theory of mind tasks [ 187 , 188 , 189 , cf. 190 ] . One solution to overcome these limitations has been to augment an LLM with a symbolic tracker of entity states and character beliefs [ 191 ] , an approach that mirrors the separation between language and theory of mind processing in humans.

### Language input can bootstrap functional competence capabilities

Many non-linguistic cognitive capabilities can be substantially enhanced by language input. In humans, this relationship is particularly salient during development: babies learn new conceptual categories more easily when they are accompanied by linguistic labels [ 192 ] , and children with delayed language access have delayed social reasoning abilities [ 193 ] . Even in adulthood, knowledge of specific number words predicts the ability to conceptually represent exact numbers [ 194 ] . Coupled with the fact that language inputs contain vast quantities of information about the world, and that language is both a crucial data source and representational substrate for much of people’s world knowledge, this evidence suggests that, in principle, a model trained exclusively on language input could acquire much of functional linguistic competence.

Thus, we do not argue that functional linguistic competence is out of reach for language-based models; our main goals are (1) to highlight the conceptual distinction between formal and functional linguistic competence—which in the human brain draw on separate neural circuits, and (2) to demonstrate the gulf between LLMs’ formal and functional linguistic abilities. These facts lead to a speculation that, like the human brain, models that can master language use would also require or benefit from separate mechanisms for formal and functional competence. We discuss this idea next.

## Toward models that use language like humans

In this paper, we have advanced the thesis that formal and functional linguistic competence are distinct capabilities, with formal competence relying on distinct language machinery and function competence requiring the integration of diverse brain networks. We have shown that formal competence emerges in contemporary LLMs as a result of the word-in-context prediction objective; however, this objective alone appears insufficient for equipping LLMs with functional linguistic competence skills. Based on the neuroscience evidence, we suggest that models that succeed at real-life language use will need to be modular , mimicking the division of labor between formal and functional competence in the human brain.

We see at least two ways to separate LLM circuits responsible for formal and functional competence: explicitly building modularity into the architecture of the system (we call this Architectural Modularity ) or naturally inducing modularity through the training process, both through the training data and the objective function (we call this Emergent Modularity ).

Architectural Modularity has a long history; it involves stitching together separate components, perhaps with quite specialized architectures [ 195 , 196 ] . Modern-day examples include a transformer language model paired with a separate memory module [ 161 , 197 , e.g., ] or a model for visual question answering, which includes a language module, a vision module, and a reasoning module [ 198 , 199 ] . Such modular models achieve high task performance, are more efficient (i.e., can be trained on smaller datasets and have lower compute demands during inference), and show better generalizability (i.e., perform well on datasets with previously unseen properties). The modules of such models can be trained separately or together, similarly to how humans can flexibly combine different cognitive skills when learning to perform novel complex tasks.

Recently, the desire for this kind of modularity has expanded to include attempts to augment language models with the ability to call separate programs, as in including API calls [ 200 ] , mathematical calculators [ 201 ] , planners [ 202 ] , and other kinds of modules that do specific structured operations.

Another approach in this vein uses LLMs as modules to translate a natural language query into code, which can then be passed to a symbolic module, which then generates an answer. [ 149 ] outline a research program for this approach, showing that a version of GPT-3 fine-tuned to generate both natural language and code (Codex) can translate text input into meaningful structured probabilistic programs; inference in these programs can be used to reason over relational domains (like kinship systems), grounded domains (like visual scenes), and situations that require planning and understanding the plans of others. Their approach demonstrates a promising avenue for integrating what LLMs succeed at (namely, formal linguistic competence) with other cognitive modules that benefit from symbolic structure and abstraction.

The Emergent Modularity approach involves training models end-to-end (similarly to contemporary LLMs) while creating the conditions that facilitate the emergence of specialized model sub-components over the course of training. Modular structure has been shown to spontaneously emerge in some end-to-end neural network systems in domains other than language [ 203 , 204 , e.g., ] , which suggests that emergent modularity may constitute an optimal solution to many complex tasks. One strategy for this approach to be successful is for the model architecture to incentivize the development of individual, specialized modules within the model. Transformers, the most popular architecture today, satisfy this condition to some extent by allowing different attention heads to attend to different input features [ 205 , 206 , 207 , e.g.] ; certain approaches promote modularization even more explicitly, e.g., by endowing transformers with a mixture-of-experts architecture that incentivizes separate “experts” to carry out different computations [ 208 , 209 , 210 ] .

A modular model architecture is much better aligned with the brain’s functional architecture for language, which includes separate components for formal and functional competence. Is it possible to build formally and functionally competent systems that do not mimic the modular structure of the human brain? In theory, yes: systems with different underlying architectures (e.g., modular vs. non-modular) can, in principle, exhibit similar behaviors. However, explicitly disentangling formal and functional competence skills at the architectural level is perhaps the most fail-safe path toward ensuring that an AI model uses language in a humanlike way.

Box 5. The need for better benchmarks To assess progress on the road toward building models that use language in human-like ways, it is important to develop benchmarks that evaluate both formal and functional linguistic competence. This distinction can reduce the confusion that arises when discussing these models by combating the “good at language -> good at thought” and the “bad at thought -> bad at language” fallacies. Several existing benchmarks already evaluate formal linguistic competence in LLMs [ 79 , 76 ] and can be complemented by additional tests of core linguistic features: hierarchy and abstraction. Benchmarks for evaluating different domains of functional linguistic competence, like commonsense world knowledge (e.g., WinoGrande [ 211 ] ), can often be “hacked” by LLMs by leveraging flawed heuristics [ 212 ] . This issue is likely exacerbated in large-scale heterogeneous datasets like BIG-bench [ 5 ] . Moreover, functional competence benchmarks often rely on a certain, often underspecified level of required formal linguistic competence skills and/or mix together different functional competence abilities. Designing benchmarks that carefully disentangle different components of language knowledge and use would therefore constitute an important step toward a more informative assessment of LLMs.

## Concluding remarks

Over the last few years, the discourse around language models has consisted of a curious mix of overclaiming and underclaiming [ 66 ] . While some claim models are on the verge of intelligence, others have pointed out the many failures of LLMs on a broad range of tasks, from number multiplication to generating factually true statements. Here, we have put these seemingly inconsistent reactions in dialog with prior and ongoing work in computational linguistics, cognitive science, and neuroscience. In particular, we argue that LLMs are remarkably successful on tasks that require a particular type of structural and statistical linguistic competence—formal linguistic competence. Although their performance is not yet fully human-like, these models achieve an impressive degree of success in representing and using hierarchical relationships among words and building representations that are sufficiently abstract to generalize to new words and constructions. As such, these LLMs are underused in linguistics as candidate models of human language processing.

We also review some of the LLMs’ failures on tasks that target real-life language use, such as reasoning, while highlighting that the capabilities these tasks require are fundamentally distinct from formal language competence and rely on machinery in the human brain distinct from language processing machinery.

The failures of LLMs on non-linguistic tasks do not undermine their utility as models of language processing. After all, the brain areas that support language processing in humans also cannot do math, solve logical problems, or even track the meaning of a story across sentences or paragraphs. If we take the human mind and brain—a good example of generalized intelligence—as a guide, we might expect that future advances in developing intelligent systems will require combining language models with models that represent abstract knowledge and support complex reasoning, rather than expecting a single model (trained with a single word prediction objective) to do it all. Finally, to detect and monitor such advances, we need benchmarks that cleanly separate formal and functional linguistic competence (Box 5 ). Formally and rigorously evaluating functional competence in LLMs will be informative for both science and engineering (see Outstanding Questions).

To those who have argued that most interesting aspects of human language cannot be learned from data alone, we say that LLMs compellingly demonstrate the possibility of learning complex syntactic features from linguistic input (even if, as of now, much more input is required than a typical child gets exposed to). To those who criticize LLMs for their inability to do complex arithmetic or to reason about the world, we say, give language models a break: given a strict separation of language and non-linguistic capabilities in the human mind, we should evaluate these capabilities separately, recognizing successes in formal linguistic competence even when non-linguistic capabilities lag behind. Finally, to those who are looking to improve the state of machine learning systems, we suggest that, instead of, or in addition to, continuously scaling up the models [ 213 ] , more promising solutions will come in the form of modular architectures—built-in or emergent—that, like the human brain, integrate language processing with additional systems that carry out perception, reasoning, and action.

## Glossary

• Abstraction is, for our purposes, a linguistic representation that allows for generalization. Part-of-speech is one such example: words like “dog” and “cat” belong to the abstract category of “nouns”.

• Architectural Modularity involves explicitly building distinct modules into a computational model, with each module responsible for achieving different goals.

• Fine-tuning is a process by which, after a model is pretrained, it receives additional training on new data, often for a specific purpose.

• Formal linguistic competence is the ability to get the form of language right. It includes knowledge of word formation (e.g, phonology and morphology), knowledge of word meaning, and knowledge of rules and statistical patterns for how words combine to create sentences. Note that our use of the term ‘competence’ differs from the classic competence/performance distinction in linguistics, given that in both models and humans separating competence and performance is often difficult.

• Emergent Modularity refers to the natural induction of modularity through the model training process, without explicitly building it into the architecture.

• Functional linguistic competence is the ability to use language to accomplish things in the world. It relies on a host of non-language-specific cognitive domains like formal reasoning, world knowledge, situation tracking, and social cognition.

• Hierarchical structure is a crucial property of language that allows it to be more than just a linear sequence of words. Rather, how words go together in a sentence is better captured by a tree-like structure, where some words and phrases are nested inside larger phrases.

• The language network is the interconnected set of brain regions that respond selectively to language but not to non-linguistic inputs and tasks.

• Large Language Models (LLMs) are models based on deep neural architectures (often but not always transformers) and trained on massive amounts of text using a word-in-context prediction task (sometimes with additional training objectives incorporated during or after the main training process). The term “large” refers to the number of parameters in these models, which ranges from millions to billions, as well as the size of the training data.

• Pretraining is the process by which a model is first trained on a general task (for LLMs, typically a text prediction task) before being trained or used for a more specialized purpose.

• Reinforcement Learning from Human Feedback (RLHF) is a process by which reinforcement learning techniques are used to impart human preferences (e.g., as to which of two model outputs is preferred) to a model. It seems to lead to significant improvements on functional tasks.

• Theory of mind is a cognitive skill that enables thinking and reasoning about the minds of others (i.e., what others know, believe, want, etc.).

• Tokens are the basic units in language models. In earlier language models, they were often words or morphemes. In today’s LLMs, they are often inferred from large amounts of text using an algorithm like Byte Pair Encoding. They can resemble words and morphemes, but sometimes also for subword or linguistically unnatural units.

## Highlights

• Formal linguistic competence (getting the form of language right) and functional linguistic competence (using language to accomplish goals in the world) are distinct cognitive skills.

• The human brain contains a network of areas that selectively support language processing (formal linguistic competence), but not other domains like logical or social reasoning (functional linguistic competence).

• In the late 2010’s, Large Language Models trained on word prediction tasks began achieving unprecedented success in formal linguistic competence, showing impressive performance on linguistic tasks that likely require hierarchy and abstraction.

• Consistent performance on tasks requiring functional linguistic competence is harder to achieve for Large Language Models and often involves augmentations beyond next word prediction.

• Evidence from cognitive science and neuroscience can illuminate the capabilities and limitations of Large Language Models and pave the way toward better, human-like models of both language and thought.

## Outstanding Questions

• How much functional competence can be acquired from the linguistic signal? Humans use language as a substrate for knowledge, and so LLMs acquire non-linguistic information from the linguistic signal. How much information in this signal can be used to bootstrap functional competence? Are there aspects of functional competence that cannot be learned from language at all?

• How can we train competent language models on smaller amounts of data? LLMs have achieved remarkable linguistic competence but they are trained on data very unlike what human children encounter. Although LLMs receive vastly more words (several orders of magnitude), they lack the richly structured and interactive input thought to be essential to child language acquisition. Would benefits emerge from training models in more interactive and human-like ways?

• Will the formal competence successes of LLMs transfer to other world languages? Most LLM evaluations have taken place in English and a handful of other world languages. Building models for lower-resourced languages and evaluating them on both formal and functional dimensions is an important ongoing project.

• How long will the LLM growth continue ? 10 years ago, most researchers in the field would not have predicted that LLMs would be as advanced as they are today. Will current AI approaches lead to further revolutionary achievements in language and thought or would the mastery of functional linguistic competence require radically new approaches?

• Which is more promising: architectural modularity or emergent modularity? If we want to build human-like modular systems, will it require explicitly building in functionally distinct components or can they be induced through end-to-end fine-tuning, e.g. with Reinforcement Learning from Human Feedback (RLHF)?

• How modular are today’s LLMs? We argue that an LLM that achieves both formal and functional competence may need to rely on separate mechanisms for different competence types. Mechanistic interpretability studies can shed light on the extent to which different cognitive tasks might segregate even within today’s LLMs.

• Should LLMs be described as individual language users or as distributions over potential user outputs? There are different ways to think about LLMs in the context of language use: e.g., as individual language users (“agent-based view”) or as tools augmenting human activities, like a calculator (“tool-based view”) [ 214 , 215 , 216 ] . Which of these views will be the most fruitful way to think about LLMs as they gain additional competencies and become more widely used?

• How much grounding do LLMs need to continue improving? How limited are text-only approaches, compared to approaches across different modalities [ 217 , 218 ] ?

• How much can LLMs ultimately tell us about human language and cognition? What are the cases where LLMs fall short as models of human language use? Are these discrepancies solvable or will they require language researchers to develop different paradigms?

## Acknowledgements

For helpful conversations, we thank Jacob Andreas, Alex Warstadt, Dan Roberts, Kanishka Misra, students in the 2023 UT Austin Linguistics 393 seminar, the attendees of the Harvard LangCog journal club, the attendees of the UT Austin Department of Linguistics SynSem seminar, Gary Lupyan, John Krakauer, members of the Intel Deep Learning group, Yejin Choi and her group members, Allyson Ettinger, Nathan Schneider and his group members, the UT NLL Group, attendees of the KUIS AI Talk Series at Koç University in Istanbul, Tom McCoy, attendees of the NYU Philosophy of Deep Learning conference and his group members, Sydney Levine, organizers and attendees of the ILFC seminar, and others who have engaged with our ideas. We also thank Aalok Sathe for help with document formatting and references.

## Funding Sources

KM acknowledges funding from NSF Grant 2104995. AI was supported by funds from the Quest Initiative for Intelligence. EF was supported by NIH awards R01-DC016607, R01-DC016950, and U01-NS121471 and by research funds from the Brain and Cognitive Sciences Department, McGovern Institute for Brain Research, and the Simons Foundation through the Simons Center for the Social Brain.

## Conflicts of Interest

The authors declare no Conflicts of Interest.

## References

[1] A. M. Turing. Computing Machinery and Intelligence. Mind , 59(October):433–60, 1950. Publisher: Oxford University Press.

[2] Y. Chang, X. Wang, J. Wang, Y. Wu, L. Yang, K. Zhu, H. Chen, X. Yi, C. Wang, Y. Wang, et al. A survey on evaluation of large language models. ACM Transactions on Intelligent Systems and Technology , 2023.

[3] R. Bommasani, K. Klyman, S. Longpre, S. Kapoor, N. Maslej, B. Xiong, D. Zhang, and P. Liang. The foundation model transparency index. arXiv preprint arXiv:2310.12941 , 2023.

[4] A. Wang, Y. Pruksachatkun, N. Nangia, A. Singh, J. Michael, F. Hill, O. Levy, and S. R. Bowman. SuperGLUE: A stickier benchmark for general-purpose language understanding systems. In 33rd Conference on Neural Information Processing Systems , 2019.

[5] A. Srivastava, A. Rastogi, A. Rao, A. A. M. Shoeb, A. Abid, A. Fisch, A. R. Brown, A. Santoro, A. Gupta, A. Garriga-Alonso, A. Kluska, A. Lewkowycz, A. Agarwal, A. Power, A. Ray, A. Warstadt, A. W. Kocurek, A. Safaya, A. Tazarv, A. Xiang, A. Parrish, A. Nie, A. Hussain, A. Askell, A. Dsouza, A. Slone, A. Rahane, A. S. Iyer, A. J. Andreassen, A. Madotto, A. Santilli, A. Stuhlmüller, A. M. Dai, A. La, A. Lampinen, A. Zou, A. Jiang, A. Chen, A. Vuong, A. Gupta, A. Gottardi, A. Norelli, A. Venkatesh, A. Gholamidavoodi, A. Tabassum, A. Menezes, A. Kirubarajan, A. Mullokandov, A. Sabharwal, A. Herrick, A. Efrat, A. Erdem, A. Karakaş, B. R. Roberts, B. S. Loe, B. Zoph, B. Bojanowski, B. Özyurt, B. Hedayatnia, B. Neyshabur, B. Inden, B. Stein, B. Ekmekci, B. Y. Lin, B. Howald, B. Orinion, C. Diao, C. Dour, C. Stinson, C. Argueta, C. Ferri, C. Singh, C. Rathkopf, C. Meng, C. Baral, C. Wu, C. Callison-Burch, C. Waites, C. Voigt, C. D. Manning, C. Potts, C. Ramirez, C. E. Rivera, C. Siro, C. Raffel, C. Ashcraft, C. Garbacea, D. Sileo, D. Garrette, D. Hendrycks, D. Kilman, D. Roth, C. D. Freeman, D. Khashabi, D. Levy, D. M. González, D. Perszyk, D. Hernandez, D. Chen, D. Ippolito, D. Gilboa, D. Dohan, D. Drakard, D. Jurgens, D. Datta, D. Ganguli, D. Emelin, D. Kleyko, D. Yuret, D. Chen, D. Tam, D. Hupkes, D. Misra, D. Buzan, D. C. Mollo, D. Yang, D.-H. Lee, D. Schrader, E. Shutova, E. D. Cubuk, E. Segal, E. Hagerman, E. Barnes, E. Donoway, E. Pavlick, E. Rodolà, E. Lam, E. Chu, E. Tang, E. Erdem, E. Chang, E. A. Chi, E. Dyer, E. Jerzak, E. Kim, E. E. Manyasi, E. Zheltonozhskii, F. Xia, F. Siar, F. Martínez-Plumed, F. Happé, F. Chollet, F. Rong, G. Mishra, G. I. Winata, G. de Melo, G. Kruszewski, G. Parascandolo, G. Mariani, G. X. Wang, G. Jaimovitch-Lopez, G. Betz, G. Gur-Ari, H. Galijasevic, H. Kim, H. Rashkin, H. Hajishirzi, H. Mehta, H. Bogar, H. F. A. Shevlin, H. Schuetze, H. Yakura, H. Zhang, H. M. Wong, I. Ng, I. Noble, J. Jumelet, J. Geissinger, J. Kernion, J. Hilton, J. Lee, J. F. Fisac, J. B. Simon, J. Koppel, J. Zheng, J. Zou, J. Kocon, J. Thompson, J. Wingfield, J. Kaplan, J. Radom, J. Sohl-Dickstein, J. Phang, J. Wei, J. Yosinski, J. Novikova, J. Bosscher, J. Marsh, J. Kim, J. Taal, J. Engel, J. Alabi, J. Xu, J. Song, J. Tang, J. Waweru, J. Burden, J. Miller, J. U. Balis, J. Batchelder, J. Berant, J. Frohberg, J. Rozen, J. Hernandez-Orallo, J. Boudeman, J. Guerr, J. Jones, J. B. Tenenbaum, J. S. Rule, J. Chua, K. Kanclerz, K. Livescu, K. Krauth, K. Gopalakrishnan, K. Ignatyeva, K. Markert, K. Dhole, K. Gimpel, K. Omondi, K. W. Mathewson, K. Chiafullo, K. Shkaruta, K. Shridhar, K. McDonell, K. Richardson, L. Reynolds, L. Gao, L. Zhang, L. Dugan, L. Qin, L. Contreras-Ochando, L.-P. Morency, L. Moschella, L. Lam, L. Noble, L. Schmidt, L. He, L. Oliveros-Colón, L. Metz, L. K. Senel, M. Bosma, M. Sap, M. T. Hoeve, M. Farooqi, M. Faruqui, M. Mazeika, M. Baturan, M. Marelli, M. Maru, M. J. Ramirez-Quintana, M. Tolkiehn, M. Giulianelli, M. Lewis, M. Potthast, M. L. Leavitt, M. Hagen, M. Schubert, M. O. Baitemirova, M. Arnaud, M. McElrath, M. A. Yee, M. Cohen, M. Gu, M. Ivanitskiy, M. Starritt, M. Strube, M. Swędrowski, M. Bevilacqua, M. Yasunaga, M. Kale, M. Cain, M. Xu, M. Suzgun, M. Walker, M. Tiwari, M. Bansal, M. Aminnaseri, M. Geva, M. Gheini, M. V. T, N. Peng, N. A. Chi, N. Lee, N. G.-A. Krakover, N. Cameron, N. Roberts, N. Doiron, N. Martinez, N. Nangia, N. Deckers, N. Muennighoff, N. S. Keskar, N. S. Iyer, N. Constant, N. Fiedel, N. Wen, O. Zhang, O. Agha, O. Elbaghdadi, O. Levy, O. Evans, P. A. M. Casares, P. Doshi, P. Fung, P. P. Liang, P. Vicol, P. Alipoormolabashi, P. Liao, P. Liang, P. W. Chang, P. Eckersley, P. M. Htut, P. Hwang, P. Miłkowski, P. Patil, P. Pezeshkpour, P. Oli, Q. Mei, Q. Lyu, Q. Chen, R. Banjade, R. E. Rudolph, R. Gabriel, R. Habacker, R. Risco, R. Millière, R. Garg, R. Barnes, R. A. Saurous, R. Arakawa, R. Raymaekers, R. Frank, R. Sikand, R. Novak, R. Sitelew, R. L. Bras, R. Liu, R. Jacobs, R. Zhang, R. Salakhutdinov, R. A. Chi, S. R. Lee, R. Stovall, R. Teehan, R. Yang, S. Singh, S. M. Mohammad, S. Anand, S. Dillavou, S. Shleifer, S. Wiseman, S. Gruetter, S. R. Bowman, S. S. Schoenholz, S. Han, S. Kwatra, S. A. Rous, S. Ghazarian, S. Ghosh, S. Casey, S. Bischoff, S. Gehrmann, S. Schuster, S. Sadeghi, S. Hamdan, S. Zhou, S. Srivastava, S. Shi, S. Singh, S. Asaadi, S. S. Gu, S. Pachchigar, S. Toshniwal, S. Upadhyay, S. S. Debnath, S. Shakeri, S. Thormeyer, S. Melzi, S. Reddy, S. P. Makini, S.-H. Lee, S. Torene, S. Hatwar, S. Dehaene, S. Divic, S. Ermon, S. Biderman, S. Lin, S. Prasad, S. Piantadosi, S. Shieber, S. Misherghi, S. Kiritchenko, S. Mishra, T. Linzen, T. Schuster, T. Li, T. Yu, T. Ali, T. Hashimoto, T.-L. Wu, T. Desbordes, T. Rothschild, T. Phan, T. Wang, T. Nkinyili, T. Schick, T. Kornev, T. Tunduny, T. Gerstenberg, T. Chang, T. Neeraj, T. Khot, T. Shultz, U. Shaham, V. Misra, V. Demberg, V. Nyamai, V. Raunak, V. V. Ramasesh, vinay uday prabhu, V. Padmakumar, V. Srikumar, W. Fedus, W. Saunders, W. Zhang, W. Vossen, X. Ren, X. Tong, X. Zhao, X. Wu, X. Shen, Y. Yaghoobzadeh, Y. Lakretz, Y. Song, Y. Bahri, Y. Choi, Y. Yang, Y. Hao, Y. Chen, Y. Belinkov, Y. Hou, Y. Hou, Y. Bai, Z. Seid, Z. Zhao, Z. Wang, Z. J. Wang, Z. Wang, and Z. Wu. Beyond the imitation game: Quantifying and extrapolating the capabilities of language models. Transactions on Machine Learning Research , 2023.

[6] B.-D. Oh and W. Schuler. Why does surprisal from larger transformer-based language models provide a poorer fit to human reading times? Transactions of the Association for Computational Linguistics , 11:336–350, 2023.

[7] S. Bubeck, V. Chandrasekaran, R. Eldan, J. Gehrke, E. Horvitz, E. Kamar, P. Lee, Y. T. Lee, Y. Li, S. Lundberg, et al. Sparks of artificial general intelligence: Early experiments with GPT-4. arXiv preprint arXiv:2303.12712 , 2023.

[8] J. Weizenbaum. Eliza—a computer program for the study of natural language communication between man and machine. Communications of the ACM , 9(1):36–45, 1966.

[9] Y. Elazar, N. Kassner, S. Ravfogel, A. Ravichander, E. Hovy, H. Schütze, and Y. Goldberg. Measuring and improving consistency in pretrained language models. Transactions of the Association for Computational Linguistics , 9:1012–1031, 2021.

[10] G. Marcus. The next decade in AI: Four steps towards robust artificial intelligence. arXiv preprint arXiv:2002.06177 , 2020.

[11] E. M. Bender and A. Koller. Climbing towards NLU: On meaning, form, and understanding in the age of data. In D. Jurafsky, J. Chai, N. Schluter, and J. Tetreault, editors, Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics , pages 5185–5198, Online, July 2020. Association for Computational Linguistics.

[12] H. Grice. Logic and conversation. In P. Cole and J. L. Morgan, editors, Syntax and Semantics, Vol. 3, Speech Acts , pages 41–58. Academic Press, New York, 1975.

[13] H. H. Clark. Arenas of Language Use . University of Chicago Press, 1992.

[14] L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. Wainwright, P. Mishkin, C. Zhang, S. Agarwal, K. Slama, A. Ray, et al. Training language models to follow instructions with human feedback. Advances in Neural Information Processing Systems , 35:27730–27744, 2022.

[15] G. Mialon, R. Dessì, M. Lomeli, C. Nalmpantis, R. Pasunuru, R. Raileanu, B. Rozière, T. Schick, J. Dwivedi-Yu, A. Celikyilmaz, et al. Augmented language models: a survey. arXiv preprint arXiv:2302.07842 , 2023.

[16] M. Halle. Phonology in generative grammar. Word , 18(1-3):54–72, 1962.

[17] M. Aronoff and K. Fudeman. What is morphology? John Wiley & Sons, 2022.

[18] D. A. Cruse. Lexical Semantics . Cambridge University Press, 1986.

[19] M. Dalrymple and T. H. King. An amazing four doctoral dissertations. Argumentum , 15(2019), 2019. Publisher: Debreceni Egyetemi Kiado.

[20] C. Keenan. A pleasant three days in Philadelphia: Arguments for a pseudopartitive analysis. University of Pennsylvania Working Papers in Linguistics , 19(1):11, 2013.

[21] A. E. Goldberg. Explain me this: Creativity, competition, and the partial productivity of constructions . Princeton University Press, 2019.

[22] J. Bresnan. Is syntactic knowledge probabilistic? Experiments with the English dative alternation. Roots: Linguistics in search of its evidential base , 96:77–96, 2007.

[23] A. Clark. Distributional Learning as a Theory of Language Acquisition. In Proceedings of the 5th Workshop on Cognitive Aspects of Computational Language Learning (CogACLL) , page 29, Gothenburg, Sweden, April 2014. Association for Computational Linguistics.

[24] J. Saffran, R. Aslin, and E. Newport. Statistical learning by 8-month-old infants. Science , 274(5294):1926, 1996.

[25] N. Chomsky. Syntactic Structures . The Hague: Mouton, 1957.

[26] L. R. Gleitman. A human universal: the capacity to learn a language. Modern Philology , 90:S13–S33, 1993. Publisher: University of Chicago Press.

[27] R. Jackendoff. Foundations of Language: Brain, meaning, grammar, evolution, 2002.

[28] H. H. Clark. Using Language . Cambridge university press, 1996.

[29] M. Bucholtz and K. Hall. Language and identity. A Companion to Linguistic Anthropology , 1:369–394, 2004.

[30] F. Deniz, A. O. Nunez-Elizalde, A. G. Huth, and J. L. Gallant. The Representation of Semantic Information Across Human Cerebral Cortex During Listening Versus Reading Is Invariant to Stimulus Modality. Journal of Neuroscience , 39(39):7722–7736, September 2019. Publisher: Society for Neuroscience Section: Research Articles.

[31] E. Fedorenko, P.-J. Hsieh, A. Nieto-Castañón, S. Whitfield-Gabrieli, and N. Kanwisher. New method for fMRI investigations of language: defining ROIs functionally in individual subjects. Journal of Neurophysiology , 104(2):1177–1194, August 2010.

[32] M. MacSweeney, B. Woll, R. Campbell, P. K. McGuire, A. S. David, S. C. R. Williams, J. Suckling, G. A. Calvert, and M. J. Brammer. Neural systems underlying British Sign Language and audio-visual English processing in native users. Brain , 125(7):1583–1593, July 2002.

[33] T. L. Scott, J. Gallée, and E. Fedorenko. A new fun and robust version of an fMRI localizer for the frontotemporal language system. Cognitive Neuroscience , 8(3):167–176, 2017.

[34] L. Menenti, S. M. E. Gierhan, K. Segaert, and P. Hagoort. Shared language: overlap and segregation of the neuronal infrastructure for speaking and listening revealed by functional MRI. Psychological Science , 22(9):1173–1182, September 2011.

[35] J. Hu, H. Small, H. Kean, A. Takahashi, L. Zekelman, D. Kleinman, E. Ryan, A. Nieto-Castañón, V. Ferreira, and E. Fedorenko. Precision fmri reveals that the language-selective network supports both phrase-structure building and lexical access during language production. Cerebral Cortex , 33(8):4384–4404, 2023.

[36] T. I. Regev, J. Affourtit, X. Chen, A. E. Schipper, L. Bergen, K. Mahowald, and E. Fedorenko. High-level language brain regions are sensitive to sub-lexical regularities. bioRxiv , 2021.

[37] E. Fedorenko, M. K. Behr, and N. Kanwisher. Functional specificity for high-level linguistic processing in the human brain. Proceedings of the National Academy of Sciences , 108(39):16428–16433, September 2011.

[38] E. Fedorenko, I. A. Blank, M. Siegelman, and Z. Mineroff. Lack of selectivity for syntax relative to word meanings throughout the language network. Cognition , 203:104348, October 2020.

[39] E. Bates, S. M. Wilson, A. P. Saygin, F. Dick, M. I. Sereno, R. T. Knight, and N. F. Dronkers. Voxel-based lesion-symptom mapping. Nature Neuroscience , 6(5):448–450, May 2003.

[40] S. M. Wilson, D. K. Eriksson, M. Yen, A. T. Demarco, S. M. Schneck, and J. M. Lucanie. Language Mapping in Aphasia. Journal of Speech, Language, and Hearing Research : JSLHR , 62(11):3937–3946, November 2019.

[41] M. Amalric and S. Dehaene. Origins of the brain networks for advanced mathematics in expert mathematicians. Proceedings of the National Academy of Sciences of the United States of America , 113(18):4909–4917, May 2016.

[42] Y. Benn, A. A. Ivanova, O. Clark, Z. Mineroff, C. Seikus, J. S. Silva, R. Varley, and E. Fedorenko. The language network is not engaged in object categorization. Cerebral Cortex , 33(19):10380–10400, 2023.

[43] X. Chen, J. Affourtit, R. Ryskin, T. I. Regev, S. Norman-Haignere, O. Jouravlev, S. Malik-Moraleda, H. Kean, R. Varley, and E. Fedorenko. The human language system, including its inferior frontal component in “Broca’s area,” does not support music perception. Cerebral Cortex , 33(12):7904–7929, 04 2023.

[44] B. Deen, K. Koldewyn, N. Kanwisher, and R. Saxe. Functional Organization of Social Perception and Cognition in the Superior Temporal Sulcus. Cerebral Cortex , 25(11):4596–4609, November 2015.

[45] O. Jouravlev, D. Zheng, Z. Balewski, A. L. A. Pongos, Z. Levan, S. Goldin-Meadow, and E. Fedorenko. Speech-accompanying gestures are not processed by the language-processing mechanisms. Neuropsychologia , 132:107132, September 2019.

[46] Y.-F. Liu, J. Kim, C. Wilson, and M. Bedny. Computer code comprehension shares neural resources with formal logical inference in the fronto-parietal network. eLife , 9:e59340, dec 2020.

[47] M. M. Monti, L. M. Parsons, and D. N. Osherson. Thought beyond language: neural dissociation of algebra and natural language. Psychological Science , 23(8):914–922, August 2012.

[48] A. M. Paunov, I. A. Blank, O. Jouravlev, Z. Mineroff, J. Gallée, and E. Fedorenko. Differential Tracking of Linguistic vs. Mental State Content in Naturalistic Stimuli by Language and Theory of Mind (ToM) Brain Networks. Neurobiology of Language , pages 1–29, June 2022.

[49] E. Fedorenko and R. A. Varley. Language and thought are not the same thing: evidence from neuroimaging and neurological patients: Language versus thought. Annals of the New York Academy of Sciences , 1369(1):132–153, April 2016.

[50] L. Fridman. Noam Chomsky: Language, Cognition, and Deep Learning: Lex Fridman Podcast #53. Available online, 2019. Accessed: January 1, 2024.

[51] T. Linzen. What can linguistics and deep learning contribute to each other? Response to Pater. Language , 95(1):e99–e108, 2019. Publisher: Linguistic Society of America.

[52] I. A. Blank. What are large language models supposed to model? Trends in Cognitive Sciences , 2023.

[53] S. Jain, V. A. Vo, L. Wehbe, and A. G. Huth. Computational language modeling and the promise of in silico experimentation. Neurobiology of Language , pages 1–65, 2023.

[54] M. C. Frank. Openly accessible LLMs can help us to understand human cognition. Nature Human Behaviour , pages 1–3, 2023.

[55] R. Cao and D. Yamins. Explanatory models in neuroscience: Part 1–taking mechanistic abstraction seriously. arXiv preprint arXiv:2104.01490 , 2021.

[56] M. Baroni. On the proper role of linguistically-oriented deep net analysis in linguistic theorizing. Algebraic structures in natural language , pages 1–16, 2022.

[57] D. Jurafsky and J. H. Martin. Speech and Language Processing: An Introduction to Natural Language Processing, Computational Linguistics, and Speech Recognition . Pearson Prentice Hall, second edition, 2009.

[58] M. Baroni and A. Lenci. Distributional memory: A general framework for corpus-based semantics. Computational Linguistics , 36(4):673–721, 2010.

[59] K. Erk. Vector space models of word meaning and phrase meaning: A survey. Language and Linguistics Compass , 6(10):635–653, 2012.

[60] D. E. Rumelhart and J. L. McClelland. Parallel Distributed Processing . MIT Press, Cambridge, MA, 1986.

[61] J. Elman. Learning and development in neural networks: the importance of starting small. Cognition , 48(1):71–99, 1993.

[62] P. Norvig. Colorless green ideas learn furiously: Chomsky and the two cultures of statistical learning. Significance , 9(4):30–33, 2012.

[63] S. Pinker and A. Prince. On language and connectionism: Analysis of a parallel distributed processing model of language acquisition. Cognition , 28(1-2):73–193, 1988. Publisher: Elsevier.

[64] M. B. Everaert, M. A. Huybregts, N. Chomsky, R. C. Berwick, and J. J. Bolhuis. Structures, not strings: linguistics as part of the cognitive sciences. Trends in Cognitive Sciences , 19(12):729–743, 2015.

[65] R. Sennrich, B. Haddow, and A. Birch. Neural machine translation of rare words with subword units. In K. Erk and N. A. Smith, editors, Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , pages 1715–1725, Berlin, Germany, August 2016. Association for Computational Linguistics.

[66] S. Bowman. The dangers of underclaiming: Reasons for caution when reporting how NLP systems fail. In S. Muresan, P. Nakov, and A. Villavicencio, editors, Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , pages 7484–7499, Dublin, Ireland, May 2022. Association for Computational Linguistics.

[67] I. Sutskever, J. Martens, and G. E. Hinton. Generating text with recurrent neural networks. In Proceedings of the 28th International Conference on Machine Learning (ICML-11) , pages 1017–1024, 2011.

[68] A. Radford, J. Wu, R. Child, D. Luan, D. Amodei, and I. Sutskever. Language models are unsupervised multitask learners. OpenAI Blog , 1(8), 2019.

[69] T. B. Brown, B. Mann, N. Ryder, M. Subbiah, J. Kaplan, P. Dhariwal, A. Neelakantan, P. Shyam, G. Sastry, A. Askell, S. Agarwal, A. Herbert-Voss, G. Krueger, T. Henighan, R. Child, A. Ramesh, D. M. Ziegler, J. Wu, C. Winter, C. Hesse, M. Chen, E. Sigler, M. Litwin, S. Gray, B. Chess, J. Clark, C. Berner, S. McCandlish, A. Radford, I. Sutskever, and D. Amodei. Language Models are Few-Shot Learners. In Advances in Neural Information Processing Systems , 2020.

[70] A. Lenci. Understanding natural language understanding systems. a critical analysis. Sistemi Intelligenti , 35(2):277–302, 2023.

[71] M. Van Schijndel and T. Linzen. Single-stage prediction models do not explain the magnitude of syntactic disambiguation difficulty. Cognitive Science , 45(6):e12988, 2021.

[72] G. Beguš. CiwGAN and fiwGAN: Encoding information in acoustic data to model lexical learning with generative adversarial networks. Neural Networks , 139:305–325, 2021.

[73] R. T. McCoy, P. Smolensky, T. Linzen, J. Gao, and A. Celikyilmaz. How much do language models copy from their training data? evaluating linguistic novelty in text generation using RAVEN. Transactions of the Association for Computational Linguistics , 11:652–670, 2023.

[74] G. Chronis and K. Erk. When is a bishop not like a rook? when it’s like a rabbi! multi-prototype BERT embeddings for estimating semantic relationships. In R. Fernández and T. Linzen, editors, Proceedings of the 24th Conference on Computational Natural Language Learning , pages 227–244, Online, November 2020. Association for Computational Linguistics.

[75] A. Wang, A. Singh, J. Michael, F. Hill, O. Levy, and S. R. Bowman. GLUE: A Multi-Task Benchmark and Analysis Platform for Natural Language Understanding. In Proceedings of the 2018 EMNLP Workshop BlackboxNLP: Analyzing and Interpreting Neural Networks for NLP , pages 353–355, 2018.

[76] A. Warstadt, A. Parrish, H. Liu, A. Mohananey, W. Peng, S.-F. Wang, and S. R. Bowman. BLiMP: The Benchmark of Linguistic Minimal Pairs for English. Transactions of the Association for Computational Linguistics , 8:377–392, 2020.

[77] D. Samuel. Mean BERTs make erratic language teachers: the effectiveness of latent bootstrapping in low-resource settings. In A. Warstadt, A. Mueller, L. Choshen, E. Wilcox, C. Zhuang, J. Ciro, R. Mosquera, B. Paranjabe, A. Williams, T. Linzen, and R. Cotterell, editors, Proceedings of the BabyLM Challenge at the 27th Conference on Computational Natural Language Learning , pages 221–237, Singapore, December 2023. Association for Computational Linguistics.

[78] A. Warstadt, A. Mueller, L. Choshen, E. Wilcox, C. Zhuang, J. Ciro, R. Mosquera, B. Paranjabe, A. Williams, T. Linzen, and R. Cotterell. Findings of the BabyLM challenge: Sample-efficient pretraining on developmentally plausible corpora. In A. Warstadt, A. Mueller, L. Choshen, E. Wilcox, C. Zhuang, J. Ciro, R. Mosquera, B. Paranjabe, A. Williams, T. Linzen, and R. Cotterell, editors, Proceedings of the BabyLM Challenge at the 27th Conference on Computational Natural Language Learning , pages 1–34, Singapore, December 2023. Association for Computational Linguistics.

[79] J. Gauthier, J. Hu, E. Wilcox, P. Qian, and R. Levy. SyntaxGym: An Online Platform for Targeted Evaluation of Language Models. In Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics: System Demonstrations , pages 70–76, Online, July 2020. Association for Computational Linguistics.

[80] T. Linzen, E. Dupoux, and Y. Goldberg. Assessing the ability of LSTMs to learn syntax-sensitive dependencies. Transactions of the Association for Computational Linguistics , 4:521–535, 2016.

[81] K. Gulordava, P. Bojanowski, E. Grave, T. Linzen, and M. Baroni. Colorless green recurrent networks dream hierarchically. In M. Walker, H. Ji, and A. Stent, editors, Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers) , pages 1195–1205, New Orleans, Louisiana, June 2018. Association for Computational Linguistics.

[82] T. Linzen and M. Baroni. Syntactic structure from deep learning. Annual Review of Linguistics , 7:195–212, 2021.

[83] C. Yu, R. Sie, N. Tedeschi, and L. Bergen. Word frequency does not predict grammatical knowledge in language models. In B. Webber, T. Cohn, Y. He, and Y. Liu, editors, Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP) , pages 4040–4054, Online, November 2020. Association for Computational Linguistics.

[84] E. G. Wilcox, R. Futrell, and R. Levy. Using computational models to test syntactic learnability. Linguistic Inquiry , pages 1–88, 2022.

[85] J. Hewitt and C. D. Manning. A structural probe for finding syntax in word representations. In J. Burstein, C. Doran, and T. Solorio, editors, Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers) , pages 4129–4138, Minneapolis, Minnesota, June 2019. Association for Computational Linguistics.

[86] S. Ravfogel, G. Prasad, T. Linzen, and Y. Goldberg. Counterfactual interventions reveal the causal effect of relative clause representations on agreement prediction. In A. Bisazza and O. Abend, editors, Proceedings of the 25th Conference on Computational Natural Language Learning , pages 194–209, Online, November 2021. Association for Computational Linguistics.

[87] A. Mueller, Y. Xia, and T. Linzen. Causal analysis of syntactic agreement neurons in multilingual language models. In A. Fokkens and V. Srikumar, editors, Proceedings of the 26th Conference on Computational Natural Language Learning (CoNLL) , pages 95–109, Abu Dhabi, United Arab Emirates (Hybrid), December 2022. Association for Computational Linguistics.

[88] Y. Lakretz, G. Kruszewski, T. Desbordes, D. Hupkes, S. Dehaene, and M. Baroni. The emergence of number and syntax units in LSTM language models. In J. Burstein, C. Doran, and T. Solorio, editors, Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers) , pages 11–20, Minneapolis, Minnesota, June 2019. Association for Computational Linguistics.

[89] B. Ambridge. Against stored abstractions: A radical exemplar model of language acquisition. First Language , 40(5-6):509–559, 2020.

[90] N. Kim and P. Smolensky. Testing for grammatical category abstraction in neural language models. In A. Ettinger, E. Pavlick, and B. Prickett, editors, Proceedings of the Society for Computation in Linguistics 2021 , pages 467–470, Online, February 2021. Association for Computational Linguistics.

[91] N. Kim, T. Linzen, and P. Smolensky. Uncontrolled lexical exposure leads to overestimation of compositional generalization in pretrained models. arXiv preprint arXiv:2212.10769 , 2022.

[92] K. Misra, J. Rayz, and A. Ettinger. COMPS: Conceptual minimal pair sentences for testing robust property knowledge and its inheritance in pre-trained language models. In A. Vlachos and I. Augenstein, editors, Proceedings of the 17th Conference of the European Chapter of the Association for Computational Linguistics , pages 2928–2949, Dubrovnik, Croatia, May 2023. Association for Computational Linguistics.

[93] A. Ettinger, A. Elgohary, and P. Resnik. Probing for semantic evidence of composition by means of simple classification tasks. In Proceedings of the 1st Workshop on Evaluating Vector-Space Representations for NLP , pages 134–139, Berlin, Germany, August 2016. Association for Computational Linguistics.

[94] Y. Belinkov. Probing classifiers: Promises, shortcomings, and advances. Computational Linguistics , 48(1):207–219, March 2022.

[95] I. Tenney, D. Das, and E. Pavlick. BERT rediscovers the classical NLP pipeline. In A. Korhonen, D. Traum, and L. Màrquez, editors, Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics , pages 4593–4601, Florence, Italy, July 2019. Association for Computational Linguistics.

[96] J. Niu, W. Lu, and G. Penn. Does BERT rediscover a classical NLP pipeline? In N. Calzolari, C.-R. Huang, H. Kim, J. Pustejovsky, L. Wanner, K.-S. Choi, P.-M. Ryu, H.-H. Chen, L. Donatelli, H. Ji, S. Kurohashi, P. Paggio, N. Xue, S. Kim, Y. Hahm, Z. He, T. K. Lee, E. Santus, F. Bond, and S.-H. Na, editors, Proceedings of the 29th International Conference on Computational Linguistics , pages 3143–3153, Gyeongju, Republic of Korea, October 2022. International Committee on Computational Linguistics.

[97] M. C. MacDonald, N. J. Pearlmutter, and M. S. Seidenberg. The lexical nature of syntactic ambiguity resolution. Psychological Review , 101(4):676, 1994. Publisher: American Psychological Association.

[98] E. Bates and B. MacWhinney. Functionalism and the competition model. In B. MacWhinney and E. Bates, editors, The Crosslinguistic Study of Sentence Processing , pages 3–73. Cambridge University Press, 1989.

[99] I. Dasgupta, A. K. Lampinen, S. C. Chan, A. Creswell, D. Kumaran, J. L. McClelland, and F. Hill. Language models show human-like content effects on reasoning. arXiv preprint arXiv:2207.07051 , 2022.

[100] A. K. Lampinen. Can language models handle recursively nested grammatical structures? a case study on comparing models and humans. arXiv preprint arXiv:2210.15303 , 2022.

[101] Y. Lakretz, T. Desbordes, D. Hupkes, and S. Dehaene. Causal Transformers Perform Below Chance on Recursive Nested Constructions, Unlike Humans, October 2021. arXiv:2110.07240 [cs].

[102] L. Weissweiler, T. He, N. Otani, D. R. Mortensen, L. Levin, and H. Schütze. Construction grammar provides unique insight into neural language models. In C. Bonial and H. Tayyar Madabushi, editors, Proceedings of the First International Workshop on Construction Grammars and NLP (CxGs+NLP, GURT/SyntaxFest 2023) , pages 85–95, Washington, D.C., March 2023. Association for Computational Linguistics.

[103] Y.-H. Tseng, C.-F. Shih, P.-E. Chen, H.-Y. Chou, M.-C. Ku, and S.-K. Hsieh. CxLM: A construction and context-aware language model. In N. Calzolari, F. Béchet, P. Blache, K. Choukri, C. Cieri, T. Declerck, S. Goggi, H. Isahara, B. Maegaard, J. Mariani, H. Mazo, J. Odijk, and S. Piperidis, editors, Proceedings of the Thirteenth Language Resources and Evaluation Conference , pages 6361–6369, Marseille, France, June 2022. European Language Resources Association.

[104] H. Tayyar Madabushi, L. Romain, D. Divjak, and P. Milin. CxGBERT: BERT meets construction grammar. In D. Scott, N. Bel, and C. Zong, editors, Proceedings of the 28th International Conference on Computational Linguistics , pages 4020–4032, Barcelona, Spain (Online), December 2020. International Committee on Computational Linguistics.

[105] K. Mahowald. A discerning several thousand judgments: GPT-3 rates the article + adjective + numeral + noun construction. In A. Vlachos and I. Augenstein, editors, Proceedings of the 17th Conference of the European Chapter of the Association for Computational Linguistics , pages 265–273, Dubrovnik, Croatia, May 2023. Association for Computational Linguistics.

[106] C. Potts. Characterizing English Preposing in PP constructions. LingBuzz , 2023. lingbuzz/007495.

[107] L. Weissweiler, V. Hofmann, A. Köksal, and H. Schütze. The better your syntax, the better your semantics? probing pretrained language models for the English comparative correlative. In Y. Goldberg, Z. Kozareva, and Y. Zhang, editors, Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing , pages 10859–10882, Abu Dhabi, United Arab Emirates, December 2022. Association for Computational Linguistics.

[108] E. Fedorenko, T. L. Scott, P. Brunner, W. G. Coon, B. Pritchett, G. Schalk, and N. Kanwisher. Neural correlate of the construction of sentence meaning. Proceedings of the National Academy of Sciences , 113(41):E6256–E6262, October 2016. Publisher: Proceedings of the National Academy of Sciences.

[109] C. Pallier, A.-D. Devauchelle, and S. Dehaene. Cortical representation of the constituent structure of sentences. Proceedings of the National Academy of Sciences , 108(6):2522–2527, February 2011. Publisher: Proceedings of the National Academy of Sciences.

[110] R. Law and L. Pylkkänen. Lists with and without syntax: A new approach to measuring the neural processing of syntax. Journal of Neuroscience , January 2021. Publisher: Society for Neuroscience Section: Research Articles.

[111] C. Shain, I. A. Blank, M. van Schijndel, W. Schuler, and E. Fedorenko. fMRI reveals language-specific predictive coding during naturalistic sentence comprehension. Neuropsychologia , 138:107307, 2020.

[112] J. R. Brennan, C. Dyer, A. Kuncoro, and J. T. Hale. Localizing syntactic predictions using recurrent neural network grammars. Neuropsychologia , 146:107479, September 2020.

[113] M. Heilbron, K. Armeni, J.-M. Schoffelen, P. Hagoort, and F. P. de Lange. A hierarchy of linguistic predictions during natural language comprehension. Proceedings of the National Academy of Sciences , 119(32):e2201968119, August 2022. Publisher: Proceedings of the National Academy of Sciences.

[114] A. J. Reddy and L. Wehbe. Can fMRI reveal the representation of syntactic structure in the brain? In M. Ranzato, A. Beygelzimer, Y. Dauphin, P. S. Liang, and J. W. Vaughan, editors, Advances in Neural Information Processing Systems , volume 34, pages 9843–9856. Curran Associates, Inc., 2021.

[115] J. Y. Huang, K.-H. Huang, and K.-W. Chang. Disentangling semantics and syntax in sentence embeddings with pre-trained language models. In K. Toutanova, A. Rumshisky, L. Zettlemoyer, D. Hakkani-Tur, I. Beltagy, S. Bethard, R. Cotterell, T. Chakraborty, and Y. Zhou, editors, Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies , pages 1372–1379, Online, June 2021. Association for Computational Linguistics.

[116] C. Caucheteux and J.-R. King. Brains and algorithms partially converge in natural language processing. Communications Biology , 5(1):1–10, February 2022. Number: 1 Publisher: Nature Publishing Group.

[117] A. Goldstein, Z. Zada, E. Buchnik, M. Schain, A. Price, B. Aubrey, S. A. Nastase, A. Feder, D. Emanuel, A. Cohen, A. Jansen, H. Gazula, G. Choe, A. Rao, C. Kim, C. Casto, L. Fanda, W. Doyle, D. Friedman, P. Dugan, L. Melloni, R. Reichart, S. Devore, A. Flinker, L. Hasenfratz, O. Levy, A. Hassidim, M. Brenner, Y. Matias, K. A. Norman, O. Devinsky, and U. Hasson. Shared computational principles for language processing in humans and deep language models. Nature Neuroscience , 25(3):369–380, March 2022. Number: 3 Publisher: Nature Publishing Group.

[118] M. Schrimpf, I. A. Blank, G. Tuckute, C. Kauf, E. A. Hosseini, N. Kanwisher, J. B. Tenenbaum, and E. Fedorenko. The neural architecture of language: Integrative modeling converges on predictive processing. Proceedings of the National Academy of Sciences , 118(45), November 2021. Publisher: National Academy of Sciences Section: Biological Sciences.

[119] E. J. Michaud, Z. Liu, U. Girit, and M. Tegmark. The quantization model of neural scaling. Proceedings of the NeurIPS Conference , 2023.

[120] S. T. Piantadosi. Modern language models refute Chomsky’s approach to language. Lingbuzz Preprint, lingbuzz/007180 , 2023.

[121] N. Chomsky. Linguistics and cognitive science: problems and mysteries. In The Chomskyan Turn . Blackwell, Oxford, UK, 1991.

[122] T. McCoy, E. Pavlick, and T. Linzen. Right for the wrong reasons: Diagnosing syntactic heuristics in natural language inference. In A. Korhonen, D. Traum, and L. Màrquez, editors, Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics , pages 3428–3448, Florence, Italy, July 2019. Association for Computational Linguistics.

[123] R. T. McCoy, S. Yao, D. Friedman, M. Hardy, and T. L. Griffiths. Embers of autoregression: Understanding large language models through the problem they are trained to solve. arXiv preprint arXiv:2309.13638 , 2023.

[124] N. Kassner and H. Schütze. Negated and misprimed probes for pretrained language models: Birds can talk, but cannot fly. In D. Jurafsky, J. Chai, N. Schluter, and J. Tetreault, editors, Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics , pages 7811–7818, Online, July 2020. Association for Computational Linguistics.

[125] A. Warstadt and S. R. Bowman. What artificial neural networks can tell us about human language acquisition. Algebraic Structures in Natural Language , pages 17–60, 2022.

[126] M. van Schijndel, A. Mueller, and T. Linzen. Quantity doesn’t buy quality syntax with neural language models. In K. Inui, J. Jiang, V. Ng, and X. Wan, editors, Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP) , pages 5831–5837, Hong Kong, China, November 2019. Association for Computational Linguistics.

[127] R. T. McCoy, R. Frank, and T. Linzen. Does syntax need to grow on trees? sources of hierarchical inductive bias in sequence-to-sequence networks. Transactions of the Association for Computational Linguistics , 8:125–140, 2020.

[128] A. Yedetore, T. Linzen, R. Frank, and R. T. McCoy. How poor is the stimulus? evaluating hierarchical generalization in neural networks trained on child-directed speech. In A. Rogers, J. Boyd-Graber, and N. Okazaki, editors, Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , pages 9370–9393, Toronto, Canada, July 2023. Association for Computational Linguistics.

[129] L. Georges Gabriel Charpentier and D. Samuel. Not all layers are equally as important: Every layer counts BERT. In A. Warstadt, A. Mueller, L. Choshen, E. Wilcox, C. Zhuang, J. Ciro, R. Mosquera, B. Paranjabe, A. Williams, T. Linzen, and R. Cotterell, editors, Proceedings of the BabyLM Challenge at the 27th Conference on Computational Natural Language Learning , pages 238–252, Singapore, December 2023. Association for Computational Linguistics.

[130] E. A. Hosseini, M. Schrimpf, Y. Zhang, S. R. Bowman, N. Zaslavsky, and E. Fedorenko. Artificial neural network language models predict human brain responses to language even after a developmentally realistic amount of training. Neurobiology of Language , pages 1–50, 01 2024.

[131] D. Blasi, A. Anastasopoulos, and G. Neubig. Systematic inequalities in language technology performance across the world’s languages. In S. Muresan, P. Nakov, and A. Villavicencio, editors, Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , pages 5486–5505, Dublin, Ireland, May 2022. Association for Computational Linguistics.

[132] S. J. Mielke, R. Cotterell, K. Gorman, B. Roark, and J. Eisner. What kind of language is hard to language-model? In A. Korhonen, D. Traum, and L. Màrquez, editors, Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics , pages 4975–4989, Florence, Italy, July 2019. Association for Computational Linguistics.

[133] L. Martin, B. Muller, P. J. Ortiz Suárez, Y. Dupont, L. Romary, É. de la Clergerie, D. Seddah, and B. Sagot. CamemBERT: a tasty French language model. In D. Jurafsky, J. Chai, N. Schluter, and J. Tetreault, editors, Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics , pages 7203–7219, Online, July 2020. Association for Computational Linguistics.

[134] Z. Wang, K. K, S. Mayhew, and D. Roth. Extending multilingual BERT to low-resource languages. In T. Cohn, Y. He, and Y. Liu, editors, Findings of the Association for Computational Linguistics: EMNLP 2020 , pages 2649–2656, Online, November 2020. Association for Computational Linguistics.

[135] K. Tirumala, A. Markosyan, L. Zettlemoyer, and A. Aghajanyan. Memorization without overfitting: Analyzing the training dynamics of large language models. Advances in Neural Information Processing Systems , 35:38274–38290, 2022.

[136] D. C. Dennett. The role of language in intelligence. In What is Intelligence? The Darwin College Lectures, ed. Jean Khalfa, Cambridge University Press, Cambridge, UK, 1994.

[137] P. Carruthers. The cognitive functions of language. The Behavioral and Brain Sciences , 25(6):657–674; discussion 674–725, December 2002.

[138] J. Duncan. The multiple-demand (MD) system of the primate brain: mental programs for intelligent behaviour. Trends in Cognitive Sciences , 14(4):172–179, April 2010.

[139] J. Fischer, J. G. Mikhael, J. B. Tenenbaum, and N. Kanwisher. Functional neuroanatomy of intuitive physical inference. Proceedings of the National Academy of Sciences , 113(34):E5072–E5081, August 2016.

[140] A. A. Ivanova, S. Srikant, Y. Sueoka, H. H. Kean, R. Dhamala, U.-M. O’reilly, M. U. Bers, and E. Fedorenko. Comprehension of computer code relies primarily on domain-general executive brain regions. eLife , 9:e58906, 2020.

[141] A. Woolgar, A. Parr, R. Cusack, R. Thompson, I. Nimmo-Smith, T. Torralva, M. Roca, N. Antoun, F. Manes, and J. Duncan. Fluid intelligence loss linked to restricted regions of damage within frontal and parietal cortex. Proceedings of the National Academy of Sciences , 107(33):14899–14902, August 2010. ISBN: 9781007928108 Publisher: National Academy of Sciences Section: Biological Sciences.

[142] A. Woolgar, J. Duncan, F. Manes, and E. Fedorenko. Fluid intelligence is supported by the multiple-demand system not the language system. Nature Human Behaviour , 2(3):200–204, 2018.

[143] N. Dziri, X. Lu, M. Sclar, X. L. Li, L. Jiang, B. Y. Lin, S. Welleck, P. West, C. Bhagavatula, R. L. Bras, J. D. Hwang, S. Sanyal, X. Ren, A. Ettinger, Z. Harchaoui, and Y. Choi. Faith and fate: Limits of transformers on compositionality. In Thirty-seventh Conference on Neural Information Processing Systems , 2023.

[144] K. Valmeekam, A. Olmo, S. Sreedharan, and S. Kambhampati. Large language models still can’t plan (a benchmark for llms on planning and reasoning about change). In NeurIPS 2022 Foundation Models for Decision Making Workshop , 2022.

[145] Z. Wu, L. Qiu, A. Ross, E. Akyürek, B. Chen, B. Wang, N. Kim, J. Andreas, and Y. Kim. Reasoning or reciting? exploring the capabilities and limitations of language models through counterfactual tasks. arXiv preprint arXiv:2307.02477 , 2023.

[146] H. Zhang, L. H. Li, T. Meng, K.-W. Chang, and G. Van den Broeck. On the paradox of learning to reason from data. In E. Elkind, editor, Proceedings of the Thirty-Second International Joint Conference on Artificial Intelligence, IJCAI-23 , pages 3365–3373. International Joint Conferences on Artificial Intelligence Organization, 8 2023. Main Track.

[147] J. Wei, X. Wang, D. Schuurmans, M. Bosma, F. Xia, E. Chi, Q. V. Le, D. Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models. Advances in Neural Information Processing Systems , 35:24824–24837, 2022.

[148] Wolfram. Wolfram plugin for chatgpt. https://www.wolfram.com/wolfram-plugin-chatgpt/ , 2023. Accessed: January 1, 2024.

[149] L. Wong, G. Grand, A. K. Lew, N. D. Goodman, V. K. Mansinghka, J. Andreas, and J. B. Tenenbaum. From word models to world models: Translating from natural language to the probabilistic language of thought. arXiv preprint arXiv:2306.12672 , 2023.

[150] I. Yildirim and L. Paul. From task structures to world models: What do LLMs know? arXiv preprint arXiv:2310.04276 , 2023.

[151] A. A. Ivanova, Z. Mineroff, V. Zimmerer, N. Kanwisher, R. Varley, and E. Fedorenko. The Language Network is Recruited but Not Required for Nonverbal Event Semantics. Neurobiology of Language , pages 1–26, January 2021. Publisher: MIT Press.

[152] K. Patterson, P. J. Nestor, and T. T. Rogers. Where do you know what you know? The representation of semantic knowledge in the human brain. Nature Reviews. Neuroscience , 8(12):976–987, December 2007.

[153] G. Grand, I. A. Blank, F. Pereira, and E. Fedorenko. Semantic projection recovers rich human knowledge of multiple object features from word embeddings. Nature Human Behaviour , 6(7):975–987, 2022.

[154] F. Petroni, T. Rocktäschel, S. Riedel, P. Lewis, A. Bakhtin, Y. Wu, and A. Miller. Language Models as Knowledge Bases? In Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP) , pages 2463–2473, Hong Kong, China, November 2019. Association for Computational Linguistics.

[155] N. Liu, T. Zhang, and P. Liang. Evaluating verifiability in generative search engines. In H. Bouamor, J. Pino, and K. Bali, editors, Findings of the Association for Computational Linguistics: EMNLP 2023 , pages 7001–7025, Singapore, December 2023. Association for Computational Linguistics.

[156] M. Sclar, Y. Choi, Y. Tsvetkov, and A. Suhr. Quantifying language models’ sensitivity to spurious features in prompt design or: How I learned to start worrying about prompt formatting. arXiv preprint arXiv:2310.11324 , 2023.

[157] J. Gordon and B. Van Durme. Reporting bias and knowledge acquisition. In Proceedings of the 2013 workshop on Automated knowledge base construction , pages 25–30, 2013.

[158] X. Liu, D. Yin, Y. Feng, and D. Zhao. Things not written in text: Exploring spatial commonsense from visual signals. In S. Muresan, P. Nakov, and A. Villavicencio, editors, Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , pages 2365–2376, Dublin, Ireland, May 2022. Association for Computational Linguistics.

[159] Y. Kim, J. Yoon, S. Ye, S. J. Hwang, and S.-Y. Yun. Carpe diem: On the evaluation of world knowledge in lifelong language models. In NeurIPS 2023 Workshop on Synthetic Data Generation with Generative AI , 2023.

[160] K. Meng, D. Bau, A. Andonian, and Y. Belinkov. Locating and editing factual associations in gpt. Advances in Neural Information Processing Systems , 35:17359–17372, 2022.

[161] S. Borgeaud, A. Mensch, J. Hoffmann, T. Cai, E. Rutherford, K. Millican, G. B. Van Den Driessche, J.-B. Lespiau, B. Damoc, A. Clark, et al. Improving language models by retrieving from trillions of tokens. In International conference on machine learning , pages 2206–2240. PMLR, 2022.

[162] R. Cohen, M. Geva, J. Berant, and A. Globerson. Crawling the internal knowledge-base of language models. In A. Vlachos and I. Augenstein, editors, Findings of the Association for Computational Linguistics: EACL 2023 , pages 1856–1869, Dubrovnik, Croatia, May 2023. Association for Computational Linguistics.

[163] E. Chersoni, E. Santus, L. Pannitto, A. Lenci, P. Blache, and C.-R. Huang. A structured distributional model of sentence meaning and processing. Natural Language Engineering , 25(4):483–502, 2019.

[164] T. A. Van Dijk and W. Kintsch. Strategies of Discourse Comprehension . Academic Press: New York, 1983.

[165] Y. Lerner, C. J. Honey, L. J. Silbert, and U. Hasson. Topographic Mapping of a Hierarchy of Temporal Receptive Windows Using a Narrated Story. The Journal of Neuroscience , 31(8):2906–2915, February 2011.

[166] N. Jacoby and E. Fedorenko. Discourse-level comprehension engages medial frontal Theory of Mind brain regions even for expository texts. Language, Cognition and Neuroscience , 35(6):780–796, July 2020. Publisher: Routledge _eprint: https://doi.org/10.1080/23273798.2018.1525494.

[167] R. L. Buckner and L. M. DiNicola. The brain’s default network: Updated anatomy, physiology and evolving insights. Nature Reviews Neuroscience , 20(10):593–608, 2019. Place: United Kingdom Publisher: Nature Publishing Group.

[168] C. Baldassano, J. Chen, A. Zadbood, J. W. Pillow, U. Hasson, and K. A. Norman. Discovering Event Structure in Continuous Narrative Perception and Memory. Neuron , 95(3):709–721.e5, August 2017.

[169] J. Su, M. Ahmed, Y. Lu, S. Pan, W. Bo, and Y. Liu. Roformer: Enhanced transformer with rotary position embedding. Neurocomputing , 568:127063, 2024.

[170] D. S. Moirangthem and M. Lee. Abstractive summarization of long texts by representing multiple compositionalities with temporal hierarchical pointer generator network. Neural Networks , 124:1–11, 2020.

[171] Q. Ruan, M. Ostendorff, and G. Rehm. HiStruct+: Improving extractive text summarization with hierarchical structure information. In S. Muresan, P. Nakov, and A. Villavicencio, editors, Findings of the Association for Computational Linguistics: ACL 2022 , pages 1292–1308, Dublin, Ireland, May 2022. Association for Computational Linguistics.

[172] N. Kim and S. Schuster. Entity tracking in language models. In A. Rogers, J. Boyd-Graber, and N. Okazaki, editors, Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , pages 3835–3855, Toronto, Canada, July 2023. Association for Computational Linguistics.

[173] S. Schuster and T. Linzen. When a sentence does not introduce a discourse entity, transformer-based models still sometimes refer to it. In M. Carpuat, M.-C. de Marneffe, and I. V. Meza Ruiz, editors, Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies , pages 969–982, Seattle, United States, July 2022. Association for Computational Linguistics.

[174] C. Andrés-Roqueta and N. Katsos. The Contribution of Grammar, Vocabulary and Theory of Mind in Pragmatic Language Competence in Children with Autistic Spectrum Disorders. Frontiers in Psychology , 8, 2017.

[175] S. Levinson. Presumptive Meanings: The Theory of Generalized Conversational Implicature . MIT Press, Cambridge, MA, 2000.

[176] M. Hauptman, I. Blank, and E. Fedorenko. Non-literal language processing is jointly supported by the language and theory of mind networks: Evidence from a novel meta-analytic fmri approach. Cortex , 162:96–114, 2023.

[177] R. Saxe. Uniquely human social cognition. Current Opinion in Neurobiology , 16(2):235–239, April 2006.

[178] A. Gopnik and H. M. Wellman. Why the child’s theory of mind really is a theory. Mind and Language , 7(1-2):145–71, 1992.

[179] R. Saxe and N. Kanwisher. People thinking about thinking people. The role of the temporo-parietal junction in "theory of mind". NeuroImage , 19(4):1835–1842, August 2003.

[180] N. Jacoby, E. Bruneau, J. Koster-Hale, and R. Saxe. Localizing Pain Matrix and Theory of Mind networks with both verbal and non-verbal stimuli. NeuroImage , 126:39–48, February 2016.

[181] E. C. Ferstl and D. Y. von Cramon. What Does the Frontomedian Cortex Contribute to Language Processing: Coherence or Theory of Mind? NeuroImage , 17(3):1599–1612, November 2002.

[182] R. Saxe and L. J. Powell. It’s the thought that counts: specific brain regions for one component of theory of mind. Psychological Science , 17(8):692–699, August 2006.

[183] P. Hagoort and S. C. Levinson. Neuropragmatics. In The cognitive neurosciences, 5th ed , pages 667–674. MIT Press, Cambridge, MA, US, 2014.

[184] J. Hu, S. Floyd, O. Jouravlev, E. Fedorenko, and E. Gibson. A fine-grained comparison of pragmatic language understanding in humans and language models. In A. Rogers, J. Boyd-Graber, and N. Okazaki, editors, Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , pages 4194–4213, Toronto, Canada, July 2023. Association for Computational Linguistics.

[185] M. Kosinski. Theory of mind may have spontaneously emerged in large language models. arXiv preprint arXiv:2302.02083 , 2023.

[186] T. Ullman. Large language models fail on trivial alterations to theory-of-mind tasks. arXiv preprint arXiv:2302.08399 , 2023.

[187] N. Shapira, M. Levy, S. H. Alavi, X. Zhou, Y. Choi, Y. Goldberg, M. Sap, and V. Shwartz. Clever hans or neural theory of mind? stress testing social reasoning in large language models. arXiv preprint arXiv:2305.14763 , 2023.

[188] M. Sap, R. Le Bras, D. Fried, and Y. Choi. Neural theory-of-mind? on the limits of social intelligence in large LMs. In Y. Goldberg, Z. Kozareva, and Y. Zhang, editors, Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing , pages 3762–3780, Abu Dhabi, United Arab Emirates, December 2022. Association for Computational Linguistics.

[189] S. Trott, C. Jones, T. Chang, J. Michaelov, and B. Bergen. Do large language models know what humans know? Cognitive Science , 47(7):e13309, 2023.

[190] K. Gandhi, J.-P. Fränken, T. Gerstenberg, and N. Goodman. Understanding social reasoning in language models with language models. In Thirty-seventh Conference on Neural Information Processing Systems Datasets and Benchmarks Track , 2023.

[191] M. Sclar, S. Kumar, P. West, A. Suhr, Y. Choi, and Y. Tsvetkov. Minding language models’ (lack of) theory of mind: A plug-and-play multi-character belief tracker. In A. Rogers, J. Boyd-Graber, and N. Okazaki, editors, Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , pages 13960–13980, Toronto, Canada, July 2023. Association for Computational Linguistics.

[192] S. R. Waxman. Early word-learning and conceptual development: Everything had a name, and each name gave birth to a new thought. Blackwell Handbook of Childhood Cognitive Development , pages 102–126, 2002.

[193] J. E. Pyers and A. Senghas. Language promotes false-belief understanding: Evidence from learners of a new sign language. Psychological science , 20(7):805–812, 2009.

[194] B. Pitt, E. Gibson, and S. T. Piantadosi. Exact number concepts are limited to the verbal count range. Psychological Science , 33(3):371–381, 2022.

[195] L. Bottou and P. Gallinari. A framework for the cooperation of learning algorithms. Advances in neural information processing systems , 3, 1990.

[196] E. Ronco and P. J. Gawthrop. Neural networks for modelling and control. Rapport Technique csc , 97008, 1997.

[197] Q. Liu, D. Yogatama, and P. Blunsom. Relational Memory-Augmented Language Models. Transactions of the Association for Computational Linguistics , 10:555–572, May 2022.

[198] J. Mao, C. Gan, P. Kohli, J. B. Tenenbaum, and J. Wu. The neuro-symbolic concept learner: Interpreting scenes, words, and sentences from natural supervision. In International Conference on Learning Representations , 2019.

[199] D. Hudson and C. D. Manning. Learning by abstraction: The neural state machine. In Advances in Neural Information Processing Systems , pages 5901–5914, 2019.

[200] T. Schick, J. Dwivedi-Yu, R. Dessì, R. Raileanu, M. Lomeli, L. Zettlemoyer, N. Cancedda, and T. Scialom. Toolformer: Language models can teach themselves to use tools. arXiv preprint arXiv:2302.04761 , 2023.

[201] K. Cobbe, V. Kosaraju, M. Bavarian, M. Chen, H. Jun, L. Kaiser, M. Plappert, J. Tworek, J. Hilton, R. Nakano, et al. Training verifiers to solve math word problems. arXiv preprint arXiv:2110.14168 , 2021.

[202] B. Liu, Y. Jiang, X. Zhang, Q. Liu, S. Zhang, J. Biswas, and P. Stone. LLM+P: Empowering large language models with optimal planning proficiency. arXiv preprint arXiv:2304.11477 , 2023.

[203] G. R. Yang, M. R. Joglekar, H. F. Song, W. T. Newsome, and X.-J. Wang. Task representations in neural networks trained to perform many cognitive tasks. Nature Neuroscience , 22(2):297–306, February 2019. Number: 2 Publisher: Nature Publishing Group.

[204] K. Dobs, J. Martinez, A. J. E. Kell, and N. Kanwisher. Brain-like functional specialization emerges spontaneously in deep neural networks. Science Advances , 8(11):eabl8913, March 2022.

[205] C. D. Manning, K. Clark, J. Hewitt, U. Khandelwal, and O. Levy. Emergent linguistic structure in artificial neural networks trained by self-supervision. Proceedings of the National Academy of Sciences , 117(48):30046–30054, December 2020.

[206] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, \. Kaiser, and I. Polosukhin. Attention is All you Need. In I. Guyon, U. V. Luxburg, S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan, and R. Garnett, editors, Advances in Neural Information Processing Systems 30 , pages 5998–6008. Curran Associates, Inc., 2017.

[207] J. Vig and Y. Belinkov. Analyzing the structure of attention in a transformer language model. In T. Linzen, G. Chrupała, Y. Belinkov, and D. Hupkes, editors, Proceedings of the 2019 ACL Workshop BlackboxNLP: Analyzing and Interpreting Neural Networks for NLP , pages 63–76, Florence, Italy, August 2019. Association for Computational Linguistics.

[208] A. Goyal, A. Didolkar, A. Lamb, K. Badola, N. R. Ke, N. Rahaman, J. Binas, C. Blundell, M. Mozer, and Y. Bengio. Coordination among neural modules through a shared global workspace. Proceedings of ICLR , 2022.

[209] S. Kudugunta, Y. Huang, A. Bapna, M. Krikun, D. Lepikhin, M.-T. Luong, and O. Firat. Beyond distillation: Task-level mixture-of-experts for efficient inference. In M.-F. Moens, X. Huang, L. Specia, and S. W.-t. Yih, editors, Findings of the Association for Computational Linguistics: EMNLP 2021 , pages 3577–3599, Punta Cana, Dominican Republic, November 2021. Association for Computational Linguistics.

[210] Y. Zhou, T. Lei, H. Liu, N. Du, Y. Huang, V. Zhao, A. M. Dai, Q. V. Le, J. Laudon, et al. Mixture-of-experts with expert choice routing. Advances in Neural Information Processing Systems , 35:7103–7114, 2022.

[211] K. Sakaguchi, R. Le Bras, C. Bhagavatula, and Y. Choi. Winogrande: An adversarial winograd schema challenge at scale. In Proceedings of the AAAI Conference on Artificial Intelligence , volume 34, pages 8732–8740, 2020.

[212] Y. Elazar, H. Zhang, Y. Goldberg, and D. Roth. Back to square one: Artifact detection, training and commonsense disentanglement in the Winograd schema. In M.-F. Moens, X. Huang, L. Specia, and S. W.-t. Yih, editors, Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing , pages 10486–10500, Online and Punta Cana, Dominican Republic, November 2021. Association for Computational Linguistics.

[213] J. Kaplan, S. McCandlish, T. Henighan, T. B. Brown, B. Chess, R. Child, S. Gray, A. Radford, J. Wu, and D. Amodei. Scaling laws for neural language models. arXiv preprint arXiv:2001.08361 , 2020.

[214] E. Yiu, E. Kosoy, and A. Gopnik. Transmission versus truth, imitation versus innovation: What children can do that large language and language-and-vision models cannot (yet). Perspectives on Psychological Science , page 17456916231201401, 2023.

[215] H. Lederman and K. Mahowald. Are language models more like libraries or like librarians? Bibliotechnism, the Novel Reference Problem, and the attitudes of LLMs. arXiv preprint arXiv:2401.04854 , 2024.

[216] M. Mitchell and D. C. Krakauer. The debate over understanding in AI’s large language models. Proceedings of the National Academy of Sciences , 120(13):e2215907120, 2023.

[217] E. Pavlick. Symbols and grounding in large language models. Philosophical Transactions of the Royal Society A , 381(2251):20220041, 2023.

[218] D. C. Mollo and R. Millière. The vector grounding problem. arXiv preprint arXiv:2304.01481 , 2023.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
