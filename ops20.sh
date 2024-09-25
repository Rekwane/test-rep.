#!/bin/bash
# Write a script that counts the number of the lines in a file.
# Hint need to use the wc command

ls
read -p "Choose a file:" file
file=$file
while true; do
    wc -l $file
    break
done