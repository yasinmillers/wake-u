# Find index of an element in tuple
t = tuple(input("Enter elements of tuple separated by spaces: ").split())
element = int(input("Enter an element to find index: "))
try:
    index = t.index(element)
    print("Index of element:", index)
except ValueError:
    print("Element not found in tuple")