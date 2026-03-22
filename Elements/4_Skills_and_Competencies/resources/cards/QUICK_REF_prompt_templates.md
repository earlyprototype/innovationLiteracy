---
element: 4
element_name: Skills and Competencies
type: quick-reference
time_to_read: 1min
card_set: prompt_engineering
source_doc: prompt_engineering.md
---

# ⚡ QUICK REF: Prompt Templates

## Universal Structure

```
Context: [Background, audience, purpose]
Task: [Specific action]
Constraints: [Boundaries, exclusions, format]
Format: [Desired output structure]
```

## Per-Stage Templates

**Discovery:** "Identify top 3-5 patterns across these [N] observations, noting contradictions. Cite observation numbers."

**Define:** "Generate 5 HMW framings emphasizing different stakeholder perspectives. Do NOT embed solutions. Ground in [discovery insights]."

**Ideate:** "Generate 10 variations on [concepts] that maintain [user needs] and [constraints]. Show trade-offs. Range incremental to ambitious."

**Prototype:** "Generate [artifact type] showing [components]. Low-resolution only. Show decision points. Format as [Mermaid/text]."

**Test:** "Identify themes across [N] users' feedback. Ground in specific quotes. Flag contradictions. Do NOT interpret significance."

## Common Mistakes → Fixes

| Mistake | Fix |
|---------|-----|
| "Improve this" | Define success criteria |
| "Make it user-friendly" | Specify what that means for YOUR users |
| Accept first output | Budget 2-3 iterations |
| "Generate ideas" | Provide seed concepts + constraints |
| "Which should we choose?" | Request analysis, keep human decision |

---

_Quick Reference · Prompt Templates_
