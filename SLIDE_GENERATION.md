# Slide Generation — NotebookLM and FUJI Method

## Slide Generation System (FUJI Method)

Root: `_tools/_notebookLM/_slidedeckPrompts/fuji/`

### Key Files
- `FUJI_METHOD_CONTEXT.md` — Full methodology documentation, workflow, and test log. Read this first.
- `fujiMasterSpec.yaml` — Template structure reference for creating new YAML specifications.
- `README.md` — Original setup notes.

### Templates
Location: `fuji/templates/`

Each template has a folder containing the YAML spec (Japanese `_jp.yaml` versions are the primary prompts):

| Template | Provenance | Notes |
|---|---|---|
| `techNeonArt/tech_neon_art.yaml` | Author original | The baseline. 52 lines. Produces the strongest results. |
| `techNeonArt/tech_neon_art_eirmersive.yaml` | Custom (ours) | Modified TechNeonArt for Eirmersive. 62 lines. Per-section accent colours, text limits, punctuation/language rules, photo guidance. **Active template.** |
| `mckinseyConsulting/mckinseyConsulting_jp.yaml` | Rewritten lean | McKinsey consulting style. |
| `mckinseyConsulting/mckinseyConsulting_mintext_jp.yaml` | Custom (ours) | McKinsey variant with aggressive text limits. |
| `bravestNewWorld/bravestNewWorld_jp.yaml` | Custom (ours) | Eastern European urban resilience aesthetic. Deprioritised. |
| `japonismTextileFlow/japonismTextileFlow_jp.yaml` | Author original | Beautiful but too bold/nationally specific for this application. |
| `cosmicObservatory/cosmicObservatory_jp.yaml` | Custom (ours) | Deep space aesthetic. Never fully tested. |
| Other templates (11 total) | Author originals | Available but not tested with this project content. |

### Test Results
Location: `fuji/test_results/`

| File | Template | Content | Notes |
|---|---|---|---|
| `McKinsey_MinText_Section0.pdf` | McKinsey minimal-text | Section 0 | Clean but one-dimensional |
| `Eirmersive_Section1.pdf` | Eirmersive (v1) | Section 1 | 15 slides, strong but has known issues (see below) |
| `Eirmersive_Section1_pages/` | — | — | PNG conversions of above |
| `Japonism_Section0.pdf` | Japonism Textile Flow | Section 0 | Stunning but inappropriate for client context |
| `TechNeonArt_Section0.pdf` | TechNeonArt (original) | Section 0 | Strong baseline reference |
| `BravestNewWorld_Section0.pdf` (in templates folder) | Bravest New World | Section 0 | Deprioritised |
| `Deck2_Section0.pdf` | Unknown (earlier test) | Section 0 | Earlier test run |

### Eirmersive Template: Design Decisions

The `tech_neon_art_eirmersive.yaml` template is a modification of the author's TechNeonArt original. Key design choices:

