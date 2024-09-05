#!/bin/bash
# Lets create a while loop than runs a conditinal statment
#Ask the user for an input if they choose:
# 1 then echo hello world
# 2 ping a website or ip address
# 3 run ifconfig
# else echo invalid entry

while true; do
    display_menu
    read -p "Enter your choice (1/2/3/4): " choice

    case $choice in
        1)
            echo "Hello World"
            ;;
        2)
            read -p "Enter IP address:" target
            if [[ -n $target ]]; then
                ping -c 4 "$target"
            else
                echo "No target specified."
            fi
            ;;
        3)
            ifconfig
            ;;
        4)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid entry"
            ;;
    esac
done

