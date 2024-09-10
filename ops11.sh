#!/bin/bash
# Given three integers (, , and ) representing the three sides of a triangle, identify whether the triangle is scalene, isosceles, or equilateral.
# If all three sides are equal, output EQUILATERAL.
# Otherwise, if any two sides are equal, output ISOSCELES.
# Otherwise, output SCALENE.
# Input Format
# Three integers, each on a new line.
# Constraints
# The sum of any two sides will be greater than the third.
# Output Format
# One word: either "SCALENE" or "EQUILATERAL" or "ISOSCELES" (quotation marks excluded).
# Hint &&(and) ||(or)

# Read the three sides of the triangle
read a
read b
read c

# Check for equilateral triangle
if [[ $a -eq $b && $b -eq $c ]]; then
    echo "EQUILATERAL"
# Check for isosceles triangle
elif [[ $a -eq $b || $b -eq $c || $a -eq $c ]]; then
    echo "ISOSCELES"
# Otherwise, it must be scalene
else
    echo "SCALENE"
fi
fi