- **Per-section accent colours**: Neon Yellow (#DFFF00) for Section 0, Electric Cyan (#00E5FF) for Section 1, Signal Coral (#FF6B6B) for Section 2. Provides subtle visual distinction between workshop sections.
- **Text limit**: Maximum 20 words per slide body. Keywords and short phrases, not sentences.
- **No terminal punctuation** on headings, labels, or captions. Body text only.
- **UK/Irish English** only (organisation, recognise, colour).
- **Photo guidance**: Individual portraits preferred over group shots. Technical/mechanical imagery prioritised. Monochrome treatment with geometric overlay.
- **Typography**: Serif/sans-serif mixing for contrast. Thin font weights for body text. (Note: the saved YAML still names "Helvetica" and "Didot, Bodoni" explicitly — the most recent generation prompt was modified to say "do not display font names on screen" but the YAML file itself was not updated.)

### Known Issues with Current Template

From the slide-by-slide review of the first Section 1 generation:

| Issue | Detail | Template Fix Applied |
|---|---|---|
| "Helvetica" font name appearing as visible text | The typography instruction named font families, and the LLM printed them on-screen | Yes — generation prompt updated. Saved YAML file still contains "Helvetica" and needs updating. |
| Full stops on labels and captions | Body captions consistently end with periods despite the no-punctuation rule | Partially — rule exists but LLM ignores it on body-text captions. May need stronger phrasing or acceptance as a limitation. |
| Grid density inconsistency | Grid backgrounds vary from sparse to very dense across slides | Yes — grid consistency rule added to generation prompt. Saved YAML file does not yet include this rule. |
| Content truncation (5-7 items reduced to 3-4) | Lists of concepts are trimmed to fit visual layouts | Systemic LLM behaviour, not template-addressable. Accept and compensate in speaker notes or handouts. |
| Engine-invented slides | 3 slides (2, 14, 15) were not in the source material | Neutral. Good editorial additions but means output count differs from input. |
| Erratic font type switching mid-title | Font weight and style changes within individual words or titles | Not yet addressed. Likely related to the serif/sans-serif mixing instruction. |

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

### Switching to the Personal Account

**Via the MCP tool (preferred):**
```
switch_account(profile="personal")
```

If the session has expired, re-authenticate manually:

**Via terminal (bash on Windows):**
```bash
NOTEBOOKLM_HOME=~/.notebooklm-personal /c/Users/Fab2/Desktop/Work/venv/Scripts/notebooklm.exe login
```

Complete the browser sign-in, then switch accounts via the MCP tool.

**Verification:** After switching, confirm the active account by calling `get_account_info()`. The response should show `personal` as the current profile.

### Active Notebooks

| Notebook | Account | ID | Purpose | Status |
|---|---|---|---|---|
| FIL Slides - Section 1: Elements of Innovation (Clean) | design | `cd8afd84-1709-49d9-aeeb-1c0c417cbfa9` | Clean Section 1 test with Eirmersive template | Generation triggered, completion unknown |
| FIL Slides - Section 1: Elements of Innovation (Eirmersive Test) | personal | `6cad0cee-0f15-42ab-9305-c9dcaa6f86ba` | First Section 1 test (may contain Section 0 residue) | Complete — produced `Eirmersive_Section1.pdf` |

Earlier test notebooks exist across accounts but are not critical to the current workflow.

### Known Tool Limitations

1. **`download_slide_deck`** tends to return the most recently completed artifact regardless of which one is requested. If multiple decks exist in a notebook, manual download from the NotebookLM web UI may be necessary.
2. **`generate_slide_deck`** times out after 300 seconds on the client side, but generation often continues server-side. Poll with `list_artifacts` or `get_artifact` to check completion.
3. **Daily generation limit**: 15 per day on Google AI Pro plan. Budget accordingly.

---

## Slide Architecture

Full specification: `Slides/SLIDE_ARCHITECTURE.md`

Two-deck structure: Element Learning slides (`Slides/Elements/E00–E11`) and Workshop Flow slides (`Slides/Flow/D1M_*, D1A_*, D2M_*, D2A_*`).

---

## Generation Workflow

1. Create/update slide prep files in `Slides/Elements/` or `Slides/Flow/`
2. Select or create the appropriate NotebookLM notebook
3. Upload all required sources (content files + slide preps)
4. Select YAML template from `_tools/_notebookLM/_slidedeckPrompts/fuji/templates/`
5. Pass YAML content as `instructions` parameter to `generate_slide_deck`
6. Download, convert to PNG, review
7. Iterate template or slide prep content as needed

---

## Next Steps

1. **Re-authenticate the personal account** — all subsequent work depends on it.
2. **Update `tech_neon_art_eirmersive.yaml`** with fixes applied only in generation prompts:
   - Typography line: remove explicit font names, add "do not display font names on screen"
   - Add grid consistency rule
3. **Create new NotebookLM notebooks** matching the two-deck architecture (see SLIDE_ARCHITECTURE.md)
4. **Generate Element Learning deck** (E00–E11) using the finalised template
5. **Generate Workshop Flow decks** per session (D1M, D1A)

---

_Last updated: 2026-03-19_
