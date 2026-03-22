---
element: 3
element_name: Tools
stage: all
type: diagnostic
time_to_read: 2min
card_set: ai_tool_failure_modes
related_cards:
  - interventions_discovery
  - verification_core_actions
source_doc: ai_tool_failure_modes.md
image_meta_description: "A mannequin seated in a user interview chair, holding scripted answers — while a real person waits unseen outside the door."
---

# Failure Mode 2: Synthetic User Substitution

## What Happens

AI-generated "user personas" or "synthetic interviews" replace actual human discovery. Innovation built on speculation instead of observation.

## Why It Occurs

- Pressure for speed makes synthetic users seductive
- Difficulty accessing real users creates temptation to substitute
- AI-generated content sounds plausible and realistic

## How It Shows Up

- **Discovery:** User needs based on AI speculation rather than interviews. Missing edge cases and emotional nuance
- **Problem Framing:** Problems defined based on assumed needs, not observed needs
- **Testing:** "Validation" from AI role-playing users instead of actual feedback

## Example

**Prompt:** "Generate typical user needs for patients managing chronic conditions"

**AI Output:** Detailed, reasonable-sounding list (medication tracking, appointment management, symptom logging)

**Problem:** Plausible but not grounded. Missing the specific friction points, workarounds, and emotional challenges real patients would reveal.

## Prevention

**Hard rule: AI cannot conduct empathy research.**

1. Budget time/resources for real user access upfront
2. AI can synthesise what humans learned, not replace the learning
3. Frame clearly: "AI assists synthesis, humans conduct discovery"

## When It Matters Most

**Discovery phase** — foundation of entire process depends on real human insight. Synthetic users corrupt everything downstream.

---

_Card Set: AI Tool Failure Modes · Mode 2_
_Source: [ai_tool_failure_modes.md](../ai_tool_failure_modes.md)_
