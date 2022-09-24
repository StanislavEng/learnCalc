import os
from math import *

def add_func(a,b):
    return a + b

def sub_func(a,b):
    return a - b

def mult_func(a,b):
    return a * b

def div_func(a,b):
    return a / b

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
        x, y = input("Enter two numbers to add: ").split()
        z = add_func(float(x),float(y))
    if user == 2:
        x, y = input("Enter two numbers to substract: ").split()
        z = sub_func(float(x),float(y))
    if user == 3:
        x, y = input("Enter two numbers to multiply: ").split()
        z = mult_func(float(x),float(y))
    if user == 4:
        x, y = input("Enter two numbers to divide: ").split()
        z = div_func(float(x),float(y))    











