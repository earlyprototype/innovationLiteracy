#!/usr/bin/env python3
"""
fill_reviews.py — Auto-fill <!-- REVIEW --> placeholders in generated prompts.

Reads source card markdown files, extracts content, and fills the REVIEW
flags in each generated prompt with concrete visual descriptions.

Usage:
    python fill_reviews.py
    python fill_reviews.py --dry-run          # preview without writing
    python fill_reviews.py --card failure_hallucination_content  # single file
"""

import json
import os
import re
import sys
import argparse
from pathlib import Path
from textwrap import shorten

# ── Paths ────────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).parent
ELEMENTS_DIR = BASE_DIR.parent / "Elements"
GENERATED_DIR = BASE_DIR / "generated"
PALETTE_MAP_PATH = BASE_DIR / "palette_map.json"


# ── YAML Parser (same as generate_prompts.py) ───────────────────────────────
def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Extract YAML frontmatter and body from markdown."""
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)", text, re.DOTALL)
    if not match:
        return {}, text

    yaml_block, body = match.group(1), match.group(2)
    meta = {}
    current_key = None
    current_list = None

    for line in yaml_block.split("\n"):
        line = line.rstrip("\r")
        if line.startswith("  - ") and current_key:
            if current_list is None:
                current_list = []
            current_list.append(line.strip("- ").strip())
            meta[current_key] = current_list
            continue

        kv = re.match(r"^(\w[\w_]*)\s*:\s*(.*)", line)
        if kv:
            if current_list is not None:
                current_list = None
            current_key = kv.group(1)
            value = kv.group(2).strip().strip('"').strip("'")
            if value:
                meta[current_key] = value
            else:
                meta[current_key] = None
                current_list = []
            continue

    return meta, body


def extract_title(body: str) -> str:
    match = re.search(r"^#\s+(.+)", body, re.MULTILINE)
    return match.group(1).strip() if match else "Untitled"


def extract_sections(body: str) -> dict:
    """Extract H2 sections from card body."""
    sections = {}
    current_section = None
    current_lines = []

    for line in body.split("\n"):
        h2 = re.match(r"^##\s+(.+)", line)
        if h2:
            if current_section:
                sections[current_section] = "\n".join(current_lines).strip()
            current_section = h2.group(1).strip()
            current_lines = []
        elif current_section:
            current_lines.append(line)

    if current_section:
        sections[current_section] = "\n".join(current_lines).strip()

    return sections


def extract_bullet_items(text: str, max_items: int = 5) -> list[str]:
    """Extract bullet point items from section text."""
    items = []
    for line in text.split("\n"):
        m = re.match(r"^[-*]\s+\*\*(.+?)\*\*[:—–]\s*(.*)", line)
        if m:
            items.append(f"{m.group(1)}: {m.group(2).strip()}")
        elif re.match(r"^[-*]\s+(.+)", line):
            item = re.match(r"^[-*]\s+(.+)", line).group(1).strip()
            # Strip bold markers
            item = re.sub(r"\*\*(.+?)\*\*", r"\1", item)
            items.append(item)
        if len(items) >= max_items:
            break
    return items


def extract_numbered_items(text: str, max_items: int = 5) -> list[str]:
    """Extract numbered list items from section text."""
    items = []
    for line in text.split("\n"):
        m = re.match(r"^\d+\.\s+\*\*(.+?)\*\*[:—–]?\s*(.*)", line)
        if m:
            items.append(f"{m.group(1)}: {m.group(2).strip()}" if m.group(2) else m.group(1))
        elif re.match(r"^\d+\.\s+(.+)", line):
            item = re.match(r"^\d+\.\s+(.+)", line).group(1).strip()
            item = re.sub(r"\*\*(.+?)\*\*", r"\1", item)
            items.append(item)
        if len(items) >= max_items:
            break
    return items


def extract_table_rows(text: str) -> list[list[str]]:
    """Extract table data rows (skip header separator)."""
    rows = []
    for line in text.split("\n"):
        if "|" in line and "---" not in line:
            cells = [c.strip() for c in line.strip("|").split("|")]
            if any(c for c in cells):
                rows.append(cells)
    return rows


def get_first_sentence(text: str) -> str:
    """Get the first meaningful sentence from text."""
    # Strip markdown formatting
    clean = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    clean = re.sub(r"\*(.+?)\*", r"\1", clean)
    # Skip blank lines, headers, and list items
    for line in clean.split("\n"):
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("-") or line.startswith("|"):
            continue
        # Get first sentence
        m = re.match(r"^(.+?[.!?])\s", line)
        if m:
            return m.group(1)
        if len(line) < 120:
            return line
    return ""


# ── Accent Usage (standard per palette) ──────────────────────────────────────
ACCENT_USAGE = {
    "a_terracotta_sage": {
        "primary": "title underline, emphasis highlights, key statement left-border rules, and square bullet accents",
        "secondary": "metadata labels, element name, structural diagram outlines, and timeline connectors",
    },
    "b_coral_teal": {
        "primary": "title underline, emphasis highlights, key statement left-border rules, and category tag fills",
        "secondary": "metadata labels, element name, diagram outlines, timeline connectors, and process step circles",
    },
    "c_orange_violet": {
        "primary": "title underline, emphasis highlights, key statement left-border rules, and square bullet accents",
        "secondary": "metadata labels, element name, structural diagram outlines, checklist markers, and box borders",
    },
    "d_amber_teal": {
        "primary": "title underline, emphasis highlights, key statement borders, timeline connectors, and template card accents",
        "secondary": "metadata labels, element name, diagram outlines, process step circles, and formula box borders",
    },
}


# ── Pattern → Visual Treatment ───────────────────────────────────────────────
def describe_principle_list(section_name: str, content: str, palette: str) -> str:
    """Generate visual treatment for a principle/bullet list."""
    items = extract_bullet_items(content, max_items=4)
    if not items:
        items = extract_numbered_items(content, max_items=4)
    if not items:
        first = get_first_sentence(content)
        if first:
            return f'A pulled quote in 18pt body text: "{shorten(first, 100)}" with a thin primary accent left-border rule (2px).'
        return f'Key points from "{section_name}" rendered as accent-coloured square bullets (4pt) with body text.'

    items_text = "; ".join(f'"{shorten(i, 60)}"' for i in items[:4])
    return f'Accent-coloured square bullets (4pt) with body text. Items reading: {items_text}.'


def describe_numbered_process(section_name: str, content: str, palette: str) -> str:
    """Generate visual treatment for a numbered process/timeline."""
    items = extract_numbered_items(content, max_items=5)
    if not items:
        return f'Horizontal timeline with numbered circles connected by a single hairline rule in primary accent. Steps from "{section_name}".'

    steps_text = " → ".join(f"{i+1}. {shorten(item, 40)}" for i, item in enumerate(items[:5]))
    return f"Horizontal timeline with numbered circles (secondary accent stroke, no fill) connected by a hairline rule in primary accent. Steps: {steps_text}. Step labels positioned below in sentence case."


def describe_category_table(section_name: str, content: str, palette: str) -> str:
    """Generate visual treatment for a category table."""
    rows = extract_table_rows(content)
    if len(rows) <= 1:
        return f'Labelled category boxes with content from "{section_name}", each outlined in secondary accent with primary accent headers.'

    # Use header row for column names, data rows for content
    headers = rows[0]
    data_rows = rows[1:]
    row_labels = [r[0] for r in data_rows[:4] if r]
    labels_text = ", ".join(f'"{l}"' for l in row_labels)

    return f'A structured table with columns: {", ".join(headers)}. Row labels: {labels_text}. Headers in primary accent, cell borders in secondary accent at 20% opacity, alternating row tints for readability.'


def describe_comparison_table(section_name: str, content: str, palette: str) -> str:
    """Generate visual treatment for a comparison/two-column table."""
    rows = extract_table_rows(content)
    if len(rows) <= 1:
        return f'Two-column comparison layout from "{section_name}" with contrasting tints.'

    headers = rows[0]
    return f'Two-column comparison layout. Columns: {" vs ".join(f"{h}" for h in headers[:2])}. Clean table with primary accent headers and secondary accent divider lines.'


def describe_matrix(section_name: str, content: str, palette: str) -> str:
    """Generate visual treatment for a 2×2 matrix."""
    return f'A 2×2 quadrant chart from "{section_name}". Axes labelled in secondary accent, quadrant labels in body text. Grid lines in neutral at 15% opacity, primary accent for the key quadrant highlight.'


def describe_formula(section_name: str, content: str, palette: str) -> str:
    """Generate visual treatment for a formula/equation."""
    # Try to extract the formula
    m = re.search(r"\*\*(.+?=.+?)\*\*", content)
    if m:
        return f'Display-italic typographic equation: "{m.group(1)}". Set larger than body text, primary accent colour, centred with generous whitespace.'
    return f'Display-italic typographic equation from "{section_name}". Prominent but not dominant, in primary accent colour.'


PATTERN_HANDLERS = {
    "principle_list": describe_principle_list,
    "numbered_process": describe_numbered_process,
    "category_table": describe_category_table,
    "comparison_table": describe_comparison_table,
    "2x2_matrix": describe_matrix,
    "formula": describe_formula,
}


def describe_generic_section(section_name: str, content: str) -> str:
    """Fallback: generate a description for a section without a detected pattern."""
    items = extract_bullet_items(content, max_items=3)
    if items:
        items_text = "; ".join(f'"{shorten(i, 50)}"' for i in items[:3])
        return f'Key points from "{section_name}" rendered as accent-coloured square bullets: {items_text}.'

    numbered = extract_numbered_items(content, max_items=3)
    if numbered:
        steps_text = " → ".join(f"{i+1}. {shorten(item, 40)}" for i, item in enumerate(numbered[:4]))
        return f'Steps from "{section_name}" as a horizontal timeline: {steps_text}.'

    first = get_first_sentence(content)
    if first:
        return f'A pulled quote in 18pt body text: "{shorten(first, 100)}" with a thin primary accent left-border rule (2px).'

    return f'Key content from "{section_name}" rendered as body text with clear typographic hierarchy.'


# ── Subtitle Generation ──────────────────────────────────────────────────────
def generate_subtitle(meta: dict, body: str, sections: dict) -> str:
    """Generate a concise subtitle for the card."""
    title = extract_title(body)

    # Priority 1: If there's a bold question near the top, use it
    m = re.search(r"\*\*(?:Question|Key Question)[:\s]*\*\*\s*(.+?)(?:\n|$)", body)
    if m:
        return shorten(m.group(1).strip(), 100)

    # Priority 2: "Why It Matters" section first sentence
    if "Why It Matters" in sections:
        s = get_first_sentence(sections["Why It Matters"])
        if s:
            return shorten(s, 100)

    # Priority 3: "What Happens" section first sentence
    if "What Happens" in sections:
        s = get_first_sentence(sections["What Happens"])
        if s:
            return shorten(s, 100)

    # Priority 4: First short paragraph after H1
    for line in body.split("\n"):
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("-") or line.startswith("|") or line.startswith("_"):
            continue
        if line.startswith("**") and ":**" in line:
            # It's a bold heading/label — skip
            continue
        clean = re.sub(r"\*\*(.+?)\*\*", r"\1", line)
        if 20 < len(clean) < 110:
            return clean

    # Priority 5: Synthesize from title
    return f"Understanding {title.lower()}"


# ── Visual Concept Generation ────────────────────────────────────────────────
def generate_title_visual_concept(meta: dict, body: str) -> str:
    """Generate visual concept for title card from image_meta_description."""
    image_meta = meta.get("image_meta_description", "")
    if image_meta:
        return (
            f"A flat vector illustration of: {image_meta} "
            f"Rendered as clean geometric shapes with solid colour fills on the background. "
            f"Abstract and evocative — not literal. No text rendered in the illustration."
        )
    # Fallback: derive from title
    title = extract_title(body)
    return (
        f"A flat vector abstract geometric illustration evoking the concept of "
        f'"{title.lower()}". Clean shapes, solid fills, asymmetric composition. '
        f"No text, no labels, no people."
    )


def generate_content_visual_concept(meta: dict, body: str, sections: dict) -> str:
    """Generate visual concept for content card."""
    title = extract_title(body)
    card_type = meta.get("type", "reference")
    element_name = meta.get("element_name", "")

    section_names = list(sections.keys())[:3]
    sections_desc = ", ".join(f'"{s}"' for s in section_names) if section_names else "key concepts"

    type_flavour = {
        "reference": "reference-style",
        "diagnostic": "diagnostic analysis",
        "structured-method": "structured methodology",
        "concept": "conceptual exploration",
        "overview": "comprehensive overview",
        "checklist": "practical checklist",
        "taxonomy": "classification framework",
        "quick-ref": "quick reference",
    }
    flavour = type_flavour.get(card_type, "informational")

    return (
        f"A premium editorial {flavour} infographic presenting {sections_desc} "
        f"for {title}. Clean flat vector layout with considered asymmetry, "
        f"generous whitespace, and clear typographic hierarchy across three horizontal zones."
    )


# ── Source Card Finder ───────────────────────────────────────────────────────
def build_card_index(elements_dir: Path) -> dict:
    """Build index: card_stem → card_path for all source cards."""
    index = {}
    for element_dir in sorted(elements_dir.iterdir()):
        cards_dir = element_dir / "resources" / "cards"
        if cards_dir.exists():
            for card_file in cards_dir.glob("*.md"):
                if not card_file.name.startswith("_"):
                    index[card_file.stem] = card_file
    return index


# ── Main Fill Logic ──────────────────────────────────────────────────────────
def fill_prompt_file(prompt_path: Path, card_index: dict, palette_map: dict, dry_run: bool = False) -> dict:
    """Fill REVIEW flags in a single generated prompt file.
    
    Returns dict with stats: {reviews_filled, reviews_total, card_found}.
    """
    prompt_text = prompt_path.read_text(encoding="utf-8")
    original_text = prompt_text
    
    total_reviews = prompt_text.count("<!-- REVIEW")
    if total_reviews == 0:
        return {"reviews_filled": 0, "reviews_total": 0, "card_found": True}

    # Determine card stem and type (title vs content)
    stem = prompt_path.stem
    is_title = stem.endswith("_title")
    is_content = stem.endswith("_content")
    card_stem = re.sub(r"_(title|content)$", "", stem)

    # Find source card
    if card_stem not in card_index:
        print(f"  ⚠ Source card not found for {stem}")
        return {"reviews_filled": 0, "reviews_total": total_reviews, "card_found": False}

    card_path = card_index[card_stem]
    card_text = card_path.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(card_text)
    sections = extract_sections(body)

    # Determine palette
    element = str(meta.get("element", "0"))
    palette_key = palette_map["element_palettes"].get(element, "a_terracotta_sage")
    accent = ACCENT_USAGE.get(palette_key, ACCENT_USAGE["a_terracotta_sage"])

    filled_count = 0

    # ── Fill subtitle ────────────────────────────────────────────────────
    if "<!-- REVIEW: write subtitle -->" in prompt_text:
        subtitle = generate_subtitle(meta, body, sections)
        prompt_text = prompt_text.replace("<!-- REVIEW: write subtitle -->", subtitle)
        filled_count += 1

    # ── Fill visual concept (title card) ─────────────────────────────────
    if "<!-- REVIEW: write visual concept -->" in prompt_text:
        concept = generate_title_visual_concept(meta, body)
        prompt_text = prompt_text.replace(
            "<!-- REVIEW: write visual concept -->\n<!-- image_meta_description:",
            f"{concept}\n<!-- image_meta_description:",
        )
        # Fallback if the image_meta line isn't there
        if "<!-- REVIEW: write visual concept -->" in prompt_text:
            prompt_text = prompt_text.replace("<!-- REVIEW: write visual concept -->", concept)
        filled_count += 1

    # ── Fill visual concept (content card) ───────────────────────────────
    if "<!-- REVIEW: write visual concept for content card -->" in prompt_text:
        concept = generate_content_visual_concept(meta, body, sections)
        prompt_text = prompt_text.replace("<!-- REVIEW: write visual concept for content card -->", concept)
        filled_count += 1

    # ── Fill accent usage ────────────────────────────────────────────────
    if "<!-- REVIEW: describe primary accent usage -->" in prompt_text:
        prompt_text = prompt_text.replace("<!-- REVIEW: describe primary accent usage -->", accent["primary"])
        filled_count += 1

    if "<!-- REVIEW: describe secondary accent usage -->" in prompt_text:
        prompt_text = prompt_text.replace("<!-- REVIEW: describe secondary accent usage -->", accent["secondary"])
        filled_count += 1

    # ── Fill extra elements ──────────────────────────────────────────────
    if "<!-- REVIEW: add extra elements if needed -->" in prompt_text:
        prompt_text = prompt_text.replace("<!-- REVIEW: add extra elements if needed -->", "None — the two-accent palette provides sufficient visual variety")
        filled_count += 1

    # ── Fill content zones with pattern-detected content ─────────────────
    # Handle pattern-detected sections: <!-- REVIEW: 'SectionName' detected as pattern_type ... -->
    pattern_matches = re.findall(
        r"<!-- REVIEW: '(.+?)' detected as (\w+) — describe visual treatment -->",
        prompt_text,
    )
    for section_name, pattern_type in pattern_matches:
        section_content = sections.get(section_name, "")
        handler = PATTERN_HANDLERS.get(pattern_type, None)
        if handler and section_content:
            description = handler(section_name, section_content, palette_key)
        elif section_content:
            description = describe_generic_section(section_name, section_content)
        else:
            description = f'Content from "{section_name}" section with clear typographic hierarchy.'

        old = f"<!-- REVIEW: '{section_name}' detected as {pattern_type} — describe visual treatment -->"
        prompt_text = prompt_text.replace(old, description)
        filled_count += 1

    # ── Fill generic content zones (left/right/footer without pattern) ───
    section_list = list(sections.items())

    if "<!-- REVIEW: describe left column content -->" in prompt_text:
        if len(section_list) >= 1:
            name, content = section_list[0]
            desc = describe_generic_section(name, content)
        else:
            desc = "Key concepts presented as body text with accent highlights."
        prompt_text = prompt_text.replace("<!-- REVIEW: describe left column content -->", desc)
        filled_count += 1

    if "<!-- REVIEW: describe right column content -->" in prompt_text:
        if len(section_list) >= 2:
            name, content = section_list[1]
            desc = describe_generic_section(name, content)
        else:
            desc = "Supporting detail or framework in secondary accent structural elements."
        prompt_text = prompt_text.replace("<!-- REVIEW: describe right column content -->", desc)
        filled_count += 1

    if "<!-- REVIEW: describe footer content -->" in prompt_text:
        if len(section_list) >= 3:
            name, content = section_list[2]
            desc = describe_generic_section(name, content)
        elif len(section_list) >= 2:
            # Use last section
            name, content = section_list[-1]
            desc = describe_generic_section(name, content)
        else:
            desc = "Key takeaway or application note anchoring the bottom of the card."
        prompt_text = prompt_text.replace("<!-- REVIEW: describe footer content -->", desc)
        filled_count += 1

    # ── Write back ───────────────────────────────────────────────────────
    if prompt_text != original_text and not dry_run:
        prompt_path.write_text(prompt_text, encoding="utf-8")

    remaining = prompt_text.count("<!-- REVIEW")
    return {
        "reviews_filled": filled_count,
        "reviews_total": total_reviews,
        "reviews_remaining": remaining,
        "card_found": True,
    }


def main():
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="Fill REVIEW placeholders in generated prompts")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing files")
    parser.add_argument("--card", type=str, help="Process a single prompt by filename (without .md)")
    args = parser.parse_args()

    # Load palette map
    if not PALETTE_MAP_PATH.exists():
        print(f"✗ palette_map.json not found at {PALETTE_MAP_PATH}")
        sys.exit(1)
    palette_map = json.loads(PALETTE_MAP_PATH.read_text(encoding="utf-8"))

    # Build card index
    card_index = build_card_index(ELEMENTS_DIR)
    print(f"  Indexed {len(card_index)} source cards")

    # Find prompt files
    prompt_files = sorted(GENERATED_DIR.glob("*.md"))
    if args.card:
        prompt_files = [f for f in prompt_files if f.stem == args.card]

    print(f"\n{'═' * 60}")
    print(f"  FX2 REVIEW Flag Filler")
    print(f"  Prompt files: {len(prompt_files)}")
    print(f"  Mode: {'DRY RUN' if args.dry_run else 'FILLING'}")
    print(f"{'═' * 60}\n")

    total_filled = 0
    total_flags = 0
    total_remaining = 0
    missing_cards = []

    for prompt_file in prompt_files:
        result = fill_prompt_file(prompt_file, card_index, palette_map, args.dry_run)

        if not result["card_found"]:
            missing_cards.append(prompt_file.stem)
            continue

        filled = result["reviews_filled"]
        total = result["reviews_total"]
        remaining = result.get("reviews_remaining", 0)

        total_filled += filled
        total_flags += total
        total_remaining += remaining

        if total > 0:
            status = "✓" if remaining == 0 else f"⚠ {remaining} remaining"
            print(f"  {status}  {prompt_file.stem}  ({filled}/{total} filled)")

    print(f"\n{'═' * 60}")
    print(f"  Done!")
    print(f"  Flags filled: {total_filled} / {total_flags}")
    print(f"  Remaining unfilled: {total_remaining}")
    if missing_cards:
        print(f"  Missing source cards: {len(missing_cards)}")
        for m in missing_cards[:5]:
            print(f"    - {m}")
    print(f"{'═' * 60}\n")


if __name__ == "__main__":
    main()
