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