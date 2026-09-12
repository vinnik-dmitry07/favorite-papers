This is how the Neocortex Learns
Randall C. O'Reilly
Astera Institute; Department of Psychology
Center for Neuroscience, University of California Davis
correspondence: oreilly@ucdavis.edu
June 7, 2026, Version: 1
https.//compcogneuro.org/oreilly-2026-cortlearn
Abstract:
A sufficient account of how the neocortex learns must meet three criteria: 1. Computationally, it must 
approximate a powerful, general-purpose learning algorithm known to scale to human-level intelligence; 2. 
Algorithmically, it must be implementable using known, well-established neural circuits within the 
neocortex and associated brain structures; 3. Implementationally, there must be a detailed account for how 
all of the algorithmic mechanisms actually function at a neurochemical level. At present, there is only one 
framework that meets all of these criteria: error-driven predictive learning via temporal derivatives, driven 
by corticothalamic circuits, based on competitive kinase synaptic plasticity induction mechanisms. This has 
been implemented in the Axon neural simulation framework using spiking neurons, and demonstrated to 
learn across a wide range of challenging cognitively motivated tasks.
Introduction
Understanding how the neocortex learns is perhaps the single most important step in understanding human 
intelligence, because our cognitive functions emerge over years of experience-driven learning within this 
brain structure, which is unique to mammals and is most greatly expanded in primates, especially humans. 
Following Marr (1982), there are three levels at which any theory of neocortical learning can be evaluated: 
computational, algorithmic, and implementational. The deliberately provocative conclusion of this paper is 
that only one current theory, which we label the temporal derivative model (Jang et al., 2026), provides a 
sufficient account across these three levels, and thus represents the most viable working hypothesis for how 
the neocortex learns.
Computational
Is there a mathematically proven basis for understanding why the neocortical learning mechanism should 
be capable in principle of accomplishing human-level intelligence through experience-driven learning? 
Have implementations of this learning mechanism actually demonstrated this capacity? There is only one 
learning mechanism that meets this criterion: error backpropagation (Rumelhart et al., 1986; Widrow & 
Hoff, 1960; Werbos, 1974), which drives learning in modern-day large-language models (LLMs) based on 
the transformer architecture (Vaswani et al., 2017), along with essentially every other type of modern 
powerful neural network model. This is essentially an open-and-shut case at this point: nothing else even 
comes close.

This is how the Neocortex Learns 2
There have been many proposals for ways of augmenting, simplifying, or approximating error 
backpropagation, but in practice, nothing else has managed to dethrone the stochastic gradient descent 
(SGD) procedure, which remains the effectively universal standard for current state-of-the-art (SOTA) 
models. Furthermore, gradient descent can also be applied to more complex probabilistic models through 
the variational inference approach (Blei et al., 2017), reinforcing the idea that this is perhaps a uniquely 
efficient way to search through combinatorially large parameter spaces. Recent work provides a more 
general overarching framework for understanding all of these gradient-based learning mechanisms (Khan 
& Rue, 2023; Vastola et al., 2026).
Since the skeptical publication of Crick (1989), there has been a widespread and persistent belief among 
many scientists that error backpropagation is fundamentally incompatible with the biology of the brain. 
However, in fact there are various longstanding proposals that show how the brain could accomplish 
backpropagation, which we discuss next.
Algorithmic
Can the computational-level mechanism be implemented algorithmically in a way that is in principle 
compatible with known neurobiological mechanisms, at the circuit and structural level? There have been 
various proposals for how to implement error backpropagation using known neocortical circuits (see 
Lillicrap et al., 2020 for a recent review, and Discussion below for more details), but only one provides a 
comprehensive fit with known neocortical (and thalamocortical) properties, while also satisfying the final 
implementational criterion described next.
The temporal derivative algorithm is based on the representation of the backpropagated error gradient 
implicitly as the temporal derivative (difference) between two distinct activation states that emerge over 
time (Figure 1), instead of requiring a distinct population of neurons to explicitly represent the gradient in 
terms of their firing rates. The idea of using two different states or phases of neural activity to compute 
error gradients originated with the Boltzmann Machine (Ackley et al., 1985), and a direct derivation from 
the error backpropagation formalism was first provided by the GeneRec (Generalized Recirculation) 
algorithm (O’Reilly, 1996), which generalized the original Recirculation model of Hinton & McClelland 
(1988). Other derivations were subsequently developed (Xie & Seung, 2003; Scellier & Bengio, 2017).
By representing the error gradient implicitly as a difference between two activation states, this algorithm 
avoids the significant additional complexity required for maintaining two distinct populations of neurons 
coding for the feedforward activity and the backpropagated error signal, with a third distinct population 
representing their difference. Instead, under this temporal derivative framework, all of the neurons in the 
neocortex are always encoding a positive, mutually compatible representation of the current state, through 
bidirectional excitatory connections that are a well-established and relatively unique property of the 
neocortex (Markov et al., 2013; Van Essen & Maunsell, 1983). In one phase, this current state reflects a 
prediction, which is then followed by an outcome that may differ from the prior prediction, with any 
difference in corresponding activation states throughout the network providing a close approximation to the 
error gradient between outcome and prediction.

