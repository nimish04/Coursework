oneToTen=("one" "two" "three" "four" "five" "six" "seven" "eight" "nine")
elevenToNineteen=("eleven" "twelve" "thirteen" "fourteen" "fifteen" "sixteen" "seventeen" "eighteen" "nineteen")
tenToNinty=("ten" "twenty" "thirty" "fourty" "fifty" "sixty" "seventy" "eighty" "ninty")
echo -n "Enter a number: "
read number
string=""
if [ $number -lt 1 ]
	then
	exit
elif [ $number -lt 10 ]
	then
	string="${oneToTen[`expr $number - 1`]}"
elif [ $number -eq 10 ]
	then
	string="${tenToNinty[0]}"
elif [ $number -lt 20 ]
	then
	string="${elevenToNineteen[`expr $number - 11`]}"
elif [ $number -lt 100 ]
	then
	val=$(echo "scale=0; ($number % 10) - 1" | bc)
	string="${oneToTen[$val]}"
	number=`expr $number / 10`
	val=$(echo "scale=0; ($number % 10) - 1" | bc)
	string="${tenToNinty[$val]} $string"
elif [ $number -lt 1000 ]
	then
	lastDigit=$(echo "scale=0; $number / 100" | bc)
	number=$(echo "scale=0; $number % 100" | bc)
	if [[($number -lt 10) && ($number -gt 0)]]
		then
		string="${oneToTen[`expr $number - 1`]}"
	elif [ $number -eq 10 ]
		then
		string="${tenToNinty[0]}"
	elif [ $number -lt 20 ]
		then
		string="${elevenToNineteen[`expr $number - 11`]}"
	elif [ $number -lt 100 ]
		then
		if [ $(echo "scale=0; $number % 10" | bc) -ne 0 ]
			then
			val=$(echo "scale=0; ($number % 10) - 1" | bc)
			string="${oneToTen[$val]}"
		fi
		number=`expr $number / 10`
		val=$(echo "scale=0; ($number % 10) - 1" | bc)
		string="${tenToNinty[$val]} $string"
	fi
	string="${oneToTen[`expr $lastDigit - 1`]} hundred $string"
fi
echo $string