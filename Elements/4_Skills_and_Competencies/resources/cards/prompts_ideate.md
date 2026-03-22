---
element: 4
element_name: Skills and Competencies
stage: ideate
type: structured-method
time_to_read: 2min
card_set: prompt_engineering
related_cards:
  - prompts_fundamentals
  - interventions_ideate
  - gate_tension
source_doc: prompt_engineering.md
image_meta_description: "A set of human-generated seed ideas feeding into an expansion engine — 5 ideas becoming 50 variations."
---

# Prompts: Ideate Phase

**Task:** Expand human-generated core concepts into variations

## Effective Prompt Structure

```
Context: We generated these 3 core solution concepts: [list].
         We need to explore variations.
Task: Generate 10 variations on each concept that maintain
      core intent whilst exploring different implementations.
Constraints:
- Variations must address [specific user need from research]
- Variations must respect [technical constraints]
- Show trade-offs (faster vs simpler, cheaper vs robust)
- Range from incremental to ambitious
Format: For each variation:
  (1) concept description (2 sentences)
  (2) what it trades off
  (3) implementation complexity (low/med/high)
```

## Common Failure

"Give me more ideas" — no seed concepts, no constraints, overwhelming volume of disconnected suggestions.

## Key Principle

Human ideas first (10-15 min brainstorming), THEN AI expansion. Constraints enable focused creativity, prevent generic solutions.

---

_Card Set: Prompt Engineering · Ideate_
_Source: [prompt_engineering.md](../prompt_engineering.md)_
