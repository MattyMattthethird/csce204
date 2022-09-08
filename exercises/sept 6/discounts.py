from calendar import TUESDAY


print("Discounts")

# convert input to lowercase and strip off leading and tailing whitespace
DayofWeek = input("Enter day of week: ").lower().strip()

if DayofWeek == "tuesday" or DayofWeek == "tues":
    
    print("Taco Tuesday")
elif DayofWeek == "monday":
    print("Moes Monday")
elif DayofWeek == "wednesday":
    print("Wine Wednesday")
else: 
    print("No discounts today")