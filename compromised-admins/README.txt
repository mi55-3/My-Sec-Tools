---
Set up:
---

make the find-copromised-admns.sh executable
chmod +x find-copromised-admns.sh

Please ensure compromised_users.txt contains the list of users compromised, this may be from an audit or any users that the password has been revealed.

Make sure the domain_admin.txt contains all the domain admins from the forest, this may be EA or DA.

---
Simple HOWTO:
---

run the script
./find-compromised-admins.sh

---
What it does:
---

The will find any domain admins listed in the domain admin file that have been compromised, this will tell you in the terminal and also create a compromised_admin.txt, this does not need to be empty, the script will replace this file each time on its own.
