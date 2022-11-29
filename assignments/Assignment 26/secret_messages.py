
def encode(message):

    ret = ""
    
    for c in range(0, len(message)):
        if (encode_map.get(message[c]) != None):
            ret += encode_map.get(message[c])
        else:
            ret += message[c]
    return ret


def to_letters(symbols):

    ret = ""
    
    for c in range(0, len(symbols)):
        if (decode_map.get(symbols[c]) != None):
            ret += decode_map.get(symbols[c])
        else:
            ret += symbols[c]
    return ret

encode_map = {
    "a" : "e",
    "b" : "a",
    "c" : "f",
    "d" : "n",
    "e" : "c",
    "f" : "r",
    "g" : "i",
    "h" : "g",
    "i" : "h",
    "j" : "b",
    "k" : "p",
    "l" : "m",
    "m" : "q",
    "n" : "s",
    "o" : "l",
    "p" : "j",
    "q" : "o",
    "r" : "d",
    "s" : "k",
    "t" : "y",
    "u" : "w",
    "v" : "x",
    "w" : "t",
    "x" : "v",
    "y" : "z",
    "z" : "u"
}

print("Secret Messages!!!")


decode_map = { encode_map[k] : k for k in encode_map}


while(True):

    
    action = str(input("(E)ncode, (D)ecode, or (Q)uit: ")).lower()
    
    
    if(action == 'q'):
        break
    elif (action == 'e'): 

        
        message = str(input("Enter a secret message: ")).lower()
        print("Your encoded message is: ",encode(message))
    elif (action == 'd'): 

        
        symbols = str(input("Enter an encoded meassage: ")).lower()
        print("Your decoded message is: ",to_letters(symbols))