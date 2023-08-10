
# List Length:
# Calculate and print the length of a list.

fruits = [
  "Banana", "Apple", "Pawpaw", "Orange", "Coconut", "Pineapple", "Kiwi",
  "Mango", "Grape", "Pawpaw"
]
print(len(fruits))

# Access Elements:
# Print the first and last element of a list.
print(fruits[::9])

# List Slicing:
# Print a sublist containing the 2nd to 4th elements of a list.
print(fruits[1:5])

# List Append:
# Append an item to the end of a list and print the updated list.
fruits.append("Cherry")
print(fruits)

# List Insert:
# Insert an item at a specific index in the list and print the updated list.
fruits.insert(4, "Watermelon")
print(fruits)
# List Remove:
# Remove a specific item from the list and print the updated list.
fruits.remove("Coconut")
print(fruits)
# List Pop:
# Remove and print the last item from the list using the pop() method.
fruits.pop(-1)
print(fruits)
# List Count:
# Count and print the occurrences of a specific element in the list.
print(fruits.count("Mango"))

# List Clear:
# Clear all the elements from the list and print the empty list.
fruits_empty = fruits

fruits_empty = []
print(fruits_empty)

# List Copy:
# Create a copy of a list and print both the original and copied lists.
copied_fruits = fruits
print(copied_fruits)

print(fruits)

# List Concatenation:
# Create two lists and concatenate them to form a new list. Print the new list.
fruit1 = fruits[:5] 
fruit2 = fruits[6:]
fruits = fruit1 + fruit2
print(fruit1)
print(fruit2)
print(fruits)

# List Reverse:
# Reverse the order of elements in a list and print the reversed list.
print(fruits[::-1])


# List Sorting:
# Sort a list in ascending order and print the sorted list.

fruits = sorted(fruits, reverse=True)

print(fruits)

# List Max and Min:
# Find and print the maximum and minimum values in a list.

print(max(fruits))
print(min(fruits))

# List Index:
# Find and print the index of a specific element in the list.
print("Pawpaw" in fruits)
print(fruits.index('Pawpaw'))

# List Join:
# Convert a list of strings into a single string by joining the elements with a specific delimiter.

sentence_list = ["I", "am", "a", "boy"]

sentence_str = ' '.join(sentence_list)
print(sentence_str)

