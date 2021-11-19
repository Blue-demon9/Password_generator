import random

def generate(ch,l=8):
    password = ""
    while len(password) < l:
        password += random.choice(ch)
    print(password)

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
number = "123456789"
special_char = "!@#$%&?"
ran = list(upper+lower+number+special_char)
length = int(input("Enter the length of password you want (min 8): "))

generate(ran,length)