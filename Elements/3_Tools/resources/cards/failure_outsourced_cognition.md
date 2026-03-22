---
element: 3
element_name: Tools
stage: all
type: diagnostic
time_to_read: 2min
card_set: ai_tool_failure_modes
related_cards:
  - interventions_discovery
  - interventions_define
  - interventions_test
  - verification_core_actions
  - gate_alignment
  - gate_source_grounding
source_doc: ai_tool_failure_modes.md
image_meta_description: "A brain on a desk with a USB cable running from it into a computer — the brain dimming as the screen brightens."
---

# Failure Mode 4: Outsourced Cognition

## What Happens

AI does the difficult cognitive work (synthesis, problem framing, evaluation). Humans just approve outputs. Learning doesn't transfer, capability stays with AI.

## Why It Occurs

- Cognitive offloading is seductive — AI is fast and plausible
- Organisations prioritise outputs over capability building
- Lack of clear ownership: Who interprets? Who decides?

## How It Shows Up

- **Synthesis:** "AI identified these pain points" without human verification. No understanding of WHY patterns matter
- **Problem Framing:** "AI says we should solve X" without human interpretation
- **Decision-Making:** Deferring strategic decisions to AI outputs. Missing opportunity for human judgement

## Example

**Process:** Paste interview notes into NotebookLM → Prompt "Identify top 3 friction points" → AI generates list → Team accepts and moves to ideation

**Problem:** Participants didn't verify patterns against quotes, didn't interpret significance, didn't maintain understanding of user context. Learning stayed with AI.

## Prevention

**Assisted synthesis protocol (not outsourced synthesis):**
1. Humans extract observations manually (5-7 per source)
2. AI identifies patterns across observations
3. Humans interpret significance: Which matter for OUR context?
4. Humans select actual problem to solve

**Ownership language:**
- "AI synthesised these patterns — which ones matter for YOUR users?"
- "You own the interpretation, not the AI"

## When It Matters Most

**All phases** — especially **Define** (problem framing) and **Test** (interpreting feedback) where human judgement is critical.

---

_Card Set: AI Tool Failure Modes · Mode 4_
_Source: [ai_tool_failure_modes.md](../ai_tool_failure_modes.md)_
