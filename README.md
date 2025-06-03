# synapse-sparks⚡
*This repo hosts LLM prompt experiments.*

## Results at a glance

| Model                              | Mode           | Accuracy | P\_supports | R\_supports | F1\_supports | P\_refutes | R\_refutes | F1\_refutes |
| ---------------------------------- | -------------- | -------- | ----------- | ----------- | ------------ | ---------- | ---------- | ----------- |
| google/flan‑t5‑base                | few‑shot       | 0.618    | 0.60        | 0.968       | 0.741        | 0.80       | 0.167      | 0.276       |
| mistralai/Mistral‑7B‑Instruct‑v0.1 | few‑shot       | 0.54     | 0.66        | 0.16        | 0.25         | 0.52       | 0.92       | 0.66        |
| mistralai/Mistral‑7B‑Instruct‑v0.1 | few‑shot (alt) | 0.55     | 1.00        | 0.08        | 0.15         | 0.53       | 1.00       | 0.69        |
| TinyLlama/TinyLlama‑1.1B‑Chat‑v1.0 | few‑shot       | 0.58     | 0.578       | 0.531       | 0.553        | 0.582      | 0.627      | 0.604       |
| deepseek‑ai/deepseek‑llm‑7b‑chat   | few‑shot       | 0.66     | 0.89        | 0.34        | 0.50         | 0.61       | 0.96       | 0.74        |
| deepseek‑ai/deepseek‑llm‑7b‑chat   | zero‑shot      | 0.57     | 0.875       | 0.14        | 0.24         | 0.54       | 0.98       | 0.699       |
| google/flan‑t5‑large               | zero‑shot      | 0.620    | 0.70        | 0.42        | 0.525        | 0.586      | 0.82       | 0.683       |
| mistralai/Mistral‑7B‑Instruct‑v0.1 | zero‑shot      | 0.57     | 0.564       | 0.62        | 0.590        | 0.578      | 0.52       | 0.547       |
---

## Prompts that work the best

### Zero‑shot 
```text
Instruction: Given a claim and evidence, determine if the evidence supports or refutes the claim.
Respond with one of the following: "Supports" or "Refutes".

Claim: {{claim}}
Evidence: {{premise}}
Stance:
```

### Few-shot
```text
You are given a claim and evidence. Your task is to determine whether the evidence supports or refutes the claim.
Respond only with one word: "Supports" or "Refutes".

Example 1:
Claim: The sky is blue.
Evidence: Scientists have confirmed that the sky appears blue due to the scattering of light.
Stance: Supports

Example 2:
Claim: Eating fast food is healthy.
Evidence: Studies show that fast food contains high levels of trans fats and sodium, leading to health problems.
Stance: Refutes

Example 3:
Claim: Solar energy reduces electricity costs.
Evidence: Households using solar panels report a significant reduction in electricity bills.
Stance: Supports

Example 4:
Claim: Exercise is harmful to health.
Evidence: Numerous studies show that regular exercise improves cardiovascular health and longevity.
Stance: Refutes

Example 5:
Claim: Climate change is primarily caused by human activity.
Evidence: Recent studies show that over 90% of the increase in greenhouse gases is due to human activities like burning fossil fuels and deforestation.
Stance: Supports

Example 6:
Claim: Video games can improve cognitive skills.
Evidence: Research indicates that playing strategy games can improve memory, attention, and problem-solving skills.
Stance: Supports

Example 7:
Claim: Exercise has no effect on weight loss.
Evidence: Scientific research consistently shows that physical activity increases energy expenditure and supports weight management.
Stance: Refutes

Example 8:
Claim: Social media has no impact on mental health.
Evidence: Multiple studies have linked social media usage with increased rates of anxiety and depression in teenagers and young adults.
Stance: Refutes

Now analyse the following:

Claim: {{claim}}
Evidence: {{premise}}
Stance:
```
---



#
