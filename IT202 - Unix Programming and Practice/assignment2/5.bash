for i in $(seq 1 999)
do
	hundredthDigit=`expr $i / 100`
	firstTwoDigits=`expr $i / 10`
	tenthDigit=`expr $firstTwoDigits % 10`
	onethDigit=`expr $i % 10`
	sumCheck=$(echo "$hundredthDigit^3 + $tenthDigit^3 + $onethDigit^3" | bc)
	if [ $sumCheck -eq $i ]
		then
		echo $i
	fi
done