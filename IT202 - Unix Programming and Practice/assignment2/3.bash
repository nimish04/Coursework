a=0
echo -n "Enter no. of elememts: "
read n
k=""
for i in $(seq 1 $n)
do
	echo -n "Enter elements $i: "
	read a
	k="$k$a"$'\n'
done
echo -n "$k"|sort -n > a.txt
k=`uniq -dc a.txt`
echo "Maximum value: $(tail -1 a.txt)"
echo "Minimum value: $(head -1 a.txt)"
if [ -z "$k" ]
	then
	printf "No repeated values!\n"
else
	printf "Following are the repeated values.\nOccurences : Values\n"
	echo "$k"
fi