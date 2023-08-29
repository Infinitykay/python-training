sentence = "This is a sample sentence with vowels"
vowels = "aeiouAEIOU"

vowel_list = []

for i in sentence:
  if i in vowels:
    # print(f'{i} is a vowel')
    vowel_list.append(i)

# print(vowel_list)

# list comprehension 
consonant_list = [char for char in sentence if char not in vowels and char != " "]
# print(consonant_list)

names = ["Adekunle", "Opeyemi", "Felix", "Kayode", "Gbenga", "Yetunde", "Demola", "Tomiwa", "Martins", "Sarah", "Precious", "Kelly"]

# filtered_names = [name for name in names if "k" not in name.lower()]
# print(filtered_names)

filtered_names = [name for name in names if "a" in name.lower()]
print(filtered_names)