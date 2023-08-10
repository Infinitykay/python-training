# strings -> str

f_name = "Hakeem"
name = "Bukunmi"
l_name = 'Olashile'
l_name = 'Olashina' # modify/update our variable name
print(l_name)

sentence = "verily erily I say unto you"
print(sentence)
print(len(sentence))
print(type(sentence))
print(sentence.lower())
print(sentence.upper())
print(sentence.title())
print(sentence.capitalize())

sentence = "Ali goes to school"
sentence = "Hello I'm Adekunle, I sing and write."

# the in operator

print("Hello" in sentence)

# string can not be modified directly
# name = "Beffo"
# name[2:4] = "ll"

# print(name)

name = "Bukunmi"
# swapcase changes the case sensitivity for our strings
print(name.swapcase())

# count function to count the targetted char in a variable
print(sentence.count("!"))
