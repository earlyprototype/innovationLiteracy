---
element: 2
element_name: Interventions
stage: test
type: structured-method
time_to_read: 3min
card_set: ai_augmented_interventions
related_cards:
  - four_gates_overview
  - gate_source_grounding
  - gate_bias_amplification
  - failure_echo_chamber
  - failure_hallucination
  - verification_core_actions
source_doc: ../(../../ai_augmented_interventions.md)
image_meta_description: "A user testing a prototype with a facilitator observing from across the table — the AI screen visible but deliberately pushed to the side."
---

# AI-Augmented Interventions: Test Phase

## Why It Matters

Testing is investigation, not validation. AI can synthesise feedback patterns efficiently — but cannot substitute for genuine user testing. The biggest risk: teams asking AI "would users like this?" instead of putting prototypes in front of real people. Interventions here enforce the boundary between AI-assisted analysis and human-sourced data.

## Pattern Interrupts

**"Test with humans, not AI"**
- AI cannot substitute for genuine user feedback
- Prevents: Synthetic testing, asking AI "would users like this?"
- Application: Hard rule — AI synthesises human feedback, doesn't replace collecting it

**"AI as documentation assistant"**
- Use AI to synthesise feedback themes, not to validate whether ideas are good
- Prevents: Echo chamber effect, confirmation bias
- Application: Frame AI role explicitly: "AI identifies patterns, we interpret significance"

**"Resistance is data"**
- When users reject AI-generated solutions, diagnose why
- Is prompt logic broken? Wrong problem? Poor execution?
- Application: User rejection triggers investigation, not defensiveness

## Structured Methods

### Feedback Synthesis Protocol
1. Collect human feedback through structured testing (think-aloud, observation, interviews)
2. Document verbatim: What users said, what they did, what surprised them
3. Upload feedback notes to NotebookLM or paste into Claude
4. Prompt AI: "Identify the top 3-5 themes, noting contradictions and edge cases"
5. For each AI-identified theme, verify against source feedback (trace to specific quotes)
6. Humans interpret significance: Which themes matter most? What do they reveal?
7. Plan iterations based on interpretation

**Tools:** NotebookLM (source-grounded synthesis), Claude (large context)
**Why it works:** AI handles pattern recognition, humans maintain interpretive ownership
**Prevents:** Outsourced cognition (Mode 4), Hallucination (Mode 5)

### Verification Protocol for Synthesised Insights
1. For each AI-synthesised insight, ask: "Can we trace this back to specific user feedback?"
2. If yes: Document which test sessions, which users, what they said
3. If no: Flag as speculative, exclude from iteration planning
4. Check for contradictory feedback AI may have smoothed over
5. Identify edge cases or outlier responses AI may have dismissed

**Tools:** NotebookLM (enables source-linking), manual review of test notes
**Why it works:** Maintains grounding in real user data
**Prevents:** Hallucination acceptance (Mode 5), Echo chamber effect (Mode 1)

## Four Gates Cross-Check

- **Gate 1 — Alignment:** Did AI synthesise the feedback we actually received, or drifted to more convenient themes?
- **Gate 2 — Tension:** Does synthesis show contradictions and conflicts, or has AI smoothed into false consensus?
- **Gate 3 — Source Grounding:** Can every synthesised theme be traced to specific user quotes?
- **Gate 4 — Bias Amplification:** Is AI surfacing feedback that challenges assumptions, or only confirming our hypothesis?

## Integration with Traditional

- Traditional: "Don't defend your prototype" (observe behaviour)
- AI-augmented: "Test with humans, not AI" (no synthetic validation)
- Work together: Both maintain focus on real user feedback

---

_Card Set: AI-Augmented Interventions · Test Phase_
_Source: [ai_augmented_interventions.md]((../../ai_augmented_interventions.md))_
