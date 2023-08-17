# Exercise 1: Even or Odd Checker

# Write a function even_or_odd(number) that takes an integer as input and returns "Even" if the number is even, and "Odd" if the number is odd.

# num_input = int(input("Enter Your number here: "))

# def get_even_odd():
#   if num_input % 2 == 0:
#     print(f"{num_input} is an even number ")
#   else:
#     print(f'{num_input} is an odd number')

# get_even_odd()

# Exercise 2: Temperature Converter

# Write a function convert_temperature(temp, unit) that converts temperatures between Fahrenheit and Celsius. The function should take a temperature value and a unit ('F' for Fahrenheit, 'C' for Celsius) as inputs and return the converted temperature. If the unit is neither 'F' nor 'C', return "Invalid unit".

temp_input = float(input("Enter temperature Here --> "))
unit_input = input("Enter Unit f for Fahrenheit, c for celcius --> ")


def convert_temperature(temp, unit):
  if unit.lower() == "f":
    converted_temp = (temp - 32) * (5 / 9)
    print(f"{temp}{unit.lower()} converted value is {converted_temp} celsius")
  elif unit.capitalize() == "C":
    converted_temp = (temp * 9 / 5) + 32
    print(
      f"{temp}{unit.capitalize()} converted value is {converted_temp} Fahrenheit"
    )
  else:
    print(
      f"{temp} can not be converted because {unit} is not a recognized conversion value"
    )


convert_temperature(temp_input, unit_input)
# convert_temperature(99, 'f')
