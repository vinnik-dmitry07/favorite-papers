# Review

## Summary
The authors address two issues in representational similarity analysis (RSA) of neural data.  The first is the bias in estimates of distance between representations when these are estimated from noisey data.  The second is the fact that the entries in a representational dissimilarity matrix (RDM) are not statistically independent.  The authors propose a new similarity metric that addresses both of these issues.

## Soundness
4

## Presentation
4

## Contribution
4

## Strengths
This is a very nice paper.  It is well-written, thorough, and addresses real issues in the analysis of neural data.  The proposed method is well-motivated and seems to work well.

## Weaknesses
The authors could do a better job of relating their work to the Bayesian approaches to RSA (e.g., those that treat the RDM as a random quantity with a matrix normal distribution, with either a known or a learned covariance function).  These approaches also deal with the issue of dependent entries in the RDM and, in the case of the known covariance function, allow for an unbiased estimate of the RDM.  I think the authors should at least mention these approaches in the discussion.

## Questions
None.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4