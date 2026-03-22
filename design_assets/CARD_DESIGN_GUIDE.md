# Card Design System — FX2 Innovation Literacy

---
**Style:** Premium editorial, sophisticated typography, considered asymmetry  
**Language:** British English | **Tone:** Intelligent, accessible, quietly confident

---

## Colour Palette

| Role | Colour | Hex | Usage |
|------|--------|-----|-------|
| Base | Rich off-white | #FAF8F5 | Backgrounds, card stock |
| Text | Deep charcoal | #2C2C2C | Body text, headings |
| Accent | Terracotta | #C1666B | Editorial punctuation — underlines, highlights, badges |
| Secondary | Sage green | #8B9D83 | Metadata, navigation, supporting elements |

Four colours. The hero images provide all the visual variety needed — the system stays calm.

---

## Signature Detail Options

Seven candidates for a personal maker's mark. Test all, then select one or pair two (one structural + one atmospheric).

### 1. The Cropped Corner
One corner of every card has a 45° diagonal cut (8mm). Like a filed passport or a library index card. On digital, rendered as a chamfer while the other three stay rounded.
*Variable: shape · Object: corner*

### 2. The Oversized Ghost Number
The element number (1–11) rendered at 200pt, 4% opacity, bleeding off the bottom-right edge. Barely visible unless you look. A watermark that rewards attention.
*Variable: scale + opacity · Object: typography*

### 3. The Widened Inner Margin
One margin is always noticeably deeper than the other three (16mm left vs 8mm elsewhere). Like a scholarly book's gutter. Subtle but it creates consistent asymmetry that becomes the signature once you notice it.
*Variable: spacing · Object: margin*

### 4. The Cobalt Edge Line
A single 2px line in electric cobalt #2D5BFF along the left edge of every card. The one colour that doesn't belong in the warm palette — which is exactly why it reads as intentional.
*Variable: colour · Object: line*

### 5. The Interrupted Rule
Every horizontal divider has a deliberate 12mm gap at one-third from the left. A line that pauses. Once you notice it across multiple cards, it becomes unmistakable.
*Variable: continuity · Object: rule/divider*

### 6. Edition Numbering
Every card carries a sequential number — `34 / 71` — in monospace, rotated 90° along the right edge. Signals "this is a considered set, each one was counted."
*Variable: sequence · Object: numbering*

### 7. The Warm Drift
The off-white base subtly shifts 2–3% warmer toward one corner, like paper that aged near a window. You'd never consciously notice it on one card. Across twenty, it becomes atmosphere.
*Variable: tone · Object: background field*

---

## Typography

| Role | Spec | Font candidates |
|------|------|-----------------|
| Display | Serif, 42–48pt titles, 22–26pt section heads | Fraunces, Instrument Serif |
| Body | Humanist sans, 15–17pt, line-height 1.6 | Satoshi, Instrument Sans |
| Supporting | Body font, lighter weight, 12–13pt, tabular figures | — |
| Code/Refs | Monospace, 11pt | JetBrains Mono, IBM Plex Mono |

---

## Design Principles

1. **One accent, not eleven** — Colour variety comes from hero images, not the system
2. **Typography does the heavy lifting** — Serif/sans contrast creates hierarchy without colour-coding
3. **Earned simplicity** — If removing an element doesn't hurt, it shouldn't be there
4. **Asymmetric balance** — Deliberate off-centre composition. Considered tension, not chaos
5. **Art not illustration** — Hero images are evocative and abstract, not literal
6. **The card is the artefact** — Worth holding. Generous margins, clear hierarchy, tactile quality
7. **Works at every scale** — Same system renders as card, slide, infographic panel, or PDF page

---

## Card Anatomy

### Front Face
```
┌───────────────────────────────┐
│                               │
│  1 · PROCESS                  │  ← element + name, 12pt sage
│                               │
│   ┌────────────────────┐      │
│   │                    │      │
│   │    HERO IMAGE      │      │  ← generated from image_meta_description
│   │    (conceptual)    │      │     asymmetric, bleeds one edge
│   │                    │      │
│   └────────────────────┘      │
│                               │
│  Card Title                   │  ← serif, 36pt, charcoal
│  One-line essence             │  ← sans, 15pt, lighter weight
│                               │
│  reference · discovery · 3min │  ← 12pt sage, bottom metadata
│                               │
└───────────────────────────────┘
```

