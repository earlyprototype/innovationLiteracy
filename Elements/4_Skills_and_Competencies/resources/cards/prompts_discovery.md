---
element: 4
element_name: Skills and Competencies
stage: discovery
type: structured-method
time_to_read: 2min
card_set: prompt_engineering
related_cards:
  - prompts_fundamentals
  - interventions_discovery
  - gate_source_grounding
source_doc: prompt_engineering.md
image_meta_description: "An AI screen showing synthesised interview themes, with a human hand circling one theme and marking verify against source."
---

# Prompts: Discovery Phase

**Task:** Synthesise interview notes to identify patterns

## Effective Prompt Structure

```
Context: We conducted 8 user interviews about [topic].
Task: Identify the top 3-5 patterns across these observations,
      noting contradictions and edge cases.
Constraints:
- Ground patterns in specific quotes (cite observation numbers)
- Flag where observations contradict each other
- Note edge cases that don't fit patterns
Format: For each pattern:
  (1) pattern description
  (2) supporting evidence (observation citations)
  (3) contradictions if any
```

## Common Failure

"Summarise these interviews" — no context, constraints, or success criteria. Produces generic, ungrounded summary.

## Key Principle

AI synthesises what humans learned, not replaces the learning. Upload source documents to enable source-grounded analysis.

---

_Card Set: Prompt Engineering · Discovery_
_Source: [prompt_engineering.md](../prompt_engineering.md)_
