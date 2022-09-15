import random 

goal = random.randint(1,100)

print(f"The goal is {goal}")

print("Welcome to the guessing game")

while True:
    guess = int(input("Guess a number between 1 and 100"))

    if guess == goal: 
        print("Yay, you got it")
        break
    elif guess < goal:
        print("Too low")

print("Goodbye")
