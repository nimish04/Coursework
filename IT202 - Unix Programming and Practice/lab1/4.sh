osch=0
echo "1. Unix (Sun OS)"
echo "2. Linux (Red Hat)"
echo -n "Select your os choice [1 or 2]?"
read osch
if [ $osch -eq 1 ]
then
echo "You pick up Unix (Sun Os)"
else
if [ $osch -eq 2 ]
then
echo "You Pick up Linux (Red Hat)"
else
echo "What don't you like linux or unix OS?"
fi
fi