This is how the Neocortex Learns 3
Figure 1: How bidirectional activation propagation can communicate error signals, in the simplest case of 
a three-layer network mapping from a Sensory Input to a Prediction output, with the Actual Outcome 
driving the Prediction layer only in the later plus phase, after an initial minus phase when the prediction is 
generated. The Error is the temporal difference between the (plus – minus) activity levels. There is just one 
network with three bidirectionally connected units, as shown at the left; the networks shown further to the 
right are snapshots of the activity state of this network at different points in time, which evolves from left 
to right. The thick colored lines also show the activation level of each of the three neurons over time, both 
in terms of the line height and the brightness and warmth of the color gradient. Initially, each neuron is 
inactive (blue). Then, external Sensory Input arrives, and a wave of bottom-up excitation propagates 
upward through the Hidden and Prediction layers. Critically, the Prediction and Hidden neurons mutually 
excite each other via bidirectional connections, which contributes to each of their activity levels. The 
snapshot of the network in the middle shows the neural activity at the end of the minus phase. Then, at the 
start of the plus phase, the Actual Outcome arrives, which is more active than the Prediction, and it 
therefore drives more activity in the Prediction neuron. This propagates top-down to the Hidden neuron as 
well, which is the key mechanism by which bidirectional connectivity communicates error signals, causing 
the Hidden neuron to have a (plus – minus) activity difference, reflecting the top-down influence from the 
Prediction layer. This temporal-difference based Error signal provides a good approximation to the error 
backpropagation error gradient (O’Reilly, 1996).

This is how the Neocortex Learns 4
Figure 2: Connectivity between the neocortex and the pulvinar nucleus of the thalamus, in the case of 
primary and secondary visual areas, that is uniquely well-suited for driving predictive error-driven learning. 
The numerous and relatively weaker projections from layer 6 (VI) neurons activate a prediction over the 
pulvinar, that integrates the signals from multiple cortical areas and neurons to synthesize the prediction, 
which improves over the course of learning throughout the neocortex and in these final projections into the 
pulvinar. By contrast, the strong, focal driver inputs from layer 5 (V) intrinsic bursting (5IB) neurons can 
activate an outcome representation that is essentially an unlearned copy of the activity pattern in lower 
cortical layers (e.g., V1 trains V2 predictions in this case). The periodic bursting of the 5IB neurons ensures 
that this outcome activity is only phasically present (i.e., the plus phase), with a complete prediction – 
outcome learning cycle occurring within roughly 200 ms (i.e., theta frequency, 5 Hz). Diagram based on 
Sherman & Guillery (2006).

The thalamocortical connectivity of the neocortex directly supports the generation of these two states, within 
an overall predictive learning framework, which is learning to predict what happens next based on what just 
happened (O’Reilly et al., 2021). Specifically, thalamic relay cells (TRCs) in the higher-order pulvinar (for 
posterior cortex) and mediodorsal (for frontal cortex) nuclei of the thalamus receive two distinct inputs 
(Figure 2; Sherman & Guillery, 2006; Usrey & Sherman, 2018):
1. A large number of normal-strength inputs onto more distal dendritic arbors from a wide range of higher-
level neocortical brain areas.
2. A much smaller number (even just one) of abnormally strong driver inputs originating from the layer 5b 
intrinsic bursting (5IB) neurons in hierarchically lower neocortical areas, which burst roughly every 
100-200 ms (i.e., at the alpha or theta rhythm), and are otherwise inactive.
This constellation of properties creates phasic alternations between a prediction state driven exclusively by 
the first pathway, and an outcome state that reflects the strong impact of the driver inputs, which only 
occurs phasically. Critically, the pulvinar neurons do not compute the difference between these two inputs 
and send that as their output, instead they merely reflect these two different inputs in their activity levels 
across time.
The TRCs send extensive excitatory reciprocal projections back to the same areas that send the prediction-
generating inputs, thereby communicating the temporal difference between the prediction and outcome 
states back into the neocortex, where local synaptic plasticity is driven by this temporal derivative. 
Furthermore, bidirectional connectivity within the neocortex effectively computes the partial derivative of 
these error signals relative to sending neural activity coming from other areas, thereby accomplishing the 
critical error backpropagation credit assignment learning process between neocortical layers (O’Reilly, 
1996).

