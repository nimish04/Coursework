echo -n "Enter basic: "
read basic
dp=$(echo "scale=2;$basic*0.5" | bc)
dp_basic=$(echo "scale=2;$basic+$dp" | bc)
da=$(echo "scale=2;0.35*$dp_basic" | bc)
hra=$(echo "scale=2;0.08*$dp_basic" | bc)
ma=$(echo "scale=2;0.03*$dp_basic" | bc)
pf=$(echo "scale=2;0.1*$dp_basic" | bc)
salary=$(echo "scale=2;$basic+$dp+$da+$hra+$ma-$pf" | bc)
printf "Salary: %.2f\n" $salary