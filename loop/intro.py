# loops in python

# for and while

# items = [1, 23, "age", "names"]
# while items:
#   print(items.pop(0))
#   if len(items) == 2:
#     break


n = 10
while n > 0:
    n -= 1
    if n == 5:
      continue
    elif n == 2:
      break
    else:
      print(n)
else:
  print('Loop ended.')

  # infinite loops
i = 0
value = True
while value:
  print("I am infinite")
  i += 1
  if i < 2000:
    print(f'Loop count is now {i}')
  else:
    value = False

while False:
  print("Hello here")
# Nested while loops

a = ['foo', 'bar']
while len(a): # first iteration
    print(a.pop(0))
    b = ['baz', 'qux'] 
    while len(b): #all iterations
        print('>', b.pop(0))


# True = 1 
# False = 0