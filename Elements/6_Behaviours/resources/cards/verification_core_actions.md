---
element: 6
element_name: Behaviours
stage: all
type: reference
time_to_read: 3min
card_set: verification_discipline
related_cards:
  - four_gates_overview
  - verification_team_integration
  - verification_stage_application
  - failure_outsourced_cognition
  - failure_hallucination
source_doc: verification_discipline.md
image_meta_description: "A quality gate with three checkpoints — trace, challenge, compare — each one a distinct action at an inspection station."
---

# Verification Discipline: Core Actions

## Why It Matters

Verification discipline treats AI outputs as drafts requiring human interpretation — not answers requiring human approval. AI outputs are fast, confident, and well-structured. These characteristics create false confidence.

**Core principle:** "Comfort with AI output is inversely correlated with verification quality."

## The Five Core Actions

### 1. Run Four Gates Checks Routinely

After every AI generation: Alignment → Tension → Source Grounding → Bias. Not occasional spot-checks — systematic routine.

### 2. Resist Accepting First Plausible Output

First outputs rarely optimal. AI optimises for coherence, not correctness.
- Generate → Verify → Identify gaps → Refine prompt → Regenerate → Compare
- **Mindset shift:** First output = draft, not deliverable

### 3. Maintain Ownership of Interpretation

AI synthesises patterns, humans decide what patterns mean.

**Ownership language:**
- ✅ "AI spotted patterns — which resonate with what you observed?"
- ✅ "AI generated options — which serves our users best and why?"
- ❌ "AI says we should do X"
- ❌ "The data shows..." (it's AI interpretation, not objective fact)

### 4. Make Verification Visible to Team

Model it visibly — private verification doesn't build team capability.
- Talk through gate checks aloud
- Surface failures: "Gate 3 caught this — claim isn't grounded"
- Normalise as professional practice, not distrust

### 5. Treat AI Failures Diagnostically

Poor output reveals what was underspecified in your thinking.
- Don't blame AI — ask "What did we fail to specify?"
- Diagnose prompt logic: "Which constraints were ambiguous?"
- Reframe failures as useful diagnostic data

## Building the Habit

| Week | Goal | Time per Check | Outcome |
|------|------|---------------|---------|
| 1 | Deliberate practice | 2-3 min | Conscious competence |
| 2-3 | Pattern recognition | ~1 min | Diagnostic capability |
| 4+ | Automatic verification | ~30 sec | Unconscious competence |

---

_Card Set: Verification Discipline · Core Actions_
_Source: [verification_discipline.md](../verification_discipline.md)_
