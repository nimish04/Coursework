echo -n "Enter name of first file: "
read first
echo -n "Enter name of second file: "
read second
if [[(-f $first) && (-f $second)]]
	then
	echo "$(cat $first >> $second)"
fi