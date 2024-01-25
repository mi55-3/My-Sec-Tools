---
Make it executable 
---
chmod u+x  automated-enum.sh

---
Create your target list: 
This will normally be DCs/Servers
---
vim enum-targets.txt  

---
Run the command:
---
sudo ./automated-enum.sh

PLEASE READ THIS:
Please note this may not work on all devices so you may need to edit the location of the tool on line7:

sudo perl /home/remote/Tools/enum4linux/enum4linux.pl -a "$IP" > "$IP-output.txt"

Replace "sudo perl /home/remote/Tools/enum4linux/enum4linux.pl" with the correct command:

---
Suggested Paths:
---

sudo perl /home/remote/Tools/enum4linux/enum4linux.pl 

If your tool is set up correctly and does not need to be in path to run you may use:
sudo enum4linux 

---
The idea of this script is for it to run the tool enum4linux against as many IPs as you like and to identify any null sessions. Stopping you from having to type the command out numerous times. Please note, if this finishes within seconds and or no files are produced, most likely this means the tool has failed. It should tell you within the terminal if there are or are not null sessions and as a conteigency it will procide the output for each IP in its own individual TXT file, please look over this. 

This script normally fails when you fail to give it the correct path to the tool. 