This is how the Neocortex Learns 5
There is a wealth of detailed neuroscience data that is consistent with this overall framework, as reviewed 
in O’Reilly et al. (2021) (e.g., Fiebelkorn & Kastner, 2021; Sherman & Guillery, 2006; Sherman & Usrey, 
2024).
Implementational
Going down a level of neurobiological detail, how could the algorithmic property of a temporal derivative 
between prediction and outcome states actually drive synaptic plasticity locally at all of the neocortical and 
thalamic synapses? Mathematically, the temporal derivative can be computed as the difference between fast 
minus slow integrals of a common driving input signal. Intuitively, the fast integral more closely reflects 
the more recent outcome state, while the slow integral still retains more of the trace from the earlier 
prediction state. See temporal derivative on compcogneuro.org for an interactive demonstration of this 
principle.
Neurochemically, the difference between LTP (long term potentiation, i.e., synaptic weight increase) versus 
LTD (long term depression, weight decrease) is determined in part by a competition between two different 
kinases, CaMKII (calcium calmodulin kinase II) and DAPK1 (death-associated protein kinase 1), both of 
which are driven by calcium-activated calmodulin (CaM) (Goodell et al., 2017; Goodell et al., 2021; Cook 
et al., 2021; Tullis & Bayer, 2023; Bayer & Giese, 2025). If CaMKII has a faster overall integration of the 
common CaM driver, and DAPK1 a slower such integration, then this would implement the necessary 
temporal derivative mechanism.
Figure 3: Results from Jang et al. (2026), which are consistent with the predictions of the temporal 
derivative learning mechanism. A Pre- and postsynaptic neurons were stimulated to either 25 Hz or 50 Hz 
across the two 100 ms halves (prediction, outcome) of a 200 ms theta cycle. B All 4 cells of the 2x2 
combination of prediction, outcome frequencies were tested. C The progression of probe EPSP amplitudes 
surrounding the stimulation protocol at time 0, showing that the increasing temporal derivative (25 to 50 
Hz for both the pre and postsynaptic neurons, in orange) resulted in LTP, while the decreasing temporal 
derivative (50 to 25 Hz, in blue) resulted in LTD. Both flat profiles (constant 25 Hz or 50 Hz) resulted in no 
net synaptic efficacy change. D, E Summary showing all cell values (open circles) and averages (bars) for 
the individual conditions at different times after stimulation, with statistically significant results highlighted 
with asterisks (** = P < .01, *** = P < .001).

This is how the Neocortex Learns 6
There is now direct experimental evidence consistent with this prediction (Jang et al., 2026). Specifically, 
pre and postsynaptic pyramidal neurons in a widely-used in vitro synaptic plasticity preparation were 
driven by different temporal patterns of activity over a 200 ms theta-cycle window, with one activity level 
for the first 100 ms (i.e., reflecting the prediction state), and another activity level for the second 100 ms 
(the outcome state).
After 10 repeated presentations of these different temporal patterns, the resulting changes from baseline 
synaptic efficacy strength matched the predictions of the temporal derivative learning mechanism (Figure 
3). Specifically, when there was a rising pattern between prediction and outcome (25 Hz to 50 Hz), LTP 
resulted. When this pattern went the opposite direction (50 Hz to 25 Hz), LTD resulted. Finally, and 
critically, for both of the stable conditions (25 Hz to 25 Hz and 50 Hz to 5 Hz), no net synaptic efficacy 
change occurred. This latter condition directly contradicts the standard Hebbian-style account of synaptic 
plasticity, because the 50-50 case has the most overall synaptic activity, and yet it did not result in LTP, 
whereas the 25-to-50 case did. Furthermore the 25-to-50 and 50-to-25 cases both have the same net amount 
of synaptic activity, just organized differently across time.
Summary
Thus, the strong conclusion from this summary evaluation is that the temporal derivative form of error-
driven predictive learning is unique in providing a consistent and empirically supported account for how 
the neocortex learns, across all three relevant levels of analysis. Furthermore, this theory has been 
implemented in large-scale spiking neural networks, in the Axon framework, described extensively at 
compcogneuro.org. That website provides many examples of these models that can be run through the web 
browser, using the WebGPU framework for GPU-based acceleration to provide reasonable performance. 
For further details, see the kinase algorithm.
Alternative frameworks
Various points of contrast with other possible learning algorithms are briefly discussed below, to clarify the 
relevant distinctions.
Explicit error and predictive coding
Various alternative proposals for implementing the error backpropagation algorithm (Lillicrap et al., 2020) 
and the classic Bayesian predictive coding framework (e.g., Rao & Ballard, 1999) both hypothesize that a 
sub-population of neurons directly represent the error, by subtracting a top-down prediction from the 
bottom-up actual outcome (Figure 4). Thus, different populations of neurons must be somehow segregated 
so that they can represent fundamentally distinct information. Furthermore, all three of these different 
signals (prediction, outcome, error) should in principle be communicated across layers, in different 
directions, requiring strongly segregated pathways.
By contrast, as emphasized above, the temporal derivative framework keeps the error gradient 
representation implicit, as the difference in activity states over time, which greatly simplifies the biological 
implementation required. Furthermore, it allows for all levels in the network to work together to drive 
parallel constraint satisfaction processing, integrating top-down and bottom-up constraints, to drive 
coherent interpretations of the current state (Hopfield & Tank, 1985; O’Reilly et al., 2013). This represents 
a powerful form of search through representation space, operating as a kind of inner-loop optimization 
within the outer-loop of error backpropagation search through synaptic weight space to improve the 
predictive accuracy of the system.

This is how the Neocortex Learns 7
Figure 4: Proposals for implementing error-driven learning that require explicit error signals and / or 
separate neural pathways for feedforward vs. prediction signals. Given the pervasive interconnectivity of 
all lamina and neurons in the neocortex, it is unlikely that such strict separation between such channels is 
sustained. A is from Rao & Ballard (1999) on predictive coding, where the error is explicitly represented in 
neural firing, as a difference between a top-down prediction and bottom-up signal. Note that the 
feedforward signal to higher layers is exclusively an error signal, not a positive representation of the input 
stimulus. B is the target-prop model from Le Cun (1986) (via Lillicrap et al., 2020), which has a separate 
feedforward pathway on the left, and top-down feedback on the right, with the difference between these 
two providing the error signal.

