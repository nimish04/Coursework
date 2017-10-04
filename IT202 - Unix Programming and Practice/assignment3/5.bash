echo -n "Enter a file name: "
read filename
if [ -f $filename ]
	then
	echo "$(stat -c %a $filename)"
fi