# Slide Architecture — Fundamentals of Innovation Literacy

## Two-Deck Structure

Workshop slides are organised as two distinct decks with different functions and generation workflows. All slides are participant-facing reference material — no facilitation content, speaker notes, or timing cues. Facilitation scripts live in `WEEK1_FACILITATION_GUIDE.md`.

### Deck 1: Element Learning Slides

**Purpose:** Visual reference cards — 2-3 cards per element. Functions as framework handoff material during reflection phases and as post-workshop reference for participants.

**When used:** During facilitated reflection (not during activities). Facilitator surfaces these at strategic moments: "Here's the map for what you just experienced."

**File location:** `Slides/Elements/` — one subfolder per element
**Naming:** `E[nn]_[ElementName]/` containing individual `.md` files per slide
**NotebookLM notebook:** `FIL Slides - Element Learning`

**Per-element subfolder structure:** Each element has its own folder containing 3-4 individual slide prep files:

- **Title slide** (`E[nn]_title.md`): Element name, cluster label, position in framework
- **Definition** (`E[nn]a_[name]_definition.md`): One-line definition, distinctive visual
- **In Practice** (`E[nn]b_[name]_in_practice.md`): Concrete examples from workshop experience
- **Key Distinctions** (`E[nn]c_[name]_distinctions.md`): Boundary statements preventing confusion with adjacent elements

| Folder | Element | Cluster | Slides |
|--------|---------|---------|--------|
| `E00_InnovationLiteracy/` | Innovation Literacy | Meta-framework | 3 (title + overview + What/How/Why breakdown) |
| `E01_Process/` | Process | The What | 4 |
| `E02_Interventions/` | Interventions | The What | 4 |
| `E03_Tools/` | Tools | The What | 4 |
| `E04_Skills/` | Skills and Competencies | The How | 4 |
| `E05_Mindset/` | Mindset | The How | 4 |
| `E06_Behaviours/` | Behaviours | The How | 4 |
| `E07_Environment/` | Environment | The How | 4 |
| `E08_Collaboration/` | Collaboration | The How | 4 |
| `E09_Facilitation/` | Facilitation | The How | 4 |
| `E10_Governance/` | Governance | The Why | 4 |
| `E11_Resources/` | Resources | The Why | 4 |

**Total: 47 slides across 12 subfolders (one file per slide)**

### Deck 2: Workshop Flow Slides

**Purpose:** Session-specific visual anchors — provocations, activity instructions, transition markers, reflection scaffolds. These drive the workshop forward from the participant's perspective.

**When used:** Throughout each session. Slides run in parallel with Mural as the collaborative working canvas.

**File location:** `Slides/Flow/`
**Naming:** `D1M_01_opening_provocation.md`, `D1A_03_intervention_speed_dating.md`, etc.
**Prefix convention:** `D1M` = Day 1 Morning, `D1A` = Day 1 Afternoon, `D2M` = Day 2 Morning, `D2A` = Day 2 Afternoon
**NotebookLM notebooks:** One per session — `FIL Slides - D1 Morning`, `FIL Slides - D1 Afternoon`, etc.

| File | Session | Content |
|------|---------|---------|
| `D1M_01_opening_provocation.md` | Day 1 Morning | Draw Your Ideal Innovation Process |
| `D1M_02_introductions_mural.md` | Day 1 Morning | Introductions and Mural Onboarding |
| `D1M_03_wallet_project.md` | Day 1 Morning | IDEO Wallet Project (overview) |
| `D1M_03a_false_start.md` | Day 1 Morning | False Start — "3 minutes. Go." |
| `D1M_03b_intervention_dig_deeper.md` | Day 1 Morning | Dig Deeper intervention |
| `D1M_03c_synthesis_to_test.md` | Day 1 Morning | Synthesis through Testing phases |
| `D1M_04_morning_close.md` | Day 1 Morning | Morning Close |
| `D1A_00_afternoon_opening.md` | Day 1 Afternoon | Afternoon Opening |
| `D1A_01_deep_reflection.md` | Day 1 Afternoon | Deep Reflection on Wallet Project |
| `D1A_02_failure_analysis.md` | Day 1 Afternoon | Failure Analysis Workshop |
| `D1A_03_intervention_speed_dating.md` | Day 1 Afternoon | Intervention Speed-Dating |
| `D1A_04_measurement_game.md` | Day 1 Afternoon | The Measurement Game |
| `D1A_05_problem_space_map.md` | Day 1 Afternoon | Problem Space Map |
| `D1A_06_homework.md` | Day 1 Afternoon | Homework Assignment |
| `D2M_placeholder.md` | Day 2 Morning | PLACEHOLDER — Gift-Giving Project |
| `D2A_placeholder.md` | Day 2 Afternoon | PLACEHOLDER — Governance and Resources |

