#Count occurrences of element in tuple
t = (1, 2, 3, 4, 5,7,8,8,8,8,4,8,4,6,6,5)
element = int(input("Enter an element to count: "))
count = t.count(element)
print("Count of element:", count)