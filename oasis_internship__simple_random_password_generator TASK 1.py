# -*- coding: utf-8 -*-
"""OASIS INTERNSHIP->Simple Random Password Generator.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11ZwvxSRT-B5xwRAu9HB8qfw3nUxh1XMY
"""



"""**AICTE OASIS INFOBYTE SIP TASK-  Simple Random Password Generator**"""

import string
import random

if __name__ == "__main__":
    string1 = string.ascii_lowercase
    # print(s1)
    string2 = string.ascii_uppercase
    # print(s2)
    string3 = string.digits
    # print(s3)
    string4 = string.punctuation
    # print(s4)
    passwordlen = int(input("Enter password length:- \n"))
    s = []
    s.extend(list(string1))
    s.extend(list(string2))
    s.extend(list(string3))
    s.extend(list(string4))
    # print(s)
    # random.shuffle(s)
    # print(s)
    print("Your password is:- ")
    print("".join(random.sample(s, passwordlen)))
    # print("".join(s[0:plen]))





#Todo1: Handle Gibberish