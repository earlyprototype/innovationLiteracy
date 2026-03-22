# Proposal: Modular Card Structure for AI Integration Resources

**Date:** 21 March 2026  
**Status:** ✅ Complete — All phases delivered
**Revision:** Final audit and index completion 21 March 2026

---

## Delivery Summary

### Total Card System: 88 files across 11 Elements

| Element | Topic Cards | Quick Refs | Index | Total |
|---------|-------------|------------|-------|-------|
| 1 — Process | 5 | 1 | 1 | 7 |
| 2 — Interventions | 12 | 1 | 1 | 14 |
| 3 — Tools | 9 | 1 | 1 | 11 |
| 4 — Skills & Competencies | 13 | 2 | 1 | 16 |
| 5 — Mindset | 3 | 1 | 1 | 5 |
| 6 — Behaviours | 5 | 1 | 1 | 7 |
| 7 — Environment | 2 | 1 | 1 | 4 |
| 8 — Collaboration | 3 | 0 | 1 | 4 |
| 9 — Facilitation | 8 | 2 | 1 | 11 |
| 10 — Governance | 3 | 1 | 1 | 5 |
| 11 — Resources | 2 | 1 | 1 | 4 |
| **Totals** | **65** | **12** | **11** | **88** |

### Method Used
Every card follows the established structure:
1. **Read source doc fully**
2. **Decompose based on size:** compact docs (< 30 lines) → 1 card; medium → 1-2; large → 3-5
3. **Write YAML frontmatter** (`element`, `element_name`, `stage`, `type`, `time_to_read`, `card_set`, `related_cards`, `source_doc`)
4. **Extract and restructure content** for 2-4 min focused, actionable reads
5. **Cross-reference** related cards across elements
6. **Create quick refs** for high-frequency lookups and **indices** for navigation

### Completed Tasks
- [x] Phase 1: 33 AI integration topic cards + 7 QR + 5 indices (Elements 2, 3, 4, 6, 9)
- [x] Phase 2: 32 foundational topic cards + 5 QR + 6 new indices (Elements 1, 5, 7, 8, 10, 11)
- [x] Phase 1 index updates: all 5 existing indices updated to include Phase 2 cards
- [x] Verification pass: file counts, YAML frontmatter, cross-references confirmed

---

## Current State

Phase 1 delivered 7 comprehensive AI integration resources (2,750+ lines total) covering interventions, facilitation, skills, behaviours, and tools. These documents are thorough and research-backed but substantial (350-550 lines each), making them challenging for quick reference during live workshop delivery.

---

## Proposed Solution: Three-Layer Modular Card System

> **Principle: Retain + Add.** Comprehensive docs remain as canonical references and NotebookLM source material. Modular cards are created *alongside* them, not as replacements.

### Layer 1: Topic Cards (80-120 lines each)
**Focused, digestible resources organized by stage or pattern**

- **33 topic cards** breaking comprehensive docs into modular units
- Discovery, Define, Ideate, Prototype, Test organization
- Self-contained yet cross-referenced
- Each follows consistent structure with YAML frontmatter metadata

**Card decomposition (pressure-tested: "would a facilitator grab this card independently?"):**
- AI-Augmented Interventions → 6 cards (one per stage + cross-stage)
- AI-Augmented Facilitation → 6 cards (prep + 4 patterns + failure handling)
- AI Tool Failure Modes → 7 cards (one per failure mode — natural diagnostic units)
- Prompt Engineering → 6 cards (fundamentals + 5 stage-specific)
- Four Gates Verification → 5 cards (overview + 4 gates)
- Verification Discipline → 3 cards (core actions & habit building, team integration, stage application)

### Layer 2: Quick Reference Cards (1-page format)
**At-a-glance guides for live workshop use — one per session block minimum**

- Four Gates Checklist (4 questions, colour-coded)
- AI Facilitation Patterns (timing and key moves)
- Failure Mode Diagnostic (flowchart format)
- Prompt Templates (copy-paste ready per stage)
- Verification Team Language (phrases that work)
- Session Opening AI Framing Script (how to introduce AI role)
- AI Failure Recovery Moves (what to do when AI breaks mid-exercise)

### Layer 3: Card Set Indices (navigation)
**PipDecks-style organization with clear pathways**

- Index per card set showing all cards and their relationships
- Navigation by element, by stage, by problem, or by learning objective
- Links to related quick reference materials
- Links back to comprehensive source documents

### Card Metadata Frontmatter

Every card carries structured metadata for navigation, filtering, and element-linking:

```yaml
---
element: 2
element_name: Interventions
stage: discovery  # discovery | define | ideate | prototype | test | cross-stage | all
type: structured-method  # pattern-interrupt | structured-method | diagnostic | reference | checklist
time_to_read: 3min
card_set: ai_augmented_interventions
related_cards:
  - four_gates_overview
  - verification_discipline_core
source_doc: ai_augmented_interventions.md
---
```

**Metadata enables:**
- Filter by element ("show me all Element 4 cards")
- Filter by stage ("what do I need for Ideate?")
- Filter by type ("give me all diagnostics")
- Trace back to comprehensive source document
- Build future tooling (card browser, Mural import)

