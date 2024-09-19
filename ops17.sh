#!/bin/bash

# Challenge today is to create a script that list all the devices on the network and ask the user to ping one of the ip address.
# There is a few different ways to list all deivices on your network you could use an arp command or an nmap command.
# We will run the a command that prints all address then ask the user to ping a specific one by entering an ip address.

echo "select method to list all devices (1/2/3):" number
read number
num=number
ip=192.168.1.0/24
while true; do
    case $number in
        1)
            echo "Retrieving Devices"    
            nmap -sn $ip
            break
            ;;
        2)
            echo "Retrieving Devices"
            arp -e
            break
            ;;
        3) ls /dev
            break
    esac
done
echo "ping one ip address:"
read ip address
ping $ip_address