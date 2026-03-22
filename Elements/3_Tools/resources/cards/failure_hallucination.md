---
element: 3
element_name: Tools
stage: all
type: diagnostic
time_to_read: 2min
card_set: ai_tool_failure_modes
related_cards:
  - gate_source_grounding
  - interventions_discovery
  - interventions_test
  - verification_core_actions
source_doc: ai_tool_failure_modes.md
image_meta_description: "A confident document filled with footnotes — but when you look closely, every citation number leads to a blank page."
---

# Failure Mode 5: Hallucination Acceptance

## What Happens

AI generates plausible but inaccurate information. Humans accept without verification because outputs are confident and well-structured.

## Why It Occurs

- AI outputs have authoritative tone signalling confidence
- Humans assume confident = accurate
- Verification feels like questioning competence, not quality control
- Speed pressure encourages accepting first output

## How It Shows Up

- **Research:** "Research" citing non-existent sources. Statistics without data support ("80% of users struggle with X")
- **Problem Framing:** User needs that sound realistic but weren't in interview data
- **Evaluation:** Market analysis with plausible but unverifiable claims

## Example

**AI Output:** "80% of test participants struggled with navigation. Primary concern was inability to find search function."

**Source Check:** Only 3 of 6 participants mentioned navigation. None quantified attempts. Search function wasn't mentioned.

**Problem:** AI quantified without data, generalised from limited mentions, added specific details that weren't in sources.

## Prevention

1. **Gate 3 (Source Grounding):** "Can we trace this claim to specific source material?"
2. **Use RAG-based tools for research:** NotebookLM (source-grounded) over general LLMs. Upload sources, don't rely on training data
3. **Verification behaviour:** Always check AI synthesis against original data. Flag quantification when sources don't support

## When It Matters Most

**Discovery synthesis and Test feedback analysis** — where grounding in real data is critical to everything downstream.

---

_Card Set: AI Tool Failure Modes · Mode 5_
_Source: [ai_tool_failure_modes.md](../ai_tool_failure_modes.md)_
