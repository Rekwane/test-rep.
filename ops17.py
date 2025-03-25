# Write a program in python that splits the bill evenly between group.
# Ask how much they want to tip and how many people


#Example
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
#total cost of bill
# total cost of the bill
total = float(input("What was the total cost: "))
# number of people splitting the bill
num_people = int(input("How many people are splitting the bill?: "))

# Initialize an empty list to store each individual's tip
individual_tips = []

# Get each individual's desired tip percentage
for i in range(num_people):
    percent = int(input(f"Person {i + 1}, what percentage would you like to tip?: "))
    individual_tips.append(percent)

# Calculate the total amount each person will pay
individual_costs = []

for i in range(num_people):
    # Calculate each person's share of the bill
    tip_percentage = individual_tips[i] / 100
    person_share = total / num_people
    total_with_tip = person_share * (1 + tip_percentage)
    individual_costs.append(total_with_tip)

# Output the result for each person
for i in range(num_people):
    print(f"Person {i + 1} will pay: ${individual_costs[i]:.2f}")