| Session | Prefix | Time | Status |
|---------|--------|------|--------|
| Day 1 Morning | D1M | 9:00–11:00 | Complete (7 slides) |
| Day 1 Afternoon | D1A | 14:00–16:10 | Complete (7 slides) |
| Day 2 Morning | D2M | 9:30–11:00 | UNFINISHED |
| Day 2 Afternoon | D2A | 14:00–16:00 | UNFINISHED |

---

## Slide Prep File Format

All slide prep files are purely participant-facing. They contain only what appears on the generated slide — no facilitation context, speaker notes, timing, transitions, or element tagging.

### Element Slides (Deck 1)

One file per slide, organised in per-element subfolders. Each file follows the same format:

```
# E01 — Process: Definition

## Slide Content

### Heading
Process

### Body
Structured, repeatable, learnable

### Visual Direction
Design Thinking five-phase cycle as non-linear loop...
```

A typical element subfolder contains:
```
E01_Process/
  E01_title.md                  (title card)
  E01a_process_definition.md    (definition)
  E01b_process_in_practice.md   (in practice)
  E01c_process_distinctions.md  (key distinctions)
```

### Flow Slides (Deck 2)

Single-card format, one file per slide:

```
# D1M — Opening Provocation

## Slide Content

### Heading
Draw Your Ideal Innovation Process

### Body
5 minutes. Silent. Pen and paper. Go.

### Visual Direction
Minimal — blank canvas feel. No diagrams, no frameworks, no hints.
```

---

## Content Separation Policy

| Content Type | Location | Purpose |
|---|---|---|
| What participants see on slides | Slide prep files (`Slides/Elements/`, `Slides/Flow/`) | NotebookLM source material for visual generation |
| How the facilitator delivers | `WEEK1_FACILITATION_GUIDE.md` | Facilitator scripts, timing, interventions, debrief questions |
| Workshop design and rationale | `WORKSHOP_OVERVIEW.md` | Canonical design document |
| Slide generation tooling | `SLIDE_GENERATION.md` | NotebookLM configuration, FUJI templates, accounts |

---

## NotebookLM Notebook Mapping

Each notebook contains ALL source files needed for its slide generation scope.

### Element Learning Notebook

| Notebook | Sources | Slides |
|----------|---------|--------|
| FIL Slides - Element Learning | All 12 element definitions (`Elements/[0-11]_*/What is *.md`), `FRAMEWORK_SUMMARY.md`, all Element slide preps (`Slides/Elements/E00_InnovationLiteracy/` through `E11_Resources/`) | E00–E11 (47 slides) |

### Workshop Flow Notebooks

| Notebook | Sources | Slides |
|----------|---------|--------|
| FIL Slides - D1 Morning | `WORKSHOP_OVERVIEW.md`, D1M slide preps, relevant element definitions | D1M_01–D1M_04 (7 slides) |
| FIL Slides - D1 Afternoon | `WORKSHOP_OVERVIEW.md`, D1A slide preps, relevant element definitions | D1A_00–D1A_06 (7 slides) |
| FIL Slides - D2 Morning | `WORKSHOP_OVERVIEW.md`, D2M slide preps [PENDING] | D2M_* |
| FIL Slides - D2 Afternoon | `WORKSHOP_OVERVIEW.md`, D2A slide preps [PENDING] | D2A_* |

### Source Upload Rules

Per the workspace Cursor rule (`notebooklm-slide-workflow.mdc`):
- Upload ALL content markdown files for the target scope
- Upload ALL slide prep documents for the target scope
- Do NOT upload YAML style specs as sources — pass YAML content as the `instructions` parameter to `generate_slide_deck`

---

## Relationship Between Decks

The two decks are complementary:

- **Flow slides** drive the session forward. They tell participants what to do, provoke thinking, and mark transitions.
- **Element slides** provide the conceptual map. They are surfaced during reflection phases when the facilitator names what participants have experienced.

During a typical reflection moment, the facilitator might switch from a Flow slide ("Mapping the Territory") to Element slides (E01 Process definition, E01 in practice), then back to Flow ("Where Did It Break?").

---

## Generation Workflow

1. Create/update slide prep files in `Slides/Elements/` or `Slides/Flow/`
2. Select or create the appropriate NotebookLM notebook
3. Upload all required sources (content files + slide preps)
4. Select YAML template from `_tools/_notebookLM/_slidedeckPrompts/fuji/templates/`
5. Pass YAML as `instructions` parameter to `generate_slide_deck`
6. Download, convert to PNG, review
7. Iterate template or slide prep content as needed

**Active template:** `techNeonArt/tech_neon_art_eirmersive.yaml` (Eirmersive custom)
**Daily generation limit:** 15 on Google AI Pro plan

---

## Archived Slides

The previous slide prep files (25 files, lecture-based three-section structure) are preserved in `_archive/`. These are retained for reference. The new two-deck structure replaces them entirely.

---

_Last updated: 2026-03-19 (subfolder structure, title slides added)_
