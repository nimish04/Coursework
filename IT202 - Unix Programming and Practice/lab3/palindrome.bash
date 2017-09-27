echo -n "Enter the string: "
read check
n=$(echo "scale=0;${#check}/2" | bc)
n=$(echo "scale=0;$n-1" | bc)
flag=0
for i in $(seq 0 $n)
do
	store=$(echo "scale=0;${#check}-$i-1" | bc)
	if [ "${check:i:1}" != "${check:store:1}" ]; then
		flag=1
		break
	fi
done
if test $flag -eq 0
	then
	echo "Yes, palindromic"
else
	echo "No, not palindromic"
fi