def read_assignments():
    ret = {}
    file = open("jobs.txt", "r")
    length = len(file.readlines())
    file = open("jobs.txt", "r")
    for i in range(length):
        line = file.readline().split(':')
        ret[line[0]] =  line[1].strip()
    file.close()
    return ret

def list_assignments(assignments):
    for item in assignments:
        print(item, ":", assignments[item])

def write_assignments(assignments):
    file = open("jobs.txt", 'w')
    for item in assignments:
        file.write(item + ":" + assignments[item]+"\n")

def add_assignment(assignments):
    job = str(input("Enter Job: ")).lower()
    if job in assignments:
        student = str(input("Enter Student: ")).lower()
        assignments[job] = student
        write_assignments(assignments)
    else:
        print("Sorry, we could not find the job ", job)


while(True):
    action = str(input("Enter (L)ist, (A)ssign Student, or (Q)uit: ")).lower()
    if(action == 'l'):
        list_assignments(read_assignments())
    elif(action == 'a'):
        add_assignment(read_assignments())
    elif(action == 'q'):
        break
    else:
        print("Invalid input.")