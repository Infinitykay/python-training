import sys
import calculator

if sys.platform == "win32":
  print(
    "This is a simple calculator app. a for addition, s for subtraction, m for multiplication, d for division, e for exponent, o for modulo"
  )
  input1 = int(input("Enter a number here:  "))
  input2 = int(input("Enter a number here:  "))
  operation = input("What operation would you like to perform? ")

  if operation.lower() == "a":
    total = calculator.get_sum(input1, input2)
    print(total)
  elif operation.lower() == "s":
    total = calculator.get_diff(input1, input2)
    print(total)
  elif operation.lower() == "m":
    total = calculator.get_multi(input1, input2)
    print(total)
  elif operation.lower() == "d":
    total = calculator.divide(input1, input2)
    print(total)
  elif operation.lower() == "e":
    total = calculator.get_exponent(input1, input2)
    print(total)
  elif operation.lower() == "o":
    total = calculator.get_modulo(input1, input2)
    print(total)
  else:
    print("You entered an invalid operation.")
else:
  raise Exception(
    f"{sys.platform} is not a linux operating system. Try to install on linux only"
  )
