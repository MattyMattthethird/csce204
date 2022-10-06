from datetime import date 

birthdays = [date(2022, 12, 30),
             date(2022, 10, 21),
             date(2023, 1, 14), 
             date(2023, 8, 4),
             date(2023, 5, 12)]
            
# loop through and display birthdays
for bday in birthdays:
    num_days = (bday - date.today()).days
    print(bday.strftime("%b %d"), end = "")
    print(f" - is in {num_days} days")

