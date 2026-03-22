---
element: 4
element_name: Skills and Competencies
stage: all
type: reference
time_to_read: 3min
card_set: four_gates_verification
related_cards:
  - gate_alignment
  - gate_tension
  - gate_source_grounding
  - gate_bias_amplification
  - verification_core_actions
source_doc: four_gates_verification.md
image_meta_description: "Four interconnected gates forming a verification checkpoint — each gate a different colour, each asking a different question."
---

# Four Gates Verification: Overview

## Why It Matters

Four Gates Verification is a systematic methodology for evaluating AI outputs before accepting them. Developed by Szczepanski (2026), it catches failures that don't appear as failures — plausible but flawed AI generation.

**Core principle:** "Comfort with AI output is inversely correlated with verification quality." When AI output feels perfect, verification is most needed.

## The Four Gates

| Gate | Question | Catches |
|------|----------|---------|
| **1. Alignment** | Did it answer my actual question? | Scope drift, wrong problem solved |
| **2. Tension** | Are trade-offs visible? | Over-smoothing, false perfection |
| **3. Source Grounding** | Can I trace claims to sources? | Hallucination, fabricated data |
| **4. Bias** | Is it challenging my assumptions? | Echo chamber, confirmation bias |

## Quick Reference: Running the Gates

After every AI generation, ask:

1. **Alignment:** Did it answer my actual question? ✓/✗
2. **Tension:** Are trade-offs visible? ✓/✗
3. **Source Grounding:** Can I trace claims to sources? ✓/✗
4. **Bias:** Is it challenging my assumptions? ✓/✗

**If any gate fails:** Don't accept output as-is. Diagnose and iterate.

## Stage-Specific Emphasis

| Stage | Primary Gates | Why |
|-------|--------------|-----|
| Discovery | Gates 3, 4 | Source grounding + bias prevention |
| Define | Gates 1, 4 | Alignment + assumption challenge |
| Ideate | Gates 2, 1 | Trade-offs + problem connection |
| Prototype | Gates 1, 2 | Intent match + complexity visibility |
| Test | Gates 3, 2 | Source grounding + contradiction preservation |

## Common Questions

- **"Doesn't this slow things down?"** — 30 seconds per check. Catching failures early saves hours building on flawed foundations
- **"When can I skip it?"** — Low-stakes, easily reversible outputs only. For decisions and synthesis — always verify
- **"Can AI verify itself?"** — Partially. Source grounding and bias checks require human judgement

## Building the Habit

- **Week 1:** Deliberately run all four gates, document results
- **Week 2:** Notice which gates catch issues most in your context
- **Week 3:** Verification becomes automatic, takes seconds

---

_Card Set: Four Gates Verification · Overview_
_Source: [four_gates_verification.md](../four_gates_verification.md)_