The available neural evidence is consistent with the coherent, synergistic, redundant encoding of 
information across all levels of the cortex, with no significant evidence of the kind of structural segregation 
required by the explicit error models (Walsh et al., 2020; Heilbron & Chait, 2018). Furthermore, the 
standard predictive coding framework only has error signals propagating forward beyond the first layer, 
which is inconsistent with the extensive evidence showing that higher cortical areas contain positive 
representations of the input stimulus, at various levels of abstraction.
Thus, the temporal derivative framework supports the widely accepted idea that the neocortex learns by 
generating top-down predictions of what will happen next, in a way that appears to be more compatible 
with available neural evidence at multiple levels of analysis.
Hebbian learning
The predominant computational-level interpretation of neocortical learning in the literature has generally 
focused on various forms of Hebbian learning, based on the well-established data demonstrating a 
relationship between the level of postsynaptic calcium, entering via NMDA receptors, and the direction and 
magnitude of synaptic plasticity (Lisman, 1989; Bear & Malenka, 1994). Specifically, low levels of 
calcium result in LTD, while higher levels result in LTP. This is generally consistent with the BCM 
(Bienenstock et al., 1982) version of a Hebbian learning algorithm.
Despite this seeming advantage at the implementational level, Hebbian learning is essentially a non-starter 
at the computational level, because it only has a local, heuristic function in terms of extracting statistical 
regularities of co-activation (Oja, 1982; Rumelhart & Zipser, 1985; Intrator & Cooper, 1992). Therefore, 
there is no reason to believe that Hebbian learning can effectively train deep layered networks like those 
present in the neocortex, whereas this is precisely the case where error backpropagation excels.

This is how the Neocortex Learns 8
The spike-timing dependent plasticity (STDP) (Bi & Poo, 1998) version of Hebbian learning has been a 
primary focus of computational models (e.g., Kheradpisheh et al., 2018; Diehl & Cook, 2015). However, it 
is now clear that the simple computationally compelling form of STDP originally described, which 
required a very particular stimulation protocol with individual pairs of spikes separated by 1 s intervals, is 
not generally applicable to more realistic patterns of neural activity (Debanne & Inglebert, 2023). Indeed 
the same BCM-like pattern emerges with more realistic, denser activity patterns (Shouval et al., 2010; 
Izhikevich & Desai, 2003). Thus, STDP lacks both implementational-level support and a coherent 
computational-level account for why it should be a powerful learning mechanism.
Eligibility traces and specialized output learning
There is increasing evidence for a form of learning that applies specifically to output neurons in the 
neocortex and the hippocampus, which may function somewhat like the output decoding neurons in 
reservoir computing networks (Verstraeten et al., 2007; Tanaka et al., 2019), where a complex internal 
dynamical state can be read out by only adapting a single layer of output neuron synapses. This has been 
termed behavioral timescale synaptic plasticity (BTSP), and extensively studied in area CA1, which is the 
output layer of the hippocampus (Magee, 2026; Bittner et al., 2015; Bittner et al., 2017).
In BTSP, elevated plateau potentials in distal dendrites provide the critical plasticity-inducing mechanism 
that establishes an eligibility trace that lasts for several seconds. In CA1, these distal plateau potentials are 
activated by entorhinal cortex layer 3 inputs, which thus serve as a special training signal for driving 
plasticity in the other major population of synaptic inputs, from area CA3. A similar mechanism has 
recently been described in layer 5 pyramidal neurons in neocortex, which also have a prominent distal 
dendritic tuft, and are the primary output neurons of the neocortex (Yaeger et al., 2025; Xiao et al., 2025).
In both of these BTSP cases, there is rapid learning driven by the distal dendritic inputs, with an inhibitory 
negative feedback loop that prevents overtraining (Campbell et al., 2026). There is evidence in the CA1 
neurons that this plasticity is generally transient, consistent with a fast mapping type of learning that can 
rapidly adapt to read out behaviorally-relevant signals from the more slowly-adapting internal 
representations of the relevant systems (hippocampus or neocortex) (Vaidya et al., 2025).
The driving target signal for plasticity in the layer 5 neocortical neurons remains unclear (Magee, 2026), 
but we do know that these neurons receive extensive thalamic input targeting the distal dendritic tuft in 
layer 1. The thalamic projections that target layer 1 are generally of the matrix type, which means they 
typically have broad axonal arbors targeting many different neurons across multiple cortical areas. A 
prominent and widespread source of such projections comes from the ventral anterior (VA) nucleus, which 
receives inputs from layer 5 neurons in motor cortical areas, and is also under disinhibitory control from 
the basal ganglia (Phillips et al., 2021; Xiao et al., 2009; Kuramoto et al., 2015; Economo et al., 2018). 
This would provide a way for direct motor-relevant target signals to drive the rapid tuning of neocortical 
output neurons across most of neocortex, even all the way down in area V1 (Yaeger et al., 2025; Kuramoto 
et al., 2015).
The temporally-extended nature of the eligibility-trace mechanism allows later outcome or motor action 
signals to drive learning from earlier state representations, providing a solution to the temporal version of 
the credit assignment process (this is what the behavioral timescale connotes). In other brain areas such as 
the basal ganglia, and recently in the neocortex, neuromodulatory signals including dopamine have been 
found to drive eligibility-trace learning mechanisms, bridging the temporal gap until reinforcement signals 
become available (He et al., 2015; Shouval & Kirkwood, 2025).

