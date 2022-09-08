print("What to wear")
temp = float(input("Enter the temperature: "))
percip = input("Enter percipitation (r), (s), or (n): ").strip().lower()

if temp <= 32 and percip == "s":
    print("You should wear a snowsuit.")
elif temp <= 70 and percip == "r":
    print("Wear a rainjacket")
elif temp >= 80 and percip == "r":
    print("Wear a swimsuit")
else: 
    print("You choose")