#!/bin/bash
# Today we are going to use a case statment instead of a conditional
# Have the program ask how your day is and echo out a response for good or bad
# Case statment format is a little different so please look up how this would be formated
# https://linuxize.com/post/bash-case-statement/

while true; do
    read -p " How is your day? (good/bad): " choice

    case $choice in 
        good)
            echo "Glad to hear it"
            break
            ;;
        bad)
            echo "Poor thing"
            break
            ;;
        *)
            echo "invalid entry"
            ;;
    esac
done 
