for file in *
do
	if [ -f $file ]
		then
		userPermission=$(echo "$(stat -c %a $file) / 100" | bc)
		if [ $userPermission -ge 6 ]
			then
			echo $file
		fi
	fi
done