x = 12
y = 13
a = 12
d = 2
e = 20

# datatype bool -> Boolean Value 
# and, or and the not

# print(x > y and a < y)
# print(x < y and not a > y)
print(x > y or not a < d)

x = 2
y = 3
z = 12

print(x < y >= z)

# print(x < y and y <= z)
# is operator

x = 1001
y = 1001
z = 1000
b = z + 1

# print(id(x)) # memory location for our variable
# print(id(y))
# print(id(b))

print(x is b)  # check if the values are the same on memory
print(x is not b) 