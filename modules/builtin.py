# modules and packages

import time
import datetime
import math
import os

from datetime import timedelta, datetime, date


today = datetime.today()
day3 = timedelta(3)

date = datetime.isoweekday(today + day3)

print(date)

twnety_days_later = today + timedelta(20)
print(twnety_days_later)

# date = datetime.date()
random_date = datetime.datetime(2023, 10, 3, 1, 34, 22)

days_ahead = datetime.timedelta(25)

# days_ahead = 25

new_date = random_date + days_ahead
print(new_date)

# print(math.factorial(5))

# print(math.pow(4, 3))
# print(math.sqrt(16))
