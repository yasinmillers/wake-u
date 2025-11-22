fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
  
fruit = ["apple1", "banana2", "cherry3"]
for x in fruit:
  if x == "banana":
    continue
  print(x)
for i in range(2,14,3):
  print(i)
  
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)    