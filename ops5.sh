#!/bin/bash
# Install whois on your Ubuntu

# Add to your bash script a sixth option that calls a function to:

# Take a user input string. Presumably the string is a domain name such as Google.com.
read -p "Enter a domain name" Domain
 echo "$Domain"
# Run whois against a user input string.
function whodis() {
    {
        whois $Domain
    } >> "who.txt"
}    
whodis
# Run dig against the user input string.
function yadig(){
    {
    dig $Domain
    } >> "dig.txt"
}
yadig
# Run host against the user input string.
function dohost() {
    {
        host $Domain
    } >> "host.txt"
}    
dohost
# Run nslookup against the user input string.
function ns() {
    {
        nslookup $Domain
    } >> "ns.txt"
}    
ns
# Output the results to a single .txt file and open it with your favorite text editor.

# For this challenge you must use at least one variable and one function.
