import sys
from strope import change_capitalise, change_lower, change_title, change_upper

platform = sys.platform
# print(platform)

if platform == "win32":
    print("""
This code will change your input . 
          Enter c to capialize, 
          l to change to lowercase,
          t to change to title or 
          u to change to uppercase
""")
    sentence = input("Enter your sentence:    ")
    operation =input("Enter an operation.    ")
    if operation.lower() == "c":
        new_sentence = change_capitalise(sentence)
        print(new_sentence)  
    elif operation.lower() == "l":
        new_sentence = change_lower(sentence)
        print(new_sentence) 
    elif operation.lower() == "t":
        new_sentence = change_title(sentence)
        print(new_sentence)
    elif operation.lower() == "u":
        new_sentence = change_upper
        print(new_sentence)
    else:
        print("Operation error.  ")
else:
    print("This application is available in win32 only.")

import calculator as calc

try:
  import calculators as calc
except ModuleNotFoundError:
  print("Module Not found")

def calculator():
  print("This is a calculator")  

calculator()

total = calc.get_sum(12, 13)

print(total)

import calculator as calc

try:
  import calculators as calc
except ModuleNotFoundError:
  print("Module Not found")

def calculator():
  print("This is a calculator")  

calculator()

total = calc.get_sum(12, 13)

print(total)
    
    