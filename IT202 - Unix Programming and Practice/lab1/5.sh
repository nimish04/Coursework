if [ $1 -gt 0 ]
then
echo "$1 is positive"
elif [ $1 -lt 0 ]
then
echo "$1 is negative"
elif [ $1 -eq 0 ]
then
echo "$1 is 0"
else
echo "Oops $1 is not a number."
fi
