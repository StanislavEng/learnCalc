import os
from math import *

# def add_func(a,b):
def add_func():
    val = 0
    here = ''
    a = input("What is the first number? ")
    b = input("What is the second number? ")
    val = int(a)
    allNum = [b]
    while True:
        here = input("+ for more or = to end\n")
        if here == "=":
            break
        c = input("What is the next number? ")
        allNum.append(c)
    for x in allNum:
        val = val + int(x)
    return val

# def sub_func(a,b):
def sub_func():
    val = 0
    here = ''
    a = input("What is the first number? ")
    b = input("What is the second number? ")
    val = int(a)
    allNum = [b]
    while True:
        here = input("- for more or = to end\n")
        if here == "=":
            break
        c = input("What is the next number? ")
        allNum.append(c)
    for x in allNum:
        val = val - int(x)
    return val

# def mult_func(a,b):
def mult_func():
    val = 0
    here = ''
    a = input("What is the first number? ")
    b = input("What is the second number? ")
    val = int(a)
    allNum = [b]
    while True:
        here = input("x for more or = to end\n")
        if here == "=":
            break
        c = input("What is the next number? ")
        allNum.append(c)
    for x in allNum:
        val = val * int(x)
    return val

# def div_func(a,b):
def div_func():
    val = 0
    here = ''
    a = input("What is the first number? ")
    b = input("What is the second number? ")
    val = int(a)
    allNum = [b]
    while True:
        here = input("/ for more or = to end\n")
        if here == "=":
            break
        c = input("What is the next number? ")
        allNum.append(c)
    for x in allNum:
        val = val / int(x)
    return val

user = 0
options = ["addition", "subtraction", "multiplication", "division"]
start = 0

while user < 5:
    if(os.name =="posix"):
        _=os.system("clear")
    else: 
        _=os.system("cls") 

    if start == 0:
        start = 1
    else:
        print("The result of your " + options[user-1] + " was: ")
        print(z)
        print()

    print("Welcome to the Calculator App")
    print("What kind of calculation do\nyou want to perform?")
    user = int(input("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit\n"))
    print()

    if user == 1:
        # x, y = input("Enter two numbers to add: ").split()
        # z = add_func(float(x), float(y))
        z = add_func()
    if user == 2:
        # x, y = input("Enter two numbers to substract: ").split()
        # z = sub_func(float(x), float(y))
        z = sub_func()
    if user == 3:
        # x, y = input("Enter two numbers to multiply: ").split()
        # z = mult_func(float(x), float(y))
        z = mult_func()
    if user == 4:
        # x, y = input("Enter two numbers to divide: ").split()
        # z = div_func(float(x), float(y))    
        z = div_func()










