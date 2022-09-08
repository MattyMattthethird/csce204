month = input("Enter your birth month: ")
day = int(input("Enter your birth day: "))

sign = ""
stone = ""

if month == "january":
    if day > 19:
        sign = "Aquarius"
    else: sign = "Capricorn"
elif month == "february":
    if day > 18:
        sign = "Pisces"
    else: sign = "Aquarius"
elif month == "march":
    if day > 20:
        sign = "Aries"
    else: sign = "Pisces"
elif month == "april":
    if day > 19:
        sign = "Taurus"
    else: sign = "Aries"
elif month == "may":
    if day > 20:
        sign = "Gemini"
    else : sign = "Taurus"
elif month == "june":
    if day > 20:
        sign = "Cancer"
    else: sign = "Gemini"
elif month == "july":
    if day > 22:
        sign = "Leo"
    else: sign = "Cancer"
elif month == "august":
    if day > 22:
        sign = "Virgo"
    else: sign = "Leo"
elif month == "september":
    if day > 22:
        sign = "Libra"
    else: sign = "Virgo"
elif month == "october":
    if day > 22:
        sign = "Scorpio"
    else: sign = "Libra"
elif month == "november":
    if day > 21:
        sign = "Sagittarius"
    else: sign = "Scorpio"
elif month == "december":
    if day > 21:
        sign = "Capricorn"
    else: sign = "Saggitarius"

if month == "january":
    if day > 21:
        stone = "Garnet"
    else: stone = "Ruby"
elif month == "february":
    if day > 21:
        stone = "Amethyst"
    else: stone = "Garnet"
elif month == "march":
    if day > 21:
        stone = "Bloodstone"
    else: stone = "Amethyst"
elif month == "april":
    if day > 20:
        stone = "Sapphire"
    else: stone = "Bloodstone"
elif month == "may":
    if day > 21:
        stone = "Agate"
    else : stone = "Sapphire"
elif month == "june":
    if day > 21:
        stone = "Emerald"
    else: stone = "Agate"
elif month == "july":
    if day > 22:
        stone = "Onyx"
    else: stone = "Emerald"
elif month == "august":
    if day > 22:
        stone = "Carnelian"
    else: stone = "Onyx"
elif month == "september":
    if day > 22:
        stone = "Peridot"
    else: stone = "Carnelian"
elif month == "october":
    if day > 22:
        stone = "Aquamarine"
    else: stone = "Peridot"
elif month == "november":
    if day > 21:
        stone = "Topaz"
    else: stone = "Aquamarine"
elif month == "december":
    if day > 21:
        stone = "Ruby"
    else: stone = "Topaz"

print("Your astrology sign is: ", sign)
print("Your astrology stone is: ", stone)