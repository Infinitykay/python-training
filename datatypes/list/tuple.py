# tuples
fruits = ( "Mango", "Banana", "Pawpaw", "Apple", "Orange")
items = (1, True, "Bukunmi", 3.1)
names = ["Bukunmi", "Mr.Akeem", "Anuoluwa"]
# fruits.append("Grape")
# fruits.remove("Banana")
# fruits[1] = "Guava"
names = tuple(names)
fruits = list(fruits)
fruits.append("Watermelon")
fruits.remove("Mango")
fruits[2] = "Pineapple"
fruits = tuple(fruits)
print(names)
print(fruits)