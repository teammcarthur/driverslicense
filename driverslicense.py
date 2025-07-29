'''
Author: Chris 
Date: 29/07/25
Version: 1.0
Description: This is a program to check if you are eligible for your restricted license
'''
import random
while(True):
    name = input("Enter your name: ")
    if name.isalpha():
        break
    else:
        print("This is an invalid name, please try again.")
        continue
while(True):
    age = input("Enter your age: ")
    if age.isnumeric == True:
        break
    else:
        print("Invalid age, please try again")
        continue
learners = int( input("How many months have you had your learners licsense for?: "))
if age < 16.5 or learners < 6:
    print(f"Sorry {name}, you cannot get a restricted drivers license")
else:
    print(f"Congratulations {name}, you can get a restricted drivers license")
