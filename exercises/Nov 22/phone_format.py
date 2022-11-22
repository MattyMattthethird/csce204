# turn (803)-123-4567 into 803.123.4567
def update_phone(phone):
    result = ""

    for let in phone:
        if let=="(" or let == ")":
            continue
        elif let==".":
            result += "."
        elif result += let 


    return result


phone = update_phone("(803)-123-4567")
print(phone)