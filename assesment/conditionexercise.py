# Exercise 6: Vowel or Consonant
# Determine if a given letter is a vowel or a consonant.

# hint: use in operator

# letter= str(input("Enter a letter"))
# if letter in "aeiouAEIOU":
#   print (f"{letter} is a vowel")
# else:
#   print(f"{letter} is a consonant")


# Exercise 7: Largest of Three Numbers
# Find the largest of three input numbers.

# num_list = input('Enter Bunch of numbers: ')

# print(f"The largest number in {num_list} is {max(num_list)}")

# Exercise 8: Age Group
# Categorize a person's age into different groups (e.g., child, teenager, adult).

age = int(input("How old are you?"))
if age >= 19:
  print("You are an adult")
elif age >= 13 and age <= 18:
  print("You are a teenager")
else:
  print("You are a child")

# Exercise 6: Vowel or Consonant
# Determine if a given letter is a vowel or a consonant.

# hint: use in operator

# letter= str(input("Enter a letter"))
# if letter in "aeiouAEIOU":
#   print (f"{letter} is a vowel")
# else:
#   print(f"{letter} is a consonant")


# Exercise 7: Largest of Three Numbers
# Find the largest of three input numbers.

# num_list = input('Enter Bunch of numbers: ')

# print(f"The largest number in {num_list} is {max(num_list)}")

# Exercise 8: Age Group
# Categorize a person's age into different groups (e.g., child, teenager, adult).

age = int(input("How old are you?"))
if age >= 19:
  print("You are an adult")
elif age >= 13 and age <= 18:
  print("You are a teenager")
else:
  print("You are a child")

# Exercise 9: Calculator
# Create a simple calculator that performs addition, subtraction, multiplication, or division based on user input.

first_num = int(input("Enter a number"))
operation = input("What operation do you want to perform?")
second_num =int(input("Enter a number"))
if operation == "+":
  total = first_num + second_num
  print(f"{first_num} plus {second_num} is {total}")
elif operation == "-":
  total = first_num - second_num
  print(f"{first_num} minus {second_num} is {total}")
elif operation == "*":
  total = first_num * second_num
  print(f"{first_num} times {second_num} is {total}")
elif operation == "/":
  total = first_num / second_num
  print(f"{first_num} divided by {second_num} is {total}")
else:
  print("There is an error in this operation")