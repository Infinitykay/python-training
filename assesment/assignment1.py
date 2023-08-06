# Don't do this
# Substring Extraction: Write a program that takes a string and two indices as input. Print the substring that lies between the given indices.

# Concatenation Practice: Write a program that takes two strings as input and concatenates them to create a new string. Print the resulting string.
firstName = input("What is your firstname?")
lastName = input("What is your lastname?")
fullName = firstName + " " + lastName
print(f'Hello {fullName}.')

# String Length: Write a program that takes a string as input and prints the length of the string (number of characters).
firstName = input("What is your firstname?")
lastName = input("What is your lastname?")
fullName = {firstName + " " + lastName}
lenfullname = len(firstName + lastName)
print(lenfullname)

# Character Count: Create a program that takes a string as input and a character to search for. Count and print the number of occurrences of that character in the given string.
firstName = input("What is your firstname?")
lastName = input("What is your lastname?")
fullName = {firstName + " " + lastName}
fullNamestr = str(fullName)
searchfor = fullNamestr.count("b")
print(searchfor)

# Uppercase and Lowercase Conversion: Write a program that takes a string as input and prints it in all uppercase and all lowercase letters.
school = input("Where did you school?") 
print(f'I schooled at {school.upper()}')

school = input("Where did you school?") 
print(f'I schooled at {school.lower()}')

# Basic Input: Write a program that takes the user's name as input and then prints a personalized greeting.
username = input("Enter Your Username")
print(f'Welcome {username}, how can I help you today?')
