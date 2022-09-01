budgetdays = float(input("How many days are you budgeting for?"))
booksneeded = float(input("How many books do you need?"))
weeksstayed = budgetdays/7

if(weeksstayed > int(weeksstayed)):
    weeksstayed = float(int(weeksstayed) + 1)

cost = 1.07 * (booksneeded * 64.99 + budgetdays * (3.85+8.95+12.79) + weeksstayed * 184.99)

print("Total cost: ", cost)