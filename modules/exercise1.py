# Exercise 1: Current Date and Time
# Write a program that prints the current date and time.
import datetime
from datetime import datetime, date
today = datetime.today()
# print(today)

# Exercise 2: Formatting Dates
# Write a program that prints the current date in the format "YYYY-MM-DD".

today_date = today.date()
# print(today_date)

#  Exercise 3: Formatting Times
# Write a program that prints the current time in the format "HH:MM:SS".
current_time = today.time()
# print(current_time)

# Exercise 4: Calculate Age
# Write a program that takes a birth year as input and calculates the user's age.
# def calculate_age(birth_year):
#     current_year = datetime.today().year
#     age = current_year - birth_year
#     return age

# try:
#     birth_year = int(input("What year were you born?"))
#     age = calculate_age(birth_year)
#     print(f"You are {age} years old. ")
# except:
#     print("Please enter a valid year. (integer)")   

# Exercise 5: Calculate Time Difference
# Write a program that calculates the time difference between two given dates and prints the result in days, hours, and minutes. 

# from datetime import datetime, date, time
# y = int(input("Enter a year-     "))
# m = int(input("Enter a month-    "))
# d = int(input("Enter a day-     "))
# random_date = datetime(y, m, d)
# print(f"Your first date is   {random_date}   ")

# y = int(input("Enter a year-     "))
# m = int(input("Enter a month-    "))
# d = int(input("Enter a day-     "))
# print(f"Your second date is   {random_date}   ")

# random_date2 = datetime(y, m, d)
# diff = random_date2 - random_date


# print(f"The difference is {diff} / {hours}hrs / {minutes}mins")

# Write a program that calculates the date that is 100 days from the current date and prints it.
from datetime import timedelta

today = datetime.today()
in100days = today + timedelta(100)
print(in100days)

# Write a program that takes a date as input and prints the corresponding day of the week.

y = int(input("Enter a year-     "))
m = int(input("Enter a month-    "))
d = int(input("Enter a day-     "))
date = datetime(y, m, d)
dayofweek = date.isoweekday()
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(f'The day of the week for {date} is {days[dayofweek]}')


