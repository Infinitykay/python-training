# Exercise 2: Write Assessment Results to a File
# Create a program that prompts the user to enter assessment results (e.g., test scores) for multiple students. Store the results in a text file (results.txt) with each line containing a student's name and their score. Ensure that the program can handle multiple students' data.

testScore = []
running = True

name = []
print("This code collects student's name and score and store in score.txt file")
while running:
  nameIn = input("Enter Student's name -> ")
  testScoreIn = int(input('Enter student test score--> '))
  name.append(nameIn)
  testScore.append(testScoreIn)
  prompt = input("Do you want to add another assesment result? if YES select 'Y' if No select 'N' ")
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