#!/usr/bin/env python3
"""
batch_generate_images.py — Generate card images via Gemini API.

Reads prompt files from design_assets/generated/, sends them to Gemini's
image generation model, and saves the resulting images.

Prerequisites:
    pip install google-genai Pillow

Usage:
    # Set your API key
    set GEMINI_API_KEY=your_key_here          (Windows)
    export GEMINI_API_KEY=your_key_here       (Linux/Mac)

    # Generate all images
    python batch_generate_images.py

    # Single card
    python batch_generate_images.py --card assumption_mapping_title

    # Dry run (show what would be generated)
    python batch_generate_images.py --dry-run

    # Use lower resolution for testing
    python batch_generate_images.py --resolution 1K

    # Only title cards
    python batch_generate_images.py --type title
"""

import argparse
import os
import re
import sys
import time
from pathlib import Path

# Load .env file from project root
try:
    from dotenv import load_dotenv
    ENV_PATH = Path(__file__).parent.parent / ".env"
    if ENV_PATH.exists():
        load_dotenv(ENV_PATH)
except ImportError:
    pass  # dotenv optional if env var is set directly

try:
    from google import genai
    from google.genai import types
except ImportError:
    print("Missing dependency. Install with:")
    print("  pip install google-genai Pillow python-dotenv")
    sys.exit(1)

# ── Config ───────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).parent
PROMPTS_DIR = BASE_DIR / "generated"
OUTPUT_DIR = BASE_DIR / "images"
STATE_FILE = BASE_DIR / "generation_state.json"

# Model config — Nano Banana 2 (gemini-3.1-flash-image-preview) for 4K image gen
MODEL = "gemini-3.1-flash-image-preview"
FALLBACK_MODELS = [
    "gemini-3.1-flash-image-preview",
    "gemini-2.5-flash-image",
    "gemini-2.0-flash-preview-image-generation",
]
ASPECT_RATIO = "16:9"
DEFAULT_RESOLUTION = "4K"

# Rate limiting — Google AI free tier: ~15 requests/minute for image gen
DELAY_BETWEEN_REQUESTS = 5  # seconds
MAX_RETRIES = 3


def load_state() -> dict:
    """Load generation state to support resume after interruption."""
    import json
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    return {"completed": [], "failed": []}


def save_state(state: dict):
    """Save generation state."""
    import json
    STATE_FILE.write_text(json.dumps(state, indent=2), encoding="utf-8")


def strip_prompt_to_text(prompt_path: Path) -> str:
    """Read a prompt markdown file and strip to plain text for the API.
    
    The model gets confused by markdown formatting in image prompts,
    so we strip headers, bold markers, bullet formatting, and HTML comments
    that are review flags.
    """
    text = prompt_path.read_text(encoding="utf-8")
    
    # Remove the file header line (# Prompt: ...)
    text = re.sub(r"^# Prompt:.*\n", "", text)
    
    # Remove <!-- REVIEW --> flags — these are for human review, not the model
    # Replace with descriptive text instead of leaving blanks
    text = re.sub(r"<!-- REVIEW:.*?-->", "[to be described]", text)
    
    # Remove markdown formatting but keep content
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)  # Bold
    text = re.sub(r"^#+\s+", "", text, flags=re.MULTILINE)  # Headers
    text = re.sub(r"^---\s*$", "", text, flags=re.MULTILINE)  # Horizontal rules
    text = re.sub(r"^- ", "", text, flags=re.MULTILINE)  # Bullet points
    
    # Remove backticks around hex codes (they're for markdown, not the model)
    text = re.sub(r"`(#[A-Fa-f0-9]{6})`", r"\1", text)
    
    # Clean up excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    
    return text.strip()


def generate_image(client, prompt_text: str, resolution: str = DEFAULT_RESOLUTION) -> bytes | None:
    """Send prompt to Gemini and get image bytes back."""
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt_text,
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE"],
            ),
        )
        
        # Extract image from response
        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                return part.inline_data.data
            elif part.text is not None:
                print(f"    Model text: {part.text[:100]}...")
        
        print("    ⚠ No image in response")
        return None
        
    except Exception as e:
        error_str = str(e)
        if "429" in error_str or "rate" in error_str.lower():
            print(f"    ⏳ Rate limited. Waiting 30s...")
            time.sleep(30)
            return None  # Will be retried
        elif "model" in error_str.lower() and "not found" in error_str.lower():
            print(f"    ✗ Model {MODEL} not available: {error_str[:100]}")
            return None
        else:
            print(f"    ✗ Error: {error_str[:150]}")
            return None


