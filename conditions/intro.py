# Conditional statements.

# username = input("Enter Your username: ")

# if username.startswith('a') == True:
#   print("You are an A star")
# else:
#   print("Not an a star artist")

# if username.lower() == "admin":
#   print(f"Welcome {username} to the admin dashboard")
# else:
#   print(f"Welcome {username} to the user dashboard")

# Exercise 1: Even or Odd
# Check if a given number is even or odd.
# print("Enter any number and we will check if it's an even number or not")
# number = int(input("Enter Number here: "))

# if number % 2 == 0:
#   print(f"{number} is an even number")
# else:
#   print(f"{number} is an odd number")

# Exercise 2: Positive/Negative/Zero
# Determine if a number is positive, negative, or zero.

# print("Enter any number and we will check if it's positive, negative or zero")
# figure = float(input("Enter number here"))

# if figure > 0:
#   print(f"{figure} is positive")
# elif figure < 0:
#   print(f"{figure} is a negative number")
# else:
#   print(f'{figure} is neither positive nor negative')


# Exercise 4: Grade Classifier
# Classify a student's grade based on a given score.
# above 90 Excellent
# 89-70 Very Good
# 69-55 Good
# 54-45 Fair
# below 45 Poor

grade_score = int(input("Enter whole number value of your grade here: "))

if grade_score >= 90:
  print("Excellent")
  print("You are an exceptional student")
elif grade_score < 90 and grade_score >= 70:
  print("Very Good")
  print("This is a very good score. not excellent though")
elif grade_score < 70 and grade_score >= 55:
  print("Good")
  print("This is a good grade")
elif grade_score < 55 and grade_score >= 45:
  print("Fair")
  print("This is a fair grade. You can do better")
elif grade_score < 45 and grade_score >= 0: 
  print("This is a poor score")
elif grade_score < 0:
  print("Grade score can not be less than 0")
else:
  print("Grade Score can not be greater than 100")