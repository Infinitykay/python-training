# Exercise 1:
# Write a program that takes a user's age as input. If the age is less than 18, print "You are a minor." Otherwise, print "You are an adult."

age = int(input("How old are you?"))
if age < 18:
  print("You are a minor")
else:
  print("You are an adult.")
# Exercise 2:
# Create a list of your favorite fruits. Write a program that checks if "banana" is in the list. If it is, print "Bananas are on the list!" Otherwise, print "No bananas found."
fruits = ["Orange", "Apple", "Cucumber", "Pineapple", "Mango", "Watermelon", "Grape"]
if "banana".title in fruits:
  print("Bananas are on the list")
else:
  print("No bananas found")


# Exercise 3:
# Write a program that asks the user to enter a number. If the number is even, print "The number is even." If it's odd, print "The number is odd."
num = int(input("Enter a number and it will be classified into even or odd"))
if num % 2 == 0:
  print(f"{num} is even")
else:
  print(f"{num} is odd")

# Exercise 4:
# Create a dictionary called student_info with keys "name", "age", and "grade". Write a program that checks if "grade" is a key in the dictionary. If it is, print "Grade information available." Otherwise, print "No grade information."
student_info = {
  'name': ["Esther", "Gideon", "Peter", "Yusuf", "Habeeb"],
  'age': [20, 23, 21, 22, 20],
  'grade': ["A", "B", "A", "C", "A"]
}
grade_input = input("Enter a Grade here: ")
if grade_input.upper() in student_info["grade"]:
  print("Grade information available")
else:
  print("No grade information")

# Exercise 5:
# Define a variable called temperature and set it to a numerical value. Write a program that uses an if statement to determine if the temperature is above 30. If it is, print "It's a hot day!" Otherwise, print "Enjoy the weather."
temp = int(input("What is the temperature?"))
if temp > 30:
  print("It's a hot day!")
else:
  print("Enjoy the weather.")

# Exercise 6:
# Write a program that asks the user to enter their favorite color. If the color is "blue", print "Great choice! Blue is a calming color." If it's "red", print "Red is a bold and energetic color." For any other color, print "Nice choice!"
color = input("What is your favorite color?")
if color.title() == "Blue":
  print("Great choice! Blue is a calming color.")
elif color.title() == "Red":
  print("Red is a old and energetic color.")
else:
  print("Nice choice")
  

# Exercise 7:
# Create a tuple called days_of_week containing the days of the week. Write a program that checks if "Sunday" is in the tuple. If it is, print "It's a weekend!" Otherwise, print "Back to work."
days_of_week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
if "Sunday" in days_of_week:
  print("It's a weekend!")
else:
  print("Back to work")

# Exercise 8:
# Define a string variable called password. Write a program that checks if the length of the password is at least 8 characters long. If it is, print "Password is strong." Otherwise, print "Password is too short."
password = input("Enter your password--->")
if len(password) >= 8:
  print("Password is strong")
else:
  print("Password is too short")

# Exercise 9:
# Write a program that takes two numbers as input and checks if the first number is greater than the second number. If it is, print "First number is larger." Otherwise, print "Second number is larger."
first_num = int(input("Enter a number."))
second_num = int(input("Enter another number."))
if first_num > second_num:
  print("First number is larger.")
else:
  print("second number is larger.")

# Exercise 10:
# Create a list of mixed data types including strings, numbers, and booleans. Write a program that iterates through the list and prints out the data type of each element.
mixed_list = ["Sing", 34, True]
print(type(mixed_list[0]))
print(type(mixed_list[1]))
print(type(mixed_list[2]))


