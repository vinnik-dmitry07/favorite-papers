# Review

## Summary
This paper proposes to use sparse autoencoders to learn interpretable and monosemantic features from the activations of a language model. The learned features are shown to be more interpretable than those obtained with PCA and ICA, and are used to identify the features that are causally responsible for counterfactual behavior on the indirect object identification task.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well written and easy to follow.
- The proposed method is simple and effective.
- The evaluation is sound and the results are convincing.

## Weaknesses
- The proposed method is only applied to the residual stream, but not to the MLPs.
- The proposed method is only evaluated on one language model (Pythia-70M).

## Questions
- The proposed method is only applied to the residual stream, but not to the MLPs. The authors explain that "there is little reason to expect features to align with the neuron basis" in the residual stream, but not for the MLPs. However, the autoencoder is also trained on the MLP activations in the Appendix, so why can't the learned features be interpreted for the MLPs? Is it because of the lower dimensionality of the MLP activations? Could you elaborate more on this?
- The proposed method is only evaluated on one language model (Pythia-70M). Would the method work for other language models, especially larger ones (e.g., GPT-3)? Would the results still be consistent with the findings of Bills et al. (2023), i.e., that the features learned by the sparse autoencoder are more interpretable than those learned by the default basis and random projections?
- In Table 1, the proposed method is compared with PCA and ICA, but not with the method of Sharkey et al. (2023). Could you explain why?
- In Figure 2, the proposed method is compared with PCA and ICA, but not with the method of Sharkey et al. (2023). Could you explain why?
- In Figure 3, it is shown that the features learned by the proposed method allow the same amount of model editing in fewer patches than the PCA decomposition. However, the minimum KL divergences are different for the two methods. Could you elaborate more on this?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4