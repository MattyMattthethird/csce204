print("Color Party")

while True:
    guess = input("Guess my fav color: ").lower().strip()

    if guess == "yellow":
        print("YAY")
        break #kicks you out of the loop

    print("wrong")

    again = input("Do you want to guess again (Y)es or (N)o: ").lower().strip()

    if again == "n" or again == "no": 
        break

    

print("goodbye")