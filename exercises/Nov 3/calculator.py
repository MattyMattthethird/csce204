def factorial(num):
    answer = 1

    for i in range(1, num+ 1):
        answer *= i

    print(f"{num}! = {answer}")

# sums up the numbers from one to num



















def get_int(prompt):
    while True:
        try:
            num = int(input(prompt))
            break
        except ValueError:
            print("Invalid whole number.")
    return num 

def get_float(prompt):
    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            print("Invalid decimal number")
    return num 

# My program
num = get_int("Enter Number: ")
factorial(num)