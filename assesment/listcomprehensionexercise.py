# Create a list of even numbers from 1 to 20 using a list comprehension.
# evens = [i for i in range(1, 51) if i % 2 == 0]
# print(evens)

# Given a string, create a list containing the uppercase version of each character in the string using a list comprehension.
# string = "This is a sample sentence with vowels"
# upper = [i.upper() for i in string]
# print(upper)

# Generate a list of prime numbers between 1 and 50 using a list comprehension.
def is_prime(number):
  if number == 2:
    return True
  elif number == 3:
    return True
  elif number == 5:
    return True
  elif number == 7:
    return True
  elif number % 2 != 0 and number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
    return True
  else:
    return False
prime = [i for i in range(2, 51) if is_prime(i)]

print(prime)

# Create a list containing the lengths of words in a sentence using a list comprehension.

sentence = "I am a boy"

sen_list = [len(i) for i in sentence.split()]
print(sen_list)