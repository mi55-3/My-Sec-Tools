Make the lm-hash-finder.sh an executable

chmod +x lm-hash-finder.sh

and run the command as follows 
./lm-hash-finder.sh

please make sure the ntds.txt file is located within the same directory as the script or ensure you change the path. 

This can also be done very quickly with the following command

grep 'aad3b435b51404eeaad3b435b51404ee' -v file | awk -F ":" '{print $1}'






