# Write a multi-line comment with your name, favorite food, and dream job on 3 different lines.
print("Rekwane \n Oranges \n Traveling Legal Attache")

# assign 5 different data types to 5 different variables. At least one datatype must be a string.
mystring = "I love Mom"
f = float(2.2)
num = int(1)
on = True
off = False

# print the length of your string.
print(len(mystring))

# create a new variable called savvy, and assign it the string with this phrase "Learning Python is Awesome!"
savvy= "learning python is awesome"
print(savvy[5:15])

# Replace "Awesome" with "great" in the string
new_savvy= savvy.replace("awesome", "great")
print(new_savvy)

# Create and assign 3 more variables called name, age and length using the multi-variable naming method.
name, age, height = "rekwane", "28", "5ft 5in"
print(f'("hi my name is {name}, I am {28}, and I am {height} feet tall")')


# Format a new string called 'miniBio' using variables in curly brackets to complete this phrase... "Hi my name is (name), I am (tall) and (so) old today."