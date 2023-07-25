make the find-copromised-admns.sh executable
chmod +x find-copromised-admns.sh

please ensure compromised_users.txt contains the list of users compromised from the audit or any users that the password has been revealted.

ensure the domain_admin.txt contains all the domain admins from the network.

run the script
./find-compromised-admins.sh

this will find any domain admins listed in the domain admin file that have been compromised, this will tell you in terminal and also created a compromised_admin.txt, this does not need to be empty, the script will replace this file each time on its own.