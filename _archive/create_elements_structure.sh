#!/bin/bash

# Create Elements folder structure for Innovation Literacy workshop
# Each of the 9 elements gets a subfolder with a definition markdown

BASE_DIR="./Elements"

# Array of elements
elements=(
    "1_Process"
    "2_Interventions"
    "3_Tools"
    "4_Skills_and_Competencies"
    "5_Mindset"
    "6_Behaviours"
    "7_Teams"
    "8_Facilitation"
    "9_Environment"
)

# Create base Elements directory
mkdir -p "$BASE_DIR"

# Create each element subfolder with its markdown file
for element in "${elements[@]}"; do
    # Create subfolder
    mkdir -p "$BASE_DIR/$element"
    
    # Extract clean name for markdown file (remove number prefix and underscores)
    clean_name=$(echo "$element" | sed 's/^[0-9]*_//' | sed 's/_/ /g')
    
    # Determine singular or plural for filename
    case "$clean_name" in
        "Skills and Competencies"|"Behaviours"|"Teams"|"Tools")
            filename="What are ${clean_name}.md"
            ;;
        *)
            filename="What is ${clean_name}.md"
            ;;
    esac
    
    # Create the markdown file
    filepath="$BASE_DIR/$element/$filename"
    
    # Add basic content to the markdown file
    cat > "$filepath" << EOF
# What is ${clean_name}?

## Definition

[To be completed - concise definition of ${clean_name} as it relates to innovation literacy]

## Why It Matters

[To be completed - explain the importance and impact]

## How It Shows Up in Practice

[To be completed - concrete examples and observable manifestations]

## In This Workshop

[To be completed - where and how this element is experienced/taught]

## Further Reading

[To be completed - resources for deeper exploration]

---

_Element: ${clean_name}_  
_Colour Code: [To be assigned]_  
_Icon: [To be assigned]_
EOF

    echo "Created: $filepath"
done

echo ""
echo "Elements structure created successfully in $BASE_DIR"
echo "Total elements: ${#elements[@]}"
