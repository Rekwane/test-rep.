#!/bin/bash

# Define the size of the square and the color
function square(){
SIZE=10
COLOR="\033[42m" # Green background
RESET="\033[0m"  # Reset to default

# Print the square
for ((i=0; i<SIZE; i++))
do
    for ((j=0; j<SIZE; j++))
    do
        echo -n -e "${COLOR}  ${RESET}"
    done
    echo
done
}
square
