---
element: 4
element_name: Skills and Competencies
stage: all
type: checklist
time_to_read: 2min
card_set: four_gates_verification
related_cards:
  - four_gates_overview
  - failure_hallucination
  - interventions_discovery
  - interventions_test
source_doc: four_gates_verification.md
image_meta_description: "A chain of citations traced backward — each link connecting a claim to its source document, with one link broken."
---

# Gate 3: Source Grounding Check

**Question:** Can you trace claims back to source material?

## Why It Matters

AI synthesises patterns, but also hallucinates — generates plausible-sounding claims not grounded in provided sources. For research synthesis, feedback analysis, and documentation tasks, source grounding is the difference between insight and fiction.

## How to Check

1. For each AI-synthesised insight, identify which source material supports it
2. Click through to source quotes (in NotebookLM) or manually verify
3. Ask: "Which interview/document/feedback session mentioned this?"
4. Flag claims that sound right but can't be linked to specific sources

## Red Flags

- Insights that sound plausible but lack source citations
- Quantification without data ("most users," "primary concern") when sources don't support
- Patterns that smooth over contradictions in source material
- Claims that go beyond what sources actually said

## Example Failure

**AI Output:** "Users primarily struggle with navigation complexity"

**Source Check:** Only 2 of 8 interview transcripts mentioned navigation; 6 mentioned data entry friction

**Problem:** AI elevated a minor theme to "primary" without grounding

## Recovery

Request citations: "For each theme, provide supporting quotes with source identifiers (which user, which session)"

**Learning:** Which sources were ambiguous? What additional context is needed?

## When to Apply

Any time AI synthesises research, feedback, or documentation. Primary emphasis in **Discovery** and **Test** phases.

---

_Card Set: Four Gates Verification · Gate 3_
_Source: [four_gates_verification.md](../four_gates_verification.md)_
