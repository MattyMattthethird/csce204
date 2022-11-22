import random

# pplante@uofsc.com username is pplante
def get_username(email):
    return email.split("@")[0]

def get_password(phrase):
    password = ""

    conversion = {
        "a" : "@"
        "b" : "8"
        }
    

    for letter in phrase: 
    if letter.lower() in conversions:
        password += conversions[letter.lower()]
    else: 
        password += letter

    return password + str(random.randint(0,100))


def maybe_capitalize(letter):
    if random .randint(0,1) == 0:
        return letter.lower()
    else:
        return letter.upper()
# main program
print("Login Program")
email = input("Enter Email: ")
username = get_username(email)
print(f"Username: {username}")

phrase = input("Enter Phrase: ")
password = get_password(phrase)
print(f"Password: {password}")