#!/bin/bash

# Function to check if an asset exists in the second file
function asset_exists() {
    local asset="$1"
    local second_file="$2"

    grep -qFx "$asset" "$second_file"
}

# Check if both files are provided as arguments
if [ $# -ne 2 ]; then
    echo "Usage: $0 <file1> <file2>"
    exit 1
fi

first_file="$1"
second_file="$2"

# Check if both files exist
if [ ! -f "$first_file" ]; then
    echo "Error: File '$first_file' does not exist."
    exit 1
fi

if [ ! -f "$second_file" ]; then
    echo "Error: File '$second_file' does not exist."
    exit 1
fi

# Add a blank line at the end of the first file if it doesn't already exist
echo "" >> "$first_file"

# Read each line from the first file and check if it exists in the second file
while IFS= read -r asset; do
    if ! asset_exists "$asset" "$second_file"; then
        echo "Asset '$asset' is missing in '$second_file'"
    fi
done < "$first_file"
