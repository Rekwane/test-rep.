#!/bin/bash
# Create a script that you think you would use in a daily job routine No right or Wrong anwsers here
# You could ping all the devices in your network?
# Run a script to reset your ip address?
# Create a script that does some math? 

while true; do
    echo "1 add user"
    echo "2 Release/renew ip"
    echo "4 ping ip address"
    read -p "Enter your choice (1/2/4): " choice

    case $choice in
        1)
            sudo adduser chunk
            ;;
        2)
            sudo dhclient -r
            sudo dhclient
            ;;
        4)
           read -p "Enter IP address:" target
            if [[ -n $target ]]; then
                ping -c 4 "$target"
            else
                echo "No target specified."
            fi
            ;;
        *)
            echo "Invalid entry"
            ;;
    esac
done