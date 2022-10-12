while(1):
    selection = str(input("(L)ist Powers, or (Q)uit: ")).lower() 
    if(selection == 'l'):
        num = float(input("Enter a number: "))
        for i in range(11):
            print(num, " to the power of ", i, " is ", num ** i)
    elif(selection == 'q'):
        print("Goodbye")
        break
    else:
        print("Invalid input")