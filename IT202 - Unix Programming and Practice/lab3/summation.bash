echo -n "Enter n: "
read n
final=$(echo "scale=2;$n*($n+1)/2" | bc)
echo $final