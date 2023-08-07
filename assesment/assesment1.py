# write a function that takes user input and multiply the inputs by 2

# function = input("Enter your number")
# solution = (int(function) * 2)
# print(solution)

# write a function that takes user Birth year and print out their age. You are 20 years old
# function = input("What year were you born?")
# solution = (2023 - int(function))
# print(f'You are {solution} years old.')

# write a function that takes user balance and adds 200 to it as a bonus. Your initial balance is 10. you got 200 bonus and net balance is now 210

initial_balance = input("What is your account balance?")
bonus_add = 200 + float(initial_balance)
print(
  f'Your initial balance is ${initial_balance}. You got $200 bonus. Your net balance is now ${bonus_add}'
)