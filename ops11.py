# Your program should print each number from 1 to 100 in turn.

# When the number is divisible by 3 then instead of printing the number it should print "Fizz".

# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

#   And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

# You will need to use a for loop to write this:


#Write your code below this row 👇
import math
counter = 1
for counter in range(1, 101):
    if counter % 3 == 0 and counter % 5 == 0:
        print("fizzbuzz")
        counter += 1
    elif counter % 3 == 0:
        print("Fizz")
        counter += 1
    elif counter % 5 == 0:
        print("buzz")
        counter += 1
    else:
        print(counter)
