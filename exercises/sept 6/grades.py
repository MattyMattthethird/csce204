print("Grades")
homework = float(input("Homework: "))
assignments = float(input("Assignments: "))
midterm = float(input("Midterm: "))
final = float(input("Final: "))

grade = homework * .2 + assignments * .3 + midterm * .2 + final * .3 

print(f"You earned a{round(grade,1)}%. ")

if grade >= 89.5:
    print("A")
elif grade >= 79.5:
    print("B")
elif grade >= 69.5:
    print("C")
elif grade >= 60.5:
    print("D")
else: 
    print("You suck/F :(")

print("Goodbye")