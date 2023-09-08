# Exercise 1: Squares of Numbers
# Create a list comprehension that generates a list of the squares of numbers from 1 to 10.

square_val = [i ** 2 for i in range(11)]

print(square_val)

# Exercise 2: Even Numbers
# Write a list comprehension to create a list of all even numbers from 1 to 20.
even = [i for i in range(21) if i % 2 == 0]
print(even)
# Exercise 3: Words Longer than 5 Characters
# Given a list of words, create a new list using a list comprehension that contains only the words that have more than 5 characters.
words = ["Goat", "Envelop", "Google", "Elephant", "fine", "Police", "Age"]
five_words = [i for i in words if len(i) > 5]
print(five_words)

# Exercise 4: Uppercase Conversion
# Given a list of words, create a new list using a list comprehension where all the words are converted to uppercase.
words = ["Adekule", "Adebayo", "Ogunsanwo", "Agemo"]
upper_case = [i.upper() for i in words  ]
print(upper_case)

# Exercise 5: Vowels in a Sentence
# Write a list comprehension to extract all the vowels (a, e, i, o, u) from a given sentence.
sentence = input("Enter any sentence of your choice: ")
vowel_list = [i for i in sentence if i in "aeiouAEIOU"]
print(vowel_list)

# Exercise 6: List of Squares for Even Numbers
# Create a list comprehension that generates a list of squares for even numbers between 1 and 15. For odd numbers, the list should contain the number itself.
number = [i ** 2 if i % 2 == 0 else i for i in range(1,16)]

print(number)

number = [i ** 2 if i% 2 == 0 else i ** 3 for i in range(1, 16)]
print(number)
# Exercise 7: Filtering Prime Numbers
# Generate a list of prime numbers between 1 and 50 using a list comprehension. You may need to write a helper function to check for prime numbers.
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


# Exercise 8: Flatten a 2D List
# Given a 2D list (a list of lists), create a list comprehension to flatten it into a single list.

# Exercise 9: Pairwise Multiplication
# Given two lists of equal length, create a list comprehension to generate a new list where each element is the product of the corresponding elements from the two input lists. For example, if you have [1, 2, 3] and [4, 5, 6], the result should be [4, 10, 18].

list1 = [10, 11, 12, 13]
list2 = [2, 3, 4, 5]

big_list = [a * b for a, b in zip(list1, list2)]

print(big_list)

# Exercise 10: Non-Negative Numbers
# Given a list of numbers, create a list comprehension that generates a new list containing only the non-negative numbers (greater than or equal to 0).

numbers = [2, 3, 56, 3, -5, 4,-8]
generate = [i for i in numbers if i >= 0]
print(generate)

