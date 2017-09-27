#!/bin/bash
ch=0
p=0
t=0
r=0
area=0
echo "1.Simple Interest"
echo "2.Area of Circle"
echo -n "Enter your choice: "
read ch
if test $ch -eq 1
	then
	echo -n "Enter principle:"
	read p
	echo -n "Enter time: "
	read t
	echo -n "Enter rate: "
	read r
	si=$(echo "scale=2;$p * $t * $r / 100" | bc)
	printf "Simple Interest: %.2f\n" $si
else
	echo -n "Enter radius: "
	read ra
	pi=3.14
	area=$( echo "scale=2;$pi * $ra * $ra" | bc )
	printf "Area: %.2f\n" $area
fi