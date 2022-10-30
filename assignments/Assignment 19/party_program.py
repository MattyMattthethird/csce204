print('Baby Shower')
def get_guests():
    global file
    ret = {}
    file = open("guest_list.txt", "r")
    length = len(file.readlines())
    file = open("guest_list.txt", "r")
    for i in range(length):
        line = file.readline().split(':')
        ret[line[0]] =  line[1].strip()
    return ret
def display_guests(guests):
    print("\nAttending guest list:")
    for item in guests:
        print("- ", item)
def get_majority_color(guests):
    extraPinkCount = 0
    for item in guests:
        if(guests[item].lower() == 'pink'): extraPinkCount += 1
        elif(guests[item].lower() == 'blue'): extraPinkCount -= 1
    if(extraPinkCount == 0): return("even")
    elif(extraPinkCount > 0): return("pink")
    else: return("blue")
while(True):
    action=str(input("View (G)uest List, (C)olor Winner, (Q)uit")).lower()
    if(action == 'g'): display_guests(get_guests())
    elif(action == 'c'): 
        if (get_majority_color(get_guests()) == 'blue'): print("People think you are having a boy.")
        elif (get_majority_color(get_guests()) == 'pink'): print("People think you are having a girl.")
        elif (get_majority_color(get_guests()) == 'even'): print("It's a tie.")
    elif(action == 'q'): 
        print("Goodbye")
        break
    else: print("Invalid input.")