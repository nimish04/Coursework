echo "Calculator"
echo -n "Enter 1 to add, 2 to substract, 3 to multiply and 4 to divide: "
read option
echo -n "Enter the first number: "
read a
echo -n "Enter the second number: "
read b
if test $option -eq 1
	then
	res=$(echo "scale=2;$a+$b" | bc)
	printf "%.2f" $res
elif test $option -eq 2
	then
	res=$(echo "scale=2;$a-$b" | bc)
	printf "%.2f" $res
elif test $option -eq 3
	then
	res=$(echo "scale=2;$a*$b" | bc)
	printf "%.2f" $res
elif test $option -eq 4
	then
	if test $b -eq 0
		then
		echo "Division by 0 error!"
		exit 1
	fi
	res=$(echo "scale=2;$a/$b" | bc)
	printf "%.2f" $res
else
	echo "You have entered wrong option."
fi