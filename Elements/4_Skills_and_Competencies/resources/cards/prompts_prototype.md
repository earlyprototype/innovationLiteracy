---
element: 4
element_name: Skills and Competencies
stage: prototype
type: structured-method
time_to_read: 2min
card_set: prompt_engineering
related_cards:
  - prompts_fundamentals
  - interventions_prototype
  - gate_alignment
source_doc: prompt_engineering.md
image_meta_description: "A prompt evolving through three iterations, each version more specific — with the output sharpening alongside it."
---

# Prompts: Prototype Phase

**Task:** Generate low-resolution structural artifact (mind map, process flow)

## Effective Prompt Structure

```
Context: We're prototyping a solution for [problem].
         Key components: [list].
Task: Generate a process flow showing how components work together.
Constraints:
- Low-resolution only (structure, not visual design)
- Show decision points and error states
- Indicate automated vs manual steps
- Format as Mermaid diagram or structured text
Source Documents: [attach style guide, component library, requirements]
Success criteria: Clear enough for developer to identify
                  integration points
```

## Common Failure

"Design an app for X" — no constraints, requests high-fidelity too early. Triggers premature convergence.

## Key Principle

Prompt iteration IS the prototyping. Language is material. Document prompt evolution to capture learning about how constraint specificity affects output.

---

_Card Set: Prompt Engineering · Prototype_
_Source: [prompt_engineering.md](../prompt_engineering.md)_
