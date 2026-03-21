# Fundamentals of Innovation Literacy -- Project Handover

## Project Summary

A two-part, 6-hour workshop (3 hours per session) for **Eirmersive** (XR advocates and industry R&D partners), delivered under the FactoryXChange FX2 Services programme. The workshop covers innovation as a structured process, its constituent elements, and the organisational practices required to sustain it.

The content is complete. The current workstream is **automated slide deck generation** using Google NotebookLM and the FUJI Method (YAML-based design prompts), with the goal of finalising a visual style and producing presentation-ready slide decks for all three sections.

---

## Current Goal

**Finalise the Eirmersive slide template and generate production slide decks for all three workshop sections.**

Specifically:
1. A clean Section 1 notebook has just been created and generation triggered using the refined Eirmersive template (notebook ID: `cd8afd84-1709-49d9-aeeb-1c0c417cbfa9`, design account). This generation may or may not have completed -- check the notebook for artifacts.
2. The previous Section 1 test (from a shared notebook containing Section 0 content as well) produced 15 strong slides but surfaced several issues to address in the template. A slide-by-slide analysis was completed and shared with the client.
3. Once the template is confirmed, generate final decks for Section 0, Section 1, and Section 2.

---

## Known Issues with Current Template

From the slide-by-slide review of the first Section 1 generation:

| Issue | Detail | Template Fix Applied |
|---|---|---|
| "Helvetica" font name appearing as visible text | The typography instruction named font families, and the LLM printed them on-screen | Yes -- the generation prompt for the clean notebook was updated to say "do not display font names on screen." The saved `tech_neon_art_eirmersive.yaml` file still contains "Helvetica" and needs updating. |
| Full stops on labels and captions | Body captions consistently end with periods despite the no-punctuation rule | Partially -- the rule exists in the template but the LLM ignores it on body-text captions. May need stronger phrasing or acceptance as a limitation. |
| Grid density inconsistency | Grid backgrounds vary from sparse to very dense across slides | Yes -- a grid consistency rule was added to the generation prompt. The saved YAML file does not yet include this rule. |
| Content truncation (5-7 items reduced to 3-4) | Lists of concepts are trimmed to fit visual layouts | Systemic LLM behaviour, not template-addressable. Accept and compensate in speaker notes or handouts. |
| Engine-invented slides | 3 slides (2, 14, 15) were not in the source material | Neutral. Good editorial additions (synthesis/overview slides) but means output count differs from input. |
| Erratic font type switching mid-title | Font weight and style changes within individual words or titles | Not yet addressed. Likely related to the serif/sans-serif mixing instruction. |

---

## Workshop Content Structure

Root: `_Projects/FactoryXChange/FX2/Services/FundamentalsInnovationLiteracy/`

### Slide Architecture (Two-Deck Structure)

Full specification: `Slides/SLIDE_ARCHITECTURE.md`

Slides are organised as two distinct decks replacing the previous three-section structure. The old slide preps (25 files) are preserved in `[section]/Slides/_archive/` for reference.

**Deck 1: Element Learning Slides** — `Slides/Elements/`
Standalone visual reference, one per element. Used during reflection phases and as post-workshop reference.

| File | Element |
|------|---------|
| `E00_innovation_literacy.md` | Meta-framework overview |
| `E01_process.md` | Process |
| `E02_interventions.md` | Interventions |
| `E03_tools.md` | Tools |
| `E04_skills_and_competencies.md` | Skills and Competencies |
| `E05_mindset.md` | Mindset |
| `E06_behaviours.md` | Behaviours |
| `E07_environment.md` | Environment |
| `E08_collaboration.md` | Collaboration |
| `E09_facilitation.md` | Facilitation |
| `E10_governance.md` | Governance |
| `E11_resources.md` | Resources |

**Deck 2: Workshop Flow Slides** — `Slides/Flow/`
Session-specific facilitation support — visual anchors, provocations, activity instructions, transition markers, reflection scaffolds.

