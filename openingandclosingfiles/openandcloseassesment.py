Exercise 1: Read and Display Assessment Scores
Create a text file (scores.txt) containing a list of assessment scores (one score per line). Write a Python program to read the scores from the file, calculate the average score, and display it on the console.
def cal_average(scores):
  total = sum(scores)
  average = total / len(scores)
  return average

scores = []
total = 0
with open("texts/scores.txt", 'r') as f:
  for i in f.readlines():
    if i == "\n":
      continue
    else:
      i = int(i)
      scores.append(i)

average_scores = cal_average(scores)

print(average_scores)