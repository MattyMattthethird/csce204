command = input("Do you want me to say 'hello' (Y)es or (N)o: ").lower().strip()

while command == "y": 
    print("Hello")
    command = input("Do you want to say hello again? (Y)es or (N)o: ").lower().strip()


print("Bye for now")