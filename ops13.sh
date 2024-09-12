#!/bin/bash
# Bob is back at it again! Now he needs us to script something that if user inserts between 2 to 5, it will print out “Valid Number” and “your number is ___”.
# And if the user input is not between 2 and 5, it will print out “not valid!”
 
#Main
# -eq = equal
# -ne = are not equal
# -gt = greater than
# -ge = greater or equal to
# -lt = less than
# -le = less than or equal to
# >= (Greater than or equal to)
# <= (Less than or equalk to)
# > (Greater)
# < (Less)
# == (comparison)
# % (Remainder)
# * (Multiply)

number = $number
while true; do
    read -p " Enter a number. (2/3/4/5): " number

    if [ $number -eq 2 ]; then 
        echo "Valid number"
        echo "your number is $number"
    elif [ $number -eq 3 ]; then
        echo "Valid number"
        echo "your number is $number"
    elif [ $number -eq 4 ]; then
        echo "Valid number"
        echo "your number is $number"
    elif [ $number -eq 5 ]; then
        echo "Valid number"
        echo "your number is $number"
    else echo "not valid"
    fi
done
