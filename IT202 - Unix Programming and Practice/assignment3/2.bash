for file in *
do
	if [ -f $file ]
		then
		echo "File: $file"
		echo "Content:"
		echo "$(cat < $file)"
		echo
	elif [ -d $file ]
		then
		echo "Directory: $file"
		echo "Files:"
		echo "$(ls $file)"
		echo
	fi
done