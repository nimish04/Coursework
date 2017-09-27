echo -n "Enter n: "
read n
summ=0
for i in $(seq 1 $n)
do
	summ=`expr $summ + $i`
done
echo $summ