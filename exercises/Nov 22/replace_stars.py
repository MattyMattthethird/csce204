# replaces all * with .
def replace_stars(phrase):
    temp = ""

    for let in phrase: 
        if let == "*":
            temp += "."
        else:
            temp += let

    return temp


sentence= "*a*b*c*d"
new_sentence = replace_stars(sentence)
print(new_sentence)