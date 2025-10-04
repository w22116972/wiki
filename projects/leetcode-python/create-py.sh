#!/bin/bash

# Usage: ./create-py.sh "2685. Count the Number of Complete Components"

input="$1"

# Extract the number (before the dot)
number=$(echo "$input" | awk -F'.' '{print $1}')

# Extract the title (after the dot and space)
title=$(echo "$input" | sed -E 's/^[0-9]+\. //')

# Convert title to lowercase, replace non-alphanumeric with underscore, collapse multiple underscores
sanitized_title=$(echo "$title" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/_/g' | sed -E 's/^_+|_+$//g' | sed -E 's/_+/_/g')

filename="leetcode_${number}_${sanitized_title}.py"

touch "$filename"
echo "Created $filename"
