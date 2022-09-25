todolist = []

print("Welcome to the todo list.")

while True:
    option = input("(V)iew, (A)dd, (R)emove, (Q)uit: ").lower().strip()

    if option == "q":
        break
    elif option == "v":
        print("todolist:")
        for todo in todolist:
            print(f"-{todo}")
        if len(todolist) == 0:
            print("Yay there is nothing todo on this list!")
    elif option == "a":
        new_todo = input("Enter ToDo: ")
        todolist.append(new_todo)
        print(f"{new_todo} was added.")
    elif option == "r":
        todo = input("Enter Color: ")
        todolist.remove(todo)
        print(f"{todo} was removed.")
    else:
        print("Invalid input")
print("goodbye") 