---
element: 4
element_name: Skills and Competencies
stage: test
type: structured-method
time_to_read: 2min
card_set: prompt_engineering
related_cards:
  - prompts_fundamentals
  - interventions_test
  - gate_source_grounding
source_doc: prompt_engineering.md
image_meta_description: "User testing notes being uploaded into a synthesis tool — raw quotes on the left, emerging themes on the right."
---

# Prompts: Test Phase

**Task:** Synthesise user feedback from testing

## Effective Prompt Structure

```
Context: We tested prototype with 6 users.
         Here are verbatim feedback notes.
Task: Identify themes across feedback, noting contradictions
      and edge cases.
Constraints:
- Ground themes in specific user quotes (cite which user, session)
- Flag contradictions (where users disagreed)
- Identify edge cases (unusual responses)
- Do NOT interpret significance — describe what users said/did
Format: For each theme:
  (1) theme description
  (2) supporting quotes with citations
  (3) contradictions if any
  (4) frequency (how many users mentioned)
```

## Common Failure

"What did users think?" — no source grounding, invites speculation, misses contradiction handling. AI will smooth feedback into false consensus.

## Key Principle

AI identifies patterns in feedback, humans interpret significance. Never let AI tell you whether an idea is "good" — that's a human judgement requiring values, priorities, and strategy.

---

_Card Set: Prompt Engineering · Test_
_Source: [prompt_engineering.md](../prompt_engineering.md)_
