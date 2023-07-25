Create the bash script:
vim automated-enum.sh 

Make it executable 
chmod u+x  automated-enum.sh

Create your target list
vim enum-targets.txt  

Run the command:
sudo ./automated-enum.sh

Please note this may not work on all devices so you may need to edit the location of the tool on line7:
sudo perl /home/remote/Tools/enum4linux/enum4linux.pl -a "$IP" > "$IP-output.txt"

Replace "sudo perl /home/remote/Tools/enum4linux/enum4linux.pl" with the correct command:

Suggested Paths:

sudo perl /home/remote/Tools/enum4linux/enum4linux.pl 

In path:
enum4linux 