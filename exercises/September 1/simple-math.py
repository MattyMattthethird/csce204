# Author Matt Murray
import math

# incrementing age
age = float(input("Enter Age: "))
first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
future_age = age + 10

print(f"{first_name} {last_name}, next decade you will be {future_age}!")

# Pizza party
print("We're having a pizza party!")
num_guests = int(input("Enter number of guests: "))
avg_slices = float(input("Enter average slices per guest: "))
total_slices = num_guests * avg_slices
num_pizzas = math.ceil(total_slices / 8)

print(f"You should order {num_pizzas} pizzas.")

# How many eggs
num_eggs = int(input("How many eggs: "))
num_cartons = num_eggs // 12
#extra_eggs = num_eggs - num_cartons * 12
extra_eggs = num_eggs % 12

print(f"""
You need {num_cartons} cartons
You have {extra_eggs} eggs left over.""")

# Overtime wage
hourly_wage = float(input("How much do you get paid per hour: "))
overtime_wage = hourly_wage * 1.5
print(f"You should make ${round(overtime_wage,2)} in overtime.")
