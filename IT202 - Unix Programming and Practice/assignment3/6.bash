echo -n "Enter number of rows: "
read rows
echo -n "Enter number of columns: "
read columns
rows=`expr $rows - 1`
columns=`expr $columns - 1`
mat1=()
for i in $(seq 0 $rows)
do
	for j in $(seq 0 $columns)
	do
		echo -n "Enter row $i column $j for matrix 1: "
		read mat1[$i,$j]
	done
done
mat2=()
for i in $(seq 0 $rows)
do
	for j in $(seq 0 $columns)
	do
		echo -n "Enter row $i column $j for matrix 2: "
		read mat2[$i,$j]
	done
done
sumMat=()
for i in $(seq 0 $rows)
do
	for j in $(seq 0 $columns)
	do
		sumMat[$i,$j]=`expr ${mat1[$i,$j]} + ${mat2[$i,$j]}`
		echo -n "${sumMat[$i, $j]} "
	done
	echo
done