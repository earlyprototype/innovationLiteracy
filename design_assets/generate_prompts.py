#!/usr/bin/env python3
"""
generate_prompts.py — Automated prompt generation for FX2 Innovation Literacy cards.

Scans all card markdown files, parses YAML frontmatter, maps metadata to
palette/template, and generates draft prompts ready for LLM review.

Usage:
    python generate_prompts.py
    python generate_prompts.py --dry-run          # preview without writing
    python generate_prompts.py --card assumption_mapping  # single card
"""

import json
import os
import re
import sys
import argparse
from pathlib import Path

# ── Paths ────────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).parent
ELEMENTS_DIR = BASE_DIR.parent / "Elements"
TEMPLATES_DIR = BASE_DIR / "templates"
PALETTE_MAP_PATH = BASE_DIR / "palette_map.json"
OUTPUT_DIR = BASE_DIR / "generated"


# ── YAML Parser (no dependency) ─────────────────────────────────────────────
def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Extract YAML frontmatter and body from markdown. Returns (metadata, body)."""
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)", text, re.DOTALL)
    if not match:
        return {}, text

    yaml_block, body = match.group(1), match.group(2)
    meta = {}
    current_key = None
    current_list = None

    for line in yaml_block.split("\n"):
        line = line.rstrip("\r")

        # List item under current key
        if line.startswith("  - ") and current_key:
            if current_list is None:
                current_list = []
            current_list.append(line.strip("- ").strip())
            meta[current_key] = current_list
            continue

        # Key: value pair
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
    """Pull H1 title from markdown body."""
    match = re.search(r"^#\s+(.+)", body, re.MULTILINE)
    return match.group(1).strip() if match else "Untitled"


def extract_subtitle(body: str) -> str | None:
    """Attempt to extract a subtitle — first paragraph after H1, if short."""
    match = re.search(r"^#\s+.+\n+(?:##\s+\w.*\n+)?(.+)", body, re.MULTILINE)
    if match:
        candidate = match.group(1).strip()
        # Only use if it's short enough to be a subtitle (not a full paragraph)
        if len(candidate) < 120 and not candidate.startswith("|") and not candidate.startswith("-"):
            return candidate
    return None


def has_parent_card(meta: dict) -> bool:
    """Determine if this card is a subdivision of another card.
    
    Heuristic: if the card's filename suggests it's a sub-stage (dt_define, dt_ideate)
    or if it has related_cards that include an 'overview' card in the same card_set,
    it's a subdivision and shouldn't get a title card.
    """
    source = meta.get("source_doc", "")
    card_set = meta.get("card_set", "")
    related = meta.get("related_cards", [])
    
    # Cards that reference an overview card are subdivisions
    if isinstance(related, list):
        for r in related:
            if "overview" in str(r).lower():
                return True
    
    # Cards in stage-specific sets (like design_thinking_stages) are subdivisions
    if "stages" in card_set.lower():
        return True
    
    return False


def format_type_label(card_type: str) -> str:
    """Format the card type for display label."""
    type_labels = {
        "reference": "REFERENCE CARD",
        "structured-method": "METHODOLOGY CARD",
        "concept": "CONCEPT CARD",
        "overview": "OVERVIEW CARD",
        "quick-ref": "QUICK REFERENCE",
        "checklist": "CHECKLIST",
        "taxonomy": "TAXONOMY CARD",
    }
    return type_labels.get(card_type, card_type.upper().replace("-", " ") + " CARD")


def extract_content_sections(body: str) -> dict:
    """Extract H2 sections from the card body for content card population."""
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


def detect_content_patterns(sections: dict) -> dict:
    """Detect visual patterns from card content for the LLM to use."""
    patterns = {}
    for name, content in sections.items():
        # Table detection
        if "|" in content and "---" in content:
            # Count columns
            header_match = re.search(r"\|(.+)\|", content)
            if header_match:
                cols = len(header_match.group(1).split("|"))
                if cols == 3 and ("Low" in content and "High" in content):
                    patterns[name] = "2x2_matrix"
                elif cols >= 3:
                    patterns[name] = "category_table"
                else:
                    patterns[name] = "comparison_table"
        # Numbered list (process steps)
        elif re.search(r"^\d+\.\s+\*\*", content, re.MULTILINE):
            patterns[name] = "numbered_process"
        # Bullet list
        elif re.search(r"^-\s+\*\*", content, re.MULTILINE):
            patterns[name] = "principle_list"
        # Formula/equation
        elif "=" in content and re.search(r"\*\*\w+\s*=\s*\w+", content):
            patterns[name] = "formula"

    return patterns


def fill_title_template(template: str, card_data: dict) -> str:
    """Fill a title template with card data, leaving REVIEW flags."""
    replacements = {
        "{{TITLE}}": card_data["title"],
        "{{SUBTITLE}}": card_data.get("subtitle") or "<!-- REVIEW: write subtitle -->",
        "{{CARD_TYPE_LABEL_1}}": card_data["type_label"],
        "{{CARD_TYPE_LABEL_2}}": card_data["element_name"].upper(),
        "{{GHOST_NUMBER}}": str(card_data["element"]),
        "{{VISUAL_CONCEPT — A flat vector illustration of...}}": (
            f"<!-- REVIEW: write visual concept -->\n"
            f"<!-- image_meta_description: {card_data.get('image_meta', 'none')} -->"
        ),
        "{{PRIMARY_ACCENT_USAGE}}": "<!-- REVIEW: describe primary accent usage -->",
        "{{SECONDARY_ACCENT_USAGE}}": "<!-- REVIEW: describe secondary accent usage -->",
        "{{EXTRA_ELEMENTS — any metaphor-specific colours or details}}": "<!-- REVIEW: add extra elements if needed -->",
    }

    result = template
    for placeholder, value in replacements.items():
        result = result.replace(placeholder, value)

    return result


def fill_content_template(template: str, card_data: dict) -> str:
    """Fill a content template with card data, leaving REVIEW flags."""
    replacements = {
        "{{TITLE}}": card_data["title"],
        "{{SUBTITLE}}": card_data.get("subtitle") or "<!-- REVIEW: write subtitle -->",
        "{{CARD_TYPE_LABEL_1}}": card_data["type_label"],
        "{{CARD_TYPE_LABEL_2}}": card_data["element_name"].upper(),
        "{{GHOST_NUMBER}}": str(card_data["element"]),
        "{{VISUAL_CONCEPT — A one-sentence description of the overall composition and editorial feel of this card.}}": (
            f"<!-- REVIEW: write visual concept for content card -->"
        ),
        "{{PRIMARY_ACCENT_USAGE}}": "<!-- REVIEW: describe primary accent usage -->",
        "{{SECONDARY_ACCENT_USAGE}}": "<!-- REVIEW: describe secondary accent usage -->",
    }

    # Content zone — inject detected patterns as guidance
    patterns = card_data.get("patterns", {})
    sections = card_data.get("sections", {})

    left_content = "<!-- REVIEW: describe left column content -->"
    right_content = "<!-- REVIEW: describe right column content -->"
    footer_content = "<!-- REVIEW: describe footer content -->"

    # Auto-map patterns to zones
    pattern_items = list(patterns.items())
    if len(pattern_items) >= 1:
        name, ptype = pattern_items[0]
        left_content = f"<!-- REVIEW: '{name}' detected as {ptype} — describe visual treatment -->"
    if len(pattern_items) >= 2:
        name, ptype = pattern_items[1]
        right_content = f"<!-- REVIEW: '{name}' detected as {ptype} — describe visual treatment -->"
    if len(pattern_items) >= 3:
        name, ptype = pattern_items[2]
        footer_content = f"<!-- REVIEW: '{name}' detected as {ptype} — describe visual treatment -->"

    # Replace content zone placeholders using regex since they're multi-line
    result = template
    for placeholder, value in replacements.items():
        result = result.replace(placeholder, value)

    # Replace the multi-line content placeholders
    result = re.sub(
        r"\{\{LEFT_COLUMN_CONTENT.*?\}\}",
        left_content,
        result,
        flags=re.DOTALL,
    )
    result = re.sub(
        r"\{\{RIGHT_COLUMN_CONTENT.*?\}\}",
        right_content,
        result,
        flags=re.DOTALL,
    )
    result = re.sub(
        r"\{\{FOOTER_CONTENT.*?\}\}",
        footer_content,
        result,
        flags=re.DOTALL,
    )

    return result


def process_card(card_path: Path, palette_map: dict, dry_run: bool = False) -> list[str]:
    """Process a single card file and generate prompt(s). Returns list of output paths."""
    text = card_path.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)

    if not meta.get("element"):
        return []

    # Skip index and admin files
    if card_path.name.startswith("_") or "TODO" in card_path.name or "QUICK_REF" in card_path.name:
        return []

    element = str(meta["element"])
    element_name = meta.get("element_name", f"Element {element}")
    card_type = meta.get("type", "reference")
    image_meta = meta.get("image_meta_description", "")
    title = extract_title(body)
    subtitle = extract_subtitle(body)

    # Look up palette
    palette_key = palette_map["element_palettes"].get(element)
    if not palette_key:
        print(f"  ⚠ No palette mapping for element {element}, skipping {card_path.name}")
        return []

    # Card data dict
    card_data = {
        "element": element,
        "element_name": element_name,
        "title": title,
        "subtitle": subtitle,
        "type": card_type,
        "type_label": format_type_label(card_type),
        "image_meta": image_meta,
        "sections": extract_content_sections(body),
        "patterns": detect_content_patterns(extract_content_sections(body)),
    }

    outputs = []
    card_stem = card_path.stem

    # ── Determine what to generate ───────────────────────────────────────
    is_subdivision = has_parent_card(meta)

    # Title card (only for non-subdivisions)
    if not is_subdivision:
        template_path = TEMPLATES_DIR / "title" / f"{palette_key}.md"
        if template_path.exists():
            template = template_path.read_text(encoding="utf-8")
            filled = fill_title_template(template, card_data)

            # Replace the base template header with a card-specific one
            filled = re.sub(
                r"^# Base Template:.*$",
                f"# Prompt: {title} — Title Card ({palette_key})",
                filled,
                flags=re.MULTILINE,
            )

            out_path = OUTPUT_DIR / f"{card_stem}_title.md"
            if not dry_run:
                out_path.write_text(filled, encoding="utf-8")
            outputs.append(str(out_path))
            print(f"  ✓ Title card → {out_path.name}")

    # Content card (always)
    template_path = TEMPLATES_DIR / "content" / f"{palette_key}.md"
    if template_path.exists():
        template = template_path.read_text(encoding="utf-8")
        filled = fill_content_template(template, card_data)

        filled = re.sub(
            r"^# Base Template:.*$",
            f"# Prompt: {title} — Content Card ({palette_key})",
            filled,
            flags=re.MULTILINE,
        )

        out_path = OUTPUT_DIR / f"{card_stem}_content.md"
        if not dry_run:
            out_path.write_text(filled, encoding="utf-8")
        outputs.append(str(out_path))

        # Count review flags
        review_count = filled.count("<!-- REVIEW")
        pattern_count = len(card_data["patterns"])
        print(f"  ✓ Content card → {out_path.name}  ({review_count} review flags, {pattern_count} patterns detected)")

    return outputs


def main():
    parser = argparse.ArgumentParser(description="Generate image prompts from card metadata")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing files")
    parser.add_argument("--card", type=str, help="Process a single card by filename (without .md)")
    args = parser.parse_args()

    # Load palette map
    if not PALETTE_MAP_PATH.exists():
        print(f"✗ palette_map.json not found at {PALETTE_MAP_PATH}")
        sys.exit(1)

    palette_map = json.loads(PALETTE_MAP_PATH.read_text(encoding="utf-8"))

    # Create output directory
    if not args.dry_run:
        OUTPUT_DIR.mkdir(exist_ok=True)

    # Find all card files
    card_files = []
    for element_dir in sorted(ELEMENTS_DIR.iterdir()):
        cards_dir = element_dir / "resources" / "cards"
        if cards_dir.exists():
            for card_file in sorted(cards_dir.glob("*.md")):
                if args.card and card_file.stem != args.card:
                    continue
                card_files.append(card_file)

    print(f"\n{'═' * 60}")
    print(f"  FX2 Prompt Generator")
    print(f"  Found {len(card_files)} card files")
    print(f"  Output: {OUTPUT_DIR}")
    print(f"  Mode: {'DRY RUN' if args.dry_run else 'GENERATING'}")
    print(f"{'═' * 60}\n")

    total_outputs = []
    total_title = 0
    total_content = 0

    for card_file in card_files:
        print(f"\n📄 {card_file.relative_to(ELEMENTS_DIR)}")
        outputs = process_card(card_file, palette_map, args.dry_run)
        total_outputs.extend(outputs)
        total_title += sum(1 for o in outputs if "title" in o)
        total_content += sum(1 for o in outputs if "content" in o)

    print(f"\n{'═' * 60}")
    print(f"  Done! Generated {len(total_outputs)} prompts")
    print(f"  Title cards: {total_title}")
    print(f"  Content cards: {total_content}")
    print(f"{'═' * 60}\n")

    if total_outputs:
        print("Next step: Run an LLM over the generated files to fill <!-- REVIEW --> placeholders.")


if __name__ == "__main__":
    main()
