def get_count():
    try:
        with open("exercises/Nov 3/count.txt") as file: 
            for line in file:
                num = int(line.strip())
                return num 
    except FileNotFoundError:
        print("Sorry your file didn't exist")
        return 0
    except ValueError:
        print("Sorry, there is not a number in the file.")
        return 0

def save_count(num):
    try:
        # w for overwrite
        # a for append
        with open("exercises/Nov 3/count.txt", "w") as file:
            file.write(f"{num}/n")
    except FileNotFoundError:
        print("Sorry your file didn't exist")


print("Let's Drink Water")
num_glasses = get_count() #gives you previous drinks 

# write the program and update num_glasses
while_True: command = input("(E)nter drinks, (V)iew total, (Q)uit: ").strip().lower() 
if command == "e":
        extra_glasses = int(input("How many glasses: "))
        num_glasses += extra_glasses 

elif command == "v": 
        print(f"You have drank {num_glasses} total glasses.")
elif command == "q": 



save_count(num_glasses)
