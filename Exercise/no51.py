# Find index of an element in tuple
t = (1, 2, 3, 4, 5,6,7,8,9,10)
element = int(input("Enter an element to find index: "))
try:
    index = t.index(element)
    print("Index of element:", index)
except ValueError:
    print("Element not found in tuple")