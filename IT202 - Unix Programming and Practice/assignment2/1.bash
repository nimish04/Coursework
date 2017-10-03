first=$1
second=$2
if test $1 -le 0
	then
	while true
	do
		echo -n "1st input is wrong. Enter a +ve number: "
		read first
		if [ $first -gt 0 ]
			then
			break
		fi
	done
fi
if test $2 -le 0
	then
	while true
	do
		echo -n "2nd input is wrong. Enter a +ve number: "
		read second
		if [ $second -gt 0 ]
			then
			break
		fi
	done
fi
echo "Input successful!"
echo "First number: $first"
echo "Second number: $second"