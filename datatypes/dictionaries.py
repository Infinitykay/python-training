# Dictionaries

# fruits = ["Apple", "Orange", "Banana"]
# names = ("Dele", "Daniel", "Datwyne", "Favour")

# items = [fruits, names]

# # print(items[0])

# item_dict = {
#   "a": fruits,
#   "b": names,
#   "c": items
# }

# print(item_dict)

student_1 = ["Ola", 10, 6]
student_2 = ["Tola", 11, 7]
student_3 = ["Bola", 12, 9]
student_4 = ["Gbenga", 14, 9]

students_info = {
  "oau/123": ["Ola", 10, 6],
  "oau/991": ["Tola", 11, 7],
  3: ["Bola", 12, 9],
  4: ["Gbenga", 14, 9]
}

# keys has to be unique
# dictionaries can be accessed by keys
# dictionaries can be modified

print(students_info[4])

students_info[4] = ["Seun", 23, 12]

print(students_info[4])

# Dictionaries

groceries = {}

print(groceries)

groceries["cereals"] = ["Corn Flakes", "Golden Morn"]

print(groceries)
groceries["cereal"] = ["Flakes", "Morn"]
print(groceries)
groceries["food"] = ["Yam", "Wheat", "Chicken"]
groceries["drinks"] = ["Beer", "Soda", "Juice"]
print(groceries)

# Dictionaries

groceries = {}

# print(groceries)

groceries["cereals"] = ["Corn Flakes", "Golden Morn"]

# print(groceries)
groceries["cereal"] = ["Flakes", "Morn"]
# print(groceries)
groceries["food"] = ["Yam", "Wheat", "Chicken"]
groceries["drinks"] = ["Beer", "Soda", "Juice"]
groceries[True] = ["Available"]
# print(groceries)

# print("food" in groceries)

# clear removes everything about the dictionary
# groceries = groceries.clear()
# print(groceries)


# print(groceries['foods'])
# get item from dictionaries
print(groceries.get('drink', 'Not available'))

print(len(groceries))

