# Create a Python script that performs the following:

# Prompt the user to type a string input as the variable for your destination URL.

# Prompt the user to select a HTTP Method of the following options:
# GET
# POST
# PUT
# DELETE
# HEAD
# PATCH
# OPTIONS
# Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.
# Add some comments of what these request are doing to your script
# Using the requests library, perform a GET request to your github.

# For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should print Site not found to the terminal instead of 404.
#response = requests.get()
# For the given URL, print response header information to the screen.

#sets the response as the selected website
from urllib import response
#summons the type of request you select
import requests
#prompts user for a url
url = input("Enter a website: ")
#list http methods 
http_methods = ["GET", "POST", "PUT", "DELETE", "HEAD", "PATCH", "OPTIONS"]
#prompts user for http method
http_method = input("Select an HTTP Method: ")
#tells code to assign numbers to the http method list
for index, method in enumerate(http_methods):
    print(f"{index + 1}: {method}")
method_choice = int(input("Enter the number corresponding to your choice: ")) - 1
http_method = http_methods[method_choice]
print(f"\nYou are about to send a {method} request to {url}.")
if http_method == "GET":
    response = requests.get(url)
    print(response.headers)
elif http_method == "POST":
    response = requests.post(url)
    print(response.headers)
elif http_method == "PUT":
    response = requests.put(url)
    print(response.headers)
elif http_method == "DELETE":
    response = requests.delete(url)
    print(response.headers)
elif http_method == "HEAD":
    response = requests.head(url)
    print(response.headers)
elif http_methods == "PATCH":
    response = requests.patch(url)
    print(response.headers)
elif http_method == "OPTIONS":
    response = requests.options(url)
    print(response.headers)
