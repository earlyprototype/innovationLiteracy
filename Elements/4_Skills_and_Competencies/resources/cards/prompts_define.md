---
element: 4
element_name: Skills and Competencies
stage: define
type: structured-method
time_to_read: 2min
card_set: prompt_engineering
related_cards:
  - prompts_fundamentals
  - interventions_define
  - gate_alignment
source_doc: prompt_engineering.md
image_meta_description: "Multiple How Might We statements fanning out like cards from a single problem brief — each reframing the challenge differently."
---

# Prompts: Define Phase

**Task:** Generate multiple problem statement framings

## Effective Prompt Structure

```
Context: Based on user research showing [key insights],
         we need to frame a problem statement.
Task: Generate 5 alternative problem framings, each emphasizing
      different aspects or stakeholder perspectives.
Constraints:
- Frame as "How Might We..." questions
- Do NOT embed solutions in problem statements
- Each framing should reflect different user needs
- Ground each framing in specific discovery insights
Format: For each HMW:
  (1) the question
  (2) which discovery insight it emphasises
  (3) what makes this framing distinct
```

## Common Failure

"Write a problem statement" — too generic, no grounding, no variation requirement. Produces single framing that embeds solutions.

## Key Principle

Prompt co-creation makes the activity collaborative. Pairs write prompts together, surfacing assumptions: "Why did we specify that constraint?"

---

_Card Set: Prompt Engineering · Define_
_Source: [prompt_engineering.md](../prompt_engineering.md)_