This is how the Neocortex Learns 9
The current evidence suggests that the BTSP-based eligibility-trace mechanisms are synergistic with the 
more slowly-accumulating and shorter time-scale plasticity mechanisms (Magee, 2026), which provide the 
initial biases and encodings upon which the fast BTSP learning builds. The logic is similar to the 
complementary learning systems framework for understanding how the hippocampus and neocortex are 
separately optimized for rapid episodic learning (hippocampus) and slow statistical learning (neocortex) 
(McClelland et al., 1995; O’Reilly et al., 2014): error-driven learning within the many layers of the 
neocortex slowly learns to extract systematic ways of representing the structure of the environment, while 
the rapid, output-focused BTSP mechanism provides a way to quickly decode the resulting complex 
internal states to satisfy the current behavioral demands.
Conclusion
Across the three levels considered here, the strongest constraint appears to come from the computational 
level, effectively narrowing the field to one viable type of learning: error backpropagation. If someone 
were to discover something even more generally powerful than error backpropagation, that would certainly 
represent an important advance across many fields, but given the massive amount of research that has been 
invested into exploring algorithms at the computational level, this is seeming increasingly unlikely.
This then puts more of the weight on the algorithmic and implementational-level arguments outlined 
above, which each now have significant empirical evidence to support them. Nevertheless, more extensive 
empirical research is essential to further test between the different possible algorithmic and 
implementational possibilities that have been advanced for accomplishing predictive error-driven learning.
References
Ackley, D.H., Hinton, G.E., & Sejnowski, T.J. (1985). A learning algorithm for Boltzmann machines. 
Cognitive Science, 9, 147–169.
Bayer, K.U., & Giese, K.P. (2025). A revised view of the role of CaMKII in learning and memory. Nature 
Neuroscience, 28, 24–34. https.//www:nature.com/articles/s41593-024-01809-x http.//doi:org/10.1038/
s41593-024-01809-x
Bear, M.F., & Malenka, R.C. (1994). Synaptic plasticity: LTP and LTD. Current Opinion in Neurobiology, 
4, 389–399. https.//www:sciencedirect.com/science/article/pii/0959438894901015 http.//doi:org/
10.1016/0959-4388(94)90101-5
Bienenstock, E.L., Cooper, L.N., & Munro, P.W. (1982). Theory for the development of neuron selectivity: 
Orientation specificity and binocular interaction in visual cortex. The Journal of Neuroscience, 2, 32–48. 
http.//www:ncbi.nlm.nih.gov/pubmed/7054394
Bi, G., & Poo, M. (1998). Synaptic modifications in cultured hippocampal neurons: dependence on spike 
timing, synaptic strength, and postsynaptic cell type. The Journal of Neuroscience, 18, 10464–10472. http.//
www:jneurosci.org/content/18/24/10464
Bittner, K.C., Grienberger, C., Vaidya, S.P., Milstein, A.D., Macklin, J.J., Suh, J., Tonegawa, S., & Magee, 
J.C. (2015). Conjunctive input processing drives feature selectivity in hippocampal CA1 neurons. Nature 
Neuroscience, 18(8), 1133–1142. https.//www:nature.com/articles/nn.4062 http.//doi:org/10.1038/nn.4062
Bittner, K.C., Milstein, A.D., Grienberger, C., Romani, S., & Magee, J.C. (2017). Behavioral time scale 
synaptic plasticity underlies CA1 place fields. Science, 357, 1033–1036. http.//science.sciencemag.org/
content/357/6355/1033 http.//doi:org/10.1126/science.aan3846

