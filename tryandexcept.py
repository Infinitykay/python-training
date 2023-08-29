# try and except

while True:
  try:
    balance = float(input("Enter your balance here : "))
    # age = int(input("Enter your age in years: "))
    print(f"Your balance is {balance}")
    break
  except:
    print('Your input is not float. it should be of type float')

    while True:
  try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator here: "))
    result = float(numerator / denominator)
    print(f"The decimal value is {result}")
    break
  except ValueError:
    print("Invalid Input")
  except ZeroDivisionError:
    print("Cannot divide by zero")

def get_sum(a, b):
  total = a + b
  print(f"{a} plus {b} is {total}")

boolean = True
while boolean:
  try:
    print("This is a simple caculation, a for addition, s for subtracion, d for division and m for multiplication")
    first_num = int(input("Enter a number"))
    operation = input("What operation do you want to perform?")
    second_num =int(input("Enter a number"))
    if operation == "a":
      get_sum(first_num, second_num)
    elif operation == "s":
      get_sum(first_num, second_num)
      total = first_num - second_num
      print(f"{first_num} minus {second_num} is {total}")
    elif operation == "m":
      total = first_num * second_num
      print(f"{first_num} times {second_num} is {total}")
    elif operation == "d":
      total = first_num / second_num
      print(f"{first_num} divided by {second_num} is {total}")
    else:
      print("There is an error in this operation")
    prompt = ("Do you wish to continue the operation? y/n")
    if prompt == "y":
      continue
    else:
      break  
  except ValueError:
       print("Invalid Input")
