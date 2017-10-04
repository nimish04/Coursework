echo -n "Enter a string: "
read string
newstring=$(echo "$string" | rev)
if [ $newstring = $string ]
	then
	echo "It is a palindrome."
else
	echo "Not a palindrome."
fi