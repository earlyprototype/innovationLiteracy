---
element: 4
element_name: Skills and Competencies
stage: all
type: checklist
time_to_read: 2min
card_set: four_gates_verification
related_cards:
  - four_gates_overview
  - prompts_fundamentals
  - failure_echo_chamber
source_doc: four_gates_verification.md
image_meta_description: "A compass needle wavering between the intended question and the answered question — measuring drift."
---

# Gate 1: Alignment Check

**Question:** Did AI answer your actual question or drift to an adjacent easier problem?

## Why It Matters

AI optimises for plausible-sounding answers. When your question is complex or ambiguous, AI drifts to simpler related questions it can answer confidently. You get a confident answer to the wrong question.

## How to Check

1. Compare AI output to your original prompt intent
2. Ask: "Is this answering what I asked, or something adjacent?"
3. Look for scope drift (broader or narrower than requested)
4. Check if AI reframed your question without acknowledgment

## Red Flags

- Output feels complete but addresses different problem than asked
- Solution to adjacent problem that's easier to solve
- Output sounds authoritative but isn't what you need

## Example Failure

**Prompt:** "How can we help users track receipts without adding cognitive load?"

**AI Output:** "Here are 5 receipt tracking apps users can adopt"

**Problem:** AI answered "what tools exist?" not "how to reduce cognitive load"

## Recovery

Refine prompt to specify what you're NOT asking for: "Do not suggest existing apps — focus on reducing friction in current workflow"

**Learning:** What did you assume was obvious that AI missed?

## When to Apply

After every AI generation, before accepting output. Primary emphasis in **Define** and **Prototype** phases.

---

_Card Set: Four Gates Verification · Gate 1_
_Source: [four_gates_verification.md](../four_gates_verification.md)_
