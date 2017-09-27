echo "Enter 1 to view date"
echo "Enter 2 to view calender"
echo "Enter 3 to view all users"
echo "Enter 4 to view current user"
echo "Enter 5 to view terminal details"
echo -n "Enter option: "
read option
if test $option -eq 1
	then
	hold=$(date +'%D')
	printf "%s\n" $hold
elif test $option -eq 2
	then
	hold=$(cal)
	printf "%s\n" $hold
elif test $option -eq 3
	then
	hold=$(who)
	echo $hold
elif test $option -eq 4
	then
	hold=$(whoami)
	echo $hold
elif test $option -eq 5
	then
	hold=$(tty)
	echo $hold
else
	echo "Wrong option!"
fi