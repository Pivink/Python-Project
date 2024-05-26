import random
import string
def Uppercase(n):
    com=""
    uppercase = string.ascii_uppercase
    for i in range(n):
        com+=random.choice(uppercase)
    return com
def Lowercase(n):
    com=""
    lowercase = string.ascii_lowercase
    for i in range(n):
        com+=random.choice(lowercase)
    return com
def Symbol(n):
    com=""
    sign=["@","#","$","%","&"]
    for i in range(n):
        com+=random.choice(sign)
    return com
def Password(upper,lower,symbol):
    uppercase=Uppercase(upper)
    lowercare=Lowercase(lower)
    symbol=Symbol(symbol)
    password=uppercase+lowercare+symbol
    pass_list=list(password)
    random.shuffle(pass_list)
    password=''.join(pass_list)
    return password
print("---Generate the Password---")
uppercase=int(input("How many Uppercase: "))
lowercase=int(input("How many Lowercase: "))
symbol=int(input("How many Symbol: "))
password=Password(uppercase,lowercase,symbol)
print("Here's your password: ",password)