| File | Session | Activity |
|------|---------|----------|
| `D1M_01_opening_provocation.md` | Day 1 Morning | Draw Your Ideal Innovation Process |
| `D1M_02_introductions_mural.md` | Day 1 Morning | Introductions and Mural Onboarding |
| `D1M_03_wallet_project.md` | Day 1 Morning | IDEO Wallet Project |
| `D1M_04_morning_close.md` | Day 1 Morning | Morning Close and Afternoon Preview |
| `D1A_01_deep_reflection.md` | Day 1 Afternoon | Deep Reflection on Wallet Project |
| `D1A_02_failure_analysis.md` | Day 1 Afternoon | Failure Analysis Workshop |
| `D1A_03_intervention_speed_dating.md` | Day 1 Afternoon | Intervention Speed-Dating |
| `D1A_04_measurement_game.md` | Day 1 Afternoon | The Measurement Game |
| `D1A_05_problem_space_map.md` | Day 1 Afternoon | Problem Space Map Demo |
| `D1A_06_homework.md` | Day 1 Afternoon | Homework Assignment |
| `D2M_placeholder.md` | Day 2 Morning | PLACEHOLDER — Gift-Giving Project |
| `D2A_placeholder.md` | Day 2 Afternoon | PLACEHOLDER — Governance and Resources |

### Content Sources

**Outline:** `outline.md` — Master workshop outline (89 lines). Three sections.

**Section 0:** `0_Introduction/` — 0.1 WhatIsInnovation, 0.2 WhyDoesInnovationFail, 0.3 WhatDoWeMeanByLiteracy, 0.0 Bibliography

**Section 1:** `1_ElementsOfInnovation/` — 1.1 Process through 1.9 Environment

**Section 2:** `2_FromLIteracyToPractice/` — 2.1 PermissionThroughUnderstanding, 2.2 CoCreatingAnInnovationCharter, 2.3 DemonstratingValue

**Elements:** `Elements/[0-11]_[ElementName]/What is [ElementName].md` — all 12 definitions complete

### NotebookLM Notebook Mapping (New Structure)

| Notebook | Sources | Slides |
|----------|---------|--------|
| FIL Slides - Element Learning | All element definitions + FRAMEWORK_SUMMARY.md + Element slide preps | E00–E11 |
| FIL Slides - D1 Morning | WORKSHOP_OVERVIEW.md + D1M slide preps + relevant element defs | D1M_01–D1M_04 |
| FIL Slides - D1 Afternoon | WORKSHOP_OVERVIEW.md + D1A slide preps + relevant element defs | D1A_01–D1A_06 |
| FIL Slides - D2 Morning | WORKSHOP_OVERVIEW.md + D2M slide preps [PENDING] | D2M_* |
| FIL Slides - D2 Afternoon | WORKSHOP_OVERVIEW.md + D2A slide preps [PENDING] | D2A_* |

---

## Slide Generation System (FUJI Method)

Root: `_tools/_notebookLM/_slidedeckPrompts/fuji/`

### Key Files
- `FUJI_METHOD_CONTEXT.md` -- Full methodology documentation, workflow, and test log. Read this first.
- `fujiMasterSpec.yaml` -- Template structure reference for creating new YAML specifications.
- `README.md` -- Original setup notes.

### Templates
Location: `fuji/templates/`

Each template has a folder containing the YAML spec (Japanese `_jp.yaml` versions are the primary prompts):

| Template | Provenance | Notes |
|---|---|---|
| `techNeonArt/tech_neon_art.yaml` | Author original | The baseline. 52 lines. Produces the strongest results. |
| `techNeonArt/tech_neon_art_eirmersive.yaml` | Custom (ours) | Modified TechNeonArt for Eirmersive. 62 lines. Per-section accent colours, text limits, punctuation/language rules, photo guidance. **This is the active template being tested.** |
| `mckinseyConsulting/mckinseyConsulting_jp.yaml` | Rewritten lean | McKinsey consulting style. |
| `mckinseyConsulting/mckinseyConsulting_mintext_jp.yaml` | Custom (ours) | McKinsey variant with aggressive text limits. |
| `bravestNewWorld/bravestNewWorld_jp.yaml` | Custom (ours) | Eastern European urban resilience aesthetic. User disliked output -- deprioritised. |
| `japonismTextileFlow/japonismTextileFlow_jp.yaml` | Author original | Beautiful but too bold/nationally specific for this application. |
| `cosmicObservatory/cosmicObservatory_jp.yaml` | Custom (ours) | Deep space aesthetic. Never fully tested. |
| Other templates (11 total) | Author originals | Available but not tested with this project content. |

