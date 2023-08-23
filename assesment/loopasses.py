# Exercise 1: Counting
# Write a program that uses a while loop to print the numbers from 1 to 10.

# Write a program that generates a random number between 1 and 100, and then asks the user to guess the number. The program should provide feedback (too high, too low) and allow the user to keep guessing until they guess the correct number.
# secret = True
# while secret:
#   secret_number = 55
#   guess = int(input('Guess the magic number===>'))
#   if guess < secret_number:
#     print(f'{guess} too low and is not the magic number')
#   elif guess > secret_number:
#     print(f'{guess} too high and is not the magic number')
#   elif guess == secret_number:
#     print(f'{guess} is the right number, You are amazing!')
#     break
#   else:
#     print("Your entry is invalid")
#   prompt = input("Do you wish to continue? y/n: ")
#   if prompt.lower() == "y":
#     continue
#   else:
#     secret = False
# else:
#   print("Thanks for using our guess machine")

# Exercise 5: Factorial
# Write a program that calculates the factorial of a given number using a while loop. The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
total = 1
factor = int(input("Enter a number and we will give the factorial"))
n = factor
while n >= 1:
  total *= n
  n -= 1
print(f'The factorial value of {factor} is {total}')

# Exercise 6: Reversing Digits
# Write a program that takes an integer as input and prints its digits in reverse order using a while loop.
# value = True
# while value:
#   integer = int(input("Enter a number here ---> "))
#   integer = str(integer)
#   rev_integer = integer[::-1]
#   print(rev_integer)
#   prompt = input("Do you wish to continue? y/n: ")
#   if prompt.lower() == "y":
#     continue
#   else:
#     value = False
# else:
#   print("Thanks for using our rev input")
    
# Exercise 7: Power Calculation
# Write a program that calculates the result of a number raised to an exponent using a while loop. For example, given 2 and 3 as inputs, the program should calculate and print 2^3 = 8.

# Exercise 8: Number Palindrome
# Write a program that checks if a given number is a palindrome. A palindrome is a number that remains the same when its digits are reversed. Use a while loop to reverse the digits of the number and compare it with the original number.
# iter = True
# while iter:
#   int_input = int(input("Enter a number here to check if it's a palindrome ===> "))
#   int_input = str(int_input)
#   rev_int = int_input[::-1]
#   if rev_int == int_input:
#     print(f'{int_input} is a palindrome')
#   else:
#     print(f'{int_input} is not a palindrome')
#   prompt = input("Do you wish to continue? y/n: ")
#   if prompt.lower() == "y":
#     continue
#   else:
#     iter = False
# else:
#   print("Thanks for using our palindrome function")

  
# Exercise 9: Multiplication Table
# Write a program that takes an integer as input and prints its multiplication table (from 1 to 10) using a while loop.

# Exercise 10: Fibonacci Sequence
# Write a program that generates and prints the first 10 numbers in the Fibonacci sequence using a while loop. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones.
# Write a program that generates a random number between 1 and 100, and then asks the user to guess the number. The program should provide feedback (too high, too low) and allow the user to keep guessing until they guess the correct number.
secret = True
while secret:
  secret_number = 55
  guess = int(input('Guess the magic number===>'))
  if guess < secret_number:
    print(f'{guess} too low and is not the magic number')
  elif guess > secret_number:
    print(f'{guess} too high and is not the magic number')
  elif guess == secret_number:
    print(f'{guess} is the right number, You are amazing!')
    break
  else:
    print("Your entry is invalid")
  prompt = input("Do you wish to continue? y/n: ")
  if prompt.lower() == "y":
    continue
  else:
    secret = False
else:
  print("Thanks for using our guess machine")

# Write a program that calculates the factorial of a given number using a while loop. The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
total = 1
factor = int(input("Enter a number and we will give the factorial"))
n = factor
while n >= 1:
  total *= n
  n -= 1
print(f'The factorial value of {factor} is {total}')

