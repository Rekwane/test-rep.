# Your task is very simple here: write a program that uses a for loop to "count mississippi" to five.
#  Having counted to five, 
# the program should print to the screen the final message "Ready or not, here I come!"
import time

#Start code below this line:

counter = 0
while counter != 5:
  print(counter, "mississippi")
  counter += 1
  time.sleep(1)
print("ready or not here i come")