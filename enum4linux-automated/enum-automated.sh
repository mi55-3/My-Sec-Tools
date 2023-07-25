#!/bin/bash

# Read the IP addresses from the file
while IFS= read -r IP
do
    # Execute the command with the IP address and redirect the output to a file
    sudo perl /home/remote/enum4linux/enum4linux.pl -a "$IP" > "$IP-output.txt"

    # Display a message indicating the completion of processing for the current IP
    echo "Processing of $IP completed."

done < enum-targets.txt

# Read each output file and check for null sessions
while IFS= read -r IP
do
    # Read the contents of the output file
    content=$(cat "$IP-output.txt")

    # Check if the output contains null sessions
    if [[ $content == *"null sessions"* ]]; then
        echo "Null sessions found in $IP-output.txt"
    else
        echo "No null sessions found in $IP-output.txt"
    fi

done < enum-targets.txt