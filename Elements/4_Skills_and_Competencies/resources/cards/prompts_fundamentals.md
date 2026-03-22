---
element: 4
element_name: Skills and Competencies
stage: all
type: reference
time_to_read: 3min
card_set: prompt_engineering
related_cards:
  - prompts_discovery
  - prompts_define
  - prompts_ideate
  - prompts_prototype
  - prompts_test
  - four_gates_overview
  - failure_prompt_quality
source_doc: prompt_engineering.md
image_meta_description: "A well-structured blueprint with annotations — context, constraints, format, and intent laid out before construction begins."
---

# Prompt Engineering: Fundamentals

## Why It Matters

The quality of AI outputs depends directly on the quality of human prompts. Prompt engineering is not "learning to talk to AI" — it is learning to articulate intent clearly enough for literal execution. This skill transfers: clear intent specification improves delegation, brief writing, requirements docs, and cross-functional collaboration.

AI makes this skill visible because failures are immediate and unambiguous.

## Core Components

### 1. Context Provision
Background AI needs to understand the task.
- Poor: "Summarise this research"
- Better: "Summarise this user research for a product team deciding which problems to prioritise. Focus on user pain points and business impact."

### 2. Constraint Specification
Explicit boundaries that shape output.
- **Technical:** "Works within existing architecture"
- **User-centred:** "Addresses pain points from testing"
- **Resource:** "Implementable within 2 weeks"
- **Format:** "Output as bullet list, max 3 sentences each"

### 3. Success Criteria
How you'll evaluate whether output meets requirements.
- Poor: "Make this better"
- Better: "Rewrite to: (1) frame as question, (2) avoid embedding solutions, (3) specify target user group"

### 4. Examples & Formats
Show AI what good looks like. 1-3 examples dramatically improve quality.
- Poor: "Generate How Might We statements"
- Better: "Generate HMW statements: 'How might we [verb] [user need] [context]?' Example: 'How might we help busy parents track receipts without adding cognitive load?'"

### 5. Iterative Refinement
Budget time for 2-3 iterations, not single generation.
1. Write initial prompt → Generate → Evaluate → Diagnose → Refine → Regenerate → Document learning

## Common Mistakes

| Mistake | Example | Fix |
|---------|---------|-----|
| Underspecification | "Improve this design" | Define success criteria explicitly |
| Hidden Assumptions | "Make it user-friendly" | Specify what "user-friendly" means for YOUR users |
| Single-Shot Prompts | Accept first output | Budget 2-3 iterations |
| No Constraints | "Generate ideas" | Provide source documents as constraints |
| Requesting Decisions | "Which should we choose?" | Request analysis, maintain human decision-making |

## Transferable Learning

Prompt engineering skills transfer to: delegation, brief writing, requirements specification, cross-functional collaboration. AI makes intent specification visible through immediate diagnostic feedback.

---

_Card Set: Prompt Engineering · Fundamentals_
_Source: [prompt_engineering.md](../prompt_engineering.md)_