### Test Results
Location: `fuji/test_results/`

| File | Template | Content | Notes |
|---|---|---|---|
| `McKinsey_MinText_Section0.pdf` | McKinsey minimal-text | Section 0 | Clean but one-dimensional |
| `Eirmersive_Section1.pdf` | Eirmersive (v1) | Section 1 | 15 slides, strong but has known issues (see table above) |
| `Eirmersive_Section1_pages/` | -- | -- | PNG conversions of above |
| `Japonism_Section0.pdf` | Japonism Textile Flow | Section 0 | Stunning but inappropriate for client context |
| `TechNeonArt_Section0.pdf` | TechNeonArt (original) | Section 0 | Strong baseline reference |
| `BravestNewWorld_Section0.pdf` (in templates folder) | Bravest New World | Section 0 | User disliked |
| `Deck2_Section0.pdf` | Unknown (earlier test) | Section 0 | Earlier test run |

### Eirmersive Template: Design Decisions

The `tech_neon_art_eirmersive.yaml` template is a modification of the author's TechNeonArt original. Key design choices:

- **Per-section accent colours**: Neon Yellow (#DFFF00) for Section 0, Electric Cyan (#00E5FF) for Section 1, Signal Coral (#FF6B6B) for Section 2. Provides subtle visual distinction between workshop sections.
- **Text limit**: Maximum 20 words per slide body. Keywords and short phrases, not sentences.
- **No terminal punctuation** on headings, labels, or captions. Body text only.
- **UK/Irish English** only (organisation, recognise, colour).
- **Photo guidance**: Individual portraits preferred over group shots. Technical/mechanical imagery prioritised. Monochrome treatment with geometric overlay.
- **Typography**: Serif/sans-serif mixing for contrast. Thin font weights for body text. (Note: the saved YAML still names "Helvetica" and "Didot, Bodoni" explicitly -- the most recent generation prompt was modified to say "do not display font names on screen" but the YAML file itself was not updated.)

---

## NotebookLM Configuration

### MCP Server
- Location: `C:\Users\Fab2\Desktop\Work\notebooklm-py-MCP-full\notebooklm_mcp_server.py`
- Python: `C:\Users\Fab2\Desktop\Work\venv\Scripts\python.exe`
- Config: `C:\Users\Fab2\.cursor\mcp.json` (entry: `notebooklm`)

### Accounts
Three Google account profiles are configured:

| Profile | Config path | Status (as of 17 Mar 2026) |
|---|---|---|
| `personal` | `~/.notebooklm-personal` | Session expired. Needs re-authentication. Has Google AI Pro subscription (paid). |
| `work` | `~/.notebooklm-work` | Session expired. Needs re-authentication. |
| `design` | `~/.notebooklm-design` | Active. Currently selected. Free tier (limited generations). |

To re-authenticate a profile:
```bash
NOTEBOOKLM_HOME=~/.notebooklm-<profile> /c/Users/Fab2/Desktop/Work/venv/Scripts/notebooklm.exe login
```

The **personal account** is the preferred account for production work (paid Google AI Pro plan, higher daily generation limits).

### Active Notebooks

| Notebook | Account | ID | Purpose | Status |
|---|---|---|---|---|
| FIL Slides - Section 1: Elements of Innovation (Clean) | design | `cd8afd84-1709-49d9-aeeb-1c0c417cbfa9` | Clean Section 1 test with Eirmersive template | Generation triggered, completion unknown |
| FIL Slides - Section 1: Elements of Innovation (Eirmersive Test) | personal | `6cad0cee-0f15-42ab-9305-c9dcaa6f86ba` | First Section 1 test (may contain Section 0 residue) | Complete -- produced `Eirmersive_Section1.pdf` |

Earlier test notebooks exist across accounts but are not critical to the current workflow.

### Known Tool Limitations

1. **`download_slide_deck`** tends to return the most recently completed artifact regardless of which one is requested. If multiple decks exist in a notebook, manual download from the NotebookLM web UI may be necessary.
2. **`generate_slide_deck`** times out after 300 seconds on the client side, but generation often continues server-side. Poll with `list_artifacts` or `get_artifact` to check completion.
3. **Daily generation limit**: 15 per day on Google AI Pro plan. Budget accordingly.

---

## Cursor Rules

| Rule | Path | Purpose |
|---|---|---|
| NotebookLM Slide Workflow | `.cursor/rules/notebooklm-slide-workflow.mdc` | Enforces notebook architecture, source upload rules, generation process, and YAML template rules. Always applied. |
| Reporting Style | `.cursor/rules/reporting-style.mdc` | Professional consultant style, UK/Irish English. Always applied. |
| Critical Tasks | `.cursor/rules/critical.mdc` | Items marked [Critical] must be completed same day. Always applied. |

---

## Working Account

All production work should be conducted on the **personal** Google account. This account has a paid Google AI Pro subscription, which provides a higher daily slide generation limit (15 per day) compared to the free tier on the other accounts.

### Switching to the Personal Account

**Via the MCP tool (preferred):**
```
switch_account(profile="personal")
```

If the session has expired, the tool will return an authentication error. In that case, re-authenticate manually:

**Via terminal (bash on Windows):**
```bash
NOTEBOOKLM_HOME=~/.notebooklm-personal /c/Users/Fab2/Desktop/Work/venv/Scripts/notebooklm.exe login
```

This opens a browser window for Google sign-in. Complete the sign-in, then switch accounts via the MCP tool.

**Verification:** After switching, confirm the active account by calling `get_account_info()`. The response should show `personal` as the current profile.

---

## Immediate Next Steps

1. **Re-authenticate the personal account** using the instructions above. This is the first priority -- all subsequent work depends on it.
2. **Check whether the clean Section 1 generation completed** on the design account notebook (`cd8afd84`). If it did, download, convert to PNG, and review against the previous run. If not, re-run on the personal account.
3. **Update `tech_neon_art_eirmersive.yaml`** with the fixes that were applied only in the generation prompt:
   - Typography line: remove explicit font names, add "do not display font names on screen"
   - Add grid consistency rule
4. **Generate Section 0 and Section 2 decks** using the finalised template on the personal account.
5. **Commence final content review** -- the slide decks are a starting point, not the finished product. Content accuracy, speaker notes, and handout materials all need a pass.

---

## File Location Summary

| Category | Path |
|---|---|
| Workshop outline | `_Projects/FactoryXChange/FX2/Services/FundamentalsInnovationLiteracy/outline.md` |
| Section 0 content | `_Projects/.../FundamentalsInnovationLiteracy/0_Introduction/` |
| Section 1 content | `_Projects/.../FundamentalsInnovationLiteracy/1_ElementsOfInnovation/` |
| Section 2 content | `_Projects/.../FundamentalsInnovationLiteracy/2_FromLIteracyToPractice/` |
| Slide architecture | `Slides/SLIDE_ARCHITECTURE.md` |
| Element slide preps | `Slides/Elements/E00–E11` |
| Flow slide preps | `Slides/Flow/D1M_*, D1A_*, D2M_*, D2A_*` |
| Archived slide preps | `[section_folder]/Slides/_archive/` |
| FUJI Method docs | `_tools/_notebookLM/_slidedeckPrompts/fuji/` |
| YAML templates | `_tools/_notebookLM/_slidedeckPrompts/fuji/templates/` |
| Active template | `_tools/.../fuji/templates/techNeonArt/tech_neon_art_eirmersive.yaml` |
| Test outputs | `_tools/_notebookLM/_slidedeckPrompts/fuji/test_results/` |
| MCP server | `C:\Users\Fab2\Desktop\Work\notebooklm-py-MCP-full\` |
| MCP config | `C:\Users\Fab2\.cursor\mcp.json` |
| Cursor rules | `C:\Users\Fab2\Desktop\Work\.cursor\rules\` |
| This handover | `_Projects/.../FundamentalsInnovationLiteracy/HANDOVER.md` |
