# Evaluation and Quality Loop

## 1. Overview

This system implements an internal evaluation loop to improve reliability
and reduce hallucination over time.

Evaluation is local, bounded, and non-autonomous.

The agent does not self-modify code.
It produces proposals and behavioral metrics.

Human oversight remains mandatory.

---

## 2. Quality Dimensions

Each interaction may be evaluated along the following axes:

- Coherence
- Usefulness
- Uncertainty
- Claim accuracy
- Correction frequency

Scores are stored locally in:
eval/results.jsonl

---

## 3. Counterfactual Memory

The agent extracts factual claims from its own responses.

Each claim is tracked with:

- Unique identifier
- Topic
- Confidence score
- Status (active / corrected / retracted)
- Correction history

User corrections directly influence future prompt context.

This creates a structured feedback loop.

---

## 4. Self-Reflection

At probabilistic intervals, the agent performs a reflective pass:

- Assess response quality
- Estimate uncertainty
- Suggest memory updates

Reflection operates with deterministic model settings.

Results are logged locally.

---

## 5. Periodic Evaluation

The `/eval` command executes a fixed prompt set from:
eval/prompts.jsonl

Each prompt is evaluated under consistent model parameters.

Outputs are stored for longitudinal comparison.

This enables tracking behavioral drift and improvement.

---

## 6. Improvement Workflow

The system supports a bounded improvement loop:

1. Collect interaction traces
2. Analyze correction patterns
3. Identify weak topics or behaviors
4. Generate improvement proposals
5. Human selects changes
6. Aider applies modifications
7. Tests are rerun

The agent does not autonomously deploy changes.

---

## 7. Design Philosophy

Evaluation exists to:

- Increase determinism
- Reduce hallucination
- Surface weaknesses
- Support deliberate iteration

It does not exist to maximize benchmark scores.

---

## 8. Non-Goals

This evaluation system does NOT attempt:

- Automatic self-rewriting
- Genetic optimization
- Reinforcement learning
- Continuous autonomous deployment

The system is intentionally conservative.
