echo -n "Enter n: "
read n
count=0
summ=0
for i in $(seq 1 $n)
do
	read num
	count=$(expr $count + 1)
	summ=$(expr $summ + $num)
done
final=$(echo "scale=2;$summ/$count" | bc)
printf "Avg: %.2f\n" $final