import random

def get_score():
    try:
        with open("exercises/Nov 3/score.txt") as file: 
            for line in file:
                num = int(line.strip())
                return num 
    except FileNotFoundError:
        print("Sorry your file didn't exist")
        return 0
    except ValueError:
        print("Sorry, there is not a number in the file.")
        return 0

def save_score(num):
    try:
        # w for overwrite
        # a for append
        with open("exercises/Nov 3/score.txt", "w") as file:
            file.write(f"{num}/n")
    except FileNotFoundError:
        print("Sorry your file didn't exist")

def sum_digits(number):
    sum = 0

    while number > 0:
        digit = number % 10 
        sum += digit
        number = number // 10

    return sum

def play_round():
    rand_num - random.randint(1000, 9999)
    ans = sum_digits(rand_num)

    user_ans = int(input("Sum the digits of {rand_num}: "))

    if ans == user_ans:
        print("YAY")
        return True
    else:
        print("sorry!")
        return False

score = get_score

if play_round():
    score += 1

    save_score(score)
