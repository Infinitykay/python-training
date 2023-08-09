# list, tuples, sets and dictionary in python

# strings, ints, floats and bools
"""
  -> lists are orderable
  -> lists are arbitrary i.e can contain any datatypes
  -> List elements can be accessed by index.

"""

fruits = ["Banana", "Apple", "Pawpaw", "Orange"]
scores = [32, 40, 34, 90]
validity = [True, False, False, True]
student_bio = ["Bukunmi", 40, True, 90.4]

print(type(fruits))
print(type(fruits[1]))


# print(fruits[2])
# print(scores[3])
# print(validity)
# print(student_bio)

# -> list are mutable

fruits = [
  "Orange", "Apple", "Cucumber", "Pineapple", "Mango", "Watermelon", "Grape"
]

# list slicing
print(fruits[3:5])

# list modification
fruits[-1] = "Banana"

# used to add to our list
fruits.append("Pawpaw")  # append can only add one item to our list
# extending a list
fruits += ["Coconut", "Currant"]
fruits.extend(['Tomato', 'Avocado'])

fruits.insert(0, "Kiwi")  # used to add new item to any position on the list

# removing from a list
fruits.remove("Currant")

fruits.pop(0)

print(fruits)
