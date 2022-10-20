def get mood(color):
    mood chart = {
        "red':"angry"
        "yellow":"mellow"
        "blue":"sad"
        "green":"happy"
        "black":"scary"
        "purple":"royal"
        "pink":"fun"
    }

    color = color.lower().strip()

    if color not in mood_chart:
        return "not moody"
    else: 
        return mood_chart[color]

print("Let's find your mood")

color = input ("Enter Color: ").lower().strip()
mood = get_mood(color)
print(f"You are feeling {mood}")

