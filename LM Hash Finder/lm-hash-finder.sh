#!/bin/bash

inputFile="ntds.txt"        # Path to the input file
outputLmFile="lm_hashes.txt"   # Path to the LM hashes output file
outputOtherFile="other_hashes.txt" # Path to the other hashes output file

# Check if the output files exist and delete them if they do
if [ -f "$outputLmFile" ]; then
    rm "$outputLmFile"
fi

if [ -f "$outputOtherFile" ]; then
    rm "$outputOtherFile"
fi

# Add an extra line at the bottom of the input file
echo >> "$inputFile"

# Initialize variables for LM hashes and other hashes
lmHashes=""
otherHashes=""

# Read the contents of the input file
while IFS= read -r line
do
    # Check if the line is not blank and does not contain 'aad3b435b51404eeaad3b435b51404ee'
    if [[ -n "$line" && ! "$line" =~ "aad3b435b51404eeaad3b435b51404ee" ]]; then
        # Append the line to the LM hashes variable
        lmHashes+="\n$line"

        # Append the line to the LM hashes output file
        echo "$line" >> "$outputLmFile"
    elif [[ -n "$line" ]]; then
        # Append the line to the other hashes variable
        otherHashes+="\n$line"

        # Append the line to the other hashes output file
        echo "$line" >> "$outputOtherFile"
    fi
done < "$inputFile"

# Inform the user about the output files and the hashes found
echo -e "Hashes categorized:"
echo -e "LM hashes have been saved to $outputLmFile"
echo -e "Other hashes have been saved to $outputOtherFile"
echo -e "\nLM Hashes:"
echo -e "$lmHashes"
echo -e "\nOther Hashes:"
echo -e "$otherHashes"



echo -e "\n*********** Please note the LM hashes are the following vulnerability: Domain LAN Manager Password Hashes:

The LAN Manager (LM) hash function was the default method for hashing local and domain level passwords prior to Windows NT. It was noted that some hash information extracted from the domain controller was stored in LM format, which can be cracked quickly using precompiled rainbow tables.
As the hashes are stored in the LM format, even strong, complex passwords can be cracked in a short period of time. It was determined that LM hashing is already disabled for the domain as there were only a small amount of accounts that utilised it. It is likely that these accounts last had their password changed when LM hashing was still enabled. A password reset for the affected accounts will remove the LM hash."
