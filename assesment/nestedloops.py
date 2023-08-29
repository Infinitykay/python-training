# nested_list

# ages = [12, 34, 22, 99, 32]
# names = ["Bello", "Bukunmi", "Adewale", "Tolu"]
# city = ["Lagos", "Imo", "Akure", "Ibadan"]
# heights = [7.0, 8.8, 9.0, 9.9]

# fruits = ["Mango", "Cherry", "Orange", "Plum"]

# heights_dict = {index: heights for index, heights in enumerate(heights)}
# print(heights_dict)

# zip, enumerate, nested for loops

# fruits = sorted(fruits, reverse=True)
# print(fruits)
# fruits = sorted(fruits)[::-1]
# print(fruits)

# for i in ages:
#   print(i)
#   for a in names:
#     print(a)
#     for c in city:
#       print(c)

# for age, name in zip(ages, sorted(names)):
#   print(age, name)


# for index, fruit in enumerate(names):
#   student_id = index + 1 
#   print(student_id, fruit)

# for index, (name, height) in enumerate(zip(names, heights)):
#   student_id = index + 1
#   print(student_id, name, height)

# # names reversed cityt sorted

# for index, (names, city) in enumerate(zip(sorted(names)[::-1], sorted(city))):
#   print(index, names, city )


words = ["apple", "banana", "cherry", "tomato"]

 # Dictionary comprehension
# word_dict = {index: word for index, word in enumerate(words)}
# print(word_dict)

names = ["Mary", "Sandra", "David", "Kane"]
city = ["Lagos", "Abuja", "Imo", "Ondo"]
for index, (names, city) in enumerate(zip(names, city)):
   print(names, city )