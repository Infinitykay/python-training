# Modifying Lists:
fruits = ["Banana", "Apple", "Pawpaw", "Orange"]

# Add a new fruit to the end of the list.
fruits.append("Mango")

# Change the first fruit in the list to another fruit.
fruits[0] = "Grape"

# Remove the third fruit from the list.
fruits.remove("Pawpaw")

# List Operations:

# Create a second list with some more fruits.
fruits2 = ["Coconut", "Pineapple", "Kiwi"]

# Concatenate the two lists to form a single list.
fruits = fruits + fruits2
print(fruits)

# Find the length of the combined list.
print(len(fruits))