# Review

## Summary
This paper proposes Latent On-Policy Self-Distillation (LOPD), a method that learns a privileged-context composer that transforms prior experience into a latent representation, which is then used to condition the teacher model in on-policy self-distillation (OPSD). This approach differs from existing OPSD methods, which typically rely on hand-designed or rule-extracted transformations of experience. The authors demonstrate that LOPD outperforms several OPSD baselines on agentic tool use and code generation tasks, while also being more sample-efficient.

## Soundness
3

## Presentation
4

## Contribution
3

## Strengths
- The paper is well-written and easy to follow. The authors clearly explain the problem of relying on hand-designed privileged contexts in OPSD and how their method addresses this issue. The description of the method is also very clear.
- The proposed method is novel and interesting. Learning the privileged context as part of the distillation process is a unique contribution to the field of OPSD.
- The experiments are well-designed and thorough. The authors evaluate their method on two different domains (agentic tool use and code generation) and compare against several relevant baselines. The ablation studies provide valuable insights into the importance of different components of the method.

## Weaknesses
- The performance improvements over the baselines are relatively small in some cases. For example, in Table 1, the improvement over SDPO is only 1.5 points on BFCL-v3 with Qwen3-8B, and in Table 2, the improvement over OPSD is only 0.2 points on LiveCodeBench with Qwen3-4B. The authors should discuss the statistical significance of these improvements and whether they are meaningful.
- The method introduces several new hyperparameters (e.g., number of latent tokens, privileged-margin threshold) that require careful tuning. This could make it more difficult to apply the method to new domains or tasks. The authors should provide more guidance on how to choose these hyperparameters and how sensitive the method is to their values.
- The method relies on a fixed set of latent tokens, which may limit its ability to capture more complex or nuanced information. The authors should discuss the potential limitations of using a fixed number of latent tokens and whether there are ways to make this more flexible.

## Questions
- Can you provide more details on how you chose the hyperparameters for your method and the baselines? Did you perform any systematic hyperparameter search?
- Have you investigated whether the latent tokens learn any interpretable or meaningful representations? Are there any patterns or clusters in the latent tokens that correspond to different types of experiences or tasks?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4