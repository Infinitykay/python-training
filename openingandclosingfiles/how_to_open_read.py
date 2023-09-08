# Read and writing of files
# f = open('tolu.txt')

# with open("tolu.txt") as f:
#   print("File opened and close")  
#   print(f.read())
with open('texts/tolu.txt')as k:
  print(k.read())

# readline will pick chars
# readlines will pick line
# read will pick the entire content

with open('texts/dog_breeds.txt', 'r') as reader:
    # Read and print the entire file line by line
    line = reader.readline()
    while line != '':  # The EOF char is an empty string
        print(line, end='')
        line = reader.readline()
        print(line)


with open('texts/tolu.txt', 'r') as reader:
    # Read and print the entire file line by line
    dog_content = reader.readlines()
    print(dog_content)

# writing to a file
with open('texts/dog_breeds.txt', 'w') as dogs:
    dog_content_reversed = reversed(dog_content)
    # print(dog_content_reversed)
    for breed in dog_content_reversed:
      dogs.write(breed)

foods = ["Amala", "Gbegiri", "Ewedu"]

with open("texts/food.txt", 'w') as f:
  for food in foods:
    f.write(f"{food}\n")