### Reverse Face
```
┌───────────────────────────────┐
│                               │
│  RELATED                      │
│  · thinking_divergent         │
│  · pattern_interrupts         │
│  · active_listening           │
│                               │
│  SOURCE                       │
│  design_thinking.md           │
│                               │
│                               │
│  FX2 · Innovation Literacy    │
│  factoryxchange.com           │
└───────────────────────────────┘
```

### Quick Reference Cards
- **Terracotta background** with white text (inverted)
- **Landscape orientation** for instant distinction
- **No hero image** — structured tabular content instead
- Same typography, just inverted colour

---

## Content Pattern → Visual Pattern

When generating infographic prompts from card content, the card file describes **what the information is**, not **how to visualise it**. Use these mappings to translate content structures into their most effective visual form.

### Pattern Recognition Rules

| Content Pattern | Visual Treatment | Example |
|----------------|-----------------|---------|
| **Table with 3–5 category rows** (each with a label + question/description) | Labelled boxes, tags, or pill shapes — one per category | "The Four Categories" → four teal-outlined rounded rectangles |
| **Table with overlapping/intersecting categories** | Venn diagram with labelled circles | Categories that can co-exist in the same item → overlapping circles |
| **2×2 matrix** (two axes, four quadrants) | Quadrant chart with axis labels and quadrant labels | "Risk = Uncertainty × Impact" → 2×2 with UNCERTAINTY/IMPACT axes |
| **Numbered step list** (sequential process) | Horizontal timeline with numbered circles and connectors | "1. Generate → 2. Cluster → ..." → circled numbers joined by arrows |
| **Formula or equation** | Display-italic typographic equation, prominent but not dominant | "Risk = Uncertainty × Impact" → set in italic serif above the matrix |
| **Bullet list of principles/rules** | Accent-coloured square bullets with body text | "Key Principles" → amber square bullets |
| **Key quote or opening statement** | Pulled quote — larger text, optional left-border accent rule | "Why It Matters" → 18pt body, thin amber left border |
| **Good vs bad comparison** | Two-column layout with ✓/✗ or contrasting tints | "Solution-embedded problem" → side-by-side columns |
| **Hierarchy or taxonomy** | Nested boxes or indented tree | Parent/child concept groupings |
| **Single metric or key number** | Large display numeral with supporting label | "5 steps" → oversized "5" with "steps" beneath |

### How to Apply

1. **Read the card body content** — identify which patterns are present
2. **Select the visual treatment** from the table above
3. **Describe the visual explicitly** in the prompt using concrete terms ("four teal-outlined rounded rectangles reading: Desirability, Feasibility, Viability, Adaptability") — never assume the image model will interpret a table as a diagram
4. **Spell out all display text** — every label, axis name, and quadrant label must be stated exactly. If it's not in the prompt, the model will guess or omit it
5. **One visual per concept** — don't combine two patterns into one diagram. A matrix is a matrix; categories are categories. Keep them as separate visual elements on the card

### Critical Rule: Separate Specification from Display

Design specifications (opacity values, pixel measurements, line weights) must **never** appear in the Content to Display section. They belong in the Visual Aesthetic section or as inline style notes clearly prefixed with "Style:" — otherwise the image model will render "10%" or "72px" as visible text on the card.

---

## Dimensions & Grid

