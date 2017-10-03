n=10
positives=0
negatives=0
zeros=0
array=()
for i in $(seq 1 $n)
do
	echo -n "Enter element $i: "
	read a
	array+=($a)
	if [ $a -gt 0 ]
		then
		positives=`expr $positives + 1`
	elif [ $a -eq 0 ]
		then
		zeros=`expr $zeros + 1`
	else
		negatives=`expr $negatives + 1`
	fi
done
echo "Array: [${array[@]}]"
echo -e "No of positive numbers: $positives \nNo of negative numbers: $negatives\nNo of zeroes: $zeros"