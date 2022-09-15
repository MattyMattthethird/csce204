print("I love math!")

num = int(input("Enter a number between 1 and 10: "))

# number is not in range
if num < 1 or num > 10:
    print("Sorry, invalid input")
else:
    sum = 0

    for i in range(num +1):
        sum += i

print(f"sum of 1 . . . {num} = {sum}. ")
