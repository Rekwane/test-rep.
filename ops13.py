# Create a program using maths and f-Strings that tells us how many 
# days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message 
# with our time left in this format:

# You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.


# 🚨 Don't change the code below 👇
age = int(input("What is your current age? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
years_left_until_90 = 90 - age
#multiply years left by 365 days
days = years_left_until_90 * 365
#multiply years left by 52 weeks
weeks = years_left_until_90 * 52
#multiply years left by 12 months
months = years_left_until_90 * 12

print(f'you have {days} days, {weeks} weeks, and {months} months until you are 90 years old.')