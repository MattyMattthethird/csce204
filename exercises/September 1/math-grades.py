print("Let's calculate your grade")
assignments = float(input("Assignments: "))
exercises = float(input("Exercises: "))
midterm = float(input("Midterm: "))
final = float(input("Final: "))
grade = assignments * .55 + exercises * .15 + midterm * .15 + final * .15

print(f"Your final grade is {round(grade, 1)}.")