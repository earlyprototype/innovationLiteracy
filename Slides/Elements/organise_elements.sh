#!/bin/bash
# Organise element slide prep files into individual subfolders per element.
# Run from the Slides/Elements/ directory.
# Each element (E00-E11) gets its own subfolder containing its title + card files.

cd "$(dirname "$0")"

declare -A NAMES=(
  [E00]="E00_InnovationLiteracy"
  [E01]="E01_Process"
  [E02]="E02_Interventions"
  [E03]="E03_Tools"
  [E04]="E04_Skills"
  [E05]="E05_Mindset"
  [E06]="E06_Behaviours"
  [E07]="E07_Environment"
  [E08]="E08_Collaboration"
  [E09]="E09_Facilitation"
  [E10]="E10_Governance"
  [E11]="E11_Resources"
)

for prefix in "${!NAMES[@]}"; do
  folder="${NAMES[$prefix]}"
  mkdir -p "$folder"
  mv ${prefix}_title.md ${prefix}a_*.md ${prefix}b_*.md ${prefix}c_*.md "$folder/" 2>/dev/null
  echo "Moved $prefix files -> $folder/"
done

echo ""
echo "Done. Structure:"
for prefix in E00 E01 E02 E03 E04 E05 E06 E07 E08 E09 E10 E11; do
  folder="${NAMES[$prefix]}"
  count=$(ls "$folder"/*.md 2>/dev/null | wc -l)
  echo "  $folder/ ($count files)"
done
