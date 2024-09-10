#!/bin/bash
# Lets create an until loop that takes a variable and adds 1 till it reachs 10
# Have the script echo out what are current number is

x=100
until [ $x -lt 10 ]
do 
    echo "your number is" $x
    # ((x++))
    x=$((x-1))
done