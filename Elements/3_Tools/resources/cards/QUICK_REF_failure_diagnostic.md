---
element: 3
element_name: Tools
type: quick-reference
time_to_read: 1min
card_set: ai_tool_failure_modes
source_doc: ai_tool_failure_modes.md
---

# ⚡ QUICK REF: Failure Mode Diagnostic

When AI output is unsatisfactory, walk through this tree:

```
Unsatisfactory AI Output
    ↓
Was prompt clear and constrained?
    → No → Mode 7: Prompt Quality
    → Yes ↓
Is output too polished for current phase?
    → Yes → Mode 3: Premature Convergence
    → No ↓
Does output validate ALL your assumptions?
    → Yes → Mode 1: Echo Chamber
    → No ↓
Can claims be traced to source material?
    → No → Mode 5: Hallucination
    → Yes ↓
Did AI do cognitive work humans should own?
    → Yes → Mode 4: Outsourced Cognition
    → No ↓
Did we skip process steps to use AI faster?
    → Yes → Mode 6: Process Acceleration
    → No ↓
Is this synthetic data instead of real research?
    → Yes → Mode 2: Synthetic Users
    → No → Output may be appropriate — verify with Four Gates
```

## Prevention Summary

| Mode | Primary Prevention | Gate Check |
|------|-------------------|------------|
| 1. Echo Chamber | Request challenge | Gate 4 |
| 2. Synthetic Users | Hard rule: no AI research | Process discipline |
| 3. Premature Convergence | Fidelity matching | Gate 1 |
| 4. Outsourced Cognition | Assisted synthesis | Gates 1, 3 |
| 5. Hallucination | Source-grounded tools | Gate 3 |
| 6. Process Acceleration | Maintain phase gates | Facilitation |
| 7. Prompt Quality | Treat as core skill | Gate 1 |

---

_Quick Reference · Failure Mode Diagnostic_
