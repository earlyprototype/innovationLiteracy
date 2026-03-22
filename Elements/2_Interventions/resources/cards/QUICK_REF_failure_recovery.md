---
element: 2
element_name: Interventions
type: quick-reference
time_to_read: 1min
card_set: ai_augmented_interventions
source_doc: ai_augmented_interventions.md
---

# ⚡ QUICK REF: Intervention Recovery

When things go wrong during AI-augmented work, here's what to deploy:

## By Symptom

| Symptom | Intervention | Card |
|---------|-------------|------|
| AI confirms everything | "What's wrong with this?" + Gate 4 | failure_echo_chamber |
| Output too polished too early | "Low-resolution first" + constrain fidelity | failure_premature_convergence |
| Participants accept without checking | "Verify against source" + Gate 3 | failure_outsourced_cognition |
| AI generates plausible fiction | Source Grounding check + RAG tools | failure_hallucination |
| Team skipping process steps | "AI accelerates WITHIN phases" | failure_process_acceleration |
| Generic/useless outputs | Prompt co-creation + add constraints | failure_prompt_quality |
| Asking AI for user needs | "Hard no. Test with humans." | failure_synthetic_users |

## By Phase

| Phase | Most Likely Failure | First Intervention |
|-------|-------------------|-------------------|
| Discovery | Synthetic Users, Hallucination | "Verify against source" |
| Define | Echo Chamber, Outsourced Cognition | "Alignment check" |
| Ideate | Premature Convergence | "Human ideas first" |
| Prototype | Prompt Quality | "Prompt iteration IS prototyping" |
| Test | Hallucination, Echo Chamber | "Test with humans, not AI" |

## Universal Recovery Steps

1. **Pause** — don't skip the failure
2. **Diagnose** — "What did we fail to specify?"
3. **Refine** — update prompt, add constraints
4. **Regenerate** — compare new output
5. **Learn** — "What does this teach us?"

---

_Quick Reference · Intervention Recovery_