---

## Benefits

**For Facilitators:**
- Study manageable chunks during preparation
- Quick reference during live delivery
- Navigate by specific need (stage, problem, pattern)
- Print individual cards as session handouts

**For Practitioners:**
- Learn one skill/pattern at a time
- Clear progression through material
- Easy to locate specific guidance
- Quick refreshers without rereading everything

**For Workshop Design:**
- Assign specific cards as pre-reading
- Reference cards directly in facilitation scripts
- Mix and match for custom sequences
- Reduced cognitive load

**For Maintenance:**
- Update individual cards without restructuring
- Add new cards as practice evolves
- Clearer change tracking
- Version control at card level

---

## Relationship to Mural Board

Modular cards and the Mural board serve **different purposes** and should not be conflated:

| | Modular Cards | Mural Board |
|---|---|---|
| **Purpose** | Facilitator prep + reference | Participant interaction |
| **When used** | Before and between sessions | During live exercises |
| **Content type** | Conceptual, methodological | Activity spaces, templates |
| **Format** | Markdown files with metadata | Visual zones with sticky notes |

**Topic cards** → source material for slide groups  
**Quick reference cards** → facilitator's live companion  
**Neither replaces the Mural board**, which is structured separately as interactive zones

---

## File Structure Impact

**Retained:** All original comprehensive docs as canonical source + NotebookLM material

**Added alongside:** 
- **65 topic cards** organized in `cards/` subfolder within existing element folders
- **12 quick reference cards** prefixed with `QUICK_REF_`
- **11 index files** prefixed with `_INDEX_`
- **Total: 88 modular files** added alongside existing comprehensive docs

**Folder organization (all 11 elements):**
- Elements/1_Process/resources/cards/
- Elements/2_Interventions/resources/cards/
- Elements/3_Tools/resources/cards/
- Elements/4_Skills_and_Competencies/resources/cards/
- Elements/5_Mindset/resources/cards/
- Elements/6_Behaviours/resources/cards/
- Elements/7_Environment/resources/cards/
- Elements/8_Collaboration/resources/cards/
- Elements/9_Facilitation/resources/cards/
- Elements/10_Governance/resources/cards/
- Elements/11_Resources/resources/cards/

---

## Implementation Approach

**Phase 1:** Break down existing comprehensive resources into topic cards (retain all content, restructure into modular format)

**Phase 2:** Create quick reference cards (distill key patterns into 1-page lookup format)

**Phase 3:** Build indices (provide navigation and card relationships)

**Phase 4:** Update element files and RECENT_CHANGES.md to reflect new structure

**Effort:** Medium (content extraction and restructuring, not new writing)

**Timeline:** 1-2 sessions to complete all layers

**Risk:** Low (all content already validated, comprehensive docs retained, additive only)

**Post-Workshop Refinement:** After delivery, review which cards were actually grabbed during live facilitation. Merge cards that were always used together, split any that proved too broad, and adjust metadata based on real usage patterns.

---

## Approach: Retain Comprehensive + Add Modular

**Approved approach:** Keep existing comprehensive docs as canonical references AND create modular card system alongside.

**Rationale:**
- Comprehensive docs serve as NotebookLM source material for slide generation
- Cards are additive — no content destroyed, no links broken
- Post-workshop refinement will evidence which cards earn their place
- Comprehensive docs remain the single source of truth; cards are views into them

---

## Example Card Format

```markdown
# AI Interventions: Discovery Phase

## Why It Matters
Discovery synthesis with AI can accelerate pattern identification 
whilst maintaining grounding in real user data. Critical: Humans 
must own interpretation, AI assists with analysis.

## Pattern Interrupts
- "AI synthesises, humans interpret"
- "Verify against source"
- "What did AI miss?"

## Structured Methods

### Assisted Synthesis Protocol
1. Humans extract observations manually (5-7 per source)
2. AI identifies patterns across observations
3. Humans interpret significance and select insights
4. Document decision rationale

**Tools:** NotebookLM, Claude
**Why it works:** Humans own difficult cognitive work
**Prevents:** Outsourced cognition

[Full detailed guidance continues...]

## Related Cards
- [Four Gates Verification](../../4_Skills_and_Competencies/resources/four_gates_overview.md)
- [Verification Discipline](../../6_Behaviours/resources/verification_discipline_core_actions.md)
- [QUICK_REF: Four Gates Checklist](QUICK_REF_four_gates_checklist.md)
```

---

## Recommendation

**Proceed with additive modular card creation** — builds an elegant, accessible, practitioner-friendly card layer on top of existing comprehensive guides. All research-backed content preserved in both forms.

**Outcome:** World-class modular resource library matching best-in-field toolkits (PipDecks, IDEO Method Cards) whilst maintaining Creative Spark's distinctive voice, research foundation, and NotebookLM-ready source documents.

---

**Decision:** ✅ Approved — retain + add modular  
**Status:** ✅ Complete — 88 modular files delivered across all 11 elements  
**Next:** Refine post-workshop based on live delivery evidence

_Proposal prepared: 21 March 2026_  
_Feedback integrated: 21 March 2026_  
_Final delivery: 21 March 2026_