This is how the Neocortex Learns 10
Blei, D.M., Kucukelbir, A., & McAuliffe, J.D. (2017). Variational Inference: A Review for Statisticians. 
Journal of the American Statistical Association, 112, 859–877. https.//doi:org/
10.1080/01621459.2017.1285773 http.//doi:org/10.1080/01621459.2017.1285773
Campbell, E.P., Martin, L., Magee, J.C., & Grienberger, C. (2026). Learning-dependent feedback by OLM 
interneurons shapes CA1 representations. 2025.12.21.695825. https.//www:biorxiv.org/content/
10.64898/2025.12.21.695825v2 http.//doi:org/10.64898/2025.12.21.695825
Cook, S.G., Buonarati, O.R., Coultrap, S.J., & Bayer, K.U. (2021). CaMKII holoenzyme mechanisms that 
govern the LTP versus LTD decision. Science Advances, https.//www:science.org/doi/abs/10.1126/
sciadv.abe2300 http.//doi:org/10.1126/sciadv.abe2300
Crick, F. (1989). The recent excitement about neural networks. Nature, 337, 129–132. http.//
www:ncbi.nlm.nih.gov/pubmed/2911347
Debanne, D., & Inglebert, Y. (2023). Spike timing-dependent plasticity and memory. Current Opinion in 
Neurobiology, 80, 102707. https.//www:sciencedirect.com/science/article/pii/S0959438823000326 http.//
doi:org/10.1016/j.conb.2023.102707
Diehl, P.U., & Cook, M. (2015). Unsupervised learning of digit recognition using spike-timing-dependent 
plasticity. Frontiers in Computational Neuroscience, 9, https.//www:frontiersin.org/articles/10.3389/
fncom.2015.00099/full http.//doi:org/10.3389/fncom.2015.00099
Economo, M.N., Viswanathan, S., Tasic, B., Bas, E., Winnubst, J., Menon, V., Graybuck, L.T., Nguyen, 
T.N., Smith, K.A., Yao, Z., Wang, L., Gerfen, C.R., Chandrashekar, J., Zeng, H., Looger, L.L., & Svoboda, 
K. (2018). Distinct descending motor cortex pathways and their roles in movement. Nature, 563(7729), 79–
84. https.//www:nature.com/articles/s41586-018-0642-9 http.//doi:org/10.1038/s41586-018-0642-9
Fiebelkorn, I.C., & Kastner, S. (2021). Spike timing in the attention network predicts behavioral outcome 
prior to target selection. Neuron, 109, 177-188.e4. https.//www:sciencedirect.com/science/article/pii/
S0896627320307637 http.//doi:org/10.1016/j.neuron.2020.09.039
Goodell, D.J., Tullis, J.E., & Bayer, K.U. (2021). Young DAPK1 knockout mice have altered presynaptic 
function. Journal of Neurophysiology, 125, 1973–1981. http.//journals.physiology.org/doi/full/10.1152/
jn.00055.2021 http.//doi:org/10.1152/jn.00055.2021
Goodell, D.J., Zaegel, V., Coultrap, S.J., Hell, J.W., & Bayer, K.U. (2017). DAPK1 mediates LTD by 
making CaMKII/GluN2B binding LTP specific. Cell Reports, 19, 2231–2243. http.//
www:sciencedirect.com/science/article/pii/S2211124717307258 http.//doi:org/10.1016/j.celrep.2017.05.068
He, K., Huertas, M., Hong, S.Z., Tie, X., Hell, J.W., Shouval, H., & Kirkwood, A. (2015). Distinct 
eligibility traces for LTP and LTD in cortical synapses. Neuron, 88, 528–538. https.//
www:sciencedirect.com/science/article/pii/S0896627315008260 http.//doi:org/10.1016/
j.neuron.2015.09.037
Heilbron, M., & Chait, M. (2018). Great Expectations: Is there Evidence for Predictive Coding in Auditory 
Cortex? Neuroscience, 389, 54–73. https.//www:sciencedirect.com/science/article/pii/S030645221730547X 
http.//doi:org/10.1016/j.neuroscience.2017.07.061
Hinton, G.E., & McClelland, J.L. (1988). Learning representations by recirculation. In D.Z. Anderson 
(Ed.), Neural Information Processing Systems (NIPS 1987 (pp. 358–366)) American Institute of Physics. 
http.//papers.nips.cc/paper/78-learning-representations-by-recirculation.pdf

