if [ -z $1 ]
then
rental="*** Unknown Vehicle ***"
elif [ -n $1 ]
then
rental=$1
fi
case $rental in 
"car") echo "For $rental Rs.20 per km";;
"van") echo "For $rental Rs.10 per km";;
"jeep") echo "For $rental Rs.5 per km";;
"bicycle") echo "For $rental Rs.0.20 per km";;
*) echo "Sorry cannot get a $rental for you";;
esac
