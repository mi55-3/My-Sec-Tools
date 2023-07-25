#!/bin/bash

# Read the IP addresses from the file
while IFS= read -r IP
do
    # Execute the command with the IP address and redirect the output to a file
    sudo perl /home/remote/Tools/enum4linux/enum4linux.pl -a "$IP" > "$IP-output.txt"

    # Display a message indicating the completion of processing for the current IP
    echo "Processing of $IP completed."

done < enum-targets.txt