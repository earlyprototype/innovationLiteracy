#!/bin/bash

# Create resources subfolder in each Elements folder (except 1_Process which already has one)

BASE_DIR="."

# Array of element folders
elements=(
    "0_Innovation_Literacy"
    "2_Interventions"
    "3_Tools"
    "4_Skills_and_Competencies"
    "5_Mindset"
    "6_Behaviours"
    "7_Teams"
    "8_Facilitation"
    "9_Environment"
)

echo "Creating resources subfolders in Elements..."
echo ""

for element in "${elements[@]}"; do
    resources_path="$BASE_DIR/$element/resources"
    
    if [ -d "$resources_path" ]; then
        echo "SKIP: $element/resources (already exists)"
    else
        mkdir -p "$resources_path"
        echo "CREATED: $element/resources"
    fi
done

echo ""
echo "Resources folders creation complete."
echo "Note: 1_Process/resources already existed and was not modified."
