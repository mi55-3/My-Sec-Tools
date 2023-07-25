#!/bin/bash

compromisedFile="compromised_users.txt"  # Path to the compromised users file
adminsFile="domain_admins.txt"           # Path to the domain admins file
outputFile="compromised_admins.txt"      # Path to the output file

# Check if the output file exists and delete it if it does
if [ -f "$outputFile" ]; then
    rm "$outputFile"
fi

# Inform the user that the comparison is processing
echo "Processing the comparison..."

# Compare the compromised users file with the domain admins file
while IFS= read -r compromisedUser
do
    grep -x "$compromisedUser" "$adminsFile" >> "$outputFile"
done < "$compromisedFile"

# Inform the user that the comparison is finished
echo "Comparison finished."

# Display the compromised admins in the terminal
echo -e "Compromised Admins:"
cat "$outputFile"
