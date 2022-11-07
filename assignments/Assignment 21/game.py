import random
#Return array storing com score and player score
def get_score():
    numbers = []
    try:
        with open("score.txt") as file:
            for line in file:
                num = int(line.strip())
                #return num 
                numbers.append(num)
            return numbers
    except FileNotFoundError:
        print("Sorry your file didn't exist")
        return 0
    except ValueError:
        print("Sorry, there is not a number in the file.")
        return 0
#Overwrites scores to file
def save_score(com_score, player_score):
    try:
        # w for overwrite
        # a for append
        with open("score.txt", "w") as file:
            file.write(f"{com_score}\n")
            file.write(f"{player_score}\n")
    except FileNotFoundError:
        print("Sorry your file didn't exist")
#Array storing scores in format [com_score, player_score]
scores = get_score()
while(True):#Main game loop
    #Print the score
    print("Computer score: ", scores[0], "    Player score: ", scores[1])
    #Generate random number
    rand_num = random.randint(0,2)
    #Set the computer action based on rand_num
    action = "r"
    if (rand_num == 0): action = "p"
    elif (rand_num == 1): action = "s"
    while(True): #Loop until valid input accepted
        #Get the user action
        user_ans = str(input("(R)ock, (P)aper, (S)cissors, or (Q)uit: ")).lower()
        if (user_ans == 'r' or user_ans == 'p' or user_ans == 's' or user_ans == 'q'): break
        print("Invalid input")
    #Quit if it was chosen
    if (user_ans == 'q'): break
    #Print computer actino
    if(action == 'r'): print("The computer chose rock")
    elif(action == 'p'): print("The computer chose paper")
    else: print("The computer chose scissors")
    #Decide winner
    if(user_ans == action):
        print("Tie game")
    else:
        if (user_ans == 'r'):
            if (action == 'p'):
                print("The computer beat you")
                scores[0] += 1
            if (action == 's'):
                print("You beat the computer")
                scores[1] += 1
        if (user_ans == 'p'):
            if (action == 's'):
                print("The computer beat you")
                scores[0] += 1
            if (action == 'r'):
                print("You beat the computer")
                scores[1] += 1
        if (user_ans == 's'):
            if (action == 'r'):
                print("The computer beat you")
                scores[0] += 1
            if (action == 'p'):
                print("You beat the computer")
                scores[1] += 1
#Save score after game has been exited
save_score(scores[0], scores[1])