echo -n "Username: "
read username
stty -echo
echo -n "Password: "
read password
stty echo
echo ""
echo -n "Enter your fav team: "
read team
echo $team