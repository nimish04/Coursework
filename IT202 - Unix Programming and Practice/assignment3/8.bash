echo -n "Enter marks scored in Unix: "
read unix
echo -n "Enter marks scored in POP: "
read pop
echo -n "Enter marks scored in DSA: "
read dsa
avg=$(echo "scale=0; ($unix + $pop + $dsa) / 3" | bc)
if [ $avg -lt 40 ]
	then
	echo "Fail"
elif [[($avg -lt 50) && ($avg -le 40)]]
	then
	echo "Third Class"
elif [[($avg -lt 60) && ($avg -le 50)]]
	then
	echo "Second Class"
elif [[($avg -lt 70) && ($avg -le 60)]]
	then
	echo "First Class"
elif [ $avg -ge 70 ]
	then
	echo "Distinction"
fi