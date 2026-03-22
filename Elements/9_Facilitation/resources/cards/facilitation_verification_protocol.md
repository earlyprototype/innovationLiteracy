---
element: 9
element_name: Facilitation
stage: all
type: structured-method
time_to_read: 2min
card_set: ai_augmented_facilitation
related_cards:
  - facilitation_pre_session
  - four_gates_overview
  - interventions_test
source_doc: ai_augmented_facilitation.md
image_meta_description: "A facilitator modelling the Four Gates check — pausing after AI output to demonstrate each gate question for the group."
---

# Facilitation: Verification Protocol

**Use case:** Synthesise feedback from user testing sessions with group verification.

## Facilitation Moves

### 1. Collect Human Feedback (pre-workshop)
- Structured testing: think-aloud, observation, interviews
- Document verbatim

### 2. AI Synthesis (5 min)
- Upload feedback notes to NotebookLM
- Prompt: "Identify top 3-5 themes, noting contradictions and edge cases"

### 3. Run Four Gates as Group Exercise (15 min)
- **Alignment:** "Did AI answer our question or something adjacent?"
- **Tension:** "Are trade-offs visible or is this suspiciously neat?"
- **Source Grounding:** "Can we trace this insight back to specific user feedback?"
- **Bias:** "Is AI reflecting our assumptions or challenging them?"

### 4. Human Interpretation (10 min)
- "Which themes matter most?"
- "What do they reveal about our solution/problem framing?"
- "How do we iterate based on this?"

## Key Language

- "AI identified these themes — now let's verify them"
- "For each theme, find the actual user quotes that support it"
- "What's missing from this synthesis that you saw in testing?"

## Failure Mode Prevented

Accepting AI synthesis without verification (Hallucination Acceptance). Outsourcing interpretation to AI (Outsourced Cognition).

## Time: ~30 min total
(5 synthesis + 15 verification + 10 interpretation)

---

_Card Set: AI-Augmented Facilitation · Verification Protocol_
_Source: [ai_augmented_facilitation.md](../ai_augmented_facilitation.md)_
