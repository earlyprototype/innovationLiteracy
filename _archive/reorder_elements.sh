#!/bin/bash

# Reorder elements to place Environment before Collaboration, Facilitation last
# New order: 1-6 unchanged, 7=Environment, 8=Collaboration, 9=Facilitation

cd "$(dirname "$0")"

echo "Reordering elements..."
echo ""

# Rename in reverse order to avoid conflicts
mv "9_Environment" "temp_7_Environment"
mv "8_Facilitation" "temp_9_Facilitation"
mv "7_Collaboration" "temp_8_Collaboration"

# Now rename from temp
mv "temp_7_Environment" "7_Environment"
mv "temp_8_Collaboration" "8_Collaboration"
mv "temp_9_Facilitation" "9_Facilitation"

echo "RENAMED: 9_Environment → 7_Environment"
echo "RENAMED: 8_Facilitation → 9_Facilitation"
echo "RENAMED: 7_Collaboration → 8_Collaboration"
echo ""
echo "New order:"
ls -d */ | sort
