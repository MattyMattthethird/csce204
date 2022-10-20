from curses import BUTTON1_RELEASED
import random 

# Will generate to random number between 1 & 6
#Will print out the roll
# Will return the total of the two dice 
def roll():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print(f"You rolled a {dice1} and a {dice2}")
    return dice1+dice2

print("Let's Play Lucky Sevens")

while True:
    command = input("(R)oll or (Q)uit: ").lower().strip()

    if command =="q":
        break
    elif command !="r":
        print("Invalid command")
        continue   # goes to beginning of loop

    # main program
    num = roll()

    if num == 7:
        print("You are lucky")
    else:
        print("You are not lucky")
