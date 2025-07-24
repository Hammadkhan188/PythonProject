import random
import string
import sys
from random import choice

import pyperclip

my_password=[]
print("Random Password Generator")
pswd_lenght=int(input("Enter Password Length"))

if pswd_lenght<8 or pswd_lenght >20:
    print("Password minimun length is 8 maximum length is 20")
    sys.exit()

else :
    password_list= string.ascii_letters + string.digits + string.punctuation
    for a in range(pswd_lenght):
        my_password.append(random.choice(password_list))

        string_pswd = "".join(my_password)
        print(f"Generated Password: {string_pswd}")

        choice=input(f"do you want to copy {string_pswd}")
        if choice.lower() =="yes":
            pyperclip.copy(string_pswd)
            print("Password has been copie4d")