# Exercise 6: Reversing Digits
# Write a program that takes an integer as input and prints its digits in reverse order using a while loop.
value = True
while value:
  integer = int(input("Enter a number here ---> "))
  integer = str(integer)
  rev_integer = integer[::-1]
  print(rev_integer)
  prompt = input("Do you wish to continue? y/n: ")
  if prompt.lower() == "y":
    continue
  else:
    value = False
else:
  print("Thanks for using our rev input")

# Exercise 8: Number Palindrome
# Write a program that checks if a given number is a palindrome. A palindrome is a number that remains the same when its digits are reversed. Use a while loop to reverse the digits of the number and compare it with the original number.
iter = True
while iter:
  int_input = int(input("Enter a number here to check if it's a palindrome ===> "))
  int_input = str(int_input)
  rev_int = int_input[::-1]
  if rev_int == int_input:
    print(f'{int_input} is a palindrome')
  else:
    print(f'{int_input} is not a palindrome')
  prompt = input("Do you wish to continue? y/n: ")
  if prompt.lower() == "y":
    continue
  else:
    iter = False
else:
  print("Thanks for using our palindrome function")

# Exercise 7: Power Calculation
# Write a program that calculates the result of a number raised to an exponent using a while loop. For example, given 2 and 3 as inputs, the program should calculate and print 2^3 = 8.

print("This code calculates the provided exponent value of a number")
n = True
while n:
  user_number = int(input("Enter a number: "))
  expo = int(input("Enter preferred exponent value: ")) 
  total = user_number ** expo
  print(total)
  prompt = input("Do you want to continue. y/n: ")
  if prompt.lower() == "y":
    continue
  else:
    n = False
else:
  print("Thank you for using the exponent machine")

# Exercise 9: Multiplication Table
# Write a program that takes an integer as input and prints its multiplication table (from 1 to 10) using a while loop.
print("This program is a multiplication table using while loop.")
num = int(input("Enter a number here: "))


# Exercise 1:
# Print the numbers from 1 to 10 using a for loop.
# for i in range(1, 11):
#   print(i)
temp_num = 1
a = True
while a:
  total = num * temp_num
  temp_num += 1
  print(total)
  if temp_num == 13:
    a = False
  else:
    continue

# Exercise 2:
# Print the even numbers from 1 to 20 using a for loop.
print("This Program prints the even number out for a range of numbers by a user")
start_input = int(input("Enter the start range (integer only): "))
end_input = int(input("Enter the end range (integer only): "))
for i in range(start_input, end_input+1):
  if i % 2 == 0:
    print(i)
  else:
    continue

# Exercise 3:
# Calculate and print the sum of numbers from 1 to 50 using a for loop.

total = 0

for i in range(1, 51):
  total += i

print(f'the total sum of numbers between 1 and 50 is {total}')


# Exercise 4:
# Print the multiplication table of a number (e.g., 5) using a for loop.
digit = int(input("Enter a number here : "))
for i in range(1, 13):
  value = i * digit
  print(f'{digit} * {i} is {value}')

# Exercise 6:
# Print the squares of numbers from 1 to 15 using a for loop.
for i in range(1, 16):
  value = i ** 2
  print(f"The square of {i} is {value}")

# Exercise 6:
# create a function that prints the exponent of numbers from the user start range and end range using a for loop.
def get_exponent_range(start, end, expo):
  for i in range(start, end + 1):
    value = i**expo
    print(f"The result of {i}  exponent {expo} is {value}")


start_input = int(input("Enter your start number: "))
end_input = int(input("Enter your end number: "))
expo = int(input("Enter an exponent number: "))
get_exponent_range(start_input, end_input, expo)

# Exercise 7:
# Given a list of numbers, calculate and print the average using a for loop.


numbers = [2, 5, 8, 6, 5, 9, 6, 7, 6]
total = 0
for i in numbers:
  total += i

average = total / len(numbers)
print(f'The mean average of {numbers}  is {average}')