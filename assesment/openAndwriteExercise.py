# Create a Python program that prompts the user to enter a sentence and appends it to a file named 
# "sentences.txt." If the file doesn't exist, create it.
sentence = []
running = True
print('This code stores new sentence in next line. ')
while running:
 sentenceInput = input('Enter a sentence:  ')
 sentence.append(sentenceInput)
 prompt = input('Do you want to add a new sentence? Y for YES N for NO'
 )
 if prompt.upper() == "Y":
   continue
 else:
   print('Code exited')
   break
with open('sentence.txt', 'w') as f:
  for n in sentence:
   f.write(f'{n} \n')

# Exercise 2: Write Assessment Results to a File
# Create a program that prompts the user to enter assessment results (e.g., test scores) for multiple students. Store the results in a text file (results.txt) with each line containing a student's name and their score. Ensure that the program can handle multiple students' data.

testScore = []
running = True

name = []
print(
  "This code collects student's name and score and store in score.txt file")
while running:
  nameIn = input("Enter Student's name -> ")
  testScoreIn = int(input('Enter student test score--> '))
  name.append(nameIn)
  testScore.append(testScoreIn)
  prompt = input(
    "Do you want to add another assesment result? if YES select 'Y' if No select 'N' "
  )
  if prompt.upper() == "Y":
    print("Test continues...")
    continue
  else:
    print("Code exited")
    break

with open("score.txt", 'w') as f:
  multi_tabs = "\t" * 9
  f.write(f"Names {multi_tabs} Scores\n")
  for n, s in zip(name, testScore):
    f.write(f"{n} {multi_tabs}\t {s}\n")

# Create a Python program that copies the contents of one file (e.g., "source.txt") to another file (e.g., "destination.txt"). Ensure that the destination file is created if it doesn't exist.

# lists = [1, "tomato", True, "32", 90]

# for i, r in enumerate(lists):
#   print(f'{r} is in position {i}')

with open("source.txt", 'r') as source:
  print("file has been opened")
  with open('destination.txt', "w") as destination:
    for index, src in enumerate(source):
      if index < 3:
        destination.write(src)
    print("file has been written")