- **Ratio:** 5:7 (70×100mm, or proportional digital)
- **Margins:** 8mm (unless using Signature #3, then 16mm left)
- **Grid:** 8pt spacing base
- **Corners:** 4mm radius (unless using Signature #1, then one 45° chamfer)

---

## Hero Image Generation — Nano Banana 2

Each card has an `image_meta_description` in its YAML metadata. These serve as the conceptual brief for image generation.

### Model-Specific Best Practices (Nano Banana 2 / Gemini 3.1 Flash Image)

**Prompt structure** — always lead with style, then subject:
```
Style: [art direction]. Subject: [image_meta_description]. 
Palette: [colour direction]. Texture: [surface quality].
```

**Key techniques from Google's official guidance:**

1. **Lead with style descriptor** — "Abstract geometric art" before describing the subject. The model responds better when style is established first
2. **Positive framing** — Describe what you want, not what to avoid. "Empty surface" works better than "no objects"
3. **Emphasise materiality (hero art only)** — For hero images, specify surfaces: "rough linen texture," "smooth matte paper." For infographic/card prompts, use flat vector language instead (see Visual Language Rules below)
4. **Control lighting explicitly** — "Soft diffused natural light" or "warm directional light from the left" produces consistent editorial results
5. **Anchor text to objects** — If any text appears in-image (generally avoid), attach it to a specific element: "a sign that reads X"
6. **Use reference images for consistency** — Generate 2–3 reference images first showing your art style, then use them as style references for all subsequent cards. This is how you maintain visual coherence across 71 cards
7. **Iterate conversationally** — Nano Banana 2 supports editing in context. Generate, then refine: "Make the background warmer" or "Shift the composition left"

### Visual Language Rules — Flat Vector Enforcement

The card system uses **flat 2D vector-style** infographics. Certain words push the model toward 3D, textured, or illustrative rendering. Avoid them.

| ✓ Safe (flat vector) | ✗ Avoid (triggers 3D/texture) |
|---------------------|-------------------------------|
| flat vector illustration | stylised |
| geometric shapes | artistic |
| diagrammatic | illustrated |
| clean, sharp edges | hand-drawn |
| solid colour fills | textured |
| outlined shapes | painted |
| schematic | realistic |
| minimal, precise | detailed, intricate |

**Rule:** Every visual concept description must include the phrase **"flat vector"** or **"flat 2D"** at least once. If the concept naturally suggests depth or texture (e.g., cork board, fabric), explicitly override it: "rendered as a flat vector illustration, not a photograph or textured surface."

### Card Hero Prompt Template

```
Style: Abstract geometric art, warm muted palette on off-white #FAF8F5, 
contemporary gallery aesthetic, evocative composition.
Inspired by Sol LeWitt wall drawings and Anni Albers textile geometry. 
Soft diffused natural light. No text, no labels, no people.

NOTE: This template is for standalone hero ART images only.
For infographic/card prompts, use the templates in templates/content/ 
and templates/title/ which enforce flat vector style.

Subject: [paste image_meta_description here]

Palette: Warm earth tones — terracotta #C1666B, sage #8B9D83, charcoal 
#2C2C2C, off-white #FAF8F5. Muted, not saturated.

Texture: Fine paper grain at 5-8% opacity. Matte finish, not glossy.

Aspect ratio: 4:3
```

### Building a Style Reference Library

Before generating all 71 hero images, create a **style anchor set** of 3–5 reference images:

1. Generate one image you love using the template above
2. Use it as a reference image for subsequent generations
3. Include "Maintain the exact visual style of the reference image" in your prompt
4. This ensures the geometric/gallery aesthetic stays consistent across the entire deck

Nano Banana 2 supports up to 5 consistent characters/elements per workflow — use this to keep a visual motif (e.g. a specific geometric pattern language) stable across cards.

### Aspect Ratios by Card Element

| Output | Ratio | Notes |
|--------|-------|-------|
| Card hero image | 4:3 | Landscape, bleeds one edge |
| Card front (full) | 5:7 | Portrait, for complete card renders |
| Slide | 16:9 | Presentation format |
| Infographic panel | 1:1 | Square, modular |

---

## Application Beyond Cards

This system scales directly to:
- **Slide decks** — same type hierarchy, one concept per slide
- **Infographics** — off-white base, charcoal text, terracotta highlights, sage for secondary
- **Workshop handouts** — card fronts printed as A5 reference sheets
- **Digital PDFs** — same grid, same palette, same restraint

---

## What Makes This Look Current (2026)

- **Serif/sans pairing** (Fraunces + Satoshi) is the dominant editorial trend — signals design literacy
- **Warm neutrals over cool greys** — editorial sophistication, not tech default
- **Generative art hero images** via Nano Banana 2 — shows AI fluency without making it the story
- **Restraint** — four colours with strong type says "confident" louder than a rainbow says "creative"
- **Grain texture** — the micro-trend bridging digital and print, signals craft
