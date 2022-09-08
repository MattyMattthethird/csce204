print("You just got pulled over!")
speed = float(input("Enter your speed: "))

if speed > 90:
    print("Jail Time")
elif speed > 80:
    print("You get a ticket.")
elif speed > 70:
    print("You get a warning.")
elif speed > 45: 
    print("Good driving")
elif speed >= 25: 
    print("You get a ticket")
elif speed >= 1: 
    print("Jail: Drugs")
    