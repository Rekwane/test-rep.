# Objectives
# Create if statements using these logical conditionals below. Each statement should print information to the screen depending on if the condition is met.

# Equals: a == b
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
if a == b:
    print("a and b are equal")
elif a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a and b are not equal")


a = int(input("Enter a number "))
b = int(input("Enter a number "))
c = int(input("Enter a number "))
if a == b and b == c:
    print("all are equal" )
elif a > b and b < c:
    print("b is less than a and c")
elif a < b and c == a:
    print("b is greater than c and a")
    print("and c is equal to a")
elif a >= b and b > c:
    print ("a and b are greater than c")
elif a >= b and c > a:
    print("c is greater than a and b")
elif a > b and b >= c:
    print("a is greater than b and c")
elif a < b and b <= c:
    print ("a is less than b and c")
# Less than or equal to: a <= b


# Greater than: a > b
# Greater than or equal to: a >= b
# Create an if statement using a logical conditional of your choice and include elif keyword that executes when other conditions met or and else when no condition is met.



# Stretch Goals (Optional Objectives)
# Pursue stretch goals if you are a more advanced user or have remaining lab time.

# Create an if statement with two conditions by using and between conditions.

# Create an if statement with two conditions by using or between conditions.

# Create a nested if statement.

# Hint:  a = int(input("Enter a number "))