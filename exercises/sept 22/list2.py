colors = ["pink", "purple", "blue", "red", "orange"]

print("Welcome to our color fun program!")

while True:
    option = input("(V)iew, (A)dd, (R)emove, (Q)uit: ").lower().strip()

    if option == "q":
        break
    elif option == "v":
        print("Colors:")
        for color in colors:
            print(f"-{color}")
    elif option == "a":
        new_color = input("Enter Color: ")
        colors.append(new_color)
        print(f"{new_color} was added.")
    elif option == "r":
        color = input("Enter Color: ")
        colors.remove(color)
        print(f"{color} was removed.")
    else:
        print("Invalid input")
print("goodbye") 