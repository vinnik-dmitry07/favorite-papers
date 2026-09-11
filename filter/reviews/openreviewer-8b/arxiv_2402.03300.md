# Review

## Summary
This paper introduces DeepSeekMath, a language model that excels in mathematical reasoning. It is trained on a large dataset of 120 billion math-related tokens from the web, curated to high quality. The model achieves 51.7% accuracy on the MATH benchmark, approaching the performance of GPT-4 and Gemini-Ultra. The authors also introduce GRPO, a more efficient variant of the PPO algorithm, which enhances reasoning abilities while optimizing memory use.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow.
2. The model is trained on a large-scale, high-quality dataset of 120 billion math-related tokens from the Common Crawl, which is almost 7 times the size of the math web pages used by Minerva and 9 times the size of OpenWebMath.
3. The model demonstrates strong performance on various benchmarks, outperforming many existing models, including Minerva, a much larger 540B parameter model.
4. The introduction of GRPO, a more efficient variant of PPO, is a valuable contribution that could have broad applicability in the field.

## Weaknesses
1. The model's performance on geometry and theorem-proof tasks is weaker than in quantitative reasoning, indicating potential data selection biases in the pre-training and fine-tuning process.
2. The model's performance is still significantly lower than GPT-4 in few-shot settings, suggesting room for improvement in its few-shot learning capabilities.

## Questions
1. How does the model's performance vary with different types of mathematical problems? Are there specific areas where it excels or struggles?
2. How does the model's performance compare in real-world mathematical tasks, such as those encountered in educational settings or mathematical research?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4