This is how the Neocortex Learns 11
Hopfield, J.J., & Tank, D.W. (1985). {`Neural'} computation of decisions in optimization problems. 
Biological Cybernetics, 52, 141–152. http.//www:ncbi.nlm.nih.gov/pubmed/4027280
Intrator, N., & Cooper, L.N. (1992). Objective function formulation of the BCM theory of visual cortical 
plasticity: Statistical connections, stability conditions. Neural Networks, 5, 3–17. https.//
www:sciencedirect.com/science/article/pii/S0893608005800036 http.//doi:org/10.1016/
S0893-6080(05)80003-6
Izhikevich, E.M., & Desai, N.S. (2003). Relating STDP to BCM. Neural computation, 15, 1511–1524. 
http.//www:ncbi.nlm.nih.gov/pubmed/12816564
Jang, J., Flores, J.C., Zito, K., & O'Reilly, R.C. (2026). Synaptic Plasticity as a Function of the Temporal 
Derivative. 2026.06.05.730489. https.//www:biorxiv.org/content/10.64898/2026.06.05.730489v1 http.//
doi:org/10.64898/2026.06.05.730489
Khan, M.E., & Rue, H. (2023). The Bayesian Learning Rule. Journal of Machine Learning Research, 24, 
1–46. http.//jmlr.org/papers/v24/22-0291.html
Kheradpisheh, S.R., Ganjtabesh, M., Thorpe, S.J., & Masquelier, T. (2018). STDP-based spiking deep 
convolutional neural networks for object recognition. Neural Networks, 99, 56–67. https.//
www:sciencedirect.com/science/article/pii/S0893608017302903 http.//doi:org/10.1016/
j.neunet.2017.12.005
Kuramoto, E., Ohno, S., Furuta, T., Unzai, T., Tanaka, Y.R., Hioki, H., & Kaneko, T. (2015). Ventral medial 
nucleus neurons send thalamocortical afferents more widely and more preferentially to layer 1 than 
neurons of the ventral anterior–ventral lateral nuclear complex in the rat. Cerebral Cortex, 25, 221–235. 
https.//academic.oup.com/cercor/article/25/1/221/369709 http.//doi:org/10.1093/cercor/bht216
Le Cun, Y. (1986). Learning Process in an Asymmetric Threshold Network. In E. Bienenstock, F.F. Soulié, 
& G. Weisbuch (Eds.), Disordered Systems and Biological Organization (pp. 233–240). Springer.  http.//
doi:org/10.1007/978-3-642-82657-3_24
Lillicrap, T.P., Santoro, A., Marris, L., Akerman, C.J., & Hinton, G. (2020). Backpropagation and the brain. 
Nature Reviews Neuroscience, 21(6), 335–346. https.//www:nature.com/articles/s41583-020-0277-3 http.//
doi:org/10.1038/s41583-020-0277-3
Lisman, J. (1989). A mechanism for the Hebb and the anti-Hebb processes underlying learning and 
memory. Proceedings of the National Academy of Sciences, 86, 9574–9578. https.//www:pnas.org/doi/abs/
10.1073/pnas.86.23.9574 http.//doi:org/10.1073/pnas.86.23.9574
Magee, J.C. (2026). Behavioral timescale synaptic plasticity: properties, elements and functions. Nature 
Neuroscience, 29, 520–534. https.//www:nature.com/articles/s41593-026-02214-2 http.//doi:org/10.1038/
s41593-026-02214-2
Markov, N.T., Ercsey-Ravasz, M., Lamy, C., Ribeiro Gomes, A.R., Magrou, L., Misery, P., Giroud, P., 
Barone, P., Dehay, C., Toroczkai, Z., Knoblauch, K., Van Essen, D.C., & Kennedy, H. (2013). The role of 
long-range connections on the specificity of the macaque interareal cortical network. Proceedings of the 
National Academy of Sciences U. S. A., 110, 5187–5192. http.//www:ncbi.nlm.nih.gov/pubmed/23479610
Marr, D. (1982). Vision.  Freeman.

This is how the Neocortex Learns 12
McClelland, J.L., McNaughton, B.L., & O'Reilly, R.C. (1995). Why There Are Complementary Learning 
Systems in the Hippocampus and Neocortex: Insights from the Successes and Failures of Connectionist 
Models of Learning and Memory. Psychological Review, 102, 419–457. http.//www:ncbi.nlm.nih.gov/
pubmed/7624455
Oja, E. (1982). A simplified neuron model as a principal component analyzer. Journal of mathematical 
biology, 15, 267–273. http.//www:ncbi.nlm.nih.gov/pubmed/7153672
O'Reilly, R.C. (1996). Biologically plausible error-driven learning using local activation differences: The 
generalized recirculation algorithm. Neural Computation, 8, 895–938. https.//www:mitpressjournals.org/
doi/abs/10.1162/neco.1996.8.5.895 http.//doi:org/https.//doi:org/10.1162/neco.1996.8.5.895
O'Reilly, R.C., Bhattacharyya, R., Howard, M.D., & Ketz, N. (2014). Complementary Learning Systems. 
Cognitive Science, 38, 1229–1248. http.//www:ncbi.nlm.nih.gov/pubmed/22141588
O'Reilly, R.C., Russin, J.L., Zolfaghar, M., & Rohrlich, J. (2021). Deep Predictive Learning in Neocortex 
and Pulvinar. Journal of Cognitive Neuroscience, 33, 1158–1196. https.//doi:org/10.1162/jocn_a_01708 
http.//doi:org/10.1162/jocn_a_01708
O'Reilly, R.C., Wyatte, D., Herd, S.A., Mingus, B., & Jilk, D.J. (2013). Recurrent Processing during Object 
Recognition. Frontiers in Psychology, 4, http.//www:ncbi.nlm.nih.gov/pubmed/23554596
Phillips, J.M., Kambi, N.A., Redinbaugh, M.J., Mohanta, S., & Saalmann, Y.B. (2021). Disentangling the 
influences of multiple thalamic nuclei on prefrontal cortex and cognitive control. Neuroscience & 
Biobehavioral Reviews, 128, 487–510. https.//www:sciencedirect.com/science/article/pii/
S0149763421002955 http.//doi:org/10.1016/j.neubiorev.2021.06.042
Rao, R.P., & Ballard, D.H. (1999). Predictive coding in the visual cortex: A functional interpretation of 
some extra-classical receptive-field effects. Nature Neuroscience, 2, 79–87. http.//www:ncbi.nlm.nih.gov/
pubmed/10195184 http.//doi:org/10.1038/4580
Rumelhart, D.E., Hinton, G.E., & Williams, R.J. (1986). Learning representations by back-propagating 
errors. Nature, 323, 533–536.
Rumelhart, D.E., & Zipser, D. (1985). Feature discovery by competitive learning* Cognitive Science, 9, 75–
112. http.//onlinelibrary.wiley.com/doi/10.1207/s15516709cog0901_5/abstract http.//doi:org/10.1207/
s15516709cog0901_5
Scellier, B., & Bengio, Y. (2017). Equilibrium propagation: Bridging the gap between energy-based models 
and backpropagation. Frontiers in Computational Neuroscience, 11, http.//www:ncbi.nlm.nih.gov/pmc/
articles/PMC5415673/ http.//doi:org/10.3389/fncom.2017.00024
Sherman, S.M., & Guillery, R.W. (2006). Exploring the Thalamus and Its Role in Cortical Function.  MIT 
Press. http.//www:scholarpedia.org/article/Thalamus
Sherman, S.M., & Usrey, W.M. (2024). Transthalamic Pathways for Cortical Function. Journal of 
Neuroscience, 44, https.//www:jneurosci.org/content/44/35/e0909242024 http.//doi:org/10.1523/
JNEUROSCI.0909-24.2024
Shouval, H.Z., & Kirkwood, A. (2025). Eligibility traces as a synaptic substrate for learning. Current 
Opinion in Neurobiology, 91, 102978. https.//www:sciencedirect.com/science/article/pii/
S0959438825000091 http.//doi:org/10.1016/j.conb.2025.102978

This is how the Neocortex Learns 13
Shouval, H.Z., Wang, S.S., & Wittenberg, G.M. (2010). Spike timing dependent plasticity: A consequence 
of more fundamental learning rules. Frontiers in Computational Neuroscience, 4, http.//
www:ncbi.nlm.nih.gov/pubmed/20725599
Tanaka, G., Yamane, T., Héroux, J.B., Nakane, R., Kanazawa, N., Takeda, S., Numata, H., Nakano, D., & 
Hirose, A. (2019). Recent advances in physical reservoir computing: A review. Neural Networks, 115, 100–
123. https.//www:sciencedirect.com/science/article/pii/S0893608019300784 http.//doi:org/10.1016/
j.neunet.2019.03.005
Tullis, J.E., & Bayer, K.U. (2023). Distinct synaptic pools of DAPK1 differentially regulate activity-
dependent synaptic CaMKII accumulation. iScience, 26, https.//www:cell.com/iscience/abstract/
S2589-0042(23)00800-3 http.//doi:org/10.1016/j.isci.2023.106723
Usrey, W.M., & Sherman, S.M. (2018). Corticofugal circuits: Communication lines from the cortex to the 
rest of the brain. Journal of Comparative Neurology, 0, https.//onlinelibrary.wiley.com/doi/abs/10.1002/
cne.24423 http.//doi:org/10.1002/cne.24423
Vaidya, S.P., Li, G., Chitwood, R.A., Li, Y., & Magee, J.C. (2025). Formation of an expanding memory 
representation in the hippocampus. Nature Neuroscience, 28, 1510–1518. https.//www:nature.com/articles/
s41593-025-01986-3 http.//doi:org/10.1038/s41593-025-01986-3
Van Essen, D.C., & Maunsell, J.H.R. (1983). Hierarchical organization and functional streams in the visual 
cortex. Trends in Neurosciences, 6, 370–375.
Vastola, J., Gershman, S.J., & Rajan, K. (2026). Gradient Descent as Loss Landscape Navigation: a 
Normative Framework for Deriving Learning Rules. Advances in Neural Information Processing Systems, 
38, 119609–119650. https.//proceedings.neurips.cc/paper_files/paper/2025/hash/
ad557daf1552a14dd0c26c11d3a72676-Abstract-Conference.html
Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N., Kaiser,  ., & Polosukhin, I. 
(2017). Attention is all you need. In I. Guyon, U.V. Luxburg, S. Bengio, H. Wallach, R. Fergus, S. 
Vishwanathan, & R. Garnett (Eds.), Advances in Neural Information Processing Systems 30 (pp. 5998–
6008). Curran Associates, Inc. http.//papers.nips.cc/paper/7181-attention-is-all-you-need.pdf
Verstraeten, D., Schrauwen, B., D'Haene, M., & Stroobandt, D. (2007). An experimental unification of 
reservoir computing methods. Neural Networks, 20, 391–403. http.//www:ncbi.nlm.nih.gov/pubmed/
17517492 http.//doi:org/10.1016/j.neunet.2007.04.003
Walsh, K.S., McGovern, D.P., Clark, A., & O'Connell, R.G. (2020). Evaluating the neurophysiological 
evidence for predictive processing as a model of perception. Annals of the New York Academy of Sciences, 
1464, 242–268. https.//www:ncbi.nlm.nih.gov/pmc/articles/PMC7187369/ http.//doi:org/10.1111/
nyas.14321
Werbos, P. (1974). Beyond Regression: New Tools for Prediction and Analysis in the Behavioral Sciences. 
[unpublished thesis, Harvard University].
Widrow, B., & Hoff, M.E. (1960). Adaptive Switching Circuits. In Institute of Radio Engineers, Western 
Electronic Show and Convention, Convention Record, Part 4 (pp. 96–104).
Xiao, K., Li, Y., Sullivan, B.J., Li, G., & Magee, J.C. (2025). Rapid neocortical network modifications via 
dendritic plateau potential induced plasticity. 2025.11.19.689338. https.//www:biorxiv.org/content/
10.1101/2025.11.19.689338v1 http.//doi:org/10.1101/2025.11.19.689338

This is how the Neocortex Learns 14
Xiao, D., Zikopoulos, B., & Barbas, H. (2009). Laminar and modular organization of prefrontal projections 
to multiple thalamic nuclei. Neuroscience, 161, 1067–1081. http.//www:sciencedirect.com/science/article/
pii/S0306452209006411 http.//doi:org/10.1016/j.neuroscience.2009.04.034
Xie, X., & Seung, H.S. (2003). Equivalence of backpropagation and Contrastive Hebbian Learning in a 
layered network. Neural Computation, 15, 441–454. http.//www:ncbi.nlm.nih.gov/pubmed/12590814
Yaeger, C.E., Soto-Albors, R.M., Liu, W., Beltramini, A., & Harnett, M.T. (2025). Plateau potentials are 
instructive signals for behavioral timescale synaptic plasticity in the neocortex. 2025.11.07.687250. https.//
www:biorxiv.org/content/10.1101/2025.11.07.687250v1 http.//doi:org/10.1101/2025.11.07.687250
