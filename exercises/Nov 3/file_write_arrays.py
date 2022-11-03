def save_pets(pets): 
    try:
        with open("exercises/Nov 3/pets.txt", "w") as file:
            # loop through list of pets and write them to the file
            for pet in pets:
                file.write(f"{pet}\n")

    except FileNotFoundError:
        print("Sorry we could not save your pets")

# When you are done make get pets that returns a list of pets from the file
def get_pets(): 
    pets = []

    # read in from the file and add each pet to the list
    try: 
        with open("exercises/Nov 3/pets.txt") as file:
            for line in file: 
                pets.append(line.strip())

    except FileNotFoundError:
        print("Sorry we couldn't load your file")

    return pets 

my_pets = get_pets()

print("My Best Pet's") 

while True: 
    command = input("(V)iew pets, (A)dd pet, (D)elete pet, (Q)uit: ").strip().lower()

    if command == "v":
        for pet in my_pets:
            print(pet)
    elif command == "a":
        pet = input("Enter pet").strip()
        my_pets.append(pet)
    elif command == "d":
        pet = input("Enter pet").strip()

        for p in my_pets:
            if p.lower() == pet:
                my_pets.remove(p)
    elif command == "q":
        break
save_pets(my_pets)