def main():
    parser = argparse.ArgumentParser(description="Generate card images via Gemini API")
    parser.add_argument("--dry-run", action="store_true", help="Preview without generating")
    parser.add_argument("--card", type=str, help="Generate a single card by name (without .md)")
    parser.add_argument("--type", choices=["title", "content"], help="Only generate title or content cards")
    parser.add_argument("--resolution", default=DEFAULT_RESOLUTION, choices=["512", "1K", "2K", "4K"],
                        help="Image resolution (default: 4K)")
    parser.add_argument("--resume", action="store_true", help="Skip already-completed cards")
    args = parser.parse_args()

    # Check API key
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key and not args.dry_run:
        print("✗ GEMINI_API_KEY environment variable not set.")
        print("  Get your key from: https://aistudio.google.com/apikey")
        print("  Then run: set GEMINI_API_KEY=your_key_here")
        sys.exit(1)

    # Find prompt files
    if not PROMPTS_DIR.exists():
        print(f"✗ No prompts directory found at {PROMPTS_DIR}")
        print("  Run generate_prompts.py first to create prompt drafts.")
        sys.exit(1)

    prompt_files = sorted(PROMPTS_DIR.glob("*.md"))
    
    # Apply filters
    if args.card:
        prompt_files = [f for f in prompt_files if f.stem == args.card]
    if args.type:
        prompt_files = [f for f in prompt_files if f.stem.endswith(f"_{args.type}")]

    # Load state for resume
    state = load_state() if args.resume else {"completed": [], "failed": []}
    if args.resume:
        prompt_files = [f for f in prompt_files if f.stem not in state["completed"]]

    print(f"\n{'=' * 60}")
    print(f"  FX2 Image Generator — Gemini API")
    print(f"  Model: {MODEL}")
    print(f"  Resolution: {args.resolution} | Aspect: {ASPECT_RATIO}")
    print(f"  Cards to generate: {len(prompt_files)}")
    print(f"  Mode: {'DRY RUN' if args.dry_run else 'GENERATING'}")
    print(f"{'=' * 60}\n")

    if args.dry_run:
        for f in prompt_files:
            prompt = strip_prompt_to_text(f)
            print(f"  {f.stem}")
            print(f"    Prompt length: {len(prompt)} chars")
            print(f"    First 100 chars: {prompt[:100]}...")
            print()
        print(f"Total: {len(prompt_files)} images would be generated.")
        return

    # Create output directory
    OUTPUT_DIR.mkdir(exist_ok=True)

    # Initialize client
    client = genai.Client(api_key=api_key)

    success_count = 0
    fail_count = 0

    for i, prompt_file in enumerate(prompt_files, 1):
        print(f"\n[{i}/{len(prompt_files)}] {prompt_file.stem}")
        
        prompt_text = strip_prompt_to_text(prompt_file)
        out_path = OUTPUT_DIR / f"{prompt_file.stem}.png"
        
        # Skip if already exists (unless overwriting)
        if out_path.exists() and not args.card:
            print(f"    ⏭ Already exists, skipping")
            continue
        
        # Generate with retries
        image_data = None
        for attempt in range(MAX_RETRIES):
            if attempt > 0:
                print(f"    Retry {attempt + 1}/{MAX_RETRIES}...")
                time.sleep(DELAY_BETWEEN_REQUESTS * 2)
            
            image_data = generate_image(client, prompt_text, args.resolution)
            if image_data:
                break
        
        if image_data:
            out_path.write_bytes(image_data)
            print(f"    ✓ Saved → {out_path.name} ({len(image_data) // 1024}KB)")
            success_count += 1
            state["completed"].append(prompt_file.stem)
        else:
            print(f"    ✗ Failed after {MAX_RETRIES} attempts")
            fail_count += 1
            state["failed"].append(prompt_file.stem)
        
        # Save state after each card (crash recovery)
        save_state(state)
        
        # Rate limit delay
        if i < len(prompt_files):
            print(f"    Waiting {DELAY_BETWEEN_REQUESTS}s (rate limiting)...")
            time.sleep(DELAY_BETWEEN_REQUESTS)

    print(f"\n{'=' * 60}")
    print(f"  Done!")
    print(f"  Success: {success_count}")
    print(f"  Failed: {fail_count}")
    print(f"  Output: {OUTPUT_DIR}")
    if state["failed"]:
        print(f"  Failed cards: {', '.join(state['failed'])}")
        print(f"  Re-run with --resume to retry failed cards")
    print(f"{'=' * 60}\n")


if __name__ == "__main__":
    main()
