# Find index of an element in tuple
t = tuple(input("Enter elements of tuple separated by spaces: ").split())
element = input("Enter an element to find index: ")
if element in t:
    index = t.index(element)
    print("Index of element:", index)
else:
    print("Element not found in tuple")