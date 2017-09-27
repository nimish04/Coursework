echo "Area of a rectangle"
length=$1
breadth=$2
if test $length -lt 0
	then
	echo "No negatives!"
elif test $breadth -lt 0
	then
	echo "No negatives!"
else
	area=$(echo "scale=2;$length*$breadth" | bc)
	printf "%.2f\n" $area
fi