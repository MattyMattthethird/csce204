from datetime import date

birthdays = {
    "Amy": date(2022, 12, 30),
    "Bobby": date(2023, 1 , 16),
    "Carl": date(2023, 8, 1),
    "Dave": date(2023, 5, 15),
    "Eric": date(2023, 9, 14)
}

# loop through and display friends and birthdays
for friend in birthdays:
    print(f"{friend} - ")
    print(birthdays[friend].strftime("%m/%d"), end = "")
    num_days = (date.today() - birthdays[friend]).days
    print(f"- {num_days} days")