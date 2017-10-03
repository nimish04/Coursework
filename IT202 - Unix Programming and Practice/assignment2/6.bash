count1=0
count2=0
for file in *
do
    if [ -f $file ]
        then
        count1=`expr $count1 + 1`
        echo "File :$file"

    elif [ -d $file ]
        then
        count2=`expr $count2 + 1`
        echo "Directory: $file"
    fi
   
done
echo "Number of files: $count1"
echo "Number of directories: $count2"