if [ $# -eq 0 ]
then
echo "Error - Number missing from command line argument"
echo "Syntax: $0 number"
echo "Use to print multiplication table"
fi
n=$1
i=1
while [ $i -le 10 ]
do
echo "$n * $i = `expr $i \* $n`"
i=`expr $i + 1`
done
